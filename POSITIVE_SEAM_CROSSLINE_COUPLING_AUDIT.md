# Independent audit of `POSITIVE_SEAM_CROSSLINE_COUPLING.md`

## 1. Verdict

I audited the finite set accounting, the atomic limiting argument, the
boundary-reservoir step, the three-direction variational optimization, and
the endpoint profile independently.  I found no counterexample and no
substantive mathematical gap.  Subject to the inherited three-box framework,
the main conclusions are valid with the scopes stated below:

* the finite coupling

  \[
  \Gamma_a\leq \Gamma_{0,a}+\Delta_a
  \]

  is unconditional and exact;
* atomic seam linearity is independent of the selected-order defect `D`;
* the cross-line envelope and the exclusion

  \[
  x>1+\frac{8-2\sqrt3}{13}
  \]

  are also independent of `D` and of any small-seam hypothesis;
* the lower bound on `Gamma` and therefore the positive desert-density bound
  use the inherited hypothesis `D=o(a^2)` through the quadratic reservoir
  law;
* the balanced data at `x=4/3` are a consistent **static limiting ledger**,
  not a geometrically realized permutation word.

There are four presentation qualifications worth recording.

1. In the statement of seam linearity, “every fixed `c<x`” should be read as
   every fixed **positive** threshold `0<c<x`, the domain in which the
   first-dangerous seam functional is defined.
2. Section 4 uses an ideal cap `(4-x)a`, while Section 2 initially defines
   the finite core with the actual cap `L-lambda(P)`.  Their total difference
   is `o(a^2)` under the atom hypothesis, so they have the same limiting
   `Gamma`; this asymptotic identification should be made explicit.
3. In the reservoir proof, exceptional plateaux can contaminate
   gap-contained windows.  There are only `o(a)` of them and deleting their
   `O(a)`-sized window neighbourhoods costs `o(a^2)`, which repairs the
   compressed sentence in Section 5.
4. Lemma 6.1 omits one short endpoint comparison: the value at the internal
   endpoint `a=1` is at most `2/3`.  The missing check is elementary and is
   supplied below.

None of these qualifications changes a constant, threshold, or theorem.

## 2. Exact finite seam--line coupling

Let `V` be the union of the selected plateau-vertex intervals, `Lambda` the
union of their complete coordinate lines, and `C` a disjoint union of chosen
positions from the predecessor complement gaps.  By construction,

\[
V\subseteq\Lambda,\qquad C\cap V=\varnothing.
\]

Consequently

\[
C\cap\Lambda\subseteq\Lambda\setminus V.
\]

This gives the exact finite inequality

\[
|C|=|C\setminus\Lambda|+|C\cap\Lambda|
   \leq |C\setminus\Lambda|+|\Lambda\setminus V|.
\]

After division by `a^2`, this is precisely

\[
\boxed{\Gamma_a\leq\Gamma_{0,a}+\Delta_a}.
\]

No atomic convergence, line distinctness, run spectrum, seam theorem, or
`D=o(a^2)` is needed for this inclusion.  Distinct selected lines become
important only when `Delta` is evaluated by line-intersection accounting.

For the weighted statement, write

\[
w_j=\frac{\lambda_j-ca}{a}.
\]

Since every plateau length is at most `2a`, one has

\[
0<w_j\leq2-c.
\]

The gap cores `C_j` are disjoint, hence

\[
\begin{aligned}
H_a(c)
 &=\frac1{a^2}\sum_jw_j|C_j|\\
 &=H_{0,a}(c)+\frac1{a^2}\sum_jw_j|C_j\cap\Lambda|\\
 &\leq H_{0,a}(c)+(2-c)\frac{|\Lambda\setminus V|}{a^2}.
\end{aligned}
\]

This verifies (2.6).  If a fixed tail threshold `b>1` is used, the atom's
regular plateaux eventually have length greater than `ba`.  The omitted
exceptional family has `o(a)` members, and each omitted weighted core is
`O(a^2)` before division by `a^3`; its total normalized contribution is
therefore `o(1)`.

## 3. `Delta` is the exact line-union slack

A selected coordinate line at integer level `t` contains

\[
2a-|t|+1
\]

points.  Thus the sum of the complete-line cardinalities is

