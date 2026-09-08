# Cycle-aligned wedge selection materializes the Boolean linkage in one factor

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional joint selection and factor-materialization theorem.
It correlates the bounded-turn Boolean full-port linkage with protected
Middle-Levels factor completion.  For every selected lower turn, one edge
of the Hamilton cycle used by the linkage is chosen as the protected wedge.
The linked terminal is then exactly the literal q1 turn occurrence in the
completed factor.  The theorem does not prove common-cap terminal-type
acceptance, survival after a compensation deletion, or regeneration.

## 0. Setting and conclusion

Fix `m>=3`, put `n=2m-1`, and let

\[
 \mathcal L={ [n]\choose m-1},\qquad
 \mathcal U={ [n]\choose m},\qquad
 \mathcal V={ [n]\choose m+1}.
\]

Choose distinct lower turns

\[
 L_1,\ldots,L_p\in\mathcal L,
 \qquad 1\le p\le \left\lfloor{m+2\over4}\right\rfloor .
\tag{0.1}
\]

For each `i`, put

\[
 C_i=[n]\setminus L_i,
 \qquad
 P_i=\{L_i+a:a\in C_i\}.
\tag{0.2}
\]

Then one can choose, simultaneously,

1. an injection

   \[
       \phi:\bigcup_{i=1}^pP_i\longrightarrow\mathcal V,
       \qquad U\subset\phi(U),
   \tag{0.3}
   \]

2. an ordered edge `a_i -> b_i` of a Hamilton cycle on `C_i`, and hence a
   full wedge

   \[
       w_i=(L_i;\{a_i,b_i\}),
   \tag{0.4}
   \]

such that, writing

\[
 U_i=L_i+a_i,\qquad
 U_i'=L_i+b_i,\qquad
 Z_i=L_i+a_i+b_i,
\tag{0.5}
\]

all `2p` owner values `U_i,U_i'` are distinct, all `p` terminal values
`Z_i` are distinct, and

\[
                         \boxed{\phi(U_i)=Z_i.}
\tag{0.6}
\]

Consequently, if an incumbent protected incidence bank `P_*` is
degree-compatible and

\[
                         |P_*|+2p\le m-2,
\tag{0.7}
\]

all selected wedges and `P_*` extend to one spanning two-factor of
`ML_m`.  In its serialized occurrence complex, every selected claim has
the literal private branch

\[
 x_i\longrightarrow u_i\longrightarrow z_i,
 \qquad
 (L_i,U_i,Z_i),
\tag{0.8}
\]

and (0.8) is the occurrence realization of the Boolean linkage edge
`U_i -> phi(U_i)`.  The selected sources, owners, and q1 terminal
occurrences are pairwise distinct.

## 1. Recalling the sequential Hamilton-cycle linkage

Process the lower turns in the order `1,...,p`.  At stage `i`, identify the
terminal cloud over `L_i` with the edge set of the complete graph on `C_i`:

\[
 \{a,b\}\longleftrightarrow L_i+a+b.
\tag{1.1}
\]

The bounded-turn full-port linkage theorem constructs a Hamilton cycle
`H_i` in this graph after deleting every terminal value already assigned
at earlier stages.  Orient `H_i` cyclically.  If the owner `L_i+a` has not
appeared in an earlier star, assign it the outgoing edge terminal

\[
                    \phi(L_i+a)=L_i+a+b_i(a),
\tag{1.2}
\]

where `a -> b_i(a)` is the oriented edge of `H_i`.  Owners already present
retain their previous assignment.  The proof of the full-port theorem
shows that these assignments are globally injective.

The new point is that `H_i` always contains an edge whose two endpoint
owners are new.  Choosing that edge as the factor wedge makes one of the
already assigned linkage terminals equal to the q1 turn value.

## 2. At most one old owner vertex per earlier source

Define

\[
 F_i=\{a\in C_i:L_i+a\in\bigcup_{j<i}P_j\}.
\tag{2.1}
\]

### Lemma 2.1

\[
                              |F_i|\le i-1.
\tag{2.2}
\]

#### Proof

For `j<i`, the two owner stars `P_i,P_j` have at most one common owner.
Indeed, a common rank-`m` owner must contain `L_i union L_j`; since the two
lower sets have the same rank, such an owner exists only when they differ
by one exchange, and then it is uniquely `L_i union L_j`.  Thus every
earlier star contributes at most one member of `P_i`, proving (2.2).
\(\square\)

### Lemma 2.2

The Hamilton cycle `H_i` has an edge with both endpoints in
`C_i setminus F_i`.

#### Proof

A cycle on `m` vertices has exactly `m` edges.  The set of cycle edges
incident with `F_i` has size at most `2|F_i|`.  By (0.1) and (2.2),

\[
 2|F_i|\le2(i-1)\le2(p-1)<m.
\tag{2.3}
\]

The strict final inequality follows from
`p<=floor((m+2)/4)`: for `m>=3`,

