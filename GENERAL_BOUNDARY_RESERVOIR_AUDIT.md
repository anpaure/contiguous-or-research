# Independent audit of `GENERAL_BOUNDARY_RESERVOIR.md`

## 1. Verdict

The argument is sound under the inherited three-box framework and the
fixed-subsequence interpretation stated in Sections 5--6.  In particular,
the following claims survive independent checks:

\[
 3-\sigma_c\le r(c)+{2\over\eta}H(c)+4\mu((c,c+\eta])
 \le {9\over4}c^2+{2\over\eta}H(c)+4\mu((c,c+\eta]),
\]

the finite precursor (4.1), the saturation consequence when
`H(c) -> 0` through small continuity points, and the abstract feasible
profile in Section 7.

There are three harmless presentation qualifications.

1. In the outcome statement, convergence of the short-band count requires
   both `c` and `c+eta` to be continuity points of `mu`; Section 5 states this
   correctly.  At an atomic endpoint one must use the finite inequality or a
   one-sided threshold convention, as the source itself notes.
2. In the abstract example, the sentence that (7.5) is “exactly large
   enough for (1.2)” implicitly uses the extremal admissible choice
   `r(c)=9c^2/4`.  Equivalently, it is a statement about the eliminated
   inequality (7.1).  With that choice, the full displayed boundary
   inequality holds for every admissible `eta`.
3. One may complete the definition of the example by setting `H(c)=0` also
   for `4/3 <= c < 2`.  All useful mass and supply constraints already lie
   below `4/3`, and the extension satisfies the remaining nonnegative upper
   bounds.

None of these points changes a theorem, constant, or conclusion.

## 2. Exact loss in a complement gap

Number an internal gap's positions `q=1,...,g`.  Since the forward window is
`[i+1,i+L]`, it lies in the gap exactly when

\[
 q\le g-L.
\]

The backward window `[i-L,i-1]` lies in the gap exactly when

\[
 q\ge L+1.
\]

Thus the invisible positions are the integral intersection

\[
 [g-L+1,L]\cap[1,g],
\]

whose cardinality is exactly

\[
 I_L(g)=
 \begin{cases}
 g,&0\le g\le L,\\
 2L-g,&L<g<2L,\\
 0,&g\ge2L.
 \end{cases}
\]

This verifies all endpoint cases: `I_L(L)=L`, `I_L(L+1)=L-1`,
`I_L(2L-1)=1`, and `I_L(2L)=0`.  In particular, gaps with length strictly
between `L` and `2L` create no hidden factor two: their actual loss is
`2L-g <= L`.

For a prefix gap, the forward orientation alone leaves at most
`min{g,L} <= L` exceptions.  For a suffix gap, the backward orientation does
the same.  Therefore a macroscopic word-boundary gap costs only `O(L)`, and
the `2L` total boundary term in (4.1) is correct.  If there are no dangerous
plateaux, regarding the one complement interval as both outside gaps only
overcounts and remains safe.

## 3. Strong/weak successor split and finite constants

For a successor of length `lambda`, let `b=L-lambda`.  Since
`lambda <= 2a` and `L=4a+2`,

\[
 2a+2=L-2a\le b\le L.
\]

The elementary comparison used in the source is valid in both regimes:

\[
 \min\{g,L\}\le {L\over b}\min\{g,b\}.
\]

Indeed, if `g<=b` the right side is `(L/b)g >= g`; if `g>b`, it is `L`,
which dominates `min{g,L}`.

The short band is defined with the upper endpoint included:

\[
 ca<\lambda\le(c+\eta)a.
\]

Consequently every dangerous successor outside that band satisfies the
strict inequality `delta=lambda-ca>eta*a`.  Combining it with the lower
bound on `b` gives

\[
 I_L(g)
 \le {L\over\eta a(L-2a)}
       \delta\min\{g,L-\lambda\}.
\]

There is no uncharged equality case at `(c+eta)a`.  A short-band successor
is charged the unconditional `L`, and there are at most
`n_a(c,eta)` such internal successors.  Counting the first plateau as well
inside `n_a` is merely a safe overcount.

Summing over gaps therefore gives exactly

