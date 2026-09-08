# Block-coherent Catalan bulk glue: partner, degree, ear, and topology criteria

Date: 2026-07-31  
Status: exact one-step construction theorem and two literal local
obstructions; no all-dimension existence theorem

## 0. Verdict

The \(K\)-square modification of the Gregor--Mütze one-port splice has a
clean constructive form, but it requires more than two palette bijections
and squarefree labels.

For every new direct occurrence one must identify its **unique physical
same-upper-colour partner**.  If that partner is retained in the tagged
child, the square orientation is forced: its vertical edge must use the
free endpoint of the old contiguous two-edge block.  Thus the recursive
input is a matching of free block ports, not merely the facet-pair hitting
condition of the earlier audit.

Under an exact free-port matching, two palette identities, and one
fragment-connectivity test, switching all
\(K=\operatorname{Cat}_m\) direct edges gives

* a physical Johnson two-factor, and one cycle exactly when the fragment
  graph is connected;
* literal contiguous cap-two blocks;
* a common lower/upper transversal;
* a rigid \(P\)-respecting three-level diamond enumeration; and
* an occurrence-colour graph consisting of \(K\) disjoint three-edge
  paths and isolated matching edges.

The last point is a colour-transversal peeling statement.  It is not by
itself leaf peeling of the full duplicate--hole repair atlas.  The two
graphs are related by a three-facet pivot.  Uniform directed sign, the
floor property of the contracted base word, and pivot-unitriangularity
remain additional conditions.

Two sharply scoped obstructions survive after replacing one port by
\(K\) ports.

1. A direct block can meet the central cycle at its block centre but not at
   its free endpoint.  The old candidate test passes, but every available
   square destroys contiguity.
2. Two adjacent doubled blocks can have the same free endpoint.  Both
   required central incidences may exist, but simultaneous switching asks
   for the same vertical cube edge twice.

These obstruct the all-direct-edge Pascal-square fibre, not arbitrary
nonlocal rethreadings.  The published recursion maintains none of the
free-port matching, the two palettes, or the fragment monodromy.

## 1. Central Pascal split

Put

\[
 n=2m-1,\qquad k=m-1,
\]

and let \(z\) be the new coordinate.  Write

\[
 A=\binom nk,\qquad B=\binom n{k-1},\qquad
 K=A-B=\operatorname{Cat}_m.
\tag{1.1}
\]

Let \(C_0\) be a tight enumeration of levels \(k,k+1\) of \(Q_n\).
At the central odd dimension it alternates between the two levels.  Let
\(C_1\) be a tight enumeration of levels \(k-1,k\), and suppress its
rank-\((k-1)\) vertices.  The resulting Hamilton cycle
\(\widehat C_1\) on rank \(k\) has exactly \(K\) direct Johnson steps.

For one direct step write

\[
 d_i=a_i b_i,\qquad x_i=a_i\cup b_i.
\tag{1.2}
\]

Suppose \(C_0\) uses the containment incidence \(b_i-x_i\).  If \(y_i\)
is the other rank-\((k+1)\) neighbour of \(b_i\) on \(C_0\), the Pascal
square is

\[
 \{b_i0-x_i0,\ a_i1-b_i1\}
 \longmapsto
 \{b_i0-b_i1,\ x_i0-a_i1\}.
\tag{1.3}
\]

The new direct edge

\[
 D_i=x_i0-a_i1
\tag{1.4}
\]

has upper colour \(z+x_i\) and lower colour \(a_i\).  The lower row
\(b_i0\) now projects to the distinguished edge

\[
 E_i=y_i0-b_i1,
\tag{1.5}
\]

whose upper colour is \(z+y_i\) and lower colour is \(b_i\).

Each square preserves vertex degree and replaces flip lengths \(1+2\)
by \(1+2\).  This does not imply that \(D_i\) is contiguous with the
distinguished occurrence of colour \(z+x_i\).

## 2. Exact physical partner theorem

Assume a physically compatible family of all \(K\) squares, an exact
distinguished upper palette, and pairwise distinct \(x_i\).  Let
\(\mathcal R\) be the distinguished projected edges retained from
\(C_1\), with \(z\) deleted from their labels.  Exactness says

