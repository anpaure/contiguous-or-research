# Audit of the capacity-respecting wreath-packing proposal

## Verdict

The capacity-deficit transfer is valid:

* if `s` cyclic orders have pairwise distinct middle intervals;
* if their depth-`q` multiplicities satisfy `mu_q(S)<=b_q(S)`;
* if `sum_S b_q(S)=W` and `b_q(S)>=1`;

then, with `L=W-ns`, the capacity deficit at every fixed depth is exactly
`L`, and the number `M_q` of genuinely missing masks satisfies `M_q<=L`.

The stated Proposition 2 is false.  A candidate wreath containing the new
middle set `Y` can share a depth-`q` target with the old wreath **outside
`Y`**.  The proof counts only shared targets `S subset Y`.

There is a corrected local-conflict bound.  It has the same leading aggregate
asymptotic `2/m+O(m^-2)`, but this local estimate alone is not a known theorem
producing the required capacity-respecting near-factor.  Thus:

* the transfer from an assumed family `P` is valid;
* the supplied proof of the existence of `P` is incomplete;
* if such a family were constructed, it would genuinely evade the additive
  append obstruction by rebuilding one common middle backbone, not by
  appending an annular word.

Throughout,

\[
 n=2m+1,\qquad W=\binom nm,\qquad N_q=\binom n{m-q}.
\]

## 1. The capacity ledger is exact

Fix a depth `q`.  Every cyclic order contributes exactly `n` distinct cyclic
intervals of length `m-q`.  Hence a family of `s` orders has total occurrence
count

\[
 \sum_S\mu_q(S)=ns=W-L.
\tag{1}
\]

Assume

\[
 \mu_q(S)\le b_q(S),\qquad
 b_q(S)\in\{\lfloor W/N_q\rfloor,\lceil W/N_q\rceil\},
 \qquad \sum_Sb_q(S)=W.
\tag{2}
\]

Then every summand below is nonnegative and

\[
 \boxed{\sum_S(b_q(S)-\mu_q(S))=L.}
\tag{3}
\]

Since `N_q<=W`, every capacity satisfies `b_q(S)>=1`.  Therefore every
missing target contributes at least one unit to (3), and

