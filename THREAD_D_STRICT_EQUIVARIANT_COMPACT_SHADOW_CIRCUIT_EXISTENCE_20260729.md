# Strict equivariant compact-shadow circuits: existence-method audit

Date: 2026-07-29

Status: pure mathematics.  No unconditional existence proof is obtained.
The report proves an exact root-transversal automaton reduction, the maximal
TU subproblem, sharp load and dependency bounds, and a conditional
path-forest/connector theorem.  It also identifies why ordinary LLL,
two-matroid intersection, unlabelled robust expansion, and a small terminal
absorber do not close the simultaneous shadow problem.

## 1. The exact object

Put

\[
 k=2m+1,\qquad r=m+1,\qquad
 W={k\choose r},\qquad N=W/k=\operatorname {Cat}_m.
\tag{1.1}
\]

Let \(C_k\) act by cyclic coordinate translation.  The two central actions
are free.  Define the bipartite quotient middle-levels multigraph

\[
 \mathcal B_k=
 \left({[k]\choose m}/C_k,
       {[k]\choose r}/C_k; E_{\subseteq}/C_k\right).
\tag{1.2}
\]

It has \(N\) vertices on each shore and is \(r=m+1\)-regular.  Parallel
incidence orbits are retained.  A pair of distinct incidence edges at a
lower vertex contracts to one coloured edge of the quotient Johnson
multigraph.  The colour is that lower vertex.

### Proposition 1.1 (circuit equivalence)

Strict equivariant lower-rainbow Johnson circuits are precisely the connected
spanning 2-factors of \(\mathcal B_k\) whose cyclic voltage generates
\(\mathbb Z_k\).

#### Proof

Degree two at every lower vertex chooses one Johnson edge over every lower
colour orbit.  Degree two at every upper vertex gives every upper owner orbit.
Contracting the lower shore gives a connected two-regular Johnson quotient,
hence one quotient circuit.  Conversely, expand each coloured Johnson edge
through its lower colour.  The regular cyclic lift of a quotient circuit of
voltage \(v\) consists of \(\gcd(k,v)\) cycles, so it is one physical cycle
exactly when \(v\) is a unit.  \(\square\)

This formulation separates the central 2-factor from chronology.  To include
residence, let a queue state be

\[
 (U;b_1,\ldots,b_d),                                    \tag{1.3}
\]

where \(U\) is an upper necklace root and the \(b_i\) are the ordered last
\(d\) inserted coordinates in a normalized representative of \(U\).  A
legal Johnson transition deletes

\[
 a\in U\setminus\{b_1,\ldots,b_d\},
\]

inserts \(b\notin U\), and shifts the queue.  Residence makes the queued
coordinates distinct.  The quotient queue automaton has at most

\[
 N(r)_{\underline d}                                    \tag{1.4}
\]

states and exact outdegree

\[
 m(r-d).                                                 \tag{1.5}
\]

Each automaton arc retains its upper root, lower colour, physical phase, and
voltage.  The compact state-path lemma says that a lower target \(S\) at
depth \(q\) is hit exactly when the selected cycle contains a \(q\)-arc path
whose \(q+1\) lifted upper states intersect to \(S\); the upper version uses
their union.  Therefore the full compact carrier problem is exactly:

> Find one directed cycle in the residence queue automaton which is a
> transversal of every upper root and every lower root, has unit voltage, and
> hits every prescribed signed shadow-path colour.

This is a root-transversal, multi-colour Hamilton problem in a
de Bruijn/Schreier-type automaton.  It is already integral; a fractional
circulation is only an intermediate object.

The current production compact gates at \(k=15\) are upper \(q=1\), lower
and upper \(q=2,3\), and residence \(d=3\).  The same state-path equivalence
holds at every \(q\).  Deeper upper windows, an upper-safe linear cut, and the
graded lower compiler are additional gates and are not silently included in
the theorem sought here.

## 2. The two critical hinge maps

Write a selected segment of the expanded factor as

\[
 U_i,L_i,U_{i+1},L_{i+1},U_{i+2}.
\]

At a lower vertex \(L\), the selected pair is