\[
 \{y_i:i\in[K]\}\mathbin{\dot\cup}
 \{u(e):e\in\mathcal R\}
 =\binom{[n]}{k+1}.
\tag{2.1}
\]

### Theorem 2.1 (unique-partner incidence)

The doubled occurrence of colour \(z+x_i\) is a literal contiguous
two-edge block if and only if exactly one of the following holds.

1. There is a unique \(j\) with \(y_j=x_i\).  Then \(E_j\) is its
   distinguished partner and shares \(x_i0\) with \(D_i\).
2. The label \(x_i\) belongs to the retained bank \(\mathcal R\), and
   its unique retained occurrence is incident with \(a_i1\).

If the output is one physical cycle, the two occurrences in case 1 are
automatically distinct.

#### Proof

By (2.1), \(z+x_i\) has a unique distinguished occurrence.  If
\(x_i=y_j\), it is \(E_j=x_i0-b_j1\), which meets
\(D_i=x_i0-a_i1\) at \(x_i0\).

Otherwise it is a retained tagged edge \(p1-q1\) with \(p\cup q=x_i\).
Such an edge cannot meet \(x_i0\), which lies in the other sector.  It
meets \(D_i\) exactly when \(a_i\in\{p,q\}\).  These exhaust (2.1).

If case 1 gave the same projected endpoints, the full enumeration would
contain the isolated triangle
\(x_i0-a_i1-a_i0-x_i0\), impossible in a spanning one-cycle output.
\(\square\)

The arcs

\[
 j\longrightarrow i\quad\Longleftrightarrow\quad y_j=x_i
\tag{2.2}
\]

form a partial permutation.  This **block-partner graph** is not the
lower--upper occurrence-colour forest.

## 3. Rooted block packages and forced ports

Call \(C_1\) a **rooted \(K\)-block child** when:

1. its direct edges are \(d_i=a_i b_i\), with distinct unions
   \(x_i=a_i\cup b_i\);
2. a distinguished projected edge \(a_i c_i\) is consecutive with
   \(d_i\) at \(a_i\) and has the same union \(x_i\);
3. the distinguished union labels of \(C_1\) are pairwise distinct; and
4. the free endpoints \(b_i\) are pairwise distinct.

Thus \(a_i\) is the block centre and \(b_i\) is its free endpoint.

### Lemma 3.1 (forced-free-port necessity)

Inside the all-direct-edge square fibre, preserving the rooted block

\[
 c_i-a_i-b_i
\tag{3.1}
\]

forces the square for \(d_i\) to use \(b_i-x_i\).  Consequently a
simultaneous block-preserving bank requires

\[
 b_i-x_i\in E(C_0)\quad(i\in[K]),\qquad
 b_i\ne b_j\quad(i\ne j).
\tag{3.2}
\]

#### Proof

Using vertical endpoint \(b_i\) replaces \(a_i1-b_i1\) by
\(x_i0-a_i1\).  The retained partner \(a_i1-c_i1\) survives, so the two
occurrences remain adjacent at \(a_i1\).

Using vertical endpoint \(a_i\) instead makes the new direct edge incident
with \(b_i1\), while the retained partner remains incident with \(a_i1\).
Contiguity is lost.  If two forced ports coincide, both squares request
the same vertical edge \(b0-b1\).  Keeping one copy leaves degree one at
both vertices after two incident edges were removed; keeping two copies
creates a forbidden parallel cube edge. \(\square\)

This strengthens

\[
 \{a_i,b_i\}\cap N_{C_0}(x_i)\ne\varnothing.
\tag{3.3}
\]

Literal blocks require the specified incidence
\(b_i\in N_{C_0}(x_i)\).

## 4. Exact topology

Delete all \(b_i0-x_i0\) from \(C_0 0\) and all \(a_i1-b_i1\) from
\(C_1 1\).  Each tagged cycle becomes \(K\) path fragments, allowing
one-vertex fragments when cuts are adjacent.  Contract every fragment and
retain the \(2K\) new edges in (1.3).  Call the resulting bipartite
two-regular multigraph \(\mathfrak F\).

