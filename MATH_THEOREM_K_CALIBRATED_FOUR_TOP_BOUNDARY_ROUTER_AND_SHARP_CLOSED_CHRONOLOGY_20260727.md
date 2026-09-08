# A calibrated four-top route exposes the unit boundary swap, while sharp chronology forbids closed companion restoration

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 \kappa=4H-1,\qquad d=M-\kappa=m-3H+1,
\tag{0.1}
\]

and assume (H\ge3), (H=o(m)), and the calibrated common-core
regime.  A length-(d) tight (H)-window path has an injective word of
length

\[
 \ell=d+H-1=M-3H=m-2H.
\tag{0.2}
\]

This report gives both a positive macro and its exact restoration
boundary.

### Positive result

There is an explicit block-hole restriction of the squarefree four-top
moving-hole cube with the following properties.

1. Every root carries one literal length-(d) tight path on each shore.
2. Both shores are squarefree and have the identical set of (4d)
   middle owners.
3. At one chosen cube corner, the same literal owner occurs at an
   arbitrary prescribed bulk phase (j) on the source (beta)-path and
   at phase (2) on the destination (alpha)-path.
4. Swapping the first two letters of that (alpha)-path then has exact
   middle derivative

   \[
                       e_Y-e_X.                              \tag{0.3}
   \]

Thus

\[
 \boxed{
 \text{four-root middle-neutral route}
 \quad\longrightarrow\quad
 \text{one-root unit Robin--Hood swap}}
\tag{0.4}
\]

is a literal macro.  It leaves the other three cube roots on the
switched shore.  Its untagged protected all-depth action is (O(H^2)).
Even under an arbitrary legal phase thinning, the trivial calibrated
bound is (O(MH)=O(H^3)), so the requested polynomial support bound
still holds.

Given an existing source word

\[
 w=(w_1,\ldots,w_\ell),\qquad
 X=U\setminus\{w_j,\ldots,w_{j+H-1}\},                       \tag{0.5}
\]

every phase

\[
                         H+2\le j\le d-H                    \tag{0.6}
\]

embeds directly in the router.  Phase (H+1) embeds after reversing the
source word.  The first and last (H) phases already admit a direct
one-window replacement.  Hence there is no abstract chronology
obstruction to an **open** catalytic route for any phase.

The resulting unit neighbor for (0.5) is the canonical predecessor
neighbor

\[
             Y=X\setminus\{w_{j-1}\}\cup\{w_j\};             \tag{0.7}
\]

word reversal supplies the corresponding successor-side neighbor.  If
(L_X\ge2) and (L_Y=0), the macro removes one duplicate and fills one
hole, and decreases collision energy strictly.

### Negative result

Exact companion restoration is impossible for a genuinely interior
source.  The sharp chronology theorem is:

> If two injective length-(d) tight paths have window decks differing
> in exactly one (H)-window, the removed window lies in the first
> (H) or the last (H) phases.

Consequently a neutral-route / one-unit-swap / neutral-unroute sequence
whose companions have zero final aggregate middle derivative cannot
remove a prescribed occurrence from any phase

\[
                         H+1\le j\le d-H.                    \tag{0.8}
\]

This sharpens the looser endpoint band in
`MATH_THEOREM_BOUNDARY_SWAP_CLOSED_CATALYST_CHRONOLOGY_OBSTRUCTION_20260727.md`.
The open four-top macro evades the theorem exactly by retaining nonzero
companion chronology.

### Exact remaining gates

The local macro is unconditional in the unrestricted/adaptive-core
tight-path catalogue.  Applying it inside a pre-existing global state
still requires:

1. the other three checkerboard companion paths to be present;
2. compatibility of four frozen (2H)-cores with one common
   ((3H-1))-coordinate safe reservoir;
3. a hole among the predecessor/successor neighbors in (0.7); and
4. a phase/tag provenance theorem if the state carries preassigned
   MSW/PBBS nested chronology.

No completion or charged-copy theorem for those conditions is proved
here, and no coefficient-one conclusion is claimed.

## 1. The block-hole four-top paths

Use the positional patterns of the audited four-top moving-hole cube.
Partition a common ((M-2))-set as

\[
 C=R\mathbin{\dot\cup}S,
 \qquad r=|R|,\quad s=|S|,\quad r+s=M-2,                     \tag{1.1}
\]

where

