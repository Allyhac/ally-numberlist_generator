import argparse

def gen(st, ls, filename):
    total = ls - st + 1
    print(f"[+] Generating {total} numbers...")

    if filename:
        with open(filename, "w") as f:
            for i in range(st, ls + 1):
                f.write(f"{i}\n")
    else:
        for i in range(st, ls + 1):
            print(i)

    print("[+] ✅ Done")
    print(f'[+]Generated {total} numbers ✅')
    if filename:
        print(f"[+] 📁 Saved {total} numbers to '{filename}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ally numeric wordlist generator")
    parser.add_argument("first_number", type=int ,help='first number where you want your wordlists to be generated. e.g: python gen.py 1 100')
    parser.add_argument("last_number", type=int,)
    parser.add_argument("-o", "--output", help="output file")

    args = parser.parse_args()

    gen(args.first_number, args.last_number, args.output)