import PyPDF2

# 创建读取的对象
reader = PyPDF2.PdfFileReader("./data/练习.pdf")
# 创建写入的对象
write = PyPDF2.PdfFileWriter()


for page_num in range (reader.numPages):
    # 将源文件中的每一页添加到write对象中去
    write.addPage(reader.getPage(page_num))

# 通过encrypt方法加密pdf文件，参数就是设置的密码
write.encrypt("123456")

with open("./data/练习-加密.pdf",'wb')  as file:
    write.write(file)

