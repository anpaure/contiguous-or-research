# Pair-cube packet orbits: exact codegrees and the augmented-slot nibble barrier

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let \(1\le r\le m\), and put \(R=2^r\).  A pair-cube frame consists of

* a full core \(F\) of size \(m-r\);
* an empty core \(G\) of size \(m-r\); and
* an unordered perfect matching \(M\) on the remaining \(2r\) points.

Its owner packet is

\[
 P(F,M)=\{F\cup Z: Z\text{ contains one endpoint of every pair of }M\},
 \qquad |P(F,M)|=R.                                      \tag{0.1}
\]

The hypergraph edges below are individual packets.  A matching may choose
owner-disjoint packets coming from different full cores, empty cores, and
pair matchings.  It does **not** choose one global frame or one whole
\(U_\kappa\)-option and then inherit all of that option's packets.

For the physical-frame catalogue, the exact owner degree is

\[
 \boxed{D_r=\binom mr^2r!.}                              \tag{0.2}
\]

If two middle owners have Johnson distance \(d\), their packet
codegree is zero for \(d>r\), while for \(0\le d\le r\),

\[
 \boxed{\lambda_d=d!(r-d)!\binom{m-d}{r-d}^2}             \tag{0.3}
\]

and therefore

\[
 \boxed{
 {\lambda_d\over D_r}
 ={1\over\binom rd}
  \left({(r)_{\underline d}\over(m)_{\underline d}}\right)^2.} \tag{0.4}
\]

Thus the proposed ratio is correct.  It is independent of the standard
indexing convention: ordering the pairs, orienting them, or adding a
distinguished phase multiplies both (0.2) and (0.3) by the same constant
number of indices per physical frame.  An owner-dependent orientation is
not a packet index and must not be used in a hypergraph degree census.

The maximum owner pair-codegree ratio is \((1+o(1))r/m^2\) when
\(r=o(m)\), but this maximum is misleadingly pessimistic.  For one fixed
packet, the aggregate second overlap of its owner stars is only

\[
 {RD_r\over2}\sum_{d=1}^r
 \left({(r)_{\underline d}\over(m)_{\underline d}}\right)^2
 =RD_r\,O\left({r^2\over m^2}\right).                    \tag{0.5}
\]

Hence its owner-conflict neighborhood has size
\((1-O(r^2/m^2))RD_r\).  The unrestricted owner packet orbit is not
blocked by a projective-plane-type concentration.

The situation changes after adding the mandatory signed target slots
needed for coefficient one.  The exact augmented hypergraph is formulated
below.  Every assertion below using the phrase **Gaussian window** assumes

\[
 a\sqrt m\le H\le r,\qquad H=o(m^{2/3}),\qquad
 \log m\ll r=o(m),                                      \tag{0.5a}
\]

for one fixed \(a>0\).  Under these hypotheses its dump-contracted
physical core has edge size

\[
 K_{\rm mand}
 =(1+o(1))R\left(1+2\sum_{q\le H}{N_q\over W}\right)
 =\Theta(R\sqrt m)                                      \tag{0.6}
\]

on a Gaussian window.  A mandatory depth-one target lies in the column
with the two packet owners containing it.  At an exactly regular orbit
point this forces

\[
 \boxed{{\Delta_2\over D}\ge {2\over m+1}.}              \tag{0.7}
\]

Consequently

\[
 K_{\rm mand}{\Delta_2\over D}
 =\Omega\left({2^r\over\sqrt m}\right),                  \tag{0.8}
\]

which diverges superpolynomially when \(\log m\ll r=o(m)\).

This still does not prove that an integral packet factor is impossible.
It proves something sharper about the proposed matching method.  Even
allowing **all** pair frames, all local cube 2-factors, and all quota
markings, a fixed retained owner's link in a product-thinned residual of
polynomial density is empty with probability \(1-o(1)\).  A safe isolated bite covers
only \(\Theta(1/(2^r\sqrt m))\) of the owners.  Thus a conventional
multiround nibble cannot regenerate.  Any positive theorem must preserve
whole frame classes or use a deterministic correlated factor/absorption;
owner and target resources cannot evolve as an approximately independent
residual.

## 1. Exact physical-frame census

