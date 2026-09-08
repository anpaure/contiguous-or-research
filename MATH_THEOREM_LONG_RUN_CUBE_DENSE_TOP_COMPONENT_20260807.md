# A long-run cube gives an exponential dense-top component with both simple \(q1\) palettes

**Date:** 2026-08-07  
**Method:** direction-indexed missing banks over a long-run binary Gray
cycle  
**Status:** unconditional local component theorem.  For every sufficiently
large triangular parameter it gives \(2^h\) distinct rank-\((t-1)\) top
targets, their exact delayed atoms, a simple rank-\(m\) Johnson owner
cycle, simple lower and upper \(q1\) palettes, positive target residence,
owner biresidence, and literal regeneration.  It does not factor the full
rank-\((t-1)\) layer or realize the lower SCD and compiler rows.

## 1. Parameters and the long-run input

Put

\[
 n=2m+1,\qquad q=d+1,\qquad r=m-d-1=m-q,
\tag{1.1}
\]

and assume \(d\ge2\).  Choose an **even** integer \(h\ge4\) satisfying

\[
 \boxed{
 \rho\ge d+1,\qquad h(d+1)\le m-1,
 }
\tag{1.2}
\]

where \(Q_h\) has a cyclic Hamilton Gray code

\[
 z_0,z_1,\ldots,z_{N-1},z_0,
 \qquad N=2^h,
\tag{1.3}
\]

whose cyclic same-direction transition separation is at least \(\rho\).
Write

\[
 z_{e+1}=z_e\oplus {\bf e}_{\tau_e},
 \qquad \tau_e\in[h].
\tag{1.4}
\]

Thus two occurrences of the same \(\tau\)-label are at cyclic edge
distance at least \(\rho\).  The evenness of \(h\) is not needed by the
single-component proof; it is imposed so that the usual undirected
Hamilton decomposition of \(Q_h\) is available for the orthogonal-family
question in Section 6.

Goddyn and Gvozdjak supply (1.3) with

\[
 \rho\ge h-3\log_2 h
\tag{1.5}
\]

for all sufficiently large \(h\).  Hence, at the triangular scale

\[
 \frac{d^2}{m}\longrightarrow\frac{\pi}{4}<1,
\tag{1.6}
\]

one may choose an even

\[
 h=d+O(\log d)
\tag{1.7}
\]

for which both inequalities in (1.2) hold.  Indeed (1.5) pays the first,
while

\[
 h(d+1)=d^2+O(d\log d)<m
\tag{1.8}
\]

pays the second.  No divisibility of \(d+1\) or \(2^h\) is needed.

## 2. The direction-bank construction

Choose pairwise disjoint sets

\[
 K,\quad H_1,\ldots,H_h,\quad
 P_i=\{a_i,b_i\}\ (i\in[h])
\tag{2.1}
\]

with

\[
 |K|=c:=m-h(d+1)-1,
 \qquad |H_i|=d.
\tag{2.2}
\]

The second inequality in (1.2) makes \(c\ge0\).  The total ground-set use
is

\[
 c+hd+2h=m+h-1\le n.
\tag{2.3}
\]

For \(z\in\{0,1\}^h\), let \(V(z)\) choose \(a_i\) or \(b_i\) from
\(P_i\) according to the \(i\)-th bit of \(z\).  At endpoint \(e\), omit
the bank indexed by the **outgoing** Gray direction and put

\[
 \boxed{
 S_e
 =K\ \cup\!
  \bigcup_{i\ne\tau_e}H_i
  \ \cup V(z_e).
 }
\tag{2.4}
\]

Then

\[
 |S_e|
 =c+(h-1)d+h
 =m-d-1=r.
\tag{2.5}
\]

The payload part \(S_e\cap\bigcup_iP_i=V(z_e)\) recovers \(z_e\), so all
\(N\) top targets are distinct.

## 3. Flat simple owners and exact adjacency

### Theorem 3.1 (owner cycle)

The top targets in (2.4) satisfy

\[
 d_J(S_e,S_{e+1})=d+1.
\tag{3.1}
\]

Their central owners

\[
 O_e=S_{e-1}\cup S_e
\tag{3.2}
\]

all have rank \(m\), are pairwise distinct, and form a simple Johnson
cycle.

#### Proof

Since \(\rho\ge3\), consecutive directions are distinct.  Passing from
\(S_e\) to \(S_{e+1}\) removes the bank \(H_{\tau_{e+1}}\), restores the
bank \(H_{\tau_e}\), and performs the one payload exchange in direction
\(\tau_e\).  The banks and payload pairs are disjoint, proving (3.1).

The two adjacent top targets omit different banks, so their union contains
every bank.  Their payload union is the coordinate-set representation of
the Gray edge \(z_{e-1}z_e\).  Therefore

\[
 \boxed{
 O_e
 =K\cup\bigcup_{i=1}^hH_i
   \cup\bigl(V(z_{e-1})\cup V(z_e)\bigr),
 }
\tag{3.3}
\]

and

