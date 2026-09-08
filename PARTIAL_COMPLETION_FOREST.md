# Linear-forest completion of a partial universal OR word

## 1. Completion lemma

Let a word `A` cover every nonzero mask except two finite families

```text
F subset C([k],r),
G subset C([k],r+1).
```

Create one base vertex labelled by each mask in `F`.  Choose some additional
auxiliary vertices, also labelled by nonzero masks.  Suppose the chosen edges
form a **linear forest**: every vertex has degree at most two and there is no
cycle.  Require every target in `G` to be handled in one of two ways:

1. it is the OR of the labels on one selected edge; or
2. it is reserved as one additional literal entry.

Order the vertices along each path component and concatenate the components
in any order.  Then append the reserved literals.  Appending this word to `A`
completes every target.  Its length is

```text
|F| + number of auxiliary vertices + number of reserved literals.
```

Indeed, each member of `F` is now a singleton entry, each edge remains an
adjacent pair inside its path component, and every reserved target is a
singleton.  Extra OR values and arbitrary joins between components are
harmless.

### Shared auxiliary bridge

An especially useful local gadget handles two upper targets at once.  Suppose
`U,V in G` have chosen **distinct** base masks `P,Q in F`, and a nonzero mask `X` satisfies

```text
P OR X = U,
X OR Q = V.
```

Then the three-entry path

```text
P, X, Q
```

covers both `U` and `V` using one auxiliary entry.  When `P` is the unique
member of `F` contained in `U` and `Q` is the unique member contained in `V`,
one may take

```text
X = (U without P) OR (V without Q)
```

exactly when this mask is contained in both `U` and `V`.

The construction is a sufficient completion theorem.  It does not claim that
every shortest completion must have this form.

## 2. Certified `k=11` completion

The 465-entry factor `k11_upper549_natural_array.txt` misses precisely the
twelve rank-seven masks

```text
251 493 607 941 956 1267 1468 1694 1763 1884 1946 1990
```

and the rank-eight mask `958`.

If the completion is required to stand alone, length 13 is optimal.
Twelve rank-seven omissions form an antichain, so any completion needs at
least twelve positions.  At equality their twelve witnesses must be the
twelve singleton positions.  Their entries therefore equal the twelve
omitted rank-seven masks.  Since only one is contained in 958, no interval of
that twelve-entry word can OR to 958.  Thus a thirteenth position is necessary.

The old/new seam saves one entry.  The exact append model
`append_completion_sat.cpp` found the twelve-entry word

```text
243 1216 774 956 941 1468 607 1694 1946 1763 1884 493
```

and appending it gives `k11_completed_477.txt`.  Most omissions occur inside
the appended block.  The essential cross-seam witness is

```text
251 = A[464] OR A[465] = 11 OR 243,
```

while `958=774 OR 956`.  The complete witness list is
`k11_append_12_witnesses.txt`.

This append length is optimal for the fixed prefix.  None of the twelve
rank-seven masks occurred before the seam, so each needs a suffix ending at a
new position.  Suffix ORs at one right endpoint form a chain and contain at
most one rank-seven mask.  Therefore twelve distinct new right endpoints are
necessary, and the displayed extension attains that bound.

Consequently

```text
nu(11) <= 477,
N(11) <= 478.
```

## 3. Stronger `k=14` completion

The genuine 3434-entry factor `k14_pinnable_factor_missing260.txt` misses
exactly 238 rank-nine masks and 22 rank-ten masks.  Fourteen upper targets
have at least two missing rank-nine subsets.  Selecting one pair for each can
be done so that the selected edges form a linear forest.

Seven further upper targets have exactly one missing rank-nine subset.  Three
compatible pairs of those targets share one auxiliary bridge each:

| auxiliary `X` | first `P -> U` | second `Q -> V` |
|---:|---|---|
| 288 | `7420 -> 7676` | `15302 -> 15334` |
| 8196 | `13283 -> 13287` | `6093 -> 14285` |
| 48 | `13423 -> 13439` | `13725 -> 13757` |

The remaining upper masks `15346` and `8015` are appended literally.  The
selected direct edges and the three two-edge auxiliary bridges simultaneously
form a linear forest on the 238 base vertices and three auxiliary vertices.
Linearizing its components and appending the two literals gives

```text
238 + 3 + 2 = 243
```

completion entries.  The resulting certificate `k14_completed_best.txt` has
length

```text
3434 + 243 = 3677.
```

Therefore

```text
nu(14) <= 3677,
N(14) <= 3678.
```

This is stronger than both the old 3704 lift and the naive 260-literal
completion length 3694.  The 243-entry word is now proved shortest among
standalone completions of these 260 masks.  The endpoint-defect proof is in
`K14_PARTIAL_COMPLETION_IMPROVEMENT.md` and its independent audit is
`K14_PARTIAL_COMPLETION_OPTIMALITY_INDEPENDENT_AUDIT.md`.  This does not rule
out a 242-entry appended suffix using witnesses that cross the old/new seam,
and therefore is not a global lower bound on `nu(14)`.

