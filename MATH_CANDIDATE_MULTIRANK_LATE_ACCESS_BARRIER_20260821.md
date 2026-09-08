# Multi-rank late access: the common-choice ledger and the bulk-coherence barrier

**Status (2026-08-21).**  Theorem 2.1, Corollary 2.2, Proposition 3.1,
Theorem 4.1, and Lemma 4.2 are deterministic and proved here.  Corollary
4.3 combines Lemma 4.2 with the stationary Poisson argument under its
explicit hypotheses.
No unproved mixing or local-uniformity assertion is used.  The conclusions
do **not** construct a DCC.  They identify the extra joint statistic that a
shared multi-rank rule must control and rule out high-probability success
for a typical stationary-plateau-then-late-repair architecture.

## 1. Tail-MTF notation

Let `n=2m+1` be sufficiently large, `W=binom(n,m)`, and

\[
 H=\lceil\sqrt{n\log n}\rceil,
 \qquad K=\{m-H,\ldots,m+1+H\}.
\]

At time `t`, write the recency order from most to least recent as
`(c_1,...,c_n)`.  Take an integer `0<=sigma<=n-1` and a floor
`f=n-sigma` satisfying
`f>max K` and put `d=sigma+1`.  The eligible pool is

\[
 E_t=\{c_f,\ldots,c_n\}.
\]

For `k in K`, let `P_{t,k-1}={c_1,...,c_{k-1}}`.  If eligible letter
`x` is chosen, the new rank-`k` window is

\[
 S_{t,k,x}=P_{t,k-1}\cup\{x\}.
\]

For fixed `(t,k)` the `d` sets `S_{t,k,x}`, `x in E_t`, are distinct,
and for fixed `(t,x)` they form a nested chain as `k` varies.  Let
`Z_{t,k}` be the rank-`k` sets still unseen immediately before time `t`,
and define

\[
 b_{t,k,x}=1_{\{S_{t,k,x}\in Z_{t,k}\}},\qquad
 c_{t,k}=\sum_{x\in E_t}b_{t,k,x},\qquad
 h_{t,k}=1_{\{c_{t,k}>0\}}.
\]

Thus `c_{t,k}` is the number of fresh members of the rank-`k` fan.
One letter `x_t in E_t` is chosen for **all** ranks.  A window is called
clean when its letters are all distinct.

## 2. Exact weighted common-choice ledger

Use the convention that `Z_{t,k}` is the unseen family immediately
before step `t`, and step `t` changes it to `Z_{t+1,k}`.  Fix a late
interval `I={t_0,...,T-1}`.  Give rank `k` a target weight
`w_k>=0` and an offer threshold `J_k>=1`.  For a set `S` unseen at time
`t_0`, let `a_I(S)` be the number of times in `I` at which `S` belongs
to its rank fan while it is still unseen.

Define the low-offer exceptional mass

\[
 E_I=\sum_{k\in K}w_k\,\#\{S\in Z_{t_0,k}:a_I(S)<J_k\}.
\]

### Theorem 2.1 (weighted common-choice snub inequality)

For every eligible schedule, with no probabilistic hypothesis,

\[
 \sum_{k\in K}w_k|Z_{T,k}|
 \le E_I+C_I,
 \tag{2.1}
\]

where

\[
 C_I=\sum_{t\in I}\sum_{x\ne x_t}\sum_{k\in K}
       {w_k\over J_k}\,b_{t,k,x}.
 \tag{2.2}
\]

**Proof.**  A final missed set in the exceptional class is charged to
`E_I`.  Any other final missed rank-`k` set has at least `J_k` late
offers.  It is unseen on every such offer and the offering letter is
never `x_t`, since the set is still missed at time `T`.  Charge
`w_k/J_k` to each of these distinct snubs.  Its total charge is at
least `w_k`.  Summing proves (2.1).  \(\square\)

The exact obstruction hidden by separate per-rank ledgers is visible
after decomposing `C_I`.  Put `v_k=w_k/J_k` and

\[
 A_{t,x}=\sum_{k\in K}v_k b_{t,k,x}.
\]

For an arbitrary common-choice schedule, define

\[
 C_I^{\rm cross}(x_\bullet)=\sum_{t\in I}\left(
   \sum_{k\in K}v_kh_{t,k}-A_{t,x_t}
 \right).                                                   \tag{2.3}
\]

Then, exactly,

