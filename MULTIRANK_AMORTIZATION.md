# Simultaneous multirank amortization

## 1. Verdict

The amortized subcube-density theorem can be coupled across all ranks through
one entry-support zeta transform and through the physical window rows.  The
result is an exact necessary ILP relaxation and a new local incidence
inequality.  Neither makes a proposed value `n=B(k)` impossible for
`1<=k<20`.

The calculation also identifies why simply stacking the scalar moment cuts
cannot close the problem:

* after simultaneous containment is imposed, almost every nominal
  long-window credit is actually zero;
* from `k=5` through `k=200`, the only live credit ranks are the upper central
  rank `ceil(k/2)` and the full rank `k`;
* the permutation-symmetric fractional relaxation is feasible at every
  `B(k)`, `1<=k<20`, and at the larger exact checkpoints
  `20,25,50,100,200`;
* the genuinely local rank-to-rank incidence bounds are no stronger, through
  `k=19`, than the already proved nested cap-and-run bounds.

There is one useful finite rigidity checkpoint.  At `k=6,n=21`, combining
the multirank moment with exact short-band saturation recovers the exact
literal-rank profile and forces all twenty adjacent-pair ORs to be the twenty
three-sets.

## 2. Common zeta transform

Let `A=(A_1,...,A_n)` be a zero-free universal word on `[k]`, and put

\[
 x_S=|\{i:A_i=S\}|\qquad(\varnothing\ne S\subseteq[k]).
\]

For every `R subseteq [k]`, define

\[
 p_R=|\{i:A_i\subseteq R\}|.
\]

All support numbers at all ranks are the same Boolean zeta transform:

\[
 \boxed{p_R=\sum_{\varnothing\ne S\subseteq R}x_S.}       \tag{2.1}
\]

Thus they are not independent variables.  Equivalently their Boolean
Möbius inverse is the common nonnegative integral vector `x_S`.

For a rank `r` with

\[
 M_r=\binom kr\le n-1,
 \quad d_r=n-M_r,
 \quad \ell_r=d_r+1,
\]

put

\[
 c_r=\left\lceil\frac{2(2^r-1)}{\ell_r}\right\rceil.
\]

For every `r`-set `R`, let `q_R^(r)` count length-`ell_r` windows whose OR
is exactly `R`.  The amortized theorem says

\[
 p_R+q_R^{(r)}\ge c_r.                                  \tag{2.2}
\]

## 3. Simultaneous credit-row theorem

For a target rank `s`, define its best simultaneous physical cap

\[
 C_s(n)=
 \min_{\rho:\binom k\rho\le n}
 \left(n-\binom k\rho+\binom s\rho\right),              \tag{3.1}
\]

where the last binomial is zero for `rho>s`.  The containment-multiplicity
theorem gives

\[
 |J|\le C_{|U(J)|}(n)                                   \tag{3.2}
\]

for every physical interval `J`.

Call rank `r` **live** if `ell_r<=C_r(n)` and **dead** otherwise.  If it is
dead, no length-`ell_r` window can have rank `r`, and hence

\[
 q_R^{(r)}=0,
 \qquad p_R\ge c_r                                      \tag{3.3}
\]

pointwise for every `r`-set `R`.

Ranks with the same binomial coefficient have the same physical window row.
An interval in that row has only one OR value.  Consequently, for every
integer `M`,

\[
 \sum_{r:\binom kr=M}\ \sum_{R\in\binom{[k]}r}q_R^{(r)}
 \le M.                                                  \tag{3.4}
\]

Eliminating the credit variables gives the joint deficiency budget

\[
 \boxed{
 \sum_{r:\binom kr=M}\ \sum_{R\in\binom{[k]}r}
       (c_r-p_R)_+\le M,}                               \tag{3.5}
\]

with the stronger pointwise constraints (3.3) on dead ranks.  Equations
(2.1), (3.3), and (3.5) are the simultaneous multirank form of the theorem.

For odd `k=2m+1`, the two central ranks have the same row.  Every window in
that row has rank at least `m+1`, so the lower central credit dies:

\[
 p_R\ge c_m\qquad(R\in\binom{[k]}m).                    \tag{3.6}
\]

At `k=11,n=465`, this recovers the pointwise five-set bound `p_R>=16`, while
the rank-six family retains the joint deficiency budget

\[
 \sum_{U\in\binom{[11]}6}(32-p_U)_+\le462.
\]

## 4. A genuinely local zeta/window coupling

The common zeta transform also couples a rank-`r` credit family inside every
larger coordinate subcube.

Fix an `s`-set `T`, `s>=r`, and let

