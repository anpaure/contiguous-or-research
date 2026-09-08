# Independent audit of `EXACT_ATOMIC_SEAM_ENVELOPE.md`

## 1. Verdict

**PASS WITH LOCAL PROOF COMPLETIONS AND A STRICT SCOPE QUALIFICATION.**

The main calculation is correct.  For an atomic plateau profile

\[
  \mu=2\delta_x,\qquad 4/3\le x\le3/2,
\]

the exact minimum guaranteed saving in the inherited **aggregate,
unlabelled, fixed-threshold seam relaxation** is

\[
 S_{\rm ex}(x)
 =(6x-7)x^2-\bigl(4-2\sqrt{2x(2-x)}\bigr)(3-2x).
\]

This statement survives the most important adversarial check: absorption
and the gap budget were not optimized independently over an impossible
product set.  At an atom, the projection of the audited joint feasible set
onto the nonabsorbed gap measure can be characterized exactly, and the
two-point attaining measure in the source belongs to that joint set.

The convex-envelope calculation, Jensen direction, monotonicity in the
number of nonabsorbed seams, endpoint values, derivative of the defect
margin, and all-cap optimization are also correct.  Consequently the
inherited large-defect theorem really gives

\[
 \liminf {D_a\over a^2}\ge {4-3x+S_{\rm ex}(x)\over7}
 \ge {4\over21},
\]

and uniformly over the atomic interval

\[
 \liminf {D_a\over a^2}\ge0.202774508983752\ldots .
\]

Three qualifications are needed.

1. “Sharp within the ledger” means sharp only in the aggregate
   fixed-threshold relaxation of `MIXED_PROFILE_SEAM_NEXT.md`.  It is not
   sharpness over real three-box words, direction-labelled ledgers, or
   multiscale-compatible ledgers.
2. The source proves the saving infimum explicitly, but its displayed proof
   of
   `lim_(c up x) U_c(2 delta_x)=3x-S_ex(x)` omits one short uniformity line
   for the seam term `H_c`.  Section 6 below supplies it.
3. Section 6 of the source, on finite-band stability, is a correct proof
   sketch rather than literally a verbatim proof.  A compact-domain
   continuity argument is needed because the nonabsorbed seam count and gap
   budget both move with the band width.  Section 9 below supplies that
   argument.  The qualitative stability and positive-defect conclusions are
   valid; the source rightly makes no numerical claim for its unspecified
   constant `C`.

The title phrase “tripled defect constants” should not be read literally for
every constant.  The balanced single-cap constant is exactly tripled, but
the old uniform single-cap constant improves by a factor `9/2`, and the
all-cap constant by a different factor.  This is wording only.

## 2. Sources and hashes

The source audited here is

```text
eb4f4eca7756a8909dbe803ac909833cb6569f7b8b7680ff4f7f51caaea4fb6d  EXACT_ATOMIC_SEAM_ENVELOPE.md
```

The complete dependencies checked were

```text
01d863d66cf2a0a2e0fdc13f8b4e1b52d109de96c1c798819dc3e8a4cf4abd60  MIXED_PROFILE_SEAM_NEXT.md
6d5a31f5fe6221345ee9ba1916767bfd58f8570e8d4715dc3ea9857d30392ac5  MIXED_PROFILE_SEAM_INDEPENDENT_AUDIT.md
34287b12488dd4e639b00f02af3d56336e37114ea96a5d03b635cb7434a811b9  LARGE_DEFECT_DICHOTOMY_NEXT.md
a0ab3855e954c353b6bb5bbf7c2e822eba52a2887ce298da2c8adb39842e696e  LARGE_DEFECT_DICHOTOMY_INDEPENDENT_AUDIT.md
ec1ce534e287af0485b98a648ed75c4f70571a52857b4bfca14925f7cd14b0e7  fable_general_case/FABLE_QUANTITATIVE_SEAM_ALTERNATIVE.md
75483123b4425561847bd00f607a545545af0a0ae2661ce9f3fb41e322bfbde6  FABLE_QUANTITATIVE_SEAM_TRACE_AUDIT.md
1b612fceabb25089060a59282a613ff01ae581e2fccab11e95cae843ce17113a  FABLE_QUANTITATIVE_SEAM_REPAIR_INDEPENDENT_AUDIT.md
```

I used the repaired conventions from the independent audits: total demand
mass at a threshold is the full weak-limit mass unless continuity is stated,
and `3 dt` is aggregate line capacity, not three already-labelled capacities.
For the atom considered here, the threshold lies strictly below `x`, so the
threshold-boundary issue does not arise.

## 3. Exact joint feasible set at one atom

