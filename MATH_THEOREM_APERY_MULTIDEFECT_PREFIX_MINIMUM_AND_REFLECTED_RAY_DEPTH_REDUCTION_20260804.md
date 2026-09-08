# Multidefect cyclic Apéry clocks: prefix minima and the reflected-ray depth scalar

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  For every honest
cyclic Apéry table it proves that the distinguished prefix is the minimum
cyclic block of each length and gives an exact subadditive-deficit
parametrization.  At exact first carry it reduces every still-possible
nonpositive multidefect clock to one explicit integer overlap scalar and one
ray-length scalar.  It closes the overlap-depth-at-most-two chamber under a
natural terminal-coverage condition.  It does not prove that every
multidefect word lies in that chamber, universal Bellman positivity, or an
OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2}.
\]

Let

\[
 0=s_0<s_1<\cdots<s_{h-1}<P,
 \qquad h\ge3,
\tag{0.1}
\]

be an honest cyclic Apéry table:

\[
 \begin{aligned}
  s_{r+t}&\ge s_r+s_t &&(r+t<h),\\
  P+s_{r+t-h}&\ge s_r+s_t &&(r+t\ge h).
 \end{aligned}
\tag{0.2}
\]

Write its cyclic gaps as

\[
 \gamma_1=s_1,\qquad
 \gamma_j=s_j-s_{j-1}\ (2\le j<h),
 \qquad \gamma_h=P-s_{h-1}.
\tag{0.3}
\]

Its exact periodic Bellman clock is

\[
                         W_{qh+r}=qP+s_r.
\tag{0.4}
\]

## 1. Every prefix is a minimum cyclic block

Set `s_h=P`.  For `0<=r<h` and `1<=t<=h`, let `B_(r,t)` be the sum
of the `t` cyclic gaps beginning immediately after residue `r`.  Thus

\[
 B_{r,t}=
 \begin{cases}
  s_{r+t}-s_r,&r+t<h,\\
  P+s_{r+t-h}-s_r,&r+t\ge h.
 \end{cases}
\tag{1.1}
\]

### Theorem 1.1 (cyclic prefix-minimum theorem)

For every `r,t`,

\[
                         \boxed{B_{r,t}\ge s_t.}
\tag{1.2}
\]

Consequently, with `p=P/h`,

\[
                         \boxed{s_t\le tp\qquad(0\le t<h).}
\tag{1.3}
\]

In particular every gap satisfies

\[
                         \boxed{\gamma_j\ge\gamma_1.}
\tag{1.4}
\]

#### Proof

For `1<=t<h`, equation (1.2) is exactly (0.2), rearranged.  For `t=h`,
one has the literal identity `B_(r,h)=P=s_h`.  Summing `B_(r,t)` over all
`h` starting residues counts every cyclic gap exactly `t` times, so

\[
 h s_t\le\sum_{r=0}^{h-1}B_{r,t}=tP.
\]

This proves (1.3).  Taking `t=1` in (1.2) proves (1.4). \(\square\)

There is an exact deficit form.  Put

\[
 d_t=tp-s_t\quad(0\le t<h),
 \qquad d_0=0.
\tag{1.5}
\]

Then `d_t>=0`, and (0.2) is equivalent to cyclic subadditivity

\[
 \boxed{
 d_{(r+t)\bmod h}\le d_r+d_t
 \qquad(0\le r,t<h).}
\tag{1.6}
\]

Moreover, on setting `d_h=d_0=0`,

\[
 \boxed{
 \gamma_j=p-(d_j-d_{j-1})
 \qquad(1\le j\le h).}
\tag{1.7}
\]

Thus a general multidefect Apéry word is precisely a positive-gap cyclic
subadditive deficit profile.  This replaces an unstructured list of gaps
by one exact scalar gauge on `Z/hZ`; it does not assert that this cone has
only one-defect extreme rays.

## 2. Exact-first-carry endpoint comparison

Assume from now on that the first threshold crossing is the exact first
carry:

\[
                         P+s_1=A.
\tag{2.1}
\]

Put

\[
                         a=s_1,\qquad \alpha={a\over A}.
\tag{2.2}
\]

The prefix-average bound (1.3) gives `a<=P/h`; using `P+a=A`,

\[
                         0<\alpha\le {1\over h+1}< {1\over2}.
\tag{2.2a}
\]

For the threshold-period train define

\[
 F(w)=\sum_{q\ge0}K(qA+w),\qquad
 C=F(0),\qquad
 f(t)=F(At),\qquad
 g(t)=\rho(At).
\tag{2.3}
\]

The authenticated analytic bounds are

\[
 C>{43\over1000},\qquad
 0<f(t)<{61\over1000}\quad(0\le t\le1/2),
\tag{2.4}
\]

