# Sparse checkpoints and SCD-compatible Hamilton cycles

This note audits two all-dimensional attempts to obtain a width-sized OR
array from the Pascal-strip/rotor framework.  It contains no finite-`k`
search.

Put `n=2m` and

\[
 W=\binom{2m}{m}.
\]

The conclusions are negative but structural:

1. a bounded number of checkpoint ranks avoids the high-order codegree
   collapse, but checkpoint injectivity does not force the omitted ranks;
2. enough checkpoints to leave only bounded gaps recreate the same
   full-codegree collapse as the complete strip; and
3. the known Hamilton cycle containing the Greene--Kleitman symmetric
   chain decomposition has a positive density of transitions that cannot
   be realized by one move-to-front update.

Thus neither route, in its literal form, proves
`nu(2m)=(1+o(1))W`.

## 1. Sparse-checkpoint codegree tradeoff

Consider a length-`H`, radius-`h` Pascal-strip atom

\[
 \{A_t^u:0\le t<H,-h\le u\le h\}.
\]

Choose a set `Q` of `s` checkpoint depths, and form the certificate edge

\[
 e_Q=\{A_t^u:0\le t<H,\ u\in Q\}.                 \tag{1.1}
\]

Its uniformity is

\[
 R_Q=sH.                                           \tag{1.2}
\]

All codegree ratios below are rankwise normalized.  Equivalently, one may
first clone/weight the checkpoint layers to equalize their degrees; the
active-coordinate estimates are unchanged.  This normalization does not
by itself supply a matching theorem.

After one vertex of the atom is fixed, the entire certificate depends on
only `O(H+h)` changing coordinates.  Therefore its degree in the simple
coordinate orbit satisfies

\[
 D_Q\le R_Q(2m)^{O(H+h)}.                          \tag{1.3}
\]

The complete certificate edge has `R_Q`-codegree one.  Consequently every
full-codegree parameter of Gould--Kelly type satisfies

\[
 \boxed{
 B_Q\le D_Q^{1/(R_Q-1)}
 \le \exp\!\left(
 O\!\left(\frac{(H+h)\log m}{sH}\right)\right).}
                                                               \tag{1.4}
\]

When `H>>h`, this is

\[
 B_Q\le m^{O(1/s)}.                                \tag{1.5}
\]

For fixed `s`, the parameter also genuinely diverges when `H=o(m)`.  To
see this, let `D_j` be a `j`-codegree.  Every distinct pair of certificate
vertices has normalized codegree `O(1/m)` by the exact Pascal-strip pair
formula, so for `4<=j<=2s`,

\[
 \left(\frac D{D_j}\right)^{1/(j-1)}
 \ge c_s m^{1/(2s)}.                               \tag{1.6}
\]

For `j>2s`, among any `j` certificate positions some checkpoint row
contains at least `ceil(j/s)` positions.  Two of them are separated along
that row by Johnson distance at least

\[
 a=\left\lceil\frac{\lceil j/s\rceil-1}{2}\right\rceil .       \tag{1.7}
\]

Partitioning embeddings according to one such pair and using the exact
same-rank pair codegree gives

\[
 \frac{D_j}{D}
 \le \frac{2\binom j2}{\binom{m-h}{a}^{,2}}.       \tag{1.8}
\]

As `a<=H=o(m)` and `binom(M,a)>=(M/a)^a`, this implies, with an absolute
loss in the exponent,

\[
 \left(\frac D{D_j}\right)^{1/(j-1)}
 \ge c_s\left(\frac mH\right)^{1/(3s)}.            \tag{1.9}
\]

The pair term itself is at least `c sqrt(m)`.  Hence the complete
full-codegree parameter obeys

\[
 \boxed{
 c_s\left(\frac mH\right)^{1/(3s)}
 \le B_Q\le m^{O(1/s)}.}                           \tag{1.10}
\]

In particular, fixed `s` removes the `B=1+o(1)` obstruction whenever
`H=o(m)`.  This numerical improvement is real, although the edge
uniformity `sH` still grows and no audited black-box theorem rounds it.

There is, however, an exact opposing constraint.  If every unselected rank
is within distance `g` of a checkpoint, then

