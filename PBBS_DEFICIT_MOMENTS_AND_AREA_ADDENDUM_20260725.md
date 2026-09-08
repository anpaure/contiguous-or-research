# PBBS deficit moments and the block-rotation area identity

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, or web search
is used.

## 0. Result

Let \(\mathcal D_m\) be the Dyck words of semilength \(m\), put

\[
 B_m=|\mathcal D_m|=\operatorname{Cat}_m,
 \qquad N=2m+1,
\]

and use the canonical first-highest-component factorization

\[
 D=P\,1\,R\,0\,S.
\]

Thus \(S\) is the terminal Dyck suffix after the first primitive component
which attains the global height.  Define

\[
 a(D)=|P|+1,
 \qquad b(D)=|R|+1,
 \qquad c(D)=|S|+1.
\]

Then \(a+b+c=N\) and the PBBS two-step quotient map is

\[
 \tau D=S\,1\,P\,0\,R.
\]

The purpose of this addendum is to prove the matching upper and lower
orders

\[
 \boxed{
  \sum_{D\in\mathcal D_m}c(D)
   =\Theta\!\left(\sqrt m\,B_m\right)
   =\Theta\!\left({4^m\over m}\right),}
 \tag{0.1}
\]

and

\[
 \boxed{
  \sum_{D\in\mathcal D_m}c(D)^2
   =\Theta\!\left(m^{3/2}B_m\right)
   =\Theta(4^m).}
 \tag{0.2}
\]

All constants in \(\Theta(\cdot)\) are absolute.  The proof includes a
uniform height-pair estimate strong enough when the suffix has semilength
arbitrarily close to either \(0\) or \(m\).

We also audit the area convention.  If

\[
 \operatorname{ar}(D)=\sum_{t=0}^{2m-1}H_D(t)
\]

is the sum of the heights immediately before the steps of \(D\), then

\[
 \boxed{
  \operatorname{ar}(\tau D)-\operatorname{ar}(D)=a(D)-b(D).}
 \tag{0.3}
\]

For balanced words, summing post-step heights or all vertex heights gives
the same value, so (0.3) has no endpoint-convention ambiguity.

## 1. Uniform Catalan and height estimates

Write

\[
 C_n=\operatorname{Cat}_n={1\over n+1}{2n\choose n}.
\]

The Stirling bounds give absolute constants \(0<c<C<\infty\) such that

\[
 c{4^n\over(n+1)^{3/2}}
 \le C_n\le
 C{4^n\over(n+1)^{3/2}}
 \qquad(n\ge0).
 \tag{1.1}
\]

For \(D\in\mathcal D_n\), let \(\operatorname{ht}(D)\) be its maximum
height, and put

\[
 A_h(n)=\#\{D\in\mathcal D_n:\operatorname{ht}(D)\le h\}.
\]

### Lemma 1.1 (two uniform height tails)

There are absolute constants \(c,C>0\) such that

\[
 {C_n-A_{h-1}(n)\over C_n}
 \le C\exp\!\left(-c{h^2\over n}\right)
 \qquad(\sqrt n\le h\le n),
 \tag{1.2}
\]

and

\[
 {A_h(n)\over C_n}
 \le C\exp\!\left(-c{n\over(h+2)^2}\right)
 \qquad(0\le h\le\sqrt n).
 \tag{1.3}
\]

#### Proof of the upper-height tail

Put

\[
 B_n(r)={2n\choose n+r},
\]

with \(B_n(r)=0\) when \(|r|>n\).  The two-barrier reflection formula for
walks in the strip \(\{0,1,\ldots,h-1\}\) is

\[
 A_{h-1}(n)
 =\sum_{\ell\in\mathbb Z}
   \bigl(B_n(\ell q)-B_n(\ell q+1)\bigr),
 \qquad q=h+1.
 \tag{1.4}
\]

This is obtained by reflecting successively in the two forbidden lines
\(-1\) and \(h\); the images of a return to zero have endpoint offsets
\(2\ell q\) and \(2\ell q+2\), with opposite signs.  The \(\ell=0\)
term is

\[
 B_n(0)-B_n(1)=C_n.
\]

Pairing \(\ell\) with \(-\ell\) in (1.4) therefore gives the exact identity

\[
 C_n-A_{h-1}(n)
 =\sum_{\ell\ge1}
 \bigl(B_n(\ell q-1)-2B_n(\ell q)+B_n(\ell q+1)\bigr).
 \tag{1.5}
\]

The binomial ratio satisfies

\[
 {B_n(r)\over B_n(0)}
 =\prod_{u=1}^{r}{n-u+1\over n+u}
 \le \exp\!\left(-{r^2\over2n}\right)
 \qquad(0\le r\le n).
 \tag{1.6}
\]

