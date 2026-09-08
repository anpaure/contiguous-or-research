# The published single-port tight-enumeration glue cannot realize the Catalan common refinement

Date: 2026-07-31  
Status: exact source audit, exact Hall obstruction, and an exact multi-port
replacement criterion.  This is an obstruction to the published recursive
architecture, not to arbitrary tight enumerations or arbitrary cap-two cycles.

## 0. Verdict

Put

\[
 M=\binom{2m}{m},\qquad N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname{Cat}_m.
\]

The directed Catalan repair identity is equivalent to a common refinement
of

1. a cap-two upper-block cycle on the rank-\(m\) states of \(Q_{2m}\); and
2. a tight enumeration of ranks \(m-1,m\),

where the edge subdivided at each rank-\((m-1)\) vertex has a different
rank-\((m+1)\) union.  The local primary source shows that the published
adjacent-level recursion cannot produce this common refinement once
\(K>1\).

The obstruction is not generic counting.  It is an explicit Hall set in
the new-coordinate split.  A common refinement needs exactly \(K\)
distinguished lower occurrences to cross the two Pascal sectors.  The
published gluing step creates exactly one.  Consequently its distinguished
upper-block map has at least \(K-1\) collision excess on the zero sector
and misses at least \(K-1\) blocks on the one sector, independently of all
input cycles and coordinate permutations.

Thus the recursive object required by Catalan repair is a **\(K\)-port bulk
glue**, not the one-port ear in the published proof.  Section 4 gives an
exact necessary-and-sufficient palette criterion for such a bulk glue;
adding a unitriangular order on its occurrence-labelled repair triples is
sufficient for a leaf-peelable repair core.

## 1. Source correction

In Gregor--Mütze, *Trimming and Gluing Gray Codes*, Lemmas 12 and 13 are
the reflected-Gray-code facts

* consecutive states on one level have Hamming distance two; and
* the `up` and rotated `down` sequences are subsequences of the adjacent
  level orders.

They drive the trimming construction.  They are not the \(n\mapsto n+1\)
adjacent-level gluing induction.

The relevant induction is Theorem 15 and its use in Theorem 8(iiia).  It
combines a tight enumeration \(C_0\) of \(Q_{n,[k,k+1]}\) and a tight
enumeration \(C_1\) of \(Q_{n,[k-1,k]}\).  After coordinate permutations,
it appends a zero to \(C_0\), appends a one to \(C_1\), removes

\[
 (b_{n,k},a_{n,k+1})\quad\hbox{and}\quad(a_{n,k},b_{n,k}),
\]

and adds

\[
 (a_{n,k+1}0,a_{n,k}1),\qquad
 (b_{n,k}0,b_{n,k}1).
\tag{1.1}
\]

The first new step in (1.1) is a same-rank distance-two step.  The second
is the unique new cross-sector cube edge incident with a lower-rank
vertex.

There is one printed-range nuance.  In the source proof, the induction
sentence states \(1\le k<\lfloor n/2\rfloor\).  At the central boundary
\(n=2m-1,\ k=m-1\), this strict inequality is not satisfied.  The
displayed splice (1.1) is nevertheless algebraically valid there: the
odd-dimensional middle-level cycle supplies the required 3-path and the
other parent supplies the switched 2-path.  Accordingly, the central
claims below concern this valid boundary application of the displayed
one-glue formula; they do not assert that the printed induction sentence
explicitly includes the equality case.

There is also no second, already synchronized recursion hidden in this
paper.  Its two-level saturating-cycle input is Theorem 3, imported from
Mütze--Su.  The cap-two compression then makes a separate Hall choice that
injects the omitted middle facets into upper blocks.  Neither the theorem
statement nor the proof of Theorem 15 couples that host injection to the
tight-enumeration gluing ports.  Synchronization is therefore genuinely a
new theorem, not a choice left unspecified inside one published recursive
object.

The paper's Theorem 8 also states explicitly that every distance-two step
in its constructed tight enumerations stays within one level, never
between levels \(k\) and \(k+2\).  This will give a second, three-level
obstruction in Section 3.