\[
 L\cup\{a\},\quad L\cup\{b\};
\]

its upper-\(q=1\) label is

\[
 L\cup\{a,b\}.                                          \tag{2.1}
\]

At an upper vertex \(U\), the selected lower pair is

\[
 U\setminus\{a\},\quad U\setminus\{b\};
\]

its lower-\(q=2\) label is

\[
 U\setminus\{a,b\}.                                     \tag{2.2}
\]

Thus upper \(q=1\) and lower \(q=2\) are two turn-label surjections on the
opposite shores of the same 2-factor.  Choosing the two turns independently
is invalid: for every incidence \(L\subset U=L\cup\{a\}\),

\[
 a\hbox{ is selected at }L
 \quad\Longleftrightarrow\quad
 a\hbox{ is selected at }U.                             \tag{2.3}
\]

This compatibility, not either marginal layer, is the first integral gate.

The marginal upper-\(q=1\) assignment is easy.  Join a rank-\(m\) centre
\(L\) to every rank-\(m+2\) target containing it.  The two degrees are

\[
 D_0={m+1\choose2},\qquad H_0={m+2\choose2}>D_0.         \tag{2.4}
\]

For any target set \(X\), all \(H_0|X|\) incident edges end in its lower
neighbourhood, whose vertices have degree at most \(D_0\).  Hence

\[
 |N(X)|\ge(H_0/D_0)|X|>|X|,
\]

and Hall gives a matching of every target to a distinct centre.  The dual
lower-\(q=2\) marginal is identical.  Consequently scalar capacity and
rankwise Hall are not the obstruction.

There is also an exact symmetric fractional point for the first marginal:
put weight \(1/H_0\) on every inclusion \(L\subset Z\).  Every target has
load one, every lower centre has load

\[
 D_0/H_0=m/(m+2)<1,
\]

and every upper owner has endpoint load

\[
 \frac{m(m+1)}{H_0}=\frac{2m}{m+2}<2.                  \tag{2.5}
\]

The subunit pointwise slack in (2.5) explains why generic additive-one
rounding is insufficient.

## 3. Exact shadow load: every shallow row is a near-design

For a rank \(a\), let

\[
 \operatorname {Orb}_k(a)=\frac1k
 \sum_{\ell\mid\gcd(k,a)}
 \varphi(\ell){k/\ell\choose a/\ell}.                  \tag{3.1}
\]

Put

\[
 t_q^- =\operatorname {Orb}_k(r-q),\qquad
 t_q^+ =\operatorname {Orb}_k(r+q).                     \tag{3.2}
\]

Complementation gives \(t_{q+1}^-=t_q^+\).  If the circuit is
\(d\)-resident, every \(q\)-window with \(q\le d\) has the exact lower and
upper ranks.  Let \(L_q^\pm(T)\) be its quotient-start load on target orbit
\(T\).  Since there are exactly \(N\) quotient starts,

### Lemma 3.1 (repeat--hole identity)

