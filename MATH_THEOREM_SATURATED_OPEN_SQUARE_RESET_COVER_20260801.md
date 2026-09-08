# Saturated coordinate covers for the support-four open-square reset

Date: 2026-08-01

Status: unconditional robust coordinate-cover theorem, exact open-square
resource count, and a conditional literal reset-host consequence.  The
result converts a bounded number of dead coordinate blocks into a longer
Chapter-9 word.  It does **not** prove that the Boolean host has bounded
dead-block number; that is now the exact physical lifting hypothesis.

## 0. Verdict

The Chapter-9 two-sided cover is useful at the rolling reset only after the
three boundary returns are bundled into one state symbol and one raw
coordinate is interpreted as one **coupled support-four open Johnson
square**.  Applying the cover separately to the attachment and two
predecessor returns is invalid: it may choose three coordinates and three
different orientations.

There is a fault-tolerant version with explicit parameters.  Let `H` be the
size of the bundled boundary alphabet, put

\[
 q=\lceil 2H\log H\rceil,
 \qquad s_0=q(q+1)+1,                                    \tag{0.1}
\]

and let `b` be a proposed upper bound on the number of physically dead
coordinate blocks for one state pair.  With

\[
 R=b+1,
 \qquad S=R s_0,                                          \tag{0.2}
\]

there are fixed maps on `[H]^S` which give at least one raw coordinate in
each of `R` disjoint blocks.  Therefore at most `b` dead blocks cannot kill
all witnesses.  Quantitatively,

\[
                 S=O\bigl((b+1)H^2\log^2 H\bigr).          \tag{0.2a}
\]

For a fixed adjacent middle-layer seam, one raw square coordinate has

\[
 (r-1)(k-r-1)                                             \tag{0.3}
\]

possible physical `(p,z)` cores.  A fixed forbidden nonseam immediate
resource kills at most

\[
 \max\{r-1,k-r-1\}                                        \tag{0.4}
\]

of them.  Thus bounded owner/q1 collision banks can be avoided
prospectively.  Equations (0.1)--(0.4), however, do not bound the genuinely
global dead blocks caused by arbitrary-width upper witnesses, residence,
the fixed-cap compiler, or failure of common phase contraction.

## 1. Bundled boundary states

Let the reset boundary data have finite typed state sets

\[
 \Sigma_{\mathsf A},\qquad
 \Sigma_{\mathsf P_0},\qquad
 \Sigma_{\mathsf P_1},\qquad
 \Sigma_{\rm phase},\qquad
 \Sigma_{\rm guard}.
\]

The guard state may contain any bounded information which the induction
really transports: clipped residence flags, protected-witness addresses,
cap state, and endpoint type.  Put

\[
 \Omega=\Sigma_{\mathsf A}\times
        \Sigma_{\mathsf P_0}\times
        \Sigma_{\mathsf P_1}\times
        \Sigma_{\rm phase}\times
        \Sigma_{\rm guard},
 \qquad H=|\Omega|,                                       \tag{1.1}
\]

and identify `Omega` with `[H]`.  A left and right boundary state are
encoded by words

\[
                         X,Y\in[H]^S.                       \tag{1.2}
\]

The product in (1.1) is load-bearing.  It forces a selected coordinate to
choose the attachment return, both signed predecessor returns, the phase,
and the guard state simultaneously.

## 2. A robust two-sided coordinate cover

Chapter 9, Lemma 2.2 gives fixed maps

\[
 f_0,g_0:[H]^{s_0}\longrightarrow[H]^{s_0}                 \tag{2.1}
\]

such that for every `x,y` some coordinate `d` satisfies

\[
       x_d=f_0(y)_d
       \quad\hbox{or}\quad
       y_d=g_0(x)_d.                                       \tag{2.2}
\]

Partition `[S]` into consecutive blocks

\[
                  I_1\dot\cup\cdots\dot\cup I_R,
                  \qquad |I_t|=s_0.                        \tag{2.3}
\]

Define `F,G:[H]^S -> [H]^S` blockwise by applying `f_0,g_0`
inside every `I_t`.

### Theorem 2.1 (R-fold two-sided cover)

