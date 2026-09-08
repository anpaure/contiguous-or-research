# A linear frozen first-shadow floor in the complete MSW `(2 3)` cube

Date: 2026-07-25

Method: pure mathematics only.  No finite search or solver is used.

## 0. The theorem

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad B=\operatorname{Cat}_m={W\over n},
\]

and let `F_m^MSW` be the canonical exact middle wreath factor.  Let
`tau=(2 3)`, and let `F_I` be an arbitrary corner of the **complete**
ownership-component cube between `F_m^MSW` and `tau F_m^MSW`.

### Theorem

For every sufficiently large `m`, the canonical factor has at least

\[
 \boxed{
 (m-3)\operatorname{Cat}_{m-2}-{2W\over m+2}}
\tag{0.1}
\]

missing rank-`(m-1)` targets which are fixed by `tau`.  Consequently every
corner of the complete fixed-transposition cube satisfies

\[
 \boxed{
 H_1(F_I)
 \ge (m-3)\operatorname{Cat}_{m-2}-{2W\over m+2}
 =\left({1\over32}-o(1)\right)W.}
\tag{0.2}
\]

Thus the complete canonical `(2 3)` cube cannot repair the first shadow to
`o(W)`.  This does not say that every edge is non-improving: antipodal
symmetry gives literal improving edges.  It says that a positive-density
subfamily of holes is frozen at every cube vertex.

The proof combines the already verified marked-gap collision certificates
with a new exact fixed-target localization and an exact occurrence-mass
ledger.

## 1. The marked-gap certificates

Put

\[
                         s=m-2,
 \qquad n'=2s+1=2m-3.
\]

For `R in D_s` and a word gap `g in {0,...,2s}`, insert either `1100` or
`1010` at that gap.  The verified insertion--erasure theorem says that in
both MSW flip orders the four inserted labels form one consecutive block,
with the same outside cyclic order.  At the pointed cut following the
block, the two roots therefore give two distinct pointed occurrences of one
common depth-one target; denote it by `S_(R,g)`.

The pointed slots belonging to distinct pairs `(R,g)` are disjoint.  There
are

\[
                         (2s+1)C_s=(2m-3)C_{m-2}
\tag{1.1}
\]

certificate pairs in total.

We now localize a linear fraction of these certificates to targets fixed by
`tau=(2 3)`.

## 2. The insertion gap is carried bijectively to an order gap

Let `rho(R)` be the MSW flip permutation.  After erasing the inserted
four-label block, let

\[
 \varphi_R(g)\in\{0,1,\ldots,2s\}
\]

be the gap of `rho(R)` at which that block occurred.  (The final gap is the
gap before the distinguished omitted label.)

### Lemma 2.1

For every Dyck word `R`, the map

\[
                 g\longmapsto\varphi_R(g)
\tag{2.1}
\]

is a permutation of the `2s+1` gaps.

### Proof

Induct on `s`.  The empty word is immediate.  Write the first-return
decomposition

\[
                         R=1u0v,
 \qquad a=|u|+2.
\]

The MSW recursion is

\[
 \rho(1u0v)=\bigl(a,\ a-\rho(\mu u),\ 1,\ a+\rho(v)\bigr),
\tag{2.2}
\]

where `mu` is reverse-complement.

* The initial gap `g=0` maps to the initial order gap `0`.
* If `g>=a`, the insertion lies in `v`, at local gap `g-a`.  The first
  `a` order entries in (2.2) are unchanged, so
  \[
        \varphi_R(g)=a+\varphi_v(g-a).
  \]
  By induction these values are exactly `a,...,2s`.
* If `1<=g<a`, the insertion lies in `u`, at local gap `g-1`.
  Reverse-complement changes this to the reflected gap
  `|u|-(g-1)` in `mu u`.  The inserted block lies in the second block of
  (2.2), after its initial entry.  Hence
  \[
   \varphi_R(g)
   =1+\varphi_{\mu u}(|u|-g+1).
  \]
  As `g` ranges from `1` to `a-1`, induction makes these values exactly
  `1,...,a-1`.

The three ranges are disjoint and exhaust `0,...,2s`.  This proves the
lemma. \(\square\)

## 3. Erased certificate targets form a complete upper layer

Apply the order-preserving erasure relabeling to `S_(R,g)`.  The outside
cyclic order becomes

