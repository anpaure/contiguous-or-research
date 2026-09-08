# Independent audit: gain-one Row-2 absorbers and forward linearization

**Date:** 2026-08-02  
**Audited source:**
`MATH_THEOREM_K_PCS_ROW2_PRIVATE_GAINONE_HEX_AND_TRANSPARENT_PULL_TREE_20260802.md`  
**Status:** **PASS after a fixed-slot catalogue clarification.**  The local
identity, canonical catalogue/load counts, greedy constant, and conditional
pull-tree implication are correct.  Fixed-`M_0` eligibility, graphic birth,
and the pull tree remain prospective hypotheses.

## 0. Corrections and scope

The count

\[
                         2(m-1)(m-2)                  \tag{0.1}
\]

is exact only after fixing one canonical auxiliary slot at every owner.
If auxiliary slots can be chosen afresh for every parameter triple, extra
literal lifts exist and (0.1) is no longer the count of *all* packets.  The
source theorem now explicitly defines the fixed-slot canonical
subcatalogue, assumes `m>=3`, and scopes (0.1) accordingly.

No other algebraic correction was needed.  In particular, the target upper
colour is physically supplied in the on phase by `f_a`; the bookkeeping
atom `e_b=A` is absent from that phase.  Therefore its old endpoints cannot
be reused when checking a fixed predecessor matching.  The source theorem
now records this point explicitly.

## 1. Literal odd-host identity

Put `r=m-1`, let `D` have rank `r`, and write

\[
                         V=D+p+q.                     \tag{1.1}
\]

Choose

\[
 b\in D,\qquad c\notin V,\qquad
 (a,s)\in\{(p,q),(q,p)\},\qquad K=D-b.               \tag{1.2}
\]

The lower and upper banks are

\[
 \begin{aligned}
 D_a&=K+a,&D_b&=K+b=D,&D_c&=K+c,\\
 U_{abs}&=K+a+b+s=V,
 &U_{acs}&=K+a+c+s,
 &U_{bcs}&=K+b+c+s.                                  \tag{1.3}
 \end{aligned}
\]

Every containment used by the two phases follows immediately:

\[
 \begin{array}{c|cc}
 D_a&U_{acs}&U_{abs}\\
 D_b&U_{abs}&U_{bcs}\\
 D_c&U_{bcs}&U_{acs}
 \end{array}                                         \tag{1.4}
\]

where an entry means containment.  With `X_uv=K+u+v`, the off phase uses

\[
 \{D_a,D_c\},\quad\{U_{acs},U_{bcs}\},\quad
 \{X_{ac},X_{as},X_{bc},X_{cs}\},                   \tag{1.5}
\]

and the on phase uses

\[
 \begin{gathered}
 \{D_a,D_b,D_c\},\quad
 \{U_{abs},U_{bcs},U_{acs}\},\\
 \{X_{ab},X_{as},X_{bc},X_{bs},X_{ac},X_{cs}\}.
                                                               \tag{1.6}
 \end{gathered}
\]

Subtracting (1.5) from (1.6) leaves exactly

\[
                         D,\quad V,\quad X_{ab},\quad X_{bs},  \tag{1.7}
\]

the four resources of the target atom.  The coordinates `a,b,c,s` are
distinct, so all six owner masks `X_uv` are distinct.  Both local physical
projections are therefore matchings, hence forests.

This proves the literal identity.  It does not show that replacing the off
phase inside an ambient forest avoids a global cycle.

## 2. Catalogue size and exact load

The ground has size `2m-1=2r+1`, while `V` has size `r+2`.  Hence

\[
       \#b=r,\qquad \#c=r-1,
       \qquad\#\text{orientations}=2,                 \tag{2.1}
\]

which gives (0.1).  Distinct parameter triples give distinct supports:
among the two auxiliary lower masks, `D_a` is the unique one containing a
member of `{p,q}`.  It recovers `a`, hence the orientation; its missing
member of `D` recovers `b`; and `D_c-D` recovers `c`.

For a fixed target, literal parameter recovery gives

\[
\begin{array}{c|c|c}
\text{resource}&\text{mask}&\text{load}\ \hline
D_a&D-b+a&r-1\\
D_c&D-b+c&2\\
U_{acs}&V-b+c&2\\
U_{bcs}&D+c+s&r\\
X_{ac}&D-b+a+c&1\\
X_{as}&V-b&2(r-1)\\
X_{bc}&D+c&2r\\
X_{cs}&D-b+c+s&1.
\end{array}                                           \tag{2.2}
\]

For example, `X_bc=D+c` leaves `b` and the orientation free, giving `2r`;
`X_as=V-b` leaves `c` and the orientation free, giving `2(r-1)`.
Every other row follows by direct recovery.  Under the fixed slot section,
a canonical owner-slot has the same load as its owner mask and a
noncanonical slot has load zero.  Thus the exact maximum non-target load is

\[
                              2r=2(m-1).              \tag{2.3}
\]

The four target resources are excluded from (2.2), correctly: every
candidate is required to contain them in its complete on/off support.

