# Multiframe recursive rotors: exact integral coupling and Hall gates

Date: 2026-07-25

This note uses only the recursive half-depth-rainbow factor proved in
`ROTOR_SCD_PARITY_CHECK_CYCLE_TILING_20260725.md`.  It does not assert the
coefficient-one theorem.

## 0. Verdict

Let

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 H=\lceil A\sqrt m\rceil .
\]

Choose a power of two \(\ell\) with

\[
 2H\leq \ell\leq m.
\]

For the low-toll application require in addition \(H=o(\ell)\); the
largest power of two not exceeding \(m\) has this property for fixed
\(A\).  Allow every perfect pairing of the \(2m\) coordinates, every
choice of \(\ell\) active split pairs, every endpoint orientation, and
every coordinate conjugate of the recursive permutation \(F_\ell\).

Three exact facts result.

1. **Column universality.**  Every saturated symmetric chain segment of
   radius at most \(H\), centred at an arbitrary middle set, is one of the
   chain columns carried by this multiframe library.  Hence there is no
   integrality or SCD-existence obstruction after singleton packets are
   allowed.
2. **Exact packet matching.**  A band SCD whose rotor components are
   intervals of recursive cycles is exactly a perfect matching in a finite
   hypergraph of integral constant-radius packets.  Its literal toll is
   exactly the weight of that matching.  This is an integer exact-cover
   problem, not a fractional surrogate.
3. **Exact Hall recursion.**  At one outward SCD-extension step, prescribing
   which current chains continue is feasible if and only if two explicit
   bipartite Hall systems hold, one below and one above.  Thus the remaining
   cross-stratum problem can be stated as choosing nested continuation sets
   which obey these Hall cuts and simultaneously split into long recursive
   rotor intervals.

One fixed coordinate pairing fails these cuts at the Gaussian census
level.  Allowing all pair frames removes every *one-rank* Hall obstruction:
the projected target--owner graph is the complete Boolean inclusion graph.
The unresolved obstruction is therefore joint: exact ownership at all
depths must be correlated with long same-cycle chronology.

The newest entropy/discrepancy notes correctly stop at this point.  Their
orbit measure is an exact fractional solution, but no stated entropy,
independent-rounding, or discrepancy theorem produces either the packet
perfect matching below or the weaker integral `MFUP_A` cover.

## 1. Recursive occurrences and their chain columns

Let \({\cal P}\) be a perfect matching between the elements of a middle set
\(X\) and those of its complement.  Thus every pair of \({\cal P}\) is
split by \(X\).  Choose \(\ell\) of these pairs and hold the orientations
of the remaining pairs fixed.  The resulting fibre is an orientation cube
\(Q_\ell\).

On that fibre use a coordinate conjugate of \(F_\ell\).  Write one of its
cycles as

\[
 C=(X_0,X_1,\ldots,X_{2\ell-1})
\]

with cyclic indices.  For \(0\le q\le H\), put

\[
 L_q(C,j)=\bigcap_{i=0}^{q}X_{j+i},\qquad
 U_q(C,j)=\bigcup_{i=0}^{q}X_{j-i}.
 \tag{1.1}
\]

Every \(q\le H\le\ell/2\) successive transitions use distinct pair
coordinates.  Consequently

\[
 |L_q(C,j)|=m-q,\qquad |U_q(C,j)|=m+q,
 \tag{1.2}
\]

and, for \(d\le H\),

\[
 K(C,j,d):quad
 L_d\subset\cdots\subset L_1\subset X_j
 \subset U_1\subset\cdots\subset U_d
 \tag{1.3}
\]

is a saturated symmetric chain segment.  The forward and reverse
injectivity in the recursive factor implies that, for fixed \(q\), the
maps \(j\mapsto L_q(C,j)\) and \(j\mapsto U_q(C,j)\), over the entire
orientation fibre, are injective.

### Lemma 1.1 (up-set path hitting)

For \(T\in\binom{[2m]}{m-q}\), let

\[
 {\cal U}_T=\{Y\in\tbinom{[2m]}m:T\subseteq Y\}.
\]

Then

