# K15 octahedral orbit packing and regenerative descent

Date: 2026-07-30  
Lane: K  
Status: **proved a 105-atom, seven-orbit, all-depth-safe structured descent
from 1425 to 1305 positive length-four runs; proved the exact baseline
maximum weight within the individually hard-safe full-orbit catalogue; and
isolated the final one-full-orbit stall. Zero residence and compiler
feasibility are not proved.**

## 0. Main result

Start from the authenticated \(k=15\) factor with physical cycles
\(6390,45\). It has minimum positive run four and

\[
(\Phi^-_5,\Phi^+_5)=(1425,5760),                         \tag{0.1}
\]

where the entries are positive-run and zero-gap curvature summed over all
fifteen coordinates.

There is an explicit sequence of seven complete
\(\mathbb Z_{15}\)-orbits of octahedral \(C_6\) switches. Each orbit has
fifteen atoms. Every one of the 105 translate prefixes is:

* a literal squarefree Johnson factor;
* degree two on the complete middle owner deck;
* exact on both \(q=1\) colour multisets;
* complete on every fixed lower and upper shadow through depth seven; and
* one-sided positive-resident, with minimum positive run four.

The exact trajectory is

\[
\begin{array}{c|c|c}
\text{completed orbit}&\Phi^-_5&\Phi^+_5\\ \hline
0&1425&5760\\
1&1425&5730\\
2&1395&5700\\
3&1365&5730\\
4&1350&5745\\
5&1335&5700\\
6&1320&5700\\
7&1305&5700.
\end{array}                                                   \tag{0.2}
\]

Thus

\[
\boxed{\Delta(\Phi^-_5,\Phi^+_5)=(-120,-60).}            \tag{0.3}
\]

Equivariance makes the final coordinate profile uniform:

\[
(\phi^-_{5,x},\phi^+_{5,x})=(87,380)
\qquad(x\in\mathbb Z_{15}),                              \tag{0.4}
\]

down from \((95,384)\). The positive defect falls by

\[
\frac{120}{1425}=\frac8{95}>8.4\%.                       \tag{0.5}
\]

The final physical component lengths are

\[
1990,1990,1990,115,115,115,75,45.                        \tag{0.6}
\]

This is a substantial literal descent. It is not a biresident carrier:
the minimum zero run is one and 1995 zero runs remain shorter than four.
The component count also rises from two to eight.

## 1. Exact cyclic symmetry

Let \(\rho\) rotate coordinate labels by \(i\mapsto i+1\pmod {15}\).

### Proposition 1.1 (factor equivariance)

The authenticated edge factor is \(\rho\)-invariant. On its two oriented
source cycles, \(\rho\) acts by

\[
+1704\pmod {6390},\qquad +33\pmod {45},                 \tag{1.1}
\]

both of order fifteen. Hence every literal atom \(g\) has a complete
translation orbit

\[
\mathcal O(g)=\{\rho^t g:0\le t<15\}.                   \tag{1.2}
\]

Every rank-eight owner necklace is free, so every generic atom orbit has
size fifteen.

### Proposition 1.2 (orbit charge identity)

Put

\[
\kappa_x(g)=\phi^-_{5,x}(F)-\phi^-_{5,x}(F^g),\qquad
w(g)=\sum_x\kappa_x(g).                                 \tag{1.3}
\]

If all translates in \(\mathcal O(g)\) compose additively, their union
reduces every coordinate by \(w(g)\):

\[
\phi^-_{5,x}(F)-\phi^-_{5,x}(F^{\mathcal O(g)})
=\sum_{t=0}^{14}\kappa_{x-t}(g)=w(g).                   \tag{1.4}
\]

The same identity holds for zero-gap curvature.

#### Proof

Coordinate rotation sends the \(x\)-charge of \(\rho^t g\) to the
\((x-t)\)-charge of \(g\). Sum over \(t\). Additivity is a physical
hypothesis and is checked below by complete replay. QED.

