# Two-stutter endpoint wrap: exact window palette and historical-reset gate

Date: 2026-08-01  
Lane: H2, regenerative endpoint sidecar  
Status: exact literal window/cell theorem and conditional reset.  No
owner/q1/Pascal/common-cap realization is asserted.

## 0. Outcome

Fix \(d\ge2\).  Let \(F=\{f_1,\ldots,f_d\}\) be disjoint from an active
aperture \(C\), let \(A\cup B=C\), and let
\(\varnothing\ne K\subseteq C\).  Put

\[
 Z=A\cup\{f_1\},\quad T=B\cup\{f_d\},\quad
 U=C\cup F,\quad D_j=U-\{f_j\}.                           \tag{0.1}
\]

Use the length-\(d\) collars

\[
\begin{aligned}
 Q&=(\{f_{d-1}\},\ldots,\{f_2\},K,Z),\\
 P&=(T,K,\{f_{d-1}\},\ldots,\{f_2\}),                    \tag{0.2}
\end{aligned}
\]

and rotate \(W=PMQ\) to \(W^*=MQP\).  There are exactly \(d\) newly
gained source windows of width \(d+1\), with ordered value multiset

\[
                  \boxed{U,D_{d-1},D_{d-2},\ldots,D_2,U}. \tag{0.3}
\]

Thus “gained \(d\)-window bank” means \(d\) physical windows of width
\(d+1\).  The two \(U\)'s are distinct cells and every internal coatom
occurs once.

The old dropped width-\((d+1)\) bank is not determined by \(P,Q\).  Its
literal values are

\[
 L_k=\bigvee P[k:d]\ \cup\ \bigvee(MQ)[0:k+1],
                         \qquad 0\le k<d.                 \tag{0.4}
\]

It matches the redesigned bank only under the extra multiset identity

\[
 \{\!\{L_k:0\le k<d\}\!\}
       =\{\!\{U,U,D_2,\ldots,D_{d-1}\}\!\}.              \tag{0.5}
\]

Occurrence-labelled use requires the corresponding cell-level Hall
matching, not just (0.5).

The two core letters give an exact contraction interpretation.  Define

\[
                         X_L=K\cup Z,\qquad X_R=T\cup K.   \tag{0.6}
\]

Then \(QP\) is the simultaneous refinement

\[
 X_L\mapsto(K,Z),\qquad X_R\mapsto(T,K)                  \tag{0.7}
\]

of

\[
 (\{f_{d-1}\},\ldots,\{f_2\},X_L,X_R,
       \{f_{d-1}\},\ldots,\{f_2\}).                       \tag{0.8}
\]

Every palette window in (0.3) closes under simultaneous contraction
without changing its OR.  The two endpoint \(U\)-windows each omit one
\(K\), but contain the other \(K\); the stutters insure one another.
Every internal coatom window contains both refined blocks completely.

Consequently, if one Pascal transition simultaneously reassigns every
historical row, contracts \(g\) old essential boundaries, and installs
only (0.7), then

\[
                              \Phi'\le\Phi-g+2.            \tag{0.9}
\]

