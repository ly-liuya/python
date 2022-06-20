import random
import xlwt

student_name = ["关羽","张飞","赵云","黄忠","马超"]

scores = [[random.randrange(50,101) for _ in range(3)] for _ in range(5)]
# print(scores)

# 创建工作簿对象
wb = xlwt.Workbook()

# 创建工作表对象
sheet = wb.add_sheet("蜀国5上将")

# 添加表头数据
titles = ["姓名","语文","数学","英语"]
for index,titles in enumerate(titles):
    sheet.write(0,index,titles)

# 将学生姓名和喀什成绩写入单元格

for row in range(len(scores)):
    sheet.write(row+1,0,student_name[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1,col +1,scores[row][col])

# 保存excel工作表

wb.save("./data/考试成绩表.xls")