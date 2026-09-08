# Cross-line inequalities for mixed plateau profiles

## 1. Outcome

The omission/intersection argument has a rigorous fixed-threshold form for
every `b>1`.  It does not require an atom or concentration of the selected
plateau lengths.

Let

\[
 F_a(b)=\#\{P:\lambda(P)>ba\},\qquad
 E_a(b)=\sum_{\lambda(P)>ba}\lambda(P).                         \tag{1.1}
\]

If `n_x,n_y,n_z` are the direction counts, `T_a(b)` is the sum of the
absolute coordinate levels, `N_a(b)` is the number of selected
cross-direction line pairs which do not meet in `H_a`, and `J_a(b)` is the
number of points incident with selected lines in all three directions, then

\[
 \boxed{
 E_a(b)\le 2aF_a(b)-T_a(b)
 -{F_a(b)^2-(n_x^2+n_y^2+n_z^2)\over2}
 +N_a(b)+J_a(b)+O_b(a).}                                      \tag{1.2}
\]

This is the strongest direct form of the cross-line charge.  It keeps the
joint tradeoff which matters: moving levels toward the ends can increase
`N_a(b)`, but it simultaneously increases `T_a(b)` and reduces the
omission budget.

The triple term is important: replacing `J_a` by its universal upper bound
`(I_0-N_a)/3` recovers the earlier `2/3` charge, but loses information.
Keeping it and applying the one-dimensional Riesz rearrangement inequality
excludes the entire vanishing-seam class of limiting measures supported on
`[4/3,3/2]`; see Theorem 8.1.  In particular, the exclusion is not confined
to atoms.

For arbitrary mixed tails, the remaining condition is an explicit joint
length-direction-level-additive variational gate: the tail measure must
admit level sets satisfying the strongest limiting inequality (4.8) at
every threshold.  The scalar laws alone do not determine this lift.

## 2. Fixed-threshold geometry

For `b>=2` the selected tail is empty.  Fix `1<b<2` and select all directed
internal coordinate-peak plateaux with
`lambda(P)>ba`.  Put

\[
 m=F_a(b),\qquad E=E_a(b).                                      \tag{2.1}
\]

A selected plateau on coordinate level `t` uses `lambda(P)+1` distinct
points of a line containing exactly `2a-|t|+1` points.  Therefore

\[
                         |t|\le2a-\lambda(P)<(2-b)a.             \tag{2.2}
\]

Two selected plateaux cannot use the same coordinate and level.  They are
distinct maximal constant blocks of the same scalar word and hence have
disjoint vertex sets, while their combined vertex count is greater than
`2ba>2a` for all sufficiently large `a`.  Consequently

\[
 n_i\le2(2-b)a+O(1),\qquad
 m=n_x+n_y+n_z\le6(2-b)a+O(1).                                 \tag{2.3}
\]

In particular, for every fixed `b>1`, the selected family has only `O_b(a)`
members.

Let

\[
 S_2=n_x^2+n_y^2+n_z^2,
 \qquad T=\sum_{P:\lambda(P)>ba}|t(P)|.                         \tag{2.4}
\]

The number of selected cross-direction line pairs is

\[
 I_0=n_xn_y+n_yn_z+n_zn_x={m^2-S_2\over2}.                     \tag{2.5}
\]

Let `N` be the number of these pairs whose two lines do not intersect in
`H_a`, and put

\[
                              I=I_0-N.                           \tag{2.6}
\]

Thus `I` is the number of genuinely intersecting selected-line pairs.
Triple intersections count three pairs, as they must.

Let `J` be the number of points through which selected lines in all three
coordinate directions pass.  Equivalently, if `A_x,A_y,A_z` are the three
sets of selected integer levels, then

\[
 J=\#\{(r,s,t)\in A_x\times A_y\times A_z:r+s+t=0\}.           \tag{2.7}
\]

Every such point contributes three to `I`, so `0<=J<=I/3`.

## 3. The finite master inequality

For a selected plateau `P` at level `t(P)`, its number of line omissions is

