# Big-picture programme after the finite-case freeze

## 1. Objective and current theorem ledger

Let \(\nu(k)\) be the minimum length for the nonzero masks and

\[
                  W(k)=\binom{k}{\lfloor k/2\rfloor}.
\]

The original problem has answer length \(N(k)=\nu(k)+1\), because one zero
is necessary and sufficient for the zero mask.

The exact values currently certified are

\[
 \nu(1),\ldots,\nu(10)=1,2,4,7,12,21,37,72,128,254,
 \qquad \nu(12)=926.
\]

The cases \(11,13,14,\ldots,19\) remain open.  The leading conjecture is

\[
                         \nu(k)=B(k),
\]

where \(B(k)\) is the rank-slack lower bound.  In particular this predicts
\(\nu(k)=W(k)+O(\sqrt{k})\).  The proved general asymptotic bounds remain

\[
          W(k)\le \nu(k)\le(\sqrt2+o(1))W(k).
\]

Finite repair of the stored fourteen-bit path is no longer the active
programme.  The first target is the all-dimensional theorem

\[
                         \nu(k)=(1+o(1))W(k).           \tag{1.1}
\]

Only after (1.1) is understood should the construction be tightened to the
additive rank-slack scale.

## 2. Why wreath factors are the right global skeleton

Put \(k=2m+1\).  The Mütze--Standke--Wiechert construction partitions every
middle \(m\)-set into exactly

\[
                         \operatorname{Cat}_m
\]

minimum odd cycles.  Each cycle is a cyclic coordinate order and its
\(2m+1\) middle masks are the cyclic \(m\)-intervals of that order.  Thus the
middle layer, which was the Sperner bottleneck, is solved **exactly in every
dimension**.

Within one wreath, every coordinate has a run of length \(m\).  Consecutive
intersections and unions are precisely the shorter and longer cyclic
intervals of the same coordinate order.  Consequently, if an exact wreath
factor can be chosen so that its cyclic intervals cover every rank in

\[
       m-H,\ldots,m+H,qquad H=\sqrt m\,\omega(m),
       \quad\omega(m)\longrightarrow\infty,
\]

then the wreaths can be linearized with \(o(W)\) seam cost.  The proven
truncated chain-product construction covers both outer tails in another
\(o(W)\) entries.  This would prove (1.1).

So the asymptotic problem has been reduced to **vertical resolution of an
exact wreath factor**, rather than construction of one enormous OR array.

## 3. The continuous problem is completely solved

For every rank \(r\), let \(B_r\) send a cyclic order to its incidence
vector of cyclic \(r\)-intervals.  An exact middle factor is a zero-one vector
\(x\) satisfying

\[
                             B_mx={\bf1}.
\]

Petr--Turek's four-order kernel vectors are exact rank selectors.  Their
coordinate translates span every zero-point-marginal discrepancy at every
rank.  Hence, for every exact middle factor \(x\), there is a **real signed**
correction \(z\in\ker B_m\) making all vertical rank vectors perfectly
balanced simultaneously.

The former gap was entirely integrality: a signed selector need not replace
disjoint selected wreaths by disjoint unselected wreaths.

## 4. New all-dimensional integral theorem

Let \(F_m\) be the explicit MSW factor and compare it with its image under a
coordinate transposition.  The bipartite interaction graph has one edge for
every middle mask; every connected component can be switched independently
without changing middle coverage.

For \(\tau=(2\ 3)\), every Dyck word \(R\) of semilength \(m-2\) supplies a
sealed two-for-two component.  Its old blocks are indexed by

\[
                         1100R,\qquad1010R.
\]

Therefore the exact factor fibre contains an integral Boolean cube of
dimension

\[
          \operatorname{Cat}_{m-2}
            =\left(\frac1{16}+O(m^{-1})\right)
               \operatorname{Cat}_m.                  \tag{4.1}
\]

At rank \(m-1\), each switch is exactly one elementary Petr--Turek square,
and the four-target supports of the switches in (4.1) are pairwise disjoint.
This is the first positive-density integral lift of the continuous selector
space.

