from selenium import webdriver

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from datetime import datetime
from pytz import timezone



format = " %H:%M:%S "


while(True):
    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    print(now_utc.strftime(format))
    # Convert to Asia/Kolkata time zone
    now_asia = now_utc.astimezone(timezone('Asia/Manila'))

    print(now_asia.strftime(format))


    print(now_asia)
    today7am = now_asia.replace(hour=7, minute=0, second=0, microsecond=0)
    today8am = now_asia.replace(hour=7, minute=59, second=59, microsecond=0)
    print(today8am)
    if (now_asia > today8am or now_asia < today7am):


      username = "trytryfuck"
      password = "qweqwe"
      amountentering = 100
      submitbuttton = "/html/body/div/div[2]/div/div/div[2]/div/div[2]/form/div[3]"
      bitstatus = '/html/body/div/div/div[2]/div[2]/div[1]/div[2]/div/table/tbody/tr/td[1]/span'
      meron_payout_xpath = '/html/body/div/div/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[1]/h5'
      wala_payout_xpath = '/html/body/div/div/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/h5'
      meron_bitbutton_xpath = '//*[@id="app"]/div[1]/div[3]/div/div[3]/div[1]/button'
      Wala_bitbutton_xpath = '//*[@id="app"]/div[1]/div[3]/div/div[3]/div[2]/button'
      enteramount_xpath = '//*[@id="app"]/div[1]/div[3]/div/div[4]/div[2]/div/div/input'

      yes_bit = '/html/body/div[2]/div/div[3]/button[1]'
      yes_bit_classname = 'swal2-confirm swal2-styled'

      driver = webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")

      url = 'https://www.Wpc2029.live/'
      driver.get(url)
      my_element_user = driver.find_element_by_id('username').send_keys(username)
      my_element_pass = driver.find_element_by_id('password').send_keys(password)
      my_element = driver.find_element_by_xpath(submitbuttton)

      my_element.click()
      meron_bit = driver.find_element_by_xpath(meron_bitbutton_xpath)
      wala_bit = driver.find_element_by_xpath(Wala_bitbutton_xpath)
      # a=len(driver.find_element_by_xpath(meron_payout_xpath))
      my_element_bit_status = driver.find_element_by_xpath(bitstatus)

      my_element_sendamount = driver.find_element_by_xpath(enteramount_xpath).send_keys(amountentering)

      if (WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.XPATH, bitstatus), 'OPEN'))):
        print("enter if")

        time.sleep(10)
        ab = driver.find_element_by_xpath(meron_payout_xpath).text
        bc = driver.find_element_by_xpath(wala_payout_xpath).text
        print(ab)
        print(bc)
        meronpay = ''.join(x for x in ab if x.isdigit())
        print(meronpay)
        meronpay = int(meronpay)
        meronpay_string = str(meronpay)
        s1 = len(meronpay_string)
        print(s1)
        if (s1 == 4):
            anans = int(str(meronpay)[:-1])
            print(anans)
        else:
            MP = meronpay // 10
            meronpay = MP // 10
            print(meronpay)

        walapay = ''.join(x for x in bc if x.isdigit())
        print(walapay)
        walapay = int(walapay)
        walapay_string = str(walapay)
        s2 = len(walapay_string)
        print(s2)
        if (s2 == 4):
            anans = int(str(walapay)[:-1])
            print(anans)
        else:
           WP = walapay // 10
           walapay = WP // 10
           print(walapay)

        if (meronpay > 200):
            print("enter meropay")
            meron_bit.click()
            anasbit = driver.find_element_by_xpath(yes_bit)
            anasbit.click()
        # my_element_yesbitdraw = driver.find_element_by_xpath(yes_bit_xpath)
        # my_element_yesbitdraw.click()

        if (walapay > 200):
            print("enter walapay")
            wala_bit.click()
            anasbit = driver.find_element_by_xpath(yes_bit)
            anasbit.click()
        # my_element_yesbitdraw = driver.find_element_by_xpath(yes_bit_xpath)
        # my_element_yesbitdraw.click()

        # title=driver.title
        #
        # print(title)
        #
        # # driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        # #
        # # url='https://www.Wpc2029.live/'
        # # driver.get(url)
        # #
        # # ab='PAYOUT + 612.6'
        #
        # from datetime import datetime
        # from pytz import timezone
        # format = "%Y-%m-%d %H:%M:%S %Z%z"
        # # Current time in UTC
        # now_utc = datetime.now(timezone('UTC'))
        # print(now_utc.strftime(format))
        # # Convert to Asia/Kolkata time zone
        # now_asia = now_utc.astimezone(timezone('Asia/Manila'))
        # print(now_asia.strftime(format))


    else:
        print("you are not in time zone")


#
# Current time in UTC
#
# now_utc = datetime.now(timezone('UTC'))
#
#  # Convert to Asia/Kolkata time zone
# now_asia = now_utc.astimezone(timezone('Asia/Manila'))
#
# print(now_asia.strftime(format))
# print(type(now_asia))
# ab=now_asia.strftime(format)
#
# ab=timezone()
# print(ab)
#
#
#
#
