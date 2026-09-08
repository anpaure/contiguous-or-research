# PBBS centered Johnson factors and the literal compiler

## Exact depth-two obstruction, complement repair, and the correct wreath criterion

Date: 2026-07-26

This note audits the interface between the canonical PBBS odd-graph
factor and the factor-blind literal owner-cycle compiler.  It uses the
independently audited PBBS first- and second-shadow theorems from

* `MATH_ATTACK_O2_FIRST_SHADOW_FACTOR_20260724.md`,
* `PBBS_Q2_DEFICIT5_CRITERION_20260725.md`, and
* `MATH_ATTACK_AD15_DIRECT_PBBS_ALLQ_EROSION_AUDIT_20260725.md`.

The outcome is precise.

1.  The centered PBBS projection is an actual owner-disjoint Johnson
    (2)-factor, not an abstract incidence object.  Its component count is
    in fact at most (W/(2m+1)), slightly sharper than the previously
    recorded (2W/(2m+1)).
2.  Its cycles need not be wreaths, but the literal compiler does not ask
    for wreaths.
3.  The centered rank-(m) cycles have complete, rank-correct lower and
    upper support through the second turn.  Nevertheless their positive
    dwell condition (P_2) fails at the classified gap-five PBBS returns.
    Thus complete (q=2) support does **not** by itself make these cycles
    literal depth-two compiler rows.
4.  Complementing the chronology changes the short positive runs into
    short zero runs.  The complemented rank-((m+1)) chronology has
    (P_2) and gives the already proved five-rank word of length
    (W+4\operatorname{Cat}_m).  One further erosion layer, with the
    polynomially many gap-five defects repaired literally, gives the
    seven-rank word of length
    
    \[
      W+6\operatorname{Cat}_m+21(2m+1)(m-1)=W+O(W/m).
    \]
5.  Hence depth two is not the asymptotic obstruction.  For growing
    (H), the dominance-staircase theorem of
    `MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md`, independently
    audited in `MATH_ATTACK_Y15_PBBS_LINEAR_DOMINANCE_SEAM_AUDIT_20260725.md`,
    supplies an exact (4H-1)-letter chart at every cut.  Thus the seam
    problem is solved.  The weakest remaining PBBS gate is the critical
    short-residence packing estimate

    \[
      \nu_{\lceil A\sqrt m\rceil}(P_m)
      =o_A(\operatorname{Cat}_m\sqrt m)
    \]

    for every fixed (A>0).  The Catalan-order estimate
    (\(\nu_H=O_A(\operatorname{Cat}_m)\)) is a stronger optional route.

## 1. Centered projection and the sharper component count

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=W/n=\operatorname{Cat}_m.
\]

Let (F) be a spanning (2)-factor of (KG(n,m)).  On an oriented
component write its vertices as

\[
 A_0,A_1,\ldots,A_{L-1},A_0.
\]

At the center (A_i), join its two (F)-neighbours:

\[
                 e_i=A_{i-1}A_{i+1}.
\]

The resulting graph (P(F)) is a spanning (2)-factor of (J(n,m)).
Indeed, each middle set occurs in the two centered edges belonging to its
two (F)-neighbours, and the center of a Johnson edge is unique.  Its
edge colours satisfy

\[
 A_{i-1}\cup A_{i+1}=A_i^c,
 \qquad
 A_{i-1}\cap A_{i+1}=:\chi_F(A_i).
\tag{1.1}
\]

On an (F)-cycle of length (L), (P(F)) is the step-two graph on
\(\mathbb Z_L\).  It has (gcd(2,L)) components, each of length
(L/\gcd(2,L)).

For the canonical PBBS factor, every odd-graph orbit length is a positive
multiple (hn) of (n).  Since (n) is odd, every projected component
has length

\[
 {hn\over\gcd(2,h)}\ge n.
\]

Consequently the number (K_P) of centered Johnson components obeys the
sharper estimate

\[
                     \boxed{K_P\le W/n=B.}
\tag{1.2}
\]

The PBBS first-shadow theorem and (1.1) give, unconditionally,

