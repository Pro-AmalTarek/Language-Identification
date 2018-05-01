from tkinter import filedialog
from tkinter import *
from Core.Classification import *
from Core.StopWords import *
from tkinter import messagebox
class Gui:
    def __init__(self):
        self.inputText="null"
        window =Tk()
        window.geometry("700x500+100+0")
        window.title("Language Identification")
        window.configure(background='#132533')
        value=Label(text='LANGUAGE IDENTIFICATION', bg="#132533", fg="#ff80aa", font=('Buxton Sketch', 30))
        value.place(relx=0.50, rely=0.10, anchor=CENTER)
        self.text = Text(window, font=('Roboto',20), width=16, height=1)
        self.text.place(relx=0.50, rely=0.47, anchor=CENTER,width=500, height=300)
        #self.text.insert('1.0', "jjjjjj")
        Browse=Button(text='Browse', bg="#ac3973", fg="#fff", font=('Times New Roman (Headings CS)', 14),command=self.BrowseFun)
        Browse.place(relx=0.30, rely=0.87, anchor=CENTER,width=130, height=44)
        stop=Button(text='StopWords', bg="#ff80aa", fg="#132533", font=('Times New Roman (Headings CS)', 14),command=self.stopwards)

        stop.place(relx=0.50, rely=0.87, anchor=CENTER,width=130, height=44)
        # f00f0f
        body=Button(text='BiGram', bg="#ff80aa", fg="#132533", font=('Times New Roman (Headings CS)', 14),command=self.unigram)
        body.place(relx=0.70, rely=0.87, anchor=CENTER,width=130, height=44)
        mainloop()

    def BrowseFun(self):
        self.filePath = filedialog.askopenfilename(initialdir="/Gui", title="Select file")
        myfile = open(self.filePath, "r")
        self.inputText=''.join(myfile.readlines())
    def stopwards(self):
        if self.inputText=="null":
            self.inputText = self.text.get('1.0', 'end-1c')
        myDetectLanguage2=stopword()
        result=myDetectLanguage2.detect_language(self.inputText)
        messagebox.showinfo("The Result ","\t "+ result+"\t \t")

    def unigram(self):
        if self.inputText=="null":
            self.inputText=self.text.get('1.0', 'end-1c')
        myDetectLanguage=Classifier(self.inputText)
        result=myDetectLanguage.detectLanguage()
        messagebox.showinfo("The Result"," \tThis text is: "+ result+"\t \t")
        print(self.inputText)


gui=Gui()
