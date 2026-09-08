# Odd-to-even reroot, pinned schedule, and maximal-common-cap compiler

Date: 2026-07-31  
Status: proved reusable reduction; K16 corollary instantiated by an exact
optimal word  
Scope: finite Boolean lattices and contiguous-OR words

## 1. Purpose

The successful K16 construction has four logically separate parts:

1. lift an odd-dimensional physical word into the two shores of the next
   even middle layer;
2. change only block orientations at a few boundaries until every upper
   target has a consecutive middle-row witness;
3. retime the middle rows and pin a required lower target at one physical
   source position; and
4. choose all remaining lower witnesses simultaneously, not independently.

The first three parts produce a compiler-ready scaffold.  The fourth part is
an exact integral matching problem with a canonical maximal solution.  This
note isolates the reusable lemmas and the precise remaining hypothesis for a
general construction.

## 2. Two-shore odd-to-even owner lift

Let \(k=2r\), let \(z\) be the new coordinate, and regard
\([k-1]\) as the old coordinates.  The middle layer splits disjointly as

\[
 { [k]\choose r}
 =
 { [k-1]\choose r}
 \mathbin{\dot\cup}
 \{\,\{z\}\cup S:S\in{[k-1]\choose r-1}\,\}.
\tag{2.1}
\]

### Lemma 2.1 (two-shore owner lift)

Suppose \(U\) lists every old \(r\)-set exactly once and \(L\) lists every
old \((r-1)\)-set exactly once.  Then any interleaving of \(U\) and
\(z\vee L\) lists the complete rank-\(r\) layer of \(B_k\) exactly once.
Orienting or permuting consecutive blocks of either list preserves this
ownership statement.

#### Proof

The first shore consists exactly of the middle sets not containing \(z\);
the second consists exactly of those containing \(z\).  The shores are
disjoint, and deletion of \(z\) is a bijection from the second shore to the
old rank-\((r-1)\) layer.  Block orientation and order do not change either
multiset.  \(\square\)

The lemma deliberately asserts ownership only.  Johnson adjacency, upper
coverage, residence, and compiler compatibility are separate boundary
conditions.

In the K16 instance, the authenticated K15 parent \(w\) has

\[
 U_i=w_i\vee w_{i+1}\vee w_{i+2}\vee w_{i+3}
\]

equal to the complete old rank-eight layer.  Its three-letter trace

\[
 L_i=w_i\vee w_{i+1}\vee w_{i+2}
\]

contains every old rank-seven mask once and one exceptional rank-six mask.
Deleting the exceptional entry and applying Lemma 2.1 gives the natural K16
middle ownership deck.

## 3. Oriented-block boundary localization

