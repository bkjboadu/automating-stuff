import webbrowser,requests,pyperclip,sys,bs4

if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
else:
    search = pyperclip.paste()

locate = 'https://pypi.org/search/?q=' + str(search)
res = requests.get(locate)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
lookup = soup.select('.package-snippet')

for i in range(len(lookup)):
    print(lookup[i])
    try:
        webbrowser.open('https://pypi.org' + lookup[i].get('href'))
    except:
        pass
