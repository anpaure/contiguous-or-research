# Right-functional compiler fibres and the eroded duplex Pascal lift

Date: 2026-07-30  
Lane: R, all-`k` compiler theorem  
Status: exact integral theorems; conditional recursive closure; no finite
`k=16` search and no unconditional all-`k` word.

## 0. Main result

An exact middle/upper carrier is not a compiler.  The remaining lower problem
has, however, a sharper form than a general bipartite Hall problem.

For one fixed literal source `Q`, every physical interval occurrence has one
and only one OR label.  Consequently the target-to-cell graph is a disjoint
union of stars.  Its deficiency is exactly the number of target labels with
zero occurrences.  A forced occurrence-labelled duplex provider consumes no
matching capacity after `Q` is fixed; its only cost is that its provider
equation filters the common-source fibre.

Thus the exact compiler functional is

\[
 \boxed{
 \Delta(\mathcal F;\mathcal P)
 =\min_{Q\in\mathcal F_{\mathcal P}}
   \#\{T\in\mathcal L\setminus\operatorname{dom}\mathcal P:
                     m_Q(T)=0\}.}                  \tag{0.1}
\]

Here `mathcal F_P` is the fibre satisfying all owner, seam, duplex-source and
forced-provider equations, and `m_Q(T)` is the number of free physical
intervals whose literal `Q`-union is `T`.  A carrier compiles exactly when
`Delta=0`; by convention `Delta=+infinity` if the constrained fibre is empty.

Pascal tag signatures are additive for each fixed `Q`.  They become
independently optimizable only when the constrained fibre is rectangular
across the signature modules.  A four-position source example proves that
blockwise minima and the union candidate graph can both be perfect while no
single `Q` supports the forced port and the other target.

For the duplex recursion there is one further exact obstruction.  Canonical
suspension

\[
                  Q^z_p=\{z\}\cup A_p,qquad A_p\ne\varnothing, \tag{0.2}
\]

transports every tagged target `z union X` with nonempty old core `X`, but no
interval realizes the new singleton `{z}`.  The minimal repair *within the
erosion-only duplex class* is to erase the old core at one
**socket-redundant** source position.  If its old contribution is also
redundant in every selected matching interval and protected future collar
which contains it (avoidance is the simplest special case), the eroded source
preserves every connector and facet owner, preserves the renewable port,
transports all nonempty tagged cores, and supplies `{z}` as one literal source
cell.  This gives a genuine one-step compiler closure theorem under explicit
hypotheses.

The remaining *one-step* existence gate is correspondingly precise:
construct a PBBS/Pascal child whose projected common-source fibre contains
such a redundant erasure while the no-tag and nonempty-tag compiler banks
remain exact.  Iteration has an additional bulk obstruction.  After the next
fresh coordinate, a sector bearing `z` while avoiding `y`, with `z` absent
outside that sector, can realize every lower target containing both `z,y`
only across a tag boundary.  With `t` boundaries and deadline horizon `d`,
there are at most `t binom(d,2)` such short intervals, versus exponentially
many required mixed targets.  Thus a genuine all-`k` recursion needs a bulk
mixed-tag compiler module, not only the renewable sector and `O(k)` seam
ports.  Scalar Hall slack and carrier completeness imply neither condition.

## 1. Fixed-source compiler graphs are right-functional

Let `mathcal C` be a set of occurrence-labelled nonempty physical source
intervals, let `mathcal L` be a set of distinct required labels, and let `Q`
be one fixed nonzero source.  After deleting any already protected target
demands and occurrence cells, denote the residual banks by
`mathcal L_res` and `mathcal C_free`.  Define

\[
 \lambda_Q(C)=\bigcup_{p\in C}Q_p                 \tag{1.1}
\]

and the residual exact candidate graph

\[
 T\sim_Q C\quad\Longleftrightarrow\quad
                  \lambda_Q(C)=T,
 \qquad (T,C)\in\mathcal L_{\rm res}\times
                     \mathcal C_{\rm free}.          \tag{1.2}
\]

For a free-cell bank `mathcal C_free`, put

\[
 m_Q(T)=
 \#\{C\in\mathcal C_{\rm free}:\lambda_Q(C)=T\}.  \tag{1.3}
\]

### Theorem 1.1 (right-functional Hall collapse)

