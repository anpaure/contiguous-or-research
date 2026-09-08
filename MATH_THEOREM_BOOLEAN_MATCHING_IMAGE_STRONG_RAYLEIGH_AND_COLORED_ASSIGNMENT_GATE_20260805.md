# Boolean matching images are Strong Rayleigh; coloured assignments are the remaining gate

**Date:** 2026-08-05  
**Method:** pure mathematics and primary-source theorem-scope audit; no
finite search, solver, or H100 computation  
**Status:** unconditional exact-marginal and Chernoff theorem for the set of
rank-`q+1` vertices occupied by old Boolean continuations.  This includes
the old-versus-dummy statistic that no old-only `C6` can move.  It does
**not** give concentration for an arbitrary colouring of the old rank-`q`
vertices; that assignment-within-the-image problem is the remaining
one-step oracle.

## 0. The augmented Boolean interface

Let `n=2r`, let `q<r`, and put

\[
 L=\binom{[n]}q,
 \qquad
 R=\binom{[n]}{q+1},
 \qquad
 m=|L|,
 \qquad
 N=|R|,
 \qquad
 h=N-m.
\tag{0.1}
\]

Join `S in L` to `T in R` when `S subset T`.  Adjoin `h` labelled
universal dummies, each adjacent to every member of `R`.  The resulting
square bipartite graph is the interface `J_q`.

A perfect matching of `J_q` consists of:

1. a matching saturating every old vertex in `L`; and
2. a bijection from the dummies to the unused members of `R`.

For a perfect matching `M`, write

\[
 I(M)=\{T\in R:T\text{ is matched to an old vertex}\}.
\tag{0.2}
\]

Thus `|I(M)|=m`, and its complement is precisely the dummy image set.

## 1. The uniform perfect matching has the exact fractional marginals

### Proposition 1.1

Choose a perfect matching of `J_q` uniformly.  Then

\[
 \Pr(ST\in M)={1\over n-q}
 \quad(S\in L,\ S\subset T),
\tag{1.1}
\]

and

\[
 \Pr(dT\in M)={1\over N}
 \quad(d\text{ a dummy},\ T\in R).
\tag{1.2}
\]

#### Proof

The coordinate-permutation group acts transitively on the old inclusion
edges.  Hence all `n-q` edges at a fixed old vertex have the same
probability, and exactly one is selected.  This gives (1.1).

Coordinate permutations on `R`, together with arbitrary permutations of
the labelled dummies, act transitively on the dummy edges.  Exactly one of
the `N` edges at each dummy is selected, giving (1.2). `square`

This is the same fractional point as equation (1.1) of
`MATH_THEOREM_COLORED_BOOLEAN_ONE_STEP_UNIFORM_FLOW_CONTRACTION_AND_EXACT_ROUNDING_GAP_20260805.md`.

## 2. Stable polynomial for the old image set

Let `H_q` be only the old inclusion graph `L--R`.  Regard `R` as the
ground-set shore of the transversal matroid presented by `H_q`: a set
`B subset R` is independent when it can be matched injectively into `L`.
Its bases are exactly the `m`-sets which occur as `I(M)` for a matching
saturating `L`.

For a base `B`, let `c_B` be the number of matchings of `H_q` saturating
`L` and having image `B`.  Define

\[
                 P_q(y)=\sum_{B}c_B\prod_{T\in B}y_T.
\tag{2.1}
\]

### Theorem 2.1 (weighted transversal-base stability)

`P_q` is a homogeneous multiaffine real-stable polynomial.

#### Proof

For completeness, apply the Heilmann--Lieb matching-polynomial theorem to
`H_q`, retaining variables only on the shore `R` and setting the variables
on `L` to one.  In the convention of the half-plane-property literature,
the resulting restricted matching polynomial

\[
 F_q(y)=\sum_{K\text{ a matching of }H_q}
             \prod_{T\in V(K)\cap R}y_T,
\tag{2.2}
\]

has the open **right** half-plane property.  Its maximum total degree is
`m`.  The homogeneous
degree-`m` part is

