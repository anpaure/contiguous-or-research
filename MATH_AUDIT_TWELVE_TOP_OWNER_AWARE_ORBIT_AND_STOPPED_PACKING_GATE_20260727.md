# Twelve-top recharge: owner-aware orbit, codegrees, and stopped packing gate

Date: 2026-07-27

Scope: the histogram-neutral twelve-top recharge and its use in a
coefficient-one, top-and-owner packing.

## 0. Verdict

Put

\[
 n=2m,\qquad M=m+H,\qquad s=m-H,\qquad
 d=m-3H+1,
\]

and assume

\[
 H\ge3,\qquad M\ge18H-10.
\tag{0.1}
\]

All orbit counts below are valid under (0.1).  Whenever a packing or
leave estimate is asserted, impose in addition the intended Gaussian
calibration

\[
 \rho:={dN\over W}={d\over\lambda}\le1,
 \qquad 1-\rho=O(H/m)=o(1).
\tag{0.1a}
\]

The local twelve-top exchange in
`MATH_THEOREM_TWELVE_TOP_HISTOGRAM_NEUTRAL_BIDIRECTIONAL_RECHARGE_20260727.md`
is valid after its edge-coloured palette repair.  Its histogram, trace,
and squarefreeness calculations pass audit, subject to three scope
corrections:

1. the file does not explicitly define the retained \(d\)-phase middle
   deck, although \(d\) is introduced;
2. the fixed-root seam normalization putting the exterior placeholders
   at positions \(1,d+1\) should be stated; and
3. an owner-aware orbit is defined only after one complete labelled
   choice of palettes, fillers, retained starts, and the two carrier
   cycles has been frozen.

After making those definitions, take the full
\(\operatorname {Sym}(2m)\)-orbit of the completed template.  Every
resource edge contains

\[
 K=12+12d=12(d+1)
\tag{0.2}
\]

distinct resources: twelve rank-\(M\) tops and the common squarefree
set of \(12d\) rank-\(m\) owners.  If

\[
 N=\binom{2m}{M},\qquad W=\binom{2m}{m},\qquad
 \lambda={W\over N},
\]

then its exact two resource degrees are

\[
 \boxed{
 D_T=12M!(s)_4,\qquad
 D_X=12d\,m!(m)_{H+4},\qquad
 {D_X\over D_T}={d\over\lambda}.}
\tag{0.3}
\]

All top--top and top--owner codegrees are computed below.  For owners
the exact distance-\(j\) identity is

\[
 \boxed{
 {D_{XX}(j)\over D_X}
 ={B_j/(12d)\over\binom mj^2},}
\tag{0.4}
\]

where \(B_j\) is the number of ordered template-owner pairs at Johnson
distance \(j\).  A retained cyclic-interval sphere argument gives

\[
 {D_{XX}(1)\over D_X}\le {36\over m^2},
 \qquad
 \max_{j\ge2}{D_{XX}(j)\over D_X}=O(m^{-3}).
\tag{0.5}
\]

Consequently, in the calibrated regime (0.1a),

\[
 \boxed{
 {\Delta_2\over D_{\min}}=O(m^{-2}),\qquad
 K{\Delta_2\over D_{\min}}=O(m^{-1})=o(1).}
\tag{0.6}
\]

Thus adding all \(12d\) physical owners does **not** create a raw
pair- or higher-codegree obstruction.  There is also a stronger static
whole-packet influence bound of order \(D/m^2\) in the Gaussian regime.

These facts do not prove an owner-aware matching through one layer, and
still less a source-compatible resolution through \(\Theta(m)\)
layers.  The missing stochastic statement is marked hereditary
regeneration of whole-packet influence, aggregate degrees, and the
two-shore cemetery bank in an endogenous residual.  Conditional on the
explicit marked-HPIR package below, the slow greedy process gives a
matching leaving

\[
 O(m^{-1/20})N
\quad\hbox{tops and}\quad
 O\!\left({H\over m}+m^{-1/20}\right)W
\quad\hbox{owners}.
\tag{0.7}
\]

Finally, even a perfect matching in the augmented undirected resource
orbit forgets the literal source shore.  A directed, state-compatible
layer flow remains necessary for repeated recharge.  Section 9 proves
a local-active-time port-core constraint: after \(\kappa=4H-1\)
consecutive moves of one sign at a top, one exterior endpoint is forced
by the earlier state.  A formal endpoint field satisfying asymptotically
flat complete position--label marginals can then leave only
\(O(N/m^6)\) compatible carriers.  This rules out regeneration from
marginals alone, but it is not a trajectory counterexample: sparse
backtracks can avoid every \(\kappa\)-long monotone run at only
\(o(W)\) move cost.  Constant one is therefore not proved.

## 1. Local packet audit and the missing retained-deck definition

The two six-cycles are edge-disjoint, their displayed edge-colouring is
proper at every outside vertex, and each cycle uses every colour once.
The palette budget is exactly

