# A subquadratic literal seam for deterministic PBBS cuts

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

**Supersession note.**  The theorem below is valid, but a subsequently
proved floor-correct dominance-staircase theorem improves its
\(O(H^{3/2})\) seam to the linear bound \(4H-1\).  The sharper result and
its coefficient-one ledger are in
`MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md`; an independent
Y-lane audit is recorded in
`MATH_ATTACK_Y15_PBBS_LINEAR_DOMINANCE_SEAM_AUDIT_20260725.md`.  This file
is retained as a stronger all-crossing-mask fallback, since its chart
covers wrong-rank lower masks as well as floor-correct ones.

## 0. Outcome and exact boundary

Let

\[
 n=2m+1,
 \qquad W={n\choose m},
 \qquad B_m=\operatorname {Cat}_m={W\over 2m+1}.
\tag{0.1}
\]

Consider one complement-projected PBBS step-two cycle of rank-\((m+1)\)
Johnson owners.  At a selected cut and for every integer

\[
 1\le \Delta\le H\le m,
\tag{0.2}
\]

this report constructs a nonzero literal contiguous-OR seam word exposing
**every** lower crossing intersection and upper crossing union of at most
\(H+1\) owners.  Its length is at most

\[
 \boxed{
 C_{\rm seam}(H,\Delta)
 \le
 2H+H\left\lceil {H\over\Delta}\right\rceil
 +(H-1)(2\Delta-1).}
\tag{0.3}
\]

Taking \(\Delta=\lceil\sqrt H\rceil\) gives the completely explicit bound

\[
 \boxed{C_{\rm seam}(H)\le 3H^{3/2}+4H.}
\tag{0.4}
\]

Thus the old \(H(H+1)\) literal-repair charge per cut in Section 8 of
`MATH_ATTACK_AD15_DIRECT_PBBS_ALLQ_EROSION_AUDIT_20260725.md` is replaced
by \(O(H^{3/2})=o(H^2)\).  No rank-correctness hypothesis is used by the
seam: it covers all crossing masks, and therefore in particular every
selected correct-rank crossing mask.

Consequently, if for every fixed \(A>0\)

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)=O_A(B_m),
\tag{0.5}
\]

then the already audited fixed-\(A\) diagonalization and product-SCD tail
construction imply

\[
 \boxed{
 \nu(k)\le(1+o(1)){k\choose\lfloor k/2\rfloor}.}
\tag{0.6}
\]

This report proves the deterministic seam input, not (0.5).  It also does
not prove the stronger \(O(H)\) or \(O(H\log H)\) seam bounds.  The proved
\(O(H^{3/2})\) bound is already quantitatively sufficient for coefficient
one under the Catalan residence-packing hypothesis (0.5).

## 1. The crossing triangle at one cut

Let

\[
 \ldots,X_{-2},X_{-1}\mid X_0,X_1,\ldots
\tag{1.1}
\]

be the cyclic owner order opened at a cut between \(X_{-1}\) and \(X_0\).
Every \(X_i\) is an \((m+1)\)-set and consecutive owners are Johnson
adjacent.  A projected PBBS cycle has length at least \(2m+1\).  Since
\(H\le m\), the collar from \(X_{-H}\) through \(X_{H-1}\) has length
\(2H<2m+1\), so it has no wrap ambiguity.

For integers

\[
 a,b\ge1,
 \qquad 2\le a+b\le H+1,
\tag{1.2}
\]

put

\[
 L_{a,b}:=\bigcap_{i=-a}^{b-1}X_i,
 \qquad
 U_{a,b}:=\bigcup_{i=-a}^{b-1}X_i.
\tag{1.3}
\]

These are exactly the lower and upper owner windows crossing this cut and
having between two and \(H+1\) owners.  The upper family is immediate.
The literal owner word

\[
 \boxed{X_{-H},X_{-H+1},\ldots,X_{-1},X_0,\ldots,X_{H-1}}
\tag{1.4}
\]

has length \(2H\), and \(U_{a,b}\) is the OR of its contiguous subword from
\(X_{-a}\) through \(X_{b-1}\).

It remains to compress the lower triangle \((L_{a,b})\).

## 2. Exact Pascal identity and its failures

### Lemma 2.1 (facet-child identity)

For \(a,b\ge1\) with \(a+b\le H\), each of

\[
 L_{a+1,b},\qquad L_{a,b+1}
\tag{2.1}
\]

