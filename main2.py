# from main1 import test
#
# print(test())


from pyntc import ntc_device as NTC
import json

var1 = NTC(host='192.168.55.5', username='cisco', password='cisco', device_type='cisco_ios_ssh')
var1.open()

var2 = var1.facts
print (json.dumps(var2, indent=4))