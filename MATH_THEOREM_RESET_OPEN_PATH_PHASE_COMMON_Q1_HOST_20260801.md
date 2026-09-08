# The complete-reversal reset has one phase-common q1 host

**Date:** 2026-08-01  
**Lane:** K, protected complete-reversal host  
**Status:** unconditional q1 planting theorem, with an economical open-path
mode and a fully guarded isolated-cycle mode.  The open mode gives one
phase-common undirected residual completion but does not preserve exterior
residence or arbitrary-width upper witnesses.  Bounded components,
upper-surjective decoration and the common compiler remain open.

## 0. Outcome

Let `Z+` and `Z-` be the two complete-reversal phases of
`MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`.
They form opposite orientations of one simple Johnson cycle on

\[
                         M=4d+2                              \tag{0.1}
\]

rank-`m` roots.

Work in the middle-levels incidence graph

\[
 ML_m=\left({[2m-1]\choose m-1},{[2m-1]\choose m};\subset\right).
\tag{0.2}
\]

Two unconditional host statements follow from the small protected-factor
theorem.

### Open path

Open one common Johnson edge of `Z`.  Its incidence lift has

\[
 \boxed{
   4d+2\ \hbox{root vertices},\quad
   4d+1\ \hbox{lower vertices},\quad
   8d+2\ \hbox{incidence edges}.}                            \tag{0.3}
\]

If

\[
                         \boxed{m\ge8d+4},                  \tag{0.4}
\]

this path is contained in a spanning two-factor of `ML_m`.  Since the two
phases give the identical undirected path, the same residual two-factor
completion works for both.

### Closed component

If instead the omitted incidence diamond is also protected, the full
packet cycle has `8d+4` incidence edges.  Hence

\[
                         \boxed{m\ge8d+6}                   \tag{0.5}
\]

plants the entire closed packet as an isolated component of a spanning
two-factor.  This mode retains the packet's complete residence,
every-width cyclic OR deck, and reversed antecedent literally.  Its price
is that global topology still contains the isolated packet component.

Both thresholds hold eventually because `d=Theta(sqrt(m))`.

## 1. The common open incidence path

Write the common undirected root cycle as

\[
 Z_0Z_1\cdots Z_{M-1}Z_0.                                  \tag{1.1}
\]

Put

\[
 I_i=Z_i\cap Z_{i+1},\qquad
 U_i=Z_i\cup Z_{i+1}.                                      \tag{1.2}
\]

All `I_i` and all `U_i` are distinct.  Open the common edge
`Z_(M-1)Z_0`.  The incidence lift of the remaining owner path is

\[
 P=Z_0-I_0-Z_1-I_1-\cdots-I_{M-2}-Z_{M-1}.                 \tag{1.3}
\]

It has `M` root vertices, `M-1` lower vertices and `2(M-1)` incidence
edges, proving (0.3).  It is a simple alternating path, so

\[
                         \Delta(P)=2.                       \tag{1.4}
\]

The reverse phase traverses (1.3) in the opposite order; as an undirected
incidence subgraph it is literally the same `P`.  Its protected adjacent
upper colours are the same `M-1` sets

\[
                         U_0,\ldots,U_{M-2}.                 \tag{1.5}
\]

## 2. Phase-common q1 completion

The small protected-factor theorem states that every subgraph `P` of
`ML_m` with

\[
                         \Delta(P)\le2,qquad |E(P)|\le m-2 \tag{2.1}
\]

extends to a spanning two-factor.

### Theorem 2.1 (economical open-path host)

If `m>=8d+4`, there is a spanning two-factor `F` of `ML_m` containing the
common path (1.3).  The undirected residual edge set

\[
                         F-E(P)                              \tag{2.2}
\]

is one phase-common q1 completion.  Both phases consume exactly the same
root vertices, lower colours and adjacent-upper colours in (1.3)--(1.5).

#### Proof

Equations (0.3)--(1.4) give

\[
                         |E(P)|=8d+2\le m-2.
\]

