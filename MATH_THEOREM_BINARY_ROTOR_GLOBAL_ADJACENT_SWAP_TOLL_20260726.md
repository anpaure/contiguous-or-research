# Binary rotors: the global adjacent-swap toll

Date: 2026-07-26

## 0. Outcome

Let an owner-transversal binary-rotor circulation on the injective de
Bruijn graph have (C) support components and (a) selected (A)-arcs.
Let (c_1) be the number of non-pure components.  Then

\[
 \boxed{W\le nC+2a-2c_1.}                         \tag{0.1}
\]

Consequently

\[
 C=o(W/m)\quad\Longrightarrow\quad
 a\ge(1/2-o(1))W.                                 \tag{0.2}
\]

This replaces the earlier Catalan-order switch lower bound.  Therefore
the sufficient condition (Ha=o(W)) cannot hold for any (H\to\infty)
when the component count is small enough for coefficient one.

The binary-rotor architecture is not entirely refuted: the exact
upper--lower identity is a **signed** sum of Johnson edges, and the
(Theta(W)) switch contributions may cancel.  The corrected surviving
condition is aggregate divergence (o(W)), not small switch count.

## 1. One adjacent swap changes at most two wreath owners

For a cyclic order (pi) on (n=2m+1) coordinates, write
(mathcal W(pi)) for its (n) length-(m) cyclic interval sets.

### Lemma 1.1

If (pi') is obtained from (pi) by swapping two cyclically adjacent
coordinates, then

\[
 |\mathcal W(\pi)\cap\mathcal W(\pi')|\ge n-2,
 \qquad
 |\mathcal W(\pi')\setminus\mathcal W(\pi)|\le2.  \tag{1.1}
\]

#### Proof

A length-(m) cyclic position interval is changed as an underlying set
only when it contains exactly one of the two swapped adjacent positions.
There is exactly one such interval on each side of the adjacent cut.
Every other interval contains both swapped positions or neither, so its
underlying set is unchanged.  This proves (1.1). \(\square\)

## 2. Consecutive rotor runs form an adjacent-swap chain

Within one non-pure rotor component, split the selected states into its
maximal (B)-runs.  Let their supporting (B)-orbits, viewed as cyclic
coordinate orders, be

\[
 \pi_1,\pi_2,\ldots,\pi_{a_C}.
\]

There is one (A)-transition between consecutive runs.  If its tail
state is

\[
 (x_1,\ldots,x_n),
\]

the next state is

\[
 A(x_1,\ldots,x_n)
 =(x_2,\ldots,x_{n-1},x_1,x_n).
\]

As a cyclic order this differs from the preceding (B)-orbit by swapping
the adjacent cyclic pair (x_n,x_1).  Hence Lemma 1.1 applies at every
run boundary.

### Lemma 2.1

For (k) consecutive (B)-runs in one component,

\[
 \left|\bigcup_{i=1}^{k}\mathcal W(\pi_i)\right|
 \le n+2(k-1).                                     \tag{2.1}
\]

#### Proof

Start with (n) owners in (mathcal W(\pi_1)).  By Lemma 1.1 each
successive support adds at most two new owners. \(\square\)

## 3. Global switch toll

### Theorem 3.1

If a non-pure component contains (a_C) (A)-arcs, then its number of
selected states is at most

\[
 n+2(a_C-1).                                        \tag{3.1}
\]

Consequently (0.1)--(0.2) hold.

#### Proof

Every selected state in a (B)-run has middle owner in the wreath support
of that run.  Owner transversality makes all selected owners globally
distinct.  Apply (2.1) with (k=a_C), obtaining (3.1).

A pure (B)-component contributes exactly (n) states.  Summing (3.1)
over the (c_1) non-pure components and adding the pure components gives

\[
 W\le n(C-c_1)+\sum_{C\ {m nonpure}}[n+2(a_C-1)]
   =nC+2a-2c_1.
\]

If (C=o(W/m)), then (nC=o(W)), and rearrangement gives (0.2).
\(\square\)

## 4. Corrected compiler currency

For lower and complementary upper load vectors (L_{m-q},R_{m-q}), the
exact identity remains

\[
 R_{m-q}-L_{m-q}=D_q,
\]

where (D_q) is the signed sum of the Johnson edges contributed by the
selected (A)-arcs.  Define

\[
 \mathfrak D_H=
 \sum_{q=0}^{H}\sum_T(L_{m-q}(T)-R_{m-q}(T))_+
 =\frac12\sum_{q=0}^{H}\|D_q\|_1.                 \tag{4.1}
\]

Then upper holes are at most lower holes plus \(\mathfrak D_H\), so the
total lower-plus-upper repair is at most twice the lower holes plus
\(\mathfrak D_H\).  The literal compiler therefore needs

\[
 C=o(W/m),\qquad
 \sum_{q\le H}M(L_{m-q})=o(W),\qquad
 \mathfrak D_H=o(W).                               \tag{4.2}
\]

The scalar estimate \(\mathfrak D_H\le(H+1)a\) is now unusable because
(a=\Omega(W)).  A successful rounding must arrange cancellation of a
linear number of nested Johnson-edge divergences simultaneously across
depths.  The exact uniform fractional circulation has (D_q=0) at every
depth, so there is no fractional obstruction; integrality and correlated
cancellation are the remaining theorem.
