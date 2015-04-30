 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml




#with open("bernadotte.yaml") as f:
    #family = yaml.load(f)



#pprint(family)

with open("bernadotte.yaml") as f:
        docs = yaml.load(f)


def skriv_ut_namn(docs):



    for i in docs():

        if i == "name":
            for n in i:
                print n

        else:
            skriv_ut_namn(i)



skriv_ut_namn(docs)




