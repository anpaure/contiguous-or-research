# Hashed three-seed `B_4` packets and uniform fixed-frame diffusion

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

The first-eligible `B_4` atlas in
`MATH_THEOREM_FIRST_ELIGIBLE_B4_SCD_PACKET_FACTOR_20260726.md` uses one
fixed coordinate pairing.  Its local cycle

\[
 14\to12\to23\to34\to14                              \tag{0.1}
\]

alternately flips the pairs `24` and `13`.  Consequently every retained
depth-`q` window is internal to the single global matching obtained by
putting

\[
                         13\mid24                     \tag{0.2}
\]

in every four-block.  If `G=W-e^{-\Omega(m)}W` is the retained owner
mass, its exact pair-frame occurrence distribution is therefore

\[
 \boxed{
 I_{P_*,q}^-=I_{P_*,q}^+=G,
 \qquad
 A_{P_*,q}^-=A_{P_*,q}^+=0.}                         \tag{0.3}
\]

Here `I` and `A` denote respectively the internal and escaping
depth-`q` occurrence masses.  The exclusive native seed-label census is

\[
 \boxed{
 \bigl(\operatorname {Occ}_{M_0}(q),
       \operatorname {Occ}_{M_1}(q),
       \operatorname {Occ}_{M_2}(q)\bigr)
 =(0,G,0)}                                            \tag{0.3a}
\]

for the exclusive native seed labels, at every depth.  Individual shallow
windows may also be contained in other full matching extensions of their
active pairs, but the whole atlas has the single common support frame
`P_*`; this is the quantity used by the Hall cut.

The window-level fixed-frame Hall theorem immediately gives

\[
 M_q^\pm\ge D_{m,q}.                                 \tag{0.4}
\]

Thus for `q=x\sqrt m+o(\sqrt m)` and fixed `x>0`,

\[
 \boxed{
 M_q^-\ge(\delta(x)-o(1))W,
 \qquad
 M_q^+\ge(\delta(x)-o(1))W,}                         \tag{0.5}
\]

where

\[
 \delta(x)=e^{-x^2}\Phi(x/2)-\Phi(-3x/2)>0.          \tag{0.6}
\]

So the current atlas fails before its open cross-packet flag problem is
reached.

There is, however, an exact packet-preserving repair of this particular
obstruction.  Use the three perfect matchings of a four-block,

\[
 M_0=12\mid34,qquad
 M_1=13\mid24,qquad
 M_2=14\mid23.                                      \tag{0.7}
\]

and their three relabelled cyclic-SCD seeds.  Freeze an anchor of
`a=(\log_2 3+\eta)r+O(1)` coordinates and hash its subset, separately
inside every anchor-cardinality layer, almost uniformly to a seed vector

\[
                         \theta\in\{0,1,2\}^r.        \tag{0.8}
\]

Scan the remaining four-blocks sequentially.  To select position `j`,
take the first block whose local state belongs to the orientation square
of `M_{\theta_j}`.  Varying the selected block inside that square leaves
the anchor, `\theta`, every skipped block, and the entire selected-index
sequence fixed.  Hence the construction again partitions all but
`e^{-\Omega(m)}W` middle owners into canonical `Q_{2r}` packets, with the
same exact `C_{4r}` factor and the same two-sided intrapacket injectivity
through depth `r`.

The new atlas is uniformly frame-diffuse.  For every fixed perfect
matching `P` of the `2m` coordinates and every `1\le q\le r`,

\[
 \boxed{
 I_{P,q}^\pm
 \le
 \bigl(3^{-q}+e^{-c_\eta r}+e^{-c m}\bigr)W.}         \tag{0.9}
\]

Equivalently,

\[
 \boxed{
 A_{P,q}^\pm
 \ge
 \bigl(1-3^{-q}-e^{-c_\eta r}-e^{-cm}\bigr)W.}       \tag{0.10}
\]

At every fixed Gaussian depth the internal mass is
`e^{-\Omega(\sqrt m)}W`, uniformly over **all** fixed pairings, including
pairings which use different local matchings in different four-blocks or
which pair coordinates across blocks.  Therefore no Gaussian cut based
only on one perfect-matching type survives.