## 2. Complete indexed generic census

A generic octahedral atom is specified by a rank-six core \(R\), a
four-label set \(L\), and one of four triangle reversals in its \(K_4\)
cell. Brute iteration would inspect

\[
\binom{15}{6}\binom94\cdot4=2\,522\,520                 \tag{2.1}
\]

cells. The exact edge index is much smaller.

### Lemma 2.1 (42-incidence index)

For a selected Johnson edge \(UV\), put

\[
I=U\cap V,\qquad J=U\cup V,\qquad |I|=7,\ |J|=9.        \tag{2.2}
\]

Choose \(i\in I\) and \(\ell\notin J\), and define

\[
R=I-i,\qquad L=(J\setminus R)+\ell.                     \tag{2.3}
\]

Then \(UV\) is exactly the directed cell edge \(q_{i\ell}\). Conversely
every directed cell incidence of \(UV\) arises uniquely this way. Thus
each selected edge has \(7\cdot6=42\) directed incidences.

#### Proof

The lower and upper colours of \(q_{i\ell}\) are \(R+i=I\) and
\(R+(L-\ell)=J\). These recover \(i=I-R\) and \(\ell=L-J\). QED.

The baseline index contains

\[
6435\text{ selected edges},\quad
270270\text{ directed incidences},\quad
221445\text{ nonempty }(R,L)\text{ cells}.              \tag{2.4}
\]

Inspecting four triangle masks per key gives

\[
\begin{array}{c|r}
\text{type relative to fixed }z&\text{alternating atoms}\\ \hline
AA&534\\
BB&445\\
z\text{-active mixed}&267\\
z\text{-spectator all-cross}&89\\ \hline
\text{total}&1335.
\end{array}                                               \tag{2.5}
\]

The all-cross class is essential: it fixes the \(z\)-shore AA/BB spectra
but can alter positive curvature in other coordinates.

The 1335 atoms form 89 free translation orbits. Individual physical replay
leaves 330 atoms, or 22 orbits, that are both all-depth complete and
positive-resident.

## 3. Baseline maximum-weight orbit packing

Every one of the 22 individually hard-safe baseline orbits was replayed
through all fifteen canonical prefixes; all complete packets remain
hard-safe. Exactly three have negative positive-curvature delta:

\[
(-30,-30),\qquad(-30,+30),\qquad(-15,+15).              \tag{3.1}
\]

### Theorem 3.1 (baseline orbit-catalogue optimum)

Within the complete catalogue of individually hard-safe generic full
orbits, the maximum additive positive-curvature weight is

\[
30+30+15=75.                                            \tag{3.2}
\]

The three positive packets compose and attain this bound. A fourth
zero-primary packet of delta \((0,-30)\) also composes, giving

\[
(1425,5760)\longmapsto(1350,5745).                      \tag{3.3}
\]

#### Proof

The sum of all positive first-coordinate weights in the complete hard-safe
orbit catalogue is 75, an upper bound. The explicit four-orbit replay
attains it and then improves the secondary coordinate by thirty without
changing the primary value. Every translate prefix passes. QED.

This is not a maximum over packets built from individually unsafe atoms
whose casualties cancel, partial orbits, larger circuits, or compiler
constraints.

### Proposition 3.2 (literal atom conflict graph)

The protected pure-AA translation bank consists of five complete orbit
classes, hence 75 physical atoms.  Give two atoms an edge when their
six-owner supports intersect.  The exact conflict graph has no edges:

\[
|V|=75,\qquad |E|=0.                                  \tag{3.4}
\]

Consequently its lexicographic maximum-weight independent set for decreasing
\((\Phi^-_5,\Phi^+_5)\) contains the two positive-primary orbit classes and
one zero-primary, secondary-improving class, 45 atoms total.  Literal replay
gives

\[
(1425,5760)\longmapsto(1365,5730).                    \tag{3.5}
\]