\[
 L_q(C,j)=T
 \quad\Longleftrightarrow\quad
 X_j,X_{j+1},\ldots,X_{j+q}\in{\cal U}_T.
 \tag{1.4}
\]

#### Proof

The forward implication is immediate.  Conversely, the right side gives
\(T\subseteq\bigcap_{i=0}^qX_{j+i}\), while (1.2) says that the latter
intersection has the same size as \(T\).  Hence they are equal. \(\square\)

The upper statement is the complementary copy in even dimension.  In the
odd wreath normalization, upper depth \(q\) is instead complementary to
lower depth \(q-1\); the shift cannot be dropped.

## 2. Every individual SCD column is available

### Theorem 2.1 (multiframe column universality)

Let

\[
 A_{-d}\subset A_{-d+1}\subset\cdots\subset A_0=X
 \subset\cdots\subset A_d
 \tag{2.1}
\]

be any saturated symmetric chain segment in \(B_{2m}\), with
\(d\le H\).  There is a recursive occurrence \((C,j)\) in the multiframe
library for which

\[
 K(C,j,d)=(A_{-d},\ldots,A_d).
 \tag{2.2}
\]

#### Proof

Write uniquely

\[
 A_{-q}=X\setminus\{a_1,\ldots,a_q\},\qquad
 A_q=X\cup\{b_1,\ldots,b_q\}
 \quad(1\le q\le d).
 \tag{2.3}
\]

The \(a_i\)'s are distinct elements of \(X\), and the \(b_i\)'s are
distinct elements of \(X^c\).  Since \(2d\le2H\le\ell\le m\), choose
distinct

\[
 c_1,\ldots,c_d\in X^c\setminus\{b_1,\ldots,b_d\},
 \qquad
 a'_1,\ldots,a'_d\in X\setminus\{a_1,\ldots,a_d\}.
\]

Use the \(2d\) disjoint pairs

