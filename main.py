from tkinter import *
from caculator.Interp import *
from caculator.nodes import *
from graph.graph import Graph
class App:
    def __init__(self):
        self.root=Tk()
        self.width=300
        self.height=400
        self.current='home'
        self.root.geometry(f'{self.width}x{self.height}')
        self.tags=[]
        self.points=[]
    def base(self):
        self.remove_tags()
        print(self.tags)
        home=Button(self.root,text='home',command=self.home)
        graph=Button(self.root,text='graph',command=self.graph)
        home.place(x=self.width/10,y=0)
        graph.place(x=self.width/2,y=0)
    def remove_tags(self):
        for t in self.tags:
            try:
                t.destroy()

            except:
                t.pack_forget()
        print(self.tags)
        self.tags=[]
    def solveeq(self,eq):
        t=tokenize(eq).generate()
        p=Parse(t).parse()
        #print(p)
        i=interp(p).traverse(p)
        return i
    def graph(self):
        self.base()

        for i in range(1,6):
            self.equations=Entry(self.root,name=f'eq{i}')
            self.tags.append(self.equations)
            self.tags[-1].place(x=self.width/5,y=0+(i*50))
        self.showgraph=Button(self.root,text='show graph',command=self.show_graph)
        self.tags.append(self.showgraph)
        self.showgraph.place(x=self.width/3,y=self.height/1.3)
    def show_graph(self):
        graph=Graph()
        for i in range(len(self.tags)):
            for x in range(graph.currentframe[0],graph.currentframe[1]):
                try:
                    for i in range(len(self.tags)):
                        t=list(self.tags[i].get())
                
                        new_eq=self.create_eq(t,x*-1)
                        new_string=self.list_to_string(new_eq)
                        if new_string!='':
                            p=[x,self.solveeq(new_string)]
                            if p not in self.points:
                                self.points.append(p)
        
                except Exception as e:
                    pass
        
        graph.coor=self.points
        graph.main()
    def list_to_string(self,list):
        new=''
        for l in list:
                    new+=str(l)
        return new

    def create_eq(self,eq,target):
        for e in range(len(eq)):
            if eq[e]=='x':
                eq[e]=float(target)
                break
        return eq
            
                
    def home(self):
        self.base()
        self.input=Entry(self.root)
        
        #self.graph=Button(self.root,text='pi',command=self.addpi)
        self.texts=Scrollbar(self.root,width=500)
        self.viewbox=Listbox(self.root,yscrollcommand=self.texts.set,width=500,height=500)
        self.tags.append(self.input)
        self.tags.append(self.texts)
        self.tags.append(self.viewbox)
        print(self.tags)

        self.root.bind('<Return>',self.solve)
        self.input.place(x=self.width/5,y=self.height/15)
        #self.pi.pack()
        self.viewbox.place(y=self.width/7)
        self.texts.config(command=self.viewbox.yview)
    def addpi(self):
        self.input.insert(END,'π')
    def solve(self,event=None):
        print(self.input.get())
        self.viewbox.insert(END,self.input.get())
        i=self.solveeq(self.input.get())
        self.viewbox.insert(END,i)
        self.input.delete(0,END)
    def main(self):
        if self.current=='home':
            self.home()
        elif self.current=='graph':
            self.graph()
        self.root.mainloop()


App().main()