## 2. Exact new-coordinate balance

Set

\[
 n=2m-1,\qquad k=m-1,
\]

and call the new coordinate \(z\).  In any tight enumeration of
\(Q_{2m,[m-1,m]}\), each lower state \(R\) is flanked by two distinct
rank-\(m\) states \(X_R,Y_R\).  Suppressing \(R\) distinguishes the
Johnson edge \(X_RY_R\), with upper-block label

\[
                         u(R)=X_R\cup Y_R.
\tag{2.1}
\]

The tight enumeration has the exact selected upper palette precisely when

\[
 u:\binom{[2m]}{m-1}\longrightarrow\binom{[2m]}{m+1}
\tag{2.2}
\]

is a bijection and the \(K\) unsubdivided middle steps have distinct union
labels.  The first condition selects one subdivided middle edge of every
upper colour; the second says the remaining \(K\) edges duplicate different
colours, hence gives the floor profile \(1^{N-K}2^K\).

For the literal cap-two **block** conclusion, one further condition is
necessary and sufficient:

\[
 \boxed{\text{every unsubdivided edge is consecutive in the projected
 cycle to the unique subdivided edge with the same union.}}
\tag{2.2a}
\]

Indeed, a colour of load two forms one contiguous block exactly when its
two edge occurrences are adjacent.  Neither palette bijectivity nor
squarefreeness of the direct labels implies (2.2a).

Write

\[
 A=\binom{2m-1}{m-1},\qquad
 B=\binom{2m-1}{m-2}.
\tag{2.3}
\]

Then

\[
 A-B=\operatorname{Cat}_m=K.
\tag{2.4}
\]

### Theorem 2.1 (Catalan sector-balance law)

If (2.2) is a bijection, exactly \(K\) of the \(z\)-free lower states
\(R\in\binom{[2m-1]}{m-1}\) have \(z\in u(R)\).  Equivalently, exactly
\(K\) distinguished lower occurrences use a cross-sector cube edge.

#### Proof

There are \(A\) lower states avoiding \(z\) and \(B\) lower states
containing \(z\).  Every lower state containing \(z\) has both flanking
middle states containing \(z\), so its union contains \(z\).

The no-\(z\) upper blocks number

\[
 \binom{2m-1}{m+1}=\binom{2m-1}{m-2}=B,
\]

whereas the upper blocks containing \(z\) number

\[
 \binom{2m-1}{m}=\binom{2m-1}{m-1}=A.
\]

Therefore exactly \(B\) of the \(A\) \(z\)-free lower states can map to
no-\(z\) blocks, and the remaining \(A-B=K\) must map to blocks containing
\(z\).

For a \(z\)-free lower state \(R\), there is only one rank-\(m\) superset
containing \(z\), namely \(R+z\).  Since its two flanking middle states
are distinct, \(z\in u(R)\) holds exactly when one of the two incident
enumeration edges crosses the sector boundary.  This proves the second
formulation. \(\square\)

The identity (2.4) follows, for example, from

\[
 A=\frac12\binom{2m}{m},\qquad
 \frac BA=\frac{m-1}{m+1}.
\]

### Theorem 2.2 (single-port Hall obstruction)

The central-boundary application of the displayed Theorem 15 gluing step
has distinguished upper-block deficiency at least \(K-1\).  More precisely:

1. among the \(A\) \(z\)-free lower states, exactly one has a
   distinguished union containing \(z\);
2. the other \(A-1\) rows have neighbourhood contained in the \(B\)
   no-\(z\) upper blocks, giving Hall deficiency
   \[
                         (A-1)-B=K-1;
   \tag{2.5}
   \]
3. the \(z\)-containing distinguished bank has only \(B+1\) occurrences
   for \(A\) target blocks, and hence misses at least \(K-1\) blocks.

#### Proof

