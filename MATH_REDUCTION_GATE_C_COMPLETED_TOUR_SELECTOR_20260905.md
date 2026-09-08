# Gate C: exact completed-tour selector reduction

**Status (2026-09-05).**  This note assumes the proved coherent-tour gap
lemma: a completed coherent FIFO tour is a cyclic singleton word of length
`b^2`, and every window of length at most `2b-2` is clean.  It corrects the
remaining selector statement and separates three facts.

1. Once the `q=b(b-1)` internal middle targets are globally disjoint, the
   middle layer and serialization already cost only `o(W)` beyond the sharp
   baseline.  The sole remaining compiler condition is aggregate coverage
   at the **nonzero** band offsets.
2. That condition itself forces an asymptotically full internal tour
   matching and simultaneous near-injectivity at a growing collection of
   central ranks.  Cleanliness has removed the boundary-repair problem, but
   not the correlated selector problem.
3. The selector has an exact symmetric fractional solution.  Independent
   rounding leaves Poisson-sized holes, and even very strong low-order
   pseudorandomness of a residual does not force it to contain one tour.

No coefficient-one construction is claimed.

Throughout, `b>=5` is odd,

\[
 W={2b\choose b},\qquad q=b(b-1),\qquad
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,
 \qquad g=b+H,                                      \tag{0.1}
\]

and `b` is sufficiently large that `g<=2b-3` (the weaker cleanliness
statement itself only needs `g<=2b-2`).  Put

\[
 W_h={2b\choose b+h}\qquad(-H\le h\le H).          \tag{0.2}
\]

For a completed tour `T` with cyclic word `w_T`, define its rank-`b+h`
support

\[
 S_h(T)=\{I_{b+h}^{w_T}(a):a\in\mathbb Z_{b^2}\},   \tag{0.3}
\]

where `I_l^w(a)` is the set of the `l` cyclic letters beginning at `a`.
For a family `mathcal T` of `t` tours, set

\[
 U_h(\mathcal T)=\bigcup_{T\in\mathcal T}S_h(T),
 \qquad h_h(\mathcal T)=W_h-|U_h(\mathcal T)|.      \tag{0.4}
\]

Every member of every `S_h(T)` is a genuine `(b+h)`-set by the gap lemma.

## 1. The exact compiler-defect identity

Write each cyclic tour period followed by its first `g-1` letters, and
append one set-valued letter for every missing band target and every
nonempty target outside the band.  The resulting word has length at most

\[
 (b^2+g-1)t+\sum_{h=-H}^{H}h_h(\mathcal T)
 +\sum_{|s-b|>H}{2b\choose s}.                       \tag{1.1}
\]

Every desired cyclic window stays inside its own linearized block, so no
condition at a join is needed.  Define the completed-middle repetition
excess

\[
 \Delta_0(\mathcal T)=b^2t-|U_0(\mathcal T)|\ge0.    \tag{1.2}
\]

Since `h_0=W-|U_0|`, the tour part of (1.1) satisfies the exact algebraic
identity

\[
 \boxed{
 b^2t+(g-1)t+\sum_{h=-H}^{H}h_h
 =W+(g-1)t+\Delta_0
   +\sum_{0<|h|\le H}h_h.}                           \tag{1.3}
\]

The Gaussian tail in (1.1) is `o(W)`.  For example, Hoeffding's bound and
`W=Theta(4^b/sqrt b)` give

\[
 \sum_{|s-b|>H}{2b\choose s}
 \le 2\,4^b e^{-H^2/b}=O(Wb^{-3/2})=o(W).            \tag{1.4}
\]

Consequently the exact nonnegative defect conditions furnished by this
accounting are

\[
 (g-1)t=o(W),\qquad \Delta_0=o(W),\qquad
 \sum_{0<|h|\le H}h_h=o(W).                          \tag{1.5}
\]

The middle hole count should not be charged once more as an independent
gate: (1.3) shows that the unfilled part of the middle layer cancels the
unused part of the `b^2t` base-word budget.  What matters there is only
repetition excess.

## 2. Internal disjointness makes the first two conditions automatic

Let `K(T) subseteq S_0(T)` be the `q=b(b-1)` internal middle targets of a
tour.  Suppose

\[
 K(T)\cap K(T')=\varnothing\qquad(T\ne T').          \tag{2.1}
\]

The internal targets in one tour are distinct, so

\[
 qt\le W,qquad |U_0|\ge qt.                         \tag{2.2}
\]

It follows that

