import urllib,re
htmlFile = urllib.urlopen("http://www.v-ringe.com")
html = htmlFile.read()
regexp_link = r'''<a href=[\'"]?([^\'" >]+)'''
pattern = re.compile(regexp_link)
links = re.findall(pattern, html)
 
#print all matches
print links