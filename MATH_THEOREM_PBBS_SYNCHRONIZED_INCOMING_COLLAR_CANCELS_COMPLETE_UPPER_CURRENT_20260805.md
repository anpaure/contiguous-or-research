# Synchronized incoming collars cancel the complete PBBS pentagon upper current

**Date:** 2026-08-05  
**Method:** exact set-union algebra and a tagged Johnson-path construction;
no computation or search  
**Status:** unconditional local owner-path theorem for every high PBBS
height pentagon.  It reduces arbitrary-width upper transparency to the
prospective planting of a polynomial-size protected collar bank.  It does
not claim that this bank has already been planted simultaneously with the
PBBS connector, residence antecedent, or typed common cap.

## 0. Outcome

For a height pentagon write its old and new owner edges as

\[
 P_iQ_i\quad\longleftrightarrow\quad P_iQ_{i+1}
 \qquad(i\in\mathbb Z_5).
\tag{0.1}
\]

At height at least four the common-deletion theorem gives

\[
 \boxed{P_{i-1}\cup Q_i=P_i\cup Q_i}
 \qquad(i\in\mathbb Z_5).
\tag{0.2}
\]

The right-ray theorem is the special case of (0.2) in which an old
crossing interval uses only the endpoint owner on its incoming side.  The
main observation here is that (0.2) actually cancels the **complete**
two-sided current if the five incoming arcs have the same cumulative union
profile outside their endpoint owners.

More precisely, there are five pairwise owner-disjoint Johnson collars
ending at the five owners `P_i` and a common nested sequence

\[
 \varnothing=C_0\subseteq C_1\subseteq\cdots\subseteq C_L,
 \qquad C_L\cup P_i=[n],
\tag{0.3}
\]

such that the union of the last `u` owners of collar `i` is

\[
                         A_i(u)=P_i\cup C_{u-1}.
\tag{0.4}
\]

Consequently every old one-cut value has an equal new occurrence:

\[
 \boxed{
 A_i(u)\cup B_i(v)=A_{i-1}(u)\cup B_i(v).}
\tag{0.5}
\]

If every intercut arc contains one such full-union collar, every interval
crossing two or more cuts already has value `[n]`.  Thus the complete
arbitrary-width upper current is zero, not merely bounded.

The collar has `O(r)` owners per incoming arc.  For a height ladder with
`H=O(d)` pentagons the aggregate protected support is `O(Hr)`.  This is
consistent with, and sharp up to constants against, the linear shield
aperture obstruction.  It costs internal owner support, not extra word
positions.

## 1. Abstract common-excess cancellation

Cut a directed owner factor at `q` edges.  At cut role `i`, let

* `P_i` be the final owner of the incoming arc;
* `Q_i` be the first owner of the outgoing arc;
* `A_i(u)` be the union of the last `u>=1` incoming owners;
* `B_i(v)` be the union of the first `v>=1` outgoing owners.

Suppose a head permutation `sigma` replaces

\[
                         P_iQ_i\longmapsto P_iQ_{\sigma(i)}.
\tag{1.1}
\]

### Theorem 1.1 (common-excess current cancellation)

Assume that for every role `j`

\[
                         P_{\sigma^{-1}(j)}\cup Q_j
                         =P_j\cup Q_j,                    
\tag{1.2}
\]

and that there are sets `C_u`, independent of the role, for which

\[
                         A_i(u)=P_i\cup C_u.              
\tag{1.3}
\]

Then every old one-cut exterior interval has a target-equal new interval
of the same two penetration depths:

\[
 \boxed{
 A_j(u)\cup B_j(v)
 =A_{\sigma^{-1}(j)}(u)\cup B_j(v).}
\tag{1.4}
\]

The correspondence is a bijection on occurrence addresses.

#### Proof

Because `Q_j subseteq B_j(v)`, equations (1.2)--(1.3) give

\[
\begin{aligned}
 A_j(u)\cup B_j(v)
 &=C_u\cup P_j\cup Q_j\cup B_j(v)\\
 &=C_u\cup P_{\sigma^{-1}(j)}\cup Q_j\cup B_j(v)\\
 &=A_{\sigma^{-1}(j)}(u)\cup B_j(v).
\end{aligned}
\]

