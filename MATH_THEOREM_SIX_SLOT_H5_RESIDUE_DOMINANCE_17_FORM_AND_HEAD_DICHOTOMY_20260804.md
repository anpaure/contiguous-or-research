# Six-slot `h=5`: thirteen Apéry forms and the unique long-head chamber

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It replaces the
sixty-four formal simple-path expressions in the six-slot `h=5` branch by
thirteen sufficient envelope expressions.  It also shortens the exact
availability head from `m<24` to `m<16` on the `c_1+c_5` endpoint face,
and to `m<18` on the other inert endpoint faces.  It identifies one strict
threshold chamber as the only place where a head through `m=23` can still
be necessary.  It does **not** sign the resulting functional or prove
complete six-slot positivity.

Let

\[
 (c_0,c_1,\ldots,c_6),\qquad c_0=0,
\]

be a canonical first-crossing, endpoint-saturated six-slot table assigned
to the least maximum-density branch `h=5`.  Put

\[
 P=c_5,\qquad \lambda={P\over5},
\tag{0.1}
\]

and use the eventual best step of each nonzero residue modulo five:

\[
\begin{aligned}
 d_1&=c_6-P-{P\over5}=c_6-{6P\over5},\\
 d_2&=c_2-{2P\over5},\\
 d_3&=c_3-{3P\over5},\\
 d_4&=c_4-{4P\over5}.
\end{aligned}
\tag{0.2}
\]

The residue-one step in (0.2) is denomination six.  It dominates the
congruent denomination-one step because `c_6>=P+c_1`.  Maximum density
gives

\[
                         d_1,d_2,d_3,d_4\le0.
\tag{0.3}
\]

For residue `r`, let `beta_r` be the maximum reduced weight of a simple
path from zero to `r` in `Z/5Z`.

## 1. Four inequalities forced by superadditivity

### Lemma 1.1

Every table above satisfies

\[
\boxed{
 d_4\ge2d_2,qquad
 d_1\ge2d_3,qquad
 d_1\ge d_2+d_4,qquad
 d_2+d_3\le0.
}
\tag{1.1}
\]

#### Proof

The four inequalities are exactly the reduced forms of

\[
 c_4\ge2c_2,qquad
 c_6\ge2c_3,qquad
 c_6\ge c_2+c_4,qquad
 P=c_5\ge c_2+c_3.
\]

In each equality the linear density terms sum to the same multiple of
`P/5`, so subtracting them gives (1.1). \(\square\)

This is the reusable principle behind the reduction: whenever an
ordinary-capacity sum stays within the displayed table, superadditivity
becomes a triangle inequality for reduced residue weights.

## 2. The thirteen-form theorem

### Theorem 2.1

The four stabilized Apéry weights are exactly

\[
\boxed{
\begin{aligned}
 \beta_1={}&\max\{d_1,\ 4d_4\},\\
 \beta_2={}&\max\{d_2,\ 2d_1,\ d_3+d_4,\ 3d_4\},\\
 \beta_3={}&\max\{d_3,\ d_1+d_2,\ 2d_4,\ 3d_1\},\\
 \beta_4={}&\max\{d_4,\ d_1+d_3,\ 4d_1\}.
\end{aligned}}
\tag{2.1}
\]

Thus only thirteen linear forms are needed for the exact envelope of the
sixty-four path words.

#### Proof

A simple path to a fixed nonzero residue has zero, one, two or three
intermediate nonzero vertices.  After identifying path words with the
same commutative weight, their raw forms are as follows.

For residue one they are

\[
\begin{gathered}
 d_1, d_2+d_4, 2d_3,\\
 d_1+d_2+d_3, 3d_2, d_3+2d_4,\\
 2d_1+2d_2, 2d_2+d_3+d_4,
 d_1+2d_3+d_4, 4d_4.
\end{gathered}
\tag{2.2}
\]

The inequalities (0.3) and (1.1) bound every expression in (2.2), except
`d_1`, `d_3+2d_4`, and `4d_4`, by `d_1`.  For example,

\[
 3d_2\le d_2+d_4\le d_1,qquad
 2d_2+d_3+d_4=(d_2+d_4)+(d_2+d_3)\le d_1.
\]

The remaining middle expression is redundant in the maximum.  If
`d_3<=2d_4`, then `d_3+2d_4<=4d_4`; if `d_3>=2d_4`, then
`d_3+2d_4<=2d_3<=d_1`.  This gives the two residue-one forms in
(2.1).

For residue two the raw distinct forms are

