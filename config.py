'''
@author: qian.xieq 
'''

import urllib
import hashlib 


class CacheRule(object):
    def __init__(self,url,md5,pro):
        self.url = url
        self.md5 = md5
        self.pro = pro
    def __repr__(self):
        return 'CacheRule Object url : %s , md5 : %s' % (self.url,self.md5)
    
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def object2dict(obj):
    #convert object to a dict
    d = {}
    d.update(obj.__dict__)
    return d
 
 
html = getHtml("http://performance.oa.vtaoshop.net/oa.appcache")
start = html.index('CACHE:')
end = html.index('NETWORK:')
start = start + 6;
cache = html[start:end]
cachelist = cache.split('\r\n')
rulelist = []
for cache in cachelist:
    if cache.strip() != '':
        res =  "http://performance.oa.vtaoshop.net"+cache
        md5 = hashlib.md5(getHtml(res)).hexdigest()
        cacherule = CacheRule(res,md5,1)
        rulelist.append(object2dict(cacherule))
        
jsonstr =  '{"urlcaches:"'+str(rulelist)+'}'
try:
    man_file = open('config.json','w')
    man_file.write(jsonstr.replace('\'','\"'))
    man_file.close()

except IOError:
    print('File Error')
        

