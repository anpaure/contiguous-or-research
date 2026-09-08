# Independent audit of the reset--return-rail complete-reversal cycle

**Date:** 2026-08-01  
**Status:** **GO**, with one sharpening.  The local theorem in
`MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`
is sound.  The unused permanent anchor in that statement is convenient but
not necessary: the construction already works under

\[
                 r\ge 2d+1,\qquad k-r\ge 2d+1.             \tag{0.1}
\]

It gives a literal local resident/all-depth three-return lift.  It does not
give a spanning owner factor, an exterior-safe linear splice, global upper
coverage, a common residual compiler, or same-parity regeneration.

The source theorem audited here had SHA-256

```text
f2a1c1bedcd58ce74c9c1b983affb2995a07d4fe73017e74e939dc6c5e0f8ac0
```

at the time of this audit.

## 1. Independent reconstruction

Put

\[
                    n=d+1,\qquad N=2n.
\]

Let `K` have rank `r-n`, choose pairwise distinct private coordinates
`z_0,...,z_(N-1)` outside `K`, and define

\[
 T_i=K\cup\{z_i,z_{i+1},\ldots,z_{i+n-1}\},
 \qquad i\in\mathbb Z_N.                                  \tag{1.1}
\]

Open the edge from

\[
 E=T_0\quad\hbox{to}\quad F=T_{N-1}.
\]

Write

\[
 L=E\cap F,qquad \delta=E-L=z_{n-1},\qquad
 \alpha=F-L=z_{N-1}.                                     \tag{1.2}
\]

Choose distinct `x_1,...,x_d` in `K` and distinct fresh
`y_1,...,y_d` outside the entire reset support

\[
                   K\cup\{z_0,\ldots,z_{N-1}\}.           \tag{1.3}
\]

For `X_j={x_1,...,x_j}` and `Y_j={y_1,...,y_j}`, put

\[
 P_j=(L-X_j)+Y_j+\alpha\qquad(0\le j\le d),               \tag{1.4}
\]

and

\[
 Q_0=(L-X_d)+Y_d+\delta,                                  \tag{1.5}
\]

\[
 Q_j=L-\{x_{j+1},\ldots,x_d\}
        +\{y_{j+1},\ldots,y_d\}+\delta
        \qquad(1\le j\le d).                            \tag{1.6}
\]

Then `P_0=F` and `Q_d=E`.  The combined cyclic root word is

\[
 Z^+=(T_0,T_1,\ldots,T_{N-1},
       P_1,\ldots,P_d,Q_0,\ldots,Q_{d-1}).                 \tag{1.7}
\]

It has

\[
                         M=N+2d=4d+2                     \tag{1.8}
\]

roots.  Its opposite phase is the complete reversal based at `T_0`:

\[
                         Z_i^-=Z_{-i}^+.                  \tag{1.9}
\]

## 2. Exact supply, roots, and immediate palettes

The two independent supplies required by (1.3) are exactly

\[
 |K|=r-d-1\ge d,
\]

and

\[
 k-|K\cup\{z_0,\ldots,z_{N-1}\}|
   =k-r-d-1\ge d.
\]

These are equivalent to (0.1).  The extra anchor `b` in the source theorem
raises the first sufficient inequality to `r>=2d+2`, but Section 4 below
shows why no anchor is needed.

Every internal `P_j`, `j>=1`, contains `y_1`; every internal `Q_j`,
`j<=d-1`, contains `y_(j+1)`.  No reset root contains a `y` coordinate.
Therefore no internal return root is a reset root.  Prefix strictness and
the `alpha/delta` split distinguish all return roots.  Hence (1.7) is
simple.  Each transition changes exactly one coordinate, so it is a simple
rank-`r` Johnson cycle.

The reset-path lower colours all contain the complete core `K`, and its
upper colours contain no `y` coordinate.  Along the return path:

* every lower colour omits at least one selected `x_j`; and
* every upper colour contains at least one fresh `y_j`.

The return palettes are internally simple by their strict prefix/suffix
indices.  Thus neither return palette can meet its reset-path counterpart,
and the complete lower and upper `q1` palettes are simple.  Reversal keeps
the undirected edges fixed, so both phases use exactly the same palettes.

## 3. Exact cyclic residence

Every nonconstant coordinate has one cyclic positive run.  Directly from
(1.1) and (1.4)--(1.6), its length is

\[
\begin{array}{c|c}
\text{coordinate type}&\text{positive-run length}\\ \hline
y_j&d+1\\
\alpha,\delta&2d+1\\
x_j&3d+1\\
z_i\in(E\cap F)-K&3d+1\\
z_i\notin E\cup F&d+1.
\end{array}                                               \tag{3.1}
\]

Coordinates in `K-{x_1,...,x_d}` are constant one, and unused ground
coordinates are constant zero.  In particular every positive run has
length at least `d+1`.  Reversal preserves these runs exactly.

The reason for the two enlarged lengths `3d+1` is transparent.  A selected
`x_j` is present on the whole reset path, while a seam-shared reset label is
present on the whole return path.  In each case replacing one old seam by
the other path lengthens, rather than splits, its positive run.

## 4. Nonempty maximal erosion without a permanent anchor

Define the maximal cyclic depth-`d` erosion by

\[
                   A_j^+=\bigcap_{h=0}^{d}Z_{j-h}^+.       \tag{4.1}
\]

The run calculation implies coordinatewise that

\[
                            D^dA^+=Z^+.                   \tag{4.2}
\]

