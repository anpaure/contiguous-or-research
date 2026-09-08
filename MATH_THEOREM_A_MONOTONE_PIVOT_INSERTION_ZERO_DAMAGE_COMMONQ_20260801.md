# Monotone pivot insertion: exact zero-damage compiler face and the rank-saturated-cut obstruction

Date: 2026-08-01  
Lane: A, additive-constant common-cap compiler  
Status: exact conditional theorem.  The result proves a genuine `H=1`
zero-matched-damage face.  It also identifies why monotone insertion is not
an unconditional rail compiler: the maximal crossing cells must already be
rank-saturated.  Owner/q1 topology and existence of such a cut in every
Pascal child remain separate.

## 0. Result

Insert one nonempty source letter `X` at a cut.  The old adjacent source
letters are `A_-1,A_1`.  Then

\[
             X\subseteq A_{-1}\cup A_1                     \tag{0.1}
\]

is necessary and sufficient for **every old interval OR** to survive under
convex-hull transport.  Inside the depth-`h` compiler band, the only old
cells whose transported hulls leave the band are the `h-1` crossing cells
of length `h`.  Every other old cell transports injectively and keeps its
literal value.  The new cells not in that transport image are exactly the
singleton `X` and the two prefix rays based at `X`.

Consequently there is an exact positive face.  If every new length-`h+1`
window through the pivot is a legal rank-`m` owner, then the lost crossing
length-`h` cells all have rank `m`; hence no matching of strict-lower targets
uses them.  The whole reference lower matching transports with zero damage.
If the task and the packet's damaged target chains equal the literal values
on the new rays, adjoining all their equality rows to the transported
matching gives a feasible **complete** common-`Q` system.  Thus

\[
                      D\cap C(M_0)=\varnothing .           \tag{0.2}
\]

The local cap footprint is `Theta(h)`, but the matched damage is zero.

The rank condition is essential.  If one maximal crossing cell has a
strict-lower value, its transported hull is a new length-`h+1` window with
the same strict-lower value.  Thus old OR coverage survives, but a flat
rank-`m` carrier is impossible.  This separates unrestricted witness
preservation from compiler/carrier legality.

## 1. Exact interval transport

Write the old source line locally as

\[
 \cdots,A_{-2},A_{-1}\mid A_1,A_2,\cdots
\]

and the new line as

\[
 \cdots,A_{-2},A_{-1},X,A_1,A_2,\cdots .                  \tag{1.1}
\]

For an old interval `I`, let `phi(I)` be its order-preserving copy if it
lies on one side of the cut, and its new convex hull if it crosses the cut.

### Theorem 1.1 (monotone-pivot equivalence)

The following are equivalent.

1. Every old interval keeps its OR under `phi`.
2. The two-point crossing interval keeps its OR.
3. Equation (0.1) holds.

#### Proof

Only a crossing interval gains a source position, namely `X`.  Every such
interval contains both adjacent old positions, so (0.1) implies

\[
 \bigcup_{p\in\phi(I)}A_p
 =X\cup\bigcup_{p\in I}A_p
 =\bigcup_{p\in I}A_p.
\]

Conversely, the old interval consisting of the adjacent positions has OR
`A_-1 union A_1`; preservation of its hull forces (0.1).  \(\square\)

Thus the statement concerns all widths and all old witnesses, not only a
selected protected bank.

## 2. The exact band ledger and the two rays

Let `B_h` denote the interval cells of lengths at most `h`.  For
`1<=i<=h-1`, put

\[
 I_i=\{-i,\ldots,-1,1,\ldots,h-i\}.                      \tag{2.1}
\]

These are the crossing old cells of length `h`.  Put

\[
 \begin{aligned}
 F^-_t&=\{-t,\ldots,-1,0\},\\
 F^+_t&=\{0,1,\ldots,t\},
 \end{aligned}
 \qquad 0\le t\le h-1,                                  \tag{2.2}
\]

where `F^-_0=F^+_0={0}`.

### Theorem 2.1 (exact band exchange)

The map `phi` is an injection from

\[
                   B_h^-\setminus\{I_1,\ldots,I_{h-1}\}
\]

into the new band `B_h^+`.  Its complement is exactly

\[
 \mathcal F_X=\{\{0\}\}\cup
       \{F^-_t:1\le t<h\}\cup\{F^+_t:1\le t<h\}.        \tag{2.3}
\]

Under (0.1), every cell in the domain keeps its literal OR.  The ray values
are

\[
 \begin{aligned}
 R^-_0=R^+_0&=X,\\
 R^-_t&=X\cup\bigcup_{s=1}^{t}A_{-s},\\
 R^+_t&=X\cup\bigcup_{s=1}^{t}A_s
 \qquad(1\le t<h).
 \end{aligned}                                           \tag{2.4}
\]

#### Proof

