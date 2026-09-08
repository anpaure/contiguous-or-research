# Nested-invariance composition of the syndrome `Q_4` braid bank

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

The syndrome-suspended `Q_4` braid can be composed through genuinely
overlapping coordinate transpositions.  The composition is not the naive
Cartesian product of all pair bits: two overlapping layers already impose
an exact statewise compatibility condition.  Nevertheless, a triangular
choice of the pair bits retains **linear information rate**.

Let `P` be the standard rooted isometric `C_(2h)` in `Q_h`, let `K_0` be
the syndrome-cycle label space, and let

\[
             \tau_j=(a_j\ b_j),\qquad
             \delta_j=e_{a_j}+e_{b_j}\in K_0                 \tag{0.1}
\]

be any ordered list of equal-syndrome coordinate transpositions.  Put

\[
             D_j=\langle\delta_j,\delta_{j+1},\ldots,
                         \delta_L\rangle.                       \tag{0.2}
\]

For every `j`, choose a bit field

\[
             \epsilon_j:K_0/D_j\longrightarrow\mathbb F_2     \tag{0.3}
\]

and define recursively

\[
 \sigma_k^{(0)}=1,
 \qquad
 \sigma_k^{(j)}=\tau_j^{\epsilon_j(k)}\sigma_k^{(j-1)}.        \tag{0.4}
\]

Then, after every layer `j`,

\[
             \mathcal F^{(j)}
             =\{\sigma_k^{(j)}P+k:k\in K_0\}                   \tag{0.5}
\]

is a literal exact factor of `Q_h` into isometric `C_(2h)`'s.  Layer `j`
is an owner-level union of the old/new shores on the actual cycle-label
pairs

\[
                         \{k,k+\delta_j\}.                       \tag{0.6}
\]

At every phase it either fixes the two owners or exchanges them.  Thus no
word-permutation surrogate is being used.

All intermediate factors have one common owner phase colouring.  Their
phase-zero and antipodal phase-`h` ports are fixed pointwise.  They admit
the same common-phase `C_(2n)` suspension for every `n>=h`, on one common
suspended carrier.  This does not assert that the carrier by itself spans
all of `Q_n`.

In the standard parity-alternating syndrome factor, one equal-column class
has size `s=h/2`.  Taking the adjacent chain on this class gives

\[
 r=s-1,qquad N=|K_0|={2^h\over2h},                               \tag{0.7}
\]

and exactly

\[
 \boxed{
 B=\sum_{j=1}^r|K_0/D_j|
   =N\sum_{t=1}^r2^{-t}
   =(1-2^{-r})N}                                                  \tag{0.8}
\]

independent Boolean parameters.  The resulting rooted factor fields are
all distinct, so there are at least

\[
                         2^{(1-2^{-r})N}                          \tag{0.9}
\]

literal exact factor states.  This is asymptotically one information bit
per syndrome cycle, despite the fact that consecutive transpositions share
coordinate directions.

A fixed adjacent sorting word can also be installed before the final
chain.  On each coset of the full displacement space, its switch values can
be chosen to produce an arbitrary direction permutation.  Hence the
construction is a genuine owner-level sorting-network composition, with a
precisely quantified correlation between different cycle labels.

The correlation is necessary.  For two adjacent transpositions

\[
              \tau_1=(a\ b),\qquad \tau_2=(b\ c),                \tag{0.10}
\]

the naive sixteen pair-bit states on one
`<delta_1,delta_2>`-plane reduce to exactly ten legal states.  If the first
bit differs between the two `delta_2`-pairs, then the second bit is forced
to vanish on the entire plane.  Thus fully independent pair bits do not
compose, but nested invariance loses no more than a constant total fraction
of one bit per cycle.

This closes the owner/factor composition gate for the braid bank.  It does
not prove a protected shadow-collar theorem or coefficient one: the braid
is designed to change consecutive direction windows, and no equality of
the resulting `X/Y` shadow ledgers is asserted.

## 1. Syndrome-cycle framework

Let

\[
                         V=\mathbb F_2^h                           \tag{1.1}
\]

and let

\[
                         \Psi:V\longrightarrow A                  \tag{1.2}
\]

