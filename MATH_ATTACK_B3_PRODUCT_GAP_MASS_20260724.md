# Third-wave B: mass and coefficient loss of obstructed three-chain product boxes

Date: 2026-07-24

## 0. Verdict

Split a Boolean cube into three equal blocks of dimension \(s\), choose an
arbitrary symmetric-chain decomposition in each block, and form the
three-chain product boxes.  If a box is selected uniformly, divide its
three chain heights by \(\sqrt s\), and sort them as

\[
A<B<C.
\]

Then \(A,B,C\) are asymptotically the order statistics of three independent
standard Rayleigh variables.  The two obstruction cones have the exact
limiting box masses

\[
\boxed{
\Pr(C>A+B)=1-\frac{\pi}{3\sqrt3},\qquad
\Pr(C>2B)=\frac15.}
\tag{0.1}
\]

They also carry positive, explicitly computable fractions of the *global
Boolean middle width*:

\[
\boxed{
\Omega_{C>A+B}
=\frac43-\frac{2\sqrt3}{\pi}>0,}
\tag{0.2}
\]

\[
\boxed{
\Omega_{C>2B}
=
\frac{2\sqrt3}{\pi}
\left(
\frac{6\sqrt5}{25}\arctan\frac1{\sqrt5}
-\frac2{15}
\right)>0.}
\tag{0.3}
\]

Thus the obstructed boxes are not a negligible tail under either box-count
measure or width measure.

There is an unconditional coefficient no-go.  Let \(L_{\rm sep}(3s)\) be
the length obtained by using an optimal local word in every product box and
concatenating the translated words independently, with the necessary local
origin anchors.  Then

\[
\boxed{
\liminf_{s\to\infty}
\frac{L_{\rm sep}(3s)}{\binom{3s}{\lfloor3s/2\rfloor}}
\ge 1+\delta_0,}
\tag{0.4}
\]

where

\[
\boxed{
\delta_0
=
\frac{3\sqrt3}{5\pi\sqrt5}\arctan\frac1{\sqrt5}
-\frac{\sqrt3}{10\pi}
>0.}
\tag{0.5}
\]

The constant in (0.5) is an exact closed-form **certified lower
coefficient**.  It is not asserted to be the true optimal loss of separate
concatenation: that would require a matching asymptotic formula for the
unknown local optimum \(g_3(p,q,r)\).  The exact finite coefficient ledger
is proved in Section 5.

More generally, every fixed three-way split with positive limiting block
proportions has a strictly positive coefficient loss under independent
box concatenation.  Changing the SCDs cannot help, because their height
histograms are invariant.  Theorem 6.2 further rules out every sequence of
three-way dimension splits, including sequences whose proportions approach
the boundary of the dimension simplex.

This kills the independently concatenated three-block product route.  It
does not disprove the contiguous-OR width conjecture.  A rescue must replace
the additive box ledger by cross-box witness sharing or by genuinely fused
higher-dimensional parents.  Section 7 gives the exact saving scale and
the smallest clean replacement lemma.

No web search, finite search, or computational experiment is used.

## 1. The exact SCD height law

Write

\[
W(s)=\binom{s}{\lfloor s/2\rfloor}.
\]

Every SCD of the \(s\)-cube contains exactly \(W(s)\) chains.

### Lemma 1.1 (histogram and exact tail)

Let \(H_s\) be the edge height of a chain selected uniformly from an
arbitrary SCD of \(2^{[s]}\).  The number of height-\(h\) chains is

\[
c_s(h)=
\binom{s}{(s-h)/2}
-\binom{s}{(s-h)/2-1}
\tag{1.1}
\]

when \(h\equiv s\pmod2\), and is zero otherwise.

Put

\[
m=\lfloor s/2\rfloor,\qquad
\epsilon_s=s-2m\in\{0,1\}.
\]

For \(0\le j\le m\),

\[
\boxed{
\Pr(H_s\ge \epsilon_s+2j)
=
\frac{\binom{s}{m-j}}{\binom{s}{m}}.}
\tag{1.2}
\]

In particular, both the histogram and the law of \(H_s\) are independent
of the chosen SCD.

#### Proof

At rank \(a\le s/2\), exactly \(\binom{s}{a-1}\) chains have already
started below rank \(a\).  Every one contains one rank-\(a\) point.
Consequently the number of chains starting at rank \(a\) is

\[
\binom{s}{a}-\binom{s}{a-1}.
\]

Such a symmetric chain ends at rank \(s-a\) and has edge height \(s-2a\),
which proves (1.1).  Heights at least \(\epsilon_s+2j\) correspond to
starting ranks \(a\le m-j\).  Summing the preceding differences telescopes
to \(\binom{s}{m-j}\), proving (1.2). \(\square\)

### Lemma 1.2 (Rayleigh limit with moments)

