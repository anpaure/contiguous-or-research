# Thread D: first coupled four-provider colour closure

**Date:** 2026-07-30  
**Scope:** exact residual quotient assignment graphs; integral bipartite
matching only.  This is a necessary colour/order/history separator, not a
carrier existence theorem and not a SAT result.

## 1. Residual coloured graph

Fix a legal collar \(\gamma\), including its rail order and its current
three-entry insertion history.  Let \(S_\gamma,T_\gamma\) be the remaining
source and target slots and let \(E_\gamma(c)\) be the literal residual
option edges of an uncovered tight q1 colour \(c\).  Parallel catalogue
options are retained when the residual graph is built; they may be collapsed
only after their colours have been recorded.

For \(C\) contained in the uncovered colour set, put

\[
 H_\gamma(C)=\bigl(S_\gamma,T_\gamma,
                    \bigcup_{c\in C}E_\gamma(c)\bigr).
\]

Every perfect residual assignment uses a matching when restricted to its
\(C\)-coloured edges.  Consequently

\[
 \mu_\gamma(C)\leq \nu(H_\gamma(C)).                 \tag{1.1}
\]

Thus \(\nu(H_\gamma(C))<|C|\) is an exact no-good for the collar.  This is
strictly stronger than the separate colour--source and colour--target Hall
projections because it retains their endpoint correlation.  It is still a
relaxation of perfect-assignment extendability, so failure to find such a
set is not a feasibility proof.

## 2. Fixed-source-cover closure theorem

For \(Z\subseteq S_\gamma\), define

\[
 N_{\gamma,Z}(c)=
 \{t\in T_\gamma:\exists s\in S_\gamma\setminus Z,
                         (s,t)\in E_\gamma(c)\}
\]

and

\[
 h_\gamma(Z)=
 \max_{C}\left(|C|-\left|\bigcup_{c\in C}N_{\gamma,Z}(c)\right|\right).
                                                        \tag{2.1}
\]

### Theorem 2.1 (exact coupled Hall separator)

If \(h_\gamma(Z)>|Z|\), an optimizing set \(C\) satisfies

\[
 \mu_\gamma(C)\leq \nu(H_\gamma(C))
 \leq |Z|+|N_{\gamma,Z}(C)|<|C|.          \tag{2.2}
\]

Hence the semantic guard selecting \(\gamma\) is false.  Conversely, every
violation of the coloured-edge matching relaxation (1.1) is detected by
some \(Z\).

**Proof.**  The vertices
\(Z\cup N_{\gamma,Z}(C)\) cover every edge of \(H_\gamma(C)\), proving the
middle inequality in (2.2).  Conversely, by Koenig's theorem, a minimum
vertex cover of \(H_\gamma(C)\) may be written as
\(Z\cup N_{\gamma,Z}(C)\) for its source part \(Z\).  This proves both
claims. \(\square\)

For fixed \(Z\), (2.1) is not an exponential search.  It is the ordinary
Hall deficiency of the bipartite graph

\[
 c\sim t \quad\Longleftrightarrow\quad
 t\in N_{\gamma,Z}(c).
\]

If this graph has \(r_Z\) colours on its left and maximum matching size
\(m_Z\), then

\[
 h_\gamma(Z)=r_Z-m_Z.                       \tag{2.3}
\]

Alternating reachability from its unmatched colours returns a literal
optimizing witness \(C\).  Equivalently, (2.1) is the max-weight closure
network with unit colour profits, infinite colour-to-target implications,
and unit target costs.

## 3. Why four providers is the first new layer

In the K16 one-collar residual graph, every literal colour--B-target
incidence has at least four source providers.  Before fixing the collar the
audited quotient multiplicities are six or seven.  The residual construction
can lose only

1. the ordered-away source \(x_3\), and
2. the history-special source \(x_4\).

The collapsed BA target starts with seven or eight providers and therefore
has at least five after the same losses.  These are literal provider counts,
not a freeness assumption.