All lower vertices inherited from \(C_0\) end in zero.  Except for
\(b_{n,k}0\), both of their flanking middle vertices also end in zero,
so their unions avoid \(z\).  The second new edge in (1.1) makes
\(b_{n,k}0\) adjacent to \(b_{n,k}1\), and hence this one distinguished
union contains \(z\).  The new distance-two step in (1.1) has no lower
vertex and cannot create another distinguished occurrence.  This proves
part 1.

Part 2 is the explicit Hall set consisting of the other \(A-1\) lower
rows.  Part 3 counts the \(B\) lower rows inherited from \(C_1\), all of
which contain \(z\), together with the one crossing row from \(C_0\).
Using (2.4) proves both deficits. \(\square\)

This theorem is invariant under the independent coordinate permutations
allowed in the proof: such permutations do not change the appended bit or
the number of cross-sector lower incidences.  It is also invariant under
the choices of the two input tight enumerations.  Therefore changing the
special 3-path or switched 2-path cannot repair the deficit while retaining
the one-port architecture.

### Proposition 2.3 (the direct duplicate bank is preserved)

The failure in Theorem 2.2 is confined to the distinguished upper-block
transversal; it is not a failure of the \(K\) direct-edge count.  In the
central specialization, \(C_0\) is bipartite Hamiltonian and has no direct
middle step.  The recursion removes from \(C_1\) the direct edge
\((a_{n,k},b_{n,k})\).  Its tagged union would have been

\[
                  z+(a_{n,k}\cup b_{n,k})=z+a_{n,k+1}.
\]

The replacement direct edge \((a_{n,k+1}0,a_{n,k}1)\) has the same union
\(z+a_{n,k+1}\).  Every other direct edge of \(C_1\) is unchanged and
tagged by \(z\).  Hence the direct-edge union multiset is carried through
the gluing step exactly.  In particular, squarefreeness of that bank is
preserved.

Thus the displayed one-port recursion already transports the prospective cap-two
duplicate bank.  What it fails to transport is exactly the one-edge-per-
upper-block distinguished bank, by the deficiency in (2.5).  A successful
modification needs \(K-1\) additional lower interface ports without
spoiling this preserved direct bank.

For the first nontrivial directed-repair fixture \(m=3\), the deficit is
already \(K-1=4\).  The positive leaf-peelable repair core has five repair
triples, exactly the number of cross-sector ports demanded by Theorem 2.1.

## 3. The independent three-level jump obstruction

The common refinement also has a canonical tight enumeration of the three
levels \(m-1,m,m+1\).  In every cap-two block, distinguish one edge below
and one edge above.  On each of the \(N-K\) singleton blocks, the common
edge expands as

\[
 A,\ A\cap B,\ A\cup B,\ B,
\tag{3.1}
\]

and therefore contributes a distance-two step from rank \(m-1\) directly
to rank \(m+1\).  There are

\[
 N-K=(m-1)K
\tag{3.2}
\]

such steps.  This is exactly the parity-shore imbalance

\[
 2N-M=(m-1)K
\tag{3.3}
\]

of the three-level interval.

By contrast, Theorem 8 states that every distance-two step in its
constructed enumerations stays within one level.  Thus its three-level
output has zero steps of type (3.1), while every diamond-tight common
refinement has all \((m-1)K\) required distance-two steps of that type and
no same-level distance-two steps.

Consequently the published three-level trimming output is not merely
missing a choice of orientation: it lies in the opposite jump-type normal
form.  Turning it into a diamond-tight common refinement requires replacing
all \((m-1)K\) distance-two steps.  The theorem does not provide that
transformation.

## 4. Exact replacement: a Catalan-port Pascal glue

Consider any sector gluing, not necessarily the published one.  Let

\[
 P\subseteq\binom{[2m-1]}{m-1}
\]

be the \(z\)-free lower states whose distinguished edge uses the unique
middle neighbour \(R+z\).  Let \(u_0\) be the union map on the other
\(z\)-free rows, let \(u_1\) be the union map on the rows containing
\(z\) after deleting \(z\), and use the same notation \(u_1\) for the
stripped unions of rows in \(P\).

### Theorem 4.1 (exact Catalan-port palette criterion)

