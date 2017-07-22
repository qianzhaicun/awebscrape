from advanced_link_crawler import link_crawler
from csv_callback import CsvCallback
link_crawler('http://example.webscraping.com/places/default/', '/(places/default/(index|view))',max_depth=-1, scrape_callback=CsvCallback())