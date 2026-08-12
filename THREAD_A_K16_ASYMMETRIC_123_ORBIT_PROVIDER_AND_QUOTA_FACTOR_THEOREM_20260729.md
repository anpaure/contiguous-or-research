# K16 asymmetric 123-hole carrier: nine-orbit provider hypergraph and quota-first factor theorem

Date: 2026-07-29

Status: exact theorem, obstruction, and first nontrivial repair packet.  The
audited asymmetric factor is an unconditional positive-resident, double-q1
carrier with precisely 123 remaining fixed-shadow holes.  Those holes are
nine cyclic rows.  However, every old edge is unique on at least one q1
shore, so the earlier ``protected cut'' specialization was vacuous: every
nonempty repair has signed q1 debt.  This note derives the corrected signed
provider system, proves that the smallest B-rail owner/exact-upper-q1 trade
is an alternating Boolean-incidence \(C_6\), and records the audited orbit of
fifteen such trades which repairs one upper-q3 orbit.  Eight original rows
remain, and the packet creates one new fixed-q4 orbit, so this is not yet a
compiler-ready factor.

The mathematical statements below are proved from the displayed ledgers.
Finite census statements are explicitly labelled and tied to their audit
artifacts; no new search is performed in this note.

## 1. The frozen carrier and its nine deficit orbits

Write

\[
 \Omega=[15]\mathbin{\dot\cup}\{z\},
\]

and let \(\rho\) rotate the first fifteen coordinates while fixing \(z\).
The factor

\[
 F_*=A\mathbin{\dot\cup}(z+\overline B)
 \subset J(16,8)
\tag{1.1}
\]

is the audited object in

\[
 \text{scratch/k16\_asymmetric\_two\_rail\_factor\_20260729.json}.
\]

It has 12,870 distinct owners, 28 cyclic components, positive residence
four, and complete lower and upper q1 palettes.  Its only fixed-window
holes are the following \(\rho\)-orbits.

\[
\begin{array}{c|c|c|c}
\text{shore/depth}&\text{representative masks}&\text{orbit sizes}
 &\text{physical total}\\ \hline
\text{lower q2}&33337,\ 33609,\ 34069&15,15,15&45\\
\text{upper q3}&36343,\ 36599,\ 39791,\ 39911,\ 40623,\ 46811
 &15,15,15,15,15,3&78
\end{array}
\tag{1.2}
\]

Thus there are exactly nine quotient deficit rows.

Every mask in (1.2) contains \(z\).  This also follows structurally.  For
old rank-eight states \(P_i\subset[15]\), put

\[
 \widehat P_i=\{z\}\cup\overline{P_i}.
\]

Then for every interval,

\[
 \bigcap_i\widehat P_i
   =\{z\}\cup\overline{\bigcup_iP_i},
\qquad
 \bigcup_i\widehat P_i
   =\{z\}\cup\overline{\bigcap_iP_i}.
\tag{1.3}
\]

Consequently the three lower-q2 deficit orbits are complements of three
old upper-q2 orbits, while the six upper-q3 deficit orbits are complements
of six old lower-q3 orbits.  An intersection containing \(z\) forces every
owner in its window to contain \(z\), so lower-q2 repair is intrinsically
confined to the \(z\)-rail even if cross edges are allowed.  An upper union
containing \(z\) can use a mixed path, but in the no-cross architecture of
this note all six upper rows are likewise supplied on the complemented
rail.

The 78 arbitrary-width upper holes are the same rank-eleven masks as the
fixed upper-q3 holes.  The audit found no cyclic contiguous vertex-interval
provider of any allowed length for them.  A new fixed four-state witness is
nevertheless one allowed interval and therefore repairs both ledgers
simultaneously.  The converse need not hold: an arbitrary-width repair could
use a longer interval.

The q1 loads split exactly by rail as follows.  An entry
\((n_1,n_2,n_3)\) means \(n_i\) colours have load \(i\).

\[
\begin{array}{c|c|c}
 &\text{lower q1}&\text{upper q1}\\ \hline
A\text{ (no }z\text{)}&6435,0,0&3675,1230,100\\
B\text{ (contains }z\text{)}&3660,1260,85&6435,0,0
\end{array}
\tag{1.4}
\]

Equivalently, among all 12,870 old factor edges, the pair
\((\text{lower load},\text{upper load})\) has histogram