\[
2am-T+m,
\qquad T=\sum_P|t(P)|.
\]

Lines in one direction are disjoint.  Among lines in different directions,
each genuinely intersecting pair contributes one intersection point; a point
on all three selected directions has been subtracted three times and must be
added once.  Therefore inclusion--exclusion gives exactly

\[
|\Lambda|=2am-T+m-I+J.
\]

The selected plateau has `lambda(P)+1` vertices.  Plateau edge intervals are
disjoint, and only consecutive intervals may share a word endpoint.  If
`omega=O(m)` is the total number of those shared endpoints, then

\[
|V|=\sum_P\lambda(P)+m-\omega.
\]

Subtracting yields

\[
a^2\Delta_a
=2am-T-\sum_P\lambda(P)-I+J+\omega.
\]

For a fixed threshold above one, `m=O(a)`, so `omega/a^2=o(1)`.  With

\[
\frac ma\to f,\quad
\frac T{a^2}\to\tau,\quad
\frac1{a^2}\sum_P\lambda(P)\to\ell,
\]

and

\[
\frac I{a^2}\to\frac{f^2-s_2}{2}-\eta,
\qquad \frac J{a^2}\to\theta,
\]

one obtains

\[
\boxed{
\Delta=2f-\tau-\ell-\frac{f^2-s_2}{2}+\eta+\theta.}
\]

Thus the limiting mixed cross-line inequality is literally `Delta>=0`; no
extra asymptotic slack has been lost.

## 4. Atomic seam linearity

Assume

\[
\mu_a=\frac1a\sum_P\delta_{\lambda(P)/a}
\Longrightarrow2\delta_x.
\]

For every fixed `epsilon>0`, all but `o(a)` plateaux obey

\[
|\lambda(P)/a-x|<\epsilon.
\]

Compact support and weak convergence also give the stronger first-moment
error

\[
\sum_P|\lambda(P)-xa|=o(a^2).
\]

Fix two positive thresholds below `x`.  Their dangerous lists differ from
the common regular list in only `o(a)` plateaux.  Inserting or deleting one
plateau changes at most a bounded number of predecessor-gap terms, each
capped by `O(a)`, so it changes the unweighted clipped sum by `O(a)`.
All insertions and deletions therefore cost `o(a^2)`.

For a regular successor, compare the actual cap with the ideal cap:

\[
\left|(L-\lambda(P))-(4-x)a\right|
 \leq |\lambda(P)-xa|+2.
\]

Since `g -> min(g,B)` is one-Lipschitz in `B`, summing this error gives
`o(a^2)`.  Consequently all fixed thresholds below `x` share, up to `o(1)`,
the normalized clipped-gap density

\[
\Gamma_a=\frac1{a^2}
 \sum_{P\ \mathrm{regular}}
 \min\{g_{\rm pred}(P),(4-x)a\}.
\]

Pass to a subsequence on which `Gamma_a -> Gamma`.  Expanding

\[
\lambda(P)-ca=a(x-c)+(\lambda(P)-xa)
\]

in the seam sum, the error term is bounded by

\[
O(a)\sum_P|\lambda(P)-xa|=o(a^3).
\]

The cap-replacement and exceptional-family errors are also `o(a^3)`.
Hence, on this same subsequence, for every fixed `0<c<x`,

\[
\boxed{H_a(c)=(x-c)\Gamma_a+o(1)},
\qquad
\boxed{H(c)=(x-c)\Gamma}.
\]

There is no threshold-dependent subsequence hidden here: once `Gamma_a`
converges, the displayed error estimate applies separately to every fixed
positive `c<x`.

## 5. Sharpened lower bound on `Gamma`

Under the atom hypothesis, the regular plateau edge mass is

\[
(2x+o(1))a^2.
\]

Passing from edge mass to the union of plateau vertices changes the count by
only `O(a)`, so the complement of the regular plateau union has size

\[
(3-2x+o(1))a^2.
\]

For an internal complement gap of length `g`, the number of positions with
neither a forward nor a backward gap-contained length-`L` window is

\[
I_L(g)\leq\min\{g,L\}.
\]

Set `B=(4-x)a`.  The elementary comparison

\[
\min\{g,L\}\leq\frac LB\min\{g,B\}
\]