is either \(L_{a,b}\) or a facet of \(L_{a,b}\).  Moreover

\[
 L_{a+1,b}\cup L_{a,b+1}=L_{a,b}
\tag{2.2}
\]

unless there is one coordinate \(x\) whose maximal positive owner run
through the cut is exactly

\[
 X_{-a},X_{-a+1},\ldots,X_{b-1}.
\tag{2.3}
\]

In the exceptional case both children in (2.1) are the same proper facet
\(L_{a,b}\setminus\{x\}\).

#### Proof

Because \(L_{a,b}\subseteq X_{-a}\) and \(X_{-a-1},X_{-a}\) are Johnson
adjacent, intersecting \(L_{a,b}\) with \(X_{-a-1}\) deletes at most the
unique coordinate in \(X_{-a}\setminus X_{-a-1}\).  Hence
\(L_{a+1,b}\) is the parent or one of its facets.  The right child is
handled identically using \(X_{b-1},X_b\).

The union of two subsets each obtained from a set by deleting at most one
coordinate can be smaller than the parent only when both delete the same
coordinate \(x\).  This says precisely

\[
 x\notin X_{-a-1},
 \quad
 x\in X_{-a}\cap\cdots\cap X_{b-1},
 \quad
 x\notin X_b,
\tag{2.4}
\]

which is (2.3).  The converse is immediate. \(\square\)

Call \((a,b)\) a **failure** when (2.2) fails.  Only failures with
\(a+b\le H\) matter, since depth \(H+1\) will be emitted literally.

### Lemma 2.2 (at most \(H-1\) failures)

At one cut,

\[
 \boxed{|\mathcal F|\le H-1.}
\tag{2.5}
\]

#### Proof

A failure \((a,b)\) is labelled by the coordinate removed at the transition

\[
 X_{b-1}\longrightarrow X_b.
\tag{2.6}
\]

For a fixed \(b\), that transition removes only one coordinate.  Its most
recent insertion before the cut uniquely determines \(a\), so two failures
cannot have the same \(b\).  Since

\[
 a,b\ge1,\qquad a+b\le H,
\tag{2.7}
\]

one has \(1\le b\le H-1\).  This proves (2.5). \(\square\)

No laminarity, nesting, or ordering of the failure runs is assumed.

## 3. The exact diagonal stopping lemma

For \(2\le R\le H+1\), define the depth-\(R\) diagonal word

\[
 \mathcal W_R=
 (L_{1,R-1},L_{2,R-2},\ldots,L_{R-1,1}).
\tag{3.1}
\]

A failure \((u,v)\) is a descendant of \((a,b)\) when

\[
 u\ge a,\qquad v\ge b.
\tag{3.2}
\]

Put

\[
 \rho(a,b)=
 \min\{u+v:(u,v)\in\mathcal F, u\ge a, v\ge b\},
\tag{3.3}
\]

with \(\rho(a,b)=+\infty\) when the set is empty.

### Lemma 3.1 (failure-stopped Pascal expansion)

If

\[
 a+b\le R\le H+1,
 \qquad R\le\rho(a,b),
\tag{3.4}
\]

then

\[
 \boxed{
 L_{a,b}=\bigcup_{j=a}^{R-b}L_{j,R-j}.}
\tag{3.5}
\]

The right side is the OR of one contiguous interval of \(\mathcal W_R\).
Equality is allowed in \(R=\rho(a,b)\): failures at depth \(R\) are
literal leaves of the expansion and do not break it.

#### Proof by Pascal induction

Induct on \(R-a-b\).  The zero case is tautological.  If the difference is
positive, then \((a,b)\) cannot be a failure: its depth \(a+b\) is strictly
less than \(R\le\rho(a,b)\).  Lemma 2.1 gives

\[
 L_{a,b}=L_{a+1,b}\cup L_{a,b+1}.
\tag{3.6}
\]

Every failure descendant of either child is also a failure descendant of
the parent, so the induction hypothesis applies to both children at the
same terminal depth \(R\).  Their diagonal index intervals are

\[
 [a+1,R-b],qquad [a,R-b-1].
\tag{3.7}
\]

Their union is the full interval \([a,R-b]\), proving (3.5). \(\square\)

The equality case in Lemma 3.1 is the decisive point.  It permits the
construction to stop at the first failure depth instead of repairing every
ancestor separately.

## 4. Slab construction and the \(O(H^{3/2})\) word