\[
 t\le {W\over q},\qquad
 \Delta_0\le(b^2-q)t=bt\le {W\over b-1}=o(W),       \tag{2.3}
\]

and, because `H=o(b)`,

\[
 (g-1)t\le{(b+H-1)W\over b(b-1)}=O(W/b)=o(W).       \tag{2.4}
\]

Combining (1.1)--(1.4) proves the precise reduction

\[
 \boxed{
 \nu(2b)\le W+O(W/b)
 +\sum_{0<|h|\le H}
   \left({2b\choose b+h}-|U_h(\mathcal T)|\right)
 +o(W).}                                             \tag{2.5}
\]

Thus, under (2.1), the corrected remaining selector condition is

\[
 \boxed{
 \sum_{0<|h|\le H}
 \left[{2b\choose b+h}
 -\left|\bigcup_{T\in\mathcal T}
   \{I_{b+h}^{w_T}(a):a\in\mathbb Z_{b^2}\}\right|
 \right]=o(W).}                                     \tag{2.6}
\]

This is the intended repair of the malformed displayed equation (7) in
the working text.  A bare assertion that the union has size `o(W)` has the
opposite meaning; the quantity which must be `o(W)` is the **sum of the
deficits**, with the rank index quantified.  Including `h=0` in (2.6) is
harmless but redundant under the condition below.

## 3. Off-middle coverage forces the near-perfect middle matching

Condition (2.6) is not a substantially weaker substitute for the middle
matching.  The single upper rank `b+1` already forces the matching to have
asymptotically full size.  A tour has at most `b^2` rank-`b+1` targets, so

\[
 h_1\ge W_1-b^2t={b\over b+1}W-b^2t.                \tag{3.1}
\]

If (2.6) holds, then `h_1=o(W)`, and hence

\[
 b^2t\ge {b\over b+1}W-o(W).                        \tag{3.2}
\]

Multiplying by `q/b^2=(b-1)/b` and using (2.2),

\[
 \boxed{qt=W-o(W),\qquad
 t=(1+o(1)){W\over b^2}.}                            \tag{3.3}
\]

In particular, literal all-band coverage cannot be obtained from a small
tour subfamily followed by inexpensive middle singletons: the nearest
upper layer forces almost all available internal middle capacity to be
used.

There is a stronger near-injectivity consequence.  The distinct-support
census of one completed tour is

\[
 d_h:=|S_h(T)|=
 \begin{cases}
 b(b+h+1),&-H\le h\le-1,\\
 b^2,&0\le h\le H.
 \end{cases}                                         \tag{3.4}
\]

For `h<0`, this follows by recording the cyclic interval of occupied pair
indices and the cut between old and new transversal choices; for `h>=0`,
the start is recoverable from the two successive occupancy boundaries.
Put

\[
 R_h(\mathcal T)=d_ht-|U_h(\mathcal T)|\ge0          \tag{3.5}
\]

for the repeated-occurrence excess at rank `b+h`.  For every integer
`R=R_b=o(b^{1/3})`, (2.1) and (2.6) imply

\[
 \boxed{\sum_{1\le|h|\le R}R_h(\mathcal T)=o(W).}    \tag{3.6}
\]

Indeed,

\[
 R_h=h_h+(d_ht-W_h).                                 \tag{3.7}
\]

For `1<=j<=R`,

\[
 {W_j\over W}={W_{-j}\over W}
 =\prod_{i=0}^{j-1}{b-i\over b+i+1}
 \ge1-{j^2\over b}.                                 \tag{3.8}
\]

The last inequality is `prod(1-x_i)>=1-sum x_i` with
`x_i=(2i+1)/(b+i+1)`.  Using `t<=W/q`, equations
(3.4) and (3.8) give

\[
 \sum_{1\le|h|\le R}(d_ht-W_h)
 \le O\!\left(W{R+R^3\over b}\right)=o(W).          \tag{3.9}
\]

Now sum (3.7) and use (2.6).  Hence a successful selector must make the
same `Theta(W/b^2)` tours almost disjoint not only internally at the middle
rank, but simultaneously across every rank in an arbitrarily growing
`o(b^{1/3})` central subband.  At larger offsets there is enough scalar
surplus for repetitions, but their union must still satisfy (2.6).

## 4. Exact fractional feasibility

The obstruction is integral, not fractional.  Let `mathfrak T_b` be the
parameter-labelled orbit of completed tours.  Its size and the degree of
an internal middle target are

