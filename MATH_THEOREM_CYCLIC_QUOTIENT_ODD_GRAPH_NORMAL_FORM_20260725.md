# Cyclic quotient normal form for invariant wreath factors

Date: 2026-07-25

Method: exact graph covering and voltage bookkeeping.

## 0. Outcome

Let `p=2m+1` be prime and let `rho:x->x+1` act on the odd graph

\[
                         O_p=KG(p,m).
\]

The action is free on its vertices.  After quotienting by `rho`, a
`rho`-invariant wreath nearfactor is exactly a packing of special
zero-voltage `p`-cycles in the quotient odd graph.  Every lower cyclic
interval becomes a necklace color of a fixed chord intersection of such
a quotient cycle.  Thus the invariant version of MWB is a rainbow
zero-voltage cycle-factor problem on `Cat_m` quotient vertices.

This is a genuine structural reduction, but not an asymptotic relaxation:
the quotient mean loads remain `W/N_q`, and the weighted overload is
divided by exactly the same factor `p` as the ambient middle mass.

## 1. The prime cyclic cover

No nonidentity power of `rho` fixes a nonempty proper subset of
`Z_p`.  Hence `rho` acts freely on the vertices of `O_p`.  Put

\[
 \overline O_p=O_p/\langle\rho\rangle,
 \qquad
 |V(\overline O_p)|={1\over p}\binom p m=\operatorname{Cat}_m=:T.
\tag{1.1}
\]

The quotient is naturally a multigraph and

\[
                         O_p\longrightarrow\overline O_p       \tag{1.2}
\]

is a regular `Z_p`-cover.  Choose representatives of quotient vertices.
Every oriented quotient edge then has a voltage in `Z_p`; the voltage of
a closed quotient walk is independent of the representative choices up
to the usual gauge change, and in particular the assertion that its total
voltage is zero is intrinsic.

### Lemma 1.1 (lift dichotomy)

Let `Cbar` be a simple quotient cycle of length `p`.

* If its voltage is zero, its inverse image is the disjoint union of `p`
  cycles of length `p`.
* If its voltage is nonzero, its inverse image is one cycle of length
  `p^2`.

#### Proof

Lift the cycle from one point in a fibre.  One circuit translates the
endpoint by its total voltage `a`.  The number of circuits needed to
close is the order of `a` in `Z_p`, which is one for `a=0` and `p`
otherwise.  The remaining assertion follows by counting the `p` points
in the starting fibre.  \(\square\)

Every `p`-cycle in `O_p` is a wreath: `p=2m+1` is the odd girth, and the
usual omitted-coordinate reconstruction recovers a cyclic order from a
shortest odd cycle.  Consequently every zero-voltage quotient `p`-cycle
lifts to one complete translation orbit of `p` wreaths.

A second admissible quotient object is a loop of nonzero voltage.  Such a
loop lifts to one physical cycle of length `p`, hence to one wreath fixed
setwise by `rho`.  These are exactly the affine/AP wreaths.  Thus the
exact invariant normal form contains

\[
 \boxed{
 \text{zero-voltage quotient `p`-cycles}
 \quad\sqcup\quad
 \text{nonzero-voltage quotient loops}.}                       \tag{1.3}
\]

There are `(p-1)/2=m` geometric AP loops, indexed by a nonzero affine
difference modulo sign.

## 2. Invariant nearfactors are zero-voltage quotient cycle packings

Call a quotient `p`-cycle **admissible** when it has zero voltage.  Let
`Cbar_1,...,Cbar_s` be vertex-disjoint admissible quotient cycles.  Their
lifts are `ps` pairwise middle-disjoint wreaths covering exactly

\[
                         p^2s                                      \tag{2.1}
\]

middle sets.  Conversely, every union of complete nonfixed `rho`-orbits
of wreaths which is a middle packing descends to a family of
vertex-disjoint admissible quotient cycles.

Therefore:

\[
 \boxed{
 \begin{array}{c}
  \text{complete nonfixed cyclic row-orbits forming a middle nearfactor}
  \\
  \longleftrightarrow
  \\
  \text{a near-spanning packing of admissible `p`-cycles in }
  \overline O_p.
 \end{array}}                                                   \tag{2.2}
\]

