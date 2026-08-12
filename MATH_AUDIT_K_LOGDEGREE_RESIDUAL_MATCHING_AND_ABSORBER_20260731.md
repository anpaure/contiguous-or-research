# Audit of the logarithmic-degree residual matching and absorber theorem

Date: 2026-07-31  
Lane: K, independent proof audit  
Status: PASS after the corrections recorded below

## 1. Object and scope

This note audits

```text
MATH_THEOREM_K_LOGDEGREE_RESIDUAL_OUTER_MATCHING_AND_CORRIDOR_PRESSURE_20260731.md
SHA256 77d4f61a2272579eed1363a7aa200d6900e3bb47f375ae6f2d58a9bd4ecf3539
```

The theorem has two logically separate conclusions.

1. The numerical residual data

   \[
   |A|=|B|=n,\quad |C|=|D|=n+\Theta(nm^{-2/3}),\quad
   \deg=\Theta(m),\quad \Delta _2=\Theta(m^{1/3})
   \]

   do not force an outer-perfect four-partite matching.
2. An almost matching *does* complete when it exports an exact endpoint
   Hall matching and sufficiently dispersed lists of matching-aligned
   independent-boundary absorbers.

The first statement is an abstract four-partite obstruction and is not
asserted to occur inside the Boolean ordered-diamond hypergraph.  The second
is a conditional deterministic theorem; the Boolean residual is not proved
to satisfy its hypotheses.

## 2. Sharp-scale AP obstruction

Choose \(r,q\to\infty\), \(R=\Theta(m^{2/3})\), and, by Bertrand,

\[
                         6r<s<12r
\]

prime.  In a regular arithmetic-progression component, fixing any vertex
and a step \(t\in[0,r)\) fixes the initial point, hence every degree is
\(r\).  Two coordinates in distinct parts recover the step because their
positional difference is one of \(1,2,3\), invertible modulo \(s\), and the
allowed step lies below \(s/3\).  Thus pair-codegree is at most one.

In a part-doubled component, the tag and \(t\) give the combined step
\(u=jr+t\in[0,2r)\).  A doubled vertex has \(r\) incident edges and an
ordinary vertex has \(2r\).  The same difference argument recovers \(u\),
the tag, \(t\), and the initial point, so pair-codegree remains at most one.

The additive \(\mathbb Z_q\)-clone lift with clone sum zero multiplies each
degree by \(q^2\) and each nonzero pair-codegree by \(q\).  Therefore all
degrees are \(rq^2\) or \(2rq^2\), and \(\Delta _2=q\).

The component multiset

```text
one A-doubled, one B-doubled,
two C-doubled, two D-doubled,
R regular
```

has part sizes

\[
 |A|=|B|=(R+7)sq,qquad |C|=|D|=(R+8)sq.
\]

The \(A\)-doubled block has \(2sq\) vertices on \(A\) but only \(sq\) on
\(B\), and no edge exits the block.  Hence every matching leaves at least
\(sq\) vertices of that \(A\)-block; the \(B\)-doubled block gives the
same lower bound on the other shore.  With

\[
 r,q=\Theta(m^{1/3}),\qquad R=\Theta(m^{2/3}),
\]

one base union has size \(n_0=\Theta(m^{4/3})\), degree \(\Theta(m)\),
codegree \(\Theta(m^{1/3})\), and relative surplus and defect
\(1/(R+7)=\Theta(m^{-2/3})\).  Taking

\[
 \left\lfloor Nm^{-1/3}/n_0\right\rfloor
\]

copies gives \(n=(1+o(1))Nm^{-1/3}\), and both surplus and outer defect are

\[
 \Theta(nm^{-2/3})=\Theta(N/m)=\Theta(\operatorname{Cat}_m).
\]

All counts and quantifiers check.  The upper bound \(s<12r\) is essential
for the displayed replication statement and was added during audit.

## 3. Regular parity obstruction

For the affine edge

\[
                         (\ell,u,\ell+u,\ell+2u)
\]

on four copies of \(\mathbb Z_g\), every degree is \(g\).  Five cross-part
pair types recover \((\ell,u)\) uniquely; the remaining type solves
\(2u=h-\ell\), so its codegree is at most two.  Weight \(1/g\) on each edge
is a fractional perfect matching.

