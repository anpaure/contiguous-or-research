# Truncated-rotor compilation of the static multi-swap cube

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let

\[
 M=m+H,
 \qquad Q=o(H),
 \qquad \frac{Q^2}{M}\longrightarrow\infty,
\]

as in the calibrated regime

\[
 H\asymp\sqrt{m\log m},
 \qquad Q\asymp\sqrt{m\log\log m}.
\]

There are two different conclusions.

1. The **square** static cube with `ell` row pairs and `ell` ports still has
   a sharp chronological obstruction.  If
   `ell asymp M/Q`, a worst cube vertex requires at least

   \[
   (4-o(1))\ell Q=(4-o(1))M
   \]

   literal state occurrences, even for truncated radius `Q`.  Under a
   coefficient-one length budget it can carry only

   \[
   O(M^2/Q^2)=o(M)
   \]

   independent directions per carrier.
2. The **rectangular** sharpening behaves differently.  There is an exact
   directed rotor routing lemma which reprograms an arbitrary ordered
   `2Q`-collar in `4Q+1` updates while making one prescribed core--tail
   exchange.  Using

   \[
   t=(1+o(1))\frac{M}{8Q}
   \]

   ports and

   \[
   p=(1/2-o(1))Q
   \]

   row pairs, every one of the `2^(pt)` static cube vertices has a literal
   one-path compilation of at most `M` states, with one initialization of
   cost `2Q+2`.  It visits all `2t` marked positive states and therefore
   certifies

   \[
   \boxed{pt=(1/16-o(1))M}
   \]

   independent, support-disjoint, rank-isolating rectangles.

For the **designated marked-state projection**, independent fair cube bits
give an exact legal positive kernel with maximum coordinate variance `1/4`
and covariance trace `(1/16-o(1))M` per carrier.  Thus truncated rotor
routing removes the former fragmentation/reset obstruction at coefficient
scale.

This is not yet `(TRP)`.  The `M-o(M)` connector states are genuine physical
states, and their full hard-flag and owner incidences depend on the cube
vertex.  The marked-state rectangle identity does not cancel those
connector incidences.  Hence the construction supplies a coefficient-scale
**designated** correction kernel, but not yet an `O(1)`-variance theorem for
the full physical load vector or an owner-preserving exact factor switch.

## 1. The truncated carrier rotor

Fix a carrier `U` of size `M`.  Put `n=2Q`.  A quotient rotor state is

\[
 \omega=(A;z_1,\ldots,z_n;B),
\]

where

\[
 |A|=m-Q,
 \qquad |B|=H-Q,
\]

and these sets and singleton labels partition `U`.  One rotor update chooses
`x in A` and `y in B` and sends

\[
 (A;z_1,\ldots,z_n;B)
 \longmapsto
 (A-x+y;x,z_1,\ldots,z_{n-1};B-y+z_n).
 \tag{1.1}
\]

As audited separately, this is the exact recurrence on the prefix-plus-tail
quotient of a genuine MTF state, and every quotient walk compiles literally.

The key new input is an exact routing algorithm.

## 2. Exact flush-and-reload routing

### Theorem 2.1 (one-exchange collar routing)

Let

\[
 \omega=(A;z_1,\ldots,z_n;B)
\]

and

\[
 \omega'=(A-a+b;z'_1,\ldots,z'_n;B-b+a),
\]

where

\[
 a\in A,
 \qquad b\in B,
 \qquad
 \{z'_1,\ldots,z'_n\}=\{z_1,\ldots,z_n\}.
\]

If `|A|>=n+1`, then there is an exact directed rotor walk from `omega` to
`omega'` of

\[
 \boxed{2n+1=4Q+1}
\]

updates.

#### Proof

Choose distinct elements

\[
 x_1,\ldots,x_n,a\in A
\]

and put `x_(n+1)=a`.

In the first `n+1` updates, use core choices

\[
 x_1,x_2,\ldots,x_n,x_{n+1},
\]

and tail choices

\[
 b,z_n,z_{n-1},\ldots,z_1.
\]

The tail choice `z_(n-r+2)` at update `r>=2` is legal because that label
dropped from the end of the ordered collar in the preceding update.  After
these `n+1` moves the state has

\[
 A_1=(A-\{x_1,\ldots,x_n,a\})+b+\{z_1,\ldots,z_n\},
\]

\[
 B_1=(B-b)+x_1,
\]

and ordered collar

\[
 (a,x_n,x_{n-1},\ldots,x_2).
\]

In the next `n` updates, use the core choices

