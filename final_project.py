#   In this project, you will develop a Python Command Line Interface (CLI) tool that 
#   facilitates file manipulation and directory navigation,similar to command-line 
#   functionalities in Unix-like operating systems. A key component of your tool will 
#   be an advanced logs system that tracks each command's usage.

#   Python CLI Tool for File Manipulation
#   You are required to implement the following commands in your CLI tool:
#     1. ls[path] —List directory contents at `path`, or the current directory if no `path` is given.
#     2. cd [path] —Change the working directory to `path`.
#     3. mkdir[path] —Create a new directory at `path`.
#     4. rmdir[path] —Remove the directory at `path` if it is empty.
#     5. rm[file] —Remove the file specified by `file`.
#     6. rm-r [directory] —Remove the directory at `directory` and its contents recursively.
#     7. cp[source] [destination] —Copy a file or directory from `source` to `destination`.
#     8. mv [source] [destination] —Move a file or directory from `source` to `destination`.
#     9. find [path] [pattern] —Search for files or directories matching `pattern` starting from `path`.
#    10. cat [file] —Output the contents of the file `file`.

#   Logs file:
#   Log each command, its arguments, the time of execution, and the outcome (success or error).
#   The log file should be human-readable and well-organized for ease of analysis and debugging.
#   Points:
#   Use the `argparse` module to parse command-line arguments.
#   Each command should be a function.
#   Handle exceptions and provide clear error messages.
#   write comment for your code.
#   Prepare a `README.md` file that documents the setup of the project

# Import the argparse module and the os module
import argparse
import sys
import os


# Create a parser 
parser = argparse.ArgumentParser(description="A Python CLI tool for file manipulation")
#--------------------------   ls  -------------------------
def ls(path):   # List the directory contents at path, or the current directory if no path is given
    try:
        # If path is not given, use the current working directory
        if not path:
            path = os.getcwd()
        files = os.listdir(path)
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error: {e}")    # Handle error messages
 #--------------------------   cd  -------------------------          
def cd(path):   # Change the working directory to path
    try:
        os.chdir(path)
        print(os.getcwd())
    except Exception as e:
        print(f"Error: {e}")    # Handle error messages
#--------------------------   mkdir  -------------------------    
def mkdir(path):     # Create a new directory at path
    try:
        os.mkdir(path)
        print(f"Created directory {path}")
    except Exception as e:
        print(f"Error: {e}")    # Handle error messages
        
#--------------------------   rmdir  -------------------------
def rmdir(path):      # Remove the directory at path if it is empty
    
    try:
        os.rmdir(path)
        print(f"Removed directory {path}")
        log("rmdir", path, "success")
    except Exception as e:
        print(f"Error: {e}")      # Handle error messages
        

#--------------------------   rm  -------------------------
def rm(file):          # Remove the file specified by file
    
    try:
        os.remove(file)
        print(f"Removed file {file}")
    except Exception as e:
        print(f"Error: {e}")     # Handle error messages
    
#--------------------------   rm_r  -------------------------
def rm_r(directory):    # Remove the directory at directory and its contents 
    
    try:
        import shutil
        #The shutil module offers a number of high-level operations on files and collections of files. 
        #In particular, functions are provided which support file copying and removal. 
        #For operations on individual files, see also the os module.
        shutil.rmtree(directory)
        print(f"Removed directory {directory} and its contents ")
    except Exception as e:
        print(f"Error: {e}")     # Handle error messages
    

#--------------------------   cp  -------------------------
def cp(source, destination):      #Copy a file or directory from source to destination
    # Copy a file or directory from source to destination
    try:
        import shutil     # Import the shutil module
        # Copy the file or directory from source to destination
        shutil.copytree(source, destination) if os.path.isdir(source) else shutil.copy(source, destination)
        print(f"Copied {source} to {destination}")
    except Exception as e:
        print(f"Error: {e}")
    
#--------------------------   mv  -------------------------
def mv(source, destination):     # Move a file or directory from source to destination
   
    try:
        import shutil                              # Import the shutil module
        shutil.move(source, destination)           # Move the file or directory from source to destination
        print(f"Moved {source} to {destination}")
    except Exception as e:
        print(f"Error: {e}")
    