If \(g\) is even, an integral perfect matching would make the \(\ell\),
\(u\), and \(\ell+u\) coordinates permutations.  Modulo \(g\), the first
two sums add to zero, while the third is
\(\sum_{x\in\mathbb Z_g}x=g/2\ne0\).  The contradiction is exact.  Thus
even regularity, constant codegree, and exact fractional feasibility do not
replace an integral transferral hypothesis.

## 4. Completion by matching-aligned corridors

The readiness definition is sufficient: the off state lies in the partial
matching, every retained atom avoids the full two-state support, and the on
state adds precisely the prescribed uncovered outer pair.  Complete outer
supports and complete two-state middle supports must be disjoint between
absorbers; endpoints alone are not enough.

For ordered demands \(e_1,\ldots,e_h\), if every earlier selected candidate
deletes at most an \(\eta_{j,i}\)-fraction of list \(i\) and

\[
                         \sum_{j<i}\eta_{j,i}<1,
\]

greedy selection leaves a candidate at every step.  This proof is exact and
does not use independence assumptions beyond the displayed pointwise list
bound.

For independent random list choices, a collision event \(E_{ij}\) depends
on the two list variables \(i,j\), hence on at most \(2h-4\) other collision
events.  The symmetric local lemma therefore gives the exact sufficient
condition

\[
                         e\chi(2h-3)\le1
\]

for \(h\ge2\); \(h=1\) is immediate.  If supports have size at most \(b\),
the relevant incidence parameter is cross-list rather than within-list
pressure.  Namely, if

\[
 \lambda_{j\leftarrow i}
 =\max_{x\in\cup_{A\in\mathcal S_i}\operatorname{supp}A}
      \Pr_{B\sim\mu_j}[x\in\operatorname{supp}B]
 \le\lambda
\]

for every \(i\ne j\), a union bound gives \(\chi\le b\lambda\).  Fixed
private endpoints may have probability one inside their own list but zero
cross-pressure, as they should.  This verifies the useful checkable
incidence-pressure criterion in Corollary 5.3.

The endpoint degree shortcut is valid only with positive degree:

\[
 \delta(P_M|D_A)\ge\Delta(P_M|D_B)>0.
\]

The positivity correction was inserted during audit; without it the empty
balanced graph is a counterexample.

## 5. Exact independent-boundary resource ledger

Write the geodesic length in the explicit absorber as \(d\), so
\(R=d+1\), \(|P^-|=R\), and \(|P^+|=R+1\).  A guaranteed common physical
middle core consists of

* the common start resource: one;
* all transition unions \(Z_1,\ldots,Z_d\): \(d\);
* the shifted filler resources common to consecutive states: \(d-2\).

Its size is \(2d-1=2R-3\).  Since the two states use \(2R\) and \(2R+2\)
physical middle vertices, they have at most three off-only and five on-only
resources.  These are total physical counts.  A per-role bound requires
bipartitioning the alternating two-state overlay and orienting both states
coherently at installation time.  It is not automatic for an already
oriented residual matching.

The full outer support has exactly \(R+1\) vertices on each shore.  Thus a
disjoint bank obeys

\[
                         \sum_i(R_i+1)\le n.
\]

For generic \(R_i=\Theta(m)\), this forces \(h=O(n/m)\).  For
\(h=\Theta(K)\), average full support must instead be
\(O(n/K)=O(m^{2/3})\).  These are counting necessities/conservative reserve
bounds, not an existence proof for a corridor packing.

For a fixed lower endpoint, the exact number of upper endpoints at distance
below three is

\[
 \sum_{s=0}^{2}\binom{m-1}{s}\binom{m+1}{s+2}=\Theta(m^6).
\]

Consequently balanced exponential defect sets have a perfect matching in
the distance-at-least-three graph.  This certifies only geometric endpoint
pairing.  Ordered boundary roles, survival, matching alignment, and
resource-disjoint corridor selection remain necessary.

## 6. Topology audit

An outer-perfect ordered matching has \(n\) directed edges on a common
middle ground of \(n+K\) vertices, with indegree and outdegree at most one.
Therefore its number of directed path components, including isolates, is

\[
                         |V|-|E|=K,
\]

independently of its number of cycle components.

For a supplied replacement packet, delete its old palette edges to leave a
forest \(F_0\).  After contracting every component of \(F_0\), including
isolates, the replacement is an undirected linear forest exactly when

1. physical degrees are at most two; and
2. the contracted replacement multigraph is loopless and acyclic, with a
   parallel pair counted as a two-cycle.

