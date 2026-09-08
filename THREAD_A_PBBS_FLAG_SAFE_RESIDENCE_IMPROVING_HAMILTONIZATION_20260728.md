# Thread A: flag-safe, residence-improving PBBS Hamiltonization

Date: 2026-07-28

Status: theorem-level conditional reduction with exact local pruning.  It
does **not** prove that the PBBS factor can be Hamiltonized with the required
decoration, and it does not prove the exact contiguous-OR formula.

## 0. Outcome

Put

\[
 \Omega=[15],\qquad O_7=KG(15,7),\qquad
 W=\binom{15}{7}=6435.
\]

The authoritative inputs are now stronger than turn coverage alone.

* The PBBS odd-graph factor has complete correct support at every depth:
  for every (0\le q\le7) and every
  (S\in\binom{\Omega}{7-q}), some canonically oriented (q)-edge
  PBBS path has full intersection (S), with occurrence load at most
  \(\binom{2q+1}{q}\).
* For an odd-graph Hamilton cycle, all upper traces of the antipodal
  Middle Levels lift are equivalent to the descending flag tower of its
  every-second order.  Turn-surjectivity is only the row (q=1) of that
  tower.
* Published GMN/MNW Hamiltonization applies to the lexical factor, not to
  PBBS.  Its connectors therefore cannot be imported into PBBS without a
  new alternation and orientation theorem.

This note proves four things.

1. An **orientation-coherent** factor switch has a finite successor seam
   (R).  At every depth (q), all PBBS flags outside an explicit collar
   (I_q(R)) are literally unchanged.  There is an exact exposed-fibre
   criterion for preserving the complete flag tower.
2. The same seam has an exact residence ledger.  Old omitted-label returns
   outside its distance-(3/5) collar survive, while every new return is
   confined to the corresponding new collar.  This gives a local,
   computable notion of a residence-improving connector.
3. Every alternating (C_6) in an odd graph has one normal form.  Its six
   turn changes and a literal portal-completion test are computed exactly.
   This is the (q=1) shadow of the flag-collar theorem, not a substitute
   for it.
4. These statements give a sharp conditional PBBS theorem.  A compatible
   join schedule must simultaneously recreate all exposed flags, hit all
   old distance-five returns without creating distance-three/five returns,
   and pass the residual common-owner Hall problem.  Ordinary component
   connectivity proves none of these conditions.

For asymptotic coefficient one, Hamiltonization is not itself necessary:
opening at most \(\operatorname{Cat}_m\) PBBS cycles and paying the proved
(O(H)) seam chart costs (O(H\operatorname{Cat}_m)=O(W/\sqrt m)) at
(H=\Theta(\sqrt m)).  The live asymptotic gate is the short-residence
transversal.  The connector theorem below is useful only when it improves
that residence ledger or preserves the exact owner interface.

## 1. Oriented factors, flags, and the coherence hypothesis

Let (F) be a spanning (2)-factor of (O_7), with every component
oriented.  Write its successor permutation as

\[
 \sigma:\binom{\Omega}{7}\longrightarrow\binom{\Omega}{7}.
\]

Thus (A\cap\sigma(A)=\varnothing).  Put

\[
 \pi=\sigma^2,
 \qquad
 \Phi_q^\pi(A)=\bigcap_{h=0}^{q}\pi^h(A)
 \quad(0\le q\le7).
\tag{1.1}
\]

The row (q) consists of (q)-edge, (q+1)-vertex flags and has target
rank (7-q).  If (sigma) is one Hamilton cycle, then multiplication by
two permutes its odd number (W) of positions.  Consequently (pi) is
also one Hamilton cycle.  In the notation of Theorem 2.6 of
`MATH_K15_COMPLEMENT_ANTIPODAL_MIDDLE_LEVELS_REDUCTION_20260728.md`,

\[
 \Phi_q^\pi(B_i)=F_i^{(q+1)}.
\tag{1.2}
\]

In particular, the row (q=1) is exactly the turn-colour word
(A_{j-1}\cap A_{j+1}), after a cyclic reindexing.

Suppose a family of factor switches changes (F) to another oriented
factor (F'), with successor (sigma').  We call the switching family
**orientation-coherent** when every retained old path is traversed in its
original PBBS orientation.  Define the actual successor-disagreement set

