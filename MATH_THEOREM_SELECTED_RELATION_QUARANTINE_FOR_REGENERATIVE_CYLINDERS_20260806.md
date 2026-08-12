# Selected-relation quarantine for regenerative cylinders

**Date:** 2026-08-06  
**Method:** post-run conflict pruning and the regenerative first-hit lemma;
no computation or search  
**Status:** unconditional abstract theorem.  It removes the need to certify
the carrier-pair row simultaneously against every unselected carrier.  Its
application still requires an averaged dynamic estimate showing that only
`O(M/d^2)` selected doublets participate in bad relations.

## 1. Adaptive selector and tested relations

Let an adaptive exponential-clock process produce an ordered matching

\[
                         \mathcal M=(E_1,\ldots,E_s)
\tag{1.1}
\]

in a hypergraph of physical resources.  Each marked occurrence `a` in a
selected edge has a distinguished carrier `v(a)`.  At every pre-hit state
write

\[
 L_v=\sum_{E\ni v}x_E,
 \qquad
 L_{v,w}=\sum_{E\supseteq\{v,w\}}x_E                 
\tag{1.2}
\]

for the current adaptive rates.

Fix constants `delta,theta,kappa`.  Test every marked occurrence and every
compatible marked block of size at most three inside a selected edge.  For
two marked occurrences `a,b` in
different selected edges, call their ordered pair **relation-bad** if, at
some state before the first selected edge meeting either carrier,

\[
 L_{v(a),v(b)}>
       \delta\min\{L_{v(a)},L_{v(b)}\}.
\tag{1.3}
\]

The definition uses the complete history, not merely the state at which
one of the two edges is accepted.  Call a selected marked block `A`
**cluster-bad** if, at some state before its carrier is first hit,

\[
 \sum_{E:A\subseteq\Sigma(E)}x_E
   >\theta\kappa^{|A|-1}L_{v(A)}.
\tag{1.4}
\]

Degree-badness may be added in the same way, for example when
`L_v` leaves a prescribed fixed interval.  None of these tests changes
the clock process.

## 2. Post-run quarantine

Form a graph `G_bad` whose vertices are the selected edges of
`mathcal M`.  Join two selected edges when some tested marked occurrence
in one and some tested marked occurrence in the other form a relation-bad
pair.  Also mark every selected edge containing a cluster-bad or
degree-bad tested block.

Delete all marked vertices and a vertex cover of `G_bad`; deleting both
endpoints of every bad edge is always allowed.  Denote the surviving
matching by `mathcal M_good`.

### Theorem 2.1 (surviving cylinders see only good histories)

Let `A_1,...,A_q` be compatible marked blocks which occur in distinct
edges of `mathcal M_good`, and let their union contain `m` marked
occurrences.  Then throughout the raw clock history before the first hit
of any remaining carrier one has

\[
 L_{v(A_i),v(A_j)}
 \le\delta\min\{L_{v(A_i)},L_{v(A_j)}\}
 \quad(i\ne j),                                      
\tag{2.1}
\]

and

\[
 \sum_{E:A_i\subseteq\Sigma(E)}x_E
 \le\theta\kappa^{|A_i|-1}L_{v(A_i)}.
\tag{2.2}
\]

Consequently, if `(q-1)delta/2<1`,

\[
 \Pr\bigl(A_1,\ldots,A_q
          \text{ occur as the prescribed blocks in }
          \mathcal M_{\rm good}\bigr)
 \le
 \left(\prod_{j=1}^q
       {1\over1-(j-1)\delta/2}\right)
       \theta^q\kappa^{m-q}.
\tag{2.3}
\]

In particular, for `q<=K d` and `delta<=gamma/d`, with
`K gamma<2`, this is a fixed-factor cylinder:

\[
 \Pr(\Pi=\pi\text{ in }\mathcal M_{\rm good})
 \le C_0^q\theta^q\kappa^{m-q},
 \qquad C_0={1\over1-K\gamma/2}.
\tag{2.4}
\]

#### Proof

If (2.1) failed at any pre-hit state, the two selected edges containing
the corresponding occurrences would be adjacent in `G_bad`; a vertex
cover deletes at least one of them.  Thus both cannot survive.  The same
argument with the marked-vertex rule proves (2.2), including any retained
degree test.

Formally, run a killed-event induction on the *raw* process.  For the fixed
prescribed blocks, assign continuation payoff zero as soon as a required
pair or cluster row has failed: future quarantine then makes the desired
event impossible.  This does not condition the clock law on future
survival.  On every still-live branch, ignore accepted edges which miss
the current requested carriers.  At a state with `j` remaining blocks,
Bonferroni and (2.1) give total carrier-hit rate at least

\[
 \left(1-{j-1\over2}\delta\right)
                   \sum_iL_{v(A_i)}.
\tag{2.5}
\]

Equation (2.2) bounds the rate serving block `A_i` by
\(\theta\kappa^{|A_i|-1}L_{v(A_i)}\).  Conditioning on the complete state
immediately before the first hit, summing over its possible first block,
and iterating gives (2.3).  Raw edges later removed by quarantine merely
act as intervening accepted edges or destroy the requested event; they
cannot increase it.  Finally each factor in (2.3) is at most `C_0` under
the hypotheses of (2.4).  \(\square\)

## 3. Cleanup accounting

Let `B_0` be the number of individually marked selected edges and let
`B_1=|E(G_bad)|`.  Deleting every marked edge and both endpoints of each
bad relation removes at most

\[
                              B_0+2B_1
\tag{3.1}
\]

selected edges.  If every macro contains `O(d)` lower resources and

\[
                      \mathbb E(B_0+B_1)=O(M/d^2),
\tag{3.2}
\]

then the expected extra lower leave is `O(M/d)`.  Markov's inequality
gives a positive-probability outcome with the same bound.

One should not condition the output law on that terminal cleanup event and
then claim the hereditary cylinder without further work: a globally
positive event can have arbitrarily small conditional probability after a
particular exposed prefix.  The proof-safe use is to retain the raw
quarantined law, whose killed-event proof is hereditary, and combine its
terminal expected-leave estimate with the downstream success estimate in
one joint probabilistic argument.  Alternatively one must prove a
uniformly prefix-positive cleanup probability.

The useful point is the quantifier in (3.2): it is an average over pairs
which are actually selected, rather than a maximum over exponentially many
potential partners of every carrier.  The rooted collision-energy sums in
the rank-compensated doublet clock are designed for precisely this
averaged estimate.

## 4. Scope

The theorem proves the cylinder after a small selected-relation cleanup,
provided all marked blocks in the tested order range are included.
It does not prove (3.2), degree tracking, or that the raw process reaches
the separator density.  Those are the remaining dynamic estimates for the
atomic doublet template.  It also does not replace same-edge merger bounds:
they enter through (1.4) and the factor `kappa^(m-q)`.
