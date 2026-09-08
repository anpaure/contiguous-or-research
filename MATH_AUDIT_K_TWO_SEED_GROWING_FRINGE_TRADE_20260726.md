# Adversarial audit: unrelated two-seed growing-fringe trades

Date: 2026-07-26

Audited file:
`MATH_ATTACK_K_TWO_SEED_GROWING_FRINGE_TRADE_20260726.md`.

Method: pure mathematics only.  No finite search, solver, program, or web
input was used.  The algebraic overlay, Catalan packetization, constants,
normalizations, and implication scopes were checked independently.

## 1. Final verdict

The corrected report is theorem-valid, conditional only on the rooted
context/substitution functor already present in the frozen PBBS/MSW
framework.  It proves both of the deliverables for this lane:

1. a positive bulk theorem: arbitrary unrelated rooted exact factors give
   a literal integral component cube, and first-size-`r` fringe placement
   lifts that cube on a `1-o(1)` fraction of Catalan rows whenever
   `m/r^(3/2) >> log m`;
2. a statewise obstruction: if the two endpoint rows differ inside one
   contiguous carrier block of width `b`, then over `H` controlled depths
   every component signing has total half-`l_1` shadow motion at most

   \[
                   {2bH\over 2m+1}W.                 \tag{A.1}
   \]

Thus strict one-hole trades with `bH=o(m)` cannot repair an `Omega(W)`
defect.  At `H=Theta(sqrt(m))`, the minimal surviving active width is
`Omega(sqrt(m))`.

The report does **not** prove coefficient one.  It does not prove a
favourable physical cap sign for the explicit pair, a coherent deployment
of all overlapping carrier appearances, or a universal fragmentation
obstruction for every possible amplification.

## 2. Ownership overlay and port closure

Let the two exact factors be `F,G`.  Join the two owners of each physical
`X/Y` token.  If a recursive interface has non-owned external ports, also
join the two candidate rows sharing each required port signature.  These
extra edges are essential: components before this closure need not be
independently legal.

After closure, every component `K` has equal shores and identical owned
token and port ledgers.  The root token gives the diagonal root-label edge,
so either whole shore is a literal exact replacement.  Conversely, exact
token and port constraints force a row-catalogue hybrid to be constant on
each closed component.  Therefore the component directions

\[
               \tau_K={\bf1}_{G_K}-{\bf1}_{F_K}
\]

are integral unit-coefficient kernel trades, not fractional or
relabeling-only moves.

For complete cyclic profiles their effects have zero total and zero
one-coordinate margins.  No higher-shadow or target-orbit conservation
follows.  A projected feature changes precisely when its projection of
`M_q tau_K` is nonzero.

## 3. First-fringe packetization and Catalan tail

Selecting the first preorder fringe subtree of size `r` partitions every
nonavoiding size-`m` tree into a class `C[D_r]` of exactly `C_r` fillings.
Replacing the marked filling preserves all outside and ancestor sizes; it
need not preserve internal fringe sizes, and the report now says this
correctly.  The marked root remains the first size-`r` root because all
internal nodes occur later in preorder.

If `a_(m,r)` counts avoiders, then

\[
 A_r(z)=1+zA_r(z)^2-C_rz^r
       ={1-\sqrt{1-4z+4C_rz^{r+1}}\over2z}.          \tag{A.2}
\]

At `z_r=(1+eta r^(-3/2))/4`, with fixed sufficiently small `eta`, the
discriminant is positive and decreasing on `[0,z_r]`.  The necessary
analyticity step is supplied by Pringsheim: a smaller Taylor radius for
this nonnegative series would force a positive-real singularity, contrary
to the strict discriminant bound.  Hence

\[
 {a_{m,r}\over C_m}
 \le C m^{3/2}\exp\!\left(-c{m\over r^{3/2}}\right). \tag{A.3}
\]

For local component sizes `s_j`, the lifted size-biased moment is exactly

\[
 \chi_m={a_{m,r}\over C_m}
       +\left(1-{a_{m,r}\over C_m}\right)
          {1\over C_r}\sum_j s_j^2.                 \tag{A.4}
\]

Thus row supply and literal integrality persist at the minimal critical
scale `r=Theta(sqrt(m))`.

## 4. Full-profile rounding and hinge dual

For nondegenerate cyclic interval lengths, one row contributes at most once
to a fixed target.  If component `K` has `b_K` rows per shore and complete
profiles `u_(K,q),v_(K,q)`, then

\[
 A_{Kq}={1\over2}\|v_{Kq}-u_{Kq}\|_1,
 \quad \|v_{Kq}-u_{Kq}\|_\infty\le b_K,
 \quad \|v_{Kq}-u_{Kq}\|_2^2\le2b_KA_{Kq},
 \quad \sum_KA_{Kq}\le W.                           \tag{A.5}
\]

The empty/full cyclic levels are deterministic and are excluded from the
`l_infinity` assertion.

If an independently biased fractional state has margins
`bar(mu)_q(S)<=p-gamma_q(S)`, the scalar inequality
`(Y-gamma)_+ <= Y^2/(4gamma)` gives an exact integral child with

