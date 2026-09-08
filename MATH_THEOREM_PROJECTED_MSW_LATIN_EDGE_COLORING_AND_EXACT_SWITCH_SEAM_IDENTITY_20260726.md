# RETRACTED: tagged projected-MSW switch--seam identity

> **Retraction (2026-07-26).**  This note treats a selected physical tag as
> if it uniquely determined the active translated directed-arc orbit.
> That is false: several tags can represent the same translation orbit.
> A colour may therefore preserve the physical MSW continuation through a
> differently coloured tag.  Consequently the tagged identities in
> Sections 3, 9--11 and all reductions based on them are not valid without
> an additional orbit-injectivity hypothesis.  The corrected theorem is
> `MATH_THEOREM_MSW_NECKLACE_EDGE_COLORING_SWITCH_AND_H_WINDOW_GATE_20260726.md`,
> which uses orbit activities and proves \(|B_c|=p s_c\).  Section 8's
> independent audit of the published two-level saturating cycle remains
> valid, but the file as a whole must not be cited as a theorem.

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let \(p=2m+1\) be prime, let

\[
                         W=\binom pm,\qquad T=W/p,
\]

and orient every row of an exact MSW wreath factor \(F\).  Project the
physical arcs to the translation-necklace quotient, retaining one
parallel copy for every physical arc.  Splitting every quotient vertex
into a source and a target copy gives a \(p\)-regular bipartite
multigraph

\[
                         B_F.
\]

Every proper \(p\)-edge-colouring of \(B_F\) has two exact
interpretations.

1. Each colour class is a perfect matching of \(B_F\), hence a directed
   simple-support quotient cycle cover.  Its voltage lift is a
   translation-invariant spanning simple two-factor of the physical odd
   graph.  Thus proper colouring repairs the parallel-copy gap in the
   arbitrary-long-cycle proposal.
2. Read the colours cyclically around every original MSW row.  Let
   \(S(c)\) be the total number of colour changes.  For colour \(\alpha\),
   let \(s_\alpha\) be the number of quotient junctions of its cycle cover
   which do not continue along one original MSW row, and let
   \(b_\alpha=ps_\alpha\) be the number of physical lifted seams.  Then

   \[
    \boxed{
       \sum_{\alpha\in\mathbb F_p}s_\alpha=S(c),
       \qquad
       \sum_{\alpha\in\mathbb F_p}b_\alpha=pS(c).}
    \tag{0.1}
   \]

   Consequently

   \[
                         \boxed{\min_\alpha b_\alpha\le S(c).}
   \tag{0.2}
   \]

This makes the exact positive target transparent:

> **Low-switch Latin colouring (open).**  Find a proper
> \(p\)-edge-colouring of \(B_F\) with
> \[
>                              S(c)=O(T).
> \tag{0.3}
> \]

If \(H=o(p)\), (0.2) then gives one invariant physical factor with
\(O(T)=o(W/H)\) seams.  Away from their \(H\)-collars, its cycles are
literal translations of long MSW row segments and are therefore
\(H\)-safe.  The affected-start collar volume is

\[
                         O(HS(c))=O(HT)=o(W).
\tag{0.4}
\]

Its every-second Johnson factor also has \(O(T+S(c))=O(T)=o(W/H)\)
components.

The proper colouring exists unconditionally by König's line-colouring
theorem; the low-switch bound does not.  It is a minimum-cost
one-factorization problem, equivalently a near-resolution of the MSW
row--necklace incidence system.  The elementary lower bounds proved here
are only polynomial and do not rule out (0.3).  Nor does (0.3) by itself
prove the required aggregate shadow coverage: that remains a separate
target-distribution condition on the selected colour class.

## 1. The projected oriented factor

Let \({\cal N}_m\) be the \(T\) translation necklaces of middle sets.
For each necklace \(O\), make a left vertex \(O_L\) and a right vertex
\(O_R\).

Every oriented physical MSW arc

