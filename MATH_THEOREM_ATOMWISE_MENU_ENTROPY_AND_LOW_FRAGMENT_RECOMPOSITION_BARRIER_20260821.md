# Sourcewise residual hitting does not lift to whole atoms or cheap low-fragment recomposition

**Status (2026-08-21).** Every assertion below is proved. This note gives an
abstract counterexample to the missing implication in
`MATH_THEOREM_POLYLOG_FACTOR_MENU_RESIDUAL_HITTING_SELECTOR_GATE_20260821.md`.
A bank may have the strongest possible residual-hitting parameter, exact
uniform one-source marginals, optimal same-target pair control, and injective
target vectors inside every `B`-source atom, while its `K`-menu has the
following separation:

* a sourcewise selector covers `1-o(1)` of the targets;
* every whole-atom selector misses a fixed positive fraction; and
* even every selector made from `R` cyclic atom fragments misses a fixed
  positive fraction whenever

  \[
             R\log(KNB)=o(N).                       \tag{0.1}
  \]

At the physical scale `B=b^2`, `log N=Theta(b)`, and `K=polylog(b)`, whole
atoms have `R=N/b^2`, while the entire fragment range `R=o(N/b)` also
satisfies (0.1). Thus the sourcewise residual theorem alone cannot supply
the required atomwise coinstantiation. More precisely, cutting the selected
atoms into a total of `R=o(N/b)` cyclic pieces does not repair the logical
gap; when `B=b^2`, this is `o(b)` pieces per selected atom on average.

This is an implication barrier, not an impossibility theorem for the
Boolean product construction. The maps below are abstract layer maps; they
do not obey Boolean containment and are not asserted to arise from cyclic
orders. A successful physical proof must use additional structure that
rules out this example or a recomposition mechanism not controlled by the
number of cyclic fragments.

## 1. The atomwise menu model

Let `L` be a source set and `V` a target set with

\[
                         |L|=|V|=N.                 \tag{1.1}
\]

Let `B` divide `N`, put `m=N/B`, and partition `L` into atoms

\[
                  \mathcal A=\{A_1,\ldots,A_m\},
                  \qquad |A_a|=B.                  \tag{1.2}
\]

For every bank-atom pair `(j,a)`, equip `A_a` with an arbitrary cyclic
order of its `B` sources; the orders may differ between banks. For each
pair, independently choose a uniformly random injection

\[
                    \phi_{j,a}:A_a\hookrightarrow V.\tag{1.3}
\]

The candidate bank map is

\[
                  F_j(u)=\phi_{j,a}(u)\quad(u\in A_a).\tag{1.4}
\]

Thus one candidate atom assigns one target to all of its `B` source
positions, and the targets inside that atom are all distinct. Different
atoms of one bank may collide, as may different banks.

A **sourcewise selector** may retain `(u,F_j(u))` with a different `j` at
every source, subject only to source and target disjointness.

An **`R`-fragment atom selector** is a tuple of pairwise disjoint source
sets

\[
                       S_1,\ldots,S_K\subseteq L    \tag{1.5}
\]

such that, over all banks and atoms, the sets `S_j\cap A_a` can be written
as unions of at most `R` cyclic intervals in the corresponding prescribed
orders.
It retains all edges

\[
                     \{(u,F_j(u)):u\in S_j\}.       \tag{1.6}
\]

Sources outside the union may be discarded. A whole-atom selector is the
special case in which each nonempty `S_j\cap A_a` is the whole atom; it has
at most `m=N/B` fragments.

For whole-atom selection, the common partition in (1.2) removes the source
overlap constraint: each atom can be assigned independently to any one
bank. It is therefore already sufficient for disproving an implication
based only on sourcewise residual hitting and atom size.

## 2. Every fresh bank has exact residual hitting

### Proposition 2.1 (unit residual-hitting parameter)

For every deterministic `S\subseteq L` and `T\subseteq V`, one fresh bank
from (1.3)--(1.4) satisfies

\[
 \boxed{
 \mathbb E|F_j(S)\cap T|
 \ge |T|\left(1-e^{-|S|/N}\right).}                \tag{2.1}
\]

Hence it has `eta=1` residual hitting in the sense of Definition 2.1 of
the sourcewise menu theorem. Moreover, for all sources `u`, targets `v`,
and distinct sources `u,u'`,

