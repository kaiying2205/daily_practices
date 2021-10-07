# https://www.reddit.com/r/dailyprogrammer/comments/nucsik/20210607_challenge_393_easy_making_change/

def change(x):
    q = 0
    for i in [500,100,25,10,5,1]:
        q = q + x // i
        r = x % i
        x = r
    return q

v1 = change(123456)
print(v1)