Let \(T=(T_0,\ldots,T_{W-1})\) be any target chronology and partition it into
consecutive blocks \(B_1,\ldots,B_t\).  Let \(T'\) be obtained by orienting
each block forward or backward and concatenating the oriented blocks in a
specified order.  Define

\[
 {\cal U}(T)=
 \left\{
   \bigvee_{i=a}^{b}T_i:0\le a\le b<W
 \right\}.
\tag{3.1}
\]

### Lemma 3.1 (boundary localization)

The set

\[
 {\cal U}_{\rm int}=
 \bigcup_{j=1}^{t}
 \left\{
   \bigvee_{T_i\in J}T_i:
   J\text{ is an interval wholly inside }B_j
 \right\}
\tag{3.2}
\]

is invariant under every block orientation.  Moreover

\[
 {\cal U}(T')={\cal U}_{\rm int}\cup{\cal U}_{\partial}(T'),
\tag{3.3}
\]

where \({\cal U}_{\partial}(T')\) consists exactly of interval unions that
cross at least one new block boundary.

Consequently \(T'\) is upper-complete if and only if every target outside
\({\cal U}_{\rm int}\) is supplied by a cross-boundary interval of \(T'\).

#### Proof

Reversal bijects the intervals of a block with themselves and preserves the
OR of each reversed interval.  Every interval of \(T'\) is either internal
to one block or crosses a block boundary, giving (3.3).  The final statement
is immediate.  \(\square\)

For a prefix or suffix reroot, \(t=2\) or \(3\).  Thus a global upper audit
can be compressed to:

- an inventory of targets with internal witnesses, which are automatically
  safe; and
- an exact census of intervals crossing the changed seams.

For rank \(r+1\), the new witnesses reduce further to adjacent seam unions.
Deeper upper targets may use longer cross-seam intervals and must not be
replaced by a fixed-width proxy.

The lemma is a localization theorem, not an existence theorem.  It explains
why two endpoint reroots were auditable in K16; it does not promise that
boundedly many reroots work in every dimension.

## 4. Pinned monotone schedules

Let \(T_0,\ldots,T_{W-1}\) be middle targets.  A physical schedule assigns
each row a nonempty integer interval

\[
 I_i=[s_i,d_i]\subseteq[0,L-1].
\tag{4.1}
\]

Assume the starts and deadlines are strictly increasing with \(i\).  The
maximal middle envelope is

\[
 E_p=\bigcap_{i:p\in I_i}T_i,
\tag{4.2}
\]

with an empty intersection interpreted as the full coordinate set.

### Lemma 4.1 (exact positional cap criterion)

Assume first that the uncapped maximal envelope is nonempty and realizes
every middle row:

\[
 E_q\ne\varnothing\quad(0\le q<L),
 \qquad
 \bigvee_{q\in I_i}E_q=T_i\quad(0\le i<W).
\]

Fix a position \(p\) and a nonempty cap \(C\subseteq E_p\).  Put

\[
 E^{(p,C)}_q=
 \begin{cases}
 C,&q=p,\\
 E_q,&q\ne p.
 \end{cases}
\tag{4.3}
\]

The capped maximal envelope realizes every middle row exactly if and only if
for each \(i\) with \(p\in I_i\),

\[
 C\ \vee\!
 \bigvee_{q\in I_i\setminus\{p\}}E_q
 =T_i.
\tag{4.4}
\]

Rows not containing \(p\) remain exact by the baseline hypothesis.

#### Proof

Every envelope letter on \(I_i\) is a subset of \(T_i\), so no extra
coordinate can appear.  After changing only position \(p\), equality of the
row OR is exactly (4.4).  Every row not containing \(p\) is unchanged and is
exact by assumption.  \(\square\)

For a singleton \(C=\{z\}\), Lemma 4.1 is the exact singleton-retiming test.
If the one-cell interval \(\{p\}\) is a physical lower cell, it can be
reserved for the singleton target before the remaining matching is chosen.
An existential requirement that \(\{z\}\) occur somewhere is weaker and is
not a substitute for this positional criterion.

### Lemma 4.2 (omitted-hole area identity)

Suppose the physical positions are \(0,\ldots,L-1\), the \(W\) row starts
are the complement of a set \(X\), the \(W\) row deadlines are the
complement of a set \(Y\), and starts and deadlines are paired in increasing
order.  Then the total proper-prefix area is

\[
 {\cal A}:=\sum_{i=0}^{W-1}(d_i-s_i)
          =\sum_{x\in X}x-\sum_{y\in Y}y.                 \tag{4.5}
\]

Consequently, replacing one omitted deadline \(y\) by \(y+t\), while
preserving distinctness and schedule legality, decreases \({\cal A}\) by
exactly \(t\).  Replacing one omitted start \(x\) by \(x+t\) increases it
by exactly \(t\).

#### Proof

Both selected coordinate sets are complements in the same position set, so

\[
 \sum_i d_i=\sum_{p=0}^{L-1}p-\sum_{y\in Y}y,
 \qquad
 \sum_i s_i=\sum_{p=0}^{L-1}p-\sum_{x\in X}x.
\]

Subtracting gives (4.5), and the two retiming assertions follow. \(\square\)

This identity counts proper-prefix area, not all boundary-truncated cells.
Its role is to quantify the exact cost of moving a deadline to a position at
which Lemma 4.1 permits a required singleton or facet cap; boundary cells and
reserved pins must still be counted literally.

### Corollary 4.3 (singleton-frontier contraction)

Let \(\Sigma\) be any finite family of monotone schedules for the same middle
chronology, and let \({\cal F}_z\) consist of the pairs \((\sigma,p)\) for
which the uncapped maximal envelope is exact, the cap \(C=\{z\}\subseteq
E_p\) passes Lemma 4.1, and \(\{p\}\) is a physical lower cell.  A compiler
in \(\Sigma\) with a one-cell witness for \(\{z\}\) exists if and only if,
for some \((\sigma,p)\in{\cal F}_z\), the residual
common-cap system obtained by

1. fixing \(M(\{z\})=\{p\}\),
2. deleting the target \(\{z\}\) and cell \(\{p\}\), and
3. building every remaining domain from the capped envelope,

is feasible by Theorem 6.1.

Indeed, in every nonempty final common cap the pinned letter is a nonempty
subset of \(\{z\}\), and therefore equals \(\{z\}\).  Conversely every
compiler with that one-cell witness induces one member of \({\cal F}_z\) and
a feasible residual assignment.  Residual cells may overlap \(p\); they are
not forbidden a priori, but common-cap nonemptiness forces their labels to
retain \(z\).  Thus the exact order is **retime, cap, contract, then match**.
A Hall graph built before the cap is not the residual graph in this theorem.

## 5. The complete lower-cell catalogue

For a fixed schedule define

\[
 {\cal C}_{\rm full}=
 \left\{
 J\subseteq[0,L-1]:
 J\text{ is an interval and contains no complete }I_i
 \right\}.
\tag{5.1}
\]

If a word realizes \(T_i\) on every \(I_i\), an interval whose OR has rank
strictly below the middle rank cannot contain any complete \(I_i\).
Therefore every lower target witness lies in \({\cal C}_{\rm full}\).
Distinct lower targets require distinct cells, because a fixed interval has
only one OR.  Hence every universal word in the fixed schedule induces an
injection from lower targets to \({\cal C}_{\rm full}\).

For a dense monotone P/Q schedule the catalogue has a smaller description.
If \(p=s_i\) is a selected start, the lower cells beginning at \(p\) are
exactly the proper prefixes of \(I_i\).  Cells beginning at omitted starts
must be added with their literal boundary-truncated lengths.  This identity
must be proved for the schedule at hand; using a convenient subcatalogue
without that proof gives only a sufficient model.

## 6. Maximal-common-cap equivalence

Allow any finite set of positional caps and let \(\widehat E_p\) denote the
resulting capped envelope.  Assume it is nonempty and still realizes every
middle row.

Let \({\cal L}\) be the nonempty lower targets, and let

\[
 M:{\cal L}\longrightarrow{\cal C}_{\rm full}
\tag{6.1}
\]

be injective.  Define the maximal common cap

\[
 A_p(M)=
 \widehat E_p\cap
 \bigcap_{S\in{\cal L}:\ p\in M(S)}S.
\tag{6.2}
\]

The empty inner intersection is the full coordinate set, so an uncovered
position has \(A_p(M)=\widehat E_p\).

### Theorem 6.1 (maximal-common-cap compiler)

There exists a nonempty physical word \(Q\) subordinate to the capped
envelope that realizes every middle row on \(I_i\) and every lower target
\(S\) on its assigned cell \(M(S)\) if and only if

\[
 A_p(M)\ne\varnothing\qquad(0\le p<L),
\tag{6.3}
\]

\[
 \bigvee_{p\in I_i}A_p(M)=T_i\qquad(0\le i<W),
\tag{6.4}
\]

and

\[
 \bigvee_{p\in M(S)}A_p(M)=S\qquad(S\in{\cal L}).
\tag{6.5}
\]

When these conditions hold, \(Q_p=A_p(M)\) is itself a realizing word.

#### Proof

Suppose \(Q\) is a realizing word.  Middle legality gives
\(Q_p\subseteq\widehat E_p\).  If \(p\in M(S)\), exact realization of \(S\)
gives \(Q_p\subseteq S\).  Hence \(Q_p\subseteq A_p(M)\) pointwise.  The
larger word \(A(M)\) is still contained in every active middle target and
every assigned lower target.  Since it contains the realizing word \(Q\),
it cannot lose a required coordinate.  Thus (6.3)--(6.5) hold.

Conversely, (6.2) prevents every forbidden coordinate.  Conditions
(6.3)--(6.5) assert nonempty letters and supply every required coordinate in
every middle and lower interval.  Therefore \(A(M)\) is a realization.
\(\square\)

This theorem is the reason fractional Hall feasibility is not the final
gate.  Individual target-cell edges may all be legal, and their bipartite
graph may have a perfect matching, while overlapping chosen cells impose
incompatible caps on the same physical letters.

Let \(G\subseteq{\cal L}\times{\cal C}_{\rm full}\) be any sound candidate
graph.  For a subgraph \(H\subseteq G\), define

\[
 A_p(H)=\widehat E_p\cap
        \bigcap_{(S,J)\in H:\ p\in J}S.                  \tag{6.6}
\]

Call \(H\) **Cartesian** when every \(A_p(H)\) is nonempty, every middle
row has exact OR under \(A(H)\), and every edge \((S,J)\in H\) has exact OR
\(S\) on \(J\).

### Theorem 6.2 (strong Cartesian-Hall factorization; exact restatement)

A simultaneous lower compiler whose assignment uses only edges of \(G\)
exists if and only if there is a Cartesian subgraph \(H\subseteq G\)
containing a matching that saturates \({\cal L}\).  Once such an \(H\) is
given, ordinary Hall in \(H\) and the single word \(A(H)\) form a complete
constructive certificate.  This is an unrestricted compiler equivalence
only when \(G\) is occurrence-complete; for a merely sound subgraph it is an
exact equivalence relative to \(G\).

#### Proof

If \(H\) is Cartesian, \(A(H)\) realizes every edge of \(H\) at once and
preserves all middle rows.  Any matching in \(H\) saturating the lower
targets therefore gives distinct physical witnesses in that one word.

Conversely, if \(M\) is a simultaneous compiler matching, take \(H=M\).
Theorem 6.1 says exactly that \(A(H)=A(M)\) is nonempty and realizes all
middle rows and all edges of \(H\), so \(H\) is Cartesian. \(\square\)

A tempting route is to construct a Cartesian edge bank first and prove its
ordinary Hall inequalities.  In the strong definition above this is nearly
tautological: every solution gives
such a bank by taking \(H=M\), and two distinct target labels cannot occupy
the same cell of a Cartesian bank.  Thus strong Cartesianity must not be
used as an inductive existence invariant.

The useful deterministic weakening is a **co-selectable guarded** graph:
guards are protected only against edges which one matching may select
together.  An independently supplied target-unit/cell-substochastic
fractional flow then proves Hall and every resulting matching is common-cap
legal.  The correlated alternative is the atomic lopsided-LLL criterion on
the complete post-closure conflict clutter.  Both dimension-free conditional
lemmas, and their exact hypotheses, are stated in
`MATH_THEOREM_MASTER_STAIRCASE_PINNED_COMMON_CAP_COMPILER_20260731.md`.
Neither follows from marginal Hall, bounded conflict rank, or interval
locality alone.

## 7. Exact integral Boolean formulation

Theorem 6.1 has a direct finite formulation.  Introduce
\(y_{S,J}\) for every retained target-cell pair and impose

\[
 \sum_J y_{S,J}=1\quad(S\in{\cal L}),\qquad
 \sum_S y_{S,J}\le1\quad(J\in{\cal C}_{\rm full}).
\tag{7.1}
\]

For each \(b\in\widehat E_p\), introduce \(q_{p,b}\).  Let

\[
 B_{p,b}=
 \{(S,J):p\in J,\ b\notin S\}.
\tag{7.2}
\]

The exact maximal-cap identity is

\[
 q_{p,b}\ \Longleftrightarrow\
 \bigwedge_{e\in B_{p,b}}\neg y_e.
\tag{7.3}
\]

An empty conjunction in (7.3) is true.  Variables outside the displayed
domain \(b\in\widehat E_p\) are absent, equivalently fixed false.

Add:

1. \(\bigvee_{b\in\widehat E_p}q_{p,b}\) for every physical position;
2. \(\bigvee_{p\in I_i:\ b\in\widehat E_p}q_{p,b}\) for every
   \(b\in T_i\);
3. \(y_{S,J}\Rightarrow
   \bigvee_{p\in J:\ b\in\widehat E_p}q_{p,b}\) for every \(b\in S\).

Because \(q\) is supported inside \(\widehat E\), and a selected
\(y_{S,J}\) forces every \(q_{p,b}\) with \(p\in J,b\notin S\) to zero,
extra coordinates are impossible.  These clauses are therefore sound and
complete for (6.3)--(6.5) relative to the retained candidate graph.  An
unrestricted negative conclusion additionally requires that graph to be
occurrence-complete or every omitted edge to have a proved safe exclusion.
The formulation is integral; no rounding step remains.

Equivalently, one may use matching-only CEGAR.  For a proposed integral
matching compute (6.2).  An empty letter has an inclusion-minimal obstruction
of size at most \(|\widehat E_p|\).  A missing middle bit has a minimal
covering obstruction of size at most \(|I_i|\).  A missing assigned-lower
bit has a minimal covering obstruction of size at most \(|M(S)|\), plus its
guarding incidence.  Adding the corresponding no-goods is exact and
terminates because the matching set is finite.

## 8. Upper transfer and the composite construction

Call the schedule chain-aligned if

\[
 \bigcup_{i=a}^{b}I_i
\]

is a physical interval for every consecutive row block \([a,b]\).

### Lemma 8.1 (upper transfer)

Assume \(Q_p\subseteq T_i\) whenever \(p\in I_i\), and
\(\bigvee_{p\in I_i}Q_p=T_i\).  If the schedule is chain-aligned, then every
consecutive-row identity

\[
 U=\bigvee_{i=a}^{b}T_i
\tag{8.1}
\]

lifts to a physical interval of \(Q\) with OR \(U\).

#### Proof

Let \(J=\bigcup_{i=a}^{b}I_i\), which is an interval.  Every \(Q_p\) with
\(p\in J\) is contained in at least one \(T_i\) from the block, so its OR is
contained in \(U\).  Conversely, the OR on \(J\) contains the exact OR of
each \(I_i\), hence contains every \(T_i\) and therefore \(U\).  \(\square\)

### Theorem 8.2 (reroot--pin--cap construction)

Let \(T\) be a chronology containing every middle target exactly once.
Assume:

1. every upper target is the OR of a consecutive block of \(T\);
2. \(T\) has a chain-aligned schedule of source length \(W+\delta\);
3. the pinned maximal envelope is nonempty and realizes every middle row;
4. the lower-cell catalogue is complete; and
5. either an injective lower assignment satisfies Theorem 6.1, or one of the
   two noncircular selection certificates in the master theorem supplies
   such an assignment.

Then the corresponding maximal common cap \(A(M)\), respectively \(A(H)\),
is a universal contiguous-OR word of length \(W+\delta\).  If an independent
deadline/counting theorem gives \(\nu(k)\ge W+\delta\), then

\[
 \nu(k)=W+\delta.
\tag{8.2}
\]

#### Proof

Hypothesis 5 and Theorem 6.1 or the master selection lemmas give one
nonempty literal word realizing
every lower target on a distinct physical cell and every middle target on its
scheduled row.  By hypotheses 1--2, Lemma 8.1 turns each upper target's
consecutive middle-row witness into one contiguous physical interval with
the same OR.  Thus the word is universal and has the asserted length.  The
last statement follows from the independent lower bound. \(\square\)

Lemmas 2.1, 3.1, and 4.1 are reusable ways to establish hypotheses 1--3;
they are not additional assumptions in Theorem 8.2.

### 8.3. What is new relative to fixed-window `COMP_d(T)`

The maximal-intersection lemma itself is older.  The nonredundant content of
Theorem 8.2 and Corollary 4.3 is the composition of upper transfer,
positional pin contraction, complete lower-cell handling, and exact
common-cap feasibility over a **variable staircase schedule**: the owner
intervals \(I_i=[s_i,d_i]\) may have different lengths and may omit
different starts and deadlines.  No identity \(D^dA=T\), residence
assumption, or flat middle derivative is required.  The earlier
fixed-chronology `COMP_d(T)` theorem is recovered by taking
\(I_i=[i,i+d]\).  In the tail-start coordinates of Section 11 this is the
threshold vector \((0,\ldots,0)\).  The K16 word is genuinely outside that
flat special case: its middle witnesses occur at several lengths.

Accordingly, the reusable search reduction is only

\[
 \text{upper-safe owner rethread}
 \;\longrightarrow\;
 \text{schedule-indexed singleton frontier}
 \;\longrightarrow\;
 \text{pin contraction}
 \;\longrightarrow\;
 \text{residual exact common cap}.
\tag{8.3}
\]

Ordinary marginal Hall is a necessary filter inside the last arrow, not a
replacement for it.

## 9. The K16 instantiation

For K16:

- \(W={16\choose8}=12870\) and \(d=3\);
- the genuine K15 parent has SHA
  \(51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4\);
- its natural K16 chronology has SHA
  \(0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c\);
- reversing prefix \([0,6388]\) and suffix \([12826,12869]\) gives the
  all-upper chronology SHA
  \(c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906\);
- the schedule holes are
  \(X=(12870,12871,12872)\) and \(Y=(0,1,6388)\);
- position \(6389\) is capped to \(0x8000\) and reserved for that singleton;
- the complete physical lower catalogue has \(32230\) cells;
- after reserving the singleton, the residual graph has \(26331\) targets,
  \(32229\) cells, and \(347677\) incidences;
- the exact common-cap model has \(1055230\) variables and \(4513893\)
  clauses.

The decoded word is

    scratch/k16_optimal_12873_20260731.word

with SHA

    890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe.

Independent direct replay covers all \(65535\) nonempty masks.  The general
deadline lower bound gives \(12873\), so Theorem 8.2 yields

\[
 \nu(16)=12873=B(16).
\tag{9.1}
\]

## 10. Exact general gate

The reusable theorem removes three false bottlenecks:

- a fixed coordinate frame is unnecessary;
- an independently chosen lower matching is insufficient; and
- a separate search over source letters is unnecessary once a matching is
  fixed, because the maximal common cap is canonical.

For one odd-to-even step, define the
**reroot--retime--guarded-selection property** at \(k=2r\) to mean that one
can supply:

1. two derivative shore lists satisfying Lemma 2.1 after an explicitly
   absorbed exceptional set;
2. oriented block boundaries for which Lemma 3.1's cross-seam catalogue
   completes the upper ideal without erasing the last protected witness;
3. a chain-aligned schedule with the required positional pins, the literal
   boundary catalogue, and prescribed surplus \(\delta\); and
4. after fixed-pin contraction, either
   - a co-selectable guard bank with a target-unit/cell-substochastic
     fractional flow, or
   - the complete relative atomic conflict family with lopsided-LLL pressure
     witnesses.

### Corollary 10.1 (one-step conditional gate)

If the reroot--retime--guarded-selection property holds at \(k\) with

\[
 \delta=B(k)-\binom{k}{\lfloor k/2\rfloor},
\]

then \(\nu(k)=B(k)\).

#### Proof

The first three clauses give the carrier and pinned staircase.  Clause 4
implies the integral common-cap assignment by Theorem 6.3 or 6.4 of the
master note.  Theorem 8.2 there gives the word, and the deadline theorem
gives the matching lower bound \(B(k)\). \(\square\)

This is a dimension-free conditional implication, not an induction theorem.
For iteration, one must regenerate a synchronized decorated joint action
fibre carrying the next carrier witnesses, staircase and pins, and one fresh
clause-4 certificate.  Separate safe-cut, owner, or sector choices need not
have a common action.  No implication from marginal Hall alone is valid.

Nothing in the K16 certificate proves that the number of exceptional shore
entries, reroot boundaries, or common-cap conflicts stays bounded with \(k\).
Those are the precise uniform induction hypotheses still missing.

## 11. Variable-staircase tail-start family and dimension recursion

The K16 schedule is one member of the following staircase family, which is
exact at the schedule and counting level for every \(k\).  It is not, by
itself, an all-\(k\) carrier or compiler construction.  Put

\[
 r_k=\lceil k/2\rceil,
 \quad M_k={k\choose r_k},
 \quad \Lambda_k=\sum_{s=1}^{r_k-1}{k\choose s},
\]

and let \(d_k\) be the least \(d\ge0\) for which

\[
 dM_k+{d+1\choose2}\ge\Lambda_k.
\tag{11.1}
\]

The unused scalar capacity is

\[
 \sigma_k=d_kM_k+{d_k+1\choose2}-\Lambda_k.
\tag{11.2}
\]

Minimality of \(d_k\) also gives the sharp range

\[
 0\le\sigma_k<M_k+d_k.
\]

### 11.1. Threshold coordinates

Fix \(M,d\), and choose a nondecreasing threshold vector

\[
 0\le a_1\le\cdots\le a_d\le M.
\tag{11.3}
\]

Use source positions \(0,\ldots,M+d-1\).  Put every omitted start at the
tail, so middle row \(i\) starts at \(s_i=i\).  Omit the deadlines

\[
 y_j=a_j+j-1,\qquad 1\le j\le d.
\tag{11.4}
\]

These are strictly increasing.  If

\[
 \delta_i=|\{j:a_j\le i\}|,
\tag{11.5}
\]

then the \(i\)-th retained deadline is \(q_i=i+\delta_i\), and its owner
interval is

\[
 I_i=[i,i+\delta_i].
\tag{11.6}
\]

Thus the depths form a nondecreasing step word.  Deadlines are strictly
increasing, every depth is at most \(d\), and
\(s_{i+1}\le q_i+1\); consequently the schedule is monotone and
chain-aligned for every threshold vector.

Conversely, this parametrizes exactly the schedules whose selected starts
are \(0,\ldots,M-1\) and whose omitted starts are the tail
\(M,\ldots,M+d-1\).  Indeed, if \(y_1<\cdots<y_d\) are their omitted
deadlines, then

\[
 a_j=y_j-j+1
\]

lies in \([0,M]\), is nondecreasing, and recovers (11.4).  Thus “tail-start”
is a genuine scope restriction, not a claim that every monotone P/Q schedule
can be put in this form without loss.

### Lemma 11.1 (exact lower-cell enumeration)

For the schedule (11.6), the complete catalogue of physical intervals which
contain no whole middle-owner interval is exactly

\[
 \{[i,i+\ell-1]:0\le i<M,\ 1\le\ell\le\delta_i\}
\tag{11.7}
\]

together with the tail family

\[
 \{[t,u]:M\le t\le u\le M+d-1\}.
\]

Hence its size is

\[
 \begin{aligned}
 |{\cal C}_{\rm full}|
   &=\sum_{i=0}^{M-1}\delta_i+{d+1\choose2}\\
   &=dM-\sum_{j=1}^{d}a_j+{d+1\choose2}.
 \end{aligned}
\tag{11.8}
\]

#### Proof

An interval beginning at \(i<M\) contains the owner \(I_i\) exactly when
its right endpoint is at least \(q_i\).  If it ends before \(q_i\), it
cannot contain a later owner because the deadlines are strictly increasing;
it cannot contain an earlier owner because its left endpoint is too late.
This gives precisely the proper prefixes in (11.7).  No owner begins at or
after \(M\), so every interval beginning at a tail start is allowed.  Finally,
each threshold \(a_j\) contributes one unit to \(\delta_i\) for exactly
\(M-a_j\) rows, proving (11.8).  \(\square\)

For the rank-count lower target family, this tail-start schedule has enough
distinct physical cells if and only if

\[
 \sum_{j=1}^{d_k}a_j\le\sigma_k.
\tag{11.9}
\]

This is only the exact scalar gate.  Hall and the common-cap equations remain
necessary after (11.9).

### 11.2. The one-pivot singleton frontier

For \(d\ge1\), a particularly small recursive family is

\[
 (a_1,\ldots,a_d)=(0,\ldots,0,p-d).
\tag{11.10}
\]

Its deadline holes are \(0,1,\ldots,d-2,p-1\).  Rows before \(p-d\) have
depth \(d-1\), later rows have depth \(d\), and position \(p\) lies
immediately after the last omitted deadline.  It is a scalar-admissible
singleton-retiming candidate precisely when

\[
 0\le p-d\le\min\{M-1,\sigma_k\}.
\tag{11.11}
\]

Lemma 4.1 must still decide whether the desired singleton is actually legal
at \(p\).  For K16, \(d=3\), \(p=6389\), and the threshold vector is
\((0,0,6386)\); equation (11.8) gives \(32230\) cells exactly.

### 11.3. Exact recursion for \(d_k\) and the threshold budget

The pair \((d_k,\sigma_k)\) can be advanced without resumming the binomial
tail.  Write \(M=M_k,d=d_k,\sigma=\sigma_k\).

If \(k=2m+1\) is odd, then

\[
 M_{k+1}=2M,
 \qquad \Lambda_{k+1}=2\Lambda_k-M+1.
\tag{11.12}
\]

Put

\[
 R_-=2\sigma-M-1-\frac{d(d+3)}2.
\tag{11.13}
\]

Then

\[
 (d_{k+1},\sigma_{k+1})=
 \begin{cases}
 (d-1,R_-),&R_-\ge0,\\
 \left(d,2\sigma+M-1-{d+1\choose2}\right),&R_-<0.
 \end{cases}
\tag{11.14}
\]

Thus an odd-to-even step either retains the threshold count or deletes
exactly one threshold.

If \(k=2m\) is even, let

\[
 C_m=\frac{M}{m+1},
\]

the \(m\)-th Catalan number.  Pascal's identity gives

\[
 M_{k+1}=M+mC_m,
 \qquad \Lambda_{k+1}=2\Lambda_k+M+1.
\tag{11.15}
\]

Put

\[
 R_0=2\sigma-dC_m-M-1-{d+1\choose2}.
\tag{11.16}
\]

Then

\[
 (d_{k+1},\sigma_{k+1})=
 \begin{cases}
 (d,R_0),&R_0\ge0,\\
 \left(d+1,
  2\sigma+C_m(m-d)-1+\dfrac{(d+1)(2-d)}2\right),&R_0<0.
 \end{cases}
\tag{11.17}
\]

Thus an even-to-odd step either retains the threshold count or adds exactly
one threshold.

#### Proof

Equations (11.12) and (11.15) are Pascal's identity, with symmetry about the
middle rank.  Substitute them into (11.1)--(11.2).  At an odd-to-even step,
testing depth \(d-1\) gives exactly \(R_-\); depth \(d\) is always feasible,
while depth \(d-2\) is excluded by minimality at the parent.  Here
\(d\le m\) and
\({2m+1\choose m}\ge {d+1\choose2}+1\), so the displayed depth-\(d\)
slack in (11.14) is nonnegative.  At an
even-to-odd step, testing depth \(d\) gives exactly \(R_0\); depth \(d-1\)
is excluded by parent minimality and depth \(d+1\) is feasible.  The latter
uses \(d\le m-1\), which follows from
\(\Lambda_k\le(m-1)M_k\), together with

\[
 C_m\ge\frac{(m-1)(m-2)}2
       \ge 1+\frac{(d+1)(d-2)}2
\]

at the worst admissible \(d=m-1\) (with \(m=1,2\) checked directly).
The displayed
slacks are the corresponding substitutions in (11.2).  \(\square\)

For example, the K15 data \((M,d,\sigma)=(6435,3,2928)\) take the second
branch of (11.14), giving \((d_{16},\sigma_{16})=(3,12284)\).  The K16 data
take the first branch of (11.17), giving
\((d_{17},\sigma_{17})=(3,7401)\).

### 11.4. Recursive schedule template

At a \(k\to k+1\) owner lift, authenticated parent block boundaries and new
Pascal-shore/reroot seams are candidate threshold positions in the child row
index.  Equations (11.14) and (11.17) change the required number of
thresholds by at most one, but do not prove that suitable geometric seams
exist.  If the authenticated candidates contain a nondecreasing child
multiset

\[
 0\le a'_1\le\cdots\le a'_{d_{k+1}}\le M_{k+1},
 \qquad \sum_j a'_j\le\sigma_{k+1},
\tag{11.18}
\]

then transporting, deleting, or adding one threshold gives, by
(11.4)--(11.6), a valid chain-aligned child schedule with a complete,
explicitly enumerated lower-cell catalogue.  The recurrence proves only the
required coordinate count and the scalar budget in (11.18); it proves
neither seam availability nor preservation of upper safety, pin legality,
Hall, or common-cap feasibility.

When \(d_k,d_{k+1}\ge1\), a one-pivot parent
\(p_k=d_k+a_k\) has the scalar-feasible proportional heuristic

\[
 a_{k+1}=\min\left\{\sigma_{k+1},M_{k+1}-1,
 \left\lfloor\frac{M_{k+1}}{M_k}a_k\right\rfloor\right\},
 \qquad p_{k+1}=d_{k+1}+a_{k+1},
\tag{11.19}
\]

or it may be replaced by a nearer actual child block seam satisfying the same
budget.  Formula (11.19) is not a geometric transport theorem.  Every
transported threshold must still pass the endpoint upper audit, Lemma 4.1
for its pin, residual Hall, and Theorem 6.1.

What is uniform inside this tail-start family is that the schedule search
has only \(d_k=\Theta(\sqrt{k})\) threshold coordinates, an exact linear
budget (11.9), and changes dimension by at most one at each step.  The
asymptotic follows from the standard central-binomial estimates
\(2^k/M_k=\Theta(\sqrt{k})\) and
\(\Lambda_k=\Theta(2^k)\); the quadratic term in (11.1) is negligible
relative to \(dM_k\).  This is a schedule template, not an induction theorem.

### 11.5. Dimension-uniform P/Q schedule identity

The threshold family has a useful extension to arbitrary omitted starts and
deadlines.  Let \(L=M+d\), let \(X,Y\subseteq[0,L-1]\) have size \(d\), and
write

\[
 [0,L-1]\setminus X=\{s_0<\cdots<s_{M-1}\},\qquad
 [0,L-1]\setminus Y=\{q_0<\cdots<q_{M-1}\}.
\]

Assume \(s_i\le q_i\), and put \(I_i=[s_i,q_i]\).  For a position \(t\),
let \(\rho(t)\) be the least \(i\) with \(s_i\ge t\), when one exists, and
define

\[
 c(t)=
 \begin{cases}
 q_{\rho(t)},&\rho(t)\text{ exists},\\
 L,&\rho(t)\text{ does not exist}.
 \end{cases}
\tag{11.20}
\]

### Lemma 11.2 (arbitrary-omission lower-cell atlas)

The complete lower-cell catalogue is

\[
 {\cal C}_{\rm full}
 =\{[t,u]:0\le t\le u<c(t)\}.
\tag{11.21}
\]

If

\[
 {\cal A}=\sum_{i=0}^{M-1}(q_i-s_i)
          =\sum_{x\in X}x-\sum_{y\in Y}y,
 \qquad
 {\cal B}=\sum_{x\in X}(c(x)-x),
\]

then

\[
|{\cal C}_{\rm full}|={\cal A}+{\cal B}.
\tag{11.22}
\]

Here \({\cal A}\) is exactly the selected-start proper-prefix area and
\({\cal B}\) is exactly the omitted-start boundary contribution.

There is an equivalent loss form which exposes the all-\(k\) invariant.  If
\(Y=\{y_1<\cdots<y_d\}\), set

\[
 \ell(X,Y)=
 \sum_{x\in X}(L-c(x))
 +\sum_{j=1}^{d}\bigl(y_j-(j-1)\bigr).
\tag{11.22a}
\]

Every summand is nonnegative, and

\[
 |{\cal C}_{\rm full}|
 =\sum_{x\in X}c(x)-\sum_{y\in Y}y
 =dM+{d+1\choose2}-\ell(X,Y).
\tag{11.22b}
\]

Thus \(dM+\binom{d+1}{2}\) is the exact maximum physical lower-cell
supply over all legal P/Q omission patterns, not merely a convenient upper
bound.  Also \(d\le{\cal B}\le\binom{d+1}{2}\) when \(d>0\); an omitted
start contributes only up to its next-owner deadline, never an automatic
triangular credit.

#### Proof

For a fixed left endpoint \(t\), the first owner interval that could be
contained in \([t,u]\) is \(I_{\rho(t)}\), because both starts and deadlines
increase.  Thus \([t,u]\) contains no owner exactly when \(u<c(t)\), proving
(11.21).  A selected start \(s_i\) contributes \(q_i-s_i\) such cells; an
omitted start \(x\) contributes \(c(x)-x\).  Summing gives (11.22), and the
complement identity for \({\cal A}\) is Lemma 4.2.  Cancelling the
\(\sum_{x\in X}x\) terms gives
\(|{\cal C}_{\rm full}|=\sum_xc(x)-\sum_yy\).  Now write

\[
 \sum_xc(x)=dL-\sum_x(L-c(x)),\qquad
 \sum_jy_j={d\choose2}+\sum_j(y_j-(j-1)),
\]

and use \(dL-\binom d2=dM+\binom{d+1}2\) to obtain (11.22b).
Finally, if \(X=\{x_1<\cdots<x_d\}\), the zero-based index of the first
selected start after \(x_j\) is \(n_j=x_j-j+1\), with \(n_j=M\) denoting
the right boundary.  Every selected deadline satisfies \(q_i\le i+d\), so
\(c(x_j)\le n_j+d=x_j+d-j+1\); legality gives \(c(x_j)>x_j\).
Hence \(1\le c(x_j)-x_j\le d-j+1\), which gives the stated bounds on
\({\cal B}\).  \(\square\)

For tail starts, \({\cal B}=\binom{d+1}{2}\), so Lemma 11.2 specializes to
Lemma 11.1.  For arbitrary omissions, chain alignment is the additional
literal condition

\[
 s_{i+1}\le q_i+1\qquad(0\le i<M-1).
\]

It is not implied merely by legality \(s_i\le q_i\).

Pins fit this accounting without an artificial scalar charge.  Let
\({\cal L}_k\) be the \(\Lambda_k\) lower targets, and let \(\Pi\) be an
injective partial target-to-cell map, written as prescribed pairs \((S,J)\)
with \(J\in{\cal C}_{\rm full}\).  Thus no target or cell identity repeats,
although different pinned cells may overlap in physical positions.  From the
middle envelope \(E_p\), form the pinned envelope

\[
 E_p^{\Pi}=E_p\cap
 \bigcap_{(S,J)\in\Pi:\ p\in J}S.
\tag{11.23}
\]

An empty second intersection means the full coordinate set.  Delete the
pinned targets and their distinct cells from the residual assignment
problem, retain every pinned equality as a guard, and rebuild all residual
target--cell domains from \(E^{\Pi}\), not from the uncapped envelope.

### Theorem 11.3 (pinned P/Q compiler invariant)

Fix the chronology, legal P/Q schedule, and pin family above.  A residual
injective assignment \(R\) of every unpinned lower target to an unpinned cell
extends the pins to a literal compiler if and only if its maximal cap

\[
 A_p(R,\Pi)=E_p^{\Pi}\cap
 \bigcap_{(S,J)\in R:\ p\in J}S
\tag{11.24}
\]

is nonempty at every position and reproduces, by interval OR, every middle
row and every lower equality in \(\Pi\cup R\).  In particular a multi-cell
pin remains a guarded equality after contraction.  For a one-cell singleton
pin, that guard follows from nonemptiness because the pinned letter is a
nonempty subset of a singleton.

If \(h=|\Pi|\), pin contraction preserves the exact scalar surplus:

\[
 \begin{aligned}
 \Omega_k(X,Y)
   &:=|{\cal C}_{\rm full}|-\Lambda_k
     ={\cal A}+{\cal B}-\Lambda_k,\\
(|{\cal C}_{\rm full}|-h)-(\Lambda_k-h)&=\Omega_k(X,Y).
\end{aligned}
\tag{11.25}
\]

Equation (11.25) is raw catalogue accounting.  Capping can delete residual
target--cell incidences even though it does not delete the underlying
physical cells; any policy that discards additional cells must charge those
cells separately.  Schedule retiming is therefore completed before this
contraction.  In particular \(\Omega_k(X,Y)\ge0\) is necessary but not
sufficient for a compiler.

If in addition the schedule is chain-aligned and each upper target is the OR
of a consecutive chronology block, the same maximal cap realizes every upper
target by Lemma 8.1.  These statements are exact for every \(k\), relative to
the fixed chronology, schedule, and pins.

#### Proof

Every realizing word is contained positionwise in (11.24), because each of
its letters is contained in every middle or assigned-lower target whose cell
passes through that position.  Conversely, (11.24) is the largest word
respecting all such containments.  Nonemptiness and the displayed OR
equalities are therefore necessary and sufficient, exactly as in Theorem
6.1.  Removing \(h\) distinct pinned targets and their \(h\) distinct cells
proves (11.25).  Upper transfer is Lemma 8.1.  \(\square\)

At the minimal depth \(d_k\), (11.22b) and (11.25) give the exact general
schedule invariant

\[
 \Omega_k=\sigma_k-\ell(X,Y).
\tag{11.26}
\]

For a tail-start threshold vector, \(c(x)=L\) at every omitted start and
\(y_j=a_j+j-1\), so \(\ell(X,Y)=\sum_j a_j\).  Hence (11.26) specializes to
\(\Omega_k=\sigma_k-\sum_j a_j\).

Equations (11.14) and (11.17) update the arithmetic part
\((M_k,\Lambda_k,d_k,\sigma_k)\) exactly.  A child threshold vector updates
the schedule loss in (11.26), and pin contraction leaves \(\Omega_k\)
unchanged.  This is the promised all-\(k\) invariant: it is an exact
accounting and decision-obligation schema for arbitrary legal omissions, and
Theorem 11.3 is the corresponding schedule specialization of Theorem 6.1.
It is not a closure theorem under \(k\to k+1\): the numerical recurrence
transports none of \(X,Y,\Pi\), the chronology, or the literal envelope.  It
does **not** assert that a compatible child chronology, legal cap, upper
transfer, or common-cap assignment exists.

### 11.6. K16 test and carrier-free K17 forecast

For K16, the omitted sets are

\[
 X_{16}=\{12870,12871,12872\},\qquad
 Y_{16}=\{0,1,6388\}.
\]

Thus \({\cal A}_{16}=32224\), \({\cal B}_{16}=6\), and

\[
 |{\cal C}_{16}|=32230,\qquad
 \Omega_{16}=32230-26332=5898.
\tag{11.27}
\]

Contracting the authenticated singleton pin at position \(6389\) leaves
\(32229\) cells and \(26331\) lower targets, still with surplus \(5898\).
This agrees with the exact K16 compiler instance.

The arithmetic recurrence gives

\[
 (M_{17},\Lambda_{17},d_{17},\sigma_{17})
 =(24310,65535,3,7401).
\tag{11.28}
\]

Proportional transport of the K16 one-pivot threshold first gives
\(\lfloor24310\cdot6386/12870\rfloor=12062\), which (11.19) clips to
\(a_{17}=7401\).  The resulting **schedule candidate**, with no carrier
assumed, is

\[
 (a_1,a_2,a_3)=(0,0,7401),\quad
 X_{17}=\{24310,24311,24312\},\quad
 Y_{17}=\{0,1,7403\}.
\]

Its candidate pivot is \(p_{17}=7404\), its proper-prefix area is \(65529\),
and its tail contribution is \(6\).  Therefore

\[
 |{\cal C}_{17}|=65535=\Lambda_{17},\qquad \Omega_{17}=0.
\tag{11.29}
\]

If a one-cell singleton is legally pinned there, contraction would leave
\(65534\) residual cells for \(65534\) residual targets and still zero
surplus.  Thus the forecast is maximally tight: every residual cell would be
used.  Nothing here supplies the K17 chronology, proves the cap legal, or
establishes upper completeness, Hall, or common-cap feasibility.

## 12. Certificate references

- MATH_THEOREM_MASTER_STAIRCASE_PINNED_COMMON_CAP_COMPILER_20260731.md.
- MATH_AUDIT_ODD_EVEN_REROOT_PINNED_COMMON_CAP_COMPILER_20260731.md.
- MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md.
- MATH_THEOREM_AD_K16_TRUE_FOURFILTER_COMMON_CAP_MATCHING_GATE_20260731.md.
- MATH_THEOREM_R_K16_TRUE_FOURFILTER_ENDPOINT_REROOT_HALL_PASS_20260731.md.
- scratch/audit_variable_staircase_recursion_20260731.py, SHA256
  \(06bf66b7ab38ea670aae7714532aa7fb52852c66c986af6cb5141a7039082f3c\).
- scratch/variable_staircase_recursion_20260731.audit.json, SHA256
  \(c6bc1179c554350891bfd55ac289df1b6f593f943fefdae4d75ff88ab4786a58\),
  payload
  \(bb5ba9ef301955fbc482f346f7c7e2c128572f83c6f9f30b97d8743845cd48d0\).
- scratch/k16_c7be_commonq_chain_independent_20260731.audit.json, payload
  \(80a94b84551c6c04a6c9a44d29e9615553ef721bb1409e700f65a933a9c030d2\).
- scratch/k16_trueff_commoncap_direct_cnf_20260731/independent_direct.audit.json,
  payload
  \(f68f801d8091246808e0d84b62d096de896eae3f468c15f179435157fad1d62a\).

The literal word, rather than its SAT lineage, is the final positive
certificate.
