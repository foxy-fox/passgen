#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib
import tkinter as tk
from tkinter import Grid
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
from random import choice

#classes
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W, pady=10, padx=10)        
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(8, weight=31)
        
    def create_widgets(self):        
        #scale
        self.searchlabel = tk.Label(self)
        self.searchlabel["text"] = "Passwortlänge:"
        self.searchlabel.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
        
        self.passlen = tk.Scale(self, from_=8, to=36, orient=tk.HORIZONTAL, length=356)
        self.passlen.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
        self.passlen["command"] = self.generate_password
        self.passlen.set(24)
        
        self.spacer = tk.Label(self)
        self.spacer["text"] = ""
        self.spacer.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
        
        #password
        self.searchlabel = tk.Label(self)
        self.searchlabel["text"] = "Passwort:"
        self.searchlabel.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
        
        self.initialPassText = tk.StringVar()
        self.passtext = tk.Entry(self, textvariable=self.initialPassText, width=44)
        self.passtext.grid(row=4, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
        self.passtext["state"] = "readonly"
        
        self.spacer = tk.Label(self)
        self.spacer["text"] = ""
        self.spacer.grid(row=5, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
                
        #checkbox
        self.useSpecial = tk.BooleanVar()
        self.useSpecial.set(True)
        self.useSpecialCb = tk.Checkbutton(self, variable = self.useSpecial)
        self.useSpecialCb["text"] = "Sonderzeichen benutzen"
        self.useSpecialCb["command"] = self.generate_password
        self.useSpecialCb.grid(row=6, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
         
        #special field
        self.special = tk.StringVar()
        self.special.set("!#$%&()*+,-.:;<=>?@[]_{|}~")
        self.specialtext = tk.Entry(self, textvariable=self.special, width=44)
        self.specialtext.grid(row=7, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
        self.specialtext["state"] = "readonly"
        self.specialtext.bind("<KeyRelease>", self.key_release)
        
        self.spacer = tk.Label(self)
        self.spacer["text"] = ""
        self.spacer.grid(row=8, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
        
        #button
        self.genbtn = tk.Button(self, width=32)
        self.genbtn["text"] = "generieren"
        self.genbtn["command"] = self.generate_password
        self.genbtn.grid(row=9, column=0, sticky=tk.N+tk.S+tk.E+tk.W)   
        
    def key_release(self, event):
        if event.keysym != "Return": 
            self.generate_password()
               
    def special_was_used(self):
        if len(self.special.get()) == 0:
            return True
        for letter in self.special.get():
            if letter in self.initialPassText.get():
                return True
        return False
            
    def number_was_used(self):
        for digit in digits:
            if digit in self.initialPassText.get():
                return True
        return False

    def lowercase_was_used(self):
        for letter in ascii_lowercase:
            if letter in self.initialPassText.get():
                return True
        return False

    def uppercase_was_used(self):
        for letter in ascii_uppercase:
            if letter in self.initialPassText.get():
                return True
        return False
    
    def generate_password(self, event=None):
        passlenght = self.passlen.get()
        password = ""
        if self.useSpecial.get():
            self.specialtext["state"] = "normal"
        else:
            self.specialtext["state"] = "readonly"
        for j in range(int(passlenght)):
            if self.useSpecial.get():
                password += choice(ascii_letters + digits + self.special.get())
            else:
                password += choice(ascii_letters + digits)
        app.initialPassText.set(password)    
        #copy password to clipboard
        app.clipboard_clear()
        app.clipboard_append(password)
        #check for special chars
        if self.useSpecial.get() and not self.special_was_used():
            self.generate_password()
        #check for numbers
        if not self.number_was_used():
            self.generate_password()
        #check for lower case letters
        if not self.lowercase_was_used():
            self.generate_password()
        #check for upper case letters
        if not self.uppercase_was_used():
            self.generate_password()
           
#application
root = tk.Tk()
root.resizable(width=True, height=True)
root.title("Passwortgenerator")
app = Application(master=root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
root.bind("<Return>", app.generate_password)
app.generate_password()
app.mainloop()
