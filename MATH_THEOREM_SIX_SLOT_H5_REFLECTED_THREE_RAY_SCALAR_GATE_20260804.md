# Six-slot `h=5`: reflected three-ray geometry and a scalar outer gate

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It rewrites the
closed endpoint-defect gate for the canonical inert `h=5` branch as two
reflected complementary rays and one reflected midpoint ray.  It gives an
exact compact physical polytope and reduces positivity to one outer scalar
inequality in the period excess.  On the repeated-middle endpoint face,
the ceiling and midpoint interlace exactly to a half-period ceiling.  The
remaining scalar gate is not signed here, so complete `h=5` positivity is
not claimed.  No search or sampled computation is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad
 C(\tau)=F_\tau(0),
\tag{0.1}
\]

and write

\[
 F=F_A,
 \qquad C=C(A),
 \qquad
 \Theta(w)=F(w)+F(A-w).
\tag{0.2}
\]

The Jacobi reflection theorem gives

\[
                         |\Theta(w)|<\varepsilon,
 \qquad \varepsilon={1\over20000},
 \qquad 0\le w\le A.
\tag{0.3}
\]

Let

\[
 (0,c_1,c_2,c_3,c_4,c_5,c_6)
\tag{0.4}
\]

be a canonical inert table in the least maximum-density branch `h=5`.
The threshold face `c_6=A` is already positive.  Hence write

\[
                         c_6=A+\delta,
 \qquad 0<\delta<{A\over5}.
\tag{0.5}
\]

The frozen endpoint-defect theorem gives the literal lower comparison

\[
 \Phi\ge C(A+\delta)+\sum_{j=1}^{5}F_{A+\delta}(c_j).
\tag{0.6}
\]

## 1. Reflected physical coordinates

Set

\[
\boxed{
\begin{aligned}
 x&=c_1,&y&=c_2,\\
 m&=A-c_3,&v&=A-c_4,&u&=A-c_5.
\end{aligned}}
\tag{1.1}
\]

Thus

\[
 (c_1,c_2,c_3,c_4,c_5)
 =(x,y,A-m,A-v,A-u).
\tag{1.2}
\]

### Theorem 1.1 (exact reflected physical polytope)

For fixed `delta`, the compact closure of the physical inert `h=5`
stratum is affinely equivalent to the set
`overline D_5(delta)` of `(u,x,y,v,m)` satisfying

\[
\boxed{
 0\le u\le{A-5\delta\over6},
 \qquad
 0\le x\le u+\delta,
 \qquad
 0\le y\le {2(A-u)\over5},}
\tag{1.3}
\]

\[
\boxed{
 v\ge {A+4u\over5},
 \qquad
 m\ge {2A+3u\over5},}
\tag{1.4}
\]

\[
\boxed{
\begin{gathered}
 y\ge2x,
 \qquad m\le A-x-y,
 \qquad m\ge x+v,\\
 v\le A-2y,
 \qquad v\ge x+u,
 \qquad m\ge y+u,
\end{gathered}}
\tag{1.5}
\]

and

\[
\boxed{
\begin{gathered}
 x-u\le\delta,
 \qquad y-v\le\delta,
 \qquad A-2m\le\delta,\\
 \max\{x-u,y-v,A-2m\}=\delta.
\end{gathered}}
\tag{1.6}
\]

The three endpoint faces are

\[
\begin{array}{c|c}
\mathrm X&x-u=\delta,\\
\mathrm Y&y-v=\delta,\\
\mathrm Z&A-2m=\delta.
\end{array}
\tag{1.7}
\]

#### Proof

Put `c_5=5a`.  Since `c_5=A-u`,

\[
                         a={A-u\over5}.
\tag{1.8}
\]

The endpoint density bound `A+delta<=6a` is exactly

\[
                         6u+5\delta\le A,
\]

which gives the first inequality in (1.3).  The density bounds for
sizes two, three, and four are respectively

\[
 y\le {2(A-u)\over5},
 \qquad
 m\ge {2A+3u\over5},
 \qquad
 v\ge {A+4u\over5}.
\tag{1.9}
\]

Endpoint superadditivity gives `x<=u+delta`.  Together with
`6u+5delta<=A`, this also implies

\[
 x\le u+\delta\le {A-u\over5}=a,
\]

so the size-one density row is already present.

The six internal superadditivity rows become, in order,

\[
\begin{array}{rcl}
c_2\ge2c_1&\Longleftrightarrow&y\ge2x,\\
c_3\ge c_1+c_2&\Longleftrightarrow&m\le A-x-y,\\
c_4\ge c_1+c_3&\Longleftrightarrow&m\ge x+v,\\
c_4\ge2c_2&\Longleftrightarrow&v\le A-2y,\\
c_5\ge c_1+c_4&\Longleftrightarrow&v\ge x+u,\\
c_5\ge c_2+c_3&\Longleftrightarrow&m\ge y+u.
\end{array}
\tag{1.10}
\]

Finally, the three endpoint deficits are

\[
\begin{aligned}
 (A+\delta)-(c_1+c_5)&=\delta-(x-u),\\
 (A+\delta)-(c_2+c_4)&=\delta-(y-v),\\
 (A+\delta)-2c_3&=\delta-(A-2m).
\end{aligned}
\tag{1.11}
\]

Their nonnegativity and endpoint saturation are exactly (1.6), and their
zero sets are (1.7).  This proves necessity.

