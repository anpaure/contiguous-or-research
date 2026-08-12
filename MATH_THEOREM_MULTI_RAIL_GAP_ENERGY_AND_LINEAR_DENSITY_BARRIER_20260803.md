# Multi-rail gap energy and the linear-density barrier

**Date:** 2026-08-03  
**Status:** unconditional signature-capacity theorem for every complete
resident cyclic Johnson carrier.  It strengthens the minimum-density
half-defect theorem: two rails still leave asymptotically one quarter of
the strict lower ideal uncovered, and every fixed number of rails leaves
a positive-density defect.  No computation is used.

## 0. Outcome

Put

\[
 W={k\choose r},\qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},\qquad
 M=\sum_{s=1}^{r-1}s{k\choose s},                    \tag{0.1}
\]

let `d` be the optimal lower-bound depth, and write

\[
                         D=d+1.                       \tag{0.2}
\]

Assume `d>=1`.  The identities below also cover the degenerate case
`S=0` by taking `J=0`; formulas containing `1/(P-W)` are stated for
`S>0`.

Let a complete cyclic rank-`r` Johnson carrier have positive coordinate
runs of lengths `L`.  Every run is assumed resident, so `L>=D`.  On its
erosion interval `[s+d,t]`, take any occurrence set which contains the two
mandatory endpoints and hits every owner-supplier interval.  If its
successive occurrence gaps are `g`, then

\[
                         1\le g\le D.                 \tag{0.3}
\]

For a cyclic `q`-cell put

\[
 V_Z(j,q)=\{x:[j,j+q-1]_W\cap Z_x\ne\varnothing\},
 \qquad
 H_Z=\sum_{q=1}^{d}\sum_{j\in\mathbb Z_W}|V_Z(j,q)|.
                                                               \tag{0.3a}
\]

The exact total cyclic signature rank mass is

\[
 \boxed{
 H_Z=U-J,\qquad
 U=Wd\left(r-{D\over2}\right),\qquad
 J=\sum_g {g\choose2}.}                              \tag{0.4}
\]

Thus the obstruction is not merely the number of occurrence markers.
Every unfilled gap carries a convex loss `binom(g,2)` across the `d`
short rows.

Let `P` be the total number of coordinate--marker incidences, counted
separately coordinate by coordinate and run by run.  A single physical
occurrence row supporting several coordinates contributes once for each such
coordinate; `P` is not asserted to count distinct physical rows.  The complete
carrier has exactly `W` positive runs, and hence

\[
 G:=\#\{\hbox{successive gaps}\}=P-W,\qquad
 S:=\sum_g g=W(r-D).                                  \tag{0.5}
\]

Convexity gives

\[
 \boxed{
 J\ge {1\over2}\left({S^2\over P-W}-S\right).}       \tag{0.6}
\]

There is also an exact discrete version: if `S=aG+b`, `0<=b<G`, then

\[
 J\ge (G-b){a\choose2}+b{a+1\choose2}.               \tag{0.7}
\]

If all but `delta` strict-lower targets are represented, even after
granting every linear boundary cell rank `r-1`, then

\[
 \boxed{
 \delta\ge
 \left\lceil
 {M-U+\frac12(S^2/(P-W)-S)
 -(r-1){D\choose2}\over r-1}
 \right\rceil_+.}                                    \tag{0.8}
\]

For fractional target coverage the same right-hand side holds **before**
the integer ceiling, with `delta` interpreted as total uncovered target
mass.

Suppose now that every run uses the union of `h` exact minimum owner nets,
or the union of `h` canonical residue phases with mandatory endpoint
corrections.  For every fixed `h`, at the central rank
`r=ceil(k/2)`, (0.8) gives

\[
 \boxed{
 \delta\ge
 \left({1\over2h}-O_h(k^{-1/2})\right)\Lambda.}       \tag{0.9}
\]

In particular two rails leave at least

\[
 \boxed{
 \delta\ge
 \left({1\over4}-O(k^{-1/2})\right)\Lambda.}         \tag{0.10}
\]

They therefore do **not** dominate the triangular lower marginals, even
fractionally: target rank is an explicit separating linear functional.
More generally, every fixed number of residue rails fails.

The gap inequality can be inverted.  Put

\[
 K=U+(r-1){D\choose2}-M+\delta(r-1).                 \tag{0.11}
\]

Every signature with defect at most `delta` must satisfy

\[
 \boxed{
 P\ge W+{S^2\over S+2K}.}                            \tag{0.12}
\]

For bounded defect and central rank, define

\[
 \epsilon_k={dW-\Lambda\over W}.                     \tag{0.13}
\]

