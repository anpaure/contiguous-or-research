# K16 three-hole incumbent: exact portal exchange complex and a radius bound

**Date:** 2026-07-30  
**Lane:** D  
**Status:** exact scoped obstruction; no length-12,873 word is claimed

## 1. Frozen instance

Let (w=(w_0,ldots,w_{12872})) be

```text
scratch/k16_12873_repaired_partial.word
SHA-256 0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

For a nonzero 16-bit mask (T), put

\[
 c_w(T)=\#\{[a,b]:0\le a\le b<12873,
                 \bigvee_{i=a}^b w_i=T\}.
\]

Exact ending-OR replay gives

\[
 H_0=\{10365,52833,52835\}
     =\{\mathtt{0x287d},\mathtt{0xce61},\mathtt{0xce63}\},
\]

with (50,170) masks of multiplicity one and (8,185) of multiplicity
two.  Thus (w) is a three-hole incumbent, not a universal word.

## 2. The exact exchange object

For a consistent finite set (F) of atomic word edits, let (w^F) be the
literal edited word and define the exact macro-edge

\[
 L(F)=\{T:c_w(T)>0=c_{w^F}(T)\},\qquad
 G(F)=\{T:c_w(T)=0<c_{w^F}(T)\}.
\tag{2.1}
\]

The directed exchange hypergraph has all (65535) nonzero masks as vertices
and one directed hyperedge (L(F)\to G(F)) for each candidate macro (F).
Since (w) has precisely the holes (H_0), the macro is a successful
exchange exactly when

\[
 H_0\subseteq G(F)\quad\hbox{and}\quad L(F)=\varnothing.
\tag{2.2}
\]

This formulation handles substitutions and any explicitly defined
delete/reinsert shift uniformly: build the resulting literal word, compute
(2.1), and use the declared operation count as the edge cost.

Atomic signed columns are useful but are not automatically composable.  For
atomic edits indexed by a set (E), define

\[
 \kappa_J(T)=\sum_{I\subseteq J}(-1)^{|J|-|I|}c_{w^I}(T).
\tag{2.3}
\]

Boolean-lattice inversion gives the exact identity

\[
 c_{w^F}(T)=\sum_{J\subseteq F}\kappa_J(T).
\tag{2.4}
\]

Consequently a linear lost-to-gained circulation is exact only after proving
that every higher interaction (kappa_J), (|J|\ge2), vanishes, or after
installing those interaction columns.  The alternative exact implementation
is state dependent: after every selected edit, recompute (2.1) in the current
word.

### Correction to the proposed vertex compression

The vertex set cannot be restricted to the current multiplicity-one masks
plus (H_0).  A single edit may hit every witness of a mask whose current
multiplicity is two or three.  The portal below does so five times.  An exact
compressed vertex set must instead contain every mask whose complete provider
family can be hit by the candidate supports; retaining the literal
multiplicity vector is simpler and fail-closed.

## 3. The two-edit portal

Use zero-based incumbent positions and set

\[
 e_1:\quad w_{6436}=18033\longmapsto18017,
 \qquad
 e_2:\quad w_{6439}=10361\longmapsto10365.
\tag{3.1}
\]

In hexadecimal these are

```text
e1: p6436  0x4671 -> 0x4661   (remove 0x0010)
e2: p6439  0x2879 -> 0x287d   (add    0x0004)
```

Their zero/nonzero boundary columns are exactly

| edit | gained masks | lost masks, with old multiplicity |
|---|---|---|
| (e_1) | (52833:0\to2, 52835:0\to1) | (18033:2, 20081:2, 20215:1, 50801:2, 52849:2, 52983:1) |
| (e_2) | (10365:0\to1) | (10361:1, 26745:1, 43129:1, 59513:3) |

The ten loss masks are pairwise distinct.  Hence the portal installs every
member of (H_0) and leaves exactly

\[
 H_1=\{10361,18033,20081,20215,26745,43129,
        50801,52849,52983,59513\}.
\tag{3.2}
\]

The resulting literal word has SHA-256

```text
2c66e35b326616d54baa8937cb06966e21e8f59e7b9eae99be678c2ec6f42834
```

and exact replay gives (3\to10) holes.

### Provider ownership

All relevant witnesses lie in positions (6430,ldots,6440).  The lost
provider intervals are

```text
18033 : [6435,6436], [6436,6436]
20081 : [6433,6436], [6434,6436]
20215 : [6430,6436]
50801 : [6435,6437], [6436,6437]
52849 : [6433,6437], [6434,6437]
52983 : [6430,6437]

