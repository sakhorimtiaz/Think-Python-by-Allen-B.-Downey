def cumsum(t):
    cumulative_sum=0
    for i in t:
        cumulative_sum=cumulative_sum+i
    print (cumulative_sum)
    return cumulative_sum

cumsum([1,2,4,5.6])