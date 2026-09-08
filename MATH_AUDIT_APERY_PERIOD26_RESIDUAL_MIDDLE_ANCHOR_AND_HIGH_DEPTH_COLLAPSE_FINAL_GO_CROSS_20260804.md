# Independent audit: period-26 residual middle anchor and high-depth collapse

**Date:** 2026-08-04  
**Verdict:** `FINAL_GO_CROSS` for the corrected theorem bytes below.
The submitted SHA `497e59d075f6af97fb64d2f5a62e6843e97bced41b837ca14159e9fb60e448c1`
required three exact proof-preserving corrections:

1. replace the malformed literal `le` in (2.4) by `\le`;
2. explicitly justify `f(1/2)<C` before the second endpoint minimum in
   (4.5), using Jacobi reflection and the theta sign/bound;
3. in Theorem 5.1(4), cite the chamber gates (4.6)/(4.7), not the
   preliminary formulas (4.4)/(4.5).

Those corrections are now present.  No substantive inequality or scope
claim changed.

## 1. Audited theorem

| file | SHA-256 |
|---|---|
| `MATH_THEOREM_APERY_PERIOD26_RESIDUAL_MIDDLE_ANCHOR_AND_HIGH_DEPTH_COLLAPSE_20260804.md` | `b1f3c516683ba0453f62bf76ff7806dc773477adf32587c31c51c304a888fe77` |

This audit is purely mathematical.  It uses no search, solver, optimizer,
or chamber sampling.

## 2. Audit of the uniform floor

For `0<=x<=1/2`,

\[
 f(x)=1-e^{-\pi(1-x)^2/4}
 -\sum_{q\ge0}e^{-\pi(1+x+q)^2/4}.
\]

At `x=6/13`, the first four adverse exponents are exactly

\[
 {49\pi\over676},
 \quad {361\pi\over676},
 \quad {256\pi\over169},
 \quad {2025\pi\over676}.
\]

Substitution of `pi>333/106` gives the exact rational lower exponents

\[
 {16317\over71656},
 \quad {120213\over71656},
 \quad {85248\over17914},
 \quad {674325\over71656}.
\]

Independent positive-Taylor cross multiplication verifies

\[
 S_3(16317/71656)>{1000\over797},
\]

\[
 S_7(120213/71656)>{250\over47},
 \qquad
 S_7(85248/17914)>100,
\]

\[
 S_{16}(674325/71656)>10000,
\]

where `S_n(z)=sum_(j=0)^n z^j/j!`.  Hence all four displayed Gaussian
upper bounds in the theorem have the correct strict direction.

For the omitted tail, the first exponent is larger than

\[
 {280053\over17914}>15.
\]

The stronger exact checks

\[
 S_{10}(15)>{1000000\over99},
 \qquad
 S_5(42957/5512)>100
\]

show that the first omitted term is below `99/1000000` and every
successor ratio is below `1/100`.  Therefore

\[
 \sum_{j\ge4}e^{-\pi(j+6/13)^2/4}
 <{99/1000000\over1-1/100}
 ={1\over10000}.
\]

This supplies the small strengthening tacit in the submitted tail line.
The full endpoint ledger is then

\[
 1-{797\over1000}-{47\over250}-{1\over100}
 -{1\over10000}-{1\over10000}
 ={3\over625}>{1\over250}.
\]

At the other endpoint,

\[
 C>{5503\over125000}>{1\over250}.
\]

Since every interior critical point on `[0,1/2]` is a strict maximum,
the minimum on `[0,6/13]` is an endpoint.  Thus

\[
 \boxed{f(x)>1/250\quad(0\le x\le6/13)}
\]

is valid.

## 3. Prefix-average and depth audit

For an honest period-26 cyclic table, prefix minimality gives

\[
 {s_r\over A}\le {rP\over26A}
 ={r(1-\alpha)\over26}<{r\over26}.
\]

The exact middle train at reflected depth `u` is

\[
 \mathcal M=\sum_{r=u+2}^{25-u}f(s_r/A).
\]

When `6<=u<=10`, the first index is between `8` and `12`, so

\[
 0<{s_{u+2}\over A}<{u+2\over26}\le {12\over26}={6\over13}.
\]

The middle train therefore contains one literal term strictly larger than
`1/250`; every other term is nonnegative.  Hence

\[
 \mathcal M>{4000\over1000000}.
\]

The authenticated residual identities contain `mathcal M` as an exact
nonnegative summand.  Their resulting margins are correctly computed:

\[
 -1882+4000=2118,
 \qquad
 -1648+4000=2352
\]

in units of `10^-6`.  This proves strict positivity for both residual
chambers at every depth `6<=u<=10`.

## 4. Depth-eleven reduction audit

At `u=11`, the middle-index interval is exactly `13<=r<=14`, so

\[
 \mathcal M_{11}=f(s_{13}/A)+f(s_{14}/A).
\]

With `z=s_13/A` and `w=s_14/A`, the depth definition gives `w<=1/2`,
the minimum-gap theorem gives `w-z>=alpha`, and prefix averaging gives
`z<=(1-alpha)/2`.  In particular

\[
 z\le w-\alpha\le1/2-\alpha.
\]

Minimum-gap spacing also gives `X_6=s_7/A>=7alpha`.  Both residual
chambers have `X_6<2/13`, hence

\[
 \alpha<2/91,
 \qquad 1/2-\alpha>1/3.
\]

Strict decrease from `2/13` and the inherited one-third anchor yield

\[
 f(1/2-\alpha)<f(1/3)<29/750<L<C.
\]

For the second endpoint minimum, Jacobi reflection gives

\[
 2f(1/2)=g(1/2),
\]

while the authenticated sign and absolute bound give

\[
 0<f(1/2)<\varepsilon/2<C.
\]

The no-interior-minimum theorem therefore proves exactly

\[
 \mathcal M_{11}
 \ge f(1/2-\alpha)+f(1/2).
\]

Removing the middle train from the nonnegative residual slack then gives
the two sufficient gates (4.6) and (4.7).  This is a reduction only: the
audit does not assign either gate a sign.

At `u=12`, the index interval `14<=r<=13` is empty, so no new credit is
available and the original residual gates remain unchanged.

## 5. Scope and non-overclaim audit

The corrected theorem proves:

* positivity of both residual chambers for `6<=u<=10`;
* reduction of `u=11` to the two explicitly displayed central-rail gates;
* no improvement at `u=12`.

It does **not** close `u=11`, close `u=12`, prove complete period-26
positivity, treat shoulders or later carries, or make an OR-word claim.

**Final independent verdict on corrected SHA `b1f3c516...`:**
`FINAL_GO_CROSS`.