be a syndrome map for which the rooted cycle

\[
 P=(p_0,p_1,\ldots,p_{h-1},
       \mathbf1+p_0,\ldots,\mathbf1+p_{h-1})                     \tag{1.3}
\]

is a syndrome transversal.  Here

\[
 p_0=0,qquad p_i=e_0+\cdots+e_{i-1}.                             \tag{1.4}
\]

Put `K=ker(Psi)`.  Let `G` be a group of coordinate permutations
preserving every syndrome column:

\[
                         \Psi\sigma=\Psi\qquad(\sigma\in G).      \tag{1.5}
\]

Its displacement space is

\[
                         D_G=\sum_{\sigma\in G}
                               \operatorname{im}(\sigma-I)
                         \subseteq K.                              \tag{1.6}
\]

Assume `1 notin D_G`.  Choose a linear functional

\[
 \eta:K\longrightarrow\mathbb F_2,qquad
 \eta(\mathbf1)=1,qquad \eta(D_G)=0,                            \tag{1.7}
\]

and put

\[
                         K_0=\ker\eta.                             \tag{1.8}
\]

Then

\[
                         K=K_0\oplus\langle\mathbf1\rangle,
 \qquad                  D_G\subseteq K_0,                         \tag{1.8a}
\]

and `K_0` is `G`-invariant.

For a row field `sigma:K_0 -> G`, define rooted cycles

\[
                         C_k=\sigma_kP+k.                          \tag{1.9}
\]

At phase `i` in the first half, the owner in row `k` is

\[
                         x_i(k)=\sigma_kp_i+k.                     \tag{1.10}
\]

The antipodal owner is `1+x_i(k)`.  Relative to the standard phase class,
put

\[
 T_i(k)=k+d_i(\sigma_k),
 \qquad d_i(\sigma)=\sigma p_i+p_i.                              \tag{1.11}
\]

Then

\[
                         x_i(k)=p_i+T_i(k).                        \tag{1.12}
\]

Thus the cycles in (1.9) form an exact owner factor if and only if every
`T_i` is a permutation of `K_0`.  This is the phasewise Latin criterion.
Also `d_i(sigma) in D_G`, so the owner colouring

\[
 c(p_i+k)=i+h\eta(k)\pmod {2h}                                   \tag{1.13}
\]

is cyclic on every exact factor of the form (1.9).

The proof below does more than invoke (1.11): it writes every new owner as
an old owner in the same literal two-cycle support.

## 2. One owner-level layer over a nonconstant row field

Fix an equal-syndrome transposition

\[
                         \tau=(a\ b),qquad
                         \delta=e_a+e_b\in D_G.                   \tag{2.1}
\]

Say that a field `sigma:K_0 -> G` is `delta`-invariant when

\[
                         \sigma_{k+\delta}=\sigma_k                \tag{2.2}
\]

for every `k`.  Let `epsilon:K_0 -> F_2` also be `delta`-invariant, and
put

\[
                         \sigma'_k=\tau^{\epsilon(k)}\sigma_k.    \tag{2.3}
\]

### Theorem 2.1 (literal pair-layer lemma)

If `F_sigma={sigma_kP+k}` is exact and `sigma,epsilon` satisfy (2.2),
then `F_(sigma')` is exact.  More precisely, for each pair
`{k,k+delta}` the two new cycles partition exactly the same `4h` owners as
the two old cycles.  At each common phase the new shore either fixes the
two old owners or exchanges them.

#### Proof

For a phase `i`, let

\[
 \alpha_i(k)
 =\mathbf1\{\sigma_kp_i\text{ contains exactly one of }a,b\}.    \tag{2.4}
\]

Transposing `a,b` in a set adds `delta` exactly in this case.  Therefore

\[
 x'_i(k)=x_i(k)+\epsilon(k)\alpha_i(k)\delta.                    \tag{2.5}
\]

The `delta`-invariance of `sigma` gives

\[
 x_i(k+\delta)=x_i(k)+\delta,
 \qquad
 \alpha_i(k+\delta)=\alpha_i(k).                                \tag{2.6}
\]

The same invariance for `epsilon` now gives, on each pair:

* if `epsilon=0`, both phase owners are fixed;
* if `epsilon=1` and `alpha_i=0`, both are fixed;
* if `epsilon=1` and `alpha_i=1`, the two owners are exchanged.

Hence the old and new shores agree phase by phase as literal owner sets.
Their antipodal owners agree after adding `1`.  This proves the `4h`-owner
identity on every pair and proves exactness globally.

Every new cycle is the coordinate image `tau sigma_k P+k`, so its
direction word is a permutation repeated twice and it is an isometric
`C_(2h)`.  The exchange occurs within one common phase, so (1.13) remains
cyclic.  Finally, `p_0=0` and `1+p_0=1` are fixed by every coordinate
permutation, hence the phase-zero owner `k` and phase-`h` owner `k+1` are
fixed pointwise.  \(\square\)

If `epsilon=1`, the owner-overlap component really contains the two old
and two new cycles.  Between the positions of `sigma_k^{-1}a` and
`sigma_k^{-1}b` in the base direction order, `alpha_i=1`; outside that
arc it is zero.  Thus each new row uses owners from both old rows.  The
component is not a formal relabelling of one cycle.

### Lemma 2.2 (the eight-tail budget survives composition)

On one active pair component, the old and new global successor maps differ
at exactly eight owner tails, independently of the distance between
`sigma_k^{-1}a` and `sigma_k^{-1}b` in the current direction order.

#### Proof

At phase `i`, the new shore assigns the two owners to the opposite rows
exactly when `alpha_i=1`.  If `alpha_i=alpha_(i+1)`, both endpoints of the
next edge are assigned to the same old row as each other, so the physical
successor edge is unchanged.  If `alpha_i != alpha_(i+1)`, the next edge
crosses between the two translated rows, so both owner tails of the pair
change successor.

In one `h`-phase half, the indicator that a prefix contains exactly one of
the two transposed directions changes exactly twice, once at each of those
directions.  The antipodal half repeats the same two changes.  There are
therefore four phase boundaries, with two changed tails at each boundary,
for a total of eight. \(\square\)

Thus a later noncommuting layer may exchange a long phase interval between
the two rows, but it remains a bounded-seam braid.  This distinction is
important: owner transport can be nonlocal while the successor edit budget
stays exactly that of the original `Q_4` component.

## 3. Arbitrarily many overlapping layers

Take the ordered transposition list (0.1), allowing the coordinate pairs
to overlap and allowing a transposition to recur.  Define the nested
spaces (0.2).  Regard each `epsilon_j` in (0.3) as a function on `K_0`
which is invariant under every vector of `D_j`.

### Theorem 3.1 (nested-invariance braid composition)

Every intermediate family (0.5) is an exact isometric factor.  Layer `j`
is a literal union of `delta_j`-pair owner trades as in Theorem 2.1.  All
intermediate factors share the phase colouring (1.13) and the pointwise
phase-zero/phase-`h` ports.

#### Proof

Before layer `j`,

\[
 \sigma_k^{(j-1)}
 =\tau_{j-1}^{\epsilon_{j-1}(k)}\cdots
   \tau_1^{\epsilon_1(k)}.                                      \tag{3.1}
\]

For `l<j`, nestedness gives

\[
                         D_j\subseteq D_l.                        \tag{3.2}
\]

Consequently every previous bit `epsilon_l` is invariant under `D_j`.
Equation (3.1) implies

\[
                         \sigma_{k+d}^{(j-1)}
                         =\sigma_k^{(j-1)}qquad(d\in D_j).       \tag{3.3}
\]

In particular the current row field is `delta_j`-invariant.  The new bit
is also `delta_j`-invariant because `delta_j in D_j`.  Apply Theorem 2.1.
Induction on `j` proves exactness and the literal pair-support assertion at
every layer.  Common phase and the two fixed ports are inherited from the
same theorem.  \(\square\)

The theorem is insensitive to noncommutativity.  In particular
`tau_j,tau_(j+1)` may share one coordinate; equation (3.3), not commutation,
is what keeps the next physical overlay two-cycle local.

### Exact parameter count

The functions `epsilon_j` may be chosen independently on the quotient
`K_0/D_j`.  Hence the construction has

