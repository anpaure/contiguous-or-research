# The exact one/two-splice neighborhood of the 24 `Q_6` seeds has no escape

## Status

The lift-fork obstruction shows that none of the `24` current union-perfect
`Q_6` pairs can be repaired merely by choosing Shearer--Kleitman modes per
chain.  This note tests the next finite escape: first modify the `Q_6`
symmetric chains by one or two exact nonlocal splices.

The search is negative for the explicitly defined complete move class in
Section 1.

* Every seed has exactly four nontrivial cyclic splices: two in each
  decomposition.
* All four are three-chain upper-tail rotations.  There are no legal
  two-chain crossovers and no bounded middle-segment rotations.
* Every one-splice state fails almost orthogonality.
* Every state obtained from two distinct splices also fails almost
  orthogonality.

In fact the four splices commute and generate a Boolean four-cube.  Every
one of its `15` noninitial states fails almost orthogonality.  Each generator
has a private two-mask intersection witness that persists under every
combination of the other three generators.

Thus this switch neighborhood cannot contain an almost-orthogonal,
union-perfect, fork-free pair.  The result does not exclude more general
rechainings that are not cyclic rotations of an existing rank segment.

## 1. Exact switch class

Let an SCD of `Q_6` be given.  Write `C_i(r)` for the member of chain `C_i`
at rank `r`, when present.

### 1.1 Bounded cyclic segment splice

Fix ranks

\[
 \ell<h
\]

and distinct chains

\[
 C_{i_0},C_{i_1},\ldots,C_{i_{t-1}}
\]

that all span ranks `ell,ell+1,h,h+1`.  Suppose cyclic indices satisfy

\[
 C_{i_s}(\ell)\lessdot C_{i_{s+1}}(\ell+1),
\qquad
 C_{i_{s+1}}(h)\lessdot C_{i_s}(h+1).
\tag{1.1}
\]

Replace, in chain `C_(i_s)`, its segment of ranks

\[
 \ell+1,\ldots,h
\]

by the corresponding segment of `C_(i_(s+1))`.

The first condition in (1.1) joins the old head to the rotated segment; the
second joins that segment back to the old tail.  Every new edge is a cube
cover.  Each chain retains its original bottom and top ranks, so symmetry is
preserved, and rotating disjoint segments preserves the partition.

### 1.2 Equal-radius cyclic tail splice

If all involved chains have the same bottom and top ranks, the upper tails
strictly above one cut rank `ell` may be rotated cyclically under the single
condition

\[
 C_{i_s}(\ell)\lessdot C_{i_{s+1}}(\ell+1).
\tag{1.2}
\]

The endpoints are permuted among equal rank intervals, so every resulting
chain is still symmetric.

Both definitions include two-chain switches when `t=2`.  A legal
permutation at fixed boundaries decomposes into disjoint directed cycles;
the search enumerates every simple directed cycle.  Consequently radius one
contains every one-component splice in this class, and radius two contains
every composition of two such components, even when the intermediate pair
is not orthogonal.

## 2. Exhaustive neighborhood counts

The verifier reconstructs the `24` seeds from the original `84` good
`Q_4` pairs, enumerates all switches in Section 1, validates every resulting
SCD directly, and evaluates the pair.

For every seed the combined pair has exactly four generators.  The complete
radius profile is

