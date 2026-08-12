# DERF recursive-pattern referee: the canonical source-ear kernel and the limits of the finite chain

Date: 2026-07-31  
Status: independent literal replay of the chained strict witnesses at child
parameters `3,4,5`; one dimension-free source-ear theorem; exact finite
counterexamples to several stronger extrapolations.  No all-parameter DERF
selection theorem is claimed.

## 0. Verdict

The frozen file

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n5_20260731.witness.json
```

is an exact chained strict construction.  Its SHA-256 is
`1fd49d57277a6bd7357816b5861ba370d26b4b863a570e35202c9801a0585c20`.
An independent consumer reconstructs every child diamond, both punctured
side palettes, both physical side forests, the complete five-sector lift,
and the recorded ambient paths.  It also transports every case through a
coordinate reversal and a reversal of the child-component order and replays
the transported witness literally.

The strongest coordinate-free deterministic rule extracted from these
fixtures does **not** choose the common basis `Q` or its representatives.
It starts after one side forest has been chosen.  Every such side has a
canonical source-ear factorization, including an exact anchor-free defect
parameter.  This factorization also localizes all side residence defects:
every bad three-edge window is internal to the kernel except possibly the
unique prefix window at one deleted ear.

The finite chain does not support a stronger local recursion rule.  At the
last stage every immediate parent sector contains both deleted and retained
edges; both old and newest-collar coordinates are used on both shores; and
thirteen fresh strict residence windows occur outside the inherited child
rail.  A second exact strict fixture has three anchor-free components on
each shore at child parameter five.  Thus no-empty topology is a selected
state, not a consequence of strict direct incidence.

## 1. General source-ear theorem with anchor-free defect

Use the standard Catalan counts

\[
 N=\binom{2n}{n-1},\qquad P=\binom{2n}{n-2},\qquad
 C=\operatorname {Cat}_{n+1},\qquad K=\operatorname {Cat}_n,
 \qquad R=P-K.
\]

Let `S` be any role-safe, anchor-capped `P`-edge side forest on `N`
physical vertices, with the prescribed bank of `C` anchors.  Role safety
and acyclicity orient every nontrivial component as a directed path.  Let
`c_j` be the number of components containing `j` anchors and put

\[
                              a=c_0.                    \tag{1.1}
\]

The anchor cap gives `j<=2`.

### Theorem 1.1 (canonical source-ear kernel)

For every such side forest,

\[
       c_2=K+a,\qquad c_1=C-2K-2a.                    \tag{1.2}
\]

In each two-anchor directed path, delete the unique first arc leaving its
source anchor.  Call these deleted arcs the **source ears** and the remaining
forest the **kernel**.  Then:

1. there are exactly `K+a` source ears;
2. the kernel has exactly `R-a` edges;
3. the kernel has exactly `C` one-anchor directed paths and `a`
   anchor-free directed paths;
4. the source ears form a matching on `2(K+a)` distinct one-anchor kernel
   paths; and
5. after all anchors are contracted to one root, the kernel is a subdivided
   rooted star together with `a` detached paths.  In particular it has
   exactly `a+1` components and is a spanning tree exactly when `a=0`.

#### Proof

The side forest has

\[
              N-P=C-K
\]

components.  Counting components and anchors gives

\[
 c_0+c_1+c_2=C-K,\qquad c_1+2c_2=C.
\]

Substitution of `c_0=a` proves (1.2).  An anchor has physical degree at
most one, so the two anchors in a two-anchor path are its source and sink.
Deleting the first arc therefore splits that path into two one-anchor
paths.  Distinct original components give disjoint pairs, proving the ear
matching assertion.  The new component counts are `C` and `a`, and the
edge count is

\[
             P-(K+a)=R-a.
\]

Every one-anchor kernel component is a path attached to the contracted
root; every anchor-free component remains a detached path.  This proves
the last assertion.  `square`

The deletion rule uses only the directed side and its anchor marks.  It is
therefore equivariant under coordinate relabelling and path-component
reordering.  A lexicographically least physical edge is unnecessary and
would not be invariant.

### Corollary 1.2 (source-ear residence factorization)

Call a three-edge side window bad for coordinate `i` when its four vertex
bits are

```text
0 1 1 0.
```

Every bad window is either wholly contained in one kernel path or is the
prefix window of one source ear.  Each source ear supports at most one bad
prefix window.  Hence, if `B`, `B_ker`, and `B_ear` count these windows,

\[
                    B=B_{\rm ker}+B_{\rm ear},\qquad
                    B_{\rm ear}\le K+a.               \tag{1.3}
\]

#### Proof

The deleted ear is the first edge of its original path.  A three-edge
window meeting it must therefore be the first window.  Every other window
uses only retained kernel edges.  Finally, the first Johnson edge adds a
unique coordinate, so at most that coordinate can have pattern `0110` in
the prefix window.  `square`

This corollary is a localization theorem, not a repair theorem: a bad
kernel-internal window still requires an interior rethread.

## 2. Exact chained measurements

The independent replay gives the following source-ear data.  The residence
entry is `all = kernel + ear-prefix`.

| child `n` | shore | `a` | ears `K+a` | kernel edges `R-a` | contracted components | bad windows |
|---:|:---|---:|---:|---:|---:|:---|
| 3 | upper | 0 | 5 | 1 | 1 | `0=0+0` |
| 3 | lower | 0 | 5 | 1 | 1 | `0=0+0` |
| 4 | upper | 0 | 14 | 14 | 1 | `0=0+0` |
| 4 | lower | 1 | 15 | 13 | 2 | `0=0+0` |
| 5 | upper | 0 | 42 | 78 | 1 | `3=2+1` |
| 5 | lower | 2 | 44 | 76 | 3 | `8=4+4` |

Thus the observed upper shores lie on the exact rooted-tree face, while
the lower rooted-kernel defects are `0,1,2`.  The theorem explains those
numbers once the shores are supplied; it does not prove that the sequence
continues or remains bounded.

The comparison file

```text
scratch/catalan_direct_edgewise_side_lift_n3_n5_20260731.witness.json
```

has SHA-256
`0cef794e33d0996bbd7d73168568e9c2613e3c06f12499751a685ac69fe554b3`.
Its cases are exact strict lifts but are not a single recursive chain.  At
child parameter five its upper and lower defects are both `a=3`, so both
kernels have `45` ears, `75` edges, and four components after anchor
contraction.  Its side residence factorizations are

```text
upper: 0 = 0 kernel + 0 prefix,
lower: 5 = 2 kernel + 3 prefix.
```

This is an exact strict-incidence counterexample to treating no-empty as
automatic.

## 3. Which visible patterns are artefacts

### 3.1 Absolute coordinate labels and raw edge ids

The strict equations commute with every permutation of the old ground set.
They also commute with arbitrary reordering of child path components after
the induced edge-id remapping.  The audit applies coordinate reversal and
component-order reversal.  Every coordinate-free metric is unchanged, but
the symmetric differences between the old and transported raw `Q` id sets
are respectively

```text
n=3: 2,     n=4: 22,     n=5: 94,
```

and the absolute upper lift-coordinate histograms change in all three
rows.  Consequently raw `Q` ids, sorted-mask order, and absolute coordinate
numbers cannot be inputs to an isomorphism-invariant rule.

### 3.2 Immediate parent sectors do not select `Q`

At child parameter five, with the preceding collar marked, the exact
`Q/retained` counts are

| immediate parent sector | `Q` | retained |
|:---|---:|---:|
| upper `0` | 19 | 9 |
| child `c` | 37 | 19 |
| central `z` | 8 | 6 |
| lower `cz` | 18 | 10 |
| seam `0-z` | 21 | 21 |
| seam `z-cz` | 29 | 13 |

Every sector is mixed.  Thus a rule which deletes or retains whole inherited
sector types is already false on the chained witness.  Even the unlabelled
path feature `(path length, unoriented distance of the edge from an end)` is
mixed on `1/8`, `10/19`, and `32/59` feature classes at child parameters
`3,4,5`; path shape alone is insufficient.

Refining the previous side sectors by the coordinate-free source-ear
factorization still does not recover `Q`.  At the `n=4 -> 5` transition the
exact `Q/total` counts are

```text
copied child, parent Q       27/42
copied child, parent not-Q   10/14
upper source ears             9/14
upper source-ear kernel      10/14
lower source ears            10/15
lower source-ear kernel       8/13
punctured centre              8/14
upper seams                  21/42
lower seams                  29/42
```

All nine refined banks remain mixed.  These source-ear counts should not be
conflated with a lexicographically chosen ear representative: both delete
one edge per double-anchor path and satisfy Theorem 1.1, but their finite
ear/kernel membership can differ.  The theorem is invariant; a particular
representative bank is extra state.

### 3.3 Coordinate age does not select representatives

Both representative shores use old and newest-collar coordinates:

| child `n` | upper old/new | lower old/new |
|---:|:---|:---|
| 4 | `17/11` | `16/12` |
| 5 | `97/23` | `90/30` |

This does not rule out a richer ancestry-dependent rule, but it rules out
both `always old` and `always newest` prescriptions.

### 3.4 Facet slack is invariant evidence, not a selector

The minimum physical continuation degrees `(eta^-,eta^+)` are genuine
coordinate-isomorphism invariants.  The chained rows are

```text
n=3: (3,3),    n=4: (3,3),    n=5: (4,3),
```

and the three independent strict comparison rows are

```text
n=3: (3,3),    n=4: (5,5),    n=5: (5,6).
```

Thus `eta^pm>=3` survives all six audited finite cases.  It is still not a
proved propagation theorem, and it does not imply rooted topology: the
comparison `n=5` case has the larger slacks `(5,6)` while both shores have
anchor-free defect `a=3`.

## 4. The exact recursive residence statement, and its limit

The untouched `c` rail is a literal copy of every child path.  Therefore
all old-coordinate bit words, including every internal residence motif,
are inherited exactly.  The replay checks

```text
n=3 output total 17  = n=4 strict c-rail 17,
n=4 output total 44  = n=5 strict c-rail 44.
```

This is dimension-free and genuinely recursive.  The stronger guess that
the other three rails create no new strict defect is false: it holds at the
first displayed transition but fails at child parameter five, where the
new strict sectors contribute

```text
upper 0: 3,      central z: 2,      lower cz: 8,
```

for thirteen fresh windows.  The chain therefore preserves old residence
debt and can create new debt; the source-ear theorem only localizes the side
part of that debt.

## 5. Reproducible audit and scope

The independent standard-library consumer is

```text
scratch/audit_catalan_derf_recursive_pattern_referee_20260731.py
```

and writes

```text
scratch/catalan_derf_recursive_pattern_referee_20260731.audit.json
```

The audit JSON has canonical payload
`d9826468a634a61e5b23eec1a26b8a18c1ed35993d067045469122a35fb0548c`.
It does not import the witness producer or either earlier DERF audit.

What is proved uniformly is the source-ear factorization **conditional on
a chosen side forest** and the exact heredity of the untouched child rail.
No deterministic all-parameter choice of `Q`, no representative SDR, no
boundedness of `a`, and no residence repair or compiler theorem is claimed.
