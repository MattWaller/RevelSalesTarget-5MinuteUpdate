try:
	import time
	from datetime import datetime, timedelta
	import Credentials
	from Datetime import tom, tomMon, tomYear
	now = datetime.now()
	timezz = str(now.hour) + "." + str(now.minute)
	timef = float(timezz)


	print(timef)

	year = str(now.year)
	month = str(now.month)
	today = str(now.day)

	#if day / month less than 10
	if (int(today)<10):
		today = str('0'+ today)
	if(int(tom)<10):
		tom = str('0'+ str(tom))
	if (int(month)<10):
		month = str('0'+ month)
	if (int(tomMon)<10):
		tomMon = str('0'+ str(tomMon))


	print("print before if")

	if timef > 9.44:
		if timef < 23.31:

			timeV = "+03%3A00%3A00"
			to = '&range_to='
			us = '%2f'

			#defining link
			download = 'https://therangelangley.revelup.com/reports/operations/data.csv?employee=&online_app=&online_app_type=&online_app_platform=&show_unpaid=1&show_irregular=1&range_from='+ str(month) + str(us) + str(today) + str(us) + str(year) +  str(timeV) + str(to) + str(tomMon) + str(us) + str(tom) + str(us) + str(tomYear) + str(timeV)
			

			username = Credentials.login['consumer_username']
			password = Credentials.login['consumer_secret']


			
			from Driver import driver
			driver.get(download)  


			# go to download file link

			time.sleep(3)

			# verify that login page is live.
			forgot = driver.find_element_by_xpath('//*[contains(text(),"Forgot")]').text
			try:
				if forgot == 'Forgot your password?':

					driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(username)
					time.sleep(1)

					driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(password)
					time.sleep(1)
					driver.find_element_by_xpath('//*[@id="form-login"]/fieldset/div[3]/input').click()

					theURL = str(driver.current_url)
					PW_reset = "reset" in theURL
					#PW_reset = driver.find_element_by_xpath('//*[contains(text(),"Password Expired")]').is_displayed()
					
					print(PW_reset)
					# reset password when expired --> PW_reset
					try:
						if (PW_reset == True):
							driver.find_element_by_xpath('//*[contains(text(),"Password Expired")]').click()


							import random
							import os
							import sys

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




							# enter and save new password

							driver.find_element_by_xpath('//*[@placeholder="Enter your new password"]').send_keys(ap)
							time.sleep(1)

							driver.find_element_by_xpath('//*[@placeholder="Retype password"]').send_keys(ap)
							time.sleep(1)


							driver.find_element_by_xpath('//*[@value="Reset"]').click()
							time.sleep(1)

							# re-load download page
							driver.get(download)  

							driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(ap)
							time.sleep(1)

							driver.find_element_by_xpath('//*[@id="id_password"]').send_keys(ap)
							time.sleep(1)
							driver.find_element_by_xpath('//*[@id="form-login"]/fieldset/div[3]/input').click()

							# Record New password in txt file
							NewPW = open(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\MyScripts\password.txt", 'w+')

							NewPW.write(ap)
							NewPW.close()


							PW = open(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32\MyScripts\password.txt",'r')
							PassW = PW.readlines()
							print(PassW)
							PW.close()


						
					except Exception as e:
						raise e

					




					time.sleep(10)
					print("file Grabbed!")
					driver.quit()
					print("driver quit")



			except Exception as e:
				raise e 
			print("relocating file")
			import xlrd
			import csv
			import shutil
			import os.path
			from datetime import datetime, timedelta
			import glob
			
			now = datetime.now()
			timezz = str(now.hour) + "." + str(now.minute)
			timef = float(timezz)


			SuffixOne = datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d')
			SuffixTwo = datetime.strftime(datetime.now(), '%Y-%m-%d_')

			

			
			exists = os.path.isfile(r'G:\My Drive\RevelSalesTarget\RawData\SalesOperationsReport.csv')
			Nexists = os.path.isfile(r'C:\\Users\\Administrator\\Downloads\\'+'Operations_Report_the-range-langley_the-range-langley_' + SuffixTwo + SuffixOne +'.csv')
			FileName = 'C:\\Users\\Administrator\\Downloads\\'+'Operations_Report_the-range-langley_the-range-langley_' + SuffixTwo + SuffixOne +'.csv'

			try:
				if  Nexists:
				 	if exists:
					 	os.remove(r"G:\My Drive\RevelSalesTarget\RawData\SalesOperationsReport.csv")
					 	print("exists file removed")
						

				if Nexists:
					shutil.move(FileName, r"G:\My Drive\RevelSalesTarget\RawData\SalesOperationsReport.csv")
					print("Nexists file moved")

			except Exception as e:
				raise e
			SuffixOne = datetime.strftime(datetime.now() + timedelta(1), '%Y-%m-%d')
			SuffixTwo = datetime.strftime(datetime.now(), '%Y-%m-%d_')

			#remove any active csv file --> ensures that if an error happens it'll delete any csv file in the dir
			arr = glob.glob('C:\\Users\\Administrator\\Downloads\\*.csv')
			i = 0

			while i < len(arr):
				try:
					os.remove(arr[i])
					i = i + 1
				except Exception as e:
					i = i + 1
					

			exit()
	exit()

except Exception as e:
	import sys
	import datetime
	from Error_email import Error_email
	scriptname = sys.argv[0]
	timestamp = datetime.datetime.now()
	errorMsg = repr(e)
	Error_email(scriptname,timestamp,errorMsg)
