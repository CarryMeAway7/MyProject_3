import requests
import json

def save_cookies(sess_cookies, file_name):
    cookie_list = [
        {'domain': c.domain, 'name': c.name, 'path': c.path, 'value': c.value}
        for c in sess_cookies
    ]
    with codecs.open(f"{file_name}_cookies", mode='wb', encoding='utf-8') as f:
        json.dump(cookie_list, f, indent=4)
        f.close()
    print('---куки выгружены успешно---')

def cookie_export_dstu(auth_log, auth_pass, cookie_file_name):
    session = requests.Session()
    link = "https://edu.donstu.ru/api/tokenauth"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    data = {
        'userName': auth_log,
        'password': auth_pass
    }
    response = session.post(link, json=data, headers=headers)
    json_data = json.loads(response.text)
    if not ('accessToken' in json_data["data"]):  # Check if auth info is correct
        print("Ошибка входа", "Неверный логин или пароль!")
    else:
        session.get('https://edu.donstu.ru/', headers=headers)
        session.cookies.set("authToken", json_data["data"]["accessToken"], domain="edu.donstu.ru")
        save_cookies(sess_cookies=session.cookies, file_name=cookie_file_name)

cookie_export_dstu('-','-','dstu')