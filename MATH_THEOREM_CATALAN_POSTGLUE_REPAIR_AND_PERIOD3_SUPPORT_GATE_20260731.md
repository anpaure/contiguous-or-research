# Post-glue repair is exactly the decorated-Hamilton gate

Date: 2026-07-31  
Status: exact all-dimension reduction; exact period-three support/forced-Hall
criterion; exact `m=5` incompatibility with the frozen complement-paired
filter bank; no all-dimension decorated Hamilton cycle is claimed

## 0. Verdict

**Later sharpening.**  The Hamilton endpoint below is sufficient but not
minimal.  `MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`
proves that a globally palette-exact, componentwise alternating decorated
spanning 2-factor already gives the Catalan path forest when every marked
component has at least one unmarked occurrence and is off the binary cycle
face.  (A wholly marked component contributes two rail cycles.)  The same alternating-circuit proof
connects any starting 2-factor to such a terminal factor.  Read every
“weakest” claim below with this sharpening; the Hamilton statements remain
correct sufficient statements.

There is a useful quantifier change in the Catalan linear-matching route.
First use any component-spanning Middle Levels gluing family, without trying
to preserve a decoration through the glues.  Only after one Hamilton cycle
has been obtained, rethread it by alternating circuits to a Hamilton cycle
which has a joint alternating turn SDR.

On this order the phrase **repair packet** introduces no new existential
gate:

\[
 \boxed{\text{a post-glue alternating repair exists}
 \iff \text{a decorated Hamilton cycle exists}.}       \tag{0.1}
\]

The implication is exact because the symmetric difference of any two
2-factors decomposes into alternating circuits.  Intermediate states need
only be 2-factors; they need not be Hamiltonian or decorated.  Consequently
no repair-disjoint ECO bank, common owner matching, or occurrence router is
part of the minimal post-glue state.  Those data are required only by the
strictly stronger repair-*first* transparent-gluing architecture.

The symmetry-broken period-three filters still give useful forced turn
data, but they do not themselves give the repair circuits.  Their exact
Middle Levels support is a vertex-disjoint union of prescribed length-two
paths.  They are usable precisely when:

1. one Hamilton cycle contains those paths; and
2. the forced turn centres extend through the residual gap--Hall matching.

Both rows are written below as finite, auditable conditions.  The known
repaired `m=5` Hamilton cycle is decorable, but supports **none** of the
complete complement-paired filter banks from the explicit nonsymmetric
construction.  Thus “construct filters, then repair the old cycle” is
strictly stronger than the live existential target.  One should choose the
terminal Hamilton cycle and its decoration jointly, or read exceptional
filters from the final matching.

## 1. Alternating-circuit universality

