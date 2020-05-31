def changeLang(message,src_lang,dest_lang):
	from selenium import webdriver
	import warnings
	import time
	from selenium.webdriver.support.ui import WebDriverWait


	warnings.filterwarnings("ignore")
	base_url = 'https://translate.google.com/#'				#URL of the target website
	final_url = base_url + src_lang + '/' + dest_lang     
	driver = webdriver.PhantomJS(r'phantomjs.exe')			#driver must be in the same folder as the code
	driver.set_page_load_timeout(30)        				#Increase the timeout value more if timeout exception occurs
	driver.get(final_url)                   
	element="//textarea[@id='source']"
	input_element=WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(element))  	#Finds the element where input text is entered
	input_element.send_keys(message.lower())  
	time.sleep(1)																							#Buffer time
	output_element = "//div[@class='result-shield-container tlid-copy-target']"								
	result = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath(output_element))	#Finds the element where translated text is obtained
	time.sleep(1)   																						#Buffer time
	return result.text


#Parameters:(Text to be translated, source Language, destination Language)
result=changeLang("I am here","en","ta")	
print(result)	


