# Shared-boundary collision gain for zero-winding PBBS returns

Date: 2026-07-25

This note works only on the coefficient-one gate

\[
 \overline\nu_{H_A}=o_A(\operatorname{Cat}_r/\sqrt r),
 \qquad H_A=\lceil A\sqrt r\rceil .
\]

It strengthens the logarithmic positive-overlap theorem in
`MATH_ATTACK_A_QST_LOG_OVERLAP_DIFFUSE_CELL_20260725.md`.  The earlier
array bound counted the forward and dual arrays independently.  A genuine
return has the same balanced boundary word on both arrays.  Enforcing this
literal equality cancels the exponential factor (4^\ell).

## 1. Set-up

Retain the notation of that theorem.  Thus a zero-winding return of
duration (s) and endpoint excess (2\ell) has

\[
 U=(0S_{s-1})\cdots(0S_1)=ER_0,
 \qquad
 V=(\overline T_{s-1}0)\cdots(\overline T_00)
   =R_s(0S_s)E,                                      \tag{1.1}
\]

where (E) is one balanced word of length (2\ell), and

\[
 \operatorname{ht}(S_j)\le \min\{j,s-j+\ell\},
 \quad
 \operatorname{ht}(T_j)\le \min\{s-1-j,j+1+\ell\}. \tag{1.2}
\]

Put

\[
 F_{s,\ell}(z)=
 \prod_{j=1}^{s-1}C_{\min\{j,s-j+\ell\}}(z).         \tag{1.3}
\]

At (z=1/4), independently give each capped Dyck block (D) the
Boltzmann probability

\[
 \Pr_a(D)=\frac{2^{-|D|}}{C_a(1/4)}.                \tag{1.4}
\]

The forward and dual array partition functions are both
(F_{s,\ell}(1/4)).

## 2. A pointwise boundary-word estimate

### Lemma 2.1

There is an absolute (C) such that, whenever (3\ell<s-2), every
balanced word (e) of length (2\ell) satisfies

\[
 \Pr(U[1,2\ell]=e)\le C4^{-\ell},
 \qquad
 \Pr(V[|V|-2\ell+1,|V|]=e)\le C4^{-\ell}.           \tag{2.1}
\]

#### Proof

Suppose first that (e) is a possible prefix of (U).  Let

\[
 h=-\min_{0\le t\le2\ell}\operatorname{net}(e[1,t]).
\]

Since (e) begins with the delimiter zero and is balanced,
(1\le h\le\ell).  Record minima give the unique parsing

\[
 e=(0D_1)\cdots(0D_{h-1})0P,                       \tag{2.2}
\]

where the (D_i) are complete Dyck words and (P) is a prefix of a
Dyck word, ending at height (h).  These are respectively the observed
parts of

\[
 S_{s-1},S_{s-2},\ldots,S_{s-h}.
\]

Because (3\ell<s-2), their caps are exactly

\[
 \ell+1,\ell+2,\ldots,\ell+h.                      \tag{2.3}
\]

For a fixed prefix (P), the total critical weight of all capped Dyck
completions of (P) is at most (2^{1-|P|}).  Indeed, decompose a
completion at its first return to zero; the first-return part has total
fair-walk weight at most one and the remaining capped Dyck suffix has
weight (C_a(1/4)\le2).  Consequently (2.2) and (1.4) give

\[
 \Pr(U[1,2\ell]=e)
 \le 2^{1-\sum_i|D_i|-|P|}
       \prod_{i=1}^{h-1}\frac1{C_{\ell+i}(1/4)}.     \tag{2.4}
\]

Now

\[
 \sum_i|D_i|+|P|=2\ell-h
\]

and

\[
 C_a(1/4)=\frac{2(a+1)}{a+2},
\]

so the product in (2.4) telescopes:

\[
 \prod_{i=1}^{h-1}\frac1{C_{\ell+i}(1/4)}
 =2^{-(h-1)}\frac{\ell+h+1}{\ell+2}.               \tag{2.5}
\]

Equations (2.4)--(2.5), together with (h\le\ell), prove the first
bound in (2.1).

