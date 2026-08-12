# Bottom Boolean stars: Sapozhenko entropy versus the two-sample Hall tail

**Date:** 2026-08-05  
**Method:** direct two-sample hypergeometric Bernstein bound and an explicit
re-optimization of the approximation counts in Balogh--Garcia--Li,
Lemmas 7.1--7.3; no computation or search  
**Status:** exact scale audit.  The published container estimates do not prove
the required `O(H/m)` deficiency at density `p=Theta(m^{-1/2})`.  Even if one
grants drift-preserving reconstruction for free, the generic fingerprint
entropy exceeds the Hall-deviation exponent by a factor
`Theta(sqrt(m) log^2 m)` at the critical drift.  The audit identifies the
precise low-drift window where a new stability/entropy theorem is required.

## 1. Parameters

Let `M=B(2m-1,m)` be the `m`-regular incidence graph between

\[
 \mathcal R={ [2m-1]\choose m},\qquad
 \mathcal L={ [2m-1]\choose m-1},\qquad
 W=|\mathcal R|=|\mathcal L|.                              \tag{1.1}
\]

Choose independent uniform `H`-subsets `X_+ subseteq mathcal R` and
`X_- subseteq mathcal L`, where

\[
 p={H\over W}=\Theta(m^{-1/2}),\qquad
 s_0={H\over m}={pW\over m}.                               \tag{1.2}
\]

For a closed family `A subseteq mathcal R`, write

\[
 a=|A|,\qquad b=|N(A)|=a+t,\qquad
 D_A=|A\cap X_+|-|N(A)\cap X_-|.                           \tag{1.3}
\]

By symmetry one may restrict to `a<=W/2`.  The middle-level
Kruskal--Katona estimate gives

\[
                         t\ge {b\over2m},
 \qquad\text{hence}\qquad a\le 2mt.                        \tag{1.4}
\]

The desired bottom theorem is

\[
                         \max_A D_A=O(s_0).                 \tag{1.5}
\]

## 2. Exact fixed-cut deviation scale

### Lemma 2.1 (two-sample Bernstein bound)

There is an absolute `c>0` such that for every fixed `A` and every `u>=0`,

\[
 \Pr(D_A\ge u)
 \le
 \exp\!\left[
   -c\min\left{
       { (u+pt)^2\over p(a+b)},\ u+pt
   \right}
 \right].                                                  \tag{2.1}
\]

The same estimate, up to changing `c`, holds for Bernoulli sampling of each
shore with probability `p`.

#### Proof

The two sample counts in (1.3) are independent hypergeometric variables
with means `pa` and `pb`.  Sampling without replacement is dominated in
the exponential-moment order by sampling with replacement.  Apply the
standard Bernstein mgf estimate separately to the centred variables and
multiply their mgfs.  Their total variance proxy is at most `p(a+b)`, their
summands have absolute value at most one, and

\[
 D_A-\mathbb ED_A=D_A+pt.
\]

Bernstein's optimization gives (2.1). \(\square\)

At the requested threshold `u=C s_0`, define the fixed-cut exponent

\[
 \Psi(a,t)=c\min\left\{
 {p^2(t+W/m)^2\over p(a+t)},\ p(t+W/m)
 \right\}.                                                 \tag{2.2}
\]

At the worst critical scale

\[
                         a=\Theta(W),\qquad t=\Theta(W/m), \tag{2.3}
\]

this is

\[
                         \Psi(a,t)=\Theta\!\left({W\over m^{5/2}}\right)
                                  =\Theta(H/m^2).           \tag{2.4}
\]

This is the probability budget available for union-bounding containers at
the hardest scale.

## 3. What Lemmas 7.1--7.2 actually cost

Use the notation of Balogh--Garcia--Li with base degree `m`, and choose their
coarse parameter

\[
                         \varphi=m/2.                       \tag{3.1}
\]

The middle-level estimate `m_varphi>=m^2/12` applies.  Their Lemma 7.1 then
gives coarse approximations `(F^*,S^*)`, and Lemma 7.2 refines them with
parameter `1<=psi<m`.  Substitution into their displayed bounds gives

