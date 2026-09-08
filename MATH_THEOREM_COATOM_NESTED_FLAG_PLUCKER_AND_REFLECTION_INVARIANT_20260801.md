# The unplanted common-order coatom action has a reflected pair invariant

Date: 2026-08-01  
Lane: nested lower-shadow routing for the additive-constant programme  
Status: unconditional algebraic theorems for the **unplanted common-order**
mixed-screen tensor.  They identify the complete rational invariant at
depth two and an all-depth invariant inside that restricted fibre.  They do
**not** give an invariant of the endpoint-planted safe-carrier graph and do
not prove bounded terminal compiler deletion.

The stronger integer maximal-chain and depth-two lattice statements are
also proved independently in
`MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`.
Section 2 below supplies a short independent rational proof.  The new point
here is the global reflected pair-degree invariant after the filler flags
are embedded into the Boolean layers.

> **Critical scope boundary.**  The authoritative repaired endpoint planting
> uses first-block order `(p,g_1,...,g_d,g_0)` and transition zero upper.
> Its untwisted lower current still obeys the reflected identity, but the
> same planted template with one label-attached adjacent omission swap in
> the `Ica` block does not.  Thus no statement in this note may be used to
> claim that an actual planted safe-move component is trapped in a reflected
> quadratic fibre.

## 0. Outcome

Let `mu_q(T)` be the occurrence-count vector of intersections of `q+1`
consecutive owners in a carrier `T`.  A mixed coatom move changes, at each
depth `2 <= q <= d`, exactly four entries of `mu_q`, with coefficient one.

At depth two this change is exactly a four-cycle (Pluecker) move in the
Johnson layer.  Abstractly, all such moves span over `Q` the complete kernel
of the coordinate-incidence map.  Thus the **only rational linear
invariants at depth two alone** are the coordinate degrees.

The coupled action across depths is strictly smaller.  For every coordinate
pair `{x,y}` and every reflected pair of depths

\[
                         q'=d+2-q,
\]

the quantity

