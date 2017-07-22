from lxml.html import fromstring, tostring
broken_html = '<ul class=country><li>Area<li>Population</ul>'
tree = fromstring(broken_html) # parse the HTML
fixed_html = tostring(tree, pretty_print=True)
tree = fromstring(fixed_html)
td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]
