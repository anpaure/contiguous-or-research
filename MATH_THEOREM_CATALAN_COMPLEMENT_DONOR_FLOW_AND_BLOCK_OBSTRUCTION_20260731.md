# Complement donor flow: the exact split-capacity relaxation and its block obstruction

Date: 2026-07-31  
Status: exact all-parameter reduction, exact obstruction to the naive
submodular-flow rounding, and exact parameter-three coupled physical
certificate.  No all-parameter physical/common-cap construction is claimed.

## 0. Result

There are two superficially similar complement couplings in the Catalan
recursion.  They behave differently.

1.  For the endpoint/SBE gate, complementarity really does turn the two
    shore systems into one supermodular **split-capacity** flow.  However, a
    path orientation moves one indivisible block of size `C`; ordinary
    submodular-flow integrality only makes the flow integer one unit at a
    time.  The authenticated `n=3` half-endpoint obstruction is exactly this
    divisibility gap.
2.  For the later physical Farkas gate, complementing one positive
    straddling row need not produce an opposite straddling donor row.  In the
    literal `n=3` example the complemented row is redundant on every common
    basis.  Nevertheless the **complete** two-shore system is stronger: one
    exact joint dual certificate forces the unique retained bank `p_14=1`,
    and that bank has an integral two-shore physical-forest witness.

Thus the correct positive target is an aggregate coupled donor theorem with
block indivisibility.  It cannot be obtained by pairing Farkas rows under
complement, nor by applying an off-the-shelf integral submodular-flow theorem
to the capacity-split relaxation.

## 1. Closed-neighbourhood SBE is supermodular before division

Fix one direct occurrence graph

\[
                  G=(O,X)
\]

of a fixed undirected Catalan path forest.  Use the standard parameters
`N=R+C`.  For `A subseteq X`, put

\[
 h_G(A)=|\{o\in O:N_G(o)\subseteq A\}|,
 \qquad
 g_G(A)=N h_G(A)-R|A|.                              \tag{1.1}
\]

### Theorem 1.1 (closed-neighbourhood form)

A terminal bank `Z subseteq X` is SBE on this shore if and only if

\[
                   C|Z\cap A|\ge g_G(A)
                   \qquad(A\subseteq X).             \tag{1.2}
\]

Moreover `g_G` is an integer supermodular set function.

#### Proof

The usual weighted Hall rows are

\[
 R|N_G(\mathcal A)|+C|Z\cap N_G(\mathcal A)|
       \ge N|\mathcal A| \qquad(\mathcal A\subseteq O). \tag{1.3}
\]

If (1.2) holds, take `A=N_G(mathcal A)`.  Every member of `mathcal A` has
its neighbourhood contained in `A`, so (1.2) implies (1.3).

Conversely, fix `A subseteq X` and take

\[
        \mathcal A_A=\{o\in O:N_G(o)\subseteq A\}.
\]

Its neighbourhood is contained in `A`.  Applying (1.3), then enlarging its
two nonnegative neighbourhood terms from `N_G(mathcal A_A)` to `A`, gives
(1.2).

For a fixed set `S=N_G(o)`, the indicator
`1[S subseteq A]` is supermodular in `A`: the only nontrivial case is when
`S` is contained in `A union B` but in neither `A` nor `B`, when the
supermodular inequality has right side one and left side zero.  Summing over
`o`, multiplying by `N`, and subtracting the modular function `R|A|`
proves the last assertion.  `square`

This formulation removes the apparently arbitrary maximization over outer
families.  The ceiling appears only when the indivisible terminal decision
is imposed:

\[
 |Z\cap A|\ge
       \left\lceil {g_G(A)\over C}\right\rceil.       \tag{1.4}
\]

## 2. Two shores form a split-capacity flow, not a Boolean flow

Delete the fixed singleton components and let `H` be the matching whose
edges are the two endpoints of each nontrivial path.  Write `z_x=1` if the
upper shore selects endpoint `x`; then

\[
 z_u+z_v=1\quad(uv\in E(H)),
 \qquad z_x^{\rm lo}=1-z_x.                           \tag{2.1}
\]

After subtracting the fixed singleton contribution, Theorem 1.1 gives the
exact simultaneous system

