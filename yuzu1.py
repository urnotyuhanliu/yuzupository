from urllib.request import urlopen as req
from bs4 import BeautifulSoup as yuzusoup

yuzu_url = 'https://skatingscores.com/unit/jpn_yuzuru_hanyu/'
#open connection grab the page
yuzu = req(yuzu_url)
#offload the content into variable
yuzu_html = yuzu.read()

yuzu.close()
#html parsing
page_yuzu = yuzusoup(yuzu_html,"html.parser")
#grab each stab
mentabs = page_yuzu.findAll("table", {"class":"men-tab"})

filename = "yuzu.csv"
f = open(filename,"w")
headers = "competition, event, scores\n"

f.write(headers)

for mentab in mentabs:
	components = mentab.findAll("tr")
	comp = components[0].text
	print(comp)
	for component in components:
		events = component.findAll("td", {"class":"l"})
		for event in events:
			eventname = event.text
			eventscores = component.findAll("td", {"class":"r"})
			print(eventname)
			for eventscore in eventscores:
				singlescore = eventscore.text
				print(singlescore)
				f.write(comp + "," + eventname + "," + singlescore + "\n")
f.close()

