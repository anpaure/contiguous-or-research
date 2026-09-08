# Exact rotor transport and a block-correlation barrier

## Status

This note does **not** prove the constant-one conjecture.  It separates the
next simultaneous-rounding problem into two pieces.

1.  At the level of fully annotated symmetric-chain flags, the horizontal
    queue dynamics has an exact integral path factor for every nonincreasing
    radius profile.  There is no endpoint, monodromy, or path-compatibility
    loss at this level.
2.  The remaining problem is an ownership transversal for the Boolean masks
    carried by those paths.  If the annotations are correlated only inside
    independent blocks of size `b`, and `R_q` centers are active through
    radius `q`, then a radius-`q` packing has `(1-o(1))R_q/b` high-radius
    components.  With separate queue resets this forces relative overhead
    `Omega(qR_q/(bW))`.  Thus the correlation length forced by this argument
    is `omega(qR_q/W)`, not always `omega(q)`.  In the intended symmetric-chain
    quota `R_q=N_q`, this distinction matters at growing depth.

Throughout,

\[
 W=\binom{2m}{m},\qquad (m)_d=m(m-1)\cdots(m-d+1).
\]

## 1. Annotated chain flags

For `0 <= d < m`, let `F_d` be the set of triples

\[
 F=(S;x_0,\ldots,x_{d-1};y_1,\ldots,y_d),
\tag{1.1}
\]

where `|S|=m`, the `x_i` are distinct elements of `S`, and the `y_i`
are distinct elements of `S^c`.  The flag advertises the saturated symmetric
chain

\[
 L_q(F)=S\setminus\{x_0,\ldots,x_{q-1}\},\qquad
 U_q(F)=S\cup\{y_1,\ldots,y_q\},\qquad 0\le q\le d.
\tag{1.2}
\]

Thus

\[
 |F_d|=W(m)_d^2.
\tag{1.3}
\]

For every `q <= d`, coordinate symmetry gives constant fibres

\[
 |L_q^{-1}(A)|=|U_q^{-1}(B)|=\frac{|F_d|}{N_q},
 \qquad N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\tag{1.4}
\]

## 2. A canonical exact rotor relation

Fix `0 <= e <= d < m`.  A directed rotor arc from `F in F_d` to
`F' in F_e` is defined as follows.

When `d=e=0`, choose arbitrary `x in S` and `a in S^c`, put

\[
 S'=S\setminus\{x\}\cup\{a\},
\tag{2.0}
\]

and use the unique unannotated flag centred at `S'`.  This is the radius-zero
queue update.

Suppose from now on that `d>0`.

Write `F` as in (1.1).  Choose

\[
 a\in S^c\setminus\{y_1,\ldots,y_d\}
\tag{2.1}
\]

and put

\[
 S'=S\setminus\{x_0\}\cup\{a\}.
\tag{2.2}
\]

If `e<d`, set

\[
 (x'_0,\ldots,x'_{e-1})=(x_1,\ldots,x_e),
 \qquad
 (y'_1,\ldots,y'_e)=(x_0,y_1,\ldots,y_{e-1}).
\tag{2.3}
\]

If `e=d`, additionally choose

\[
 b\in S\setminus\{x_0,\ldots,x_{d-1}\}
\tag{2.4}
\]

and set

\[
 (x'_0,\ldots,x'_{d-1})=(x_1,\ldots,x_{d-1},b),
 \qquad
 (y'_1,\ldots,y'_d)=(x_0,y_1,\ldots,y_{d-1}).
\tag{2.5}
\]

These are prefix relations induced by one move-to-front queue update.  They
form a convenient biregular **subrelation** of all valid one-step updates:
when the radius drops, an incoming coordinate could also consume an old
upper annotation that is no longer advertised, and in the equal-radius case
the discarded last upper annotation could likewise be consumed.  Condition
(2.1) deliberately excludes those extra transitions.  In the equal-radius
case, the choice `b` is the element split off from the old leading
lower-core block by the next word entry.

### Theorem 2.1 (biregular rotor transport)

The bipartite rotor graph from `F_d` to `F_e` is biregular.  Its left degree
is