For the second bound, reverse (V).  Every block
(\overline T_j0) becomes

\[
 0\,\operatorname{rev}(\overline T_j),
\]

and (\operatorname{rev}(\overline T_j)) is Dyck.  The blocks met from
the right have caps

\[
 \ell+1,\ell+2,\ldots .
\]

The same record-minimum argument, applied to
(\operatorname{rev}(e)), proves the second bound.  \(\square\)

### Corollary 2.2 (Hadamard collision)

Let the forward and dual arrays be independent under their critical
Boltzmann laws.  Then

\[
 \boxed{
 \Pr\bigl(U[1,2\ell]=V[|V|-2\ell+1,|V|]
          \text{ and this word is balanced}\bigr)
 \le C\frac{4^{-\ell}}{\sqrt{\ell+1}}.}            \tag{2.6}
\]

#### Proof

There are at most
\(\binom{2\ell}{\ell}\le
C4^\ell/\sqrt{\ell+1}\) balanced words.  Sum the product of the two
pointwise estimates (2.1).  In fact a common carrier word must begin and
end with zero, so its exact number of possibilities is
\(\binom{2\ell-2}{\ell}\); in particular the \(\ell=1\) sector is empty.
\(\square\)

Thus the exact equality of the two copies of (E) recovers (4^{-\ell}),
and balanced-word anti-concentration gives a further
((\ell+1)^{-1/2}).

## 3. Anti-concentration survives conditioning on (E)

### Lemma 3.1

There are absolute (c,C>0) such that, if

\[
 0\le h\le\ell\le cs,
\]

then the critical coefficient distribution of

\[
 P_{s,\ell,h}(z)
 :=\prod_{j=1}^{s-h-1}C_{\min\{j,s-j+\ell\}}(z)     \tag{3.1}
\]

has largest atom at most (C/s^2).

#### Proof

Put (M=s+\ell) and (a=\ell+h+1).  Direct telescoping gives

\[
 P_{s,\ell,h}(z)=\frac{Q_a(z)}{Q_U(z)Q_V(z)},       \tag{3.2}
\]

where

\[
 |U-V|\le1,
 \qquad U+V=M+1.
\]

Indeed, if (M=2p), the caps in (3.1) are

\[
 1,2,\ldots,p,p-1,\ldots,a,
\]

and (3.2) has ((U,V)=(p,p+1)).  If (M=2p+1), the central cap (p)
is repeated and ((U,V)=(p+1,p+1)).

Normalize (3.2) at (z=1/4).  For (z=e^{it}/4), put

\[
 x=\sqrt{1-e^{it}},\qquad \Re x\ge0.
\]

The exact formula

\[
 Q_j(z)=\frac{(1+x)^{j+1}-(1-x)^{j+1}}{2^{j+1}x}
\]

gives

\[
 \frac{|Q_a(e^{it}/4)|}{Q_a(1/4)}\le e^{a|x|}.     \tag{3.3}
\]

When (V=U+1), use

\[
 \frac{z^U}{Q_UQ_{U+1}}=H_U=C_U-C_{U-1};
\]

when (V=U), use

\[
 \frac{z^{U-1}}{Q_U^2}=C_{U-1}H_{U-1}.
\]

The normalized (C_{U-1}) factor has modulus at most one, and the exact
path-kernel bound is

\[
 |\varphi_{H_U}(t)|\le
 \begin{cases}
 1,&U|x|\le1,\\
 C(U|x|)^2e^{-cU|x|},&U|x|\ge1.
 \end{cases}                                       \tag{3.4}
\]

Choose the absolute constant in (ell\le cs) small enough that
(a\le2\ell+1\le cU/2).  Then (3.3) is absorbed by (3.4).  Since
(|x|\asymp\sqrt{|t|}) near zero,

\[
 \int_{-\pi}^{\pi}|\varphi_{P_{s,\ell,h}}(t)|dt
 \le\frac C{U^2}\le\frac C{s^2}.                  \tag{3.5}
\]

