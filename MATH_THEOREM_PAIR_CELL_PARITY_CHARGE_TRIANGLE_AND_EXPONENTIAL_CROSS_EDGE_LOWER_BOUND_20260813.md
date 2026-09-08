# Pair-cell parity charge, the minimal triangle carrier, and an exponential cross-edge lower bound

**Date:** 2026-08-13  
**Status:** unconditional.  This note strengthens the fixed-pair-structure
obstruction after the transversal lift.  It gives the full mod-two edge
signature, proves that no owner/lower-conformal relative trade can change
the parity charge, classifies the smallest closed parity carrier, and proves
that a global exact completion needs exponentially many nonlift cross-cell
edges.  It does not construct that completion or address residence, upper
support, or fusion.

## 0. Setting and outcome

Put

\[
 k=2p+1,\qquad R=p+1,\qquad
 \mathcal O={{[k]}\choose {p+1}},\qquad
 \mathcal L={{[k]}\choose p},\qquad
 W=|\mathcal O|=|\mathcal L|.                         \tag{0.1}
\]

Write

\[
 [k]=\{z\}\mathbin{\dot\cup}\bigdotcup_{i=1}^pP_i,
 \qquad P_i=\{a_i,b_i\}.                              \tag{0.2}
\]

Fix a transversal edge-lift cycle `P_H`.  It uses the `2^p`
transversal lower colours and saturates `2^p` owners, all of which omit
`z` and have exactly `p-1` singleton matched pairs.  A residual coloured
edge has the form

\[
 e=(L;u,v)=\{L\cup\{u\},L\cup\{v\}\},
 \qquad u,v\notin L,\quad u\ne v.                     \tag{0.3}
\]

It is internal to the fixed pair structure exactly when
`{u,v}=P_i` for some `i`.  Every other residual edge is called cross-cell.

The conclusions are:

1. every exact residual factor has a full `F_2^p` edge-signature identity;
2. when `p=2^s-1`, its cross-cell bank has odd parity charge;
3. an owner/lower-conformal relative trade preserves that charge, so no
   such trade, bounded or otherwise, repairs the obstruction;
4. the smallest closed owner/lower-exact parity carrier is a three-edge
   bottom Johnson triangle, and one such triangle removes the scalar parity
   contradiction;
5. nevertheless, for every odd `p`, any exact factor containing `P_H`
   has at least

\[
 \boxed{
 \binom p{(p-1)/2}
 +p\binom{p-1}{(p-1)/2}
 }
 =\Theta(\sqrt p\,2^p)                                \tag{0.4}
\]

nonlift cross-cell edges.  Thus `O(1)` absorbers suffice only for the
one-bit parity ledger, not for a global exact completion whose other edges
are internal to this fixed pair structure.

## 1. The full edge signature

For a residual edge `(0.3)`, define

\[
 \alpha(e)_i=\mathbf 1_{\{a_i\in\{u,v\}\}}
       \quad\text{in }\mathbb F_2,
 \qquad
 \eta(e)=1+\sum_{i=1}^p\alpha(e)_i
       \quad\text{in }\mathbb F_2.                    \tag{1.1}
\]

Thus `alpha(e)` records which distinguished `a`-coordinates are exchanged,
and `eta(e)` is its scalar parity charge.

### Theorem 1.1 (residual cut identity)

If `F` is any exact residual completion after `P_H`, then

\[
                         \sum_{e\in F}\alpha(e)=0
                         \quad\text{in }\mathbb F_2^p. \tag{1.2}
\]

Consequently

\[
                         \sum_{e\in F}\eta(e)
                         \equiv W-2^p\pmod2.           \tag{1.3}
\]

#### Proof

Fix `i` and sum the residual owner-degree equations over all owners
containing `a_i`.  Every residual capacity is zero or two, so the right
side is even.  The edge `(L;u,v)` contributes oddly precisely when exactly
one endpoint contains `a_i`.  If \(a_i\in L\), both endpoints contain it; if
\(a_i\notin L\), exactly one contains it precisely when
\(a_i\in\{u,v\}\).
The contribution is therefore `alpha(e)_i`, proving `(1.2)` coordinatewise.

There is one residual edge for each of the `W-2^p` residual colours.  Sum
the definition of `eta` over all edges and use `(1.2)` to obtain `(1.3)`.
\(\square\)

