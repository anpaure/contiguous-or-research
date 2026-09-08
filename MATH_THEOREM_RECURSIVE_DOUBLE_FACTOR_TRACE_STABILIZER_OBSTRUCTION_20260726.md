# Recursive affine double factors and the exact trace-stabilizer obstruction

Date: 2026-07-26

Method: pure mathematics only.

> **Scope.**  Every fibre computation in this note is for the augmented
> code carrying `J`.  A collision with the same tag is a literal target
> collision, so all lower bounds survive after forgetting `J`.  Positive
> augmented-code injectivity would not by itself imply literal OR
> injectivity.

## 0. Outcome

The affine complete-mapping certificate on `Q_4` does recurse.  There is
an explicit parity-alternating product which carries a same-vertex double
factor

\[
                 \delta _1(y)=S\delta _0(y)
\tag{0.1}
\]

on `Q_r` to one on `Q_(2r)`, with coordinate permutation `S\oplus S`.
Starting from the displayed factors with words `1234 1234` and
`1432 1432` therefore gives double factors at every dimension

\[
                         r=4\,2^t.
\tag{0.2}
\]

This recursion does **not** make the affine trace code near-injective.
There are two exact obstructions.

1.  For the orientation in
    `MATH_THEOREM_DOUBLE_FACTOR_AFFINE_PARITY_COMPLETE_MAPPING_20260726.md`,
    the permutation `S=(2 4)` fixes half the coordinates at every scale.
    At every growing aligned depth `d`, the collision excess is at least

    \[
     \left({d-2\over2(d-1)}\right)
     \left(1-2^{1-d}\right)2^{2r-1}
       =\left({1\over2}-o(1)\right)2^{2r-1}.
    \tag{0.3}
    \]

    Moreover at least one third of all coarse phase states lie in
    same-phase trace fibres of multiplicity at least

    \[
                         2^{\lceil d/4\rceil-1}.
    \tag{0.4}
    \]

2.  Independently of fixed coordinates, the recursive outgoing-direction
    rule has an exact translation stabilizer of dimension `r/2`.  Every
    nonempty aligned depth-`d` trace fibre consequently has cardinality at
    least

    \[
             \boxed{2^{\max\{0,\,2d-r/2-1\}}}.       \tag{0.5}
    \]

    In particular half-depth fibres have multiplicity at least
    `2^(r/2-1)`, and their collision excess is at least

    \[
            2^{2r-1}\left(1-2^{1-r/2}\right).        \tag{0.6}
    \]

The finite seed itself gives no reduction in total trace multiplicity.
At coarse depths `d=1,2,3,4`, its nonempty fibre sizes are exactly

\[
                         1,\ 2,\ 8,\ 128,             \tag{0.7}
\]

the same values obtained from the context-independent lift of the same
`Q_4` factor.

There is a useful scope correction.  Reversing the second `Q_4` factor
changes (0.1) to the fixed-point-free relation

\[
                   S^\dagger=(1\ 2)(3\ 4).           \tag{0.8}
\]

This relation also recurses, so it escapes (0.3).  It does not escape the
stabilizer bound (0.5).  Thus an inverse orientation can only remain a
candidate when the protected depth is at most `r/4+O(1)`.  Escaping the
audited obstruction requires a recursion which destroys the inherited
half-dimensional translation stabilizer; extra phase shifts or common
coordinate relabellings do not do so.

## 1. The parity-alternating recursive double factor

Let `H` be a neighbour permutation of `Q_r`, all of whose components are
isometric `C_(2r)`'s.  Define a neighbour map on
`Q_(2r)=Q_r^L square Q_r^R` by

\[
 {\cal R}(H)(u,v)=
 \begin{cases}
   (H(u),v),&|u|+|v|\equiv0\pmod2,\\
   (u,H(v)),&|u|+|v|\equiv1\pmod2.
 \end{cases}                                         \tag{1.1}
\]

### Lemma 1.1 (recursive isometric factor)

`R(H)` is a neighbour permutation of `Q_(2r)`, and all its components are
isometric `C_(4r)`'s.

#### Proof

Every move of `H` changes Hamming parity.  Hence the two clauses in
(1.1) alternate, and, irrespective of the parity of the initial state,