There is also a structural proof that every source letter in (4.1) is
nonempty, even when `K={x_1,...,x_d}`.  The Johnson transition

\[
                  Z_{j-d-1}^+\longrightarrow Z_{j-d}^+
\]

inserts one coordinate.  Its positive run begins at `Z_(j-d)^+` and, by
Section 3, lasts at least `d+1` roots.  It is therefore present in every
root

\[
                  Z_{j-d}^+,Z_{j-d+1}^+,\ldots,Z_j^+,
\]

and hence belongs to `A_j^+`.  Thus

\[
                              A_j^+\ne\varnothing          \tag{4.3}
\]

for every `j`.  This proves the sharper first inequality in (0.1).

For the reversed phase, the maximal erosion satisfies the exact identity

\[
                              A_i^-=A_{d-i}^+.             \tag{4.4}
\]

Indeed,

\[
 A_i^-=\bigcap_{t=i-d}^{i}Z_{-t}^+
      =\bigcap_{s=-i}^{d-i}Z_s^+
      =A_{d-i}^+.
\]

Consequently, for every `0<=q<=d`,

\[
                   (D^qA^-)_i=(D^qA^+)_{d-i-q}.           \tag{4.5}
\]

So every derivative-row occurrence inventory agrees, not merely its rank
histogram.

## 5. Exact all-width reversal

For every cyclic interval width `ell`, reversal gives

\[
 \bigcup_{h=0}^{\ell-1}Z_{i+h}^-
 =
 \bigcup_{h=0}^{\ell-1}Z_{-i-h}^+
 =
 \bigcup_{h=0}^{\ell-1}Z_{-i-\ell+1+h}^+.                 \tag{5.1}
\]

Thus the complete cyclic root interval-OR decks agree pointwise after
reflection at every width.  Equation (4.4) gives the identical statement
for the source words `A+`,`A-`; (4.5) gives it for every lower derivative
row.

This is exact internal phase invariance.  It is stronger than matching
rank counts and stronger than matching only immediate palettes.

## 6. Literal three-return signature

For each undirected cycle edge `Z_iZ_(i+1)`, compare the forward atom with
its reversed atom.  In the head--upper-owner projection the alternating
overlay advances one root at a time around the `M`-cycle, so it is one
cycle.  The lower--tail overlay is likewise one cycle.

In the typed tail--head predecessor overlay, two alternating steps advance
the root index by two.  Hence the number of components is

\[
                              \gcd(M,2)=2,                 \tag{6.1}
\]

because `M=4d+2` is even.  These are the two parity cycles.

Opening the same undirected edge in both orientations turns the attachment
cycle into one path and each predecessor parity cycle into one path.  The
result is exactly the one attachment return plus two predecessor returns
exported by the opened rolling reset.  All three projections arise from
the same literal atoms.  Therefore this construction **does** give the
previously missing local compatible three-return lift, now with strict
depth-`d` residence and all internal widths included.

## 7. Independent H100 replay

The independent C++20 audit

```text
scratch/audit_reset_return_rail_independent_20260801.cpp
```

uses `std::bitset`, pointwise reflected intervals, and a separate
bipartite-component replay rather than the source theorem's `uint64_t`
implementation.  It tests:

* `1<=d<=30`;
* the sharp core size `|K|=d` and four larger core sizes;
* three different unused-ground surpluses;
* root and both q1 palette simplicity;
* every coordinate run;
* every cyclic root interval width;
* nonempty maximal erosion and exact depth-`d` factorization;
* pointwise reversal of every derivative row and every source interval;
* one attachment component and two predecessor parity components.

Compiled and run on H100 with `g++ -std=c++20 -O3`, it reports

```text
PASS_INDEPENDENT_RESET_RETURN_RAIL cases=450 d=1..30 core_surplus=-1..3 unused_surplus=0..2 roots=4d+2 q1_simple residence source_reversal all_widths derivative_rows attachment1 predecessor2
```

The retained transcript is

```text
scratch/audit_reset_return_rail_independent_20260801.out
```

## 8. Exact remaining gates

The result is local and cyclic.  It closes the literal role-conversion,
residence, erosion, immediate-palette, and internal all-width rows.  It does
not close any of the following global rows.

1. **Coefficient-one root planting.**  The `2d` new internal return roots
   must replace roots in a spanning middle-owner factor; they cannot be
   appended to a one-copy middle layer.
2. **Global topology.**  The packet is a closed component.  It must be
   opened and connected to the ambient path/cycle structure through a safe
   common cut.
3. **Exterior crossing intervals.**  Equation (5.1) is cyclic/internal.
   After a linear splice into a fixed exterior, crossing intervals agree
   only if the exterior sockets are also reflected or those witnesses are
   protected elsewhere.
4. **Global upper completeness.**  Equal packet decks do not prove that
   the ambient chronology covers every upper target.
5. **Common residual compiler.**  Internal target--cell incidence graphs
   are exactly isomorphic by reversal, but crossing cells and exterior
   assignments still need one common contracted Hall/Rado certificate.
6. **Private supply and regeneration.**  One packet has the required fresh
   labels.  No theorem yet plants enough protected copies or regenerates
   the same interface under the same-parity Pascal lift.

Accordingly the next precise statement is a **protected complete-reversal
host theorem**: plant this `4d+2`-root cycle in an upper-complete
coefficient-one owner factor, give it a phase-common exterior cut, and
prove a common residual compiler after contracting the packet.

