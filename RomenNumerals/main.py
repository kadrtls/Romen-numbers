from tkinter import *
from tkinter import messagebox

#GUI
window = Tk()
window.title("Calculator")
#window.config(bg='black')
window.minsize(350,750)

photo=PhotoImage(file="calculator2.png")
photo_label =Label(image=photo)
photo_label.pack()

romen_number_title = Label(text="Enter a romen number")
romen_number_title.config(pady=10)
romen_number_title.pack()

romen_number_entry = Entry(width=40)
romen_number_entry.pack()

decimal_number_title = Label(text="Decimal number")
decimal_number_title.config(pady=10)
decimal_number_title.pack()

decimal_number_txt = Text(width=30,height=1)
decimal_number_txt.pack()


def calculate_romen_number():
        result = 0
        number_list=[]
        romen_numbers=['M','D','C','L','X','V','I']
        #input_number = input("Enter a romen number:")
        input_number=romen_number_entry.get()
        input_number=input_number.upper()
        for x in input_number:
            number_list.append(x)
        print(number_list)
        #---------------------------------------------------
        # --------------------------------------------------
        if (len(number_list) >13):
            #BURALARDA ERROR MESSAGES OLABİLİR
            print("!YOU ENTER MANY NUMBER!.PLEASE TRY ENTER.(Max 13 number)")
            calculate_romen_number()
            #it  should return to the input section
        elif(number_list.count("D")>=2 or number_list.count("C")>=4 or number_list.count("L")>=2 or
              number_list.count("X")>=4 or number_list.count("V")>=2 or number_list.count("I") >=4):
            # BURALARDA ERROR MESSAGES OLABİLİR
            print("!YOU ENTER WRONG NUMBER!PLEASE TRY ENTER")
            calculate_romen_number()
            #it  should return to the input section
        else:
            for y in range(0,len(number_list)):
                # if(number_list[y]!=romen_numbers):
                # BURALARDA ERROR MESSAGES OLABİLİR
            #CASE M
                if(number_list[y] == "M"):
                    c=0
                    for i in range(0,y+1):
                        if(number_list[i]=="C"):
                            c+=1
                    if(c==1):
                         result+=800
                    elif(c>1):
                        print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                        calculate_romen_number()
                    else:
                        for i in range(0, y+1):
                            if(number_list[i]=="D" or number_list[i]=="C" or number_list[i]=="L" or number_list[i]=="X" or
                                number_list[i]=="V" or number_list[i]=="I"):
                                print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                                calculate_romen_number()
                            if(i==y):
                                result+=1000
            # CASE D
                elif(number_list[y]=="D"):
                    if (len(number_list) >= 3):
                        if(number_list[y-1]=="M" and number_list[y-2]=="C"):
                            print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                            calculate_romen_number()
                    a=0
                    for i in range(0, y+1):
                        if(number_list[i]=="C"):
                            a+=1
                    if(a==1 and number_list[y-1] =="C" and number_list[y]=="D"):
                        result+=300
                    elif(a>1):
                        print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                        calculate_romen_number()
                    elif(a==0):
                        for i in range(0, y+1):
                            if(number_list[i]=="C" or number_list[i]=="L" or number_list[i]=="X" or
                                number_list[i]=="V" or number_list[i]=="I"):
                                print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                                calculate_romen_number()
                            if(i==y):
                                result+=500
            # CASE C
                elif(number_list[y]=="C"):
                    if(len(number_list)>=3):
                        if (number_list[y - 1] == "D" and number_list[y - 2] == "C"):
                            print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                            calculate_romen_number()
                        if (number_list[y - 1] == "M" and number_list[y - 2] == "C"):
                            print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                            calculate_romen_number()
                    x = 0
                    for i in range(0, y + 1):
                        if (number_list[i] == "X"):
                            x += 1
                    if (x == 1 and number_list[y - 1] == "X" and number_list[y] == "C"):
                        result += 80
                    elif (x > 1):
                        print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                        calculate_romen_number()
                    elif (x == 0):
                        for i in range(0, y+1):
                            if(number_list[i]=="L" or number_list[i]=="X" or
                                number_list[i]=="V" or number_list[i]=="I"):
                                print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                                calculate_romen_number()
                            if(i==y):
                                result+=100
            # CASE L
                elif(number_list[y]=="L"):
                    if (number_list[y - 1] == "C" and number_list[y - 2] == "X"):
                        print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                        calculate_romen_number()
                    x = 0
                    for i in range(0, y + 1):
                        if (number_list[i] == "X"):
                            x += 1
                    if (x == 1 and number_list[y - 1] == "X" and number_list[y] == "L"):
                        result += 30
                    elif (x > 1):
                        print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                        calculate_romen_number()
                    elif (x == 0):
                        for i in range(0, y + 1):
                            if (number_list[i] == "X" or number_list[i] == "V" or number_list[i] == "I"):
                                print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                                calculate_romen_number()
                            if (i == y):
                                result += 50
            # CASE X
                elif(number_list[y]=="X"):
                    if(len(number_list)>=3):
                        if (number_list[y - 1] == "C" and number_list[y - 2] == "X"):
                            print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                            calculate_romen_number()
                        if (number_list[y - 1] == "L" and number_list[y - 2] == "X"):
                            print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                            calculate_romen_number()
                    I = 0
                    for i in range(0, y + 1):
                        if (number_list[i] == "I"):
                            I += 1
                    if (I == 1 and number_list[y - 1] == "I" and number_list[y] == "X"):
                        result += 8
                    elif (I > 1):
                        print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                        calculate_romen_number()
                    elif (I == 0):
                        for i in range(0, y + 1):
                            if (number_list[i] == "V" or number_list[i] == "I"):
                                print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                                calculate_romen_number()
                            if (i == y):
                                result += 10
            # CASE V
                elif(number_list[y]=="V"):
                    if (len(number_list) >= 3):
                        if (number_list[y - 1] == "I" and number_list[y - 2] == "V" and len(number_list)>3):
                            print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                            calculate_romen_number()
                        if (number_list[y - 1] == "X" and number_list[y - 2] == "I" and len(number_list)>3):
                            print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                            calculate_romen_number()
                    v=0
                    for i in range(0, y + 1):
                        if (number_list[i] == "I"):
                            v += 1
                    if (v == 1 and number_list[y - 1] == "I" and number_list[y] == "V"):
                        result += 3
                    elif (v > 1):
                        print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                        calculate_romen_number()
                    elif (v == 0):
                        for i in range(0, y + 1):
                            if (number_list[i] == "I"):
                                print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                                calculate_romen_number()
                            if (i == y):
                                result += 5
            # CASE I
                elif(number_list[y]=="I"):
                    if(len(number_list)>=3):
                        if (number_list[y - 2] == "I" and number_list[y - 1] == "V"):
                            messagebox.showinfo(title="ERROR",message="Wrong number try again")
                            #print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                            #calculate_romen_number()
                        elif(number_list[y - 2] == "I" and number_list[y - 1] == "X"):
                            print("YOU ENTER WRONG NUMBER!!TRY AGAİN.")
                            calculate_romen_number()
                        else:
                            result += 1
                    else:
                        result += 1
        a=str(result)
        decimal_number_txt.delete(1.0, END)
        decimal_number_txt.insert(1.0, a)

        print(f"YOUR DECİMAL NUMBER : {result}")
calculate_romen_number()
decimal_number_txt.delete(1.0, END)
calculate_btn = Button(text="Calculate",command=calculate_romen_number)
calculate_btn.config(pady=7)
calculate_btn.pack()

window.mainloop()