\[
 \boxed{
 \sum_T(L_q^\pm(T)-1)_+
   =N-t_q^\pm+\#\{T:L_q^\pm(T)=0\}.}
\tag{3.3}
\]

#### Proof

Separate the load sum \(N=\sum_TL_q^\pm(T)\) into occupied targets, one
baseline copy per occupied target, and its repeat excess.  The number of
occupied targets is \(t_q^\pm-H_q\).  Rearrangement gives (3.3).
\(\square\)

Thus hole-free coverage is exactly the minimum possible repeat excess.
Ignoring the exponentially smaller periodic-layer correction,

\[
 \lambda_q^-:=N/t_q^-
 =\frac{W}{{2m+1\choose m+1-q}},
 \qquad
 \log\lambda_q^-
 =\frac{q(q-1)}m+O(q^3/m^2),                            \tag{3.4}
\]

and

\[
 \lambda_q^+=\lambda_{q+1}^-.
\tag{3.5}
\]

For the coefficient-one application, let \(d_*\) be the least integer with

\[
 d_*W+{d_*+1\choose2}\ge4^m-1.                         \tag{3.6}
\]

Then

\[
 d_*=\frac{\sqrt\pi}{2}\sqrt m+O(1),                  \tag{3.7}
\]

because the complete lower mass is \(4^m-1\).  Hence throughout the whole
application band \(q\le d_*\)

\[
 \lambda_q^\pm\le e^{\pi/4+o(1)}.                      \tag{3.8}
\]

In particular

\[
 N-t_1^+=N-t_2^-=\left(\frac2m+O(m^{-2})\right)N.      \tag{3.9}
\]

The two hinge maps must therefore be almost bijections.  A diffuse random
map, which leaves a constant fraction of its coupons empty, is on the wrong
scale by a factor \(m\).

## 4. Exact finite calibration at k=15

For general \(q\), one lower target has

\[
 s_q^-={m+q\choose q},\qquad
 a_q^-=q m s_q^-                                         \tag{4.1}
\]

central states and directed transition rows.  One upper target has

\[
 s_q^+={m+1+q\choose q},\qquad
 a_q^+=q(m+1)s_q^+.                                     \tag{4.2}
\]

For \(q\le d=\Theta(\sqrt m)\), these are
\(\exp(O(\sqrt m\log m))=N^{o(1)}\) per target.  Compactness therefore
removes the enormous explicit DNF, but it does not make the miss event
probabilistically rare.

Here

\[
 (m,r,d,N)=(7,8,3,429).                                 \tag{4.3}
\]

The expanded quotient has \(858\) vertices, degree eight, and \(3432\)
incidence-edge orbits.  The contracted catalogue has

\[
 429{8\choose2}=12012                                  \tag{4.4}
\]

choices; 14 are quotient loops, leaving 11,998 strict-circuit choices.  The
residence automaton bounds are

\[
 429(8)_{\underline3}=144144\quad\hbox{states},
 \qquad 35\quad\hbox{outdegree},
 \qquad 5{,}045{,}040\quad\hbox{arcs}.                 \tag{4.5}
\]

The target-orbit capacities are

| row | target orbits | repeat slack `N-t` |
|---|---:|---:|
| upper `q=1` | 335 | 94 |
| lower `q=2` | 335 | 94 |
| upper `q=2` | 201 | 228 |
| lower `q=3` | 201 | 228 |
| upper `q=3` | 91 | 338 |

The compact state domains, directed transition rows, optimistic shared-arc
dependency degrees, and corresponding symmetric-LLL thresholds are

| gate | states/target | directed rows | dependency degree | `1/[e(Delta+1)]` |
|---|---:|---:|---:|---:|
| lower `q=2` | 36 | 504 | 54 | 0.00669 |
| lower `q=3` | 120 | 2520 | 500 | 0.000734 |
| upper `q=2` | 45 | 720 | 50 | 0.00721 |
| upper `q=3` | 165 | 3960 | 374 | 0.000981 |

The dependency formulas are

\[
 \Delta_q^-=
 \sum_{j=1}^{q-1}{r-q\choose j}{m+q\choose j},
 \qquad
 \Delta_q^+=
 \sum_{j=1}^{q-1}{r+q\choose j}{m-q\choose j}.         \tag{4.6}
\]

They are already \((1+o(1))m^{2q-2}/((q-1)!)^2\) for fixed \(q\).

The current residence-perfect strict seed has missing-orbit vector

\[
 (H_{U1},H_{L2},H_{U2},H_{L3},H_{U3})=(67,47,27,11,1).
\tag{4.7}
\]

By (3.3), its repeat ledgers are

| row | holes | repeat excess |
|---|---:|---:|
| upper `q=1` | 67 | 161 |
| lower `q=2` | 47 | 141 |
| upper `q=2` | 27 | 255 |
| lower `q=3` | 11 | 239 |
| upper `q=3` | 1 | 339 |

For scale comparison, the iid quotient-coupon benchmarks for 429 starts are

\[
 (334/335)^{429}=0.277\ldots,
 \quad(200/201)^{429}=0.118\ldots,
 \quad(90/91)^{429}=0.0087\ldots.                       \tag{4.8}
\]

They predict approximately 93, 24, and 0.8 holes in the three orbit layers.
The resident seed is polarized relative to that benchmark at several rows,
and its two critical leaves are already on the natural \(\Theta(N/m)\)
completion scale.  What is missing is a degree-preserving, multi-ledger
connector/absorber at that scale; the exact one-row repair loses degree two.

Thus the problem is to remove exactly the excess above the fixed floor while
retaining the other ledgers.  The exact upper-\(q=1\) choice repair changes
67 of 429 lower choices, meeting the unavoidable lower bound, but its degree
incidence has \(L^1\)-distance 156 from degree two.  It is a shadow scaffold,
not a factor; at least 39 further choice changes are needed from that
scaffold merely to restore the degrees.

For comparison, the canonical MMM circuit has 38 missing upper-\(q=1\)
orbits, 38 missing lower-\(q=2\) orbits, 36 missing lower-\(q=3\) orbits,
and 132 rotation orbits of short residence runs.  These facts show that
the canonical cycle is not a residence-safe last-mile object.  The
residence-first seed reaches the correct \(N/m\) order in its two tight
shadow leaves, but its known exact one-row repair is not a 2-factor; the
missing last-mile primitive is degree- and history-preserving.

## 5. Total unimodularity and matroid intersection

The natural central-edge TU subsystem is

\[
 P_2=\{x\in[0,1]^{E(\mathcal B_k)}:
         x(\delta v)=2\ (v\in V(\mathcal B_k))\}.       \tag{5.1}
\]

The incidence matrix of a bipartite graph is TU, so every vertex of \(P_2\)
is an integral spanning 2-factor.  Fractional-to-integral rounding is
therefore unconditional through the complete central cycle-cover gate.
It does not give one component, unit voltage, residence, or shadows.

The contracted chronological matrix is not TU on the actual catalogue.  At
\(k=15\), take

\[
 L=\{0,1,\ldots,6\},\quad
 A=L+7,\ B=L+8,\ C=L+9.
\]

The three upper necklaces are distinct, and the three legal pair choices
\(AB,BC,CA\) have upper-incidence submatrix

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad\det=2.                                          \tag{5.2}
\]

