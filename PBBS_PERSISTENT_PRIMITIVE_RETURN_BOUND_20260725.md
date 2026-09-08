# Persistent-primitivity cannot obstruct the fixed-Gaussian PBBS gate

Date: 2026-07-25

No computation or external input is used.

## 0. Outcome

Let \(N=2r+1\), let \(\tau=\phi^2\) be the normalized two-step PBBS
map on semilength-\(r\) Dyck roots, and write

\[
 D_h=\tau^hD.
\]

The tempting assertion that \(\tau\) preserves primitive Dyck paths is
false: for example

\[
 D=110100
 \quad\hbox{is primitive, whereas}\quad
 \tau D=110010
 \]

is not.  Nevertheless the genuinely persistent unit-deficit subclass is
harmless.  For every fixed \(A>0\), the number of roots whose first-maximum
sector deficit stays equal to one until a
consecutive omitted-label return of gap at most \(2A\sqrt r+1\) is

\[
 \boxed{
  4^r\exp(-c_A r^{1/4})
  =o_A(\operatorname{Cat}_r/r^K)
 }
\]

for every fixed \(K\).  Thus neither primitive roots nor unary-root trees
whose whole relevant \(\tau\)-trajectory has unit sector deficit can
furnish a counterexample to the fixed-window residence statement.  Any
dangerous unary-root family must acquire a nontrivial sector suffix before
its return.

## 1. The exact return equation in the persistent sector

Use the first-maximum decomposition

\[
 D_h=P_h1R_h0S_h,
 \qquad d(D_h)=|S_h|+1.
\]

A primitive Dyck word certainly has empty root-branch suffix \(S_h\), but
the converse need not hold because smaller primitive components may precede
the final maximum-bearing component.  The exact condition needed below is

\[
 S_h=\varnothing\quad\Longleftrightarrow\quad d(D_h)=1.
\]

### Lemma 1.1

Suppose that

\[
 D_0,D_1,\ldots,D_{s-1}
\]

all satisfy \(d(D_h)=1\), and that the omitted physical coordinate at \((u,D_0)\)
returns after \(2s+1<N\) PBBS updates.  Then

\[
 \boxed{\delta(D_s)=s,}
\]

where \(\delta(E)\) is the position of the first up-step attaining the
global maximum of \(E\).

#### Proof

The exact two-step skew product is

\[
 (u,D_h)\longmapsto(u-d(D_h),D_{h+1})\pmod N.
\]

The unit-deficit hypothesis gives \(d(D_h)=1\) for \(0\le h<s\), so after
the \(s\) two-step moves the spatial root is \(u-s\).  The last odd PBBS
move advances it by \(\delta(D_s)\).  A return therefore gives

\[
 \delta(D_s)\equiv s\pmod N.
\]

Both quantities lie strictly between zero and \(N\), so the congruence is
the displayed integer equality. \(\square\)

The map \(\tau\) is a bijection.  Consequently the number of possible
starts in Lemma 1.1 is no larger than the number of Dyck paths whose first
global maximum is attained at step \(s\).  We now bound that endpoint
class.

## 2. Early first maxima are stretched-exponentially sparse

Let \(M_{r,t}\) be the number of semilength-\(r\) Dyck paths for which the
first visit to the global maximum ends at step \(t\).

### Theorem 2.1

There are absolute constants \(c,C>0\) such that, uniformly for
\(1\le t\le r\),

\[
 \boxed{
  M_{r,t}
  \le C r^2 4^r
       \exp\!\left[-c\sqrt{r/t}\right].
 }
\]

#### Proof

Fix the attained maximum height \(h\), where \(1\le h\le t\).  Ignore
the first-visit restriction in the prefix and the exact-maximum restriction
in the suffix; this only enlarges the class.

The number of length-\(t\) binary walks from zero to \(h\) is at most

\[
 \binom{t}{(t+h)/2}
 \le 2^t\exp\!\left(-{h^2\over2t}\right),
\]

with the usual convention that a parity-incompatible binomial is zero.
After the marked step, the remaining walk has length \(2r-t\), starts at
height \(h\), ends at zero, and stays in \(\{0,1,\ldots,h\}\).  The
adjacency matrix of this path graph has spectral radius

\[
 2\cos {\pi\over h+2}.
\]

Bounding one matrix entry by its operator norm and using
\(\cos x\le \exp(-x^2/3)\) for \(0\le x\le\pi/3\), with a harmless
adjustment for \(h=1\), gives

\[
 \#\{\hbox{such suffixes}\}
 \le 2^{2r-t}
      \exp\!\left(-c_0{r\over(h+2)^2}\right)
\]

for an absolute \(c_0>0\).

Thus the contribution of height \(h\) is at most

\[
 4^r\exp\!\left(
   -{h^2\over2t}-c_0{r\over(h+2)^2}
 \right).
\]

For \(h\ge2\), the arithmetic--geometric mean inequality gives

\[
 {h^2\over2t}+c_0{r\over(h+2)^2}
 \ge c_1\sqrt{r/t}
\]

with an absolute \(c_1>0\); the cases \(h=1\) are stronger after reducing
\(c_1\).  Summing over at most \(r\) heights and absorbing all small
values of \(r\) into \(C r^2\) proves the theorem. \(\square\)

### Corollary 2.2

For every fixed \(A>0\),

\[
 \sum_{1\le t\le A\sqrt r}M_{r,t}
 \le C_A r^3 4^r e^{-c_A r^{1/4}}
 =o_A(\operatorname{Cat}_r/r^K)
\]

for every fixed \(K\).

#### Proof

For \(t\le A\sqrt r\), Theorem 2.1 has

\[
 \sqrt{r/t}\ge A^{-1/2}r^{1/4}.
\]

Sum over at most \(A\sqrt r+1\) values of \(t\), and use
\(\operatorname{Cat}_r\asymp4^r/r^{3/2}\). \(\square\)

## 3. Consequence and exact boundary

Combining Lemma 1.1 with Corollary 2.2 proves the outcome in Section 0.
The argument is deliberately limited: an initially primitive root usually
leaves the unit-deficit sector under \(\tau\).  For example

\[
 110100\longmapsto110010.
\]

Once some \(d(D_h)=|S_h|+1\) exceeds one, the exact return equation is

\[
 \sum_{h=0}^{s-1}d(D_h)=\delta(D_s)+aN,
\]

and no early-first-maximum conclusion follows.  Therefore the theorem
removes the persistent-unary candidate only.  The coefficient-one problem
still requires a weighted estimate for trajectories with nontrivial sector
deficits, equivalently the Pascal-weighted predecessor-passage gate in the
current PBBS residence reduction.
