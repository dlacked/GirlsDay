from tkinter import *
from tkinter import messagebox
from random import *
from time import *

global i
i = 0

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


def ingame1(): #게임 시작 함수
    global alert1, usermoneylabel, cpumoneylabel, betmoneylabel, usermoney, cpumoney
    global cpu1, cpu2, user1, user2
    global worlimage, rebutton, i

    i += 1 

    if i >= 2: #ingame1 함수가 두 번 이상 실행되었다면 (잔액 부족 시 게임을 끝내야 함)
        if usermoney < 2000000:
            messagebox.showinfo("패", "게임 진행시 필요한 최소 보유 금액이 부족하여 강제 퇴장당하셨습니다.")
            quit()
        elif cpumoney < 2000000:
            messagebox.showinfo("승", "상대가 게임 진행시 필요한 최소 보유 금액이 부족하여 강제 퇴장당하였습니다.")
            quit()
        else: #이전 화면 구성 정리
            backcard = PhotoImage(file = "img/back.png")
            backimage1 = Label(image = backcard)#cpu1card
            backimage1.place(x = 15+2, y = 15+2)

            backimage2 = Label(image = backcard)#user1card
            backimage2.place(x = 15+2, y = 396-140)

            backimage3 = Label(image = backcard)#cpu2card
            backimage3.place(x = 253-93-2, y = 15+2)

            backimage4 = Label(image = backcard)#user2card
            backimage4.place(x = 253-93-2, y = 396-140)
            worlimage.destroy()
            rebutton.destroy()
            usermoneylabel.destroy()
            cpumoneylabel.destroy()
            betmoneylabel.destroy()
    else:
        buttonimage.destroy() #라벨 제거 메소드 destroy()
        
    while True: #각자의 패 부여
        cpu1 = randrange(1, 49)
        cpu2 = randrange(1, 49)
        user1 = randrange(1, 49)
        user2 = randrange(1, 49)
        if (cpu1 != cpu2) and (cpu1 != user1) and (cpu1 != user2) and (cpu2 != user1) and (cpu2 != user2) and (user1 != user2):
            break

    #사용자와 CPU의 잔액 출력
    usermoneylabel = Label(text = f"User: {usermoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    cpumoneylabel = Label(text = f"CPU: {cpumoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    betmoneylabel = Label(text = f"Betting: {betmoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")

    usermoneylabel.place(x = 0, y = 230)
    cpumoneylabel.place(x = 0, y = 145)
    betmoneylabel.place(x = 130, y = 145)
    

    #패에 해당하는 이미지 생성 및 배치
    
    user1c = PhotoImage(file = f"img/{user1}.png")
    

    #베팅 시작 알림
    alert1 = Label(text = "곧 첫 번째 턴 베팅이 시작됩니다.\n패를 잘 확인하신 후 신중히 베팅해주세요.", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    alert1.place(x = 0, y = 175)
    alert1.after(5000, userbetsetting1) #5000ms 정지 후에 betsetting 함수로 이동
    
    user1card = Label(image = user1c)
    user1card.place(x = 15+2, y = 396-140)
    
    root.mainloop()

def userbetsetting1(): #첫 번째 베팅 설정 관리
    global money, bettingbutton, betting, alert2, alert1
    
    alert1.destroy()
    money = StringVar() #사용자 베팅 입력값
    
    alert2 = Label(text = "베팅 최소금액은 1,000,000\\입니다.", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    alert2.place(x = 22, y = 175)

    betting = Entry(root, width=10, textvariable = money, font = ("맑은 고딕", 10))
    betting.place(x = 73, y = 195)

    bettingbutton = Button(root, text = "bet", command = userbetsys1)
    bettingbutton.place(x = 150, y = 195)

def userbetsys1(): #첫 번째 베팅 시스템
    global usermoney
    global betmoney
    global usermoneylabel, betmoneylabel, betyorn
    
    bet = money.get() 
    bet = int(bet) #사용자가 건 판돈을 담는 변수 bet
    if usermoney >= bet and bet >= 1000000:
        betmoney += bet
        usermoney -= bet
        bettingbutton.destroy()
        betting.destroy()
        alert2.destroy()
        usermoneylabel.destroy()
        betmoneylabel.destroy()
        usermoneylabel = Label(text = f"User: {usermoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
        usermoneylabel.place(x = 0, y = 230)
        betmoneylabel = Label(text = f"Betting: {betmoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
        betmoneylabel.place(x = 130, y = 145)
        betyorn = 1
        cpubetsetting1()
    elif bet == 0:
        messagebox.showinfo("dlacked", "첫 번째 턴은 다이(0\\ 베팅)할 수 없습니다.")
    else:
        messagebox.showinfo("dlacked", "베팅에 실패했습니다. 다시 입력해주세요.")
        
    

def cpubetsetting1(): #첫 번째 CPU 베팅 설정 관리
    global cpumoney
    global betmoney
    global cpumoneylabel, betmoneylabel
    global alert4
    global bet
    alert4 = Label(text = "CPU가 베팅 중입니다...", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    alert4.place(x = 55, y = 185)
    alert4.after(5000, cpubetsys1)
    bet = randrange(1000000, cpumoney-1000000+1)
    betmoney += bet
    cpumoney -= bet
    
def cpubetsys1():
    global cpumoney, cpumoneylabel
    global betmoney, betmoneylabel
    global alert4, alert5, bet
    alert4.destroy()
    betmoneylabel.destroy()
    cpumoneylabel.destroy()
    cpumoneylabel = Label(text = f"CPU: {cpumoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    cpumoneylabel.place(x = 0, y = 145)
    betmoneylabel = Label(text = f"Betting: {betmoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    betmoneylabel.place(x = 130, y = 145)
    alert5 = Label(text = f"CPU가 {bet}\\만큼 베팅하였습니다.", font=("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    alert5.place(x = 15, y = 185)
    alert5.after(3000, ingame2)

def ingame2():
    global user2, alert3, alert5, user2card
    alert5.destroy()    
    user2c = PhotoImage(file = f"img/{user2}.png")
    alert3 = Label(text = "곧 두 번째 턴 베팅이 시작됩니다.\n패를 잘 확인하신 후 신중히 베팅해주세요.", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    alert3.place(x = 0, y = 175)
    alert3.after(5000, userbetsetting2)
    
    user2card = Label(image = user2c)
    user2card.place(x = 253-93-2, y = 396-140)

    root.mainloop()
        
def userbetsetting2():
    global money, bettingbutton, betting, alert2, alert3
    
    alert3.destroy()
    money = StringVar()
    
    alert2 = Label(text = "베팅 최소금액은 1,000,000\\입니다.", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    alert2.place(x = 22, y = 175)

    betting = Entry(root, width=10, textvariable = money, font = ("맑은 고딕", 10))
    betting.place(x = 73, y = 195)

    bettingbutton = Button(root, text = "bet", command = userbetsys2)
    bettingbutton.place(x = 150, y = 195)

def userbetsys2():
    global usermoney
    global betmoney
    global usermoneylabel, betmoneylabel, betyorn
    
    bet = money.get()
    bet = int(bet)
    if usermoney >= bet and bet >= 1000000:
        betmoney += bet
        usermoney -= bet
        bettingbutton.destroy()
        betting.destroy()
        alert2.destroy()
        usermoneylabel.destroy()
        betmoneylabel.destroy()
        usermoneylabel = Label(text = f"User: {usermoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
        usermoneylabel.place(x = 0, y = 230)
        betmoneylabel = Label(text = f"Betting: {betmoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
        betmoneylabel.place(x = 130, y = 145)
        betyorn = 1
        cpubetsetting2()
    elif bet == 0:
        bettingbutton.destroy()
        betting.destroy()
        alert2.destroy()
        betyorn = 0
        end()
    else:
        messagebox.showinfo("dlacked", "베팅에 실패했습니다. 다시 입력해주세요.")
        
    

def cpubetsetting2():
    global cpumoney
    global betmoney
    global cpumoneylabel, betmoneylabel, alert5, bet
    alert5 = Label(text = "CPU가 베팅 중입니다...", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    alert5.place(x = 55, y = 185)
    alert5.after(5000, cpubetsys2)
    bet = randrange(1000000, cpumoney+1)
    betmoney += bet
    cpumoney -= bet

def cpubetsys2():
    global cpumoney, cpumoneylabel
    global betmoney, betmoneylabel
    global alert5, alert6, bet
    alert5.destroy()
    cpumoneylabel.destroy()
    betmoneylabel.destroy()
    cpumoneylabel = Label(text = f"CPU: {cpumoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    cpumoneylabel.place(x = 0, y = 145)
    betmoneylabel = Label(text = f"Betting: {betmoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    betmoneylabel.place(x = 130, y = 145)
    alert6 = Label(text = f"CPU가 {bet}\\만큼 베팅하였습니다.", font=("맑은 고딕", 10), fg = "white", bg = "#00B41E")
    alert6.place(x = 15, y = 185)
    alert6.after(3000, end)
    
def end():
    global cpu1, cpu2, usermoney, betmoney, cpumoney, usermoneylabel, cpumoneylabel, betmoneylabel, alert6, worlimage, rebutton
    global usermoneyfirst, cpumoneyfirst, i, worllabel, betyorn, user2c

    #족보에 맞게 점수 부여
    cpuscore = jokbo(cpu1, cpu2)
    userscore = jokbo(user1, user2) 
    if betyorn == 1:
        alert6.destroy()
        if userscore > cpuscore:
            win = PhotoImage(file = "img/win.png")
            worlimage = Label(image = win)
            worlimage.place(x = 10, y = 170)
            usermoney += betmoney
            betmoney = 0
            betmoneylabel.destroy()
            usermoneylabel.destroy()
            usermoneylabel = Label(text = f"User: {usermoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
            betmoneylabel = Label(text = f"Betting: {betmoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
            usermoneylabel.place(x = 0, y = 230)
            betmoneylabel.place(x = 130, y = 145)
        elif userscore == cpuscore:
            draw = PhotoImage(file = "img/draw.png")
            worlimage = Label(image = draw)
            worlimage.place(x = 10, y = 170)
            betmoney = 0
        else:
            lose = PhotoImage(file = "img/lose.png")
            worlimage = Label(image = lose)
            worlimage.place(x = 10, y = 170)
            cpumoney += betmoney
            betmoney = 0
            betmoneylabel.destroy()
            cpumoneylabel.destroy()
            betmoneylabel = Label(text = f"Betting: {betmoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
            cpumoneylabel = Label(text = f"CPU: {cpumoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
            cpumoneylabel.place(x = 0, y = 145)
            betmoneylabel.place(x = 130, y = 145)
    else:
        user2c = PhotoImage(file = f"img/{user2}.png")
        user2card = Label(image = user2c)
        user2card.place(x = 253-93-2, y = 396-140)
        lose = PhotoImage(file = "img/lose.png")
        worlimage = Label(image = lose)
        worlimage.place(x = 10, y = 170)
        cpumoney += betmoney
        betmoney = 0
        betmoneylabel.destroy()
        cpumoneylabel.destroy()
        betmoneylabel = Label(text = f"Betting: {betmoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
        cpumoneylabel = Label(text = f"CPU: {cpumoney}\\", font = ("맑은 고딕", 10), fg = "white", bg = "#00B41E")
        cpumoneylabel.place(x = 0, y = 145)
        betmoneylabel.place(x = 130, y = 145)
        
    cpu1c = PhotoImage(file = f"img/{cpu1}.png")
    cpu2c = PhotoImage(file = f"img/{cpu2}.png")

    cpu1card = Label(image = cpu1c)
    cpu1card.place(x = 15+2, y = 15+2)

    cpu2card = Label(image = cpu2c)
    cpu2card.place(x = 253-93-2, y = 15+2)

    #돈 증감 출력
    if usermoney - usermoneyfirst >= 0:
        if i >= 2:
            worllabel.destroy()
        worllabel = Label(text = f"+{usermoney - usermoneyfirst}\\", font = ("맑은 고딕", 10), fg = "yellow", bg = "#00B41E")
        worllabel.place(x = 110, y = 230)
    else:
        if i >= 2:
            worllabel.destroy()
        worllabel = Label(text = f"{usermoney - usermoneyfirst}\\", font = ("맑은 고딕", 10), fg = "red", bg = "#00B41E")
        worllabel.place(x = 110, y = 230)

    #re 버튼 출력
    re = PhotoImage(file = "img/re.png")
    rebutton = Button(root, image = re, command = ingame1)
    rebutton.place(x = 140, y = 180)

    root.mainloop()
        
def main(): #프로그램 기본 세팅 함수
    global buttonimage, usermoneyfirst, cpumoneyfirst
    global usermoney, cpumoney, betmoney, worlimage, rebutton
    global betyorn
    usermoneyfirst = randrange(8000000, 12000000)
    cpumoneyfirst = randrange(8000000, 12000000)
    usermoney = usermoneyfirst
    cpumoney = cpumoneyfirst
    betmoney = 0
    betyorn = 0
    
    #창 사이즈 조절 
    root.title("Girl's Day")
    root.maxsize(width = 253, height = 415)
    root.minsize(width = 253, height = 415)

    #이미지 가져옴
    background = PhotoImage(file = "img/bg.png")
    backcard = PhotoImage(file = "img/back.png")

    #백그라운드 이미지, 화투패 뒷면 이미지 생성 및 배치
    bgimage = Label(image = background)
    bgimage.place(x = -2, y = -2)

    backimage1 = Label(image = backcard)#cpu1card
    backimage1.place(x = 15+2, y = 15+2)

    backimage2 = Label(image = backcard)#user1card
    backimage2.place(x = 15+2, y = 396-140)

    backimage3 = Label(image = backcard)#cpu2card
    backimage3.place(x = 253-93-2, y = 15+2)

    backimage4 = Label(image = backcard)#user2card
    backimage4.place(x = 253-93-2, y = 396-140)

    #시작 버튼 생성 및 배치
    startbutton = PhotoImage(file = "img/start.png")
    buttonimage = Button(root, image = startbutton, command = ingame1)
    buttonimage.place(x = 63, y = 170)

    #저작권 표시
    copyrightlabel = Label(text = "Copyright © 2022 dlacked\nall rights reserved.", font = ("맑은 고딕", 6), fg = "white", bg = "#00B41E")
    copyrightlabel.place(x=75, y = 385)
    
    root.mainloop()
    
root = Tk()
main()


