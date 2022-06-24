# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
   pass


def func_and_arg(*args):
    function_number = 1
    for func in args:
        func_and = func.__name__
        func_and = func_and.replace("_", " ")

        arguments_and = func.__code__.co_varnames
        # не придумал как отредактировать внутри агрумента(

        print("Function name ===> " + func_and +  '\nArgument ===> ', arguments_and)
        function_number += 1

func_and_arg(open_browser,go_to_companyname_homepage, find_registration_button_on_login_page())


