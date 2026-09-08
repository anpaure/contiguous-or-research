# IRRC16: exact eight-plus-one rainbow-collar absorption

Date: 2026-07-29

Status: proved conditional construction and independent audit.  This note
does not prove IRRC16.

## 1. Exact slack localization

Put

\[
 N=\binom{16}{8}=12870,\qquad
 C=\binom{16}{7}=\binom{16}{9}=11440.
\]

Then

\[
 C={8N\over9},\qquad N-C={N\over9}=1430,\qquad {N\over C}={9\over8}.
\tag{1.1}
\]

Thus one occurrence of every colour on either q1 shore consumes exactly
eight ninths of the factor edges, leaving exactly 1,430 edges for
chronology closure.  Equivalently, if \(y^*\) is the symmetric IRRC16
circulation, then

\[
 y^*={8\over9}y^*+{1\over9}y^*,
\tag{1.2}
\]

where the two terms have, respectively, colour loads \(1\) and \(1/8\).
This is only fractional arithmetic, not a rounding theorem.

For a Johnson edge \(e=XY\), write

\[
 \sigma(e)=X\triangle Y,\quad
 \lambda(e)=X\cap Y,\quad
 \upsilon(e)=X\cup Y.
\]

Full residence through four is equivalent to
\(\sigma(e_i)\cap\sigma(e_j)=\varnothing\) whenever the cyclic edge
distance is at most three.

## 2. Rainbow-path collar theorem

Suppose the middle owners admit a partition into 1,430 oriented paths

\[
 P_i=(X_{i,0},X_{i,1},\ldots,X_{i,8}).
\tag{2.1}
\]

Assume:

1. within every path, swap labels at edge distance at most three are
   disjoint;
2. the 11,440 internal edges have pairwise distinct lower colours; and
3. those edges also have pairwise distinct upper colours.

The last two conditions mean that the internal edges contain exactly one
witness of every q1 colour on both shores.

Define a balanced bipartite connector graph \(\Gamma\), with path terminals
on the left and path initials on the right.  Put \(i^-j^+\in E(\Gamma)\)
when \(X_{i,8}X_{j,0}\) is a Johnson edge and all nine seam comparisons
hold.  If the last three old labels are
\(\alpha_3,\alpha_2,\alpha_1\), the seam label is \(c\), and the first
three new labels are \(\beta_1,\beta_2,\beta_3\), these comparisons are

\[
 c\cap\alpha_t=c\cap\beta_t=\varnothing\quad(1\le t\le3),
\tag{2.2}
\]

and

\[
 \alpha_1\cap\beta_1=
 \alpha_1\cap\beta_2=
 \alpha_2\cap\beta_1=\varnothing.
\tag{2.3}
\]

### Theorem 2.1

If \(\Gamma\) has a fractional perfect matching, then IRRC16 holds.

#### Proof

A fractional perfect matching in a bipartite graph implies Hall and hence
an integral perfect matching \(M\).  Add the 1,430 connector edges of
\(M\) to the internal path edges.  This gives degree two at every owner.
Two connectors are separated by eight internal edges.  Therefore every
pair of factor edges at cyclic distance at most three is either internal
to one path or is one of the nine pairs in (2.2)--(2.3).  The resulting
factor is fully resident.

All lower and upper q1 colours already have permanent internal witnesses,
so connector choice cannot create a hole.  Sliding the three-step history
window gives the required binary IRRC16 circulation.  \(\square\)

This theorem is constructive after the path system is supplied: one
ordinary bipartite max-flow completes it.

For a fixed terminal, at most 25 physical neighbours can occur in
\(\Gamma\).  Indeed the previous three disjoint swaps leave five legal
deletions and five legal insertions.  Future-collar tests can only remove
possibilities.  Thus the 25-in/25-out history regularity becomes a
degree-at-most-25 connector graph; it does not imply Hall.

## 3. Sharp weighted Hall robustness

### Theorem 3.1

Let \(\Gamma=(L,R;E)\) be balanced bipartite, and suppose
\(w:E\to\mathbb R_{\ge0}\) has row and column sums one.

