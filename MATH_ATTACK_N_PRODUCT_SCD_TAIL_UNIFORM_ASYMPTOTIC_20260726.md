# Uniform product-SCD tail asymptotics and the exact odd lift

Date: 2026-07-26

## 1. Statement

Put

\[
 h_m=\lfloor m/2\rfloor,
 \qquad \epsilon_m=m-2h_m\in\{0,1\},
 \qquad M_m=\binom m{h_m},
 \qquad W_{2m}=\binom{2m}m.
\]

For \(0\le a\le h_m\), define

\[
 A_m(a)=\binom ma-\binom m{a-1},
 \qquad
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+1,&a>0,
 \end{cases}
\]

and

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\
 \displaystyle\binom m{\min(t,h_m)},&t\ge0.
 \end{cases}
\]

The exact length of the standard product-SCD word for the two tails of
\(Q_{2m}\) is

\[
 \boxed{
 L_m(r)=2\sum_{a=0}^{h_m}A_m(a)w_m(a)C_m(r-a).}
 \tag{1.1}
\]

The word represents every nonempty set of rank at most \(r\) and every set
of rank at least \(2m-r\). The leading factor \(2\) in (1.1) is already the
two-sided chain-pair length count; it is not an additional later tail factor.

The following gives the uniform asymptotic needed in the constant-one
argument.

### Theorem 1.1 (uniform product-SCD tail theorem)

There is an absolute constant \(C\) such that, for all \(m\ge1\) and all
integers \(0\le H\le m-1\),

\[
 \boxed{
 \frac{L_m(m-H-1)}{\binom{2m}m}
 \le C\exp\!\left(-\frac{H^2}{8m}\right).}
 \tag{1.2}
\]

In particular, uniformly for every integer sequence \(H=H_m\),

\[
 \frac{H_m}{\sqrt m}\longrightarrow\infty
 \quad\Longrightarrow\quad
 L_m(m-H_m-1)=o\!\binom{2m}m.
 \tag{1.3}
\]

No hypothesis \(H\le m/2\) is needed for (1.2) or (1.3). If \(H\ge m\),
then \(m-H-1<0\) and (1.1) is zero under the stated convention, so the
conclusion is trivial.

The scale in (1.3) is sharp for this product-SCD word. If

\[
 \frac{H_m}{\sqrt m}\longrightarrow c\in[0,\infty),
\]

then

\[
 \frac{L_m(m-H_m-1)}{\binom{2m}m}\longrightarrow T(c)>0,
 \tag{1.4}
\]

where

\[
 \boxed{
 \begin{aligned}
 T(c)={}&4\left(c^2+\frac12\right)e^{-c^2}\operatorname{erf}(c)
       +\frac{4c}{\sqrt\pi}e^{-2c^2}\\
      &\hspace{28mm}+2\sqrt2\,\operatorname{erfc}(\sqrt2c).
 \end{aligned}}
 \tag{1.5}
\]

Consequently, for \(0\le H_m\le m-1\),

\[
 L_m(m-H_m-1)=o\!\binom{2m}m
 \quad\Longleftrightarrow\quad
 \frac{H_m}{\sqrt m}\longrightarrow\infty.
 \tag{1.6}
\]

The reverse implication in (1.6) is a tightness statement only about this
explicit product-SCD word; it is not a lower bound for all possible tail
words.

## 2. Exact parity normal form

Let

\[
 r=m-H-1,
 \qquad d=H+1-\epsilon_m,
 \qquad x=h_m-a.
\]

Then

\[
 r-a=h_m+x-d.
 \tag{2.1}
\]

For \(0\le x<h_m\), the exact chain weight is

\[
 B_{m,x}:=A_m(h_m-x)w_m(h_m-x)
 =\binom m{h_m-x}
   \frac{(2x+\epsilon_m+1)^2}{h_m+x+\epsilon_m+1}.
 \tag{2.2}
\]

At the exceptional value \(x=h_m\), corresponding to \(a=0\),

\[
 B_{m,h_m}=m,
 \tag{2.3}
\]

rather than \(m+1\). Thus (1.1) becomes the exact parity-uniform formula

\[
 \boxed{
 L_m(m-H-1)
 =2\sum_{x=0}^{h_m}B_{m,x}
   \binom m{h_m-(d-x)_+},}
 \tag{2.4}
\]

where a binomial with a negative lower index is interpreted as zero. Also

\[
 \boxed{\sum_{x=0}^{h_m}B_{m,x}=2^m-1.}
 \tag{2.5}
\]

