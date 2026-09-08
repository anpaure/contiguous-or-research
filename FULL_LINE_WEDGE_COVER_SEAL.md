# The full-line wedge-cover seal

## 1. Outcome

The zero-gap, edge-mass-three branch of the mixed-profile three-box
relaxation is impossible with a uniform margin.  More precisely, every
full-line-realizable limiting ledger in this branch satisfies

\[
\boxed{U(1^+)\le {15\over4}.}                               \tag{1.1}
\]

The proof uses the lines of **all** selected plateaux, not merely the
absorbed successors.  This is exactly the information omitted by the local
counterexample in `LOCAL_ABSORPTION_COUNTEREXAMPLE.md`.

## 2. Almost-full plateau edge mass forces an almost line cover

Let

\[
H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                 |x|,|y|,|z|\le a\},
\]

so

\[
|H_a|=3a^2+3a+1.
\]

Fix a threshold above one and select the dangerous directed internal peak
plateaux.  Let `E_a` be their total edge length and let `L_a` be the union of
their complete coordinate lines in `H_a`.

The plateau edge intervals are disjoint intervals of the middle-order word;
they can share only endpoints.  Their vertex union therefore contains at
least `E_a` distinct middle points and is contained in `L_a`.  Hence

\[
|L_a|\ge E_a.                                                \tag{2.1}
\]

In the zero-gap edge-mass-three limit,

\[
E_a=(3-o(1))a^2.
\]

Writing

\[
D_a=|H_a\setminus L_a|,
\]

equation (2.1) gives

\[
D_a=o(a^2).                                                  \tag{2.2}
\]

Equivalently, the selected complete coordinate lines cover asymptotically
all of the middle hexagon.  This conclusion is also the saturation case of
the full fixed-threshold line inequality

\[
|L_a|=(2a+1)m_a-T_a-I_a+J_a.
\]

## 3. The wedge-cover inequality

Let `P_a` and `N_a` be the total numbers, over all three directions, of
selected strictly positive and strictly negative coordinate levels.  Zero
levels contribute only `O(1)` and will disappear after normalization.

Fix a direction `i` and an unselected positive integer level `x`,
`1<=x<=a`.  For every `1<=y<x`, the point

\[
(x,-y,-(x-y))                                                \tag{3.1}
\]

lies in the sign wedge of `H_a` having positive `i`-coordinate and two
negative coordinates.  Since the positive `i`-line is unselected, a covered
point in (3.1) must lie on either the selected negative level `-y` in one
other direction or the selected negative level `-(x-y)` in the third.

Let `n_j,n_k` be the selected negative-level counts in those two directions,
and let `r_i(x)` count uncovered points in the wedge slice (3.1).  Then

\[
x-1\le n_j+n_k+r_i(x).                                      \tag{3.2}
\]

Choose an integer `h>=1`.  There are at most `n_j+n_k+h+1`
unselected positive levels for which the excess in (3.2) is at most `h`;
every remaining one contributes more than `h` uncovered wedge points.  If
`R_i` is the number of unselected positive levels in direction `i`,

\[
R_i\le n_j+n_k+h+1+{1\over h}\sum_x r_i(x).                  \tag{3.3}
\]

The three open sign wedges are disjoint, so

\[
\sum_{i,x}r_i(x)\le D_a.
\]

Summing (3.3) gives the finite robust cover inequality

\[
3a-P_a\le2N_a+3h+3+{D_a\over h}.                            \tag{3.4}
\]

Take `h=max(1,floor(sqrt(D_a)))`.  By (2.2), division by `a` and passage to
the limit yield

\[
\boxed{P+2N\ge3.}                                           \tag{3.5}
\]

Every selected dangerous plateau occupies a distinct coordinate line:
two plateaux longer than `a` cannot fit on one line.  Thus, if `f` is the
normalized selected-plateau count,

\[
P+N=f.                                                       \tag{3.6}
\]

Equations (3.5)--(3.6) imply

\[
\boxed{P\le2f-3.}                                           \tag{3.7}
\]

## 4. Absorbed seams cannot exceed the positive-line supply

Every actually absorbed successor at a fixed threshold `c>1` has a distinct
strictly positive selected level, because

\[
t\ge p-1>c-1>0.
\]

If `A` denotes absorbed seam mass, then

\[
A\le P\le2f-3.                                              \tag{4.1}
\]

There is no hidden atom at zero in the limiting passage: at finite `a` each
direction has only one zero level, and the level measures are dominated by
Lebesgue measure.

## 5. Uniform seam margin

Write

\[
x=p-1,\qquad y=s-1,
\]

and let `alpha` be the absorbed submeasure.  Put

\[
C=\int_\alpha(p+s-1)=\int_\alpha(1+x+y).
\]

Absorption legality gives `x+y<=1`, so (4.1) implies

\[
C\le2A\le4f-6.                                              \tag{5.1}
\]

Both marginals of the complete seam coupling have mass `f` and first moment
three.  Since `alpha` is a submeasure and `x,y>=0`,

\[
\int_\alpha x\le3-f,
\qquad
\int_\alpha y\le3-f.
\]

Using (4.1) again,

\[
C=A+\int_\alpha(x+y)
\le A+2(3-f)
\le3.                                                        \tag{5.2}
\]

Therefore, for the nonabsorbed product correction

\[
R_\beta=\int_{\rho-\alpha}(p-1)(s-1)\ge0,
\]

we have

\[
C-R_\beta\le\min\{4f-6,3\}.                                \tag{5.3}
\]

The conditions `1<=s<=2`, mass `f`, and first moment three force
`3/2<=f<=3`.  On this entire interval,

\[
1+f-\min\{4f-6,3\}\ge{1\over4},                            \tag{5.4}
\]

with equality only at `f=9/4` in the scalar envelope.

Finally, the exact zero-gap seam identity is

\[
U(1^+)=3-f+C-R_\beta.
\]

Equations (5.3)--(5.4) prove (1.1).

## 6. Scope and next step

Proved here:

1. the finite robust wedge-cover inequality (3.4);
2. the positive-line cap `A<=2f-3` under edge-mass-three saturation;
3. the uniform full-line zero-gap bound `U(1+)<=15/4`.

Not proved here:

1. the corresponding quantitative statement when the plateau edge mass is
   `3-delta` and the uncovered set has positive density;
2. control of the positive-gap seam term at all thresholds;
3. the complete mixed-profile three-box theorem or the original all-`k`
   contiguous-OR conjecture.

The strict `1/4` margin makes the first extension stable for sufficiently
small edge-mass deficit.  The remaining task is to combine the robust error
in (3.4) with the exact gap budget and common-threshold contraction laws.
