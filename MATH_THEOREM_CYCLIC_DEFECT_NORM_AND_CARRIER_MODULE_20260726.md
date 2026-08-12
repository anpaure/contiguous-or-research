# Cyclic defect norms and the smallest productive strand router

## 1. Norms on permutation lattices

Let \(\tau\) have finite order \(h\) on a finite set \(\Omega\), and put

\[
N_\tau=1+\tau+\cdots+\tau^{h-1}
\]

on the permutation lattice \(L=\mathbb Z[\Omega]\).  If \(O\) is a
\(\tau\)-orbit of length \(d_O\), write

\[
\mathbf 1_O=\sum_{x\in O}e_x.
\]

### Lemma 1.1 (integral orbit-sum formula)

For \(v=\sum_x a_xe_x\),

\[
\boxed{
N_\tau v=
\sum_O {h\over d_O}\left(\sum_{x\in O}a_x\right)\mathbf 1_O .}
\tag{1.1}
\]

Consequently,

\[
\ker N_\tau=\left\{v:\sum_{x\in O}a_x=0\text{ for every }O\right\}
=\operatorname{im}(1-\tau),
\tag{1.2}
\]

\[
L^\tau=\bigoplus_O\mathbb Z\mathbf 1_O,
\qquad
\operatorname{im}N_\tau=
\bigoplus_O {h\over d_O}\mathbb Z\mathbf 1_O.
\tag{1.3}
\]

In particular, \(N_\tau\) is multiplication by \(h\) on the invariant
submodule, and \(L^\tau\cap\ker N_\tau=0\).

#### Proof

Starting at one point of an orbit of length \(d_O\), the \(h\) powers of
\(\tau\) visit every point exactly \(h/d_O\) times.  This proves (1.1)
and all assertions except the last equality in (1.2).  On one cyclic
orbit, every integral vector with coefficient sum zero is the cyclic
difference of its integral partial-sum vector.  Taking the direct sum over
orbits proves \(\ker N_\tau=\operatorname{im}(1-\tau)\).  \(\square\)

Thus a ledger defect has zero serial norm exactly when its coefficient
sum vanishes separately on every transported ledger orbit.  Total signed
mass zero is not enough when there is more than one orbit.

### Corollary 1.2 (transported-collar normal form)

Every norm-zero defect in a permutation ledger has the form

\[
\varepsilon=(1-\tau)w
\tag{1.4}
\]

for an integral ledger preload \(w\).  Its serial copies telescope:

\[
\sum_{j=0}^{h-1}\tau^j\varepsilon
=
\sum_{j=0}^{h-1}(\tau^jw-\tau^{j+1}w)=0.
\tag{1.5}
\]

Thus the universal symbolic dirty atom is a collar that exports \(w\) at
one boundary and imports its transported copy \(\tau w\) at the other.
The hard issue is not algebraic cancellation, but realizing this collar
by actual equal-length incidence paths.

## 2. The natural two-boundary carrier module

Take the regular port cycle \(P=\mathbb Z/h\mathbb Z\), with
\(\tau i=i+1\), and let

\[
V=\mathbb Z[P\times P]
\]

with the diagonal action \(\tau(i,j)=(i+1,j+1)\).  The first coordinate
records the incoming strand and the second the outgoing strand.  Put

\[
u_r=\sum_{i\in P}e_{(i,i+r)},\qquad r\in P.
\tag{2.1}
\]

### Lemma 2.1 (cyclic diagonals)

The diagonal \(\tau\)-orbits on \(P\times P\) are the \(h\) sets

\[
O_r=\{(i,i+r):i\in P\},
\]

and hence

\[
V^\tau=\bigoplus_{r\in P}\mathbb Zu_r.
\tag{2.2}
\]

For arbitrary \(v=(v_{ij})\),

\[
N_\tau v=
\sum_{r\in P}\left(\sum_i v_{i,i+r}\right)u_r.
\tag{2.3}
\]

Let \(\rho,\kappa:V\to\mathbb Z[P]\) be the row and column marginal
maps.  Then

\[
V^\tau\cap\ker\rho\cap\ker\kappa
=
\left\{\sum_r a_ru_r:\sum_r a_r=0\right\},
\tag{2.4}
\]

a free lattice of rank \(h-1\).  The norm is multiplication by \(h\)
on this whole sublattice.

#### Proof

The difference \(j-i\) is the complete invariant of the diagonal action,
which proves (2.2); (2.3) is Lemma 1.1.  Both marginals of \(u_r\) equal
\(\mathbf 1_P\), so a linear combination has zero marginals exactly when
its coefficients sum to zero.  \(\square\)

The fundamental invariant carrier direction is

\[
\boxed{\delta_h=u_1-u_0.}
\tag{2.5}
\]

