# Independent audit of the multi-rail gap-energy and linear-density barrier

**Date:** 2026-08-03  
**Method:** pure symbolic rederivation from the definitions in the source;
no finite computation or experimental existence evidence.  
**Verdict:** PASS after the scope clarifications incorporated into the final
source described below.

## 0. Audited source and scope

Source:

`MATH_THEOREM_MULTI_RAIL_GAP_ENERGY_AND_LINEAR_DENSITY_BARRIER_20260803.md`

Final SHA-256:

`0be8dc483ddefb344524e1fb4b1d4714748c34222671ea0cc8b5e19308fe8e17`

The theorem is a necessary lower-signature-capacity result for complete cyclic
Johnson carriers whose audited lower-target capacity is supplied by
coordinate-counted occurrence markers inside resident erosion factors, plus
the explicitly granted boundary cells.  Here `P` counts coordinate--marker
incidences, not necessarily distinct physical rows.  External/nonresident
factors, extra markers outside the erosion intervals, and unrelated occurrence
carriers are outside scope.  No sufficiency or arbitrary-architecture no-go is
claimed.

## 1. One-run q-hull and gap identity

Fix a run of length `L>=D=d+1`, with erosion markers

\[
 z_1=s+d<z_2<\cdots<z_p=t,
 \qquad g_i=z_{i+1}-z_i,\qquad1\le g_i\le D.          \tag{1.1}
\]

For a fixed `q`, a marker `z_i` hits exactly the start interval

\[
                         I_i(q)=[z_i-q+1,z_i].       \tag{1.2}
\]

Their integer hull is `[s+d-q+1,t]`, of size

\[
 t-(s+d-q+1)+1=L-D+q.                               \tag{1.3}
\]

Between consecutive intervals, the uncovered integer starts are exactly

\[
                         (g_i-q)_+.                  \tag{1.4}
\]

These holes are disjoint, so

\[
 H_q(R)=L-D+q-\sum_i(g_i-q)_+.                      \tag{1.5}
\]

Since `g_i<=D=d+1`,

\[
 \sum_{q=1}^d(g_i-q)_+
 =\sum_{q=1}^{g_i-1}(g_i-q)={g_i\choose2},          \tag{1.6}
\]

whereas

\[
 \sum_{q=1}^d(L-D+q)=d\left(L-{D\over2}\right).    \tag{1.7}
\]

Therefore the source's exact identity is correct:

\[
 \boxed{
 \sum_{q=1}^dH_q(R)
 =d\left(L-{D\over2}\right)-\sum_i{g_i\choose2}.}  \tag{1.8}
\]

It also covers `L=D`: the endpoints coincide, `p=1`, and the gap sum is empty.

## 2. Cyclic disjointness and the global ledger

For consecutive maximal positive runs of one coordinate, with the first ending
at `t` and the next beginning at `s'`, positivity gives `s'>=t+2`.  The next
`q`-hull begins at

\[
                         s'+d-q+1\ge s'+1>t,         \tag{2.1}
\]

so same-coordinate run hulls are disjoint.  Across the cyclic cut, lift the
next run by one period `W` and apply the identical inequality.  Cross-coordinate
disjointness is unnecessary because `H_Z` sums coordinate indicators.

Every Johnson transition births one positive coordinate run, hence there are
exactly `W` runs.  Double-counting positive owner--coordinate incidences gives

\[
                         \sum_RL(R)=rW.              \tag{2.2}
\]

Summing (1.8) proves

\[
 \boxed{
 H_Z=U-J,\qquad
 U=Wd\left(r-{D\over2}\right),\qquad
 J=\sum_g{g\choose2}.}                              \tag{2.3}
\]

A run with `p` markers has `p-1` gaps and

\[
                         \sum_i g_i=L-D.             \tag{2.4}
\]

Thus, with `P` counted coordinate by coordinate,

\[
 \boxed{
 G=\sum_R(p(R)-1)=P-W,\qquad
 S=\sum_g g=rW-WD=W(r-d-1).}                        \tag{2.5}
\]

