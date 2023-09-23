
                                                     # THIS WILL WORK WELL ON PYCHARM


from tkinter import *
from PIL import ImageTk, Image
import winsound

#Music playing in background
# winsound.PlaySound("music.wav",winsound.SND_ASYNC+winsound.SND_LOOP)

#closing the application
def close_m():
   m.destroy()

#making a count variable for counter i.e score
global count
count=0

#counter function for increments
def counter(cot):
    global count
    count=count+cot
    l2 = Label(score, text=count, bg='white', fg='black', font=('Amaranth bold', 50))
    l2.place(x=660, y=325)

#creating the main window
m = Tk()
m.title("QUIZ BUZZ")
m.geometry('1366x768')
m.state("zoomed")

frame1 = Frame(m, width=1366, height=768)
frame1.pack()

frame2 = Frame(m, width=1366, height=768)
frame2.pack()

frame3 = Frame(m, width=1366, height=768)
frame3.pack()

frame4 = Frame(m, width=1366, height=768)
frame4.pack()

frame5 = Frame(m, width=1366, height=768)
frame5.pack()

frame6 = Frame(m, width=1366, height=768)
frame6.pack()

frame7 = Frame(m, width=1366, height=768)
frame7.pack()

frame8 = Frame(m, width=1366, height=768)
frame8.pack()

frame9 = Frame(m, width=1366, height=768)
frame9.pack()

frame10 = Frame(m, width=1366, height=768)
frame10.pack()

frame11 = Frame(m, width=1366, height=768)
frame11.pack()

frame12 = Frame(m, width=1366, height=768)
frame12.pack()

frame13 = Frame(m, width=1366, height=768)
frame13.pack()

frame14 = Frame(m, width=1366, height=768)
frame14.pack()

frame15 = Frame(m, width=1366, height=768)
frame15.pack()

frame16 = Frame(m, width=1366, height=768)
frame16.pack()

frame17 = Frame(m, width=1366, height=768)
frame17.pack()

frame18 = Frame(m, width=1366, height=768)
frame18.pack()

frame19 = Frame(m, width=1366, height=768)
frame19.pack()

frame20 = Frame(m, width=1366, height=768)
frame20.pack()

frame21 = Frame(m, width=1366, height=768)
frame21.pack()

frame22 = Frame(m, width=1366, height=768)
frame22.pack()

frame23 = Frame(m, width=1366, height=768)
frame23.pack()

frame24 = Frame(m, width=1366, height=768)
frame24.pack()

frame25 = Frame(m, width=1366, height=768)
frame25.pack()

frame26 = Frame(m, width=1366, height=768)
frame26.pack()

frame27 = Frame(m, width=1366, height=768)
frame27.pack()

frame28 = Frame(m, width=1366, height=768)
frame28.pack()

frame29 = Frame(m, width=1366, height=768)
frame29.pack()

frame30 = Frame(m, width=1366, height=768)
frame30.pack()

frame31 = Frame(m, width=1366, height=768)
frame31.pack()

score = Frame(m, width=1366, height=768)
score.pack()

for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, score,frame11,frame12,frame13,frame14,frame15,frame16,frame17,frame18,frame19,frame20,frame21,frame22,frame23,frame24,frame25,frame26,frame27,frame28,frame29,frame30,frame31):
    frame.place(width=1366, height=768)


# tkraise is used on frame to bring it to the front of the display order #
def show_frame(frame):
    frame.tkraise()

# Dashboard
show_frame(frame1)
img = Image.open("Dashboard.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame1, image=jpg)
l1.place(width=1366, height=768)

b1 = Button(frame1, text="General Knowledge", bg='#5E17EB', fg="white", font="georgia 15", width=15, border=0,
            command=lambda:show_frame(frame2))
b1.place(x=590, y=290)
b2 = Button(frame1, text="Riddles", bg='#5E17EB', fg="white", font="georgia 15",width=15, border=0, command=lambda:show_frame(frame12))
b2.place(x=590, y=427)
b3 = Button(frame1, text="IQ", bg='#5E17EB', fg="white", width=15, font="georgia 15", border=0, command=lambda:show_frame(frame22))
b3.place(x=590, y=562)


#####################  GENERAL KNOWLEDE  #####################
# Q1 (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame2, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame2, text="Q1: What is the National Bird of \n Pakistan?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=505, y=135)
b1 = Button(frame2, text="A. Eagle", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame3),)
b1.place(x=485, y=255)
b2 = Button(frame2, text="B. Chukar", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame3))
b2.place(x=485, y=364)
b3 = Button(frame2, text="C. Markhor", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame3), counter(1)])
b3.place(x=485, y=473)

# Q2 (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame3, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame3, text="Q2: What is the National Flower of \n Pakistan?", bg="#545454", fg="White",
           font=("Calibri", 20))