It has zero incoming and outgoing marginals, is nonzero and
\(\tau\)-invariant, and therefore

\[
\boxed{N_\tau\delta_h=h\delta_h\ne0.}
\tag{2.6}
\]

This identifies where productive carrier information can live: not in
either one-sided port ledger, but in the correlation between the two
boundaries.

### Corollary 2.2 (one-sided carrier obstruction)

Every separable carrier score

\[
w(i,j)=\alpha(i)+\beta(j)
\]

annihilates \(\delta_h\).  More generally, any carrier chart that factors
through \((\rho,\kappa)\) kills every invariant balanced direction in
(2.4).  A productive strand router must therefore retain a genuinely
two-sided or crossing-boundary carrier coordinate.

## 3. Alternating \(C_{2h}\) splices realize the invariant direction

Let the two shores be

\[
Y=\{y_i:i\in P\},\qquad Z=\{z_i:i\in P\}.
\]

Consider the old and new perfect matchings

\[
M_0=\{y_iz_i:i\in P\},
\qquad
M_1=\{y_iz_{i+1}:i\in P\}.
\tag{3.1}
\]

Their union is an alternating \(C_{2h}\), and its signed switch vector is

\[
\gamma_h=\sum_i([y_iz_{i+1}]-[y_iz_i]).
\tag{3.2}
\]

Let \(\partial\) be the unsigned vertex-incidence ledger map.

### Theorem 3.1 (clean cyclic router)

The switch (3.2) satisfies

\[
\partial\gamma_h=0,
\qquad
\tau\gamma_h=\gamma_h.
\tag{3.3}
\]

It sends the suffix formerly owned by strand \(i\) to strand \(i-1\),
so its endpoint monodromy is an \(h\)-cycle (up to orientation).  Under
the boundary-pair carrier map

\[
[y_iz_j]\longmapsto e_{(i,j)},
\]

its carrier increment is \(\delta_h\).  Thus the local ledger defect is
zero while the carrier norm is \(h\delta_h\ne0\).

If \(h\) coherent copies are placed serially on the same transported port
label, the endpoint monodromy closes, every local incidence ledger remains
exact, and any occurrence-additive carrier retaining the local boundary
pair directions adds to \(h\delta_h\).

#### Proof

Every \(y_i\) and every \(z_i\) occurs once in each matching, proving
\(\partial\gamma_h=0\).  Rotation of all indices fixes the two matching
sums separately.  The reconnection and carrier claims follow directly
from (3.1).  The serial statement is the norm formula.  \(\square\)

The locality qualification is essential.  If the carrier records only the
single global start-to-final endpoint pairing, then after \(h\) routers it
sees \(\tau^h=1\) and hence zero change.  The productive module above is
the direct sum of slab-local crossing records (or a physical protected
target chart that is additive over those records), not the final endpoint
permutation itself.

This is an incidence-level symbolic family with

\[
N_\tau\varepsilon=0,\qquad N_\tau\delta\ne0,
\]

indeed with \(\varepsilon=0\).  Therefore there is no general
incidence-conservation obstruction to a productive finite-order twist.
The remaining issue is physical: synchronized equal-length occurrences,
switch stability, exterior transport, and a carrier chart that retains the
two-boundary correlation.

### Proposition 3.2 (smallest Boolean-incidence instance is \(C_6\))

Let \(K\) be an \((r-1)\)-set and let \(a_0,\ldots,a_{h-1}\) be distinct.
Set

\[
z_i=K\cup\{a_i\},
\qquad
y_i=K\cup\{a_i,a_{i+1}\}.
\tag{3.4}
\]

Then (3.1) is an alternating \(C_{2h}\) in the inclusion graph between
rank \(r\) and rank \(r+1\).  The construction works for every \(h\ge3\).
There is no \(C_4\) in this inclusion graph, because two distinct
\(r\)-sets have at most one common \((r+1)\)-superset.  Hence \(h=3\),
the common-core \(C_6\), is the smallest Boolean-incidence router.

In particular, three synchronized common-core \(C_6\) routers are the
smallest abstract serial conveyor: their order-three port twist closes
and their correlation carrier equals \(3(u_1-u_0)\).

### Theorem 3.3 (a genuine fixed-rank Boolean target carrier)

The abstract two-boundary carrier can be realized by a literal lower-shadow
target.  Fix \(h\ge3\) and \(r\ge h+2\), and let \(|J|=2r\).  Choose

\[
K\in\binom J{r-1},qquad
k,t_0,\ldots,t_{h-1}\in K
\]

all distinct, and choose distinct

\[
a_0,\ldots,a_{h-1},b\in J\setminus K.
\]

Indices below are modulo \(h\).  Define

