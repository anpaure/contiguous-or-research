# Protected Ore stability: the sharp metric scale and exact positive-defect block gluing

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that
Hamming stability around the zero-clique-defect families has the optimal
general scale `Theta(m sigma)`, not `O(sigma)` and not `O(b)`.  It then
replaces the false metric heuristic by an exact margin-gluing identity for
overlapping complete support blocks.  Combined with the frozen constrained
reservoir margins and Hamming Lipschitz theorem, this closes a nonempty and
asymptotically broad family of Johnson-connected cuts with `b>0`.  It does
not classify arbitrary positive-defect cuts.

No computation, search, or finite solver result is used.

## 0. Setting

Fix `m>=3`, put

\[
 k=m-1,\qquad \Omega=[2m-1],\qquad
 \mathcal L={\Omega\choose k},\qquad W=|\mathcal L|,
\]

and let `P` be any protected subgraph of the middle-levels incidence graph
with maximum degree at most two.  For `A subseteq mathcal L`, retain the
frozen notation

\[
 \mu_P(A)=\sigma(A)-\lambda_P(A),
\]

where `A` satisfies the protected Ore inequality exactly when
`mu_P(A)>=0`.  Also retain

\[
 b(A)=\sum_{U:2\le a_U\le m-1}(m-a_U).
\]

Let `mathfrak E` be the zero-defect class.  By the frozen equality
classification, its members are exactly

\[
 E=\mathop{\dot\bigcup}_i {S_i\choose k},
 \qquad |S_i\cap S_j|\le k-2\quad(i\ne j).
\tag{0.1}
\]

Write

\[
 d_{\mathfrak E}(A)=\min_{E\in\mathfrak E}|A\triangle E|.
\tag{0.2}
\]

## 1. The best possible general Hamming scale is `Theta(m sigma)`

### Theorem 1.1 (universal metric upper bound)

For every `A subseteq mathcal L`,

\[
 \boxed{
 d_{\mathfrak E}(A)
 \le \min\{|A|,W-|A|\}
 \le {m(m-1)\over 2m-1}\,\sigma(A).}
\tag{1.1}
\]

#### Proof

Both the empty and full lower shores belong to `mathfrak E`, proving the
first inequality.  The frozen weighted-boundary and Johnson spectral
inequalities give

\[
 \sigma(A)\ge {2\over m(m-1)}|\partial_JA|
 \ge {2(2m-1)\over m(m-1)}
       {|A|(W-|A|)\over W}.
\tag{1.2}
\]

If `t=min{|A|,W-|A|}`, then

\[
 {|A|(W-|A|)\over W}={t(W-t)\over W}\ge {t\over2}.
\]

Substitution in (1.2) proves the second inequality. \(\square\)

The factor of order `m` cannot be removed.

### Theorem 1.2 (principal-star lower bound)

Fix one coordinate `c in Omega`, and put

\[
 \mathcal A_c=\{X\in\mathcal L:c\in X\},
 \qquad M=|\mathcal A_c|={2k\choose k-1}.
\tag{1.3}
\]

Then

\[
 \sigma(\mathcal A_c)={2\over k}M,
\tag{1.4}
\]

whereas

\[
 \boxed{
 d_{\mathfrak E}(\mathcal A_c)
 \ge
 \left(1-{(k+1)^2\over4k(k+2)}\right)M.}
\tag{1.5}
\]

Consequently

\[
 {d_{\mathfrak E}(\mathcal A_c)\over\sigma(\mathcal A_c)}
 \ge {k\over2}
 \left(1-{(k+1)^2\over4k(k+2)}\right)
 =\left({3\over8}+o(1)\right)m.
\tag{1.6}
\]

Thus the order `m sigma` in (1.1) is sharp.

#### Proof

The formula (1.4) is the principal-up-star identity with one prescribed
coordinate.

Take an arbitrary `E in mathfrak E` and write it as in (0.1).  Because the
blocks in (0.1) are disjoint,

\[
 |\mathcal A_c\triangle E|
 =M-\sum_i g(S_i),
 \qquad
 g(S)=2\left|{S\choose k}\cap\mathcal A_c\right|
      -{ |S|\choose k}.
\tag{1.7}
\]

Blocks not containing `c` have `g(S)<=0` and may be discarded when
upper-bounding the sum.  If `c in S`, put `r=|S|-1`.  Pascal's identity
gives

