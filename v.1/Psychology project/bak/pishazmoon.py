
from os import path
import random
import arabic_reshaper
from bidi.algorithm import get_display
from tkinter import *
from tkinter import messagebox
import json
from sys import exit
from collections import OrderedDict 

#-------------------------
def bc800(root):
    bg=PhotoImage(file="../Psychology project/bak/bc1-800.500.png")
    bg_label=Label(root,image=bg)
    bg_label.place(x=0,y=0)

def bc1000(root):
    bg=PhotoImage(file="../Psychology project/bak/bc1-1000.600.png")
    bg_label=Label(root,image=bg)
    bg_label.place(x=0,y=0)
#-------------------------

class sce:    #class that get the scenario from the file  + with the loop

    def __init__(self,path1,def_name):
        self.name=str() 
        self.def_name=def_name
        self.text_list=list() 
        self.simp_question=str() 
        self.main_question=dict() 
        data_folder="../Psychology project/scenarios/soogiri/"
        file_to_open=data_folder+path1
        file=open(file_to_open,"r",encoding="utf-8")
        a=0
        for line in file:
            line=line.replace("\n","")
            if line =="**":
                a+=1
                continue
            if a==0:
                self.name=line
                a+=1
            elif a==1:
                reshaped_line = arabic_reshaper.reshape(line)
                self.text_list.append(get_display(reshaped_line))
            elif a==2:
                self.simp_question=line
                a+=1
            elif a==3: # for the first question of the questions target
                line=line.split(":")
                self.main_question[line[0]]=line[1]
                     
        file.close()
    def __del__(self):
        print('ok')



def shoro():
        root=Tk()
        width=800
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.title("شروع")


        bc800(root)
        def GButton_944_command():
            exit()

        GButton_944_3=Button(root,font=("Times",10))
        GButton_944_3["bg"] = "#fe9d9d"
        GButton_944_3["fg"] = "#000000"
        GButton_944_3["justify"] = "center"
        GButton_944_3["text"] = "خروج کامل"
        GButton_944_3.place(x=730,y=0,width=70,height=25)
        GButton_944_3["command"] = GButton_944_command    

        GLabel_7400=Label(root)
        GLabel_7400["bg"] = "#fad400"
        GLabel_7400["fg"] = "#333333"
        GLabel_7400["justify"] = "center"
        GLabel_7400["text"] = ""
        GLabel_7400.place(x=0,y=20,width=801,height=30)

        # lbl1=Label(root,text="جهت شروع ابتدا نام و آیدی مد نظر خود را وارد کرده و سپس روی دکمه زیر کلیک کنید",font=("B Nazanin",15,),bg="#00babd")
        # lbl1.place(x=150,y=150)
        GLabel_944=Label(root,font=("Times",15))
        GLabel_944["bg"] = "#dcdcdc"
        
        GLabel_944["justify"] = "center"
        GLabel_944["text"] = "جهت شروع ابتدا نام و آیدی مد نظر خود را وارد کرده و سپس روی دکمه شروع کلیک کنید"
        GLabel_944.place(x=10,y=100,width=775,height=37)

        GLabel_584=Label(root,font=("Times",13))
        GLabel_584["fg"] = "#333333"
        GLabel_584["justify"] = "center"
        GLabel_584["text"] = " : نام "
        GLabel_584.place(x=370,y=190,width=70,height=25)

        ins_name=Entry(root,font=("Times",12))
        ins_name["bg"] = "#ffffff"
        ins_name["borderwidth"] = "1px"
        ins_name["fg"] = "#333333"
        ins_name["justify"] = "center"
        ins_name.place(x=200,y=220,width=411,height=37)
        

        GLabel_33=Label(root,font=("Times",13))
        GLabel_33["fg"] = "#333333"
        GLabel_33["justify"] = "center"
        GLabel_33["text"] = " : آیدی  "
        GLabel_33.place(x=370,y=300,width=70,height=25)

        ins_id=Entry(root,font=("Times",12))
        ins_id["bg"] = "#ffffff"
        ins_id["borderwidth"] = "1px"
        ins_id["fg"] = "#333333"
        ins_id["justify"] = "center"
        ins_id.place(x=200,y=330,width=410,height=40)
        
        data1=dict()

        def insert():
            client_name=ins_name.get()
            client_id=ins_id.get()
            next_page=True

            data_folder="../Psychology project/data/"
            file_to_open=data_folder+'client.json'        
            with open(file_to_open,'r') as f:
                data=json.load(f)
                f.close()
            for id_check in data["client"]:
                if id_check["id"]==client_id or id_check["name"]==client_name:
                    messagebox.showinfo("خطا","آیدی و یا نام وارد شده تکراری است")
                    next_page=False
                    break;

            if client_name=="" or client_id=="":
                messagebox.showinfo("خطا","لطفا نام و آیدی خود را وارد کنید")
                next_page=False
                
            if next_page==True:
                
                data1["name"]=client_name.lower()
                data1["id"]=client_id
                root.destroy()
                

        GButton_281=Button(root,font=("Times",18),command=insert)
        GButton_281["activeforeground"] = "#ffffff"
        GButton_281["bg"] = "#fad400"
        GButton_281["fg"] = "#000000"
        GButton_281["justify"] = "center"
        GButton_281["text"] = "شروع"
        GButton_281["relief"] = "raised"
        GButton_281.place(x=340,y=410,width=125,height=37)

        root.mainloop()
        return data1