\[
 [F_q]_{m}=\sum_{K:\,|K|=m}
             \prod_{T\in V(K)\cap R}y_T=P_q(y).
\tag{2.3}
\]

The top homogeneous part retains the same right-half-plane property: it is
the locally uniform limit

\[
                 [F_q]_m(y)=\lim_{t\to\infty}t^{-m}F_q(ty),
\tag{2.4}
\]

and Hurwitz closure applies.  It is nonzero because the normalized
matching property of the Boolean lattice supplies a matching saturating
`L`.

Finally `P_q` is homogeneous of degree `m`.  If every `z_T` has positive
imaginary part, then every `-i z_T` has positive real part, and

\[
 P_q(-iy)=(-i)^mP_q(y).
\tag{2.5}
\]

Right-half-plane nonvanishing therefore implies upper-half-plane
nonvanishing.  Since the coefficients are real, `P_q` is real stable.
`square`

This is the weighted, or weak-half-plane, theorem for transversal
matroids.  It is important that the coefficients are `c_B`; no claim that
the unweighted basis polynomial of every transversal matroid is stable is
being made.

### Theorem 2.2 (Strong Rayleigh old-image law)

Under a uniform perfect matching of `J_q`, the random set `I(M)` is Strong
Rayleigh.

#### Proof

Every old matching with image `B` has exactly `h!` completions by the
labelled dummies.  Hence

\[
 \Pr(I(M)=B)={c_B\over\sum_{B'}c_{B'}}.
\tag{2.6}
\]

Its generating polynomial is therefore `P_q(y)/P_q(1)`, which is real
stable by Theorem 2.1 and has nonnegative coefficients.  This is exactly
the Strong Rayleigh property. `square`

There is no conflict with the edge-coordinate no-go in
`MATH_THEOREM_PERFECT_MATCHING_MAXENT_EXACT_MARGINAL_AND_STRONG_RAYLEIGH_NOGO_20260805.md`.
The full vector of selected **edges** is not Strong Rayleigh.  The theorem
here concerns only its coarser projection to the occupied right vertices.

## 3. Exact owner concentration

Let `U subset [n]` have size `v>=q+1`, and put

\[
 R_U=\binom U{q+1},
 \qquad
 X_U=|I(M)\cap R_U|.
\tag{3.1}
\]

### Corollary 3.1

The mean is exactly

\[
 \mu_U=\mathbb E X_U
 ={m\over N}\binom v{q+1}
 ={v-q\over n-q}\binom vq.
\tag{3.2}
\]

Moreover `X_U` obeys the usual Bernoulli Chernoff bounds; for example,

\[
 \Pr(X_U\ge\mu_U+t)
 \le
 \exp\!\left(-{t^2\over2(\mu_U+t/3)}\right),
\tag{3.3}
\]

and

\[
 \Pr(X_U\le\mu_U-t)
 \le
 \exp\!\left(-{t^2\over2\mu_U}\right).
\tag{3.4}
\]

#### Proof

The group on coordinates is transitive on `R`, so every `T in R` has
inclusion probability `m/N`.  This also follows by summing (1.1) over the
`q+1` old neighbours of `T`.  Summing over `R_U` proves the first formula;
the second is the binomial identity

\[
 {m\over N}\binom v{q+1}
 ={q+1\over n-q}\binom v{q+1}
 ={v-q\over n-q}\binom vq.
\]

Strong Rayleigh implies negative association.  The standard exponential-
moment proof for negatively associated Bernoulli variables gives
(3.3)--(3.4). `square`

Since `R\setminus I(M)` is the dummy image set, its count in every `R_U`
has the same two-sided concentration by complementation.

### Corollary 3.2 (the `C6`-invisible statistic is nevertheless controlled)

Colour precisely the old vertices `S subset U`.  Any old edge ending in
`R_U` starts at such a vertex, so its coloured owner statistic is exactly
`X_U`.  It therefore has (3.2)--(3.4), even though every old-only Boolean
`C6` switch leaves this statistic unchanged.

