# Master redirect, lane U: the compact four-box local theorem is false

Date: 2026-07-25

## 0. Definitive lane verdict

Let

\[
Q_n=[0,36n]^3\times[0,105n].
\]

This is a compact-balanced strict-polygon-interior four-box:

\[
\max_i\ell_i=105n,\qquad
\min_i\ell_i=36n>\frac13(105n),
\]

and

\[
105n<36n+36n+36n.
\]

Nevertheless,

\[
\boxed{
\liminf_{n\to\infty}
\frac{g_4(36n,36n,36n,105n)
-w_4(36n,36n,36n,105n)}
{n^3}
\ge\frac{165579}{512}>0.}
\tag{0.1}
\]

Equivalently, with \(R_n=\max_i\ell_i=105n\),

\[
\boxed{
\liminf_{n\to\infty}
\frac{g_4(Q_n)-w_4(Q_n)}{R_n^3}
\ge
\frac{165579}{512\cdot105^3}>0.}
\tag{0.2}
\]

Therefore there is no function \(\varepsilon(R)\to0\) for which

\[
g_4(\ell_1,\ell_2,\ell_3,\ell_4)
\le
w_4(\ell_1,\ell_2,\ell_3,\ell_4)
+\varepsilon(R)R^3
\tag{0.3}
\]

holds for every strict-polygon-interior integer four-box satisfying

\[
\frac R3\le\ell_i\le R.
\]

This refutes the compact-balanced local theorem assigned to lane U.  A
reset-free surface braid inside one exact parent is a literal word counted
by \(g_4\), so no chronology, portal degree, or hook reorganization can
evade (0.1).  The no-go is architecture-free.

It does not refute the equal ray, a word sharing letters between different
four-box parents, or the global constant-one conjecture.  It definitively
closes the proposed **uniform one-parent compact four-box route**.

No computation, finite search, or external source is used below.

## 1. Literal subbox monotonicity

For a product of chains \(Q\), let \(g(Q)\) be the minimum length of a word
of nonzero points of \(Q\) whose nonempty contiguous coordinatewise maxima
contain every nonzero target of \(Q\).

### Lemma 1.1 (origin-subbox monotonicity — PROVED)