If `S=0`, residency forces every `L=D`, hence `G=0`, `P=W`, and `J=0`.

## 3. Convex and discrete gap energy

For `S>0`, actual positive gaps imply `G>0` and

\[
 J={1\over2}\left(\sum_g g^2-S\right)
 \ge {1\over2}\left({S^2\over G}-S\right).          \tag{3.1}
\]

This is exactly (0.6).  If `S=aG+b`, `0<=b<G`, discrete smoothing of a pair
`g>=h+2` to `(g-1,h+1)` strictly lowers the energy.  Hence the unique minimum
multiset, up to ordering, has `G-b` copies of `a` and `b` copies of `a+1`:

\[
 \boxed{
 J\ge(G-b){a\choose2}+b{a+1\choose2}.}              \tag{3.2}
\]

The bounds remain legal: existence gives `G<=S<=DG`, so `a>=1`, and
`a+1<=D` whenever `b>0`.

## 4. Defect inequality, fractional form, and boundary cells

For a linear word of length `W+d`, the number of `q`-cell starts exceeds the
`W` cyclic starts by

\[
                         (W+d-q+1)-W=D-q.            \tag{4.1}
\]

Therefore the total number of granted boundary cells is exactly

\[
 B_\partial=\sum_{q=1}^d(D-q)={D\choose2}.          \tag{4.2}
\]

If uncovered target mass is `delta`, the omitted target-rank mass is at most
`delta(r-1)`.  Unit cell capacity and target containment in the cell signature
therefore give, integrally or fractionally,

\[
 M-\delta(r-1)
 \le U-J+(r-1){D\choose2}.                          \tag{4.3}
\]

Substituting (3.1) gives exactly the source's (0.8), with the positive-part
integer ceiling only in the integral version.  With

\[
 K=U+(r-1){D\choose2}-M+\delta(r-1),                \tag{4.4}
\]

feasibility implies `J<=K` and `S+2K>0`; hence

\[
 \boxed{
 P=W+G\ge W+{S^2\over S+2K}.}                      \tag{4.5}
\]

The fractional argument uses only linear rank mass and does not assume an
integral assignment.

## 5. Sparse h-rail energy and the coefficient 1/(2h)

For one exact minimum net on a run,

\[
                         \tau(L)=\left\lceil{L\over D}\right\rceil
                         \le {L+d\over D}.           \tag{5.1}
\]

Thus `h` exact nets give

\[
 P\le {hW(r+d)\over D}.                              \tag{5.2}
\]

A canonical residue phase plus endpoint corrections has at most
`tau(L)+1` markers, giving

\[
 P\le {hW(r+2d+1)\over D}.                          \tag{5.3}
\]

At central rank and fixed `h`, either resulting upper bound on `G=P-W` is

\[
                         A_h={hWr\over d}
                              \left(1+O_h(d^{-1})\right),       \tag{5.4}
\]

while

\[
                         S=Wr\left(1-O(d/r)\right).             \tag{5.5}
\]

Consequently

\[
 {S^2\over2A_h}
 ={Wrd\over2h}\left(1+O_h(d^{-1})\right).           \tag{5.6}
\]

After division by `r-1`, the `S/2`, `U-M`, and boundary terms contribute
`O(W)=O(Lambda/d)`.  Since `Wd=Lambda(1+O(1/d))`,

\[
 \boxed{
 \delta\ge{\Lambda\over2h}-O_h\left({\Lambda\over d}\right)
 =\left({1\over2h}-O_h(k^{-1/2})\right)\Lambda.}    \tag{5.7}
\]

Hence the fixed-`h` coefficient is exactly `1/(2h)`, and `h=2` gives `1/4`.
The uniform form for `h=o(d)` is the same leading term with an
`O(Lambda/d)` error.  It forces `h=Omega(d)` for bounded absolute defect, and
more generally for `delta=o(Lambda/d)`; relative defect
`delta/Lambda->0` alone is insufficient.

## 6. Exact odd/even rank-mass equations

Let `r=ceil(k/2)` and `W={k choose r}`.

