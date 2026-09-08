# Thread D: K16 order-eight provider-codegree theorem

**Date:** 2026-07-30  
**Scope:** exact proper-colour source-cover separator for the K16 quotient;
solver-free mathematics and finite catalogue replay.  This is not a carrier
existence theorem, SAT result, compiler certificate, or K16 word.

## 1. Result

No order-eight proper-colour Hall no-good exists for any of the three AAAB
middle-orbit representatives in the 21-case any-unit quotient.  The proof
has two complementary layers:

1. a 91,806-pair quotient audit gives maximum distinct-colour provider
   codegree three, while exact phase-aware profile censuses certify minimum
   residual provider size five for representatives A380, A378, and A396; and
2. a scope-complete provider-hyperedge union census checks all 1,925 frozen
   O80 semantic profiles and reaches the same zero-cut conclusion directly.

The audited unit maps transport the three representatives to all nine raw
AAAB middle cases.  The result does **not** cover the other 18 non-AAAB
formulas in the 21-case quotient.

Because no semantic collar is forbidden, the correct CNF update is empty.
No redundant clause family or generic timed SAT portfolio was launched.

## 2. Scalable exact separator

For a fixed collar \(\gamma\), let \(G_\gamma\) be the residual bipartite
graph from 427 uncovered colours to 428 endpoint slots.  For a literal
colour--target incidence \(e=(c,t)\), let \(P_e\) be its exact set of source
providers.  For \(Z\) in the residual source shore define

\[
 F_\gamma(Z)=\{e:P_e\subseteq Z\},\qquad
 \delta_\gamma(Z)=427-\nu(G_\gamma-F_\gamma(Z)).
\]

If \(M\) is a matching saturating the 427-colour shore of \(G_\gamma\), deleting
\(F_\gamma(Z)\) removes at most \(\nu(F_\gamma(Z))\) edges of \(M\).
Therefore

\[
 \boxed{\delta_\gamma(Z)\leq\nu(F_\gamma(Z)).}       \tag{2.1}
\]

An order-eight proper-colour obstruction requires

\[
 \nu(F_\gamma(Z))\geq9
 \quad\text{and}\quad
 \nu(G_\gamma-F_\gamma(Z))\leq418.                 \tag{2.2}
\]

This does not require enumerating \(\binom{428}{8}\) source sets.  If an
eight-cover \(Z\) were bad and

\[
 U=\bigcup_{e\in F_\gamma(Z)}P_e,
\]

then \(F_\gamma(U)=F_\gamma(Z)\).  The frozen order-at-most-seven theorem
forces \(U=Z\); otherwise the same deficiency already occurs on
\(|U|\leq7\).  Every provider set has size at least five, so at most four
observed provider supports generate \(Z\).  The exact generator is:

* every observed eight-provider set;
* every size-eight union containing a seven-provider set, found through
  indexed intersections of sizes six, five, and four; and
* the size-eight closure of the approximately 147 five/six-provider sets.

Once \(Z\) is known, its 93 subsets of sizes five through eight recover all
of \(F_\gamma(Z)\).  The incidence-count and deleted-matching filters in
(2.2) precede any 427-by-428 replay.

## 3. Exact codegree-three theorem

For each tight lower-q1 quotient colour \(c\), let \(A(c)\) be the set of
B-source nodes having an outgoing option of colour \(c\).  Exact catalogue
replay gives

\[
 |A(c)|=7^{14},8^{415}
\]

and the complete distinct-colour intersection histogram

\[
 |A(c)\cap A(d)|=
 0^{80144},1^{11416},2^{240},3^6.                 \tag{3.1}
\]

Thus

\[
 \boxed{\max_{c\ne d}|A(c)\cap A(d)|=3.}          \tag{3.2}
\]

Every residual incidence provider set is a subset of its carrier \(A(c)\).
The frozen O80 profile family checks directly that every residual incidence
has at least five providers.  A separate phase-aware replay proves the same
for A378 and A396: each has 960 terminal AAAB paths, 4,340 semantic profiles,
33,600 literal collars, and collar-weighted minimum histogram
\(5^{22400},6^{11200}\).  For carrier degree eight the bound five is automatic
after the target and two collar-source losses.  The replay checks literally
the 14 degree-seven carrier colours; it finds no size-below-five witness.

This second fact is not implied by the quotient codegree table alone: two
quotient source nodes can support the same colour orbit in different phases.
That is why the dedicated A378/A396 audit is part of the theorem certificate.

### Theorem 3.1

For every eight-source set \(Z\) in a collar whose residual provider sets
have certified minimum size five,

\[
 \nu(F_\gamma(Z))\leq8.
\]

**Proof.**  Suppose a nine-edge matching in \(F_\gamma(Z)\) exists.  Its
incidences have nine distinct colours and targets, with provider supports
\(P_1,\ldots,P_9\subseteq Z\), each of size at least five.  Put
\(d_z=|\{i:z\in P_i\}|\).  Then

\[
 \sum_{i<j}|P_i\cap P_j|=\sum_{z\in Z}\binom{d_z}{2}. \tag{3.3}
\]

