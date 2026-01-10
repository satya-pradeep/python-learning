#anagrams
def angram(s1,s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()
    return sorted(s1)==sorted(s2)
print(angram("sai","iab"))


#non_repeating_string
def non_repeating_ch(s):
    for ch in s:
        if s.count(ch)==1:
            return ch
    return None
print(non_repeating_ch("pradeep"))


#count frequency of character 
def ch_freq(s):
    freq={}

    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq
print(ch_freq("pradeep"))

