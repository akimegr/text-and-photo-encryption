from PIL import Image
import random as rn

def cez():
    for key in range(0, 255, 25):
        im = Image.open(r"C:\pyCharm curs\cezar\tiger.png")
        img = im.load()
        w,h = im.size
        for x in range(0,w):
            for y in range(0,h):
                (r,g,b) = img[x,y]
                r,g,b = (r+key)%255, (g+key)%255, (b+key)%255
                img[x,y] = (r,g,b)

        im.save((r"C:\pyCharm curs\cezar\tiger"+str(key)+".png"))


def vinz():
    im = Image.open(r"C:\pyCharm curs\cezar\tiger.png")

    w, h = im.size
    keys = [
        [rn.randint(0,255) for i in range(10)],
        [rn.randint(0,255) for i in range(100)],
        [rn.randint(0,255) for i in range(1000)],
        [rn.randint(0,255) for i in range(w*h)]
        ]

    for ik in range(0, len(keys)):
        im = Image.open(r"C:\pyCharm curs\cezar\tiger.png")
        img = im.load()

        w,h = im.size
        key = keys[ik]
        k = key*(w*h//len(key)+1)*3
        i = 0
        for x in range(0,w):
            for y in range(0,h):
                (a, b, c) = img[x,y]
                a,b,c = (a+k[i])%255, (b+k[i+1])%255, (c+k[i+2])%255
                img[x,y] = (a,b,c)
                i+=3
            im.save(r"C:\pyCharm curs\cezar\tiger99" + str(ik)+".png")


def aff():
    k2 = int(input("Введите ключ номер два: "))
    for key in range(0, 255, 25):
        im = Image.open(r"C:\pyCharm curs\cezar\tiger.png")
        img = im.load()
        w,h = im.size
        for x in range(0,w):
            for y in range(0,h):
                (r,g,b) = img[x,y]
                r,g,b = (r+key)*k2%255, (g+key)*k2%255, (b+key)*k2%255
                img[x,y] = (r,g,b)

        im.save((r"C:\pyCharm curs\cezar\tigerAFF"+str(key)+".png"))

vinz()
cez()
aff()