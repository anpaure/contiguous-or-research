# Six-slot size-two-efficient Bellman clocks: complete three-compact-row closure

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It derives the exact
first-crossing, endpoint-saturated size-two normal form for six slots,
retains its two finite transients, and proves the complete branch strictly
positive.  It does not close the size-three-, size-four-, or size-five-
efficient six-slot branches, the all-grid Bellman inequality, or an OR-word
upper bound.

Put

\[
 A={\sqrt\pi\over2},\qquad \alpha=A^2={\pi\over4},
\tag{0.1}
\]

and let `K` be the Rayleigh signed-tail kernel.  For `y>0`, write

\[
 C(y)=\sum_{q\ge0}K(qy),\qquad
 F_y(s)=\sum_{q\ge0}K(qy+s),
\tag{0.2}
\]

and

\[
 \mathcal L_2(y;s)=C(y)+F_y(s).
\tag{0.3}
\]

## 1. Exact six-slot normal form

Consider a nonnegative internally superadditive first-crossing table after
endpoint saturation,

\[
 (c_0,\ldots,c_6)=(0,x,y,z,w,T,E),
 \qquad x,y,z,w,T<A\le E,
\tag{1.1}
\]

and suppose size two is a maximum-density denomination.  In particular,
this applies when the table is assigned to least maximum-density size two.

Put

\[
                         s=T-2y.
\tag{1.2}
\]

### Theorem 1.1 (literal normal form)

One has

\[
 w=2y,\qquad E=3y,
\tag{1.3}
\]

and

\[
 x\le z-y\le s\le {y\over2}.
\tag{1.4}
\]

Moreover,

\[
 {A\over3}\le y<{A\over2},
 \qquad 0\le s\le {y\over2},
 \qquad s<A-2y.
\tag{1.5}
\]

The complete Bellman clock is

\[
 \boxed{
 V_{2q}=qy,qquad
 V_1=x,qquad V_3=z,qquad
 V_{2q+1}=qy+s\quad(q\ge2).}
\tag{1.6}
\]

Consequently its functional is exactly

\[
 \boxed{
 \Phi
 =\mathcal L_2(y;s)
  +K(x)-K(s)
  +K(z)-K(y+s).}
\tag{1.7}
\]

Thus every availability effect is retained: there are exactly two finite
pulses, at capacities one and three.

#### Proof

Maximum density of size two gives `c_j<=jy/2` for every `j`.  Internal
superadditivity gives

\[
 w=c_4\ge2c_2=2y,
 \qquad
 E=c_6\ge c_2+c_4=3y.
\]

The density upper bounds reverse both inequalities, proving (1.3).  Notice
that endpoint saturation is **not** being replaced by the five-slot
endpoint normalization: the size-six endpoint can be Bellman-inert and
strictly larger than `A`, but it is exactly three size-two generators.

Also

\[
 z\ge x+y,qquad T\ge y+z,qquad T\le{5y\over2},
\]

which gives (1.4).  First crossing at slot six and (1.3) give

\[
 2y=w<A\le E=3y,
\]

while `T=2y+s<A`; this proves (1.5).

Every even generator has value at most its size times `y/2`, and size-two
generators attain that bound, so `V_(2q)=qy`.  In an odd fill, pair all
but one of its odd generators.  Each pair has even total size, and its
value is at most that total size times `y/2`; replacing it by size-two
generators therefore cannot lower the fill value.  The same replacement
applies to every even generator.  Hence a maximizing odd fill may be
chosen to consist of size-two generators and exactly one generator of
size one, three, or five.  Their three possible formal shifts are

\[
 x,\qquad z-y,\qquad T-2y=s.
\]

Equation (1.4) makes `s` the largest.  It first becomes available at
capacity five.  Before then, internal superadditivity gives `V_1=x` and
`V_3=z`; from capacity five onward, one size-five generator padded by
size-two generators gives the formal odd value.  The size-six generator is
even and equals three size-two generators, so it creates no later
exception.  This proves (1.6).  Subtracting the formal odd entries at
capacities one and three gives (1.7). \(\square\)

## 2. The complementary scalar region

Normalize

\[
                         y=At,\qquad s=Au.
\tag{2.1}
\]

The exact scalar domain (1.5), enlarged harmlessly to its closure, is

