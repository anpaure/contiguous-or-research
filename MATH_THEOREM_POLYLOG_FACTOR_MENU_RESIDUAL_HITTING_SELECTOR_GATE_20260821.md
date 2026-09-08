# Polylogarithmic factor menus beat coupon loss exactly when future banks hit residual targets

**Status (2026-08-21).**  Every assertion below is proved.  This note gives
an exact fixed-layer criterion for the proposed correlated escape from the
independent-conjugation coupon barriers.

At one upper offset, regard each candidate factor bank as a single-valued
map from middle sources to upper targets.  A selector may inspect `K`
independent candidate banks and retain at most one image for each source.
If every fresh bank hits arbitrary residual source/target sets at a fixed
positive fraction of the ideal independent rate, a greedy source-disjoint
selector misses at most an `O(1/K)` fraction of the layer.  Thus
`K=polylog(b)` is more than enough in the abstract sourcewise menu graph.
Turning that sourcewise selection into physical output without paying for
`K` banks requires an additional atomwise coinstantiation theorem.

The criterion is genuinely additional.  Independent banks, uniform
one-source marginals, and exact mean target load do not imply it: a bank can
collapse every source onto one uniformly random target.  Then `K` banks
have at most `K` usable targets.  For physical factor banks, the remaining
question is therefore a residual image-expansion theorem, not another
first-moment calculation.

This is a fixed-layer theorem.  The selected edges at different offsets
need not be nested parts of common chains, and no simultaneous all-`q`
coinstantiation or serialization is claimed.

## 1. The exact menu-selector model

Let `L` be a source set and `R` a target set, with

\[
 \ell=|L|\ge n=|R|.                                \tag{1.1}
\]

A candidate bank is a single-valued map

\[
 F:L\longrightarrow R.                             \tag{1.2}
\]

The menu consists of independent random maps
`F_1,...,F_K`, not necessarily with independent values inside one map.
Its bipartite menu graph contains the edge `(u,F_j(u))` for every source
`u` and bank `j`.

A **source-disjoint selector** is a matching in this menu graph.  It pays
for only its selected edges: even though `K` candidate descriptions were
available, each physical source is retained at most once.  Whether the
selected edges can subsequently be serialized is a separate question.

The following deficiency formula is immediate from Hall's theorem and
records the completely exact gate:

\[
 n-\nu(G)=
 \max_{T\subseteq R}\bigl(|T|-|N_G(T)|\bigr)_+.    \tag{1.3}
\]

Thus a menu leaves at most `epsilon n` targets unmatched exactly when

\[
 |N_G(T)|\ge |T|-\varepsilon n
 \quad\hbox{for every }T\subseteq R.               \tag{1.4}
\]

Checking (1.4) directly is difficult.  Residual hitting is a sufficient
probabilistic condition designed for a greedy proof.

## 2. Residual target hitting

Run the following algorithm.  Initially every source and target is unused.
In round `j`, reveal `F_j` only on the currently unused source set `S`.
Let `T` be the currently unmatched targets.  For every distinct target in

\[
 F_j(S)\cap T                                      \tag{2.1}
\]

choose one proposing source and add that edge to the matching.  These
chosen sources are automatically distinct: a single-valued map cannot send
one source to two different targets.

### Definition 2.1 (eta-residual hitting)

For `0<eta<=1`, a fresh-bank law has **eta-residual hitting** if, for every
deterministic pair `S subseteq L`, `T subseteq R` satisfying

\[
 |S|\ge \ell-n+|T|,                                \tag{2.2}
\]

one has

\[
 \boxed{
 \mathbb E|F(S)\cap T|
 \ge |T|\left(1-\exp\{-\eta |S|/n\}\right).}      \tag{2.3}
\]

Because the candidate banks are independent, the same inequality holds
conditional on the entire preceding greedy history: the resulting `S,T`
are then fixed and the next bank remains fresh.

### Theorem 2.2 (source-disjoint residual-hitting selector)

Suppose the `K` candidate banks are independent and each satisfies
`eta`-residual hitting.  Let `U_K` be the number of unmatched targets after
the greedy selector.  Put

\[
 \delta={\ell-n\over n}.                            \tag{2.4}
\]

Then

\[
 \boxed{
 {\mathbb EU_K\over n}
 \le \min\left\{{1\over1+\eta K},
                  e^{-\eta\delta K}\right\}.}      \tag{2.5}
\]

In particular, if `eta K->infinity`, the selector matches
`(1-o(1))n` targets.  Moreover

