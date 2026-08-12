# Independent audit of the even top-bit splice recurrence

**Date:** 2026-07-31  
**Verdict:** PASS, with the minor domain clarification `k >= 2`

The construction

```text
X | b | (x_1|b),...,(x_(n-1)|b)
```

is universal and has length `2n`.  The potentially delicate case is an old
target `A` whose chosen witness ends at `x_n`.  Its marked copy is not needed:
the original suffix witness followed by the adjacent singleton `b` is a
contiguous interval with OR `A union {b}`.  Thus omitting `x_n|b` is
intentional and correct.

The theorem should explicitly assume `k >= 2` (or `n >= 1`).  If one defines
the empty word as universal on the empty ground set, the displayed length
identity is not the `k=1` construction.

An independent replay from `answers/k15.word` checked one selected witness
for every old nonempty mask.  Of the `32,767` selected witnesses, `3` use the
last source letter and are correctly delivered across the central singleton.
The resulting length-`12,876` word covers all `65,535` nonempty `k=16` masks.

For even `k=2m`,

```text
W(k) = 2 W(k-1),
2 B(k-1) = B(k) + 2 d(k-1) - d(k).
```

The requested arithmetic is:

| `k` | `d(k-1)` | `d(k)` | overhead |
|---:|---:|---:|---:|
| 16 | 3 | 3 | 3 |
| 24 | 4 | 3 | 5 |
| 42 | 5 | 4 | 6 |
| 64 | 6 | 5 | 7 |

Therefore the recurrence gives length `12,876` at `k=16`, which is weaker
than the existing verified `12,874` upper bound and does not decide whether
the optimum is `12,873` or `12,874`.

The former claims `2d(k-1)-d(k) <= 4` for all even `k` and constant overhead
three for all even `k >= 16` are false.  Since

```text
d(k) = sqrt(pi*k/8) + O(1),
```

the even recurrence overhead is `Theta(sqrt(k))`, not `O(1)`.

Replay artifacts:

```text
scratch/audit_even_topbit_splice_recurrence_20260731.py
scratch/even_topbit_splice_recurrence_20260731.audit.json
```
