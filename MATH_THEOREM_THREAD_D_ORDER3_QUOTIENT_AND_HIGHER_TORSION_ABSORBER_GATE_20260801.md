# Order-three quotient rows force Catalan-scale off-support symmetry breaking

Date: 2026-08-01  
Lane: Thread D / prospective M0 / bounded-total rounding  
Status: exact quotient obstruction and exact reconciliation with the
higher-denominator and residual-slot absorber theorems. No unrestricted
Boolean infeasibility or B+O(1) claim is made.

## 0. Verdict

Three exact obstructions now point to the same conclusion.

1. The prospective oriented-diamond LP is not half-integral: it has a full
   denominator-11 vertex, and denominator 4 persists after fixing a
   correlated predecessor path.
2. A half-integral Boolean Q3 block has fractional value four but support
   matching number two. A resource-disjoint bank of such blocks forces
   \(\Omega(U)\) off-support changes, so the \(C=\operatorname{Cat}_m\)
   residual slots cannot be charged independently to support circuits.
3. When \(m=3r+2\), the full rotation quotient contains exactly
   \(\operatorname{Cat}_r\) row orbits fixed by the order-three subgroup,
   while the column and symbol shores have no fixed vertices. No invariant
   selected cell exists on any one of those row orbits.

The third obstruction is a symmetry statement, not another LP
denominator. It proves that a construction which remains fully equivariant
except on a bounded number of row orbits cannot work. The first two prove
that abandoning equivariance only through independent odd-circuit/one-slot
repairs cannot work either.

The forced sectors themselves are not residual defects. They admit an
exact isolated-edge Latin forest bank and should be preselected and
quarantined. The remaining positive route is a genuinely off-support,
recursive rounding of the free bulk after deleting the bank's distinct
columns, symbols, and matched values. It may make Catalan-many internal
changes, but it must export only a bounded live boundary. The exact
residual-slot/graphic absorber rank then determines whether that boundary
closes.

There is already an unconditional protected \(o(W)\)-total synchronization
theorem from the owner-slot nibble. It is the correct positive baseline,
but it does not give \(O(1)\) total defect, exact prospective M0 completion,
or the graphic forest.

## 1. The complement-Latin table

Let \(m=3r+2\) and

\[
 n=2m-1=3(2r+1).
\]

Use the prospective complement table

\[
 \mathcal C={ [n]\choose m-2},\qquad
 \mathcal B={ [n]\choose m-1},
\]

where a selected cell in row \(C\) uses a column \(B\supset C\) and one
symbol \(A\in\mathcal B\). A row-saturating column/symbol-injective
selection with acyclic column-to-symbol graph is equivalent to the rooted
upper-exact Catalan forest.

Let \(H\) be the order-three subgroup of the full coordinate rotation
\(G=\mathbb Z_n\). Its coordinate orbits are the \(2r+1\) triples

\[
                     \{i,i+(2r+1),i+2(2r+1)\}.         \tag{1.1}
\]

## 2. Exact fixed-row count

### Theorem 2.1 (Catalan fixed-row orbits)

Under the full rotation group \(G\):

1. the number of \(H\)-fixed rows in \(\mathcal C\) is

   \[
                         {2r+1\choose r};              \tag{2.1}
   \]

2. the quotient group \(G/H\cong\mathbb Z_{2r+1}\) acts freely on those
   rows;
3. consequently they form exactly

   \[
       {1\over2r+1}{2r+1\choose r}
          ={1\over r+1}{2r\choose r}
          =\operatorname {Cat}_r                       \tag{2.2}
   \]

   full-rotation row orbits; and
4. neither the column shore nor the symbol shore has an \(H\)-fixed
   vertex.

#### Proof

A row has size \(m-2=3r\). It is fixed by \(H\) exactly when it is a union
of \(r\) coordinate triples from (1.1), proving (2.1).

Identify those coordinate triples with \(\mathbb Z_{2r+1}\). If a
nonidentity translation stabilizes an \(r\)-subset, that subset is a union
of orbits of a nontrivial subgroup. Its size is then divisible by a
nontrivial divisor of \(2r+1\), impossible because
\(\gcd(r,2r+1)=1\). Thus the residual quotient action is free, and
division by \(2r+1\) gives (2.2).

A column or symbol has size \(m-1=3r+1\). Every \(H\)-fixed coordinate set
is a union of triples and has size divisible by three. Hence no column or
symbol is fixed by \(H\). \(\square\)

### Corollary 2.2 (no invariant cell on a fixed row)

There is no \(H\)-invariant selected cell over any row counted in
Theorem 2.1.

#### Proof

The stabilizer of a selected row must stabilize its selected column and
symbol under an equivariant selector. The row stabilizer contains \(H\),
whereas Theorem 2.1 gives no \(H\)-fixed column or symbol. Equivalently,
the three translates of a nonfixed column would select three cells in the
same fixed row. \(\square\)