As \(s\to\infty\),

\[
\boxed{
\frac{H_s}{\sqrt s}\Longrightarrow Y,\qquad
f_Y(y)=y e^{-y^2/2}\quad(y>0).}
\tag{1.3}
\]

All fixed polynomial moments converge.  For chains selected independently
from different block SCDs, the limiting Rayleigh variables are independent.

#### Proof

For even \(s=2m\),

\[
\frac{\binom{2m}{m-j}}{\binom{2m}{m}}
=
\prod_{r=1}^{j}\frac{m-r+1}{m+r},
\tag{1.4}
\]

and for odd \(s=2m+1\),

\[
\frac{\binom{2m+1}{m-j}}{\binom{2m+1}{m}}
=
\prod_{r=1}^{j}\frac{m-r+1}{m+r+1}.
\tag{1.5}
\]

For \(j=O(\sqrt s)\), expanding the logarithms uniformly gives

\[
\log
\frac{\binom{s}{m-j}}{\binom{s}{m}}
=-\frac{2j^2}{s}+o(1).
\tag{1.6}
\]

If \(\epsilon_s+2j\sim y\sqrt s\), the right side tends to
\(-y^2/2\).  Equation (1.2) therefore gives

\[
\Pr(H_s/\sqrt s\ge y)\longrightarrow e^{-y^2/2},
\]

which is (1.3).

The same products, using \(\log(1-u)\le-u\), give absolute constants
\(c,C>0\) such that

\[
\Pr(H_s\ge t\sqrt s)\le Ce^{-ct^2}
\qquad(t\ge0).
\tag{1.7}
\]

This uniform Gaussian tail proves uniform integrability of every fixed
polynomial in \(H_s/\sqrt s\), hence moment convergence.  Independence is
exact before taking the limit. \(\square\)

For later use, if \(s_i/N\to\alpha_i>0\) and \(H_i\) is the uniform SCD
height in block \(i\), then

\[
\frac{H_i}{\sqrt N}\Longrightarrow X_i,
\qquad
f_{\alpha_i}(x)
=\frac{x}{\alpha_i}e^{-x^2/(2\alpha_i)}
\quad(x>0),
\tag{1.8}
\]

independently.  Polynomially bounded almost-everywhere continuous
functions of the normalized height triple converge in expectation by
(1.7).

## 2. Product boxes and the exact width measure

Take three blocks \(X_1,X_2,X_3\), each of size \(s\), and arbitrary SCDs
\(\mathcal D_i\).  A triple of chains of heights \(p,q,r\) gives a product
box

\[
[0,p]\times[0,q]\times[0,r].
\]

Let \(w_3(p,q,r)\) be its width.  The product boxes partition the Boolean
cube, and each has the symmetric unimodal rank polynomial
\[
(1+z+\cdots+z^p)(1+z+\cdots+z^q)(1+z+\cdots+z^r)
\]
centered at global rank \(3s/2\).  Therefore their local middle antichains
partition the global middle layer:

\[
\boxed{
\sum_{\text{product boxes}}w_3(p,q,r)=W(3s).}
\tag{2.1}
\]

The number of boxes is

\[
\mathcal B_s=W(s)^3.
\tag{2.2}
\]

Stirling's formula gives the exact normalization

\[
\boxed{
\frac{s\mathcal B_s}{W(3s)}
\longrightarrow\frac{2\sqrt3}{\pi}.}
\tag{2.3}
\]

If \(0\le p\le q\le r\) and \(r\ge p+q\), projection to the first two
coordinates is injective on every antichain, while every rank from \(p+q\)
through \(r\) contains one point above every \((x,y)\).  Hence

\[
\boxed{
w_3(p,q,r)=(p+1)(q+1)
\qquad(r\ge p+q).}
\tag{2.4}
\]

Let \(A<B<C\) be the order statistics of three independent standard
Rayleigh variables.  Equations (1.3), (1.7), and (2.3)--(2.4) imply that
for either cone

\[
\mathcal E\in
\bigl\{\{C>A+B\},\{C>2B\}\bigr\},
\]

\[
\boxed{
\frac1{W(3s)}
\sum_{\substack{\text{boxes}\\
                 (p_{(1)},p_{(2)},p_{(3)})/\sqrt s
                 \in\mathcal E}}
w_3(p,q,r)
\longrightarrow
\frac{2\sqrt3}{\pi}
\mathbb E\!\left[AB\,\mathbf1_{\mathcal E}\right].}
\tag{2.5}
\]

The cone walls have limiting measure zero.  The moment bound (1.7)
justifies the unbounded weight \(AB\).

For general positive proportions \(s_i/N\to\alpha_i\), put

\[
\mathcal B_N=\prod_{i=1}^3W(s_i).
\]

Then

