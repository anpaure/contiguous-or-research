# Rounding the recursive MSW trade cube: the integer gate is cheap on logarithmic windows

Date: 2026-07-26

## 0. Outcome

The special MSW matrix does not presently admit a proved balanced-matrix
or total-unimodularity theorem.  Nevertheless its integrality loss can be
bounded without one.

Let `M` be the number of elementary rectangle bits at one fixed recursive
scale.  At every depth, toggling one bit changes at most four old target
occurrences into four new ones.  Moreover the possible target of that
toggle depends on at most four other bits.  These two facts imply:

* for a fixed-depth additive subcube, every fractional point rounds with
  cap-tail loss at most `2M`;
* for the full, possibly nonadditive cube, every product fractional state
  has an integral realization with cap-tail loss at most `16M` per depth;
* simultaneously on a window `Q`, the loss is at most
  `16M|Q|`, or `16M sum_(q in Q) w_q` for weighted cap tails.

At the fatal Catalan scale `r=Theta(log p)`,

\[
 M=\Theta(W/r^{3/2}).                                    \tag{0.1}
\]

Consequently the full integer-rounding loss is `o(W)` on every window

\[
                         |Q|=o(r^{3/2}),                 \tag{0.2}
\]

and in particular is `O(W/sqrt(r))=o(W)` on a one-sided
`O(r)=O(log p)` window.  Thus **integrality is not the remaining gate for
the logarithmic-band theorem**.  The remaining gate there is fractional
four-arm dispersion (or its exact dynamic analogue).

The same estimate does not reach a Gaussian window: for
`|Q|` of order `p^(1/4)` or larger, (0.2) fails by a polynomial factor.
Laminarity and the five color classes do not by themselves improve this,
because the same bit can have cap-sensitive action at every depth.

---

## 1. A universal additive rounding lemma

Let `A_q` be the signed target matrix of an additive switch family
`E`, with `|E|=M`.  Assume

\[
 \sum_Sa_{q,e}(S)=0,qquad
 \|a_{q,e}\|_1\le8,qquad
 \|a_{q,e}\|_2^2\le8.                                  \tag{1.1}
\]

The interior-depth MSW columns satisfy (1.1) with equality.  Let

\[
 K_{q,b}(y)=\sum_S(y(S)-b)_+                              \tag{1.2}
\]

and let `x in [0,1]^E` be arbitrary.

### Theorem 1.1 (additive `2M` rounding)

There is `X in {0,1}^E` such that, simultaneously after summing any
nonnegative depth weights `w_q`,

\[
\boxed{
 \sum_qw_qK_{q,b_q}(\mu_q+A_qX)
 \le
 \sum_qw_qK_{q,b_q}(\mu_q+A_qx)
 +2M\sum_qw_q.}                                         \tag{1.3}
\]

The same assertion holds after replacing each `K_(q,b_q)` by
`(K_(q,b_q)-c_q)_+`.

#### Proof

Round the coordinates independently with `P(X_e=1)=x_e`, and put

\[
                   Y_q=A_q(X-x).                        \tag{1.4}
\]

Only targets in

\[
                   U_q=\bigcup_e\operatorname{supp}a_{q,e}
\]

can fluctuate, so `|U_q|<=8M`.  Independence and (1.1) give

\[
 \sum_S\operatorname {Var}Y_q(S)
 =\sum_ex_e(1-x_e)\|a_{q,e}\|_2^2
 \le2M.                                                  \tag{1.5}
\]

Both the fractional and rounded histograms have the same total mass;
hence `sum_S Y_q(S)=0`.  Therefore

\[
\begin{aligned}
 K_{q,b}(\bar\mu_q+Y_q)-K_{q,b}(\bar\mu_q)
 &\le\sum_SY_q(S)_+\\
 &=\frac12\|Y_q\|_1.                                    \tag{1.6}
\end{aligned}
\]

By Cauchy--Schwarz,

\[
 \mathbb E\|Y_q\|_1
 \le\sqrt{|U_q|\sum_S\operatorname {Var}Y_q(S)}
 \le4M.                                                  \tag{1.7}
\]

Multiply by `w_q`, sum, and choose an outcome no worse than its
expectation.  The outer positive-part map is one-sided one-Lipschitz, so
the same proof applies after subtracting `c_q`.  \(\square\)

At one fixed depth this proves

\[
             0\le K_{q,b}^{\mathbb Z}-K_{q,b}^{\rm LP}
             \le2M.                                     \tag{1.8}
\]

For the fixed-scale parent family, `M=Theta(W/r^(3/2))`; hence the
integrality gap in the exact one-depth four-arm dual is automatically
`o(W)`.  No special total-unimodularity theorem is required for that
conclusion.

---

## 2. Nonadditive cube: finite dependence replaces a matrix

Let the `M` elementary switches be independent Bernoulli bits with
arbitrary biases.  Every bit-state is an exact middle factor.  Write

\[
                    \mu_q(X),\qquad
                    \bar\mu_q=\mathbb E\mu_q(X).         \tag{2.1}
\]

For a fixed depth `q`, join two switches when they occur in a common row
as the two boundary phases of one depth-`q` window.  Boundary locality of
the rectangle gives

\[
                         \Delta(G_q)\le4.                \tag{2.2}
\]

