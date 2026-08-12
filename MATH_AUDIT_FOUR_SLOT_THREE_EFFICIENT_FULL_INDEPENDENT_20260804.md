# Independent audit: four-slot three-efficient pulse normal forms

**Date:** 2026-08-04  
**Verdict:** **PASS** for every exact reduction, normalized positive face,
period-monotonicity statement, and boundary-surface reduction actually
claimed in the audited theorem.  The full three-efficient regime remains
open.  
**Method:** pure algebra, calculus, and exact rational arithmetic only; no
search, SAT/CP solver, H100, or floating-point sign decision was used.

## 1. Frozen inputs and scope

Audited theorem:

`MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_PULSE_NORMAL_FORMS_20260804.md`

SHA-256:

`b620128fdefd9063099a6e1032c1685d155ba9aa95bab96b0e49612c11987faf`

Independent exact-rational replay:

`scratch/n4_three_efficient_independent_audit_20260804/exact_rational_replay.py`

SHA-256:

`a3bb2e0348a4f164bec0a0a7fd58a5d3d07bfb77c476d78db39209ac38d62da3`

The replay uses `fractions.Fraction` for every sign assertion and prints
`PASS: exact rational replay`.

This note is an audit of a reduction theorem.  It does **not** promote the
remaining `w=y` boundary functions or the remaining `w=2u` five-pulse
system to positive theorems.

## 2. Kernel monotonicity

For `x=At`, direct differentiation gives

\[
 K'(At)=2A\bigl(h(1+t)-h(1-t)\bigr),
 \qquad h(s)=s e^{-\pi s^2/4}.
\]

The logarithmic ratio is

\[
 f(t)=\log {h(1-t)\over h(1+t)}
 =\pi t-2\operatorname {arctanh}t.
\]

On `[0,2/3]`,

\[
 f''(t)=-{4t\over(1-t^2)^2}\le0,
\]

while `f(0)=0` and

\[
 f(2/3)=2\pi/3-\log5>0
\]

from the elementary strict inequalities `pi>3` and `e^2>5`.  Concavity
places `f` above its endpoint chord.  Thus `K` is decreasing on the exact
interval asserted in Lemma 1.1.

Since `K(v)=sigma([v,infinity))`, the signed interval identity

\[
 K(a)-K(b)=\sigma([a,b))
\]

is valid for every ordered pair `a<=b`, including intervals wholly in the
negative Gaussian tail.

## 3. Exact split into the two faces

By definition `w=max(y,2u)`, so the two closed faces `w=y` and `w=2u`
cover the regime and overlap only when `y=2u`.

### 3.1 The face `w=y`

Here `y>=2u`.  Since `x<=u`,

\[
 u+x\le2u\le y,
\]

and hence `v=max(y,u+x)=y`.  Both the `K(y)-K(w)` transient and the
far-tail `K(z+v)-K(z+w)` transient vanish.  Formula (2.1) follows exactly.

The gap inequalities are

\[
 u\le y-u\le z-y.
\]

The first is `y>=2u`; the second is exactly the inherited condition
`z+u=T>=2y`.  There is no missing orientation assumption.

### 3.2 The face `w=2u`

Here `y<=2u`, while `x<=u` and `v<=w=2u`.  Thus all three intervals in
(3.1) have the displayed left-to-right orientation.  At the overlap
`y=2u`, the second interval is empty; moreover `v=2u`, so the third is
empty too.  Formulas (2.1) and (3.1) consequently agree on the overlap.

## 4. Normalized positive faces

On `w=y`, the effective table `(0,u,y,z)` satisfies

\[
 y\ge2u,\qquad z\ge u+y,
 \qquad3y\le2z,qquad2y-z\le u.
\]

The last two inequalities follow from `y<=(z+u)/2` and `u<=z/3`.
Therefore the exact regime-II residue in the proved three-slot theorem is
`max(u,2y-z)=u`, and its Bellman sum is exactly `L_3(z;u,y)`.  When
`z>=A`, that term is strictly positive.  If also `u<=2A/3`, Lemma 1.1
makes the sole remaining transient nonnegative.  Theorem 2.2 is sound.

On `w=2u`, one has `z>=3u`.  Hence `(0,u,2u,z)` is internally
superadditive and is again a regime-II table with exact residue `u`.
Under (3.4), the far-tail transient is empty, while the endpoints of both
compact transients lie in `[0,2A/3]`.  Corollary 3.2 has the correct sign.

## 5. Pulse identities and multiplicities

Splitting `C(z/3)` into its three residue classes modulo `z` gives

\[
 C(z/3)=\sum_{q\ge0}
 \left(K(qz)+K(qz+z/3)+K(qz+2z/3)\right).
\]

On `w=y`, replacing the last two residues by `u,y` produces exactly the
two occurrence-labelled interval families `P_1,P_2` in (2.6).  Thus
(2.7) is an equality of signed measures with multiplicity, even when two
physical intervals overlap.

On `w=2u`, the same calculation with residues `u,2u` gives precisely
`Q_1,Q_2` in (3.2).  Together with the three finite transients in (3.1),
this is exactly five occurrence-labelled pulse families.  None is merged,
cancelled, or assigned a sign without proof.

