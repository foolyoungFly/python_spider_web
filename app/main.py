# -*- coding: utf-8 -*- 
import spider



def getdata(Name):
    url = "https://baike.baidu.com/item/"+Name.encode(encoding='UTF-8')
    
    
    sp = spider.Spider()
#     download = dowload_url.Dowwload()
#     print download.crawdata(url)
    data= sp.get_node(url)
    print data["title"]
    data_dict = {
        "nodes": [{"name": data["title"], "symbolSize": 60,"category":0}],
        "links": []
    }
    #data_dict["nodes"].append({"name": data["name"], "symbolSize": 60,"category":0})
    nodes = data["nodes"]
    for node in nodes:
        data_dict["nodes"].append({"name": node["name"], "symbolSize": 40,"category":1})
        data_dict["links"].append({"source":data["title"],"target":node["name"]})
        node_url = node["url"]
        node_data = sp.get_node(node_url)
        if node_data!= None:
            print "  "+node_data["title"]
            source = node["name"]
            for thrid_node in node_data["nodes"]:
                print "    " +thrid_node["name"]
                data_dict["nodes"].append({"name": thrid_node["name"], "symbolSize": 20,"category":2})
                data_dict["links"].append({"source":source,"target":thrid_node["name"]})
    return data_dict 
    #json_file= open("data.json","w")
    #json_file.write(json.dumps(data_dict))
    
    
    