\[
 W_{\ell_r}(T)=
 |\{J:|J|=\ell_r,\ U(J)\subseteq T\}|.
\]

Summing (2.2) over the `r`-subsets of `T` gives the exact incidence bound

\[
 \boxed{
 \binom sr c_r
 \le
 \sum_{i:A_i\subseteq T}
       \binom{s-|A_i|}{r-|A_i|}
 +W_{\ell_r}(T).}                                      \tag{4.1}
\]

Indeed, an entry `A_i subseteq T` is counted by exactly
`C(s-|A_i|,r-|A_i|)` of the support sums.  Every credited window has one
rank-`r` OR contained in `T`, so the sum of the `q` terms is at most
`W_{ell_r}(T)`.  If rank `r` is dead, the last term can be deleted.

If `p_T=|{i:A_i subseteq T}|`, merging its support runs gives

\[
 W_{\ell_r}(T)\le(p_T-\ell_r+1)_+,
\]

and nonempty entries give

\[
 \binom{s-|A_i|}{r-|A_i|}\le\binom{s-1}{r-1}.
\]

Therefore

\[
 \boxed{
 \binom sr c_r
 \le \binom{s-1}{r-1}p_T+(p_T-\ell_r+1)_+,}            \tag{4.2}
\]

again omitting the final term for a dead rank.  This is a true multirank
consequence, rather than an independent scalar average.

The exact checker evaluates the least `p_T` allowed by (4.2) for every
`r<=s<=k`.  For every `k<20`, that lower bound is at most the existing nested
cap-and-run bound.  Thus (4.1) is structurally useful, but its present
one-number projection does not improve the established local-density table.

## 5. Necessary ILP and its symmetric LP collapse

A finite necessary ILP relaxation at a proposed length `n` has variables

```text
x_S in Z_+                    (nonempty S subseteq [k])
q_R^(r) in Z_+                (active r and |R|=r)
```

and constraints

```text
sum_S x_S = n,
p_R = sum_(S subseteq R) x_S,
p_R + q_R^(r) >= c_r,
sum_(r:C(k,r)=M) sum_R q_R^(r) <= M,
q_R^(r)=0 when ell_r>C_r(n).
```

One may safely add all rank-filtration constraints.  In particular, with

\[
 \beta_t(k)=\max_{u\le t}\left(\binom ku+\tau(k,u)\right),
\]

they include

\[
 \sum_{|S|\le t}x_S\ge\beta_t(k).                       \tag{5.1}
\]

At an exact strict record `n=beta_r(k)>beta_(r-1)(k)`, Rank-Filtration
Stability forbids entries above rank `r`, forbids duplicate excess among
literal rank-`r` entries, and makes the lower-rank entries one component.  It
does **not** forbid distinct rank-`r` boundary literals.  The component and
boundary-order conditions are not captured by this multiset ILP.

A further coarse but valid window-row constraint is

\[
 \ell_r\sum_S|S|x_S\ge r\binom kr,                     \tag{5.3}
\]

because all `M_r` length-`ell_r` windows have OR-rank at least `r`, while an
entry is counted in at most `ell_r` such windows.

The continuous relaxation is permutation invariant.  Averaging any feasible
solution over `S_k` gives variables depending only on `|S|`.  If
`x_s=sum_{|S|=s}x_S`, then every rank-`r` support becomes

\[
 \bar p_r
 =\sum_{s\le r}x_s\frac{\binom rs}{\binom ks}
 =\frac1{\binom kr}\sum_{s\le r}
      x_s\binom{k-s}{r-s}.                              \tag{5.4}
\]

Thus the symmetric LP is an exact rational `k`-variable test.  A dead row
requires `bar p_r>=c_r`; a live singleton row requires
`bar p_r>=c_r-1`.  For a particularly simple feasible certificate, the
checker uses the highest-rank profile satisfying all cumulative cuts and
then voluntarily moves its first-record rank mass down by one rank.  This is
stronger than filtration stability requires; it produces the allowed
zero-boundary special case, preserves all cumulative cuts, and can only
increase every zeta moment.

## 6. Exact computation through `k=19`

`scratch/check_multirank_amortization.py` uses only integer and rational
arithmetic.  `D` below means dead and `L` live.