Fix a middle owner \(X\).  For a packet to contain \(X\), choose

1. the \(r\) active endpoints in \(X\), equivalently the full core
   \(F\subset X\), in \(\binom mr\) ways;
2. the \(r\) opposite active endpoints in \([2m]\setminus X\), in
   \(\binom mr\) ways; and
3. a bijection between the two chosen \(r\)-sets, in \(r!\) ways.

This proves (0.2).

Equivalently, the total number of physical frames is

\[
 |\mathscr P_r|
 ={(2m)!\over 2^rr!(m-r)!^2}
 ={WD_r\over R},                                         \tag{1.0}
\]

the second equality being the owner--packet incidence identity.

Now fix owners \(X,Y\) at Johnson distance \(d\).  Write

\[
 A=X\setminus Y,\quad B=Y\setminus X,\quad I=X\cap Y,\quad
 C=[2m]\setminus(X\cup Y),                                \tag{1.1}
\]

so \(|A|=|B|=d\) and \(|I|=|C|=m-d\).

If one packet contains both owners, every point of \(A\) must be paired
with a point of \(B\).  There are \(d!\) such matchings.  The remaining
\(r-d\) active pairs have their commonly selected endpoints in \(I\)
and their commonly unselected endpoints in \(C\).  Choose these two
endpoint sets and match them in

\[
 \binom{m-d}{r-d}^2(r-d)!                                  \tag{1.2}
\]

ways.  The full and empty cores are then forced.  This proves (0.3).
Dividing by (0.2) and using

\[
 {\binom{m-d}{r-d}\over\binom mr}
 ={(r)_{\underline d}\over(m)_{\underline d}}             \tag{1.3}
\]

proves (0.4).

### Indexing convention

Let every physical frame be replaced by exactly \(\kappa_r\) indexed
copies.  Then

\[
 D_r^{\rm ind}=\kappa_rD_r,\qquad
 \lambda_d^{\rm ind}=\kappa_r\lambda_d,                   \tag{1.4}
\]

so (0.4) is unchanged.  The usual conventions are

\[
 \kappa_r=1\quad\text{(unordered pairs)},\qquad
 \kappa_r=r!\quad\text{(ordered pairs)},
\]

and

\[
 \kappa_r=2^rr!\quad\text{(ordered and oriented pairs)}.   \tag{1.5}
\]

In particular, the ordered-pair convention has

\[
 D_r^{\rm ord}=(m)_{\underline r}^{,2},
\]

and the ordered-and-oriented convention has

\[
 D_r^{\rm oo}=2^r(m)_{\underline r}^{,2}.                \tag{1.6}
\]

Their distance-\(d\) codegrees are obtained by multiplying (0.3) by
\(r!\) and \(2^rr!\), respectively.

The orientation in (1.5) is fixed as part of the frame, independently of
which owner incidence is later queried.  Orienting every pair toward the
queried owner would give a different incidence index for every owner and
is not one common edge catalogue.

## 2. Maximum versus aggregate owner overlap

For \(r=o(m)\), (0.4) is maximized over \(d\ge1\) at \(d=1\), and

\[
 {\lambda_1\over D_r}={r\over m^2}.                        \tag{2.1}
\]

Indeed the ratio of the \((d+1)\)-st expression in (0.4) to the
\(d\)-th is

\[
 {(d+1)(r-d)\over(m-d)^2}=o(1)                            \tag{2.2}
\]

uniformly in the possible maximizing range.

Inside one packet, the number of unordered owner pairs at Johnson
distance \(d\) is

\[
 {R\over2}\binom rd.                                      \tag{2.3}
\]

Therefore (0.4) and (2.3) give the exact second-star sum

\[
 \sum_{\{X,Y\}\subset P}\lambda_{d_J(X,Y)}
 ={RD_r\over2}\sum_{d=1}^r
 \left({(r)_{\underline d}\over(m)_{\underline d}}\right)^2. \tag{2.4}
\]

Since

\[
 {(r)_{\underline d}\over(m)_{\underline d}}
 \le\left({r\over m}\right)^d,                            \tag{2.5}
\]

the sum in (2.4) is at most

