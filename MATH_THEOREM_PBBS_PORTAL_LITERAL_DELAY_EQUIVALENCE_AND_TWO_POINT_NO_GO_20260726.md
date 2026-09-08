# PBBS portal walks and literal delay: exact residence equivalence and the two-point no-go

Date: 2026-07-26

Method: pure mathematics only.  This note incorporates the correction in
`MATH_AUDIT_PBBS_PORTAL_TREE_CHRONOLOGY_NOT_LITERAL_WORD_20260726.md`.

## 0. Outcome

The portal-tree walk does not solve the literal contiguous-OR problem.  Its
portal cost is nevertheless harmless and can be factored at \(o(W)\) cost.
The surviving obstruction is exactly the old Gaussian PBBS residence gate.

Put

\[
 N=2m+1,\qquad
 W=\binom{2m+1}m=N B,
 \qquad B=\operatorname {Cat}_m,                    \tag{0.1}
\]

and let

\[
                         H=\lceil A\sqrt m\rceil    \tag{0.2}
\]

for fixed \(A>0\).  Let \(P_m\) be the physical PBBS step-two factor, and
let \(\nu_H(P_m)\) be the maximum number of pairwise physical-edge-disjoint
short coordinate-residence intervals of duration at most \(H\).  Let
\(\overline\nu_H\) be the corresponding long-cycle quotient packing.

The exact conclusions are these.

1. Every required PBBS window destroyed at a portal may be replaced by the
   established one-cut literal dominance chart of length at most \(4H-1\).
   Bridge/backtracking windows that are not PBBS witnesses are discarded,
   not counted as targets.  Since the portal tree has at most \(2B\) portal
   endpoints, all portal-specific required targets cost
   \[
                         O(HB)=O(W/\sqrt m)=o(W).    \tag{0.3}
   \]
   Immediate backtracking in the chronology is therefore not a new
   coefficient-one obstruction.

2. The portal set cannot materially improve the internal delay problem.
   If \(D\) is the set of portal cuts and \(|D|=p=O(B)\), and
   \(\nu_H(P_m;D)\) is the largest edge-disjoint short-residence family
   avoiding all portal edges, then
   \[
   \boxed{
                         \nu_H(P_m)-p
                   \le\nu_H(P_m;D)\le\nu_H(P_m).}   \tag{0.4}
   \]
   Because the critical physical scale is \(B\sqrt m\), the subtraction
   \(p=O(B)\) is negligible.

3. Within the complete established delay/cut/dominance architecture, the
   portal walk has an \(o(W)\)-overhead literal factorization if and only if
   the same vanishing residence condition required before the portal
   construction holds:
   \[
   \boxed{
     \nu_H(P_m)=o_A(B\sqrt m)
     \quad\Longleftrightarrow\quad
     \overline\nu_H=o_A(B/\sqrt m).}                \tag{0.5}
   \]
   Here the equivalence between the two displayed packing conditions is
   the established PBBS deck reduction, after removal of the negligible
   short quotient cycles.  The portal modification changes neither
   direction of the compiler criterion.

4. There is a quantitative no-go.  On retained quotient cycles let \(E_H\)
   be the eligible return starts,
   \[
     R_H=|E_H|,
     \qquad
     \mathcal C_H=\sum_{t=1}^{H+1}
             |E_H\cap\tau^{-t}E_H|.                \tag{0.6}
   \]
   If, along a subsequence,
   \[
     R_H\ge c_A{B\over H},
     \qquad
     \mathcal C_H\le C_A R_H,                       \tag{0.7}
   \]
   then every additive delay-\(H\) portal factorization has
   \(\Omega_A(W)\) auxiliary literal cost.  In particular it cannot prove
   coefficient one.

5. Conversely, at critical start density \(R_H=\Omega_A(B/H)\), an
   \(o(W)\) factorization through this architecture requires the genuinely
   dynamical clustering law
   \[
   \boxed{
                         \mathcal C_H/R_H\longrightarrow\infty.}           \tag{0.8}
   \]

Thus the delay-\(H\) portal factorization is neither solved nor independently
refuted for PBBS.  It is rigorously reduced back to the two-time return
correlation theorem (0.8).  The portal-tree chronology provides no shortcut
around that theorem.  A literal construction avoiding (0.5) must use a
genuinely in-place baseline replacement outside the additive
cut/dominance model.

## 1. The literal interface and why the portal walk is insufficient

Let

\[
                         X_0,X_1,\ldots,X_{L-1}      \tag{1.1}
\]

be a Johnson chronology.  Owner states themselves can literally represent
upper unions, but no OR containing a rank-\(m\) owner letter can equal a
proper lower target.

The standard delay transform uses

\[
                         A_i=\bigcap_{j=0}^H X_{i+j}.           \tag{1.2}
\]

The identity

\[
                         X_i=\bigcup_{j=i}^{i+H}A_j             \tag{1.3}
\]

