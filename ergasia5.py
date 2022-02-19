from collections import Counter

allowed_chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
f = open("two_cities_ascii.txt", "r",encoding='ascii')
data= f.read()
filtered_txt= ""
for c in data:
    if c in allowed_chars:
        filtered_txt = filtered_txt + c.lower()
f.close()

words= filtered_txt.split()
#print(words)

Count = Counter(words)
most_occur = Count.most_common(10)
print("οι δέκα δημοφιλέστερες λέξεις ", most_occur)

p2=""
for i in words:
    p2+=i[:2]
    p2+='\n'
f2chars=p2.split()
#print(f2chars)

C=Counter(f2chars)
treis1=C.most_common(3)
print("οι τρεις πρώτοι συνδυασμοί δύο πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις ",treis1)

p3=""
for i in words:
    if len(i)>3:
        p3+=i[:3]
        p3+='\n'
f3chars=p3.split()
#print(f3chars)

C=Counter(f3chars)
treis2=C.most_common(3)
print("οι τρεις πρώτοι συνδυασμοί τριών πρώτων γραμμάτων που αρχίζουν οι περισσότερες λέξεις ",treis2)