\[
                         r\ge2H+2,\qquad s\ge4H-3.           \tag{1.2}
\]

Write

\[
 R=(z,y_0,y_1,\ldots,y_{r-2}),
 \qquad S=(t_0,t_1,\ldots,t_{s-1}),                          \tag{1.3}
\]

and define cyclic words on (C\cup\{A,B\}) by

\[
\begin{aligned}
 \alpha&=(A,z,y_0,\ldots,y_{r-2},B,t_0,\ldots,t_{s-1}),\\
 \beta&=(A,y_0,\ldots,y_{r-2},z,B,t_{s-1},\ldots,t_0).
\end{aligned}                                                \tag{1.4}
\]

Thus (beta) moves (z) to the other end of (R) and reverses
(S).

Delete from (alpha) the following cyclically consecutive block of
phase starts:

\[
 D_\alpha=
 (t_{s-4H+3},t_{s-4H+4},\ldots,t_{s-1},A,z).                 \tag{1.5}
\]

It has ((4H-3)+2=\kappa) starts.  Delete from (beta) the
cyclically consecutive block

\[
 D_\beta=
 (y_{r-H},y_{r-H+1},\ldots,y_{r-2},z,B,
   t_{s-1},t_{s-2},\ldots,t_{s-3H+2}).                       \tag{1.6}
\]

It has

\[
                         (H-1)+2+(3H-2)=\kappa               \tag{1.7}
\]

starts.  The complements of (1.5)--(1.6) are (d=M-\kappa)
consecutive starts.  They therefore define literal length-(d) tight
paths, denoted (alpha^\circ,beta^\circ).

## 2. Exact middle equality and squarefreeness

For the middle length (H), put

\[
\begin{aligned}
 I_i&=\{y_i,y_{i+1},\ldots,y_{i+H-1}\},
       &&0\le i\le r-H-1,\\
 S_i&=\{t_i,t_{i+1},\ldots,t_{i+H-1}\},
       &&0\le i\le s-H,\\
 E_L&=\{z,y_0,\ldots,y_{H-2}\},\\
 E_R&=\{y_{r-H},\ldots,y_{r-2},z\}.
\end{aligned}                                                \tag{2.1}
\]

The complete core-only window families are

\[
\begin{aligned}
 \mathcal Q_H^{\rm core}(\alpha)
   &=\{E_L\}\cup\{I_i:0\le i\le r-H-1\}
       \cup\{S_i:0\le i\le s-H\},\\
 \mathcal Q_H^{\rm core}(\beta)
   &=\{E_R\}\cup\{I_i:0\le i\le r-H-1\}
       \cup\{S_i:0\le i\le s-H\}.
\end{aligned}                                                \tag{2.2}
\]

Reversal of (S) changes its phase order but not its unordered window
family.

### Lemma 2.1 (exact block census)

The core-only (H)-windows deleted in (1.5) are exactly

\[
 \{E_L\}\cup
 \{S_i:s-4H+3\le i\le s-H\},                                \tag{2.3}
\]

and those deleted in (1.6) are exactly

\[
 \{E_R\}\cup
 \{S_i:s-4H+3\le i\le s-H\}.                                \tag{2.4}
\]

#### Proof

In (alpha), the starts (t_i) with
(s-4H+3\le i\le s-H) give the displayed internal (S)-windows.
The last (H-1) (S)-starts and the start (A) meet placeholder
(A); the last start (z) gives (E_L).  No other deleted start is
core-only.

In (beta), the first start (y_{r-H}) gives (E_R).  Every later
start before or through (B) meets placeholder (B).  Reading the
deleted (t)-starts in the reversed (S)-order gives, in reverse, the
same unordered family

\[
                  S_{s-H},S_{s-H-1},\ldots,S_{s-4H+3}.
\]

This proves (2.3)--(2.4).  (square)

It follows from (2.2)--(2.4) that

\[
 \boxed{
 \mathcal Q_H^{\rm core}(\alpha^\circ)
 =\mathcal Q_H^{\rm core}(\beta^\circ).}                     \tag{2.5}
\]

Choose distinct (a_0,a_1,b_0,b_1\notin C), put

\[
 U_{ij}=C\cup\{a_i,b_j\},\qquad i,j\in\{0,1\},              \tag{2.6}
\]

and specialize (A\mapsto a_i,B\mapsto b_j).  Define the two
checkerboard shores

