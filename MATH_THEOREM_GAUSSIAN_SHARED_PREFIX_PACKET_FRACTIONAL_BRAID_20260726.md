# Gaussian shared-prefix product braids: an exact fractional moving-frame packet cover

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, web input,
or probabilistic rounding is used.

> **Audit correction (2026-07-26).**  The cyclic packet below is an
> ordinary directed cyclic order, and its full coordinate-orbit average
> is only the standard symmetric fractional point.  More importantly,
> Section 5 imposes the unnecessarily strong owner-disjoint density
> \(W/(2m)\).  The correct weak integral gate uses
> \(K=\lfloor N_{q_0}/(2m)\rfloor\), middle collision excess \(o(W)\),
> and aggregate signed annular holes \(o(W)\).  The corrected compiler
> ledger and the exact all-depth trace-rigidity audit are in
> MATH_THEOREM_Q0_PARTIAL_PACKET_GATE_AND_HEREDITARY_TRACE_RIGIDITY_20260726.md.
> The fractional identities in this note remain valid; the claim that
> Section 5 is the exact remaining gate is superseded.

## 0. Outcome

Work in \(B_{2m}\), put

\[
 W=\binom{2m}{m},
\tag{0.1}
\]

and fix constants

\[
 0<a<b<\infty,\qquad
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor.
\tag{0.2}
\]

The separated-prefix audit forced
\(\Omega(W/\sqrt m)\) frame-escaping product atoms and showed that paying
an independent \(\Theta(\sqrt m)\) prefix for each atom costs
\(\Omega(W)\).  This note constructs the smallest exact shared-state model
which avoids that toll.

There is an explicit simple middle-owner cycle

\[
 {\cal C}=(Z_0,Z_1,\ldots,Z_{2m-1})\cong C_{2m}
\tag{0.3}
\]

with the following properties.

1. Its cyclic support word is \(H'\)-safe for every \(H'\le m\).
2. It is antipodal:
   \[
    Z_{j+m}=Z_j^c.
   \tag{0.4}
   \]
3. For every \(h=\Theta(\sqrt m)\), all but \(O(h)\) of its edges split
   into \(\Theta(m/h)=\Theta(\sqrt m)\) complete length-\(h\)
   product-SCD atoms, each allowed its own coordinate frame.
4. Its entire all-depth state sequence is compiled with one cyclic collar:
   the literal factor length is \(2m+2H\), not
   \(\Theta(m/h)\cdot H\).

Let \(\mathscr O\) be the complete labelled coordinate-conjugacy orbit of
\({\cal C}\).  Give every labelled packet the common weight

\[
 \theta_m=\frac{W}{(2m)!\,2m}.
\tag{0.5}
\]

Then:

\[
 \boxed{
 \sum_{P\in\mathscr O}\theta_m\,a_X(P)=1
 \quad\text{for every }X\in\binom{[2m]}m,}
\tag{0.6}
\]

and, simultaneously for every \(q_0\le q\le H\),

\[
 \boxed{
 \sum_{P\in\mathscr O}\theta_m\,b_{q,T}^-(P)
 =\frac{W}{N_q}\ge1
 \quad
 (T\in\binom{[2m]}{m-q}),}
\tag{0.7}
\]

\[
 \boxed{
 \sum_{P\in\mathscr O}\theta_m\,b_{q,U}^+(P)
 =\frac{W}{N_q}\ge1
 \quad
 (U\in\binom{[2m]}{m+q}),}
\tag{0.8}
\]

where \(N_q=\binom{2m}{m-q}\), \(a_X(P)\) is owner incidence, and
\(b^\pm\) count cyclic intersection/union windows.

The total fractional literal cost is

\[
 \boxed{
 \sum_{P\in\mathscr O}\theta_m(2m+2H)
 =W+\frac HmW
 =W+O_{a,b}(W/\sqrt m).}
\tag{0.9}
\]

Thus the Gaussian annulus admits an exact simultaneous-depth
**fractional shared-prefix braid** with \(o(W)\) collar toll.  It moves
frames on positive occurrence mass and therefore genuinely evades the
two-fixed-pair obstruction.

At atom scale \(h=\Theta(\sqrt m)\), the weighted packet family contains
\(\Theta(W/\sqrt m)\) product-atom occurrences, but its total collar is
only \(O(W/\sqrt m)\).  The average collar charge per atom is \(O(1)\).
This is the precise sharing mechanism missing from separated prefixes.