\[
 6(2H-1)+6(H-1)=18H-12\le M-2.
\tag{1.1}
\]

The filler multigraph is regular of degree \(M-5H+1\), so its Koenig
decomposition gives the claimed columnwise equality.  Consequently

\[
 P_j=Q_j
\]

at every rooted column, and

\[
 P_j+Q_{j+1}=P_{j+1}+Q_j
\]

proves the histogram identity, including the cyclic wrap.  The two
six-cycle trace derivatives telescope separately.  The edge-coloured
\(F\)- and \(G\)-palettes also repair the former pure-context
collision.  At the endpoint value \(t=H-1\), the \(F\)-part is empty;
there equality is excluded by the distinct nonempty \(G\)-colours, not
by recovery of an \(F\)-colour.  This is a wording correction, not a
failure of squarefreeness.

For owner-aware packing, one must explicitly import the retained deck.
For each completed rooted word \(p=(p_1,\ldots)\) on a top \(U\), put

\[
 \mathcal O(U,p)=
 \left\{
 U\setminus\{p_j,p_{j+1},\ldots,p_{j+H-1}\}:
 1\le j\le d
 \right\}.
\tag{1.2}
\]

Fix also the seam normalization implicit in the recharge telescope: in
each unrotated row the two exterior placeholders occupy positions
\(1\) and \(d+1\).  After left rotation they occupy \(M\) and \(d\).
The port-core statements in Section 9 use this normalization; it should
be made explicit in the source theorem together with (1.2).

The starts in (1.2) are the intended consecutive retained starts; the
word is read far enough that no displayed interval wraps.  The local
squarefreeness proof says that the twelve sets (1.2) are mutually
disjoint as owner families, so their union has size \(12d\), and the
old and new shores have the same union.

Without (1.2), the symbol \(d\) is unused in the source theorem and the
phrase “all \(12d\) owners” has no defined meaning.  Likewise the
undecorated top packet \((C,S,J)\) does not determine its owners.  From
now on one complete labelled filler/template is fixed.

The assertion that \(\Theta(m)\) top layers contain \(\Theta(W)\)
packet occurrences additionally uses the calibration

\[
                         {W\over N}=\Theta(m);
\tag{1.3}
\]

it does not follow from (0.1) alone.

## 2. The completed role orbit and exact degrees

Let \(R\) be the active role set of the completed template.  It consists
of the \(M-2\) common-core roles and six outside roles, so

\[
                         |R|=M+4.
\tag{2.1}
\]

For every injection \(\phi:R\hookrightarrow[2m]\), take the resource
edge

\[
 E_\phi=
 \{\phi(U):U\text{ one of the twelve top slots}\}
 \ \dot\cup\
 \{\phi(X):X\text{ one of the }12d\text{ owner slots}\}.
\tag{2.2}
\]

The role-labelled orbit has

\[
                         |\mathcal P|=(2m)_{M+4}
\tag{2.3}
\]

edges with multiplicity.  The symmetric group is transitive on physical
tops and on physical owners.  Incidence counting gives

\[
 ND_T=12|\mathcal P|,
 \qquad
 WD_X=12d|\mathcal P|.
\tag{2.4}
\]

Since

\[
 { (2m)_{M+4}\over N}=M!(s)_4,
 \qquad
 { (2m)_{M+4}\over W}=m!(m)_{H+4},
\]

(0.3) follows.  If one passes to the simple orbit, every resource edge
has the same number of labelled representations: two representations
differ by an automorphism of the completed template.  Thus all degrees
and codegrees below are divided by the same constant, and every ratio is
unchanged.

The ratio \(D_X/D_T=d/\lambda\) is important.  Under (0.1a), the
uniform weight \(D_T^{-1}\) saturates every top and loads every owner by
exactly \(d/\lambda\le1\).  Hence there is no fractional top/owner
capacity cut in the calibrated regime.  Without (0.1a), the displayed
degree identity remains true but this capacity conclusion need not.

## 3. A general exact higher-codegree formula

The orbit admits an exact formula at every order.  Let
\(Y_1,\ldots,Y_t\) be distinct physical resources, each of rank \(M\)
or \(m\).  For a tuple of distinct template slots
\(A_1,\ldots,A_t\) of the corresponding ranks, and every nonempty
\(I\subseteq[t]\), put

\[
 c_I=\left|\left(\bigcap_{i\in I}A_i\right)
       \setminus\left(\bigcup_{i\notin I}A_i\right)\right|.
\tag{3.1}
\]

Let \(u=|\bigcup_iA_i|\), and define the physical Venn cells in the
same way.  The slot tuple is compatible with
\((Y_1,\ldots,Y_t)\) precisely when all corresponding cell sizes are
the same.  For one compatible tuple, the number of role injections is

\[
 \left(\prod_{\varnothing\ne I\subseteq[t]}c_I!\right)
 (2m-u)_{M+4-u}.
\tag{3.2}
\]

