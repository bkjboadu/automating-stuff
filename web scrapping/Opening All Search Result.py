import requests,bs4,webbrowser,pyperclip,sys
if len(sys.argv) > 1:
    on_search = ' '.join(sys.argv[1:])
else:
    on_search = pyperclip.paste()

res = requests.get('https://pypi.org/search/?q=' + str(on_search))
print(res.raise_for_status())
Soup = bs4.BeautifulSoup(res.text,'html.parser')
Selected = Soup.select('.package-snippet')
print(Selected)
numOpen = min(5,len(Selected))
for i in range(numOpen):
    url = 'https://pypi.org/search/?q=' + Selected[i].get('href')
    webbrowser.open(url)

