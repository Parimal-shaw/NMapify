import xml.etree.ElementTree as trees
import sys
import re
import yaml
import pyfiglet
from pyfiglet import Figlet
import time
from colorama import init, Fore, Back, Style

Ports = ["25","26","22","443","80","8080","169","553","449","2272"]  

file = sys.argv[1]

init() 
custom_fig = Figlet(font='banner3-D')
print(custom_fig.renderText('NMapify'))

if str(sys.argv[1]) == "-h":
	print(Fore.YELLOW+"Usage:", end = '\n')
	print(Fore.YELLOW+"Provide Nmap Output In XML Format", end = '\n')
	print(Fore.RED+"Command Format:"+Fore.GREEN+" Python NMapify.py [/path/to/file/nmap_output.xml]", end = '\n')
	exit()

print(Fore.GREEN+"Please Wait it may Take Some Time ...", end = '\n')
time.sleep(2)

def GenerateXML(fileName) :
	root = trees.Element("node")
	root.set("Text","Nmap_output")
	
	#Child node 1 for ip address
	for elements in new_list2:
		if re.match("[0-9]{0,2}.\.[0-9]{0,2}.\.[0-9]{0,2}.\.[0-9]{0,2}",elements):
			elem1 = trees.Element("node")
			elem1.set('Text',elements)
			elem1.set('Position','right')
			root.append(elem1)
			
		elif re.match('\d',elements):
			sub1 = trees.SubElement(elem1,"node")
			sub1.set('Text',elements)
			#print(str(elements))
			#new subchild node 1 of subchild node for service and test cases
			subelem1 = trees.SubElement(sub1,"node")
			subelem1.set("Text","Service")
			
			subelem2 = trees.SubElement(sub1,"node")
			subelem2.set("Text","Test cases")
			#new subchild node 1 for subelem node for service name
		else:
			subelem1_sub1= trees.SubElement(subelem1,"node")
			subelem1_sub1.set("Text",elements)
			subelem2_sub1 = trees.SubElement(subelem2,"font")
			subelem2_sub1.set("Bold","true")
			subelem2_sub1.set("Name","SansSerif")
			subelem2_sub1.set("Size","12")
			with open('test_cases.yaml') as file:
				config = yaml.safe_load(file)
				for x,y in config.items():
					#print(x)
					if str(x) == str(elements):
						for data in y:
							subelem3 = trees.SubElement(subelem2,"node")
							subelem3.set("Text",data)
					else:
						continue


	#subelem3 = trees.SubElement(subelem2,"node")
	#subelem3.set("Text",config)
	
	tree = trees.ElementTree(root)
	print(Fore.GREEN+"Generating Mindmap ...", end = '\n')
	time.sleep(2)
	with open ("Output.mm", "wb") as files :
		tree.write(files)


f= open(file)
ipaddress_with_blank = []
'''
for x in f:
	new1 = re.findall("<address.*./>",str(x))
	new2 = re.sub("\[\'<address addr=\"|\" addrtype=\"ipv4\" />\'\]|\[\]","",str(new1))
	ipaddress_with_blank.append(new2)
ipaddress_list_new = [x for x in ipaddress_with_blank if x != '']
print(*ipaddress_list_new,sep ="\n")'''

temp1 = []
for x in f:
	new3 = re.findall("\<port protocol\=.*. portid\=.*.\>\<state state\=\"open\" reason\=.*. reason_ttl\=.*.\/\>\<service name\=\".*.\" product\=|\<port protocol\=.*. portid\=.*.\>\<state state\=\"open\" reason\=.*. reason_ttl\=.*.\/\>\<service name\=\".*.\" servicefp\=|\<port protocol\=.*. portid\=.*.\>\<state state\=\"open\" reason\=.*. reason_ttl\=.*.\/\>\<service name\=\".*.\" tunnel\=|\<port protocol\=.*. portid\=.*.\>\<state state\=\"open\" reason\=.*. reason_ttl\=.*.\/\>\<service name\=\".*.\" method\=|\<port protocol\=.*. portid\=.*.\>\<state state\=\"open\" reason\=.*. reason_ttl\=.*.\/\>\<service name\=\".*.\" extrainfo=|\<port protocol\=.*. portid\=.*.\>\<state state\=\"open\" reason\=.*. reason_ttl\=.*.\/\>|<address.*./>",str(x))
	new4 = re.sub("\[\'<address addr=\"|\" addrtype=\"ipv4\" />\'\]|\[\]|\<port protocol=\"(.*?)\" portid=\"|\>|\<state state=\"open\"|reason\=\"(.*?)\"|product\=|reason_ttl=\"(.*?)\"|\<service name\= \|\/|\"|\'|\[|\]|addrstype=\"ipv4\"|\/|servicefp\=|tunnel\=|method\=\"(.*?)\"|extrainfo\=\"(.*?)\"","",str(new3))
	new5 = re.sub("\/\<service name\=|\<service name\=",":",str(new4))
	new6 = re.sub(" ","",str(new5))
	temp1.append(new6)
new_port_list = [x for x in temp1 if x != '']
new_list = [x for element in new_port_list for x in re.split((':'),element)]
new_list2 = [x for x in new_list if x]
#print(*new_port_list,sep='\n')
print("Fetching Data from XML file ...")
time.sleep(2)
#print(str(new_port_list))
#print(str(new_list))
#print(str(new_list2))
# Driver Code
if __name__ == "__main__": 
    GenerateXML("tem.mm")

print(Fore.GREEN+"Mindmap Has Been Generated Succesfully.", end = '')	