# Gate C: tunable balanced microbanks and a cross-pairing factor packet

**Status (2026-08-22).**  Every assertion in Sections 1--5 is proved.
The maximal coset banks in Appendix I are not the only balanced banks
available.  They have an exact nested refinement into microbanks with

\[
 2^s\asymp \sum_{j=1}^H {b\choose j}=2^{o(b)}
\]

states.  The microbanks remain exactly `H`-wise uniform and jointly
target-disjoint at ranks `b-1,b,b+1` inside each parent bank.

This smaller atomic scale permits a first genuinely cross-pairing theorem.
For every one-factorization of `K_(2b)`, one can choose one microbank on
each of its `2b-1` pairings so that all chosen banks are jointly
target-disjoint at the three central ranks.  Their middle-target union is
an exact `2`-design.  Thus the pair-profile constraint of any whole-bank
near-factor can be satisfied locally, rather than left to a future global
rounding.

The packet has only `2^{o(b)}` middle targets and is not a near-factor.
Nothing below proves that almost all of the middle layer can be tiled by
such packets, or repairs offsets beyond `b-1,b,b+1`.  Those two points
remain the exact limitations of this result.

## 1. Setup

Let `b` be odd, let `Omega` have size `2b`, and put

\[
 q=b(b-1),\qquad W={2b\choose b},\qquad
 M_b=2b^3+8b^2-16b.                                      \tag{1.1}
\]

Fix one coherent FIFO pairing/order as in Appendix I.  Its set of
three-rank collision differences is

\[
 \mathcal B\subseteq\mathbb F_2^b\setminus\{0\},
 \qquad |\mathcal B|\le M_b.                            \tag{1.2}
\]

Thus a state set contained in one coset of a linear code disjoint from
`mathcal B` gives tours jointly target-disjoint at ranks
`b-1,b,b+1`.

Let

\[
 2\le H=o(b/\log b),\qquad
 V_H=\sum_{j=1}^H{b\choose j}.                          \tag{1.3}
\]

Appendix I supplies a code `C_+ <= F_2^b` satisfying

\[
 \dim C_+=d=b-\rho,\qquad
 \rho=\lceil\log_2(4M_b)\rceil,
 \qquad C_+\cap\mathcal B=\varnothing,
 \qquad d(C_+^\perp)>H.                                \tag{1.4}
\]

## 2. A nested small balanced code

### Theorem 2.1 (exact tunable refinement)

If an integer `s` satisfies

\[
 1\le s\le d,\qquad
             V_H2^{-s}+2^{s-d}<1,                     \tag{2.1}
\]

then `C_+` contains an `s`-dimensional subcode `C_-` such that

\[
 \boxed{C_-\cap\mathcal B=\varnothing,
        \qquad d(C_-^\perp)>H.}                       \tag{2.2}
\]

Every coset of `C_-` therefore gives a balanced three-rank-disjoint bank
of exactly `2^s` tours and

\[
                         m=q2^s                       \tag{2.3}
\]

targets at each of ranks `b-1,b,b+1`.  Each coset of `C_+` is partitioned
into exactly `2^{d-s}` such microbanks, and all the microbanks in that
partition are jointly three-rank-disjoint.

#### Proof

Choose independent uniform vectors `X_1,...,X_s` from `C_+`.  For every
nonzero `y in F_2^b` of weight at most `H`, (1.4) says that the functional
`x -> y dot x` is nonzero on `C_+`.  Hence

\[
 \Pr(y\cdot X_i=0\text{ for every }i)=2^{-s}.
\]

A union bound over the `V_H` possible words gives failure probability at
most `V_H2^{-s}` for the dual-distance assertion.

The probability that the sampled vectors are linearly dependent is at
most

\[
 \sum_{i=0}^{s-1}2^{i-d}={2^s-1\over2^d}<2^{s-d}.       \tag{2.4}
\]

Condition (2.1) therefore leaves a choice for which the vectors are
independent and their span `C_-` has dual distance greater than `H`.
Containment in `C_+` proves collision avoidance in (2.2).

