from docx import Document
from docx.shared import Cm

# 创建word对象
document = Document()

# 向文档中插入图片( 图片路径要存在)
document.add_picture('./data/5-汽车.png',width=Cm(5.3))

# 保存文档
document.save("./data/img图片.docx")

