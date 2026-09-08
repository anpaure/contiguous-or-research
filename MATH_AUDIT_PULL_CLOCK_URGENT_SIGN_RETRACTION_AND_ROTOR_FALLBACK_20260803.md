# Urgent pull-clock sign audit: retract the pasted derivation, retain the corrected theorem

**Date:** 2026-08-03

**Status:** exact algebraic retraction and independent proof audit.  The
newly pasted derivation quarantined by handoff item `2580B` is invalid and
must not be cited.  The authoritative corrected pull-clock theorem is algebraically
sound, and the independent monotone-rotor theorem separately proves the
fractional conclusion

\[
                         q\in\mathsf{ST}_{k,r,d}.       \tag{0.1}
\]

No fixed-host ticket pushforward, one-copy integral rounding, Euler fusion,
or `B(k)+O(1)` consequence is asserted here.

## 1. Exact retraction of the pasted sign chain

Let

\[
 p_s={\binom{k}{s}\over W},\qquad
 R_s={p_s\over p_{s-1}}={k-s+1\over s}.               \tag{1.1}
\]

Then

\[
 R_s-R_{s+1}={k+1\over s(s+1)}>0,                     \tag{1.2}
\]

so `R_s` is strictly **decreasing**, not increasing.

For the pull coefficients

\[
 x_{\delta,j}
 =A_\delta\Delta_j-A_{\delta+1}\Delta_{j+1},          \tag{1.3}
\]

nonnegativity requires

\[
 {A_\delta\over A_{\delta+1}}
       \ge {\Delta_{j+1}\over\Delta_j}                \tag{1.4}
\]

in cross-multiplied form when a denominator can vanish.  The pasted bounds
`A_delta/A_(delta+1)<=rho` and
`Delta_(j+1)/Delta_j>=rho` point the other way and do not prove (1.4); in
the strict case they force `x_(delta,j)<0`.

Finally, in the intended positive-core range `c>0`,

\[
 c=r-d-1< {k+1\over2},
 qquad \rho={k-c+1\over c}>1.                         \tag{1.5}
\]

Thus `(1-rho)^(-1)<0` and cannot upper-bound a nonnegative geometric tail.
The valid denominator is `rho-1`, or equivalently one uses the contraction
factor `theta=1/rho<1`.

These three errors retract that derivation, not merely its exposition.

### Exact in-family counterexample to the pasted inequalities

At `k=15`,

\[
                 (r,d,c,\rho)=(8,3,4,3),\qquad h=0.
\]

Hence

\[
 {A_2\over A_3}
 ={\binom{15}{3}\over\binom{15}{2}}
 ={13\over3}>3,                                       \tag{1.6}
\]

contrary to the pasted upper bound.  With
`D_s=p_(s+1)-p_s`,

\[
 {\Delta_2\over\Delta_1}
 ={D_6\over D_5}
 ={6435-5005\over5005-3003}
 ={5\over7}<3,                                        \tag{1.7}
\]

contrary to the pasted lower bound, while
`1/(1-rho)=-1/2`.  This is a canonical triangular instance.

## 2. Independent derivation of the corrected sign chain

Let `b_s` be the left-filled Ferrers column counts, so

\[
 b_s\le b_{s-1},qquad
 q_s={\binom{k}{s}-b_s\over W}.                       \tag{2.1}
\]

Put

\[
 A_t=q_{c-t+1},qquad
 G_j=1-q_{c+j},qquad
 H=\sum_jG_j,qquad
 w_j={G_j\over H},qquad
 \Delta_j=w_j-w_{j+1}.                                \tag{2.2}
\]

Assume first the separated range `c>d`; the finite remainder is discussed
in Section 4.

For `s<=c`, monotonicity of (1.1) gives `R_s>=R_c=rho`.  Moreover

\[
\begin{aligned}
 W(q_s-\rho q_{s-1})
 &=\bigl(\tbinom{k}{s}-\rho\tbinom{k}{s-1}\bigr)
   +(\rho b_{s-1}-b_s)\\
 &\ge0.                                                \tag{2.3}
\end{aligned}
\]

The first term is nonnegative because `R_s>=rho`; the second is
nonnegative because `rho>1` and `b_(s-1)>=b_s`.  Reversing the low indices
therefore gives

\[
                  {A_\delta\over A_{\delta+1}}\ge\rho. \tag{2.4}
\]

In the high band the Ferrers correction is zero.  Directly,

