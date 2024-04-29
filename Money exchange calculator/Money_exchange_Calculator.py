import json
from urllib.request import urlopen

with urlopen("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json") as response: #EUR as base
    source = response.read()
    data = json.loads(source)
    countries = data["eur"]
with urlopen("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json") as extra:
    extra_source = extra.read()
    extra_data = json.loads(extra_source)
    name = dict(extra_data)

def get_countries_code():
    while True:
        cont = input('Start, input Y for start, N for stop, Y/N: ')
        if cont == 'Y' or cont == 'y':
            country_code = input('Enter the country code:')
            rate = float(input('Enter the amount you want to convert:'))
            if country_code not in countries:
                print(country_code, 'not found')

            for key, value in countries.items():
                if country_code == key:
                    converted_rate = rate * value
                    print('Country code abbreviation: ', key)
                    print('This is the rate: ', value)
                    for k, v in name.items():
                        if country_code == k:
                            print('The country code is :', v)
                            print('A', rate, 'is worth', converted_rate, 'in', v)
                    break
        elif cont == 'N' or cont == 'n':
            print('Thank you. See you soon!')
            exit()




def main():
    get_countries_code()

if __name__ == '__main__':
    main()