\[
 (1,1)^{7335}(1,2)^{2460}(1,3)^{300}
 (2,1)^{2520}(3,1)^{255}.
\tag{1.5}
\]

### Proposition 1.1 (no nonempty protected cut)

Every old factor edge is the unique provider of at least one of its two q1
colours.  Hence deleting any nonempty set of old edges leaves at least one q1
colour with no wholly retained provider.  In particular, a nonempty cut set
cannot be protected in the sense of leaving one retained witness of every
old q1 colour.

#### Proof

Every pair in (1.5) has at least one coordinate equal to one.  For an edge
with lower load one, deleting that edge deletes the only old witness of its
lower colour; the same statement holds on the upper shore.  Additional
deletions cannot restore a retained witness.  \(\square\)

Thus new seams must restore q1 resources in the same compound move which
creates deep witnesses.  A model which first protects all old q1 witnesses
and then adds providers has no nontrivial feasible point.

## 2. Separated cuts and the exact positive collar

Orient every component of the complemented rail.  Cut a family \(H\) of
directed factor edges.  Assume every retained path has at least three
transitions, equivalently at least four vertices.  Thus no two replacement
seams can occur in one three-transition window.

At a terminal port use the last three retained vertices

\[
 L_{-2},L_{-1},L_0,
\]

and at an initial port use the first three

\[
 R_0,R_1,R_2.
\]

For a coordinate \(x\) present at a port, let
\(\tau_x^L,\tau_x^R\in\{1,2,3,4\}\) be the inward terminal positive-run
length, capped at four.

### Lemma 2.1 (positive-residence seam test)

A Johnson seam \(e=L_0R_0\) is positive-residence compatible exactly when,
for every coordinate \(x\),

\[
\begin{array}{c|c}
(1_{x\in L_0},1_{x\in R_0})&\text{condition}\\ \hline
(1,1)&\tau_x^L+\tau_x^R\ge4\\
(1,0)&\tau_x^L\ge4\\
(0,1)&\tau_x^R\ge4\\
(0,0)&\text{none}.
\end{array}
\tag{2.1}
\]

If every seam passes (2.1), the rethreaded rail has positive residence
four.

#### Proof

A positive run crossing one seam is respectively the concatenation of the
two terminal fragments, the left fragment, or the right fragment in the
first three cases of (2.1).  If a run crosses at least two seams, it
must remain present at every vertex of each intervening retained path.
Hence it contains all vertices of one such path, and that path has at least
four vertices.  Internal runs are unchanged.  These observations prove
necessity and sufficiency.
\(\square\)

No zero-run condition is imposed here; this is the exact residence notion
needed by the asymmetric carrier.

## 3. The literal seam-provider signature

For an allowed seam \(e=L_0R_0\), define its two q1 colours by

\[
 \lambda_1(e)=L_0\cap R_0,\qquad
 \upsilon_1(e)=L_0\cup R_0.
\tag{3.1}
\]

Its two possible new lower-q2 windows are

\[
 \Lambda_2(e)=
 \left\{
 L_{-1}\cap L_0\cap R_0,\
 L_0\cap R_0\cap R_1
 \right\},
\tag{3.2}
\]

retaining an occurrence only when its rank is six.  Its three possible new
upper-q3 windows are

\[
\begin{aligned}
 \Upsilon_3(e)=\{&
 L_{-2}\cup L_{-1}\cup L_0\cup R_0,\\
 &L_{-1}\cup L_0\cup R_0\cup R_1,\\
 &L_0\cup R_0\cup R_1\cup R_2\},
\end{aligned}
\tag{3.3}
\]

retaining an occurrence only when its rank is eleven.  Multiplicity is
retained if two displayed windows coincide.

For later all-depth auditing, (3.2)--(3.3) have the following uniform form.
If collars are exposed through depth \(Q\), then at depth \(q\le Q\) the
exact \(q\) crossing windows are, for \(1\le a\le q\),

\[
 \Lambda_{q,a}(e)=
 \bigcap_{i=0}^{a-1}L_{-i}
 \cap\bigcap_{j=0}^{q-a}R_j,
 \qquad
 \Upsilon_{q,a}(e)=
 \bigcup_{i=0}^{a-1}L_{-i}
 \cup\bigcup_{j=0}^{q-a}R_j.
\tag{3.4}
\]