Then

\[
 -{{D\choose2}\over W}\le\epsilon_k
 <1-{{d\choose2}\over W},                           \tag{0.14}
\]

and (0.12) yields the refined necessary density

\[
 \boxed{
 {P\over rW}\ge
 {4\over 8-\pi+8\epsilon_k}-o(1).}                  \tag{0.15}
\]

Uniformly in the possible rounding phase of `d`,

\[
 \boxed{
 {P\over rW}\ge {4\over16-\pi}-o(1)
 =0.311\ldots-o(1).}                                 \tag{0.16}
\]

Thus bounded lower defect requires a positive fraction of all available
erosion occurrences.  Since `h` residue rails supply only
`O(hrW/d)` markers, the number of rails must be `Omega(d)`, not `O(1)`.
More precisely, any bounded-defect canonical `h`-rail system satisfies

\[
 {h\over d}\ge
 {4\over8-\pi+8\epsilon_k}-o(1)
 \ge {4\over16-\pi}-o(1).                            \tag{0.17}
\]

## 1. The exact gap identity on one positive run

Unwrap one positive owner run as

\[
                         T_s,T_{s+1},\ldots,T_t,
 \qquad L=t-s+1\ge D.                                \tag{1.1}
\]

Its erosion interval is

\[
                         R=[s+d,t],\qquad |R|=L-D+1. \tag{1.2}
\]

Let

\[
 z_1=s+d<z_2<\cdots<z_p=t                            \tag{1.3}
\]

be its distinct occurrence markers.  When `L=D`, the two displayed
endpoints coincide, `p=1`, and there are no gaps.  Otherwise put

\[
                         g_i=z_{i+1}-z_i
 \qquad(1\le i<p).                                   \tag{1.4}
\]

The owner-hitting condition is exactly `g_i<=D`; positivity gives
`g_i>=1`.

For `1<=q<=d`, a `q`-cell start sees a marker `z_i` exactly when it lies
in

\[
                         [z_i-q+1,z_i].               \tag{1.5}
\]

The hull of these start intervals is

\[
                         [z_1-q+1,z_p],               \tag{1.6}
\]

of cardinality

\[
                         L-D+q.                       \tag{1.7}
\]

Between two successive markers, the number of hull starts missed by both
is exactly

\[
                         (g_i-q)_+.                   \tag{1.8}
\]

### Lemma 1.1 (one-run gap formula)

The number `H_q(R)` of `q`-cell starts hit by the run is

\[
 H_q(R)=L-D+q-\sum_{i=1}^{p-1}(g_i-q)_+.             \tag{1.9}
\]

Summing over all short rows,

\[
 \boxed{
 \sum_{q=1}^{d}H_q(R)
 =d\left(L-{D\over2}\right)
 -\sum_{i=1}^{p-1}{g_i\choose2}.}                   \tag{1.10}
\]

#### Proof

The intervals in (1.5) cover their hull except for the disjoint open
gaps counted in (1.8), proving (1.9).  Since `g_i<=D=d+1`,

\[
 \sum_{q=1}^{d}(g_i-q)_+
 =\sum_{q=1}^{g_i-1}(g_i-q)
 ={g_i\choose2}.                                    \tag{1.11}
\]

Finally,

\[
 \sum_{q=1}^{d}(L-D+q)
 =d(L-D)+{dD\over2}
 =d\left(L-{D\over2}\right).                       \tag{1.12}
\]

Substitution gives (1.10). \(\square\)

## 2. Globalization over the complete carrier

Different positive runs of one coordinate contribute disjoint start
hulls.  Indeed, if one run ends at owner index `t` and the next begins at
`s'>t`, then the coordinate is absent between them, so `s'>=t+2`.  The
leftmost start in the next run's `q`-hull is

\[
 s'+d-q+1\ge s'+1>t,                                 \tag{2.1}
\]

for `q<=d`.  The same argument works across the cyclic cut after
unwrapping that coordinate's runs.

The complete cyclic Johnson carrier has exactly `W` positive coordinate
runs, one born at every Johnson transition, and their lengths sum to
`rW`.  Therefore summing (1.10) gives (0.4).

Also, every run with `p` markers has `p-1` successive gaps, while

\[
 \sum_i g_i=L-D.                                     \tag{2.2}
\]

Summing over the `W` runs proves (0.5).

### Lemma 2.1 (sharp discrete convexity)

Assume `S>0`, and write

\[
                         S=aG+b,\qquad0\le b<G.       \tag{2.3}
\]

Then

\[
 J\ge (G-b){a\choose2}+b{a+1\choose2},              \tag{2.4}
\]