\[
 F(w)+F(A-w)=\rho(w),\qquad
 |g(t)|<{1\over20000}.
\tag{2.5}
\]

The compact train `f` is one-mode on `[0,1/2]`: it is monotone, or it
increases to one maximum and then decreases.  The complete theta error
`g` is strictly increasing there and has zero half-interval mean:

\[
 g'(t)>0\quad(0<t<1/2),\qquad
 \int_0^{1/2}g(t)\,dt=0,\qquad g(1/2)>0.
\tag{2.6}
\]

The exact first carry is itself a legal size-`h+1` configuration of value
`A`.  Hence at capacity `(h+1)q+r`, use `q` such configurations and the
displayed residue-`r` generator.  At `q=0` this is equality; at `q>=1`
both values lie in the increasing Gaussian tail.  Therefore

\[
 \boxed{
 \Phi(W)\ge E(s):=
 C+\sum_{r=1}^{h-1}F(s_r)+F(P).}
\tag{2.7}
\]

No availability cell or finite correction is omitted in this comparison.

## 3. The two reflected rays

Let `u` be the number of shifts strictly above the midpoint:

\[
 s_{h-u-1}\le {A\over2}
 <s_{h-u}<\cdots<s_{h-1},
\tag{3.1}
\]

with the evident interpretation `u=0` if every shift is at most `A/2`.

If `u=0`, then (2.4)--(2.5) immediately give

\[
 E(s)> {43\over1000}-{1\over20000}>0.
\tag{3.2}
\]

Assume below that `u>=1`.  For `1<=i<=u`, define the normalized early and
reflected late rays

\[
 X_i={s_{i+1}\over A},
 \qquad
 Y_i={A-s_{h-i}\over A}.
\tag{3.3}
\]

The carry inequality with indices `i+1` and `h-i` gives

\[
 s_{i+1}+s_{h-i}\le P+s_1=A,
\]

and hence

\[
                         \boxed{0<X_i\le Y_i<1/2.}
\tag{3.4}
\]

Since `X_u<1/2<s_(h-u)/A`, strict increase also gives
`u+1<h-u`; the early and late rays are disjoint.

The minimum-gap theorem gives a second exact constraint.  Since

\[
 A-s_{h-1}=a+\gamma_h\ge2a
\]

and

\[
 (A-s_{h-i-1})-(A-s_{h-i})=\gamma_{h-i}\ge a,
\]

one has

\[
                         \boxed{Y_i\ge(i+1)\alpha.}
\tag{3.5}
\]

The theta error is symmetric, `rho(A-w)=rho(w)`.  Reflecting every upper
shift in (2.7), and pairing it with the indicated early shift, gives the
exact identity

\[
\boxed{
\begin{aligned}
 E(s)={}&C+\Theta+T+
 \sum_{r=u+2}^{h-u-1}f(s_r/A),\\
 \Theta={}&g(\alpha)+\sum_{i=1}^{u}g(Y_i),\\
 T={}&\sum_{i=1}^{u}\bigl(f(X_i)-f(Y_i)\bigr).
\end{aligned}}
\tag{3.6}
\]

The final middle sum is nonnegative by (2.4).  Thus all multidefect
dependence relevant to this lower comparison has collapsed to two
ordered rays.

## 4. The compact transport-depth scalar

Define the interval-overlap function and its integer depth by

\[
 D(t)=\#\{i:X_i\le t<Y_i\},
 \qquad
 H=\max_{0\le t\le1/2}D(t).
\tag{4.1}
\]

Since `f` is differentiable,

\[
 T=-\int_0^{1/2} f'(t)D(t)\,dt.
\tag{4.2}
\]

Where `f'<=0`, the integrand in (4.2) is nonnegative.  The one-mode
property implies that the total positive variation of `f` is at most

\[
                         \sup f-f(0)<{61\over1000}-C.
\]

Therefore

\[
 \boxed{
 T\ge-H(\sup f-C)
 \ge-H\left({61\over1000}-C\right).}
\tag{4.3}
\]

The second inequality is strict when `H>0`; its weak form is written so
that the harmless case `H=0` is also literal.

This is the desired uncrossing substitute: arbitrary many literal gap
defects cost only their maximum reflected-ray overlap depth, not their
number.

## 5. The theta ray and a complete scalar gate

The crude theta bound is

\[
                         \Theta>-{u+1\over20000}.
\tag{5.1}
\]

There is a period-independent improvement whenever the forced arithmetic
minorant reaches within one mesh of the midpoint:

\[
                         (u+2)\alpha\ge {1\over2}.
\tag{5.2}
\]

Indeed, (3.5) and monotonicity of `g` give

\[
 \Theta\ge\sum_{j=1}^{u+1}g(j\alpha).
\tag{5.3}
\]