The target projection has already been audited to satisfy Hall for all 427
uncovered colours.  If \(|Z|\leq3\), no colour--target incidence is erased,
so \(N_{\gamma,Z}(c)=N_{\gamma,\varnothing}(c)\) for every \(c\).  Therefore

\[
 h_\gamma(Z)=h_\gamma(\varnothing)=0\leq |Z|.          \tag{3.1}
\]

There is consequently no genuinely coupled separator at source-cover order
zero, one, two, or three.  The coarse uniform bound makes order four the
first *a priori* possible new layer.

For \(|Z|=4\), an incidence can disappear only when its exact residual
provider set equals \(Z\).  It is therefore sufficient and exact at this
first layer to enumerate the deduplicated literal four-provider sets; one
must not enumerate all \(\binom{428}{4}\) source sets or all colour subsets.
For each such \(Z\), one matching computes (2.3).  A violation is exactly

\[
             m_Z < 427-4=423.                         \tag{3.2}
\]

The threshold is adjusted mechanically if a different collar leaves a
different number of uncovered colours.

### Exact O80 refinement through order seven

The complete AAAB_A380 semantic-profile audit strengthens the coarse bound:
the minimum residual provider count is actually five throughout all 1,925
profiles (22,400 collars with multiplicity).  Its provider-incidence census
is

\[
 5^{9630},\qquad6^{270685},\qquad
 7^{6293660},\qquad8^{772525}.               \tag{3.3}
\]

Consequently there is no order-four candidate at all.  At order five the
9,630 exact provider sets each erase exactly one incidence, so deleting-edge
monotonicity gives deficiency at most one, far below the required six.

The same audit is scope-complete at order six.  Since there are no
four-provider incidences and every five-provider set carries one incidence,
a six-set with no exact six-provider incidence erases at most its six
five-subsets and is automatically safe.  It is therefore enough to scan the
270,685 exact six-provider sets.  Of these,

* 269,080 erase one incidence and are safe without another matching; and
* 1,605 erase seven incidences, but exact matching replay gives deficiency
  exactly one in every case.

Thus no coloured-edge Hall separator exists with \(|Z|\leq6\) in the
audited AAAB \(\mathcal O_{80}\) family.

At order seven, a violation needs at least eight erased incidences.  Every
such cover is the union of at most three exact provider hyperedges of sizes
five through seven; this gives a scope-complete finite generation rather than
\(\binom{428}{7}\) source sets.  Across the 1,925 semantic profiles the
generator retains 38,220 candidates (443,980 with collar multiplicity).
Every retained candidate erases exactly eight incidences.  In every case
those incidences have

\[
  \text{one distinct colour},\qquad
  \text{eight distinct targets},\qquad
  \nu(E_{\rm erased})=1.                       \tag{3.4}
\]

Deleting an edge family \(F\) from a graph with a perfect matching lowers
its matching number by at most \(\nu(F)\): intersect the old perfect matching
with \(F\) and retain every other matched edge.  Equation (3.4) therefore
bounds the new Hall deficiency by one, far below the strict order-seven
threshold eight.  No 427-by-427 replay is needed for this final step.

Thus no coloured-edge Hall separator exists with \(|Z|\leq7\) in the
audited AAAB \(\mathcal O_{80}\) family.  The first unresolved source-cover
order there is eight.  This is a positive statement only about the
coloured-edge-matching relaxation; it neither proves residual assignment
extendability nor settles the stronger two-collar co-singleton obstruction.

## 4. Clause and covariance scope

If alternating reachability returns a violating colour set \(C\), the CNF
consequence is simply the negation of the complete semantic collar guard.
For the AAAB collar written as \((p_{ef},s,g)\), this is

\[
             \neg p_{ef}\vee\neg x_s\vee\neg x_g.    \tag{4.1}
\]

No new colour-selection variables are required.  The provider graph used to
certify (4.1), including its order and one-step history filters, must be
stored or replayed with the row.

