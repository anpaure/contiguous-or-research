# The entrance-coupled promotion ring: exact degree-two columns and absence of a linear character gap

Date: 2026-07-26

Method: pure mathematics only.  Every column below is an actual cyclic
frame on one top.  The middle and entrance rows are never decoupled.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad q=\lceil m^{1/4}\rceil,
 \qquad r=m-q,
\tag{0.1}
\]

where

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 R=\binom nM,\qquad T=MR=W+o(W),
 \qquad W=\binom nm.
\tag{0.2}
\]

For each top \(U\in\binom{[n]}M\), choose one oriented cyclic frame
\(\pi_U\).  Let \(a\) be the load of the cyclic \(m\)-intervals and
\(b\) the load of the cyclic \(r\)-intervals of those same frames.

This note settles the first nonconstant sector beyond the already frozen
degree-zero and degree-one sectors.

1.  If \(h=(h_{xy})\) is a degree-two harmonic pair array and
    \(H_kh(Q)=\sum_{\{x,y\}\subset Q}h_{xy}\) is its rank-\(k\)
    Johnson lift, then the contribution of the actual frame selection is
    exactly

    \[
    \langle a,H_mh\rangle
      =\sum_U\sum_{\{x,y\}\subset U}
        h_{xy}(H-d_{\pi_U}(x,y))_+,
    \tag{0.3}
    \]

    \[
    \langle b,H_rh\rangle
      =\sum_U\sum_{\{x,y\}\subset U}
        h_{xy}(H+q-d_{\pi_U}(x,y))_+.
    \tag{0.4}
    \]

    Here \(d_{\pi_U}\) is undirected cyclic distance.  Thus the first
    coupled chronology shell is literally

    \[
    (H+q-d)_+-(H-d)_+.
    \tag{0.5}
    \]

2.  On one frame, the autocorrelation kernel
    \(K_L(s)=(L-d(s))_+\), including its diagonal value \(K_L(0)=L\),
    has symbol

    \[
    \widehat K_L(t)
       =\left|\sum_{j=0}^{L-1}e^{2\pi i tj/M}\right|^2
       =\frac{\sin^2(\pi tL/M)}{\sin^2(\pi t/M)}
       \quad(t\ne0).
    \tag{0.6}
    \]

    The actual off-diagonal, degree-two-centered pair kernel has instead

    \[
    \boxed{\Lambda_L(t)=
      \frac{\sin^2(\pi tL/M)}{\sin^2(\pi t/M)}
      -L+\frac{L(L-1)}{M-1}}
      \qquad(t\ne0).
    \tag{0.6a}
    \]

    In particular the first cyclic character has entrance/middle ratio

    \[
    \frac{\Lambda_{H+q}(1)}{\Lambda_H(1)}
      =1+\frac{2q}{H}
       +O\left(\frac{q^2}{H^2}+\frac1H+\frac{H^2}{M^2}\right)
      =1+o(1).
    \tag{0.7}
    \]

    It has the same sign on the two rows and supplies no one-sided
    entrance-versus-middle character.

3.  More strongly, there is an **integral one-frame-per-top selection**
    for which, simultaneously for every normalized degree-two Johnson
    character \(\phi\) on either target rank,

    \[
    \left|\langle a-TW^{-1}{\bf1},\phi\rangle\right|
       =O(Wm^{-3}),
    \qquad
    \left|\langle b-TN^{-1}{\bf1},\phi\rangle\right|
       =O(Wm^{-3}),
    \tag{0.8}
    \]

    where \(N=\binom nr\) and normalization means
    \(\|\phi\|_\infty\le1\).  The same integral selection is used in
    both displays.

Consequently the projection of the integral frame-column set onto the
coupled degree-two Johnson sector comes within \(o(W)\) of the uniform
fractional point.  Hence no bounded linear separating inequality with an
\(\Omega(W)\) gap can live purely in degree two, nor in the first cyclic
chronology shell (0.5).  This conclusion is about the exact integral
column set, not about detached slot tables.

