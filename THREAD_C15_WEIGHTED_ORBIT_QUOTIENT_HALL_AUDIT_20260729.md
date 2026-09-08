# C15 weighted-orbit census and quotient-Hall audit

Date: 2026-07-29

Status: exact hand audit.  No computational search is used.  The orbit
profiles and weighted Hall criterion in
`MATH_THEOREM_EQUIVARIANT_GRADED_COMPILER_QUOTIENT_HALL_20260729.md` are
correct, subject to the exact cyclic-boundary and free-right-action
hypotheses stated below.

## 1. Exact orbit census

For later reuse, the general composite formula is as follows.  If `C_k`
acts regularly on `Z_k`, `H_a` is the subgroup of order `a|k`, and the
subset rank is `s`, then

\[
 F_a^{(k)}(s)=
 \begin{cases}
 {k/a\choose s/a},&a\mid s,\\
 0,&a\nmid s,
 \end{cases}
 \qquad
 E_a^{(k)}(s)=
 \sum_{a\mid b\mid k}\mu(b/a)F_b^{(k)}(s).             \tag{1.0}
\]

Here `F_a` counts sets fixed by `H_a`, while `E_a` counts sets whose
stabilizer is exactly `H_a`.  Such sets have orbit size `k/a`, so their
number of physical orbits is `E_a/(k/a)`.  Formula (1.0), together with the
actual orbit size as its quotient demand, is the complete stabilizer input
for every composite cyclic weighted-Hall instance.

Let `G=C_15=<rho>` act on subsets of `Z_15` by translation.  For each
divisor `d` of 15, let `H_d` be the unique subgroup of order `d`.  Every
`H_d`-orbit on coordinates has size `d`, so the number of rank-`s` subsets
fixed by `H_d` is

\[
 F_d(s)=
 \begin{cases}
 {15/d\choose s/d},&d\mid s,\\
 0,&d\nmid s.
 \end{cases}                                             \tag{1.1}
\]

Let `E_d(s)` denote the number of rank-`s` subsets whose stabilizer is
exactly `H_d`.  Since the subgroup lattice of `C_15` is the divisor lattice,

\[
 F_d(s)=\sum_{d\mid e\mid15}E_e(s),\qquad
 E_d(s)=\sum_{d\mid e\mid15}\mu(e/d)F_e(s).             \tag{1.2}
\]

A set counted by `E_d(s)` has orbit size `15/d`, hence contributes
`E_d(s)/(15/d)` physical orbits.  For ranks one through five, (1.1)--(1.2)
give

\[
\begin{array}{c|rrrr|rrrr|c}
s&F_1&F_3&F_5&F_{15}&E_1&E_3&E_5&E_{15}
 &\text{orbit profile}\\ \hline
1&15&0&0&0&15&0&0&0&15^1\\
2&105&0&0&0&105&0&0&0&15^7\\
3&455&5&0&0&450&5&0&0&15^{30},5^1\\
4&1365&0&0&0&1365&0&0&0&15^{91}\\
5&3003&0&3&0&3000&0&3&0&15^{200},3^1.
\end{array}                                               \tag{1.3}
\]

The exceptional rank-three orbit consists of the five translates of

\[
 \{0,5,10\};                                             \tag{1.4}
\]

each such set has stabilizer `<rho^5>` of order three.  The exceptional
rank-five orbit consists of the three translates of

\[
 \{0,3,6,9,12\};                                        \tag{1.5}
\]

each such set has stabilizer `<rho^3>` of order five.  There are no other
short orbits in these ranks.  Complementation is equivariant and preserves
stabilizers, so ranks 14,13,12,11,10 respectively have the same profiles as
ranks 1,2,3,4,5.  Ranks zero and fifteen each consist of one fixed orbit;
neither belongs to the nonempty rank-at-most-five compiler target family.

It follows at once that the target quotient has

\[
 1+7+31+91+201=331                                      \tag{1.6}
\]

vertices and total physical weight

\[
 15(1+7+30+91+200)+5+3=4943.                            \tag{1.7}
\]

Thus (4.3)--(4.5) of the audited note are exact.

## 2. Exact weighted quotient Hall theorem

The following is the precise form that handles short orbits.

### Theorem 2.1

