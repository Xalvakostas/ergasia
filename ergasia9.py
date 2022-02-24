import binascii


allowed_chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
f = open("two_cities_ascii.txt", "r",encoding='ascii')
data= f.read()
filtered_txt= ""
for c in data:
    if c in allowed_chars:
        filtered_txt = filtered_txt + c.lower()
f.close()
ones = 0 
zeros =0 
max_word_one=0
max_word_zero = 0 
maxones=0
maxzeros=0
words= filtered_txt.split()
print(words)
j =0
for word in words :
    ones = 0 
    zeros =0 
    byte_array = word.encode()
    binary_int = int.from_bytes(byte_array,"big")
    Binary = bin(binary_int)
    print(Binary)
    if j ==0 :
        max_word_a =Binary
        max_word_b =Binary
        j=j+1
    for i in range(len(Binary)-1):
        if str(Binary[i])=='1' and str(Binary[i+1])=='1' :
            ones = ones +1
            if max_word_one < ones :
                max_word_a =Binary
                max_word_one= ones
        else:
            ones=0
               
        if str(Binary[i])=='0' and str(Binary[i+1])=='0' :
            zeros = zeros +1
            if max_word_zero <zeros :
                max_word_b =Binary
                max_word_zero=zeros
        else :            
            zeros =0
            
print("ones"+max_word_a+" fores : "+ str(max_word_one))
print("zeros"+max_word_b+" fores : "+ str(max_word_zero))