\[
 \Pr\left(U_K>{n\over\sqrt{1+\eta K}}\right)
 \le {1\over\sqrt{1+\eta K}}.                     \tag{2.6}
\]

#### Proof

If `u` targets are unmatched, the current matching uses `n-u` sources, so
the unused source count is exactly

\[
 s=\ell-(n-u)=\ell-n+u.                            \tag{2.7}
\]

Thus (2.2) holds with equality.  By (2.3), conditional on the history,

\[
 \mathbb E(U_{j+1}\mid U_j=u)
 \le u\exp\{-\eta(\delta+u/n)\}.                  \tag{2.8}
\]

On `[0,1]` the function `x exp(-eta x)` is concave when `0<eta<=1`.
Jensen's inequality therefore gives, with
`a_j=E U_j/n`,

\[
 a_{j+1}\le a_j e^{-\eta(\delta+a_j)}.             \tag{2.9}
\]

Dropping `a_j` from the exponent yields
`a_j<=e^(-eta delta j)`.  Dropping `delta` and using

\[
 e^{-\eta a}\le{1\over1+\eta a}                  \tag{2.10}
\]

gives

\[
 {1\over a_{j+1}}\ge {1\over a_j}+\eta.
\]

Since `a_0=1`, induction proves the first term in (2.5).  Markov's
inequality gives (2.6).  \(\square\)

### Corollary 2.3 (the ideal independent menu)

Suppose every value `F_j(u)` is independent and uniform on `R`, over all
sources and banks.  Then (2.3) holds with `eta=1`, because

\[
 \mathbb E|F_j(S)\cap T|
 =|T|\left[1-\left(1-{1\over n}\right)^{|S|}\right]
 \ge |T|(1-e^{-|S|/n}).                            \tag{2.11}
\]

Consequently `K->infinity` gives a source-disjoint matching of
`(1-o(1))n` targets with high probability.  Any polylogarithmic `K` works.

The selector is essential.  Choosing one candidate independently at every
source would again give a mean-one coupon map and a constant miss fraction;
the greedy algorithm correlates the choices by always aiming at the current
target holes.

There is a concrete second-moment condition which allows arbitrary
dependence inside one bank.

### Corollary 2.4 (same-target pair control implies residual hitting)

Assume `ell/n<=B`.  Suppose a fresh random map satisfies, for every source
`u`, target `v`, and distinct sources `u,u'`,

