from selenium import webdriver
import pyperclip,sys,bs4,requests,os
if len(sys.argv) > 1:
    keyword = ' '.join(sys.argv[1:])
else:
    keyword = pyperclip.paste()

os.makedirs('imgur',exist_ok=True)
on_search=requests.get('https://imgur.com/search?q=' + keyword)
on_search_soup = bs4.BeautifulSoup(on_search.text,'html.parser')
searchlist = on_search_soup.select('.post > .image-list-link img')
try:
    numOpen = len(searchlist)
    for i in range(numOpen):
        url = 'https:' + searchlist[i].get('src')
        download = requests.get(url)
        filename = os.path.join('imgur',url.basename())
        save = open(filename,'wb')
        for chunks in download.iter_content(1000000):
            save.write(chunks)
        save.close()
except numOpen == 0:
    raise Exception('no link found')
print(searchlist)