\[
 M_a-|U|\le |R_a(c)|
 +{L\over\eta a(L-2a)}a^3H_a(c)
 +Ln_a(c,\eta)+2L.
\]

If `m=0` this remains valid directly.  If `m>0`, the dangerous plateaux have
disjoint edge sets.  Writing `omega` for shared endpoints,

\[
 |U|=\sum_j(\lambda_j+1)-\omega,
 \qquad 0\le\omega\le m-1,
\]

so

\[
 0\le |U|-\sum_j\lambda_j\le m.
\]

This proves the source's `+m` correction with the correct sign.  Shared
endpoints are in the plateau union, not in a complement gap, so no position
is counted twice.  Edge disjointness also gives `m=O_c(a)`, because every
dangerous plateau uses more than `ca` of the `M_a-1=O(a^2)` word edges.

After division by `a^2`, the seam and short-band coefficients are

\[
 {L\over\eta(L-2a)}\longrightarrow {2\over\eta},
 \qquad
 {L\over a}{n_a(c,\eta)\over a}\longrightarrow
 4\nu(c,\eta).
\]

Thus the constants `2/eta` and `4` are correct; neither the boundary gaps nor
the shared endpoints leave an additional limiting term.

## 4. Weak convergence and limsup passage

All normalized lengths lie in the common compact interval `[0,2]`.  Hence
weak convergence of the finite measures gives convergence against every
bounded function whose discontinuity set has `mu`-measure zero.  If `c` is
a continuity point,

\[
 {1\over a^2}\sum_{\lambda_j>ca}\lambda_j
 =\int_{(c,2]}x\,d\mu_a(x)\longrightarrow\sigma_c.
\]

If both `c` and `c+eta` are continuity points,

\[
 {n_a(c,\eta)\over a}=\mu_a((c,c+\eta])
 \longrightarrow\mu((c,c+\eta]).
\]

The tail convention matches the strict dangerous inequality
`lambda>ca`.  Taking limsups in the finite inequality is legitimate because
all terms are nonnegative and the deterministic seam coefficient converges:

\[
 \limsup(X_a+C_aY_a)\le\limsup X_a+C\limsup Y_a
 \quad(C_a\to C>0).
\]

The terms `(2L+m)/a^2` vanish.  This yields (5.4).  The inherited subset
run-spectrum estimate supplies `r(c)<=9c^2/4` for every fixed
`0<c<2/3`, so the second inequality follows with no interchange of the
`a`-limit and the threshold limit.

For fixed `c`, the sets `(c,c+eta]` decrease to the empty set as
`eta downarrow 0`.  Finiteness of `mu` therefore gives
`nu(c,eta)->0`; no assumption about an atom at `c` is needed for this
particular continuity-from-above step.  Choosing non-atomic upper endpoints
is always possible because a finite measure has only countably many atoms.

## 5. Saturation and limit order

If `H(c)=0` at a fixed continuity point, first take the profile limit, then
send `eta downarrow 0` through admissible upper endpoints.  Equation (1.2)
gives

\[
 \sigma_c\ge3-{9\over4}c^2.
\]

For the more general hypothesis `H(c)->0`, after the `a`-limit choose

\[
 \eta_0(c)=c+\sqrt{H(c)}.
\]

For all sufficiently small `c`, this lies in the allowed range.  An
admissible `eta(c)` can be selected in
`[eta_0(c)/2,eta_0(c)]` with `c+eta(c)` non-atomic.  Then

\[
 {H(c)\over\eta(c)}
 \le {2H(c)\over c+\sqrt{H(c)}}
 \le2\sqrt{H(c)},
\]

and

\[
 \mu((c,c+\eta(c)])
 \le\mu((0,2c+\sqrt{H(c)}])\longrightarrow0.
\]

The last limit is valid even when `mu({0})>0`, since zero is excluded and
`mu` is finite.  Meanwhile `sigma_c -> sigma` by monotone convergence, and
the edge-disjointness bound gives `sigma<=3`.  Sending `c downarrow 0`
through continuity points in (1.2) yields `3-sigma<=0`, hence `sigma=3`.

This verifies the source's fixed order of limits:

\[
 (c,\eta)\text{ fixed}\quad\longrightarrow\quad a\to\infty
 \quad\longrightarrow\quad \eta=\eta(c)
 \quad\longrightarrow\quad c\downarrow0.
\]

No threshold depending on `a` is used.

## 6. Boundary lower bound and abstract feasible profile

Eliminating `r(c)` from (1.2) gives, for each admissible `eta`,

\[
 H(c)\ge {\eta\over2}
 \left[3-\sigma_c-{9\over4}c^2
       -4\mu((c,c+\eta])\right]_+.
\]

Taking the supremum is exactly (7.1).

For

\[
 \mu=2\delta_{4/3},\qquad \sigma={8\over3},\qquad d={1\over3},
\]

one has, for `0<c<4/3`,

\[
 e(c)=2(4/3-c),\qquad S(c)=2(4-4/3)={16\over3}.
\]

The line-capacity law holds because for `1<x<=4/3`,
`2<=6(2-x)`, while above `4/3` the tail is zero.  The mass-law slack is

\[
 2e(c)-(4-3c)={4\over3}-c\ge0.
\]

Now put `q(c)=9c^2/4` and, for `0<c<2/3`,

\[
 H(c)={4/3-c\over2}[d-q(c)]_+.
\]

If `c+eta<4/3`, the short-band mass is zero and

\[
 {2H(c)\over\eta}
 ={4/3-c\over\eta}[d-q(c)]_+
 \ge[d-q(c)]_+.
\]

Thus (1.2) holds with `r(c)=q(c)`.  If `c+eta>4/3`, the atom contributes
`4nu=8`, so the inequality is automatic.  The equality endpoint is excluded
from the continuity-point version, but approaching it from below produces
the supremum in (7.1).  Therefore

\[
 \mathcal B_c(2\delta_{4/3})
 ={4/3-c\over2}[d-q(c)]_+=H(c).
\]

Finally,

\[
 H(c)\le(4-c)e(c),
 \qquad H(c)\le(2-c)d,
\]

the first with substantial slack and the second from
`(4/3-c)/2 <= 2-c`.  Setting `H=0` once the positive part vanishes preserves
all constraints.  Hence the example is genuinely feasible for every scalar
and boundary inequality listed in (7.2), though, as correctly stated, this
does not establish geometric realizability.

## 7. Counterexample stress tests

The natural evasions do not break the proof.

* **Macroscopic boundary gap.**  It contributes no internal seam mass, but
  only its last or first `L` positions lack the available gap-contained
  orientation.  The rest enters `R_a(c)`.
* **Internal gap with `L<g<2L`.**  Its exact invisible count is `2L-g`, not
  `2L`; the source's charge dominates it.
* **Many near-threshold successors.**  They are precisely the family counted
  by `n_a(c,eta)`.  Their entire loss is at most `Ln_a`, which becomes
  `4nu(c,eta)` after normalization.  Sending `eta` down occurs only after the
  profile limit.
* **Many longer successors.**  Every one has excess greater than `eta*a` and
  is charged by its corresponding term of `H_a(c)`; each internal gap has a
  unique successor.
* **Shared plateau endpoints.**  They reduce the vertex-union correction and
  never become complement positions.  The total discrepancy from edge mass
  is at most `m=O_c(a)`, already present in (4.1).

I also exhaustively checked the exact gap formula for integer
`1<=L<30` and `0<=g<=4L`, and checked the strong-successor charge over a
finite grid of integer `a,lambda,g` and rational `c,eta`.  No counterexample
occurred; the symbolic inequalities above explain why none can.

## 8. Ledger

Proved as stated, subject to the continuity-endpoint convention:

* the exact one-sided invisible-count formula (3.1);
* the finite boundary--seam inequality (4.1), including `2L+m`;
* the constants `2/eta`, `4`, and `9/4` in the profile inequality;
* the `H(c)->0` edge-saturation consequence with the stated order of limits;
* the variational lower bound (7.1); and
* feasibility of (7.4)--(7.5) for all inequalities currently listed.

Not proved, exactly as the source records:

* geometric realization of the abstract feasible profile;
* a theorem forcing `H(c)->0`; or
* exclusion of the remaining positive-seam region.