The identity is stable under every complete Dyck prefix.  If \(P,R\) have
semilengths \(s,m-s-2\), then

\[
                         P1100R,\qquad P1010R
\]

give a legal two-for-two component for the shifted transposition
\((2s+2\ 2s+3)\).  For fixed \(s\) this yields

\[
              \operatorname{Cat}_s
              \operatorname{Cat}_{m-s-2}              \tag{4.2}
\]

independent components.  The proof is the MSW concatenation law

\[
             \rho(PQ)=(\rho(P),2s+\rho(Q)),
\]

followed by the same four-position cut table.  Summing (4.2) over all
boundaries gives \(\operatorname{Cat}_{m-1}\) contextual selector
occurrences.  Different depths can overlap, so this is a recursive atlas of
legal cubes, not one flat cube.

## 5. What the component analysis actually permits

For a switch component \(K\), write

\[
 \Delta_{K,r}=B_r({\bf1}_{K\cap\tau F_m}
                   -{\bf1}_{K\cap F_m}).
\]

The local size-two charts do **not** themselves give a bulk frame.  Their
rank-\(m-1\) projections are linearly independent over every field, and
their combined support is only \(O(W/m)\) of that layer.  Consequently no
nonzero combination of them can change a deeper rank while preserving a
completed first shadow.  They are sparse final absorbers, not a recursive
Haar basis.

It was tempting to declare the complete interaction-component hierarchy the
bulk solution.  The exact missing-mask calculation shows that this is still
too optimistic for one fixed transposition.

An exact uniform resolution is stronger than necessary.  If `c_S(F)` is the
number of cyclic occurrences of a central-band target in a factor, the
renormalized excess

\[
 \Phi_H(F)=\sum_{q\le H}\left[
    \sum_{|S|=m-q}(c_S(F)-1)_+-(W-N_q)
 \right]
 +\text{the complementary upper terms}                 \tag{5.1}
\]

is exactly the total number of missing central-band masks.  Therefore the
weakest useful component theorem only has to construct a reachable exact
factor with \(\Phi_H(F)=o(W)\).  A potential-descent or randomized absorption
argument on the full component hierarchy is sufficient; perfect
multiplicity balance at every target is not required.

Component resampling has an exact heat-bath law.  For any factor `F` and
transposition `tau`, independently selecting one side of every interaction
component gives another exact factor `G` with

\[
 \mathbb E[c_r(G)\mid F,\tau]
   ={c_r(F)+\tau c_r(F)\over2},
 \qquad
 \operatorname {Cov}(c_r(G))
   ={1\over4}\sum_K\Delta_{K,r}\Delta_{K,r}^{\mathsf T}. \tag{5.2}
\]

Thus the mean is exactly one Johnson-diffusion step and the component vectors
are exactly its integral rounding noise.  The target-wise law is sharper.
On a moved orbit \(\{S,\tau S\}\), if no component contains both targets and
the occurrence families meet \(d\) components, the expected number missing is
exactly \(2^{1-d}\).  A target fixed by \(\tau\) is frozen component by
component.

At every fixed depth from the middle the occurrence budget is only
\(1+O(1/m)\) per target.  A Jensen bound therefore proves that fair switching
can have \(o(W)\) expected misses only if all but \(o(W)\) targets already
occur on **both** sides of one component.  Large one-sided cube dimension is
not enough.  Moreover one transposition fixes asymptotically half of every
central layer.

Every vertical discrepancy has zero point marginals and therefore lies in
Johnson harmonics \(j\ge2\).  Averaging over a uniform coordinate
transposition gives the sharp spectral estimate

\[
 \mathbb E_\tau\left\|{f+\tau f\over2}\right\|_2^2
      \le\left(1-{2\over n}\right)\|f\|_2^2.          \tag{5.3}
\]

Hence a weighted multirank energy contracts by \(\varepsilon_m\) whenever

