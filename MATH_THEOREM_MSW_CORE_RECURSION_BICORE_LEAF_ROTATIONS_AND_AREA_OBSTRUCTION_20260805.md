# MSW core recursion, bi-core leaf rotations, and the area obstruction

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, enumeration, or solver  
**Status:** exact recursive characterization and exact local exchange
theorem.  A canonical leaf-rotation edge is always safe in at least one
sign when `r>2h`, but leaf rotations cannot by themselves give a spanning
Dyck Gray path in every semilength.  The remaining issue is the
bi-core safety of the necessarily numerous long transpositions.

## 0. Outcome

Let `x` be a Dyck word of semilength `r`, and write its canonical MSW flip
permutation as

\[
             \pi(x)=(\pi_1,\ldots,\pi_{2r}).          \tag{0.1}
\]

The odd entries are the zero positions of `x`, in their MSW insertion
order, and the even entries are the one positions, in their MSW deletion
order.  Put

\[
 \mathsf I(x)=(\pi_1,\pi_3,\ldots,\pi_{2r-1}),
 \qquad
 \mathsf D(x)=(\pi_2,\pi_4,\ldots,\pi_{2r}).          \tag{0.2}
\]

The forward and reverse stem cores are exactly

\[
\begin{aligned}
 Q_h^+(x)
   &=\operatorname{Up}(x)\setminus
       \{\mathsf D_1(x),\ldots,\mathsf D_h(x)\},\\
 Q_h^-(x)
   &=\operatorname{Down}(x)\setminus
       \{\mathsf I_{r-h+1}(x),\ldots,\mathsf I_r(x)\}.
                                                               \tag{0.3}
\end{aligned}
\]

Section 1 gives a complete first-return recursion for these sets.  In
particular, the plus core is obtained by processing primitive factors from
left to right, while the minus core is obtained by processing them from
right to left.

For a transposition

\[
       y=x-\{q\}+\{p\},\qquad x_q=1,\quad x_p=0,       \tag{0.4}
\]

define the MSW deletion and insertion ranks

\[
 d_x(q)=\operatorname{pos}_{\mathsf D(x)}(q),
 \qquad i_x(p)=\operatorname{pos}_{\mathsf I(x)}(p).  \tag{0.5}
\]

Then the edge is bi-core safe in the two signs exactly as follows:

\[
\begin{array}{c|c}
\text{forward sign}&d_x(q)>h\ \text{and}\ d_y(p)>h,\\[2mm]
\text{reverse sign}&i_x(p)\le r-h\ \text{and}\ i_y(q)\le r-h.
\end{array}                                           \tag{0.6}
\]

Thus the condition is intrinsic to the unordered transposition edge; no
choice of which endpoint is called the target changes it.

For the basic contextual leaf rotation

\[
 x=A\,10\,1B0\,C,
 \qquad
 y=A\,110B0\,C,                                      \tag{0.7}
\]

where `A,B,C` are Dyck and have semilengths `a,b,c`, put

\[
             \ell=a+b+1,
 \qquad      r=a+b+c+2.                               \tag{0.8}
\]

The exact bi-core criterion collapses to

\[
 \boxed{
 \begin{aligned}
   xy\text{ is plus-safe}  &\iff \ell>h,\\
   xy\text{ is minus-safe} &\iff r-\ell>h.
 \end{aligned}}                                       \tag{0.9}
\]

Consequently every such rotation has at least one safe sign when
`r>2h`, and it has both signs when

\[
                         h<\ell<r-h.                  \tag{0.10}
\]

This also gives the exact answer to the proposed automaticity shortcut.
Target-core safety does **not** force source-core safety.  On the plus
shore the only leaf-rotation failure occurs at `ell=h`: the target
coordinate has deletion rank `h+1`, while the source coordinate has rank
`h`.  There is an analogous reverse boundary.

The positive local theorem does not yield the desired Hamilton path.
Let `L_r` be the graph of Dyck words joined only by adjacent
`01 <-> 10` leaf rotations.  Its area bipartition has imbalance