Only intersections of rank \(8-q\) and unions of rank \(8+q\) are retained.
Thus one seam has \(q\), not \(2q\), literal crossing slots at depth \(q\).
If every retained path between seams has at least \(Q\) transitions, every
window through depth \(Q\) crosses at most one seam, and the ledger below is
valid simultaneously for all \(q\le Q\).

For every target \(T\) on either q1 shore, the lower-q2 shore, or the
upper-q3 shore, let \(b_H(T)\) be the number of old occurrences lying
wholly in the retained paths.  For a seam \(e\), let \(a_T(e)\) be its
multiplicity in (3.1), (3.2), or (3.3), as appropriate.

### Theorem 3.1 (exact additive shadow ledger)

For every perfect matching \(M\) of the exposed terminal and initial ports
using allowed seams,

\[
 \operatorname{load}_{(F_*-H)\cup M}(T)
   =b_H(T)+\sum_{e\in M}a_T(e)
\tag{3.5}
\]

at q1, lower q2, and upper q3.  With \(Q\)-collars and the stated
separation, the same identity holds at every depth \(q\le Q\), with
\(a_T(e)\) defined by (3.4).

#### Proof

Every new window which is not wholly retained crosses a seam.  Since every
retained path has at least three transitions, a q1, q2, or q3 window
crosses exactly one seam.  The windows crossing that seam are precisely
(3.1)--(3.3), or (3.4) at general depth.  All other occurrences are counted
by \(b_H(T)\).
\(\square\)

Thus an allowed seam is a provider hyperedge using two port resources and
carrying at most

\[
 1+1+2+3=7
\]

quota incidences.  Including its two ports, the literal provider
hypergraph has rank at most nine.  This rank-nine statement is only for the
truncated q1/lower-q2/upper-q3 model.  Through depth \(Q\), the full signed
signature has the correspondingly growing collection of crossing slots from
(3.4).

There is also an architecture-free description of the two deep provider
types.

### Proposition 3.2 (intrinsic provider paths)

For a rank-six target \(L\), a lower-q2 provider is exactly a selected
two-edge path \(X_0X_1X_2\) such that

\[
 X_i=L\cup A_i,\qquad
 A_i\in\binom{\Omega\setminus L}{2},\qquad
 A_iA_{i+1}\in E(J(10,2)),\qquad
 A_0\cap A_1\cap A_2=\varnothing.
\tag{3.6}
\]

For a rank-eleven target \(U\), an upper-q3 provider is exactly a selected
three-edge path \(X_0X_1X_2X_3\) such that

\[
 X_i=U\setminus D_i,\qquad
 D_i\in\binom U3,\qquad
 D_iD_{i+1}\in E(J(11,3)),\qquad
 \bigcap_{i=0}^3D_i=\varnothing.
\tag{3.7}
\]

#### Proof

The first identities merely separate the fixed intersection \(L\) from
the two moving coordinates; Johnson adjacency and empty total intersection
are then exactly the edge and target conditions.  The second statement is
the complementary missing-triple formulation inside \(U\).
\(\square\)

For targets containing \(z\), equations (1.3) transport (3.6)--(3.7) to
the corresponding union/intersection provider paths in the old
rank-eight source.  These formulas show that the provider hypergraph is
literal, not a marginal shadow approximation.

### Corollary 3.3 (the lower bow-tie and cross-only obstruction)

Let \(L=z\cup S\) be one of the missing lower-q2 targets.  Every provider
\(X_0X_1X_2\) lies wholly on the \(B\)-rail.  Writing its center as

\[
 X_1=z\cup S\cup\{p,q\},
\]

there are \(a,b\notin S\cup\{p,q\}\) such that, after possibly reversing
the path,

\[
 X_0=z\cup S\cup\{q,a\},\qquad
 X_2=z\cup S\cup\{p,b\}.
\tag{3.8}
\]

If the two upper-q1 colours of these edges are to be distinct, then
\(a\ne b\).  In particular, a rethread which adds only cross-rail edges and
leaves every \(B\!-\!B\) adjacency unchanged cannot repair any of the 45
lower holes.

#### Proof

Since \(z\in L=X_0\cap X_1\cap X_2\), all three owners contain \(z\).
Apply (3.6) after removing \(z\).  The two consecutive \(J(10,2)\) moves
give exactly (3.8).  Their upper colours are