\[
\begin{aligned}
 \mathcal O&=\{\alpha_{00}^\circ,\beta_{01}^\circ,
                 \beta_{10}^\circ,\alpha_{11}^\circ\},\\
 \mathcal N&=\{\beta_{00}^\circ,\alpha_{01}^\circ,
                 \alpha_{10}^\circ,\beta_{11}^\circ\}.
\end{aligned}                                                \tag{2.7}
\]

### Theorem 2.2 (calibrated neutral router)

Both shores in (2.7) are squarefree at the middle and have the same
literal support of (4d) owners.

#### Proof

For a core-only omitted window (Q), the alternating specialization on
the four roots is the four-cell rectangle

\[
 \Gamma_{C\setminus Q}
 =\sum_{i,j\in\{0,1\}}(-1)^{i+j}
   e_{(C\setminus Q)\cup\{a_i,b_j\}}.                        \tag{2.8}
\]

An omitted window meeting (A) is independent of (i) after taking
its complementary target, and its alternating sum over (i) vanishes;
the same applies to (B) and (j).  Equation (2.5) therefore makes
the complete middle derivative (mathcal O-\mathcal N) zero.

The block (D_\alpha) contains the exceptional phase (E_L), and
(D_\beta) contains (E_R).  Hence every path in (2.7) is obtained by
deleting additional phases from the corresponding audited one-hole
four-top shore.  That shore is squarefree, and deletion cannot create a
collision.  Each present shore has (4d) distinct owners.  Its zero
middle derivative makes the two supports identical.  (square)

## 3. Exact common-core reservoir

The preceding construction is not merely an equal-length path identity.
It has a common protected-core reservoir.

Put

\[
 T_*=\{t_{s-3H+2},t_{s-3H+3},\ldots,t_{s-1}\},
 \qquad |T_*|=3H-2.                                         \tag{3.1}
\]

The coordinates outside the injective retained path word are

\[
 P_\alpha=T_*\cup\{A,z\},\qquad
 P_\beta=T_*\cup\{z,B\}.                                   \tag{3.2}
\]

Indeed, for (kappa) consecutive deleted starts, the union of retained
(H)-windows omits the last (kappa-H+1=3H) coordinates of that
deleted block.  Reading (1.5)--(1.6) gives (3.2).  Thus

\[
 Z=P_\alpha\cap P_\beta=T_*\cup\{z\},
 \qquad |Z|=3H-1.                                           \tag{3.3}
\]

Every (2H)-subset of (Z) lies in every middle owner of both paths.
At one specialized root, the old and new path may therefore use the
same prescribed (2H)-core.

For a four-root packet inside a previously frozen core atlas, a
sufficient condition is

\[
                  Q_{ij}\subseteq Z
                  \quad(i,j\in\{0,1\}),                     \tag{3.4}
\]

where (Q_{ij}) is the prescribed core at (U_{ij}).  A generic four
tuple of independently chosen cores need not satisfy (3.4).  This is
the exact fixed-core completion gate; (3.3) must not be inflated into an
unconditional global embedding theorem.

## 4. Routing an arbitrary bulk occurrence

At corner (U_{00}), shore (mathcal N) uses
(beta_{00}^\circ) and shore (mathcal O) uses
(alpha_{00}^\circ).

The block (1.5) ends at the start (z).  Therefore the retained
(alpha)-starts begin

\[
 y_0,y_1,y_2,\ldots,                                        \tag{4.1}
\]

and

\[
                         I_1=\{y_1,\ldots,y_H\}              \tag{4.2}
\]

is its phase-(2) middle window.

The retained (beta)-starts begin

\[
 t_{s-3H+1},t_{s-3H},\ldots,t_0,A,y_0,y_1,\ldots.            \tag{4.3}
\]

Hence the same literal window (I_1) has (beta)-phase

\[
                         j=s-3H+5.                            \tag{4.4}
\]

This is already a nonlocal chronology route at the same provider root.

### Theorem 4.1 (arbitrary-source embedding)

Let (U) carry an existing injective path word

\[
 w=(w_1,\ldots,w_\ell)
\tag{4.5}
\]

and let the chosen occurrence (X) be as in (0.5), with

\[
                         H+2\le j\le d-H.                    \tag{4.6}
\]

Then the packet can be labelled so that

