# An affine orthogonal complete mapping and its paired-erasure cut

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The parity complete-mapping equations in
`MATH_THEOREM_PARITY_COMPLETE_MAPPING_PAIRED_ORDER_LIFT_20260726.md`
have an explicit algebraic solution in which every coarse factor is the
recursive half-depth rainbow factor.  Thus exact ownership and ordinary
two-sided coarse-shadow injectivity are simultaneously compatible.

The same construction nevertheless fails the physical context code as
badly as the context-independent construction.  If an aligned window
completes (d) local pairs, every one of its signed context-code fibres
has cardinality at least

\[
                              2^{d-1}.                 \tag{0.1}
\]

The obstruction is an exact translation stabilizer: complementing both
coordinates in any bottom sibling pair leaves the entire recursive
direction trajectory unchanged.  Simultaneously complementing the phase
and parity bits in any even collection of completed pairs is invisible to
the physical trace.

Consequently the evident affine/Latin-square solution of the ownership
equations does **not** supply the missing pair-clustered trace code.  A
successful affine construction must use an orthogonal pair of factors
whose direction field has no such paired translation stabilizer; ordinary
recursive shadow injectivity alone is insufficient.

## 1. Orthogonal direction fields give complete mappings

For a neighbor permutation (K) of (Q_r), write

\[
 K(y)=y\oplus e_{\rho_K(y)}.                           \tag{1.1}
\]

Let (A\in S_r) be a coordinate permutation.  Suppose that (G,H) are
neighbor permutations of (Q_r) satisfying the pointwise orthogonality
identity

\[
                         \rho_H(y)=A\rho_G(y)
                         \qquad(y\in Q_r).             \tag{1.2}
\]

Let (E,O\) denote the even and odd shores of (Q_r).  For (p\in E)
and (x\in Q_r), put

\[
 y=p\oplus Ax,
 \qquad d_p(x)=\rho_G(y),
 \qquad F_p(x)=x\oplus e_{d_p(x)}.                    \tag{1.3}
\]

### Theorem 1.1 (orthogonal affine lift)

For every (p\in E), the affine map

\[
                         \theta_p(x)=p\oplus Ax        \tag{1.4}
\]
conjugates (F_p) to (H):

\[
                         \theta_pF_p=H\theta_p.        \tag{1.5}
\]

Moreover, for every (x\in Q_r),

\[
 T_x:p\longmapsto p\oplus e_{d_p(x)}                 \tag{1.6}
\]
is a bijection (E\to O).

#### Proof

If (i=d_p(x)=\rho_G(y)), then (1.2) gives

\[
 \theta_p(F_p(x))
 =p\oplus A(x\oplus e_i)
 =y\oplus e_{Ai}
 =y\oplus e_{\rho_H(y)}
 =H(y),                                                 \tag{1.7}
\]

which proves (1.5).

Fix (x).  The map (p\mapsto y=p\oplus Ax) bijects (E) onto the
parity shore of parity \(|x|\pmod2).  Under the same identification,

\[
 T_x(p)\oplus Ax
 =y\oplus e_{\rho_G(y)}
 =G(y).                                                 \tag{1.8}
\]

Every neighbor permutation bijects either parity shore onto the other.
Thus (1.8) conjugates (T_x) to the restriction of (G) between the two
shores, proving that (T_x:E\to O) is bijective. \(\square\)

In particular, if (H) is a (C_{2r})-factor, then every (F_p) is a
(C_{2r})-factor.  Any forward or reverse labelled-shadow property of
(H) is inherited by every (F_p).

The preceding construction is the general one-quotient affine Latin
ansatz, up to coordinate relabelling.

### Proposition 1.2 (classification of the affine Latin ansatz)

Let \(L,R\in S_r\), let \(c\in Q_r\), and let
\(\mu:Q_r\to[r]\).  Put

\[
 y=Lp\oplus Rx\oplus c,
 \qquad d_p(x)=L^{-1}\mu(y),                           \tag{1.9}
\]

and define

\[
 G_\mu(y)=y\oplus e_{\mu(y)},
 \qquad
 H_\mu(y)=y\oplus e_{(RL^{-1})\mu(y)}.                \tag{1.10}
\]

Then all column maps \(T_x\) are bijections and all row maps \(F_p\)
are permutations if and only if both \(G_\mu\) and \(H_\mu\) are
neighbor permutations.  Under that condition every \(F_p\) is affinely
conjugate to \(H_\mu\).

#### Proof