The result is fractional, not an integral factor theorem.  The remaining
gate is now exact: choose an owner-disjoint family of these packets with
aggregate signed annular holes \(o(W)\).  If such a family exists, its
literal compilation has length \(W+o(W)\) on the fixed annulus.  No
statewise or fractional fixed-frame obstruction survives; only integral
packet selection and target dispersion remain.

## 1. The shared-state packet

Choose a middle owner \(Z_0\), enumerate it as

\[
 Z_0=\{u_1,\ldots,u_m\},
\]

and enumerate its complement as

\[
 Z_0^c=\{v_1,\ldots,v_m\}.
\]

Put \(e_i=\{u_i,v_i\}\).  Define

\[
 Z_j
 =Z_0-\{u_1,\ldots,u_j\}
      +\{v_1,\ldots,v_j\},
 \qquad0\le j\le m,
\tag{1.1}
\]

and

\[
 Z_{m+j}
 =Z_0^c-\{v_1,\ldots,v_j\}
        +\{u_1,\ldots,u_j\},
 \qquad0\le j\le m.
\tag{1.2}
\]

The endpoint at \(2m\) is identified with \(Z_0\).

### Lemma 1.1 (antipodal universal-safety packet)

The states \(Z_0,\ldots,Z_{2m-1}\) are distinct, satisfy (0.4), and form a
simple \(2m\)-cycle in the Johnson graph.  Its cyclic edge-support word is

\[
 e_1,e_2,\ldots,e_m,e_1,e_2,\ldots,e_m.
\tag{1.3}
\]

Consequently every cyclic window of at most \(m\) edges uses every physical
coordinate at most once.  In particular the packet is cyclically
\(H'\)-safe for every \(H'\le m\).

#### Proof

Equations (1.1)--(1.2) exchange one coordinate at each step, so consecutive
states are Johnson adjacent.  In the first half, pair \(e_i\) is oriented
toward \(v_i\) exactly after time \(i\); in the second half it is oriented
toward \(u_i\) exactly after time \(m+i\).  These two prefix patterns are
distinct except at the identified endpoints, proving simplicity.
Equation (1.2) also gives \(Z_{m+j}=Z_j^c\).  Finally the two occurrences
of each support \(e_i\) in (1.3) are exactly \(m\) edges apart, while the
\(e_i\)'s are pairwise coordinate-disjoint.  Every cyclic window of at
most \(m\) edges therefore sees each coordinate at most once. \(\square\)

### Lemma 1.2 (product-atom decomposition)

Fix \(h=\Theta(\sqrt m)\) with \(h\le H-1\) and
\(h\equiv m\pmod2\).  Each half of the packet can
be divided into

\[
 \left\lfloor\frac mh\right\rfloor
\tag{1.4}
\]

complete monotone segments of length \(h\), apart from one residual segment
of fewer than \(h\) edges.  Every complete segment is a product-SCD
diagonal in a suitable coordinate-conjugate product frame.

#### Proof

Partition the ordered supports \(e_1,\ldots,e_m\) into consecutive
length-\(h\) blocks and one remainder.  A complete block removes \(h\)
distinct labels from the current owner and inserts \(h\) distinct labels
from its complement.  Put \(r=(m-h)/2\).  Choose one local coordinate
half containing all inserted labels, no removed label, exactly \(r\) of
the other currently present coordinates, and exactly \(r\) of the other
currently absent coordinates.  Its complement contains all removed
labels.  The two half-ranks therefore change from \(r\) to \(r+h\) and
from \(r+h\) to \(r\).

Order the two local halves so the inserted and removed labels are the next
singleton increments of coordinate-conjugate BTK chains.  Their product
diagonal is exactly the prescribed segment.  The reverse half is handled
identically. \(\square\)

The point is not the BTK choice: it merely certifies that each segment is
a physical product-SCD atom.  Different segments may use unrelated frames.
Their inherited chronology is the single state cycle (0.3), so no atom
receives an independent prefix.

## 2. One collar compiles the whole packet

For \(0\le q\le H\), define the cyclic lower and upper windows

\[
 L_{j,q}=\bigcap_{t=0}^{q}Z_{j+t},
 \qquad
 U_{j,q}=\bigcup_{t=0}^{q}Z_{j+t},
\tag{2.1}
\]

with indices modulo \(2m\).  Lemma 1.1 gives

