# Derivative-transparent Pascal seams and the upper-middle opening obstruction

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional seam identities, an unconditional no-go for the
strict triangular recursion, and an exact conditional linear Pascal module.
The note does not construct the decorated lower-middle cycle required by
the module and does not prove `nu(k)<=B(k)+O(1)`.

## 0. Outcome

The strict seam condition in the nested-intersection-bank recursion is not
inductively closed.  On an odd ground set of size `2q-1`, a rank-`q`
upper-middle factor has as many roots as rank-`q-1` collar colours.  Every
root must therefore have positive height, whereas a triangularly safe cut
requires its immediate predecessor to have height zero.  No such cut can
exist.

There is an exact replacement.  If

\[
 D_i=Q_i\cap Q_{i+1},
\tag{0.1}
\]

then the future-intersection flags satisfy

\[
 I^Q_{i,j}=I^D_{i,j-1}\qquad(j\ge1).
\tag{0.2}
\]

More importantly, open `Q` at one edge and continue it by the lifted
derivative prefix

\[
 z+D_{-1},\ z+D_0,\ z+D_1,\ldots.
\tag{0.3}
\]

Every `Q`-flag crossing the seam is **identical** to its former cyclic
flag.  The new coordinate `z` disappears from the intersection because the
root started in the `z`-free sector.

This gives an exact paired Pascal module.  A lower-middle cyclic factor `D`
on `2q-1` points which is

* upper-rainbow;
* `d`-resident;
* equipped with supported nested banks through depth `d-1`; and
* triangularly safe at one cut

produces a complete linear rank-`q` factor on `2q` points with the same
depth banks and a triangularly safe terminal opening.  Its upper-middle
sector needs no safe cut: the derivative seam transports all of its cyclic
flags exactly.

The Middle Levels Theorem supplies the unlabelled upper-rainbow pair.  The
remaining co-selection is now precise: choose such a lower-shore order with
the supported banks and one safe cut.

## 1. Exact height-cycle criterion

Let a cyclic factor have root set `Z_N` and supported height word

\[
 h:\mathbb Z_N\longrightarrow\{0,1,\ldots,d-1\}.
\tag{1.1}
\]

A cut `c` lies between roots `c-1` and `c`.  There are `t` complete roots
strictly between root `c-1-t` and that cut; equivalently, the cut is `t+1`
Johnson steps ahead.

### Lemma 1.1 (safe cuts are uncovered points of the deadline arcs)

The cut `c` is triangularly safe if and only if

\[
 h(c-1-t)\le t\qquad(0\le t\le d-2).
\tag{1.2}
\]

Equivalently,

\[
 c\notin\bigcup_{i\in\mathbb Z_N}
 \{i+1,i+2,\ldots,i+h(i)\}.
\tag{1.3}
\]

#### Proof

A root of height `h(i)` uses `Q_i,...,Q_(i+h(i))`.  For
`i=c-1-t`, it crosses the cut exactly when `h(i)>=t+1`, equivalently when
`h(i)>t`; the noncrossing condition is exactly (1.2).  Root `i` forbids the
next `h(i)` cuts, which gives (1.3).  `square`

In particular, the predecessor of every safe cut has height zero.

### Corollary 1.2 (upper-middle triangular-opening no-go)

Let the ground set have size `2q-1`, and let `Q` be a cyclic rank-`q`
factor with nested banks whose first collar map is surjective.  Then `Q`
has no triangularly safe cut.

#### Proof

The number of roots and the number of first-collar colours agree:

\[
 N={2q-1\choose q}={2q-1\choose q-1}=|\mathcal X_1|.
\tag{1.4}
\]

The first bank has size `|mathcal X_1|`, so it is the entire root set.
Thus every root has height at least one.  Lemma 1.1 says that a safe cut
would need a height-zero predecessor.  `square`

Consequently, a one-coordinate Pascal induction using strict triangular
safety necessarily stops when a recursively exposed sector is upper
middle.  This is a structural obstruction, not a shortage in the scalar
height inventory.

## 2. Derivatives preserve the whole future flag

Let

\[
 Q=(Q_i)_{i\in\mathbb Z_N}
\tag{2.1}
\]

be a cyclic rank-`q` Johnson factor, and put

\[
 D_i=Q_i\cap Q_{i+1}.
\tag{2.2}
\]

Whenever consecutive `D_i` are distinct, they are adjacent rank-`q-1`
sets: `D_i` and `D_(i+1)` are distinct coatoms of `Q_(i+1)`.

For either row define

\[
 I^Q_{i,j}=\bigcap_{u=0}^jQ_{i+u},
 \qquad
 I^D_{i,j}=\bigcap_{u=0}^jD_{i+u}.
\tag{2.3}
\]

### Lemma 2.1 (derivative flag identity)

For every `j>=1`,

\[
 \boxed{I^Q_{i,j}=I^D_{i,j-1}.}
\tag{2.4}
\]

#### Proof

Using `D_u=Q_u cap Q_(u+1)`,