For odd `k=2m+1`, `r=m+1`, binomial symmetry and
`s{k choose s}=k{k-1 choose s-1}` give

\[
 M={k\over2}\Lambda-{r\over2}W+{k\over2}.          \tag{6.1}
\]

For even `k=2m`, `r=m`, the analogous central-pair calculation gives

\[
 M={k\over2}\Lambda-{k\over4}W+{k\over2}.          \tag{6.2}
\]

Since `Lambda/W=d-epsilon_k`, these are exactly

\[
 {M\over W}
 ={k\over2}(d-\epsilon_k)-{r\over2}+{k\over2W}      \tag{6.3}
\]

in the odd case, and

\[
 {M\over W}
 ={k\over2}(d-\epsilon_k)-{k\over4}+{k\over2W}     \tag{6.4}
\]

in the even case.  Subtracting from
`U/W=d(r-(d+1)/2)` yields respectively

\[
 {U-M\over W}
 ={k\epsilon_k+r-d^2\over2}-{k\over2W},            \tag{6.5}
\]

\[
 {U-M\over W}
 ={k\epsilon_k\over2}+{k\over4}
  -{d(d+1)\over2}-{k\over2W}.                       \tag{6.6}
\]

These reproduce source equations (6.3)--(6.6), including both endpoint terms
`k/(2W)` and all parity signs.

## 7. Epsilon range and the density constants

Minimality of `d` is exactly

\[
 dW+{d+1\choose2}\ge\Lambda,
 \qquad(d-1)W+{d\choose2}<\Lambda.                  \tag{7.1}
\]

Therefore

\[
 \boxed{
 -{{d+1\choose2}\over W}\le\epsilon_k
 <1-{{d\choose2}\over W}.}                         \tag{7.2}
\]

At central rank the binomial estimates give

\[
 \epsilon_k\ge-o(1),\qquad \epsilon_k<1,qquad
 {d^2\over k}\to{\pi\over8},qquad {r\over k}\to{1\over2}. \tag{7.3}
\]

For bounded defect, (6.5)--(6.6) give in both parities

\[
 {K\over kW}={4-\pi\over16}+{\epsilon_k\over2}+o(1),
 \qquad {S\over kW}={1\over2}+o(1).                \tag{7.4}
\]

Insert (7.4) into (4.5) and divide by `rW`.  The `W/(rW)` term is `o(1)`, and
the remaining rational expression is

\[
 \boxed{
 {P\over rW}\ge
 {4\over8-\pi+8\epsilon_k}-o(1).}                  \tag{7.5}
\]

The right side decreases with `epsilon_k`.  Since `epsilon_k<1`, uniformly
over the rounding phase,

\[
 \boxed{
 {P\over rW}\ge {4\over16-\pi}-o(1)
 =0.31108\ldots-o(1).}                              \tag{7.6}
\]

Finally, either sparse rail ledger gives

\[
                         {P\over rW}
 \le {h\over d}(1+o(1)).                            \tag{7.7}
\]

Combining (7.5)--(7.7) proves

\[
 \boxed{
 {h\over d}\ge{4\over8-\pi+8\epsilon_k}-o(1)
 \ge{4\over16-\pi}-o(1).}                          \tag{7.8}
\]

This implication is only for systems satisfying the exact-minimum-net bound
(5.2) or canonical-residue bound (5.3); it does not cover an arbitrary dense
object merely called a rail.

## 8. Final audit boundary

All requested identities, signs, factors, ceilings, parity forms, and density
constants pass.  The only corrections needed were proof-safety statements:

* orient the discrete smoothing step explicitly;
* distinguish coordinate--marker incidences from physical occurrence rows;
* replace ambiguous “vanishing defect” by bounded defect, or
  `delta=o(Lambda/d)`; and
* restrict the architectural conclusion to resident erosion-factor marker
  capacity plus the granted boundary cells.

The theorem remains a necessary capacity barrier.  It does not prove that the
lower density bound is sufficient, and it does not use computation as
existence evidence.
