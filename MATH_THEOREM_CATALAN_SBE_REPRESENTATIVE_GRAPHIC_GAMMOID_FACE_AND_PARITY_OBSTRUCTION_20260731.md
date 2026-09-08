# Strict side representatives: the exact graphic--gammoid face and the first parity obstruction

Date: 2026-07-31  
Status: exact fixed-\(Q\) formulation, exact obstruction to the natural
matroid/gammoid collapse, and exact conditional graphic--gammoid theorem.
The accompanying literal \(n=3\) theorem independently refutes
`SBE + eta >= 3` as a universal representative-existence hypothesis.

## 0. Verdict

Strict balanced expansion (`SBE`) and the raw facet slack
\(\eta^\pm\ge3\) do **not** imply that either strict side has physical
representatives satisfying the degree caps, even before the final contracted
graphic row is imposed.  The independently replayed literal counterexample
is

```text
MATH_THEOREM_CATALAN_SBE_ETA3_SIDE_REPRESENTATIVE_N3_COUNTEREXAMPLE_20260731.md
```

and already occurs at \(n=3\).

There is also a structural reason that ordinary matroid intersection does
not automatically repair the gap.  After an orientation and a common basis
\(Q\) are fixed, one strict side asks for

```text
two palette partition bases
+ physical endpoint capacities
+ one rooted/contracted graphic row.
```

The first three rows already contain the four-column determinant-two parity
minor of Section 3.  The family of palette matchings is not a matroid on the
occurrence ground, and the family of physical linear forests is not a
matroid either.  Since every gammoid is a matroid, neither conjunction can
be hidden in one ordinary gammoid on the atomic occurrence ground.

There is, however, one clean polynomial face.  If complete side ears have
already been packetized so that palette ownership and all internal degree
caps are private, and a single unit-gated linkage gammoid exactly represents
the remaining socket choices, then the only live rows are that gammoid and
the contracted graphic matroid.  Edmonds' ordinary two-matroid min--max is
then necessary and sufficient.  This is a genuine protected-reserve theorem;
its packet/private hypotheses are not consequences of SBE or \(\eta\).

## 1. Exact fixed-\(Q\) atomic system

Fix one oriented structural parent, one common direct basis \(Q\), and one
strict shore.  Let \(E_Q\) be the retained occurrence ground.  Each
\(e\in E_Q\) has

\[
 a(e)\in A,\qquad b(e)\in B,\qquad
 \partial e=\{u(e),v(e)\}\subseteq Y,                 \tag{1.1}
\]

where \(A,B\) are the two palette banks, \(|A|=|B|=P\), and \(Y\) is the
physical side layer, \(|Y|=N\).  Let \(A_Q^\partial\subseteq Y\) be the
seam-anchor bank and put

\[
 c(y)=\begin{cases}1,&y\in A_Q^\partial,\\2,&y\notin A_Q^\partial.
 \end{cases}                                           \tag{1.2}
\]

Adjoin a root \(\rho\) and the root-star edge \(r_y=\rho y\) for every
anchor \(y\).  Since \(H=N-P\), a no-empty anchor-capped side is exactly a
binary solution \((x,z)\) of

\[
\begin{aligned}
 \sum_{e:a(e)=i}x_e&=1 &(i\in A),\\
 \sum_{e:b(e)=j}x_e&=1 &(j\in B),                     \tag{1.3}\\
 \sum_{e:y\in\partial e}x_e&\le c(y) &(y\in Y),       \tag{1.4}\\
 \sum_y z_y&=H,\\
 \{e:x_e=1\}\cup\{r_y:z_y=1\}
     &\text{ is a base of }M_{\rm gr}(Y\cup\{\rho\}). \tag{1.5}
\end{aligned}
\]

Here a physical occurrence is represented in the graphic matroid by its
edge \(\partial e\).  The selected set in (1.5) has \(P+H=N\) edges on
\(N+1\) vertices, so graphic independence is exactly the spanning-tree
condition.  Removing the root edges leaves a physical forest in which every
component contains an anchor.  The cap one in (1.2) makes every anchor an
endpoint.  Thus (1.3)--(1.5) are an exact extended formulation, not a
relaxation.

