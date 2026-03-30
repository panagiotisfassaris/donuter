import donut
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Donut Python Wrapper (CLI Clone)")
    parser.add_argument("-i", "--input", required=True, help="Input executable/DLL")
    parser.add_argument("-a", "--arch", type=int, default=3, help="Target architecture: 1=x86, 2=amd64, 3=x86+amd64 (default: 3)")
    parser.add_argument("-b", "--bypass", type=int, default=3, help="Bypass AMSI/WLDP: 1=None, 2=Abort on fail, 3=Continue on fail (default: 3)")
    parser.add_argument("-p", "--params", type=str, default="", help="Command line parameters for the executable")
    parser.add_argument("-o", "--output", default="payload.bin", help="Output file")

    args = parser.parse_args()

    print(f"[*] Generating shellcode for {args.input}...")
    print(f"    - Arch:   {args.arch}")
    print(f"    - Bypass: {args.bypass}")
    print(f"    - Params: '{args.params}'")
    
    try:
        shellcode = donut.create(
            file=args.input,
            arch=args.arch,
            bypass=args.bypass,
            params=args.params
        )
        
        with open(args.output, 'wb') as f:
            f.write(shellcode)
            
        print(f"[+] Success! Shellcode saved to {args.output}")
        
    except Exception as e:
        print(f"[-] Error generating shellcode: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
