# Phase layers, hereditary `D_4` arms, and the surviving growing-port gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Audit verdict

The newest phase-layer and hereditary-boundary theorems do not yet imply
MWB or coefficient one.  They do establish three exact facts.

1. There are genuine integral parent-active path-factor switches.  The
   two-row/two-cut Chung--Feller rectangle preserves every `X` owner,
   preserves all `Y` owners in aggregate, fixes both row endpoints, and
   changes one first-edge flag.  The noncanonical fourteen-row `D_4`
   factor is likewise a legal port-preserving replacement in every common
   aligned one-hole context.
2. A boundary-straddling `D_4` block has a complete, literal, simultaneous
   multidepth action.  Its sixteen prefix/suffix profile columns form
   one-deletion chains through all protected depths.  There is no formal
   cancellation between different depths.
3. Neither fact supplies the required quantitative drain.  The phase
   rectangles move at most a `1/8+o(1)` fraction of the first canonical
   layer.  A fixed root-aligned `D_4` chart reaches only
   `7/128+o(1)` of the ports per boundary.  Strict-interior `D_4` packets
   can cover almost every root but are exactly invisible to the parent
   endpoint target.  On the boundary, the marked six-unit `D_4` profile
   comes with eighty-two units of companion positive-mass budget per
   depth, and no theorem controls their physical backgrounds.

The growing Catalan-skeleton hypergraph does not amplify the bounded seed
through the proved context functor.  Its average degree is exponentially
large in the skeleton size, but its exceptional codegrees are large, and
the union of all edges satisfying the literal common-port test is
`o(C_s)`.

The strongest surviving exact construction interface is therefore the
direct growing-`D_s` completion theorem: prescribed first columns extend
to a port path factor exactly when two residual Hall conditions and one
marked-monodromy condition hold.  The shortest viable new theorem is a
balanced marked-monodromy completion with full boundary profiles.  It must
be proved directly on the size-`s` inclusion graph; it cannot be obtained
from coordinate components, a bounded `D_4/H_4` library, strict fringe
substitutions, or the shape-respecting skeleton hypergraph.

## 1. Exact phase-layer result and its quantitative ceiling

Let `D_s` be the Catalan family of Dyck roots.  A phase-respecting exact
path factor can be indexed by permutations `p_t` of `D_s`.  If

\[
                        X'_t(u)=X_t(p_tu),
\]

then exactness is equivalent to:

\[
 X'_t(u)\sim_JX'_{t+1}(u),\qquad p_s=p_0,
\tag{1.1}
\]

and

\[
 \biguplus_{t,u}\{X'_t(u)\cup X'_{t+1}(u)\}
                   =\binom{[2s]}{s+1}.
\tag{1.2}
\]

Condition (1.2) is aggregate across cuts.  Requiring it separately at
each cut is stronger and would incorrectly exclude the basic rectangle.

For two rows and two adjacent cuts, every nontrivial legal switch has the
octahedral form

\[
\begin{array}{c|ccc}
 &X_t&X_{t+1}&X_{t+2}\\ \hline
P&Kxy&Kxw&Kzw\\
Q&Kxz&Kyz&Kyw
\end{array}
\quad\longmapsto\quad
\begin{array}{c|ccc}
P&Kxy&Kyz&Kzw\\
Q&Kxz&Kxw&Kyw.
\end{array}
\tag{1.3}
\]

The four `Y` colours on either shore are exactly

\[
                         Kxyz,Kxyw,Kxzw,Kyzw.
\tag{1.4}
\]

At the first two cuts of the canonical Chung--Feller factor, recursion
forces the root pair

\[
                         1100R\longleftrightarrow1010R,
             \qquad R\in D_{s-2}.
\tag{1.5}
\]

These pairs are disjoint, so all first-two-cut rectangles generate the
cube `(C_2)^(C_(s-2))`.  The active root proportion is exactly

