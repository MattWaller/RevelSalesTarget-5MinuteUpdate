try:

	import time
	import Credentials
	import random
	import os
	import sys
	from Driver import driver

	# Generate New Password
	s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	num = "01234567890"
	spec = "!@#$%^&*()?"
	lower = "abcdefghijklmnopqrstuvwxyz"
	upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	passlen = 10
	p = "".join(random.sample(s,passlen ))
	np = "".join(random.sample(num, 1 ))
	ns = "".join(random.sample(spec,1 ))
	nl = "".join(random.sample(lower, 1 ))
	nu = "".join(random.sample(upper, 1 ))

	ap = np + p + ns + nl + nu

	print(ap)

	username = Credentials.login['consumer_username']
	password = Credentials.login['consumer_secret']

	currenturl = # define revelup company id.

	
		

	driver.get(currenturl)

	time.sleep(3)

	driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(username)
	time.sleep(1)

	driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(password)
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="form-login"]/fieldset/div[3]/input').click()

	time.sleep(1)


	driver.find_element_by_xpath('//*[@id="change_own_password"]').click()
	time.sleep(1)
	
	# define pop up blockers
	
	blockers = driver.find_elements_by_xpath('//*[@aria-label="close"]')
	blockers_len = len(blockers)

	i = 0
	# loop through blockers on page & close active popup
	if i < blockers_len:
		while i < blockers_len:
			if(blockers[i].is_displayed() == True):
				blockers[i].click()
			i = i + 1

	driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(password)
	time.sleep(1)



	driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys(ap)
	time.sleep(1)

	driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys(ap)
	time.sleep(1)

	# Text contains Update & is same button coding as Cancel Button
	driver.find_element_by_xpath('//*[@class="ui-button-text"][contains(text(),"Update")]').click()

	time.sleep(2)

	driver.quit()

	# Record New password in txt file
	NewPW = open(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\MyScripts\password.txt", 'w+')

	NewPW.write(ap)
	NewPW.close()


	PW = open(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\MyScripts\password.txt",'r')
	PassW = PW.readlines()
	print(PassW)
	PW.close()

except Exception as e:
	import sys
	import datetime
	from Error_email import Error_email
	scriptname = sys.argv[0]
	timestamp = datetime.datetime.now()
	errorMsg = repr(e)
	Error_email(scriptname,timestamp,errorMsg)
