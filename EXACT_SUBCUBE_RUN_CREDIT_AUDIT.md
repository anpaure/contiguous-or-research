# Independent audit of the exact subcube run-credit envelope

## Verdict

**PASS.**  The exact capacity formula, the definition and use of
`gamma_(r,d)`, the two global credit budgets, the `k=11` coefficient rows
`7,5,3,1` and `6,4,2`, and the boundary-core right-hand sides `462` and
`461` are all mathematically valid.

The supplied checker correctly exhausts the advertised finite partition
range and reproduces the `k=11` table.  Its enumeration is corroborative;
the general closed formula follows from a separate convexity argument and
does not depend on the finite range tested by the script.

There were two presentation qualifications, neither affecting the theorem:

1. the equation label `(2.4)` was used twice in the note;
2. in the boundary-core branch, the relevant local credit function is
   formally the version requiring 62 proper subsets for every `q`, rather
   than the main definition which requires 63 targets when `q=0`.  On the
   only active support values `28,...,32`, both definitions give exactly
`7,5,3,1,0`, so every displayed boundary-core cut remains unchanged.

Both presentation points were repaired after the proof audit: equation labels
are now unique, and the boundary-core paragraph explicitly defines the
proper-subset function `eta_(r,d)`.

## 1. Run interpretation and target demand

For an `r`-set `R`, a run of

```text
P_R={i:A_i subseteq R}
```

has OR contained in `R`.  The containment theorem at rank `r` bounds its
length by `d+1`.  If its length is `d+1`, the rank-slack theorem says its OR
has rank at least `r`; containment in the `r`-set `R` then makes its OR
exactly `R`.  Conversely, a length-`d+1` window with OR `R` lies in a
`P_R`-run, and the same maximum-length bound makes it the whole run.  Thus
`q_R` really is both:

* the number of `P_R`-runs of length `d+1`; and
* the number of length-`d+1` physical windows with OR exactly `R`.

Every nonempty proper subset of `R` has rank below `r`, hence has a witness
of length at most `d`.  Exact OR contained in `R` forces that witness wholly
inside a `P_R`-run.  These `2^r-2` targets use distinct physical intervals.
If `q_R=0`, a witness for `R` cannot have length `d+1`, so it too is a
distinct short interval.  Therefore the capacity demand is exactly

```text
2^r-2 + 1_{q_R=0}.
```

This proves that the actual run partition is feasible for
`F_d(p_R,q_R)` and meets the defining demand.  Since `gamma_(r,d)(p)` is the
least nonnegative `q` meeting that demand, `q_R>=gamma_(r,d)(p_R)` follows.
No monotonicity assumption on `F_d(p,q)` in `q` is needed: the actual `q_R`
is simply an element of the feasible set and hence is no smaller than its
minimum.

## 2. General closed form for `F_d`

For `1<=ell<=d`,

\[
 f_d(\ell)=\frac{\ell(\ell+1)}2,
\]

while

\[
 f_d(d+1)=\frac{d(d+3)}2.
\]

After prescribing `q` parts of length `d+1`, the remaining mass is

\[
 s=p-q(d+1).
\]

The pair is infeasible exactly when `s<0`.  For the remaining parts, all
lengths lie in `1,...,d`, and the objective is the convex triangular function
`ell(ell+1)/2`.  If `1<=x<=y<d`, replacing the two parts `x,y` by
`x-1,y+1` (and deleting a zero part) changes the objective by

\[
 -(x)+(y+1)=y-x+1>0.
\]

Repeated transfers therefore leave as many length-`d` parts as possible and
one residual part.  Writing

\[
 s=ad+b,\qquad 0\le b<d,
\]

gives

\[
 \boxed{
 F_d(p,q)=q\frac{d(d+3)}2
          +a\frac{d(d+1)}2
          +\frac{b(b+1)}2.}
\]

This also covers `s=0`; the residual partition is then empty.  It proves the
formula for every positive integer `d`, not only the range checked
computationally.

The script `scratch/check_exact_subcube_run_credit.py` independently
enumerates every integer partition for

```text
1 <= d <= 6,  0 <= p < 45,
0 <= q <= floor(p/(d+1)),
```

and matches the closed form in every case.  It separately checks the `d=3`
specialization through `p=49`.

## 3. The two global budgets

There are exactly

\[
 n-(d+1)+1=n-d=M=\binom kr
\]

