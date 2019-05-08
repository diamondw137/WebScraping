from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


def scrape_info():
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html


#scape page into soup
soup = BeautifulSoup(html, 'html.parser')

#  Parse HTML with Beautiful Soup
# Retrieve all elements that contain book information
articles = soup.find('li', class_='slide')
# print(articles)
news_title = articles.find(class_='content_title').text
news_para = articles.find(class_='article_teaser_body').text

news_data = {"new_title": news_title, "new_para":news_para}

browser.quit()

return news_data

def init_browser():
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape_info():
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# to be able to select the text to get images
browser.click_link_by_partial_text('FULL IMAGE')
browser.click_link_by_partial_text('more info')

#Parse Beautiful Soup
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#image retrival
image_urls = soup.find_all('div', class_='download_tiff')

#for loop
for image_url in image_urls:
    if "JPG" in image_url.text:
        featured_image_url = image_url.find('a')['href']
    else:
        continue 


#image print 
featured_image_url =  'https:'+ featured_image_url
print = print(featured_image_url)

#quit
browser.quit()

return print

#%%
import requests
from splinter import Browser
from bs4 import BeautifulSoup


#%%
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


#%%
url = 'https://twitter.com/marswxreport?lang=en'
data = requests.get(url)


#%%
print(data.text)


#%%
mars_weather = []
html = BeautifulSoup(data.text, 'html.parser')
timeline = html.select('#timeline li.stream-item')
for tweet in timeline:
    tweet_text = tweet.select('p.tweet-text')[0].get_text()


#%%
print(tweet_text)


#%%
browser.quit()


#%%
import pandas as pd


#%%
url = 'https://space-facts.com/mars/'


#%%
tables = pd.read_html(url)
tables


#%%
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


#%%
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


#%%
browser.visit(url)


#%%
html_hemispheres = browser.html


#%%
soup = BeautifulSoup(html_hemispheres, 'html.parser')


#%%
# results = soup.find_all('div', class_='item')
# for items in results:
#     print(items)


#%%
hemisphere_images_urls = []


#%%
for result in results:
    hemi_dict={}
    #get titles
    title = result.find('h3').text
    #thumb images 
    images = result.find('a', class_ = 'itemLink product-item')['href']
    print(images)
    #access the second page with full size image
    browser.visit('https://astrogeology.usgs.gov/'+ images)
    #second page html
    img_html = browser.html
    soup = BeautifulSoup(img_html, 'html.parser')
    #retrieve imagess
    imgs_url = url + soup.find('img', class_ = 'wide-image')['src']
    #append 
    hemi_dict=({"title" : title, "imgs_url" : imgs_url})
    hemisphere_images_urls.append(hemi_dict)
#     hemisphere_images_urls['title']=title
#     hemisphere_images_urls['imgs_url']=imgs_url


#%%
hemisphere_images_urls


#%%
hemisphere_images_urls[0]["title"]