\[
 z'_n,z'_{n-1},\ldots,z'_1
\]

and the tail choices

\[
 x_1,x_2,\ldots,x_n.
\]

At the first of these moves, `x_1` is in the tail.  At every later move,
`x_r` was dropped from the collar one move earlier, so all choices are legal.
The chosen `z'` labels appear in the final collar in reverse chronological
order, namely

\[
 (z'_1,\ldots,z'_n).
\]

All `x_1,...,x_n` have returned to the core, while `a` drops into the tail
on the last move.  The final unordered blocks are therefore

\[
 A-a+b,
 \qquad B-b+a.
\]

This is exactly `omega'`. \(\square\)

The theorem is uniform in the target collar permutation.  It routes all
pair-orientation signatures at the same cost; no adjacent transposition is
paid separately.

## 3. Radius-`Q` static rectangular cube

Use a cyclic order `pi` on `U`.  For a cyclic order `rho`, let
`S_t^Q(rho)` be its radius-`Q` carrier state at phase `t`.  Its owner is the
length-`m` positional interval, and its lower and upper flag members are the
positional intervals of lengths `m-q` and `m+q`, `q<=Q`.

Choose integers `p,t` satisfying

\[
 4t+2p\le Q.
 \tag{3.1}
\]

Let the row swaps `alpha_i`, `0<=i<p`, have cuts

\[
 a_i=4t+2i,
\]

and let the marked phases and column-swap cuts be

\[
 s_j=2j,
 \qquad b_j=m+2j-1,
 \qquad 0\le j<t.
\]

All swap pairs are disjoint.  Put

\[
 \alpha_x=\prod_{i=0}^{p-1}\alpha_i^{x_i},
 \qquad
 \beta=\prod_{j=0}^{t-1}\beta_j.
\]

For a bit matrix `E in {0,1}^{p times t}`, write `x^j` for its `j`-th
column and define the two marked states

\[
 A_j(E)=S_{s_j}^Q(\alpha_{x^j}\pi),
\]

\[
 B_j(E)=S_{s_j}^Q(\alpha_{1-x^j}\beta\pi).
 \tag{3.2}
\]

Exactly as in the static port-cube proof, toggling bit `(i,j)` changes the
sum of the two marked flag columns by an elementary rectangle `rho_(ij)` at
lower depth

\[
 q_{ij}=4t+2i-2j+1.
 \tag{3.3}
\]

The inequalities

\[
 2t+3\le q_{ij}\le4t+2p-1\le Q-1
\]

place every rectangle in the truncated band.  The supports of distinct
`rho_(ij)` are pairwise disjoint, and

\[
 \|\rho_{ij}\|_2^2=4.
 \tag{3.4}
\]

The marked middle-owner multiset at port `j` is

\[
 \{X_j,\beta_jX_j\},
\]

independent of `x^j`.

The only issue left by the static construction was literal chronology.

## 4. One-path compilation of every cube vertex

### Lemma 4.1 (the marked pairs satisfy Theorem 2.1)

For every `j`, the two states `A_j(E)` and `B_j(E)` have the same set of
ordered-collar labels.  Their collar orders may be arbitrary, and their
unordered core and carrier-tail blocks differ by exactly the exchange made
by `beta_j`.

If `j<t-1`, follow the cyclic rotor trajectory of the frame defining
`B_j(E)` for two updates and call the resulting phase-`s_(j+1)` state
`C_j(E)`.  Then `C_j(E)` and `A_(j+1)(E)` again have the same ordered-collar
label set and differ by exactly the one core--tail exchange `beta_(j+1)`.

#### Proof

At phase `s_j`, (3.3) says every row pair lies wholly inside the lower
ordered half of the radius-`Q` collar.  Row swaps therefore permute the
collar but do not change its label set or either unordered block.

The pair `beta_j` is exactly the pair crossing the right boundary of the
middle owner.  Its inside label lies in the large unordered core, and its
outside label lies in the carrier tail.  Every `beta_h`, `h<j`, lies wholly
inside the core, and every `beta_h`, `h>j`, lies wholly inside the tail.
Thus the product `beta` changes the quotient state blocks only through the
single exchange `beta_j`.

After two cyclic updates the phase is `s_(j+1)`.  All row pairs are still in
the lower ordered collar by the lower bound in (3.3), and now the only
column pair crossing the owner boundary is `beta_(j+1)`.  The same argument
applies. \(\square\)

### Theorem 4.2 (literal cube-vertex compilation)

Put

\[
 d=4Q+1.
\]

For every bit matrix `E`, there is one directed truncated-carrier rotor walk
which visits

