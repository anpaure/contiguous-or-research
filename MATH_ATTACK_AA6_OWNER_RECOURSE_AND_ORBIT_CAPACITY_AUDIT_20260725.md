# Independent audit of AA6 owner recourse and orbit capacity

Date: 2026-07-25

Audited source:
`MATH_ATTACK_AA6_OWNER_RECOURSE_AND_ORBIT_CAPACITY_20260725.md`.

Method: pure mathematics only.  No search, computation, solver, or external
black box is used.

## 0. Verdict

The two principal theorems pass.

1.  For the owner-map distance defined in the source,

    \[
    d_{\rm own}(F,G)=n,d_{\rm row}(F,G)
    \]

    is exact.  Combined with the canonical disjoint-packet family, it gives

    \[
    \operatorname{Rec}_{\rm own}
    \ge\left(\frac1{256}-o(1)\right)W
    \]

    for every exact-factor path from the canonical MSW factor to an FSP
    endpoint.  No restriction on coordinate support is used.

2.  The moving-label orbit bounds

    \[
    |B|\ge\frac1D\sum_O(T_O-B_O)_+,
    \qquad
    \|x\|_1\ge\frac1{DR}\sum_O(T_O-B_O)_+
    \]

    are correct with the stated meanings of \(D\) and \(R\).  Bijective row
    lineage preserves the number of tags per row, and the packet averaging
    has no missing factor.

3.  The half-orbit lemma and the relaxed capacity conclusion are correct
    under the displayed hypothesis

    \[
    s\le\min(2u,2v).
    \]

    The relaxation is not an integral exact factor, and the source correctly
    says so.

Three wording corrections are needed.

* The half-orbit conclusion is not proved for endpoint-heavy fixed splits
  with \(2u<s\) or \(2v<s\).  The Outcome and broad section title should
  retain the hypothesis above.
* Equation (3.10) gives \(1/3\), not the sharp value one, for one invariant
  three-owner packet.  Thus the invariant-target argument is detected as a
  singleton-orbit case, but its sharp packet lower bound is not literally a
  special case with the same constant.
* Lemma 4.1 makes the quota-independent surrogate summand
  \((3r_O-2|O|)_+\) vanish.  It does not make the actual quantity
  \((T_O-B_O)_+\) vanish for every balanced quota assignment.  The later
  relaxed quota/load construction is what shows that orbit totals alone
  admit a capacity-feasible assignment.

With those scope corrections, the report is proof-grade.

## 1. Exact owner-map conversion

Let \(c=|F\cap G|\).  A common wreath owns the same \(n\) middle windows in
both factors.  Exact factorhood makes the window families of distinct common
wreaths disjoint, so at least \(nc\) middle owners are unchanged.

Conversely, if one middle set has the same owner in both factors, that owner
is one wreath belonging to \(F\cap G\).  Hence every unchanged middle set is
one of the \(n\) windows of a common wreath.  The unchanged-owner count is
therefore exactly \(nc\), not merely at least that value.  Since
\(W=n|F|=nt\),

\[
d_{\rm own}(F,G)=W-nc=n(t-c)=n,d_{\rm row}(F,G).
\]

This uses wreath identity in the unoriented convention adopted by the
source.  If orientation or a deletion direction were separately decorated,
the resulting decorated distance could be larger; that is outside the
definition being audited.

Summing the identity along a path and applying the triangle inequality for
half symmetric difference gives source equation (1.5) exactly.

## 2. Canonical packet robustness and constants

The \(\operatorname{Cat}_{m-4}\) canonical triples are row-disjoint.  If an
endpoint factor deletes \(d\) canonical rows, at most \(d\) triples cease to
be intact.  Every intact triple still consists of three owners of its old
target.  At depth one the balanced quota is one or two, so it contains an
actual packet of size two or three.  Inserted rows cannot invalidate an
existing packet.

The surviving packets are vertex-disjoint.  Summing their fractional-cover
constraints gives

\[
\vartheta(H,\beta)
\ge \operatorname{Cat}_{m-4}-d_{\rm row}(H,F_m^{\rm MSW}),
\]

which is source equation (2.7).

The Catalan ratio also passes.  Direct cancellation gives

\[
\frac{\operatorname{Cat}_{m-4}}{\operatorname{Cat}_m}
=
\frac{(m-2)(m-1)m(m+1)}
 {16(2m-7)(2m-5)(2m-3)(2m-1)}
=\frac1{256}+O(m^{-1}).
\]

An FSP endpoint has packet value \(o(t/\sqrt m)=o(t)\), so its row distance
from the canonical factor is \((1/256-o(1))t\).  Multiplication by \(n\)
using the exact owner-map identity gives \((1/256-o(1))W\).  This proves an
owner-recourse lower bound, not a literal connector-length lower bound; the
source states this distinction correctly.

## 3. Row lineage and the integral orbit bound

For one transposition \(\tau=(x\ y)\) and one wreath \(E\), the total
incidence of \(x,y\) among the \(n\) middle windows of \(E\) is \(2m=n-1\).
If every window contained exactly one of them, that total would be \(n\).
Thus some window is fixed by \(\tau\), placing the colored rows \(E\) and
\(\tau E\) in the same ownership component.  A component choice selects
exactly one of this pair.  Composition gives a bijection from source rows to
endpoint rows, with each descendant equal to \(g_EE\) for one
\(g_E\in\Gamma\).

Consequently a source row carrying at most \(D\) distinct tags has an
endpoint descendant carrying at most \(D\) distinct image tags.  Different
tags on one row remain different because \(g_E\) is a permutation, and
different rows remain different because lineage is bijective.

