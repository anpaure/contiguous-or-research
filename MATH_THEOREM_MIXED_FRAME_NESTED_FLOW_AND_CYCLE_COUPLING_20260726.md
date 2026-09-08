# Mixed frames: nested-flow integrality and the exact cycle-coupling failure

Date: 2026-07-26

Method: pure mathematics.

## 0. Outcome

Fix a catalogue of coordinate pair frames on `[2m]` and a protected depth
`H`.  The mixed-pair owner/type theorem assigns integral marginal
capacity independently at every depth.  The first coherence question has
a stronger exact answer.

> Once each physical target copy has been assigned to a frame, all depths
> in that frame can be routed simultaneously through one layered
> pair-flip network.  Fractional feasibility implies integral feasibility,
> and the integral flow decomposes into owner-rooted nested prefix paths.

The owner-to-frame choice on one side may be left inside this network:
source arcs select the frame and every subsequent arc stays there.  The
constraint matrix remains a directed node--arc incidence matrix with
split-node capacity arcs, hence is totally unimodular.  The exact
feasibility criterion is Hoffman's family of circulation cuts.

This proves substantially more than independent depthwise Hall.  It does
not prove that the marginal target-frame assignments supplied by the
mixed-pair theorem can be chosen coherently.  If target certificates are
also allowed to choose their frames, the owner/path/certificate matrix has
a determinant-two minor already at depths one and two:

\[
 \begin{pmatrix}
  1&0&1\\
  1&1&0\\
  0&1&1
 \end{pmatrix}.
\tag{0.1}
\]

Thus total unimodularity of the direct network formulation stops at the
target-frame linking rows.

Whole-cycle grouping is a second, independent failure.  In one
three-dimensional cube fibre, an isometric six-cycle is the cube with one
complementary vertex pair deleted.  Three such cycles and one vertex from
each of three omitted pairs give the actual cycle-owner incidence minor

\[
 \begin{pmatrix}
  0&1&1\\
  1&0&1\\
  1&1&0
 \end{pmatrix},
 \qquad\det=2.                                         \tag{0.2}
\]

Consequently the direct owner/frame/prefix/cycle matrix is not totally
unimodular.  Its natural cycle block is not a matroid on owner
assignments; the formulation is a network-flow polytope coupled to a
hypergraph cycle-packing polytope.

The strongest unconditional rounding statement is therefore:

\[
\boxed{
\begin{array}{l}
\text{integral target-frame partitions}
 +\text{ fractional nested pair-flip flow}\\
\Longrightarrow
\text{integral owner-frame assignment and integral nested flags};\\[1mm]
\text{an integral cycle selection fixed in advance}
 +\text{ fractional residual flow}\\
\Longrightarrow
\text{integral residual nested flags}.
\end{array}}
\tag{0.3}
\]

No corresponding rounding of fractional target-frame choices or
fractional cycle variables follows from total unimodularity alone.

---

## 1. The frame-specific deletion DAG

Let

\[
 \mathcal M=\binom{[2m]}m,\qquad
 \mathcal L_q=\binom{[2m]}{m-q}.
\tag{1.1}
\]

Fix a coordinate perfect matching `P_j`.  A middle owner `X` has
`f_j(X)` full pairs and `m-2f_j(X)` split pairs.  Deleting the selected
coordinate from one split pair makes that pair empty and leaves the number
of full pairs unchanged.

For each frame `j` form a layered DAG `D_j^-`.  Its level-zero vertices
are the eligible middle owners `(j,0,X)`.  Its level-`q` vertices are
`(j,q,T)` with `T\in\mathcal L_q` of an eligible pair type.  Put an arc

\[
 (j,q-1,S)\longrightarrow(j,q,T)                       \tag{1.2}
\]

when

\[
 T=S\setminus\{x\}
\tag{1.3}
\]

and `x` is the currently selected coordinate of a split `P_j`-pair.
Along a directed path no pair can be used twice, because after its
selected coordinate is removed the pair is empty.

Hence every length-`H` path from `X` has the form

\[
 X,\quad X\setminus\{x_1\},\quad
 X\setminus\{x_1,x_2\},\ldots,
 X\setminus\{x_1,\ldots,x_H\},                         \tag{1.4}
\]

where the `x_i` belong to distinct split pairs.  Conversely every legal
nested pair-flip prefix has exactly one path representation in `D_j^-`.

The reverse construction, adjoining one coordinate from a split pair at
each step, gives the upper DAG `D_j^+`.

---

## 2. One coupled nested-prefix network

For each lower target `T\in\mathcal L_q` choose an assigned frame
`\psi_q(T)`.  Put

\[
 B_{j,q}=\{T:\psi_q(T)=j\}.                           \tag{2.1}
\]

More generally one may prescribe integral lower and upper throughputs

