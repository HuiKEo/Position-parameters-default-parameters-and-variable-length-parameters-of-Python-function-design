########### definition function Begin ###########
def message(name, age=6, *scores, **kwargs):

    scores = sum(scores)
    result = scores
    print("name:", name, "age:", age, "result:", result, "other:", kwargs)


########### End ###########

if __name__ == '__main__':
    sign = int(input("请输入一个操作选项（整数）："))
    if sign == 0:
        name = input("请输入姓名：")
        message(name)
    elif sign == 1:
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        message(name, int(age))
    elif sign == 2:
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        score1 = int(input("请输入第一门课成绩（整数）："))
        score2 = int(input("请输入第二门课成绩（整数）："))
        message(name,int(age),score1,score2)
    elif sign == 3:
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        score1 = int(input("请输入第一门课成绩（整数）："))
        score2 = int(input("请输入第二门课成绩（整数）："))
        others = {'hobby': 'basketball'}
        message(name,int(age),score1,score2,**others)
    else:
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        score1 = int(input("请输入第一门课成绩（整数）："))
        score2 = int(input("请输入第二门课成绩（整数）："))
        others = {'height': 122, 'weight': 20}
        message(name,int(age),score1,score2,**others)