\[
 |L_{j,q}|=m-q,\qquad |U_{j,q}|=m+q.
\tag{2.2}
\]

The finite delay-\(H\) factorization of a cyclic \(H\)-safe state route
produces a literal set-word of length

\[
 |{\cal C}|+2H=2m+2H
\tag{2.3}
\]

which represents every set in (2.1) for every \(q\le H\).  Only one
prefix collar is copied for the entire packet.  Every internal product
atom and every cross-atom window uses that same factor word.

Complement-antipodality also gives

\[
 L_{j+m,q}=U_{j,q}^c,
\tag{2.4}
\]

so the lower and upper occurrence ledgers are exactly paired.

## 3. The smallest packet-incidence LP

Let

\[
 G=S_{2m}.
\]

Keep every \(g\in G\) as a label, even if two permutations yield the same
unlabelled packet.  Write \(P_g=g{\cal C}\), and put
\(\mathscr O=\{P_g:g\in G\}\).

For a packet \(P\), define

\[
 a_X(P)=\#\{j:Z_j(P)=X\},
\tag{3.1}
\]

\[
 b_{q,T}^-(P)=\#\{j:L_{j,q}(P)=T\},
 \qquad
 b_{q,U}^+(P)=\#\{j:U_{j,q}(P)=U\}.
\tag{3.2}
\]

Because packets are simple, \(a_X(P)\in\{0,1\}\); target incidences may
have multiplicity.

The exact fractional shared-prefix model is

\[
 x_P\ge0,
\tag{3.3}
\]

\[
 \sum_{P\in\mathscr O}x_Pa_X(P)=1
 \quad\text{for every middle owner }X,
\tag{3.4}
\]

\[
 \sum_{P\in\mathscr O}x_Pb_{q,T}^-(P)\ge1,
 \qquad
 \sum_{P\in\mathscr O}x_Pb_{q,U}^+(P)\ge1
\tag{3.5}
\]

for every \(q_0\le q\le H\) and every target on the indicated signed
rank.  Its objective is

\[
 \min\sum_{P\in\mathscr O}x_P(2m+2H).
\tag{3.6}
\]

The column \(P\) is one complete inherited state cycle.  There are no
cellwise prefix variables; all constituent product atoms share the one
packet collar.

### Theorem 3.1 (exact orbit-averaged fractional braid)

The constant assignment

\[
 x_{P_g}=\theta_m=\frac{W}{(2m)!\,2m}
\tag{3.7}
\]

satisfies (3.4)--(3.5) simultaneously at every depth
\(q_0\le q\le H\), with equality (0.6)--(0.8).  Its objective is (0.9).

#### Proof

Fix a middle owner \(X\).  For each one of the \(2m\) owner positions
\(j\), exactly

\[
 \frac{(2m)!}{W}
\tag{3.8}
\]

permutations \(g\) send \(Z_j\) to \(X\).  Therefore

\[
 \sum_{g\in G}a_X(P_g)
 =2m\,\frac{(2m)!}{W}.
\]

Multiplication by (3.7) proves (3.4).

Fix \(q\le H\) and \(T\in\binom{[2m]}{m-q}\).  Every
\(L_{j,q}\) has rank \(m-q\) by (2.2).  Transitivity of \(G\) on that rank
gives exactly

\[
 \frac{(2m)!}{N_q}
\tag{3.9}
\]

permutations sending a fixed \(L_{j,q}\) to \(T\).  Sum over the \(2m\)
starts and multiply by (3.7):

\[
 \sum_{g\in G}\theta_m b_{q,T}^-(P_g)
 =\frac{W}{N_q}.
\tag{3.10}
\]

The same argument at rank \(m+q\) proves the upper identity.  Since
\(N_q\le W\), both values are at least one, establishing (3.5).

Finally

\[
 \sum_{g\in G}\theta_m
 =\frac{W}{2m}.
\tag{3.11}
\]

Multiply (3.11) by the packet cost (2.3) to obtain (0.9). \(\square\)

No independence or entropy assertion appears in the proof.  It is a
single transitive-orbit double count.

## 4. Exact sharing rate across product cells

Let \(h=d\sqrt m+O(1)\), where \(0<d<b\), with the parity choice required
in Lemma 1.2.  That lemma gives
\(\Theta(m/h)\) complete product atoms in each packet.  From (3.11), the
weighted packet count is \(W/(2m)\).  Hence the total weighted number of
product-atom occurrences is

