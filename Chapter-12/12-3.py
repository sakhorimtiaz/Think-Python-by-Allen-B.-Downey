def sort_letters(arg):
    s = sorted(word)
    p = "".join(s)
    return p

with open("C:\\Users\\THINKPAD\\Downloads\\words.txt", "r") as file:
    d = {}  # Dictionary to store original word and its sorted version
    for line in file:
        word = line.strip()  # Remove any leading/trailing whitespace
        w = sort_letters(word)  # Sort the letters of the word, make tuple
        #because we want to create a set of tuples, we cannot make a set of list
        if w not in d:
            d[w]=[word]  #making a dictionary for the values
        else:
            d[w].append(word) #adding new words to the dictionary of values
    #print(d)
    #now d={tuple:list}  {sorted letters, tuple:original word,list}
    #we will look for the list having more than 1 word
    list_of_lists=[]
    for word,group in d.items():
        if len(group)>1:
            l=[len(group),len(word),group] #length of a word is noted for further use
            list_of_lists.append(l)
    #print(list_of_lists)
    #print(list_of_lists[3][2][1])
def check_metathesis(t,n):
    # t is a list of [number of words,number of letters in a word, words list]
    metathesis=set()
    for k in range(len(t)):
        for i in range(t[k][0] - 1):  # 1st one indicates number of words, len(group)
            difference = []
            for j in range(t[k][1]):
                if t[k][2][i][j] != t[k][2][i + 1][j]:
                    difference.append(j)
            if len(difference) == n:
                m=tuple(sorted((t[k][2][i], t[k][2][i + 1])))
                metathesis.add(m)
    print(len(metathesis))
    return metathesis
#t=[[2,6,['winzes', 'wizens']], [2, 5, ['wirer', 'wrier']], [2, 7, ['wisents', 'witness']], [2, 4, ['wist', 'wits']], [2, 8, ['woodlark', 'workload']], [2, 9, ['woodlarks', 'workloads']], [2, 8, ['woodworm', 'wormwood']], [2, 9, ['woodworms', 'wormwoods']], [2, 8, ['worthful', 'wrothful']], [2, 5, ['wrist', 'writs']], [2, 3, ['wye', 'yew']], [2, 4, ['wyes', 'yews']], [2, 8, ['xanthein', 'xanthine']], [2, 9, ['xantheins', 'xanthines']], [2, 6, ['yarely', 'yearly']], [2, 6, ['zaffer', 'zaffre']], [2, 7, ['zaffers', 'zaffres']], [2, 7, ['zaniest', 'zeatins']]]
#t=[2,5,['wirer', 'wrier']]
print(check_metathesis(list_of_lists,2))