\[
 s\ge \frac{2h+1}{g+1}.                            \tag{1.11}
\]

Combining (1.4) and (1.6), still with `H>>h`, gives

\[
 \log B_Q=O\!\left(\frac{(g+1)\log m}{h}\right).  \tag{1.12}
\]

In particular, if `h>>log m` and `g=O(1)`, then

\[
 B_Q=1+o(1).                                       \tag{1.13}
\]

This is the **checkpoint-density tradeoff**: fixed `s` leaves growing
uncontrolled gaps, while bounded gaps reproduce the complete-strip
high-codegree obstruction.

## 2. Checkpoints do not force an omitted row

The missing implication already fails in the smallest possible gap.

### Lemma 2.1 (two-sided funnel)

Fix an `r`-set `S`.  For any

\[
 t\le \min(r,n-r)
\]

there are `t` saturated two-step chains

\[
 S-\{x_i\}\subset S\subset S+\{y_i\},
 \qquad 1\le i\le t,                              \tag{2.1}
\]

whose rank-`r-1` endpoints are pairwise distinct and whose rank-`r+1`
endpoints are pairwise distinct, although all their rank-`r` members are
the same set `S`.

#### Proof

Choose distinct `x_1,...,x_t in S` and distinct
`y_1,...,y_t notin S`.  Equation (2.1) gives the required chains.  \(\square\)

So even perfect local injectivity at the two neighboring checkpoints can
lose a factor `Theta(m)` in the omitted row.  Longer checkpoint gaps have
larger funnels.  Any theorem controlling omitted ranks must therefore use
pseudorandomness, expansion, absorption, or explicit labels; it cannot be a
deterministic consequence of checkpoint matching alone.

Together, (1.13) and Lemma 2.1 rule out the naive checkpoint program:

* keeping only `O(1)` rows preserves polynomial codegrees but supplies no
  automatic intermediate coverage;
* certifying enough rows to make automatic local interpolation plausible
  destroys the full-codegree parameter.

Sparse certificates may still be useful inside a custom pseudorandom
rounding theorem, but existing black-box matching theorems do not provide
that missing implication.

## 3. Move-to-front exposure of a saturated chain

Let

\[
 \Pi=(B_1,\ldots,B_q)                              \tag{3.1}
\]

be the ordered last-occurrence partition after an array prefix.  Its suffix
ORs are the prefix unions

\[
 B_1,\ B_1\cup B_2,\ \ldots .                     \tag{3.2}
\]

An update by a mask `X` changes the partition to

\[
 \operatorname{MTF}_X(\Pi)
 =(X,B_1\setminus X,\ldots,B_q\setminus X),        \tag{3.3}
\]

with empty blocks deleted.

Write a saturated chain as

\[
 C=(L;z_1,z_2,\ldots,z_d),                         \tag{3.4}
\]

meaning

\[
 L\subset L+z_1\subset\cdots\subset
 L+z_1+\cdots+z_d.                                \tag{3.5}
\]

The state `Pi` exposes `C` exactly when, for some `a`,

\[
 B_1\cup\cdots\cup B_a=L,
 \qquad B_{a+i}=\{z_i\}\quad(1\le i\le d).       \tag{3.6}
\]

Blocks following `z_d` are irrelevant.

## 4. The first-star deletion barrier

For a Greene--Kleitman chain encoded by stars in spatial order, let `f(C)`
be obtained by replacing the first two stars by `0,1`.  In the notation
(3.4), this is the chain

\[
 f(C)=(L+z_2;z_3,z_4,\ldots,z_d),                 \tag{4.1}
\]

with `z_1` fixed outside the chain.

### Lemma 4.1 (`f` is not one-update compatible)

No single move-to-front update can take a state exposing `C` to a state
exposing `f(C)`.  No single update can take a state exposing `f(C)` to a
state exposing `C` either.

#### Proof: `C` to `f(C)`

Suppose the update mask is `X`.  Every element of `X` lies in the first
block of the new partition.  Since the new minimum is `L+z_2`, which
excludes `z_1,z_3,...,z_d`, we must have

\[
 X\subseteq L+z_2.                                 \tag{4.2}
\]