\[
 \Pr(F(u)=v)={1\over n},
 \qquad
 \Pr(F(u)=v,F(u')=v)\le {C\over n^2}.              \tag{2.12}
\]

Then it has `eta`-residual hitting with

\[
 \boxed{\eta={1\over1+CB}.}                        \tag{2.13}
\]

Consequently `K/(1+CB)->infinity` is sufficient for an asymptotically
perfect source-disjoint selector.

#### Proof

Fix `S,T` and, for `v in T`, put

\[
 N_v(S)=|\{u\in S:F(u)=v\}|,
 \qquad \mu={|S|\over n}.                           \tag{2.14}
\]

The hypotheses give

\[
 \mathbb EN_v(S)=\mu,
 \qquad
 \mathbb EN_v(S)^2\le\mu+C\mu^2.                 \tag{2.15}
\]

Paley--Zygmund, or Cauchy--Schwarz on
`N_v 1_(N_v>0)`, yields

\[
 \Pr(N_v(S)>0)\ge{\mu\over1+C\mu}.                \tag{2.16}
\]

Since `mu<=B` and `1-e^(-x)<=x`,

\[
 {\mu\over1+C\mu}
 \ge {\mu\over1+CB}
 \ge1-e^{-\mu/(1+CB)}.                             \tag{2.17}
\]

Summing (2.16)--(2.17) over `v in T` proves (2.3) with (2.13).
\(\square\)

Condition (2.12) is not asserted for the physical containment maps.  A
fixed middle source can only reach targets which contain it, so literal
global target-uniformity requires an additional full-orbit mixing or a
profilewise reformulation.  The corollary identifies the precise useful
pair statistic once the correct marginal kernel has been supplied.

## 3. What symmetry and target means do not prove

Let the bank law be target-transitive and put

\[
 p={\Pr}(v\in F(L))
   ={\mathbb E|F(L)|\over n},                       \tag{3.1}
\]

which is independent of `v`.  For `K` independent banks, a target absent
from their union cannot be covered by any selector.  Therefore

### Proposition 3.1 (image-support obstruction)

Every selector satisfies

\[
 \boxed{
 \mathbb E U_K\ge n(1-p)^K.}                       \tag{3.2}
\]

In particular `Kp->infinity` is necessary for an `o(n)` expected union
deficit whenever `p=o(1)`.  This condition is not sufficient for a
matching, because Hall deficiencies may remain inside the covered union.

#### Proof

For a fixed target, absence events are independent across banks and have
probability `1-p`; hence its union-absence probability is `(1-p)^K`.
Sum over targets.  \(\square\)

There is a sharp counterexample even when every source has the correct
uniform marginal and every target has mean load one in one bank.  Choose a
uniform target `Y` and put

\[
 F(u)=Y\qquad(u\in L),                              \tag{3.3}
\]

with `ell=n`.  Then each `F(u)` is uniform, and a fixed target has expected
preimage count one.  Nevertheless `p=1/n`, one bank has only one distinct
image, and `K` independent banks have matching number at most `K`.
Thus `K=polylog(b)` is useless when `n=exp(Theta(b))`.

The collapse can also respect Boolean containment and the exact uniform
neighbor marginal.

### Proposition 3.2 (containment-respecting collapsed full-orbit menu)

Let the sources be the `b`-subsets and the targets the `(b+q)`-subsets of a
`2b`-set.  Put

\[
 W={2b\choose b},\qquad M={2b\choose b+q},
 \qquad d={b\choose q}.                             \tag{3.5}
\]

There is a deterministic containment map `F`, with `U subset F(U)`, whose
image satisfies

\[
 \boxed{
 {|F(L)|\over M}
 \le {\log W+1\over d}+{1\over M}.}                \tag{3.6}
\]

Let `g` be a uniform permutation of the `2b` labels and conjugate the map by

\[
 F_g(U)=gF(g^{-1}U).                                \tag{3.7}
\]

Then, for every source `U`, `F_g(U)` is exactly uniform over the `d`
targets containing `U`.  A fixed target has expected preimage load `W/M`.
Nevertheless, a menu of `K` independent conjugates has matching number at
most

\[
 K|F(L)|.                                          \tag{3.8}
\]

Hence, for `2<=q<=b/2` and `K=polylog(b)`, its matched target fraction is
`o(1)`.

#### Proof

Choose `m` targets independently and uniformly.  A fixed source belongs to
exactly `d` of the `M` targets, so its probability of being missed is at
most `exp(-md/M)`.  Taking

\[
 m=\left\lceil {M\over d}(\log W+1)\right\rceil    \tag{3.9}
\]

makes the expected number of missed sources below one.  Therefore some
family `C` of at most `m` targets covers every source.  Choose for each
source one containing member of `C`; this defines `F` and proves (3.6).

The symmetric group is transitive on containment flags `(U,V)`.  Every
base source contributes one chosen flag `(U,F(U))`, and the number of group
elements sending any one flag to a prescribed flag is constant.  Thus the
conjugated chosen flag above a fixed source is uniform over its `d`
neighbors.  Each target contains
`D=binom(b+q,q)` sources, and double counting containment flags gives

\[
 W{b\choose q}=M{b+q\choose q}.                   \tag{3.10}
\]

Hence a fixed target's expected preimage load is `D/d=W/M`.

Every selected target from the `K`-menu lies in the union of the `K`
conjugated image sets, proving (3.8).  Finally `log W=Theta(b)` and
`d>=binom(b,2)=Theta(b^2)` for the indicated offsets, so
`K(log W+1)/d=o(1)` for every polylogarithmic `K`.  \(\square\)

Proposition 3.2 is not asserted to arise from tight-cycle factors.  It shows
that containment, exact uniform neighbor marginals, independent global
conjugates, and the correct mean load still do not imply a useful selector.
Specific factor geometry must rule out such small-image fibers.

More generally, if `N_v=|F^{-1}(v)|` is a fixed target's occurrence load,
then

\[
 p=\Pr(N_v>0),
 \qquad
 p\ge{(\mathbb EN_v)^2\over\mathbb EN_v^2}         \tag{3.4}
\]

by Cauchy--Schwarz.  A bounded normalized second moment is enough to make
the union-support obstruction disappear when `K->infinity`, but it still
does not imply residual hitting (2.3).

## 4. Translation to candidate factor banks

Fix one offset `q`.  After discarding any exponentially small inadmissible
middle splits, a complete candidate product-factor bank supplies one upper
target for each retained middle source.  Put `W_b=binom(2b,b)`.  The bank
therefore defines a map

\[
 F_q:\mathcal U\longrightarrow\mathcal V_q,
 \qquad
 \ell=(1-o(1))W_b,\qquad n=M_q={2b\choose b+q}.    \tag{4.1}
\]

Independent rank-and-side conjugations in different candidate banks make
the maps independent across the bank index.  They do **not** make the
values inside one map independent.  Every factor order simultaneously
controls many sources, and repeated longer/shorter interval windows can
create large fibers.

Theorem 2.2 gives a precise sufficient factor-bank theorem:

\[
 \boxed{
 \text{prove (2.3) for a fresh conjugated factor bank with }
 \eta_bK_b\longrightarrow\infty.}                  \tag{4.2}
\]

Then the sourcewise union of `K_b` candidate banks admits a matching
covering `(1-o(1))M_q` targets at this offset.  Ignoring the exponentially small
central-split truncation, the source-surplus proxy is

\[
 \delta_q={W_b-M_q\over M_q}
 =\exp\{q^2/b+O(q/b+q^3/b^2)\}-1.                 \tag{4.3}
\]

The expansion in (4.3) is uniform for `q=o(b^(2/3))`, in particular
through the DCC band considered in the surrounding program.  Thus the
second term of (2.5) gives additional decay once
`eta_b K_b q^2/b->infinity`.

The actual `delta=(ell-M_q)/M_q` differs from (4.3) by
`e^{-Omega(b)}`.

Proposition 3.1 supplies the first necessary audit.  Without global target
transitivity, let `p_q(V)` be the probability that one fresh bank covers
the target `V`.  Union support requires

\[
 {1\over M_q}\sum_{V\in\mathcal V_q}(1-p_q(V))^{K_b}=o(1).    \tag{4.4}
\]

If the bank law is transitive on a split profile carrying a nonnegligible
fraction of the layer, this in particular requires
`K_b[-log(1-p_(q,s))]->infinity` on that profile.  Under full target
transitivity the same condition holds with `p_q`; when the relevant support
probability is `o(1)`, it is equivalent to `K_b p_q->infinity` (and
similarly profilewise).  The exact row/window multiplicity formulas
determine these support probabilities and their second-moment lower bounds,
but the current factor hypotheses give no factor-uniform bound of the form
(2.3).

This cleanly separates the two earlier obstructions.

- A concentrated affine schedule can fail (4.4) on off-central row or
  column shoulders because only one or two factor decks matter.
- A well-spread independent schedule can have `p_q=Theta(1)` yet still
  leave the `e^(-1)` one-bank coupon fraction.  Theorem 2.2 shows that a
  residual-hitting `K`-menu would remove that fraction.

The remaining issue is within-bank dependence under a global factor
conjugation.  One-point transitivity, exact target means, and independence
between the `K` banks do not settle it.

## 5. Output cost and exact scope

The `K` banks in this theorem are a sourcewise menu of alternatives.  Its
matching retains one edge from a source at most once, so the abstract
selected fixed-layer occurrence count is at most `ell`, not `K ell`.
This is a combinatorial statement, not yet a physical length statement.

That observation does not manufacture the candidates for free and does not
solve the physical assembly.  In particular:

- different offsets may select different candidate indices at the same
  source;
- the selected targets need not form nested extension chains;
- two sources in one physical `b^2`-source product atom may select different
  bank indices, even though that atom cannot generally be split;
- factor orders shared by many sources may prevent the selected edges from
  coexisting in one serialized atom bank;
- storing or generating `K` complete physical banks and then concatenating
  them would cost `K W_b` and is not authorized by this selector model.

Thus (4.2) is a rigorous fixed-layer **sourcewise** correlated-selector
escape and an exact new gate.  An atomwise recomposition theorem is required
before its lack of `K`-fold combinatorial usage can be converted into a
coefficient-one physical construction.

## 6. Audit

The H100 checker
`scratch/audit_polylog_factor_menu_residual_hitting_selector_20260821.py`
does the following.

- It exhaustively averages every ideal map at `n<=5` and verifies the
  residual-hit identity (2.11).
- It simulates the roundwise greedy selector for several `n,K`, checks
  source disjointness, and compares the empirical deficit with (2.5).
- It enumerates the collapsed-uniform counterexample and verifies its exact
  matching number, its sharp pair constant `C=n`, and the image-support
  bound (3.2).
- It constructs small Boolean covering maps for Proposition 3.2 and checks
  containment, total source coverage, and the stated image-size bound.
- For the complete rank factors at `b=5`, it constructs independently
  conjugated physical product-bank maps and computes the maximum matching
  in their `K`-menu as a finite diagnostic.  This last experiment is
  evidence only and is not used in any proof.

The proofs above are independent of the finite checks.
