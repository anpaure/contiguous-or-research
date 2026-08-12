# Rayleigh second rearrangement: an exact signed-moment reduction

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional reduction.  The signed first moment after the
second anchored-component rearrangement is nonpositive once one explicit
positive-lobe area inequality is proved.  The area inequality itself is
not proved here.

## 1. Setup

Let

\[
 H_1=\mathcal RK
\]

be the authenticated first Rayleigh transform.  Write

\[
 P=H_1(0)>0,
\]

let `beta` be its unique zero, let `b` be its unique minimum location,
and write

\[
 q=-H_1(b)>0.
\]

The one-well theorem gives

\[
 g(t)=-H_1'(t)>0\quad(0<t<b),
 \qquad
 f(t)=H_1'(t)>0\quad(t>b).
\]

The second equal-level rearrangement pairs the sockets in `(beta,b)`
with all jobs in `(b,infinity)`.  It leaves the socket bank

\[
 g(t)\mathbf1_{(0,\beta)}(t)dt                    \tag{1.1}
\]

and creates remainders of total count `q`.  Put

\[
 W=\int_0^\beta t g(t)dt
  =\int_0^\beta H_1(t)dt.                         \tag{1.2}
\]

The equality follows by integration by parts.  Exact work conservation
in the equal-level subtraction says that the new remainder bank also has
total first moment `W`.

## 2. Second-moment comparison

### Theorem 2.1

The second rearranged kernel `H_2=mathcal R^2K` satisfies

\[
 \boxed{
 \int_0^\infty tH_2(t)dt
 \le {W\over2}\left(\beta-{W\over q}\right).}    \tag{2.1}
\]

Consequently the scalar inequality

\[
 \boxed{\int_0^\beta H_1(t)dt\ge q\beta}          \tag{2.2}
\]

implies

\[
 \boxed{\int_0^\infty tH_2(t)dt\le0.}            \tag{2.3}
\]

Strict inequality in (2.2) gives strict inequality in (2.3).

### Proof

For a signed-tail kernel, Fubini gives

\[
 \int_0^\infty tH_2(t)dt
 ={1\over2}left(
   \int y^2\,d\nu_2(y)-\int x^2\,d\mu_2(x)
 \right),                                        \tag{2.4}
\]

where `nu_2` is the remaining socket measure (1.1) and `mu_2` is the
second remainder measure.

Every remaining socket has size at most `beta`, so

\[
 \int y^2\,d\nu_2(y)
 \le\beta\int y\,d\nu_2(y)=\beta W.              \tag{2.5}
\]

The remainder measure has mass `q` and first moment `W`.  Cauchy--Schwarz
therefore gives

\[
 \int x^2\,d\mu_2(x)\ge {W^2\over q}.            \tag{2.6}
\]

Substitution of (2.5)--(2.6) in (2.4) proves (2.1), and (2.2) gives the
remaining assertions. `square`

## 3. Exact surviving scalar

The area condition (2.2) can be written as

\[
 {1\over\beta}\int_0^\beta H_1(t)dt\ge q.        \tag{3.1}
\]

Thus it compares the average height of the first positive lobe with the
depth of its negative lobe.  The authenticated count theorem gives only

\[
 q<P<2q,
\]

which does not by itself imply (3.1).  Proving (3.1) requires genuine
Rayleigh shape information on `H_1`, not merely its endpoint heights.

If (3.1) is established, the nonpositive signed-moment barrier is
verified through `H_2`.  The all-iterate moment barrier remains a separate
problem; this theorem makes no induction claim.

## 4. Frozen dependencies

1. `MATH_THEOREM_ANCHORED_NEGATIVE_COMPONENT_REARRANGEMENT_OPERATOR_20260805.md`,
   SHA-256
   `d25d240c3bafc39e4b581dfa5fbb0379dfa6dd9a76e00458d24227a146e0ba8b`.
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`,
   SHA-256
   `910adbabec163e81d7896e155255561ec00463ca8fb67b9c7bf69aebd9588e20`.
3. `MATH_THEOREM_RAYLEIGH_FIRST_TRANSFORM_EXACT_TWO_THREE_COUNT_WINDOW_20260805.md`,
   SHA-256
   `1931d629efdcf12c2ec0167a004ead83e547050d44bc23464252dc0a1e062a10`.

