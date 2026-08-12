# Paired turn-diamond deletion and the minimal common-cap occurrence lift

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional deletion theorem for a protected bank of paired
literal alternatives, followed by its exact Middle-Levels turn-diamond
specialization.  It identifies a smaller occurrence-lift premise than a
full-port suffix gammoid.  It does not prove that the current Pascal child
supplies this lift or bounds its deletion casualties.

## 0. Main conclusion

For each logical claim \(i\), suppose there are two alternative literal
paths

\[
                         P_i^0,\qquad P_i^1.
\]

Different claims have disjoint total supports:

\[
 (V(P_i^0)\cup V(P_i^1))
 \cap
 (V(P_j^0)\cup V(P_j^1))
 =\varnothing
 \qquad(i\ne j).
\tag{0.1}
\]

Within one pair, put

\[
 C_i=V(P_i^0)\cap V(P_i^1),
 \qquad
 E_i^\epsilon=V(P_i^\epsilon)\setminus C_i.
\tag{0.2}
\]

Thus \(E_i^0,E_i^1\) are disjoint.  Fix a physical deletion bank \(F\).
Define

\[
\begin{aligned}
c_F&=
 |\{i:F\cap C_i\ne\varnothing\}|,\\
s_F&=
 |\{(i,\epsilon):
      F\cap C_i=\varnothing,\ 
      F\cap E_i^\epsilon\ne\varnothing\}|.
\end{aligned}
\tag{0.3}
\]

### Paired-deletion theorem

All but at most

\[
                         \boxed{c_F+\left\lfloor{s_F\over2}\right\rfloor}
\tag{0.4}
\]

claims retain one path, and the retained choices can be made pairwise
vertex-disjoint.

For a protected full-wedge bank in a Middle-Levels factor, the two
canonical turn branches have exactly this form:

\[
 x_i\longrightarrow u_i^0\longrightarrow z_i,
 \qquad
 x_i\longrightarrow u_i^1\longrightarrow z_i.
\tag{0.5}
\]

The common core is the source/terminal/phase-common guard bank, while the
two owner sides are exclusive.  Because protected wedge packing makes all
sources, all \(2p\) owners, and all q1 terminal values distinct, different
wedge pairs automatically satisfy (0.1) once equal values have
capacity-faithful occurrence lifts.

Consequently, a uniformly bounded common casualty count and side-hit count
give a uniformly bounded common-cap deficiency without any full-port
gammoid theorem.  If the common cores are protected from deletion, every
dead claim costs two side losses.

## 1. Exact paired-deletion lemma

### Theorem 1.1

Under (0.1)--(0.3), the exact set of claims having no surviving displayed
path is

\[
 D_F=
 \{i:F\cap C_i\ne\varnothing\}
 \ \cup\
 \{i:F\cap C_i=\varnothing,\
       F\cap E_i^0\ne\varnothing,\
       F\cap E_i^1\ne\varnothing\}.
\tag{1.1}
\]

In particular,

\[
                         |D_F|
 \le c_F+\left\lfloor{s_F\over2}\right\rfloor.
\tag{1.2}
\]

Every claim outside \(D_F\) can choose one surviving path, and all chosen
paths are pairwise vertex-disjoint.

#### Proof

If \(F\) meets \(C_i\), it meets both paths.  If it avoids \(C_i\), path
\(P_i^\epsilon\) survives precisely when \(F\) avoids
\(E_i^\epsilon\).  This proves (1.1).

Among claims whose common core survives, a dead claim contributes both
ordered side hits \((i,0)\) and \((i,1)\) to \(s_F\).  Distinct dead claims
contribute disjoint pairs, so their number is at most
\(\lfloor s_F/2\rfloor\).  This proves (1.2).

For every surviving claim choose a surviving displayed path.  Condition
(0.1) makes choices from different claims vertex-disjoint automatically.
\(\square\)

The bound is attained: delete one common-core resource in each of \(c\)
claim pairs and one side-exclusive resource on both sides of each of \(t\)
other pairs.  Then \(c_F=c\), \(s_F=2t\), and exactly \(c+t\) claims die.

