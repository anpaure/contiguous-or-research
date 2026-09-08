# Independent audit of the small-deficit wedge seal

## Verdict

**PASS.**  The square-root cover error, exact gap correction, affine
optimization, and threshold constant are correct.  The theorem is a
fixed-bottom-threshold result for `delta<delta_0`; it does not use common
lifetimes and does not treat larger deficits.

## Cover error

If `R_i` is the number of missing positive levels in direction `i` and
`q_i` is the total selected negative count in the other two directions,
wedge slices give

\[
D_a\ge\sum_i{(R_i-q_i)_+\choose2}.
\]

Convexity and `D_a<=delta a^2+o(a^2)` imply

\[
P+2N\ge3-\sqrt{6\delta}.
\]

Thus `P<=2f-3+sqrt(6delta)` and the same holds for absorbed mass `A`.

## Gap inequality

The pointwise inequality

\[
\phi(p,s,z)+(4-s)z\ge p+s-1
\]

passes all three regions: before the factor switch, after the switch while
`z<s`, and after the second factor vanishes.  It gives a total correction at
most `3 int z`, and the coefficient three is attained at `p=s=2,z=1`.

## Optimization

With `epsilon=sqrt(6delta)`, the two absorbed-base bounds are

\[
C\le4f-6+2\epsilon,
\qquad
C\le3-2\delta+\epsilon.
\]

The exact seam identity therefore yields

\[
U\le\min(3f-3+2\epsilon+3\delta,
          6-f+\epsilon+\delta).
\]

The branches meet at `(9-epsilon-2delta)/4`, giving

\[
U\le15/4+(5/4)\sqrt{6\delta}+(3/2)\delta.
\]

Solving strict inequality against four gives

\[
\delta_0={ (\sqrt{29}-5)^2\over24}
=0.0061813303606\ldots .
\]

No normalization or endpoint correction survives the limit.
