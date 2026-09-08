# Third-wave S: sharp optimization of the three-box endpoint-potential dual

Date: 2026-07-24

## 0. Main theorem and scope of sharpness

Let

\[
1\le p\le q,\qquad P=p+q,\qquad r\ge P,\qquad
W=(p+1)(q+1).
\]

Here \(g_3(p,q,r)\) is the least length of a word whose nonempty
contiguous-factor coordinatewise maxima contain every nonzero box point.
Projection to \((x,y)\) bounds every antichain by \(W\), while rank \(P\)
contains one point over every \((x,y)\); hence \(W\) is the exact width.

For a universal three-box range-maximum word of length \(W+D\), the
endpoint-potential argument may be applied to any consecutive rank band
obtained by attaching independent lower and upper shoulders to the full
width plateau \(P,\ldots,r\).  This report optimizes that entire family.

The finite answer is exact: asymmetric shoulders, shoulders deeper than
the shorter side, and odd total shoulder depth give no improvement over
some symmetric band.  On fixed rays, put

\[
s=a+b,\qquad c\ge s,
\]

and define \(x_*=x_*(a,b,c)\) as the unique root in

\[
0<x_*<\frac{ab}{2(a+b)}
\]

of

\[
\boxed{
4x^3+3(c-4s)x^2-12csx+6ab\,s=0.}                          \tag{0.1}
\]

Then the sharp coefficient supplied by all consecutive plateau-attached
sloped-rank bands in the endpoint-potential dual is

\[
\boxed{
\mathcal E_{\rm EP}(a,b,c)
=\frac{ab}{2}-(a+b)x_*+\frac{x_*^2}{4}.}                   \tag{0.2}
\]

Consequently, for every fixed integral ray \(0<a\le b\), \(c\ge a+b\),

\[
\boxed{
\liminf_{t\to\infty}
\frac{
g_3(at,bt,ct)-(at+1)(bt+1)
}{t^2}
\ge \mathcal E_{\rm EP}(a,b,c)>0.}                          \tag{0.3}
\]

At the exact width boundary \(c=s=a+b\), let

\[
\rho=\frac{ab}{(a+b)^2}
\]

and let \(y_\rho\) be the unique root in
\((0,\rho/2)\) of

\[
4y^3-9y^2-12y+6\rho=0.                                    \tag{0.4}
\]

Then

\[
\boxed{
\mathcal E_{\rm EP}(a,b,a+b)
=(a+b)^2y_\rho^2\left(1-\frac{y_\rho}{3}\right).}           \tag{0.5}
\]

The required root has the explicit real branch

\[
\boxed{
y_\rho=
\frac34+\frac52
\cos\!\left(
\frac13\arccos\!\frac{99-48\rho}{125}
-\frac{2\pi}{3}
\right).}                                                  \tag{0.6}
\]

Thus the optimized boundary obstruction is exact within this dual family.
For a simple radical-free certificate,

\[
\boxed{
\mathcal E_{\rm EP}(a,b,a+b)
\ge
\frac{49a^2b^2}{240(a+b)^2}.}                              \tag{0.7}
\]

Here “sharp” means sharp among all plateau-attached consecutive rank-band
certificates using the two endpoint partitions, their orthogonality, the
potential \(\phi=x+y\), and vertical-edge capacity.  It is not asserted to be the
true asymptotic excess of \(g_3\), nor to dominate certificates from a
different potential, a non-rank target region, or the independent
ordered-witness corridor theorem.

No web search, finite search, or computational search was used.  The
finite asymmetric calculation and the one-variable optimization were
independently reconstructed and adversarially audited.

## 1. Endpoint partitions recalled

Choose one nonempty witnessing interval

\[
I_T=[\ell_T,r_T]
\]

for every target \(T\) in a selected rank band.  Group the targets first
by common left endpoint and then by common right endpoint.  Each group is
a poset chain: increasing an interval at one fixed endpoint can only
increase its coordinatewise maximum.

