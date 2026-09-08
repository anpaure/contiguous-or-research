# The `k=17` dead-block split superatlas still has 568 empty colour rows

**Date:** 2026-08-01  
**Status:** exact finite classification, an unconditional extra-cut lower
bound for refinements of the frozen interiors, and a solver-free no-go for
every strategy which splits each initially dead block at most once.  This is
not a no-go for a global owner rethread or for `nu(17)=B(17)`.

## 0. Outcome

The authenticated protected `ML_9` factor was cut at the deterministic
rightmost-greedy protected-gap-avoiding minimum residence transversal emitted
by the cited audit.  Its direct
endpoint atlas has 1,289 deleted rank-eight colours with no seam satisfying
even the relaxed necessary residence test, and 368 physical blocks with no
incoming or outgoing candidate.

The obstruction is broad rather than equivariant or component-local:

* the zero colours occur on five of the seven factor components, with counts
  `748,458,81,1,1`;
* the dead blocks occur on five components, with counts `215,124,27,1,1`;
* the zero set meets 864 cyclic `Z_17` necklace orbits, and no orbit contains
  more than five zero colours.

Every dead block has an internal gap.  Nevertheless, even the following
deliberately impossible superatlas retains

\[
                         \boxed{568}                            \tag{0.1}
\]

of the original zero-colour rows: retain every old endpoint state, add every
endpoint state obtainable from every possible single split of every dead
block, allow incompatible alternatives to coexist, and give every such state
a private block identity.  Since every actual one-split-per-dead-block
strategy is a subatlas, no such strategy can restore the exact `q1` palette by
ordinary seams.

A deterministic best-local split of all 368 dead blocks does remove every
zero physical block and makes every newly cut colour nonzero.  It still leaves
812 of the original zero colours, and its block--colour matching has size only

\[
                         3363/4175.                             \tag{0.2}
\]

Thus the natural repair fixes endpoint topology before it fixes the named
palette.  The next construction must alter more of the bulk or introduce
whole seam sockets; merely splitting the initially dead blocks is impossible.

## 1. Exact classification of the obstruction

The seven original factor components have owner sizes

\[
                 14305,8615,1362,18,4,3,3.                    \tag{1.1}
\]

The zero colours and dead blocks distribute as follows:

\[
\begin{array}{c|rrrrrrr}
\text{component}&0&1&2&3&4&5&6\\ \hline
\text{zero colours}&748&458&81&1&1&0&0\\
\text{dead blocks}&215&124&27&1&0&0&1.
\end{array}                                                    \tag{1.2}
\]

The 1,289 zero masks occupy cyclic necklace orbits with occupancy histogram

\[
\begin{array}{c|rrrrr}
\text{zero masks in orbit}&1&2&3&4&5\\ \hline
\text{number of orbits}&551&223&72&14&4.
\end{array}                                                    \tag{1.3}
\]

In particular, the obstruction is not one broken `Z_17` orbit and cannot be
removed by completing a bounded number of partial rotation orbits.

### 1.1 Raw endpoint degrees

Before residence filtering every zero colour has raw Boolean seams.  Their
raw degree histogram is

\[
\begin{array}{c|rrrrrrrr}
\text{raw degree}&2&4&6&10&12&18&20&30\\ \hline
\text{colours}&281&1&539&7&336&4&100&21.
\end{array}                                                    \tag{1.4}
\]

Thus the 1,289 empty rows are caused by residence correlation, not missing
Johnson endpoint pairs.

For every raw seam, count violations of the relaxed necessary residence
inequalities.  Minimizing lexicographically over all raw seams for a fixed
colour gives

\[
\begin{array}{c|rrrr}
\text{minimum number of violations}&1&2&3&4\\ \hline
\text{colours}&1078&193&17&1.
\end{array}                                                    \tag{1.5}
\]

The more refined best-failure types are

