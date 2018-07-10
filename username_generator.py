import requests
import string
import random


def get_names():
    url = 'https://uinames.com/api/'
    response = requests.get(url).json()

    # Since names from these regions have special characters they are skipped to avoid errors
    skip_list = ['Iran', 'China', 'Russia', 'Armenia', 'Azerbaijan', 'Bulgaria', 'Egypt', 'Georgia', 'Greece', 'Israel', 'Japan', 'Korea', 'Saudi Arabia', 'Ukraine', 'Vietnam']

    if response['region'] in skip_list:
        name, surname = get_names()
        return name, surname

    name = response['name']
    surname = response['surname']

    return name, surname


def create_username():

    first_name, last_name = get_names()

    return number_last(first_name, last_name), number_mid(first_name, last_name)


def number_last(first_name, last_name):

    username = ''
    n = random.choice(range(1, 4))
    username += first_name[0]
    username += last_name
    username += ''.join(random.choice(string.digits) for _ in range(n))

    return username


def number_mid(first_name, last_name):

    username = ''
    n = random.choice(range(1, 4))
    username += first_name
    username += ''.join(random.choice(string.digits) for _ in range(n))
    username += last_name

    return username


print(create_username())
