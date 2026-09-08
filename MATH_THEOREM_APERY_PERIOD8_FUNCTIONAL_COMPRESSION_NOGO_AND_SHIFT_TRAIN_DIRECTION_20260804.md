# Period-eight depth-three Apéry clocks: functional compression no-go

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical obstruction theorem. It gives an
honest period-eight depth-three family for which both the endpoint-period
comparison and the literal periodic Bellman functional are strictly smaller
than for every same-\((a,P)\) canonical two-spike representative. Thus the
proposed functional compression gate is false. It does not produce a
nonpositive Bellman clock.

## 1. The symmetric canonical word and a legal perturbation

Fix

\[
                         a={A\over15},\qquad P=14a,\qquad A=P+a.
\tag{1.1}
\]

The symmetric canonical two-spike word is

\[
 G_0=(a,a,a,a,4a,a,a,4a).
\tag{1.2}
\]

For

\[
                         0<\varepsilon<a
\tag{1.3}
\]

put

\[
 G_\varepsilon
 =(a,a,a,a+\varepsilon,4a-\varepsilon,a,a,4a).
\tag{1.4}
\]

### Lemma 1.1

Every \(G_\varepsilon\) in (1.4) is an honest cyclic Apéry word with

\[
                         h=8,\qquad u=H=3,
\tag{1.5}
\]

and has the same first gap \(a\), period \(P=14a\), and exact threshold
\(A=15a\) as \(G_0\).

#### Proof

After subtracting the baseline \(a\), the nonzero excesses of
\(G_\varepsilon\) are

\[
 \varepsilon,\qquad3a-\varepsilon,\qquad3a
\]

at positions four, five, and eight. Prefixes of lengths one through three
have excess zero, the length-four prefix has excess \(\varepsilon\), and
prefixes of lengths five through seven have excess \(3a\).

Every cyclic block of length four contains at least one of positions four,
five, and eight, and its excess is therefore at least \(\varepsilon\).
Every cyclic block of length five, six, or seven either contains position
eight, of excess \(3a\), or contains both positions four and five, whose
total excess is also \(3a\). Hence every prefix is a minimum cyclic block
of its length. This is equivalent to carry-aware superadditivity.

For the exact period-eight overlap inequalities,

\[
 L=\gamma_2+\gamma_3+\gamma_4=3a+\varepsilon,
 \qquad T=\gamma_8=4a,
\]

so \(T>L\). Also

\[
 L+\gamma_5=7a>T+\gamma_6+\gamma_7=6a.
\]

Thus \(u=H=3\). The total gap sum is \(14a\), proving every remaining
claim. \(\square\)

The shifts of \(G_\varepsilon\) are

\[
 a,2a,3a,4a+\varepsilon,8a,9a,10a.
\tag{1.6}
\]

Only residue four moves.

## 2. Endpoint-period compression already fails

Let \(\mathscr E(G)\) denote the threshold endpoint-period comparison

\[
 \mathscr E(G)
 =C+\sum_{r=1}^{7}F_A(s_r)+F_A(P).
\tag{2.1}
\]

Since \(4a=A(4/15)>A/4\) and
\(4a+\varepsilon<A/3<A/2\), the authenticated threshold train is strictly
decreasing on this interval. Equation (1.6) gives

\[
 \boxed{
 \mathscr E(G_\varepsilon)-\mathscr E(G_0)
 =F_A(4a+\varepsilon)-F_A(4a)<0.}
\tag{2.2}
\]

Now classify every same-\((a,P)\) canonical two-spike representative. It
has gaps

\[
 (a,a,a,a,b_z,a,a,t_z),
\qquad
 t_z=a+z,\qquad b_z=7a-z,
\tag{2.3}
\]

where honesty and depth three are exactly

\[
                         3a\le z<{7a\over2}.
\tag{2.4}
\]

Its early reflected-ray points are fixed, while its three late reflected
points are

\[
 Y_1={2a+z\over A},\qquad
 Y_2={3a+z\over A},\qquad
 Y_3={4a+z\over A}.
\tag{2.5}
\]

They lie in \([1/3,1/2)\). In reflected form their contribution is

\[
                         q(Y_i):=g(Y_i)-f(Y_i).
\]

On \([1/4,1/2]\), \(g'>0\) and \(f'<0\), hence

\[
                         q'(y)=g'(y)-f'(y)>0.
\tag{2.6}
\]

Therefore the canonical endpoint comparison is strictly increasing in
\(z\) and is minimized at \(z=3a\), namely at \(G_0\). Combining this with
(2.2),

\[
 \boxed{
 \mathscr E(G_\varepsilon)
 <
 \mathscr E(G_0)
 \le
 \mathscr E(G_z)
 \quad\hbox{for every canonical representative }G_z.}
\tag{2.7}
\]

Thus the endpoint-period functional compression gate is false.

## 3. A shift-train derivative at the perturbation point

The failure also holds for the literal periodic Bellman functional. Put

\[
 h(x)=xe^{-\pi x^2/4},\qquad
 F_P(w)=\sum_{q\ge0}K(qP+w),\qquad p={P\over A}={14\over15}.
\tag{3.1}
\]

For \(0<u<1\),