\[
                         B=\sum_{j=1}^L|K_0/D_j|                  \tag{3.4}
\]

Boolean parameters.  Formula (3.4) counts choices of tied physical
`delta_j`-pair components: one bit on a `D_j`-coset switches every
`delta_j`-pair in that coset together.  It does not incorrectly count those
pairs as independent after future layers have been prescribed.

## 4. An overlapping adjacent chain with one bit per cycle

Let an equal-syndrome coordinate class be

\[
                         E=\{a_0,a_1,\ldots,a_r\}.                \tag{4.1}
\]

Use

\[
 \tau_j=(a_{j-1}\ a_j),
 \qquad
 \delta_j=e_{a_{j-1}}+e_{a_j}qquad(1\le j\le r).               \tag{4.2}
\]

Consecutive transpositions share the direction `a_j`.  The vectors
`delta_1,...,delta_r` are linearly independent: in a vanishing linear
combination, the coefficient of `e_(a_0)` first forces the coefficient of
`delta_1` to vanish, and induction along the path forces all coefficients
to vanish.  Thus

\[
                         \dim D_j=r-j+1.                           \tag{4.3}
\]

Let `d=dim K_0` and `N=2^d`.  Equations (3.4) and (4.3) give

\[
 B=\sum_{j=1}^r2^{d-r+j-1}
  =2^d(1-2^{-r})=(1-2^{-r})N.                                   \tag{4.4}
\]

### Proposition 4.1 (the chain states are distinct)

The `2^B` parameter choices in the adjacent-chain construction give
`2^B` distinct rooted exact factors.

#### Proof

For one row `k`, the final coordinate permutation is

\[
 \sigma_k=\tau_r^{e_r}\tau_{r-1}^{e_{r-1}}\cdots\tau_1^{e_1},
 \qquad e_j=\epsilon_j(k).                                      \tag{4.5}
\]

The map `(e_1,...,e_r) -> sigma_k` is injective.  Indeed all factors
except `tau_r` fix `a_r`, so

\[
 \sigma_k(a_r)=
 \begin{cases}
  a_r,&e_r=0,\\
  a_{r-1},&e_r=1.
 \end{cases}                                                     \tag{4.6}
\]

This recovers `e_r`.  Multiplying by `tau_r^{e_r}` on the left reduces to
the same statement with `r-1`, proving injectivity by induction.

If two global parameter choices differ, choose a row `k` on which their
bit vectors differ.  Their `sigma_k` differ by the preceding paragraph.
The phase-zero owner of row `k` is always `k`, so no relabelling of rows can
identify the two rooted factors.  Hence the factors are distinct. \(\square\)

For the standard parity-alternating syndrome presentation with `h=2^a`,
the even coordinate positions form one equal-column class of size

\[
                         s={h\over2}.                              \tag{4.7}
\]

Here

\[
 \dim K_0=h-a-1,
 \qquad
 N=2^{h-a-1}={2^h\over2h},
 \qquad
 r={h\over2}-1.                                                  \tag{4.8}
\]

Substitution into (4.4) proves (0.8)--(0.9).  The number of physical
braid layers is `r`, and every two consecutive layers overlap in one cube
direction.  In the reference order one may take `a_j=2j`; hence each first
use of `(a_(j-1) a_j)` is precisely a distance-two syndrome `Q_4` braid.
After previous noncommuting layers its exchanged owner interval can be
longer, but Lemma 2.2 keeps its physical successor difference at eight
tails per active two-cycle component.

## 5. A literal sorting-network extension

The same theorem compiles a fixed coordinate sorting word.  Let
`E={a_0,...,a_r}` and let `s_j=(a_(j-1) a_j)`.  There is a fixed list

\[
                         \mathcal W=(\omega_1,\ldots,\omega_M),   \tag{5.1}
\]

of adjacent transpositions such that every permutation in `S_E` is a
subproduct

\[
                         \omega_M^{b_M}\cdots\omega_1^{b_1}.     \tag{5.2}
\]

One may take the chronological reverse of the triangular bubble word

\[
 (s_1)(s_2s_1)\cdots(s_rs_{r-1}\cdots s_1),
 \qquad M={r(r+1)\over2}.                                       \tag{5.3}
\]

