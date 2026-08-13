import itertools
import sys
from collections import Counter

lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
high = Counter()
triples = []
for line in lines:
    if not line.startswith("core="):
        continue
    words = line.split(" roots=", 1)[1].split(" supports=", 1)[0].split(",")
    decorated = []
    for word in words:
        heights = list(itertools.accumulate(1 if bit == "1" else -1 for bit in word))
        decorated.append((max(heights), word))
    decorated.sort()
    triples.append(decorated)
    high[decorated[-1][1]] += 1

print("high roots")
for word, count in sorted(high.items(), key=lambda item: (max(itertools.accumulate(
        1 if bit == "1" else -1 for bit in item[0])), item[0])):
    height = max(itertools.accumulate(1 if bit == "1" else -1 for bit in word))
    print(height, count, word)
print("triples")
for decorated in triples:
    print(" | ".join(f"h{height}:{word}" for height, word in decorated))