\[
 C_I=C_I^{\rm in}+C_I^{\rm cross}(x_\bullet),              \tag{2.4}
\]

where

\[
 C_I^{\rm in}=\sum_{t\in I}\sum_{k\in K}v_k(c_{t,k}-1)_+,
 \tag{2.5}
\]

and a rule choosing `x_t` to maximize `A_{t,x}` minimizes the current
cross term, giving

\[
 C_I^{\rm cross}=\sum_{t\in I}\left(
   \sum_{k\in K}v_kh_{t,k}-\max_{x\in E_t}A_{t,x}
 \right).
 \tag{2.6}
\]

Indeed, rank by rank,

\[
 c_{t,k}-b_{t,k,x_t}
 =(c_{t,k}-1)_+ + h_{t,k}-b_{t,k,x_t}.
\]

The first term is ordinary within-rank fan crowding.  The second is
**column discordance**: ranks having some fresh eligible completion but
not sharing one common fresh letter with the selected ranks.

### Corollary 2.2 (correct simultaneous late-access criterion)

Take `w_k=1`.  A single schedule has total final band defect `o(W)` if
for some thresholds `J_k` its late interval and actual common choices
satisfy

\[
 E_I=o(W),\qquad C_I^{\rm in}=o(W),\qquad
 C_I^{\rm cross}(x_\bullet)=o(W).                          \tag{2.7}
\]

This is an actual multi-rank version of LAL'.  Separate per-rank offer
and crowd estimates, even when strong enough to aggregate over the
growing band, address only the first two assertions in (2.7); they do
not establish the third.

## 3. Nested fans do not themselves control column discordance

### Proposition 3.1 (sharp abstract one-state matrix barrier)

Fix any tail-MTF recency permutation and its eligible fan geometry, and
let `R<=min(|K|,d)`.  There is a choice of
`R` ranks and an abstract seen/unseen assignment on the distinct targets
in the current fans for which

\[
 c_{t,k}=1\quad\hbox{at every chosen rank},\qquad
 C_{t}^{\rm in}=0,
\]

but every common letter choice serves at most one of those ranks.  Thus
the minimum unweighted one-step column discordance is `R-1`.

**Proof.**  Choose distinct ranks `k_1,...,k_R` and distinct eligible
letters `x_1,...,x_R`.  At rank `k_i`, declare
`S_{t,k_i,x_i}` unseen and the other `d-1` fan members seen.  These
assignments are consistent on the distinct fan targets: within a rank
the fan members are distinct, and sets at different ranks have different
cardinalities.  Declare all fan members at unselected ranks seen.  Hence
each active row has exactly one fresh entry, while the fresh entries
occupy distinct columns.  Any selected column contains exactly one of
them, so (2.6) has one-step value `R-1`.  \(\square\)

This proposition does not assert that such a status is dynamically
reachable from empty coverage.  It proves the precise logical barrier:
any argument using only nestedness and separate per-rank fan counts leaves
`C_I^{cross}` uncontrolled.  Closing this particular ledger route needs
a dynamical **cross-rank alignment** statement.

## 4. Near-`W` DCCs require bulk central-chain coherence

The next obstruction is global and applies to every singleton word, not
only to tail-MTF rules.

Let `r=r(n)` satisfy

\[
 r\longrightarrow\infty,\qquad r=o(\sqrt n),
\]

and set

\[
 K_r=\{m-r,\ldots,m+1+r\},\qquad R=|K_r|=2r+2.
\]

Uniformly for `k in K_r`,

\[
 {\binom nk\over W}=1-O(r^2/n).                            \tag{4.1}
\]

For example, on the lower side this follows by writing

\[
 {\binom n{m-j}\over\binom nm}
 =\prod_{s=0}^{j-1}{m-s\over m+2+s}
 =\exp\!\bigl(-O(j^2/n+j/n)\bigr),
\]

and the upper side follows by symmetry.

Consider a cyclic singleton word of length
`T=(1+epsilon_n)W`, where `epsilon_n>-1` may have either sign, whose
`k`-windows are clean for `k in K_r`.
Chronologically order its `T` cyclic windows at each rank.  Let `D_r`
be the total number of missed targets over `K_r`, with
`D_k=binom(n,k)` minus the number of distinct clean cyclic `k`-windows
and `D_r=sum_k D_k`.  (Every rank-`k` singleton interval contains `k`
consecutive positions; cleanliness makes that subwindow its target, so
this is also the interval-realization defect.)  Let `Q_r` be the
number of step-rank pairs `(t,k)` for which the window at time `t` has
already appeared earlier in that chronological order.

