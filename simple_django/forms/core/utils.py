import requests
from lxml import html
from core.models import Currency


def notify(text):
    print(f"Notify {text.first_name.capitalize()} {text.last_name.capitalize()}")


currency_names = ['USD', 'EUR', 'RUR']


def get_mono_bank_currency():
    title = 'monobank'
    UAH = 980
    USD = 840
    EUR = 978
    RUR = 643
    code_lst = [USD, EUR, RUR]
    currency_data = []

    response = requests.get('https://api.monobank.ua/bank/currency')
    if response.status_code == 200:
        data = response.json()

        for code in code_lst:
            course = [d for d in data if d["currencyCodeB"] == UAH and d["currencyCodeA"] == code]
            currency_data.append(course)

        currency_lst = []
        i = 0
        for currency in currency_data:
            currency_lst.append(Currency(
                ccy=Currency.convert_str_to_choice(currency_names[i]),
                buy_price=currency[0]['rateBuy'],
                sell_price=currency[0]['rateSell'],
                title=title,
            ))
            i += 1
        Currency.objects.bulk_create(currency_lst)
    else:
        print(response.status_code)


def get_industrial_bank_currency():
    title = 'industrial_bank'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get('https://industrialbank.ua/ua/', headers=headers)

    if response.status_code == 200:
        tree = html.fromstring(response.text)

        currency_map = [{
            'ccy': 'USD',
            'buy': '//*[@id="exchange-rate"]/div[1]/ul/li[1]/span[2]',
            'sale': '//*[@id="exchange-rate"]/div[2]/ul/li[1]/span[2]',
        }, {
            'ccy': 'EUR',
            'buy': '//*[@id="exchange-rate"]/div[1]/ul/li[2]/span[2]',
            'sale': '//*[@id="exchange-rate"]/div[2]/ul/li[2]/span[2]',
        }, {
            'ccy': 'RUR',
            'buy': '//*[@id="exchange-rate"]/div[1]/ul/li[3]/span[2]',
            'sale': '//*[@id="exchange-rate"]/div[2]/ul/li[3]/span[2]',
        }]

        currency_lst = []

        for row in currency_map:
            ccy = Currency.convert_str_to_choice(row['ccy'])
            if ccy:
                currency_lst.append(Currency(
                    ccy=ccy,
                    buy_price=tree.xpath(row['buy'])[0].text,
                    sell_price=tree.xpath(row['sale'])[0].text,
                    title=title,
                ))

        Currency.objects.bulk_create(currency_lst)
    else:
        print(response.status_code)


def get_vkurse_currency():
    title = 'vkurse'
    response = requests.get('http://vkurse.dp.ua/course.json')

    if response.status_code == 200:
        resp = response.json()
        dollar = resp['Dollar']
        euro = resp['Euro']
        rub = resp['Rub']
        currency_data = [dollar, euro, rub]

        currency_lst = []
        i = 0
        for row in currency_data:
            currency_lst.append(Currency(
                ccy=Currency.convert_str_to_choice(currency_names[i]),
                buy_price=row['buy'],
                sell_price=row['sale'],
                title=title
            ))
            i += 1
        Currency.objects.bulk_create(currency_lst)

    else:
        print(response.status_code)


def get_kurs_currency():
    title = 'kurs'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get('https://kurs.com.ua/', headers=headers)

    if response.status_code == 200:
        tree = html.fromstring(response.text)

        currency_map = [{
            'ccy': 'USD',
            'buy': '//*[@id="main_table"]/tbody/tr[1]/td[2]/div/text()',
            'sale': '//*[@id="main_table"]/tbody/tr[1]/td[3]/div/text()',
        }, {
            'ccy': 'EUR',
            'buy': '//*[@id="main_table"]/tbody/tr[2]/td[2]/div/text()',
            'sale': '//*[@id="main_table"]/tbody/tr[2]/td[3]/div/text()',
        }, {
            'ccy': 'RUR',
            'buy': '//*[@id="main_table"]/tbody/tr[3]/td[2]/div/text()',
            'sale': '//*[@id="main_table"]/tbody/tr[3]/td[3]/div/text()',
        }]

        currency_lst = []

        for row in currency_map:
            ccy = Currency.convert_str_to_choice(row['ccy'])
            if ccy:
                currency_lst.append(Currency(
                    ccy=ccy,
                    buy_price=tree.xpath(row['buy'])[0],
                    sell_price=tree.xpath(row['sale'])[0],
                    title=title,
                ))

        Currency.objects.bulk_create(currency_lst)

    else:
        print(response.status_code)


def get_minfin_currency():
    title = 'minfin'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get('https://minfin.com.ua/ua/currency/', headers=headers)

    if response.status_code == 200:
        tree = html.fromstring(response.text)
        currency_map = [{
            'ccy': 'USD',
            'buy': '/html/body/main/div[2]/div/div[1]/div/section[2]/div/table[1]/tbody/tr[1]/td[4]/text()[1]',
            'sale': '/html/body/main/div[2]/div/div[1]/div/section[2]/div/table[1]/tbody/tr[1]/td[4]/text()[2]',
        }, {
            'ccy': 'EUR',
            'buy': '/html/body/main/div[2]/div/div[1]/div/section[2]/div/table[1]/tbody/tr[2]/td[4]/text()[1]',
            'sale': '/html/body/main/div[2]/div/div[1]/div/section[2]/div/table[1]/tbody/tr[2]/td[4]/text()[2]',
        }, {
            'ccy': 'RUR',
            'buy': '/html/body/main/div[2]/div/div[1]/div/section[2]/div/table[1]/tbody/tr[3]/td[4]/text()[1]',
            'sale': '/html/body/main/div[2]/div/div[1]/div/section[2]/div/table[1]/tbody/tr[3]/td[4]/text()[2]',
        }]

        currency_lst = []
        for row in currency_map:
            ccy = Currency.convert_str_to_choice(row['ccy'])
            if ccy:
                currency_lst.append(Currency(
                    ccy=ccy,
                    buy_price=tree.xpath(row['buy'])[0].replace(',', '.'),
                    sell_price=tree.xpath(row['sale'])[0].replace(',', '.'),
                    title=title,
                ))

        Currency.objects.bulk_create(currency_lst)
    else:
        print(response.status_code)