\[
 g(S)={2k-r-1\over k}{r\choose k-1}.
\tag{1.8}
\]

Only the positive terms matter.  Write

\[
 x=r-k+2,
\]

so `1<=x<=k` on that range.  Then

\[
 g(S)=
 {x(k+1-x)\over k(k-1)}{r\choose k-2}
 \le{(k+1)^2\over4k(k-1)}{r\choose k-2}.
\tag{1.9}
\]

For two supports containing `c`, (0.1) implies

\[
 |(S_i\setminus\{c\})\cap(S_j\setminus\{c\})|\le k-3.
\]

Their `(k-2)`-shadows are therefore disjoint.  All lie on the `2k`
coordinates different from `c`, so (1.9) yields

\[
 \sum_i g(S_i)
 \le{(k+1)^2\over4k(k-1)}{2k\choose k-2}
 ={(k+1)^2\over4k(k+2)}M.
\tag{1.10}
\]

Equations (1.7)--(1.10) prove (1.5), and (1.4) then gives (1.6).
\(\square\)

The principal star is already known to satisfy the protected Ore
inequality.  The point of Theorem 1.2 is different: it proves that a
metric argument using only proximity to the equality class necessarily
loses a factor of order `m`.  Principal stars must be treated as a second
extremal geometry, exactly as in the frozen reservoir proof.

## 2. Clique defect does not control distance to the equality class

The failure for `b` is much stronger: even a polynomial factor in `m`
cannot work.

### Theorem 2.1 (two-block counterexample)

Let `m>=5` be odd, choose a set `H` of size `m-2`, and partition
`Omega\setminus H` into two sets `P_0,Q_0` of the common size

\[
 p={m+1\over2}.
\]

Put

\[
 S=H\cup P_0,\qquad T=H\cup Q_0,
 \qquad
 A={S\choose k}\mathbin{\dot\cup}{T\choose k},
\tag{2.1}
\]

and

\[
 B={|S|\choose k}={|T|\choose k}.
\]

Then `A` is Johnson-connected,

\[
 \boxed{b(A)=(m-2)p^2=O(m^3),}
\tag{2.2}
\]

but

\[
 \boxed{d_{\mathfrak E}(A)\ge {B\over p}=\exp(\Theta(m)).}
\tag{2.3}
\]

In particular, for every fixed `C`, no universal inequality

\[
 d_{\mathfrak E}(A)\le m^C b(A)
\]

is possible, even on Johnson-connected positive-defect cuts.

#### Proof

Each block in (2.1) is Johnson-connected.  For every
`x in P_0,y in Q_0`, the two facets `H+x` and `H+y` are adjacent, so their
union is connected.

An owner contained in `S` or `T` is full.  An owner meeting both blocks
in at least one facet must be

\[
 U=H\cup\{x,y\},\qquad x\in P_0,\quad y\in Q_0,
\]

and it has exactly two selected facets.  All other nonempty owner fibres
have size one.  Thus there are exactly `p^2` partial fibres, all of size
two, proving (2.2).

We need one elementary packing observation.  Let `E` be an equality
family with support blocks `R_i`, and fix a set
`Z` of size

\[
 z=k-1+p.
\]

If no `R_i` contains `Z`, put `Q_i=R_i intersect Z`.  The families
`{Q_i choose k-1}` are disjoint, because
`|R_i intersect R_j|<=k-2`.  Also `|Q_i|<=z-1`; hence

\[
\begin{aligned}
 \left|E\cap{Z\choose k}\right|
 &=\sum_i{|Q_i|\choose k}\\
 &\le {z-k\over k}\sum_i{|Q_i|\choose k-1}\\
 &\le {z-k\over k}{z\choose k-1}
 ={p-1\over p}{z\choose k}.
\end{aligned}
\tag{2.4}
\]

Now suppose, for contradiction, that `|A symmetric-difference E|<B/p`.
Then fewer than `B/p` members of each of the two blocks in (2.1) are
missing from `E`.  By (2.4), some support `R_i` contains `S`, and
some support `R_j` contains `T`.

They cannot be distinct, because their intersection would contain
`H`, of size `k-1`, contradicting (0.1).  Therefore one support contains
`S union T=Omega`, so it is `Omega` itself.  The separation condition in
(0.1) then leaves no other nonempty block, and `E=mathcal L`.

