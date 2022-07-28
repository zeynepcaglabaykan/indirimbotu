from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import smtplib
import hesap

#MAİL HESABINI AÇMA

mail = smtplib.SMTP_SSL("smtp.gmail.com",465)
mail.login(hesap.email,hesap.password)
mail.quit()
print("çalıştı")


#ÜRÜN BİLGİLERİNİ ALMA

product_link = input("İndirim beklediğiniz ürün linki: ")
price = float(input("Kaç TL'nin altına düşmesini bekliyorsunuz? "))
email = input("Gönderilecek mail adresi: ")

#DRİVER İLE YAPILACAK İŞLEMLER

chrome_options = webdriver.ChromeOptions()
c = webdriver.ChromeOptions()
c.add_argument("--incognito")
c.add_argument("--headless")
ser = Service(r'C:\Users\zeyne\Desktop\Files\TrendyolBot\chromedriver.exe')

print("servise bağlandı")

driver = webdriver.Chrome(service=ser,options=c)
driver.maximize_window()
driver.delete_all_cookies()
action = ActionChains(driver)

print("driver açıldı")

def slide():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

while True:
    driver.get(product_link)
    print("driver çalıştı")
    time.sleep(3)
    slide()
    time.sleep(1)
    product_name = driver.find_element_by_class_name("pr-new-br").text
    #urun_ismi = driver.find_element(by=CLASS_NAME,value="pr-new-br").text
    current_price = driver.find_element_by_class_name("prc-dsc").text
    current_price = current_price.replace(",",".")
    current_price = current_price.split(" ")

    if float(current_price[0]) <= price:
        mail.sendmail(hesap.email,email,f"{urun_ismi} isimli ürün beklediğiniz fiyatın altına inmiştir.")

    else:
        print("Ürün hala istediğiniz fiyatta değil.")
        pass
    driver.close()
    time.sleep(180)