\[
 L={ (2b)!\over b},\qquad
 D_{\rm int}={Lq\over W}=(b-1)(b!)^2.                \tag{4.1}
\]

Give every labelled tour weight `1/D_int`.  Every internal middle target
then has load exactly one, and the total tour weight is

\[
 {L\over D_{\rm int}}={W\over q}.                    \tag{4.2}
\]

By coordinate transitivity, a rank-`b+h` target has weighted load

\[
 \lambda_h={W\over q}{d_h\over W_h}.                 \tag{4.3}
\]

For `h>=0`,

\[
 \lambda_h={b\over b-1}{W\over W_h}
 \ge {b\over b-1}>1.                                \tag{4.4}
\]

For `h=-j<0`, cancellation in the product formula gives

\[
 {W_{-j}\over W}
 =\prod_{i=0}^{j-1}{b-i\over b+i+1}
 \le {b-j+1\over b+1},                              \tag{4.5}
\]

and therefore

\[
 \lambda_{-j}
 ={b-j+1\over b-1}{W\over W_{-j}}
 \ge {b+1\over b-1}>1.                              \tag{4.6}
\]

Equivalently, the linear system

\[
 \sum_{T:C\in K(T)}x_T\le1
 \quad(C\in{\Omega\choose b}),                     \tag{4.7}
\]

\[
 \sum_{T:A\in S_h(T)}x_T\ge1
 \quad(0<|h|\le H,\ A\in{\Omega\choose b+h})      \tag{4.8}
\]

has the explicit solution `x_T=1/D_int`.  It uses the exact optimum
middle mass `W/q` and fractionally covers every off-middle band target.
The minimum excess load near the middle is only `Theta(1/b)`, so a coarse
rounding theorem cannot preserve (4.8).

### 4.1 What incidence averaging and greedy covering actually give

The same calculation gives a deterministic cover, but only with a
logarithmic coefficient loss.  Let

\[
 Z(\mathcal A)=\sum_{0<|h|\le H}
 \left(W_h-\left|\bigcup_{T\in\mathcal A}S_h(T)\right|\right).       \tag{4.9}
\]

For arbitrary current uncovered sets, the average over a uniformly
labelled next tour of the number of newly covered targets is

\[
 \sum_{0<|h|\le H}{d_h\over W_h}h_h
 \ge {q\over W}Z,                                    \tag{4.10}
\]

where the inequality is exactly (4.4)--(4.6).  Hence some next tour gives

\[
 Z_{m+1}\le\left(1-{q\over W}\right)Z_m.             \tag{4.11}
\]

Starting with `Z_0<=2HW`, ordinary greedy averaging therefore proves

\[
 Z_m\le2HW\exp(-mq/W).                               \tag{4.12}
\]

To make this bound `o(W)` requires

\[
 {mq\over W}-\log H\longrightarrow+\infty.          \tag{4.13}
\]

Its serialized base length is then
`b^2m >= (1-o(1))W log H`, not `W+o(W)`.  Moreover, (4.11) does not
preserve internal disjointness.  Thus the standard deterministic
set-cover/conditional-expectation argument is valid but quantitatively
incapable of proving coefficient one; it cannot replace the correlated
near-partition required by (2.6).

## 5. Independent selection fails throughout a growing central band

Take

\[
 t=\left\lfloor {W\over q}\right\rfloor             \tag{5.1}
\]

independent uniformly relabelled completed tours, without conditioning on
internal disjointness.  A fixed rank-`b+h` target belongs to one tour with
probability

\[
 p_h={d_h\over W_h}.                                  \tag{5.2}
\]

If `R=o(sqrt b)`, then uniformly for `1<=|h|<=R`,

\[
 tp_h=1+o(1),\qquad p_h=o(1),\qquad W_h=(1-o(1))W.    \tag{5.3}
\]

Thus

\[
 \mathbb Eh_h=W_h(1-p_h)^t=(e^{-1}+o(1))W,           \tag{5.4}
\]

and, for

\[
 Z_R=\sum_{1\le|h|\le R}h_h,
\]

\[
 \boxed{\mathbb EZ_R=(2e^{-1}+o(1))RW.}              \tag{5.5}
\]

This aggregate failure is concentrated.  Replacing one sampled tour
changes `Z_R` by at most

\[
 \sum_{1\le|h|\le R}d_h\le2Rb^2.                    \tag{5.6}
\]

Efron--Stein therefore gives

\[
 \operatorname {Var}Z_R=O(tR^2b^4)=O(WR^2b^2)
 =o(R^2W^2).                                         \tag{5.7}
\]