\[
 {1\over3}\le t\le {1\over2},
 \qquad
 0\le u\le\min\left\{{t\over2},1-2t\right\}.
\tag{2.2}
\]

The physical endpoint `t=1/2` has empty strict interior but is useful as a
limiting boundary.

Put

\[
 h(v)=v e^{-\alpha v^2},
 \qquad
 R(v)=h(1-v)-h(1+v)\quad(0\le v\le1).
\tag{2.3}
\]

The terms with period indices `q=0,1,2` in `F_(At)(Au)` lie on the compact
branch, while every `q>=3` term lies on the increasing Gaussian tail.
Direct differentiation gives

\[
 {d\over du}F_{At}(Au)=-2A^2W_t(u),
\tag{2.4}
\]

where

\[
 W_t(u)=R(u)+R(t+u)+R(2t+u)
        -\sum_{q\ge3}h(1+u+qt).
\tag{2.5}
\]

Since `1+u+3t>=2`, the tail is decreasing.  Comparing every term with the
integral over its preceding interval gives

\[
 \sum_{q\ge3}h(1+u+qt)
 \le {1\over t}\int_{1+u+2t}^{\infty}h(v)\,dv
 ={e^{-\alpha(1+u+2t)^2}\over2\alpha t}.
\tag{2.6}
\]

Define the lower envelope

\[
 \boxed{
 H_t(u)=R(u)+R(t+u)+R(2t+u)
        -{e^{-\alpha(1+u+2t)^2}\over2\alpha t}.}
\tag{2.7}
\]

Then `W_t(u)>=H_t(u)`.

## 3. Concavity reduces the triangle to three rows

### Lemma 3.1

The function `R` is concave on `[0,1]`, strictly so away from zero.

#### Proof

Write

\[
 G(v)=h'(1+v)+h'(1-v).
\]

Then `R'(v)=-G(v)`.  The authenticated compact derivative lemma proves
that `G` is strictly increasing on `[0,1/2]`.  For `1/2<=v<=1`, one has
`h''(1-v)<=0<h''(1+v)`, so `G'(v)>0` there as well.  Hence
`R''(v)=-G'(v)<0` in the interior. \(\square\)

For fixed `t`, the last exponential in (2.7) is strictly convex in `u`,
because, with `x=1+u+2t`,

\[
 {d^2\over du^2}{e^{-\alpha x^2}\over2\alpha t}
 ={(2\alpha x^2-1)e^{-\alpha x^2}\over t}>0.
\tag{3.1}
\]

Therefore `H_t` is strictly concave in `u`, and its minimum occurs at an
endpoint of the interval (2.2).

Put

\[
\begin{aligned}
 M(t)={}&H_t(0)
 =R(t)+R(2t)-{e^{-\alpha(1+2t)^2}\over2\alpha t},\\
 N(t)={}&H_t(t/2)
 =R(t/2)+R(3t/2)+R(5t/2)
   -{e^{-\alpha(1+5t/2)^2}\over2\alpha t}.
\end{aligned}
\tag{3.2}
\]

For `2/5<=t<=1/2`, the other endpoint is

\[
 H_t(1-2t)=L(t),
\tag{3.3}
\]

where `L(t)` is exactly the authenticated lower-edge function in the
five-slot two-efficient wedge theorem.  That theorem gives

\[
                         L(t)>{1\over100}.
\tag{3.4}
\]

It remains to sign `M` on `[1/3,1/2]` and `N` on `[1/3,2/5]`.

### Lemma 3.2

Both `M` and `N` are concave on their displayed intervals.

#### Proof

For `c>0`, put

\[
 Q_c(t)={e^{-\alpha(1+ct)^2}\over2\alpha t}.
\]

Logarithmic differentiation gives

\[
 {Q_c''(t)\over Q_c(t)}
 =\left(2\alpha c(1+ct)+{1\over t}\right)^2
   -2\alpha c^2+{1\over t^2}.
\tag{3.5}
\]

For `c=2`, `t<=1/2`, the right side is positive already from

\[
 {2\over t^2}-2\alpha c^2\ge8-2\pi>0.
\]

For `c=5/2`, `t<=2/5`, it is positive from

\[
 {2\over t^2}-2\alpha c^2
 \ge{25\over2}-{25\pi\over8}>0.
\]

Thus both relevant `Q_c` are convex.  Lemma 3.1 makes every `R` term in
(3.2) concave, proving the claim. \(\square\)