Also `(u+1)alpha<=Y_u<1/2`.  Right-endpoint quadrature and the zero-mean
tail property from (2.6) give

\[
 \alpha\sum_{j=1}^{u+1}g(j\alpha)
 \ge\int_0^{(u+1)\alpha}g(t)\,dt
 \ge-\left({1\over2}-(u+1)\alpha\right)g(1/2).
\tag{5.4}
\]

Under (5.2), the terminal gap in (5.4) is at most `alpha`.  Thus

\[
                         \boxed{\Theta\ge-g(1/2)>-{1\over20000}.}
\tag{5.5}
\]

Define

\[
 \tau=
 \begin{cases}
  1,&(u+2)\alpha\ge1/2,\\
  u+1,&(u+2)\alpha<1/2.
 \end{cases}
\tag{5.6}
\]

Combining (2.4), (3.6), (4.3), (5.1), and (5.5) yields the complete
two-scalar bound

\[
\boxed{
 \Phi(W)\ge E(s)>
 {860-360H-\tau\over20000}.}
\tag{5.7}
\]

### Theorem 5.1 (reflected-ray depth closure)

If

\[
                         \boxed{360H+\tau\le860,}
\tag{5.8}
\]

then

\[
                         \boxed{\Phi(W)>0.}
\tag{5.9}
\]

In particular, every exact-first-carry cyclic Apéry clock satisfying

\[
 H\le2,\qquad (u+2)a\ge {A\over2}
\tag{5.10}
\]

is strictly positive, with the uniform endpoint-comparison margin

\[
                         E(s)>{139\over20000}.
\tag{5.11}
\]

Without (5.2), depth two still closes every `u<=139`; depth one closes
every `u<=499`.

## 6. Consequence after the one-defect closure

The uniform, short-first, and long-wrap one-defect clocks at exact first
carry are all positive: the first two by the audited arithmetic/affine
theorems, and the last by the all-period monotone-quadrature theorem.

Consequently, if an exact-first-carry formal cyclic clock is nonpositive,
then all of the following are necessary:

1. its cyclic gap word is genuinely multidefect;
2. `u>=1`;
3. its reflected-ray scalars obey

   \[
                         \boxed{360H+\tau>860.}
   \tag{6.1}
   \]

In particular, a counterexample whose arithmetic minorant reaches the
midpoint as in (5.2) must have

\[
                         \boxed{H\ge3.}
\tag{6.2}
\]

If (5.2) fails, then a depth-two counterexample must have `u>=140`, and a
depth-one counterexample must have `u>=500`.

Since `u+1<h-u`, these two residual cases also require respectively

\[
                         h\ge282,
 \qquad\text{or}\qquad h\ge1002.
\tag{6.3}
\]

Thus the first irreducible multidefect obstruction is no longer an
arbitrary gap word.  It is exactly a high-multiplicity overlap of the
reflection intervals, or a quantitatively short reflected theta ray.  The
theorem does not prove that these residual geometries are realizable, nor
does it sign them.

## 7. Scope and frozen dependencies

The result is confined to the pure periodic formal clock at exact first
carry.  It does not address threshold overshoot, later first crossing, the
finite shoulder between an original physical clock and its formal Apéry
clock, or the endpoint-critical branch of the all-grid trichotomy.

| role | file | SHA-256 |
|---|---|---|
| honest cyclic Apéry table and exact formal clock | `MATH_THEOREM_APERY_SHIFT_CYCLIC_SUPERADDITIVITY_AND_TAIL_RECURSION_20260804.md` | `324f040f5604767fc867c78806c8a7ab7524d6ed82cabe77bc3e2e0ea36121ba` |
| one-defect classification and affine/broad closure | `MATH_THEOREM_APERY_ONE_DEFECT_GAP_CLASSIFICATION_AND_AFFINE_EXCLUSION_20260804.md` | `9b7b3f459d979205d111fe0be1f2e21ba3ce783056b16fd021716e841f67622e` |
| Euclidean compact-train bounds and one-mode theorem | `MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md` | `7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738` |
| all-period long-wrap closure and theta monotonicity | `MATH_THEOREM_APERY_LONG_WRAP_MONOTONE_QUADRATURE_ALL_PERIOD_CLOSURE_20260804.md` | `24f440d2b516618f7798b5f4e053de0f5b3253ad1825e7685e2494bddacf8ecd` |
| independent audit of all-period long-wrap theorem | `MATH_AUDIT_APERY_LONG_WRAP_MONOTONE_QUADRATURE_ALL_PERIOD_CLOSURE_INDEPENDENT_20260804.md` | `ab249d01d769f42e9ca26cf17d4170397b021fe5d0714e3e20127d57a614a85b` |