Partition the depth set

\[
 \{2,3,\ldots,H+1\}
\tag{4.1}
\]

into consecutive slabs, each containing at most \(\Delta\) depths.  For
every slab, let \(R\) be its terminal depth and append the full word
\(\mathcal W_R\).  There are \(\lceil H/\Delta\rceil\) slabs and every
full diagonal has length at most \(H\), so these words cost at most

\[
 H\left\lceil{H\over\Delta}\right\rceil.
\tag{4.2}
\]

For every failure \(f=(u,v)\), put

\[
 p_f=u+v
\tag{4.3}
\]

and append the local depth-\(p_f\) diagonal segment

\[
 \mathcal V_f=
 \bigl(L_{j,p_f-j}\bigr)_
 {\max(1,u-\Delta+1)\le j\le
  \min(p_f-1,u+\Delta-1)}.
\tag{4.4}
\]

It has length at most \(2\Delta-1\).  By Lemma 2.2, all local segments cost
at most

\[
 (H-1)(2\Delta-1).
\tag{4.5}
\]

### Theorem 4.1 (literal lower-seam chart)

The concatenation of the full slab-terminal diagonals and the local
failure segments exposes every \(L_{a,b}\) in (1.2).  Its length is at most

\[
 \boxed{
 C^-_{\rm seam}(H,\Delta)
 \le
 H\left\lceil{H\over\Delta}\right\rceil
 +(H-1)(2\Delta-1).}
\tag{4.6}
\]

#### Proof

Fix \((a,b)\), put \(p=a+b\), and let \(R\) be the terminal depth of the
slab containing \(p\).

If \(\rho(a,b)\ge R\), Lemma 3.1 gives

\[
 L_{a,b}=\bigcup_{j=a}^{R-b}L_{j,R-j},
\tag{4.7}
\]

which is a contiguous interval of the emitted word \(\mathcal W_R\).

Suppose instead that \(\rho(a,b)<R\).  Choose a minimum-depth descendant
failure

\[
 f=(u,v),qquad p_f=u+v=\rho(a,b).
\tag{4.8}
\]

The target depth \(p\) and \(p_f\) lie in the same slab, so

\[
 d:=p_f-p=(u-a)+(v-b)\le\Delta-1.
\tag{4.9}
\]

Apply Lemma 3.1 with terminal depth \(p_f\):

\[
 L_{a,b}=\bigcup_{j=a}^{p_f-b}L_{j,p_f-j}.
\tag{4.10}
\]

The required index interval is contained in the local segment (4.4), since

\[
 a=u-(u-a)\ge u-d\ge u-\Delta+1
\tag{4.11}
\]

and

\[
 p_f-b=u+(v-b)\le u+d\le u+\Delta-1.
\tag{4.12}
\]

Therefore (4.10) is one contiguous subword of \(\mathcal V_f\).

This argument permits arbitrarily many tied minimum-depth failures.  The
entire diagonal interval in (4.10), not merely the chosen failure leaf, is
present in \(\mathcal V_f\).  Deeper failures are already carried inside
the literal sets on the depth-\(p_f\) diagonal.  Thus no laminarity or
single-failure assumption is hidden in the proof. \(\square\)

Combining Theorem 4.1 with the upper word (1.4) proves (0.3).  For
\(\Delta=\lceil\sqrt H\rceil\), one has

\[
 \left\lceil{H\over\Delta}\right\rceil\le\Delta,
 \qquad
 \Delta\le\sqrt H+1.
\tag{4.13}
\]

Hence

\[
\begin{aligned}
 C_{\rm seam}(H,\Delta)
 &\le 2H+H\Delta+(H-1)(2\Delta-1)\\
 &\le 3H^{3/2}+4H,
\end{aligned}
\tag{4.14}
\]

which proves (0.4).

### Nonzero and integral audit

Every letter of (1.4) has size \(m+1\).  A lower-chart letter
\(L_{j,R-j}\) is the intersection of \(R\le H+1\) Johnson-adjacent owners.
Starting with its first owner, at most one current coordinate can be lost
at each of the \(R-1\le H\) transitions.  Therefore

\[
 |L_{j,R-j}|
 \ge m+1-(R-1)
 \ge m+1-H
 \ge1.
\tag{4.15}
\]

Thus every emitted letter is a genuine nonempty subset.  All unions in the
proof are literal ORs of consecutive emitted letters.  There is no
averaging, fractional state, common-owner synchronization, or mixing of
exact factors.