The resulting left and right chain partitions are orthogonal.  If one
left chain and one right chain shared two targets, the two targets would
have the same selected left and right endpoints, hence the same physical
witness interval and the same maximum.  They would therefore be one
target.

Each endpoint partition has at most the word length \(W+D\) chains.  A
vertical \(z\)-cover edge cannot occur in both partitions, since its two
endpoint targets would then be two common targets of one left chain and
one right chain.

These are the only word-specific facts used below.

## 2. The exact asymmetric-band theorem

For \(0\le j\le P\), define the rank profile of the
\((p+1)\)-by-\((q+1)\) rectangle by

\[
f_j
=\#\{(x,y):0\le x\le p,\ 0\le y\le q,\ x+y=j\}.             \tag{2.1}
\]

For \(0\le k\le P\), put

\[
F_k=\sum_{j<k}f_j,\qquad
L_k=\sum_{j<k}j f_j,\qquad
G_k=\sum_{i=1}^{k}F_i,                                     \tag{2.2}
\]

and

\[
\boxed{
\mathcal R_k
=-3G_k+2(1-P)F_k+2L_k.}                                   \tag{2.3}
\]

The value at \(k=0\) is zero.

### Theorem 2.1 — exact independent-shoulder certificate

Let

\[
0\le u\le P-1,\qquad 0\le v\le P,
\]

and use every nonzero target in the rank band

\[
P-u,\ P-u+1,\ldots,r+v.                                   \tag{2.4}
\]

Then every universal word of length \(W+D\) satisfies

\[
\boxed{
D\ge
\max\!\left\{
0,
\left\lceil
\frac{
(r-P+u+v)W+\mathcal R_u+\mathcal R_v
}{
2(r+u+v)
}
\right\rceil
\right\}.}                                                 \tag{2.5}
\]

The restriction \(u\le P-1\) merely keeps the unrequired zero target out
of the bottom layer.  The optimization below proves that every positive
maximizer already has \(u,v\le p\), so this endpoint convention loses
nothing.

#### Proof

Write

\[
H=r-P,\qquad J=H+u+v.
\]

At bottom rank \(P-u\), the omitted \((x,y)\)-columns correspond under
\((x,y)\mapsto(p-x,q-y)\) to pairs of sum below \(u\).  At top rank
\(r+v\), the omitted columns are the pairs of sum below \(v\).  Therefore
the two boundary sizes are

\[
M_-=W-F_u,\qquad M_+=W-F_v.                                \tag{2.6}
\]

The lower shoulder loses \(F_i\) targets at depth \(i\), and the upper
shoulder has the same profile.  Hence the total number of selected targets
is

\[
T=(J+1)W-G_u-G_v.                                          \tag{2.7}
\]

Every vertical column meets the band in one nonempty interval.  Its number
of vertical edges is one less than its number of vertices, so the exact
vertical-edge capacity is

\[
A_{\rm vert}=T-W=JW-G_u-G_v.                               \tag{2.8}
\]

Use the transverse potential

\[
\phi(x,y,z)=x+y,\qquad 0\le\phi\le P.
\]

The bottom boundary omits \(F_u\) columns whose total \(\phi\)-mass is
\(PF_u-L_u\).  The top boundary omits \(F_v\) columns whose total
\(\phi\)-mass is \(L_v\).  Since the full rectangular \(\phi\)-mass
cancels, the top-minus-bottom boundary mass is

\[
\Delta_\phi=PF_u-L_u-L_v.                                  \tag{2.9}
\]

Consider either endpoint partition and let it have \(C\) chains.  If
successive band layers have sizes \(m_i,m_{i+1}\), the sets of chains
meeting them intersect in at least \(m_i+m_{i+1}-C\).  Every chain in the
intersection supplies a genuine rank-one cover.  Summing gives at least

\[
2T-M_--M_+-JC                                              \tag{2.10}
\]

cover edges.  This remains valid if some individual lower bound is
negative or some chains skip ranks.