The same local triangle appears whenever pair-state variables are linked to
three distinct incident darts.  Uncontracting removes (5.2) for the bare
2-factor; the direct chronological pair/path formulation restores it.  This
minor refutes TU of that literal matrix.  It does not rule out an unknown
extended TU formulation.

At the abstract slot-colour level, one signed shadow row in isolation is a
partition-matroid elongation: an \(N\)-set of slots covers \(t_q\) target
colours while using \(N-t_q\) repeat slots.  The literal formulation couples
upper-root, lower-root, and several elongated target partitions with
successor overlap, connectivity, and a modular voltage condition.  Generic
three-partition systems are three-dimensional matching rather than ordinary
two-matroid intersection, so the standard theorem does not apply directly.
This is not a reduction proving hardness or excluding a catalogue-specific
extended matroid formulation.  The family of spanning 2-factors is not
itself a matroid base family: in a simple graph, replacing one edge of one
2-factor by one edge of another cannot preserve all degrees unless the edge
has the same endpoints.

## 6. Why the natural LLL models fail

First choose independently one of \({r\choose2}\) pairs at every physical
lower set, temporarily ignoring compatibility at the upper shore.  A fixed
upper set has

\[
 \deg(U)\sim\operatorname {Bin}\left(r,\frac2r\right),
\]

so

\[
 \Pr(\deg U=2)\longrightarrow2e^{-2}.                  \tag{6.1}
\]

The bad-degree dependency is \(m(m+1)\).  At \(k=15\),

\[
 \Pr(\deg U=2)=5103/16384,
 \qquad \Delta=56.                                     \tag{6.2}
\]

Thus a random lower transversal is exponentially rarely even a 2-factor;
conditioning on degree two is not a local perturbation.

For a fixed upper-\(q=1\) target the same favourable product relaxation gives

\[
 p_{\rm miss}=
 \left(1-{r\choose2}^{-1}\right)^{{r+1\choose2}}
 \longrightarrow e^{-1}.                              \tag{6.3}
\]

