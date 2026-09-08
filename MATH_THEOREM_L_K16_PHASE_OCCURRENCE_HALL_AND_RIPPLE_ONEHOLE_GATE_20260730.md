# K16 phase-occurrence Hall theorem and the ripple one-hole gate

**Date:** 2026-07-30  
**Status:** exact solver-free Hall obstruction and scoped portal local-minimum theorem

## 1. Frozen finite status

The current exact bracket is

\[
12873\le \nu(16)\le12875.
\]

The upper certificate is

```text
answers/k16_upper12875.word
SHA-256 d4690a0d11f1d8e69765ec988d9fbcbac63d354ebd6ab07aa8081b577a9ac0c9
```

It is the authenticated length-12,873 three-hole partial word followed by
`0x0200,0x287d`.  This note does not claim a length-12,873 or length-12,874
universal word.

## 2. Exact two-phase occurrence Hall quotient

Put \(z=0x8000\), and project a 16-bit word \(w\) to

\[
 a_i=\pi(w_i)=w_i\mathbin{\&}0x7fff.
\]

For each nonzero 15-bit mask \(m\), let

\[
 \mathcal I_m(a)=
 \{[r,s]:a_r\vee\cdots\vee a_s=m\},
 \qquad c_a(m)=|\mathcal I_m(a)|.
\]

There are two required 16-bit labels over this projection: \(m\) and
\(z\vee m\).  One physical interval in \(\mathcal I_m(a)\) has one top-bit
OR and therefore realizes at most one of these two labels.

### Theorem 2.1 (phase-occurrence Hall theorem)

For fixed projected trace \(a\), the occurrence-capacity matching has one
component \(K_{2,c_a(m)}\) for each nonzero \(m\).  Its exact Hall deficiency
is

\[
 \boxed{D(a)=\sum_{m=1}^{32767}\max\{0,2-c_a(m)\}.}
\tag{2.1}
\]

In particular, if \(D(a)>0\), no assignment of top bits to the fixed trace
can produce a universal 16-bit word.

#### Proof

The two left vertices in the \(m\)-component are the labels \(m\) and
\(z\vee m\); its right vertices are the physical interval occurrences in
\(\mathcal I_m(a)\).  Components for different projected masks are disjoint.
The maximum matching in one component has size
\(\min\{2,c_a(m)\}\), so its deficiency is
\(\max\{0,2-c_a(m)\}\).  Summing over the disjoint components gives (2.1).
Every literal word supplies such a matching by choosing one witness interval
for each label.  Thus positive deficiency is an exact no-go. \(\square\)

The converse is deliberately **not** asserted.  Even when every
\(c_a(m)\ge2\), the same top-bit variables occur in many intervals.  Shared
chronology is a further constraint.

## 3. Reconciliation of the portal ledgers

All positions below are zero based.  Starting from

```text
scratch/k16_12873_repaired_partial.word
SHA-256 0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6,
```

the exact comparison is:

| state | exact holes | deficient projected masks | \(D(a)\) |
|---|---:|---|---:|
| source | 3 | `10365,20065,20067` each once | 3 |
| seam portal | 10 | `10361,18033,20081,20215,26745` each zero | 10 |
| boundary portal | 8 | `10349,11373` zero; `19553,19555,19559,19687` once | 8 |
| P0 | 6 | `10365,19553,19555,19559,19687` each once | 5 |
| P1 | 6 | `10365,20065,20067` each once | 3 |

The two six-debt portals are literal:

```text
P0:
  p6440 0xa069 -> 0x2069
  p6441 0x806d -> 0x006d
  p12872 0xcc41 -> 0xce41
  holes {43129,43133,52321,52323,52327,52455}

P1:
  p6435 0x0600 -> 0x8600
  p6440 0xa069 -> 0x2069
  p6441 0x806d -> 0x006d
  holes {20065,20067,20081,20215,43129,43133}.
```

