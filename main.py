import os
from sys import exit

print("欢迎使用pip助手！\n您的 pip版本 / pip位置 / python版本 为：")
a = os.system("pip --version")
if a:
	print("pip未安装！请参照 https://blog.csdn.net/pythonxiaopeng/article/details/109642099 文章安装pip！")
	os.system("pause")
	exit()

xx = "更新库输1，列出库输2，安装库输3，卸载库输4,显示指定库的详细信息输5： "


while 1:
	while 1:
		try:
			c = int(input(xx))
		except ValueError:
			print("请输入数字！")
		else:
			break
	if c == 1:
		print("需更新的库：")
		os.system("pip --outdated")

		k = input("输入你需更新的库名称: ")
		cmd = f"pip install --upgrade {k}"
		print (f">{cmd}")

		a = os.system(cmd)
		if a:
			print("库更新失败！原因可能为：库名称输入错误、网络异常。")
		else:
			print("库更新成功！")

	elif c == 2:
		print("所有python库：")
		os.system("pip list")

	elif c == 3:
		k = input("输入你需安装的库名称: ")
		cmd = f"pip install {k}"
		print (f">{cmd}")

		a = os.system(cmd)
		if a:
			print("库安装失败！原因可能为：库名称输入错误、网络异常。")
		else:
			print("库安装成功！")

	elif c == 4:
		print("所有python库：")
		os.system("pip list")

		k = input("输入你需卸载的库名称: ")
		cmd = f"pip uninstall {k}"
		print (f">{cmd}")

		a = os.system(cmd)
		if a:
			print("库卸载失败！原因可能为：库名称输入错误。")
		else:
			print("库卸载成功！")

	elif c == 5:
		print("所有python库：")
		os.system("pip list")

		k = input("输入你需显示详细信息的库名称: ")

		a = os.system(f"pip show {k}")
		if a:
			print("库详细信息显示失败！原因可能为：库名称输入错误。")

	else:
		print("请输入1-5的数字！")

	y = input("处理已完成！是否继续？(Y,n)")
	if y == "n":
		print("感谢您使用本软件！按任意键退出···")
		os.system("pause>nul")

		break

	elif y == "Y":
		os.system("cls")
	else:
		print("请输入(Y,n)（区分大小写）")