\[
 \bigcap_{u=0}^{j-1}D_{i+u}
 =\bigcap_{u=0}^{j-1}(Q_{i+u}\cap Q_{i+u+1})
 =\bigcap_{u=0}^{j}Q_{i+u}.
\]

`square`

Thus a complete supported bank on the derivative row lifts one level to a
supported bank on the original row; no independent named matching is
created.

## 3. Exact transparency of a derivative seam

Open the `Q` cycle between `Q_{-1}` and `Q_0`.  Let `z` be a new point, and
form the linear prefix

\[
 \mathcal P=
 Q_0,Q_1,\ldots,Q_{-1},
 z+D_{-1},z+D_0,z+D_1,\ldots,z+D_{L}.
\tag{3.1}
\]

The seam is Johnson because `D_(-1) subset Q_(-1)`.  The lifted derivative
prefix is Johnson whenever its displayed vertices are distinct.

### Theorem 3.1 (derivative-seam transparency)

Let a root `Q_(-1-t)` have a future flag of depth `j`.  If that flag stays
inside the displayed part of (3.1), then its intersection value in
`mathcal P` is exactly its old cyclic value `I^Q_(-1-t,j)`.

In particular, a displayed derivative prefix of length `d-1` transports
every cyclic `Q`-flag of height at most `d-1` across the seam.

#### Proof

The assertion is immediate when `j<=t`.  Otherwise put `s=j-t`; the new
future window contains `s` lifted derivative owners

\[
 z+D_{-1},z+D_0,\ldots,z+D_{s-2}.
\]

The earlier `Q` owners do not contain `z`, so `z` is absent from the total
intersection.  Moreover

\[
 \begin{aligned}
 &\left(\bigcap_{v=-1-t}^{-1}Q_v\right)
   \cap\left(\bigcap_{v=-1}^{s-2}D_v\right)\\
 &\qquad=
 \left(\bigcap_{v=-1-t}^{-1}Q_v\right)
   \cap\left(\bigcap_{v=-1}^{s-2}(Q_v\cap Q_{v+1})\right)\\
 &\qquad=\bigcap_{v=-1-t}^{s-1}Q_v
 =I^Q_{-1-t,j}.
 \end{aligned}
\tag{3.2}
\]

For height at most `d-1`, the largest required value of `s` is `d-1`.
`square`

This theorem is asymmetric.  A flag beginning in the `z`-containing sector
and crossing back to a `z`-free sector loses `z`; it is not transported by
the same identity.  Thus a linear order should put the derivative sector
last, where it can use a genuinely safe terminal opening.

## 4. Upper-rainbow lower factors are exactly derivative lifts

Let `|K|=2q-1`, and let

\[
 D=(D_i)_{i\in\mathbb Z_N},
 \qquad |D_i|=q-1,
 \qquad N={2q-1\choose q-1},
\tag{4.1}
\]

be a Hamilton cycle in the Johnson graph.  Define its consecutive unions

\[
 Q_i=D_{i-1}\cup D_i.
\tag{4.2}
\]

### Proposition 4.1 (middle-level derivative pair)

If the `Q_i` are pairwise distinct, then they enumerate the complete
rank-`q` layer of `K`, form a Hamilton cycle, and satisfy

\[
 Q_i\cap Q_{i+1}=D_i.
\tag{4.3}
\]

Conversely, an alternating Hamilton cycle in the middle-levels incidence
graph gives exactly such a pair `(D,Q)`.

#### Proof

Consecutive `D` vertices are adjacent, so every union in (4.2) has rank
`q`.  The two middle layers have the same size `N`; distinctness therefore
makes the `Q_i` the complete upper layer.  Both `Q_i` and `Q_(i+1)` contain
`D_i`.  They are distinct rank-`q` sets, so their intersection is exactly
`D_i` and they are Johnson adjacent.

Conversely, list the lower vertices of an alternating middle-levels
Hamilton cycle in cyclic order.  Its intervening upper vertices are their
consecutive unions, each used once.  `square`

This is the precise meaning of an **upper-rainbow** lower-middle factor.
The Middle Levels Theorem proves that such pairs exist for every `q`; it
does not impose the supported deeper banks or a prescribed safe cut.

### Proposition 4.2 (residence expands under the upper lift)

If every positive coordinate run in `D` has length at least `d`, then every
positive coordinate run in `Q` has length at least `d+1`.

#### Proof

The incidence rule is

\[
 \mathbf1_{\{x\in Q_i\}}
 =\mathbf1_{\{x\in D_{i-1}\cup D_i\}}.
\tag{4.4}
\]

Every positive run of the `D` incidence word expands by one position to the
right.  Expanded runs separated by a one-position zero gap may merge, but
no expansion or merger creates a shorter positive run.  Thus every `Q` run
has length at least `d+1`.  `square`

## 5. The paired derivative Pascal module

Fix `2<=d<=q-1`.  Assume `D` in Section 4 has nested banks

\[
 R^D_{d-1}\subseteq\cdots\subseteq R^D_1
\tag{5.1}
\]

