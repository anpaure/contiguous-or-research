# Independent audit: five-slot two-efficient wedge and least endpoint normalization

**Date:** 2026-08-04  
**Verdict:** **PASS after two scope repairs.**  The derivative/tail envelope,
strict concavity, both endpoint certificates, scalar-wedge monotonicity, and
complete five-slot size-two-efficient branch exhaustion are correct.  The
least-critical endpoint theorem and the `h=n => c_n=A` branch assignment are
also correct.

No search, H100 computation, solver, or parameter enumeration was used.
The endpoint certificates were checked as exact rational inequalities, not
as floating-point signs.

## 1. Audited sources and repairs

| role | file | before SHA-256 | after SHA-256 |
|---|---|---|---|
| five-slot wedge | `MATH_THEOREM_FIVE_SLOT_TWO_EFFICIENT_SMALL_PERIOD_WEDGE_CLOSURE_20260804.md` | `04f984fb18194ded852be68e23c2ec9376f62c46c98289397460ff3a46604b3a` | `a678fc5a33c6457d9d640aa963d902fdb8c7ed932ade6a14fd320caf8d285e43` |
| endpoint normalization | `MATH_THEOREM_LEAST_CRITICAL_ENDPOINT_THRESHOLD_NORMALIZATION_20260804.md` | `a4f737dc79869e65a3076c6e551974a8f1119f3b3829ff778c1585ee26037c02` | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |

The audit-note hash is reported outside the note.

Two repairs were applied.

1. The five-slot theorem now explicitly assumes a nonnegative table.  This
   is inherited from the Bellman setting and is needed for the compact
   kernel comparisons and the displayed inequalities `0<=x`, `0<=z`.
2. The endpoint theorem now disposes of `n=1` before defining `P_n`, whose
   exact-capacity lower-denomination partition set would otherwise be empty.
   It also spells out why `c_n=P_n` makes the endpoint Bellman-inert.

No mathematical conclusion was weakened.

## 2. Exact derivative and tail envelope

Normalize `y=At`, `s=Au`, with

\[
 2/5\le t\le1/2,
 \qquad1-2t\le u\le t/2.
\]

For the shifted train `F_(At)(Au)`, the terms `q=0,1` are compact and all
terms `q>=2` are on the Gaussian tail.  Direct differentiation gives

\[
 {d\over du}F_{At}(Au)=-2A^2 W_t(u),
\]

where

\[
 W_t(u)=h(1-u)+h(1-t-u)
       -\sum_{q\ge0}h(1+u+qt),
 \qquad h(v)=ve^{-\pi v^2/4}.
\]

The signs and the index origin are exact: the positive terms in the sum with
`q=0,1` are the `A+x` halves of the two compact derivatives, while the
remaining sum is the differentiated tail.

Put `x=1+t+u`.  It satisfies `x>=3/2`, beyond the maximum of `h`, so `h`
is decreasing throughout the sampled tail.  The spacing-`t` integral test
gives

\[
 \sum_{q\ge1}h(1+u+qt)
 \le h(x)+h(x+t)+{1\over t}\int_{x+t}^{\infty}h(v)\,dv
 =h(x)+h(x+t)+{e^{-a(x+t)^2}\over2at}.
\]

Thus `W_t>=H_t` with exactly the envelope displayed in the theorem.  There
is no omitted `q=1` term or spacing factor.

## 3. Concavity of the envelope

The derivatives

\[
 h''(z)=2az(2az^2-3)e^{-az^2},
\]

and