holds for every `g`, and

\[
\frac LB\longrightarrow\frac4{4-x}.
\]

The two outside word gaps contribute only `O(a)` invisible positions.
The `o(a)` exceptional plateaux and all windows meeting them may be deleted
at a cost `o(a) O(a)=o(a^2)`.  Every remaining complement position not
charged by the ideal clipped cores has a valid one-sided window containing
no complete `c`-dangerous plateau, and hence lies in `R_c`.  This gives

\[
3-2x
\leq \limsup\frac{|R_c|}{a^2}
   +\frac4{4-x}\Gamma.
\]

This is the first point where `D=o(a^2)` is used.  The audited subset
run-spectrum theorem supplies, for every fixed `0<c<2/3`,

\[
\limsup\frac{|R_c|}{a^2}\leq\frac94c^2.
\]

Take the large-`a` limit with `c` fixed and only then let the numerical
threshold tend to zero.  The result is

\[
\boxed{
\Gamma\geq\frac{4-x}{4}(3-2x).}
\]

Without `D=o(a^2)`, the finite coupling and seam linearity remain valid, but
this lower bound on `Gamma` is not presently justified.

## 6. Independent verification of the cross-line envelope

Put `u=x-1`, so `1/3<=u<=1/2`.  For a tail threshold approaching `x` from
below, the atom has count mass `f=2`, edge mass

\[
\ell=2x=2+2u,
\]

and direction masses satisfying

\[
0\leq\alpha_i\leq2(1-u),
\qquad\sum_i\alpha_i=2.
\]

The mixed cross-line capacity is

\[
2+\frac12\sum_i\alpha_i^2-\tau+\eta+\theta.
\]

### 6.1 Nonintersection and level cost

All selected normalized levels lie in `[-(1-u),1-u]`.  Given a level `v`,
the mass in one other direction which can fail to intersect it is at most

\[
(|v|-u)_+.
\]

Summing over the two other directions and dividing by two because every
unordered nonintersection is seen at both endpoints gives

\[
\eta\leq\sum_i\int(|v|-u)_+\,d\nu_i(v).
\]

Therefore

\[
\tau-\eta\geq\sum_i h_u(\alpha_i),
\]

where centered compression gives

\[
h_u(t)=
\begin{cases}
t^2/4,&0\leq t\leq2u,\\
ut-u^2,&2u\leq t\leq2(1-u).
\end{cases}
\]

This computation correctly uses level measures dominated by Lebesgue
measure; it does not assume that their densities are uniform.

### 6.2 Triple intersections

For masses sorted as `alpha>=beta>=gamma`, the discrete one-dimensional
rearrangement inequality and scaling give

\[
\theta\leq
\beta\gamma-\frac14(\beta+\gamma-\alpha)_+^2.
\]

This is the centered-interval convolution formula.  The same-level
uniqueness required to regard the selected levels as sets is valid for the
regular atom family because `x>1`; exceptional plateaux vanish in the
limit.

### 6.3 Three-variable maximization

Define

\[
A_u(t)=\frac{t^2}{2}-h_u(t).
\]

Sort the masses as `a>=y>=z` and put `r=y+z=2-a`.  At fixed `a`,

\[
A_u(y)+A_u(z)+yz
\]

is concave as a function of `y`: piecewise its second derivative is

\[
A_u''(y)+A_u''(z)-2\leq0,
\]

and the first derivative is continuous across `2u`.  Symmetry therefore
allows `y=z=1-a/2`.  The remaining triple-correction term depends only on
`a` and `r`.

Since `a>=2/3`, this common smaller mass is at most `2u`.  Direct substitution
gives the three expressions in the source:

\[
\frac12+\frac a2-\frac{3a^2}{8}
\quad(a\leq2u),
\]

\[
u^2+\frac12+\left(\frac12-u\right)a-\frac{a^2}{8}
\quad(2u\leq a\leq1),
\]

and

\[
u^2+\frac32-\left(\frac32+u\right)a+\frac{7a^2}{8}
\quad(1\leq a\leq2(1-u)).
\]

The first two are nonincreasing on their stated domains; the third is
convex.  Its internal endpoint value is

\[
V(1)=u^2-u+\frac78\leq\frac23
\qquad(1/3\leq u\leq1/2),
\]

