# Exact atomic seam envelope: sharp saving and tripled defect constants

## 1. Outcome

This note replaces the one-parameter cutoff relaxation (3.1)--(3.4) of
`MIXED_PROFILE_SEAM_NEXT.md` by an exact convex-envelope computation.  On
the atomic segment the resulting saving constant is **sharp within the
audited fixed-threshold ledger**: it is simultaneously a guaranteed lower
bound for every atomic word and attained by an explicit adversarial ledger.

Fix `x in [4/3,3/2]` and put

\[
 n(x)=6x-7,\qquad Z(x)=3-2x,\qquad
 z_t(x)=\sqrt{2x(2-x)}.
\]

> **Theorem 1 (exact atomic envelope).**  For the atom `mu => 2 delta_x`,
> the guaranteed normalized saving of the audited seam repair is
> \[
>  S_{\rm ex}(x)=(6x-7)\,x^2-\bigl(4-2\sqrt{2x(2-x)}\bigr)(3-2x),
> \]
> and no larger constant is possible: an explicit feasible ledger attains
> it.  Consequently, for every `tau>0` there is a forward span-`4a+3`
> assignment with
> \[
>  {Q\over a^3}\le3x-S_{\rm ex}(x)+\tau+o(1),
> \]
> and `lim_(c up x) U_c(2 delta_x)=3x-S_{\rm ex}(x)`.

Comparison with the audited optimized cutoff constant
`S_*(x)=x(sqrt(x(6x-7))-sqrt(3-2x))^2`:

\[
 S_{\rm ex}(x)\ge S_*(x),\qquad
 S_{\rm ex}(4/3)={4\over3}=3\,S_*(4/3),\qquad
 S_{\rm ex}(3/2)=S_*(3/2)={9\over2}.
\]

> **Theorem 2 (tripled margins and defect constants).**  Put
> `g(x)=4-3x+S_(ex)(x)`.  Then `g` is strictly increasing on `[4/3,3/2]`,
> with
> \[
>  g(4/3)={4\over3},\qquad g(3/2)=4.
> \]
> Hence, by the audited large-defect transfer (Theorem B of
> `LARGE_DEFECT_DICHOTOMY_NEXT.md`), every universal word with
> `mu_a => 2 delta_x`, `4/3<=x<=3/2`, satisfies
> \[
>  \liminf{D_a\over a^2}\ \ge\ {g(x)\over7}\ \ge\ {4\over21},
> \]
> and, after all-cap optimization, **uniformly over the whole interval**
> \[
>  \liminf{D_a\over a^2}\ \ge\ {t_*^2\over2}=0.2027745089\ldots,
> \]
> where `t_*=0.6368273062...` is the unique root in `(0,1)` of
> \[
>  2t^3-21t^2+8=0.
> \]

Previous audited constants: exclusion margin `8/27~0.296` becomes
`4/3~1.333`; uniform defect `8/189~0.0423` becomes `4/21~0.1905`;
balanced-atom all-cap defect `0.0657635...` becomes `0.2027745...`, which
is also the new uniform all-cap constant because `g` is increasing.  The
band-stability theorem inherits the same improvement (Section 6).

**Scope.**  The broad thresholdwise obstruction `Psi(4/3)=4.371...>4` of
`MIXED_PROFILE_SEAM_NEXT.md`, Section 6, already used the exact integrand
`phi`; it is untouched by this note.  The envelope closes the gap between
lower and upper values **inside** the atomic fixed-threshold ledger; the
genuinely open directions remain multiscale/threshold coupling,
direction-labelled absorption, and cross-line gap transport.

## 2. The one-atom adversarial reduction

Work at threshold `c=x-zeta` with fixed small `zeta>0`, and regularity
width `eps>0`.  All but `o(a)` dangerous plateaux are regular, and the
audited seam repair gives, for every regular nonabsorbed seam with
normalized data `(p,s,z)`, at least

\[
 \phi(p,s,z)=\min\{p,(4-s-z)_+\}(s-z)_+
\]

normalized saving (disjoint service starts times per-start saving).  For
the atom, `|p-x|,|s-x|<=eps`, and `phi` is Lipschitz:

\[
 |\phi(p,s,z)-\phi(x,x,z)|\le2|p-x|+4|s-x|\le6\,\varepsilon,
\]