1. \(\Gamma\) has a perfect matching.
2. If \(Z\subseteq E\) and \(w(Z)<1\), then \(\Gamma-Z\) has a perfect
   matching.
3. Let \(Q\) be a matching of size \(t\), with endpoint sets \(L_Q,R_Q\).
   If
   \[
   w(E(L_Q,R_Q))>t-1,
   \tag{3.1}
   \]
   then some perfect matching contains \(Q\).

#### Proof

For \(S\subseteq L\),

\[
 |S|=w(E(S,R))\le |N_\Gamma(S)|,
\]

which proves item 1.  If item 2 fails at \(S\), then
\(|N_{\Gamma-Z}(S)|\le |S|-1\).  Column capacities imply that at least one
unit of \(w\)-mass from \(S\) goes through deleted edges, so \(w(Z)\ge1\),
a contradiction.

For item 3, delete \(L_Q\cup R_Q\).  A residual Hall violation at \(S\)
would force at least one unit of \(w\)-mass from \(S\) into \(R_Q\).
But the total mass entering \(R_Q\) from outside \(L_Q\) is

\[
 t-w(E(L_Q,R_Q))<1.
\]

This is impossible.  Add \(Q\) to a residual perfect matching. \(\square\)

If \(\Gamma\) is \(d\)-regular, \(w_e=1/d\) shows that any \(d-1\)
forbidden connector edges can be absorbed.  In particular, a 25-regular
bank survives 24 arbitrary edge deletions.  The threshold is sharp:
deleting all \(d\) edges at one terminal isolates it.

## 4. Minimum connector trade basis

### Theorem 4.1

Fix a path system satisfying Theorem 2.1.  The difference of any two
connector perfect matchings is a disjoint union of alternating even
cycles.  Toggling any subfamily preserves owner exactness, full residence,
and both q1 palettes.

The smallest nonzero connector trade is an alternating four-cycle,
changing two old and two new seams.  If one alternating cycle changes
\(r\) connectors, the difference of the canonical history lifts has
support at most \(8r\).

#### Proof

The first statement is the standard symmetric-difference decomposition of
two bipartite perfect matchings.  Every replacement connector remains in
\(\Gamma\), and all palette witnesses are internal.

An alternating cycle has length at least four.  For the support bound,
only the \(r\) terminal successors and the first three owner positions
after the \(r\) affected initials can change their memory-three arcs.
The old and new matchings use the same affected initial set.  Hence at
most \(4r\) owner fibres change, with one negative and one positive history
arc in each. \(\square\)

Thus, after exact witness localization, the absorber basis is genuinely
small and its completion polytope is integral.  The unresolved
nonintegrality occurs before this stage.

## 5. A general history-support bound