The distinguished edges select one edge of every rank-\((m+1)\) upper
colour if and only if

\[
 \begin{aligned}
 |P|&=K,\\
 u_0&:\binom{[2m-1]}{m-1}\setminus P
       \longrightarrow\binom{[2m-1]}{m+1}
       &&\text{is a bijection},\\
 u_1&:\left(z+\binom{[2m-1]}{m-2}\right)\mathbin{\dot\cup}P
       \longrightarrow\binom{[2m-1]}m
       &&\text{is a bijection}.
 \end{aligned}
\tag{4.1}
\]

It has the cap-two floor profile if and only if, in addition, the union
labels of the \(K\) direct middle steps are distinct.  It is a literal
cap-two block common refinement if and only if (2.2a) also holds.

#### Proof

Upper blocks split disjointly into those avoiding and containing \(z\).
Theorem 2.1 forces \(|P|=K\).  Once this holds, the source and target sizes
in both displayed maps agree, and exact upper-colour coverage is precisely
their bijectivity.  Every lower colour is already present exactly once
because the source is a tight enumeration.  The projected middle cycle has
one distinguished edge of every upper colour and exactly \(K\) additional
direct edges.  Its load profile is \(1^{N-K}2^K\) exactly when those
additional edges enter distinct colours.  Under that floor profile,
condition (2.2a) is exactly contiguity of every doubled colour block.
\(\square\)

This is the weakest finite recursive interface exposed by the source
audit.  It is stronger than a count of \(K\) ports: the two palette maps
and the direct-edge labels must all be squarefree.

### Lemma 4.2 (one Pascal square preserves the direct label)

Let \(b-x\) be a lower--upper edge of \(C_0\), and let \(a-b\) be a
direct upper--upper step of \(C_1\), where

\[
                         x=a\cup b.
\tag{4.2}
\]

After appending sector bits, replace

\[
             b0-x0,\quad a1-b1
 \qquad\hbox{by}\qquad
             b0-b1,\quad x0-a1.
\tag{4.3}
\]

Then all four new incidences are legal, vertex degrees are preserved, and
the direct-edge upper label is unchanged:

\[
       (a1)\cup(b1)=z+x=(x0)\cup(a1).
\tag{4.4}
\]

If the other upper neighbour of the lower vertex \(b\) in \(C_0\) is
\(y\), then the distinguished label at that row changes from

\[
                         x\cup y
 \quad\hbox{to}\quad
                         z+y.
\tag{4.5}
\]

#### Proof

The edge \(b0-b1\) flips only \(z\).  Since \(a,b\) are Johnson adjacent
and their union is \(x\), the sets \(x0\) and \(a1\) differ by exchanging
the unique member of \(x\setminus a\) with \(z\), so they form a legal
direct middle step.  Equations (4.4) and (4.5) follow from
\(a,b\subset x\) and \(b\subset y\).  Each of the four endpoints loses
and gains one incidence, proving the degree assertion. \(\square\)

The published gluing is exactly one instance of (4.3).  Lemma 4.2 shows
how to generalize it without sacrificing the already-correct direct
duplicate bank: apply compatible Pascal squares at additional direct
edges.

### Corollary 4.3 (all-direct-edge square-glue target)

Suppose a simultaneous family of Pascal squares is physically compatible:
the removed occurrences are distinct, no vertical edge \(b0-b1\) is
repeated, and after all switches the result is one cycle.  Then their
direct-edge union multiset is unchanged.  If the result is a common
refinement, the family has exactly \(K\) members; hence it uses every
direct step of \(C_1\).

Conversely, if the input direct-step union labels are distinct, a compatible
family using all \(K\) direct steps gives a floor-profile common refinement
exactly when the two transported distinguished palettes in (4.1) are
bijective.  It gives a literal cap-two block refinement exactly when
(2.2a) also holds.  Thus an explicit synchronized recursion reduces to
choosing one compatible orientation/incidence for every direct step,
followed by the two palette checks, the block-adjacency check, and the
one-cycle check.

#### Proof