### Theorem 4.1 (bulk-coherence identity and necessity)

Exactly,

\[
 Q_r=RT-\sum_{k\in K_r}\binom nk+D_r.                      \tag{4.2}
\]

Consequently, if `epsilon_n=o(1)` and `D_r=o(W)`, then

\[
 {Q_r\over RT}
 =O(|\epsilon_n|+r^2/n)+o(1/R)=o(1).                       \tag{4.3}
\]

Equivalently, for all but `o(T)` times, the selected nested prefix chain
is fresh at `1-o(1)` of the ranks in every such growing central subband.

**Proof.**  At rank `k`, the number of repeated observations is exactly
`T` minus the number of distinct observed sets, namely
`T-(binom(n,k)-D_k)`.  Sum over `k` to get (4.2), then use (4.1).  The
last formulation follows from Markov's inequality applied to the number
of repeated ranks at a time.  \(\square\)

Thus coefficient one is not an endgame-only coverage property.  It
forces almost every selected suffix/prefix chain, throughout the bulk of
the run, to be simultaneously new on almost every rank in any growing
`o(sqrt(n))` central subband.  This repeat-density conclusion is only a
coarse necessary diagnostic.  The exact target equivalent to
`D_r=o(W)` is the stronger excess-repeat estimate

\[
 Q_r-\left(RT-\sum_{k\in K_r}\binom nk\right)=o(W).         \tag{4.4}
\]

### Lemma 4.2 (late repair capacity)

At any time `t_0`, let

\[
 D_r(t_0)=\sum_{k\in K_r}|Z_{t_0,k}|.
\]

After `U` further singleton steps,

\[
 D_r(t_0+U)\ge D_r(t_0)-RU.                                \tag{4.5}
\]

**Proof.**  One step realizes only one set at each of the `R` ranks, so
it can remove at most `R` members from the summed deficit.  \(\square\)

### Corollary 4.3 (a Poisson plateau cannot be repaired late)

If at the start of a purported late phase

\[
 D_r(t_0)\ge cRW
\]

for a fixed `c>0`, while the phase has `U=o(W)` steps, then its final
defect is at least `(c-o(1))RW`, in particular not `o(W)`.

For the probabilistic specialization, assume `sigma>=C log n`,
`sigma=o(n)`, `d<=m<=f`, choose uniformly from the eligible pool, and
start the bottom-`d`-to-top chain in its uniform stationary law.  The
factorial-moment proof of the stationary plateau, with the same argument
for any fixed `mu>0`, says that after `mu W+o(W)` steps the rank-`m`
defect is `(e^{-mu}+o(1))W` in probability.  Hence, with probability
`1-o(1)`, an `o(W)` adaptive late phase cannot turn a typical such prefix
into coefficient-one coverage.

More quantitatively, for a pure stationary-random prefix of length `mu W`
followed by an arbitrary repair phase inside total length
`(1+epsilon)W` to succeed with probability bounded away from zero, it is
necessary that the single-rank capacity inequality

\[
 e^{-\mu}\le 1+\epsilon-\mu+o(1).                          \tag{4.6}
\]

For `epsilon=o(1)`, (4.6) fails by a fixed gap for every fixed
`mu in (0,1]`, since `e^{-mu}>1-mu` for `mu>0`.  Thus the success
probability of this typical two-phase randomized architecture tends to
zero, even if the continuation adapts to the realized prefix.  This does
not exclude exceptional prefixes of vanishing probability or an
existence argument selecting one of them.  Uniform randomness may also
be interleaved with feedback from the beginning; this corollary does not
rule that out.

## 5. Research consequence

The exact ledger gives the following sufficient target for this route:

1. control low-offer exceptions and within-rank crowd as in LAL';
2. prove that the same chosen eligible letter aligns fresh candidates
   across ranks, making the weighted column-discordance sum in (2.6)
   `o(W)`; and
3. obtain this coherence in the bulk, not only during an `o(W)` terminal
   interval.

Theorem 4.1 supplies a necessary diagnostic, but its theorem-level DCC
target is not merely `o(1)` repeat density.  It is the `o(W)`
**excess-repeat** estimate (4.4) in every growing `o(sqrt(n))` central
subband.  Per-rank Poissonization and late fan access alone cannot imply
that estimate.
