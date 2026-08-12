# The all-phase PBBS corner atlas and the exact cross-interval residual

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Let

\[
 D_j=P_j1R_j0S_j,\qquad 0\le j\le s,
 \tag{0.1}
\]

be the canonical staircase of a genuine first zero-winding PBBS return
with \(s\ge2\),
and suppose that its endpoint overlap is positive.  Thus

\[
 \Lambda=\delta(D_0)+\delta(D_s)-2m>0.
 \tag{0.2}
\]

Let \(T_0,\ldots,T_{s-1}\) be the dual staircase blocks.  The exact
common-boundary identities are

\[
 U=(0S_{s-1})\cdots(0S_1)=ER_0,
 \tag{0.3}
\]

\[
 V=(\overline T_{s-1}0)\cdots(\overline T_00)
   =R_s(0S_s)E,
 \tag{0.4}
\]

where \(E\) is balanced and

\[
 |E|=\Lambda.
 \tag{0.5}
\]

This note proves the following exact all-phase theorem.

For

\[
 a,b\ge0,\qquad a+b\le s-2,
 \tag{0.6}
\]

put

\[
 X_a=\sum_{0\le j<a}|T_j|,
 \qquad
 Y_b=\sum_{s-b\le j<s}|S_j|,
 \tag{0.7}
\]

with empty sums equal to zero.  The lattice point \((a,b)\) represents
the transported phase pair

\[
 t=a,\qquad u=s-b-1,
 \qquad r:=s-(u-t)-1=a+b.
 \tag{0.8}
\]

Then the pair is in the nonoverlap branch if and only if

\[
 \boxed{X_a+Y_b\ge\Lambda,}
 \tag{0.9}
\]

and it is in the overlap branch if and only if

\[
 \boxed{X_a+Y_b\le\Lambda-2(a+b).}
 \tag{0.10}
\]

Thus the nonoverlap set is an upset in the triangular lattice (0.6).
Every coordinate-minimal nonoverlap point is a genuine corner.  At an
interior corner, the common endpoint word has one literal, disjoint
factorization

\[
 \boxed{
 E=\mathcal U_{b-1}\,H_R\,Z\,H_L\,\mathcal L_{a-1}.}
 \tag{0.11}
\]

Here \(Z\) is the negative common corridor and \(H_L,H_R\) are the two
positive predecessor bridges.  In particular, \(Z\) occurs once in
(0.11), not once for each transported chart.

There is also an exact rectangle law.  If two incomparable minimal
corners have an interlaced upper cross, then its corridor is

\[
 \boxed{Z_{\rm upper}=Z_{\rm left}\,H_{\rm lower}\,Z_{\rm right}.}
 \tag{0.12}
\]

All three words in (0.12) are literal consecutive pieces.  Hence a third
same-return phase supplies no extra projection: it either enlarges a
corridor at its two ends, concatenates two corner corridors through the
unique lower bridge, touches only at one phase, or has disjoint phase
support.

Every corner nevertheless supplies one or two canonical quotient-edge
charges.  Equality of either charged root for two returns forces an actual
quotient-edge collision.  The common edge

\[
 1^s0^K Y0^s
\]

from `MATH_AUDIT_OCR_CRITICAL_CORNER_QUOTIENT_PACKING_20260725.md` is
exactly the left boundary charge in this theorem.

The theorem gives an exact trichotomy:

* **P:** persistent overlap, with no nonoverlap lattice point;
* **B:** nonoverlap exists, but all minimal corners are boundary endpoint
  shields;
* **I:** at least one interior minimal corner, hence the one-copy
  factorization (0.11).

This closes the same-return three-phase lane.  It does not prove a packing
asymptotic.  The residual is genuinely cross-interval: distinct actual
returns in classes B and I may have distinct canonical charged roots on
disjoint quotient supports.

## 1. The exact phase lattice

For \(0\le t<u<s\), write

\[
 A_{t,u}=(\overline T_{u-1}0)\cdots(\overline T_t0),
 \qquad
 C_{t,u}=(0S_u)\cdots(0S_{t+1}).
 \tag{1.1}
\]

The transported tail equation is

\[
 A_{t,u}R_t=R_uC_{t,u}.
 \tag{1.2}
\]

For the lattice point \((a,b)\), define the two omitted outer words

\[
 \mathcal L_a
 :=(\overline T_{a-1}0)\cdots(\overline T_00),
 \qquad \mathcal L_0:=\varnothing,
 \tag{1.3}
\]