\[
\begin{array}{c|r}
(\text{common},\text{departing},\text{entering})&\text{colours}\\ \hline
(0,0,1)&1018\\
(1,0,0)&60\\
(0,1,1)&116\\
(1,0,1)&77\\
(1,1,1)&15\\
(2,0,1)&2\\
(2,1,1)&1.
\end{array}                                                    \tag{1.6}
\]

So 1,018 rows are only one entering-age failure away from a legal seam.  The
factor is close in a precise local sense, but the missing maturity is spread
over more than a thousand named colours.

### 1.2 Dead-block age signatures

The dead block lengths range from three to 27; none is a singleton and hence
all 368 can be split.  At the 736 oriented block ends, let the age signature
record the numbers of positive coordinates with boundary run length
`1,2,3,at least 4`.

* The 58 oriented ends of the 29 length-three blocks have signature
  `(1,1,7,0)` and seven all-one coordinates.
* Every other oriented dead end has signature `(1,1,1,6)`; the number of
  all-one coordinates depends on its block length.

This explains why the obstruction is not a raw shortage.  Each ordinary end
has six mature coordinates, but the named deleted colour can force the unique
young entering/departing coordinate.

## 2. An extra-cut lower bound

Let `Z` be the set of 1,289 original zero colours.  The authenticated census
over all 24,310 rank-nine owners gives

\[
 \max_{T\in\binom{[17]}9}|\{I\in Z:I\subset T\}|=5.            \tag{2.1}
\]

The complete histogram of the number of `Z`-facets of an owner is

\[
\begin{array}{c|rrrrrr}
\text{number of `Z`-facets}&0&1&2&3&4&5\\ \hline
\text{owners}&14553&8080&1522&144&10&1.
\end{array}                                                    \tag{2.2}
\]

### Theorem 2.1 (at least 65 further cuts in any pure refinement)

Refine the frozen 3,807 blocks by `s` additional internal cuts, without
changing the order or labels of owners inside an original block.  If ordinary
direct seams in the refined endpoint atlas serve every colour in `Z`, then

\[
                             s\ge65.                            \tag{2.3}
\]

#### Proof

Suppose `p` original blocks are touched.  Relative to the original endpoint
atlas, a touched block can change the states at its two old outer owners, and
each new cut exposes its two incident owners.  Hence every changed endpoint
state is supported on a set `E` of owner masks satisfying

\[
                         |E|\le2p+2s\le4s.                     \tag{2.4}
\]

An originally zero colour which acquires a seam must use at least one changed
endpoint state; otherwise that seam was already present.  Therefore every
member of `Z` is a facet of some owner in `E`.  By (2.1),

\[
                         1289\le5|E|\le20s.
\]

Thus `s` is at least `ceil(1289/20)=65`.  \(\square\)

This bound permits recursive cuts and arbitrary coordination between them.
For the narrower face in which every original block is split at most once,
the exact affected-row census is stronger: one baseline split affects at most
nine members of `Z`, so at least

\[
                         \lceil1289/9\rceil=144                \tag{2.5}
\]

splits are necessary.  Restricting the eligible blocks to the 368 initially
dead blocks lowers the maximum influence to seven, giving the necessary bound

\[
                         \lceil1289/7\rceil=185.               \tag{2.6}
\]

Neither scalar bound asserts sufficiency.  Section 3 gives a much stronger
structural no-go for the dead-only face.

## 3. The all-single-split superatlas

For each initially dead block and each of its internal gaps, form the two
subblocks and both orientations of each.  Define `E_super` by:

1. retaining every old oriented state, including the states which an actual
   split would remove;
2. adjoining every state arising from every possible single split;
3. assigning private block identities to incompatible alternatives, so they
   may even seam to one another; and
4. imposing only Johnson adjacency, the original deleted colour, and the
   relaxed necessary residence predicate.

This construction has 15,910 oriented states and 46,200 seam triples.

### Theorem 3.1 (one split per dead block is impossible)

Every endpoint atlas obtained by splitting each initially dead block at most
once is a subatlas of `E_super`.  Yet 568 original deleted colours have degree
zero in `E_super`.  Therefore no such split strategy can restore the exact
rank-eight palette by ordinary direct seams.