The state-projection argument of Appendix I now makes every coset exactly
`H`-wise uniform.  Collision avoidance makes each microbank internally
three-rank-disjoint.  If two states lie in microbanks contained in the
same coset of `C_+`, their difference lies in `C_+`; (1.4) therefore also
makes different microbanks in that parent coset mutually disjoint at the
three ranks.  The coset index is `|C_+|/|C_-|=2^{d-s}`.  This proves all
claims. \(\square\)

There is always a sublinear admissible value.  Namely, take

\[
                 s=\left\lceil\log_2(4V_H)\right\rceil. \tag{2.5}
\]

Then `V_H2^{-s}<=1/4`, while

\[
 \log_2V_H
 \le\log_2(H+1)+H\log_2(eb/H)=o(b).                  \tag{2.6}
\]

Thus `s=o(b)`, so `2^{s-d}=o(1)` and (2.1) holds for all sufficiently
large `b`.  At the live value

\[
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,           \tag{2.7}
\]

equations (2.3), (2.5), and (2.6) give

\[
                         m=2^{o(b)}.                   \tag{2.8}
\]

This is exponentially smaller than the `2^b/poly(b)`-tour banks obtained
by minimizing the syndrome rank in Appendix I.

## 3. The exact two-coordinate profile

Fix a microbank with `c=2^s` states and underlying pairing `P`.  For two
different ground coordinates `u,v`, the number of its middle targets
containing both is

\[
 N_{uv}(P)=
 \begin{cases}
 c(b-1),&\{u,v\}\in P,\\[3pt]
 \displaystyle {c(b-2)(b+1)\over4},&\{u,v\}\notin P.
 \end{cases}                                             \tag{3.1}
\]

Indeed, if `u,v` form one pair, that pair must be the doubled pair; the
empty pair then has `b-1` choices.  If they lie in different pairs, either
one of those pairs is doubled and the other split, contributing
`c(b-2)` in total, or both are split while the ordered empty/doubled pair
is chosen from the other `b-2` pairs, contributing
`c(b-2)(b-3)/4`.  Exact two-bit projection uniformity of `C_-` justifies
the factors `1/2` and `1/4`; their sum is the second line of (3.1).

It is also useful to record the equivalent XOR cut.  Put

\[
 \mathcal R_{uv}=\{C\in{\Omega\choose b}:|C\cap\{u,v\}|=1\}.
                                                               \tag{3.2}
\]

Then

\[
 { |\mathfrak B\cap\mathcal R_{uv}|\over m}=
 \begin{cases}
 \displaystyle {b-2\over b},&\{u,v\}\in P,\\[5pt]
 \displaystyle {1\over2}+{1\over b(b-1)},&\{u,v\}\notin P.
 \end{cases}                                             \tag{3.3}
\]

For the first line, exactly `(b-1)(b-2)` of the `q` flags split the pair.
For the second, the two flags whose empty and doubled pairs are the two
distinguished pairs always have XOR one; every other flag has XOR one for
exactly half of the states.

### Corollary 3.2 (necessary pairing balance)

Suppose `N` equal-size microbanks are middle-target-disjoint and leave
`E` middle targets uncovered.  If `n_(uv)` of their underlying pairings
contain the edge `{u,v}`, then, uniformly in `{u,v}`,

\[
 \boxed{\left|n_{uv}-{N\over2b-1}\right|
 \le {E\over m\delta_b},\qquad
 \delta_b={b^2-5b+2\over2b(b-1)}.}                    \tag{3.4}
\]

Here `delta_b>0` for `b>=5`.  In particular, if `E=o(W)` and
`Nm=W-E`, then

\[
                         n_{uv}={N\over2b-1}+o(N)       \tag{3.5}
\]

for every ground edge.

#### Proof

The full XOR cut has

\[
 |\mathcal R_{uv}|=2{2b-2\choose b-1}
                  ={b\over2b-1}W.                     \tag{3.6}
\]

The difference of the two bank densities in (3.3) is `delta_b`, and

\[
 {b\over2b-1}
 =\left({1\over2}+{1\over b(b-1)}\right)
   +{\delta_b\over2b-1}.                               \tag{3.7}
\]

Because the selected targets are distinct, (3.3) gives their exact count
inside the cut.  Its difference from the full count is at most `E`.
Substitute `Nm=W-E` and use (3.7); division by `m delta_b` proves (3.4).
Since `E=o(Nm)` and `delta_b ->1/2`, equation (3.5) follows. \(\square\)