uniformly in `z`: both factors lie in `[0,2]` (the min is capped by
`p<=2`, and `(s-z)_+<=s<=2`), the min is 1-Lipschitz in `p` and in `s`,
and the second factor is 1-Lipschitz in `s`.  Write

\[
 \phi_x(z)=\phi(x,x,z)
 =\begin{cases}
   x(x-z),&0\le z\le4-2x,\\
   (4-x-z)(x-z)=z^2-4z+x(4-x),&4-2x\le z\le x,\\
   0,&z\ge x.
  \end{cases}
\]

The adversary (the word) controls three things, each in the safe
direction for a lower bound:

1. **Which seams are absorbed.**  Absorption capacity is
   `3(3-2x+2eps)a+O(1)` (audited high-line count).  Absorbed seams
   contribute zero saving, so the worst case absorbs the maximum count,
   leaving at least `n_eps a` nonabsorbed regular seams,
   `n_eps=6x-7-O(eps)-o(1)`.
2. **The gap sizes of the nonabsorbed seams.**  Complement gaps are
   disjoint, so their total normalized mass is at most
   `Z_eps=3-2x+O(eps)`.
3. **The predecessor/successor coupling**, already frozen to `(x,x)` up
   to the `6 eps` Lipschitz error.

Thus the guaranteed saving is at least

\[
 S\ \ge\ \min\Bigl\{\sum_{j=1}^{N}\phi_x(z_j):
   N\ge n_\varepsilon a,\ z_j\ge0,\ \sum_j z_j\le Z_\varepsilon a\Bigr\}
   \cdot a^2\ -\ 6\varepsilon\cdot O(a^3),
\]

a purely finite minimization.  Section 3 evaluates it exactly.

The legitimacy of the minimization is the standard guaranteed-bound
direction: the actual gap multiset of any given word is one feasible point
of the minimization, so the minimum is a valid lower bound for every word.
Long gaps need no separate treatment here: `phi_x(z)=0` for `z>=x`
automatically, which is exactly why the cutoff relaxation lost a factor.

## 3. The lower convex envelope

`phi_x` is piecewise: linear with slope `-x` on `[0,4-2x]`; the convex
parabola `q(z)=z^2-4z+x(4-x)` on `[4-2x,x]`; zero beyond `x`.  At the
first junction the left slope is `-x` and the right slope is `4-4x`; since
`x>4/3` implies `-x>4-4x`, the slope drops and `phi_x` is **not convex**
there.  Its lower convex envelope on `[0,infty)` is therefore the tangent
line from the left endpoint `(0,x^2)` to the parabola piece, then the
function itself.

**Tangent computation.**  The tangent to `q` at `z_t` passes through
`(0,x^2)` iff `q(z_t)-q'(z_t)z_t=x^2`, i.e.

\[
 (z_t^2-4z_t+4x-x^2)-(2z_t-4)z_t=x^2
 \iff z_t^2=4x-2x^2=2x(2-x),
\]

so `z_t=sqrt(2x(2-x))`, with slope `q'(z_t)=2z_t-4=-(4-2z_t)`.  The
tangency point lies on the parabola piece:

\[
 z_t\ge4-2x\iff(3x-4)(x-2)\le0,\qquad
 z_t\le x\iff x\ge4/3,
\]

both true on `[4/3,3/2]`.  Hence

\[
 \operatorname{env}(z)=
 \begin{cases}
  x^2-(4-2z_t)\,z,&0\le z\le z_t,\\
  \phi_x(z),&z\ge z_t,
 \end{cases}
\]

and `env<=phi_x` everywhere (verified analytically by convexity of the
two right pieces and the slope comparison at `4-2x`; also checked on a
grid).

**Jensen step.**  For `N` seams with `sum z_j<=Za` (write `w=Z/n`, mean
gap at the minimal count),

\[
 \sum_j\phi_x(z_j)\ \ge\ \sum_j\operatorname{env}(z_j)
 \ \ge\ N\operatorname{env}\Bigl({\textstyle\sum_j z_j\over N}\Bigr)
 \ \ge\ N\operatorname{env}(Za/N),
\]

using convexity and then monotonicity (`env` is nonincreasing).  The
perspective `N mapsto N env(Za/N)` is nondecreasing in `N`: its
`N`-derivative is `env(w)-w\,env'(w)`, the tangent at `w` extrapolated to
zero, which is nonnegative because `env>=0` and `env'<=0`.  So the
adversary uses the minimal count `N=n a`, and

