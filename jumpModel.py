from peewee import *


db = MySQLDatabase(host="127.0.0.1",  user="root", passwd="", database="eve")

class jump (Model):
    id_system=IntegerField()
    jumps = IntegerField()
    time_cr = IntegerField()

    class Meta:
        database = db




class kills(Model):
    id =IntegerField(primary_key=True)
    solarSystemID =IntegerField()
    shipKills=IntegerField()
    factionKills=IntegerField()
    podKills=IntegerField()

    class Meta:
        database = db


db.connect()