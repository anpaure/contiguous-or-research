# Prime-period Apéry variance and complete formal Rayleigh positivity

**Date:** 2026-08-05  
**Method:** pure mathematics; sublevel sumsets, quantile majorization, and
the exact phase-moment gate; no computation, search, or solver  
**Status:** unconditional.  Every formal Apéry clock of prime true residue
period has strictly positive Rayleigh phase functional.  More generally,
the same conclusion holds whenever all relevant defect-sublevel sumsets
have Cauchy--Davenport growth.  Thus the only surviving formal-clock
obstruction has composite period and a nontrivial Kneser stabilizer in a
critical sublevel sumset.  Finite shoulders remain separate.

## 1. Sublevel balls and sorted defect quantiles

Let

\[
 e:\mathbb Z/g\mathbb Z\longrightarrow[0,\infty),
 \qquad e_0=0,
\]

be the normalized Apéry defect.  It is cyclically subadditive,

\[
 e_{r+t}\le e_r+e_t,
\tag{1.1}
\]

and physical nonnegativity of the shift table gives

\[
 e_r\le r
 \qquad(0\le r<g).
\tag{1.2}
\]

For `t>=0`, define the sublevel ball

\[
 B_t=\{r:e_r\le t\}.
\tag{1.3}
\]

Subadditivity gives the exact sumset inclusion

\[
 \boxed{B_s+B_t\subseteq B_{s+t}.}
\tag{1.4}
\]

Let

\[
 0=q_0\le q_1\le\cdots\le q_{g-1}
\tag{1.5}
\]

be the defect values in nondecreasing order, with multiplicity.  Their
mean and variance equal those of the residue profile `e`.

## 2. Cauchy--Davenport growth makes the quantiles subadditive

Assume the following growth condition:

\[
 \boxed{
 |B_s+B_t|
 \ge\min\{g,|B_s|+|B_t|-1\}
 \qquad(s,t\ge0).}
\tag{2.1}
\]

### Lemma 2.1

Under (2.1), the sorted quantiles are subadditive on their index interval:

\[
 \boxed{
 q_{i+j}\le q_i+q_j
 \qquad(0\le i,j,\ i+j<g).}
\tag{2.2}
\]

They also satisfy

\[
 \boxed{q_j\le j.}
\tag{2.3}
\]

#### Proof

The balls `B_(q_i)` and `B_(q_j)` contain at least `i+1` and `j+1`
elements.  Equations (1.4) and (2.1) imply that `B_(q_i+q_j)` contains at
least `i+j+1` elements.  Hence its `(i+j)`-th ordered value is at most
`q_i+q_j`, proving (2.2).

For (2.3), the residues `0,1,...,j` all have defect at most `j` by (1.2).
Thus at least `j+1` defect values are at most `j`. \(\square\)

When `g` is prime, (2.1) is exactly the Cauchy--Davenport theorem.  Hence
every prime-period Apéry profile satisfies Lemma 2.1.

## 3. A sharp majorization theorem for subadditive quantiles

### Theorem 3.1

Let

\[
 0=q_0\le q_1\le\cdots\le q_N
\]

be nonnegative, subadditive in the sense `q_(i+j)<=q_i+q_j`, and satisfy
`q_j<=j`.  Put

\[
 \mu={1\over N+1}\sum_{j=0}^Nq_j.
\]

Then

\[
 \boxed{
 \operatorname {Var}(q)
 \le {\mu(\mu+1)\over3}.}
\tag{3.1}
\]

#### Proof

Let

\[
 S_n=\sum_{j=0}^nq_j.
\]

For every `0<=j<=n`, subadditivity gives

\[
 q_n\le q_j+q_{n-j}.
\]

Summing over `j` yields

\[
 (n+1)q_n\le2S_n.
\tag{3.2}
\]

Since `q_n=S_n-S_(n-1)`, equation (3.2) is equivalent, for `n>=2`, to

\[
 {S_n\over n(n+1)}
 \le {S_{n-1}\over(n-1)n}.
\tag{3.3}
\]

Thus the displayed ratio is nonincreasing.  At `n=N`,

\[
 S_N=(N+1)\mu,
\]

so, for every `n`,

\[
 \boxed{
 S_n\ge {\mu n(n+1)\over N}.}
\tag{3.4}
\]

Define the linear reference sequence

\[
 \ell_j={2\mu j\over N}.
\tag{3.5}
\]

It has the same total sum as `q`, and its prefix sums are exactly the
right side of (3.4).  Since both sequences are nondecreasing, (3.4) says
that `q` is majorized by `ell`.  Convexity of the square gives

\[
 {1\over N+1}\sum_{j=0}^Nq_j^2
 \le {1\over N+1}\sum_{j=0}^N\ell_j^2
 ={4\mu^2\over3}+{2\mu^2\over3N}.
\tag{3.6}
\]

Finally, `q_j<=j` gives `mu<=N/2`.  Therefore

\[
 {2\mu^2\over3N}\le{\mu\over3}.
\]

Subtracting `mu^2` from (3.6) proves (3.1). \(\square\)

The directed-cycle quantiles `q_j=j` attain equality throughout.  Thus
both the coefficient and the lattice correction in (3.1) are sharp.

## 4. Complete prime-period formal positivity

### Theorem 4.1

Let a formal Apéry clock have true prime residue period `g` and fundamental
endpoint period

\[
 0<P\le\zeta.
\]

Then its complete Rayleigh phase functional is strictly positive.

#### Proof

Cauchy--Davenport gives (2.1).  Lemma 2.1 and Theorem 3.1 therefore give

\[
 \operatorname {Var}(e)
 \le {\overline e(\overline e+1)\over3}.
\]

The exact general Apéry phase-moment theorem then shows that the positive
zeroth Fourier mode strictly dominates all nonzero modes.  Hence the
formal phase functional is positive. \(\square\)

The same proof works verbatim for composite `g` whenever (2.1) holds for
the relevant sublevel balls.

## 5. Exact composite-period obstruction

Kneser's theorem says that failure of (2.1) can occur only when a sumset

\[
 B_s+B_t
\]

has a nontrivial stabilizer subgroup `H`.  Therefore every formal profile
not covered by Theorem 4.1 has all of the following properties:

1. its true period is composite;
2. some critical defect-sublevel sumset is a union of nontrivial
   `H`-cosets;
3. the sorted defect quantiles can fail ordinary subadditivity only across
   that periodic coset obstruction.

This is sharper than “genuinely multi-kink”: arbitrary multi-kink profiles
of prime period are already closed.  The remaining finite theorem should
be a coset variance induction.  One must combine the within-`H` metric and
the quotient metric without increasing

\[
 \operatorname {Var}(e)-{\overline e(\overline e+1)\over3}.
\]

The cheap-subgroup calibration, where the defect law is a sum of a
within-coset ramp and a quotient ramp, satisfies the bound with room; a
general coset-gluing theorem is not proved here.

## 6. Scope

The theorem closes the complete **formal periodic** Rayleigh functional at
every prime true residue period.  It does not control the finite
availability shoulder, whose counting queue is nonperiodic.  Nor does it
yet prove the coset variance induction for every composite period.

## 7. Dependencies

1. `MATH_THEOREM_RAYLEIGH_GENERAL_APERY_PHASE_MOMENTS_AND_VARIANCE_GATE_20260805.md`;
2. the Cauchy--Davenport theorem for `Z/pZ`;
3. Kneser's theorem for the structural boundary statement.
