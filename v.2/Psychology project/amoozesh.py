from os import path
import random
import arabic_reshaper
from bidi.algorithm import get_display
from tkinter import *
from tkinter import messagebox
import json
from sys import exit

#-------------------------
class sce:    #class that get the scenario from the file

    def __init__(self,path1,def_name,jalaseh):
        self.name=str() 
        self.def_name=def_name 
        self.text_list=list() 
        self.simp_question=str() 
        self.estenbat=dict() 
        data_folder="../Psychology project/scenarios/amoozeshi/"+jalaseh+"/"
        file_to_open=data_folder+path1
        file=open(file_to_open,"r",encoding="utf-8")
        a=0
        for line in file:
            line=line.replace("\n","")
            if line =="**":
                a+=1
                continue
            if line == "":
                break
            elif a==0:
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
                self.estenbat[line[0]]=line[1]
                     
        file.close()
    def __del__(self):
        print('ok')
#-------------------------
def shoro():
        vorod_dasti=False
        root=Tk()
        width=800
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.title("شروع")


        def on_closing():
                        exit()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        GLabel_7400=Label(root)
        GLabel_7400["bg"] = "#fad400"
        GLabel_7400["fg"] = "#333333"
        GLabel_7400["justify"] = "center"
        GLabel_7400["text"] = ""
        GLabel_7400.place(x=0,y=20,width=801,height=30)


        GLabel_944=Label(root,font=("Times",15))
        GLabel_944["bg"] = "#dcdcdc"

        GLabel_944["justify"] = "center"
        GLabel_944["text"] = "جهت شروع ابتدا آیدی خود را که در گذاشته وارد کرده بودید مجددا وارد کنید و سپس روی دکمه شروع کلیک کنید"
        GLabel_944.place(x=10,y=100,width=775,height=37)

        

        GLabel_33=Label(root,font=("Times",13))
        GLabel_33["fg"] = "#333333"
        GLabel_33["justify"] = "center"
        GLabel_33["text"] = " : آیدی  "
        GLabel_33.place(x=360,y=220,width=70,height=25)

        ins_id=Entry(root,font=("Times",12))
        ins_id["bg"] = "#ffffff"
        ins_id["borderwidth"] = "1px"
        ins_id["fg"] = "#333333"
        ins_id["justify"] = "center"
        ins_id.place(x=190,y=270,width=410,height=40)

        lbl_j=Label(root,font=("arial",13),text="وارد کنید a1 تا a6 جلسه مورد نظر خود را با فرمت")
        lbl_j.pack()
        lbl_j.pack_forget()

        ent_j=Entry(root,font=("arial",13))
        ent_j["bg"] = "#ffffff"
        ent_j["borderwidth"] = "1px"
        ent_j["fg"] = "#333333"
        ent_j["justify"] = "center"
        ent_j.pack()
        ent_j.pack_forget()
        #-------------------------
        data1=dict()
        
        def custom_insert():
            nonlocal vorod_dasti
            lbl_j.pack()
            lbl_j.place(x=250,y=320,width=300,height=25)
            ent_j.pack()
            ent_j.place(x=250,y=350,width=300,height=25)
            messagebox.showinfo("هشدار","با ورود دستی ممکن است دیتابیس دچار آسیب شود")
            vorod_dasti=True

        #----------
        def insert():
            
            client_id=ins_id.get()
            next_page=True
            file_to_open='../Psychology project/data/client.json'        
            with open(file_to_open,'r') as f:
                data=json.load(f)
                f.close()
            for id_check in data["client"]:
                if id_check["id"]==client_id :
                    messagebox.showinfo("تایید","خوش آمدید "+id_check["name"])
                    client_name=id_check["name"]
                    if vorod_dasti==False :
                        jalaseh=""
                        last_j=list(id_check.keys())[-1]
                        print(last_j)
                        if last_j=="pish":
                            jalaseh="a1"
                        elif last_j=="a1":
                            jalaseh="a2"
                        elif last_j=="a2":
                            jalaseh="a3"
                        elif last_j=="a3":
                            jalaseh="a4"
                        elif last_j=="a4":
                            jalaseh="a5"
                        elif last_j=="a5":
                            jalaseh="a6"
                        elif last_j=="a6":
                            jalaseh="a7"
                        elif last_j=="a7":
                            jalaseh="a8"
                        elif last_j=="a8":
                            messagebox.showinfo("هشدار","شما جلسات آموزشی را به پایان رسانده اید لطفا این برنامه را ببندید")
                            next_page=False
                            break;
                        else:
                            messagebox.showinfo("هشدار","خطایی رخ داده است لطفا این برنامه را ببندید و به پشتیبانی اطلاع دهید")
                            next_page=False
                            break;
                    else:
                                jalaseh=ent_j.get()
                    next_page=True    
                    break;
            else:
                messagebox.showinfo("رد","آیدی مورد نظر پیدا نشد")
                next_page=False
            if  client_id=="":
                messagebox.showinfo("خطا","لطفا آیدی خود را وارد کنید")
                next_page=False
                
            if next_page==True:
                
                data1["name"]=client_name
                data1["id"]=client_id
                data1["jalaseh"]=jalaseh
                root.destroy()
        #-------       
        GButton_281=Button(root,font=("Times",18),command=insert)
        GButton_281["activeforeground"] = "#ffffff"
        GButton_281["bg"] = "#fad400"
        GButton_281["fg"] = "#000000"
        GButton_281["justify"] = "center"
        GButton_281["text"] = "شروع"
        GButton_281["relief"] = "raised"
        GButton_281.place(x=340,y=410,width=125,height=37)
        #---------------------------       
        GButton_50=Button(root,font=("Times",10),command=custom_insert)
        GButton_50["fg"] = "#000000"
        GButton_50["justify"] = "center"
        GButton_50["text"] = "ورود دستی"
        GButton_50.place(x=710,y=460,width=70,height=25)

        root.mainloop()
        return data1