## 5. Several cuts and the global PBBS band ledger

The seam charts may be appended independently for different cuts.  This
does not require the cuts to be \(H\)-separated.  A window crossing several
cuts is restored by the chart of each such cut, and duplicate restoration
is harmless.

Let a projected cycle of length \(\ell\) be cut at \(J\ge1\) transition
edges hitting all positive residence intervals of length at most \(H\).
The endpoint-capped erosion words on its \(J\) path fragments have total
length

\[
 \ell+HJ.
\tag{5.1}
\]

They expose every owner window lying within a fragment.  Appending one seam
chart for each cut exposes every original window which crosses a cut.
Hence this one cycle is replaced by a literal word of length at most

\[
 \ell+(H+C_{\rm seam}(H))J.
\tag{5.2}
\]

Return now to the PBBS factor.  Let \(c_2(P_m)\) be the number of projected
step-two cycles and let \(\nu_H(P_m)\) be the summed circular residence
packing number from the audited reduction.  On every active cycle choose a
minimum circular-interval transversal.  Since an active cycle has packing
number at least one,

\[
 J_H:=\sum_{C\ {\rm active}}J_C
 \le2\nu_H(P_m).
\tag{5.3}
\]

Inactive cycles use the cyclic erosion word of length \(\ell+2H\).  Since

\[
 c_2(P_m)\le B_m,
\tag{5.4}
\]

equations (0.4), (5.2), and (5.3) give the following unconditional transfer.

### Theorem 5.1 (subquadratic PBBS cut transfer)

For every \(1\le H\le m\), there is a nonzero literal word covering all
ranks

\[
 m-H+1,m-H+2,\ldots,m+H+1
\tag{5.5}
\]

and having length

\[
\begin{aligned}
 L_H
 &\le W+2HB_m
      +2\bigl(3H^{3/2}+5H\bigr)\nu_H(P_m)\\
 &=\boxed{
 W+2HB_m+(6H^{3/2}+10H)\nu_H(P_m).}
\end{aligned}
\tag{5.6}
\]

#### Proof

The unextended owner-cycle lengths sum to \(W\).  The inactive cyclic
extensions cost at most \(2Hc_2(P_m)\le2HB_m\).  On active cycles, (5.2)
adds at most \((H+C_{\rm seam}(H))J_H\).  Apply (0.4) and (5.3).

The all-depth PBBS corridor theorem proves complete correct support for the
uncut consecutive owner masks in every rank in (5.5).  Any selected correct
occurrence either remains within a cut fragment and is exposed by endpoint
erosion, or crosses a cut and is exposed by the corresponding seam chart.
Thus the constructed word covers (5.5). \(\square\)

## 6. Conditional coefficient-one consequence

### Theorem 6.1

Assume that for every fixed \(A>0\) there are constants \(K_A<\infty\) and
\(M_A\) such that

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)\le K_AB_m
 \qquad(m\ge M_A).
\tag{6.1}
\]

Then (0.6) holds.

#### Proof

Fix \(A\) and put \(H=\lceil A\sqrt m\rceil\).  For all sufficiently large
\(m\), \(H\le m\).  Divide (5.6) by \(W=(2m+1)B_m\).  Equation (6.1) gives

\[
 {L_H-W\over W}
 \le {2H\over2m+1}
 +K_A{6H^{3/2}+10H\over2m+1}
 =O_A(m^{-1/4}).
\tag{6.2}
\]

Thus, for every fixed \(A\), the PBBS word covers the depth-\(A\sqrt m\)
central band with normalized excess tending to zero.

