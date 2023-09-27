
from os import path
import random
import arabic_reshaper
#pip install arabic-reshaper
#pip install python-bidi
from bidi.algorithm import get_display
from tkinter import *
from tkinter import messagebox
import json
from sys import exit
from collections import OrderedDict 
import time
#ui
from signup_interface import SignupInterface
from question_interface import yesnoquestion
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
            if a==0: # name of scenario
                self.name=line
                a+=1
            elif a==1: # explain of story
                reshaped_line = arabic_reshaper.reshape(line)
                self.text_list.append(get_display(reshaped_line))
            elif a==2: # simple question (bale/kheir)
                self.simp_question=line
                a+=1
            elif a==3: # for the first question of the questions target
                line=line.split(":")
                self.main_question[line[0]]=[line[1],line[2]]
                     
        file.close()
    def __del__(self):
        print('ok')



def shoro():
    
        signup_interface=SignupInterface()
        signup_interface.button.configure(command=lambda:insert(signup_interface.entry_1.get(),signup_interface.entry_2.get()))

        data1=dict()

        def insert(client_name,client_id):

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
                    break

            if client_name=="" or client_id=="":
                messagebox.showinfo("خطا","لطفا نام و آیدی خود را وارد کنید")
                next_page=False
                
            if next_page==True:
                
                data1["name"]=client_name.lower()
                data1["id"]=client_id
                signup_interface.window.destroy()
                
        signup_interface.run()

        return data1

#-------------------------
shoro1=shoro()
#----------------------
scenario_packs=[[1, 5, 9, 11, 15], [19, 21, 25, 29, 31], [35, 39, 41, 45, 49], [51, 55, 59, 61, 65], [69, 71, 75, 79, 85]]

final_data=dict()