\[
 \left|\sum_{x\in\mathcal D_r}(-1)^{\operatorname{area}(x)}\right|
 =
 \begin{cases}
   0,&r\text{ even},\\
   \operatorname{Cat}_{(r-1)/2},&r\text{ odd}.
 \end{cases}                                          \tag{0.11}
\]

Hence `L_r` has no Hamilton path for odd `r>=5`.  More sharply, any
transposition Hamilton path through all Dyck words must use at least

\[
                   \operatorname{Cat}_{(r-1)/2}-1     \tag{0.12}
\]

area-parity-preserving, necessarily nonadjacent transitions when `r` is
odd.  Thus a leaf-rotation path plus a bounded set of long bridges cannot
solve the signed MSW ordering problem.  The minimal remaining theorem is
to control a Catalan-scale family of long Proskurowski--Ruskey
transpositions under the exact rank test (0.6).

## 1. Recursive description of the MSW cores

Let `mu` denote reverse-complement.  Write the first-return decomposition

\[
                     x=1u0v,
 \qquad              d=|u|+2.                        \tag{1.1}
\]

The MSW recursion is

\[
 \pi(1u0v)=
   \bigl(d,\ d-\pi(\mu u),\ 1,\ d+\pi(v)\bigr),       \tag{1.2}
\]

where affine operations are entrywise and concatenation is understood.

### Theorem 1.1 (insertion/deletion recursion)

The two half-orders in (0.2) satisfy

\[
\boxed{
\begin{aligned}
 \mathsf I(1u0v)
   &=\bigl(d,\ d-\mathsf D(\mu u),\ d+\mathsf I(v)\bigr),\\
 \mathsf D(1u0v)
   &=\bigl(d-\mathsf I(\mu u),\ 1,\ d+\mathsf D(v)\bigr).
                                                        \tag{1.3}
\end{aligned}}
\]

In particular, if `P,Q` are Dyck and `P` has semilength `s`, then

\[
\begin{aligned}
 \mathsf I(PQ)&=\mathsf I(P)\,\Vert\,
                         (2s+\mathsf I(Q)),\\
 \mathsf D(PQ)&=\mathsf D(P)\,\Vert\,
                         (2s+\mathsf D(Q)).             \tag{1.4}
\end{aligned}
\]

#### Proof

The middle block in (1.2) has even length and begins at global flip
position two.  Its odd global positions therefore come from the even
local positions of `pi(mu u)`, while its even global positions come from
the odd local positions.  The leading `d` is odd-positioned and the
closing `1` is even-positioned.  Splitting (1.2) by parity gives (1.3).
Formula (1.4) is the corresponding split of the usual MSW concatenation
law. `square`

### Corollary 1.2 (primitive-factor localization)

Let `x=wv`, where `w` is the first primitive factor, of semilength `a`,
and `v` has semilength `b=r-a`.  For `0<=h<=r`,

\[
 Q_h^+(wv)=
 \begin{cases}
   Q_h^+(w)\ \cup\ (2a+\operatorname{Up}(v)),&h<a,\\
   2a+Q_{h-a}^+(v),&h\ge a,
 \end{cases}                                          \tag{1.5}
\]

and

\[
 Q_h^-(wv)=
 \begin{cases}
   \operatorname{Down}(w)\ \cup\ (2a+Q_h^-(v)),&h<b,\\
   Q_{h-b}^-(w),&h\ge b.
 \end{cases}                                          \tag{1.6}
\]

Thus at most one primitive factor is partially cut by either core.  The
plus boundary moves from left to right and the minus boundary from right
to left.

#### Proof

By (1.4), `mathsf D(wv)` is the deletion order of `w` followed by that of
`v`, and has block lengths `a,b`.  Removing its first `h` entries gives
(1.5).  The first reverse deletions are the last entries of
`mathsf I(wv)`, so they process `v` first and then `w`, which gives (1.6).
`square`

For a primitive word `w=1u0` of semilength `a`, (1.3) specializes to