\[
\boxed{
\frac{N\mathcal B_N}{W(N)}
\longrightarrow
\kappa_{\boldsymbol\alpha}
:=\frac{2}{\pi\sqrt{\alpha_1\alpha_2\alpha_3}}.}
\tag{2.6}
\]

Thus every nonempty open subcone of \(C>A+B\) has positive box mass and
positive global-width mass for every fixed interior block split.

## 3. Exact mass of the two obstruction cones

### Theorem 3.1 (box-count masses)

For the Rayleigh order statistics \(A<B<C\),

\[
\boxed{
\Pr(C>A+B)=1-\frac{\pi}{3\sqrt3},}
\tag{3.1}
\]

\[
\boxed{
\Pr(C>2B)=\frac15.}
\tag{3.2}
\]

#### Proof of (3.1)

Fix the third variable as the largest.  Conditional on \(Y_1=x,Y_2=y\),

\[
\Pr(Y_3>x+y)=e^{-(x+y)^2/2}.
\]

Hence

\[
\begin{aligned}
\Pr(Y_3>Y_1+Y_2)
&=
\int_0^\infty\!\!\int_0^\infty
xy\,e^{-(x^2+y^2+xy)}\,dx\,dy.
\end{aligned}
\tag{3.3}
\]

Set \(x=\rho\cos\theta,\ y=\rho\sin\theta\).  Integrating first in
\(\rho\), and then putting \(t=\tan\theta\), transforms (3.3) into

\[
\frac12\int_0^\infty
\frac{t}{(t^2+t+1)^2}\,dt.
\tag{3.4}
\]

Completing the square in \(t^2+t+1\) gives

\[
\int_0^\infty\frac{dt}{(t^2+t+1)^2}
=\frac{4\pi}{9\sqrt3}-\frac13,
\]

and therefore

\[
\frac12\int_0^\infty
\frac{t}{(t^2+t+1)^2}\,dt
=\frac13-\frac{\pi}{9\sqrt3}.
\tag{3.5}
\]

Exactly one of the three variables can exceed the sum of the other two.
Multiplying (3.5) by three proves (3.1).

#### Proof of (3.2)

Put \(Z_i=Y_i^2/2\).  These variables are independent exponentials of
mean one.  One oriented event has probability

\[
\begin{aligned}
\Pr(Y_1<Y_2,\ Y_3>2Y_2)
&=
\int_0^\infty
(1-e^{-t})e^{-4t}e^{-t}\,dt\\
&=\frac15-\frac16=\frac1{30}.
\end{aligned}
\tag{3.6}
\]

There are three choices of the largest variable and two orders of the
remaining variables.  The resulting six events are disjoint up to null
ties, proving (3.2). \(\square\)

### Theorem 3.2 (global-width masses)

The limiting fractions of the global Boolean middle layer carried by the
two cones are precisely (0.2) and (0.3).

#### Proof for \(C>A+B\)

For a fixed choice of the largest variable, integration over it gives

\[
\begin{aligned}
\mathbb E\!\left[
AB\,\mathbf1_{\{C>A+B\}}\right]
&=
3\int_0^\infty\!\!\int_0^\infty
x^2y^2e^{-(x^2+y^2+xy)}\,dx\,dy\\
&=
3\int_0^\infty
\frac{t^2}{(t^2+t+1)^3}\,dt\\
&=\frac{2\pi}{3\sqrt3}-1.
\end{aligned}
\tag{3.7}
\]

The second equality follows from the same polar substitution as in
(3.3), and the last integral follows by completing the square.  Combining
(3.7) with (2.5) gives

\[
\Omega_{C>A+B}
=
\frac{2\sqrt3}{\pi}
\left(\frac{2\pi}{3\sqrt3}-1\right)
=\frac43-\frac{2\sqrt3}{\pi}.
\]

#### Proof for \(C>2B\)

For one orientation \(0<x<y,\ z>2y\), integrate first over \(z\):

\[
\begin{aligned}
J
&=
\int_{0<x<y}
x^2y^2e^{-(x^2+5y^2)/2}\,dx\,dy\\
&=
8\int_0^1\frac{u^2}{(u^2+5)^3}\,du\\
&=
\frac{\sqrt5}{25}\arctan\frac1{\sqrt5}
-\frac1{45}.
\end{aligned}
\tag{3.8}
\]

Here \(x=uy\) gives the second line, and

\[
\int_0^1\frac{u^2}{(u^2+5)^3}\,du
=
\frac{\sqrt5}{200}\arctan\frac1{\sqrt5}
-\frac1{360}.
\tag{3.9}
\]

Summing the six orientations,

\[
\mathbb E\!\left[
AB\,\mathbf1_{\{C>2B\}}\right]
=
\frac{6\sqrt5}{25}\arctan\frac1{\sqrt5}
-\frac2{15}.
\tag{3.10}
\]