Full contraction gives \(\Phi'\le2\).  The local theorem does not prove
that antecedent.  For every \(t\) there is a two-block rotation with
identical old and new two-stutter collars, both width banks exactly (0.3),
the complete OR-deck multiset equal at every width, and \(t\) private
essential boundaries in one block, none reclaimed.  Thus even the complete
two-stutter state does not imply an unconditional \(\Phi\le2\) recurrence.

## 1. Exact lost and gained physical cells

For a nonempty word \(R\), write \(\operatorname{Pre}_b(R)\) and
\(\operatorname{Suf}_a(R)\) for its nonempty prefixes and suffixes.

### Theorem 1.1 (global rotation partition)

Between \(W=PMQ\) and \(W^*=MQP\):

1. common cells are exactly
   \(\operatorname{Int}(P)\cup\operatorname{Int}(MQ)\);
2. lost cells are exactly
   \[
          \operatorname{Suf}_a(P)\operatorname{Pre}_b(MQ);
                                                               \tag{1.1}
   \]
3. gained cells are exactly
   \[
          \operatorname{Suf}_a(MQ)\operatorname{Pre}_b(P).      \tag{1.2}
   \]

There are \(d(|M|+d)\) cells in each exceptional family.  The lost values
split as

\[
\begin{array}{ll}
 \bigvee\operatorname{Suf}_a(P)\cup
 \bigvee\operatorname{Pre}_b(M),
     &\text{endpoint in }M,\\[1mm]
 \bigvee\operatorname{Suf}_a(P)\cup\bigvee M\cup
 \bigvee\operatorname{Pre}_b(Q),
     &\text{endpoint in }Q,                              \tag{1.3}
\end{array}
\]

and the gained values as

\[
\begin{array}{ll}
 \bigvee\operatorname{Suf}_a(Q)\cup
 \bigvee\operatorname{Pre}_b(P),
     &\text{new start in }Q,\\[1mm]
 \bigvee\operatorname{Suf}_a(M)\cup\bigvee Q\cup
 \bigvee\operatorname{Pre}_b(P),
     &\text{new start in }M.                              \tag{1.4}
\end{array}
\]

#### Proof

A labelled occurrence sequence is unchanged precisely when it lies in
\(P\), or in the still-consecutive word \(MQ\).  Every other old cell
starts in \(P\) and ends in \(MQ\); every other new cell starts in \(MQ\)
and ends in \(P\).  This proves the partition, counts and formulas.
\(\square\)

In particular \(M\mid Q\) is unchanged.  The width-\((d+1)\)
specialization of (1.1) is (0.4).

### Corollary 1.2 (protected-cut Hall)

Ordinary coverage survives exactly when every lost value occurs in a
common or gained cell.  For a fixed old matching, freeze only assignments
whose labelled cells relocate to distinct admissible cells of \(W^*\).
Put **every unfrozen old row** and every new row in \(R\), and let
\(C_{\rm free}\) be the final cells not used by the frozen assignments.
After all unary cell guards have been imposed, the matching survives
exactly when the literal equality graph satisfies

\[
                         |N(Y)|\ge |Y|\qquad(Y\subseteq R). \tag{1.5}
\]

This is Hall's theorem for the cell-assignment layer.  Coupled
source/global guards which are not edge-local are separate antecedents.
Palette equality (0.5) does not imply upper or common-cap matching safety.

## 2. Local cross-grid and width anti-diagonal

The local \(Q\mid P\) cells are

\[
 G_{a,b}=
     \bigvee\operatorname{Suf}_a(Q)\cup
     \bigvee\operatorname{Pre}_b(P),
                 \qquad 1\le a,b\le d.                   \tag{2.1}
\]

These are \(d^2\) physical cells, though their values may collide.  The
width-\((d+1)\) bank is the anti-diagonal \(a+b=d+1\).  In chronological
order put

\[
                G_k=\bigvee Q[k:d]\cup\bigvee P[0:k+1],
                       \qquad 0\le k<d.                   \tag{2.2}
\]

### Theorem 2.1 (exact two-stutter palette)

\[
 G_0=U,\qquad
 G_k=D_{d-k}\ (1\le k\le d-2),\qquad
 G_{d-1}=U.                                               \tag{2.3}
\]

#### Proof

\(G_0\) contains all of \(Q\) and \(T\), hence \(A\cup B=C\) and every
filler.  Shifting once removes \(f_{d-1}\) while only the right \(K\)
enters.  At each internal shift, \(f_j\) leaves one step before it enters
on the right, so the unique hole walks through
\(f_{d-1},\ldots,f_2\).  The last shift restores every filler.
\(\square\)

Only \(A\cup B=C\) and \(K\subseteq C\) are used; \(A,B\) may overlap.
Two middle prefixes made of different fresh repeated labels give different
old banks (0.4) while leaving (2.3) unchanged.  Hence matching the
redesigned dropped bank is a separate host condition.

### Proposition 2.2 (sharp flag/stutter containment)

The owner-window palette (2.3) needs only \(K\subseteq C\).  In contrast,
the canonical left exclusive ray based at \(A\), the canonical right
exclusive ray based at \(B\), and a literal stutter of the already-existing
letters \(Z,T\) all coexist if and only if

\[
                              K\subseteq A\cap B.           \tag{2.4}
\]

Indeed, every nontrivial left ray contains the adjacent \(K,Z\), so its
active base is \(A\cup K\), equal to \(A\) exactly when \(K\subseteq A\).
Every nontrivial right ray contains \(T,K\), so its base is \(B\cup K\),
equal to \(B\) exactly when \(K\subseteq B\).  Equivalently,
\(X_L=Z\) and \(X_R=T\) in (0.6) exactly under the same two containments.
Thus \(K\subseteq C\) is insufficient for the canonical two-flag claim.

## 3. Mutual contraction insurance

Contract the blocks (0.7).  Every contracted interval has its injective
equal-OR full-block lift.

### Theorem 3.1 (palette contraction)

Every \(G_k\) closes under this contraction with unchanged OR.

For \(1\le k\le d-2\), \(G_k\) contains both \(K,Z\) and \(T,K\)
completely.  \(G_0\) contains the whole left block and only \(T\) from the
right; closure adds a \(K\) already present on the left.  Dually,
\(G_{d-1}\) contains only \(Z\) from the left and the whole right block;
closure adds a \(K\) already present on the right.

For \(d\ge3\), the \(d\) closed cells remain physically distinct.  At
\(d=2\), the two \(U\)-cells coalesce to \(X_LX_R\); there are then no
internal coatom rows.

If \(K\subseteq A\cap B\), then \(X_L=Z,X_R=T\), so these are literal
contained-\(K\) stutters and the canonical two flags are retained.
Otherwise (0.7) remains an exact refinement and the owner palette remains
valid, but the contracted letters are \(X_L,X_R\) and the canonical flag
bases are enlarged as in Proposition 2.2.

This proves OR safety, not flat-source safety.  Contraction changes source
length and the widths of the surviving witnesses.

## 4. Exact conditional reset

Choose a presentation attaining the old state's minimum \(\Phi\), with each
tracked block lying wholly in \(P\) or wholly in \(MQ\).  Choose \(g\) of
its boundaries for contraction and install (0.7).  Freeze only assignments
which relocate to pairwise distinct admissible cells after both operations.
The residual Hall bank contains every unfrozen old **target-to-cell equality
row** and every new equality task, including the required
\(D_2,\ldots,D_{d-1}\) rows and any labelled surplus rows.  Its cell shore
excludes every frozen cell.  Residence, topology and other non-edge-local
conditions are not Hall rows.

### Theorem 4.1 (two-stutter reset)

If this residual equality graph has a saturating matching, the old dropped
bank meets its literal cell requirements, and the combined frozen-plus-
residual assignment and resulting source separately pass every coupled
source-legality, Johnson, deadline/residence, topology and common-cap check,
then

\[
                              \Phi'\le\Phi-g+2.             \tag{4.1}
\]

Thus full old contraction gives \(\Phi'\le2\), and
\(g\ge\theta\Phi\) gives

\[
                       \Phi'\le(1-\theta)\Phi+2.            \tag{4.2}
\]

For the restricted owner-only subsystem whose displaced target rows are
only \(D_2,\ldots,D_{d-1}\), Theorems 2.1 and 3.1 supply the literal local
part of the Hall certificate.  They do not prove that the contracted word
remains a flat depth-\(d\) antecedent.

#### Proof

The retained and residual assignments saturate every row.  Exactly
\(\Phi-g\) old boundaries and the two new boundaries remain.  The
owner-only statement follows from the distinct coatom cells and their
contraction-safe closures.  \(\square\)

## 5. Widthwise-multiset-exact zero-reclaim obstruction

To avoid confusing the local collars with the full rotation blocks, write

\[
                              L=Q,\qquad R=P.             \tag{5.1}
\]

Choose a nonempty private core \(H\), fresh \(a_i,b_i\), and put

\[
 C_i=H\cup\{a_i\},\qquad E_i=H\cup\{b_i\},\qquad
 Y_i=C_i\cup E_i.                                         \tag{5.2}
\]

Let \(\Omega\) be the union of every label in \(L,R,C_i,E_i\).  Define two
full blocks

\[
\begin{aligned}
 {\mathsf R}&=R,\Omega,L,\\
 {\mathsf S}&=R,\Omega,C_1,E_1,\ldots,C_t,E_t,\Omega,L,
                                                               \tag{5.3}
\end{aligned}
\]

and rotate

\[
                     {\mathsf R}{\mathsf S}
                              \longmapsto
                     {\mathsf S}{\mathsf R}.               \tag{5.4}
\]

Both the old cut \({\mathsf R}\mid{\mathsf S}\) and the new cut
\({\mathsf S}\mid{\mathsf R}\) have the literal local collar \(L\mid R\).
Protect every target \(C_i\) at \(C_i\mid E_i\).

### Theorem 5.1 (full two-stutter state with zero reclaim)

For every \(d\ge2,t\ge1\):

1. at every physical width, rotation (5.4) preserves the complete
   interval-OR **multiset**;
2. its old dropped and new gained width-\((d+1)\) banks are both exactly
   (0.3), address by address;
3. every old/new crossing address with both arm lengths at most \(d\) has
   the same literal \(L\mid R\) formula, while every crossing address with
   a longer arm has value \(\Omega\);
4. no nonempty subset of the \(t\) private boundaries can be contracted.

#### Proof

A crossing cell of \({\mathsf R}\mid{\mathsf S}\) with both arm lengths at
most \(d\) is
literally a suffix of the terminal \(L\) and a prefix of the initial \(R\).
The new \({\mathsf S}\mid{\mathsf R}\) seam has the identical formula at
the same arm pair.  If either arm is longer than \(d\), it reaches the
nearest \(\Omega\) inside its block, so its value is \(\Omega\) at both
seams.

Internal intervals of \({\mathsf R}\) and \({\mathsf S}\) are unchanged.
For crossing intervals of a fixed width \(w=a+b\), transposition
\((a,b)\mapsto(b,a)\) bijects the old and new arm domains because the two
block lengths are exchanged.  Inside the \(d\times d\) arm square, the
same-address formulas already give identical multisets.  Outside that
square every value is \(\Omega\), and transposition preserves its
multiplicity at each \(w\).  This proves row 1.  At width \(d+1\), both
arms are at most \(d\), so the old and new banks coincide address by
address; Theorem 2.1 gives (0.3).

Contracting \(C_i,E_i\) produces \(Y_i\), which contains the extra private
bit \(b_i\).  No other singleton equals \(C_i\), and every longer interval
containing \(H\) has an extra private, aperture, or \(\Omega\) bit.  Hence
\(C_i\) disappears, independently for every \(i\).  \(\square\)

Thus even exact old/new two-stutter palette equality, complete short-arm
identity, and widthwise equality of the full OR-deck multiset do not erase
unrelated historical debt.  An all-dimensional \(\Phi\le2\) theorem must
prove that every reachable historical row enters the simultaneous reset
Hall graph of Theorem 4.1.

## 6. Audit and scope

Run

    python3 scratch/audit_h2_two_stutter_endpoint_wrap_window_reset_20260801.py

The replay checks the ordered palette, all \(d^2\) cross cells and every
palette closure for \(2\le d\le64\); the \(d=2\) coalescence; all active
\((A,B,K)\) triples on a three-bit aperture for the sharp flag containment;
explicit middle-prefix dependence of the dropped bank; and the two-block
identical-collar private family, including widthwise OR-multiset equality
and every contraction subset, for \(2\le d\le8,\ 1\le t\le6\).

It reports

    PASS_H2_TWO_STUTTER_ENDPOINT_WRAP_WINDOW_RESET_GATE
    payload_sha256=c0bef3b777ab0f18924b5a9816d55e24999929f886526642ae94ee1904fe520e

No simple owner carrier, q1 palette, exact Pascal inverse, fixed-width
compiler, common-cap assignment, or all-\(k\) recurrence is proved.
