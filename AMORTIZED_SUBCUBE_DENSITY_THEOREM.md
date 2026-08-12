# Amortized subcube-density inequalities for contiguous-OR words

## 1. Statement

Let `A=(A_1,...,A_n)` be a zero-free universal word on `[k]`.  Fix `r`, put

\[
 M=\binom kr,\qquad d=n-M\ge1,
\]

and choose one witness for every rank-`r` target.  For
`R in binom([k],r)`, define

\[
 P_R=\{i:A_i\subseteq R\},\quad p_R=|P_R|,
\]

and let `q_R` be the number of physical intervals of length `d+1` whose OR
is exactly `R`.  Finally put

\[
 c_{r,d}=\left\lceil\frac{2(2^r-1)}{d+1}\right\rceil.
\]

Then

\[
 p_R+q_R\ge c_{r,d}\quad\hbox{for every }R,
\]

\[
 \sum_Rq_R\le M,
 \qquad
 \sum_R(c_{r,d}-p_R)_+\le M,
\]

and hence

\[
 \boxed{
 \sum_{i=1}^n\binom{k-|A_i|}{r-|A_i|}
 \ge(c_{r,d}-1)\binom kr.}
\]

For every integer `j>=1`, the stronger distributional consequence is

\[
 |\{R:p_R\le c_{r,d}-j\}|\le \frac Mj.
\]

## 2. Physical containment cap

Order the selected rank-`r` witnesses by their left endpoints.  In the usual
antichain normal form the `i`th witness lies in `[i,i+d]`.  If an interval
`J=[a,b]` has length `L>d`, it contains the selected witnesses indexed
`a,...,b-d`.  Their `L-d` distinct rank-`r` values are all subsets of
`U(J)`.  Therefore

\[
 |J|\le d+\binom{|U(J)|}{r}.
\]

In particular, intervals of OR-rank below `r` have length at most `d`, and
intervals of OR-rank exactly `r` have length at most `d+1`.

## 3. Local long-window credit

The positions in `P_R` form runs, each of length at most `d+1`.  A run has
length `d+1` exactly when the OR of the whole run is `R`; hence such runs are
counted by `q_R`.

For a run of length `ell`, let

\[
 f_d(\ell)=\sum_{j=1}^d(\ell-j+1)_+.
\]

For `1<=ell<=d+1`,

\[
 2f_d(\ell)\le(d+1)\ell+(d-1)\mathbf1_{\{\ell=d+1\}}.
\]

Every nonempty proper subset of `R` has a witness of length at most `d`
inside these runs.  If `q_R=0`, `R` itself must also have such a witness.
Thus, when `q_R=0`, summing the run inequality gives

\[
 (d+1)p_R\ge2(2^r-1).
\]

When `q_R>=1`, it gives

\[
 (d+1)p_R+(d-1)q_R\ge2(2^r-2).
\]

Adding `2q_R` and using `q_R>=1` proves
`p_R+q_R>=c_{r,d}` in both cases.

## 4. Global amortization

There are exactly `n-d=M` intervals of length `d+1`.  Every one has OR-rank
at least `r`.  A rank-`r` interval contributes to exactly one `q_R`; a
higher-rank interval contributes to none.  Consequently `sum_R q_R<=M`.
Since `(c-p_R)_+<=q_R`, the deficiency inequality follows.

Finally,

\[
 \sum_Rp_R
 =\sum_i|\{R:A_i\subseteq R,\ |R|=r\}|
 =\sum_i\binom{k-|A_i|}{r-|A_i|}.
\]

The deficiency inequality implies `sum_R p_R>=(c-1)M`, proving the moment
cut.

## 5. The `k=11,n=465,r=6` cut

Here `M=462`, `d=3`, and `c_{6,3}=32`.  Therefore

\[
 \sum_{U\in\binom{[11]}6}(32-p_U)_+\le462
\]

and

\[
 \boxed{
 252n_1+126n_2+56n_3+21n_4+6n_5+n_6\ge14322.}
\]

Together with the independently proved pointwise bound `p_U>=28`, if
`a_j=|{U:p_U=j}|`, then

\[
 4a_{28}+3a_{29}+2a_{30}+a_{31}\le462.
\]

This strictly strengthens the previous aggregate threshold `12936`, but is
still arithmetically feasible at length 465.  As a standalone local-density
comparator it is stronger; however, after all cumulative entry-rank
truncation inequalities `#{i:|A_i|<=s}>=b_s(11)` are imposed, those older
inequalities already force this particular weighted sum to be at least
`18866`.  The genuinely nonredundant information at `k=11` is therefore the
per-subcube lower-tail inequality, not the aggregate number `14322` alone.

## 6. Equality scope

If the moment inequality is an equality, then

\[
 \sum_Rq_R=M,qquad p_R+q_R=c_{r,d}\quad\hbox{for every }R.
\]

Hence every physical interval of length `d+1` has OR-rank exactly `r`.
This forces a fixed-rank derivative row, but **does not by itself prove that
the row's `M` values are distinct**: rank-`r` targets may also use shorter
witnesses.  Nor does the ceiling in `c_{r,d}` force every raw local quadratic
run inequality to be an equality.

There is a stronger special conclusion at `k=11,r=6,d=3`.  If the moment
cut is tight, then every six-set has `p_U+q_U=32`.  A `q_U=0` support would
need 63 distinct short intervals, while a `q_U>=2` support has at most 61
short intervals available for the 62 proper targets.  Since the global
average of `q_U` is one, necessarily

\[
 q_U=1,\qquad p_U=31
\]

for every six-set.  The only support-run inventory capable of providing 62
proper witnesses is one run of length four and nine runs of length three.
Consequently the 462 physical length-four windows enumerate all 462 six-sets
exactly once.  Thus the traditional fixed-delay central row is genuinely
forced on this **tight moment branch**, though not on every hypothetical
length-465 word.