\[
 \ell_{j,q}(T)\le v_{j,q}(T)\le u_{j,q}(T),            \tag{2.2}
\]

with `\ell_{j,q}(T)\ge1` for every `T\in B_{j,q}`.
The upper bounds may encode pair-type supply, floor quotas, or a literal
one-copy rainbow requirement.

Split every state vertex `v=(j,q,T)` of `D_j^-` into `v^{in},v^{out}`
and join them by a throughput arc `a_v` with bounds (2.2).  Redirect the
incoming transition arcs to `v^{in}` and the outgoing transition arcs
from `v^{out}`.

To allow the lower-side owner-frame assignment to be chosen inside the
model, give every owner `X` a source node `s_X` of supply one and arcs

\[
 s_X\longrightarrow(j,0,X)^{in}                       \tag{2.3}
\]

for its allowed frames.  Give the terminal level a common sink.  Add the
usual return arc from the sink to a supersource to express the system as a
circulation with lower and upper bounds.

Call the resulting network `\mathcal N^-(\psi,\ell,u)`.

### Theorem 2.1 (simultaneous nested-prefix integrality)

The following are equivalent.

1. `\mathcal N^-(\psi,\ell,u)` has a real feasible flow.
2. It has an integral feasible flow.
3. There is an integral assignment of every owner to one allowed frame
   and one legal nested prefix (1.4) in that frame such that all
   throughputs satisfy (2.2).

#### Proof

After node splitting, every variable is an arc variable and every
conservation equation is a row of a directed node--arc incidence matrix.
Appending integral lower and upper arc bounds preserves total
unimodularity.  Therefore every nonempty bounded face with integral data
has an integral vertex, proving `1\Rightarrow2`.

At an integral flow, the unit supply leaving `s_X` uses exactly one arc
(2.3).  Integral flow decomposition then gives one root-to-terminal path
for every owner.  Since frame layers are disjoint after (2.3), the path
cannot change frame.  Section 1 identifies it with a legal nested prefix.
The throughput arcs give (2.2), proving `2\Rightarrow3`.  The converse is
obtained by sending one unit along every displayed path. \(\square\)

This is an extended formulation.  A root-labelled path-column matrix may
contain determinant-two minors, but cross-splicing integral flow at a
common state vertex restores a valid decomposition into nested paths.  The
arc-flow theorem, not the naive path matrix, is the relevant integrality
statement.

### Corollary 2.2 (two-sided conditional integrality)

Fix an integral owner-frame assignment.  If the lower and upper
frame-specific nested-flow systems are fractionally feasible, then they
have integral solutions simultaneously.

#### Proof

With the roots fixed, `D_j^-` and `D_j^+` are two disjoint collections of
networks with integral data.  Apply Theorem 2.1 separately and take the
two integral solutions.  They use distinct forward and reverse occurrence
slots. \(\square\)

The qualification “roots fixed” is material.  Requiring the lower and
upper flows to choose the same frame while both choices remain fractional
adds linking equalities between two network blocks.  Those equalities are
not part of a single directed incidence matrix.

---

## 3. The exact all-depth cut theorem

Theorem 2.1 has a necessary-and-sufficient cut form.  For an arc set
`A` write `\ell(A)=\sum_{a\in A}\ell_a` and
`u(A)=\sum_{a\in A}u_a`.

### Theorem 3.1 (Hoffman cuts for nested pair transport)

The simultaneous nested-prefix system is feasible if and only if, after
the standard supply-to-circulation conversion, every vertex set
`S\subseteq V(\mathcal N^-)` satisfies

\[
 \boxed{\ell(\delta^-(S))\le u(\delta^+(S)).}           \tag{3.1}
\]

All quantities are integral, so satisfaction of these cuts produces an
integral nested-prefix solution.

#### Proof

This is Hoffman's circulation theorem applied to the split network.
Necessity follows by summing flow conservation over `S`.  Sufficiency is
the max-flow/min-cut theorem after adding the standard lower-bound
imbalance arcs.  Integrality follows from Theorem 2.1. \(\square\)

For `H=1`, (3.1) is exactly the face-Hall system inside the assigned
frame bins when the roots are fixed, and the combined face-Hall system
when the roots may choose frames.  For `H>1` it includes every staircase
cut crossing several successive Boolean levels.  Thus independent
validity of the depthwise Hall inequalities is necessary but not
sufficient; (3.1) is their exact simultaneous replacement.

### Corollary 3.2 (no rounding loss after the mixed-pair marginals)

Take any integral target-frame assignments `\psi_q` supplied by the
mixed-pair marginal theorem.  If their associated layered network
satisfies (3.1), then the same assignments admit integral nested prefixes
for all depths simultaneously.  No discrepancy, randomized rounding, or
depth-by-depth repair is required after this cut verification.

---