The empty owner graph proves simultaneous degree compatibility for this
bank.  It does not by itself prove shadow compatibility; the latter follows
from the full final and prefix replay.  The larger regenerative construction
therefore uses iterative re-census rather than treating pairwise conflicts
as a complete resource model.

## 4. Regeneration under re-census

At state \((1350,5745)\), the complete atlas contains

\[
1350\text{ atoms},\qquad24\text{ individually hard-safe orbits}, \tag{4.1}
\]

with type counts

\[
540\ AA,\quad450\ BB,\quad270\text{ mixed},\quad90\text{ all-cross}. \tag{4.2}
\]

A fresh all-cross orbit has delta \((-15,-45)\), giving

\[
(1350,5745)\longmapsto(1335,5700).                      \tag{4.3}
\]

Subsequent complete-orbit replays activate

\[
(1335,5700)\longmapsto(1320,5700),                      \tag{4.4}
\]

\[
(1320,5700)\longmapsto(1305,5700).                      \tag{4.5}
\]

Regeneration includes both genuinely new atoms and atoms present earlier
with neutral primary charge that become improving after another orbit.

### Theorem 4.1 (seven-orbit descent)

Close each seed row below under all fifteen coordinate translations, in
the displayed order:

\[
\begin{array}{c|l|c}
\text{stage}&\text{seed old}\longrightarrow\text{seed new}
&\Delta(\Phi^-_5,\Phi^+_5)\\ \hline
1&
\begin{array}{l}
(28779,30825),(29033,31080),(29034,30826)\\
\to(28779,30826),(29033,30825),(29034,31080)
\end{array}&(0,-30)\\[2mm]
2&
\begin{array}{l}
(16889,17905),(17912,19952),(18929,18936)\\
\to(16889,18929),(17905,17912),(18936,19952)
\end{array}&(-30,-30)\\[2mm]
3&
\begin{array}{l}
(29214,31258),(29270,31254),(29274,31314)\\
\to(29214,31254),(29270,31314),(29274,31258)
\end{array}&(-30,+30)\\[2mm]
4&
\begin{array}{l}
(3197,17533),(1661,18013),(3677,19549)\\
\to(3677,18013),(3197,19549),(1661,17533)
\end{array}&(-15,+15)\\[2mm]
5&
\begin{array}{l}
(1151,17519),(3167,17503),(3183,19535)\\
\to(1151,17503),(3167,19535),(3183,17519)
\end{array}&(-15,-45)\\[2mm]
6&
\begin{array}{l}
(1947,3994),(3867,18203),(18330,20250)\\
\to(1947,3867),(3994,18330),(18203,20250)
\end{array}&(-15,0)\\[2mm]
7&
\begin{array}{l}
(2995,4003),(3507,7587),(6579,7075)\\
\to(2995,7075),(3507,4003),(6579,7587)
\end{array}&(-15,0).
\end{array}                                               \tag{4.6}
\]

Every stage-start orbit has pairwise disjoint six-owner supports. Every old
edge is selected, every new edge absent, and every completed orbit restores
translation invariance.

#### Proof

The deterministic chain applies all 105 switches in stage/translation
order. After every translate it traverses the complete factor, checks
Johnson degree two, recomputes every lower/upper fixed window through depth
seven, and recomputes every positive run. The completed-orbit curvatures
are exactly (0.2). An independent implementation reproduced the full
prefix chain. QED.

The final coordinate shift acts on the eight components as

\[
[2,0,1,4,5,3,6,7],                                     \tag{4.7}
\]

so the three 1990-cycles and three 115-cycles form component orbits, while
the 75- and 45-cycles are individually invariant.

## 5. Per-atom capacity and graph scope

For the \(r-1\) core coordinates, one atom is a three-path positive-tail
exchange; for the three active labels it is a two-path exchange; the fourth
label is a spectator. Therefore one positive-resident atom removes at most