\[
 {2C_{s-2}\over C_s}
 ={s(s+1)\over2(2s-1)(2s-3)}
 \longrightarrow {1\over8}.
\tag{1.6}
\]

Thus the phase switch is a valid nonrigidity theorem and a literal
one-row fibre split.  It is not a dense first-layer router.

### Audit of the octahedral classification

The only compressed step in the written proof is the exclusion of
adjacent middle states.  It is sound.  Write

\[
 A=Kab,\quad C=Kcd,\quad B=Kac,\quad E=Kad.
\]

The first row then loses `Kabc` and gains `Kabd`.  A common Johnson
neighbour `Z` of `B,E` either has the form `Kaz`, in which case its
signed colour difference is

\[
                         Kad z-Kac z,
\]

or has identical unions with `B,E`, in which case its difference is zero.
Producing `Kabd-Kabc` forces `z=b`, hence `Z=A`, which repeats an already
owned `X` state.  Therefore `B,E` must be opposite in the common-neighbour
square.  Their other opposite pair is then forced, giving (1.3).

## 2. Exact hereditary `D_4` carrier theorem

For a row `P` of the canonical factor `F` or the noncanonical factor `G`,
write its port-linearized coordinate word as

\[
 \widehat q_H(P)=(b_1,b_2,b_3,b_4,9,a_1,a_2,a_3,a_4),
                         \qquad H\in\{F,G\}.
\tag{2.1}
\]

This is a cut of the literal local wreath: its first four entries are the
exit port, its last four entries are the entrance port, and coordinate
`9` separates them.

Embed (2.1) contiguously in a parent cyclic word and suppose the protected
target interval has length `L_q` with

\[
                         9\le L_q\le |R|,
\tag{2.2}
\]

where `R` is the exterior arc.  Every changed interval then meets the
local block in one nonempty proper prefix or suffix.  With row-common
carrier sets, the exact signed depth-`q` histogram is

\[
 \boxed{
 D_q=\sum_{\ell=1}^{8}\left(
 K^-_{q,\ell}\star\Delta_{\ell,4}
 +K^+_{q,\ell}\star\Delta_{\ell,4-\ell}
 \right).}
\tag{2.3}
\]

Moreover

\[
 K^\pm_{q+1,\ell}
       =K^\pm_{q,\ell}\setminus\{z^\pm_{q,\ell}\}.
\tag{2.4}
\]

Thus all sixteen columns in (2.3) are coherent one-deletion chains
through the serviced depths.  Since different depths have different
target ranks, there is no cross-depth histogram cancellation.

The common-carrier hypothesis is essential.  In the actual row-dependent
case the authoritative formula is

\[
 D_q=\sum_{P\in D_4}\sum_{\ell=1}^{8}
 \left(
   \Phi^-_{q,P,\ell}d_{P,\ell,4}
  +\Phi^+_{q,P,\ell}d_{P,\ell,4-\ell}
 \right).
\tag{2.5}
\]

One may sum local profiles before applying carriers only after proving
that the maps `Phi` agree on the relevant rows.

Exact ownership is not a gap here.  Both local factors have the same
rowwise complementary endpoints and the same complete `X` and `Y`
ledgers.  Hence the anchored port-context substitution theorem proves
that one aligned replacement is an integral exact factor.  Disjoint open
replacement slabs may be chosen independently.  Overlapping or nested
parent slabs still require a joint ledger.

## 3. What the hereditary theorem does and does not move

The marked left singleton profile is

\[
 \Delta_{1,4}=-4e_2+4e_3-e_4-e_6+2e_7,
\qquad m(\Delta_{1,4})=6.
\tag{3.1}
\]

For example, individual rows contain the coherent arms

\[
                P=1345:2\longrightarrow6,
 \qquad         P=1256:4\longrightarrow7.
\tag{3.2}
\]

The same integral factor choice orients these moves at every protected
depth.  This is genuine simultaneous-depth movement.