\[
 \Theta\left(\frac{W}{2m}\frac mh\right)
 =\Theta(W/h)
 =\Theta(W/\sqrt m).
\tag{4.1}
\]

The complete collar toll is

\[
 2H\frac{W}{2m}
 =\frac HmW
 =O(W/\sqrt m).
\tag{4.2}
\]

Dividing (4.2) by (4.1), the average collar charge is

\[
 \Theta(Hh/m)=\Theta_{b,d}(1)
\tag{4.3}
\]

per product atom.  An independent-prefix construction would instead pay
\(\Theta(H)=\Theta(\sqrt m)\) per atom.  The factor-\(\sqrt m\) saving is
literal state inheritance along the packet cycle.

## 5. The exact integral gate

The same columns define the integral shared-prefix problem.  Select a
family \(\mathcal F\subseteq\mathscr O\) satisfying owner disjointness

\[
 \sum_{P\in\mathcal F}a_X(P)\le1
 \quad\text{for every }X\in\binom{[2m]}m.
\tag{5.1}
\]

Let

\[
 R(\mathcal F)
 =W-\sum_X\sum_{P\in\mathcal F}a_X(P)
 =W-2m|\mathcal F|
\tag{5.2}
\]

be the owner leave.  The exact-factor case \(R=0\) is arithmetically
possible only when \(2m\mid W\); the asymptotic gate needs only
\(R=o(W)\).  Equivalently,

\[
 |\mathcal F|=\frac{W-R(\mathcal F)}{2m}.
\tag{5.3}
\]

Define its aggregate signed annular hole count

\[
 \mathcal H_{a,b}(\mathcal F)
 =
 \sum_{q=q_0}^{H}
 \left[
  \sum_T
   \left(1-\sum_{P\in\mathcal F}b_{q,T}^-(P)\right)_+
 +\sum_U
   \left(1-\sum_{P\in\mathcal F}b_{q,U}^+(P)\right)_+
 \right].
\tag{5.4}
\]

### Proposition 5.1 (integral braid implication)

If an owner-disjoint packet family \(\mathcal F\) satisfies

\[
 R(\mathcal F)=o(W),
 \qquad
 \mathcal H_{a,b}(\mathcal F)=o(W),
\tag{5.5}
\]

then the fixed Gaussian annulus \(a\sqrt m<q<b\sqrt m\) has a literal
compiler of length

\[
 W+\frac HmW+o(W)=W+o(W).
\tag{5.6}
\]

#### Proof

Compile every selected packet by its length-\((2m+2H)\) factor word and
concatenate the packet words.  Append every uncovered middle owner once.
Equations (5.2)--(5.3) and (2.3) give

\[
 |\mathcal F|(2m+2H)
 +R(\mathcal F)
 =W+\frac Hm\bigl(W-R(\mathcal F)\bigr).
\]

Append every missing signed target once.  Its total number is (5.4), which
is \(o(W)\) by hypothesis.  Concatenation preserves all internal packet
witnesses. \(\square\)

The integral gate is deliberately an \(L^1\) missing-shadow condition,
not quadratic pair balance and not exact one-copy target ownership.
Repeated annular targets are harmless except insofar as they consume the
fixed owner partition.

## 6. Audit and boundary

Proved here:

1. an explicit \(H\)-safe antipodal packet containing
   \(\Theta(\sqrt m)\) moving-frame product atoms;
2. the smallest whole-packet owner/target incidence LP;
3. an exact simultaneous-depth fractional solution by complete orbit
   averaging;
4. fractional cost \(W+O(W/\sqrt m)\) across every fixed Gaussian annulus;
   and
5. the exact integral owner-factor plus \(L^1\)-hole gate whose solution
   would give a literal \(W+o(W)\) annulus compiler.

Not proved here:

1. an integral owner-disjoint near-packing from the packet orbit with
   owner leave \(o(W)\);
2. \(o(W)\) aggregate annular holes after such a partition;
3. an absorber or deterministic switch system for the packet hypergraph;
   or
4. coefficient one.

The theorem answers the shared-prefix audit positively at the fractional
level.  The separated-prefix linear toll is not statewise: one
\(2m\)-state braid amortizes its Gaussian collar across
\(\Theta(\sqrt m)\) product cells.  What remains is not another exterior
or fixed-frame obstruction, but the integral selection of these
whole shared-state packets with controlled \(L^1\) target holes.
