import tkinter as tk
from tkinter import messagebox, filedialog, Text, Entry
from collections import Counter
import time
import json
import random

class Trainer:
    bgcolor = "#282828"
    correct_color = "#0f0"
    false_color = "#ff0"
    standby_color = "#fff"
    second_color = "yellow"
    third_color = "orange"
    false_color = "red"
    dict_loc = ''
    dict_len = 0
    current_word = ''
    strokeword = ''
    points = ''
    point = 0
    global canvas
    letters = {}
    userinv = ''
    correct_bar = ''
    

    def __init__(self, root):
        self.root = root

    def new_word(self):
        self.dict_len = len(open(self.dict_loc).readlines())
        self.dict_full = json.load(open(self.dict_loc))
        rand_word = random.choice(list(self.dict_full.values()))
        return rand_word

    def draw_keys(self):
        keycodes = ['s','t','k','p','w','h','r','a','o','*','e','u','f','r2','p2','b','l','g','s2','t2','d','z','1','2','3','4','5','6','7','8','9','0']
        self.letters = {'s':'s','t':'t','k':'k','p':'p','w':'w','h':'h','r':'r','a':'a','o':'o','*':'*','e':'e','u':'u','f':'f','r2':'r2','p2':'p2','b':'b','l':'l','g':'g','s2':'s2','t2':'t2','d':'d','z':'z','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','0':'0'}
        keylocs = {'s':'20|120|80|180','t':'120|120|80|80','k':'120|220|80|80','p':'220|120|80|80','w':'220|220|80|80','h':'320|120|80|80','r':'320|220|80|80','a':'320|320|80|80','o':'420|320|80|80','*':'420|120|80|180','e':'520|320|80|80','u':'620|320|80|80','f':'520|120|80|80','r2':'520|220|80|80','p2':'620|120|80|80','b':'620|220|80|80','l':'720|120|80|80','g':'720|220|80|80','t2':'820|120|80|80','s2':'820|220|80|80','d':'920|120|80|80','z':'920|220|80|80','1':'30|30|60|60','2':'130|30|60|60','3':'230|30|60|60','4':'330|30|60|60','5':'430|30|60|60','6':'530|30|60|60','7':'630|30|60|60','8':'730|30|60|60','9':'830|30|60|60','0':'930|30|60|60'}
        self.canvas = tk.Canvas(self.root, bg=self.bgcolor, highlightthickness=0)
        for i in keycodes:
            xpos = str(keylocs[i])[:str(keylocs[i]).index('|')]
            ypos = str(keylocs[i]).split('|')[1]
            width = int(str(keylocs[i]).split('|')[2])
            height = int(str(keylocs[i]).split('|')[3])
            self.letters[i] = self.canvas.create_rectangle(int(xpos), int(ypos), int(xpos)+width, int(ypos)+height,
                                                           outline=self.bgcolor, fill=self.standby_color)
            self.canvas.create_text((int(xpos)+(int(keylocs[i].split('|')[2])/2), int(ypos)+(int(keylocs[i].split('|')[3])/2)), text=i[0])
            self.canvas.pack(expand=True, fill="both")

    def draw_key(self, key, color):
        if self.canvas.itemcget(self.letters[key], "fill") != self.correct_color:
            self.canvas.itemconfig(self.letters[key], fill=self.correct_color)
            return
        elif self.canvas.itemcget(self.letters[key], "fill") == self.correct_color:
            self.canvas.itemconfig(self.letters[key], fill=self.second_color)
            return
        elif self.canvas.itemcget(self.letters[key], "fill") == self.second_color or correct_color:
            self.canvas.itemconfig(self.letters[key], fill=self.third_color)
            return

    def clear_key(self, key):
        self.canvas.itemconfig(self.letters[key], fill=self.standby_color)

    def draw_stroke(self, stroke):
        q = 0
        if isinstance(stroke, list):
            for i in stroke:
                q =+ 1 
                for j in i:
                    if q == 1:
                        self.draw_key(j.lower(), self.correct_color)
                    elif q == 2:
                        self.draw_key(j.lower(), self.second_color)
                    elif q == 3:
                        self.draw_key(j.lower(), self.third_color)

        elif isinstance(stroke, str):
            for i in stroke:
                self.draw_key(i.lower(), self.correct_color)


    def separate_sides(self, value):
        stroke = list(self.dict_full.keys())[list(self.dict_full.values()).index(value)]
        repcnt = 0
        divcnt = 0
        enable_keys = []
        if "/" in stroke:
            sides = stroke.split('/')
            divcnt = len(sides)
            for q in sides:
                for i in range(0, len(q)):  
                    count = 1;  
                    for j in range(i+1, len(q)):  
                        if(q[i] == q[j] and q[i] != ' '):  
                            count = count + 1;  
                            q = q[:j] + '0' + q[j+1:];  

                    if(count > 1 and q[i] != '0'):  
                        repcnt = count
        else:
            for i in range(0, len(stroke)):  
                count = 1;  
                for j in range(i+1, len(stroke)):  
                    if(stroke[i] == stroke[j] and stroke[i] != ' '):  
                        count = count + 1;  
                        stroke = stroke[:j] + '0' + stroke[j+1:];  

                if(count > 1 and stroke[i] != '0'):  
                    repcnt = count
        if divcnt != 0 and repcnt != 0:
            return str(stroke.replace('-','')).split('/')
        elif divcnt != 0 and repcnt == 0:
            return str(stroke.replace('-','')).split('/')
        elif divcnt == 0 and repcnt != 0:
            return stroke.replace('-','')
        elif divcnt == 0 and repcnt == 0:
            return stroke.replace('-','')
        return 'error'





    def update_word(self):
        for i in self.letters:
            self.clear_key(i)
        self.userinv.delete(0, tk.END)
        self.current_word.set(self.new_word())
        self.draw_stroke(self.separate_sides(self.current_word.get()))
        self.strokeword.set(self.separate_sides(self.current_word.get()))

    def check_word(self, event=None):
        if self.userinv.get() == self.current_word.get():
            #print('check') #{debug}
            self.canvas.itemconfig(self.correct_bar, fill=self.correct_color)
            self.point += 1
            self.points.set(str("Points: "+str(self.point)))
        else:
            #print('false') #{debug}
            self.point -= 1
            self.canvas.itemconfig(self.correct_bar, fill=self.false_color)
            self.points.set(str("Points: "+str(self.point)))
        self.update_word()

    def constant_checker(self, event=None):
        # this is a not so great way of doing this but it gets the job done!
        if self.userinv.get() != self.current_word.get():
            return
        else:
            self.canvas.itemconfig(self.correct_bar, fill=self.correct_color)
            self.point += 1
            self.points.set(str("Points: "+str(self.point)))
            self.update_word()



    def main(self):
        # Create dictionary select screen

        self.dict_loc = filedialog.askopenfilename()
        #get_full_dict()
        # GUI window configuration

        self.root.geometry("1000x455")
        self.root.configure(bg=self.bgcolor)
        self.root.resizable(False, False)
        self.root.title("Lisabet Stenography Trainer (Version 1.43)")
        self.points = tk.StringVar(self.root)
        points = tk.Label(self.root,
                        textvariable=self.points,
                        font=("arial", 20, "italic"),
                          bg=self.bgcolor, fg=self.standby_color)
        points.pack(anchor="w")
        self.strokeword = tk.StringVar(self.root)
        test = tk.Label(self.root,
                        textvariable=self.strokeword,
                        font=("arial", 20, "italic"),
                        bg=self.bgcolor, fg=self.standby_color)
        test.pack()
 
        # label
        self.current_word = tk.StringVar(self.root)
        self.current_word.set("PLACEHOLDER")
        # show new word
        #self.current_word.set(self.new_word())
 
        self.word = tk.Label(self.root,
                             textvariable=self.current_word, font=(
                                 "arial", 22, "bold"),
                             bg=self.bgcolor, fg=self.standby_color)
        self.word.pack()
        self.draw_keys()
        xpos = 20
        ypos = 0
        width = 980
        height = 10
        self.correct_bar = self.canvas.create_rectangle(int(xpos), int(ypos), int(xpos)+width, int(ypos)+height,
                                                           outline=self.bgcolor, fill=self.standby_color)

        self.userinv = tk.Entry(self.root,
                                justify=tk.CENTER,
                                font = ("arial", 18, "bold"),
                                bg=self.bgcolor, fg=self.standby_color, borderwidth=0)
        self.userinv.bind('<KeyRelease>', self.constant_checker)
        self.userinv.bind('<Return>', self.check_word)
        self.userinv.pack()
        print(self.userinv.get())


        b = tk.Button(self.root,text = "update", command = self.check_word)
        b.pack()
        self.root.mainloop()

        
 
if __name__ == '__main__':
    tnr = Trainer(tk.Tk())
    tnr.main()
