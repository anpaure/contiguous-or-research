# Full-ticket row energy: an exact token identity, a sufficient router condition, and the cap-bottleneck threshold

Date: 2026-07-31  
Status: proved conditional theorem plus an exact non-implication result  
Scope: buffered incidence-C6 / suspended-hex packet menus in the Pascal--Catalan construction

## 0. Verdict

The conditional row bound required by the tunable sparse extraction has a
clean exact form.  If `P_e` is the complete packet menu at anchor/task `e`,
then its typed-token witness row energy is

\[
 {cal R}_e={1\over |P_e|}\sum_r a_e(r)\bigl(A(r)-a_e(r)\bigr),       \tag{0.1}
\]

where `a_e(r)` is the number of options in `P_e` using capacity token `r`
and `A(r)=sum_f a_f(r)`.  Equivalently, it is the menu-average of the sum
of the external loads of all tokens carried by one option.

Consequently the desired

\[
                         {cal R}_e=O(Dm^3)                         \tag{0.2}
\]

follows from one concrete routing condition:

* every complete packet has tokenized nonlocal ticket length `O(D)`; and
* every capacity token is used by at most `O(m^3)` options outside any one
  menu.

This **bounded-dilation / bounded-menu-congestion** condition applies
separately to protected prefix/suffix summaries, common-cap paths, sinks,
and topology slots.  Together with the exact local C6 row

\[
             18m^3+51m^2-4m-5<44m^3,                              \tag{0.3}
\]

it proves (0.2).

The current Catalan host theory does **not** yet supply this condition.  Its
ECO atoms, ports, owner data and local transparency are compatible with two
different occurrence routers: one with private paths, and one in which all
complete tickets traverse a common capacity-one vertex.  A blow-up to `Q`
menus of size `L` has exact row contribution

\[
                              (Q-1)L.                              \tag{0.4}
\]

For `L=Theta(m^2)`, the target (0.2) therefore forces
`Q=O(Dm)`.  Taking `Q/(Dm)->infinity` gives an exact countermodel to deriving
(0.2) from the present local Catalan data.

This is a logical non-implication, not a theorem that the actual Boolean
occurrence router has such a cut vertex.  The actual host remains
undetermined at precisely this point.

## 1. Complete token model

Let `E` be a finite anchor/task set.  Each `e in E` has a nonempty finite
menu `P_e` of complete buffered packets.  A packet `p` carries a finite set
`T(p)` of **typed capacity tokens**.  Tokens of different types are kept
distinct even when they have the same underlying set.  They include, when
applicable,

1. raw lower, upper, incidence and owner-slot resources;
2. protected prefix/suffix or affected-occurrence witnesses;
3. common-cap internal vertices, arcs, sink slots and pinned assignments;
4. physical, root, endpoint and topology slots after the global graphic
   row has been reduced to a pairwise ticket model.

Only resources whose simultaneous use is forbidden are tokens.  A formal
super-source or super-sink of unlimited capacity is not a token.

Assume every pairwise packet incompatibility is witnessed by at least one
shared typed token.  Non-pairwise conditions, such as three individually
compatible connectors forming a cycle, must first be eliminated by a fixed
skeleton, component-private placement, a block-triangular fundamental-path
certificate, or an explicit higher-order selection theorem.  Row energy by
itself does not encode such a condition.

For a token `r`, define

\[
 a_e(r)=|\{p\in P_e:r\in T(p)\}|,
 \qquad A(r)=\sum_{f\in E}a_f(r).                                 \tag{1.1}
\]

For two different menus put

\[
 K_{tok}(e,f)={1\over |P_e|}\sum_r a_e(r)a_f(r).                   \tag{1.2}
\]

This counts shared-token witnesses.  A packet pair sharing several tokens
is counted several times.

### Theorem 1.1 (exact full-ticket row identity)

For every `e`,

\[
\begin{aligned}
 {cal R}_e
   &:=\sum_{f\ne e}K_{tok}(e,f)\\
   &={1\over |P_e|}\sum_r a_e(r)(A(r)-a_e(r))\\
   &={1\over |P_e|}\sum_{p\in P_e}\sum_{r\in T(p)}
                      \bigl(A(r)-a_e(r)\bigr).                    \tag{1.3}
\end{aligned}
\]

