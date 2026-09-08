# RETRACTED packet-escape claim: the NAE colouring leaves invariant mixed packets

**Correction.**  The component-colouring theorem below is correct, but its
interpretation as an escape from the packet obstruction is false.  For the
prefix \(P=10\), the suspended target is fixed by \(\tau=(2\ 3)\).
Consequently a mixed choice of canonical and transposed owners still gives
three owners of the *same* target.  The complete corrected theorem is in
GLOBAL_SEED_NATIVE_CUBE_INVARIANT_OBSTRUCTION_20260725.md.

What remains valid below is:

* the explicit NAE component colouring;
* the exact-factor child construction;
* the component-support lower bound.

What is retracted is the assertion that NAE destroys the actual packet.
It destroys only the all-left and all-right presentations of that packet.

Date: 2026-07-25

Method: pure mathematics only. No search, computation, solver, or external
black box is used.

## 0. Outcome

The global edit barrier in
FRACTIONAL_PACKET_GLOBAL_SEED_MATCHING_20260725.md is real but is not a
self-regenerating obstruction inside the canonical
\((2\ 3)\)-interaction cube.

Let

\[
 A=11110000,\qquad B=11101000,\qquad D=1100,
\]

so the three collision variants are

\[
 A,\qquad B,\qquad DD.
\]

For every Dyck prefix \(U\) and suffix \(V\), the canonical rows

\[
 UAV,\qquad UBV,\qquad UDDV
 \tag{0.1}
\]

form one three-owner depth-one packet seed.

There is an explicit two-colouring of the canonical
\((2\ 3)\)-interaction components for which every triple (0.1) is
nonmonochromatic. Choosing the left or right side according to this
colouring gives a genuine exact wreath factor \(F_m^\star\).

Consequently:

1. no full canonical triple (0.1) survives in \(F_m^\star\);
2. no full \((2\ 3)\)-transposed copy of a triple survives either;
3. one may assign depth-one quota two to every canonical and transposed
   seed target simultaneously;
4. the exact row distance can be chosen to satisfy
   \[
    L_m+H_m\le d(F_m^\star,F_m^{\rm MSW})
             \le\frac12\operatorname{Cat}_m,
    \tag{0.2}
   \]
   where
   \[
    \frac{L_m}{\operatorname{Cat}_m}\to\frac{275}{19321},
    \qquad
    \frac{H_m}{\operatorname{Cat}_m}
    \to\frac{4352}{1238769}.
   \]

Thus exact middle ownership does permit a global move beyond the
\(1.4233\%\) seed-transversal barrier. There is no compensating theorem
saying that a switched seed must reappear as its complete transposed seed.

This does **not** prove \((\mathrm{FSP}_A)\). Mixed-side rows may create
unrelated packet resources, and the theorem does not bound the full packet
LP of \(F_m^\star\).

## 1. The audited component hierarchy

Let \(\tau=(2\ 3)\). The canonical interaction components between
\(F_m^{\rm MSW}\) and \(\tau F_m^{\rm MSW}\) are

\[
 \mathcal C_{j,R}
 =\{E(XR):X\in\mathcal A_j\},
 \tag{1.1}
\]

where

\[
 \mathcal A_j
 =
 \{1u0:u\in\mathcal D_{j+1}\}
 \mathbin{\dot\cup}
 \{10\,1v0:v\in\mathcal D_j\}.
 \tag{1.2}
\]

The first set in (1.2) consists of all primitive Dyck words of semilength
\(j+2\). The second consists of \(10\) followed by a primitive Dyck word
of semilength \(j+1\).

Hence the component label of a Dyck root has the following direct
first-return description. Write its primitive-component sequence as

\[
 Q_1Q_2\cdots.
\]

* If \(Q_1\ne10\) has semilength \(q_1\ge2\), then
  \[
   j=q_1-2,
  \]
  and \(R\) is the suffix after \(Q_1\).
* If \(Q_1=10\), and \(Q_2\) has semilength \(q_2\), then
  \[
   j=q_2-1,
  \]
  and \(R\) is the suffix after \(Q_1Q_2\).

This is merely (1.2) read through unique primitive factorization.

Every component has equally many left and right wreaths and covers the same
middle sets on both sides. Therefore any independent choice of its
canonical side or its \(\tau\)-transposed side produces an exact factor.
The audited canonical hierarchy also has

