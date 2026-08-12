# The four-switch Haar sequence is not a sealed Dyck-suffix cylinder

**Date:** 2026-08-06  
**Method:** pure mathematics; no finite search, solver, or computation  
**Status:** unconditional no-go for lifting all four recorded interaction
components while leaving the outside completion untouched.  It does not
rule out a larger lifted component which absorbs additional suffix sectors.

## 0. Verdict

The certified semilength-four Haar circuit is

\[
 \begin{aligned}
 F_1&=H_{(1\,3),K_1}(F_0),&|K_1|&=7,\\
 F_2&=H_{(2\,4),K_2}(F_1),&|K_2|&=2,\\
 F_3&=H_{(1\,5),K_3}(F_2),&|K_3|&=8,\\
 F_4&=H_{(1\,2),K_4}(F_3),&|K_4|&=4,
 \end{aligned}                                             \tag{0.1}
\]

where `F_0` is the canonical MSW factor and the last edge is the nonlocal
four-for-four Haar trade.

A local exact support trade does not automatically remain sealed after a
common suffix is attached.  Its base state and adjacent-union ledgers
cancel, but every proper tail phase remembers the chosen terminal endpoint
of each changed row.  The exact sealing criterion is equality of the
oriented terminal endpoint multisets on the two component shores.

For the last edge `K_4`, the endpoint-pair ledgers agree exactly at omitted
coordinates

\[
                              z\in\{3,4,6\}.             \tag{0.2}
\]

Thus that edge can be suffix-sealed at those cuts (and the port-restored
Tamari version is rowwise endpoint-fixed).  At every other cut the final
edge already leaks.

However, **no cut seals all four switches with the outside completion
untouched**.  If it did, the terminal Catalan port ledger of the canonical
fourteen-row cylinder would survive all four steps.  The resulting completed
Haar factor would then be `D_4`-port-transversal.  The exact port audit proves
that neither completed Haar factor is `D_4`-port-transversal under any
coordinate relabelling.  Hence at least one of the three preparatory lifted
components must join an outside suffix sector or change the completion.

The common-tail tensor therefore solves the final local trade, but not the
state-level suspension of the preparatory circuit.  The required successor
is a component-enlargement theorem, not a sealed-cylinder theorem.

## 1. General cylinder notation

Let `J` have size `2a`.  A local shortest complement path is

\[
                         P=(P_0,P_1,\ldots,P_a),        \tag{1.1}
\]

with `P_a=J-P_0`.  Let `E` be disjoint from `J`, `|E|=2s` with `s>=1`,
and let

\[
                         S=(S_0,S_1,\ldots,S_s)         \tag{1.2}
\]

be a fixed tail complement path.  For one chosen orientation of `P`, define

\[
 \operatorname{Cyl}_S(P)=
 (P_0+S_0,\ldots,P_a+S_0,
  P_a+S_1,\ldots,P_a+S_s).                            \tag{1.3}
\]

Call

\[
                              e(P)=P_a                  \tag{1.4}
\]

the oriented terminal endpoint.

Let `K^- -> K^+` be a local support-matched trade: the two row families
have identical aggregate rank-`a` state ledgers and identical aggregate
rank-`a+1` adjacent-union ledgers.  Choose an orientation on every row of
both shores and put

\[
                      E^\pm(K)=\{\!\{e(P):P\in K^\pm\}\!\}. \tag{1.5}
\]

## 2. Exact cylinder-sealing criterion

### Theorem 2.1 (terminal ledger is necessary and sufficient)

The replacement