## 2. Physical-resource corollaries

Suppose every physical capacity belongs to at most one paired support
\(V(P_i^0)\cup V(P_i^1)\), and within a pair every side-exclusive capacity
belongs to only one side.  Let

\[
 f_C=|F\cap\bigcup_i C_i|,
 \qquad
 f_E=|F\cap\bigcup_{i,\epsilon}E_i^\epsilon|.
\]

Then

\[
                         c_F\le f_C,\qquad s_F\le f_E,
\]

and hence

\[
                         |D_F|
 \le f_C+\left\lfloor{f_E\over2}\right\rfloor.
\tag{2.1}
\]

If all common cores are protected, \(f_C=0\), so

\[
                         |D_F|\le\left\lfloor{|F|\over2}\right\rfloor.
\tag{2.2}
\]

These resource bounds are weaker than the exact support-hit quantities in
(0.3).  A large deletion bank may miss every displayed path.

## 3. Protected Middle-Levels wedge specialization

Let \(L_1,\ldots,L_p\) be distinct lower turns, and let

\[
 w_i=(L_i;\{a_i,b_i\})
\]

be a protected wedge bank with:

* all \(2p\) owner values
  \(U_i^0=L_i+a_i,U_i^1=L_i+b_i\) distinct; and
* all q1 terminal values
  \(Z_i=L_i+a_i+b_i\) distinct.

Complete the bank to a spanning two-factor.  At the turn of \(L_i\), the
serialized occurrence complex contains the two canonical branches

\[
 P_i^0:x_i\to u_i^0\to z_i,
 \qquad
 P_i^1:x_i\to u_i^1\to z_i.
\tag{3.1}
\]

### Definition 3.1 (raw dual-branch occurrence lift)

The protected bank has a raw dual-branch occurrence lift in a fixed cap
state when:

1. every \(x_i,u_i^0,u_i^1,z_i\) is one physical unit-capacity occurrence;
2. every arc in (3.1) is present, has no unrecorded finite-capacity
   interior, and is typed legal for claim \(i\);
3. \(z_i\) is a legal typed sink, or each branch contains its complete
   private continuation to one such sink;
4. equal Boolean values use the correct physical capacity quotient;
5. the total supports of different \(i\) are disjoint; and
6. every common phase, flag, guard, or continuation resource is explicitly
   placed either in \(C_i\) or one side-exclusive set \(E_i^\epsilon\).

This is a pre-deletion statement.  It does not assert that the paths survive
the fixed compensation linkage.

### Theorem 3.2 (exact post-compensation wedge survival)

Suppose the protected wedge bank has a raw dual-branch occurrence lift and
the frozen compensation/background model deletes the physical bank \(F\).
Then all but at most

\[
                         c_F+\left\lfloor{s_F\over2}\right\rfloor
\tag{3.2}
\]

wedge claims retain pairwise vertex-disjoint typed routes.

#### Proof

Apply Theorem 1.1 to (3.1).  The distinct lower, owner, and terminal values
give cross-claim disjointness on the value-injective occurrence face; item
5 of Definition 3.1 prices every remaining hidden capacity. \(\square\)

When the only deleted route resources are selected owner occurrences, the
common casualty count is zero.  Since all \(2p\) owners are distinct, if
\(r\) selected owner occurrences are deleted then

\[
                         |D_F|\le\left\lfloor{r\over2}\right\rfloor.
\tag{3.3}
\]

If a fixed predeclared deletion bank meets the direct face only through
owner and q1-terminal values, and wedge selection avoids every such
forbidden value, then \(c_F=s_F=0\) on this direct face and every claim
survives.  Any source, flag, or hidden-capacity deletion must still be
included in (0.3).

## 4. Minimality of the occurrence-lift premise

The serialized factor theorem already supplies:

* the values and occurrence addresses \(x_i,u_i^0,u_i^1,z_i\);
* the two literal containments in (3.1);
* empty incidence-skeleton prefix interiors; and
* the exact source/owner/terminal collision ledger.

It does **not** supply:

* activation after the common cap and phase flags are fixed;
* survival after the compensation/background capacities are removed;
* acceptance of \(z_i\) as the required typed sink;
* a private continuation when \(z_i\) is not the final sink; or
* the capacity identity of equal values and hidden guards.

Definition 3.1 consists exactly of those missing physical rows.  Once it is
proved, Theorem 3.2 handles the frozen deletion without a further Hall or
gammoid argument.

The regular private-port theorem is stronger in a different direction.  It
requires private incidence prefixes and one simultaneous suffix linkage of
the selected physical port set.  It does not construct the occurrence lift
or suffix linkage.  Moreover, it treats displayed ports as simultaneous
demands, while (3.1) contains two **alternatives** sharing one source and
terminal.  Applying the regular theorem to both sides would overprice the
claim.  Applying it after selecting one surviving side is valid but adds
nothing to Theorem 1.1.

## 5. Exact common-cap cut interpretation

For a fixed protected bank, contract each surviving complete branch in
(3.1) to a claim-to-sink edge.  The residual claim graph has one or two
parallel alternatives per claim and distinct sink capacities across
claims.  Its maximum matching omits exactly \(|D_F|\) claims.

Equivalently, the factor-restricted Rado deficiency is

\[
 \delta(D,c)
 =\max_{X\subseteq[p]}
 \left(
 |X|-r_\Gamma\!\left(\bigcup_{i\in X}A_i(D)\right)
 \right)
 =|D_F|
\tag{5.1}
\]

on this exact paired direct-route face.  Thus Theorem 3.2 is not merely an
upper estimate on an unrelated model; it evaluates the fixed-bank Rado
deficiency after the deletions, provided Definition 3.1 is complete.

## 6. Sharp obstruction: one hidden common capacity

Cross-claim support disjointness in (0.1) is load-bearing.  Let one hidden
unit flag \(g\) lie on both alternatives of every claim.  Before deletion,
every individual claim has two valid branches.  Deleting the single
capacity \(g\) kills all \(p\) claims:

\[
                         |F|=1,\qquad |D_F|=p.
\]

Therefore no bound depending only on the number of deleted resources is
valid until every shared hidden resource is represented once and its
cross-claim multiplicity is controlled.  This is the exact failure mode
excluded by Definition 3.1(5)--(6).

The example also explains why marginal cap activation and separately
typed terminal lists do not prove a joint router.

## 7. Additive-constant consequence

Suppose that at every same-parity lift:

1. a protected bank of \(p=O(d)\) wedges is selected and factor-completed;
2. it has a raw dual-branch occurrence lift in one common state; and
3. the frozen deletion satisfies

   \[
   c_F+\left\lfloor{s_F\over2}\right\rfloor\le C
   \]

   for one absolute constant \(C\).

Then this one-coordinate common-cap row contributes at most \(C\) terminal
casualties, independently of \(m\).  If the rest of the regenerative
construction transports those casualties as one nonaccumulating sidecar,
the existing bounded-defect terminal theorem converts them to an additive
constant in the final word length.

This is conditional on regeneration and the other construction gates.  It
does not by itself prove \(\nu(k)\le B(k)+O(1)\).

## 8. Exact scope

The theorem proves:

* the exact casualty formula for two alternatives with a common core;
* automatic cross-claim privacy from the protected wedge value ledger;
* a post-compensation bounded-deficiency theorem;
* the minimal raw dual-branch occurrence-lift interface; and
* a sharp hidden-common-capacity obstruction.

It does not prove the raw dual-branch lift, bounded deletion intersection,
two-coordinate product closure, topology, upper decoration, residence,
compiler regeneration, or the all-\(k\) OR-word theorem.

## 9. Dependencies

| role | file |
|---|---|
| protected wedge packing and exact owner/terminal ledger | MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md |
| factor occurrence lift | MATH_THEOREM_PROTECTED_ML_FACTOR_OCCURRENCE_LIFT_AND_OPENING_PARITY_20260804.md |
| canonical turn-diamond routes | MATH_THEOREM_MIDDLE_LEVELS_TURN_DIAMOND_CAPACITY_ROUTER_20260804.md |
| factor-restricted Rado deficiency | MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md |
| regular private-port comparison | MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md |
