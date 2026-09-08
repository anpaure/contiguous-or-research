# Endpoint rotation gives upper-support-monotone relative seam trades at `m=7,8`

**Date:** 2026-08-13  
**Status:** unconditional abstract endpoint-rotation lemma and exact finite
`m=7,8` witnesses.  A uniform first-aligned-packet construction remains open.

## 1. The endpoint-rotation digraph

Let an exact owner/lower factor assign to every rank-`m` facet `L` a
two-element owner pair

\[
                         e_0(L)=\{P_L,V_L\},       \tag{1.1}
\]

where both owners contain `L`, and every rank-`m+1` owner occurs in exactly
two pairs.

Define a directed, facet-labelled graph `D(e_0)` on owners.  For each
oriented old pair `(P_L,V_L)` and each owner `W` containing `L`, distinct
from `P_L` and `V_L`, put an arc

\[
                         V_L\xrightarrow{L}W.       \tag{1.2}
\]

The arc retains `P_L` and changes only the moving endpoint:

\[
 \{P_L,V_L\}\longmapsto\{P_L,W\}.                 \tag{1.3}
\]

### Lemma 1.1 (endpoint-rotation circuit)

Let

\[
 V_0\xrightarrow{L_1}V_1\xrightarrow{L_2}\cdots
 \xrightarrow{L_t}V_t=V_0                            \tag{1.4}
\]

be a directed circuit whose facet labels are distinct.  Apply `(1.3)` at
each label.  Then every facet is still used once and every owner degree is
unchanged.

If `P_i` is the stationary endpoint at `L_i`, the rank-`m+2` upper-current
change is exactly

\[
 \Delta\mu^+
 =\sum_{i=1}^t
   \bigl(\mathbf e_{P_i\cup V_i}
         -\mathbf e_{P_i\cup V_{i-1}}\bigr).       \tag{1.5}
\]

#### Proof

Each color `L_i` remains attached to two distinct containing owners, so
lower incidence stays exact.  The stationary endpoints cancel termwise.
The moving endpoint multiset before the change is
`{V_0,...,V_(t-1)}` and afterward is `{V_1,...,V_t}`, the same multiset
because `V_t=V_0`.  Hence all owner degrees are unchanged.  Formula `(1.5)`
is the literal change of the union on each colored edge. \(\square\)

### Corollary 1.2 (two-path installation of a new colored edge)

Suppose the old edge of a facet `L_0` is `{A,B}` and the desired edge is
`{C,U}`.  If `D(e_0)` contains facet-label-disjoint paths

\[
                         C\leadsto A,qquad U\leadsto B,  \tag{1.6}
\]

avoiding `L_0`, then the two paths together with the two endpoint changes
`A->C`, `B->U` at `L_0` form endpoint-rotation circuits and install
`{C,U}` while preserving exact owner/lower incidence.

The same conclusion holds with `A,B` interchanged.  Any protected facet
bank is preserved if the two paths avoid it.

This is the exact relative rethread object.  It reduces the middle-rank
problem to two directed paths rather than a new global factor theorem.

## 2. The relevant upper condition is support monotonicity

Let `mu_0^+` be the immediate-upper load vector of the initial factor and
`mu_1^+` the load after the circuit.  The condition

\[
 \operatorname{supp}\mu_0^+
 \subseteq
 \operatorname{supp}\mu_1^+                         \tag{2.1}
\]

says that the relative trade creates no new upper hole.  It does **not**
claim that the initial factor covers every upper target, and it does not
preserve upper multiplicities.

By `(1.5)`, `(2.1)` is equivalent to

\[
 \mu_0^+(T)
 +\#\{i:P_i\cup V_i=T\}
 -\#\{i:P_i\cup V_{i-1}=T\}
 \ge1
\tag{2.2}
\]

for every `T` with `mu_0^+(T)>0`.

For an OR-covering application, `(2.1)` is the natural relative
requirement.  Global upper holes already present in the base factor remain
the responsibility of the upper backup atlas.

## 3. Exact `m=7` five-facet witness

Take the complete first-aligned MSW packet factor, freeze every selected
internal-portal row, and use the following five colored-edge replacements.
The displayed pair gives the two labels added separately to the facet.

