# Audit of all half-step sectors in the repaired late-cross compiler

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

For the repaired cross-once-then-parallel compiler, aligned injectivity
does imply every **augmented** half-step code, provided one uses the full
coarse envelope.  The four start-parity/length cases have envelope sizes

\[
\begin{array}{c|cc}
 &q=2d&q=2d+1\\ \hline
\text{even start}&d&d+1\\
\text{odd start}&d+1&d+1.
\end{array}                                           \tag{0.1}
\]

Thus, writing `R=8B`, exact augmented aligned injectivity through coarse
depth `B` gives exact augmented half-step injectivity, for both signs and
both cyclic starting parities, at every physical length

\[
                         1\le q\le2B-1=R/4-1.        \tag{0.2}
\]

The formerly informal “one boundary endpoint” explanation needs one
correction: an odd-start even-length segment has two partial boundary
pairs.  Both belong to the aligned envelope, and both retained endpoints
are extra data.

This is not a literal OR-target theorem.  If the tag recording the varied
support is forgotten, neither the envelope nor its boundary directions
need be recoverable.  An untouched `00` pair and a completed
`00 -> 01 -> 11` pair have the same lower trace, with the dual ambiguity
for upper trace `11`.  Hence augmented aligned injectivity alone cannot
imply untagged half-step injectivity.

## 1. Exact physical word enumeration

For one even coarse context, write the forward physical word as

\[
 b_{i_0},a_{i_0},b_{i_1},a_{i_1},b_{i_2},a_{i_2},\ldots .    \tag{1.1}
\]

An even physical start occurs immediately before `b_(i_0)`; an odd start
occurs immediately before `a_(i_0)`.  The four cases are

\[
\begin{array}{c|c|l|c}
\text{start}&q&\text{traversed physical directions}&|A|\\ \hline
E&2d&
 \{b_{i_s},a_{i_s}:0\le s<d\}&d\\
E&2d+1&
 \{b_{i_s},a_{i_s}:0\le s<d\}\cup\{b_{i_d}\}&d+1\\
O&2d+1&
 \{a_{i_0}\}\cup\{b_{i_s},a_{i_s}:1\le s\le d\}&d+1\\
O&2d&
 \{a_{i_0}\}\cup\{b_{i_s},a_{i_s}:1\le s<d\}
       \cup\{b_{i_d}\}&d+1.
\end{array}                                                   \tag{1.2}
\]

Here `A` is the coarse envelope, the set of every `i_s` whose pair is
used at least partially.  In the last row there are `d-1` completed
pairs, one initial `a`-only pair, and one terminal `b`-only pair.  For
`d=1`, the middle family is empty and the word is simply
`a_(i_0),b_(i_1)`.

The reverse word has coarse pairs `a_i,b_i`; interchanging `a` and `b`
in (1.2) gives the same four envelope sizes.  Thus (0.1) is valid in both
orientations.

## 2. Reduction to the aligned augmented code

Use physical pair coordinates

\[
                         a_j=x_j,
 \qquad                  b_j=x_j\oplus p_j.          \tag{2.1}
\]

The augmented trace supplies its traversed physical directions.  It
therefore supplies `A`, distinguishes completed pairs from the one or two
partial boundary pairs, and records their retained endpoints.

For every `k notin A`, neither `a_k` nor `b_k` is traversed.  The trace
records both, hence records

\[
                         x_k=a_k,
 \qquad                  p_k=a_k\oplus b_k.          \tag{2.2}
\]

Therefore every row of (1.2) determines the aligned augmented code

\[
                         (A,p|_{A^c},x|_{A^c})       \tag{2.3}
\]

at coarse depth `|A|`.  No erased boundary endpoint is required in
(2.3), because its coordinate lies in `A`.  The retained boundary
endpoint or endpoints are additional information.

### Theorem 2.1 (augmented half-step inheritance)

If the aligned augmented code is injective at every coarse depth at most
`B`, then every forward and reverse augmented physical trace with
`|A|<=B` is injective, for both signs.

#### Proof

The trace determines (2.3), which recovers the unique even coarse anchor
by aligned injectivity.  For an even physical start this anchor is the
start.  For an odd start, the `a`-only initial boundary identifies the
unique preceding `b_(i_0)` half-edge; toggling that bit recovers the odd
starting vertex.  The same argument with `a,b` interchanged applies in
reverse.  Lower and upper augmented traces record the same exterior word,
so the proof applies to both signs.  \(\square\)

For odd `q=2d+1`, both starts have `|A|=d+1`, so the allowed range ends at
`q=2B-1`.  For even `q=2d`, the odd start is the larger case with
`|A|=d+1`, so the allowed range ends at `q=2B-2`.  Together these give
every integer in (0.2).  At `q=2B`, even starts remain aligned, but odd
starts have `|A|=B+1`; no conclusion follows from the depth-`B` theorem.

## 3. Literal-target obstruction

The reduction in Section 2 begins by reading `A` from the augmented tag.
A single literal lower target cannot in general do this.  On one pair,

\[
                         00\longrightarrow01\longrightarrow11        \tag{3.1}
\]

has lower intersection `00`, exactly as an untouched pair initially in
state `00`.  Its upper union is `11`, exactly as an untouched pair
initially in state `11`.  A partial boundary has the analogous ambiguity
with an untouched split state.

Consequently:

* augmented aligned injectivity implies augmented half-step injectivity by
  Theorem 2.1;
* it does not imply literal aligned or literal half-step injectivity after
  `A` is forgotten;
* in a coordinate-disjoint Johnson interface where local occupancy
  distinguishes varied pairs from untouched pairs, the interface itself
  supplies `A`, and Theorem 2.1 becomes a literal statement there.

The surviving raw-cube gate is therefore support recovery, not a
half-step parity calculation.