\[
2(r-1)+3=2r+1.                                         \tag{5.1}
\]

At \(k=15\), this is at most fifteen. Complete positive repair needs at
least

\[
\left\lceil\frac{1425}{15}\right\rceil=95              \tag{5.2}
\]

atoms, and a symmetry-preserving repair needs at least seven full orbits.
The construction uses seven orbits and 105 atoms, so orbit count is not
the obstruction.

Owner/edge conflict graphs certify binary degree compatibility but not
all-depth resource survival. If a target has two old witnesses, one atom
may delete each; both single switches remain safe while their union creates
a hole. The exact resource condition is

\[
\mu_\tau+\sum_{g\in I}\delta_g(\tau)\ge1
\quad\text{for every required target }\tau.             \tag{5.3}
\]

Hence a theorem-level packing needs a common protected witness bank,
disjoint local replacements, or complete final replay. This report uses
the third. It does not check COMP3, the three Pascal compiler packages,
the safe opening, or terminal suffix cells.

## 6. Exact one-full-orbit stall

At \((1305,5700)\), the complete generic index has

\[
1365\text{ atoms in }91\text{ free translation orbits}. \tag{6.1}
\]

Every individually hard-safe orbit was replayed through all fifteen
prefixes. Exactly 23 complete packets remain hard-safe; none has negative
first-coordinate delta. Their delta histogram is

\[
\begin{array}{c|r@{\qquad}c|r}
\Delta&\#&\Delta&\#\\ \hline
(0,-60)&1&(0,-30)&2\\
(0,-15)&4&(0,0)&3\\
(0,+60)&1&(0,+75)&1\\
(+15,-45)&1&(+15,-15)&1\\
(+15,0)&1&(+15,+45)&2\\
(+15,+60)&1&(+30,-30)&1\\
(+30,-15)&1&(+30,0)&2\\
(+45,-30)&1.
\end{array}                                               \tag{6.2}
\]

### Corollary 6.1 (scoped stall)

No single complete translation orbit of a generic octahedral \(C_6\) can
continue the strict positive descent while preserving every shadow and
positive residence at each canonical prefix.

Among the 23 hard-safe packets, exactly 12 are primary-neutral, meaning that
their first-coordinate delta is zero.  For each of these twelve routers, an
independent H100 replay applied all fifteen prefixes, rebuilt the complete
generic octahedral atlas at the intermediate factor, and then tested every
strict full-orbit successor through its own fifteen prefixes.

### Theorem 6.2 (scoped neutral-router two-step stall)

No ordered pair

\[
\text{primary-neutral hard-safe full orbit}
\quad\longrightarrow\quad
\text{strict hard-safe full orbit}                    \tag{6.3}
\]

continues the descent from \((1305,5700)\) within the complete freshly
recensed generic octahedral \(C_6\) library.

This excludes all twelve first routers and every full-orbit second step, not
only secondary-improving routers.  It does not exclude a positive-primary-
cost router repaid by a larger second drop, a jointly safe compound of
individually failing orbits, a partial non-equivariant packing, or a larger
alternating circuit.  It is not a C6 impossibility theorem.

## 7. Frozen artifacts

The authoritative chain replay is:

    scratch/audit_k15_iterative_octahedral_orbit_descent_20260730.py
    5c514fe65761dc392e13f1daff15018e08f4c4707633d0a77abdda22c0505626

    scratch/k15_iterative_octahedral_orbit_descent_20260730.audit.json
    3be199c2304ff370afed0116666bedbae75a9be3dd88137fd7898091d117f346

    scratch/k15_iterative_octahedral_orbit_descent.factor.json
    2458e2c70234bca21ddc21c84160a659143e73ee2c762a105df53250608f32ea

The complete remote neutral-router two-step portfolio is:

    scratch/k15_c6_iterative_two_step_remote_20260730/
      k15_c6_neutral_router_two_step_portfolio_20260730.audit.json
    4c07c1d418b649e8544068edf0cc437cc5bf06da10862496d11b72a077b9f55a