\[
 2(p-1)\le {m+2\over2}-2={m-2\over2}<m.
\]

Hence not every edge of `H_i` meets `F_i`; an edge outside it has both
endpoints in `C_i setminus F_i`.  \(\square\)

## 3. Joint wedge and linkage selection

For each stage `i`, choose an edge of `H_i` supplied by Lemma 2.2.  Give it
the inherited cyclic orientation

\[
                         a_i\longrightarrow b_i
\tag{3.1}
\]

and define `U_i,U_i',Z_i` by (0.5).

### Theorem 3.1 (cycle-aligned protected wedges)

The selected wedges satisfy:

1. all `U_i,U_i'` are pairwise distinct;
2. all `Z_i` are pairwise distinct; and
3. `phi(U_i)=Z_i` for every `i`.

#### Proof

Both endpoints of the chosen edge lie outside `F_i`.  Therefore both owner
values `L_i+a_i` and `L_i+b_i` are absent from the entire earlier star
union.  Inductively, neither can equal an owner endpoint of an earlier
selected wedge.  The two endpoints at one stage are different, proving
pairwise owner distinctness.

The Hamilton cycle `H_i` was constructed after deleting every terminal
value used at an earlier linkage stage.  Thus every edge value of `H_i`, in
particular `Z_i`, is new relative to every earlier assigned terminal.  The
earlier selected `Z_j` were assigned terminals, so the `Z_i` are pairwise
distinct.

Finally `U_i=L_i+a_i` is a new owner at stage `i`.  Rule (1.2) therefore
assigns to it the outgoing cycle edge from `a_i`, which is precisely
`a_i -> b_i`.  Hence

\[
 \phi(U_i)=L_i+a_i+b_i=Z_i.
\]

\(\square\)

Notice that no assertion is needed about `phi(U_i')`.  A protected logical
claim chooses the `U_i` side of the wedge.  The second owner `U_i'` is the
other factor incidence needed to make `Z_i` a literal q1 turn occurrence.

## 4. Factor completion and occurrence materialization

Let `M` be the union of the two incidence edges of every selected wedge:

\[
 M=\bigcup_{i=1}^p
 \{L_i--U_i,\ L_i--U_i'\}.
\tag{4.1}
\]

Every selected lower vertex has degree two in `M`.  Theorem 3.1 makes all
selected upper owners distinct, so every selected upper vertex has degree
one.  Thus

\[
                         |M|=2p,\qquad\Delta(M)=2.
\tag{4.2}
\]

Assume `P_* union M` is degree-compatible.  Under (0.7), the small
protected-factor theorem extends it to a spanning two-factor `Phi` of
`ML_m`.

At `L_i`, the two protected incidences exhaust its factor degree.  They are
therefore consecutive around one factor component, and the q1 upper-turn
interval at this occurrence has value

\[
                         U_i\cup U_i'=Z_i.
\tag{4.3}
\]

The protected factor occurrence lift contains the canonical literal paths

\[
 x_i\to u_i\to z_i,
 \qquad
 x_i\to u_i'\to z_i.
\tag{4.4}
\]

Choose the first.  By (0.6), its owner-to-terminal value edge is exactly
the edge of the Boolean full-port linkage.  The selected lower values are
distinct by hypothesis, and Theorem 3.1 gives distinct owner and terminal
values.  Hence their occurrence addresses are distinct as well.  This
proves (0.8).

## 5. What this removes, and what remains

The theorem closes the following correlation:

\[
 \boxed{
 \text{Boolean owner--terminal linkage}
 +\text{protected wedge choice}
 +\text{factor occurrence materialization}
 }
\tag{5.1}
\]

for any bounded or `O(sqrt(m))` bank satisfying (0.1) and (0.7).  The
terminal selected by the Boolean linkage is no longer merely a set value
which might fail to occur in the factor; it is exactly the q1 turn
occurrence created by the protected wedge.

The theorem does **not** prove that this q1 occurrence

1. has the terminal type demanded by the folded two-coordinate common cap;
2. survives the frozen compensation/background deletion;
3. has a legal private continuation when q1 itself is not the final sink;
4. coexists with one common phase, flag, and guard state; or
5. is regenerated with bounded nonaccumulating footprint in the next
   Pascal child.

Thus the remaining cap-side statement is now accurately a
**typed-survival and regeneration theorem**, not an occurrence-existence or
raw Boolean-rank theorem.

## 6. Dependencies

* `MATH_THEOREM_BOUNDED_TURN_STARS_ONE_STEP_FULL_PORT_LINKAGE_20260804.md`;
* `MATH_THEOREM_PROTECTED_TURN_DIAMOND_WEDGE_PACKING_20260804.md`;
* `MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md`;
* `MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md`;
* `MATH_THEOREM_MIDDLE_LEVELS_TURN_DIAMOND_CAPACITY_ROUTER_20260804.md`.