At \(k=15\), this is \((27/28)^{36}=0.270\ldots\), with
variable-dependency degree 594.  More generally, (3.8) leaves the diffuse
empty-target probability bounded away from zero throughout the residence
band.

The lopsided version does not cure the coupon problem.  In the iid benchmark
of \(N\) starts placed among \(b\) targets, for two empty-target events
\(A_i,A_j\),

\[
 \Pr(A_i\mid\neg A_j)>\Pr(A_i).                         \tag{6.4}
\]

Hence the valid lopsided dependency graph is complete.  Its best symmetric
criterion requires

\[
 p_{\rm empty}\lesssim1/(eb),                           \tag{6.5}
\]

whereas here it is constant.  Reaching (6.5) would require average load
\(\Omega(\log b)\), or \(q\gtrsim\sqrt{m\log m}\), outside
\(d=\Theta(\sqrt m)\).

Even the exact compact local dependencies in (4.6) would require
\(p_{\rm miss}=O(m^{-2q+2})\), not a constant.

Residence alone is closer.  Take \(d=d_*\) and use the favourable
nonbacktracking Johnson-walk proxy.  In that particular parametrization,

\[
 p_{\rm short}
 =1-\left(1-\frac1{r-1}\right)^{d-1}
 =\frac{\sqrt\pi}{2\sqrt m}+O(m^{-1}).                  \tag{6.6}
\]

Grouping the short returns gives

\[
 e p(\Delta+1)\longrightarrow e\pi/2>1;
\]

splitting by exact delay still gives \(3e\pi/8>1\).  At \(k=15\),
\(p_{\rm short}=13/49\) and the grouped dependency is at most four.  A
special residence resampling theorem is not excluded, but residence is not
the dominant obstacle: it would still leave the near-design shadows.

## 7. Ordinary robust expansion is the wrong expansion

The contracted quotient Johnson multigraph has degree

\[
 D=m(m+1).                                               \tag{7.1}
\]

The \(E_1\) Johnson module is the coordinate-sum-zero standard module, whose
fixed space under a full \(k\)-cycle is zero.  Nonconstant cyclic
pair-distance functions give fixed vectors in \(E_2\), and the Johnson
eigenvalues decrease with the module index.  Hence the second largest
quotient eigenvalue is

\[
 \theta_2=m(m-3),
\]

and the normalized second-eigenvalue gap is

\[
 \frac{D-\theta_2}{D}=\frac4{m+1}\longrightarrow0.     \tag{7.2}
\]

For \(k=15\), \(D=56\), \(\theta_2=28\), and the gap ratio is \(1/2\).
This is useful ordinary expansion at the finite instance, but it is not a
uniform robust-expander hypothesis.

More seriously, one residence history forbids up to \(dm\) Johnson
extensions, while the spectral gap is only \(4m\).  Since
\(d=\Theta(\sqrt m)\), ordinary spectral resilience does not pass to the
queue automaton.  Expansion of the unlabelled quotient also says nothing
about whether the surviving endpoint arcs carry unused lower colours,
needed shadow labels, safe boundary histories, and useful voltage.

The exact scale appears already after installing upper \(q=1\).  A spanning
path forest using one edge for each of the \(t_1^+\) targets would have

\[
 s=N-t_1^+=\left(\frac2m+O(m^{-2})\right)N              \tag{7.3}
\]

components and the same number of unused lower colours.  If endpoints and
unused colours behaved generically, a port would see only

\[
 D(s/N)^2\longrightarrow4                               \tag{7.4}
\]

usable connectors.  At \(k=15\), the calibration is

\[
 56(94/429)^2=2.69\ldots.                               \tag{7.5}
\]

Thus the minimal reserve produces constant connector degree, not the
logarithmic no-isolated-port regime of the binomial endpoint model.  This is
not a deterministic obstruction to a specially correlated constant-degree
connector graph; it says precisely that the endpoints and colours must be
engineered rather than treated as independent.

If a reserve fraction \(\rho\) must hit one further independent target
ledger, the generic calibration becomes \(D\rho^3\); for \(L\) ledgers it is
\(D\rho^{L+2}\).  Making this dominate \(\log N=\Theta(m)\) requires