## 4. Why choosing target frames jointly is not TU

The target assignments in (2.1) were fixed.  Introduce certificate
variables which choose one frame-path occurrence for each physical target
and require every owner to choose one frame.  The direct coupled matrix is
not totally unimodular, already for two depths.

Choose a rank-`m-2` set `B` and distinct coordinates `a,b,c` outside it.
Put

\[
 A=B\cup\{a\},\qquad A'=B\cup\{b\}.                   \tag{4.1}
\]

Let

\[
 X=B\cup\{a,b\},\qquad Y=B\cup\{a,c\}.                 \tag{4.2}
\]

There are legal frame paths with the following certificate profiles.

* `p_1` starts at `X`, certifies `A` at depth one, and uses at depth two
  a private child different from `B`.
* `p_3` starts at `X` in another frame, uses a private depth-one target,
  and certifies `B` at depth two.
* `p_2` starts at `Y`, certifies `A` and then `B`.

Every finite displayed deletion chain can be embedded in a pair frame:
pair its deleted coordinates with distinct coordinates outside the root
owner.  Hence these are literal mixed-pair paths, not abstract columns.

Restrict the coupled constraint matrix to

* the owner-choice row for `X`;
* the unique-certificate row for `A`;
* the unique-certificate row for `B`;

and to columns `p_1,p_2,p_3`.  The resulting matrix is

\[
\begin{array}{c|ccc}
 &p_1&p_2&p_3\\ \hline
 X&1&0&1\\
 A&1&1&0\\
 B&0&1&1
\end{array}                                           \tag{4.3}
\]

and has determinant two.

This is not merely a bad path-column projection.  Restrict the three
frame DAGs so that the displayed paths are the only paths meeting `A` or
`B`, and give `Y` one additional completely private path `p_4`.  The
integer right-hand sides

\[
 p_1+p_3=1,\qquad
 p_1+p_2=1,\qquad
 p_2+p_3=1,\qquad
 p_2+p_4=1                                             \tag{4.4}
\]

express respectively the owner supply of `X`, exact physical throughput
at `A`, exact physical throughput at `B`, and the owner supply of `Y`.
They have the fractional solution

\[
                         p_1=p_2=p_3=p_4={1\over2}
\]

and no integral solution.  In the restricted DAG every internal arc has
one predecessor and one successor, so conservation forces all arcs of a
path to carry the same value `p_i`.  Hence the unprojected
arc-flow-plus-linking system itself is nonintegral on this instance.

### Theorem 4.1 (target-frame linking destroys TU)

The direct owner/path/target-certificate formulation is not totally
unimodular for `H\ge2`.  Fractional target-frame marginals therefore
cannot in general be rounded by one network-integrality argument.

The obstruction is absent when the target-frame partition is fixed:
then certificate rows become integral node lower bounds and Theorem 2.1
applies.  It is also absent at one depth, where owner choices and target
certificates form an ordinary bipartite assignment network.

Theorem 4.1 does not prove that the full symmetric catalogue lacks an
integral coherent assignment.  It proves that such an assignment requires
dependent rounding, an absorber, or a non-TU matching theorem beyond the
two marginal transport networks.

---

## 5. Coupling complete isometric cycles

Let `\mathscr C_j` be a catalogue of oriented isometric cycles in the
pair-cube fibres of frame `j`.  A cycle `C` determines

* an owner incidence vector `\chi_C(X)`;
* lower nested-prefix incidences `a^-_{C,q}(T)`;
* upper incidences `a^+_{C,q}(T)`.

Introduce cycle variables `z_C\in[0,1]` and residual owner variables
`r_{X,j}`.  The natural coupled system contains

\[
 \sum_j\sum_{\substack{C\in\mathscr C_j\\X\in C}}z_C
 +\sum_jr_{X,j}=1
 \qquad(X\in\mathcal M),                              \tag{5.1}
\]

Cycle owners must not be rerouted through arbitrary prefix paths.  Only
the residual owners enter the free nested-flow network, with root
equations

\[
                         f_{j,0}(X)=r_{X,j}.            \tag{5.2}
\]

The cycle columns contribute their fixed physical target incidences
directly.  The coupled coverage rows are

\[
 v^{\pm,\mathrm{res}}_{j,q}(T)
 +\sum_{C\in\mathscr C_j}a^\pm_{C,q}(T)z_C
 \ge\ell^\pm_{j,q}(T).                                \tag{5.3}
\]

Equations (5.1)--(5.3), together with the residual nested-flow
conservation equations, are one exact network-plus-cycle-hypergraph
formulation of the requested problem.

The cycle variables are not a matroidal block.  “Being a union of complete
cycles” is not hereditary on owner assignments, so it is not a matroid on
the owner-frame ground set.  On the cycle ground set, owner disjointness
is hypergraph matching; it is a partition matroid only when the entire
allowed cycle catalogue is already globally disjoint.