Equations (2.5) and (3.10) give (0.3).  Positivity follows directly from
the positive integral in (3.8). \(\square\)

## 4. The local plateau obstruction

Let \(g_3(p,q,r)\) be the least length of a nonzero word in

\[
[0,p]\times[0,q]\times[0,r]
\]

whose contiguous coordinatewise maxima contain every nonzero box point.
For every nonzero box,

\[
g_3(p,q,r)\ge w_3(p,q,r).
\tag{4.1}
\]

Indeed, choose a maximum antichain of targets.  Witnesses for two
incomparable targets cannot have the same left endpoint: intervals with a
common left endpoint are nested, so their maxima are comparable.

The following endpoint-potential theorem is the local input needed for the
coefficient calculation.  A proof is included to keep the report
self-contained.

### Theorem 4.1 (flat-plateau endpoint bound)

Let

\[
1\le p\le q,\qquad r\ge p+q,
\qquad W=(p+1)(q+1).
\]

Then

\[
\boxed{
g_3(p,q,r)
\ge
W+
\left\lceil
\frac{W(r-p-q)}{2r}
\right\rceil.}
\tag{4.2}
\]

#### Proof

Put

\[
P=p+q,\qquad H=r-P.
\]

The ranks \(P,P+1,\ldots,r\) are full plateau layers, each containing one
point

\[
(x,y,t-x-y)
\]

for every \(0\le x\le p,\ 0\le y\le q\).  Thus each layer has \(W\)
targets, and there are exactly \(WH\) vertical covers between consecutive
plateau layers.

Fix one witnessing interval for every plateau target.  Group the targets
first by common physical left endpoint and then, independently, by common
physical right endpoint.  Each group is a chain: intervals with a common
endpoint are nested.  The two partitions are orthogonal, because a fixed
left endpoint and a fixed right endpoint determine one physical interval
and hence one target.

Consider either endpoint partition and write its number of chains as

\[
C=W+\delta.
\]

Every plateau layer meets \(W\) distinct chains.  Therefore the sets of
chains meeting two consecutive layers intersect in at least

\[
2W-C=W-\delta
\]

chains.  Across all \(H\) consecutive layer pairs, the partition contains
at least

\[
H(W-\delta)
\tag{4.3}
\]

grid covers.

Use the horizontal potential

\[
\phi(x,y,z)=x+y,\qquad0\le\phi\le P.
\]

The bottom and top plateau layers have the same \(\phi\)-multiset.  Exactly
\(W\) partition chains meet either boundary, while the other \(\delta\)
start and the other \(\delta\) end internally.  Telescoping \(\phi\) over
all partition chains shows that the total number of horizontal covers is
at most \(P\delta\).  Hence the number of vertical covers in this
partition is at least

\[
H(W-\delta)-P\delta
=HW-r\delta.
\tag{4.4}
\]

Let \(\delta_L,\delta_R\) be the two excesses.  Orthogonality forbids a
vertical cover from belonging to both endpoint partitions.  Since only
\(WH\) vertical covers exist, (4.4) gives

\[
2HW-r(\delta_L+\delta_R)\le WH,
\]

so

\[
\delta_L+\delta_R\ge\frac{WH}{r}.
\tag{4.5}
\]

If the physical word has length \(N\), it has at most \(N\) distinct left
endpoints and at most \(N\) distinct right endpoints.  Thus

\[
\delta_L,\delta_R\le N-W.
\]

Combining this with (4.5) yields

\[
N-W\ge\frac{WH}{2r}.
\]

Taking the integer ceiling proves (4.2). \(\square\)

For normalized sorted heights \(p/\sqrt s\to a\),
\(q/\sqrt s\to b\), \(r/\sqrt s\to c\), Theorem 4.1 gives the lower
profile

\[
\boxed{
\frac{g_3(p,q,r)-w_3(p,q,r)}s
\ \ge\
\frac{ab(c-a-b)}{2c}-o(1)
\qquad(c>a+b).}
\tag{4.6}
\]

## 5. The exact independent-concatenation ledger

A translated product box has a common Boolean base.  The relative local
origin represents that base.  If the base is nonempty, an independently
encoded box costs exactly

\[
g_3(p,q,r)+1
\tag{5.1}
\]

entries: append the base to an optimal translated nonzero word for the
upper bound.  Conversely, projecting a local word to relative coordinates
and deleting zero projections leaves a nonzero relative word of length at
least \(g_3\), while a witness for the base requires at least one zero
projection.  This proves (5.1).

There is exactly one product box with empty base, namely the product of
the three SCD chains containing the empty sets.  The global empty target
is not required, so this one box needs no origin anchor.

Put

\[
\mathcal B_s=W(s)^3.
\]

Let \(Z_s\) be the number of boxes whose three chain heights are all zero.
Then