\[
 \mathsf D(w)=(2a-\mathsf I(\mu u),\ 1),
 \qquad
 \mathsf I(w)=(2a,\ 2a-\mathsf D(\mu u)).             \tag{1.7}
\]

Hence, for `h<a`, one may also write the cores explicitly as

\[
\begin{aligned}
 Q_h^+(w)
  &=\{1\}\cup
    \Bigl(2a-\bigl(\operatorname{Down}(\mu u)
             \setminus\{\mathsf I_1(\mu u),\ldots,
                          \mathsf I_h(\mu u)\}\bigr)\Bigr),\\
 Q_h^-(w)
  &=\{2a\}\cup
    \Bigl(2a-\bigl(\operatorname{Up}(\mu u)
             \setminus\{\mathsf D_{a-h}(\mu u),\ldots,
                          \mathsf D_{a-1}(\mu u)\}\bigr)\Bigr).
                                                        \tag{1.8}
\end{aligned}
\]

Here a scalar minus a set is interpreted elementwise.  Formula (1.8) is
the precise left-tree recursion missing from the purely factorwise
description: a plus-core cut becomes an insertion-order cut in the
mirrored interior, while a minus-core cut becomes a terminal
deletion-order cut there.

## 2. The intrinsic bi-core exchange graph

### Theorem 2.1 (rank criterion)

Let `x,y` be related by (0.4).  The edge can be used with full clipped
residence in the forward sign if and only if

\[
                         d_x(q)>h,
 \qquad                 d_y(p)>h.                    \tag{2.1}
\]

It can be used with full clipped residence in the reverse sign if and
only if

\[
                         i_x(p)\le r-h,
 \qquad                 i_y(q)\le r-h.               \tag{2.2}
\]

These predicates are unchanged if `x` and `y` exchange the roles of
source and target.

#### Proof

The first `h` forward departures from `x` are precisely the first `h`
entries of `mathsf D(x)`.  Thus the upstep `q` survives the target stem
exactly when `d_x(q)>h`; the new upstep `p` survives the terminal part of
the source stem exactly when `d_y(p)>h`.  This proves (2.1).

Starting at the complementary endpoint reverses the path.  The departure
order of the original downsteps is therefore

\[
                \mathsf I_r(x),\mathsf I_{r-1}(x),
                    \ldots,\mathsf I_1(x).            \tag{2.3}
\]

The downstep `p` of `x` survives its first `h` reverse departures exactly
when `i_x(p)<=r-h`, and similarly for `q` in `y`.  This proves (2.2).
Both conditions are conjunctions of one statement at each endpoint, so
reversing the edge changes neither predicate. `square`

### Corollary 2.2 (Dyck-context shielding)

Suppose `x=AB` and `y=AB'`, where `A,B,B'` are Dyck, `A` has semilength
at least `h`, and `B,B'` differ by one transposition.  Then `xy` is
plus-safe.

Dually, if `x=BA` and `y=B'A` with a common Dyck suffix `A` of semilength
at least `h`, then `xy` is minus-safe.

#### Proof

In the first case, (1.4) places every deletion coordinate changed in the
suffix after all `|A|/2>=h` deletion coordinates of `A`, at both
endpoints.  This gives (2.1).

In the second case, the insertion ranks of every changed coordinate in
the prefix are at most `r-|A|/2<=r-h`, at both endpoints.  This gives
(2.2). `square`

This shielding lemma gives a direct recursive design rule: suffix
transitions behind an `h`-semilength Dyck guard may be assigned the plus
sign, and prefix transitions before such a suffix guard may be assigned
the minus sign.  It does not cover primitive roots or transitions crossing
the guard boundary.

## 3. Exact analysis of a contextual leaf rotation

Let `A,B,C` be Dyck words of semilengths `a,b,c`, and define (0.7).  The
two words differ by swapping

\[
             p=2a+2,
 \qquad      q=2a+3,                                 \tag{3.1}
\]

where `p` is a downstep of `x` and `q` is an upstep of `x`.

