# Common-core compression and a disjoint witness reservoir for the hinge-ring upper damage

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical construction on the odd
Middle-Levels shore.  It gives a vertex- and immediate-lower-colour-disjoint
Johnson path witnessing every proper target in the complete possible
upper-damage family of the cyclic common-history hinge ring, using
`O(m 2^m)=o(W)` incidence edges.  In the full-size specialization `c=m`,
the ring hinges are the first edges of the top witness paths and the cyclic
rethread preserves their complete prefix-union deck at every width; every
private noninterval witness is untouched.  It does **not** prove that this
joint protected bank extends to a spanning two-factor; the weighted
protected Ore--Ryser cuts remain required.

## 0. The common-core damage family

Assume `m>=4` and `3<=c<=m`.  Work on a ground set of size `2m-1`, with middle-owner rank
`m`, and write

\[
 W={2m-1\choose m}
\]

for the size of either Middle-Levels shore.  In the
cyclic common-history hinge ring put

\[
 K=B\cup\{b\},
 \qquad |K|=m-1,
 \qquad E=[2m-1]\setminus K,
 \qquad |E|=m.
\tag{0.1}
\]

The seam bases are

\[
 U_i=K\cup\{a_{i-1},a_i\},
\tag{0.2}
\]

where the distinguished labels `a_0,...,a_(c-1)` are distinct members of
`E` and form a cyclic order.
Let `mathcal D` be the union of their upper cones, with the full-ground
target removed.

### Lemma 0.1 (single common-core compression)

One has

\[
 \boxed{
 \mathcal D=
 \{K\cup T:\varnothing\ne T\subsetneq E,
   \ \{a_{i-1},a_i\}\subseteq T\text{ for some }i\}.}
\tag{0.3}
\]

In particular every member has a unique external trace `T=Z\setminus K`.

#### Proof

The containment `U_i subseteq Z` is equivalent to `K subseteq Z` and
`{a_(i-1),a_i} subseteq Z\setminus K`.  Removing the full-ground target is
exactly `T ne E`. \(\square\)

If desired, the number of possible targets is

\[
 2^{m-c}\bigl(2^c-I(C_c)\bigr)-1,
\tag{0.4}
\]

where `I(C_c)` is the number of independent vertex sets of the `c`-cycle;
the final `-1` removes the full external set (which is non-independent).
The exact count is not used below.

## 1. A top-rank geodesic bank

Fix cyclic orders

\[
 E=(e_0,e_1,\ldots,e_{m-1}),
 \qquad
 K=(k_1,k_2,\ldots,k_{m-1}).
\tag{1.1}
\]

For `j in Z/mZ` and `1<=ell<=m-1`, define the cyclic external interval

\[
 T_{j,\ell}=\{e_{j+1},e_{j+2},\ldots,e_{j+\ell}\}
\tag{1.2}
\]

and the rank-`m` owner

\[
 O_{j,\ell}=
 \bigl(K\setminus\{k_1,\ldots,k_{\ell-1}\}\bigr)
 \cup T_{j,\ell}.
\tag{1.3}
\]

For fixed `j`, let

\[
 \mathcal P_j=(O_{j,1},O_{j,2},\ldots,O_{j,m-1}).
\tag{1.4}
\]

### Theorem 1.1

The paths `mathcal P_j` are pairwise owner-disjoint Johnson paths, and both
their immediate lower and immediate upper colours are distinct.  Moreover, for every
`1<=ell<=m-1`, the prefix of `mathcal P_j` ending at `O_(j,ell)` has union

\[
 \boxed{K\cup T_{j,\ell}.}
\tag{1.5}
\]

Consequently the bank witnesses every target whose external trace is a
nonempty proper cyclic interval of `E`; in particular `mathcal P_j`
witnesses the rank-`2m-2` target `K\cup(E\setminus\{e_j\})`.

#### Proof

Every owner in (1.3) has size

\[
 (m-1)-(\ell-1)+\ell=m.
\]