\[
Z_s=
\begin{cases}
\displaystyle
\mathcal B_s\left(\frac2{s+2}\right)^3,&s\ \text{even},\\[2mm]
0,&s\ \text{odd}.
\end{cases}
\tag{5.2}
\]

Indeed, when \(s\) is even,

\[
c_s(0)
=W(s)-\binom{s}{s/2-1}
=\frac2{s+2}W(s).
\]

Define

\[
\Delta(p,q,r)=
\begin{cases}
g_3(p,q,r)-w_3(p,q,r),&p+q+r>0,\\
0,&p=q=r=0.
\end{cases}
\tag{5.3}
\]

For independent uniform SCD heights \(H_1,H_2,H_3\), the separate
concatenation has the exact finite ledger

\[
\boxed{
L_{\rm sep}(3s)-W(3s)
=
\mathcal B_s\,\mathbb E\Delta(H_1,H_2,H_3)
+\mathcal B_s-1-Z_s.}
\tag{5.4}
\]

To see this, start from

\[
L_{\rm sep}(3s)
=
\sum_{\text{boxes}}g_3(p,q,r)+\mathcal B_s-1
\]

and subtract the exact width identity (2.1).  An all-zero-height box has
\(g_3=0,w_3=1\), which accounts for the term \(-Z_s\).

Since

\[
\frac{\mathcal B_s}{W(3s)}
\sim\frac{2\sqrt3}{\pi s},
\tag{5.5}
\]

the anchor and zero-height corrections in (5.4) are \(o(W(3s))\).  Thus

\[
\boxed{
\frac{L_{\rm sep}(3s)-W(3s)}{W(3s)}
=
\frac{s\mathcal B_s}{W(3s)}
\mathbb E\!\left[\frac{\Delta(H_1,H_2,H_3)}s\right]
+o(1).}
\tag{5.6}
\]

Equation (5.6) is the exact asymptotic coefficient reduction.  If the
normalized local excess converges in \(L^1\) to a profile \(d(A,B,C)\),
then the true coefficient loss is exactly

\[
\boxed{
\frac{2\sqrt3}{\pi}\,\mathbb E d(A,B,C).}
\tag{5.7}
\]

No such sharp local profile is currently proved.  Therefore (5.7) must
not be replaced by a claimed numerical equality.  What can be determined
unconditionally is a strictly positive exact lower coefficient.

## 6. Explicit coefficient no-go

On the subcone \(c>2b\), the endpoint profile admits an elementary
minorant.  For \(0<a\le b\) and \(c\ge2b\),

\[
\begin{aligned}
\frac{c-a-b}{2c}-\frac{b-a}{4b}
&=
\frac{(a+b)(c-2b)}{4bc}\ge0.
\end{aligned}
\tag{6.1}
\]

Hence, for every sorted discrete height triple \(p\le q\le r\),
Theorem 4.1 gives the exact finite minorant

\[
\frac{\Delta(p,q,r)}s
\ge
\mathbf1_{\{p\ge1,\ r>2q\}}
\frac{(p+1)(q+1)}s\,\frac{q-p}{4q}.
\tag{6.2}
\]

The right side of (6.2) is defined to be zero off
\(\{p\ge1,\ r>2q\}\); on that event \(q\ge1\), so the displayed quotient
is defined.

The right side converges in expectation to

\[
\frac{A(B-A)}4\,\mathbf1_{\{C>2B\}}.
\tag{6.2a}
\]

Indeed, \(\Pr(p=0)\to0\), the cone wall has limiting probability zero,
and (1.7) supplies the required polynomial uniform integrability.

The ordered Rayleigh triple has joint density

\[
6abc\,e^{-(a^2+b^2+c^2)/2}
\qquad(0<a<b<c).
\tag{6.3}
\]

Integrating \(c\) on \(c>2b\), then putting \(a=ub\), gives

\[
\begin{aligned}
\mathbb E\!\left[
\frac{A(B-A)}4\mathbf1_{\{C>2B\}}\right]
&=
12\int_0^1
\frac{u^2(1-u)}{(u^2+5)^3}\,du\\
&=
\frac{3}{10\sqrt5}\arctan\frac1{\sqrt5}
-\frac1{20}.
\end{aligned}
\tag{6.4}
\]

For the last equality,

\[
\int_0^1\frac{u^2}{(u^2+5)^3}\,du
=
\frac{\sqrt5}{200}\arctan\frac1{\sqrt5}
-\frac1{360},
\tag{6.5}
\]

\[
\int_0^1\frac{u^3}{(u^2+5)^3}\,du
=\frac1{720}.
\tag{6.6}
\]

The integral in (6.4) is strictly positive, so its closed form is positive
without any numerical approximation.

Apply (6.2)--(6.2a), (5.6), and (2.3).  This proves

