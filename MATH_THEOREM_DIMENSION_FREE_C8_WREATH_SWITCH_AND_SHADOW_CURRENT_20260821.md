# A dimension-free two-row wreath switch and its exact shadow current

**Date:** 2026-08-21  
**Status:** analytic switch theorem; the global augmenting-path theorem in
Section 7 remains open

## 1. The switch

Put (b=2r+1), (r\ge2).  Let (a,b_0,c,d) be four distinct labels,
let

\[
 P=(p_1,\ldots,p_{r-1}),\qquad
 Q=(q_1,\ldots,q_{r-2})
\]

be disjoint ordered words on the remaining labels, and regard the following
as unoriented cyclic orders:

\[
\begin{array}{ll}
 R_0=a\,b_0\,P\,c\,d\,Q,
 &R_1=c\,a\,P\,d\,b_0\,Q,\\[2mm]
 S_0=a\,c\,P\,b_0\,d\,Q,
 &S_1=b_0\,a\,P\,d\,c\,Q.
\end{array}                                                    \tag{1.1}
\]

For a cyclic order (C), write \({\cal W}_k(C)\) for the multiset of its
(b) cyclic (k)-windows.

### Theorem 1.1 (dimension-free (2\leftrightarrow2) trade)

For every (r\ge2),

\[
 {\cal W}_r(R_0)\uplus {\cal W}_r(R_1)
 =
 {\cal W}_r(S_0)\uplus {\cal W}_r(S_1),                       \tag{1.2}
\]

and every member of this common multiset has multiplicity one.  Hence, in
any exact middle wreath factor containing (R_0,R_1), they may be replaced
by (S_0,S_1) without changing a single middle target.

#### Proof

Index starts by (0,\ldots,2r) in the displayed words.  The following is a
literal bijection between old and new (r)-windows:

\[
\begin{array}{c|c|c}
\text{old row}&\text{start}&\text{new row/start}\\ \hline
R_0&0&S_1/0\\
R_0&1&S_0/2\\
R_0&2&S_0/1\\
R_0&3\le i\le r+1&S_1/i\\
R_0&r+2&S_0/(r+2)\\
R_0&r+3\le i\le2r&S_1/i.
\end{array}                                                    \tag{1.3}
\]

The table for (R_1) is obtained by interchanging (S_0,S_1).  Each line
is checked by observing that the relevant window contains either both
members of an exchanged adjacent pair or the same long block together with
the same boundary label.  The starts in (1.3) are disjoint and exhaustive.
The same table backwards proves that no target is repeated.  This proves
(1.2).  \(\square\)

## 2. It is one factor-alternating (C_8)

The (r)-windows in one wreath induce their unique (b)-cycle in
(KG(b,r)).  Use the old occurrence ((j,i)) to denote the window of
(R_j) at start (i), identifying new windows through (1.3).

### Proposition 2.1 (exact odd-edge footprint)

The old and new two-cycle factors have (4r-2) common odd-graph edges.
The four deleted edges are

\[
\begin{split}
 &(0,1)(0,r+1),\quad (0,2)(0,r+3),\\
 &(1,1)(1,r+1),\quad (1,2)(1,r+3),
\end{split}                                                    \tag{2.1}
\]

and the four inserted edges are

\[
\begin{split}
 &(0,1)(1,r+3),\quad (0,2)(1,r+1),\\
 &(0,r+1)(1,1),\quad (0,r+3)(1,2).
\end{split}                                                    \tag{2.2}
\]

Their symmetric difference is one alternating (C_8).  In particular,
the switch is a genuine local odd-graph two-factor toggle, and both sides
are again two (C_b)'s rather than arbitrary even-factor components.

#### Proof

Two (r)-windows of one cyclic word are disjoint exactly when their starts
differ by (r) or (r+1) modulo (2r+1).  Substitute the window bijection
(1.3).  Every edge cancels except (2.1)--(2.2), which occur in alternating
order on the displayed eight vertices.  \(\square\)

## 3. Exact currents at every lower depth

Assume first that (r\ge3).  Put (U=P-p_{r-1}) and (V=P-p_1), with order forgotten.  At first shadow
the switch has the exact signed current

