# 配合flask的markdown文本渲染
from functools import reduce
from markdown import markdown
from urllib import parse
from os import listdir
import re

class Mgekdown():
    def __init__(self):
        pass

    def filelist(self,path):
        # 读取md文件目录获取文件名称
        # 返回格式化的url格式
        templist = listdir(path)
        filelist = []
        for l in templist:
            filelist.append(parse.quote(l))

        return filelist

    def read(self,file):
        # 读取md文件内容
        with open(file, encoding='utf-8')as md_file:
            content = reduce(lambda x, y: x + y, md_file.readlines())
        return content

    def title(self,txt):
        # 读取文章标题
        title = re.search(r'title: (.*)',txt, re.M | re.I)

        return title.group(1)

    def date(self,content):
        date = re.search(r'date: (.*) ', content, re.M | re.I)
        return date.group(1)
		
    def content(self,txt):
        # 读取文章内容
        post = re.sub(r'---\n.*---', "", txt, 0, re.M | re.S)

        return post

    def abstract(self,txt):
        # 摘要文字
        txt = self.content(txt)
        abstract = re.search(r'(.*)<!--more-->',txt,re.M|re.S|re.I).group(1)

        return abstract

