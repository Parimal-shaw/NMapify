# NMapify <br />
Creating a mindmap from an Nmap XML output can be a complex and time-consuming process, but with the right tools, it can be made much simpler and speedier. 
With the help of a specialized tool, converting Nmap XML output into a mindmap with test cases is easy, fast, and efficient. 
This tool helps users quickly and accurately create a visual representation of their Nmap output, allowing them to better understand the data and make better decisions. 
__This tool is perfect for users who need to quickly and accurately convert Nmap XML output into a mindmap with test cases.__<br />

## Information <br />
This tool is for those who need to test Internl and External Network and test each and every port thoroughly to find any kind of vulnerability and resolve it too.<br />
The main task of the tool is to convert and nmap xml output into visually comfortablle format so that we can perform further testing on it.
This tool extract all the __Open ports__ of all the ip provided by Nmap (Network Mapper) Tool with the Service name from the output file and generate a Mindmap file which make it easy to understand the open port and do further testing for each Open Ports thoroughly to solve the second part to for adding the test cases according to each port and Service this tool alse helps in adding all the test cases in the network pentester perspective to each and every node of open ports in the mindmap.<br />
All the Test Cases have been taken from [Hacktricks](https://book.hacktricks.xyz/network-services-pentesting/)<br />

This tool helps us to convert the following Nmap output to the Mindmap <br />
<img src="/images/Nmap_output.png" width="400" height="250">    <img src="/images/mindmap.png" width="400" height="250"><br />
To Preview the mindmap and to make changes to it we require [Freemind](https://en.softonic.com/download/freemind/windows/post-download/v/1.0.1) Application <img src="https://upload.wikimedia.org/wikipedia/commons/d/d9/Free_Mind.png"  width="20" height="20"> <br />

## Requirements
__Mindmap Viewer:__<br />
[Freemind v 1.0.1](https://en.softonic.com/download/freemind/windows/post-download/v/1.0.1) (Works best with this Version)

## Installations
1. We need to download the files <br />
```
$ git clone https://github.com/Parimal-s/NMapify.git
```

2. Go the the Nmapify directory
```
$ cd NMapify
```

3. Install all the requirments with the following command
```
$ pip install -r requirements.txt
```

## Usage
After installing requirements we are good to run the tool with the following command and also provide nmap xml file at the end.
```
$ python NMapify.py /path/to/nmap_output.xml
```

### Thank You for Visiting My Repo :blush:
