# Standard-output Fisher scale is exponentially impossible at depth two

**Date:** 2026-08-22

**Status:** unconditional normalization obstruction and exact orbit-sum
reduction.  It does not settle the dimensionless compensated-angle gate.

## 1. Setup

Fix `r>=4`, put

\[
 b=2r+1,\qquad k=r-2,\qquad N={b\choose k},\qquad p={b\over N}.
                                                               \tag{1.1}
\]

Let `G=S_b` with the uniform probability law.  For `g in G`, let
`D_k(g)` be the `b` distinct cyclic `k`-windows of the word
`(g(0),...,g(b-1))`, and put

\[
 q_T(g)=\mathbf1_{\{T\in D_k(g)\}},
 \qquad T\in{[b]\choose k}.                         \tag{1.2}
\]

A tangent to the uniform configuration law has the form

\[
                         \delta_g={f(g)\over b!},              \tag{1.3}
\]

and its Fisher norm and relative coordinate norm are

\[
 \|\delta\|_{\rm F}^2={1\over b!}\sum_g f(g)^2
       =\mathbb E f^2,
 \qquad
 \left\|{\delta\over\lambda^0}\right\|_\infty=\|f\|_\infty.
                                                               \tag{1.4}
\]

The unconstrained shallow-current operator is

\[
 (Sf)_T=\mathbb E[f(g)q_T(g)].                     \tag{1.5}
\]

Every target has uniform marginal `p`.  The standard Euclidean current is
`Sf`; its relative-density version is

\[
                         \widehat S f=p^{-1}Sf.                 \tag{1.6}
\]

The distinction between (1.5) and (1.6) is exponentially large and cannot
be suppressed in an asymptotic Gate-B statement.

## 2. Exact shallow orbit eigenvalues

Let

\[
 \mathbb R^{{[b]\choose k}}
   =\bigoplus_{j=0}^{k}V_{(b-j,j)},
 \qquad
 d_j=\dim V_{(b-j,j)}={b\choose j}-{b\choose{j-1}}.             \tag{2.1}
\]

This is the standard multiplicity-free subset decomposition.  One
self-contained construction takes the nested images of the inclusion maps
from `j`-sets to `k`-sets.  The new quotient at level `j` has the displayed
dimension, and the column-antisymmetrized subset differences give the
two-row irreducible.  The dimensions telescope to `{b choose k}`.

Put

\[
 n_h={k\choose h}{b-k\choose k-h},
 \qquad
 w_h=\begin{cases}
 b-2k+1=6,&h=0,\\
 2,&1\le h\le k-1,\\
 1,&h=k.
 \end{cases}                                                   \tag{2.2}
\]

With the convention that an out-of-range binomial coefficient is zero,
define

\[
 E_j(h)=\sum_{a=0}^{j}(-1)^{j-a}{j\choose a}
       {k-j\choose h-a}
       {b-k-j\choose k-j-h+a}.                    \tag{2.3}
\]

### Theorem 2.1 (closed orbit-sum formula)

The squared Fisher singular value of `S` on `V_(b-j,j)` is

\[
 \boxed{
 \theta_{r,j}={b\over N}
       \sum_{h=0}^{k}{w_hE_j(h)\over n_h}.}         \tag{2.4}
\]

In particular `theta_(r,j)>=0`, and

\[
 \boxed{\sum_{j=0}^{k}d_j\theta_{r,j}=b.}          \tag{2.5}
\]

#### Proof

The kernel of `SS^*` is

\[
                         K_{TU}=\mathbb E[q_Tq_U].             \tag{2.6}
\]

It depends only on `h=|T cap U|`.  In one cyclic `k`-deck, the number of
ordered window pairs is `b` at overlap `k`, `2b` at every overlap
`1,...,k-1`, and

\[
 b^2-b-2b(k-1)=b(b-2k+1)=6b                  \tag{2.7}
\]

at overlap zero.  There are `N n_h` ordered pairs of target `k`-sets with
overlap `h`.  Uniform relabeling therefore gives

\[
                         K_{TU}={bw_h\over Nn_h}.               \tag{2.8}
\]

For an elementary eigenvector of level `j`, choose disjoint coordinate
pairs `(a_i,b_i)`, `1<=i<=j`, and set

\[
 F_j(X)=\prod_{i=1}^{j}
       (\mathbf1_{\{a_i\in X\}}-\mathbf1_{\{b_i\in X\}}).     \tag{2.9}
\]

It is the `k`-set lift of the harmonic signed `j`-set function which
chooses exactly one member of every pair.  Every down-sum cancels its two
possible choices, so (2.9) lies in `V_(b-j,j)`.

Choose `T` containing every `a_i`, no `b_i`, and `k-j` further labels.
Then `F_j(T)=1`.  Among the `U` with `|T cap U|=h`, a nonzero term chooses
`a` of the `a_i`, the other `j-a` choices being the `b_i`, with sign
`(-1)^(j-a)`.  It then chooses `h-a` of the `k-j` remaining labels of `T`
and `k-j-h+a` labels outside `T` and outside the pairs.  Hence

\[
                  \sum_{U:|T\cap U|=h}F_j(U)=E_j(h).           \tag{2.10}
\]

Equations (2.8)--(2.10) prove (2.4).  Positivity follows independently
from `K=SS^*`.  Finally

\[
 \operatorname {tr}K
   =\sum_T\mathbb E q_T
   =\mathbb E|D_k(g)|=b.                         \tag{2.11}
\]

The multiplicity of `theta_(r,j)` is `d_j`, proving (2.5). `square`

For calibration, (2.4) gives the relative-density squared singular values
`Theta_(r,j)=theta_(r,j)/p^2`

\[
 \Theta_{4,2}=4,qquad
 \Theta_{5,2}={180\over7},qquad
 \Theta_{5,3}={75\over7}.                         \tag{2.12}
\]

These are unconstrained values.  They do not assert exposure compensation.

## 3. Exponential obstruction in the standard output norm

### Theorem 3.1

Let `j=k=r-2`.  If a tangent `delta=lambda^0 f` produces a standard
Euclidean unit current in `V_(r+3,r-2)`, then, even without imposing any
central or exposure constraint,

\[
 \boxed{
 \|\delta\|_{\rm F}\ge
 \sqrt{\frac{6{2r+1\choose r-2}}{(r+4)(2r+1)}}.}               \tag{3.1}
\]

The same lower bound holds for `||delta/lambda^0||_infty`.  In particular
both lower bounds are exponential in `r`.

#### Proof

All terms in (2.5) are nonnegative, so

\[
                         \theta_{r,k}\le {b\over d_k}.         \tag{3.2}
\]

Here

\[
 d_k={b\choose k}-{b\choose{k-1}}
     ={6\over r+4}{2r+1\choose r-2}.             \tag{3.3}
\]

On the `k`-th irreducible, `SS^*=theta_(r,k)I`.  Thus the least possible
Fisher norm of a preimage of a unit current is
`theta_(r,k)^(-1/2)`, which is at least `sqrt(d_k/b)` by (3.2).  Restricting
the input to a compensated kernel cannot decrease this minimum.  Also
`||f||_infty>=||f||_(L^2)`, proving the relative-coordinate assertion.

For an explicit exponential estimate, the maximal-binomial bound and

\[
 {2r+1\choose r-2}
 ={2r+1\choose r}{r(r-1)\over(r+2)(r+3)}
 \ge {2^{2r+1}\over7(r+1)}                       \tag{3.4}
\]

for `r>=4` make (3.1) exponential. `square`

### Consequence

No all-module theorem can give a polynomial Fisher-norm or polynomial
relative-`l_infinity` right inverse for **unit standard Euclidean shallow
currents**.  This failure occurs before central balance, exposure balance,
stopping, or punctured-residual asymmetry enters.  Consequently an absolute
condition of the form

\[
                  \text{standard-output Fisher singular value}
                  \ge r^{-C}                                  \tag{3.5}
\]

is impossible through the whole depth-two band.

## 4. The corrected dimensionless compensated gate

Let `m_(k,lambda)` be the actual isometrically scaled shallow multiplicity
vector, and let `M_(B,lambda)` be the span of the four central/exposure
multiplicity vectors.  Put

\[
 \eta_{r,j}=\|\operatorname {proj}_{M_{B,\lambda}^{\perp}}m\|^2,
 \qquad
 \alpha_{r,j}={\eta_{r,j}\over\|m\|^2}\in[0,1],
 \qquad \lambda=(b-j,j).                         \tag{4.1}
\]

Since `||m||^2/b!=theta_(r,j)`, the compensated squared Fisher singular
value is exactly

\[
                         {\eta_{r,j}\over b!}
                         =\alpha_{r,j}\theta_{r,j}.            \tag{4.2}
\]

For the relative-density output (1.6), it is

\[
 \boxed{
 \widehat\sigma_{r,j}^2
   =\alpha_{r,j}\Theta_{r,j},
 \qquad
 \Theta_{r,j}=\left({N\over b}\right)^2\theta_{r,j},}        \tag{4.3}
\]

where `Theta` is given explicitly by (2.4).  Thus the first genuinely open
scalar is the dimensionless angle `alpha`, not the exponentially scaled
absolute quantity in (3.5).

If the four constraint vectors are independent and `G_B` is their Gram
matrix, while `G_5` is the Gram matrix after appending `m`, then

\[
 \boxed{
 \alpha_{r,j}={\det G_5\over\|m\|^2\det G_B}.}                 \tag{4.4}
\]

With dependent constraint vectors, the equivalent definition (4.1), or
the Moore--Penrose Schur complement, applies.  Formula (4.4) includes the
duplicate-exposure directions; no independence or regenerated-state
approximation has been made.

A viable complete-catalogue theorem must therefore do both of the following:

1. prove a polynomial lower bound for
   `alpha_(r,j) Theta_(r,j)` in the chosen relative-current norm; and
2. construct the simultaneous inverse with a polynomial relative
   `l_infinity` bound.

The exact `r=4,5` rank certificates prove only `alpha_(r,j)>0` on their
tested modules.  They do not bound (4.4) as `r` grows.  Stability of the
corresponding restricted operator in the stopped nonsymmetric residual
remains a further Gate-B input.

## 5. Verifier

Run

```text
python3 scratch/verify_depth_two_fisher_scale_obstruction_20260822.py
```

The standard-library checker verifies the cyclic overlap counts, evaluates
(2.4) in exact rational arithmetic, independently applies the full kernel
to the harmonic eigenvectors at `r=4,5`, checks the trace identity through
`r=35`, and audits (3.3)--(3.4) and the calibration values (2.12).