Let a finite cyclic group `G` of order `k` act by automorphisms on a finite
bipartite graph `(L,R;E)`.  Assume that the action on `R` is free.  Give a
left orbit `O` demand `w(O)=|O|`, give every right orbit capacity `k`, and
join quotient vertices `O,J` when at least one physical edge joins them.
Then the physical graph has a matching saturating `L` if and only if

\[
 \sum_{O\in X}|O|\le k|N_{\rm quot}(X)|                 \tag{2.1}
\]

for every collection `X` of left orbits.

#### Proof

For `A subseteq L`, put `delta(A)=|A|-|N(A)|`.  Since
`N(A union B)=N(A) union N(B)` and
`N(A intersection B) subseteq N(A) intersection N(B)`, one has

\[
 \delta(A\cup B)+\delta(A\cap B)
 \geq \delta(A)+\delta(B).                              \tag{2.2}
\]

If physical Hall fails, the maximum deficiency `M` is positive.  Every
translate of a maximizer is a maximizer.  Applying (2.2) to two maximizers,
and using maximality of `M`, shows that their union and intersection are
again maximizers.  The union of all translates of one maximizer is therefore
a `G`-invariant deficient shore.  It is a union of complete left orbits.

The neighborhood of an invariant shore is invariant.  Since the action on
`R` is free, every right orbit has size `k`; transitivity on each orbit shows
that an invariant neighborhood contains either none or all of it.  Physical
Hall on invariant shores is consequently exactly (2.1).  The reverse
implication is immediate by expanding a violating quotient shore.  This
proves the equivalence.  QED

No freeness assumption on the left is needed.  More explicitly, if a left
target has stabilizer of order `d` and one edge from that target enters a
right orbit `J`, translating that edge by the stabilizer gives `d` distinct
candidate positions in `J`, because the right action is free.  Translating
by the whole group gives all `k` right positions as neighbors of the whole
left orbit.  The left demand is nevertheless only the orbit size `k/d`.
This is precisely why stabilizer weights, rather than uniform orbit-node
counts, give the physical Hall inequality.

More quantitatively, the number of neighbors which one fixed target has in
`J` is a multiple of `d`, and the total edge count between its target orbit
and `J` is a multiple of `k`.  These edge multiplicities do not enter
(2.1): Hall counts distinct right vertices, so an adjacent right orbit
contributes capacity `k`, not the number of edge orbits.  Also, when `d>1`
there is no equivariant injection from the short orbit `G/H` into the free
orbit `G`: the image of the coset `H` would have to be fixed by `H`.
Therefore allowing the final matching to break symmetry is essential, not
merely convenient.

For `k=15`, write `epsilon_3(X)` for membership of the exceptional
rank-three orbit and `epsilon_5(X)` for membership of the exceptional
rank-five orbit, and let `f(X)` count the full size-15 target orbits in `X`.
Then (2.1) is exactly

\[
 15f(X)+5\epsilon_3(X)+3\epsilon_5(X)
 \le 15|N_{\rm quot}(X)|,                              \tag{2.3}
\]

or, after normalization,

\[
 f(X)+\frac13\epsilon_3(X)+\frac15\epsilon_5(X)
 \le |N_{\rm quot}(X)|.                                \tag{2.4}
\]

This proves that short orbits create fractional normalized demand, not a
new phase obstruction.

## 3. Hypotheses and implementation cautions

Theorem 3.1 of the audited note is valid as written.  Its application uses
the following essential facts.

1. The spiral symmetry and the one-core symmetry must be exact on the
   cyclic word, including the twisted closing seam.  A quotient path whose
   last-to-first constraint was dropped does not define an automorphism of
   the physical candidate graph, so Theorem 2.1 cannot be applied before a
   genuine seam repair.
2. The right action must be free.  In the strict spiral it is: on
   `Z_W`, translation by `N=W/k` has order exactly `k`.  Without freeness,
   the right side of (2.1) must be replaced by the sum of the actual right
   orbit sizes.
3. The voltage must be a unit modulo `k` for the note's single-coordinate
   construction of an equivariant core and for its use of the full
   coordinate-rotation orbit census.  At `k=15`, this is exactly
   `gcd(15,v)=1`.
4. Every collection of target orbits must be tested.  Positive quotient
   degree of each target orbit is not sufficient.