Thus old-only local switching was too small a proof mechanism, not an
obstruction to the actual uniform matching law.

## 4. Exact `C6` sensitivity formula

The preceding distinction can be made sharp.  Let `A subset L` be an
arbitrary old colour class.  A Boolean incidence hexagon is specified by

\[
 C\in\binom{[n]}{q-1},
 \qquad
 a,b,c\notin C\text{ distinct},
\tag{4.1}
\]

with old vertices `C+a,C+b,C+c` and upper vertices
`C+ab,C+bc,C+ca`.  Toggle its two alternating perfect matchings.

### Proposition 4.1

For a fixed future owner `U`, the number of unoriented hexagons on which
the toggle changes the `A`-coloured image count in `R_U` is

\[
 (n-v)\,\bigl|\partial_{J(v,q)}(A\cap\tbinom Uq)\bigr|,
\tag{4.2}
\]

where the boundary is in the Johnson graph on `binom(U,q)`.

#### Proof

The toggle can change the statistic only when `C subset U` and exactly
two of `a,b,c` lie in `U`.  If, say, `a,b in U` and `c notin U`, the sole
hexagon upper vertex inside `U` is `C+ab`; its old provider changes between
`C+a` and `C+b`.  The statistic changes exactly when these two rank-`q`
sets have opposite `A`-colours.

Every Johnson boundary edge inside `binom(U,q)` uniquely supplies `C,a,b`,
and there are `n-v` choices of `c outside U`.  This proves (4.2). `square`

For `A=binom(U,q)`, the boundary in (4.2) is empty, whereas (3.2) is
positive.  No number of old-only `C6` toggles can randomize that statistic.
The Strong Rayleigh projection works because the full perfect-matching law
also changes which upper vertices are occupied by old vertices; in local
language it necessarily uses old--dummy alternating circuits, beginning
with suitable `C4` switches.

## 5. Why arbitrary persistent colours remain open

For a general colour class `A subset L`, the required statistic is

\[
 X_{A,U}(M)=
 |\{S\in A:M(S)\in R_U\}|.
\tag{5.1}
\]

This is not determined by `I(M)`.  The stable polynomial `P_q` knows which
right vertices are occupied by old continuations, but not which old colour
is assigned to each occupied right vertex.

### Proposition 5.1 (a fixed colour image need not be a matroid base law)

Already for `n=4,q=1`, let the old vertices be `1,2,3,4` and take

\[
                         A=\{1,2,3\}.
\tag{5.2}
\]

The support of the random image set

\[
                         I_A(M)=\{M(i):i\in A\}
\tag{5.3}
\]

under the uniform matching contains

\[
 B=\{14,23,34\},
 \qquad
 C=\{13,24,34\},
\tag{5.4}
\]

but violates basis exchange.  Consequently `I_A(M)` is not Strong
Rayleigh.

#### Proof

The set `B` is realized by

\[
 1\mapsto14,quad2\mapsto23,quad3\mapsto34,quad4\mapsto24,
\tag{5.5}
\]

and `C` by

\[
 1\mapsto13,quad2\mapsto24,quad3\mapsto34,quad4\mapsto14.
\tag{5.6}
\]

Take `e=23 in B\setminus C`.  The two candidates in `C\setminus B` are
`13` and `24`.

* In `B-e+13={14,13,34}`, the old vertex `2 in A` has no possible image.
* In `B-e+24={14,24,34}`, the three members of `A` can use all three
  pairs, but they exhaust every neighbour `14,24,34` of the remaining old
  vertex `4`; no saturated extension exists.

Thus no exchange for `e` remains in the support.  The support of a
homogeneous multiaffine real-stable polynomial must be a matroid base
family, so this fixed-colour image law is not Strong Rayleigh. `square`

The ordinary rank-sequence notion of ultra-log-concavity is vacuous here:
`|I_A|=|A|` deterministically.  It supplies no owner-count concentration.

### Proposition 5.2 (exact block-polynomial boundary)

Define the owner-block probability generating polynomial