A crossing old interval of length `j` has a hull of length `j+1`.
Therefore precisely the crossing cells of length `h`, namely (2.1), leave
the band.  Conversely, a new band cell avoiding `0` is an old one-sided
cell.  A new cell containing `0` and old positions on both sides is the
hull of the old crossing cell obtained by deleting `0`.  The only remaining
cells have `0` as an endpoint, giving (2.3).  Deleting `0` recovers the old
cell, so transport is injective.  The value statements follow from Theorem
1.1 and direct union.  \(\square\)

The ledger is therefore `(h-1)` lost cells, `2h-1` new ray cells, and net
gain `h`.

### Corollary 2.2 (exact ray assignment criterion)

Let `N` be an occurrence-labelled multiset of targets to be assigned to
new cells, with the singleton task required at `{0}`.  There is an injective
literal assignment of these occurrences to `mathcal F_X` if and only if the singleton
task equals `X` and, after reserving `{0}`, for every mask `S`,

\[
 \operatorname{mult}_N(S)-\mathbf1_{S=X}
 \le
 \#\{(\epsilon,t):\epsilon\in\{-,+\},\ 1\le t<h,
                         R^\epsilon_t=S\}.                \tag{2.5}
\]

In particular, occurrence-labelled left and right damaged chains
`D^-_t,D^+_t` occupy their natural rays exactly when

\[
                D^-_t=R^-_t,\qquad D^+_t=R^+_t
                \quad(1\le t<h).                          \tag{2.6}
\]

#### Proof

A target is adjacent precisely to the physical ray cells having the same
literal OR.  The equality graph is a disjoint union of complete bipartite
graphs indexed by the mask value.  Its Hall inequalities are exactly the
multiplicity inequalities (2.5).  Equation (2.6) is the fixed-address
specialization.  \(\square\)

This is cell-side injectivity for occurrence requirements.  If the rows are
to be added as edges of a target--cell matching, repeated copies of one mask
represent one target vertex, not several; after discarding redundant copies,
the genuinely new target vertices must also be disjoint from those already
saturated by the transported reference matching.

Thus the two target families must be genuine nested pivot rays; marginal
cardinality or separate fan Hall is not enough.

## 3. The rank-saturated cut

Assume the old source word has flat depth `h`: every old length-`h+1`
window has rank `m`.  The new length-`h+1` windows through `0` are

\[
 J_i=\{-i,\ldots,-1,0,1,\ldots,h-i\},
               \qquad0\le i\le h,                        \tag{3.1}
\]

with values

\[
 T_i^+=X\cup\bigcup_{s=1}^{i}A_{-s}
          \cup\bigcup_{s=1}^{h-i}A_s.                    \tag{3.2}
\]

Call the cut **rank-saturated for `X`** when every set in (3.2) has rank
`m` and is an allowed new middle owner.  Under (0.1), for `1<=i<h`,

\[
                         T_i^+=\bigcup_{p\in I_i}A_p.      \tag{3.3}
\]

### Theorem 3.1 (zero-damage monotone pivot compiler)

Let `M_0` be a reference matching saturating a family `L` of strict-lower
targets by old cells of lengths at most `h`.  Suppose:

1. `X` is nonempty and satisfies (0.1);
2. the cut is rank-saturated for `X`;
3. a task and any damaged packet chains satisfy Corollary 2.2; and
4. every additional physical owner, q1, topology, or upper condition needed
   by the packet is separately valid for the new chronology.

For a combined target--cell matching, assume additionally that each genuinely
new ray target is not already a target vertex of `M_0`; a repeated equality
for an old target is simply a redundant protected row.

Then every edge of `M_0` transports to a distinct new band cell with the
same literal target.  The transported matching is cell-disjoint from all
new ray cells.  Moreover, the plus-state common-`Q` system containing

* every new middle equality,
* every transported edge equality of `M_0`,
* all assigned ray equalities, and
* any chosen old protected interval witnesses transported by `phi`,

is feasible.  In its componentwise maximal word every edge of `M_0` still
holds.  Hence the complete matched damage is zero, as in (0.2).

#### Proof

By (3.3), each lost band cell `I_i` has rank `m`.  It therefore cannot be a
cell of an edge of `M_0`, whose target is strict lower.  Theorem 2.1 now
transports every `M_0` cell injectively inside the new band and preserves
its value.  Its image avoids `mathcal F_X`, again by Theorem 2.1, so the new
ray assignments create no cell conflict.

Use the literal inserted word (1.1).  It realizes every new middle row by
(3.2), every transported matching row and every transported protected row
by Theorem 1.1, and every ray row by (2.4).  Its letters lie in the maximal
middle envelopes because they realize all middle rows.  Thus it is a
nonempty feasible word for the complete assigned common-`Q` system.

The maximal-letter common-`Q` theorem now applies: its maximal word is
nonempty and reproduces every assigned row exactly.  In particular all
transported `M_0` equalities remain true.  Therefore no matched cell belongs
to the complete damage set.  \(\square\)

The proof includes remote common-cap effects rather than checking the task
and rays in isolation: all reference matching rows and every desired
protected witness are present in one common system.