#--------------------------   find  -------------------------
def find(path, pattern):        # Search for files or directories matching pattern starting from path
    try:
        # The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell,
        # although results are returned in arbitrary order. 
        # No tilde expansion is done, but *, ?, and character ranges expressed with [] will be correctly matched.
        # This is done by using the os.scandir() and fnmatch.fnmatch() functions in concert,
        # and not by actually invoking a subshell.
        import glob
        # Get the list of files or directories matching pattern starting from path
        matches = glob.glob(os.path.join(path, pattern), recursive=True)
        for match in matches:
            print(match)
    except Exception as e:
        # Handle exceptions and provide clear error messages
        print(f"Error: {e}")
    
    #--------------------------   cat  -------------------------
def cat(file):            # Output the contents of the file file
    try:
       
        with open(file, "r") as f:       # Read the file contents
            contents = f.read()
            print(contents)     # Print the file contents
       
        #log("cat", file, "success")
    except Exception as e:
        # Handle exceptions and provide clear error messages
        print(f"Error: {e}")
    
#--------------------------   log command  -------------------------
def log_command(line):
    import datetime
    with open("commands.log", "a") as file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d")
        file.write(f"{time_now}: {line}\n")

#--------------------------   main body  -------------------------
subparsers = parser.add_subparsers(dest="command")

ls_parser = subparsers.add_parser("ls", help="List directory contents")         # Add a subparser for the ls comman
ls_parser.add_argument("path", nargs="?", default="", help="The path to list")  # Add an optional argument for the path


cd_parser = subparsers.add_parser("cd", help="Change the working directory")    # Add a subparser for the cd command
cd_parser.add_argument("path", help="The path to change to")                    # Add a required argument for the path


mkdir_parser = subparsers.add_parser("mkdir", help="Create a new directory")    # Add a subparser for the mkdir command
mkdir_parser.add_argument("path", help="The path to create")                    # Add a required argument for the path


rmdir_parser = subparsers.add_parser("rmdir", help="Remove an empty directory")  # Add a subparser for the rmdir command
rmdir_parser.add_argument("path", help="The path to remove")                     # Add a required argument for the path

rm_parser = subparsers.add_parser("rm", help="Remove a file")                   # Add a subparser for the rm command
rm_parser.add_argument("file", help="The file to remove")                       # Add a required argument for the file


rm_r_parser = subparsers.add_parser("rm-r", help="Remove a directory and its contents")  # Add a subparser for the rm-r command
rm_r_parser.add_argument("directory", help="The directory to remove")                    # Add a required argument for the directory


cp_parser = subparsers.add_parser("cp", help="Copy a file or directory")     # Add a subparser for the cp command
cp_parser.add_argument("source", help="The source file or directory")        # Add two required arguments for the source and destination
cp_parser.add_argument("destination", help="The destination file or directory")


mv_parser = subparsers.add_parser("mv", help="Move a file or directory")     # Add a subparser for the mv command
mv_parser.add_argument("source", help="The source file or directory")        # Add two required arguments for the source and destination
mv_parser.add_argument("destination", help="The destination file or directory")


find_parser = subparsers.add_parser("find", help="Search for files or directories matching")  # Add a subparser for the find command
find_parser.add_argument("path", help="The path to start from")                               # Add two required arguments for the path and pattern
find_parser.add_argument("pattern", help="The pattern to match")


cat_parser = subparsers.add_parser("cat", help="Output the contents of a file")     # Add a subparser for the cat command
cat_parser.add_argument("file", help="The file to output")                           # Add a required argument for the file

# Parse the command-line arguments
args = parser.parse_args()
command_line = " ".join(sys.argv)
log_command(command_line)

# Execute the corresponding function based on the command
if args.command == "ls":
    ls(args.path)
elif args.command == "cd":
    cd(args.path)
elif args.command == "mkdir":
    mkdir(args.path)
elif args.command == "rmdir":
    rmdir(args.path)
elif args.command == "rm":
    rm(args.file)
elif args.command == "rm-r":
    rm_r(args.directory)
elif args.command == "cp":
    cp(args.source, args.destination)
elif args.command == "mv":
    mv(args.source, args.destination)
elif args.command == "find":
    find(args.path, args.pattern)
elif args.command == "cat":
    cat(args.file)
else:
    print("command not found")    # Print a usage message if no command is given