# https://www.reddit.com/r/dailyprogrammer/comments/njxq95/20210524_challenge_391_easy_the_abacaba_sequence/

#1 needs to print a
#2 print a + b + a
#3 print aba + c + aba
#4 print abacaba + d + abacaba
#5 print abacabadabacaba + e + abacabadabacaba

# v1 = 'a'
# v2 = v1 + 'b' + v1
# v3 = v2 + 'c' + v2
# v4 = v3 + 'd' + v3
# v5 = v4 + 'e' + v4

def seq():
    y=''
    for i in range(0,26):
        c=chr(97+i)
        x=y+c+y
        y=x
    return x

v1=seq()
print(v1)