\[
 z\cup S\cup\{p,q,a\},\qquad
 z\cup S\cup\{p,q,b\},
\]

and are equal exactly when \(a=b\).  A pure cross splice creates no new
three-owner \(B\!-\!B\!-\!B\) subpath, so it creates no provider of \(L\).
\(\square\)

## 4. Exact endpoint matching formulation

Let \(\Gamma_H\) be the bipartite graph whose left vertices are terminal
ports and whose right vertices are initial ports.  Its edges are precisely
the Johnson seams passing (2.1).  Define the demand family

\[
 \mathcal D_H=\{T:b_H(T)=0\}
\tag{4.1}
\]

over the two q1 shores and the two deep shores under consideration.

### Theorem 4.1 (provider-matching equivalence)

Within the separated, direction-coherent cut architecture, a repair of
\(F_*\) preserving positive residence and both q1 palettes and filling all
lower-q2 and upper-q3 targets exists if and only if \(\Gamma_H\) has a
perfect matching \(M\) satisfying

\[
 b_H(T)+\sum_{e\in M}a_T(e)\ge1
 \qquad(T\in\mathcal D_H).
\tag{4.2}
\]

#### Proof

A perfect matching restores one incoming and one outgoing transition at
every exposed endpoint, hence degree two at every owner.  Lemma 2.1 gives
positive residence and Theorem 3.1 turns every required palette/shadow
condition into (4.2).  Conversely, every direction-coherent rethread is
exactly such a port perfect matching, and its literal loads obey (3.5).
\(\square\)

This is an exact quota-constrained one-factor, not an ordinary matching:
the quota rows destroy bipartite total unimodularity in general.

There is a useful signed form which makes Proposition 1.1 explicit.  Let
\(m_T^0\) be the load of \(T\) before cutting.  Under the separation
hypothesis, every destroyed window contains a unique cut transition.  Let
\(d_T(i)\) be the number of such windows charged to source cut \(i\), and
for a seam \(i\to j\) put

\[
 \sigma_T(i,j)=a_T(i,j)-d_T(i).
\tag{4.3}
\]

Because a port perfect matching uses every source cut once,

\[
 m_T^{\rm new}
   =m_T^0+\sum_{(i,j)\in M}\sigma_T(i,j).
\tag{4.4}
\]

This is the correct ledger for simultaneous cut selection and repair.  The
nine rows (1.2) have \(m_T^0=0\).  Previously covered q1 and deep rows have
positive baselines but may receive negative \(\sigma\)-mass.  They cannot be
discarded.

### Corollary 4.2 (unavoidable packet size)

If \(c\) old edges are cut and replaced, at most \(2c\) new lower-q2
windows and at most \(3c\) new upper-q3 windows are created.  Therefore any
fixed-window repair of all 45 and 78 original holes has

\[
 c\ge
 \max\{\lceil45/2\rceil,\lceil78/3\rceil\}=26.
\tag{4.5}
\]

This lower bound applies before residence, q1 restoration, port
disjointness, or higher-depth collateral is imposed.

## 5. Cyclic quotient compression

The undirected edge set of \(F_*\) is \(\rho\)-invariant.  Its displayed
cycle orientations are not quite invariant, but an equivariant reorientation
exists; the invariant one-seam census uses that orientation.  Assume from
now on that \(H\), its orientation, and the selected seam family are
\(\rho\)-invariant.

For any target orbit \(\mathcal O_j\) and seam orbit \(\omega\), define the
signed orbit coefficient

\[
 \Sigma_{j\omega}
  ={1\over|\mathcal O_j|}
    \sum_{e\in\omega}\sum_{T\in\mathcal O_j}\sigma_T(e).
\tag{5.1}
\]

Equivariance makes the signed change equal on every member of
\(\mathcal O_j\), so \(\Sigma_{j\omega}\) is an integer.  It may be negative.
If \(x_\omega\in\{0,1\}\) selects the whole seam orbit, every physical row
in \(\mathcal O_j\) is equivalent to the single exact row

\[
 m_j^0+\sum_\omega\Sigma_{j\omega}x_\omega\ge1.
\tag{5.2}
\]

