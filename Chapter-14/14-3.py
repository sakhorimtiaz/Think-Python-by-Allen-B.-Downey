#for pycharm
import os

def walk(directory,extension):
    d={}
    for name in os.listdir(directory):
        path=os.path.join(directory,name)
        if os.path.isfile(path) and os.path.splitext(path)[1]==extension: #checking specific file type
            file_hash=hash_function(path)
            if file_hash not in d:
                d[file_hash]=[path]
            else:
                d[file_hash].append(path)

        elif os.path.isdir(path):
            sub_dict=walk(path,extension)
            # Merge the results into the main dictionary
            for h, paths in sub_dict.items():
                if h in d:
                    d[h].extend(paths)  # Append existing paths
                else:
                    d[h] = paths  # Add new hash and its paths
    return d

def hash_function(file):
    cmd = 'certutil -hashfile "' + file + '" MD5'  # Wrapping file path in quotes to handle spaces
    #print(cmd)
    fp = os.popen(cmd)
    res = fp.read()
    fp.close()
    #print(res)

    # Extract the hash value (second line in the output)
    hash_lines = res.splitlines()
    #print(hash_lines)
    if len(hash_lines) > 1 and len(hash_lines[1])==32: #checking the 2nd line is of 32 character hash
        #print(len(hash_lines[1]))
        return hash_lines[1]
    else:
        return None

if __name__=="__main__":
    dic = walk(r"C:\Users\THINKPAD\Desktop\books", ".pdf")
    for key, files in dic.items():
        if len(files) > 1:
            print(f"for {key} we get {files}")
            for i in range(len(files) - 1):
                file1 = files[i]
                file2=files[i + 1]

                fc_result = os.system(f'fc "{file1}" "{file2}"') #using fc instead of diff for windows
                if fc_result == 0:
                    print(f"Confirmed duplicate: {file1} and {file2}")

#using git bash
#using "diff"

#git bash setup

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ source~/.bashrc
bash: source~/.bashrc: No such file or directory

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ source ~/.bashrc
THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ source ~/.bashrc

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ conda --version
bash: conda: command not found

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ ^C

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ conda init bash
bash: conda: command not found

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ conda init bash
bash: conda: command not found

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ nan0 ~/.bashrc
bash: nan0: command not found

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ nano ~/.bashrc

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ source ~/.bashrc

THINKPAD@DESKTOP-RFL7FL2 MINGW64 ~
$ conda --version
conda 24.5.0
C:\Users\THINKPAD>

C:\Users\THINKPAD>cd "C:\Users\THINKPAD\PycharmProjects\linearegression\12debugging"

C:\Users\THINKPAD\PycharmProjects\linearegression\12debugging>python 14-3.py

#python code 
import os

def walk(directory,extension):
    d={}
    for name in os.listdir(directory):
        path=os.path.join(directory,name)
        if os.path.isfile(path) and os.path.splitext(path)[1]==extension: #checking specific file type
            file_hash=hash_function(path)
            if file_hash not in d:
                d[file_hash]=[path]
            else:
                d[file_hash].append(path)

        elif os.path.isdir(path):
            sub_dict=walk(path,extension)
            # Merge the results into the main dictionary
            for h, paths in sub_dict.items():
                if h in d:
                    d[h].extend(paths)  # Append existing paths
                else:
                    d[h] = paths  # Add new hash and its paths
    return d

def hash_function(file):
    cmd = 'certutil -hashfile "' + file + '" MD5'  # Wrapping file path in quotes to handle spaces
    #print(cmd)
    fp = os.popen(cmd)
    res = fp.read()
    fp.close()
    #print(res)

    # Extract the hash value (second line in the output)
    hash_lines = res.splitlines()
    #print(hash_lines)
    if len(hash_lines) > 1 and len(hash_lines[1])==32: #checking the 2nd line is of 32 character hash
        #print(len(hash_lines[1]))
        return hash_lines[1]
    else:
        return None

if __name__=="__main__":
    dic = walk(r"C:\Users\THINKPAD\Desktop\books", ".pdf")
    for key, files in dic.items():
        if len(files) > 1:
            print(f"for {key} we get {files}")
            for i in range(len(files) - 1):
                file1 = files[i]
                file2=files[i + 1]

                diff_result = os.system(f'diff "{file1}" "{file2}"') #using fc instead of diff for windows
                if diff_result == 0:
                    print(f"Confirmed duplicate: {file1} and {file2}")