#-------
def list_of_jalaseh(jalaseh):
    if jalaseh=="a1":
        data_list=[2,6,10,12,16,20,22,26,30,32,36,40,42,46,50,52,56,60,62,66,70,72,76,80,86]
    elif jalaseh=="a2":
        data_list=[3,7,11,13,17,21,23,27,31,33,37,41,43,47,51,53,57,61,63,67,71,73,77,81,87]
    elif jalaseh=="a3":
        data_list=[4,8,12,14,18,22,24,28,32,34,38,42,44,48,52,54,58,62,64,68,72,74,78,82,88]
    elif jalaseh=="a4":
        data_list=[3,10,13,20,23,33,43,53,63,73,83,4,14,24,34,44,54,64,74,84,89,90,30,40,50]
    elif jalaseh=="a5":
        data_list=[6,16,26,36,46,56,66,76,86,7,17,27,37,47,57,67,77,87,8,18,28,38,48,58,68]
    elif jalaseh=="a6":
        data_list=[2,3,10,13,20,23,33,43,53,60,63,70,73,77,78,80,83,87,88,89,90,55,65,75,85]
    elif jalaseh=="a7":
        data_list=[2,4,12,14,22,24,32,34,42,44,52,54,62,64,72,74,82,84,90,80,70,60,50,40,30]
    elif jalaseh=="a8":
        data_list=[6,8,16,18,26,28,36,38,46,48,56,58,66,68,76,78,86,88,7,17,27,37,47,57,67]
    return data_list            

#-------------------------
person=shoro()
client_name=person["name"]

#-------------------------
data_list=list_of_jalaseh(person["jalaseh"])
# print(type(data_list))

final_list=[]
tmp_lst1=[]
tmp_a=0
for i in range (0,len(data_list)+1): # change sces to (list in list)

    if tmp_a<5 : 
        tmp_lst1.append(data_list[i])    
        tmp_a+=1
    else:
        final_list.append(tmp_lst1)
        tmp_lst1=[]
        tmp_a=1
        if i!=len(data_list):
            tmp_lst1.append(data_list[i]) 