and

\[
 \mathcal U_b
 :=(0S_{s-1})\cdots(0S_{s-b}),
 \qquad \mathcal U_0:=\varnothing.
 \tag{1.4}
\]

Their lengths are

\[
 |\mathcal L_a|=a+X_a,
 \qquad
 |\mathcal U_b|=b+Y_b.
 \tag{1.5}
\]

The corrected outer-collar ledger from the two-phase chronology audit is

\[
 B_{t,u}
 =\sum_{0\le j<t}(|T_j|+1)
  +\sum_{u<j<s}(|S_j|+1).
 \tag{1.6}
\]

Substituting (0.8) gives

\[
 B_{a,b}:=B_{a,s-b-1}
 =a+b+X_a+Y_b
 =|\mathcal L_a|+|\mathcal U_b|.
 \tag{1.7}
\]

The exact transported length difference is

\[
 \Delta_{a,b}=B_{a,b}-\Lambda.
 \tag{1.8}
\]

If \(\Delta_{a,b}\ge0\), free-monoid cancellation gives the unique word
\(Z_{a,b}\) such that

\[
 R_u=A_{a,u}Z_{a,b},
 \qquad
 R_a=Z_{a,b}C_{a,u}.
 \tag{1.9}
\]

Its net height is \(-r\), so its length must be at least \(r\).  By
(1.7)--(1.8), this is equivalent to

\[
 a+b+X_a+Y_b-\Lambda\ge a+b,
\]

which is (0.9).  Moreover

\[
 |Z_{a,b}|
 =a+b+X_a+Y_b-\Lambda.
 \tag{1.10}
\]

If \(\Delta_{a,b}<0\), cancellation instead gives the unique bridge
\(H_{a,b}\) such that

\[
 A_{a,u}=R_uH_{a,b},
 \qquad
 C_{a,u}=H_{a,b}R_a.
 \tag{1.11}
\]

Its net height is \(r\), so \(|H_{a,b}|\ge r\).  Since

\[
 |H_{a,b}|=\Lambda-a-b-X_a-Y_b,
 \tag{1.12}
\]

this is exactly (0.10).

Equation (1.2) has only the two free-monoid alternatives (1.9) and
(1.11).  Hence every lattice point satisfies exactly one of (0.9) and
(0.10); the open numerical strip between them is forbidden for an actual
PBBS staircase.

Because \(X_a\) and \(Y_b\) are nondecreasing, the set

\[
 \mathcal N
 :=\{(a,b):a,b\ge0, a+b\le s-2, X_a+Y_b\ge\Lambda\}
 \tag{1.13}
\]

is an upset in the coordinatewise order.

## 2. Minimal corners and their two predecessor bridges

Call \(c=(a,b)\in\mathcal N\) a **minimal corner** if there is no
\((a',b')\in\mathcal N\), distinct from \((a,b)\), with
\(a'\le a\) and \(b'\le b\).  Put

\[
 r=a+b,
 \qquad
 u=s-b-1,
 \qquad
 Z=Z_{a,b}.
 \tag{2.1}
\]

Since \(\Lambda>0\), the point \((0,0)\) is overlap.  Thus every minimal
corner has \(r\ge1\).

### Lemma 2.1 (left predecessor)

If \(a>0\), there is a unique word \(H_L\) such that

\[
 \boxed{\overline T_{a-1}0=ZH_L,}
 \qquad
 \operatorname {net}(H_L)=r-1.
 \tag{2.2}
\]

#### Proof

The predecessor \((a-1,b)\) is not in \(\mathcal N\), hence is in the
overlap branch.  Its phase pair is \((a-1,u)\), and its bridge satisfies

\[
 A_{a-1,u}=R_uH_L.
 \tag{2.3}
\]

The collar factorization and the corner identity (1.9) are

\[
 A_{a-1,u}=A_{a,u}(\overline T_{a-1}0),
 \qquad
 R_u=A_{a,u}Z.
 \tag{2.4}
\]

Substitution in (2.3) and left cancellation give (2.2).  Its net-height
identity follows from

\[
 -1=\operatorname {net}(\overline T_{a-1}0)
   =-r+\operatorname {net}(H_L).
\]

Uniqueness is free-monoid uniqueness.  \(\square\)

### Lemma 2.2 (right predecessor)

If \(b>0\), there is a unique word \(H_R\) such that

