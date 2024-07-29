with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
    # Read the file into a variable called wiki
    #the file object in Python is iterable and it naturally iterates line by line
    for line in file:
        if len(line)>=20:
            print(line)


