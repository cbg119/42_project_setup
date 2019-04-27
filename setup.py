import os
import sys
import errno
import shutil

#edit this with your libft link
GITHUB_LINK = ""

def copy_files(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dst)

def error_exit(error_string):
    print(error_string)
    sys.exit()

if (len(sys.argv) != 3):
    error_exit("Error! Too little or too many arguments!")

if not os.path.isdir(os.path.realpath(sys.argv[2])):
    error_exit("Error! Specified path does not exist!")

if GITHUB_LINK == ""
    error_exit("Error! Github link is empty.")

name = str(sys.argv[1])
path = os.path.realpath(sys.argv[2]) + "/" + name

if os.path.isfile(path) or os.path.isdir(path):
    error_exit("Error! Path + name combo already exists!")

resources = os.path.realpath("./resources") + "/"
os.mkdir(path)

#shutil.copytree demands the dst path be the full copy path (aka the
#dir you want to copy to + the dir_to_copy name. 
copy_files(resources + "Makefile", path)
copy_files(resources + "src", path + "/src")
copy_files(resources + "includes", path + "/includes")

#clone the specified libft
os.chdir(path)
os.system("git clone " + GITHUB_LINK + " libft")
