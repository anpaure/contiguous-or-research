# Direct flagged Johnson Gray codes under arbitrary-mask move-to-front

This note studies a route which does **not** assign a fixed symmetric chain
to each middle set.  Instead, list the middle layer in a combination Gray
code and evolve an ordered-partition flag directly, using one arbitrary-mask
move-to-front update at every step.  The prefix unions of the evolving flags
are the candidate witnesses for all other Boolean ranks.

There is a positive local fact: every Johnson edge can be lifted in one MTF
step.  The global obstruction is a monotone flag-depth invariant.  Once the
number of blocks inside the middle prefix decreases, it can never increase
again.  This yields an exact queue criterion for deep flagged Gray codes and
a rigorous asymptotic no-go theorem for every genlex transposition order,
including the classical reflected/revolving-door and Chase families.  The
same argument, with depth two instead of one, rules out cool-lex.

The conclusion is not that direct flagged codes are impossible.  It says
that a successful code must have long element-residence times and must be
designed together with its flags; the standard combination orders have
dense constant-size recency resets and therefore collapse almost
immediately.

For background on the Gray codes audited here, see the survey
[Mütze, *Combinatorial Gray codes---an updated
survey*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/ds26/pdf/)
and [Ruskey--Williams, *The coolest way to generate
combinations*](https://webhome.cs.uvic.ca/~ruskey/Publications/Coollex/CoolComb.html).

## 1. Ordered-partition flags

Let

\[
                       \Pi=(B_1,\ldots,B_s)           \tag{1.1}
\]

be an ordered partition of `[n]`.  Its prefix unions are

\[
              B_1,\quad B_1\cup B_2,\quad\ldots.     \tag{1.2}
\]

For a nonempty update mask `X`, define

\[
 M_X(\Pi)=(X,B_1-X,\ldots,B_s-X),                    \tag{1.3}
\]

deleting empty blocks.  This is the exact last-occurrence/move-to-front
state update for appending the array entry `X`.

If a set `S` is a prefix union of `Pi`, let

\[
 \kappa_\Pi(S)=\text{the number of nonempty blocks in its prefix}. \tag{1.4}
\]

We call this the flag depth of `S` in `Pi`.

### Theorem 1 (flag depth never increases)

Let `S` and `T` be distinct sets of the same size.  Suppose `S` is a prefix
union of `Pi`, `T` is a prefix union of `M_X(Pi)`, and `X` is nonempty.  Then

\[
                 \boxed{\kappa_{M_X(\Pi)}(T)
                         \leq\kappa_\Pi(S).}          \tag{1.5}

#### Proof

Write `S=B_1 union ... union B_j`.  In the updated state, suppose the prefix
for `T` ends with the residual of the old block `B_q`; put `q=0` if the
prefix is only the new block `X`.  Then

\[
 T=X\cup(B_1\cup\cdots\cup B_q).                     \tag{1.6}

If `q>=j`, (1.6) gives `S subseteq T`.  Equal cardinality would force
`S=T`, contrary to the hypothesis.  Hence `q<j`.  The target prefix consists
of the new block and at most `q` old residual blocks, proving

\[
 \kappa(T)\leq q+1\leq j=\kappa(S).                  \tag{1.7}
\]

QED.

This theorem allows arbitrary ties, arbitrary update masks, and arbitrary
changes in more than one coordinate.  It is not restricted to singleton
states or Johnson edges.

## 2. Every Johnson edge lifts, but with a price

Suppose the current middle set is

\[
 S=B_1\cup\cdots\cup B_j
\]

and the next one is the Johnson neighbor

\[
                       T=S-\{a\}+\{b\}.              \tag{2.1}

Let `a in B_r`.  Put

\[
 X=\{b\}\cup(B_r-\{a\})\cup B_{r+1}\cup\cdots\cup B_j.
\tag{2.2}
\]

Then the updated state begins

\[
 X,B_1,\ldots,B_{r-1},\{a\},\ldots,                 \tag{2.3}

after empty blocks are deleted, and the union through `B_(r-1)` is exactly
`T`.  Thus every edge of every Johnson graph has a one-step arbitrary-mask
MTF lift.

One may add to `X` any optional elements from the earlier blocks
`B_1,...,B_(r-1)` without changing the middle target.  This is the full
local freedom used in the original flagged-Johnson proposal.

The equality case of Theorem 1 is rigid.

### Corollary 2 (last-block law)

In a Johnson step, preserving flag depth `j` requires the departing element
`a` to lie in the last middle block `B_j`.  Every earlier block must retain
at least one element after the optional moves.

#### Proof

To exclude `a`, the target prefix must stop before the residual block
containing it.  In the notation of Theorem 1, if `a in B_r` then the new
depth is at most `r`.  Equality with `j` therefore forces `r=j`; optional
moves must not delete any of the preceding `j-1` residual blocks.  QED.

So a deep flagged Johnson walk is a queue of nonempty blocks: the last block
loses the departing element, gains the arrival (and any optional refreshed
elements), and rotates to the front.

## 3. Short residence times collapse the flag

Consider consecutive middle sets.  Say that an element has residence time
`ell` if it enters at one transition and leaves `ell` transitions later,
without leaving in between.

### Lemma 3 (residence bound)

If the current flag depth is `j>ell`, then the departure of an element of
residence time `ell` forces the new flag depth to be at most `ell`.

In particular, if a newly entered element leaves at the very next
transition, the flag collapses to depth one.

#### Proof

An entering element lies in the new first block.  At each later
depth-preserving step, its block can move right by at most one position;
optional refreshes move it back to the first block and only make the bound
stronger.  Immediately before its departure after `ell` transitions, it is
therefore in one of the first `ell` blocks.  Corollary 2 says that preserving
depth would require it to be in the last block.  Applying the proof of
Theorem 1 with its actual block position bounds the new depth by `ell`.
QED.

Equivalently, a cyclic lift of constant depth `j` must have every element
residence time at least `j`.  In the no-optional singleton case `j=m`, this
is precisely the sliding-window or subset-ucycle condition.

## 4. A six-state local obstruction

The six `2`-subsets of a `4`-set form the vertices of `J(4,2)`, the line
graph of `K_4`.

### Lemma 4

Every transposition Gray path listing all six vertices of `J(4,2)` has an
element which enters and leaves at the next transition.

#### Proof

Regard each `2`-set as an edge of `K_4`.  Suppose no newly entered endpoint
ever leaves at the following transition.  Then, at every internal edge of
the six-edge list, the endpoint shared with the preceding edge and the
endpoint shared with the following edge are distinct.  Orienting through
those two endpoints turns the list into an Euler trail using all six edges
of `K_4`.  This is impossible: `K_4` has four odd-degree vertices, whereas
an Euler trail has at most two.  QED.

The lemma is independent of the particular revolving-door or Chase
successor rule.

## 5. Genlex transposition codes have dense collapses

A combination order is genlex if all bitstrings with any fixed prefix form
an interval.  The classical binary-reflected/revolving-door order and the
homogeneous Chase orders are cyclic genlex transposition Gray codes.

Put `n=2m`, `W=binomial(2m,m)`, and choose an integer `c` with

\[
                       4\leq c=o(\sqrt m).            \tag{5.1}

Partition a genlex order into intervals with the first `2m-c` membership
bits fixed.  If the free `c`-bit suffix has weight `r` with

\[
                       2\leq r\leq c-2,              \tag{5.2}

then refine once more by fixing `c-4` of those bits with weight `r-2`.
The resulting contiguous six-state interval lists every `2`-subset of four
free coordinates.  By Lemma 4 it contains an immediate re-exit and hence a
depth-one collapse.

Only suffix weights

\[
                         r\in\{0,1,c-1,c\}           \tag{5.3}

are bad.  The fraction of middle sets in those intervals is

\[
 \frac1W\sum_{r\in\{0,1,c-1,c\}}
       \binom cr\binom{2m-c}{m-r}
   =O\!\left(c,2^{-c}e^{O(c^2/m)}\right).           \tag{5.4}

This is just the four extreme probabilities of the hypergeometric
distribution obtained by intersecting a uniform middle set with the last
`c` coordinates.

Take, for example, `c=floor(log_2 m)`.  Then the total number of bad states
is `o(W)`, and every good prefix interval has length at most `2^c=o(W)` and
contains a collapse.  Consequently the largest cyclic gap between immediate
re-exits is at most

\[
                    o(W)+2^{c+1}=o(W).               \tag{5.5}

### Theorem 5 (genlex barrier)

For every cut of a cyclic genlex transposition Gray code of the middle layer,
every arbitrary-mask flagged MTF lift reaches depth one after `o(W)` states
and stays there.  It therefore cannot cover the Boolean lattice.

#### Proof

By (5.5), the first immediate re-exit after the cut occurs within `o(W)`
steps.  Lemma 3 collapses the middle flag to one block, and Theorem 1 prevents
any later increase.

A depth-one state has the entire middle set as its first block, so it exposes
no nonempty proper subset below rank `m`.  Hence at most `o(W)` rank-`m-1`
sets can have appeared, whereas the number required is

\[
                         \binom{2m}{m-1}
                         =\frac{m}{m+1}W
                         =(1-o(1))W.                 \tag{5.6}

QED.

This rules out the reflected/revolving-door and Chase families even after
allowing arbitrary tied blocks, arbitrary optional retained elements, and an
optimal cyclic cut.  It is a property of their genlex recursion, not of one
implementation.

## 6. Cool-lex collapses to depth at most two

Cool-lex is genlex but some steps exchange two pairs of bits, so Lemma 4 does
not apply literally.  Its four-free-coordinate, weight-two suborder is,
up to reversal,

```text
0011, 1001, 1100, 0110, 1010, 0101.
```

Inside this list an entering coordinate leaves two transitions later; the
reversed list has an even shorter such event.  Therefore every good
`c`-coordinate prefix interval from (5.2) contains a residence-time-at-most-
two event.  The same hypergeometric estimate (5.4) and gap argument give:

### Theorem 6 (cool-lex barrier)

For every cut of the cyclic cool-lex order, any flagged MTF lift has depth at
most two after `o(W)` states and never recovers.

Such a lift cannot be universal.  A depth-two state exposes at most one
nonempty proper lower prefix, so all `W` states expose at most `W+o(W)` lower
sets.  But just the two ranks immediately below the middle contain

\[
 \binom{2m}{m-1}+\binom{2m}{m-2}
                         =(2-o(1))W                  \tag{6.1}

distinct targets.

## 7. Exact remaining direct-code target

There is also an unavoidable quantitative depth scale.  Let `Pi_t` be the
state assigned to the `t`th middle set and put `j_t=kappa_(Pi_t)(S_t)`.
Every state contributes at most `j_t-1` nonempty prefixes below the middle.
The lower half of `B_(2m)` has

\[
 L_m=\sum_{r=1}^{m-1}\binom{2m}{r}
    =\frac{2^{2m}-\binom{2m}{m}}2-1                \tag{7.1}
\]

targets.  Universality therefore requires

\[
 \sum_t(j_t-1)\geq L_m,
 \qquad
 \frac1W\sum_tj_t
     \geq\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m.\tag{7.2}
\]

So the `sqrt(m)` flag-depth scale is forced by counting, not merely suggested
by the known SCD radius distribution.

The direct flagged route is not closed.  The theorems isolate its necessary
global property.

> **Long-residence flagged Johnson problem.**  Construct a Hamilton or
> near-Hamilton middle-layer walk together with a nonincreasing ordered-block
> flag such that, for `W-o(W)` steps, the flag has `omega(1)` (in fact roughly
> `sqrt(m)` useful) nonempty blocks, every departure occurs in the last block,
> and the prefix unions over all states cover the central Boolean band.

In a cyclic constant-depth realization, the blocks form a rotating queue.
With singleton blocks this is a simple subset universal cycle: the middle
sets are consecutive length-`m` windows of one symbol word.  With tied blocks
it is a strictly weaker multi-lane version in which optional elements may be
refreshed to the front.

The standard Gray codes fail because they contain a dense family of constant-
size recency resets.  A successful code must instead be designed around long
bit runs/residence times.  This points toward tight hypergraph tours,
wreath-like factors, or a new long-run Johnson Gray code, rather than another
relabeling of revolving-door, Chase, or cool-lex.

The known universal-cycle theorem for complete uniform hypergraphs
([Glock--Joos--Kuhn--Osthus, *Euler tours in
hypergraphs*](https://arxiv.org/abs/1808.07720)) is for each fixed uniformity
with the ground-set size tending to infinity.  Its quantifiers do not cover
the present central regime `k=n/2`, so it cannot be invoked as the missing
all-`m` construction.
