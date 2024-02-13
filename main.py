# var
# condition
# loop (for, while)
# module
# function
# indentation
# list [1,2,3]
# str "test"
# tuple (1,2,3)
# dic  {1: "a", 2: 100}
# int 100
# set {100, 200}
# import yaml
# for i in range(10):
#     if i == 3:
#         continue
#     elif i == 6:
#         continue
#     elif i == 7:
#         break
#     else:
# #         print(i)
#
#
# var_while = 0
# while var_while < 10:
#     var_while += 1 # var_while = var_while + 1
#     if var_while == 5:
#         break
#     else:
#         print("hi")
import json

# for var_ip in range(1, 20, 2):
#     if var_ip == 18:
#         continue
#     else:
#         print("192.168.1.{}".format(var_ip))


# var_ip = 0
# while var_ip < 20:
#     var_ip += 1
#     if var_ip == 10:
#         continue
#     else:
#         print(f"192.168.1.{var_ip}")


# def func_1():
#     for var_ip in range(1, 20, 2):
#         if var_ip == 18:
#             continue
#         else:
#             print("192.168.1.{}".format(var_ip))
#
# func_1()


# def func_2(var_range):
#     var_list = []
#     for var_ip in range(1, var_range, 2):
#         if var_ip == 18:
#             continue
#         else:
#             print("192.168.1.{}".format(var_ip))
#             var_list.append("192.168.1.{}".format(var_ip))
#     return var_list
#
# var_range = int(input("please enter number: "))
# var_result = func_2(var_range)
# print(var_result)



# class ikco:
#     pass
#
# peugeot = ikco()
# peugeot.speed = 200
# peugeot.color = "red"
#
# samand = ikco()
# samand.speed = 180
# samand.color = "black"
#
# print(peugeot.speed)
# print(samand.speed)


# class ikco:
#     def __init__(self, name, speed, color):
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.test_mohsen()
#
#     def func_print(self):
#         print(f"name is {self.name} speed is {self.speed} color {self.color}")
#
#     def func_print_1(self):
#         print(f"name is {self.name} speed is {self.speed} color {self.color}*******")
#
#     def test_mohsen(self):
#         print("hi dostan")
#
# object1 = ikco("dena", 220, "red")
# object2 = ikco("samand", 200, "gray")
# object1.func_print()
# object2.func_print_1()
#
#








# class subneting:
#     def __init__(self, ip):
#         self.ip = ip
#
#     def func_even(self):
#         list_even = []
#         for i in range(2, self.ip, 2):
#             # print("even ip is 192.168.1.{}".format(i))
#             list_even.append("192.168.1.{}".format(i))
#         return list_even
#
#     def func_odd(self):
#         list_odd = []
#         for j in range(1, self.ip, 2):
#             # print("even ip is 192.168.1.{}".format(j))
#             list_odd.append("192.168.1.{}".format(j))
#         return list_odd
#
# # var_ip = int(input("please enter ip last octet:"))
# # object1 = subneting(var_ip)
# # object1.func_even()
# # object1.func_odd()
#
# class child_ip(subneting):
#     var_class = 10
#     def __init__(self, ip, sub):
#         self.sub = sub
#         # super().__init__(ip)
#         subneting.__init__(self, ip)
#
#     def final_even(self):
#         list_final_even = []
#         for t in self.func_even():
#             print(t+"/"+self.sub)
#             list_final_even.append(t+"/"+self.sub)
#         return list_final_even
#         #['192.168.1.2/24', '192.168.1.4/24','192.168.1.6/24']
#
#
#     def final_odd(self):
#         list_final_odd = []
#         for z in self.func_odd():
#             print(z+"/"+self.sub)
#             list_final_odd.append(z+"/"+self.sub)
#         return list_final_odd
#
# class child_file(child_ip):
#     def __init__(self, ip, sub, namefile):
#         self.namefile = namefile
#         super().__init__(ip, sub)
#
#     def save_to_file_even(self):
#         with open("{}.txt".format(self.namefile), "a+") as evenf:
#             for even_loop in self.final_even():
#                 evenf.write(str(even_loop))
#                 evenf.write("\n")
#
#
#     def save_to_file_odd(self):
#         with open("{}.txt".format(self.namefile), "a+") as oddf:
#             for odd_loop in self.final_odd():
#                 oddf.write(str(odd_loop))
#                 oddf.write("\n")
#
#
#
# var_ip = int(input("please enter ip last octet:"))
# var_sub = input("please enter subnet:")
# var_namefile = input("name file please: ")
# obj1 = child_file(var_ip, var_sub, var_namefile)
# obj1.save_to_file_even()