\[
 \min=n\,\operatorname{env}(w)\,a^3,\qquad w={Z\over n}={3-2x\over6x-7}.
\]

**The mean gap sits on the linear piece.**

\[
 w\le{1\over3}\iff9-6x\le6x-7\iff x\ge{4\over3},
\]

while `z_t^2=2x(2-x)>=3/2` on the interval, so `z_t>1.22>1/3>=w`.
Therefore

\[
 n\,\operatorname{env}(w)
 =n x^2-(4-2z_t)\,n w
 =(6x-7)x^2-(4-2z_t)(3-2x)
 =S_{\rm ex}(x).
\]

Letting `eps->0` and then `zeta->0` (both after `a->infty`, exactly as in
the audited transfer) proves the guaranteed-saving half of Theorem 1:
every atomic word admits the modified assignment with

\[
 {Q\over a^3}\le3x-S_{\rm ex}(x)+\tau+o(1).
\]

## 4. Sharpness: the attaining ledger

Within the fixed-threshold feasible set of `MIXED_PROFILE_SEAM_NEXT.md`
(marginals `mu=2 delta_x`, gap budget `3-2x`, absorption interval
`[p-1,2-s]=[x-1,2-x]`, level resource `3 dt`), take:

* **Absorbed block:** seam mass `3(3-2x)` absorbed at levels spread with
  density exactly `3` on `[x-1,2-x]` (capacity tight), gaps `z=0`.
* **Nonabsorbed block:** the remaining mass `n=2-3(3-2x)=6x-7`, with the
  two-point gap law
  \[
   z=0\ \text{with weight}\ 1-{w\over z_t},\qquad
   z=z_t\ \text{with weight}\ {w\over z_t},\qquad w={3-2x\over6x-7}.
  \]

The gap budget is used exactly: `n*w=3-2x`.  The saving of this ledger is

\[
 n\Bigl[\Bigl(1-{w\over z_t}\Bigr)\phi_x(0)
        +{w\over z_t}\phi_x(z_t)\Bigr]
 =n\,\operatorname{env}(w)=S_{\rm ex}(x),
\]

because the mixture of the endpoint and the tangency point lies on the
tangent line (verified symbolically and numerically at
`x=4/3,1.4,1.45,1.5`).  As `c up x`, both `e_c` and `H_c` of this ledger
tend to zero, so

\[
 \lim_{c\uparrow x}\ \mathcal U_c(2\delta_x)=3x-S_{\rm ex}(x).
\]

No feasible ledger for the atom does better in either direction: the
minimization of Section 3 is exactly over this feasible set.  Hence
`S_(ex)` is the sharp fixed-threshold atomic constant, and further
improvement **must** add constraints absent from the ledger (multiscale,
direction labels, cross-line transport) rather than sharpen the
optimization.

Two degenerate checks.  At `x=3/2`: `n=2`, `Z=0`, `w=0`, so
`S_(ex)=2*(9/4)=9/2` and the whole saving comes from zero-gap seams; the
cutoff bound has the same limit.  At `x=4/3`: `n=1/3`, `w=1/3`,
`z_t=4/3`, mixture weights `(3/4,1/4)`; the adversary parks a quarter of
the nonabsorbed seams at the dead gap `z=z_t=x` (where `phi_x=0`) and
still loses `S_(ex)(4/3)=4/3`, three times `S_*(4/3)=4/9`.

## 5. Proof of Theorem 2

`g(x)=4-3x+S_(ex)(x)=4-3x+(6x-7)x^2-(4-2 z_t(x))(3-2x)`.

**Endpoints.**  `g(4/3)=4-4+ (1)(16/9)-(4-8/3)(1/3)=16/9-4/9=4/3`;
`g(3/2)=4-9/2+9/2=4`.

**Monotonicity.**  With `z_t'=(2-2x)/z_t`,

\[
 g'(x)=18x^2-14x+5-4z_t+{2(2-2x)(3-2x)\over z_t}.
\]

On `[4/3,3/2]`: the quadratic `18x^2-14x+5` is increasing (vertex at
`x=7/18`), so it is at least its value at `4/3`, namely
`32-56/3+5=55/3`.  Since `z_t` is decreasing with `z_t(4/3)=4/3`, the
term `-4z_t` is at least `-16/3`.  The last term is negative
(`2-2x<0<=3-2x`) with magnitude at most
`2\cdot1\cdot(1/3)/\sqrt{3/2}<0.55`, using `|2-2x|\le1`, `3-2x\le1/3`,
`z_t\ge z_t(3/2)=\sqrt{3/2}`.  Hence

