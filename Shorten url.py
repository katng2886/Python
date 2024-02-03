import pyshorteners
while True:
    cont = input('Do you want to start (Y/N): ')
    if cont == 'Y' or cont == 'y':
        long_url = input('Enter URL: ') #input the url
        short_url = pyshorteners.Shortener() #Shortener
        tiny_url = short_url.tinyurl.short(long_url)
        print('The shortened URL is: ', tiny_url)
    elif cont == 'N' or cont == 'n':
        print('Bye now')
        exit()

