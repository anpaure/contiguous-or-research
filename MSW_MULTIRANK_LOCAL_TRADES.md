# Exact multirank action of the local MSW trades

## 1. Outcome

Put

\[
        n=2m+1.
\]

Unless stated otherwise, the first-shadow independence statements below
assume `m>=3`; the degenerate case `m=2` has `m-1=1`, where every trade is
invisible because rank-one interval counts are constant for every order.

The `Cat_(m-2)` two-for-two components found for the transposition
`(2 3)` admit a completely explicit action at **every** rank.  More is
true: the same four-letter component occurs at every top-level Dyck
concatenation boundary.  Altogether this gives

\[
 \sum_{p=0}^{m-2}\operatorname {Cat}_p
                    \operatorname {Cat}_{m-p-2}
       =\operatorname {Cat}_{m-1}                         \tag{1.1}
\]

local support-feasible trades, distributed among different coordinate
transpositions.

Each trade has the following multirank profile.

* It is zero at ranks `1,m,m+1,n-1`.
* At every lower rank `2<=r<=m-2` it has eight distinct entries, all
  coefficients being `+1` or `-1`.
* At rank `m-1` it is one elementary four-set square.
* The upper-rank action is the complementary copy of the lower-rank
  action.

The eight entries do not occur mysteriously.  They lie on four nested
prefix/suffix flags of two MSW flip-coordinate lists.  Thus one local trade
is a four-armed Boolean flag dipole.

There is also a decisive negative conclusion.  The whole family (1.1) is
already linearly independent after projection to rank `m-1`.  Hence

\[
 \boxed{
 B_{m-1}\sum c_{p,P,R}z_{p,P,R}=0
       \quad\Longrightarrow\quad
 c_{p,P,R}=0\text{ for every }(p,P,R).}                \tag{1.2}
\]

So these local components cannot form a Haar absorber which changes deeper
ranks while preserving a completed first shadow.  They are useful as a
sparse final absorber, but a bulk frame or a sequential multirank correction
requires genuinely larger/nonlocal components.

## 2. A universal four-letter identity

Let `alpha,beta,gamma,delta` be four distinct labels and let

\[
              T=(t_0,t_1,\ldots,t_{2m-4})              \tag{2.1}
\]

be an arbitrary ordering of the other `2m-3` labels.  Consider the four
cyclic omitted-label words

\[
\begin{aligned}
 C  &=(\delta,\beta,\gamma,\alpha,T),
 &D  &=(\beta,\alpha,\delta,\gamma,T),\\
 C' &=(\delta,\gamma,\beta,\alpha,T),
 &D' &=(\gamma,\alpha,\delta,\beta,T).
\end{aligned}                                             \tag{2.2}
\]

Thus `C',D'` are obtained from `C,D` by the coordinate transposition
`beta <-> gamma`.  Put

\[
                    z_T=e_{C'}+e_{D'}-e_C-e_D.           \tag{2.3}
\]

For a cyclic word `q`, write

\[
 I_i^{(r)}(q)=\{q_i,q_{i+2},\ldots,q_{i+2r-2}\},
 \qquad
 B_re_q=\sum_{i\in\mathbb Z_n}e_{I_i^{(r)}(q)}.          \tag{2.4}
\]

The step-two convention in (2.4) is the omitted-label representation of
ordinary cyclic intervals in the associated wreath.

Split the common tail into its two parity lists

\[
 \mathsf E=(t_0,t_2,\ldots,t_{2m-4}),
 \qquad
 \mathsf O=(t_1,t_3,\ldots,t_{2m-5}).                    \tag{2.5}
\]

Their lengths are `m-1` and `m-2`, respectively.  For a list `X`, let
`pre_l(X)` and `suf_l(X)` denote the sets of its first and last `l`
entries.  Finally define

\[
       \partial K=e_{K\cup\{\gamma\}}-e_{K\cup\{\beta\}}. \tag{2.6}
\]

### Theorem 1 (exact all-rank action)

For `2<=r<=m-1`, with `l=r-1`,

\[
\boxed{
 B_rz_T={}
   \partial\operatorname{suf}_l(\mathsf O)
  +\partial\operatorname{suf}_l(\mathsf E)
  -\partial\operatorname{pre}_l(\mathsf E)
  -\partial\operatorname{pre}_l(\mathsf O).
}                                                         \tag{2.7}
\]

Moreover,

\[
 B_1z_T=B_mz_T=0,                                        \tag{2.8}
\]

and for every `r`,

\[
 B_{n-r}z_T=\mathcal C(B_rz_T),                          \tag{2.9}
\]

where `mathcal C(e_S)=e_([n]\S)` is coordinatewise complementation.

#### Proof

Read positions in the step-two cyclic order.  The four exceptional
positions occur in two adjacent pairs.  Since `r<=m-1`, a length-`r`
window cannot meet both pairs.

If it meets neither pair, all four terms in (2.3) are identical and cancel.
If it contains both positions of one pair, the two old prefix sets and the
two new prefix sets agree as multisets, so they again cancel.  A contribution
therefore survives only when the window contains exactly one exceptional
position.

There is exactly one such window for each of the four positions.  The
common tail cores are, respectively,

\[
 \operatorname{suf}_l(\mathsf O),\quad
 \operatorname{pre}_l(\mathsf E),\quad
 \operatorname{suf}_l(\mathsf E),\quad
 \operatorname{pre}_l(\mathsf O).                      \tag{2.10}
\]

At the first and third exceptional positions the signed singleton change
is `+partial`, and at the second and fourth it is `-partial`.  This gives
(2.7).

For `r=1` the four copies of `partial(emptyset)` cancel.  At `r=m`, the
same elementary prefix table used in the two-for-two middle-wreath proof
matches all old and new masks; no property of `T` is needed.  Finally, the
complement of a cyclic `r`-interval is a cyclic `(n-r)`-interval in the same
order, proving (2.9).  QED.

### Corollary 2 (support and norm)

For `2<=r<=m-2`, the four cores in (2.7) are distinct and `B_rz_T` has
support eight, with all coefficients in `{+1,-1}`.  Hence

\[
                         \|B_rz_T\|_2^2=8.             \tag{2.11}
\]

At `r=m-1`, put

\[
 x=t_0,\qquad y=t_{2m-4},\qquad
 K=\mathsf E\setminus\{x,y\}.
\]

Then

\[
\boxed{
 B_{m-1}z_T=
 e_{K\cup\{\beta,x\}}-e_{K\cup\{\gamma,x\}}
 -e_{K\cup\{\beta,y\}}+e_{K\cup\{\gamma,y\}}.
}                                                         \tag{2.12}
\]

In particular `||B_(m-1)z_T||_2^2=4`.

#### Proof

The parity lists are disjoint and contain no `beta,gamma`.  Proper prefix
and suffix sets of a list of distinct entries cannot agree.  This proves
the first assertion.  At `r=m-1`, the prefix and suffix of `mathsf O` are
both the whole list and cancel.  The two `mathsf E` cores are
`mathsf E\{x}` and `mathsf E\{y}`, which gives (2.12).  QED.

Thus the complete lower profile of one trade is not a collection of
unrelated errors.  It is the rank-by-rank trace of four saturated flags.
Increasing `r` by one adjoins exactly one new coordinate to each of the four
cores in (2.7).

## 3. The depth form: four boundary deletions

It is useful to measure depth from the middle.  Put

\[
                         r=m-q.                       \tag{3.1}
\]

Write

\[
 \mathsf E=(e_0,\ldots,e_{m-2}),
 \qquad
 \mathsf O=(o_0,\ldots,o_{m-3}).
\]

Then (2.7) becomes

\[
\begin{aligned}
 B_{m-q}z_T={}&
 \partial\bigl(\mathsf O\setminus\{o_0,\ldots,o_{q-2}\}\bigr)
 +\partial\bigl(\mathsf E\setminus\{e_0,\ldots,e_{q-1}\}\bigr)\\
 &-\partial\bigl(\mathsf E\setminus
                  \{e_{m-q-1},\ldots,e_{m-2}\}\bigr)
 -\partial\bigl(\mathsf O\setminus
                  \{o_{m-q-1},\ldots,o_{m-3}\}\bigr).
                                                               \tag{3.2}
\end{aligned}
\]

Empty deletion lists are omitted.  Formula (3.2) is the exact locality
statement: the depth-`q` side effect is determined by deleting only the
first or last `q` entries of the two flip lists.  Passing from depth `q` to
`q+1` deletes one more boundary coordinate on each of four arms.

For coefficients `c_T`, let `d_q` be the maximum number of local trades
whose depth-`q` support contains one fixed target.  The sparse-matrix norm
bound gives

\[
 \left\|\sum_Tc_TB_{m-q}z_T\right\|_2^2
       \le 8d_q\sum_Tc_T^2.                             \tag{3.3}
\]

