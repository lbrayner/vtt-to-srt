#vtt-to-srt subtitle converter

A simple python module to convert vtt files to srt files **_with colours_**!

## ❓ Why this fork?

Some streaming platforms use vtt subtitles with colours. (ie. Auvio)

- [upstream](https://github.com/lbrayner/vtt-to-srt) doesn't convert vtt to srt subtitles when there are colours.  
see [issue #2](https://github.com/lbrayner/vtt-to-srt/issues/2) 


- other tools like `ffmpeg` don't work either  
`ffmpeg -i captions.vtt captions.srt`    
see ticket [subtitles: vtt conversion to srt creates an empty output](https://trac.ffmpeg.org/ticket/9609)


- the library used is `webvtt-py`
it can't convert vtt files with colours to srt files  
see [pull request #39](https://github.com/glut23/webvtt-py/pull/39)

## 💾 Installation

```
pip3 install .
```

## 🖥️ Command line interface

```
usage: vtt_to_srt [-h] [-s] [file [file ...]]

vtt_to_srt  is a command line tool to convert vtt subtitles to srt files

positional arguments:
  file        a file. The command accepts zero, one or more files as arguments. For each .vtt, a .srt will be
              generated in the same folder. Any other extension is ignored.

optional arguments:
  -h, --help  show this help message and exit
  -s          strip all tags in output srt
```

## 📙 Usage

The command accepts zero, one or more files as arguments.  
For each _.vtt_, a _.srt_ will be generated in the same folder.  
Any other extension is ignored.  
If you specify no file, it will convert all _.vtt_ files in the directory.

## Other projects

`vtt_to_srt` is used in a docker image for youtube-dl with vtt to srt conversion
https://github.com/darodi/docker-youtube-dl-vtt-to-srt
