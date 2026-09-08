# All-grid Bellman minimal counterexamples: Apéry descent trichotomy and finite shoulder correction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It gives an exact
minimal-counterexample induction step.  Every lower-critical branch either
produces a genuinely smaller first-crossing clock plus a finite,
quantitatively bounded correction, or is a subthreshold periodic
no-descent carry gate.  The remaining endpoint-critical branch is forced
onto the threshold face.  The theorem does not prove universal Bellman
positivity.

Put

\[
                         A={\sqrt\pi\over2}
\]

and let `K` be the Rayleigh signed-tail kernel.  Assume a nonpositive
finite Bellman table exists.  Choose one with minimum first-crossing grid
size `n`, and apply endpoint saturation.  Thus

\[
 c_j<A\quad(1\le j<n),\qquad c_n\ge A,
\tag{0.1}
\]

the table is internally superadditive, and its Bellman functional is still
nonpositive.  Complete positivity through grid five implies `n>=6`.

Let `V` be its Bellman clock.  Put

\[
 \lambda=\max_{1\le j\le n}{c_j\over j},qquad
 h=\min\operatorname*{argmax}_{1\le j\le n}{c_j\over j}.
\tag{0.2}
\]

Let `S` be the complete critical set, let `g=gcd(S)`, and let
`beta_r`, `0<=r<g`, be the maximum reduced residue weights.  Define

\[
 P=g\lambda,qquad s_r=r\lambda+\beta_r,qquad
 W_{qg+r}=qP+s_r.
\tag{0.3}
\]

The cyclic Apéry theorem says that `W` is the exact Bellman clock of the
honest internally superadditive table

\[
                         (0,s_1,\ldots,s_{g-1},P).
\tag{0.4}
\]

Here `g` need not itself be an original critical denomination.  The cited
cyclic proof still applies verbatim: every original critical denomination
is a zero-reduced-weight loop modulo `g`, concatenation of residue walks
gives the cyclic superadditivity inequalities for the `s_r`, and the
formal size-`g` generator of value `P=g\lambda` then has the exact clock
`W_(qg+r)=qP+s_r`.

## 1. Exact domination and finite correction

### Proposition 1.1

For every `m>=0`,

\[
                         \boxed{V_m\le W_m.}
\tag{1.1}
\]

Moreover,

\[
                         V_m=W_m\qquad(m\ge T),
 \qquad T:=n(n-1).
\tag{1.2}
\]

Consequently

\[
\boxed{
 \Phi(V)=\Phi(W)+\mathcal H(V,W),
 \qquad
 \mathcal H(V,W)=
 \sum_{m=0}^{T-1}\bigl(K(V_m)-K(W_m)\bigr).
}
\tag{1.3}
\]

#### Proof

Every exact-fill configuration of capacity `m` is a residue walk from
zero to `m mod g`.  After subtracting `lambda` times its capacity, its
reduced weight is at most `beta_(m mod g)`.  This proves (1.1).
The all-slot Apéry conductor theorem gives equality once
`m>=n(n-1)`, proving (1.2) and then (1.3). \(\square\)

Thus the formal periodic clock is an upper envelope of the physical
clock, but no denomination-deletion monotonicity is asserted.  All failure
of literal Apéry replacement is priced by the finite correction
`mathcal H`.

## 2. The unique compact shoulder

There is a unique number `zeta in (0,A)` at which `K` attains its global
minimum.  The kernel is strictly decreasing on `[0,zeta]` and strictly
increasing on `[zeta,infinity)`.

Indeed, for `0<t<1`, put

