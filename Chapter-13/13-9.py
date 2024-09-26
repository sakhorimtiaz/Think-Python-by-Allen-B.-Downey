# I have used two methods for slope calculation, but using linear-regression is more accurate
import string
import math
import matplotlib.pyplot as plt #or, from matplotbib import pyplot
import scipy.stats as st #or, from spicy import stats
def word_histogram(book):
    with open(book) as file:
        d={}
        process=False
        translation_table=str.maketrans("","",string.punctuation)
        for line in file:
            if "*** START OF THE PROJECT GUTENBERG" in line:
                process=True
                continue
            if process:
                words=line.split()
                for word in words:
                    cleaned_word=word.translate(translation_table).lower()
                    if cleaned_word:
                        d[cleaned_word]=d.get(cleaned_word,0)+1
        return d

def sorted_dictionary(h):
    return sorted(h.items(),key=lambda x: (-x[1],x[0]))
def print_word_freq_rank(sorted_words):
    log_rank=[]
    log_frequency=[]
    for i in range(len(sorted_words)):
        log_f=math.log(sorted_words[i][1])
        log_r=math.log(i+1)
        log_rank.append(log_r)
        log_frequency.append(log_f)

        #print(f"word: '{sorted_words[i][0]}' with log f: {log_f} with log r: {log_r}")
    return (log_rank,log_frequency)
def graph(g):
    x= g[0]
    y= g[1]
    plt.plot(x,y)
    plt.xlabel("rank(in log)")
    plt.ylabel("frequency(in log)")
    plt.title("Zipf's Law")
    plt.show()

def slope_calculation_without_linregress(g):
    slopes=[]
    x_values=g[0]
    y_values=g[1]
    for i in range(len(x_values)-1):
        x1 = x_values[i]
        x2 = x_values[i + 1]
        y1 = y_values[i]
        y2 = y_values[i+1]
        slope=(y2-y1)/(x2-x1)
        slopes.append(slope)
    res=sum(slopes)/len(slopes)
    return res


def slope_calculation(g):
    x_values = g[0]
    y_values = g[1]

    # Using linear regression for a best-fit slope
    slope = st.linregress(x_values, y_values)
    return slope

if __name__=="__main__":
    histogram = word_histogram("C:\\Users\\THINKPAD\\Downloads\\emma.txt")
    sorted_words = sorted_dictionary(histogram)
    word_rank_freq=print_word_freq_rank(sorted_words)
    print(slope_calculation_without_linregress(word_rank_freq))
    print(slope_calculation(word_rank_freq))
    graph(word_rank_freq)