\[
 \boxed{M_q:=\#\{S:\mu_q(S)=0\}\le L.}
\tag{4}
\]

This conclusion is per depth.  Its summed consequence is

\[
 \sum_{q=1}^hM_q\le hL,
\tag{5}
\]

not `sum_q M_q<=L`.  Complementation inside each cyclic order gives the same
missing count in the paired upper rank.  Thus erosion blocks plus literal
repairs cost at most `2hL` beyond their core/seam cost.  In particular, the
transfer needs `L=o(W/h)` (as well as the usual `h=o(n)` seam condition).

## 2. Which parts of Proposition 2 are valid

Fix an old cyclic order `e`, a middle set `Y` which is not a length-`m`
interval of `e`, and put `r=m-q`, where `q<m/2`.

The assertion

\[
 \#\{S\in\mathcal C_q(e):S\subseteq Y\}\le q
\tag{6}
\]

is valid.  In the cyclic binary indicator of `Y`, decompose the ones into
runs.  A length-`r` interval contained in `Y` lies in one of those runs.  If
there is one qualifying run, its length is at most `m-1` because `Y` is not
an old middle interval, so it contains at most

\[
 (m-1)-r+1=q
\]

length-`r` intervals.  If there are at least two qualifying runs, their total
contribution is no larger; explicitly it is at most
`m-2(r-1)=2q+2-m<=q` in the stated range.

Also valid is the conditional calculation for a fixed `S subset Y`:

\[
 \Pr(S\in\mathcal C_q(f)\mid Y\in f)
 =\frac{q+1}{\binom mq},
\tag{7}
\]

where `f` is uniform among cyclic orders containing `Y`.  Once `Y` is a
length-`m` block, it contains exactly `q+1` length-`r` subintervals, and the
stabilizer of `Y` is transitive on its `r`-subsets.

The invalid step is the inference from (6)--(7) to a bound on *all* shared
targets.  A common member of `C_q(e)` and `C_q(f)` need not be contained in
`Y`.

## 3. Exact counterexample

Take

\[
 n=7,\quad m=3,\quad q=1,
\]

let the old order be

\[
 e=(0,1,2,3,4,5,6),
\]

and let

\[
 Y=\{0,2,4\}.
\]

Then `Y` is not a length-three interval of `e` and contains no member of
`C_1(e)`.  Nevertheless

\[
 f=(0,1,3,5,6,2,4)
\]

contains `Y` as its wraparound length-three interval and shares the two
depth-one targets

\[
 \{0,1\},\qquad\{5,6\}
\]

with `e`; neither is contained in `Y`.

Exhausting all `7!` labelled permutations gives 1,008 permutations
conditioned to contain `Y`, of which 840 share at least one depth-one target
with `e`.  Hence the true fraction is

\[
 \frac{840}{1008}=\frac56,
\]

whereas the claimed bound is

\[
 \frac{q(q+1)}{\binom mq}=\frac23.
\]

The RunPod audit is `scratch/audit_wreath_prop2_small.py`.

## 4. A corrected local-conflict bound

The omitted targets can be included explicitly.

### Proposition (corrected conditional sharing bound)

Under the hypotheses above, if `f` is uniform among cyclic orders containing
`Y`, then

\[
\begin{aligned}
 &\Pr(\mathcal C_q(e)\cap\mathcal C_q(f)\ne\varnothing\mid Y\in f)\\
 &\quad\le
 \frac{q(q+1)}{\binom mq}
 +\frac{(q+1)(q+2)}{\binom{m+1}{q+1}}
 +\frac{2n}{(m+1)\binom m{q+1}}.
\end{aligned}
\tag{8}
\]

Consequently, uniformly for `h<=m/3`,

\[
 \sum_{q=1}^h
 \Pr(\mathcal C_q(e)\cap\mathcal C_q(f)\ne\varnothing\mid Y\in f)
 \le \frac2m+\frac{32}{m^2}+O(m^{-3}).
\tag{9}
\]

#### Proof

Put `Z=Y^c`.  Conditional on `Y` being an `m`-block of `f`, the complement
`Z` is the consecutive block of length `m+1`.  Fix an `r`-set `S` and put
`a=|S cap Y|`.  Counting position windows of length `r` in the two-block
cycle gives

\[
 \Pr(S\in\mathcal C_q(f)\mid Y\in f)
 =\frac{c_a}{\binom ma\binom{m+1}{r-a}},
\tag{10}
\]

where

\[
 c_r=q+1,\qquad c_0=q+2,\qquad c_a=2\ (1\le a\le r-1).
\tag{11}
\]

The first value counts windows wholly in the `Y` block, the second counts
windows wholly in the `Z` block, and an intermediate intersection size can
cross either of the two block boundaries.

Equation (6) bounds the number of old targets with `a=r` by `q`.  Similarly,
the number with `a=0`, namely the old length-`r` intervals contained in `Z`,
is at most `q+1`.  Indeed `Z` is not an old length-`m+1` interval (otherwise
its complement `Y` would be an old middle interval), and the same run count
applies with total size `m+1`.

For `1<=a<=r-1`, log-concavity of the two binomial sequences shows that

\[
 \binom ma\binom{m+1}{r-a}
 \ge
 \min\left\{
 m\binom{m+1}{q+2},
 (m+1)\binom m{q+1}
 \right\}
 =(m+1)\binom m{q+1}.
\tag{12}
\]

There are only `n` old targets in total.  Applying the union bound to (10),
using the three counts just obtained, proves (8).

For (9), the `q=1` contributions of the three terms in (8) are respectively

\[
 \frac2m,
 \qquad
 \frac{12}{m(m+1)}=\frac{12}{m^2}+O(m^{-3}),
\]

and

\[
 \frac{4(2m+1)}{(m+1)m(m-1)}
 =\frac8{m^2}+O(m^{-3}).
\]

The `q=2` contribution of the first term is
`12/[m(m-1)]=12/m^2+O(m^-3)`.  All remaining contributions sum to
`O(m^-3)`; this follows directly from successive binomial ratios uniformly
for `q<=m/3`.  Adding the four displayed leading contributions gives (9).
QED

## 5. What the corrected estimate does and does not prove

The correction preserves the proposed `2/m+O(m^-2)` *local* asymptotic.
It does not by itself construct a family of

\[
 s=\frac{W-L}{n},\qquad L=o(W/h),
\]

cyclic orders satisfying all middle-disjointness and multidepth capacity
constraints.  There are exponentially many selected orders and a growing
collection of capacity constraints.  A per-old-wreath local conflict
probability of order `1/m` cannot simply be union-bounded over the selected
family.

Nor does the corrected estimate fit any currently invoked generic matching
theorem at the needed precision.  Encoding all marked depths in one edge has
growing incidence size on the order of `nh`; a normalized pair-conflict
estimate `O(1/m)` does not yield the additive `L=o(W/h)` residual from
the available ABKV bound in that uniformity regime.  A specialized switching,
absorption, or capacity-respecting factor theorem is still required.

There is an additional structural reason that the pair estimate is not itself
the capacity theorem.  At depth `q`, collisions are legal up to the prescribed
load `b_q(S)`, which can grow to order `W/N_q`.  Treating every shared target
as a forbidden pair would force all depth-`q` occurrences to be distinct and
therefore

\[
 W-L\le N_q,
 \qquad L\ge W-N_q.
\]

At the proposed outer controlled depth, `N_h/W` is about the reciprocal of a
growing logarithmic factor, so this would force `L=(1-o(1))W`, the opposite of
`L=o(W/h)`.  The actual forbidden configurations are capacity-overflow
families of size `b_q(S)+1`, with nonuniform orders across the depths.  A valid
rounding theorem must control those higher-order saturation events while
retaining the unavoidable lower-order collisions.

If such a family `P` is supplied by another argument, however, equations
(1)--(5) make the erosion-block transfer rigorous.  This would materially
evade the no-append theorem in
`QUEUE_MULTISCALE_COMMON_BACKBONE_20260724.md`: the same `ns=W-L` middle
occurrences would own all controlled depths at once.  It is a one-shot common
backbone construction, not an `o(W)` annular appendage.  Hence there is no
contradiction with endpoint capacity; the current issue is existence of that
common backbone.
