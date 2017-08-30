from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display
from sqlalchemy import create_engine
import psycopg2, time
import os, datetime,re


def victor_scrapping():
	
	display = Display(visible = 0, size = (1200, 900))
	display.start()

	try:
		Victor = webdriver.Chrome(executable_path=os.path.abspath("/usr/bin/chromedriver"))
		Victor.get("https://partners.victorsaffiliates.com/login.asp")
		username = Victor.find_element_by_name("username")
		username.clear()
		username.send_keys("betfyuk")
		password = Victor.find_element_by_name("password")
		password.clear()
		password.send_keys("dontfuckwithme")
		password.send_keys(Keys.RETURN)
		time.sleep(20)
		mtd_valArr = []
		table = Victor.find_element(by=By.ID, value = "dashboard_quick_stats")
		mtds_val = table.find_element(by=By.CLASS_NAME, value = "row_light_color")
		for mtd_val in mtds_val.find_elements_by_tag_name("td"):
			mtd_valArr.append(mtd_val.text)
		time.sleep(2)
		Victor.find_element_by_xpath('//*[@id="dashboard"]/div[1]/div[1]/div/div[1]/div/div/select[1]/option[2]').click()
		time.sleep(40)
		table = Victor.find_element(by=By.ID, value = "dashboard_quick_stats")
		mtds_val = table.find_element(by=By.CLASS_NAME, value = "row_light_color")
		for mtd_val in mtds_val.find_elements_by_tag_name("td"):
			if mtd_val.text != 'Total -':
				mtd_valArr.append(mtd_val.text)

		Victor.get("https://partners.victorsaffiliates.com/reporting/quick_summary_report.asp")
		toDate = Victor.find_element_by_id('enddate').get_attribute('value')
		toDateObj = datetime.datetime.strptime(toDate, '%Y/%m/%d').date()
		delta = datetime.timedelta(days = 1)
		aDayAgo = toDateObj - delta
		aDayAgoObj = aDayAgo.strftime("%Y/%m/%d")
		reportDiv = Victor.find_element_by_id("reportcriteria")
		merchantDiv = reportDiv.find_elements_by_tag_name("tr")[3]
		merchantId = merchantDiv.find_element_by_tag_name("select")
		merchant = merchantId.find_elements_by_tag_name("option")[0]
		
		Victor.execute_script("document.getElementById('startdate').value = '{0}'".format(aDayAgoObj))
		Victor.execute_script("document.getElementById('enddate').value = '{0}'".format(aDayAgoObj))
		merchant.click()
		time.sleep(5)
		Victor.find_element_by_class_name("button").click()
		time.sleep(20)
		tableDiv = Victor.find_element_by_id("internalreportdata")
		table = tableDiv.find_element_by_tag_name("table")
		todayVal = table.find_elements_by_tag_name("tr")

		pattern = re.compile(r'[\-\d.\d]+')
		impreto = pattern.search(todayVal[1].text).group(0)
		mtd_valArr.append(impreto)
		clito = pattern.search(todayVal[2].text).group(0)
		mtd_valArr.append(clito)
		regto = pattern.search(todayVal[4].text).group(0)
		mtd_valArr.append(regto)
		ndto = pattern.search(todayVal[7].text).group(0)
		mtd_valArr.append(ndto)
		commito = pattern.search(todayVal[-1].text).group(0)
		mtd_valArr.append(commito)
		mtd_valArr.append(aDayAgoObj)
		print(mtd_valArr)
		return mtd_valArr
	finally:
		Victor.quit()
		display.stop()


data = victor_scrapping()

merchant = str(data[0])
impression = int(data[1])
click = int(data[2])
registration = int(data[3])
new_deposit = int(data[4])
commission = float(data[5])
impreytd = int(data[6])
cliytd = int(data[7])
regytd = int(data[8])
ndytd = int(data[9])
commiytd = float((data[10]).replace(",", ""))
impreto = int(data[11])
clito = int(data[12])
regto = int(data[13])
ndto = int(data[14])
commito = float(data[15])
dateto = datetime.datetime.strptime(data[16], '%Y/%m/%d').date()


engine = create_engine('postgresql://postgres:root@localhost/kyan')
result = engine.execute("INSERT INTO victors (merchant, impression, click, registration, new_deposit, commission, impreytd, cliytd, regytd, ndytd, commiytd, impreto, clito, regto, ndto, commito, dateto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", merchant, impression, click, registration, new_deposit, commission, impreytd, cliytd, regytd, ndytd, commiytd, impreto, clito, regto, ndto, commito, dateto)