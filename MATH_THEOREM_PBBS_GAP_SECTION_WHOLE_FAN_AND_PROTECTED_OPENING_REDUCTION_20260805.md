# The PBBS gap section contains a whole fan for every lower target

**Date:** 2026-08-05  
**Method:** pure cyclic-parenthesis mathematics; no computation or search  
**Status:** unconditional.  This strengthens the fixed gap-section theorem
from a root-occurrence statement to a whole-path statement.  It then gives
an exact protected-edge reduction of the upper occurrence-transport and
quiet-opening problem.  It does not prove the remaining protected
Hamiltonization/puncture theorem.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad
 g=f^2:{[n]\choose m}\longrightarrow {[n]\choose m},
\]

and let `mathcal S` be the one-occurrence q1 section selected by the
gap-potential rule of
`MATH_THEOREM_PBBS_GAP_POTENTIAL_SECTION_ALL_DEPTH_LOWER_COMPLETE_20260805.md`.

The earlier theorem proves that, for every strict lower target `S`, the
first edge of one correct PBBS corridor for `S` belongs to `mathcal S`.
The main theorem below proves the stronger fact

\[
 \boxed{
 \text{every edge of that same corridor belongs to }\mathcal S.}
 \tag{0.1}
\]

Consequently one fixed protected edge set simultaneously contains:

1. a correct intersection path for every strict lower target; and
2. after complementing the owners, a correct union path for every proper
   upper target.

Therefore any spanning two-factor or Hamilton rethread which retains every
edge of `mathcal S` retains the complete named lower and upper occurrence
banks automatically.  There is no separate exterior-overhang transport
problem on that restricted rethreading face.

The all-unit PBBS component is disjoint from `mathcal S`.  Its already
proved `m-1`-vertex quiet path can consequently be protected together with
`mathcal S`.  The exact remaining opening theorem is reduced to a
protected-section Hamiltonization, or to a controlled puncture-and-repair
of the wholly selected components of `mathcal S`.

## 1. The global corridor

Fix `1<=q<=m` and

\[
                         S\in{[n]\choose m-q}.
\]

Use the global-maximum corridor boundary in the expanded unmatched-mark
word of `S`.  Write the reverse marks forward as

\[
 C_0,C_1,\ldots,C_{2q},
\]

and the forward marks backward as

\[
 A_0,A_1,\ldots,A_{2q}.
\]

The corridor inequalities are

\[
 x_j\le j,
 \qquad
 y_j\le j,
 \tag{1.1}
\]

where `x_j` counts forward marks strictly between `C_0,C_j`, and `y_j`
counts reverse marks crossed on moving backward from `A_0` to `A_j`.
The correct corridor is

\[
 B_t=S+\{C_0,\ldots,C_{q-t-1}\}
        +\{A_0,\ldots,A_{t-1}\},
 \qquad 0\le t\le q.
 \tag{1.2}
\]

For `0<=t<q`, put

\[
 r=q-t-1
\]

and let

\[
 K_t=S+\{C_0,\ldots,C_{r-1}\}
          +\{A_0,\ldots,A_{t-1}\}.
 \tag{1.3}
\]

The all-depth corridor calculation already proves

\[
 U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\},
 \qquad
 U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\},
 \tag{1.4}
\]

and

\[
 g(K_t+C_r)=K_t+A_t.
 \tag{1.5}
\]

Thus (1.5) is precisely the corridor edge `B_t B_(t+1)`.  What was not
previously recorded is that the fixed gap-potential rule selects this edge
for every `t`, not only for `t=0`.

## 2. Every corridor edge is selected

### Lemma 2.1 (induced three-by-three order)

In the expanded deficit-three word of `K_t`:

1. `A_t` is the last retained forward mark before `C_r`;
2. no retained forward mark lies strictly between `C_r` and `C_(r+1)`;
3. at most one retained forward mark lies strictly between `C_(r+1)` and
   `C_(r+2)`.

For `q>=3`, the last bound improves to zero.

#### Proof

The survivor identities are (1.4), including literal cyclic order after
matched marks are contracted.  The proof of the all-depth corridor theorem
also shows that `C_r` lies after the removed forward block and before the
first surviving forward mark in cyclic predecessor order.  Its strict
predecessor among the three marks in `U_+(K_t)` is therefore `A_t`.  This
proves item 1.

For the forward gaps, use the reverse corridor inequality.  Moving backward
from `A_0` to `A_h` crosses at most `h` reverse marks.  Hence `A_h` lies in
one of the last `h+1` reverse-mark gaps before `C_0`; in forward indexing it
does not occur before the gap following

\[
                         C_{2q-h}.
 \tag{2.1}
\]

The earliest of the three surviving marks is therefore controlled by
`h=t+2`.  Since

\[
 2q-(t+2)-(r+2)=q-3,
 \qquad r=q-t-1,
 \tag{2.2}
\]