\[
 F_m^{\rm MSW}\cap\tau F_m^{\rm MSW}=\varnothing,
 \tag{1.3}
\]

so the number of canonical rows switched is exactly the row distance of
the resulting child.

## 2. Component colouring

For a Dyck word \(R\), let

\[
 a(R)=\#\{\text{primitive components of }R\text{ equal to }A\}.
 \tag{2.1}
\]

Put

\[
 \gamma_j=\left\lfloor\frac j2\right\rfloor\pmod2
 \tag{2.2}
\]

and colour the component \(\mathcal C_{j,R}\) by

\[
 \boxed{
  \chi(\mathcal C_{j,R})
  =a(R)+\gamma_j\pmod2.
 }
 \tag{2.3}
\]

### Theorem 2.1 -- every seed triple is NAE

For every Dyck \(U,V\), the components containing the three rows in (0.1)
are not all the same colour.

#### Proof

First suppose that the component-defining initial primitive block or blocks
lie entirely inside \(U\). This happens whenever

* the first primitive component of \(U\) has semilength at least two; or
* the first component is \(10\) and \(U\) contains a second primitive
  component.

All three roots then have the same index \(j\). After the fixed
component-defining prefix, their suffixes have the form

\[
 R_0AV,\qquad R_0BV,\qquad R_0DDV.
\]

Their \(A\)-counts are

\[
 k+1,\qquad k,\qquad k
\]

for one integer \(k\). Since the same \(\gamma_j\) is added to all three,
their component colours have the pattern

\[
 1-c,\qquad c,\qquad c
\]

in some order, and are nonmonochromatic.

There are exactly two exceptional prefixes.

If \(U\) is empty, the \(A\)- and \(B\)-rows lie in
\(\mathcal C_{2,V}\), whereas the \(DD\)-row lies in
\(\mathcal C_{0,DV}\). Since \(D\ne A\),

\[
 a(DV)=a(V),
\]

and

\[
 \gamma_2=1\ne0=\gamma_0.
\]

Thus the two component colours differ.

If \(U=10\), the \(A\)- and \(B\)-rows lie in
\(\mathcal C_{3,V}\), whereas the \(DD\)-row lies in
\(\mathcal C_{1,DV}\). Again \(a(DV)=a(V)\), while

\[
 \gamma_3=1\ne0=\gamma_1.
\]

These colours also differ. The cases exhaust all Dyck prefixes \(U\).
\(\square\)

## 3. The exact child factor

For every component, choose its transposed side when \(\chi=1\) and its
canonical side when \(\chi=0\). Component switching gives an exact factor,
call it \(F_m^{(1)}\).

Complementing every component choice also gives an exact factor
\(F_m^{(0)}\). The two switch supports partition the \(t\) canonical rows,
so one of them has row distance at most \(t/2\). Call that child
\(F_m^\star\).

For a seed triple (0.1), Theorem 2.1 gives at least one canonical-side
component and at least one transposed-side component. Hence not all three
canonical rows occur in the child. Also not all three transposed rows
occur. Since coordinate transposition carries their common target to the
common target of the three transposed rows, both complete designated
three-owner packets are destroyed.

The baseline lower bound in (0.2) follows from the disjoint global matching
of the preceding report. Every one of its \(L_m\) triples is
nonmonochromatic, so the switch support meets each triple in at least one
canonical row. Since those triples are row-disjoint, at least \(L_m\) rows
are switched. The next lemma proves the additional \(H_m\) term forced by
whole-component switching.

### Lemma 3.1 -- a strict legal-component premium

Let

\[
 U_0(z)
 =
 \frac1{1-(1+z^2)\bigl(zC(z)-z^2-2z^4\bigr)}
 \tag{3.1}
\]

be the clean-word series from the global matching report, and put

\[
 H_m=[z^{m-4}]U_0(z).
 \tag{3.2}
\]

Every set of canonical \((2\ 3)\)-components meeting all \(L_m\) matching
triples has total row size at least

\[
 L_m+H_m.
 \tag{3.3}
\]

Moreover,

\[
 \frac{H_m}{\operatorname{Cat}_m}
 \longrightarrow
 \frac{4352}{1238769}.
 \tag{3.4}
\]

#### Proof