\[
                {\cal R}(H)^{2s}(u,v)=(H^su,H^sv).   \tag{1.2}
\]

The right side first returns to `(u,v)` when `s` is a multiple of `2r`,
so every orbit of `R(H)` has length `4r`.  During its first `2r` moves it
uses `r` consecutive directions of the `H`-cycle through `u` and `r`
consecutive directions of the `H`-cycle through `v`, alternately.  Each
parent list contains every parent coordinate exactly once.  Thus the
first `2r` directions form a permutation of all `2r` child coordinates;
the next `2r` directions repeat it.  The doubled-permutation criterion
proves isometry.  Formula (1.2), or the two alternating bijections in
(1.1), also proves that `R(H)` is a permutation.  \(\square\)

### Lemma 1.2 (double-factor recursion)

Suppose neighbour permutations `G_0,G_1` on `Q_r` satisfy (0.1).  Then

\[
 {\cal G}_j={\cal R}(G_j),\qquad
 {\cal S}=S_L\oplus S_R                              \tag{1.3}
\]

satisfy

\[
                    \delta_{{\cal G}_1}(u,v)
       ={\cal S}\,\delta_{{\cal G}_0}(u,v)           \tag{1.4}
\]

at every common vertex `(u,v)`.

#### Proof

The parity test selecting the left or right child in (1.1) depends only
on the common vertex, not on `j`.  On the selected child, (0.1) changes
the outgoing parent direction by `S`.  This is exactly the action of
`S_L\oplus S_R` on the selected child direction.  \(\square\)

Starting with the two audited `Q_4` factors and iterating Lemma 1.2 gives
the promised recursive double factor.  Applying the affine complete-
mapping lemma at every scale then gives an exact pair-clustered factor on
`Q_(2r)`.

## 2. An exact fibre formula for every affine double factor

Let `G_0,G_1,S` satisfy (0.1), and use the affine construction

\[
 y=Sp+x,\qquad F_p(x)=x+e_{\delta _0(y)},qquad p\in E.       \tag{2.1}
\]

For `1<=d<=r`, let `J_d(y)` be the set of the first `d` directions on the
`G_0`-trajectory from `y`.  The aligned trace code is

\[
 {\cal C}_d(p,x)=
       \bigl(J_d(y),x|_{J_d(y)^c},p|_{J_d(y)^c}\bigr).       \tag{2.2}
\]

### Lemma 2.1 (same-phase affine fibre)

Fix `y`, put `J=J_d(y)`, and set

\[
                         K=J\cap S^{-1}J.             \tag{2.3}
\]

As `p` ranges over the even shore and `x=y+Sp`, every nonempty fibre of
the code (2.2), restricted to this fixed `y`, has exactly

\[
                 \boxed{2^{\max\{|K|-1,0\}}}         \tag{2.4}
\]

members.

#### Proof

Let two contexts differ by `z=p+p'`.  Equality of the recorded outside
parts of `p` says `supp(z) subseteq J`.  Since

\[
                         x+x'=Sz,                    \tag{2.5}
\]

equality of the recorded outside parts of `x` says
`supp(Sz) subseteq J`, or `supp(z) subseteq S^{-1}J`.  Finally both
contexts are even exactly when `z` has even weight.  Thus the differences
inside one fibre are precisely the even vectors supported on `K`.  There
is one such vector if `|K|=0` or `1`, and `2^(|K|-1)` otherwise.  \(\square\)

This formula identifies exactly what the affine complete mapping can and
cannot encode: only coordinates moved out of the erased set by `S` are
made visible in the recorded outside orientation.

The same lemma and all collision bounds below hold for the reverse
aligned code: replace the forward `G_0` trajectory by the `G_0^{-1}`
trajectory.  Translation stabilizers and the fixed-coordinate count are
unchanged.

## 3. Exact trace multiplicities of the `Q_4` seed

For the displayed `Q_4` factor, the translation stabilizer of the
outgoing-direction rule is

\[
 L=\langle0101,1010\rangle.                          \tag{3.1}
\]

Equivalently, put

\[
 \alpha(y)=y_2+y_4,qquad \beta(y)=y_1+y_3.          \tag{3.2}
\]

The four directions `1,2,3,4` correspond respectively to