with equality only when the global gap multiset consists of `G-b` copies
of `a` and `b` copies of `a+1`.

#### Proof

If two positive integer gaps satisfy `g>=h+2`, replacing them by
`g-1` and `h+1` preserves their sum and strictly decreases
`binom(g,2)+binom(h,2)`.  Iteration balances all gaps to the two values in
(2.4).  The owner-hitting constraint causes no problem: its existence
implies `S<=DG`, so the balanced values are at most `D`. \(\square\)

The Cauchy bound

\[
 \sum_g g^2\ge {S^2\over G}                          \tag{2.5}
\]

and the identity

\[
 J={1\over2}\left(\sum_g g^2-S\right)               \tag{2.6}
\]

give (0.6).

## 3. Exact defect and density inequalities

Let `B_<r` be the nonempty strict lower ideal.  If all but `delta` of its
targets are assigned to distinct short cells, their total rank is at least

\[
                         M-\delta(r-1).               \tag{3.1}
\]

The cyclic cells have total signature rank `H_Z=U-J`.  A linear word of
length `W+d` has at most

\[
                         B_\partial={D\choose2}       \tag{3.2}
\]

additional short boundary cells.  Granting every one a distinct target of
rank `r-1` gives the necessary inequality

\[
 M-\delta(r-1)
 \le U-J+(r-1)B_\partial.                            \tag{3.3}
\]

Combining (3.3) with (0.6) proves (0.8).

The argument is unchanged for a fractional assignment: multiply each
target rank by its covered mass, use unit capacity at every cell, and note
that a target assigned to a cell has rank at most the cell's signature
rank.  If the total uncovered target mass is `delta`, its omitted rank
mass is at most `delta(r-1)`.  Thus (3.3) still holds.

For the inverse form, (3.3) says `J<=K`, with `K` from (0.11).  Hence

\[
 {1\over2}\left({S^2\over P-W}-S\right)\le K.        \tag{3.4}
\]

Whenever a feasible assignment exists, the denominator below is positive,
and rearrangement gives (0.12).  Integer ceilings may of course be placed
on its right side.

## 4. Unions of `h` occurrence rails

Let `tau(L)=ceil(L/D)` be the exact minimum owner-net size on a run.
If a run carries the union of `h` exact minimum nets, then, without making
any independence or phase assumption,

\[
                         p(R)\le h\tau(L).            \tag{4.1}
\]

The complete run ledger gives

\[
 P\le {hW(r+d)\over D}.                              \tag{4.2}
\]

If instead each rail is one canonical residue class plus the mandatory
endpoints, then each has size at most `tau(L)+1`, and

\[
 P\le {hW(r+2d+1)\over D}.                           \tag{4.3}
\]

Put

\[
\begin{aligned}
 A_h^{\min}&=W\left({h(r+d)\over D}-1\right),\\
 A_h^{\rm res}&=W\left({h(r+2d+1)\over D}-1\right).
\end{aligned}                                        \tag{4.4}
\]

Thus `G=P-W` is at most the corresponding `A_h`.  Since the right side of
(0.6) decreases with `G`, exact minimum rails obey

\[
 \delta\ge
 \left\lceil
 {M-U+\frac12(S^2/A_h^{\min}-S)
 -(r-1)B_\partial\over r-1}
 \right\rceil_+,                                    \tag{4.5}
\]

and canonical residue rails obey the same bound with
`A_h^{res}`.  These are exact finite-parameter obstructions.

## 5. Central-rank asymptotics

Take `r=ceil(k/2)`.  The standard central estimates are

\[
 d=\Theta(\sqrt k),\qquad
 Wd=\Lambda\bigl(1+O(d^{-1})\bigr),\qquad
 {M\over\Lambda}=r-\Theta(\sqrt k).                 \tag{5.1}
\]

For fixed `h`, either quantity in (4.4) satisfies

\[
 A_h={hWr\over d}\bigl(1+O_h(d^{-1})\bigr).         \tag{5.2}
\]

Also

\[
 S=Wr\bigl(1-O(d/r)\bigr),\qquad
 U-M=O(kW),\qquad
 (r-1)B_\partial=o(M).                               \tag{5.3}
\]

Consequently

\[
 {1\over2}{S^2\over A_h}
 ={Wrd\over2h}\bigl(1+O_h(d^{-1})\bigr).            \tag{5.4}
\]

After division by `r-1`, the terms `S/2`, `U-M`, and the boundary
allowance contribute only `O(W)=O(\Lambda/d)`.  Since `Wd=Lambda(1+O(1/d))`,
(4.5) gives