This is the decisive audit.  Put

\[
 Z=3-2x,\qquad n=6x-7=2-3Z.
\]

The seam measure has total mass two and has `p=s=x` identically.  Every
absorbed seam asks for a level in the same interval

\[
 I_x=[x-1,2-x],\qquad |I_x|=Z.
\]

Let `A=||alpha||` be absorbed seam mass.  The aggregate capacity
`kappa(t in B)<=3|B|` gives exactly

\[
                         A\le3Z.                    \tag{3.1}
\]

Therefore the nonabsorbed measure `nu=rho-alpha` has mass

\[
                         N=2-A\ge n.                \tag{3.2}
\]

Its gap moment satisfies

\[
                         \int z\,d\nu\le Z,          \tag{3.3}
\]

because `nu<=rho` and the total gap budget is `Z`.

Conversely, these projected constraints are sufficient in the aggregate
relaxation.  Given any nonabsorbed measure of mass

\[
                         n\le N\le2
\]

with `p=s=x` and gap moment at most `Z`, add absorbed mass `2-N` at
`(p,s,z)=(x,x,0)`.  When `Z>0`, distribute its level demand over `I_x`
with constant density `(2-N)/Z<=3`; when `Z=0`, (3.2) forces `N=2` and no
absorbed mass is present.  This constructs `rho`, `alpha`, and `kappa`
satisfying the marginal, gap, support, and aggregate capacity constraints
simultaneously.

Hence the true projected feasible set is

\[
 \left\{\nu:\ n\le\|\nu\|\le2,quad
                 \int z\,d\nu\le Z\right\}.         \tag{3.4}
\]

The source temporarily drops the harmless upper bound `N<=2`.  Since the
minimizer below occurs at `N=n`, this enlargement does not change the
infimum.  This proves that the source did not double-spend absorption
capacity and gap mass.  In particular, giving the whole gap budget to the
nonabsorbed block is feasible: the attaining absorbed block has zero gaps.

## 4. Saving integrand and the convex envelope

At the atom the audited mixed saving integrand becomes

\[
 \phi_x(z)=
 \begin{cases}
 x(x-z),&0\le z\le4-2x,\\
 (4-x-z)(x-z),&4-2x\le z\le x,\\
 0,&z\ge x.
 \end{cases}                                      \tag{4.1}
\]

Write

\[
 q(z)=z^2-4z+x(4-x),\qquad
 z_t=\sqrt{2x(2-x)},\qquad m=2z_t-4.
\]

The line

\[
                         T(z)=x^2+mz               \tag{4.2}
\]

is tangent to `q` at `z_t`, because

\[
 q(z_t)-q'(z_t)z_t=x^2.
\]

The location checks are exact:

\[
 4-2x\le z_t\le x\quad\Longleftrightarrow\quad x\ge4/3
\]

on the present interval.  Moreover

\[
 q(z)-T(z)=(z-z_t)^2,                              \tag{4.3}
\]

and on the first linear branch

\[
 x(x-z)-T(z)=(4-x-2z_t)z\ge0,                     \tag{4.4}
\]

because

\[
 (4-x)^2-4z_t^2=(3x-4)^2\ge0.
\]

Thus `T<=phi_x` up to the tangency point.  From `z_t` to `x`, the quadratic
is convex; at `x`, its left derivative `2x-4` is at most the derivative zero
of the constant tail.  Therefore

\[
 \operatorname{env}_x(z)=
 \begin{cases}
 x^2-(4-2z_t)z,&0\le z\le z_t,\\
 \phi_x(z),&z\ge z_t
 \end{cases}                                      \tag{4.5}
\]

is convex and lies below `phi_x`.

It is the **greatest** convex minorant.  Indeed, any convex minorant is at
most `x^2` at zero and at most `q(z_t)=T(z_t)` at `z_t`, so convexity bounds
it above by their chord `T` on `[0,z_t]`; after `z_t` it cannot exceed
`phi_x`, which already forms the convex continuation in (4.5).

This independently verifies the source's lower-convex-envelope claim,
including both junctions.

## 5. Jensen, count monotonicity, and the exact infimum

Let a nonabsorbed gap measure have mass `N` and gap moment at most `Z`.
Jensen and monotonicity of the envelope give

\[
 \int\phi_x(z)\,d\nu
 \ge N\operatorname{env}_x\!\left({\int z\,d\nu\over N}\right)
 \ge N\operatorname{env}_x(Z/N).                   \tag{5.1}
\]

For every `N>=n`,

\[
 {Z\over N}\le {Z\over n}\le{1\over3}<z_t.       \tag{5.2}
\]

