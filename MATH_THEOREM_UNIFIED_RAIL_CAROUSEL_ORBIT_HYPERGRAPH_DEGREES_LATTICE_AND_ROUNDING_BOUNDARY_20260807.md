# Unified rail components form an exact carousel-orbit hypergraph, but maximal cycles have genuine lattice obstructions

**Date:** 2026-08-07  
**Input:** MATH_THEOREM_UNIFIED_RAIL_QUEUE_FULL_FRACTIONAL_SHADOW_BRAID_20260807.md  
**Method:** constant-core cyclic-window normal form, parameterized orbit
counting, and incidence-lattice projections  
**Status:** proof-safe exact degree/codegree theorem and exact obstruction.
The owner-copy hypergraph is extremely pseudorandom pairwise, and arbitrary
designated target/ticket rows admit exact orbit formulas.  Nevertheless a
single maximal rail type usually fails elementary part-size divisibility.
More strongly, at \(k=17\) *all* maximal rail types fail a coordinate
congruence, so no perfect owner factor made solely of maximal rail cycles
exists.  A lattice-breaking opened or nonmaximal component is necessary
before any perfect-matching theorem can apply.

## 1. Constant-core carousel normal form

Fix \(k,R,d\), choose

\[
0\le a\le d,
\qquad p=d-a+1,
\]

and positive integers

\[
h_0,\ldots,h_{p-1}\ge1,
\qquad H=\sum_i h_i\le R-a.
\]

Put

\[
c=R-d-1,
\qquad w=d+1.
\tag{1.1}
\]

For the maximal rail clock let

\[
L=1+\left\lfloor\frac{k-R+a}{p}\right\rfloor,
\qquad N=Lp,
\qquad r_0=(k-R+a)\bmod p.
\tag{1.2}
\]

The component uses

\[
U=c+N=k-r_0
\tag{1.3}
\]

coordinates.  Its permanent owner core is

\[
C=K\mathbin{\dot\cup}P_0\mathbin{\dot\cup}\cdots
\mathbin{\dot\cup}P_{p-1},
\qquad |C|=c,
\tag{1.4}
\]

because

\[
|K|=R-a-H,
\qquad \sum_i|P_i|=H-p,
\qquad |C|=R-a-p=R-d-1.
\]

Write the \(N\) toggle coordinates in source order as a directed cyclic
list

\[
X=(x_0,x_1,\ldots,x_{N-1}).
\]

If \(I_t^j\) denotes the cyclic \(j\)-interval ending at \(x_t\), then the
rank-\(R\) owners are exactly

\[
\boxed{O_t=C\cup I_t^w\qquad(t\in\mathbb Z_N).}
\tag{1.5}
\]

Thus every unified rail component, irrespective of \(a\) and the
composition \(h\), has the same owner geometry: a constant \(c\)-core and
all cyclic \(w\)-windows of a toggle cycle.

For \(j\ge p\), every proper source interval is likewise

\[
S_{t,j}=C\cup I_t^j,
\qquad |S_{t,j}|=c+j.
\tag{1.6}
\]

For \(j<p\), with \(t\equiv i\pmod p\), put

\[
B_{i,j}=K\cup P_i\cup P_{i-1}\cup\cdots\cup P_{i-j+1}.
\tag{1.7}
\]

Then

\[
S_{t,j}=B_{i,j}\cup I_t^j,
\qquad
|S_{t,j}|=R-a-H+\sum_{v=0}^{j-1}h_{i-v}.
\tag{1.8}
\]

All sets in (1.5), and all proper interval sets in (1.6)--(1.8), are
distinct in one component.  At \(j=N\), however, all endpoints give the
same full component universe.  Hence endpoint-distinct upper tickets run
only through rank \(U-1\); rank \(U\) contributes one universe target per
component, not \(N\).

## 2. The decorated component hypergraph

Fix one rooted, directed abstract component of the above type.  In
addition to its \(N\) owners, choose any occurrence-labelled set of
**designated** proper lower targets.  Let