This does **not** prove the desired \(o(W)\) collision/hole rounding.
Coverage is nonlinear: an integral selection can have all degree-two
moments balanced while retaining a positive-density Poisson hole set.
The remaining obstruction, if one exists, must use a nonlinear
coverage/character coupling, higher Johnson degree, or finite-character
holonomy rather than a linear degree-two character.

## 1. Harmonic pair arrays and their normalization

Let \(\mathcal H_2\) be the space of symmetric arrays
\(h=(h_{xy})_{\{x,y\}\in\binom{[n]}2}\) satisfying

\[
                    \sum_{y\ne x}h_{xy}=0
                    \qquad(x\in[n]).
\tag{1.1}
\]

Then automatically

\[
                         \sum_{\{x,y\}}h_{xy}=0.
\tag{1.2}
\]

For \(2\le k\le n-2\), define its rank-\(k\) lift by

\[
                   (H_kh)(Q)=\sum_{\{x,y\}\subset Q}h_{xy}.
\tag{1.3}
\]

These lifts are exactly the degree-two Johnson eigenspace on the
rank-\(k\) slice.

### Lemma 1.1 (sup-norm inversion)

For \(h\in\mathcal H_2\) and \(2\le k\le n-2\),

\[
                       \boxed{\|h\|_\infty
                              \le4\|H_kh\|_\infty.}
\tag{1.4}
\]

#### Proof

Fix distinct \(i,j,a,b\).  Choose any \((k-2)\)-set \(Q\) disjoint
from these four coordinates.  The four-set difference

\[
\begin{aligned}
 &(H_kh)(Qij)+(H_kh)(Qab)\\
 &\hspace{25mm}-(H_kh)(Qia)-(H_kh)(Qjb)
   =h_{ij}+h_{ab}-h_{ia}-h_{jb}
\end{aligned}
\tag{1.5}
\]

has absolute value at most \(4\|H_kh\|_\infty\).  The right side is
independent of the auxiliary set \(Q\).

Now fix \(i,j\), put \(V=[n]\setminus\{i,j\}\), and sum the right side
of (1.5) over ordered pairs \((a,b)\in V^2\), \(a\ne b\).  Harmonicity
gives

\[
 \sum_{a\in V}h_{ia}=\sum_{a\in V}h_{ja}=-h_{ij},
 \qquad
 \sum_{\{a,b\}\subset V}h_{ab}=h_{ij}.
\tag{1.6}
\]

Therefore the sum is

\[
                    (n-2)(n-1)h_{ij}.
\tag{1.7}
\]

Divide by the number \((n-2)(n-3)\) of ordered pairs only after noting
that (1.7), rather than that number, is the coefficient of \(h_{ij}\):
the triangle terms in (1.6) supply the missing \(2(n-2)h_{ij}\).
Since every summand has absolute value at most
\(4\|H_kh\|_\infty\), (1.7) yields

\[
 |h_{ij}|\le
 4\frac{n-3}{n-1}\|H_kh\|_\infty
 \le4\|H_kh\|_\infty.
\]

This proves (1.4). \(\square\)

### Lemma 1.2 (centering)

For every \(h\in\mathcal H_2\),

\[
                       \sum_{Q\in\binom{[n]}k}(H_kh)(Q)=0.
\tag{1.8}
\]

#### Proof

Every pair occurs in \(\binom{n-2}{k-2}\) rank-\(k\) sets, so (1.8)
is that constant times (1.2). \(\square\)

Thus subtracting a uniform target load never changes a degree-two
pairing.

## 2. The exact degree-two column

Fix a cyclic frame \(\pi\) on an \(M\)-set.  For two distinct positions
at undirected cyclic distance \(d\le M/2\), let
\(c_{k,M}(d)\) be the number of cyclic \(k\)-intervals containing both.

### Lemma 2.1 (complementary-arc kernel)

If \(k=M-L\) and \(1\le L<M/2\), then

\[
                 \boxed{c_{M-L,M}(d)=M-2L+(L-d)_+.}
\tag{2.1}
\]

#### Proof

Choose one of the two directed separations to be \(s\), so the other is
\(M-s\).  The common starts of two length-\(k\) intervals are counted by

