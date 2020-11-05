# pdf_merge

用python的PyPDF2库写的pdf合并脚本，双击即可食用，会自动识别当前路径下的pdf与非pdf文件（后缀名判断），然后将所有pdf文件合并生成一个"合并后.pdf"到当前路径下

# 食用指南

### 依赖

+ python >= 3.6
+ PyPDF2库 ```pip install PyPDF2```

### 食用
把你要合并的pdf文件和pdf_merge.py塞到一个单独的文件夹中，然后在那个目录下执行
```
python pdf_merge.py
```
