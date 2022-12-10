# links to resources that helped me :)
# https://www.youtube.com/watch?v=5smq0hCANaE
# https://www.geeksforgeeks.org/radiobutton-in-tkinter-python/
# https://www.geeksforgeeks.org/python-program-to-find-largest-number-in-a-list/

import json
from tkinter import *
from tkinter import messagebox as mb


# creating gui window
root = Tk()
# window title
root.title('Project 2 - The Sorting Hat Quiz')
# dimensions, non re-sizeable
root.geometry("900x500")
root.resizable(False, False)
root.configure(bg='light grey')


# incorporating questions, answers, and correlating houses from json file
with open('data.json') as f:
    obj = json.load(f)
    q = (obj["ques"])
    options = (obj["options"])
    ravenclaw = (obj["ravenclaw"])
    hufflepuff = (obj["hufflepuff"])
    slytherin = (obj["slytherin"])
    gryffindor = (obj["gryffindor"])


class Quiz:
    def __init__(self) -> None:
        """
        Constructor to create an initial instance of the Quiz class
        :return: user's Hogwarts House
        """
        # sets question # to 0
        self.__num = 0
        # converts selected option to an int
        self.__opt_selected = IntVar()
        # uses radiobuttons() method to show options
        self.__opts = self.radiobuttons()
        # shows question based off of corresponding question count number
        self.__ques = self.title(self.__num)
        # displays options for corresponding question count number
        self.__displayoptions(self.__num)
        # uses buttons() method to create and activate next and quit buttons
        self.buttons()
        # sets all house counts to 0
        self.__rCount = 0
        self.__hCount = 0
        self.__gCount = 0
        self.__sCount = 0

    # creates and places next and quit buttons
    def buttons(self) -> None:
        """
        Method to create and place the next and quit buttons
        """
        nextbutton = Button(root, text='Next', command=self.__nextbutton, bg="dark grey", font=('Sitka Text', 16))
        nextbutton.place(x=790, y=415)
        quitbutton = Button(root, text="Quit", bg="dark grey", font=('Sitka Text', 16), command=root.destroy)
        quitbutton.place(x=30, y=30)

    # static method because it doesn't change any values in the quiz class, remains constant
    @staticmethod
    # displays title label
    def title(num) -> str:
        """
        Method to print the title of the quiz
        :param num: question number
        :return: title display
        """
        title = Label(root, text="The Sorting Hat Quiz", font=('Sitka Small Semibold', 20, 'underline'), bg='light grey')
        title.pack(padx=10, pady=20)
        qn = Label(root, text=q[num], font=('Sitka Small Semibold', 16), anchor='center', bg='light grey')
        qn.pack()
        return qn

    # creates and displays radio buttons based off of corresponding question count value
    def radiobuttons(self) -> str:
        """
        Method to create and print the radio buttons for the multiple choice options
        :return: radio buttons displayed for current question
        """
        val = 0
        b = []
        yp = 170
        # while option value is less than 4 (until we reach the end of the options available for current question)
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.__opt_selected, value=val + 1, font=('Sitka Text', 14),
                              anchor=W, bg='light grey')
            b.append(btn)
            btn.place(x=120, y=yp)
            val += 1
            yp += 70
        return b

    # displays text options available for current question count value
    def __displayoptions(self, num) -> str:
        """
        Method to display multiple choice options
        :param num: option item number
        :return: options desplayed for each question
        """
        val = 0
        # leaves options unselected at start of question
        self.__opt_selected.set(0)
        self.__ques['text'] = q[num]
        # displays each option for current question
        for op in options[num]:
            self.__opts[val]['text'] = op
            val += 1

    # creates and places next button
    def __nextbutton(self) -> None:
        """
        Method to navigate to the next question
        """
        # if selected option corresponds to the indicated ravenclaw option
        if self.__opt_selected.get() == ravenclaw[self.__num]:
            self.__rCount += 1
        # if selected option corresponds to the indicated hufflepuff option
        elif self.__opt_selected.get() == hufflepuff[self.__num]:
            self.__hCount += 1
        # if selected option corresponds to the indicated slytherin option
        elif self.__opt_selected.get() == slytherin[self.__num]:
            self.__sCount += 1
        # if selected option corresponds to the indicated gryffindor option
        else:
            self.__gCount += 1
        # adds 1 to question count so the program can proceed to the next question
        self.__num += 1
        # if question number count reaches the end of list of questions in json file
        if self.__num == len(q):
            self.displayresults()
        # otherwise, display options for next question
        else:
            self.__displayoptions(self.__num)

    # displays results in a pop-up box
    def displayresults(self) -> mb:
        """
        Method to determine which house applies to the user
        :return: message box with results
        """
        # creating a list of the final counts
        finalcount = [self.__rCount, self.__hCount, self.__gCount, self.__sCount]
        # if rCount is higher than the other count values
        if max(finalcount) == self.__rCount:
            rResult = "You're a Ravenclaw!\nYou value cleverness, wisdom, wit, intellectual ability, and creativity."
            mb.showinfo("Results are in...", "\n".join([rResult]))
        # if hCount is higher than the other count values
        elif max(finalcount) == self.__hCount:
            hResult = "You're a Hufflepuff!\nYou value patience, fairness, hard work, kindness, and compassion."
            mb.showinfo("Results are in...", "\n".join([hResult]))
        # if gCount is higher than the other count values
        elif max(finalcount) == self.__gCount:
            gResult = "You're a Gryffindor!\nYou value courage, bravery, nerve, chivalry, and morality."
            mb.showinfo("Results are in...", "\n".join([gResult]))
        # if sCount is higher than the other count values
        elif max(finalcount) == self.__sCount:
            sResult = "You're a Slytherin!\nYou value ambition, resourcefulness, determination, cunningness, and heritage."
            mb.showinfo("Results are in...", "\n".join([sResult]))
        # otherwise, no clear result is detectted
        else:
            uhohResult = "Inconclusive :(\nTake the quiz again! Click on your first instinct for the\n most accurate results!"
            mb.showinfo("Results are in...", "\n".join([uhohResult]))


# call quiz
quiz = Quiz()
# launch window
root.mainloop()