\[
                              e:X\longrightarrow Y
\tag{1.1}
\]

gives one edge

\[
                    \bar e: [X]_L\longrightarrow[Y]_R
\tag{1.2}
\]

of \(B_F\).  Distinct physical arcs are retained as distinct parallel
copies.  Each copy remembers its quotient voltage, equivalently the
phases of \(X\) and \(Y\) relative to fixed necklace representatives.

### Proposition 1.1 (exact regularity)

\[
                         d_{B_F}(O_L)=d_{B_F}(O_R)=p
\tag{1.3}
\]

for every necklace \(O\).

#### Proof

The fibre \(O\) contains exactly \(p\) physical middle sets.  Every one
has exactly one outgoing and one incoming arc in the oriented factor
\(F\).  Projection retains all those copies.  \(\square\)

Therefore \(B_F\) is a \(p\)-regular bipartite multigraph.  König's
theorem gives a proper edge-colouring

\[
                         c:E(B_F)\longrightarrow\mathbb F_p
\tag{1.4}
\]

with exactly \(p\) colours.  At each left and each right vertex, every
colour occurs exactly once.

### Equivalent physical formulation

Identify an oriented arc with its source owner \(X\).  Then \(c\) is a
map from physical middle owners to \(\mathbb F_p\) such that

* \(c\) is a permutation of the colours on every translation necklace;
* \(c\) is a permutation of the colours on the set of predecessors of
  every translation necklace under the MSW successor.

This is the exact Latin condition.  It is stronger than merely balancing
the number of edges of each colour.

## 2. One colour gives a valid invariant factor

Fix \(\alpha\in\mathbb F_p\).  At each \(O_L\) there is one outgoing
edge copy of colour \(\alpha\), and at each \(O_R\) there is one incoming
copy.  Hence the colour class \(M_\alpha\) is a perfect matching of
\(B_F\), or equivalently a directed cycle cover of the unsplit quotient
vertices.

### Theorem 2.1 (proper colour eliminates doubled voltage edges)

The voltage lift \(G_\alpha\) of \(M_\alpha\) is a
translation-invariant spanning simple two-factor of \(O_m\).

#### Proof

Parallel copies in \(B_F\) share both endpoints, so a proper edge
colouring assigns them different colours.  Thus \(M_\alpha\) uses at most
one copy of every quotient voltage edge orbit.  Its degree is one on the
left and one on the right at every quotient vertex.  Lifting the selected
voltage edges therefore gives one outgoing and one incoming *distinct*
physical edge at every middle owner.  This is a spanning simple directed
two-factor, invariant under translation.  \(\square\)

This closes the precise gap left by an arbitrary multigraph
two-factorization: proper colours separate all copies of one physical
edge orbit.

## 3. Original-row switches and inherited junctions

For a physical owner \(X\), write

\[
              e_X^-:F^{-1}X\to X,\qquad e_X^+:X\to FX
\tag{3.1}
\]

for its incoming and outgoing MSW arcs.  Define the switch indicator

\[
 \operatorname{sw}_c(X)
   =\mathbf1_{\{c(e_X^-)\ne c(e_X^+)\}},
\tag{3.2}
\]

and the total cyclic row-switch count

\[
                         S(c)=\sum_X\operatorname{sw}_c(X).
\tag{3.3}
\]

This is exactly the number of colour changes read around all \(T\)
oriented MSW \(p\)-cycles.

At one quotient necklace \(O\), colour \(\alpha\) chooses one incoming
copy \(e_{\alpha,O}^-\) and one outgoing copy \(e_{\alpha,O}^+\).  Call
the quotient junction **inherited** when these two copies are
\(e_X^-,e_X^+\) for the same physical owner \(X\in O\).  Otherwise call
it a **quotient seam**.  Let

\[
 s_\alpha
   =\#\{O\in{\cal N}_m:
          \text{the \(\alpha\)-junction at \(O\) is a seam}\}.
\tag{3.4}
\]

### Theorem 3.1 (exact switch--seam identity)