### Theorem 3.1 (leaf-rotation rank table)

With `ell` as in (0.8), the four relevant ranks are

\[
\boxed{
\begin{array}{c|cc}
 &x&y\\ \hline
 \text{forward rank}&d_x(q)=\ell+1&d_y(p)=\ell\\
 \text{insertion rank}&i_x(p)=a+1&i_y(q)=\ell+1\\
 \text{reverse rank}&r+1-i_x(p)=r-a&r+1-i_y(q)=r-\ell.
\end{array}}                                         \tag{3.2}
\]

Consequently (0.9) holds.

#### Proof

Remove the common prefix `A`; (1.4) later adds `a` to every half-order
rank.  Put `D=2b+4`.  Direct substitution in the MSW recursion gives the
local flip words

\[
\begin{aligned}
 \pi(10\,1B0\,C)
   &=(2,1,D,D-\pi(\mu B),3,D+\pi(C)),\\
 \pi(110B0\,C)
   &=(D,D-\pi(\mu B),2,3,1,D+\pi(C)).                \tag{3.3}
\end{aligned}
\]

In the first row, `q=3` is at even flip position `D`, so its local
deletion rank is `D/2=b+2`; `p=2` is the first insertion.  In the second
row, `p=2` is at even flip position `D-2`, so its local deletion rank is
`b+1`; `q=3` is at odd flip position `D-1`, so its local insertion rank is
`b+2`.  Adding the `a` prefix ranks proves the first two rows of (3.2).
Reverse rank is `r+1-i`, which gives the last row.  Theorem 2.1 now gives

\[
 d_x(q),d_y(p)>h\iff\ell>h,
\]

and, since `r-ell<=r-a`,

\[
 r+1-i_x(p),r+1-i_y(q)>h\iff r-\ell>h.
\]

This is (0.9). `square`

### Corollary 3.2 (the source-core condition is not automatic)

For every `h>=1` and `r>=h+1`, there is a leaf rotation for which the
coordinate at the target belongs to `Q_h^+`, but the entering coordinate
at the source does not.

For example take `a=h-1`, `b=0` in (0.7).  Then `ell=h`, and

\[
                  d_x(q)=h+1,
 \qquad           d_y(p)=h.                           \tag{3.4}
\]

In the zigzag specialization this is

\[
 (10)^r
 \longleftrightarrow
 (10)^{h-1}\,1100\,(10)^{r-h-1}.                    \tag{3.5}
\]

There is a reverse analogue: choose `c=h-1`.  Then the source reverse
rank is `r-ell=c+1=h`, while the target reverse rank is
`r-a=b+c+2>h`.

Thus a Proskurowski--Ruskey-style local rotation is usually well behaved
away from the aperture boundary, but target-core safety alone is not a
theorem.  The precise plus loss is one departure rank.

### Corollary 3.3 (one safe sign above the Gaussian aperture)

If `r>2h`, every contextual leaf rotation is bi-core safe in at least one
sign.  It is forced to the minus sign when `ell<=h`, forced to the plus
sign when `ell>=r-h`, and is safe in both signs for (0.10).

#### Proof

The two safety resources in (0.9) sum to

\[
                         \ell+(r-\ell)=r.
\]

They cannot both be at most `h` when `r>2h`.  The remaining assertions are
immediate from (0.9). `square`

## 4. Why leaf rotations alone cannot span

Let

\[
 \operatorname{area}(x)
   =\operatorname{inv}(x)-\frac{r(r+1)}2,             \tag{4.1}
\]

where `inv(x)` is the number of pairs `i<j` with `x_i=1,x_j=0`.  An
adjacent `10 <-> 01` rotation changes `area` by one.  Hence the leaf
rotation graph is bipartite by area parity.

### Theorem 4.1 (exact area-parity imbalance)

Put

\[
                 E_r=\sum_{x\in\mathcal D_r}
                           (-1)^{\operatorname{area}(x)}.              \tag{4.2}
\]

Then