The inverse correspondence uses `sigma`, so the address map is bijective.
\(\square\)

For a high PBBS pentagon, `sigma(i)=i+1`, and (1.2) is precisely the
common-deletion identity (0.2).

## 2. Intervals crossing several cuts

### Lemma 2.1 (full-collar domination)

Suppose every incoming arc contains, immediately before its cut, a block
whose owner union is `[n]`.  Every interval crossing at least two cuts has
union `[n]`, both before and after an arbitrary head permutation.

#### Proof

Between two successive crossed cuts the interval contains the complete
terminal block of the intervening incoming arc.  That block has union
`[n]`.  A head permutation moves whole arcs and does not alter the block.
\(\square\)

### Corollary 2.2 (complete upper transparency)

Under Theorem 1.1 and Lemma 2.1, the head permutation preserves every
contiguous owner-union value of arbitrary width.  Intervals internal to an
arc are literal copies, one-cut intervals use (1.4), and multi-cut
intervals use Lemma 2.1.

## 3. The high-pentagon screen geometry

Use

\[
 n=2r+1,\qquad R=r+1.
\tag{3.1}
\]

For one high pentagon the three-screen theorem writes

\[
                         P_i=G+X_i,
 \qquad |G|=R-3,quad |X_i|=3.                           
\tag{3.2}
\]

The literal PBBS formula is slightly stronger: all five `X_i` contain the
same distinguished deletion coordinate `p`, and the other two elements
form the five edges of a five-cycle on the active survivor bank.  In
particular

\[
                         \left|\bigcup_iX_i\right|=6.     
\tag{3.3}
\]

Put

\[
                         E=[n]\setminus G,
 \qquad |E|=R+2=r+3.                                    
\tag{3.4}
\]

Then `X_i subseteq E`, and

\[
                         |E\setminus\bigcup_iX_i|=r-3.   
\tag{3.5}
\]

## 4. Tagged synchronized Johnson collars

The following lemma is stated for five endpoints because that is the
pentagon application.  The same proof works for every fixed number of
endpoints.

### Lemma 4.1 (tagged common-union collars)

Assume `r>=18`, and fix an integer

\[
                         5\le \delta\le r-6.             \tag{4.0}
\]

Let `G` and `X_0,...,X_4` satisfy (3.2)--(3.5).  There are five
pairwise vertex-disjoint, lower-colour-disjoint simple Johnson paths

\[
 P_i=S_i(0),S_i(1),\ldots,S_i(L)                         
\tag{4.1}
\]

and one common nested sequence

\[
 \varnothing=C_0\subseteq C_1\subseteq\cdots\subseteq C_L=E
\tag{4.2}
\]

such that

\[
 \boxed{
 \bigcup_{t=0}^{u}S_i(t)=P_i\cup C_u}
 \qquad(0\le u\le L).                                  
\tag{4.3}
\]

Every `S_i(t)` has rank `R`, consecutive owners differ by one exchange,
and every coordinate first inserted from `E` remains present for
`delta+1` consecutive owner states, except for the inevitable clipping at
the right endpoint.  One may take `L=|E|=r+3`.

#### Proof

Choose distinct tags

\[
                         g_0,\ldots,g_4\in G.             
\tag{4.4}
\]

For each `i`, choose a set

\[
 D_i\subseteq G,\qquad |D_i|=\delta-2,                  \tag{4.5}
\]

which contains `g_i` and contains none of the other four tags.  Put

 \[
                         K_i=G\setminus D_i,
 \qquad |K_i|=r-\delta.                                 \tag{4.6}
 \]

Order `D_i` with `g_i` first, and then append any ordering of the three
members of `X_i`.  This gives an initial word of length `delta+1`.

Next order the elements of `E` as

\[
 c_1,c_2,\ldots,c_L,\qquad L=r+3,                       \tag{4.7}
\]

putting the `r-3` elements outside `union_i X_i` first and the six
elements of `union_i X_i` last.  Let

\[
                         C_u=\{c_1,\ldots,c_u\}.          \tag{4.8}
\]

For role `i`, concatenate its initial word with (4.7), and denote the
result by

