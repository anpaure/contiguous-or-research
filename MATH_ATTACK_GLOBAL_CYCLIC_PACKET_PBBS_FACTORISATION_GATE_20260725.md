# Global cyclic packets from PBBS fragments: the factorisation gate

Date: 2026-07-25

Pure mathematics only.  No computation, solver, web input, or
fixed-uniformity matching theorem is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=W/n.
 \tag{0.1}
\]

The middle-only request for \(B\) cyclic packets is already solved exactly
by the minimum odd-cycle factor: its \(B\) cycles are literal cyclic
orders and partition the middle layer.  The unresolved near-design is the
simultaneous central-shadow requirement

\[
 \sum_{q\le H}(M_q^-+M_q^+)=o(W).
 \tag{0.2}
\]

Trying to obtain a better factor by cutting the PBBS factor into
return-free pieces and globally repacketizing the pieces meets a new
obstruction before (0.2): the departure alphabets of the pieces must admit
an asymptotically optimal hypergraph edge-colouring.

More precisely, if the PBBS pieces have common length \(h\), cover
\((1-o(1))W\) owner positions, and have balanced coordinate flow, their
departure multihypergraph is approximately \(B\)-regular and has
approximately \(nB/h\) edges.  Packing the pieces into
\((1+o(1))B\) cyclic orders requires