\[
 h'''(z)=2ae^{-az^2}(-4a^2z^4+12az^2-3)
\]

are correct.  On `[3/4,5/4]`, `q=az^2` lies inside `[1/3,3/2]` using
`157/50<pi<22/7`.  The quadratic `-4q^2+12q-3` is positive there: it is
concave and its endpoint values are positive.  Hence `h''` increases on
that interval and

\[
 h''(1-u)-h''(1+u)\le0.
\]

The remaining argument ranges are exact:

\[
 1/4\le1-t-u\le1/2,
 \quad x\ge3/2,
 \quad x+t\ge2.
\]

Therefore the `h(1-t-u)` contribution has negative second derivative, both
subtracted `h` terms contribute negatively, and the subtracted exponential
integral term also has negative second derivative.  At least one inequality
is strict, so `H_t''(u)<0`.  A concave function's minimum on the compact
shift interval is at an endpoint.

## 4. Lower endpoint certificate

Substitution of `u=1-2t` gives exactly

\[
 L(t)=h(2t)-h(2-2t)+h(t)-h(2-t)-h(2)
      -{e^{-4a}\over2at}.
\]

Its derivative in the theorem is correct.  On `2/5<=t<=1/2`:

* `h'(2t)<=0`, since `pi>25/8`;
* `h'(2-2t)<=h'(1)` and `h'(t)<=h'(2/5)`, because `h''<0` on the relevant
  intervals;
* `h'(2-t)<=h'(8/5)`, because `h''>0` on `[3/2,8/5]`;
* the differentiated integral term is at most
  `(25/(2pi))e^{-pi}`.

After substituting the sign-safe Taylor bounds, this upper derivative is
exactly the rational `D_L` from (1.5), hence is below `-1/20`.  Thus `L`
decreases and `L(t)>=L(1/2)`.

At `t=1/2`, the `h(1)` terms cancel and

\[
 L(1/2)={1\over2}e^{-\pi/16}
        -{3\over2}e^{-9\pi/16}
        -\left(2+{4\over\pi}\right)e^{-\pi}.
\]

The three sign-safe replacements in `B_L` are in the correct directions:
`Q_9` lowers a positive exponential term; `1/P_8` raises the exponentials
carrying negative coefficients; and `pi>157/50` raises the adverse
coefficient bound.  Exact cross-multiplication gives `B_L>1/100`.

## 5. Upper endpoint certificate

At `u=t/2`, the decomposition into `D_1`, `D_3`, the last `h` term, and the
integral tail is exact.  Differentiation gives

\[
 D_1'(t)=-{1\over2}\bigl(h'(1-t/2)+h'(1+t/2)\bigr),
\]

and

\[
 D_3'(t)=-{3\over2}\bigl(h'(1-3t/2)+h'(1+3t/2)\bigr).
\]

The rational checks (1.6)--(1.7), together with decrease of `h'` on
`[1/4,5/4]` and increase on `[3/2,7/4]`, imply

\[
 D_1'(t)>0,
 \qquad D_3'(t)<0.
\]

Therefore `D_1(t)>=D_1(2/5)` and `D_3(t)>=D_3(1/2)`.
Since `1+5t/2>=2`, monotonicity of `h` and `t>=2/5` give the two tail bounds
in (5.6).  Each term in `B_R` is exactly the corresponding sign-safe Taylor
bound for

\[
 D_1(2/5)+D_3(1/2)-h(2)-{5\over\pi}e^{-\pi}.
\]

Exact rational cross-multiplication gives `B_R>1/100`.  Both shift endpoints
are therefore strictly positive.

## 6. Scalar wedge sign

Strict concavity and the endpoint bounds yield `H_t(u)>0`, hence
`W_t(u)>0`.  The derivative identity has the negative sign, so
`F_(At)(Au)` decreases in `u`.  Since `u<=t/2`,

\[
 F_{At}(Au)\ge F_{At}(At/2).
\]

The two period-`At` residue classes at shifts zero and `At/2` interlace
exactly into the arithmetic clock of step `At/2`:

\[
 C(At)+F_{At}(At/2)=C(At/2)>0.
\]

Thus `mathcal L_2(At;Au)>0` throughout the closed normalized wedge.  This
also covers the limiting boundary `t=1/2`, although the five-slot
first-crossing application uses `t<1/2`.

## 7. Exhaustion of the five-slot size-two branch

Let the nonnegative table be `(0,x,y,z,w,T)` and suppose `y/2` is maximal.
Internal superadditivity and efficiency give

\[
 w\ge2y,
 \quad w/4\le y/2,
\]

so `w=2y`.  Put `s=T-2y`.  The inequalities

\[
 T\ge x+w,
 \quad T\ge y+z,
 \quad z\ge x+y,
 \quad T/5\le y/2
\]

give

\[
 x\le z-y\le s\le y/2.
\]

If the first threshold occurs before slot five, first-crossing deletion
reduces to an already-proved positive table of at most four slots and the
full functional is no smaller.  Otherwise `w=2y<A<=T`, yielding

\[
 2A/5\le y<A/2,
 \qquad A-2y\le s\le y/2.
\]

The exact odd/even Bellman clock has baseline shift `s`; its capacity-one
and capacity-three values are respectively `x` and `z`, rather than `s`
and `y+s`.  Hence

\[
 \Phi=\mathcal L_2(y;s)+K(x)-K(s)+K(z)-K(y+s).
\]

No transient is missing.  The concavity argument for
`pi q-2 arctanh(q)` proves `K` decreases on `[0,3A/4]`.  The derived bounds

\[
 0\le x\le s,
 \qquad0\le z\le y+s\le3y/2<3A/4
\]

make both corrections nonnegative.  The scalar wedge is strictly positive,
so the complete size-two-efficient branch passes, including efficiency
ties assigned to it.

## 8. Least-critical endpoint normalization

For `n>=2`, saturation sets

\[
 c_n'=\max(A,P_n).
\]

If `c_n'>A`, then `c_n'=P_n`.  Choose an attaining exact-capacity partition
`n=j_1+...+j_t`.  The identity

\[
 {c_n'\over n}
 =\sum_i{j_i\over n}{c_{j_i}\over j_i}
\]

writes the endpoint density as a weighted average of lower densities.
At least one lower density is at least this average.  Therefore an endpoint
which is strictly denser than every lower denomination cannot satisfy
`c_n'>A`; saturation forces `c_n'=A`.

Assigning a saturated table to the least density maximizer `h`, the event
`h=n` is exactly the strict inequality against every lower index, since
`n` is the largest available index.  The theorem therefore gives
`c_n=A` on that branch.

If instead `c_n=P_n>A`, replacing every occurrence of the size-`n`
generator by one fixed attaining lower partition preserves both capacity
and value in every Bellman configuration.  The endpoint is Bellman-inert,
and the weighted-average argument supplies a lower denomination of density
at least `c_n/n`; consequently the least maximizer has `h<n`.

For `n=1`, saturation directly gives `c_1'=A`, so the same corollary holds
without defining an empty lower-partition maximum.  The five-slot
specialization to a genuinely size-five-efficient branch is valid.

## 9. Scope

The first theorem closes only the five-slot maximal-size-two branch.  It
does not address maximal sizes three, four, or five.  The second theorem is
only a branch normalization: an inert endpoint may still display the first
threshold and need not be deleted while preserving the chosen
first-crossing presentation.

Neither result proves the all-slot Bellman inequality or an OR-word
additive bound.