\[
 P_i=\{a_i,c_i\},\qquad Q_i=\{a'_i,b_i\}
 \quad(1\le i\le d),
\]

and extend them to a perfect matching between \(X\) and \(X^c\).  Choose
\(\ell-2d\) further pairs as active.

At any vertex of an \(F_\ell\)-cycle, the next \(\ell\) transition
directions form one cyclic permutation of the active coordinates.  Relabel
the active directions so that the next \(d\) directions are
\(P_1,\ldots,P_d\), while the preceding directions, read backwards from
the vertex, are \(Q_1,\ldots,Q_d\).  The two blocks are disjoint because
\(2d\le\ell\).  Choose endpoint names in every active pair so that this
vertex represents \(X\).

The forward intersection deletes \(a_1,\ldots,a_q\).  The reverse union
adds \(b_1,\ldots,b_q\).  Hence its lower and upper members are exactly
the two sets in (2.3), proving (2.2). \(\square\)

### Corollary 2.2 (integral feasibility without a toll bound)

The multiframe chain-column exact-cover system has an integral solution.

#### Proof

Take any full Boolean SCD and clip it at depth \(H\).  Apply Theorem 2.1
independently to each clipped chain.  The resulting singleton recursive
packets partition every mask in the band exactly once. \(\square\)

This is important logically.  The remaining problem is not whether the
fractional orbit point belongs to an integer-free affine space.  Integer
solutions exist.  What is missing is an integer solution concentrated on
long packets, rather than on \(W\) singleton packets.

## 3. The exact radius-packet matching

Let

\[
 {\cal B}_H=\bigcup_{q=-H}^{H}\binom{[2m]}{m+q}
\]

be the central band.  A **recursive packet** is a triple
\(P=(C,I,d)\), where \(C\) is a recursive cycle in an arbitrary frame,
\(I\) is a nonempty directed cyclic interval of its centres (with a marked
cut when \(I=C\)), and \(0\le d\le H\).  Its mask support is

\[
 E(P)=\bigcup_{j\in I}K(C,j,d).
 \tag{3.1}
\]

By the two-sided injectivity of \(F_\ell\), this union is disjoint: it is a
partial SCD consisting of \(|I|\) radius-\(d\) chains.

Let \({\cal H}_{m,H,\ell}\) be the hypergraph with vertex set
\({\cal B}_H\) and one edge \(E(P)\) for every recursive packet.  Give that
edge cost

\[
 w(P)=2d+1
 \tag{3.2}
\]

for the conservative literal-word ledger (or \(2d\) for the exact useful-
prefix toll).

### Theorem 3.1 (packet-matching equivalence)

The following objects are equivalent.

1. A saturated band SCD whose same-radius rotor path components are
   directed intervals of recursive cycles from arbitrary pair frames.
2. A perfect matching \({\cal M}\) of \({\cal H}_{m,H,\ell}\).

Under the equivalence, the conservative central-band word length is

\[
 \boxed{W+\sum_{P\in{\cal M}}w(P).}
 \tag{3.3}
\]

#### Proof

A hypergraph perfect matching partitions the band into the partial SCDs
in (3.1), hence into one saturated band SCD.  Every packet is one genuine
directed rotor path after its marked cut.  Conversely, decompose every
radius class of the stated SCD into its maximal recursive-cycle path
components; their mask supports are disjoint packet edges covering the
band.

A radius-\(d\) component on \(t\) centres has literal length
\(t+2d+1\).  Summing the \(t\)'s gives \(W\), and every component adds
exactly (3.2).  This proves (3.3). \(\square\)

In variables, the exact problem is

\[
 \min\sum_Pw(P)x_P,
 \qquad
 \sum_{P:S\in E(P)}x_P=1\quad(S\in{\cal B}_H),
 \qquad x_P\in\{0,1\}.
 \tag{3.4}
\]

The radius census is automatic.  If \(n_d\) is the number of selected
centres of exact radius \(d\), then rank \(m-q\) gives

\[
 \sum_{d=q}^Hn_d=N_q.
\]

Thus

\[
 n_d=N_d-N_{d+1}\ (d<H),\qquad n_H=N_H.
 \tag{3.5}
\]

The desired rotor statement in this library is precisely that the optimum
in (3.4) is \(o_A(W)\) for every fixed \(A\).

Whole \(2\ell\)-cycles alone need not satisfy (3.5): they force the
congruences \(2\ell\mid n_d\).  These fail infinitely often.  Allowing
marked intervals or correction chains removes that scalar obstruction at
only polynomial census cost, but does not solve (3.4).

## 4. The exact one-layer Hall flow

The standard SCD extension theorem admits a useful prescribed-continuation
form.

Suppose \({\cal D}_q\) is a saturated SCD of the band from ranks
\(m-q\) through \(m+q\).  Let \(Y_q\) be its chains which meet both
boundary ranks.  For \(y\in Y_q\), write its lower and upper endpoints as

\[
 A_y\in\binom{[2m]}{m-q},\qquad
 B_y\in\binom{[2m]}{m+q}.
\]

Fix a proposed continuation set \(C\subseteq Y_q\).  Define

\[
 X_q=\binom{[2m]}{m-q-1},\qquad
 Z_q=\binom{[2m]}{m+q+1},
\]

and the two bipartite graphs

\[
 x\sim_-y\iff x\subset A_y
 \quad(x\in X_q,y\in C),
 \tag{4.1}
\]

\[
 y\sim_+z\iff B_y\subset z
 \quad(y\in C,z\in Z_q).
 \tag{4.2}
\]

### Theorem 4.1 (prescribed-continuation Hall theorem)

There is an integral symmetric extension of \({\cal D}_q\) by one rank on
each side which continues exactly the chains in \(C\) if and only if

\[
 |C|=|X_q|=|Z_q|=N_{q+1}
 \tag{4.3}
\]

and both graphs (4.1)--(4.2) have perfect matchings.  Equivalently, the
following Hall inequalities hold:

\[
 |\Gamma_-(S)|\ge |S|\quad(S\subseteq X_q),
 \tag{4.4}
\]

\[
 |\Gamma_+(T)|\ge |T|\quad(T\subseteq C).
 \tag{4.5}
\]

#### Proof

If the extension exists, every new lower set is attached to one continued
chain and every continued chain receives one new lower set, giving a
perfect matching in (4.1).  The upper attachments give a perfect matching
in (4.2).

Conversely, choose the two perfect matchings.  For every \(y\in C\), append
its matched lower set below \(A_y\) and its matched upper set above
\(B_y\).  Stop every chain outside \(C\).  All new outer masks are used
once, every extension is saturated, and symmetry is preserved. \(\square\)

Iterating Theorem 4.1 gives an exact integral flow description of all band
SCDs.  The rotor problem asks for the continuation sets to have much more
structure: if

\[
 R_d=Y_d\setminus Y_{d+1}
 \]

is the exact-radius class, then \(R_d\) must split into few recursive-cycle
intervals, and the vertical matchings selected in (4.1)--(4.2) must agree
with the chain flags of those intervals.  The sum of the interval costs is
the objective in (3.4).

Thus an exact Hall form of the remaining theorem is:

> choose nested continuation sets \(Y_{q+1}\subseteq Y_q\), satisfying
> (4.3)--(4.5) at every depth, together with their integral attachment
> matchings, so that each stopped class is supported by recursive-cycle
> intervals from owner-dependent pair frames and their total weighted
> number is \(o(W)\).

The Hall conditions are necessary and sufficient for SCD membership.  The
recursive-interval condition is the independent chronology constraint.

### Corollary 4.2 (uniform integral common-base multicover)

For every fixed band SCD \({\cal D}_q\), the family of continuation sets
which satisfy Theorem 4.1 has an exact rational distribution with uniform
marginal

\[
 \Pr(y\in C)={m-q\over m+q+1}
 ={N_{q+1}\over N_q}
 \qquad(y\in Y_q).
 \tag{4.6}
\]

Equivalently, after one common integer scaling there is an integral
multiset of Hall-feasible continuation sets in which every current chain is
continued the same number of times.

#### Proof

Use the square auxiliary bipartite graph with sides

\[
 X_q\mathbin{\dot\cup}Y_q^-
 \quad\hbox{and}\quad
 Z_q\mathbin{\dot\cup}Y_q^+.
\]

Give every comparison edge in (4.1)--(4.2) weight
\(1/(m+q+1)\), and give every identity edge
\(y^-y^+\) weight

\[
 1-{m-q\over m+q+1}.
\]

Every row and column sum is one.  Decompose this rational doubly stochastic
point into integral perfect matchings.  A perfect matching continues \(y\)
exactly when it does not use its identity edge.  The total comparison
weight at \(y\) is \((m-q)/(m+q+1)\), proving (4.6).  Clearing the
denominators gives the integral multicover. \(\square\)

Thus even the *simultaneous lower/upper* Hall system has exact integral
balanced marginals.  What this decomposition does not control is the joint
probability that consecutive recursive-cycle owners continue together.
Independent or negatively correlated choices create a boundary at positive
density.  Coefficient one needs a decomposition with strong positive
correlation along long recursive intervals.

This missing implication is false for abstract common-base systems.  On
the cyclically ordered ground set \(Y=\{1,\ldots,2r\}\), let the first
partition matroid require one element from each pair

\[
 \{1,2\},\{3,4\},\ldots,\{2r-1,2r\},
\]

and let the second require one element from each shifted pair

\[
 \{2,3\},\{4,5\},\ldots,\{2r,1\}.
\]

The only common bases are the odd and the even elements.  Their uniform
mixture has marginal \(1/2\) at every element, but either base has all
\(2r\) cyclic edges crossing its boundary.  Partition matroids are
transversal matroids.  Hence uniform integral common-base marginals, by
themselves, contain no low-boundary theorem; any proof must use additional
Boolean/rotor structure.

### Corollary 4.3 (exact full-SCD radius multicover)

There is a finite rational distribution on genuine full Boolean SCDs such
that, for every middle owner \(X\) and every \(q\),

\[
 \Pr\{\text{the chain of }X\text{ has radius at least }q\}
 ={N_q\over W}.
 \tag{4.7}
\]

After clearing denominators, this is an exact integral multiset of SCDs in
which every middle owner occurs in every radius class with the forced
uniform frequency.

#### Proof

Begin with the singleton decomposition of the middle rank.  At each outward
extension step, conditionally on the current partial SCD, use any rational
distribution from Corollary 4.2.  Its continuation probability

\[
 p_i={N_{i+1}\over N_i}
\]

is the same for every currently active chain and for every partial SCD.
Therefore a fixed middle owner survives through depth \(q\) with
probability

\[
 \prod_{i=0}^{q-1}p_i={N_q\over W}.
\]

There are finitely many choices and all probabilities are rational.  Clear
their common denominator. \(\square\)

This completely removes radius quotas, full-SCD integrality, and vertical
Hall feasibility as separate obstructions.  It still supplies no one SCD
whose equal-radius owners have few recursive-rotor runs.

## 4.4 An exact two-resolution multicover

There is an even sharper aggregate statement.  Let \({\mathscr K}_d\) be
the set of all labelled saturated radius-\(d\) chain segments in the band.
The symmetric group \(G=S_{2m}\) acts transitively on
\({\mathscr K}_d\): a chain is specified by its middle set, an ordered
\(d\)-tuple deleted below, and an ordered \(d\)-tuple added above.

Fix one full recursive radius-\(d\) necklace \(B_d\), containing
\(R=2\ell\) chain columns, and fix one clipped full SCD \({\cal D}\),
containing

\[
 c_d=N_d-N_{d+1}\quad(d<H),\qquad c_H=N_H
\]

columns of clipped radius \(d\).

### Theorem 4.4 (recursive-necklace/SCD double resolution)

There is one exact integral multiset \({\mathfrak X}\) of chain columns
with both of the following resolutions.

1. **Dynamic resolution:** for every \(d\), it is the union of \(c_d\)
   indexed copies of the complete coordinate orbit
   \(\{\sigma B_d:\sigma\in G\}\).
2. **Coverage resolution:** it is the union of \(R\) indexed copies of
   every coordinate relabeling \(\sigma{\cal D}\), \(\sigma\in G\).

Thus \({\mathfrak X}\) is simultaneously a union of genuine recursive
rotor cycles and a union of \(R|G|\) genuine integral full-SCD colours.

#### Proof

By transitivity and double counting, a fixed chain column
\(K\in{\mathscr K}_d\) occurs

\[
 {|G|R\over|{\mathscr K}_d|}
\]

times in the indexed coordinate orbit of \(B_d\), and

\[
 {|G|c_d\over|{\mathscr K}_d|}
\]

times among the radius-\(d\) columns in the indexed orbit of
\({\cal D}\).  Multiplying the first orbit by \(c_d\) and the second by
\(R\) gives the same multiplicity

\[
 { |G|Rc_d\over|{\mathscr K}_d|}
\]

for every \(K\).  Hence the two radius-\(d\) multisets are identical.
Take their disjoint union over \(d\). \(\square\)

If every dynamic necklace could retain one SCD colour for long runs, its
normalized one-cut toll would be

\[
 {1\over R|G|}
 \sum_{d=0}^H 2d\,c_d|G|
 ={2\over R}\sum_{q=1}^HN_q
 \le {2HW\over R}=o(W).
 \tag{4.8}
\]

The theorem does **not** supply that colouring.  Identifying the two
resolutions requires, for every repeated chain type, a bijection between
its dynamic occurrences and its SCD-colour occurrences.  Arbitrary
typewise bijections can switch colour at essentially every step of every
necklace.  The exact residual problem is therefore a low-switch resolution
of two already integral decompositions, rather than a fractional or
divisibility problem.

### 4.5 Exact minimum-switch assignment

The last sentence has a literal matching formulation.  On the left put
every chain occurrence in the dynamic resolution of Theorem 4.4.  On the
right put every chain slot in its coverage resolution; a right slot carries
the colour \((r,\sigma{\cal D})\), where \(1\le r\le R\) is the copy
index.  Join a left occurrence to a right slot exactly when they are the
same labelled chain column.

Call this bipartite multigraph \({\cal G}\).  For each chain type, its left
and right multiplicities agree by Theorem 4.4, so the corresponding
component of \({\cal G}\) is a balanced complete bipartite graph.  Hence
\({\cal G}\) has perfect matchings, and every perfect matching is an exact
integral colouring of all dynamic occurrences by genuine SCD colours.

For a perfect matching \(M\), read the induced colours around every
recursive necklace and let \(r_d(M)\) be the total number of maximal cyclic
constant-colour runs in the radius-\(d\) necklaces (a monochromatic whole
cycle counts as one run).  Then

\[
 \boxed{
 \operatorname{Switch}(M)=
 \sum_{d=0}^H(2d+1)r_d(M)}
 \tag{4.9}
\]

is exactly the aggregate conservative toll of the induced
within-necklace rotor skeleton across all \(Q=R|G|\) SCD colours.  Indeed,
each constant-colour run is one directed rotor path component in that
colour, and every chain slot is used once.  Additional rotor arcs between
different necklaces could only lower the globally optimized toll.

Thus the two-resolution form of the missing theorem is the entirely
integral optimization

\[
 \boxed{
 \min_{M\text{ perfect matching of }{\cal G}}
 \operatorname{Switch}(M)=o(QW).}
 \tag{4.10}
\]

The matching constraints themselves decouple by chain type; the run
objective couples consecutive *different* types.  This pinpoints why
typewise Birkhoff matching proves feasibility but gives no switch bound.

## 5. What multiframe freedom removes, and what it does not

At a fixed lower depth \(q\), project the complete multiframe occurrence
library onto lower targets and middle owners.  A target
\(T\in\binom{[2m]}{m-q}\) is adjacent to \(X\in\binom{[2m]}m\) exactly
when

\[
 T\subseteq X.
 \tag{5.1}
\]

Necessity follows from (1.1).  For sufficiency, pair the \(q\) elements of
\(X\setminus T\) with \(q\) distinct elements of \(X^c\), make these the
first \(q\) active recursive directions, and complete the pair frame as in
Theorem 2.1.

Hence the projected graph is the full biregular Boolean inclusion graph.
It has a matching saturating every lower target.  Indeed, for a target
family \({\cal A}\), double-counting edges gives

\[
 |\Gamma({\cal A})|
 \ge {\binom{m+q}{q}\over\binom mq}|{\cal A}|
 ={W\over N_q}|{\cal A}|
 \ge |{\cal A}|.
 \tag{5.2}
\]

The upper projection is identical by complementation.  More strongly,
Corollary 2.2 gives simultaneous all-depth integral ownership when packet
length one is permitted.

This proves that there is no surviving *marginal* Hall obstruction in the
all-frame library.

By contrast, fix one coordinate pairing.  If a lower target has \(f\) full
pairs, its pure pair-flip source must be one of

\[
 V_f={m!\over f!^2(m-2f)!}2^{m-2f}
\]

middle owners of source type \(f\), whereas the number of targets is

\[
 T_{f,q}={m!\over f!(f+q)!(m-2f-q)!}2^{m-2f-q}.
\]

Thus a fixed-frame exact cover has the Hall-capacity deficit

\[
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+.
 \tag{5.3}
\]

At \(q=A\sqrt m+o(\sqrt m)\), this is

\[
 D_{m,q}=(\kappa_A+o(1))W,
 \qquad \kappa_A>0.
 \tag{5.4}
\]

Therefore no fixed-frame subhypergraph of (3.4) has a perfect matching in
the Gaussian band.  Multiple, owner-dependent pair frames are mandatory.

## 6. Audit of the entropy/discrepancy claim

The orbit-average calculation in
`MATH_ATTACK_FELL_MULTIFRAME_ENTROPY_DISCREPANCY_AUDIT_20260725.md` and
`MATH_ATTACK_ROTOR_RECURSIVE_CUBE_MIXED_FRAME_INTEGRAL_DISCREPANCY_20260725.md`
is correct: coordinate conjugates give an exact rational solution of the
linear relaxation of (3.4), with fractional toll \(O(HW/\ell)\).

It does not round (3.4).

* Independent selection at mean-one mask rows leaves an asymptotic
  \(e^{-1}\) fraction of holes and a positive pair-collision density.
* A discrepancy bound proves exact ownership only when every integer row is
  brought within strictly less than one of its required value.  No such
  bound is established.
* Conditioning on middle ownership alone does not force internal frame
  spread: a uniformly relabelled fixed-frame factor is exact in the middle
  and symmetric in law, but every realization retains (5.3).
* Whole-cycle rank congruences are only the first obstruction.  Correction
  segments repair the scalar residues cheaply, but no argument proves that
  the remaining mask vector belongs to the nonnegative packet semigroup.

Thus the entropy notes contain no hidden integral rounding step.  The exact
conclusion presently available is only

\[
 \mathbf1_{{\cal B}_H}\in
 \operatorname{cone}_{\mathbb Q_{\ge0}}\{\mathbf1_{E(P)}\},
\]

whereas coefficient one through this SCD lane requires an integral perfect
matching of cost \(o(W)\).

## 7. Comparison with the weaker direct compiler

The literal compiler does not require a band SCD.  Let \({\mathscr P}_H\)
be all legal radius-\(H\) recursive-cycle intervals in all frames.  For a
piece \(P\), let \(O(P)\) be its middle owners and let
\({\cal T}^{\pm}_q(P)\) be the targets hit by its ambient consecutive paths,
as certified by (1.4) and complementation.

An integral `MFUP_A` object is an ordered family
\((P_1,\ldots,P_s)\) satisfying

\[
 \sum_{i:X\in O(P_i)}1=1
 \quad\text{for every middle }X,
 \tag{7.1}
\]

and having objective

\[
 \Theta=
 \sum_{q=1}^H\left(
 N_q-\left|\bigcup_i{\cal T}^-_q(P_i)\right|
 +N_q-\left|\bigcup_i{\cal T}^+_q(P_i)\right|
 \right)
 +\sum_{i<s}(b(P_i,P_{i+1})-1).
 \tag{7.2}
\]

Here \(b\) is the exact useful-prefix bridge length.  The direct compiler
has length

\[
 W+2H+\Theta.
 \tag{7.3}
\]

Thus `MFUP_A` is exactly the assertion that (7.1) has an integral ordered
solution with \(\Theta=o(W)\).  It drops target uniqueness, the radius
census, and SCD semigroup membership.  It nevertheless retains the two
hard correlations that fractional averaging loses:

1. the pieces must partition the middle owners exactly; and
2. the same long pieces must simultaneously hit almost every target and
   admit low-excess ordering.

If all selected pieces have length at least \(2\ell\), then their number is
at most \(W/(2\ell)\), and even the worst bridge bound gives

\[
 \sum(b-1)\le {HW\over\ell}=o(W).
 \tag{7.4}
\]

Therefore, for unfragmented whole necklaces, the remaining `MFUP_A` issue
is the integral exact-owner/low-hole selection.  An \(o(W/H)\) population
of short residual pieces is harmless; a merely \(o(W)\) residual population
is not.

No discrepancy or entropy argument currently proves this weaker integral
selection either.

## 8. Exact remaining statements

The stronger rotor--SCD gate is

\[
 \boxed{
 \min\left\{\sum_{P\in{\cal M}}(2d(P)+1):
 {\cal M}\text{ is a perfect matching of }{\cal H}_{m,H,\ell}
 \right\}=o_A(W).}
 \tag{RSCD\(_A^{\rm rec}\)}
\]

The weaker direct gate is

\[
 \boxed{\min\Theta=o_A(W)}
 \tag{MFUP\(_A\)}
\]

over the integral ordered owner partitions in (7.1)--(7.2).

The recursive cube theorem proves that every proposed packet is physically
valid, has long residence, and is two-sided rainbow internally.  The orbit
average proves the fractional versions of both boxes.  The fixed-frame
Hall deficit proves that any integral solution must genuinely mix pair
frames.  Theorem 2.1 and Corollary 2.2 prove that all-frame integral
feasibility exists when the packet-cost constraint is dropped.

What is not proved is the low-cost clustering of that integral feasibility
into long recursive intervals.  That is the exact cross-stratum coupling
problem.
