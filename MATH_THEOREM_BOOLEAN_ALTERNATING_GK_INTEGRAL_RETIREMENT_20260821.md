# Alternating Greene--Kleitman chains give an integral Boolean retirement matching

**Status (2026-08-21).**  The Boolean-containment theorem below is proved.
Order the two `b`-letter blocks alternately and apply the Greene--Kleitman
symmetric-chain decomposition.  Every chain then alternates its `A`- and
`B`-steps.  After assigning its middle source to the persistent half-step
phase of the same orientation and retaining the longest-top chains allowed
by each physical phase capacity, one obtains an **integral** retired-chain
matching with aggregate uncovered target incidence `o(W_b)` for

\[
 H=O(\sqrt{b\log b}),\qquad W_b={2b\choose b}.       \tag{0.1}
\]

This removes generic growing-rank hypergraph rounding from the labelled
Boolean-containment problem.  It does not coinstantiate the chosen chains
inside common cyclic tight-factor orders or product atoms.  That later
order-bank packing problem is kept explicit in Section 6.

## 1. An exactly alternating symmetric-chain decomposition

Let `A={A_1,...,A_b}` and `B={B_1,...,B_b}` and order the coordinates of
`2^(A union B)` as

\[
                  A_1,B_1,A_2,B_2,\ldots,A_b,B_b.   \tag{1.1}
\]

Represent a set by its zero--one word in this order.  In the usual
Greene--Kleitman bracketing, scan from left to right and pair each zero with
the latest still-unpaired one to its left.  After the paired coordinates
are fixed, the unpaired coordinates carry a block of zeros followed by a
block of ones.  Moving the zero--one cut through those coordinates gives a
saturated symmetric chain.  These chains partition the Boolean lattice.

### Lemma 1.1 (alternating GK chains)

Every two consecutive upward edges in every Greene--Kleitman chain from
(1.1) have different block colours.  Hence the part of every chain above
rank `b` has one persistent alternating orientation.

#### Proof

The greedy pairs are noncrossing.  Between two consecutive unpaired
coordinates, all coordinates are therefore paired internally.  Their
number is even, so the two unpaired coordinates have indices of opposite
parity.  Upward chain edges flip consecutive unpaired coordinates, in
reverse order, and odd/even coordinate indices in (1.1) are exactly the
`A/B` colours.  Thus the colours alternate.  \(\square\)

Every symmetric chain crosses rank `b` once and contains every rank between
its bottom and top.  Consequently the full family of upper chain pieces
covers every target at every rank `b+q` exactly once.  A chain whose top has
rank `b+k` is said to have **top excess** `k`; it retires after offset `k`.

At its rank-`b` word there are `k` unpaired zeros and `k` unpaired ones.
The first upward edge flips the rightmost unpaired zero.  At that coordinate
the prefix walk first reaches height `-k`, so its coordinate index has the
same parity as `k`.  With convention (1.1),

\[
 \boxed{\text{top excess }k\text{ is `A`-first iff }k\text{ is odd}.} \tag{1.2}
\]

Chains with `k=0` carry no real upper target and may be given the formal
`B` parity without consequence.

## 2. Exact split-refined chain-top counts

For a chain with middle member `U`, write

\[
 r=|U\cap A|,qquad L_r={b\choose r}^{\!2},qquad
 E_{r,u}={b\choose{r+u}}{b\choose{r-u}},             \tag{2.1}
\]

with every out-of-range binomial interpreted as zero.  Let `n_(r,k)` be the
number of GK chains whose middle member has split `r` and whose top excess
is exactly `k`.  This count does not have a separate orientation parameter:
the orientation is forced by (1.2).

### Lemma 2.1 (refined GK top formula)

For `0<=k<b`, put

\[
 a=r-\lfloor k/2\rfloor,\qquad
 c=b-r-\lceil k/2\rceil.                            \tag{2.2}
\]

Then

\[
 \boxed{
 n_{r,k}={
 (k+1){b\choose{a-1}}{b\choose c}
 +k{b+1\choose a}{b-1\choose{c-1}}
 \over b-k}.}                                      \tag{2.3}
\]

Equivalently, the two parities telescope as

\[
 \boxed{
 \begin{aligned}
 n_{r,2u}
  &= {r+u\over b}E_{r,u}
    -{r+u+1\over b}E_{r,u+1},\\
 n_{r,2u+1}
  &= {b-r-u\over b}E_{r,u}
    -{b-r-u-1\over b}E_{r,u+1}.
 \end{aligned}}                                    \tag{2.4}
\]

