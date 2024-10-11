def linecounter(filename):
    count=0
    for line in open(filename):
        count+=1
    return count
if __name__=="__main__":
    linecounter("C:\\Users\\THINKPAD\\PycharmProjects\\linearegression\\12debugging\\wc.py")