A packing leaving `o(T)` quotient vertices uncovered lifts to a middle
nearfactor leaving `o(pT)=o(W)` physical middle sets.  This nearfactor
form avoids the fixed-row and invariant-deck congruence issue which arises
for a fully exact invariant factor.

For a fully exact invariant factor, let `f` be the number of AP loops.
All other rows occur in orbits of size `p`, so `f` is congruent to `T`
modulo `p`.  The Catalan congruence gives

\[
 T\equiv
 \begin{cases}
 2& (m\text{ even}),\\
 p-2&(m\text{ odd})
 \end{cases}
 \pmod p.                                                       \tag{2.3}
\]

Since only `m` AP loops exist, full invariance is impossible for odd `m`.
For even `m`, any fully invariant exact factor must contain exactly two
AP loops.  This is a necessary condition, not an existence theorem.  It
is realized at `m=2,p=5`, where the two AP wreaths form the whole factor.

The first nontrivial finite target is therefore `m=6,p=13`: two AP loops
and ten zero-voltage quotient `13`-cycles on the remaining `130` of the
`T=132` quotient vertices.

This target has a completely explicit exact-cover form.  There are

\[
 W={13\choose6}=1716,qquad T=C_6=132,qquad T=10\cdot13+2.    \tag{2.4}
\]

Up to rotation and reversal there are `12!/2` geometric rows.  Exactly
the six AP rows are fixed by translation, so the number of free row
orbits is

\[
 {12!/2-6\over13}=18,423,138.                                 \tag{2.5}
\]

A free row orbit is admissible only when the row is middle-transversal:
its thirteen middle intervals must lie in thirteen distinct translation
classes.  An invariant exact factor at `m=6` is therefore exactly a
choice of two of the six AP loops and ten admissible free row orbits whose
thirteen-element class sets partition the remaining 130 middle classes.
This is a finite diagnostic instance, not an asserted construction.

At depth one there are

\[
 {1\over13}{13\choose5}=99
\]

target necklaces and mean quotient load `lambda_1=4/3`.  Any invariant
factor has physical hole count

\[
 H_1=13\,\#\{\hbox{empty depth-one necklaces}\}.              \tag{2.6}
\]

The Poisson benchmark is `99 exp(-4/3)`, about 26 empty necklaces.  A
solution of the middle exact-cover instance with substantially fewer
empty depth-one necklaces would be evidence for useful quotient
structure, but a single finite instance of course proves no asymptotic
claim.

At every depth, one AP loop places all `p` of its interval occurrences in
one target necklace.  Thus two forced loops contribute at most `2p` units
of quotient overload per depth (up to the smaller balanced quota
subtraction), and at most `2p^2` physical units.  Across every
`H=o(p)` band their total physical cost is `O(p^2H)=o(W)`.  They are
arithmetically indispensable for exact invariance but asymptotically
harmless for MWB.

Restricting this architecture to `p congruent 1 (mod 4)` would not by
itself prevent the final all-dimensional asymptotic theorem.  The prime
number theorem in the progression `1 mod 4` supplies, below every large
dimension, such a prime of relative size `1-o(1)`.  The standard repeated
trimmed lift and central-binomial comparison then transfer a
coefficient-one result from that prime subsequence to all dimensions.
Thus the odd-`m` congruence obstruction removes half of the prime test
cases, but it does not kill the architecture.

### The row-phase lift as a complete-mapping system

Fix a prime cycle `sigma` and an exact factor `F`.  Form the bipartite
middle-incidence multigraph with left vertices the rows of `F`, right
vertices the middle necklaces, and one edge for every physical middle
set.  Label an edge by its phase in its necklace.  Exact middle ownership
says that, at every right vertex, the incident phase labels form the
permutation `Z_p`.

For an exponent map `a:F->Z_p`, replacing each row `C` by
`sigma^{a(C)}C` adds `a(C)` to all labels incident with `C`.  Hence the
shift is legal if and only if, at every middle necklace, the translated
incident labels are again a permutation of `Z_p`.  This is an exact
simultaneous complete-mapping constraint.  At a depth-`q` necklace the
same variables must make approximately `p lambda_q` translated labels
nearly surjective, with only

\[
                         p(\lambda_q-1)\asymp2q^2              \tag{2.7}
\]

spare occurrences in the shallow range.  Thus the phase lift is not a
generic rounding after the middle problem: its exact and lower-shadow
constraints are two versions of the same multi-Latin system.