For \(r\le n/2\), the exact adjacent ratios

\[
 {B_n(r+1)\over B_n(r)}={n-r\over n+r+1},
 \qquad
 {B_n(r-1)\over B_n(r)}={n+r\over n-r+1}
\]

give

\[
 |B_n(r-1)-2B_n(r)+B_n(r+1)|
 \le C\left({1\over n}+{r^2\over n^2}\right)B_n(r).
 \tag{1.7}
\]

For \(r>n/2\), the crude bound by \(4B_n(r-1)\), together with (1.6),
has the same exponential order after reducing the constant in the
exponent.  Since \(C_n=B_n(0)/(n+1)\), equations (1.5)--(1.7) imply

\[
 {C_n-A_{h-1}(n)\over C_n}
 \le C\sum_{\ell\ge1}
 \left(1+{\ell^2q^2\over n}\right)
 \exp\!\left(-c{\ell^2q^2\over n}\right).
 \tag{1.8}
\]

When \(q\ge\sqrt n\), the sum in (1.8) is at most
\(C\exp(-cq^2/n)\).  Since \(q=h+1\), this proves (1.2), after changing
the absolute constants.

#### Proof of the lower-height tail

Dyck paths of height at most \(h\) are the length-\(2n\) returns to zero
in the path graph on \(\{0,1,\ldots,h\}\).  Diagonalizing its adjacency
matrix gives

\[
 A_h(n)
 ={2\over q}\sum_{r=1}^{q-1}
   \sin^2{r\pi\over q}
   \left(2\cos{r\pi\over q}\right)^{2n},
 \qquad q=h+2.
 \tag{1.9}
\]

Pair the terms \(r\) and \(q-r\).  For \(1\le r\le q/2\),

\[
 \sin{r\pi\over q}\le {\pi r\over q},
 \qquad
 \left|\cos{r\pi\over q}\right|
 \le \exp\!\left(-c{r^2\over q^2}\right).
\]

Consequently

\[
 A_h(n)
 \le {C4^n\over q^3}
      \sum_{r\ge1}r^2
       \exp\!\left(-c{nr^2\over q^2}\right).
 \tag{1.10}
\]

If \(q\le\sqrt n+2\), the sum is at most
\(C\exp(-cn/q^2)\), with constants enlarged for the bounded transition
range.  Dividing (1.10) by the lower bound in (1.1) gives

\[
 {A_h(n)\over C_n}
 \le C\left({n\over q^2}\right)^{3/2}
          \exp\!\left(-c{n\over q^2}\right)
 \le C\exp\!\left(-c'{n\over q^2}\right),
\]

which is (1.3).  \(\square\)

The same spectral formula also supplies a lower population at every fixed
square-root height.

### Lemma 1.2 (a bounded-height population)

Fix \(\kappa>0\).  There is \(c_\kappa>0\) such that, whenever
\(m/3\le n\le2m/3\) and

\[
 L=\lfloor\kappa\sqrt m\rfloor,
\]

one has, for all sufficiently large \(m\),

\[
 A_{L-1}(n)\ge c_\kappa C_n.
 \tag{1.11}
\]

#### Proof

In (1.9), with \(q=L+1\), retain the nonnegative term \(r=1\).  The
inequalities

\[
 \sin(\pi/q)\ge {2\over q},
 \qquad
 \cos(\pi/q)\ge\exp(-C/q^2)
\]

give

\[
 A_{L-1}(n)
 \ge c q^{-3}4^n\exp(-Cn/q^2)
 \ge c_\kappa{4^n\over m^{3/2}}.
\]

Now use \(n\asymp m\) and the upper bound in (1.1).  \(\square\)

### Lemma 1.3 (the height-pair estimate)

For integers \(1\le k\le j\),

\[
 \boxed{
 \#\{(U,V)\in\mathcal D_k\times\mathcal D_j:
          \operatorname{ht}(V)\le\operatorname{ht}(U)\}
 \le C C_kC_j
       \exp\!\left(-c\sqrt{j/k}\right).}
 \tag{1.12}
\]

#### Proof

Put \(t=(jk)^{1/4}\).  Since \(k\le j\), one has

\[
 \sqrt k\le t\le\sqrt j.
\]

If \(\operatorname{ht}(V)\le\operatorname{ht}(U)\), then either
\(\operatorname{ht}(U)\ge t\) or
\(\operatorname{ht}(V)\le t\).  Lemma 1.1, with harmless integer
rounding of \(t\), gives

\[
 \Pr(\operatorname{ht}(U)\ge t)
 \le C\exp\!\left(-c{t^2\over k}\right),
\]

where the left side is simply zero if \(t>k\), and

and

