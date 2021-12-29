import csv
import telebot
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

bot = telebot.TeleBot('5065626928:AAE8UvP78pmudoVhgHKNbaR0gy3VT7EwOfE')

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://ru.investing.com/crypto/")
    # Coin#1
    Coin1Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(1) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin1Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(1) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin1Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(1) > td.price.js-currency-price > a')
    Coin1MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(1) > td.js-market-cap')
    Coin1Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(1) > td.js-24h-volume')
    Coin1Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(1) > td.js-total-vol')
    Coin1Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[1]/td[8]')
    Coin1Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[1]/td[9]')
    # Coin#2
    Coin2Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(2) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin2Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(2) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin2Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(2) > td.price.js-currency-price > a')
    Coin2MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(2) > td.js-market-cap')
    Coin2Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(2) > td.js-24h-volume')
    Coin2Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(2) > td.js-total-vol')
    Coin2Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[2]/td[8]')
    Coin2Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[2]/td[9]')
    # Coin#3
    Coin3Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(3) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin3Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(3) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin3Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(3) > td.price.js-currency-price > a')
    Coin3MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(3) > td.js-market-cap')
    Coin3Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(3) > td.js-24h-volume')
    Coin3Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(3) > td.js-total-vol')
    Coin3Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[3]/td[8]')
    Coin3Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[3]/td[9]')
    # Coin#4
    Coin4Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(4) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin4Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(4) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin4Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(4) > td.price.js-currency-price > a')
    Coin4MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(4) > td.js-market-cap')
    Coin4Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(4) > td.js-24h-volume')
    Coin4Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(4) > td.js-total-vol')
    Coin4Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[4]/td[8]')
    Coin4Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[4]/td[9]')
    # Coin#5
    Coin5Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(5) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin5Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(5) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin5Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(5) > td.price.js-currency-price > a')
    Coin5MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(5) > td.js-market-cap')
    Coin5Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(5) > td.js-24h-volume')
    Coin5Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(5) > td.js-total-vol')
    Coin5Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[5]/td[8]')
    Coin5Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[5]/td[9]')
    # Coin#6
    Coin6Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(6) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin6Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(6) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin6Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(6) > td.price.js-currency-price > a')
    Coin6MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(6) > td.js-market-cap')
    Coin6Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(6) > td.js-24h-volume')
    Coin6Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(6) > td.js-total-vol')
    Coin6Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[6]/td[8]')
    Coin6Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[6]/td[9]')
    # Coin#7
    Coin7Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(7) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin7Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(7) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin7Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(7) > td.price.js-currency-price > a')
    Coin7MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(7) > td.js-market-cap')
    Coin7Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(7) > td.js-24h-volume')
    Coin7Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(7) > td.js-total-vol')
    Coin7Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[7]/td[8]')
    Coin7Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[7]/td[9]')
    # Coin#8
    Coin8Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(8) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin8Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(8) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin8Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(8) > td.price.js-currency-price > a')
    Coin8MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(8) > td.js-market-cap')
    Coin8Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(8) > td.js-24h-volume')
    Coin8Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(8) > td.js-total-vol')
    Coin8Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[8]/td[8]')
    Coin8Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[8]/td[9]')
    # Coin#9
    Coin9Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(9) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin9Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(9) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin9Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(9) > td.price.js-currency-price > a')
    Coin9MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(9) > td.js-market-cap')
    Coin9Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(9) > td.js-24h-volume')
    Coin9Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(9) > td.js-total-vol')
    Coin9Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[9]/td[8]')
    Coin9Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[9]/td[9]')
    # Coin#10
    Coin10Name = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(10) > td.left.bold.elp.name.cryptoName.first.js-currency-name > a')
    Coin10Ticker = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(10) > td.left.noWrap.elp.symb.js-currency-symbol')
    Coin10Prise = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(10) > td.price.js-currency-price > a')
    Coin10MarketCap = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(10) > td.js-market-cap')
    Coin10Volume24h = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(10) > td.js-24h-volume')
    Coin10Volume = driver.find_element_by_css_selector('#fullColumn > div:nth-child(9) > table > tbody > tr:nth-child(10) > td.js-total-vol')
    Coin10Changes24h = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[10]/td[8]')
    Coin10Changes7d = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/table/tbody/tr[10]/td[9]')

    global allCoin
    allCoin = [Coin1Prise.text, Coin2Prise.text, Coin3Prise.text, Coin4Prise.text, Coin5Prise.text, Coin6Prise.text, Coin7Prise.text, Coin8Prise.text, Coin9Prise.text, Coin10Prise.text]



while allCoin:
    if allCoin != 0:
        bot.send_message(chat_id='1653692753', text=f'123123asdasd')
    elif allCoin == 0:
        break
            
            
# with open('info.csv', 'w', newline='') as csvfile:
#     fileWriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     fileWriter.writerow(['Name', 'Ticker', 'Prise', 'MarketCap', 'Volume', 'Volume(24h)', 'Changes(24)', 'Changes(7d)'])
#     fileWriter.writerow([Coin1Name.text, Coin1Ticker.text, Coin1Prise.text, Coin1MarketCap.text, Coin1Volume24h.text, Coin1Volume.text, Coin1Changes24h.text, Coin1Changes7d.text])
#     fileWriter.writerow([Coin2Name.text, Coin2Ticker.text, Coin2Prise.text, Coin2MarketCap.text, Coin2Volume24h.text, Coin2Volume.text, Coin2Changes24h.text, Coin2Changes7d.text])
#     fileWriter.writerow([Coin3Name.text, Coin3Ticker.text, Coin3Prise.text, Coin3MarketCap.text, Coin3Volume24h.text, Coin3Volume.text, Coin3Changes24h.text, Coin3Changes7d.text])
#     fileWriter.writerow([Coin4Name.text, Coin4Ticker.text, Coin4Prise.text, Coin4MarketCap.text, Coin4Volume24h.text, Coin4Volume.text, Coin4Changes24h.text, Coin4Changes7d.text])
#     fileWriter.writerow([Coin5Name.text, Coin5Ticker.text, Coin5Prise.text, Coin5MarketCap.text, Coin5Volume24h.text, Coin5Volume.text, Coin5Changes24h.text, Coin5Changes7d.text])
#     fileWriter.writerow([Coin6Name.text, Coin6Ticker.text, Coin6Prise.text, Coin6MarketCap.text, Coin6Volume24h.text, Coin6Volume.text, Coin6Changes24h.text, Coin6Changes7d.text])
#     fileWriter.writerow([Coin7Name.text, Coin7Ticker.text, Coin7Prise.text, Coin7MarketCap.text, Coin7Volume24h.text, Coin7Volume.text, Coin7Changes24h.text, Coin7Changes7d.text])
#     fileWriter.writerow([Coin8Name.text, Coin8Ticker.text, Coin8Prise.text, Coin8MarketCap.text, Coin8Volume24h.text, Coin8Volume.text, Coin8Changes24h.text, Coin8Changes7d.text])
#     fileWriter.writerow([Coin9Name.text, Coin9Ticker.text, Coin9Prise.text, Coin9MarketCap.text, Coin9Volume24h.text, Coin9Volume.text, Coin9Changes24h.text, Coin9Changes7d.text])
#     fileWriter.writerow([Coin10Name.text, Coin10Ticker.text, Coin10Prise.text, Coin10MarketCap.text, Coin10Volume24h.text, Coin10Volume.text, Coin10Changes24h.text, Coin10Changes7d.text])

if __name__ == '__main__':
    main()
