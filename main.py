import os
from sys import exit
import easygui as g


def exec_cmd(cmd):
    cmd = os.popen(cmd)
    cmd_result = cmd.read()
    cmd.close()
    return cmd_result


a = exec_cmd('pip --version')
if a == '':
    if g.msgbox('pip未安装！请参照文章安装pip！', 'pip未安装', '打开文章'):
        os.system(
            'start https://blog.csdn.net/qq_42257666/article/details/117884849')
    exit()

g.msgbox('欢迎使用pip助手！\n您的 pip版本 / pip位置 / python版本 为：\n'+a, '版本信息')

while 1:
    r = g.choicebox("请选择要用的模式，或者按 Cancel 退出", "模式选择", [
                    "更新指定库", "列出所有库", "安装指定库", "卸载指定库", "显示指定库的详细信息"])
    if not r:
        exit()
    if r == "更新指定库":
        ec = exec_cmd('pip --outdated')
        if ec:
            k = g.enterbox(msg="需更新的库：\n"+ec+'输入你想更新的库：',
                           title='更新指定库', default='pip')
            b = os.system('pip install --upgrade ' + k)
            if b:
                g.msgbox("库更新失败！原因可能为：库名称输入错误、网络异常。", '更新失败')
            else:
                g.msgbox("库更新成功！", '更新成功')
        else:
            g.msgbox('你没有需要更新的库', '无需更新')
    elif r == "列出所有库":
        g.msgbox("所有python库：\n"+exec_cmd('pip list'), '所有库')
    elif r == '安装指定库':
        k = g.enterbox(msg='输入你想安装的库：', title='安装指定库', default='')
        b = os.system('pip install ' + k)
        if b:
            g.msgbox("库安装失败！原因可能为：库名称输入错误、网络异常。", '安装失败')
        else:
            g.msgbox("库安装成功！", '安装成功')
    elif r == "卸载指定库":
        ec = exec_cmd('pip list')
        k = g.enterbox(msg="所有库：\n"+ec+'输入你想卸载的库：', title='卸载指定库', default='')
        b = os.system('pip uninstall ' + k + ' -y')
        if b:
            g.msgbox("库卸载失败！原因可能为：库名称输入错误。", '卸载失败')
        else:
            g.msgbox("库卸载成功！", '卸载成功')
    elif r == "显示指定库的详细信息":
        ec = exec_cmd('pip list')
        k = g.enterbox(msg="所有库：\n"+ec+'输入你想显示详细信息的库：',
                       title='显示详细信息', default='pip')
        eco = exec_cmd('pip show '+k)
        if eco:
            g.msgbox("库"+k+'的详细信息：\n'+eco, '显示详细信息')
        else:
            g.msgbox("详细信息显示失败！原因可能为：库名称输入错误。", '详细信息显示失败')