For completeness, the subword assertion follows by insertion induction.
After a permutation of `a_0,...,a_(t-1)` has been formed, the block
`s_t s_(t-1)...s_1` can move `a_t` to any prescribed one of the `t+1`
positions; then apply the induction hypothesis to the remaining symbols.
Reversing the chronological list changes (5.3) into the left-product
convention (5.2).

Append to `W` the adjacent chain

\[
                         s_1,s_2,\ldots,s_r.                      \tag{5.4}
\]

Apply Theorem 3.1 to the entire list.  The appended displacements span

\[
                         D=\langle\delta_1,\ldots,\delta_r\rangle.\tag{5.5}
\]

Therefore every bit belonging to the earlier sorting word is required to
be constant on `D`-cosets.  Set every appended-chain bit to zero.  On each
coset `Q in K_0/D`, choose independently a subword of (5.3) producing an
arbitrary prescribed permutation `pi_Q in S_E`.  The resulting exact
factor has

\[
                         \sigma_k=\pi_{k+D}.                       \tag{5.6}
\]

Thus arbitrary direction permutations are independently programmable on
the `|K_0/D|` owner blocks, and every intermediate comparator is a literal
owner-level `delta`-pair shore switch.  This is a sorting-network theorem,
not merely the assertion that the final direction words happen to be
permutations.

The appended chain may instead be activated.  Its fields contribute the
linear entropy (4.4).  Consequently the same compiled bank has both:

1. a universal coordinate-permutation menu on every full-displacement
   owner block; and
2. an explicit subfamily with `(1-2^{-r})N` independent bits.

It does not give arbitrary, mutually independent `S_E` values on all `N`
rows.  That stronger menu would contain `N log_2(s!)` bits, whereas the
present linear-rate theorem asserts only `Theta(N)` bits.  The correlations
are physical and are quantified by the suffix spaces `D_j`.

## 6. The exact two-layer obstruction to naive independence

The nested condition is not a proof artefact.  Consider three
equal-syndrome coordinates occurring in the base prefix order as

\[
                         a,\ b,\ c,                                \tag{6.1}
\]

and put

\[
 \tau_1=(a\ b),\quad \delta_1=e_a+e_b,
 \qquad
 \tau_2=(b\ c),\quad \delta_2=e_b+e_c.                           \tag{6.2}
\]

Let `epsilon_1` be constant on `delta_1`-pairs and `epsilon_2` constant on
`delta_2`-pairs.  Form

\[
                         \sigma_k
 =\tau_2^{\epsilon_2(k)}\tau_1^{\epsilon_1(k)}.                  \tag{6.3}
\]

Fix a coset of the plane

\[
                         H=\langle\delta_1,\delta_2\rangle.       \tag{6.4}
\]

Write a point of the plane as `(u,v) in F_2^2`, where adding `delta_1`
changes `u` and adding `delta_2` changes `v`.  Pair constancy has the form

\[
                         \epsilon_1(u,v)=A(v),
 \qquad                  \epsilon_2(u,v)=B(u).                    \tag{6.5}
\]

### Theorem 6.1 (ten-state adjacent-layer classification)

The row family `{sigma_kP+k}` is exact on this plane if and only if

\[
 \boxed{
 A(0)=A(1)\quad\hbox{or}\quad B(0)=B(1)=0.}                     \tag{6.6}
\]

Thus exactly ten of the sixteen formal pairs `(A,B)` are legal: eight with
`A` constant and arbitrary `B`, and two with `A` nonconstant and `B=0`.

#### Proof

Consider the phase just after direction `a` and before direction `b`.
The membership pattern on `(a,b,c)` is `100`.  Applying (6.3) changes its
kernel label by

\[
 \epsilon_1\delta_1+\epsilon_1\epsilon_2\delta_2.                \tag{6.7}
\]

Hence its phase map on the plane is

\[
 (u,v)\longmapsto
 (u+A(v),\ v+A(v)B(u)).                                          \tag{6.8}
\]

At the phase after `b` and before `c`, the pattern is `110`.  The first
transposition fixes this set and the second changes it by `delta_2`, so the
phase map is