\[
 r^+_{d,e}=
 \begin{cases}
 m-d,&e<d,\\
 (m-d)^2,&e=d.
 \end{cases}
\tag{2.6}
\]

Its right degree is

\[
 r^-_{d,e}=r^+_{d,e}\frac{|F_d|}{|F_e|}
 =r^+_{d,e}(m-e)_{d-e}^2.
\tag{2.7}
\]

Consequently, if `F` is uniform on `F_d` and an outgoing rotor arc is chosen
uniformly, then its head is exactly uniform on `F_e`.

#### Proof

For `e<d`, only `a` is free, giving `m-d` choices.  For `e=d>0`, the choices
of `a` and `b` are independent and each has `m-d` possibilities.  For
`d=e=0`, the choices of the departing and incoming coordinates in (2.0)
give `m^2` arcs.  This proves (2.6).

The symmetric group on the `2m` coordinates is transitive on `F_e` and
preserves the rotor relation.  Hence every right vertex has the same
indegree.  Double-counting arcs and using (1.3) gives (2.7).  The last
assertion is the standard uniform-marginal consequence of biregularity.
QED

### Corollary 2.2 (uniform monotone rotor process)

Let

\[
 d_0\ge d_1\ge\cdots\ge d_{H-1}.
\tag{2.8}
\]

Start with a uniform member of `F_(d_0)` and at step `t` choose a uniform
outgoing rotor arc to `F_(d_(t+1))`.  Then the time-`t` flag is exactly
uniform on `F_(d_t)` for every `t`.  The number of continuations from any
fixed initial flag is the state-independent product

\[
 \prod_{t=0}^{H-2}r^+_{d_t,d_{t+1}}.
\tag{2.9}
\]

Every resulting flag path is realized by a genuine queue word: initialize
the ordered last-occurrence partition for the first flag, and at each step
append the successor lower core `L_(d_(t+1))(F_(t+1))`.  Relations
(2.3)--(2.5) are precisely the move-to-front update of its leading blocks.

For completeness, the ordered partition exposing a flag `F in F_d` is

\[
 \bigl(L_d(F),\{x_{d-1}\},\ldots,\{x_0\},
       \{y_1\},\ldots,\{y_d\},
       S^c\setminus\{y_1,\ldots,y_d\}\bigr).
\tag{2.10}
\]

Both end blocks are nonempty because `d<m`.  Writing these
blocks once in reverse order initializes (2.10) literally.  Its prefix
unions are exactly the chain (1.2).  If `e<d`, the appended successor lower
core absorbs the old lower core, the singleton blocks down through
`\{x_{e+1}\}` when present, and the incoming coordinate `a`; the first
surviving blocks are `\{x_e\},\ldots,\{x_0\},\{y_1\},\ldots`.  If `e=d`,
the old lower core
leaves the singleton residual `\{b\}`.  These are exactly the successor
orders specified in (2.3) and (2.5).  The radius-zero update is immediate
from the partition `(S,S^c)`.

## 3. An integral flag-space path factor

The preceding uniform process is not merely fractional.

### Theorem 3.1 (exact rotor path factor)

For every profile (2.8), there is an integer `M>0` and a multiset of exactly
`M` genuine rotor paths of that profile such that, at every time `t`, every
flag in `F_(d_t)` occurs exactly

\[
 \frac{M}{|F_{d_t}|}
\tag{3.1}
\]

times.  The integer `M` may be chosen divisible by all flag-space sizes and
all arc denominators occurring in the profile.

#### Proof

Between two consecutive layers put the uniform coupling weight

\[
 \frac{M}{|F_d|r^+_{d,e}}
\tag{3.2}
\]

on every rotor arc.  Choose `M` so that all these weights are integers.
The total weight incident with a left flag is `M/|F_d|`; by (2.7), the total
weight incident with a right flag is `M/|F_e|`.  Split each flag into that
many copies.  The integer arc weights give a bipartite multigraph in which
every copy can be matched once across the two layers.  Doing this at every
consecutive pair of layers and composing the matchings partitions all layer
copies into `M` full rotor paths.  QED

### Corollary 3.2 (exact mask marginals inside the factor)