\[
\begin{aligned}
\liminf_{s\to\infty}
\frac{L_{\rm sep}(3s)-W(3s)}{W(3s)}
&\ge
\frac{2\sqrt3}{\pi}
\left(
\frac{3}{10\sqrt5}\arctan\frac1{\sqrt5}
-\frac1{20}
\right)\\
&=
\frac{3\sqrt3}{5\pi\sqrt5}\arctan\frac1{\sqrt5}
-\frac{\sqrt3}{10\pi}\\
&=\delta_0>0.
\end{aligned}
\tag{6.7}
\]

This proves (0.4)--(0.5).

The full plateau cone gives the stronger exact certified functional

\[
\boxed{
\Delta_{\rm EP}
=
\frac{\sqrt3}{\pi}
\mathbb E\!\left[
AB\,\frac{C-A-B}{C}
\mathbf1_{\{C>A+B\}}
\right]
>\delta_0.}
\tag{6.8}
\]

It is left as an exact positive integral because evaluating it is not
needed for the no-go.  Again, \(\Delta_{\rm EP}\) is a certified lower
coefficient, not a proved equality for the true optimum.

### Theorem 6.1 (every fixed interior split fails)

Let

\[
s_1+s_2+s_3=N,\qquad
\frac{s_i}{N}\longrightarrow\alpha_i>0.
\]

Use arbitrary SCDs in the three blocks and concatenate optimal box words
independently.  Let \(X_i\) be independent with density (1.8), and sort
them as \(A\le B\le C\).  Then

\[
\boxed{
\liminf_{N\to\infty}
\frac{L_{\rm sep}(N)-W(N)}{W(N)}
\ge
\delta_{\rm EP}(\boldsymbol\alpha)>0,}
\tag{6.9}
\]

where

\[
\boxed{
\delta_{\rm EP}(\boldsymbol\alpha)
=
\frac1{\pi\sqrt{\alpha_1\alpha_2\alpha_3}}
\mathbb E\!\left[
AB\,\frac{C-A-B}{C}
\mathbf1_{\{C>A+B\}}
\right].}
\tag{6.10}
\]

#### Proof

Sort each discrete height triple as \(p\le q\le r\).  Theorem 4.1 and
the trivial nonnegative excess outside the plateau give the normalized
minorant

\[
\frac{\Delta(p,q,r)}N
\ge
\mathbf1_{\{p\ge1\}}
\frac{(p+1)(q+1)}N
\frac{(r-p-q)_+}{2r},
\tag{6.11}
\]

with the right side defined as zero at \(r=0\).  It converges to

\[
AB\,\frac{(C-A-B)_+}{2C}.
\]

Indeed, the event \(p=0\) has probability tending to zero, while the
limiting minimum \(A\) is positive almost surely.  The minorant is bounded
by a quadratic polynomial in the normalized heights, so (1.7) gives
convergence of its expectation.  Multiply by the box normalization (2.6).
This gives (6.9)--(6.10).

The densities in (1.8) are strictly positive on the positive octant.
The integrand in (6.10) is strictly positive on every compact set inside
\(C>A+B\), so \(\delta_{\rm EP}(\boldsymbol\alpha)>0\). \(\square\)

Thus no choice of SCD and no fixed positive-proportion three-way split
rescues independent concatenation.

### Theorem 6.2 (no degenerating-split rescue)

Let

\[
0\le s_1(N)\le s_2(N)\le s_3(N),\qquad
s_1+s_2+s_3=N,
\]

be an arbitrary sequence of three-way dimension splits.  For arbitrary
SCDs in the blocks, let \(L_{\rm sep}(N)\) be the independently
concatenated optimal-box length.  Then

\[
\boxed{
\liminf_{N\to\infty}
\frac{L_{\rm sep}(N)-W(N)}{W(N)}>0.}
\tag{6.12}
\]

The positive lower bound may depend on the dimension sequence.

#### Proof

We use the absolute central-binomial comparison

\[
W(t)\asymp\frac{2^t}{\sqrt{t+1}},
\]

which gives

\[
\frac{W(s_1)W(s_2)W(s_3)}{W(N)}
\asymp
\frac{\sqrt{N+1}}
{\sqrt{(s_1+1)(s_2+1)(s_3+1)}}.
\tag{6.13}
\]

The unequal-block analogue of (5.4) has the same correction
\(\mathcal B_N-1-Z_N\ge0\), where \(Z_N\) counts all-zero-height product
boxes.  Consequently
\(L_{\rm sep}(N)-W(N)\) is at least the sum of the nonnegative local
excesses over any selected family of nonzero boxes.

Suppose (6.12) were false.  On some subsequence the normalized excess
would tend to zero.  Pass to further subsequences as needed.

**Case 1: \(s_1\to\infty\).**  Select chains in the fixed Rayleigh windows

