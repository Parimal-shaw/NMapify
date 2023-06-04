
# NMapify
<p align="center">
  <img src="https://i.ibb.co/8MhwP3k/NMapify.jpg"  height="300"/>
</p>

NMapify is a powerful Python-based tool that enables users to generate mind maps for visualizing network layouts using Nmap's XML output. The tool comes with an added advantage of auto-generating test cases on each identified port using HackTricks, which can help in efficient network penetration testing. 

## Requirements

- NMap XML Output
- [Freemind v1.0.1](https://en.softonic.com/download/freemind/windows/post-download/v/1.0.1)
- Python 3




## Installation

### Pip Installation

```bash
  pip install NMapify
```

### Manual Installation
```bash
  git clone https://github.com/Parimal-shaw/NMapify.git
  cd NMapify
  pip install -r requirements.txt
```


## Usage/Examples

The generated output can be opened using Freemind.

```bash
python NMapify.py -f nmap-output.xml -o output.mm
```


## Acknowledgements

 - [HackTricks Test Cases](https://book.hacktricks.xyz/welcome/readme)


## Screenshot

 <img src="https://raw.githubusercontent.com/Parimal-shaw/NMapify/main/images/mindmap.png"  height="300"/>