\[
                         q_s(R)=(\rho(R),\infty'),
\]

the canonical MSW wreath in dimension `n'=2s+1`.  Starting immediately
after the gap `varphi_R(g)`, the erased certificate target is the
step-two cyclic interval of length `s+1`.

By Lemma 2.1, as `g` runs through all word gaps these are all `n'` upper
middle intervals of the row `q_s(R)`.  As `R` runs through `D_s`, the MSW
rows partition all middle `s`-sets.  Complementing within each row therefore
shows that the erased certificate targets run through

\[
                         \binom{[n']}{s+1}
\]

exactly once.

Among the `(s+1)`-sets of `[n']`, the number fixed by `(2 3)` is

\[
 \binom{n'-2}{s+1}+\binom{n'-2}{s-1}
 ={s\over2s+1}\binom{2s+1}{s+1}
 =sC_s.
\tag{3.1}
\]

For original gaps `g>=3`, the inserted coordinate block begins at label
at least four.  Erasure therefore fixes the physical labels `2,3`, and
fixedness of the erased target is exactly fixedness of the original
target.  Removing the three gaps `g=0,1,2` can discard at most `3C_s` of
the fixed erased targets.

On the other hand, for `g=0,1` the inserted four-label block contains both
physical labels `2,3`.  The certificate target avoids the whole block and
is therefore automatically fixed by `tau`.  Adding these `2C_s`
certificates back proves:

### Lemma 3.1 (fixed certificate count)

At least

\[
 \boxed{
 K_{\rm fix}\ge (s-1)C_s=(m-3)C_{m-2}}
\tag{3.2}
\]

marked-gap certificate pairs have a `tau`-fixed common target.

No distinct-target assertion is needed here; the pointed occurrences are
the disjoint objects.

## 4. Fixed certificates force fixed duplicate excess

For a fixed rank-`(m-1)` target `S`, let `mu(S)` be its canonical MSW load,
and put

\[
 D_{\rm fix}
 =\sum_{\substack{|S|=m-1\\ \tau S=S}}(\mu(S)-1)_+.
\tag{4.1}
\]

Because the certificate pairs use disjoint pointed occurrences, a target
of load `t` supports at most `floor(t/2)` certificate pairs.  Hence Lemma
3.1 gives

\[
 K_{\rm fix}
 \le\sum_{\tau S=S}\left\lfloor{\mu(S)\over2}\right\rfloor
 \le D_{\rm fix}.
\tag{4.2}
\]

Thus the fixed part of the first shadow alone has duplicate excess at least
`(m-3)C_(m-2)`.

## 5. The fixed-target occurrence baseline is only `O(W/m)`

Let

\[
 N_0^{\rm fix}
 =\binom{2m-1}{m}+\binom{2m-1}{m-2}
\tag{5.1}
\]

be the number of `tau`-fixed middle `m`-sets, and let

\[
 N_1^{\rm fix}
 =\binom{2m-1}{m-1}+\binom{2m-1}{m-3}
\tag{5.2}
\]

be the number of `tau`-fixed rank-`(m-1)` targets.

For a wreath row `C`, let `d_C in {1,...,m}` be the shorter cyclic distance
between labels `2,3`.  The row has `n-2d_C` fixed middle intervals.  Since
the factor owns every middle set exactly once,

\[
                   \sum_C(n-2d_C)=N_0^{\rm fix}.
\tag{5.3}
\]

At rank `m-1`, the row again has `n-2d_C` fixed intervals when
`d_C<=m-1`, and it has three fixed intervals when `d_C=m`, two more than
the middle count.  If

\[
                   z=\#\{C:d_C=m\}\le B,
\]

then the total fixed-target occurrence mass is exactly

\[
                         L_{\rm fix}=N_0^{\rm fix}+2z.
\tag{5.4}
\]

The first binomial terms in (5.1)--(5.2) are equal, and

\[
 N_0^{\rm fix}-N_1^{\rm fix}
 ={2(m-1)W\over(m+2)(2m+1)}.
\tag{5.5}
\]

Using `z<=B=W/(2m+1)`, equations (5.4)--(5.5) give the exact upper bound

\[
 \boxed{
 L_{\rm fix}-N_1^{\rm fix}
 \le {2W\over m+2}.}
\tag{5.6}
\]

## 6. Fixed duplicate excess becomes fixed holes

Let `M_fix` be the number of fixed rank-`(m-1)` targets with load zero.
On the fixed target family, the elementary mass identity is

\[
 D_{\rm fix}
 =L_{\rm fix}-(N_1^{\rm fix}-M_{\rm fix}).
\]

Therefore, by (4.2) and (5.6),

\[
\begin{aligned}
 M_{\rm fix}
 &=D_{\rm fix}-(L_{\rm fix}-N_1^{\rm fix})\\
 &\ge(m-3)C_{m-2}-{2W\over m+2}.
\end{aligned}
\tag{6.1}
\]

This proves (0.1).  Finally,

\[
 {C_{m-2}\over C_m}
 ={m(m+1)\over4(2m-1)(2m-3)},
\]

so

\[
 {(m-3)C_{m-2}\over W}\longrightarrow{1\over32},
 \qquad {2\over m+2}\longrightarrow0.
\tag{6.2}
\]

## 7. Why every complete-cube corner inherits the floor

First note that every ownership component is invariant under the involution
which swaps shores and applies `tau`.  Indeed, for a canonical row `C`, let
`d_C<=m` be the shorter cyclic distance between `2,3`.  As in Section 5,
the row owns `n-2d_C>=1` middle intervals fixed by `tau`.  One such fixed
middle owner gives an ownership edge joining the left copy of `C` to the
right copy of `tau C`.  Hence those two row vertices lie in the same
component.  Applying this to every left row shows that, component by
component, the right shore is exactly `tau` of the left shore.

For a `tau`-fixed target `S` and every ownership component `K`, the
new-side component load is

\[
                         b_K(S)=a_K(\tau S)=a_K(S).
\]

Thus its multiplicity is constant component by component throughout the
cube.  In particular every fixed canonical hole remains a hole at every
corner.  Equation (6.1) therefore proves (0.2). \(\square\)

## 8. Consequence and scope

This theorem closes one precise escape route:

\[
 \boxed{
 \text{no selection of components in the complete canonical `(2 3)`
 cube can make }H_1=o(W).}
\]

It is stronger than the earlier `3/8`-tail diameter bound because it applies
to the previously unresolved large-atom head as well.  It does not rule out
productive canonical cuts: a corner may reduce the nonfixed half of the
hole family, and antipodal private edges explicitly improve by one.  It
rules out only the coefficient-one goal inside this one fixed-transposition
fibre.  Any successful route must change the coordinate bridge, recompute
ownership components after leaving this fibre, or start from a different
exact factor.

## 9. An averaged obstruction for coordinate bridges

The marked-gap certificates also show that the phenomenon is not confined
to the specially localized pair `(2 3)`.

Let

\[
 K=(2m-3)C_{m-2}
\]

be the total number of marked-gap certificate pairs.  A rank-`(m-1)`
target is fixed by exactly

\[
 \binom{m-1}{2}+\binom{m+2}{2}=m^2+2
\]

of the `binom(n,2)=m(2m+1)` coordinate transpositions.  Therefore, if
`K_fix(tau)` counts certificate pairs whose common target is fixed by
`tau`, double counting gives

\[
 \mathbb E_\tau K_{\rm fix}(\tau)
 =\alpha_mK,
 \qquad
 \alpha_m={m^2+2\over m(2m+1)}\longrightarrow{1\over2}.
\tag{9.1}
\]

For every transposition separately, disjoint pointed slots give
`D_fix(tau)>=K_fix(tau)`, while the fixed-target baseline proof of Section 5
is label-independent and gives

\[
 L_{\rm fix}(\tau)-N_1^{\rm fix}
 \le {2W\over m+2}.
\]

Hence

\[
 \boxed{
 \mathbb E_\tau M_{\rm fix}(\tau)
 \ge\alpha_m(2m-3)C_{m-2}-{2W\over m+2}
 =\left({1\over32}-o(1)\right)W.}
\tag{9.2}
\]

Moreover, since `0<=K_fix(tau)<=K`, the elementary bound

\[
 \Pr\{K_{\rm fix}(\tau)\ge\alpha_mK/2\}
 \ge{\alpha_m\over2-\alpha_m}
 ={1\over3}-o(1)
\tag{9.3}
\]

shows that at least `(1/3-o(1))` of all coordinate transpositions freeze

\[
 \left({1\over64}-o(1)\right)W
\]

canonical first-shadow holes throughout their complete component cubes.
Thus a successful adaptive bridge selector must be genuinely targeted; a
generic coordinate bridge has a linear frozen obstruction.