Toggling \(p_i\), where \(i=L^{-1}\mu(y)\), toggles coordinate
\(Li=\mu(y)\) of \(y\).  Thus a column map is, after the affine change
of variables (1.9), the restriction of \(G_\mu\) from one parity shore
to the other.  As \(x\) ranges over both parities, the two column shores
give both restrictions of \(G_\mu\).  Hence all columns are bijections
exactly when \(G_\mu\) is a permutation.

The same physical direction in an \(x\)-move toggles coordinate

\[
 R L^{-1}\mu(y)
\]

of \(y\).  Therefore (1.9) conjugates every row \(F_p\) to
\(H_\mu\), proving the row assertion and the final claim. \(\square\)

Thus a one-quotient affine construction does not face any further Latin
square equation: its exact content is precisely a pair of pointwise
direction-related neighbor permutations.  The trace-code requirement is
an additional condition on that pair.

## 2. An explicit orthogonal pair of recursive rainbow factors

Let (r=2^t\ge2).  Partition its coordinates into bottom sibling pairs,
and let (A_r) interchange the two coordinates in every such pair.

For (r=2), define

\[
 \rho_{G_2}(y)=
 \begin{cases}
  1,&|y|\equiv0\pmod2,\\
  2,&|y|\equiv1\pmod2,
 \end{cases}
 \qquad
 \rho_{H_2}(y)=A_2\rho_{G_2}(y).                       \tag{2.1}
\]

Thus (G_2) and (H_2) are the two orientations of the same (C_4).

Inductively write (r=2s) and (y=(u,v)\in Q_s\times Q_s).  Define

\[
 G_r(u,v)=
 \begin{cases}
   (G_s(u),v),&|u|+|v|\equiv0\pmod2,\\
   (u,G_s(v)),&|u|+|v|\equiv1\pmod2,
 \end{cases}                                           \tag{2.2}
\]

and define (H_r) by the identical recursion with (G_s) replaced by
(H_s).  Put (A_r=A_s\sqcup A_s).

### Theorem 2.1 (recursive orthogonal rainbow pair)

For every power of two (r\ge2):

1. (G_r) and (H_r) are neighbor permutations whose cycles are
   isometric (C_{2r})'s;
2. every cycle has direction word \(\pi\pi\) for a permutation \(\pi\)
   of the (r) coordinates;
3. both forward and reverse labelled-shadow maps are injective through
   depth (r/2); and
4. pointwise,
   \[
                         \rho_{H_r}(y)=A_r\rho_{G_r}(y).\tag{2.3}
   \]

#### Proof

The base case is immediate from (2.1).  Every cube edge reverses total
parity.  Hence (2.2) alternates left and right moves.  On an even state,

\[
 G_r^2(u,v)=(G_s(u),G_s(v)),                           \tag{2.4}
\]

and the same identity, with the two commuting moves in the opposite
order, holds on an odd state.  If the two component cycles have period
(2s), (2.4) gives exact period (4s=2r): an odd return is excluded by
parity, and an even return requires both component exponents to be a
multiple of (2s).

During the first (r=2s) moves, each component advances through (s)
consecutive edges of an isometric (C_{2s}).  Its directions are
therefore all (s) component coordinates exactly once.  The child first
half consequently uses every one of its (r) directions exactly once.
After those (r) moves, both component states are complemented.  The
component direction words and the parity scheduler then repeat, so the
second half has the same direction permutation.  This proves items 1--2.

For forward labelled shadows, use induction.  A window of length (2a)
splits into two component windows of length (a).  A window of length
(2a+1) splits into lengths (a+1,a), and the component containing
(a+1) directions identifies which side moved first.  If the child
window has length at most (s=r/2), both component depths are at most
(s/2).  The two component labelled shadows therefore recover (u,v)
by induction.  The inverse recurrence has the same alternating form, with
the parity choice interchanged, so the reverse proof is identical.

Finally, (2.3) holds at the base.  The two recursions choose the same
half at a given state, and (A_r) preserves each half and restricts there
to (A_s).  Induction proves (2.3). \(\square\)

Combining Theorems 1.1 and 2.1 gives an explicit solution of every parity
complete-mapping equation in which all (F_p)'s are themselves
two-sided coarse-shadow-injective through depth (r/2).

## 3. The hidden bottom-pair translation group

For a bottom sibling pair (B=\{i,A_ri\}), put

\[
                         z_B=e_i\oplus e_{A_ri}.        \tag{3.1}
\]

Let (Z_r\le Q_r) be the span of all (z_B).  Thus

