# Rational multicover resolution and the exact singleton/Berge cut

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The pointwise isolated-pruning theorem converts the retained protected
catalogue into a rational multihypergraph with

* degree exactly (D) at every retained tag;
* degree at most ((1+\eta)D) at every protected target; and
* one hyperedge for each legal geodesic chunk occurrence.

Here \(\eta=o(1)\).  If this multihypergraph has an edge-colour
resolution with at most ((1+\epsilon)D) colours, one colour contains
paths over all but (O(\epsilon T)) retained tags.  This gives two exact
coefficient ledgers.

1. With literal row repair, it is enough that

   \[
    Q(\beta+\epsilon)=o(1),
   \]

   where \(\beta\) is the initially discarded tag fraction.
2. With a tagged chain cover of the missing claims and the coefficient-safe
   horizontal braid estimate (p=O(B/Q)+o(W/Q)), it is enough that

   \[
    \beta+\epsilon=o(1).
   \]

   The already proved one-column chain word alone does **not** give this
   improvement: its cost is (O(QB)), and still requires
   (Q(\beta+\epsilon)=o(1)).

The exact first-order obstruction is the fractional chromatic-index cut

\[
 \boxed{
  \chi_f'(\mathcal M_D)
  =\sup_{w\ge0}{w(E)\over\nu_w(\mathcal M_D)}.}
\]

Thus a near-(D) resolution is equivalent to a weighted matching theorem,
not to a bound on pair moments or clique size.  The recent singleton-strip
calculation proves useful local facts--a non-star linear intersecting
family has at most (K^2-K+1=o(D)) members, and one external strip hits
only an (m^{-1/2+o(1)}) fraction of a target star--but those facts do not
establish the weighted matching cut.  Strong odd Berge cycles and, more
generally, the integrality gap of every weighted residual remain.

## 1. Rationally scaled protected multicover

