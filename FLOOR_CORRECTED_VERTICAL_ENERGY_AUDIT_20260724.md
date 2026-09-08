# Audit: floor-corrected vertical energy and common-owner flags

## Verdict

The four submitted results are mathematically valid in their stated
conditional scope.  In particular, the floor subtraction, every coefficient
in the hole decomposition, the integral common-owner flag construction, the
owner-mismatch charge, and the constants in the heat-bath descent all check
out.  The heat-bath hypothesis is only a sufficient condition; this audit
does not establish its component-variance inequality.

There are three minor presentation corrections:

1. the lower-bounded-flow proof should explicitly add a source, sink, and a
   return arc (or state the equivalent integral `b`-flow theorem);
2. the example tail depth should be typeset unambiguously as
   `H=ceil(sqrt(m) log log m)` (more generally `H/sqrt(m)->infinity` and
   `H=o(m)`);
3. equation (36) contains rendering artifacts: its first term is the squared
   Euclidean norm and its last term is `||Delta_{K,q}||_2^2`.

None changes a theorem.

## 1. Integer-floor identity and transfer coefficients

For `T=aN+b`, direct expansion gives

```text
sum_i (c_i-T/N)^2 - b(N-b)/N
 = sum_i c_i^2-a^2 N-(2a+1)b
 = sum_i (c_i-a)(c_i-a-1).
```

Every summand on the right is nonnegative because the two factors are
consecutive integers.  Its values are exactly

```text
c_i=0:       a(a+1),
1<=c_i<a:    (a-c_i)(a+1-c_i),
c_i=a,a+1:  0,
c_i>=a+2:   (c_i-a)(c_i-a-1).
```

Thus the displayed decomposition (4), including the hole coefficient
`a_q(a_q+1)`, is exact.  Since `N_q<=W` for the relevant lower ranks,
`a_q>=1`, so division by this coefficient is legitimate.  Summing gives

```text
sum_{q<=H} M_q <= sum_{q<=H} Phi_q/[a_q(a_q+1)].
```

Substitution into the established wreath word contributes twice this
quantity, exactly as in (8) and (9).  The symmetric-chain-product tail is
`o(W)` under `H/sqrt(m)->infinity`, `H=o(m)`; the proposed
`H=ceil(sqrt(m) log log m)` satisfies this.  The seam is also `o(W)`.

At depth one, `W/N_1=(m+2)/m`, hence `a_1=1` for `m>=3`, and the identity
reduces to

```text
Phi_1=2M_1+sum_{t>=3}(t-1)(t-2)n_{1,t}.
```

Also `b_1=W-N_1=2W/(m+2)`.  For `m=4`, the balanced histogram is
`1^42 2^42`, and its unavoidable raw squared discrepancy is
`42*42/84=21`, as claimed.

## 2. Integral nested common-owner flags

The fractional flow is correct.  A depth-`q` set receives
`lambda_q=W/N_q`; after equal facet splitting, a depth-`q+1` set receives

```text
lambda_q (m+q+2)/(m-q)=W/N_{q+1}.
```

This lies in `[a_q,a_q+1]` at every split vertex.

For a fully explicit integral formulation, add vertices `sigma,t`, arcs

```text
sigma -> X^in             capacity [1,1]       (|X|=m),
S^out -> t                capacity [0,W]       (|S|=m-H),
t -> sigma                capacity [W,W],
```

as well as the submitted internal and facet arcs.  The uniform fractional
flow is a feasible circulation.  All bounds are integral and the directed
node-arc incidence matrix is totally unimodular, so an integral circulation
exists.  Delete the return arc.  The remaining graph is layered and acyclic,
and its integral `sigma`-to-`t` flow decomposes into `W` unit paths.  Because
each top arc has flow one, there is exactly one path indexed by each middle
set `X`.  Its layer vertices form the required nested deletion chain.

At layer `q`, every integral throughput is `a_q` or `a_q+1`.  Total
throughput is `W=a_qN_q+b_q`, so exactly `b_q` vertices have the upper value.
This proves all four assertions of Theorem 2, including common ownership.
It proves a lower-flag table, not cyclic realizability of that table.

## 3. Owner-mismatch charging

If `S` is an actual depth-`q` hole, all owners in the target fibre
`{X:L_q(X)=S}` are mismatches.  That fibre has size at least `a_q`, and
fibres of distinct targets are disjoint.  Therefore

```text
a_q M_q <= R_q,
```

which gives (22)--(24) with no missing factor.  The estimate uses only
`a_q>=1`; it does not assume independence between depths.

The asymptotic load formula is also correct:

```text
lambda_q=product_{i=0}^{q-1}(m+2+i)/(m-i),
log lambda_q=q(q+1)/m+O(q^3/m^2+q/m).
```

The stated error is uniform and is `o(1)` for `q=o(m^(2/3))`.  In the
coarse comparison used afterward, `a_q` and `lambda_q` are within absolute
constant factors because `lambda_q>=1` and `floor(lambda_q)>=lambda_q/2`.

## 4. Heat-bath spectrum and descent constants

For rank `r=m-q`, every wreath order contributes exactly `r` intervals
containing a fixed coordinate.  With `B=W/n`,

```text
sum_{S containing x} mu_q(S)=rB
 =lambda_q binom(n-1,r-1).
```

Thus `f_q` has zero total and zero point marginals and lies only in Johnson
modules `U_j`, `j>=2` (for `r=1`, this forces `f_q=0`).

For a uniformly random coordinate transposition, the averaging operator has
eigenvalue

```text
theta_j=1-2j(n-j+1)/(n(n-1))
```

on the module indexed by `(n-j,j)`.  Consequently the squared-norm
smoothing multiplier is `(1+theta_j)/2`.  Since the allowed
`j` satisfy `2<=j<=r<=m`, `j(n-j+1)` is minimized at `j=2`, and

```text
(1+theta_j)/2 <= 1-2/n,
```

with equality at `j=2`.  Equation (37) therefore has the right normalization.

The component covariance trace is exactly

```text
(1/4) sum_K ||Delta_{K,q}||_2^2.
```

After weighting and averaging,

```text
E Q_H(G) <= (1-2/n)Q_H(F)+(1/4)V_H(F).
```

Using (31) gives

```text
E Q_H(G) <= Q_H(F)-epsilon_m E_H(F)+rho_m.
```

Since `Q_H^min` is independent of the factor and
`E_H=Q_H-Q_H^min`, subtraction yields exactly

```text
E E_H(G) <= (1-epsilon_m)E_H(F)+rho_m.
```

If `E_H(F)>rho_m/epsilon_m`, some deterministic transposition/component
choice strictly lowers the energy.  There are finitely many exact factors,
so descent terminates and proves (32).  The new right side differs from the
uncorrected target by

```text
4 epsilon_m Q_H^min+4 rho_m,
```

so the claimed weakening is exact (strict whenever this addition is
positive).

## Scope warning

Theorem 2 does not imply an exact wreath factor realizing its flags, and
Theorem 4 does not prove (31).  Accordingly, the valid conclusion is the
submitted reduction: cyclic alignment or the component-variance estimate
remains the missing construction theorem, and the coefficient-one bound is
still conditional.
