import string

def stringSimilarity(s):
    length = len(s)
    answer = length
    start=1
    while start<length-1:
        count=0
        begin = start
        for i in range(length):
            if string.ascii_lowercase.index(s[i])==string.ascii_lowercase.index(s[begin]):
                count+=1
            else:
                break
            begin+=1
        start+=1
        answer+=count    
    return answer+1
    
      s = input()
      result = stringSimilarity(s)
      print(result)