\[
 \boxed{0S_{u+1}=H_RZ,}
 \qquad
 \operatorname {net}(H_R)=r-1,
 \tag{2.5}
\]

where \(u+1=s-b\).

#### Proof

The predecessor \((a,b-1)\) corresponds to the phase pair \((a,u+1)\)
and is overlap.  Its bridge satisfies

\[
 C_{a,u+1}=H_RR_a.
 \tag{2.6}
\]

Now

\[
 C_{a,u+1}=(0S_{u+1})C_{a,u},
 \qquad
 R_a=ZC_{a,u}.
 \tag{2.7}
\]

Substitution in (2.6) and right cancellation give (2.5).  The net-height
calculation is

\[
 -1=\operatorname {net}(0S_{u+1})
   =\operatorname {net}(H_R)-r.
\]

Again uniqueness is literal.  \(\square\)

Write

\[
 q_c:=X_a+Y_b-\Lambda\ge0.
 \tag{2.8}
\]

Then (1.10) gives

\[
 |Z|=r+q_c.
 \tag{2.9}
\]

Every word of net \(r-1\) has length at least \(r-1\).  Therefore
(2.2) and (2.5) imply the exact lower bounds

\[
 |T_{a-1}|\ge2r+q_c-2\quad(a>0),
 \tag{2.10}
\]

\[
 |S_{s-b}|\ge2r+q_c-2\quad(b>0).
 \tag{2.11}
\]

In particular, both interior transition blocks have length at least
\(2r-2\).  These are the two-dimensional versions of the forced-jump
bound; no union over a chosen monotone scan is present.

## 3. The one-copy common-boundary factorization

Assume first that \(a,b>0\).  The two predecessor overlap inequalities
give

\[
 |\mathcal L_{a-1}|+|\mathcal U_b|
 \le\Lambda-(r-1)<\Lambda,
 \tag{3.1}
\]

and

\[
 |\mathcal L_a|+|\mathcal U_{b-1}|
 \le\Lambda-(r-1)<\Lambda.
 \tag{3.2}
\]

Consequently \(\mathcal L_a\) is a suffix of \(E\), while
\(\mathcal U_b\) is a prefix of \(E\).  The exact block recursions are

\[
 \mathcal L_a
 =(\overline T_{a-1}0)\mathcal L_{a-1}
 =ZH_L\mathcal L_{a-1},
 \tag{3.3}
\]

and

\[
 \mathcal U_b
 =\mathcal U_{b-1}(0S_{s-b})
 =\mathcal U_{b-1}H_RZ.
 \tag{3.4}
\]

Their total length exceeds \(|E|\) by

\[
 |\mathcal L_a|+|\mathcal U_b|-\Lambda
 =B_{a,b}-\Lambda
 =|Z|.
 \tag{3.5}
\]

Thus the suffix \(\mathcal L_a\) and prefix \(\mathcal U_b\) overlap
inside \(E\) in exactly \(|Z|\) letters.  Equations (3.3)--(3.4) show
that this common word is \(Z\): it is the prefix of \(\mathcal L_a\)
and the suffix of \(\mathcal U_b\).  Removing the duplicate display of
that one physical word gives

\[
 \boxed{
 E=\mathcal U_{b-1}H_RZH_L\mathcal L_{a-1}.}
 \tag{3.6}
\]

Every letter of \(E\) occurs exactly once on the right side of (3.6).
The net-height audit is

\[
 -(b-1)+(r-1)-r+(r-1)-(a-1)=0.
 \tag{3.7}
\]

This agrees with the fact that \(E\) is balanced.

There are two exact boundary versions.

### Lemma 3.1 (right endpoint shield)

If \(a=0<b\), then

\[
 \boxed{E=\mathcal U_{b-1}H_R,}
 \tag{3.8}
\]

and \(Z\) is a prefix of \(R_0\).

#### Proof

Here \(\mathcal L_0\) is empty, so (1.8) gives

\[
 |\mathcal U_b|=\Lambda+|Z|.
\]

By (3.4),

\[
 \mathcal U_b=\mathcal U_{b-1}H_RZ.
\]

This is a prefix of \(U=ER_0\).  The first two factors have total length
\(\Lambda\), proving (3.8); the following word \(Z\) is therefore a
prefix of \(R_0\).  \(\square\)

### Lemma 3.2 (left endpoint shield)

If \(b=0<a\), then

\[
 \boxed{E=H_L\mathcal L_{a-1},}
 \tag{3.9}
\]

and \(Z\) is a suffix of \(R_s(0S_s)\).