\[
 A_0(E),B_0(E),A_1(E),B_1(E),\ldots,A_{t-1}(E),B_{t-1}(E)
\]

in this order and has exactly

\[
 \boxed{N=(2t-1)(4Q+2)}
 \tag{4.1}
\]

state occurrences.

#### Proof

Start at `A_0(E)`.  Apply Theorem 2.1 to reach `B_0(E)` in `d` updates.
For `j<t-1`, take the two cyclic rotor updates from `B_j(E)` to `C_j(E)`,
then apply Theorem 2.1 from `C_j(E)` to `A_(j+1)(E)`.  Finally apply
Theorem 2.1 from every `A_j(E)` to `B_j(E)`.

The number of transitions is

\[
 td+(t-1)(d+2).
\]

Adding the initial state gives

\[
 1+td+(t-1)(d+2)
 =(2t-1)(4Q+2).
\]

Every transition is a genuine rotor update, so the entire sequence is one
literal-compilable path. \(\square\)

Choose `t` to be the largest integer with

\[
 (2t-1)(4Q+2)\le M,
 \tag{4.2}
\]

and put

\[
 p=\left\lfloor\frac{Q-4t}{2}\right\rfloor.
 \tag{4.3}
\]

Since `M/Q^2->0`, these satisfy

\[
 t=(1+o(1))\frac{M}{8Q},
 \qquad
 p=(1/2-o(1))Q.
\]

Consequently

\[
 \boxed{pt=(1/16-o(1))M.}
 \tag{4.4}
\]

If the walk in Theorem 4.2 has fewer than `M` states, continue by arbitrary
legal rotor steps until it has exactly `M`.  Initializing its first state
costs `2Q+2` letters, and every later state costs one.  The complete literal
word therefore has length

\[
 M+2Q+1=M+o(M).
 \tag{4.5}
\]

There is one path and one initialization per carrier.  Thus the
fragmentation/reset cost is `O(Q)=o(M)`, independent of the number
`pt=Theta(M)` of marked repair bits.

## 5. The square cube still fails sharply

The positive theorem uses the rectangular geometry `p asymp Q`,
`t asymp M/Q`.  It does not rescue the square choice
`ell times ell` with `ell asymp M/Q`.

### Lemma 5.1 (ordered-collar recycle latency)

Suppose a marked label pair lies in the lower half of the ordered `2Q`-collar
at two rotor states and has opposite relative orientation at those states.
If its ordered indices at the two states each lie in an interval of width
`R`, then the two states are separated by at least

\[
 2Q-R-O(1)
 \tag{5.1}
\]

rotor updates.

#### Proof

While two labels remain in the ordered collar, recurrence (1.1) shifts both
one position to the right and preserves their relative order.  Therefore at
least one label must drop past position `2Q` and later reenter at position
one.

A label beginning at ordered index `r` drops after `2Q-r+1` updates.  It
cannot be selected from the tail in that same update.  It can enter the core
one update later and can be selected into ordered position one one further
update later.  Reaching target ordered index `r'` then needs another
`r'-1` updates.  The total is

\[
 2Q-r+r'+2.
\]

Minimizing over two index intervals of common width `R` gives (5.1), with an
absolute endpoint slack. \(\square\)

In the square static cube, the row-pair deletion depths all lie between
`2ell+3` and `6ell-1`.  Hence their ordered indices lie in an interval of
width at most `4ell+O(1)`.  Put

\[
 D_Q=2Q-4\ell-O(1).
\]

Choose a cube vertex whose `2ell` column and complementary-column signatures
are pairwise distinct.  If a literal realization uses `F` rotor paths
containing these marked states and `N` state occurrences, Lemma 5.1 gives

\[
 \boxed{N\ge F+(2\ell-F)D_Q.}
 \tag{5.2}
\]

Including one initialization per path, its word length is at least

\[
 N+F(2Q+1)
 \ge
 2\ell D_Q+F(2Q+2-D_Q).
 \tag{5.3}
\]

For `ell=o(Q)`, this is

\[
 (4-o(1))\ell Q.
 \tag{5.4}
\]

Thus `ell asymp M/Q` costs `(4-o(1))M`, not `M+o(M)`.  Conversely a
coefficient-one budget forces

\[
 \ell\le(1/4+o(1))\frac{M}{Q},
\]

so the square cube contains at most

\[
 \ell^2\le(1/16+o(1))\frac{M^2}{Q^2}=o(M)
 \tag{5.5}
\]

independent cells.