Thus an arbitrary menu with the right cardinality is not enough: a
near-factor must asymptotically distribute its chosen pairings like a
one-factorization on every ground edge.

## 4. A three-rank-disjoint one-factorization packet

### Theorem 4.1 (balanced cross-pairing packet)

Fix an admissible `s` satisfying (2.1) with `s=o(b)` (in particular, one
may take (2.5)), and put `c=2^s` and `m=qc`.  For all sufficiently large
odd `b`, there are `2b-1` such microbanks, with one underlying pairing
from each factor of a one-factorization of `K_(2b)`, such that the banks
are jointly target-disjoint separately at ranks `b-1,b,b+1`.

Their middle-target union has `(2b-1)m` elements and is an exact
`2-(2b,b,lambda_2)` design, with

\[
 \boxed{\lambda_1={(2b-1)m\over2},\qquad
        \lambda_2={c\,b(b-1)^2\over2}.}               \tag{4.1}
\]

Here `lambda_1` is the number of selected middle targets containing one
fixed coordinate and `lambda_2` the number containing one fixed pair.

#### Proof

A one-factorization exists explicitly on
`{infinity} union Z_(2b-1)`: for `a in Z_(2b-1)`, take

\[
 P_a=\{\{\infty,a\}\}\cup
     \{\{a+j,a-j\}:1\le j\le b-1\}.                  \tag{4.2}
\]

Every ground edge occurs in exactly one `P_a`.  We first prove that one
microbank can be chosen on each `P_a` with the asserted disjointness.

For two different factors `P,Q`, the graph `P union Q` is a disjoint union
of even cycles of length at least four, and hence has at most `b/2`
components.  Regard a target as a zero--one coloring of `Omega`.  At any
of the ranks `b-1,b,b+1`, every target accessible to a coherent tour on a
pairing has at most three monochromatic pairing edges.  If a target is
accessible for both `P` and `Q`, choose the at most three exceptional
edges and their zero/one types for each pairing, then impose opposite
colors across every remaining edge of `P union Q`.  Deleting at most six
edges creates at most `b/2+6` components.  Consequently, for an absolute
constant `C`, the common accessible support at each one of the three ranks
has size at most

\[
                         Cb^6 2^{b/2}.                 \tag{4.3}
\]

This deliberately crude bound is sufficient.

Fix a template microbank on each factor and transport it by an independent
uniform automorphism of that factor.  The pair order, state-coordinate
labels, code, and coset are transported with the ground labels, so every
image is again a coherent-tour microbank; no cyclic order is held fixed.
The automorphism group is transitive on each occupancy-signature orbit.  A
fixed accessible target is therefore in the transported bank with
probability equal to the bank's orbit count divided by the orbit size.  The
four relevant ratios are

\[
 \begin{array}{c|c}
 \text{orbit}&\text{inclusion probability}\\ \hline
 b-1&\displaystyle {(b-1)c\over2^{b-1}}\\[3pt]
 b&\displaystyle {c\over2^{b-2}}\\[3pt]
 b+1\text{ internal}&\displaystyle {c\over(b-1)2^{b-4}}\\[3pt]
 b+1\text{ boundary}&\displaystyle {c\over2^{b-1}}.
 \end{array}                                             \tag{4.4}
\]

For example, the lower orbit has `b2^(b-1)` targets and a bank has `qc`
lower targets.  The middle orbit has `q2^(b-2)` targets and a bank has
`qc` targets.  The internal upper orbit has
`b(b-1)(b-2)2^(b-4)` targets and a bank has `b(b-2)c`; the boundary orbit
has `b2^(b-1)` targets and a bank has `bc`.

Every ratio in (4.4) is at most `2bc/2^b`.  Independence, (4.3), and a
union bound over the three ranks show that two randomly transported banks
collide with probability at most

\[
                         C'b^8 2^{2s-3b/2}.            \tag{4.5}
\]

There are fewer than `2b^2` bank pairs.  Since `s=o(b)`, the union bound
on (4.5) is `o(1)`.  Thus a simultaneous collision-free choice exists.

Every individual bank is an exact one-design, so the first formula in
(4.1) follows.  For a fixed ground pair, exactly one of the selected
underlying pairings contains it.  Summing (3.1) over that pairing and the
other `2b-2` pairings gives