\[
 r(P)=(2a-|t(P)|+1)-(\lambda(P)+1)
     =2a-|t(P)|-\lambda(P).                                    \tag{3.1}
\]

Summing gives the exact identity

\[
                         R:=\sum_Pr(P)=2am-E-T.                  \tag{3.2}
\]

At a point `p in H_a`, let `d_p` be the number of selected coordinate lines
through `p`, and let `u_p` be the number of the corresponding selected
plateaux which use `p`.  Selected plateau edge sets are pairwise disjoint:
different constant blocks in one coordinate have disjoint edge sets, while
an edge constant in two coordinates would have identical endpoints because
`x+y+z=0`.

It follows that `u_p<=2`.  If `u_p=2`, the word position of `p` is the shared
endpoint of two consecutive plateau edge intervals.  There are at most `m`
such positions.  Away from them `u_p<=1`, and direct checking at
`d_p=0,1,2,3` gives the sharper local inequality

\[
 d_p-u_p\ge {d_p\choose2}-\mathbf 1_{\{d_p=3\}}.               \tag{3.3}
\]

At a shared endpoint the deficit from (3.3) is at most one.  Hence

\[
 R=\sum_p(d_p-u_p)
   \ge\sum_p{d_p\choose2}-J-m
   =I-J-m.                                                      \tag{3.4}
\]

Combining (3.2), (3.4), and (2.5)-(2.6) proves

\[
 E\le2am-T-{m^2-S_2\over2}+N+J+m.                              \tag{3.5}
\]

This is (1.2), since `m=O_b(a)`.  No length concentration, direction
balance, seam hypothesis, or prescribed order of plateau directions was
used.

Since `J<=I/3`, (3.5) implies the triple-blind form

\[
 E\le2am-T-{m^2-S_2\over3}+{2\over3}N+m.                       \tag{3.6}
\]

Among `n` distinct integer levels, the smallest absolute-level sum is
`floor(n^2/4)`.  Thus the weaker but sometimes convenient consequence is

\[
 E\le2am-{m^2\over3}+{S_2\over12}+{2\over3}N+O_b(a).            \tag{3.7}
\]

Equation (3.5), rather than (3.6) or (3.7), should be used when end-fringe
placement or additive triple structure is important, because `T`, `N`, and
`J` are correlated.

## 4. The exact limiting variational gate

Let

\[
 \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a}
       \Longrightarrow\mu                                     \tag{4.1}
\]

along a subsequence.  All these measures are supported on `[0,2]`.  Fix a
continuity threshold `b>1`, meaning `mu({b})=0`, and write

\[
 f(b)=\mu((b,2]),\qquad
 \ell(b)=\int_{(b,2]}x\,d\mu(x).                               \tag{4.2}
\]

For a selected plateau in direction `i`, record both its normalized length
`x=lambda(P)/a` and normalized level `u=t(P)/a`.  The empirical joint
measures are

\[
 \rho_{i,a}={1\over a}\sum_{\substack{P:\lambda(P)>ba\\
                                      P\text{ in direction }i}}
                \delta_{(\lambda(P)/a,t(P)/a)}.                 \tag{4.3}
\]

After a further subsequence they converge weakly to measures `rho_i`.
Their level marginals `nu_i` have the following properties:

\[
 \begin{aligned}
 &\rho_i\text{ is supported on }
   \{(x,u):b\le x\le2,\ |u|\le2-x\},\\
 &\nu_i\le\text{Lebesgue measure on }[-(2-b),2-b],\\
 &\sum_i(\text{length marginal of }\rho_i)
       =\mu|_{(b,2]}.
 \end{aligned}                                                  \tag{4.4}
\]

The domination by Lebesgue measure is the continuum form of same-level
uniqueness: an interval of normalized levels contains at most `a` times its
length, plus `O(1)`, distinct integer levels.

Put

\[
 \alpha_i=\nu_i(\mathbb R),\quad
 s_2=\alpha_x^2+\alpha_y^2+\alpha_z^2,\quad
 \tau=\sum_i\int|u|\,d\nu_i(u),                                 \tag{4.5}
\]