#### Proof

Now \(\mathcal U_0\) is empty and

\[
 |\mathcal L_a|=\Lambda+|Z|.
\]

Equation (3.3) gives

\[
 \mathcal L_a=ZH_L\mathcal L_{a-1}.
\]

This word is a suffix of \(V=R_s(0S_s)E\).  The last two factors have
total length \(\Lambda\), so they equal \(E\), while the preceding
\(Z\) is a suffix of \(R_s(0S_s)\).  \(\square\)

Thus an interior corner puts \(Z\) inside the balanced carrier once,
whereas a boundary corner moves \(Z\) into exactly one endpoint terminal
corridor.  These are exhaustive.

## 4. Canonical quotient-edge charges

Every minimal corner supplies an actual edge of the return support which
contains its corner factorization in a canonical location.

If \(a>0\), the tail identity at phase \(a-1\) is

\[
 \overline T_{a-1}0R_{a-1}=R_a0S_a.
 \tag{4.1}
\]

Using (2.2), the root at phase \(a\) is therefore

\[
 \boxed{
 D_a=P_a1ZH_LR_{a-1}.}
 \tag{4.2}
\]

Define the left corner charge by

\[
 \kappa_L(c):=e_{D_a}.
 \tag{4.3}
\]

This charge is intrinsic to the root.  The word \(P_a1\) reaches the
global maximum for the first time.  The word \(\overline T_{a-1}\)
stays at or below that maximum and returns to it.  After its following
zero, the word \(R_{a-1}\), now based one level lower, never reaches the
maximum.  Hence \(\overline T_{a-1}\) is exactly the segment from the
first visit to the last visit to the global maximum of \(D_a\).  In
particular its length is recoverable from the charged root without a
choice among staircase positions.

If \(b>0\), put \(u+1=s-b\).  Equation (2.5) gives

\[
 \boxed{
 D_{u+1}=P_{u+1}1R_{u+1}H_RZ.}
 \tag{4.4}
\]

Define

\[
 \kappa_R(c):=e_{D_{u+1}}=e_{D_{s-b}}.
 \tag{4.5}
\]

Here \(S_{u+1}\), and hence the terminal factor \(0S_{u+1}=H_RZ\), is
the canonical terminal forest in the first-maximum factorization of
\(D_{u+1}\).

Both charged edges lie in the full quotient support

\[
 Q(D_0,s)=\{e_{D_0},e_{D_1},\ldots,e_{D_{s+1}}\}.
 \tag{4.6}
\]

Therefore two return intervals whose left charged roots agree, or whose
right charged roots agree, have a literal common quotient edge.

For a single-valued charge, order the finite set of minimal corners
lexicographically, choose its first member \(c=(a,b)\), and use
\(\kappa_L(c)\) when \(a>0\), otherwise \(\kappa_R(c)\).  Since
\(a+b>0\), this always exists.  On every quotient-edge-disjoint family
this charge map is injective.  This removes all raw multiplicity from
choosing a transported phase pair, but it does not by itself bound the
number of possible charged roots.

In the audited critical-corner construction, the left boundary corner is

\[
 a=t+1,\qquad b=0,
\]

and (4.2) is exactly

\[
 D_{t+1}=1^s0^K Y0^s.
 \tag{4.7}
\]

Thus the previously isolated common edge is the sparse specialization of
the general charge (4.3).  The symmetric right boundary corner also gives
the root \(D_u=1^s0^sY0^K\) in that construction.

## 5. Nested nonoverlap phases only enlarge the same corridor

Let \(c=(a,b)\in\mathcal N\), set \(u=s-b-1\), and let

\[
 q=(A,B)\in\mathcal N,
 \qquad A\ge a,\quad B\ge b,\quad A+B\le s-2.
 \tag{5.1}
\]

Put \(U_q=s-B-1\).  Define

\[
 A_{a,A}=(\overline T_{A-1}0)\cdots(\overline T_a0)
 \tag{5.2}
\]

and

\[
 C_{U_q,u}=(0S_u)(0S_{u-1})\cdots(0S_{U_q+1}),
 \tag{5.3}
\]

with either word empty when its endpoints agree.  Repeated use of the
one-step tail identity gives

\[
 \boxed{
 Z_{A,B}=A_{a,A}\,Z_{a,b}\,C_{U_q,u}.}
 \tag{5.4}
\]

