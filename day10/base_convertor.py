"""Day 10: number base converter (dec, bin, oct, hex)."""

BASES = {"dec": 10, "bin": 2, "oct": 8, "hex": 16}


def parse(text, base):
    """Text → int. Raise ValueError if invalid for base."""
    return int(text.strip(), base)


def convert(n):
    """int → dict of all bases."""
    return {
        "dec": str(n),
        "bin": bin(n)[2:],
        "oct": oct(n)[2:],
        "hex": hex(n)[2:].upper(),
    }


def main():
    print("Base converter. Bases: dec, bin, oct, hex. Type 'q' quit.")
    while True:
        src = input("\nFrom base: ").strip().lower()
        if src == "q":
            break
        if src not in BASES:
            print("Pick: dec, bin, oct, hex")
            continue

        value = input("Number: ").strip()
        if value.lower() == "q":
            break

        try:
            n = parse(value, BASES[src])
        except ValueError:
            print(f"Bad {src} number: {value}")
            continue

        if n < 0:
            print("Negative not supported.")
            continue

        for name, result in convert(n).items():
            print(f"{name}: {result}")


if __name__ == "__main__":
    main()