Indeed, \(A_m(a)\) is the number of symmetric chains with minimum rank
\(a\), and a full such chain has \(m-2a+1\) members. These chains partition
\(Q_m\), so the corresponding full sum is \(2^m\). The definition
\(w_m(0)=m\) omits the empty initial block on the unique \(a=0\) chain and
subtracts exactly one.

Formula (2.4) audits both parity shifts. For even \(m\), saturation begins
at \(x=H+1\); for odd \(m\), it begins at \(x=H\).

## 3. Uniform exponential estimate

We first record the elementary central-ratio inequality

\[
 \boxed{
 \frac{\binom m{h_m-y}}{M_m}\le e^{-y^2/m}}
 \qquad(0\le y\le h_m).
 \tag{3.1}
\]

For \(m=2h\), the ratio is

\[
 \prod_{j=1}^{y}\frac{h-j+1}{h+j}.
\]

The logarithm of the \(j\)-th factor is at most
\(-(2j-1)/(h+j)\le-(2j-1)/m\); summing gives \(-y^2/m\).
For \(m=2h+1\), the factors are

\[
 \frac{h-j+1}{h+j+1},
\]

whose logarithms are at most \(-2j/m\). This is even stronger than (3.1).

Equations (2.2) and (3.1) imply, for \(x<h_m\),

\[
 \boxed{
 \frac{B_{m,x}}{M_m}
 \le \frac{8(x+1)^2}{m}e^{-x^2/m}.}
 \tag{3.2}
\]

Split (2.4) at

\[
 t=\lfloor d/2\rfloor.
\]

If \(x\le t\), then \(d-x\ge d/2\ge H/2\). By (3.1),

\[
 \binom m{h_m-(d-x)_+}
 \le M_m e^{-H^2/(4m)}.
\]

Using (2.5), this part of (2.4), divided by \(W_{2m}\), is at most

\[
 2\frac{2^mM_m}{W_{2m}}e^{-H^2/(4m)}.
 \tag{3.3}
\]

If \(x>t\), then \(x>d/2\ge H/2\). The second binomial in (2.4) is at
most \(M_m\), while

\[
 e^{-x^2/m}
 \le e^{-H^2/(8m)}e^{-x^2/(2m)}.
\]

Therefore (3.2) bounds the nonexceptional part by

\[
 16\frac{M_m^2}{W_{2m}}e^{-H^2/(8m)}
 \left[
  \frac1m\sum_{x\ge0}(x+1)^2e^{-x^2/(2m)}
 \right].
 \tag{3.4}
\]

The bracket is \(O(\sqrt m)\), by comparison with the Gaussian second
moment integral. The standard Wallis bounds give, uniformly in \(m\),

\[
 \frac{2^mM_m}{W_{2m}}=O(1),
 \qquad
 \frac{M_m^2\sqrt m}{W_{2m}}=O(1).
 \tag{3.5}
\]

The exceptional term \(x=h_m\) is at most

\[
 \frac{2mM_m}{W_{2m}}=O(m2^{-m}),
\]

which is \(O(e^{-H^2/(8m)})\) for \(H\le m-1\). Combining (3.3)--(3.5)
proves (1.2). Keeping elementary numerical versions of the Wallis and
Gaussian-integral bounds shows that \(C=10^4\) is valid; no optimization of
this inessential absolute constant is intended.

For completeness, monotonicity gives a second way to remove the historical
restriction \(H\le m/2\): \(C_m(r-a)\), hence \(L_m(r)\), is nondecreasing
in \(r\). Thus every \(H>m/2\) is bounded by the case
\(H=\lfloor m/2\rfloor\), already exponentially small.

## 4. Fixed-deviation limit and sharpness

Let

\[
 u=\frac{2x+\epsilon_m}{\sqrt m}.
\]

The mesh in \(u\) is \(2/\sqrt m\). Uniformly on compact \(u\)-intervals,
Stirling's formula and (2.2) give

\[
 \frac{B_{m,x}}{M_m}
 \longrightarrow 2u^2e^{-u^2/2}.
 \tag{4.1}
\]

If \(H/\sqrt m\to c<\infty\), then (2.1) gives

\[
 \frac{\binom m{h_m-(d-x)_+}}{M_m}
 \longrightarrow
 \begin{cases}
 e^{-(2c-u)^2/2},&0\le u<2c,\\
 1,&u\ge2c.
 \end{cases}
 \tag{4.2}
\]

The bounds (3.1)--(3.2) supply an integrable Gaussian dominator. Since

\[
 \frac{M_m^2}{W_{2m}}\sim\frac2{\sqrt{\pi m}},
\]

Riemann summation in (2.4) yields

\[
 T(c)=\frac4{\sqrt\pi}
 \left[
  \int_0^{2c}u^2e^{-[u^2+(2c-u)^2]/2}\,du
  +\int_{2c}^{\infty}u^2e^{-u^2/2}\,du
 \right].
 \tag{4.3}
\]