Apply the small protected-factor theorem once.  The two phases do not ask
for the union of two protected paths: they ask for opposite orientations
of the **same** undirected path.  Therefore the one resulting `F` and the
one residual set (2.2) support either phase. \(\square\)

The threshold is exact for this application of the theorem:

\[
                         2(4d+1)\le m-2
 \quad\Longleftrightarrow\quad m\ge8d+4.                    \tag{2.3}
\]

It is not asserted to be a necessary threshold for some other extension
argument.

## 3. Orientation and deferred switching

Let `C` be the factor component of `F` containing `P`.  The complement
`C-E(P)` is a residual path joining the two endpoints of `P`.

Orienting `C` one way traverses `P` as `Z+`; orienting the whole component
the other way traverses it as `Z-`.  Thus `F` supports either packet phase.
However, the residual path orientation reverses at the same time.

This yields two distinct use modes.

1. **One terminal phase.**  If the construction only needs a chosen final
   phase, orient `C` accordingly.  Theorem 2.1 is a complete unconditional
   q1 host theorem for that use.
2. **Deferred phase switching.**  One may postpone the phase choice and
   later reverse the entire component `C`.  Complete reversal preserves
   whatever cyclic interval-OR spectrum and coordinate-run inventory `C`
   already has.  But the present theorem does not prove that the arbitrary
   residual completion initially has the required upper coverage,
   residence or compiler.

What is **not** proved is a local phase switch which reverses `P` while
holding a directed exterior path fixed.  That would require a compatible
three-return exterior or a phase-symmetric boundary state.

## 4. Fully guarded isolated-cycle mode

Let

\[
 \widehat P=P\cup\{I_{M-1}Z_{M-1},I_{M-1}Z_0\}.             \tag{4.1}
\]

This is the complete incidence cycle of the reset-return packet.  It has

\[
                         |E(\widehat P)|=2M=8d+4,
 \qquad                  \Delta(\widehat P)=2.              \tag{4.2}
\]

### Theorem 4.1 (closed protected component)

If `m>=8d+6`, there is a spanning two-factor of `ML_m` containing
`widehat P`.  In every such factor, `widehat P` is an isolated component.
Both packet phases are obtained by orienting that component in the two
directions, while the residual factor is held literally fixed.

#### Proof

Condition (0.5) is exactly

\[
                         8d+4\le m-2.
\]

The protected-factor theorem supplies the spanning two-factor.  Every
vertex of `widehat P` already has protected degree two, so no completion
edge can meet it; it remains a whole component.  Reversal changes no
undirected incidence, lower or upper-q1 resource. \(\square\)

Unlike the economical open mode, this preserves all local guards proved
for the closed packet:

* every positive run is at least `d+1`;
* every cyclic root interval union is preserved;
* the nonempty maximal antecedent reverses;
* every derivative-row inventory and internal compiler incidence agrees.

The cost is topological rather than scalar: a later construction still has
to merge or open this component without losing those guards.

## 5. The protected path is already Catalan-compatible

The q1 factor from Theorem 2.1 has an alternating decomposition into two
perfect matchings.  Along the protected path, colour the incidences as

\[
 P_0=\{I_iZ_i:0\le i<M-1\},
 \qquad
 P_1=\{I_iZ_{i+1}:0\le i<M-1\}.                            \tag{5.1}
\]

Choose the factor's two-colouring so that

\[
                         P_0\subseteq M_0,
 \qquad                  P_1\subseteq M_1.                  \tag{5.2}
\]

For an incidence `e=IR` outside `M_0`, recall

\[
 \operatorname{up}_{M_0}(e)=M_0(I)\cup R,
 \qquad
 \lambda_{M_0}(e)=\{I,M_0^{-1}(R)\}.                      \tag{5.3}
\]

### Theorem 5.1 (protected upper-rainbow link path)

`P_1` carries the `M-1=4d+1` distinct protected upper colours

\[
                         U_i=Z_i\cup Z_{i+1},               \tag{5.4}
\]

