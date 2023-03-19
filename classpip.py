import os


def exec_cmd(cmd):  # 读取cmd输出结果
    cmd = os.popen(cmd)
    cmd_result = cmd.read()
    cmd.close()
    return cmd_result


def outdated():  # 可更新目录
    q = exec_cmd('pip --outdated')
    if q:
        return q
    else:
        return "全部最新"


def upgrade(k, v):  # 更新
    if v:
        v = "=="+v
    b = os.system('pip install --upgrade ' + k + v)
    if b:
        return False, 'pip install --upgrade ' + k + v, k
    else:
        return True, 'pip install --upgrade ' + k + v, k


def piplist():  # 库目录
    return exec_cmd('pip list')


def install(k, v):  # 安装
    if v:
        v = "=="+v
    b = os.system('pip install ' + k + v)
    if b:
        return False, 'pip install ' + k + v, k
    else:
        return True, 'pip install ' + k + v, k


def uninstall(k):  # 卸载
    b = os.system('pip uninstall ' + k + ' -y')
    if b:
        return False, 'pip uninstall ' + k, k
    else:
        return True, 'pip uninstall ' + k, k


def pipshow(k):  # 详细信息
    eco = exec_cmd('pip show '+k)
    if eco:
        return True, eco, k
    else:
        return False, 'pip show '+k, k