An internal direction-`i` edge exchanges `{a_i,b_i}`, hence has
`alpha(e)=e_i` and `eta(e)=0`.  A cross-cell edge is parity-active exactly
when its exchange pair contains an even number of `a`-coordinates.  The
three possible forms are

\[
 \{a_i,a_j\},\quad \{b_i,b_j\}\quad(i\ne j),
 \qquad\text{or}\qquad \{z,b_i\}.                     \tag{1.4}
\]

The cross forms \(\{a_i,b_j\}\) with \(i\ne j\) and \(\{z,a_i\}\) have
charge zero.

### Corollary 1.2 (odd cross charge)

If `p=2^s-1`, `s>=2`, then

\[
                         \sum_{e\in F\text{ cross}}\eta(e)=1.
                                                                    \tag{1.5}
\]

#### Proof

Lucas's theorem gives `W` odd, whereas `2^p` is even.  Equation `(1.3)`
is therefore one.  Internal edges have charge zero. \(\square\)

This refines the direction-parity proof: not every cross-cell edge repairs
the obstruction.  The parity-active class `(1.4)` must occur oddly.

## 2. Conformal trades cannot change the charge

Call two partial coloured configurations `F_0,F_1` owner/lower-conformal
when they use the same lower-colour set, use one edge of each colour, and
have the same owner incidence degree at every owner.

### Theorem 2.1 (relative-trade charge invariance)

For every owner/lower-conformal pair,

\[
 \sum_{e\in F_0}\alpha(e)=\sum_{e\in F_1}\alpha(e),
 \qquad
 \sum_{e\in F_0}\eta(e)=\sum_{e\in F_1}\eta(e).       \tag{2.1}
\]

In particular, if every edge of `F_0` is internal, the cross edges of
`F_1` have total charge zero.  No owner/lower-conformal relative trade of
any size can supply `(1.5)`.

#### Proof

For each `i`, the sum of `alpha(e)_i` over a partial configuration is the
parity of

\[
 \sum_{T:a_i\in T}\deg_F(T).                           \tag{2.2}
\]

Equal owner degree vectors give the first identity.  The two configurations
have the same number of colours and hence the same number of edges; the
definition `(1.1)` then gives the second identity. \(\square\)

Thus a literal request for a degree-preserving trade which changes the
parity vector has no solution.  A parity carrier must instead be installed
as a closed partial factor, or it must expose a nonzero owner boundary to a
larger joint completion.

## 3. The minimum closed parity carrier

Choose three distinct matched pairs and, after relabelling, use
`a_1,a_2,a_3`.  Let `B` be any `(p-1)`-set disjoint from these three
coordinates and containing `z`; such a set exists for every `p>=3`.  Put

\[
 U=B\cup\{a_1,a_2,a_3\},\qquad
 T_i=U-\{a_i\}\quad(i=1,2,3).                          \tag{3.1}
\]

Use the three owner edges

\[
 T_1T_2,\qquad T_2T_3,\qquad T_3T_1,                  \tag{3.2}
\]

with respective lower colours

\[
 U-\{a_1,a_2\},\quad
 U-\{a_2,a_3\},\quad
 U-\{a_3,a_1\}.                                      \tag{3.3}
\]

### Theorem 3.1 (minimal bottom-triangle carrier)

The bank `(3.1)--(3.3)` is a simple closed coloured factor on three
owners: every owner has degree two and its three lower colours are distinct.
All three edges are cross-cell and parity-active.  The bank is disjoint
from the owner and lower shores of `P_H`, and

\[
 \sum_{e\in(3.2)}\alpha(e)=0,
 \qquad
 \sum_{e\in(3.2)}\eta(e)=1.                            \tag{3.4}
\]

It is the smallest possible zero-boundary owner/lower-exact bank with odd
charge.  More precisely, every three-edge example is, up to relabelling, a
bottom Johnson triangle

\[
 T_x=U-\{x\},\quad T_y=U-\{y\},\quad T_w=U-\{w\},      \tag{3.5}
\]

and all three edges are cross-cell exactly when no two of `x,y,w` are a
matched pair.

#### Proof

The owners in `(3.1)` have rank `p+1`.  Pairwise intersections are exactly
the three rank-`p` sets in `(3.3)`, so the colours are legal and distinct.
Each edge exchanges two `a`-coordinates from different matched pairs, and
therefore is cross-cell with signature `e_i+e_j` and charge one.  Every
coordinate occurs in two of the three signatures, proving `(3.4)`.