\[
 -[\{b_0\}\cup U]-[\{c\}\cup V]
 +[\{c\}\cup U]+[\{b_0\}\cup V].                            \tag{3.1}
\]

Thus it is a Boolean (2\times2) square current on the four
((r-1))-sets obtained from the common ((r-3))-core
(P-\{p_1,p_{r-1}\}).

More generally, put (k=r-q).  For (2\le q\le r-2), the four negative
depth-(q) targets are

\[
\begin{array}{ll}
 \{b_0\}\cup\operatorname{pre}_{k-1}P,&
 \{c\}\cup\operatorname{suf}_{k-1}P,\\
 \{b_0\}\cup\operatorname{pre}_{k-1}Q,&
 \{c\}\cup\operatorname{suf}_{k-1}Q,
\end{array}                                                    \tag{3.2}
\]

and the four positive targets are obtained by exchanging (b_0,c).
At (q=r-1) these four formal terms cancel in pairs.

### Corollary 3.1 (sharp all-depth footprint)

For (r\ge3), one switch has the following old/new target-multiset
differences:

\[
\begin{array}{c|c}
q&\text{number of negative and positive occurrence units}\\ \hline
1&2\text{ and }2,\\
2\le q\le r-2&4\text{ and }4,\\
r-1&0\text{ and }0.
\end{array}                                                    \tag{3.3}
\]

Consequently the aggregate one-sided footprint through depth (H\le r-2)
is exactly (4H-2), independent of (r).

For the boundary case (r=2), the only lower deck is the singleton deck;
it is unchanged, so the footprint is zero.

#### Proof

Enumerate cyclic (k)-windows in (1.1).  Windows internal to (P) or
(Q), and windows containing both members of an exchanged adjacent pair,
cancel.  The only uncancelled boundary windows are precisely (3.2).  When
(k=r-1), the two (Q)-terms coincide crosswise and cancel, leaving
(3.1).  When (k=1), all four terms cancel.  Distinctness for
(2\le k\le r-2) follows from the disjoint labels and ordered block
lengths.  \(\square\)

The occurrence-resolved same-start ribbon is also local, but not perfectly
preserved: optimizing the two orientations on each side changes exactly
seven middle-window/lower-prefix attachments for every (r\ge3).  Thus one
dirty window per row can absorb at most two of those seven changes; the
literal punctured-ribbon trade still has five clean attachment changes.

## 4. Convex first-shadow energy

For an exact factor (F), let (mu_F(T)) be the multiplicity of the
rank-((r-1)) target (T), let

\[
 A=\binom{2r+1}{r},\qquad N=\binom{2r+1}{r-1},\qquad
 \Phi(F)=\sum_T\binom{\mu_F(T)}2.                              \tag{4.1}
\]

If (h_1(F)=|\{T:\mu_F(T)=0\}|), then the exact identity

\[
 \boxed{\quad
 \Phi(F)-(A-N)
 =h_1(F)+\sum_{T:\mu_F(T)\ge3}\binom{\mu_F(T)-1}{2}.
 \quad}                                                        \tag{4.2}
\]

holds.  Hence driving the energy gap to (o(A)) is sufficient for
(h_1=o(A)).

For the square (3.1), write the donor loads as (x,y) and the recipient
loads as (z,w).  Its exact energy change is

\[
 \Delta\Phi=z+w-x-y+2.                                       \tag{4.3}
\]

This is the natural augmenting-path potential: a switch is strictly
improving exactly when the two donor loads exceed the two recipient loads
by at least three in total.

For a factor (F), let ({\cal S}(F)) be its currently legal oriented C8
moves.  For a lower target (T), let (d_T^-) and (d_T^+) be its donor
and recipient incidences in these moves, and put

\[
             \eta_T=d_T^- -d_T^+.
\]

Summing (4.3) gives the exact drift identity

\[
 \boxed{\quad
 \sum_{s\in{\cal S}(F)}\Delta_s\Phi
 =2|{\cal S}(F)|-\sum_T\mu_F(T)\eta_T.
 \quad}                                                        \tag{4.4}
\]

Consequently the desired local-minimum theorem would follow from the single
correlation estimate

\[
 \sum_T\mu_F(T)\eta_T
 \ge 2|{\cal S}(F)|
      +c\bigl(\Phi(F)-(A-N)\bigr)-C A/r                       \tag{4.5}
\]