\[
m_s=\#\{\text{designated distinct rank-}s\text{ targets in the component}\}.
\tag{2.1}
\]

Optional immediate-palette or upper tickets may be added in exactly the
same way; give each ticket rank/type its own vertex shore and multiplicity.
Physical but undesignated repeated occurrences are not vertices of this
capacity hypergraph.

Let

\[
\mathcal V_R={ [k]\choose R}
\]

be the owner shore, and let \(\mathcal V_s\) be a labelled copy of the
rank-\(s\) target shore for every designated rank.  Form a parameterized
multihypergraph \(\mathcal H_\theta\): for every injection of the \(U\)
abstract component coordinates into \([k]\), insert the hyperedge
containing the images of all \(N\) owners and all designated targets.
Parallel copies are retained.  They make the orbit counts exact and do
not affect existence of a matching.

The number of parameterized component copies is

\[
\boxed{M_\theta=(k)_U=\frac{k!}{(k-U)!}.}
\tag{2.2}
\]

One can quotient internal permutations and cyclic rootings instead; all
degrees and codegrees below are then divided by the same stabilizer
factor.  Their ratios and matching support are unchanged.

## 3. Exact orbit degrees and the universal pair formula

### Theorem 3.1 (exact degrees)

Every owner vertex has degree

\[
\boxed{
D_R=N\,R!\,(k-R)_{U-R}.}
\tag{3.1}
\]

Every designated rank-\(s\) target vertex has degree

\[
\boxed{
D_s=m_s\,s!\,(k-s)_{U-s}.}
\tag{3.2}
\]

The same formula holds for any optional ticket shore, with its per-component
multiplicity in place of \(m_s\).

#### Proof

For a fixed owner, choose which of the \(N\) abstract owners maps to it,
bijection its \(R\) labels to the prescribed owner, and inject the
remaining \(U-R\) labels outside it.  This gives (3.1).  The target proof
is identical. \(\square\)

For two vertex types of ranks \(r,s\), define the exact internal
intersection inventory

\[
\kappa_{r,s,q}
=\#\{(A,B): A,B\text{ are ordered distinct designated template }
\text{vertices of the indicated shores and }|A\cap B|=q\}.
\tag{3.3}
\]

### Theorem 3.2 (universal pair-codegree formula)

If named vertices \(X,Y\) have ranks \(r,s\) and
\(|X\cap Y|=q\), then

\[
\boxed{
D(X,Y)=\kappa_{r,s,q}\,
q!(r-q)!(s-q)!
(k-r-s+q)_{U-r-s+q}.}
\tag{3.4}
\]

If \(\kappa_{r,s,q}=0\), the codegree is zero.

#### Proof

Choose the ordered abstract pair counted by \(\kappa_{r,s,q}\).  Bijection
its intersection, first difference, and second difference to the
corresponding three regions of \(X,Y\).  Inject every remaining abstract
coordinate outside \(X\cup Y\).  These choices are independent and give
(3.4). \(\square\)

Equation (3.4) reduces every pair-codegree question, including phase-bank
targets (1.8), to a finite intersection inventory inside one component.

## 4. Closed owner ledger

Because \(N\ge2(d+2)=2w+2\), two distinct cyclic \(w\)-intervals have
either a short overlap or are disjoint.  For ordered owner pairs,

\[
\boxed{
\kappa_{R,R,R-\delta}=2N
\quad(1\le\delta\le w-1),}
\tag{4.1}
\]

and

\[
\boxed{
\kappa_{R,R,c}=N(N-2w+1).}
\tag{4.2}
\]

There are no other owner-pair intersection sizes.  Substitution into
(3.4), or direct cancellation against (3.1), gives

\[
\boxed{
\frac{D(X,Y)}{D_R}
=\frac{2}{{R\choose\delta}{k-R\choose\delta}}
\quad\text{if }|X\cap Y|=R-\delta,\ 1\le\delta<w,}
\tag{4.3}
\]