Finally,

\[
 {W\over B}
 =\prod_{j=1}^{p}{|S|+j\over |S|+j-k}
 \ge\left({2m-1\over m}\right)^p
 >2+{1\over p}
\tag{2.5}
\]

for `m>=5`.  Hence

\[
 |\mathcal L\triangle A|=W-2B>{B\over p},
\]

the final contradiction.  This proves (2.3). \(\square\)

Theorem 2.1 explains why the maximal complete support blocks must be
kept rather than rounded away.  A partial owner meets any one such block
in at most one facet, but a polynomial number of cross owners can couple
two exponentially large blocks.

## 3. Exact margin gluing across complete support blocks

The same decomposition which defeats Hamming stability admits an exact
nonmetric argument.

Let `S_1,...,S_h subseteq Omega` satisfy

\[
 |S_i|\ge k,qquad |S_i\cap S_j|\le k-1\quad(i\ne j),
\tag{3.1}
\]

and put

\[
 A_i={S_i\choose k},qquad A=\mathop{\dot\bigcup}_{i=1}^h A_i.
\tag{3.2}
\]

The blocks are disjoint.  An owner not contained in one support meets
each block in at most one facet.  For such an owner define

\[
 q_U=a_U,qquad d_U=d_P(U),qquad
 t_U=e_P(U,A).
\tag{3.3}
\]

Call it a **cross owner** when `q_U>=2`, and set

\[
 \psi_P(U)=
 \begin{cases}
  q_U-2,&d_U=0,\\
  q_U-1-t_U,&d_U=1,\\
  0,&d_U=2.
 \end{cases}
\tag{3.4}
\]

Every value in (3.4) is nonnegative.

### Theorem 3.1 (exact block-gluing identity)

For every family (3.2),

\[
 \boxed{
 \mu_P(A)=\sum_{i=1}^h\mu_P(A_i)
           -\sum_{U:q_U\ge2}\psi_P(U).}
\tag{3.5}
\]

Consequently, if certified lower margins `Delta_i` satisfy

\[
 \mu_P(A_i)\ge\Delta_i
\]

and

\[
 \sum_i\Delta_i\ge\sum_{U:q_U\ge2}\psi_P(U),
\tag{3.6}
\]

then the positive-defect union `A` satisfies every protected Ore demand
represented by this cut.

#### Proof

The terms `-2|A|` in `sigma` are additive over the disjoint blocks.  An
owner internal to one support and an owner meeting at most one block have
exactly the same local contribution on the two sides of (3.5).  It remains
to inspect one cross owner.

For each separate block it has `a=1`.  If the unique selected facet of
block `i` is protected, write `epsilon_i=1`; otherwise write
`epsilon_i=0`.  Then

\[
 \sum_i\epsilon_i=t_U.
\]

The separate `sigma` owner contribution is `q_U`, while the union
contribution is two.  The separate `lambda` contribution is zero when
`d_U<=1`; when `d_U=2`, it is

\[
 \sum_i(1-\epsilon_i)=q_U-t_U.
\]

On the union, `a=q_U>=2` and the number of protected complement incidences
is `d_U-t_U`, so its `lambda` contribution is exactly `d_U-t_U`.
Therefore

\[
 \mu_U(A)-\sum_i\mu_U(A_i)
 =
 \begin{cases}
  2-q_U,&d_U=0,\\
  1-q_U+t_U,&d_U=1,\\
  0,&d_U=2,
 \end{cases}
\]

which is `-psi_P(U)`.  Summing proves (3.5), and (3.6) is immediate.
\(\square\)

The singleton partition `A=dotcup_(X in A){X}` is always an admissible
instance of (3.2).  More generally, any partition of `A` into complete
support blocks may be used.  A partial owner meets each such block in at
most one facet: two facets from one block force the owner to lie inside
that block's support and hence force all its facets into the block.  Thus
(3.5) is an exact version of the maximal-full-clique-component heuristic;
maximalization is useful only because it replaces many singleton margins
by one much larger certified block margin.

There is no monotonic relation between the gluing penalty and `b(A)`:
at one cross owner the former grows with `q_U`, while the latter equals
`m-q_U` when `q_U<m`.  This is the exact reason a scalar bound in terms
of `b` alone cannot replace (3.5).