Its worker scripts have SHA-256

    e2bf50d956ddfba397a0a83598490b18f66770dc4b2a56a50238daced76c1e3a
    59b6e0be1d3f8f89522f0bbb3c9193ccb9d3da7773bf129cdfc73a99665e722f

and its deterministic freezer has SHA-256

    cc7051a94c2b2953a666f81fb508ed50a1d302ef28a05a0ba8149afdfc58c1e4

The literal protected-AA conflict-graph/maximum-weight packing replay is:

    scratch/audit_k15_octahedral_translation_packing_20260730.py
    07e18827bb63ed98de20b4c5e43fe9f94ecd8706f86f85527d4f70d823047ea3

    scratch/k15_octahedral_translation_packing_20260730.audit.json
    c8e7d2fa15b27c3bc1edbef8b140d4b7fb5746dc83e3267d65394fb8ec9a951b

    scratch/k15_octahedral_translation_descent_r1.factor.json
    bf6844e697ec86bee4da19868d7847cacec19bcff7d70e3879ef2a9844830f5d

The complete generic index and full-orbit catalogue programs are:

    scratch/search_k15_indexed_octahedral_recensus_20260730.py
    3a42e6a73838b1dcf4eaa9963aa1fe0dae75fd5d5cabaeffaf4e91de47dbe2b0

    scratch/audit_k15_complete_full_orbit_catalogue_20260730.py
    0fde80a1b89a629b31fc6d9fd33fc5ecb3d9755ae46c61aa114ad75351025139

The frozen baseline and first regenerative re-census outputs are:

    scratch/k15_octahedral_recensus_baseline.audit.json
    34c9c68ccf02c66959d9ff3a74cf51fa1f729826886156cb956a901bfeb

    scratch/k15_full_orbit_catalogue_baseline.audit.json
    8092b1983ffa59c3656d29b28c893de74e25135a9d27fd39dd57981fe9f19f98

    scratch/k15_octahedral_recensus_r2.audit.json
    aaebb3b5a0bfc5d6a3b725c9183b6f642e7ebbdfc92d897e6849d3ccb7e0d520

The independently replayed final recensus and complete full-orbit stall
catalogue are:

    scratch/k15_octahedral_recensus_final1305.audit.json
    8ead1f2faeb778edf8695ec3a47fd4d6509e01fcee4a954a86bee57b5742e346

    scratch/k15_full_orbit_catalogue_final1305.audit.json
    8f9ee7c51ee4c82201462b813484d572891d3d4c25fc7213bf69cb98185821fa

## 8. Resource discipline

The complete generic re-censuses ran on one H100 CPU core, never the GPU,
under:

    ulimit -v 393216
    OPENBLAS_NUM_THREADS=1
    OMP_NUM_THREADS=1
    MKL_NUM_THREADS=1
    nice -n 15
    taskset -c 61 or 63
    timeout 300

The indexed script is 10.5 KB and each input factor about 82.5 KB. No
sustained local search, SAT solve, or high-memory local process was used.

## 9. Final boundary

The requested finite target is achieved:

\[
\boxed{1425\longrightarrow1305}
\]

using only exact octahedral atoms, with no shadow loss and no positive
residence regression. The library is genuinely regenerative: re-census
exposes or activates further improving packets.

The stopping point is now both the complete one-full-orbit stall of
Corollary 6.1 and the primary-neutral-router two-step stall of Theorem 6.2.
The next finite class must use a positive-primary-cost router repaid later, a
simultaneous/non-orbit C6 packing, or a larger-support atom.  Independently,
the all-\(k\) theorem still needs a common protected witness/compiler bank;
finite replay at \(k=15\) does not supply that induction.

No biresidence, S3, COMP3, k16 lift, or coefficient-one conclusion is
claimed.
