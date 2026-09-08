# Lane D: an exact successor/zeta DAG for Hall neighborhoods

Date: 2026-07-28

Method: pure mathematics.  The finite H29 figures quoted below are
audited inputs; no new exhaustive leaf enumeration is used.

## 0. Outcome

Let \(G=(V,E)\) be the directed union of several parent chronologies,
let \(\sigma\) be a selected spanning directed path in \(G\), and let
\(A\) be a fixed Hall target family.  At depth three, the exact
compiler neighborhood

\[
                         N_\sigma(A)
\tag{0.1}
\]

can be evaluated by a finite deterministic DAG with:

1. a variable-successor chain of radius at most twelve;
2. the exact erosion/carrier state of the resulting local word;
3. one ternary interval-zeta table for \(A\); and
4. thirty-six separate endpoint indicators.

No catalogue of all possible 10--12-step directed motifs is needed.

The size bounds below use the natural state-DAG model: immutable finite
tables are stored once, and a lookup node carries its computed address.
Thus they are bounds for an exact evaluator or for a solver with element/table
constraints.  They are not a claim that separately bit-blasting the same ROM
at every cell preserves the bound.

### Theorem A (exact neighborhood circuit)

Assume first that the selected path has at least twelve middle vertices,
as in H29.  There is an exact arithmetic/Boolean circuit which, from the selected
successor and predecessor maps of \(\sigma\), computes

\[
 \boxed{
 |N_\sigma(A)|
 =\sum_{\text{interior cells }C}H_A(C)
  +\sum_{d=0}^{2}\sum_{s=0}^{5}
       \bigl(H_A(C^{\rm L}_{d,s})
             +H_A(C^{\rm R}_{d,s})\bigr).}
\tag{0.2}
\]

Here every \(H_A(C)\in\{0,1\}\) is exact: it is one precisely when
some target of \(A\) is feasible in the literal compiler cell \(C\).
The two endpoint sums are the exact boundary palettes.  They replace
the unsafe projection allowance \(+36\).

For every cell of row depth \(d\), \(H_A(C)\) is obtained from at most

\[
                         2^{d+1}\le8
\tag{0.3}
\]

lookups in a table indexed by ternary coordinate states.  The complete
table has at most

\[
                         3^k
\tag{0.4}
\]

entries and is shared by every cell and every parent union.

### Corollary A.1 (H29 scale)

For \(k=15\),

\[
                         3^{15}=14\,348\,907.
\tag{0.5}
\]

The table values lie in \([0,|A|]\); for H29 they fit in sixteen bits.
For a 6,435-vertex selected chronology, the structural successor DAG
has at most

\[
                         12|V|=77\,220
\tag{0.6}
\]

forward pointer states.  Using the depth-sensitive lookup counts
\(2,4,8\), it makes at most

\[
             (2+4+8)|V|+2\cdot6(2+4+8)
             =90\,258
\tag{0.7}
\]

zeta queries.  This is far smaller than the
\(213\,501\,726\) full directed leaves traversed by the three-parent
radius enumeration.  An \(A\)-specific reduced decision DAG may replace
the full table and merge equal residual subfunctions.

The H29 calibration is

\[
 |A|=1524,\qquad |N(A)|=1495.
\tag{0.8}
\]

The reported projected upper counts

\[
                         U_3=2886,\qquad U_4=2860
\tag{0.9}
\]

are not exact neighborhood counts.  They identify a short central arc
tuple and existentially pool incompatible completions.  Formula (0.2)
keeps one selected successor history and therefore returns 1495 on the
H29 chronology, including its literal boundary cells.

### Theorem B (certified convergent refinement)

There is also a projection-refinement version.  At radius \(h\), retain
the set of exact radius-twelve compiler states compatible with the
current partial successor history.  Declare a cell:

- forced if every compatible completion hits \(A\);
- impossible if no compatible completion hits \(A\);
- unresolved otherwise.

If \(L_h,U_h\) are obtained by counting forced cells and
forced-or-unresolved cells, then