Let (G=(V,E)) be any graph and let (F,F'\subseteq E) be 2-factors on
the same vertex set.  Colour the edges of (F\setminus F') red and those
of (F'\setminus F) blue.

### Theorem 1.1 (2-factor difference theorem)

The coloured graph (F\mathbin\triangle F') has an edge-disjoint
decomposition

\[
                 Z_1\mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup} Z_t             \tag{1.1}
\]

into closed alternating circuits.  Toggling them successively gives

\[
 F_i=F\mathbin\triangle Z_1\mathbin\triangle\cdots
                  \mathbin\triangle Z_i,
 \qquad 0\le i\le t,                                  \tag{1.2}
\]

and every (F_i) is a 2-factor, with (F_t=F').  Every unprocessed
(Z_j) is still alternating with the current (F_i).

#### Proof

At every vertex, the red degree equals the blue degree: both are the number
of incident edges used by exactly one of the two degree-two factors.  Pair
the red and blue half-edges arbitrarily at each vertex.  Following these
pairings decomposes all coloured edges into closed trails which alternate
red and blue.  Splitting at repeated transition states gives the
edge-disjoint alternating circuits (1.1).

On one circuit every incident vertex loses one red edge and gains one blue
edge, so its degree remains two.  The circuits are edge-disjoint.  Hence a
red edge of an unprocessed circuit has not yet been removed and a blue edge
of that circuit has not yet been inserted.  It remains alternating after
every earlier toggle.  After all toggles, precisely the red edges have been
deleted and the blue edges inserted, giving (F'). \(\square\)

Connectivity of the intermediate (F_i)'s is neither asserted nor needed.
Demanding every prefix to be Hamiltonian is an optional stronger routing
condition, not part of the existence theorem.

### Corollary 1.2 (post-glue repair equivalence)

Fix any Hamilton cycle (C_0) of ({\rm ML}(2m-1)).  The following are
equivalent.

1. Some Hamilton cycle (C_*) of ({\rm ML}(2m-1)) has a Catalan
   decoration whose physical diamond lift is a linear forest.
2. A finite alternating-circuit packet transforms (C_0) through
   2-factors into such a terminal Hamilton cycle.

The implication `1 -> 2` is Theorem 1.1 with (F=C_0,F'=C_*); the reverse
implication reads the terminal state.  The same equivalence holds with the
stronger terminal requirement that the decoration be leaf-peelable.

Thus the minimal terminal certificate is only:

* one Hamilton cycle (C_*);
* one upper-turn transversal (I);
* a perfect matching of its gap--lower-colour graph; and
* the exact binary-trace forest alternative.

Requiring the gap graph itself to be a forest makes the matching unique and
leaf-peelable, but is stronger than existence of the Catalan linear matching.

## 2. A useful labelled switch digraph

Although Theorem 1.1 removes circuit realization as a separate existential
problem, one restricted normal form is useful for finite searches and for
diagnosing why static defect Hall may fail.

Let (F) be a 2-factor in the bipartite Middle Levels graph with lower rail
(P=\binom{\Omega}{m-1}) and upper rail
(Q=\binom{\Omega}{m}).  Orient a factor edge as
(e=(p_e,q_e)), (p_e\in P,q_e\in Q).  Let

* (\alpha(e)) be the other (P)-neighbour of (q_e) in (F); and
* (\beta(e)) be the other (Q)-neighbour of (p_e) in (F).

Make a directed graph (S_F) on the factor edges, with

\[
 e\longrightarrow f
 \quad\Longleftrightarrow\quad p_f\subset q_e
 \text{ and }p_fq_e\notin F.                         \tag{2.1}
\]

Label the arc by its two simultaneous turn gains

\[
 \lambda(e,f)=
 \bigl(p_f\cap\alpha(e),\ q_e\cup\beta(f)\bigr),     \tag{2.2}
\]

and label a vertex by its two old turn colours

\[
 \lambda_0(e)=
 \bigl(p_e\cap\alpha(e),\ q_e\cup\beta(e)\bigr).    \tag{2.3}
\]

### Theorem 2.1 (switch-digraph normal form)

An admissible directed cycle

\[
                e_0\to e_1\to\cdots\to e_{s-1}\to e_0 \tag{2.4}
\]

whose factor edges have pairwise disjoint physical endpoints is exactly the
alternating circuit which deletes (p_{e_i}q_{e_i}) and inserts
(q_{e_i}p_{e_{i+1}}).  Its signed lower/upper turn derivative is

\[
       \sum_i {\bf1}_{\lambda(e_i,e_{i+1})}
       -\sum_i {\bf1}_{\lambda_0(e_i)}.               \tag{2.5}
\]

Conversely every simple alternating circuit which changes at most one
factor edge at each physical vertex gives (2.4).

#### Proof

Containment in (2.1) makes every inserted edge a Middle Levels edge.  At
the upper endpoint (q_{e_i}), its unchanged factor neighbour is
(\alpha(e_i)), so the new lower turn colour is the first coordinate of
(2.2).  At the lower endpoint (p_{e_{i+1}}), its unchanged factor
neighbour is (\beta(e_{i+1})), so the new upper turn colour is the second
coordinate.  The deleted edge had the two colours (2.3).  Disjoint physical
endpoints make the displayed old and new edges a simple alternating circuit.
Reading any such circuit after contracting its deleted factor edges gives
the directed cycle in reverse. \(\square\)

Selecting pairwise compatible directed cycles is therefore a 0--1
circulation with colour-cover rows.  Static lower-defect versus upper-defect
Hall is only the projection which forgets flow conservation.  In
particular, a required gain arc which lies on no directed cycle can pass the
static defect-pair table and still be physically unusable.  This is the
first exact circuit-closure obstruction.

## 3. The nonsymmetric period-three filters force disjoint `P3`s

Now put

\[
 q=2m-1=3(2a+1),\qquad \Omega=\mathbb Z_q,
 \qquad \widehat\Omega=\Omega\sqcup\{\infty\}.
\]

Let (K_3) be the order-three subgroup, let
(\pi:\mathbb Z_q\to\mathbb Z_{2a+1}), and for every (a)-set (A)
put

\[
 T_A=\pi^{-1}(A),\qquad
 B=\mathbb Z_{2a+1}\setminus A.                       \tag{3.1}
\]

Choose distinct quotient points (b_A,c_A\in B) and representatives
(x_A\in\pi^{-1}(b_A)), (y_A\in\pi^{-1}(c_A)).  The two diamonds of the
nonsymmetric filter theorem have the following forced support in
({\rm ML}(q)):

\[
 \begin{aligned}
 P_A^-:
 &\quad T_A+x_A
   \;--\;T_A+x_A+y_A
   \;--\;T_A+y_A,\\
 P_A^+:
 &\quad U_B-x_A
   \;--\;U_B-x_A-y_A
   \;--\;U_B-y_A,
 \end{aligned}                                         \tag{3.2}
\]

where (U_B=\pi^{-1}(B)).  The first path has its centre on the upper rail;
the second has its centre on the lower rail.

### Lemma 3.1 (private forced support)

All vertices in all paths (3.2) are distinct.  Hence

\[
                    \Theta_{\rm per3}
       =\mathop{\dot\bigcup}_A(P_A^-\mathbin{\dot\cup}P_A^+)      \tag{3.3}
\]

is a linear forest of (2\binom{2a+1}{a}) vertex-disjoint `P3`s.

#### Proof

The six vertex types are recovered by their (K_3)-coset occupancies:

\[
\begin{array}{c|c}
\text{type}&\text{finite occupancy}\ \hline
\text{endpoint of }P_A^-&3^a1^1\\
\text{centre of }P_A^-&3^a1^2\\
\text{endpoint of }P_A^+&3^a2^1\\
\text{centre of }P_A^+&3^{a-1}2^2
\end{array}                                            \tag{3.4}
\]

with the evident direct interpretation when (a=0).  Within each type,
the full cosets recover (A) or (B), and the partial cosets recover the
chosen representatives.  The rail rank and the distinct occupancy patterns
separate the four rows.  Thus no two vertices collide. \(\square\)

This strengthens the endpoint-only injectivity of the filter theorem: the
previously implicit Middle Levels centres are private too.

## 4. Exact support and forced-decoration gate

Let (R=E(\Theta_{\rm per3})), and put
(G={\rm ML}(q)).  A Hamilton cycle containing all forced filter turns is
exactly a solution of the following finite 0--1 system on
(E(G)\setminus R):

\[
 \sum_{e\ni v}x_e=2-\deg_R(v)\qquad(v\in V(G)),        \tag{4.1}
\]

\[
 |R\cap\delta(S)|+\sum_{e\in\delta(S)}x_e\ge2
 \quad(\varnothing\ne S\subsetneq V(G)).              \tag{4.2}
\]

Indeed, (4.1) makes (R\cup\{e:x_e=1\}) a spanning 2-factor, and the
subtour cuts (4.2) make it connected.  Conversely every containing
Hamilton cycle satisfies them.  This is the exact Hamilton-support gate;
endpoint injectivity alone does not imply it.

Suppose (C) passes (4.1)--(4.2).  The centres of the (P_A^+) paths are
forced upper-turn marks and the centres of the (P_A^-) paths are forced
lower-turn marks.  Call their index sets (P_A,P_B), respectively.  The
explicit filters extend to a Catalan decoration supported by (C) if and
only if:

1. there is an upper-turn transversal (I\supseteq P_A);
2. every cyclic (I)-gap contains at most one point of (P_B); and
3. after deleting those forced gaps and their forced lower colours, the
   residual gap--lower-colour graph has a perfect matching.              \tag{4.3}

This is the forced-port gap--Hall theorem applied to the private paths
(3.2).  Distinctness of the forced colours is already supplied by the
filter construction.  If the completed gap graph is a forest, the matching
is unique and the output is leaf-peelable.  The binary trace must separately
avoid the unique cycle face to obtain a Catalan linear forest.

Equations (4.1)--(4.3) are the promised exact finite-dimensional condition.
They reconcile the symmetry-broken filters with actual alternating-circuit
repair: first choose a terminal Hamilton cycle and decoration containing
their forced support; Theorem 1.1 then supplies the repair circuits from
any already-glued Hamilton cycle.

## 5. First literal obstruction at the repaired `m=5` target

The explicit complement-paired filter family must not be mistaken for the
filters selected by the known repaired `m=5` decoration.

Take the authenticated repaired Hamilton cycle obtained from the standard
transparent `m=5` output by the three displayed `C10` toggles.  Here
(q=9,a=1).  For each of the three quotient singletons (A), exhaust all
nine choices

\[
 x_A\in\pi^{-1}(b_A),\qquad
 y_A\in\pi^{-1}(c_A),                                  \tag{5.1}
\]

where (b_A,c_A) are the two complementary quotient points.

The exact result is:

\[
\begin{array}{c|c|c}
A&\text{choices supporting both }P_A^-,P_A^+
 &\text{choices supporting exactly one shore}\\ \hline
0&\{(1,8)\}&0\\
1&\varnothing&0\\
2&\varnothing&\{(0,7),(3,1)\}.
\end{array}                                            \tag{5.2}
\]

Consequently all (9^3=729) complete complement-paired banks fail the
support condition on this Hamilton cycle.  Nevertheless that cycle has the
authenticated leaf-peelable Catalan decoration.

This is the first exact obstruction to the naive reconciliation:

\[
 \boxed{\text{a good repair endpoint need not support a preassigned
 complement-paired exceptional filter}.}              \tag{5.3}
\]

It is not a no-go to another terminal cycle satisfying (4.1)--(4.3), and
not a no-go to choosing a global diamond matching first and reading its
exceptional restrictions afterward.  It proves only that the explicit
nonsymmetric filter and the known `m=5` circuit packet are two different
certificates which cannot be identified pointwise.

## 6. Correct all-dimension target

The minimal post-glue statement is therefore:

> **Post-glue decorated-Hamilton theorem.**  For every (m\ge2), some
> Hamilton cycle of ({\rm ML}(2m-1)) admits an upper-turn transversal whose
> gap--lower-colour graph has a perfect matching, and whose mark trace is on
> the linear-forest side.

A leaf-peelable version asks the gap graph to be a forest.  Either version
is independent of the particular Hamilton cycle produced by the first
gluing stage, by Theorem 1.1.  The leaf-peelable version is a clean stronger
inductive target, not a logically necessary owner export.

This target is strictly weaker than the repair-first ECO theorem: it stores
no common product cube, no forced owners through old glues, no repair-
disjoint fixed-rotation bank, and no occurrence router.  It is also not yet
proved.  The real remaining row is the decorated Hamilton cycle itself;
alternating-circuit realization and period-three phase words are no longer
separate gates.

### 6.1 Relation to transparent gluing

The transparent-hexagon theorem remains a valid and useful **sufficient
construction route**.  It starts with a decoration on a multi-component
factor and asks every component merge to preserve that same decoration (or
a controlled finite relation of decorations).  Its palette, boundary and
leaf-forest transfer tests are exactly what that stronger invariant needs.

It is not a necessary interface for the central existence theorem.  One may
instead:

1. use the ordinary Middle Levels/ECO machinery only to obtain an arbitrary
   Hamilton cycle (C_0);
2. forget every decoration, owner and router used during that gluing; and
3. apply Theorem 1.1 to move to any accepting terminal Hamilton cycle
   (C_*).

The repaired `ML(7)` fixture is the smallest literal illustration.  One
incidence-hex toggle takes the explicit nondecorable Hamilton cycle to a
decorable one.  The fact that six Hamilton toggles admit common forest
decorations proves the transparent route is nonempty, while the one-toggle
repair itself needs only the accepting decoration at its terminal endpoint.

Consequently the smallest all-dimension theorem in this lane is:

> **Decorated Middle Levels Theorem.**  For every (m\ge2),
> ({\rm ML}(2m-1)) contains one Hamilton cycle with a Catalan decoration
> whose binary trace is on the linear-forest side.

The leaf-peelable decorated Middle Levels theorem is a stronger recursive
version.  A transparent leaf-peelable gluing tree would prove it, but is not
equivalent to it.  Conversely, Theorem 1.1 shows that the undecorated
Hamilton cycle used as the post-glue starting point is immaterial: all the
content is in existence of the accepting terminal cycle.

## 7. Audit

Run

```text
python3 scratch/audit_catalan_postglue_period3_support_20260731.py
```

The audit reconstructs the authenticated three-`C10` repaired `m=5` cycle,
enumerates all representative choices in (5.1), and checks (5.2) and the
`729`-bank no-go.  It also verifies the disjoint-support lemma for
(a=0,1,2,3).  The all-dimension proofs do not depend on the finite replay.