Indeed, after absorption the first power of the right side of (3.4)
is integrable under the substitution \(y=U\sqrt{|t|}\), and its
integral is \(O(U^{-2})\).  Fourier inversion now proves the claim.
\(\square\)

### Corollary 3.2

Condition on any common boundary word (E=e) in (1.1).  The largest
atom of the total forward-plus-dual semilength is at most (C/s^2),
uniformly for (ell\le cs).

#### Proof

Let (h) be the record depth in (2.2).  Conditioning on the forward
prefix fixes the complete blocks (S_{s-1},\ldots,S_{s-h+1}) and a
prefix of (S_{s-h}).  It leaves

\[
 S_1,\ldots,S_{s-h-1}

\]

independent with partition function (3.1).  Their total semilength has
largest atom (C/s^2) by Lemma 3.1.  Adding the conditional partial-block
completion and the complete dual array is convolution, which cannot
increase the largest atom.  Mixing over (E) also preserves this bound.
\(\square\)

## 4. Polynomial positive-overlap theorem

Let (G_{s,\ell}(z)) count pairs of forward and dual capped arrays that
have the same balanced boundary word (E) of length (2\ell).  From
Corollary 2.2,

\[
 G_{s,\ell}(1/4)
 \le C\frac{4^{-\ell}}{\sqrt{\ell+1}}
       F_{s,\ell}(1/4)^2.                          \tag{4.1}
\]

The exact rank identity is

\[
 r=s+\sum_{j=1}^{s-1}|S_j|_e
     +\sum_{j=0}^{s-1}|T_j|_e-\ell.                \tag{4.2}
\]

Corollary 3.2, (4.1), and coefficient tilting at (1/4) therefore give

\[
 z_{r,s,2\ell}
 \le C4^{r-s+\ell}\frac1{s^2}
          \frac{4^{-\ell}}{\sqrt{\ell+1}}
          F_{s,\ell}(1/4)^2.                       \tag{4.3}
\]

The exact telescope from the earlier note says

\[
 4^{-(s-\ell)}F_{s,\ell}(1/4)^2
 \le C\frac{4^\ell(\ell+2)^2}{s^4}.               \tag{4.4}
\]

Combining (4.3)--(4.4) yields

\[
 \boxed{
 z_{r,s,2\ell}
 \le C4^r\frac{(\ell+2)^2}{s^6\sqrt{\ell+1}}.}    \tag{4.5}
\]

### Theorem 4.1

Fix (A>0), and let (Z_r(A,L)) count normalized roots starting genuine
zero-winding returns with

\[
 s\le A\sqrt r,
 \qquad 0<\Lambda\le2L.
\]

If

\[
 \boxed{L\log r=o(r^{1/5}),}                       \tag{4.6}
\]

then

\[
 \boxed{Z_r(A,L)=o_A(B_r/\sqrt r).}                \tag{4.7}
\]

#### Proof

Choose

\[
 s_0=\left\lfloor\sqrt{\frac r{K\log r}}\right\rfloor
\]

with fixed sufficiently large (K).  The path-graph spectral estimate
makes all (s<s_0) contribute (o(B_r/\sqrt r)).  Condition (4.6)
implies (L=o(s_0)), so (4.5) applies to every retained term.  Hence

\[
 \begin{aligned}
 \sum_{\ell\le L}\sum_{s\ge s_0}z_{r,s,2\ell}
 &\le C4^r
   \left(\sum_{\ell\le L}\frac{(\ell+2)^2}{\sqrt{\ell+1}}\right)
   \left(\sum_{s\ge s_0}s^{-6}\right)\\
 &\le C4^r\frac{L^{5/2}(\log r)^{5/2}}{r^{5/2}}.
 \end{aligned}                                     \tag{4.8}
\]

Since (B_r/\sqrt r\asymp4^r/r^2), (4.6) turns (4.8) into little-oh.
\(\square\)

## 5. Consequence and exact residual

The complete zero-winding sector with

\[
 \Lambda=o\!\left(\frac{r^{1/5}}{\log r}\right)
\]

is now negligible at the coefficient-one quotient scale.  This is a
strict polynomial improvement over the earlier logarithmic range.

