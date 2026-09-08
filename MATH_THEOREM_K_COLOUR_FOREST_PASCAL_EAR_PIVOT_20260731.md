# The colour-forest / Pascal-ear pivot and the exact block-coherent lift gate

Date: 2026-07-31  
Status: exact occurrence-level equivalence and audited local obstruction;
no all-dimensional physical construction is claimed

## 1. Purpose and notation

Put

\[
 M=\binom{2m}{m},\qquad N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname {Cat}_m.
\]

Let \(B_m\) be the inclusion graph between
\(\mathcal L=\binom{[2m]}{m-1}\) and
\(\mathcal U=\binom{[2m]}{m+1}\).  An incidence \(L\subset U\) has the
unique physical lift

\[
 \psi(L,U)=\{L+a,L+b\},\qquad U\setminus L=\{a,b\},               \tag{1.1}
\]

which is an edge of \(J(2m,m)\).  For an inclusion subgraph \(H\), write
\(F(H)\) for the union of these physical edges.

The abstract forest theorem constructs a spanning
\(H=Q\mathbin{\dot\cup}S\subset B_m\), where both shore-degree profiles
are \(1^{N-K}2^K\), \(Q\) is a perfect matching, and \(H\) is a union of
balanced paths.  The Pascal/Boolean-square ledger instead records triples
\((X,d,h;i)\) consisting of an omitted middle facet, a removed duplicate
lower colour, an inserted hole colour, and a physical host occurrence.
This note identifies the exact map between these objects and the exact
information that is not shared by them.

## 2. Matching complement and the true contiguity test

### Lemma 2.1 (the complement is a matching)

Suppose every vertex of \(H\) has degree one or two and \(Q\) is a
perfect matching of \(H\).  Then \(S=E(H)\setminus Q\) is a matching of
size \(K\), joining precisely the degree-two vertices on the two shores.
Moreover, \(Q\) is the unique perfect matching of \(H\) if and only if
\(H\) is a disjoint union of balanced paths.

#### Proof

Every degree-one vertex uses its unique edge in \(Q\).  Every degree-two
vertex uses one \(Q\)-edge and has exactly one residual edge.  Hence the
residual edges are pairwise disjoint and meet exactly the degree-two
vertices.  There are \(K\) of those on either shore, so \(|S|=K\).
The uniqueness assertion is the standard alternating path/cycle
decomposition: a balanced path has one perfect matching and an even cycle
has two. \(\square\)

Fix a degree-two upper colour \(U\), and write its two lower neighbours as
\(h_U\) on the \(Q\)-edge and \(\alpha_U\) on the \(S\)-edge.

### Lemma 2.2 (wedge criterion)

The two occurrences of \(U\) form one literal cap-two block -- equivalently,
their lifted Johnson edges are contiguous and share a middle vertex -- if
and only if

\[
             |h_U\cap\alpha_U|=m-2.                         \tag{2.1}
\]

When (2.1) holds, their unique common middle endpoint is

\[
                         X_U=h_U\cup\alpha_U.                \tag{2.2}
\]

#### Proof

A common rank-\(m\) endpoint must contain both rank-\((m-1)\) lower
labels.  Since the labels are distinct, such an endpoint exists exactly
when their union has rank \(m\), equivalently when their intersection has
rank \(m-2\).  In that case the union is the unique common endpoint.
\(\square\)

Thus palette bijectivity, cap-two multiplicity, and squarefreeness of the
two labels do **not** imply block contiguity.  Already at \(m=3\), with

\[
 U=\{1,2,3,4\},\qquad h=\{1,2\},\qquad \alpha=\{3,4\},       \tag{2.3}
\]

the lifted edges are

\[
 \{123,124\},\qquad \{134,234\},                            \tag{2.4}
\]

and are disjoint.  This is the smallest literal local obstruction to the
missing block condition.

## 3. The three-facet pivot

Assume (2.1).  In the common upper block write

\[
 U=R\mathbin{\dot\cup}\{a,b,c\},\qquad |R|=m-2,
\]

so that, after naming the two outer middle vertices according to a chosen
orientation,

\[
 C^- =R+\{b,c\},\qquad X_U=R+\{a,c\},\qquad
 C^+=R+\{a,b\}.                                           \tag{3.1}
\]

If \(Q\) selects the outgoing occurrence \(X_UC^+\), then

\[
 \alpha_U=C^-\cap X_U=R+c,\qquad
 h_U=X_U\cap C^+=R+a,\qquad
 d_U=C^-\cap C^+=R+b.                                    \tag{3.2}
\]

Equivalently, without the coordinate names,

\[
 d_U=(h_U\cap\alpha_U)
       \cup\bigl(U\setminus(h_U\cup\alpha_U)\bigr).       \tag{3.3}
\]