\[
 \sum_q\omega_q K_p(\mu_q)
 \le \sum_{q,S}{\omega_q V_q(S)\over4\gamma_q(S)}.  \tag{A.6}
\]

For `gamma_q(S)>=alpha_qp` and `b_K<=b_max`, this is at most

\[
 {b_{\max}W\over8p}\sum_q{\omega_q\over\alpha_q}.  \tag{A.7}
\]

Consequently `b_max=o(sqrt(p))` is sufficient when the margins are
uniformly proportional and the weighted depth sum is `O(sqrt(p))`.  This
is a sufficient route, not a necessary sign condition near a floor hinge.

The fractional obstruction is exactly

\[
\min_{0\le x_K\le1}\sum_q\omega_qK_p(\mu_q(x))
=\max_{0\le z_q(S)\le\omega_q}
\left[
 \sum_{q,S}z_q(S)(\lambda_q(S)-p)
 +\sum_K\min\{\langle z,u_K\rangle,
               \langle z,v_K\rangle\}
\right].                                             \tag{A.8}
\]

This follows by the box representation of the positive part and bilinear
minimax.  It includes all collars and backgrounds.  Any successful
integral constant-one construction must in particular make this fractional
dual `o(W)` on the controlled ledger, but it may do so through correlated
selection rather than a common directed sign.

## 5. Explicit non-row-power pair

The once-suspended rooted pentagon, followed by every suffix
`B in D_(r-4)`, gives two exact size-`r` factors with exactly `C_(r-4)`
independent five-row components.  The checked local profiles are

\[
 \Delta_{\rm marked}=2e_3+e_5-e_4-2e_2,             \tag{A.9}
\]

\[
 \|\Delta_{\rm complete}\|_1=18C_{r-4},\qquad
 \|\Delta_{H_r\text{-orbit}}\|_1=16C_{r-4}.         \tag{A.10}
\]

The orbit separation is genuine.  With `c` the first suffix coordinate,
the four outer-coordinate groups have distinct invariant signatures from
`a/star` presence and occupancies `1,2,2,0` in the ambient pair `{b,c}`.
Suffixes in a common orbit therefore add identical signed vectors rather
than cancel them.

The component moment is

\[
 \chi_r=1+20{C_{r-4}\over C_r}\longrightarrow{69\over64}.       \tag{A.11}
\]

This proves a positive-density **row/component** bank and a genuine escape
from relabeling-only rigidity.  Its full cyclic occurrence densities are
only

\[
 {18C_{r-4}\over(2r+1)C_r}\sim{9\over256r},\qquad
 {16C_{r-4}\over(2r+1)C_r}\sim{1\over32r}.          \tag{A.12}
\]

The active carrier has width `b=9`, despite growing `r`; hence the locality
ceiling makes every strict one-hole/first-fringe signing `o(W)` over
`H=O(sqrt(m))` depths.

## 6. Deployment and normalization corrections

Three quantities are distinct.

1. The disjoint first-fringe lift has exactly
   `P_(m,r)C_(r-4)` independent five-row components.
2. The full aligned atlas has `H_(m,r)C_(r-4)` component appearances.
   These overlap in rows and are not independent components; their number
   can exceed `C_m`.
3. Physical global action includes collars and target collisions.  The
   local value eighteen is a full `l_1` variation, so its half-`l_1`
   action is nine.  The exact quantity
   `9P_(m,r)C_(r-4)` is only the intrinsic/tagged local packet budget until
   a full context ledger proves physical isometry.

Likewise, in the canonical tensor construction the tagged full `l_1`
variation and half-`l_1` action are respectively

\[
 18\binom{2r-8}{r-4},\qquad
 9\binom{2r-8}{r-4}.                                 \tag{A.13}
\]

Their normalized limits are `9/256` and `9/512`.  The same tensor has

\[
 \mathbb E k=\left({5\over256}+o(1)\right)r,
 \qquad
 \chi_r\ge5^{(5/256+o(1))r}.                        \tag{A.14}
\]

This is an exact action--fragmentation obstruction for the canonical
flip-every-slot tensorization only.  It is not a theorem about every
correlated amplification of a bounded packet.

## 7. Precise proved/conditional boundary

Proved:

* unrelated exact factors yield literal port-closed overlay trades;
* growing first-fringe placement gives asymptotically complete row coverage
  and preserves component fragmentation exactly;
* the explicit pentagon pair changes complete shadow and `H_r`-orbit
  profiles with bounded component moment;
* every contiguous `b`-carrier-local architecture obeys (A.1);
* the safe-mean theorem and protected-mass dual give exact positive and
  negative full-profile criteria.

Not proved:

* a coherent `Theta(W)` physical action deployment with bounded component
  moment;
* an `o(W)` floor-cap child for the canonical MSW/PBBS background;
* a critical pair with active width `Omega(sqrt(m))` and a dual-evading
  full collar/background profile;
* a coefficient-one theorem.

The remaining two-seed gate is therefore sharply localized but open: find
an unrelated exact pair at some `r=Omega(sqrt(m))`, with active width
`b=Omega(sqrt(m))`, controlled port-closed fragmentation, and a correlated
full-profile selection which makes (A.8) `o(W)`.  At the minimal scale
`r=Theta(sqrt(m))`, this requires genuinely root-scale activity.