\[
 g'\ \ge\ {55\over3}-{16\over3}-0.55\ =\ 13-0.55\ >\ 0
\]

(numerically `g'` ranges over `[12.67,19.6]`; the closed form for `g'`
was checked against central differences at four points).  Hence the
uniform bound is the left endpoint:

\[
 \min_{[4/3,3/2]}g=g(4/3)={4\over3}.
\]

**Defect transfer at `y=3`.**  Theorem B with `U(x)=3x-S_(ex)(x)` gives

\[
 \liminf{D_a\over a^2}\ge{(4-U(x))_+\over7}={g(x)\over7}
 \ge{4\over21}.
\]

**All-cap optimization.**  With `F(3-t)=4-t^3/6` and `U=4-g`,

\[
 \liminf{D_a\over a^2}\ge R_g(t)={g-t^3/6\over7-t},\qquad0\le t<1,
\]

maximized where `(7-t)(-t^2/2)+(g-t^3/6)=0`, i.e.
`t^3/3-{7\over2}t^2+g=0`; multiplying by 6: `2t^3-21t^2+6g=0`.  At the
critical point `g=(21t^2-2t^3)/6`, so

\[
 R_g(t_*)={(21t_*^2-2t_*^3)/6-t_*^3/6\over7-t_*}
 ={t_*^2(21-3t_*)\over6(7-t_*)}={t_*^2\over2}.
\]

For the uniform `g=4/3` the critical equation is `2t^3-21t^2+8=0`, whose
unique root in `(0,1)` is `t_*=0.63682730623...` (the cubic is `8>0` at
`0`, `-11<0` at `1`, and decreasing there), giving

\[
 \liminf{D_a\over a^2}\ \ge\ {t_*^2\over2}=0.20277450898\ldots
\]

**uniformly on `[4/3,3/2]`**, since `g` increasing makes every
`x>4/3` at least as constrained.  (The interior condition `t_*<1` holds
whenever `g<19/6`; for `x` with `g(x)>=19/6`, i.e. `x>~1.455`, the
supremum is the boundary limit `y->2`, `t->1`, value `>=(g-1/6)/6>=1/2`,
even larger — but those `x` are already excluded unconditionally by the
cross-line cutoff `x>1.3489`.)  The identity `R=t_*^2/2` also
re-derives the audited `0.0657635...=t^2/2` at `t=0.36266655...` for the
old `g=4/9`, confirming consistency of the two computations.  QED.

## 6. Band stability with the envelope

Theorem 4.1 of `MIXED_PROFILE_SEAM_NEXT.md` (uniform band stability)
survives verbatim with the envelope in place of the cutoff.  For plateaux
in the band `[x-eps,x+eps]`, the Lipschitz estimate of Section 2 replaces
`phi_x` at cost `6 eps` per seam; absorption capacity becomes
`3(3-2x+2eps)`, the gap budget `3-(2-eps)(x-eps)`.  The minimization of
Section 3 is continuous in these parameters, so the guaranteed saving is
`S_(ex)(x)-O(eps)-o(1)`, and the excess terms still cost only
`29 eps+15 eps^2`.  Since the zero-band margin is now `g(x)>=4/3` instead
of `8/27`, one absolute `eps_0` (roughly `4.5` times larger than before,
though we make no exact claim) gives: every word whose `c`-dangerous list
is `eps`-banded around any `x in [4/3,3/2]` satisfies

\[
 \liminf{D_a\over a^2}\ge{\eta_\varepsilon\over7},\qquad
 \eta_\varepsilon\ \ge\ {4\over3}-C\varepsilon>0,
\]

with an absolute constant `C`.  The qualitative statement is unchanged;
only the constants strengthen.

## 7. Adversarial audit of every step