The neighborhoods of two distinct target labels are disjoint.  Hence

\[
 \nu(G_Q)=\#\{T\in\mathcal L_{\rm res}:m_Q(T)>0\},\tag{1.4}
\]

and the matching deficiency is

\[
 \boxed{
 \operatorname{def}(G_Q)
 =\sum_{T\in\mathcal L_{\rm res}}\mathbf 1[m_Q(T)=0].} \tag{1.5}
\]

More generally, if target `T` has integral demand `b_T`, then

\[
 \boxed{
 \operatorname{def}_{\mathbf b}(G_Q)
 =\sum_{T\in\mathcal L_{\rm res}}(b_T-m_Q(T))^+.} \tag{1.6}
\]

#### Proof

One physical interval has the single label (1.1), so it cannot be adjacent
to two distinct left labels.  Thus for unit demands `G_Q` is a disjoint union
of stars.  For demand `b_T`, its component is
`K_(b_T,m_Q(T))` (equivalently one left vertex of capacity `b_T`).  Its
maximum matching leaves `(b_T-m_Q(T))^+` demands unmatched.  Summing proves
(1.4)--(1.6).  \(\square\)

This does not make the compiler trivial: before `Q` is fixed, owner and
provider equations couple all interval labels.  It does show that after the
common-source choice there is no further multi-target Hall interaction.

### Corollary 1.2 (forced providers have zero fixed-source matching tax)

Let

\[
 \mathcal P=\{(T_j,C_j):1\le j\le s\}              \tag{1.7}
\]

be distinct exact protected edges under `Q`, with distinct target labels and
distinct occurrence-labelled cells.  Remove their labels and cells from the
residual unit-demand problem.  Every other target multiplicity is unchanged.
For general demands with `b_T>=1` and `m_Q(T)>=1`, consuming one occurrence
and one unit of the same target leaves its deficiency unchanged:

\[
 ((b_T-1)-(m_Q(T)-1))^+=(b_T-m_Q(T))^+.            \tag{1.8}
\]

#### Proof

The removed cell `C_j` has label `T_j` and therefore belongs to no other
target neighborhood.  Equation (1.8) is immediate.  \(\square\)

The port can still be expensive by deleting sources from the admissible
fibre.  That is the only possible cost in the unit-demand exact-label model.

## 2. The exact fibre functional

Let `mathcal F` be the full source fibre satisfying nonemptiness, envelope
containment, every central owner equation and every cross-interface equation.
Let `mathcal P` be a typed protected port whose protected target labels are
pairwise distinct and whose protected occurrence cells are pairwise distinct.
Besides exact provider equations, `mathcal P` may contain suspension, copy,
future-collar, or other typed source relations.  Define

\[
 \mathcal F_{\mathcal P}
 =\{Q\in\mathcal F:Q\text{ satisfies every typed relation of }\mathcal P,
       \ \lambda_Q(C_j)=T_j\text{ for every protected provider }(T_j,C_j)\}.
                                                               \tag{2.1}
\]

Delete the protected demands and protected cells before computing every
`m_Q(T)` in (0.1).  For unit demands, define `Delta` by (0.1), with

\[
 \Delta(\mathcal F;\mathcal P)=+\infty
 \quad\text{when }\mathcal F_{\mathcal P}=\varnothing.          \tag{2.2}
\]

### Theorem 2.1 (minimal typed compiler criterion)

Fix an exact middle deck, a complete upper catalogue, the physical source
positions, and a protected port `mathcal P`.  A literal terminal compiler
preserving that port exists if and only if

\[
                         \boxed{\Delta(\mathcal F;\mathcal P)=0.} \tag{2.3}
\]

When (2.3) holds, choose one occurrence of every residual target; these cells
are automatically distinct and unite with `mathcal P` to form the compiler
matching.

#### Proof

If `Delta=0`, take a minimizing `Q`.  Every residual label has a free
occurrence, and Theorem 1.1 makes arbitrary one-per-label choices injective.
The protected edges remain exact by (2.1).  Conversely, the source of any
completing compiler belongs to `mathcal F_P` and gives every residual target
positive multiplicity.  \(\square\)

The quantifiers cannot be interchanged.  It is insufficient that every
target occurs under some source in `mathcal F_P`, or that the union of the
candidate graphs passes Hall.

