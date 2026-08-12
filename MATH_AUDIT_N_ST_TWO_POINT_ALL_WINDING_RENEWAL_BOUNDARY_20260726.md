# Audit of the all-winding ST transfer and renewal boundary

Date: 2026-07-26

Method: independent hand audit; no computation, search, solver, or external
input.

Audited files:

* `MATH_THEOREM_N_ST_KILLED_TRANSFER_AND_RENEWAL_BLOCK_GATE_20260726.md`;
* `MATH_THEOREM_N_ST_POSITIVE_WINDING_TWO_POINT_TRANSFER_20260726.md`;
* `MATH_THEOREM_N_ST_ZERO_WINDING_MOUNTAIN_RENEWAL_SUSCEPTIBILITY_20260726.md`;
* `MATH_THEOREM_N_ST_MOUNTAIN_POSITIVE_WINDING_RENEWAL_AND_SHORT_CYCLE_NOGO_20260726.md`;
* `MATH_SYNTHESIS_N_ST_TWO_POINT_ALL_WINDING_RENEWAL_BOUNDARY_20260726.md`.

## 1. Verdict

The exact operator identities, terminal-layer matrix, saddle constants,
mountain renewal formulas, positive-winding short-cycle obstruction, and
implication scopes pass.  The reports do not prove a global asymptotic for
\(\mathcal C_H/R_H\), and the synthesis states this correctly.

Two issues were found during audit and repaired before this verdict:

1. the reduced killed operator must use persistent equality-particle
   identities, not parent physical coordinate labels; the report now
   defines the orbitwise particle-labelled augmentation explicitly;
2. the transported terminal free coordinate was initially left with a
   possible affine offset; subtracting compulsory occupancies and testing
   the two extreme simplex vectors force that offset to be zero.

## 2. Killed-operator ordering

The convention is \({\cal U}e_x=e_{f(x)}\).  Therefore

\[
 K_j=(I-Q_j){\cal U}
\]

first updates and then kills a visit to \(Q_j\).  Reading

\[
 Q_j{\cal U}K_j^{g-1}Q_j
\]

from right to left tests times \(1,\ldots,g-1\) outside \(Q_j\) and time
\(g\) inside \(Q_j\).  Thus proper-prefix firstness and the endpoint are
both exact.  The same check shows that the two-hit operator first reaches
the predecessor at time \(a\) and reaches it next at time \(a+b\).

The domains for distinct first-return times are disjoint.  Hence the sums
of \({\cal R}^{*}{\cal R}\) are diagonal projections, and the trace
identities count starts rather than paths with multiplicity.

## 3. Persistent-particle augmentation

After peak deletion, the selected-particle itinerary is indexed by
persistent equality-particle identities in cyclic order.  A normalized
core has exactly \(p=2d+1\) cyclic augmentations, according to the identity
assigned to its current selected particle.  The equality-particle theorem
preserves these labels and conjugates their recorded word to the ordinary
length-\(p\) PBBS update.  Consequently division of the augmented traces
by \(p\) is exact, and \(Q_{j-1}\) really means selection of the immediate
predecessor of current identity \(j\).

Without this augmentation the two-hit formula would be false: an unmatched
parent physical coordinate is not a persistent particle identity.  The
corrected report no longer makes that identification.

## 4. Winding coefficient and fixed-layer invariance

For a return of gap \(2s+1\),

\[
 \sum_{t=0}^{2s}\delta(f^tD)
 =sN-\left(\sum_{j<s}d(\tau^jD)-\delta(\tau^sD)\right)
 =(s-w)N.
\]

Thus Laurent coefficient extraction separates winding exactly.

For a fixed reduced core and terminal occupancy \(z\), the selected
particle word and closing predecessor occurrence are fixed.  Varying the
other free occupancies is an orientation-preserving deformation of the
same persistent-particle trajectory.  Unit transfers change each relevant
integer arc by \(0\) or \(\pm2\) without crossing zero; over
\(s\le H-1\) the endpoint ledger changes by less than \(N\).  Since both
ledgers are multiples of \(N\), their winding is equal.  Connectivity of
the fixed-\(z\) simplex proves winding constancy.

## 5. Terminal-layer transportation

After compulsory leaves are removed, the phase-\(u\) terminal test is one
initial free coordinate \(q_{\eta_u}\).  If a residual shift \(\Delta\)
were present, the simplex vector with \(q_{\eta_u}=0\) would force
\(\Delta\ge0\), while the vector with \(q_{\eta_u}=y\) would force
\(\Delta\le0\).  Hence \(\Delta=0\).

Fixing two distinct coordinates at \(z,z'\) leaves \(y-z-z'\) units in
\(p-2\) boxes and gives

\[
 \binom{M-z-z'-2}{2d-2}.
\]

For the same coordinate the conditions agree only when \(z=z'\), giving
\(K_z\).  Row and column sums follow because the source and target
terminal layers partition two fibres related by a bijection.

At the saddle, direct binomial division gives

\[
 K_z/P=(3/4+o(1))4^{-z},
 \qquad
 J(z,z')/P=(9/16+o(1))4^{-(z+z')}
\]

for distinct coordinates.  Terminal-zero intersections have the sharp
inclusion--exclusion floor \((1/2-o(1))P\).

For \(\alpha=K_0/P=3/4+o(1)\) and
\(\beta=1-\alpha=1/4+o(1)\), a positive-layer pair has size at most
\(\beta P\), whereas its terminal-zero companion has size at least
\((2\alpha-1)P\).  The ratios in the reports are therefore exactly
\(1/2+o(1)\) for positive--positive pairs and \(1+o(1)\) for pairs with
at least one positive terminal occupancy.

## 6. Mountain renewal constants and cycle cutoff

For the mountain fibre, \(p=2h-1\), \(y=r-h\), and \(\tau\) rotates the
\(p\) weak-composition coordinates.  Terminal zero gives

\[
 R/|\Omega|={p-1\over y+p-1},
 \qquad
 \mathcal C/R=(H+1){p-2\over y+p-2}.
\]

With \(h/\sqrt r\to c\), these give the common limit \(2Ac\) after the
appropriate normalization.  The factorial-moment formula is bounded by
an exponential series uniformly in \(r\), so moment convergence to
Poisson\((2Ac)\) is legitimate.

For terminal occupancy \(z\), the predecessor arithmetic progression
gives

\[
 g_z=2+(2z+1)p,
 \qquad s_z=h+zp.
\]

One full rotor lap contributes \(N-2\) to the deficit ledger, while the
residual \(h\)-step segment contributes the missing \(2z\).  Therefore
the winding is exactly \(z\).  If \(z\ge1\) is active, then
\(3p+2\le2H-1\), so \(p<H+1\).  Since every fibre orbit has period
dividing \(p\), all such positive starts are removed by the retained-cycle
cut.  The complete one-generation inverse fibre is already the whole weak
composition simplex, so no spectator erased in that same deletion can
increase its period.

## 7. Final scope

The exact reduced Palm functional still needs the joint alignment of:

* successor visits in the suffix of one predecessor-renewal block;
* the following predecessor gap; and
* the corresponding block decompositions for the particle identities seen
  at later even phases.

Neither the nilpotent Jordan block lengths nor one-time deficit marginals
contain these data.  The genuine mountain process proves that bounded
susceptibility occurs in an exact retained fibre, but that fibre is
Catalan-negligible and outside the long-core Pascal saddle.  Therefore the
global alternatives remain open exactly as stated in the synthesis.