Consequently the relevant part of the envelope is always the line in
(4.5), and no nonsmooth perspective argument is actually needed:

\[
 N\operatorname{env}_x(Z/N)
     =Nx^2-(4-2z_t)Z.                              \tag{5.3}
\]

This is strictly increasing in `N`.  The adversary therefore takes
`N=n`, and the exact minimum saving is

\[
 \begin{aligned}
 S_{\rm ex}(x)
 &=nx^2-(4-2z_t)Z\\
 &=(6x-7)x^2-\bigl(4-2\sqrt{2x(2-x)}\bigr)(3-2x).
 \end{aligned}                                    \tag{5.4}
\]

This proves the Jensen direction and count monotonicity without relying on
differentiability of a perspective at the envelope's junctions.

The inequality `S_ex>=S_*` also follows without a separate radical
calculation: `S_*` is obtained by applying Markov's inequality at one gap
cutoff to the same joint feasible set, whereas (5.4) is its exact infimum.
The endpoint equalities are

\[
 S_{\rm ex}(4/3)=4/3=3S_*(4/3),\qquad
 S_{\rm ex}(3/2)=9/2=S_*(3/2).
\]

## 6. Attainment and the limit of the adversarial functional

Let

\[
                         w={Z\over n}.
\]

The nonabsorbed measure of mass `n` with conditional gap law

\[
 z=0\quad\hbox{with probability }1-w/z_t,
 \qquad
 z=z_t\quad\hbox{with probability }w/z_t             \tag{6.1}
\]

has mean gap `w` and saving `n env_x(w)=S_ex(x)`.  Add absorbed mass `3Z`
at gap zero and spread it with aggregate density three over `I_x`.  The
total seam mass is

\[
                         n+3Z=2,
\]

both `p`- and `s`-marginals are `2 delta_x`, the total gap moment is `Z`,
and the aggregate line resource is saturated but not exceeded.  Thus this
is a genuinely joint feasible ledger, not two separately feasible
marginals pasted together.

At `x=3/2`, `Z=0` and the absorbed block vanishes.  At `x=4/3`,
`w=1/3`, `z_t=x=4/3`, and the conditional weights are `3/4` and `1/4`, as
claimed in the source.

To complete the displayed limit for `U_c`, put `c=x-zeta`.  Uniformly over
every feasible atomic ledger,

\[
 e_c=2\zeta,
 \qquad
 0\le H_c
   =\zeta\int\min\{z,4-x\}\,d\rho
   \le2(4-x)\zeta.                                 \tag{6.2}
\]

Therefore `H_c->0` uniformly, not merely for the attaining ledger.  The
guaranteed lower bound `S>=S_ex` gives the limsup inequality for `U_c`, and
the explicit ledger above gives the matching liminf inequality.  Hence

\[
 \lim_{c\uparrow x}\mathcal U_c(2\delta_x)
                       =3x-S_{\rm ex}(x).           \tag{6.3}
\]

This is the one short uniformity step omitted from the source's written
proof.

## 7. Transfer to quadratic defect

For every fixed tolerance `tau>0`, choose the threshold and regularity band
numerically before sending `a` to infinity.  The exact seam repair then
gives a forward span-`4a+3` assignment on all but `O(a)` starts with

\[
 {Q\over a^3}\le3x-S_{\rm ex}(x)+\tau+o(1).        \tag{7.1}
\]

Every substituted seam-local run with positive saving has
`z<s<=3/2+o(1)`, so its cost is below `2a+O(1)`; when `phi=0`, the original
first-dangerous assignment may be retained.  Thus every hypothesis of the
independently audited large-defect transfer applies to this same assignment.

Put

\[
 g(x)=4-3x+S_{\rm ex}(x).
\]

The cap `y=3` gives

\[
 \liminf {D_a\over a^2}\ge {g(x)\over7}.           \tag{7.2}
\]

Differentiating with `z_t'= (2-2x)/z_t` yields

\[
 g'(x)=18x^2-14x+5-4z_t
       +{2(2-2x)(3-2x)\over z_t}.                  \tag{7.3}
\]

On `[4/3,3/2]`, the first two grouped terms obey

\[
 18x^2-14x+5\ge55/3,\qquad -4z_t\ge-16/3,
\]

while the last term is at least

\[
 -{2\over3\sqrt{3/2}}>-0.545.
\]

Thus `g'>0`.  Since

\[
                         g(4/3)=4/3,
\]

(7.2) is uniformly at least `4/21`.

For all caps, write `t=3-y`.  Since

\[
 F(3-t)=4-t^3/6,
\]

the transfer gives