### Corollary 3.2 (one added letter)

Under Theorem 3.1, one physical source letter creates the typed singleton
and both ray banks while retaining the whole old strict-lower matching.
Any final additive charge comes only from failures of the separate
owner/q1/topology rows in item 4, not from the lower common-cap compiler.

### Corollary 3.3 (separated fixed-`H` pivots)

Let `H` cuts be separated so that no old interval of length at most `h`
crosses two of them.  At cut `s`, insert a nonempty `X_s` contained in its
two adjacent old letters.  Suppose every cut is rank-saturated, its ray
assignment passes Corollary 2.2, and the genuinely new target and physical
resource assignments are mutually disjoint.  Then all `H` pivots compose
in one common-`Q` state and

\[
                         D\cap C(M_0)=\varnothing .        \tag{3.4}
\]

The cap support has `Theta(Hh)` positions while the matched damage is zero.

#### Proof

An arbitrary old interval gains precisely the inserted letters at the cuts
it crosses.  For each such cut it contains the two old adjacent letters, so
the corresponding `X_s` is redundant; hence every old OR is preserved even
when the interval crosses several cuts.  A band cell crosses at most one
cut by the separation hypothesis.  Its transport therefore follows the
one-cut ledger, and the only cells which leave the band are the rank-`m`
maximal crossing cells at the individual cuts.  No strict-lower matching
edge uses them.  The transported matching and the `H` ray banks are
cell-disjoint.  Finally the simultaneous inserted word realizes all middle,
transported, ray and protected rows, so the global mixed-row maximal-letter
criterion is feasible and retains every matching row.  \(\square\)

## 4. Sharp incompatibility

### Proposition 4.1 (strict-lower maximal crossing obstruction)

Assume (0.1).  If for some `1<=i<h`

\[
                 \left|\bigcup_{p\in I_i}A_p\right|<m,   \tag{4.1}
\]

then the new central window `J_i` has the same strict-lower value.  Hence
the inserted word cannot have a flat rank-`m` depth-`h` derivative, even
though every old interval OR survives.

#### Proof

Equations (0.1) and (3.3) identify the two unions.  A length-`h+1` central
window of rank below `m` is not a middle owner.  \(\square\)

The obstruction already occurs for `h=2`.  Take the old local source word

\[
                       \{c\},\{a\}\mid\{b\},\{c\}
\]

at middle rank `m=3`; its two old length-three windows both have union
`{a,b,c}`.  Insert `X={a}`.  Condition (0.1) holds, so every old interval
OR survives, but the new central window

\[
                       \{a\},\{a\},\{b\}
\]

has union `{a,b}` and rank two.  Thus unrestricted witness preservation
alone cannot prove a legal compiler/carrier insertion.

### Proposition 4.2 (the canonical shortest rail is never rank-saturated)

Let `h>=2` and use the frozen shortest rotating-hole rail antecedent

\[
                       W_j=K\cup\{z_j\},
             \qquad |K|=m-h-1,                            \tag{4.2}
\]

where the active labels `z_j` run around the `(h+3)`-cycle.  At any internal
cut of its linear unrolling, insert a letter `X` satisfying the monotone
condition (0.1).  Then every interior new central window through the pivot
has rank `m-1`.  In particular no choice of the rail parameters makes this
pure insertion a flat rank-`m` depth-`h` compiler.

#### Proof

An old crossing interval of length `h` contains `h` distinct active labels
and the common core `K`; hence its union has rank

\[
                         |K|+h=m-1.                        \tag{4.3}
\]

It contains both adjacent old letters.  Therefore (0.1) makes `X`
redundant in its new hull, and (3.3) shows that the corresponding central
window still has rank `m-1`.  Since `h>=2`, there is at least one such
interior window.  \(\square\)

Thus the monotone pivot completely defeats the rail-amplified *matching*
damage only on a prepared rank-saturated host.  It cannot be inserted into
the rail's canonical maximal erosion source.  On that source, raising the
new central windows to rank `m` requires a coordinate outside at least one
old crossing union, which is exactly a departure from monotone
old-witness preservation.

## 5. Scope

The theorem proves the requested `H=1` **zero residual compiler-damage**
face under an exact, checkable rank-saturated-cut and ray-equality
hypothesis.  Proposition 4.2 proves that the frozen rail's own canonical
erosion cut is not such a host.  A successful use must therefore plant the
rail packet at a different rank-saturated cut or use a noncanonical/nonflat
antecedent.  The remaining host statement is
precisely the simultaneous existence of:

1. a rank-saturated cut;
2. a task `X` contained in the adjacent old union;
3. the required two literal ray decks; and
4. the separate owner/q1/topology realization.

Without item 1, Proposition 4.1 is a minimal obstruction.  Without item 3,
Corollary 2.2 is the exact multiplicity certificate.  Neither obstruction
is visible from the raw count of `2h-1` new fan cells.
