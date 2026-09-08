# Self-audit: pinned-ray rank-row transport and collar-debt collapse

**Date:** 2026-08-04  
**Method:** independent symbolic replay; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_PINNED_RAY_RANK_ROW_TRANSPORT_AND_COLLAR_DEBT_COLLAPSE_20260804.md`

## 0. Verdict

**GO at the stated rank-projection scope.**  The forced-ray rank/length
calculation, Ferrers transportation cuts, asymptotic low-rank estimate, and
mandatory-collar collapse are correct.  The theorem deliberately does not
lift the rank schedule to named physical apertures or one occurrence state.

## 1. Forced-ray arithmetic

The aligned theorem has `|J|=r-d-2`, `|P_j|=j`, and `|S_j|=d-j`.
Therefore

\[
 |X_j|=r-d-1+j,
 \qquad
 |Y_j|=r-j-1.
\]

The physical lengths are `j` and `d-j`, respectively.  In length row
`q`, the pair is `X_q,Y_(d-q)`, and both ranks equal

\[
                         r-d-1+q.
\]

The targets and addresses are distinct by the authenticated aligned-ray
theorem.  If `r>=2d`, then for `q<=d-1`,

\[
 r-d-1+q-2q=r-d-1-q\ge0.
\]

Thus neither pin contributes to `(2q-s)_+`.

## 2. Exact Ferrers cut family

After reserving the two pins, rows `q<d` have capacity `W-2` and row `d`
has capacity `W`.  A remaining rank `s>=2` may use rows

\[
                 1,\ldots,\min(d,\lfloor s/2\rfloor),
\]

while rank one may use only row one.  These are nested initial intervals.
For a capacitated Ferrers graph, the only Hall cuts are the initial row
segments.  For `t<d`, the items whose complete neighbourhood lies in the
first `t` rows are exactly those of ranks at most `2t+1`; for `t=d`, every
item is counted.  Hence the theorem lists the exact cut family, not merely
a sufficient subfamily.

## 3. Uniform low-tail estimate

Since `d=Theta(sqrt(k))`, `m=2d-1=o(k)` and, for all large `k`, `m<k/2`.
The binomial coefficients increase through `m`, so

\[
 \sum_{s=1}^{m}{k\choose s}
 \le m{k\choose m}
 \le(m+1)(ek/m)^m
 =\exp(O(\sqrt{k}\log k)).
\]

The central coefficient satisfies

\[
                         W\ge2^k/(k+1).
\]

The ratio of the first display to the second tends to zero exponentially.
Therefore the claimed eventual inequality

\[
                         \sum_{s=1}^{2d-1}{k\choose s}\le W-2d
\]

is valid.

For `1<=t<d`, demand in the first `t` rows is at most `W-2d`, and

\[
 W-2d\le t(W-2)
\]

because the difference is `(t-1)W+2(d-t)>=0`.  At `t=d`, deleting the
`2(d-1)` forced targets from total demand at most `dW` leaves exactly at
most the total residual row capacity `dW-2(d-1)`.  All cuts pass, so
integral max flow gives the asserted named-target-to-row-copy schedule.

## 4. Mandatory-collar left side

Every non-singleton scheduled by the flow obeys `s>=2q`; the forced rays
obey the same inequality.  Hence all their terms `(2q-s)_+` vanish.  The
only remaining case is `s=q=1`, whose term equals one.  Therefore

\[
 \sum_s(2q-s)_+n_{s,q}
 =n_1\mathbf1_{\{q=1\}}.
\]

In the exact run census, the `q=1` right side is

\[
 \sum_R(1-(L(R)-d-1))_+,
\]

which counts precisely runs with the minimum legal integer length `d+1`.
This exact reading uses the theorem's cyclic resident-factor scope; an
opened linear factor has separately priced clipped boundary runs.
The labelled singleton theorem requires the run label to equal the target
coordinate.  One such run for every residual singleton therefore supplies
the complete remaining demand.  For `q>1`, the left side is zero and the
right side is nonnegative.

## 5. Scope boundary

The flow assigns a named target to a **row copy**, not to a physical cell.
It does not prove the mandatory set containment

\[
                         K_{j,q}\subseteq S\subseteq E_{j,q},
\]

nor simultaneous interval-cover feasibility, distinct target values in one
fixed word, owner reconstruction, residence, upper completeness, or
regeneration.  The result removes the aggregate rank/run obstruction only.
It cannot be cited as a lower-deck construction or as an additive upper
bound.