1. (U_{00}=U);
2. (beta_{00}^\circ) is exactly the prescribed word (w);
3. the chosen omitted window is (I_1); and
4. after the neutral switch (mathcal N\to\mathcal O), that same
   owner (X), at the same provider root, occurs at phase (2).

If the old path has a prescribed (2H)-core, the labels can be chosen
so that this core is retained by both focal paths.

#### Proof

Set

\[
 s=j+3H-5,
 \qquad r=M-2-s=M-3H-j+3.                                  \tag{4.7}
\]

The bounds in (4.6) give (s\ge4H-3) and (r\ge2H+2).
Identify, in order,

\[
 (t_{s-3H+1},t_{s-3H},\ldots,t_0,A,
   y_0,y_1,\ldots,y_{r-2})
 =(w_1,w_2,\ldots,w_\ell).                                  \tag{4.8}
\]

The (t)-block in (4.8) has (s-3H+2=j-3) entries.  Therefore

\[
 A=w_{j-2},\qquad y_0=w_{j-1},\qquad y_1=w_j,                \tag{4.9}
\]

and (4.2) is exactly the omitted window in (0.5).  Equations
(4.1)--(4.4) prove the phase route.

The (3H) labels of (U) outside (w) form (P_\beta).  If a
prescribed (2H)-core (Q_U) is present, choose (B) among the at
least (H) labels of (P_\beta\setminus Q_U), and assign the other
(3H-1) labels to (Z=T_*\cup\{z\}).  Then

\[
                         Q_U\subseteq Z=P_\alpha\cap P_\beta. \tag{4.10}
\]

Set (a_0=A,b_0=B), take (C=U\setminus\{A,B\}), and choose fresh
(a_1,b_1\notin C).  This completes the four tops and proves every
assertion.  (square)

For the single omitted phase (j=H+1), reverse the source word.  Its
phase becomes (d-H), which lies in (4.6) for (d\ge2H+2).  The same
reflection handles the opposite orientation.  Thus Theorem 4.1 reaches
every phase outside the two direct boundary collars.

## 5. The nonneutral boundary step

Starting from (mathcal O), interchange (y_0,y_1) only in the
(alpha_{00}^\circ)-word.  The first middle window contains both
letters and is unchanged.  The second changes from

\[
 Q=\{y_1,y_2,\ldots,y_H\}
 \quad\hbox{to}\quad
 Q'=\{y_0,y_2,\ldots,y_H\},                                 \tag{5.1}
\]

and every later middle window contains neither (y_0) nor the old
position of (y_1), so it is unchanged.  Complementation inside
(U_{00}) gives

\[
 X=U_{00}\setminus Q,
 \qquad
 Y=U_{00}\setminus Q'
   =X\setminus\{y_0\}\cup\{y_1\}.                           \tag{5.2}
\]

### Theorem 5.1 (exact open Robin--Hood macro)

Let (mathcal O^*) be obtained from (mathcal O) by the preceding
one-root boundary swap.  Then

\[
 \boxed{
 1_{\operatorname{mid}(\mathcal O^*)}
 -1_{\operatorname{mid}(\mathcal N)}=e_Y-e_X.}               \tag{5.3}
\]

Every root still carries one literal length-(d) path.  If the ambient
load has (L_X\ge2,L_Y=0), then the macro fills one hole, removes one
duplicate occurrence, and

\[
 \Psi(L+e_Y-e_X)-\Psi(L)=L_Y-L_X+1\le-1.                    \tag{5.4}
\]

#### Proof

Theorem 2.2 makes (mathcal N\to\mathcal O) exactly middle-neutral.
Equation (5.2) shows that (mathcal O\to\mathcal O^*) has derivative
(e_Y-e_X).  Addition proves (5.3), and the exact quadratic expansion
gives (5.4).  (square)

For the embedded word (4.8), formula (5.2) is precisely

\[
                         Y=X-w_{j-1}+w_j,                    \tag{5.5}
\]

which is (0.7).

## 6. Polynomial all-depth collateral

First ignore extra stopping tags and compare the complete retained path
decks at a fixed deletion length (h\le2H).

The full core-only (h)-window families of (alpha,beta) differ by
at most the two (z)-end exceptions: reversal of (S) preserves its
unordered interval family.  Removing the two phase blocks can add at
most (2\kappa) interval occurrences to their multiset difference.
The alternating specialization of one core interval is a four-cell
rectangle of (ell^1)-norm four, while every placeholder interval
cancels in one cube coordinate.  Therefore

