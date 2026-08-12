# Every upper-tail injection has a disjoint second-facet projection, including the protected reset path

**Date:** 2026-08-01  
**Status:** unconditional exact two-endpoint ordered-diamond projection.
For the opened complete-reversal packet, all `4d+1` prescribed second-facet
tickets are retained under the existing hypothesis `m>=8d+4`.  This does
**not** close the rooted Catalan head row relative to a fixed predecessor
matching: the lower-colour/root compatibility remains correlated with head
injectivity and graphic acyclicity.

## 0. Outcome

Work on a ground set of order `2m-1`.  Put

\[
 {cal U}={[2m-1]\choose m+1},\qquad
 {cal O}={[2m-1]\choose m}.
\]

Suppose

\[
 \psi:{\cal U}\longrightarrow{cal O},\qquad
 \psi(R)\subset R                                      \tag{0.1}
\]

is injective.  Then there is another injection

\[
 \phi:{\cal U}\longrightarrow{cal O},\qquad
 \phi(R)\subset R,qquad \phi(R)\ne\psi(R)             \tag{0.2}
\]

for every `R`.

For the opened complete-reversal packet, let

\[
 Z_0,Z_1,\ldots,Z_h,qquad h=4d+1,                      \tag{0.3}
\]

be its protected rank-`m` root path and put

\[
 U_i=Z_i\cup Z_{i+1}\qquad(0\le i<h).                  \tag{0.4}
\]

If the given tail matching retains

\[
                         \psi(U_i)=Z_i,                 \tag{0.5}
\]

then the head matching may simultaneously be required to retain

\[
                         \phi(U_i)=Z_{i+1}.              \tag{0.6}
\]

Thus the upper-colour, tail-injectivity, and abstract second-facet
injectivity rows close exactly.  The selected arcs

\[
                         \psi(R)\longrightarrow\phi(R)
\]

form a partial permutation, but this theorem does not assert either that it
is rooted-compatible with the fixed predecessor matching or that it is
cycle-free.

## 1. Strict Hall after deleting the chosen tails

Delete from the containment graph `U--O` the selected edge
`R psi(R)` at every upper vertex.  Call the resulting graph `G_psi`.

Every upper set `R` has exactly `m+1` rank-`m` facets, so

\[
                         d_{G_\psi}(R)=m.               \tag{1.1}
\]

Every owner `T` has exactly

\[
                         (2m-1)-m=m-1                  \tag{1.2}
\]

rank-`m+1` supersets before the deletions.  Hence

\[
                         d_{G_\psi}(T)\le m-1.          \tag{1.3}
\]

### Theorem 1.1 (unconditional disjoint second-facet matching)

For every nonempty `X\subseteq\mathcal U`,

\[
 \boxed{
 |N_{G_\psi}(X)|
 \ge |X|+\left\lceil {|X|\over m-1}\right\rceil.}     \tag{1.4}
\]

Consequently `G_psi` has a matching saturating every upper vertex, and its
matched owner map is an injection `phi` satisfying (0.2).

#### Proof

Count the edges from `X` to its neighbourhood in two ways.  Equations
(1.1)--(1.3) give

\[
 m|X|\le(m-1)|N_{G_\psi}(X)|.
\]

Since

\[
 {m\over m-1}|X|=|X|+{|X|\over m-1},
\]

integrality gives (1.4).  In particular Hall's inequalities hold strictly
for every nonempty left family.  A saturating matching gives `phi`; the
deleted edges ensure `\phi(R)\ne\psi(R)`. \(\square\)

This proof is independent of how `psi` was chosen.  It closes the
unprotected head row without SBE, common-basis averaging, or a second
matroid intersection.

## 2. The complete-reversal root cycle is chordless

The forced protected heads require more than arbitrary deletion: after
using (0.6), both the protected upper vertices and the protected head
vertices must be removed before applying Hall.  The needed fact is that
the explicit reset path is induced in the Johnson graph.

### Lemma 2.1 (induced reset-plus-rail cycle)

The rank-`m` root cycle of the complete-reversal packet has no Johnson
chord.  Equivalently, two of its roots have union of rank `m+1` if and only
if they are consecutive on the displayed cycle.

#### Proof

Write `n=d+1`, and write the reset half as