After one upper shore has been fixed, the lower alternating-cycle condition
is represented by the augmented graphic matroid obtained by attaching the
lower anchors to the components of the fixed central-plus-upper forest.
This augmented independence row is imposed **in addition to** (1.5) when a
no-empty lower shore is required; it replaces only the formerly separate
alternating-cycle test.  Thus each topology test is genuinely graphic after
the representatives on the other shore are fixed, but there can be two
graphic rows as well as the two palette rows and endpoint capacities.  They
collapse to the single graphic row of Section 4 only when the root/scaffold
obligation has already been fixed or certified inside private packets.

## 2. Why the atomic system is not one gammoid

### Proposition 2.1 (the two-palette family is not a matroid)

Take the four cells of \(K_{2,2}\), denoted \(e_{ij}\) with palette labels
\((i,j)\), \(i,j\in\{0,1\}\).  Its two perfect matchings are

\[
 B_0=\{e_{00},e_{11}\},\qquad
 B_1=\{e_{01},e_{10}\}.                              \tag{2.1}
\]

For \(e_{00}\in B_0\setminus B_1\), neither member of
\(B_1\setminus B_0\) can replace it: one repeats the first palette label and
the other repeats the second.  Hence the basis-exchange axiom fails.

This does not make palette matching hard--it is ordinary bipartite
matching--but it proves that its selected **occurrence edges** are not the
bases of one matroid or gammoid.  A transversal matroid records which source
vertices can be matched; it forgets which representative edges carried the
matching, while the physical row depends precisely on those representatives.

### Proposition 2.2 (physical linear forests are not a matroid)

On vertices \(1,2,3,4\), take occurrence edges

\[
 E=\{12,23,24,13\},\quad
 I=\{12,23\},\quad J=\{12,24,13\}.                   \tag{2.2}
\]

Both \(I\) and \(J\) are linear forests and \(|I|<|J|\).  Adding \(24\)
to \(I\) gives degree three at vertex \(2\), while adding \(13\) closes the
triangle \(123\).  Thus no element of \(J\setminus I\) augments \(I\).

Consequently the simultaneous physical degree-two and acyclicity row is not
a matroid, hence not a gammoid, on the atomic occurrence ground.  Splitting
physical vertices into capacity slots turns each occurrence into a paired
or multi-token object; requiring all tokens of an occurrence to be chosen
together is a parity/hypergraph constraint, not ordinary matroid
independence.

## 3. The first Boolean integrality obstruction

The failure appears before any graphic cycle.  Again use the four palette
cells \(e_{ij}\), and let every occurrence meet exactly one capped anchor.
Assign the anchor owner by parity:

\[
 \gamma(e_{00})=\gamma(e_{11})=0,qquad
 \gamma(e_{01})=\gamma(e_{10})=1.                    \tag{3.1}
\]

The two palette bases require a perfect matching of \(K_{2,2}\).  The
diagonal matching overloads anchor zero, and the off-diagonal matching
overloads anchor one.  Hence there is no integral cap-safe palette base.

Nevertheless

\[
                         x_{ij}=\tfrac12              \tag{3.2}
\]

satisfies every palette equality and both anchor caps with equality.  The
four tight rows

\[
\begin{pmatrix}
1&1&0&0\\
1&0&1&0\\
1&0&0&1\\
0&1&1&0
\end{pmatrix}                                         \tag{3.3}
\]

on columns \((x_{00},x_{01},x_{10},x_{11})\) have determinant \(2\), and
their unique solution at right side \((1,1,1,1)\) is (3.2).  Thus the
natural matching-plus-cap relaxation is not integral.  Equivalently, two
palette partition matroids plus the anchor partition already contain the
standard three-dimensional-matching correlation; the graphic row is a
fourth constraint, not a cure.

The scope is exact: this rules out the natural occurrence-ground TU,
generalized-polymatroid, and ordinary two-matroid argument.  It does not
rule out every conceivable enlarged formulation exploiting additional
Catalan geometry.

## 4. Exact protected graphic--gammoid face

The obstruction disappears when the recursive state has already internalized
the palette and degree correlations into complete private packets.