l2.place(x=495, y=135)
b1 = Button(frame3, text="A. Rose ", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame4))
b1.place(x=485, y=255)
b2 = Button(frame3, text="B. Daffodil", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame4))
b2.place(x=485, y=364)
b3 = Button(frame3, text="C. Jasmine", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame4), counter(1)])
b3.place(x=485, y=473)

# Q3 (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame4, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame4, text="Q3: What country drinks the most \n coffee per capita?", bg="#545454", fg="White",
           font=("Calibri", 20))
l2.place(x=495, y=135)
b1 = Button(frame4, text="A. Finland", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame5), counter(1)])
b1.place(x=485, y=255)
b2 = Button(frame4, text="B. Netherlands", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame5))
b2.place(x=485, y=364)
b3 = Button(frame4, text="C. Singapore", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame5))
b3.place(x=485, y=473)

# Q4 (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame5, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame5, text="Q4: Which planet in the Milky Way is \n the hottest?", bg="#545454", fg="White",
           font=("Calibri", 20))
l2.place(x=480, y=135)
b1 = Button(frame5, text="A. Venus ", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame6), counter(1)])
b1.place(x=475, y=255)
b2 = Button(frame5, text="B. Mercury", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame6))
b2.place(x=485, y=364)
b3 = Button(frame5, text="C. Earth", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame6))
b3.place(x=485, y=473)

# Q5 (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame6, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame6, text="Q5: Which company was initially \n known as 'Blue Ribbon Sports'? ", bg="#545454", fg="White",
           font=("Calibri", 20))
l2.place(x=500, y=135)
b1 = Button(frame6, text="A. Adidas ", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame7))
b1.place(x=485, y=255)
b2 = Button(frame6, text="B. Nike", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame7), counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame6, text="C. Louis Vuitton", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame7))
b3.place(x=485, y=473)

# Q6 (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame7, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame7, text="Q6: In what country is the Chernobyl \n Nuclear power plant located?", bg="#545454",
           fg="White",
           font=("Calibri", 20))
l2.place(x=485, y=135)
b1 = Button(frame7, text="A. Germany ", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame8))
b1.place(x=485, y=255)
b2 = Button(frame7, text="B. Spain", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame8))
b2.place(x=485, y=364)
b3 = Button(frame7, text="C. Ukraine", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame8), counter(1)])
b3.place(x=485, y=473)

# Q7 (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame8, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame8, text="Q7: Aureolin is shade of what color?", bg="#545454", fg="White",
           font=("Calibri", 20))
l2.place(x=485, y=145)
b1 = Button(frame8, text="A. Green ", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame9))
b1.place(x=485, y=255)
b2 = Button(frame8, text="B. Blue", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame9))
b2.place(x=485, y=364)
b3 = Button(frame8, text="C. Yellow", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame9), counter(1)])
b3.place(x=485, y=473)

# Q8 (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame9, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame9, text="Q8: How many minutes are in a \n full week?", bg="#545454", fg="White",
           font=("Calibri", 20))
l2.place(x=500, y=135)
b1 = Button(frame9, text="A. 11,080 min", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame10))
b1.place(x=485, y=255)
b2 = Button(frame9, text="B. 10,080 min", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame10), counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame9, text="C. 12,080 min", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame10))
b3.place(x=485, y=473)

# Q9 (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame10, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame10, text="Q9: Who has won the most total \n Academy Awards?", bg="#545454", fg="White",
           font=("Calibri", 20))
l2.place(x=485, y=135)
b1 = Button(frame10, text="A. Katharine Hepburn ", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame11))
b1.place(x=485, y=255)
b2 = Button(frame10, text="B. Meryl Streep", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame11))
b2.place(x=485, y=364)
b3 = Button(frame10, text="C. Walt Disney", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame11), counter(1)])
b3.place(x=485, y=473)

# Q1O (GENERAL KNOWLEDE)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame11, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame11, text="Q10: how many bones do we \n have in an ear?", bg="#545454", fg="White",
           font=("Calibri", 20))
l2.place(x=512, y=135)
b1 = Button(frame11, text="A. 5 ", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(score))
b1.place(x=485, y=255)
b2 = Button(frame11, text="B. 4", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(score))
b2.place(x=485, y=364)
b3 = Button(frame11, text="C. 3", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(score), counter(1)])
b3.place(x=485, y=473)

#############################  RIDDLES #####################################
# Q1 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame12, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame12, text="Q1: Which is heavier: A ton of\n bricks or A ton of feathers?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=505, y=135)
b1 = Button(frame12, text="A. Ton of feathers", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame13))
b1.place(x=485, y=255)
b2 = Button(frame12, text="B. Ton of bricks", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame13))
b2.place(x=485, y=364)
b3 = Button(frame12, text="C. Neither", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame13),counter(1)])
b3.place(x=485, y=473)

