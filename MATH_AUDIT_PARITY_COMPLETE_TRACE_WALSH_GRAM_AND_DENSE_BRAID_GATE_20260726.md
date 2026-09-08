# Parity-complete paired lifts: exact erased-context Walsh--Gram and the dense-braid gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The affine double-factor theorem solves the pointwise parity
complete-mapping equations, but its \(Q_4\) seed does not solve the trace
code.

For aligned coarse depth \(d\), the even-time start set has size

\[
 N=2^{2r-1}.                                                       \tag{0.1}
\]

After the affine change \(y=Sp+x\), the trace collision operator is
translation invariant in the even parity context \(p\). It therefore
diagonalizes exactly under the Walsh transform of

\[
 E=\{p\in\mathbb F_2^r:|p|\equiv0\pmod2\}.
\]

If \(J=J_d^{G_0}(y)\), define

\[
 H_{S,J}
 =E\cap\mathbb F_2^J\cap S^{-1}\mathbb F_2^J.                     \tag{0.2}
\]

The zero parity-Walsh block has diagonal entry at least
\(|H_{S,J}|\). Equivalently, every trace through phase \(y\) has at least
\(|H_{S,J}|\) starts in its fibre before any additional off-phase
collision is counted.

For the affine \(Q_4\) seed \(S=(2\,4)\), every \(d\)-set satisfies

\[
 |H_{S,J}|\ge2^{d-2}\qquad(d\ge2).                                \tag{0.3}
\]

Thus at \(d=3\) the 128 aligned starts already have collision excess at
least 64, and at growing \(d\)

\[
 \operatorname {Exc}_d
 \ge
 2^{2r-1}\bigl(1-2^{2-d}\bigr).                                  \tag{0.4}
\]

The affine seed is therefore not a recursively usable trace-rainbow seed.

Dense equal-column \(Q_4\) compositions do not repair this within the
currently certified affine/syndrome architecture. If \(G_0\) remains a
standard \(K=\ker\Psi\)-translation syndrome factor and the net
coordinate permutation satisfies \(\Psi S=\Psi\), then every

\[
 e\in E\cap K\cap\mathbb F_2^J                                  \tag{0.5}
\]

produces an exact trace collision, independently of how densely \(S\)
is written as equal-column transpositions. Since
\(\operatorname {rank}\Psi=\log_2r\),

\[
 \dim(E\cap K\cap\mathbb F_2^J)
 \ge d-\log_2r-1.                                                 \tag{0.6}
\]

At every \(d-\log r\to\infty\), the collision excess is
\((1-o(1))2^{2r-1}\), not \(o(2^{2r})\).

There is one possible escape, but it is a new theorem: use genuinely
row-dependent dense braid compositions so that translation by \(K\)
changes the coarse order and encodes the row/context. The existing
phasewise Latin criterion proves exactness of one such coarse factor, but
does not simultaneously provide the same-owner relation required by the
affine double-factor lemma. Nor does it estimate the zero Walsh block
below.

The exact remaining condition is:

\[
 \left\langle{\bf1},
   (\widehat{\mathcal K}_{d,0}-I){\bf1}\right\rangle
 =o(2^r)
 \qquad(d\le H),                                                   \tag{0.7}
\]

together with both half-step analogues. This is necessary and sufficient
for pair-collision mass \(o(2^{2r})\). No proved dense equal-column braid
construction currently satisfies (0.7).

## 1. Trace incidence and collision Gram

For a parity-complete family \((F_p)_{p\in E}\), put

\[
 J_{p,d}(x)=
 \{d_p(x),d_p(F_px),\ldots,d_p(F_p^{d-1}x)\}.                       \tag{1.1}
\]

The aligned lower or upper physical trace determines the code

\[
 \mathcal C_d(p,x)
 =
 \bigl(J_{p,d}(x),\,x|_{J_{p,d}(x)^c},\,
                     p|_{J_{p,d}(x)^c}\bigr).                     \tag{1.2}
\]

Let \(\mathcal R_d\) be its literal trace space, and define

\[
 A_d(t;p,x)
 ={\bf1}\{\mathcal C_d(p,x)=t\}.                                  \tag{1.3}
\]

Every column of \(A_d\) contains one \(1\). The exact owner-resolved
trace Gram is

\[
 \mathcal K_d=A_d^*A_d,                                          \tag{1.4}
\]

so

\[
 \mathcal K_d((p,x),(p',x'))
 =
 {\bf1}\{\mathcal C_d(p,x)=\mathcal C_d(p',x')\}.                  \tag{1.5}
\]

If \(n_d(t)=|\mathcal C_d^{-1}(t)|\), the occurrence collision excess
and pair collision mass are