\[
 \mathbb E_\tau\sum_{q,K}w_q\|\Delta_{K,m-q}\|_2^2
 \le\left({8\over n}-4\varepsilon_m\right)
       \sum_qw_q\|f_{m-q}\|_2^2.                     \tag{5.4}
\]

This component-variance inequality remains useful for an adaptive descent,
but it cannot by itself turn one fair component cube into a low-excess
factor.  For the explicit MSW factor and \(\tau=(2\ 3)\), exact ledgers through
\(m=10\) show an even sharper split: all ranks below \(m-1\) contract (for
\(m\ge5\)), while rank \(m-1\) expands.  The full hierarchy is therefore a
deeper-rank smoother with a one-layer obstruction, not a finished absorber.

The full component law is now proved for every \(m\):

\[
 \#\{\text{components of size }\operatorname{Cat}_j+
       \operatorname{Cat}_{j+1}\}
       =\operatorname{Cat}_{m-j-2}.                    \tag{5.5}
\]

Suffix locality of the MSW recursion reduces the formula to boundary
connectivity.  That boundary theorem is now proved through the published
MNW flippability hypergraph, using exact prefix, suffix, and outer-primitive
context functors rather than the false mirror-wrap homomorphism.  Together
with the explicit colex-leading pivot theorem, this proves that the
**entire** \((2\ 3)\) hierarchy has linearly independent rank-\(m-1\) effects
over every field.  Thus the fixed one-cube absorber is an unconditional
all-dimensional no-go; the productive next target is a recursive multiscale
absorption theorem using many transpositions or successive component cubes.

The hierarchy has the right global scale.  Its total component count is

\[
 \sum_{j=0}^{m-2}\operatorname{Cat}_{m-j-2}
   \sim \frac1{12}\operatorname{Cat}_m,              \tag{5.6}
\]

and for fixed \(j\), the proportion of components of size
\(\operatorname{Cat}_j+\operatorname{Cat}_{j+1}\) tends to
\(3/4^{j+1}\).  Hence three quarters of the legal moves are microscopic
size-two switches, while exponentially rarer components occur at every
Catalan scale.  This is precisely the multiscale supply one would want for
a recursive absorber; what remains is to prove simultaneous vertical-shadow
control, not to discover more finite components.

## 6. The two scalable routes which survive

The global programme is now a genuine dichotomy rather than continued
finite repair.

1. **Adaptive multi-transposition routing.**  If \(Z\) is the set of holes
   and \(D\) the set of duplicate targets at one rank, the best orbit-wise
   floor averaged over transpositions is

   \[
      \mathbb E_\tau\Psi_\tau(c)
        =|Z|-\frac{e_{J(n,r)}(Z,D)}{\binom n2}.        \tag{6.1}
   \]

   The missing theorem must combine Johnson expansion with component
   fragmentation: route many hole--duplicate edges through different
   transpositions and prove that duplicate occurrences split between enough
   components to realize a deterministic descent.

   The first nontrivial legal circuit now exists.  At \(m=4\), two exact
   fourteen-wreath factors differ by a four-for-four trade \(w\) satisfying

   \[
                   B_4w=B_3w=0,\qquad B_2w\ne0.       \tag{6.2}
   \]

   It is created by three preparatory switches in different transposition
   fibres and one final component switch.  Naive order-padding does not lift
   it to \(m=5\).

   The linear part of that suspension problem is now solved.  Insert two new
   coordinates into gaps at cyclic distance \(m\), and sum over all
   \(2m+1\) choices of the first gap; call the operator \(P_m\).  Exact gap
   counting gives

   \[
    B_mw=B_{m-1}w=0
      \Longrightarrow
    B_{m+1}P_mw=B_mP_mw=0,                            \tag{6.3}
   \]

   and the next row is the injective image

   \[
    (B_{m-1}P_mw)_{U\cup\{x\}}
      =(m-1)(B_{m-2}w)_U,                             \tag{6.4}
   \]

   with the identical formula in the \(y\)-sector.  Thus there is no longer
   an algebraic uncertainty about whether a Haar direction can be suspended.
   The remaining obstruction is integral: the translate sum repeats middle
   wreaths, so it must be thinned and completed.

   For one pointed extension per changed wreath, equality of the new top two
   rows has an exact finite-state description: five offset classes on old
   middle occurrences and three on old first-lower occurrences.  The known
   four-for-four edge has no solution even to this coarse criterion from
   \(m=4\) to \(m=5\), including both antipodal orientations.  Therefore the
   all-dimensional theorem must introduce genuinely seam-crossing auxiliary
   Dyck orders that reroute the lifted middle targets and complete the packing;
   extending the common old completion pointwise cannot work.  This is now a
   precise **Catalan absorption/completion theorem**, not a vague request to
   pad the eight finished orders.