It does not act on the original hereditary source when the whole local
block is strictly inside the matched ancestor window.  That window
contains both complementary port states `P` and `[8]\P`; hence its local
intersection is

\[
                         P\cap([8]\setminus P)=\varnothing.
\tag{3.3}
\]

The carrier is then the rowwise collapse

\[
                         e_S\longmapsto e_{O_q},
\tag{3.4}
\]

on both factor shores.  Consequently

\[
                         D_q^{\rm source}=0
\tag{3.5}
\]

for every depth and every background.  This is the exact early-label
erasure obstruction.

For a boundary-straddling placement, the full companion budget is large.
The positive masses of the paired prefix/suffix profiles are

\[
\begin{array}{c|rrrrrrrr}
\ell&1&2&3&4&5&6&7&8\\ \hline
m(\Delta_{\ell,4})&6&7&8&0&0&7&9&7\\
m(\Delta_{\ell,4-\ell})&7&9&7&0&0&8&7&6.
\end{array}
\tag{3.6}
\]

Therefore

\[
 \boxed{
 \sum_{\ell=1}^{8}
 [m(\Delta_{\ell,4})+m(\Delta_{\ell,4-\ell})]=88.}
\tag{3.7}
\]

Only six units belong to the marked profile (3.1); the remaining
triangle-inequality budget is eighty-two per depth.  Complementary
profiles have the same coefficient sign after complementation and sit on
different exterior carriers, so complementation does not cancel them.

For a physical load `mu_q` and signed full profile `D_q`, the exact new
minus old cap derivative is

\[
 \sum_T\big[(\mu_q(T)+D_q(T)-p)_+-(\mu_q(T)-p)_+\big].
\tag{3.8}
\]

No sign follows from (3.7).  The length-two aggregate has a negative
scalar-background hinge only in the explicitly audited residual-capacity
range

\[
                  {21\over10}+\eta\le c_q\le5-\eta,
\tag{3.9}
\]

and this result assumes an injective common carrier.  It has not been
correlated with the physical Catalan source cells.  The length-three old
and new multiplicity multisets agree under a scalar background, so that
sector is exactly neutral there.

Hence the hereditary theorem proves `Theta(number of depths)` raw
movement, not `Omega(number of depths)` PCap descent.

## 4. Quantitative bounded-seed no-go ledger

Every proposed amplification of the fixed seed must pass the following
audited obstructions.

1. **First-two-cut phase rectangles.**  Their active support is only
   (1.6).
2. **Root-aligned `D_4`.**  A one-boundary chart covers

   \[
                         14C_{s-4}
        =\left({7\over128}+o(1)\right)C_s
   \tag{4.1}
   \]

   ports.  Two opposite charts cover at most `7/64+o(1)` before overlap
   and compatibility losses.
3. **Terminal collective `D_4` routing.**  The strongest proved
   two-spectator product interface has incidence at most

   \[
                         14C_{s-3}
        =\left({7\over32}+o(1)\right)C_s.
   \tag{4.2}
   \]
4. **Strict fringe packets.**  They can cover all but `o(C_s)` roots and
   can be chosen independently, but every packet fixes both local ports.
   The full matched parent target therefore stays fixed occurrence by
   occurrence.  Dense coverage lies in the endpoint-profile kernel.
5. **Coordinate components.**  The two endpoint coordinate swaps have one
   `V_4` component containing the four root populations

   \[
                         (C_s,C_{s-1},C_{s-1},C_{s-2}).
   \tag{4.3}
   \]

   A shore choice only permutes these cells, leaving a cell of load at
   least `C_s`.  The direct `F_4/G_4` ownership overlay is also connected,
   so it has no proper component subtrade.
