import requests
import time
from xml.etree.ElementTree import fromstring, ElementTree
from jumpModel import *



class EVE ():
    _url = "http://api.eveonline.com/"
    _keyId = 1361382
    _ver_code = "MjriXAGICSL2h02jtCe66sNBufjJq0LGQf2kWOPxXMOaTBSaw0RG0gO2lC4jo86Y"


    def getJumpsLog(self):

        dopUrl = '/map/Jumps.xml.aspx'
        respons = self.get(dopUrl=dopUrl)
        for one in respons.find('result/rowset'):
            elements = one.attrib
            jump1 = jump()
            jump1.id_system = elements['solarSystemID']
            jump1.jumps = elements['shipJumps']
            jump1.time_cr = time.time()
            jump1.save()

    def getKillLog(self):
        dopUrl = '/map/kills.xml.aspx'
        respons = self.get(dopUrl=dopUrl)
        for one in respons.find('result/rowset'):
            k = kills()
            killsDict = one.attrib
            k.solarSystemID = killsDict['solarSystemID']
            k.shipKills = killsDict['shipKills']
            k.factionKills = killsDict['factionKills']
            k.podKills = killsDict['podKills']
            k.save()




    def get(self , dopUrl  , auth=False):
        """

        :param dopUrl: str
        :return:obj(ElementTree)
        """

        url = self._url +dopUrl

        if auth:
            authParam = {"keyID": self._keyId, "vCode": self._ver_code}
            req = requests.get(url , authParam )

        else:
            req = requests.get(url)

        if req.status_code != 200:
            return  False
        # print(req.content())

        strXML = req.content

        obj = ElementTree(fromstring(strXML.decode("utf-8")))
        return  obj.getroot()

    def opasnyeSystem(self):
        print('wwww')
        for one in kills.select().order_by(kills.shipKills.desc()):
            print("solatId: "+str(one.solarSystemID) +" shipKills: "+str(one.shipKills))
    def fullLog(self):
        while(True):
            self.getJumpsLog()
            self.getKillLog()
            print ("---===== OK ====-----")
            time.sleep(60*60)


    def getVerf(self , dopUrl):

        url = self._url + dopUrl
        auth = {"keyID":self._keyId,"vCode":self._ver_code}

