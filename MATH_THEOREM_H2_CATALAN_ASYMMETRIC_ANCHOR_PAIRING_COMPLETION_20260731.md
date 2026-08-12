# Asymmetric anchor-pair completion for the two-coordinate physical row

Date: 2026-07-31  
Status: exact abstract/physical sufficient theorem; punctured-side realization
remains open

## 0. Verdict

The synchronized common basis is automatic.  After it is fixed, each
anchor-capped punctured side forest contracts to a matching on the seam
labels.  If that side has `c_0` anchor-free components, the exact charge
identity says that the matching has

\[
                   r=\operatorname{Cat}_n+c_0
\tag{0.1}
\]

edges.

The no-anchor-free normal form is useful but not necessary.  Let

\[
                   C=\operatorname{Cat}_{n+1},\qquad
                   K=\operatorname{Cat}_n.
\]

Once either shore matching and the punctured central relation are fixed,
one can choose a matching of order `r` on the other shore so that the full
contracted attachment graph is a forest whenever

\[
                         2r<C.                         \tag{0.2}
\]

The proof is a greedy union--find construction.  It is independent of the
size and shape of the already fixed shore matching.

For the exact positive fixtures, `(C,K)=(14,5)` at `n=3` and `(42,14)` at
`n=4`.  Their shore values are respectively `c_0=(0,0)` and `(0,1)`, so
the completing-shore inequalities are `10<14` and `30<42`.  Thus both
fixtures lie inside this asymmetric topology-safe range; the extra empty
component at `n=4` is not a global topology obstruction.

This theorem does **not** realize the requested matching by a punctured
side incidence system.  It reduces the remaining all-`n` problem to a
shore-local prescribed-pair realization theorem.

## 1. Exact side charge

Let a side forest have `N` physical vertices, `P` edges and
`C=Cat_(n+1)` seam anchors.  Every anchor has side degree at most one.
Every component is therefore a path with at most two anchors.  If `c_j`
counts components containing `j` anchors, then

\[
 c_0+c_1+c_2=N-P,
 \qquad c_1+2c_2=C,
\]

and hence

\[
                    c_2-c_0=C-(N-P)=K.              \tag{1.1}
\]

The side contraction matching consequently has exactly `K+c_0` edges.

## 2. Abstract asymmetric completion

Let `L` and `R` be disjoint sets of order `C`.  Let `P_0` be any partial
matching between `L` and `R`; in the physical application it is the
relation induced by the components of the punctured child forest.  Let
`P_L` be any matching on `L`, of arbitrary order.

### Theorem 2.1 (asymmetric matching completion)

For every integer `r>=0` satisfying `2r<C`, there is an `r`-edge matching
`P_R` on `R` such that

\[
                         P_0\cup P_L\cup P_R          \tag{2.1}
\]

is a forest.

### Proof

The initial graph `G_0=P_0 union P_L` is a forest: every `R`-vertex has
degree at most one, so a cycle is impossible.  More precisely, each
nontrivial component is an alternating subpath of

```text
R - L - L - R,
```

and contains at most two unused `R`-vertices.

Construct `P_R` greedily.  At each step join two unused `R`-vertices lying
in different current components.  This keeps the graph acyclic.  If the
two old components contain `s,t<=2` unused `R`-vertices, the merged
component contains `s+t-2<=2`, so the invariant survives.

Before step `j+1`, where `j<r`, the number of unused `R`-vertices is

\[
                         C-2j\ge C-2r+2>2.            \tag{2.2}
\]

No component contains more than two of them, so a legal pair in distinct
components always exists.  After `r` steps (2.1) is a forest. \(\square\)

The strict inequality is a simple uniform sufficient condition, not a
claimed necessary condition for a particular instance. It is, however,
sharp for a theorem uniform over the already fixed relation.

### Proposition 2.2 (the strict boundary is worst-case sharp)

For every even `C=2r>=4`, there are `P_0` and `P_L` for which no perfect
matching `P_R` makes (2.1) a forest.

### Proof

Let `P_0` be the perfect matching `L_i R_i`, and pair
`L_(2j)` with `L_(2j+1)` in `P_L`. The initial graph consists of `r`
vertex-disjoint paths

    R_(2j) - L_(2j) - L_(2j+1) - R_(2j+1).

