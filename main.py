import tkinter as tk
from tkinter import messagebox
import random
from math import ceil

    
class Mines():
    def __init__(self,root,rows:int,cols:int):
        super().__init__()
        self.rows=rows
        self.cols=cols
        self.buttons={}
        self.mine_positions=set()
        self.create_widgets()
        self.place_mines()
        self.all_good_cases()
       
    def create_widgets(self):
        for i in range(self.rows):
            for j in range(self.cols):
                button=tk.Button(width=2,height=1,command=lambda x=i,y=j :self.on_click(x,y))
                button.grid(row=i,column=j)
                #button.bind("<Button-1>",lambda x=i,y=j :self.on_click(x,y))
                #button.bind("<Button-3>",lambda x=i,y=j : self.right_click(x,y))
                self.buttons[(i,j)] = [button,False] 
        #print(self.buttons[(0,2)][1])
        
    def place_mines(self):
        mines = ceil((self.rows*self.cols*10)/100)
        while len(self.mine_positions) < mines:
            x= random.randint(0,self.rows -1)
            y= random.randint(0,self.cols -1)
            self.mine_positions.add((x,y))
            
    def all_good_cases(self):
        good_cases=[]
        for key in self.buttons:
            if not key in self.mine_positions:
                good_cases.append([key,self.buttons[key][1]])
        return good_cases
    def new_game(self):
        self.create_widgets()
        self.place_mines()
        
    def on_click(self,x,y):
        good=self.all_good_cases()
        good_key=[list(g[0] for g in good)]
        if (x,y) in self.mine_positions:
            self.buttons[(x,y)][0].config(text="*",bg="red")
            self.game_over()
            
        else:
            self.reveal(x,y)
            if (x,y) in good_key[0]:
                for g in good:
                    print(g)
                    if g[0]==(x,y):
                        g[1]=True
            if all(good[1]):
                messagebox.showinfo("Booss", "Good game")
                self.new_game()
            print(good)
                
    def right_click(self,x,y):
        print(self.buttons[(x,y)])
        if not self.buttons[(x,y)][0].cget("text")=="#":
            self.buttons[(x,y)][0].config(text="#",bg="green")
        else:
            self.buttons[(x,y)][0].config(text="",bg="grey")
    def reveal(self,x,y):
        if(x,y) in self.mine_positions or self.buttons[(x,y)][0]["text"]:
            return
            
        mine_count = 0
        for i in range(x-1,x+2):
            for j in range (y-1,y+2):
                if (i,j) in self.mine_positions:
                    mine_count+=1
        
        self.buttons[(x,y)][0].config(text=str(mine_count) if mine_count > 0 else '',bg="grey" )
        
        if mine_count == 0:
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if 0 <= i < self.rows and 0 <= j <self.cols:
                        self.reveal(i,j)
        elif mine_count >0 :
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if (i,j) in self.mine_positions:
                        if self.buttons[(x,y)][0].cget("text")=="#":
                            self.reveal(i,j)
        
    def game_over(self):
        for(x,y) in self.mine_positions:
            self.buttons[(x,y)][0].config(text="*",bg="red")
        messagebox.showerror("Looser", "Game over")
        self.new_game()
        
    
       

if __name__ =="__main__":
    #row=int(input("Nombre de ligne \n"))
    #col=int(input("Nombre de colonnes \n"))
    root= tk.Tk()
    root.title("Démineur")
    game = Mines(root,4,4)
    root.mainloop()
    