# Factorial overlap bound for domino-twin superpackets

Date: 2026-07-27

## 0. Theorem

Use the labelled domino-twin superpacket catalogue with

\[
 n=2m,\qquad R=m-q_0,\qquad q_0=a\sqrt m+O(1),
\]

on the parity subsequence \(R\) odd. Let

\[
 K=2n,\qquad D_{\rm lab}=2nR!(n-R)!
\]

be its edge size and labelled vertex degree.  Collapse parallel labelled
copies and write \(D=D_{\rm lab}/M\) for the resulting simple degree;
the multiplicity \(M\) is uniform by relabelling transitivity.  Every
relative cluster codegree is unchanged by this collapse.  Then for every
fixed \(C_0>0\) there
is \(C=C(a,C_0)\) such that, uniformly for every entrance target \(X\),
every superpacket \(F\ni X\), and every
\[
 1\le p\le C_0\log m,
\]
one has

\[
 \boxed{
 \frac1D\sum_{\substack{F'\ni X\\F'\ne F}}
 (|F\cap F'|-1)_p
 \le (Cp)^{Cp}m^{-2}.}                                    \tag{0.1}
\]

Here parallel labelled copies of one support are collapsed, as they must be
for a simple matching catalogue.  All vertex degrees and cluster
codegrees are divided by the same (uniform) support multiplicity, so every
normalized estimate below is unchanged.  If labelled parallel copies are
retained instead, their diagonal term must be written separately.  In
particular, the fixed domino transpositions already give at least
\(2^{n/2}\) labels for one support, so a former claim that this term was
only polynomial was incorrect.

Consequently every static common-column diagram \(K_{2,\ell}\), for
\(\ell\le C_0\log m\), has the ACLE scale

\[
 \sum_{F,F'\ni X}c_X(F,F')^\ell
 \le(C\ell)^{C\ell}D^{\ell+2}.                            \tag{0.2}
\]

Thus the \(K_{2,5}\) gate isolated in the preceding audit is closed
statically. The unresolved issue is now dynamic: prove that an analogue of
(0.1), normalized by the current links, survives the stopped slow-bite
trajectory.

## 1. Factorial moments as cluster codegrees

Fix \(X\in F\), and put
\[
 r(F,F')=|F\cap F'|-1.
\]

For an integer \(p\ge1\),
\[
 \boxed{
 \sum_{F'\ni X}(r(F,F'))_p
 =p!\sum_{\substack{C\subseteq F\setminus\{X\}\\|C|=p}}
 d^\square(\{X\}\cup C).}                                 \tag{1.1}
\]

Indeed, both sides count a packet \(F'\ni X\) and an ordered \(p\)-tuple
of further distinct members of \(F\cap F'\).

For a family \(\mathcal A\) of entrance targets, define its Johnson
diameter
\[
 \operatorname{diam}(\mathcal A)
 =\max_{A,B\in\mathcal A}\bigl(R-|A\cap B|\bigr).
\]

## 2. Two geometric inputs

### Lemma 2.1 (balls)

For \(1\le h\le R-2\), every Johnson ball of radius \(h\), intersected
with one twin superpacket, has at most
\[
 4h+2                                                   \tag{2.1}
\]
vertices.

This is the exact ball lemma from the degree audit: one component supplies
at most \(2h+1\) vertices and the other supplies at most \(2h+1\).

### Lemma 2.2 (diameter codegree)

If \(\mathcal A\) is contained in a twin superpacket and
\[
 1\le h=\operatorname{diam}(\mathcal A)\le R-1,
\]
then
\[
 \frac{d^\square(\mathcal A)}D
 \le\frac5{\binom Rh\binom{n-R}h}.                       \tag{2.2}
\]

If \(h=R\), then
\[
 \frac{d^\square(\mathcal A)}D
 \le\frac{2(n-2R)+1}{\binom{n-R}R}.                       \tag{2.3}
\]

#### Proof

Choose a pair in \(\mathcal A\) at distance \(h\). The degree of the whole
family is at most the pair codegree. Equations (2.2)--(2.3) are the exact
pair table for the twin catalogue. \(\square\)

### Lemma 2.3 (the diameter-one exceptions)

The Johnson-distance-one graph induced by one twin superpacket has clique
number four. A fixed vertex belongs to exactly six triangles and two
\(K_4\)'s in that graph.

The two triangle orbits have relative degrees
\[
 \frac6{R(n-R)(n-R-1)},\qquad
 \frac6{(n-R)R(R-1)},                                    \tag{2.4}
\]
and the two \(K_4\) orbits have relative degrees
\[
 \frac6{R(n-R)(n-R-1)(n-R-2)},\qquad
 \frac6{(n-R)R(R-1)(R-2)}.                               \tag{2.5}
\]

#### Proof

A clique in a Johnson graph is contained either in a star with a common
\((R-1)\)-core or in a top inside one \((R+1)\)-set. Each component cyclic
order contributes at most two members to either clique, so the twin has
clique number at most four; the canonical local patches attain four.

One twin contains \(2n\) star triangles, \(2n\) top triangles,
\(n/2\) star \(K_4\)'s, and \(n/2\) top \(K_4\)'s. Divide the resulting
incidence counts over the \(n!\) labelled columns by the numbers
\[
 \binom n{R-1}\binom{n-R+1}3,\quad
 \binom n{R+1}\binom{R+1}3,
\]
and their \(4\)-element analogues. Division by \(D\) gives
(2.4)--(2.5). The vertex-incidence counts are
\[
 \frac{3(4n)}{2n}=6,\qquad
 \frac{4n}{2n}=2.
\]
\(\square\)

## 3. Diameter summation

Fix \(p\), and partition the \(p\)-subsets \(C\subseteq F\setminus\{X\}\)
according to
\[
 h=\operatorname{diam}(\{X\}\cup C).
\]

For \(2\le h\le R-2\), Lemma 2.1 gives at most
\[
 \binom{4h+1}{p}                                          \tag{3.1}
\]
such subsets, because every member of \(C\) lies in the radius-\(h\)
ball around \(X\). Therefore Lemma 2.2 gives

\[
 \frac{p!}{D}
 \sum_{\substack{|C|=p\\\operatorname{diam}(\{X\}\cup C)=h}}
 d^\square(\{X\}\cup C)
 \le
 \frac{5p!\binom{4h+1}p}
      {\binom Rh\binom{n-R}h}.                            \tag{3.2}
\]

Since
\[
 p!\binom{4h+1}p\le(5h)^p,                               \tag{3.3}
\]
the right side is at most
\[
 5(5h)^p\left(\frac{h^2}{R(n-R)}\right)^h.                \tag{3.4}
\]

### Lemma 3.1 (small and central diameters)

Uniformly for \(p\le C_0\log m\),
\[
 \sum_{h=2}^{\lfloor R/2\rfloor}
 \frac{5p!\binom{4h+1}p}
      {\binom Rh\binom{n-R}h}
 \le (Cp)^{Cp}m^{-2}.                                     \tag{3.5}
\]

#### Proof

Fix a sufficiently large absolute constant \(A\).  For
\(2\le h\le Ap\), (3.4) gives
\[
 5(5h)^p\left(\frac{h^2}{R(n-R)}\right)^h
 \le (Cp)^{Cp}m^{-2h}.
\]
There are only \(O(p)\) terms in this range, and \(h\ge2\), so their
sum is at most \((Cp)^{Cp}m^{-4}\) after enlarging \(C\).

For \(Ap<h\le m^{1/3}\), the logarithm of (3.4) is at most
\[
 p\log(5h)-2h\log\frac mh+O(h).
\]
Here \(p<h/A\) and \(\log(m/h)\ge(2/3)\log m\).  Choosing \(A\)
large and then taking \(m\) large makes this at most \(-h\log m\).
Thus this entire range contributes \(O(m^{-3})\).

For \(m^{1/3}<h\le R/4\), the denominator in (3.2) is
\[
 \exp\!\left[\Omega\!\left(h\log\frac mh\right)\right],
\]
whereas its numerator is \(\exp[O(p\log h)]\).  Since
\(p\le C_0\log m\), this range contributes
\(\exp[-\Omega(m^{1/3})]\).

Finally, for \(R/4<h\le R/2\), both binomial coefficients in (3.2)
are exponential in \(m\), while the numerator is
\(\exp[O((\log m)^2)]\).  Combining the four ranges proves (3.5).
\(\square\)

### Lemma 3.2 (large diameters)

Uniformly for \(p\le C_0\log m\),
\[
 \sum_{h>R/2}
 \frac{p!}{D}
 \sum_{\substack{|C|=p\\\operatorname{diam}(\{X\}\cup C)=h}}
 d^\square(\{X\}\cup C)
 =\exp[-\Omega_a(\sqrt m\log m)].                         \tag{3.6}
\]

#### Proof

Use the crude count \((2n)^p=\exp[O((\log m)^2)]\) for all subsets.
For \(R/2<h\le R-2\), the product
\[
 \binom Rh\binom{n-R}h
\]
is minimized at an endpoint of this interval. At \(h=R-2\), its second
factor is
\[
 \binom{n-R}{R-2}
 =\binom{n-R}{2q_0+2}
 =\exp[\Omega_a(\sqrt m\log m)].
\]
At the other endpoint the factors are exponential in \(m\). The cases
\(h=R-1,R\) follow directly from (2.2)--(2.3) and have the same
superpolynomial margin. \(\square\)

## 4. Diameter one

For \(p=1\), the exact conditioned pair census gives
\[
 \frac1D\sum_{F'\ni X}r(F,F')
 =\frac{25}{R(n-R)}+O(m^{-4})=O(m^{-2}).                  \tag{4.1}
\]

For \(p=2\), diameter-one clusters are triangles. A fixed \(X\) belongs
to only six of them, and (2.4) gives total contribution \(O(m^{-3})\).

For \(p=3\), diameter-one clusters are \(K_4\)'s. A fixed \(X\) belongs
to only two, and (2.5) gives total contribution \(O(m^{-4})\).

For \(p\ge4\), a diameter-one cluster \(\{X\}\cup C\) would have at least
five vertices, impossible by Lemma 2.3.

Combining this paragraph with Lemmas 3.1--3.2 and identity (1.1) proves
(0.1).

## 5. Static ACLE consequence

Let
\[
 c_X(F,F')
 =|\{e\not\ni X:e\cap F\ne\varnothing,\
                    e\cap F'\ne\varnothing\}|.
\]
The elementary witness split gives
\[
 c_X(F,F')
 \le D(|F\cap F'|-1)+K^2\Delta_2^\square
 \le CD(1+r(F,F')).                                      \tag{5.1}
\]

For \(\ell\le C_0\log m\), expand
\[
 r^\ell=\sum_{p=1}^{\ell}S(\ell,p)(r)_p
\]
and apply (0.1). This yields
\[
 \sum_{F,F'\ni X}c_X(F,F')^\ell
 \le(C\ell)^{C\ell}D^{\ell+2},
\]
which is (0.2).

Hence every static \(K_{2,\ell}\) common-column core through logarithmic
order has the required factorial control. In particular, the former
\(K_{2,5}\) gap is closed.

The remaining step is not another static common-interval classification.
It is the stopped hereditary version: after earlier selected edges delete
most links, normalize (0.1) by the current degree \(d_t(X)\) and prove the
same bound for the surviving overlap distribution. The time-zero theorem
does not imply that dynamic statement for an arbitrary residual.