Evaluation of the two Gaussian integrals gives (1.5). In particular,
\(T(c)>0\) for every finite \(c\ge0\). If
\(L_m(m-H_m-1)/W_{2m}\to0\) but \(H_m/\sqrt m\not\to\infty\), a
subsequence has \(H_m/\sqrt m\to c<\infty\), contradicting (1.4). This
proves the reverse
direction of (1.6).

The large-\(c\) behavior of the exact fixed-deviation profile is

\[
 T(c)\sim4c^2e^{-c^2}.
 \tag{4.4}
\]

There is also a sharper uniform moderate-deviation estimate. Put
\(g=H+1\). Uniformly for

\[
 \sqrt m\le g=o(m^{2/3}),
\]

the Vandermonde/hypergeometric second-moment calculation gives

\[
 L_m(m-g)
 \le C_1\left(1+\frac{g^2}{m}\right)\binom{2m}{m-g}.
 \tag{4.5}
\]

Moreover, the exact successive-ratio product gives

\[
 \frac{\binom{2m}{m-g}}{\binom{2m}m}
 \le\exp\!\left(-\frac{g^2}{m+g}\right).
 \tag{4.6}
\]

Thus, if \(c=g/\sqrt m\to\infty\) in this range,

\[
 \frac{L_m(m-g)}{W_{2m}}
 =O\!\left((1+c^2)e^{-c^2+o(1)}\right),
 \tag{4.7}
\]

consistent with the sharp fixed-profile asymptotic (4.4).

## 5. Exact trimmed lift to odd dimension

Let \(B=(b_1,\ldots,b_L)\) be the product-SCD word in \(Q_{2m}\), and let
\(z\) be a new coordinate. Form

\[
 B^+=
 (b_1,\ldots,b_L,\{z\},
   b_1\cup\{z\},\ldots,b_{L-1}\cup\{z\}).
 \tag{5.1}
\]

This word has exactly \(2L\) entries. Every old target uses its old witness
in the first copy, and ({z\}) is literal. For a target (S\cup\{z\})
with (S\ne\varnothing), choose a (B)-witness (b_i,\ldots,b_j) for
(S). If (j<L), use the corresponding interval in the transformed copy.
If (j=L), use the first-copy suffix (b_i,\ldots,b_L) followed by
({z\}). Hence (5.1) is the exact trimmed one-coordinate lift; the old
(2L+1) lift has one redundant final transformed entry.

For \(r=m-H-1\), the even word covers

\[
 |S|\le m-H-1
 \quad\text{or}\quad
 |S|\ge m+H+1.
\]

The lifted word therefore covers every nonempty odd-dimensional target
outside

\[
 m-H\le |T|\le m+H+1.
\]

Indeed, removing \(z\) lowers the rank by one for targets containing it,
and targets not containing it retain their even rank. Thus the exact odd
tail charge is

\[
 \boxed{2L_m(m-H-1),}
 \tag{5.2}
\]

not \(L_m\), and not \(4L_m\) in addition to the factor already present in
(1.1).

Since

\[
 \binom{2m+1}m=\frac{2m+1}{m+1}\binom{2m}m,
\]

(1.2) gives the exact normalization

\[
 \frac{2L_m(m-H-1)}{\binom{2m+1}m}
 \le
 \frac{2(m+1)}{2m+1}C
 e^{-H^2/(8m)}.
 \tag{5.3}
\]

The nonzero problem \(\nu\) is therefore handled without an additive
entry. If the full problem \(N\), including the empty target, is desired,
one global empty entry is prepended after all words are concatenated.

## 6. Exact compositional scope

The product-SCD word is an independently appended literal word. Its proof
uses no property of the Stage-A middle factor, no MSW chronology, no owner
labels, and no assumption that the middle construction is complete rather
than obtained after deleting a leave. Consequently it composes with every
Stage-A word: witnesses internal to either concatenated block remain valid.

For the tail term itself, the sole asymptotic condition is

\[
 H/\sqrt m\longrightarrow\infty.
\]

The upper hypothesis

\[
 H=o(m)
\]

enters elsewhere: the standard row-linearization of the central factor has
exact collar cost

\[
 \frac{2H+1}{2m+1}\binom{2m+1}m,
\]

which is \(o(W)\) precisely in that construction when \(H=o(m)\). Thus the
natural fully composable regime is

\[
 \boxed{\sqrt m\ll H\ll m.}
\]

The previously stated \(H\le m/2\) is only a convenient sufficient range;
it is neither needed nor sharp for the product-SCD tail estimate.
