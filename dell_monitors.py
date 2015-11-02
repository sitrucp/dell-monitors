#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import csv
import re
from datetime import datetime

def main():

	#text_file = open("Output.txt", "w")
	output = list()
	countries = ('ca','sg','cn','my','th')
	todaydate = datetime.today().strftime('%Y-%m-%d')
	
	for country in countries:
		pagenum = 1
		
		while pagenum < 6:
		
			url = "http://accessories.dell.com/sna/category.aspx?c="+country+"&category_id=6481&l=en&s=dhs&ref=3245_mh&cs=cadhs1&~ck=anav&p=" + str(pagenum)
			page = urllib2.urlopen(url).read()
			soup = BeautifulSoup(page)
				
			if soup.find("div", {"class":"rgParentH"}):
				tablediv = soup.find("div", {"class":"rgParentH"})
				tables = tablediv.find_all('table')
				data_table = tables[0] # outermost table parent =0 or no parent
				rows = data_table.find_all("tr")
				
				for row in rows:
			#		if len(row.find_parents("tr")) == 0:
					rgDescription = row.find("div", {"class":"rgDescription"})
					rgMiscInfo = row.find("div", {"class":"rgMiscInfo"})
					pricing_retail_nodiscount_price = row.find("span", {"class":"pricing_retail_nodiscount_price"})

					if rgMiscInfo: 
						delivery = rgMiscInfo.get_text().encode('utf-8')
					else:
						delivery = ''
						
					if pricing_retail_nodiscount_price:
						price = pricing_retail_nodiscount_price.get_text().encode('utf-8').replace('*', '').replace('$','').replace(',','').replace('RMB','').replace('RM','').strip()
					else:
						price = ''
						
					if rgDescription:
						orig_desc = rgDescription.get_text().encode('utf-8')
						desc = orig_desc.replace("–","-").replace("|","-").replace('Built-in','built in')
						prod_name = desc.split("-")[0].strip()
						try:
							size1 = [int(s) for s in prod_name.split() if s.isdigit()]
							size = str(size1[0])
						except:
							size = 'unknown'
						try:
							model = desc.split("-")[1].strip()
						except:
							model = desc
							
						results = str(todaydate)+","+country+","+str(pagenum)+","+orig_desc+","+desc+","+prod_name+","+size+","+model+","+delivery+","+price+","+url
						
						output.append(results)
				
				pagenum +=1
			else:
				pass
				pagenum +=1
	
	with open('output.csv', 'wb') as file:
		writer = csv.DictWriter(file, fieldnames = ['date', 'country', 'page', 'orig_desc', 'desc', 'prod_name', 'size','model', 'delivery', 'price', 'url'], delimiter = ',')
		writer.writeheader()
		for line in output:
			file.write(line + '\n')
			
			
if __name__ == '__main__':
	main()
