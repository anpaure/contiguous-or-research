# K16 H1: exact outside-edit kernel growth and the sharp stabbing boundary

Date: 2026-07-30  
Status: **proved solver-independent source-relative theorem; one-outside-site coupled fibre remains open**

## 1. Frozen source and notation

Let `x` be the authenticated length-12,873 one-hole word

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

with unique hole

```text
H = 0x2c6d.
```

Fix the joint13 support

```text
S = {0,1,4486,4487,4488,4489,6438,6439,6440,
     12869,12870,12871,12872}.
```

Its fixed complement is the union of the three integer intervals

```text
[2,4485], [4490,6437], [6441,12868].
```

For every nonzero target `t`, let

```text
W_x^S(t) = {source intervals I : OR_x(I)=t and I intersect S is empty}.
```

For an outside set `E` contained in the fixed complement, define the exact
active kernel

```text
K_S(E) = {t : every I in W_x^S(t) meets E}.
```

The empty-family convention is intentional: if `W_x^S(t)` is empty, then
`t` belongs to `K_S(E)` for every `E`.

## 2. Exact wider-support reduction

### Theorem 2.1 (active-kernel reduction)

Let `y` be any nonzero-mask word of length 12,873 and put

```text
E = {p outside S : y[p] != x[p]}.
```

Then every target outside `K_S(E)` has a literal `y`-witness disjoint from
`S union E`. Consequently,

```text
y is universal  <=>  y covers every target in K_S(E).             (2.1)
```

This is valid for arbitrary values on `S` and arbitrary nonzero replacement
values on `E`.

#### Proof

If `t` is outside `K_S(E)`, some source interval `I` in `W_x^S(t)` avoids
`E`. It also avoids `S` by definition. The words `x` and `y` therefore agree
at every position of `I`, so `OR_y(I)=t`. Thus all targets outside the kernel
are automatic, while the targets in the kernel are exactly the rows still
requiring verification. This proves (2.1).

For `E` empty, direct enumeration gives

```text
K_S(empty) = R,       |R|=55,
```

where `R` is exactly the residual family of item 1993. Theorem 2.1 therefore
strictly generalizes the fixed-complement part of that projection theorem to
an arbitrary outside edit set.

## 3. Exact interval dual and kernel growth

Let `tau(t)` be the minimum number of positions piercing `W_x^S(t)`. Because
these are intervals on a line, greedy earliest-finish packing gives the exact
duality

```text
tau(t) = maximum number of pairwise disjoint intervals in W_x^S(t).
```

Independent forward and reverse endpoint-state recurrences give the complete
histogram:

| `tau` | number of targets | `tau` | number of targets |
|---:|---:|---:|---:|
| 0 | 55 | 1 | 51,312 |
| 2 | 9,239 | 3 | 2,363 |
| 4 | 1,132 | 5 | 440 |
| 6 | 123 | 7 | 182 |
| 8 | 270 | 9 | 58 |
| 10 | 32 | 11 | 57 |
| 13 | 2 | 14 | 28 |
| 18 | 6 | 19 | 63 |
| 20 | 51 | 22 | 32 |
| 23 | 28 | 27 | 3 |
| 28 | 27 | 86 | 1 |
| 87 | 6 | 88 | 23 |
| 333 | 1 | 334 | 1 |

The 55 zero rows are exactly `R`. For every one of the 51,312 targets with
`tau(t)=1`, all fixed-only source witnesses have a nonempty common core

```text
C_t = intersection of all I in W_x^S(t).
```

Their length histogram is

```text
length  1     2      3       4       5      6    7  8
count   7220  7729   12879   13479   7631   2315 58 1.
```

The unique length-eight core is

```text
t = 0xcef7,       C_t = [6429,6436].
```

Most importantly, these common cores cover every one of the 12,860 outside
positions. Their exact position-load range is 1 through 20; the unique
minimum-load position is

```text
p = 6437,
```

covered only by the core of `t=0xc879`, namely `[6435,6437]`.

For a singleton outside set this is exact:

```text
|K_S({p})| = 55 + (number of common cores containing p).
```