Equation (4.4) proves preservation independently at every switched edge.
Every switch creates one and only one cross-sector distinguished lower
row.  Theorem 2.1 therefore forces exactly \(K\) switches in a common
refinement.  There are exactly \(K\) direct steps in the input tight
enumeration, so all are used.  The converse is Theorem 4.1 together with
the unchanged, squarefree direct bank. \(\square\)

### Corollary 4.4 (exact oriented direct-edge atlas)

Assume the direct steps of \(C_1\) have distinct unions.  For every direct
step \(d=\{a,b\}\), put \(x(d)=a\cup b\).  An endpoint
\(r\in\{a,b\}\) is an admissible orientation when \(C_0\) uses the
incidence \(r-x(d)\).  Let \(y(d,r)\) be the other upper neighbour of
the lower vertex \(r\) in \(C_0\).  The candidate has loss/gain signature

\[
        \left(x(d)\cup y(d,r),\ y(d,r)\right),
\tag{4.6}
\]

meaning that it removes the first label from the no-\(z\) distinguished
bank and inserts \(z+y(d,r)\) into the tagged bank.

Within the simultaneous-Pascal-square fibre, a literal cap-two common refinement
is equivalent to choosing one admissible orientation for every direct step
such that

1. no oriented endpoint \(r\) is used twice;
2. the unchosen \(C_0\) distinguished labels enumerate
   \(\binom{[2m-1]}{m+1}\);
3. the \(C_1\) distinguished labels, after deleting \(z\), together with
   the gain labels \(y(d,r)\), enumerate
   \(\binom{[2m-1]}m\); and
4. the simultaneous switches produce one cycle; and
5. every preserved direct edge is adjacent to the unique distinguished
   edge having the same union label.

#### Proof

Admissibility is exactly the local hypothesis of Lemma 4.2.  Reusing an
oriented endpoint would repeat the physical vertical edge \(r0-r1\), so
condition 1 is necessary; with distinct direct unions it also makes the
removed \(C_0\) incidences distinct.  Lemma 4.2 gives the loss/gain
signature.  Conditions 2 and 3 are exactly the two bijections in (4.1),
condition 4 is the remaining topology requirement, and condition 5 is
exactly (2.2a).  The same facts prove sufficiency. \(\square\)

Every direct step has at most two candidate orientations.  Thus the new
recursion target is not an unrestricted Hamilton search: it is a
Catalan-sized binary orientation atlas with explicit endpoint, two-palette,
and subtour constraints.  A missing candidate at even one direct step is
an immediate literal obstruction.

There is a particularly transparent local form of this first test.  The
two endpoints \(a,b\) of a direct step are two facets of its union \(x\),
while the two lower neighbours of \(x\) in the central cycle \(C_0\) are
another two facets of \(x\).  Hence

\[
 \operatorname{Cand}(d)\neq\varnothing
 \quad\Longleftrightarrow\quad
 \{a,b\}\cap N_{C_0}(x)\neq\varnothing.
\tag{4.7}
\]

After identifying a facet of \(x\) by its missing element, (4.7) says that
two 2-subsets of an \(m\)-set must intersect.  This is automatic for
\(m=3\), but not for \(m\ge4\).  Thus the first genuinely recursive local
invariant is a **facet-pair hitting condition** between the direct bank of
\(C_1\) and the incidence pair selected by \(C_0\) in the same upper
block.  The separate existence theorems impose no such coupling.

### Theorem 4.5 (Pascal square floor-core equivalence)

Assume \(m\ge3\).  Let \(q_0(r)\) be the union of the two \(C_0\)
upper neighbours of a lower vertex \(r\), and let \(q_1(s)\) be the union
of the two \(C_1\) upper neighbours of a lower vertex \(s\).  Assume:

1. the \(A=B+K\) labels \(q_0(r)\), on the \(B\) no-\(z\) target
   blocks, have floor profile \(1^{B-K}2^K\);
2. the \(B\) labels \(q_1(s)\) are distinct; and
3. the \(K\) direct-step unions of \(C_1\) are distinct.