Let \(F,F'\) be oriented fully resident factors with successor
permutations \(s,s'\), and put

\[
 D=\{X:s(X)\ne s'(X)\}.
\]

### Lemma 5.1

Put \(H=s(D)=s'(D)\), and recursively define

\[
 R_0=H,\qquad R_{j+1}=H\cup s(R_j\setminus D)
                   =H\cup s'(R_j\setminus D).
\tag{5.1}
\]

The selected memory-three history arcs can differ only over
\(D\cup R_2\).  Consequently

\[
 |D\cup R_2|\le4|D|,\qquad
 |\operatorname{supp}(y'-y)|\le8|D|.
\tag{5.2}
\]

#### Proof

Because the two permutations agree off \(D\), bijectivity gives
\(s(D)=s'(D)\).  Immediate predecessors can differ only at owners in
\(H\).  If the immediate predecessor of \(X\notin H\) is common and a
deeper predecessor differs, that common predecessor lies outside \(D\);
there \(s=s'\).  Induction therefore gives \(R_j\) as a containing set for
owners whose first \(j+1\) predecessors can differ.  A memory-three arc
records three predecessors and the outgoing transition, so only
\(D\cup R_2\) can change.

Now \(|H|=|D|\) and
\(|R_{j+1}|\le |H|+|R_j|\), whence \(|R_2|\le3|D|\).
Each affected owner fibre replaces at most one old arc by one new arc,
giving (5.2).
\(\square\)

Direction-coherent path rethreads have the sharper \(8r\) bound above.
A long path reversal can have small physical support and large history
support.

## 6. FRR comparison

For a rank-eight \(U\subset[15]\), changing its selected pair from
\(\{a_U^0,b_U^0\}\) to \(\{a_U,b_U\}\) changes the endpoint vector by

\[
 {\bf1}_{U-a_U}+{\bf1}_{U-b_U}
 -{\bf1}_{U-a_U^0}-{\bf1}_{U-b_U^0}.
\tag{6.1}
\]

Therefore FRR equation (4.10) is exactly physical degree balance, and
(4.11) is exactly lower-colour restoration.  Upper colours stay fixed
because one edge is still selected at each \(U\).  These are necessary
projections of an owner-zero history correction, but not sufficient:
statewise history divergence additionally requires a direction-coherent
rethread and all nine seam tests (2.2)--(2.3).

For the audited 60-orbit proposal:

1. 60 is a minimum positive-collar cut transversal, not a constructed
   rethread.  The saved old-choice-excluded fixed-\(H\) equations are
   already infeasible before residence.
2. The advertised source is outside the legal IRRC16 history graph.  The
   unchanged rail has 2,010 short zero-gaps; the facet rail has 1,425 short
   positive runs and 915 short zero-gaps.  Thus there is no legal source
   circulation from which to take a sparse signed difference.
3. Conditionally, \(r\) direction-coherent seam changes between two
   already fully resident rails would lift to an owner-zero history
   correction of support at most \(8r\).  At 60 translation orbits,
   \(r=900\), giving 7,200 arcs or 480 translation orbits.  This is only a
   conditional support bound.

Adjoining the sixteenth coordinate and taking a complemented second rail
would turn a fully biresident, both-q1-complete K15 factor into a spanning
K16 factor.  One-sign FRR does not satisfy that premise.

## 7. Audit of the companion trade-lattice note

The kernel description and the nine seam conditions in
THREAD_A_IRRC16_HISTORY_TRADE_LATTICE_AND_FRR_EMBEDDING_20260729.md are
correct.  Four scope corrections are required.

1. In the Q8 rung construction, the displayed sixteen-word and the exact
   eight-positive/eight-negative history count require orienting the first
   old cycle as displayed and the second old cycle in reverse.
2. The converse port decomposition must include zero-edge singleton
   pieces for owners on no common directed edge, and wholly common cycles
   should be discarded.  Literal compound-window checking then covers the
   no-common-edge case.
3. The \(8r\) FRR bound requires direction coherence; arbitrary path
   reversals do not satisfy it.
4. Four is the minimum support of a nonzero projected edge-set trade, not
   of every nontrivial history trade.  Orientation changes can project to
   zero.

The Hall-bank reserve condition should also be stated globally: for each
colour \(c\), the total net-negative multiplicity over the whole
support-disjoint bank must be at most \((w_c-1)_+\).  Thus the spent
duplicate occurrences are distinct and at least one baseline occurrence
remains untouched.  With that clarification, the commuting-bank Hall
theorem is valid.

## 8. Exact remaining lemma

The proved sufficient statement is:

> **RFCC16.**  There exists an internally legal, both-q1-rainbow
> eight-path resolution whose connector graph has a fractional perfect
> matching.

Theorems 2.1--4.1 prove that RFCC16 implies IRRC16 and give a robust,
constructive integral completion with a minimum alternating absorber
basis.

RFCC16 is not known and is stronger than unrestricted IRRC16.  No explicit
integral separating cut for the physical 25-regular IRRC16 instance is
known.  The odd \(3\times3\) determinant-two choice matrix remains an
abstract obstruction to any argument using only regularity and the
fractional \(9/8\) margin; it has not been shown to be a separating face of
this physical instance.