#-------------------------
shoro1=shoro()
#----------------------
square=[[1,11, 61, 2, 12], [62, 3, 13, 63, 4], [14, 64, 5, 15, 65], [6, 16, 66, 7, 17], [67, 8, 18, 68, 9], [19, 69, 10, 20, 70]]

final_data=dict()

for reza in square :

    list_of_sen=list()
    for i in reza:
        sc_temp=sce("scenario"+str(i)+".txt","scenario"+str(i))
        list_of_sen.append(sc_temp)
        del sc_temp;

    #-----------------------------

    for i in range (0,len(list_of_sen)):  #show  main sentenses and simple question of each one
        root=Tk()
        root.title('psycho test')
        
        
        width=1000
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        bg=PhotoImage(file="../Psychology project/bak/bc1-1000.600.png")
        bg_label=Label(root,image=bg)
        bg_label.place(x=0,y=0)

        def GButton_944_command():
            exit()
        GButton_944_5=Button(root,font=("Times",10))
        GButton_944_5["bg"] = "#fe9d9d"
        GButton_944_5["fg"] = "#000000"
        GButton_944_5["justify"] = "center"
        GButton_944_5["text"] = "خروج کامل"
        GButton_944_5.place(x=930,y=0,width=70,height=25)
        GButton_944_5["command"] = GButton_944_command

        

        GLabel_747=Label(root)
        GLabel_747["bg"] = "#fad400"
        GLabel_747["fg"] = "#333333"
        GLabel_747["justify"] = "center"
        GLabel_747["text"] = ""
        GLabel_747.place(x=0,y=20,width=1000,height=30)

        lbl1=Label(root,text="عنوان سناریو: "+list_of_sen[i].name,width=50, 
                bg="#dcdcdc",
                justify="center",
                relief="raised",
                font=("ariel", 18))
        lbl1.place(x=350,y=100,width=340,height=63)

        a=0
        sc=list_of_sen[i].text_list
        sq=list_of_sen[i].simp_question
        lbl2=Label(root,
        text="",
        relief="solid",
        background='#ffffff',
        justify="center",
        font=("Times",17))
        lbl2.place(x=50,y=230,width=890,height=136)
        def move():
            global a
            global sc
            if a<len(sc):
                lbl2.configure(text=sc[a])
                a+=1
                root.after(10000,move)
            elif a==len(sc):

                def create_window():
                    global sq
                    new_window = Tk()
                    new_window.title('سوال')
                    width=1000
                    height=600
                    screenwidth = new_window.winfo_screenwidth()
                    screenheight = new_window.winfo_screenheight()
                    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                    new_window.geometry(alignstr)
                    new_window.resizable(width=False, height=False)


                    def GButton_944_command():
                        exit()

                    GButton_944_3=Button(new_window,font=("Times",10))
                    GButton_944_3["bg"] = "#fe9d9d"
                    GButton_944_3["fg"] = "#000000"
                    GButton_944_3["justify"] = "center"
                    GButton_944_3["text"] = "خروج کامل"
                    GButton_944_3.place(x=930,y=0,width=70,height=25)
                    GButton_944_3["command"] = GButton_944_command




                    GLabel_747=Label(new_window)
                    GLabel_747["bg"] = "#fad400"
                    GLabel_747["fg"] = "#333333"
                    GLabel_747["justify"] = "center"
                    GLabel_747["text"] = ""
                    GLabel_747.place(x=0,y=20,width=1000,height=30)

                    lbl1=Label(new_window,text="عنوان سناریو : "+list_of_sen[i].name,
                    bg = "#dcdcdc",
                    relief="raised",
                    justify = "center",
                    font=('Times',18))
                    lbl1.place(x=350,y=100,width=340,height=63)

                    lbl2=Label(new_window,text=sq,
                    relief="solid",
                    background="#ffffff",
                    justify="center",
                    fg = "#333333",
                    font=("Times",17))
                    lbl2.place(x=50,y=230,width=890,height=136)

                    def simp_check(a):
                        if a==1:
                            v_tow.set(0)
                        elif a==2:
                            v_one.set(0)
                            

                    v_one=IntVar()
                    v_tow=IntVar()
                    optn1=Checkbutton(new_window,text="بله",variable=v_one,
                    activeforeground= "#fad400",
                    bg = "#00babd",
                    font=('Times',18),
                    fg = "#333333",
                    justify = "center",
                    relief="raised",
                    command=lambda:simp_check(1)
                    )
                    optn1.place(x=550,y=450,width=100,height=35)

                    optn2=Checkbutton(new_window,text="خیر",variable=v_tow,
                    activeforeground = "#fad400",
                    bg = "#00babd",
                    font=('Times',18),
                    fg = "#333333",
                    justify = "center",
                    relief="raised",
                    command=lambda:simp_check(2))
                    optn2.place(x=340,y=450,width=100,height=35)

                    btn1=Button(new_window,text="ادامه",
                    activeforeground = "#fad400",
                    bg = "#fad400",
                    fg = "#000000",
                    justify = "center",
                    relief = "raised",
                    command=new_window.destroy,font=('Times',18))
                    btn1.place(x=430,y=520,width=125,height=37)

                    root.destroy()
                create_window()    
        move()
        root.mainloop()

    root=Tk()
    root.title('psycho test')

    width=800
    height=500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    bg=PhotoImage(file="../Psychology project/bak/bc1-800.500.png")
    bg_label=Label(root,image=bg)
    bg_label.place(x=0,y=0)

    GLabel_748=Label(root)
    GLabel_748["bg"] = "#fad400"
    GLabel_748["fg"] = "#333333"
    GLabel_748["justify"] = "center"
    GLabel_748["text"] = ""
    GLabel_748.place(x=0,y=20,width=801,height=30)

    GButton_944_5=Button(root,font=("Times",10))
    GButton_944_5["bg"] = "#fe9d9d"
    GButton_944_5["fg"] = "#000000"
    GButton_944_5["justify"] = "center"
    GButton_944_5["text"] = "خروج کامل"
    GButton_944_5.place(x=930,y=0,width=70,height=25)
    GButton_944_5["command"] = GButton_944_command

    def GButton_944_command():
        exit()

    GButton_944_5=Button(root,font=("Times",10))
    GButton_944_5["bg"] = "#fe9d9d"
    GButton_944_5["fg"] = "#000000"
    GButton_944_5["justify"] = "center"
    GButton_944_5["text"] = "خروج کامل"
    GButton_944_5.place(x=930,y=0,width=70,height=25)
    GButton_944_5["command"] = GButton_944_command

    sq="""در این مرحله عناوین داستان هایی که تا اینجای کار مشاهده کردید ارائه میشوند و پس از آن
    چهار استنباط ( نتیجه گیری) متفاوت از داستان نیز ارائه میشود.لطفا مشخص نمایید که
    هر نتیجه گیری تا چه حد به دیدگاه شما شباهت دارد"""
    lbl2=Label(root,text=sq,
    relief="solid",
    background="#ffffff",
    justify="center",
    fg = "#333333",
    font=("Times",17))
    lbl2.place(x=50,y=200,width=700,height=140)

    btn1=Button(root,text="ادامه",
    activeforeground = "#fad400",
    bg = "#fad400",
    fg = "#000000",
    justify = "center",
    relief = "raised",
    command=root.destroy,font=('arial',18)).place(x=330,y=430,width=125,height=37)

    root.mainloop()
    #-----------------------------------------------------                        ui check

    def check(option):
        if(option==1):
            val2.set(0)
            val3.set(0)
            val4.set(0)
        elif(option==2):
            val1.set(0)
            val3.set(0)
            val4.set(0)
        elif(option==3): 
            val1.set(0)
            val2.set(0)
            val4.set(0)
        elif(option==4):
            val1.set(0)
            val2.set(0)
            val3.set(0)


    def next():
        global Question_no,a_first,d_last
        cont=False
        if Ansewers[Question_no-1]=='a':
            if val1.get()==1:
                a_first='3'
                cont=True
            elif val2.get()==1:
                a_first='2'
                cont=True
            elif val3.get()==1:
                a_first='1'
                cont=True
            elif val4.get()==1:
                a_first='0'
                cont=True
                
            # main_data[def_name]:"a"+selected_option    
        elif   Ansewers[Question_no-1]=='d':
                if val1.get()==1:
                    d_last='0'
                    cont=True
                elif val2.get()==1:
                    d_last='1'
                    cont=True
                elif val3.get()==1:
                    d_last='2'
                    cont=True
                elif val4.get()==1:
                    d_last='3'
                    cont=True
        else:
            if val1.get()==1:
                tmp='0'
                cont=True
            elif val2.get()==1:
                tmp='1'
                cont=True
            elif val3.get()==1:
                tmp='2'
                cont=True
            elif val4.get()==1:
                tmp='3'
                cont=True


        Question_no+=1
        if cont==False:
            messagebox.showinfo("خطا","لطفا یک گزینه را انتخاب کنید")
            Question_no-=1
            return
        elif Question_no>Total_No_Questions:
            main_data[def_name]="a"+a_first+"/"+"d"+d_last
            if len(main_data[def_name]) != 5:
                if main_data[def_name][1]=='/':
                    main_data[def_name]=main_data[def_name][:1]+'1'+'/'+main_data[def_name][2:]
                elif main_data[def_name][-1]=='d':
                    main_data[def_name]=main_data[def_name]+'1'

            win.destroy()
        else :
            val1.set(0)
            val2.set(0)
            val3.set(0)
            val4.set(0)
            question.config(text=Questions[Question_no-1])         
        
    def ran_dic(dic):
        keys=list(dic.keys())
        random.shuffle(keys)
        return [(key,dic[key]) for key in keys]

    #---------------------------------------------------------    
    p_a_list=dict() 
    a_q_list=list() 
    score=0
    main_data=dict()
    random.shuffle(list_of_sen)
    #----------------------------------------------------------
    for a in range (0,len(list_of_sen)):
        
        sub="عنوان سناریو : "+list_of_sen[a].name
        name_for_answers=list_of_sen[a].name
        def_name=list_of_sen[a].def_name
        Questions=list() #list of questions
        Ansewers=list()
        a_first=""
        d_last=""
        main_q_list=ran_dic(list_of_sen[a].main_question)
        # a_q_list.append(main_q_list)


        for i in main_q_list:
            Questions.append(i[0])
            Ansewers.append(i[1])
        Options=["بسیار مشابه","نسبتا مشابه","نسبتا متفاوت","بسیار متفاوت"]


        Total_No_Questions=len(Questions)
        Question_no=1

        win =Tk()
        win.title("Story test")
            #setting window size
        width=1000
        height=600
        screenwidth = win.winfo_screenwidth()
        screenheight = win.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        win.geometry(alignstr)
        win.resizable(width=False, height=False)

        

        root=Frame()
        root.place(width=1000,height=600)

        bg=PhotoImage(file="../Psychology project/bak/bc1-1000.600.png")
        bg_label=Label(root,image=bg)
        bg_label.place(x=0,y=0)

        def GButton_944_command():
            exit()

        GButton_944_5=Button(root,font=("Times",10))
        GButton_944_5["bg"] = "#fe9d9d"
        GButton_944_5["fg"] = "#000000"
        GButton_944_5["justify"] = "center"
        GButton_944_5["text"] = "خروج کامل"
        GButton_944_5.place(x=930,y=0,width=70,height=25)
        GButton_944_5["command"] = GButton_944_command

        GLabel_747=Label(root)
        GLabel_747["bg"] = "#fad400"
        GLabel_747["fg"] = "#333333"
        GLabel_747["justify"] = "center"
        GLabel_747["text"] = ""
        GLabel_747.place(x=0,y=20,width=1000,height=30)

        sub=Label(root,
        bg = "#dcdcdc",
        justify = "center",
        relief = "raised",
        font=('Times',18),text=sub)
        sub.place(x=350,y=100,width=340,height=63)

        question=Label(root,font=('Times',18),text=Questions[0],
        fg = "#333333",
        justify= "center",
        relief="solid",
        bg = "#ffffff"
        )
        question.place(x=50,y=210,width=900,height=55)
        
        #----------------
        val1=IntVar()
        val2=IntVar()
        val3=IntVar()
        val4=IntVar()

        option1=Checkbutton(root,text=Options[0],variable=val1,
        bg = "#dcdcdc",
        font=('arial',17),
        
        justify = "center",
        relief = "raised",
        command=lambda:check(1))
        option1.place(x=440,y=300,width=130,height=30)

        option2=Checkbutton(root,text=Options[1],variable=val2,
        bg = "#dcdcdc",
        font=('arial',17),
        justify = "center",
        relief = "raised",
        command=lambda:check(2))
        option2.place (x=440,y=350,width=130,height=30)

        option3=Checkbutton(root,text=Options[2],variable=val3,
        bg = "#dcdcdc",
        font=('arial',17),
        justify = "center",
        relief = "raised",
        command=lambda:check(3))
        option3.place(x=440,y=400,width=130,height=30)

        option4=Checkbutton(root,text=Options[3],variable=val4,
        bg = "#dcdcdc",
        font=('arial',17),
        justify = "center",
        relief = "raised",
        command=lambda:check(4))
        option4.place(x=440,y=450,width=130,height=30)
        
        next_b=Button(root,text='ادامه',
        activeforeground = "#ffffff",
        bg = "#fad400",
        font=('Times',18),
        fg = "#000000",
        justify = "center",
        relief = "raised",
        command=next)
        next_b.place(x=430,y=510,width=145,height=37)

        win.mainloop()
    #--------------------------------
    if shoro1['id']=="" or shoro1['id']==None:
        False
    elif shoro1['name']=="" or shoro1['name']==None:
        False
    elif len(main_data) <len(list_of_sen):
        False
    else:    
        final_data.update(main_data)
#---------------------------------

data_folder="../Psychology project/data/"
file_to_open=data_folder+'client.json'

try:
    with open(file_to_open,'r') as f:
            data=json.load(f)
            f.close()
except:
    messagebox.showerror("خطا","فایل مورد نظر یافت نشد")

temp_dic=dict()
temp_dic['id']=shoro1['id']
temp_dic['name']=shoro1['name']
#sorted the dictionary of scenario and data of it

temp_dic['pish']=dict(sorted(final_data.items()))

data['client'].append(temp_dic)
print(data)
try:
    with open(file_to_open,'w') as f:
        json.dump(data,f)
        f.close()    
except:
    messagebox.showerror("خطا","فایل مورد نظر یافت نشد")    
        