\[
 Z_{A,U}(z)=
 \sum_{M\in\operatorname{PM}(J_q)}
 z^{|M\cap(A\times R_U)|}.
\tag{5.7}
\]

If `A` contains every rank-`q` subset of `U`, then `Z_(A,U)` is real
rooted with nonpositive zeros.

For arbitrary `A`, no conditioning-stable real-rooted permanent theorem is
possible, even on Boolean owner blocks.  In `J_1` for `n=8`, a conditioning
leaves a residual `C_12` for which the conditional block polynomial is

\[
                         1+z^2.
\tag{5.8}
\]

#### Proof

If `binom(U,q) subset A`, every old edge ending in `R_U` starts in `A`.
The exponent in (5.7) is therefore `|I(M)\cap R_U|`.  Up to the constant
dummy factor, (5.7) is the stable specialization

\[
 P_q(y_T=z\ (T\in R_U),\ y_T=1\ (T\notin R_U)),
\tag{5.9}
\]

so it is univariate real rooted.  Nonnegative coefficients force all roots
to be nonpositive.

For the negative conditional statement, take the six residual old vertices
`1,...,6` and the six residual upper vertices

\[
                         12,23,34,45,56,16.
\tag{5.10}
\]

Condition old vertex `7` to use `17`, old vertex `8` to use `28`, and the
twenty labelled dummies to use all upper vertices outside (5.10) other
than those two fixed old images.  The remaining incidence graph is one
alternating `C_12`, with exactly two perfect matchings.

Let

\[
 A=\{1,4\},
 \qquad
 U=\{1,2,4,5\}.
\tag{5.11}
\]

One alternating phase contains `1->12` and `4->45`, contributing two
block edges.  The other contains `1->16` and `4->34`, contributing none.
The conditional polynomial is (5.8), whose roots are `+i,-i`. `square`

Proposition 5.2 does **not** assert that the unconditional `Z_(A,U)` is
non-real-rooted for some Boolean `A,U`; that remains open.  It proves that
real-rootedness cannot be obtained from a multivariate stability statement
which survives arbitrary edge conditioning.  The endpoint-forced colour
case is exactly the image-set theorem and is fully solved.

Conditioning on `I(M)=B` leaves a perfect matching of the induced graph
`H_q[L,B]`.  The edge indicators of that conditional perfect matching are
not generically Strong Rayleigh, and the support obstruction from the
edge-coordinate no-go still applies.  Therefore Theorem 2.2 cannot be
iterated colour by colour without an additional theorem.

The exact surviving one-step statement is:

> **Boolean coloured-assignment oracle.**  Under the uniform perfect
> matching of `J_q`, or under another law having the exact marginals
> (1.1)--(1.2), prove a Bernstein/Chernoff bound for every
> `X_(A,U)` required by the persistent whole-configuration colouring.

The theorem above removes the occupancy half of this oracle.  What remains
is concentration of the assignment **within** the random old image set.
Promising proof mechanisms must therefore control one of:

1. the conditional perfect matching on `H_q[L,I(M)]`;
2. alternating circuits which include both old vertices and universal
   dummies, not old-only `C6`s; or
3. permanent ratios under exposing a coloured subset of the old shore.

## 6. Scope of the external theorem

The only external input in the proof is the Heilmann--Lieb stability
theorem in its restricted matching-polynomial form, and the standard
Strong-Rayleigh implication to negative association.

Primary references:

* Y.-B. Choe, J. Oxley, A. Sokal and D. Wagner,
  *Homogeneous multivariate polynomials with the half-plane property*,
  Advances in Applied Mathematics 32 (2004),
  <https://arxiv.org/abs/math/0202034>.  Section 10 gives the matching-
  polynomial/permanent construction and the weak half-plane property of
  transversal matroids.
* J. Borcea, P. Branden and T. Liggett,
  *Negative dependence and the geometry of polynomials*, JAMS 22 (2009),
  <https://arxiv.org/abs/0707.2340>.  It develops Strong Rayleigh measures,
  their closure properties and negative association.

No assertion about concentration of arbitrary edge-coloured assignment
statistics is imported from either source.
