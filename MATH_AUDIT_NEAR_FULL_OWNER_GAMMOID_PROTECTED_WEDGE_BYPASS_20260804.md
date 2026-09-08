# Audit of the near-full owner-gammoid protected-wedge bypass

**Date:** 2026-08-04  
**Method:** independent pure-mathematical replay; no computation, search,
or solver  
**Audited theorem:** MATH_THEOREM_NEAR_FULL_OWNER_GAMMOID_PROTECTED_WEDGE_BYPASS_20260804.md  
**Audited SHA-256:** 4962e57f888848a40bc9b1f6cb8cb871d95bc2f1d777858a609ef9aebe93aadd

## 0. Verdict

**GO at the theorem's explicit occurrence-faithful fixed-state scope.**

The theorem correctly proves three nested statements:

1. the exact fixed-bank condition is the factor-restricted Rado inequality;
2. an independent owner set hitting every required star at least \(p\)
   times gives a protected wedge bank satisfying that inequality; and
3. residual owner-port corank \(K\le m-p\) forces such an independent
   hitting set.

The frozen-deletion and adaptive-contraction formulas correctly give two
ways to establish that scalar corank bound.  The theorem correctly leaves
the literal owner-port lift and its rank as premises.

## 1. Star-hit calculation

Every lower turn \(L_i\) has exactly

\[
 |N_i|=(2m-1)-(m-1)=m
\]

rank-\(m\) owner neighbours.  If \(B\) is a basis of
\(\Gamma|P_0\), then

\[
 |P_0\setminus B|
 =|P_0|-r_\Gamma(P_0)
 =K.
\]

Therefore

\[
 |B\cap N_i|
 =m-|N_i\setminus B|
 \ge m-K.
\]

Under \(K\le m-p\), every required owner star has at least \(p\) basis
owners.  This argument needs neither symmetry nor a random basis.  The
main theorem also assumes \(p\le m-1\), which is necessary for the strict
menu inequality below.

The weaker local-basis premise is exact for the ensuing construction:
any independent \(B\) with \(|B\cap N_i|\ge p\) suffices, even if it does
not span \(P_0\).

## 2. Basis-supported menu calculation

If \(s_i=|B\cap N_i|\), a wedge at \(L_i\) is unsupported precisely when
both of its owner coordinates lie outside \(B\).  Hence

\[
 |W_i(B)|
 ={m\choose2}-{m-s_i\choose2}
 =B_{s_i}(m).
\]

Because \(s_i\ge p\), \(p\le m-1\), and

\[
 B_{q+1}(m)-B_q(m)=m-q-1>0
\]

through the relevant range,

\[
 |W_i(B)|\ge B_p(m)>B_{p-1}(m).
\]

The exact menu-packing theorem therefore selects one wedge per lower turn
with all owner and q1-terminal values distinct.  Only its combinatorial
menu proof is used; no direct own-q1 branch activation is imported.

## 3. Gammoid routing replay

Each selected wedge has a basis owner.  Since all \(2p\) selected wedge
owners are distinct, choosing one basis owner from each wedge gives a
\(p\)-element set \(Q\subseteq B\).

Strict-gammoid independence is hereditary, so \(Q\) has simultaneous
vertex-disjoint typed suffixes to distinct sinks.  The theorem explicitly
assumes empty-interior, occurrence-faithful prefixes with distinct sources
and ports, and separation from the suffix interiors and frozen
compensation linkage.  Prepending those prefixes is therefore valid.

The q1 wedge terminal and the typed gammoid sink are not silently
identified.  This distinction is necessary and is correctly stated.

## 4. Factor completion replay

The menu packing gives:

* one distinct lower turn per wedge;
* lower degree two;
* \(2p\) distinct owners, hence upper degree one in the selected bank; and
* \(2p\) selected incidence edges.

Together with degree compatibility and

\[
 2p+|P_*|\le m-2,
\]

the small protected-factor theorem applies.  The completion-stability
hypothesis is necessary because the cap port \(p_U\) was chosen before
factor completion.

## 5. Exact fixed-bank Rado form

For a fixed wedge bank \(D\), claim \(i\) has the two-port menu \(A_i(D)\).
Rado's theorem gives maximum service rank

\[
 \min_{X\subseteq[p]}
 \left(
 p-|X|+
 r_\Gamma\!\left(\bigcup_{i\in X}A_i(D)\right)
 \right).
\]

Subtracting from \(p\) gives exactly

\[
 \delta(D,c)=
 \max_{X\subseteq[p]}
 \left(
 |X|-
 r_\Gamma\!\left(\bigcup_{i\in X}A_i(D)\right)
 \right).
\]

Thus (5.2) is necessary and sufficient for the displayed architecture,
and (5.4) leaves at most \(C\) claims.

## 6. Sharp corank obstruction