2. **Direct two-sided coloured chains.**  The GJM lexical construction gives
   a lower-colour-perfect Johnson forest with only Catalan-scale component
   defect.  Prove Catalan-scale rainbow pruning and an endpoint completion
   that simultaneously restores the upper colours.  This bypasses the MSW
   heat bath and builds the adjacent two shadows exactly before attacking
   deeper shadows by a separate hierarchy.

These are stop/go targets.  If neither a multi-transposition circuit nor a
two-sided endpoint theorem can be proved, the present wreath/SCD programme
does not justify further finite optimization.

## 7. Routes deliberately deprioritized

Several plausible shortcuts have now been disproved rather than merely
failing computationally.

* The GJM middle-four-level lexical forest has a Catalan-sized explicit
  family of duplicate upper colours.  Connecting its existing components
  cannot make it two-sided; Catalan-scale pruning and rewiring are necessary.
* Standard genlex, revolving-door, Chase, and cool-lex Johnson codes have a
  monotone move-to-front depth collapse and cannot expose the required
  \(\Theta(\sqrt m)\) average flag depth.
* A fixed coordinate pairing has the wrong moderate-deviation type law.
  Polynomially many pairings repair the fractional law but leave a genuine
  integral necklace-bundle problem.
* Compressing necklace blocks into native SCD atoms is not an ordinary
  Pippenger matching problem: the native-atom overlap graph is connected.
  The honest reduction retains growing conflict cliques and a weighted
  radius-tail defect.
* Bounded local sums of formal selector squares cannot be support-feasible;
  the new two-for-two moves evade this because they carry correlated effects
  at other ranks.
* The unchanged MSW factor is not a low-excess solution.  Its first lower
  shadow misses `270337/1144066` targets already at `m=11`, and the observed
  miss fraction grows from `0.0476` at `m=4` to `0.2363` at `m=11`.
  Positive-density switching is necessary, not cosmetic.

These exclusions are useful: they reduce the next work to the two
all-dimensional routes in Section 6, rather than a collection of unrelated
finite searches.

## 8. Stop rule after the absorption audit

The pointwise Catalan suspension route is now closed, not merely
unsuccessful.  Three all-dimensional facts are proved in
`CATALAN_SEAM_ABSORPTION_OBSTRUCTION.md`:

1. phase-oblivious extension of one wreath forces its full pointing orbit,
   whose members overlap;
2. a common Dyck prefix or suffix cannot create the linearly growing
   cyclic-order distance required by a lifted packing; and
3. the complete component hierarchy for one fixed transposition has
   linearly independent first-shadow effects, so it has no nontrivial
   first-shadow-neutral selection.

Therefore no further work should be spent on pointwise caps, fixed-context
lifts, or component selection in one unchanged interaction cube.  A viable
Haar proof must be noncommutative: preparatory switches change the factor,
later components are recomputed in that changed state, and middle ownership
is mixed across contexts.  The alternative is to abandon suspension and
prove the direct two-sided coloured-chain/MTF path-cover theorem.

This is also the criterion for future finite experiments: a run is justified
only when it distinguishes these two all-dimensional mechanisms or supplies
a counterexample to a proposed general lemma.  Improving one isolated
`k=14` score is not a research objective.