Hence each of `M,N` has its minimum at one of its two interval endpoints.

## 4. Exact endpoint certificates

Define

\[
 P_m(x)=\sum_{j=0}^m{x^j\over j!},
 \qquad
 Q_3(x)=1-x+{x^2\over2}-{x^3\over6}.
\tag{4.1}
\]

For `x>0`,

\[
                         Q_3(x)<e^{-x}<{1\over P_m(x)}.
\tag{4.2}
\]

We use `333/106<pi<22/7`.  The following rational checks are direct
cross-multiplications:

\[
 P_5(74/53)>4,
 \qquad
 P_8(925/424)>{200\over23},
\tag{4.3}
\]

\[
\begin{aligned}
 {2\over3}Q_3(22/63)+{1\over3}Q_3(11/126)
 -{1\over3}-{397\over111}{23\over200}
 >{1\over50},
\end{aligned}
\tag{4.4}
\]

and

\[
 P_5(1813/1696)>{20\over7},
 \quad
 P_5(2997/1696)>{40\over7},
 \quad
 P_8(4477/1696)>{40\over3},
\tag{4.5}
\]

\[
\begin{aligned}
 &{5\over6}Q_3(275/504)
 +{1\over2}Q_3(11/56)
 +{1\over6}Q_3(11/504)\\
 &\hspace{12mm}-{49\over120}-{21\over80}-{23\over80}
 >{1\over20}.
\end{aligned}
\tag{4.6}
\]

No decimal estimate occurs in these certificates.

### Lemma 4.1 (the zero-shift row)

\[
                         \boxed{M(t)>0
                         \quad(1/3\le t\le1/2).}
\tag{4.7}
\]

#### Proof

At `t=1/2`, `M(1/2)` is exactly the lower-edge value `L(1/2)` from the
five-slot wedge theorem, hence is greater than `1/100`.

At `t=1/3`, direct expansion gives

\[
\begin{aligned}
 M(1/3)={}&{2\over3}e^{-\pi/9}
 +{1\over3}e^{-\pi/36}
 -{4\over3}e^{-4\pi/9}\\
 &-\left({5\over3}+{6\over\pi}\right)e^{-25\pi/36}.
\end{aligned}
\tag{4.8}
\]

The first two terms are bounded below using `pi<22/7` and `Q_3`.  From
`pi>333/106`, (4.3) gives

\[
 e^{-4\pi/9}<{1\over4},
 \qquad
 e^{-25\pi/36}<{23\over200},
 \qquad
 {6\over\pi}<{212\over111}.
\]

Certificate (4.4) therefore gives `M(1/3)>1/50`.  Concavity of `M` now
proves (4.7). \(\square\)

### Lemma 4.2 (the diagonal row)

\[
                         \boxed{N(t)>0
                         \quad(1/3\le t\le2/5).}
\tag{4.9}
\]

#### Proof

At `t=2/5`, one has `1-5t/2=0`, so `N(2/5)` is exactly the authenticated
upper-edge value in the five-slot wedge theorem and is greater than
`1/100`.

At `t=1/3`,

\[
\begin{aligned}
 N(1/3)={}&{5\over6}e^{-25\pi/144}
 +{1\over2}e^{-\pi/16}
 +{1\over6}e^{-\pi/144}\\
 &-{7\over6}e^{-49\pi/144}
 -{3\over2}e^{-9\pi/16}\\
 &-\left({11\over6}+{6\over\pi}\right)
      e^{-121\pi/144}.
\end{aligned}
\tag{4.10}
\]

The three positive terms are bounded below using `pi<22/7` and `Q_3`.
Using `pi>333/106`, (4.5) gives

\[
 e^{-49\pi/144}<{7\over20},
 \qquad
 e^{-9\pi/16}<{7\over40},
 \qquad
 e^{-121\pi/144}<{3\over40}.
\]

Also `6/pi<2`, so the last coefficient is less than `23/6`.
Certificate (4.6) gives `N(1/3)>1/20`.  Concavity of `N` proves (4.9).
\(\square\)

## 5. Positivity of the scalar region

For fixed `t`, concavity of `H_t` and Lemmas 4.1--4.2, together with
(3.4), prove

\[
 H_t(u)>0
\]

throughout (2.2).  Hence `W_t(u)>0`, and (2.4) gives

