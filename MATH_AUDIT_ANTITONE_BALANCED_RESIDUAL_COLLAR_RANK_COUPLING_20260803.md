# Self-audit: antitone balanced residual--collar rank coupling

**Date:** 2026-08-03  
**Audited file:**
`MATH_THEOREM_ANTITONE_BALANCED_RESIDUAL_COLLAR_RANK_COUPLING_20260803.md`  
**Method:** independent symbolic proof audit.  No computation or finite
search is used.

## 0. Verdict

**GO at exactly the anonymous rank-incidence scope stated.**

The joint construction attains the averaging lower bound, the fixed-load
Gale formula is exact, and equitable residual loading is extremal for all
collar cuts simultaneously.  The theorem does not produce named nested
Boolean flags and explicitly excludes that inference.

The result is a factorized strengthening/diagnostic form of the already
proved noncontiguous rank-law equitable decomposition.  Its genuinely new
content is the exact fixed-residual min--max together with the universal
majorization statement explaining why balanced residual loads, rather than
parity-block full chunks, are the optimal collar interface.

## 1. Collar balancing audit

An initial zero--one matrix exists because each `m_j<=W`: choose `m_j`
distinct rows independently for every column.

If row `u` has degree at least two larger than row `v`, then
`N(u)\not\subseteq N(v)`; otherwise `deg(u)<=deg(v)`.  Moving an edge in
`N(u)\setminus N(v)` from `u` to `v` preserves the column degree and the
zero--one condition.  The squared-degree potential drops strictly.  Thus
termination gives degrees differing by at most one, and the exact heavy-row
count follows from the total.  This verifies Lemma 1.1, including `W=1`,
empty columns, and zero total mass.

## 2. Antitone histogram audit

The residual heavy set has size `a`, the collar heavy set size `b`.  The
smallest possible intersection of two subsets of a `W`-set with those
sizes is `(a+b-W)_+`, and it is attained by antitone placement.

* For `a+b<W`, combined loads are base and base plus one.
* For `a+b=W`, every combined load is base plus one.
* For `a+b>W`, combined loads are base plus one and base plus two, with
  `a+b-W` rows of the latter kind.

These are exactly the floor and ceiling of the combined average.  Hence
the maximum is the information-theoretic optimum.  No owner label exists
at this projection, so the row permutation is legitimate.

## 3. Residual matching audit

Replacing residual edge `e` by `n_e` parallel copies gives a bipartite
multigraph of maximum degree at most `W`.  Balanced proper `W`-edge
colouring produces exactly `W` matchings with equitable cardinalities.
Superposing the independently balanced collar rows after an antitone row
permutation preserves every residual edge multiplicity and matching
constraint, and preserves every collar column multiplicity.

For a path rank graph, the maximum-degree rows are exactly

\[
                          n_s+n_{s+1}\le W,
\]

together with `n_s<=W` at isolated or endpoint ranks.  A matching is
exactly a set with no adjacent residual ranks.  Collar ranks are represented
by disjoint isolated columns and have no mutual exclusion.  If a numerical
rank occurs in both banks, it must be coalesced first; the theorem states
this scope condition.

## 4. Fixed-load Gale audit

At total depth `t`, the collar capacities are `c_i=t-h_i`, so
`t>=max h_i` is necessary.  The source--column--row--sink network has
integral capacities `m_j,1,c_i`; its integral max flows are exactly the
desired zero--one collar matrices.

For a set `Q` of collar columns, the corresponding cut is

\[
                     \sum_{j\in Q}m_j
       \le \sum_i\min(c_i,|Q|).
\]

For fixed `|Q|=q`, the left side is maximized by the `q` largest `m_j`,
giving the sorted-column form.  The conjugate row form follows by forcing
`(m_j-W+x)_+` entries of column `j` into any `x` rows and taking the `x`
least capacities, which are the rows with the `x` largest `h_i`.

Solving

\[
 x t-\sum_{i=1}^{x}h_i^\downarrow
 \ge \sum_j(m_j-W+x)_+
\]

for integral `t`, and adjoining `t>=h_1^downarrow`, gives formula (0.7)
exactly.  No asymptotic estimate is hidden.

## 5. Majorization audit

For fixed integral total, every load vector majorizes the equitable vector.
For `t>=max h_i`, both vectors lie in `[0,t]`.  The function

\[
                         f_q(x)=\min(t-x,q)
\]

is concave there: its slope changes from zero to minus one.  Karamata gives

\[
                   \sum_i f_q(h_i)\le\sum_i f_q(\bar h_i)
\]

for every `q`.  These are exactly the right sides of all sorted-column Gale
cuts.  Therefore any depth feasible for `h` is feasible for the equitable
vector.  The explicit balanced collar plus antitone coupling attains the
combined averaging bound, proving the exact optimum for the equitable
vector.

The condition `t>=max h_i` is essential for this formulation; the theorem
includes it.

## 6. Scope audit

The theorem proves no assignment of named subsets.  In the literal Boolean
problem, a row is eventually an owner `T`, every assigned target must lie
inside `T`, and all assigned targets in that row must be nested.  Arbitrary
antitone row relabelling can violate containment.  Separate rankwise
matching or matroid intersection does not enforce cross-rank comparability.

Thus the remaining lower-side gate is exactly a perfect matching in the
combined pattern/owner/named-target configuration hypergraph.  Chronology,
occurrence, upper-deck, and residence constraints are further gates.  The
audit therefore accepts only the implication

\[
 \boxed{
 \text{feasible joint rank marginals}
 \Longrightarrow
 \text{optimal anonymous integral row schedule}.}
\]

It rejects any claim that this alone proves `nu(k)<=B(k)+O(1)` or
`nu(k)=B(k)`.