\[
 E_{2m}=0\quad(m>=1),
 \qquad
 E_{2m+1}=(-1)^m\operatorname{Cat}_m.                \tag{4.3}
\]

#### Proof

For the first-return decomposition `x=1u0v`, with `u` of semilength `j`,

\[
 \operatorname{area}(x)
   =\operatorname{area}(u)+\operatorname{area}(v)+j. \tag{4.4}
\]

Therefore, with `E_0=1`,

\[
 E_r=\sum_{j=0}^{r-1}(-1)^jE_jE_{r-1-j}.             \tag{4.5}
\]

Let `F(z)=sum_(r>=0) E_r z^r`.  Equation (4.5) is

\[
 F(z)=1+zF(-z)F(z).                                   \tag{4.6}
\]

Replacing `z` by `-z` and adding gives

\[
                         F(z)+F(-z)=2,                \tag{4.7}
\]

so every positive even coefficient vanishes.  Write
`F(z)=1+G(z)`, where `G` is odd.  Equations (4.6)--(4.7) give

\[
                         G=z(1-G^2).                  \tag{4.8}
\]

The unique formal solution with leading term `z` is

\[
 G(z)=\sum_{m\ge0}(-1)^m\operatorname{Cat}_m z^{2m+1},
                                                               \tag{4.9}
\]

which proves (4.3). `square`

### Corollary 4.2 (Catalan many long transitions are unavoidable)

For odd `r=2m+1>=5`, the leaf-rotation graph has no Hamilton path.
Moreover, every Hamilton path in the full Dyck transposition graph uses at
least

\[
                         \operatorname{Cat}_m-1       \tag{4.10}
\]

transitions preserving area parity.

#### Proof

The two area-parity shores differ in size by `Cat_m`.  A path using only
leaf rotations alternates shores, so its shore sizes can differ by at most
one.  This proves the first assertion.

For the second, encode the shore sequence of an arbitrary Hamilton path as
a binary word with shore counts `n_+>=n_-`.  The `n_-` minority symbols
create at most `n_-+1` blocks of majority symbols.  Hence there are at
least

\[
                     n_+-(n_-+1)=\operatorname{Cat}_m-1
\]

same-shore adjacencies.  Such a transition preserves area parity.  A swap
of positions at distance `s` is a product of `s` adjacent binary swaps, so
it preserves parity exactly when `s` is even; in particular it is not a
leaf rotation. `square`

## 5. Sharpened frontier

The core sets themselves are no longer opaque: (1.3)--(1.8) compute them
recursively from the Dyck factorization, and (2.1)--(2.2) give a scalar
rank test for every proposed transposition edge.

The common local PR/Tamari move is also completely understood.  Its two
safe-sign apertures are the complementary integers `ell` and `r-ell`.
At Gaussian depth `h=Theta(sqrt(r))`, every such edge has a safe sign, and
all except the two `h`-wide boundary bands have both signs.

However, Theorem 4.1 prevents a proof based on leaf rotations plus only a
bounded connector bank.  In every odd semilength there is a Catalan-scale
parity surplus, and (4.10) requires a Catalan-scale family of long
transpositions.  Therefore the exact remaining combinatorial statement is:

> Construct, or audit in the recursive Proskurowski--Ruskey order, the
> required long transpositions so that their endpoint ranks satisfy
> (2.1) or (2.2) with the prescribed alternating sign.

The factor recursion (1.5)--(1.8) and the shielding Corollary 2.2 reduce
that audit to transitions crossing the current primitive/core boundary.
They do not yet prove a spanning path or a Hall matching in the full
bi-core graph.

The adjacent-path obstruction is consistent with, and gives a direct
parity proof of, the sharp adjacent-generation boundary in
F. Ruskey and A. Proskurowski, *Generating binary trees by
transpositions*, Journal of Algorithms **11** (1990), 68--84: adjacent
transposition generation exists exactly when the semilength is even or is
less than five.  Their unrestricted transposition Gray code supplies the
long transitions whose new MSW rank audit is isolated above.
