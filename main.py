from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window 

class Ui(ScreenManager):
    pass

class Main(MDApp):
    def build(self):
        Window.size = (225,400)
        self.title = "calculadora"
        Builder.load_file("client/ui.kv")
        self.vars()
        return Ui()
    def num(self,*args, num:int = 0):
        if self.end == 1:
            self.end = 0
            self.root.ids.screen.text = "0"
        screen = self.root.ids.screen.text
        self.root.ids.screen.text = screen + str(num)
        if self.dat == 0 and self.root.ids.screen.text[0] == "0":
            a = list(self.root.ids.screen.text)
            a.remove(a[0])
            c=""
            for b in a:
                c += b
            self.root.ids.screen.text = c
    def ops(self,*args,op:int= 0):
        match op:
            case 0:
                self.root.ids.opSubScreen.text = "%"
            case 1:
                self.root.ids.opSubScreen.text = "/"
            case 2:
                self.root.ids.opSubScreen.text = "X"
            case 3:
                self.root.ids.opSubScreen.text = "-"
            case 4:
                self.root.ids.opSubScreen.text = "+"
        if self.root.ids.subScreen.text != "":
            self.result(op=1)
        else:
            self.root.ids.subScreen.text = self.root.ids.screen.text
            self.clear(op=1)
    def sops(self,*args,op:int= 0):
        match op:
            case 0:
                c =""
                a = list(self.root.ids.screen.text)
                a.reverse()
                try:                    
                    a.remove(a[0])
                    a.reverse()
                    for b in a:
                        c += b
                    self.root.ids.screen.text = (lambda x: "0" if len(x) <= 0 else x)(c)
                except:
                    pass
            case 1:
                if self.grade == 0 and (self.root.ids.screen.text[0] != "0" or self.dat == 1):
                    self.root.ids.screen.text = "-" + self.root.ids.screen.text
                    self.grade = 1
                else:
                    self.root.ids.screen.text = self.root.ids.screen.text.lstrip("-")
                    self.grade = 0
            case 2:
                if self.dat == 0:
                    self.root.ids.screen.text += "."
                    self.dat = 1
    def clear(self,*args,op:int = 0):
        match op:
            case 0:
                self.root.ids.subScreen.text = ""
                self.root.ids.screen.text = "0"
                self.root.ids.opSubScreen.text = ""
                self.dat = 0
                self.grade = 0
            case 1:
                self.root.ids.screen.text = "0"
                self.dat = 0
                self.grade = 0
            case 2:
                self.root.ids.subScreen.text = ""
                self.root.ids.opSubScreen.text = ""
                self.dat = 0
                self.grade = 0
    def result(self,*args,op:int = 0):
        dat = 0
        try:
            num_1 = float(self.root.ids.subScreen.text)
            ops = (lambda x: int("error") if x == "" else x)(self.root.ids.opSubScreen.text)
            num_2 = float(self.root.ids.screen.text)
        except ValueError:
            print(90)
            return
        match ops:
            case "+":
                res = num_1 + num_2
            case "-":
                res = num_1 - num_2
            case "/":
                try:
                    res = num_1 / num_2
                except ZeroDivisionError:
                    self.root.ids.screen.text = "Zero Division Error"
                    self.clear(op=2)
                    self.end = 1
                    return
            case "X":
                res = num_1 * num_2
            case "%":
                res = num_1 /100 * num_2
        try:
            if 0 == res % int(res):
                res = int(res)
            else:
                res = float(res)
                dat = 1
        except ZeroDivisionError:
            res = float(res)
            dat = 1
        if op == 0:
            self.root.ids.screen.text = str(res)
            self.clear(op=2)
            self.end = 1
            if dat == 1:
                self.dat = 1
        else:
            self.root.ids.subScreen.text = str(res)

    def vars(self,*args,**kwargs)->None:
        self.dat = 0
        self.grade = 0
        self.end = 0
if __name__ == "__main__":
    Main().run()
    