Every triangle owner and every triangle colour contains `z`.  Every lifted
owner and every transversal colour omits `z`, proving disjointness.

A zero-boundary simple owner bank is 2-regular, so each component is a
simple cycle and has at least three edges.  Its total signature is zero by
the same cut calculation as Theorem 1.1, so odd charge is equivalent to an
odd number of edges.  One and two edges are impossible, while `(3.2)` has
three.

Finally, three distinct pairwise adjacent Johnson vertices form one of two
triangle types.  If they share a common rank-`p` subset, all three edge
intersections are that same subset and lower-colour injection fails.
Otherwise their union is one rank-`p+2` set `U` and they have the form
`(3.5)`; their three pairwise intersections are distinct.  The edge
`T_xT_y` is internal exactly when `{x,y}` is one matched pair. \(\square\)

Freezing one such triangle removes three colours and saturates three
owners.  The remaining capacities are still zero or two and the remaining
colour count is `W-2^p-3`, which is even under Corollary 1.2.  Therefore
the triangle removes the scalar contradiction in the internal direction
equations.  This is a parity statement only; it does not assert that those
remaining equations are feasible.

## 4. Low pair cells force exponentially many cross edges

For an owner `T`, let `m(T)` be its number of singleton matched pairs.
The owners with fixed sentinel and double/empty/singleton statuses form a
cube `Q_{m(T)}`.  Hence `T` has exactly `m(T)` internal neighbours in the
fixed pair structure.

Let `N_m` be the total number of owners with `m(T)=m`, summed over both
sentinel sectors.

### Theorem 4.1 (internal-degree deficiency bound)

Let `F` be any simple exact owner/lower factor containing `P_H`, and let
`C_res` be its nonlift cross-cell edge set.  For `p>=3`,

\[
 2|C_{\rm res}|\ge 2N_0+N_1,
 \qquad
 |C_{\rm res}|\ge N_0+\left\lceil{N_1\over2}\right\rceil.  \tag{4.1}
\]

If `p` is odd, then

\[
 N_0=\binom p{(p-1)/2},\qquad
 N_1=2p\binom{p-1}{(p-1)/2},                            \tag{4.2}
\]

and `(4.1)` is exactly the bound `(0.4)`.

#### Proof

An owner in a `Q_0` cell has no internal incident edge, so both of its two
factor incidences are cross-cell.  An owner in a `Q_1` cell has only one
internal neighbour.  Simplicity permits at most one copy of that edge, so
at least one of its two factor incidences is cross-cell.  The lifted owners
all have `m=p-1>=2`, so none is counted in `N_0,N_1`.  Summing the forced
cross incidences gives `2N_0+N_1`; one cross edge supplies at most two of
them, proving `(4.1)`.

For odd `p`, the rank equation for an owner is

\[
                         2d+m+\epsilon=p+1,             \tag{4.3}
\]

where `d` is the number of double pairs and `epsilon` records the sentinel.
At `m=0`, necessarily `epsilon=0` and `d=(p+1)/2`, giving the first count.
At `m=1`, necessarily `epsilon=1` and `d=(p-1)/2`; choose the singleton
pair, its endpoint, and the double pairs to obtain the second count.
\(\square\)

For `p=2^s-1`, the lower bound is

\[
 |C_{\rm res}|\ge
 \binom p{(p-1)/2}+p\binom{p-1}{(p-1)/2}
 =\Theta(\sqrt p\,2^p).                                \tag{4.4}
\]

Thus the fixed-pair internal-closure programme has an exponential cross-edge
requirement before residence, upper support, or component joining are considered.
The three-edge triangle is sharp only as a closed carrier for the parity bit.

## 5. Exact scope

This note proves four different minimality statements which must not be
conflated:

* one parity-active cross edge is the smallest algebraic marker, but it
  leaves two owner degree deficits;
* no owner/lower-conformal relative trade can change the charge at any size;
* three cross edges in a bottom Johnson triangle are the smallest closed
  exact parity carrier;
* a global exact factor containing the transversal lift needs
  `Theta(sqrt(p)2^p)` nonlift cross-cell edges relative to the fixed pair
  structure.

The theorem does not select those exponentially many edges, prove the
capacitated Hall system for a proposed bank, preserve immediate-upper
support, establish a transition collar, or fuse components.  Those remain
joint completion problems.