\[
                         w_{i,1},\ldots,w_{i,L+\delta+1}.
\]

Define

\[
 S_i(t)=K_i\cup
   \{w_{i,t+1},w_{i,t+2},\ldots,w_{i,t+\delta+1}\}
                    \qquad(0\le t\le L).              \tag{4.9}
\]

The three repeated labels are the members of `X_i`.  Their initial and
final occurrences are separated by at least `r-2>delta+3`; every other
label occurs once.  Hence every window in (4.9) has `delta+1` distinct
members, and consecutive windows exchange their first and next labels.
Also

\[
 S_i(0)=K_i\cup D_i\cup X_i=G\cup X_i=P_i.             \tag{4.10}
\]

For `t>=1`, the first letter `g_i` has left the window and never returns,
whereas every other tag `g_j` belongs to the fixed core `K_i`.  Thus the
positive-time states on different paths have opposite tag signatures.
An endpoint contains all five tags, so it cannot equal a positive-time
state on another path.  The five endpoints themselves are distinct.

The owner windows on one path are distinct.  Indeed, two equal windows
with shift at least `delta+1` would require at least `delta+1>=6` repeated
labels.  With a smaller shift, equality would require either at least four
repeated leaving labels or a repetition at distance at most `delta+3`.
Both are impossible.  The same argument, now for the length-`delta`
intersections

\[
 S_i(t)\cap S_i(t+1)
   =K_i\cup\{w_{i,t+2},\ldots,w_{i,t+\delta+1}\},       \tag{4.11}
\]

shows that the lower colours on one path are distinct.  Tag signatures
make the lower colours belonging to different paths distinct as well.
Therefore the five incidence lifts form a genuine path forest, not merely
five vertex-disjoint paths in the owner graph.

Each `c_u` enters at state `u` and remains through state `u+delta`, when
those states exist.  This proves the residence assertion.  Finally, the
sliding-window definition gives directly

\[
 \bigcup_{t=0}^{u}S_i(t)=P_i\cup\{c_1,\ldots,c_u\}
                         =P_i\cup C_u.                 \tag{4.12}
\]

At the final stage,

\[
                         P_i\cup C_L=G\cup X_i\cup E=[n].
\]

\(\square\)

### Lemma 4.2 (uniform exposure of the explicit collars)

For one path in Lemma 4.1:

1. any fixed rank-`r` lower set is contained in at most `16` owner
   states; and
2. any fixed rank-`R` owner contains at most `5` of the path's lower
   colours.

#### Proof

Every owner has the form `K_i` plus a consecutive `(delta+1)`-window.
A rank-`r` subset of such an owner either contains `K_i` and a
`delta`-subset of the window, or contains all of the window and omits one
member of `K_i`.  Only the three labels in `X_i` occur twice.  A fixed
`delta`-set therefore has at most `2^3` occurrence realizations, and each
realization lies in at most two consecutive `(delta+1)`-windows.  A fixed
`(delta+1)`-set has at most `2^3` realizations.  This proves the bound
`16`.

For the second assertion an owner containing one of (4.11) must contain
`K_i`.  Write its remaining `(delta+1)`-set as `F`.  If two length-`delta`
blocks contained in `F` start `s` positions apart, their set intersection
has size at least `delta-1`.  Positional overlap and the three possible
repeated labels give the upper bound `delta-s+3`; hence `s<=4`.  Two
disjoint blocks cannot both lie in `F` because `delta>=5`.  All qualifying
starts consequently lie in an interval of length four, so there are at
most five. \(\square\)

The sliding construction is therefore simultaneously resident and
small-exposure.  Its first and last `delta` states export the usual two
clipped boundary flag banks.  No claim is made here that the surrounding
PBBS arcs already absorb those flags.

## 5. Application to one pentagon and to a ladder

Reverse each path in Lemma 4.1 and place it immediately before its endpoint
`P_i`.  Equation (4.3) becomes the incoming-suffix identity (0.4).  The
last suffix is full-ground.  Theorems 1.1 and 2.1 therefore give:

### Theorem 5.1 (high-pentagon complete upper-current cancellation)

