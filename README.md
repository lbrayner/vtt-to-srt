# 💾 Installation

```
pip3 install -r requirements.txt
```

# 🖥️ Command line interface

```
usage: vtt-to-srt [-h] [-s] [file [file ...]]

vtt-to-srt is a command line tool to convert vtt subtitles to srt files

positional arguments:
  file        a file. The command accepts zero, one or more files as arguments. For each .vtt, a .srt will be
              generated in the same folder. Any other extension is ignored.

optional arguments:
  -h, --help  show this help message and exit
  -s          strip all tags in output srt
```

# 📙 Usage

The command accepts zero, one or more files as arguments.  
For each _.vtt_, a _.srt_ will be generated in the same folder.  
Any other extension is ignored.  
If you specify no file, it will convert all _.vtt_ files in the directory.
