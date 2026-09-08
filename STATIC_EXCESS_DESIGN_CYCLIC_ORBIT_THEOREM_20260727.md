# Static Catalan excess designs by cyclic-orbit rounding

Date: 2026-07-27

This note isolates the purely static part of the excess-design target from
`BALLOT_UPPER_DUALITY_THEOREM_20260727.md`.  The conclusion is favourable:
the prescribed cardinality and the forced endpoint vertex degrees admit an
explicit cyclic-orbit construction, and the higher inclusion degrees can be
made simultaneously quasirandom by selecting the remaining full orbits.

What this does **not** solve is the inverse chronological problem: realizing
the resulting design as the doubled-upper-colour set of one endpoint-rooted,
lower-rainbow Hamilton path.  That realization remains the hard gate.

## 1. Parameters and the endpoint simplification

Put

\[
 v=2r-1,\qquad k=r-2,\qquad C=\operatorname{Cat}_r,
 \qquad b=C-1.
\]

The desired excess design is a simple family

\[
 D\subseteq\binom{\mathbb Z_v}{k},\qquad |D|=b.
\]

The vertex degrees forced by the upper-duality theorem are

\[
 d_D(x)=A-1-\mathbf1_{x\in C_*}
       +\mathbf1_{x\in T_0}+\mathbf1_{x\in T_{\rm end}},
 \tag{1.1}
\]

where

\[
 A=\frac{kC}{v}
  =\frac{2(r-2)}{r+1}\operatorname{Cat}_{r-1}
  =\operatorname{Cat}_r-2\operatorname{Cat}_{r-1}\in\mathbb Z.
 \tag{1.2}
\]

Choose a (k)-set (B) and two distinct points (a,b\notin B), and set

\[
 C_*=\mathbb Z_v\setminus(B\cup\{a,b\}),\qquad
 T_0=C_*\cup\{a\},\qquad
 T_{\rm end}=C_*\cup\{b\}.
 \tag{1.3}
\]

Thus the two endpoints are adjacent middle sets and have intersection
(C_*).  Substitution in (1.1) gives the particularly simple target

\[
 \boxed{d_D(x)=A-\mathbf1_{x\in B}.}
 \tag{1.4}
\]

So all endpoint corrections are absorbed by one missing translate of one
(k)-set.

This endpoint choice is not artificial.  If a lower-rainbow Hamilton cycle
in the middle-levels graph is broken at its lower colour \(C_*\), then its
two projected \(r\)-set endpoints are adjacent, their intersection is
\(C_*\), and their union has complement \(B\).  Thus (1.4) is precisely the
natural degree vector of a broken middle-levels cycle.

This is a **chosen normalization**, not a statement about arbitrary endpoint
data.  Formula (1.1) remains the correct forced vector for a general
one-hole path, and it need not simplify to (1.4) unless
\(T_0\cap T_{\rm end}=C_*\).  The theorem below proves that the static target
is feasible in the cycle-break normalization; it does not prescribe an
arbitrary preassigned triple \((C_*,T_0,T_{\rm end})\).

### Closed-cycle normal form

There is an even cleaner way to state the same observation.  Restore the
deleted closing transition between \(T_{\rm end}\) and \(T_0\).  Its upper
colour is \(\mathbb Z_v\setminus B\).  In the construction below \(B\notin
D\), so this transition changes that upper load from one to two.  Therefore

\[
 \widetilde D:=D\cup\{B\}
 \tag{1.5}
\]

is the excess design of the closed cycle.  It satisfies

\[
 |\widetilde D|=\operatorname{Cat}_r,\qquad
 d_{\widetilde D}(x)=A\quad\hbox{for every }x.
 \tag{1.6}
\]

Thus the endpoint-corrected path problem is equivalent to the especially
natural closed problem:

> construct a lower-rainbow Hamilton cycle whose simple upper excess design
> is a regular \((r-2)\)-uniform family of Catalan cardinality.