with absolute (c>0,C): at a C8-local minimum the left side of (4.4) is
nonnegative, and (4.5) forces the energy gap to be (O(A/r)).  Equation
(4.4) is unconditional; (4.5), or an augmenting-path substitute using
neutral moves, is the precise missing expansion estimate.

## 5. Every canonical marked gap is such a switch

The canonical MSW factor has the marked pairs obtained by inserting
(1100) and (1010) in one of the (2r-3) gaps of a Dyck root of
semilength (r-2).  There are

\[
 K_r=(2r-3)\operatorname{Cat}_{r-2}                            \tag{5.1}
\]

pointed pairs.

### Theorem 5.1 (marked-gap realization)

Every one of these pairs of canonical rows has a unique representation,
up to the dihedral symmetries and exchanging the two rows, as (R_0,R_1)
in (1.1).  Its alternate pair is (S_0,S_1).  Distinct pointed marked gaps
give distinct unordered row pairs.

#### Proof

The marked-gap block lemma gives the two omitted-label words with one common
outside word and local permutations

\[
 \rho(1100)=(4,2,3,1),\qquad
 \rho(1010)=(2,1,4,3).                                      \tag{5.2}
\]

Apply the inverse-two position map converting an omitted-label word to its
wreath order.  Rotating to the local block and, when necessary, reversing
the common outside word yields exactly (1.1): the two alternating outside
subwords have lengths (r-1) and (r-2), and the four block labels become
(a,b_0,c,d).  Reversing this dictionary recovers the inserted gap and
the outside root, proving uniqueness.  \(\square\)

The marked-gap graph has maximum degree at most (r-1).  Therefore a greedy
matching contains at least

\[
 \frac{K_r}{2r-3}=\operatorname{Cat}_{r-2}                    \tag{5.3}
\]

edges.  Applying their C8 switches gives an unconditional bank of that many
pairwise row-disjoint exact factor switches.  Because one switch changes
only two first-shadow occurrence units, however, one disjoint round can
alter only (O(\operatorname{Cat}_r)=O(A/r)) holes.  Reuse through
augmenting sequences is essential.

## 6. Exact (b=9) component calculation

Starting from the canonical fourteen-row factor, exhaustively applying only
the switches (1.1) produces a connected component of exactly (3014)
factors.  Its minimum first-shadow defect is one, attained first at switch
distance four; no zero-hole factor lies in this component.  A shortest
energy-monotone path has

\[
 (h_1,\Phi)=(4,47),(2,45),(2,45),(2,44),(1,43),               \tag{6.1}
\]

and reuses only one intermediate row once.  The separate optimal five-row
trade reaching zero holes is not a composition of these C8 moves.

This finite fact is not an asymptotic obstruction: one hole is already
(o(A)).  It does show that the C8 squares are not an exact Markov basis for
all wreath factors.

## 7. Remaining quantitative theorem

The exact open gate is now narrow.  One needs to prove that, in the C8
switch component of the canonical factor, there is a factor (F) with

\[
 \Phi(F)-(A-N)=O(A/r)\quad\text{or merely }o(A).               \tag{7.1}
\]

Equivalently, one needs an availability/augmenting-path theorem for the
physically present squares (3.1), not for all abstract Boolean squares.
The desired proof must also bundle switch paths so that the four-term
currents (3.2) telescope at every (q\le H).  The local theorem above
supplies the sharp cost (4H-2); it does not prove the required global
paths exist.

Finite greedy/tabu diagnostics reduce the canonical defects

\[
 r=4:4\to1,\qquad r=5:32\to19,\qquad r=6:176\to133,
\qquad r=7:837\to693,                                        \tag{7.2}
\]

using C8 moves only.  These are evidence for an (O(A/r)) local-minimum
scale, not a proof.

## 8. Checker

The finite audit scripts are

```text
scratch/research_two_row_wreath_switch_20260821.py
scratch/audit_msw_marked_gap_c8_switch_20260821.py
scratch/search_b9_c8_switch_path_20260821.py
scratch/research_msw_c8_shadow_anneal_20260821.py
```

All finite computation was run on `h100`.  The analytic statements in
Sections 1--5 do not depend on those runs.
