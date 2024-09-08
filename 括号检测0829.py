'''
目标/可行性分析：给你一串字符串，你要做的是编写一个几乎没有bug的程序，使其能够检查该字符串中括号是否配对
即()是否成对(符合先左再右)，并输出对应成对情况
请尽可能避免特殊情况的误判
'''
#代码实现(暂时只支持英文括号)
a = str(input("请输入你要检查的字符串："))
def numb(a):
    lb = 0
    rb = 0
    bl = []
    for i in enumerate(a):
        if i == "(":
            lb += 1
            bl.append("(")
        elif i == ")":
            rb += 1
            bl.append(")")
    bl = bl[::-1]
    return lb,rb,bl
def bmatch(lb,rb,bl):
    om = 0
    llb = a.rfind("(")
    frb = a.find(")")
    if lb == rb and llb < frb:
        return "括号匹配！"
    if lb == rb:
        for j in range(0,len(bl)):
            if bl[j] == "(" and bl[j+1] == ")":
                om += 1
        if om == lb:
                return "括号匹配！"
        else:
                return "括号不匹配!"
lb = (numb(a)[0])
rb = (numb(a)[1])
bl = (numb(a)[2])
print(bmatch(lb,rb,bl))