Exactly \(M_-\) chains begin on the bottom boundary, and exactly \(M_+\)
end on the top boundary.  The remaining \(C-M_+\) chain ends have
\(\phi\le P\), while all internal starts have nonnegative \(\phi\).
Telescoping \(\phi\) therefore bounds the horizontal covers in (2.10) by

\[
\Delta_\phi+P(C-M_+).                                      \tag{2.11}
\]

Subtracting (2.11) from (2.10), the partition uses at least

\[
(2J+P)W
-2(G_u+G_v)
+(1-P)(F_u+F_v)
+L_u+L_v
-(J+P)C                                                    \tag{2.12}
\]

vertical edges.

Apply (2.12) to the left and right endpoint partitions.  Their vertical
edge sets are disjoint, their chain counts satisfy

\[
C_L+C_R\le2(W+D),
\]

and the coefficient of this sum in (2.12) is negative.  Comparing their
combined lower bound with (2.8), substituting the upper bound on
\(C_L+C_R\), and simplifying gives

\[
2(J+P)D
\ge JW+\mathcal R_u+\mathcal R_v.                           \tag{2.13}
\]

Since \(J+P=r+u+v\), taking the integer ceiling and positive part proves
(2.5). \(\square\)

### Triangular-shoulder specialization

For \(0\le k\le p\), the deficit corner is triangular:

\[
F_k=\frac{k(k+1)}2,\qquad
L_k=\frac{k(k-1)(k+1)}3,\qquad
G_k=\frac{k(k+1)(k+2)}6.
\]

Thus

\[
\boxed{
\mathcal R_k
=\frac{k(k+1)(k-6P-4)}6.}                                 \tag{2.14}
\]

Putting \(u=v=k\) in (2.5) recovers the audited symmetric-band inequality

\[
2(r+2k)D
\ge
(r-P+2k)W+\frac{k(k+1)(k-6P-4)}3.                          \tag{2.15}
\]

## 3. Exact finite optimization over all shoulder depths

Define the unrounded raw certificate

\[
Q(u,v)
=
\frac{
(r-P+u+v)W+\mathcal R_u+\mathcal R_v
}{
2(r+u+v)
}.                                                         \tag{3.1}
\]

This section proves

\[
\boxed{
\max_{u,v}\max\{0,\lceil Q(u,v)\rceil\}
=
\max_{0\le k\le p}\max\{0,\lceil Q(k,k)\rceil\}.}           \tag{3.2}
\]

Thus asymmetry gives no improvement even before passage to a ray limit.

### 3.1 A positive maximizer never goes deeper than \(p\)

From (2.2)--(2.3),

\[
\mathcal R_{k+1}-\mathcal R_k
=-3F_k+(2k-2P-1)f_k.                                      \tag{3.3}
\]

Increasing one shoulder from \(k\) to \(k+1\) changes the numerator of
(3.1) by

\[
W+\mathcal R_{k+1}-\mathcal R_k.                            \tag{3.4}
\]

The rectangle rank profile gives the exact values

\[
W+\mathcal R_{k+1}-\mathcal R_k
=-(p+1)\left(k+\frac p2+q\right)<0
\quad(p\le k\le q),                                        \tag{3.5}
\]

and, writing \(d=P-k\),

\[
W+\mathcal R_{k+1}-\mathcal R_k
=-2W+\frac{(d+1)(4-d)}2<0
\quad(q\le k<P).                                           \tag{3.6}
\]

Once a shoulder reaches \(p\), every further increment strictly decreases
the numerator and increases the denominator.  A positive value of
\(Q\) therefore strictly decreases.  A nonpositive value cannot beat the
symmetric nonnegative certificate \(Q(0,0)=HW/(2r)\).  Hence every
positive maximizer
satisfies

\[
u,v\le p.                                                   \tag{3.7}
\]

### 3.2 Fixed total depth is balanced

On \(0\le k\le p\), equation (2.14) is a cubic.  For fixed

\[
S=u+v\le2p,
\]

direct expansion gives

