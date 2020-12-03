# 利用python读取docx文件
'''
  1. 首先需要安装python-docx库
'''

from docx import Document

document = Document("d:\\1.docx")

for para in document.paragraphs:
    para.append('dd')
    print(para.text)