\[
\begin{aligned}
X_i&=K\cup\{a_i\},\\
Y_i&=K\cup\{a_i,a_{i+1}\},\\
Z_i&=(K\setminus\{k\})\cup\{a_i,a_{i+1}\},\\
V_i&=(K\setminus\{k\})\cup\{a_i,a_{i+1},b\},\\
W_i&=(K\setminus\{k,t_i\})\cup\{a_i,a_{i+1},b\}.
\end{aligned}
\tag{3.5}
\]

Then

\[
P_i^-:X_i-Y_i-Z_i-V_i-W_i
\tag{3.6}
\]

are \(h\) vertex-disjoint equal-length inclusion paths.  Toggling the
clean common-core cycle replaces them by

\[
P_{i+1}^+:X_{i+1}-Y_i-Z_i-V_i-W_i.
\tag{3.7}
\]

The two packets have exactly the same lower and upper vertex ledgers, and
the endpoint operation is an \(h\)-cycle.

For a two-step path with lower states \(Q_0,Q_1,Q_2\), define its depth-two
target by

\[
\Theta(Q_0,Q_1,Q_2)=Q_0\cap Q_1\cap Q_2
\in\binom J{r-2}.
\tag{3.8}
\]

The signed target increment of (3.6)--(3.7) is

\[
\boxed{
\delta=
\sum_i
\left(
e_{(K\setminus\{k,t_i\})\cup\{a_{i+1}\}}
-e_{(K\setminus\{k,t_i\})\cup\{a_i\}}
\right).}
\tag{3.9}
\]

It is nonzero.  Moreover, the coordinate permutation

\[
\rho:a_i\mapsto a_{i+1},qquad t_i\mapsto t_{i+1},
\tag{3.10}
\]

fixing all other chosen coordinates, satisfies \(\rho\delta=\delta\).
Use \(\rho\) as the physical target action induced by the endpoint
\(h\)-cycle \(\tau\).  Consequently \(h\) coherently transported copies
have

\[
N_\tau\varepsilon=N_\rho\varepsilon=0,
\qquad
N_\tau\delta=N_\rho\delta=h\delta\ne0,
\tag{3.11}
\]

where \(\varepsilon=0\) is the exact X/Y ledger defect.

#### Proof

The cardinalities in (3.5) alternate between \(r\) and \(r+1\), and
every displayed adjacency is containment.  Distinct indices give distinct
vertices: the \(a_i,a_{i+1}\) pair distinguishes the middle states, while
the presence or absence of \(k,b,t_i\) distinguishes the five displayed
types.  Thus (3.6) is a disjoint path packet.

The selected edges \(X_iY_i\) and replacement edges \(Y_iX_{i+1}\)
form the common-core alternating \(C_{2h}\).  The toggle changes no vertex
ledger and preserves the two-upper-state length of every path, proving the
first assertions.

Since \(Z_i\cap W_i=(K\setminus\{k,t_i\})\cup
\{a_i,a_{i+1}\}\), the old and new targets are respectively

\[
(K\setminus\{k,t_i\})\cup\{a_i\},
\qquad
(K\setminus\{k,t_i\})\cup\{a_{i+1}\},
\]

which proves (3.9).  A positive target with index \(i\) cannot equal a
negative target with index \(j\): equality of the unique elements outside
\(K\) would force \(j=i+1\), while equality inside \(K\) would then force
\(t_i=t_{i+1}\), contrary to the choice of the \(t_i\).  Hence
\(\delta\ne0\).  Finally, \(\rho\) cyclically permutes the positive terms
and the negative terms separately, proving (3.10)--(3.11). \(\square\)

This removes the caveat that the productive carrier in Theorem 3.1 might
be merely a formal crossing record.  Already at the second lower shadow,
literal Boolean incidence admits an exact-ledger finite-order router with
nonzero invariant target norm.  What remains is an ambient atlas and exact
collar construction placing these packets at positive density.

### Corollary 3.4 (dirty transported-collar extension)

Suppose the packet of Theorem 3.3 is equipped with a literal input/output
collar whose incoming preload is \(w\) and whose outgoing preload is its
transport \(\tau w\).  When the two collar shores are recorded separately,
one slab has nonzero signed defect

\[
\varepsilon=(1-\tau)w.
\tag{3.12}
\]

The internal target increment is still \(\delta\).  Therefore \(h\)
coherently glued copies satisfy

\[
N_\tau\varepsilon=0,
\qquad
N_\tau\delta=h\delta\ne0.
\tag{3.13}
\]

Thus a dirty productive family is automatic once the transported collar
is physically realized.  This corollary is conditional on literal seam
ownership: writing down \((1-\tau)w\) does not itself construct the collar.

## 4. The exact module criterion for a dirty atom

Let \(S\) be a torsion-free \(\tau\)-lattice of local switch data, and let

\[
B:S\to L,\qquad C:S\to V
\]

