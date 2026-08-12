# A global design/line-graph quotient for the extremal (k=11) branch

Date: 2026-07-25

## 1. Verdict

This note does **not** prove that a nonzero universal word of length (465)
exists or does not exist.  It gives a new exact global reduction, and then an
explicit certificate showing that a large middle-level/rank-seven quotient of
the hardest symmetric branch is feasible.

Assume the audited zero-margin normal form, and specialize to the branch

\[
E=132,
\qquad
V_Y=5\quad(Y\in\tbinom{[11]}4).
\tag{1.1}
\]

The previously proved parity-shadow theorem says that the (132) external
complementary five-sets form a simple (4)-\((11,5,2)\) design
\(\mathcal H\).  Put

\[
\mathcal K=\binom{[11]}5\setminus\mathcal H,
\qquad |mathcal K|=330.
\tag{1.2}
\]

The new conclusions are:

1. The external design graph (G=J(11,5)[\mathcal H]) is (5)-regular,
   and its (330) edges are canonically identified with the (330) members
   of \(\mathcal K\).
2. Under this identification, central transitions carrying a label in
   \(\mathcal H\) are exactly star-clique edges of the line graph (L(G)).
   More generally, the (3300) possible central Johnson transitions split
   into (132) colour classes (K_5) and (330) colour classes (K_4).
3. In any surviving six-path forest, at least (132-c-d\ge124) central
   transitions must be line-graph transitions with distinct vertices of
   (G) as labels.
4. These facts, exact component counts, the exact rank-five/rank-six
   inclusion matching, and the current rank-seven support and multiplicity
   bounds are simultaneously feasible.  An explicit certificate has:

   \[
   c=6,quad b_H=2,quad d=0,
   \]

   four external paths on (33) vertices each and two central paths on
   (152) and (178) vertices; all (456) edge-source labels are distinct;
   the six root-source labels complete them to all (462) five-sets; and

   \[
   z_7=323,qquad M_7=7,qquad
   \max_Qt_Q=4,qquad \Delta_7=133.
   \tag{1.3}
   \]

Thus a contradiction cannot use only the design shadow, path-component
counts, source-label injectivity, exact inclusion matching, and the existing
rank-seven (319/330) support theorem.  The next cut must use the physical
sliding reconstruction (rank four and below), endpoint offsets, or their
interaction with the upper hulls.

All claims in the explicit certificate are checked directly from stored
integer lists; the verifier does not trust a SAT solver output.

## 2. The design graph and its edge labels