**Subsequent audit correction.**  This does not remove the coarser cut
created by the fixed partition into four-blocks.  Every within-block seed
preserves the common odd-block set of its lower and upper shadows and
changes the number of rank-three blocks by exactly `q`.  The exact side
sizes are `4^s\binom sk` and `4^s\binom{s}{k+q}`.  The resulting Gaussian
Hall obstruction is proved in
`MATH_OBSTRUCTION_B4_ODD_BLOCK_GAUSSIAN_HALL_CUT_20260726.md`.  Thus the
hashed construction is a correct frame-label diffuser, but it is still
not a coefficient-one candidate without cross-block recouplings.

## 1. Audit of the original seed

Let `B={1,2,3,4}`.  Consecutive moves in (0.1) are

\[
\begin{array}{c|c}
14\to12&4\to2,\\
12\to23&1\to3,\\
23\to34&2\to4,\\
34\to14&3\to1.
\end{array}                                           \tag{1.1}
\]

Thus its two physical directions are exactly the pairs `24` and `13`.
Moreover

\[
 \{14,12,23,34\}
 =\{S\in\tbinom B2:|S\cap13|=|S\cap24|=1\}.          \tag{1.2}
\]

It is the orientation square of `M_1=13\mid24`, not merely an abstract
copy of `Q_2`.

Partition the ambient coordinates into four-blocks and put `M_1` in
each block; pair the at most two leftover coordinates together.  Call
the resulting global matching `P_*`.  Every active move in every packet
is a flip of a pair of `P_*`.  The recursive Hamming order uses distinct
local blocks in every window of length at most `r`, so every such window
consists of distinct `P_*`-pair flips.  This proves (0.3).

For completeness, the window-level fixed-frame inequality says that an
exact owner factor with `A_{P,q}^\pm` non-`P`-internal signed windows
satisfies

\[
 M_q^\pm\ge D_{m,q}-A_{P,q}^\pm.                    \tag{1.3}
\]

where

\[
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+.                      \tag{1.4}
\]

\[
 V_f={m!\over f!^2(m-2f)!}\,2^{m-2f}.               \tag{1.5}
\]

and

