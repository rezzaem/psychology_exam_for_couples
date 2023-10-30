from tkinter import Tk,Canvas,Button,PhotoImage
from sys import exit

class yesnoquestion:
    def address(self,file):
        return "../Psychology project/bak/yesnoquestion/"+file
    def on_closing(self):
        exit()
    def __init__(self):
        self.window = Tk()
        # self.window.geometry("1000x600")
        # self.window.configure(bg="#FFFFFF")
        # self.window.title("Question psycho")
        # self.window.resizable(False,False)
        width=1000
        height=600
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)

        #load images
        self.image_1=PhotoImage(file=self.address("image_1.png"))
        self.image_2=PhotoImage(file=self.address("image_2.png"))
        self.button_1_image=PhotoImage(file=self.address("button_1.png"))
        self.button_2_image=PhotoImage(file=self.address("button_2.png"))
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.setup_ui()

    def setup_ui(self):

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)
        # back layer
        image_1 = self.canvas.create_image(
            500.0,
            300.0,
            image=self.image_1
        )
        image_2 = self.canvas.create_image(
            501.0,
            300.0,
            image=self.image_2
        )
        # x=50,y=230,width=890,height=136
        #text
        self.tt=self.canvas.create_text( 
            520, #x
            130,
            text="عنوان سناریو : دوست کتابخانه",
            fill="#000000",
            font=("arial bold", 20 * -1)
        )
        self.question=self.canvas.create_text(
            500.0,
            300.0,
            anchor="center",
            text="آیا استاد به سئوالات شما پاسخ داد؟",
            fill="#000000",
            font=("arial bold", 24 * -1)
        )
        #buttons
        self.button_yes = Button(
            image=self.button_1_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_yes clicked"),
            relief="flat"
        )
        self.button_yes.place(
            x=580.0,
            y=456.0,
            width=154.0,
            height=53.0
        )

        self.button_no = Button(
            image=self.button_2_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_no clicked"),
            relief="flat"
        )
        self.button_no.place(
            x=268.0,
            y=456.0,
            width=154.0,
            height=53.0
        )
    

    def run(self):
        self.window.mainloop()


if __name__=="__main__":
    interf=yesnoquestion()
    interf.run()