\[
 \Pr(\operatorname{ht}(V)\le t)
 \le C\exp\!\left(-c{j\over t^2}\right).
\]

Both exponents equal \(\sqrt{j/k}\).  Multiplication by \(C_kC_j\)
proves (1.12).  \(\square\)

Notice that (1.12) becomes exponentially strong when \(k\) is small.
This is the estimate needed for suffix sizes \(j=m-O(1)\); a bare Catalan
convolution loses a power of \(m\) in precisely that regime.

## 2. The upper moment bounds, including both endpoints

Let \(b_{m,j}\) be the number of \(D\in\mathcal D_m\) with

\[
 |S|=2j,
 \qquad c(D)=2j+1.
\]

Put \(k=m-j\).  The prefix through the distinguished first-highest
primitive component is a Dyck path \(U\in\mathcal D_k\), and the terminal
suffix is a Dyck path \(V=S\in\mathcal D_j\).  Necessarily

\[
 \operatorname{ht}(V)\le\operatorname{ht}(U).
\]

For fixed \(j\), the map \(D\mapsto(U,V)\) is injective.  Hence

\[
 b_{m,j}\le C_kC_j                                      \tag{2.1}
\]

always, while Lemma 1.3 gives, when \(j\ge k\),

\[
 b_{m,j}
 \le C C_kC_j\exp\!\left(-c\sqrt{j/k}\right).       \tag{2.2}
\]

For \(p=1,2\), set

\[
 M_p(m)=\sum_{D\in\mathcal D_m}c(D)^p
       =\sum_{j=0}^{m-1}(2j+1)^p b_{m,j}.             \tag{2.3}
\]

First take \(0\le j\le m/2\).  Then \(k\ge m/2\), and (1.1), (2.1)
give

\[
 (2j+1)^p b_{m,j}
 \le C_p4^m m^{-3/2}(j+1)^{p-3/2}.                  \tag{2.4}
\]

Therefore

\[
 \sum_{0\le j\le m/2}(2j+1)b_{m,j}
 \le C{4^m\over m},                                 \tag{2.5}
\]

and

\[
 \sum_{0\le j\le m/2}(2j+1)^2b_{m,j}
 \le C4^m.                                          \tag{2.6}
\]

These estimates include \(j=0\), using the \((j+1)\)-form of (1.1).

Now take \(m/2<j<m\), and write \(k=m-j\), so \(1\le k<m/2\).
Equations (1.1) and (2.2) give

\[
 (2j+1)^p b_{m,j}
 \le C_p4^m m^{p-3/2}(k+1)^{-3/2}
       \exp\!\left(-c\sqrt{m/(k+1)}\right).         \tag{2.7}
\]

The elementary dyadic estimate

\[
 \sum_{k=1}^{m/2}(k+1)^{-3/2}
       \exp\!\left(-c\sqrt{m/(k+1)}\right)
 \le C m^{-1/2}                                     \tag{2.8}
\]

follows by grouping the integers for which
\(2^r\le\sqrt{m/(k+1)}<2^{r+1}\): the \(r\)-th group contributes at
most \(Cm^{-1/2}2^r e^{-c2^r}\).  Consequently

\[
 \sum_{m/2<j<m}(2j+1)b_{m,j}
 \le C{4^m\over m},                                 \tag{2.9}
\]

and

\[
 \sum_{m/2<j<m}(2j+1)^2b_{m,j}
 \le C4^m.                                          \tag{2.10}
\]

In particular, the extreme case \(j=m-1\), where \(k=1\), is absorbed
by the factor \(\exp(-c\sqrt m)\).  Combining (2.5)--(2.10) proves

\[
 \boxed{M_1(m)=O(4^m/m),\qquad M_2(m)=O(4^m).}       \tag{2.11}
\]

## 3. Matching lower bounds

We give a common population which supplies both lower bounds.  Choose the
fixed \(\kappa>0\) in Lemma 1.2 sufficiently small that Lemma 1.1 also
gives

\[
 A_{L-1}(n)\le {1\over2}C_n                         \tag{3.1}
\]

whenever \(m/3\le n\le2m/3\), where
\(L=\lfloor\kappa\sqrt m\rfloor\).  This is possible because the
right side of (1.3) is \(C\exp(-c/\kappa^2)\).

For each

\[
 \lceil m/3\rceil\le j\le\lfloor m/2\rfloor,
 \qquad n=m-j-1,
\]

choose

\[
 E\in\mathcal D_n,
 \quad \operatorname{ht}(E)\ge L,
 \qquad
 S\in\mathcal D_j,
 \quad \operatorname{ht}(S)\le L-1,
\]

and form

\[
 D=1E0S.                                             \tag{3.2}
\]

