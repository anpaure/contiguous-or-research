# Joint minimum-rooted counter transfer

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

**Final status.**  The analytic implication below is correct, but the
combinatorial `O(sqrt(q))` target is false for the intrinsic MSW windows.
Section 18 gives an exact invisible-subtree family whose normalized
ordered collision count grows as `4^q/(4 pi q^3)`, even in the shallow
regime `q^2/m -> 0`.  Thus Sections 1--17 are a reduction and obstruction
audit, not an open route to (3.3).

Tracking the two individual counters removes the formal `+/-2` obstruction.
The move `+2` of the difference is simply the joint move `(-1,+1)` (up to
orientation) in the two-counter state.  More importantly, **arbitrary
coupling between the two counters costs nothing analytically**: if one
coordinate marginal of the joint shell kernel is dominated by the killed
critical Motzkin kernel, then the entire joint survival Green mass through
depth `q` is `O(sqrt(q))`.

The resulting analytic theorem is rigorous and allows an arbitrary,
time-dependent hidden overlap state.  The unresolved statement is purely
combinatorial: a genuine MSW collision shell must admit a reversible
deletion whose joint local weights have the required Motzkin marginal.
The depth-two values `3/8,1/4,3/8` and the depth-three one-ladder audit do
not prove that marginal, because the two depth-two parents of a genuine
depth-three bowtie are distinct.

## 1. The one-dimensional killed kernel

Put

\[
 p_{-1}={3\over8},\qquad p_0={1\over4},\qquad
 p_{+1}={3\over8}.
\tag{1.1}
\]

Let `T` be the substochastic kernel on `N_0` given by

\[
 T(x,x+i)=p_i\quad(i\in\{-1,0,1\},\ x+i\ge0),
\tag{1.2}
\]

with the transition from zero to minus one deleted.  Write

\[
                         s_r=\delta_0T^r\mathbf1.
\tag{1.3}
\]

### Lemma 1.1 (survival and Green mass)

There is an absolute constant `C` such that

\[
 \boxed{
 s_r\le {C\over\sqrt{r+1}},\qquad
 \sum_{r=0}^{q}s_r\le C\sqrt{q+1}.}
\tag{1.4}
\]

#### Proof

Realize `T` as the lazy walk with increment law (1.1), killed on first
visiting minus one.  Let `N_r` be the number of nonzero increments in its
first `r` steps.  Then `N_r` has law `Bin(r,3/4)`.  Conditional on
`N_r=a`, the nonzero skeleton is a simple symmetric walk of length `a`,
and the ballot/reflection identity gives

\[
 \Pr\left[\min_{j\le a}S_j\ge0\right]
 ={\binom a{\lfloor a/2\rfloor}\over2^a}
 \le {C\over\sqrt{a+1}}.
\tag{1.5}
\]

On `N_r>=r/2` this is `O(r^(-1/2))`, while
`Pr[N_r<r/2]<=e^(-cr)`.  This proves the first bound; summation proves the
second. \(\square\)

## 2. Arbitrarily coupled counters

The shell may carry additional overlap information, and that information
may grow with the depth.  Accordingly let `Omega_r` be an arbitrary set of
hidden states at time `r`.  Let

\[
 K_r:\mathbb R_+^{\mathbb N_0^2\times\Omega_r}
       \longrightarrow
       \mathbb R_+^{\mathbb N_0^2\times\Omega_{r+1}}
\tag{2.1}
\]

be any nonnegative, possibly time-inhomogeneous kernel.  It is supported
on counter increments `(i,j) in {-1,0,1}^2`, with transitions leaving the
nonnegative quadrant omitted.

### Definition 2.1 (one-coordinate Motzkin domination)

The sequence `(K_r)` has a killed Motzkin first marginal if, for every
`(x,y,omega)`, every `i in {-1,0,1}` with `x+i>=0`,