For the original holes, (5.2) gives precisely nine mandatory rows.  All
emergent q1 and collateral deep orbits give additional signed rows.  Thus
the symmetry compression is exact, but it does not mean that nine unsigned
cover inequalities suffice.

The endpoint equations remain exact orbit-incidence equations: the
coefficient of a seam orbit at a port orbit is the number of its physical
seams incident with one fixed representative port.  This convention
handles short orbits and quotient loops.  Without an invariant repair one
must keep all 123 physical hole rows; summing an orbit would certify only
average coverage.

The equivariantly reoriented, four-separated seam catalogue gives the
following number of \(B\!-\!B\) provider literals per physical target:

\[
\begin{array}{c|c|c}
\text{row representative}&|\mathcal O|&
 \text{\(B\!-\!B\) providers per target}\\ \hline
33337&15&62\\
33609&15&53\\
34069&15&23\\
36343&15&67\\
36599&15&46\\
39791&15&44\\
39911&15&64\\
40623&15&46\\
46811&3&45
\end{array}
\tag{5.3}
\]

So reachability is not the obstruction.  In the audit's one-source-edge
signed-charge test, each member of the exceptional orbit \(46811\) has 60
provider literals across all rail types and none is individually q1-safe.
Thus even this weaker local test forces coordinated compensation on that
row.

The counts in (1.5) and (5.3) are certified by
[the equivariant provider audit](/Users/amir.nuriyev/Documents/problem/scratch/k16_asymmetric_123_provider_hypergraph_equivariant_20260729.audit.json),
SHA-256
\(e38fa34818385bc809b68e3a17b1ee76f3639e786f984d3bdd143ed4ef483bd4\).

## 6. The exact B-rail trade space

Write a \(B\)-owner as \(z\cup Q\), where
\(Q\in\binom{[15]}7\).  A \(B\)-edge has upper-q1 colour \(z\cup M\),
where \(M\in\binom{[15]}8\), and its two endpoints are two distinct
7-facets of \(M\).  Let \(I_{7,8}\) be the Boolean incidence graph between
these two ranks.

### Theorem 6.1 (incidence two-factor and alternating-circuit normal form)