\[
 T_{f,q}=
 {m!\over f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.           \tag{1.6}
\]

Indeed, internal starts of source type `f` can cover at most `V_f`
literal targets of target type `f`, while the exceptional starts can
repair at most `A_{P,q}^\pm` further targets.  Substitution of (0.3) into
(1.3), followed by the Gaussian census

\[
 {D_{m,q}\over W}\to\delta(x).                       \tag{1.7}
\]

proves (0.4)--(0.5).

The exponentially small middle leave does not reduce this lower bound:
omitting sources can only create additional holes.

## 2. The three relabelled cyclic-SCD seeds

For `c\in\{0,1,2\}`, define

\[
 \mathcal A_c=
 \{S\in\tbinom B2:|S\cap e|=1\text{ for every }e\in M_c\}.          \tag{2.1}
\]

Explicitly,

\[
\begin{aligned}
 \mathcal A_0&=\{13,14,23,24\},\\
 \mathcal A_1&=\{12,14,23,34\},\\
 \mathcal A_2&=\{12,13,24,34\}.
\end{aligned}                                         \tag{2.2}
\]

Use the oriented cycles

\[
\begin{aligned}
 C_0&=(13,14,24,23),\\
 C_1&=(14,12,23,34),\\
 C_2&=(12,13,34,24).
\end{aligned}                                         \tag{2.3}
\]

Each alternately flips the two edges of `M_c`.  Its four lower edge
intersections are four different singletons, and its four upper edge
unions are four different triples.  Thus every `C_c` has the same
two-sided rank-one flag injectivity as the original seed.  Coordinate
relabeling transports the full local SCD, so all three are literal cyclic
SCD seeds.

Two elementary facts will drive the frame census.

### Lemma 2.1 (equal rank inventory)

For every `c`,

\[
 \sum_{S\in\mathcal A_c}z^{|S|}=4z^2.                \tag{2.4}
\]

and hence the failure inventory is

\[
 \sum_{S\subseteq B,\ S\notin\mathcal A_c}z^{|S|}
 =(1+z)^4-4z^2.                                      \tag{2.5}
\]

Both polynomials are independent of `c`.

### Lemma 2.2 (one frame value per physical direction)

Fix one of the two abstract directions of the oriented squares.  The
three corresponding physical pairs, one from each `M_c`, belong to three
different one-factors of `K_4`.  Any two pairs from different one-factors
intersect.  Therefore a fixed perfect matching of the ambient coordinates
contains the corresponding pair for at most one value of `c`.

The conclusion remains true if the ambient matching pairs some
coordinates of `B` outside the block: then it contains at most one edge
of `B`, and hence again at most one compatible value of `c` for the
specified abstract direction.  \(\square\)

## 3. A middle-slice-balanced ternary anchor

Fix `\eta>0` and let `A` be a reserved anchor set of size

\[
 a=\left\lceil(\log_2 3+\eta)r\right\rceil.           \tag{3.1}
\]

Put

\[
                         \Theta=\{0,1,2\}^r,
 \qquad |\Theta|=3^r.                                \tag{3.2}
\]

For every `0\le k\le a`, partition the layer `\binom Ak` among the
members of `\Theta` as evenly as possible: every fibre has size either

\[
 \left\lfloor{\binom ak\over3^r}\right\rfloor
 \quad\text{or}\quad
 \left\lceil{\binom ak\over3^r}\right\rceil.         \tag{3.3}
\]

This defines a deterministic map

\[
                         \vartheta:2^A\to\Theta.      \tag{3.4}
\]

### Lemma 3.1 (uniformity on the middle slice)

Let `X` be uniform in `\binom{[2m]}m`.  If `r=o(m)`, then

\[
 \left\|
 \mathcal L(\vartheta(X\cap A))-\operatorname {Unif}(\Theta)
 \right\|_{\rm TV}
 \le e^{-c_\eta r}.                                  \tag{3.5}
\]

The same estimate holds after fixing the entire configuration outside
`A`, except when the forced value `|X\cap A|` lies in an anchor-size tail
whose total middle-slice mass is `e^{-c_\eta r}`.

#### Proof

Conditional on `|X\cap A|=k`, every member of `\binom Ak` has the same
number

\[
                         \binom{2m-a}{m-k}.           \tag{3.6}
\]

of completions.  Thus (3.3) gives conditional total-variation error at
most

\[
                         \min\left(1,{3^r\over2\binom ak}\right).   \tag{3.7}
\]

Choose a small constant `\epsilon=\epsilon(\eta)>0`.  Uniformly for

\[
                         |k-a/2|\le\epsilon a.        \tag{3.8}
\]

the entropy estimate for binomial coefficients and (3.1) give

\[
                         \binom ak\ge3^r e^{c_\eta r}.              \tag{3.9}
\]

The hypergeometric anchor count in a uniform middle set has mean `a/2`;
the standard exponential-moment bound gives

\[
 \Pr\bigl(\bigl||X\cap A|-a/2\bigr|>\epsilon a\bigr)
 \le2e^{-c\epsilon^2a}=e^{-\Omega_\eta(r)}.          \tag{3.10}
\]

Average (3.7) over `k` and use (3.9)--(3.10).  If the outside
configuration is fixed, `k` is fixed and all anchor `k`-sets remain
equiprobable, proving the conditional statement.  \(\square\)

No random hash is being invoked.  The layerwise equitable partitions in
(3.3) may be fixed arbitrarily once and for all.

## 4. Sequential first-eligible packets

Partition the coordinates outside `A` into ordered four-blocks

\[
                         B_1<B_2<\cdots<B_b.          \tag{4.1}
\]

leaving at most three further coordinates frozen.

For a middle owner `X`, put

\[
                         \theta(X)=\vartheta(X\cap A).              \tag{4.2}
\]

Scan the blocks from left to right.  Initially `j=1`.  While `j\le r`,
select the first unused block `B_i` satisfying

\[
                         X\cap B_i\in\mathcal A_{\theta_j}.         \tag{4.3}
\]

record it as `i_j`, and then increment `j`.  Retain `X` if all `r`
positions are selected.

For a retained owner, define its packet by freezing the anchor, every
skipped block, every block after `i_r`, and the leftover coordinates,
while allowing

\[
                         Y\cap B_{i_j}\in\mathcal A_{\theta_j}
 \qquad(1\le j\le r).                                \tag{4.4}
\]

### Lemma 4.1 (exact context stability)

Every `Y` in the packet of `X` has the same anchor subset, seed vector,
selected indices, and packet as `X`.

#### Proof

The anchor is frozen, so `\theta(Y)=\theta(X)`.  Proceed inductively over
`j`.  All blocks skipped before `i_j` are frozen and still fail the test
for `\mathcal A_{\theta_j}`.  The selected block `i_j` remains in
`\mathcal A_{\theta_j}` by (4.4), so it remains the first success for
stage `j`.  This proves the selected indices one at a time.  All remaining
packet data are then identical.  \(\square\)

Consequently the retained owners are partitioned into packets

\[
 \mathcal A_{\theta_1}\times\cdots\times
 \mathcal A_{\theta_r}\cong Q_2^r=Q_{2r}.            \tag{4.5}
\]

### Lemma 4.2 (small middle leave)

Assume `r=o(m)`.  The number `E` of middle owners for which the scan finds
fewer than `r` selected blocks satisfies

\[
                         E=e^{-\Omega(m)}W.           \tag{4.6}
\]

#### Proof

Under independent fair bits, conditional on the anchor and on every
previous scan decision, a fresh four-block passes (4.3) with probability
`4/16=1/4`.  This probability is independent of the requested seed value.
There are `(1-o(1))m/2` fresh blocks and only `r=o(m)` successes are
required, so a Chernoff bound gives failure probability `e^{-\Omega(m)}`.
Conditioning on total size `m` costs only

\[
 {2^{2m}\over\binom{2m}m}=O(\sqrt m).                \tag{4.7}
\]

which is absorbed by the exponential.  \(\square\)

### Theorem 4.3 (exact packet and cycle factor)

Let `r` be a power of two, put `h=2r`, and assume

\[
                         H\ll r=o(m).                 \tag{4.8}
\]

The retained middle owners admit an exact owner-disjoint factor into
physical `C_{4r}=C_{2h}` cycles.  Every signed depth-`q` shadow map is
injective inside each packet for `q\le r`.

#### Proof

Lemma 4.1 gives the packet partition (4.5).  Install the same recursive
Hamming factor in abstract `Q_{2r}` coordinates, making the two directions
of each local seed siblings.  Every local seed is a physical square, so
all cycles are physical.  A window of length at most `r` touches any
local block at most once.  The local singleton and triple edge labels of
every `C_c` are injective, so the touched block and starting local state
are recovered exactly from either signed shadow, as in the original
`B_4` proof.  \(\square\)

## 5. Uniform pair-frame distribution

Fix an arbitrary perfect matching `P` of all `2m` coordinates.  It may
pair coordinates inside four-blocks, across distinct four-blocks, into
the anchor, or into the frozen remainder.

For a signed depth-`q` occurrence in a retained packet, write its abstract
direction list as

\[
 (j_1,\epsilon_1),\ldots,(j_q,\epsilon_q).           \tag{5.1}
\]

where `j_s\in[r]` is the selected packet position and
`\epsilon_s\in\{0,1\}` is one of the two directions of its local square.
For `q\le r`, the positions `j_1,\ldots,j_q` are distinct.

Fix the anchor cardinality, the scan success/failure history, the actual
selected block indices, and the abstract Hamming cycle and start, and sum
over all skipped and frozen local states consistent with that history.
By Lemma 2.1, the resulting coefficient weight is independent of the seed
vector `\theta`: before an abstract packet vertex is fixed a selected
block contributes `4z^2`; after the vertex is fixed it contributes `z^2`.
A skipped block contributes `(1+z)^4-4z^2`.  All three expressions are
independent of the requested seed.  Thus the only remaining condition for
the occurrence to be `P`-internal is

\[
 d_{\theta_{j_s},\epsilon_s}(B_{i_{j_s}})\in P
 \qquad(1\le s\le q).                                \tag{5.2}
\]

where `d_{c,\epsilon}(B_i)` is the physical coordinate pair representing
abstract direction `\epsilon` in seed `c` on block `B_i`.

By Lemma 2.2, each constraint in (5.2) permits at most one value of the
distinct coordinate `\theta_{j_s}`.  Therefore at most

\[
                         3^{r-q}                      \tag{5.3}
\]

of the `3^r` seed vectors make the occurrence `P`-internal.

### Theorem 5.1 (uniform fixed-frame diffusion)

For every perfect matching `P`, both signs, and every `1\le q\le r`,

\[
 \boxed{
 I_{P,q}^\pm
 \le
 \left(3^{-q}+e^{-c_\eta r}+e^{-cm}\right)W.}        \tag{5.4}
\]

#### Proof

On the central anchor-cardinality layers, Lemma 3.1 makes the seed-vector
law `e^{-c_\eta r}`-close to uniform.  For the uniform law, (5.3) bounds
the internal fraction by `3^{-q}` after every other item of data is fixed.
The coefficient inventories (2.4)--(2.5) justify this conditioning on the
middle rank exactly; no independent-row approximation is used.  The
anchor-size tails contribute `e^{-c_\eta r}W`, and the failed packet scan
contributes `e^{-cm}W` by Lemma 4.2.  Summing the conditional estimates
proves (5.4).  Reversing a Hamming cycle changes the abstract direction
order but not Lemma 2.2 or the distinct-position property, so the same
bound holds for the opposite sign.  \(\square\)

Subtracting (5.4) from the retained mass proves (0.10).  In particular,
if `q=x\sqrt m+o(\sqrt m)` and `r\gg\sqrt m`, then uniformly in `P`,

\[
                         I_{P,q}^\pm\le e^{-\Omega_x(\sqrt m)}W+o(W). \tag{5.5}
\]

and

\[
                         A_{P,q}^\pm=W-o(W).          \tag{5.6}
\]

The fixed-frame escape theorem requires only

\[
                         A_{P,q}^\pm\ge(\delta(x)-o(1))W.           \tag{5.7}
\]

Equations (5.6)--(5.7) show that every perfect-matching-type Gaussian
deficit is cleared with macroscopic slack.  They do not address the
odd-block cut below.

## 6. The surviving fixed-block obstruction

The construction proves all of the following simultaneously:

1. canonical context stability;
2. exponentially small middle leave;
3. exact owner-disjoint physical cycle factors;
4. exact two-sided intrapacket shadow injectivity;
5. one common chronology through every depth `q\le r`; and
6. uniform escape from every fixed coordinate pairing.

The implication

\[
 A_{P,q}^\pm\text{ large for every }P
 \quad\Longrightarrow\quad
 M_q^\pm=o(W)                                        \tag{6.1}
\]

is false here for an explicit reason.  All three seeds move only inside
the same four-blocks.  If `J` is the common set of odd-rank blocks and the
lower target has `k` rank-three blocks, then the paired upper target has
`k+q`.  Conditional on the exact outside trace, the two target sides have
sizes

\[
 4^{|J|}\binom{|J|}{k},
 \qquad
 4^{|J|}\binom{|J|}{k+q}.                            \tag{6.2}
\]

For the radius-balanced start mass `P_q=N_q+o(W)`, the resulting exact
max-side Hall inequality gives

\[
 M_q^-+M_q^+
 \ge
 \bigl(e^{-x^2}(2\Phi(x)-1)-o(1)\bigr)W             \tag{6.3}
\]

at `q=x\sqrt m+o(\sqrt m)`.  This is positive for every fixed `x>0`.

The original one-seed atlas is ruled out by (0.5).  The hash eliminates
that matching-label obstruction but not (6.3).  A viable successor must
use cross-block coordinate exchanges, change the block partition with
context or phase, or install a larger exact trade which moves occurrences
between distinct odd-block sets `J`.