If \(Q'\) is an origin-anchored coordinate subbox of \(Q\), then

\[
\boxed{g(Q)\ge g(Q').}
\tag{1.1}
\]

#### Proof

Take any universal word for \(Q\) and delete every letter outside \(Q'\).
If an interval witnesses a target \(T\in Q'\), then every letter in that
interval is coordinatewise at most \(T\), hence already belongs to \(Q'\).
The whole selected interval survives; deleting other letters merely
compresses it.  Thus the restricted word is universal for \(Q'\).
\(\square\)

This proof permits arbitrary crossing intervals and arbitrary ambient
letters from the larger parent.  It is therefore already stronger than an
obstruction to a particular shell decomposition.

### Lemma 1.2 (translated ambient retraction — PROVED)

Let

\[
B=\prod_{i=1}^4[a_i,a_i+\ell_i]
\]

be a translated four-box inside an ambient product of chains.  Any ambient
word covering every target of \(B\) has length at least
\(g_4(\ell_1,\ell_2,\ell_3,\ell_4)\).

#### Proof

In coordinate \(i\), define

\[
\pi_i(x)=
\min\{\ell_i,\max\{0,x_i-a_i\}\}.
\]

The map \(\pi=(\pi_i)\) preserves coordinatewise joins and is the identity
in local coordinates on \(B\).  Project every ambient letter and delete
zero images.  A witness for a nonzero local target projects to a witness
for the same target; deletion of zero images only compresses its interval.
Thus the projected word is a local universal word of no greater length.
\(\square\)

If the translated local origin is itself a demanded nonzero ambient
target, that adds a requirement and cannot weaken the lower bound.

## 2. The exact boundary shoulder bound

The only nontrivial input is the audited two-endpoint shoulder inequality.
Its four-dimensional specialization is recorded here in the exact integral
form needed below.

### Lemma 2.1 (symmetric four-box shoulder — PROVED)

Let

\[
B=(p+1)(q+1)(s+1),\qquad P=p+q+s,
\]

assume \(r\ge P>0\), and let
\(0\le k\le\min\{p,q,s\}\) be integral.  If a universal word
for

\[
[0,p]\times[0,q]\times[0,s]\times[0,r]
\]

has length \(B+D\), then

\[
\boxed{
2(r+2k)D
\ge
(r-P+2k)B
+6\binom{k+2}{4}
-(4P+2)\binom{k+2}{3}.}
\tag{2.1}
\]

#### Proof

Choose one witness for every target in the symmetric rank band

\[
P-k,\ldots,r+k.
\]

Targets with one common left endpoint form a target-poset chain, and the
same holds on the right.  A left class and a right class meet in at most
one target, since two common targets would have the same physical interval.

For one endpoint partition, consecutive occupied band layers force
target-poset covers.  Telescope the transverse potential

\[
\phi(x_1,x_2,x_3,x_4)=x_1+x_2+x_3.
\]

The lower and upper shoulder omissions have exact corner counts

\[
F_k=\binom{k+2}{3},\qquad
E_k=\binom{k+3}{4},\qquad
M_k=3\binom{k+2}{4}.
\]

Put

\[
J=r-P+2k,\qquad
B_0=B-F_k,\qquad
T=(J+1)B-2E_k.
\]

Here \(B_0\) is either boundary-layer size and \(T\) is the total number of
band targets.  The number of available fourth-coordinate covers is

\[
A_v=T-B=JB-2E_k,
\]

while the boundary transverse-potential difference is

\[
\Delta_\phi=PF_k-2M_k.
\]

If one endpoint partition has \(C\) nonempty classes, adjacent occupied
layers force at least \(2T-2B_0-JC\) band covers.  Its transverse covers
are at most

\[
\Delta_\phi+P(C-B_0).
\]

Thus its fourth-coordinate covers number at least

\[
2T-2B_0-\Delta_\phi+PB_0-(J+P)C.
\]

The two endpoint partitions cannot use the same fourth-coordinate cover.
Add their lower bounds, compare with \(A_v\), use
\(J+P=r+2k\), and substitute

\[
C_L+C_R\le2(B+D).
\]

After collecting terms one obtains

\[
2(r+2k)D
\ge
(r-P+2k)B
+4F_k-6E_k+4M_k-4PF_k.
\]

Pascal's identities reduce the correction to

\[
6\binom{k+2}{4}-(4P+2)\binom{k+2}{3},
\]

which is (2.1).  No canonical witness, saturation, or physical adjacency
assumption occurs. \(\square\)

### Corollary 2.2 (integral boundary ray — PROVED)

For integral \(t\to\infty\),

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_4(t,t,t,3t)-(t+1)^3}{t^3}
\ge\frac{49}{512}.}
\tag{2.2}
\]

Consequently,

\[
\boxed{
g_4(t,t,t,3t)
\ge
\frac{561}{512}t^3-O(t^2).}
\tag{2.3}
\]

#### Proof

In (2.1), take

\[
p=q=s=t,\qquad r=P=3t,\qquad
k=\left\lfloor\frac t2\right\rfloor.
\]

Then \(B=(t+1)^3\), and the right side of (2.1) has leading term

\[
\left(
1-\frac14+\frac1{64}
\right)t^4
=\frac{49}{64}t^4.
\]

The denominator \(2(3t+2k)\) is

\[
8t+O(1).
\]

Floors and the lower-degree binomial terms change the quotient by only
\(O(t^2)\).  Hence

\[
D\ge\frac{49}{512}t^3-O(t^2),
\]

which proves (2.2).  Adding
\((t+1)^3=t^3+O(t^2)\) gives (2.3). \(\square\)

The sign convention in \(O(t^2)\) is immaterial: the precise statement is
the liminf (2.2).

## 3. Exact width of the strict-interior parent

We use the following standard central-section count, with its constant
included.

### Lemma 3.1 (four-box width on the \((1,1,1,d)\) ray — PROVED)

Fix \(1\le d\le3\), with integral rounding understood.  Then

\[
\boxed{
w_4(t,t,t,dt)
=
\left(
1-\frac{(3-d)^3}{24}
\right)t^3+O(t^2).}
\tag{3.1}
\]

#### Proof

The product rank sequence is symmetric and unimodal, so its width is a
middle-rank coefficient.  At a middle rank, the fourth coordinate is legal
exactly when the normalized sum of the first three coordinates lies
between

\[
a=\frac{3-d}{2}
\qquad\text{and}\qquad
3-a.
\]

Inside the unit cube, the omitted regions are two opposite tetrahedra, each
of volume \(a^3/6\).  Their total volume is

\[
\frac{a^3}{3}=\frac{(3-d)^3}{24}.
\]

The lattice boundary contributes \(O(t^2)\); middle-rank rounding also
changes only \(O(t^2)\) points.  This proves (3.1). \(\square\)

For \(t=36n\) and

\[
d=\frac{105}{36}=\frac{35}{12},
\]

formula (3.1) gives

\[
\boxed{
w_4(36n,36n,36n,105n)
=
\left(36^3-\frac98\right)n^3+O(n^2).}
\tag{3.2}
\]

Indeed \(3-d=1/12\), and

\[
36^3\frac{(1/12)^3}{24}=\frac98.
\]

For completeness, the width has exact parity forms.  If \(n=2m\), then

\[
\boxed{
w_4(Q_n)
=(72m+1)^3-2\binom{3m+2}{3}.}
\tag{3.3}
\]

If \(n=2m+1\), then

\[
\boxed{
w_4(Q_n)
=(72m+37)^3
-\binom{3m+3}{3}
-\binom{3m+4}{3}.}
\tag{3.4}
\]

At a middle rank, the first three coordinates range over the full short
cube except for a low corner and its complementary high corner.
Stars-and-bars gives the displayed binomial counts.  Expanding either
formula recovers (3.2), including both parities.

## 4. The strict-interior counterexample

### Theorem 4.1 (compact-balanced local no-go — PROVED)

The bound (0.1) holds.

#### Proof

The parent \(Q_n\) contains the origin-anchored boundary subbox

\[
Q'_n=[0,35n]^3\times[0,105n].
\tag{4.1}
\]

This is exactly the boundary ray of Corollary 2.2 with \(t=35n\).  By
Lemma 1.1 and (2.3),

\[
\begin{aligned}
g_4(Q_n)
&\ge g_4(Q'_n)\\
&\ge
\frac{561}{512}\,35^3n^3-O(n^2).
\end{aligned}
\tag{4.2}
\]

Subtract (3.2).  The leading coefficient is

\[
\begin{aligned}
\frac{561}{512}35^3
-36^3+\frac98
&=
\frac{
561\cdot35^3-512\cdot36^3+576
}{512}\\
&=\frac{165579}{512}.
\end{aligned}
\tag{4.3}
\]

Taking the liminf proves (0.1), and division by \(105^3\) proves (0.2).
\(\square\)

Every side length and every selected subbox side in this proof is integral.
The argument stays inside one exact parent factor throughout.

## 5. An open strict-interior collar

The obstruction is not an isolated rational ray.

### Theorem 5.1 (open collar no-go — PROVED)

For fixed \(1\le d<3\), let

\[
\eta(d)=
\frac{561}{512}\left(\frac d3\right)^3
-\left(1-\frac{(3-d)^3}{24}\right).
\tag{5.1}
\]

Whenever \(\eta(d)>0\),

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_4(t,t,t,dt)-w_4(t,t,t,dt)}{t^3}
\ge\eta(d)>0,}
\tag{5.2}
\]

with integral rounding changing only \(O(t^2)\).

In particular, (5.2) holds on a nonempty open interval of strict-interior
ratios \(d<3\).

#### Proof

Put \(L_t=\lfloor dt\rfloor\) and

\[
s_t=\left\lfloor\frac{L_t}{3}\right\rfloor.
\]

The full box contains the integral subbox

\[
[0,s_t]^3\times[0,3s_t],
\]

and \(s_t=(d/3)t+O(1)\).  This is a \((1,1,1,3)\) boundary box at scale
\(s_t\).  Lemma 1.1, Corollary 2.2, and Lemma 3.1 give exactly
(5.1)--(5.2), with all rounding absorbed in \(O(t^2)\).

Finally,

\[
\eta(3)=\frac{561}{512}-1=\frac{49}{512}>0.
\]

Continuity gives a nonempty interval immediately below \(3\) on which
\(\eta(d)>0\). \(\square\)

The explicit value \(d=35/12\) used in Theorem 4.1 lies in this collar;
(4.3) verifies positivity without any numerical approximation.

### Theorem 5.2 (full-dimensional robust collar — PROVED)

Put \(\delta=1/100\).  For every integer four-tuple satisfying

\[
|\ell_j-36n|\le\delta n\quad(1\le j\le3),
\qquad
|\ell_4-105n|\le\delta n,
\tag{5.3}
\]

one has, uniformly,

\[
\boxed{
g_4(\boldsymbol\ell)-w_4(\boldsymbol\ell)
\ge c_\delta n^3-O(n^2),}
\tag{5.4}
\]

where

\[
c_\delta=
\frac{561}{512}\left(35-\frac{\delta}{3}\right)^3
-(36+\delta)^3>0.
\tag{5.5}
\]

#### Proof

Let

\[
s_n=\left\lfloor
\left(35-\frac{\delta}{3}\right)n
\right\rfloor.
\]

The inequalities (5.3) imply

\[
[0,s_n]^3\times[0,3s_n]
\subseteq
\prod_{i=1}^4[0,\ell_i].
\]

Indeed \(s_n<(36-\delta)n\), and
\(3s_n\le(105-\delta)n\).  Lemma 1.1 and Corollary 2.2 give

\[
g_4(\boldsymbol\ell)
\ge
\frac{561}{512}
\left(35-\frac{\delta}{3}\right)^3n^3
-O(n^2).
\tag{5.6}
\]

Every antichain projects injectively onto the first three coordinates:
two points with the same projection differ only in their fourth coordinate
and are comparable.  Hence

\[
w_4(\boldsymbol\ell)
\le\prod_{j=1}^3(\ell_j+1)
\le(36+\delta)^3n^3+O(n^2).
\tag{5.7}
\]

It remains only to check the sign in (5.5), without decimal
approximation.  At \(\delta=0\),

\[
\frac{561}{512}35^3-36^3
=\frac{165003}{512}>300.
\]

For \(0\le\delta\le1\),

\[
\frac{561}{512}
\left(35^3-\left(35-\frac{\delta}{3}\right)^3\right)
<2450\delta,
\]

and

\[
(36+\delta)^3-36^3
\le3\cdot37^2\delta=4107\delta.
\]

At \(\delta=1/100\), the total loss is less than
\(6557/100<66\).  Thus \(c_\delta>234>0\). \(\square\)

## 6. Consequence for the constant-one route

### Corollary 6.1 (uniform compact local gate is impossible — PROVED)

No uniform compact-balanced theorem of the form (0.3) is true.  In
particular, it cannot be used as the four-box local input to prove

\[
\nu(k)\le(1+o(1))W(k).
\]

#### Proof

The sequence \(Q_n\) lies in the fixed compact aspect window

\[
\frac13R_n\le\ell_i\le R_n
\]

and in the strict polygon interior, while (0.2) contradicts (0.3).
\(\square\)

The robust neighborhood in Theorem 5.2 also rules out paying four-box
factors independently in an averaged construction from four independent
SCD heights whose underlying block sizes are fixed positive proportions of
\(k\).
The normalized SCD height law has positive continuous density on every
compact positive interval, so (5.3), after a fixed common rescaling, has
positive limiting product mass.  On that event
\(R=\Theta(\sqrt{k})\), and (5.4) charges
\(\Theta(k^{3/2})\) local excess.  Since \(g_4\ge w_4\) for every nonzero
box, contributions outside the neighborhood cannot cancel it: selected
witnesses for two incomparable maximum-antichain targets cannot have one
common left endpoint, because intervals with a common left endpoint are
nested and have comparable maxima.  Thus the
averaged local gate

\[
\mathbb E\,[g_4(L_1,L_2,L_3,L_4)-w_4(L_1,L_2,L_3,L_4)]
=o(k^{3/2})
\]

also fails for independently paid parents.

This last statement does not constrain a genuinely global word which
shares physical letters or endpoints across different four-box parents.
It also does not address an average artificially supported in a
near-diagonal shape sector.  Such variants are outside the local \(g_4\)
theorem assigned to lane U.

## 7. Audit and exact scope

### Proved

- literal origin-subbox monotonicity;
- the exact integral shoulder inequality used at the boundary;
- the boundary coefficient \(49/512\);
- the strict-interior width coefficient;
- the exact positive gap \(165579/512\);
- both a one-parameter and a full-dimensional strict-interior collar of
  counterexamples;
- failure of the uniform compact-balanced and independently paid averaged
  local gates.

### Not claimed

- a lower bound on \(g_4(R,R,R,R)-w_4(R,R,R,R)\);
- a lower bound on a global Boolean word sharing across product parents;
- a disproof of the constant-one conjecture itself.

### Independent audits

1. The boundary audit substituted
   \(t=35n\), \(k=\lfloor t/2\rfloor\) directly into the finite shoulder
   polynomial
   \[
   \mathcal N(t,k)=
   2k(t+1)^3+6\binom{k+2}{4}
   -(12t+2)\binom{k+2}{3}
   \]
   and recovered
   \[
   \mathcal N(t,k)=\frac{49}{64}t^4+O(t^3).
   \]
   It independently derived both exact parity formulae (3.3)--(3.4) and
   checked
   \[
   \frac{561\cdot35^3}{512}-36^3+\frac98
   =\frac{165579}{512}.
   \]
   Verdict: pass.

2. A separate literal-scope audit reconstructed Lemmas 1.1--1.2 and
   confirmed that arbitrary foreign parent letters, crossing intervals,
   translations, and a demanded translated origin cannot weaken the
   lower bound.  It also checked that the result refutes every
   one-parent surface theorem implying uniform compact \(g_4=w_4+o(R^3)\),
   but not cross-parent global sharing.  Verdict: pass.

3. The first averaging audit found a real quantifier gap: a single rational
   ray has zero limiting SCD mass.  Theorem 5.2 is the repair.  Its
   full-dimensional integer neighborhood, projection width bound, and
   positive coefficient \(c_\delta>234\) were then independently
   rechecked.  This supplies positive product-Rayleigh mass and validates
   the independently paid averaged no-go.  Verdict after repair: pass.

### Final implication

\[
\boxed{
\text{compact-balanced one-parent four-box theorem}
\quad\textbf{is false}.}
\tag{7.1}
\]

Therefore a reset-free surface braid cannot prove that theorem.  Any
surviving constant-one proof must either restrict to a genuinely smaller
local shape family (for example, a still-open equal-ray theorem) and prove
that all excluded shapes are negligible, or fuse different exact parents
globally.  Neither operation belongs to the lane closed here.
