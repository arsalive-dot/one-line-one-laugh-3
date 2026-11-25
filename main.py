"""One Line, One Laugh — make.fun entry.

Writes a single funny line (<=200 chars) to /output/entry.txt.
The joke is a small, concrete humiliation: the GPS declares arrival
while the driver is still in the driveway, and the punchline is the
feeling of being judged by a robot. The laugh lands in the last
sentence: a machine's bland announcement becomes a verdict on the
driver.
"""

import os


ENTRY = (
    "My GPS said 'you have arrived' while I was still in the driveway. "
    "I have never felt so judged by a robot."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
