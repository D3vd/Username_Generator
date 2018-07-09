import requests


def get_names():
    url = 'https://uinames.com/api/'
    response = requests.get(url).json()

    # Since names from these regions have special characters they are skipped to avoid errors
    skip_list = ['Iran', 'China', 'Russia', 'Armenia', 'Azerbaijan', 'Bulgaria', 'Egypt', 'Georgia', 'Greece', 'Israel', 'Japan', 'Korea', 'Saudi Arabia', 'Ukraine', 'Vietnam']

    if response['region'] in skip_list:
        print('Skipped {}'.format(response['region']))
        name, surname = get_names()
        return name, surname

    name = response['name']
    surname = response['surname']

    return name, surname


n, s = get_names()
print('{} {}'.format(n, s))