This recovers the full-equivariance no-go and quantifies it: it is not one
exceptional row but \(\operatorname {Cat}_r\) full-rotation row orbits.

The obstruction is not an internal Hall defect of this exceptional bank.
The stronger residual-quotient theorem proves that, for every fixed clean
matching \(\mu\), all fixed rows can be assigned pairwise distinct columns
and symbols whose directed edges are isolated. With a fully rotational
\(\mu\), each Catalan sector needs and admits exactly one wrap seam. The
open problem is completing the nonfixed bulk around this large reserved
bank while keeping only bounded live interface state.

### Proposition 2.3 (quarantine preserves the scalar surplus)

Let

\[
 s=3^{v_3(n)},\qquad g=n/s,
\]

and quotient first by the maximal clean subgroup of order \(g\). The
residual order-three subgroup fixes

\[
                         f={s\over3}\operatorname {Cat}_r             \tag{2.3}
\]

quotient rows. The isolated bank uses exactly \(f\) distinct columns,
symbols, and matched values. After deleting those resources, the free
quotient table has

\[
             {U\over g}-f\quad\hbox{rows},\qquad
             {W\over g}-f\quad\hbox{columns and symbols},             \tag{2.4}
\]

so its column and symbol surplus remains exactly

\[
              \left({W\over g}-f\right)
              -\left({U\over g}-f\right)
                 ={\operatorname {Cat}_m\over g}.                     \tag{2.5}
\]

#### Proof

The fixed-row count and resource injectivity are the residual Catalan
exception and isolated-bank theorems. Quarantine removes one row, one
column, and one symbol per selected isolated edge. Subtraction proves
(2.4)--(2.5). \(\square\)

Thus preabsorption pays no scalar-surplus tax. Its effect is relational:
the free bulk must avoid a large, structured set of reserved resources.

## 3. Exact bounded-patch lower bound

Call a selector p-orbit patched when it agrees with a
full-rotation-equivariant row rule outside at most \(p\) full-rotation row
orbits. The rule may be arbitrary on the patched orbits.

### Corollary 3.1

Every row-saturating selector at \(m=3r+2\) which is p-orbit patched
satisfies

\[
                              p\ge\operatorname {Cat}_r.             \tag{3.1}
\]

#### Proof

By Corollary 2.2 the equivariant rule supplies no legal cell on any of the
\(\operatorname {Cat}_r\) fixed-row orbits. Every one must therefore
belong to the patch set. \(\square\)

The scope matters. Equation (3.1) does not say that a non-equivariant
construction has Catalan additive length or Catalan final defect. A single
recursive packet may reorganize all these rows internally while exporting
only a bounded interface. It says that such a packet cannot be modelled as
an invariant core plus \(O(1)\) exceptional row-orbit edits.

Within this equivariant-core architecture, treating a fixed tight-pivot
bank as the only exceptional patch changes only \(O(\sqrt m)\) literal
cells in the current planting range and leaves the Catalan family (2.2)
unserved. A viable recursive completion must break the quotient symmetry
away from the protected path as well.

## 4. Reconciliation with higher LP torsion

The order-three stabilizer and the LP denominators are distinct phenomena.

* The quotient obstruction is present before choosing a fractional basic
  solution. It says an invariant support has empty column/symbol fibres on
  \(\operatorname {Cat}_r\) row orbits.
* The denominator-11 and protected denominator-4 vertices occur in the
  unrestricted prospective LP. They say that, after symmetry is broken,
  fractional support components are not classified by half-integral odd
  cycles.
* The eight-column Q3 circuit says even a genuinely half-integral support
  may need two off-support representatives for four colours.
  Pairwise role-resource-disjoint copies force linear total off-support
  motion; asymptotically its lower bound exceeds the \(C\)-slot count by
  the factor \((m-1)/64\).

For a general determinant-\(q\) basic face, the exact upstream escape test
is the cofactor direction \(\operatorname {adj}(B)e_i\) obtained by
releasing one active capacity row: all other basis rows remain fixed, and
the sign/slack inequalities decide whether the motion reaches a support
boundary legally. This criterion successfully escapes the calibrated
cubic face but is not known for every Boolean basis. It should be applied
after contracting the quarantined quotient bank. The residual-slot rank in
Section 5 is downstream and denominator-independent: it begins only after
cofactor/off-support motion has produced an integral partial state.

Thus the proposed implication

\[
 \text{fractional point}
   \Longrightarrow \text{odd circuits}
   \Longrightarrow \text{one residual slot per circuit}
   \Longrightarrow O(1)\text{ final defect}
\]

fails at every arrow.

These are method obstructions only. The \(m=3\) prospective system has
many integral completions, and the protected denominator-4 face itself
contains 289 integral points. Global off-support motion can escape the
fractional faces.

