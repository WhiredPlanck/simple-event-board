#!/usr/bin/env python
#-*- coding:utf-8 -*-

from daycalc2 import days_left,is_this_year,show_year,today
from sentencelist import get_sentence
import tkinter as tk
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.creatWidgets()
        self.change_colors()
        self.one_sentence()
        self.button()
    def creatWidgets(self):
        self.labContext = tk.Label(self)
        self.labContext['text'] = "距离 {0} 年高考还有".format(show_year())
        self.labContext['font'] = ('Noto Sans',36)
        self.labContext.pack(padx='10m')

        self.labDaysNum = tk.Label(self)
        self.labDaysNum['text'] = "{}".format(days_left())
        self.labDaysNum['font'] = ('Noto Sans',48,'bold')
        #self.labDaysNum['fg'] = "#00aa00"
        self.labDaysNum.pack()

        self.labUnit= tk.Label(self)
        self.labUnit['text'] = "天"
        self.labUnit['font'] = ('Noto Sans',36)
        self.labUnit.pack()
        
        self.labGap = tk.Label(self, text="== O ==")
        self.labGap.pack()
    def change_colors(self):
        if days_left() >=300:
            self.labDaysNum.config(fg = "#00aa00")
        elif days_left() >= 200:
            self.labDaysNum.config(fg = "#aaff00")
        elif days_left() > 100:
            self.labDaysNum.config(fg = "#ffaa00")
        else:
            self.labDaysNum.config(fg = "#aa0000")
        #'''
    def one_sentence(self):
        self.sentence = tk.Label(self)
        self.sentence['text'] = '{0}'.format(get_sentence())
        self.sentence['font'] = ('Noto Sans',10,'italic')
        self.sentence.pack(expand = 1, padx = '3m')

    def button(self):
        self.aboutButton = tk.Button(self, 
                                     text = "关于",
                                     relief = 'flat',
                                     bg = '#ccc')
        self.aboutButton.pack(padx='5m',pady='3m',side='left')
        def show_about(e):
            messagebox.showinfo("关于","简易高考倒计时器\n 版本 0.4 alpha\n 使用 Python 和 tkinter 编写")
        self.aboutButton.bind("<Button - 1>", show_about)
    
        self.quit = tk.Button(self, text="退出",
                              command=self.master.destroy,
                              relief = 'flat',
                              bg = '#ccc')
        self.quit.pack(padx='5m',side="right")
            

root = tk.Tk()
root.title("简易高考倒计时器")
root.geometry('+0+0')
root.maxsize(720, 400)
root.minsize(720, 400)
app = Application(master=root)
app.mainloop()