Hence the exact singleton-kernel sizes range from 56 through 75. The unique
minimum 56 occurs at `p=6437`.

### Theorem 3.1 (linear kernel-growth floor)

For every outside edit set `E`,

```text
|K_S(E)| >= 55 + ceil(|E|/8).                                    (3.1)
```

#### Proof

For each `p` in `E`, choose a common core `C_t` containing `p`. Then `p`
meets every member of `W_x^S(t)`, so `t` belongs to `K_S(E)`. A fixed target
can receive charges from at most the positions of its core, and every core
has length at most eight. Hence the charged positions require at least
`ceil(|E|/8)` distinct nonempty-family targets. These are disjoint from the
55 empty-family targets already in `K_S(E)`, proving (3.1).

Thus a universal word with `e` outside edits must actively service at least

```text
55 + ceil(e/8)
```

distinct targets by intervals touching `S union E`. This is a genuine
source-relative workload lower bound that grows with unrestricted outside
support. It is not by itself an edit-count contradiction.

The complete core census gives a substantially stronger Hall-weighted form.
For an outside position `p`, put

```text
d(p) = number of common cores C_t containing p.
```

The exact load multiset is

| `d` | 1 | 2 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 1 | 2 | 4 | 1 | 22 | 199 | 451 | 1,038 | 1,690 | 2,017 |

| `d` | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 2,116 | 2,003 | 1,498 | 813 | 605 | 237 | 159 | 4 |

Let `L_e` be the sum of the `e` smallest entries of this 12,860-entry
multiset, with `L_0=0`.

### Theorem 3.2 (weighted core-incidence Hall bound)

For every outside set `E` of cardinality `e`,

```text
|K_S(E)| >= 55 + ceil(L_e/8).                                    (3.2)
```

In particular,

```text
e >= 30  ==>  |K_S(E)| >= e+49.                                  (3.3)
```

#### Proof

Let `X(E)` be the set of `tau=1` targets whose common core meets `E`.
Every target in `X(E)` belongs to `K_S(E)`, and double-counting the
position--core incidences gives

```text
sum_{p in E} d(p)
  = sum_{t:tau(t)=1} |C_t intersect E|
  <= 8 |X(E)|.
```

The left side is at least `L_e`, while `X(E)` is disjoint from the 55
empty-family targets. This proves (3.2). There are exactly 30 positions of
load below eight, and their total load is

```text
1*1 + 2*2 + 5*4 + 6*1 + 7*22 = 185.
```

Thus `L_e >= 185+8(e-30)=8e-55` for `e>=30`, and
`ceil((8e-55)/8)=e-6`, proving (3.3).

For scale, the exact profile gives

| `e` | 1 | 4 | 10 | 30 | 100 | 1,000 | 5,000 | 12,860 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `55+ceil(L_e/8)` | 56 | 57 | 61 | 79 | 149 | 1,185 | 6,794 | 21,017 |

These are lower bounds on the number of targets that become dependent on
the active support, not claims that all of them are holes of the edited
word. The value-dependent interval equations still have to service them.

## 4. H-valued portals incur an incompatible fixed-complement debt

Among the 51,312 common cores, 51,280 have

```text
H & ~t != 0,
```

so an `H`-valued cell cannot occur in an interval whose OR is `t`. These
`H`-incompatible cores also cover every outside position, again with minimum
load one and unique minimum row

```text
p = 6437,       t = 0xc879,       C_t = [6435,6437].
```

Consequently, replacing a single outside source cell `p` by `H` removes all
fixed-complement witnesses for at least one `H`-incompatible target `t`:
intervals avoiding `p` were already nonwitnesses, while intervals containing
`p` acquire an `H`-bit forbidden by `t`. That target must be serviced through
the active support. This is an exact fixed-complement debt statement, not a
claim that `t` is globally uncovered after arbitrary simultaneous edits.

## 5. Sharp boundary: single-family stabbing gives no bound above one

The full-source interval hypergraph of the 55 residual targets is extremely
thin:

