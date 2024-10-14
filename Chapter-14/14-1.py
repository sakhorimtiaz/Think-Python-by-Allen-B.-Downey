#the solution given by the author uses less memory,
def sed(pattern_string,replacement_string,file1,file2):
    try:
        with open(file1, "r") as file1:
            reading = file1.read()
        replaced = reading.replace(pattern_string, replacement_string)
        with open(file2, "w") as file2:
            file2.write(replaced)
    except:
        print("something is wrong")

sed("Emma","KT","C:\\Users\\THINKPAD\\Downloads\\emma.txt","text_write.txt")

