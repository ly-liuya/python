import PyPDF2
# from PyPDF2.pdf import PageObject

reader1 = PyPDF2.PdfFileReader("./data/练习.pdf")
reader2 = PyPDF2.PdfFileReader("./data/watermark.pdf")

writer = PyPDF2.PdfFileWriter()

# 获取水印页
watermark_page = reader2.getPage(0)



for page_num in range(reader1.numPages):
    current_page = reader1.getPage(page_num)
    # 合并水印和当前页进行合并
    current_page.mergePage(watermark_page)
    writer.addPage(current_page)

# 将pdf写入文件
with open("./data/练习-水印.pdf",'wb') as file:
    writer.write(file)