This also rules out retaining a near-full subset of square-cube vertices.
Let `c(E)` be the number of distinct complement classes among the `ell`
columns of `E`.  The marked state family contains `2c(E)` distinct
signatures, so (5.2)--(5.3) force

\[
 c(E)\le(1/4+o(1))\ell
\]

when `ell asymp M/Q` and the word has coefficient one.  The number of such
matrices is at most

\[
 \sum_{c\le(1/4+o(1))\ell}
 \binom{2^{\ell-1}}c(2c)^\ell
 =2^{(1/4+o(1))\ell^2},
 \tag{5.6}
\]

whereas the full cube has `2^(ell^2)` vertices.  Thus no
`2^((1-o(1))ell^2)` subset has coefficient-one literal compilations in
this square geometry.

## 6. Independent directions and variance

For a compiled path, designate only the two marked flag columns at each
port.  Let `J(E)` be their hard-band incidence vector.  The static phasewise
identity remains exact:

\[
 \boxed{
 J(E)-J(0)=\sum_{i=0}^{p-1}\sum_{j=0}^{t-1}E_{ij}\rho_{ij}.}
 \tag{6.1}
\]

All states counted in `J(E)` occur literally on the one rotor path from
Theorem 4.2.  Hence this is a positive legal **designated-incidence** kernel,
not a formal signed-state construction.

Let the bits be independent fair Bernoulli variables.  Since the rectangle
supports are disjoint and `||rho_(ij)||_2^2=4`, the centered covariance
satisfies

\[
 \operatorname{tr}\operatorname{Cov}(J(E))
 =\frac14\sum_{i,j}\|\rho_{ij}\|_2^2
 =pt=(1/16-o(1))M.
 \tag{6.2}
\]

Every target coordinate belongs to at most one rectangle, and therefore

\[
 \boxed{
 \max_S\operatorname{Var}(J(E)_S)\le\frac14.}
 \tag{6.3}
\]

This is the requested `O(1)` upper-variance legal kernel on the designated
repair projection, with coefficient-scale total variance.

The square construction cannot do this at coefficient scale.  Equation
(5.5) gives covariance trace `o(M)` per carrier, hence `o(W)` after summing
over the calibrated `N_H=(1+o(1))W/M` carriers.  Its average useful variance
is asymptotically zero.

### 6.1 Why this is not yet a full-load kernel

The literal path also contains `M-2t` connector/padding states.  Their flags
are real and can only add coverage, so ignoring them is legitimate in a
positive cover certificate.  But their incidence vector depends on `E`:
the flush-and-reload route inserts the target collar labels in an
`E`-dependent order.

Accordingly, if

\[
 \widetilde J(E)
\]

denotes the **complete** hard-band multiplicity vector of the physical path,
then (6.1) does not assert

\[
 \widetilde J(E)-\widetilde J(0)
 =\sum E_{ij}\rho_{ij}.
\]

There is a real reason not to assume an automatic `O(1)` variance bound.
Under an equivariant routing of two adjacent labels, their order discrepancy
is carried through the ordered `2Q`-collar for `Theta(Q)` successive states.
In the time-resolved flag vector this creates `Theta(Q)` nonzero
differences.  Projection to the aggregate load vector may cancel some of
them, but no such cancellation theorem is currently proved.

The same distinction initially appears at middle rank: the `2t` marked
middle-owner multiset is independent of `E`, while the connector-owner
multiset can vary.  Section 6.2 below shows that this particular variation
is nevertheless affine with bounded influence.  It is not identically zero,
so Theorem 4.2 is still not an owner-preserving exact-factor switch.

One useful fractional fact survives.  If the base cyclic order and all
buffer choices in Theorem 2.1 are averaged equivariantly under coordinate
permutations of `U`, then every fixed time marginal is uniform on rank-`m`
owners and every designated rank marginal is symmetric.  Hence the compiled
path family retains exact symmetric **expected occurrence loads**.  Turning
that measure into one support-level near-rainbow selection remains the same
correlated integral gate as `(TRP)`.

### 6.2 The complete middle-owner kernel is already bounded

There is a stronger conclusion at the middle rank.  Use the slot-equivariant
version of Theorem 2.1: the buffer slots are fixed independently of the row
pair orientations, and the target collar labels are inserted in the target
slot order.  Do not add the optional padding after the last marked state.

Consider one marked adjacent row pair.  During Phase I of Theorem 2.1 its
two labels shift together through the ordered collar.  The middle owner is
the unordered core together with the first `Q` collar slots.  The pair can
affect this set only twice:

1. once when its two adjacent collar slots straddle the boundary between
   positions `Q` and `Q+1`;