\[
 T_a=C\cup\{X_a,X_{a+1},\ldots,X_{a+n-1}\},
 \qquad a\in\mathbb Z_{2n}.                             \tag{2.1}
\]

For two reset roots, Johnson distance is the cyclic distance between their
length-`n` private windows, truncated by reflection at `n`.  It equals one
only when their indices differ by `1` modulo `2n`.  Hence the reset segment
has no chord.

For the return rail, write `L=E\cap F`, let `alpha=F-L` and `delta=E-L`,
and pair the core labels `x_1,...,x_d` with the fresh labels
`y_1,...,y_d`.  Every rail root has the form

\[
 (L-X_A)\cup Y_A\cup\{\epsilon\},                      \tag{2.2}
\]

where `epsilon` is `alpha` or `delta`.  Along the `alpha` half,
`A={1,...,i}` is a prefix.  Along the `delta` half,
`A={j+1,...,d}` is a suffix.

Two roots with the same seam label have Johnson distance
`|A\mathbin\triangle B|`.
They are adjacent precisely at consecutive positions of their half.  Two
roots with different seam labels have distance

\[
                         1+|A\mathbin\triangle B|.      \tag{2.3}
\]

They are adjacent only when the prefix and suffix agree.  A prefix equals a
suffix only when both are empty or both are all of `[d]`.  These are exactly
the closing pair `F,E` and the central pair `P_d,Q_0`.

Finally, every internal rail root contains a fresh `y` and omits its paired
core `x`, while reset roots contain every core label and no `y`.  If at least
two pairs have been changed, Johnson distance from every reset root is at
least two.  With exactly one changed pair, the root is `P_1` or `Q_(d-1)`;
the fresh/missing pair already consumes the unique possible swap, so its
only reset neighbour is respectively `F` or `E`.

These cases exhaust the cycle and prove chordlessness. \(\square\)

### Corollary 2.2 (one reserved head per residual upper)

Let

\[
                         H=\{Z_1,\ldots,Z_h\}.          \tag{2.4}
\]

If an upper set `R` outside the protected family
`{U_0,...,U_(h-1)}` contains two vertices of `H`, then those two rank-`m`
sets are Johnson adjacent and have union `R`.  Lemma 2.1 makes them
consecutive protected roots, forcing `R=U_i` for some `i`, a contradiction.
Therefore

\[
 |N_{G_\psi}(R)\cap H|\le1
 \quad
 (R\notin\{U_0,\ldots,U_{h-1}\}).                     \tag{2.5}
\]

## 3. Forced protected second-facet completion

### Theorem 3.1 (protected second-facet completion)

Assume `psi` satisfies (0.5).  There is an injective `phi` satisfying
(0.2) and all prescribed equations (0.6).

#### Proof

The protected upper colours `U_i` are distinct, the second facets
`Z_(i+1)` are distinct, and each prescribed edge survives in `G_psi` because
`Z_(i+1)\ne Z_i`.

Delete the protected left bank

\[
                         L_0=\{U_0,\ldots,U_{h-1}\}
\]

and the protected right bank `H`.  Let `G'` be the remaining bipartite
graph.  By (1.1) and (2.5), every residual upper vertex has degree at least