\[
\begin{array}{c|c|c}
L&\text{old pair}&\text{new pair}\\ \hline
\{0,3,6,8,9,11,14\}&\{4,5\}&\{4,12\}\\
\{0,5,6,7,8,9,14\}&\{3,12\}&\{3,11\}\\
\{0,5,6,8,9,11,14\}&\{7,10\}&\{3,10\}\\
\{0,6,7,8,9,12,14\}&\{10,11\}&\{5,10\}\\
\{0,6,8,9,11,12,14\}&\{3,13\}&\{7,13\}.
\end{array}                                           \tag{3.1}
\]

In particular the fourth facet is

\[
 L_0=\{0,6,7,8,9,12,14\},                            \tag{3.2}
\]

and its replacement is exactly

\[
 \{L_0+5,L_0+10\}=\{C_4,U_5\}.                       \tag{3.3}
\]

### Theorem 3.1

The five replacements `(3.1)`:

1. are literal old edges of the `m=7` complete first-aligned packet factor;
2. avoid all six selected internal-portal rows;
3. preserve every owner degree and every facet color;
4. install `C_4-U_5`; and
5. satisfy the upper-support monotonicity `(2.1)`.

Every net removed upper value has old load at least two.  The minimum final
load among them is one.

#### Proof

Literal factor membership and protected avoidance are checked by recovering
the packet rows.  The owner endpoint multiset in the two columns of `(3.1)`
is identical, proving middle exactness.  Equation `(3.3)` proves the seam.
Finally compute the old global upper loads and apply `(2.2)`; all five net
removed occurrences leave positive load. \(\square\)

## 4. Exact `m=8` seven-facet witness

At `m=8`, write the seven replacements as follows:

\[
\begin{array}{c|c|c}
L&\text{old pair}&\text{new pair}\\ \hline
\{0,5,6,7,8,9,12,16\}&\{3,14\}&\{3,4\}\\
\{0,4,6,7,8,9,12,16\}&\{5,14\}&\{3,14\}\\
\{0,3,6,7,8,9,12,16\}&\{4,5\}&\{5,11\}\\
\{0,6,7,8,9,11,12,16\}&\{3,10\}&\{10,14\}\\
\{0,6,7,8,9,10,12,16\}&\{3,14\}&\{3,13\}\\
\{0,6,7,8,9,12,13,16\}&\{10,11\}&\{11,14\}\\
\{0,6,7,8,9,12,14,16\}&\{11,13\}&\{5,10\}.
\end{array}                                           \tag{4.1}
\]

The first four rows form the path from `C_4` to one old endpoint of the
seam facet; the next two form the path from `U_5` to the other; the last
row closes both paths at `L_0`.

### Theorem 4.1

The seven replacements `(4.1)` satisfy all five conclusions of Theorem
3.1 for the `m=8` packet factor.  In particular they preserve the support
of the old immediate-upper load vector while installing `C_4-U_5` and
fixing every selected portal row.

#### Proof

Apply Corollary 1.2 to the two displayed endpoint-rotation paths.  Exact
factor reconstruction checks every old pair and protected-facet avoidance.
The upper-load replay verifies `(2.2)` target by target. \(\square\)

## 5. What this changes, and what it does not

These witnesses show that the first coexistence obstruction is not a
middle-rank lattice hole.  The absent seam can be installed by a small
relative endpoint rotation while fixing the selected portal rows and
without destroying any upper value already covered by the base factor.

The remaining theorem is uniform: construct the two paths `(1.6)` for all
large `m` and all compound seams, jointly disjoint from the selected portal
bank, with `(2.2)` and with a chronology/residence realization.  The finite
witnesses do not prove that assertion.  They identify its exact directed-
path form and refute the possibility that the very first seam requires a
global re-factorization.

## 6. H100 replay

The standard-library verifier

* `scratch/verify_endpoint_rotation_upper_cover_m7_m8_20260813.py`

reconstructs both complete packet factors and checks every assertion above.
Its frozen H100 output is

* `scratch/h100_results/endpoint_rotation_upper_cover_m7_m8_20260813.json`.

All substantive replay ran on H100; the Mac was used only for lightweight
proof and file inspection.