Let \(\mathcal D\) be the \(K\) doubled \(q_0\)-labels and let
\(\mathcal H\) be the \(K\) rank-\((k+1)\) labels omitted by \(q_1\).
Form the occurrence-labelled three-partite hypergraph on

\[
                  E_{\rm dir}(C_1)\ \dot\cup\ \mathcal D\ \dot\cup\ \mathcal H
\]

by including

\[
           \bigl(d,q_0(r),y(d,r);r\bigr)
\tag{4.8}
\]

for every admissible orientation \(r\) of \(d\) with
\(q_0(r)\in\mathcal D\) and \(y(d,r)\in\mathcal H\).

Then a simultaneous Pascal-square family has both distinguished palettes
exactly once if and only if (4.8) contains a perfect matching.  It gives a
floor-profile common-refinement cycle if and only if, additionally, the
matched squares have one-cycle topology.  It gives a literal cap-two block
cycle if and only if (2.2a) also holds.

#### Proof

The no-\(z\) bank starts with exactly one surplus occurrence in every
colour of \(\mathcal D\).  Since every square only deletes from this bank,
exactness forces and is forced by deleting one occurrence of each member
of \(\mathcal D\).  The tagged bank starts with the distinct image of
\(q_1\), so exactness forces and is forced by adding every member of
\(\mathcal H\) once.  Every direct step must be switched by Corollary 4.3.
These are exactly the three shore conditions for a perfect matching in
(4.8).

Two chosen candidates cannot reuse one physical oriented endpoint: they
would then have the same loss label \(q_0(r)\), contrary to matching on
\(\mathcal D\).  Hence the switches are physically edge-distinct.  The
direct bank remains squarefree by Lemma 4.2 and assumption 3.  The
one-cycle condition gives the floor-profile cycle.  Condition (2.2a) is
independently necessary and sufficient for its doubled colours to be
contiguous. \(\square\)

This theorem is the literal common-refinement core sought from a recursive
proof.  It has \(K\) vertices on each shore, and its hyperedges are bounded
local Pascal squares.  A leaf-peelable instance supplies a forced perfect
matching; a missing direct-edge candidate or a Hall-deficient subcore is a
finite obstruction.

### Lemma 4.6 (block-coherent closure)

Assume the hypotheses of Theorem 4.5.  Suppose every direct edge
\(d=ab\) of \(C_1\), with \(x=a\cup b\), already has a distinguished
edge of the same union sharing exactly the endpoint \(a\).  Call \(b\)
the free endpoint of this cap-two block.  Suppose further that

1. the free endpoints of the \(K\) blocks are pairwise distinct;
2. \(C_0\) uses the incidence \(b-x\) for every block; and
3. the \(K\) resulting Pascal squares satisfy the two palette bijections
   and have one-cycle topology.

Then their output is a literal cap-two block common refinement.

#### Proof

Use (4.3) with vertical endpoint \(b\).  It replaces \(ab\) by
\(x0-a1\), preserving its union as \(z+x\).  The distinguished partner
through \(a\) is untouched in the tagged \(C_1\) sector; its union also
becomes \(z+x\).  Hence the two occurrences remain adjacent at \(a1\),
so (2.2a) holds for every direct edge.  Conditions 1 and 2 make the square
supports compatible, while condition 3 and Theorem 4.5 give the exact
palettes and one cycle. \(\square\)

This is a proved recursive closure rule, but not yet an existence theorem:
it requires the central child to hit all free facet ports of an already
block-coherent lower child.  The separate Gregor--Mütze and Mütze--Su
existence statements do not provide that coupled incidence condition.

### Corollary 4.7 (unitriangular bulk-ear criterion)

Assume the hypotheses of Theorem 4.5.  Suppose its hypergraph (4.8) has
edges

\[
                       e_j=(d_j,\delta_j,h_j)
\]

that cover all three shores and can be ordered so that, after deleting the
vertices of \(e_1,\ldots,e_{j-1}\), one vertex of \(e_j\) has no remaining
incident edge except \(e_j\).  Then (4.8) is leaf-peelable, the matched
Pascal squares give exact distinguished palettes, and they give a
floor-profile common-refinement cycle whenever their contracted fragment
graph is one cycle.  They give a literal cap-two block cycle when (2.2a)
also holds, in particular under Lemma 4.6.

