import tkinter as tk
import random

global version,versionType
version = 1.0
versionType = ""
root = tk.Tk()
root.geometry("600x400")
root.title(f"LanguageModule: Latein {versionType}v{version}")
root.resizable(width=False, height=False)

richtig = 0
falsch = 0
rand = False
Wörter = [[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
Answers = ["","","",""]

# PP = Passiv Präsens, PI = Passiv Imperfekt, Pf = Passiv Futur I, AP = Aktiv Präsens, AI = Aktiv Imperfekt, Ap Aktiv Perfekt, Al = Aktiv Plqp., Af = Aktiv Futur I

def get_dict(Wdh):
    global rawInput,Wörter,dic,chosen,Answers
    if Wdh == False and Wörter != [[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]:
        Wörter = [[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]],[[],[],[],[],[],[]]]
    insert = ""
    if Wdh == False:    
        with open(r'C:\Users\Rubikus\Coding\Python\LanguageModule\Latein-dictonary.txt','r') as f:
            rawInput = f.read()
    
    for i in range(len(rawInput)):
        if rawInput[i] == '\\' or (rawInput[i] == 'n' and rawInput[i-1]== '\\'):
            pass
        else:
            if rawInput[i] == "P" and rawInput[i+1] == "P" and rawInput[i+2] == "1":
                dic = [0,0]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "P" and rawInput[i+2] == "2":
                dic = [0,1]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "P" and rawInput[i+2] == "3":
                dic = [0,2]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "P" and rawInput[i+2] == "4":
                dic = [0,3]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "P" and rawInput[i+2] == "5":
                dic = [0,4]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "P" and rawInput[i+2] == "6":
                dic = [0,5]
                one_time = True
                
            if rawInput[i] == "P" and rawInput[i+1] == "I" and rawInput[i+2] == "1":
                dic = [1,0]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "I" and rawInput[i+2] == "2":
                dic = [1,1]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "I" and rawInput[i+2] == "3":
                dic = [1,2]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "I" and rawInput[i+2] == "4":
                dic = [1,3]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "I" and rawInput[i+2] == "5":
                dic = [1,4]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "I" and rawInput[i+2] == "6":
                dic = [1,5]
                one_time = True
            
            if rawInput[i] == "P" and rawInput[i+1] == "f" and rawInput[i+2] == "1":
                dic = [2,0]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "f" and rawInput[i+2] == "2":
                dic = [2,1]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "f" and rawInput[i+2] == "3":
                dic = [2,2]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "f" and rawInput[i+2] == "4":
                dic = [2,3]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "f" and rawInput[i+2] == "5":
                dic = [2,4]
                one_time = True
            if rawInput[i] == "P" and rawInput[i+1] == "f" and rawInput[i+2] == "6":
                dic = [2,5]
                one_time = True
                
            if rawInput[i] == "A" and rawInput[i+1] == "P" and rawInput[i+2] == "1":
                dic = [3,0]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "P" and rawInput[i+2] == "2":
                dic = [3,1]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "P" and rawInput[i+2] == "3":
                dic = [3,2]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "P" and rawInput[i+2] == "4":
                dic = [3,3]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "P" and rawInput[i+2] == "5":
                dic = [3,4]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "P" and rawInput[i+2] == "6":
                dic = [3,5]
                one_time = True
                
            if rawInput[i] == "A" and rawInput[i+1] == "I" and rawInput[i+2] == "1":
                dic = [4,0]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "I" and rawInput[i+2] == "2":
                dic = [4,1]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "I" and rawInput[i+2] == "3":
                dic = [4,2]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "I" and rawInput[i+2] == "4":
                dic = [4,3]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "I" and rawInput[i+2] == "5":
                dic = [4,4]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "I" and rawInput[i+2] == "6":
                dic = [4,5]
                one_time = True
                
            if rawInput[i] == "A" and rawInput[i+1] == "p" and rawInput[i+2] == "1":
                dic = [5,0]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "p" and rawInput[i+2] == "2":
                dic = [5,1]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "p" and rawInput[i+2] == "3":
                dic = [5,2]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "p" and rawInput[i+2] == "4":
                dic = [5,3]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "p" and rawInput[i+2] == "5":
                dic = [5,4]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "p" and rawInput[i+2] == "6":
                dic = [5,5]
                one_time = True
                
            if rawInput[i] == "A" and rawInput[i+1] == "l" and rawInput[i+2] == "1":
                dic = [6,0]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "l" and rawInput[i+2] == "2":
                dic = [6,1]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "l" and rawInput[i+2] == "3":
                dic = [6,2]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "l" and rawInput[i+2] == "4":
                dic = [6,3]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "l" and rawInput[i+2] == "5":
                dic = [6,4]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "l" and rawInput[i+2] == "6":
                dic = [6,5]
                one_time = True
                
            if rawInput[i] == "A" and rawInput[i+1] == "f" and rawInput[i+2] == "1":
                dic = [7,0]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "f" and rawInput[i+2] == "2":
                dic = [7,1]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "f" and rawInput[i+2] == "3":
                dic = [7,2]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "f" and rawInput[i+2] == "4":
                dic = [7,3]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "f" and rawInput[i+2] == "5":
                dic = [7,4]
                one_time = True
            if rawInput[i] == "A" and rawInput[i+1] == "f" and rawInput[i+2] == "6":
                dic = [7,5]
                one_time = True
                
            if rawInput[i] != "," and rawInput[i] != ".":
                insert += rawInput[i]
            if  rawInput[i] == ",":
                if one_time == True:
                    Wörter[dic[0]][dic[1]].append(insert[4:])
                    insert = ""
                    one_time = False
                else:
                    Wörter[dic[0]][dic[1]].append(insert)
                    insert = ""

def PassivPräsens():
    global randNum2,Form
    Form = 0
    EinsVier = [0,1,2,3]
    EinsSechs = [0,1,2,3,4,5]
    for i in range(4):
        randNum1 = random.choice(EinsVier)
        EinsVier.remove(randNum1)
        randNum2 = random.choice(EinsSechs)
        EinsSechs.remove(randNum2)
        randNum3 = random.randint(0,2)
        Answers[randNum1] = Wörter[0][randNum2][randNum3]
    
    if randNum2 >= 3:
        Numerus = "Plural"
        Person = randNum2 - 2
    elif randNum2 < 3:
        Numerus = "Singular"
        Person = randNum2 + 1


    Text2.config(text=f'Wählen sie bitte die {Person}. Person {Numerus} Passiv Präsens Indikativ')
    Text2.pack()
    Text2.place(x=150, y=100)

    A1.pack()
    A1.place(x=150, y=300)     
    A1.config(text=Answers[0])
    
    A2.pack()
    A2.place(x=350, y=300)
    A2.config(text=Answers[1])
    
    A3.pack()
    A3.place(x=150, y=200)
    A3.config(text=Answers[2])
    
    A4.pack()
    A4.place(x=350, y=200)
    A4.config(text=Answers[3])

def PassivImperfekt():
    global randNum2,Form
    Form = 1
    EinsVier = [0,1,2,3]
    EinsSechs = [0,1,2,3,4,5]
    for i in range(4):
        randNum1 = random.choice(EinsVier)
        EinsVier.remove(randNum1)
        randNum2 = random.choice(EinsSechs)
        EinsSechs.remove(randNum2)
        randNum3 = random.randint(0,2)
        Answers[randNum1] = Wörter[1][randNum2][randNum3]
    
    if randNum2 >= 3:
        Numerus = "Plural"
        Person = randNum2 - 2
    elif randNum2 < 3:
        Numerus = "Singular"
        Person = randNum2 + 1


    Text2.config(text=f'Wählen sie bitte die {Person}. Person {Numerus} Passiv Imperfekt Indikativ')
    Text2.pack()
    Text2.place(x=150, y=100)

    A1.pack()
    A1.place(x=150, y=300)     
    A1.config(text=Answers[0])
    
    A2.pack()
    A2.place(x=350, y=300)
    A2.config(text=Answers[1])
    
    A3.pack()
    A3.place(x=150, y=200)
    A3.config(text=Answers[2])
    
    A4.pack()
    A4.place(x=350, y=200)
    A4.config(text=Answers[3])

def PassivFuturI():
    global randNum2,Form
    Form = 2
    EinsVier = [0,1,2,3]
    EinsSechs = [0,1,2,3,4,5]
    for i in range(4):
        randNum1 = random.choice(EinsVier)
        EinsVier.remove(randNum1)
        randNum2 = random.choice(EinsSechs)
        EinsSechs.remove(randNum2)
        randNum3 = random.randint(0,2)
        Answers[randNum1] = Wörter[2][randNum2][randNum3]
    
    if randNum2 >= 3:
        Numerus = "Plural"
        Person = randNum2 - 2
    elif randNum2 < 3:
        Numerus = "Singular"
        Person = randNum2 + 1


    Text2.config(text=f'Wählen sie bitte die {Person}. Person {Numerus} Passiv Futur I Indikativ')
    Text2.pack()
    Text2.place(x=150, y=100)

    A1.pack()
    A1.place(x=150, y=300)     
    A1.config(text=Answers[0])
    
    A2.pack()
    A2.place(x=350, y=300)
    A2.config(text=Answers[1])
    
    A3.pack()
    A3.place(x=150, y=200)
    A3.config(text=Answers[2])
    
    A4.pack()
    A4.place(x=350, y=200)
    A4.config(text=Answers[3])

def AktivPräsens():
    global randNum2,Form
    Form = 3
    EinsVier = [0,1,2,3]
    EinsSechs = [0,1,2,3,4,5]
    for i in range(4):
        randNum1 = random.choice(EinsVier)
        EinsVier.remove(randNum1)
        randNum2 = random.choice(EinsSechs)
        EinsSechs.remove(randNum2)
        randNum3 = random.randint(0,2)
        Answers[randNum1] = Wörter[3][randNum2][randNum3]
    
    if randNum2 >= 3:
        Numerus = "Plural"
        Person = randNum2 - 2
    elif randNum2 < 3:
        Numerus = "Singular"
        Person = randNum2 + 1


    Text2.config(text=f'Wählen sie bitte die {Person}. Person {Numerus} Aktiv Präsens Indikativ')
    Text2.pack()
    Text2.place(x=150, y=100)

    A1.pack()
    A1.place(x=150, y=300)     
    A1.config(text=Answers[0])
    
    A2.pack()
    A2.place(x=350, y=300)
    A2.config(text=Answers[1])
    
    A3.pack()
    A3.place(x=150, y=200)
    A3.config(text=Answers[2])
    
    A4.pack()
    A4.place(x=350, y=200)
    A4.config(text=Answers[3])

def AktivImperfekt():
    global randNum2,Form
    Form = 4
    EinsVier = [0,1,2,3]
    EinsSechs = [0,1,2,3,4,5]
    for i in range(4):
        randNum1 = random.choice(EinsVier)
        EinsVier.remove(randNum1)
        randNum2 = random.choice(EinsSechs)
        EinsSechs.remove(randNum2)
        randNum3 = random.randint(0,2)
        Answers[randNum1] = Wörter[4][randNum2][randNum3]
    
    if randNum2 >= 3:
        Numerus = "Plural"
        Person = randNum2 - 2
    elif randNum2 < 3:
        Numerus = "Singular"
        Person = randNum2 + 1


    Text2.config(text=f'Wählen sie bitte die {Person}. Person {Numerus} Aktiv Imperfekt Indikativ')
    Text2.pack()
    Text2.place(x=150, y=100)

    A1.pack()
    A1.place(x=150, y=300)     
    A1.config(text=Answers[0])
    
    A2.pack()
    A2.place(x=350, y=300)
    A2.config(text=Answers[1])
    
    A3.pack()
    A3.place(x=150, y=200)
    A3.config(text=Answers[2])
    
    A4.pack()
    A4.place(x=350, y=200)
    A4.config(text=Answers[3])

def AktivPerfekt():
    global randNum2,Form
    Form = 5
    EinsVier = [0,1,2,3]
    EinsSechs = [0,1,2,3,4,5]
    for i in range(4):
        randNum1 = random.choice(EinsVier)
        EinsVier.remove(randNum1)
        randNum2 = random.choice(EinsSechs)
        EinsSechs.remove(randNum2)
        randNum3 = random.randint(0,2)
        Answers[randNum1] = Wörter[5][randNum2][randNum3]
    
    if randNum2 >= 3:
        Numerus = "Plural"
        Person = randNum2 - 2
    elif randNum2 < 3:
        Numerus = "Singular"
        Person = randNum2 + 1


    Text2.config(text=f'Wählen sie bitte die {Person}. Person {Numerus} Aktiv Perfekt Indikativ')
    Text2.pack()
    Text2.place(x=150, y=100)

    A1.pack()
    A1.place(x=150, y=300)     
    A1.config(text=Answers[0])
    
    A2.pack()
    A2.place(x=350, y=300)
    A2.config(text=Answers[1])
    
    A3.pack()
    A3.place(x=150, y=200)
    A3.config(text=Answers[2])
    
    A4.pack()
    A4.place(x=350, y=200)
    A4.config(text=Answers[3])

def AktivPlusquamperfekt():
    global randNum2,Form
    Form = 6
    EinsVier = [0,1,2,3]
    EinsSechs = [0,1,2,3,4,5]
    for i in range(4):
        randNum1 = random.choice(EinsVier)
        EinsVier.remove(randNum1)
        randNum2 = random.choice(EinsSechs)
        EinsSechs.remove(randNum2)
        randNum3 = random.randint(0,2)
        Answers[randNum1] = Wörter[6][randNum2][randNum3]
    
    if randNum2 >= 3:
        Numerus = "Plural"
        Person = randNum2 - 2
    elif randNum2 < 3:
        Numerus = "Singular"
        Person = randNum2 + 1


    Text2.config(text=f'Wählen sie bitte die {Person}. Person {Numerus} Aktiv Plusquamperfekt Indikativ')
    Text2.pack()
    Text2.place(x=150, y=100)

    A1.pack()
    A1.place(x=150, y=300)     
    A1.config(text=Answers[0])
    
    A2.pack()
    A2.place(x=350, y=300)
    A2.config(text=Answers[1])
    
    A3.pack()
    A3.place(x=150, y=200)
    A3.config(text=Answers[2])
    
    A4.pack()
    A4.place(x=350, y=200)
    A4.config(text=Answers[3])

def AktivFuturI():
    global randNum2,Form
    Form = 7
    EinsVier = [0,1,2,3]
    EinsSechs = [0,1,2,3,4,5]
    for i in range(4):
        randNum1 = random.choice(EinsVier)
        EinsVier.remove(randNum1)
        randNum2 = random.choice(EinsSechs)
        EinsSechs.remove(randNum2)
        randNum3 = random.randint(0,2)
        Answers[randNum1] = Wörter[7][randNum2][randNum3]
    
    if randNum2 >= 3:
        Numerus = "Plural"
        Person = randNum2 - 2
    elif randNum2 < 3:
        Numerus = "Singular"
        Person = randNum2 + 1


    Text2.config(text=f'Wählen sie bitte die {Person}. Person {Numerus} Aktiv Futur I Indikativ')
    Text2.pack()
    Text2.place(x=150, y=100)

    A1.pack()
    A1.place(x=150, y=300)     
    A1.config(text=Answers[0])
    
    A2.pack()
    A2.place(x=350, y=300)
    A2.config(text=Answers[1])
    
    A3.pack()
    A3.place(x=150, y=200)
    A3.config(text=Answers[2])
    
    A4.pack()
    A4.place(x=350, y=200)
    A4.config(text=Answers[3])

def CheckAnswer(Button):
    global richtig,falsch
    if Answers[Button] in Wörter[Form][randNum2]:
        richtig += 1
        if rand:
            randomSet()        
        elif Form == 0:
            PassivPräsens()
        elif Form == 1:
            PassivImperfekt()
        elif Form == 2:
            PassivFuturI()
        elif Form == 3:
            AktivPräsens()
        elif Form == 4:
            AktivImperfekt()
        elif Form == 5:
            AktivPerfekt()
        elif Form == 6:
            AktivPlusquamperfekt()
        elif Form == 7:
            AktivFuturI()
    else:
        falsch += 1

    RFText.config(text= "Richtig: " + str(richtig) + "\nFalsch: " + str(falsch) + "\n Quote: " + str(int(round((richtig / (richtig + falsch)) * 100,0))) + "%")

def randomSet():
    global rand
    num = random.randint(0,7)
    rand = True
    if num == 0:
        PassivPräsens()
    elif num == 1:
        PassivImperfekt()
    elif num == 2:
        PassivFuturI()
    elif num == 3:
        AktivPräsens()
    elif num == 4:
        AktivImperfekt()
    elif num == 5:
        AktivPerfekt()
    elif num == 6:
        AktivPlusquamperfekt()
    elif num == 7:
        AktivFuturI()

Text2 = tk.Label(root)

RFText = tk.Label(root,text= "Richtig: " + str(richtig) + "\nFalsch: " + str(falsch) + "\n Quote: " + str(int(round((richtig / (richtig + falsch + 1)) * 100,0))) + "%")
RFText.pack
RFText.place(x=300,y=10)

PassivPräsensKnopf = tk.Button(root, text="Passiv - Präsens",command=lambda:[get_dict(False),PassivPräsens()],width= 14)
PassivPräsensKnopf.pack()
PassivPräsensKnopf.place(x=10,y=50)

PassivImperfektKnopf = tk.Button(root, text="Passiv - Imperfekt",command=lambda:[get_dict(False),PassivImperfekt()],width= 14)
PassivImperfektKnopf.pack()
PassivImperfektKnopf.place(x=10,y=80)

PassivFuturIKnopf = tk.Button(root, text="Passiv - Futur I",command=lambda:[get_dict(False),PassivFuturI()],width= 14)
PassivFuturIKnopf.pack()
PassivFuturIKnopf.place(x=10,y=110)

AktivPräsensKnopf = tk.Button(root, text="Aktiv - Präsens",command=lambda:[get_dict(False),AktivPräsens()],width= 14)
AktivPräsensKnopf.pack()
AktivPräsensKnopf.place(x=10,y=180)

AktivImperfektKnopf = tk.Button(root, text="Aktiv - Imperfekt",command=lambda:[get_dict(False),AktivImperfekt()],width= 14)
AktivImperfektKnopf.pack()
AktivImperfektKnopf.place(x=10,y=210)

AktivPerfektKnopf = tk.Button(root, text="Aktiv - Perfekt",command=lambda:[get_dict(False),AktivPerfekt()],width= 14)
AktivPerfektKnopf.pack()
AktivPerfektKnopf.place(x=10,y=240)

AktivPlusquamperfektKnopf = tk.Button(root, text="Aktiv - Plqp.",command=lambda:[get_dict(False),AktivPlusquamperfekt()],width= 14)
AktivPlusquamperfektKnopf.pack()
AktivPlusquamperfektKnopf.place(x=10,y=270)

AktivFuturIKnopf = tk.Button(root, text="Aktiv - Futur I",command=lambda:[get_dict(False),AktivFuturI()],width= 14)
AktivFuturIKnopf.pack()
AktivFuturIKnopf.place(x=10,y=300)

ZufallsKnopf = tk.Button(root, text="Zufall",command=lambda:[get_dict(False),randomSet()],width= 14)
ZufallsKnopf.pack()
ZufallsKnopf.place(x=10,y=363)

A1 = tk.Button(root, text="Antwort 1",width=20,height=2,command=lambda : [CheckAnswer(0)])
A2 = tk.Button(root, text="Antwort 2",width=20,height=2,command=lambda : [CheckAnswer(1)])
A3 = tk.Button(root, text="Antwort 3",width=20,height=2,command=lambda : [CheckAnswer(2)])
A4 = tk.Button(root, text="Antwort 4",width=20,height=2,command=lambda : [CheckAnswer(3)])

if __name__ == "__main__":
    root.mainloop()