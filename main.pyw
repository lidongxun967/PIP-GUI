from time import time
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import scrolledtext
import classpip
import time
import os
import sys
from csv import reader

def ll(i, bi):
    print(f"\r[{i * '*'}{(bi-i)*' '}]{i}/{bi}", end="")

def batpip(li):
    j=0
    for i in li:
        j+=1
        if i[0] == 'ins':
            if len(i) == 3:
                classpip.install(i[1],i[2])
            else:
                classpip.install(i[1],)
        elif i[0] == 'upg':
            if len(i) == 3:
                classpip.upgrade(i[1],i[2])
            else:
                classpip.upgrade(i[1],)
        elif i[0]=='uni':
            classpip.uninstall(i[1])
            ll(j,len(li))
        
"""pass
try:
    if sys.argv[1] == "b":
        with open(sys.argv[2], 'r') as csv_file:
            csv_reader = reader(csv_file)
            # Passing the cav_reader object to list() to get a list of lists
            list_of_rows = list(csv_reader)
            batpip(list_of_rows)
            sys.exit(0)
except :
    print("文件不存在")
"""

def OpenLog():
    os.system('start piplog.log')


def LogTxt(oa, oe):
    with open("piplog.log", "a") as f:
        if oe:
            oe = 'ok'
        else:
            oe = 'err'
        f.write('\n'+str(time.time())+'\n>'+oa +
                "\n 'ok' or 'err':"+str(oe)+'\n')


def fiveok():

    txt.config(state=NORMAL)
    text.config(state=NORMAL)
    txt.delete(1.0, END)
    text.delete(1.0, END)
    txt.insert(INSERT, "所有已安装库列表：\n"+classpip.piplist())
    text.insert(INSERT, "所有可更新库列表：\n"+classpip.outdated())
    txt.config(state=DISABLED)
    text.config(state=DISABLED)


def show():
    a = classpip.pipshow(pkn.get())
    if a[0]:
        showinfo(title=a[2]+'的详细信息', message=a[1])
    else:
        showinfo(title='详细信息显示失败', message="详细信息显示失败！原因可能为：库名称输入错误。")


def upgrade():
    a = classpip.upgrade(pkn.get(), pknv.get())
    if a[0]:
        fiveok()
        showinfo(title='更新成功', message=a[2]+"库更新成功！")
        LogTxt(a[1], a[0])
    else:
        showinfo(title='更新失败', message="库更新失败！原因可能为：库名称输入错误、网络异常。log已经计入")
        LogTxt(a[1], a[0])


def install():
    a = classpip.install(pkn.get(), pknv.get())
    if a[0]:
        fiveok()
        showinfo(title='安装成功', message=a[2]+"库安装成功！")
        LogTxt(a[1], a[0])
    else:
        showinfo(title='安装失败', message="库安装失败！原因可能为：库名称输入错误、网络异常。log已经计入")  # 后期log
        LogTxt(a[1], a[0])


def uninstall():
    a = classpip.uninstall(pkn.get())
    if a[0]:
        fiveok()
        showinfo(title='卸载成功', message=a[2]+"库卸载成功！")
        LogTxt(a[1], a[0])
    else:
        showinfo(title='卸载失败', message="库卸载失败！原因可能为：库名称输入错误。log已经计入")  # 后期log
        LogTxt(a[1], a[0])


root = Tk()
root.title("PIP GUI")
root.iconbitmap('python.ico')
root.geometry('600x700')
txt = scrolledtext.ScrolledText(root, width=40, height=30)
text = scrolledtext.ScrolledText(root, width=40, height=30)
hand = Label(root, text="PIP GUI")
hand.config(font=("宋体", 24))
hand.grid(row=0)
pkn = Entry(root)
pknv = Entry(root)

txt                                                                 .grid(
    column=0, row=2)
text                                                                .grid(
    column=1, row=2)
Label(root, text="库名称:")                                          .grid(
    row=8, column=0, sticky="WE", padx=10, pady=0)
pkn                                                                 .grid(
    row=9, column=0, sticky="WE", padx=10, pady=5)
Label(root, text="版本号（留空即禁用，更新与安装使用）:")              .grid(
    row=10, column=0, sticky="WE", padx=10, pady=0)
pknv                                                                .grid(
    row=11, column=0, sticky="WE", padx=10, pady=5)
Button(root, text="更新此库", command=upgrade)                       .grid(
    row=8, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="安装此库", command=install)                       .grid(
    row=9, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="卸载此库", command=uninstall)                     .grid(
    row=10, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="列出此库详细信息", command=show)                  .grid(
    row=11, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="手动刷新", command=fiveok)                       .grid(
    row=12, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="打开日志", command=OpenLog)                      .grid(
    row=13, column=1, sticky="WE", padx=10, pady=5)
fiveok()
txt.config(state=DISABLED)
text.config(state=DISABLED)
root.mainloop()