\[
 \|\Delta_h^{\rm route}\|_1
 \le4(2+2\kappa)=8\kappa+8=32H.                              \tag{6.1}
\]

The adjacent boundary swap changes at most two interval occurrences at
one fixed length, and hence

\[
                         \|\Delta_h^{\rm swap}\|_1\le4.     \tag{6.2}
\]

Across the at most (2H+1) protected deletion lengths,

\[
 \sum_h\|\Delta_h^{\rm macro}\|_1
 \le(2H+1)(32H+4)=O(H^2).                                  \tag{6.3}
\]

This is an untagged or route-symmetrically tagged statement.  An
arbitrary phase thinning can destroy the reversed-(S) cancellations.
The safe trivial bound at one row is the total mass of four old plus
four new paths,

\[
                         \|\Delta_h^{\rm route}\|_1\le8d.   \tag{6.4}
\]

Thus its protected all-row collateral is (O(dH)=O(MH)).  Under the
calibration (H^2/m=\log m+o(1)), one has (M=O(H^2)), so this is
(O(H^3)).  This proves polynomial support conditional on the endpoint
tagged paths being legal.  It does not prove compatibility with an
arbitrary preassigned MSW/PBBS tag history.

## 7. Sharp one-window chronology

We now prove the exact obstruction to closing the companions.

For an injective word (w=(w_1,\ldots,w_{d+H-1})), put

\[
 J_i(w)=\{w_i,w_{i+1},\ldots,w_{i+H-1}\},
 \qquad1\le i\le d.                                        \tag{7.1}
\]

### Theorem 7.1 (sharp endpoint-collar theorem)

Assume (H\ge3) and (d\ge2H+1).  Let (w,v) be injective words of
length (d+H-1) satisfying

\[
 |\mathcal J(w)\triangle\mathcal J(v)|=2,
 \qquad
 \mathcal J(w)=\{J_1(w),\ldots,J_d(w)\}.                    \tag{7.2}
\]

If (J_i(w)) is the unique old-only window, then

\[
                         \boxed{i\le H\quad\text{or}\quad i\ge d-H+1.}
\tag{7.3}
\]

Both bands are sharp.

#### Proof

Join two windows when their intersection has size (H-1).  Injectivity
of the word makes this intrinsic graph the path

\[
                         J_1-J_2-\cdots-J_d.                 \tag{7.4}
\]

Deleting the unique old-only and new-only vertices leaves the same
labelled family of (d-1) windows.  The two component orders determine
the missing position up to reversal.  When both components are
nonempty, their facing endpoints are intrinsic: among all cross-component
pairs they uniquely maximize intersection, with value (H-2).  After
one possible global reversal, all common windows therefore align and the
new-only window (R) occupies position (i).

Assume for contradiction that

\[
                         H+1\le i\le d-H.                    \tag{7.5}
\]

Put

\[
 A=J_{i-1}(w),\qquad B=J_{i+1}(w),\qquad
 S=A\cap B=\{w_{i+1},\ldots,w_{i+H-2}\}.                    \tag{7.6}
\]

The new window (R) must meet each of (A,B) in (H-1) labels.  A
size-(H) set with this property contains (S), one member of
({w_{i-1},w_i\}), and one member of
({w_{i+H-1},w_{i+H}\}).  The old window is

\[
                         J_i=S\cup\{w_i,w_{i+H-1}\}.         \tag{7.7}
\]

Every alternative (R\ne J_i) therefore contains (w_{i-1}) or
(w_{i+H}).

Under (7.5), each of these two extreme letters already occurs in exactly
(H) of the common windows.  It does not occur in the removed (J_i).
Adding it to (R) would give coordinate frequency (H+1) in
(mathcal J(v)).  This is impossible: one position of an injective
word belongs to at most (H) consecutive (H)-windows.  This proves
(7.3).

For (2\le i\le H), swapping word positions (i-1,i) changes exactly
window (J_i).  At (i=1), replace (w_1) by any unused top label;
only (J_1) changes.  Reversing the word gives the last (H) phases.
Thus both bands are attained.  (square)

The exact boundary-eligible fraction of one path is therefore

\[
                         {2H\over d}=O(H/m)=o(1).             \tag{7.8}
\]

## 8. Closed restoration is impossible, and the open cube is necessary

