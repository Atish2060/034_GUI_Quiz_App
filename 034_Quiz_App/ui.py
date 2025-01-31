import tkinter
from tkinter import  *
THEME_COLOR = "#375362"
from quiz_brain import  QuizBrain
THEME = "#375362"
score = 0
track = 0



class QuizInterface:

    def __init__(self, data: QuizBrain):
        global track
        self.question = data
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg= THEME, padx= 20, pady= 20)

        self.label = Label(text=f"Score: {score}", bg= THEME, highlightthickness= 0, fg= "white", font= ("Arial", 15, "bold") )
        self.label.grid(row = 0, column = 1 , padx=(0,0), pady= (0,35))

        self.canvas = Canvas(height= 250, width=300, bg= "white" )
        self.que = self.canvas.create_text(150 , 125 , text = f" ", font= ("Arial", 20, "italic"),width= 280)
        self.canvas.grid(row =1 , column = 0, columnspan = 2, padx=(0,0), pady= (0,45))

        self.photo_tick = PhotoImage(file= "./images/true.png" )
        self.tick = Button(height= 70, width= 80, image= self.photo_tick, bg = THEME, highlightthickness= 10, command= lambda: self.click_btn("True"))
        self.tick.grid(row = 2, column = 0,  padx=(0,0), pady= (0,35))

        self.photo_cross = PhotoImage(file="./images/false.png")
        self.cross = Button(height=70, width=80, image=self.photo_cross, bg=THEME, highlightthickness=10, command= lambda: self.click_btn("False"))
        self.cross.grid(row=2, column=1,  padx=(0,0), pady= (0,35))
        track += 1
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white", highlightthickness=0)
        q_text = self.question.next_question()
        self.canvas.itemconfig(self.que, text=q_text)

    def click_btn(self, answer):
        global  score, track
        ans = self.question.check_answer(answer)
        if ans:
            self.canvas.config(bg= "green", highlightthickness=0)
            self.canvas.itemconfig(self.que, text = f"It's right!!")
            score += 1
            self.label.config(text=f"Score: {score}", bg= THEME, highlightthickness= 0, fg= "white", font= ("Arial", 15, "bold"))
            track += 1
            self.check_end(track)
        else:
            self.canvas.config(bg="red", highlightthickness=0)
            self.canvas.itemconfig(self.que, text=f"Its wrong!!")
            track += 1
            self.check_end(track)

    def check_end(self, track_val):
        if track_val <= 10:
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.que, text=f"You have reached the end of the Quiz.\n Your score is: {score}")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")