\[
 \begin{array}{ll}
 \text{upper union colours of }P(F_{PBBS}) &	ext{exactly once},\\
 \text{lower intersection colours} &1\le\mu_1\le3,\\
 \text{lower holes} &0.
 \end{array}
\tag{1.3}
\]

Thus (P(F_{PBBS})) is already made of literal middle-set rows and is
owner-disjoint.  No conversion to cyclic coordinate orders is part of the
factor-blind interface.

## 2. Correct characterization of a wreath row

The following tempting assertion is false:

> a length-(n) Johnson cycle is a wreath whenever its (n) deleted
> coordinates are distinct.

Here is the exact replacement.

### Proposition 2.1 (wreath criterion)

Let (X_0,\ldots,X_{n-1},X_0) be a simple cycle in (J(n,m)), and put

\[
 d_i=X_i\setminus X_{i+1},\qquad
 a_i=X_{i+1}\setminus X_i.
\]

It is a wreath row if and only if, after cyclic indexing,

\[
 \boxed{
   d_0,\ldots,d_{n-1}\text{ are all distinct}
   \quad\text{and}\quad
   a_i=d_{i+m}\quad\text{for every }i.}
\tag{2.1}
\]

Equivalently, every coordinate has positive residence exactly (m), and

\[
                  X_i=\{d_i,d_{i+1},\ldots,d_{i+m-1}\}.
\tag{2.2}
\]

#### Proof

For a wreath with cyclic coordinate order (d_0,d_1,\ldots,d_{n-1}),
the transition from the (i)-th to the ((i+1))-st interval deletes
(d_i) and inserts (d_{i+m}).  This proves necessity.

Conversely, (2.1) says that (d_j) is inserted at transition (j-m)
and deleted at transition (j).  Hence it is present in exactly the
states (X_{j-m+1},\ldots,X_j).  At state (X_i), the present deletion
labels are precisely (d_i,\ldots,d_{i+m-1}), proving (2.2).  These are
the length-(m) cyclic intervals of the deletion order. \(\square\)

Distinct deletions alone do not force the residence lengths.  The smallest
counterexample lies in (J(5,2)):

\[
  01,\ 12,\ 02,\ 03,\ 04,\ 01.
\tag{2.3}
\]

Its deleted coordinates are respectively (0,1,2,3,4), all distinct,
but its vertex set is not the edge set of a (5)-cycle on the ground
coordinates and hence is not a wreath.  Its coordinate residence lengths
are (4,2,2,1,1), not all (2).

This distinction has no adverse effect on the literal compiler: the
compiler accepts arbitrary cyclic rows of actual middle owners, provided
their coordinate dwell and rank-correct trace conditions hold.

## 3. Exact complement identity at every turn depth

For any oriented odd-graph cycle, adjacent disjointness gives

\[
                 A_{j+1}=[n]\setminus(A_j\cup A_{j+2}).
\tag{3.1}
\]

Therefore, for every (q\ge0),

\[
 \boxed{
 [n]\setminus\bigcup_{h=0}^{q+1}A_{i+2h}
   =\bigcap_{h=0}^{q}A_{i+2h+1}.}
\tag{3.2}
\]

Indeed, intersect (3.1) over (j=i,i+2,\ldots,i+2q).
Thus the upper ((q+2))-state trace on one step-two chronology is the
complement of the lower ((q+1))-state trace on the opposite chronology.
The shift (i\mapsto i+1) permutes all oriented PBBS starts, so the two
trace systems have identical support and multiplicity after complementation.

The audited PBBS depth-two theorem says

\[
 1\le
 \#\left\{i:\bigcap_{h=0}^{2}A_{i+2h}=S\right\}
 \le10
 \qquad
 \left(S\in\binom{[n]}{m-2}\right),
\tag{3.3}
\]

and every displayed intersection has rank (m-2).  Together with the
first-shadow theorem and (3.2), this proves complete, rank-correct support
of the centered PBBS chronology for

