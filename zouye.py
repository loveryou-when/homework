#homework(1)
import urllib.request
import urllib.request
x=input('请输入x：')
def f(x):
    x+1
print(f(x)) 
data = urllib.parse.urlencode({'wd':str(x)})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)
#homework2:
import urllib.request
import urllib.request

data = bytes(urllib.parse.urlencode({'wd':'央视'}),enconding='utf8')
url = 'http://www.cctv.com/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)