\[
 R=\{A:\sigma'(A)\ne\sigma(A)\}
\tag{1.3}
\]

in all cases.  Under orientation coherence, (R) consists only of the cut
tails.  Without it, (R) can contain every vertex of a reversed inherited
segment, so none of the later bounded-support estimates is available.

This hypothesis is essential.  An undirected join may reverse an entire
old component.  Such a reversal changes its canonical PBBS flags at
macroscopic support and cannot be treated as a bounded collar.

### Lemma 1.1 (square-successor seam)

Put (pi'=(\sigma')^2) and

\[
 D=\{A:\pi'(A)\ne\pi(A)\}.
\]

Then

\[
 \boxed{D\subseteq R\cup\sigma^{-1}(R),\qquad |D|\le2|R|.}
\tag{1.4}
\]

If one orientation-coherent alternating (C_{2\ell}) switch removes
(ell) oriented factor arcs and reconnects their tails to their heads,
then (|R|=\ell), and hence (|D|\le2\ell).

#### Proof

If (A\notin R) and (sigma(A)\notin R), then

\[
 \sigma'(A)=\sigma(A),\qquad
 (\sigma')^2(A)=\sigma'(\sigma(A))=\sigma^2(A).
\]

This proves (1.4).  In an orientation-coherent (C_{2\ell}) switch, the
only changed successor arcs are the (ell) cut tails.  \(\square\)

## 2. Exact all-depth flag collars

For (q\ge1), define the old (q)-collar

\[
 I_q=\bigcup_{h=0}^{q-1}\pi^{-h}(D).
\tag{2.1}
\]

The analogous expression formed with (pi') gives the same set.

### Theorem 2.1 (literal flag-collar identity)

For every (q\ge1):

1. the old and new definitions of (I_q) agree;
2. (|I_q|\le q|D|\le2q|R|); and
3. for every (A\notin I_q),

   \[
    \boxed{\Phi_q^{\pi'}(A)=\Phi_q^\pi(A).}
   \tag{2.2}
   \]

For one orientation-coherent alternating (C_{2\ell}), at most
(2\ell q) depth-(q) starts are therefore altered.  In particular one
hexagon alters at most (6q) starts.

#### Proof

If (A\notin I_q), then none of

\[
 A,\pi(A),\ldots,\pi^{q-1}(A)
\]

lies in (D).  Induction gives
((\pi')^h(A)=\pi^h(A)) for (0\le h\le q), proving (2.2) and showing
that (A) is outside the new collar as well.  The converse follows by
interchanging (pi,pi').  Hence the two collars agree.  The union bound
in (2.1), followed by Lemma 1.1, proves the size estimate. \(\square\)

The theorem has an exact support consequence.  Let

\[
 \mathcal T_q=\binom{\Omega}{7-q},
\]

and define the old correct-rank occurrence fibre

\[
 \mathcal O_q(S)=\{A:\Phi_q^\pi(A)=S\}.
\tag{2.3}
\]

Let (H_q\subseteq\mathcal T_q) be the old hole set, and let

\[
 E_q(I_q)=
 \{S\in\mathcal T_q\setminus H_q:\mathcal O_q(S)\subseteq I_q\}
\tag{2.4}
\]

be the targets whose entire old fibre is exposed by the collar.  Finally
put

\[
 G_q(I_q)=
 \{\Phi_q^{\pi'}(A):A\in I_q,
                    |\Phi_q^{\pi'}(A)|=7-q\}.
\tag{2.5}
\]

### Theorem 2.2 (exact exposed-fibre recurrence)

Put

\[
 a_q^-(S)=|\mathcal O_q(S)\cap I_q|,\qquad
 a_q^+(S)=
 |\{A\in I_q:\Phi_q^{\pi'}(A)=S\}|.
\]

Then the complete multiplicity transport is

\[
 \boxed{\mu_q'(S)=\mu_q(S)-a_q^-(S)+a_q^+(S).}
\tag{2.6}
\]

The new depth-(q) hole set is

\[
 \boxed{H_q'=(H_q\cup E_q(I_q))\setminus G_q(I_q).}
\tag{2.7}
\]

Consequently, when (F) is the PBBS factor, (H_q=\varnothing) at every
depth and the switch family preserves the complete correct flag tower if
and only if

\[
 \boxed{E_q(I_q)\subseteq G_q(I_q)
        \quad(1\le q\le7).}
\tag{2.8}
\]

A stronger sufficient condition is that every target have one canonical
PBBS occurrence outside (I_q).  The PBBS load cap by itself does not
imply this condition, because some targets may have load one.

#### Proof

A start outside \(I_q\) contributes the same old and new flag, while all
changed contributions have their starts in \(I_q\).  Splitting both
multiplicities into collar and noncollar parts proves (2.6).

A target outside (H_q\cup E_q(I_q)) has an old occurrence outside the
collar, and Theorem 2.1 preserves that occurrence.  A target in
(H_q\cup E_q(I_q)) has no old occurrence outside the collar.  Since all
outside occurrences are unchanged, it occurs after the switch exactly
when it belongs to the new collar palette (G_q(I_q)).  This is (2.7).
The PBBS specialization uses the audited all-depth support theorem. \(\square\)

### Corollary 2.3 (owner data localize, but do not disappear)

Every literal flag occurrence and every label attached to it outside
(I_q) transports unchanged.  Hence any pre-existing owner assignment
using only starts outside the collars survives verbatim.  All owner demands
whose chosen occurrences meet a collar reduce to a residual common-owner
matching problem on the new collar occurrences.

This is a localization theorem, not a Hall theorem.  Marginal inclusions
(2.8) do not imply that the residual demands at different depths admit one
common integral owner assignment.

### 2.4 Relation to hypersimplex completion

Theorem 2.2 is a chronology theorem, not another rankwise balancing
argument.  The hypersimplex-completion theorem proves that whenever

\[
 0\le \gamma_{q,x}\le e_q,
\]

the forced depth-\(q\) point-degree vector has a hole-free uniform
multidesign realization, and every actual row is connected to such a
realization by symmetric two-block exchanges.  For frozen Hall-29,

\[
 \gamma_{2,x}\in[568,574]\quad(e_2=1428),\qquad
 \gamma_{3,x}\in[1138,1147]\quad(e_3=3429).
\tag{2.9}
\]

Consequently there is no marginal or separate-rank obstruction at
depths \(2\) and \(3\).

For one successor change, however, Theorem 2.2 gives the coupled
increments

\[
 \delta_q(S)=a_q^+(S)-a_q^-(S)
 \qquad\text{simultaneously for every }q.
\tag{2.10}
\]

The exact remaining simultaneous hypersimplex-lift problem is therefore
to choose one successor \(\sigma'\) whose collar increments realize
compatible hole-free completions at every depth, while also satisfying
the residence conditions and one common integral owner-Hall extension.
Abstract two-block connectivity in each hypersimplex does not supply
such a chronology.  The \(2\)-for-\(2\) \(C_6\) rectangle case in
Section 4 is one depth-one chronological lift; its deeper collars remain
forced.

## 3. Exact residence collars

For an oriented odd edge, let

\[
 z_\sigma(A)=\Omega\setminus(A\cup\sigma(A))
\tag{3.1}
\]

be its unique omitted label.  For an odd distance (s\), put

\[
 \mathcal B_s(\sigma)=
 \{A:z_\sigma(A)=z_\sigma(\sigma^s(A))\}.
\tag{3.2}
\]

The antipodal lift is depth-three resident exactly when

\[
 \mathcal B_3(\sigma)=\mathcal B_5(\sigma)=\varnothing;
\tag{3.3}
\]

distance one is automatic for a simple factor cycle.  Define the
distance-(s) seam collar

\[
 J_s=\bigcup_{h=0}^{s}\sigma^{-h}(R).
\tag{3.4}
\]

As in Theorem 2.1, the definition using (sigma') gives the same set.

### Theorem 3.1 (residence transport and local improvement)

For every (s\ge1),

\[
 \boxed{
 \mathcal B_s(\sigma')
 =\bigl(\mathcal B_s(\sigma)\setminus J_s\bigr)
   \ \dot\cup\
   \bigl(\mathcal B_s(\sigma')\cap J_s\bigr).
 }
\tag{3.5}
\]

In particular:

* every old bad comparison outside (J_s) survives;
* every new bad comparison is confined to (J_s) unless it was already
  present outside; and
* the exact change is

  \[
   |\mathcal B_s(\sigma')|-|\mathcal B_s(\sigma)|
   =|\mathcal B_s(\sigma')\cap J_s|
    -|\mathcal B_s(\sigma)\cap J_s|.
  \tag{3.6}
  \]

Thus (3.6), summed over (s=3,5), is a genuine local
**residence-improvement invariant** for a connector.

#### Proof

If (A\notin J_s), none of the (s+1) edge sources

\[
 A,\sigma(A),\ldots,\sigma^s(A)
\]

lies in (R).  Induction shows that the old and new walks and their two
compared edge labels coincide.  The symmetric argument proves equality of
the old and new collars and equality of the bad-start sets off the collar.
Splitting the new bad set into its inside and outside parts gives (3.5),
and cardinalities give (3.6). \(\square\)

### Corollary 3.2 (exact depth-three seam test)

The final factor is depth-three resident if and only if

\[
 \mathcal B_3(\sigma)\subseteq J_3,
 \qquad
 \mathcal B_5(\sigma)\subseteq J_5,
\tag{3.7}
\]

and

\[
 \mathcal B_3(\sigma')\cap J_3=\varnothing,
 \qquad
 \mathcal B_5(\sigma')\cap J_5=\varnothing.
\tag{3.8}
\]

For PBBS at (m=7), the audited return classification gives

\[
 \mathcal B_3(\sigma)=\varnothing,qquad
 |\mathcal B_5(\sigma)|=15(7-1)=90.
\tag{3.9}
\]

Therefore a successful PBBS Hamiltonization must hit all ninety old
distance-five starts with (J_5), and its new seam collars must contain no
distance-three or distance-five equality.  Since (|J_5|\le6|R|), this
implies the elementary necessary bound (|R|\ge15).

## 4. The minimal odd-graph connector and its turn portal

This section records the complete (q=1) local picture.  It is useful for
constructing candidate connectors, but Theorems 2.1--3.1 remain necessary
at all larger depths.

### Theorem 4.1 (classification of (C_6\)'s in (O_m))

Every simple (6)-cycle in (O_m=KG(2m+1,m)), (m\ge3), has, up to
rotation and reversal, the form

\[
\begin{array}{lll}
 v_0=K\cup\{a\},&v_1=L\cup\{c\},&v_2=K\cup\{b\},\\
 v_3=L\cup\{a\},&v_4=K\cup\{c\},&v_5=L\cup\{b\},
\end{array}
\tag{4.1}
\]

where

\[
 \Omega=K\mathbin{\dot\cup}L\mathbin{\dot\cup}\{a,b,c\},
 \qquad |K|=|L|=m-1.
\tag{4.2}
\]

Moreover (O_m) has no (4)-cycle, so this is the smallest alternating
factor switch.

#### Proof

Two distinct (m)-sets have at most one common odd-graph neighbour, so a
simple (4)-cycle is impossible.  In a (6)-cycle, the three even
vertices form a triangle in (J(2m+1,m)).  A top-type Johnson triangle
would force all three intervening odd vertices to be the same complement.
Hence the even triangle has one common ((m-1))-core (K), and its three
extra points are (a,b,c).  Taking the unique complements of the unions of
successive even vertices yields the core (L) and (4.1). \(\square\)

Assume the old factor edges on (4.1) are

\[
 v_0v_1,\qquad v_2v_3,\qquad v_4v_5,
\tag{4.3}
\]

and switch to the other three hexagon edges.  Let (p_i) be the omitted
label of the retained factor edge at (v_i).  Alternation forces

\[
 p_0,p_2,p_4\in L,qquad p_1,p_3,p_5\in K.
\tag{4.4}
\]

### Theorem 4.2 (complete turn ledger)

The six old and new turns are

\[
\begin{array}{c|c|c}
 &\text{old}&\text{new}\\ \hline
v_0&(L-p_0)+c&(L-p_0)+b\\
v_1&(K-p_1)+a&(K-p_1)+b\\
v_2&(L-p_2)+a&(L-p_2)+c\\
v_3&(K-p_3)+b&(K-p_3)+c\\
v_4&(L-p_4)+b&(L-p_4)+a\\
v_5&(K-p_5)+c&(K-p_5)+a.
\end{array}
\tag{4.5}
\]

The point-degree vector is unchanged.  On either core side the trade is
neutral when its three retained labels agree, is a (2)-for-(2)
rectangle when exactly two agree, and is (3)-for-(3) when they are all
distinct.

#### Proof

At (v_0=K+a), for example, the removed and inserted hexagon edges omit
(b) and (c), while the retained edge omits (p_0\in L).  The turn is
the complement of (v_0) with the two incident edge labels deleted,
giving the first row.  The other rows follow cyclically.  The three added
outside labels on either core side are cyclically permuted, proving point
balance.  Equality of two displayed colours forces equality of both their
outside label and omitted core point, which gives the stated trichotomy.
\(\square\)

The following completion test turns a desired one-vertex portal into a
literal connector.

### Lemma 4.3 (portal-to-hexagon completion)

Let \(AB,NC,DE\) be three undirected factor edges and let \(AN\) be the
desired new odd edge.  Suppose

\[
 C\cap D=\varnothing,\qquad E\cap B=\varnothing,
\tag{4.6}
\]

and all six vertices (A,N,C,D,E,B) are distinct.  Then

\[
 Q=(A,N,C,D,E,B,A)
\tag{4.7}
\]

is factor-alternating: it deletes (AB,NC,DE) and adds (AN,CD,EB).
If the three deleted edges lie in three distinct current components, the
switch merges them into one.

For this switch also to be orientation-coherent in the sense of Section 1,
the deleted arcs must be oriented

\[
 A\to B,\qquad C\to N,\qquad E\to D,
\]

and the new arcs

\[
 A\to N,\qquad C\to D,\qquad E\to B,
\]

or all six directions must be reversed.  Merely orienting the displayed
undirected sequence \(A,N,C,D,E,B,A\) cyclically reverses inherited paths
and does not satisfy the bounded-collar hypothesis.

At a portal centre (A), let (S\subset A^c) be a currently missing
turn and put (D_A=A^c\setminus S), a two-set.  If the two current
incident edge labels at (A) are (P_A), a one-edge switch can create
(S) at (A) exactly when

\[
 \boxed{|P_A\cap D_A|=1.}
\tag{4.8}
\]

The label in the intersection is retained and the other member of (D_A)
is forced as the new edge label.  Lemma 4.3 is then the exact remaining
hexagon-completion test.

#### Proof

The six successive edges in (4.7) alternate new, old, new, old, new, old;
(4.6) supplies the two nontrivial new odd edges.  Cutting three distinct
factor cycles once and reconnecting their paths cyclically gives one cycle.
At (A), a turn is (A^c) minus its two incident omitted-edge labels.
One incident label is retained and the other is replaced, proving (4.8).
\(\square\)

This gives a genuine local acquisition mechanism, but it controls only the
turn at (A).  Its full (q)-collars, its distance-(3/5) label collar,
and its owner incidences must still pass Theorems 2.2--3.1 and the residual
owner matching.

## 5. Conditional PBBS flag-residence Hamiltonization theorem

Let (F_{\rm P}) be the canonically oriented PBBS factor of (O_7), with
successor (sigma).  Let a family of alternating switches produce an
oriented Hamilton cycle (F_*), with successor (sigma_*), and assume
the family is orientation-coherent.  Form (R,D,I_q,J_s,E_q,G_q) as in
Sections 1--3.

### Theorem 5.1 (exact sufficient connector theorem)

If

\[
 E_q(I_q)\subseteq G_q(I_q)
 \qquad(1\le q\le7),
\tag{5.1}
\]

and

\[
 \mathcal B_5(\sigma)\subseteq J_5,
 \qquad
 \mathcal B_3(\sigma_*)\cap J_3
 =\mathcal B_5(\sigma_*)\cap J_5=\varnothing,
\tag{5.2}
\]

then:

1. (F_*) is a Hamilton cycle of (O_7) whose turn colours cover every
   (6)-set;
2. every descending flag row of its every-second order covers its complete
   target layer;
3. its complement-antipodal Middle Levels lift is upper-universal at every
   rank; and
4. the lifted middle chronology is depth-three resident.

#### Proof

The PBBS all-depth theorem gives (H_q=\varnothing).  Theorem 2.2 and
(5.1) give complete support in every row.  Row (q=1) is the turn word.
Theorem 2.6 of the complement-antipodal reduction converts the full flag
tower into all upper ranks.  PBBS has no distance-three bad start, and
(5.2), together with Corollary 3.2, proves depth-three residence. \(\square\)

The theorem deliberately stops before the exact OR formula.  To preserve a
pre-existing labelled owner solution, the new collar occurrences must also
admit the residual **common integral owner matching** left by Corollary 2.3.
Separate rankwise support or separate rankwise matchings do not imply that
common Hall condition.

### Quantitative calibration for a hypothetical (C_6) merge forest

The PBBS factor has at most

\[
 \operatorname{Cat}_7=429
\]

components.  If an orientation-coherent all-(C_6),
component-transversal forest existed (which in particular requires the
appropriate odd component parity), it would use at most

\[
 a\le(429-1)/2=214
\]

three-way merges.  Consequently

\[
 |R|\le3a\le642,qquad |D|\le6a\le1284,qquad
 |I_q|\le1284q.
\tag{5.3}
\]

At the turn row, PBBS has

\[
 W-\binom{15}{6}=1430
\]

excess occurrences, so the worst scalar comparison leaves (146) more
excess occurrences than the bound (1284).  This is only a scalar
calibration.  It neither places the surplus in the exposed fibres nor
proves any connector or owner Hall condition.

Published MNW connectivity does not supply this forest for PBBS.  It
Hamiltonizes the distinct lexical factor.  Even if a PBBS forest is found,
ordinary component merging verifies only the first clause in the premise
of Theorem 5.1, not (5.1)--(5.2).

## 6. Why topology is cheap asymptotically

There is a quantitative stability statement which makes the distinction
precise.  Let \(P,Q\) be coherently oriented projected Johnson cycle
systems on the same \(W\) owners, and count directed transition slots:

\[
 e=|E(P)\setminus E(Q)|=|E(Q)\setminus E(P)|.
\tag{6.1}
\]

Residence intervals below include their insertion and deletion boundary
transitions, as in the PBBS return definition.

### Theorem 6.1 (edit stability of residence and fixed flag witnesses)

For every \(H\),

\[
 \boxed{|\nu_H(P)-\nu_H(Q)|\le e.}
\tag{6.2}
\]

If \(P\) has complete depth-\(q\) flag support and one occurrence is fixed
for every target, then the number of those targets whose fixed witness is
destroyed in \(Q\) is at most

\[
 \boxed{h_q(Q)\le h_q^{\rm fixed}(Q)\le qe.}
\tag{6.3}
\]

Consequently

\[
 \boxed{\sum_{q=1}^{H}h_q^{\rm fixed}(Q)
        \le {eH(H+1)\over2}.}
\tag{6.4}
\]

#### Proof

Take a maximum edge-disjoint family of residence intervals in \(P\).  At
most \(e\) members meet a deleted transition, because the intervals are
edge-disjoint.  Every other interval survives verbatim in \(Q\), so
\(\nu_H(Q)\ge\nu_H(P)-e\).  Interchanging \(P,Q\) proves (6.2).

At fixed depth \(q\), chosen witnesses for distinct targets have distinct
starts.  One deleted directed transition lies in at most \(q\) cyclic
\(q\)-edge windows (and in at most the component length if that length is
smaller than \(q\)).  Hence all \(e\) deleted transitions destroy at most
\(qe\) chosen witnesses.  Summing \(q\) proves (6.4). \(\square\)

For the orientation-coherent odd-factor switches of Sections 1--5, the
projected edit count is \(e=|D|\le2|R|\); it is \(6\) for a nondegenerate
directed hexagon.  Thus \(O(\operatorname{Cat}_m)\) local edits can change
\(\nu_H\) by only \(O(\operatorname{Cat}_m)\), which is
\(o(\operatorname{Cat}_m\sqrt m)\).  Such a Hamiltonization cannot by
itself manufacture the missing vanishing improvement in the critical
residence bound.  On the other hand, (6.4) gives only
\(O(\operatorname{Cat}_mH^2)=O(W)\) at Gaussian depth, not the required
little-oh flag loss.  Exact or aggregate flag safety remains separate.

For general (m), PBBS has at most

\[
 B_m=\operatorname{Cat}_m=\frac{W}{2m+1}
\]

projected components.  Opening them and using the proved linear
dominance-staircase chart costs (O(H)) per seam.  At
(H=\Theta(\sqrt m)),

\[
 H B_m=O(W/\sqrt m)=o(W).
\tag{6.5}
\]

This is the component term already present in the exact ledger (24.7) of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.  Therefore a one-cycle
Hamiltonization is not a necessary asymptotic coefficient-one gate.  The
separate-cut architecture isolates the genuinely live quantity as the
short-residence transversal/packing number.

For the finite (k=15) formula, seams may consume scarce target and owner
slack.  A connector is consequently useful only if at least one of the
following is proved:

* it has negative residence increment (3.6), or collectively kills all
  ninety old distance-five starts without creating new forbidden returns;
* it satisfies the full flag recreation conditions (5.1); or
* it is compatible with the residual common-owner Hall matching.

Pure component reduction has no such consequence.

More generally, within the existing dominance-staircase architecture it is
sufficient, for each fixed \(A\) and \(H=\lceil A\sqrt m\rceil\), to build
a legal projected factor \(Q_{m,A}\) satisfying

\[
 c(Q_{m,A})=O_A(\operatorname{Cat}_m),\qquad
 \nu_H(Q_{m,A})=o_A(\operatorname{Cat}_m\sqrt m),
\tag{6.6}
\]

and aggregate lower-plus-upper flag holes

\[
 E_H(Q_{m,A})=o_A(W).
\tag{6.7}
\]

Indeed the proved seam ledger then has the form

\[
 L_H\le W+2Hc(Q_{m,A})+2(5H-1)\nu_H(Q_{m,A})+E_H(Q_{m,A})
     =W+o_A(W),
\tag{6.8}
\]

and the established diagonal tail argument gives asymptotic coefficient
one.  Hamiltonicity is not assumed in this sufficient theorem.  Exact flag
preservation is the special case \(E_H=0\).

## 7. Sharp remaining obstruction and adversarial audit

The exact missing finite theorem is not another rankwise balancing lemma.
It is the following simultaneous chronological lift.

> **PBBS simultaneous hypersimplex-lift/owner theorem at \(m=7\).**
> There is one orientation-coherent family of PBBS-alternating switches
> with successor \(\sigma_*\) such that:
>
> 1. at every required depth, the coupled increments
>    \(\delta_q(S)=a_q^+(S)-a_q^-(S)\) induced by this *same*
>    \(\sigma_*\) yield a hole-free correct-rank row; equivalently,
>    (5.1) holds, and the induced row is then one of the admissible
>    hypersimplex completions;
> 2. its residence collars satisfy (5.2);
> 3. its new collar occurrences extend the fixed outside assignment
>    through one common integral owner-Hall system; and
> 4. if an exact Hamilton cycle is desired, its component monodromy is
>    one cycle.

For the frozen Hall-29 depth-two and depth-three rows, Theorem 2.1 of
MATH_HYPERSIMPLEX_MARGINAL_COMPLETION_AND_CHRONOLOGY_GATE_20260728.md
proves that admissible hole-free endpoints in item 1 exist separately,
with the numerical margins (2.9).  It gives no common \(\sigma_*\), no
residence guarantee, and no owner extension.

Nothing read or proved here establishes this statement.  The following
possible overclaims are explicitly excluded.

1. **Lexical/PBBS transfer.**  The published GMN/MNW join tree belongs to
   the lexical factor.  It is not a PBBS connector atlas.
2. **Undirected/oriented transfer.**  An undirected merge may reverse a
   PBBS component.  Without orientation coherence, the bounded-collar
   theorem is false.
3. **Turn/all-depth transfer.**  A safe (q=1) rectangle can destroy a
   unique deeper canonical flag in its (q)-collar.
4. **Support/rank transfer.**  Only correct-rank PBBS occurrences enter
   (2.3)--(2.8).  An intersection of the wrong rank is not a target witness.
5. **Marginal/chronology/owner transfer.**  Hypersimplex decomposition and
   symmetric two-block connectivity solve each eligible row separately.
   They do not lift the row exchanges to one deletion word, nor do they
   prove one nested integral owner assignment.
6. **Topology/asymptotics.**  Hamiltonicity is not the asymptotic
   coefficient-one bottleneck; the short-residence packing gate remains.

The proved advances are therefore the exact all-depth collar recurrence,
the exact residence-improvement recurrence, the complete local hexagon
portal, and Theorem 5.1.  The existence of the decorated PBBS switch family
remains conjectural.