Two consecutive owners differ by deleting `k_ell` and inserting
`e_(j+ell+1)`, so they are Johnson adjacent.  Their intersection is

\[
 I_{j,\ell}=
 \bigl(K\setminus\{k_1,\ldots,k_\ell\}\bigr)
 \cup T_{j,\ell},
\tag{1.6}
\]

of rank `m-1`.

For a fixed length `ell<m`, the cyclic intervals `T_(j,ell)` are distinct;
different lengths have different cardinalities.  Hence every owner is
distinguished by its external trace, and the same is true of every lower
colour (1.6).  The upper colour on the same edge has external trace
`T_(j,ell+1)`, again unique, so the upper palette is simple as well.
Finally `O_(j,1)=K\cup{e_(j+1)}` contains all of `K`, while
the external traces in the first `ell` owners have union `T_(j,ell)`.
This proves (1.5). \(\square\)

## 2. Private-trace paths for every remaining target

Let `mathcal I` denote the family of nonempty proper cyclic intervals of
`E`.  Fix any target

\[
 Z=K\cup T\in\mathcal D,
 \qquad T\notin\mathcal I.
\tag{2.1}
\]

Put

\[
 q=|T|,
 \qquad p=q-1,
 \qquad n=|K|=m-1.
\tag{2.2}
\]

Because `T` contains a seam pair, `q>=2`.  Every co-singleton of `E` is a
cyclic interval, so `T notin mathcal I` also gives `q<=m-2`; hence

\[
                         1\le p\le n-2.
\tag{2.3}
\]

If `q=2`, choose two distinct coordinates `u_T,v_T in K` and put

\[
 V_{T,0}=(K\setminus\{u_T\})\cup T,
 \qquad
 V_{T,1}=(K\setminus\{v_T\})\cup T.
\tag{2.4}
\]

In this case take the one-edge path

\[
                         \mathcal Q_T=(V_{T,0},V_{T,1}).
\tag{2.5}
\]

Now assume `q>=3`.  Read the order on `K` cyclically and put

\[
 D_{T,j}=\{k_j,k_{j+1},\ldots,k_{j+p-1}\}
 \qquad(j\in\mathbb Z/n\mathbb Z),
\tag{2.6}
\]

with indices modulo `n`.  Define

\[
 V_{T,j}=(K\setminus D_{T,j})\cup T
 \qquad(0\le j<n)
\tag{2.7}
\]

and take the linear path

\[
 \mathcal Q_T=(V_{T,0},V_{T,1},\ldots,V_{T,n-1}).
\tag{2.8}
\]

### Theorem 2.1

The family `(mathcal Q_T)_(K union T in mathcal D, T notin mathcal I)` is a
pairwise owner-disjoint family of Johnson paths, disjoint from every path
in Section 1.  All immediate lower colours in the combined bank are
distinct, and

\[
                         \bigcup_{V\in\mathcal Q_T}V=K\cup T.
\tag{2.9}
\]

#### Proof

For `q=2`, both owners in (2.4) have rank `m`, are Johnson
adjacent, and have union `K union T`.  Their unique lower colour is

\[
                  (K\setminus\{u_T,v_T\})\cup T.
\tag{2.10}
\]

Assume now `q>=3`.  Every `V_(T,j)` has size

\[
 n-p+q=(m-1)-(q-1)+q=m.
\]

Successive cyclic windows `D_(T,j),D_(T,j+1)` differ by one element, so
the corresponding owners are Johnson adjacent.  Their lower intersection
is

\[
 J_{T,j}=
 \bigl(K\setminus(D_{T,j}\cup D_{T,j+1})\bigr)\cup T.
\tag{2.11}
\]

The union of the two deletion windows is a cyclic interval of size `p+1`.
Since `p+1<=n-1`, these unions, and hence the lower colours `J_(T,j)`, are
distinct along the path.