Changing bit `e` changes at most four old occurrences into four new ones.
Its target difference depends only on the states of its neighbors in
`G_q`: each affected window has only one opposite boundary.

### Lemma 2.1 (active target support)

Let `U_q` be the set of targets whose load is nonconstant on the Boolean
cube.  Then

\[
                         |U_q|\le128M.                   \tag{2.3}
\]

#### Proof

If a target varies, it changes on some edge of the Boolean cube, hence
belongs to the support of the toggle difference of some switch `e` in
some state.  The toggle difference has at most eight endpoints and, by
(2.2), at most `2^4` possible neighbor states.  Thus switch `e` contributes
at most `8*2^4=128` possible targets.  Sum over `e`.  \(\square\)

The constant is deliberately crude; using the fact that each boundary
window has only one opposite boundary improves it, but no asymptotic
gain is needed.

### Theorem 2.2 (nonadditive `16M` rounding)

Some exact cube state `X` satisfies

\[
\boxed{
 \sum_qw_q\bigl(K_{q,b_q}(\mu_q(X))-c_q\bigr)_+
 \le
 \sum_qw_q\bigl(K_{q,b_q}(\bar\mu_q)-c_q\bigr)_+
 +16M\sum_qw_q.}                                        \tag{2.4}
\]

#### Proof

Put `Y_q=mu_q(X)-bar(mu)_q`.  Resampling one Bernoulli bit changes a
histogram by a vector with at most four removed and four inserted units.
After cancellations its positive and negative masses are at most four,
so its squared norm is at most

\[
                         4^2+4^2=32.                     \tag{2.5}
\]

Efron--Stein, summed over targets, gives

\[
 \sum_S\operatorname {Var}\mu_q(X;S)
 \le\frac12\sum_e
     \mathbb E\|\mu_q(X)-\mu_q(X^{(e)})\|_2^2
 \le8M.                                                  \tag{2.6}
\]

Here `X^(e)` denotes independent resampling of bit `e`; the sharper
constant follows because the two samples differ with probability at most
one half.  By (2.3) and Cauchy--Schwarz,

\[
 \sum_S\mathbb E|Y_q(S)|
 \le\sqrt{128M\cdot8M}=32M.                              \tag{2.7}
\]

Every cube state and its mean have total mass `W`, so the one-sided
inequality (1.6), followed by the outer positive part, costs at most half
of (2.7).  Sum over depths and choose an outcome no worse than the
expectation.  \(\square\)

Taking `w_q=1` on a depth set `Q` gives error at most `16M|Q|`.
Together with (0.1),

\[
 {16M|Q|\over W}=O\left({|Q|\over r^{3/2}}\right).       \tag{2.8}
\]

This proves the claim (0.2), without extracting an additive color class
and without losing its density.

---

## 3. The parent-laminar refinement

At the matched depth, switches in one aligned parent context `C` have the
form

\[
 a_{C,R}
 =\partial_C(A_C+B_C)
  -\partial_C(P^E_{C,R}+P^O_{C,R}).                      \tag{3.1}
\]

The suffix arms `A_C,B_C` are common to all `R` in that parent.  Thus a
dependent rounding which preserves

\[
                         \sum_Rx_{C,R}                   \tag{3.2}
\]

up to its floor or ceiling makes the entire common-suffix discrepancy at
most one copy per parent, rather than one copy per elementary switch.
For depths `q>=r`, the relevant suffix length lies in the exterior tail,
so the same packet sum controls the two common suffix arms simultaneously
at all such depths.

This is a valid structural gain, but by itself it changes only constants
in Theorems 1.1--2.2: the two prefix arms still vary with `R`, and no
audited bounded-frequency theorem is known for their global target
collisions.  In particular, laminar parent contexts do not presently give
a Gaussian-window discrepancy theorem.

Similarly, the five-color conflict decomposition proves additivity inside
one color.  It says nothing about total unimodularity of the four-arm
columns inside that color, and using only one color loses four fifths of
the already critical raw capacity.  Theorem 2.2 is preferable for
rounding because it uses all colors at once.

---

## 4. What is and is not settled

The following statements are now rigorous.

1. **One depth.**  Once the fractional weighted-potential inequalities are
   proved for the fixed-scale additive MSW family, the integer answer is
   within `O(W/r^(3/2))=o(W)`.  The determinant-two phenomenon cannot
   obstruct the theorem at the `o(W)` scale.
2. **Logarithmic windows.**  Any product fractional construction on the
   full exact cube rounds with `o(W)` aggregate loss for
   `H=O(r)=O(log p)`.
3. **Gaussian windows.**  The bound is too large.  A new correlated
   discrepancy theorem would have to exploit cancellation of the prefix
   flags, not merely bounded degree, laminar contexts, or conflict colors.

No positive-density determinant-two minor has been proved for the literal
MSW matrix.  The common suffix rows in (3.1) are star-like rather than an
odd-cycle certificate; any such minor would have to use collisions among
the variable prefix targets across parent contexts.  That collision
geometry is exactly the unresolved four-arm routing problem, so asserting
a positive-density obstruction there would be circular.

The sharp remaining constant-one gate is therefore not fixed-depth
integrality.  It is a common multidepth fractional/dynamic drain theorem,
or a genuinely stronger discrepancy estimate that reduces the factor
`|Q|` in (2.8) on Gaussian windows.