### Lemma 4.1 (fragment monodromy)

After the all-\(K\) switch every physical vertex has degree two.  Its
cycle components correspond canonically to the components of
\(\mathfrak F\).  Hence the result is one cycle if and only if

\[
 \mathfrak F\text{ is connected}.
\tag{4.1}
\]

#### Proof

Every removed edge contributes boundary ports to adjacent fragments, and
the \(2K\) new edges pair all ports.  Every contracted fragment therefore
has degree two.  Contracting or expanding a path fragment preserves
components. \(\square\)

## 5. Constructive rooted bulk-glue theorem

For a lower row \(r\) of \(C_0\), let \(q_0(r)\) be the union of its two
rank-\((k+1)\) neighbours.  Let \(\mathcal R\) be the \(B\) distinct
distinguished union labels of \(C_1\).

### Theorem 5.1 (rooted Catalan bulk glue)

Assume \(C_1\) is a rooted \(K\)-block child.  Assume \(C_0\) contains
\(\{b_i-x_i:i\in[K]\}\), and let \(y_i\) be the other neighbour of
\(b_i\).  Suppose

\[
 \{q_0(r):r\notin\{b_i:i\in[K]\}\}
 =\binom{[n]}{k+2}
\tag{5.1}
\]

and

\[
 \mathcal R\mathbin{\dot\cup}\{y_i:i\in[K]\}
 =\binom{[n]}{k+1}.
\tag{5.2}
\]

Both are multiplicity-one identities.  If \(\mathfrak F\) is connected,
all \(K\) forced Pascal squares produce a tight Hamilton enumeration of
levels \(k,k+1\) of \(Q_{n+1}\), whose projected middle cycle \(P\)
satisfies:

1. the lower distinguished edges and their upper colours are exact
   transversals;
2. the direct edge \(D_i=x_i0-a_i1\) is contiguous with the retained
   partner \(a_i1-c_i1\), both of upper colour \(z+x_i\);
3. the direct lower colours \(a_i\) are pairwise distinct, so both
   occurrence-load profiles are \(1^{N-K}2^K\), where
   \(N=\binom{2m}{m+1}=mK\);
4. the common-transversal occurrence graph is
   \[
       KP_4\mathbin{\dot\cup}(N-2K)P_2;
   \tag{5.3}
   \]
5. the blockwise complementary upper transversal gives a rigid
   cap-two \(P\)-respecting tight enumeration of ranks \(k,k+1,k+2\);
6. contracting the \(i\)-th block centre gives the literal repair triple
   \[
   (X_i,d_i,h_i;U_i)
    =\bigl(z+a_i,\ c_i,\ z+(a_i\cap c_i);\ z+x_i\bigr).
   \tag{5.4}
   \]

The triples in (5.4) form a duplicate--hole perfect matching exactly when
the \(c_i\) are pairwise distinct.  A uniformly directed repair
additionally requires all doubled blocks to have the same cyclic sign.

#### Proof

Distinct free ports make all supports simple and edge-distinct.  Every
square preserves degree; Lemma 4.1 and connectedness give one physical
cycle.  The two input cycles partition the target vertices by their last
bit, and (1.3) preserves total flip length, so the output is tight.

Every lower vertex still subdivides one projected edge.  Thus the lower
palette is automatic.  Identity (5.1) is the no-\(z\) upper bank, while
(5.2) is the \(z\)-containing bank.  This proves the common transversal.

The retained \(a_i1-c_i1\) has union \(z+x_i\) and shares \(a_i1\) with
\(D_i\), proving literal contiguity.  The centres \(a_i\) are distinct:
the two incident projected-cycle edges at a centre are already the direct
edge and its partner.  Hence \(\ell(D_i)=a_i\) are distinct, proving both
floor profiles.