\[
                              |Z_r|=2^{r/2}.            \tag{3.2}
\]

### Lemma 3.1 (direction stabilizer)

For every (z\in Z_r), every (y\in Q_r), and (K\in\{G_r,H_r\}),

\[
 \rho_K(y\oplus z)=\rho_K(y),
 \qquad
 K^j(y\oplus z)=K^j(y)\oplus z\quad(j\in\mathbb Z). \tag{3.3}
\]

#### Proof

For (r=2), adding (z_{\{1,2\}}=(1,1)) preserves parity, and both
directions in (2.1) depend only on parity.  For (r=2s), write
(z=(z_L,z_R)).  Every element of (Z_s) has even weight, so adding
(z) preserves the parity scheduler in (2.2).  In the half selected by
that scheduler, induction preserves the selected direction.  This proves
the first identity.  The successor identity and all its iterates follow
immediately. \(\square\)

The recursive interlacing also gives the following standard balance
property.

### Lemma 3.2 (one direction per bottom pair)

Every consecutive direction block of length (d\le r/2) in a cycle of
(G_r) or (H_r) meets every bottom sibling pair in at most one
coordinate.

#### Proof

At each recursion level, an interval is split between the two children
in sizes differing by at most one.  At the depth whose nodes are the
bottom two-coordinate pairs, a (d)-interval contributes either

\[
             \left\lfloor\frac d{r/2}\right\rfloor
 \quad\hbox{or}\quad
             \left\lceil\frac d{r/2}\right\rceil
\]

directions to each node.  For (d\le r/2), this is at most one. \(\square\)

The collision mechanism has a general affine form.  In the notation of
Proposition 1.2, define the translation stabilizer

\[
 \operatorname{Stab}(\mu)
 =\{z\in Q_r:\mu(y\oplus z)=\mu(y)\text{ for every }y\}. \tag{3.4}
\]

### Lemma 3.3 (affine stabilizer criterion)

Consider one affine-Latin trajectory with physical direction set (I).
If

\[
 e_{Li}\oplus e_{Ri}\in\operatorname{Stab}(\mu)
                         \qquad(i\in I),               \tag{3.5}
\]

then its aligned context-code fibre has multiplicity at least
(2^{|I|-1}).

#### Proof

For an even subset (S\subseteq I), put

\[
 s_S=\bigoplus_{i\in S}e_i,
 \qquad p'=p\oplus s_S,
 \qquad x'=x\oplus s_S.                               \tag{3.6}
\]

The new affine quotient differs from the old one by

\[
 Ls_S\oplus Rs_S
 =\bigoplus_{i\in S}(e_{Li}\oplus e_{Ri}),             \tag{3.7}
\]

which lies in the subgroup (3.4) by (3.5).  Hence the complete direction
trajectory, and in particular (I), is unchanged.  The changes in
(p,x) are supported on (I), while evenness of (S) preserves
(p\in E).  All (2^{|I|-1}) even subsets therefore give the same
context code. \(\square\)

For the recursive pair, take (L=1), (R=A_r), and
(mu=\rho_{G_r}).  Then (3.5) is exactly Lemma 3.1.

## 4. Exact aligned-trace collision

Install the affine family (1.3) using (A=A_r), (G=G_r), and
(H=H_r).  For (p\in E), (x\in Q_r), and (1\le d\le r/2), let

\[
 I=J_{p,d}(x)                                           \tag{4.1}
\]

be the set of the (d) consecutive coarse directions of (F_p).  Its
aligned physical context code is

\[
 \mathcal C_d(p,x)
 =\bigl(I,x|_{I^c},p|_{I^c}\bigr).                    \tag{4.2}
\]

### Theorem 4.1 (paired-erasure multiplicity)

Every fibre of (4.2) has cardinality at least (2^{d-1}).  The same is
true for the reverse aligned code and hence for both physical signs.

#### Proof

Under the conjugacy \(y=p\oplus A_rx\), an (F_p)-trajectory becomes an
(H_r)-trajectory.  Its (H_r)-direction at a step is the (A_r)-mate
of the corresponding (F_p)-direction.  Lemma 3.2 therefore says that
the (d) members of (I) lie in (d) distinct bottom sibling pairs.

For a subset (S\subseteq I), write

\[
 s_S=\bigoplus_{i\in S}e_i,
 \qquad z_S=s_S\oplus A_rs_S\in Z_r.                 \tag{4.3}
\]

If (|S|) is even, define