Thus P1 is the smaller projected compiler gate: it needs one additional
physical projected occurrence of each of

\[
                 10365,\quad20065,\quad20067.                 \tag{3.1}
\]

P0 needs five such occurrence units.  These lower bounds are sharp for their
fixed projections if arbitrary retagging is allowed: the source top trace
has exactly three holes on P1's projection, while the endpoint-only trace has
exactly five holes on P0's projection.

The source trace has 121 maximal top-bit runs, 61 high and 60 low.  Across
all nine minimum canonical-lift alignments, the byte artifact has 61
high-to-low changes, one low-to-high change, and 135 same-phase
substitutions.  This is the exact meaning of the net 60-portal phase braid.

### One-portal augmentation no-go

For P0 and P1, exhaust every one of the 61 original untagged-high portal
cells.  If one changed projection creates a new occurrence of a deficient
mask \(m\), its new nonzero value must be a submask of \(m\).  This leaves
735 candidate values for P0 and 495 for P1.

Recompute the exact projected occurrence vector after every such edit and
require every previously adequate projection to retain multiplicity at least
two.  The complete censuses are:

```text
P0: 44,796 non-noop pairs; 223 Hall-safe pairs; best deficiency gain 0.
P1: 30,144 non-noop pairs; 228 Hall-safe pairs; best deficiency gain 0.
```

Hence neither six-debt state has an improving one-portal projected-Hall move.
This is not a compound-edit no-go.

## 4. The length-12,874 ripple basin

The newer artifact is

```text
scratch/k16_ripple_insert12874_onehole.word
SHA-256 5ac147eca512b7e398c7217f1796836f454a304274c6e54fda7050fc9b4f66db.
```

Exact replay finds the sole hole

\[
                         10365=0x287d.                         \tag{4.1}
\]

Its projected trace has exactly one deficient mask, again `0x287d`, with
one and only one physical occurrence:

\[
                  \mathcal I_{10365}=\{[6439,6441]\}.          \tag{4.2}
\]

The current top phase makes this interval `0xa87d`, so its low partner is
missing.  Equation (2.1) gives \(D=1\).  Merely retagging the existing trace
cannot close the word.

Now clear the top bit at position 6440:

```text
p6440 0xa069 -> 0x2069.
```

The unique resource (4.2) becomes low, and exact replay leaves precisely

\[
                       \{43129,43133\}
                       =\{0xa879,0xa87d\}.                     \tag{4.3}
\]

This is a phase swap, not progress in the projected Hall quotient.

### Theorem 4.1 (64-portal local minimum)

In the two-hole state (4.3), allow one arbitrary projected value at any of
the 64 currently untagged tail cells.  A value capable of creating a second
`0x287d` occurrence must be one of its 255 nonzero submasks.  Among all
16,290 non-noop position/value pairs:

1. 806 create a second `0x287d` occurrence;
2. every one of those 806 makes at least one other projected mask have
   multiplicity below two;
3. the minimum collateral is one projection, attained by exactly 16 values,
   all at position 6440; and
4. every minimum edit moves the sole deficiency from `0x287d` to `0x2879`.

The exact collateral-size histogram is

```text
1:16, 2:287, 3:16, 4:112, 5:32, 6:8, 7:1,
8:72, 9:18, 10:42, 11:148, 12:24, 13:20, 14:8, 15:2.
```

After each of the 16 minimum transfers, a second arbitrary edit at another
one of the same tail portals, with any nonzero submask of `0x2879`, was
exhausted.  Among 127,696 non-noop second pairs, 6,528 restore the moved
`0x2879` occurrence count, but every one creates at least two other projected
deficits.  Thus no second pair closes projected Hall; the minimum second
collateral is two.  All 2,032 minimum-collateral moves occur at position 6438
and leave exactly the fixed pair `0x4879,0x6879`.  The sharp alternating
defect ripple in this fibre is therefore

\[
 \{0x287d\}\longrightarrow\{0x2879\}
 \longrightarrow\{0x4879,0x6879\}.                            \tag{4.4}
\]