In the old partition the singleton `z_1` precedes the singleton `z_2`.
For `z_2` to enter the new minimum before the unselected `z_1` block, it is
necessary that `z_2 in X`.  But `z_1 notin X`, so its singleton survives
and still precedes every old singleton `z_3,...,z_d`.  Immediately after
the new prefix union reaches `L+z_2`, the next available old singleton is
therefore `z_1`, whereas `f(C)` requires `z_3`.  This is impossible.

#### Proof: `f(C)` to `C`

In every state exposing `f(C)`, the coordinate `z_2` lies in the prefix
forming its minimum, while `z_1`, which is absent from the top of `f(C)`,
lies after all the retained singleton blocks `z_3,...,z_d`.  An update
whose new prefixes expose `C` cannot contain `z_1` or `z_2` in its first
block, because the new minimum is `L`.  The relative order of all
unselected old blocks is preserved by (3.3).  Hence the surviving `z_2`
block still precedes the surviving `z_1` block, whereas `C` requires
`z_1` immediately before `z_2`.  This is again impossible.  \(\square\)

There is an important asymmetry.  If `ell(C)` is obtained by replacing the
last two stars by `0,1`, then the forward transition is compatible: update
by `L+z_d`.  The retained singleton sequence

\[
 z_1,z_2,\ldots,z_{d-2}                            \tag{4.3}
\]

appears before the discarded `z_{d-1}` block, so the entire chain
`ell(C)` is exposed.  Move-to-front dynamics can discard a suffix of the
increment queue, but not a prefix.

## 5. Consequence for the known SCD Hamilton cycle

Gregor--Micka--Mutze proved that the Greene--Kleitman SCD extends to a
Hamilton cycle of the hypercube.  Their recursive cycle ordering replaces
an even-dimensional parent chain `C` of positive length by the four
descendants

\[
 A=*C*,\qquad f(A),\qquad f(\ell(A)),\qquad \ell(A),              \tag{5.1}
\]

possibly in reverse order.

The boundary between `A` and `f(A)` is an `f`-pair.  The boundary between
`f(ell(A))` and `ell(A)` is the same `f`-pair in the reverse direction.
By Lemma 4.1, neither boundary is realizable by one MTF update, regardless
of the direction in which (5.1) is read.

There are

\[
 W_{2m-2}=\binom{2m-2}{m-1}                       \tag{5.2}
\]

parent chains at the preceding recursion level, and all but a lower-order
fraction have positive length.  Consequently this explicit Hamilton
ordering contains

\[
 (2-o(1))W_{2m-2}
 =\left(\frac12-o(1)\right)W_{2m}                 \tag{5.3}
\]

one-update barriers, using

\[
 \frac{W_{2m-2}}{W_{2m}}
 =\frac{m}{2(2m-1)}=\frac14+o(1).                 \tag{5.4}
\]

Thus the known SCD-compatible Hamilton construction cannot simply be read
as one long rotor path with `W+o(W)` updates.  Repairing each forbidden
boundary separately incurs `Omega(W)` extra updates.

This does **not** rule out another SCD or another ordering with
`o(W)` first-star barriers.  It identifies the exact statistic a useful
construction must control:

> order almost all symmetric chains so that almost every transition is a
> suffix-compatible queue move (or a genuine rotor move), not merely a
> bounded Hamming-distance change of the ternary chain encoding.

The 3-Gray property of the known chain ordering is therefore insufficient
for the OR problem.

## 6. All-dimensional verdict

The two audited shortcuts both fail for precise reasons.

* **Sparse checkpoints:** polynomial full-codegree parameter is available
  only while the uncontrolled rank gaps grow, and checkpoint matching alone
  does not control those gaps.
* **Known SCD Hamilton cycle:** it has a linear number of prefix-deletion
  transitions, while MTF exposure is intrinsically suffix-compatible.

The remaining viable all-`k` mechanisms are narrower than before:

1. construct an SCD whose chains admit an ordering with only `o(W)`
   first-star barriers;
2. prove a custom pseudorandom sparse-certificate theorem that controls the
   omitted ranks without inserting them into the matching edge; or
3. abandon matching and use an overlapping rotor cover with total rank
   defect `o(W)`.

Any of these would be genuinely new mathematics; none follows from the
currently cited Hamilton or nibble theorems.