### Corollary 3.2 (two blocks)

Suppose `S intersect T=H` has size `k-1`, and put

\[
 p=|S\setminus H|,\qquad q=|T\setminus H|.
\]

For

\[
 A={S\choose k}\mathbin{\dot\cup}{T\choose k}
\]

one has

\[
 \boxed{b(A)=(m-2)pq.}
\tag{3.7}
\]

Moreover, the exact gluing penalty is the number of cross owners

\[
 U=H\cup\{x,y\},\qquad x\in S\setminus H,\quad y\in T\setminus H,
\]

which have protected degree one and whose protected facet lies outside
`A`.  In particular,

\[
 \boxed{
 \mu_P(A)\ge\mu_P({S\choose k})+
                  \mu_P({T\choose k})-pq.}
\tag{3.8}
\]

#### Proof

Every cross owner has `q_U=2`; these are exactly the `pq` displayed
owners.  Formula (3.4) is then one precisely when `d_U=1,t_U=0`, and is
zero in every other case.  Formula (3.7) follows because every cross
owner has fibre size two.  Apply Theorem 3.1. \(\square\)

## 4. A closed positive-defect regime for the constrained reservoir

Now specialize to the constrained common-`G_2` resident reservoir in
`MATH_THEOREM_COMMON_CORE_EQUALITY_CUTS_CONSTRAINED_SPREAD_COMPLETE_20260804.md`,
frozen SHA
`b07682e2aee1b5d3017e96fc1483b17a91be8d249673a2c4b49433610867eb5e`.

For one support `S`, write `t=|S|`, `u=2m-1-t`, and let
`Δ(S)` denote either certified margin from that theorem:

\[
 \Delta(S)=
 \left({u(m-2)\over m}-(R_m+7)\right){t\choose k}
\tag{4.1}
\]

in its broad range, and

\[
 \Delta(S)={u(m-2)\over m}{t\choose k}-M_P
\tag{4.2}
\]

in its near-full range.  These satisfy
`mu_P({S choose k})>=Delta(S)` in their stated ranges.

### Theorem 4.1 (positive-defect two-block closure and neighbourhood)

Let `S,T` meet in `m-2` points, and retain `p,q` from Corollary 3.2.
If

\[
 \boxed{\Delta(S)+\Delta(T)\ge pq,}
\tag{4.3}
\]

then the Johnson-connected cut

\[
 A_0={S\choose k}\mathbin{\dot\cup}{T\choose k},
 \qquad b(A_0)=(m-2)pq>0,
\]

is safe.  More generally, every `A` with

\[
 r=|A\triangle A_0|
\]

is safe whenever

\[
 \boxed{
 \Delta(S)+\Delta(T)-pq\ge(2m+2)r.}
\tag{4.4}
\]

#### Proof

Equation (4.3) and Corollary 3.2 give `mu_P(A_0)>=0`.  In fact

\[
 \mu_P(A_0)\ge\Delta(S)+\Delta(T)-pq.
\]

The frozen Hamming theorem says that `mu_P` changes by at most `2m+2`
per toggled lower vertex.  This proves (4.4). \(\square\)

This regime is nonempty with room to spare.  For example, take
`|S|=|T|=m` and `|S intersect T|=m-2`.  Then `p=q=2`,

\[
 b(A_0)=4(m-2),
\]

and for all sufficiently large `m`, (4.1) gives the common lower margin

\[
 \Delta_0=
 \left({(m-1)(m-2)\over m}-(R_m+7)\right)m.
\tag{4.5}
\]

Thus `A_0` and its entire Hamming ball of radius

\[
 \boxed{
 \left\lfloor{2\Delta_0-4\over2m+2}\right\rfloor}
 =\Theta(m)}
\tag{4.6}
\]

are safe positive-defect cuts.  The two exponentially large blocks in
Theorem 2.1 are also closed by (4.3) for all sufficiently large `m`, since
their certified block margins are exponential while `pq=O(m^2)`.

There is also a criterion which applies directly to non-block families.
Retain the exceptional set

\[
 \mathcal B=\{(K\setminus G_2)\cup R:R\in{E\choose2}\}
\tag{4.7}
\]

from the constrained reservoir theorem, and put

\[
 D_m=m-R_m-6.
\tag{4.8}
\]

For an arbitrary cut `A`, define its singleton-partition penalty