In the hosted cap-two construction, the direct-step shore is indexed by
the \(K\) inserted omitted facets.  Under that identification these are
exactly occurrence-labelled omitted-facet/duplicate/hole repair triples.
The leaf-peelability assertion is for the Pascal-square atlas (4.8).
Reintroducing additional all-host repair edges can destroy degree-one
vertices, although the perfect matching already found in (4.8) remains a
valid existence certificate in the larger hypergraph.

#### Proof

At every stage the indicated vertex forces \(e_j\).  Delete its three
vertices and continue.  The ordered triples give a perfect matching of the
core.  Theorem 4.5 gives the palette conclusion, and its final topology
clause gives the floor-profile cycle conclusion.  The literal cap-two
block conclusion additionally requires (2.2a). \(\square\)

The displayed one-port recursion supplies only one member of the required
\(K\)-triple bank.  Thus Corollary 4.7 is not a reinterpretation of its
one-port gluing; it specifies the genuinely new bulk interface that an
all-\(m\) proof must construct.

## 5. K15/K16-source calibration

For the even ground \(14\) feeding the K15 Pascal braid,

\[
 (A,B,K)=\left(\binom{13}{6},\binom{13}{5},429\right)
          =(1716,1287,429).
\]

The common refinement therefore needs \(429\) cross-sector distinguished
rows and \(858\) physical cross seams.  These are exactly the forced
generalized-Pascal counts.  The published one-port splice leaves the exact
tag discrepancy \(428\), irrespective of which authenticated K15 cycle is
used inside the two sectors.

For the even ground \(16\), which is the source dimension for the K17
lift,

\[
 (A,B,K)=\left(\binom{15}{7},\binom{15}{6},1430\right)
          =(6435,5005,1430).
\]

Thus the synchronized recursion requires \(1430\) square ports and
\(2860\) physical cross seams; the one-port deficit is \(1429\).  This is
the same Catalan mass that appears as the separated-interface tax in the
K17 anatomy.  The statement concerns K16 as the even **source** of K17;
it does not assert that the solved K16 word itself was constructed by this
common-refinement recursion.

## 6. Scope

Proved here:

* the exact \(K\)-port sector-balance law;
* a deficiency-\((K-1)\) Hall certificate for the central-boundary
  application of the displayed Theorem 15 one-port gluing architecture;
* the incompatible distance-two-step types of the published three-level
  trimming output and the desired diamond-tight output; and
* a necessary-and-sufficient palette criterion, the exact block-adjacency
  condition, a block-coherent closure lemma, and a sufficient leaf-peeling
  condition for a replacement bulk glue.

Not proved here:

* that no other tight enumeration is a cap-two common refinement;
* that a \(K\)-port bulk glue cannot exist;
* that every cap-two common refinement has a leaf-peelable repair core; or
* any all-\(m\) coefficient-one compiler theorem.

The obstruction is therefore sharp in architecture and implication scope:
the displayed single-port splice cannot be synchronized at the central
boundary by choosing different internal cycles, but a new Catalan-port
recursion remains a live construction target.

## 7. Audited source

Primary source:

* `tmp/pdfs/trimming_gluing_gray_codes_1607.08806.pdf`
* SHA-256
  `8717be904a3aba9dee006133dbbe803bbd2069d2dd32478bbcf397d982cda668`
* P. Gregor and T. Mütze, *Trimming and Gluing Gray Codes*, Theoretical
  Computer Science 714 (2018), 74--95,
  <https://arxiv.org/pdf/1607.08806>, DOI
  `10.1016/j.tcs.2017.12.003`.

The source passages were checked both by text extraction and by rendering
the theorem statement and the Theorem 15 gluing page.  The mathematical
argument above uses only the displayed gluing edges, the explicit
same-level distance-two property in Theorem 8, and binomial identities.