\[
 {F_P'(Au)\over2A}
 =
 \sum_{q\ge0}h(1+u+qp)-h(1-u).
\tag{3.2}
\]

### Lemma 3.1

At \(u=4/15\),

\[
                         \boxed{F_P'(4A/15)<0.}
\tag{3.3}
\]

#### Proof

Divide the positive terms in (3.2) by \(h(11/15)\). The first ratio is

\[
 {h(19/15)\over h(11/15)}
 ={19\over11}e^{-4\pi/15}<{4\over5}.
\tag{3.4}
\]

Indeed \(\pi>3\), and

\[
 e^{4/5}>
 1+{4\over5}+{8\over25}+{32\over375}
 ={827\over375}>{95\over44}.
\]

The next ratio is

\[
 {h(33/15)\over h(11/15)}
 =3e^{-242\pi/225}<{1\over8}.
\tag{3.5}
\]

Here \(\pi>3\), \(e>19/7\), and

\[
 e^{242/75}
 =e^{3+17/75}
 >\left({19\over7}\right)^3{92\over75}>24.
\]

For every later positive term, with \(z\ge33/15\),

\[
 {h(z+14/15)\over h(z)}
 \le{47\over33}e^{-56\pi/45}
 <{1\over20}.
\tag{3.6}
\]

The final inequality follows from \(47/33<3/2\), \(\pi>3\), and

\[
 e^{56/15}
 =e^{3+11/15}
 >\left({19\over7}\right)^3{26\over15}>30.
\]

Thus all positive terms in (3.2), divided by the adverse term, sum to less
than

\[
 {4\over5}+{1/8\over1-1/20}
 ={4\over5}+{5\over38}
 ={177\over190}<1.
\]

This proves (3.3). \(\square\)

By continuity, there exists \(\varepsilon_0\in(0,a)\) such that

\[
 F_P(4a+\varepsilon)<F_P(4a)
 \qquad(0<\varepsilon<\varepsilon_0).
\tag{3.7}
\]

Since only residue four moves,

\[
 \boxed{
 \Phi(W_\varepsilon)-\Phi(W_0)
 =F_P(4a+\varepsilon)-F_P(4a)<0.}
\tag{3.8}
\]

## 4. Every canonical literal clock is above the symmetric one

### Lemma 4.1

For

\[
                         {A\over2}\le w\le {2A\over3},
\tag{4.1}
\]

one has

\[
                         \boxed{F_P'(w)<0}
\tag{4.2}
\]

at \(P=14A/15\).

#### Proof

Write \(w=Au\), \(1/2\le u\le2/3\). The first positive/adverse ratio in
(3.2) is

\[
 R_0(u)={1+u\over1-u}e^{-\pi u}.
\tag{4.3}
\]

Its logarithm is convex because the derivative

\[
 {2\over1-u^2}-\pi
\]

is increasing. Hence its maximum occurs at an endpoint. At \(u=1/2\),

\[
 3e^{-\pi/2}<{7\over10},
\]

using \(\pi>3\) and the degree-four positive Taylor sum for \(e^{3/2}\).
At \(u=2/3\),

\[
 5e^{-2\pi/3}<{7\over10},
\]

using \(e^2>(19/7)^2>50/7\). Thus \(R_0<7/10\).

The first tail term, relative to the adverse term, has prefactor at most
\(39/5<8\) and exponent at least \(319\pi/225\). Since

\[
 e^{319/75}
 =e^{4+19/75}
 >\left({19\over7}\right)^4{94\over75}>64,
\]

that ratio is less than \(1/8\).

For successive tail terms the prefactor is at most
\(101/73<7/5\), while the exponent increment is at least
\(203\pi/150>4\). Since \((19/7)^4>42\), every successive ratio is less
than \(1/30\).

Hence the complete positive/adverse ratio is less than

\[
 {7\over10}+{1/8\over1-1/30}
 ={7\over10}+{15\over116}
 ={481\over580}<1.
\]

This proves (4.2). \(\square\)

For the canonical family (2.3), the moving shifts are

\[
 s_5=11a-z,\qquad s_6=12a-z,\qquad s_7=13a-z.
\tag{4.4}
\]

As \(3a\le z<7a/2\), all three belong to \([A/2,2A/3]\). Therefore

\[
 {d\over dz}\Phi(W_z)
 =-\sum_{r=5}^{7}F_P'(s_r)>0.
\tag{4.5}
\]

Every canonical literal clock is consequently minimized at \(z=3a\):

\[
                         \Phi(W_0)\le\Phi(W_z).
\tag{4.6}
\]

Combining (3.8) and (4.6) gives, for all sufficiently small positive
\(\varepsilon\),

\[
 \boxed{
 \Phi(W_\varepsilon)
 <
 \Phi(W_z)
 \quad\hbox{for every same-\((a,P)\) canonical two-spike representative}.}
\tag{4.7}
\]

Thus the literal Bellman functional compression gate is also false.

## 5. Consequence and scope

The obstruction is a legal Robin-Hood transfer from gap five into gap four.
It leaves \(a,P,A\), all later shifts, and the depth-three topology fixed,
but moves one early compact shift to the right along a strictly decreasing
train.

Canonical two-spike positivity therefore cannot be extended to arbitrary
period-eight depth-three words by a same-\((a,P)\) monotone compression.
A successful proof must retain at least one additional early-ray parameter
or use a nonmonotone global inequality.

The theorem does not assert that \(G_\varepsilon\) is nonpositive; it only
disproves the proposed comparison principle. It does not address larger
periods, higher overlap depth, overshoot, later crossing, or finite physical
shoulders.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| full canonical two-spike closure and proposed gate | MATH_THEOREM_APERY_PERIOD8_TWO_SPIKE_FULL_CLOSURE_AND_CANONICAL_COMPRESSION_20260804.md | 76f1ced69d953d0ed0d6f1b4dd20566fcf5d6a657158c4b6de5b349e155e8e27 |
| independent audit of that theorem | MATH_AUDIT_APERY_PERIOD8_TWO_SPIKE_FULL_CLOSURE_AND_CANONICAL_COMPRESSION_INDEPENDENT_20260804.md | ed3ba018742e88c7473fa8d8b7f0ea043912c0f5c8b1a09ebc4864700279c0fb |
| compact train decrease and reflection | MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md | fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7 |
