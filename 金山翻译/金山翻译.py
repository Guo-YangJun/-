import json
from urllib import parse,request

class Translate():
    def __init__(self,word):
        self.word=word
    def change(self):
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
        }
        url = "http://fy.iciba.com/ajax.php?a=fy"
        data = {
            "w":self.word
        }
        mydata = parse.urlencode(data)

        req=request.Request(url = url,headers = head,data = bytes(mydata,encoding = "utf-8"))
        response = request.urlopen(req).read().decode("utf-8")
        obj =json.loads(response)
        print("翻译如下：")
        try:
            for v in obj["content"]["word_mean"]:
                print(v)
        except:
            print(obj["content"]["out"])

while True:
    word = input("请输入要翻译内容：")
    data=Translate(word)
    data.change()