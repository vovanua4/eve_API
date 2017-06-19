
import requests
import time
from jumpModel import *
from eve import *
# import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring, ElementTree


eve = EVE()
eve.fullLog()
# eve.getJumps()
# eve.getKill()
# eve.opasnyeSystem();

from peewee import *



# urlAutoriz = "https://login.eveonline.com/oauth/authorize"
# urlAutoriz = "https://api.eveonline.com/account/"
#
#
#
# urlAPImain ="http://api.eveonline.com/"
# idKey = '6259293'
# key = 'hCbrVhVmAmAcrXUFboAooNFZKbTIe0Gz5IARVkRn7CqUQJnqlwTD2JMJfCWrm4y7'
# dopUrl = '/map/Jumps.xml.aspx'
# url = urlAPImain + dopUrl
#
# req = requests.get(url)
# htmStr = req.content
# # XMLobj = ET.fromstring()
#
# obj = ElementTree(fromstring(htmStr.decode("utf-8")))
# # obj = XMLobj.getroot()
# # result = obj.find('result/rowset/row')
# root = obj.getroot();
# # print(root)
#
# for one in root.find('result/rowset'):
#     elements = one.attrib
#     jump1 = jump()
#     jump1.id_system = elements['solarSystemID']
#     jump1.jumps = elements['shipJumps']
#     jump1.time_cr =time.time()
#     jump1.save()
#     # print( elements['solarSystemID'])
#
# '''
# https://api.eveonline.com/account/AccountStatus.xml.aspx?keyID=5342860&vCode=1JlLzA5N7fsKh0keyYfFQtkCfm4VvnO4coFXXUDun2ySQjd66AxxJF0OxljvdwdZ
# '''
#
#
# 'http://api.eveonline.com/map/Jumps.xml.aspx'
#
# import xml.etree.ElementTree as ET
#
#
#

