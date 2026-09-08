# Active cycle-aligned wedge linkage and layer-energy selection

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional joint selection theorem for one fixed
selection-stable active-wedge state.  It chooses active wedges, forces them
into the sequential Boolean linkage cycles, and materializes their exact q1
occurrences in one protected Middle-Levels factor.  Typed activity itself
and regenerative owner-area control remain premises.

## 0. Main theorem

Fix `m>=3` and distinct lower turns

\[
 L_1,\ldots,L_p\in{[2m-1]\choose m-1},
 \qquad
 1\le p\le\left\lfloor{m+1\over4}\right\rfloor.
\tag{0.1}
\]

For each `i`, let `A_i` be a menu of active full wedges at `L_i` in one
fixed, selection-stable cap/guard/phase state.  Every member carries a
distinguished active owner side.  Its certificate says that, if the wedge
is protected and extended to a compatible factor, that Boolean
source--owner--q1 path is a surviving typed legal route independently of
the unprotected part and orientation of the completed factor.  For every
owner/terminal-distinct selected bank, all certified paths coexist: their
nonendpoint resources are private, or their conflicts have already been
removed from the menus.

Put

\[
 B_q(m)={m\choose2}-{m-q\choose2}.
\tag{0.2}
\]

### Theorem 0.1

If

\[
 \boxed{
 |A_i|>B_{p-1}(m)+2(p-1)
 \qquad(1\le i\le p),
 }
\tag{0.3}
\]

then one can construct simultaneously:

1. a Boolean full-port injection

   \[
   \phi:\bigcup_iP_i\longrightarrow{[2m-1]\choose m+1},
   \qquad U\subset\phi(U),
   \tag{0.4}
   \]

   where `P_i` is the complete rank-`m` owner star of `L_i`;
2. an active wedge `w_i=(L_i;{a_i,b_i}) in A_i` for every source;
3. globally distinct selected owner values
   `U_i=L_i+a_i,U_i'=L_i+b_i` and globally distinct selected terminals
   `Z_i=L_i+a_i+b_i`; and
4. the exact correlation

   \[
                         \boxed{\phi(U_i)=Z_i.}
   \tag{0.5}
   \]

If an incumbent protected bank `P_*` is degree-compatible with the selected
wedge bank and

\[
                         |P_*|+2p\le m-2,
\tag{0.6}
\]

the selected wedges extend to a spanning Middle-Levels two-factor.  In its
serialized occurrence complex, every selected `Z_i` is exactly the q1 turn
occurrence on the active branch `L_i -> U_i -> Z_i`.  These branches are
pairwise private.

## 1. Earlier assignment and old-owner exclusions

Process the sources sequentially.  Suppose stages `<i` have already built
their Hamilton cycles and extended the injective assignment `phi` as in the
bounded-turn full-port theorem.

Let `E_i` be the set of edges in the current terminal graph `K_(C_i)` whose
terminal values were assigned at earlier stages.  The assigned terminal
set from any earlier source is a subset of one Hamilton cycle.  The exact
terminal-cloud overlap lemma therefore gives

\[
                         |E_i|\le2(i-1).
\tag{1.1}
\]

Let `F_i` be the set of current extension coordinates whose owner values
already occur in an earlier complete owner star.  Pairwise owner-star
intersection at most one gives

\[
                         |F_i|\le i-1.
\tag{1.2}
\]

The union of all wedge edges incident with `F_i` has size at most

\[
 B_{i-1}(m)\le B_{p-1}(m).
\tag{1.3}
\]

Consequently (0.3) leaves an active edge

\[
                         e_i={a_i,b_i}\in A_i
\tag{1.4}
\]

which is neither incident with `F_i` nor a member of `E_i`: the combined
forbidden union has size at most

\[
 B_{i-1}(m)+2(i-1)
 \le B_{p-1}(m)+2(p-1).
\tag{1.5}
\]

Thus both selected owner endpoints are new relative to every earlier star,
and the selected terminal has not been assigned earlier.  Name the wedge's
distinguished certified side `a_i` and name the other endpoint `b_i`.
This ordered labelling is fixed before the Hamilton cycle is chosen.

## 2. Force the active edge into the linkage cycle

Delete `E_i` from `K_(C_i)` and call the residual graph `G_i`.  Equation
(1.1) gives

\[
 \delta(G_i)\ge m-1-2(i-1)=m-2i+1.
\tag{2.1}
\]

The range (0.1) implies

\[
                         \delta(G_i)\ge{m+1\over2}.
\tag{2.2}
\]

Ore's Hamilton-connected theorem says that a graph on `m` vertices with
minimum degree at least `(m+1)/2` has a Hamilton path between every ordered
pair of distinct vertices.  Apply it to `a_i,b_i`.  Adding the edge `e_i`,
which lies in `G_i` by construction, closes that Hamilton path into a
Hamilton cycle `H_i` containing `e_i`.

Orient `H_i` so that

\[
                         a_i\longrightarrow b_i.
\tag{2.3}
\]

For every owner coordinate new at stage `i`, assign its outgoing cycle-edge
terminal, exactly as in the bounded-turn full-port theorem.  Old owners keep
their previous assignments.

Because `a_i` is new and (2.3) is its outgoing edge,

\[
 \phi(L_i+a_i)=L_i+a_i+b_i=Z_i.
\tag{2.4}
\]