so that `alpha_x+alpha_y+alpha_z=f(b)`.  Finally define the normalized
nonintersection count

\[
 \eta=\sum_{i<j}\iint \mathbf{1}_{\{|u+v|>1\}}\,d\nu_i(u)\,d\nu_j(v). \tag{4.6}
\]

Because `nu_i<=Leb`, the boundary `|u+v|=1` has product measure zero.
Thus the finite nonintersection counts converge to (4.6).  After one more
subsequence, let

\[
                         \theta=\lim {J_a(b)\over a^2}.          \tag{4.7}
\]

Dividing the strongest finite inequality (3.5) by `a^2` gives

\[
 \boxed{
 \ell(b)\le
 2f(b)-\tau-{f(b)^2-s_2\over2}+\eta+\theta.}                   \tag{4.8}
\]

Here

\[
 0\le\theta\le{1\over3}
       \left({f(b)^2-s_2\over2}-\eta\right),                   \tag{4.9}
\]

because every triple point contributes three intersecting line pairs.
Using only this upper bound on `theta` recovers the triple-blind relaxation

\[
 \ell(b)\le
 2f(b)-\tau-{f(b)^2-s_2\over3}+{2\over3}\eta.                  \tag{4.10}
\]

Equation (4.8), together with the requirement that `theta` arise from the
additive triples of the same three discrete level sets, is the strongest
limiting gate supplied by this method.  It retains the actual
length-dependent ranges `|u|<=2-x`.  Weak level marginals alone need not
determine `theta`: microscopic arithmetic structure can survive in the
normalized additive-triple count.  This is the residual
length-direction-level-additive variational problem for a general tail.

For reference, a count-sensitive upper bound on (4.6) is also available.
When `1<b<3/2`, put

\[
 q=2-b,\qquad w=3-2b.                                           \tag{4.11}
\]

Let `p_i^+` and `p_i^-` be the `nu_i` masses in the positive and negative
end fringes

\[
 (b-1,q]\quad\text{and}\quad[-q,-(b-1)).
\]

Compression toward the relevant end of the interval gives

\[
 \eta\le\sum_{i<j}
 \left(\Phi_w(p_i^+,p_j^+)+\Phi_w(p_i^-,p_j^-)\right),          \tag{4.12}
\]

where

\[
 \Phi_w(r,s)=rs-{1\over2}(r+s-w)_+^2.
\]

Indeed, after writing a positive fringe level as `q-u`, nonintersection is
`u+v<w`; the maximizing subsets are the initial intervals of lengths `r`
and `s`.  If `b>=3/2`, the fringes are empty and `eta=0`.

The simple product estimate `Phi_w(r,s)<=rs` is valid but loses the
triangular geometry.  The strongest gate (4.8) loses neither this geometry nor
the accompanying absolute-level cost.

## 5. A closed triple-blind scalar envelope

It is useful to have a necessary inequality which can be checked without
solving the additive problem in (4.8).  Start from the relaxed inequality
(4.10).  For `1<b<2`, put

\[
 q=2-b,\qquad C=2q=2(2-b),\qquad c_0=b-1.                       \tag{5.1}
\]

Thus `0<=alpha_i<=C`.  For a level `u`, the total measure in one other
direction which could fail to intersect it is at most

\[
                         d_b(u)=(|u|-c_0)_+.                    \tag{5.2}
\]

Summing degrees over the two other directions and dividing by two because
each nonintersecting pair has two endpoints gives

\[
                         \eta\le\sum_i\int d_b(u)\,d\nu_i(u).  \tag{5.3}
\]

Consequently

\[
 \tau-{2\over3}\eta
 \ge\sum_i\int
   \left(|u|-{2\over3}(|u|-c_0)_+\right)d\nu_i(u).              \tag{5.4}
\]

The integrand is even and increasing in `|u|`.  Under `nu_i<=Leb` and
`nu_i(R)=alpha_i`, its integral is minimized by the centered interval of
length `alpha_i`.  Denote that minimum by `h_b(alpha_i)`.

If `b>=3/2`, there is no end fringe and