\[
 D_s=p_{s+1}-p_s
     =p_s{k-2s-1\over s+1},                            \tag{2.5}
\]

and, when the denominator is positive,

\[
 {D_{s+1}\over D_s}
 ={(k-s)(k-2s-3)\over(s+2)(k-2s-1)}
 <{k-s\over s+1}<\rho\qquad(s\ge c).                 \tag{2.6}
\]

The zero middle endpoint satisfies the cross-multiplied weak inequality.
Since `Delta_j=D_(c+j)/H`, (2.6) yields

\[
                  {\Delta_{j+1}\over\Delta_j}\le\rho. \tag{2.7}
\]

Combining (2.4) and (2.7),

\[
 A_{\delta+1}\Delta_{j+1}
 \le {A_\delta\over\rho}(\rho\Delta_j)
 =A_\delta\Delta_j,                                   \tag{2.8}
\]

so every coefficient (1.3) is nonnegative.  The fact that `R_s` decreases
is used in the correct direction: on `s<=c`, its minimum is at `c`.

## 3. Independent derivation of the corrected cost bound

Put

\[
 P=\sum_tA_t,qquad
 \alpha=p_c,quad\beta=p_{c+1},\quad\gamma=p_{c+2},
 \quad\theta={1\over\rho}.                            \tag{3.1}
\]

Summing the coefficients exactly gives

\[
 {\cal C}=A_1+Pw_1+(P-A_1)(w_1-w_2).                 \tag{3.2}
\]

In the separated range `A_1=alpha`; on the boundary face `c=d`, the robust
form is `A_1<=alpha`.  Since (2.4) gives
`A_(t+1)<=theta A_t`,

\[
 P-A_1\le\theta P,qquad
 P-A_1\le {A_1\over\rho-1}.                           \tag{3.3}
\]

Because `H>=P`,

\[
 {P-\alpha\over H}\le\theta.                         \tag{3.4}
\]

The high-band identities are

\[
 Pw_1\le G_1=1-\beta,qquad
 w_1-w_2={\gamma-\beta\over H},                       \tag{3.5}
\]

and the same adjacent-difference calculation one step earlier gives

\[
                  {\gamma-\beta\over\beta-\alpha}
                  \le\rho.                            \tag{3.6}
\]

Substitution into (3.2), using `A_1<=alpha`, gives

\[
 {\cal C}
 \le\alpha+(1-\beta)+\theta\rho(\beta-\alpha)=1.     \tag{3.7}
\]

No factor `(1-rho)^(-1)` occurs.  For the `k=15` instance of Section 1,
the corrected cost is `10102/21879<1`.

## 4. Endpoint and finite-range audit

At the high endpoint, set `p_r=1`.  Then

\[
 \Delta_d={1-p_{r-1}\over H}
          ={p_r-p_{r-1}\over H},qquad\Delta_{d+1}=0, \tag{4.1}
\]

so the difference formula remains valid for both parities.  The standard
depth estimate gives `c>d` for `k>=15`.  The authoritative corrected theorem
checks `k<=14` by exact rational arithmetic.  The detailed audit extends the
symbolic proof to `c>=d` by retaining `A_1<=alpha`; the only positive-core
cases with `c<d` are `k=7,8,11` and are included in those finite checks.

As independent corroboration only, the existing exact-bigint verifier was
compiled locally from its frozen source and replayed through `k=400`; it
reported zero ratio, sign or cost failures.  The all-parameter conclusion
rests on Sections 2--3 plus the finite exact cases, not on this replay.

The literal block realization then follows from the proved cost bound: clear
denominators, concatenate low runs of length at most `d`, place a high
separator after each, and cycle `d+1` private labels.  Every full window has
the same owner, while direct suffix counting gives the staircase low gains
and high losses.  This establishes the specific corrected fractional
pull-clock construction.

## 5. Independent ratio-free proof of fractional membership

Even if the staircase construction were discarded, (0.1) follows from the
monotone-rotor theorem, whose proof contains no `rho`, `Delta`, `x`, or cost
argument.

Let

\[
 {\cal M}_{r,d}
 =\{0\le q_1\le\cdots\le q_{r-1}\le1:
                         \sum_sq_s\le d\}.             \tag{5.1}
\]

If `v_ell` is the indicator of the final `ell` ranks, successive differences
give