## 6. Strict period monotonicity

Fix `u,y` and vary `P` in (2.8).  Every term with period index `q>=2`
has argument at least `2P>=3A/2`, so its derivative with respect to `P`
is positive.  The two shifted `q=1` terms are also in the increasing tail:

\[
 P+u\ge A,\qquad P+y\ge P+u\ge A.
\]

Only the bare term `K(P)` can contribute negatively.

Writing `p=P/A`, the `q=1` contribution divided by `2A` is

\[
 -h(1-p)+h(1+p)
 +h(1+p+u/A)+h(1+p+y/A).
\]

At all shifted tail arguments `h` is decreasing.  The inequalities
`u/A<=p/3` and `y/A<=2p/3` therefore give the lower bound `R(p)` in
(2.10) in the stated direction.

### 6.1 Strong convexity of `R`

Differentiation gives exactly

\[
 R''(p)=-h''(1-p)+h''(1+p)
 +{16\over9}h''(1+4p/3)+{25\over9}h''(1+5p/3).
\]

For `3/4<=p<=1`, the first term is nonnegative.  On each of the three
remaining argument intervals, the sign polynomial in `h'''` shows that
`h''` has no interior minimum, so it suffices to check the endpoints.

Put `rho=exp(-pi/64)`.  The exact implications

\[
 {119\over125}<\rho<{497\over522}
\]

were replayed as follows:

\[
 1+{11\over224}
 +{(11/224)^2/2\over1-(11/224)/3}
 <{125\over119},
\]

with exact margin `439/5034176`, and

\[
 \sum_{j=0}^{3}{(333/(106\cdot64))^j\over j!}
 >{522\over497},
\]

with exact margin

\[
 {2702354647\over310344392114176}>0.
\]

Using the lower classical bound for the positive algebraic prefactor and
the lower `rho` bound for the exponential factor verifies both endpoints
of each interval:

\[
\begin{array}{c|c|c}
\text{interval}&\text{endpoint powers of }\rho&\text{uniform lower bound}\\
\hline
[7/4,2]&49,64&2/5\\
[2,7/3]&64,\lceil784/9\rceil=88&1/4\\
[9/4,8/3]&81,\lceil1024/9\rceil=114&1/10.
\end{array}
\]

All six exact cross-multiplications are strict in the hash-bound replay.
Consequently

\[
 R''(p)>{2\over5}+{16\over9}{1\over4}
                  +{25\over9}{1\over10}
 ={101\over90}>1.
\]

### 6.2 Initial value and slope

The exact lower rational used for (2.15) is

\[
 -{1\over4}{497\over522}
 +{7\over4}\left({119\over125}\right)^{49}
 +2\left({119\over125}\right)^{64}
 +{9\over4}\left({119\over125}\right)^{81}
 >{9\over200}.
\]

For (2.16), the first coefficient is positive and the other three are
negative.  Therefore the sign-safe exact lower rational is

\[
\begin{aligned}
 &(1-{(22/7)\over32}){119\over125}
 +(1-{49(22/7)\over32})\left({497\over522}\right)^{49}\\
 &\quad+{4\over3}(1-2(22/7))\left({497\over522}\right)^{64}
 +{5\over3}(1-{81(22/7)\over32})
    \left({497\over522}\right)^{81}
 >-{1\over100}.
\end{aligned}
\]

Both inequalities are expanded and asserted as exact fractions by the
replay artifact.  Since `R''>1`, the worst quadratic tangent loss is
`1/20000`; hence

\[
 R(p)>{9\over200}-{1\over20000}
 ={899\over20000}>0.
\]

Thus `Psi'(P)>0`; all derivative directions and all rational inequalities
in Theorem 2.3 are valid.

## 7. Reduction to the two boundary surfaces

Every feasible original period satisfies

\[
 z\ge A-u,\qquad z\ge2y-u,
\]

so `z>=P_0=max(A,2y)-u`.  If `P_0=2y-u`, the inequality `y>=2u`
shows that `P_0` also dominates `3u`, `3y/2`, and `u+y`.  If
`P_0=A-u`, then `A>=2y>=4u`, and the same domination follows.

Moreover:

* on the `A-u` branch, `P_0>=3A/4` because `u<=A/4`;
* on the `2y-u` branch, `P_0>=3y/2>=3A/4`.

Therefore every period in `[P_0,z]` retains all scalar feasibility
conditions needed in Theorem 2.3.  Strict period monotonicity gives

\[
 \mathcal L_3(z;u,y)\ge\mathcal L_3(P_0;u,y),
\]

and `P_0+u=max(A,2y)` yields exactly the two surfaces in (2.20).  No
interior period survives this reduction.

## 8. Final verdict

The exact `w=y` and `w=2u` normal forms, all pulse multiplicities, both
normalized positive subfaces, the strict period derivative, and the two
boundary surfaces are correct.

**Final independent verdict: PASS in the theorem's stated reduction
scope.**  Complete positivity of the three-efficient branch is not proved.