The `n` cyclic `p`-windows themselves are distinct because `1<=p<n`;
hence the owners `V_(T,j)` are distinct.  Likewise the consecutive-window
intersections are the distinct cyclic `(p-1)`-windows (when `p>=2`), so
the immediate upper colours are distinct along the path.

Every owner and every lower colour in `mathcal Q_T` has external trace
exactly `T`.  Thus different targets give disjoint vertices and lower
colours.  Since `T notin mathcal I`, they are also disjoint from the bank in
Section 1, whose external traces lie in `mathcal I`.

The immediate upper colour on the same edge is obtained by deleting the
cyclic intersection `D_(T,j) cap D_(T,j+1)`, of size `p-1`.  For `q=2`
there is only one upper colour, namely
`K union T`.  External traces distinguish all lower and upper colours
belonging to different target paths and separate them from the cyclic-
interval top bank.

Finally `p<n`, so the intersection of all `n` cyclic `p`-windows is empty.
Equivalently, every coordinate of `K` survives in at least one owner
`V_(T,j)`.  Every owner contains all of `T`, proving (2.9). \(\square\)

## 3. Complete reservoir and size

Let `P_D` be the Middle-Levels incidence graph obtained by inserting the
rank-`m-1` intersection vertex between every consecutive owner pair in all
paths `mathcal P_j` and `mathcal Q_T`.

### Corollary 3.1

The bank `P_D` has maximum degree at most two, no repeated owner, no
repeated immediate-lower or immediate-upper colour, and contains a literal
contiguous Johnson witness for every target in `mathcal D`.  Furthermore

\[
 |E(P_D)|
 \le 2(m-2)\bigl(m+|\mathcal D|\bigr)
 <2(m-2)(m+2^m)
 =o\!\left({2m-1\choose m}\right).
\tag{3.1}
\]

#### Proof

Sections 1 and 2 partition the target traces into cyclic intervals and
nonintervals and prove all disjointness statements.  Every long owner path
has `m-1` owners, hence `m-2` Johnson adjacencies and `2(m-2)` incidence
edges; the `q=2` paths are shorter.  There are `m` top paths and at most
`|mathcal D|` private paths.
Finally `m2^m=o(4^m/\sqrt m)` and the central binomial estimate gives the
last assertion. \(\square\)

The bound deliberately counts one private path for every damage target,
even though the top paths already witness many of them; it is therefore
not optimized.

## 4. Full-size ring coinstantiation and all-width upper safety

Now specialize the common-history ring to

\[
                         c=m,
\tag{4.1}
\]

so its external labels are all of `E`.  This is allowed whenever the common
history partitions `B` into `d` nonempty letters, equivalently
`d<=|B|=m-2`.

Orient the cyclic order so that the top path indexed by `i` has external
prefixes

\[
 T_{i,\ell}=\{a_i,a_{i-1},\ldots,a_{i-\ell+1}\},
\qquad1\le\ell\le m-1,
\tag{4.2}
\]

and choose the first coordinate in the order on `K` to be `b`.  Then

\[
 O_{i,1}=K\cup\{a_i\}=L_i,
\tag{4.3}
\]

while

\[
 O_{i,2}=(K\setminus\{b\})\cup\{a_i,a_{i-1}\}
        =B\cup\{a_i,a_{i-1}\}=R_i.
\tag{4.4}
\]

Their lower intersection is

\[
 O_{i,1}\cap O_{i,2}=B\cup\{a_i\}=I_i.
\tag{4.5}
\]

Thus every common-history ring hinge `L_i-I_i-R_i` is literally the first
Johnson adjacency of one top witness path.  No separate hinge owner or
lower-colour occurrence is required.  At incidence level, if

\[
 P_c=\{I_iL_i,I_iR_i:0\le i<m\},
\tag{4.6}
\]

then `P_c subseteq P_D`; indeed these are exactly the two incidence edges
subdividing the first adjacency of each top path.  Hence the joint
protected bank is setwise just `P_D`, and neither the hinge edges nor their
endpoints are counted twice.