Put

\[
 a_q=|\{t:d_t\ge q\}|.
\tag{3.3}
\]

Across the `M` paths of Theorem 3.1:

* every middle mask occurs exactly `HM/W` times;
* every rank-`m-q` mask occurs as a certified lower member exactly
  `a_q M/N_q` times;
* every rank-`m+q` mask occurs as a certified upper member exactly
  `a_q M/N_q` times.

#### Proof

At a fixed active time, (1.4) and (3.1) give exactly `M/N_q` occurrences of
each signed depth-`q` mask.  Sum over the `a_q` active times.  The middle-row
statement is the case `q=0` summed over all `H` times.  QED

### Corollary 3.3 (an internally simple balanced orbit)

Assume `d_0<=h` and `H+h<=m`.  Take every injective coordinate queue

\[
 z_{-h},z_{-h+1},\ldots,z_{H+m-1}
\tag{3.5}
\]

on `[2m]` with equal multiplicity, and at time `t` use

\[
 S_t=\{z_t,\ldots,z_{t+m-1}\},\qquad
 x_i(t)=z_{t+i},\qquad y_j(t)=z_{t-j}.
\tag{3.6}
\]

For the fixed profile (2.8), these are genuine rotor paths and have the
uniform flag and mask marginals of Corollary 3.2.  Moreover, all certified
masks inside one path are distinct.

#### Proof

Uniformity follows either from coordinate transitivity and constant fibres,
or directly by counting completions of the fixed positions in (3.6).  The
rotor identities are literal shifts of the queue indices.

The certified mask at time `t` and signed depth `s` is the coordinate image
of the position interval

\[
 [t-s,t+m-1].
\]

Different `s` give different cardinalities.  For fixed `s`, different `t`
give shifted equal-length intervals with different boundary positions; an
injective coordinate queue makes their image sets distinct.  QED

Thus the balanced transport may be taken inside an explicit orbit whose
individual paths already have zero internal certified duplicate count.  The
word "factor" in Theorem 3.1 refers to exact uniform coverage of the
annotated flag layers; it does not assert disjoint Boolean-mask ownership
between different paths.

In particular, if the profile mixture has

\[
 \mathbb E a_q=H\frac{N_q}{W},
\tag{3.4}
\]

then its middle and every signed nonmiddle row have exactly the same
normalized multiplicity.  Thus the monotone-radius law and the rotor
endpoint dynamics admit exact **integral** transport before Boolean-mask
ownership is imposed.  For the usual shifted-floor quota law, the finitely
many profile probabilities are rational because every `N_q/W` is rational.
Apply Theorem 3.1 to each profile and clear all profile weights and path-factor
denominators; their disjoint union is an actual finite integral path
multiset with the equality in (3.4), not merely a probability distribution.

The remaining rounding gate can consequently be stated without any dynamic
ambiguity:

> Choose about `W/H` paths from a balanced rotor path factor so that the
> Boolean masks appearing on the chosen path flags have total duplicate plus
> missing defect `o(W)`.

This is a common-ownership transversal problem, not a path-existence problem.

## 4. A block-correlation barrier

The exact transport above also shows what kind of dependence a successful
rounding must create.  The following proposition generalizes the
independent-center obstruction.

Fix `q>=2`.  Partition the middle centers into blocks of size at most `b`.
Inside one block the depth-`q` annotations may be arbitrarily correlated.
Different blocks are independent.  Condition on the high-center declarations
block by block, and assume that this conditional law still factors over the
blocks.  Conditional on a center being declared radius at least `q`, its
ordered lower and upper `q`-prefixes are mutually independent uniform ordered
tuples (the standard symmetric flag marginal).  Denote the now fixed number
of high centers by `R_q`.  This conditional formulation includes, for
example, independently annotated blocks with a prescribed number of high
centers in each block.

\[
 R_q=|\{\text{centers declared radius at least }q\}|.
\tag{4.1}
\]

Call a transition between centers in different blocks `q`-compatible if it
satisfies the necessary rotor-prefix relations through depth `q`.

### Proposition 4.1 (independent-block component lower bound)

