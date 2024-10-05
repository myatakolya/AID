import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as opt
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By as by
from bs4 import BeautifulSoup
from time import sleep

def parser(page):
    options = opt()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(f"https://www.wildberries.ru/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki?page={page}")

    try:
        wdw(driver, 10).until(
            ec.presence_of_element_located((by.CLASS_NAME, "product-card-overflow"))) # ждём прогруз и проверям наличие дива с классом product-card-overflow иначе возвращаем пустой лист
    except Exception:
        return []
    html_page = driver.page_source
    soup = BeautifulSoup(html_page, "html.parser")
    item = soup.findAll("article", {"class": "product-card"})
    cards = {f"page_{page}" : {}}
    k = 1
    for params in item:
        name = params.find_all(class_="product-card__name")
        brand = params.find_all(class_="product-card__brand")
        id = params["id"]
        price = params.find_all(class_="price__lower-price")
        rate = params.find_all(class_='address-rate-mini')
        cards[f"page_{page}"][f"item{k}"] = {
            "name": name[0].text.replace('  / ','').replace(" "*12, ''),
            "brand": brand[0].text,
            "id": id,
            "price": price[0].text.replace(" ",""),
            "rate": rate[0].text
        }
        k += 1
    driver.close()
    return cards


pages = 3
cards = list()

for i in range(1,pages+1):
    cards.append(parser(i))

with open("./unsorted_data.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

with open("./unsorted_data.json", "r", encoding="utf-8") as f:
    new_cards = {"page_1" : {}}
    data = json.load(f)
    new_item = 1
    for page in range(1,pages+1):
        for item in range(1,31):
            if data[page-1][f'page_{page}'][f"item{item}"]['rate'] == '4.8':
                new_cards["page_1"][f"item{new_item}"] = {
                    "name": data[page-1][f'page_{page}'][f"item{item}"]['name'],
                    "brand": data[page-1][f'page_{page}'][f"item{item}"]['brand'],
                    "id": data[page-1][f'page_{page}'][f"item{item}"]['id'],
                    "price": data[page-1][f'page_{page}'][f"item{item}"]['price'],
                    "rate": data[page-1][f'page_{page}'][f"item{item}"]['rate']
                }
                new_item += 1
    with open("./sorted_data.json", "w", encoding="utf-8") as f2:
        json.dump(new_cards,f2,ensure_ascii=False, indent=2)
    
                
