from docx import Document

# 创建文档对象

document = Document("./data/demo.docx")
print(document)
for index,p in enumerate(document.paragraphs):
    print(index,p.text)