\[
 {(r/m)^2\over1-(r/m)^2}.                                 \tag{2.6}
\]

Let \(\Gamma(P)\) be the physical packets other than \(P\) which meet
\(P\) in an owner.  Applying the union bound and the first Bonferroni
inequality to the \(R\) owner stars gives

\[
\begin{aligned}
 R(D_r-1)-{RD_r\over2}
   \sum_{d=1}^r\left({(r)_{\underline d}\over(m)_{\underline d}}\right)^2
 &\le |\Gamma(P)|\\
 &\le R(D_r-1).                                           \tag{2.7}
\end{aligned}
\]

Thus, uniformly for \(r=o(m)\),

\[
 \boxed{|\Gamma(P)|=RD_r\left(1-O(r^2/m^2)-O(1/D_r)\right).} \tag{2.8}
\]

This is the geometric fact which a maximum-codegree black box discards.

For comparison, independently sample every physical packet with
probability \(a/(RD_r)\), \(0<a\le1\), and retain it only when no
owner-intersecting packet was sampled.  Equation (2.8) gives

\[
 \Pr(P\text{ retained})
 ={a\over RD_r}e^{-a+o(1)}.                               \tag{2.9}
\]

There are \(WD_r/R\) physical packets.  Hence one owner-only isolated
bite covers

\[
 \left(ae^{-a}+o(1)\right){W\over R}                      \tag{2.10}
\]

owners, a fraction \((ae^{-a}+o(1))/R\).  This calculation invokes no
fixed-uniformity matching theorem.

## 3. The exact mandatory-slot plus dump lift

Put

\[
 N_q=\binom{2m}{m-q},\qquad p_q={N_q\over W}.              \tag{3.1}
\]

For every \(q\le H\) and sign \(\epsilon\), make a slot part

\[
 \mathcal Z_q^\epsilon
 =\mathcal T_q^\epsilon\mathbin{\dot\cup}\mathcal D_q^\epsilon, \tag{3.2}
\]

where \(\mathcal T_q^\epsilon\) is the physical target rank, of size
\(N_q\), and \(\mathcal D_q^\epsilon\) is a set of
\(W-N_q\) labelled dump tokens.  Thus every slot part has size \(W\).

A local packet state consists of an oriented 2-factor on the cube packet,
return-free through depth \(H\le r\).  It has \(R\) signed trace occurrences
at each depth.  A lifted column contains

1. all \(R\) owners of the packet; and
2. at every signed depth, exactly \(R\) slot resources, one per
   occurrence: either its literal physical target, or a distinct dump
   token.

A physical target can be used at most once in one column.  Thus repeated
trace occurrences must be dumped except for at most one representative.
The column size is exactly

\[
 \boxed{K_{\rm full}=R(1+2H).}                            \tag{3.3}
\]

### Proposition 3.1 (near-perfect matching implication)

If the lifted hypergraph has a matching of \(t\) columns and

\[
 \ell=W-Rt,                                               \tag{3.4}
\]

then it leaves exactly \(\ell\) owner resources and exactly \(\ell\)
resources in every signed slot part uncovered.  In particular, it leaves
at most \(2H\ell\) physical target holes in aggregate.  Hence

\[
 \ell=o(W/H)                                              \tag{3.5}
\]

implies owner leave \(o(W/H)\) and aggregate target defect \(o(W)\).

Conversely, an owner-disjoint packet family with owner leave \(\ell\),
globally distinct accepted physical targets, and at most \(\ell\) holes
in every signed target rank can be lifted by assigning its unaccepted
occurrences injectively to dump tokens.

#### Proof

Every column uses \(R\) resources in each of the \(1+2H\) parts, proving
the first assertion.  For the converse, if a signed rank has \(h\le\ell\)
holes, the number of unaccepted occurrences is

\[
 Rt-(N_q-h)
 =(W-N_q)-(\ell-h),                                      \tag{3.6}
\]

which is at most the dump supply \(W-N_q\).  Assign distinct dump
tokens. \(\square\)

The dump labels are bookkeeping, not physical constraints.  Delete them
from every column to obtain the **mandatory projection**.  If the column
accepts \(a_q^\epsilon\) distinct targets, its projected size is