\[
                    (k-s)_+ +(k-(M-s))_+.
\tag{2.2}
\]

Replacing \(s\) by \(d=\min(s,M-s)\), and using \(k=M-L>M/2\), gives
\(M-L-d\) when \(d\le L\), and \(M-2L\) when \(d>L\).  This is
(2.1). \(\square\)

### Theorem 2.2 (actual-frame harmonic formula)

Let \(F=(\pi_U)_{U\in\binom{[n]}M}\) be any integral frame selection.
For \(L\in\{H,H+q\}\), let \(\ell_{M-L}^F\) be the load vector of all
cyclic \((M-L)\)-intervals.  Then for every \(h\in\mathcal H_2\),

\[
 \boxed{
 \left\langle\ell_{M-L}^F,H_{M-L}h\right\rangle
   =\sum_U\sum_{\{x,y\}\subset U}
       h_{xy}(L-d_{\pi_U}(x,y))_+.}
\tag{2.3}
\]

#### Proof

Interchange the target-interval and pair sums.  Lemma 2.1 gives

\[
\begin{aligned}
 \left\langle\ell_{M-L}^F,H_{M-L}h\right\rangle
 &= (M-2L)\sum_U\sum_{\{x,y\}\subset U}h_{xy}\\
 &\quad+\sum_U\sum_{\{x,y\}\subset U}
      h_{xy}(L-d_{\pi_U}(x,y))_+.
\end{aligned}
\tag{2.4}
\]

Every pair lies in exactly \(\binom{n-2}{M-2}\) tops.  The first line
of (2.4) is therefore

\[
 (M-2L)\binom{n-2}{M-2}\sum_{\{x,y\}}h_{xy}=0
\]

by (1.2). \(\square\)

Taking \(L=H\) gives (0.3), while \(L=H+q\) gives (0.4).  Subtracting
them gives the exact chronology shell

\[
 \sum_U\sum_{\{x,y\}\subset U}h_{xy}J_{H,q}(d_{\pi_U}(x,y)),
\tag{2.5}
\]

where

\[
 J_{H,q}(d)=
 \begin{cases}
 q,&d\le H,\\
 H+q-d,&H<d<H+q,\\
 0,&d\ge H+q.
 \end{cases}
\tag{2.6}
\]

For a uniformly placed labelled pair, the directed separation is uniform
on \(\{1,\ldots,M-1\}\).  Hence the exact centered shell is

\[
 \widetilde J_{H,q}(d)=J_{H,q}(d)-
        \frac{q(2H+q-1)}{M-1},
\tag{2.7}
\]

and its exact one-pair variance is

\[
 \boxed{
 \frac{2Hq^2+q(q-1)(2q-1)/3}{M-1}
 -\left(\frac{q(2H+q-1)}{M-1}\right)^2
 =(2+o(1))\frac{Hq^2}{m}.}
\tag{2.8}
\]

Indeed there are two directed separations at each undirected distance;
the shell has value \(q\) at distances \(1,\ldots,H\), followed by
\(q-1,\ldots,1\).  This also checks directly that the shell is not a
conserved local character.

No detached entrance table has been introduced: (2.3) is evaluated on
the same frame that supplies the middle intervals.

## 3. The local cyclic Fourier character

Write \(\omega=e^{2\pi i/M}\).  On \(\mathbb Z_M\), first include the
diagonal value and put

\[
                     K_L(s)=(L-d(0,s))_+.
\tag{3.1}
\]

This is the cyclic autocorrelation of the indicator of
\(\{0,1,\ldots,L-1\}\).  Hence its discrete Fourier transform is

\[
 \widehat K_L(t)
 =\left|\sum_{j=0}^{L-1}\omega^{tj}\right|^2.
\tag{3.2}
\]

For \(t\ne0\), the geometric sum proves (0.6).  There are two corrections
before this becomes the actual Johnson degree-two pair kernel.  First,
pairs are off-diagonal, so deleting \(K_L(0)=L\) subtracts \(L\) from
every Fourier eigenvalue.  Second, the mean off-diagonal value is