2. once when the first label has been promoted from the tail into the core
   while the second label is still in the tail.

At the next update both labels are in the core.  During Phase II the two
target labels are inserted consecutively.  Before insertion both lie in the
core; after the first insertion one is in the first collar slot and the
other remains in the core; after the second both lie in the first two collar
slots.  All of these locations belong to the middle owner, and the target
pair finishes in the lower half of the collar.  Thus target insertion adds
no further bit-dependent middle owner.

The two cyclic steps between ports also preserve the middle owner under all
row-pair orientations: every row pair remains wholly inside the middle
interval.  It follows that bit `(i,j)` affects middle owners only

* at at most two states of the route `A_j -> B_j`; and
* at at most two states of the route `C_j -> A_(j+1)` when `j<t-1`.

In particular, if `O(E)` is the **complete** middle-owner multiplicity vector
of the compiled, unpadded path, then

\[
 \boxed{
 O(E)=O(0)+\sum_{i,j}E_{ij}d_{ij}}
 \tag{6.4}
\]

for integral directions satisfying

\[
 \|d_{ij}\|_1\le8,
 \qquad
 \|d_{ij}\|_2^2\le64.
 \tag{6.5}
\]

To justify the affine statement, observe that at a middle-owner boundary at
most one disjoint marked pair is split.  The later core--tail split occurs
only after all original marked lower pairs have moved beyond the first-`Q`
boundary, so the two possible split mechanisms do not create a two-bit
interaction at one owner occurrence.

For independent fair bits,

\[
 \boxed{
 \operatorname{tr}\operatorname{Cov}(O(E))
 \le16pt=O(M).}
 \tag{6.6}
\]

Thus connector variation does **not** create a superconstant total-variance
penalty at the middle rank.  The complete middle-owner kernel is already a
coefficient-scale bounded-influence affine kernel.  The unresolved variance
is confined to the nonmiddle hard flags, where the one-step core--tail split
of a marked pair can change an entire radius-`Q` flag column.

## 7. Calibrated global ledger

Use one compiled `M`-state path in each of the `N_H` calibrated carriers.
The primary word length is

\[
 MN_H+(2Q+1)N_H=W+o(W).
\]

The number of independent designated rectangles is

\[
 ptN_H=(1/16-o(1))MN_H=(1/16-o(1))W.
 \tag{7.1}
\]

Their marked-state covariance trace is the same quantity, and every
within-carrier target variance is at most `1/4`.

Thus truncated-radius routing genuinely crosses the former static/literal
capacity barrier:

\[
 \boxed{
 \text{one-reset literal paths can carry }\Theta(W)
 \text{ independent designated hard-band directions}.}
\]

The remaining coefficient-one theorem is no longer a fragmentation or bit
count question.  It is one of the following equivalent-looking correlation
tasks:

1. control or cancel the connector-state incidence variance;
2. choose the path bits jointly with the carrier paths so connector owners
   and flags remain near-rainbow;
3. build a paired routing whose complete incidence difference, not merely
   its marked projection, equals the rectangle sum;
4. use only the designated positive corrections inside a global monotone
   cover argument which is insensitive to incidental connector coverage.

None of these final correlation statements is proved here.  What is proved
is the exact literal compilation and a coefficient-scale, support-disjoint,
`O(1)`-variance designated kernel.

## 8. Positive all-connector reinterpretation

The signed-kernel limitation above is not a limitation on using connector
flags as positive coverage.  The exact monotone reinterpretation is proved
in
`MATH_ATTACK_RECTANGULAR_COMPILED_CUBE_VERTICAL_BRAID_20260725.md`.

For every rotor transition its complete flag columns satisfy the Boolean
diamond identities

\[
 F_h(t)\cap F_h(t+1)=F_{h-1}(t),
 \qquad
 F_h(t)\cup F_h(t+1)=F_{h+1}(t+1).
\]

Hence every connector flag is a literal contiguous OR and is exactly an
iterated intersection/union shadow of the connector-owner chronology.  The
resulting complete-braid hole count has an exact excess-collision formula.
It yields a new sufficient gate: choose one mixed-frame compiled route per
carrier so that the aggregate excess collision over all hard ranks is
`o(W)`.

This does not make individual cube-bit flips monotone.  A flip replaces one
braid by an incidence-incomparable braid at `Omega(Q)` ranks.  The positive
route must therefore select whole braids globally.  Also, since the marked
states occupy only `o(W)` positions, the connector states themselves must
supply `W-o(W)` distinct middle owners in any coefficient-one realization.