| `k` | `B(k)` | upper-central rank | `d` | upper `c` | odd lower `c` | symmetric LP |
|---:|---:|---:|---:|---:|---:|:---:|
| 1 | 1 | 1 | 0 | - | - | pass |
| 2 | 2 | 1 | 0 | - | - | pass |
| 3 | 4 | 2 | 1 | 3 L | 1 D | pass |
| 4 | 7 | 2 | 1 | 3 L | - | pass |
| 5 | 12 | 3 | 2 | 5 L | 2 D | pass |
| 6 | 21 | 3 | 1 | 7 L | - | pass |
| 7 | 37 | 4 | 2 | 10 L | 5 D | pass |
| 8 | 72 | 4 | 2 | 10 L | - | pass |
| 9 | 128 | 5 | 2 | 21 L | 10 D | pass |
| 10 | 254 | 5 | 2 | 21 L | - | pass |
| 11 | 465 | 6 | 3 | 32 L | 16 D | pass |
| 12 | 926 | 6 | 2 | 42 L | - | pass |
| 13 | 1719 | 7 | 3 | 64 L | 32 D | pass |
| 14 | 3434 | 7 | 2 | 85 L | - | pass |
| 15 | 6438 | 8 | 3 | 128 L | 64 D | pass |
| 16 | 12873 | 8 | 3 | 128 L | - | pass |
| 17 | 24313 | 9 | 3 | 256 L | 128 D | pass |
| 18 | 48623 | 9 | 3 | 256 L | - | pass |
| 19 | 92381 | 10 | 3 | 512 L | 256 D | pass |

The complete output also lists the exact integer rank profile used for each
fractional certificate and every nontrivial credit row.  It checks:

1. all cumulative rank-filtration cuts;
2. compatibility with filtration stability through the voluntarily stronger
   zero-boundary special case;
3. all live deficiency and dead pointwise support moments;
4. all coarse row-rank inequalities (5.3);
5. the exact live-rank classification for every `5<=k<=200`;
6. the incidence bound (4.2) against the nested cap-and-run theorem for every
   `k<20`.

No proposed `B(k)` is rejected.

## 7. The exact `k=6` structural branch

Before making the checker's optional downward mass move, the profile that
minimizes every decreasing support moment under rank truncation is

\[
 (n_1,n_2,n_3)=(6,10,5).
\]

At `k=6,n=21,r=3`, the amortized moment is

\[
 10n_1+4n_2+n_3\ge120,                                 \tag{7.1}
\]

whereas that raw profile gives only `105`.  This is the only failure of the
raw extremal profile for `k<20`.

Here the rank-count residual is zero.  The independent boundary-mass bound
`d_r z<=sigma_r` therefore gives `z=0`: unlike the general filtration
theorem, this special arithmetic-tight case really has no literal rank-three
entry.  Every singleton physical cell is then the unique selected witness of
one of the `6+15=21` masks of ranks one and two.  Hence

\[
 (n_1,n_2,n_3)=(6,15,0).
\]

Equation (7.1) is tight.  Equality rigidity in the amortized theorem then
forces every one of the twenty length-two windows to have rank three.  Since
there are exactly twenty three-sets, these windows enumerate the complete
third layer; moreover every three-set has

\[
 p_R=6,\qquad q_R=1.
\]

The checker verifies these statements directly on the certified optimal
word

```text
1,34,16,3,4,33,40,10,18,6,36,8,5,17,32,20,12,2,9,24,48.
```

This is a real structural equality branch, although it does not give a new
value because `nu(6)=21` was already known.

## 8. Asymptotic interpretation

At the conjectured length

\[
 B(k)=W(k)+\sqrt{\pi k/8}+O(1),
\]

the only exponentially significant live credit is the upper-central one.
For `k=2m+1`, its lower symmetric partner is dead, so

\[
 p_R\ge
 \left(\frac4{\sqrt\pi}+o(1)\right)
 \frac{2^m}{\sqrt m}
 = (2\sqrt2+o(1))W(m)                                  \tag{8.1}
\]

for every `m`-set `R`.  The upper-central threshold is twice this:

\[
 c_{m+1}=
 \left(\frac8{\sqrt\pi}+o(1)\right)
 \frac{2^m}{\sqrt m}
 = (4\sqrt2+o(1))W(m).                                 \tag{8.2}
\]

These are strong local support requirements.  Nevertheless their averaged
zeta constraints remain feasible with substantial slack in the symmetric
LP.  Apart from the equal odd-dimensional central partner, the other
near-central ranks acquire enormous `d_r=n-C(k,r)` and lose meaningful
long-window credit; ranks near the full set have only polynomial `c_r`
against support sizes of order `n`.

Therefore the multirank amortization theorem sharpens the structural picture
but does not change the asymptotic lower constant.  A decisive next step must
retain information discarded by the permutation average: correlations of
the deficiency sets

\[
 \{R:p_R<c_r\}
\]

under Boolean inclusion, together with the ordered component and pin
constraints.  Independent scalar moments, even imposed at every rank, have
now been exhausted at this relaxation level.
