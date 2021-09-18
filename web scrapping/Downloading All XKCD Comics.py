import requests,os,bs4

url = 'https://xkcd.com/'
os.makedirs('xkcd')
while not url.endswith('#'):
    page = requests.get(url)
    print(page.raise_for_status())
    page_html = bs4.BeautifulSoup(page.text,'html.parser')
    image_link = page_html.select('#comic img')
    if image_link == []:
        print('no download link found')
    else:
        comic_link = 'https:' + image_link[0].get('src')
        download_link = requests.get(comic_link)
        print(download_link.raise_for_status())
        save_to_folder = os.path.join('xkcd',os.path.basename(comic_link))
        image_file = open(save_to_folder,'wb')
        for chunk in download_link.iter_content(100000):
            image_file.write(chunk)

    previous_link_on_page = page_html.select('a[rel="prev"]')[0].get('href')
    url = 'https://xkcd.com' + previous_link_on_page


print('done')