# Audit of isolated-pruning fractional overload and the edge-coloring gate

Date: 2026-07-25

Pure mathematics only.

## 0. Verdict

The abstract theorem in
`ISOLATED_PRUNING_FRACTIONAL_OVERLOAD_THEOREM_20260725.md` is correct.
Its sharper Section 2.1 is also correct after one bookkeeping repair:
when tag and target fibres are put into the same application of the
weighted pruning lemma, a tag must have weight \(Qg\), not merely \(g\).
Equivalently, one may normalize the tag and target exceptional fractions
as two separate random ledgers.  With that repair, for

\[
 \delta=m^{-2/3},\qquad L=Qm^{2/3}\log m,
\tag{0.1}
\]

there are only \(o(T/Q)\) exceptional tags and \(o(W)\) exceptional
targets, and the uniform good-fibre point satisfies

\[
 \ell(v)\le 1+3\delta
\tag{0.2}
\]

at every nonexceptional target.

Choose a rational number

\[
 \rho\le(1+3\delta)^{-1},\qquad
 1-\rho=O(\delta)+o(1/Q).
\tag{0.3}
\]

Then \(\widehat x_P=\rho/|\mathcal I_U|\) is a genuine fractional
matching on the good targets, and its total tag deficit, including
exceptional tags, is \(o(T/Q)\).  Clearing denominators produces a
multihypergraph with reference capacity \(D\) such that

\[
 d(U)=\rho D,\qquad d(v)\le D,\qquad |e|\le K+1,
\tag{0.4}
\]

where \(K\le(2Q+1)g\).  This is the correct rational integral form of
the new fractional point.

The proposed full-coloring conclusion, even in the weaker form

\[
 \chi'(\mathcal H)=(1+o(1))D,
\tag{0.5}
\]

does **not** follow from (0.4) and the protected width-two exponential
intersection census.  There is an exact abstract counterexample with all
of the following properties:

1. every tag has degree \(D\);
2. every target has degree at most \(D\);
3. every pair of edges on different tags intersects in at most one target,
   so every nonlinear width-two intersection excess is identically zero;
