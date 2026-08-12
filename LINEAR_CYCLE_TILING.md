# Explicit linear-code tiling by partial pair-flip cycles

This note removes the last existence theorem from Stage A.  For every
power-of-two half-length `ell`, the standard `2ell` pair-flip cycle tiles the
entire orientation cube `Q_ell` by translations.  Consequently every larger
orientation cube tiles by the same blocks, and the middle layer admits the
required partial-block factor at a prescribed depth
`H=Theta(sqrt(m log m))`.

The argument is elementary linear algebra over `F_2`.

## 1. The standard cycle is a linear-code transversal

Let

\[
 \ell=2^t,
 \qquad G=\mathbb F_2^\ell,
\]

and let `e_1,...,e_ell` be the standard basis.  Put

\[
 p_0=0,
 \qquad p_i=e_1+\cdots+e_i\quad(1\le i\le\ell).
\]

Thus `p_ell=1^ell`.  The vertex set of the standard partial pair-flip cycle
is

\[
 P_\ell={p_i:0\le i<\ell}
       \mathbin{\dot\cup}
       {p_\ell+p_i:0\le i<\ell}.                  \tag{1.1}
\]

It has `2ell=2^(t+1)` elements.

Let

\[
 U=\mathbb F_2^t\times\{0\}
 \subset\mathbb F_2^{t+1},
 \qquad v=(0,\ldots,0,1).
\]

Choose any enumeration

\[
 u_0,u_1,\ldots,u_{\ell-1}
\]

of `U` with `u_0=0`.  Define a linear map

\[
 \phi:G\longrightarrow\mathbb F_2^{t+1}              \tag{1.2}
\]

on the standard basis by

\[
 \begin{aligned}
  \phi(e_i)&=u_i+u_{i-1} &&(1\le i<\ell),\\
  \phi(e_\ell)&=v+u_{\ell-1}.
 \end{aligned}                                         \tag{1.3}
\]

### Theorem 1 (cycle-transversal theorem)

The restriction of `phi` to `P_ell` is a bijection onto
`F_2^(t+1)`.  Hence, with

\[
 K=\ker\phi,
\]

the translated cycles

\[
 \boxed{\{P_\ell+k:k\in K\}}                         \tag{1.4}
\]

partition `F_2^ell`.

#### Proof

Telescoping (1.3) gives

\[
 \phi(p_i)=u_i\quad(0\le i<\ell),
 \qquad \phi(p_\ell)=v.                              \tag{1.5}
\]

Therefore

\[
 \phi(p_\ell+p_i)=v+u_i.
\]

The two halves of (1.1) map respectively to the two cosets `U` and `v+U`,
which partition `F_2^(t+1)`.  Thus `phi|P_ell` is bijective and `phi` is
surjective.

If

\[
 p+k=p'+k',\qquad p,p'\in P_\ell,\ k,k'\in K,
\]

then applying `phi` gives `phi(p)=phi(p')`, so `p=p'` and then `k=k'`.
Thus the translates in (1.4) are disjoint.  Their total size is

\[
 |K|\,|P_\ell|
 =2^{\ell-(t+1)}2^{t+1}=2^\ell,
\]

so they cover the cube.  QED.

Every translate is an isometric copy of the same cycle, with the same cyclic
coordinate-flip order.  Translation merely reverses the chosen orientation
of some active coordinate pairs.

### Corollary 2 (all larger cubes)

For every `s>=ell`, `Q_s` partitions explicitly into isometric copies of
`P_ell`.

#### Proof

Write

\[
 \mathbb F_2^s=\mathbb F_2^\ell\times\mathbb F_2^{s-\ell}.
\]

For every fixed second coordinate `y`, use the tiling

\[
 \{(P_\ell+k)\times\{y\}:k\in K\}.
\]

QED.

No asymptotic matching theorem and no nonconstructive cube-tiling theorem is
needed.

## 2. Explicit prescribed-scale middle factor

Fix a perfect matching of the `2m` original coordinates.  As in
`MIDDLE_BLOCK_FACTOR.md`, middle masks split into orientation-cube strata
`Q_s`, where `s` is the number of split coordinate pairs.  Apply Corollary 2
to every stratum with `s>=ell`.  The resulting blocks are genuine partial
pair-flip blocks in the original middle layer: fixed full pairs and fixed
orientations outside the active `ell` coordinates form the block core.

Only strata with `s<ell` remain.  Their total number of middle masks is at
most

\[
 U_{m,\ell}
 \le 2^m\sum_{s<\ell}\binom ms.                    \tag{2.1}
\]

If

\[
 \ell=o(m),\qquad \ell\log m=o(m),                 \tag{2.2}
\]

then

\[
 U_{m,\ell}=2^{-m+o(m)}W=o(W),
 \qquad W=\binom{2m}{m}.                            \tag{2.3}
\]

Indeed,

\[
 \sum_{s<\ell}\binom ms
 \le \ell\left(\frac{em}{\ell}\right)^\ell
 =\exp(o(m)),
\]

whereas `W=Theta(4^m/sqrt(m))`.

Now take, for example,

\[
 H=(1+\varepsilon)\sqrt{m\log m}                  \tag{2.4}
\]

and choose a power of two `ell` with

\[
 m^{3/4}\le\ell<2m^{3/4}.                          \tag{2.5}
\]

Then

\[
 H/\ell\to0,
 \qquad \ell\log m=o(m),                          \tag{2.6}
\]

and even `H U_(m,ell)=o(W)`.

### Theorem 3 (prescribed-depth Stage A)

For the choices (2.4)--(2.5), all but `o(W/H)` middle masks partition
explicitly into partial pair-flip cycles of length `2ell`.  Concatenating the
cycles, copying their first `H` states, and adding constant run pads costs

\[
 O\left(\frac{HW}{\ell}\right)+O(HU_{m,\ell})=o(W). \tag{2.7}
\]

The resulting middle row has length `W+o(W)`, contains every middle mask, has
no internal coordinate one-run shorter than `H+1`, and preserves every
designated cyclic block window through depth `H`.

#### Proof

The tiling and omission bound are (2.1)--(2.6).  Each selected block contains
`2ell` middle masks, so there are at most `W/(2ell)` seams.  The standard
prefix and endpoint padding uses `O(H)` extra states per seam, giving the
first term of (2.7).  Repair an omitted middle mask by `H+1` constant copies,
giving the second term.  Lemma 1 of `PARTIAL_BLOCK_PACKING.md` proves the run
and geodesic-window claims.  QED.

This closes Stage A at the full literal-tail depth.  The remaining issue is
solely Stage B: coordinate the choice of cycle tilings (or augment them) so
that their lower and upper consecutive shadows cover all but `o(W)` masks in
total.

## 3. Freedom left for Stage B

The enumeration `u_0,...,u_(ell-1)` in Theorem 1 is arbitrary.  Different
enumerations give different kernels and hence different cycle tilings.
One may also choose, independently in every orientation stratum,

* which `ell` split coordinates form the tiled factor;
* a permutation of those active coordinates;
* coordinate complements; and
* a linear-code transversal as above.

This is substantial structured freedom for resolving the shadow projections.
The next theorem should exploit it rather than return to an unstructured
global block nibble.
