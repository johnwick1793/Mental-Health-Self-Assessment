from tkinter import *
from time import sleep
from PIL import ImageTk,Image
import time

class GUI(Tk):

    ques_file = "ques-ans.txt"
    part_a = 3
    part_b = 2
    part_c = 1
    part_d = 0

    #ranges
    #Excelling : [60 to 69]
    #thriving : [50 to 60)
    #surviving : [45 to 50)
    #Struggling : [40 to 45)
    #in Crisis :  < 40

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ques = 0
        self.radiovar = IntVar()

        self.geometry("500x400")
        self.iconbitmap("images\\icon.ico")
        self.title("Mental Health Monitoring System")

        self.cover = Image.open("images\\cover.jpeg")
        self.cover = ImageTk.PhotoImage(self.cover)
        self.label = Label(self,image = self.cover,bg = "#FFFFFF")
        self.label.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

        for i in range(3):
            self.label.update()
            sleep(1)
        self.label.destroy()

    def first_view(self):
        with open("start.txt","r") as file:
            message = file.read()
        
        self.frame = Frame(self,bg = "white")
        self.header = Label(self.frame,text = "One stop to monitor mental condition!!",font = "comicsansms 15",
        fg = "red")
        self.header.place(relx = 0 ,rely = 0,relwidth = 1,relheight = 0.1)

        self.message_label = Label(self.frame,text = message,fg = "blue",bg = "white",borderwidth = 5,relief = RIDGE,
        anchor = "w",font = "comicsansms 14")
        self.message_label.place(relx = 1/20,rely = 0.1,relwidth = 18/20,relheight = 0.8)
        self.start_button = Button(self.frame,text = "Start",bg = "black",fg = "lime",font = "comicsansms 15",command = self.next_ques)
        self.start_button.place(relx = 2/5,relwidth = 2/10,rely = 0.9,relheight = 0.1)

        self.frame.place(relx = 0 ,rely = 0,relwidth = 1,relheight = 1)
    def next_ques(self):

        if self.ques:

            vals = self.radiovar.get()
            self.score += vals
               

        self.frame = Frame(self,bg = "white")
        GUI.get_questions()
        self.max_score = 3*(len(GUI.questions) - 1) 
        self.part = GUI.questions[self.ques]
        self.answers = self.part[1]
        self.queslabel = Label(self,fg = "blue",font = "comicsansms 13",text = GUI.every_6(self.part[0]),
        borderwidth = 5,relief = RIDGE)
        self.queslabel.place(relx = 0,rely = 0,relwidth = 1,relheight = 2/10)

        self.next_button = Button(self,fg = "lime",bg = "black",text = "NEXT",command = self.next_ques,font = "comicsansms 13")
        self.next_button.place(relx = 2/5,rely =  8/10,relheight = 1/10,relwidth = 1/5)

        self.option1 = Radiobutton(self.frame,variable = self.radiovar,value = GUI.part_a,text = self.answers[0],
        font = "comicsansms 10",fg = "black",anchor = "w")  
        self.option2 = Radiobutton(self.frame,variable = self.radiovar,value = GUI.part_b,text = self.answers[1],
        font = "comicsansms 10",fg = "black",anchor = "w")  
        self.option3 = Radiobutton(self.frame,variable = self.radiovar,value = GUI.part_c,text = self.answers[2],
        font = "comicsansms 10",fg = "black",anchor = "w")               
        self.option4 = Radiobutton(self.frame,variable = self.radiovar,value = GUI.part_d,text = self.answers[3],
        font = "comicsansms 10",fg = "black",anchor = "w")  

        self.option1.place(relx = 1/6,relwidth = 4/6,relheight = 1/20 - 0.01,rely = 1/5 + 0.01)
        self.option2.place(relx = 1/6,relwidth = 4/6,relheight = 1/20,rely = 1/5 + 3/20)
        self.option3.place(relx = 1/6,relwidth = 4/6,relheight = 1/20,rely = 1/5 + 6/20)
        self.option4.place(relx = 1/6,relwidth = 4/6,relheight = 1/20,rely = 1/5 + 9/20)

        
        self.frame.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)
        self.ques += 1
        if self.ques == len(GUI.questions)-1:
            self.next_button.configure(text = "END")
            self.next_button.configure(command = self.end_view)
        
    def end_view(self):

        self.end_image = Image.open("images\\end.png")
        self.end_image = ImageTk.PhotoImage(self.end_image)

        self.image_label = Label(self,image = self.end_image)
        self.image_label.place(relx = 0,relheight = 1,relwidth = 0.6,rely = 0)
        self.end_frame = Frame(self,bg = "white")

        vals = self.radiovar.get()
        self.score += vals
        self.end_label = Label(self.end_frame,fg = "violet",bg = "white",text = "Test has ended and \nits results are \ndisplayed as follows",
        font = "comicsansms 15 bold")
        self.end_label.place(relx = 0 ,rely = 0,relwidth = 1,relheight = 0.2)
       

        if self.score in range(60,70):
            message = "Kudos! you are \nworking just fine\nSpread positivity :)"
            score_bg = "#43A047"
           

        elif self.score in range(50,60):
            score_bg = "#CDDC39"
            message = "Try to be more \npositive \nand stay in touch with \nyour family and friends"
           

        elif self.score in range(45,50):
            score_bg = "#FDD835"
            message = "Try to be  positive \nand stay in touch with \nyour family and friends"
           

        elif self.score in range(40,45):
            score_bg = "#F9A825"
            message = "You need to\n have a word with \nyour family and friends"
           

        else:
            score_bg = "red"
            message = "We recommend \nto consult a therapist"
        
       
        self.result_label = Label(self.end_frame,fg = "white",bg = score_bg,text = f"YOUR SCORE: {self.score} \nout of {self.max_score}\n{message}",
        font = "comicsansms 12 bold")
        self.result_label.place(relx = 0,rely = 0.3,relwidth = 1,relheight = 0.4)

        
        self.end_frame.place(relx = 0.6,rely = 0,relwidth = 0.4,relheight = 1)

        for i in range(2):
            self.end_frame.update()
            sleep(10)
        self.last_show()
    
    def last_show(self):
        self.geometry("300x700")
        self.image_frame = Frame(self,bg = "white")

        self.image1 = Image.open("images\\101.jpg")
        self.image1 = ImageTk.PhotoImage(self.image1)

        self.image2 = Image.open("images\\102.jpg")
        self.image2 = ImageTk.PhotoImage(self.image2)

        self.image_label1 = Label(self.image_frame,image = self.image1,bg = "white",borderwidth = 0)
        self.image_label1.place(relx = 0 , rely = 0,relwidth = 1,relheight = 5/10)
        
        self.image_label2 = Label(self.image_frame,image = self.image2,bg = "white",borderwidth = 0)
        self.image_label2.place(relx = 0 , rely = 5/10,relwidth = 1,relheight = 5/10)

        self.image_frame.place(relx = 0,rely = 0,relwidth = 1,relheight = 1)

        for i in range(3):
            self.image_frame.update()
            sleep(10)
        self.destroy()
    @classmethod
    def get_questions(cls):
        cls.questions = []
        with open(cls.ques_file,"r") as file:
            ques = file.readline()
            while ques:
                ans = []
                for i in range(4):
                    ans.append(file.readline().strip())
                cls.questions.append([ques,ans])
                ques = file.readline()
    @staticmethod
    def every_6(sentence):
        sentence = sentence.split()
        
        start = 0
        while start < len(sentence):
            if not start % 10:
                sentence.insert(start,"\n")
            start += 1 

        return " ".join(sentence)

if __name__ == "__main__":
    
    
    window = GUI()
    window.first_view()
    window.mainloop()