Indeed, each nonempty domain cell must be mapped bijectively to its
physical cell; the roles outside the union are then injected into the
physical complement.  Therefore, if \(A_{\mathbf c}\) is the number
of ordered template-slot tuples with the prescribed Venn profile,

\[
 \boxed{
 D(Y_1,\ldots,Y_t)=
 A_{\mathbf c}
 \left(\prod_{\varnothing\ne I}c_I!\right)
 (2m-u)_{M+4-u}.}
\tag{3.3}
\]

If the physical profile is absent from the template, the codegree is
zero.  Formula (3.3) is also the complete answer for mixed higher
codegrees.  In particular every codegree of order at least two is at
most each of its constituent pair codegrees.

## 4. Pair codegrees

### 4.1 Two tops

The carrier graph is \(K_6\) minus a perfect matching.  It has twelve
edges.  There are 72 ordered adjacent edge pairs and 60 ordered disjoint
edge pairs.  Hence two distinct physical tops have nonzero codegree only
when their intersection has size \(M-1\) or \(M-2\), and

\[
 D_{TT}(M-1)=72(M-1)!(s-1)_3,
\tag{4.1}
\]

\[
 D_{TT}(M-2)=240(M-2)!(s-2)_2.
\tag{4.2}
\]

After division by \(D_T\),

\[
 \boxed{
 {D_{TT}(M-1)\over D_T}={6\over Ms},\qquad
 {D_{TT}(M-2)\over D_T}
 ={20\over M(M-1)s(s-1)}.}
\tag{4.3}
\]

### 4.2 One top and one owner

Every retained row has exactly \(H\) owners retaining one of its two
outside labels and \(d-H\) owners retaining both.  A singleton-outside
owner is contained in the four carrier tops incident with its retained
outside label and meets the other eight tops in \(m-1\) points.  A
double-outside owner is contained in its own top, meets the six adjacent
carrier tops in \(m-1\) points, and meets the five disjoint carrier tops
in \(m-2\) points.

Thus the ordered top-slot/owner-slot counts at intersections
\(m,m-1,m-2\) are respectively

\[
 12d+36H=12(m+1),
 \qquad 72d+24H,
 \qquad 60(d-H).
\tag{4.4}
\]

Equivalently, relative to one fixed packet top, the numbers are

\[
 A_0=m+1,qquad A_1=6d+2H,qquad A_2=5(d-H),
\tag{4.5}
\]

where \(b\) means intersection size \(m-b\).  Formula (3.2) gives

\[
 \boxed{
 {D_{TX}(m-b)\over D_T}
 ={A_b\over\binom M{m-b}\binom s b}}
 \qquad(0\le b\le2).
\tag{4.6}
\]

In expanded form,

\[
 D_{TX}(m)=12(m+1)m!H!(s)_4,
\tag{4.7}
\]

\[
 D_{TX}(m-1)
 =(72d+24H)(m-1)!(H+1)!(s-1)_3,
\tag{4.8}
\]

and

\[
 D_{TX}(m-2)
 =120(d-H)(m-2)!(H+2)!(s-2)_2.
\tag{4.9}
\]

For \(H\ge3\), all ratios in (4.6) are \(O(m^{-2})\).  The largest
mixed physical core is genuine: every packet top contains exactly

\[
                         d-H+4H=d+3H=m+1
\tag{4.10}
\]

of the packet-owner resources.  Its normalized codegree is nevertheless
\((m+1)/\binom MH\), which is superpolynomially small in the Gaussian
regime.

### 4.3 Two owners

Let \(B_j\) be the number of ordered pairs of distinct owner slots in
the completed template at Johnson distance \(j\).  Two such slots have
union size \(m+j\), so (3.2) gives

\[
 D_{XX}(j)=
 B_j(m-j)!(j!)^2(m-j)_{H+4-j}.
\tag{4.11}
\]

Division by \(D_X\) gives the exact identity (0.4).  Also
\(B_j=0\) for \(j>H+4\), since all owner slots lie in the common active
role set of size \(M+4\).