\[
 \begin{array}{c|c}
 \text{trace}&\text{rank}\\ \hline
 A_i\cap A_{i+2}&m-1\\
 A_i\cap A_{i+2}\cap A_{i+4}&m-2\\
 A_i\cup A_{i+2}&m+1\\
 A_i\cup A_{i+2}\cup A_{i+4}&m+2\\
 A_i\cup A_{i+2}\cup A_{i+4}\cup A_{i+6}&m+3.
 \end{array}
\tag{3.4}
\]

This is a support theorem.  It is not yet the dwell theorem needed to
turn the centered rows directly into delayed-atom words.

## 4. The first literal obstruction occurs at centered depth two

For an oriented odd-graph cycle define its omitted labels

\[
                    g_j=[n]\setminus(A_j\cup A_{j+1}).
\]

Then

\[
                  A_{j+2}=A_j-\{g_{j+1}\}+\{g_j\}.
\tag{4.1}
\]

Suppose a PBBS omitted label has a consecutive gap-five return

\[
                         g_s=g_{s+5}=x.
\tag{4.2}
\]

The label (x) is absent from (A_s), is inserted in the transition
(A_s\to A_{s+2}), remains in (A_{s+2},A_{s+4}), and is deleted in
the transition (A_{s+4}\to A_{s+6}).  Hence the centered rank-(m)
step-two row has a positive (x)-run of exactly two states.

The literal compiler's condition (P_2) requires every nonconstant
positive run to have at least three states.  Thus every gap-five return is
an explicit violation of (P_2).  Such returns genuinely occur; their
exact PBBS census is

\[
                      (2m+1)(m-1).
\tag{4.3}
\]

This explains the otherwise paradoxical interface:

* the centered chronology has complete and rank-correct second-turn
  support by (3.3)--(3.4);
* nevertheless the erosion/dilation identity needed by the direct literal
  compiler can erase (x) completely on the two-state run, so it cannot
  reconstruct every intended owner and union window.

Therefore the PBBS centered (2)-factor cannot simply be handed to the
depth-two delayed-atom compiler.  The missing premise is dwell, not support,
owner integrality, component control, or wreath structure.

## 5. Complement repair and the exact finite-band positive result

Put (X_i=A_i^c) and take the step-two (X)-cycles.  For this
complemented chronology, consecutive omitted labels have gap at least five,
and the PBBS residence dictionary gives every positive coordinate run
length at least three.  Hence (P_2) holds.

Define

\[
                       D_i=X_i\cap X_{i+1}\cap X_{i+2}
\]

on each reindexed step-two cycle.  The exact binary erosion/dilation
identities are

\[
\begin{aligned}
D_i&=X_i\cap X_{i+1}\cap X_{i+2},\\
D_i\cup D_{i+1}&=X_{i+1}\cap X_{i+2},\\
D_i\cup D_{i+1}\cup D_{i+2}&=X_{i+2},\\
D_i\cup\cdots\cup D_{i+3}&=X_{i+2}\cup X_{i+3},\\
D_i\cup\cdots\cup D_{i+4}&=X_{i+2}\cup X_{i+3}\cup X_{i+4}.
\end{aligned}
\tag{5.1}
\]

Complete PBBS first- and second-shadow support identifies these five lines
with all targets in ranks

\[
                         m-1,m,m+1,m+2,m+3.
\]

Repeating four prefix atoms per cycle costs at most (4B), by (1.2).
Thus one obtains the unconditional literal word

\[
 \boxed{|Q_2|\le W+4B}
\tag{5.2}
\]

covering those five ranks.

The missing rank (m-2) can also be restored at negligible cost.  Use
four-fold erosion on the complemented chronology.  Its first failures are
the positive runs of length three, again the classified gap-five returns.
Each such run spoils at most (1+2+\cdots+6=21) intended windows.  Appending
the spoiled targets literally gives

\[
 \boxed{|Q_3|\le
   W+6B+21(2m+1)(m-1)=W+O(W/m)}
\tag{5.3}
\]

and covers all seven ranks

\[
                         m-2,m-1,m,m+1,m+2,m+3,m+4.
\tag{5.4}
\]