Conversely, define the table by (1.2).  Equations (1.3)--(1.4) give all
density and nonnegativity rows; (1.5) gives every internal
superadditivity row; and (1.6) gives endpoint superadditivity and
saturation.  Thus no physical row is lost.  Replacing the strict
least-maximizer and first-crossing inequalities by weak ones is precisely
the stated compact closure.  \(\square\)

## 2. Exact three-ray reflection identity

For `0<=w<=A`, define the exact period gain

\[
 D_\delta(w)=F_{A+\delta}(w)-F_A(w)\ge0.
\tag{2.1}
\]

For a reflected pair define

\[
 G_\delta(p,q)
 =F(p)-F(q)+D_\delta(p)+D_\delta(A-q),
\tag{2.2}
\]

and for the midpoint ray define

\[
 M_\delta(m)=D_\delta(A-m)-F(m).
\tag{2.3}
\]

### Theorem 2.1 (exact reflected decomposition)

Every point of `overline D_5(delta)` satisfies the identity

\[
\boxed{
\begin{aligned}
 \mathscr E_5={}&C+D_\delta(0)
 +G_\delta(x,u)+G_\delta(y,v)+M_\delta(m)\\
 &+\Theta(u)+\Theta(v)+\Theta(m),
\end{aligned}}
\tag{2.4}
\]

where `mathscr E_5` is the literal endpoint-period expression in (0.6).

#### Proof

For any reflected pair `(p,A-q)`, equations (0.2), (2.1), and (2.2)
give

\[
 F_{A+\delta}(p)+F_{A+\delta}(A-q)
 =G_\delta(p,q)+\Theta(q).
\tag{2.5}
\]

Apply this to `(p,q)=(x,u)` and `(y,v)`.  For the middle shift,

\[
\begin{aligned}
 F_{A+\delta}(A-m)
 &=F(A-m)+D_\delta(A-m)\\
 &=\Theta(m)-F(m)+D_\delta(A-m)\\
 &=\Theta(m)+M_\delta(m).
\end{aligned}
\tag{2.6}
\]

Finally `C(A+delta)=C+D_delta(0)`.  Adding the three identities proves
(2.4).  \(\square\)

## 3. One outer scalar gate

Define the exact correlated inner envelope

\[
\boxed{
 \Gamma_5(\delta)=
 \inf_{(u,x,y,v,m)\in\overline{\mathcal D}_5(\delta)}
 \left\{G_\delta(x,u)+G_\delta(y,v)+M_\delta(m)\right\}.}
\tag{3.1}
\]

### Theorem 3.1 (reflected scalar reduction)

Every physical inert `h=5` table satisfies

\[
\boxed{
 \Phi>
 C+D_\delta(0)+\Gamma_5(\delta)-3\varepsilon.}
\tag{3.2}
\]

Consequently the complete inert branch is positive if

\[
\boxed{
 C+D_\delta(0)+\Gamma_5(\delta)>3\varepsilon
 \qquad(0<\delta<A/5).}
\tag{3.3}
\]

#### Proof

The endpoint-period theorem gives `Phi>=mathscr E_5`.  Apply (2.4), use
each strict bound `Theta> -epsilon`, and then take the correlated infimum
over the single physical polytope.  This gives (3.2), and (3.3) is
immediate.  \(\square\)

The point of (3.1) is not merely notation.  All three reflected losses
remain coupled by (1.3)--(1.6); in particular one of the three endpoint
differences equals `delta`.  Minimizing the two pairs and the midpoint
separately would be an invalid relaxation.

## 4. Exact collapse of the repeated-middle face

On face `Z`, equation (1.7) gives

\[
                         m={A-\delta\over2},
 \qquad c_3={A+\delta\over2}.
\tag{4.1}
\]

The even and odd half-period classes interlace exactly:

\[
\boxed{
 C(A+\delta)+F_{A+\delta}\left({A+\delta\over2}\right)
 =C\left({A+\delta\over2}\right).}
\tag{4.2}
\]

Hence the literal face-`Z` expression reduces to

\[
\boxed{
\begin{aligned}
 \mathscr E_{5,Z}={}&C\left({A+\delta\over2}\right)\\
 &+F_{A+\delta}(x)+F_{A+\delta}(A-u)\\
 &+F_{A+\delta}(y)+F_{A+\delta}(A-v).
\end{aligned}}
\tag{4.3}
\]

This is an exact face-specific simplification, not a bound.  It removes
the midpoint variable and the separate ceiling allocation simultaneously.

## 5. Exact scope

The theorem proves:

1. an exact reflected-coordinate description of the compact physical
   closure;
2. an exact two-pair/one-midpoint reflection identity;
3. a single outer scalar sufficient gate in `delta`;
4. exact half-period interlacing on the repeated-middle face.

It does not sign `Gamma_5`, close any inert face, prove complete six-slot
positivity, extend to arbitrary grid size, or prove an OR-word result.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| exact endpoint-defect reduction | `MATH_THEOREM_SIX_SLOT_H5_ENDPOINT_DEFECT_POLYTOPE_AND_CORRELATED_GATE_20260804.md` | `4a751598067165d88cd1e01e0406c3dce09c941cbba7fa0dd95487d0ff3e4b59` |
| period gain and exact reflected-pair identity | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |
| Jacobi reflection and theta bound | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