Let \(\mathcal T'\) be retained tags and \(\mathcal I_U\) the retained
candidate paths over (U\).  Suppose rational weights (x_P\) satisfy

\[
 \sum_{P\in\mathcal I_U}x_P=1 \qquad(U\in\mathcal T')
 \tag{1.1}
\]

and

\[
 \ell(v):=\sum_{P\ni v}x_P\le1+\eta
 \qquad(v\in V).
 \tag{1.2}
\]

Choose a common denominator (D) for all (x_P).  Replace (P) by

\[
 m_P:=Dx_P
 \tag{1.3}
\]

labelled copies.  Define the augmented multihypergraph \(\mathcal M_D\)
on vertex set

\[
 \mathcal T'\ \dot\cup\ V
\]

by making each copy of (P\in\mathcal I_U) the edge

\[
 \widehat P=\{U\}\cup C(P).
 \tag{1.4}
\]

Then, exactly,

\[
 d_{\mathcal M_D}(U)=D,
 \tag{1.5}
\]

while

\[
 d_{\mathcal M_D}(v)=D\ell(v)\le(1+\eta)D.
 \tag{1.6}
\]

The total number of multiedges is

\[
 |E(\mathcal M_D)|=D|\mathcal T'|.
 \tag{1.7}
\]

This scaling is exact; no asymptotic rounding occurs in (1.3)--(1.7).

## 2. One colour gives one large legal family

### Theorem 2.1 (colour-to-matching reduction)

Suppose the edges of \(\mathcal M_D\) have a proper colouring with

\[
 C\le(1+\epsilon)D
 \tag{2.1}
\]

colours.  Then some colour class is a target-disjoint family using
distinct tags and has size at least

\[
 {D|\mathcal T'|\over C}
 \ge {|\mathcal T'|\over1+\epsilon}.
 \tag{2.2}
\]

Consequently it misses at most

\[
 r\le {\epsilon\over1+\epsilon}|\mathcal T'|
 \le\epsilon|\mathcal T'|
 \tag{2.3}
\]

retained tags.

#### Proof

A proper colour class is a matching because tag and target vertices are
part of every augmented edge.  The (C) colour classes partition the
(D|\mathcal T'|) edge copies.  Their average size is the first quantity
in (2.2). \(\square\)

The full colouring is stronger than necessary.  For coefficient one it
is enough to prove directly

\[
 \boxed{
  \nu(\mathcal M_D)
  \ge{D|\mathcal T'|\over C}.}
 \tag{2.4}
\]

## 3. Exact literal coefficient ledger

Let (T) be the original chunk-tag count, let

\[
 b=T-|\mathcal T'|=\beta T,
\]

and select the matching from Theorem 2.1.  Its number of omitted original
tags is

\[
 R=b+r\le(\beta+\epsilon)T.
 \tag{3.1}
\]

Write (g) for the middle claims per path and (c_q) for the claims in
each signed depth-(q) row.  Put

\[
 \delta_0=W-gT,
 \qquad
 \delta_{q,\pm}=R_q-c_qT,
 \tag{3.2}
\]

where the capped, floor, deadline, and carrier-remainder ledgers are
understood as in the audited chunk construction.  Their total is (o(W)).

Because one colour is a matching, all its designated targets are distinct.
It therefore leaves exactly

\[
 \delta_0+gR
 \tag{3.3}
\]

middle targets and

\[
 \delta_{q,\pm}+c_qR
 \tag{3.4}
\]

targets in signed row ((q,\pm)).

Emit the selected chunk words.  Their main contribution plus literal
middle repair is

\[
 g(T-R)+\delta_0+gR=W,
 \tag{3.5}
\]

apart from the already (o(W)) seam/reset ledger.  Literal signed-row
repair costs

\[
\begin{aligned}
 2\sum_{q=1}^Q(\delta_q+c_qR)
 &\le o(W)+2R\sum_{q=1}^Qc_q\\
 &\le o(W)+O(QgR)\\
 &\le o(W)+O(Q(\beta+\epsilon)W).
\end{aligned}
 \tag{3.6}
\]

Hence

\[
 \boxed{
  Q(\beta+\epsilon)=o(1)
  \quad\Longrightarrow\quad
  \nu(k)\le(1+o(1))W(k).}
 \tag{3.7}
\]

This is the strongest conclusion available from colour count and literal
repair alone.

## 4. What chain-width sharing changes

The excess holes in (3.4) have only row-count bounds from a bare colour
resolution.  Those bounds do not imply small Boolean-poset width: the
weighted-antichain construction in
`TAGGED_FLAGGED_RESERVE_CHAIN_HALL_AUDIT_20260725.md` shows that this
failure can occur even when every row budget is respected.

Suppose, in addition to the colour resolution, that the excess hole family
admits a tagged chain assignment with

\[
 B\le gR+o(W)
 \tag{4.1}
\]

chains.  The proved one-column compilation uses at most

\[
 (2Q+2)B
 \tag{4.2}
\]

entries.  Equations (3.1) and (4.1) show that this still asks for

\[
 Q(\beta+\epsilon)=o(1).
 \tag{4.3}
\]

Thus chain width by itself does not improve the required colour error.

If the same chains also satisfy the horizontal rotor path-cover bound

\[
 p\le {C B\over Q}+o(W/Q),
 \tag{4.4}
\]

then the braid compilation has length

\[
 B+O(Qp)=O(B)+o(W).
 \tag{4.5}
\]

Now (3.1), (4.1), and (gT=(1-o(1))W) give

\[
 B=O((\beta+\epsilon)W)+o(W).
\]

Consequently the coefficient-safe condition relaxes to

\[
 \boxed{
  \beta+\epsilon=o(1)
  \quad\hbox{under tagged chain Hall plus horizontal braid grouping}.}
 \tag{4.6}
\]

This distinction is important for the pointwise isolated pruning.  Its
elementary Markov/Chernoff implementation gives

\[
 \beta+\eta
 =O\left(L^{-1/2}+\sqrt{{m\over\mu}}\right)=o(1),
 \tag{4.7}
\]

but not (o(1/Q)) at the present mesoscopic parameters.  Therefore it is
already at the right scale for (4.6), but not for the literal condition
(3.7).

More generally, if deletion-bad tags are defined using threshold
(Z_U>\delta\mu), the elementary proof gives

\[
 \beta=O\left({1\over L\delta}ight),
 \qquad
 \eta=O\left(\delta+\sqrt{{m\over\mu}}\right).
 \tag{4.8}
\]

Thus literal repair would require

\[
 Q\left({1\over L\delta}+\delta+sqrt{{m\over\mu}}
 \right)=o(1).
 \tag{4.9}
\]

With \((\Delta+1)/A=m^{-3+o(1)}\), one has

\[
 \mu=m^{3-o(1)}/L.
\]

Even after optimizing \(\delta\), the two elementary errors in (4.9)
have the competing scales

\[
 {Q\over\sqrt L}
 \quad\hbox{and}\quad
 {Q\sqrt L\over m^{1-o(1)}}.
 \tag{4.10}
\]

At (Q/\sqrt m\to\infty), no choice of (L) makes both vanish.  This is
an exact reason the pointwise pruning naturally needs global chain/braid
sharing, or a stronger concentration theorem for isolated deletions.

## 5. The exact fractional chromatic-index cut

Let (E) be the labelled edge-copy set of \(\mathcal M_D\).  A fractional
edge colouring assigns weights \(\lambda_M\ge0\) to matchings (M\) such
that

\[
 \sum_{M\ni e}\lambda_M\ge1\qquad(e\in E).
 \tag{5.1}
\]

Its minimum total weight is \(\chi_f'(\mathcal M_D)\).  For a
nonnegative edge weight (w=(w_e)), put

\[
 \nu_w(\mathcal M_D)=\max_{M\text{ matching}}\sum_{e\in M}w_e.
 \tag{5.2}
\]

### Theorem 5.1 (exact weighted Berge cut)

\[
 \boxed{
 \chi_f'(\mathcal M_D)
 =\sup_{w\ge0,\ w\ne0}{\sum_ew_e\over\nu_w(\mathcal M_D)}.}
 \tag{5.3}
\]

Consequently,

\[
 \boxed{
 \chi_f'(\mathcal M_D)\le(1+\epsilon)D}
 \tag{5.4}
\]

if and only if every nonnegative edge weighting satisfies

\[
 \boxed{
 \nu_w(\mathcal M_D)
 \ge{w(E)\over(1+\epsilon)D}.}
 \tag{5.5}
\]

#### Proof

The LP dual to (5.1) maximizes \(\sum_ew_e\) subject to

\[
 \sum_{e\in M}w_e\le1
 \qquad(M\text{ every matching}),
\]

and (w_e\ge0).  Normalizing an arbitrary nonzero (w) by
(\nu_w\) gives (5.3), and (5.4)--(5.5) are immediate. \(\square\)

For merely extracting one coefficient-safe colour, the unweighted special
case

\[
 \nu(\mathcal M_D)
 \ge {|E|\over(1+\epsilon)D}
 ={ |\mathcal T'|\over1+\epsilon}
 \tag{5.6}
\]

is sufficient.  The weighted statement is the correct hereditary theorem
needed for an actual fractional colour resolution or iterative proof.

## 6. Fractional matching integrality gap

Let \(\nu_w^*\) denote the weighted fractional matching optimum of
\(\mathcal M_D\).  Since its maximum vertex degree is at most
((1+\eta)D), the constant assignment

\[
 z_e={1\over(1+\eta)D}
\]

is a feasible fractional matching.  Hence

\[
 \nu_w^*\ge{w(E)\over(1+\eta)D}.
 \tag{6.1}
\]

It follows that the weighted integrality-gap theorem

\[
 \boxed{
  \nu_w\ge(1-\rho)\nu_w^*
  \quad\hbox{for every }w\ge0}
 \tag{6.2}
\]

would imply

\[
 \chi_f'(\mathcal M_D)
 \le{(1+\eta)D\over1-\rho}
 =(1+\eta+\rho+o(\eta+\rho))D.
 \tag{6.3}
\]

Thus the exact missing theorem is a (1+o(1)) weighted matching
integrality theorem for the actual protected-strip incidence matrix.

## 7. Singleton intersections and strong odd Berge cycles

The nonlinear width-two moment

\[
 \sum_E\bigl(w^{|C(P)\cap C(E)|}-1-(w-1)|C(P)\cap C(E)|\bigr)
\]

vanishes on intersections of size zero or one.  It therefore cannot imply
(5.5) or (6.2) by itself.

The local singleton results in
`MATH_ATTACK_FIRST_ORDER_PROTECTED_STRIP_INTERSECTING_EXPANSION_20260725.md`
are nevertheless useful and appear correct:

* every linear pairwise-intersecting non-star family has at most
  (K^2-K+1=o(D)) supports;
* for a good target (v) and an external strip (E), at most an
  (m^{-1/2+o(1)}) fraction of the retained (v)-star also intersects
  (E); and
* these estimates survive the same isolated-pruning experiment.

They bound special cliques in the line graph.  Clique bounds are not the
weighted matching cut (5.5): a graph can have small cliques and still have
large fractional chromatic number.  No near-(D) edge-colouring conclusion
follows without a further theorem.

For the incidence matrix, the first exact obstruction is a **clean strong
odd Berge cycle**: (2s+1) hyperedges with cyclic singleton
intersections, with no target lying in more than two of the selected
hyperedges.  Assigning weight (1/2) to every cycle hyperedge is then a
feasible fractional matching of value ((2s+1)/2), whereas the integral
matching value is at most (s).  The gap is

\[
 1+{1\over2s}.
 \tag{7.1}
\]

The explicit three-strip non-Helly triangle in the first-order note has
pairwise intersections equal to three different singleton owners and no
other common protected flags.  It is therefore a literal (s=1) clean
strong Berge cycle, so such cycles genuinely occur in the actual
return-free strip geometry.

A concrete sufficient theorem would be an approximate balancedness
statement: delete (o(DT)) edge copies so that the remaining protected
incidence matrix is balanced (equivalently, it has no odd cycle submatrix
in the balanced-matrix sense).  Balanced-hypergraph
matching integrality would then give a matching of size

\[
 {DT-o(DT)\over(1+\eta)D}=(1-o(1))T.
 \tag{7.2}
\]

This condition is stronger than necessary, but it is genuinely first
order and it directly implies the unweighted cut (5.6).  The currently
proved one-star and width-two estimates do not bound the minimum odd-cycle
edge transversal, so (7.2) remains open.

## 8. Exact frontier for bounded-displacement geodesic strips

For the actual rational multicover, coefficient one now reduces to either
of the following precise alternatives.

1. Prove the unweighted near-perfect matching cut (5.6) with
   \(\epsilon=o(1/Q)\) for literal repair, or with \(\epsilon=o(1)\)
   together with the tagged chain-Hall and horizontal braid estimates.
2. Prove the hereditary weighted cut (5.5), equivalently
   \(\chi_f'=(1+o(1))D\), and use one matching from the resulting
   resolution.
3. Prove the weighted matching integrality estimate (6.2) directly from
   bounded-displacement phase geometry.
4. Prove an approximate balancedness/odd-Berge-cycle transversal theorem
   strong enough for (7.2).

The singleton star expansion rules out one obvious projective-plane-scale
clique at the numerical (D)-scale, but it does not settle any of these
four matching-number statements.  This is the exact mathematical content
still missing after the fractional weighted-cut closure.

## 9. Audit of four-antichain pruning

If the conflict is strengthened from a shared three-antichain to a shared
four-antichain, the retained strip intersections have width at most three
and the retained fibre degree becomes

\[
 D_0=\mu=m^{23/6-o(1)}\gg K^2.
\]

This is a genuine numerical improvement, but it does not prove the
weighted cut (5.5).  It makes every singleton-only non-star intersecting
clique (o(D_0)).  In the mixed clique reduction of the first-order note,
it would be enough to prove

\[
 B=o(D_0/K^2)=m^{11/6-o(1)},
\]

where (B) is the maximum number of nonlinear (intersection at least two)
neighbours inside the obstruction.  The current exponential overlap
census supplies an averaged normalized moment of order
(D_0m^{o(1)}), not this maximum-degree estimate.

More importantly, even that clique estimate would not be the hereditary
weighted matching theorem (5.5).  Width at most three, (D_0\gg K^2),
and small non-star cliques do not by themselves bound fractional chromatic
number.  An extensive system of singleton odd Berge cycles can have no
large local clique while still violating a weighted matching cut.  Thus
the exact residual statement after four-antichain pruning remains

\[
 \nu_w(\mathcal M_D)
 \ge {w(E)\over(1+o(1))D}
 \qquad\hbox{for every }w\ge0,
\]

or its unweighted near-perfect-matching specialization.  No proved
four-antichain census currently implies this statement.

### Theorem 9.1 (the numerical (D\gg K^2) regime is not enough)

There are partitioned (K)-uniform hypergraphs with (T-o(T)) tags,
exactly (D) candidates per retained tag, target degree at most
((1+o(1))D), and target intersection at most one between every two
different candidates, but whose largest tag--target matching has size
(o(T)).  This holds whenever

\[
 K\to\infty,\qquad \log D=o(K),\qquad
 D\gg\log(KT),\qquad T\gg D^2K^2.
 \tag{9.1}
\]

In particular it is compatible with (D\gg K^2).

#### Proof

Let (N=KT), and choose (DT) independent uniform (K)-subsets of an
(N)-element target universe.  Before sampling, divide their labels into
(T) groups of (D), which will be the tags.

Every target has binomial degree of mean (D).  Chernoff and
(D\gg\log N) imply that, with probability tending to one, the maximum
target degree is ((1+o(1))D).

The probability that two sampled edges meet in at least two targets is

\[
 O(K^4/N^2)=O(K^2/T^2).
\]

Hence the expected number of such pairs is (O(D^2K^2)).  Delete every
tag containing an edge in one of these pairs.  Markov's inequality and
(T\gg D^2K^2) show that only (o(T)) tags are deleted.  All retained
tags still have exactly (D) candidates, and all different retained
candidates meet in at most one target.

It remains to bound the matching number.  For (t) specified sampled
edges, sequential exposure gives

\[
\begin{aligned}
 \Pr(\hbox{the }t\hbox{ edges are disjoint})
 &\le\prod_{i=0}^{t-1}
 \left(1-{iK\over N}\right)^K\\
 &\le\exp\left(-{K^2t(t-1)\over2N}\right).
\end{aligned}
 \tag{9.2}
\]

Therefore the expected number of disjoint (t)-edge families is at most

\[
 \binom{DT}{t}
 \exp\left(-{K^2t(t-1)\over2N}\right).
 \tag{9.3}
\]

Take (t=\alpha T), where

\[
 \alpha=C\sqrt{{\log D+\log K\over K}}\longrightarrow0
\]

and (C) is a sufficiently large constant.  The logarithm of the
binomial factor in (9.3) is at most

\[
 \alpha T\log(eD/\alpha),
\]

whereas the negative exponent is

\[
 (1-o(1)){\alpha^2KT\over2}.
\]

The latter dominates, so with positive probability no matching has size
(t).  Deleting bad tags cannot increase the matching number.  Intersect
this event with the degree and linearity events above.

Finally, giving every candidate weight (1/D) saturates each retained tag
and gives every target load at most (1+o(1)).  Thus the claimed
pointwise fractional point exists although every integral matching uses
only (o(T)) tags. \(\square\)

Theorem 9.1 is an abstract counterexample, not a geodesic-strip
counterexample.  Its role is exact: four-antichain width, pointwise
fractional feasibility, (D\gg K^2), and even complete linearity do not
logically imply the required rounding.  Any positive result must use the
bounded-displacement phase geometry in a way that proves the matching cut
(5.5), rather than only its local degree and intersection consequences.