final_score=0
for reza in final_list :
    list_of_sen=list()
    for i in reza:
        i=str(i)
        sc_temp=sce("scenario"+i+".txt","scenario"+i,person["jalaseh"])
        list_of_sen.append(sc_temp)
        del sc_temp
    #-------------------------
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

        GLabel_747=Label(root)
        GLabel_747["bg"] = "#fad400"
        GLabel_747["fg"] = "#333333"
        GLabel_747["justify"] = "center"
        GLabel_747["text"] = ""
        GLabel_747.place(x=0,y=20,width=1000,height=30)

        def on_closing():
                        exit()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        lbl1=Label(root,text="عنوان سناریو : "+list_of_sen[i].name,width=50, 
                bg="#dcdcdc",

                justify="center",
                relief = "raised",
                font=("ariel", 15))
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
        lbl2.place(x=10,y=230,width=980,height=136)
        def move():
            global a
            global sc
            if a<len(sc):
                lbl2.configure(text=sc[a])
                a+=1
                root.after(100,move) # time of each scense
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

                

                    GLabel_747=Label(new_window)
                    GLabel_747["bg"] = "#fad400"
                    GLabel_747["fg"] = "#333333"
                    GLabel_747["justify"] = "center"
                    GLabel_747["text"] = ""
                    GLabel_747.place(x=0,y=20,width=1000,height=30)

                    def on_closing():
                        exit()

                    new_window.protocol("WM_DELETE_WINDOW", on_closing)


                    lbl1=Label(new_window,text="عنوان سناریو : "+list_of_sen[i].name,
                    bg = "#dcdcdc",
                    relief="raised",

                    justify = "center",
                    font=('Times',15))
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

                    def simp_check(check):
                        if check == 1:  # If option 1 is checked
                            optn2.deselect()  # Deselect option 2
                        elif check == 2:  # If option 2 is checked
                            optn1.deselect()  # Deselect option 1

                    btn1=Button(new_window,text="ادامه",
                    activeforeground = "#fad400",
                    bg = "#fad400",
                    fg = "#000000",
                    justify = "center",
                    relief = "raised",
                    command=new_window.destroy,font=('Times',18)).place(x=430,y=520,width=125,height=37)

                    root.destroy()
                create_window()    
        move()
        root.mainloop()
    #-----------------
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

    def on_closing():
                        exit()

    root.protocol("WM_DELETE_WINDOW", on_closing)


    sq="""در این مرحله عناوین داستان هایی که تا اینجای کار مشاهده کردید ارائه میشوند و پس از آن
    چهار استنباط ( نتیجه گیری) متفاوت از داستان نیز ارائه میشود
    لطفا مشخص نمایید که کدام نتیجه گیری از لحاظ معنایی بیشترین شباهت با متن رو دارد"""
    lbl2=Label(root,text=sq,
    relief="solid",
    background="#ffffff",
    justify="center",
    fg = "#333333",
    font=("Times",16))
    lbl2.place(x=50,y=230,width=691,height=136)

    btn1=Button(root,text="ادامه",
    activeforeground = "#fad400",
    bg = "#fad400",
    fg = "#000000",
    justify = "center",
    relief = "raised",
    command=root.destroy,font=('Times',18)).place(x=330,y=450,width=125,height=37)

    root.mainloop()
    #-----------------

    def check(option): #مسدود سازی گزینه های دیگر در یک چها گزینه ایی پس از انتخاب یک گزینه
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
    #---
    text_of_con=""
    def next(): #چک کردن گزینه ایی که کاربر زده
        global options,main_q_list,score,text_of_con
        if val1.get()==1:
            temp=options[0]
        elif val2.get()==1:
            temp=options[1]
        elif val3.get()==1:
            temp=options[2]
        elif val4.get()==1:
            temp=options[3]
        else:
            temp='-1'
        #--------
        if temp=='-1':
            messagebox.showinfo('خطا','لطفا یک گزینه انتخاب کنید')    
        elif dic_of_q[temp]=="t" :
            score+=1
            scr_dsp.configure(text="امتیاز:"+str(score))
            text_of_con="درست بود ! آفرین"
            win.destroy()
        else:
            text_of_con=""
            win.destroy()    
        

    #---
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
        name_for_answers=list_of_sen[a].name # حذف شود؟
        def_name=list_of_sen[a].def_name
        options=list() #list of questions
        Ansewers=list()
        dic_of_q=dict()
        main_q_list=ran_dic(list_of_sen[a].estenbat)
        


        for i in main_q_list:
            options.append(i[0])
            dic_of_q[i[0]]=i[1]
            # Ansewers.append(i[1])


        Total_No_Questions=1 ##
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

        def on_closing():
                        exit()

        win.protocol("WM_DELETE_WINDOW", on_closing)


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
        font=('Times',15),text=sub)
        sub.place(x=350,y=100,width=340,height=63)

        #------------
        val1=IntVar()
        val2=IntVar()
        val3=IntVar()
        val4=IntVar()

        option1=Checkbutton(root,text=options[0],variable=val1,
        bg = "#dcdcdc",
        font=('arial',17),
        justify = "center",
        relief = "raised",
        command=lambda:check(1))
        option1.place(x=100,y=200,width=800,height=40)

        option2=Checkbutton(root,text=options[1],variable=val2,
        bg = "#dcdcdc",
        font=('arial',17),
        justify = "center",
        relief = "raised",
        command=lambda:check(2))
        option2.place (x=100,y=270,width=800,height=40)

        option3=Checkbutton(root,text=options[2],variable=val3,
        bg = "#dcdcdc",
        font=('arial',17),
        justify = "center",
        relief = "raised",
        command=lambda:check(3))
        option3.place(x=100,y=340,width=800,height=40)

        option4=Checkbutton(root,text=options[3],variable=val4,
        bg = "#dcdcdc",
        font=('arial',17),
        justify = "center",
        relief = "raised",
        command=lambda:check(4))
        option4.place(x=100,y=410,width=800,height=40)

        scr_con=Label(root,font=('arial',10))
        scr_con["justify"] = "center"
        scr_con["relief"] = "sunken"
        scr_con["fg"]='#5fb878'
        scr_con["text"] = text_of_con
        scr_con.place(x=10,y=490,width=135,height=46)


        scr_dsp=Label(root,font=('Times',15,'bold'))
        scr_dsp["fg"] = "#333333"
        scr_dsp["justify"] = "center"
        scr_dsp["text"] = "امتیاز:"+str(score)
        scr_dsp["relief"] = "sunken"
        scr_dsp.place(x=10,y=550,width=127,height=40)
        
        next_b=Button(root,text='ادامه',
        activeforeground = "#ffffff",
        bg = "#fad400",
        font=('Times',18),
        fg = "#000000",
        justify = "center",
        relief = "raised",
        command=next)
        next_b.place(x=427,y=500,width=145,height=37)

        win.mainloop()
    if person['id']=="" or person['id']==None:
        False
    elif person['name']=="" or person['name']==None:
        False
    else:
        final_score+=score
#---------------------------------
#---------------------------------
file_to_open='../Psychology project/data/client.json'

try:
    with open(file_to_open,'r') as f:
            data=json.load(f)
            f.close()
except:
    messagebox.showerror("خطا","فایل مورد نظر یافت نشد")

for id_check in data["client"]:
    if id_check["id"]==person['id']:
        id_check[person["jalaseh"]]=final_score
        break;    
print(data)
try:
    with open(file_to_open,'w') as f:
        json.dump(data,f)
        f.close()    
except:
    messagebox.showerror("خطا","فایل مورد نظر یافت نشد")




