n="Satya"
v=0
c=0
for ch in n:
    if ch.lower() in "aeiou":
        v+=1
    elif ch.isalpha():
        c+=1
print("vowels: ",v,"consonants: ",c)