6. **Bounded multistate orbit.**  In the full sixteen-state `D_4/H_4`
   library, roots `1234` and `1235` always insert coordinate `8` first.
   Choices are factor-coupled, not a product of rowwise menus.  At the
   canonical early-parent background the best statewise hinge relief of
   the eight forward states is exactly zero.
7. **Cell capacity.**  The complete two-endpoint preload is

   \[
   M_s=C_s+2C_{s-1}+C_{s-2}=\rho_sC_s,
   \qquad
   \rho_s={5s(5s-7)\over4(2s-1)(2s-3)}\to{25\over16}.
   \tag{4.4}
   \]

   Four zero-background cells are possible only when

   \[
                         {C_s\over p}\le{4\over\rho_s}
                         \longrightarrow {64\over25}.
   \tag{4.5}
   \]

   Above that threshold a surviving library must expose five, six, or
   seven physical cells according to
   `ceil(rho_s C_s/p)`.  Actual background only lowers these capacities.

These statements jointly close every known route which tries to obtain a
dense parent router by iterating a bounded seed.

## 5. Growing skeletons: abundant roots, no proved factor packets

Let `T_s` be the `C_s` ordered full binary trees of size `s`.  For a fixed
ordered forest `(U_0,...,U_t)` of total size `s-t`, let

\[
 E_{\mathbf U}
   =\{S[U_0,\ldots,U_t]:S\in\mathcal T_t\}.
\tag{5.1}
\]

The exact edge and incidence counts are

\[
 |E_{\mathbf U}|=C_t,
\tag{5.2}
\]

\[
 |\mathcal E_{s,t}|
 ={t+1\over2s-t+1}\binom{2s-t+1}{s-t},
\tag{5.3}
\]

and

\[
 \bar d_{s,t}
 =\binom{2t}{t}{(s)_t\over(2s)_t}
 =(1+o(1)){2^t\over\sqrt{\pi t}}
\tag{5.4}
\]

for `t=o(sqrt(s))`, `t -> infinity`.

This is not a matching theorem.  There are at least