\[
\begin{aligned}
 \operatorname {Exc}_d
 &=N-|\operatorname {Im}\mathcal C_d|
   =\sum_t(n_d(t)-1)_+,\\
 P_d
 &=\sum_t\binom{n_d(t)}2
   =\frac12\left(
      \langle{\bf1},\mathcal K_d{\bf1}\rangle-N\right).
\end{aligned}                                                     \tag{1.6}
\]

In particular \(\operatorname {Exc}_d\le P_d\), and
\(P_d=o(2^{2r})\) implies the requested collision-excess estimate.

## 2. Affine double-factor normal form

Assume the affine construction

\[
 y=Sp+x,\qquad
 d_p(x)=\delta_0(y),\qquad
 F_p(x)=x\oplus e_{d_p(x)}.                                      \tag{2.1}
\]

The change \(x\leftrightarrow y\) is a bijection for every \(p\), and
the coarse trajectory is the \(G_0\)-trajectory of \(y\). Hence

\[
 J_{p,d}(x)=J_d^{G_0}(y)=:J(y),                                  \tag{2.2}
\]

independent of \(p\) in the \((p,y)\) coordinates. The code becomes

\[
 \boxed{
 \mathcal C_{S,d}(p,y)
 =
 \bigl(J(y),\,(y+Sp)|_{J(y)^c},\,p|_{J(y)^c}\bigr).}               \tag{2.3}
\]