#### Proof

Changing position \(p\) affects only intervals containing \(p\).  Every such
projected interval has label

\[
                         \ell\vee x\vee r,                     \tag{4.5}
\]

where \(\ell\) is a suffix-OR state to the left, \(r\) is a prefix-OR state
to the right, and \(x\) is the new projected value.  The audit enumerates all
distinct states with their exact interval multiplicities, subtracts the old
labels and adds the new labels in (4.5).  A new `0x287d` occurrence forces
\(x\subseteq0x287d\), so the 255-value domain is exhaustive.  The same
argument with `0x2879` makes the second-layer domain exhaustive.  The stated
counts follow by exact integer replay.  Positive projected-Hall deficiency
then invokes Theorem 2.1. \(\square\)

Scope is essential: positions outside the 64 tail portals, a nonminimal first
transfer, or a compound packet of larger support remain open.

## 5. What the two-cell completion teaches

For the old length-12,873 partial word, no one-cell insertion at any of its
12,874 gaps can install all three holes.  Every inserted value must lie in

\[
0x287d\cap0xce61\cap0xce63=0x0861,
\]

so only 15 nonzero values are possible.  The exact 193,110 gap/value census
has maximum coverage two and zero full candidates.

There is also a solver-free append obstruction.  All new witnesses after one
append are suffixes ending at the new cell, so their OR labels form an
inclusion chain.  The holes `0x287d` and `0xce61` are incomparable.  Thus two
appends are necessary for this fixed partial, and the verified append pair
`0x0200,0x287d` is optimal within the append-only class.

The useful balanced reduction is sharper.  Clearing the top bits at positions
6440 and 6441 and then appending `0x0661` produces a length-12,874 word whose
only holes are again `0xa879,0xa87d`.  The ripple basin reaches the same
two-label gate without that append.  Both therefore isolate the same task:

> create a second projected occurrence of `0x287d`, give the two occurrences
> opposite phases, and preserve multiplicity at least two for every other
> projected mask.

After this projected Hall gate is cleared, shared top-bit chronology and full
literal replay are still mandatory.

## 6. Reproducible artifacts

```text
scratch/audit_l_k16_six_debt_phase_portal_hall_20260730.py
  SHA 82c76ef53f7a727e945df714b7fdbbf8421dffb4a6d44e40729a9cae4bbb1f34
scratch/k16_six_debt_phase_portal_hall_20260730.audit.json
  SHA 3b12bf7243f4910b7b5d9f241d94b742145540995e5bd58e8af0ce6468d5504a
  payload e61ca9290b80f330a4a2c3e0ef57feb99d1eb52ab7b7c6bee4d5dcdba1a9e820

scratch/audit_l_k16_ripple_onehole_twohole_portal_hall_20260730.py
  SHA d1afe1c2d99045ee008e6b57c281d76c66cb73d783951b3fea83b60be39d34ec
scratch/k16_ripple_onehole_twohole_portal_hall_20260730.audit.json
  SHA b815bf54e6a3848ba50148657f6ff12209790e051665862f818c8ba9b7d537d0
  payload b29d547bed20d7ba152f4f2ab225d745bf19f996f3707f4c3bf9f91614bc1e46

scratch/audit_l_k16_partial_one_insert_append_gate_20260730.py
  SHA c71ff157a8b727686509096a9f61e3371e7c448d61c79ea6338a7c3dacc7decc
scratch/k16_partial_one_insert_append_gate_20260730.audit.json
  SHA 08e4adbccff354dc21115122d5a5285aa5791687b8e27a83fc0cb5be7c4e4013
  payload bb50036c7b8704596355edc070a5c10a68510df55025d7f23191c9ea9d301a17
```

All three audits are standard-library only, fail closed on source hashes and
exact ledgers, and use no solver.  Their conclusions are local to the named
byte artifacts and declared portal fibres.
