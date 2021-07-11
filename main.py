import requests
import json
import lxml.html

def save_cookies(sess_cookies, file_name):
    cookie_list = [
        {'domain': c.domain, 'name': c.name, 'path': c.path, 'value': c.value}
        for c in sess_cookies
    ]
    with codecs.open(f"{file_name}_cookies", mode='wb', encoding='utf-8') as f:
        json.dump(cookie_list, f, indent=4)
        f.close()
    print('---куки выгружены успешно---')

def cookie_export_vk(auth_log, auth_pass, cookie_file_name):
    session = requests.Session()
    url = "https://vk.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }
    data = session.get(url, headers=headers)
    web_page = lxml.html.fromstring(data.content)
    form = web_page.forms[0]
    form.fields['email'] = auth_log
    form.fields['pass'] = auth_pass
    response = session.post(form.action, data=form.form_values())
    if not ('onLoginDone' in response.text):
        print('Ошибка входа', 'Неверный логин или пароль!')
    else:
        save_cookies(sess_cookies=session.cookies, file_name=cookie_file_name)

cookie_export_vk('-','-','vk')