\[
 \Psi_{\rm sing}(A)=
 \sum_{U:a_U\ge2}
 \begin{cases}
  a_U-2,&d_P(U)=0,\\
  a_U-1-e_P(U,A),&d_P(U)=1,\\
  0,&d_P(U)=2.
 \end{cases}
\tag{4.9}
\]

### Theorem 4.2 (arbitrary-cut singleton-margin criterion)

For all sufficiently large `m`, every cut `A` satisfying

\[
 \boxed{
 \Psi_{\rm sing}(A)\le D_m|A\setminus\mathcal B|}
\tag{4.10}
\]

is safe.

If, additionally, `A` has no full owner and every partial owner has
`a_U<=r_0<m`, then the simpler sufficient condition

\[
 \boxed{
 {r_0-1\over m-r_0}\,b(A)
 \le D_m|A\setminus\mathcal B|}
\tag{4.11}
\]

implies (4.10).  In the especially transparent two-facet regime
`a_U in {0,1,2}`, this becomes

\[
 \boxed{
 {b(A)\over m-2}\le D_m|A\setminus\mathcal B|.}
\tag{4.12}
\]

Since the number `n_2` of two-facet owners satisfies
`2n_2<=m|A|`, every such cut is safe under the concrete density condition

\[
 \boxed{
 |A\setminus\mathcal B|\ge {m\over2D_m}|A|.}
\tag{4.13}
\]

The coefficient on the right tends to `1/2`.  Thus, asymptotically, every
two-facet positive-defect cut with at least slightly more than half of its
vertices outside the exceptional fixed-`G_2` face is closed.

These are genuine positive-defect closures and do not assume that `A` is
a union of large complete blocks.

#### Proof

For every singleton `X`, one has `sigma({X})=m-2`.  The frozen singleton
envelope gives

\[
 \lambda_P(\{X\})\le R_m+4
 \quad(X\notin\mathcal B),
\]

while the exact common-`G_2` singleton theorem gives nonnegative margin on
`mathcal B`.  Therefore

\[
 \sum_{X\in A}\mu_P(\{X\})
 \ge D_m|A\setminus\mathcal B|.
\tag{4.14}
\]

Apply Theorem 3.1 to the singleton partition.  Its cross penalty is
exactly (4.9), so (4.10) proves safety.

Now suppose the hypotheses preceding (4.11) hold.  For every partial
owner,

\[
 \psi_P(U)\le a_U-1\le r_0-1,
 \qquad
 m-a_U\ge m-r_0.
\]

Hence

\[
 \Psi_{\rm sing}(A)
 \le {r_0-1\over m-r_0}
      \sum_{U:2\le a_U\le r_0}(m-a_U)
 ={r_0-1\over m-r_0}b(A).
\]

This proves (4.11); setting `r_0=2` gives (4.12).  Finally
`b(A)/(m-2)=n_2<=m|A|/2`, so (4.13) implies (4.12). \(\square\)

## 5. Exact frontier

The results establish the following proof-safe boundary.

1. Hamming distance to `b=0` is controlled universally by `O(m sigma)`,
   and this order is sharp.
2. Neither `b` nor any polynomial multiple of `b` controls that distance,
   even for Johnson-connected cuts.
3. Large maximal complete blocks should therefore not be destroyed in a
   repair argument.  Their individual certified margins glue by the exact
   local identity (3.5).
4. This closes all complete-block unions satisfying (3.6), and by Hamming
   Lipschitz it closes explicit positive-defect neighbourhoods around
   them.  The singleton specialization additionally closes the arbitrary
   low-multiplicity regime (4.11).

The remaining protected-Ore family consists of cuts with a genuinely
non-block residual: after extracting useful complete support blocks, the
uncovered selected facets are not paid by the block margins and cross-owner
penalty alone.  A full proof still needs an erosion/partial-component
theorem for that residual.  No claim about endpoint collars, component
placement, or the common cap is made here.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| exact shadow identity/equality classification | `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |
| constrained reservoir margins and Hamming Lipschitz theorem | `MATH_THEOREM_COMMON_CORE_EQUALITY_CUTS_CONSTRAINED_SPREAD_COMPLETE_20260804.md` | `b07682e2aee1b5d3017e96fc1483b17a91be8d249673a2c4b49433610867eb5e` |