The cycle avoids all earlier assigned terminals, so the global assignment
remains injective.  Its newly assigned terminal set is a subset of `H_i`,
preserving the induction invariant needed for (1.1) at every later stage.

## 3. Distinctness and factor materialization

Both endpoints of `e_i` avoid `F_i`, so their owner values lie outside the
entire earlier star union.  Induction gives global distinctness of all
selected owner values.  Equation (2.4) and injectivity of `phi` give global
distinctness of all selected `Z_i`.

Protect both incidences of every selected wedge.  Their union has lower
degree two and upper degree one.  Under (0.6) and degree compatibility, the
small protected-factor theorem supplies a spanning two-factor containing
them.

At `L_i`, the two protected incidences exhaust factor degree two.  The
factor q1 turn value is therefore

\[
 (L_i+a_i)\cup(L_i+b_i)=Z_i.
\tag{3.1}
\]

The protected occurrence lift and canonical turn diamond materialize the
path

\[
                         L_i\longrightarrow U_i\longrightarrow Z_i.
\tag{3.2}
\]

It is active by the definition of `A_i`.  Selected turns cannot be
consecutive because consecutive turns share an owner while all selected
owners are distinct.  Thus the selected active paths are pairwise private.
This proves Theorem 0.1.

## 4. Layer-energy form

Suppose the inactive wedges at source `i` are covered by

\[
 {R_i\choose2}\cup S_i\cup H_i,
\tag{4.1}
\]

where `R_i` is a set of inactive owner sides, `S_i` is a set of unavailable
q1 terminal pairs, and `H_i` is the explicitly priced hidden-hole bank.
Put

\[
 r_i=|R_i|,
 \qquad t_i=|S_i|+|H_i|,
 \qquad I=\sum_i r_i,
 \qquad J=\sum_i t_i.
\tag{4.2}
\]

The menu row (0.3) follows whenever

\[
 {r_i\choose2}+t_i<T_*:=
 {m-p+1\choose2}-2(p-1).
\tag{4.3}
\]

For an integer `R` with

\[
 S_R^*:=T_*-{R-1\choose2}>0,
\]

all but at most

\[
 \boxed{
 \left\lfloor{I\over R}\right\rfloor+
 \left\lfloor{J\over S_R^*}\right\rfloor
 }
\tag{4.4}
\]

sources satisfy (4.3).  This is the same owner-heavy/terminal-heavy split:
a failing source with `r_i<R` has `t_i>=S_R^*`.

After deleting the exceptional sources, reindex the retained family.  Its
required threshold is no larger than the original right side of (0.3), so
Theorem 0.1 applies.

### Corollary 4.1

For fixed constants `A,D,C`, if

\[
 p\le C\sqrt m,
 \qquad I\le Am,
 \qquad J\le Dm^2,
\tag{4.5}
\]

then for all sufficiently large `m`, all but at most

\[
                         \boxed{\lfloor2A\rfloor+\lfloor4D\rfloor}
\tag{4.6}
\]

sources admit the complete active-linkage-factor materialization.

#### Proof

Take `R=floor(m/2)+1`.  Since `p=O(sqrt(m))`, eventually

\[
 S_R^*
 ={m-p+1\choose2}-2(p-1)-{\lfloor m/2\rfloor\choose2}
 \ge {m^2\over4}.
\]

Substitute (4.5) into (4.4).  The retained source count still satisfies the
Hamilton-connected range and the protected-factor edge row must be checked
with that retained count.  \(\square\)

## 5. Interface with regenerative owner area

Let a frozen background have distinct rank-`m` owner projection of size
`f` and terminal-only exception bank of size `e`.  The nonmonotone
owner-area theorem gives

\[
                         g\le(m-1)f+e
\tag{5.1}
\]

for its ordinary q1-terminal projection.  The audited two-layer incidence
bounds convert

\[
 f=O(m),\qquad e+\sum_i|H_i|=O(m^2),qquad p=O(\sqrt m)
\tag{5.2}
\]

into the energy row (4.5).  Thus Regenerative Owner Area plus
selection-stable activity gives bounded active-linkage-factor casualties;
no per-path monotonicity is required.

The remaining premise is exactly that the common Pascal/common-cap child
exports (5.2), one fixed typed/phase state, private nonendpoint resources,
and a fresh nonaccumulating successor state.

## 6. Exact scope

The theorem proves a joint quantifier order:

\[
 \text{active wedge}
 \longrightarrow
 \text{Hamilton cycle containing it}
 \longrightarrow
 \text{Boolean linkage assignment}
 \longrightarrow
 \text{factor q1 occurrence}.
\]

It does not prove the selection-stable activity menus, their type/phase
legality, the owner-area bound, terminal-only/hidden pricing, two-coordinate
product closure, or nonaccumulating regeneration.

## 7. Dependencies

- `MATH_THEOREM_BOUNDED_TURN_STARS_ONE_STEP_FULL_PORT_LINKAGE_20260804.md`
- `MATH_THEOREM_CYCLE_ALIGNED_WEDGE_LINKAGE_FACTOR_MATERIALIZATION_20260804.md`
- `MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md`
- `MATH_THEOREM_AUTOMATIC_PROTECTED_TURN_LIFT_AND_REGENERATIVE_OWNER_AREA_20260804.md`
- Ore's Hamilton-connected theorem
