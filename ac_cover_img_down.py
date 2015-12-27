#coding=utf-8
import urllib
import urllib2
import os
cover='http://cover.acfunwiki.org/cover.php'
face='http://cover.acfunwiki.org/face.php'
now=1
local=os.getcwd()+'\\download\\'
url_1=face#设置来源
exist=0
success=0
fail=0
all=0
def download(num,yes):
    global now
    global exist
    global success
    global fail
    global all
    try:#创建目录
        os.makedirs(local)
    except WindowsError:
        None
    if num >0:
        while now<=num:
            url= urllib2.urlopen(url_1).geturl()
            file= url[url.rfind('/')+1:]
            if os.path.exists(local+file):
                print now,'X',file,u'已存在'
                exist=exist+1
                if yes==0:
                    now=now+1
            else:
                try:#下载
                    urllib.urlretrieve(url,local+file)
                    print now,'√',file,u'下载成功'
                    success=success+1
                    now=now+1
                except IOError:
                    print now,'X',file,u'下载失败！！'
                    fail=fail+1
                    if yes==0:
                        now=now+1
            all=all+1
    print u'结束'
    print u'共下载',str(all),u'成功',str(success),u'已存在',str(exist),u'失败',str(fail)
    now=1
    num=0
    yes=0
    all=0
    main()

def main():
    input=raw_input(u'输入下载个数：')
    print u'当前来源：',url_1
    print u'下载目录:',local
    download(int(input),1)#参数二为失败或已存在文件是否不算入已下载量'now'(是1/否0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print u'######\n'
        print u'用户中断'
