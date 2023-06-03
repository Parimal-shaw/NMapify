import xml.etree.ElementTree as trees
import re
import yaml
from pyfiglet import Figlet
import argparse
from rich import print as rprint

custom_fig = Figlet(font="banner3-D")
print(custom_fig.renderText("NMapify"))
Ports = ["25", "26", "22", "443", "80", "8080", "169", "553", "449", "2272"]

parser = argparse.ArgumentParser()#description=help_message(), )
parser.add_argument("-f","--file",dest="file",required=True, help="Nmap XML File Path (path/to/file)")
parser.add_argument("-o","--output",dest="output",required=True, help="Output File Path")
parser.add_argument("-t","--test_cases",dest="testcases", help="Test cases File Path in YAML format only.")
args = parser.parse_args()


rprint("[green]Please Wait it may Take Some Time ...[/green]")

def GenerateXML():
    root = trees.Element("node")
    root.set("Text", "Nmap_output")

    # Child node 1 for ip address
    for elements in new_list2:
        if re.match("[0-9]{0,2}.\.[0-9]{0,2}.\.[0-9]{0,2}.\.[0-9]{0,2}", elements):
            elem1 = trees.Element("node")
            elem1.set("Text", elements)
            elem1.set("Position", "right")
            root.append(elem1)

        elif re.match("\d", elements):
            sub1 = trees.SubElement(elem1, "node")
            sub1.set("Text", elements)
            # print(str(elements))
            # new subchild node 1 of subchild node for service and test cases
            subelem1 = trees.SubElement(sub1, "node")
            subelem1.set("Text", "Service")

            subelem2 = trees.SubElement(sub1, "node")
            subelem2.set("Text", "Test cases")
            # new subchild node 1 for subelem node for service name
        else:
            subelem1_sub1 = trees.SubElement(subelem1, "node")
            subelem1_sub1.set("Text", elements)
            subelem2_sub1 = trees.SubElement(subelem2, "font")
            subelem2_sub1.set("Bold", "true")
            subelem2_sub1.set("Name", "SansSerif")
            subelem2_sub1.set("Size", "12")
            if args.testcases:
                with open(args.testcases) as file:
                    config = yaml.safe_load(file)
                for x, y in config.items():
                    # print(x)
                    if str(x) == str(elements):
                        for data in y:
                            subelem3 = trees.SubElement(subelem2, "node")
                            subelem3.set("Text", data)
                    else:
                        continue
            else:
                with open("test_cases.yaml") as file:
                    config = yaml.safe_load(file)
                    for x, y in config.items():
                        # print(x)
                        if str(x) == str(elements):
                            for data in y:
                                subelem3 = trees.SubElement(subelem2, "node")
                                subelem3.set("Text", data)
                        else:
                            continue

    # subelem3 = trees.SubElement(subelem2,"node")
    # subelem3.set("Text",config)

    tree = trees.ElementTree(root)
    rprint("[green]Generating Mindmap ...[/green]")
    with open(args.output, "wb") as files:
        tree.write(files)


# Driver Code
if __name__ == "__main__":
    with open(args.file, "r") as file:
        xml_string = file.read()
        xml_string = re.sub(r"<hosthint>.*?</hosthint>", "", xml_string, flags=re.DOTALL)


    ipaddress_with_blank = []

    temp1 = []
    for x in xml_string.split("\n"):
        new9 = re.sub(r"<hosthint>.*?</hosthint>", "", str(x), flags=re.DOTALL)
        new3 = re.findall('\<port protocol\=.*. portid\=.*.\>\<state state\="open" reason\=.*. reason_ttl\=.*.\/\>\<service name\=".*." product\=|\<port protocol\=.*. portid\=.*.\>\<state state\="open" reason\=.*. reason_ttl\=.*.\/\>\<service name\=".*." servicefp\=|\<port protocol\=.*. portid\=.*.\>\<state state\="open" reason\=.*. reason_ttl\=.*.\/\>\<service name\=".*." tunnel\=|\<port protocol\=.*. portid\=.*.\>\<state state\="open" reason\=.*. reason_ttl\=.*.\/\>\<service name\=".*." method\=|\<port protocol\=.*. portid\=.*.\>\<state state\="open" reason\=.*. reason_ttl\=.*.\/\>\<service name\=".*." extrainfo=|\<port protocol\=.*. portid\=.*.\>\<state state\="open" reason\=.*. reason_ttl\=.*.\/\>|<address.*./>',str(new9),)
        new4 = re.sub('\[\'<address addr="|" addrtype="ipv4" />\'\]|\[\]|\<port protocol="(.*?)" portid="|\>|\<state state="open"|reason\="(.*?)"|product\=|reason_ttl="(.*?)"|\<service name\= \|\/|"|\'|\[|\]|addrstype="ipv4"|\/|servicefp\=|tunnel\=|method\="(.*?)"|extrainfo\="(.*?)"|addrtype\="ipv4"|method\=',"",str(new3),)
        new5 = re.sub("\/\<service name\=|\<service name\=", ":", str(new4))
        new6 = re.sub(" ", "", str(new5))
        temp1.append(new6)
    new_port_list = [x for x in temp1 if x != ""]
    new_list = [x for element in new_port_list for x in re.split((":"), element)]
    new_list2 = [x for x in new_list if x]

    rprint("[green]Fetching Data from XML file ...[/green]")
    GenerateXML()

    rprint("[green]Mindmap Has Been Generated Succesfully.[/green]")