Consequently the centered (q=2) dwell failure is real but is not an
asymptotic no-go.  It can be shifted to the complemented chronology and
repaired at polynomial cost.

## 6. The growing-window gate and the linear seam

For a target height (H), let \(\mathcal I_H\) be the family of projected
PBBS coordinate-residence arcs of length at most (H), equivalently the
omitted-label return arcs of odd gap at most (2H-1).  Any attempt to turn
the unmodified PBBS chronology into (P_H)-safe paths must cut every arc
of \(\mathcal I_H\), or else explicitly repair all erosion/dilation windows
spoiled by that residence.

Let \(\nu_H(P_m)\) be the maximum number of pairwise edge-disjoint arcs in
\(\mathcal I_H\).  The still-open Catalan packing estimate is

\[
                         \nu_H(P_m)=O(W/m).
\tag{6.1}
\]

Even (6.1) is not by itself the whole literal theorem.  A transversal of
the short residences creates (O(W/m)) cuts.  The factor-blind path
compiler charges only (O(H)) collar letters per cut, which is harmless
for (H=o(m)).  But deleting all cyclic windows crossing a bare cut loses

\[
                       2\sum_{q=1}^{H}q=H(H+1)
\tag{6.2}
\]

occurrences per cut.  The support-blind bound is therefore

\[
                         O(H^2W/m),
\tag{6.3}
\]

which is (o(W)) only for (H=o(\sqrt m)).  Coefficient one needs a
window beyond the Gaussian scale.

The support-blind estimate (6.3) is not the final ledger.  The audited
dominance-staircase construction recodes, at one cut, every floor-correct
lower intersection and every upper union of depth at most (H) in exactly
(4H-1) nonzero letters.  Combining this chart with endpoint-capped erosion
of the cut paths gives, deterministically,

\[
 \boxed{
 L_H\le W+2H\operatorname{Cat}_m
          +2(5H-1)\nu_H(P_m).}
\tag{6.4}
\]

Consequently, for (H=\lceil A\sqrt m\rceil), the single estimate

\[
 \boxed{\nu_H(P_m)=o_A(\operatorname{Cat}_m\sqrt m)}
\tag{ST_A}
\]

makes the right side of (6.4) equal to (W+o_A(W)).  The fixed-(A)
diagonalization, product-SCD outer tails, and the trimmed parity lift then
give the constant-one upper bound.  The seam is therefore proved; only
((ST_A)) remains open.  The height-gap spectrum already gives the matching
critical-order upper bound (O_A(\operatorname{Cat}_m\sqrt m)); the missing
content is a vanishing improvement, not a new polynomial factor.

The later multi-cut dominance chart does not provide an independent escape
from this gate.  The exact comparison in
`PBBS_ST_CS_EQUIVALENCE_20260726.md` proves, after the already controlled
sub-Gaussian-height tail is removed,

\[
 \mathfrak S_H=o_A(\operatorname{Cat}_m)
 \quad\Longleftrightarrow\quad
 H\overline\nu_H=o_A(\operatorname{Cat}_m).
\tag{6.4a}
\]

Thus clustering changes constants but not the critical asymptotic scale.
If ((ST_A)) fails, the surviving PBBS option must replace principal
baseline letters in place, rather than append dominance charts, or change
the owner architecture.

Thus the PBBS-to-compiler status is:

\[
\boxed{
\begin{array}{ll}
q=1:&\text{complete and literal on the centered factor},\\
q=2:&\text{complete support; centered dwell fails, but complement repair
            is }o(W),\\
q=3\text{ fixed}:&\text{literal after the polynomial gap-five repair},\\
H=\lceil A\sqrt m\rceil:&\text{linear seam proved; critical residence
                   packing }(ST_A)\text{ open}.
\end{array}}
\tag{6.5}
\]

There is no remaining wreath-length or seam interface.  The obstruction
is exactly the maximum number of pairwise edge-disjoint short coordinate
residences in the PBBS chronology, normalized by ((ST_A)).
