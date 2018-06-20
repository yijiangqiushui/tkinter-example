#coding=utf8

"""
1、创建窗口
2、添加文字
3、添加按钮
"""

import tkinter

root = tkinter.Tk()
label = tkinter.Label(root, text='Hello, GUI')
label.pack()

button1 = tkinter.Button(root, text='Button1')
button1.pack(side=tkinter.LEFT)

button2 = tkinter.Button(root, text='Button2')
button2.pack(side=tkinter.RIGHT)

root.mainloop()