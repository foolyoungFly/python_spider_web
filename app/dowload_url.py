# -*- coding: utf-8 -*- 

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re



class Dowwload(object):
    
    def __init__(self):
        self.names_=set()   
        
        
    def crawurl(self,url):
        
        repose = urlopen(url)
        soup = BeautifulSoup(repose.read(),"html.parser",from_encoding = "utf-8")
        title_node = soup.find('dd',class_ = "lemmaWgt-lemmaTitle-title").find("h1")
        title = title_node.get_text().encode('utf-8') 
        
        
        self.names_.add(title)
        same_ul = soup.find('ul',class_="polysemantList-wrapper cmn-clearfix")
        if same_ul!=None:
            same_lis = same_ul.find_all('li')
            stat_num= len(same_lis)+3
        else:
            stat_num =2
                
        links = soup.find_all('a',href=re.compile(r"^/item/"))
        if len(links)<stat_num+11:
            T = len(links)
        else:
            T = stat_num+10
        data = {"title":title,"nodes":[]}
        for i in range(stat_num,T):
            name = links[i].get_text().encode('utf-8')
            aurl = links[i]['href']
            realurl = "https://baike.baidu.com" + aurl
            if name not in self.names_:
                self.names_.add(name)
                node = {"name":name,"url":realurl.encode(encoding='UTF-8')}
                data["nodes"].append(node)
    
        return data
    
        