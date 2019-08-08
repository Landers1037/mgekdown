from mgekdown import Mgekdown

if __name__ == '__main__':
      m = Mgekdown()
      # print(m.filelist('post'))
      # print(m.read('post/weixinqrcode.md'))
      txt = m.read('post/weixinqrcode.md')
      # print(m.title(txt))
      # print(m.content(txt))
      print(m.abstract(txt))