\[
 \boxed{
             \sum_{\alpha}s_\alpha=S(c).}
\tag{3.5}
\]

The lift of every quotient seam consists of exactly \(p\) physical seam
junctions.  Therefore, with

\[
                         b_\alpha=ps_\alpha,
\tag{3.6}
\]

one has

\[
 \boxed{
       \sum_\alpha b_\alpha=pS(c),
       \qquad
       \min_\alpha b_\alpha\le S(c).}
\tag{3.7}
\]

#### Proof

There are \(pT=W\) pairs \((\alpha,O)\).  A nonswitch owner \(X\) with

\[
                         c(e_X^-)=c(e_X^+)=\alpha
\tag{3.8}
\]

creates one inherited \((\alpha,[X])\)-junction.

This correspondence is injective.  If two owners in the same necklace
gave inherited junctions of the same colour, the corresponding incoming
copies would repeat colour \(\alpha\) at one right vertex and the
outgoing copies would repeat it at one left vertex, contradicting proper
colouring.  It is also surjective onto inherited junctions by definition.
Hence the total number of inherited pairs is exactly

\[
                         W-S(c).
\tag{3.9}
\]

Subtracting this from the \(W\) pairs \((\alpha,O)\) proves (3.5).

One quotient voltage junction lifts equivariantly at every one of the
\(p\) phases of its necklace.  It is inherited at all phases or at none,
so a quotient seam gives exactly \(p\) physical seams.  This proves the
first identity in (3.7); averaging over the \(p\) colours proves the
second.  \(\square\)

The theorem is exact even when an MSW row revisits one necklace: proper
colouring prevents two visits from being inherited in the same colour.

## 4. Long inherited segments and the \(H\)-collar cost

A maximal monochromatic interval on an original row lifts, in its colour
class, to all \(p\) coordinate translates of that literal MSW row
interval.  Consecutive arcs inside it retain the original omitted-label
permutation, so every every-second Johnson window lying at distance at
least \(2H\) odd arcs from a seam is \(H\)-safe.

### Proposition 4.1 (one good colour)

For some colour \(\alpha\), all but

\[
                         O(H S(c))
\tag{4.1}
\]

physical starts of \(G_\alpha\) lie in inherited \(H\)-safe interiors.

#### Proof

Choose \(\alpha\) with \(b_\alpha\le S(c)\) by (3.7).  A seam can be met
by a length-\(2H\) omitted-label window from only \(O(H)\) cyclic starts.
Outside this collar the complete window lies in one translated MSW row.
Summing over the \(b_\alpha\) seams gives (4.1).  \(\square\)

If \(S(c)=O(T)\) and \(H=o(p)\), then

\[
                  HS(c)=O(HT)=O(HW/p)=o(W).
\tag{4.2}
\]

The bad collars therefore occupy the correct \(o(W)\) start scale.  This
is one common collar over all depths, not an independent \(O(H)\) set of
starts at each depth.  Turning that quarantine into a literal word at
the same cost still uses the separate compiler/seam interface and is not
proved by the colouring identity alone.

### Proposition 4.2 (component count from seams)

For the same colour \(\alpha\), the every-second Johnson lift has

\[
                         O(T+b_\alpha)
                         =O(T+S(c))
\tag{4.3}
\]

components.

#### Proof

A quotient component with no seam is the projection of one complete
original MSW row.  It has length \(p\), voltage zero, and lifts to \(p\)
physical wreaths.  Since such quotient components are vertex-disjoint,
there are at most \(T/p\) of them, contributing at most \(T\) physical
components.

Every other quotient component contains a seam, so there are at most
\(s_\alpha\) of them.  Each voltage cycle lifts to at most \(p\) physical
cycles, and every-second traversal splits each into at most two Johnson
cycles.  Their contribution is at most

\[
                         2p s_\alpha=2b_\alpha.
\]

This proves (4.3).  \(\square\)

