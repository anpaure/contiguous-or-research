# Two-hole packet q1 intersections: one top obstruction and an exact triple-overlap census

## Status

For the all-parity one-step two-hole packet, normalized pair codegrees hide
one genuine concentration: two owner-disjoint packets with the same top can
share all of their immediate-upper resources.  This note classifies that
obstruction exactly.

After imposing the very cheap rule "at most one selected packet per top",
two owner-disjoint packets share at most two immediate-lower roots and at
most one immediate-upper target.  Sharing two lower roots forces sharing
the upper target as well and has a rigid five-vertex path form.  The number
of such triple-overlap partners of a fixed packet is computed exactly and
is only `O(r^(-7/2))` of one resource degree at triangular depth.

This is a proof-safe quasi-linearity theorem, not a cover-down theorem.
Single-resource stars can still be large, so expansion does not follow from
the intersection classification alone.

## 1. Packet notation

Put

\[
 n=2r-1,\qquad D=d+1,\qquad L=D+2,\qquad c=r-D,           \tag{1.1}
\]

and assume `L>=5`.  A packet `P=(H,K,C)` consists of

\[
 K\subset H\subset[n],\qquad |K|=c,\quad |H|=r+2,        \tag{1.2}
\]

and a Hamilton cycle `C` on the private set `F=H-K`, of size `L`.
Its three q1-relevant rows are

\[
 \begin{aligned}
 \mathcal O(P)&=\{H-e:e\in E(C)\},\\
 \mathcal Q(P)&=\{H-V(R):R\text{ is a two-edge path of }C\},\\
 \mathcal U(P)&=\{H-f:f\in F\}.
 \end{aligned}                                             \tag{1.3}
\]

They are respectively the rank-`r` owners, rank-`r-1` lower roots, and
rank-`r+1` upper targets.  Throughout Sections 2--4, packets `P,P'` are
**owner-disjoint**:

\[
                         \mathcal O(P)\cap\mathcal O(P')
                           =\varnothing.                    \tag{1.4}
\]

## 2. Upper intersections

### Theorem 2.1 (the unique large upper intersection)

Let `P=(H,K,C)` and `P'=(H',K',C')` satisfy (1.4).

1. If `H=H'`, then

   \[
       |\mathcal U(P)\cap\mathcal U(P')|=|F\cap F'|,       \tag{2.1}
   \]

   which can be as large as `L`.
2. If `|H cap H'|=r+1`, then the upper intersection has size at most one.
   Writing

   \[
       H=J\mathbin{\dot\cup}\{a\},\qquad
       H'=J\mathbin{\dot\cup}\{b\},                      \tag{2.2}
   \]

   the common upper is `J`; it occurs exactly when `a in F` and `b in F'`.
   Under (1.4), this additionally forces

   \[
                         N_C(a)\cap N_{C'}(b)=\varnothing.  \tag{2.3}
   \]
3. If `|H cap H'|<=r`, the upper intersection is empty.

#### Proof

A common upper `U` has the form

\[
                         H=U\cup\{f\},\qquad
                         H'=U\cup\{f'\}.                   \tag{2.4}
\]

If the tops agree, then `f=f'`, and (2.1) follows.  If they differ,
(2.4) forces `U=H cap H'`, proving the size assertions and the criterion
in item 2.

In the notation (2.2), an owner can lie in both packets only in the form

\[
                         J-\{x\}=H-\{a,x\}=H'-\{b,x\}.     \tag{2.5}
\]

Such an owner occurs exactly when `ax in E(C)` and `bx in E(C')`.
Condition (1.4) is therefore exactly (2.3).  \(\square\)

The first row is a real obstruction.  Even with no common owner, two
edge-disjoint Hamilton cycles on the same private set may have identical
upper inventories.

## 3. Lower-root intersections

### Theorem 3.1 (complete lower-intersection bound)

For owner-disjoint packets with `L>=5`,

\[
                         |\mathcal Q(P)\cap\mathcal Q(P')|
                              \le2.                         \tag{3.1}
\]

More precisely:

1. if `H=H'`, the intersection is empty;
2. if `|H cap H'|=r+1`, it has size at most two;
3. if `|H cap H'|=r` or `r-1`, it has size at most one; and
4. if `|H cap H'|<r-1`, it is empty.

Two common lower roots are possible only in item 2.  In the notation
(2.2), write the two directed length-two walks away from `a` in `C` as

\[
                 a-x_+-y_+,qquad a-x_--y_-.                \tag{3.2}
\]

Then equality in (3.1) holds exactly when `C'` contains the five-vertex
path

\[
                         x_+-y_+-b-y_--x_-                 \tag{3.3}
\]

up to reversal.  The two common roots are

\[
                         (H\cap H')-\{x_+,y_+\},\qquad
                         (H\cap H')-\{x_-,y_-\}.            \tag{3.4}
\]

#### Proof

A common lower root `Q` has rank `r-1` and

\[
                         H=Q\mathbin{\dot\cup}A,\qquad
                         H'=Q\mathbin{\dot\cup}B,          \tag{3.5}
\]

where `A` and `B` are vertex sets of two-edge paths in `C` and `C'`.
This immediately gives item 4 and the uniqueness in the `r-1` intersection
case.

If `H=H'`, then `A=B`.  Two paths on the same three vertices share at
least one edge.  The corresponding owner `H-e` lies in both packets,
contrary to (1.4).  This proves item 1.

Suppose `|H cap H'|=r+1` and use (2.2).  Then every common root is

\[
                         Q=J-\{x,y\},                       \tag{3.6}
\]

with path vertex sets `{a,x,y}` and `{b,x,y}`.  The owners incident with a
root are obtained by adjoining the two path endpoints to `Q`.  To avoid a
common owner, `a` and `b` must both be path endpoints, and the common
endpoint chosen on one path must be the common *middle* label on the other.
Thus the paths have the opposed form

\[
                         a-x-y,qquad b-y-x.                 \tag{3.7}
\]

There are only the two directed length-two walks away from `a`, proving
the bound two.  Taking both gives exactly (3.2)--(3.4), and the converse is
immediate.

Finally suppose `|H cap H'|=r`.  Write

\[
 H=J\mathbin{\dot\cup}A_0,\qquad
 H'=J\mathbin{\dot\cup}B_0,qquad |A_0|=|B_0|=2.          \tag{3.8}
\]

A common root is `J-{x}` and requires both `A_0+{x}` and `B_0+{x}` to be
two-edge paths.  A fixed pair belongs to at most two three-vertex intervals
of a cycle.  If there are two for `A_0`, then `A_0` is a cycle edge and
the two possible `x`'s are endpoints in their respective paths.  Avoiding
the common owner `J` forces both `x`'s to be middle vertices between the
two labels of `B_0`.  In a cycle of length at least five, two fixed vertices
have at most one common neighbour.  Hence at most one common root survives.
This proves item 3 and the theorem.  \(\square\)

### Corollary 3.2 (triple q1 overlap is rigid)

If owner-disjoint packets share two lower roots, then they also share the
unique upper `J=H cap H'`.  Their total common q1 inventory is exactly the
three resources consisting of (3.4) and `J`.

Indeed (3.2)--(3.3) give

\[
 N_C(a)=\{x_+,x_-\},\qquad N_{C'}(b)=\{y_+,y_-\},
\]

and the four labels are distinct.  Thus (2.3) holds, while item 2 of
Theorem 2.1 supplies the common upper.

## 4. Exact census of triple-overlap partners

### Theorem 4.1

Fix one packet `P`.  The number of owner-disjoint packets `P'` sharing two
lower roots (and hence one upper) with `P` is exactly

\[
 \boxed{
 N_3=L(r-3)\binom{r-3}{L-5}(L-5)! .}                       \tag{4.1}
\]

If

\[
             D_0=\binom{r-1}{2}\binom r{L-2}(L-2)!        \tag{4.2}
\]

is the packet degree of one owner or one lower root, then

\[
 \boxed{
 {N_3\over D_0}
   ={2L(r-3)\over r(r-1)^2(r-2)^2}
   =O\!\left({L\over r^4}\right).}                         \tag{4.3}
\]

At triangular depth this is `O(r^(-7/2))`.

#### Proof

Choose the exclusive label `a in F` in `L` ways and the new top label
`b outside H` in `r-3` ways.  The four neighbours in (3.2), together with
`b`, must belong to `F'`.  Choose its other `L-5` private labels from the
remaining `r-3` elements of `H'`, giving the binomial factor in (4.1).

The cycle `C'` must contain the fixed undirected five-vertex path (3.3).
Contracting it to one object shows that the number of unoriented Hamilton
cycles containing it is `(L-5)!`.  The neighbour sets of `a` and `b` are
disjoint, so the resulting packet is owner-disjoint.  Theorem 3.1 says
there are no other double-root configurations, proving (4.1).

Substitute `D=L-2` into (4.2), cancel factorials, and obtain (4.3).
\(\square\)

## 5. Top simplicity is fractionally cheap

Add the packet top `H` itself as a capacity-one resource.  Under uniform
packet weight `1/D_0`, owner and lower-root loads are one.  The total packet
weight is `W/L`, while the number of possible tops is

\[
 \binom{2r-1}{r+2}
   ={(r-1)(r-2)\over(r+1)(r+2)}W.                          \tag{5.1}
\]

By symmetry, the load of one top is therefore

\[
 \boxed{
 \rho_H={ (r+1)(r+2)\over L(r-1)(r-2)}=O(L^{-1}).}         \tag{5.2}
\]

Thus requiring distinct tops has a factor-`Theta(L)` fractional capacity
margin.  Once this rule is imposed, Theorems 2.1 and 3.1 give

\[
 \begin{aligned}
 |\mathcal U(P)\cap\mathcal U(P')|&\le1,\\
 |\mathcal Q(P)\cap\mathcal Q(P')|&\le2,\\
 |(\mathcal Q\cup\mathcal U)(P)
       \cap(\mathcal Q\cup\mathcal U)(P')|&\le3
 \end{aligned}                                             \tag{5.3}
\]

for every owner-disjoint selected pair, with the three-resource case
having the exact negligible census (4.3).

## 6. Why expansion remains a separate theorem

Quasi-linearity does not by itself give the required cover-down.  The
following literal construction gives a growing top-simple star.

### Proposition 6.1 (linear root star)

Fix a rank-`r-1` root `Q`.  There are

\[
                         \left\lfloor{r-1\over2}\right\rfloor          \tag{6.1}
\]

packets which have distinct tops, are pairwise owner-disjoint, and whose
pairwise common q1 inventory is exactly the singleton `{Q}`.

#### Proof

The complement of `Q` has size `r`.  Fix one label `z` there and partition
as many as possible of the other `r-1` labels into pairs `{x_i,y_i}`.
Choose a fixed `(L-3)`-set `P subset Q`.  For every pair put

\[
 H_i=Q\cup\{x_i,z,y_i\},\qquad
 F_i=P\cup\{x_i,z,y_i\},                                  \tag{6.2}
\]

and choose a Hamilton cycle on `F_i` containing the path `x_i-z-y_i`.
Then `Q=H_i-{x_i,z,y_i}` is one lower root of the packet.

For `i != j`,

\[
                         H_i\cap H_j=Q\cup\{z\}             \tag{6.3}
\]

has rank `r`.  A common owner would have to equal this intersection, which
would require `{x_i,y_i}` and `{x_j,y_j}` to be cycle edges.  They are not:
in each chosen path the label `z` separates the corresponding pair.
Hence the packets are owner-disjoint.  Their tops are visibly distinct.
Theorems 2.1 and 3.1 show that tops meeting in rank `r` share no upper and
at most one lower root; since `Q` is common, it is the whole common q1
inventory.  \(\square\)

Thus the packet--resource incidence graph contains stars of order
`Theta(r)` even after top simplification.  Pairwise intersections are only
one, but no alternating expansion follows without a reservoir of other
roots.

The exact next theorem is therefore an **all-cut mesoscopic reservoir
lemma**: choose a top-simple owner packet packing so that every residual
family of packets has enough distinct lower and upper exits, with the
owner/lower leaves equal and the upper demand priced against its exact
`2/(r-1)` fractional oversupply.  Theorems 2.1--5.1 make the local side of
that lemma proof-safe; they do not supply its global expansion.
