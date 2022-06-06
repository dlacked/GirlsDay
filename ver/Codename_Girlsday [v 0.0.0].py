from tkinter import *
from random import *

def jokbo(c1, c2):
    cardlist = [c1, c2]
    score = None
    if 9 in cardlist and 29 in cardlist:
        score = 28 #삼팔광땡
        print("삼팔광땡")
    elif 1 in cardlist and 29 in cardlist:
        score = 27 #일팔광땡
        print("일팔광땡")
    elif 1 in cardlist and 9 in cardlist:
        score = 26 #일삼광땡
        print("일삼광땡")
    elif ((cardlist[0] >= 1 and cardlist[0] <= 4) and (cardlist[1] >= 5 and cardlist[1] <= 8)) or ((cardlist[0] >= 5 and cardlist[0] <= 8) and (cardlist[1] >= 1 and cardlist[1] <= 4)):
        score = 15 #알리
        print("알리")
    elif ((cardlist[0] >= 1 and cardlist[0] <= 4) and (cardlist[1] >= 13 and cardlist[1] <= 16)) or ((cardlist[0] >= 13 and cardlist[0] <= 16) and (cardlist[1] >= 1 and cardlist[1] <= 4)):
        score = 14 #독사
        print("독사")
    elif ((cardlist[0] >= 1 and cardlist[0] <= 4) and (cardlist[1] >= 33 and cardlist[1] <= 36)) or ((cardlist[0] >= 33 and cardlist[0] <= 36) and (cardlist[1] >= 1 and cardlist[1] <= 4)):
        score = 13 #구삥
        print("구삥")
    elif ((cardlist[0] >= 1 and cardlist[0] <= 4) and (cardlist[1] >= 37 and cardlist[1] <= 40)) or ((cardlist[0] >= 37 and cardlist[0] <= 40) and (cardlist[1] >= 1 and cardlist[1] <= 4)):
        score = 12 #장삥
        print("장삥")
    elif ((cardlist[0] >= 13 and cardlist[0] <= 16) and (cardlist[1] >= 37 and cardlist[1] <= 40)) or ((cardlist[0] >= 37 and cardlist[0] <= 40) and (cardlist[1] >= 13 and cardlist[1] <= 16)):
        score = 11 #장사
        print("장사")
    elif ((cardlist[0] >= 13 and cardlist[0] <= 16) and (cardlist[1] >= 21 and cardlist[1] <= 24)) or ((cardlist[0] >= 21 and cardlist[0] <= 24) and (cardlist[1] >= 13 and cardlist[1] <= 16)):
        score = 10 #세륙
        print("세륙")
    if score == None:
        for i in range(1, 11):
            if (cardlist[0] >= 41-i*4 and cardlist[0] <= 44-i*4) and (cardlist[1] >= 41-i*4 and cardlist[1] <= 44-i*4):
                score = 25-i #장땡 ~ 삥땡
                print(f"{10-i+1}땡")
    if score == None:
        score = ((cardlist[0]-1)//4)+1 + ((cardlist[1]-1)//4)+1
        if score >= 20:
            score -= 20
        elif score >= 10:
            score -= 10
        print(f"{score}끗")
    return score

def ingame(): #게임 시작 함수

    buttonimage.destroy()

    while True: #패
        cpu1 = randrange(1, 49)
        cpu2 = randrange(1, 49)
        user1 = randrange(1, 49)
        user2 = randrange(1, 49)
        if (cpu1 != cpu2) and (cpu1 != user1) and (cpu1 != user2) and (cpu2 != user1) and (cpu2 != user2) and (user1 != user2):
            break

    #패에 해당하는 이미지 생성 및 배치
    cpu1c = PhotoImage(file = f"img/{cpu1}.png")
    cpu2c = PhotoImage(file = f"img/{cpu2}.png")
    user1c = PhotoImage(file = f"img/{user1}.png")
    user2c = PhotoImage(file = f"img/{user2}.png")

    cpu1card = Label(image = cpu1c)
    cpu1card.place(x = 15+2, y = 15+2)

    cpu2card = Label(image = cpu2c)
    cpu2card.place(x = 253-93-2, y = 15+2)
    
    user1card = Label(image = user1c)
    user1card.place(x = 15+2, y = 396-140)
    
    user2card = Label(image = user2c)
    user2card.place(x = 253-93-2, y = 396-140)

    #패에 맞는 점수를 부여
    cpuscore = jokbo(cpu1, cpu2)
    userscore = jokbo(user1, user2)
    
    #승패 결정
    if userscore > cpuscore:
        win = PhotoImage(file = "img/win.png")
        winimage = Label(image = win)
        winimage.place(x = 10, y = 170)
    elif userscore == cpuscore:
        draw = PhotoImage(file = "img/draw.png")
        drawimage = Label(image = draw)
        drawimage.place(x = 10, y = 170)
    else:
        lose = PhotoImage(file = "img/lose.png")
        loseimage = Label(image = lose)
        loseimage.place(x = 10, y = 170)
        
    re = PhotoImage(file = "img/re.png")
    rebutton = Button(root, image = re, command = main)
    rebutton.place(x = 140, y = 180)
    
    root.mainloop()
    
def main(): #프로그램 기본 세팅 함수
    global buttonimage
    
    #창 사이즈 조절 
    root.title("dlacked")
    root.maxsize(width = 253, height = 396)
    root.minsize(width = 253, height = 396)

    #이미지 가져옴
    background = PhotoImage(file = "img/bg.png")
    backcard = PhotoImage(file = "img/back.png")

    #백그라운드 이미지, 화투패 뒷면 이미지 생성 및 배치
    bgimage = Label(image = background)
    bgimage.place(x = -2, y = -2)

    backimage1 = Label(image = backcard)
    backimage1.place(x = 15+2, y = 15+2)

    backimage2 = Label(image = backcard)
    backimage2.place(x = 15+2, y = 396-140)

    backimage3 = Label(image = backcard)
    backimage3.place(x = 253-93-2, y = 15+2)

    backimage4 = Label(image = backcard)
    backimage4.place(x = 253-93-2, y = 396-140)

    #시작 버튼 생성 및 배치
    startbutton = PhotoImage(file = "img/start.png")
    buttonimage = Button(root, image = startbutton, command = ingame)
    buttonimage.place(x = 63, y = 170)
    
    root.mainloop()


root = Tk()
main()