\[
 q=\sum_{\ell=1}^{r-1}\alpha_\ell v_\ell,qquad
 \alpha_\ell\ge0,quad
 \sum_\ell\alpha_\ell\le1,quad
 \sum_\ell\ell\alpha_\ell\le d.                    \tag{5.2}
\]

The vertices of this two-row polytope are

\[
 0,quad v_a\ (a\le d),\quad {d\over b}v_b\ (b>d),
 \quad {b-d\over b-a}v_a+{d-a\over b-a}v_b
       \ (a<d<b).                                      \tag{5.3}
\]

They have literal same-owner type circulations:

* `(r-d,1,...,1)` with its self-loop supplies `v_a`;
* uniform cyclic rotation of positive `(d+1)`-part compositions of `b+1`
  supplies `(d/b)v_b`, because the `d` cut positions are uniform among the
  `b` possible positions;
* the same rotor at depth `d-a`, followed by `a` terminal singleton age
  classes, supplies the two-support vertex in (5.3).

For every legal type edge `c->c'`, the labelled compatibility graph is
biregular.  If

\[
 N_c={r!\over\prod_i c_i!},quad
 D^+_{c,c'}=\prod_{i<d}\binom{c_i}{c'_{i+1}},quad
 D^-_{c,c'}={c'_0!\over c_d!\prod_{i<d}(c_i-c'_{i+1})!}, \tag{5.4}
\]

then `N_cD^+_(c,c')=N_(c')D^-_(c,c')`.  Giving every compatible
labelled arc weight `f_(c,c')/(N_cD^+)` lifts any type circulation to a
literal same-owner circulation.  Hence

\[
                         {\cal M}_{r,d}subseteq
                         \mathsf{ST}_{k,r,d}.           \tag{5.5}
\]

For the left-filled triangular boundary,

\[
 q_s={\binom{k}{s}-b_s\over W}                        \tag{5.6}
\]

is nondecreasing because the binomial ranks increase while `b_s` is
nonincreasing; it lies in `[0,1]`, and
`sum_s q_s=(Lambda-h)/W<=d`.  Thus (5.5) proves (0.1) independently.

## 6. Frozen proof status

The following statement is **RETRACTED**:

> The newly pasted reversed-ratio/`(1-rho)^(-1)` derivation proves the
> triangular pull-clock theorem.

The following statements are **PROVED**:

1. The corrected staircase sign and cost chain in Sections 2--4.
2. The resulting fractional stationary same-owner pull-clock realization.
3. Independently, the monotone-rotor inclusion (5.5) and hence
   `q in ST_(k,r,d)` for the triangular residual vector.

The following statements remain **UNPROVED**:

1. a literal pushforward of either fractional law into one fixed protected
   replacement-host ticket packet;
2. one-copy owner/target integral rounding, exact balance after private
   packet rounding, and connected Euler chronology;
3. protected residence, upper/source/common-cap, compiler and birail rows;
4. any unconditional `B(k)+O(1)` or `B+1` conclusion.

## 7. Authoritative sources

```text
MATH_THEOREM_TRIANGULAR_PULL_CLOCK_CORRECTED_20260801.md
  SHA 7302724eb8b405c2bf1efcc743a1de06809cd1f9b3134e07ba8aa6933b631b21
MATH_THEOREM_CORRECTED_PULL_CLOCK_PACKING_AND_FRACTIONAL_TRACE_CIRCULATION_20260801.md
  SHA 6ce355b0bb5f5ffeacfb4b44a3fb6225cb6772b96d61103a205257e3447b3465
MATH_AUDIT_PULL_CLOCK_RATIO_REPAIR_AND_ONE_COPY_GATE_20260801.md
  SHA 2e7e6e378fc9b636966485f0b2727547f6044061e42e736e7e371deb699194dc
MATH_THEOREM_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md
  SHA 157f446c9b728b4d54b03202c3add6f32d806261c682c87bfd2c9ac7e7f8435e
MATH_AUDIT_R_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md
  SHA 13de8d306dc142104a7a6180ba227c086f3a1f97bdf5ce9deef5467d190894d4
MATH_AUDIT_R_MONOTONE_ROTOR_LABELLED_BIREGULAR_LIFT_20260801.md
  SHA 3cb197f4dbd369657bc2d8e1d2b9ab6ecd82dc68563d90e2ea5b0058ac05c746
```

This 2026-08-03 audit was independently rederived in four lanes.  All four
agreed on the retraction boundary and on the corrected fractional theorem.
