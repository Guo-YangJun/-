# import requests,re
# from lxml import etree
# # from
#
# Ip = {'http':'202.169.43.219:33161','https':'194.25.1.196:3128'}
#
# head = {
#      'Cookie': 'FSSBBIl1UgzbN7N443S=g8vMT3jGwKtLpbVtguWOxmX_33WtMlx8btHl8hVk.GH1ECulvwed04fFy1qPbxVQ; insert1_cookie=40449351; Hm_lvt_0076fef7e919d8d7b24383dc8f1c852a=1551230760,1551235180; browseHistory=%5B%7B%22name%22%3A%22%E5%8C%97%E4%BA%AC%E6%8B%9C%E5%85%8B%E6%B4%9B%E5%85%8B%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E8%A5%BF%E5%AE%89%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22MnF6Rnc2czFmWw%3D%3D%5Cn%22%7D%2C%7B%22name%22%3A%22%E5%8C%97%E4%BA%AC%E6%8B%9C%E5%85%8B%E6%B4%9B%E5%85%8B%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E6%B7%B1%E5%9C%B3%E5%88%86%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22cXdnO3FnLH05MQ%3D%3D%5Cn%22%7D%2C%7B%22name%22%3A%22%E6%98%86%E5%B1%B1%E5%90%89%E7%BA%B3%E5%B0%94%E5%85%B1%E4%BA%AB%E5%8D%95%E8%BD%A6%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%22%2C%22encryStr%22%3A%22bGNBRmMxOXtb%5Cn%22%7D%2C%7B%22name%22%3A%22%E4%BA%91%E5%8D%97%E6%95%99%E8%82%B2%E5%87%BA%E7%89%88%E7%A4%BE%E6%95%99%E8%82%B2%E4%B9%A6%E5%BA%97%22%2C%22encryStr%22%3A%22enZ9bGdBY3p2aQ%3D%3D%5Cn%22%7D%5D; Hm_lpvt_0076fef7e919d8d7b24383dc8f1c852a=1551237278; FSSBBIl1UgzbN7N443T=3XrKxgwSC_uZf2XAk0v4NM0Sxg7UQhgSYSk68qtCooNm.YlUrAogZWGT64JrvmOsQ.mjuU2beS4ECQTu5BFqCVG4lP3.93rw_VYSlyUKukoRXBTqx.XLmPeW.53P90qnNYTOJYPh8Ou2y.R30q4C0I.koUuVj4BMoTVqYzDf.dYVv8A0mCyNIDZ.K_.KCXP0FM5AYsEsPsqC60YC64xxl2oIFn64Av24Xkkcc04gOrmPcMBFNYijfFinkpjNvaC2lOCD3XNZD_js5sglD2o5Dj3Aqr.9PgqKUd6bbmG0QaYidtBPSKurj.t3QQhynLTuraBa',
#      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
# }
#
# obj = requests.get("https://api.bilibili.com/x/v1/dm/list.so?oid=77659537",headers = head,proxies =Ip).content.decode('utf-8')
# print(obj)
# # data = re.findall(r'<d[\d\D]*?>([\d\D]*?)</d>',obj,re.S)
# data = re.findall(r'<d[\s\S]*?>([\s\S]*?)</d>',obj,re.S)
# print(data)


from selenium import webdriver
from lxml import etree

#这里路径是我本地路径
driver = webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\爬虫\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get('https://api.bilibili.com/x/v1/dm/list.so?oid=77659537')
html = etree.HTML(driver.page_source.encode('utf-8'))
data = html.xpath('//d/text()')

with open('哔哩哔哩弹幕.txt','a',encoding='utf-8')as f:
    for i in data:
        f.write(i+'\n')