## 3. Pascal tag signatures

Let `Z` be a fixed tag set.  Partition target labels by their exact tag
signature

\[
 \mathcal L_\sigma
 =\{T\in\mathcal L:T\cap Z=\sigma\},
 \qquad \sigma\subseteq Z.                         \tag{3.1}
\]

For fixed `Q`, partition physical cells by the signature of their actual
label:

\[
 \mathcal C_\sigma(Q)
 =\{C\in\mathcal C:\lambda_Q(C)\cap Z=\sigma\}.   \tag{3.2}
\]

### Theorem 3.1 (fixed-source signature decomposition)

For every fixed `Q`,

\[
 G_Q=\bigsqcup_{\sigma\subseteq Z}G_{Q,\sigma},
 \qquad
 \operatorname{def}(G_Q)
 =\sum_{\sigma\subseteq Z}\operatorname{def}(G_{Q,\sigma}). \tag{3.3}
\]

Suppose now that `Z` is fresh: it is disjoint from every old source letter
and every old target label.  For a common-tag suspension

\[
 Q^Z_p=Z\cup Q_p,                                  \tag{3.4}
\]

there is an occurrence-preserving identity

\[
 m_{Q^Z}(Z\cup T)=m_Q(T)                            \tag{3.5}
\]

on every transported cell bank.  Copy while avoiding a fresh tag also
preserves every multiplicity.

#### Proof

A cell adjacent to `T` has the same tag signature as `T`; hence (3.3) is a
disjoint-union decomposition.  Equation (3.5) follows from

\[
 \lambda_{Q^Z}(C)=Z\cup\lambda_Q(C).               \tag{3.6}
\]

\(\square\)

Thus the renewable duplex germ pays zero fixed-source matching tax inside
its transported signature block.  What can fail is simultaneous choice of
one `Q` across the blocks.

### Theorem 3.2 (rectangular-fibre factorization)

Suppose there is a fixed, source-independent partition of the residual cells

\[
 \mathcal C_{\rm free}=\bigsqcup_{\sigma\subseteq Z}\mathcal C_\sigma,
                                                               \tag{3.7}
\]

such that every cell in `mathcal C_sigma` has signature `sigma` throughout
the constrained fibre.  Suppose also that the constrained fibre has a true
Cartesian parametrization by nonempty, disjoint source-variable modules,

\[
 \mathcal F_{\mathcal P}
   \cong\prod_{\sigma\subseteq Z}\mathcal F_\sigma, \tag{3.8}
\]

and the full labels of cells in the `sigma` block depend only on `Q_sigma`.
All graphs below are residual graphs.  Then

\[
 \boxed{
 \Delta(\mathcal F;\mathcal P)
 =\sum_{\sigma\subseteq Z}
      \min_{Q_\sigma\in\mathcal F_\sigma}
          \operatorname{def}(G_{Q_\sigma,\sigma}).} \tag{3.9}
\]

In particular, exact compilation in every signature block implies one exact
global compiler.

#### Proof

Apply (3.3).  Under (3.7)--(3.8) the variables in its summands are
independent, so the minimum of the sum is the sum of the minima.  \(\square\)

### Proposition 3.3 (minimal fibre-correlation obstruction)

Take one owner `1234` at horizon three on four nonempty source positions and
the two-source fibre

```text
Q^0 = (14,14,23,3),
Q^1 = (4,2,14,3).
```

Both sources union to `1234`.  Let coordinate `4` be the tag, force target
`A=14` to use cell `[0,0]`, and also require target `B=2`.

- Under `Q^0` the forced edge is exact, but no interval has OR `2`.
- Under `Q^1`, cells `[2,2]` and `[1,1]` cover `A` and `B`, but `[0,0]`
  has OR `4`, so the forced edge fails.

The union candidate graph contains the distinct cells `A->[0,0]` and
`B->[1,1]`.  Before the natural join with the forced-port relation, the tag
module has a zero-deficiency choice `Q^0` and the no-tag module has a
zero-deficiency choice `Q^1`.  But forcing `A->[0,0]` leaves the constrained
fibre `{Q^0}`, where `B` has deficiency one.  Hence separate projection
minima and union-Hall are both invalid substitutes for the common natural
join required in Theorem 3.2.  \(\square\)

## 4. The singleton obstruction in a duplex suspension