\[
 \boxed{
   \deg^{(2)}_q(x,y)-\deg^{(2)}_{q'}(x,y)
 }
 \tag{0.1}
\]

is invariant under every **unplanted common-order** mixed coatom move, where

\[
 \deg^{(2)}_q(x,y)
   =\sum_{S\supseteq\{x,y\}}\mu_q(S).
\]

It remains invariant under compositions made entirely from that restricted
common-order catalogue.  It is not invariant under the planted catalogue.
Modulo the already conserved point degrees, (0.1) supplies

\[
 \left\lfloor\frac{d-1}{2}\right\rfloor
       \left(\binom{k}{2}-k\right)                 \tag{0.2}
\]

independent rational invariants in the stable central range of the
unplanted fibre.  Hence screen changes and label changes alone are not a
depth-by-depth Markov basis.  Endpoint planting and variable coatom orders
are genuine additional directions and invalidate this as an obstruction to
the additive-constant programme.

## 1. Exact signed action

Write

\[
 J=K\cup\{\infty,c\},\qquad
 P_t=\{f_1,\ldots,f_t\},\qquad
 S_t=\{f_{d-t+1},\ldots,f_d\}.
\]

At depth `q`, put `t=d-q+1`.  The old-only entries are

\[
                  J\cup\{b\}\cup P_t,
             \qquad J\cup\{a\}\cup S_t,
\]

and the new-only entries are

\[
                  J\cup\{a\}\cup P_t,
             \qquad J\cup\{b\}\cup S_t.
\]

Every displayed occurrence has multiplicity one in the local signed deck.
Consequently, with `[R]` denoting the basis vector at a set `R`,

\[
\begin{aligned}
 \Delta_q={}&[J\cup\{a\}\cup P_t]
             +[J\cup\{b\}\cup S_t]\\
            &-[J\cup\{b\}\cup P_t]
             -[J\cup\{a\}\cup S_t].               \tag{1.1}
\end{aligned}
\]

All four sets have rank `r-q`.  Formula (1.1) is valid for the reverse move
after changing its sign.

### Lemma 1.1 (exact natural-hole update)

Let the two negative entries of (1.1) be `O_1,O_2` and the two positive
entries be `N_1,N_2`.  If `h_q` denotes the number of absent natural
depth-`q` targets, then

\[
 h_q(T')-h_q(T)
   =\sum_{i=1}^2 {\bf1}_{\{\mu_q(O_i)=1\}}
    -\sum_{i=1}^2 {\bf1}_{\{\mu_q(N_i)=0\}}.         \tag{1.2}
\]

#### Proof

The four entries are distinct and their multiplicities change by exactly
one.  Decrementing an entry creates a hole exactly at multiplicity one;
incrementing an entry fills a hole exactly at multiplicity zero.  No other
entry changes.  \(\square\)

Thus a monotone repair requires duplicate donors, not merely missing
targets.  Equation (1.2) is exact, but it does not assert that a desired
embedded packet is present in the current carrier.

## 2. Depth two is exactly a Johnson square

At `q=2`, put

\[
 H=J\cup\{f_2,\ldots,f_{d-1}\}.
\]

Then (1.1) is

\[
 [Haf_1]+[Hbf_d]-[Hbf_1]-[Haf_d].                 \tag{2.1}
\]

Here `|H|=r-4`; the four letters `a,b,f_1,f_d` are distinct.  Thus (2.1)
is the difference of the two diagonals of a Johnson square on a common
rank-`r-4` core.

Conversely, assume `r>=d+4` and that the ground set has at least `r+4`
coordinates.  Given an arbitrary rank-`r-4` core `H` and four distinct
outside coordinates, partition `H` as

\[
 H=K\,\dot\cup\,\{\infty,c\}
       \,\dot\cup\,\{f_2,\ldots,f_{d-1}\},
\]

assign the four outside coordinates to `a,b,f_1,f_d`, and use four further
outside coordinates for `f_0,f_{d+1}` and the two inactive active labels.
This realizes either orientation of every abstract Johnson square as the
depth-two projection of a labelled coatom template.  This is a catalogue
statement; a particular physical carrier need not contain every labelled
planting.

### Theorem 2.1 (complete rational depth-two span)

Let `s=r-2`, let

\[
 A_s:\mathbb Q^{\binom{[k]}s}\longrightarrow\mathbb Q^k,
 \qquad (A_sz)_x=\sum_{S\ni x}z_S,
\]

and suppose `2<=s<=k-2`.  The rational span of all Johnson-square vectors
(2.1) is exactly

\[
                              \ker A_s.             \tag{2.2}
\]

Therefore every rational linear invariant of the depth-two occurrence deck
is a linear combination of its coordinate degrees.

#### Proof

Every square vector has zero coordinate degree, so its span is contained in
`ker A_s`.

For the reverse inclusion, let `w` be a function on the `s`-sets orthogonal
to every square.  For distinct `i,j` and an `(s-1)`-set `R` avoiding them,
put

\[
             \delta_{ij}(R)=w(R+i)-w(R+j).
\]

If `R=G+x` and `R'=G+y` are adjacent `(s-1)`-sets avoiding `i,j`, the
square on `G` and `i,j,x,y` gives

\[
                       \delta_{ij}(R)=\delta_{ij}(R').
\]

The relevant Johnson graph is connected, so `delta_ij(R)` is independent
of `R`.  Choose numbers `beta_i` realizing these pairwise differences.
Then

\[
                       w(S)-\sum_{i\in S}\beta_i
\]

is unchanged by every one-coordinate exchange and is therefore constant
on the rank-`s` Johnson graph.  Since every `S` has the same size, absorb
that constant equally into the `beta_i`.  Hence

\[
                         w(S)=\sum_{i\in S}\beta_i,
\]

so the orthogonal complement of the square span is precisely the row space
of `A_s`.  Taking orthogonal complements proves (2.2).  \(\square\)

The theorem is deliberately rational.  It does not say that nonnegative
integer occurrence decks in the same fibre are connected by legal serial
moves.  Indeed, a two-edge `s`-uniform multihypergraph whose edges do not
share an `(s-2)`-core admits no such local square at all.  Rational span is
not physical reachability.

## 3. The reflected quadratic invariant

For a signed occurrence vector `z` on one layer define

\[
 \deg^{(1)}_z(x)=\sum_{S\ni x}z_S,
 \qquad
 \deg^{(2)}_z(x,y)=\sum_{S\supseteq\{x,y\}}z_S.
\]

### Theorem 3.1 (point balance and pair reflection)

For the signed move (1.1):

\[
 \deg^{(1)}_{\Delta_q}(x)=0
       \quad\hbox{for every `q` and every `x`},       \tag{3.1}
\]

and

\[
 \boxed{
 \deg^{(2)}_{\Delta_q}(x,y)
   =\deg^{(2)}_{\Delta_{d+2-q}}(x,y)
 }
 \tag{3.2}
\]

for every coordinate pair `{x,y}`.

#### Proof

Point balance is immediate from the `2 by 2` rectangle (1.1).

For pair degrees, all pairs have zero signed count except possibly
`{a,f_i}` and `{b,f_i}`.  For the former the signed count is

\[
 \epsilon_t(i)={\bf1}_{\{i\le t\}}
                 -{\bf1}_{\{i>d-t\}},               \tag{3.3}
\]

and for the latter it is `-epsilon_t(i)`.  At reflected depth
`q'=d+2-q`, the corresponding prefix length is `t'=d-t`.  But

\[
\begin{aligned}
 \epsilon_{d-t}(i)
   &={\bf1}_{\{i\le d-t\}}-{\bf1}_{\{i>t\}}\\
   &={\bf1}_{\{i\le t\}}-{\bf1}_{\{i>d-t\}}
    =\epsilon_t(i),                                  \tag{3.4}
\end{aligned}
\]

because each of the two complementary indicator pairs sums to one.  This
proves (3.2).  \(\square\)

### Corollary 3.2 (common-order components split into quadratic fibres)

Along every walk using only unplanted common-order moves, all point degrees
at each depth and all quantities (0.1) are constant.

#### Proof

Each restricted step has signed change `Delta_q` or `-Delta_q`.  Equations
(3.1)--(3.2) telescope.  This derivation does not cover the endpoint-planted
order.  The repaired untwisted planting happens to remain reflected, while
the adjacent `Ica` twist explicitly breaks it.  \(\square\)

### Proposition 3.3 (independent invariant count)

Assume every involved rank lies between `2` and `k-2`.  In addition to the
`(d-1)k` point-degree invariants, (0.1) contains at least

\[
 \left\lfloor\frac{d-1}{2}\right\rfloor
       \left(\binom{k}{2}-k\right)
\]

independent invariants.

#### Proof

On any nontrivial uniform layer, the pair-containment functions have rank
`binom(k,2)` over `Q`.  One elementary proof is to suppose coefficients
`c_xy` sum to zero on every fixed-size set, compare two such sets differing
by one coordinate, and conclude first that all edges incident to a fixed
outside coordinate have equal coefficient, then that all coefficients are
equal, and finally that the common coefficient is zero.

The point functions form a `k`-dimensional subspace of the pair functions,
because on a rank-`s` layer

\[
 \sum_{y\ne x}{\bf1}_{\{x,y\}\subseteq S}
       =(s-1){\bf1}_{\{x\in S\}}.                   \tag{3.5}
\]

Thus each reflected depth pair contributes `binom(k,2)-k` genuinely
quadratic differences modulo the already counted point invariants.  The
reflection partitions the `d-1` depths into `floor((d-1)/2)` disjoint
pairs and at most one fixed middle depth, so the contributions from
different pairs are independent.  \(\square\)

## 4. Exact consequence for routing

Let `1_q` denote the all-one vector on the rank-`r-q` target layer, and put

\[
                         e_q=\mu_q-\mathbf1_q.
\]

If a terminal carrier has no natural depth-`q` holes, then `e_q>=0`; it is
the repeat-excess distribution.  Corollary 3.2 gives an immediate finite LP
test for every component of the **restricted unplanted common-order** move
graph:

> there must exist nonnegative excess vectors at all depths, with the
> prescribed total masses, point degrees, and reflected pair differences
> inherited from the starting carrier.

Failure proves only that this restricted component cannot reach complete
natural lower shadows.  It says nothing about a component containing the
endpoint-planted or variable-order moves.  Passing it does not prove
physical reachability or common-cap compilability.

The main conceptual conclusion is stricter than a warning about proof
method.  The canonical packet transports a **single coupled flag current**:

\[
 \text{repair at depth `q`}
 \quad\Longleftrightarrow\quad
 \text{the same quadratic current at depth `d+2-q`}.
\]

Therefore an argument that routes each lower depth independently cannot be
correct if it uses only this common-order move family.  Within that
restricted family one would need one of:

1. prove that every relevant quadratic fibre contains a carrier with
   bounded terminal compiler deletion;
2. construct a second resident, owner-exact, upper-transparent packet with
   a non-reflection-symmetric quadratic depth profile, so that the combined
   multiplicity space is full; or
3. prove that the compiler's subset/cap freedom bypasses natural-shadow
   completeness while remaining uniformly bounded inside every fibre.

This trichotomy applies only if one elects to stay in the common-order
subcatalogue.  The actual planted catalogue takes the second route once a
label-attached adjacent coatom-order twist is admitted, so the useful
conclusion is diagnostic rather than a no-go for serial reachability.

## 5. Audit

The finite audit

```text
python3 scratch/audit_coatom_nested_flag_reflection_20260801.py
```

reconstructs the authenticated active row for every `2<=d<=32` and checks,
with full occurrence multiplicity:

* exactly two old-only and two new-only values at every depth;
* unit signed multiplicities;
* point balance at every depth;
* equality of pair-degree changes at reflected depths; and
* the Johnson-square form at depth two.

The audit supports the symbolic proof; it is not the source of the all-`d`
claim.