Consequently

\[
 Z_R=(2e^{-1}+o(1))RW                                \tag{5.8}
\]

with high probability.  In particular, even two nearest off-middle ranks
leave `Theta(W)` holes, while any `R->infinity` makes the aggregate deficit
much larger than `W`.  Conditioning on internal disjointness can radically
change this law, so (5.8) is an obstruction to independent rounding, not a
no-go theorem for the desired correlated selector.

It also rules out a small alteration of the independent sample.  Replacing
or deleting one tour changes the two-rank union at `h=±1` by at most
`2b^2`.  Hence altering `o(t)=o(W/b^2)` sampled tours changes its aggregate
hole count by only `o(W)`, whereas (5.8) with `R=1` leaves
`(2/e+o(1))W` holes.  Any successful alteration must therefore reorganize
`Omega(t)` tours; it cannot be a local cleanup of an independent sample.

## 6. Low-order pseudorandomness does not imply tour availability

There is a robust hereditary obstruction stronger than the coordinate-star
example.  Let `mathcal V=binom(Omega,b)`.  For the live `H`, there is a
two-colouring

\[
 \mathcal V=\mathcal R_0\mathbin{\dot\cup}\mathcal R_1             \tag{6.1}
\]

such that neither colour contains the internal support `K(T)` of a
completed coherent tour, while both colours have asymptotically random
coordinate-cylinder and global Johnson-pair statistics.

More precisely, for either colour `c`, uniformly over every
`J subseteq Omega` with `|J|<=H`,

\[
 |\{A\in\mathcal R_c:J\subseteq A\}|
 =\left({1\over2}+o(1)\right){2b-|J|\choose b-|J|},  \tag{6.2}
\]

and, for every `1<=d<=b`,

\[
 |\{(A,B)\in\mathcal R_c^2:d_J(A,B)=d\}|
 =\left({1\over4}+o(1)\right)W{b\choose d}^2.       \tag{6.3}
\]

To prove this, colour the `W` middle targets independently and fairly.
There are at most `(2b)!/b` parameter-labelled tours.  Since every internal
support has `q=b(b-1)` distinct targets, the probability that some support
is monochromatic is at most

\[
 { (2b)!\over b}\,2^{1-q}
 =\exp\{-\Omega(b^2)\}.                              \tag{6.4}
\]

For fixed `J`, the left side of (6.2) is binomial with population
`binom(2b-|J|,b-|J|)`.  Its minimum over `|J|<=H` is
`exp(Omega(b))`, while the number of such `J` is
`exp(o(b))`.  Chernoff's bound and a union bound therefore prove (6.2),
even with relative error `b^{-10}`.

For (6.3), the expectation is one quarter of the displayed ambient ordered
pair count.  Changing the colour of one target changes the distance-`d`
count by at most `2 binom(b,d)^2`.  Bounded differences gives failure
probability `exp(-Omega(b^{-20}W))` for relative error `b^{-10}`, uniformly
in `d`; a union bound over the `b` distances completes the proof.  The
positive-probability intersection of these events and (6.4) gives (6.1)--
(6.3).

Thus density, all coordinate marginals through the compiler depth, and the
global pair-distance data can all look random while the induced tour
hypergraph has degree zero.  This does not rule out a theorem exploiting
the exact algebraic coset structure or the entire higher-overlap hierarchy.
It does rule out deriving hereditary availability merely from the existing
low-order balance and pair-codegree identities.

## 7. Exact surviving theorem

The completed-tour route is now reduced to the following integral
statement.

> **Completed coherent-tour selector.**  Choose a family `mathcal T` of
> completed tours whose internal middle supports are pairwise disjoint and
> which satisfies (2.6).

The all-pairing orbit proves exact regular fractional feasibility for this
statement.  The balanced coset and one-factorization banks supply large
locally disjoint batches and exact low-order balance.  Neither input rounds
the fractional solution: the tour rank grows as `Theta(b^2)`, the maximum
normalized middle pair-codegree is `Theta(1/b)`, independent selection has
the Poisson obstruction (5.8), and low-order hereditary criteria fail by
Section 6.

A positive proof must therefore correlate the near-perfect internal
matching with simultaneous near-injectivity at the nearby ranks and
coverage at the remaining offsets.  A matching-correlated regeneration,
an absorber/switching theorem for the completed-tour orbit, or an explicit
resolution with those common rank supports would suffice.  No such theorem
is proved here.