For odd `b`, the unique `k=b` chain has middle split `(b-1)/2`; this is
also the terminal boundary term obtained by telescoping (2.4).

#### Proof

A chain top is a ballot word: on reading one as `+1` and zero as `-1`, all
prefix heights are nonnegative.  Let `x,y` mark ones in the `A,B`
positions and let `t` mark pairs of consecutive positions.  Write `D_A`
and `D_B` for the generating functions of balanced nonnegative excursions
when the next position has colour `A` and `B`, respectively.  First-return
decomposition gives

\[
 D_A=1+xtD_AD_B,qquad D_B=1+ytD_AD_B.              \tag{2.5}
\]

A ballot word ending at height `2k` has `2k` unmatched up-steps, alternating
in colour, with an excursion before, between, and after them.  Its
generating function is therefore

\[
                    (xyt)^kD_A^{k+1}D_B^k.          \tag{2.6}
\]

The top contains `r+ceil(k/2)` `A`-letters.  After removing the factor in
(2.6), the desired exponents are exactly `a,c` in (2.2).  Put

\[
 Q=tD_AD_B,qquad D_A=1+xQ,qquad D_B=1+yQ,
 \qquad Q=t(1+xQ)(1+yQ).                            \tag{2.7}
\]

For `m=b-k`, Lagrange inversion applied to
`(1+xQ)^(k+1)(1+yQ)^k` gives

\[
\begin{aligned}
 &[t^m x^a y^c](1+xQ)^{k+1}(1+yQ)^k\\
 &\quad={1\over m}[z^{m-1}x^ay^c]
 \left((k+1)x(1+xz)^b(1+yz)^b
       +ky(1+xz)^{b+1}(1+yz)^{b-1}\right),
\end{aligned}                                      \tag{2.8}
\]

which is (2.3).  Substituting `k=2u` and `k=2u+1` and using adjacent
binomial ratios gives (2.4).  At `k=b`, no paired coordinate remains, so
there is one chain; its middle word is `0^b1^b`, which has the stated split
when `b` is odd.  \(\square\)

### Corollary 2.2 (exact integral orientation masses)

Let `G^A_(r,u)` and `G^B_(r,u)` denote the numbers of `A`-first and
`B`-first chains, respectively, which survive to even offset `2u`.  Then

\[
 \boxed{
 G^A_{r,u}={b-r-u\over b}E_{r,u},
 \qquad
 G^B_{r,u}={r+u\over b}E_{r,u}.}                   \tag{2.9}
\]

At odd offset `2u+1`, the surviving masses are

\[
             G^A_{r,u},\qquad G^B_{r,u+1}.          \tag{2.10}
\]

Indeed, sum the odd and even identities in (2.4) from `u` to the terminal
boundary.  These are integer identities because they count chains.  Their
sum at even offset is `E_(r,u)`, the exact size of the target rectangle
with `A`-rank `r+u`; at odd offset the two neighboring source splits give
the exact Boolean rectangle quota.  Thus (2.9)--(2.10) are an integral
two-state Boolean flow, not rounded versions of real masses.

Both sequences in (2.9) are nonincreasing in `u`.  Using

\[
 {E_{r,u+1}\over E_{r,u}}
 ={(b-r-u)(r-u)\over(r+u+1)(b-r+u+1)},              \tag{2.11}
\]

this is immediate after multiplying by the respective linear factor.

## 3. Physical persistent-phase capacities

Assume now that `b` is an odd prime.  Use the half-step affine schedule

\[
 R(x)={b-1\over2}x\pmod b,qquad P_r=\{x:R(x)<r\}.  \tag{3.1}
\]

Put `d_r=|2r-b|`.  As proved by the half-step word calculation, for each
orientation there are at least

\[
 n_r=\max\!\left\{0,
       \left\lfloor{b-d_r-H+2\over2}\right\rfloor\right\} \tag{3.2}
\]

phase origins whose next `H` type letters alternate persistently in that
orientation.  Each phase has exactly `L_r/b` occurrence tokens, so the
integer capacity per orientation is

\[
                  K_r={n_rL_r\over b}.              \tag{3.3}
\]

