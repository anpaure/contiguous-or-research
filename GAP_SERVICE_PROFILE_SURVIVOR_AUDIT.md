# Audit and closure of the proposed gap-service survivor

## 1. Verdict

The marked process in `GAP_SERVICE_PROFILE_SURVIVOR.md` is a genuine
survivor of the scalar gap, full-line, contraction, and absorbed-lifetime
ledgers, but it is **not** a survivor of the inherited heterogeneous
internal-run cover.

Its finite word has a direct bounded-congestion assignment with

\[
 Q\le {7\over2}a^3+O(a^2)<(4-o(1))a^3.                 \tag{1.1}
\]

Thus it contradicts the capped-run lower bound whenever the product-word
defect is `o(a^2)`.  The scalar value `389/84` arose only because each
contracted gap was replaced by one number and its visible cost-`a`
separator was not allowed to serve starts in the neighbouring blocks.

This audit was obtained independently twice and checked on finite instances
by `scratch/verify_gap_service_survivor.py`.

## 2. Finite record order

Up to `O(a)` boundary, diagonal, and breaker positions, the word has two
components made of records

\[
                  L_j\;S_j\;G_j\;L_{j+1}.           \tag{2.1}
\]

Here:

* `L_j` is a low directed peak plateau, with edge cost
  `lambda_j` between `a+O(1)` and `2a+O(1)`;
* `S_j` is the reflected high plateau, with edge cost `a+O(1)`;
* `G_j` is a block of unused negative-negative points, of size
  `a/2+O(1)`.

The two components exchange `x` and `y`.  Their aggregate sizes are

\[
 \sum_j\lambda(L_j)={3\over2}a^2+O(a),\qquad
 \sum_j|G_j|={1\over2}a^2+O(a),                     \tag{2.2}
\]

and there are `a+O(1)` separator blocks, each with `a+O(1)` positions.

The orientations can be chosen so that every displayed `L_j` and `S_j` is
a maximal internal peak plateau.  For example, reverse a low `x=t` fibre
so it ends at `y=-a`, and follow it by its opposite high `y`-fibre.  Both
neighbours of the latter have smaller `y`, making `S_j` an internal
threshold run.  The preceding desert and following opposite separator have
`x<0<t`, making `L_j` an internal `x`-peak.  Shared endpoints and component
ends affect only `O(a)` positions.

## 3. Service assignment

For every ordinary record, make the following assignments.

1. Every start in `L_j`, except a possible endpoint shared with `S_j`, is
   sent forward to the run `S_j`.
2. Every start in `G_j` is sent backward to `S_j`.
3. Every start in `S_j` is sent forward to `L_(j+1)`.

Every chosen run avoids its assigned start.  The respective one-sided spans
are at most

\[
 3a+O(1),\qquad {3\over2}a+O(1),\qquad
 {7\over2}a+O(1),                                  \tag{3.1}
\]

all below the universal `4a+3` span.  Each run receives only `O(a)` starts,
so both endpoint-congestion constants are `O(a)`.  Leave the `O(a)`
component-end and breaker starts unassigned; their capped penalty is only
`O(a^2)`.

## 4. Cost

Starts in the long blocks and desert blocks pay `a+O(1)`.  Separator starts
have `a+O(1)` positions per separator and pay the cost of the next long
block.  Consequently

\[
\begin{aligned}
 Q
 &\le (a+O(1))\left(\sum_j\lambda(L_j)+\sum_j|G_j|\right)
      +\sum_j(a+O(1))\lambda(L_{j+1})+O(a^2)\\
 &=a\left({3\over2}a^2+{1\over2}a^2\right)
      +a\left({3\over2}a^2\right)+O(a^2)\\
 &={7\over2}a^3+O(a^2).                            \tag{4.1}
\end{aligned}
\]

The fan-capped run-spectrum theorem requires

\[
 Q\ge(4-o(1))a^3                                    \tag{4.2}
\]

under `D=o(a^2)`.  Equations (4.1)--(4.2) are incompatible.

Relative to the scalar survivor's bound, the service assignment saves

\[
 {389\over84}-{7\over2}={95\over84},                \tag{4.3}
\]

which is substantially more than the required `53/84` margin.

## 5. Scope

This closes the particular coherent multiscale survivor; it does not yet
prove the arbitrary-order three-box run-cover theorem.  The correct lesson
is nevertheless stronger than the former “unknown service profile” status:
visible subcritical separator plateaux may serve both the preceding long
block and the following desert, while the next long block serves the
separator.  Any future scalar counterprofile must survive this cyclic
three-block service operation, not merely the pointwise seam functional.

