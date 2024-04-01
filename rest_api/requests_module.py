import requests
'''url = 'https://www.ibm.com/'
r =  requests.get(url)
print(r.status_code)
print(r.headers)
print(r.request.body)
print(r.headers['date'])
print(r.headers['content-type'])
print(r.text)'''

base_url = 'http://httbin.org/get'

payload ={"name":"Parviz","ID":"123"}

r =  requests.get(base_url,params=payload)

'''print(r.url)
print(r.request.body)
print(r.text)
print(r.status_code)
print(r.headers['Content-type'])
print(r.json())
'''

payload ={"name":"Parviz","ID":"123"}

url_post = 'http://httpbin.org/post'
r_post = requests.post(url_post,data=payload)

#print(r_post.url)



#print(r_post.request.body)
print(r_post.request.body)
#why only post has a body