\[
 |O_e|=c+hd+(h+1)=m.
\tag{3.4}
\]

Distinct edges of a Hamilton cycle are distinct coordinate-set payload
unions, so the owners are pairwise distinct.

At the central target \(S_e\),

\[
\begin{aligned}
 S_{e-1}\setminus S_e
   &=H_{\tau_e}\mathbin{\dot\cup}
     \{\text{the payload value removed in direction }\tau_{e-1}\},\\
 S_{e+1}\setminus S_e
   &=H_{\tau_e}\mathbin{\dot\cup}
     \{\text{the payload value inserted in direction }\tau_e\}.
\end{aligned}
\tag{3.5}
\]

The two singleton payload values belong to different pairs because
\(\tau_{e-1}\ne\tau_e\).  Thus the two differences have intersection
exactly \(H_{\tau_e}\), of rank \(d\).  The dense top-row adjacency
criterion now gives \(O_e\sim O_{e+1}\). \(\square\)

## 4. Exact residence and delayed atoms

### Theorem 4.1 (literal common history)

Every positive run in every target-membership word
\(({\bf1}_{x\in S_e})_e\) has length at least \(d\).  Hence the maximal
delayed atoms

\[
 B_p=\bigcap_{j=0}^{d-1}S_{p+j}
\tag{4.1}
\]

realize every top target:

\[
 \boxed{
 S_e=\bigcup_{p=e-d+1}^{e}B_p.
 }
\tag{4.2}
\]

Every atom has the forced rank

\[
 \boxed{|B_p|=m-d(d+1).}
\tag{4.3}
\]

More explicitly, put

\[
 T_p=\{\tau_p,\tau_{p+1},\ldots,\tau_{p+d-1}\},
 \qquad
 U_p=\{\tau_p,\tau_{p+1},\ldots,\tau_{p+d-2}\}.
\tag{4.4}
\]

These sets have ranks \(d\) and \(d-1\), respectively, and

\[
 \boxed{
 B_p
 =K
  \cup\bigcup_{i\notin T_p}H_i
  \cup\bigcup_{i\notin U_p}\bigl(V(z_p)\cap P_i\bigr).
 }
\tag{4.5}
\]

The complete target, atom, and owner state returns after \(N=2^h\)
positions.

#### Proof

A bank coordinate in \(H_i\) is absent from \(S_e\) exactly when
\(\tau_e=i\).  Between two such absences it has a positive run of length
at least \(\rho-1\ge d\).  A payload coordinate changes membership only
when its Gray direction occurs, so its positive runs have length at least
\(\rho\).  Core coordinates are permanent.  This proves positive target
residence, and the delayed-intersection equivalence gives (4.2).

The \(\rho\)-separation makes the directions in \(T_p\) distinct.  A bank
survives all \(d\) targets in (4.1) exactly when its direction is outside
\(T_p\).  The vertices \(z_p,\ldots,z_{p+d-1}\) use precisely the
\(d-1\) transition directions in \(U_p\); a payload pair contributes its
common selected value exactly when its direction is outside \(U_p\).
This proves (4.5), whose rank is

\[
\begin{aligned}
 |B_p|
 &=c+d(h-d)+(h-d+1)\\
 &=m-d(d+1).
\end{aligned}
\tag{4.6}
\]

Cyclicity of the Gray code proves regeneration. \(\square\)

### Corollary 4.2 (owner biresidence)

The owner sequence is bi-resident through depth \(d\).

#### Proof

Every core and bank coordinate is permanent in (3.3).  Fix one payload
pair.  Between two consecutive transitions of its direction, one value
is selected at all intervening vertices.  The owner edge at either
boundary contains both values.  Thus a payload value has an owner
positive run of length at least \(\rho+1\), while its owner zero gap has
length at least \(\rho-1\ge d\). \(\square\)

The top-target words themselves are not negatively resident: every
\(H_{\tau_e}\) supplies \(d\) isolated zeroes at endpoint \(e\), exactly
as required by
*MATH_COROLLARY_DENSE_TOP_ROW_FORCED_ISOLATED_ZEROES_20260807.md*.
This does not affect the one-sided residence used in (4.2).

## 5. Both \(q1\) palettes are simple

Put

\[
 Q^-_e=O_e\cap O_{e+1},
 \qquad
 Q^+_e=O_e\cup O_{e+1}.
\tag{5.1}
\]

### Theorem 5.1 (lower and upper \(q1\) simplicity)

The \(N\) lower colours and the \(N\) upper colours are respectively
pairwise distinct.  More precisely,

\[
 \boxed{
 Q^-_e
 =K\cup\bigcup_iH_i\cup V(z_e),
 \qquad |Q^-_e|=m-1,
 }
\tag{5.2}
\]

and

\[
 \boxed{
 Q^+_e
 =K\cup\bigcup_iH_i
  \cup V(z_e)
  \cup\{\overline z_e(\tau_{e-1}),
        \overline z_e(\tau_e)\},
 \qquad |Q^+_e|=m+1.
 }
\tag{5.3}
\]