\[
                         c_L=\frac{L(L-1)}{M-1}.
\tag{3.2a}
\]

Subtracting \(c_L\) from every off-diagonal entry makes every row sum
zero.  At a nonzero frequency, the off-diagonal constant matrix has
eigenvalue \(-c_L\), so this centering adds \(c_L\).  The exact centered
symbol is therefore (0.6a).

This centering does not alter the global character in Theorem 2.2:
summed over all tops, its added term is a constant multiple of
\(\sum_{\{x,y\}}h_{xy}=0\).  Formula (0.6), by itself, is only the
diagonal-included autocorrelation symbol; formula (0.6a) is the literal
degree-two symbol.

For \(t=1\), Taylor's formula \(\sin x=x(1+O(x^2))\) gives

\[
\begin{aligned}
 \frac{\Lambda_{H+q}(1)}{\Lambda_H(1)}
 &=\frac{(H+q)^2}{H^2}
   \left(1+O\left(\frac1H+\frac{H^2}{M^2}\right)\right)\\
 &=1+\frac{2q}{H}
   +O\left(\frac{q^2}{H^2}+\frac1H+\frac{H^2}{M^2}\right).
\end{aligned}
\tag{3.3}
\]

At the tuned scales, \(q/H\to0\) and \(H/M\to0\), proving (0.7).
The first centered symbols are positive for large \(m\), and their ratio
tends to one.  There is no anti-invariant **first** Fourier sign waiting
to separate the two target rows.  The centered symbols (0.6a) can have
either sign at high resonant frequencies, and their ratios need not be
close to one; the next section avoids assuming such a false uniform
comparison.

## 4. Integral simultaneous balancing of all degree-two characters

For a pair \(p=\{x,y\}\) and \(L\in\{H,H+q\}\), define

\[
 Z_L^F(p)=
 \sum_{U\supset p}(L-d_{\pi_U}(x,y))_+.
\tag{4.1}
\]

Let

\[
                         R_2=\binom{n-2}{M-2}.
\tag{4.2}
\]

### Lemma 4.1 (exact pair expectation)

If each \(\pi_U\) is chosen independently and uniformly, then

\[
                    \boxed{\mathbb EZ_L^F(p)
                     =\mu_L:=R_2\frac{L(L-1)}{M-1}.}
\tag{4.3}
\]

The value is independent of \(p\).

#### Proof

In a uniform cyclic frame containing a prescribed labelled pair, its
directed separation is uniform on \(\{1,\ldots,M-1\}\).  Since
\(L<M/2\), each undirected distance \(d=1,\ldots,L-1\) occurs twice.
Therefore

\[
 \mathbb E(L-d)_+
   =\frac2{M-1}\sum_{d=1}^{L-1}(L-d)
   =\frac{L(L-1)}{M-1}.
\]

There are \(R_2\) tops containing the pair. \(\square\)

### Theorem 4.2 (integral pair-kernel balancing)

For all sufficiently large \(m\), there is an integral actual-frame
selection \(F\) such that, simultaneously for both
\(L=H,H+q\) and all \(p\in\binom{[n]}2\),

\[
                  \boxed{|Z_L^F(p)-\mu_L|\le Wm^{-5}.}
\tag{4.4}
\]

#### Proof

Use the independent uniform choice from Lemma 4.1.  For a fixed
\((L,p)\), the summands in (4.1) are independent, lie in \([0,L]\),
and have total variance at most \(R_2L^2\).  Bernstein's inequality gives

\[
 \Pr\{|Z_L^F(p)-\mu_L|>t\}
 \le2\exp\left(
 -\frac{t^2}{2R_2L^2+(2/3)Lt}
 \right).
\tag{4.5}
\]

The tuned capacity relation implies

\[
 R=(1+o(1))\frac Wm,qquad
 R_2=R\frac{M(M-1)}{n(n-1)}=\Theta(W/m).
\tag{4.6}
\]

Moreover \(L=O(\sqrt{m\log m})\).  With \(t=Wm^{-5}\), the exponent
in (4.5) is at least