### Proposition 4.1 (empty-core obstruction)

Suppose every source letter is nonempty.  In a canonical suspended sector

\[
 Q^z_p=\{z\}\cup A_p,
 \qquad A_p\ne\varnothing.                          \tag{4.1}
\]

Every nonempty physical interval has a nonempty old-coordinate core.
Therefore

\[
             \boxed{\{z\}\notin\operatorname{IntOR}(Q^z).} \tag{4.2}
\]

More generally, if every no-tag letter is nonempty and every tag-containing
letter has nonempty old core, no interval anywhere in the source realizes
`{z}`.

#### Proof

The union of one or more nonempty old cores is nonempty.  Adding `z` cannot
remove it.  An interval of no-tag letters omits `z`.  \(\square\)

The canonical duplex transport therefore carries every nonempty tagged core
but misses the unique tagged target whose old core is empty.  A literal
tag-only source cell repairs it.  The next section characterizes when such a
cell can be made by erosion without changing the declared owner windows; it
does not exclude a different architecture which supplies a noncanonical
tag-only cell.

## 5. Socket-redundant erosion

Let a parent source `A=(A_p)` realize the connector chronology at horizon
`D>=1`.  Assume it is order-one transparent, so its `D`-position overlap
windows realize the facet chronology at horizon `D-1`.  Let `mathscr J`
contain every declared internal source window whose union must be preserved:
in particular every connector window of `D+1` positions and every facet
window of `D` positions, including cyclic wraps or the literal linear
endpoint-completion windows.  Any affected cross-interface window not put in
`mathscr J` must instead be checked by the global-extension hypothesis in
Theorem 6.1.

### Definition 5.1

A source position `p_*` is **socket-redundant** when

\[
 \boxed{
 A_{p_*}\subseteq
 \bigcup_{q\in J\setminus\{p_*\}}A_q
 \quad\text{for every }J\in\mathscr J\text{ containing }p_*.} \tag{5.1}
\]

Define

\[
 B_{p_*}=\varnothing,
 \qquad B_p=A_p\ (p\ne p_*),                       \tag{5.2}
\]

and the eroded tagged source

\[
 Q^{z,B}_p=\{z\}\cup B_p.                          \tag{5.3}
\]

### Lemma 5.2 (owner-preserving singleton erasure)

If `p_*` is socket-redundant, (5.3) realizes exactly the same suspended
connector and facet owners as the canonical source (4.1), and

\[
                         Q^{z,B}_{p_*}=\{z\}.       \tag{5.4}
\]

#### Proof

For a declared window not containing `p_*`, nothing changes.  If `p_* in J`,
(5.1) gives

\[
 \bigcup_{p\in J}B_p=\bigcup_{p\in J}A_p.          \tag{5.5}
\]

Adjoining `z` preserves its connector or facet owner.  Equation (5.4) is
immediate.  \(\square\)

### Proposition 5.3 (necessity for erosion-only repair)

Let `B_p subseteq A_p`, suppose the eroded tagged source preserves every
declared connector and facet owner, and suppose some interval realizes
`{z}`.  Every position in that witnessing interval has `B_p=emptyset` and is
socket-redundant in the sense of (5.1).  Consequently, if no position is
socket-redundant, no multi-position erosion-only duplex lift can realize
`{z}`.

#### Proof

An interval realizes `{z}` only if every one of its old cores `B_p` is empty.
For such a position `p` and every declared window `J` containing it, owner
preservation gives

\[
 \bigcup_{q\in J}A_q=\bigcup_{q\in J}B_q.
\]

The right side is contained in `union_(q in J minus {p}) A_q`, which proves
(5.1).  \(\square\)

### Lemma 5.4 (exact selected-interval survival test)

For any occurrence-labelled source interval `C`, eroding only `p_*` preserves
its old-coordinate union if and only if either `p_* notin C` or

\[
 A_{p_*}\subseteq
       \bigcup_{q\in C\setminus\{p_*\}}A_q.          \tag{5.6}
\]

Thus a family of selected matching edges, port providers, and future collar
intervals survives the erasure exactly when (5.6) holds for every member of
the family which contains `p_*`.

#### Proof

Only `A_(p_*)` is deleted.  Its deletion changes `union_(q in C)A_q` exactly
when it contains a coordinate absent from every other `A_q`, `q in C`.
This is precisely the negation of (5.6).  \(\square\)

