#根据学生成绩，做不同的划分

"""
大于90分表示优秀
大于80分表示良+
大于70分表示良
大于60分表示一般
其他表示不及格
"""

score = int(input("请输入成绩："))
if score > 90:
    print("优秀")
elif score>80:
    print("良+")
elif score >70:
    print("良")
elif score > 70:
    print("一般")
else:
    print("不及格")