\[
\mathcal R_u+\mathcal R_v
=C_P(S)+\frac{S-4P-2}{8}(u-v)^2,                            \tag{3.8}
\]

where \(C_P(S)\) is independent of \(u-v\).  Since

\[
S\le2p\le P<4P+2,
\]

the imbalance coefficient is strictly negative.  For every fixed total
depth, (3.1) is therefore maximized by shoulders as equal as parity
permits.

For even \(S=2k\), this gives \(u=v=k\).  For odd \(S=2k+1\), the balanced
choice is \((k,k+1)\).  Put

\[
d_k=2(r+2k).
\]

Its raw value is the denominator-weighted average

\[
Q(k,k+1)
=
\frac{
d_kQ(k,k)+d_{k+1}Q(k+1,k+1)
}{
d_k+d_{k+1}
}.                                                         \tag{3.9}
\]

It lies between the two adjacent symmetric values.  Applying a ceiling
cannot put it above both ceilings.  Equations (3.7)--(3.9) prove (3.2).

### 3.3 Omitting plateau layers cannot help

A lower-shoulder band which stops after only \(L\le H\) full plateau
transitions has raw certificate

\[
Q_L(u)
=\frac{(L+u)W+\mathcal R_u}{2(P+L+u)}.                      \tag{3.10}
\]

As a function of \(L\), it is strictly increasing, because

\[
\frac{\partial Q_L(u)}{\partial L}
=
\frac{PW-\mathcal R_u}{2(P+L+u)^2}>0.                       \tag{3.11}
\]

Here \(\mathcal R_u\le0\), which follows directly from (2.3):
\(L_u\le(u-1)F_u\le(P-1)F_u\) and \(G_u\ge0\).
The upper-shoulder calculation is identical.  A consecutive band reaching
both shoulders necessarily contains the entire plateau.  Therefore the
strongest consecutive rank-band certificate that reaches a plateau layer
uses all available plateau layers, exactly as in Theorem 2.1.

This completes the exact finite optimization of the plateau-attached
rank-band family.

## 4. The general fixed-ray functional

Let

\[
p=at,\qquad q=bt,\qquad r=ct,\qquad
0<a\le b,\qquad c\ge s=a+b,
\]

and let shoulder depths satisfy

\[
\frac{u}{t}\to x,\qquad \frac{v}{t}\to y,
\qquad 0\le x,y\le s.
\]

To retain the full, possibly nontriangular shoulder profile, define

\[
\mathsf A(x)
=\operatorname{area}
\{(X,Y)\in[0,a]\times[0,b]:X+Y<x\},                         \tag{4.1}
\]

\[
\mathsf B(x)
=\int_{\substack{0\le X\le a,\ 0\le Y\le b\\X+Y<x}}
(X+Y)\,dX\,dY,                                             \tag{4.2}
\]

and

\[
\boxed{
\varrho(x)
=5\mathsf B(x)-(3x+2s)\mathsf A(x).}                       \tag{4.3}
\]

Indeed,

\[
\frac{F_u}{t^2}\to\mathsf A(x),\qquad
\frac{L_u}{t^3}\to\mathsf B(x),
\]

while the exact identity

\[
G_u=\sum_{j<u}(u-j)f_j
\]

gives

\[
\frac{G_u}{t^3}
\to x\mathsf A(x)-\mathsf B(x).
\]

Consequently,

\[
\frac{\mathcal R_u}{t^3}\to\varrho(x).
\]

Dividing (2.13) by \(t^3\) yields the full two-shoulder functional

\[
\boxed{
\Gamma_{\rm gen}(x,y)
=
\frac{
ab(c-s+x+y)+\varrho(x)+\varrho(y)
}{
2(c+x+y)
}.}                                                        \tag{4.4}
\]

This is the asymptotic certificate before any restriction to triangular
shoulders or symmetric depths.

### 4.1 Explicit shoulder profile

The density of \(X+Y\) on the rectangle is

\[
\mathsf A'(x)
=
\begin{cases}
x,&0\le x\le a,\\
a,&a\le x\le b,\\
s-x,&b\le x\le s.
\end{cases}
\]