## 9. The exact lift was stronger than necessary

`CONTRACTIVE_DEFECT_LIFT.md` gives a weaker and quantitatively sufficient
target.  When two coordinates are added, the odd Boolean width grows by

\[
 \frac{W_{m+1}}{W_m}=4-\frac2{m+2}.
\]

Suppose a factor lift propagates each old central-band hole into at most
`a<4` new holes and creates only `O(H Cat_m)` marked seam holes through depth
`H`.  Starting halfway to a desired final dimension and iterating the lift
contracts the normalized inherited defect geometrically.  The accumulated
seam defect is `O(HW_m/m)=o(W_m)` for
`H=sqrt(m omega(m))`, while the truncated two-tail construction is also
`o(W_m)`.  Therefore such a **contractive Catalan lift** already proves

\[
                    \nu(k)=(1+o(1))W(k).
\]

This changes the grid-shuffle audit materially.  It no longer has to preserve
every shadow exactly.  It only has to complete the middle factor, have
propagation norm below four, and leave a bounded number of seam transversals
per old path.  The coordinate-cut construction is now being evaluated
against precisely those three quantities.

There is a further weakening which is closer to the original OR objective.
The raw cut has `Theta(q)` unresolved windows at depth `q`, hence
`Theta(H^2 Cat_m)` unresolved masks through depth `H`.  Those masks are not
independent: they form the interval triangle of one `O(H)` seam halo.  If
that halo is written once per old path, its cost is only `O(H Cat_m)`.
The repair-cost version of the contraction theorem in
`CONTRACTIVE_DEFECT_LIFT.md` therefore asks for a short word covering the
seam defects, not a separate completed factor slot for every missing mask.
With two inherited endpoint sections its contraction coefficient is expected
to be `2`, safely below the width growth factor four.

## 10. Exact punctured-prism braid reduction

`PRISM_SEGMENT_COMPLETION.md` gives a more global accounting of the Catalan
seam.  For every old complementary path

\[
 x_0,y_0,x_1,\ldots,y_{m-1},x_m,
\]

two explicit new complementary paths cover all **lower-middle** vertices
having zero or two of the added coordinates, together with the four tagged
endpoint vertices.  Across the old factor these `2 Cat_m` paths are disjoint
on lower support.

The uncovered support is *exactly* the two tagged internal segments

\[
 (x_1p,\ldots,x_{m-1}p),\qquad
 (x_1q,\ldots,x_{m-1}q).
\]

Its size satisfies the exact Catalan identity

\[
 2(m-1)\operatorname {Cat}_m
 =(m+2)\bigl(\operatorname {Cat}_{m+1}
                   -2\operatorname {Cat}_m\bigr).
\]

At the upper-edge level the provisional decomposition has the exact sector
imbalance

\[
 (+D_m,-2D_m,+D_m),
 \qquad D_m=\operatorname {Cat}_{m+1}-2\operatorname {Cat}_m,
\]

for zero, one, and two new coordinates.  Hence exact completion requires
exactly `D_m` net rhombus transfers replacing one zero-tag and one two-tag
edge by two one-tag edges.  If this braid can be realized with total
`O(Cat_m)` cuts of the displayed old segments, halo compression gives

\[
 R_{m+1,H}\le2R_{m,H}+O(H\operatorname {Cat}_m),
\]

and hence asymptotic optimality.  This is the sharp exact-recursive target.
It replaces both finite-`k` optimization and the false picture of two
independent Cartesian endpoint sectors.

## 11. Primary route: long-run MTF atoms

`GLOBAL_LONG_RUN_MTF_ATOMS.md` now gives an independent reduction with fewer
factor-completion constraints.

For a Johnson path

\[
 S_{t+1}=S_t-p_t+q_t,
\]

