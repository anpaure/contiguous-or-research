# A sub-width construction for both outer Boolean tails

This note gives a positive answer, in the asymptotic form actually needed, to
the truncated-ideal escape question.  A direct chain-product construction does
not have length `O(binomial(2m,m-h))` uniformly in `h`; its natural loss is
`1+h^2/m`.  That loss is harmless.  As soon as

\[
                 h^2/m\longrightarrow\infty
\]

slowly, the construction has length `o(binomial(2m,m))` and covers **both**
outer tails.  Consequently a near-width central construction need only resolve
a band whose half-width is `sqrt(m) omega(1)`, rather than
`Theta(sqrt(m log m))`.

## 1. The truncated chain-product word

Split the ground set into two disjoint `m`-sets

\[
                         X\mathbin{\dot\cup}Y=[2m].
\]

Fix symmetric-chain decompositions of `2^X` and `2^Y`.  A chain in either
half has the form

\[
 C=(C_c\subset C_{c+1}\subset\cdots\subset C_{m-c}),             \tag{1.1}
\]

where the subscript denotes rank.  If

\[
 C_{i}=C_{i-1}\mathbin{\dot\cup}\{e_i\},
\]

define

\[
 R(C)=[C_c]_{C_c\ne\varnothing},\{e_{c+1}\},\ldots,
       \{e_{m-c}\},
 \qquad L(C)=\operatorname{rev}R(C).                              \tag{1.2}
\]

The nonempty prefix unions of `R(C)`, and the nonempty suffix unions of
`L(C)`, are precisely the nonempty members of `C`.  The word length depends
only on the minimum rank:

\[
 w_c:=|R(C)|=
 \begin{cases}
 m,&c=0,\\
 m-2c+1,&c>0,
 \end{cases}
 \qquad w_c\le m-2c+1.                                            \tag{1.3}
\]

Put

\[
                         r=m-h.
\]

For every pair `(C,D)` of half-chains whose minimum ranks `c,d` satisfy

\[
                         c+d\le r,                                \tag{1.4}
\]

append the gadget

\[
                         L(C)\Vert R(D).                           \tag{1.5}
\]

The order of the gadgets is irrelevant.

### Theorem 1 (two-tail coverage)

The word (1.5), concatenated over (1.4), represents every nonempty set `S`
whose rank satisfies

\[
                    |S|\le m-h
                    \quad\hbox{or}\quad
                    |S|\ge m+h.                                  \tag{1.6}
\]

#### Proof

Write `S=S_X dotcup S_Y`, and let `C,D` be the unique half-chains containing
`S_X,S_Y`, with minimum ranks `c,d`.

If `|S|<=r`, then

\[
                         c+d\le |S_X|+|S_Y|\le r.
\]

Thus the pair is scheduled.  A suffix of `L(C)` has union `S_X`, and a prefix
of `R(D)` has union `S_Y`; taking the crossing interval gives `S`.  If one
part is empty, use only the appropriate one-sided interval.

Every member of a symmetric chain with minimum rank `c` has rank between
`c` and `m-c`.  Hence

\[
             c\le m-|S_X|,\qquad d\le m-|S_Y|.
\]

If `|S|>=2m-r=m+h`, it follows that

\[
 c+d\le 2m-|S_X|-|S_Y|=2m-|S|\le r.
\]

The same gadget therefore represents `S`.  QED.

The upper-tail conclusion is important: no complementation of OR witnesses
is being used.  It follows directly from the symmetric upper endpoints of the
same two chains.

## 2. Exact length

Let

\[
 a_c=\binom mc-\binom m{c-1},\qquad
 0\le c\le\lfloor m/2\rfloor,                                    \tag{2.1}
\]

where `binomial(m,-1)=0`.  There are `a_c` half-chains of minimum rank `c`,
and telescoping gives

\[
 \sum_{d=0}^{t}a_d
   =\binom mt\qquad(0\le t\le\lfloor m/2\rfloor).                \tag{2.2}
\]

By symmetry between the two halves, the exact word length is

\[
 \boxed{
 U(m,h)=2\sum_{c=0}^{\lfloor m/2\rfloor}
       a_cw_c\binom m{\min\{m-h-c,\lfloor m/2\rfloor\}}
 }                                                               \tag{2.3}
\]

with a binomial interpreted as zero if its lower index is negative.

## 3. Asymptotic estimate

For clarity assume `m` is even; changing floors in odd `m` changes only
absolute constants.  The following range is more than enough for the intended
application.

### Theorem 2 (truncated-product estimate)

Uniformly for

\[
                   \sqrt m\le h=o(m^{2/3}),                       \tag{3.1}
\]

one has

\[
 \boxed{
 U(m,h)=O\!\left(
       \left(1+\frac{h^2}{m}\right)\binom{2m}{m-h}
                 \right).
 }                                                               \tag{3.2}
\]

#### Proof

Write

\[
                         z=m/2-c.
\]

From (2.1) and (1.3),

\[
 a_cw_c
 \le \binom mc\frac{(m-2c+1)^2}{m-c+1}
 \le \frac{2(2z+1)^2}{m}\binom mc.                              \tag{3.3}
\]

First consider `c>m/2-h`, equivalently `z<h`.  Here the second binomial in
(2.3) is

\[
 \binom m{m-h-c}=\binom m{c+h}.                                  \tag{3.4}
\]

Vandermonde's identity gives

\[
 \sum_c\binom mc\binom m{c+h}=\binom{2m}{m-h}.                  \tag{3.5}
\]

After normalization, the summation variable in (3.5) has the hypergeometric
law obtained by taking `m-h` objects from two classes of size `m`.  Therefore

\[
 \mathbb E c=(m-h)/2,
 \qquad
 \operatorname{Var}(c)le m/8+O(1),
\]

