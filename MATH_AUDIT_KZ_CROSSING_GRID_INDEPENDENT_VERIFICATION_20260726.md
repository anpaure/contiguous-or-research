# Independent audit: KZ crossing grids and the missing star normalization

Date: 2026-07-26

Scope: independent verification of Sections 4--6 of
`MATH_AUDIT_KZ_SPREAD_APPROXIMATION_PHYSICAL_PORT_HIGH_COVER_20260726.md`
against the journal-version source of Kupavskii--Zakharov,
*Spread approximations for forbidden intersections problems*
([arXiv:2203.13379](https://arxiv.org/abs/2203.13379)).

## 0. Verdict

The deterministic crossing-grid theorem and its consequence for ordinary
conditional spreadness are correct.  In particular, for
\(s\to\infty\), \(s=o(m^{1/4})\), \(s\le H\), every exact
target-regular port system contains a middle target \(S\) and an
\((s+1)\times(s+1)\) target grid \(\mathcal G\) with

\[
 d^\#(\mathcal G)\ge {cD_0\over s(m)_s^2}.                       \tag{0.1}
\]

After conditioning on \(S\), this forces

\[
 \log r\le {2\log m+o(\log m)\over s}.                            \tag{0.2}
\]

Thus \(s=m^{1/5}\) gives \(r=1+o(1)\) using only
\(m^{2/5+o(1)}=o(q_*)\) further targets.  This genuinely contradicts
the ordinary \((r_0,q)\)-spread hypothesis in Kupavskii--Zakharov
Theorem 11 for every (q\ge1).

There is, however, an additional normalization issue not isolated in the
source audit.  If the whole catalogue is used as ambient family, then
even a new flag-aware notion with effective spread
\(r_\partial\asymp m\) leaves a KZ approximation remainder measured
against \(M\), whereas the desired theorem is measured against one star
degree \(D_1\), and \(M/D_1=\exp(\Theta(m))\).

This is not fatal: after fixing \(E\in\mathcal F\), an intersecting
family lies in the localized ambient catalogue
\[
 \mathcal A_E=\{C:e_C^\#\cap e_E^\#\ne\varnothing\},
\]
and \(|\mathcal A_E|\le k_{\rm port}D_1\).  Thus the weakest useful
replacement is flag-compressed and must work uniformly on every
\(\mathcal A_E\).  Star-normalization on the full catalogue is an
equivalent stronger alternative.

## 1. Audit of the deterministic grid count

For a strip \(C=(K,z)\) and a base phase \(t\), put

\[
 T_{i,j}^{(t)}=K\cup I_z(t+i,h-i+j),\qquad 0\le i,j\le s.          \tag{1.1}
\]

Since \(s<h\), every active interval in (1.1) is nonempty and proper.
It is therefore determined by its start and length.  Base phases spaced
by \(s+1\) have disjoint start ranges, so the

\[
 g=\left\lfloor {2h\over s+1}\right\rfloor\ge c h/s              \tag{1.2}
\]

chosen grids in a fixed strip have pairwise disjoint target sets.  This
justifies the key assertion that one omitted strip--target incidence can
destroy at most one chosen strip--grid pair.

At signed depth \(q\), exact target regularity omits exactly the fraction
\(1-\theta_q\), where \(\theta_q=N_q/N_1\).  Hence the total number of
omitted incidences at the two signs through depth \(s\) is

\[
 4hM\sum_{q=2}^s(1-\theta_q)
 \le C hM\sum_{q=2}^s{q^2\over m}
 \le {C hM s^3\over m}.                                           \tag{1.3}
\]

Relative to the \(Mg\) chosen pairs, the destroyed fraction is

\[
 O\left({s^4\over m}\right)=o(1).                                \tag{1.4}
\]

A coordinate grid is specified by a middle set \(S\), an ordered
\(s\)-tuple of distinct elements of \(S\), and an ordered \(s\)-tuple
outside \(S\).  Thus there are at most

\[
 W(m)_s^2                                                          \tag{1.5}
\]

such grids.  Pigeonholing the surviving pairs and using
\(2hM=WD_0\) gives

\[
 { (1-o(1))Mg\over W(m)_s^2}
 \ge {cD_0\over s(m)_s^2},                                       \tag{1.6}
\]

which is (0.1).  No independence or probabilistic port property is used
here; only the exact degree ledger is used.

## 2. Conditional normalization

Kupavskii--Zakharov use ordinary unweighted set families, not
multifamilies.  Consequently one must justify that, after conditioning on
the middle target \(S\), the denominator really is \(D_0\).

This is valid, but should be stated.  Every selected port edge retains
all \(2h\) middle targets of its strip.  Those middle targets determine
the physical strip: their total intersection is the core \(K\), and the
Johnson-adjacency graph on the remaining \(h\)-windows is the unique
\(2h\)-cycle, recovering the active cyclic order up to the rotation and
reversal already factored out.  Hence distinct strips through \(S\)
remain distinct after deleting \(S\), and

\[
 |\mathcal A(S)|=D_0.                                             \tag{2.1}
\]

Equivalently, one may add a private label vertex to each strip; this
does not change intersections between distinct edges and changes the
maximum edge size by only one.

Take \(X=\mathcal G\setminus\{S\}\), so

\[
 |X|=(s+1)^2-1=s^2+2s.                                           \tag{2.2}
\]

If \(\mathcal A(S)\) were \(r\)-spread, then (0.1) and (2.1) would give

\[
 {c\over s(m)_s^2}
 \le {d^\#(\mathcal G)\over D_0}
 \le r^{-(s^2+2s)}.                                               \tag{2.3}
\]

Since

\[
 \log (m)_s=s\log m+O(s^2/m),                                    \tag{2.4}
\]

(2.3) is exactly (0.2).  With \(s=m^{1/5}\),

\[
 {s^2\over q_*}
 =m^{-1/10+o(1)}(\log m)L_m=o(1),                                \tag{2.5}
\]

so the failure occurs below the advertised high-cover scale.

## 3. Comparison with the exact KZ hypotheses

The journal source defines \(\mathcal A\) to be \((r_0,q)\)-spread if
\(\mathcal A(B)\) is ordinarily \(r_0\)-spread for every
\(|B|\le q\).  Its Theorem 11 assumes

\[
 r_0\ge2\tau q,
 \qquad
 r_0>2^{12}\tau\log_2(2k),                                      \tag{3.1}
\]

where \(\tau\) is the relative-homogeneity parameter (not the target
cover number) and \(k\) is an upper bound on ambient edge size.  Here

\[
 k=k_{\rm port}=\Theta(h\sqrt m)=m^{1+o(1)},                      \tag{3.2}
\]

so (3.1) requires \(r_0=\Omega(\log m)\).  Since \(q\ge1\) tests the
one-target conditioning \(B=\{S\}\), (0.2) disproves the hypothesis by
an unbounded factor.

KZ Theorem 12 assumes, for ordinary intersection (t=1), that the
ambient family is \((r,1)\)-spread and

\[
 \varepsilon r\ge2^{17}q\log_2q.                                \tag{3.3}
\]

Again, \((r,1)\)-spread includes every one-target conditioned family,
so the same grid refutes the ambient hypothesis.  The numerical
calculation in the source audit is correct: if a hypothetical replacement
gave \(r_\partial\asymp m\), then with

\[
 q_*= {\sqrt m\over(\log m)L_m}m^{o(1)},\qquad
 \varepsilon={1\over\sqrt m\sqrt{L_m}},                          \tag{3.4}
\]

(3.3) would hold with room.

## 4. Full-ambient normalization and the localization repair

Condition (3.3) controls only the union of a nontrivial approximating
core family.  The preceding KZ approximation lemma leaves a remainder

\[
 |\mathcal F'|\le\tau^{-q-1}|\mathcal A|
 =\tau^{-q-1}M.                                                    \tag{4.1}
\]

For the physical catalogue,

\[
 {M\over D_1}={N_1\over2h}
 =\exp\big((2\log2+o(1))m\big).                                  \tag{4.2}
\]

Even granting boundary spread \(r_\partial\asymp m\), Theorem 11 also
forces \(2\tau q\le r_\partial\).  At \(q=q_*\), this gives

\[
 q_*\log\tau=O(\sqrt m\,m^{o(1)})=o(m).                          \tag{4.3}
\]

Consequently

\[
 {\tau^{-q_*-1}M\over D_1}
 =\exp(\Theta(m)),                                                 \tag{4.4}
\]

not (o(m^{-1/2})).  More generally, under (2\tau q\le m), the
quantity (q\log\tau\) is at most (m/(2e)), still below the
((2\log2)m+o(m)) exponent in (4.2).  Thus a literal boundary analogue
of KZ Theorems 11--12, with the same ambient-normalized remainder, does
not close the physical high-cover gate.

For the natural boundary rank this comparison cannot be repaired by a
large hidden constant in \(r_\partial\): the same grid has boundary rank
\(2s\), so its density \(m^{-2s+o(s)}\) itself forces
\(r_\partial\le(1+o(1))m\).

This calculation applies to the **full** ambient catalogue.  There is a
standard localization that repairs it.  Fix any \(E\in\mathcal F\) and
put
\[
 \mathcal A_E=\{C:e_C^\#\cap e_E^\#\ne\varnothing\}.              \tag{4.5}
\]
Since \(\mathcal F\) is intersecting, \(\mathcal F\subseteq\mathcal
A_E\).  A union bound over the targets of \(e_E^\#\) gives
\[
 |\mathcal A_E|
 \le |e_E^\#|D_1
 \le k_{\rm port}D_1.                                             \tag{4.6}
\]
Consequently a localized approximation remainder with \(\tau=2\) and
\(q=q_*\) would satisfy
\[
 2^{-q_*-1}|\mathcal A_E|
 \le 2^{-q_*-1}k_{\rm port}D_1
 =o(D_1/\sqrt m).                                                  \tag{4.7}
\]

Thus the normalization issue is a warning against applying KZ directly
to the full catalogue, not a second no-go.  A flag-compressed KZ theorem
valid uniformly for every localized ambient family \(\mathcal A_E\)
would have the correct normalization automatically.

Concretely, the weakest sufficient replacement would reproduce the KZ
conclusions inside every \(\mathcal A_E\): for \(\tau=2\), it would
decompose
\[
 \mathcal F\subseteq\mathcal A_E[\mathcal S]\cup\mathcal R,
 \qquad
 |\mathcal R|\le2^{-q-1}|\mathcal A_E|,                           \tag{4.8}
\]
with \(\mathcal S\) intersecting, and in the nontrivial-core case give
\[
 |\mathcal A_E[\mathcal S]|
 \le C{q\log q\over r_\partial}
       \max_T|\mathcal A_E[T]|.                                  \tag{4.9}
\]
At \(q=q_*\) and \(r_\partial\asymp m\), (4.6)--(4.9) give
\[
 |\mathcal F|=O(D_1/(\sqrt mL_m))
              +2^{-q_*}k_{\rm port}D_1
              =o(D_1/\sqrt m).                                  \tag{4.10}
\]
If \(\mathcal S\) is a single-star core \(T\), non-starness supplies a
witness \(C\in\mathcal R\) with \(T\notin e_C^\#\); the existing
off-edge-star estimate bounds the core part by
\(2\widehat\rho_mD_1=o(D_1/\sqrt m)\), and (4.7) bounds the remainder.

## 5. A sufficient replacement

For a co-occurring target collection (X), let
\(\beta_B(X)\) denote its endpoint-boundary rank after conditioning on
(B): the minimum number of independent ordered left/right endpoint
moves needed to generate (X) inside one realizing cyclic strip.  In
particular,

\[
 \beta_S(\mathcal G\setminus\{S\})=2s                            \tag{5.1}
\]

for the crossing grid, while an \(\ell\)-step nested flag has boundary
rank \(\ell\).  The grid density
(m^{-2s+o(s)}\) is therefore compatible with effective
boundary spread (r_\partial\asymp m), even though it destroys ordinary
cardinality spread.

The following stronger full-catalogue star-normalized statement would
also suffice.

> **Boundary-KZ/Hilton--Milner replacement.**  For the physical cyclic
> port hypergraph, let (r_\partial\asymp m).  Every intersecting strip
> family \(\mathcal F\) with target-cover number at least (q) admits a
> boundary-closed nontrivial core approximation satisfying
> \[
> |\mathcal F|
> \le e^{-cq}D_1
>   +C{q\log q\over r_\partial}D_1.                              \tag{5.2}
> \]
> Equivalently, both the approximation remainder and the nontrivial-core
> term are normalized by the star degree (D_1), not by (M), and
> crossing rectangles are charged by \(\beta\), not by their number of
> implied target vertices.

At (q=q_*\), (5.2) gives

\[
 |\mathcal F|
 =O\left({D_1\over\sqrt m\,L_m}\right)
  +e^{-cq_*}D_1
 =o(D_1/\sqrt m),                                                  \tag{5.3}
\]

which is exactly the missing physical high-cover estimate.

A proof modeled on KZ would need two genuinely new ingredients:

1. a robust two-colour containment lemma for measures spread in
   endpoint-boundary rank \(\beta\), rather than in target cardinality;
2. a boundary-core decomposition whose discarded mass is measured in
   units of (D_1).

The first addresses the crossing grid.  The second addresses the
exponential catalogue/star normalization (4.2).  Either ingredient alone
is insufficient.

## 6. Final audit status

Verified without correction:

* the deterministic surviving-grid count;
* the (D_0/[s(m)_s^2]\) lower bound;
* the conditional inequality \(\log r\le(2+o(1))\log m/s\);
* the comparison (s^2=o(q_*)\);
* the constants and quantifiers in KZ Theorems 11 and 12.

Necessary clarifications/corrections:

* justify that conditioning on a middle target leaves exactly (D_0)
  distinct residual edges (or add private labels);
* distinguish the KZ homogeneity parameter \(\tau\) from target-cover
  number;
* do not apply a flag analogue directly to the full catalogue without
  also repairing its normalization: either localize first to
  \(\mathcal A_E\), or prove a star-normalized remainder bound.