This is the exact reconciliation:

* the full colour-incidence graph sees the two edges
  \(\alpha_U-U\) and \(h_U-U\);
* the directed Boolean-square repair graph sees the edge \(d_U-h_U\),
  labelled by \((X_U,U)\).

Thus a repair ear is obtained by the local pivot

\[
                         \alpha_U\longmapsto d_U           \tag{3.4}
\]

with \(h_U\) fixed.  It is not the same edge, and path components are not
preserved under this pivot.

### Lemma 3.1 (contracted base word)

Suppose \(F(H)\) is a Hamilton cycle and (2.1) holds at all \(K\)
degree-two upper colours.  Orient the cycle so that \(Q\) chooses the
outgoing occurrence at every such block, and contract all \(X_U\).  The
lower-colour multiset \(B\) of the resulting saturating cycle is

\[
 B=\mathcal L-\{h_U: \deg_H U=2\}+\{d_U:\deg_H U=2\}.      \tag{3.5}
\]

It has profile \(0^K1^{N-2K}2^K\) if and only if the \(d_U\) are
pairwise distinct and

\[
             \{d_U\}\cap\{h_U\}=\varnothing.             \tag{3.6}
\]

#### Proof

The \(Q\)-edges enumerate \(\mathcal L\).  At a doubled upper block,
contraction removes its selected occurrence of colour \(h_U\) and replaces
the two-edge block by the base edge of colour \(d_U\), proving (3.5).
The \(h_U\) are already distinct because \(Q\) is a matching.  In (3.5),
exactly \(K\) zeros and \(K\) twos occur precisely when none of the removed
colours is reinserted and the inserted colours are distinct. \(\square\)

## 4. Exact block-coherent forest equivalence

Call \((H,Q)\) a **directed block-coherent colour-forest certificate** when:

1. both shore-degree profiles of \(H\) are \(1^{N-K}2^K\), and \(H\) is
   a balanced linear forest with unique matching \(Q\);
2. \(F(H)\) is a spanning connected two-regular graph, hence a Hamilton
   cycle on rank \(m\);
3. the wedge condition (2.1) holds at every degree-two upper colour;
4. in one cyclic orientation of \(F(H)\), every \(Q\)-edge in a doubled
   block points away from its common endpoint \(X_U\); and
5. the pivot labels satisfy (3.6).

Condition 2 is physical Johnson degree two and topology.  Condition 3 is
the corrected contiguity condition.  Condition 4 is orientation coherence,
not a consequence of forest parity.  Condition 5 is the contracted-base
floor ledger.

### Theorem 4.1 (P-respecting equivalence)

Directed block-coherent colour-forest certificates are in bijection with
the following data whose full occurrence graph is a balanced linear
forest:

* a saturating cycle on all upper colours;
* one distinct omitted middle facet hosted in each of \(K\) cap-two
  blocks;
* a uniform outgoing repair of an exact
  \(0^K1^{N-2K}2^K\) base word;
* pairwise distinct incoming split colours; and
* the associated rigid \(P\)-respecting lower/upper diamond-tight
  enumeration.

Under the bijection, the \(K\) Boolean-square repair triples are

\[
                       (X_U,d_U,h_U;U),                    \tag{4.1}
\]

and they form a three-shore perfect matching.

#### Proof

Starting from \((H,Q)\), Conditions 2 and 3 make every doubled upper
colour one contiguous wedge \(C^-X_UC^+\).  A Hamilton vertex cannot be
the common endpoint of two different wedges, so the \(X_U\) are distinct.
Contract them.  Every upper colour remains exactly once, and the remaining
middle vertices are distinct, giving a saturating cycle.  Condition 4
makes \(Q\) uniformly outgoing.  Lemma 3.1 and Condition 5 give the exact
base floor and show that replacing every \(d_U\) by \(h_U\) restores
\(\mathcal L\).  The incoming colours \(\alpha_U\) are pairwise distinct
because \(S=H\setminus Q\) is a matching.  Formula (3.2) is the literal
Boolean-square geometry, so (4.1) covers every omitted facet, duplicate,
and hole once.

For the three-level enumeration, put the lower insertion on \(Q\), the
upper insertion on the blockwise complement of \(Q\), and put both on
the sole edge of every degree-one upper block.  This is exactly the rigid
diamond rule; all lower, middle, and upper vertices occur once.

Conversely, expand every hosted saturating block through its omitted
facet and let \(H\) be the occurrence-colour graph of the resulting middle
cycle.  The retained outgoing edges give \(Q\), while the incoming edges
give \(S\).  Exact lower and upper palettes give the two degree profiles;
the assumed balanced-forest qualifier makes \(Q\) unique.  Literal hosting
gives Conditions 2--4, and the exact base floor gives Condition 5 by
Lemma 3.1.  The constructions reverse each other occurrence for
occurrence. \(\square\)

