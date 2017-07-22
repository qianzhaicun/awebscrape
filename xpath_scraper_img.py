from lxml.html import fromstring
from advanced_link_crawler import download

url = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = download(url)

tree = fromstring(html)
img = tree.xpath('//tr[@id="places_national_flag__row"]/td[@class="w2p_fw"]//@src')[0]
print('http://example.webscraping.com' + img)


