# Independent audit: affine setup-cost first-crossing and Apéry no-descent theorem

**Date:** 2026-08-04  
**Verdict:** **GO.**  The theorem gives an exact all-grid structural
obstruction to first-crossing size descent.  It does not claim a
nonpositive Bellman functional, and this audit does not infer one.

## 1. Exact binding

Audited theorem:

`MATH_THEOREM_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_20260804.md`

SHA-256:

`408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce`

No theorem byte was changed during this audit.

## 2. Complementary-pair saturation formula

For any lower partition

\[
 n=j_1+\cdots+j_t,
\]

internal superadditivity collapses `j_2+...+j_t` to the single lower
entry `c_(n-j_1)`.  Hence its value is at most

\[
                         c_{j_1}+c_{n-j_1}.
\]

Every displayed complementary pair is itself an admissible partition.
Therefore

\[
 P_n=\max_{1\le i<n}(c_i+c_{n-i})
\]

exactly.  The stated three inert faces at `n=6` are consequently
`c_1+c_5`, `c_2+c_4`, and `2c_3`; none is omitted.

## 3. Audit of the affine family

The theorem sets

\[
 \alpha={A+2\beta\over n},\qquad
 c_j=\alpha j-\beta\ (1\le j<n),\qquad
 c_n=A=\alpha n-2\beta,
\]

with `0<beta<A/(n-2)`.

The bound on `beta` gives

\[
 c_1={A-(n-2)\beta\over n}>0.
\]

Every lower increment is `alpha`, while the final increment is
`alpha-beta=c_1>0`; hence the table is strictly increasing.  For
`i+j<n`,

\[
 c_{i+j}-(c_i+c_j)=\beta>0,
\]

whereas for `i+j=n` equality holds.  This proves every internal
superadditivity row.

Since

\[
 c_{n-1}=A-c_1<A,
\]

strict increase puts every lower entry below `A`, so the first crossing is
exactly `n`.  A lower partition of `n` into `t>=2` parts has value

\[
 \alpha n-t\beta\le\alpha n-2\beta=A,
\]

with equality for every two-part partition.  Thus `P_n=A`, endpoint
saturation is exact, and the endpoint is replaceable by any complementary
pair.

Likewise, a partition of `j<n` avoiding denomination `j` has at least two
parts and value at most

\[
 \alpha j-2\beta=c_j-\beta<c_j.
\]

Therefore every lower denomination is genuinely indispensable at its own
capacity; there is no hidden dominated lower generator.

For `j<n`, the density

\[
 \alpha-{\beta\over j}
\]

strictly increases with `j`.  Moreover direct subtraction gives

\[
 {c_{n-1}\over n-1}-{c_n\over n}
 ={\beta(n-2)\over n(n-1)}>0.
\]

Hence `h=n-1` is the unique maximum-density denomination, exactly as
claimed.

## 4. Exact clock and no-descent cycle

After replacing every endpoint part by a complementary lower pair, a
partition of capacity `m` into `t` lower parts has value

\[
                         \alpha m-t\beta.
\]

Because `beta>0`, maximizing value is equivalent to minimizing the number
of parts.  With maximum lower part `n-1`, that minimum is
`ceil(m/(n-1))`, and it is attained by quotient many `(n-1)`-parts plus
one remainder part when needed.  Therefore

\[
 V_m=\alpha m-\beta\left\lceil{m\over n-1}\right\rceil
\]

for every `m`, including `m=0`.

Put `h=n-1` and `P=c_h`.  For `m=qh+r`, this becomes

\[
 V_{qh}=qP,qquad V_{qh+r}=qP+c_r\quad(1\le r<h).
\]

Also

\[
 P=A-c_1<A,qquad P+c_1=A.
\]

Thus the Apéry table is exactly the lower prefix, has no availability
head, and remains subthreshold.  Deleting the inert endpoint and then
adjoining the first crossing returns the original table.  The proof that
no clock-equivalent first-crossing table of grid at most `n-1` exists is
also exact: such a table would have `V_m>=A` at its displayed endpoint
`m<n`, whereas this clock has `V_m=c_m<A` there.

## 5. Six-slot specialization

At `n=6`, `beta=A/10` gives `alpha=A/5` and

\[
 (c_0,\ldots,c_6)={A\over10}(0,1,3,5,7,9,10).
\]

The three complementary equalities are literal, size five is the unique
maximizer, and

\[
 V_m={A\over10}\left(2m-\left\lceil{m\over5}\right\rceil\right).
\]

Writing `m=5q+r` gives the five residues

\[
 9q,\quad9q+1,\quad9q+3,\quad9q+5,\quad9q+7
\]

in units `A/10`, precisely the train displayed in the theorem.  The
general Beatty rewrite follows from the integer identity

\[
 2m-\lceil m/h\rceil
 =\left\lfloor{(2h-1)m\over h}\right\rfloor.
\]

## 6. Scope

The theorem proves that first-crossing deletion, endpoint saturation,
dominated-generator deletion, and formal Apéry recursion do not alone
force a smaller first-crossing grid.  It does not assert that the affine
family is extremal, minimal among nonpositive tables, or nonpositive at
all.  The identified missing object is an analytic subthreshold-carry
sign theorem, not another structural deletion.