\[
                         (u,v)\longmapsto(u,v+B(u)),               \tag{6.9}
\]

which is bijective precisely because `B` is a function of `u`, i.e. because
`epsilon_2` is constant on its `delta_2`-pairs.  All other relevant
three-coordinate prefix states are `000` and `111`, on which both maps are
the identity.  Antipodal phases give the same displacement equations.

It remains to classify (6.8).  If `A` is constant zero, the map is the
identity.  If `A` is constant one, it exchanges the two `u`-lines and on
each line optionally translates `v`; it is bijective for every `B`.

Suppose `A(0) != A(1)`.  On the line on which `A=0`, both points are fixed.
On the other line, a value `B(u)=1` sends one point onto a fixed point of
the first line.  Thus bijectivity forces `B(0)=B(1)=0`.  With `B=0`, the
active line simply exchanges its two `u`-coordinates, so the map is
bijective.  This proves (6.6).

The phasewise Latin criterion from Section 1 makes this both necessary and
sufficient for literal owner exactness. \(\square\)

Consequences:

* the independent Boolean product of the two pair banks is false;
* wherever the first field stores a `delta_2`-difference, the second
  overlapping layer has zero capacity;
* retaining arbitrary second-layer bits forces the first field to be
  `span(delta_1,delta_2)`-invariant on that plane; and
* Theorem 3.1 chooses exactly this full-capacity branch recursively.

## 7. Ports, overlays, and common suspension

The construction preserves the following data literally.

1. **Middle owners.** Every intermediate factor partitions every owner of
   `Q_h` exactly once.
2. **Layer overlays.** One active physical component at layer `j` is the
   union of the two old cycles labelled `k,k+delta_j` and the two new
   cycles with those labels.  Both shores have the same `4h` owners.
3. **Common phase.** The owner colouring (1.13) is cyclic on every cycle in
   every layer.
4. **Root ports.** The phase-zero owner of row `k` is always `k`, and its
   antipodal phase-`h` owner is always `k+1`.  These two ports are fixed
   pointwise, not only as an aggregate.
5. **Other phase ports.** For every phase `i`, the whole phase class is
   fixed as an owner set.  A layer only exchanges two row assignments
   inside a `delta_j`-pair.

The common-colour suspension theorem now applies simultaneously.  Given
`n>=h`, append the same `n-h` split directions in every common phase fibre.
Because every factor uses exactly the same owner phase classes, the lifted
owner support is independent of the braid state.  Every lifted row has a
permutation of `n` directions repeated twice and is therefore an isometric
`C_(2n)`.  Thus all factors in Theorem 3.1 possess a common-support,
common-phase suspension on the displayed carrier.  Ambient completion to a
spanning factor of a larger cube is a separate theorem.

What is **not** preserved is equally important.  Consecutive direction
windows, and hence their lower/upper shadow targets, are meant to change.
Common phase does not imply equality of a phase-resolved depth-`H` collar.
No `D_r` port-transversality, `X/Y` rainbow, or coefficient-one balancing
conclusion follows without a separate occurrence calculation.

## 8. Exact implication boundary

Proved:

* a general owner-level composition theorem for any ordered list of
  equal-syndrome transpositions, including noncommuting overlapping ones;
* exact factor legality at every intermediate layer;
* literal two-cycle owner components at every layer;
* common phase, pointwise root/antipode ports, and common suspension;
* an adjacent overlapping chain with
  `(1-2^{-r})|K_0|` independent bits;
* a compiled sorting-word realization of arbitrary direction permutations
  on full-displacement owner blocks; and
* the exact ten-state obstruction to naively independent composition of
  the first two overlapping layers.

Not proved:

* mutually independent arbitrary `S_s` permutations on every individual
  syndrome cycle;
* equality, or small total discrepancy, of the complete protected
  lower/upper collars after the dense braid;
* a parity-complete same-owner double factor coupling two independently
  chosen row fields; or
* the zero-collision/constant-one theorem.

The composition obstruction is therefore no longer the absence of a
literal braid network.  Such a network exists with linear entropy.  The
remaining quantitative problem is to choose its correlated fields so that
the changed owner-resolved shadow occurrences balance all protected depths.