\[
\begin{gathered}
 d_2, 2d_1, d_3+d_4,\\
 d_1+d_2+d_4, d_1+2d_3, 3d_4,\\
 2d_1+d_2+d_3, d_1+d_3+2d_4,
 4d_3, 2d_2+2d_4.
\end{gathered}
\tag{2.3}
\]

Here

\[
\begin{aligned}
 d_1+d_2+d_4&\le2d_1,&
 d_1+2d_3&\le2d_1,\\
 2d_1+d_2+d_3&\le2d_1,&
 2d_2+2d_4&\le2d_1,
\end{aligned}
\]

while

\[
 d_1+d_3+2d_4\le d_3+d_4,
 \qquad
 4d_3\le2d_1.
\]

This leaves the four residue-two forms in (2.1).  The second additional
domination is the doubled form of `d_1>=2d_3`.

For residue three the raw distinct forms are

\[
\begin{gathered}
 d_3, d_1+d_2, 2d_4,\\
 3d_1, d_1+d_3+d_4, 2d_2+d_4,\\
 2d_1+d_2+d_4, 2d_1+2d_3,
 d_2+d_3+2d_4, 4d_2.
\end{gathered}
\tag{2.4}
\]

The last five nonsurviving forms obey

\[
\begin{aligned}
 2d_2+d_4&\le2d_4,\\
 2d_1+d_2+d_4&\le3d_1,\\
 2d_1+2d_3&\le3d_1,\\
 d_2+d_3+2d_4&\le2d_4,\\
 4d_2&\le2d_4.
\end{aligned}
\]

Finally,

\[
 d_1+d_3+d_4\le d_3
\]

because `d_1,d_4<=0`.  This leaves the four residue-three forms in
(2.1).

Finally, for residue four the raw forms are

\[
\begin{gathered}
 d_4, d_1+d_3, 2d_2,\\
 2d_1+d_2, d_2+d_3+d_4, 3d_3,\\
 4d_1, d_1+2d_2+d_4,
 d_1+d_2+2d_3, 2d_3+2d_4.
\end{gathered}
\tag{2.5}
\]

One has

\[
\begin{aligned}
 2d_2&\le d_4,&
 d_2+d_3+d_4&\le d_4,&
 3d_3&\le d_1+d_3,\\
 d_1+2d_2+d_4&\le2d_1+d_2,&
 d_1+d_2+2d_3&\le2d_1+d_2,&
 2d_3+2d_4&\le d_4.
\end{aligned}
\]

Of the remaining four expressions, `2d_1+d_2` is redundant in the
maximum.  If `d_2<=2d_1`, then `2d_1+d_2<=4d_1`; if
`d_2>=2d_1`, then `2d_1+d_2<=2d_2<=d_4`.  The other three
expressions are exactly the residue-four line of (2.1).  This exhausts
all simple paths and proves the theorem. \(\square\)

## 3. Exact availability capacities

Each form in (2.1) has the following simple realizing word.  A symbol
`1` in the first column means the residue-one denomination six, not the
original denomination one.

\[
\begin{array}{c|c|c|c}
 r&\text{form}&\text{step denominations}&\text{ordinary capacity}\\ \hline
1&d_1&(6)&6\\
1&4d_4&(4,4,4,4)&16\\ \hline
2&d_2&(2)&2\\
2&2d_1&(6,6)&12\\
2&d_3+d_4&(3,4)&7\\
2&3d_4&(4,4,4)&12\\
\hline
3&d_3&(3)&3\\
3&d_1+d_2&(6,2)&8\\
3&2d_4&(4,4)&8\\
3&3d_1&(6,6,6)&18\\
\hline
4&d_4&(4)&4\\
4&d_1+d_3&(6,3)&9\\
4&4d_1&(6,6,6,6)&24
\end{array}
\tag{3.1}
\]

Every listed residue walk is simple.  Thus the only surviving form whose
first availability exceeds eighteen is `4d_1`, and it occurs only in
`beta_4`.

For cutoff purposes we also retain the redundant residue-four path

\[
 2d_1+d_2\quad\hbox{realized by }(6,6,2)
 \quad\hbox{at capacity }14.
\tag{3.1a}
\]

It never changes the stabilized envelope, because it is at most
`max{d_4,4d_1}`, but equality with `4d_1` can supply a short realizing
path.  This is why it legitimately remains in the cutoff criterion
(4.4).

Let

\[
 s_r={rP\over5}+\beta_r,
 \qquad
 \widehat V_{5q+r}=qP+s_r.
\tag{3.2}
\]

Universally, (3.1) recovers the exact canonical expression