If `K_conf(e,f)` denotes the normalized number of genuinely incompatible
packet pairs, then

\[
                         K_{conf}(e,f)\le K_{tok}(e,f),            \tag{1.4}
\]

and hence the true pairwise-conflict row is at most (1.3).

#### Proof

Interchange the finite sums in (1.2):

\[
 \sum_{f\ne e}{1\over |P_e|}\sum_r a_e(r)a_f(r)
 ={1\over |P_e|}\sum_r a_e(r)\sum_{f\ne e}a_f(r).
\]

The inner sum is `A(r)-a_e(r)`, proving the second line of (1.3).  Expanding
`a_e(r)` as the number of packets of `P_e` containing `r` proves the third.
For (1.4), the indicator that a pair is incompatible is at most the number
of shared conflict-witness tokens.  Sum over pairs.  \(\square\)

## 2. The sufficient bounded-congestion routing theorem

Partition the tokens into types `t in J`.  Write

\[
        T_t(p)=T(p)\cap R_t,
        \qquad \lambda_e^\times(r)=A(r)-a_e(r).                   \tag{2.1}
\]

### Theorem 2.1 (typed dilation times menu congestion)

Suppose that for every packet `p in P_e`,

\[
                         |T_t(p)|\le s_t(D),                      \tag{2.2}
\]

and every token of type `t` used by a packet in `P_e` obeys

\[
                         \lambda_e^\times(r)\le M_t(m,D).        \tag{2.3}
\]

Then

\[
                    {cal R}_e\le\sum_{t\in J}s_t(D)M_t(m,D).    \tag{2.4}
\]

In particular, if the local core contributes at most `K_0 m^3`, while

\[
 \sum_{t\ne0}s_t(D)\le cD+c_0,
 \qquad M_t(m,D)\le\kappa_t m^3,                                \tag{2.5}
\]

then, for `D>=1`,

\[
             {cal R}_e\le
       \left(K_0+(cD+c_0)\max_t\kappa_t\right)m^3=O(Dm^3).       \tag{2.6}
\]

#### Proof

Apply the last expression in (1.3), split its inner sum by token type, and
use (2.2)--(2.3) for each packet before averaging over the menu.  Add the
separately audited local-core row.  \(\square\)

The maximum-load form (2.3) is convenient but stronger than necessary.  The
exact weakest row hypothesis is

\[
 {1\over|P_e|}\sum_{p\in P_e}\sum_{r\in T_t(p)}
          \lambda_e^\times(r)\le K_tDm^3.                        \tag{2.7}
\]

Equation (2.7), summed over types, is already (1.3).  The point of
(2.2)--(2.3) is that it separates geometry (dilation) from routing
(congestion) and can be attacked combinatorially.

### Corollary 2.2 (common-cap path tickets)

Suppose a complete cap option is a path with at most `c_cap D+c'_cap`
capacity tokens, counting internal vertices/arcs, the selected sink slot and
every pinned cap assignment.  If each such token occurs in at most
`kappa_cap m^3` candidate tickets outside any fixed menu, then the cap part
of every row is at most