\[
\sqrt{s_1}\le p\le2\sqrt{s_1},\qquad
4\sqrt{s_2}\le q\le5\sqrt{s_2},\qquad
12\sqrt{s_3}\le r\le13\sqrt{s_3},
\tag{6.14}
\]

with harmless parity rounding.  Lemma 1.2 gives a positive absolute lower
bound on the fraction of chain triples in these windows.  They satisfy

\[
p\le\frac q2,\qquad r>2q.
\]

The exact minorant (6.2) therefore gives

\[
\Delta(p,q,r)\ge c\sqrt{s_1s_2}
\tag{6.15}
\]

for an absolute \(c>0\).  Multiplying (6.13) by (6.15) gives

\[
\sqrt{s_1s_2}\,
\frac{W(s_1)W(s_2)W(s_3)}{W(N)}
\asymp
\sqrt{\frac{N+1}{s_3+1}}
=\Omega(1),
\tag{6.16}
\]

contradicting normalized excess tending to zero.

**Case 2: \(s_1=d\ge1\) is fixed and \(s_2\to\infty\).**  Select the
unique longest chain in the first block, so \(p=d\), and use the windows

\[
\sqrt{s_2}\le q\le2\sqrt{s_2},\qquad
5\sqrt{s_3}\le r\le6\sqrt{s_3}.
\tag{6.17}
\]

The selected fraction is positive with a constant depending only on \(d\).
For large \(N\), \(p\le q/2\) and \(r>2q\), so (6.2) gives

\[
\Delta(d,q,r)\ge c_d\sqrt{s_2}.
\tag{6.18}
\]

Equation (6.13) now yields

\[
\sqrt{s_2}\,
\frac{W(d)W(s_2)W(s_3)}{W(N)}
\asymp_d
\sqrt{\frac{N+1}{s_3+1}}
=\Omega_d(1),
\tag{6.19}
\]

again a contradiction.

**Case 3: \(s_1=0\) and \(s_2\to\infty\).**  The local boxes are
two-dimensional.  For \(q,r>0\),

\[
g_2(q,r)\ge q+r.
\tag{6.20}
\]

Indeed, every pure-axis target \((i,0)\), \(1\le i\le q\), forces an
occurrence with value \((i,0)\), and every \((0,j)\), \(1\le j\le r\),
forces a distinct occurrence with value \((0,j)\).  In the positive
Rayleigh windows

\[
\sqrt{s_2}\le q\le2\sqrt{s_2},\qquad
5\sqrt{s_3}\le r\le6\sqrt{s_3},
\]

the width is \(q+1\), and therefore the excess is at least \(r-1\).
Equation (6.13) gives

\[
\sqrt{s_3}\,
\frac{W(s_2)W(s_3)}{W(N)}
\asymp
\sqrt{\frac{N+1}{s_2+1}}
=\Omega(1).
\tag{6.21}
\]

**Case 4: \(s_2\) is bounded.**  Pass to a further subsequence on which

\[
s_1=d,\qquad s_2=e
\]

are fixed.  If \(d\ge1\), select the two longest fixed-block chains and a
positive Rayleigh window for the third height.  For large \(r\),
Theorem 4.1 gives

\[
\Delta(d,e,r)
\ge
\frac{(d+1)(e+1)}4>0.
\tag{6.22}
\]

If \(d=0<e\), (6.20) gives excess at least \(r-1\).  If \(d=e=0\), every
one-dimensional word needs at least one occurrence of each value
\(1,\ldots,r\), so \(g_1(r)\ge r\).  In all three subcases the selected
fraction of boxes is positive, and

\[
\frac{W(d)W(e)W(s_3)}{W(N)}
\asymp_{d,e}1.
\tag{6.23}
\]

Thus the aggregate normalized excess is bounded away from zero.

Every subsequence has one of the preceding further subsequences, yielding
the desired contradiction. \(\square\)

Theorem 6.2 is qualitative: unlike the balanced calculation, it does not
claim one universal closed coefficient for all moving splits.  It shows
that driving a block proportion to zero cannot rescue the separately paid
architecture.

## 7. Exact repair scale and the smallest surviving lemma

Let \(\mathscr D_s\) be the boxes whose normalized sorted heights lie in
\(C>2B\).  Theorem 3.1 gives

\[
|\mathscr D_s|
=\left(\frac15+o(1)\right)\mathcal B_s.
\tag{7.1}
\]

The conditional mean of the certified local excess profile on this cone is

\[
\begin{aligned}
\gamma_0
&=
\mathbb E\!\left[
\frac{A(B-A)}4\,\middle|\,C>2B
\right]\\
&=
\frac{3}{2\sqrt5}\arctan\frac1{\sqrt5}
-\frac14
>0.
\end{aligned}
\tag{7.2}
\]

Therefore the selected boxes alone carry certified isolated excess at
least