For comparison, after additionally fixing the next B edge \(h\), the three
fixed tight colours are distinct and the residual has 427 edges, 426
uncovered colours, and one repeat.  For an uncovered colour \(d\), define

\[
 \kappa_{\gamma h}(d)=
 \min_M |M\cap E(\{c(s),c(g),c(h),d\})|.
\]

Every completion requires \(\kappa_{\gamma h}(d)\leq2\).  A certified value
at least three gives the five-option no-good
\(\neg x_e\vee\neg x_f\vee\neg x_s\vee\neg x_g\vee\neg x_h\).
This is the smallest co-singleton two-collar separator, but it is a separate,
stronger audit; no such row is claimed by the source-cover census here.

Multiplication by a unit of \(\mathbb Z_{15}\) bijects sources, targets,
colours, histories, and exact provider sets.  Hence the theorem and every
literal witness transport under the proved any-unit-voltage action.  The
separator *algorithm* is therefore valid in each of the 21 orbit formulas.
The current finite audit enumerates the AAAB \(\mathcal O_{80}\) semantic
profiles only; it does not claim that the other two middle orbits or the six
non-AAAB shore patterns have been scanned until their own literal collars
are passed through the same routine.

## 5. Executable audit

The solver-independent order-at-most-six implementation is

```text
scratch/audit_threadD_k16_four_provider_colour_closure_20260730.py
```

It reconstructs the 1,925 deduplicated AAAB_A380 residual profiles, records
all literal provider sets, and tests source-cover orders four through six.
It uses the exact incidence-deletion budget before invoking a matching and
therefore needs only 1,605 nontrivial matching computations.  Its output is
fail-closed: a reported no-good includes \(Z\), the alternating Hall witness
\(C\), its neighbourhood, the matching size, and the exact profile.  The
frozen audit is `PASS` with payload

```text
b917789b161f8db141ab5e3b6d288f6c31e25328f78b727d6733c368187cb339
```

and zero violations at orders four, five, and six.  This means only that
these coloured-edge-matching layers found no obstruction in the stated
profile family.

The fail-closed order-seven continuation is

```text
scratch/audit_threadD_k16_aaab_sourcecover7_separator_20260730.py
scratch/threadD_k16_aaab_sourcecover7_separator_20260730.audit.json
```

It verifies the preceding payload before using it, generates the complete
provider-hyperedge union family, and records the one-colour/eight-target
deleted-edge certificates.  The frozen payload is

```text
48fd6926ecf620e286b0b0785c2f83e59c1fbc9ab1558dbb75cd1ec110d4afb8
```

The H100 CPU run used one Python process under a 1 GiB address-space and
900-second CPU cap.  It finished in 142.69 seconds, used no solver and no
swap, and emitted zero clauses because it found zero violating guards.

Frozen identities are

```text
scratch/audit_threadD_k16_four_provider_colour_closure_20260730.py
  3d6500acecde95004da91e023e1f4d1608e5c62c0202b89775fe0f673810540c
scratch/threadD_k16_four_provider_colour_closure_20260730.audit.json
  376c1d71b8a55a93cb9a87bcd157bec07deefebdcbacc5bb56d855197da00866
scratch/audit_threadD_k16_aaab_sourcecover7_separator_20260730.py
  0c1be5f5c224b0389472d24ef3b213a3beeda22c4047d9472567d1f6d2b09e58
scratch/threadD_k16_aaab_sourcecover7_separator_20260730.audit.json
  ad46a4ac8718694d6d151a6749d619dd2a75ec245c97f0482ca1aa79115bb248
scratch/threadD_k16_aaab_sourcecover7_20260730.resource.txt
  df210a68aa2350d5b35ae0cdaa5189e1eef58ea186948403bef1bf711b93ad47
```

`scratch/test_threadD_k16_proper_colour_separator_20260730.py` replays both
payloads, the dependency hash, the scope flags, and the deleted-star matching
bound.  Its three lightweight tests pass without a solver.