Call a macro **closed outside a focal root (U)** if the aggregate
middle derivative of every nonfocal endpoint configuration is zero.
Literal restoration of every companion is a special case.

### Theorem 8.1 (no closed conjugate of the boundary swap)

Suppose a sequence of arbitrary middle-neutral routes, one unit
boundary swap, and arbitrary middle-neutral unroutes starts and ends in
one-path-per-root tables, has net derivative (e_Y-e_X), and is closed
outside one focal root (U).  If its initial occurrence of (X) at
(U) lies at phase (j), then

\[
                         j\le H\quad\text{or}\quad j\ge d-H+1. \tag{8.1}
\]

In particular no specified occurrence satisfying (0.8) can be routed,
swapped, and closed, regardless of the number or type of neutral
intermediate moves.

#### Proof

The nonfocal endpoint derivative is zero and the full derivative is
(e_Y-e_X).  Therefore the initial and final focal middle decks differ
by exactly that unit vector.  Complementation inside (U) makes their
(H)-window decks differ in exactly one window.  Theorem 7.1 proves
(8.1).  The argument depends only on endpoint chronology, not on the
neutral move library.  (square)

Thus a deep repair must leave a nonzero aggregate companion derivative.
Any nonzero integral zero-total companion derivative has
(ell^1)-norm at least two.

For the particular four-top macro, write (d_{ij}) for the individual
middle-deck derivative at (U_{ij}) under
(mathcal N\to\mathcal O).  Then

\[
                         \sum_{i,j}d_{ij}=0.                 \tag{8.2}
\]

At (U_{00}), (d_{00}\ne0): the (alpha)-block deletes its full
(A)-collar, while the corresponding (beta)-path retains that
collar.  Restoring the other three roots immediately after the boundary
swap would leave net derivative

\[
                         d_{00}+e_Y-e_X,                     \tag{8.3}
\]

not the desired unit.  A further neutral network can close (8.3) only
by violating Theorem 8.1 for a deep source.  Hence the three switched
companions in Theorem 5.1 are genuine chronology carriers, not an
artifact of the proof.

## 9. Final implication boundary

The following are proved.

1. The block deletions (1.5)--(1.6) give literal calibrated tight paths.
2. Their four-top checkerboard exchange is squarefree and exactly
   middle-neutral.
3. Every prescribed bulk source word and occurrence embeds at the focal
   corner while preserving its prescribed (2H)-core.
4. The route moves that occurrence to phase (2) at the same provider.
5. The subsequent one-root swap is the exact unit transfer (5.3).
6. Untagged all-depth collateral is (O(H^2)), and the calibrated
   trivial tagged bound is (O(H^3)).
7. Exact or aggregate-zero companion restoration is impossible for a
   deep occurrence; the sharp direct bands contain exactly (2H)
   phases.

The following remain unproved.

1. A generic global factor need not contain the other three source-shore
   companion paths.
2. Four independently frozen cores need not fit the common safe
   reservoir (3.3).
3. A duplicated target need not have a hole at either canonical neighbor
   exposed by the two word orientations.
4. Arbitrary MSW/PBBS terminal tags need not transport through the long
   (S)-reversal with the sharp (O(H^2)) cancellation.
5. No theorem yet packs these open macros at positive density or recycles
   their companion chronology with (o(W)) global cost.

The precise advance is therefore

\[
 \boxed{
 \begin{gathered}
 \text{the local neutral-route/nonneutral-swap macro exists with}\
 O(\operatorname{poly}(H))\text{ support and routes every bulk phase;}\\
 \text{its three companion paths cannot all be restored, and}\
 \text{global companion completion is now the sole local incidence gate.}
 \end{gathered}}
\tag{9.1}
\]

## Source dependencies

The unit boundary swap is from
`MATH_THEOREM_COMMON_CORE_BOUNDARY_SWAP_MARGINAL_ESCAPE_20260727.md`.
The one-hole squarefree cube and its placeholder-cancellation lemma are
from
`MATH_THEOREM_PROMOTION_FOUR_TOP_SQUAREFREE_MOVING_HOLE_CUBE_20260726.md`.
The earlier closed chronology theorem is
`MATH_THEOREM_BOUNDARY_SWAP_CLOSED_CATALYST_CHRONOLOGY_OBSTRUCTION_20260727.md`;
Section 7 supplies its sharp constant correction.
