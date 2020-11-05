import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # 把每张PDF页面加入到这个可读取对象中
            pdf_writer.addPage(pdf_reader.getPage(page))
    # 把这个已合并了的PDF文档存储起来
    with open(output, 'wb') as out:
        pdf_writer.write(out)

paths = os.listdir()
for i in paths:
    if i.split('.')[-1] != 'pdf' :
        paths.remove(i)
        print("发现非pdf文件:{}".format(i))

print("开始合并pdf文件:{}".format(paths))
#"合并后"这个名字自己改吧
merge_pdfs(paths, output='合并后.pdf')
print("合并完成")
