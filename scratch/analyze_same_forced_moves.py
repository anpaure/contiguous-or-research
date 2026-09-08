import collections
import sys


def g(mask, m):
    before = []
    height = down_zero = 0
    for i in range(2 * m):
        before.append(height)
        if not mask >> i & 1 and height == 0:
            down_zero += 1
        height += 1 if mask >> i & 1 else -1
    seen = 0
    for i in range(2 * m):
        if not mask >> i & 1 and before[i] in (0, 1):
            seen += 1
            if seen == down_zero + 1:
                return mask | 1 << i, i
    raise AssertionError


def hmap(mask, m):
    before = []
    height = up_one = 0
    for i in range(2 * m):
        before.append(height)
        if mask >> i & 1 and height == 1:
            up_one += 1
        height += 1 if mask >> i & 1 else -1
    seen = 0
    for i in range(2 * m):
        if mask >> i & 1 and before[i] in (0, 1):
            seen += 1
            if seen == up_one:
                return mask & ~(1 << i), i
    raise AssertionError


def flip_word(word):
    m = len(word) // 2
    mask = sum((bit == "1") << i for i, bit in enumerate(word))
    out = []
    for _ in range(m):
        mask, a = g(mask, m)
        mask, b = hmap(mask, m)
        out += [a, b]
    return out + [2 * m]


def cyclic_cover_length(indices, n):
    if not indices:
        return 0
    indices = sorted(indices)
    gaps = [(indices[(i + 1) % len(indices)] - indices[i]) % n
            for i in range(len(indices))]
    return n - max(gaps) + 1


records = []
for line in open(sys.argv[1], encoding="utf-8"):
    if not line.startswith("same_forced_shortest "):
        continue
    fields = dict(item.split("=", 1) for item in line.split()[1:])
    word = fields["root"]
    if len(sys.argv) > 2 and len(word) != int(sys.argv[2]):
        continue
    p = int(fields["p"])
    q = int(fields["q"])
    records.append((word, p, q))

print("records", len(records))
print("gap_hist", collections.Counter(q - p for _, p, q in records))
print("p_hist", collections.Counter(p for _, p, _ in records))


def height_before(word, position):
    return sum(1 if bit == "1" else -1 for bit in word[:position])


print("height_at_p_hist", collections.Counter(
    height_before(word, p) for word, p, q in records if p >= 0))
print("nonadjacent", sum(q - p > 1 for _, p, q in records))
print("long_pattern_hist", collections.Counter(
    word[p:q + 1] for word, p, q in records if q - p > 1))
print("long_pq_hist", collections.Counter(
    (p, q) for word, p, q in records if q - p > 1))
if len(records) <= 20000:
    cover_hist = collections.Counter()
    support_hist = collections.Counter()
    cover_by_pattern = collections.defaultdict(collections.Counter)
    for word, p, q in records:
        if p < 0:
            continue
        mate = word[:p] + "1" + word[p + 1:q] + "0" + word[q + 1:]
        left = flip_word(word)
        right = flip_word(mate)
        changed = [i for i, (a, b) in enumerate(zip(left, right)) if a != b]
        cover = cyclic_cover_length(changed, len(left))
        cover_hist[cover] += 1
        support_hist[len(changed)] += 1
        cover_by_pattern[word[p:q + 1]][cover] += 1
    print("q_change_cover_hist", cover_hist)
    print("q_change_support_hist", support_hist)
    print("q_change_cover_by_pattern", dict(cover_by_pattern))
for word, p, q in records:
    if q - p > 1:
        print("long", word, p, q, "h", height_before(word, p),
              "middle", word[p:q + 1])
        if sum(1 for w, pp, qq in records if qq - pp > 1 and w <= word) >= 80:
            break

# Test deterministic local rules, all returning a candidate promotion p<q.
def candidates(word):
    ans = []
    for p, bit in enumerate(word):
        if bit != "0":
            continue
        for q in range(p + 1, len(word)):
            if word[q] == "1":
                ans.append((p, q))
    return ans


rules = {
    "leftmost_valley": lambda cs: min(cs, key=lambda x: (x[0], x[1])),
    "rightmost_valley": lambda cs: max(cs, key=lambda x: (x[0], -x[1])),
    "shortest_left": lambda cs: min(cs, key=lambda x: (x[1] - x[0], x[0], x[1])),
    "shortest_right": lambda cs: min(cs, key=lambda x: (x[1] - x[0], -x[0], -x[1])),
    "widest": lambda cs: max(cs, key=lambda x: (x[1] - x[0], -x[0])),
}
chosen = {(word, p, q) for word, p, q in records}
for name, rule in rules.items():
    hit = total = 0
    for word, _, _ in records:
        cs = candidates(word)
        if not cs:
            continue
        total += 1
        p, q = rule(cs)
        hit += (word, p, q) in chosen
    print("rule", name, hit, total)