Let \(\Omega=[11]\).  For \(B,B'\in\mathcal H\), join them in (G) when

\[
|B\cap B'|=4.
\]

Label this edge by

\[
\ell(BB')=\Omega\setminus(B\cup B')\in\binom\Omega5.
\tag{2.1}
\]

The design calculation already gives, for every five-set (S),

\[
r(S):=\#\{B\in\mathcal H:B\cap S=\varnothing\}
=2-\mathbf1_{\{S\in\mathcal H\}}.
\tag{2.2}
\]

### Theorem 2.1 (edge/central-vertex duality)

The graph (G) is (5)-regular, and

\[
\boxed{\ell:E(G)\longrightarrow\mathcal K}
\]

is a bijection.

#### Proof

If (B,B') are adjacent, their union has size six, so (2.1) is a
five-set disjoint from both.  It cannot lie in \(\mathcal H\), because a
design block has only one disjoint design block by (2.2), while it would be
disjoint from the two distinct blocks (B,B').  Thus the label lies in
\(\mathcal K\).

Conversely, if (D\in\mathcal K\), equation (2.2) gives exactly two design
blocks (B,B') disjoint from (D).  Both are five-subsets of the six-set
\(\Omega\setminus D\), so they intersect in four points and
\(\ell(BB')=D\).  This proves the bijection.  There are (330) edges on
(132) vertices, and every block contains five four-subsets, each selecting
one adjacent block.  Hence every degree is five. \(\square\)

### Corollary 2.2 (decomposition criterion)

The simple (4)-\((11,5,2)\) design \(\mathcal H\) is the disjoint union of
two (4)-\((11,5,1)\) designs if and only if (G) is bipartite.

Indeed, every four-set determines the edge joining the two design blocks
that contain it.  A bipartition places exactly one endpoint of every such
edge in each class, so each class contains every four-set exactly once.
Conversely, two disjoint index-one designs put the two blocks over each
four-set in opposite classes.  This criterion turns design decomposition
into an ordinary graph test.  The explicit certificate below uses the
bipartite case.

We henceforth identify a central vertex (D\in\mathcal K) with the edge
\(\ell^{-1}(D)\in E(G)\).

## 3. The exact line-graph decomposition of central transitions

For adjacent (D,D'\in\mathcal K), define their source colour

\[
\chi(DD')=\Omega\setminus(D\cup D').
\tag{3.1}
\]

This is the rank-five source between the two corresponding rank-six targets.

### Theorem 3.1 (star-clique theorem)

For (S\in\mathcal H), the five members of \(\mathcal K\) disjoint from
(S) are exactly the five edges of (G) incident with the vertex (S).
The central transitions of colour (S) are all ten pairs among those five
edges.  Consequently that colour class is the star (K_5) in (L(G)).

For (S\in\mathcal K), exactly four members of \(\mathcal K\) are disjoint
from (S), and its central colour class is the (K_4) on those four
vertices, with six candidate transitions.

Hence

\[
\boxed{
E(J(11,5)[\mathcal K])
=\bigsqcup_{S\in\mathcal H}E(K_5(S))
\sqcup
\bigsqcup_{S\in\mathcal K}E(K_4(S)),
}
\tag{3.2}
\]

and the two sides contain

\[
132\binom52+330\binom42=1320+1980=3300
\]

candidate transitions.

#### Proof

Fix (S\).  Every five-set disjoint from (S) is a facet of the six-set
\(\Omega\setminus S\), and any two distinct such facets meet in four points,
so every pair is a central Johnson transition of colour (S).

If (S\in\mathcal H), (2.2) says one of the six facets lies in
\(\mathcal H\), leaving five in \(\mathcal K\).  A member
(D\in\mathcal K) is disjoint from (S) exactly when the graph edge
labelled (D) has (S) as one endpoint, by Theorem 2.1.  This is the
star-clique assertion.

If (S\in\mathcal K), two of the six facets lie in \(\mathcal H\), leaving
four in \(\mathcal K\).  Finally every Johnson edge has the unique colour
(3.1), so the union is disjoint. \(\square\)

## 4. A global label-conservation cut

Complement the spanning six-set forest.  Its vertices are all (462)
five-sets, partitioned as \(\mathcal K\) (central) and \(\mathcal H\)
(external).  Every forest edge has one distinct rank-five source colour;
the (c) component-start sources are the (c) unused edge colours.

Let (h_0) be the number of component-start sources in \(\mathcal H\),
and let (i_H) be the number of interface-edge source colours in
\(\mathcal H\).

### Theorem 4.1 (forced line-transition count)

Every external-external edge has its source colour in \(\mathcal K\).
Therefore the number (k_H) of central-central transitions whose colour
lies in \(\mathcal H\) is exactly

\[
\boxed{k_H=132-h_0-i_H.}
\tag{4.1}
\]

In particular,

\[
\boxed{k_H\ge132-c-d\ge124.}
\tag{4.2}
\]

Under the identification \(\mathcal K=E(G)\), these are (k_H) consecutive
edge pairs sharing a vertex of (G), and no vertex of (G) is used twice as
their colour.

#### Proof

An external-external edge is an edge (BB') of (G), so Theorem 2.1 says
its source colour is \(\ell(BB')\in\mathcal K\).  Partition the (132)
colours in \(\mathcal H\) among central edges, interfaces, and component
starts.  This gives (4.1).  Since (h_0\le c\), (i_H\le d\), and
(c\le6,d\le2), (4.2) follows.  Source-colour injectivity and Theorem 3.1
give the last statement. \(\square\)

This is an order-sensitive global restriction on the central path: among its
edges-as-vertices, at least (124) successive pairs must genuinely continue
through distinct vertices of the external design graph.

## 5. Exact feasible quotient certificate

The certificate uses a simple design \(\mathcal H\) obtained as the union of
two disjoint copies of the unique Witt (4)-\((11,5,1)\) design.  The second
copy is obtained from the first by the coordinate permutation

```text
[4,9,2,8,5,10,6,0,7,1,3].
```

The checker verifies directly that every four-set occurs twice.  It then
checks the following data.

### External sector

A Hamilton cycle of the (5)-regular design graph is supplied.  Deleting
four equally spaced cycle edges produces four paths of (33) vertices, hence

\[
|F_E|=4\cdot32=128.
\tag{5.1}
\]

Their (128) source colours are exactly their (128) edge labels in
\(\mathcal K\).

### Central sector

The (330) vertices of \(\mathcal K\) are partitioned into two paths of
sizes (152) and (178).  Thus

\[
|F_C|=151+177=328.
\tag{5.2}
\]

Their colours split as

\[
126\text{ colours in }\mathcal H,qquad
202\text{ colours in }\mathcal K.
\tag{5.3}
\]

The (202) central colours in \(\mathcal K\) are exactly the complement of
the (128) external edge labels.  Hence all (456) forest-edge source
colours are distinct.  The six unused colours are

```text
1173 929 1564 782 31 598
```

and are all in \(\mathcal H\).

### Perfect inclusion matching

The six path roots and their unused sources are

```text
root D   source S
810      1173
1102     929
227      1564
241      782
1417     598
1952     31
```

Every displayed pair is disjoint.  Orient each path away from its root.  If
(D\to D') is an oriented forest edge with colour
(S=\Omega\setminus(D\cup D')\), set

\[
M(S)=\Omega\setminus D'.
\tag{5.4}
\]

At a root use its displayed source and set (M(S)=\Omega\setminus D).
The verifier proves that (5.4) is a bijection from all (462) five-sets to
all (462) six-sets, with (S\subset M(S)).  It also recomputes the exact
added-coordinate histogram

\[
42^{11}.
\tag{5.5}
\]

### Rank-seven hull ledger

For a complemented-forest edge (DD'), its rank-seven hull complement is
(Y=D\cap D').  Direct counting over all (456) edges gives

\[
\#\{Y:t_Y=1\}=212,quad
\#\{Y:t_Y=2\}=91,quad
\#\{Y:t_Y=3\}=18,quad
\#\{Y:t_Y=4\}=2.
\tag{5.6}
\]

Thus the support is (323), seven colours are missing, and

\[
\Delta_7=91+2\cdot18+3\cdot2=133
=132-c+M_7.
\tag{5.7}
\]

The certificate therefore satisfies the exact duplicate identity, the
(319/330) support bound, the eleven-hole bound, and the multiplicity-six
cap with room to spare.  Since every four-set belongs to exactly two design
blocks, it also has (V_Y=5) for every (Y), as required by (1.1).

## 6. Symmetry-reduced SAT formulation

After fixing the design and the external four-path forest, only the (3300)
candidate transitions in (3.2) are primary variables.  The exact quotient
formula enforces:

1. one transition for each of the (202) available \(\mathcal K\)-colours;
2. one transition for each of the (126) nonroot \(\mathcal H\)-colours;
3. degree one or two at every central vertex;
4. all but at most eleven rank-seven hull colours present;
5. the two prescribed central root sources occurring at central endpoints;
6. no central cycle.

The final generated instance before solving had

```text
3310 variables
388685 clauses
```

including six exact cycle cuts.  This SAT run was used only to discover the
lists.  The promoted theorem is the direct certificate check in Section 5,
which reconstructs and verifies every asserted object independently.

## 7. What the certificate does not realize

The quotient is deliberately weaker than a physical OR word.  In particular
it does not yet provide:

* a single central entry word (A_0,\ldots,A_{332}) of ranks at most three;
* the ordinary rank-four pair and rank-five triple sliding identities;
* near-complete lower rank-four forest colours;
* the exact endpoint-offset state schedule;
* external anchor entries and their directed occurrence offsets; or
* literal intervals for the abstract forest edges.

Indeed, the certified quotient's lower rank-four intersection support is
only (286/330).  Thus it is not a model of the audited equality template.
That failure is informative: the upper (323/330) hull system, exact middle
matching, and global source-label conservation can all coexist, while the
lower sliding reconstruction is where this particular model breaks.

There is an exact local test for that break.  Orient an alternating path as

\[
S_0,U_0,S_1,U_1,\ldots,S_r,U_r,
\]

and put

\[
B_i=S_i\cap S_{i+1},qquad
A_i=B_{i-1}\cap B_i.
\tag{7.1}
\]

Every (B_i) is automatically a four-set: (S_i,S_{i+1}) are distinct
facets of (U_i).  At an ordinary internal position,

\[
|A_i|=3\quad\Longleftrightarrow\quad B_{i-1}\ne B_i.
\tag{7.2}
\]

When the two neighboring instances of (7.2) hold,

\[
A_i\cup A_{i+1}=B_i
\quad\Longleftrightarrow\quad A_i\ne A_{i+1}.
\tag{7.3}
\]

These follow because distinct codimension-one facets of a fixed set have
union equal to that set.  Iterating (7.2)--(7.3) reconstructs the ordinary
rank-three entries, rank-four pairs, rank-five triples, and rank-six
four-windows.  Thus the physical central condition is a two-level
non-laziness constraint on the exact quotient path, not an unspecified mask
condition.

For the explicit certificate, the two central paths have respectively

```text
source vertices       178   152
adjacent equal B's      35    19
adjacent equal rank-3 A's 22  32
```

so it fails already at (7.2), well before endpoint-offset realization.
This identifies the next SAT layer precisely: forbid lazy (B)-turns and
lazy (A)-turns while retaining both extreme-shadow support bounds.

The sharpened remaining gate in the (E=132,V_Y=5) branch is therefore:

> Find or exclude a two-path ordering of the (330=|E(G)|) central vertices
> satisfying the line-graph count (4.2), the complementary colour bijection,
> **both** near-complete rank-four and rank-seven shadows, and the rank-at-most-
> three sliding reconstruction across the seam.

This is a finite (330)-vertex coloured path problem, not a raw search over
(465) arbitrary eleven-bit entries.

## 8. Reproduction

Run

```text
python3 scratch/verify_k11_design_branch_quotient_certificate.py
```

Expected output:

```text
PASS
design: 4-(11,5,2), blocks=132
external graph: vertices=132 edges=330 degree=5
external forest: components=4 edges=128
central forest: components=2 edges=328 sizes=152,178
central label split: H=126 K=202; all 456 labels distinct
rank-seven hulls: support=323 missing=7 max-multiplicity=4 excess=133
perfect inclusion matching: 462 sources/targets, added-coordinate degree 42
lower rank-four colours: support=286 missing=44 max-multiplicity=4
central local defects: (178,35,22) (152,19,32)
```

```text
bbfc114954377a79c6d7757ca4077cc8a84fd31d5ddd27508c557b3b75b90a03  scratch/k11_design_branch_quotient_sat.py
32a69bc4112209f3517a6a31bcbc41a16c778e4792549ea8c2c961cca79ec3ff  scratch/verify_k11_design_branch_quotient_certificate.py
```

No internet lookup is used anywhere in this result.

## 9. Exact status

Proved here:

* the design/edge duality \(\mathcal K\cong E(G)\);
* the line-graph and (K_4) colour-class decomposition (3.2);
* the forced (124)-transition global cut (4.2);
* an exact six-component, perfect-inclusion-matching quotient satisfying all
  current rank-seven support, multiplicity, and duplicate ledgers.

Not proved:

* feasibility of the simultaneous lower rank-four shadow;
* physical sliding-word reconstruction;
* a length-(465) universal word;
* or impossibility of such a word.

Thus the certified numerical frontier remains

\[
\boxed{465\le\nu(11)\le477}.
\]
