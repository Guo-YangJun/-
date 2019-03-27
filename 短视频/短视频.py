import json,requests,os


files = '数据'
file = os.listdir(files)
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Cookie": "pgv_pvi=7591888896; _ga=GA1.2.328793799.1548377860; _gcl_au=1.1.93483166.1548377861; _gcl_aw=GCL.1548387641.EAIaIQobChMI88rKqYGI4AIVRiqWCh1wCQecEAEYAiAAEgKtwPD_BwE; PHPSESSID=aglj3ngrfgrtjbj1her8e208g7; __guid=65747447.764478436445523500.1551317739942.2886; pgv_si=s2617882624; monitor_count=6",
}
pag =1
for j in file:
    with open(files+'/'+j,'rb')as f:
        data = f.read().decode('utf-8')
        obj = json.loads(data)
        bj = 1
        if bj>6:
            bj=1
        for i in obj['aweme_list']:
            url = i['video']['play_addr']['url_list'][0]
            video = requests.get(str(url),headers = head).content
            print(url)
            with open('视频/上海第%d页第%d个视频.mp4' % (pag, bj), 'wb')as f:
                f.write(video)
            bj+=1
    pag+=1