Compare \((p,y)\) with \((p+e,y')\). Equality of (2.3) is equivalent to

\[
\boxed{
\begin{aligned}
 &e\in E\cap\mathbb F_2^J,\\
 &J(y)=J(y')=J,\\
 &(y+y'+Se)|_{J^c}=0.
\end{aligned}}                                                     \tag{2.4}
\]

The criterion depends on \(p,p'\) only through their difference \(e\).
Thus \(\mathcal K_d\) is convolutional in \(E\).

## 3. Exact parity-Walsh blocks

The character group of \(E\) is

\[
 \widehat E=\mathbb F_2^r/\langle{\bf1}\rangle,
 \qquad \chi_\alpha(e)=(-1)^{\alpha\cdot e}.                       \tag{3.1}
\]

Use the unitary Walsh transform in the \(p\)-coordinate. For
\(\alpha\in\widehat E\), the corresponding block of \(\mathcal K_d\) is

\[
\boxed{
\begin{aligned}
 \widehat{\mathcal K}_{d,\alpha}(y,y')
 ={}&
 {\bf1}\{J(y)=J(y')=:J\}\\
 &\cdot
 \sum_{\substack{
 e\in E\cap\mathbb F_2^J\\
 (Se)|_{J^c}=(y+y')|_{J^c}}}
 (-1)^{\alpha\cdot e}.
\end{aligned}}                                                     \tag{3.2}
\]

Let

\[
 L_{S,J}:E\cap\mathbb F_2^J\longrightarrow\mathbb F_2^{J^c},
 \qquad L_{S,J}(e)=(Se)|_{J^c}.                                   \tag{3.3}
\]

Its kernel is exactly \(H_{S,J}\) from (0.2). If the fibre in (3.2) is
empty, the entry is zero. If it is \(e_0+H_{S,J}\), then

\[
 \widehat{\mathcal K}_{d,\alpha}(y,y')
 =
 (-1)^{\alpha\cdot e_0}
 \sum_{h\in H_{S,J}}(-1)^{\alpha\cdot h}.                         \tag{3.4}
\]

Consequently

\[
 \widehat{\mathcal K}_{d,\alpha}(y,y')
 =
 \begin{cases}
  |H_{S,J}|(-1)^{\alpha\cdot e_0},
      &\alpha\in H_{S,J}^{\perp},\\
  0,&\alpha\notin H_{S,J}^{\perp}.
 \end{cases}                                                       \tag{3.5}
\]

This is the complete erased-parity Walsh spectrum. In particular the
zero character is the nonnegative matrix

\[
\boxed{
 \widehat{\mathcal K}_{d,0}(y,y')
 =
 {\bf1}\{J(y)=J(y')=:J\}
 \#\{e\in E\cap\mathbb F_2^J:
       (Se)|_{J^c}=(y+y')|_{J^c}\}.}                              \tag{3.6}
\]

Because the full start vector is constant in \(p\), only this zero block
contributes to the unweighted collision total:

\[
 \boxed{
 \langle{\bf1},\mathcal K_d{\bf1}\rangle
 =
 |E|\,
 \left\langle{\bf1},
    \widehat{\mathcal K}_{d,0}{\bf1}\right\rangle.}                \tag{3.7}
\]

The identity operator has zero block \(I_{Q_r}\). Therefore

\[
 \boxed{
 P_d=
 \frac{|E|}{2}
 \left\langle{\bf1},
   (\widehat{\mathcal K}_{d,0}-I){\bf1}\right\rangle.}             \tag{3.8}
\]

Equation (0.7) follows. Nonzero parity-Walsh modes describe signed context
correlations, but they cannot compensate a positive zero-block collision:
every even context is used once in the exact lift.

## 4. The unavoidable diagonal subgroup

Set \(y'=y\) in (3.6). Then

\[
 \widehat{\mathcal K}_{d,0}(y,y)
 =|H_{S,J(y)}|.                                                   \tag{4.1}
\]

More directly, for every \(e\in H_{S,J(y)}\),

\[
 (p,y)\longmapsto(p+e,y)                                         \tag{4.2}
\]

preserves the code (2.3): both \(e\) and \(Se\) are supported on the
erased set \(J\). The code fibres at fixed \(y\) therefore contain the
cosets of \(H_{S,J(y)}\).

If \(|H_{S,J(y)}|\ge L\) for every \(y\), then

\[
\begin{aligned}
 |\operatorname {Im}\mathcal C_{S,d}|
 &\le N/L,\\
 \operatorname {Exc}_d
 &\ge N(1-L^{-1}),\\
 P_d
 &\ge\frac N2(L-1).
\end{aligned}                                                     \tag{4.3}
\]

These bounds use only the diagonal part of (3.6); off-phase solutions of
(2.4) can only increase collisions.

## 5. Audit of the affine \(Q_4\) seed

For the double-factor seed,

\[
 r=4,\qquad S=(2\,4).                                             \tag{5.1}
\]

For a \(d\)-set \(J\), put

\[
 t(J)=|J\cap S^{-1}J|.                                           \tag{5.2}
\]

The group \(H_{S,J}\) consists of the even vectors supported on that
intersection. Thus

\[
 |H_{S,J}|=2^{\max\{t(J)-1,0\}}.                                 \tag{5.3}
\]

A transposition changes membership of at most one element of \(J\), so

\[
 t(J)\in\{d-1,d\}.                                                \tag{5.4}
\]

Therefore

\[
 |H_{S,J}|\ge2^{d-2}\qquad(d\ge2),                               \tag{5.5}
\]

proving (0.3)--(0.4).

The finite depths are already decisive:

* \(d=1\): the subgroup bound is trivial;
* \(d=2\): the four consecutive supports in the \(1234\) order contain
  exactly one of \(2,4\), so the subgroup bound is again one;
* \(d=3\): every trace fibre has multiplicity at least two, and some have
  multiplicity four;
* \(d=4\): the even parity subgroup has size eight.

Thus the seed may be useful as a complete-mapping atom, but it is not a
depth-three trace-code atom. Any recursion which merely tensors this
fixed transposition repeats, rather than removes, its parity fibres.

## 6. Dense equal-column compositions in a fixed syndrome factor

Let \(G_0\) now be the standard \(C_{2r}\) syndrome factor with syndrome
map

\[
 \Psi:\mathbb F_2^r\longrightarrow\mathbb F_2^a,
 \qquad a=\log_2r,
 \qquad K=\ker\Psi.                                                \tag{6.1}
\]

Every \(k\in K\) translates a cycle to a cycle with the same phase and
the same coarse direction support:

\[
 J(y+k)=J(y).                                                     \tag{6.2}
\]

Let \(S\) be any permutation obtainable as a composition of
equal-column transpositions for this same syndrome presentation. Then

\[
 \Psi S=\Psi,\qquad SK=K.                                        \tag{6.3}
\]

Fix \(J=J(y)\), and take

\[
 e\in E\cap K\cap\mathbb F_2^J.                                  \tag{6.4}
\]

Put

\[
 p'=p+e,\qquad y'=y+Se.                                          \tag{6.5}
\]

Since \(Se\in K\), equation (6.2) gives \(J(y')=J(y)=J\). Moreover,

\[
 y'+Sp'
 =y+Se+Sp+Se
 =y+Sp,                                                          \tag{6.6}
\]

so the physical phase vector \(x\) is unchanged, while
\(p'|_{J^c}=p|_{J^c}\). Hence (6.5) is an exact trace collision.

The collision subgroup

\[
 H_J^{\rm syn}=E\cap K\cap\mathbb F_2^J                           \tag{6.7}
\]

is independent of the chosen dense composition \(S\). Since restriction
of \(\Psi\) to \(\mathbb F_2^J\) has rank at most \(a\), and even parity
adds at most one further equation,

\[
 \dim H_J^{\rm syn}\ge d-a-1.                                    \tag{6.8}
\]

Therefore every aligned trace has multiplicity at least

\[
 2^{(d-\log_2r-1)_+}.                                             \tag{6.9}
\]

For \(d-\log r\to\infty\),

\[
 \boxed{
 \operatorname {Exc}_d
 \ge
 2^{2r-1}
 \left(1-2^{-(d-\log_2r-1)}\right)
 =(1-o(1))2^{2r-1}.}                                             \tag{6.10}
\]

Thus making \(S\) a dense product of equal-column transpositions does not
help while the coarse base remains the same translation-syndrome factor.
The obstruction is the kernel \(K\), not the transposition length of
\(S\).

## 7. Why arbitrary row-specific braid fields are not yet a solution

The row-specific routing theorem permits cycles

\[
 C_k=\sigma_kP+k
\]

with \(\sigma_k\) in the equal-column stabilizer, provided every phase map

\[
 T_i(k)=k+d_i(\sigma_k)                                           \tag{7.1}
\]

is a permutation. This can make the coarse direction order depend on the
kernel row \(k\), and therefore can break (6.2). It is the only currently
visible way for equal-column braids to encode the erased context.

However, the affine parity-complete lemma needs **two** neighbour
permutations \(G_0,G_1\) satisfying the same-owner pointwise relation

\[
 \delta_1(y)=S\delta_0(y)                                        \tag{7.2}
\]

for one coordinate permutation \(S\). The phasewise Latin conditions
(7.1) for one row field do not imply (7.2), and independently chosen
fields on two shores need not have a common owner coupling.

There is also an exact storage cost. If a net equal-column permutation
\(S\) has \(c(S)\) coordinate cycles, its ownership overlay component
contains

\[
 2^{r-c(S)}                                                       \tag{7.3}
\]

coarse cycles on each shore. A dense product of transpositions therefore
does not remain a product of independent two-cycle \(Q_4\) bits. The
phasewise Latin equations couple those bits on the growing overlay
components.

Hence “compose the independent \(Q_4\) switches densely” skips two
unproved integrality conditions:

1. simultaneous Latin legality of the dense row field; and
2. the same-owner double-factor relation (7.2).

Even after those are supplied, the trace theorem is still the zero-block
condition (0.7), not merely nonconstancy of the row orders.

## 8. Exact positive criterion for a future dense construction

For a fixed affine permutation \(S\), the diagonal collision subgroup is
trivial exactly when

\[
 |J(y)\cap S^{-1}J(y)|\le1                                       \tag{8.1}
\]

for every protected phase \(y\). This removes the collisions in Section
4 but not the off-phase terms of (3.6).

The full necessary and sufficient zero-block condition is

\[
\boxed{
\sum_{\substack{y,y'\\J(y)=J(y')=:J}}
\#\left\{
 e\in E\cap\mathbb F_2^J:
 (Se)|_{J^c}=(y+y')|_{J^c}
\right\}
=2^r+o(2^r).}                                                     \tag{8.2}
\]

The \(2^r\) diagonal solutions \(y'=y,e=0\) are unavoidable. Every other
solution is a trace collision. Equation (8.2) is exactly (0.7) written
without operator notation.

Equivalently, put

\[
 Y_J=\{y:J(y)=J\}.
\]

Then a future construction must make the outside difference multiset

\[
 \{(y+y')|_{J^c}:y,y'\in Y_J\}
\]

asymptotically disjoint, with multiplicity, from

\[
 L_{S,J}(E\cap\mathbb F_2^J)
\]

away from the common zero. This is a physical difference-set condition,
not a direction-histogram condition.

The odd-time and odd-length traces append a boundary direction and one
retained endpoint. Their Walsh blocks are obtained from (3.2) by adding
the corresponding boundary-equality indicator. A coefficient-one local
factor needs (8.2) and both boundary variants simultaneously for every
\(d\le H\).

## 9. Conclusion

The parity-complete programme has advanced by one exact gate:

* the affine double factor proves the complete-mapping ownership equations;
* the \(Q_4\) common-phase braid supplies its first nonconstant finite
  seed.

But the trace audit is negative for every construction currently certified:

* the \(Q_4\) affine seed has \(2^{d-2}\)-size erased-parity fibres;
* every dense global composition inside one fixed syndrome stabilizer
  retains \(2^{d-\log r-1}\)-size syndrome fibres;
* arbitrary row-specific dense braid fields are not yet coupled into a
  parity-complete double factor.

Therefore no proved affine/dense-braid construction has
\(o(2^{2r})\) collision excess through \(d\le H\). The exact remaining
object is a row-dependent double factor satisfying the Latin equations,
the same-owner relation, and the zero-block difference-set condition
(8.2) at every protected depth.
