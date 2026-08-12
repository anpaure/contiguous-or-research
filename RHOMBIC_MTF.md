# Rhombic strips versus move-to-front OR arrays

This note audits the type-`A` permutahedron construction in Akitaya--
Cardinal--Felsner--Kleist--Lauff, *Facet-Hamiltonicity*
([arXiv:2411.02172](https://arxiv.org/abs/2411.02172)), against the exact
move-to-front and pin-survival formulations of the contiguous-OR problem.

The conclusion is mixed but clean.

* A rhombic strip is exactly the right geometric language for a **flag
  process** through the Boolean lattice.
* The construction in the paper is not a near-width OR construction.  Its
  canonical recursive grouping has `2^(k-1)` chain pieces, whereas the width
  is

  \[
      W(k)=\binom{k}{\lfloor k/2\rfloor}
      \sim 2^k\sqrt{\frac{2}{\pi k}}.
  \]

* An adjacent transposition of a permutation is usually not a move-to-front
  update.  The recursive construction also uses reversed sweeps, which have
  the wrong orientation for last-occurrence dynamics.
* The most obvious interval family supplied by the facet cycle fails the
  exact pin-survival criterion already in the displayed `k=4` example.
* There is nevertheless an exact useful bridge: a near-width, directed
  move-to-front transversal of the flags of a rhombic strip would immediately
  give a near-width OR array.  This is stated below as the flag-compression
  lemma.  The paper proves neither of its two extra hypotheses.

No negative statement below rules out a more global regrouping of the
rhombic strip or the use of arbitrary-mask, block-valued move-to-front
updates.  The obstructions apply to the direct and canonical translations.

## 1. The exact flag translation

For a permutation

\[
   \pi=(\pi_1,\ldots,\pi_k),
\]

write

\[
   P_r(\pi)=\{\pi_1,\ldots,\pi_r\},\qquad 1\le r\le k.
\]

The sets `P_1(pi),...,P_(k-1)(pi)` are the proper facets of the
permutahedron incident with `pi`.  If two permutations differ by swapping
positions `j,j+1`, then their maximal Boolean flags differ only at rank `j`.
This is the rhombus associated with that edge of the permutahedron.

Consequently, a facet-Hamiltonian permutation cycle is a cyclic sequence of
maximal Boolean flags such that, for every proper nonempty set `S`,

\[
   J_S=\{t:S=P_{|S|}(\pi_t)\}
\]

is a nonempty cyclic interval.  At every time there is exactly one active set
of each rank.  In particular, at the middle rank the intervals `J_S` are
pairwise disjoint and partition the time circle.

The paper's rhombic strip records all these intervals simultaneously.  It
also implies that each rank is read as a Johnson-graph Gray cycle.  This is a
strong all-rank compatibility statement, but it is not yet the compatibility
required by an OR array.

## 2. Adjacent transposition is not move-to-front

If the last-occurrence state of an OR array is the singleton ordered
partition `pi`, appending the singleton `{x}` changes it to

\[
   \operatorname{mtf}_x(\pi)
    =(x,\pi_1,\ldots,\widehat{x},\ldots,\pi_k).
\]

Appending a set with more than one element creates one tied first block; it
does not produce another permutation state.

### Lemma 1 (singleton-state transition test)

For two distinct permutations `pi,sigma`, one singleton array entry changes
the state from `pi` to `sigma` if and only if

\[
   \sigma=\operatorname{mtf}_x(\pi)
\]

for some element `x`.  Equivalently, `x` is first in `sigma` and the relative
order of every pair of elements other than `x` is unchanged.

In particular, an adjacent transposition at positions `j,j+1` is a
move-to-front transition only when `j=1`.

#### Proof

A singleton update gives the displayed move-to-front formula.  Conversely,
that formula is realized by appending `{x}`.  A nontrivial move-to-front
operation changes the first element.  An adjacent transposition below the
first position does not, so it cannot be such an operation.  At positions
`1,2`, updating the old second element realizes the swap.  QED.

For example, the paper's `k=4` cycle contains

```text
2134 -> 2314,
```

which swaps positions two and three and is not an MTF transition.  Thus the
permutation cycle cannot simply be read as the suffix-state walk of an OR
array.

## 3. Front fans are the exact local common object

Let `x` occupy position `j` of `pi`, and let

\[
   \sigma=\operatorname{mtf}_x(\pi).
\]

Moving `x` left by `j-1` adjacent transpositions traces a stack of rhombi.
The two boundary flags satisfy

\[
  P_r(\sigma)=
  \begin{cases}
     \{x\}\cup P_{r-1}(\pi),&1\le r<j,\\
     P_r(\pi),&j\le r\le k.
  \end{cases}                                      \tag{3.1}
\]

Every Boolean vertex in this stack lies on one of the two boundary flags.
Call such a stack, oriented from `pi` to `sigma`, a **front fan**.  It is the
precise local overlap between a rhombic strip and a singleton MTF update.

The reverse traversal is a back fan.  It is not one MTF update.  Restoring
the old singleton order generally needs all `j-1` earlier elements to be
updated.  Arbitrary-mask MTF can coarsen those elements into one block, but it
does not recover the missing lower prefixes of the old maximal flag.

## 4. Exact countercount for the paper's canonical recursion

Let `P_k` be the facet-Hamiltonian path used in the paper.  Its recursion is

* one lifted copy of `P_(k-1)`;
* one connector `Q_k` that moves the new element from the back to the front;
* one reversed lifted copy of `P_(k-1)`.

Regard every recursively occurring connector `Q_j` as one fan.  If `g_k` is
the number of these fans in `P_k`, then

\[
   g_1=0,\qquad g_k=2g_{k-1}+1,
\]

and hence

\[
   g_k=2^{k-1}-1.                                  \tag{4.1}
\]

Equivalently, there are `2^(k-j)` occurrences of a `j`-coordinate connector
for every `2<=j<=k`.  The initial flag and the new-facet chains contributed by
all connectors partition the proper nonempty Boolean lattice, because

\[
 (k-1)+\sum_{j=2}^k2^{k-j}(j-1)=2^k-2.             \tag{4.2}
\]

Thus the canonical recursive compression has

\[
   1+g_k=2^{k-1}
\]

chain pieces.  Relative to the width this is

\[
  \frac{2^{k-1}}{W(k)}
     \sim \sqrt{\frac{\pi k}{8}},                  \tag{4.3}
\]

which diverges.  Moreover, the reversed recursive copy reverses the
orientations of its inherited fans, so not all of these pieces are joined in
the direction required by MTF dynamics.

Equation (4.3) is a countercount to the **canonical fan grouping**, not a
lower bound against every possible regrouping of the strip.  A genuinely new
global selection would have to merge almost all of these short recursive
pieces and simultaneously repair their directions.

The pieces are not a hidden symmetric-chain decomposition.  A connector on
`j` free coordinates in a context with `a` already-forced leading elements
occupies ranks

\[
   a+1,a+2,\ldots,a+j-1.
\]

It is symmetric in the full `k`-cube only in the special case
`2a+j=k`.  The recursion has many contexts not satisfying this equation.

## 5. The native facet intervals fail pin survival

A second tempting translation is to use the facet-activity interval `J_S` as
the proposed witness interval for `S`.  The exact pin theorem makes the
failure transparent.

Fix a coordinate `b`, and define legal times against all targets omitting
`b` by

\[
  Z_b=[L]\setminus\bigcup_{S:\,b\notin S}J_S.
\]

### Lemma 2 (legal times in a flag path)

For the facet-activity intervals of any permutation flag path,

\[
   Z_b=\{t:\pi_t(1)=b\}.                            \tag{5.1}
\]

#### Proof

If `pi_t(1)=b`, every nonempty active prefix contains `b`, so no active
negative interval excludes `t` from `Z_b`.  If `pi_t(1)=a` with `a!=b`, the
active singleton `{a}` omits `b`; its interval contains `t`, so `t` is not
legal.  QED.

Therefore the facet intervals satisfy the exact pin-survival test if and only
if

\[
  \text{for every }S\text{ and every }b\in S,
  \text{ some permutation in }J_S\text{ begins with }b.       \tag{5.2}
\]

Facet-Hamiltonicity asserts only that `J_S` is connected.  It does not assert
(5.2).

The displayed `k=4` construction in the paper gives an explicit failure.
The two permutations for which `{1,3}` is the rank-two prefix are

```text
3124, 3142.
```

Both begin with `3`.  Hence

\[
   J_{\{1,3\}}\cap Z_1=\varnothing.
\]

By the exact pin-survival theorem, no array can realize all the native facet
intervals simultaneously.  This is a failure of the interval assignment,
not a proof that the same rhombic strip cannot support some completely
different interval assignment.

### Corollary 3 (root-complete flag paths)

Suppose a permutation flag **path** has property (5.2), also with
`J_[k]` taken to be the whole path.  Then the singleton word

\[
   \pi_1(1),\pi_2(1),\ldots,\pi_L(1)
\]

is a universal contiguous-OR word.

Indeed, while `S` is an active prefix the first element never lies outside
`S`, and (5.2) says that every element of `S` occurs.  Thus the OR over the
activity interval is exactly `S`.  This gives a precise strengthening of
facet-Hamiltonicity that would imply an OR construction.  The recursive path
of the paper is not root-complete, as the `k=4` example shows.

## 6. The exact flag-compression lemma

The most useful positive bridge is the following.

### Theorem 4 (directed flag-compression lemma)

Let

\[
  \pi^{(1)},\pi^{(2)},\ldots,\pi^{(N)}
\]

be permutations of `[k]`.  Suppose:

1. every nonempty subset of `[k]` is a prefix of at least one
   `pi^(i)`; and
2. for each `2<=i<=N` there is an element `x_i` such that

   \[
       \pi^{(i)}=\operatorname{mtf}_{x_i}(\pi^{(i-1)}).
   \]

Then

\[
   \nu(k)\le N+k-1.                                 \tag{6.1}
\]

#### Proof

Initialize the recency order `pi^(1)` by appending its elements in reverse
order.  Then append the singleton entries

\[
   x_2,x_3,\ldots,x_N.
\]

The recency state after the `i`th selected flag is exactly `pi^(i)`.  Its
suffix ORs are its prefix sets, so hypothesis 1 covers the Boolean lattice.
The initialization costs `k` entries and the transitions cost `N-1`.  QED.

### Rhombic-strip transversal form

For a facet-Hamiltonian rhombic strip, choose times

\[
   t_1<t_2<\cdots<t_N
\]

in its cyclic or linear order.  Theorem 4 applies if

* the chosen times hit every activity interval `J_S`; and
* consecutive chosen flags are related by a directed front fan, equivalently
  by the MTF equation in hypothesis 2.

For `k=2m`, if `N=W(k)`, the first condition forces exactly one chosen time
in each of the `W(k)` disjoint middle-set activity blocks.  Hence the sharp
rhombic target is:

> choose one representative flag from every middle block so that all other
> facet intervals are hit and the representatives form a directed MTF walk.

A choice of

\[
   N=W(k)+o(W(k))
\]

with only `o(W(k))` missed sets would also suffice after appending the missed
sets literally.  This would prove

\[
   \nu(k)=(1+o(1))W(k).
\]

The average size of a middle activity block in the paper's full cycle is

\[
   \frac{2^k-2}{W(k)}
     \sim \sqrt{\frac{\pi k}{2}}.
\]

Thus this transversal would be a genuine `Theta(sqrt(k))` compression of the
facet cycle.  Neither the all-facet hitting condition nor the directed-MTF
condition follows from the rhombic-strip axioms or from the recursion in the
paper.

### Geometric formulation

Equivalently, seek `W(k)+o(W(k))` meridional flags in the cylindrical
rhombic strip such that

1. their union contains all but `o(W(k))` Boolean vertices; and
2. every consecutive pair bounds a directed front fan.

This is the cleanest way to import the rhombic-strip geometry into the
MTF--SCD program.  It is stronger than interleaved Gray codes and weaker than
asking the entire `2^k-2`-step facet cycle to be an MTF walk.

## 7. Relation to ordered SCDs and witness intervals

The rhombic strip by itself supplies one cyclic family of maximal flags.  It
does **not** supply:

* a width-sized symmetric-chain decomposition carried by selected flags;
* the second, orthogonal endpoint-chain decomposition;
* triangular endpoint orders; or
* legal coordinate pins.

If Theorem 4's hypotheses hold, these issues disappear because the resulting
array is already real: choosing one suffix witness for each target produces
the ordered endpoint decompositions and pins automatically.  Without the MTF
walk, assigning every set to a selected containing flag produces only one
chain cover.  Symmetry, an orthogonal second cover, endpoint order, and pin
survival remain additional conditions.

The arbitrary-mask MTF--SCD theorem in `GLOBAL_MTF_SCD_HANDOFF.md` is more
general than Theorem 4: its states may be ordered partitions with tied blocks,
and an assigned SCD need only occur as subchains of their prefix chains.
Consequently, the singleton obstructions here do not disprove that broader
route.  They identify exactly what extra theorem is needed to make the
specific rhombic-strip construction useful.

## 8. Audited verdict

The paper contributes a serious big-picture object: one planar structure
simultaneously organizes Gray codes in every Boolean rank.  It therefore
deserves to remain in the handoff as a possible host geometry for the global
construction.

What it does **not** currently provide is a width-scale OR array:

\[
 \text{facet-Hamiltonian rhombic strip}
 \;
 \not\Longrightarrow
 \;
 \text{near-width move-to-front tour}.
\]

There are three precise missing implications:

1. compress the `2^(k-1)` canonical recursive chain pieces to
   `W(k)+o(W(k))` selected flags;
2. orient the jumps between selected flags as genuine MTF/front-fan moves;
3. cover all sets with the selected flags, or replace the native facet arcs
   by a different interval family satisfying pin survival.

The directed flag-compression lemma isolates a mathematically sharp target.
Proving it for these recursive strips, or constructing a different rhombic
strip with such a transversal built in, would be genuinely new progress
toward the constant-one conjecture.  The existing facet-Hamiltonian theorem
alone does not do so.
