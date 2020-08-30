# import os
# os.system("ssh harikrishnan.m@192.168.2.13")
# os.system("echo msil@1234")

import json

with open('sample.json') as jsonFile:
    jsonResult = json.load(jsonFile)
    jsonResultFailures = jsonResult['run'].get('failures')
    jsonResult = jsonResult['run'].get('executions')
    print(len(jsonResultFailures))

print("Test Result analysis Started...\n")
if (len(jsonResultFailures) > 0):
    
    for i in range(len(jsonResult)):
        if ('assertions' in jsonResult[i]):
            print("\nChecking '{0}' result...\n".format(jsonResult[i].get('item')['name']))
            for assertion in range(len(jsonResult[i].get('assertions'))):
                if (jsonResult[i].get('assertions')[assertion].get('skipped') == False):
                    print("{0} failed.".format(jsonResult[i].get('assertions')[assertion], "\n"))
            print("\n'{0}' analysis done...".format(jsonResult[i].get('item')['name']))
            print("*"*50)
        
    print("\nTest Result analysis complete....")
else:
    print("No Failures :)")