4. the tag-uniform fractional point has zero overload; but
5. \(\chi'(\mathcal H)\ge(1-o(1))KD\).

The counterexample is a padded projective-plane line system.  It proves
that the width-two moment census controls repeated intersections, but not
the global arrangement of singleton intersections.  A projective-plane
clique is invisible to every moment in which the linear term has been
subtracted.

For the full-coloring-by-averaging route, coefficient one requires the
sharper fractional edge-coloring, or weighted matching, inequality

\[
 \boxed{
 \sum_e m_e y_e
 \le(1+o(1/Q))D
 \max_{M\text{ matching}}\sum_{e\in M}y_e
 \quad\text{for every }y_e\ge0.}
\tag{EC_Q}
\]

Here \(m_e\) is the scaled multiplicity of the underlying chunk.  Because
the rational scale may be enlarged once more, \((\mathrm{EC}_Q)\) is
necessary and sufficient for a \((1+o(1/Q))D\) edge coloring of a further
integral blow-up.  The \(o(1/Q)\), rather than merely \(o(1)\), is forced
by the protected-row ledger.

There is a strictly weaker one-color route.  It asks directly for a
matching meeting \(T-o(T/Q)\) tags and leaving only \(o(W)\) protected
claims for literal repair.  The padded projective-plane example does not
refute this weaker statement, because its private filler edges themselves
give a perfect tag matching.  It refutes the decomposition of the whole
fractional point into nearly \(D\) matchings.  This distinction is
essential.

Thus the corrected fractional-capacity gate is closed at exactly the
required \(o(T/Q)\) accuracy, but neither \((\mathrm{EC}_Q)\) nor the
economical near-transversal gate is closed.

## 1. Audit of the abstract overload theorem

Use the notation of the source theorem: \(T\) tags, \(A\) candidates per
tag, \(K\) targets per candidate, target catalogue degrees \(d_v\le A\),
bad-graph maximum degree \(\Delta\), and

\[
 p={1\over L(\Delta+1)},
 \qquad \mu=pA.
\tag{1.1}
\]

For a tag \(U\), let \(Y_U\) be its number of marked candidates and
\(Z_U\) the marked candidates removed by isolation.  Then

\[
 \mathbb EY_U=\mu,
 \qquad
 \mathbb EZ_U\le Ap^2\Delta\le\mu/L.
\tag{1.2}
\]

Consequently the source's Chernoff--Markov estimate

\[
 \Pr(A'_U<\mu/2)
 \le e^{-\mu/32}+4/L
\tag{1.3}
\]

is valid.  So is

\[
 \mathbb E|A'_U-\mu|
 \le\sqrt\mu+\mu/L.
\tag{1.4}
\]

For a target \(v\), the number of retained incidences is bounded by the
number \(Y_v\) of marked incidences, and

\[
 Y_v\sim\operatorname {Bin}(d_v,p),
 \qquad
 {pd_v\over\mu}={d_v\over A}\le1.
\tag{1.5}
\]

On a good tag, uniform fibre weights give

\[
 \ell(v)
 \le {Y_v\over\mu}
 +\sum_U n_{Uv}\left|{1\over A'_U}-{1\over\mu}\right|.
\tag{1.6}
\]

The second summand totals exactly

\[
 {K\over\mu}\sum_U|A'_U-\mu|
\tag{1.7}
\]

after summing over \(v\).  Since

\[
 \mathbb E(Y_v-pd_v)_+\le\sqrt{pd_v}\le\sqrt\mu,
\]

the overload expectation is

\[
 { |V|\over\sqrt\mu}
 +KT\left({1\over\sqrt\mu}+{1\over L}\right).
\tag{1.8}
\]

The final simultaneous-outcome argument is also valid: normalize the bad
tag count and overload by their respective expectation bounds, add them,
and choose an outcome where the sum is at most two.

No independence between the random variables in the two ledgers is used.

## 2. Audit of the sharp protected-geodesic substitution

The source now chooses

\[
 \delta=m^{-2/3},\qquad L=Qm^{2/3}\log m.
\tag{2.1}
\]

Since \((\Delta+1)/A=m^{-3+o(1)}\), the retained mean and the relative
Chernoff exponent are

\[
 \mu={A\over L(\Delta+1)}=m^{11/6-o(1)},
 \qquad
 \delta^2\mu=m^{1/2-o(1)}.
\tag{2.2}
\]

For target fibres the Chernoff exponent is actually
\(\delta^2pd_v\), so a lower as well as an upper calibration check is
needed.  It holds in the protected band.  On an uncapped row, writing
\(\lambda_q=R_q/T\ge1\),

\[
 {d_v\over A}
 ={T\lfloor\lambda_q\rfloor\over R_q}
 ={\lfloor\lambda_q\rfloor\over\lambda_q}\ge {1\over2}.
\tag{2.3}
\]

On a capped row \(c_q=g\), one has \(R_q\le W\) and
\(gT/W=1-o(1)\), so \(d_v/A=Tg/R_q\ge1-o(1)\).  The middle-owner ratio
is the same \(Tg/W=1-o(1)\).  Hence every controlled fibre has
\(pd_v=\Theta(\mu)\), and the exponent in (2.2) applies uniformly.

Corollary 1.2 of
`RECTANGLE_BAD_GRAPH_BALANCED_PRUNING_LEMMA_20260725.md` therefore gives
exceptional weighted proportion

\[
 \varepsilon_{\rm pr}
 \le 2e^{-m^{1/2-o(1)}}+{2\over L\delta}
 =O\!\left({1\over Q\log m}\right).
\tag{2.4}
\]

There is one necessary normalization detail.  The target-fibre ledger has
total weight \(O(QW)\), whereas the tag ledger with weight \(g\) has total
weight only \(gT=\Theta(W)\).  Thus a single combined application with
tag weight \(g\) would prove only an \(O(1/\log m)\) exceptional tag
fraction.  Give each tag weight \(Qg\), or equivalently add the two
exceptional fractions after normalizing them separately.  Then both
ledgers have scale \(O(QW)\), and (2.4) gives

\[
 |V_{\rm exc}|=O(W/\log m)=o(W),
 \qquad
 |\mathcal T\setminus\mathcal T'|
 =O(T/(Q\log m))=o(T/Q).
\tag{2.5}
\]

On every retained tag and nonexceptional target,

\[
 |A'_U-\mu|\le\delta\mu,
 \qquad
 |d'_v-pd_v|\le\delta pd_v.
\tag{2.6}
\]

The simultaneous cap on every raw marked target count is also valid.  A
binomial upper tail gives probability \(e^{-\Omega(\mu)}\) that a fixed
target has more than \(2\mu\) marked candidates, while there are only
\(e^{O(m)}\) targets and \(\mu=m^{11/6-o(1)}\).  Intersecting this event
with the weighted-pruning outcome costs asymptotically nothing.  Since
every retained good-tag denominator is at least \((1-\delta)\mu\), every
exceptional target then carries only \(O(1)\) fractional incidence.
Consequently the exceptional-target incidence ledger is also \(o(W)\).

Finally, calibration \(d_v/A\le1\) and (2.6) give, pointwise,

\[
 \ell(v)
 \le{(1+\delta)pd_v\over(1-\delta)pA}
 \le {1+\delta\over1-\delta}
 \le1+3\delta
\tag{2.7}
\]

for all sufficiently large \(m\).  This is stronger than the old
aggregate-overload conclusion and is the form needed below.

## 3. Exact rational scaling

The literal number \((1+3\delta)^{-1}\) need not be rational.  Choose
instead a rational \(\rho\) such that

\[
 0\le(1+3\delta)^{-1}-\rho<m^{-10}.
\tag{3.1}
\]

For \(P\in\mathcal I_U\), set

\[
 \widehat x_P={\rho\over A'_U}.
\tag{3.2}
\]

By (2.7), the total \(\widehat x\)-mass at every good target is at most
one.  Every retained tag has mass exactly \(\rho\), and

\[
 (T-|\mathcal T'|)+(1-\rho)|\mathcal T'|
 =o(T/Q)+O(\delta T)=o(T/Q),
\tag{3.3}
\]

because \(Q\delta=o(1)\).

Choose a common denominator \(D\) for all numbers
\(\rho/A'_U\), and replace each chunk \(P\) by

\[
 m_P={D\rho\over A'_U}
\tag{3.4}
\]

parallel copies.  A copy is an edge containing its tag and all of its
nonexceptional protected targets.  Then

\[
 d(U)=\rho D,
 \qquad
 d(v)=D\sum_{P\ni v}\widehat x_P\le D.
\tag{3.5}
\]

Both quantities are integers by the choice of \(D\).  Each edge remains
one legal geodesic chunk and has size at most \(K+1\).  Further common
blow-ups preserve every normalized load and intersection statistic.

## 4. What a near-\(D\) edge coloring would give

Suppose the scaled multihypergraph has a proper edge coloring with

\[
 C=(1+\varepsilon_m)D,
 \qquad \varepsilon_m=o(1/Q)
 \tag{4.1}
\]

colors.  A color class is a matching on tags and protected targets.  The
total number of edge copies is

\[
 \rho D|\mathcal T'|.
\]

Hence some color contains at least

\[
 {\rho D|\mathcal T'|\over C}
 =(1-o(1/Q))|\mathcal T'|
\tag{4.2}
\]

edges.  It therefore chooses one legal chunk on all but \(o(T/Q)\) tags and
has no duplicate nonexceptional protected target.  The exceptional
targets, discarded tags, integer floor holes, and resets together cost
\(o(W)\).

This verifies the proposed implication from edge coloring to coefficient
one.  The missing assertion is the edge coloring itself.

Here both losses matter:

\[
 1-\rho=O(\delta)=o(1/Q),
 \qquad C/D-1=o(1/Q).
\tag{4.3}
\]

The weaker estimate \(C=(1+o(1))D\) controls only the missing middle
owners.  If a color misses \(s\) tags, the literal protected-row repair
ledger is bounded only by

\[
 Ks\le(2Q+1)gs.
\tag{4.4}
\]

Since \(gT=\Theta(W)\), a uniform coefficient-safe conclusion from this
bound requires \(s=o(T/Q)\).  For \(s=\varepsilon_mT\), the uncontrolled
worst-case ledger is \(O(\varepsilon_mQW)\).  A weaker tag estimate
finishes only if one additionally proves that the holes are aligned so a
cross-rank chain/rotor reserve repairs them for \(o(W)\) cost.

## 5. Exact fractional edge-coloring dual

Let \(\mathfrak M\) be the set of matchings of the scaled hypergraph, and
keep one variable for each underlying edge type with multiplicity \(m_e\).
Its fractional chromatic index is

\[
 \chi_f'(\mathcal H,m)
 =\min\left\{
   \sum_{M\in\mathfrak M}\lambda_M:
   \sum_{M\ni e}\lambda_M\ge m_e,
   \ \lambda_M\ge0
 \right\}.
\tag{5.1}
\]

Linear-programming duality gives

\[
 \boxed{
 \chi_f'(\mathcal H,m)
 =\max_{y_e\ge0}
 {\sum_e m_ey_e
  \over
  \max_{M\in\mathfrak M}\sum_{e\in M}y_e}.}
\tag{5.2}
\]

Consequently \((\mathrm{EC}_Q)\) is exactly the assertion

\[
 \chi_f'(\mathcal H,m)\le(1+o(1/Q))D.
\tag{5.3}
\]

This fractional condition is also sufficient after a further rational
blow-up.  Indeed, choose a rational optimal solution \((\lambda_M)\) of
(5.1) and clear its denominators by an integer \(b\).  Use
\(b\lambda_M\) copies of matching \(M\) as colors.  If an edge type is
covered more than \(bm_e\) times, delete it from surplus matching copies.
The result is a proper coloring of the \(b\)-fold multihypergraph with

\[
 b\chi_f'(\mathcal H,m)
\]

colors.  Conversely every integral coloring supplies a feasible solution
of (5.1).  Thus \((\mathrm{EC}_Q)\) is the exact full-coloring gate at the
accuracy needed for coefficient one when rational rescaling is allowed.

The scale \(o(1/Q)\) is sharp for this averaging argument.  If only
\(\chi_f'\le(1+\varepsilon_m)D\) is known, its average matching has size at
least \(\rho T'/(1+\varepsilon_m)\), and the resulting tag deficit is
\(O((\delta+\varepsilon_m)T)\).  Without a chain-aligned reserve this is
\(o(T/Q)\) precisely when \(Q(\delta+\varepsilon_m)=o(1)\).

The degree constraints (3.5) test only star-shaped instances of
the dual.  They do not bound (5.2) for a general weight vector \(y\).

## 6. Width two does not imply the coloring gate

We give an abstract counterexample which retains every advertised local
parameter.

Let \(q\) be a prime power and let \(\Pi\) be a projective plane of order
\(q\).  It has

\[
 n=q^2+q+1
\tag{6.1}
\]

points and the same number of lines; every line contains \(q+1\) points,
every point lies on \(q+1\) lines, and two lines meet in exactly one point.
Fix an integer \(a\ge1\) and put

\[
 D=a(q+1).
\tag{6.2}
\]

For every line \(L\), make one tag \(\tau_L\).  Above it put:

1. \(a\) line edges containing all \(q+1\) points of \(L\);
2. \(aq\) filler edges using only targets private to that edge.

Pad every filler edge by private targets to common size \(K=q+1\).  The tag
degree is

\[
 a+aq=D.
\tag{6.3}
\]

A projective point has degree

\[
 a(q+1)=D,
\tag{6.4}
\]

and every private target has degree one.  Giving every edge above a tag
weight \(1/D\) therefore gives target load at most one and zero fractional
overload.

For two distinct tags, two nonprivate edges meet in exactly one target;
all other pairs are disjoint.  Hence, for every \(w\ge1\),

\[
 w^{|e\cap f|}-1-(w-1)|e\cap f|=0.
\tag{6.5}
\]

Thus the complete cross-tag nonlinear intersection-excess hierarchy is
zero.  Every cross-tag intersection has Boolean width one, so a fortiori
width at most two.

Nevertheless all \(an\) line-edge copies are pairwise intersecting.  They
form a clique in the line graph, and therefore

\[
 \chi'(\mathcal H)\ge an.
\tag{6.6}
\]

Since

\[
 {an\over D}={q^2+q+1\over q+1}=q+{1\over q+1},
\tag{6.7}
\]

the chromatic index is a factor \(\Theta(q)=\Theta(K)\) larger than \(D\).
In the exact dual (5.2), take \(y_e=1\) on the line edges and zero on the
fillers.  Then

\[
 \sum_e m_ey_e=an,
 \qquad
 \max_{M\text{ matching}}\sum_{e\in M}y_e=1,
\tag{6.8}
\]

and hence the normalized weighted-cut ratio is

\[
 {\sum_e m_ey_e\over
  D\max_M\sum_{e\in M}y_e}
 ={n\over q+1}=q+{1\over q+1}.
\tag{6.9}
\]

This example proves:

\[
 \boxed{
 \text{degree balance + width-two nonlinear moments}
 \not\Longrightarrow \chi'=(1+o(1))D.}
\tag{6.10}
\]

It is an abstract logical obstruction, not a claim that a projective plane
is embedded in the geodesic catalogue.  A successful geodesic proof must
use a global property which rules out this singleton-intersection design.

The word *singleton* is exact here.  The protected nonlinear statistic

\[
 w^{|e\cap f|}-1-(w-1)|e\cap f|
\]

vanishes whenever \(|e\cap f|\le1\), so no estimate of that statistic,
at any value of \(w\), sees the clique in (6.8).  In particular, the
missing hypothesis cannot be another bound involving only the
\(j\ge2\) binomial intersection moments.  At minimum it must control the
linear singleton arrangement after arbitrary reweighting; the exact such
control is \((\mathrm{EC}_Q)\).

This obstruction is to edge decomposition, not to the existence of one
large tag matching.  The private filler edges are mutually disjoint, so
choosing one filler above each line gives a perfect tag matching.  Thus a
proof aimed only at one coefficient-one color may bypass
\((\mathrm{EC}_Q)\), but then it must prove directly

\[
 \max_{M\text{ matching}}|M|
 \ge T-o(T/Q)
\tag{TM_Q}
\]

together with the \(o(W)\) protected-hole ledger.  The projective-plane
test vector shows why a whole fractional edge coloring is too ambitious
from the presently available moments; it does not disprove
\((\mathrm{TM}_Q)\) for the geodesic catalogue.

## 7. What the protected census actually transfers

For two chunks on distinct tags put

\[
 r(P,E)=|C(P)\cap C(E)|
\]

after exceptional targets are omitted, and define the scaled weighted
excess, writing \(x=\widehat x\),

\[
 \mathcal K_w^x(P)
 =\sum_{E:\tau(E)\ne\tau(P)}x_E
 \left(w^{r(P,E)}-1-(w-1)r(P,E)\right).
\tag{7.1}
\]

This equals the normalized excess moment of the multihypergraph, because
\(m_E/D=x_E\).

The protected width-two census is initially uniform in the unpruned
catalogue.  It does not automatically give a uniform bound on (7.1) for
the particular isolated-pruning outcome selected only through tag loss
and overload.  One can add a time-zero average moment ledger to the
pruning experiment.  On a good tag, \(x_E\le2/\mu\).  Conditional on a
fixed path \(P\) being retained, a nonconflicting path \(E\) is marked
with probability \(p\).  Therefore

\[
 \mathbb E\mathcal K_w^x(P)
 \le {2p\over\mu}
 \sum_E
 \left(w^{r(P,E)}-1-(w-1)r(P,E)\right)
 \le 2m^{o(1)}
\tag{7.2}
\]

for \(1\le w\le C\log m\), using \(\mu=pA\).  Markov and a dyadic set of
\(w\)'s show that one may simultaneously arrange a bound
\(m^{o(1)}\) for all but an \(o(1)\) weighted fraction of retained edge
copies.

This is useful, but it has two exact limitations.

1. It says nothing about the linear singleton-intersection arrangement,
   as (6.5) demonstrates.
2. It is a time-zero average.  After a matching or palette nibble, the
   residual multiplicities are nonuniform and need not be dominated by
   the original uniform census.

## 8. The hereditary moment gate for a palette nibble

Although nonlinear moments cannot replace \((\mathrm{EC}_Q)\), they
remain the natural local input to a nibble once a global
matching-dispersal condition has ruled out projective-plane-type
obstructions.

At a residual stage \(t\), let \(m_t(E)\) be the uncolored multiplicity,
let \(D_t\) be the reference degree, and define

\[
 \Psi_{j,t}(P)
 ={1\over D_t}
  \sum_{E:\tau(E)\ne\tau(P)}
  m_t(E)\binom{r(P,E)}j.
\tag{8.1}
\]

The exact binomial identity gives

\[
 \mathcal K_t(P,w)
 :=\sum_{j\ge2}\Psi_{j,t}(P)(w-1)^j
 ={1\over D_t}
  \sum_E m_t(E)
  \left(w^{r(P,E)}-1-(w-1)r(P,E)\right).
\tag{8.2}
\]

In a palette bite, an edge is tentatively assigned a specified color with
probability on the scale \(1/(KD_t)\).  If \(I_P,I_E\) are two residual
survival indicators, their exact covariance multiplier is

\[
 {\mathbb E(I_PI_E)\over\mathbb EI_P\,\mathbb EI_E}
 =(1-p_t)^{-|\Gamma_t(P)\cap\Gamma_t(E)|}.
\tag{8.3}
\]

The deterministic conflict-neighbourhood bound is

\[
 |\Gamma_t(P)\cap\Gamma_t(E)|
 \le(1+o(1))r(P,E)D_t+K^2\Delta_{2,t},
\tag{8.4}
\]

where \(\Delta_{2,t}\) is the largest residual two-target codegree after
same-tag conflicts are handled by an injective tag palette.  Over
\(\Theta(K\log(1/\eta))\) bites down to density \(\eta\), (8.3)--(8.4)
produce weights \((c/z_t)^{r(P,E)}\).

Accordingly a safe hereditary local gate is

\[
 \boxed{
 K^2{\Delta_{2,t}\over D_t}\log(1/\eta)=o(1),}
\tag{8.5}
\]

\[
 \boxed{
 \sup_P\mathcal K_t(P,c/z_t)
 =o\!\left({1\over K\log(1/\eta)}\right)}
\tag{8.6}
\]

uniformly along the residual trajectory, together with the corresponding
one-round mean-degree and palette-balance estimates.  These are the direct
palette analogues of the audited conflict-neighbourhood conditions in
`MATH_ATTACK_TRP_PHASE_CODE_WEIGHTED_NIBBLE_20260725.md`.

Conditions (8.5)--(8.6) are sufficient local covariance bounds, not a
replacement for the exact global condition \((\mathrm{EC}_Q)\).  The
proved protected census supplies only the unweighted \(t=0\) analogue of
(8.2), with size \(m^{o(1)}\), and therefore does not establish (8.6).

This is the exact point where the claimed transfer from “protected
width-two census” to a near-\(D\) edge-coloring breaks.

## 9. Full coloring versus the coefficient-one partial coloring

Suppose a palette nibble with \((1+\varepsilon)D\) colors properly colors
all but an \(\eta\) fraction of the copies at every retained tag.  The
number of colored tag incidences is

\[
 (1-\eta)\rho D|\mathcal T'|.
\]

Hence some color meets at least

\[
 { (1-\eta)\rho\over1+\varepsilon}|\mathcal T'|
\tag{9.1}
\]

tags.  Without a chain-aligned reserve this is the required
owner-near-factor only if

\[
 \eta+\varepsilon+(1-\rho)=o(1/Q).
\tag{9.2}
\]

The new pruning point supplies \(1-\rho=O(\delta)=o(1/Q)\), but the
coloring still has to supply \(\eta+\varepsilon=o(1/Q)\).  Mere
\(\eta,\varepsilon=o(1)\) is insufficient.

Completing the edge coloring is substantially stronger.  If the residual
maximum degree is \(O(\eta D)\), greedy coloring of its line graph uses at
most

\[
 O(K\eta D)
\tag{9.3}
\]

new colors.  To make this \(o(D)\), one needs

\[
 K\eta=o(1).
\tag{9.4}
\]

The present exponential census reaches only

\[
 \eta=1/\log m,
\]

because it is proved for \(w\le C\log m\).  This is not even enough for
the coefficient-one averaging route: in the truncated regime
\(1/\log m\) is not \(o(1/Q)\), so (9.2) fails.  It is much farther from
full greedy completion, since \(K\asymp gQ\gg\log m\) and hence (9.4)
also fails.  The present time-zero census can support the claimed
coefficient only if a chain-aligned reserve absorbs the much larger
\(T/\log m\) tag deficit, or if a new hereditary argument continues the
nibble down to \(o(1/Q)\) density.

## 10. Exact remaining coefficient-one gates

There are now two clean formulations.

### Full edge-color route

Prove the weighted matching inequality \((\mathrm{EC}_Q)\) for the actual
scaled geodesic multihypergraph, together with an integral coloring or the
equivalent rational blow-up.  Local degrees and width-two moments do not
imply it.

### Economical one-color route

Without an additional reserve theorem, it is enough to prove that the
scaled hypergraph contains a matching meeting
\((1-o(1/Q))|\mathcal T'|\) tags and missing only \(o(W)\) protected
targets, or to construct a partial proper coloring whose average color has
those two properties.  For the palette nibble, the missing inputs are:

1. a global matching-dispersal condition excluding singleton-intersection
   designs such as Section 6; and
2. hereditary weighted versions of (8.5)--(8.6), or the exact palette
   transfer-energy bound replacing them, through residual density
   \(o(1/Q)\), unless a chain-aligned reserve absorbs the tail.

The isolated-pruning theorem closes the fractional overload dual and
supplies the rational demand vector.  It does not supply either of these
two integral properties.  That is the exact remaining discrepancy.