1. **Is `phi` per-seam saving legitimate at unequal `(p,s)`?**  Yes; the
   audited mixed functional (2.9) of `MIXED_PROFILE_SEAM_NEXT.md` was
   certified exactly in this generality by
   `MIXED_PROFILE_SEAM_INDEPENDENT_AUDIT.md`, Section 4 ("correct as the
   exact asymptotic guaranteed saving integrand").  We only evaluate it
   at the atom.
2. **Convexity/Jensen direction.**  `env` is convex by construction
   (tangent line + convex parabola tail meeting tangentially at `z_t`,
   then constant `0` from `z=x` where `q(x)=0` and `q'(x)=2x-4<=0`...
   note `q'(x)=2x-4<0` for `x<2`, and the parabola's minimum is at
   `z=2>x`, so `q` is decreasing on `[4-2x,x]`; continuity with the zero
   tail holds since `q(x)=x^2-4x+x(4-x)=0`, and convexity of the
   two-piece `max(q,0)`-type junction holds because the left slope at
   `z=x` is `2x-4<0=` right slope — slopes increase.  So `env` is convex
   on `[0,infty)`.)
3. **Jensen at the constraint, not the mean.**  The adversary may use
   fewer gaps than the budget; `env` nonincreasing makes `env(mean)>=
   env(Za/N)` safe.  The count may exceed `n a`; the perspective
   monotonicity argument (tangent-intercept nonnegativity) makes the
   minimal count worst.  Both directions were checked.
4. **Absorption interacts with gaps.**  Could the adversary do better by
   absorbing seams with *small* gaps and leaving large-gap seams
   nonabsorbed?  That is exactly what the minimization allows: absorption
   removes count but not gap budget, and we gave the nonabsorbed block
   the full gap budget `3-2x`.  Absorbing fewer than the capacity only
   increases the nonabsorbed count, which increases the bound (step 3).
   Absorption capacity itself is the audited high-line count and cannot
   be enlarged by gap choices.
5. **`w<=z_t` and `w<=1/3`.**  `w=(3-2x)/(6x-7)<=1/3` iff `x>=4/3`;
   `z_t=sqrt(2x(2-x))>=sqrt(3/2)>1/3` on the interval (minimum at
   `x=3/2`: `z_t=sqrt(3/2)=1.2247`).  So the mean always sits on the
   tangent segment, and the closed form is exact, not a case split.
6. **Attainment feasibility.**  The two-point ledger satisfies marginals
   (`p=s=x`), gap budget with equality, absorption interval (`t` ranges
   over `[x-1,2-x]` at density 3, total `3(3-2x)` = absorbed mass), and
   the `3 dt` level resource with equality.  It is a bona fide member of
   the audited feasible set — sharpness is within that set, exactly as
   claimed, and no stronger sharpness (against real words) is asserted.
7. **Numerical confirmations.**  Grid checks: `env<=phi_x` (no
   violations, 60 x 4000 grid); `S_(ex)>=S_*` on the interval;
   `S_(ex)(4/3)=4/3=3 S_*(4/3)`; mixture value = `n env(w)` at four
   sample points; `g` strictly increasing, `g(4/3)=4/3`, `g(3/2)=4`;
   `t_*` root and `R(t_*)=t_*^2/2` identity; grid max of `R` agrees to
   `1e-11`.
8. **Where `D=o(a^2)` enters.**  Nowhere in Sections 2--4.  Theorem 2
   uses the audited transfer (which keeps the `(7a+2)D` term exactly);
   the constants inherit its conditionality structure: the *defect lower
   bounds* are unconditional statements about universal words with the
   stated profiles.

## 8. Ledger

### Proved here (within the inherited audited framework)

1. Theorem 1: the exact atomic envelope
   `S_(ex)(x)=(6x-7)x^2-(4-2 sqrt(2x(2-x)))(3-2x)`, guaranteed and
   attained; sharp within the fixed-threshold ledger.
2. `S_(ex)(4/3)=4/3`, exactly three times the previous audited `4/9`.
3. Theorem 2: `g=4-3x+S_(ex)` increasing; uniform atomic exclusion
   margin `4/3`; uniform quadratic-defect constants `4/21` (single cap)
   and `t_*^2/2=0.2027745...` (all caps), the latter uniform over the
   entire atomic segment.
4. The general identity: the all-cap optimum of the transfer always
   equals `t_*^2/2` at the critical root of `2t^3-21t^2+6g=0`.
5. Band stability inherits the tripled margin with an absolute band
   width.

### Not proved

1. Any improvement to the broad mixed obstruction `Psi>4`: the envelope
   is atomic/band-local; the broad ledger already uses the exact `phi`.
2. Multiscale threshold coupling, direction-labelled absorption, or
   cross-line gap transport (the three genuinely open routes).
3. Realizability of any static ledger by a word; the three-box theorem;
   the OR-array conjecture.

