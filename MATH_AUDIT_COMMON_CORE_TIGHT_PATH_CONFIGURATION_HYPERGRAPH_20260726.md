# Audit of the common-core tight-path configuration hypergraph

Date: 2026-07-26

Source audited:
`MATH_THEOREM_COMMON_CORE_TIGHT_PATH_CONFIGURATION_HYPERGRAPH_20260726.md`.

## 0. Verdict

The degree formulas, arbitrary-rank pair enumerator, maximum codegree,
edge-size asymptotic, scalar hole identity, edge transitivity, and rooted
matching threshold are correct.

Two scope corrections were required and have been patched.

1. The physical intersection bound applies to edges at **distinct
   roots**.  It is false for arbitrary distinct parallel edges: changing
   only the order of core labels can leave the entire target part
   unchanged.
2. The hypergraph fixes one phase-tag word globally and lets each edge
   choose its core.  Thus a perfect matching is the free-core,
   synchronized-tag form of CCTPF, not literally the earlier
   fixed-core/root-dependent-tag formulation.  A near-perfect matching at
   the stated scale nevertheless gives an approximate fusion and is
   sufficient for constant one.

## 1. One-target degrees

Let \(X\) have rank \(m+r\), set \(q=|r|\) and
\(\ell=H-r\).  The number of tops containing \(X\) is

\[
\binom{m-r}{H-r}=\binom{m-r}{\ell}.
\]

For a fixed containing top and one fixed active phase, the deletion set
\(U\setminus X\) must occupy a prescribed \(\ell\)-interval of tail
positions.  It has \(\ell!\) internal orders, and all remaining labels
have \((M-\ell)!\) orders.  Equal-length deletion intervals at different
phases of an injective word are distinct, so summing over the \(b_q\)
active phases has no overcount.  Hence

\[
d(U,X)=b_q\ell!(M-\ell)!,
\]

and

\[
d(X)=b_q{(m-r)!(m+r)!\over s!}
=M!{b_q\over\Lambda_q}.
\]

Every root has \(M!\) rooted words.  Parallel words are intentionally
retained, so \(D=M!\) is exact.  Distinct roots have codegree zero.

## 2. Arbitrary-rank target pair codegree

For distinct targets \(X,Y\), let

\[
a=M-|X\cup Y|,quad b=|Y\setminus X|,quad
c=|X\setminus Y|,quad d=|X\cap Y|.
\]

A common top adds exactly \(a\) labels outside \(X\cup Y\).  Since the
available outside set has size \(s+a\), there are
\(\binom{s+a}{a}\) possible tops.  For one phase pair whose positional
deletion intervals overlap in \(a\) positions, the four position cells
have sizes \(a,b,c,d\), and assigning their label cells takes
\(a!b!c!d!\) bijections.  Every common word recovers its top and unique
phase pair, so there is no multiplicity loss.  Therefore

\[
d(X,Y)={(s+a)!\over s!}b!c!d!\,\Theta_{r,t}(a).
\]

Dividing by \(d(X)\) gives exactly

\[
{d(X,Y)\over d(X)}
={\Theta_{r,t}(a)\over b_q}
 {b!\over(s+a+1)_b}{c!\over(d+1)_c}.
\]