\[
 \rho\gg m^{-1/(L+2)},                                  \tag{7.6}
\]

far larger than the natural \(2/m\) slack.  This is not an impossibility
bound; it is the exact reason unlabelled robust expansion does not imply the
decorated connector cut.

## 8. Exact path-forest completion theorem

The useful positive reduction is not a small prescribed forest but a nearly
spanning decorated path forest.

Let \(F\) be a directed spanning path forest on the \(N\) upper roots.  Its
edges use distinct lower colours.  Write its components as
\(P_1,\ldots,P_s\), with initial and terminal history ports \(a_i,b_i\), and
suppose exactly \(s\) lower colours are unused.  Protect any compact shadow
witness lying wholly inside a component.  Let \(\mathcal R\) be the residual
target obligations; cross-component windows are allowed to serve them.

A connector option

\[
 (b_i,a_j;c,\omega)                                     \tag{8.1}
\]

is a directed quotient arc from the terminal port of \(P_i\) to the initial
port of \(P_j\), with unused colour \(c\) and voltage increment \(\omega\),
whose one-seam length-\(d\) boundary histories are residence-safe.  A
connector selection is **fully decorated** if it

1. uses every terminal port, initial port, and unused colour once;
2. makes every cyclic length-\(d\) history in the fully concatenated word
   residence-safe, including windows crossing more than one seam;
3. covers every obligation in \(\mathcal R\) by its cross-seam compact
   paths;
4. preserves every protected internal witness; and
5. has unit total voltage after adding the forest voltage.

If every path component has at least \(d\) internal arcs, the one-seam tests
already imply item 2.  Shorter components require the stated global test.

### Theorem 8.1 (decorated forest-to-circuit theorem)

If a fully decorated connector selection induces one cycle on the component
set \([s]\), then its union with \(F\) is the required strict equivariant,
resident, compact-shadow-complete circuit.

#### Proof

Contract every path component.  The port and colour equalities make the
union an exact colourful directed 2-factor.  Its components are exactly the
cycles of the induced successor permutation on \([s]\).  The one-cycle
hypothesis gives a quotient Hamilton circuit.  Internal path words are
unchanged, every new length-\(d\) boundary word was explicitly checked, and
the two shadow ledgers cover all internal and residual targets.  Unit voltage
gives one physical lift.  \(\square\)

This theorem has an exact switch-expansion version.  Given two connector
arcs

\[
 i\to\pi(i),\qquad j\to\pi(j),
\]

replace them by the crossed arcs

\[
 i\to\pi(j),\qquad j\to\pi(i).                          \tag{8.2}
\]

If \(i,j\) lie in distinct cycles, an admissible decorated crossing merges
them.  Hence a connector 2-factor can be made Hamilton whenever, at every
intermediate fully decorated factor reachable by earlier safe crossings,
every nontrivial union of its cycles has a crossing pair which leaves the
new factor fully decorated.  Equivalently, one may preselect a conflict-free
cycle-merging switch system.  A sufficient robust cut, required for every
reachable intermediate factor, is

\[
 \#\{(i,j)\in A\times\bar A:
       \text{the crossing (8.2) is decorated-safe}\}
 \ge\zeta|A||\bar A|.                                  \tag{8.3}
\]

Equation (8.3), not expansion of the unlabelled Johnson graph, is the needed
robust-expansion hypothesis.

The forest cannot protect every shallow target internally at the minimal
\(q=1\) size: its cross-seam windows are essential.  At depth \(q\), at most
\(qs\) cyclic starts cross the \(s\) seams.  Thus the natural exact target is
an internal near-design with at most \(O(qs)\) residual obligations, followed
by a connector word which supplies those obligations coherently.

## 9. What absorption can and cannot do

Let

\[
 J=|E_{\rm old}\setminus E_{\rm new}|
  =|E_{\rm new}\setminus E_{\rm old}|,                 \tag{9.1}
\]

half the symmetric-difference size.  At most \(qJ\) old \(q\)-windows are
destroyed and at most \(qJ\) new ones are created.  Hence

\[
 J\ge H_q/q                                               \tag{9.2}
\]