```text
source occurrence count per target:  0:1, 1:51, 2:2, 3:1
total intervals:                     58
interval lengths:                    1:4, 2:7, 3:16, 4:18,
                                     5:8, 6:4, 7:1.
```

The only multiple-occurrence targets are

```text
0xa87d : 3 intervals
0xcc63 : 2 intervals
0xce63 : 2 intervals.
```

Every nonempty residual source family has

```text
packing number = piercing number = 1
```

and its common core contains a cell of `S`. There are 41 families whose
common core also contains an outside cell, 13 supported wholly inside `S`,
and the source hole `H` has no source interval.

For completeness, the union of all 58 source intervals has exact packing and
piercing number eight. One support-restricted minimum transversal is

```text
{0,1,4486,4489,6438,6440,12869,12871}.
```

The 43 edges belonging to the 41 outside-pierceable families have exact
outside-restricted piercing number six, with certificate

```text
{3,4485,4490,6437,6441,12868}.
```

These collective numbers do **not** lower-bound the escape set in item 1993,
because that escape alternative asks for all final-word witnesses of just one
residual target to meet `E`.

Indeed the one-edit bound is sharp at the witness-family level:

* For `T=H`, set one outside cell `p` to `H`. The singleton `[p,p]` is an
  `H`-witness, and every `H`-witness meets `p` because the source had none.
* For `T != H`, choose a common support cell `q` of all source `T`-witnesses,
  set `q` to `0xffff`, and set one outside cell `p` to `T`. The singleton
  `[p,p]` witnesses `T`. Any interval avoiding `p` either contains `q` and
  has OR `0xffff`, or avoids both changed cells and would be a source
  `T`-witness avoiding `q`, impossible.

The constructed words need not be universal. They prove precisely that no
uniform lower bound above one can follow from individual residual-family
stabbing plus arbitrary replacement values alone. A stronger theorem must
couple the enlarged kernel targets through value compatibility or capacity.

## 6. Remaining exact subcase

The joint13 obstruction settles `E=empty`. The next source-relative case is:

> Can 13 arbitrary values on `S`, together with one arbitrary-valued outside
> cell, cover the exact kernel `K_S({p})` for some outside position `p`?

Theorem 3.1 says this kernel has at least 56 targets for every `p`; Section 4
adds a literal incompatible debt when the portal value is `H`. The present
interval theorem does not prove the resulting 14-cell-support fibre
infeasible. This is the precise open subcase; no radius-at-most-three or
collar594 search is used here.

## 7. Replay artifacts and scope

Primary audit (independent forward and reverse compressed endpoint scans):

```text
scratch/audit_k16_h1_outside_edit_source_kernel_20260730.py
SHA-256 f60a85850a16c8b179945ae8c5ad0ab26a771a33763f48f766e6957c6916c760

scratch/k16_h1_outside_edit_source_kernel_20260730.audit.json
SHA-256 617cf6144d056ef28e2706dae94c113687f7c38da3e344dbe268d499f8500802
payload SHA-256 e1e73b2178f13bc10344fbe3bba235a367d624f31196017f436fbc4eda22eccb
```

Its exact fixed-only interval count is 32,616,502. The forward recurrence
uses at most 11 endpoint states, the reverse recurrence at most 12.

An independently written endpoint-range audit agrees on the authenticated
word, all 82,863,501 full-source intervals, all 32,616,502 fixed-only
intervals, the 55 residual targets, and the complete 58-edge residual census:

```text
scratch/audit_k16_h1_outside_escape_transversal_sharpness_20260730.py
SHA-256 440c4e3eace293b8cfb6f660b5cde475085cce465ca1b8684f2f67aa39845d86

scratch/k16_h1_outside_escape_transversal_sharpness_20260730.audit.json
SHA-256 1d213833fe5cb18f4d1d769f97d9ba3dfe11db75320d86b465876a8fcbdbc4ed
```

This package is solver-free and source-relative. It proves the exact active
kernel reduction and the growth floor (3.1). It does not prove unrestricted
length-12,873 or K16 UNSAT. The global bracket remains

```text
12873 <= nu(16) <= 12874.
```