\[
 \boxed{
 \sum_{j,\omega'}
 K_r\big((x,y,\omega),(x+i,y+j,\omega')\big)\le p_i.}
\tag{2.2}
\]

For `x=0`, no mass is allowed to replace the omitted `i=-1` transition.
There is no restriction on the conditional coupling of `i` and `j`, and
no bound on `|Omega_r|`.

### Theorem 2.2 (arbitrary-coupling joint Green bound)

Let `mu_0` be a nonnegative source supported on first-counter height zero,
and put

\[
                         \mu_r=\mu_0K_0K_1\cdots K_{r-1}.
\tag{2.3}
\]

If (2.2) holds, then

\[
 \boxed{
 \|\mu_r\|_1\le {C\|\mu_0\|_1\over\sqrt{r+1}},\qquad
 \sum_{r=0}^{q}\|\mu_r\|_1
       \le C\|\mu_0\|_1\sqrt{q+1}.}
\tag{2.4}
\]

Consequently every joint return mass, every finite-boundary return mass,
and every accepted terminal mass is bounded by the same right-hand side.
The conclusion is uniform over all couplings, all hidden-state spaces, and
all time dependence.

#### Proof

Project onto the first counter:

\[
                         u_r(x)=\sum_{y,\omega}\mu_r(x,y,\omega).
\tag{2.5}
\]

Condition (2.2) gives coefficientwise

\[
                         u_{r+1}\le u_rT.
\tag{2.6}
\]

Since `u_0=||mu_0||_1 delta_0`, induction yields

\[
                         u_r\le\|\mu_0\|_1\delta_0T^r.
\tag{2.7}
\]

Sum over `x` and apply Lemma 1.1.  Any terminal/return subset has mass at
most the total surviving mass. \(\square\)

Only one marginal is needed.  If both individual shell counters have the
Motzkin marginal, one may root and project onto whichever counter is
convenient on a given irreducible piece.

In particular, let `Q=(q_ij)_(i,j in {-1,0,1})` be **any** coupling of the
law (1.1) with itself:

\[
 q_{ij}\ge0,qquad \sum_jq_{ij}=p_i,qquad\sum_iq_{ij}=p_j.
\tag{2.8}
\]

Restricting its walk to the nonnegative quadrant by killing every move
that exits the quadrant satisfies (2.2).  Hence every such coupling,
including synchronous, anti-synchronous, and state-dependent mixtures,
has joint survival Green mass `O(sqrt(q))` when started at a boundary
minimum.  No independence or joint local limit theorem is required.

### Corollary 2.3 (reflected alternative)

If the first marginal is stochastic/reflected rather than killed, total
survival need not decay.  Nevertheless, if its heat kernel satisfies

\[
                         \sup_z\widetilde T^r(0,z)le
                         {C\over\sqrt{r+1}},
\tag{2.9}
\]

then the total joint mass whose first coordinate lies in a fixed set `A`
is at most `C|A|/sqrt(r+1)`.  Hence localized returns still have
`O(sqrt(q))` Green mass.  A diagonal target such as `{x=y}`, however, is
not localized in either coordinate and can have mass one under synchronous
coupling.  Thus either killing or boundary localization is essential.

## 3. The exact combinatorial hypothesis

For one ladder, remove forward-disjoint cells and minimum-root each
remaining irreducible block.  Its critical letters are

\[
                         \mathcal A=\{-,C,+\},
\tag{3.1}
\]

with counter increments `-1,0,+1` and critical weights (1.1).  For a pair
of ladders the critical local alphabet is therefore

\[
                         \mathcal A^2,
\tag{3.2}
\]

which has nine letters.  The `+/-2` moves of the raw gap are exactly the
two pair letters `(+,-)` and `(-,+)`; no fifth one-counter direction is
needed.

The analytic theorem reduces the all-depth collision estimate to the
following statement.

### Joint shell marginal theorem (unproved combinatorial target)

Every centered intrinsic MSW collision pair can be partitioned into
irreducible shells and bounded geometric decorations so that:

1. one occurrence in each shell is rooted at its first global counter
   minimum, and deletion reads each half away from that minimum;
2. every critical deletion step has a pair letter `(a,b) in A^2` and a
   hidden overlap state; after summing over the second letter and all next
   hidden states, its normalized generating weight with first letter `a`
   is coefficientwise bounded by `p_a`;
3. a forbidden downward move from height zero is deleted, not reassigned
   to another letter;
4. forward-disjoint cells are regeneration cuts and all their insertions
   have a uniformly summable resolvent;
5. the shell list, hidden boundary data, and pointed base object reconstruct
   the collision pair with uniformly bounded multiplicity;
6. balanced-baseline collisions are removed before the nonnegative shell
   transfer is applied.

Under clauses 1--6, Theorem 2.2 gives `O(sqrt(q))` amplification for each
localized source.  With an `O(W)` source ledger this yields

\[
                         E_q=O(\sqrt q\,W),
\tag{3.3}
\]

which is sublinear in `q` and is sufficient for the prime-cycle smoothing
argument.

Clause 2 is the load-bearing new assertion.  It is stronger than saying
that the nine pair weights have scalar sum at most one: it requires the
three row marginals (or, symmetrically, column marginals) to be bounded by
`3/8,1/4,3/8`.  It is also not a consequence of the two separate
one-ladder tables.  At depth three the four depth-two parents of a genuine
bowtie are distinct, so the depth-two collision bijections cannot be
multiplied to manufacture this coupling.

## 4. Different minimum locations do not hurt the analytic bound

The two ladders need not attain their first minima at the same index.
Choose the first minimum of the first ladder and read its left and right
halves outward.  The first counter starts at the killing boundary on each
half.  The second counter starts at some nonnegative height and may be read
in either orientation; all its behavior is absorbed into the arbitrary
coupling and hidden state of Theorem 2.2.  Thus synchronized minima are not
an analytic requirement.

They may still matter combinatorially: deletion of the two halves must
carry enough boundary data to join them injectively.  This is part of
clause 5, not part of the Green estimate.

## 5. Is the pair-overlap alphabet bounded independently of `q`?

There are two different answers.

### 5.1 The raw local alphabet is bounded

A local cell records two consecutive pivot intervals in each ladder.  Its
order/equality type involves only the finitely many endpoints in those two
windows.  Hence the raw ordered pair alphabet is finite independently of
`q`; after deleting the forward-disjoint symbol it projects to the nine
letters in (3.2).  Reversing orientation on the left of a minimum merely
interchanges `+` and `-`.

### 5.2 A reconstructive Markov alphabet is not yet known to be bounded

Distant pivot endpoints of the two ladders may be identified or linked by
overlap data.  A finite local order alphabet does not prevent an unbounded
number of such links from remaining open across a deletion cut.  Encoding
those open links can require a state space growing with `q`, just as a
finite parenthesis alphabet can have unbounded stack depth.

A sufficient bounded-state hypothesis is:

> **Bounded-frontier hypothesis.** There is a deletion order for which at
> every cut at most `K` overlap identifications connect the deleted and
> undeleted portions, with `K` absolute; completed overlap components are
> closed permanently at the cut.

Under this hypothesis the equality/order type of the active frontier gives
a finite hidden alphabet depending only on `K`.  No such bounded-frontier
theorem has presently been proved for general MSW collision pairs.

Crucially, Theorem 2.2 does **not** require it: `Omega_r` may grow
arbitrarily.  Bounded frontier is needed only as a prospective way to prove
the marginal domination and reconstruction clauses locally.  Therefore an
unbounded pair-overlap alphabet is not itself an analytic obstruction.

## 6. Exact status

Proved here:

\[
 \boxed{
 \text{one killed Motzkin marginal}
 \Longrightarrow
 \text{joint Green mass }O(\sqrt q)
 \text{ under arbitrary coupling}.}
\]

This resolves the `+/-2` objection at the level of state choice and shows
that correlation between the two counters is harmless once a marginal
kernel is available.

Still unproved: the joint shell marginal theorem, especially the
coefficientwise row/column marginal bound and reversible reconstruction.
The raw pair-cell alphabet is uniformly finite, but a uniformly finite
reconstructive overlap state has not been established.

## 7. Exact depth-three obstruction to a raw-symbol marginal

The raw symbols alone do not give any sparsity in the joint alphabet.
The following three depth-three prototypes will be useful.  In each row
`R` is the common endpoint-`-6` core and `(b,a)` abbreviates the two pivot
triples.

\[
\begin{array}{c|c|c|c}
\text{first symbol}&R&(b_0,b_1,b_2);(a_0,a_1,a_2)&
       \text{two-symbol word}\\ \hline
+&000000&(2,3,1);(6,4,5)&(+,-)\\
C&000000&(2,1,5);(4,3,6)&(C,F)\\
-&00000100&(3,1,7);(4,5,8)&(-,F).
\end{array}                                                    \tag{7.1}
\]

### Lemma 7.1 (the raw `3 by 3` compatibility table is full)

Every ordered pair `(a,b) in {-,C,+}^2` occurs as the first joint cell
of a genuine depth-three collision.  The four depth-two parent targets
of the two occurrences can be required to be distinct.  Thus the raw
compatibility table is

\[
\begin{array}{c|ccc}
 &-&C&+\\ \hline
-&\checkmark&\checkmark&\checkmark\\
C&\checkmark&\checkmark&\checkmark\\
+&\checkmark&\checkmark&\checkmark.
\end{array}                                                     \tag{7.2}
\]

#### Proof

For the first prototype the four states on its six-step block are

\[
111000,\quad101001,\quad100101,\quad000111.
\]

Its edge counters are `(0,1,0)`.  For the second prototype the three edge
cores are

\[
100010,\qquad000110,\qquad001100,
\]

with selected pairs `(2,4)`, `(1,3)`, `(5,6)` and counters `(0,0,0)`.
For the third they have up-step sets
`{1,6,7}`, `{4,6,7}`, `{4,5,6}`, selected pairs
`(3,4)`, `(1,5)`, `(7,8)`, and counters `(1,0,0)`.
Lemma 2.1 of the MSW depth-two note verifies all nine edges directly;
the interval orders give exactly the last column of (7.1).

Every path `R` in (7.1) stays at or below zero, first reaches `-6` at its
last position, and ends there.  Consequently a concatenation

\[
                         R_{i_1}1^6R_{i_2}1^6\cdots1^6R_{i_t}             \tag{7.3}
\]

is again an endpoint-`-6` core.  For an occurrence supported on one
block, every preceding block followed by `1^6` is a zero-net prefix with
no `D_1`.  Every following word `1^6R_i`, when entered by an edge core at
height `-2`, rises to `4`, returns to `-2`, and has no `D_{-2}`.  Hence
all ordinal equalities and all local corridor conditions of that block
are unchanged.

Take two copies of each prototype as interior blocks of (7.3), with an
unused guard block on each side.  The guards ensure that every balanced
state visits both signs and hence belongs to an internal flaw class.
Choosing any two distinct interior blocks gives every ordered pair in
(7.2).  Their pivot coordinates lie in disjoint blocks, so the two
coordinates `b_2,a_0` from each occurrence are four distinct positions.
By (13.11k) of the MSW depth-three audit, the four depth-two parent
targets are therefore distinct. \(\square\)

The second obstruction is that a physical excursion shared by the two
occurrences is only one combinatorial object.  It cannot be charged as
two independent Catalan atoms.

### Lemma 7.2 (genuine shared-wrapper inflation)

Let `(A,B)` be any genuine depth-three collision over an endpoint-`-6`
core `S`.  Prepend to `S` a primitive positive excursion `E^+` based at
zero and append a primitive negative excursion `E^-` based at `-6`.
After shifting every pivot by `|E^+|`, the result is another genuine
collision with the same joint symbols.  Every counter of both occurrences
has increased by one.

The generating function of this common wrapper is

\[
                              K(u)^2,                         \tag{7.4}
\]

not `K(u)^4`.  Thus treating its two primitive excursions as independent
atoms for both coordinates undercounts its critical weight by the factor

\[
 {K(1/4)^2\over K(1/4)^4}=4.                                \tag{7.5}
\]

#### Proof

A primitive positive excursion contributes exactly one new `D_1` before
every pivot.  An edge core ends the old word at height `-2`; on that edge
core the appended negative excursion is based at `-2` and contributes
exactly one new `D_{-2}` after every pivot.  Thus both sides of every
ordinal equality increase by one.  Pivot heights and the corridors
between pivots are unchanged.  The wrapper is common to the physical core
and hence is chosen once, giving (7.4).  Since `K(1/4)=1/2`, (7.5)
follows. \(\square\)

More generally, before overlap identifications the two coordinate
kernels have four primitive factors.  If exactly `s` of those factors
are identified physically, their union has factor `K^(4-s)` rather than
`K^4`.  At the Catalan point the exact inflation table is

\[
\begin{array}{c|ccc}
s&0&1&2\\ \hline
\text{union factor}&K^4&K^3&K^2\\
\text{critical value}&1/16&1/8&1/4\\
\text{inflation}&1&2&4.
\end{array}                                                     \tag{7.6}
\]

Writing

\[
 H_C=K^2,\qquad H_-=H_+=L_2K^2,qquad
 L_2={1-u\over1-2u},                                         \tag{7.7}
\]

separate bounded-strip decorations simply multiply the three entries in
(7.6) by the appropriate `L_2` factors.  If an `L_2` decoration is itself
shared, replacing `L_2^2` by `L_2` contributes the critical ratio
`1/L_2(1/4)=2/3`; it does not cancel a two-factor Catalan sharing unless a
canonical parsing proves that the two events are coupled.  Thus neither
the product table nor its critical row sums survive unidentified sharing.

### Corollary 7.3 (the forgetful first-coordinate row bound is false)

Fix one interior prototype of first symbol `a`.  By repeating the other
interior blocks in (7.3), the same core and the same first occurrence can
have arbitrarily many distinct compatible second occurrences.  If a
wrapper deletion forgets which second occurrence was selected, `N` such
extensions give the row series

\[
                              N K(u)^2.                       \tag{7.8}
\]

Already `N=2` violates coefficientwise domination by each of the proposed
one-coordinate kernels in (7.7): `K^2` and `L_2K^2` all have leading
coefficient one, whereas (7.8) has leading coefficient two.  At `u=1/4`
it gives `1/2`, larger than both `p_C=1/4` and
`p_-=p_+=3/8`.

This is not a refutation of an injective joint-shell theorem.  It proves
that such a theorem cannot project away the second occurrence before the
local transition is charged.  The minimum extra normalization is:

1. the current hidden state retains the selected second occurrence, or an
   injective anchor for it, through every shared-wrapper deletion;
2. every physical primitive excursion has one canonical owner (a cell, a
   regeneration cut, or the source ledger), and is charged exactly once;
3. all open overlap identifications needed to decide that ownership are
   present in the current state, not introduced among the next states
   after the row sum is taken;
4. common `F` overlap loops and common outer wrappers are absorbed once at
   their owner and cannot reappear as freely iterable transitions.

Only after such a reversible ownership rule is fixed does the
coefficientwise question

\[
 \sum_{b,\omega'}Q_{a,b}^{\omega,\omega'}(u)
 \preceq H_a(u)                                               \tag{7.9}
\]

have an invariant meaning.  Lemmas 7.1--7.2 show respectively that no
symbolic exclusivity proves (7.9), and that naive independent charging
gives the wrong weight by factors up to four.  Establishing (7.9) for a
specific ownership-preserving deletion remains the exact combinatorial
gate.

## 8. Lexicographic ownership: the exact remaining local conflict

There is a natural minimal repair of the failure in Corollary 7.3.  A
deletion state is an ordered selected collision pair together with its
active overlap frontier,

\[
                         \omega=(S,A,B,\mathfrak F).          \tag{8.1}
\]

Order all incident slots lexicographically by `(coordinate,cut)`.  Every
physical primitive excursion component is owned by its first incident
slot.  Its word is recorded and charged only at that owner; every other
incident slot carries a pointer to the owner and a bit saying whether the
component has already been removed.  The frontier `mathfrak F` contains
these pointers and bits before the outgoing row is summed.

For the common wrapper in Lemma 7.2 this rule is reversible.  The positive
word is the first primitive return to zero at the marked left boundary and
the negative word is the last primitive departure-and-return at the marked
right boundary.  Deletion records the two words at the first cut, and
reinsertion there restores the unique common wrapper.  Later cuts see
owner pointers and charge neither word again.  Its one-time row weight is
`K^2`, which equals `H_C` and is coefficientwise bounded by
`H_-=H_+=L_2K^2`.

This ownership rule removes duplicate charging, but it does not by itself
prove the desired marginal.  Under the still-hypothetical product parsing
in which each coordinate first receives its depth-two kernel, the exact
formal residual test is as follows.  Put

\[
 d(C)=0,\qquad d(-)=d(+)=1,
 \qquad H_a=L_2^{d(a)}K^2.                                  \tag{8.2}
\]

Suppose a joint cell has first symbol `a`, second symbol `b`, exactly `s`
of its four primitive Catalan factors are physically identified, and `t`
of its bounded-strip factors are identified.  Here `0<=s<=2`, and
`t=1` is possible only when both symbols are offset types.  Unique
ownership gives the union series

\[
 Q_{a,b}^{s,t}(u)
   =L_2(u)^{d(a)+d(b)-t}K(u)^{4-s}.                          \tag{8.3}
\]

Relative to the proposed first-coordinate budget, its critical ratio is

\[
 {Q_{a,b}^{s,t}(1/4)\over H_a(1/4)}
   =\left({3\over2}\right)^{d(b)-t}2^{s-2}.                 \tag{8.4}
\]

Consequently the complete one-entry critical audit is

\[
\begin{array}{c|c|ccc}
\text{second type}&\text{strip status}&s=0&s=1&s=2\\ \hline
C&\text{none}&1/4&1/2&1\\
+\text{ or }-&\text{independent}&3/8&3/4&3/2\\
+\text{ or }-&\text{shared}&1/4&1/2&1.
\end{array}                                                   \tag{8.5}
\]

The last row applies only when `a` is also an offset type.  Thus all
primitive-only cases pass at the Catalan point.  The unique smallest
critical conflict is

\[
 \boxed{
 b\in\{-,+\},\qquad s=2,\qquad t=0: 
 \quad Q(1/4)={3\over2}H_a(1/4).}                            \tag{8.6}
\]

In words: the two coordinate cells share both primitive excursions, but
the second offset cell retains an independent bounded-strip decoration.
Lexicographic ownership correctly charges each shared excursion once, yet
there remains an uncompensated factor `L_2(1/4)=3/2`.  Therefore a
successful MSW parsing must prove one of the following structural facts:

* double primitive sharing forces the offset strip to be shared as well;
* the independent strip is a one-off decoration owned by a regeneration
  cut or source rather than an iterable cell factor; or
* the offending pattern is impossible for genuine adjacent MSW windows.

Absent one of these statements, the critical marginal fails even after
canonical ownership.

There is also a distinction between critical-value and coefficientwise
domination.  Since `K(1-K)=u`,

\[
 K^r-K^{r+1}=uK^{r-1}\succeq0,                              \tag{8.7}
\]

so every entry with second type `C` is coefficientwise bounded by `H_a`.
An independent strip can destroy this stronger order even when (8.4) is
less than one.  For example

\[
 [u^6]K^2=42,\qquad [u^6]L_2K^3=47,                         \tag{8.8}
\]

although `(L_2K)(1/4)=3/4`.  Thus a proof based only on the critical norm
may still be viable, but it is not automatically the coefficientwise
theorem stated in clause 2.  It must supply a coefficient majorant or use
a critical weighted norm with a separate finite-prefix estimate.

Finally, retaining `B` in (8.1) prevents the outgoing multiplicity in
(7.8), but it moves those `N` choices into distinct source states.  Hence
the repair is useful only together with an `O(W)` ledger for the ordered
anchored base states; otherwise the original collision energy has merely
been moved into `||mu_0||_1`.  At depth three the remaining combinatorial
question is whether a common-core deletion makes the formal pattern (8.6)
an intrinsic case at all.  The next section answers this preliminary
question negatively for the presently available data.

### 8A. Pure shared-atom pinning is exactly critical

The factor `K^(-1)=2` at the Catalan point can be read as contact fugacity
two for one physically shared primitive excursion.  It does not by itself
cause exponential growth.  The unrestricted primitive Catalan kernel is
exactly critical:

\[
 K(u)={1-\sqrt{1-4u}\over2},\qquad K(1/4)={1\over2},
\]

and

\[
 \boxed{{1\over1-2K(u)}={1\over\sqrt{1-4u}}.}               \tag{8.9}
\]

Thus repeated single-atom contacts have central-binomial coefficients,
of the same order as `W`.  For double-atom contacts the relative fugacity
is four and

\[
 \boxed{
 {1\over1-4K(u)^2}
 ={1\over(1-2K(u))(1+2K(u))}.}                              \tag{8.10}
\]

The second factor is analytic and nonzero at `u=1/4`, so this resolvent
has the same square-root singularity and again has
`O(binomial(2m,m))` coefficients.

Accordingly a genuine renewal of pure single or double shared primitive
atoms is compatible with the desired ambient-size ledger even at equality.
The dangerous formal event (8.6) is more specific: after critical double
sharing it retains an independent bounded-strip factor with
`L_2(1/4)=3/2`.  Repetition of that decoration is supercritical.  A
common-`S` deletion need not prove a strict defect in the primitive contact
kernel; it is enough to prove that the extra strip is shared, is charged
once at a source/regeneration cut, or is impossible.

Equations (8.9)--(8.10) use the ambient semilength generating variable.
They do not create the missing contact renewal.  Section 9 still shows
that a shared contact is not an intrinsic event until a reversible
common-`S` parsing has been specified.

## 9. The formal bad pattern is not an intrinsic MSW pattern

The factors in (8.3) came from the depth-two collision kernels, but a
depth-three collision does not supply the common targets needed to invoke
those kernels.

### Theorem 9.1 (same-target mismatch)

Let `A` and `B` be the two occurrences of a genuine depth-three bowtie
over the common endpoint-`-6` core `S`.  Their two depth-two windows have
the four endpoint-`-4` cores

\[
 z_0^A=S+\{b_2^A\},\qquad z_1^A=S+\{a_0^A\},\qquad
 z_0^B=S+\{b_2^B\},\qquad z_1^B=S+\{a_0^B\}.                \tag{9.1}
\]

In the shared-parent-removed sector these four paths are distinct.  The
factorization

\[
                         H_\pm=L_2K^2                         \tag{9.2}
\]

of Lemma 13.8 is defined only for two nested offset occurrences over one
and the same endpoint-`-4` path `z`.  Consequently none of the four
windows in (9.1) canonically supplies an `L_2K^2` shell with another
window.  In particular, the integers `(s,t)` in (8.3), and hence the
formal bad event (8.6), are not determined by the genuine bowtie data
`(S,A,B)` plus lexicographic ownership of already identified physical
excursions.

#### Proof

Formula (9.1) is the exact subtarget identity (13.11k), applied to each
occurrence.  The distinctness is precisely the definition of the sector
remaining after equal depth-two parents are removed.

In Lemma 13.8 the `L_2` block is the path between two successive selected
`D_1` steps of a single word `z`; the positive `K` block ends at the next
selected `D_1` of that same word, and the negative `K` block lies between
the corresponding selected `D_{-4}` steps of the same word.  All three
blocks use the common renewal index

\[
 D_1(z;[1,P))=D_{-4}(z;(Q,2m]).                              \tag{9.3}
\]

Changing `z` to `S+\{v\}` changes heights by two after `v` and changes
which steps are counted in (9.3).  Equality of a physical substring does
not therefore identify either its renewal endpoints or its role as an
`L_2` versus a primitive block.  Since the four choices of `v` in (9.1)
are distinct, Lemma 13.8 cannot be applied to any pair merely from the
adjacent inverse criteria.

Lexicographic ownership chooses an owner only after an excursion
component and all its incident cuts have been specified.  It cannot
create the missing common word, renewal endpoints, or incidence
relation.  For example, the wrapper of Lemma 7.2 can reversibly be owned
by the first cell, giving `s=2`, or absorbed as one source decoration,
giving no cell value of `s`; the physical collision and all adjacent
inverse criteria are identical.  Thus `(s,t)` is not intrinsic.
\(\square\)

### Corollary 9.2 (what must precede a decision on (8.6))

The adjacent MSW inverse criteria alone can neither prove that (8.6)
forces strip sharing nor exhibit it as an iterable cell.  Either claim
would first have to construct a common-`S` deletion that:

1. selects the shell endpoints directly in the endpoint-`-6` path `S`;
2. parses every physical block as a strip, a primitive excursion, or a
   one-off decoration before applying lexicographic ownership;
3. records all incidences in the incoming frontier state;
4. is reversed by its typed shell record with uniformly bounded
   multiplicity.

Only for that specified map do `s`, `t`, and the alternatives in (8.6)
become mathematical predicates.  Thus (8.6) is a diagnostic table for a
future deletion, not yet a counterexample to the joint marginal theorem.

The source ledger imposes a further exact restriction.

### Lemma 9.3 (one-anchor source is linear; a pair source is circular)

The total number of pointed intrinsic depth-three lower occurrences at
semilength `m` is

\[
 N_{\alpha,3}=(m-2)\operatorname{Cat}_m
 ={m-2\over2m+1}W<{W\over2}.                                \tag{9.4}
\]

Hence terminal data consisting of one selected occurrence and one of
`O(1)` boundary/frontier types have total mass `O(W)`.  Terminal data
that retain an arbitrary ordered collision pair instead have mass
`2P_3`, up to the diagonal convention, and using them as the source in
Theorem 2.2 is circular.

#### Proof

Every canonical MSW column has `m-2` intrinsic depth-three slots, and
there are `Cat_m` columns.  Also

\[
                         W=(2m+1)\operatorname{Cat}_m,
\]

which proves (9.4).  An ordered pair source counts exactly the pointed
collision pairs whose energy is to be bounded. \(\square\)

Accordingly, an ownership-preserving transfer may retain the ordered pair
and its frontier during deletion, but at its terminal cut the two records
must coalesce to one anchored occurrence plus bounded boundary data; the
typed shell list must reconstruct the other occurrence.  This coalescence
and the common-`S` parsing of Corollary 9.2 are the two missing
combinatorial statements.  Until they are proved, assigning the
depth-two values `L_2K^2` to the two coordinates of a depth-three bowtie
is circular, and the apparent sole conflict (8.6) has no invariant
truth value.

## 9A. Direct common-core inverse criterion and spatial faces

There is nevertheless an exact starting object that does not import any
depth-two collision kernel.  Let `S` be a length-`2m` path with `m-q`
up-steps, hence endpoint `-2q`.  For one proposed occurrence choose
pairwise distinct down-step positions of `S`

\[
 b_0,\ldots,b_{q-1},a_0,\ldots,a_{q-1},
 \qquad b_t<a_t.                                             \tag{9.5}
\]

Put

\[
 L_t=\{a_j:j<t\}\cup\{b_j:j>t\},\qquad
 C_t=S+L_t,qquad
 \nu_t(x)=|L_t\cap[1,x)|.                                  \tag{9.6}
\]

Thus `C_t` has endpoint `-2`, and

\[
                         H_{C_t}(x)=H_S(x)+2\nu_t(x).         \tag{9.7}
\]

### Lemma 9.4 (exact all-depth common-`S` inverse criterion)

The data (9.5) form an intrinsic depth-`q` lower occurrence over `S` if
and only if, for every `0<=t<q`, the following four conditions hold:

\[
 H_S(b_t)+2\nu_t(b_t)\in\{0,1\},\qquad
 H_S(a_t)+2\nu_t(a_t)\in\{-2,-1\},                          \tag{9.8}
\]

there is no position `x` with `b_t<x<a_t` such that

\[
 \bigl(S_x=1\ \text{or}\ x\in L_t\bigr)
 \quad\text{and}\quad
 H_S(x)+2\nu_t(x)\in\{-2,-1\},                             \tag{9.9}
\]

and

\[
\begin{split}
 &|\{x<b_t:S_x=0,\ x\notin L_t,
                 \ H_S(x)+2\nu_t(x)=1\}|\\
 &\qquad=
 |\{x>a_t:S_x=0,\ x\notin L_t,
                 \ H_S(x)+2\nu_t(x)=-2\}|.
\end{split}                                                   \tag{9.10}
\]

For a collision pair, take two diagrams `A,B` satisfying
(9.5)--(9.10) over the same `S`; positions may coincide between the two
diagrams, but are distinct inside each diagram.  This is an exact
common-core description with `4q` marked endpoints before cross-diagram
identifications.

#### Proof

The balanced states encoded by the diagram are

\[
 X_t=S+\{a_j:j<t\}+\{b_j:j\ge t\}\qquad(0\le t\le q).       \tag{9.11}
\]

Their `t`-th edge core is exactly `C_t=X_t\cap X_{t+1}`, and the
selected pair on that edge is `(b_t,a_t)`.  Equation (9.7) translates
the two height conditions of Lemma 2.1 into (9.8).  The up-steps of
`C_t` are precisely the old up-steps of `S` together with the positions
in `L_t`, giving (9.9).  Its down-steps are precisely the down-steps of
`S` outside `L_t`; substituting (9.7) into the two ordinal counts gives
(9.10).  Every translation is reversible, and composing the `q` valid
edges gives (9.11). \(\square\)

For `q=3`, Lemma 9.4 is a finite system on the twelve endpoints of the
ordered collision pair and is strictly stronger than listing the two
Motzkin symbols: it retains every cross-occurrence equality and every
height shift caused by the other pivots.

### Lemma 9.5 (canonical common spatial face atomization)

For an ordered collision diagram `(S,A,B)`, sort the distinct positions
in the union of its `4q` pivot endpoints and cut `S` at those marked
steps.  These cuts give at most `4q+1` open faces.  On each face `F`, all
`2q` quantities

\[
                  (\nu_t^A,\nu_t^B)_{0\le t<q}              \tag{9.12}
\]

are constant.  Within `F`, make an additional cut immediately before and
after every step which appears in one of (9.9)--(9.10), and at every
visit to one of the corresponding barrier levels

\[
 1-2\nu_t^\epsilon,\qquad -1-2\nu_t^\epsilon,\qquad
 -2-2\nu_t^\epsilon
 \quad(\epsilon\in\{A,B\},\ 0\le t<q).                      \tag{9.13}
\]

The resulting ordered marked steps and maximal intervening subpaths are
canonical **common spatial atoms**.  Recording their words, boundary
heights, the endpoint order/equality type, and their incidences with
(9.9)--(9.10) reconstructs `(S,A,B)` uniquely.  A physical atom incident
with several coordinates or cuts may therefore be assigned to the
lexicographically first incidence without duplication.

#### Proof

Constancy in (9.12) follows because a face contains no pivot.  Hence the
levels relevant to every inverse condition are the fixed finite set
(9.13) on that face.  Cutting at all marked event steps and all visits to
these levels is deterministic.  Concatenating the recorded atoms and
reinstating the marked pivot steps recovers `S`; the stored endpoint type
recovers both pivot diagrams.  Conversely the diagram uniquely produces
the cuts and records. \(\square\)

Lemma 9.5 is deliberately an atomization, not yet a useful shell
factorization.  It provides the incidence relation that was missing in
Theorem 9.1 and makes lexicographic ownership well-defined.  It does not
show that the owned atom series has a Motzkin marginal, that the active
frontier is small, or that deleting an atom leaves another valid diagram.

### Proposition 9.6 (the current exact state has no cycle test)

If the hidden state is the full residual diagram from Lemma 9.5, and a
transition consumes at least one pivot cell or one owned spatial atom,
then its directed state graph is acyclic.  Therefore the request for two
accessible cycles with different average counter increments is not yet a
well-defined test of the exact common-`S` model.  A cycle appears only
after one proves a quotient which forgets absolute locations and atom
words while preserving reversible reconstruction and transition weights.

#### Proof

Order residual states by the pair

\[
 (\text{number of undeleted pivot cells},
   \text{total length of undeleted owned atoms})              \tag{9.14}
\]

lexicographically.  Every stated deletion strictly decreases (9.14), so
there is no directed cycle.  Projecting merely to the symbols
`{-,C,+,F}` creates formal cycles, but Lemma 7.1 shows only that their
edges are separately realizable; it does not identify their full frontier
states.  Such projected cycles may therefore be artifacts. \(\square\)

Thus the non-coboundary alternative in a future Markov-additive theorem
must be checked only after constructing a translation-invariant quotient
of the owned face process.  At that point two cycles with different
increment sums would disprove the coboundary case; before that quotient,
neither a positive cycle certificate nor a coboundary obstruction follows
from the adjacent signatures alone.

### Corollary 9.7 (anchored source ledger at every depth)

The total number of pointed intrinsic lower depth-`q` occurrences is

\[
 N_{\alpha,q}=(m-q+1)\operatorname{Cat}_m
 ={m-q+1\over2m+1}W<W.                                     \tag{9.15}
\]

Hence a terminal source consisting of one anchored occurrence and a
uniformly bounded set of quotient-frontier states has mass `O(W)`; for
`q=3` it has mass less than `W/2` before the bounded state factor.  A
valid owned-shell quotient must therefore coalesce the ordered pair to
one such anchor.  Storing both residual occurrences at the terminal state
instead restores the unknown collision mass and gives no estimate.

The exact next combinatorial object is now isolated: a reversible quotient
of the common spatial atomization in Lemma 9.5 which (i) deletes owned
atoms while preserving (9.8)--(9.10), (ii) terminates at the one-anchor
ledger (9.15), and (iii) has either a killed one-coordinate marginal or
a non-coboundary Markov-additive return bound.  No `L_2` or `K` label from
a distinct depth-two target is needed in its definition.

## 10. Drift audit: return localization is not survival domination

The Markov-additive shortcut "nonzero drift is better" must be qualified.
It is true for return probabilities to a fixed finite set, but it is false
for the survival Green mass used in Theorem 2.2.

### Lemma 10.1 (one-sided drift trichotomy)

Let `S_t` be an aperiodic finite-range integer walk started at zero and
killed on its first visit to the negative half-line.  Assume its increment
law has nonzero variance and mean `mu`.

1. If `mu<0`, then the survival probability decays exponentially.
2. If `mu=0`, then the survival probability is `Theta(t^(-1/2))`.
3. If `mu>0`, then the probability of never being killed is positive, so
   the survival Green mass through time `q` is `Theta(q)`.

In the third case the return probability to any fixed finite set still
decays exponentially.

#### Proof

For negative drift, choose a small positive exponential tilt for which the
one-step moment generating function is strictly below one and apply the
standard exponential supermartingale bound.  The zero-drift assertion is
the ballot/fluctuation estimate used in Lemma 1.1.  For positive drift,
the strong law gives escape to `+infinity`, and the classical ruin
probability is strictly below one for a finite-range nondegenerate walk;
therefore survival has a positive limiting probability.  A Chernoff bound
places `S_t` at distance `Theta(t)` from every fixed finite set except on
an exponentially small event, proving the last assertion.  \(\square\)

### Consequence 10.2 (the exact qualitative gate)

For the present transfer, a finite shell graph with two cycles of different
average increment proves non-coboundary variance, but by itself it does not
prove the required `O(sqrt(q))` **survival** Green bound.  One additionally
needs one of:

* zero stationary drift, uniformly nondegenerate variance, and the killed
  local-limit/ballot estimate;
* stationary drift uniformly toward the killing boundary; or
* a new reconstruction theorem showing that all accepted terminal states
  lie in a fixed boundary set, so that return rather than survival mass is
  the relevant quantity.

Thus drift away from the boundary is favorable only after terminal
localization has been proved.  Without that localization it gives the
fatal linear amplification, just as a coboundary does.

## 11. Contact fugacity after common-core phase pinning

The common spatial atomization identifies exactly where the formal
critical factors `2K` and `4K^2` arise.  For a barrier level `h`, there
are two primitive excursions,

\[
 E_h^\uparrow=U_h A D_{h+1},\qquad
 E_h^\downarrow=D_h B U_{h-1},                              \tag{11.1}
\]

where `A` stays strictly above `h` and `B` strictly below `h`.  Each has
series `K(u)`.

### Lemma 11.1 (a pinned count contact has one orientation)

Fix a face, an incidence `(epsilon,t)`, its height shift `2 nu`, and a
down-step level `ell` in the shifted edge core.  The departure/return
boundary down-step of a primitive spatial atom based at raw height `h` is
the distinguished `D_ell` precisely in one of the two mutually exclusive
phases

\[
 \begin{array}{c|c}
 \text{upper phase}&h+2\nu=\ell-1,\\
 \text{lower phase}&h+2\nu=\ell.
 \end{array}                                                  \tag{11.2}
\]

Consequently, after the raw boundary height and incidence are present in
the incoming frontier, an owned single contact has series at most `K`,
and two independently located owned contacts have series at most `K^2`.
If one forgets the phases before taking the row sum, the corresponding
unrestricted bounds are exactly

\[
 2K(1/4)=1,\qquad 4K(1/4)^2=1,                              \tag{11.3}
\]

whereas the phase-pinned values are `1/2` and `1/4`.

#### Proof

In the shifted core, the final down-step of `E_h^\uparrow` is
`D_(h+1+2nu)`, while the first down-step of `E_h^\downarrow` is
`D_(h+2nu)`.  Setting either label equal to `ell` gives (11.2).  The two
equalities differ by one and cannot hold for the same pinned `h,nu,ell`.
Both primitive classes are counted by `K`.  Summing the two possible
unpinned phases gives `2K`; doing this independently at two contacts gives
`4K^2`.  Use `K(1/4)=1/2`. \(\square\)

For the MSW ordinal equality the left contact has `ell=1` and the right
contact has `ell=-2`.  If one physical atom is incident with several
coordinates, Lemma 11.1 is applied to every incidence.  Incompatible
orientation requirements give no transition; compatible requirements
still describe one physical word, charged once to its lexicographic
owner.

### Corollary 11.2 (outer shared contacts have a strict defect)

For the common wrapper of Lemma 7.2 the left boundary is pinned at height
zero and the right boundary, in every edge core, is pinned at height
`-2`.  Hence the only count-changing orientation pair is

\[
                         (E_0^\uparrow,E_{-2}^\downarrow),    \tag{11.4}
\]

with series `K^2`.  The opposite orientations contribute neither the
required left `D_1` nor the required right `D_{-2}`, and a mixed choice
changes only one side of (9.10), so it is invalid as an active wrapper.
Repeated active wrappers therefore have nonempty renewal series

\[
 {K(u)^2\over1-K(u)^2},\qquad
 {K(1/4)^2\over1-K(1/4)^2}={1\over3}.                       \tag{11.5}
\]

Thus the outer common-`S` contact kernel is genuinely subcritical; the
formal factor `4K^2` overcounts it by forgetting both pinned boundary
phases.

There is, however, no corresponding theorem yet for every interior
inter-contact transition.

### Proposition 11.3 (phase refinement alone does not give row defect)

The full face state of Lemma 9.5 records the phase in (11.2), so every
individual owned contact entry is bounded by `K` or `K^2`.  A quotient
state which records only the current phase but allows both phases for the
next contact has row bound `2K`, or `4K^2` for a contact pair, and is
exactly critical at `u=1/4`.  Strict subcriticality therefore requires a
genuine common-`S` statement that, from every incoming quotient state,
either

1. at least one next phase is forbidden;
2. the phase choices share a physical atom and hence are not additive; or
3. one choice is an inert/source decoration rather than an iterable
   contact.

#### Proof

Lemma 11.1 bounds each phase entry.  If both next phases are compatible
and correspond to distinct atoms, their nonnegative series add to `2K`;
two independent contacts give the four products and sum to `4K^2`.
Equation (11.3) shows that no strict defect remains.  Lexicographic
ownership prevents duplicate charging of one atom but does not remove two
genuinely distinct next atoms. \(\square\)

The direct atomization therefore has a sharp, mixed outcome.  It proves a
defective renewal kernel for the pinned outer contacts, and it identifies
the two-bit phase information whose loss creates the critical fugacity.
It does **not** prove a defective general inter-contact kernel: that would
amount to proving one of the three structural alternatives in Proposition
11.3 for the reversible anchored quotient requested after Corollary 9.7.
Conversely, merely summing the two or four unrestricted phases proves
critical renewal, not decay.  This is the exact contact-level gate.

## 12. Barrier-gap quotient for interior contacts

The two phases in Lemma 11.1 can be separated using only local data from
the common core.  Let `F` be an open spatial face and put

\[
 \mathcal I(F)=\{(\epsilon,t):b_t^\epsilon<F<a_t^\epsilon\},
 \qquad
 V(F)=\{\nu_t^\epsilon(F):(\epsilon,t)\in\mathcal I(F)\}.    \tag{12.1}
\]

The clean-corridor conditions forbid raw up-steps at the barrier levels

\[
 \mathcal B(F)=
 \bigcup_{v\in V(F)}\{-2-2v,-1-2v\}.                       \tag{12.2}
\]

### Lemma 12.1 (consecutive barriers are one-way membranes)

If \([r,s]\cap\mathbb Z\) is a consecutive component of `V(F)`, then

\[
 \bigcup_{v=r}^{s}\{-2-2v,-1-2v\}
   =[-2-2s,-1-2r]\cap\mathbb Z.                             \tag{12.3}
\]

Inside `F` the path can cross this entire band downward, but after doing
so it cannot return above it.  In particular, a closed primitive contact
whose return up-step starts in the band is impossible; a down-step through
the band is a one-off passage rather than an iterable contact.

#### Proof

The two levels for `v+1` are the two integers immediately below the two
levels for `v`, proving (12.3).  Every upward crossing of an edge in the
band starts at a member of \(\mathcal B(F)\) and is forbidden by (9.9).
Hence a return after a downward crossing is impossible. \(\square\)

For an incidence with shift `2 nu`, the raw down-step levels counted on the
two sides of the ordinal equality are

\[
 \lambda_L=1-2\nu,\qquad \lambda_R=-2-2\nu.                 \tag{12.4}
\]

A primitive contact using `D_lambda` has gateway level
`g=lambda-1` and exactly the two forms

\[
 U_g A D_\lambda\quad\text{or}\quad D_\lambda B U_g.        \tag{12.5}
\]

Both forms use the same up-step level `g`—at departure in the first form
and at return in the second.

### Lemma 12.2 (exact phase classification at a face)

For a left contact of shift `nu`, the gateway is forbidden exactly when
`nu-1 in V(F)`.  For a right contact it is forbidden exactly when
`nu+1 in V(F)`:

\[
\begin{array}{c|c|c}
\text{role}&g&g\in\mathcal B(F)\ \Longleftrightarrow\\ \hline
L&-2\nu&\nu-1\in V(F),\\
R&-3-2\nu&\nu+1\in V(F).
\end{array}                                                   \tag{12.6}
\]

If the displayed adjacent value is present, neither form in (12.5) is a
closed renewable contact; its `U_g` is forbidden.  If it is absent, the
two forms lie on opposite sides of the same barrier edge.  Their residual
cut heights are respectively `g` and `g+1=lambda`, so they belong to two
different incoming face states.  From a state which retains the barrier
side—or merely the parity of the residual cut height—at most one phase is
available, with series `K`, not `2K`.

#### Proof

For the left role, `g=-2nu`.  It equals the even barrier `-2-2v`
precisely for `v=nu-1`, and cannot equal an odd barrier.  For the right
role, `g=-3-2nu`; it equals the odd barrier `-1-2v` precisely for
`v=nu+1`, and cannot equal an even barrier.  This proves (12.6).
Lemma 12.1 excludes a closed return when `g` is forbidden.  Otherwise
(12.5) shows that the upper primitive is based at `g` and the lower
primitive at `g+1`.  Those heights have opposite parity and remain
distinct after the primitive word is deleted. \(\square\)

Both phases are genuinely realizable when the gateway is free.  The
standard wrapper uses \(E_0^\uparrow\) on the left and, in every shifted
edge core, \(E_{-2}^\downarrow\) on the right.  For the opposite phases,
prepend

\[
                         U_0\,E_1^\downarrow\,D_1
\]

and append to the raw endpoint-`-2q` core

\[
                  D_{-2q}\,E_{-2q-1}^\uparrow\,U_{-2q-1}.   \tag{12.7}
\]

The first word adds two prefix `D_1` contacts.  In every edge core the
second word is shifted to
\(D_{-2}E_{-3}^\uparrow U_{-3}\) and adds two suffix `D_(-2)` contacts.
Both words are zero-net and lie outside all pivot corridors, so
(9.8)--(9.10) are preserved.  Hence neither phase can be discarded
globally.  They occur at different residual cut heights; Lemma 12.2 says
they are not outgoing alternatives from one height-pinned state.

### Definition 12.3 (the barrier-gap anchored quotient)

A local quotient state retains:

1. one anchored occurrence `A`;
2. the ordered pivot-endpoint skeleton of the residual second occurrence;
3. for the current face, the ordered consecutive components of `V(F)`
   and the chamber containing the cut height;
4. the lexicographic owner incidence of the next contact and its
   left/right role;
5. the incidence-balance vector recording, for every edge equation, the
   number of deleted left `D_1` contacts minus deleted right `D_{-2}`
   contacts.

The internal word of a deleted primitive atom is carried by the transition
record, not by the state.  Among quotients that normalize vertical height,
the chamber-side parity bit is minimal: merging it identifies the two
residual heights in (12.5) and restores the critical row `2K`.

Call a finite owned atom collection **balanced** if its incidence-balance
vector is zero and every atom stays inside its recorded barrier chamber.

### Proposition 12.4 (local reversible deletion and contact defect)

Deleting a balanced owned collection from a barrier-gap state preserves
all conditions (9.8)--(9.10).  The ordered atom words, owner incidences,
and chamber sides reinsert it uniquely.  Under the canonical rule “delete
the lexicographically first available balanced collection,” every owned
primitive contact has one phase and contributes `K`; a collection of `r`
distinct physical primitives contributes `K^r`, with no factor `2^r`.

In particular:

* a contact adjacent to a consecutive barrier component is forbidden as a
  closed atom or is a one-off downward passage;
* two coordinate incidences using one physical primitive are charged once;
* a free upper/lower choice is split by the incoming chamber side;
* an unbalanced contact which has no later canonical partner is terminal
  boundary/source data, not an iterable transition.

#### Proof

Every deleted primitive is a zero-net subpath, so all later pivot heights
are unchanged.  Deletion removes no pivot and creates no new up-step;
hence the height and corridor conditions remain valid.  For each edge,
the change in the two sides of (9.10) is the corresponding coordinate of
the incidence-balance vector, which is zero.  This proves validity.

The face boundary, side, and owner identify the insertion point.  The
stored word restores the unique atom, and reversing the ordered list
restores the collection.  Lemma 12.2 gives at most one primitive phase in
each incoming state.  Lexicographic ownership prevents a shared physical
word from being charged at another incidence.  These facts give `K^r` and
the four listed alternatives. \(\square\)

The proposition proves a strict defect in the **contact-choice** part of
the kernel: for example, two distinct balanced contacts contribute
`K(1/4)^2=1/4`, not `4K(1/4)^2=1`.  It does not yet bound the generating
series of the bridges between successive contacts, nor prove that the
canonical balanced collection always exists and eventually coalesces the
two pivot diagrams.

### Corollary 12.5 (source ledger remains linear)

Require the deletion to terminate only when the incidence-balance vector
is zero and the second pivot skeleton has coalesced with the anchored
occurrence.  The terminal state then consists of one occurrence plus a
fixed empty chamber/ownership flag, so its total source mass is
`N_(alpha,q)<W` by (9.15), and is less than `W/2` at `q=3`.

Thus the smallest useful quotient does not preload an entire phase word:
it carries one local barrier-side bit during the transfer and has a
one-anchor terminal ledger.  What remains for a full Markov-additive bound
is a global coalescence theorem and control of the inter-contact bridge
series.  The unrestricted critical values in (11.3) are an artifact of
merging the two chamber sides before taking the row sum.

### Lemma 12.6 (incidence pairing isolates the bridge components)

Let `A` be any finite family of physical spatial atoms after every counted
left and right down-step in (9.10) has been assigned to its unique owned
atom.  For an atom `P`, let

\[
                         w(P)\in\mathbb Z^{2q}               \tag{12.8}
\]

record, in each occurrence/edge equation, its number of left count events
minus its number of right count events.  Then

\[
                         \sum_{P\in\mathcal A}w(P)=0.         \tag{12.9}
\]

Pair the positive and negative unit incidences separately in every
coordinate of (12.8), and join the two atoms carrying a paired incidence.
Every connected component `Q` of the resulting atom multigraph is
automatically balanced:

\[
                         \boxed{\sum_{P\in Q}w(P)=0.}         \tag{12.10}
\]

Consequently, if an atom is called a **bridge atom** when it is not a
zero-net closed primitive contained in its recorded chamber, every
component containing no bridge atom is a deletable balanced collection in
the sense of Proposition 12.4.  After all such components are deleted,
the number of remaining atom components is at most the number of bridge
atoms.

#### Proof

Equation (12.9) is exactly the collection of ordinal equalities (9.10),
after physical ownership prevents duplicate counting.  It permits a
bijection between positive and negative unit incidences in each coordinate.
Every matching edge lies wholly inside one connected component.  Hence,
for a fixed coordinate, the positive incidences in a component are paired
bijectively with its negative incidences; summing over coordinates gives
(12.10).

If the component has no bridge atom, all of its atoms are zero-net closed
primitives in their recorded chambers.  Equation (12.10) is precisely the
incidence-balance condition, so Proposition 12.4 deletes it reversibly.
Every remaining component contains at least one bridge atom, and distinct
components contain distinct bridge atoms, proving the last assertion.
\(\square\)

This lemma removes the existence of a balanced contact collection as an
independent obstruction.  All repeated closed-contact mass can be peeled
off componentwise.  The unresolved global estimate is now concentrated
on the bridge atoms: one-way barrier passages, endpoint pieces, and the
words connecting successive closed contacts.  A bound showing that their
owned series has a critical Motzkin (or smaller) marginal would complete
the coalescence step without any additional contact fugacity.

### Lemma 12.7 (irreducible chamber bridges are monotone)

Fix one open face and one barrier chamber.  Let `R` be a pivot-free
subpath lying in that chamber.  If two vertices of `R` have the same
height, the subword between their first such pair is a nonempty zero-net
atom.  If its incidence vector is zero, deleting that subword preserves
(9.8)--(9.10) and is reversibly recorded exactly as in Proposition 12.4.

Consequently, after every chamber-contained zero-net atom of incidence
zero has been deleted, every **incidence-free** residual bridge segment
inside one chamber is strictly monotone.  More generally, every
nonmonotone residual bridge contains a repeated-height subword with
nonzero incidence, and is therefore attached by the pairing graph of
Lemma 12.6 to another count atom or to a boundary/passage component.

#### Proof

Equal endpoint heights make the intervening word zero-net.  It contains no
pivot because it lies in an open face.  Deleting it changes no later raw
height, creates no new step, and removes no forbidden condition.  Its zero
incidence vector says that the two ordinal counts in every equation change
equally.  Thus all inverse conditions remain valid, and storing the word
and its face position gives the inverse insertion.

A nearest-neighbor integer path which is not strictly monotone repeats a
height: at its first reversal it must revisit the preceding level.  If
the resulting zero-net subword has zero incidence it is deletable by the
first paragraph.  Otherwise one of its signed incidences is paired, in
Lemma 12.6, to an opposite incidence outside the subword, placing it in a
nontrivial count/bridge component.  This proves both assertions.
\(\square\)

This does not yet remove one-way passages between different chambers or
prove that the residual pivot skeleton coalesces with the anchor.  It does
show that there is no independent incidence-free bridge series.  Once
zero-net loops are assigned to their balanced atom components, all
remaining nonmonotonic bridge growth is tied to the same signed incidence
graph as the one-way passages.  Bounding those bridge-containing
components, rather than arbitrary bridge words, is the remaining task.

## 13. Signed contact incidence and the residual bridge forest

The existence of balanced closed collections can be made canonical.  Let

\[
                         \mathcal E=\{A,B\}\times\{0,\ldots,q-1\}
                                                                    \tag{13.1}
\]

index the `2q` ordinal equations.  For every count-carrying spatial atom
`Q`, define its signed incidence vector

\[
 \partial_e Q=
 \#\{D_1\text{ contacts of }Q\text{ left of }b_e\}
 -\#\{D_{-2}\text{ contacts of }Q\text{ right of }a_e\},
 \qquad e\in\mathcal E.                                     \tag{13.2}
\]

Here the heights are measured in the edge core belonging to `e`; one
physical down-step may therefore supply half-edges for several equations.
Summing (9.10) over the atomization gives

\[
                              \sum_Q\partial Q=0.             \tag{13.3}
\]

### Lemma 13.1 (canonical signed incidence components are balanced)

At the vertex `Q`, place `|partial_e Q|` signed half-edges labelled `e`,
with the sign of `partial_e Q`.  For each `e`, order its positive and
negative half-edges by spatial position, atom owner, and local occurrence
number, and match the `k`-th positive half-edge to the `k`-th negative
half-edge.  This produces a canonical labelled multigraph `G_contact` on
the physical atoms.  Every connected component `K` satisfies

\[
                              \sum_{Q\in K}\partial Q=0.       \tag{13.4}
\]

#### Proof

Equation (13.3) says that, separately for every label `e`, the two ordered
half-edge lists have the same length, so the matching exists.  Every edge
of a connected component joins one `+e` half-edge to one `-e` half-edge.
All half-edges at a vertex lie in the same component as that vertex.
Summing within a component therefore cancels every matched pair and gives
(13.4). \(\square\)

Call an atom **closed** if it is a zero-net primitive subpath lying in one
recorded barrier chamber.  Put in `P_boundary` every other atom: external
initial/final pieces, nonzero-net bridges, and the one-way passages of
Lemma 12.1.

### Theorem 13.2 (closed-component deletion dichotomy)

Every component of `G_contact` disjoint from `P_boundary` is a balanced
collection deletable by Proposition 12.4.  Delete the lexicographically
first such component and recompute the canonical atomization and incidence
matching.  Iteration terminates, and its terminal diagram has the property

\[
 \boxed{\text{every remaining contact component contains a boundary or
 one-way bridge atom}.}                                     \tag{13.5}
\]

The number of terminal components is at most `|P_boundary|`.  With the
face atomization of Lemma 9.5 one has the coarse deterministic bound

\[
 |P_{\rm boundary}|\le(4q+1)(2q+1)+4q=O(q^2),               \tag{13.6}
\]

because a face has at most `2q+1` barrier chambers.  After its maximal
closed excursions are removed, its residual passage skeleton visits each
chamber at most once: returning through a barrier band is forbidden by
Lemma 12.1.  There are at most `4q+1` faces plus the external endpoint
pieces.

#### Proof

Lemma 13.1 makes a boundary-free component incidence-balanced.  All its
atoms are closed by definition, so Proposition 12.4 deletes it reversibly
and preserves the common-`S` inverse conditions.  Every deletion strictly
shortens the word, proving termination.  At termination a component
disjoint from `P_boundary` would still be eligible, a contradiction;
this proves (13.5).  Distinct remaining components contain distinct
boundary atoms, proving the first bound.  Lemma 12.1 and the face count
give (13.6). \(\square\)

Thus a balanced deletion always exists unless the diagram is already in
the boundary-bridge regime.  No choice of a second occurrence is forgotten:
the ordered pivot skeleton and the labelled incidence matching remain in
the frontier, while the deleted atom words form the reversible shell
record.

The contact incidence theorem does not, by itself, make the residual
bridge kernel strictly subcritical.  The exact scalar alternatives are
already visible from `K(1/4)=1/2`:

\[
 \begin{array}{c|c|c}
 \text{iterable layer}&\text{renewal series}&\text{value at }1/4\\ \hline
 \text{one pinned primitive}&K/(1-K)&1\\
 \text{two pinned primitives}&K^2/(1-K^2)&1/3.
 \end{array}                                                  \tag{13.7}
\]

Every boundary-free component is deleted component-by-component.  A
singleton zero-incidence primitive has one-step weight `K(1/4)=1/2`; its
full stack resolvent `1/(1-K)` is finite at the Catalan point and is a
harmless decoration as long as the whole stack is not promoted to a new
iterable transition.  Components with at least two distinct primitives
have the stronger two-atom defect in the second row of (13.7).  A
component attached to a boundary passage may instead be balanced by that
passage using only one new primitive per bridge layer.  Collapsing an
arbitrary nonempty stack into one bridge transition gives the first row of
(13.7), of critical mass one.

### Proposition 13.3 (incidence balance alone cannot contract bridges)

There are abstract signed bridge components with boundary vectors
`-e_0,+e_r` and closed-atom vectors

\[
                 e_0-e_1,\ e_1-e_2,\ldots,e_{r-1}-e_r.      \tag{13.8}
\]

The whole component is balanced, but no nonempty proper consecutive
subchain is.  If each link admits an arbitrary nonempty stack of pinned
primitive contacts, its link series is `K/(1-K)`, with critical mass one.
Therefore Lemma 13.1 cannot imply a row mass below one, coalescence, or a
non-coboundary Motzkin return bound for the residual bridge transfer.

#### Proof

The vectors in (13.8) telescope with the two boundary vectors.  A proper
consecutive subchain retains a nonzero vector at each exposed end, so it
is not deletable as a balanced closed collection.  Unique phase pinning
gives `K^j` for a stack of `j>=1` primitives; summing over `j` gives the
first row of (13.7). \(\square\)

The example in Proposition 13.3 is an incidence-level obstruction, not a
claim that every such chain is realized by the MSW corridors.  The exact
remaining geometric question is now narrower:

* if every genuine one-atom bridge link is a one-way passage, it is
  source-only and Theorem 13.2 coalesces to the anchored ledger;
* if every iterable bridge link contains two owned primitives, its scalar
  transfer is strictly subcritical by (13.7);
* otherwise the genuine one-atom links form a critical stateful chain and
  their counter increments must be shown to have killed Motzkin or
  non-coboundary localized return mass.

Until this bridge trichotomy is decided from the endpoint skeleton, the
signed incidence construction closes balanced-component existence but
does not prove that every diagram reduces to one anchored skeleton.  It
reduces that global coalescence problem exactly to the `O(q^2)` family of
boundary-connected components in (13.5)--(13.6).

### Lemma 13.4 (raw-height parity separates the two incidence signs)

Let a physical down-step of the common core start at raw height `h`.  In
an edge core with face shift `2 nu`, this step contributes to the left
`D_1` count only if

\[
                         h+2\nu=1,                           \tag{13.9}
\]

and contributes to the right `D_(-2)` count only if

\[
                         h+2\nu=-2.                          \tag{13.10}
\]

Consequently one physical down-step can never carry incidences of both
signs: every left-count step has odd raw height and every right-count step
has even raw height.

#### Proof

Equations (13.9)--(13.10) are just the height translation (9.7) in the
two counts of (9.10).  Their right sides have opposite parity, whereas
`2 nu` is even. \(\square\)

The canonical atomization already cuts immediately before and after every
counted step.  Hence, if the primitive-contact hierarchy assigns each
marked count-step to a separate owned contact (nested contacts being owned
by their innermost marked boundary), every contact incidence vector is
sign-pure.  Under that refinement the abstract relay atom
`e_i-e_j` in Proposition 13.3 is impossible: a boundary-free balanced
component contains at least one positive and one negative contact and
therefore at least two primitive factors.

This gives the prospective critical values

\[
 K(1/4)^2={1\over4}quad\hbox{for a boundary-free component},
 \qquad
 {K(1/4)\over1-K(1/4)^2}={2\over3}                          \tag{13.11}
\]

for a boundary component with one initial contact followed by paired
contacts.  These numbers are strictly below one.  What remains to promote
(13.11) to a theorem is a disjoint nested-contact ownership showing that
an outer primitive never reabsorbs an internally marked count-step.  The
parity lemma proves the sign separation at the physical-step level; it
does not by itself prove multiplicativity of the resulting primitive
series or coalescence of the pivot skeleton.

### Theorem 13.5 (neutral bridge interiors reduce to monotone passages)

Refine the cuts of Lemma 9.5 by retaining, as labelled cuts, every pivot
endpoint, both sides of every step counted in (9.10), every change of
lexicographic owner, and every visit to a level of `B(F)`.  Call a maximal
word between two consecutive labelled cuts a **neutral bridge interval**.
It lies in one face and one barrier chamber and contains no counted step.

If two vertices of a neutral bridge interval have the same raw height,
the word between a closest such pair is a primitive zero-displacement
excursion `P` satisfying

\[
                  \partial P=0.                              \tag{13.15}
\]

It can be deleted reversibly without changing (9.8)--(9.10).  Iterating
the lexicographically first such deletion terminates, and every remaining
neutral bridge interval is either empty or strictly monotone.  In
particular its residual word is forced by its two boundary heights and
has no Catalan or strip-bridge multiplicity.

#### Proof

There is no pivot or count event between the two selected vertices, so
`P` changes no coordinate of (9.10), proving (13.15).  Equal endpoint
heights give zero vertical displacement.  The closest-pair choice implies
that the path stays strictly on one side of its base height until its
return, so `P` is primitive.  It stays in the same chamber (allowing a
labelled chamber boundary only at its two ends), and hence is a balanced
collection covered by Proposition 12.4.

More directly, deleting `P` changes no later raw height, removes no pivot
or counted step, and creates no new up-step.  Thus (9.8), (9.9), and
(9.10) are preserved.  The two neighbouring labelled cuts, the base
height, phase, and stored word identify the reinsertion site; deletion
does not change the spatial order or owner of any surviving marked step.
This proves reversibility even if recomputing the atomization merges the
two adjacent unmarked intervals.

Each deletion shortens the word.  At termination all vertex heights in a
neutral interval are distinct.  A nearest-neighbour word with both an up
and a down step has a direction change, and the heights immediately
before and after that change coincide.  Hence a word with distinct vertex
heights uses only up-steps or only down-steps and is strictly monotone.
Its word and length are then fixed by its endpoint heights. \(\square\)

The cut conditions in Theorem 13.5 are essential.  A repeated-height
subword which straddles a contact/owner cut need not have zero incidence.
For example, an upper primitive carrying a left `D_1` contact has zero
vertical displacement but incidence `+e`; it cannot be deleted until a
matching `-e` incidence is included.  Likewise a word crossing a
forbidden barrier band cannot return across it by Lemma 12.1.  Therefore
the theorem proves monotonicity of the **unmarked inter-contact pieces**,
not of an entire boundary-connected component.

### Corollary 13.6 (bridge normal form)

After the deletions of Theorems 13.2 and 13.4, every residual
boundary-connected component alternates among

1. labelled pivot/contact or owner-cut events;
2. one-way downward barrier passages; and
3. uniquely determined monotone chamber connectors.

Thus no independent Catalan or finite-strip series remains inside an
irreducible connector.  The erased neutral excursions must still be
charged as their own reversible deletion layers, and the marked contact
events can still form the critical chain of Proposition 13.3.  The
remaining questions are consequently pivot-skeleton coalescence and the
Motzkin/non-coboundary control of that marked stateful transfer; loop
erasure alone does not make its row mass strictly smaller than one.

### Lemma 13.7 (count-refined contact layers are sign-pure)

Let `x` be a physical down-step of `S`, with raw starting height `h`, and
refine the atomization by cutting immediately before and after `x` whenever
it is counted in at least one equation (9.10).  Its positive and negative
label sets are exactly

\[
\begin{split}
 P(x)=\{e=(\epsilon,t):{}&x<b_e,\ x\notin L_e,\
                         \nu_e(x)=(1-h)/2\},\\
 N(x)=\{e=(\epsilon,t):{}&x>a_e,\ x\notin L_e,\
                         \nu_e(x)=(-2-h)/2\}.
\end{split}                                                   \tag{13.16}
\]

At most one of `P(x),N(x)` is nonempty.  Consequently the incidence
vector carried by one count-refined contact layer is of one of the forms

\[
             \sum_{e\in P(x)}e
       \qquad\hbox{or}\qquad
            -\sum_{e\in N(x)}e,                              \tag{13.17}
\]

and all equation labels served by that layer have the same value of
`nu`.  In particular, a genuine single contact layer never has incidence
`e-e'`, for any two labels `e,e'`.

#### Proof

The two alternatives in (9.10), written at raw height `h`, are

\[
                  h+2\nu_e(x)=1,
       \qquad     h+2\nu_e(x)=-2.                            \tag{13.18}
\]

They give (13.16).  The first equality requires `h` odd and the second
requires `h` even, so the same physical step cannot satisfy both.  For a
fixed sign, (13.18) also determines `nu_e(x)` uniquely, proving the last
assertion. \(\square\)

The refinement is compatible with nesting.  If a primitive word contains
another counted down-step in its interior, expose the interior marked
step first and retain the two labelled cuts in the frontier.  Recursing
leaves layers with one distinguished counted step.  Lemma 12.2 pins its
upper/lower phase, and its allowed word class is a subclass of the
primitive class counted by `K`.  If the same marked step serves several
labels in (13.16), all those coordinates remain on the one vector
(13.17), while lexicographic ownership charges its physical word only
once.  Thus internal marked steps produce nested, separately recorded
layers; they do not turn an outer layer into a mixed-sign atom.

### Corollary 13.8 (the abstract critical relay is not genuine)

Every nonempty boundary-free contact renewal which returns to the same
incidence state contains at least two count-refined primitive layers, one
of each sign.  Its one-step series is therefore at most `K^2`.  A
boundary-attached stack may start with one sign-pure seed, but every
further renewal again costs at least `K^2`; hence its scalar series is

\[
 {K(u)\over1-K(u)^2},\qquad
 {K(1/4)\over1-K(1/4)^2}={2\over3}<1.                       \tag{13.19}
\]

A component containing only one nonzero contact layer cannot be a closed
iterable renewal.  Its unmatched sign is carried by an external endpoint
piece or by a one-way barrier passage, and it is boundary/source data.
Thus the vectors in (13.8) cannot be realized by single primitive layers:
the last scalar-critical `K/(1-K)` alternative disappears after
count-refinement.

This statement does not identify `nu` with the pivot counter.  Labels
sharing one physical step have `Delta nu=0` and the same sign.  Matching
opposite signs for a fixed equation uses two different steps
`x_L<b_t<a_t<x_R`, for which

\[
 \nu_t(x_R)-\nu_t(x_L)
       =|L_t\cap[x_L,x_R)|                                  \tag{13.20}
\]

can exceed one.  The nearest-neighbour increments `-1,0,+1` belong
instead to the adjacent pivot counters `k_(t+1)-k_t` of the one-ladder
order table.  After (13.19), that pivot-skeleton coalescence/Motzkin
transfer—not a one-atom contact relay—is the remaining critical problem.

## 14. Exact terminal pivot skeleton and its Motzkin deletion

First consider the coalesced minimal core

\[
                              S_q=0^{2q}.                    \tag{14.1}
\]

A depth-`q` occurrence over (14.1) is one complete MSW column.  Its first
balanced state is a Dyck path `x` of semilength `q`.  If the successive
common-core pivot intervals are `(b_t,a_t)`, put

\[
                  \pi(x)=(a_0,b_0,a_1,b_1,\ldots,
                           a_{q-1},b_{q-1}).                 \tag{14.2}
\]

This is the MSW flip-position permutation (the `g` position precedes the
`h` position).  For the canonical first-return decomposition
`x=U u D v`, and with `theta(u)` denoting reverse-complement, the exact
MSW flip recursion is

\[
 \pi(x)=\bigl(|u|+2,\ |u|+2-\pi(\theta u),\ 1,\
                    |u|+2+\pi(v)\bigr).                    \tag{14.3}
\]

The operations on a sequence in (14.3) are entrywise.  Formula (14.3)
also proves directly that `pi(x)` is a permutation and that every pair in
(14.2) satisfies `b_t<a_t`.

For two successive intervals attach the letter

\[
\begin{array}{c|c|c}
\text{letter}&\text{endpoint order}&k_{t+1}-k_t\\ \hline
F&b_t<a_t<b_{t+1}<a_{t+1}&0\\
+&b_t<b_{t+1}<a_{t+1}<a_t&+1\\
-&b_{t+1}<b_t<a_t<a_{t+1}&-1\\
C&b_{t+1}<b_t<a_{t+1}<a_t&0.
\end{array}                                                  \tag{14.4}
\]

Write `Phi(x)` for the resulting word of length `q-1`.  A word in
`{F,C,+,-}` is a **two-colour Motzkin excursion** if `+,-` have increments
`+1,-1`, both `F,C` have increment zero, and its partial sums are
nonnegative and end at zero.

### Theorem 14.1 (the terminal MSW skeleton is exactly two-colour Motzkin)

The map

\[
 \boxed{\Phi:\{\text{Dyck paths of semilength }q\}
       \longrightarrow
       \{\text{two-colour Motzkin excursions of length }q-1\}}
                                                               \tag{14.5}
\]

is a bijection.  Along the image word, its Motzkin height at time `t` is
the exact pivot counter `k_t`.  Thus `k_0=k_(q-1)=0`, and deleting a
letter `-` at height zero is genuinely forbidden rather than reassigned.

#### Proof

Define an auxiliary word

\[
                              \Psi(u):=\Phi(UuD).             \tag{14.6}
\]

Substitution of (14.3) into the four comparisons (14.4) gives the two
mutual recursions below.  If `x=UuDv`, then

\[
 \Phi(x)=
 \begin{cases}
   \Psi(u),&v=\varnothing,\\
   \Psi(u)\,F\,\Phi(v),&v\ne\varnothing.
 \end{cases}                                                  \tag{14.7}
\]

If `u=UrDs`, then

\[
 \Psi(u)=
 \begin{cases}
   \Psi(s)\,C,&r=\varnothing,\\
   \Psi(s)\,+\,\Phi(r)\,-,&r\ne\varnothing.
 \end{cases}                                                  \tag{14.8}
\]

Here `Phi(empty)=Psi(empty)=empty`.  For completeness, the separation in
(14.7) follows because all entries belonging to `u` lie below `|u|+2`,
whereas every entry belonging to the nonempty suffix `v` lies above it;
the intervening adjacent intervals therefore have order `F`.  Applying
(14.3) once more to `u=UrDs` gives respectively the crossing order `C`
or the outer orders `+,-` in (14.8); the entries of `s` occur first because
the `u` block in (14.3) is reverse-complemented.  All internal comparisons
are exactly those defining `Psi(s)` and `Phi(r)`.

Let `M_n` be the two-colour Motzkin excursions of length `n`, and let
`R_n` be those having no `F` step at height zero.  Recursion (14.8) is a
bijection from Dyck paths of semilength `n` to `R_n`: every nonempty
ground-level component of a word in `R_n` ends uniquely either in a
single `C`, or in `+ M -` with `M` a two-colour Motzkin excursion.  Reading
the last component recovers `r` and the preceding word recovers `s`.

Recursion (14.7) is then a bijection to `M_(q-1)`.  Indeed, the first
ground-level `F`, if present, uniquely separates `Psi(u)` from `Phi(v)`;
if it is absent then `v` is empty.  This also gives the inverse map and
proves (14.5).

Finally, the increments in (14.4) are the exact order table for the
ordinal counters.  At the first edge of a complete column the ordinal
index is zero, so `k_0=0`.  Since `Phi(x)` is an excursion, its partial
sums and `(k_t)` have the same initial value and increments, hence agree
at every `t`. \(\square\)

### Corollary 14.2 (canonical adjacent-cell deletion)

The inverse proof of Theorem 14.1 is a reconstructive deletion of the
terminal endpoint diagram:

1. every `F` at Motzkin height zero is a regeneration cut;
2. inside a block with no such `F`, read its last ground-level component;
3. a terminal `C` deletes one flat crossing cell;
4. a terminal `+ M -` deletes the matched outer pair and recursively
   processes the enclosed word `M`.

Equivalently, the word may be read sequentially while retaining its
nonnegative height and the usual nesting stack.  The terminal source is
empty plus the fixed endpoint convention; no second arbitrary endpoint
diagram is stored.  Hence, after physical pivot supports have coalesced,
the pure endpoint skeleton has exactly the killed-Motzkin support needed
by Theorem 2.2.  The critical letters are `-,C,+`; `F` is a regeneration
separator.

The theorem is a support and reconstruction statement, not yet the
weighted marginal.  To finish that marginal one must attach the owned
common-`S` shell to each decoded cell and prove the row bounds

\[
             H_-(1/4)\le {3\over8},\qquad
             H_C(1/4)\le {1\over4},\qquad
             H_+(1/4)\le {3\over8},                          \tag{14.9}
\]

with every `F` decoration having a uniformly summable resolvent.  The
sign-pure theorem controls the contact part of these entries, but does not
by itself identify the complete cell shell.

### Proposition 14.3 (the remaining obstruction is physical support coalescence)

For a subladder on temporal indices `r,...,s`, the common core of one
occurrence `epsilon` is

\[
 S_{r,s}^\epsilon
   =S+\{a_j^\epsilon:j<r\}
      +\{b_j^\epsilon:j\ge s\}.                             \tag{14.10}
\]

Thus independently deleting the left or right adjacent cell of two
colliding occurrences does not preserve a common core unless the newly
exposed pivot sets in (14.10) coincide physically.  Standardizing the
`2q` endpoints of the second occurrence and applying `Phi` forgets exactly
this identification data.

#### Proof

Intersect the states (9.11) for `r<=t<=s`.  A pivot with index below `r`
is present as `a_j` in every state, and a pivot with index at least `s` is
present as `b_j` in every state; every other pivot is absent from at least
one state.  This gives (14.10).  Applying the formula to `A` and `B`
proves the assertion. \(\square\)

Consequently Theorem 14.1 completely solves the **coalesced minimal
skeleton**, but it does not prove that the contact/bridge deletions force
the two physical pivot supports to coalesce.  Once that support theorem
and the weighted bounds (14.9) are supplied, Corollary 14.2 gives the
desired killed-Motzkin deletion with a one-anchor source.  Without it,
retaining the second embedded endpoint diagram in the terminal state is
again the circular pair ledger of Lemma 9.3.

### Corollary 14.4 (every intrinsic ladder is a Motzkin window)

Let `x` be the Dyck root of a full MSW column of semilength `m`, and index
the pairs in its flip permutation as

\[
 \pi(x)=(a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1}).           \tag{14.11}
\]

The intrinsic occurrence `alpha_q(x,i)` of (13.1),
`0<=i<=m-q`, has local pivot pairs

\[
            (b_i,a_i),(b_{i+1},a_{i+1}),\ldots,
                       (b_{i+q-1},a_{i+q-1}).               \tag{14.12}
\]

Consequently its adjacent order word is the contiguous substring

\[
                  \Phi(x)[i,i+q-1)                          \tag{14.13}
\]

of length `q-1` (the right endpoint in (14.13) is excluded).  If `h_j` is
the height of the global two-colour Motzkin excursion `Phi(x)` before its
`j`-th letter, then the occurrence counters satisfy

\[
                   k_t-k_0=h_{i+t}-h_i,qquad0\le t<q.      \tag{14.14}
\]

After subtracting the minimum of the window and reading its two halves
away from the first minimum, (14.13) is therefore two killed Motzkin
paths.  The anchored-window source count is exactly

\[
                  (m-q+1)\operatorname{Cat}_m<W.            \tag{14.15}
\]

#### Proof

The full column flips the two positions in the `j`-th pair of (14.11) on
its `j`-th edge.  Formula (13.6) says that `alpha_q(x,i)` is precisely the
subchain of edges `i,...,i+q-1`, proving (14.12)--(14.13).  The increments
of both sides of (14.14) are the same four-case order increments in
(14.4), so their difference is constant; it vanishes at `t=0`.  Minimum
rooting proves the killed support, and counting the `m-q+1` windows in
each of the `Cat_m` roots gives (14.15). \(\square\)

Thus the `Phi/Psi` bijection is not merely a terminal-size phenomenon:
it is an exact global cross-depth code for every intrinsic ladder.  What
is absent from the code is the equality of the target cuts produced by
two different rooted windows; that equality is exactly the spatial
selector problem of Section 15.

## 15. Virtual-core erasure of the second pivot support

Literal coincidence of the two pivot supports is not needed for an
`O(W)` terminal ledger.  The second support can be moved entirely into the
typed shell record while the anchor and its physical common core remain
fixed.

For occurrence `B`, write its balanced states as

\[
 Y_t^B=S+\{a_j^B:j<t\}+\{b_j^B:j\ge t\},
                    \qquad 0\le t\le q.                    \tag{15.1}
\]

For `0<=r<s<=q`, the contiguous subladder with edges
`r,r+1,...,s-1` has virtual common core

\[
 C_{r,s}^B
   =S+\{a_j^B:j<r\}+\{b_j^B:j\ge s\}.                      \tag{15.2}
\]

In particular,

\[
 C_{r+1,s}^B=C_{r,s}^B+\{a_r^B\},\qquad
 C_{r,s-1}^B=C_{r,s}^B+\{b_{s-1}^B\}.                     \tag{15.3}
\]

The plus signs in (15.2)--(15.3) are virtual flips inside the `B` record;
they do not modify `S` or the anchored occurrence `A`.

### Theorem 15.1 (canonical support erasure has a one-anchor source)

Let `t_*` be the first global minimum of the anchor counter
`(k_t^A)_(0<=t<q)`.  There is a canonical reversible erasure of all pivot
labels of `B` with the following form.

1. Start from the full virtual interval `[r,s]=[0,q]`.
2. While `r<t_*`, record the typed left boundary edge
   `(b_r^B,a_r^B)`, its physical owner pointers and adjacent atom address,
   and replace `r` by `r+1` using the first identity in (15.3).
3. While `s>t_*+1`, record the typed right boundary edge
   `(b_(s-1)^B,a_(s-1)^B)` and the same ownership data, and replace `s`
   by `s-1` using the second identity in (15.3).
4. Record the remaining edge `(b_(t_*)^B,a_(t_*)^B)` as the central
   boundary seed and erase the residual `B` label.

The order “all left boundaries, then all right boundaries” fixes the
canonical convention; any fixed interleaving determined by `A` would give
the same conclusion.  Reversing the typed list reconstructs the original
embedded occurrence `B` uniquely.  The terminal state is precisely the
single anchored occurrence `A`, so its source mass is

\[
                 (m-q+1)\operatorname{Cat}_m<W.             \tag{15.4}
\]

#### Proof

Formula (15.2) is obtained by intersecting the states `Y_r^B,...,Y_s^B`.
It proves (15.3), and also proves that every residual object in steps 2--3
is a genuine contiguous MSW subladder.  The physical path `S` and every
condition belonging to `A` are untouched.

Every noncentral pivot pair is recorded exactly once.  At termination the
virtual core is

\[
 C_{t_*,t_*+1}^B
 =S+\{a_j^B:j<t_*\}+\{b_j^B:j>t_*\},
\]

which is the edge core of the recorded central pair.  Hence the complete
list contains all `2q` endpoints of `B`, their temporal indices, their
physical equality/owner type relative to `A`, and their insertion
addresses.  Starting with `S`, the list first reconstructs the central
edge core and pair, and the inverse operations in (15.3) then restore the
left and right edges in reverse deletion order.  This gives all states in
(15.1), so reconstruction is unique.

No datum belonging only to `B` remains in the terminal state.  The index
`t_*` is determined by `A`, rather than chosen as an additional source
flag.  Corollary 9.7 therefore gives (15.4). \(\square\)

If an endpoint of `B` is also an endpoint of `A`, the record carries an
owner pointer and does not charge its physical word twice.  If it is
`B`-only, the record carries the endpoint mark and its address.  Thus the
theorem erases arbitrary `B`-only support; it does not assume the physical
support-coincidence condition excluded by Proposition 14.3.

### Corollary 15.2 (the erasure order has killed-Motzkin support)

Insert the recorded edges away from `t_*`.  On the right half the anchor
height is

\[
                         k_t^A-k_{t_*}^A\qquad(t\ge t_*),
\]

and its successive increments are the letters of (14.4).  On the left
half, read indices downward; the height is the same difference and the
increment is `-(k_(t+1)^A-k_t^A)`, so `+` and `-` are interchanged while
`C,F` remain flat.  Both halves start at zero and never become negative.
Therefore, after `F` cells are separated as regeneration decorations, the
pure support of the two insertion lists is two killed Motzkin walks rooted
at the boundary.

Theorem 15.1 closes the **source/coalescence ledger**, but deliberately
does not assign a weight to an absolute pivot address.  The remaining
load-bearing assertion is the following row estimate for the owned record
kernel `Q`.  For every incoming anchored/frontier state and
`a in {-,C,+}` one needs

\[
 \boxed{
   \sum_{b,\omega'}Q_{a,b}^{\omega,\omega'}(u)
      \preceq H_a(u),\qquad
   H_-=H_+=L_2K^2,\quad H_C=K^2.}                           \tag{15.5}
\]

The parity theorem and Corollary 13.8 make every contact renewal in this
record strictly subcritical, and Theorem 13.5 removes independent
incidence-free bridge multiplicity.  What is not yet proved is that the
endpoint-address part of one boundary-edge record introduces no additional
iterable strip factor.  Proving (15.5), together with a summable `F`
resolvent, would combine Theorem 15.1 with Theorem 2.2 and complete the
`O(sqrt(q)W)` collision transfer.

### Definition 15.3 (the reduced local row table)

Perform the deletions of Theorems 13.2 and 13.4 before one step of the
virtual erasure, and do not collapse a nonempty stack of balanced contacts
into that step.  A **reduced local type** records only:

1. the ordered equality type of the at most eight endpoints in the active
   adjacent cells of `A` and `B`;
2. the two letters in `{F,C,+,-}` and the left/right orientation of the
   erasure;
3. the owner partition of their distinguished counted steps, together
   with the common sign on each physical owner block;
4. the pinned upper/lower phase and chamber side at each owned contact;
5. whether the unique offset connector is owned by `A`, by `B`, or is
   physically shared; and
6. whether the record is iterable or is the final boundary seed.

After vertical translation, this is a finite set `T`.  The complete remote
incidence sets, absolute equation labels, and values of `nu` remain in the
hidden frontier rather than in `T`.  Lemma 13.7 forces equal `nu` and one
common sign on all coordinates sharing one step, Lemma 12.2 reduces every
gateway decision to a phase/side bit, and a connector crossing any further
barrier is one-way rather than iterable.  These facts make the **word type**
finite; they do not make the number of spatial embeddings of that type
finite.

For a fixed incoming frontier `omega`, anchor letter `a`, and
`tau in T`, let `I_(omega,tau)` be the set of compatible physical
embeddings/next states of type `tau`.  Write
`G_(omega,tau,iota)(u)` for the generating function of the newly owned
words in embedding `iota`.

### Proposition 15.4 (a finite type table does not control row multiplicity)

The exact remaining selector-series inequality is

\[
 \boxed{
       \sum_{\tau\in T}
       \sum_{\iota\in I_{\omega,\tau}}
             G_{\omega,\tau,\iota}(u)
           \preceq
       \begin{cases}
          L_2(u)K(u)^2,&a\in\{-,+\},\\
          K(u)^2,&a=C,
       \end{cases}}                                         \tag{15.6}
\]

and the analogous summable statement for `F`.  It cannot be replaced by
a sum containing one copy of each compatible local type.

#### Proof

Use the repeated guarded-block construction of Lemma 7.1.  Fix the common
core and the anchored occurrence `A`, and place `N` identical guarded
blocks, each supporting a distinct compatible occurrence `B_i` with the
same prescribed local letter and the same reduced phase/owner type.  The
virtual erasure of Theorem 15.1 sends every `(A,B_i)` to the same source
`A`.  In reverse, the first central-seed insertion has `N` distinct
spatial embeddings of one local type.  With the common wrapper of Lemma
7.2 their row contribution is

\[
                                N K(u)^2,                    \tag{15.7}
\]

exactly as in Corollary 7.3.  Already `N=2` exceeds every proposed
one-coordinate cell budget at the leading coefficient.  Therefore remote
data can create multiplicity within one member of `T`; it is not merely a
zero-one compatibility restriction.  Summing over embeddings gives
(15.6), and summing over types only does not. \(\square\)

Consequently Theorem 15.1 proves an injective `O(W)`-source **code**, but
does not by itself orient that code as a substochastic insertion kernel.
One of the following additional mechanisms is necessary:

1. a spatial selector kernel whose generating series pays the sum over
   `I_(omega,tau)` in (15.6);
2. an ownership pointer retained until its embedding has been paid, with
   an independently proved `O(W)` source ledger; or
3. a signed centering/quarantine theorem which removes the repeated
   disjoint-block embeddings as balanced baseline mass before the
   nonnegative Motzkin transfer begins.

Conditional on such a selector, the finite word table is favorable.  A
nonboundary iterable type has at least one positive and one negative
primitive factor, so it contains `K^2`; any additional primitive only
decreases the coefficientwise bound because

\[
                  K^r-K^{r+1}=uK^{r-1}\succeq0.             \tag{15.8}
\]

There is no second independent strip factor in an irreducible connector
by Theorem 13.5.  Thus an offset row has at most its one allowed `L_2`
factor.  After spatial embeddings have been controlled, the remaining
finite check is the sum over maximally shared owner types: alternatives
pointing to the same two `A`-owned primitives must be mutually exclusive,
share the offset connector, or form one subcritical paired renewal.  The
selector-series bound, not the finite table alone, is now the exact gate.

## 16. Centering does not remove the spatial selector multiplicity

Let

\[
 N_q=\binom{2m+1}{m-q},\qquad
 \lambda_q={W\over N_q}=c_q+\theta_q,
 \quad c_q=\lfloor\lambda_q\rfloor,quad0\le\theta_q<1.     \tag{16.1}
\]

For any integer target-load vector `mu` with total mass `W`, put

\[
 \mathcal F_q(\mu)
   =\sum_S(\mu(S)-c_q)(\mu(S)-c_q-1).                       \tag{16.2}
\]

### Lemma 16.1 (exact floor-correct centering identity)

One has

\[
 \boxed{
 \sum_S(\mu(S)-\lambda_q)^2
   =\mathcal F_q(\mu)+N_q\theta_q(1-\theta_q).}             \tag{16.3}
\]

The first term on the right is a nonnegative integer.  For `c_q=1`, its
contribution at a target of load `d` is

\[
                  (d-1)(d-2)=2\binom{d-1}{2}.               \tag{16.4}
\]

#### Proof

Expand (16.2), use `sum_S mu(S)=W=lambda_q N_q`, and subtract it from the
left side of (16.3).  The difference per `N_q` is

\[
 (2c_q+1)\lambda_q-c_q(c_q+1)-\lambda_q^2
       =\theta_q(1-\theta_q).
\]

Since `(z-c_q)(z-c_q-1)>=0` for every integer `z`, the remaining
assertions follow. \(\square\)

### Proposition 16.2 (guarded repeated blocks survive centering)

The repeated-block family of Lemma 7.1 can give one target `S` a fibre of
size `d` tending to infinity while all selected occurrences have the same
reduced first insertion type.  Removing a balanced floor/ceiling baseline
can designate at most `c_q+1` occurrences at that target.  At least

\[
                              d-c_q-1                       \tag{16.5}
\]

spatial embeddings remain, and the floor-correct excess at that target is

\[
                         (d-c_q)(d-c_q-1).                  \tag{16.6}
\]

In particular, for fixed `q` and growing `m`, one has `c_q=1`, so both
(16.5) and (16.6) are unbounded.  The multiplicity in Proposition 15.4 is
therefore centered excess, not purely independent/balanced baseline mass.

#### Proof

A floor/ceiling-balanced profile has load `c_q` or `c_q+1` at every
target, proving (16.5).  Formula (16.6) is the corresponding summand of
(16.2).  For fixed `q`,
`lambda_q=W/N_q=1+O(q^2/m)`, hence `c_q=1` for all sufficiently large
`m`.  The guarded blocks make `d` grow with the number of blocks while
preserving the common target and local insertion type. \(\square\)

Thus the scalar subtraction
`2P_q-(lambda_q-1)W` has no interpretation as a local injection canceling
all repeated embeddings.  The floor-correct version (16.2) is the closest
nonnegative combinatorial centering, and it still retains the repeated
fibre.  Pairing a spike against deficits at other targets would require a
signed global transport, not the nonnegative local Motzkin kernel of
Theorem 2.2.  Consequently baseline centering cannot replace the spatial
selector series in (15.6).

## 17. The exact zero-window selector in the MSW flip permutation

The embedding multiplicity has a direct description that does not mention
the local contact parsing.  For a Dyck root `x`, retain the full flip
permutation

\[
               \pi(x)=(a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1}).
                                                               \tag{17.1}
\]

### Lemma 17.1 (target equality is a one-zero-window mask)

For `0<=i<=m-q`, the intrinsic target of the window
`alpha_q(x,i)` is

\[
                S(x,i,q)=\{a_j:j<i\}\cup
                          \{b_j:j\ge i+q\}.                 \tag{17.2}
\]

Equivalently, mark an entry of `pi(x)` by `1` when it belongs to `S` and
by `0` otherwise.  Pairing the marks according to (17.1) gives exactly

\[
              (10)^i\,(00)^q\,(01)^{m-i-q}.                \tag{17.3}
\]

Consequently a collision fibre over a fixed target `S` is precisely the
set of rooted windows `(x,i)` whose recursive MSW permutation realizes
the mask (17.3) with `1`-set `S`.

#### Proof

Formula (17.2) is (13.1), with the full-column `A,B` sequences identified
with the odd/even entries of (17.1).  Before the window, (17.2) selects
`a_j` and not `b_j`; inside it selects neither; after it selects `b_j` and
not `a_j`.  This is (17.3), and every implication is reversible.
\(\square\)

Thus the `2q` pivot endpoints of an occurrence are literally the entries
in the zero window of (17.3).  The `B`-only pivot support in a collision is
the part of the second zero window not already in the first.

### Lemma 17.2 (the zero window has a two-branch recursive frontier)

Build the canonical first-return decomposition tree of `x`.  The positions
of every Dyck subpath form one consecutive interval in `pi(x)`.  At every
level of this tree, the zero window in (17.3) partially intersects at most
two subpath intervals; every other subpath interval at that level is
wholly before the window, wholly inside it, or wholly after it.

#### Proof

For `x=UuDv`, recursion (14.3) lists the first root boundary position,
then one consecutive block containing exactly the positions of `u` (in
reverse-complement order), then the other root boundary position, and then
one consecutive block containing exactly the positions of `v`.  Applying
the same recursion inside either child gives the interval property for
every descendant subpath.  At a fixed level these intervals are disjoint
and ordered.  A single interval—the zero window—can partially meet only
the interval containing its left boundary and the interval containing its
right boundary. \(\square\)

The side of the window and the parity of the next selected entry determine
whether a completed recursive block must realize the `10` or `01` mask.
Reverse-complementing a child only swaps the two finite orientation bits.
Hence the selector admits a recursive state with two active boundary
branches plus completed left/right blocks; it does not require the full
set of `2q` pivot endpoints in its active frontier.

This is a structural bounded-frontier theorem, not yet a generating
function estimate.  Completed blocks can occur in arbitrarily many
spatial locations, as the guarded construction shows.  The remaining
selector task can now be stated without reference to the collision pair:

> Bound the total Catalan generating series of recursive flip permutations
> realizing the prescribed mask (17.3), conditional on one anchored
> realization, by a kernel whose active two-boundary marginal is summable
> (or killed Motzkin) uniformly in the window length.

A proof would pay the embedding sum in (15.6).  Merely counting the finite
two-boundary states does not: the completed recursive blocks carry the
unbounded multiplicity exposed by Proposition 15.4.

## 18. An invisible Catalan block disproves the square-root selector bound

The two-boundary formulation also exposes a stronger obstruction.  A
recursive block which is wholly contained in the zero window is not merely
a finite-state side bush: its entire Catalan shape is invisible to the
target.  The resulting multiplicity is exponentially larger than the
proposed `O(sqrt(q))` selector bound.

Define the **permutation recursion tree** `T(x)` by

\[
 T(UuDv)=\bigl(T(\theta u),T(v)\bigr),                       \tag{18.1}
\]

where `theta` is reverse-complement.  This is an ordinary ordered binary
tree with `m` internal nodes, and every such tree occurs exactly once.
Call a node **aligned** if its block in `pi(x)` starts in an odd-numbered
position, so that the block is a union of adjacent pairs in (17.1).

### Lemma 18.1 (aligned subtrees are target-invisible)

Let an aligned node of `T(x)` have subtree size `q`.  Delete this subtree
but retain the resulting ordered-tree context and the size `q` of its
hole.  Filling the hole by any of the `Cat_q` ordered binary trees gives a
rooted intrinsic window `(x',i)` with one and the same target
`S(x',i,q)`.

#### Proof

In (14.3), relative to the start of the parent block, the first recursive
child occupies positions `2,...,2|u|+1`, while the second child starts in
position `2|u|+3`.  Thus passage to a first child adds the odd offset one
and toggles the parity of the block's starting position; passage to a
second child adds the even offset `2|u|+2` and preserves it.  The
reverse-complement operation causes no extra parity change: the affine
map `j mapsto |u|+2-j` changes physical coordinate values, not their
positions in `pi`, and the child is recursively defined to be
`T(theta u)`.  This proves the parity rule at every recursion depth.
Every recursive subtree occupies one consecutive block by Lemma 17.2.
An aligned subtree of size `q` therefore occupies exactly `q` whole
adjacent pairs, say pair indices `i,...,i+q-1`.

The affine translations and reflections which place this block in the
global permutation depend only on the ancestor context and on subtree
sizes.  Induction in (14.3) therefore shows that replacing the subtree by
another tree of the same size permutes only the same `2q` physical
coordinates inside the block; every physical coordinate entry outside it
is exactly unchanged.  Put the zero window of (17.3) on those `q` pairs.
Formula (17.2) selects only odd entries before the block and even entries
after it, and selects no entry inside it.  Thus the selected physical set
`S` itself—not merely its cardinality or order type—is independent of the
filling. \(\square\)

The aligned contexts can be counted exactly.  Let

\[
 C(z)=1+zC(z)^2,
 \qquad R(z)=zC(z).
\]

At every ancestor of the hole one chooses whether the distinguished child
is first or second and chooses the other child arbitrarily.  Either choice
has series `R`; the first-child choice toggles alignment.  Hence the series
of contexts with an even number of toggles is

\[
 E(z)={1\over2}\left({1\over1-2R(z)}+1\right)
     ={1\over2}\left({1\over\sqrt{1-4z}}+1\right).           \tag{18.2}
\]

Consequently, for `m>q`, the number of size-`m` contexts with an aligned
hole of size `q` is

\[
 H_{m,q}=[z^{m-q}]E(z)
        ={1\over2}\binom{2(m-q)}{m-q}.                       \tag{18.3}
\]

### Theorem 18.2 (exponential intrinsic collision lower bound)

Let `mu^alpha_(m,q)(S)` count the intrinsic windows (17.2), and put

\[
 P^\alpha_{m,q}
   =\sum_S\mu^\alpha_{m,q}(S)
             \bigl(\mu^\alpha_{m,q}(S)-1\bigr).
\]

Then

\[
 \boxed{
 P^\alpha_{m,q}\ \ge\
 {1\over2}\binom{2(m-q)}{m-q}
       \operatorname{Cat}_q(\operatorname{Cat}_q-1).}       \tag{18.4}
\]

In particular, with the original odd-wreath normalization

\[
 W=\binom{2m+1}{m}={2m+1\over m+1}\binom{2m}{m},
\]

for fixed `q` and `m` tending to infinity,

\[
 \liminf_{m\to\infty}{P^\alpha_{m,q}\over W}
 \ge {\operatorname{Cat}_q(\operatorname{Cat}_q-1)\over
           4\,4^q}
 \sim {4^q\over4\pi q^3}.                                  \tag{18.5}
\]

The same lower-bound asymptotic holds along every diagonal on which
`q -> infinity` and `q^2/m -> 0`.

#### Proof

Each one of the `H_(m,q)` contexts in (18.3) gives, by Lemma 18.1, a
fibre of `d=Cat_q` distinct rooted windows.  A rooted window determines
its zero interval in `pi`.  Recursive blocks are nested or disjoint, so
there is a unique size-`q` node having that interval; deleting it recovers
the unique context.  Hence the rooted-window groups belonging to distinct
contexts are disjoint.  In particular, their within-group ordered pairs
cannot be counted twice.  Different groups may nevertheless have the
same target, but merging such groups only adds cross-pairs and increases
ordered collision count, since

\[
                  (hd)(hd-1)\ge h d(d-1)\qquad(h\ge1).
\]

This proves (18.4).  Moreover

\[
 {\binom{2(m-q)}{m-q}\over W}
       \longrightarrow {1\over2}4^{-q},
\]

and `Cat_q ~ 4^q/(sqrt(pi)q^(3/2))`, proving (18.5).  More
precisely, the displayed ratio is
`(1/2)4^(-q) exp(O(q^2/m+1/m))`, which also proves the diagonal
assertion. \(\square\)

There is also a pointwise form: every anchored occurrence whose zero
window is an aligned recursive subtree has at least `Cat_q-1` compatible
second occurrences obtained by changing only that subtree.  Thus the
failure is not caused by averaging over spatial locations.

### Corollary 18.3 (floor centering does not restore `O(sqrt(q)W)`)

Let `mu_q` be the full canonical MSW depth-`q` load, which contains the
intrinsic windows above, and use the original target count

\[
 N_q=\binom{2m+1}{m-q},\qquad
 c_q=\left\lfloor{W\over N_q}\right\rfloor.
\]

Write its floor-correct energy as

\[
 \Phi_q:=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)
        =\mathcal F_q(\mu_q).
\]

If `c_q=1` and `q>=3`, then

\[
 \boxed{
 \Phi_q\ \ge\
 {1\over2}\binom{2(m-q)}{m-q}
   (\operatorname{Cat}_q-1)(\operatorname{Cat}_q-2).}       \tag{18.6}
\]

By Lemma 16.1 the ordinary centered quadratic energy is even larger:

\[
       \|\mu_q-(W/N_q)\mathbf1\|_2^2
       =\Phi_q+N_q\theta_q(1-\theta_q)\ge\Phi_q.            \tag{18.7}
\]

Hence no absolute estimate `Phi_q=O(sqrt(q)W)` is possible, even
in the shallow regime `q^2/m -> 0` where `c_q=1`.

#### Proof

If `h` aligned contexts merge at one target, the intrinsic load there is
at least `h d`, with `d=Cat_q`.  For `d>=3`,

\[
 (hd-1)(hd-2)\ge h(d-1)(d-2).
\]

The full load is no smaller and `z mapsto (z-1)(z-2)` is increasing for
integer `z>=2`, so summing over targets and using (18.3) proves (18.6).
Finally

\[
 {W\over N_q}=\prod_{r=0}^{q-1}{m+r+2\over m-r}
              =\exp\bigl(O(q^2/m)\bigr),
\]

and this ratio is strictly larger than one.  Thus it lies in `(1,2)` and
has floor one when `q^2/m` is sufficiently small.  Dividing (18.6) by
`W` and applying (18.5) gives growth asymptotic to
`4^q/(4 pi q^3)`, which dominates every constant times `sqrt(q)`.
For example, the diagonal `m=q^4` lies in the advertised shallow regime,
has `c_q=1` for all sufficiently large `q`, and makes this contradiction
explicit.
\(\square\)

### Corollary 18.4 (the unshifted canonical factor fails MWB in `L1`)

Assume `c_q=1`, and write the high-side linear overload as

\[
 U_q:=\sum_S(\mu_q(S)-2)_+.
\]

Then the balanced overload `O_q` satisfies

\[
 \boxed{
 O_q\ge U_q\ge
 {1\over2}\binom{2(m-q)}{m-q}
       (\operatorname{Cat}_q-2).}                            \tag{18.8}
\]

Consequently, for every fixed `q>=3`,

\[
 \liminf_{m\to\infty}{O_q\over W}
 \ge {\operatorname{Cat}_q-2\over4\,4^q}
 \sim {1\over4\sqrt\pi q^{3/2}}.                           \tag{18.9}
\]

#### Proof

Each aligned context group contains `d=Cat_q` disjoint intrinsic
occurrences at one target.  If `h` groups have the same target, then

\[
                         (hd-2)_+\ge h(d-2)qquad(d\ge2).
\]

Distinct context groups have disjoint rooted-window occurrences, as in
Theorem 18.2, so summing gives the second inequality in (18.8).  For
`c_q=1`, the exact balanced-overload identity gives
`O_q=max(D_q^-,D_q^+)` with
`D_q^+=sum_S(mu_q(S)-2)_+=U_q`, proving the first inequality.  Divide by
the original `W=binom(2m+1,m)` and use (18.3) to obtain (18.9).
\(\square\)

Thus the unshifted canonical MSW factor fails the MWB requirement already
at every fixed depth `q>=3`; no summation over growing depths is needed.
This does not rule out a legal phase lift which moves different rows of a
context group to different translates of its target.  That distinct
question is treated in Section 20.

This also explains why assigning an extra critical factor `4^(-q)` to a
second filling would give a misleading subcritical tree sum.  At fixed
ambient semilength the two fillings occupy the same coordinate block; the
collision count does not pay `q` additional ambient coordinates.  Such a
weight silently changes the size being extracted from `m` to `m+q`.
Therefore the proposed two-spine mass transport cannot prove (3.3): the
invisible fully-inside blocks already contradict the conclusion, before
either boundary spine is considered.

## 19. Plateau/residual decomposition of the selector

Although Section 18 rules out a raw quadratic-energy estimate, its
obstruction is sharply localized.  The recursive mask parser separates
all Catalan multiplicity from a genuine two-boundary residue.

For a rooted window `(x,i,q)`, let

\[
 I=[2i+1,2i+2q]
\]

be its zero interval in the positions of `pi(x)`.  A node of `T(x)` is
**interior**, **exterior**, or **frontier** according as its permutation
block is contained in `I`, disjoint from `I`, or meets both `I` and its
complement.  Use only maximal interior nodes, so their blocks are
pairwise disjoint.

### Lemma 19.1 (completed-block dichotomy)

Conditional on the coordinate interval, its affine orientation, and the
selected physical target `S`, every exterior recursive block is uniquely
determined.  An interior block of size `r` is completely unconstrained and
has exactly `Cat_r` possible fillings.  At every recursion level there are
at most two frontier blocks.

Consequently every selector realization has a unique encoding consisting
of

1. a two-boundary frontier skeleton; and
2. one freely chosen Catalan tree for each maximal interior block.

#### Proof

On a block disjoint from `I`, the mask alternates.  After accounting for
the starting-position parity, it selects either all odd or all even local
entries of the block permutation.  For a local Dyck root `y`, these two
sets are

\[
                 \{a_0,\ldots,a_{r-1}\}=\overline y,
 \qquad          \{b_0,\ldots,b_{r-1}\}=y,                 \tag{19.1}
\]

where a bar denotes the complementary step set.  The affine translation
or reflection inherited from the ancestors is known and invertible.
Thus the selected physical coordinates in the block recover `y`
uniquely.

The mask is identically zero on an interior block.  Its coordinate set and
size are fixed by the outer context, while none of its permutation entries
is selected.  Every one of its `Cat_r` tree shapes is therefore allowed,
exactly as in Lemma 18.1.  Finally, a single interval can partially meet at
most two disjoint recursive intervals at one level, by Lemma 17.2.
Recursing on those intervals and stopping on completed blocks gives the
claimed unique encoding. \(\square\)

Call an interior block **variable** when its size is at least two.  If a
selector realization has a variable block, choose the first maximal one
in left-to-right block order.  This is a canonical first-plateau charge.
If it has none, all completed interior blocks are single nodes and hence
carry no choice; all remaining multiplicity lies on the two frontier
spines.  Thus there is no third source of selector multiplicity.

The available linear budget for plateau charges has an exact Catalan tail.

### Lemma 19.2 (pointed-subtree tail)

The number `A_(m,r)` of pairs consisting of a Dyck root of semilength `m`
and a distinguished node of its permutation recursion tree whose subtree
has size `r` is

\[
 \boxed{
 A_{m,r}=\operatorname{Cat}_r\binom{2(m-r)}{m-r}.}          \tag{19.2}
\]

For the odd-wreath normalization `W=binom(2m+1,m)`, uniformly in
`1<=R<=m`,

\[
 \boxed{
 {1\over W}\sum_{r=R}^{m}A_{m,r}\le {C\over\sqrt R}.}      \tag{19.3}
\]

#### Proof

Deleting the distinguished subtree leaves an arbitrary one-hole ordered
binary-tree context.  With `R(z)=zC(z)`, its series is

\[
 {1\over1-2R(z)}={1\over\sqrt{1-4z}}.
\]

Choosing the size-`r` filling gives (19.2).  Standard central-binomial and
Catalan estimates give

\[
 {A_{m,r}\over W}
 \le C{\sqrt m\over(r+1)^{3/2}\sqrt{m-r+1}}.               \tag{19.4}
\]

For `r<=m/2`, summing (19.4) is at most
`C sum_(r>=R)(r+1)^(-3/2)=O(R^(-1/2))`.  For `r>m/2`, put
`s=m-r`; the sum is `O(m^(-1) sum_(s<=m/2)(s+1)^(-1/2))
=O(m^(-1/2))`, which is also `O(R^(-1/2))`. \(\square\)

For `r=q` and aligned nodes, (19.2) reduces to the linear occurrence mass
behind Section 18:

\[
 {H_{m,q}\operatorname{Cat}_q\over W}
       \sim {1\over4\sqrt\pi q^{3/2}}.                     \tag{19.5}
\]

Hence its tail over `q>=q_0` is `O(W/sqrt(q_0))`, even though its
quadratic pair energy is exponential.  More generally, (19.3) is exactly
the budget needed by a plateau-aware truncation which marks a variable
subtree once and removes every window serviced by that mark.

There is an important bookkeeping qualification.  The map from a rooted
window to its first variable node need not be injective after the window
index is forgotten: one pointed subtree can lie in several larger zero
windows.  Thus (19.3) pays the plateau sector only if the truncation
coalesces all windows served by the same pointed node.  Retaining each
window separately reintroduces a factor depending on its available
placements and is not justified by (19.3).

After this plateau sector is removed, Lemma 19.1 leaves a literal
two-boundary/no-variable-block parser.  Its positional critical kernel is
already the required killed Motzkin kernel.

### Lemma 19.3 (the residual positional word has a killed marginal)

Give each of the four letters `F,C,+,-` critical weight `1/4`, and give
them increments `0,0,+1,-1`.  For a residual window, its internal cell
word is the contiguous segment

\[
                 w=\Phi(x)[i,i+q-1)                         \tag{19.6}
\]

of Corollary 14.4.  Root `w` at its first minimum.  Read the left half
backwards with signs reversed and the right half forwards.  Both are
nonnegative walks with increment weights

\[
                 p_{-1}={1\over4},\qquad
                 p_0={1\over2},\qquad
                 p_{+1}={1\over4}.                          \tag{19.7}
\]

Consequently the critical positional mass of residual words, with either
boundary and all physical address data retained as a hidden state, has an
`O(sqrt(q))` minimum-rooted Green bound provided that the hidden-state
refinement does not duplicate a word transition.

#### Proof

Equation (19.6) is (14.13).  The first-minimum construction gives two
nonnegative halves by definition.  Under the critical letter weights the
two flat colours combine to mass `1/2`, giving (19.7).  The ballot proof of
Lemma 1.1 applies verbatim and gives survival `O(r^(-1/2))` and Green mass
`O(sqrt(r))`.  For a fixed minimum location the other half and all address
information may be arbitrarily coupled hidden state, by Theorem 2.2.
Summing over the possible first-minimum locations still gives the stated
Green order (and the uncoupled four-letter word measure gives the stronger
convolution bound).  Passing to the residual subclass can only delete
words. \(\square\)

The proviso in Lemma 19.3 is the exact remaining reconstructive issue.
The unrestricted one-hole context series is

\[
                 {1\over1-2zC(z)}={1\over\sqrt{1-4z}},      \tag{19.8}
\]

so a legitimate one-copy critical charging of the address context has
coefficients `Theta(4^r/sqrt(r))`.  What must still be proved for a full
plateau-aware repair is that the physical two-spine addresses can be
coalesced into this one-copy context, rather than replicated once for each
compatible embedding.  Unlike the situation in Section 18, no completed
Catalan filling remains in this proviso: Lemmas 19.1--19.3 isolate it as a
pure boundary-address question.