through depth `d-1`, and write `h_D` for their height word.  Rotate indices
so that the cut between `D_{-2}` and `D_{-1}` is triangularly safe:

\[
 h_D(-2-t)\le t\qquad(0\le t\le d-2).
\tag{5.2}
\]

Let `Q` be the upper lift (4.2), let `z` be new, and form the linear owner
path

\[
 \boxed{
 \mathcal P=
 Q_0,Q_1,\ldots,Q_{-1},
 z+D_{-1},z+D_0,\ldots,z+D_{-2}.}
\tag{5.3}
\]

It lists every rank-`q` member of `K+z` exactly once.

Give a `Q_i` root height

\[
 h_Q(i)=\min\{d-1,1+h_D(i)\},
\tag{5.4}
\]

and give the lifted `D_i` root height `h_D(i)`.

### Theorem 5.1 (exact linear Pascal bank lift)

The height assignment (5.4) partitions

\[
 \bigcup_{j=1}^{d-1}{K+z\choose q-j}
\tag{5.5}
\]

into the actual future-intersection flag prefixes of the path (5.3).  Its
terminal cut is triangularly safe.

#### Proof

The `Q` sector lists the complete `z`-free rank-`q` layer, while the lifted
`D` sector lists the complete `z`-containing rank-`q` layer.  Internal steps
are Johnson, and the one sector seam is Johnson because
`D_(-1) subset Q_(-1)`.

At depth one, every `Q` root is selected and

\[
 I^Q_{i,1}=D_i.
\]

The `D_i` enumerate every rank-`q-1` subset of `K`.  At depth `j>=2`, the
selected `Q` roots are exactly `R^D_(j-1)`, and Lemma 2.1 gives

\[
 I^Q_{i,j}=I^D_{i,j-1}.
\tag{5.6}
\]

Therefore the `Q` roots supply every `z`-free rank-`q-j` target exactly
once.  The cyclic `Q` flags which cross the sector seam keep these exact
values by Theorem 3.1.

At depth `j`, the selected lifted roots are `R^D_j`, and their values are

\[
 z+I^D_{i,j}.
\tag{5.7}
\]

They supply every `z`-containing rank-`q-j` target exactly once.  The two
families (5.6)--(5.7) are disjoint and are precisely the two Pascal parts
of the layer in (5.5).  Nesting follows from the nesting of the `D` banks
and (5.4).

At the terminal cut, only the last `d-1` lifted `D` roots can cross.  Their
height inequalities are exactly (5.2); all `Q` roots are farther than
`d-1` positions from the terminal.  Hence the terminal cut is triangularly
safe.  `square`

### Proposition 5.2 (interior residence of the linear module)

If `D` is cyclically `d`-resident, every internal positive coordinate run
of (5.3) has length at least `d`.  Only the fragments clipped by the global
left and right endpoints may be shorter.

#### Proof

The new coordinate `z` has one run consisting of the entire second sector.
For a coordinate of `K`, every unsplit internal run in the `Q` sector has
length at least `d+1` by Proposition 4.2, and every unsplit internal run in
the `D` sector has length at least `d`.

It remains to inspect the one sector seam.  A coordinate present at the
first `D` owner is also present at `Q_(-1)` and hence joins its `Q` tail to
its `D` initial fragment.  If its `D` run is split by the chosen cut into
initial and terminal lengths `u,v`, then its `Q` tail contains the whole
terminal fragment and one additional position.  The joined internal run
therefore has length at least

\[
 u+(v+1)\ge d+1.
\tag{5.8}
\]

If the coordinate is absent from `D_(-1)` but leaves at the seam, its
preceding `D` run has length at least `d`; the union rule (4.4) makes the
corresponding `Q` tail at least one position longer.  Thus this run is also
long enough.  Every remaining short fragment lies at the global beginning
of the `Q` sector or the global end of the `D` sector.  `square`

The two clipped endpoint fragments are exactly the usual linear boundary
state; this proposition does not claim a cyclic residence closure.

## 6. What the module removes, and what remains

Corollary 1.2 proves that strict triangular safety cannot recursively open
the upper-middle sector.  Theorem 5.1 removes that obstruction without
paying any collar colour: the upper-middle sector is opened through its
derivative, and all crossing flags are transported literally.

The remaining input is one lower-middle cycle `D` for which the following
properties coexist:

\[
 \boxed{
 \text{upper-rainbow middle-levels order}
 +\text{supported nested banks}
 +\text{one triangularly safe cut}.}
\tag{6.1}
\]

The first property alone is the Middle Levels Theorem.  The present note
does not prove the latter two, nor does it preserve arbitrary-width upper
OR witnesses, produce the residual low-rank renewal deck, close the two
linear endpoint fragments, or construct a cyclic parent factor.  It
therefore does not prove the additive-constant conjecture.

What it does prove is a sharper Pascal frontier: a safe cut is needed only
on the final lower derivative sector.  The preceding upper-middle sector,
where such a cut is arithmetically impossible, has an exact zero-loss
derivative seam.
