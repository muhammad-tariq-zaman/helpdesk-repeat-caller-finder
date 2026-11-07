"""Find callers who opened many tickets recently.

Usage: python3 main.py tickets.csv [--threshold 3]
CSV columns: ticket,caller.
Callers at or above the threshold are REPEAT, most tickets first.
"""
import argparse, csv, sys
from collections import Counter

def find(rows, threshold):
    counts = Counter(r["caller"].strip() for r in rows)
    return sorted(((c, n) for c, n in counts.items() if n >= threshold), key=lambda r: -r[1])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--threshold", type=int, default=3)
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for caller, count in find(list(csv.DictReader(f)), args.threshold):
            print(f"{caller}: REPEAT ({count} tickets)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
