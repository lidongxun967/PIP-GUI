
import tkinter as tk
from tkinter import ttk

def string_to_array(input_string):
    lines = input_string.strip().split('\n')
    lines = lines[2:]  # 忽略第一行
    array = [line.split() for line in lines]
    return array

input_string = """
Package                        Version
------------------------------ ------------
aiohttp                        3.8.4
aiosignal                      1.3.1
altgraph                       0.17.3
anyio                          3.6.2
"""

result = string_to_array(input_string)
print(result)


import tkinter as tk
from tkinter import ttk

data = [["sdes", "6"], ["tdb", "35"], ["wr", "434"]]

# 创建Tkinter窗口
window = tk.Tk()

# 创建Treeview小部件
tree = ttk.Treeview(window)

# 定义列名
tree["columns"] = ("Column1", "Column2")

# 设置列的标题
tree.heading("Column1", text="Column 1")
tree.heading("Column2", text="Column 2")

# 调整列宽度以适应内容
tree.column("Column1", width=100, anchor=tk.CENTER)
tree.column("Column2", width=100, anchor=tk.CENTER)

# 添加数据到Treeview
for item in data:
    tree.insert("", tk.END, values=item)

# 将Treeview放置到窗口中
tree.pack()

# 启动Tkinter事件循环
window.mainloop()