# class ip_class:
#     def __init__(self, ip):
#         self.ip = ip
#
#     def print_ip(self):
#         print("ip is {}".format(self.ip))
#
#
# class subnet:
#     def __init__(self, sub):
#         self.sub = sub
#
#     def print_subnet(self):
#         print(f"subnet is {self.sub}")
#
#
#
# class ip_subnet(ip_class, subnet):
#     def __init__(self, ip, sub, namefile):
#         self.namefile = namefile
#         ip_class.__init__(self, ip)
#         subnet.__init__(self, sub)
#
#     # def print_result(self):
#     #     print(str(self.ip)+self.sub)
#
#     def write_to_file(self):
#         with open("{}.txt".format(self.namefile), "w") as f:
#             for i in self.ip:
#                 f.write(str(self.ip)+self.sub)
#                 f.write("\n")
#
# list_1 = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
# object_child1 = ip_subnet(list_1, "/32", "writefile")
# # object_child1.print_result()
# object_child1.write_to_file()
#

# with open("writefile.txt", "a+") as f:
#     f.write("\n")
#     f.write("salam")
#     f.write("\n")
#     f.write("salam1")
#     f.seek(0)
#     print(f.read())
#
#

# name: testname
# family: testfamily
# age: 10
# listfile:
#   - 10
#   - 20
#   - 30
# dictfile:
#   a: 10
#   b: "hi"

# import yaml
#
# with open("testyamlf.yml", "r") as yf:
#     var1 = yaml.load(yf, Loader=yaml.SafeLoader)
#     print(var1)
#     print(type(var1))



# import yaml
# with open("testyamlf.yml", "r") as yf:
#     var1 = tuple(yaml.load_all(yf, Loader=yaml.SafeLoader))
#     print(var1)
# import yaml
#
# yaml_file = """
# - 'test1'
# - 'test2'
# """
#
# yaml_module = yaml.safe_load(yaml_file)
# with open("cretae_yaml.yaml", "w") as fi:
#     yaml.dump(yaml_module, fi)

# import xmltodict
# import json
#
# def convert_to_dict(xml_file):
#     dict_result = xmltodict.parse(xml_file)
#     print(dict_result)
#     var_json = json.dumps(dict_result, indent=4)
#     print(var_json)
#
#
#
# xml_file = '''
# <students>
#  <student>
#    <name>Rick Grimes</name>
#    <age>35</age>
#    <subject>Maths</subject>
#    <gender>Male</gender>
#  </student>
#  <student>
#    <name>Daryl Dixon </name>
#    <age>33</age>
#    <subject>Science</subject>
#    <gender>Male</gender>
#  </student>
#  <student>
#    <name>Maggie</name>
#    <age>36</age>
#    <subject>Arts</subject>
#    <gender>Female</gender>
#  </student>
# </students>
# '''
#
#
# convert_to_dict(xml_file)
#
# import json
#
# var1 = '{"a": "test1", "age": 23}'
#
# print(var1)
# print(type(var1))
# var_convert_to_dict = json.loads(var1)
# print(var_convert_to_dict['a'])
# print(type(var_convert_to_dict))
# var_indentation = json.dumps(var_convert_to_dict, indent=4)
# print(var_indentation)



# import json
#
# x = '{"a": 10, "b": 20, "c": 30}'
#
# print(x)
# print(type(x))
# var_convert_todict = json.loads(x)
# print(var_convert_todict)
# print(type(var_convert_todict))
# print(var_convert_todict["a"])








# import json
# x = {
#     "name": "MTC",
#     "status": "Telecom",
#     "age": 20
# }
# print(type(x))
# print(x)
# var_convert_tojson = json.dumps(x)
# print(var_convert_tojson)
# print(type(var_convert_tojson))


# import json
# x = {
#     "name": "MTC",
#     "status": "Telecom",
#     "ID": 1010,
#     "Best": True,
#     "DC": [
#         "motahari",
#         "paya"
#     ]
# }
#
# print(type(x))
# print(x)
#
# print(json.dumps(x, indent=4, sort_keys=True))


# from netmiko import ConnectHandler
# import re
#
# var_connection = ConnectHandler(device_type="cisco_ios", ip="192.168.50.158", username="test", password="test")
# var_result = var_connection.send_command("sh ip int brief")
#
# print(var_result)
# print(type(var_result))
#
# var_regex = re.findall("\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", str(var_result))
# print(var_regex)
# for var_listnetmiko in var_regex:
#     print(var_listnetmiko)

# import requests

#
# url = "https://stat.ripe.net/data/announced-prefixes/data.json?resource=AS3333&starttime=2011-12-12T12:00"
# var_req = requests.request("GET", url).json()
# var_list = var_req["data"]["prefixes"]
# for list_api in var_list:
#     print(list_api['prefix'])

# print(var_req)
# print(var_req.text)







