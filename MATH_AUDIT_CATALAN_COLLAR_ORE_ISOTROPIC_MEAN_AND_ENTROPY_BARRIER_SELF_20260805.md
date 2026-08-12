# Self-audit: Catalan-collar protected-Ore mean and entropy barrier

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_CATALAN_COLLAR_ORE_ISOTROPIC_MEAN_AND_ENTROPY_BARRIER_20260805.md`  
**Method:** independent symbolic recount; no computation or search

## 1. Full Johnson-edge mass

For one lower colour `q notin A`, its `m` extensions form `K_m`.  Each
extension in `N(A)` occurs in `m-1` of those edges, so its contribution is

\[
                         (m-1)d_N(q).
\]

Summing over `q notin A` gives `(m-1)e(N,L-A)`.  Since every incidence
out of `A` ends in `N(A)`, balanced `m`-regularity gives

\[
 e(N,L-A)=m|N|-m|A|=m\delta(A).
\]

Thus the exact total is `m(m-1)delta(A)`.  Dividing by
`Wm(m-1)/2` gives `2delta(A)/W`.  No factor two is missing.

The frozen identity

\[
 (m-1)\sigma=(m-2)\delta+\beta
\]

then gives the stated isotropic ratio

\[
 {\mathbb E c_P(A)\over\sigma(A)}
 \le {2b\ell(m-1)\over W(m-2)}=\Theta(m^{-1/2}).
\]

## 2. Orbit average and invariance

The action of `S_n` is transitive on Johnson edges and obeys

\[
                         w_{\pi A}(e)=w_A(\pi^{-1}e).
\]

Hence averaging `c_P(pi A)` over `pi` gives `2Edelta/W` for every fixed
bank with `E` edges.  The maximum violation is unchanged because
`A -> pi A` is a bijection.  Therefore the note correctly distinguishes
orbitwise mean from an all-cut relabelling theorem.

## 3. Exact thinning tail

For an exact `b`-subset of `M` blocks, inclusion indicators are negatively
associated.  With `0<=z_i<=L`,

\[
 \mathbb E e^{\theta\sum z_iI_i}
 \le\prod_i(1-p+pe^{\theta z_i})
 \le\exp\left({p\sum z_i\over L}(e^{\theta L}-1)\right).
\]

Optimization at `e^(theta L)=y/(p sum z_i)` gives

\[
 \Pr(S\ge y)
 \le\exp\left[-{y\over L}\log{y\over p\sum z_i}
               +{y-p\sum z_i\over L}\right]
 \le\left({ep\sum z_i\over y}\right)^{y/L}.
\]

Taking `L=2ell` verifies Theorem 3.1.

## 4. Principal-star formulas

For `|R|=j<=m-2`,

\[
 |A_R|={n-j\choose m-1-j},\qquad
 N_j={n-j\choose m-j},\qquad
 |A_R|={m-j\over m}N_j.
\]

Every shadow owner has `m-j>=2` selected facets, so

\[
                         \delta={j\over m}N_j,qquad
                         \sigma={2j\over m}N_j.
\]

For one Johnson edge `q+a,q+b`, a principal star contributes at the first
endpoint exactly for `R={a} union T`, `T in binom(q,j-1)`, and analogously
for `b`.  The two families are disjoint, proving the exact mass
`2 binom(m-1,j-1)`.

On the internal geodesic, `R subseteq M_t` is equivalent to all required
entering indices having arrived and no required deletion index having
departed.  Its truth set is therefore an interval in `t`.  It changes at
most twice internally and at most once at each seam, proving the sharper
aperture `min(2j,4)`.

Using

\[
 {n\choose j}{n-j\choose m-j}=W{m\choose j}
\]

gives total slack `2W binom(m-1,j-1)`, so the aggregate charge/slack ratio
is exactly `E/W`.

For `j=1`, a balanced collar exchanges each coordinate at most twice.
Therefore `c<=2b`, while

\[
 \sigma={2W\over2m-1}=2\operatorname{Cat}_{m-1},
 \qquad b=\operatorname{Cat}_{m-1}-1.
\]

The strict two-unit reserve is correct.

For a union of `g` principal stars, if a lower colour is outside the union,
then every centre witnessing an endpoint disappears across that edge;
otherwise it would lie in the common lower colour.  Thus the edge weight is
at most the sum of the `g` centre-indicator variations.  Each variation is
at most four on one collar, proving the `4g` multi-centre aperture.  With
`(2^n)^g` descriptions and isotropic row energy, the displayed exponent is
`O(mg)-Omega(m log(m)/g)`, negative exactly in the stated
`g^2=o(log m)` regime.

The aperture four is valid throughout the principal hierarchy, while the
unrestricted aperture `2ell` is genuinely attained on a support cut:
fixing one outside coordinate `y` in every owner and performing every
collar exchange inside a support `S` makes every lower colour contain `y`
and every owner lose `y` to an `(m-1)`-set in `S`.  Hence every edge has
weight two.  The support has exactly enough fresh labels when
`|S|=m+h`, including the right seam label.

## 5. Entropy and junta scope

At isotropic block scale, the tail exponent is

\[
 {\sigma\over2\ell}
 \left({1\over2}\log m+O(1)\right).
\]

The frozen connected-set count has exponent
`4t log m+O(m)`.  Its direct size-stratum union bound therefore asks for
`sigma>(16+o(1))ell t`.  The connected partial-colex family with
`sigma<6t` proves only that this **proof package** cannot close; it does
not refute collar cut-thinness.  The theorem note states this scope
explicitly.

For one toggled lower vertex, at most `m` upper-shadow vertices change,
each of protected degree at most two, and `D_P(A)` changes by at most two.
Thus `|Delta c|<=2m+2`.  The capped slack changes by at most `m+2`, giving
the displayed `(3m+4)` Lipschitz bound.  An approximate junta at constant
Hamming error cannot preserve a unit integral margin; an exact or
margin-sensitive container is genuinely required.

## 6. Verdict

All promoted identities, constants, and strict inequalities rederive.
The note is a theorem/reduction and a scoped method no-go.  It does **not**
claim protected factor extension, a global cut container, residence,
deeper shadows, or compiler feasibility.

**Audit verdict: GO.**