for `q>=3` all three retained forward marks occur at or after
`C_(r+2)` in the cyclic arc ending at `C_0`.  At a shared coordinate the
expanded order is `C,A`, so equality still places the `A` after
`C_(r+2)`, not in the preceding open gap.  Thus both first gaps contain no
retained `A`.

For `q=2`, there are two cases.  At `t=1`, the surviving reverse marks are
`C_0,C_1,C_2`.  The bounds `y_1<=1,y_2<=2,y_3<=3` place no retained `A`
in the first gap and at most `A_3` in the second.  At `t=0`, the already
audited entrance restriction gives the same conclusion.  The case `q=1`
has only the defining q1 edge.  This proves all assertions. `square`

### Theorem 2.2 (whole-fan section theorem)

Every edge

\[
                         B_t\longrightarrow B_{t+1}
 \qquad(0\le t<q)
\]

of (1.2) is the occurrence chosen by the one fixed gap-potential section
`mathcal S`.

#### Proof

In the induced deficit-three word, index the three surviving reverse marks
from `C_r`.  Let `z_0,z_1,z_2` be the numbers of retained forward marks in
the three successive open gaps.  Lemma 2.1 gives

\[
                         z_0=0,
 \qquad
                         z_0+z_1\le1.
 \tag{2.3}
\]

Normalize the gap potential to zero at `C_r`.  Its values at the other two
reverse marks are

\[
                         z_0-1=-1,
 \qquad
                         z_0+z_1-2\le-1.
 \tag{2.4}
\]

Thus `C_r` is the unique maximum.  Lemma 2.1(1) identifies the last
forward mark before it as `A_t`.  The fixed rule consequently selects

\[
                         K_t+C_r\longrightarrow K_t+A_t,
\]

which is the declared corridor edge by (1.5). `square`

### Corollary 2.3 (selected-edge lower bank)

For every strict lower target `S`, one complete correct PBBS intersection
path witnessing `S` is contained in `mathcal S`.

The choice is simultaneous: `mathcal S` was fixed once from the q1 cores,
and the target `S` is used only to identify one path already contained in
that fixed subgraph.

## 3. Complementary upper bank

Complement every middle owner.  For the path (1.2),

\[
 \bigcup_{t=0}^{q}\overline{B_t}
   =[n]\setminus\bigcap_{t=0}^{q}B_t
   =[n]\setminus S.
 \tag{3.1}
\]

### Corollary 3.1 (one protected edge set carries both banks)

On the upper-middle complement orientation, every proper upper target has
a correct owner-interval witness all of whose internal Johnson edges lie
in `mathcal S`.

The full-ground target is supplied by the complete opened owner path and
does not require a protected proper interval.

## 4. Exact cut-avoidance criterion after a rethread

Let `F'` be any spanning two-factor on the same owner vertex set.  Assume