and

\[
\boxed{
\frac{D(X,Y)}{D_R}
=\frac{N-2w+1}{{R\choose w}{k-R\choose w}}
\quad\text{if }|X\cap Y|=c.}
\tag{4.4}
\]

For central \(R\), \(w=o(R)\), the maximum is the \(\delta=1\) value

\[
\boxed{
\frac{\Delta_2^{\rm owner}}{D_R}
=\frac{2}{R(k-R)}=\Theta(k^{-2}).}
\tag{4.5}
\]

Thus the owner-copy hypergraph is pairwise much sparser than the
projective-plane boundary \(1/N\); here \(N=\Theta(k)\) and the ratio is
\(\Theta(N^{-2})\).

## 5. Closed interval-ticket ledgers

For cyclic intervals of lengths \(\alpha,\beta\) with
\(\alpha+\beta\le N\), let

\[
n_N(\alpha,\beta;z)
=\#\{u\in\mathbb Z_N:|I_0^\alpha\cap I_u^\beta|=z\}.
\]

Writing \(b=\min(\alpha,\beta)\), the exact distribution is

\[
\boxed{
n_N(\alpha,\beta;z)=
\begin{cases}
N-\alpha-\beta+1,&z=0,\\
2,&1\le z<b,\\
|\alpha-\beta|+1,&z=b,\\
0,&\text{otherwise}.
\end{cases}}
\tag{5.1}
\]

Indeed the \(\alpha+\beta-1\) relative starts with positive overlap form
two unit-slope ramps and a plateau of length
\(|\alpha-\beta|+1\); every other start has zero overlap.

For a designated constant-core length-\(\ell\) ticket
\(S=C\cup I_t^\ell\), let \(m_\ell\) be the number of its designated
endpoints.  Its owner--ticket inventory is

\[
\boxed{
\kappa_{R,c+\ell,c+z}
=m_\ell\,n_N(w,\ell;z).}
\tag{5.2}
\]

For a short phase-bank ticket (1.8), put \(b_{i,j}=|B_{i,j}|\).  If
\(\mathcal M_s\) is the set of marked phase/depth pairs of rank \(s\), then

\[
\boxed{
\kappa_{R,s,q}
=L\sum_{(i,j)\in\mathcal M_s}
n_N(w,j;q-b_{i,j}).}
\tag{5.3}
\]

Equations (3.4), (5.2), and (5.3) are exact owner--lower codegrees.  Two
target shores have the following closed finite formula.  For all depths
put

\[
Q_{i,j}=
\begin{cases}
\{i-j+1,\ldots,i\}\pmod p,&j<p,\\
\mathbb Z_p,&j\ge p,
\end{cases}
\qquad
\widehat B_{i,j}=K\cup\bigcup_{v\in Q_{i,j}}P_v,
\tag{5.4}
\]

and define the phase-restricted interval correlation

\[
n_{N,p}^{\,r}(\alpha,\beta;z)
=\#\left\{v\in\mathbb Z_N:
v\equiv r\pmod p,\ 
|I_0^\alpha\cap I_v^\beta|=z\right\}.
\tag{5.5}
\]

If \(\mathcal M_s,\mathcal M_t\) are the marked phase/depth pairs on two
ticket shores, then their exact ordered internal inventory is

