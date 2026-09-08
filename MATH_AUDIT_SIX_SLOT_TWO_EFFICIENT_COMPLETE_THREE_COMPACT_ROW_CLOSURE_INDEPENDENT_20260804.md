# Independent audit: complete six-slot size-two / three-compact-row closure

**Date:** 2026-08-04  
**Verdict:** **GO.**  The exact two-pulse normal form, scalar domain,
three-compact-row derivative, tail comparison, concavity reductions,
endpoint identifications, rational certificates, and final branch
implication are all correct.  No theorem byte was changed during this
audit.

## 1. Exact binding and dependencies

Audited theorem:

`MATH_THEOREM_SIX_SLOT_TWO_EFFICIENT_COMPLETE_THREE_COMPACT_ROW_CLOSURE_20260804.md`

SHA-256:

`53a65d72f9f6a22ccef91f43c5759c61fc0a0ea831294b71b56a46d1cae95d3a`

This is the current theorem hash; it supersedes the earlier delegated
prefix `23e639...`.

Every frozen dependency hash matches the current workspace:

| role | SHA-256 |
|---|---|
| all-slot first crossing and saturation | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| independent all-slot audit | `d404632e3bd805f92333276c74d3a094991da224f22259f11ba24193c0842173` |
| complete positivity through five | `69d8d73e52342a74d11a8673811e0d41d15063a2d66d1fdbc504138b4ed76bed` |
| exact five-slot two-pulse normal form | `2ba2be5a52e4761790f031fcc63955c8066fd032fc3afaa81de866b50abd9b9e` |
| five-slot wedge and authenticated edges | `a678fc5a33c6457d9d640aa963d902fdb8c7ed932ade6a14fd320caf8d285e43` |
| compact `G` monotonicity | `b494371c790ed20f14e29bd4beba67b27aa30f7f5b1447e4ef8da4e74db8ea14` |
| all-ceiling positivity | `18a5d75526774673909d29a26d93710a1d56e9298c51d3a4cebaa8ebcd62baf3` |
| independent all-ceiling audit | `9f807a2a044469bed61c2943adf51b48f71ce594748cc8d3fb41ceea3394ac39` |

## 2. Exact normal form and domain

Let the table be `(0,x,y,z,w,T,E)` with first crossing at six and size two
of maximum density.  Density and superadditivity give both directions in

\[
 w=2y,qquad E=3y.
\]

Also

\[
 z\ge x+y,qquad T\ge y+z,qquad T\le5y/2.
\]

With `s=T-2y`, these are exactly

\[
 0\le x\le z-y\le s\le y/2.
\]

The first-crossing inequalities `w<A<=E` and `T<A` give

\[
 A/3\le y<A/2,qquad s<A-2y.
\]

For even capacities, density bounds every fill by `my/2` and size-two
parts attain it.  For an odd fill, pair all but one odd generator; every
even generator or paired odd block can be replaced by size-two generators
without loss.  The remaining odd representative has size one, three, or
five, with shifts

\[
 x,qquad z-y,qquad s,
\]

in increasing order.  The best representative, size five, first becomes
available at capacity five.  Therefore

\[
 V_{2q}=qy,quad V_1=x,quad V_3=z,quad
 V_{2q+1}=qy+s\quad(q\ge2)
\]

and the only head corrections are exactly those at capacities one and
three.  The size-six generator is identical to three size-two generators
and creates no later transient.

After `y=At`, `s=Au`, the honest strict domain is contained in the closed
triangle

\[
 1/3\le t\le1/2,qquad
 0\le u\le\min\{t/2,1-2t\}.
\]

Adjoining `u=1-2t` and the empty physical edge `t=1/2` is harmless for a
sufficient continuous inequality.

## 3. Derivative and tail direction

On this triangle,

\[
 u,\quad t+u,\quad2t+u\in[0,1].
\]

Thus period rows `q=0,1,2` use the complete compact derivative

\[
 R(v)=h(1-v)-h(1+v).
\]

Every `q>=3` argument is at least one, and the compact and tail derivative
formulas agree at equality.  Termwise differentiation consequently gives

\[
 {d\over du}F_{At}(Au)=-2A^2W_t(u)
\]

with exactly the displayed `W_t`.

For `q>=3`, the first `h` argument is at least two, where `h` decreases.
For a decreasing function, each point is bounded above by the average over
its preceding interval.  Summing those intervals gives

\[
 \sum_{q\ge3}h(1+u+qt)
 \le {1\over t}\int_{1+u+2t}^{\infty}h(v)\,dv
 ={e^{-\alpha(1+u+2t)^2}\over2\alpha t}.
\]