Here \(\overline z_e(i)\) denotes the unselected member of \(P_i\).

#### Proof

The two Gray edges \(z_{e-1}z_e\) and \(z_ez_{e+1}\) use different
directions.  Their payload-coordinate intersection is therefore exactly
\(V(z_e)\), proving (5.2).  Hamiltonicity makes the \(z_e\)'s distinct,
so the lower palette is simple.  Their payload union doubles exactly the
two pairs in directions

\[
 D_e:=\{\tau_{e-1},\tau_e\},
\tag{5.4}
\]

which proves (5.3).

Suppose \(Q^+_e=Q^+_f\).  The doubled payload pairs recover
\(D_e=D_f=:D\), and outside those two pairs the equality says that
\(z_e\) and \(z_f\) agree.  Their Hamming distance is therefore zero,
one, or two.

If it is zero, Hamiltonicity gives \(e=f\).

If it is one, the two vertices are neighbours in one direction of \(D\).
Both \(D\)-directions are the Hamilton-cycle directions incident with
\(z_e\), so this neighbour is \(z_{e-1}\) or \(z_{e+1}\).  Thus
\(f=e\pm1\).  Equality of the two incident-direction sets then gives a
transition pattern \(a,b,a\), repeating direction \(a\) at cyclic
distance two.  This contradicts \(\rho\ge d+1\ge3\).

If the distance is two, the vertices are opposite corners of the
two-dimensional face spanned by \(D\).  At each opposite corner, both
incident Hamilton-cycle edges lie in that face.  These are the four
distinct boundary edges of the square, so they form a closed \(C_4\)
component of the Hamilton cycle.  Since \(h\ge4\), the Hamilton cycle has
more than four vertices, a contradiction.

Therefore \(e=f\), proving upper-palette simplicity. \(\square\)

## 6. Exact local scope and the orthogonal-family interface

One long-run cube component closes:

* \(2^h\) distinct rank-\((t-1)\) top targets;
* their explicit nonempty maximal delayed atoms;
* a flat simple rank-\(m\) Johnson owner cycle;
* simple lower and upper \(q1\) palettes;
* positive target residence, owner biresidence, and regeneration.

It does not cover every target of rank \(t-1\).  Even on one fixed frame
\((K,(H_i),(P_i))\), the possible structured top targets are indexed by

\[
 (z,i)\in\{0,1\}^h\times[h],
\tag{6.1}
\]

where \(z\) is the payload vector and \(i\) is the missing bank.  One
oriented Gray Hamilton cycle selects only

\[
 (z_e,\tau_e),
\tag{6.2}
\]

one outgoing direction at every cube vertex.

Consequently, covering the entire fixed-frame bank (6.1) exactly once is
equivalent to decomposing the symmetric directed cube into directed
Hamilton cycles: one needs \(h\) oriented Hamilton cycles such that at
each vertex their outgoing directions are all of \([h]\).  For even \(h\),
an undirected Hamilton decomposition of \(Q_h\) into \(h/2\) Hamilton
cycles, with both orientations of every cycle, gives such an exact
directed decomposition.  This explains the parity choice in Section 1.

There are two separate obstructions to using this observation as the
desired PBBS factor.

First, the standard Hamilton decomposition need not consist of long-run
cycles.  Its residence-preserving strengthening would be:

> **Orthogonal long-run cube theorem.**  For some even
> \(h=d+O(\log d)\), decompose the symmetric directed \(h\)-cube into
> \(h\) directed Hamilton cycles, each with same-direction transition
> separation at least \(d+1\).

Second, even this stronger theorem would factor only the **top targets**,
not the one-copy owner or \(q1\) rows on the same frame.  This failure is
sharp:

* a directed decomposition uses both orientations of every cube edge;
  formula (3.3) forgets orientation, so every rank-\(m\) owner occurs
  exactly twice;
* formula (5.2) depends only on the payload vertex \(z\), so at a fixed
  vertex the \(h\) cycles all use the same lower \(q1\) colour.  Every
  lower colour occurs exactly \(h\) times.

Equivalently, the fixed frame has \(h2^h\) structured top targets but only
\(h2^{h-1}\) possible owners and only \(2^h\) possible lower colours of
the forms (3.3) and (5.2).  Therefore no same-frame factor can cover all
\((z,i)\) while keeping either owners or lower \(q1\) colours globally
simple.  One long Hamilton component already saturates the fixed frame's
entire lower-\(q1\) palette.

Thus the correct positive use is one long-run cycle per labelled frame,
followed by a target-disjoint selection of different frames.  An
orthogonal long-run decomposition would be useful only for top-target
coverage if the owner and \(q1\) rows were redecorated between cycles.
A further coordinate-labelled frame factor is still needed to cover the
complete Boolean rank-\((t-1)\) target layer and to couple the lower SCD,
full upper deck, owner fusion, and compiler rows.

**Long-run source:** L. Goddyn and P. Gvozdjak, *Binary Gray Codes with
Long Bit Runs*, Electronic Journal of Combinatorics 10 (2003), R27.