\[
                         \mathcal S\subseteq E(F').
 \tag{4.1}
\]

Every path in Corollary 2.3 remains consecutive in `F'`: at each internal
vertex its two incident path edges already consume the full degree two.
Hence its intersection and the complementary union (3.1) are unchanged.

### Theorem 4.1 (protected-section transport)

Under (4.1), `F'` contains:

1. every strict-lower target in a named occurrence;
2. every proper upper target in the complementary named occurrence; and
3. the complete middle owner set.

Thus, on this face, arbitrary-width upper occurrence transport is reduced
exactly to retaining the q1 section edge set.  No packetwise exterior
upper-monotonicity theorem is needed.

#### Proof

Choose the paths from Corollary 2.3.  Condition (4.1) retains every edge
of each path.  A degree-two factor cannot insert another edge between two
successive retained path edges, so every path remains a literal consecutive
owner interval.  Its intersection remains `S`, and (3.1) retains the
complementary upper target.  Spanning gives the owner row. `square`

There is an equivalent forbidden-cut formulation which does not fix the
section.  If `D` is the set of old factor edges deleted by a rethread and
`mathcal W(Y)` is the complete old occurrence family of an upper target,
then an old witness of `Y` survives exactly when

\[
 \boxed{
 \exists I\in\mathcal W(Y)\quad E(I)\cap D=\varnothing.}
 \tag{4.2}
\]

Equivalently, `D` is not a transversal of `mathcal W(Y)`.  Upper witnesses
have no cross-target capacity coupling: distinct target values cannot be
the value of the same exact-rank interval cell.  Thus (4.2) is targetwise,
not an additional Hall matching.  The stronger protected-section condition
`D cap mathcal S=emptyset` satisfies (4.2) simultaneously by Corollary 3.1.

## 5. The all-unit component is bank-free

Let `Q` be the rectangular all-unit PBBS component with rooted shape
`(10)^m`.  The exact mark calculation in the source-opening theorem proves

\[
                         E(Q)\cap\mathcal S=\varnothing.
 \tag{5.1}
\]

Because every path selected in Corollary 2.3 begins with an edge in
`mathcal S` and stays inside the PBBS component containing that edge, no
selected lower path or complementary upper path meets `Q` at all.

### Corollary 5.1 (literal quiet-tail reserve)

The complete all-unit component is disjoint from both named occurrence
banks.  Any `m-1` consecutive owner starts on it may be retained as a
terminal quiet path without consuming or cutting a named lower or upper
witness.

This is stronger than the scalar count `W-N_1>=m`: the required quiet
starts already occur consecutively in one canonical component, and the
entire component is occurrence-bank-free.

## 6. Exact remaining topology theorem and obstruction

If there is a Hamilton cycle `H` satisfying

\[
 \mathcal S\cup P_{quiet}\subseteq E(H),
 \tag{6.1}
\]

where `P_quiet` is an `m-1`-vertex directed path in `Q`, then cutting `H`
immediately after `P_quiet` gives the zero-defect upper staircase.  Together
with the imported source factorization, residence and common-cap premises,
the standard `d`-letter unroll has length exactly `B(k)`.

Condition (6.1) cannot be asserted from an arbitrary protected two-factor
extension theorem.  A Johnson path of `m-1` vertices uses `m-2` Johnson
edges but `2m-4` containment incidences, which exceeds the generic
`m-2`-incidence protected bound.  Here the path is available only because
it is already part of the canonical PBBS factor.

There is also a genuine cycle obstruction.  If `mathcal S` contains every
edge of a proper PBBS factor component, then no Hamilton cycle can contain
all of `mathcal S`: every vertex of that selected component already has
degree two inside `mathcal S`.  The next theorem shows that this is not a
hypothetical obstruction.

### Theorem 6.1 (the single-soliton component is wholly gap-selected)

For every `m>=2`, every outgoing edge on the rectangular single-soliton
PBBS component with rooted Dyck shape

\[
                         1^m0^m
 \tag{6.2}
\]

belongs to `mathcal S`.

#### Proof

Root one state as

\[
                         A=0_r1^m0^m.
\]

The PBBS successor deletes the final up-step `p` of the mountain and
inserts `r`.  Write the original down-steps as

\[
                         v_1,v_2,\ldots,v_m
\]

in forward order and put `K=A-{p}`.  Forward cancellation in

\[
                         K=0_r1^{m-1}0_p0_{v_1}\cdots0_{v_m}
\]

leaves

\[
                         U_+(K)=\{r,v_{m-1},v_m\}.
 \tag{6.3}
\]

Reverse cancellation pairs the `m-1` ones with the last `m-1` zeros in
the cyclic block preceding them, and leaves

\[
                         U_-(K)=\{p,v_1,v_2\}.
 \tag{6.4}
\]

For `m>=3`, the three forward-mark counts in the open gaps beginning at
`C_p,C_(v_1),C_(v_2)` are

\[
                         (0,0,3).
 \tag{6.5}
\]

For `m=2`, the shared-coordinate order `C,A` changes this to

\[
                         (0,1,2).
 \tag{6.6}
\]

In both cases the gap-potential values away from `C_p` are strictly
negative after normalizing the value at `C_p` to zero.  Thus `C_p` is the
unique maximum.  The last forward mark before it is `A_r`, so the fixed
section selects

\[
                         K+p\longrightarrow K+r,
\]

the outgoing component edge.  The rooted single-soliton evolution fixes
the shape (6.2) and only rotates the physical root.  The calculation is
therefore valid at every edge of the component. `square`

### Corollary 6.2 (unselected-native-C6 isolation)

Let `mathcal H_0` be the component hypergraph whose hyperedges are native
clean PBBS C6 switches with all three old edges in

\[
                         E(F)\setminus\mathcal S
\]

and on three distinct PBBS components.  The single-soliton component is an
isolated vertex of `mathcal H_0`.

In fact no serial rethread which deletes only old unselected section edges
can ever change or merge that component: the first move touching it would
have to delete one of its edges, and every such edge lies in `mathcal S`.

Thus the native unselected-edge C6 hypergraph cannot span the PBBS
components.  Protected-section Hamiltonization in the literal form (6.1)
is impossible.

The remaining theorem must puncture at least one selected edge in every
wholly selected component, beginning already with the single-soliton
component, and reroute every corridor using a punctured edge.  The
whole-fan theorem removes arbitrary exterior upper transport from that
problem: only the punctured selected paths themselves require replacement.

## 7. Scope

Proved here:

1. every edge of every canonical global corridor is selected by one fixed
   q1 gap section;
2. one protected edge set carries the complete lower and complementary
   upper occurrence banks;
3. retaining that edge set in a rethread retains all those witnesses;
4. the exact targetwise forbidden-cut criterion (4.2); and
5. complete occurrence-bank freedom of the all-unit quiet component.
6. a wholly selected single-soliton obstruction, which makes the
   unselected-native-C6 component hypergraph nonspanning.

Not proved here:

1. a Hamilton cycle containing the complete section;
2. absence or repair of wholly selected gap-section components;
3. source/residence compatibility of a repaired global rethread;
4. terminal common-cap compatibility; or
5. the unconditional exact formula `nu(k)=B(k)`.
