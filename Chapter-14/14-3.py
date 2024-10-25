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