## 3. Exact lower-necklace colors

Take one lifted wreath cycle and index its odd-graph vertices as

\[
                         A_i=I_\pi(im,m),\qquad i\in\mathbb Z_p. \tag{3.1}
\]

Consecutive starts in the original cyclic order correspond to an index
change of `-2` in (3.1), because

\[
                         m^{-1}\equiv-2\pmod p.                  \tag{3.2}
\]

It follows that the common intersection of the `q+1` consecutive middle
windows is

\[
 I_\pi(j+q,m-q)
 =A_i\cap A_{i-2}\cap\cdots\cap A_{i-2q},
 \qquad j=im.                                                    \tag{3.3}
\]

For an admissible quotient cycle `Cbar`, choose any one of its lifts and
define its depth-`q` color at position `i` by

\[
 \boxed{
 \chi_q(\overline C,i)
 =\left[A_i\cap A_{i-2}\cap\cdots\cap A_{i-2q}\right]_{\rho}.    \tag{3.4}
\]

where brackets denote the translation necklace.  A different lift is a
global translate, so (3.4) is well defined.

The `p` lifted wreaths contain, between them, every phase of each color
in (3.4) with the indicated multiplicity.  Hence if `Pbar` is a quotient
cycle packing, the physical load of its lift is constant on target
necklaces and its common value on a necklace `O` is exactly

\[
 \boxed{
 k_q(O)=
 \#\{(\overline C,i):\overline C\in\overline P,
                       \chi_q(\overline C,i)=O\}.}               \tag{3.5}
\]

For `q=1`, this is the necklace color of the two-step chord intersection
`A_i cap A_(i-2)`.  Thus first-shadow balance asks for a near-rainbow
color profile of the selected quotient cycles.  For general `q`, the
colors are the `(q+1)`-fold chord intersections in (3.4).

## 4. Exact overload scaling

There are

\[
                         \overline N_q=N_q/p                       \tag{4.1}
\]

depth-`q` target necklaces.  A spanning quotient factor has total color
mass `T`, and therefore

\[
                         {T\over\overline N_q}
                         ={W\over N_q}=\lambda_q.                \tag{4.2}
\]

Let `c_q=floor(lambda_q)` and define the quotient lower and upper defects

\[
 \overline L_q=\sum_O(c_q-k_q(O))_+,
 \qquad
 \overline U_q=\sum_O(k_q(O)-c_q-1)_+.
\tag{4.3}
\]

Every physical target necklace has `p` phases with the same load, so the
exact balanced-overload ledger gives

\[
 \boxed{
 O_q=p\,\overline O_q,
 \qquad
 \overline O_q=\max\{\overline L_q,\overline U_q\}.}            \tag{4.4}
\]

Since `W=pT`,

\[
 \boxed{
 \sum_{q\le H}{O_q\over c_q}=o(W)
 \quad\Longleftrightarrow\quad
 \sum_{q\le H}{\overline O_q\over c_q}=o(T).}                  \tag{4.5}
\]

For a nearfactor, uncovered quotient middle vertices and the missing row
mass add the corresponding explicit error; an `o(T)` quotient leave is
an `o(W)` physical error.

## 5. The exact quotient theorem which would advance MWB

The invariant route now has a precise target.

> **Rainbow zero-voltage quotient theorem.**  For a suitable prime
> sequence `p=2m+1`, find a near-spanning packing of admissible
> zero-voltage `p`-cycles in `O_p/<rho>` whose chord-intersection color
> loads (3.5) satisfy
> 
> \[
>   \sum_{q\le H_m}{1\over c_q}
>   \max\left\{
>      \sum_O(c_q-k_q(O))_+,
>      \sum_O(k_q(O)-c_q-1)_+
>   \right\}=o(T).
> \tag{5.1}
> \]

Its lift is a cyclically invariant middle nearfactor with physical MWB
defect `o(W)`.

This theorem is not supplied by orbit-mass conservation.  It is a
simultaneous colored cycle-factor theorem with an additional zero-voltage
constraint.  Quotienting reduces the number of vertices by `p`, but (4.2)
and (4.5) show that it preserves the critical occupancy and relative
error scales exactly.  Its possible advantage is algebraic structure of
the quotient odd graph, not extra probabilistic slack.
