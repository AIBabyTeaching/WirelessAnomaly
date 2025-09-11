"""Download dataset placeholder."""
import hashlib
from pathlib import Path


def main():
    print("Download dataset from DOI 10.17632/p4n85smvms.1 and place under data/external/")
    Path("data/external").mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    main()