The balanced-forest qualifier is a uniqueness/peeling certificate, not a
necessary condition for a directed repair: a repair may have an
occurrence graph with alternating cycles and hence several common
transversals.

## 5. Which leaf peeling transfers, and which does not

Let \(\mathscr R\) be the **full** occurrence-labelled repair atlas of the
contracted saturating cycle: it contains every physically legal triple
\((X,d,h;i)\), not only the \(K\) selected triples (4.1).  A matched Pascal
square is the same object after retaining its direct-step and host labels;
the square reconstruction formulas recover \((X,d,h;i)\).  Hence the
Pascal-square atlas and \(\mathscr R\) are occurrence-isomorphic once a
physical block map is fixed.

### Proposition 5.1 (exact unitriangular criterion)

For a fixed selected matching \(e_j=(X_j,d_j,h_j;i_j)\) of \(\mathscr R\),
the full atlas is leaf-peelable along this matching if and only if the
indices can be ordered so that, after deleting all shores used by
\(e_1,\ldots,e_{j-1}\), at least one of \(X_j,d_j,h_j\) is incident with
no remaining legal square other than \(e_j\).

This condition is preserved verbatim under the occurrence-labelled
Pascal-square identification.

#### Proof

This is the degree-one peeling definition applied after each matched
triple is removed.  Occurrence-labelled square reconstruction is a
bijection on triples and preserves incidence with every shore vertex, so
it preserves the condition in both directions. \(\square\)

By contrast, leaf peeling of the full colour graph \(H\) does **not**
transfer through (3.4).  It peels alternating paths built from
\(Q\)- and \(S\)-occurrences \(h_U-U\) and \(\alpha_U-U\).  Proposition
5.1 peels a different hypergraph whose incidences are
\(X_U,d_U,h_U\), including alternative hosts absent from \(H\).  Thus a
balanced-colour-forest peeling order does not, by itself, furnish a
repair/Pascal-atlas peeling order.  The two properties live on different
incidence systems, and no componentwise equivalence exists.  This
statement deliberately does not assert that their Boolean truth values
can never coincide; they do coincide in the positive \(m=3\) fixture
below.

The exact additional recursive invariant is **pivot-unitriangularity**:
Conditions 2--5 of Theorem 4.1 together with the order in Proposition
5.1.  The abstract forest theorem supplies none of physical degree two,
wedge contiguity, uniform sign, pivot-floor separation, or
pivot-unitriangularity.

## 6. Independent finite audit

The dependency-free replay

```text
python3 scratch/audit_k_colour_forest_pascal_ear_pivot_20260731.py
```

checks the positive \(m=3\) directed fixture occurrence for occurrence.
It verifies all five local pivots (3.2), the exact base identity (3.5),
the selected three-shore matching (4.1), and the local non-wedge
(2.3)--(2.4).

The full occurrence-colour forest has edge-component census

\[
                    7P_1\ \dot\cup\ P_3\ \dot\cup\ 2P_5, \tag{6.1}
\]

whereas the complete duplicate--hole repair projection has

\[
                         2P_1\ \dot\cup\ P_5.             \tag{6.2}
\]

Both happen to be peelable, but the different component decompositions
give an exact physical counterexample to any componentwise identification
of colour-forest ears with repair ears.  It does not claim that one of the
two peelability properties fails in this fixture.

Artifact hashes:

* `scratch/audit_k_colour_forest_pascal_ear_pivot_20260731.py` --
  `8ae1889ffcd080197bd6e5023303eb11d7c2e3544067e237157404ecf3c25cd6`;
* `scratch/k_colour_forest_pascal_ear_pivot_20260731.audit.json` --
  `b1f61545b8c8db38735610a039f826a2a2bac21f614a42021f682014f0bc182e`.

## 7. Exact remaining induction gate

A synchronized GMM/BTK recursion may therefore work with an abstract
balanced forest only if it simultaneously proves:

1. the lifted incidences have physical Johnson degree two and one-cycle
   topology;
2. each doubled upper row obeys the local intersection equation (2.1);
3. all \(K\) selected wedges have one cyclic sign;
4. the pivot labels (3.3) are distinct and avoid the selected \(h\)-bank;
5. the resulting Pascal-square/repair atlas is pivot-unitriangular, or at
   least has a perfect matching; and
6. the recursion retains the rigid blockwise-opposite lower/upper diamond
   rule.

This is stronger than the known one-port \(K-1\) count obstruction: even a
putative \(K\)-port palette-perfect recursion can fail locally at (2.1),
globally at physical degree two, or after the three-facet pivot.  The note
does not rule out a modified bulk recursion satisfying these conditions.
