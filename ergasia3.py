import string

allowed_chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
f = open("two_cities_ascii.txt", "r",encoding='ascii')
data= f.read()
filtered_txt= ""
for c in data:
    if c in allowed_chars:
        filtered_txt= filtered_txt +c
f.close()

words= filtered_txt.split()

for i in range(len(words)):
    if i < len(words):
        j=0
        success=True
        while success and j<len(words):
            if len(words[i])+len(words[j]) == 20:
                words.pop(i)
                words.pop(j)
                success=False
            else:
                j+=1
words.sort(key = len)

#print(words)
#print(len(words))
for i in range(len(words)):
    k=len(words[i])

total= []
total = [[] for _ in range(k)]
t=0
for i in range(len(words)):
    if len(words[i])== t:
        total[t].append(1)
    else:
        t+=1

for i in range(len(total)):
    total[i]=sum(total[i])

for i in range(len(total)):
    if total[i]!=0:
        print( total[i],"Λεξεις",i+1,"γραμμάτων")




    

