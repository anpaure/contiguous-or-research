# The controlled Catalan packet is exactly a decorated two-factor cut, but not a frozen-`M_0` ear

Date: 2026-08-01  
Lane: controlled Catalan leave / physical topology / fixed-SCD comparison  
Status: unconditional equivalence and exact fixed-`M_0` phase obstruction.
The one-stratum decorated factor is impossible by the coordinate cocycle;
the shared-signature resource-disjoint two-stratum packet/hole bank exists
only asymptotically and requires `2C<=binom(2m-3,m-2)`, first at `m=15`.
The separate-target phase-compatible bank is asymptotically positive, while
its common owner basis and decorated-factor completion remain open.

## 0. Outcome

For one controlled packet write

\[
 S<L,\qquad V=S+b,
\]

and put

\[
 D=zL,\qquad A=aL,\qquad C_0=azS,\qquad B=aV.       \tag{0.1}
\]

These four rank-`m` owners form the Johnson three-path

\[
                         D-A-C_0-B.                 \tag{0.2}
\]

Its edge colours are

\[
\begin{array}{c|c|c}
\text{edge}&\text{lower intersection}&\text{upper union}\\ \hline
D-A&L&azL\\
A-C_0&aS&azL\\
C_0-B&aS&azV.
\end{array}                                         \tag{0.3}
\]

Thus the controlled-leave construction can be restated exactly as a
decorated spanning two-factor problem:

* every packet contributes the whole path (0.2);
* the middle edge `A-C_0` is marked for deletion;
* the background uses every unreserved owner slot, lower colour and upper
  colour exactly as in the residual host; and
* every cycle of the factor contains a marked middle edge.

Deleting the `C=Cat_m` marked middle edges gives the desired upper-exact
`C`-component linear forest.  Conversely, adding those middle edges to a
controlled-leave forest gives the decorated two-factor.  This equivalence
turns the former residual-forest gate into a support-first factor gate, but
does not evade the coordinate obstruction: no one-stratum decorated factor
exists.

There is also an exact phase boundary.  Under the frozen four-row SCD
matching `M_0`,

\[
                         M_0(L)=zL=D,
 \qquad                   M_0(aS)=aL=A.             \tag{0.4}
\]

Hence `D-A` and `A-C_0` are rooted at one of their physical endpoints, but
the target edge `C_0-B` is not: its lower colour is `aS`, while
`M_0(aS)=A` is neither `C_0` nor `B`.  Therefore the standard fixed-`M_0`
paired-ear grammar cannot instantiate the controlled packet.  Any positive
construction must change the owner basis or select the support and basis
jointly.

## 1. Exact two-factor equivalence

Use the full odd owner layer

\[
 \mathcal M={\Omega\choose m},\qquad |\mathcal M|=W,
\]

and let

\[
 U={2m-1\choose m+1},\qquad C=W-U=\operatorname {Cat}_m.
\]

Assume a resource-disjoint controlled packet bank of order `C`.  Its four
owner banks `A,B,C_0,D` are pairwise disjoint, including across packet
types.  For packet `i`, denote the three edges in (0.2) by

\[
 e_i^L=D_iA_i,\qquad e_i^0=A_iC_i,
 \qquad e_i^R=C_iB_i.                               \tag{1.1}
\]

### Definition 1.1 (decorated packet factor)

A decorated packet factor is a spanning two-factor `Z` on `\mathcal M`
such that:

1. `Z` contains all three edges in (1.1) for every packet;
2. its remaining `W-3C` edges use exactly the residual upper resources,
   distinct residual lower resources and all residual owner slots;
3. among those residual lower resources exactly `C` are unused; and
4. every cycle of `Z` contains at least one marked edge `e_i^0`.

The colour multiplicities of `Z` are then forced.  Every upper colour is
used once, except the `C` auxiliary colours `azL_i`, which are used twice.
Every used lower colour is used once, except the `C` old lower colours
`aS_i`, which are used twice; exactly `C` lower colours are absent.

### Theorem 1.2 (cut-factor equivalence)

The following objects are equivalent.

1. A matching in the controlled residual host saturating all residual
   upper resources and owner slots, whose physical projection is a forest.
2. An upper-exact spanning linear forest on `\mathcal M` containing every
   outer packet edge `e_i^L,e_i^R`, with endpoints exactly
   `{A_i,C_i:1<=i<=C}`.
3. A decorated packet factor.

Under the equivalence, object 2 is obtained from object 3 by deleting all
marked edges `e_i^0`.

#### Proof

Start from object 1.  Its residual counts are

\[
 \text{edges}=U-2C=W-3C.
\]