\[
 R_g(t)={g-t^3/6\over7-t},\qquad0\le t<1.          \tag{7.4}
\]

The interior critical equation is

\[
                         2t^3-21t^2+6g=0,          \tag{7.5}
\]

and at such a point

\[
                         R_g(t)=t^2/2.              \tag{7.6}
\]

The function in (7.4) is pointwise increasing in `g`; since `g` is
increasing in `x`, its uniform minimum occurs at `x=4/3`, where `g=4/3`.
The unique root in `(0,1)` of

\[
                         2t^3-21t^2+8=0
\]

is

\[
 t=0.636827306235768\ldots,
\]

giving

\[
                         t^2/2
 =0.202774508983752\ldots .                         \tag{7.7}
\]

The endpoint case for larger `g` only increases the bound.  This verifies
the source's all-cap constant and its uniformity.

## 8. Meaning of “sharp within the ledger”

The exactness proved in Sections 3--6 is exactness for the relaxation with

* one fixed threshold;
* only the two atomic length marginals;
* one total gap-moment budget;
* aggregate capacity `3 dt`; and
* the audited seam-local saving integrand.

It does not impose three separately labelled direction resources, the
predecessor's actual rising direction, cross-line desert placement,
intersection geometry, or nesting of successor couplings as the threshold
changes.  Nor has the attaining ledger been realized by a word.

The source mostly says this correctly.  The safest exact phrase is:

> `S_ex` is the sharp atomic guarantee in the aggregate unlabelled
> fixed-threshold seam-repair relaxation.

Any phrase dropping the words “aggregate relaxation” risks overstating the
result.

## 9. Finite-band stability

The source's qualitative claim is correct, but “survives verbatim” hides a
small continuity argument.  Here is the missing completion.

Under the finite-band hypotheses, regular-to-regular seam mass is at least

\[
                         2-2\varepsilon-o(1).
\]

Aggregate absorption removes at most

\[
                         3(Z+2\varepsilon)+o(1),
\]

so nonabsorbed regular seam mass is at least

\[
                         n-8\varepsilon-o(1).       \tag{9.1}
\]

The total gap budget is at most

\[
 G_\varepsilon
 =3-(2-\varepsilon)(x-\varepsilon)
 =Z+(2+x)\varepsilon-\varepsilon^2.                \tag{9.2}
\]

Every regular seam satisfies

\[
 \phi(p,s,z)\ge\phi_x(z)-6\varepsilon.             \tag{9.3}
\]

For sufficiently small absolute `epsilon`, (9.1) is uniformly bounded
away from zero on the compact atomic interval.  The function

\[
 (N,G,x)\longmapsto N\operatorname{env}_x(G/N)
\]

is uniformly continuous on the resulting compact parameter domain after
clipping `G/N` to the finite support needed here.  Also the actual
nonabsorbed mass is at most `2+epsilon`, so the integrated Lipschitz loss in
(9.3) is `O(epsilon)`.  It follows that the guaranteed saving is

\[
                         S_{\rm ex}(x)-O(\varepsilon)-o(1).  \tag{9.4}
\]

Combining this with the inherited first-dangerous upper cost

\[
                         3x+29\varepsilon
                               +15\varepsilon^2+o(1)
\]

gives a strict margin

\[
                         g(x)-O(\varepsilon)
                         \ge4/3-O(\varepsilon).     \tag{9.5}

Thus one absolute band width gives both the small-defect contradiction and,
via the audited transfer, a positive quadratic-defect bound.  This proves
the qualitative content of source Section 6.  It does not certify the
informal “roughly 4.5 times larger” comment as a numerical theorem.

## 10. Final theorem ledger

### Certified under the inherited framework

1. The exact formula for `S_ex`.
2. Exact joint feasibility of the attaining absorption/gap ledger.
3. Sharpness inside the aggregate unlabelled fixed-threshold relaxation.
4. The limit formula for `U_c` after the uniform `H_c` completion.
5. `S_ex(4/3)=4/3` and `S_ex(3/2)=9/2`.
6. Strict monotonicity of `g` and the uniform single-cap defect `4/21`.
7. The all-cap uniform defect `0.202774508983752...`.
8. Qualitative finite-band stability with strengthened constants.

### Not certified or claimed

1. Realizability of the attaining static ledger by one middle ordering.
2. Sharpness after adding direction labels, cross-line placement, or
   multiscale consistency.
3. Exclusion of arbitrary mixed profiles.
4. A universal three-box lower bound.
5. A construction or exact formula for the original contiguous-OR problem.

The result is a substantial and correct tightening of the atomic branch.  It
does not seal the mixed-profile branch, which remains the real obstruction.