\[
\begin{aligned}
 C z(A)&\ge \widetilde g^-(A),\\
 C(|A|-z(A))&\ge \widetilde g^+(A),
                         \qquad(A\subseteq V(H)),     \tag{2.2}\\
 z_u+z_v&=1\qquad(uv\in E(H)),\\
 z_x&\in\{0,1\}.
\end{aligned}
\]

The two functions `tilde g^-`, `tilde g^+` remain supermodular after the
modular singleton correction.

Put `y=Cz`.  Dropping the last Boolean row turns (2.2) into

\[
\begin{aligned}
 y(A)&\ge\widetilde g^-(A),\\
 y(A)&\le C|A|-\widetilde g^+(A),\\
 y_u+y_v&=C,qquad 0\le y_x\le C.                    \tag{2.3}
\end{aligned}
\]

The first set function is supermodular and the second is submodular.  This
is the natural generalized-polymatroid/submodular-flow relaxation suggested
by complement symmetry.

### Theorem 2.1 (the exact block obstruction)

Integral feasibility of (2.3) does not imply a coherent path orientation.
The missing condition is

\[
                         y_x\in\{0,C\},               \tag{2.4}
\]

whereas an integral submodular-flow theorem supplies only
`y_x in {0,1,...,C}`.  Equivalently, normalizing first restores the Boolean
matching base (2.1), but replaces the supermodular right side by