length-`d+1` windows.  Every one has rank at least `r`.  Rank-`r` windows
contribute once to exactly one `q_R`; higher-rank windows contribute zero.
Thus

\[
 \sum_Rq_R\le M,
\]

and `q_R>=gamma(p_R)` proves

\[
 \sum_R\gamma_{r,d}(p_R)\le M.
\]

For the residual budget, let

```text
z = #{R:q_R=0},
H = # length-(d+1) windows of rank >r,
D = sum_R(q_R-1)_+.
```

There are `M-H` rank-`r` long windows and exactly `M-z` rank-`r` values
represented at least once in that row.  Therefore

\[
 D=(M-H)-(M-z)=z-H\le z.                                \tag{3.1}
\]

Every one of the `z` omitted row values needs a distinct rank-`r` witness of
length at most `d`.  After selecting one short witness for each lower target,
such a physical interval is one of the

\[
 \sigma=dM+\binom{d+1}{2}-\sum_{s<r}\binom ks
\]

remaining short cells.  Hence `z<=sigma`.  Finally

\[
 (\gamma(p_R)-1)_+\le(q_R-1)_+
\]

termwise, so

\[
 \sum_R(\gamma(p_R)-1)_+\le D\le z\le\sigma.
\]

The `M` budget and the `sigma` budget are not being double-counted.  The
first counts physical cells in the length-`d+1` row; the second controls how
many missing values from that row can consume residual cells in the
width-`d` short band.  Identity (3.1) is the exact bridge between them.

## 4. Exact `k=11` arithmetic

For `k=11,n=465,r=6`,

```text
M=462, d=3, sigma=369,
f_3(1,2,3,4)=1,3,6,9.
```

Using the closed formula gives:

| `p` | last failing `q` | its capacity | first passing `q` | capacity/demand |
|---:|---:|---:|---:|---:|
| 28 | 6 | 61 | 7 | 63 / 62 |
| 29 | 4 | 61 | 5 | 63 / 62 |
| 30 | 2 | 61 | 3 | 63 / 62 |
| 31 | 0 | 61 | 1 | 63 / 62 |
| 32 | - | - | 0 | 63 / 63 |

Consequently

\[
 \gamma_{6,3}(28,29,30,31,32)=(7,5,3,1,0).
\]

The `M=462` budget is exactly

\[
 \boxed{7a_{28}+5a_{29}+3a_{30}+a_{31}\le462.}
\]

Subtracting one credit and using `sigma=369` gives exactly

\[
 \boxed{6a_{28}+4a_{29}+2a_{30}\le369.}
\]

The stated tail consequences are correct:

* `a_28<=floor(369/6)=61`;
* `a_28+a_29<=floor(369/4)=92`;
* `a_28+a_29+a_30<=floor(462/3)=154`.

The supplied checker reproduces both coefficient rows and checks that the
exact charge dominates the older linear charge `(32-p)_+` throughout the
active tested range `28<=p<80`.

## 5. Boundary-core branches

At exact `k=11` equality, rank-filtration/boundary-core rigidity gives a
single rank-at-most-five core and `h_6 in {0,1}` distinct literal six-set
boundary entries.  Every proper subset of every six-set has every witness
wholly inside the core.

Let `p_U^C` count core positions contained in `U`.  Core support runs still
have length at most four.  They need to supply all 62 proper targets, whether
or not `U` itself is a boundary literal.  The maximum capacity on 27
positions is only 60, so `p_U^C>=28`.  With the core demand fixed at 62 for
all `q`, direct evaluation gives again

```text
p_U^C : 28 29 30 31 >=32
credit:  7  5  3  1   0.
```

This explains why a core support of 31 still costs one long run even for the
literal boundary value: zero four-runs supply only 61 proper-target cells.

The core has length `465-h_6`, hence exactly

\[
 (465-h_6)-4+1=462-h_6
\]

length-four windows.  Summing exact-rank-six core runs therefore gives

\[
 7a_{28}^C+5a_{29}^C+3a_{30}^C+a_{31}^C\le462-h_6.
\]

Thus the two displayed branches are exactly

```text
h_6=0: RHS 462,
h_6=1: RHS 461.
```

Both are correct.  No special exemption at core support 31 is needed.

## 6. Final scope

The result is an unrestricted necessary condition.  It neither constructs a
length-465 word nor contradicts one.  Its principal gain over the linear
amortized theorem is distributional: the `k=11` charge vector improves from
`4,3,2,1` to `7,5,3,1`, with the independent residual row `6,4,2`.