## 6. One-erasure Pascal compiler closure

Let `r>=2`, let the old ground be `Omega` of size `2r-1`, let
`z notin Omega`, and split
the strict lower targets of the rank-`r` even child on `Omega union {z}` as

\[
\begin{aligned}
 \mathcal L_0
 &=\{X\subseteq\Omega:1\le |X|\le r-1\},\\
 \mathcal L_1
 &=\{\{z\}\cup X:X\subseteq\Omega,
                         0\le |X|\le r-2\}.         \tag{6.1}
\end{aligned}
\]

### Theorem 6.1 (one-erasure inductive compiler)

Assume all of the following.

1. Under a prescribed no-tag source, a no-tag sector has a protected exact
   matching `M_0` covering every label in `mathcal L_0`.
2. A prescribed parent source `A` has a protected exact matching `M_1`
   covering every nonempty old core `X subseteq Omega` with
   `1<=|X|<=r-2`.  Every exported lower provider of the renewable duplex
   germ is one of the selected edges of `M_1`.
3. One position `p_*` is socket-redundant and every interval of `M_1` which
   contains `p_*` satisfies the exact redundancy test (5.6).
4. The no-tag and tagged sector embeddings preserve the selected physical
   intervals, and the images of `M_0`, `M_1`, and `[p_*,p_*]` are pairwise
   distinct occurrence-labelled cells.
5. All sector assignments, boundary assignments, duplex relations, and
   cross-interface owner equations have one common **nonempty** global
   child-source extension `Q` in the post-erasure child carrier fibre.  On
   the `M_0` bank, `Q` restricts to the prescribed no-tag source; on the
   tagged bank it restricts to the eroded source `Q_p={z} union B_p`; on the
   germ it satisfies the declared parent--child duplex relation; and it
   satisfies every protected mixed/interface future-collar equation.
6. Every exported germ provider interval and every wholly tagged-bank source
   interval in its complete declared future facet/bridge dependency collars
   which contains `p_*` satisfies (5.6).  Mixed/interface dependencies are
   covered instead by hypothesis 5.
7. Under that same post-erasure source `Q`, the child carrier has exact middle
   ownership, complete upper replay, residence, and legal physical
   boundaries.

Then the child has a literal common source and an exact matching of its whole
strict lower ideal.  Explicitly,

\[
\begin{aligned}
 M={}&M_0^{\rm no\text{-}tag}\\
 &\sqcup
 \{\{z\}\cup X\longmapsto\iota_1(M_1(X)):
                         1\le|X|\le r-2\}\\
 &\sqcup
 \{\{z\}\longmapsto[\iota_1(p_*),\iota_1(p_*)]\}. \tag{6.2}
\end{aligned}
\]

The compiler preserves the renewable duplex germ.  If the carrier has `W`
middle owners and `W+d` source positions, its source word is universal at the
deadline length `B(k)=W+d`.

#### Proof

The no-tag matching is unchanged.  Lemma 5.4 and hypothesis 3 show that
eroding `p_*` leaves the old union `X` of every `M_1` interval unchanged.  In
the tagged source its union is therefore `{z} union X`.  Lemma 5.2 supplies
the remaining singleton `{z}` while preserving all connector and facet
owners.  The three physical cell families are disjoint by hypothesis 4 and
cover exactly (6.1).

Hypothesis 5 makes these sector assignments one source, rather than separate
compilers.  Because the germ's lower provider is already an edge of `M_1`,
it consumes no additional occurrence.  Hypothesis 6 preserves every duplex
edge and its complete declared future collar.
Hypothesis 7 supplies the middle and upper ideals and every physical
obligation.  The resulting word is universal; the final length statement is
the deadline ledger.  \(\square\)

The theorem is integral and occurrence-labelled.  It does not append a hole,
alter the exact carrier, or choose independent rankwise sources.

## 7. Recursive all-`k` implication and remaining gate

### Corollary 7.1 (typed recursive implication)

Suppose a typed recursion has an initial compiler/socket base case and, at
every odd-to-even lift covered by Theorem 6.1:

1. the exact middle/upper/residence data in Theorem 6.1;
2. the renewable duplex sector socket of the preceding report;
3. the two protected parent compiler banks `M_0,M_1`;
4. a socket-redundant source position satisfying (5.6) throughout `M_1`, the
   germ, and its complete future dependency collars; and
5. a nonempty relational natural join giving the common global source.

Assume additionally that the output type of each lift is literally the input
type of the next lift, and that every intervening parity transition not
covered by Theorem 6.1 has its own verified compiler- and
deadline-position-count-preserving theorem.
Then Theorem 6.1 composes with those typed transition theorems and produces
deadline-length universal words throughout that recursion.  Together with
the deadline lower bound, these words are optimal.

The exact unproved one-step existence statement is:

> **Redundant-core duplex compiler lemma (UNPROVED).**  Construct one
> recursive PBBS/Pascal family in which the two inherited compiler banks and
> a renewable duplex germ admit, at every lift, one source position satisfying
> (5.1) and (5.6) for the nonempty-core matching and every future dependency
> collar, while all cross-interface source equations have a common solution.

This is strictly sharper than asking for scalar Hall slack.  It identifies the
new singleton `{z}`, owner-preserving redundancy, matching survival, and
source-fibre amalgamation separately.

It is not by itself an all-`k` construction.  In the next two-coordinate
round, let the old ground have size `2r`, let the fresh coordinates be `z,y`,
and let the new middle rank be `R=r+1`.  Suppose a linear horizon-`d` child
source has a sector-position set `P` satisfying

\[
 p\in P\Rightarrow z\in Q_p,\ y\notin Q_p,
 \qquad
 p\notin P\Rightarrow z\notin Q_p.                 \tag{7.1}
\]

If `t` adjacent pairs cross between `P` and its complement, complete strict
lower coverage forces

\[
 \boxed{
 t\binom d2\ge
   \sum_{j=0}^{r-2}\binom{2r}{j}.}                 \tag{7.2}
\]

Indeed each target `{z,y} union X`, `|X|<=r-2`, has rank at most `R-1`.
Every lower witness has at most `d` source letters because any `d+1`
consecutive letters contain a rank-`R` owner.  By (7.1) it crosses a boundary
of `P`; one boundary belongs to only `binom(d,2)` intervals of length at most
`d`.  Union-bounding over the `t` boundaries proves (7.2).  In a cyclic
version the wrap adjacency must be counted as well.

At `d=Theta(sqrt(r))`, even `t=O(r)` is polynomial while the right side of
(7.2) is exponential.  More exactly, any construction satisfying the
corresponding exhaustive internal/boundary dichotomy must provide internal
witnesses for all but `t binom(d,2)` members of this mixed-tag family: all but
`O(k)` when `t=O(1)`, and all but `O(k^2)` when `t=O(k)`.  Alternatively it
must abandon the support separation (7.1) or charge further escape
boundaries.  This **mixed-bulk compiler lemma is UNPROVED**.  The full proof
and the exact one-cut repair ledger are recorded separately in
`MATH_THEOREM_R_DUPLEX_COMPILER_TAG_BLOCK_AND_MIXED_BULK_OBSTRUCTION_20260730.md`.

The independently reported `k=16` exact/upper-complete carriers confirm only
the carrier side of Theorem 6.1.  Their reported compiler/Hall deficiencies
are `34/35`, but the carrier statement alone does not identify those numbers
with `Delta`.  If they were computed after fixing a literal source `Q`, they
are `def(G_Q)>0`; if they were computed in a pre-source candidate/domain
graph, they are an outer Hall obstruction.  Only minimization over the full
typed constrained source fibre computes `Delta`.  In every interpretation
the data confirm that exact ownership and upper completeness do not
themselves imply the compiler theorem; they neither prove nor refute the
redundant-core lemma for a recursive family.

## 8. Audit boundary

All statements above are pure finite mathematics; no SAT, exhaustive search,
web access, or remote computation was used.  The decisive distinctions are:

1. right-functionality holds only after one common source is fixed;
2. fixed-source tag deficiencies add, but minima add only for rectangular
   fibres;
3. the canonical suspension preserves every nonempty tagged core but not the
   empty core;
4. socket redundancy is both sufficient for one erasure and necessary for
   every erosion-only singleton repair; and
5. Theorem 6.1 remains conditional on literal global source amalgamation and
   the exact carrier hypotheses.