requires two-sided delay-\(H\) residence: a coordinate may not leave and
return, or enter and leave, inside the relevant window.  A short positive
residence gives two indices at which (1.3) loses the coordinate even though
it belongs to the intended owner target.

The portal repair excursion \(PP^{-1}\) has immediate returns and is
maximally unsafe for (1.2).  Therefore chronology-window coverage does not
imply literal-OR coverage.

## 2. Portal windows have a linear literal chart

The preceding failure does not force a quadratic portal cost for the
required PBBS targets.  The proved one-cut dominance-staircase theorem
applies to an arbitrary Johnson cut.  For every cut and every \(H\) with
\(2H\le m+1\), it supplies

* a \((2H-1)\)-letter lower staircase chart for every floor-correct crossing
  intersection of depth at most \(H\); and
* a \(2H\)-owner upper chart for every crossing union.

The concatenated chart has length

\[
                         4H-1.                       \tag{2.1}
\]

Every displayed object is an actual nonzero set-valued letter and every
target is a literal contiguous OR.

Let \(c_m\) be the number of physical PBBS components.  The portal tree of
the chronology theorem has at most

\[
                         p\le2(c_m-1)\le2B           \tag{2.2}
\]

portal endpoints.  Omit the unsafe forward/backward repair excursions from
the literal compiler.  Instead concatenate the literal words constructed
on the PBBS component pieces and append one chart (2.1) at every portal cut
whose PBBS crossing targets are to be retained.  Bridge and reverse-trace
windows introduced only by the portal chronology are not part of the PBBS
witness catalogue and are simply discarded.  This is a concatenation of
literal set-valued words; it is not an assertion that the concatenated
letters form a Johnson walk or that every incidental window of the portal
walk is reproduced.  The total portal-specific cost is at most

\[
                         (4H-1)p\le2(4H-1)B=O(HB).   \tag{2.3}
\]

Equation (0.3) follows from \(W=(2m+1)B\) and \(H=\Theta_A(\sqrt m)\).
Thus the audit's immediate-return objection is repaired locally, but only at
the portals.

## 3. Internal short residences survive the portal selection

Let \(\mathcal I_H\) be the family of physical short-residence intervals on
the PBBS factor.  Choose one incident physical PBBS edge at every portal
endpoint at which a component word is cut, and call the resulting set
\(D\).  Repeated choices can only reduce \(|D|\), so \(|D|\le p\).  Put

\[
 \mathcal I_H(D)=\{I\in\mathcal I_H:I\cap D=\varnothing\},
 \qquad
 \nu_H(P_m;D)=\nu(\mathcal I_H(D)).                 \tag{3.1}
\]

### Theorem 3.1 (portal deletion changes packing by at most its size)

For every edge set \(D\),

\[
                         \nu_H(P_m)-|D|
                  \le\nu_H(P_m;D)\le\nu_H(P_m).    \tag{3.2}
\]

#### Proof

Take a maximum pairwise edge-disjoint family
\(\mathcal P\subseteq\mathcal I_H\).  Because its intervals are
edge-disjoint, a fixed portal edge belongs to at most one member of
\(\mathcal P\).  Hence at most \(|D|\) members of \(\mathcal P\) meet
\(D\).  Deleting those members leaves an edge-disjoint subfamily of
\(\mathcal I_H(D)\) of size at least \(\nu_H(P_m)-|D|\).  The other
inequality follows from inclusion. \(\square\)

For the portal tree, \(|D|=O(B)\).  Relative to the critical scale,

\[
                         {|D|\over B\sqrt m}=O(m^{-1/2})=o(1).             \tag{3.3}
\]

Thus no choice of one or boundedly many portal cuts per PBBS component can
turn a critical residence packing into a vanishing one.

## 4. Upper factorization ledger

Cut every remaining short residence by a minimum circular interval
transversal.  On each safe linear PBBS path use the endpoint-capped erosion
factorization.  At every cut use the literal dominance chart from Section 2.
The established deterministic ledger is

\[
 L_H
 \le W+2HB+2(5H-1)\nu_H(P_m).                       \tag{4.1}
\]

Adding the portal charts changes only the constant multiplying \(HB\):

\[
 \boxed{
 L_H^{\rm portal}
 \le W+C_0HB+C_1H\nu_H(P_m)}                        \tag{4.2}
\]

for absolute constants \(C_0,C_1\).

At Gaussian depth, \(HB=O(W/\sqrt m)=o(W)\).  Therefore

\[
                         H\nu_H(P_m)=o(W)            \tag{4.3}
\]

is sufficient for an \(o(W)\)-overhead literal portal factorization.
The established PBBS deck reduction, after removal of the negligible short
quotient cycles, converts (4.3) to

\[
                         H\overline\nu_H=o(B),       \tag{4.4}
\]

up to the already proved negligible short-quotient-cycle term.  This is
precisely (0.5).

## 5. Lower bound inside the additive delay/cut architecture

The upper ledger does not by itself prove necessity for an arbitrary
literal word.  Necessity is exact for the established additive
delay/cut/dominance architecture, including arbitrary clustering of nearby
cuts.