\[
                         h_b(\alpha)={\alpha^2\over4}.           \tag{5.5}
\]

If `1<b<3/2`, put `K=2(b-1)`.  Direct integration gives

\[
 h_b(\alpha)=
 \begin{cases}
  \alpha^2/4,&0\le\alpha\le K,\\[2mm]
  \alpha^2/12+{2(b-1)\over3}\alpha
       -{2\over3}(b-1)^2,&K\le\alpha\le C.
 \end{cases}                                                    \tag{5.6}
\]

Set

\[
                         k_b(\alpha)={\alpha^2\over3}-h_b(\alpha). \tag{5.7}
\]

Explicitly,

\[
 k_b(\alpha)=
 \begin{cases}
  \alpha^2/12,& b\ge3/2,\\
  \alpha^2/12,&1<b<3/2\text{ and }0\le\alpha\le K,\\
  \alpha^2/4-{2(b-1)\over3}\alpha
       +{2\over3}(b-1)^2,
      &1<b<3/2\text{ and }K\le\alpha\le C.
 \end{cases}                                                    \tag{5.8}
\]

The function `k_b` is convex on `[0,C]`; at `K` both its value and first
derivative agree.  Therefore, among triples with sum `f`, the maximum of
`sum_i k_b(alpha_i)` is obtained by filling coordinate directions one at a
time to the cap `C`.  Write

\[
 f=jC+r,qquad j\in\{0,1,2\},\quad0\le r\le C,                  \tag{5.9}
\]

with the convention `j=2,r=C` when `f=3C`.  Define

\[
 \overline{\mathfrak C}_b(f)
 =2f-{f^2\over3}+j k_b(C)+k_b(r).                              \tag{5.10}
\]

Equations (4.10) and (5.3)-(5.9) prove the fully scalar necessary law

\[
 \boxed{
       \ell(b)\le\overline{\mathfrak C}_b(f(b)),
       \qquad f(b)\le6(2-b),}                                  \tag{5.11}
\]

at every continuity threshold `b>1`.  This envelope is weaker than the
triple-aware inequality (4.8).  It is deliberately one-sided: a profile satisfying
(5.11) need not possess a joint length-level lift satisfying (4.4), much
less a word realization.

## 6. Generalizing the boundary-reservoir saturation step

The atom assumption in the saturation part of
`BOUNDARY_RESERVOIR_PROFILE.md` is unnecessary when the limiting plateau
measure is supported a fixed positive distance from zero.

### Theorem 6.1 (mixed-profile boundary saturation)

Assume

1. `D=o(a^2)` in the selected-middle-order framework;
2. `mu_a -> mu` and `supp(mu) subseteq [beta,2]` for some `beta>0`; and
3. `H_a(c)->0` for every sufficiently small fixed `c>0`.

Then

\[
                         \sigma:=\int x\,d\mu(x)=3.             \tag{6.1}
\]

#### Proof

Fix `c<beta` for which the seam limit vanishes, and choose
`beta'` strictly between `c` and `beta`.  All but `o(a)` of the
`c`-dangerous plateaux have length at least `beta'a`: this follows from
weak convergence and the absence of limiting mass below `beta`.  For such
a successor plateau,