At the start-count level, the unresolved zero-winding sector begins at
order (r^{1/5}/\log r).  Section 6 improves the packing frontier to
order (r^{1/5}).  The positive-winding residual remains bounded winding
with an interior-macroscopic transported overlap cell.  No coefficient-one
claim is made here.

## 6. Packing-level removal of the logarithm

Theorem 4.1 counts every start and therefore used a shrinking spectral
cutoff (s_0\asymp\sqrt{r/\log r}).  The coefficient-one gate asks only
for a quotient-edge-disjoint packing.  For such a packing the already
proved sub-Gaussian height theorem gives

\[
 \lim_{a\downarrow0}\limsup_{r\to\infty}
 \frac{\sqrt r}{B_r}
 \overline\nu_{\le a\sqrt r}=0.                  \tag{6.1}
\]

### Theorem 6.1 (log-free shared-boundary packing range)

Fix (A>0), let \(L=L(r)\) be a deterministic integer sequence, and let
\(\mathcal P_r(A,L)\) be any quotient-edge-disjoint
family of genuine zero-winding returns satisfying

\[
 s\le A\sqrt r,
 \qquad0<\Lambda\le2L.
\]

If

\[
 \boxed{L=o(r^{1/5}),}                            \tag{6.2}
\]

then

\[
 \boxed{|\mathcal P_r(A,L)|=o_A(B_r/\sqrt r).}    \tag{6.3}
\]

#### Proof

Fix \(0<a<A\).  The low part satisfies the exact normalized inequality

\[
 \frac{\sqrt r}{B_r}
 |\mathcal P_r(A,L;\ s\le a\sqrt r)|
 \le
 \frac{\sqrt r}{B_r}\overline\nu_{\le a\sqrt r}.
 \tag{6.4}
\]

For fixed \(a\), condition (6.2) implies, uniformly for
\(\ell\le L\) and \(s>a\sqrt r\),

\[
 3\ell<s-2,\qquad \ell\le cs
\]

for all sufficiently large \(r\).  Thus the domain hypotheses behind
(4.5) hold.  A packing is a subset of the start set, so (4.5) gives

\[
 \begin{aligned}
 |\mathcal P_r(A,L;\ s>a\sqrt r)|
 &\le C4^r
 \left(\sum_{\ell\le L}\frac{(\ell+2)^2}{\sqrt{\ell+1}}\right)
 \left(\sum_{s>a\sqrt r}s^{-6}\right)\\
 &\le C_a4^r\frac{L^{5/2}}{r^{5/2}}.
 \end{aligned}                                    \tag{6.5}
\]

Here one may take \(C_a=O(a^{-5})\).  Since
\(B_r/\sqrt r\asymp4^r/r^2\), the normalized high part is

\[
 \frac{\sqrt r}{B_r}
 |\mathcal P_r(A,L;\ s>a\sqrt r)|
 \le
 C'_a\frac{L^{5/2}}{\sqrt r}
 =
 C'_a\left(\frac{L}{r^{1/5}}\right)^{5/2}
 =o(1)                                             \tag{6.6}
\]

for every fixed \(a>0\).  Therefore, for every fixed \(a\in(0,A)\),

\[
 \limsup_{r\to\infty}
 \frac{\sqrt r}{B_r}|\mathcal P_r(A,L)|
 \le
 \limsup_{r\to\infty}
 \frac{\sqrt r}{B_r}\overline\nu_{\le a\sqrt r}.
 \tag{6.7}
\]

Now let \(a\downarrow0\) and use (6.1).  This proves (6.3).
No estimate uniform in \(a\), and no choice \(a=a(r)\), is being used.
\(\square\)

Thus the valid coefficient-one packing frontier is the complete sector

\[
 \Lambda=o(r^{1/5}),
\]

with no logarithmic loss.  Here the little-oh is uniform through one
common deterministic envelope \(0<\Lambda\le2L(r)\); it is not a
pointwise assertion with a different threshold for each family member.
The stronger start-count theorem retains its \((\log r)\) denominator.
