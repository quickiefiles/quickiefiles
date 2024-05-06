import requests
import os

# git repo located at: https://github.com/quickiefiles/quickiefiles
# check if local and global installation match (excluding some files)

if os.path.exists("../.git"):
    if os.path.exists("./version"):
        with open("./version", "r") as file:
            version_local = file.read()
            version_global = requests.get("https://raw.githubusercontent.com/quickiefiles/quickiefiles/main/testing/version").text.strip()
            
        print(f"local version is  {version_local}")
        print(f"global version is {version_global}")
        
        if not version_global == version_local:
            print("versions do not match, updating...")
            os.system(f"git pull")
            
        else:
            print("versions match, continuing startup process...")
            cwd = os.getcwd()
            os.system(f"python3 {cwd}/explorer.py")

    else:
        print("file 'version' does not exist, performing repair...")
        # make python file outside of quickiefiles folder
        # run that python file
        # that python file will delete the quickiefile folder contents and clone a new
        # install.

else:
    print("folder '.git' does not exist, performing repair...")
    # make python file outside of quickiefiles folder
    # run that python file
    # that python file will delete the quickiefile folder contents and clone a new
    # install.