Let \(\mathfrak S_H\) be its minimum quotient clustered-seam cost in the
absence of the extra portal cuts.  The proved packing--cluster equivalence
gives, after the established sub-Gaussian-height deletion,

\[
 \boxed{
                         \mathfrak S_H=o_A(B)
             \quad\Longleftrightarrow\quad
                         H\overline\nu_H=o_A(B).}    \tag{5.1}
\]

The portal cuts need not be deck-invariant, so one may not merely divide
their number by \(N\).  The correct argument is physical.  Fix
\(a\in(0,A)\), and choose a maximum quotient-edge-disjoint family
\(\overline{\mathcal P}^{\ge a}\) of eligible intervals whose starting
root has height at least \(a\sqrt m\).  Every interval is nonwrapping on a
retained quotient cycle.  The PBBS deck-lift lemma therefore gives all
\(N\) mutually physical-edge-disjoint spatial lifts of every member, and
disjoint quotient traces give disjoint lift families.  Thus

\[
 |\mathcal P^{\ge a}|=N\overline\nu_H^{\ge a}.     \tag{5.2}
\]

Delete the members meeting the free portal-cut set \(D\).  Since
\(\mathcal P^{\ge a}\) is physical-edge-disjoint, at most \(|D|\) members
are deleted.  Apply the physical version of the cluster-span argument to
the survivors.  Their traces have length at least
\(\gamma_{a,A}H\), so a cluster of span \(S\) assigned \(t\) surviving
intervals obeys

\[
                         S\ge\gamma_{a,A}H(t-2).
                                                               \tag{5.3}
\]

Consequently the nonportal seam cost is at least

\[
 \boxed{
   c_{a,A}H\bigl(N\overline\nu_H^{\ge a}-|D|\bigr)_+.}
                                                               \tag{5.4}
\]

This is the needed non-symmetric portal estimate.  Because
\(|D|=O(B)\), its possible subtraction is only

\[
                         O(HB)=o(NB)=o(W).          \tag{5.5}
\]

If \(H\overline\nu_H\not=o_A(B)\), the proved low-height packing tail
allows one to fix an \(a>0\) and a subsequence on which
\(H\overline\nu_H^{\ge a}=\Omega_A(B)\).  Equations (5.4)--(5.5) then
give physical seam cost \(\Omega_A(NB)=\Omega_A(W)\).  Conversely,
(5.1) and the upper construction give \(o(W)\) total overhead whenever
\(H\overline\nu_H=o_A(B)\).  This proves the necessity direction in
Outcome 3 without assuming that the portal set is deck-invariant, and
with the stated additive-compiler scope.

## 6. The two-point quantitative no-go

Work on retained nonwrapping quotient cycles.  Let \(E_H,R_H,\mathcal C_H\)
be as in (0.6).  Make the conflict graph whose vertices are eligible starts
and whose edges join overlapping residence intervals.  Its independence
number is \(\overline\nu_H\), and it has at most \(\mathcal C_H\) edges.
The Turan--Cauchy bound gives

\[
 \boxed{
                         \overline\nu_H
             \ge {R_H^2\over R_H+2\mathcal C_H}.}   \tag{6.1}
\]

Under (0.7),

\[
                         \overline\nu_H
               \ge {c_A\over1+2C_A}{B\over H}.      \tag{6.2}
\]

Therefore

\[
                         H\overline\nu_H=\Omega_A(B).          \tag{6.3}
\]

By the low-height deletion and the physical lower bound (5.4), every
additive delay/cut/dominance factorization has physical auxiliary literal
cost \(\Omega_A(W)\).  This proves the no-go in Outcome 4 even when the
portal cuts themselves are not deck-invariant.

Conversely, if \(R_H\ge c_AB/H\) and an \(o(W)\) factorization in this
architecture exists, then (6.1) and (5.1) force

\[
                         {\mathcal C_H\over R_H}\to\infty,     \tag{6.4}
\]

which is (0.8).

## 7. Exact frontier

The corrected status is now:

* the portal-tree walk is a valid \(W+o(W)\) chronology;
* every required PBBS window lost at a portal has an \(O(H)\) literal
  chart, while incidental bridge/backtrack windows are discarded, so the
  portal-specific witness cost is only \(o(W)\);
* the untouched PBBS interiors retain the full Gaussian short-residence
  packing gate;
* portal cuts are too sparse by a factor \(\sqrt m\) to change a critical
  physical packing; and
* bounded short-lag return correlation gives a rigorous \(\Omega(W)\)
  no-go for the entire additive delay/cut/dominance compiler class.

No unconditional asymptotic for \(R_H\) and \(\mathcal C_H\) is presently
proved, so this does not settle arbitrary literal OR words.  It proves that
the portal construction cannot settle them without either the divergent
PBBS clustering theorem (0.8) or a nonadditive, in-place baseline
replacement which is not representable as a sum of local seam costs.