# Q2 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame13, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame13, text="Q2: What can fill a room but \n takes up no space?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=505, y=135)
b1 = Button(frame13, text="A. Oxygen", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame14))
b1.place(x=485, y=255)
b2 = Button(frame13, text="B. Water", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame14))
b2.place(x=485, y=364)
b3 = Button(frame13, text="C. Light", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame14), counter(1)])
b3.place(x=485, y=473)

# Q3 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame14, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame14, text="Q3: People make me, save me,\n change me, raise me. What am I?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=500, y=130)
b1 = Button(frame14, text="A. Child", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame15))
b1.place(x=485, y=255)
b2 = Button(frame14, text="B. Money", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame15),counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame14, text="C. Cloth", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame15))
b3.place(x=485, y=473)

# Q4 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame15, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame15, text="Q4: What goes through cities\nand fields, but never moves?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=520, y=133)
b1 = Button(frame15, text="A. Air", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame16))
b1.place(x=485, y=255)
b2 = Button(frame15, text="B. Road", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame16),counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame15, text="C. Sky", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame16))
b3.place(x=485, y=473)

# Q5 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame16, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame16, text="Q5: What tastes better than\nit smells?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=515, y=135)
b1 = Button(frame16, text="A. Sushi", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame17))
b1.place(x=485, y=255)
b2 = Button(frame16, text="B. Tongue", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame17),counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame16, text="C. Ear", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame17))
b3.place(x=485, y=473)

# Q6 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame17, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame17, text="Q6: What has words, but never\nspeaks?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=505, y=135)
b1 = Button(frame17, text="A. Mobile Phone ", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame18))
b1.place(x=485, y=255)
b2 = Button(frame17, text="B. Speaker", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame18))
b2.place(x=485, y=364)
b3 = Button(frame17, text="C. Book", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame18) ,counter(1)])
b3.place(x=485, y=473)

# Q7 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame18, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame18, text="Q7: What is 3/7 chicken, 2/3 cat\nand 2/4 goat?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=505, y=135)
b1 = Button(frame18, text="A. China", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame19))
b1.place(x=485, y=255)
b2 = Button(frame18, text="B. Chicago", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame19),counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame18, text="C. Chile", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame19))
b3.place(x=485, y=473)

# Q8 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame19, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame19, text="Q8: The more you take, the more you\nleave behind. What are they?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=480, y=135)
b1 = Button(frame19, text="A. Money", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame20))
b1.place(x=485, y=255)
b2 = Button(frame19, text="B. Air", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame20))
b2.place(x=485, y=364)
b3 = Button(frame19, text="C. Footsteps", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame20),counter(1)])
b3.place(x=485, y=473)

# Q9 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame20, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame20, text="Q9: Where does today come before\nyesterday?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=480, y=135)
b1 = Button(frame20, text="A. Afer Death", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame21))
b1.place(x=485, y=255)
b2 = Button(frame20, text="B. In Parallel Universe", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame21))
b2.place(x=485, y=364)
b3 = Button(frame20, text="C. In dictionary", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame21),counter(1)])
b3.place(x=485, y=473)

# Q10 (Riddles)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame21, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame21, text="Q10: You go at red and stop at green.\nWhat am I?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=470, y=135)
b1 = Button(frame21, text="A. Traffic Light", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(score))
b1.place(x=485, y=255)
b2 = Button(frame21, text="B. Water Melon", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(score),counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame21, text="C. None of the above", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(score))
b3.place(x=485, y=473)

#############################  IQ  #####################################
# Q1 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame22, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame22, text="Q1: The library is to Books, as Book is \n to what?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=480, y=133)
b1 = Button(frame22, text="A. Cover", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame23))
b1.place(x=485, y=255)
b2 = Button(frame22, text="B. Entertainment", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame23))
b2.place(x=485, y=364)
b3 = Button(frame22, text="C. Pages", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame23), counter(1)])
b3.place(x=485, y=473)

# Q2 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame23, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame23, text="Q2:Which word means the opposite of \n Contrast?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=470, y=133)
b1 = Button(frame23, text="A. Compare", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame24),counter(1)])
b1.place(x=485, y=255)
b2 = Button(frame23, text="B. Difference", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame24))
b2.place(x=485, y=364)
b3 = Button(frame23, text="C. Focus", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame24))
b3.place(x=485, y=473)