\[
 L_h\le |N_\sigma(A)|\le U_h,\qquad
 L_h\nearrow |N_\sigma(A)|,\qquad
 U_h\searrow |N_\sigma(A)|.
\tag{0.10}
\]

At \(h=12\) all cells, including boundary cells, are resolved and

\[
                         L_{12}=U_{12}=|N_\sigma(A)|.
\tag{0.11}
\]

Thus a short projection may be used as an initial relaxation only when
its completion set is retained and refined.  A bare \(k=3\) or \(k=4\)
motif projection is not a proof-safe compression.

## 1. Literal depth-three compiler cell

We first isolate the finite local predicate being computed.

Let

\[
                         W=(w_0,\ldots,w_{\ell-1}),
 \qquad w_i\subseteq[k],
\tag{1.1}
\]

be a finite middle word.  Its maximal depth-three linear erosion is

\[
 p_i=\bigcap_{j=\max(0,i-3)}^{\min(i,\ell-1)}w_j,
 \qquad 0\le i<\ell+3.
\tag{1.2}
\]

For a middle position \(t\) and coordinate \(x\in w_t\), define its
complete carrier set

\[
 K_{t,x}
 =\{i\in\{t,t+1,t+2,t+3\}:x\in p_i\}.
\tag{1.3}
\]

Fix a compiler cell whose consecutive erosion positions are

\[
                         C=\{c,c+1,\ldots,c+d\},
 \qquad d\in\{0,1,2\}.
\tag{1.4}
\]

Its envelope and mandatory mask are

\[
                         E_C=\bigcup_{i\in C}p_i,
\tag{1.5}
\]

\[
 M_C
 =\{x:\text{for some }t,\ x\in w_t,
             \varnothing\ne K_{t,x}\subseteq C\}.
\tag{1.6}
\]

For a lower target \(T\subseteq[k]\), the authoritative compiler
predicate is

\[
\boxed{
 \operatorname {Fit}(T,C)
 \iff
 \begin{cases}
 M_C\subseteq T\subseteq E_C,\\
 T\cap p_i\ne\varnothing&\text{for every }i\in C.
 \end{cases}}
\tag{1.7}
\]

The permitted target ranks are already encoded by membership in \(A\).
Consequently

\[
                         H_A(C)
 =\mathbf1_{\{\exists T\in A:\operatorname {Fit}(T,C)\}}.
\tag{1.8}
\]

Equations (1.2)--(1.8) are exactly the envelope, mandatory-carrier, and
row-intersection tests in the Hall auditor.  In particular, (1.6)
retains all carriers; no \(k=3\) or \(k=4\) arc projection is being
substituted for them.

## 2. Exact locality radius

For an interior row-depth-\(d\) cell, take

\[
                         c=6,\qquad \ell=d+10.
\tag{2.1}
\]

### Lemma 2.1 (the \(d+10\) locality lemma)

The complete signature

\[
                         (p_i:i\in C;\ E_C;\ M_C)
\tag{2.2}
\]

is determined by the \(d+10\) middle vertices in (2.1).

#### Proof

The erosion sets \(p_i\), \(i\in C=[6,6+d]\), depend only on middle
positions

\[
                         3,\ldots,6+d.
\tag{2.3}
\]

If a carrier \(K_{t,x}\) is a nonempty subset of \(C\), then

\[
                         3\le t\le6+d.
\tag{2.4}
\]

Indeed \(t+3<6\) gives no carrier in \(C\), while \(t>6+d\) starts
strictly after \(C\).  For \(t\) in (2.4), all four erosion positions
in (1.3) depend only on middle positions

\[
                         t-3,\ldots,t+3
 \subseteq\{0,\ldots,d+9\}.
\tag{2.5}
\]

These are precisely the positions of the word of length \(d+10\).
Thus (1.5)--(1.6), and hence (2.2), are local to that word.
\(\square\)

Under the Hall audit's entry/exit-slot convention this is the advertised
10--12-arc motif.  The authoritative evaluator stores the same object
as \(d+10\) middle vertices.  Lemma 2.1 is independent of this indexing
choice.