Indeed increasing \(a\) by one prefixes \(\overline T_a0\) to the
corridor, while increasing \(b\) by one suffixes \(0S_u\).  Left and
right additions commute because they are literal concatenations at
opposite ends.

Likewise, for every intermediate phase \(a\le v\le u\),

\[
 \boxed{
 R_v=A_{a,v}Z_{a,b}C_{v,u}.}
 \tag{5.5}
\]

This follows by cancellation from the transported equations, and its
native legality follows from the same corridor bounds as the endpoint
phases.  Thus phases inside one chart retain the same \(Z\), while phases
outside it only perform the two end additions in (5.4).

## 6. The interlaced rectangle identity

Let

\[
 c=(a,b),\qquad c'=(a',b')
 \tag{6.1}
\]

be two distinct minimal corners, ordered so that \(a<a'\).  Minimality
forces

\[
 b>b'.
 \tag{6.2}
\]

The lower cross

\[
 p=(a,b')
 \tag{6.3}
\]

is properly coordinatewise below each corner, so it is overlap.  Let
\(H_p\) be its unique bridge.  Its net height is

\[
 \operatorname {net}(H_p)=a+b'.
 \tag{6.4}
\]

Put

\[
 u=s-b-1,
 \qquad
 u'=s-b'-1,
 \tag{6.5}
\]

so \(u<u'\).  The upper cross

\[
 q=(a',b)
 \tag{6.6}
\]

is a valid transported pair exactly when

\[
 a'+b\le s-2,
 \tag{6.7}
\]

equivalently \(a'<u\).  In that case it belongs to \(\mathcal N\) by
upward closure.

### Theorem 6.1 (rectangle concatenation)

Under (6.7),

\[
 \boxed{
 Z_{a',b}=Z_{a',b'}\,H_p\,Z_{a,b}.}
 \tag{6.8}
\]

The three displayed factors are literal consecutive words and are not
duplicated.

#### Proof

Define the cross collars

\[
 A^\times=(\overline T_{a'-1}0)\cdots(\overline T_a0),
 \tag{6.9}
\]

\[
 C^\times=(0S_{u'})(0S_{u'-1})\cdots(0S_{u+1}).
 \tag{6.10}
\]

At the lower overlap point \(p=(a,b')\),

\[
 A_{a,u'}=R_{u'}H_p,
 \qquad
 C_{a,u'}=H_pR_a.
 \tag{6.11}
\]

The corner \(c'=(a',b')\) gives

\[
 R_{u'}=A_{a',u'}Z_{a',b'},
 \tag{6.12}
\]

while

\[
 A_{a,u'}=A_{a',u'}A^\times.
 \tag{6.13}
\]

Equations (6.11)--(6.13) and left cancellation yield

\[
 A^\times=Z_{a',b'}H_p.
 \tag{6.14}
\]

Similarly, the corner \(c=(a,b)\) gives

\[
 R_a=Z_{a,b}C_{a,u},
 \tag{6.15}
\]

and

\[
 C_{a,u'}=C^\times C_{a,u}.
 \tag{6.16}
\]

Equations (6.11), (6.15), and (6.16), followed by right cancellation,
give

\[
 C^\times=H_pZ_{a,b}.
 \tag{6.17}
\]

Finally, at \(c\),

\[
 R_u=A_{a,u}Z_{a,b}
     =A_{a',u}A^\times Z_{a,b}.
\]

Insert (6.14):

\[
 R_u=A_{a',u}Z_{a',b'}H_pZ_{a,b}.
\]

The unique nonoverlap corridor at \(q=(a',b)\) is therefore the word in
(6.8).  The net check is

\[
 -(a'+b')+(a+b')-(a+b)=-(a'+b),
\]

as required.  \(\square\)

If

\[
 a'+b=s-1,
 \tag{6.18}
\]

then \(a'=u\).  The two phase ranges meet only at the single phase
\(v=u\).  There is no valid upper-cross pair, but the same cancellation
still gives the exact degenerate rectangle formula

\[
 \boxed{R_u=Z_{a',b'}H_pZ_{a,b}.}
 \tag{6.19}
\]

Indeed (6.14) remains valid and now \(A^\times=A_{a,u}\), so
\(R_u=A_{a,u}Z_{a,b}=Z_{a',b'}H_pZ_{a,b}\).  Thus even the touching
case is a literal concatenation at the unique common phase.  If
\(a'+b\ge s\), then \(a'>u\), and the two phase ranges are disjoint.

For a chain of minimal corners

\[
 c_i=(a_i,b_i),qquad
 a_1<\cdots<a_k,qquad b_1>\cdots>b_k,
 \tag{6.20}
\]

suppose that the top cross \((a_k,b_1)\) is valid.  Let \(H_i\) be the
bridge at the lower cross \((a_i,b_{i+1})\).  Induction using (6.8)
gives the exact atlas formula

\[
 \boxed{
Z_{a_k,b_1}
 =Z_{c_k}H_{k-1}Z_{c_{k-1}}\cdots H_1Z_{c_1}.}
 \tag{6.21}
\]

For clarity, the induction uses the following generalized form of
Theorem 6.1: its cancellation proof requires only that the lower cross be
overlap and that the two side points and valid upper cross be nonoverlap;
the upper point need not itself be minimal.  At each induction step these
conditions follow from minimality of the original corners and upward
closure of \(\mathcal N\).  Thus no unstated minimality assumption is used
in (6.21).

Thus every genuinely interlaced finite collection is an alternating
concatenation of minimal corner corridors and lower overlap bridges.  It
does not create a new intersection condition on one already counted
physical corridor.

## 7. The exact P/B/I residual

The phase lattice yields the following exhaustive trichotomy.

### P. Persistent overlap

The nonoverlap set \(\mathcal N\) is empty.  Equivalently,

\[
 \boxed{
 X_a+Y_b\le\Lambda-2(a+b)
 \quad\text{for every }a+b\le s-2.}
 \tag{7.1}
\]

Taking any point with \(a+b=s-2\) and using \(X_a,Y_b\ge0\) gives the
necessary bound

\[
 \Lambda\ge2(s-2).
 \tag{7.2}
\]

Statement (7.1), not merely (7.2), is the exact characterization.

### B. Boundary-shield onset

The set \(\mathcal N\) is nonempty, but every minimal corner lies on an
axis.  Each such corner has one of the exact forms

\[
 E=\mathcal U_{b-1}H_R,qquad Z\preceq R_0,
 \tag{7.3}
\]

or

\[
 E=H_L\mathcal L_{a-1},
 \qquad Z\text{ is a suffix of }R_s(0S_s).
 \tag{7.4}
\]

Here \(\preceq\) denotes literal prefix.  This is the exact one-sided
endpoint-shield family.  Both boundary corners may occur in the same
return.

### I. Interior one-copy onset

At least one minimal corner has \(a,b>0\).  Every such corner has the
literal disjoint factorization

\[
 E=\mathcal U_{b-1}H_RZH_L\mathcal L_{a-1}.
 \tag{7.5}
\]

All incomparable interior charts are governed by the rectangle law
(6.8), and every finite interlaced atlas is the alternating concatenation
(6.21).

Classes P, B, and I are pairwise disjoint and exhaustive.  A boundary
corner may coexist with an interior corner; by definition such a return
belongs to I.

## 8. Proved boundary

The following statements are now proved for every genuine positive-
overlap zero-winding return, with no asymptotic or genericity hypothesis.

1. All transported phase pairs are classified by the two additive
   cumulants \(X_a,Y_b\) through the exact alternatives (0.9)--(0.10).
2. Every minimal nonoverlap corner has one or two unique predecessor
   bridges and the exact transition identities (2.2), (2.5).
3. An interior corner cuts the physical common boundary into the five
   disjoint pieces (3.6), with the common corridor counted once.
4. Boundary corners are exactly the two endpoint-shield factorizations
   (3.8)--(3.9).
5. Every corner has canonical quotient-edge charges (4.2), (4.4).
   Equality of a charged root is a genuine edge collision, and a packing
   admits an injective single-valued charge.
6. Nested phases only add literal collars at the two ends of the same
   corridor.  Incomparable interlaced corners satisfy the exact rectangle
   concatenation (6.8); a finite atlas satisfies (6.21).

Consequently there is no unresolved same-return two/three-phase
noncommutativity.  The phase atlas is a free-monoid concatenation atlas.

What remains unproved is a cross-return packing theorem.  In the critical
window \(s\asymp\sqrt m\), one must show that actual class-B and class-I
returns cannot supply

\[
 \Theta(\operatorname {Cat}_m/\sqrt m)
\]

pairwise quotient-edge-disjoint intervals with pairwise distinct
canonical charges.  The theorem above removes phase-pair multiplicity and
isolates the exact words which such a residual family must carry, but it
does not prove that their number is little-oh.  No coefficient-one claim
is made.