\[
                         {d\over du}F_{At}(Au)<0.
\tag{5.1}
\]

If `1/3<=t<=2/5`, then `u<=t/2`, so

\[
 \mathcal L_2(At;Au)
 \ge \mathcal L_2(At;At/2)
 =C(At/2)>0.
\tag{5.2}
\]

If `2/5<=t<=1/2`, then `u<=1-2t`.  The authenticated five-slot scalar
wedge theorem applies at that lower edge and gives

\[
 \mathcal L_2(At;Au)
 \ge\mathcal L_2(At;A(1-2t))>0.
\tag{5.3}
\]

Thus

\[
 \boxed{
 \mathcal L_2(y;s)>0
 \quad\left(
 {A\over3}\le y<{A\over2},\ 
 0\le s\le {y\over2},\ s<A-2y
 \right).}
\tag{5.4}
\]

## 6. Complete branch positivity

The kernel is decreasing on `[0,3A/4]`.  Equations (1.4)--(1.5) give

\[
 0\le x\le s,
 \qquad
 0\le z\le y+s\le{3y\over2}<{3A\over4}.
\]

Therefore

\[
 K(x)-K(s)\ge0,
 \qquad
 K(z)-K(y+s)\ge0.
\tag{6.1}
\]

The scalar theorem (5.4) makes the first term in (1.7) strictly positive.
Hence:

### Theorem 6.1

Every first-crossing, endpoint-saturated six-slot Bellman table for which
size two is a maximum-density denomination has

\[
                         \boxed{\Phi(c)>0.}
\tag{6.2}
\]

In particular, a normalized nonpositive six-slot table cannot be assigned
to least maximum-density size two.

## 7. Scope and frozen dependencies

For a hypothetical nonpositive six-slot table, complete positivity through
five slots first forces the threshold crossing to occur at slot six.  The
all-slot endpoint-saturation theorem may then be applied before choosing
the least maximum-density branch.  The present theorem closes the resulting
size-two branch without assuming any five-slot endpoint identity.

| role | file | SHA-256 |
|---|---|---|
| all-slot first crossing and endpoint saturation | `MATH_THEOREM_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md` | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| independent all-slot normalization audit | `MATH_AUDIT_ALL_N_FIRST_CROSSING_AND_MAXIMUM_DENSITY_APERY_REDUCTION_20260804.md` | `d404632e3bd805f92333276c74d3a094991da224f22259f11ba24193c0842173` |
| complete positivity through five slots | `MATH_THEOREM_FIVE_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `69d8d73e52342a74d11a8673811e0d41d15063a2d66d1fdbc504138b4ed76bed` |
| exact five-slot Apéry/two-pulse normal form | `MATH_THEOREM_FIVE_SLOT_MAXIMUM_EFFICIENCY_APERY_NORMAL_FORMS_20260804.md` | `2ba2be5a52e4761790f031fcc63955c8066fd032fc3afaa81de866b50abd9b9e` |
| five-slot scalar wedge, edge bounds, and kernel monotonicity | `MATH_THEOREM_FIVE_SLOT_TWO_EFFICIENT_SMALL_PERIOD_WEDGE_CLOSURE_20260804.md` | `a678fc5a33c6457d9d640aa963d902fdb8c7ed932ade6a14fd320caf8d285e43` |
| compact `G` monotonicity used in Lemma 3.1 | `MATH_THEOREM_FIVE_SLOT_THREE_EFFICIENT_DELAYED_B_CONCAVITY_AND_PURE_LATTICE_GATE_20260804.md` | `b494371c790ed20f14e29bd4beba67b27aa30f7f5b1447e4ef8da4e74db8ea14` |
| all-ceiling positivity | `MATH_THEOREM_RAYLEIGH_CEILING_DOMINATION_AND_FINITE_MIR_CONE_NOGO_20260804.md` | `18a5d75526774673909d29a26d93710a1d56e9298c51d3a4cebaa8ebcd62baf3` |
| independent all-ceiling audit | `MATH_AUDIT_RAYLEIGH_CEILING_DOMINATION_AND_FINITE_MIR_CONE_NOGO_20260804.md` | `9f807a2a044469bed61c2943adf51b48f71ce594748cc8d3fb41ceea3394ac39` |

No assertion is made about the remaining six-slot least-maximizer sizes
three, four, or five.
