'''
目标/可行性分析：给你一串字符串，你要做的是编写一个几乎没有bug的程序，使其能够检查该字符串中括号是否配对
即()是否成对(符合先左再右)，如果成对，输出成对括号数量，否则则输出"括号不配对，请检查!"
请尽可能避免特殊情况的误判
'''
#代码实现(暂时只支持英文括号)
a = str(input("请输入你要检查的字符串："))
b = 0 #成对数目
lbracket = 0 #记录左括号数
rbracket = 0 #记录右括号数
bfr1_lbracket = 0 #q全称before first one bracket，定义它方便计算后期第一个右括号前的左括号数
flag = True
exception1 = False #flag和exception1两个变量共同完善无法识别"()()()"等类似的情况
exception2 = False #处理误判")("为一对的情况
printc = False
for i in range(0,len(a)):
    if a[i] == "(":
        lbracket += 1
        flag = False
    if a[i] == ")":
        if lbracket == 0:
            print("右括号开头，错误格式！")
            exception2 = True
            break
        rbracket += 1
        flag = True
        if rbracket == 1:
            first_bracket = i
            for d in range(0,first_bracket):
                if a[d] == "(":
                    bfr1_lbracket += 1
if lbracket - rbracket != 0 and printc == False:
    printc = True
    c = abs(lbracket - rbracket)
    printc = True
    if lbracket - rbracket > 0:
        print("该字符串不成对，缺少", c, "个右括号","请检查！")
    else:
        print("该字符串不成对，缺少", c, "个左括号", "请检查！")
if lbracket == rbracket and bfr1_lbracket == lbracket or flag == True:
    b = lbracket
    if printc == False:
        if flag == True:
            if exception2 == True:
                print()
            else:
                exception1 = True
                if b == 0:
                    print("该字符串中无括号")
                print("该字符串内括号成对，且成对数量为",b)
                printc = True
print("This project was programmed by Soulake~")
print("We are looking forward to your creative brainstorm,too!")
print("latest version:18:43,Feburary 6th,2024")