The autocorrelation expression for \(\Theta\) is also exact: after
writing the second phase as \(j+u\), its interval overlap depends only on
\(u\), while the fixed tag word contributes precisely
\(\alpha_{q,q'}(u)\).

## 3. Maximum pair codegree

For positive overlap \(a>0\), a fixed first interval has at most two
relative positions giving a proper partial overlap, or
\(|\ell-h|+1\le b+c+1\) positions when the shorter interval is fully
contained.  Thus, with \(u=b+c\ge1\),

\[
{\Theta_{r,t}(a)\over b_q}\le u+1.
\]

Both denominator bases in the relative formula are at least
\(m-3H\), so

\[
{d(X,Y)\over d(X)}
\le{(u+1)u!\over(m-3H)^u}\le{4\over m}.
\]

For \(a=0\), there are at most \(L\le m\) relative phases and
\(u=\ell+h\ge2\), giving

\[
{d(X,Y)\over d(X)}
\le {m u!\over(m-3H)^u}\le{4\over m}.
\]

Interchanging the targets yields the minimum-degree form.  A root-target
pair has ratio

\[
{d(U,X)\over D}={b_q\over\binom M\ell}.
\]

The only possible \(\ell=1\) row has \(b_{H-1}=0\).  Every
positive-degree row has \(2\le\ell\le2H-1<M/2\), and hence the ratio is
at most \(M/\binom M2\le3/m\).  Thus

\[
\Delta_2\le4D/m.
\]

For nested \(X\in\mathcal X_0\),
\(Y\in\mathcal X_1^+\), the same-phase configurations give

\[
{d(X,Y)\over D}\ge{1+o(1)\over m},
\]

so the exact order is

\[
\Delta_2=\Theta(D/m).
\]

## 4. Edge size and vertical-spine mass

The cap affects only \(O(\sqrt H)\) depths and changes the raw Gaussian
sum by \(O(H^{3/2})\); integer rounding costs \(O(H)\).  The omitted
Gaussian tail past the critical \(H\) is also lower order.  Therefore

\[
\sum_{q=1}^{H-1}b_q
=\left({\sqrt\pi\over2}+o(1)\right)m^{3/2},
\]

and

\[
k=L+2\sum_{q=1}^{H-1}b_q
=(\sqrt\pi+o(1))m^{3/2}.
\]

Here \(k\) is the target-part size.  Each rooted hyperedge has total
cardinality \(k+1\), a distinction which does not alter any asymptotic or
the one-bite calculation.

Consequently \(k\Delta_2/D=\Theta(\sqrt m)\).

The stronger edgewise lower bound is also correct.  For each
\(q\le\sqrt m\), every phase active at depth \(q\) supplies the nested
upper pair at depths \(q-1,q\).  Its normalized same-phase codegree is at
least

\[
{1\over m+q}{b_q\over\Lambda_q}=\Omega(1/m).
\]

There are \(b_q=\Theta(m)\) such pairs per depth and
\(\Theta(\sqrt m)\) depths, giving normalized pair mass
\(\Omega(\sqrt m)\) in every edge.

## 5. Physical intersections

For two paths at distinct roots, the common-core span bound gives at most
\(\ell\) equal traces at deletion length \(\ell\).  Summing the loose
range \(1\le\ell\le2H\) gives

\[
|P(e)\cap P(f)|\le H(2H+1).
\]

Since \(k=\Theta(m^{3/2})\), the ratio is
\(O(\log m/\sqrt m)=o(1)\).  The qualifier on the roots is essential:
same-root parallel states may have identical target parts.  Rooted
matchings never use two such states, so the corrected version is the one
relevant to a nibble.

## 6. Hole identity and matching precision

The target count and forced shortage are

\[
B=W+2\sum_{q=1}^{H-1}N_q,
\qquad
\Delta=B-kN
=(W-LN)+2\sum_{q=1}^{H-1}(N_q-b_qN)=o(W).
\]

A matching of size \(t\) covers exactly \(kt\) target vertices, so its
uncovered target count is exactly

\[
\mathfrak H=\Delta+k(N-t).
\]

Using \(k\sim\sqrt\pi m^{3/2}\) and \(N=\Theta(W/m)\),

\[
\mathfrak H=o(W)
\iff N-t=o(N/\sqrt m).
\]

This equivalence is exact for the protected target set of this
hypergraph.  The two depth-\(H\) boundary layers are outside it and cost
only \(2N=o(W)\) in the final compiler.

## 7. Edge transitivity and convex collapse

For edges \((U,z)\), \((U',z')\), the coordinate permutation defined
positionwise by \(z_i\mapsto z'_i\) maps one edge to the other because
the phase-tag word is globally fixed.  Hence the multihypergraph is
edge-transitive and has \(|E|=ND\).

Averaging a maximum matching gives a fractional edge colouring of total
weight \(|E|/\nu\), while summing all edge-cover constraints gives the
reverse inequality.  Therefore

\[
\chi_f'={ND\over\nu}.
\]

Writing \(\nu=N-\ell\) proves

\[
\chi_f'=D+o(D/\sqrt m)
\iff \ell=o(N/\sqrt m).
\]

## 8. Exact relation to calibrated CCTPF

A perfect matching is equivalent to the free-core CCTPF in which every
root uses the same positional tag word.  The previously stated CCTPF is
broader in one direction (root-dependent tag placements) and narrower in
another (preselected cores), so the two formulations are not literally
equivalent.

The near-perfect threshold is nevertheless sufficient.  Complete the
missed roots by arbitrary states.  Adding \(\ell=o(N/\sqrt m)\) states
cannot increase holes and creates at most

\[
k\ell=o(W)
\]

repeat occurrences.  If \(M_0,E_0\) are the resulting middle hole and
repeat counts, then the fixed middle occurrence mass \(LN\) gives

\[
LN+M_0=W+E_0.
\]

Compile every state with its \(L+2H\) delayed-atom block.  Appending the
middle holes gives baseline \(W+E_0+2HN=W+o(W)\).  Append the aggregate
protected signed holes, the two boundary layers, and the product-SCD
exterior, all of total length \(o(W)\).  Thus

\[
\nu(\mathcal K_{\rm cc})=N-o(N/\sqrt m)
\]

implies constant one.  It is the exact approximate fixed-word fusion
target, while a perfect matching is the exact synchronized-tag CCTPF
target.