\[
 \boxed{
 \log \#\{\text{fingerprints at fixed }(a,b)\}
 \le
 C\left(
 {t\log^2m\over m}+{t\log m\over\psi}
 \right)+O(\log W).
 }
 \tag{3.2}
\]

Here the term `b log^2(m)/m^2` from the coarse approximation was absorbed
using `b<=2mt`, and all binomial-choice terms are bounded by the first term
on the right.  The resulting strong pair satisfies

\[
 A\subseteq S,\qquad F\subseteq N(A),\qquad
 |S|\le |F|+{2t\psi\over m-\psi}.                          \tag{3.3}
\]

Two cautions are essential.

1. Equation (3.2) counts fingerprints, not exact closed families.
   Reconstruction still has to retain the negative mean `-pt`; replacing
   `A,N(A)` merely by `S,F` loses that drift through (3.3).
2. Consequently, comparing (3.2) directly with (2.2) is an *optimistic*
   audit: it grants drift-preserving reconstruction at zero additional
   entropy.  Failure of even this optimistic comparison is a rigorous
   obstruction to the proposed use of the published lemmas.

## 4. The critical mismatch

At (2.3), the best possible first term in (3.2) is

\[
                         \Theta\!\left({W\log^2m\over m^2}\right),
 \tag{4.1}
\]

whereas the complete fixed-cut deviation exponent is only (2.4).  Their
ratio is

\[
 {W\log^2m/m^2\over W/m^{5/2}}
                         =\Theta(\sqrt m\log^2m).           \tag{4.2}
\]

Thus Lemmas 7.1--7.2 miss the desired union bound by a polynomial factor,
not by a removable constant or one logarithm.

The newer iterative container theorem of Jenssen--Malekshahian--Park has
the same diagnostic boundary.  Its reconstruction gain is of order

\[
                         {\lambda t\over\sqrt m},           \tag{4.3}
\]

while its generic fingerprint cost is `O(t log^2(m)/m)`.  It therefore
requires

\[
                         \lambda\gg {\log^2m\over\sqrt m}. \tag{4.4}
\]

Our density/activity scale is `lambda asymp p asymp m^{-1/2}`, missing
exactly the `log^2 m` factor.  This agrees with (4.2).

## 5. Scale-by-scale optimistic comparison

Ignoring reconstruction as above and retaining only the leading generic
fingerprint entropy

\[
                         K(t)=C{t\log^2m\over m},           \tag{5.1}
\]

gives a precise split.

### 5.1 Drift at least the target: `t>=W/m`

Using (1.4) in (2.2),

\[
 \Psi(a,t)
 \ge c{p t^2\over a+t}
 \ge c'{pt\over m}
 =\Theta\!\left({t\over m^{3/2}}\right).                  \tag{5.2}
\]

Therefore

\[
                         {K(t)\over\Psi(a,t)}
                         =O(\sqrt m\log^2m).                \tag{5.3}
\]

The mismatch persists uniformly throughout this entire drift range.

### 5.2 Drift below the target: `t<=W/m`

Now `s_0` dominates.  Again from (1.4),

\[
 \Psi(a,t)
 \ge c{p(W/m)^2\over mt}
 =c'{W^2\over m^{7/2}t}.                                   \tag{5.4}
\]

The optimistic inequality `Psi>>K` holds only when

\[
                         t\ll {W\over m^{5/4}\log m}.       \tag{5.5}
\]

Hence the unresolved low-drift window already begins at

\[
 {W\over m^{5/4}\log m}
 \lesssim t\lesssim {W\over m},                            \tag{5.6}
\]

and continues through all larger drifts unless additional structural
information reduces the catalogue entropy.

Equation (5.5) is only a necessary entropy comparison, not a completed
proof in the smaller range, because exact reconstruction has not been paid.

## 6. Why ordinary weighted reconstruction cannot simply be imported

Balogh--Garcia--Li Lemma 7.3 controls the hard-core weight

\[
                         {\lambda^{|A|}\over(1+\lambda)^{|N(A)|}}. \tag{6.1}
\]

Our Hall event instead compares two independently sampled counts:

\[
                         |A\cap X_+|-|N(A)\cap X_-|.        \tag{6.2}
\]