At a target \(S\), let \(h_S\) be the number of tagged endpoint owners.  A
quota-safe deletion removes at least \((h_S-\beta(S))_+\) of them.  On
summing over targets, a deleted row is counted at most \(D\) times.  Hence

\[
D|B|\ge\sum_S(h_S-\beta(S))_+.
\]

Inside one target orbit \(O\),

\[
\sum_{S\in O}(h_S-\beta(S))_+
\ge\left(T_O-B_O\right)_+.
\]

Summing over orbits proves (3.6) with no omitted overlap term.

## 4. Fractional packet averaging

Put \(k_S=\beta(S)+1\).  When \(h_S\ge k_S\), every \(k_S\)-subset of the
tagged owners is a genuine survival packet.  Summing all its cover
constraints and dividing by
\(\binom{h_S-1}{k_S-1}\) yields

\[
\sum_{E\text{ tagged at }S}x_E
\ge\frac{h_S}{k_S}.
\]

Since \(k_S\le R\) and \((h_S-\beta(S))_+\le h_S\),

\[
\frac{h_S}{k_S}
\ge\frac{(h_S-\beta(S))_+}{R}.
\]

If \(h_S<k_S\), the positive part is zero.  A row weight appears in at most
\(D\) tagged target sums, so summing gives

\[
D\|x\|_1
\ge\frac1R\sum_S(h_S-\beta(S))_+.
\]

The orbit positive-part inequality then proves (3.7).  The factor \(R\) is
therefore valid.

It is intentionally coarse.  For a singleton orbit containing exactly one
three-owner target with quota two, direct packet averaging gives
\(\sum x_E\ge1\), whereas (3.7) gives only \(1/3\).  Thus source sentence
“the old invariant-target bound is the special case” should be read as a
structural, not constant-preserving, specialization.  Calling (3.10)
“sharp” is not justified by the proof.

## 5. Half-orbit calculation

Assume \(s\le\min(2u,2v)\).  Then the first \(s\) positions lie inside
\(U\), and the reflected last \(s\) positions lie inside
\(V^*=\operatorname{rev}(\overline V)\).  If there are \(p\) unequal pairs
of type \((1,0)\) and \(q\) of type \((0,1)\), the orbit size is
\(2^{p+q}\).

For an exchanged word to remain in the fixed-split universe, its first
\(2u\)-bit block must still contain exactly \(u\) ones.  Therefore it must
exchange equally many pairs of the two unequal types.  The number of
exchange subsets satisfying this necessary condition is

\[
\sum_j\binom pj\binom qj
=\binom{p+q}p.
\]

Dyck nonnegativity can only reduce the count.  If \(d=p+q>0\),
\(\binom dp\le2^{d-1}\).  Thus the fixed-split seed universe occupies at
most half of every nontrivial orbit, exactly as claimed in Lemma 4.1.

The positional hypothesis is essential to this proof.  If \(2u<s\) or
\(2v<s\), the exchanged positions meet the fixed seed block, so the
first-block balance argument above does not apply.  The broad Outcome and
Section 4 heading should not be read as covering those endpoint-heavy
splits.

## 6. What the capacity conclusion does and does not say

For a selected row-disjoint triple family in one admissible fixed split,
let \(r_O\) be the number of its seed targets in a nontrivial orbit \(O\).
The half-orbit lemma gives

\[
r_O\le |O|/2,
\qquad
3r_O\le\frac32|O|<2|O|.
\]

Therefore the quota-independent lower-bound term used in (3.10),

\[
(3r_O-2|O|)_+,
\]

is zero.  This is valid.  It must not be replaced by the stronger assertion
\((T_O-B_O)_+=0\) for every balanced quota vector, because an actual orbit
may contain quota-one labels.

The separate relaxed-capacity paragraph repairs exactly that distinction.
A row-disjoint triple family has at most \(t\) tagged rows and hence at most
\(t\) image labels.  The number of available depth-one upper quotas is

\[
\rho_1=\frac{2W}{m+2}
=\frac{2n}{m+2}t>t.
\]

Within an orbit, independent rowwise group choices can place \(3r_O\) tags
in bins of capacity two because \(3r_O\le2|O|\).  One may then put quota two
on every touched bin and use surplus upper quotas elsewhere.  This proves
capacity feasibility in the orbit-total relaxation.

It does not prove that one exact factor realizes those independent rowwise
group choices.  They may violate common component signs, row distinctness,
or exact middle ownership.  The source states all three limitations, so its
final conclusion is correctly limited to failure of an orbit-total-only
obstruction.

## 7. Final scope ledger

### Passed

1. Exact factor \(n\) between row and owner-map distance.
2. Canonical packet robustness under arbitrary endpoint replacement.
3. The \(1/256\) Catalan ratio and the resulting \(W\)-scale owner distance.
4. Bijective row lineage for arbitrary finite component-switch paths.
5. Integral orbit-excess deletion bound with factor \(1/D\).
6. Fractional orbit-excess packet bound with factor \(1/(DR)\).
7. The fixed-split half-orbit lemma under its stated positional hypothesis.
8. The quota-count calculation \(\rho_1>t\) and the relaxed capacity
   assignment.

### Corrections / qualifications

1. Add \(s\le\min(2u,2v)\) wherever the half-orbit statement is summarized.
2. Replace “special case” by “coarse singleton-orbit consequence,” or note
   explicitly that (3.10) loses a factor three on one invariant triple.
3. Replace “sharp next static quantity” by “valid quota-independent static
   certificate.”
4. Say that the surrogate summand in (3.10), rather than every actual orbit
   excess, vanishes on nontrivial half-occupied orbits.

After these corrections, the report rigorously establishes a genuine
\(W\)-scale owner-travel obstruction and a correctly scoped moving-label
orbit-capacity theorem.
