# Audit: forced Pascal endpoint flow and minimum-slice no-go

**Date:** 2026-08-04  
**Method:** independent symbolic replay; no search, solver, or finite census  
**Audited theorem:**
`MATH_OBSTRUCTION_PASCAL_ENDPOINT_FORCED_SQUARE_FLOW_AND_MINIMUM_SLICE_NOGO_20260804.md`

## Verdict

**GO**, with the following exact scope.

The rank-flow identity, the rank-two contradiction, the closed-form minimum
augmentation, the terminal singleton correction, and the short exact-trace
witness path are correct.  The theorem deliberately does not claim an
occurrence-level endpoint matching after augmentation, preservation of all
distinguished paths under arbitrary deletions, or a one-cycle quotient.

## 1. Independent flow replay

At residual trace rank `q`, let `e_q` incidences go upward by an external
step.  The remaining `2R_q-e_q` go horizontally by a `K`-step.  Components at
owner-trace rank `q` receive the latter incidences and the `e_(q-1)` upward
incidences from the previous residual rank.  Therefore

\[
 2C_q=2R_q-e_q+e_{q-1}.
\]

With `e_(-1)=0` and

\[
 R_q-C_q=a_q^2-a_{q-1}^2,
\]

this gives

\[
 e_q=2\sum_{j=0}^q(R_j-C_j)=2a_q^2.
\]

No endpoint orientation or probabilistic symmetry enters this argument.

## 2. Rank-two contradiction

For `q=2`, one trace has

\[
 v_2=m-1,qquad l_2=\binom{m-1}{2},qquad
 r_2=l_2-v_2+1=\binom{m-2}{2}.
\]

Across `binom(m,2)` traces,

\[
 R_2^{\min}
 =\binom m2\binom{m-2}{2}
 =\binom{m-1}{2}^2-\binom{m-1}{2}.
\]

The forced upward demand is twice
`binom(m-1,2)^2`, strictly larger than the total residual capacity
`2R_2^min`.  This verifies the no-go for every `m >= 4`.

## 3. Component formula and augmentation

Pascal gives the number of traces

\[
 \binom mq=a_{q-1}+a_q.
\]

On the increasing half, `b_q^min=1`, so
`C_q^min=a_(q-1)+a_q`.  On the decreasing half,
`b_q^min=a_(q-1)-a_q`, so

\[
 C_q^{\min}
 =(a_{q-1}+a_q)(a_{q-1}-a_q)
 =a_{q-1}^2-a_q^2.
\]

The square-flow capacity requires `C_q >= a_(q-1)^2`.  Hence the displayed
rankwise deficits in the theorem follow.  At the top, rank flow asks for one
residual co-singleton, but the unique full-trace owner is a singleton with two
literal endpoint slots.  A simple incidence edge cannot be repeated, so two
distinct residual co-singletons are necessary; this adds exactly one further
deletion.

Summing the squared terms leaves every `a_j^2` except `a_h^2`, while the two
endpoint squares are the terminal `+2`.  Vandermonde then gives

\[
 \Delta_{\rm phys}
 =\binom{2m-2}{m-1}-a_h^2
  -\sum_{q=2}^{h}(a_{q-1}+a_q).
\]

Both subtracted terms are lower order than `binom(2m-2,m-1)`, and its ratio
to `W=binom(2m-1,m)` tends to one half.  The `Theta(W)` classification is
therefore correct.

## 4. Short witness path replay

For `s=m-q`, the windows

\[
 H_j=\{x_{j+1},\ldots,x_{j+s}\},\qquad0\le j<q,
\]

fit exactly in the `m-1=q+s-1` ordered coordinates.  Consecutive windows
exchange one coordinate, their intersections are distinct `(s-1)`-windows,
and their union is all of `K`.  Complementing gives a Johnson path of
`(q-1)`-sets with distinct `q`-set union labels and empty total
intersection.  Thus its actual owners have union `K union T`.

The square component total leaves `a_(q-1)a_q` same-trace edges.  Dividing by
the number of traces gives

\[
 \frac{a_{q-1}a_q}{a_{q-1}+a_q}
 =\frac q m a_q\ge q-1
\]

for `2 <= q <= m-2`.  This verifies scalar compatibility only; extension of
all prescribed short paths into one exact forest family remains open, as the
theorem states.

## 5. Scope exclusions checked

The note does **not** infer any of the following:

* that the rooted literal square works on the increasing half;
* that one residual top connector may be used twice;
* that rank capacities imply Hall;
* that deleting arbitrary slice edges preserves `K union T` witnesses;
* that an all-`E` square completion contains cross-rank chains;
* that any completed quotient is connected;
* residence, arbitrary-upper, or common-cap compatibility.

These exclusions are necessary and are stated in the audited theorem.
