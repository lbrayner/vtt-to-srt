#!/usr/bin/env python3
import argparse
import html
import os
import re
import sys

from pysrt.srtitem import SubRipItem, SubRipTime
from webvtt import WebVTT


def replace_colors(raw_text, colours_arg, tag_name):
    result = raw_text
    for k, v in colours_arg.items():
        regex_string = "<" + tag_name + "(?:\\..*?)?\\." + str(k) + "(?:\\..*?)?>(.*?)</" + tag_name + ">"
        if re.search(regex_string, result) is not None:
            result = re.sub(regex_string, lambda x: replace_color(x, tag_name, v), result)
    return result


def replace_color(x, tag_name, v):
    return ("" if tag_name == "c" else ("<" + tag_name + ">")) \
           + "<font color=\"" + v + "\">" \
           + html.unescape(x.group(1)) \
           + "</font>" \
           + ("" if tag_name == "c" else ("</" + tag_name + ">"))


COLOURS_PATTERN = re.compile(r'::cue\(\.([^)]+)\)\s*{.*?color:(.*?);.*?}')


def main():
    parser = argparse.ArgumentParser(
        description='vtt_to_srt is a command line tool to convert vtt subtitles to srt files')
    parser.add_argument('file', nargs='*',
                        help='a file. The command accepts zero, one or more files as arguments.\n'
                             'For each .vtt, a .srt will be generated in the same folder.\n'
                             'Any other extension is ignored.')
    parser.add_argument('-s', dest='strip', action='store_true', help='strip all tags in output srt')
    args = parser.parse_args()

    if len(args.file) == 0:
        for file in os.listdir():
            if file.endswith(".vtt"):
                args.file.append(file)

    for file in args.file:
        index = 0

        file_name, file_extension = os.path.splitext(file)

        if not file_extension.lower() == ".vtt":
            sys.stderr.write("Skipping %s.\n" % file)
            continue

        srt = open(file_name + ".srt", "w", encoding='utf-8')

        read = WebVTT().read(file)

        colours = dict()
        if args.strip is False:
            for style in read.styles:
                colours_found = COLOURS_PATTERN.findall(style.text)
                colours_classes = list(map(lambda x: x[0], colours_found))
                colours_values = list(map(lambda x: x[1].replace(" ", ""), colours_found))
                colours = dict(zip(colours_classes, colours_values))

        for caption in read.captions:
            index += 1
            start = SubRipTime(0, 0, caption.start_in_seconds)
            end = SubRipTime(0, 0, caption.end_in_seconds)
            caption_text = caption.raw_text
            no_tag_found = True
            if args.strip is False:
                for tag in ['c', 'i', 'b', 'u']:
                    if re.search("<" + tag + "\\..*?>.*?</" + tag + ">", caption_text) is not None:
                        caption_text = replace_colors(caption_text, colours, tag)
                        no_tag_found = False
            if no_tag_found:
                caption_text = html.unescape(caption.text)
            srt.write(SubRipItem(index, start, end, caption_text).__str__() + "\n")


if __name__ == "__main__":
    main()