Let \(T=\bigsqcup_{i=1}^h T_i\) be a catalogue of complete side ears, with
one unit \(T_i\) for each required residual packet.  Assume:

1. Every option in \(T_i\) covers the same fixed palette packet, and the
   palette packets of distinct units are disjoint and together equal the
   residual palette banks.
2. Every option is internally a degree-valid path ear.  Internal vertices,
   palette cells and cap slots are private between units; only declared
   boundary sockets can interact.
3. There is a directed vertex-capacitated network with a unit gate \(p_i\)
   through which every route belonging to an option of \(T_i\) must pass.
   The desired simultaneous boundary routing is exactly vertex-disjoint
   linkage to a fixed sink bank.  Let \(M_L\) be the resulting gammoid on
   \(T\).  In particular an independent set uses at most one option from
   each unit.
4. After the fixed scaffold is contracted, every option has one declared
   attachment edge.  Let \(M_G\) be the graphic matroid of these quotient
   edges.  The quotient has \(h+1\) live components, so an independent set
   of order \(h\) is a spanning tree.  All root and common-cap guards are
   included in the fixed scaffold or in the private packet certificates.

### Theorem 4.1 (prepared private-packet min--max)

Under assumptions 1--4, a complete palette-exact, cap-safe, socket-disjoint
and contracted-acyclic side completion exists if and only if

\[
 r_{M_G}(X)+r_{M_L}(T\setminus X)\ge h
                         \qquad(X\subseteq T).         \tag{4.1}
\]

#### Proof

Edmonds' matroid-intersection theorem says that the maximum order of a set
independent in both \(M_G\) and \(M_L\) is the minimum left side of (4.1).
Thus (4.1) gives a common independent set \(I\) of order \(h\).  The unit
gates give at most one member of each of the \(h\) units, hence exactly one.
Assumptions 1 and 2 make the palette and internal degree rows automatic.
Gammoid independence is exactly the simultaneous socket routing, and
graphic independence of \(h\) quotient edges on \(h+1\) components is
exactly a spanning tree.  The converse sends any valid completion to the
same two independent sets, so matroid intersection gives (4.1). \(\square\)

This is the maximal standard two-matroid face of the present decomposition:
the unit partition must be absorbed into the linkage gammoid, and all atomic
palette/endpoint competition must already be private.  If a palette or cap
resource is shared between units outside the linkage network, it contributes
a third independent system and the parity minor of Section 3 can reappear.

## 5. Literal owner-alignment obstruction

The authenticated \(n=3\) counterexample makes the distinction literal,
not merely abstract.  Both shores are SBE and

\[
                         (\eta^-,\eta^+)=(3,3).        \tag{5.1}
\]

For every co-singleton common basis
\(Q_r=E(F)\setminus\{r\}\), each shore has exactly one palette-perfect
matching.  It is acyclic but has one degree-two centre.  If \(f^s(r)\) is
the child edge owning that centre's anchor colour, then

\[
                          f^s(r)\ne r                 \tag{5.2}
\]

for every \(r\) and both shores.  Under \(Q_r\), all owner colours except
the one owned by \(r\) are anchors, so (5.2) forces a cap-one violation.

This exposes the missing recursive state.  SBE controls the deletion basis
through palette expansion, while \(\eta\) counts unpunctured physical
occurrences.  Neither controls the correlation between the puncture and the
forced physical centre.  A positive recursion needs a
**puncture-correlated owner-aligned reserve**, or the stronger prepared
packet state of Theorem 4.1.  Merely increasing raw local occurrence degree
to three is insufficient.

## 6. Reproducibility and scope

The standard-library audit

```text
scratch/audit_catalan_sbe_representative_graphic_gammoid_face_20260731.py
```

checks the two exchange failures, determinant (3.3), the unique fractional
solution, absence of an integral parity completion, and the no-fixed-point
owner maps in the independently generated literal counterexample audit.

No statement here proves extension of the recursively produced SBE parents
at \(n=5,6,7\).  The exact surviving target is to construct the private
packet/unit-gammoid state, or a stronger occurrence-correlated reserve, for
that narrower recursive family.
