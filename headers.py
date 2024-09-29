#default hreaders
import requests

r= requests.get('https://httpbin.org/user-agent')
print(r)
print(r.text)

with open('x.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
    


#with integrated headers

import requests

r= requests.get('https://httpbin.org/user-agent', headers={
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
})
print(r)

with open('x.html', 'w', encoding='utf-8') as f:
    f.write(r.text)