## 3. Greedy constant and cross-target audit

Assume the `p` target atoms are resource-disjoint at the literal
lower/upper/slot level and the external bank `B` meets no target.  When
choosing a packet for one target, forbid

\[
 |B|+4(p-1)+8(p-1)=|B|+12(p-1)                     \tag{3.1}
\]

non-target resources: the other target resources and all auxiliary
resources previously used.  Each kills at most `2r` candidates.  Therefore

\[
 |B|+12(p-1)<r-1                                   \tag{3.2}
\]

implies that fewer than

\[
                 2r(r-1)=|\mathcal Z(A)|             \tag{3.3}
\]

candidates are killed.  A greedy choice remains.  No probabilistic
independence is used, and overlaps among killed lists only improve the
bound.

There is no omitted cross-target resource collision in this argument.
Every earlier packet was chosen while all later target resources were
already forbidden.  Thus an earlier auxiliary cannot occupy a later target
resource.  Conversely, the current step forbids all earlier auxiliaries.

The conclusion is resource privacy, not owner-vertex disjointness.  Two
packets may use distinct slots of the same owner mask when the host permits
that.  Such sharing can affect physical degree or create a global graphic
cycle; those constraints are deliberately retained in `DOP`.

## 4. Prospective and pull-tree scope

The lossless absorption theorem is exact only after all off phases are
already present and all four target resources are free.  Resource identity
then shows that switching all private packets:

* preserves every old lower, upper and slot resource;
* adds each target lower and upper once; and
* adds the two target slots once.

It does not prove that an arbitrary factor contains the off phases.  It
also does not prove that the newly supplied occurrence of target upper `V`
is legal for the chosen `M_0`: that occurrence is `f_a`, so its rooted
tail/head must be checked from `f_a` in the common predecessor phase.

The transparent pull conclusion is likewise correctly conditional.  A
tree-coherent family must preserve the full palettes and representative
tokens, avoid the protected packet bank and opening, and remain available
in parent-before-child order.  Ordinary connectivity after resource
deletion does not prove tree coherence.  The displayed edge-connectivity
bound proves only survival of the unlabelled auxiliary graph.

Thus the audited unconditional implication is precisely

\[
 \text{resource-disjoint targets + prospectively planted off phases}
 \Longrightarrow
 \text{private lossless resource repair}.             \tag{4.1}
\]

Graphic birth, fixed-phase eligibility, transparent component fusion, and
the aperture-qualified cut remain open.

## 5. Recheck of the forward-potential selector

The independent Row-2 support audit reduces the remaining integral object
further.  Fix `M_0` and an injective potential `phi` increasing along the
protected pivot.  Every upper-colour fibre contains a directed cycle, so
its forward part

\[
                  E_\phi=\{u\to v:\phi(u)<\phi(v)\}   \tag{5.1}
\]

contains at least one arc of every upper colour.

An upper-surjective rooted Hamilton path exists on this fixed phase if and
only if one can select `Q subset E_phi` such that

\[
 \begin{aligned}
 |Q|&=W-1,\\
 |Q\cap\delta^+(v)|&\le1,
 &|Q\cap\delta^-(v)|&\le1 &&(v),\\
 |Q\cap E_R|&\ge1 &&& (R),                           \tag{5.2}
 \end{aligned}
\]

and retain the protected arcs.  Indeed, any undirected cycle under the two
port capacities would be coherently directed, contradicting strict
increase of `phi`.  Thus `Q` is a forest; `W-1` edges on `W` vertices make
it connected, and the port bounds make it one directed Hamilton path.  The
converse takes `phi` in path order.

For prescribed rooted source `s_*` and sink `t_*`, this equivalence also
requires

\[
 \phi(s_*)=\min\phi,qquad \phi(t_*)=\max\phi,qquad
 Q\cap\delta^-(s_*)=Q\cap\delta^+(t_*)=\varnothing.   \tag{5.3}
\]

In the corrected terminal aperture, `t_*=o` and `M_0(o)` is fixed to the
intended endpoint owner containing `o`.  Without (5.3), (5.2) proves only
an unpinned path.

The gain-one theorem and (5.2) therefore meet at one exact interface:
`DOP` must plant every target on-phase occurrence as an allowed forward arc
while preserving the two port capacities.  Resource repair alone does not
establish this interface.

## 6. Final verdict

Proof-safe:

* literal `2 -> 3` gain-one identity;
* fixed-slot canonical catalogue `2(m-1)(m-2)`;
* maximum non-target resource load `2(m-1)`;
* greedy privacy under `|B|+12(p-1)<m-2`;
* lossless resource repair after prospective off-phase planting; and
* the conditional transparent pull-tree implication.

Still open:

* birth of the off phases in one lower-rainbow graphic support;
* fixed-`M_0` tail/head eligibility of `f_a` for every repaired upper;
* the coloured near-perfect matching (5.2)--(5.3);
* a surviving tree-coherent pull tree and protected cut; and
* every later `PCS` row.

No `PCS`, `PCPS`, all-parameter Row 2, or K17 completion follows from the
catalogue alone.
