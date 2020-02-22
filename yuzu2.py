from urllib.request import urlopen as req
from bs4 import BeautifulSoup as yuzusoup

yuzu_url = 'https://skatingscores.com/2020/gpcan/long/jpn_yuzuru_hanyu/'
yuzu = req(yuzu_url)
yuzu_html = yuzu.read()
yuzu.close()
page_yuzu = yuzusoup(yuzu_html,"html.parser")


filename = "yuzu.txt"
f = open(filename,"w")
#headers = "competition, event, scores\n"
#f.write(headers)
comp = page_yuzu.h1.text
print(comp)

s = page_yuzu.findAll('tr')

def elementscore(s):
	row = ""
	for tr in s:
		tds = tr.findAll('td')
		row += '\n'
		for tdele in tds:
			#row.append(tdele.text)
			row += tdele.text + '|'
	return row

print(elementscore(s[4:17])+'\n'+elementscore(s[17:18]) + elementscore(s[27:28]))

f.write(elementscore(s[4:17])+'\n'+elementscore(s[17:18]) + elementscore(s[27:28]))
f.close()