Breaking one transition deletes one block \(B\) from that regular design and
produces exactly the forced path boundary vector.

## 2. The only possible Catalan remainders

One has

\[
 \gcd(v,k)=\gcd(2r-1,r-2)=\gcd(3,r-2)\in\{1,3\}.
 \tag{2.1}
\]

Since (A=kC/v) is integral, (v\mid kC).  If (s\) is the residue of
(C\) modulo (v), then

\[
 \boxed{
 \begin{array}{c|c}
 3\nmid v&s=0,\\
 3\mid v&s\in\{0,v/3,2v/3\}.
 \end{array}}
 \tag{2.2}
\]

This is the complete divisibility audit.  There is no uncontrolled Catalan
remainder.

There is also a useful orbit audit.  A non-full translation orbit on
(\binom{\mathbb Z_v}{k}) can occur only when (3\mid v).  Indeed, the
stabilizer order divides both (v) and (k), hence divides (3).  In the
exceptional case every nontrivial stabilizer has order exactly (3), and
the number of periodic (k)-sets is

\[
 P=\binom{v/3}{k/3}.
 \tag{2.3}
\]

This is exponentially smaller than

\[
 N:=\binom vk=\frac{r-1}{2}\operatorname{Cat}_r.
 \tag{2.4}
\]

## 3. Exact cyclic remainder gadgets

Let (G=\mathbb Z_v) act by translation.

### Case 1: (s=0)

Choose (B) with a full (G)-orbit and put

\[
 R=(G\cdot B)\setminus\{B\}.
 \tag{3.1}
\]

Then

\[
 |R|=v-1,\qquad d_R(x)=k-\mathbf1_{x\in B}.
 \tag{3.2}
\]

### Case 2: (s=v/3)

Write (v=3u), (k=3h), and let (H\le G) be the subgroup of order
(u).  Choose (B) so that it has (h) points in each of the three
(H)-cosets and has a full (H)-orbit.  Put

\[
 R=(H\cdot B)\setminus\{B\}.
 \tag{3.3}
\]

Every vertex occurs in exactly (h=k/3) members of (H\cdot B), and hence

\[
 |R|=u-1=s-1,\qquad
 d_R(x)=k/3-\mathbf1_{x\in B}.
 \tag{3.4}
\]

### Case 3: (s=2v/3)