\[
       \left\lceil\widetilde g(A)/C\right\rceil,      \tag{2.5}

which need not be crossing supermodular.

#### Proof and sharpness

All assertions except sharpness follow directly from (2.2)--(2.3).  For the
authenticated `n=3` forest, `C=14`.  The half-endpoint point `z_x=1/2`
satisfies every exact row on both shores, so `y_x=7` is an **integer**
solution of the split-capacity system.  Nevertheless no one of the coherent
endpoint orientations is SBE: the rounded lower-shore demands on the two
ends `19,49` of one matching edge are both one.  One orientation cannot
enter both singleton blocks.  The same fixture gives the already-audited
positive crossing-supermodularity violation after (2.5).

Thus even integer split-capacity flow is strictly weaker than coherent
orientation.  `square`

This resolves the ceiling issue: it is not a technical rounding nuisance.
It is exactly the operation that reinstates an indivisible `C`-packet, and
it can destroy the supermodularity needed by the standard theorem.

## 3. Complement does not pair physical Farkas rows

For an oriented child edge `e=(t_e,h_e)`, write

\[
 L_e=t_e\cap h_e,qquad U_e=t_e\cup h_e.
\]

An upper physical dual triple `(a,b,z)` has modular edge cost

\[
                       c_e^+=z_{U_e}-a_{t_e}.          \tag{3.1}

Complementing a lower-shore diamond to the same rank-three-to-rank-five
normal form gives

\[
                       c_e^-=z_{\overline{L_e}}
                                -a_{\overline{h_e}}.  \tag{3.2}

There is no sign or permutation relation between (3.1) and (3.2) unless the
oriented parent itself has a complement-reversing automorphism matching the
two labelled pairs.  Complement symmetry of the Boolean lattice alone is
therefore insufficient for rowwise donor pairing.

### Theorem 3.1 (literal failure of rowwise pairing)

For the authenticated parameter-three oriented parent, the upper dual row

\[
 a_{07}=a_{13}=a_{23}=1,quad a_{34}=-1,quad
 b_{37}=1,quad z_{17}=z_{27}=z_{33}=1               \tag{3.3}

has values

\[
 (1,-1,0,0,0,0,0,0,-1,0,-1,0,0,0,-1)               \tag{3.4}
\]

on the fifteen co-singleton common bases.  Its literal complemented lower
row has values

\[
 (-1,0,0,0,0,-1,0,0,0,0,0,0,0,-1,0).               \tag{3.5}

Thus the upper row genuinely straddles, but its complement is redundant and
has no positive basis at all.

The exact replay is in the audit cited below.  This disproves the proposed
rule “every positive straddling row is paired by complement with an opposite
donor row.”  It does not disprove aggregate two-shore integrality.

## 4. Aggregate coupling succeeds exactly in the same fixture

Let `p_i` denote the retained-edge distribution, so the selected deletion
vector is `q=1-p` and `sum_i p_i=1`.  Put both complete unlabelled physical
marginals in rank-three-to-rank-five normal form.  Their variables are

\[
 p_i\ge0,qquad w^s_{D,V}\ge0\quad(s=0,1),            \tag{4.1}

with punctured row sums `p_i`, five unpunctured row sums one, all six top
row sums one, and owner capacities `1+p_i` at the fifteen anchors and two
elsewhere.

### Theorem 4.1 (exact joint donor collapse at `n=3`)

For the literal parent of Theorem 3.1, the projection of the complete joint
fractional physical system onto `p` is

\[
                         \boxed{p=e_{14}}.             \tag{4.2}

Moreover `p=e_14` has integral side matchings whose contracted attachment
graph is a forest.

#### Proof

The exact audit stores one joint dual combination.  Its capacity
multipliers are nonnegative; every `w` coefficient is nonnegative; its
coefficient on each of `p_0,...,p_13` is at least one; and its right side is
zero.  Hence every feasible point satisfies

\[
                         \sum_{i=0}^{13}p_i\le0.       \tag{4.3}

Nonnegativity and `sum p_i=1` force (4.2).  Conversely, the audit replays
the following two literal matchings at retained basis 14:

```text
upper:  0b->1f, 23->2f, 13->37, 31->3b, 0d->3d, 0e->3e;
lower:  04->16, 08->2c, 01->31, 02->32, 20->34, 10->38.
```

They saturate both outer palettes, respect every ordinary capacity two and
every seam-anchor capacity one, and are forests.  Contracting their anchor
components together with the retained central edge gives cycle rank zero.
This proves feasibility and the graphic assertion.  `square`

The joint dual is only fifty-three nonzero integer multipliers, not a
floating-point solver report.  It demonstrates the right phenomenon:
individual rows may straddle asymmetrically, while their aggregate across
both shores exposes one integral bank.

## 5. Consequence for the general construction

Complement symmetry supplies a useful continuous model, but there are two
distinct exactness requirements:

1. **endpoint block coherence:** all `C` capacity units belonging to one
   path must choose the same endpoint;
2. **aggregate physical donor balance:** the complete upper/lower Farkas
   systems must be combined before rounding; their rows do not pair
   individually.

A sufficient all-parameter theorem could therefore be a block-submodular
flow theorem specialized to Catalan endpoint pairs, or a recursive
construction that exports the block choices explicitly.  A theorem about
ordinary integral submodular flow, independent shore polymatroids, or
rowwise complemented donors cannot suffice.

The weakest useful all-parameter formulation suggested by Theorem 4.1 is
an **integral-point property**, not total dual integrality:

> **Aggregate Catalan block-donor lemma (target).**  At every recursive
> parameter `n>=4`, the allowed structural-child menu contains one forest
> `F` for which the joint extended system consisting of
> 
> * complementary endpoint blocks `z_u+z_v=1`;
> * one strict common basis `Q` for the resulting two endpoint maps;
> * both complete physical marginal systems; and
> * the contracted attachment graphic row
> 
> is nonempty and has at least one point with `z`, `1_Q` and both physical
> selectors integral.

This deliberately does **not** demand that every parent work, that every
fractional point round, that the whole projection be an integral
generalized polymatroid, or that dual rows pair individually.  It asks only
for the one block-integral point actually needed by the induction.  The
`n=3` certificate proves the strongest possible finite calibration—its
complete fractional projection already collapses to such a point—but the
all-parameter lemma remains open.  Residence, deeper witnesses and common
cap regeneration remain downstream rows unless they are included in the
recursive child menu.

Exact finite source:

```text
scratch/audit_catalan_n3_joint_donor_collapse_20260731.py
scratch/catalan_n3_joint_donor_collapse_20260731.audit.json
```

The existing `n=3` SBE half-point and ceiling obstruction is independently
replayed in:

```text
scratch/audit_h2_catalan_sbe_endpoint_orientation_20260731.py
scratch/h2_catalan_sbe_endpoint_orientation_20260731.audit.json
```