two-sided residence of the next and previous `d` departure coordinates has
an explicit move-to-front realization: the update mask is the minimum of
the next radius-`d` symmetric chain.  Long-run Gray cycles in orientation
cubes consequently give length-`Theta(m)` MTF atoms containing pairwise
disjoint symmetric chains through every radius
`d<=Theta(sqrt(m log m))`.

For

\[
 N_q=\binom{2m}{m-q},\qquad
 c_d=N_d-N_{d+1},quad c_h=N_h,
\]

the full coordinate-permutation orbit of one radius-`d` atom, with total
mass `c_d/H`, gives every band vertex weight one.  Thus the MTF dynamics,
the SCD radius ledger, and the interface cost are simultaneously solved at
the fractional level.

The remaining theorem is purely integral:

> round these symmetric atom orbits to a packing whose total central-band
> defect is `o(W)` while exposing the atoms' internal chains.

Ordinary fixed-uniformity Pippenger--Spencer cannot simply be quoted: atom
size grows and adjacent chain members have codegree `Theta(1/m)`.  A staged
nibble/absorption proof must work at the internal-chain level.  This is now
the primary route because it bypasses exact wreath-factor completion.  The
punctured-prism braid remains the strongest exact recursive alternative.

## 12. Reprioritization after the global no-go audits

The long-run atom formulation remains a useful normal form, but it is not a
current proof route by itself.  The exact high-order rectangle codegrees in
`GLOBAL_MTF_ATOM_INTEGRALITY.md` show that no available growing-uniformity
matching theorem rounds the full atoms.  Likewise, contracting the all-zero
Mütze--Weber paths through the reversed Greene--Kleitman matching leaves only

\[
  W_m\frac{3m}{(m+1)(m+2)}=O(W_m/m)
\]

one-step-compatible adjacencies.  Literal repairs therefore cost
`(2-o(1))W_m`.  Finally, the canonical antipodal MSW factor is
`Omega(m Cat_m)` edges away from the Mütze--Weber factor, so it cannot be the
required sparse endpoint refinement.

The finite-case search and these three literal constructions are frozen.  The
two stop/go theorems which remain are:

1. **Endpoint-balanced Catalan braid.**  Antipodalize the Mütze--Weber
   dangling-path factor with an `O(Cat_m)`-support signed T-join whose
   augmented cycles contain exactly one antipodal edge and whose unchanged
   bulk retains two-copy shadow provenance.  Geodesic path length is then
   automatic, and halo compression gives `W+o(W)`.
2. **Targetwise critical ECO charging.**  Prove the Catalan-rate recurrence
   of `CRITICAL_CATALAN_LIFT.md` while charging only genuinely missing child
   masks.  Raw seam deduplication is impossible: the terminal ECO family
   alone has `3 Cat_m` distinct lower depth-one seams, although those seams
   are already covered and should cost zero.

Either theorem implies the all-dimensional asymptotic result

\[
                 \nu(k)=(1+o(1))W(k).
\]

Until one of these gates moves, further optimization of a single `k=14`
path is not mathematically justified.

## 13. Orthogonal chains must be ordered during construction

There is now an exact obstruction to a third apparent shortcut.  Given two
width-sized orthogonal chain partitions, form their bipartite incidence graph
`G`.  The minimum number of empty endpoint slots needed to place all occupied
cells in the physical triangle `left <= right` is exactly the one-sided
bandwidth

\[
 \max\left(0,\min_{\pi,\sigma}\max_{LR\in E(G)}
                   (\pi(L)-\sigma(R))\right).
\]

Bandwidth `d` forces a complete nested flag `X_s` of left-chain sets with

\[
                         |N(X_s)|\le |X_s|+d
                         \quad(0\le s\le W).
\]

Thus any expander-like or independently randomized orthogonal pair needs
`Omega(W)` padding.  For the conjectural exact length, the entire allowed
bandwidth is only `Theta(sqrt(k))`.  A successful orthogonal-chain proof must
therefore construct a recursively nested, almost Hall-tight incidence graph
and its triangular support simultaneously; abstract orthogonality alone is
far from enough.  The forced within-chain precedence orders and pinning are
additional gates.  This strengthens the reason to prioritize the Catalan
braid and genuine MTF path-cover routes, where order is built into the object.