### Theorem 4.1 (complete prefix-deck transport)

Perform the cyclic ring rethread

\[
                         L_iR_i\longmapsto L_iR_{i+1}.
\tag{4.7}
\]

Attach after `R_(i+1)` the old suffix

\[
 O_{i+1,3},O_{i+1,4},\ldots,O_{i+1,m-1}.
\]

For every `2<=ell<=m-1`, the new prefix

\[
 L_i,O_{i+1,2},O_{i+1,3},\ldots,O_{i+1,\ell}
\tag{4.8}
\]

has the same union as the old prefix

\[
 O_{i+1,1},O_{i+1,2},\ldots,O_{i+1,\ell},
\tag{4.9}
\]

namely

\[
                         K\cup T_{i+1,\ell}.
\tag{4.10}
\]

Consequently the rethread preserves, by cyclic permutation, one literal
contiguous witness for every damage target whose external trace is a
cyclic interval.  Every remaining damage target has its witness in a
private path `mathcal Q_T`, which contains no ring hinge and is unchanged.
Therefore every target in `mathcal D` survives the rethread.

#### Proof

The owner identities (4.3)--(4.5) are immediate from `K=B union {b}` and
the definitions.  In (4.7), the first two owners have union

\[
 (K\cup\{a_i\})\cup
 ((K\setminus\{b\})\cup\{a_{i+1},a_i\})
 =K\cup\{a_{i+1},a_i\}.
\]

Every later owner is identical to the corresponding owner in (4.9), so
both prefixes have union `K union T_(i+1,ell)`.  This proves (4.10).
The length-one prefixes are the owners `L_i` themselves; their target
multiset is unchanged because the rethread merely permutes which suffix
follows each `L_i`.  Thus the complete prefix deck, including width one,
is preserved.

The external trace of a private-path owner or lower colour is a
noninterval `T`, whereas every ring owner/colour used in (4.3)--(4.5) has
an external singleton or cyclic adjacent pair.  Hence no private path edge
is changed.  Sections 1--2 exhaust `mathcal D`. \(\square\)

### Corollary 4.2 (arbitrary-width upper gate removed after planting)

Suppose an upper-complete resident owner chronology contains `P_D` with
the displayed path occurrences, and regards its first top-path
adjacencies as the full-size ring hinges.  Then the cyclic common-history
rethread remains upper complete at **every** interval width.

#### Proof

By the hinge-ring damage-cone theorem, a possibly lost old upper target
lies in `mathcal D`.  Theorem 4.1 retains or redelivers every member of
`mathcal D`.  Every target outside `mathcal D` retains its old witness.
\(\square\)

Thus arbitrary-width upper safety no longer requires an abstract rainbow
witness selector in this specialization.  It is carried by an explicit
literal reservoir whose affected part is covariant under the same cyclic
head permutation.

## 5. Exact remaining gate

This theorem closes the **local literal witness-supply** row for the localized
upper damage: paths exist simultaneously, with no owner or immediate-lower
collision, use a vanishing fraction of the Middle-Levels vertices, and in
the full-size ring specialization survive the actual cyclic rethread.

It does not close the **factor-extension** row.  A maximum-degree-two
`o(W)` protected bank can violate a singleton residual Ore--Ryser cut.
For the present reservoir one must still choose the cyclic orders, path
cuts, and joint placement with the hinge bank so that, for every
`A subseteq mathcal L`,

\[
 m\bigl(q_1^{P_D}(A)+q_{\ge2}^{P_D}(A)\bigr)
 \le (m-2)n_1(A)+2b_{\ge2}(A),
\tag{5.1}
\]

using the notation of
`MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md`.
Component distribution, residence outside the protected paths, and the
common cap remain additional rows.

In particular, the setwise inclusion `P_c subseteq P_D` removes a local
collision/double-counting issue only.  It does not show that `P_D` has any
spanning two-factor completion, nor that its `m` distinguished hinge
adjacencies lie on distinct components of one.