There are at least 45 memberships.  Convexity over eight points gives a
lower bound 105 in (3.3), while (3.2) gives the upper bound
\(3\binom92=108\).  If there were at least 46 memberships, convexity gives
110, a contradiction.  Thus every \(|P_i|=5\).

Let \(Q_i=Z\setminus P_i\).  These are nine triples.  From

\[
 |P_i\cap P_j|=2+|Q_i\cap Q_j|\leq3
\]

the triples form a linear 3-graph: two meet in at most one point.  At any
point, the remaining pairs in incident triples are disjoint subsets of the
other seven points, so its degree is at most three.  Total triple incidence
is therefore at most \(8\cdot3=24\), contradicting the required
\(9\cdot3=27\).  \(\square\)

Combining Theorem 3.1 with (2.1) proves
\(\delta_\gamma(Z)\leq8\).  Hence order eight has no proper-colour
source-cover separator.

## 4. Independent provider-union replay

The complete O80 audit independently generates the order-eight covers rather
than relying on Theorem 3.1.  It scans

* 1,925 semantic profiles and 22,400 collars;
* 781,930 semantic source-cover candidates;
* 9,099,000 candidates with collar multiplicity.

The exact filters give

\[
\begin{array}{c|r|r}
\text{killed incidences}&\text{semantic disposition}&
                         \text{collar multiplicity}\\ \hline
8&9,405\text{ incidence-budget safe}&109,480\\
9&772,525\text{ deleted-matching safe}&8,989,520.
\end{array}
\]

Every nine-incidence deleted graph has matching number one.  Thus zero full
residual matchings are needed and zero violations are emitted.  The audit
status is `COMPLETE_NO_ORDER8_SEPARATOR_IN_SCOPE`.

This hyperunion replay is deliberately O80-specific.  The broader AAAB
conclusion uses Theorem 3.1 plus the separate literal minimum-provider audit;
neither argument is extended to a non-AAAB shore pattern.

## 5. CNF interface and exact remaining gate

For a future violating AAAB profile, all proof data \((Z,C,N(C))\) are
certificate-only.  Group bad profiles by terminal \((e,f,s)\), reconstruct
its exact 35 residence-safe first-B options, and let `Good` be those not
certified bad.  The compact option-only clause is

\[
 \neg x_e\vee\neg x_f\vee\neg x_s
       \vee\bigvee_{g\in\mathrm{Good}}x_g.          \tag{5.1}
\]

Logically this is
\(\neg p_{ef}\vee\neg x_s\vee\bigvee_{g\in\mathrm{Good}}x_g\), but the
expanded form avoids the private prefix-variable numbering.  Semantic option
keys, not raw IDs, transport under \(U(15)\).  A certificate may transport
within its audited middle orbit; it must not be reused across another middle
representative or shore pattern without literal replay.

Order eight produces no bad profile on any AAAB representative, so (5.1)
contributes zero clauses to all three AAAB formulas and there is no
strengthened SAT candidate to promote.  The next proper-colour source-cover
order is nine.  The stronger two-collar co-singleton gate
\(\kappa_{\gamma h}(d)\leq2\) remains separate.

## 6. Frozen artifacts

```text
scratch/audit_threadD_k16_distinct_colour_provider_codegree_20260730.py
scratch/threadD_k16_distinct_colour_provider_codegree_20260730.audit.json
  payload e7ba51e1e8ac933fb0109b1ee601bffc5852896b7d6cf499d7d224b486bee359

scratch/threadD_k16_four_provider_colour_closure_20260730.audit.json
  O80 provider-size histogram 5^9630 6^270685 7^6293660 8^772525
  payload b917789b161f8db141ab5e3b6d288f6c31e25328f78b727d6733c368187cb339

scratch/audit_threadD_k16_all_aaab_min_provider_20260730.py
scratch/threadD_k16_all_aaab_min_provider_20260730.audit.json
scratch/threadD_k16_all_aaab_min_provider_20260730.resource.txt
  A378/A396 collar-minimum histogram 5^22400 6^11200 for each
  payload f46ba09b2140f12dc401ba9a349977e78704635d0960e835c3b23d5edf093576

scratch/audit_threadD_k16_aaab_sourcecover8_separator_20260730.py
scratch/threadD_k16_aaab_sourcecover8_separator_20260730.audit.json
  payload 99a30911d8dae05561dcb4ffa310ff83a0a3223b37f4a0f957cd5cbf15202bdd

scratch/threadD_k16_aaab_sourcecover8_20260730.resource.txt
scratch/test_threadD_k16_order8_separator_20260730.py
```

The numerical codegree table was independently replayed locally and on H100;
the frozen payload above makes its minimum-provider premise explicit.  The
phase-aware A378/A396 replay used one H100 CPU under a 1 GiB address-space and
120-second CPU cap, completed in 50.73 seconds, used 49,152 KiB maximum RSS,
and no swap.  The hyperunion audit used one H100 CPU under a 1 GiB
address-space and 900-second CPU cap, completed in 338.65 seconds, used
69,792 KiB maximum RSS and no swap.  Neither run invoked a SAT/LP/CP solver.