Primality gives `b | binom(b,r)` for `0<r<b`, hence (3.3) is integral in
the central range.

For completeness, the half-step bit word has one interval of `d_r`
equal-bit edges.  Its complementary arc is therefore an alternating linear
word of length `b-d_r+1`, containing exactly `b-d_r-H+2` length-`H`
windows when this number is positive.  Their starting bits alternate, so
each orientation occurs at least the floor in (3.2).  This proves the phase
count used here directly.

For each split `r` and each orientation, order its GK chains by decreasing
top excess and retain the first `K_r`; ties are arbitrary.  Since survival
sets are nested by top excess, the number retained at each layer is exactly

\[
 \boxed{\min(K_r,G^A_{r,u})}
 \quad\hbox{or}\quad
 \boxed{\min(K_r,G^B_{r,u})},                       \tag{3.4}
\]

with the odd-layer indexing from (2.10).  No chain can revive.

There are enough chains of each formal orientation: for `H>=1`, (3.2)
gives `n_r<=(b-d_r)/2`, while (2.9) at `u=0` gives orientation-class
sizes `rL_r/b` and `(b-r)L_r/b`, whose minimum is
`(b-d_r)L_r/(2b)`.  A selected top-excess-zero chain is only bookkeeping:
it retires before the first real target and its token and source are omitted
from the actual `ell>=1` retired-chain matching.  Unused tokens and sources
are allowed.

Partition the `K_r` retained chains into `n_r` blocks of size `L_r/b` and
bijection each block to the occurrence tokens of one persistent affine
phase of the same orientation.  The side word of every selected GK chain
agrees with its token until retirement.  The GK decomposition already
makes the middle sources distinct and all real targets distinct, at every
rank simultaneously.  Discarding the bookkeeping pairs of top excess zero,
this assignment is an integral matching of tokens, sources, and labelled
target prefixes.

This last bijection is an abstract occurrence-token assignment.  It does
not assert that the chosen source and successor labels occur at that phase
inside one preassigned cyclic tight-factor order; Section 6 records that
separate gate.

## 4. Finite clamp bound

Assume

\[
 b\ge128,\qquad 8\le H\le b/16,\qquad d_r\le b/16. \tag{4.1}
\]

Write `L=L_r`, `d=d_r`, and `Delta=d+H`.  From (3.2),

\[
 K_r\ge {b-d-H+1\over2b}L.                         \tag{4.2}
\]

At `u=0` the two formal orientation masses in (2.9) are
`(b-r)L/b` and `rL/b`; their maximum is `(b+d)L/(2b)`.  Monotonicity and
(4.2) therefore show that every positive clamp excess is at most

\[
                         {\Delta\over b}L.           \tag{4.3}
\]

For `u` in the displayed band, the exact product formula gives

\[
 {E_{r,u}\over L}
 =\prod_{t=0}^{u-1}
 { (b-r-t)(r-t)\over(r+t+1)(b-r+t+1)}
 \le e^{-u^2/b}.                                    \tag{4.4}
\]

Indeed the negative logarithm of the `t`th factor is

\[
 \log\!\left(1+{2t+1\over b-r-t}\right)
 +\log\!\left(1+{2t+1\over r-t}\right),            \tag{4.5}
\]

and (4.1) keeps both fractions below one.  Using
`log(1+x)>=x/2` and summing `2t+1` proves (4.4).

For `u<=sqrt b`, `1-e^(-u^2/b)>=u^2/(2b)`.  The `A` fraction in (2.9)
decreases with `u`, while the `B` fraction increases by only `u/b` before
being multiplied by (4.4).  Since both initial fractions are at least
`15/32`,

\[
 \begin{aligned}
 G^A_{r,0}-G^A_{r,u}&\ge {u^2\over5b}L,\\
 G^B_{r,0}-G^B_{r,u}&\ge {u^2\over16b}L
                         \qquad(u\ge8).             \tag{4.6}
 \end{aligned}
\]

If `u>=sqrt b`, (4.4) and the central fractions give
`G^A_(r,u),G^B_(r,u)<K_r`.  Hence a positive excess can occur only for

\[
                         u<8+4\sqrt\Delta.           \tag{4.7}
\]

Each `G` value occurs on at most two displayed layers.  Combining
(4.3)--(4.7), the aggregate clamp deficit contributed by one core split is

\[
 \boxed{D_r\le {64\over b}(d_r+H+1)^{3/2}L_r.}      \tag{4.8}
\]