If `P_R` pairs the two `R`-ends of one old path, it immediately closes a
cycle. Otherwise contract the old paths. Every contracted vertex has
degree two in the perfect matching `P_R`, so the contracted multigraph is
a union of cycles. Thus no choice is acyclic. \(\square\)

## 3. Physical corollary

Fix a common basis `Q`, orient the child paths, and contract the components
of `F-Q`.  The inherited central relation is a partial matching `P_0`
between the two seam-label banks.  Suppose one punctured side forest has
already been realized; its double-anchor components give `P_L`.

### Corollary 3.1 (slack-tolerant shore decoupling)

Suppose the other shore can physically realize a prescribed matching of
`r=K+c_0` disjoint anchor pairs while satisfying its exact outer-label
matching, side degree at most two, seam-anchor degree at most one, and the
specified number `c_0` of anchor-free components.  If

\[
                  2(K+c_0)<C,                        \tag{3.1}
\]

then a prescribed pairing can be selected so that the complete contracted
graph `Gamma_Q` is acyclic.  Hence the full central five-sector support is
a linear forest.

### Proof

Apply Theorem 2.1 to choose the pairing on the completing shore.  The
component-incidence graph `Gamma_Q` is obtained from
`P_0 union P_L union P_R` by subdividing edges and adjoining leaves and
isolated anchor-free side components.  These operations preserve cycle
rank.  The individual central and side pieces are forests and all seam
degrees are capped, so the uncontracted support is a linear forest.
\(\square\)

Since

\[
 {C\over K}=4-{6\over n+2},
\]

condition (3.1) is equivalently

\[
                  c_0<{K(n-1)\over n+2}.             \tag{3.2}
\]

It permits a linear number of anchor-free components; `c_0=0` is only the
cleanest special case.

## 4. Product/SCD interpretation

For a fixed common basis `Q`, a product/SCD certificate must still supply
the two punctured side incidence systems.  The exact safe sequential form
is:

1. realize either shore by an anchor-capped side forest;
2. contract its double-anchor paths to obtain `P_L`;
3. run Theorem 2.1 to request a topology-safe pairing `P_R`; and
4. realize that prescribed pairing on the other shore, with
   `2(K+c_0)<C`.

Thus global topology does not require a simultaneous two-shore search
*conditional on* a shore theorem capable of realizing the requested
pairing. Such a universal physical theorem is false: every realized pairing
obeys the Johnson transport budget

\[
                  \sum_{\{A,B\}}d_J(A,B)\le P,
\]

while maximum-distance requested pairings violate it in every `n>=3`.
The exact surviving gate is therefore joint selection from the two
physically realizable pairing families; Theorem 2.1 describes an abstract
acyclic-completion class which the second family may try to meet.

The canonical BTK diagonal does not provide even the local side theorem:
it fails the anchor/degree row for every `n>=3`. Any successful
product/SCD induction must use a noncanonical bank, export collisions
between SCD blocks, or use a more general diagonal matching.

## 5. Finite fixtures and the sharp remaining gate

The exact `n=3` and `n=4` integral collar fixtures have side charge rows

\[
\begin{array}{c|cc|cc}
 n&c_0^-&c_2^-&c_0^+&c_2^+\\ \hline
 3&0&5&0&5\\
 4&0&14&1&15.
\end{array}
\]

Their literal contracted matching unions are already forests.  Theorem
2.1 additionally explains why their charge profiles leave abstract
topology slack.

The complete fixed-child census at `n=3` supplies the complementary
warning: all fifteen deletion banks are common incidence bases, but only
ten have a physical two-shore realization; two fail anchor capacity and
three force a contracted cycle.  Therefore the automatic common basis
cannot be selected obliviously.

One sufficient sequential constructive theorem exposed here is:

> choose at least one automatic common basis `Q`; realize one punctured
> side forest; and find in the other shore's physically realizable family
> a topology-safe pairing of the order handled by Theorem 2.1.

The exact, weaker formulation is simply to choose both realizable shore
pairings jointly so their union with the central partial matching is a
forest. The theorem here solves only the abstract topology part of that
selection.

No arbitrary-SCD existence, all-`n` punctured-side construction, residence,
deep-shadow, compiler, or `nu(k)=B(k)` theorem is claimed.