\[
                 (\alpha,\beta)=(0,0),(0,1),(1,1),(1,0).     \tag{3.3}
\]

For `d<4`, the cyclic `d`-set in the order `1234` determines its first
direction.  Fixing a trace therefore fixes the two equations (3.2), with
`y=Sp+x`, as well as the parity equation on `p`.

### Proposition 3.1 (complete seed trace table)

For the affine seed with `S=(2 4)`, the forward aligned code has the
following exact data:

\[
\begin{array}{c|c|c|c}
d&\text{unknown inside bits}&\text{independent equations}
 &\text{nonempty fibre size}\\ \hline
1&2&2&1\\
2&4&3&2\\
3&6&3&8\\
4&8&1&128.
\end{array}                                           \tag{3.4}
\]

Consequently the image sizes are respectively

\[
                         128,\ 64,\ 16,\ 1.           \tag{3.5}
\]

The reverse aligned code has the same values.

#### Proof

At `d=1`, parity fixes the missing context bit, and exactly one of
`alpha,beta` contains the missing `x` bit; it fixes that bit.  At `d=2`,
every cyclic two-set contains one coordinate from `{1,3}` and one from
`{2,4}`.  Hence the two equations in (3.2) and parity are independent.
They remain independent at `d=3`.  This gives ranks `2,3,3` on the
respective `2d` unknown bits.

At `d=4`, the set `J=[4]` does not record the initial direction and there
are no outside bits.  The code is constant on all
`|E|2^4=8*16=128` starts.  Reversing the cyclic order changes none of the
rank calculations.  \(\square\)

The identical calculation with `y=x`, namely the context-independent
lift, gives the same ranks and the same four fibre sizes.  Thus the
nonconstant affine seed reduces some *fixed-`y` parity fibres* in Lemma
2.1, but it does not reduce the total physical trace multiplicity at any
depth of the seed.

For reference, Lemma 2.1 gives the fixed-`y` intersection sizes

\[
\begin{array}{c|c}
d&|J\cap S^{-1}J|\\ \hline
1&0\text{ or }1\\
2&1\\
3&2\text{ or }3\\
4&4.
\end{array}                                           \tag{3.6}
\]

## 4. The fixed-coordinate obstruction at every scale

Let `Fix(S)` have size `f`.  For a phase state `y`, set

\[
 a(y)=|J_d(y)\cap\operatorname {Fix}(S)|.             \tag{4.1}
\]

Since every fixed coordinate belonging to `J` also belongs to
`S^{-1}J`, Lemma 2.1 gives same-phase fibre size at least

\[
                         2^{\max\{a(y)-1,0\}}.        \tag{4.2}
\]

### Lemma 4.1 (exact average fixed content)

For any factor of `Q_r` into isometric `C_(2r)`'s,

\[
                 {1\over2^r}\sum_{y\in Q_r}a(y)
                         ={df\over r}.                \tag{4.3}
\]

#### Proof

On one component the direction word is `pi pi`.  A fixed coordinate
occurs twice around the `2r` cyclic starts, and each occurrence belongs
to exactly `d` of the length-`d` windows.  Its total contribution on the
component is therefore `2d`.  Summing over the `f` fixed coordinates and
then over all components proves (4.3).  \(\square\)

For the audited orientation, `S=(2 4)` has `f=2`.  Under Lemma 1.2,
`S_t` is a direct sum of `2^t` copies of `S`, so at dimension
`r=4*2^t` it has exactly `r/2` fixed coordinates.  Common coordinate
relabeling merely conjugates `S_t` and does not change this count.

### Theorem 4.2 (linear collision excess from fixed directions)

Suppose `S` fixes exactly `r/2` coordinates.  For every `2<=d<=r`, the
collision excess of (2.2) is at least

\[
 \boxed{
 {d-2\over2(d-1)}(1-2^{1-d})\,2^{2r-1}.}             \tag{4.4}
\]

Also, at least one third of all `y` satisfy

\[
 a(y)\ge d/4,                                        \tag{4.5}
\]

and hence lie in same-`y` fibres of multiplicity at least
`2^(ceil(d/4)-1)`.

#### Proof

By Lemma 4.1, the mean of `a(y)` is `d/2`.  Put