\[
 \delta\ge {\Lambda\over2h}-O_h\left({\Lambda\over d}\right)
 =\left({1\over2h}-O_h(k^{-1/2})\right)\Lambda.      \tag{5.5}
\]

This proves (0.9)--(0.10).  The same calculation is uniform for
`h=o(d)`, in the form

\[
                         \delta\ge
 {\Lambda\over2h}-O\left({\Lambda\over d}\right).  \tag{5.6}
\]

Thus bounded absolute defect, and more generally
`delta=o(Lambda/d)`, forces `h=Omega(d)` within the stated sparse
residue-rail model.  The weaker condition `delta/Lambda->0` alone does not:
it is compatible with `h->infinity` and `h=o(d)`.

## 6. The refined linear occurrence-density constant

Define `epsilon_k` by (0.13).  The depth inequality and its strict
minimality predecessor are

\[
 dW+{D\choose2}\ge\Lambda,
 \qquad
 (d-1)W+{d\choose2}<\Lambda.                         \tag{6.1}
\]

They give (0.14).  In particular

\[
                         -o(1)\le\epsilon_k<1.        \tag{6.2}
\]

For completeness, the rank-mass ledger gives exact parity-specific forms.
If `k=2m+1` and `r=m+1`, then

\[
 {U-M\over W}
 ={k\epsilon_k+r-d^2\over2}-{k\over2W}.             \tag{6.3}
\]

If `k=2m` and `r=m`, then

\[
 {U-M\over W}
 ={k\epsilon_k\over2}+{k\over4}
 -{d(d+1)\over2}-{k\over2W}.                        \tag{6.4}
\]

Indeed, in the odd case

\[
 {M\over W}
 ={k\over2}(d-\epsilon_k)-{r\over2}+{k\over2W},    \tag{6.5}
\]

while in the even case

\[
 {M\over W}
 ={k\over2}(d-\epsilon_k)-{k\over4}+{k\over2W}.    \tag{6.6}
\]

Using

\[
                         {d^2\over k}\longrightarrow {\pi\over8},
 \qquad {r\over k}\longrightarrow {1\over2},       \tag{6.7}
\]

both parities yield, for bounded `delta`,

\[
 {K\over kW}
 ={4-\pi\over16}+{\epsilon_k\over2}+o(1),
 \qquad
 {S\over kW}={1\over2}+o(1).                        \tag{6.8}
\]

Substitution into (0.12), followed by division by `rW`, proves (0.15).
Since the right side decreases with `epsilon_k` and `epsilon_k<1`, (0.16)
follows.  Equations (4.2)--(4.3) give

\[
                         {P\over rW}
 \le {h\over d}(1+o(1)),                             \tag{6.9}
\]

for a union of `h` exact or canonical sparse rails.  Combining (6.9)
with (0.15)--(0.16) proves (0.17).

## 7. Structural conclusion and scope

The earlier raw count `q|Z_x|` treats the `q` start intervals generated by
different occurrences as if they were disjoint.  They are not.  Formula
(0.4) prices their overlap exactly: a gap of length `g` loses
`binom(g,2)` units of rank capacity across all short rows.

For `h` optimally interlaced sparse rails, typical gaps have length about
`D/h`, and their total gap energy is asymptotically `M/(2h)`.  This is why
the first coarse scale `h=2` still loses one quarter of the lower ideal.

The theorem is deliberately a lower-side signature theorem.  It assumes
that all lower-target occurrence capacity under audit is supplied by the
coordinate-counted markers inside these resident erosion factors, together
with the explicitly granted standard boundary cells.  It also assumes the
standard mandatory erosion endpoints and owner-hitting condition, but it does
not assume probabilistic independence, a particular residue choice, or any
upper-deck property.  Within that scope it applies before topology, upper
witnesses, common-cap matching, and regeneration are considered.  External or
nonresident factors, extra markers outside the erosion intervals, and other
occurrence carriers add capacity and are not ruled out here.

It does not say that positive linear occurrence density is sufficient.
It proves only the necessary conclusion

\[
 \boxed{
 \text{bounded lower defect requires }P=\Omega(rW),
 \text{ hence }\Omega(d)\text{ sparse rails per run}.}
\]

Consequently, any construction whose lower-target capacity is confined to
this resident erosion-factor architecture must replace a bounded sparse rail
sidecar satisfying (4.1) or its canonical analogue by a genuinely dense
erosion schedule, and then solve the remaining incidence-level compiler and
upper-carrier gates on that dense schedule.  No conclusion is made about an
arbitrary architecture with additional occurrence carriers.