\[
 K_{\rm mand}=R+\sum_{q,\epsilon}a_q^\epsilon.            \tag{3.7}
\]

The fractional orbit is balanced by mixing

\[
 a_q^\epsilon\in\{\lfloor Rp_q\rfloor,\lceil Rp_q\rceil\}
\]

so that its mean is \(Rp_q\).  Full coordinate symmetrization and full
dump-token symmetrization then give equal fractional degree to every
owner, target slot, and dump token.  This is the exact packet analogue of
accepted occurrence plus forced surplus dumping.

For \(H=o(m^{2/3})\),

\[
 \log p_q=-q^2/m+O(q/m+q^3/m^2).                          \tag{3.8}
\]

Thus on every window \(H\ge a\sqrt m\), \(a>0\),

\[
 \sum_{q\le H}p_q=\Theta_a(\sqrt m),                      \tag{3.9}
\]

and because \(R=2^r\gg H\) when \(\log m\ll r\), every projected
column has

\[
 \boxed{K_{\rm mand}=\Theta_a(R\sqrt m).}                 \tag{3.10}
\]

## 4. Mandatory target codegree

Assume a packet state has a return-free depth-\(q\) trace.  That trace
fixes one endpoint on \(r-q\) active pairs and leaves the other \(q\)
active choices free.  Consequently exactly \(2^q\) owners of the packet
contain a lower trace, and exactly \(2^q\) packet owners lie inside an
upper trace.

### Theorem 4.1 (exact containment codegree)

At an exactly regular coordinate-orbit point of degree \(D\), for every
incident physical pair \(T\subset X\) at lower depth \(q\),

\[
 \boxed{{d(T,X)\over D}={2^q\over\binom{m+q}q}.}           \tag{4.1}
\]

The same formula holds for \(X\subset U\) at upper depth \(q\).
Without the exact degree balancing, the invariant formula has the target
degree in the denominator:

\[
 {d(T,X)\over D_T}={2^q\over\binom{m+q}q}.                \tag{4.1a}
\]

#### Proof

Every column containing the mandatory target \(T\) contains exactly
\(2^q\) packet owners which contain \(T\).  Hence

\[
 \sum_{X\supset T}d(T,X)=2^qD_T.                          \tag{4.2}
\]

There are \(\binom{m+q}q\) middle supersets of \(T\), and the full
coordinate group is transitive on the incident pairs.  This proves
(4.1a); at the regular augmented point \(D_T=D\), giving (4.1).
Complementation proves the upper formula. \(\square\)

At \(q=1\), (4.1) is (0.7).  Combining it with (3.10) gives

\[
 K_{\rm mand}{\Delta_2\over D}
 \ge\Theta_a(R\sqrt m){2\over m+1}
 =\Theta_a\left({2^r\over\sqrt m}\right).                 \tag{4.3}
\]

This is much larger than the owner-only maximum
\(r/m^2\).  It is forced by literal endpoint ownership and survives all
frame mixing.

## 5. A self-contained bite rate

Consider an exactly \(D\)-regular, \(K\)-uniform version of the mandatory
projection; the floor/ceiling edge-size difference \(O(H)\) is negligible
in (3.10), or can be handled using the maximum size.

Select every column independently with probability

\[
 p={1\over KD}                                             \tag{5.1}
\]

and retain a selected column precisely when no resource-intersecting
column was selected.  Every column has at most \(K(D-1)\) conflict
neighbors.  Therefore

\[
 \Pr(E\text{ retained})
 \ge {1\over KD}\left(1-{1\over KD}\right)^{K(D-1)}
 ={e^{-1}+o(1)\over KD}.                                  \tag{5.2}
\]

Owner-column incidence counting gives \(|\mathscr E|R=WD\).  Hence some
outcome covers at least

\[
 {e^{-1}+o(1)\over K}W                                   \tag{5.3}
\]

owners.  Conversely, before conflict deletion the experiment (5.1)
covers only \(W/K\) owners in expectation.  Thus this safe isolated-bite
scheme has the exact scale

\[
 \boxed{\Theta(1/K_{\rm mand})
 =\Theta_a(1/(2^r\sqrt m))}                               \tag{5.4}
\]

