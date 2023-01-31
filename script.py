import chromedriver_binary # <- これでChromeDriverをPATHに自動追加してくれる
import schedule
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

def job():
    driver = webdriver.Chrome()
    driver.get('https://www.oasisreserve.com/allservice/login/')

    elem_mail = driver.find_element(By.ID,'login_id')
    elem_pass = driver.find_element(By.ID,'password')
    elem_login_btn = driver.find_element(By.CLASS_NAME,'js_submit_form')

    elem_mail.send_keys('mimi99okada405@gmail.com')
    elem_pass.send_keys('1129Mimi99')
    elem_login_btn.click()


    driver.get('https://www.oasisreserve.com/allservice/event/detail?id=1037357&date=2023-02-04&time=15%3A10')

    elem_on_time_reserve_btn = driver.find_element(By.CLASS_NAME,'onTimeReserve')
    elem_on_time_reserve_btn.click()


    elem_position = driver.find_element(By.NAME,'position')
    select = Select(elem_position)
    elem_check_box = driver.find_element(By.ID,'reserve_policy')
    elem_confirm_btn = driver.find_element(By.CLASS_NAME,'js_submit_form')

    select.select_by_visible_text('C5')
    elem_check_box.click()
    elem_confirm_btn.click()

    elem_reserve_btn = driver.find_element(By.CLASS_NAME,'js_submit_form')
    elem_reserve_btn.click()
    
    print("予約完了しました")
    
    time.sleep(30)
    driver.quit()



def main():
    schedule.every().tuesday.at("12:25:00").do(job)
    print("処理を開始します")
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    job()