Its endpoint slots are exactly the free slots at `B_i,D_i`.  Add the outer
edges `D_i-A_i` and `C_i-B_i`.  The new owners `A_i,C_i` become leaves,
every `B_i,D_i` endpoint becomes internal, and no cycle is created.  The
resulting spanning forest has

\[
 (W-3C)+2C=W-C=U
\]

edges, hence exactly `C` components.  Formula (0.3) and the reserved
resource ledger show that every upper colour occurs exactly once.  This is
object 2.

Add all middle edges `A_i-C_i`.  Every degree-one endpoint receives one
new edge, so every owner has degree two.  The result is a spanning
two-factor.  Its three packet edges have precisely the colour ledger
(0.3), while the background has the residual ledger, giving Definition
1.1(1)--(3).  Since the graph before the addition was a forest, every
resulting cycle contains at least one added middle edge.  Thus object 3
holds.

Conversely, remove all marked middle edges from a decorated factor.  The
cycle-hitting condition makes the result acyclic.  Exactly `C` edges were
removed, so the result has `C` path components; its only degree-one owners
are `A_i,C_i`.  Formula (0.3) deletes precisely the repeated occurrence of
each auxiliary upper colour, leaving every upper colour once.  This is
object 2.  Finally remove every outer packet edge and the now-isolated
owners `A_i,C_i`.  The remaining edges lie in the residual resource host,
saturate every residual upper and owner slot, and remain acyclic.  This is
object 1. \(\square\)

## 2. The one-stratum factor is impossible

Put `c=Cat_(m-1)`.  The coordinate-cocycle theorem for an upper-exact
owner forest says that its endpoint and unused-lower degree vectors obey

\[
                             E_t=H_t+2c.             \tag{2.1}
\]

In one active stratum every one of the `2C` final endpoints `A_i,C_i`
contains the distinguished coordinate `a`.  Therefore `E_a=2C`, so (2.1)
would require

\[
                         H_a=2C-2c>C\qquad(m>=3).    \tag{2.2}
\]

But only `C` lower colours are unused.  Hence object 2 in Theorem 1.2, and
therefore the decorated packet factor, does not exist in one stratum.

This is a palette obstruction before topology.  Changing the cycle
structure of the factor cannot repair it.

## 3. Exact frozen-`M_0` phase obstruction

The standard four-row SCD matching roots every lower colour `q` at the
owner `M_0(q)`.  For the controlled packet,

\[
 M_0(L)=zL=D,
 \qquad
 M_0(aS)=aL=A.                                      \tag{3.1}
\]

Thus:

* `D-A` has lower colour `L` and endpoint `D=M_0(L)`;
* `A-C_0` has lower colour `aS` and endpoint `A=M_0(aS)`;
* `C_0-B` has lower colour `aS`, but neither endpoint equals
  `M_0(aS)=A`.

The last edge is therefore absent from every support whose directed
diamonds are required to be rooted in the frozen `M_0` row.  In particular,
the fixed-`M_0` short-triangle paired-ear selector cannot contain the full
three-edge packet path.

This is not a no-go for SCD methods in general.  It says exactly that the
controlled packet is **basis-changing**.  A future construction may use

1. a different owner matching adapted to the target edges;
2. a simultaneous selection of the owner basis and decorated support; or
3. a multi-phase detachment which changes `M_0` before the target edge is
   installed.

The existing theorem that extends a protected incidence subgraph of at
most `m-2` edges to a spanning two-factor does not apply to this bank:
the decorated packet support already has `3C` prescribed edges.

## 4. Repaired frontier

The one-stratum residual theorem is closed negatively.  The minimum
singleton-coordinate repair uses two swapped active strata, as constructed
in
`MATH_THEOREM_TWO_STRATUM_PACKET_COORDINATE_COCYCLE_FEASIBILITY_20260801.md`.
That theorem supplies the shared-signature resource-disjoint typed packet
bank only in its stated sufficiently-large range and an exact simple hole
family, but not the decorated factor.  It cannot be instantiated at
`m=6,7,8,9` because its two upper banks already violate `2C<=N`.  The
corrected separate-`aU/zU` phase bank is given asymptotically in
`MATH_THEOREM_CATALAN_PHASE_COMPATIBLE_PAIRED_KNESER_BLOCK_BANK_20260801.md`;
its planted `3C` owner-basis rows still require a residual Hall extension.

The remaining owner-layer target is therefore:

> Complete the explicit two-stratum packet bank to a spanning decorated
> two-factor containing all its three-edge paths, with every cycle hit by a
> middle packet edge.

The separate connector-repeat cocycle theorem
`MATH_THEOREM_CATALAN_CONNECTOR_REPEAT_DESIGN_COCYCLE_20260801.md` proves
that the repeated-upper multiset required by a final Hamilton path has an
abstract regular realization.  It does not yet place those repeats on the
literal component endpoints of this two-stratum factor.