#### Proof

Every state available after a chosen split was explicitly placed in
`E_super`; every unchanged state was retained.  The superatlas also discards
orientation consistency and mutual-exclusion constraints, so it only adds
seams.  A zero row in this relaxation is consequently zero in every actual
strategy.  The exact enumeration leaves 568 such rows.  \(\square\)

This theorem is independent of how the 368 split positions are selected.  It
is stronger than the lower bounds (2.5)--(2.6).

## 4. The deterministic best-local repair

For calibration, choose one split in every dead block by the deterministic
lexicographic objective:

1. require the newly deleted colour to have a relaxed seam if possible;
2. maximize the number of old zero rows activated against the baseline
   atlas;
3. maximize the new colour degree;
4. maximize the number of local seam triples; and
5. choose the earliest gap on a tie.

All 368 blocks are splittable and every selected new colour has positive
degree.  The number of old zero rows locally activated by the chosen split is
distributed as

\[
\begin{array}{c|rrrrrr}
\text{rows activated}&0&1&2&3&4&5\\ \hline
\text{blocks}&30&138&147&43&9&1.
\end{array}                                                    \tag{4.1}
\]

After all selections are installed and the atlas is rebuilt from scratch,
there are 4,175 blocks and colours.  Its exact relaxed census is

\[
\begin{array}{c|r}
\text{seam triples}&24588\\
\text{zero colours}&812\\
\text{zero outgoing physical blocks}&0\\
\text{zero incoming physical blocks}&0\\
\text{block tail--head matching}&4153/4175\\
\text{block tail--colour matching}&3363/4175\\
\text{colour--block head matching}&3363/4175.
\end{array}                                                    \tag{4.2}
\]

All 812 zero rows are members of the original zero set; none is a newly cut
colour or an old formerly nonzero colour.  Thus the rule repairs 477 named
rows and every isolated block, but a large palette obstruction remains.

## 5. Consequence for constant-size `q=3` seam gadgets

Regrouping the same atomic endpoints into a ternary fusion cannot change an
empty direct-colour row: some actual seam must still have the named rank-eight
intersection.  More generally, suppose a collection of seam gadgets changes
or exposes `g` rank-nine endpoint owner masks while retaining all other frozen
interiors.  By (2.1), those sockets are incident with at most `5g` members of
the original zero set.  Therefore serving all 1,289 rows requires

\[
                              g\ge258.                          \tag{5.1}
\]

If one fixed `q=3` gadget exposes at most `g_0` changed owner sockets, at least
`ceil(1289/(5g_0))` gadget occurrences are necessary on this factor.

This does not obstruct a zero-added-letter global rethread: hundreds or
thousands of owner occurrences may be changed without increasing word
length.  It does rule out repairing the frozen atomic factor with a bounded
number of constant-socket seam gadgets.

## 6. Reproducible artifacts and scope

The standalone C++20 audit is

```text
scratch/audit_k17_h2_dead_endpoint_repair_20260801.cpp
SHA256 1394e3f07760c8247b758b11343bbac3fbec0e8e2be677026038acd3ea3fd75e
```

and the retained output is

```text
scratch/k17_h2_dead_endpoint_repair_20260801.out
SHA256 6cccd1f025053095ddc11442c298ca5393c6b855bb3d2bbc6f3409d00ea1c979
```

It was compiled and run on H100 with
`g++ -std=c++20 -O3 -DNDEBUG`, ending in

```text
PASS_K17_H2_DEAD_ENDPOINT_REPAIR_AUDIT
```

The input factor and preceding endpoint theorem are unchanged.  This result
rules out only:

* ordinary seams between the deterministic minimum-cut blocks;
* every choice of at most one additional split in each initially dead block;
* and any bounded collection of bounded-socket gadgets which otherwise
  retains the frozen interiors.

It does **not** rule out additional cuts throughout the nondead bulk, a global
residence-aware rethread, a whole socket gadget with growing support, a new
protected factor, or `nu(17)=B(17)`.