## 3. Ternary interval-zeta compression

The literal evaluator could enumerate every \(T\in A\) for every cell.
The following transform removes that factor.

For \(B\subseteq U\subseteq[k]\), put

\[
 Z_A(B,U)
 =|\{T\in A:B\subseteq T\subseteq U\}|.
\tag{3.1}
\]

We extend this definition by the convention

\[
                         Z_A(B,U)=0\qquad\text{if }B\nsubseteq U.
\tag{3.1a}
\]

This case genuinely occurs in the inclusion--exclusion terms below:
deleting \(P_J\) from the envelope may delete a mandatory coordinate.

Each coordinate has exactly three states:

\[
 \begin{array}{c|c}
 0&x\notin U\quad\text{(forbidden)},\\
 1&x\in U\setminus B\quad\text{(optional)},\\
 2&x\in B\quad\text{(mandatory)}.
 \end{array}
\tag{3.2}
\]

Hence the entire interval-zeta table has \(3^k\) entries.

### Lemma 3.1 (exact zeta recurrence)

Let \({\cal T}_A\) be the binary trie of the masks in \(A\), with
coordinates read in a fixed order.  At coordinate \(x\), the recurrence
for a ternary query is:

\[
 {\cal Z}(q,x,\tau)=
 \begin{cases}
 {\cal Z}(q_0,x+1,\tau),&\tau_x=0,\\
 {\cal Z}(q_0,x+1,\tau)+{\cal Z}(q_1,x+1,\tau),
                                      &\tau_x=1,\\
 {\cal Z}(q_1,x+1,\tau),&\tau_x=2,
 \end{cases}
\tag{3.3}
\]

where \(q_0,q_1\) are the zero and one children of trie node \(q\);
a missing child contributes zero.  At depth \(k\), the value is the
terminal multiplicity.  The root value is \(Z_A(B,U)\).

#### Proof

If \(x\notin U\), a feasible target must omit \(x\).  If
\(x\in B\), it must contain \(x\).  If \(x\in U\setminus B\), either
choice is allowed.  These are the three lines of (3.3), and induction
on the remaining coordinates proves (3.1).
\(\square\)

Equal residual subtries in (3.3) may be merged.  This gives an
\(A\)-specific reduced ordered decision DAG.  Keeping the full ternary
table gives the uniform worst-case bound (0.4).

### Theorem 3.2 (eight-query cell formula)

For a cell \(C\), define

\[
                         P_J=\bigcup_{i\in J}p_i
 \qquad(J\subseteq C).
\tag{3.4}
\]

Then the exact number of targets of \(A\) fitting \(C\) is

\[
 \boxed{
 Q_A(C)
 =\sum_{J\subseteq C}(-1)^{|J|}
 Z_A(M_C,E_C\setminus P_J).}
\tag{3.5}
\]

In particular,

\[
                         H_A(C)=\mathbf1_{\{Q_A(C)>0\}}.
\tag{3.6}
\]

#### Proof

First impose \(M_C\subseteq T\subseteq E_C\), counted by
\(Z_A(M_C,E_C)\).  For \(i\in C\), let the bad event be
\(T\cap p_i=\varnothing\).  Imposing all bad events indexed by
\(J\subseteq C\) is exactly the upper restriction

\[
                         T\subseteq E_C\setminus P_J.
\]

Inclusion--exclusion gives (3.5).  Formula (1.7) proves (3.6).
Since \(|C|=d+1\le3\), there are at most eight summands.
\(\square\)

This compression is exact for arbitrary \(A\).  It does not use
downward closure, rank projection, or a singleton-target approximation.

## 4. Variable-successor DAG

Let \(G=(V,E)\) be the union of the directed parent paths.  Adjoin a
cemetery symbol \(\bot\).  A selected directed path is represented by

\[
                         \sigma:V\cup\{\bot\}\to V\cup\{\bot\},
\tag{4.1}
\]

where:

- \(\sigma(v)\) is one of the allowed out-neighbors of \(v\), unless
  \(v\) is the sink;