Choose a second balanced (k)-set (B') whose full (H)-orbit is disjoint
from that of (B), and put

\[
 R=((H\cdot B)\setminus\{B\})\cup(H\cdot B').
 \tag{3.5}
\]

Then

\[
 |R|=2u-1=s-1,\qquad
 d_R(x)=2k/3-\mathbf1_{x\in B}.
 \tag{3.6}
\]

Balanced (B,B') with the stated freeness are elementary to obtain: in
each (H)-coset choose a nonempty proper cyclic interval of length (h),
and use unequal offsets between the three cosets when a second orbit or the
avoidance of order-three periodicity is required.

## 4. Exact forced-degree theorem

### Theorem 4.1

For every sufficiently large (r) (and directly also in the small cases),
there are endpoint data of the form (1.3) and a simple family

\[
 D\subseteq\binom{\mathbb Z_{2r-1}}{r-2}
\]

such that

\[
 |D|=\operatorname{Cat}_r-1,
 \qquad d_D(x)=A-\mathbf1_{x\in B}.
 \tag{4.1}
\]

Equivalently, (D) has exactly the forced endpoint degree vector (1.1).

#### Proof

Write (C=qv+s), (0\le s<v).

* If (s=0), take (q-1) mutually disjoint full (G)-orbits, avoiding
  (G\cdot B), and adjoin the remainder (3.1).  The cardinality is
  ((q-1)v+(v-1)=C-1), and every full orbit contributes degree (k), so
  the degree is (qk-\mathbf1_B=A-\mathbf1_B).
* If (s>0), take (q) mutually disjoint full (G)-orbits, avoiding the
  orbit(s) used by the remainder, and adjoin (3.3) or (3.5).  Since
  (ks/v=k/3) or (2k/3), the degree is again
  (qk+ks/v-\mathbf1_B=A-\mathbf1_B).

There are ample full orbits: their catalogue has order (N/v\asymp C/4),
whereas only (q=O(C/r)) are selected; the exceptional periodic catalogue
has size (P=o(N)).  All chosen orbit families are disjoint, so (D) is
simple.  QED.

Thus neither Catalan divisibility nor the endpoint correction is an
obstruction to the static design.

In the closed-cycle language the construction is simpler still:

\[
 \boxed{
 \widetilde D=D\cup\{B\}
 =
 \begin{cases}
 \text{a union of full \(G\)-orbits},&s=0,\\
 \text{full \(G\)-orbits plus one full \(H\)-orbit},&s=v/3,\\
 \text{full \(G\)-orbits plus two full \(H\)-orbits},&s=2v/3.
 \end{cases}}
 \tag{4.2}
\]

Every term on the right is vertex-regular, so (1.6) is immediate.  The
apparently awkward endpoint defect is exactly the one block removed when
the cycle is opened into a path.

## 5. Simultaneous higher-degree discrepancy

The remaining full orbits may be selected to balance every higher inclusion
degree at once.

For a full orbit (O) and a (t)-set (Q), put

\[
 X_O(Q)=|\{A\in O:Q\subseteq A\}|\in[0,v].
\]

Choose the required (q_0=\lfloor(C-1)/v\rfloor) full orbits uniformly
without replacement from the admissible catalogue, after reserving the one
or two orbits used by (R).  If

\[
 L_T=\sum_{t=2}^{T}\binom vt,
\]

Hoeffding's inequality for sampling without replacement and a union bound
give one choice for which, simultaneously for every (2\le |Q|\le T),

\[
 \left|d_D(Q)-\mathbb E d_D(Q)\right|
 \le
 v\sqrt{\frac{q_0}{2}\log(2L_T)}.
 \tag{5.1}
\]

Let

\[
 \lambda_t=(C-1)\frac{\binom{v-t}{k-t}}{\binom vk}
 \tag{5.2}
\]

be the degree of the uniform fractional design.  The fixed remainder,
reserved orbits, and (only when (3\mid v)) periodic (k)-sets alter the
expectation by at most (O(P+v)).  Hence the same construction satisfies

\[
 \boxed{
 |d_D(Q)-\lambda_t|
 \le
 v\sqrt{\frac{q_0}{2}\log(2L_T)}+O(P+v)
 }
 \tag{5.3}
\]

for all (2\le |Q|\le T).  For prime (v), (P=0).

At the critical range (T=O(\sqrt r)), this error is exponentially small
relative to the mean degree.  Indeed,

\[
 \lambda_t=\operatorname{Cat}_r\,2^{-t}\exp(O(t^2/r)),
 \tag{5.4}
\]

whereas the main error in (5.3) is only

\[
 O\!\left(\sqrt{v\operatorname{Cat}_r\,T\log(ev/T)}\right),
 \tag{5.5}
\]

and (P=2^{v/3+o(v)}) in the exceptional composite case.  Consequently

\[
 \max_{2\le |Q|\le T}
 \frac{|d_D(Q)-\lambda_{|Q|}|}{\lambda_{|Q|}}
 =\exp(-\Omega(r))
 \qquad(T=O(\sqrt r)).
 \tag{5.6}
\]

This is vastly stronger than the relative balance required merely to keep
the zero-section counts (z_Q=Z_{r,t}-d_D(Q)) capacity-ordered.  The first
degrees are not probabilistic: they are already exact by Theorem 4.1.

There is in fact a large capacity margin.  If
\(S_t=\binom{v-t}{k-t}\), then

\[
 \frac{Z_{r,t}}{S_t}
 =
 \frac{t+2}{r-1-t},
 \qquad
 \frac{\lambda_t}{S_t}
 =
 \frac{2}{r-1}\left(1-\frac1C\right).
 \tag{5.7}
\]

Consequently, for every fixed \(K\), uniformly for
\(2\le t\le K\sqrt r\),

\[
 Z_{r,t}-\lambda_t
 =
 S_t\left[
 \frac{t(r+1)}{(r-1-t)(r-1)}
 +\frac{2}{C(r-1)}
 \right]
 =(1+o(1))\frac{t}{r}S_t.
 \tag{5.8}
\]

The identity follows because
\(S_t=\binom{v-t}{r-2-t}=\binom{v-t}{r+1}\), so
\(\binom{v-t}{r}/S_t=(r+1)/(r-1-t)\).  In particular, the margin is
positive exactly, and is at least \(tS_t/r\) for all
\(2\le t<r-1\).  On the other hand, (5.3)--(5.6) make the discrepancy
\(o(tS_t/r)\), uniformly for \(2\le t\le K\sqrt r\).  Therefore the
specific orbit selection furnished above rigorously obeys

\[
 d_D(Q)\le Z_{r,t},\qquad
 z_Q:=Z_{r,t}-d_D(Q)\ge0
 \tag{5.9}
\]

for every \(2\le |Q|\le K\sqrt r\), once \(r\) is sufficiently large.
For \(|Q|=1\), nonnegativity follows directly from the exact endpoint degree
formula (1.1).  Thus the claimed critical-window capacity ceiling is a
consequence of an explicit positive margin, not merely of relative
quasirandomness.

### 5.1 Difference-family interpretation

At order two the construction is exactly a partial cyclic difference
family.  If \(O=G\cdot A\), then for \(x\ne y\)

\[
 X_O(\{x,y\})
 =
 |A\cap(A+(y-x))|.
 \tag{5.10}
\]

Thus selecting full orbits selects base blocks whose directed difference
multisets are to be balanced.  Exact balance of the full-orbit part would
require

\[
 (v-1)\mid q_0k(k-1),
 \tag{5.11}
\]

before the small endpoint remainder is even considered; this divisibility
usually fails.  The random-orbit theorem is the appropriate approximate
difference-family substitute.  At higher orders the analogous “difference”
is the translation class of the whole \(t\)-configuration \(Q\), and the
same orbit sampling balances all such shapes simultaneously.

## 6. What standard design theory can and cannot add

* Exact (t)-designs are usually arithmetically unavailable here.  Even an
  exactly constant pair degree would require
  \((C-1)\binom{k}{2}/\binom v2\in\mathbb Z\), which already fails in small
  cases.  Thus floor/ceiling or discrepancy balance, not exact constancy, is
  the correct static target.
* General discrepancy machinery or random rounding of the complete
  (k)-uniform hypergraph would plausibly give approximate balance, but it
  would not preserve the forced vertex vector automatically.  Cyclic-orbit
  rounding is better adapted: every full orbit is an exact (1)-design,
  and the small remainder implements the endpoint defect exactly.
* The absolute error in (5.3) is exponentially large, so this is not a
  claim of floor/ceiling balance at all higher orders.  It is, however,
  exponentially small in relative terms throughout the critical
  (t=O(\sqrt r)) window.  Any theorem demanding absolute (O(1))
  discrepancy would be a genuinely stronger design problem and may face
  further divisibility constraints.

## 7. Verdict on the gate

The static gate is easy in the sense relevant to the present program:

1. cardinality is exact;
2. the endpoint vertex degrees are exact;
3. all critical higher inclusion degrees can be made simultaneously
   quasirandom with overwhelming room;
4. the construction is simple and cyclic-orbit based.

The hidden difficulty is not static discrepancy.  It is **path
realizability**.  Given such a (D), one still has to find a one-hole
lower-rainbow Hamilton path whose upper colours have multiplicity two
exactly on complements of (D).  Standard design/discrepancy theorems say
nothing about that prescribed-colour Hamilton chronology.  In particular,
the hard problem has now sharpened to an inverse realization theorem, not a
block-design existence theorem.
