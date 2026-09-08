# Endpoint-only active wedges have an exact \(m-p\) terminal margin

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional fixed-state corollary of the exact protected-wedge
packing theorem.  It closes activation when cap legality factorizes into
star-active owner sides and forbidden own-q1 terminals.  It does not prove
that the current common cap has this endpoint-only form.

## 0. Result

Fix distinct lower turns \(L_1,\ldots,L_p\) in \(ML_m\), with

\[
                         1\le p\le m-1.
\]

At \(L_i\), identify the \(m\) possible owner extensions with the set

\[
                         C_i=[2m-1]\setminus L_i.
\]

Fix one residual cap/guard/phase/occurrence state.  Let

\[
                         A_i\subseteq C_i,\qquad |A_i|=a_i,
\]

be a bank of **star-active sides**: for every \(a\in A_i\) and every
\(b\in C_i-\{a\}\), the direct branch

\[
 L_i\longrightarrow L_i+a\longrightarrow L_i+a+b
\tag{0.1}
\]

is present and typed legal unless its terminal pair \(\{a,b\}\) belongs to
a declared forbidden terminal set \(T_i\).

Every displayed source, owner, terminal, and arc is a completion-stable
physical occurrence in this same state.  Direct branches for different
selected owner/terminal values have no hidden shared capacity.

Let

\[
 t_i=
 |\{e\in T_i:e\cap A_i\ne\varnothing\}|
\tag{0.2}
\]

be the number of forbidden terminals which would otherwise be supported
by an active side.

### Theorem

The exact active wedge menu at \(L_i\) has size

\[
 \boxed{
 |W_i^c|
 =B_{a_i}(m)-t_i
 ={m\choose2}-{m-a_i\choose2}-t_i.
 }
\tag{0.3}
\]

Consequently, if

\[
 \boxed{
 B_{a_i}(m)-t_i>B_{p-1}(m)
 \qquad(1\le i\le p),
 }
\tag{0.4}
\]

one can select one active wedge per lower turn so that all \(2p\) owners
and all \(p\) q1 terminal values are pairwise distinct.  Choosing a
star-active side in every selected wedge gives pairwise vertex-disjoint
typed direct routes.

The particularly simple sufficient row is

\[
 \boxed{
 a_i\ge p,\qquad t_i\le m-p-1
 \qquad(1\le i\le p).
 }
\tag{0.5}
\]

Indeed,

\[
                         B_p(m)-B_{p-1}(m)=m-p.
\tag{0.6}
\]

Under the usual degree compatibility and edge budget

\[
                         2p+|P_*|\le m-2,
\]

the selected wedges and the incumbent protected bank \(P_*\) extend to one
spanning Middle-Levels two-factor.

## 1. Proof of the exact count

There are \({m\choose2}\) full wedges at \(L_i\).  A wedge has no
star-active side exactly when both extension coordinates lie in
\(C_i\setminus A_i\), giving

\[
                         {m-a_i\choose2}
\]

unsupported pairs.  The remaining supported pairs are distinct own-q1
terminal values.  Exactly \(t_i\) of them are forbidden by (0.2).
This proves (0.3).

Under (0.4), apply the exact active-menu packing theorem.  It selects
wedges with all owners and terminals distinct.  Every selected wedge lies
in \(W_i^c\), so it has at least one side in \(A_i\) and a nonforbidden
terminal.  Choose such a side.  The automatic-private-routing corollary
then gives the literal linkage.

Finally,

\[
\begin{aligned}
B_p(m)-B_{p-1}(m)
 &=
 \left[{m\choose2}-{m-p\choose2}\right]
 -
 \left[{m\choose2}-{m-p+1\choose2}\right]\\
 &=m-p.
\end{aligned}
\]

Thus (0.5) implies

\[
 |W_i^c|
 \ge B_p(m)-(m-p-1)
 >B_{p-1}(m).
\]

## 2. Sharpness of both endpoint rows

The owner-side threshold is sharp for this cardinality implication.  With
only \(a_i=p-1\) star-active sides and no terminal holes,

\[
                         |W_i^c|=B_{p-1}(m),
\]

which is exactly the attained one-step conflict maximum.

The terminal margin is also sharp.  With \(a_i=p\), the newly supplied
margin over the threshold consists of exactly

\[
                         B_p(m)-B_{p-1}(m)=m-p
\]

wedges.  Declare precisely those \(m-p\) terminal pairs forbidden.  The
retained active menu has size \(B_{p-1}(m)\), and the sharp protected
prefix can block all of it.

Thus neither \(a_i\ge p\) nor \(t_i\le m-p-1\) can be weakened in a
uniform endpoint-count proof using no further structure.

## 3. Relation to gammoid corank

If the star-active side set is obtained from an independent owner-port set
\(B\) in a residual suffix gammoid, then

\[
                         A_i=B\cap N(L_i).
\]

Global owner-port corank \(K\le m-p\) guarantees \(a_i\ge p\).  The
near-full owner-gammoid theorem then routes through arbitrary typed
suffixes and does not need own-q1 terminal availability.

The present theorem is the complementary direct face: it needs the
own-q1 branch (0.1), but once that branch is active it replaces all suffix
rank cuts by the endpoint count (0.4).

## 4. Exact scope

The theorem proves a zero-defect one-coordinate router from:

* \(p\) completion-stable star-active owner sides per source;
* fewer than \(m-p\) forbidden supported q1 terminals per source; and
* the exact protected-wedge factor-completion ledger.

It does not prove star activation, terminal typing, value-to-occurrence
injectivity, survival after a dynamic factor-dependent deletion, or any
two-coordinate product, topology, upper, residence, compiler, or
regeneration theorem.

The endpoint-only premise is stronger than an ordinary nonloop or gammoid
rank statement: one active owner side must retain its complete q1 fan
apart from the explicitly counted terminal holes.

## 5. Dependencies

| role | file |
|---|---|
| exact active-menu threshold and automatic private routing | MATH_THEOREM_CAP_AWARE_PROTECTED_WEDGE_ACTIVATION_AND_EXACT_MENU_THRESHOLD_20260804.md |
| near-full gammoid alternative | MATH_THEOREM_NEAR_FULL_OWNER_GAMMOID_PROTECTED_WEDGE_BYPASS_20260804.md |
| protected factor completion | MATH_THEOREM_PROTECTED_TURN_DIAMOND_WEDGE_PACKING_20260804.md |