\[
 \Phi=\mathcal L_5(P;s_1,s_2,s_3,s_4)
       +\sum_{m=0}^{23}\{K(V_m)-K(\widehat V_m)\}.
\tag{3.3}
\]

The next section shows when the final six head positions are unnecessary.

## 4. Endpoint-face shortening

Endpoint saturation says

\[
 c_6=\max\{A,c_1+P,c_2+c_4,2c_3\}.
\tag{4.1}
\]

### Theorem 4.1

The exact availability cutoff can be chosen as follows.

1. On the face `c_6=c_1+P`, every eventual path is available by ordinary
   capacity sixteen.  Hence

   \[
   \boxed{
   \Phi=\mathcal L_5(P;s_1,s_2,s_3,s_4)
       +\sum_{m=0}^{15}\{K(V_m)-K(\widehat V_m)\}.}
   \tag{4.2}
   \]

2. On either face `c_6=c_2+c_4` or `c_6=2c_3`, every eventual maximum
   has a realizing path of capacity at most eighteen.  Hence

   \[
   \boxed{
   \Phi=\mathcal L_5(P;s_1,s_2,s_3,s_4)
       +\sum_{m=0}^{17}\{K(V_m)-K(\widehat V_m)\}.}
   \tag{4.3}
   \]

3. More generally, (4.3) holds whenever

   \[
                         4d_1\le
       \max\{d_4,d_1+d_3,2d_1+d_2\}.
   \tag{4.4}
   \]

#### Proof

On `c_6=c_1+P`, the original denomination-one reduced weight

\[
                         c_1-{P\over5}
\]

equals `d_1`.  Therefore every residue-one step in (3.1) may use ordinary
denomination one instead of denomination six.  Replacing all such steps
reduces the maximum capacity in (3.1) to sixteen, attained by the word
`(4,4,4,4)`.  This proves (4.2).

On `c_6=c_2+c_4`, one has

\[
                         d_1=d_2+d_4\le d_4.
\]

Since `d_1<=0`, it follows that `4d_1<=d_4`; the capacity-twenty-four
form cannot be the sole maximizer in `beta_4`.

On `c_6=2c_3`, one has `d_1=2d_3`, and hence

\[
                         4d_1=8d_3\le3d_3=d_1+d_3.
\]

Again the long form is dominated.  In either case, every surviving
maximizer has a realization of capacity at most eighteen by (3.1), proving
(4.3).  The same argument proves the general assertion (4.4). \(\square\)

### Corollary 4.2 (the unique possible long-head chamber)

A head extending through `m=23` can be necessary only if

\[
\boxed{
\begin{gathered}
 c_6=A>\max\{c_1+P,c_2+c_4,2c_3\},\\
 4d_1>\max\{d_4,d_1+d_3,2d_1+d_2\}.
\end{gathered}}
\tag{4.5}
\]

#### Proof

If an inert endpoint equality holds, Theorem 4.1 gives cutoff sixteen or
eighteen.  If no inert equality holds, endpoint saturation (4.1) forces
the first strict line of (4.5).  Finally, if the second strict line fails,
(4.4) gives cutoff eighteen. \(\square\)

Thus every `h=5` point outside the explicit chamber (4.5) has an exact
head of length at most eighteen, and the entire `c_1+c_5` face has length
at most sixteen.

## 5. Reusable residue-path principle

The proof did not use a special analytic property of `K`.  Its reusable
content for the `h=3` and `h=4` branches is:

> Translate every internally superadditive relation whose ordinary
> capacities sum within the six-slot table into a reduced-weight triangle
> inequality before taking the maximum over simple residue paths.

This can eliminate formal Apéry chambers and can shorten an availability
head even when it does not sign the remaining Gaussian train.  It must be
applied before analytic deformation toward an affine gap pattern; otherwise
the deformation carries many path forms which can never be maximal.

## 6. Frozen dependencies and scope

| role | file | SHA-256 |
|---|---|---|
| canonical six-slot branch and exact 64-form/head representation | `MATH_THEOREM_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `3b537980a6f18aae936979335cc6756079ff10b92a80019acf3a97df8be9bede` |
| independent audit of the canonical representation | `MATH_AUDIT_SIX_SLOT_CANONICAL_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_INDEPENDENT_20260804.md` | `fae9fe02688d666e956619abe40698791a4146004a59a483893d0634ebbe3006` |

No numerical search, remote computation, or external theorem is used.
The result is an exact structural reduction, not a positivity proof.  It
does not close the affine complement, the strict threshold chamber (4.5),
the `h=3` or `h=4` branches, complete six-slot positivity, or any
router/common-cap statement.
