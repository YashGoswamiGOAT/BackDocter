import json
data = open('hospitaldata.txt','r').read()
import pandas as pd
from graph import HashMap

Hospitals = json.loads(data)

def Frame(hospital):
    HOSP_NAME = hospital['HOSP_NAME']
    HOSP_TYPE = hospital['HOSP_TYPE']
    HOSP_CONTACT_NO = hospital['HOSP_CONTACT_NO']
    HOSP_EMAIL_ID = hospital['HOSP_EMAIL_ID']
    HOSP_ADDRESS = hospital['HOSP_ADDRESS']
    SPECIALTY_NAME = str(hospital['SPECIALTY_NAME']).replace('<br>',"")
    DISTRICT_NAME = hospital['DISTRICT_NAME']
    return (([HOSP_NAME,HOSP_TYPE,DISTRICT_NAME,SPECIALTY_NAME,HOSP_CONTACT_NO,HOSP_EMAIL_ID,HOSP_ADDRESS]))

csv = [['HOSP_NAME','HOSP_TYPE','DISTRICT_NAME','SPECIALTY_NAME','HOSP_CONTACT_NO','HOSP_EMAIL_ID','HOSP_ADDRESS']]
for hospital in Hospitals:
    csv.append(Frame(hospital))
# pd.DataFrame(csv).to_csv('data.csv')

specs = HashMap()
for hospital in csv:
    for spec in hospital[3].split(","):
        while (spec.__contains__("  ")):
            spec = spec.replace("  "," ")
        spec = spec.split("(")[0]
        specs.set(spec,1)

# print(open("specility.txt","w").write(str(specs.keys())))
print(len(specs.keys()))