\[
 \boxed{\chi'(\mathcal D)=(1+o(1))B.}
 \tag{0.3}
\]

The quotient-edge corner theorems do not imply (0.3).  There are
translation-equivariant, perfectly regular, pairwise-intersecting
departure systems in which every individual piece is a legal return-free
Johnson geodesic and has no internal PBBS return or corner, but

\[
 \frac{\chi'(\mathcal D)}{\Delta(\mathcal D)}
 =\Theta(h).
 \tag{0.4}
\]

Thus the natural lemma

> quotient-edge disjointness + balanced labels + sparse PBBS corners
> imply global cyclic packetization

is false.

This is not yet a counterexample to the actual PBBS near-design theorem.
The projective obstruction cannot occupy a positive owner-scale mass with
distinct middle starts: its departure blocks have exponentially small
middle upward shadow.  The genuine surviving theorem must combine
PBBS balance with this owner-spread information and prove all weighted
matching cuts for the departure/arrival systems, followed by the
central-shadow condition (0.2).  That global spread-to-factorisation
theorem is currently unproved.

## 1. Exact completion of one return-free fragment

Let

\[
 P=(X_0,X_1,\ldots,X_h)
 \tag{1.1}
\]

be a directed Johnson geodesic with

\[
 X_{i+1}=X_i-\{d_i\}+\{a_i\},
 \qquad 0\le i<h,
 \tag{1.2}
\]

where all \(2h\) labels

\[
 d_0,\ldots,d_{h-1},a_0,\ldots,a_{h-1}
 \tag{1.3}
\]

are distinct.  Put

\[
 D(P)=\{d_0,\ldots,d_{h-1}\},\qquad
 A(P)=\{a_0,\ldots,a_{h-1}\},
 \tag{1.4}
\]

\[
 K(P)=X_0\setminus D(P),\qquad
 R(P)=[n]\setminus(X_0\cup A(P)).
 \tag{1.5}
\]

Then

\[
 |K(P)|=m-h,\qquad |R(P)|=m+1-h.
 \tag{1.6}
\]

### Lemma 1.1 (literal cyclic completion)

Choose arbitrary linear orders of \(K(P)\) and \(R(P)\).  The cyclic
coordinate order

\[
 \pi_P=
 (d_0,\ldots,d_{h-1},K(P),
  a_0,\ldots,a_{h-1},R(P))
 \tag{1.7}
\]

has

\[
 X_i=I_{\pi_P}(i,m),\qquad 0\le i\le h.
 \tag{1.8}
\]

In particular every return-free PBBS fragment of length \(h<m\) is
individually a legal cyclic-interval packet segment.

#### Proof

The first \(m\) entries of (1.7) are

\[
 D(P)\dot\cup K(P)=X_0.
\]

After shifting the window \(i\) positions, its entries are

\[
 \{d_i,\ldots,d_{h-1}\}
 \dot\cup K(P)
 \dot\cup\{a_0,\ldots,a_{i-1}\},
 \]

which is exactly \(X_i\) by (1.2).  This proves (1.8).
\(\square\)

The difficulty is therefore not the completion of one box.  It is the
simultaneous completion of about \(n/h\) boxes inside each one of only
\(B\) global packets.

## 2. Every global packet colour is a departure matching

In a complete cyclic order

\[
 \pi=(z_0,\ldots,z_{n-1}),
 \tag{2.1}
\]

the transition from its \(m\)-window at start \(j\) to the next window
deletes \(z_j\).  Going once around the packet deletes every coordinate
exactly once.

### Lemma 2.1 (departure disjointness)

Suppose owner-disjoint fragments \(P_1,\ldots,P_t\) occur as disjoint
transition segments of one cyclic packet.  Then

\[
 D(P_i)\cap D(P_j)=\varnothing
 \qquad(i\ne j).
 \tag{2.2}
\]

The analogous statement holds for their arrival sets.

#### Proof

The transition slots occupied by owner-disjoint segments are distinct.
The deleted label at a transition slot is the coordinate occupying that
slot in (2.1), and every coordinate occupies only one slot.
\(\square\)

Let \(\mathcal D\) be the multihypergraph on \([n]\) whose edge belonging
to \(P\) is \(D(P)\).  A packetization into \(C\) cyclic packets gives a
proper \(C\)-edge-colouring of \(\mathcal D\).  Consequently

\[
 C\ge\chi'(\mathcal D)
 \ge\sup_{\mathcal F\subseteq E(\mathcal D)}
       \frac{|\mathcal F|}{\nu(\mathcal F)},
 \tag{2.3}
\]

where \(\nu(\mathcal F)\) is the maximum number of pairwise disjoint
departure blocks in \(\mathcal F\).

If all fragments have length \(h\), their owner mass is
\((1+o(1))W\), and every coordinate is deleted
\((1+o(1))B\) times, then

\[
 |E(\mathcal D)|=(1+o(1))\frac{nB}{h},
 \qquad
 \Delta(\mathcal D)=(1+o(1))B.
 \tag{2.4}
\]

Thus \(B\) colours have exactly the scalar capacity: almost every colour
would have to be an \(h\)-set matching of size \(n/h\).  The required
statement is a near-resolution, not an ordinary sparse matching.

## 3. Deck phases do not remove the obstruction

Identify the labels with \(\mathbb Z_n\).  Changing the spatial phase of a
quotient fragment translates its departure set.  Two fragments \(P,Q\)
can share a packet only if some relative phase makes their departure sets
disjoint.  Equivalently, a necessary condition is

\[
 D(P)-D(Q)\ne\mathbb Z_n.
 \tag{3.1}
\]

Indeed,

\[
 (D(P)+u)\cap(D(Q)+v)\ne\varnothing
 \quad\Longleftrightarrow\quad
 v-u\in D(P)-D(Q).
 \tag{3.2}
\]

There are small explicit sets for which every phase conflicts.  Put
\(k=\lceil\sqrt n\rceil\) and

\[
 E=
 \{0,1,\ldots,k-1\}
 \cup
 \{0,-k,-2k,\ldots,-(k-1)k\}
 \pmod n.
 \tag{3.3}
\]

Then

\[
 |E|\le2k,\qquad E-E=\mathbb Z_n.
 \tag{3.4}
\]

For if \(0\le x<n\), write \(x=ak+b\) with
\(0\le a,b<k\); then

\[
 x=b-(-ak)\in E-E.
\]

Hence two fragments with departure alphabet \(E\) cannot occur in one
cyclic packet under any two deck phases.  This is already a genuinely
global phase obstruction: neither fragment has an internal return.

## 4. A regular projective obstruction

The preceding pair can be made perfectly balanced.  Let \(q\) be a prime
power, let

\[
 n=q^2+q+1,\qquad h=q+1,
 \tag{4.1}
\]

and take the point-line incidence system of the projective plane of order
\(q\).  It has \(n\) points and \(n\) lines; every line has \(h\) points,
every point lies on \(h\) lines, and two lines meet.

Repeat every line \(t\) times.  The resulting \(h\)-uniform
multihypergraph \(\mathcal L_t\) satisfies

\[
 |E(\mathcal L_t)|=tn,\qquad
 \Delta(\mathcal L_t)=th,\qquad
 \nu(\mathcal L_t)=1.
 \tag{4.2}
\]

All its edge copies are pairwise intersecting, so

\[
 \boxed{
 \chi'(\mathcal L_t)=tn
 =\frac nh\,\Delta(\mathcal L_t)
 =\Theta(h)\Delta(\mathcal L_t).}
 \tag{4.3}
\]

For \(q\) a power of two, \(n\) is odd.  The Singer model makes the line
set one cyclic translation orbit, so (4.3) persists under the exact deck
symmetry: every coordinate has the same departure degree, and arbitrary
spatial phase shifts cannot separate two line blocks.

It also fits the scalar quotient-edge ledger exactly.  Take \(t\)
abstract quotient traces, give each trace \(h\) fresh quotient edges, and
put the same normalized Singer line on every trace.  The traces are
pairwise quotient-edge-disjoint and use \(th\) quotient edges.  Lifting
one trace through all \(n\) deck phases produces every translated line
once.  Hence the complete deck lift of the \(t\) traces is precisely
\(\mathcal L_t\).  Every trace has distinct internal labels, so its
zero-winding return and corner ledgers are empty.

Each line can be realized as the departure alphabet of a legal
return-free fragment.  Choose an \(m\)-owner \(X\) containing the line,
choose an \(h\)-set \(A\subseteq[n]\setminus X\), and order the line and
\(A\).  Formula

\[
 X_i=(X\setminus\{d_0,\ldots,d_{i-1}\})
       \cup\{a_0,\ldots,a_{i-1}\}
 \tag{4.4}
\]

is an \(h\)-step Johnson geodesic, and Lemma 1.1 makes it a literal cyclic
segment.  It has no repeated departure, no repeated arrival, no internal
zero-winding return, and hence no nonoverlap corner for the PBBS corner
atlas to charge.

Take \(t=\lfloor B/h\rfloor\).  Then
\(th=(1-o(1))B\), so (4.2) has the balanced departure degree demanded in
(2.4) up to a negligible scalar residue, but it requires

\[
 tn=(1-o(1))B\,\frac nh=\Theta(Bh)
 \tag{4.5}
\]

packets instead of \(B\).  Thus even perfect one-coordinate balance,
translation equivariance, legal chronology, and zero corner count do not
prove the global packet lemma.

This deck is a countermodel to an inference from the recorded packing,
balance, and corner properties.  It is not asserted to be an orbit of the
canonical PBBS permutation; that additional chronology is exactly what an
actual positive PBBS theorem would have to exploit.

## 5. Why this does not refute the actual PBBS near-design

The projective obstruction cannot occur with owner-scale multiplicity and
distinct middle starts.  A fixed \(h\)-set \(D\) is contained in exactly

\[
 C_h=\binom{n-h}{m-h}
 \tag{5.1}
\]

middle owners, and

\[
 \frac{C_h}{W}
 =\frac{(m)_h}{(n)_h}
 \le\left(\frac mn\right)^h
 <2^{-h}.
 \tag{5.2}
\]

There are only \(n\) projective lines.  Therefore the number of distinct
possible starting owners whose departure block is a projective line is at
most

\[
 nC_h<n2^{-h}W=o(W/h).
 \tag{5.3}
\]

But a full owner-scale decomposition into \(h\)-fragments needs
\((1+o(1))W/h\) distinct starts.  The counterexample in Section 4 is
therefore a counterexample to the proposed structural implication, not an
embedding into the actual PBBS owner factor.

This scale calculation is useful positive information: any genuine
critical obstruction must use exponentially many departure shapes rather
than a projective-plane-sized catalogue.

## 6. The strengthened global lemma actually required

For a PBBS fragment family \(\mathcal P\), retain simultaneously:

1. its departure block \(D(P)\);
2. its arrival block \(A(P)\);
3. its distinct starting owner \(X(P)\supseteq D(P)\);
4. its ordered entry and exit ports; and
5. all attached correct central flags which must survive repacketization.

The first missing assertion is the following owner-spread
factorisation statement.

> **PBBS global factorisation \(\mathrm{PGF}_h\).**
> If \(\mathcal P\) is the deck-balanced, quotient-edge-disjoint
> return-free fragment family extracted from the actual PBBS factor, then
> its departure and arrival demands have one common
> \((1+o(1))B\)-colouring in which every colour is slot-compatible with a
> single cyclic coordinate order.

Even before the common arrival and slot conditions, \(\mathrm{PGF}_h\)
requires every matching cut

\[
 \boxed{
 |\mathcal F|
 \le(1+o(1))B\,\nu_D(\mathcal F)
 \qquad(\mathcal F\subseteq\mathcal P),}
 \tag{6.1}
\]

and the weighted analogues of (6.1).  Here \(\nu_D\) is matching number
for the departure blocks.  Coordinate balance tests only star cuts.
The projective system tests a non-star cut and violates (6.1) by a factor
\(\Theta(h)\).

The exact fractional version is

\[
 \boxed{
 \sum_{P\in\mathcal P}x_Py_P
 \le(1+o(1))B
 \max_{M\ {\rm departure\ matching}}
       \sum_{P\in M}y_P
 \qquad(y_P\ge0),}
 \tag{6.1a}
\]

with \(x_P\) the multiplicity of the fragment demand.  Even (6.1a) is
only the one-sided departure gate; a packet construction needs a common
integral colouring for departures, arrivals, and ordered slots.

The new ingredient available in the actual PBBS family is the injective
owner assignment

\[
 P\longmapsto X(P),\qquad D(P)\subseteq X(P).
 \tag{6.2}
\]

Section 5 shows that this assignment kills the projective example.  A
plausible global route is therefore a stability theorem of the following
form:

\[
 \begin{array}{c}
 \text{if an \(h\)-uniform weighted family has matching number \(k\),}\\
 \text{point degrees at most \(B\), and distinct assigned
 \(m\)-supersets,}\\
 \text{then its total weight is at most \((1+o(1))kB\).}
 \end{array}
 \tag{6.3}
\]

Statement (6.3) is exactly a global cross-box sharing lemma.  It would
combine an Erdős-matching-type star stability alternative with an
upper-shadow bound for the non-star residue.  It is not a consequence of
the PBBS corner inequalities currently proved, and no proof of (6.3) is
known here.

## 7. Packet factorisation is still only the first half

Suppose \(\mathrm{PGF}_h\) is proved.  It gives about \(B\) legal cyclic
orders and covers the PBBS middle owners up to the permitted residue.  To
finish the cyclic-interval near-design, the same colours must satisfy

\[
 \boxed{
 \sum_{q\le H}
 \left[
 N_q-\bigl|\{I_\pi(j,m-q)\}\bigr|
 +
 N_q-\bigl|\{I_\pi(j,m+1+q)\}\bigr|
 \right]
 =o(W),}
 \tag{7.1}
\]

where the unions range over the selected packet orders and starts.

The PBBS correct-support theorem says that every target has at least one
correct witness before the cuts.  The corner theorem controls the internal
geometry of witnesses belonging to one return and shows that macroscopic
corners are sparse.  Neither theorem says that the witnesses retained by a
common packet colour satisfy (7.1).  This is a second augmented
matching-cut problem, now on the attached interval targets.

Thus the genuinely global route has two exact gates:

\[
 \boxed{
 \begin{array}{ll}
 \text{G1:}&\text{owner-spread departure/arrival factorisation
 as in (6.3);}\\
 \text{G2:}&\text{one common factorisation whose attached
 interval rows satisfy (7.1).}
 \end{array}}
 \tag{7.2}
\]

The local coefficient-\(>1\) product boxes do not enter either gate.

## 8. Final status

The PBBS corner theory does not by itself yield a global cyclic-interval
near-design.  Its local conclusion is compatible with a global
projective-plane line-graph obstruction.  The naive global packing lemma is
therefore false.

The obstruction is not yet large enough to live inside the actual
distinct-owner PBBS factor.  Owner spread eliminates it at the required
scale and points to the correct replacement theorem (6.3).  Proving
(6.3), then its two-sided ordered and shadow-augmented version (7.2), would
give the requested \((1+o(1))B\) cyclic packets and \(o(W)\) central
misses.  No such theorem, and no actual PBBS counterexample to it, is
proved here.