\[
                         d_{G'}(R)\ge m-1.              \tag{3.1}
\]

Deleting right vertices cannot increase their degrees, so every residual
owner still has degree at most `m-1`.  Hence for every residual upper family
`X`,

\[
 (m-1)|X|\le e_{G'}(X,N(X))\le(m-1)|N_{G'}(X)|.        \tag{3.2}
\]

Thus `|N_G'(X)|>=|X|`, and Hall gives a matching saturating all residual
upper colours.  Adjoin the prescribed matching (0.6).  The two right banks
are disjoint by construction, so the union is the required injective
second-facet map. \(\square\)

The numerical hypothesis `m>=8d+4` is used upstream to plant the common
protected path and to construct `psi` retaining (0.5).  Once those objects
exist, Theorem 3.1 uses no further size inequality.

## 4. The rooted-coordinate correction

Fix a perfect predecessor matching

\[
 M_0:{[2m-1]\choose m-1}\longrightarrow{[2m-1]\choose m},
 \qquad L\subset M_0(L).                                \tag{4.1}
\]

For a tail ticket `T=psi(R)`, put

\[
 L(R)=M_0^{-1}(T),\qquad
 V_{M_0}(R,T)=L(R)\cup(R-T).                            \tag{4.2}
\]

The rooted Catalan occurrence of upper colour `R` with tail `T` has the
**unique** other owner corner `V_(M0)(R,T)`.  Therefore an arbitrary second
facet `phi(R)` delivered by Theorems 1.1 or 3.1 is a legal rooted head only
when

\[
 \boxed{
 M_0(\psi(R)\cap\phi(R))=\psi(R).}                    \tag{4.3}
\]

Equivalently,

\[
                         \phi(R)=V_{M_0}(R,\psi(R)).    \tag{4.4}
\]

The projection theorem does not impose (4.3).

There is already a two-ticket obstruction to treating it as automatic.
For `m=3`, take

\[
\begin{aligned}
 R_1&=\{1,2,3,4\},& T_1&=\{1,2,3\},&V_1&=\{1,2,4\},\\
 R_2&=\{1,2,3,5\},& T_2&=\{1,2,5\},&V_2&=\{1,2,3\}.
\end{aligned}                                           \tag{4.5}
\]

The tails are distinct and the second facets are distinct, but

\[
                         T_1\cap V_1=T_2\cap V_2=\{1,2\}.
                                                               \tag{4.6}
\]

Thus the induced lower colours collide.  No predecessor matching can map
that one lower colour to both tails.  Even when all intersections

\[
                         J(R)=\psi(R)\cap\phi(R)        \tag{4.7}
\]

are distinct, one still has to prove that the partial incidence matching

\[
                         J(R)\longmapsto\psi(R)         \tag{4.8}
\]

extends to a perfect predecessor matching `M_0`.

For the protected packet itself, equations (0.5)--(0.6) give

\[
 J(U_i)=Z_i\cap Z_{i+1}=I_i,\qquad M_0(I_i)=Z_i,       \tag{4.9}
\]

so its prescribed bank is rooted-compatible.  The unresolved issue is the
simultaneous completion of the unprotected bulk.

## 5. Exact remaining immediate-layer gate

Identify each upper colour `R` with the directed owner arc

\[
                         \psi(R)\longrightarrow\phi(R).
                                                               \tag{5.1}
\]

Both endpoint maps are injective, so (5.1) is a directed partial
permutation on the `W` owners with `U=W-C` arcs.  Its components are
directed paths and directed cycles.  If it has no cycle, it is already the
desired rooted Catalan forest with exactly `C=Cat_m` path components.

The protected immediate-layer problem has therefore reduced only to the
following **joint** target:

\[
 \boxed{
 \begin{gathered}
 \text{choose }(M_0,\phi)\text{ so that (4.3) holds for every }R,\\
 \phi\text{ is injective, and the arcs (5.1) are cycle-free.}
 \end{gathered}}                                             \tag{5.2}
\]

The strict Hall surplus (1.4) solves one projection of (5.2), but ordinary
Hall does not certify the rooted equation (4.3), distinct lower colours, or
cycle-freeness.  This is precisely the head/lower/root/graphic correlation
in the protected Catalan criterion; no all-`m` completion theorem is claimed
here.

Finite `-O3` audits on H100 found no counterexample:

* all `444` upper-tail injections at `m=3` admit an acyclic head completion;
* `20,000` randomized injections at `m=4` all admit one;
* for the explicit protected reset path at `d=1,...,7`, its largest upper
  clique has order two and every unprotected upper contains at most one
  protected head, agreeing with Lemma 2.1.

Those first two bullets test only the endpoint projection.  A separate
corrected audit imposes distinct intersections, extendability of
`J(R)->psi(R)` to a perfect predecessor matching, and cycle-freeness
simultaneously.  It passes all `444` injections at `m=3` and `2,000`
randomized injections at `m=4`; this is positive finite evidence, not a
general theorem.

The audit sources are

```text
scratch/audit_catalan_head_forest_completion_small_20260801.cpp
scratch/audit_reset_protected_head_overlap_20260801.cpp
scratch/audit_rooted_ordered_diamond_completion_small_20260801.cpp
```

The exact mathematical gain is independent of those finite checks: the
second-facet capacity projection, including all protected reset tickets, is
proved.  The remaining correlation is the simultaneous rooted equation
(4.3), lower-colour injectivity, head injectivity, and graphic
cycle-freeness.