Let \(Q\) be the common transversal.  At upper colour \(z+x_i\), its
selected occurrence is the retained partner and has lower colour
containing \(z\).  The unselected \(D_i\) has lower colour \(a_i\),
which avoids \(z\).  The \(Q\)-edge at \(a_i\) cannot end at another
\(z+x_j\), because that upper colour is already \(Q\)-matched to a
\(z\)-containing lower colour.  Thus every \(D_i\), together with its
two incident \(Q\)-edges, is an isolated \(P_4\).  The remaining
\(Q\)-edges are isolated, proving (5.3).

The blockwise opposite upper transversal gives the standard rigid diamond
expansion.  For (5.4), the selected partner has lower colour

\[
 h_i=z+(a_i\cap c_i),
\]

the direct edge has lower colour \(\alpha_i=a_i\), their common upper
colour is \(U_i=z+x_i\), and the three-facet pivot is

\[
 (h_i\cap\alpha_i)
 \cup\bigl(U_i\setminus(h_i\cup\alpha_i)\bigr)=c_i.
\tag{5.5}
\]

The omitted middle state is \(X_i=z+a_i\).  The \(X_i,h_i,U_i\) are
already pairwise distinct, so (5.4) covers all three repair shores exactly
when the \(c_i\) are distinct.  Uniform direction is exactly common local
block sign. \(\square\)

### Corollary 5.2 (exact rooted-fibre criterion)

Fix the two input cycles and insist that every retained block partner
survive.  An all-direct-edge Pascal-square output is a literal cap-two
common-refinement Hamilton cycle if and only if:

1. every forced \(b_i-x_i\) occurs in \(C_0\);
2. the \(b_i\) are distinct;
3. (5.1)--(5.2) hold; and
4. \(\mathfrak F\) is connected.

Physical Johnson degree two, both occurrence-colour floor profiles, and
the colour-forest peeling (5.3) then follow automatically.  A directed
floor-repair package additionally needs distinct \(c_i\) and one common
cyclic sign.  Leaf peeling of the full repair atlas is separate.

#### Proof

Necessity is Lemma 3.1, sectorwise upper-colour exactness, and Lemma 4.1.
Theorem 5.1 proves sufficiency and the automatic conclusions. \(\square\)

## 6. Two minimal local obstructions

Both examples live on old ground \([5]\), with \(k=2\), and are replayed
by the script cited in Section 9.

### 6.1 Centre-only hit

Let

\[
 x=123,\qquad a=23,\qquad b=12,\qquad c=13.
\]

The child block is \(c-a-b\), with centre \(a\) and free endpoint \(b\).
Suppose the two \(C_0\)-neighbours of \(x\) are \(a,c\).  Then

\[
 \{a,b\}\cap N_{C_0}(x)=\{a\},
\]

so (3.3) passes, but \(b-x\) is absent.  The available centre square
destroys contiguity.

### 6.2 Free-port bow-tie

Consider the child segment

\[
 23,\ 13,\ 12,\ 24,\ 14.
\tag{6.1}
\]

The first block has colour \(123\), direct edge \(13-12\), centre \(13\),
and free endpoint \(12\).  The second has colour \(124\), direct edge
\(12-24\), centre \(24\), and the same free endpoint \(12\).  Let
\(C_0\) contain

\[
 123,\ 12,\ 124.
\tag{6.2}
\]

Every direct edge is individually block-switchable, both direct unions
are distinct, and both required incidences occur.  Simultaneous switching
asks twice for \(12\,0-12\,1\).  One copy leaves both endpoints at degree
one; two copies are a forbidden parallel physical cube edge.

Thus a \(K\)-port bank with every direct step locally eligible can still
fail before palettes or topology are tested.  This is strictly stronger
than the one-port \(K-1\) count obstruction within this fibre.

## 7. Abstract colour forest versus Boolean-square repair ears

The palette identities produce a common matching \(Q\), and the \(K\)
direct Johnson edges are its nonmatching colour incidences.  The rooted
new-coordinate split forces the colour-forest decomposition (5.3).
Literal cap-two additionally requires the physical wedge condition of
Theorem 2.1, and Hamiltonicity is the separate fragment condition (4.1).

At one doubled block the exact pivot is

\[
 \alpha_i=a_i,\qquad h_i=z+(a_i\cap c_i),\qquad
 U_i=z+x_i,\qquad d_i=c_i.
\tag{7.1}
\]

