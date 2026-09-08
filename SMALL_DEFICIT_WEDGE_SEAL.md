# Quantitative wedge-cover seal with positive edge and gap deficit

## 1. Outcome

Let the selected dangerous plateau length moment at the bottom threshold be

\[
\ell=3-\delta,
\]

and assume the exact gap budget

\[
\int z\,d\rho\le\delta.
\]

For every full-line-realizable limiting ledger,

\[
\boxed{
U(1^+)\le {15\over4}
          +{5\over4}\sqrt{6\delta}
          +{3\over2}\delta.}                               \tag{1.1}
\]

Consequently

\[
U(1^+)<4
\]

whenever

\[
0\le\delta<\delta_0,
\qquad
\boxed{\delta_0={ (\sqrt{29}-5)^2\over24}}
=0.0061813303606\ldots .                                    \tag{1.2}
\]

This strictly extends the zero-gap theorem
`FULL_LINE_WEDGE_COVER_SEAL.md`.

## 2. Sharp square-root cover error

Let `D_a` be the number of middle-hexagon points missed by the selected
complete coordinate lines.  The selected plateau vertex union contains at
least the sum of the disjoint plateau edge lengths.  Therefore

\[
{D_a\over a^2}\le\delta+o(1).                               \tag{2.1}
\]

Use the notation `P_a,N_a` for selected positive and negative level counts.
For direction `i`, let `R_i` be the number of unselected positive levels and
let `n_i` be its selected negative count.  Put

\[
q_i=(R_i-(N_a-n_i))_+.
\]

The wedge-slice argument of `FULL_LINE_WEDGE_COVER_SEAL.md` can be summed
without introducing an arbitrary cutoff.  Among `R_i` missing positive
levels, the smallest possible uncovered-slice excesses are

\[
0,1,\ldots,q_i-1.
\]

The three open sign wedges are disjoint, so

\[
D_a\ge\sum_i {q_i\choose2}.                                 \tag{2.2}
\]

Writing `Q=sum_i q_i`, convexity gives

\[
D_a\ge {Q^2\over6}-{Q\over2}.                               \tag{2.3}
\]

Also

\[
3a-P_a=\sum_iR_i\le2N_a+Q.
\]

After division by `a`, (2.1)--(2.3) yield

\[
3-P-2N\le\sqrt{6\delta}.                                   \tag{2.4}
\]

Since `P+N=f`,

\[
P\le2f-3+\varepsilon,
\qquad
\varepsilon=\sqrt{6\delta}.                                \tag{2.5}
\]

Every absorbed successor uses a distinct positive selected line, hence

\[
A\le2f-3+\varepsilon.                                      \tag{2.6}
\]

## 3. Two bounds for the absorbed base value

Put

\[
C=\int_\alpha(p+s-1).
\]

Absorption legality gives `p+s-1<=2`, so

\[
C\le2A\le4f-6+2\varepsilon.                                \tag{3.1}
\]

The complete predecessor and successor marginals have mass `f` and first
moment `3-delta`.  Therefore

\[
\int_\rho(p-1)=\int_\rho(s-1)=3-\delta-f.
\]

Together with (2.6),

\[
C\le A+2(3-\delta-f)
\le3-2\delta+\varepsilon.                                  \tag{3.2}
\]

## 4. Exact three-times-gap bound

Recall

\[
\phi(p,s,z)=\min\{p,(4-s-z)_+\}(s-z)_+,
\]

and write

\[
h(s,z)=(s-1)\min\{z,4-s\}
\]

for the bottom-threshold seam term.

### Lemma 4.1

For `1<=p,s<=2` and `z>=0`,

\[
\phi(p,s,z)+(4-s)z\ge p+s-1.                               \tag{4.1}
\]

#### Proof

Put `q=4-p-s>=0`.

If `0<=z<=q`, then `phi=p(s-z)`, and the left side of (4.1)
minus its right side is

\[
(p-1)(s-1)+qz\ge0.
\]

If `q<z<s`, then `phi=(4-s-z)(s-z)`.  Using `p<=2`, the same difference is
at least

\[
z^2-sz+3s-s^2-1.
\]

Its minimum over `0<=z<=s` is

\[
3s-{5s^2\over4}-1\ge0
\]

for `1<=s<=2`.  Finally, if `z>=s`, then `phi=0` and

\[
(4-s)z\ge s(4-s)\ge p+s-1.
\]

This proves (4.1).  QED.

For a nonabsorbed seam, (4.1) and `h<=(s-1)z` give

\[
h+(p+s-1)-\phi\le3z.                                      \tag{4.2}
\]

For an absorbed seam, only `h` remains and `h<=z<=3z`.
Consequently the total positive-gap correction is at most

\[
3\int z\,d\rho\le3\delta.                                 \tag{4.3}
\]

The coefficient three is pointwise sharp at `p=s=2,z=1`.

## 5. Optimization

The exact seam algebra, split into absorbed and nonabsorbed edges, gives

\[
U(1^+)\le3-f+C+3\delta.                                    \tag{5.1}
\]

Substitute (3.1)--(3.2):

\[
U(1^+)\le3-f+3\delta+
\min\{4f-6+2\varepsilon,,3-2\delta+\varepsilon\}.         \tag{5.2}
\]

The first affine branch increases with `f` after the outside `-f` term and
the second decreases.  Their intersection is

\[
f_0={9-2\delta-\varepsilon\over4}.
\]

Evaluation at the intersection yields

\[
U(1^+)\le {15\over4}+{5\over4}\varepsilon
                         +{3\over2}\delta,
\]

which is (1.1).

Finally, (1.1) is strictly below four exactly when

\[
5\sqrt{6\delta}+6\delta<1.
\]

With `x=sqrt(6delta)`, this is `x^2+5x<1`, proving (1.2).

## 6. Scope

The theorem handles every full-line profile with bottom-threshold edge
deficit below `0.00618133`, including its exact positive-gap correction.
It does not yet control fixed deficits at or above `delta_0`.  Closing that
remaining range requires either a stronger cover/length coupling or the
common-threshold lifetime/coarea constraints, rather than a sharper
pointwise gap estimate (whose coefficient three is already exact).