is necessary to repair \(H_q\) missing targets at depth \(q\).  Residence
can change only in the \(O(dJ)\) seam collar.  The \(k=15\) seed therefore
forces \(J\ge67\) from upper \(q=1\) alone.

In a complete critical row with \(t=N-e\), repeat excess is exactly \(e\).
At most \(e\) targets can be repeated and at most \(2e\) start positions can
lie in repeated fibres.  Thus at least

\[
 N-2e=N-O(N/m)                                           \tag{9.3}
\]

starts are sole witnesses.  Almost the whole critical chronology is
protected; a generic local Hamilton switch is unsafe.

A valid absorber must have the same owner set, lower-colour set, boundary
history, protected shadow signature, and voltage, except for its advertised
missing-versus-repeat exchange.  If each of \(B\) residual defects has \(A\)
candidate transparent absorbers and choosing one absorber conflicts with at
most \(H\) candidates for each other defect, then

\[
 A>(B-1)H                                                \tag{9.4}
\]

greedily gives disjoint absorbers.  With \(O(d)\)-sized collars, this is a
last-mile theorem only after an additional packing estimate.  For example,
if a concrete bank has \(A=O(N)\) candidates per defect and every chosen
absorber blocks \(H=\Omega(d)\) candidates for another defect, then (9.4)
can certify only \(B=O(N/d)\) defects.  Those bounds are not automatic from
collar size.  Under such bounds the primary leave must be \(O(N/d)\), and
preferably \(O(N/m)\).  A diffuse random circuit has \(\Theta(N)\) shallow
holes, so this conventional greedy absorber cannot start from the diffuse
model.

## 10. Method verdict and the surviving theorem

| Method | What it proves | Exact failure at the joint gate |
|---|---|---|
| bipartite TU / `b`-matching | an integral spanning central 2-factor | no connectivity, history, voltage, or shadow control |
| ordinary matroid intersection | isolated root or abstract one-row constraints | the direct model has a determinant-two pair minor and at least three coupled partitions; no suitable extended two-matroid representation is known |
| product random choice / lopsided LLL | useful local abundance estimates | degree-two and shallow miss probabilities stay constant; coupon lopsidependency is complete |
| residence LLL | plausibly improvable with a special resampler | elementary constants still exceed one and shadows remain |
| ordinary robust expansion | topology in the undecorated quotient | normalized gap vanishes and decorated connector degree is only constant at natural slack |
| small absorption | completion of an already polarized near-design | diffuse random factors have too many holes; the current seed has the right order but no multi-ledger degree-preserving absorber, and almost all complete-row witnesses are protected |

The strongest precise remaining statement is the following.

### Decorated root-transversal path-forest theorem (open)

Construct a spanning, lower-colour-simple path forest in the residence queue
automaton with

1. \(s=(2+o(1))N/m\) deliberately engineered history ports and unused
   colours;
2. upper-\(q=1\), lower-\(q=2\), and every other compact row covered except
   for at most \(O(qs)\) explicitly tagged cross-seam obligations;
3. a fully decorated connector system satisfying the cut (8.3); and
4. reachable unit voltage.

Theorem 8.1 would then give the desired strict circuit.  An unquantified
\(o(N)\) shadow leave is insufficient: the critical natural reserve is
\(\Theta(N/m)\), while a bound such as \(o(N/m)\) is of course stronger.
Proving only expansion of the quotient graph is also not
enough: the needed object is decorated expansion in the queue/history
root-transversal.

One structured possible escape is complement-antipodality.  In that class,
upper depth \(q\) and lower depth \(q+1\) become the same shifted flag ledger,
and residence becomes a finite set of colour-distance exclusions.  This
halves the principal shadow systems, but no theorem currently supplies the
same cycle with strict rotational equivariance, the full flag cover, and the
required colour exclusions.  It is an architecture for the open path-forest
theorem, not an existence proof.

The final conclusion is therefore sharp: central integrality, marginal Hall,
local path abundance, and ordinary expansion are all proved.  The missing
mathematics is a **joint near-design plus decorated connector theorem** for
the residence queue automaton.
