def remove_blank_lines(filename):
    # 打开文件并读取内容
    with open(filename, 'r') as file:
        lines = file.readlines()

    # 删除空白行
    lines = [line.strip() for line in lines if line.strip()]

    # 重新写入文件
    with open(filename, 'w') as file:
        file.write('\n'.join(lines))

if __name__ == "__main__":
    # 输入文件名
    filename = input("请输入文件名: ")

    # 删除空白行
    remove_blank_lines(filename)
    print("空白行已删除！")
