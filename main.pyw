from time import time
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from tkinter import scrolledtext
import classpip
import time
import os
import sys
import webbrowser,json
from csv import reader
from PIL import Image, ImageTk


def gpl3(event):
    webbrowser.open("https://www.gnu.org/licenses/gpl-3.0.en.html", new=0)
def gw():
    webbrowser.open("https://ldx967.github.io/pipgui/")
def et():
    sys.exit(0)





def ma(array1, array2):
    merged_array = []
    for item1 in array1:
        found = False
        for i in range(len(array2)):
            if item1[0] == array2[i][0]:
                merged_array.append([item1[0], item1[1] + "(new)"])
                found = True
                break
        if not found:
            merged_array.append(item1)
    return merged_array


def stc(input_string):
    lines = input_string.strip().split('\n')
    lines = lines[2:]  # 忽略第一行
    array = [line.split() for line in lines]
    return array


def item_selected(event):
    item = tree.item(tree.focus())
    values = item['values']
    if values:
        v.set(values[0])


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
    l = stc(classpip.piplist())
    o = stc(classpip.outdated()) 
    d = ma(l,o)
    for item in d:
        tree.insert("", END, values=item)


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
root.geometry('600x500')
v = StringVar()
tree = Treeview(root, show="headings")
tree["columns"] = ("package", "version")
tree.heading("package", text="包")
tree.heading("version", text="版本")
tree.column("package", width=100)
tree.column("version", width=100)
tree.bind("<<TreeviewSelect>>", item_selected)
tree.configure(height=20)  # 设置高度 为5行
hand = Label(root, text="PIP GUI")
hand.config(font=("宋体", 24))
hand.grid(column=0, row=0,padx=100, pady=0)
pkn = Entry(root,textvariable=v)
pknv = Entry(root)


tree                                                               .grid(
    column=0, row=1,rowspan=16,ipadx=50)


Label(root, text="库名称:")                                          .grid(
    row=1, column=1, sticky="WE", padx=10, pady=0)
pkn                                                                 .grid(
    row=2, column=1, sticky="WE", padx=10, pady=0)
Label(root, text="版本号（留空即禁用，更新与安装使用）:")              .grid(
    row=3, column=1, sticky="WE", padx=10, pady=0)
pknv                                                                .grid(
    row=4, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="更新此库", command=upgrade)                       .grid(
    row=5, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="安装此库", command=install)                       .grid(
    row=6, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="卸载此库", command=uninstall)                     .grid(
    row=7, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="列出此库详细信息", command=show)                  .grid(
    row=8, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="手动刷新", command=fiveok)                       .grid(
    row=9, column=1, sticky="WE", padx=10, pady=5)
Button(root, text="打开日志", command=OpenLog)                      .grid(
    row=10, column=1, sticky="WE", padx=10, pady=5)
fiveok()
root.mainloop()