A \(B\)-rail graph is degree two at every owner and uses every upper-q1
colour exactly once if and only if, after replacing each coloured factor
edge \(Q Q'\) of colour \(M=Q\cup Q'\) by the two incidences
\(Q M,M Q'\), the selected incidences form a spanning 2-factor of
\(I_{7,8}\).

Consequently, the symmetric difference of any two such \(B\)-rail graphs
decomposes into alternating even circuits of \(I_{7,8}\), and flipping any
alternating circuit preserves owner degree and the exact upper-q1 palette.
The incidence graph has no 4-cycle.  Its smallest circuit is a 6-cycle, so
every nontrivial exact-upper-q1 trade changes at least three factor edges.

#### Proof

At an owner \(Q\), incidence degree is exactly factor degree.  At a colour
\(M\), incidence degree is twice the number of selected factor edges of
that colour.  This proves both directions of the first assertion: two
selected, distinct facets of \(M\) determine one Johnson edge, and the
union \(M\) is unique.

The symmetric difference of two 2-factors is even at every vertex and
therefore decomposes into alternating circuits.  Conversely an alternating
flip preserves degree two.  A 4-cycle would give two distinct 7-sets
contained in two distinct common 8-supersets.  Distinct 7-sets which have a
common 8-superset have union of size eight, and that union is their unique
common 8-superset.  Hence no 4-cycle exists.  Bipartiteness excludes odd
cycles, so the minimum is six.  \(\square\)

Every 6-cycle has the explicit form

\[
\begin{gathered}
 S+a,\quad S+b,\quad S+c,\\
 S+a+b,\quad S+b+c,\quad S+c+a,
\end{gathered}
\tag{6.1}
\]

where \(|S|=6\) and \(a,b,c\) are distinct.  In one orientation the three
selected incidences

\[
 (S+a)(S+a+b),\quad
 (S+b)(S+b+c),\quad
 (S+c)(S+c+a)
\tag{6.2}
\]

are replaced by the other three.  Each colour vertex retains its second,
off-circuit endpoint.  On the factor this is exactly a directed three-edge
endpoint rotation.  Lower q1, positive residence, and all deeper shadows
are the side quotas; exact upper q1 and owner degree are automatic.

For completeness, three rank-seven vertices on a 6-cycle are pairwise
adjacent in \(J(15,7)\).  If they were all facets of one rank-eight set,
their three intervening rank-eight vertices would coincide, contrary to a
simple 6-cycle.  Hence they form the other Johnson-triangle type: they share
one rank-six core \(S\) and have distinct extra points \(a,b,c\).  Their
pairwise unions are exactly the three sets in (6.1), proving that the
displayed form exhausts all incidence 6-cycles.

This proves algebraically that no \(B\)-only two-edge move in the exact
\(B\)-upper palette fibre can be the sought repair.  The broader reciprocal
2-switch census additionally finds no q1- and deep-safe gain, but that
finite statement is stronger than the incidence-girth argument.

## 7. Quota first, then colour-resolved Hall

The incidence normal form gives a compact exact trade space.  The following
port theorem gives the corresponding quota-first completion criterion.
Fix a maximum depth \(Q_0\), expose collars through that depth, and fix a set
\(H\) of \(c\) directed \(B\)-edges whose retained paths have at least
\(Q_0\) transitions.  Because the old \(B\)-upper q1 palette is exact,
their deleted colours form a set \(\mathcal C_H\) of \(c\) distinct colours.
Let
\(\mathcal E_H\) be every non-\(B\)-upper target which has zero retained
load: lower q1 and all required fixed depths through \(Q_0\).  Completeness
at every fixed upper depth implies arbitrary-upper completeness, so no
nonlocal arbitrary-interval row is inserted into this additive seam ledger.

A partial matching \(Q\) of the port graph is a quota bank if

\[
 b_H(T)+\sum_{e\in Q}a_T(e)\ge1
 \quad(T\in\mathcal E_H),
\tag{7.1}
\]

and its seam upper colours are distinct members of \(\mathcal C_H\).
Delete its used terminals, initials, and colours.  For a bijection
\(\phi\) from residual terminals to residual colours, let \(G_\phi\) join a
terminal \(\ell\) to an initial \(r\) exactly when \(\ell r\) is an allowed
seam and

\[
 \upsilon_1(\ell r)=\phi(\ell).
\tag{7.2}
\]

### Theorem 7.1 (exact quota-bank/colour-Hall equivalence)

A \(B\)-only rethread on \(H\) preserves positive residence, every required
non-upper row, and the exact \(B\)-upper q1 palette if and only if there
exist a quota bank \(Q\) and a bijection \(\phi\) as above such that

\[
 |N_{G_\phi}(S)|\ge |S|
 \quad\text{for every set \(S\) of residual terminals}.
\tag{7.3}
\]

#### Proof

Given \(Q,\phi\), Hall gives a residual perfect matching.  Together with
\(Q\) it uses every port once.  It uses every deleted colour exactly once,
so it restores the exact \(B\)-upper palette; (7.1) restores all other
deficits.  Every edge was restricted by the collar test, hence positive
residence holds.

Conversely, let \(M\) be a valid rethread.  Its \(c\) seams must cover the
\(c\) deleted, pairwise distinct \(B\)-upper colours.  Therefore their
colours are exactly \(\mathcal C_H\), each once.  Choose an
inclusion-minimal subset \(Q\subseteq M\) covering \(\mathcal E_H\).
For every residual terminal, let \(\phi\) be the colour of its edge in
\(M\setminus Q\).  This is a bijection, and \(M\setminus Q\) witnesses every
Hall inequality in (7.3).  \(\square\)

Theorem 7.1 is the promised checkable sufficient condition: quota atoms are
selected first, and only an ordinary bipartite Hall test remains after a
colour assignment.  It is also necessary within the fixed separated
\(B\)-only architecture.  The hard integral choice is the compatible
triple \((Q,\phi,H)\), not rankwise marginal balance.  The theorem does not
bound the absorber: its converse may choose \(Q=M\).  A useful sparse
absorber theorem must additionally prove a quantitative bound on \(|Q|\).

## 8. The first audited orbit packet

The short-rethread census and independent materialization give the
following finite certificate.

### Proposition 8.1 (the \(39911\) triangle-orbit packet)

There is a full \(\rho\)-orbit of fifteen directed three-edge rotations,
all in old \(B\)-component 2, with 45 distinct cut transitions and minimum
mutual cyclic gap seven, such that simultaneous application:

1. preserves Johnson adjacency, every owner degree, both q1 palettes, and
   positive residence four;
2. creates no new lower-q2 or upper-q3 hole;
3. fills exactly the size-15 upper-q3 orbit represented by \(39911\), so
   the upper-q3 and arbitrary-rank-11 hole counts fall from \(78\) to \(63\);
4. leaves all 45 lower-q2 holes;
5. creates one size-15 fixed upper-q4 hole orbit, while creating no
   arbitrary-rank-12 hole.

#### Certificate and audit

The materialized factor is
[k16_asymmetric_triangle_orbit_repair_20260729.json](/Users/amir.nuriyev/Documents/problem/scratch/k16_asymmetric_triangle_orbit_repair_20260729.json),
SHA-256
\(6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc\).
Its literal physical audit is
[k16_asymmetric_triangle_orbit_repair_20260729.audit.json](/Users/amir.nuriyev/Documents/problem/scratch/k16_asymmetric_triangle_orbit_repair_20260729.audit.json).
Its SHA-256 is
\(3519ff2a8e08d48a7e58513a3b631f82b2d7229f2cfef3ab1ecd102ab2ef9f73\).
The fifteen transition triples are embedded in the factor artifact.  The
audit reports zero bad Johnson edges, minimum positive run four, zero q1
holes (the first nonzero fixed rows are q2), the stated q2/q3/q4 hole
lists, and the stated arbitrary-upper lists.  Comparing the old and new
q3 lists removes exactly \(\mathcal O(39911)\).

For the representative transition triple \((6448,9321,7508)\), the old
directed edges are

\[
64264\to62217,\qquad
64384\to64257,\qquad
62344\to62337,
\]

and the new edges are

\[
64264\to64257,\qquad
64384\to62337,\qquad
62344\to62217.
\]

The old and new upper-colour lists are both
\((64265,64385,62345)\), in the displayed order.  Thus exactly one endpoint
incidence changes at each of three colour vertices, and Theorem 6.1
identifies the symmetric difference as one incidence \(C_6\).  The other
fourteen triples are its \(\rho\)-rotates.  Hence the packet consists of the
smallest possible exact-upper-q1 local atoms, not accidental three-seam
constructions.

The post-packet census
[k16_asymmetric_short_rethread_cycles_round1_20260729.audit.json](/Users/amir.nuriyev/Documents/problem/scratch/k16_asymmetric_short_rethread_cycles_round1_20260729.audit.json)
finds no positive, q1- and q2/q3-safe gain among directed cycles of lengths
two, three, or four.  This is a scoped finite no-go, not a structural
impossibility for longer or interacting circuits.

## 9. Exact remaining lemma

After Proposition 8.1 the original quota vector has eight nonzero orbit
rows:

\[
 3\ \text{lower-q2 rows},\qquad
 5\ \text{upper-q3 rows},
\tag{9.1}
\]

representing \(45+63=108\) physical holes.  There is also the new
size-15 fixed upper-q4 row.  The next exact gate is:

> **Signed all-depth orbit-circuit completion.**  Starting from the
> triangle-orbit factor, find a \(\rho\)-invariant compatible family of
> alternating circuits in \(I_{7,8}\), or a more general colour-resolved
> port rethread, such that the signed inequalities (4.4)/(5.2) hold for
> every q1 and fixed-shadow target at every depth, all arbitrary-upper
> targets remain covered, and every new seam passes (2.1).

Within the enumerated class of one separated cyclic port permutation whose
seams are individually in the positive-compatible catalogue and whose net
q1/q2/q3 ledger is nonnegative, any next gain requires directed length at
least five.  This finite no-go says nothing about higher-shadow safety.  A
multi-packet construction may instead allow one packet's signed q1 or
higher-depth debt to be cancelled by another.  Theorem 7.1 is an exact
finite certificate for such a completion once \(H,Q,\phi\) are proposed.

No theorem here claims the 123 holes were solved.  What is now proved is
sharper: the mandatory deficits are nine cyclic rows; isolated protected
absorption is impossible; owner- and exact-upper-q1-preserving
\(B\)-trades start at incidence \(C_6\); and one full orbit of those minimal trades gives a
literal, positive-resident descent \(9\to8\) on the original row count,
with its exact q4 collateral exposed.
