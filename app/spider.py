# -*- coding: utf-8 -*-
import Url_Manage, dowload_url


class Spider(object):


    def __init__(self):
        self.urlmanage = Url_Manage.urlsManage()
        self.getData = dowload_url.Dowwload()
    def get_node(self,url):
        if self.urlmanage.nothave(url):
            self.urlmanage.addnewUrl(url)
            data = self.getData.crawurl(url)
            if data!=None:        
                node = {"title":data["title"],"nodes":data["nodes"]}
                return node
        else:
            return None