For the original `p=0` family, remote data through `m=10` give the sharp
value `d_q=Cat_q`.  Formula (3.2) reduces a proof of that observation to an
exact fiber count for four boundary flags; no wreath enumeration remains.
The Catalan fiber bound itself is not claimed here as proved.

## 4. The same component at every Dyck concatenation boundary

Let `D_j` denote the Dyck words of semilength `j`.  The MSW flip permutation
satisfies the concatenation law

\[
             \rho(UV)=\rho(U)\,\Vert\,
                       (|U|+\rho(V))                   \tag{4.1}
\]

for Dyck words `U,V`, where `|U|` is the ordinary word length.

Fix

\[
 0\le p\le m-2,\qquad P\in\mathcal D_p,qquad
 R\in\mathcal D_{m-p-2},\qquad d=2p.                  \tag{4.2}
\]

Define

\[
                         X=P1100R,qquad Y=P1010R.      \tag{4.3}
\]

Using (4.1), and cyclically rotating the omitted-label words so that the
displayed four-letter block comes first, gives

\[
\begin{aligned}
q(X)&=(d+4,d+2,d+3,d+1,T_{P,R}),\\
q(Y)&=(d+2,d+1,d+4,d+3,T_{P,R}),                       \tag{4.4}
\end{aligned}
\]

where

\[
 T_{P,R}=(d+4+\rho(R),\ n,\ \rho(P)).                  \tag{4.5}
\]

Let `tau_p=(d+2 d+3)`.  The universal identity of Section 2 proves:

### Theorem 3 (Catalan family at every position)

For every triple `(p,P,R)`,

\[
 z_{p,P,R}=e_{\tau_pq(X)}+e_{\tau_pq(Y)}-e_{q(X)}-e_{q(Y)} \tag{4.6}
\]

is a support-feasible two-for-two exact-middle trade.  For fixed `p`, the
negative supports of these trades are pairwise disjoint, as are the positive
supports, so all

\[
              \operatorname {Cat}_p
              \operatorname {Cat}_{m-p-2}             \tag{4.7}
\]

trades may be switched independently.

Across all `p`, the number of local trade occurrences is `Cat_(m-1)` by
the Catalan convolution (1.1).

#### Proof

Equations (4.4)--(4.5) put the four words in exactly the form (2.2), so
their middle multiplicity vectors agree.  The two old wreaths belong to the
MSW factor and are disjoint.  Equality of multiplicity vectors forces the
two new wreaths to be disjoint as well, proving support feasibility.

For fixed `p`, distinct pairs `(P,R)` give disjoint pairs of Dyck words in
(4.3).  Their transposed middle unions equal those disjoint old unions, so
the positive supports are disjoint too.  QED.

The original `Cat_(m-2)` theorem is the case `p=0`.

## 5. Exact Dyck-coordinate form of the flags

For a Dyck word `W` of semilength `s`, split its flip permutation into
insertion and deletion lists

\[
 \rho(W)=(a_0,b_0,a_1,b_1,\ldots,a_{s-1},b_{s-1}),
 \qquad
 \mathsf A(W)=(a_i),\quad \mathsf B(W)=(b_i).          \tag{5.1}
\]

The sets underlying `mathsf A(W)` and `mathsf B(W)` are respectively the
down-step and up-step positions of `W`.

For the local trade `(p,P,R)`, the parity lists (2.5) are exactly

\[
\boxed{
\begin{aligned}
 \mathsf E_{P,R}&=(d+4+\mathsf A(R),\ n,\ \mathsf B(P)),\\
 \mathsf O_{P,R}&=(d+4+\mathsf B(R),\ \mathsf A(P)).
\end{aligned}}                                           \tag{5.2}
\]

In particular, as unordered sets,

\[
\begin{aligned}
 E_{P,R}&=(d+4+\operatorname {Down}(R))
             \cup\{n\}\cup\operatorname {Up}(P),\\
 O_{P,R}&=(d+4+\operatorname {Up}(R))
             \cup\operatorname {Down}(P).              \tag{5.3}
\end{aligned}

The two sets partition all coordinates outside the local four-coordinate
block.  Formula (5.2), substituted into (2.7), is the promised exact
Dyck-coordinate description at every rank.

The first-return recursion also gives

\[
\begin{aligned}
 \mathsf A(1u0v)
   &=(2|u|_s+2,\ 2|u|_s+2-\mathsf B(\operatorname{rev}u),
                   \ 2|u|_s+2+\mathsf A(v)),\\
 \mathsf B(1u0v)
   &=(2|u|_s+2-\mathsf A(\operatorname{rev}u),\ 1,
                   \ 2|u|_s+2+\mathsf B(v)),            \tag{5.4}
\end{aligned}

where `|u|_s` is the semilength.  Thus the four boundary flags in (3.2)
peel recursively through the first and last Dyck atoms.  This is the exact
Catalan-local structure suggested by the experiments.

## 6. Triangular independence at the first shadow

Although Section 5 looks like the beginning of a Catalan/Haar absorber, the
orientation is the wrong one: every local variable already has its own
pivot at the first lower rank.

For a subset `S` of `[n]`, define its first-negative position along the
first `2m` coordinates

\[
 \eta(S)=\min\{j:2|S\cap[j]|-j<0\}.                    \tag{6.1}
\]

For the context `(p,P,R)`, let

\[
 \beta_p=2p+2,qquad
 x_{P,R}=\text{the first entry of }\mathsf E_{P,R},
\]

and choose the following one of the four square targets in (2.12):

\[
 S^*_{p,P,R}=E_{P,R}\setminus\{x_{P,R}\}\cup\{\beta_p\}.
                                                               \tag{6.2}
\]

### Lemma 4 (pivot recovery)

The target (6.2) has

\[
                         \eta(S^*_{p,P,R})=2p+1.        \tag{6.3}
\]

It occurs in no local-trade column with parameter `p'<p`, and among the
columns with parameter `p` it occurs only in `B_(m-1)z_(p,P,R)`.

#### Proof

On coordinates `1,...,2p`, the target is exactly the up-step set of the
Dyck word `P`, so its height is nonnegative and returns to zero.  Coordinate
`2p+1` is the first coordinate of the local four-block and is absent.
Hence (6.3).

Every square target belonging to a context `p'<p` first becomes negative
no later than `2p'+1`, so it cannot equal (6.2).  For a context with the
same `p`, a square target obtained by deleting the last `mathsf E` endpoint
removes an up-step from `P` and therefore becomes negative before the local
block (unless `p=0`, when presence of `n` distinguishes the two sides).
The inserted choice `beta_p` rather than `gamma_p` is visible directly.

It remains to recover `P,R` from the first-endpoint side.  The first `2p`
coordinates recover `P`.  If `R` is nonempty, the suffix part is

\[
             \operatorname {Down}(R)\setminus\{a_0(R)\}, \tag{6.4}
\]

where `a_0(R)` is the first-return down-step of `R`.  The map in (6.4) is
injective.  Indeed, treat the positions outside (6.4) as up-steps and let
`h'` be the resulting height.  The deleted first-return position is

\[
                  1+\max\{j:h'(j)=1\};                \tag{6.5}
\]

adding it back as a down-step recovers `R`.  The empty `R` case is marked
by deletion of the coordinate `n`.  Thus the context is unique.  QED.

### Theorem 5 (no local Haar kernel)

Assume `m>=3`.

The vectors

\[
 \{B_{m-1}z_{p,P,R}:
       0\le p\le m-2, P\in\mathcal D_p,
       R\in\mathcal D_{m-p-2}\}                       \tag{6.6}
\]

are linearly independent over every field.  Consequently (1.2) holds over
the integers and the reals.

#### Proof

Suppose a nonzero linear relation exists and choose the largest `p` carrying
a nonzero coefficient.  Within that level choose any nonzero column.  Its
pivot row (6.2) is absent from every lower-`p` column by Lemma 4, from every
other column at the same `p`, and there are no nonzero higher-`p` columns by
choice of `p`.  Its coefficient in the alleged relation is therefore the
nonzero column coefficient times `+1` or `-1`, a contradiction.  QED.

For each fixed `p`, the four square supports are in fact pairwise disjoint
as `(P,R)` varies.  One endpoint side recovers `R` by (6.5); the other side
recovers `P` by the dual rule that its deleted up-step is the first position
where the modified Dyck height becomes negative.  Hence the fixed-level
map is an exact isometry:

\[
 \left\|B_{m-1}\sum_{P,R}c_{P,R}z_{p,P,R}\right\|_2^2
       =4\sum_{P,R}c_{P,R}^2.                          \tag{6.7}
\]

## 7. Consequences for a frame/absorption program

The exact formulas settle what these components can and cannot do.

### 7.1 No bulk frame

There are only `Cat_(m-1)` local columns, each touching four first-shadow
targets.  Therefore their entire rank-`m-1` support has size at most

\[
                         4\operatorname {Cat}_{m-1}.   \tag{7.1}
\]

But

\[
 \binom{2m+1}{m-1}=\Theta(m\operatorname {Cat}_m),
 \qquad
 \operatorname {Cat}_{m-1}=\Theta(\operatorname {Cat}_m). \tag{7.2}
\]

Thus these components see only an `O(1/m)` fraction of the first-shadow
coordinates.  A frame inequality on the full zero-margin discrepancy space
is impossible: take a discrepancy supported outside (7.1).

### 7.2 No sequential absorber

By Theorem 5, once rank `m-1` is held fixed, no nontrivial linear
combination of these local trades remains.  In particular, no binary choice
of them can repair rank `m-2` while preserving an already exact rank
`m-1` shadow.

This also rules out the most direct Catalan/Haar proposal.  The tail in
(4.5) is a literal smaller MSW flip word, and (5.4) really does give a
recursive flag structure; nevertheless the top square records every local
coefficient injectively.  Recursion alone does not create an absorber.

### 7.3 The viable role: sparse final absorption

The local switches can still be valuable after a separate bulk mechanism
has reduced the residual defect to `O(Cat_m)` specially located targets.
Their exact eight-support profile and bounded boundary depth make them good
candidates for a final independent-transversal or local-lemma step.  They
cannot perform the bulk correction themselves.

### 7.4 Exact next theorem

A genuine multirank absorber must contain a nonzero support-feasible circuit
`w` satisfying

\[
                         B_{m-1}w=0,
              \qquad B_{m-q}w\ne0\text{ for some }q\ge2. \tag{7.3}
\]

Elementary first-shadow squares have algebraic three-cube syzygies, but
Theorem 5 proves that none of those syzygies is lifted by the complete
concatenation-local two-for-two family.  The next plausible sources are:

1. the larger interaction components in the `(2 3)` MSW component tower;
2. commutators of switches belonging to different factor fibers, where the
   second switch is taken after the first rather than both at the original
   MSW factor; or
3. a legal lift of one three-cube relation among Petr--Turek squares.

Any of these would be the first true Haar detail: invisible at depth one but
active below it.  Until such a circuit is produced, a multirank
frame/absorption theorem based only on the constant-size local components is
mathematically impossible.

## 8. Exact heat-bath identity and the variance gate

There is a useful global operation which should not be confused with the
local absorber above.  Let `F` be any exact middle factor, let `tau` be a
coordinate transposition, and let `K` run through the connected components
of the `F` versus `tau F` interaction graph.  Independently on each
component, retain its `F` side or replace it by its `tau F` side, each with
probability `1/2`.  The resulting collection is again an exact middle
factor.

At rank `r`, put

\[
 c_r=B_r{\bf1}_F,
 \qquad
 \Delta_{K,r}=B_r({\bf1}_{K\cap\tau F}
                       -{\bf1}_{K\cap F}).             \tag{8.1}
\]

### Lemma 6 (factor heat bath)

If `C_r` is the random rank-`r` multiplicity vector after the component
choices, then

\[
 \boxed{\mathbb E C_r={c_r+\tau c_r\over2}.}            \tag{8.2}
\]

For every `tau`-invariant target vector `u_r`, in particular the constant
mean vector,

\[
\boxed{
 \mathbb E\|C_r-u_r\|_2^2
 =\|c_r-u_r\|_2^2
  -{1\over4}\|c_r-\tau c_r\|_2^2
  +{1\over4}\sum_K\|\Delta_{K,r}\|_2^2.
}                                                         \tag{8.3}
\]

The identical formula holds after summing ranks with arbitrary nonnegative
weights.

#### Proof

The component effects sum to

\[
                    \sum_K\Delta_{K,r}=\tau c_r-c_r.   \tag{8.4}
\]

Writing each Bernoulli choice as `1/2+epsilon_K`, where the independent
variables `epsilon_K` have mean zero and variance `1/4`, gives (8.2) and

\[
 C_r-u_r={c_r+\tau c_r\over2}-u_r
             +\sum_K\epsilon_K\Delta_{K,r}.            \tag{8.5}
\]

The cross terms vanish in expectation.  Since `(I+tau)/2` is the
orthogonal projection onto the `tau`-even subspace,

\[
 \left\|{c_r+\tau c_r\over2}-u_r\right\|_2^2
 =\|c_r-u_r\|_2^2-{1\over4}\|c_r-\tau c_r\|_2^2,
\]

which proves (8.3).  QED.

Formula (8.2) is an exact Johnson-diffusion statement: averaging over the
choice of `tau` sends every rank discrepancy through the random-transposition
operator.  But (8.3) displays the missing integral gate.  Mean contraction
is useful only when it beats component noise.

Define

\[
 D_r=\sum_K\Delta_{K,r}=\tau c_r-c_r.                  \tag{8.6}
\]

The heat bath contracts rank-`r` energy exactly when

\[
                  \|D_r\|_2^2>
                  \sum_K\|\Delta_{K,r}\|_2^2.         \tag{8.7}
\]

Equivalently, the total pairwise correlation of the component effects is
positive.  Disjoint small effects give equality, not strict contraction.
In particular, for any fixed `p`, the local size-two components have
disjoint first-shadow supports by (6.7), so randomizing them causes **zero**
expected change of the rank-`m-1` quadratic energy.  Their mean is smoother,
but their variance cancels that smoothing exactly.

For the original `p=0` family, if only its `Cat_(m-2)` independent
components are randomized, the variance contributions are explicit from
Corollary 2:

\[
 {1\over4}\sum_K\|\Delta_{K,m-1}\|_2^2
     =\operatorname {Cat}_{m-2},
 \qquad
 {1\over4}\sum_K\|\Delta_{K,r}\|_2^2
     =2\operatorname {Cat}_{m-2}quad(2\le r\le m-2). \tag{8.8}
\]

Thus an actual diffusion/absorption theorem needs two separate ingredients.

1. **Bulk alignment.**  Find a transposition (or a short product of them)
   whose full interaction components satisfy the weighted version of
   (8.7) with a quantitative gap.  Conditional expectation then chooses a
   deterministic side of every component with at most the heat-bath energy.
2. **Sparse residue absorption.**  Reserve disjoint constant-size local
   components for the final `O(Cat_m)` residue.  Their exact four-flag
   actions make this a bounded-conflict selection problem, but Theorem 5
   requires the first shadow and deeper shadows to be solved simultaneously.

Random-transposition spectral contraction of the **mean alone** is not a
proof of progress.  The precise new inequality to establish is the
multirank component-alignment bound

\[
 \sum_q w_q\sum_K\|\Delta_{K,m-q}\|_2^2
 \le (1-\varepsilon_m)
       \sum_qw_q\left\|\sum_K\Delta_{K,m-q}\right\|_2^2, \tag{8.9}
\]

for some useful positive `epsilon_m`, possibly after excluding a reserved
local absorber.  Equation (8.9), rather than (8.2), is the exact bridge from
Johnson diffusion to an integral factor contraction.

There is an explicit spectral benchmark for (8.9).  Let `tau` now be a
uniform random coordinate transposition.  Every factor discrepancy

\[
                         f_r=c_r-\mu_r{\bf1}           \tag{8.10}
\]

has zero point marginals: each selected cyclic order contains a fixed point
in exactly `r` of its rank-`r` intervals.  Hence `f_r` has no
`S^(n)` or `S^(n-1,1)` component in the multiplicity-free Johnson
decomposition

\[
 \mathbb R^{\binom{[n]}r}
       =\bigoplus_{j=0}^r S^{(n-j,j)}.                 \tag{8.11}
\]

The average transposition has eigenvalue

\[
 1-\frac{j(n-j+1)}{\binom n2}                          \tag{8.12}
\]

on `S^(n-j,j)`.  Since `(I+tau)/2` is a projection for each `tau`,
(8.11)--(8.12) give

\[
 \mathbb E_\tau\left\|{f_r+\tau f_r\over2}\right\|_2^2
 \le\left(1-\frac2n\right)\|f_r\|_2^2,               \tag{8.13}
\]

or equivalently

\[
 \mathbb E_\tau {1\over4}\|f_r-\tau f_r\|_2^2
       \ge {2\over n}\|f_r\|_2^2.                    \tag{8.14}
\]

Therefore a completely concrete sufficient bulk theorem is

\[
 \mathbb E_\tau\sum_qw_q\sum_K
       \|\Delta_{K,m-q}\|_2^2
 \le\left({8\over n}-4\varepsilon_m\right)
       \sum_qw_q\|f_{m-q}\|_2^2.                     \tag{8.15}
\]

Under (8.15), choosing `tau` and then all component sides by conditional
expectation decreases the weighted discrepancy energy by at least
`epsilon_m` times its current value.  This is the sharp quantitative
form of the proposed heat-bath contraction.  The unresolved issue is now
entirely the component-variance estimate (8.15), not the spectral action of
the mean.