The theorem and proof are in `TRIANGULAR_BANDWIDTH_OBSTRUCTION.md`.

## 14. July 22 all-dimensional audit: one branch closed, one narrowed

The two gates above are no longer on equal footing.

For the unchanged canonical MSW wreath factor, let `L_m` be the number of
missing first lower-shadow masks on `2m+1` coordinates and let
`C_m=Cat_m`.  A critical ECO recurrence

\[
  2L_{m+1}\le {C_{m+1}\over C_m}\,2L_m+B_m
\]

with Cesaro-sub-Catalan error would force

\[
 {L_m\over \binom{2m+1}{m-1}}\longrightarrow0.
\]

This follows by dividing by `C_(m+1)` and telescoping; the normalized defect
is asymptotic to four times `m` times the missing fraction.  Exact data
through `m=12` go in the opposite direction: the missing fraction rises from
`0.0476` to `0.2465`, and the *unavoidable cardinality residual* in the
two-sided recurrence rises from `2.857 C_m` to `4.840 C_m`.  A Hall theorem
cannot repair this mismatch.  Unless that density eventually reverses and
tends to zero, the unchanged-factor ECO branch is closed.  The exact
statement is `MSW_CRITICAL_CARDINALITY_AUDIT.md`.

The Catalan braid branch has improved in a different way.  If `H_0` is the
all-zero Mütze--Weber factor and `H_CF` the canonical complementary MSW
factor, every MSW root path shares exactly three edges with `H_0`.  Hence

\[
 |H_0\cap H_{CF}|=3C_n,
 \qquad |H_0\triangle H_{CF}|=2(2n-3)C_n,
\]

but the symmetric difference has at most `3C_n` connected components and an
alternating Euler decomposition with at most `4C_n` trails/circuits.  Cutting
at the two fixed top-level tag coordinates gives at most `11C_n`
sector-local pieces.  Thus the canonical factors are far in **edge support**
but close in **section complexity**.  The former sparse-edge no-go does not
kill a long-section braid.

There is, however, a sharp remaining obstruction.  A pure cut-and-reconnect
proof would retain all but `O(C_n)` old transitions, whereas the canonical
factor replaces `(2n-3)C_n` of them.  Therefore each long blue section must
carry its own shadow-preserving coordinate projection.  ECO supplies such a
projection only after deleting a path-dependent coordinate pair; fixing the
top-level tag sector does not make that pair global.  The live theorem is:

> Construct a coordinate-consistent projection/transport for the
> Catalan-many long blue sections, or prove that their path-dependent ECO
> deletion cocycle has nontrivial holonomy.

This is now the primary all-dimensional gate.  The fallback global route is
not another finite path search, but a positive-density re-bundling theorem:
replace a macroscopic fraction of the MSW wreaths so that the first-shadow
defect is already `o(W)` before any ECO lift.  Either route attacks the
constant-one theorem directly.

## 15. The blue-section cocycle is explicit; geometry is no longer the gate

The path-dependent deletion maps can in fact be organized without a
super-Catalan proliferation.  In the lift by peak insertion, a gap `g` uses
the fixed deletion chart which removes physical positions `g+1,g+2`; there
are only linearly many chart types.  The three blue path sections per MSW
root fragment into at most six tight-wreath intervals under the step-two
order.  Hence the entire braid has at most `6 Cat_n` blue charted row
intervals, and depth-`H` windows crossing their boundaries cost only
`O(H Cat_n)` occurrences.

The exact target collision between charts is also elementary.  For a binary
target word `u`, deleting adjacent pairs at positions `i<j` gives the same
parent word exactly when `u_i...u_(j+1)` has period two.  Thus distinct
one-tag parents are indexed by maximal alternating blocks, not by individual
transitions.  All but `o(Cat_m)` central targets still have linearly many
such distinct parents, by the run-endpoint count

