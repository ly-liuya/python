
import xlrd

wb = xlrd.open_workbook("./data/演示1.xlsx")

# 获取工作表名称
sheetnames = wb.sheet_names()
print(sheetnames)

# 通过指定的工作表名称获取工作表对象

sheet = wb.sheet_by_name(sheetnames[0])
# 获取工作表中的行数和列表
print(sheet.nrows,sheet.ncols)

#获取指定单元格里面的值
# content = sheet.cell_value(第几行,第几列)

for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell(row,col).value
        if row > 0:
            # col为0 ，表示第一列，将第一列的日期数据处理成年月日格式
            if col == 0 :
                value = xlrd.xldate_as_tuple(value,0)
                value = f"{value[0]}年{value[1]:>02d}月{value[2]:>02d}日"
            # 其他的number类型处理为保留2位的数字小数
            else:
                value = f"{value:.2f}"
        print(value,end="\t")
    print()