Thus (0.3) simultaneously gives \(o(W)\) collar cost and
\(o(W/H)\) components:

\[
 {T\over W/H}={H\over p}=o(1).
\tag{4.4}
\]

It does **not** prove aggregate necklace coverage.  Interior flags are
translations of MSW flags, but different long segments may use different
translations; showing that their union fills almost every target necklace
is an additional global statement.

## 5. The exact minimum-switch problem

Let

\[
                         S_{\min}(F,\rho)
  =\min\{S(c):c\text{ is a proper \(p\)-edge-colouring of }B_F\}.
\tag{5.1}
\]

Equivalently, a proper colouring is a one-factorization

\[
                         E(B_F)=M_0\dot\cup\cdots\dot\cup M_{p-1}.
\tag{5.2}
\]

For each physical owner \(X\), its transition pair
\(\{e_X^-,e_X^+\}\) earns one unit exactly when both edges lie in the
same \(M_\alpha\).  Hence

\[
 \boxed{
 S_{\min}
 =W-\max_{(5.2)}
   \sum_{\alpha}\#\{X:e_X^-,e_X^+\in M_\alpha\}.}
\tag{5.3}
\]

This is a quadratic minimum-cost one-factorization, not an ordinary
minimum-cost perfect matching.

There is also an exact segment formulation.  Cutting every MSW row at
its colour changes partitions it into monochromatic cyclic segments.
Every segment is a matching in \(B_F\), and the segments can be assigned
\(p\) colours so that every left and right quotient vertex sees all
colours exactly once.  Conversely every such coloured segment
decomposition is a proper edge-colouring, with total cuts \(S(c)\).

Thus the desired theorem is:

\[
 \boxed{
                         S_{\min}(F,\rho)=O(T).}
\tag{5.4}
\]

No total-unimodularity theorem is implicit: grouping a long segment into
one colour is a hyperedge constraint.

## 6. Two exact lower bounds

The following bounds calibrate the problem but are far below \(T\).

### 6.1 A row-necklace repetition bound

For an MSW row \(C\), put

\[
 \nu_C(O)=|V(C)\cap O|,
 \qquad
 r_C=\max_O\nu_C(O).
\tag{6.1}
\]

If \(r_C\ge2\), the \(r_C\) corresponding outgoing edges are incident
with one left vertex of \(B_F\), so properness forces \(r_C\) distinct
colours on the row.  A nonconstant cyclic word using \(r_C\) colours has
at least \(r_C\) switches.  Therefore

\[
 \boxed{
 S(c)\ge
 \sum_{C:r_C\ge2}r_C.}
\tag{6.2}
\]

In particular an AP row, for which \(r_C=p\), costs at least \(p\)
switches.  There are only polynomially many possible AP anomalies, so
this does not threaten (5.4).

Writing

\[
 P_C=\sum_O\binom{\nu_C(O)}2,
\tag{6.3}
\]

the elementary inequality

\[
 P_C\le{p(r_C-1)\over2}
\tag{6.4}
\]

also gives

\[
 S(c)\ge
 \sum_{C:r_C\ge2}\left(1+{2P_C\over p}\right)
\tag{6.5}
\]

after taking integer ceilings where needed.

### 6.2 The Catalan residue bound

Call a row constant when all its \(p\) arcs have one colour, and let
\(R\) be the number of nonconstant rows.  Put

\[
                         r=T\bmod p,\qquad0<r<p.
\tag{6.6}
\]

For one colour \(\alpha\), its perfect matching has exactly \(T\) edges.
Constant \(\alpha\)-rows contribute multiples of \(p\), so the number
of its edges lying on nonconstant rows is congruent to \(r\pmod p\) and
is at least \(r\).  Summing over the \(p\) colours gives

\[
                         pR\ge pr,\qquad R\ge r.
\tag{6.7}
\]

Every nonconstant cyclic row has at least two switches.  Hence

\[
                         \boxed{S(c)\ge2r.}
\tag{6.8}
\]

Since

\[
                         T\equiv2(-1)^m\pmod p,
\tag{6.9}
\]

this is \(S(c)\ge4\) for even \(m\), and
\(S(c)\ge2p-4\) for odd \(m\).  Again this is only polynomial, while
\(T\) is exponential.

### 6.3 A row-hypergraph matching lower bound

On the transversal rows, let \({\cal H}_{\rm row}\) be the hypergraph on
middle necklaces whose edge for row \(C\) is the set of necklaces visited
by \(C\), and let \(\nu({\cal H}_{\rm row})\) be its matching number.
For any one colour, its constant rows have pairwise disjoint necklace
sets, hence form a matching in \({\cal H}_{\rm row}\).  Across all \(p\)
colours there are therefore at most \(p\nu({\cal H}_{\rm row})\) constant
rows.  Every other cyclic row has at least two switches, giving

\[
 \boxed{
 S(c)\ge2\bigl(T-p\nu({\cal H}_{\rm row})\bigr),}
\tag{6.10}
\]

with nontransversal rows automatically counted as nonconstant.

This shows that \(O(T)\) is the natural best general scale.  For example,
in a projective-plane incidence hypergraph every two row edges meet, so
\(\nu=1\) and (6.10) is \(2T-O(p)\), despite exact regularity and an exact
uniform fractional matching.  The bound still does not exclude (5.4);
it calibrates it as an order-sharp integral statement rather than a
consequence of regularity.

## 7. Boundary

Proved:

* the exact \(p\)-regular bipartite projection;
* unconditional proper \(p\)-edge-colourability;
* a simple invariant physical factor from every colour;
* the exact identities (0.1)--(0.2);
* \(O(HS)\) common-collar start volume and \(O(T+S)\) components for one
  colour;
* the minimum-cost one-factorization and segment formulations; and
* two explicit lower bounds, neither close to \(T\).

Open:

* \(S_{\min}(F,\rho)=O(T)\), or any lower bound excluding it;
* simultaneous selection of a low-switch colour with aggregate
  \(o(T)\) quotient shadow holes; and
* a literal repair/compilation implementing all seam collars at the
  claimed common \(O(HS)\) cost.

The low-switch Latin edge-colouring is therefore a genuine new gate.  It
closes the simple-support and component-count problems if proved, while
preserving almost all of the long \(H\)-safe MSW segments.

## 8. The true switch scale and the published two-level saturating cycle

The bound \(S(c)=O(T)\) is a convenient strong target, but it is not the
sharp interface requirement.  Proposition 4.1 uses only

\[
                         \boxed{H S(c)=o(W),}
\tag{8.1}
\]

or equivalently

\[
                         S(c)=o(W/H)=o(pT/H).
\tag{8.2}
\]

Thus, for the usual choice \(H=\sqrt p\,\omega(p)\), one may allow

\[
                         S(c)=o\!\left({\sqrt p\over\omega(p)}T\right).
\tag{8.3}
\]

In particular a polylogarithmic number of switches per MSW row would be
more than sufficient.  This relaxation does not make an arbitrary proper
edge-colouring useful--a generic colouring has order \(p\) switches per
row--but it is the correct quantitative target for subsequent work.

There is a superficially stronger one-component object at depth one.  The
Gregor--Micka--M\"utze saturating-cycle theorem, applied to ranks
\(m-1,m\), gives a simple Johnson cycle

\[
 X_0X_1\cdots X_{N_1-1}X_0,
 \qquad N_1=\binom p{m-1},
\tag{8.4}
\]

on distinct middle owners such that

\[
 \{X_i\cap X_{i+1}:i\in\mathbb Z/N_1\mathbb Z\}
   =\binom{[p]}{m-1}.
\tag{8.5}
\]

It omits only

\[
                         W-N_1={2W\over m+2}=o(W)
\tag{8.6}
\]

middle owners.  After the standard distinct-facet insertion, it becomes
one Hamilton Johnson cycle on all \(W\) middle owners whose lower
depth-one multiplicities are exactly balanced in \(\{1,2\}\).  Therefore
the published theorem *does* solve, with one owner component, the complete
lower depth-one ledger.

It does not replace the Latin low-switch construction.  Put

\[
                         U_i=X_i\cup X_{i+1}.
\tag{8.7}
\]

The saturating theorem says nothing forcing the \(U_i\)'s to be distinct
or even to have \(o(W)\) collision excess.  In the direct odd compiler,
these are precisely the upper depth-one owners.  Appending their missing
targets costs their collision excess, potentially \(\Theta(W)\).  Applying
the central-level theorem to ranks \(m,m+1\) gives the opposite one-sided
object--all \(U_i\)'s exactly once--but gives no lower-intersection ledger.
Using the two cycles separately pays the baseline \(W\) twice.

There is a second, independent incompatibility with the mesoscopic route.
An arbitrary Johnson cycle records only one-coordinate exchanges.  It does
not impose the FIFO/tight-window condition on successive exchanges which
is needed for literal depth \(q>1\).  At depth one every individual edge is
safe, but no long \(H\)-safe MSW segment follows from (8.4).

Consequently the exact missing upgrade is a **two-sided tight saturating
cycle**: one owner cycle (or an \(o(W/H)\)-component path factor) whose
intersection and union ledgers are both near-rainbow and whose successive
exchange labels are tight through the required window.  The published
two-level theorem supplies any one of the two central rainbows, not their
simultaneous occurrence and not the tight memory.  It is therefore a
valuable depth-one pilot, but not a substitute for (8.1) in the final
array construction.

## 9. The full Latin colouring is stronger than necessary

There is a useful final simplification.  For one perfect matching
\(M\subseteq E(B_F)\), define \(s(M)\) exactly as in (3.4): at each
necklace compare the unique selected incoming and outgoing copies and
charge one unless they are consecutive arcs of one physical MSW row.  Put

\[
 s_*(F,\rho)=\min\{s(M):M\text{ is a perfect matching of }B_F\}.
\tag{9.1}
\]

The proof of Theorem 3.1 did not use the other colour classes except to
average.  For every proper edge-colouring,

\[
                         \sum_\alpha s(M_\alpha)=S(c),
\tag{9.2}
\]

and therefore

\[
                         \boxed{s_*\le S_{\min}/p.}
\tag{9.3}
\]

Conversely, a single matching attaining

\[
                         \boxed{s(M)=o(T/H)}
\tag{9.4}
\]

already has the structural consequences sought from the Latin theorem.
Its physical voltage lift has \(ps(M)=o(W/H)\) seams.  Cutting at those
seams, and at the at most \(T/p\) seam-free projected MSW components,
gives

\[
                         o(W/H)
\tag{9.5}
\]

physical Johnson paths/cycles after the every-second lift.  Removing the
common \(H\)-collars costs

\[
                         O(Hp,s(M))=o(W)
\tag{9.6}
\]

physical starts.  All surviving interiors are literal translated MSW
segments.  As before, their aggregate target-collision ledger remains a
separate condition.

Thus the genuinely minimal structural gate is the **minimum-seam perfect
matching** problem (9.4).  Proving a low-switch one-factorization is one
way to obtain it, but is unnecessarily strong: after choosing one good
matching, the other \(p-1\) matchings may have arbitrary switch cost.  An
arbitrary perfect matching extends to a one-factorization because its
complement in \(B_F\) is \((p-1)\)-regular bipartite, but that extension
does not improve or damage the selected factor.

The optimization (9.1) is still nontrivial.  It is a cycle-cover problem
with a transition cost depending jointly on the chosen incoming and
outgoing copy at a necklace; ordinary minimum-cost bipartite matching sees
only individual selected arcs.  Nevertheless (9.4), rather than the full
Latin statement (5.4), is the exact one-colour theorem to attack next.

There is an exact row form of this cost.  For a physical MSW row \(C\),
let

\[
 A_C(M)=\{i\in\mathbb Z_p:\text{the (i)-th oriented arc of (C)
 belongs to (M)}\},
\tag{9.7}
\]

and, when \(A_C\) is a nonempty proper subset, let \(r_C(M)\) be its
number of cyclic interval components.  A full row has no seam and an
unused row contributes nothing.  Since a proper subset of size \(k\)
with \(r\) cyclic runs has exactly \(k-r\) inherited adjacent pairs,

\[
                         \boxed{
 s(M)=\sum_{C:\,0<|A_C(M)|<p}r_C(M).}
\tag{9.8}
\]

Thus (9.4) asks for one quotient perfect matching whose selected arcs are
the union of \(o(T/H)\) cyclic MSW-row intervals, in addition to any
number of complete rows.  This is the cleanest phase-free formulation of
the remaining long-segment gate.

## 10. Equivalent asymptotic long-interval matching gate

The perfect-matching requirement can itself be relaxed to a partial
packing, because an \(o(W)\) middle leave is permitted.  For \(L\le p\),
form the **row-interval hypergraph** \({\cal I}_L\) on the split necklace
set

\[
                         {\cal N}_{m,L}\sqcup{\cal N}_{m,R}.
\tag{10.1}
\]

An edge of \({\cal I}_L\) is the set of left and right endpoints occupied
by a cyclic interval of at least \(L\) consecutive arcs of one MSW row.
Only intervals which are matchings in \(B_F\) are admitted; after deleting
the polynomial nontransversal rows supplied by the prime-cycle averaging
theorem, every row interval is admissible.  Give such a hyperedge weight
equal to its number of arcs.

### Theorem 10.1 (low seams imply an almost-spanning long-interval packing)

Suppose \(H=o(p)\) and perfect matchings \(M=M_m\) satisfy

\[
                         Hs(M)/T\longrightarrow0.
\tag{10.2}
\]

Then there are lengths \(L=L_m\) with

\[
                         H=o(L),\qquad L=o(p),
\tag{10.3}
\]

and a matching in \({\cal I}_L\) of total weight \(T-o(T)\).

#### Proof

Put \(\delta=Hs(M)/T=o(1)\).  If \(\delta=0\), choose
\(L=\lfloor\sqrt{Hp}\rfloor\).  Otherwise choose

\[
 L=H\min\{\delta^{-1/2},(p/H)^{1/2}\},
\tag{10.4}
\]

with harmless rounding.  Then \(L/H\to\infty\), \(L/p\to0\), and
\(Ls(M)=o(T)\).  Use the cyclic run decomposition (9.8), regarding every
complete row as one length-\(p\) interval.  These intervals are mutually
disjoint on both shores of the split necklace graph because they come
from one perfect matching.  Delete every partial run of length below
\(L\).  Its total arc mass is at most \(Ls(M)=o(T)\), proving the claim.
\(\square\)

### Theorem 10.2 (a long-interval packing suffices structurally)

Conversely, suppose some \(L\) satisfies \(L/H\to\infty\) and
\({\cal I}_L\) has a matching \({\cal P}\) with total weight

\[
                         w({\cal P})=T-o(T).
\tag{10.5}
\]

Then its voltage lift, after deleting at most two boundary necklaces per
segment, is a physical packing by literal translated MSW paths which has

\[
 o(W)\text{ omitted middle owners},\qquad
 o(W/H)\text{ path components},
\tag{10.6}

and is \(H\)-safe outside \(o(W)\) starts.

#### Proof

The number of selected segments is at most

\[
                         |{\cal P}|\le T/L=o(T/H).
\tag{10.7}

Delete the two endpoint necklaces when two split-shore segments meet at
one unsplit necklace; this loses \(O(|{\cal P}|)=o(T)\) quotient owners
and makes the open segments vertex-disjoint.  Translation lifting produces
at most \(p|{\cal P}|=o(W/H)\) physical paths.  The uncovered quotient
mass in (10.5), together with the endpoint deletion, lifts to \(o(W)\)
middle owners.  Finally discard an \(H\)-collar at every path end; its
mass is

\[
                         O(Hp|{\cal P}|)=o(W).
\tag{10.8}
\]

Every remaining window lies inside one translated literal MSW row.
\(\square\)

Theorems 10.1--10.2 show that, at the structural level, the low-switch
Latin problem is asymptotically equivalent to an almost-spanning matching
of **long MSW row intervals**.  This removes both the demand for all
\(p\) colours and the demand for exact quotient completion.  It does not
remove the aggregate target-repeat condition: the long intervals must
also have \(o(T)\) total quotient shadow holes after the common collar is
discarded.

## 11. The fractional optimum is exactly seam-free

The new gate is purely integral.  Introduce matching variables \(x_e\)
on \(E(B_F)\), with the usual degree-one equations on both shores, and a
straight-through reward \(z_X\) for every physical owner:

\[
 0\le z_X\le x_{e_X^-},\qquad
 0\le z_X\le x_{e_X^+}.
\tag{11.1}
\]

Maximize \(\sum_Xz_X\).  Since \(B_F\) is \(p\)-regular,

\[
                         x_e={1\over p},\qquad z_X={1\over p}
\tag{11.2}
\]

is feasible and has value \(W/p=T\).  This is optimal, because

\[
 \sum_Xz_X\le\sum_Xx_{e_X^+}=T.
\tag{11.3}
\]

Hence the natural linear relaxation has seam cost exactly zero.  The
positive integral theorem cannot follow from a fractional matching or
from the ordinary bipartite matching polytope alone; it must round the
pair correlations in (11.1).

The same fact has a row-hypergraph form.  Assume for clarity that all MSW
rows are transversal to the chosen necklace partition, and let
\({\cal H}_{\rm row}\) have the \(T\) necklaces as vertices and one
\(p\)-edge for the necklace set visited by each of the \(T\) MSW rows.
Every vertex has degree \(p\).  Therefore

\[
                         y_C={1\over p}\qquad(C\in F)
\tag{11.4}
\]

is an exact fractional perfect matching by complete rows.  Prime-cycle
averaging deletes only polynomially many nontransversal rows, so in the
actual application this statement loses only polynomial mass.

Regularity, linearity, and this exact fractional solution are not by
themselves enough.  A finite projective plane is a uniform regular linear
hypergraph in which every two edges meet: its uniform fractional matching
is exact, while every integral matching has size one.  Thus any rounding
of (11.4) must use the particular recursive/ordered geometry of the MSW
row intervals.  This explains why neither Koenig edge-colouring nor a
generic fractional-to-integral argument proves Theorem 10.2.

## 12. Exact-length interval successor and the shallow-shadow cut

`MATH_THEOREM_LONG_MSW_INTERVAL_MATCHING_AND_SHALLOW_SHADOW_HALL_CUT_20260726.md`
analyzes the structural successor at exact interval length `L`. On the
middle-transversal core, assigning `1/(pL)` to every cyclic
length-`L` interval gives a fractional owner matching of weight `T-o(T)`.
Thus the owner gate has no fractional Hall deficit.

The direct target-support LP does have an explicit dual cut. For the two
signed target layers through depth `Q`, every open interval has at most

\[
                         2(QL-Q^2)
\]

literal target necklaces. Uniform owner price `Q-Q^2/L` therefore gives

\[
 \operatorname {def}_{L,Q}
 \ge2T\left[
 {Q^2\over L}-{Q(Q+1)(Q+2)\over3m}
 \right]_+.
\]

At calibrated `H asymp sqrt(m log m)`, taking `Q=floor(m/L)` shows that
exact-length open intervals require `L >> m^(2/3)` before this direct
missing-shadow deficit is `o(T)`. The cut is fractional and hence survives
every integral owner-packing theorem. It does not cover complete rows or
the surviving range `m^(2/3) << L << m`.