- the sink maps to \(\bot\);
- \(\sigma(\bot)=\bot\);
- the corresponding predecessor map has one source and one sink; and
- the usual global connectivity constraint excludes a disjoint cycle.

The last item belongs to the carrier model, not to the local compiler
DAG.

For every possible window anchor \(v\), introduce the states

\[
 v^{(0)}=v,\qquad
 v^{(j+1)}=\sigma(v^{(j)}),
 \qquad0\le j<11.
\tag{4.2}
\]

These are element/table transitions through the one shared successor
map; they are not separate enumerations of all directed walks.
The label state is

\[
                         w_j=\lambda(v^{(j)})\subseteq[k],
\tag{4.3}
\]

where \(\lambda(v)\) is the fixed middle mask attached to vertex \(v\).

For depth \(d\), if

\[
                         v^{(d+9)}\ne\bot,
\tag{4.4}
\]

the states (4.2)--(4.3) provide the complete word of Lemma 2.1.
Equations (1.2), (1.5)--(1.6), and (3.5) then form a deterministic
acyclic circuit ending in the hit bit

\[
                         h_{v,d}=H_A(C_{v,d}).
\tag{4.5}
\]

The recurrence has twelve layers, independent of the number of parent
paths and of the number of directed walks in their union.

### Lemma 4.1 (one state per actual interior cell)

If \(\sigma\) is one spanning path, the valid pairs \((v,d)\) in
(4.4) are in bijection with all row-depth-\(d\) compiler cells whose
start is at least six and which are not in the right boundary palette.

#### Proof

The local word anchored at \(v\) places its queried erosion cell at
offset six.  Thus its cell start is six positions after \(v\).  A full
word exists exactly when the required right context exists, which is
(4.4).  Moving \(v\) one step along \(\sigma\) moves the cell start one
step, so the correspondence is injective and consecutive.  The omitted
first six starts form the left palette; the starts lacking a full right
context form the right palette.
\(\square\)

## 5. Exact boundary state

The boundary cannot be represented by a scalar \(+36\).  For the unique
source \(s\), form its twelve-vertex prefix

\[
                         W^{\rm L}
 =(s,\sigma(s),\ldots,\sigma^{11}(s)).
\tag{5.1}
\]

For \(d=0,1,2\) and \(j=0,\ldots,5\), evaluate the literal cell

\[
                         C^{\rm L}_{d,j}
 =\{j,j+1,\ldots,j+d\}
\tag{5.2}
\]

in the maximal linear erosion of \(W^{\rm L}\).  Define

\[
                         \beta^{\rm L}_{d,j}
 =H_A(C^{\rm L}_{d,j}).
\tag{5.3}
\]

For the sink \(t\), use the predecessor map to form

\[
                         W^{\rm R}
 =(t,\pi(t),\ldots,\pi^{11}(t)).
\tag{5.4}
\]

This is the reversed suffix convention of the exact boundary auditor.
Define

\[
                         \beta^{\rm R}_{d,j}
 =H_A(C^{\rm R}_{d,j}).
\tag{5.5}
\]

There are precisely

\[
                         2\cdot3\cdot6=36
\tag{5.6}
\]

bits.  Their contribution is their sum, not 36:

\[
                         B_A(\sigma)
 =\sum_{d=0}^{2}\sum_{j=0}^{5}
   (\beta^{\rm L}_{d,j}+\beta^{\rm R}_{d,j}).
\tag{5.7}
\]

For a directed cycle there is no boundary term.  For a path cover,
apply (5.1)--(5.7) independently to every path component having at
least twelve vertices.  A shorter component is itself one exact local
word: evaluate all of its compiler cells directly and count each once.
This finite fallback is needed only to avoid overlap of its two endpoint
palettes; it never occurs for the 6,435-vertex H29 path.

## 6. Proof of Theorem A

Partition the compiler cells of a selected path into:

1. the six leftmost starts in each of the three row depths;
2. the six right boundary starts in each row depth, under reversal; and
3. all remaining interior starts.