Substitution in (4.3) gives

\[
\varrho(x)
=
\begin{cases}
\dfrac{x^3}{6}-sx^2,
&0\le x\le a,\\[2mm]
-\dfrac a2x^2
-\left(\dfrac{a^2}{2}+2ab\right)x
+a^2s-\dfrac{5a^3}{6},
&a\le x\le b,\\[2mm]
-\dfrac52abs+3ab(s-x)+\dfrac{(s-x)^3}{6},
&b\le x\le s.
\end{cases}                                                \tag{4.5}
\]

The pieces and their first derivatives agree at \(a\) and \(b\).

### 4.2 Deep shoulders cannot maximize

Write

\[
g(x)=ab\,x+\varrho(x).
\]

Differentiating (4.3) gives

\[
\varrho'(x)
=-3\mathsf A(x)-2(s-x)\mathsf A'(x).                       \tag{4.6}
\]

For \(x\ge a\), the explicit signs are

\[
g'(x)
=-ax-\frac{a^2}{2}-ab<0
\quad(a\le x\le b),                                        \tag{4.7}
\]

and

\[
g'(x)
=-2ab-\frac{(s-x)^2}{2}<0
\quad(b\le x\le s).                                        \tag{4.8}
\]

The numerator in (4.4) is

\[
ab(c-s)+g(x)+g(y).
\]

If it is positive and \(x>a\), replacing \(x\) by \(a\) strictly increases
the numerator and decreases the denominator.  If it is nonpositive, it
cannot maximize the positive part of the certificate: for \(c>s\),
\((x,y)=(0,0)\) is already positive, while for \(c=s\), sufficiently small
equal positive shoulders give a positive numerator.  Therefore every
maximizer satisfies

\[
0\le x,y\le a.                                              \tag{4.9}
\]

### 4.3 Asymmetry cannot maximize

On the range (4.9), put

\[
q(z)=-sz^2+\frac{z^3}{6}.
\]

Then \(\varrho(z)=q(z)\) and

\[
q''(z)=-2s+z<0.
\]

For fixed \(x+y\), the denominator and the \(ab\)-term in (4.4) are fixed,
while strict concavity gives

\[
q(x)+q(y)
\le2q\!\left(\frac{x+y}{2}\right),
\]

with equality only at \(x=y\).  Equivalently, the exact imbalance term is

\[
q(x)+q(y)-2q\!\left(\frac{x+y}{2}\right)
=\frac{x+y-4s}{8}(x-y)^2<0                                 \tag{4.10}
\]

when \(x\ne y\).

The passage from finite depths to the continuous maximum loses nothing.
By Section 3 every exact maximizer has \(0\le u,v\le p\), so normalized
maximizing depths have convergent subsequences in the compact square
\([0,a]^2\).  Formula (2.14), divided by \(t^3\), converges uniformly on
that square to (4.4).  Conversely every \(x,y\) in the square is realized
to \(o(1)\) by \(u=\lfloor xt\rfloor\), \(v=\lfloor yt\rfloor\).

Thus the sharp asymptotic band functional is one-dimensional:

\[
\boxed{
\sup_{x,y}\Gamma_{\rm gen}(x,y)
=
\max_{0\le x\le a}
\Gamma_{a,b,c}(x),}                                        \tag{4.11}
\]

where

\[
\boxed{
\Gamma_{a,b,c}(x)
=
\frac{
ab(c-s+2x)-2sx^2+x^3/3
}{
2(c+2x)
}.}                                                        \tag{4.12}
\]

## 5. Exact optimization of the one-variable functional

Normalize by

\[
\alpha=\frac as\le\frac12,\qquad
\rho=\frac{ab}{s^2}=\alpha(1-\alpha),\qquad
\lambda=\frac cs\ge1,\qquad
y=\frac xs.
\]

Then

\[
\Gamma_{a,b,c}(x)
=s^2\gamma_{\rho,\lambda}(y),                               \tag{5.1}
\]