The ordinary row-disjoint matching gives a component-cover dual which
assigns weight one to every matching triple: a component of \(s\) rows
meets at most \(s\) such triples.

Increase the dual weight from one to two on the special top-level triples

\[
 \{AV,BV,DDV\},
 \tag{3.5}
\]

where \(V\) contains no \(A\), no \(B\), no consecutive \(D,D\), and does
not begin in \(D\).

For such a \(V\), the component \(\mathcal C_{2,V}\) contains the two
selected rows \(AV,BV\). Its other five canonical rows have no active
marker and belong to no recursive matching triple. The component
\(\mathcal C_{0,DV}\) contains the selected row \(DDV\); its other row is
\(1010DV\), which has no active marker because \(V\) does not begin in
\(D\). Thus both components meet no other matching triple. Their sizes are
seven and two, respectively, so increasing the special edge weight to two
respects both component capacities. Different \(V\)'s give different
components.

The number of marker-free \(V\)'s not beginning in \(D\) equals the number
not ending in \(D\), by reversing their primitive-component sequences.
The latter are exactly the clean words counted by \(U_0\). Hence there are
\(H_m\) special triples, and the component-cover dual has value
\(L_m+H_m\). This proves (3.3).

Write

\[
 d=\frac{1113}{2048},
 \qquad d_1=\frac{17}{32}.
\]

At \(s=\sqrt{1-4z}\),

\[
 U_0(z)=d^{-1}-d_1d^{-2}s+O(s^2).
\]

Square-root coefficient comparison with \(C(z)=2-2s+O(s^2)\), including
the four-step coefficient shift in (3.2), gives

\[
 \frac{H_m}{\operatorname{Cat}_m}
 \longrightarrow
 4^{-4}\frac{d_1}{2d^2}
 =\frac{4352}{1238769}.
\]

This proves (3.4). \(\square\)

## 4. Quota-two budget

The number of contexts \(U,V\) in (0.1) is

\[
 \sum_{u=0}^{m-4}
 \operatorname{Cat}_u\operatorname{Cat}_{m-4-u}
 =\operatorname{Cat}_{m-3}.
 \tag{4.1}
\]

There are therefore at most

\[
 2\operatorname{Cat}_{m-3}
 \tag{4.2}
\]

distinct targets among all canonical seed targets and all their
\(\tau\)-transposes.

At depth one the number of quota-two targets is

\[
 \rho_1=W-N_1
 =\frac{2W}{m+2}
 =\frac{2(2m+1)}{m+2}\operatorname{Cat}_m.
 \tag{4.3}
\]

For \(m\ge2\),

\[
 2\operatorname{Cat}_{m-3}
 <2\operatorname{Cat}_m
 <\rho_1.
 \tag{4.4}
\]

Thus one balanced depth-one quota vector may assign quota two to every
target in (4.2), with the remaining upper quotas placed arbitrarily.

Under this quota choice, two surviving owners from an NAE triple are not
the designated packet: packet size is three. Hence the colouring really
eliminates every complete old or complete transposed packet used by the
seed argument.

## 5. Exact boundary of the escape theorem

The theorem eliminates the entire canonical/transposed seed certificate
inside one legal exact-factor cube. It does not assert that a seed target
has no other owners, nor that a mixed collection of new rows cannot form a
different packet. It also says nothing about deeper ranks.

Accordingly, the next required quantity is the packet-cover value generated
by **mixed-side** owner sets in \(F_m^\star\). Any global expansion theorem
must use those mixed collisions; it cannot count only the canonical seed
and its transposed image.

## 6. Adversarial self-audit

1. **Two owners may share one component.** In the exceptional cases
   \(U=\varnothing\) and \(U=10\), the \(A\)- and \(B\)-rows are in the same
   component. The proof uses their common colour and compares it with the
   \(DD\)-component.
2. **NAE alone would not kill quota-one pairs.** Section 4 explicitly
   assigns quota two to all designated old and transposed seed targets.
3. **The quota budget counts contexts, not assumed-distinct resources.**
   Coincident targets only reduce the number of required upper quotas.
4. **The exact-factor property is automatic.** No partial leave or
   completion is used; every component side choice partitions the same
   middle sets.
5. **Mixed packets remain open.** The result is a certificate-escape
   theorem, not a proof of \((\mathrm{FSP}_A)\).
