import turtle
turtle.screensize(100,100)
turtle.bgcolor('orange')
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t2.hideturtle()
t2.up()
t2.goto(0,250)

t2.write('HANG MAN', font = ('algerian',30))
t1.ht()
t1.pensize(3)
t1.speed(0)
import random
vowels = ['A','E','I','O','U',' ' ]
copy = ['A','E','I','O','U',' ' ]
m = ["THE PAST","ON THE EDGE OF TOMORROW","JUMANJI ","NIGHT AT THE MUSEUM","STORM","FAST AND FURIOUS","HELP",
      "SHARK","KHILADI KA CHALLENGE","RAJ MAHAL","MADAGASCAR","LIFE OF PI",
      "SHOLAY","TEKKEN","SHREK","SON OF ROBINSON","KUNG FU PANDA","BAHUBALI ",'GOOD NEWZ','ARMY','MUMBAI KI KIRAN BEDI','BAADSHAH',
     'MELA', 'SANDWICH','ALIGATOR','RACE GURRAM','MENTAL','GANGSTER','MOST WANTED','KABHI KUSHI KABHI GAM','DON', 'SINGH IS BLING',
     'TUTAK TUTAK TUTIYA','MAHABHARAT' , 'TRAIN TO BUSAN' , 'AVENGERS INFINITY WAR','NEMO','PUSS IN BOOTS' , 'HOME ALONE' , 'BHOOL BHULAYA',
     'MOHANJODARO']
i = random.randint(0,41)
c = m[i]
emptyplaces = 0
for j in c:
    if j in vowels:
        print(j,end=" ")
    else:
        print("_",end=" ")
        emptyplaces+=1
print()
def aa():
    t1.fd(200)
    t1.goto(100,0)
    t1.left(90)
def bb():
    t1.fd(200)
    t1.right(90)
def cc():
    t1.fd(200)
    t1.penup()
    t1.goto(200,200)
    t1.pendown()
    t1.right(90)
def dd():
    t1.fd(30)
def ee():
    t1.up()
    t1.goto(180,150)
    t1.down()
    t1.circle(20)
    t1.up()
    t1.goto(200,130)
    t1.down()
def ii():
    t1.up()
    t1.goto(190,158)
    t1.dot(10)
    t1.goto(210,158)
    t1.dot(10)
def jj():
    t1.goto(195,138)
    t1.down()
    t1.circle(5)
    t1.up()
    t1.goto(10,-29)
    t1.down()
    t1.write('you lost the game',font=('algerian', 20))

def ff():
    t1. fd(50)
def gg():
    t1.up()
    t1.goto(200,130)
    t1.right(45)
    t1.down()
    t1.fd(20)
    t1.left(180)
    t1.fd(20)
    t1.right(90)
    t1.fd(20)
def hh():
    t1.up()
    t1.goto(200,80)
    t1.right(90)
    t1.down()
    t1.fd(20)
    t1.left(180)
    t1.fd(20)
    t1.right(90)
    t1.fd(20)
i=0
count= 0
while count < 10:
    a  = input("enter the alphabet")
    a = a.upper()
    if a in vowels or len(a)>1:
        print("enter the consonant not vowel")
        print("enter only one alphabet")
    elif a not in c:
        count+=1
        print(10 - count,"chances left")
        ch = [aa,bb,cc,dd,ee,ff,gg,hh,ii,jj]
        ch[i]()
        i+=1
    else:
        copy.append(a)
        N = ''
        for k in c:
            if k in copy:
                N+=k
            else:
                N+=' _ '
        if N == c:
            print(N)
            t1.up()
            t1.goto(0,-30)
            t1.write("YOU HAVE WON THE GAME",font=('algerian',20))
            break
        print(N)
turtle.mainloop()

