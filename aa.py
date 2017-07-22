import re
link = '/places/default/index/3'
link_regex = '/(places/default/(index|view))'
if re.match(link_regex, link):
    print(1)