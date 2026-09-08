# Self-audit: pointwise codegree and random spread-top naming

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_SPREAD_TOP_NAMING_POINTWISE_CODEGREE_AND_RANDOM_PARTITION_20260805.md`  
**Method:** exact symbolic and probabilistic replay; no computation, search,
or solver  
**Verdict:** **GO in its top-only scope.**  Fixed relative slack is
sufficient, the exact Bernstein threshold permits vanishing slack, and the
insured one-depth shift can afford that threshold at every capacity.

## 1. Fractional matching certificate

At rank `u`, uniform continuation flow from every rank-`u-1` set gives a
fixed right load

\[
 {u\over n-u+1}={C_{u-1}\over C_u}=1-{H_u\over C_u}.
\]

A request with top rank `s` has exactly `binom(n-s,u-s)` containing
rank-`u` starts.  Uniform flow over them has total one, and the accumulated
request load at `T` is exactly the displayed `lambda_u(T)`.  Hence the
pointwise bound `lambda_u(T)<=H_u/C_u` produces a fractional matching
saturating every continuation and request vertex with right capacity one.
Bipartite integrality gives the claimed exact matching.  This proves every
Hall/Rado cut simultaneously; no converse is asserted.

## 2. Mean-load identity

For a uniform `m_(s,u)`-subset of `B_s`, the number contained in fixed
`T in B_u` is hypergeometric with mean

\[
 m_{s,u}{\binom us\over C_s}.
\]

The flag identity

\[
 C_s\binom{n-s}{u-s}=C_u\binom us
\]

shows that after division by the containment degree its expected load is
`m_(s,u)/C_u`.  Summing ranks gives `m_u/C_u`, so fixed relative count slack
is exactly fixed relative pointwise slack in expectation.

## 3. Concentration check

For fixed `(u,T)`, uniform sampling without replacement is negatively
associated; independent rank partitions preserve that property across the
summed blocks.  Every weighted indicator is at most `1/d_min(u)`, and the
variance sum is at most `mu/d_min(u)`.  Weighted Bernstein therefore gives

\[
 \Pr\{L(T)>\alpha_u\}
 \le\exp\{-c\epsilon^2\alpha_ud_{\min}(u)\}
\]

for an absolute positive `c`.

With `b=r-D-1`, `u=b+g`, and `N=r+D+2`, direct substitution gives

\[
 d_{\min}(u)=\binom N{g+1},
 \qquad
 \alpha_u={2D+3-2g\over N-g}.
\]

At `g=1`, their product is `(2D+1)N/2`.  At `g>=2`, it is at least
`binom(N,3)/N`.  Hence the uniform exponent is `Omega(rD)=Omega(r^(3/2))`.
The number of tested right vertices over all collar ranks is at most
`(D+1)W=exp(O(r))`, so the union bound tends to zero.  The random
rankwise partition therefore has a deterministic successful outcome.

## 4. Structural and scope check

The variable-slack refinement uses the absolute gap

\[
 \tau_u={H_u-m_u\over C_u}.
\]

The same Bernstein calculation has exponent

\[
 \Omega\left({(H_u-m_u)^2d_{\min}(u)\over C_uH_u}\right).
\]

Requiring this to exceed a sufficiently large constant times `r` is
therefore exactly enough for the previous `exp(O(r))` union bound.  The
reserve in (2.20) is algebraically correct.

For the insured adjacent-depth construction, the old and new capacity
tails satisfy

\[
 K_1^+-K_1=H_t,
 \qquad K_q^+-K_q=H_{t+q-1} (2\le q\le D),
 \qquad K_{D+1}^+=H_r.
\]

Insurance can increase only the number of nonempty pieces, by at most the
sum of the insured old capacities.  For every `q>=2`, replacing a piece by
singletons weakly decreases the `q`-tail.  Terminal deletion also weakly
decreases every tail.  If the `p<=h` uninstalled-descendant pieces are
assigned first to their insured maximum occurrences, the transported bulk
has tails at most `K_1+R_ins,K_2,...,K_D,0`, while the remaining capacity
tail is `K_q^+-p`.  This verifies (2A.6)--(2A.8) without losing the physical
old-singleton/new-exception pairing.

For capacity `g`, the chosen empty reserve is

\[
 \Delta_g=O(W\sqrt{D/d_g})+1,
 \qquad d_g=\binom{r+D+2}{g+1}.
\]

The `g=1` reserve is `O(W sqrt(D)/r)=o(H_t)`.  For `g>=2`, the containment
degrees grow by a factor `Omega(sqrt(r))` at each step, so each reserve
tail is dominated by its first term and is
`O(W sqrt(D)/r^(3/2))+O(D)=o(W/r)`.  Every collar difference `H_(b+q)` is
at least a constant multiple of `W/r`; the first one is
`Theta(W/sqrt(r))`.  Thus every desired empty-socket tail is strictly
smaller than the adjacent-depth tail margin.  The sorted-tail matching
criterion legitimately reassigns all transported bulk interval pieces
after those sockets are removed; the exceptional pieces remain on their
insured occurrences.

The resulting count gap at each start rank meets the variable Bernstein
condition, so the abstract top slots admit a simultaneous spread naming.
This removes the zero-slack **arithmetic** issue; it does not choose the
lower members of the flags.

The partition is target-once at the **top rank** because bins at each rank
are disjoint.  It does not construct the lower members of the chunk chains.
Prescribing all spread tops and extending them downward is stronger than
the existing upward interval Boolean lift.  The source explicitly leaves
that extension-surjectivity/correlation open.

At exact saturation `m_u=H_u`, the mean equals the pointwise capacity, so
the sufficient condition forces exact constant load.  Random concentration
cannot supply this without a balanced orbit/design identity.  The
orbit-core paragraph correctly treats only a core whose fractional load is
already constant and leaves a fixed positive fraction of capacity for the
random remainder.  No claim is made for a saturated partial class.

Thus the result closes all top-to-collar Hall cuts under its explicit
spread/slack hypotheses, but not the unrestricted named bulk.  Audit
verdict: GO.
