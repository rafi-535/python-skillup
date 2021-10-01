text = input()
vowel=['a','e','i','o','u']
count=0
for i in range(0,len(text)):
    for j in range(0,len(vowel)):
        if text[i]==vowel[j]:
            count+=1
print(count)