For every `X,Y in [H]^S` and every `t in [R]`, the raw cell set

\[
\begin{aligned}
 {cal C}_t(X,Y)=
 &\{(+,d):d\in I_t,\ X_d=F(Y)_d\}\\
 &\cup\{(-,d):d\in I_t,\ Y_d=G(X)_d\}
\end{aligned}                                             \tag{2.4}
\]

is nonempty.  In particular, the full cover has witnesses in `R`
different coordinate blocks.

#### Proof

Restrict `X,Y` to `I_t` and apply (2.2).  The resulting coordinate belongs
to (2.4).  The blocks are disjoint, so the `R` witnesses are distinct.
\(\square\)

This elementary block product is the exact robustness that the one-copy
reset use needs.  It does not assert that the witnesses are physical.

## 3. The literal support-four square attached to one coordinate

Let `E,F` be adjacent rank-`r` owners and write

\[
 E=L\cup\{x\},\qquad F=L\cup\{y\},\qquad
 U=L\cup\{x,y\},                                         \tag{3.1}
\]

where `|L|=r-1`.  Choose

\[
             p\in L,qquad z\in[k]\setminus U             \tag{3.2}
\]

and put

\[
 E'=L-p+x+z,qquad F'=L-p+y+z.                             \tag{3.3}
\]

The two orientations of the open Johnson square are

\[
\begin{aligned}
 {cal S}^{+}_{p,z}&:E\longrightarrow E'\longrightarrow F'
                      \longrightarrow F,\\
 {cal S}^{-}_{p,z}&:F\longrightarrow F'\longrightarrow E'
                      \longrightarrow E.                  \tag{3.4}
\end{aligned}
\]

They have the same three lower and upper/owner resources

\[
\begin{aligned}
 D_x&=L-p+x,&D_0&=L-p+z,&D_y&=L-p+y,\\
 O_x&=L+x+z,&O_0&=L-p+x+y+z,&O_y&=L+y+z.                  \tag{3.5}
\end{aligned}
\]

Their symmetric difference has exactly the opened reset signature:

* one head--owner alternating path from `E` to `F`; and
* the two correctly crossed predecessor tail--head paths.

This is Theorem 8.4 of
`MATH_THEOREM_H3_NONLEXICAL_PROTECTED_RADO_FOREST_AND_TRANSPARENT_CONNECTOR_GATE_20260801.md`.
The omitted fourth edge is the direct seam `EF`; its unique lower and owner
resources `L,U` are shared internally and are not selected in either
square phase.

Thus one raw coordinate must select one pair `(p,z)` and one orientation
of (3.4).  It must not select three independent return paths.

## 4. Exact immediate-resource supply

Put

\[
 a=|L|=r-1,qquad c=|[k]\setminus U|=k-r-1,
 \qquad M=\max\{a,c\}.                                    \tag{4.1}
\]

There are exactly

\[
                         ac                                \tag{4.2}
\]

square cores `(p,z)`.  For central rank this is `(m-1)^2` when
`k=2m,r=m`, and `m(m-1)` when `k=2m+1,r=m+1`.

### Lemma 4.1 (typed collision multiplicity)

Fix one typed lower resource, typed owner resource, or internal middle
root other than the seam resources and endpoints.  At most `M` pairs
`(p,z)` use it in (3.3)--(3.5).

#### Proof

The lower families `D_x,D_y` determine `p` and then allow all `c` choices
of `z`; `D_0` determines `(p,z)`.  Their outside-`L` membership patterns
are respectively `x`, `y`, and `z`, so a fixed lower target cannot belong
to two of these families.

The owner families `O_x,O_y` determine `z` and then allow all `a` choices
of `p`; `O_0` determines `(p,z)`.  Their membership patterns in `x,y`
separate the three families.  Finally `E'` and `F'` each determine
`(p,z)`, and are separated by containing `x` or `y`.  The largest
multiplicity is therefore `max(a,c)=M`. \(\square\)

### Corollary 4.2 (prospective clean coordinate bank)

Let `B` be a fixed bank of forbidden typed immediate resources and
internal roots, not including the mandatory seam endpoints/resources.
At least

\[
                         ac-|B|M                           \tag{4.3}
\]

