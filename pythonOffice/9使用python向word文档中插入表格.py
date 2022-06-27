from docx import Document

# 创建
document = Document()

# 准备插入的数据
records = (
    ('亚瑟','战士英雄'),
    ('白起','坦克英雄'),
    ('赵云','刺客英雄'),
    ('女娲','法师英雄')
)

# 添加表格
table = document.add_table(rows = 1,cols=2)
table.style = "Dark List"
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "姓名"
hdr_cells[1].text = "类型"

# 为表格添加行
for name,type in records:
    row_cells = table.add_row().cells
    row_cells[0].text = name
    row_cells[1].text = type

# 保存
document.save("./data/插入表格.docx")
