import xml.etree.ElementTree as trees
import re
import yaml
from pyfiglet import Figlet
import argparse
from rich import print as rprint
from rich.text import Text
from rich.console import Console
from lxml import etree
custom_fig = Figlet(font="banner3-D")
console = Console()
rprint(Text(custom_fig.renderText("NMapify"), style="green"))
rprint(Text("Version 0.3", style="red"))

parser = argparse.ArgumentParser()#description=help_message(), )
parser.add_argument("-f","--file",dest="file",required=True, help="Nmap XML File Path (path/to/file)")
parser.add_argument("-o","--output",dest="output",required=True, help="Output File Path")
parser.add_argument("-t","--test_cases",dest="testcases", default='test_cases.yaml',help="Test cases File Path in YAML format only.")
args = parser.parse_args()


rprint("[green]Please Wait it may Take Some Time ...[/green]")

def GenerateXML(new_list2):
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
            
            with open(args.testcases) as file:
                config = yaml.safe_load(file)
                file.close()
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
        files.close()

def xml_parser(file_path):
        new_list2 = []                        
        for event, elem in etree.iterparse(file_path, events=("end",), tag="host"):
                address = elem.find(".//address")
                if address is not None:
                    new_list2.append(address.attrib.get("addr"))
                    #print("Address:", address.attrib.get("addr"))
                    #print("Address type:", address.attrib.get("addrtype"))

                for port in elem.findall(".//port"):
                    #portid = port.attrib.get("portid")
                    #protocol = port.attrib.get("protocol")
                    #print("Port ID:", portid)
                    new_list2.append(port.attrib.get("portid")+'/'+port.attrib.get("protocol"))
                    #print("Protocol:", protocol)

                    state_elem = port.find("state")
                    state = state_elem.attrib.get("state") if state_elem is not None else "unknown"
                    #print("State:", state)

                    service_elem = port.find("service")
                    #service = service_elem.attrib.get("name") if service_elem is not None else "unknown"
                    #print("Service:", service)
                    new_list2.append(service_elem.attrib.get("name"))

                    # Free memory
                elem.clear()
        #print(new_list2)

        rprint("[green]Fetching Data from XML file ...[/green]")
        GenerateXML(new_list2)

def normal_parser(normal_file_output):
    normal_list2 = []
    for lines in normal_file_output.splitlines():
        #extract IP address
        new_line1 = re.findall( r'Nmap scan report for (.+)', lines, re.DOTALL)
        normal_list2.append(new_line1)
        #print(new_line1)
        #Extract Port Number
        newline2 = re.findall('.*. open', lines, re.DOTALL)
        newline2 = re.sub( ' open', '', str(newline2)).strip()
        newline2 = re.sub( ' ', '', str(newline2))
        #print(newline2)
        normal_list2.append(newline2)
        newline3 = newline2 = re.findall('open .*.', lines, re.DOTALL)
        newline3 = re.sub( 'open ', '', str(newline3))
        newline3 = re.sub( ' ', '', str(newline3))  
        #print(newline3)
        normal_list2.append(newline3)
    #print(normal_list2)
    cleaned = []
    for item in normal_list2:
        if isinstance(item, list) and item:  # Non-empty list
            cleaned.append(item[0])
        elif isinstance(item, str) and item not in ['[]', '']:
            # Extract the value inside the string list
            match = re.match(r"\['(.+?)'\]", item)
            if match:
                val = match.group(1)
                cleaned.append(val)
    GenerateXML(cleaned)

def is_xml_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            etree.parse(f)
        return True
    except (etree.XMLSyntaxError, OSError):
        return False

# Driver Code
if __name__ == "__main__":
    with open(args.file, "r") as file:
        if is_xml_file(args.file):
            xml_parser(args.file)
            rprint("[green]Creating Mindmap using the provided XML file...[/green]")
        else:
            normal_output = file.read()
            normal_parser(normal_output)
            rprint("[green]Creating Mindmap using the provided Normal file...[/green]")

rprint("[green]Mindmap Has Been Generated Succesfully.[/green]")