\[
 c(b-1)+(2b-2){c(b-2)(b+1)\over4}
 ={c\,b(b-1)^2\over2},                                  \tag{4.6}
\]

independent of the pair.  Middle-target disjointness turns this incidence
count into the asserted exact design parameter. \(\square\)

The construction also explains (3.5): a one-factorization packet is the
smallest exact batch in which every ground pair receives its required
`1/(2b-1)` share of aligned pairings.

## 5. A finite orbit-packing lemma and the precise remaining gap

The microbank scale also gives a quantitative, but deliberately partial,
cross-pairing packing statement.

### Lemma 5.1 (one collision-free orbit batch)

Let `E` be the middle support of any microbank, `|E|=m`, and let
`pi_1,...,pi_L` be independent uniform permutations of `Omega`.  If

\[
                 e(2L-3){m^2\over W}\le1,             \tag{5.1}
\]

then there are choices of the permutations for which the `L` relabelled
banks have pairwise disjoint middle supports.

#### Proof

Transitivity on the middle layer gives
`Pr(C in pi_i E)=m/W` for every target `C`.  Hence, for `i ne j`,

\[
 \Pr(\pi_iE\cap\pi_jE\ne\varnothing)
 \le\mathbb E|\pi_iE\cap\pi_jE|={m^2\over W}.          \tag{5.2}
\]

The cases `L<=1` are trivial.  If `L=2`, condition (5.1) and (5.2)
make the collision probability at most `1/e<1`, so a disjoint choice
exists.  We may therefore assume `L>=3` below.

The event for the pair `{i,j}` is jointly independent of the family of
all pair-events using neither index, so its dependency degree is at most
`2L-4`.  The symmetric Lovasz local lemma applies under (5.1).

For self-containment, the lemma says that events of probability at most
`p`, each dependent on at most `D` others, have a simultaneous avoidance
when `ep(D+1)<=1`.  Set `x=1/(D+1)`.  Since
`(1-x)^D >= e^{-1}`, the hypothesis gives
`p<=x(1-x)^D`.  We prove by induction on `|S|` that

\[
 \Pr(A_i\mid A_j^c\ (j\in S))\le x                 \tag{5.3a}
\]

for every set `S` not containing `i`.  Split `S` into the neighbors
`S_1` of `i` and the nonneighbors `S_0`.  Independence from the latter
family, followed by the chain rule in the denominator, gives

\[
 \Pr(A_i\mid A_j^c\ (j\in S))
 \le {p\over
  \Pr(A_j^c\ (j\in S_1)\mid A_j^c\ (j\in S_0))}
 \le {p\over(1-x)^{|S_1|}}\le x.                    \tag{5.3b}
\]

The second inequality applies the induction hypothesis to each
conditional factor after ordering `S_1`; every conditioning set there is
smaller than `S`.  This proves (5.3a).  Finally, order all bad events and
use (5.3a) in the chain rule: every successive conditional complement is
at least `1-x`, so their intersection has positive probability.
\(\square\)

At (2.5), one may take `L=Theta(W/m^2)`, so this batch covers

\[
                         \Theta(W/m)                  \tag{5.4}
\]

middle targets.  This is exponentially more than one maximal Appendix-I
bank, but it is only a `Theta(1/m)=2^{-o(b)}` fraction of the middle layer.
Condition (5.1) cannot be applied with the `Theta(W/m)` banks needed for a
near-factor: it then misses by a factor of order `m`.

Theorem 4.1 and Lemma 5.1 therefore establish the following exact boundary.

* Small whole banks with exact `H`-wise balance exist and refine the old
  maximal banks without losing three-rank disjointness.
* Cross-pairing disjoint selection is possible for one exact
  one-factorization-balanced packet, and for an orbit batch covering a
  `Theta(1/m)` fraction.
* The next positive theorem must correlate about `m` such batches (or give
  an equivalent augmenting/absorption argument) while preserving target
  disjointness.  Independent priorities or the one-shot local lemma above
  do not supply that correlation.
* Even a middle near-factor would still need the physical all-offset repair
  and aggregate band-hole estimate in (I.41).

Thus the result removes bank size and two-coordinate pairing imbalance as
local obstructions.  It does not certify Gate `C_F` or coefficient one.
