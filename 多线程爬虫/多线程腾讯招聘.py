import requests,threading,time
from urllib import parse
from queue import Queue
from bs4 import BeautifulSoup


class Mone(threading.Thread):
    def __init__(self,q,xc,q2):
        super().__init__()
        self.q=q
        self.q2=q2
        self.xc=xc

    def run(self):
        while self.q.qsize():
            self.tx()
    def tx(self):
        pag = self.q.get()
        url = "https://hr.tencent.com/position.php?keywords=python&start={}".format( pag)
        print("第%s页"%(pag/10))
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Cookie": "pgv_pvi=7591888896; _ga=GA1.2.328793799.1548377860; _gcl_au=1.1.93483166.1548377861; _gcl_aw=GCL.1548387641.EAIaIQobChMI88rKqYGI4AIVRiqWCh1wCQecEAEYAiAAEgKtwPD_BwE; PHPSESSID=aglj3ngrfgrtjbj1her8e208g7; __guid=65747447.764478436445523500.1551317739942.2886; pgv_si=s2617882624; monitor_count=6",
        }
        num = 3
        while num>0:
            try:
                data = requests.get(url=url, headers=head).content
                self.q2.put(data)
                break
            except:
                num-=1
        print(num,'请求次数')

class Jx(threading.Thread):
    def __init__(self,q2,n):
        self.q2=q2
        self.n=n
        super().__init__()
    def run(self):
        while True:
            if bj ==False and self.q2.qsize()==0:
                break
            try:
                print(self.n, '开始解析')
                data2 = self.q2.get(block = False)
                self.hq(data2)
                print(self.n, '解析完成')
            except:
                pass
    def hq(self,data2):
        all = BeautifulSoup(data2, 'lxml')
        need = all.find_all('tr')
        # for i in need:
        #     needget = i.find_all('a')[0].get_text()
        print(need)
if __name__ == '__main__':
    bj = True
    with open('多线程.txt', 'a', encoding='utf-8')as f:
        time_one = time.time()
        q=Queue()
        q2 = Queue()
        for j in range(0,110,10):
            q.put(j)
        mylist = []
        for i in range(1,4):
            data = Mone(q,i,q2)
            data.start()
            mylist.append(data)
        for n in range(1,4):
            data=Jx(q2,n)
            data.start()
        for m in mylist:
            m.join()
        bj =False
        time_tow=time.time()
        print(time_tow-time_one)