\[
 g(k)=
 \begin{cases}0,&k=0,1,\\1-2^{1-k},&2<=k<=d.
 \end{cases}                                         \tag{4.6}
\]

For fixed `y`, `g(a(y))` is a lower bound for the fraction of its
`2^(r-1)` even-context starts lost to collisions already within that
one `y`-slice.  On the integer interval `[1,d]`, `g` is concave.  It lies
above the chord joining `(1,0)` to `(d,1-2^(1-d))`.  Since its value at
zero is also zero, the lower convex envelope at mean `d/2` gives

\[
 {1\over2^r}\sum_y g(a(y))
 \ge {d/2-1\over d-1}(1-2^{1-d}).                    \tag{4.7}
\]

Codes coming from different `y`-slices may merge, but such merging only
increases global collision excess.  Multiplying (4.7) by `2^(2r-1)`
proves (4.4).

If a proportion `rho` of the `y`'s have `a(y)>=d/4`, then

\[
 d/2=\mathbb E a\le \rho d+(1-\rho)d/4,
\]

so `rho>=1/3`.  Equation (4.2) proves the multiplicity assertion.  \(\square\)

Thus the original affine seed cannot become near-injective under the
recursive double-factor relation, even when the protected depth is
`o(r)`.  This conclusion is not the old fixed-common-order count: it
allows arbitrary component-dependent recursive orders and uses only the
same-vertex permutation inherited by exact ownership.

## 5. The half-dimensional phase stabilizer

Let `Stab(delta)` denote the translation stabilizer of an outgoing-
direction function:

\[
 \operatorname {Stab}(\delta)
 =\{w\in Q_r:\delta(y+w)=\delta(y)\text{ for every }y\}.      \tag{5.1}
\]

The base stabilizer is the two-dimensional, even-weight space `L` in
(3.1).

### Lemma 5.1 (exact stabilizer recursion)

If every vector in `Stab(delta_H)` has even weight, then

\[
 \operatorname {Stab}(\delta_{{\cal R}(H)})
 =\operatorname {Stab}(\delta_H)
       \oplus\operatorname {Stab}(\delta_H).         \tag{5.2}
\]

Consequently, after `t` recursions from the `Q_4` seed,

\[
                   L_t=L^{\oplus2^t},\qquad
                   \dim L_t=r/2,                    \tag{5.3}
\]

and every vector of `L_t` has even weight.

#### Proof

Translation by `(a,b)` preserves the selected child in (1.1) if and only
if `|a|+|b|` is even.  Once the selected child is preserved, equality of
the outgoing directions for every `(u,v)` is equivalent separately to
`a,b in Stab(delta_H)`.  Under the hypothesis these two vectors are both
even, so the parity condition is automatic.  This proves (5.2).  The
base identity and induction give (5.3).  \(\square\)

Translation invariance of the outgoing direction propagates along the
whole orbit:

\[
 H(y+w)=H(y)+w,qquad
 H^s(y+w)=H^s(y)+w\quad(w\in\operatorname {Stab}(\delta_H)).  \tag{5.4}
\]

In particular `J_d(y+w)=J_d(y)` for every depth.

Both coordinate permutations used here preserve the base stabilizer:

\[
                  S L=L,
 \qquad            S^\dagger L=L.                    \tag{5.4a}
\]

The same is true after every direct-sum recursion.

### Proposition 5.2 (exact recursive factor-type multiplicity)

At dimension `r=4*2^t`, for either `S_t` or `S_t^dagger`, the
`2^(r-1)` even contexts in the affine construction use exactly

\[
                         2^{r/2-1}                    \tag{5.4b}
\]

distinct coarse neighbour permutations, each repeated on exactly

\[
                         2^{r/2}                      \tag{5.4c}
\]

contexts.

#### Proof

For even contexts `p,p'`, equality of their outgoing-direction functions
is equivalent to

