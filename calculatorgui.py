from tkinter import *

first_num=sec_num=operator=None

def get_digit(digit):
    current=  box['text']
    new= current + str(digit)
    box.config(text=new)

def clear():
    box.config(text='')

def get_operator(op):
    global first_num,operator

    first_num=float(box['text'])
    operator=op
    box.config(text='')

def get_result():
    global first_num,sec_num,operator
    sec_num=float(box['text'])

    if operator== '+':
        box.config(text=str(first_num+sec_num))
    elif operator=='-':
        box.config(text=str(first_num-sec_num))
    elif operator=='*':
        box.config(text=str(first_num*sec_num))
    elif operator=="%":
        box.config(text=str(first_num*sec_num/100))
    else:
        if sec_num==0:
            box.config(text="Error")
        else:
            box.config(text=str(first_num/sec_num))

root=Tk()
root.title("Made by Sharif")
root.geometry("357x420")
root.resizable(0,0)
root.config(bg="gray")


box=Label(root,text='',width=17,bg="#ccddff",font=("Arial Bold",28),anchor='w')
box.place(x=0,y=0)

btn_c=Button(root,width=11,height=4,text='(',relief='flat',bg='white',command=lambda:get_digit("(")).place(x=0 ,y=50 )
btn_c2=Button(root,width=11,height=4,text=')',relief='flat',bg='white',command=lambda:get_digit(")")).place(x=90 ,y=50 )
btn_per=Button(root,width=11,height=4,text='%',relief='flat',bg='white',command=lambda:get_operator("%")).place(x=180 ,y=50 )
btn1=Button(root,width=11,height=4,text='1',relief='flat',bg='white',command=lambda:get_digit(1)).place(x=0 ,y=125 )
btn2=Button(root,width=11,height=4,text='2',relief='flat',bg='white',command=lambda:get_digit(2)).place(x=90 ,y=125 )
btn3=Button(root,width=11,height=4,text='3',relief='flat',bg='white',command=lambda:get_digit(3)).place(x=180 ,y=125 )
btn4=Button(root,width=11,height=4,text='4',relief='flat',bg='white',command=lambda:get_digit(4)).place(x=0 ,y=200 )
btn5=Button(root,width=11,height=4,text='5',relief='flat',bg='white',command=lambda:get_digit(5)).place(x=90 ,y=200 )
btn6=Button(root,width=11,height=4,text='6',relief='flat',bg='white',command=lambda:get_digit(6)).place(x=180 ,y=200 )
btn7=Button(root,width=11,height=4,text='7',relief='flat',bg='white',command=lambda:get_digit(7)).place(x=0 ,y=275 )
btn8=Button(root,width=11,height=4,text='8',relief='flat',bg='white',command=lambda:get_digit(8)).place(x=180 ,y=275 )
btn9=Button(root,width=11,height=4,text='9',relief='flat',bg='white',command=lambda:get_digit(9)).place(x=90 ,y=275 )
btn0=Button(root,width=11,height=4,text='0',relief='flat',bg='white',command=lambda:get_digit(0)).place(x=90 ,y=350 )
btn_dot=Button(root,width=11,height=4,text='.',relief='flat',bg='white',command=lambda:get_digit(".")).place(x=180 ,y=350 )
btn_add=Button(root,width=11,height=4,text='+',relief='flat',bg='white',command=lambda:get_operator("+")).place(x=270 ,y=275 )
btn_sub=Button(root,width=11,height=4,text='-',relief='flat',bg='white',command=lambda:get_operator("-")).place(x=270 ,y=200 )      
btn_div=Button(root,width=11,height=4,text='/',relief='flat',bg='white',command=lambda:get_operator("/")).place(x=270 ,y=50 )
btn_mul=Button(root,width=11,height=4,text='x',relief='flat',bg='white',command=lambda:get_operator("*")).place(x=270 ,y=125 )
btn_equal=Button(root,width=11,height=4,text='=',relief='flat',bg='lightblue',command=lambda:get_result()).place(x=270 ,y=350 )
btn_clear=Button(root,width=11,height=4,text='C',relief='flat',bg='white',command=lambda:clear()).place(x=0 ,y=350 )

root.mainloop()