\[
\begin{array}{c|c|c|c}
\text{number of distinct splices}&\text{states per seed}
 &\text{state occurrences over 24}&\text{almost orthogonal}\\ \hline
1&4&96&0\\
2&6&144&0\\
3&4&96&0\\
4&1&24&0.
\end{array}
\tag{2.1}

All `360` noninitial pair occurrences are distinct across the `24` seeds.
In particular, the requested one/two-splice neighborhood consists of

\[
 96+144=240
\]

failed states.

Since none is almost orthogonal, none reaches the later tests of central
union injectivity, fork-freeness, or the relaxed `Q_8` Hall graph.

## 3. The four generators in a representative seed

For seed zero, the four tail rotations are as follows.  A slash separates
the three chains rotated in one directed cycle.

### `D`, cut after rank three

\[
\begin{aligned}
 2-26-256-2356-23456\;/\;
 4-46-456-2456-12456\;/\;
 3-36-356-3456-13456
\end{aligned}
\]

rotates the tails to

\[
\begin{aligned}
 2-26-256-2456-12456\;/\;
 4-46-456-3456-13456\;/\;
 3-36-356-2356-23456.
\end{aligned}
\]

Its private persistent cross-intersection is

\[
 \{456,3456\}.
\tag{3.1}
\]

### `D`, cut after rank two

\[
 25-235-2345\;/\;45-245-1245\;/\;35-345-1345
\]

rotates to

\[
 25-245-1245\;/\;45-345-1345\;/\;35-235-2345,
\]

with private witness

\[
 \{45,345\}.
\tag{3.2}
\]

### `E`, cut after rank two

\[
 1-14-134-1345-13456\;/\;
 2-12-124-1245-12456\;/\;
 3-13-123-1235-12356
\]

rotates to

\[
 1-14-124-1245-12456\;/\;
 2-12-123-1235-12356\;/\;
 3-13-134-1345-13456,
\]

with private witness

\[
 \{12,123\}.
\tag{3.3}
\]

### `E`, cut after rank three

\[
 16-146-1346\;/\;26-126-1246\;/\;36-136-1236
\]

rotates to

\[
 16-146-1246\;/\;26-126-1236\;/\;36-136-1346,
\]

with private witness

\[
 \{126,1236\}.
\tag{3.4}
\]

The other `23` seeds have the same four-generator architecture after
coordinate relabelling.

## 4. Persistent-witness obstruction

### Theorem 4.1

For each seed and each of its four splice generators `g`, there is a pair of
nonextreme masks `P_g={x_g,y_g}` such that every state using `g`, regardless
of which subset of the other three generators is also used, has a cross-pair
of chains intersecting in both `x_g,y_g`.

Consequently every nonempty splice subset violates almost orthogonality.

#### Proof

For one seed there are only `2^4` states.  The verifier constructs each SCD
from the chain rotation, then independently enumerates every cross-pair of
chains and every pair of masks in an illegal intersection.  For a fixed
generator it intersects these violation-pair catalogs over the eight states
containing that generator.  The intersection is nonempty.

This check is repeated for all four generators and all `24` seeds, producing

\[
 4\cdot24=96
\]

private persistent witnesses.  For seed zero they are exactly
(3.1)--(3.4).

The certificate is finite and direct: membership of two masks in each
displayed chain pair is the complete almost-orthogonality violation.  QED.

Structurally, a cyclic tail rotation uses an unused matching cycle at one
rank boundary, but one rotated tail enters an opposing chain that already
shares the adjacent two-mask segment `P_g`.  The other three rotations use
disjoint tail catalogs and cannot separate this private pair.

## 5. Strategic consequence

The negative result is stronger than “the first switch was chosen badly.”
Within this exact move language:

* every legal nontrivial generator immediately breaks almost orthogonality;
* composing generators never repairs all private violations;
* therefore union perfection and fork removal are unreachable.

A successful escape must change the move language in one of two ways.

1. **Coupled cross-decomposition rechain.**  Alter a `D` tail and the
   opposing `E` witness chain in one atomic move, so the private double
   intersection is removed as it is created.
2. **Non-rotational path replacement.**  Replace a larger chain packet by a
   new symmetric path cover not obtainable by rotating existing rank
   segments.  This can change the endpoint/singleton ownership responsible
   for the lift fork.

Independent cyclic splices of the existing chain paths, even four at once,
cannot escape any current seed.

## 6. Correct ledger

**Proved by exhaustive finite verification**

* all simple two-chain tail and bounded-segment switches are included;
* all multi-chain cyclic segment and equal-radius tail rotations are
  included;
* each seed has exactly four generators, all three-chain tail rotations;
* every one- and two-generator state fails almost orthogonality;
* all `15` nonempty generator subsets fail, each by a persistent private
  witness.

**Not proved**

* impossibility of an arbitrary symmetric rechain on `Q_6`;
* impossibility of a coupled atomic move changing both decompositions;
* nonexistence of a union-perfect fork-free OSCD pair outside this
  neighborhood.

The finite escape attempt is therefore closed: the next move must be
coupled across the two decompositions or genuinely replace a larger path
packet.
