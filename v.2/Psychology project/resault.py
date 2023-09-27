from os import path
import arabic_reshaper
from bidi.algorithm import get_display
import tkinter as tk
import tkinter.font as tkFont
import json
# Load the data from the json file\
file_to_open='../Psychology project/data/client.json'        
with open(file_to_open,'r') as f:
    data=json.load(f)
    f.close()

# Create the window

class App:
    


    def interface (self, root):
        #setting title
        root.title("data_resault")
        #setting window size
        width=403
        height=751
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.num=tk.Label(root)
        self.num["bg"] = "#fad400"
        ft = tkFont.Font(family='Times',size=10)
        self.num["font"] = ft
        self.num["fg"] = "#333333"
        self.num["justify"] = "center"
        self.num["text"] = "/"+str(self.totalnumber)
        self.num.place(x=170,y=20,width=70,height=25)

        name=tk.Label(root)
        name["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=13)
        name["font"] = ft
        name["fg"] = "#333333"
        name["justify"] = "center"
        name["text"] = "نام "
        name.place(x=20,y=90,width=70,height=25)

        self.name_data=tk.Label(root)
        self.name_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.name_data["font"] = ft
        self.name_data["fg"] = "#333333"
        self.name_data["justify"] = "center"
        self.name_data["text"] = ""
        self.name_data.place(x=120,y=90,width=236,height=30)

        id=tk.Label(root)
        id["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        id["font"] = ft
        id["fg"] = "#333333"
        id["justify"] = "center"
        id["text"] = "آیدی"
        id.place(x=20,y=160,width=70,height=25)

        self.id_data=tk.Label(root)
        self.id_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.id_data["font"] = ft
        self.id_data["fg"] = "#333333"
        self.id_data["justify"] = "center"
        self.id_data["text"] = ""
        self.id_data.place(x=120,y=160,width=235,height=30)

        pish=tk.Label(root)
        pish["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        pish["font"] = ft
        pish["fg"] = "#333333"
        pish["justify"] = "center"
        pish["text"] = "درجه سوگیری در پیش آزمون"
        pish.place(x=20,y=220,width=127,height=35)

        self.pish_data=tk.Label(root)
        self.pish_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.pish_data["font"] = ft
        self.pish_data["fg"] = "#333333"
        self.pish_data["justify"] = "center"
        self.pish_data["text"] = ""
        self.pish_data.place(x=190,y=220,width=163,height=36)

        pas=tk.Label(root)
        pas["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        pas["font"] = ft
        pas["fg"] = "#333333"
        pas["justify"] = "center"
        pas["text"] = "درجه سوگیری در پس آزمون"
        pas.place(x=20,y=270,width=128,height=38)

        self.pas_data=tk.Label(root)
        self.pas_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.pas_data["font"] = ft
        self.pas_data["fg"] = "#333333"
        self.pas_data["justify"] = "center"
        self.pas_data["text"] = ""
        self.pas_data.place(x=190,y=270,width=162,height=36)

        GLabel_549=tk.Label(root)
        GLabel_549["bg"] = "#ffb800"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_549["font"] = ft
        GLabel_549["fg"] = "#333333"
        GLabel_549["justify"] = "center"
        GLabel_549["text"] = "امتیازات در جلسات آموزشی"
        GLabel_549.place(x=130,y=370,width=145,height=30)

        j1=tk.Label(root)
        j1["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        j1["font"] = ft
        j1["fg"] = "#333333"
        j1["justify"] = "center"
        j1["text"] = "جلسه اول"
        j1.place(x=30,y=450,width=70,height=25)

        self.j1_data=tk.Label(root)
        self.j1_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.j1_data["font"] = ft
        self.j1_data["fg"] = "#333333"
        self.j1_data["justify"] = "center"
        self.j1_data["text"] = ""
        self.j1_data.place(x=100,y=450,width=70,height=25)

        j2=tk.Label(root)
        j2["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        j2["font"] = ft
        j2["fg"] = "#333333"
        j2["justify"] = "center"
        j2["text"] = "جلسه دوم"
        j2.place(x=210,y=450,width=70,height=25)

        self.j2_data=tk.Label(root)
        self.j2_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.j2_data["font"] = ft
        self.j2_data["fg"] = "#333333"
        self.j2_data["justify"] = "center"
        self.j2_data["text"] = ""
        self.j2_data.place(x=280,y=450,width=70,height=25)

        j3=tk.Label(root)
        j3["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        j3["font"] = ft
        j3["fg"] = "#333333"
        j3["justify"] = "center"
        j3["text"] = "جلسه سوم"
        j3.place(x=30,y=510,width=70,height=25)

        self.j3_data=tk.Label(root)
        self.j3_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.j3_data["font"] = ft
        self.j3_data["fg"] = "#333333"
        self.j3_data["justify"] = "center"
        self.j3_data["text"] = ""
        self.j3_data.place(x=100,y=510,width=70,height=25)

        GLabel_396=tk.Label(root)
        GLabel_396["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_396["font"] = ft
        GLabel_396["fg"] = "#333333"
        GLabel_396["justify"] = "center"
        GLabel_396["text"] = "جلسه چهارم"
        GLabel_396.place(x=210,y=510,width=70,height=25)

        self.j4_data=tk.Label(root)
        self.j4_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.j4_data["font"] = ft
        self.j4_data["fg"] = "#333333"
        self.j4_data["justify"] = "center"
        self.j4_data["text"] = ""
        self.j4_data.place(x=280,y=510,width=70,height=25)

        GLabel_645=tk.Label(root)
        GLabel_645["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_645["font"] = ft
        GLabel_645["fg"] = "#333333"
        GLabel_645["justify"] = "center"
        GLabel_645["text"] = "جلسه پنجم"
        GLabel_645.place(x=30,y=570,width=70,height=25)

        self.j5_data=tk.Label(root)
        self.j5_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.j5_data["font"] = ft
        self.j5_data["fg"] = "#333333"
        self.j5_data["justify"] = "center"
        self.j5_data["text"] = ""
        self.j5_data.place(x=100,y=570,width=70,height=25)

        GLabel_702=tk.Label(root)
        GLabel_702["bg"] = "#1e9fff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_702["font"] = ft
        GLabel_702["fg"] = "#333333"
        GLabel_702["justify"] = "center"
        GLabel_702["text"] = "جلسه ششم"
        GLabel_702.place(x=210,y=570,width=70,height=25)

        self.j6_data=tk.Label(root)
        self.j6_data["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times',size=10)
        self.j6_data["font"] = ft
        self.j6_data["fg"] = "#333333"
        self.j6_data["justify"] = "center"
        self.j6_data["text"] = ""
        self.j6_data.place(x=280,y=570,width=70,height=25)

        self.btn=tk.Button(root)
        self.btn["activeforeground"] = "#ffffff"
        self.btn["bg"] = "#899f9d"
        ft = tkFont.Font(family='Times',size=10)
        self.btn["font"] = ft
        self.btn["fg"] = "#000000"
        self.btn["justify"] = "center"
        self.btn["text"] = "شروع"
        self.btn["relief"] = "raised"
        self.btn.place(x=140,y=660,width=97,height=39)
        self.btn["command"] = self.GButton_288_command

    def GButton_288_command(self):
        if self.number==0:
            self.btn["text"] = "ادامه"
            
        elif self.number==self.totalnumber:
            root.destroy()
        try:    
            self.num["text"]=str(self.number+1)+"/"+str(self.totalnumber)
        except:
            self.num["text"]="None"
        try:
            self.name_data["text"]=data["client"][self.number]["name"] 
        except:
            self.name_data["text"]="None"
        try:        
            self.id_data["text"] =data["client"][self.number]["id"]
        except:
            self.id_data["text"]="None"
        #---------
        try:
            tmp=data["client"][self.number]["pish"]
            tmp=list(tmp.values())
            tmp=[int(item) for item in tmp]
            points_sum=sum(tmp)
        except:
            tmp=[]
            points_sum=0
        #--------
        try:
            self.pish_data["text"] = str(points_sum)+"/225"
        except:
            self.pish_data["text"]="None/225"
        #---------
        try:
            tmp=data["client"][self.number]["pas"]
            tmp=list(tmp.values())
            tmp=[int(item) for item in tmp]
            points_sum=sum(tmp)
        except:
            tmp=[]
            points_sum=0
        #--------
        try:
            self.pas_data["text"] = str(points_sum)+"/225"
        except:
            self.pas_data["text"] = "Non/225"
        try:
            self.j1_data["text"] = data["client"][self.number]["a1"]
        except:
            self.j1_data["text"] = ""
        try:
            self.j2_data["text"] = data["client"][self.number]["a2"]
        except:
            self.j2_data["text"] = ""
        try:
            self.j3_data["text"] = data["client"][self.number]["a3"]
        except:
            self.j3_data["text"] = ""
        try:
            self.j4_data["text"] = data["client"][self.number]["a4"]
        except:
            self.j4_data["text"] = ""
        try:
            self.j5_data["text"] = data["client"][self.number]["a5"]
        except:
            self.j5_data["text"] = ""
        try:
            self.j6_data["text"] = data["client"][self.number]["a6"]
        except:
            self.j6_data["text"] = ""
        self.number+=1

    
    def __init__(self,root):
        file_to_open='../Psychology project/data/client.json'        
        with open(file_to_open,'r') as f:
            self.data=json.load(f)
            f.close()
        self.totalnumber=len(data["client"])
        self.number=0
        self.interface(root)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()