5. A capacitated quotient-flow implementation must assign left demands
   `15,5,3`, right capacities 15, and effectively unbounded capacities to
   quotient adjacency edges.  Treating quotient edges or quotient vertices
   as unit capacity is not the physical problem; in particular, the two
   short orbits may share one right orbit when the remaining incidences
   permit it.  Quotient adjacency means an edge at **some relative phase**;
   representative-to-representative containment alone is insufficient.
6. A feasible quotient flow certifies all physical Hall inequalities and
   hence the existence of a physical matching.  It does not, without a
   separate phase-lifting argument, itself specify the physical matched
   positions.  To emit the literal compiler word, one should recover a
   phase-resolved physical matching (or prove a dedicated lift).  This is an
   implementation clarification, not a defect in the existential theorem.
7. Cutting is a separate boundary operation.  Appending the depth-sized
   prefix recovers the cyclic lower rows, but upper nonwrapping safety still
   requires the upper-safe cut hypothesis already isolated in the audited
   note.

Therefore there is no missing stabilizer hypothesis in the weighted Hall
theorem itself.  The only potentially misleading reading is to regard an
ordinary unit-capacity matching of the `331 x 429` orbit-node graph as the
physical matching.  The exact quotient object is a node-weighted
capacitated flow/Hall test, followed, when a certificate word is required,
by phase-resolved matching.

## 4. Composite weighted-orbit graded compiler theorem

The two reductions in the audited note combine in the following exact
form.  This is the version which should be used for composite odd `k`.

### Theorem 4.1

Let `k=2m+1`, let `r=m+1`, put `W=binom(k,r)` and `N=W/k`, and let
`1<=d<r`, with `h=r-d>=1`.  Suppose:

1. `T` is a cyclic rank-`r` Johnson Hamilton cycle with a cyclically
   `d`-resident maximal erosion `P`, so that `D^dP=T` and every row `D^jP`
   has constant rank `h+j`;
2. the graded shadow rows `D^jP`, `1<=j<=d`, cover every rank-`h+j`
   target;
3. a cyclic group `G=C_k` acts by
   \[
      g(S,i)=(\rho^vS,i+N),\qquad N=W/k,
      \tag{4.1}
   \]
   with `gcd(k,v)=1`, the envelope obeys
   \(P_{i+N}=\rho^vP_i\) for every cyclic `i`, and the action is exact
   across the twisted cyclic seam;
4. `C` is an equivariant one-core:
   \[
      C_i\subseteq P_i,\qquad DC=DP,qquad
      C_{i+N}=\rho^vC_i \quad(i\bmod W);
      \tag{4.2}
   \]
5. the right vertices are occurrence-labelled source positions (or based
   interval starts), so the `G`-action on them is free.

Let `O` range over rotation orbits of nonempty targets of rank at most `h`,
and let `J` range over right-position orbits.  Join `O` to `J` when some
physical containment edge `C_i subseteq S subseteq P_i` joins them.  Then
the following are equivalent for this fixed core `C`:

* the physical containment graph has a matching saturating all flexible
  targets;
* for every quotient shore `X`,
  \[
     \sum_{O\in X}|O|
     \leq
     \sum_{J\in N_{\rm quot}(X)}|J|;
     \tag{4.3}
  \]
* the node-capacitated quotient network, with left demand `|O|`, right
  capacity `|J|`, and unbounded quotient-edge capacity, has a flow of value
  \(\sum_O|O|\).

When these conditions hold there exists a nonempty physical word `A` with

\[
   C\subseteq A\subseteq P,qquad DA=DP,qquad
   D^jA=D^jP\ (1\leq j\leq d),                         \tag{4.4}
\]

and its rows cover every nonempty target of rank at most `r`.  The word `A`
need not be equivariant.

#### Proof

The action (4.1)--(4.2) makes the physical containment graph invariant.
Theorem 2.1, or its actual-right-orbit-size version, proves equivalence of
physical Hall and (4.3).  The max-flow/min-cut theorem with integral node
capacities proves equivalence with the quotient flow statement.  Physical
Hall gives a phase-resolved physical matching.  Put the matched target `S`
at its matched position and put `P_i` at every unmatched position.  Then

\[
 C\subseteq A\subseteq P,qquad
 DP=DC\subseteq DA\subseteq DP,
\]