\[
             \kappa_{cap}(c_{cap}D+c'_{cap})m^3=O(Dm^3).         \tag{2.8}
\]

Thus node-private occurrence paths are more than sufficient: their external
cap load is zero.  Uniformly bounded path overlap is also sufficient; full
privacy is not necessary.

### Corollary 2.3 (protected prefix/suffix tickets)

Suppose every affected upper occurrence is either invariant by a proved
trace identity or is represented by one of at most `c_up D+c'_up` typed
prefix/suffix tickets, and every such ticket has external menu load at most
`kappa_up m^3`.  Then the protected-upper contribution is `O(Dm^3)`.

This compression clause is substantive.  A constant-size edit can affect
`Theta(q)` literal crossing windows at width `q`; recording all such
occurrences through `q<=D` can require `Theta(D^2)` tickets.  Without a
transparency/trace compression, Theorem 2.1 gives only `O(D^2m^3)` from the
same per-token congestion bound.  Calling `D` the maximum protected width
does not by itself prove linear ticket dilation.

### Corollary 2.4 (topology tickets)

If packet topology is compiled onto a fixed oriented forest skeleton so
that each option uses `O(D)` private/capacity-one slots and every slot has
external menu load `O(m^3)`, then its row contribution is `O(Dm^3)`.
Without such a compilation, the three-edge triangle obstruction is
higher-order and has no valid pairwise row-energy encoding.

## 3. What the exact C6 role tables already pay

For the raw incidence-C6 catalogue, the exact calculation already frozen in
the repository gives

\[
                  R_{raw}(m)=18m^3+51m^2-4m-5<44m^3.             \tag{3.1}
\]

No new hypothesis is needed for this local row.

There is also a useful scaling change between maximum-degree selection and
average-energy selection.  At one raw anchor, token roles have
multiplicities `m^2,m,1`.  For an assigned anchor family, the exact global
menu load is

\[
                         m^2N_0(r)+mN_1(r)+N_2(r).                \tag{3.2}
\]

For the former `O(m)` maximum-load route, source-fixed tokens had to be
private, one-free tokens could occur at only `O(1)` anchors, and zero-free
tokens at `O(m)` anchors.  For (2.3), the much weaker weighted code

\[
                         m^2N_0+mN_1+N_2=O(m^3)                  \tag{3.3}
\]

suffices.  In isolation this permits the scales

\[
                         N_0=O(m),\quad N_1=O(m^2),
                         \quad N_2=O(m^3).                        \tag{3.4}
\]

The suspended gain-one hex has the same hierarchy.  Its exact table has
fixed roles of multiplicity `2m(m-2)`, one-free roles of order `m`, and
zero-free roles of order one (with the displayed factors `1` or `2`).  Thus
the analogous weighted sum being `O(m^3)` pays its local lower/upper,
owner-slot and semantic cap-pair row.  It still says nothing about a full
alternating common-cap path appended to the local semantic pair.

The allowances in (3.4) do not themselves choose a compatible transversal.
Mandatory source collisions are later removed by the sparse alteration and
Haxell step when the constants in the tunable extraction pass.  They are
only the correct scale for proving the full-atlas average row.

## 4. Exact cap cut-vertex threshold

The two-task cut-vertex example in the current handoff proves failure of a
simultaneous cap linkage, but it is too small to refute (0.2): with quadratic
menus it contributes only `Theta(m^2)`.

The following blow-up gives the exact energy threshold.

### Proposition 4.1 (shared cut-vertex blow-up)

Fix integers `Q>=2` and `L>=1`.  There are `Q` packet menus, each of size
`L`, whose local C6 supports, displayed palettes, prefix/suffix states and
owner data are mutually private, but every complete cap ticket uses one
common capacity-one internal vertex `z`.  For each menu `e`,

\[
                       {cal R}^{cap}_e=(Q-1)L.                   \tag{4.1}
\]

No compatible choice exists for two or more menus.

#### Proof

Give each local option otherwise private typed resources.  In the cap
network, route source `s_e` to its option-specific sink through `z` and no
other source--sink path.  Then

\[
                         a_e(z)=L,\qquad A(z)=QL.
\]

Equation (1.3) gives

\[
 {1\over L}a_e(z)(A(z)-a_e(z))
 ={1\over L}L(Q-1)L=(Q-1)L.
\]

Since `z` has capacity one, Menger's theorem gives cap rank one.  \(\square\)

### Corollary 4.2 (sharp menu-sharing scale)

If `L>=alpha m^2`, a uniform bound

\[
                         {cal R}^{cap}_e\le KDm^3               \tag{4.2}
\]

on the family in Proposition 4.1 requires

\[
                         Q-1\le {K\over\alpha}Dm.                \tag{4.3}
\]

Conversely (4.3) is exactly sufficient for the contribution of this one
token.  Hence a cut token shared by `omega(Dm)` complete quadratic menus
violates the desired row bound.

For any polynomial protected span `D`, the Catalan atlas has enough formal
tasks to take `Q/(Dm)->infinity`.  Appending the common vertex `z` leaves
all local C6/suspended-hex role tables and all prefix/suffix words unchanged.
It therefore gives a dimension-uniform countermodel to any attempted proof
of (0.2) from those local data alone.

## 5. Audit of the current Catalan host

The current results divide cleanly.

### 5.1 What is supplied

* Exact raw C6 local energy (3.1).
* Exact suspended-hex within-menu role multiplicities.
* Physical side forests and private physical port banks on the prepared
  common-basis face.
* Conditional private-router and private-tree-sum theorems: if literal
  node-private occurrence paths are supplied, the cap part of (2.8) follows
  immediately.
* Exact common-cap linkage/Rado formulations for a **selected** family.

### 5.2 What is not supplied

No theorem currently bounds, over the complete option atlas,

1. the length of every full common-cap ticket by `O(D)`;
2. the number of options using any internal cap vertex/arc/sink by
   `O(m^3)`;
3. an `O(D)` prefix/suffix representation of the literal all-width halo;
4. pairwise tokenization of the graphic row without first fixing a topology
   skeleton.

The exact ECO data-separation theorem is decisive about the quantifier.  It
keeps the same atoms, disjoint ports, component edges and owner data while
realizing either dedicated internally disjoint routes or routes through one
shared unit vertex.  Therefore the known Catalan genealogy and local
transparency do not imply bounded menu congestion.

This does **not** exhibit a high-multiplicity cut vertex in the actual
Boolean occurrence router.  It proves that the current description is
insufficient to decide whether one exists.  The honest status is therefore

\[
 \boxed{\text{bounded full-ticket row energy: conditional; actual host:
 unresolved; local-data implication: false.}}                   \tag{5.1}
\]

## 6. Exact sufficient target left for the construction

One of the following would close the row-energy gate.

1. **Private-path atlas.**  Build every complete cap route in a node-private
   annulus, plus an `O(D)` transparent upper summary.
2. **Bounded-congestion path atlas.**  Prove route dilation `O(D)` and
   external option load `O(m^3)` for every typed capacity token.
3. **Direct energy routing.**  Without a pointwise load bound, prove

   \[
     {1\over|P_e|}\sum_{p\in P_e}\sum_{r\in T_{nonlocal}(p)}
              \lambda_e^\times(r)\le KDm^3                       \tag{6.1}
   \]

   for every menu.

Together with quadratic guarded list size, any of these feeds the frozen
tunable extraction: density `Theta(1/(Dm))` gives `Omega(W/D)` compatible
packets.  A prescribed regenerative task bank still needs a spread
task--anchor assignment or freedom to choose tasks after extraction; row
energy alone does not provide it.

## 7. Dependencies and scope

This note uses, without strengthening them:

* `MATH_THEOREM_SPARSE_C6_AVERAGE_LOAD_EXTRACTION_20260731.md`;
* `MATH_THEOREM_R_BUFFERED_C6_WEIGHTED_ANCHOR_AND_TOKEN_LOAD_20260731.md`;
* `MATH_THEOREM_AD_BUFFERED_HEX_GLOBAL_COMPOSITION_HAXELL_AND_BOUNDED_SIDECAR_20260731.md`;
* `MATH_THEOREM_CATALAN_ECO_OCCURRENCE_CONFLICT_PATH_AND_ROUTER_GATE_20260731.md`;
* `MATH_THEOREM_CATALAN_ROUTER_TREE_SUM_AND_PRIVATE_OCCURRENCE_COMPOSITION_20260731.md`; and
* `MATH_THEOREM_K_MINIMAL_COMMON_GUARD_LINKAGE_STATE_AND_EXPLICIT_CONTRACTION_20260731.md`.

It proves an exact conditional implication and an exact countermodel to an
overstrong implication.  It does not claim a full-ticket atlas, an actual
Catalan cut vertex, a prescribed-task absorber, or the all-`k` construction.