because

\[
u^2-u+\frac5{24}\leq0
\]

on this interval.  Thus the only global candidates are the balanced point
`(2/3,2/3,2/3)` and the capped point
`(2(1-u),u,u)`.  Their values are respectively

\[
\frac23,
\qquad 2-6u+\frac{13}{2}u^2.
\]

Hence

\[
\boxed{
M(u)=\max\left\{\frac23,
2-6u+\frac{13}{2}u^2\right\}.}
\]

I also evaluated the original three-variable objective on a fine grid over
the full feasible simplex for 101 values of `u` in `[1/3,1/2]`; every value
agreed with this closed envelope to the grid tolerance.  This is only a
sanity check; the preceding case analysis is the proof.

## 7. Threshold and cross-line slack

The required edge mass forces

\[
2+2u\leq2+M(u),
\qquad\text{or equivalently}\qquad 2u\leq M(u).
\]

The first branch `2/3` is strictly smaller than `2u` for `u>1/3`.  The
second branch meets `2u` when

\[
13u^2-16u+4=0.
\]

The relevant root is

\[
\boxed{u_* = \frac{8-2\sqrt3}{13}=0.348915\ldots.}
\]

Between this root and `1/2`, the quadratic branch is also strictly smaller
than `2u`.  Therefore every atom with `u>u_*` is impossible.  This
exclusion uses neither `D=o(a^2)` nor any hypothesis about `H`.

For `1/3<=u<=u_*`, the quadratic branch exceeds `2/3`, so subtracting the
required edge mass from the capacity gives

\[
\boxed{
\Delta\leq2-8u+\frac{13}{2}u^2.}
\]

The phrase “unconditional atomic exclusion” should be understood in this
precise sense: it is unconditional with respect to the selected-order defect
and seam mass, while retaining the atom hypothesis and the inherited
three-box word geometry.

## 8. Desert-density inequality

Use the common regular family and choose its ideal clipped cores.  As noted
in Section 4, changing back to the actual caps modifies their total size by
`o(a^2)`, so the finite coupling implies on the chosen cross-line
subsequence

\[
\Gamma_{0,a}\geq\Gamma_a-\Delta_a+o(1).
\]

Taking a liminf on the left and genuine limits on the right gives

\[
\liminf\Gamma_0\geq\Gamma-\Delta.
\]

Now insert the lower bound from Section 5 and the upper bound from Section 7:

\[
\begin{aligned}
\liminf\Gamma_0
&\geq\frac{3-u}{4}(1-2u)
  -\left(2-8u+\frac{13}{2}u^2\right)\\
&=\boxed{\frac{-5+25u-24u^2}{4}}.
\end{aligned}
\]

Its smaller zero is

\[
\frac{25-\sqrt{145}}{48}<\frac13,
\]

and its larger zero is above the interval under consideration.  Hence it is
strictly positive for every `1/3<=u<=u_*`.  At the two endpoints it gives

\[
\liminf\Gamma_0\geq\frac16
\quad(u=1/3),
\]

and, since the cross-line slack bound vanishes at `u_*`,

\[
\liminf\Gamma_0\geq\frac{3-u_*}{4}(1-2u_*)>0.
\]

This theorem does depend on `D=o(a^2)`, solely through the lower bound on
`Gamma`.

## 9. The balanced `x=4/3` abstract survivor

Take

\[
\mu=2\delta_{4/3},
\qquad
\nu_x=\nu_y=\nu_z={\bf1}_{[-1/3,1/3]}\,du.
\]

Then

\[
f=2,\qquad
\alpha_i=\frac23,\qquad
s_2=\frac43,\qquad
\tau=3\int_{-1/3}^{1/3}|v|\,dv=\frac13.
\]

Every pair of selected normalized levels intersects because
`|u+v|<=2/3`, so `eta=0`.  Centered interval convolution gives

\[
\theta=\frac49-\frac19=\frac13.
\]

The exact cross-line expression is therefore

\[
4-\frac13-\frac43+\frac13=\frac83,
\]

equal to the required edge mass.  Thus `Delta=0`.  The ambient normalized
area is `3`, so the complement of the line union has density `1/3`.

Choose the static densities

