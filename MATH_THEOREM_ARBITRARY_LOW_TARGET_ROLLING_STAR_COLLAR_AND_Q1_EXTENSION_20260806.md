# Every low target has an explicit rolling-star collar, and one collar extends in the q1 factor

**Date:** 2026-08-06  
**Method:** a fixed-background Johnson window path and the small protected
middle-levels factor theorem; no computation or search  
**Status:** unconditional local source/owner theorem and one-packet q1
extension.  It closes literal nested-path consistency for an arbitrary
rank-at-most-`d` target without PBBS run geometry.  Simultaneous extension
of the subexponential packet bank with residence and upper guards remains
open.

## 1. Parameters

Let the ground set have size `2r-1`, let owners have rank `r`, and let the
source deadline be `d`.  Assume

\[
 4d+4\le r.
\tag{1.1}
\]

Let

\[
 S=\{s_1,\ldots,s_A\},
 \qquad 1\le A\le d,
\tag{1.2}
\]

where the displayed order is arbitrary.  No cyclic-run condition is
imposed.

Choose a background set `B` of size

\[
 |B|=r-d-1
\tag{1.3}
\]

disjoint from `S`.  Choose pairwise distinct marker coordinates

\[
 z_{-d},z_{-d+1},\ldots,z_{A+d+1}
\tag{1.4}
\]

outside `B`, with

\[
 z_p=s_p
 \qquad(1\le p\le A).
\tag{1.5}
\]

The number of coordinates requested is

\[
 |B|+(A+2d+2)
 =r+A+d+1
 \le r+2d+1
 \le2r-1,
\tag{1.6}
\]

so the choice is possible under `(1.1)`.

## 2. The rolling-star source and owner rows

For `-d<=p<=A+d+1`, put

\[
 P_p=B\cup\{z_p\}.
\tag{2.1}
\]

For `-d<=i<=A+1`, put

\[
 T_i=\bigcup_{p=i}^{i+d}P_p
     =B\cup\{z_i,z_{i+1},\ldots,z_{i+d}\}.
\tag{2.2}
\]

Every `T_i` has rank

\[
 (r-d-1)+(d+1)=r.
\]

Moreover

\[
 T_i\cap T_{i+1}
 =B\cup\{z_{i+1},\ldots,z_{i+d}\}
\tag{2.3}
\]

has rank `r-1`, while

\[
 T_i\cup T_{i+1}
 =B\cup\{z_i,\ldots,z_{i+d+1}\}
\tag{2.4}
\]

has rank `r+1`.  Thus `(T_i)` is a simple Johnson path.  Its immediate
lower and upper colours are pairwise distinct because all marker windows
are distinct.

### Theorem 2.1 (exact local maximal antecedent)

For every `0<=p<=A+1`,

\[
 \boxed{
 \bigcap_{h=0}^dT_{p-h}=P_p=B\cup\{z_p\}.}
\tag{2.5}
\]

Consequently, for every target position `1<=p<=A`, the mandatory erosion
core is exactly

\[
 \boxed{
 F_p=(P_p-P_{p-1})\cup(P_p-P_{p+1})=\{s_p\}.}
\tag{2.6}
\]

#### Proof

The set `B` occurs in every displayed owner.  The marker windows in
`T_(p-d),...,T_p` are

\[
 \{z_{p-d},\ldots,z_p\},
 \ldots,
 \{z_p,\ldots,z_{p+d}\}.
\]

Their unique common marker is `z_p`, proving `(2.5)`.  Adjacent envelopes
have the same background and different markers, so `(2.6)` follows from
`z_p=s_p`.  \(\square\)

## 3. Literal arbitrary-target ticket

Define the source letters on the target block by

\[
 A_p=\{s_p\}
 \qquad(1\le p\le A),
\tag{3.1}
\]

and retain the maximal letters `P_p` at all other positions of a resident
completion.

### Corollary 3.1 (rolling-star low ticket)

In every spanning owner completion which retains the displayed collar and
has positive coordinate runs of length at least `d+1`, the block `(3.1)`
is a valid depth-`d` source modification and

\[
 \bigcup_{p=1}^AA_p=S.
\tag{3.2}
\]

It uses exactly `A<=d` consecutive source positions.

#### Proof

The displayed target block has length at most `d`.  Equations `(2.5)` and
`(2.6)` give

\[
 F_p\subseteq A_p\subseteq P_p
\]

at every changed position.  The mandatory-core short-gap theorem therefore
preserves the complete owner row.  Equation `(3.2)` is literal.  \(\square\)

This construction ignores the cyclic run decomposition of `S`.  It has no
native hook parity, terminal-bank, singleton-payload, or nested-context
obstruction.  All target coordinates are simply the successive markers of
one rolling Johnson collar.

## 4. One-packet q1 extension is unconditional

The owner path in Section 2 has

\[
 A+d+2
\]

vertices and `A+d+1` Johnson edges.  Lift each Johnson edge through its
rank-`r-1` intersection to the middle-levels incidence graph.  The
resulting protected incidence path has

\[
 2(A+d+1)\le4d+2\le r-2
\tag{4.1}
\]

incidence edges and maximum degree two.

### Theorem 4.1 (single rolling collar extends to a q1 two-factor)

The protected rolling-star incidence path extends to a spanning
two-factor of the middle-levels incidence graph.

#### Proof

Apply the small protected-factor theorem to the path.  Its edge count and
maximum degree satisfy `(4.1)`.  \(\square\)

Thus there is no local owner or immediate-lower-palette obstruction to an
arbitrary low target.  The immediate-upper colours inside the protected
path are also simple by `(2.4)`, although an arbitrary two-factor
completion is not asserted to be globally upper-surjective.

## 5. Exact boundary of the result

Theorem 4.1 concerns one packet.  The complete low bank contains

\[
 L_d=\sum_{s=1}^d\binom{2r-1}s=2^{o(r)}
\]

packets, with total protected size `2^{o(r)}`.  This is negligible against
the middle width `W=2^{Theta(r)}`, but the small protected-factor theorem
has a linear-in-`r` edge hypothesis and cannot be applied to their union.

For a partial incidence factor `H`, exact extension is a bipartite
`b`-matching problem with residual demand

\[
 b(v)=2-d_H(v).
\]

Its proof-safe all-cut form is

\[
 \boxed{
 \sum_{x\in X}b(x)
 \le
 \sum_{y\in N(X)}b(y)
 \qquad\text{for every left-shore }X.}
\tag{5.1}
\]

Pairwise packet disjointness and the scalar estimate `|H|=o(W)` do not by
themselves imply `(5.1)`.  A cut-sparse packet selection or a robust
protected-factor theorem is still required.

Even after q1 extension, the spanning completion must additionally retain:

1. positive and zero-gap residence outside every protected collar;
2. the complete immediate and arbitrary-width upper palettes;
3. the component/topology interface; and
4. the terminal common-cap state.

## 6. Consequence for the nested-C6 programme

At the literal source/owner level, nested C6 exposure is not necessary to
express a low target: the rolling-star collar already realizes every
target in `|S|` cells.  Clean C6s remain a possible mechanism for embedding
and reconnecting these collars inside a PBBS-based global factor, but the
true remaining row is now the simultaneous protected-factor/upper/residence
extension of a subexponential rolling-collar bank.

This is strictly sharper than the former parity-and-singleton source
language gate.  Those obstructions belong to untouched native hook
components, not to the general resident Johnson source geometry.