with

\[
\gamma_{\rho,\lambda}(y)
=
\frac{
\rho(\lambda-1+2y)-2y^2+y^3/3
}{
2(\lambda+2y)
},
\qquad 0\le y\le\alpha.                                    \tag{5.2}
\]

### 5.1 Strict unimodality

The derivative of (5.2) has the sign of

\[
h_{\rho,\lambda}(y)
=2\rho-4\lambda y+(\lambda-4)y^2+\frac43y^3,                \tag{5.3}
\]

because

\[
\gamma'_{\rho,\lambda}(y)
=\frac{h_{\rho,\lambda}(y)}
       {2(\lambda+2y)^2}.                                  \tag{5.4}
\]

The decisive factorization is

\[
\frac{\partial h_{\rho,\lambda}}{\partial y}
=2(y-2)(2y+\lambda)<0
\qquad(0\le y\le\alpha).                                   \tag{5.5}
\]

Also

\[
h_{\rho,\lambda}(0)=2\rho>0.
\]

At \(y=\rho/2\),

\[
h_{\rho,\lambda}\!\left(\frac\rho2\right)
=
\rho\left[
2(1-\lambda)
+\frac{\lambda-4}{4}\rho
+\frac{\rho^2}{6}
\right]<0.                                                 \tag{5.6}
\]

For fixed \(\rho\le1/4\), the bracket decreases with \(\lambda\); at
\(\lambda=1\) it equals

\[
-\frac{3\rho}{4}+\frac{\rho^2}{6}<0.
\]

Therefore (5.3) has one and only one zero

\[
0<y_*<\frac\rho2<\frac\alpha2.                              \tag{5.7}
\]

The function \(\gamma\) increases before \(y_*\) and decreases after it.
The endpoint constraint is never active.  Multiplying \(h(y_*)=0\) by
\(3s^3\) gives exactly the cubic (0.1).

An equivalent equation, useful for fixed \(a,b\), is

\[
\boxed{
c=
\frac{
2ab\,s-4sx_*^2+\frac43x_*^3
}{
x_*(4s-x_*)
}.}                                                       \tag{5.8}
\]

### 5.2 Optimized value

At a stationary point, the quotient rule identity is

\[
(\lambda+2y_*)\,n'(y_*)=2n(y_*),
\]

where \(n\) is the numerator of (5.2).  Hence

