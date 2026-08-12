# Independent GO audit: adjacent principal-star protected closure

**Date:** 2026-08-04  
**Method:** independent symbolic derivation; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_PRINCIPAL_STAR_UNION_PROTECTED_CROSSING_CLOSURE_20260804.md`  
**Audited theorem SHA-256:**
`33c60f18e4eded178218a0619b664948b9c8fca5ac67ce13778f2a44cd8014a7`

## Verdict

**GO after correction and strengthening.**

The exact owner fibres, cardinality, weighted slack, crossing-plus-swap
identity, all three asymptotic rank regimes, and fixed-`h` extension are
correct.  The original per-path bounds `6` and `4h-2` were valid but not
sharp.  Ownerwise monotone-DNF domination gives the stronger bounds `4` and
`2h`; the theorem and self-audit have been patched accordingly.  Thirteen
missing display-math closing delimiters were also repaired.  These were
formatting defects, not mathematical gaps.

## 1. Exact two-centre fibres and sizes

Let `|H|=c-1=m-r-1`.  An owner containing `H` has exactly `r+1`
coordinates outside `H`.

* With exactly one of `a,b`, deleting that pivot is the only deletion which
  destroys the lower DNF; the fibre is `r`.
* With both pivots, every deletion outside `H` leaves a pivot; the fibre is
  `r+1`.

After removing `H,a,b`, the residual ground set has size
`N=m+r-2`.  The two owner types therefore number

\[
 2{N\choose r},\qquad {N\choose r-1}.
\]

On the lower shore, either choose one principal star and subtract their
intersection, or choose one/two pivots directly.  With
`B=binom(N,r-1)`, this gives

\[
 |A|=2{N+1\choose r-1}-{N\choose r-2}
     =2B+{N\choose r-2}
     ={2m+r-1\over m}B.
\]

For `r>=2`, the weighted Ore contributions of fibres `r,r+1` are

\[
 {2(m-r)\over m},\qquad {2(m-r-1)\over m}.
\]

Multiplying by the two owner counts proves (1.7), and
`binom(N,r)=(m-1)B/r` proves (1.8).  For `r=1`, there are
`2(m-1)` fibre-one owners and one fibre-two owner, yielding

\[
 {m-2\over m}2(m-1)+{2(m-2)\over m}=2(m-2).
\]

Thus all fibre and slack formulas replay exactly.

## 2. Exact path-loss identity

For `r>=2`, every selected owner has fibre at least two, so its protected
loss is precisely the number of protected incidences to lower facets outside
the cut.

For one projected Johnson edge `UV`, with `X=U cap V`:

1. if exactly one endpoint lies in `Q`, then `X` cannot contain `H` and a
   pivot, since both supersets would then lie in `Q`; exactly one loss unit
   is incurred;
2. if both endpoints lie in `Q` but `X` lies outside the lower DNF, then
   `X` still contains `H` and contains no pivot.  Johnson adjacency forces
   the endpoints to have pivot states `{a}` and `{b}`.  Both incidences are
   lost, giving weight two;
3. no other edge contributes.

This independently proves

\[
 \lambda_P(A)=|\partial_PQ|+2\tau_P(H;a,b).
\]

The factor two is necessary.

## 3. Sharp per-path bounds

The old direct estimate gave at most four union-boundary edges plus one
double-priced swap, hence six.  It is safe but loose.

At any owner, a facet outside the union is outside every individual star
active at that owner.  Hence, path by path,

\[
 \lambda_P\left(\bigcup_i\mathcal A_{C_i};\text{path}\right)
 \le\sum_i\lambda_P(\mathcal A_{C_i};\text{path}).
\tag{3.1}
\]

For one core, coordinate-interval convexity makes the owner star an interval
on the protected path, so its crossing loss is at most two.  Equation (3.1)
therefore gives

\[
 \lambda_P(A;\text{path})\le4
\]

for two stars and

\[
 \lambda_P(A_h;\text{path})\le2h
\]

for `h` stars.  Consequently the patched global estimates

\[
 \lambda_P(A)\le4(2H_r+m+H_d)
\]

and

\[
 \lambda_P(A_h)\le2h(hH_r+m+H_d)
\]

are valid.  They imply the requested old `6` and `4h-2` bounds as immediate
weaker inequalities (`h>=2` in the latter comparison; `h=1` agrees exactly
at two).

## 4. Uniform two-centre closure

For `r>=2`, every nonzero fibre is at most `r+1`.  From

\[
 \sigma=(m-2)|A|-\sum_U(a_U-2)_+,
 \qquad
 {a-2\over a}\le{r-1\over r+1},
 \qquad
 \sum_Ua_U=m|A|,
\]

one obtains

\[
 \sigma\ge\left({2m\over r+1}-2\right)|A|.
\]

### Small `r`

If `r<=m/10` and `m>=190`, the coefficient is at least 17.  Also
`|A|>=m+1`, so

\[
 15|A|+2m<17|A|\le\sigma.
\]

This closes the whole small-rank regime by the frozen all-cut loss estimate.

### Intermediate `r`

The first exact slack term implies

\[
 \sigma\ge{4\over m}{m+r-2\choose r-1},
\]

because

\[
 {(m-r)(m-1)\over r}\ge1
 \iff m(m-1-r)\ge0.
\]

For `m/10<=r<=m/2`, its ratio to `binom(m,r)` is at least

\[
 {r\over m+r-1}
 \left(1+{r-1\over m}\right)^r
 =\exp(\Omega(m)).
\]

This uniformly dominates `(r+1)binom(m,r)`, and hence `H_r`, as well as
`m+H_d`.

### Large `r`

Write `alpha=r/m`.  Up to `o(m)`, the binary exponent of
`binom(m+r-2,r-1)` is

\[
 (1+\alpha)H_2\left({\alpha\over1+\alpha}\right)m.
\]

In natural logs the corresponding function is

\[
 f(\alpha)=(1+\alpha)\log(1+\alpha)-\alpha\log\alpha,
\]

whose derivative is `log((1+alpha)/alpha)>0`.  Thus on
`alpha in [1/2,1]` its minimum is at `1/2`, giving binary exponent
`(3/2)H_2(2/3)>1`.  This uniformly dominates `H_r<=2^m` and `H_d=2^{o(m)}`.

For `r=1`, the shared owner contributes at most one more union-loss unit
than the two singleton rows together.  Hence `lambda<=21`, while
`sigma=2m-4`, closing `m>=13`.

## 5. Fixed-`h` extension

Outside `H` there are `h` pivots and

\[
 R=m+r-h
\]

nonpivots.  Choosing `s` pivots and respectively `r+1-s` or `r-s`
nonpivots proves the owner and lower counts (4.3)--(4.4).  The same deletion
argument gives fibre `r` at `s=1` and `r+1` at `s>=2`, so (4.5) follows.

At `r=1`, there are `h(m+1-h)` fibre-one owners and `binom(h,2)` fibre-two
owners.  Therefore

\[
 \sigma={m-2\over m}
 \left(h(m+1-h)+2{h\choose2}\right)=h(m-2).
\]

Every pair-shared owner can add at most one unit beyond the sum of singleton
losses, giving

\[
 \lambda_P(A_h)\le hR_0+{h\choose2}=O_h(1),
\]

which is eventually smaller than the displayed slack.

For `r>=2`, the small-rank proof is unchanged.  In the intermediate range,

\[
 {{m+r-h\choose r}\over{m\choose r}}
 \ge\left(1+{r-h\over m}\right)^r
 =\exp(\Omega_h(m))
\]

uniformly for `r>=m/10`; fixed `h` is eventually smaller than `r`.  In the
large range, subtracting fixed `h` changes the entropy exponent by only
`o(m)`.  The sharp loss bound has only a fixed factor `2h^2`, so the same
comparisons prove uniform closure for all `1<=r<=m-1`.

## 6. Scope

The GO verdict assumes exactly the four frozen reservoir properties listed
in Section 0 of the theorem.  It proves protected Ore safety for every fixed
number of adjacent equal-core-rank stars sharing one codimension-one root.
It does not address a growing number of centres, arbitrary shifted cuts,
factor component structure, endpoint collars, residence beyond the frozen
reservoir, or the common cap.
