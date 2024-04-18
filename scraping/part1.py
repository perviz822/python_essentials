import requests
from bs4 import BeautifulSoup
r =  requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
#r1 =  requests.get('https://www.theguardian.com/world/2024/apr/18/man-arrested-schoolgirls-knife-attack-in-france')


#print(r1.headers)
#soup1 =  BeautifulSoup(r1.text,'html.parser')
#print(soup1.title)
#print(soup1.find('a').get_text())
#print(soup1.find_all('a'))


# a change from branch1
#  a  second change from branch1

























# response object

soup =  BeautifulSoup(r.text,'html.parser')

#print(r.text)

# the record shape in this website
'''<span class="short-desc">
<strong>Jan. 23&nbsp;</strong>
“Between 3 million and 5 million illegal votes caused me to lose the popular vote.” 
<span class="short-truth">
<a href="https://www.nytimes.com/2017/01/23/us/politics/donald-trump-congress-democrats.html" target="_blank">
(There's no evidence of illegal voting.)</a>
</span>
</span>'''


results =  soup.find_all('span',attrs={'class':'short-desc'})
print(len(results))