The colour graph sees \(\alpha_i-U_i\) and \(h_i-U_i\); the repair atlas
sees \(d_i-h_i\), labelled by \((X_i,U_i)\).  Therefore the \(P_4\)
components in (5.3) must not be identified componentwise with paths in
the duplicate--hole graph.

Let \(\mathscr R\) be the full occurrence-labelled repair/Pascal atlas,
including every alternative host.  A chosen matching (5.4) is
leaf-peelable in \(\mathscr R\) exactly when its triples can be ordered so
that, after earlier matching vertices are deleted, one of
\(X_i,d_i,h_i\) has no remaining incident atlas edge except the selected
one.  This independent property is **pivot-unitriangularity**.

Thus the abstract forest theorem is not being reproved.  It supplies an
incidence ledger; Theorem 5.1 supplies a special physical lift whose
colour ledger is a union of ears and whose selected Boolean squares are
an explicit repair matching when the \(c_i\) are distinct.  The all-\(m\)
construction still needs coupled input cycles satisfying (5.1), (5.2),
(4.1), pivot distinctness, uniform sign, and, for a forced recursive
certificate, pivot-unitriangularity.

## 8. Audit of the earlier Lemma 4.6

No logical counterexample to Lemma 4.6 of
MATH_AUDIT_K_GMM_SINGLE_PORT_GLUE_CATALAN_COMMON_REFINEMENT_OBSTRUCTION_20260731.md
was found.  Under its strong hypotheses, the direct edge remains adjacent
to the retained partner.  The present result sharpens its scope:

1. the free endpoint is forced, and free-port injectivity is necessary;
2. its one-cycle clause is exactly (4.1);
3. its hypotheses force distinct direct lower colours and (5.3).

They do not force distinct pivot labels \(c_i\), a common cyclic sign, or
leaf peeling of the full repair atlas.  Lemma 4.6 did not claim those
stronger conclusions.

Lemma 4.6 is not necessary outside the rooted fibre: Theorem 2.1 permits
a gain edge \(E_j\) to partner \(D_i\) when \(y_j=x_i\).

The authenticated positive \(m=3\) directed fixture illustrates the
scope.  Its occurrence-colour forest is

\[
 7P_2\mathbin{\dot\cup}P_4\mathbin{\dot\cup}2P_6,
\]

rather than the rooted signature \(5P_4\dot\cup5P_2\).  It is a valid
literal common refinement outside the independent-ear subfibre, not a
counterexample to Theorem 5.1.

## 9. Artifacts and remaining gate

Local replay:

* scratch/audit_k_block_coherent_pascal_local_obstructions_20260731.py;
* scratch/k_block_coherent_pascal_local_obstructions_20260731.audit.json.

The script checks ranks, containments, Johnson adjacencies, union labels,
the centre-only hit, and the doubled vertical edge in (6.1)--(6.2).  It is
a constant-size audit, not a search.

The positive \(m=3\) forest profile is independently recorded in
MATH_AUDIT_CATALAN_COLOUR_INCIDENCE_GRAPH_M3_M4_20260731.md and its
associated audit JSON.

The smallest all-dimensional statement left by this fibre is:

> For every \(m\), construct a rooted \(K\)-block child and a central
> alternating child containing the forced free-port matching, with palette
> complements (5.1)--(5.2), connected fragment graph, distinct pivot labels
> \(c_i\), and uniform block sign.  A forced recursive certificate also
> needs pivot-unitriangularity of the full atlas.

The published 3-path/switched-2-path state proves these requirements at
one port only.  The centre-only and bow-tie examples prove that \(K\)
individually admissible ports are not an adequate induction invariant.

Proved here: the exact partner theorem, the rooted-fibre
necessary-and-sufficient criterion, automatic physical degree two, the
automatic \(K\)-ear colour forest, the exact repair pivot, the exact
topology reduction, and two literal local obstructions.

Not proved: all-dimensional rooted packages, extension of the forced port
matching to a suitable central Hamilton cycle, connected monodromy in
every dimension, pivot-unitriangularity, or the general gain-partner
recursion.
