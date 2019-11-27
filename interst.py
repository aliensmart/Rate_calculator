from tkinter import *
import tkinter.messagebox


class Interest:
     
     def __init__(self, root):
         self.root = root
         self.root.title("Interest Rate Calculator")
         self.root.geometry("1350x800")
         self.root.configure(background='Gray')

         #================================Frame=============================================================

         MainFrame = Frame(self.root, bd=20, width =1350, height = 900, padx = 10, pady = 10, bg = "powder blue", relief = RIDGE)
         MainFrame.grid()

         LeftFrame = Frame(MainFrame, bd=10, width =600, height = 600, padx = 10, pady = 42, relief = RIDGE)
         LeftFrame.pack(side=LEFT)

         RightFrame = Frame(MainFrame, bd=10, width =600, height = 600, padx = 10, pady = 42, relief = RIDGE)
         RightFrame.pack(side=RIGHT)

         #================================Frame==============================================================
         LeftFrame0 = Frame(LeftFrame, bd=5, width =712, height = 143, padx = 5, bg = "powder blue", relief = RIDGE)
         LeftFrame0.grid(row=0, column=0)
         LeftFrame1 = Frame(LeftFrame, bd=5, width =712, height = 170, padx = 5, pady = 12, relief = RIDGE)
         LeftFrame1.grid(row=4, column=0)
         LeftFrame2 = Frame(LeftFrame, bd=5, width =712, height = 168, padx = 5, pady = 13, relief = RIDGE)
         LeftFrame2.grid(row=2, column=0)

         RightFrame0 = Frame(RightFrame, bd=5, width =522, height = 280, padx = 5, pady = 19, relief = RIDGE)
         RightFrame0.grid(row=1, column=0)

         #=====================================================================================================
         var1 = StringVar()
         var2 = StringVar()

         #================================== Entry and Labels ======================================================
         self.lblTitle = Label(LeftFrame0, text= "Interest Rate Calculator", padx = 17, pady = 10, bd = 1, font = ('arial', 20, 'bold')
                            , bg = "powder blue", width = 25)
         self.lblTitle.pack()

         self.lblBalance = Label(LeftFrame2, text="Please Enter the initial balance", font = ('arial', 20, 'bold')
                                , bd = 2, justify=LEFT)
         self.lblBalance.grid(row=0, column=0, padx=15)

         self.txtBalance = Entry(LeftFrame2, textvariable = var1, font = ('arial', 20, 'bold'), bd = 5, width = 14, justify=RIGHT)
         self.txtBalance.grid(row=0, column=1, padx=3, pady=10)

         self.lblYear = Label(LeftFrame2, text="Please Enter the Num. of years", font = ('arial', 20, 'bold')
                                , bd = 2, justify=LEFT)
         self.lblYear.grid(row=1, column=0)

         self.txtYear = Entry(LeftFrame2, textvariable = var2, font = ('arial', 20, 'bold'), bd = 5, width=14, justify=RIGHT)
         self.txtYear.grid(row=1, column=1, padx=3, pady=10)

         
         self.lblRateTable = Label(RightFrame0, font = ('arial', 20, 'bold'), text = "\t Pay Back").grid(row =0, column = 0)
         self.txtRateTable = Text(RightFrame0, height = 15, width = 52, bd = 16, font = ('arial', 12, 'bold'))
         self.txtRateTable.grid(row = 1, column = 0, columnspan = 3)
         


         
        
        



if __name__=="__main__":
    root = Tk()
    application = Interest(root)
    root.mainloop()
         