For a fixed cut its moment generating function is

\[
 (1-p+pe^\theta)^a(1-p+pe^{-\theta})^b,                    \tag{6.3}
\]

which cannot be written as (6.1) with one activity without an additional
factor carrying the variance term.  Moreover a Hall witness may retain many
sampled vertices in `N(A)`; hard-core weight corresponds to forbidding all of
them.  Thus Lemma 7.3 is not a black-box reconstruction theorem for (6.2).

Any successful adaptation must preserve both the deterministic drift `pt`
and the two-sample variance in (2.1).

## 7. What the threshold counterexample teaches

The moderate-deviation threshold cuts in

`MATH_THEOREM_BOTTOM_STAR_JUNTA_CONTAINER_COUNTEREXAMPLE_AND_ENTROPY_REPLACEMENT_20260805.md`

have

\[
                         t=\Theta(W/m)                      \tag{7.1}
\]

but are not approximable, to `O(W/m)` error, by any
`O(sqrt m)`-coordinate junta.  Nevertheless their complete catalogue has
only `(2m+1)2^(2m-1)` members, whose logarithm is `O(m)`, vastly below
(2.4).  They therefore satisfy the sharp empirical bound by a direct union
bound.

This shows that the missing improvement cannot be phrased solely as
Kruskal--Katona stability toward small juntas.  A valid theorem must admit
high-coordinate, low-entropy shapes as first-class containers.

## 8. Exact remaining theorem

A sufficient statement is the following.

### Drift-sensitive paired entropy theorem

For every `(a,t)` there is a catalogue `C(a,t)` of paired approximants such
that:

1. every closed 2-linked `A` with `|A|=a` and
   `|N(A)|=a+t` maps to one member of `C(a,t)`;
2. reconstruction preserves the random Hall score up to `O(H/m)` rather
   than replacing it by a one-sided container score;
3. its logarithmic size plus reconstruction entropy is `o(Psi(a,t))`, with
   `Psi` as in (2.2), except for explicitly listed structured catalogues
   which are balanced directly.

This theorem, together with Lemma 2.1 and decomposition into 2-linked
components, would prove

\[
                         \operatorname{def}(X_-,X_+)=O(H/m). \tag{8.1}
\]

The exact numerical bottleneck is now certified:

\[
 \boxed{
 \text{generic entropy }{t\log^2m\over m}
 \quad\hbox{versus}\quad
 \text{critical Hall exponent }{W\over m^{5/2}}.
 }
 \tag{8.2}

At `t=Theta(W/m)`, the generic entropy must improve by a factor
`Omega(sqrt m log^2 m)`, or the corresponding cuts must be split into
special low-entropy shape classes.  That is the exact unresolved bottom
Boolean-star row.

## 9. Relation to the random-Sperner frontier

For equal samples of size `H`, Kőnig's theorem gives the exact identity

\[
 \alpha\bigl(M[X_-\cup X_+]\bigr)
 =H+\operatorname{def}(X_-,X_+),                            \tag{9.1}
\]

where `alpha` is the independence number.  Thus (8.1) is the quantitative
random-Sperner assertion

\[
 \alpha\bigl(M[X_-\cup X_+]\bigr)
                         \le H+O(H/m)                       \tag{9.2}
\]

at site density `p=Theta(m^{-1/2})`.

The general random version of Sperner's theorem proves only a
`(1+o(1))H` bound when `pm->infinity`; it does not provide the `O(1/m)`
relative error in (9.2).  The sharper middle-two-layer container results
which classify maximum antichains have historically required constant
`p`.  The 2026 iterative-container improvement reaches the structured
hard-core regime at

\[
                         p\gtrsim {\log^2m\over\sqrt m},    \tag{9.3}
\]

whereas (1.2) is smaller by `log^2 m`.

Therefore (8.1) is not a routine corollary of an existing random-Sperner
theorem.  It sits exactly at a current container-method threshold.  For the
OR-word construction this makes a correlated choice of the skeleton and
owner banks mathematically attractive: a deletion-coupled bank carries a
perfect containment matching by construction, while independent banks force
the new quantitative random-Sperner theorem (9.2).