\[
\boxed{
\kappa_{s,t,q}
=L\!\!\sum_{\substack{(i,j)\in\mathcal M_s\\(i',\ell)\in\mathcal M_t}}
n_{N,p}^{\,i'-i}
\left(j,\ell;\
q-|\widehat B_{i,j}\cap\widehat B_{i',\ell}|\right),}
\tag{5.6}
\]

with the \(m_s\) identical-occurrence diagonal terms removed when the two
shores and their designation are the same.  Formula (5.6), followed by
(3.4), computes every
lower--lower, q1, and proper-upper pair-codegree.  For long upper intervals
one may evaluate (5.5) by passing to cyclic complements; no approximation
is required.

In particular, immediate containment incidences have relative codegree
at most \(O(d/k)=o(1)\), while generic intersections are much smaller.
The orbit is therefore a credible *approximate*-matching host once the
different shores have been degree-balanced.

## 6. Part-size and lattice constraints

Let

\[
W={k\choose R}
\]

and let \(Q_s\) be the number of named rank-\(s\) targets that the
carousel bank is required to cover exactly once.  A perfect matching in
one fixed-type decorated hypergraph would use some number \(b\) of
components.  Necessarily

\[
\boxed{
bN=W,
\qquad bm_s=Q_s\quad\text{for every designated shore}.}
\tag{6.1}
\]

Equivalently,

\[
\boxed{
N\mid W,
\qquad \frac{m_s}{N}=\frac{Q_s}{W}.}
\tag{6.2}
\]

Since \(m_s\) is integral—and for a phase-invariant marking is a multiple
of \(L\)—a single maximal component type almost never has the exact
optimal Ferrers proportions.  The fractional rail theorem avoids (6.2)
by mixing component types and fractional marks; that does not establish
an integral factor.

For a family \(\Theta\) of allowed component types, with \(x_\theta\)
selected copies, the exact global size lattice is

\[
\boxed{
\sum_{\theta\in\Theta}N_\theta x_\theta=W,
\qquad
\sum_{\theta\in\Theta}m_{\theta,s}x_\theta=Q_s.}
\tag{6.3}
\]

Thus the demand vector must lie in the integer lattice generated by the
component size vectors

\[
v_\theta=(N_\theta,(m_{\theta,s})_s).
\tag{6.4}
\]

The convex-hull theorem proves only real-cone membership.

There is a stronger coordinatewise owner congruence.  In one component a
ground coordinate lies in:

* all \(N_\theta\) owners if it is a core coordinate;
* exactly \(w=d+1\) owners if it is a toggle coordinate; or
* zero owners if it is unused.

If selected maximal components partition all rank-\(R\) owners, then for
every ground coordinate \(x\),

\[
\sum_{\theta}
\bigl(N_\theta c_{x,\theta}+w t_{x,\theta}\bigr)
={k-1\choose R-1},
\tag{6.5}
\]

where \(c_{x,\theta},t_{x,\theta}\) count selected copies in which \(x\)
has the two roles.  Therefore

\[
\boxed{
\gcd\bigl(w,(N_\theta)_{\theta\in\Theta}\bigr)
\ \Bigm|\ {k-1\choose R-1}.}
\tag{6.6}
\]

This is a genuine incidence-lattice condition, not a scalar restatement
of (6.3).

An exact named Ferrers boundary also breaks the full symmetric orbit.  To
retain the regular hypergraph above, its boundary cells must be included
as additional block types in the same configuration design.  Deleting an
arbitrary named boundary set first leaves an irregular residual host, to
which the orbit degrees (3.1)--(3.2) no longer apply verbatim.

## 7. Decisive \(k=17\) obstruction

For \(k=17\),

\[
R=9,
\qquad d=3,
\qquad w=4,
\qquad c=5.
\]

For every \(a=0,1,2,3\), the maximal clock has

\[
\boxed{N=12,\qquad U=17.}
\tag{7.1}
\]

But

\[
W={17\choose9}=24310\not\equiv0\pmod{12},
\tag{7.2}
\]

so even the owner part-size equation fails.

More invariantly, every coordinate belongs to

\[
{16\choose8}=12870\equiv2\pmod4
\tag{7.3}
\]

rank-\(9\) owners.  Every maximal rail component contributes either \(12\),
\(4\), or \(0\) owner incidences at that coordinate, all divisible by
\(4\).  Equation (6.5) is impossible.

Hence

\[
\boxed{
\text{No union of maximal unified-rail cycles—allowing every }a,h
\text{ and every embedding—can partition the }k=17\text{ owners}.}
\tag{7.4}
\]

This obstruction is already present before lower targets, upper tickets,
cycle fusion, or the compiler are imposed.  It does not obstruct opened,
truncated, or lattice-breaking components.

## 8. Does a known perfect-matching theorem finish the rounding?

### 8.1 Approximate owner matching is plausible

The owner hypergraph is regular, has an exact fractional perfect matching,
and has relative pair-codegree \(\Theta(k^{-2})\).  This is excellent nibble
geometry.  A quantitative growing-uniformity nibble specialized to
\(N=\Theta(k)=\Theta(\log W)\) should plausibly give an owner matching
covering \(1-o(1)\) of the owner shore.

The classical Pippenger--Spencer theorem is not, by itself, a proof here:
its standard formulation fixes the uniformity before taking the limit,
whereas \(N\to\infty\).  More importantly, an almost-perfect matching
would still leave exponentially many owners and does not solve exact
target correlation.

### 8.2 Exact design theorems are conceptually relevant but not directly applicable

Keevash's lattice/design framework, including *The existence of designs
II*, is conceptually the closest match because it allows labelled faces,
extra colours/orders, and lattice-valued subset sums.  Kuperberg--Lovett--
Peled likewise treats exact regular structures through a lattice local
central limit theorem.  Iterative absorption is the natural mechanism for
turning a nibble into an exact factor.

None is an off-the-shelf conclusion for the present system:

1. the block size and number of ticket coordinates grow with \(k\);
2. the optimal construction mixes several component types;
3. the exact Ferrers boundary and common-cap rows are occurrence-labelled;
4. robust local lattice generation/extendability has not been proved; and
5. the raw maximal family actually violates (6.2) and (6.6) in some
   dimensions, including \(k=17\).

No theorem can round through a failed divisibility condition.

### 8.3 Proof-safe next target

The appropriate next theorem is a **lattice-breaking carousel absorber**:
adjoin a bounded catalogue of opened or nonmaximal rail components whose
size/incidence vectors

* generate the demand lattice in (6.3);
* break the coordinate congruence (6.6);
* admit bounded signed trades localized to any owner/target residue; and
* preserve the literal residence, upper-ticket, and common-cap interface.

After those rows are established, a Keevash-style design theorem or a
custom nibble-plus-absorption proof becomes genuinely plausible.  Before
them, the exact perfect-matching proposal is false for the maximal
carousel family.

## 9. Verdict

The unified rail theorem has produced an unusually clean integral host:

\[
\boxed{
\text{constant core}+\text{one cyclic toggle order}
\Longrightarrow
\text{exact regular orbit and }\Delta_2/D=\Theta(k^{-2}).}
\]

That closes the degree/codegree audit and strongly supports approximate
packing.  It does **not** close exact rounding.  The first obstruction is
now explicit and arithmetic: maximal cycles alone do not generate the
required incidence lattice.  At \(k=17\) they cannot even partition the
owner layer.

The fractional Shadow--Braid theorem therefore remains valuable, but its
correct integral continuation is

\[
\boxed{
\text{maximal-carousel nibble}
+\text{lattice-breaking opened components}
+\text{literal absorber},}
\]

not a direct perfect matching of maximal carousel edges.

This note does not prove an integral component factor,
\(\nu(k)\le B(k)+O(1)\), or exact equality.

## References for the theorem boundary

* N. Pippenger and J. Spencer, *Asymptotic Behavior of the Chromatic
  Index for Hypergraphs* (1989).
* P. Keevash, *The existence of designs*, arXiv:1401.3665.
* P. Keevash, *The existence of designs II*.
* G. Kuperberg, S. Lovett, and R. Peled, *Probabilistic existence of
  regular combinatorial structures*, arXiv:1302.4295.
* S. Glock, D. Kühn, A. Lo, and D. Osthus, *The existence of designs via
  iterative absorption: hypergraph F-designs for arbitrary F*,
  arXiv:1611.06827.
