# donuter
A lightweight Python wrapper for Donut shellcode generator

## Installation

You don't need `make` or `gcc` for this. Just grab the Python package and you're good to go.

```bash
# Install the core donut-shellcode library
pip3 install donut-shellcode

# Clone this wrapper
git clone https://github.com/panagiotisfassaris/donuter.git
cd donuter
```
---

## Syntax

```
python3 donuter.py -i <INPUT_FILE> [OPTIONS]
```

---

## Arguments
```
-i	--input	[Required] Path to the input executable or DLL	(Default = None)
-o	--output	Output payload file name	(Default = payload.bin)
-a	--arch	Target architecture: 1=x86, 2=amd64, 3=x86+amd64	(Default = 3)
-b	--bypass	AMSI/WLDP bypass: 1=None, 2=Abort on fail, 3=Continue on fail	(Default = 3)
-p	--params	Command line parameters to pass to the executable	(Default = "")
```

---

## Examples

Basic executable conversion (defaults to `x86+x64` & output to `payload.bin`):
```
python3 donuter.py -i mimikatz.exe
```

Specifying architecture and output file:
```
python3 donuter.py -i safetykatz.exe -a 2 -o loader.bin
```

Passing command-line parameters to the executable:
```
python3 donuter.py -i Rubeus.exe -p "triage" -o rubeus.bin
```

![GodPotato Example](/example_usage_godpotato.png)

---

## ⚠️ Disclaimer
This tool is designed for authorized red teaming, penetration testing, and security research. Don't do bad things with it. I am not responsible for what you do with this code.