\[
 \delta_t(S_tp+x)=\delta_t(S_tp'+x)\quad\hbox{for every }x.
\]

By the exact stabilizer identity (5.3), this is equivalent to
`S_t(p+p') in L_t`.  Equation (5.4a) makes this equivalent to
`p+p' in L_t`.  The space `L_t` has dimension `r/2` and lies in the
even shore.  Its cosets in the `(r-1)`-dimensional even shore are exactly
the factor-type fibres, proving (5.4b)--(5.4c).  \(\square\)

This is an exact exponential phase-library degeneracy, not merely an
upper bound.  The next theorem determines when that degeneracy must
survive the outside bits recorded by a physical trace.

### Theorem 5.3 (stabilizer trace bound)

Let the outgoing-direction function of `G_0` have a linear translation
stabilizer `L_0` of dimension `ell`.  Then every nonempty fibre of the
affine trace code (2.2) has cardinality at least

\[
                  2^{\max\{0,\,2d-(r-\ell)-1\}}.      \tag{5.5}
\]

For the recursive `Q_4` double factor, `ell=r/2`, giving (0.5).

#### Proof

Fix one input `(p,x)`, its set `J`, and write `y=Sp+x`.  Consider
perturbations

\[
 p'=p+z,\qquad x'=x+u,qquad z,u\in Q_J.             \tag{5.6}
\]

They preserve the recorded outside restrictions.  They preserve even
context precisely when `|z|` is even.  Finally

\[
                    y'=y+Sz+u.                       \tag{5.7}
\]

If `Sz+u in L_0`, (5.4) shows that the complete direction trajectory,
and hence `J`, is unchanged.  Thus all solutions of

\[
 |z|=0\pmod2,qquad Sz+u\in L_0                    \tag{5.8}
\]

lie in the same trace fibre.

There are `2d` binary variables in `(z,u)`.  The quotient equation
`Sz+u in L_0` imposes at most `r-ell` independent equations, and parity
imposes at most one more.  The solution space therefore has dimension at
least `2d-(r-ell)-1`; when this number is negative the zero perturbation
still gives one solution.  This proves (5.5).  \(\square\)

At `ell=r/2,d=r/2`, (5.5) gives fibre size at least `2^(r/2-1)` at every
trace.  Dividing the total number `2^(2r-1)` of aligned starts by this
minimum fibre size gives the image bound and collision excess (0.6).

This theorem also quantifies the phrase “phase-shift only.”  At scale
`r`, the complete recursive direction trajectory factors through the
quotient `Q_r/L_t`, which contains only `r/2` bits.  Coordinate phase
shifts cannot turn those `r/2` syndrome bits into the `2d` independent
inside bits erased by a depth-`d` physical trace once `d>r/4+O(1)`.

## 6. The inverse orientation and the exact remaining boundary

Let `c(y)` be the common phase in the displayed `Q_4` tables.  The
outgoing directions of `G_1^{-1}` at phases `0,1,...,7` are

\[
                         2,1,4,3,2,1,4,3.             \tag{6.1}
\]

Compared owner by owner with the `G_0` sequence
`1,2,3,4,1,2,3,4`, this gives

\[
 \delta_{G_1^{-1}}(y)=S^\dagger\delta_{G_0}(y),
 \qquad S^\dagger=(1\ 2)(3\ 4).                    \tag{6.2}
\]

Thus the affine complete-mapping lemma applies equally to
`(G_0,G_1^{-1},S^dagger)`.  Lemma 1.2 recursively carries it to
`S_t^dagger=(S^dagger)^(oplus 2^t)`, which has no fixed coordinate.
This proves that the fixed-point obstruction in Section 4 is specific to
the orientation used in the named theorem, not to every possible
orientation of the two owner factors.

However, the affine lift still uses the same `G_0` trajectory, whose
stabilizer is `L_t`.  Therefore Theorem 5.3 applies unchanged.  Common
coordinate relabelings conjugate `L_t` but preserve its dimension; direct
tensoring and the recursion (1.1) add its dimensions.  Neither operation
can remove (0.5).

The rigorous boundary is therefore:

* the original orientation is excluded at every growing protected depth
  by Theorem 4.2;
* the fixed-point-free inverse orientation is excluded whenever the
  protected coarse depth exceeds `r/4+omega(1)`;
* for `d<=r/4`, this note does not rule out the inverse orientation;
* a successful recursive double factor must replace the base direction
  rule, or introduce a genuinely non-product trade, so that its
  translation stabilizer has codimension at least `2d+omega(1)` at the
  protected depths.

No coefficient-one conclusion is claimed.