so `DA=DP` and hence (4.4).  The matching supplies ranks at most `h`, while
the fixed rows supply ranks `h+1,...,r`.  The hypothesis `h>=1` makes every
unmatched letter `P_i` nonempty.  QED

The quotient flow proves existence of the phase-resolved physical matching;
it is not itself such a matching.  Thus the last constructive step is an
ordinary physical bipartite matching unless a separate phase-lifting
theorem is available.

### Corollary 4.2 (`k=15`)

For `(k,r,d,h,W,N)=(15,8,3,5,6435,429)`, every right orbit has size 15.
If `f(X)` is the number of full target orbits in `X`, and
`epsilon_3,epsilon_5` indicate the exceptional rank-three and rank-five
orbits, respectively, then the exact and complete quotient condition is

\[
  15f(X)+5\epsilon_3(X)+3\epsilon_5(X)
  \leq 15|N_{\rm quot}(X)|                            \tag{4.5}
\]

for all `X` among the 331 target-orbit vertices.  There is no divisibility
condition requiring the left side to be a multiple of 15.  The final
physical matching may and generally will break rotation symmetry.

## 5. Adversarial audit and exact corrections

The principal theorems of the audited note pass, with the following formal
qualifications.

1. **Cyclic residence includes the cut.**  Lemma 1.1 needs the residence
   condition for runs crossing index zero, not merely for runs internal to a
   displayed fundamental block.  Otherwise its wraparound intersection
   ranks need not follow.
2. **The twisted core seam is a hypothesis.**  If only positions
   `0,...,N-1` are stored, (4.2) includes in particular
   \[
     C_{N-1}\cup\rho^vC_0
       =P_{N-1}\cup\rho^vP_0.                          \tag{5.1}
   \]
   Dropping (5.1) destroys the graph automorphism.  The seam-cone lemma
   localizes the resulting defect but does not repair it.
3. **Right vertices are based occurrences.**  Capacity 15 is correct for
   physical positions and for intervals retaining the label
   `(start,length)`, even at full-circumference length, because the start
   still moves freely.  It is not correct after equal set-valued cells are
   coalesced or starts are forgotten.  For a nonfree right action, use the
   actual sum of right-orbit sizes in (4.3).
4. **The word must be nonempty.**  The general form of the graded compiler
   theorem needs `h=r-d>=1`; this is automatic in the intended `k=15`
   specialization, where `h=5`.
5. **Lemma 1.2 needs one explicit hypothesis and one sentence.**  Its phrase
   “cyclic depth-`d` compiler” must include `D^dA=T`; if that convention has
   not already been defined, the equality must be added to the statement.
   The proof excludes rows below `D^(d-1)A` as possible rank-`r-1`
   witnesses.  Rows of length at least `d+1` are excluded because each
   contains a central `d+1` block whose union is the rank-`r` set
   `D^dA=T`, so its union has rank at least `r`.  With the explicit
   hypothesis and that sentence the lemma is correct.
6. **A quotient flow is not a phased matching certificate.**  The weighted
   flow is an exact decision certificate because it implies physical Hall.
   The phrases “a passing matching emits `A` directly” and “weighted max
   flow ... `231/231`” should be read as followed by a physical matching
   recovery step unless the implementation separately records such a lift.
   This distinction is real even with free actions.  For example, let `C_2`
   have free left orbits `A={a_0,a_1}`, `B={b_0,b_1}` and free right orbits
   `C={c_0,c_1}`, `D={d_0,d_1}`, with edges
   \[
      a_i c_i,\qquad a_i d_i,\qquad
      b_i c_i,\qquad b_i d_{1-i}.
   \]
   The integral aggregate flow putting one unit on each of the four
   quotient edges cannot be phase-lifted, although the physical graph has a
   perfect matching.  Thus quotient feasibility certifies that *some*
   physical matching exists, not that every feasible aggregate allocation
   lifts.
7. **The boundary collar is distributed.**  In Lemma 5.2 the `O(kd)` collar
   is a union of `k` seam collars, not necessarily one contiguous physical
   interval.  Lemma 5.1 itself is correct: appending exactly `d` prefix
   letters reproduces the first `W` cyclic starts in every lower row.

These are hypothesis and certificate-scope corrections, not a failure of
the weighted quotient-Hall equivalence.  In particular, no additional
stabilizer transversality, orbit divisibility, or equivariant-matching
hypothesis is required at composite `k=15`.