Every height-`h` PBBS pentagon with `h>=4` has an explicit five-collar
owner-path decoration for which its complete arbitrary-width exterior
upper current is zero.

This includes all one-cut two-sided penetrations and all intervals crossing
several pentagon cuts.

### Corollary 5.2 (height-ladder support size)

For pentagons `h=4,...,H-1`, the collars use

\[
                         O(Hr)                            
\tag{5.1}
\]

owner transitions.  The height-two and height-three pentagons form a
bounded exceptional bank.  Therefore a prospective factor containing the
high collars has only `O(1)` unresolved upper target values from the low
end, not a defect growing with `H`.

The estimate (5.1) is polynomial and is internal to the middle-owner
factor.  It is not an additive length charge.

### Corollary 5.3 (exact incidence count and exposure)

Let

\[
                         N_H=H-4
\]

be the number of high pentagons `h=4,...,H-1`.  Suppose the prospective
choices are made so that the union of the collars and rethread edges is an
incidence path forest: the intended attachment at each `P_i` is the only
owner overlap, and every other owner and every lower colour is distinct.
Then the high protected bank has

\[
 e_{\rm high}=10N_H(r+4)                              \tag{5.2}
\]

incidence edges: five collars of `r+3` Johnson transitions and five
rethread transitions per pentagon, with two incidence edges per Johnson
transition.  A bounded low-height bank changes (5.2) by `O(1)`.

Its two exposure parameters, in the notation of the protected-factor
theorem, satisfy the proof-safe bounds

\[
                         \alpha\le85N_H+O(1),
 \qquad                 \beta\le30N_H+O(1).           \tag{5.3}
\]

Indeed Lemma 4.2 contributes at most `16` and `5`, respectively, per
collar path.  There are five paths per pentagon.  The five rethread head
owners and five rethread lower colours contribute at most five more to
the corresponding star loads.

In particular, if `H=O(sqrt(r))`, then

\[
 e=O(r^{3/2}),\qquad \alpha,\beta=O(\sqrt r).          \tag{5.4}
\]

Apply
`MATH_THEOREM_POLYNOMIAL_PROTECTED_FOREST_EXTENSION_FROM_TWO_EXPOSURES_20260805.md`
with its owner-rank parameter equal to `R=r+1` (its ground size
`2R-1` is the present `2r+1`).  Equations (5.2)--(5.4) make its exact
inequality

\[
 {R(R-1)\over2R-1}e
 \le
 \min\left\{
 {2(R-\alpha-1)-1\choose R-\alpha-1},
 {2(R-\beta-1)-1\choose R-\beta-1}+1
 \right\}                                             \tag{5.5}
\]

hold for all sufficiently large `r`.  Thus **once the prospective
cross-pentagon resource-disjoint planting is made**, there is no further
owner/lower-`q1` Hall obstruction to extending this entire polynomial
bank to a spanning two-factor.

## 6. Exact remaining gate

The theorem removes the **set-theoretic** two-sided exterior-current
obstruction.  The remaining global statement is now:

> **Correlated collar planting.**  Construct one owner/`q1` factor which
> simultaneously contains the PBBS height-pentagon connector bank and the
> synchronized collars of Lemma 4.1, absorbs their clipped residence flags,
> and preserves the typed common-cap/source-history interface.

The collar incidence bank is 2-bounded and has polynomial size
`O(Hr)=O(r^(3/2))` at the word deadline.  Corollary 5.3 and the polynomial
protected-factor theorem now supply its factor extension after a
cross-pentagon resource-disjoint prospective planting.  What remains is
that correlated planting itself, together with component control, the
absorption of the clipped residence flags, and preservation of the typed
common-cap/source-history interface.

## 7. Dependencies and scope

Used:

* `MATH_THEOREM_PBBS_HEIGHT_PENTAGON_FORCED_Q1_AND_RIGHT_RAY_REGENERATION_20260805.md`;
* `MATH_THEOREM_PBBS_PENTAGON_THREE_SCREEN_COMMON_HISTORY_AND_UPPER_CURRENT_GATE_20260805.md`;
* the elementary Johnson adjacency relation.

Not used: a solver, finite search, an unproved multiplicity estimate, or
an unproved claim that the collar bank already lies in the PBBS factor.