### Theorem 5.1 (an actual cycle-incidence determinant)

The owner--cycle incidence matrix is not totally unimodular, already
inside one three-dimensional pair-cube fibre.

#### Proof

In `Q_3` an isometric six-cycle has transition word `\pi\pi` and omits
exactly one complementary vertex pair.  Conversely, deleting any one of
the four complementary pairs leaves such a six-cycle.

Choose three complementary pairs `P_1,P_2,P_3` and let `C_i` be a
six-cycle omitting `P_i`.  Choose one vertex `v_i\in P_i`.  Then `v_i`
does not lie on `C_i` and lies on each `C_j` with `j\ne i`.  On the rows
`v_1,v_2,v_3` and columns `C_1,C_2,C_3` the incidence matrix is

\[
 \begin{pmatrix}
  0&1&1\\
  1&0&1\\
  1&1&0
 \end{pmatrix},
\]

whose determinant is two. \(\square\)

The same fibre gives an actual fractional integrality gap for exact owner
cover.  Let `C_1,\ldots,C_4` be the four six-cycles, where `C_i` omits
the complementary pair `P_i`.  Then

\[
                         z_{C_i}={1\over3}\qquad(1\le i\le4)           \tag{5.4}
\]

covers every cube vertex with total weight one, because a vertex lies in
the three cycles not omitting its complementary pair.  No integral exact
cover exists: every selected block has six vertices, while `Q_3` has
eight, so `6\sum_i z_{C_i}=8` has no integral solution.  Thus the
fractional cycle-cover relaxation itself is nonintegral, not merely
represented by a non-TU matrix.

This is a genuine minor in the unprojected physical cycle catalogue.
Unlike path-flow cross-splicing, ordinary state-flow splicing does not
preserve the requirement of remaining a complete selected cycle.  The
minor does not rule out a different extended formulation based on
additional cycle trades; none is supplied by the marginal TU theorem.

### Corollary 5.2 (conditional residual rounding)

Fix any integral disjoint family of complete cycles.  Delete their owners
and subtract their lower and upper target incidences.  If the remaining
frame-specific nested-flow systems have integral target-frame demands and
are fractionally feasible, then all residual owners and flags can be
rounded integrally.

#### Proof

The fixed cycles give integral right-hand sides in the residual split
networks.  Apply Theorem 2.1, and Corollary 2.2 when both orientations are
required. \(\square\)

Thus integrality survives **after** the cycle decision, not through it.

---

## 6. Exact model classification

The coupled formulation has three blocks.

\[
\begin{array}{c|c|c}
\text{block}&\text{polyhedral type}&\text{integrality}\\ \hline
\text{fixed-frame nested prefixes}
 &\text{split-node network flow}&\text{TU}\\
\text{variable target-frame certificates}
 &\text{multiple-choice path cover}&\text{not TU for }H\ge2\\
\text{complete isometric cycles}
 &\text{hypergraph set packing}&\text{not TU already in }Q_3.
\end{array}                                           \tag{6.1}
\]

Accordingly the displayed full system is not an ordinary network, and its
natural owner-cycle block is not a matroid intersection formulation.  The
exact surviving positive route is a decomposition theorem:

1. choose or absorb an integral near-packing of complete cycles;
2. assign every remaining physical target certificate to a frame
   coherently;
3. verify the Hoffman cuts (3.1);
4. invoke Theorem 2.1 to obtain integral nested flags at no rounding loss.

Steps 1 and 2 are the only non-TU stages.  Step 3 is a fractional
feasibility question but no longer an integrality question.  This is the
sharpest integral reduction presently justified by the mixed-pair
owner-frame theorem.

## 7. Successor: exact target/frame coherence with a \(W^{o(1)}\) catalogue

The successor note
MATH_THEOREM_SCD_FLAG_LITERALIZATION_HOFFMAN_INTERFACE_20260726.md closes
Step 2 and the Hoffman verification exactly after enlarging the frame
catalogue to

\[
 J\le Cm\,4^H\exp(O(H^2/m))=W^{o(1)}
\]

in the calibrated range.  A symmetric-chain target-to-owner system is
fixed first; a random-frame union bound then gives every owner one balanced
frame literalizing its complete lower and upper flags.  The resulting
fixed target partitions have an explicit integral flow, so every Hoffman
cut holds with zero target exceptions.

That successor also proves a positive-density limitation on the original
polynomial random catalogue: every predeclared polynomial-size menu of
two-sided length-\(H\) flags serves only \(o(W)\) owners when
\(H/\log m\to\infty\).  Thus a polynomial-catalogue solution, if one
exists, must choose flags adaptively from an exponentially large implicit
family.  Complete-cycle grouping remains unresolved.