For \(2j<H\), fix an arbitrary owner \(X\) and one retained row
\(Y_r=V\setminus I_r\), where \(I_r\) is a linear \(H\)-interval.  If
two row owners \(Y_r,Y_{r'}\) are both at distance \(j\) from \(X\),
then

\[
 |I_r\triangle I_{r'}|
 =|Y_r\triangle Y_{r'}|\le4j.
\]

Since \(4j<2H\), the starts satisfy \(|r-r'|\le2j\).  Thus one row
contains at most \(2j+1\) such owners, and all twelve rows contain at
most \(12(2j+1)\).  Consequently

\[
                         B_j\le12d\cdot12(2j+1)
 \qquad(2j<H).
\tag{4.12}
\]

At \(j=1\), (4.12) and (0.4) give

\[
                         {D_{XX}(1)\over D_X}\le{36\over m^2}.
\tag{4.13}
\]

For \(j\ge2\), use (4.12) while \(2j<H\), and otherwise use
\(B_j<(12d)^2\).  Since \(2\le j\le H+4<m/2\), the binomial denominator
in (0.4) gives

\[
                         {D_{XX}(j)\over D_X}=O(m^{-3}).
\tag{4.14}
\]

The order \(m^{-2}\) is sharp: consecutive phases in the twelve paths
give

\[
 B_1\ge24(d-1),
 \qquad
 {D_{XX}(1)\over D_X}\ge {2(d-1)\over dm^2}.
\tag{4.15}
\]

One must not extend (4.12) to every \(j\).  At \(j=H\), a fixed row
owner has \(\Theta(d)\) same-row owners whose deletion intervals are
disjoint from its own.  They are harmless only because
\(\binom mH^{-2}\) is then extremely small.

Combining (4.3), (4.6), and (4.13)--(4.14) proves (0.6).  Formula (3.3)
and monotonicity under adding constraints give the same absolute
\(O(m^{-2})D_{\min}\) upper bound at every higher order.

## 5. Static whole-packet influence

Under the bounded degree ratio in (0.1a), pair codegrees can be summed
using the same physical sphere geometry.
For a resource \(v\) and a packet edge \(e\), put

\[
 I(v,e)=\sum_{w\in e\setminus\{v\}}D(v,w).
\tag{5.1}
\]

For an owner \(v\), group the \(12d\) owner resources of \(e\) by
their Johnson distance from \(v\).  Equations (0.4) and (4.12) give

\[
 {1\over D_X}\sum_{w\in e\cap\mathcal X}D(v,w)
 \le
 \sum_{1\le 2j<H}{144(2j+1)^2\over\binom mj^2}
 +o(m^{-A})
 =O(m^{-2})
\tag{5.2}
\]

for every fixed \(A\); the large-distance part uses the trivial
\(12d\) count and the binomial denominator.  The twelve top resources
add only \(O(m^{-2})\).

For a top \(v\), (4.3) controls the other tops.  The owner contribution
is at most

\[
 O\!\left({m^2\over\binom MH}\right)D_T.
\tag{5.3}
\]

Therefore, uniformly in the Gaussian regime \(H\to\infty\),

\[
 \boxed{
 I(v,e)\le \iota_m D_{\operatorname{type}(v)},
 \qquad
 \iota_m=O(m^{-2})+O\!\left({m^2\over\binom MH}\right)
 =O(m^{-2}).}
\tag{5.4}
\]

The second term in (5.4) matters for the finite endpoint \(H=3\), where
it is only \(O(m^{-1})\).  The constant-one Gaussian application is in
the first regime.

For \(v\notin e\), let

\[
 a_v(e)=|\{f:v\in f,\ f\cap e\ne\varnothing\}|.
\tag{5.5}
\]

For \(v\notin e\), union bounding over the first common resource gives

\[
                         a_v(e)\le I(v,e)\le\iota_mD_v.
\tag{5.6}
\]

Moreover, in (5.7)--(5.8) sum only over \(e\not\ni v\):

\[
 \sum_ea_v(e)
 \le D_vKD_{\max},
\tag{5.7}
\]

because after choosing \(f\ni v\), the conflicting packet \(e\) may
be charged to one of the \(K\) resources of \(f\).  Hence

\[
 \boxed{
 \sum_ea_v(e)^2
 \le \iota_m K D_v^2D_{\max}.}
\tag{5.8}
\]

Thus the owner augmentation also passes the static first-column energy
test for nonkilling jumps.  If \(e\ni v\), then selecting \(e\) kills
the tracked resource and \(a_v(e)=D_v\); including those terms would
make (5.8) false.  Degree martingales are stopped when their root is
killed.  The estimate is stronger than (0.6), but it is still a
time-zero orbit statement.

## 6. A fresh matching bite

There is an unconditional one-round calculation.  Since the completed
orbit is edge-transitive, every packet edge has the same conflict degree

\[
 L_c=|\{f\ne e:f\cap e\ne\varnothing\}|.
\]

Put

\[
 S_0=12D_T+12dD_X.
\tag{6.1}
\]

Bonferroni and (0.6) give

\[
 S_0-1-\binom K2\Delta_2
 \le L_c\le S_0-1,
\]

and therefore

\[
                         L_c=(1+O(m^{-1}))S_0.
\tag{6.2}
\]

Activate every packet independently with probability

\[
                         p={\theta\over S_0},
\tag{6.3}
\]

where \(\theta>0\) is fixed, and retain precisely the activated packets
having no activated conflict.  They form a matching.  A packet is
retained with probability

\[
 p(1-p)^{L_c}
 ={\theta e^{-\theta}+o(1)\over S_0}.
\tag{6.4}
\]

Selected packets incident with one resource are mutually exclusive, so
a top is covered with probability

\[
 q_T={\theta e^{-\theta}+o(1)\over
              12(1+d^2/\lambda)},
\tag{6.5}
\]

and an owner is covered with probability

\[
                         q_X={d\over\lambda}q_T.
\tag{6.6}
\]

Thus one fresh bite is balanced in exactly the fractional proportion,
and has size \(\Theta(1/m)\) on each resource shore.  This calculation
does not justify iterating the bite in the endogenous residual.

## 7. The exact conditional stopped process

The preceding estimates identify a clean sufficient dynamic theorem.
Run continuous random greedy on the active augmented orbit, selecting
each active packet at rate

\[
                         \nu_t={1\over K\mathcal D_T(t)}.
\tag{7.1}
\]

If \(x\) and \(u\) are the surviving top and owner fractions, then the
literal matching ledger is

\[
                         u=1-{d\over\lambda}(1-x).
\tag{7.2}
\]

The product-density degree references are

\[
 \mathcal D_T=D_Tx^{11}u^{12d},
 \qquad
 \mathcal D_X=D_Xx^{12}u^{12d-1}.
\tag{7.3}
\]

Put

\[
 z=m^{-1/20},\qquad T=K\log(1/z).
\tag{7.4}
\]

### HPIR (hereditary packet-influence regeneration)

For every active resource \(v\) outside its cemetery set and every
active packet \(e\not\ni v\), require

\[
 \boxed{
 \sum_{w\in e}d_t(v,w)
 \le \eta(t)\mathcal D_{\operatorname{type}(v)}(t),
 \qquad
 \eta(t)=m^{-2+o(1)}\max\{x(t)^{-1},u(t)^{-1}\}.}
\tag{HPIR}
\]

To make this a sufficient stopped hypothesis, rather than a pointwise
influence slogan, also require the following marked aggregate clauses.
There are monotone cemetery sets \(Q_T(t),Q_X(t)\), whose membership is
frozen when a resource first stops, and a deterministic widening
envelope \(\varepsilon_m=o(1)\), such that uniformly for \(t\le T\),

\[
 |Q_T(t)|\le\varepsilon_m xN,
 \qquad
 |Q_X(t)|\le\varepsilon_m uW,
\tag{7.3a}
\]

and

\[
 \sum_{v\in V_T(t)\setminus Q_T(t)}
 |d_t(v)-\mathcal D_T(t)|
 \le\varepsilon_m xN\mathcal D_T(t),
\tag{7.3b}
\]

\[
 \sum_{v\in V_X(t)\setminus Q_X(t)}
 |d_t(v)-\mathcal D_X(t)|
 \le\varepsilon_m uW\mathcal D_X(t).
\tag{7.3c}
\]

If \(\tau_v\) is the time at which \(v\) was first marked, put

\[
 (r_T,n_T)=(x,N),\qquad (r_X,n_X)=(u,W),
\]

and require, for \(\sigma\in\{T,X\}\),

\[
 \sum_{v\in Q_\sigma(t)}\mathcal D_\sigma(\tau_v)
 \le\varepsilon_m r_\sigma n_\sigma\mathcal D_\sigma(t).
\tag{7.3d}
\]

Edges incident with a cemetery mark may be suppressed, with their full
frozen reference weight charged in (7.3d); require also that the current
degree plus suppressed incidence at each marked \(v\) is at most
\(2\mathcal D_\sigma(\tau_v)\).  Finally require

\[
                         \varepsilon_m\log(1/z)=o(1).
\tag{7.3e}
\]

Call this complete package **marked HPIR**.  The cardinality clauses are
essential: current-incidence control alone permits arbitrarily many
isolated stopped resources of degree zero and would not imply the top
ledger below.  The pointwise inequality is correctly scaled for the
product trajectory, since

\[
 \int_0^T\eta(t)\,dt
 \le m^{-2+o(1)}K\int_z^1{dy\over y^2}
 =O((mz)^{-1+o(1)})=o(1).
\tag{7.4a}
\]

It does **not** by itself imply (7.3b)--(7.3d): link-family overlap and
summed-square influence require a separate marked/quarantine proof.
Those aggregate clauses are explicit hypotheses here.

### Theorem 7.1 (conditional owner-aware near-matching)

Assume (0.1a), and suppose that the stopped construction satisfies
marked HPIR uniformly through time \(T\) on an event of probability
\(1-o(1)\).

Then the stopped greedy process contains, with probability \(1-o(1)\), a
matching \(\mathcal M\) satisfying

\[
 N-12|\mathcal M|=(z+o(1))N,
\tag{7.5}
\]

and

\[
 W-12d|\mathcal M|
 =O\!\left({H\over m}+z\right)W=o(W).
\tag{7.6}
\]

#### Proof

Let \(E_t\) be the number of active packet edges.  On the marked-HPIR
event, (7.3a)--(7.3d) and the marked-resource upper bound give

\[
 12E_t=\sum_{v\in V_T(t)}d_t(v)
 =(1+O(\varepsilon_m))xN\mathcal D_T(t).
\tag{7.7}
\]

Let \(S_t\) be the number of selected packets.  Then exactly

\[
                         x(t)=1-{12S_t\over N}.
\tag{7.8}
\]

Since every active packet rings at rate
\((K\mathcal D_T(t))^{-1}\), the predictable drift is

\[
 \mathbb E[dx(t)\mid\mathcal F_{t-}]
 =-(1+O(\varepsilon_m)){x\over K}\,dt.
\tag{7.9}
\]

The compensated counting martingale has jumps \(12/N\) and predictable
quadratic variation at most

\[
 O\!\left({T\over KN}\right)
 =O\!\left({\log(1/z)\over N}\right)=o(z^2).
\tag{7.9a}
\]

Freedman's inequality therefore makes its terminal error \(o(z)\) with
probability \(1-o(1)\).  Since
\(\varepsilon_mT/K=\varepsilon_m\log(1/z)=o(1)\), integration of the
compensator gives \(x(T)=z(1+o(1))\).  Intersecting this event with the
marked-HPIR event proves (7.5).  Finally the exact matching ledger (7.2)
gives

\[
 {W-12d|\mathcal M|\over W}
 =1-{d\over\lambda}(1-x(T))
 =O(H/m+z),
\]

which is (7.6). \(\square\)

The reference degrees remain enormous through this stop.  Since
\(x,u\ge z\),

\[
 \log\mathcal D_T
 \ge\log D_T+(11+12d)\log z
 =\left({2\over5}+o(1)\right)m\log m,
\tag{7.10}
\]

and similarly for \(\mathcal D_X\).  Thus the obstruction to Theorem
7.1 is not exhaustion of candidate packets; it is proving HPIR in the
endogenous residual.

## 8. Why this does not yet give \(\Theta(m)\) legal recharge layers

For each adjacent rooted-position direction, a conjugate completed
template has the same orbit census.  If Theorem 7.1 were available
uniformly for \(L=\Theta(m)\) independently specified direction
classes, the aggregate missed top-direction mass would be

\[
                         O(LzN)=O(zW)=o(W).
\tag{8.1}
\]

This would solve owner collisions *within* the layers.  It would not
solve chronology.  An undirected augmented edge remembers only its
twelve tops and common owner support.  It does not assert that its old
shore is the word state currently present on those tops.  After a
switch, its new shore need not be the old shore of any packet chosen in
the next matching.

This is a literal obstruction to using a fixed-uniformity top matching,
or even a perfect augmented resource matching, as the whole proof.  The
two directed shores are extra state data.  A legal sequence requires a
resolvable directed flow in which every target shore at time \(i\) is
the source shore at time \(i+1\), with the desired top directions used
without repetition.

A one-shot matching or absorber across all \(L\) layers is also
impossible without recycling resources: top capacity would allow only
\(N/12\) packets, whereas \(L\) near-full layers require
\(LN/12=\Theta(W)\) packet occurrences.  Recycling is therefore part
of the state-flow problem, not a defect that a bounded static absorber
can repair.

No deterministic absorber achieving this directed recycling is
constructed here.  Static formula (3.3) does not imply HPIR after
endogenous restriction; arbitrary edge deletion can concentrate a link
while preserving all time-zero codegrees.

## 9. A port-core constraint and a marginal-only regeneration no-go

The preceding chronology gap has an exact local manifestation.  All
lag statements in this section use **local active-move time at one
top** and concern consecutive standard fixed-root twelve-top recharge
moves.  They do not cover a history interrupted by a different
word-changing primitive, nor may global layer time be substituted when
the top pauses.

For a rooted state

\[
                         w=(w_1,\ldots,w_M)
\tag{9.1}
\]

on a top \(U\), define its two port cores

\[
 C_0(w)=U\setminus\{w_1,w_{d+1}\},
 \qquad
 C_1(w)=U\setminus\{w_M,w_d\}.
\tag{9.2}
\]

### Lemma 9.1 (the two possible source cores)

If \(w\) occurs as one row of a completed fixed-root twelve-top source
shore, its packet common core is either \(C_0(w)\) or \(C_1(w)\).

#### Proof

In an unrotated template row \(p\), the two exterior placeholders are
at positions \(1\) and \(d+1\), so the common core is \(C_0(p)\).
If \(w=rp=(p_2,\ldots,p_M,p_1)\), those same two placeholders are at
positions \(M\) and \(d\), so the common core is \(C_1(w)\).  Every
row on either source shore is of one of these two forms.  The four
positions in (9.2) are distinct under (0.1), so the alternatives are
distinct. \(\square\)

Put

\[
                         \kappa=M-d=4H-1.
\tag{9.3}
\]

### Lemma 9.2 (the lag-\(\kappa\) endpoint law)

Suppose the undirected root edges used in consecutive active moves at
one top are not repeated and the resulting root walk has length less
than \(M\).  Then the walk is monotone.  For left motion from a cyclic
word \(p\), the core used at local active time \(t\) is

\[
 C_t=C_0(r^tp)
 =U\setminus\{p_{t+1},p_{t+d+1}\},
\tag{9.4}
\]

with cyclic indices.  If \(A_t=U\setminus C_t\), then for
\(\kappa\le t<M\),

\[
 \boxed{
 A_t=\{p_{t+1},p_{t-\kappa+1}\},
 \qquad
 p_{t-\kappa+1}\in A_t\cap A_{t-\kappa}.}
\tag{9.5}
\]

The right-moving statement is obtained by reversing the indices.

#### Proof

A change of direction in a walk on the cycle \(C_M\) immediately
retraces the preceding undirected edge.  Thus a nonrepeating walk of
length below \(M\) is monotone.  Formula (9.4) follows from Lemma 9.1
at the successive left roots.  Since \(d=M-\kappa\), cyclic reduction
of the second index in (9.4) gives

\[
                         p_{t+d+1}=p_{t-\kappa+1}.
\]

The latter label is the first displayed label of \(A_{t-\kappa}\),
which proves (9.5). \(\square\)

Thus, after \(\kappa\) consecutive active moves of one sign at that
top, one endpoint of the next exterior pair is forced by the ordered
state \(\kappa\) active moves earlier.
Write this forced endpoint as \(a_t(U)\in U\).

Let \(\mathcal B\) be the undecorated carrier catalogue.  A member is
specified by a common \((M-2)\)-set \(C\), a disjoint six-set \(S\),
and a perfect matching \(J\) on \(S\); its twelve tops are

\[
                         C\cup e,
 \qquad e\in E(K_6\setminus J).
\tag{9.6}
\]

### Lemma 9.3 (endpoint compatibility)

If a late-layer packet with common core \(C\) is legal for a forced
endpoint field \(a\), then

\[
                         \boxed{a(C\cup e)\in e}
\tag{9.7}
\]

for all twelve carrier edges \(e\in E(K_6\setminus J)\).

#### Proof

At the carrier top \(U_e=C\cup e\), the current exterior pair is
exactly \(U_e\setminus C=e\).  Lemma 9.2 forces \(a(U_e)\) to be one
of the two members of that pair. \(\square\)

Condition (9.7) is only necessary.  The palette, filler-column, and
shore-orientation constraints can delete further carriers.

### Theorem 9.4 (a balanced sparse compatible-carrier field)

There is a deterministic choice \(a(U)\in U\) for every
\(U\in\binom{[2m]}M\) such that

\[
 \left|\{U:a(U)=x\}\right|
 =(1+o(1)){N\over2m}
 \qquad(x\in[2m]),
\tag{9.8}
\]

but the number of carriers satisfying (9.7) is only

\[
                         O(Nm^{-6}).
\tag{9.9}
\]

Consequently all compatible carriers together touch only
\(O(Nm^{-6})\) tops.  Moreover the field may be completed to rooted
orders \(w_U\) so that \(a(U)\) occupies any prescribed, possibly
top-dependent, lag position
and, at every rooted position \(j\),

\[
 |\{U:w_U(j)=x\}|=(1+o(1)){N\over2m}
 \qquad(x\in[2m]).
\tag{9.9a}
\]

#### Proof

The exact number of simple carriers is

\[
 \begin{aligned}
 |\mathcal B|
 &=\binom{2m}{M-2}\binom{s+2}{6}\,15\\
 &=N\binom M2\binom s4.
 \end{aligned}
\tag{9.10}
\]

Choose independently for every top \(U\) a uniform rooted order
\(w_U\), and let \(a(U)\) be its label in its prescribed lag position.
A fixed carrier has twelve distinct tops.  At each top the probability
of (9.7) is \(2/M\), and these twelve events are independent.  Hence

\[
 \mathbb E|\mathcal B(a)|
 =N\binom M2\binom s4\left({2\over M}\right)^{12}
 =O(Nm^{-6}).
\tag{9.11}
\]

For a fixed coordinate \(x\), the random variable

\[
                         L_x=|\{U:a(U)=x\}|
\]

is binomial with mean

\[
 \binom{2m-1}{M-1}{1\over M}={N\over2m}.
\tag{9.12}
\]

For every rooted position \(j\) and coordinate \(x\), the analogous
count \(|\{U:w_U(j)=x\}|\) has the same binomial law and mean.  Chernoff
concentration and a union bound over the \(2mM\) position--coordinate
pairs give (9.8) and (9.9a) with probability \(1-o(1)\).  Markov's
inequality gives (9.9), with a fixed constant in the \(O\)-term, with
probability bounded away from zero.  The events therefore occur
simultaneously for all sufficiently large \(m\).  Finally each carrier
has twelve tops, so their union has the asserted size. \(\square\)

There is also a useful exact, though deliberately unbalanced, Hall
cut.

### Proposition 9.5 (a singleton endpoint cut)

For any endpoint field \(a\), put

\[
                         A_x=\{U:a(U)=x\}.
\]

Every compatible carrier contains at most four tops from \(A_x\).
Consequently every top-disjoint compatible packet family
\(\mathcal M\) satisfies

\[
 |A_x\cap V(\mathcal M)|\le4|\mathcal M|\le {N\over3}.
\tag{9.13}
\]

In particular, if \(a(U)=x\) on every top containing \(x\), then

\[
 |A_x|={M\over2m}N=\left({1\over2}+o(1)\right)N,
\tag{9.14}
\]

and every compatible packet matching leaves \(\Omega(N)\) tops.

#### Proof

If a compatible carrier top \(C\cup e\) lies in \(A_x\), (9.7)
implies \(x\in e\).  The graph \(K_6\setminus J\) is 4-regular, so
only four of its twelve edges contain \(x\) (and none do if
\(x\notin S\)).  This proves the first assertion.  A top-disjoint
family has \(12|\mathcal M|\le N\), giving (9.13), while (9.14) is
the elementary top-incidence count. \(\square\)

### Proposition 9.6 (the lag law alone has no constant-one cost)

The sign word

\[
                         (+)^{\kappa-1}-,
                         (+)^{\kappa-1}-,\ldots
\tag{9.15}
\]

has no monotone run of length \(\kappa\), but advances the cyclic root
by \(\kappa-2\) edges per \(\kappa\) active moves.  Relative to pure
forward motion it uses only \(O(1/\kappa)\) backtracking/reset mass.
Consequently, over \(\Theta(W)\) required top-move incidences, this
avoidance costs only

\[
                         O(W/\kappa)=o(W).
\tag{9.16}
\]

#### Proof

Each displayed block has \(\kappa-1\) forward steps and one backward
step, hence net displacement \(\kappa-2\); its longest constant-sign
run has length \(\kappa-1\).  The minus step retraces the preceding
edge, and the first plus of the next block traverses that same edge once
more.  Equivalently the displacement deficit is two per \(\kappa\)
moves.  Since \(\kappa=4H-1\to\infty\), (9.16) follows. \(\square\)

Thus Lemma 9.2 becomes a quantitative chronology obstruction only if a
separate theorem shows that repeated root edges or these sawtooth resets
are physically unusable, or charges them more than their raw
\(O(W/\kappa)\) frequency.  No such theorem is proved here.

Theorem 9.4 is not asserted to be owner-resolved or to arise from a
reachable legal history.  It proves the logically sharper point needed
for this audit: even an asymptotically flat complete rooted
position--label histogram does not imply a positive-density compatible
layer.  Hence no deterministic absorber or stopped-process theorem
based only on the static augmented orbit, pair codegrees, and those
marginals can be valid; owner resolution and reachable-history
correlation remain possible additional hypotheses.

Once a coefficient-one source table has been installed, a simultaneous
top-disjoint firing automatically remains owner-disjoint: its source
owners were already distinct globally, and each packet preserves its
exact owner support.  Thus at time \(t\) the relevant object is the
12-uniform hypergraph \(\mathcal P_t\) of packets whose **complete
source shores are literally present**.  The minimum dynamic precursor
is a near-cover theorem for \(\mathcal P_t\), including (9.7), with
aggregate leave \(o(W)\) over the \(\Theta(m)\) layers.  Abstract
near-matchings in the time-zero augmented orbit do not establish this.

## 10. Exact remaining statement and adversarial audit

The minimum positive package presently visible has two parts.

1. **Stopped owner-aware packing:** prove the full marked-HPIR package
   (pointwise residual influence, aggregate two-shore degree tracking,
   and frozen cemetery bounds) through time
   \(K\log(m^{1/20})\).  Theorem 7.1 then produces one near-perfect
   augmented matching.
2. **Directed resolution:** propagate the old/new shore states through
   \(\Theta(m)\) conjugate layers, allowing an aggregate
   \(o(W)\) exceptional direction mass.  Equivalently, prove an
   aggregate near-cover theorem for the actual source-shore
   hypergraphs \(\mathcal P_t\), with pauses, backtracks, palettes, and
   owner-resolved reachability included.

The independent audit found the following tempting but invalid
shortcuts.

* The top-only 12-uniform Pippenger--Spencer matching ignores all
  \(12d\) owners.
* The statement \(K\Delta_2/D=o(1)\) is static; it does not regenerate
  codegrees or whole-packet influences in a random residual.
* A bound of \(O(j)\) owners in one cyclic sphere is false at
  \(j=H\); the proof must split at \(2j<H\) and use the binomial factor
  afterwards.
* A perfect undirected owner-aware matching still does not certify that
  its source shores are present.
* The lag-\(\kappa\) endpoint law applies only in local active-move time
  on a nonbacktracking monotone segment.  Sawtooth resets evade it at
  raw cost \(o(W)\).
* The balanced sparse endpoint field is not owner-resolved and is not
  proved reachable.  It refutes marginal-only regeneration, not a
  specially correlated trajectory-aware process.
* \(\Theta(m)\) abstract colour classes give \(\Theta(W)\) volume only
  under the separate calibration \(W/N=\Theta(m)\).

Accordingly the static owner-codegree concern is closed, but neither the
stopped matching process nor the directed \(\Theta(m)\)-layer compiler
is unconditional.  Constant one remains open.
