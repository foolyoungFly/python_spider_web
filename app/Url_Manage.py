# -*- coding: utf-8 -*- 


class urlsManage(object):
    def __init__(self):
        self.urls = []
        
    def addnewUrl(self,url):
        if self.nothave(url):
            self.urls.append(url)
            

    def nothave(self,url):
        if url not in self.urls:
            return True
        else:
            return False