square cores avoid `B`.  Hence `S` distinct clean coordinate cores may be
assigned whenever

\[
                         ac-|B|M\ge S.                     \tag{4.4}
\]

The cores in (4.4) are alternative prospective columns; the corollary does
not claim that all `S` alternatives coexist in one frozen factor.

For fixed `H,b,|B|` and central `r`, the left side of (4.4) is
`Theta(k^2)` while `S` is constant.  Hence static owner/q1 avoidance has
ample asymptotic supply.  This conclusion does not extend to guards whose
forbidden set depends nonlocally on the selected square.

## 5. Literal eligibility and dead blocks

For a raw cell `(sigma,d) in C_t(X,Y)`, let

\[
                 {\cal Q}_{\sigma,d}(X,Y)                  \tag{5.1}
\]

be its menu of occurrence-labelled square cores.  A member is **eligible**
only if all of the following hold in one literal host.

1. **Coupled return.**  Its one square supplies the attachment and both
   predecessor returns with the signs encoded in the bundled symbol.
2. **One-copy owner/q1.**  The resources (3.5), physical roots, and marked
   occurrences are simple after the declared alternating removals and do
   not collide with the exterior.
3. **Upper guard.**  Every arbitrary-width upper target has a retained or
   explicitly recreated witness after the phase exchange.
4. **Residence guard.**  Every affected coordinate run is legal at depth
   `d(k)`.  In particular, the three square turns are not silently treated
   as a consecutive strict source segment when that creates short runs.
5. **Compiler guard.**  In one fixed cap `theta`, the complete hazard union
   is independent in the dual compiler transversal/strict gammoid.
6. **Common phase exterior.**  Contracting the combined reset-plus-square
   bank in the two phases leaves literally the same represented residual
   table and the required common matroid minors.
7. **Private auxiliary palette.**  Every nonshared chronology, flag,
   provider, witness and compiler-sink occurrence lies in the coordinate's
   declared private palette.  Only the cancellation resources internal to
   the coupled square may be shared.

Write `Q^elig_{sigma,d}(X,Y)` for the eligible sub-menu and define

\[
 {cal E}_t(X,Y)=
 \bigcup_{(\sigma,d)\in{cal C}_t(X,Y)}
             {\cal Q}^{\rm elig}_{\sigma,d}(X,Y).          \tag{5.2}
\]

Block `t` is **dead** for `(X,Y)` when `E_t(X,Y)` is empty.

### Theorem 5.1 (robust saturated open-square reset cover)

Assume that every boundary state is bundled as in (1.1), and that for
every pair `X,Y` at most `b` of the `R=b+1` blocks are dead.  Then every
boundary-state pair admits an eligible support-four open-square reset
packet.

If the two contracted residual stages additionally satisfy the nested
Rado rank conditions of the protected-host theorem, the packet gives a
switch-ready protected reset host.

#### Proof

By Theorem 2.1 every block has at least one raw coordinate cell.  At most
`b` blocks are dead, while there are `b+1` blocks.  Choose a live block
and an eligible member of (5.2).  Its orientation is the sign of its raw
cell.  The support-four identity gives all three typed returns on that one
coordinate, and eligibility Conditions 2--7 give every physical and guard
row.  The final statement is exactly the contraction-and-nested-Rado
implication of the protected-host theorem. \(\square\)

The exact, non-numerical condition in this coordinate architecture is

\[
 \forall X,Y\qquad
       \bigcup_{t=1}^{R}{\cal E}_t(X,Y)\ne\varnothing.      \tag{5.3}
\]

The dead-block bound is a convenient sufficient way to prove (5.3), not a
necessary one.

### Corollary 5.2 (cell-fault form)

If for every pair `(X,Y)` at most `b` raw coordinates in the whole cover
have empty eligible menu, then Theorem 5.1 applies.

#### Proof

A dead block contains at least one raw coordinate by Theorem 2.1, and all
its raw coordinates have empty eligible menu.  Distinct dead blocks
therefore consume distinct bad coordinates. \(\square\)

## 6. Orientation palettes

Suppose two abstract palettes `P,Q` satisfy

\[
                |Q\setminus P|\ge S,
                \qquad |P\setminus Q|\ge S.                \tag{6.1}
\]