per round.  An ideal trajectory would require
\(\Theta(2^r\sqrt m\log H)\) regenerated rounds to reach owner density
\(1/H\).

## 6. Hereditary product regeneration is impossible

The number of possible physical projected columns is far too small to
survive such a trajectory under product-like thinning.

Fix an owner \(X\).  There are \(D_r\) physical frames through \(X\).  On
one cube packet, an oriented 2-factor is specified by choosing one of at
most \(r\) outgoing cube neighbors at each of the \(R\) owners; hence
there are at most

\[
 r^R                                                       \tag{6.1}
\]

local states.  This upper bound permits nonbijective choices and is
therefore valid for every legal 2-factor or Hamilton subclass.

For the quota marks, the standard binomial entropy bound and (3.8) give

\[
 \sum_{q\le H}h_2(p_q)=O(\sqrt m),                        \tag{6.2}
\]

where \(h_2(x)=-x\log x-(1-x)\log(1-x)\).  Allowing both adjacent
integer quota sizes at every signed depth therefore contributes at most

\[
 \exp\{O(R\sqrt m+H\log R)\}                              \tag{6.3}
\]

markings.  Combining (0.2), (6.1), and (6.3), and using
\(\log m\ll r=o(m)\), gives the upper bound

\[
 \boxed{\log D_{\rm phys}(X)=O(R\sqrt m)}                 \tag{6.4}
\]

for the number of distinct mandatory projected columns through \(X\).
Indeed \(\log D_r=O(r\log m)\), \(R\log r=o(R\sqrt m)\), and
\(H\log R=o(R\sqrt m)\) in the Gaussian range.

### Theorem 6.1 (packet-link death)

Retain every owner and mandatory target independently with probability
\(\varepsilon=m^{-\alpha}\), where \(\alpha>0\) is fixed, and condition
on retaining \(X\).  Then the expected number of projected physical
columns through \(X\) whose other resources all survive is

\[
 \boxed{o(1).}                                            \tag{6.5}
\]

#### Proof

Every projected column contains at least
\(c_aR\sqrt m\) resources by (3.9)--(3.10).  Equations (6.4) and
independent survival give

\[
\begin{aligned}
 \log\mathbb E[d_{\rm res}(X)\mid X\text{ retained}]
 &\le O(R\sqrt m)
   -(c_aR\sqrt m-1)\alpha\log m\\
 &=-\Omega_a(R\sqrt m\log m).
\end{aligned}                                             \tag{6.6}
\]

This tends to \(-\infty\). \(\square\)

Labelled dump assignments may give one projected column many formal
lifts, but they cannot create a surviving physical core when none exists.
Thus dump-token multiplicity does not repair (6.5).

The exact owner-only packet factor from a fixed pair frame is consistent
with this theorem: it is a deterministic, perfectly correlated
partition, not a product-residual nibble.  Theorem 6.1 says that this same
kind of correlation is indispensable after target slots are added.

## 7. Exact conclusion boundary

The following are proved.

1. The physical and indexed packet degrees and codegrees are exactly
   (0.2)--(0.4), including all indexing factors.
2. Owner-star overlaps aggregate to only \(O(r^2/m^2)\), despite maximum
   normalized owner codegree \(r/m^2\).
3. The mandatory-target plus dump lift converts an
   \(o(W/H)\)-leave matching into aggregate \(o(W)\) target defect.
4. Literal target ownership forces the exact containment codegree (4.1).
5. For \(\log m\ll r=o(m)\), the augmented mandatory projection is far
   outside every \(K\Delta_2/D=o(1)\) regime.
6. A self-contained isolated bite has rate only
   \(\Theta(1/(2^r\sqrt m))\), and polynomial-density product residuals
   have empty links.

The following are not proved.

1. A Hall cut against every integral packet factor.
2. Nonexistence of a correlated quota-safe fixed-frame completion.
3. A coefficient-one construction.

Thus the all-frame packet orbit has excellent fractional balance and no
owner-only projective-plane obstruction.  Its exact surviving gate is a
deterministic or strongly correlated common-frame completion which keeps
the mandatory target slots aligned while reusing the known owner packet
partition.  A generic growing-edge nibble, even on the unrestricted
frame orbit, cannot provide that completion.