\[
 2\sum_{s\le\eta m}\binom{2m+O(1)}{2s}
 =2^{(2m+O(1))H_2(\eta)+o(m)},\qquad \eta<1/2.
\]

Therefore the proposed ``nontrivial section holonomy'' fork is resolved:
there is no occurrence-level holonomy obstruction.  The unresolved issue is
strictly targetwise.  Different chart occurrences can collide, actual roots
own only a restricted subset of the charts, and the unchanged canonical
factor already fails the cardinality gate in Section 13.  A useful braid
theorem must consequently end in a re-bundled factor with submacroscopic
first-shadow defect; proving provenance for the unchanged canonical endpoint
factor cannot by itself establish constant one.  Details are in
`MSW_BLUE_SECTION_PROVENANCE.md`.

## 16. A new route: reduce the exponential problem to three-chain boxes

There is now a fourth route which avoids both wreath recursion and a
growing-uniformity matching theorem.  Split the coordinates into three
balanced blocks and SCD each block cube.  Tuples of component chains
partition the Boolean cube into three-dimensional chain boxes.  The sum of
the widths of those boxes is exactly the global width `W(k)`.

If a box of heights `p,q,r` admits a contiguous-union word of length

\[
             \operatorname{width}([0,p]\times[0,q]\times[0,r])
             +O(p+q+r),
\]

then summing those words over all chain boxes gives

\[
             \nu(k)\le W(k)+O(W(k)/\sqrt{k}).
\]

The error calculation is exact: the number of boxes is `Theta(W/k)`, typical
chain heights are `Theta(sqrt(k))`, and the SCD height moments control the
atypical boxes.  More generally, a surface-order error for any fixed
`t>=3` works.

The corresponding two-chain statement is false.  A `p` by `q` chain
rectangle requires exactly `p+q` entries just to realize its two pure axes,
while its balanced width is only about `min(p,q)`.  This recovers the
two-block constant-factor obstruction and explains why dimension three is
the first plausible local geometry.

The remaining conjecture is polynomial-size and independent of `k`: solve
the three-chain interval-join problem with width plus boundary.  A proof by
a lozenge/diagonal traversal, ordered orthogonal chains with a join growth
diagram, or a bounded-boundary recursion would establish constant one in all
dimensions.  The complete reduction is
`FIXED_DIMENSION_GRID_REDUCTION.md`.

## 17. The three-chain route has now been stress-tested

The local problem is exactly a componentwise range-maximum problem: every
entry may be closed to a triple of chain prefixes without destroying any
box witness.  Its rank-slack lower bound is already surface-sharp.  For a
cube of side `d`,

\[
 g_3(d,d,d)\geq \operatorname{width}([0,d]^3)+{2d\over3}+O(1).
\]

The first nontrivial local cube is proof-producing exact:

\[
                         g_3(2,2,2)=10,
\]

whereas its rank-slack bound is nine.

Two useful all-`d` structures were found.  A concentric hexagonal walk of
length `width+O(d)` has every lower point as an interval minimum and every
upper point as an interval maximum.  Separately, two hook-based chain
partitions can be made orthogonal with respectively `width` and
`width+d` chains.

Both obvious completions have also been ruled out.  No fixed-delay middle
row can work, because the three rare extreme increments cannot all use two
row boundaries.  More strongly, every monotone `O(d)` witness band whose
middle order consists of contiguous complete hexagonal rings leaves only
`3d^3/8+O(d^2)` lower-eligible intervals, while the lower half has
`d^3/2+O(d^2)` targets.  The hook rechain clears raw orthogonality but its
endpoint-precedence DAG contains cycles.

Thus the local conjecture is neither solved nor a vague traversal problem.
It now has two exact remaining forms: interleave radii to obtain enough
factorable lower-interval capacity while retaining upper shadows, or build
an **ordered** orthogonal pair with `width+O(d)` chains and a pinning rule.
The audited ledger is in `THREE_BOX_PROGRAM_SYNTHESIS.md`.