## 5. Exact local absorber after symmetry breaking

For an integral partial state \((X,Y)\) whose selected rooted arcs form a
forest and whose omitted colour set is \(D\), let \(H_0\) be the unused
heads. A one-slot insertion is a triple

\[
       (R,(L,T),V),\qquad R\in D,\quad(L,T)\in Y,\quad V\in H_0,
\]

such that

\[
                         T\cap V=L,\qquad T\cup V=R.                 \tag{5.1}
\]

After contracting the old rooted forest, impose graphic independence on
the new arcs \(T\to V\). The maximum simultaneous absorber size is the
common-independence number

\[
 \nu_D(X,Y)=\max\{|A|:A\text{ is independent by colour, residual slot,
 head, and contracted graphic resource}\}.                           \tag{5.2}
\]

The best final defect using fixed-\(X\) insertions is exactly

\[
                              |D|-\nu_D(X,Y).                         \tag{5.3}
\]

If (5.3) is positive, protected slot transpositions reroute unprotected
existing colours and release new predecessor/head slots. Writing
\(r_P(X,Y;D)\) for the least number of such transpositions needed to reach
absorber rank \(|D|\), and setting \(r_P=+\infty\) when no such state is
reachable, the exact compound service cost when finite is

\[
                              |D|+r_P(X,Y;D).                         \tag{5.4}
\]

At \(m=3\) there is a literal one-colour state with \(\nu_D=0\): all four
tail facets of the missing upper set are consumed. One protected-safe
transposition of another colour releases a slot, after which insertion is
legal. Hence its compound service cost is exactly two
\((r_P=1)\). This proves the local
actuator is a compound alternating chain, not an independent slot.

Full \(H\)-equivariance cannot populate the fixed rows, but the
one-seam-per-sector construction populates all of them as an isolated-edge
bank. Freeze that bank and delete its used columns, symbols, matched values,
and graphic endpoints from the residual catalogue. The local rank (5.2)
should then be applied only to defects exported by the remaining free-bulk
rounding. Charging the already solved fixed sectors again would double
count the quotient obstruction.

## 6. The surviving recursive theorem

Let \(P_{\rm fix}\) be one of the exact isolated-edge banks on all forced
fixed-row sectors, and let \(\mathcal T_{\rm free}(P_{\rm fix})\) be the
complement-Latin table after deleting its used columns, symbols, and
matched values and contracting its isolated graphic edges.

The exact positive target exposed by the combined results is:

> **Off-support recursive absorber.** For every scale \(r\), construct a
> choice of \(P_{\rm fix}\) and an off-support packet on
> \(\mathcal T_{\rm free}(P_{\rm fix})\) which preserves the tight-pivot
> cells, retains \(P_{\rm fix}\) literally, and exports a boundary state
> \((X,Y;D)\) for
> which protected slot transpositions reach absorber rank \(|D|\) and
> \[
>                         |D|+r_P(X,Y;D)=O(1).
> \]

The quarantined bank may contain Catalan-many edges and one internal wrap
seam per sector; these are solved internal state, not exported defects.
The free-bulk packet is likewise allowed Catalan internal support and
changes. The required bound is on its **live exported boundary**, not on
the size of the preabsorbed bank or the number of internal edits. This is
how a genuine recursive reroute can evade Corollary 3.1 while still aiming
at \(B+O(1)\).

No such all-dimensional packet is proved here. What is proved is that a
bounded exceptional-orbit patch, half-integral circuit rounding, and
independent use of the \(C\) residual slots are each insufficient.

## 7. Dependencies

* The complement-Latin equivalence and full-rotation no-go are in
  MATH_THEOREM_BORN_LINEAR_COMPLEMENT_LATIN_PIVOT_AND_CYCLIC_QUOTIENT_20260801.md.
* The exact residual fixed-row census, isolated-edge bank, and one-seam
  sharpness are in
  MATH_THEOREM_THREE_PRIMARY_RESIDUAL_CATALAN_EXCEPTION_AND_TORSOR_RIGIDITY_20260801.md.
* Higher-denominator vertices are in
  MATH_THEOREM_THREAD_D_PROSPECTIVE_DIAMOND_EXTREME_DENOMINATORS_20260801.md.
* The Q3 circuit bank is in
  MATH_THEOREM_THREAD_D_BOOLEAN_PARITY_CIRCUIT_AND_RESIDUAL_SLOT_ROUNDING_NOGO_20260801.md.
* Exact local and compound absorption is in
  MATH_THEOREM_THREAD_D_HALF_INTEGRAL_HYPERCIRCUIT_AND_RESIDUAL_SLOT_ABSORPTION_20260801.md.
* The protected \(o(W)\)-total synchronization theorem is in
  MATH_THEOREM_ODD_DIAMOND_PROTECTED_SLOT_NIBBLE_AND_TORSION_ESCAPE_20260801.md.