Use now the already audited fixed-\(A\) diagonalization and exact
symmetric-chain-product tail theorem.  In its quantified form, the latter
provides tail words outside the depth-\(j\sqrt m\) band whose normalized
limsup is \(\varepsilon_j\), where \(\varepsilon_j\to0\) as
\(j\to\infty\).  For each positive integer \(j\), choose a threshold
\(M_j'\) beyond which both the central excess in (6.2) is at most \(1/j\)
and the tail excess is at most \(\varepsilon_j+1/j\).  Increase the
thresholds to be strictly increasing, and take \(j=j(m)\) constant on
successive intervals \([M_j',M_{j+1}')\).  Then

\[
 j(m)\longrightarrow\infty
\tag{6.3}
\]

while every application of (6.1) is made only after its fixed-\(j\)
threshold.  Concatenating the central PBBS word with the two product-SCD
tail words has total length

\[
 W+o(W).
\tag{6.4}
\]

This proves coefficient one in odd dimension.  The standard trimmed
one-coordinate lift gives the same leading constant in even dimension.
\(\square\)

The product-SCD tail is essential in this last step.  Literal enumeration
of all outer subsets at fixed \(A\) would not have normalized cost \(o(1)\).

## 7. Independent audit of the decisive stopping identity

The proof of Lemma 3.1 was independently rederived coordinatewise, without
using Pascal induction.

Fix \(x\in L_{a,b}\).  Let its maximal positive run through the cut be

\[
 X_{-u},X_{-u+1},\ldots,X_{v-1},
 \qquad u\ge a,\quad v\ge b,
\tag{7.1}
\]

with an infinite endpoint allowed if the run leaves the local collar.  For
an index \(j\in[a,R-b]\),

\[
 x\in L_{j,R-j}
\quad\Longleftrightarrow\quad
 j\le u\ \hbox{ and }\ R-j\le v.
\tag{7.2}
\]

Such a \(j\) exists if and only if

\[
 R-v\le u,
 \quad\hbox{equivalently}\quad R\le u+v.
\tag{7.3}
\]

The first depth at which \(x\) disappears from the whole descendant
diagonal is therefore one more than the length \(u+v\) of its maximal
crossing run.  At depth \(R=u+v\), the leaf \(j=u\) still contains \(x\).
This proves exactly the equality case in Lemma 3.1.

It also audits the multiple-failure issue.  If several descendant failures
tie at the minimum depth \(p_f\), each corresponding coordinate occurs in
its own literal leaf on the depth-\(p_f\) interval in (4.10).  The interval
has only

\[
 p_f-(a+b)+1\le\Delta
\tag{7.4}
\]

leaves, so all tied failures lie in the same emitted local segment.
Coordinates whose failures are deeper than \(p_f\) satisfy
\(p_f<u+v\) and hence occur in at least one of those same leaves by (7.3).
Thus neither incomparable failures nor nested failures create an omitted
coordinate.

The remaining audit points are as follows.

1. A failure has owner length at most \(H\), not \(H+1\), because the
   depth-\(H+1\) diagonal is emitted literally.
2. Failure injection uses the distinct right departure transitions
   \(X_{b-1}\to X_b\), giving the exact cap \(H-1\).
3. Every local witness interval is wholly inside the displayed local word
   by the two separate endpoint inequalities (4.11)--(4.12).
4. The cycle-length inequality \(2H<2m+1\) prevents an accidental second
   traversal of the cut collar.
5. Every chart letter is nonzero by (4.15), even when its mask has the
   wrong rank.  Correct rank is needed only in the pre-existing support
   theorem, not in the seam identity.
6. Nearby cuts do not require synchronized charts, because the final word
   is a concatenation and each destroyed window is restored in at least
   one whole chart block.

The decisive step therefore survives an independent coordinate audit.

## 8. Final proved and unproved boundary

### Proved

1. Upper crossing unions cost exactly one \(2H\)-owner local word per cut.
2. Lower crossing intersections form the exact Pascal triangle of
   Lemma 2.1.
3. Its failures are exactly short positive coordinate runs crossing the
   cut, with at most \(H-1\) failures per cut.
4. Slab-terminal diagonals plus minimum-failure local diagonals give the
   literal bound (0.3), hence \(O(H^{3/2})\) per cut.
5. All emitted letters are integral and nonzero, and every asserted target
   is the OR of a literal contiguous subword.
6. The PBBS central-band word obeys the exact global ledger (5.6).
7. The fixed-window Catalan packing hypothesis (6.1), for every fixed
   \(A\), now suffices for coefficient one after the frozen
   diagonalization and product-SCD tails.

### Not proved

1. The residence estimate (6.1).
2. An \(O(H)\) or \(O(H\log H)\) deterministic seam.
3. Any converse saying that a subquadratic seam forces Catalan residence
   packing.
4. Any claim that every crossing window has correct rank.  The construction
   only needs, and proves, literal coverage of all windows; the existing
   PBBS corridor theorem supplies complete correct support.

There is therefore no remaining deterministic \(H^2\)-seam obstruction in
the PBBS lane.  The surviving coefficient-one gate is the Catalan-scale
residence packing estimate (6.1).