The numerical constant is deliberately loose; only its uniformity matters.
If `H<8`, the same bound follows directly from (4.3), after enlarging the
already loose constant, because there are fewer than eight displayed
layers.  Thus the lower bound on `H` in (4.1) is only a convenience in the
decay argument.

## 5. Aggregate integral theorem

Under the squared-binomial law

\[
 \Pr(\mathbf R=r)={L_r\over W_b},                   \tag{5.1}
\]

one has the exact hypergeometric moment

\[
 \mathbb E(2\mathbf R-b)^2={b^2\over2b-1},
 \qquad
 \mathbb E|2\mathbf R-b|^{3/2}
 \le\left({b^2\over2b-1}\right)^{3/4}.             \tag{5.2}
\]

The omitted source tail `d_r>b/16` has probability at most
`2e^(-b/512)`.  Charging every one of its at most `H` upper incidences, and
using `(x+y)^(3/2)<=sqrt(2)(x^(3/2)+y^(3/2))` in (4.8), gives

\[
 \boxed{
 {D_{\rm GK}\over W_b}
 \le {64\sqrt2\over b}
 \left[
   \left({b^2\over2b-1}\right)^{3/4}
   +(H+1)^{3/2}
 \right]
 +2H e^{-b/512}.}                                   \tag{5.3}
\]

Here `D_GK` is the total number of targets missed, summed over all offsets
`1<=q<=H`, relative to the exact full GK cover.

### Theorem 5.1 (integral Boolean alternating retirement)

For odd primes `b` and

\[
                         H=O(\sqrt{b\log b}),        \tag{5.4}
\]

there is an integral occurrence-token/source/labelled-target retired-chain
matching, using only persistent half-step affine phases, whose real-target
incidence value is

\[
 \boxed{
       \sum_{q=1}^H{2b\choose{b+q}}-o(W_b).}        \tag{5.5}
\]

Indeed (5.3) is
`O(b^(-1/4)+b^(-1/4)log^(3/4)b)+e^(-Omega(b))=o(1)`.
All integrality is literal: chains, sources, tokens, and target sets are
not fractionally weighted.

## 6. Exact relation to product atoms and the remaining order gate

One selected retired chain can always be embedded as one distinguished
prefix of a two-block product atom.  If its middle source is
`U=X union Y`, choose a cyclic `A`-order having `X` as its rank-`r` window
and listing the future added `A`-labels immediately afterward.  Do the same
on `B` with `Y` and the future `B`-labels.  Use the half-step type word and
the selected persistent phase origin.  The atom then reproduces the whole
retired chain prefix exactly.  Independent counter translations generate
the other `b^2-1` source paths of that product atom; internal band simplicity
makes those translated targets distinct **inside that atom**.

This observation does not partition the GK decomposition into physical
product atoms.  The other translated paths are dictated by the same two
cyclic orders and need not be the GK chains through their translated
sources.  Greene--Kleitman bracketing is linear-boundary dependent and is
not invariant under arbitrary independent cyclic `A/B` relabellings.  For
example, at `b=3` the long-chain middle word `000111` first adds `A_2`.
Cyclically relabelling only the `A` coordinates sends the source word to
`100101`; its GK chain still first adds `A_2`, rather than the translated
label `A_3`.
Different prototype atoms can also share sources or upper targets.

Thus the remaining statement is precisely an orbit-packing/coinstantiation
theorem: choose product-atom prototypes so that their entire translated
source and target orbits realize almost all of the abstract GK matching
without collisions, while the local cyclic orders come from the required
tight-factor banks.  Arbitrarily bijecting GK chains to phase tokens in
Section 3 does not prove that theorem.  No claim that the canonical GK
chains themselves partition into product orbits is made here.

## 7. H100 audit

The companion checker
`scratch/audit_boolean_alternating_gk_integral_retirement_20260821.py`
constructs the GK chains literally for small `b`, verifies the Boolean
partition, symmetry, alternating colours, top-excess orientation, formulas
(2.3)--(2.10), the longest-top selection rule, token divisibility, and
source/target disjointness.  It also replays the exact finite clamp ledger
from (3.4) and checks the inequalities used in (4.2)--(4.8) over its stated
finite audit range.  The asymptotic conclusion is the analytic estimate
(5.3), not a numerical extrapolation.
