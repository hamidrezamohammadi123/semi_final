#   Python CLI Tool for File Manipulation

file manipulation and directory navigation,similar to command-line functionalities in Unix-like operating systems.

## Setup

1. Ensure Python 3.8 or higher is installed on your system.
2. Place `final_project.py`  in the same directory.


## Usage

Run the `final_project.py` script using Python with the desired arguments:

```
python final_project.py ls[path] 
python final_project.py cd [path]
python final_project.py mkdir[path] 
python final_project.py rmdir[path] 
python final_project.py rm[file] 
python final_project.py rm-r [directory] 
python final_project.py cp[source] [destination] 
python final_project.py mv [source] [destination] 
python final_project.py find [path] [pattern] 
python final_project.py cat [file] 
```

### Arguments

- `--ls[path]`: List directory contents at `path`, or the current directory if no `path` is given.
- `--cd [path]`:Change the working directory to `path`.
- `-- mkdir[path]`:Create a new directory at `path`.
- `-- rmdir[path]`:Remove the directory at `path` if it is empty.
- `-- rm[file]`:Remove the file specified by `file`.
- `--rm-r [directory]`:Remove the directory at `directory` and its contents recursively.
- `-- cp[source] [destination]`:Copy a file or directory from `source` to `destination`.
- `-- mv [source] [destination]`:Move a file or directory from `source` to `destination`.
- `-- find [path] [pattern]`:Search for files or directories matching `pattern` starting from `path`.
- `-- cat [file]`:Output the contents of the file `file`.

## Logs

Logs of the executed commands are stored in `command.log`, with each entry timestamped.