### Cross-seam improvement

Such a 242-entry suffix now exists.  Prepending `1095,8014,15694` to a
mechanical rearrangement of the standalone completion uses two suffix ORs of
the unchanged prefix:

```text
12329 OR 1095 = 13423,
12409 OR 1095 = 13439.
```

The combined certificate `k14_completed_3676.txt` has nonzero length 3676,
so `nu(14)<=3676` and `N(14)<=3677`.  Any suffix for this fixed prefix has
length at least 241.  The explicit construction, endpoint proof, and exact
remaining 241-branch reduction are in `K14_CROSS_SEAM_COMPLETION_NEXT.md`;
the independent audit is `K14_APPEND_242_INDEPENDENT_AUDIT.md`.

### Exact remaining 241-entry decision problem

The fixed-prefix question at 241 entries is no longer an informal branch
suggestion.  `scratch/k14_append241_exact.cpp` gives a sound-and-complete
52-formula disjunction retaining arbitrary nonzero suffix entries, every
append-only interval, and every possible old/new crossing interval.  The
branches split as `9+31+12` for respectively one, two, and three selected
rank-nine crossings.  Each has 1,012,539 variables and about 2.632 million
source clauses.

The encoding and all 52 build inventories are described in
`K14_APPEND241_EXACT_ENCODING.md`; the independent source/formula audit
`K14_APPEND241_ENCODING_INDEPENDENT_AUDIT.md` reports PASS.  A SAT branch
would give `nu(14)<=3675`.  A fixed-prefix optimality claim requires checked
refutations of all 52 branches.  Initial representative runs are live, but no
SAT or UNSAT result is currently claimed.

## 4. Reproduction and certificates

`partial_completion_forest.cpp` computes the missing families, chooses direct
edges and compatible shared auxiliaries under the linear-forest constraint,
emits the completion and combined word, and performs a suffix-OR coverage
check.  It is a sufficient constructor, not a complete shortest-completion
optimizer.  Production compilation and all searches were run remotely with C++
optimization, not on the local Mac.

The two completed words were then checked independently by:

1. exhaustive enumeration of every physical interval using
   `verify_or_array.cpp`; and
2. the distinct-suffix-OR recurrence using `verify_or_suffix.cpp`.

Both report full coverage:

```text
k=11: length=477,  covered=2047/2047;
k=14: length=3676, covered=16383/16383.
```

Key SHA-256 values are:

```text
aa88d2c22431af19e4b4c4a2073251d1316d02a6e152d218cca2082bdc58d58b  k11_completed_477.txt
ba44a89403c6b402fb6c9b48cd8a1274dd716cd56885af710db8f091e8ee6989  k11_append_12.txt
099ec7dbe7f706f84645592faa17bd9f436d4cbaff9c8cda7b0031ae1e023012  k11_append_12_witnesses.txt
d5fc5c13685ca0e2eb182de0d245e93368453d0aaeaf6e2f5cfdff219a59c83c  k14_completed_best.txt
06f4b5a06f411a896df9d471b4e2f60d97eea537b4c81710f5e1c62117d68b19  k14_completion_best.txt
41d7028668cde93d6f9347ae881b352dfbc3de446845324a185b21414099d8a8  k14_append_242.txt
df86beff2854227f215a8720a7959489c689d3d3d5747e9847a2ff9fd3aeac94  k14_completed_3676.txt
f7e362a9248ae1aaf32036bd47904e246342fd5c7b231584d04be4d6e5b5b38d  k14_append_242_seam_certificate.txt
ae2aa7d6fd67da00ce33452f19fa9375b7189a3812f885080bc38641ec0c8a23  k11_completed_477_exhaustive.log
cb2c0650d53926e3327d36c1a50cec8e8783194349ce309aa9ae9f955b76d741  k11_completed_477_suffix.log
180074fdc468b4fde2bb6ca5c346c420ab3186ccc9ccd1d327857c1e32e36828  k14 exhaustive log
74d4f71ba91f72c76ddf76378ae1652b3b1384e7964ad15bc2636e19f83d3450  k14 suffix log
49e044c4d1be8a144bec80026ac4ceef41002fe7b1c133a64dd97952ed8ceed5  k14_completed_3676_exhaustive.log
c8565cc9d1f594bcbe479cd8844535eb3dcfbe6a5d865285225c0cb34c59ea13  k14_completed_3676_suffix.log
```

The fixed-prefix `k=11` append, its explicit witness selectors, both verifier
families, the endpoint-chain lower bound, and the SAT encoding used to find it
were independently regenerated and audited in
`K11_APPEND_12_INDEPENDENT_AUDIT.md` (SHA-256
`1ad88f4807f2450d0cd3b8a2210a22ba949a980163f3a324d438cf30e6951a8e`).
The interval indices in `k11_append_12_witnesses.txt` are zero-based.