\[
\gamma_{\rho,\lambda}(y_*)
=\frac{n'(y_*)}{4}
=\frac\rho2-y_*+\frac{y_*^2}{4}.                            \tag{5.9}
\]

Returning to unnormalized variables proves (0.2).

The optimizer decreases strictly as the long-side ratio increases.
Indeed,

\[
\frac{\partial h}{\partial\lambda}=y(y-4)<0,
\qquad
\frac{\partial h}{\partial y}<0,
\]

so implicit differentiation gives

\[
\frac{dy_*}{d\lambda}<0.                                   \tag{5.10}
\]

Since the right side of (5.9) decreases with \(y_*\) on this range,
\(\mathcal E_{\rm EP}\) increases strictly with \(c\).  Moreover,

\[
x_*=\frac{ab}{2c}+O_{a,b}(c^{-2})
\]

and

\[
\mathcal E_{\rm EP}(a,b,c)
=\frac{ab}{2}-\frac{ab(a+b)}{2c}+O_{a,b}(c^{-2})
\qquad(c\to\infty).                                       \tag{5.11}
\]

Thus the sharp endpoint-band coefficient approaches \(ab/2\) from below.
This does not contradict the independently proved ordered-witness corridor
coefficient, which approaches \(ab\); that theorem uses additional
literal-order information not present in the endpoint-potential band dual.

## 6. Exact optimization at the width boundary

Set

\[
c=s=a+b,\qquad \lambda=1.
\]

The unique critical equation (5.3) becomes

\[
4y^3-9y^2-12y+6\rho=0,                                    \tag{6.1}
\]

which is (0.4).  Equivalently,

\[
\boxed{
\rho
=2y+\frac32y^2-\frac23y^3.}                               \tag{6.2}
\]

Substitution of (6.2) into (5.9) gives

\[
\gamma_{\rho,1}(y)
=y^2\left(1-\frac y3\right),                               \tag{6.3}
\]

proving the exact value (0.5).

### 6.1 Closed form for the correct cubic branch

Divide (6.1) by \(4\) and set

\[
y=z+\frac34.
\]

The cubic becomes

\[
z^3-\frac{75}{16}z+\frac{48\rho-99}{32}=0.                 \tag{6.4}
\]

Since \(0<\rho\le1/4\), the arccosine argument in (0.6) lies in
\([87/125,99/125)\).  The branch in (0.6) is the unique root from (5.7);
the other two real branches lie outside the admissible maximizing
interval.  This proves (0.6) without a branch ambiguity.

### 6.2 Explicit rational certificate

Equation (6.2) and \(0<y<1/2\) imply

\[
\frac\rho4<y_\rho<\frac\rho2.                              \tag{6.5}
\]

The former S2 test point \(y=\rho/4\) therefore lies below the true
optimizer.  A better elementary point is \(y=\rho/2\), which is still
admissible because \(\rho/2<\alpha\).  Direct substitution in (5.2) gives

\[
\gamma_{\rho,1}\!\left(\frac\rho2\right)
=
\rho^2\frac{1+\rho/12}{4(1+\rho)}.                          \tag{6.6}
\]

The factor \((1+\rho/12)/(1+\rho)\) decreases on
\(0<\rho\le1/4\), and its endpoint value is \(49/60\).
Multiplying by \(s^2\) proves (0.7).

The exact coefficient (0.5), not (0.7), is the optimized answer.

## 7. Audit and implication ledger

### Proved here

- the exact asymmetric-shoulder inequality (2.5);
- the arbitrary-depth rectangular shoulder profile (2.1)--(2.3);
- exact finite exclusion of shoulder depths beyond \(p\);
- exact balancing of finite shoulders, including odd total depth and
  integer ceilings;
- monotonic improvement from retaining all available plateau layers;
- the full two-variable fixed-ray functional (4.4);
- exclusion of all nontriangular shoulder depths from a positive optimum;
- strict optimality of symmetric shoulder depths;
- strict unimodality and the unique cubic optimizer (0.1);
- the closed optimized coefficient (0.2);
- the exact width-boundary root and coefficient (0.4)--(0.6); and
- the explicit boundary certificate (0.7).

No unproved lemma remains in these statements.

### Sharpness scope

The equality

\[
\sup_{\rm plateau\text{-}attached\ sloped\ rank\ bands}\Gamma
=\mathcal E_{\rm EP}(a,b,c)
\]

is proved for consecutive rank bands attached to the width plateau and
for the fixed endpoint-potential/vertical-capacity certificate.  It does
not assert optimality among:

- arbitrary column-dependent target regions;
- non-rank or disconnected target families;
- consecutive bands lying wholly inside one sloped shoulder and never
  reaching a plateau layer;
- other transverse potentials or combinations of potentials;
- lower bounds using the literal order of middle witnesses; or
- the actual class of all possible lower-bound arguments for \(g_3\).

In particular, the independent ordered-witness corridor bound may be
larger for sufficiently long boxes.

### Global implication scope

Equation (0.3), especially the positive boundary value (0.5), confirms
that every full-width-plateau ray has quadratic excess.  This refutes the
three-box width-plus-subquadratic ray gate and the uniform compact
three-box estimate.  It does not by itself lower-bound unrestricted
four-box words, Boolean contiguous-OR words, MWB, exact wreath factors, or
labelled common-owner synchronization.

The final optimized endpoint-potential statement is

\[
\boxed{
\begin{gathered}
\text{Every plateau-attached sloped rank band is dominated by a symmetric one,}\\
\text{and its unique optimal depth is the cubic root in (0.1).}
\end{gathered}}
\]