\[
(\delta_0+o(1))W(3s),
\tag{7.3}
\]

or equivalently certified average excess at least

\[
(\gamma_0+o(1))s
\tag{7.4}
\]

per obstructed box.

### Theorem 7.1 (sublinear-per-box repair no-go)

Suppose an architecture begins with independently encoded three-chain
boxes and replaces or fuses their local words, but its total saving from
the independent sum is \(o(s\mathcal B_s)\).  Then

\[
\liminf_{s\to\infty}
\frac{L(3s)}{W(3s)}
\ge1+\delta_0.
\tag{7.5}
\]

In particular, a repair saving only \(o(s)\) per product box, uniformly or
on average, cannot reach coefficient one.

#### Proof

By (2.3),

\[
s\mathcal B_s
=\left(\frac{2\sqrt3}{\pi}+o(1)\right)W(3s).
\]

A saving \(o(s\mathcal B_s)\) is therefore \(o(W(3s))\).  Subtracting it
from the lower bound (0.4) leaves (7.5). \(\square\)

Consequently a coefficient-one rescue must save

\[
\boxed{\Omega(W(3s))}
\tag{7.6}
\]

relative to isolated box costs.  Since
\(|\mathscr D_s|=\Theta(\mathcal B_s)\), dividing this necessary aggregate
saving by the number of obstructed boxes gives the normalization
\(\Omega(s)\).  This is a scale statement; a genuinely global construction
need not admit a canonical allocation of its saving to individual boxes.
Adding short seams to unchanged local words cannot supply the aggregate
saving.  The local words themselves must be replaced by words whose
witnesses cross box boundaries.

The scale-minimal clean replacement is the following.

> **Unproved bounded-packet fusion lemma (BPF).**  
> There is a fixed \(K\ge2\) and, for every \(s\), a partition of the
> three-chain product boxes into packets of at most \(K\) boxes such that
> each packet has one literal Boolean word covering the union of its boxes,
> and
> \[
> \sum_{\text{packets }P}|{\mathcal W}_P|
> \le
> \sum_{\text{boxes }B}w_3(B)+o(s\mathcal B_s).
> \tag{7.7}
> \]

Because of (2.1) and (2.3), BPF would give

\[
W(3s)+o(W(3s))
\]

after an \(O(\mathcal B_s)=o(W(3s))\) packet-anchor correction.  Pair
fusion (\(K=2\)) is the smallest-cardinality version.

BPF is not contradicted by Theorem 4.1: that theorem applies to a word
confined to one box, while a packet word may use intervals and letters
from both boxes.  On the other hand, (7.3)--(7.4) show exactly what BPF
must accomplish in aggregate: the obstruction charges a positive-density
family at mean scale \(s\), and BPF must recover
\(\Omega(s\mathcal B_s)\) overall.  No particular packetwise allocation of
that recovery is asserted.

One may instead retain four or more chain factors and solve the fused
higher-dimensional local problem.  That also breaks the three-box
additive ledger and is not ruled out here.

## 8. Adversarial audit and exact scope

1. **Uniform chains, not uniform vertices.**  The Rayleigh law is the law
   of a uniformly selected SCD chain.  A vertex-biased height law would be
   different and is not used.
2. **SCD invariance.**  Formula (1.1) fixes the height multiset of every
   SCD, so changing or randomizing the decompositions cannot change any
   cone mass above.
3. **Parity.**  Heights occupy a parity-two mesh.  All limiting cone walls
   have Rayleigh measure zero, and the exact tail formula (1.2) controls the
   mesh without selecting forbidden heights.
4. **Box mass versus width mass.**  Equations (3.1)--(3.2) count boxes;
   (0.2)--(0.3) are separately weighted by local middle width.  The two
   notions are not conflated.
5. **Anchor correction.**  Equation (5.4) includes every translated local
   origin and every all-zero-height box.  These terms are lower order but
   are not silently discarded.
6. **Coefficient language.**  Equation (5.6) is the exact ledger.
   Equation (0.5) is an exact closed-form lower coefficient.  The exact
   true optimal coefficient is unknown because no matching local upper
   profile for \(g_3-w_3\) is proved.
7. **Cone boundary.**  The no-go uses the strict subcone \(C>2B\); no
   uniform positive gap is claimed on its wall.  The integral itself
   supplies the positive aggregate coefficient.
8. **Scope of the no-go.**  Theorem 7.1 rules out independent concatenation
   and sublinear-per-box repairs.  It does not rule out bounded-packet
   fusion, high-degree global sharing, or a genuinely fused four-box word.
9. **Status of the conjecture.**  The contiguous-OR width conjecture is
   neither proved nor disproved here.  The independently concatenated
   three-block SCD route is rigorously exhausted; BPF or a fused
   higher-dimensional theorem is the smallest replacement.