\[
\Gamma=\Gamma_0=\frac29.
\]

They obey the exact coupling with equality, fit within the outside-line
area `1/3`, and yield

\[
H(c)=\left(\frac43-c\right)\frac29,
\qquad0<c<\frac43.
\]

The sharpened boundary law is also tight as `c` tends to zero:

\[
\frac4{4-4/3}\Gamma
=\frac32\frac29
=\frac13
=3-2\left(\frac43\right).
\]

For completeness, this profile passes the other cited scalar gates:

* edge mass is `8/3<=3`;
* line capacity holds because the count tail is `2<=6(2-4/3)=4`;
* the mass law holds since

  \[
  2e(c)=4(4/3-c)\geq4-3c;
  \]

* weighted supply is `2(4-4/3)=16/3`, above its required lower bound;
* the seam upper bounds hold because

  \[
  H(c)\leq(4-c)e(c),
  \qquad
  H(c)\leq(2-c)(3-8/3);
  \]

* the general boundary lower bound is weaker: before the atom is crossed it
  asks for at most

  \[
  \frac{4/3-c}{2}\left[\frac13-\frac94c^2\right]_+,
  \]

  whose coefficient is at most `1/6<2/9`.

These checks establish consistency of the **aggregate data only**.  They do
not place the desert points between particular successive plateaux, orient
plateau intervals on their lines, or produce a permutation.  Thus the source
correctly identifies the survivor as a no-go example for further scalar or
static level-set optimization, not as evidence that the endpoint is
geometrically realizable.

## 10. Counterexample stress tests

I tested the natural failure modes against the proof.

* **Reuse a selected line.**  Two regular atom plateaux have lengths greater
  than `a`; two such disjoint edge intervals cannot fit on one coordinate
  line of at most `2a` edges.  Reuse is confined to the `o(a)` exceptional
  family and vanishes from the limiting line ledger.
* **Hide seam cores on used plateau vertices.**  Impossible: predecessor-gap
  positions lie outside the plateau vertex union by definition.
* **Let one exceptional plateau contaminate a macroscopic gap.**  It can
  contaminate only `O(L)=O(a)` candidate window starts.  There are `o(a)`
  exceptions, so the total loss is `o(a^2)`.
* **Concentrate all complement at a word boundary.**  Only `O(L)` positions
  there lack the available one-sided gap-contained window; the remaining
  quadratic mass enters `R_c` and is caught by the reservoir law.
* **Exploit limsup/liminf mismatch.**  After taking a common subsequence on
  which the level data and `Delta_a` converge, the pointwise finite inequality
  gives `liminf Gamma_0 >= Gamma-Delta`; no illicit reversal of limsup and
  liminf is used.
* **Unbalance direction masses.**  The capped endpoint
  `(2(1-u),u,u)` is already included in `M(u)` and is exactly the competing
  maximizer responsible for the threshold `u_*`.

None produces a counterexample.

## 11. Final theorem ledger

### Proved without `D=o(a^2)`

* `Gamma_a<=Gamma_(0,a)+Delta_a` and its weighted version;
* the exact identity interpreting `Delta` as unused selected-line-union
  capacity;
* atomic multiscale seam linearity for fixed positive thresholds;
* the closed cross-line envelope `M(u)`;
* exclusion of every atom

  \[
  2\delta_x,\qquad
  x>1+\frac{8-2\sqrt3}{13}.
  \]

### Proved using `D=o(a^2)`

* `Gamma >= ((4-x)/4)(3-2x)`;
* the positive cross-line-desert lower bound

  \[
  \liminf\Gamma_0
  \geq\frac{-5+25u-24u^2}{4}
  \quad(1/3\leq u\leq u_*).
  \]

### Consistent but not geometrically realized

* the balanced endpoint ledger

  \[
  \mu=2\delta_{4/3},\quad
  \nu_i={\bf1}_{[-1/3,1/3]}du,\quad
  \Gamma=\Gamma_0=2/9.
  \]

### Still open

* an ordering theorem for the positive-density cross-line-desert points;
* exclusion or construction of the endpoint `2delta_(4/3)`;
* a corresponding threshold-independent desert coupling for arbitrary mixed
  profiles; and
* the full three-box obstruction and the Boolean-lattice conjecture.