10361 : [6439,6439]
26745 : [6438,6439]
43129 : [6439,6440]
59513 : [6437,6439], [6437,6440], [6438,6440].
```

Thus (e_1) owns every displayed witness in the first group and (e_2)
owns every witness in the second.  In particular the multiplicity-two and
multiplicity-three losses are genuine exchange vertices.

The two signed columns happen to be exactly additive, not merely additive at
the hole indicator.  Every interval affected by both edits contains
positions 6437 and 6438, whose OR is (51321).  That middle OR already
contains the bit removed by (e_1), so (e_1) does not change an interval
spanning both edit positions.  Therefore

\[
 \kappa_{\{e_1,e_2\}}(T)=0\qquad(0\le T<2^{16}).
\tag{3.3}
\]

This proves that the two displayed columns form one proof-safe portal
macro.  It does not imply additivity for a third edit.

## 4. Exact substitution-radius bounds

### 4.1 The original incumbent has substitution radius at least two

Suppose one substitution at position (p), with replacement (r), covered
all three masks in (H_0).  Every new witness must contain (p), because an
interval avoiding (p) is unchanged.  Hence

\[
 r\subseteq\bigcap_{T\in H_0}T
   =2145=\mathtt{0x0861}.
\tag{4.1}
\]

There are only (15) nonzero submasks in (4.1).  Exhaustive exact
left-suffix/right-prefix replay of all (12873\cdot15=193095) candidates has
the following histogram by the number of original holes gained:

```text
0 gained : 192530
1 gained :    534
2 gained :     31
3 gained :      0
```

Thus no single substitution can complete the incumbent.  This is a global
one-substitution theorem, not a heuristic scan over replacement values.

### 4.2 No third substitution completes the fixed portal

Now start from the exact portal word.  If one further substitution with
replacement (r) covered all ten masks in (H_1), the same unchanged-
interval argument would force

\[
 r\subseteq\bigcap_{T\in H_1}T
   =113=\mathtt{0x0071}.
\tag{4.2}
\]

Again there are exactly (15) nonzero candidates for (r).  The complete
(12873\cdot15=193095) census gives

```text
number of H1 masks gained : candidate count
0 : 190982
1 :   1897
2 :    156
3 :     20
4 :     24
5 :      0
6 :     16
7,8,9,10 : 0
```

The maximum six gains occur only at positions (6434) or (6435), with

\[
 r\in\{16,17,48,49,80,81,112,113\}.
\]

Literal full replay leaves respectively twelve or eight holes in those
sixteen cases.  In particular:

> **Portal radius corollary.** No three-substitution sequence whose first two
> edits are (3.1) is universal.  Any final word retaining both portal values
> and differing from the incumbent only by substitutions has Hamming radius
> at least four.

This is the requested sound radius bound.  It is conditional on retaining
the named portal values and on measuring substitutions.  It is not a global
radius-three no-go for all possible first two edits.

## 5. Additional exact local obstructions

The solver-free three-window Hall audit proves that arbitrary replacement of
the central three positions (6437,6438,6439) cannot complete the incumbent:
fourteen residual targets have maximum matching twelve into the twenty-seven
window forms.  Across all (12871) three-cell windows, (7804) fail this
ordinary Hall relaxation and (5067) pass it; passing Hall is not a positive
certificate because the forms must still share literal cell bits.

Separately, the exact arbitrary-block model with portal values fixed proves
`INFEASIBLE` for centered widths 6, 8, 10, and 12.  Widths 14 and above have
not been closed: time-limited `UNKNOWN` results are not used as no-goes.

## 6. Deletion-shift scope

There is no byte-intrinsic canonical-lift deletion history for the incumbent.
The exact order-preserving alignment ledger has nine equally minimum
alignments, each with 197 substitutions and deletion choices

\[
 \{0,1,2\}\times\{6439,6440,6441\}\times\{12875\}.
\]

Accordingly, “shift one of the three original deletions” is not a well-defined
atomic move until an alignment is declared.  A proof-safe exchange catalogue
must do one of the following.

1. Branch over all nine authenticated alignments and define deletion shifts
   relative to each branch; or
2. use a byte-level operation, for example delete the current letter at
   position (a) and reinsert that same letter at a declared gap (b), then
   compute its exact macro-edge by (2.1).

The radius results in Section 4 do not cover such a shift.  This is the sharp
remaining qualification, rather than an implicit claim that a deletion shift
is equivalent to a substitution.

## 7. Reproducible inputs

The portal and all displayed witnesses are independently replayed by

```text
scratch/audit_k16_12873_partial_support_neighborhood_20260730.py
scratch/k16_12873_partial_support_neighborhood_20260730.audit.json
```

The source/provenance and complete multiplicity ledger are

```text
scratch/audit_k16_12873_repaired_partial_exact_edit_ledger_20260730.py
scratch/k16_12873_repaired_partial_exact_edit_ledger_20260730.audit.json
```

The central three-window Hall certificate is

```text
scratch/audit_k16_12873_partial_threewindow_hall_20260730.py
scratch/k16_12873_partial_threewindow_hall_20260730.audit.json
```

The complete all-submask radius census is

```text
scratch/audit_k16_trimmed_lift_exchange_portal_radius_20260730.py
  SHA-256 b8037d843dfc5bb0a1938660937a65118ac759c29387c7e0949b5ce24ecb32eb
scratch/k16_trimmed_lift_exchange_portal_radius_20260730.audit.json
  SHA-256 030ff257178546e8f8681d7afd181b7b9bd1adca24cd5cd953973fdfead21538
  stable payload c273f1315384d2576872ea5e1b290d9b9e70ddeec846cb4416e56f9c444a0ca7
```

It is intentionally separate from the earlier minimum-Hamming-per-window
audit: nonminimal submasks are necessary for a complete one-substitution
theorem.