and consequently

\[
 \mathbb E(m/2-c)^2=O(m+h^2).                                   \tag{3.6}
\]

Equations (3.3)--(3.6) show that this part of (2.3) is at most the right side
of (3.2).

It remains to handle `c<=m/2-h`, or `z>=h`.  In this range the second
binomial in (2.3) is the central coefficient `binomial(m,m/2)`.  Standard
successive-ratio bounds for binomial coefficients give, for `h>=sqrt(m)`,

\[
 \sum_{z\ge h}\frac{(2z+1)^2}{m}
       \binom m{m/2-z}
   =O\!\left(h\binom m{m/2-h}\right).                            \tag{3.7}
\]

For completeness, divide the summand by its value at `z=h`.  The ratio after
`t` further steps is at most `exp(-2ht/m)`; summing the resulting geometric
moments of `(h+t)^2/m` proves (3.7).

Thus the remaining contribution is

\[
 O\!\left(
 h\binom m{m/2}\binom m{m/2-h}
 \right).                                                        \tag{3.8}
\]

The usual uniform central-binomial estimates in the range (3.1) give

\[
 \binom m{m/2}=\Theta(2^m/\sqrt m),
\quad
 \binom m{m/2-h}=\Theta\!\left(
       \frac{2^m}{\sqrt m}e^{-2h^2/m+o(1)}\right),
\]

and

\[
 \binom{2m}{m-h}=\Theta\!\left(
       \frac{4^m}{\sqrt m}e^{-h^2/m+o(1)}\right).                \tag{3.9}
\]

The ratio of (3.8) to the last expression in (3.9) is

\[
 O\!\left(\frac h{\sqrt m}e^{-h^2/m+o(1)}\right)=O(1).          \tag{3.10}
\]

This proves (3.2).  QED.

## 4. Consequence for the universal-OR program

Let `omega=omega(m)` tend to infinity arbitrarily slowly, subject for example
to `omega=o(m^(1/3))`, and take

\[
                         h=\left\lceil\sqrt{m\omega}\right\rceil.
                                                                        \tag{4.1}
\]

Writing `W=binomial(2m,m)`, (3.2) and the moderate-deviation estimate give

\[
 \frac{U(m,h)}W
   =O\!\left((1+\omega)e^{-\omega+o(1)}\right)=o(1).             \tag{4.2}
\]

Hence:

### Corollary 3

There is an explicit OR word of length `o(W)` which represents every mask
outside the open central band

\[
                         m-h<|S|<m+h.                             \tag{4.3}
\]

Therefore a construction of length `W+o(W)` for just the band (4.3), with
`h/sqrt(m)->infinity` arbitrarily slowly, already implies

\[
                         \nu(2m)=(1+o(1))W.                       \tag{4.4}
\]

The previous literal-tail strategy required `h=Theta(sqrt(m log m))`.
The chain-product tail compressor lowers this to

\[
                         h=\sqrt m\,\omega(1),                   \tag{4.5}
\]

which is the natural moderate-deviation threshold.  Any further central-row
argument should use (4.5), not pay for literal outer masks.

## 5. Comparison with `TRUNCATED_TAIL_CONSTRUCTION.md`

The two notes prove the same asymptotic escape, but the words are not
identical.

The Euler construction in `TRUNCATED_TAIL_CONSTRUCTION.md` uses the
two-direction connector

\[
 \omega(C)=[C_c]_{c>0},\{e_{c+1}\},\ldots,\{e_{m-c}\},
             [X\setminus C_{m-c}]_{c>0}.                         \tag{5.1}
\]

Its prefix unions give `C` and its suffix unions give the complement-dual
chain `C^*`.  Thus its connector length is

\[
 \widehat w_c=
 \begin{cases}
 m,&c=0,\\
 m-2c+2,&c>0.
 \end{cases}                                                     \tag{5.2}
\]

After cutting its Euler circuit, that note obtains

\[
 \widehat U(m,h)
 \le 2\sum_c a_c\widehat w_c C_m(m-h-c)+m.                       \tag{5.3}
\]

Here `C_m(t)=binomial(m,min(t,floor(m/2)))`, with value zero for `t<0`.

The present note does not need complement-dual suffixes.  It writes one
gadget `L(C)||R(D)` for each **undirected** compatible pair and uses the
chains containing the two target halves themselves.  Hence it omits the last
term of (5.1), has

\[
 w_c=
 \begin{cases}
 m,&c=0,\\
 m-2c+1,&c>0,
 \end{cases}                                                     \tag{5.4}
\]

and needs no cyclic cut duplication.  Its exact length is therefore

\[
 U(m,h)=2\sum_c a_cw_c C_m(m-h-c).                               \tag{5.5}
\]

In particular,

\[
 \widehat U(m,h)-U(m,h)
 \le 2\sum_{c>0}a_cC_m(m-h-c)+m,                                \tag{5.6}
\]

with equality if the Euler bound (5.3) is attained.  There is no
off-by-one disagreement: the extra `+1` in (5.2) is exactly the nonempty
terminal complement block, and the final `+m` is exactly the linearization
cost.

Both formulas have the same leading asymptotics.  Writing `h=c sqrt(m)`, the
more detailed estimate in the Euler note is

\[
 O\!\left((1+c^2)\binom{2m}{m-h}
       +c e^{-2c^2}\binom{2m}{m}\right).                         \tag{5.7}
\]

The second term is at most a constant times the first, because

\[
 \binom{2m}{m-h}/\binom{2m}{m}=e^{-c^2+o(1)},
 \qquad c e^{-c^2}=O(1).                                        \tag{5.8}
\]

Thus (5.7) and the simpler bound (3.2) are asymptotically consistent.
