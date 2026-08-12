# The terminal `J_b=(3,2,1^(b-1))` component has a constant-gap rotation orbit

**Date:** 2026-08-05  
**Method:** exact periodic-BBS action--angle matrix and a mod-three quotient
character; no computation or search  
**Status:** unconditional subject to the standard exact action--angle
correspondence used in the PBBS component census.  Every physical component
containing the terminal tie phase contains either all its coordinate
rotations or one third of them, with factor-cycle gap at most 21.

## 1. The terminal phase and its action data

Put

\[
 D_*=111000(10)^{b-1}1100,
 \qquad r=b-1,qquad m=r+5,qquad n=2r+11.
\tag{1.1}

Peak pruning gives

\[
                         \lambda(D_*)=(3,2,1^r).
\tag{1.2}

The distinct soliton sizes are `1,2,3`, with multiplicities `(r,1,1)`.
Their vacancy numbers are

\[
                         (q_1,q_2,q_3)=(7,3,1).
\tag{1.3}

The only possible internal symmetry is

\[
                         \gamma\mid\gcd(r,7).
\tag{1.4}

Thus `gamma` is either one or seven.

## 2. Exact torus translation index

For the symmetry sector `gamma`, the action--angle period matrix and PBBS
translation vector are

\[
 F_\gamma=
 \begin{pmatrix}
 (2r+7)/\gamma&2&2\\
 2r/\gamma&7&4\\
 2r/\gamma&4&7
 \end{pmatrix},
 \qquad
 h_\infty=\begin{pmatrix}1\\2\\3\end{pmatrix}.
\tag{2.1}

Its determinant is

\[
                         \Delta={21n\over\gamma}.
\tag{2.2}

Replacing columns `1,2,3` by `h_infty` gives determinants

\[
 3,qquad {2(r+7)\over\gamma},qquad
 {16r+91\over\gamma}.
\tag{2.3}

For a translation on `Z^3/F_gamma Z^3`, the number of its cycles is the
index of the cyclic subgroup it generates, namely the gcd of (2.2)--(2.3).
Since the first replacement minor is three, that index is

\[
 \boxed{\delta=\gcd(3,r+1)\in\{1,3\}.}
\tag{2.4}

Indeed division by `gamma in {1,7}` does not change residues modulo three,
and both latter minors are divisible by three exactly when `r+1` is.

Consequently every action torus in this sector contains exactly `delta`
PBBS cycles, each of length

\[
                         P={\Delta\over\delta}.
\tag{2.5}

This length is odd, so an `f`-cycle is also one `g=f^2` factor component.

## 3. Spatial rotation is transitive on the exceptional three cycles

The one-site spatial rotation is the action--angle translation

\[
                         s=(1,1,1)^T.
\tag{3.1}

When `delta=1`, the PBBS component is the entire torus and is already
rotation invariant.

Assume `delta=3`, equivalently `r=2 mod 3`.  Modulo three, every column of
`F_gamma` is congruent to `(2,1,1)^T`, while

\[
 h_\infty\equiv(1,2,0)^T.
\tag{3.2}

The linear character

\[
                         \chi(x_1,x_2,x_3)=x_1+x_2\pmod3
\tag{3.3}

annihilates all columns of `F_gamma` and annihilates `h_infty`, but

\[
                         \chi(s)=2\ne0.
\tag{3.4}

Therefore spatial rotation cyclically permutes the three PBBS cycles in
the torus.  Its cube preserves each one.

Combining both cases:

### Theorem 3.1 (rotation orbit)

Every physical component containing `D_*` contains exactly

\[
                         {n\over\delta}
\tag{3.5}

of its `n` coordinate rotations, where `delta=gcd(3,r+1)`.  The stabilizing
rotations are precisely the powers of `rho^delta`.

## 4. Constant spacing on the factor component

Inside the cyclic PBBS component of length `P`, the orbit of
`rho^delta` is the unique subgroup of order `n/delta`.  Its index, and
hence the exact gap between consecutive orbit positions in factor time,
is

\[
 {P\over n/\delta}={\Delta\over n}={21\over\gamma}le21.
\tag{4.1}

Because `P` is odd, replacing `f` by `g=f^2` only multiplies the cyclic
time coordinate by a unit; the same subgroup and the same index result.

Thus the terminal component contains a rotation copy of `D_*` in every
factor interval of length at most 21.  In particular, for all sufficiently
large `b`, it contains arbitrarily many pairwise support-separated copies,
and certainly two copies on any two factor arcs whose lengths tend to
infinity.

## 5. Consequence for terminal omissions

If the displayed phase `D_*` is equipped with its authenticated alternate
max-height q1 occurrence, each rotation supplies the rotated alternate
occurrence.  The q1 labels are distinct under nontrivial rotation because
`gcd(m,n)=1`.  Theorem 3.1 and (4.1) therefore provide a constant-gap bank
of terminal omission sites on the **same** named `J_b` component.

This closes the rotation-supply row needed to place one omission on each
of two long hybrid rails.  It does not by itself prove that a prescribed
pair of short arcs both contains a copy, nor does it audit q2 damage of
choosing the alternate occurrence; those are separate local interfaces.