The first primitive component has height at least \(L+1\), while the
suffix has height at most \(L-1\).  It is therefore the first component
attaining the global height, and the canonical suffix in (3.2) is exactly
\(S\).  Thus

\[
 c(D)=2j+1\ge {2m\over3}.                            \tag{3.3}
\]

The construction is injective.  Equations (1.11) and (3.1) give at least

\[
 c C_{m-j-1}C_j                                      \tag{3.4}
\]

such words for each \(j\).  Both indices in (3.4) are comparable to
\(m\), and their sum is \(m-1\).  Hence (1.1) gives

\[
 C_{m-j-1}C_j\ge c{B_m\over m^{3/2}}.               \tag{3.5}
\]

There are \(\Theta(m)\) permitted values of \(j\), and different \(j\)'s
give different canonical suffix lengths.  Therefore

\[
 \#\{D\in\mathcal D_m:c(D)\ge2m/3\}
 \ge c{B_m\over\sqrt m}.                            \tag{3.6}
\]

Multiplying (3.6) respectively by \(2m/3\) and \((2m/3)^2\) yields

\[
 M_1(m)\ge c\sqrt m\,B_m,                           \tag{3.7}
\]

and

\[
 M_2(m)\ge c m^{3/2}B_m.                            \tag{3.8}
\]

Together with (1.1) and (2.11), these prove (0.1)--(0.2).

## 4. Audit of the area identity

For a finite zero--one word \(W=w_1\cdots w_\ell\), put

\[
 \sigma(W)=\sum_{i=1}^{\ell}(2w_i-1),
 \qquad
 H_W(t)=\sum_{i=1}^{t}(2w_i-1),
\]

and define its pre-step height area by

\[
 \operatorname{ar}(W)=\sum_{t=0}^{\ell-1}H_W(t).
 \tag{4.1}
\]

For arbitrary words \(X,Y\), this convention has the exact concatenation
law

\[
 \operatorname{ar}(XY)
 =\operatorname{ar}(X)+\operatorname{ar}(Y)+|Y|\sigma(X).
 \tag{4.2}
\]

Let the global height of \(D=P1R0S\) be \(M\).  Then

\[
 \sigma(P)=M-1,
 \qquad \sigma(R)=1-M,
 \qquad \sigma(S)=0.
\]

Writing

\[
 a=|P|+1,
 \qquad b=|R|+1,
 \qquad c=|S|+1,
\]

repeated use of (4.2) gives

\[
 \operatorname{ar}(P1R0S)
 =\operatorname{ar}(P)+\operatorname{ar}(R)
  +\operatorname{ar}(S)+bM,                         \tag{4.3}
\]

whereas

\[
 \begin{aligned}
 \operatorname{ar}(S1P0R)
 &=\operatorname{ar}(S)+\operatorname{ar}(P)
   +\operatorname{ar}(R)\\
 &\quad +(a-1)+M+(b-1)(M-1)\\
 &=\operatorname{ar}(P)+\operatorname{ar}(R)
   +\operatorname{ar}(S)+bM+a-b.
 \end{aligned}                                      \tag{4.4}
\]

Since \(\tau D=S1P0R\), subtraction proves

\[
 \operatorname{ar}(\tau D)-\operatorname{ar}(D)=a-b.
\]

Finally, for every balanced word \(W\),

\[
 \sum_{t=1}^{|W|}H_W(t)-
 \sum_{t=0}^{|W|-1}H_W(t)
 =H_W(|W|)-H_W(0)=0.                                \tag{4.5}
\]

Thus the post-step convention gives exactly the same area on \(D\) and
\(\tau D\).  Including both endpoint heights also changes nothing, and
subtracting a word-length-dependent constant from every semilength-\(m\)
Dyck path preserves the difference.  This completes the convention audit.

## 5. Consequence for the Gaussian second-moment ledger

For an edge-disjoint quotient family of zero-winding intervals, Cauchy's
inequality gives

\[
 \sum_I{a(D_{s(I)})^2\over s(I)}\le M_2(m).
\]

Even if every selected endpoint obeyed the favorable bound
\(a(D_{s(I)})\ge\eta N\), at
\(H_A=\lceil A\sqrt m\rceil\) this would give only

\[
 |\mathcal P|
 \le {H_AM_2(m)\over\eta^2N^2}
 =O_{A,\eta}(B_m),                                  \tag{5.1}
\]

whereas the deck-reduced residence gate requires

\[
 o_A(B_m/N).
\]

Thus the exact second moment is larger than the scale needed for the gate
by a factor of order \(N\).  The missing input cannot be recovered by
sharpening the one-step marginal estimate: it must be a correlation or
clustering theorem for the actual iterates of the block rotation.