\[
 \min\left\{
  \frac{W}{O(m^{10}\log m)},
  \frac{W}{O(m^5\sqrt{m\log m})}
 \right\},
\tag{4.7}
\]

which tends to infinity faster than every power of \(m\).  There are
fewer than \(2n^2\) events.  Their union has probability less than one,
so an integral outcome satisfying (4.4) exists. \(\square\)

### Theorem 4.3 (the coupled degree-two projection is \(o(W)\))

For the integral selection supplied by Theorem 4.2, let

\[
 \theta_m=T/W,\qquad \theta_r=T/N,
 \qquad N=\binom nr.
\tag{4.8}
\]

Then

\[
 \sup_{\substack{\phi\in E_2(m)\\\|\phi\|_\infty\le1}}
 |\langle a-\theta_m{\bf1},\phi\rangle|
 \le 2n^2Wm^{-5}=O(Wm^{-3}),
\tag{4.9}
\]

and

\[
 \sup_{\substack{\psi\in E_2(r)\\\|\psi\|_\infty\le1}}
 |\langle b-\theta_r{\bf1},\psi\rangle|
 \le 2n^2Wm^{-5}=O(Wm^{-3}).
\tag{4.10}
\]

Here \(E_2(k)\) denotes the degree-two Johnson eigenspace on rank \(k\).

#### Proof

Write \(\phi=H_mh\), where \(h\in\mathcal H_2\).  Lemma 1.1 gives
\(\|h\|_\infty\le4\).  Lemma 1.2 deletes the uniform term, and
Theorem 2.2 gives

\[
 \langle a-\theta_m{\bf1},\phi\rangle
  =\sum_ph_pZ_H^F(p)
  =\sum_ph_p(Z_H^F(p)-\mu_H),
\tag{4.11}
\]

because \(\sum_ph_p=0\).  By (4.4), its absolute value is at most

\[
 4\binom n2Wm^{-5}\le2n^2Wm^{-5}.
\]

This proves (4.9).  The proof of (4.10) is identical with \(L=H+q\).
\(\square\)

For any normalized pair \((\phi,\psi)\in E_2(m)\oplus E_2(r)\), the
absolute value of the corresponding coupled two-row functional is
therefore \(O(Wm^{-3})=o(W)\).  This is precisely the dual-norm statement
that the uniform coupled target lies within \(o(W)\) of the projection
of an integral actual-frame point.

## 5. Exact proved boundary

The preceding theorem rules out the proposed first higher-character
obstruction in its linear form:

* degree zero is only the scalar surplus;
* degree one is frozen exactly by coordinate census;
* degree two, including the first complementary-arc chronology shell,
  can be balanced to \(o(W)\) by one integral actual-frame selection.

There is also a simple necessary-side check.  If an integral selection
has coupled deficiency

\[
 \Delta(F)=T-W+o(W),
\tag{5.1}
\]

then its middle load is \(o(W)\) away from \({\bf1}\) in \(\ell^1\),
and its entrance load is likewise \(o(W)\) away from \({\bf1}\): indeed,

\[
 \|a-\mathbf1\|_1
 =2\sum_X(a_X-1)_+-(T-W)=o(W),
\tag{5.2}
\]

while integrality of \(b\) gives

\[
 \|b-\mathbf1\|_1
 =(T-N)+2\#\{S:b_S=0\}=o(W).
\tag{5.3}
\]

Thus every bounded character, of every degree, is automatically
\(o(W)\) on a successful rounding.  A useful character obstruction must
therefore prove that some character magnitude is forced to be
\(\Omega(W)\) for every integral frame selection.  Theorem 4.3 proves
that this is false throughout the coupled degree-two sector.

What remains open is not another linear degree-two calculation.  It is
one of the following genuinely stronger statements:

1. a nonlinear inequality coupling degree-two mass to the zero sets of
   the two load vectors;
2. a higher-degree or modular holonomy forced on every integral global
   selection; or
3. a dependent cyclic-frame rounding which directly controls coverage.

No coefficient-one conclusion is claimed here.