Hence `W_t>=H_t`; the inequality is in the required direction for proving
the derivative negative.

## 4. Concavity and exhaustive boundary rows

Writing

\[
 G(v)=h'(1+v)+h'(1-v)
\]

gives `R'(v)=-G(v)`.  The cited compact lemma proves `G` strictly
increasing through `1/2`; on `[1/2,1]`,
`h''(1-v)<=0<h''(1+v)`, so it remains strictly increasing.  Therefore
`R` is concave on `[0,1]`.

The exponential quotient in `H_t` has positive second derivative in `u`,
so its negative is concave.  Thus `H_t` is strictly concave in `u` and its
minimum lies at a shift endpoint.

The upper shift changes at `t=2/5`:

* `M(t)=H_t(0)` is needed on `1/3<=t<=1/2`;
* `N(t)=H_t(t/2)` is needed on `1/3<=t<=2/5`;
* `L(t)=H_t(1-2t)` is needed on `2/5<=t<=1/2`.

For

\[
 Q_c(t)={e^{-\alpha(1+ct)^2}\over2\alpha t},
\]

the displayed logarithmic differentiation is exact.  The lower bounds

\[
 2/t^2-2\alpha(2)^2\ge8-2\pi>0
\]

and

\[
 2/t^2-2\alpha(5/2)^2
 \ge25/2-25\pi/8>0
\]

prove the relevant quotients convex.  Hence `M,N` are concave and attain
their minima at their interval endpoints.  The three rows listed above
therefore exhaust the whole triangular domain.

At `M(1/2)`, the new third compact term has argument one and its missing
mirror is `h(0)=0`; the expression is exactly the authenticated five-slot
lower edge `L(1/2)`.  Likewise `N(2/5)` is exactly the authenticated
five-slot upper edge.  Both exceed `1/100`.

## 5. Exact endpoint expansions and certificates

Direct expansion independently reproduces

\[
\begin{aligned}
M(1/3)={}&{2\over3}e^{-\pi/9}+{1\over3}e^{-\pi/36}
 -{4\over3}e^{-4\pi/9}\\
&-\left({5\over3}+{6\over\pi}\right)e^{-25\pi/36},
\end{aligned}
\]

and

\[
\begin{aligned}
N(1/3)={}&{5\over6}e^{-25\pi/144}
 +{1\over2}e^{-\pi/16}+{1\over6}e^{-\pi/144}\\
&-{7\over6}e^{-49\pi/144}-{3\over2}e^{-9\pi/16}\\
&-\left({11\over6}+{6\over\pi}\right)e^{-121\pi/144}.
\end{aligned}
\]

Using `333/106<pi<22/7`, exact rational cross-multiplication gives the
following positive margins for the seven displayed certificates:

\[
\begin{array}{c|c}
\text{certificate}&\text{exact positive margin}\\ \hline
P_5(74/53)>4&170381813/6272932395\\
P_8(925/424)>200/23&
31178084968906145054363147/193733715610425264200220672\\
M(1/3)>1/50&4709815/444083472\\
P_5(1813/1696)>20/7&622886529839366531/11787142275362979840\\
P_5(2997/1696)>40/7&328773932550792993/3929047425120993280\\
P_8(4477/1696)>40/3&
1802829855547368535169466478241/2760115823096702198831665643520\\
N(1/3)>1/20&350735083/7681443840
\end{array}
\]

Here the labels in the last column mean the left side of each theorem
inequality minus its claimed right side.  Every denominator is positive.
The lower exponential bounds use the odd Taylor polynomial `Q_3`; the
upper bounds use `e^x>P_m(x)`, so every inequality direction is safe.

Concavity now yields `M>0` and `N>0` on their complete intervals, while
the authenticated row gives `L>0`.

## 6. Scalar and literal branch closure

The three positive rows imply `H_t(u)>0`, hence `W_t(u)>0` and

\[
                         {d\over du}F_{At}(Au)<0.
\]

For `t<=2/5`, decreasing the shifted train gives

\[
 \mathcal L_2(At;Au)
 \ge\mathcal L_2(At;At/2)=C(At/2)>0.
\]

For `t>=2/5`, it gives the lower comparison with the authenticated
five-slot edge `u=1-2t`, which is strictly positive.  This proves the
scalar inequality on the entire honest domain.

Finally, `x<=s<A/4` and `z<=y+s<3A/4`; monotonic decrease of `K` through
`3A/4` makes both finite corrections nonnegative.  The scalar term is
strictly positive, so the literal six-slot functional is strictly
positive.

The theorem closes exactly the normalized size-two maximum-density branch.
It makes no claim about least-maximizer sizes three, four, or five, the
complete six-slot problem, the all-grid inequality, or OR words.