be equivariant ledger and carrier maps.  For one local atom \(s\), put

\[
\varepsilon=Bs,\qquad \delta=Cs.
\]

### Theorem 4.1 (invariant-cycle criterion)

One has

\[
N_\tau\varepsilon=B(N_\tau s),
\qquad
N_\tau\delta=C(N_\tau s).
\tag{4.1}
\]

Hence the serial atom is ledger-exact and productive precisely when

\[
\boxed{N_\tau s\in\ker B\setminus\ker C.}
\tag{4.2}
\]

The vector \(N_\tau s\) is invariant.  Therefore a general obstruction is

\[
\ker(B|_{S^\tau})\subseteq\ker(C|_{S^\tau});
\tag{4.3}
\]

under (4.3) no dirty serial atom can work.  In particular, if the carrier
is an equivariant linear function of the ledger defect, \(C=T B\), then
\(N_\tau\varepsilon=0\) forces \(N_\tau\delta=0\).

Conversely, an invariant exact switch \(s\in S^\tau\cap\ker B\) with
\(Cs\ne0\) is automatically productive, because
\(N_\tau s=hs\).  The alternating-cycle vector \(\gamma_h\) is exactly
such an invariant cycle.

#### Proof

Equivariance lets \(B\) and \(C\) commute with every power of \(\tau\),
giving (4.1).  All remaining statements follow immediately.  \(\square\)

This theorem isolates the physical question.  The incidence ledger sees
only \(B\); a successful carrier must detect an invariant part of the
cycle space forgotten by \(B\).

## 5. The D3 four-token defect and its minimal order-three extension

Write the formal D3 splice defect as

\[
\varepsilon=e_A+e_B-e_C-e_D,
\tag{5.1}
\]

where

\[
A=1345,\quad B=2346,\quad C=1245,\quad D=2356.
\]

An order-three permutation on the four displayed coordinates cannot kill
this defect: its orbits have lengths one or three, every fixed coordinate
must have coefficient zero in a norm-zero vector, and a three-orbit cannot
contain two \(+1\) and two \(-1\) coordinates.

### Lemma 5.1 (minimal neutral padding)

Suppose an order-three permutation action transports the four distinct
nonzero coefficients in (5.1), without combining coefficients.  Then an
ambient set of at least six ledger coordinates is necessary for
\(N_\tau\varepsilon=0\), and six is sufficient.

Indeed, introduce two coordinates \(U,V\), initially of coefficient zero,
and take

\[
\tau_L=(A\ C\ U)(B\ D\ V).
\tag{5.2}
\]

Each orbit has coefficient pattern \((1,-1,0)\), so

\[
\boxed{N_{\tau_L}\varepsilon=0.}
\tag{5.3}
\]

#### Proof

Every active order-three orbit has length three and must contain both
signs.  One orbit can contain at most one of the two positive-negative
pairs, because the four active coordinates do not fit in three positions.
Thus two three-orbits, hence six ambient coordinates, are necessary.
Construction (5.2) proves sufficiency.  \(\square\)

In fact (5.2) puts the explicit defect directly in transported-collar
normal form:

\[
\varepsilon
=(1-\tau_L)(e_A+e_B).
\tag{5.4}
\]

Couple (5.2) to the order-three endpoint representation on
\(P=\mathbb Z/3\mathbb Z\) and choose the carrier direction

\[
\delta=u_1-u_0.
\]

Then

\[
N_\tau\varepsilon=0,
\qquad
N_\tau\delta=3\delta\ne0.
\tag{5.5}
\]

This is a complete module-level order-three solution for the explicit D3
defect.  It is not yet a physical lift of the D3 pentagon: a real context
must realize the two neutral ledger coordinates and the action (5.2) by
actual equal-length incidence paths.

For comparison, an order-four action can kill the same four-token defect
without padding: place \(A,B,C,D\) in one four-cycle.  Its orbit coefficient
sum is zero.  Thus an appropriately transported \(C_8\) context is
ledger-economical, although it is not the order-three monodromy of the
existing D3 mixed splice.

## 6. Exact verdict

The cyclic norm problem itself is completely transparent:

1. ledger cancellation is orbitwise augmentation-zero;
2. productive carriers live in an invariant correlation submodule;
3. clean alternating \(C_{2h}\) switches already realize the required
   separation, with the Boolean minimum \(h=3\);
4. any one-sided or ledger-factored carrier is rigorously invisible;
5. the existing D3 defect needs two neutral ledger coordinates for an
   order-three cancellation action, or a different order-four context.

Accordingly, the next construction target is not another abstract norm
identity.  It is a synchronized physical common-core \(C_6\) conveyor (or
a six-coordinate realization of (5.2)) whose protected target chart
retains the two-boundary correlation \(u_1-u_0\) through serial gluing.