\[
      \{\operatorname{Cyl}_S(P):P\in K^-\}
        \longrightarrow
      \{\operatorname{Cyl}_S(P):P\in K^+\}            \tag{2.1}

has zero aggregate central-state and adjacent-union current if and only if

\[
                              E^-(K)=E^+(K).            \tag{2.2}

When (2.2) holds, the lifted component is sealed: any factor rows disjoint
from the old cylinder remain disjoint from the new cylinder and may be left
untouched.

#### Proof

On the base segments, equality is exactly the two assumed local ledgers,
tensored by `S_0`.

For each proper tail phase `j>=1`, the state ledger is

\[
                         \{\!\{e(P)+S_j:P\in K^\pm\}\!\}. \tag{2.3}

Because `J` and `E` are disjoint, equality of (2.3) on the two shores is
equivalent to (2.2).  The tail adjacent-union ledger is similarly

\[
 \{\!\{e(P)+(S_{j-1}\cup S_j):P\in K^\pm\}\!\},       \tag{2.4}

and gives the same criterion.  The base/tail junction is included in
(2.4) at `j=1`.

Thus (2.2) is necessary and sufficient for zero cylinder current.  If the
old rows form part of an exact factor, replacing a support by an identical
support leaves its complement literally unchanged.  \(\square\)

### Corollary 2.2 (unoriented endpoint-pair form)

If the two shores have the same multiset of unordered complementary
endpoint pairs, orientations can be chosen so that (2.2) holds.  Conversely,
(2.2) implies equality of those endpoint-pair multisets.

This is the exact interface tested by the port ledger of a completed local
factor.

## 3. The final Haar edge

Let `F^-` and `F^+` be the two completed fourteen-row factors in
`NONLOCAL_HAAR_M4.md`, and let `K_4^-`, `K_4^+` be their four changed rows.
For an omitted coordinate `z`, let `mathcal E_z` be the multiset of the
four-core complementary endpoint pairs obtained by cutting every wreath at
`z`.

The exact port audit proves

\[
              \mathcal E_z(F^-)=\mathcal E_z(F^+)
              \quad\Longleftrightarrow\quad
              z\in\{3,4,6\}.                         \tag{3.1}

The ten common rows cancel from this equality.

### Proposition 3.1 (exact sealing scope of `K_4`)

The final four-row Haar component admits a common-tail sealed lift exactly
at the three cuts in (3.1).  At every other omitted-coordinate cut, any
suffix lift must change rows outside the four-row component.

#### Proof

After cancelling the ten common rows, (3.1) is equality of the unordered
endpoint-pair ledgers of `K_4^-` and `K_4^+`.  Apply Corollary 2.2 and
Theorem 2.1.  \(\square\)

For the port-restored Tamari packet `P^- <-> P^*`, the endpoint pairs agree
row by row, so its final local edge is suffix-sealed without an aggregate
rematching of its four rows.

## 4. Global obstruction to sealing the preparatory sequence

The canonical MSW factor `F_0` is `D_4`-port-transversal: after one fixed
choice of omitted coordinate and local coordinate order, its fourteen
paths have the fourteen Dyck roots as one endpoint each.

### Theorem 4.1 (no fully sealed four-switch cylinder)

There is no choice of one Dyck-suffix cylinder interface for which all four
switches in (0.1) lift as sealed components while every outside row of the
ambient MSW completion remains untouched.

#### Proof

Assume such an interface exists.  By Theorem 2.1 and Corollary 2.2, each
lifted switch preserves the complete unordered endpoint-pair multiset of the
fourteen-row cylinder.  Starting from `F_0`, after all four switches this
multiset is therefore still the Catalan port transversal.  Projecting away
the common suffix shows that the terminal semilength-four factor is
`D_4`-port-transversal, possibly after the one fixed coordinate relabelling
used to define the cylinder.

But the completed factor after the preparatory switches and final Haar edge
is one of the two factors audited in
`MATH_AUDIT_HAAR_M4_PORT_CONTEXT_20260726.md`, Theorem 5.1.  That theorem
rules out a fixed-boundary Dyck-context realization for **every** choice of
parent coordinate, row orientations, and common coordinate relabelling.
This contradiction proves the claim.  \(\square\)

### Corollary 4.2 (a preparatory component must leak)

At a cut `z notin {3,4,6}`, the final component `K_4` already leaks.  At a
cut `z in {3,4,6}`, the final component may be sealed, but at least one of
`K_1,K_2,K_3` fails (2.2).  Its high-dimensional interaction component
must contain additional suffix-cylinder rows, or the outside completion
must be reselected.

The same conclusion applies when the last edge is replaced by the
port-restored Tamari redecomposition: its local sealing does not repair the
nontransversal host produced by the preparatory sequence.

## 5. What survives

The no-go is narrower than the state-level suspension problem.

It does not rule out:

1. lifting a low component to a **larger** connected interaction component
   which absorbs the terminal-ledger discrepancy in neighbouring suffix
   sectors;
2. changing the common outside completion after each preparatory switch;
3. using several suffixes jointly so their endpoint currents cancel; or
4. a noncanonical high-dimensional factor built directly around the sealed
   final Tamari packet.

It does prove that the simplest hoped-for recursion is unavailable:

\[
 \boxed{
 \text{the four recorded low-dimensional components cannot all be tensored
 independently while the ambient MSW complement stays fixed}.}
\]

The exact successor is therefore an **endpoint-current absorbing component
lift**.  It must enlarge each leaking preparatory component until the total
terminal endpoint ledger closes.