This follows in both directions by expanding or contracting the unique
paths inside the trees of \(F_0\).  It is an undirected criterion.  If every
diamond orientation remains available, orient the resulting paths
consistently; otherwise directed-role feasibility is a separate row.

## 7. Final verdict and precise boundary

PASS after the following repairs, all present in the audited SHA:

* a Bertrand upper bound on the AP modulus;
* positive endpoint degree;
* explicit treatment of \(h=1\);
* complete-support independence;
* an internal-forest hypothesis for generic inserted states;
* role-coherent orientation scope;
* the exact \(R_i+1\) outer-support count; and
* separation of undirected cycle elimination from fixed-role orientation.

The proved theorem is sharp in the following sense: local logarithmic
degree, \(m^{1/3}\) pair-codegree, and Catalan middle surplus can coexist
with a Catalan-size Hall defect, whereas generic length-\(m\) corridors can
absorb only \(O(Km^{-1/3})\) defects.  The exact missing Boolean theorem is
therefore an absorber-aware core construction with leave \(O(n/m)\),
preinstalled or contained off states, endpoint Hall, and corridor incidence
pressure satisfying the greedy or local-lemma inequality.  Cycle removal
then requires a separate palette-neutral packet passing the contraction
test.  No claim of that Boolean construction, or of \(\nu=B\), is made.

## 8. Audited deterministic rebase

Sections 8--9 were added after the original audit and were checked
independently against two source theorems.

First,

```text
MATH_THEOREM_CATALAN_BALANCED_SUBCUBE_RESERVE_AND_EXACT_COLLAR_DEFECT_20260731.md
SHA-256 201f080014022cc9c9bad39409fd65436a28ff8037b227bd8f3fee14280bc11b
```

has an independently verified fractional collar completion.  The exact
negative-atom losses are

\[
 w_0\frac{m}{a(a-1)r},
 \qquad
 \frac{w_0}{\binom a2\binom{r+1}2},
\]

on disjoint trace types.  The stated \(\varepsilon_{m,a}\) lower bound on
every complement atom follows.  The three possible positive middle-load
types retain exactly the three margins minimized in
\(\sigma_{m,a}\); every other correction is harmless.  Hence the
full-support relative-interior theorem is correct for \(a\ge3,r\ge2\),
with \(\varepsilon=1-O(a^{-2})\) and
\(\sigma=(1-o(1))/m\) at the intended scale.

Each signed outer path is statewise a literal \(1\to2\) augmentor.  Giving
each of its eight triples of physical orientations weight \(\alpha/8\)
recovers coefficient \(\alpha/2\) on each oriented signed diamond.  This
is a rational augmentor superposition, not a disjoint or automatically
matching-ready bank.  Family (5.1) has a shared cross-state physical label,
so role alignment and full-support isolation remain necessary.

Second,

```text
MATH_THEOREM_CATALAN_ENDPOINT_BANK_TWO_SHADOW_EXTENDABILITY_20260731.md
SHA-256 41d0ee40060443233f65ddab87bca4abb7ee870ee975a49c1d519a6f96c11383
```

proves that a Catalan endpoint bank is independently matchable into either
two-step shadow.  Its Kruskal--Katona threshold, \(n=3\) base, and
transversal-matroid rank all audit exactly.  Thus separate one-sided
endpoint Hall is automatic in the two-coordinate recursion.

Finally, the stronger current theorem

```text
MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md
SHA-256 b0979c3c3cbaceda8159c3857f2dc396c0a9b3935bb4d8141e8b333ba2cdda3a
```

closes synchronization itself for \(n\ge4\).  Its exact dual-rank density

\[
                         r_{T^*}(A)\ge(C/N)|A|
\]

makes Edmonds' rank-sum inequality equal \(C\) term by term after pulling
the two dual matroids back through the child tail/head injections.  Hence a
common \(C\)-basis always exists.  The constant vector \(C/N\) also lies in
both base polytopes, giving a distribution on common bases with exact
uniform marginals and the stated additive-cost average.

These additions discharge the fractional capacity clause, both one-sided
endpoint-Hall clauses, and synchronized incidence for the deterministic
recursive route.  They do not transfer to an arbitrary \(p=m^{-1/3}\)
thinning and do not prove integral off-state-aligned collar rounding,
resource-disjoint augmentor selection, punctured side degree/anchor caps,
or the contracted physical forest condition.