\[
                         p'=p\oplus s_S,
 \qquad                  x'=x\oplus s_S.              \tag{4.4}
\]

Then (p'\in E), and

\[
 p'\oplus A_rx'
 =(p\oplus A_rx)\oplus z_S
 =y\oplus z_S.                                         \tag{4.5}
\]

Lemma 3.1 says that the complete (H_r)-direction trajectory from the
last state is identical to that from (y).  Hence the (F_{p'})-window
from (x') has the same direction set (I).  Also (4.4) changes (p,x)
only on (I), so

\[
 x'|_{I^c}=x|_{I^c},
 \qquad p'|_{I^c}=p|_{I^c}.                           \tag{4.6}
\]

Thus all even subsets (S\subseteq I) give the same code.  They give
distinct starts, and there are (2^{d-1}) of them.

The reverse trajectories obey the same translation identity (3.3), and
Lemma 3.2 is cyclic and orientation-free.  The proof therefore applies
unchanged to the reverse code. \(\square\)

There are (2^{2r-1}) pairs ((p,x)\in E\times Q_r).  Consequently the
number of distinct aligned signed traces is at most

\[
                              2^{2r-d},                 \tag{4.7}
\]

and their collision excess is at least

\[
                   2^{2r-1}-2^{2r-d}.                 \tag{4.8}
\]

For (d\to\infty), (4.8) is asymptotically one half of the entire
physical cell.

### Corollary 4.2 (the affine orbit does not help)

The conclusion of Theorem 4.1 holds for every common affine conjugate of
the orthogonal pair \((G_r,H_r,A_r)\).

#### Proof

Let \(g(y)=\sigma y\oplus a\) be a cube automorphism and conjugate both
factors by \(g\).  Their pointwise relation becomes

\[
 \rho_{gH_rg^{-1}}(y)
   =(\sigma A_r\sigma^{-1})
       \rho_{gG_rg^{-1}}(y).                           \tag{4.9}
\]

The direction stabilizer becomes the translate subgroup \(\sigma Z_r\),
whose generators complement the two coordinates in the conjugated bottom
pairs.  Conjugating the proof of Theorem 4.1 gives the same
\(2^{d-1}\) invisible even-subset action. \(\square\)

## 5. Half-step traces do not remove the cut

A nonaligned physical window consists of some number (c) of completed
local pairs and at most two partial boundary pairs.  Its exact code is the
aligned completed-pair code together with the boundary directions and the
retained boundary endpoints.

Assume the whole coarse direction interval has length at most (r/2).
Lemma 3.2 then places the partial boundary directions in bottom pairs
different from the (c) completed pairs.  In the proof of Theorem 4.1,
restrict (S) to the completed directions.  The transformation (4.4)
does not touch either boundary pair, and so preserves all additional
half-step data.

### Corollary 5.1 (half-step multiplicity)

Every such half-step code with (c\ge1) completed pairs has multiplicity
at least

\[
                              2^{c-1}.                  \tag{5.1}
\]

Thus neither aligned nor half-step trace injectivity is obtained from the
orthogonal recursive affine construction.

## 6. The exact stronger affine gate

Theorem 1.1 isolates the useful positive algebra.  It is enough to find a
coordinate permutation (A) and two (C_{2r})-factors (G,H) with

\[
                              \rho_H=A\rho_G.           \tag{6.1}
\]

The complete-mapping equations then cost nothing further.  But physical
trace recovery asks for more than the ordinary labelled-shadow code of
(H).  If (K=D_d^H(y)) is its (d)-direction set, the physical code
reveals (y) automatically only outside

\[
                              K\cup A^{-1}K.            \tag{6.2}
\]

The missing finite theorem is therefore a **paired-erasure direction
code**: the map consisting of (K), the outside data in (6.2), and the
single parity constraint must be injective or have negligible aggregate
collision through the protected depths.

For the explicit recursive pair, (A=A_r), the sets (K,A^{-1}K) are
disjoint at shallow depth, but Lemma 3.1 supplies one independent hidden
translation for every touched bottom pair.  The parity constraint removes
only one of those bits, yielding exactly the lower bound (0.1).  Hence
mere disjointness of (K) and (A^{-1}K), ordinary two-sided rainbow
behaviour, and a Latin-square complete mapping are jointly insufficient.

No obstruction is proved here for an orthogonal pair satisfying (6.1)
with trivial direction-translation stabilizer.  Constructing such a pair
with a paired-erasure code, or proving that (6.1) itself forces a large
stabilizer, is the minimum remaining algebraic problem.