and its labelled links are graphic-independent.  More precisely, if

\[
                         J=M_0^{-1}(Z_{M-1}),               \tag{5.5}
\]

then

\[
 \lambda(P_1)=
   I_0-I_1-\cdots-I_{M-2}-J.                               \tag{5.6}
\]

The vertex `J` lies outside the protected lower bank.

#### Proof

For `e_i=I_iZ_(i+1)`, equation (5.2) gives `M_0(I_i)=Z_i`, so

\[
                         \operatorname{up}(e_i)
                           =Z_i\cup Z_{i+1}=U_i.
\]

These colours are distinct by packet q1 simplicity.  For `i<M-2`, the
protected edge `I_(i+1)Z_(i+1)` lies in `M_0`, hence

\[
                         M_0^{-1}(Z_{i+1})=I_{i+1}.
\]

At the last root the preimage is `J`.  Every protected lower vertex is
already matched by `P_0`, so `J` is outside that bank.  Thus (5.6) is a
simple path and is graphic-independent. \(\square\)

This is the strongest unconditional upper-decorated conclusion available
from the q1 host: the packet itself is a valid rooted-Catalan **seed**.  It
has no local repeated-upper or graphic-cycle obstruction, and the same seed
works for both directed phases because orientation does not change the
undirected incidence colouring.

What remains is to extend this `4d+1`-edge seed to one matching carrying all
remaining upper colours while retaining graphic independence and residual
Hall.  That is still a Catalan-scale correlated selector.

## 6. The upper-decorated and component gates remain real

Theorem 2.1 completes incidence degrees only.  At a lower vertex `I`, the
two selected root neighbours determine the paired upper colour given by
their union.  Ore--Ryser completion has no constraint forcing all
rank-`m+1` colours to occur.  The existing `ML_4` counterexample is a
spanning two-factor missing one such colour.

Likewise, the protected-factor theorem gives only the bulk bound

\[
                         c(F)\le\lfloor W/3\rfloor,
 \qquad W={2m-1\choose m}.                                  \tag{6.1}
\]

The long path improves only the size of its own component; it does not
make the number of other components bounded.  Even the closed mode adds an
explicit isolated component.

The exact next selector is the rooted upper-decorated near-factor
certificate from
`MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`:
choose a near-perfect second matching whose paired upper colours are
surjective and whose contracted links have graphic rank `W-O(1)`, then
complete the bounded residue by Hall.  Because `P` is phase-common as an
undirected bank, any such certificate needs to be found only once.  Its
existence with the packet protected is not proved here.

## 7. Exact scope

The unconditional gain is:

\[
 \boxed{
 \text{one }(4d+2)\text{-root complete-reversal packet}
 \Longrightarrow
 \text{one phase-common spanning q1 two-factor}
 }
\]

under (0.4), or one fully guarded isolated packet component under (0.5).

Still open are:

* `O(1)` factor components;
* surjectivity of all paired upper colours;
* residence on the arbitrary open-mode residual path;
* arbitrary-width upper witnesses crossing the packet/residual boundary;
* one occurrence-labelled global compiler/common cap;
* a safe opening/merge and Pascal regeneration;
* any `k=17`, all-`k`, or `B+O(1)` conclusion.

## 8. Independent H100 `-O3` replay

`scratch/audit_reset_open_incidence_path_host_threshold_20260801.cpp`
reconstructs the complete-reversal packet for `1<=d<=12`, opens one common
edge, and independently checks:

* `4d+2` distinct roots;
* `4d+1` distinct lower and adjacent-upper colours;
* `8d+2` identical undirected incidence edges in both phases;
* maximum protected degree two; and
* the sharp application threshold `m=8d+4`.

The frozen H100 verdict is

```text
PASS_RESET_OPEN_INCIDENCE_PATH_HOST_THRESHOLD d=1..12
roots=4d+2 lower=upper=4d+1 incidence_edges=8d+2
phases=identical_undirected_path Delta=2 threshold=m>=8d+4
protected_Catalan_seed=link_path
```