Let `E_q^cross` be the number of directed cross-block `q`-compatible
transitions.  Then

\[
 \mathbb E E_q^{cross}
 \le
 \frac{mR_q}{(m)_{q-1}(m)_q}.
\tag{4.2}
\]

If

\[
 b\,\frac{m}{(m)_{q-1}(m)_q}=o(1),
\tag{4.3}
\]

then with probability tending to one every **direct rotor packing** of the
annotations--one in which consecutive advertised centers are joined by one
rotor update and no extra connector states are inserted--has at least

\[
 (1-o(1))\frac{R_q}{b}
\tag{4.4}
\]

distinct radius-at-least-`q` components.

With separately initialized queue words, their reset overhead is therefore

\[
 (2q+1)(1-o(1))\frac{R_q}{b}.
\tag{4.5}
\]

In particular, vanishing reset cost relative to `W` requires

\[
 \boxed{\frac{bW}{qR_q}\longrightarrow\infty.}
\tag{4.6}
\]

#### Proof

Condition on a high tail flag and on the block containing it.  There are at
most `m` possible incoming coordinates and hence at most `m` candidate head
centers.  For a candidate in a different block, its annotation is
independent.  In the most permissive equal-radius case, the successor upper
`q`-tuple and its first `q-1` lower entries are prescribed.  The probability
is at most

\[
 \frac1{(m)_{q-1}(m)_q}.
\tag{4.7}
\]

If the old radius is larger than the new one, all `q` entries on both sides
are prescribed and the probability is smaller.  Summing over candidates and
tails proves (4.2).

There are at least `R_q/b` nonempty high blocks.  Within each block, a path
forest on its high vertices uses at most `v-1` internal transitions, so
before cross-block transitions there is at least one high component per
nonempty block.  Each cross-block transition can reduce the component count
by at most one.  Markov's inequality, (4.2), and (4.3) show

\[
 E_q^{cross}=o_p(R_q/b),
\]

which proves (4.4).

Along one such direct monotone-radius queue atom, the
radius-at-least-`q` centers form a single prefix.  Hence distinct high
components require distinct initializations.  An atom starting at radius at
least `q` has `2d_0+1 >= 2q+1` initialization entries beyond its
one-per-center updates.  This proves (4.5), and (4.6) follows.  The
proposition does not rule out inserting additional connector states; their
cost would require a separate lower bound.  QED

For every `q>=2`, condition (4.3) holds uniformly for `b<=m`.  Indeed,
`(m)_(q-1)(m)_q` is increasing in `q` on this range, so its left side is at
most

\[
 \frac{bm}{(m)_1(m)_2}=\frac{b}{m(m-1)}\le\frac1{m-1}.
\]

For the intended symmetric-chain quota `R_q=N_q`, at the reservoir threshold

\[
 q=(1+o(1))\sqrt{m\log\log m},
\]

we have

\[
 \frac{R_q}{W}=\frac{N_q}{W}=(\log m)^{-1+o(1)}.
\]

Consequently this proposition forces correlation across blocks of length

\[
 \omega\!\left(\sqrt{m\log\log m}\,
 (\log m)^{-1+o(1)}\right),
\]

not across `omega(q)` centers.  Completion of bounded-size independent blocks
using only direct compatible arcs and separate resets is still ruled out
there, but `Theta(q)`-local correlation is **not** ruled out by this reset
ledger.

## 5. Exact boundary after these results

The positive theorem removes a possible false obstruction: monotone radii
can be transported integrally along genuine queue paths with exactly uniform
flag marginals.  No horizontal endpoint correction is needed before masks
are identified.

The negative theorem removes a false strategy only at the density-sensitive
scale quantified by (4.6): those flag paths cannot be assembled from
independent blocks of size `o(qR_q/W)` and then joined cheaply by random
compatible endpoints.  It does not show that correlation length must always
dominate the advertised radius.

The remaining falsifiable target is therefore a **long-block ownership
transversal theorem** for one of the exact path factors in Theorem 3.1, with
block length `H >> q` and total Boolean-mask defect `o(W)`.  Neither ordinary
pair-codegree bounds nor post-hoc local absorption proves that target.