\[
                         2^tC_{s-t}
\tag{5.5}

degree-one vertices.  More decisively, when `2^t=o(s)` there are vertex
pairs of codegree `C_(t-2)`, and

\[
 {C_{t-2}\over\bar d_{s,t}}
 =(1+o(1)){2^{t-4}\over t}\longrightarrow\infty.
\tag{5.6}

Thus a maximum-codegree nibble cannot be invoked.

There is an earlier factor obstruction.  The shape-preserving common-port
interface would require

\[
 \operatorname{port}(S(\mathbf U))
   =W\mathbin{\dot\cup}\iota(\operatorname{port}(S))
                    \qquad(S\in\mathcal T_t).
\tag{5.7}

For `t>=3`, (5.7) forces `U_0` to be a mountain and

\[
                         U_1=\cdots=U_{t-2}=\varnothing.
\tag{5.8}

The number of forest tuples even passing this necessary port test is at
most

\[
 B_{s-t}=[z^{s-t}]{C(z)^2\over1-z}
                         =\sum_{j=0}^{s-t}C_{j+1}.
\tag{5.9}

Consequently, even if all candidate edges were disjoint, their union has
size at most

\[
 C_tB_{s-t}
 \le\left({16\over3\sqrt\pi}+o(1)\right){C_s\over t^{3/2}}
 =o(C_s).
\tag{5.10}

A root-hypergraph matching therefore would not provide a physical `X/Y`
factor packet.  Escaping (5.10) requires row-dependent global paths and a
new complete ownership proof; that is already a direct growing-`D_s`
construction.

## 6. Strongest surviving exact interface: Hall plus marked monodromy

Put

\[
 \mathcal X=\binom{[2s]}s,
 \quad\mathcal Y=\binom{[2s]}{s+1},
 \quad U=\mathcal X\setminus\overline D_s,
 \quad V=\mathcal X\setminus D_s.
\tag{6.1}
\]

Prescribe distinct first columns

\[
                         P\subset Y_P\supset Q_P,
                 \qquad P\in D_s,\quad Q_P\in V,
\tag{6.2}
\]

and write `Y_0={Y_P}`, `Q_0={Q_P}`.  The prescribed columns extend to
the two ownership matchings exactly when

\[
 |N(A)\setminus\mathcal Y_0|\ge|A|
                   \qquad(A\subseteq U\setminus D_s),
\tag{6.3}
\]

and

\[
 |N(B)\setminus\mathcal Q_0|\ge|B|
                   \qquad(B\subseteq\mathcal Y\setminus\mathcal Y_0).
\tag{6.4}
\]

For any two such perfect matchings, compose the upward and downward maps
and adjoin the marked closure arrows

\[
                         \overline P\longrightarrow P.
\tag{6.5}

The matchings form a `D_s`-port complement-path factor if and only if
every cycle of the resulting permutation of `\mathcal X` contains exactly
one arrow (6.5).  Hall alone does not imply this marked-monodromy
condition.

This criterion is exact.  Once every cycle has one marked arrow, deleting
the arrows produces `C_s` paths.  Their total number of successor arcs is
`sC_s`, while every path from `P` to its complement has Johnson distance
at least `s`.  Hence every path is automatically a length-`s` complement
geodesic, and the two matchings give the complete `X/Y` ownership ledgers.

There is one universal obstruction which every construction must reserve.
If `a(P)` is the step at which coordinate `1` is deleted and `b(P)` the
step at which coordinate `2s` is inserted, then every exact `D_s`-port
factor has exactly

\[
                         C_{s-1}
\tag{6.6}

rows with

\[
                         b(P)=1,\qquad a(P)=s.
\tag{6.7}

Indeed exact `X` ownership gives total joint containment
`(s-1)C_(s-1)`, exact `Y` ownership says exactly `C_(s-1)` rows have
`b(P)<=a(P)`, and every such row contributes at most `s-1`.  Equality
forces (6.7) in every counted row.

Consequently, if `C_s>=4p`, then

\[
 C_{s-1}={s+1\over2(2s-1)}C_s>p,
\tag{6.8}
\]

so no exact factor can put every global first-insertion coordinate below
cap.  This does not rule out distributing the forced rows among the
canonical first-return fibres; the exact factor need not take them from
one fibre.

## 7. The single live construction lemma

The following is the narrowest surviving local theorem that would make
new progress.  It is unproved.

### Balanced marked-monodromy boundary completion `BMMC_s` — UNPROVED

Let `\mathfrak p` be the physical cell cap and take the first Catalan
scale

\[
                         C_{s-1}<\mathfrak p\le C_s.
\tag{7.0}
\]

Thus the forced population `C_(s-1)` itself fits below the cap; the
stronger obstruction (6.8) is not being ignored.  For this slowly growing
`s`, prescribe for every `P in D_s` a first column

\[
 P\subset P\cup\{b_1(P)\}\supset
             P-\{a_1(P)\}+\{b_1(P)\}.
\tag{7.1}
\]

The prescription must satisfy all of the following.

1. The `Y_P` and `Q_P` in (7.1) are distinct, and the two residual Hall
   inequalities (6.3)--(6.4) hold with quantitative slack.
2. There are residual ownership matchings for which the closed successor
   permutation has exactly one marked arrow per cycle.
3. The forced endpoint population (6.6)--(6.7) is reserved exactly; no
   global quota contradicting (6.8) is imposed.  Instead, in every
   canonical first-return fibre, both first-insertion and first-deletion
   target multiplicities obey the required local cap.  Whenever the full
   two-boundary preload (4.4) is served in one physical carrier family,
   the prescription exposes at least

   \[
              \left\lceil {M_s\over\mathfrak p}\right\rceil
              =\left\lceil\rho_s{C_s\over\mathfrak p}\right\rceil
   \tag{7.2}
   \]

   genuinely distinct cells; an abstract label split which later
   identifies these cells is not admissible.
4. The resulting family of completions contains enough independently
   selectable states that, after a literal parent-boundary embedding, its
   complete row-resolved prefix/suffix profiles—not only (7.1)—satisfy the
   carrier/background weighted cap inequalities at every serviced depth.

Items 1--2 alone produce one integral exact `D_s`-port factor.  Item 3
provides the parent-active child-shadow split without violating the forced
endpoint invariant.  Item 4 is indispensable for PCap: the `D_4` audit
shows that a favourable first edge can be outweighed by its collar.

This lemma survives all known no-go theorems:

* it is not a coordinate-component shore choice;
* it is not confined to the connected `F_4/G_4` overlay;
* it acts at the parent boundary, so strict-interior erasure does not
  apply;
* its support grows with `s`, so the `7/128` and `7/32` bounded-seed
  ceilings do not apply;
* it constructs one factor directly on a fixed coordinate ground, so the
  operadic common-port obstruction (5.10) does not apply;
* it uses no small-codegree root-hypergraph nibble;
* it explicitly reserves the `C_(s-1)` forced endpoint rows; and
* it demands the full physical collar/background ledger, so it does not
  infer cap descent from a local first-insertion histogram.

## 8. Shortest viable route and exact boundary

The shortest credible proof route is now:

1. Prove `BMMC_s` directly in the middle-levels inclusion graph.  First
   choose the prescribed columns with per-fibre quotas and the exact
   endpoint reserve.  Prove robust residual Hall.  Then use alternating
   cycles in the two residual matchings to merge or split successor cycles
   until every cycle contains one marked arrow, while preserving the
   prescribed columns.
2. Audit all prefix/suffix flags of those completions under the actual
   parent carriers.  Establish a full weighted hinge or direct-hole bound
   for one common choice across depths; scalar-background or marked-row
   estimates do not suffice.
3. Install only product-compatible parent-aligned atoms, preserving the
   port endpoints and both ownership ledgers.  Nested or overlapping
   atoms must be grouped into one joint atom whenever one serviced window
   meets both.
4. Only after that local/global carrier theorem may one invoke the exact
   middle factor, common multidepth row choice, and the literal central
   interval plus SCD-tail ledger.

Current theorems complete none of Steps 1--2.  Therefore they do not prove
MWB or coefficient one.  The exact positive boundary is:

\[
 \boxed{
 \begin{array}{c}
 \text{integral port legality: proved;}\\
 \text{local parent-active nonrigidity: proved;}\\
 \text{raw simultaneous-depth boundary action: proved;}\\
 \text{dense growing completion with physical cap sign: open.}
 \end{array}}
\]

## 9. Sources audited

* `MATH_ATTACK_LANE_F_MSW_CHUNG_FELLER_LAYERED_PHASE_SWITCH_20260726.md`;
* `MATH_THEOREM_ALL_FIRST_TWO_CUT_RECTANGLES_20260726.md`;
* `MATH_THEOREM_D4_HEREDITARY_BOUNDARY_ARM_20260726.md`;
* `MATH_AUDIT_D4_HEREDITARY_ANCESTOR_CHAIN_20260726.md`;
* `MATH_THEOREM_D4_HEREDITARY_ARM_AND_CHAINWISE_COLLAR_20260726.md`;
* `MATH_THEOREM_W_GROWING_OPERADIC_SKELETON_HYPERGRAPH_20260726.md`;
* `MATH_AUDIT_GROWING_CATALAN_SKELETON_HYPERGRAPH_AND_PORT_OBSTRUCTION_20260726.md`;
* `MATH_ATTACK_N_D4_FIVE_INPUT_OPERAD_CROSS_AUDIT_AND_GROWING_GATE_20260726.md`;
* the cited `D_4/H_4`, `V_4`, strict-fringe, and cell-capacity audits.