# Q3 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame24, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame24, text="Q3: 112::5  543::23  329::15 Which \n analogy below follows the same logic?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=470, y=130)
b1 = Button(frame24, text="A. 460 :: 9", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame25))
b1.place(x=485, y=255)
b2 = Button(frame24, text="B. 780 :: 26", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame25))
b2.place(x=485, y=364)
b3 = Button(frame24, text="C. 435:: 9", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame25), counter(1)])
b3.place(x=485, y=473)

# Q4 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame25, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame25, text="Q4:  If 3 apples and 1 banana cost 70 pence,\n and 3 bananas and 1 apple cost 50 pence,\n then what are the price of 1 apple and 1 banana??", bg="#545454", fg="White", font=("Calibri", 15))
l2.place(x=465, y=130)
b1 = Button(frame25, text="A. 24 pence", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame26))
b1.place(x=485, y=255)
b2 = Button(frame25, text="B. 40 pence", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame26))
b2.place(x=485, y=364)
b3 = Button(frame25, text="C. 30 pence", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame26), counter(1)])
b3.place(x=485, y=473)

# Q5 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame26, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame26, text="Q5: Which set of letters and numbers\n would follow the same logic as the ones listed\n below? [A25] [H18] [Z0]?", bg="#545454", fg="White", font=("Calibri", 16))
l2.place(x=480, y=127)
b1 = Button(frame26, text="A. [G20]", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame27))
b1.place(x=485, y=255)
b2 = Button(frame26, text="B. [P10]", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame27),counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame26, text="C. [X19]", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame27))
b3.place(x=485, y=473)

# Q6 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame27, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame27, text="Q6:Which number should come next \n in the pattern 37, 34, 31, 28 ?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=480, y=133)
b1 = Button(frame27, text="A. 25", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame28),counter(1)])
b1.place(x=485, y=255)
b2 = Button(frame27, text="B. 18", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame28))
b2.place(x=485, y=364)
b3 = Button(frame27, text="C. 11", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame28))
b3.place(x=485, y=473)

# Q7 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame28, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame28, text="Q7: Find two words, one from each group,that \nare the closest in meaning:talkative, job, ecstatic?", bg="#545454", fg="White", font=("Calibri", 16))
l2.place(x=475, y=139)
b1 = Button(frame28, text="A. ecstatic and angry", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame29))
b1.place(x=485, y=255)
b2 = Button(frame28, text="B. talkative and loquacious", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame29),counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame28, text="C. angry and wind", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame29))
b3.place(x=485, y=473)

# Q8 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame29, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame29, text="Q8: Which of the following can be \n arranged into a 5-letter English word?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=470, y=133)
b1 = Button(frame29, text="A.  R I L S A", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame30),counter(1)])
b1.place(x=485, y=255)
b2 = Button(frame29, text="B. W Q R G S", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame30))
b2.place(x=485, y=364)
b3 = Button(frame29, text="C. H R G S T", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda:show_frame(frame30))
b3.place(x=485, y=473)

# Q9 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame30, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame30, text="Q9: Some months have 31 days. Some \n have 30. How many have 28?", bg="#545454", fg="White", font=("Calibri", 20))
l2.place(x=475, y=133)
b1 = Button(frame30, text="A. 1", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame31))
b1.place(x=485, y=255)
b2 = Button(frame30, text="B. 12", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(frame31),counter(1)])
b2.place(x=485, y=364)
b3 = Button(frame30, text="C. 2", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(frame31))
b3.place(x=485, y=473)

# Q10 (IQ)
img = Image.open("QA.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(frame31, image=jpg)
l1.place(width=1366, height=768)
l2 = Label(frame31, text="Q10: A plane crashes on the United States/Canada\n border. Where are the survivors buried?", bg="#545454", fg="White", font=("Calibri", 16))
l2.place(x=468, y=142)
b1 = Button(frame31, text="A. They aren't", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: [show_frame(score),counter(1)])
b1.place(x=485, y=255)
b2 = Button(frame31, text="B. US ", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(score))
b2.place(x=485, y=364)
b3 = Button(frame31, text="C. Canada", bg='#9A6EC4', fg="white", font=("Calibri", 20), border=0, width=28,
            command=lambda: show_frame(score))
b3.place(x=485, y=473)

# score
img = Image.open("Score.jpg")
jpg = ImageTk.PhotoImage(img)
l1 = Label(image=jpg)
l1.image = jpg
l1 = Label(score, image=jpg)
l1.place(width=1366, height=768)
b10 = Button(score, text="MENU", bg="#D9D9D0", fg="black", font=("Calibri", 20), border=0, width=10,
             command=lambda: [show_frame(frame1),counter(-count)])
b10.place(x=180, y=520)
b92=Button(score, text="QUIT", bg="#D9D9D0", fg="black", font=("Calibri", 20), border=0, width=10,
             command=close_m)
b92.place(x=180, y=617)

m.mainloop()