\[
 \Pr(F_j(u)=v)={1\over N},\qquad
 \Pr(F_j(u)=v,F_j(u')=v)\le {1\over N^2}.          \tag{2.2}
\]

Thus the same-target pair constant is at most one, and is zero when the two
sources lie in the same atom.

#### Proof

Put `s_a=|S\cap A_a|`. For a fixed target `v`, the restriction of a
uniform injection on `A_a` to these `s_a` sources avoids `v` with exact
probability

\[
                         1-{s_a\over N}.             \tag{2.3}
\]

The atom injections are independent, so

\[
 \Pr(v\notin F_j(S))
   =\prod_{a=1}^m\left(1-{s_a\over N}\right)
   \le \exp\left\{-{|S|\over N}\right\}.           \tag{2.4}
\]

Summing the complementary probability over `v in T` proves (2.1).
Uniformity gives the first identity in (2.2). Two sources in the same atom
cannot hit the same target, while injections on different atoms are
independent, proving the second assertion. \(\square\)

By the sourcewise residual-hitting selector theorem, the greedy selector
on `K` independent banks therefore leaves `U_K` unmatched targets with

\[
 {\mathbb E U_K\over N}\le {1\over1+K},\qquad
 \Pr\left(U_K>{N\over\sqrt{1+K}}\right)
       \le {1\over\sqrt{1+K}}.                     \tag{2.5}
\]

In particular, if `K\to\infty`, the sourcewise menu contains a matching
covering `N-o(N)` targets with probability tending to one.

For comparison, when `B=o(N)`, one entire bank still has the ordinary
coupon-scale image.
Indeed, a fixed target is absent from all `m` atom images with probability

\[
                  \left(1-{B\over N}\right)^{N/B}
                         =e^{-1+O(B/N)}=e^{-1+o(1)}. \tag{2.6}
\]

Internal injectivity has removed collisions inside an atom but not the
mean-one collisions between the `N/B` atoms.

## 3. A fixed fragment selection has a constant deficit

Fix deterministic pairwise disjoint sets `S_1,...,S_K`; they may have been
specified by any list of atom intervals. For every pair `g=(j,a)`, put

\[
                    s_g=|S_j\cap A_a|.              \tag{3.1}
\]

The selected image of this group is a uniform `s_g`-subset of `V`, and
these subsets are independent over `g`. We have

\[
                    0\le s_g\le B,qquad
                    \sum_gs_g\le N.                 \tag{3.2}
\]

### Lemma 3.1 (uniform coupon deficit and exponential tail)

Assume `N>=2B`, and let

\[
                  Z=\left|\bigcup_{j=1}^K F_j(S_j)\right|.\tag{3.3}
\]

Then

\[
          \mathbb EZ\le(1-e^{-2})N,                 \tag{3.4}
\]

and, with

\[
                \gamma={e^{-2}\over2},\qquad
                c={e^{-4}\over8},                  \tag{3.5}
\]

one has

\[
        \boxed{
        \Pr\bigl(Z>(1-\gamma)N\bigr)\le e^{-cN}.}  \tag{3.6}
\]

#### Proof

For a fixed `v in V`, independence of the group images gives

\[
 p_0:=\Pr(v\notin \textstyle\bigcup_jF_j(S_j))
      =\prod_g\left(1-{s_g\over N}\right).         \tag{3.7}
\]

The elementary inequality

\[
                   \log(1-x)\ge-{x\over1-x}        \tag{3.8}
\]

and (3.2) imply

\[
 \log p_0
 \ge-{\sum_gs_g/N\over1-B/N}
 \ge-{1\over1-B/N}\ge-2.                          \tag{3.9}
\]

Thus `p_0>=e^{-2}`, proving (3.4).

For completeness, expose the selected images within each group one at a
time, sampling without replacement. The Doob martingale for `Z` has
increments of absolute value at most one. To see this, couple two possible
values at the next exposure by transposing those two target labels in the
unexposed part of the same group injection. The two final target unions
differ by at most one element. There are at most `N` exposures, so Azuma's
inequality gives

\[
 \Pr(Z-\mathbb EZ\ge t)\le\exp\left\{-{t^2\over2N}\right\}.\tag{3.10}
\]

Take `t=e^{-2}N/2`. Equations (3.4) and (3.10) give (3.6). \(\square\)

The estimate is deliberately coarse. When nearly all sources are selected
and `B=o(N)`, (2.6) shows that the natural missing fraction is `e^{-1}`;
only a fixed positive constant is needed below.

## 4. Entropy beats every low-fragment selector simultaneously

### Theorem 4.1 (atomwise low-fragment barrier)

Under (1.1)--(1.4), assume `N>=2B`. For any integer `R>=0`,

\[
 \boxed{
 \Pr\left(\begin{array}{c}
  \text{some `R`-fragment atom selector has}\cr
  \left|\bigcup_jF_j(S_j)\right|>(1-\gamma)N
 \end{array}\right)
 \le (R+1)(KNB)^R e^{-cN},}                        \tag{4.1}
\]

where `gamma,c` are the absolute constants in (3.5).

Consequently, if

\[
                   R\log(KNB)=o(N),                \tag{4.2}
\]

then with probability tending to one every such selector misses at least
`gamma N` targets.

#### Proof

A cyclic interval is specified by a bank, an atom, a starting position,
and a length. There are at most

\[
                         K\,{N\over B}\,B^2=KNB    \tag{4.3}
\]

such marked intervals. Hence at most `(R+1)(KNB)^R` ordered interval lists
of length at most `R` need be considered. This overcounts heavily: lists
may describe the same tuple, may overlap, or may fail source disjointness.
It is nevertheless a valid upper bound for all selectors.

For every fixed valid tuple, Lemma 3.1 bounds the probability of target
image greater than `(1-gamma)N` by `e^{-cN}`. A union bound proves (4.1),
including selectors chosen adaptively after all bank maps have been
revealed. Equation (4.2) makes the right side tend to zero. \(\square\)

### Corollary 4.2 (separation from the sourcewise theorem)

Let `K=K_N\to\infty` and let `R=R_N` satisfy (4.2). With probability
tending to one, the same realized `K`-menu simultaneously has both of the
following properties.

1. Its sourcewise menu graph contains a matching of size `N-o(N)`.
2. Every `R`-fragment atom selector covers at most `(1-gamma)N` targets.

In particular, deterministic menus with both properties exist.

#### Proof

The failure probability for the first assertion is at most
`1/sqrt(1+K)` by (2.5). The failure probability for the second tends to
zero by Theorem 4.1. Their union therefore has probability `o(1)`. \(\square\)

### Corollary 4.3 (whole atoms)

If

\[
                         \log(KNB)=o(B),            \tag{4.4}
\]

then every whole-atom selector misses at least `gamma N` targets with
probability tending to one, even though `K\to\infty` gives an
asymptotically perfect sourcewise selector.

#### Proof

A whole-atom selector uses at most `R=N/B` cyclic intervals. Substitution
in (4.2) gives (4.4). \(\square\)

For whole atoms alone, counting bank choices instead of interval endpoints
gives the sharp coupon-scale conclusion under a weaker hypothesis.

### Corollary 4.4 (even a subexponential atom menu retains coupon loss)

Assume `B=o(N)` and

\[
                         \log(K+1)=o(B).             \tag{4.5}
\]

Then, for every fixed `delta>0`, with probability tending to one **every**
whole-atom selector satisfies

\[
 \boxed{
 \left|\bigcup_jF_j(S_j)\right|
       \le (1-e^{-1}+\delta)N.}                    \tag{4.6}
\]

This includes selectors which discard atoms. Thus a generic menu needs
`log K=Omega(B)` even to escape the one-bank coupon scale by whole-atom
choice; `K=polylog(b)` is far below this threshold when `B=b^2`.

#### Proof

For each atom choose one of the `K` banks or discard it. There are at most
`(K+1)^m` such selectors. Fix one which retains `r<=m` atoms. A target is
absent with probability

\[
              \left(1-{B\over N}\right)^r
       \ge    \left(1-{B\over N}\right)^{N/B}
       =e^{-1+o(1)}.                                \tag{4.7}
\]

Consequently its expected image is at most
`(1-e^{-1}+o(1))N`. The exposure argument in Lemma 3.1, now with at most
`rB<=N` exposures, shows that its probability of exceeding the right side
of (4.6) is at most

\[
                         \exp\{-\delta^2N/8\}       \tag{4.8}
\]

for all sufficiently large `N`. A union bound over the selectors has log
failure probability at most

\[
             {N\over B}\log(K+1)-{\delta^2N\over8}
                         =-\Omega(N)                \tag{4.9}
\]

by (4.5). \(\square\)

### Corollary 4.5 (quantitative fragment lower bound)

Assume `log(KNB)=o(N)`. With probability tending to one, every fragment
selector whose target image is greater than `(1-gamma)N` uses at least

\[
              {cN\over4\log(KNB)}                  \tag{4.10}
\]

fragments, up to the immaterial integer rounding.

#### Proof

Put `R_0=floor(cN/(4log(KNB)))`. In (4.1), the interval-list factor has
logarithm

\[
             \log(R_0+1)+R_0\log(KNB)
                         \le {cN\over2}             \tag{4.11}
\]

for all sufficiently large `N`. The exceptional probability is therefore
at most `e^{-cN/2}`. Since selectors with fewer fragments are included in
the same event, the result follows. \(\square\)

## 5. The physical asymptotic scale and the exact surviving gate

Take

\[
 B=b^2,qquad \log N=\Theta(b),qquad
 K=\operatorname{polylog}(b).                     \tag{5.1}
\]

One may take `N` to be any multiple of `b^2` within `b^2` of the relevant
middle-layer volume; this changes an exponential central layer by `o(N)`.
Then

\[
 {N\over B}\log(KNB)=O\left({N\over b}\right)=o(N).\tag{5.2}
\]

Thus whole `b^2`-source atoms fail in the counterexample. More generally,
every

\[
                         R=o(N/b)                   \tag{5.3}
\]

satisfies (4.2). Conversely, any fragment selector which beats the fixed
deficit in this example must have

\[
                   R=\Omega\left({N\over\log(KNB)}\right)
                    =\Omega(N/b).                  \tag{5.4}
\]

The proved universal product-atom seam compiler spends `O(b)` output
positions per separately serialized fragment. Its established `o(N)`
range is therefore `R=o(N/b)`, exactly a range eliminated by this abstract
example. Equation (5.4) does **not** prove that every possible physical
recomposition has linear cost: `O(b)` is an upper bound for the known
compiler, not a lower bound for unknown compilers. It proves that the
sourcewise residual theorem plus the current fragment-and-seam mechanism
cannot by themselves establish coefficient one.

The construction can also be made vector-valued without changing the
argument. Give every `v in V` a private abstract chain

\[
                      v_1\prec v_2\prec\cdots\prec v_H              \tag{5.5}
\]

and let source `u` in bank `j` receive the whole chain indexed by
`F_j(u)`. Every candidate atom then assigns one nested target vector to all
of its sources, and Theorem 4.1 applies at each coordinate. What remains
absent is specifically the Boolean-containment and cyclic-order geometry.

Accordingly, a positive atomwise lift must add at least one genuinely new
ingredient:

* a factor-geometric theorem forcing a subexponential family of structured
  atom choices to cover almost every target, contrary to the generic
  injection model;
* a correlated construction of the `K` candidate banks which already
  aligns their target holes on whole atoms;
* or a physical recomposition whose complexity is not measured by
  `o(N/b)` cyclic fragments and whose total charged windows are still
  `o(N)`.

Residual hitting, uniform marginals, pair control, internal atom
injectivity, and nested target vectors alone are insufficient.

## 6. A deterministic overlap-graph cut for crossed atom banks

The preceding counterexample deliberately used a common source partition,
so choosing a different bank on each whole atom created no source conflict.
For two genuinely different candidate atom partitions there is an
additional exact rigidity.

Let `P` and `Q` be two partitions of the same `N=mB` sources into `m`
atoms of size `B`. Form the bipartite multigraph

\[
                         G=G(P,Q)                   \tag{6.1}
\]

with vertex classes `P,Q` and one edge `e_u` for every source `u`, joining
the two atoms which contain `u`. Thus `G` is `B`-regular, with parallel
edges allowed.

Choose whole-atom families `X subseteq P` and `Y subseteq Q`. A source is
good if it lies in exactly one selected atom and bad if it lies in zero or
two. Let

\[
 D(X,Y)=|\{u:{\bf1}_{P(u)\in X}+{\bf1}_{Q(u)\in Y}\ne1\}|.\tag{6.2}
\]

### Proposition 6.1 (component rigidity)

Put

\[
 Z=X\ \cup\ \{q\in Q:q\notin Y\}\subseteq V(G).   \tag{6.3}
\]

Then the bad sources are exactly the edge boundary of `Z`:

\[
 \boxed{D(X,Y)=|\partial_G Z|.}                    \tag{6.4}
\]

Consequently an exact source partition, `D(X,Y)=0`, chooses one whole bank
on each connected component of `G`. In particular, if `G` is connected,
the only exact selectors are

\[
                   (X,Y)=(P,\varnothing)
                   \quad\hbox{or}\quad
                   (\varnothing,Q).                \tag{6.5}
\]

#### Proof

On the edge belonging to `u`, membership of the `P` endpoint in `Z` is
`1_{P(u) in X}`, while membership of the `Q` endpoint is
`1-1_{Q(u) in Y}`. The edge crosses `Z` exactly when these two values
differ, equivalently when the two original selection indicators are equal.
That is precisely the zero-or-two condition in (6.2), proving (6.4).
Zero boundary means that `Z` is a union of connected components. On each
such component (6.3) says to take all its `P` atoms and no `Q` atoms, or
vice versa. \(\square\)

There is also a robust form. Define the normalized edge-expansion constant
by

\[
 h(G)=\min_{\varnothing\ne Z\subsetneq V(G)}
 { |\partial_G Z|\over
   B\min\{|Z|,2m-|Z|\}}.                           \tag{6.6}
\]

### Corollary 6.2 (expansion forces near-purity)

If `h(G)>=h_0>0`, then every whole-atom choice `(X,Y)` differs, in number
of selected or unselected atoms, from one of the two pure choices in (6.5)
on at most

\[
                         {D(X,Y)\over h_0B}          \tag{6.7}
\]

atoms. Hence it differs on at most `D(X,Y)/h_0` source positions.

If, at a fixed target layer, both complete banks have image at most
`(1-gamma)N`, then every choice with `D(X,Y)=o(N)` has target image at most

\[
                         (1-\gamma+o(1))N.          \tag{6.8}
\]

#### Proof

Equations (6.4) and (6.6) show that either `Z` or its complement has at
most `D/(h_0B)` vertices. By (6.3), changing exactly those atom decisions
gives the corresponding pure bank, proving (6.7). The selected atoms from
the non-dominant bank contribute at most `B` target occurrences each; the
selected atoms from the dominant bank contribute a subset of that full
bank's image. Thus the mixed image exceeds the dominant full-bank image by
at most `D/h_0=o(N)`, proving (6.8). \(\square\)

Proposition 6.1 is unconditional for the actual source partitions of any
two product-factor banks. What is not currently proved is a uniform lower
bound on `h(G)` for the physical conjugated partitions. Nor does the
two-bank cut by itself settle a simultaneous `K`-bank recomposition. It
identifies the exact new statistic: connected components and expansion of
the atom-overlap graphs, rather than sourcewise residual target expansion.

For an exactly source-disjoint `K`-bank selector, pairwise spectral
expansion gives a clean simultaneous version. Let
`\mathcal P_1,...,\mathcal P_K` be `B`-uniform partitions of the same
`N=mB` sources. For `j\ne k`, let `A_{jk}` be the `m\times m` biadjacency
matrix of their overlap multigraph and assume

\[
 \left\|{1\over B}A_{jk}\right\|_{{\bf1}^{\perp}\to{\bf1}^{\perp}}
                         \le\lambda.                \tag{6.9}
\]

### Proposition 6.3 (pairwise expansion forces one-bank dominance)

From partition `j`, choose an atom family `X_j` and let `S_j` be its source
union. Suppose the `S_j` are pairwise disjoint. Put

\[
 x_j={|S_j|\over N}={|X_j|\over m},\qquad
 s=\sum_{j=1}^Kx_j.                                \tag{6.10}
\]

Then, for every `j\ne k`,

\[
                         x_jx_k\le\lambda^2.        \tag{6.11}
\]

If `j_*` maximizes `x_j` and `s>0`, then

\[
 \boxed{
 \sum_{j\ne j_*}x_j
       \le {K(K-1)\lambda^2\over s}.}              \tag{6.12}
\]

Consequently, if `s=1-o(1)` and `K\lambda=o(1)`, all but `o(N)` selected
sources come from one bank. If every full bank has target image at most
`(1-gamma)N`, the selected atoms also have target image at most
`(1-gamma+o(1))N`.

#### Proof

The bipartite expander-mixing identity following from (6.9) is

\[
 \left|{|S_j\cap S_k|\over N}-x_jx_k\right|
 \le\lambda\sqrt{x_j(1-x_j)x_k(1-x_k)}.            \tag{6.13}
\]

The left intersection is empty. Therefore

\[
 x_jx_k
 \le\lambda\sqrt{x_jx_k(1-x_j)(1-x_k)}
 \le\lambda\sqrt{x_jx_k},                          \tag{6.14}
\]

which proves (6.11), including the zero case. Write
`M=x_{j_*}`. Since `M>=s/K`, (6.11) gives

\[
 \sum_{j\ne j_*}x_j
 \le{(K-1)\lambda^2\over M}
 \le{K(K-1)\lambda^2\over s},                     \tag{6.15}
\]

proving (6.12). The dominant selected atoms contribute a subset of their
full bank image, and every non-dominant selected source contributes at most
one additional target. This proves the last assertion. \(\square\)

At the benchmark value `lambda=O(B^{-1/2})`, taking `B=b^2` and
`K=polylog(b)` lies in the rigidity regime `Klambda=o(1)`. Such a spectral
bound is not asserted for the physical factor partitions. The conditional
calculation shows, however, that making candidate source partitions
random-like in this precise sense would obstruct whole-atom mixing rather
than justify it.

For the two-block product atoms, the overlap statistic has an exact local
factorization. Fix one payload profile `r`. In a candidate bank on `A`, let

\[
              \mathcal D_A=(D_i)_{i\in I},qquad |D_i|=b,             \tag{6.16}
\]

be the partition of the rank-`r` subsets into cyclic-window decks. Let
`\mathcal D'_A=(D'_{i'})` be the corresponding local partition in a second
bank. On `B`, write `\mathcal E_B=(E_j)` and `\mathcal E'_B=(E'_{j'})`
for the rank-`(b-r)` deck partitions. Define the local overlap matrices

\[
 M_A(i,i')=|D_i\cap D'_{i'}|,qquad
 M_B(j,j')=|E_j\cap E'_{j'}|.                      \tag{6.17}
\]

### Proposition 6.4 (Kronecker factorization of physical atom overlaps)

Assume `gcd(r,b)=1`; in the intended application `b` is prime and
`1<=r<=b-1`.

Identify a split middle source with its pair `(X,Y)`, where
`X subseteq A`, `Y subseteq B`, `|X|=r`, and `|Y|=b-r`. The product atom
indexed by `(i,j)` has source set `D_i times E_j`. Hence its overlap with
the second-bank atom `(i',j')` is

\[
 \boxed{
 |(D_i\times E_j)\cap(D'_{i'}\times E'_{j'})|
       =M_A(i,i')M_B(j,j').}                       \tag{6.18}
\]

Equivalently, the profile-`r` atom-overlap biadjacency matrix is

\[
                         M_r=M_A\otimes M_B,        \tag{6.19}
\]

and

\[
                    {M_r\over b^2}
       =\left({M_A\over b}\right)\otimes
        \left({M_B\over b}\right).                \tag{6.20}
\]

In particular, its normalized singular values are exactly all pairwise
products of the normalized local singular values. Atom-overlap graphs for
different payload profiles have no common source edges, so the complete
bank-overlap matrix is the direct sum of the matrices `M_r`.

#### Proof

Under `gcd(r,b)=1`, the torus enumeration of a product atom lists every pair consisting of one
local `r`-window in `D_i` and one local `(b-r)`-window in `E_j`, exactly
once. Thus the middle source set is their Cartesian product. Intersections
of Cartesian products factor, proving (6.18) and (6.19). Every local deck
has `b` members and the primed decks partition the same local layer, so
every row and column sum of `M_A,M_B` is `b`; this gives the normalization
in (6.20). The singular values of a Kronecker product are the pairwise
products of those of its factors. Finally, the split profile of a source is
intrinsic, proving the direct-sum assertion. \(\square\)

Thus the two-bank component and expansion gate is computable entirely from
the intersections of the two local cyclic-order factors. In particular,
ordinary exact factorhood supplies the row and column sums `b` but gives no
bound on component count or nontrivial singular values. Those are new
coinstantiation data, not consequences of Baranyai--Katona coverage.

## 7. Audit scope

The companion H100 checker
`scratch/audit_atomwise_menu_entropy_barrier_20260821.py` verifies the
exact avoidance identity (2.4) exhaustively on small atom partitions,
checks (3.7)--(3.9) for every integer group profile in its audit range,
verifies the overlap-graph identity (6.4) for every atom selection in a
small crossed pair, and constructs finite random menus comparing sourcewise
maximum matching with the best whole-atom choice. The finite experiment is
diagnostic only. All asymptotic assertions above follow from the proofs and
not from the checker.