For \(p\le m-1\), at \(K=m-p+1\), choose \(m-p+1\) loop ports inside one star \(N_1\) and
make every other port free.  This is a strict gammoid: nonloops have
private sinks and loops have no path.  Its unique full basis meets \(N_1\)
in only

\[
 m-(m-p+1)=p-1
\]

ports.  Hence the supported menu has exactly \(B_{p-1}(m)\) wedges.

The attained conflict construction can place \(p-1\) protected wedges
whose forbidden set at \(L_1\) is precisely those \(p-1\) coordinate
stars.  Therefore all basis-supported candidates can be blocked at the
next step.  This proves sharpness for any implication using only the scalar
corank and sequential menu cardinality.

It does not prove that every factor-compatible Rado selection fails at
larger corank; the theorem correctly excludes that stronger claim.

## 7. Frozen deletion replay

Fix a full raw linkage \(\mathcal R\) of \(P_0\).  Its paths are
vertex-disjoint and have distinct terminal slots.  Each deleted physical
capacity or sink slot can therefore meet at most one path.  If
\(h_F(\mathcal R)\) displayed paths meet the deletion bank \(F\), then

\[
 r_\Gamma(P_0)\ge |P_0|-h_F(\mathcal R)\ge |P_0|-|F|
\]

and residual corank is at most \(h_F(\mathcal R)\).  Thus the existence of
a raw full linkage with \(h_F(\mathcal R)\le m-p\) implies the main
theorem.  The coarser row \(|F|\le m-p\) is sufficient.

The theorem correctly counts physical resources, not logical background
claims.  No bound on path length is assumed.

## 8. Adaptive contraction replay

For an independent background set \(C\), \(|C|=b\),

\[
\begin{aligned}
r_{M/C}(P_0)
 &=r_M(C\cup P_0)-r_M(C)\\
 &=r_M(C\cup P_0)-b.
\end{aligned}
\]

Therefore

\[
 |P_0|-r_{M/C}(P_0)
 =b+|P_0|-r_M(C\cup P_0).
\]

The raw joint-rank floor

\[
 r_M(C\cup P_0)\ge b+|P_0|-(m-p)
\]

is exactly equivalent to residual corank at most \(m-p\).

## 9. Full-set cut and current common-cap interface

The basis-supported selection needs only

\[
 r_\Gamma(P_0)\ge |P_0|-(m-p).
\]

By Menger this is equivalent to the single full-set cut family

\[
 \operatorname{cap}(C)\ge |P_0|-(m-p)
\]

for every residual \(P_0\)-to-sink cut \(C\).  It is weaker than requiring
the corresponding rank floor for every owner subset.

The one-step factor prefixes have empty interiors in the serialized
occurrence model, so reserving them causes no hidden rank loss.  Any
implementation which prices an additional boundary or flag resource must
add it to the frozen deletion bank.

The regular private-port theorem closes the row under its stronger premise
\(r_\Gamma(P_0)=|P_0|\), but that theorem assumes rather than derives the
occurrence ports, private prefixes, and suffix linkage.

If the existing common-cap all-subset premise is instantiated with one
singleton ticket per owner port, it yields

\[
 r_\Gamma(X)\ge |X|-k
\qquad(X\subseteq P_0),
\]

hence corank \(K\le k\).  The row \(k\le m-p\) then closes the suffix
gate.

This is only an interface: the current source states this rank inequality
as a hypothesis and does not establish the occurrence lift or the rank for
the owner tickets.  The theorem and audit preserve that scope.

## 10. Paired-port post-factor deletion replay

After a wedge bank is fixed, suppose all \(2p\) distinct owner ports have
one raw disjoint suffix linkage.  If \(h\) displayed paths meet the frozen
deletion bank, a claim loses both alternatives only when two of those
\(h\) paths belong to its owner pair.  The owner pairs are disjoint, so at
most

\[
 \left\lfloor{h\over2}\right\rfloor
\]

claims lose both paths.  Every other claim chooses one surviving path, and
the chosen paths remain disjoint.  This proves the post-factor deficiency
bound.

A common source or guard deleted once can kill both alternatives of one
claim.  Separating \(c\) such common casualties from the side-path losses
correctly changes the bound to

\[
 c+\left\lfloor{h\over2}\right\rfloor.
\]

## 11. Remaining exact alternatives

The one-coordinate cap gate is reduced to either:

\[
 \exists B\in\mathcal I(\Gamma):
 |B\cap N_i|\ge p\quad(1\le i\le p),
\]

or, more weakly, selecting a protected wedge bank \(D\) satisfying

\[
 r_\Gamma\!\left(\bigcup_{i\in X}A_i(D)\right)\ge |X|
 \quad(X\subseteq[p]).
\]

A global corank at most \(m-p\), a raw full linkage meeting the frozen bank
in at most \(m-p\) paths, or the adaptive joint-rank condition are three
zero-defect sufficient certificates.  A post-factor raw linkage with
bounded deletion intersection gives bounded deficiency.  None is presently
derived for the current all-dimensional child.
