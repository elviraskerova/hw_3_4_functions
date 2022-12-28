def replace_name_function(name_func, *args):
    full_name = name_func.__name__.title().replace('_', '')


def open_browser(browser_name):
    replace_name_function(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    replace_name_function(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    replace_name_function(find_registration_button_on_login_page, page_url, button_text)


open_browser('Opera')
go_to_companyname_homepage('https://qa.quru/')
find_registration_button_on_login_page('login', 'https://qa.quru/')