\[
 \lambda-ca\ge(\beta'-c)a,
 \qquad (4a+2)-\lambda\ge2a+2.                                 \tag{6.2}
\]

The seam argument from the atom proof therefore applies verbatim to the
nonexceptional successors.  The exceptional `o(a)` successors cost only
`o(a^2)` after every gap is truncated at `O(a)`.  Hence all but `o(a^2)`
positions in the complement of the `c`-dangerous plateau union belong to
the one-sided dangerous-free reservoir `R_c`.

The dangerous plateau edge mass is `(sigma+o(1))a^2`.  Indeed, the
non-dangerous normalized count tends to zero and lengths are uniformly
bounded by `2a`.  Passing from the sum of edge lengths to the size of the
vertex union changes the answer by only `O(a)`, because the total plateau
count is `O(a)` and vertex intervals share only endpoints.  Thus

\[
                         |R_c|\ge(3-\sigma-o(1))a^2.             \tag{6.3}
\]

The quadratic reservoir law gives

\[
                         3-\sigma\le{9\over4}c^2.               \tag{6.4}
\]

First let `a` tend to infinity for fixed `c`, then let `c` decrease to
zero.  This gives `sigma>=3`.  Pairwise disjointness of all plateau edge
sets gives `sigma<=3`, proving (6.1).  \(\square\)

The support-away-from-zero and vanishing-seam hypotheses are essential to
this deduction.  The corrected scalar laws do not themselves force
`H(c)=0`, and positive seam mass can fragment the complement so that it has
no macroscopic deep reservoir.

Under the same hypothetical `D=o(a^2)` framework, the other corrected
scalar necessary laws remain available, in particular

\[
 \sigma\le3,
 \qquad
 2\int(x-c)_+\,d\mu(x)+H(c)\ge4-3c
       \quad(0<c<4/3),                                          \tag{6.5}
\]

and the corrected interval-supply and survival-count laws.  These laws can
be imposed simultaneously with (4.8) or (5.11), but they do not determine
the direction/level lift in (4.4).

## 7. Preliminary triple-blind exclusions

Assume throughout this section that

\[
 \operatorname{supp}(\mu)\subseteq[4/3,3/2],qquad
 D=o(a^2),qquad H_a(c)\longrightarrow0
 \text{ for all sufficiently small fixed }c>0.                 \tag{7.1}
\]

Theorem 6.1 gives

\[
                         \int x\,d\mu(x)=3.                    \tag{7.2}
\]

The two consequences below use only the relaxed `2/3` envelope (5.11).
They are retained as useful tail tests for profiles not covered by the full
support hypothesis.  The triple-aware argument in Section 8 is strictly
stronger under (7.1).

### 7.1 Mass at `3/2`

Put `h=mu({3/2})`.  Apply (5.11) and let `b` increase to `3/2`.  Then
`f(b)->h`, `ell(b)->(3/2)h`, `C->1`, and `k_b(alpha)->alpha^2/12`.
Global edge disjointness already gives `h<=2`.  For `1<=h<=2`, (5.11)
becomes

\[
 {3h\over2}
 \le2h-{h^2\over3}+{1+(h-1)^2\over12}.                         \tag{7.3}
\]

Equivalently,

\[
                         3h^2-4h-2\le0.                         \tag{7.4}
\]

The same conclusion is automatic when `h<1`, so every profile satisfying
(7.1) must obey

\[
                         \boxed{h\le{2+\sqrt {10}\over3}.}      \tag{7.5}
\]

This excludes not only `2 delta_(3/2)` but every mixed profile placing more
than `(2+sqrt(10))/3` units of counting mass at `3/2`.

### 7.2 Total plateau count

Let

\[
                              s=\mu([4/3,3/2]).                  \tag{7.6}
\]

From (7.2) and the support bounds, `2<=s<=9/4`.  Apply (5.11) at thresholds
`b<4/3` and let `b` increase to `4/3`.  Then `f(b)=s`, `ell(b)=3`,
`C=4/3`, and `K=2/3`.  Write

\[
                         r=s-{4\over3},qquad {2\over3}\le r\le{11\over12}.
\]

The direction-filling maximum in (5.10) uses masses `(4/3,r,0)`.  Here

\[
 k_{4/3}(4/3)={2\over9},qquad
 k_{4/3}(r)={r^2\over4}-{2r\over9}+{2\over27}.                  \tag{7.7}
\]

After subtracting the required edge mass `3`, the right side of (5.11) is

\[
                         -{17\over27}+{8r\over9}-{r^2\over12}.  \tag{7.8}
\]

It is negative for

\[
 r<{16-2\sqrt {47}\over3},
 \quad\text{equivalently}\quad
 s<{20-2\sqrt {47}\over3}.                                    \tag{7.9}
\]

Therefore

\[
 \boxed{
 \mu([4/3,3/2])\ge{20-2\sqrt {47}\over3}=2.096\ldots.}        \tag{7.10}
\]

This is a genuine mixed-profile extension of the saturated-atom
obstruction.  It is not claimed to be the optimum of the exact gate (4.8).

## 8. Triple-aware exclusion of the full interval

### Theorem 8.1

No sequence satisfies all three hypotheses in (7.1).  Equivalently, under
`D=o(a^2)` and vanishing seam mass at every sufficiently small fixed
threshold, no limiting directed-plateau measure is supported on
`[4/3,3/2]`.

#### Proof

Suppose such a measure exists.  By Theorem 6.1 its total edge mass is `3`.
Put

\[
 s=\mu([4/3,3/2]),\qquad 2\le s\le9/4.                         \tag{8.1}
\]

Apply (4.8) below `4/3` and let the threshold increase to `4/3`.  The
limiting direction counts satisfy

\[
 0\le\alpha_i\le4/3,\qquad \alpha_x+\alpha_y+\alpha_z=s.       \tag{8.2}
\]

All levels lie in `[-2/3,2/3]`.  A level `u` has at most
`d(u)=(|u|-1/3)_+` nonintersecting level mass in either other direction.
Thus

\[
 \eta\le\sum_i\int d(u)\,d\nu_i(u),\qquad
 \tau-\eta\ge\sum_i\int\min\{|u|,1/3\}\,d\nu_i(u).              \tag{8.3}
\]

For a level measure of mass `alpha` dominated by Lebesgue measure, the
last integral is minimized by the centered interval.  Its minimum is

\[
 h(\alpha)=
 \begin{cases}
  \alpha^2/4,&0\le\alpha\le2/3,\\
  \alpha/3-1/9,&2/3\le\alpha\le4/3.
 \end{cases}                                                   \tag{8.4}
\]

The one-dimensional Riesz rearrangement inequality applied to the three
integer level sets bounds the normalized additive-triple count by its value
for centered intervals.  If their masses in decreasing order are
`alpha>=beta>=gamma`, then

\[
 \theta\le\Theta(\alpha,\beta,\gamma)
 :=\beta\gamma-\frac14(\beta+\gamma-\alpha)_+^2.                \tag{8.5}
\]

This formula follows by integrating the trapezoidal convolution of the
centered `beta`- and `gamma`-intervals over the centered
`alpha`-interval.  Discrete endpoints contribute only `O(a)`.

Set

\[
 A(\alpha)=\frac{\alpha^2}{2}-h(\alpha)=
 \begin{cases}
  \alpha^2/4,&0\le\alpha\le2/3,\\
  \alpha^2/2-\alpha/3+1/9,&2/3\le\alpha\le4/3.
 \end{cases}                                                   \tag{8.6}
\]

The strongest cross-line inequality now implies

\[
 3\le2s-\frac{s^2}{2}
       +\sum_iA(\alpha_i)+\Theta(\alpha_x,\alpha_y,\alpha_z).   \tag{8.7}
\]

An elementary three-variable optimization gives

\[
 \max_{\substack{0\le\alpha_i\le4/3\\\sum\alpha_i=s}}
 \left(\sum_iA(\alpha_i)+\Theta(\alpha_x,\alpha_y,\alpha_z)\right)
 =\frac59+\frac38\left(s-\frac43\right)^2.                     \tag{8.8}
\]

Here is the case check.  Sort the variables as `a>=y>=z` and put
`r=y+z=s-a`.  If `a>=r`, then `Theta=yz`.  A direct check across the
break at `2/3` shows that, at fixed `a`, the expression in `y,z` is
maximized at `y=z=r/2`.  It is then

\[
 A(a)+{3r^2\over8}.                                             \tag{8.9}
\]

This is convex in `a` on `[s/2,4/3]`.  Its value at `a=4/3` exceeds its
value at `a=s/2` by

\[
 {5s^2\over32}-{5s\over6}+{10\over9}
 ={5(3s-8)^2\over288}>0.                                      \tag{8.10}
\]

If `a<r`, then `Theta=yz-(r-a)^2/4`.  At fixed `r`, the maximum of
`A(y)+A(z)+yz` is `3r^2/8` for `r<=4/3`, and
`r^2/2-r/3+2/9` for `r>=4/3`.  Along `a+r=s`, the first resulting
expression has derivative `r/4-1/3<=0`, while the second has derivative
zero.  Thus its maximum is represented at the common boundary `r=4/3`.
Its deficit from the `a=4/3` value, with `q=s-4/3`, is

\[
 \frac{q^2}{8}-\frac q3+\frac29>0,\qquad
 q=s-\frac43<\frac43.                                         \tag{8.11}
\]

Thus the maximizer is

\[
 \left(\frac43,\frac12\left(s-\frac43\right),
                 \frac12\left(s-\frac43\right)\right),
\]

which proves (8.8).  Writing `q=s-4/3`, where
`2/3<=q<=11/12`, the right side of (8.7) is at most

\[
 \frac73+\frac{2q}{3}-\frac{q^2}{8}
 \le\frac{3271}{1152}<3.                                      \tag{8.12}
\]

This contradicts (8.7).  \(\square\)

### Why the triple refinement is necessary

The triple-blind inequalities of Sections 5 and 7 do not remove the entire
interval-supported class.  Consider the abstract limiting profile

\[
                              \mu={9\over4}\delta_{4/3}.         \tag{8.13}
\]

It has total edge mass `3`, so it passes Theorem 6.1.  With `H(c)=0`, it
also satisfies the corrected mass law in (6.5): for `0<c<4/3`,

\[
 2\int(x-c)_+\,d\mu(x)=6-{9\over2}c\ge4-3c.                    \tag{8.14}
\]

It also satisfies the corrected supply and line-survival count laws.

At a threshold just below `4/3`, the following continuum level lift passes
the relaxed `2/3` cross-line inequality:

\[
 \nu_x={\bf1}_{[-2/3,2/3]}\,du,qquad
 \nu_y={\bf1}_{[-11/24,11/24]}\,du,qquad
 \nu_z=0,                                                       \tag{8.15}
\]

with every length coordinate equal to `4/3`.  Its values are

\[
 \begin{aligned}
 f&={9\over4},&
 \tau&={4\over9}+{121\over576}={377\over576},\\
 I_0&={11\over9},&
 \eta&={1\over64},&
 I&={695\over576}.
 \end{aligned}                                                  \tag{8.16}
\]

The omission budget and required charge are

\[
 2f-3-\tau={487\over576}
 \quad\text{and}\quad
 {2\over3}I={695\over864},                                    \tag{8.17}
\]

and the first is larger by `71/1728`.  Thus the triple-blind cross-line
master inequality does not contradict this abstract lift.

This is not a construction of a word: it checks only the scalar,
line-capacity, level-placement, and pair-intersection ledgers.  It has no
third direction, so `J=0`; the stronger local charge is `R>=I-O(a)`, which
this lift fails.  Theorem 8.1 is exactly the refinement which excludes it.

## 9. Ledger

### Proved here

* The finite mixed-tail master inequality (1.2)/(3.5) for every fixed
  `b>1`.
* The strongest limiting joint lift condition (4.8), including the
  additive-triple density.
* The fringe-pair estimate (4.12) and explicit triple-blind scalar envelope
  (5.11).
* Mixed-profile boundary saturation `sigma=3` under support away from zero,
  `D=o(a^2)`, and vanishing small-threshold seam mass.
* The endpoint-mass exclusion (7.5) and total-count exclusion (7.10) for
  measures supported on `[4/3,3/2]` under those hypotheses.
* The stronger Theorem 8.1 excluding every limiting measure supported on
  `[4/3,3/2]` under the same `D` and vanishing-seam hypotheses.

### Not proved

* A closed solution of the enriched variational gate (4.8) for arbitrary
  tails with mass outside `[4/3,3/2]`.
* A stability theorem for profiles only approximately, rather than exactly,
  supported on `[4/3,3/2]`.
* Any conclusion for a positive-seam profile merely from its scalar seam
  upper bounds.
* The full three-box or Boolean-lattice conjecture.