The first two classes are disjoint and are evaluated by
(5.3), (5.5).  By Lemma 4.1, the third class is in bijection with the
valid successor states \((v,d)\), and Lemma 2.1 shows that their local
signatures are exact.  Theorem 3.2 computes the Boolean neighborhood
indicator of every cell without target overcounting.

Every compiler cell occurs in exactly one of the three classes.
Summing its indicator proves (0.2).  In particular, if several targets
of \(A\) fit one cell, (3.6) still contributes one.  This is exactly the
set cardinality \(|N_\sigma(A)|\), not the number of target--cell
incidences.
\(\square\)

## 7. Multi-witness and Hall-cut form

Suppose \(A_1,\ldots,A_q\) are DM witnesses from several parents.  Store
the vector

\[
 \mathbf Z(B,U)
 =(Z_{A_1}(B,U),\ldots,Z_{A_q}(B,U)).
\tag{7.1}
\]

The recurrence (3.3) is componentwise, while the structural successor,
erosion, carrier, and boundary DAG is shared.  Formula (3.5) produces
all \(q\) exact hit bits at each cell.

For witness \(A_j\), the Hall cut is

\[
                         |N_\sigma(A_j)|\ge|A_j|.
\tag{7.2}
\]

It may be inserted directly as the pseudo-Boolean inequality

\[
 \sum_{v,d}h^{(j)}_{v,d}
 +\sum_{d,s}
   (\beta^{{\rm L},j}_{d,s}+\beta^{{\rm R},j}_{d,s})
 \ge |A_j|.
\tag{7.3}
\]

This is an exact Benders cut over one selected chronology.  Unlike an
arc-projection cut, it cannot count two incompatible completions of the
same local successor state.

## 8. Certified projection refinement

For completeness, we state the convergent alternative to building the
full successor DAG at once.

For a partial local successor history \(\eta\), let

\[
                         {\cal S}_h(\eta)
\tag{8.1}
\]

be the set of exact depth-twelve states extending its first \(h\)
arcs.  Two partial histories are equivalent at radius \(h\) if:

1. they end at the same directed vertex;
2. they have the same live/dead endpoint status;
3. their compatible exact-state sets in (8.1) agree; and
4. for a boundary history, their unresolved left or right boundary
   indicator sets agree.

The quotient states form a DAG because each transition increases \(h\).
For a cell represented by quotient state \(Q\), define

\[
 \ell(Q)=\min_{\omega\in Q}H_A(\omega),\qquad
 u(Q)=\max_{\omega\in Q}H_A(\omega).
\tag{8.2}
\]

Refining by one arc partitions every \(Q\), so

\[
                         \ell(Q)\ \text{can only increase},\qquad
                         u(Q)\ \text{can only decrease}.
\tag{8.3}
\]

Summing (8.2) over the actual cell positions gives (0.10).  By the
locality lemma, two full radius-twelve histories with the same exact
state have the same hit bit.  Hence every terminal quotient class has
\(\ell=u\), proving (0.11).

This is the proof-safe use of a short projection.  The raw \(U_3,U_4\)
counts retain only a central tuple, discard the completion class, and
therefore need not decrease to the exact value.

## 9. Exact surviving implementation gate

The mathematical compression is complete.  A concrete solver may use
either of two equivalent forms:

1. **Functional form:** selected successor/predecessor variables,
   twelve shared element layers, erosion/carrier gates, ternary-zeta
   lookups, and the exact inequality (7.3).
2. **Refinement form:** begin with short projected states, retain their
   exact completion classes, and split only unresolved classes until
   (0.11).

The functional form has the cleanest proof and the predictable bound
(0.5)--(0.7).  The refinement form can be smaller on a sparse
multi-parent circuit.  Both eliminate the \(213\)M-leaf catalogue and
both retain the boundary exactly.

What remains computational, not mathematical, is choosing the most
efficient low-level representation of the successor element lookup
\(v^{(j+1)}=\sigma(v^{(j)})\) and, in a backend without native table
constraints, the ternary ROM lookup.  Those choices cannot change
\(|N_\sigma(A)|\), because Theorem A fixes the complete recurrence.