for pack in scenario_packs :

    list_of_sen=list()
    for sen_num in pack:
        sc_temp=sce("scenario"+str(sen_num)+".txt","scenario"+str(sen_num))
        list_of_sen.append(sc_temp)
        del sc_temp;

    #-----------------------------

    for sen_num in range (0,len(list_of_sen)):  #show  main sentenses and simple question of each one

        # make window to sghow just title at first
        root2=Tk()
        root2.title('psycho test')
        
        width=1000
        height=600
        screenwidth = root2.winfo_screenwidth()
        screenheight = root2.winfo_screenheight() 
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root2.geometry(alignstr)
        root2.resizable(width=False, height=False)
        bg=PhotoImage(file="../Psychology project/bak/bc1-1000.600.png")
        bg_label=Label(root2,image=bg)
        bg_label.place(x=0,y=0)

        yellow_roban=Label(root2)
        yellow_roban["bg"] = "#fad400"
        yellow_roban["fg"] = "#333333"
        yellow_roban["justify"] = "center"
        yellow_roban["text"] = ""
        yellow_roban.place(x=0,y=20,width=1000,height=30)

        lbl1=Label(root2,text="عنوان سناریو: "+list_of_sen[sen_num].name,width=50, 
                bg="#dcdcdc",
                justify="center",
                relief="raised",
                font=("vazir", 16))
        lbl1.place(x=350,y=200,width=340,height=63)

        
    
        #schadule for close after 3 second 
        root2.after(3000,root2.destroy)
        root2.mainloop()

        #make main window
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



        def on_closing():
            exit()

        root.protocol("WM_DELETE_WINDOW", on_closing)

        

        yellow_roban=Label(root)
        yellow_roban["bg"] = "#fad400"
        yellow_roban["fg"] = "#333333"
        yellow_roban["justify"] = "center"
        yellow_roban["text"] = ""
        yellow_roban.place(x=0,y=20,width=1000,height=30)

        
        lbl1=Label(root,text="عنوان سناریو: "+list_of_sen[sen_num].name,width=50, 
                bg="#dcdcdc",
                justify="center",
                relief="raised",
                font=("vazir", 16))
        lbl1.place(x=350,y=100,width=340,height=63)
        

        a=0
        sc=list_of_sen[sen_num].text_list
        sq=list_of_sen[sen_num].simp_question
        lbl2=Label(root,
        text="",
        relief="solid",
        background='#ffffff',
        justify="center",
        font=("vazir",14))
        lbl2.place(x=50,y=230,width=890,height=136)
        def move():
            global a
            global sc
            if a<len(sc):
                lbl2.configure(text=sc[a])
                a+=1
                root.after(100,move) # time of each scense 
            elif a==len(sc):
                root.destroy()
                global sq
                questioninterf=yesnoquestion() # qi = question interface
                
                def destroy_window():
                    questioninterf.window.destroy()

                questioninterf.canvas.itemconfig(questioninterf.question, text=sq)
                onvan_text="عنوان سناریو : "+list_of_sen[sen_num].name
                questioninterf.canvas.itemconfig(questioninterf.tt, text=onvan_text)
                questioninterf.button_yes.configure(command=lambda:destroy_window())
                questioninterf.button_no.configure(command=lambda:destroy_window())
                questioninterf.run()
                    
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



    
    def on_closing():
        exit()

    root.protocol("WM_DELETE_WINDOW", on_closing)



    sq="""در این مرحله عناوین داستان هایی که تا اینجای کار مشاهده کردید ارائه میشوند و پس از آن
    چهار استنباط ( نتیجه گیری) متفاوت از داستان نیز ارائه میشود.لطفا مشخص نمایید که
    هر نتیجه گیری تا چه حد به دیدگاه شما شباهت دارد"""
    lbl2=Label(root,text=sq,
    relief="solid",
    background="#ffffff",
    justify="center",
    fg = "#333333",
    font=("vazir",14))
    lbl2.place(x=50,y=200,width=700,height=140)

    btn1=Button(root,text="ادامه",
    activeforeground = "#fad400",
    bg = "#fad400",
    fg = "#000000",
    justify = "center",
    relief = "raised",
    command=root.destroy,font=('vazir',16)).place(x=330,y=430,width=125,height=37)

    root.mainloop()
    #-----------------------------------------------------                        ui check

    

    # def next():
    #     global Question_no,a_first,d_last
    #     cont=False
    #     if Ansewers[Question_no-1]=='a':
    #         if val1.get()==1:
    #             a_first='3'
    #             cont=True
    #         elif val2.get()==1:
    #             a_first='2'
    #             cont=True
    #         elif val3.get()==1:
    #             a_first='1'
    #             cont=True
    #         elif val4.get()==1:
    #             a_first='0'
    #             cont=True
                
    #         # main_data[def_name]:"a"+selected_option    
    #     elif   Ansewers[Question_no-1]=='d':
    #             if val1.get()==1:
    #                 d_last='0'
    #                 cont=True
    #             elif val2.get()==1:
    #                 d_last='1'
    #                 cont=True
    #             elif val3.get()==1:
    #                 d_last='2'
    #                 cont=True
    #             elif val4.get()==1:
    #                 d_last='3'
    #                 cont=True
    #     else:
    #         if val1.get()==1:
    #             tmp='0'
    #             cont=True
    #         elif val2.get()==1:
    #             tmp='1'
    #             cont=True
    #         elif val3.get()==1:
    #             tmp='2'
    #             cont=True
    #         elif val4.get()==1:
    #             tmp='3'
    #             cont=True


    #     Question_no+=1
    #     if cont==False:
    #         messagebox.showinfo("خطا","لطفا یک گزینه را انتخاب کنید")
    #         Question_no-=1
    #         return
    #     elif Question_no>Total_No_Questions:
    #         main_data[def_name]="a"+a_first+"/"+"d"+d_last
    #         if len(main_data[def_name]) != 5:
    #             if main_data[def_name][1]=='/':
    #                 main_data[def_name]=main_data[def_name][:1]+'1'+'/'+main_data[def_name][2:]
    #             elif main_data[def_name][-1]=='d':
    #                 main_data[def_name]=main_data[def_name]+'1'

    #         win.destroy()
    #     else :
    #         val1.set(0)
    #         val2.set(0)
    #         val3.set(0)
    #         val4.set(0)
    #         question.config(text=Questions[Question_no-1])         
        
    def ran_dic(dic):
        keys=list(dic.keys())
        random.shuffle(keys)
        return [(key,dic[key]) for key in keys]

    def next_2(selected_item):
        global Question_no,sum_q_point,sum_q_point
        if selected_item=='+':
            sum_q_point+=int(Ansewers[Question_no-1][1])
        elif selected_item=='-':
            sum_q_point+=int(Ansewers[Question_no-1][0])
        Question_no+=1
        if Question_no>Total_No_Questions:
            main_data[def_name]=str(sum_q_point)
            sum_q_point=0
            win.destroy()
        else:
            question.config(text=Questions[Question_no-1])
        



    #---------------------------------------------------------    
    p_a_list=dict() 
    a_q_list=list() 
    main_data=dict()
    random.shuffle(list_of_sen)
    #----------------------------------------------------------
    for a in range (0,len(list_of_sen)):
        
        sub="عنوان سناریو : "+list_of_sen[a].name
        name_for_answers=list_of_sen[a].name
        def_name=list_of_sen[a].def_name
        Questions=list() #list of questions
        Ansewers=list()
        sum_q_point=0
        main_q_list=ran_dic(list_of_sen[a].main_question)
        

        for sen_num in main_q_list:
            Questions.append(sen_num[0])
            Ansewers.append(sen_num[1])


        Total_No_Questions=len(Questions)
        Question_no=1

        win =Tk()
        win.title("Psycho test")
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



        yellow_roban=Label(root)
        yellow_roban["bg"] = "#fad400"
        yellow_roban["fg"] = "#333333"
        yellow_roban["justify"] = "center"
        yellow_roban["text"] = ""
        yellow_roban.place(x=0,y=20,width=1000,height=30)

        sub=Label(root,
        bg = "#dcdcdc",
        justify = "center",
        relief = "raised",
        font=('vazir',16),text=sub)
        sub.place(x=350,y=100,width=340,height=63)

        question=Label(root,font=('vazir',16),text=Questions[0],
        fg = "#333333",
        justify= "center",
        relief="solid",
        bg = "#ffffff"
        )
        question.place(x=50,y=210,width=900,height=55)
        
        #----------------

        btn_positive=Button(root,
                            text="تناسب ندارد",
                            bg="#dcdcdc",
                            font=('vazir',15),
                            justify="center",
                            relief="raised",
                            command=lambda :next_2("-")
                            )
        btn_positive.place(x=290,y=390,width=160,height=60)

        btn_positive=Button(root,
                            text="تناسب دارد",
                            bg="#dcdcdc",
                            font=('vazir',15),
                            justify="center",
                            relief="raised",
                            command=lambda :next_2("+")
                            )
        btn_positive.place(x=580,y=390,width=160,height=60)


        

        win.mainloop()
    #--------------------------------
    if shoro1['id']=="" or shoro1['id']==None:
        False
        messagebox.showinfo("خطا","آیدی تنظیم نبود،فایل سیو نشد")
    elif shoro1['name']=="" or shoro1['name']==None:
        False
        messagebox.showinfo("خطا","نام تنظیم نبود ، فایل سیو نشد")
    elif len(main_data) <len(list_of_sen):
        False
        messagebox.showinfo("خطا","لیست سناریو ها تنظیم نبود از نظر تعدادی ، فایل سیو نشد")
    else:    
        final_data.update(main_data) #update the dictionary with the new data
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
        