Choose distinct labels

\[
 a_d\in Q\setminus P,qquad b_d\in P\setminus Q
                         \quad(d\in[S]).                    \tag{6.2}
\]

Use `a_d` on the `+` branch and `b_d` on the `-` branch.  This is exactly
the separated-palette role in Chapter 9: the chosen orientation has a
coordinate-specific label active on one side and absent on the other.

To become physical, (6.2) needs a **palette realization map** sending the
chosen abstract label to the auxiliary occurrence bank of an eligible
square while preserving all literal types.  Distinct abstract labels do
not themselves imply disjoint physical owners, q1 targets, upper witnesses,
or compiler sinks.  Theorem 5.1 assumes that realization in Condition 7.

For `H>=3`, the separated-palette packing proof of Chapter 9 applies with
the enlarged coordinate count `S` (take palette size
`S ceil(log H)`), so the block replication changes only the constants in
the palette recursion.

## 7. Why raw equality is insufficient

The implication

\[
 X_d=F(Y)_d\ \hbox{or}\ Y_d=G(X)_d
 \quad\Longrightarrow\quad
 \hbox{eligible square}                                  \tag{7.1}
\]

is false without the explicit lift hypotheses.

* **Owner/q1:** the square is internally simple, but one of (3.5) may be an
  incumbent exterior occurrence.  Abstract palette separation cannot split
  a physical owner fibre.
* **All-width upper deck:** reversing the three turns changes their order
  in the ambient chronology.  Immediate owners agree, but intervals
  crossing the module can lose their only upper witness.
* **Residence:** the uncollared three-edge path has short coordinate runs
  when read consecutively.  A legal occurrence lift must use a planted
  nonconsecutive flag table or a separately proved resident collar.
* **Compiler:** three otherwise private return hazards may form the sharp
  `U_(2,3)` safe-deletion obstruction: every proper subfamily is safe and
  the union is not.
* **Common exterior:** the two phasewise residual matroids can separately
  pass Rado while having no common task transversal (the three-label
  Borromean minor).
* **Coupling:** three separate applications of the cover can choose three
  coordinates or signs.  Only the bundled square identity guarantees that
  the head--owner and two tail--head projections come from the same literal
  turns.

Consequently the new theorem removes only a **bounded coordinate-hole**
obstruction.  It does not prove that the number of physically dead blocks
is bounded.

## 8. Exact remaining theorem

The Chapter-9 route is now reduced to the following Boolean statement.

> **Bounded dead-block square-lift lemma.**  For one prospectively selected
> reset seam and the `R=b+1` block coordinate atlas above, there is an
> absolute `b` such that every bundled boundary pair leaves at most `b`
> blocks without an eligible occurrence-labelled open-square core.

Together with the common residual nested-Rado conditions, this lemma and
Theorem 5.1 give a switch-ready reset for every bounded boundary state.
If the reset regenerates the same atlas after the same-parity lift, it is
the precise finite-state input needed by the bounded-defect `B(k)+O(1)`
programme.

What remains hard is proving the dead-block lemma simultaneously for the
upper, residence, compiler, and common-exterior guards.  The saturated
matrix supplies the redundancy **after** that bound; it does not establish
the bound.

## 9. Dependencies

* Chapter 9, Lemmas 2.1--2.3 of
  `https://cdn.openai.com/pdf/ten-proofs-oai.pdf`;
* `MATH_ASSESSMENT_SATURATED_ENDPOINT_MATRICES_MEDIAN_EXPANDER_AND_PROTECTED_RESET_GATE_20260801.md`;
* `MATH_THEOREM_D2_SUPPORT4_ROLE_CONVERTER_AND_PROTECTED_PROJECTIONS_20260801.md`;
* `MATH_THEOREM_H3_NONLEXICAL_PROTECTED_RADO_FOREST_AND_TRANSPARENT_CONNECTOR_GATE_20260801.md`;
* `MATH_THEOREM_L_ROLLING_RESET_THREE_RETURN_STRICT_GAMMOID_OBSTRUCTION_AND_PRIVATE_SINK_GATE_20260801.md`.

No computation is used.
