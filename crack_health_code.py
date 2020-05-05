from selenium import webdriver
import datetime


driver1 = webdriver.Chrome()
loginUrl = 'https://www.wjx.cn/jq/57714657.aspx' #address
driver1.get(loginUrl)
driver1.find_element_by_name('q1').send_keys('name')
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/ul/li[2]/a').click()
driver1.find_element_by_name('q3').send_keys('1111111')
driver1.find_element_by_name('q4').send_keys('2020')

# get system time and add one to day
theTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
# remove restriction on write
js = 'document.getElementById("q5").removeAttribute("readonly");'
# execute js to remove restriction on write
driver1.execute_script(js)
# write the time on the bar
driver1.find_element_by_name('q5').send_keys(theTime)

driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[6]/div[2]/ul/li[1]/a').click()
driver1.find_element_by_name('q7').send_keys('xue hao')
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[8]/div[2]/ul/li[3]/a').click()
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[9]/div[2]/ul/li[6]/a').click()
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[10]/div[2]/ul/li[1]/a').click()
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[11]/div[3]/ul/li[3]/a').click()
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[18]/div[2]/ul/li[2]/a').click()
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[19]/div[2]/ul/li[2]/a').click()
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[20]/div[3]/ul/li[2]/a').click()
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[23]/div[3]/ul/li[2]/a').click()
driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[25]/div[2]/ul/li[2]/a').click()
# submit the result
#driver1.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[4]/table/tbody/tr/td[1]/input').click()