\[
 D(t)={K'(At)\over2A}
 =h_0(1+t)-h_0(1-t),qquad
 h_0(u)=u e^{-\pi u^2/4}.
\]

The sign of `-D(t)` is the sign of

\[
 f(t)=\pi t-2\operatorname{arctanh}t.
\]

Here `f(0)=0`, `f'(0)=pi-2>0`,

\[
 f''(t)=-{4t\over(1-t^2)^2}<0,
\]

and `f(t)` tends to minus infinity as `t` tends to one.  Hence `f` has
exactly one zero in `(0,1)`.  Beyond `A`, the explicit Gaussian tail has
positive derivative.  This proves the assertion about `zeta`.

Define the finite adverse-shoulder index set

\[
                         \mathcal D
 =\{0\le m<T:W_m>\zeta\}.
\tag{2.1}
\]

### Proposition 2.1 (quantitative correction bound)

One has

\[
 \boxed{
 \mathcal H(V,W)
 \ge\sum_{m\in\mathcal D}
       \bigl(K(V_m)-K(W_m)\bigr)
 \ge |\mathcal D|K(\zeta).
 }
\tag{2.2}
\]

In particular, if `Phi(W)>0` while `Phi(V)<=0`, then

\[
 \boxed{
 |\mathcal D|\ge {\Phi(W)\over-K(\zeta)}.
 }
\tag{2.3}

#### Proof

If `W_m<=zeta`, then `0<=V_m<=W_m` and monotone decrease gives

\[
                         K(V_m)-K(W_m)\ge0.
\]

Dropping these nonnegative terms proves the first inequality in (2.2).
Since `zeta` is the global minimizer, `K(V_m)>=K(zeta)`.  Also
`K(W_m)<0` whenever `W_m>zeta`; after its minimum the compact kernel stays
negative and the Gaussian tail approaches zero from below.  Thus every
remaining difference is at least `K(zeta)`, proving the second inequality.
Finally (1.3), `Phi(V)<=0`, and `Phi(W)>0` imply (2.3). \(\square\)

This is the promised quantitative boundary correction.  A positive
smaller Apéry clock can only be overturned by finitely many literal
availability cells lying after the formal clock enters the increasing
compact shoulder.  Aggregate denomination deletion outside this statement
is not used.

## 3. The descent trichotomy

Let

\[
                         N=\min\{m>=1:W_m\ge A\}
\tag{3.1}
\]

be the first threshold crossing of the formal Apéry clock.

### Theorem 3.1 (minimal-counterexample trichotomy)

Exactly one of the following holds.

### A. Endpoint-critical threshold branch

If `h=n`, endpoint saturation forces

\[
                         \boxed{c_n=A.}
\tag{3.2}

This is the genuine threshold-critical branch.  It is not eliminated by
the present induction.

### B. Strict Apéry descent

If `h<n` and `N<n`, the prefix

\[
                         (W_0,W_1,\ldots,W_N)
\tag{3.3}

is an internally superadditive first-crossing table of grid `N`, and its
Bellman clock is exactly `W`.  Minimality of `n` therefore gives

\[
                         \boxed{\Phi(W)>0.}
\tag{3.4}

Consequently a nonpositive original table must satisfy the explicit
finite obstruction

\[
 \mathcal H(V,W)\le-\Phi(W)<0,
\tag{3.5}

and hence the shoulder bound (2.3).  If every correction cell lies before
`W` reaches `zeta`, this branch is impossible.

### C. Subthreshold no-descent carry branch

If `h<n` and `N=n`, then

\[
                         \boxed{P<A,}
\tag{3.6}

and the smaller displayed Apéry table (0.4) obeys the exact carry system

\[
 qP+s_r<A\quad(qg+r<n),
 \qquad
 q_0P+s_{r_0}\ge A
 \quad(n=q_0g+r_0).
\tag{3.7}

Thus first-crossing extension of the smaller periodic table returns the
same grid size `n`.  This is the only lower-critical way in which grid
descent can fail.  If `Phi(W)<=0`, the pure periodic extension is itself a
minimal-grid counterexample.  If `Phi(W)>0`, the original table again
requires the finite negative shoulder correction (3.5).

#### Proof

If `h=n`, the least-critical endpoint normalization gives (3.2).

Suppose `h<n`.  Since `g<=h` and `h` is critical,

\[
 P=g\lambda\le h\lambda=c_h<A,
\]

which proves (3.6).  Proposition 1.1 gives `W_n>=V_n=c_n>=A`, so
`N<=n`.

The clock `W` is superadditive.  Adjoining its values through its first
crossing therefore gives the internally superadditive table (3.3).
Moreover `P<A` and `s_r<P` for `0<r<g`, so `W_m<A` for
`1<=m<=g`; hence `N>g` and that prefix contains all generators (0.4).
Because superadditivity
prevents any newly adjoined denomination from improving a Bellman value,
its clock remains exactly `W`.  If `N<n`, minimality proves (3.4), and
(3.5) follows from (1.3).  If `N=n`, the definition of `N` is exactly
(3.7).  These cases are exhaustive. \(\square\)

## 4. Inductive meaning and exact scope

The theorem reduces an all-grid Bellman proof to three explicit tasks:

1. prove positivity on the endpoint-critical threshold branch;
2. prove positivity of the subthreshold cyclic carry gates (3.6)--(3.7),
   or classify the nonpositive ones;
3. in strict-descent branches, prove that the finite shoulder correction
   cannot outweigh the positive smaller-clock margin.

The affine setup-cost family is an exact instance of branch C: its
subthreshold Apéry table first crosses only when the original endpoint is
restored.  Its existence shows why a theorem claiming unconditional grid
descent would be false.

This result is an exact reduction, not an elimination of any one of the
three branches.  It does not prove positivity beyond the known finite
grids, does not assume denomination-deletion monotonicity, and has no
implication for the separate common-cap/router problem or for an OR-word
upper bound.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| all-grid first crossing, saturation, and Apéry conductor | `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md` | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| cyclic Apéry table and exact formal clock | `MATH_THEOREM_APERY_SHIFT_CYCLIC_SUPERADDITIVITY_AND_TAIL_RECURSION_20260804.md` | `324f040f5604767fc867c78806c8a7ab7524d6ed82cabe77bc3e2e0ea36121ba` |
| least-critical endpoint normalization | `MATH_THEOREM_LEAST_CRITICAL_ENDPOINT_THRESHOLD_NORMALIZATION_20260804.md` | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |
| complete positivity through grid five | `MATH_THEOREM_FIVE_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `69d8d73e52342a74d11a8673811e0d41d15063a2d66d1fdbc504138b4ed76bed` |
| affine no-descent obstruction | `MATH_THEOREM_AFFINE_SETUP_COST_FIRST_CROSSING_AND_APERY_NO_DESCENT_20260804.md` | `408aacd10f2e20bf26364f6464d06a7d0fb9c4d179e93e21b8a26482ce7405ce` |
