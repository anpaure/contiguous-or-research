# Lane C: exact global moving-DM separation for the canonical five-parent catalogue

Date: 2026-07-28

## 0. Audited conclusion

For the canonical five-parent catalogue

```text
P0 = H29       = scratch/k15_doubletrans_05_213_hall29.json
P1 = H30       = scratch/k15_outer2_p1_h30_bridge.json
P2 = H31       = scratch/k15_trans1113_balanced_hall31.json
P3 = tau(1,12) = scratch/k15_transposition_parent_winner.json
P4 = tau(5,7)  = scratch/k15_accumulated_zero_parent_winner.json
```

The transposition pairs in this display are the zero-based bit indices stored
in the two JSON artifacts.

the surviving Hall separator can be made literal on the full mixed-parent
catalogue.  It has three exact layers.

1. A selected Hamilton chronology determines exactly \(19,311\) physical
   lower-compiler cells.  The first and last nine middle vertices determine
   all \(36\) boundary cells; there is no scalar boundary allowance.
2. For every target shore \(A\), one conditional target witness per physical
   cell gives an existential CP-SAT row which is feasible exactly when

   \[
      |N_P(A)|\ge |A|-a.                              \tag{0.1}
   \]
3. A native maximum matching returns a maximizing Dulmage--Mendelsohn shore.
   Adding its literal row excludes the current deficient chronology.  If the
   defect moves, the next exact matching returns the new shore.  Acceptance
   is based only on the newly computed global matching number, never on the
   number of old shores repaired.

Thus allowance \(a=28\) is an exact search for a compiler matching strictly
larger than the current \(16,354\), and allowance \(a=0\) is the exact Hall-zero
search.  Any claimed improvement must carry a matching and an equal-size
vertex cover from the full compiler graph.

There is also a sharp restriction on what the ten pair certificates prove.
They rigorously imply ten augmented-arc escape clauses and hence the

\[
        \binom53+\binom54+\binom55=10+5+1             \tag{0.2}
\]

minimal-parent branch cover.  They do **not** turn pair-local motif tables
or pair-local endpoint maxima into globally exact five-parent shore scores.
The source now rejects such producer/consumer catalogue mismatches.

No H100 search result is asserted in this note.  Section 10 is deliberately
reserved for the exact run certificate.

## 1. Frozen finite objects

Put

\[
 V=\binom{[15]}8,\qquad W=|V|=6435,\qquad
 \mathcal T=\{T\subset[15]:1\le |T|\le7\}.
\]

Then

\[
       |\mathcal T|=\sum_{j=1}^7\binom{15}{j}=16383.   \tag{1.1}
\]

The five frozen parent hashes are, in the order displayed above,

```text
5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c
6ea03a3d48a7dd4462d936218385c5cacc17957bbe3be377ca2e00a360487d91
6d7cee2418f10dbd02076971fdd119d7bc7c35d154430522a70c06f953687ea7
8d0f732c28a552e919857b1a1c80794ac65f390816d2b89b66a67ed63475d2dd
2b25279185b50a9485c65cbc727a08d95b71a1d310332cbdcb23dd6b0b3d2cb7
```

Their full directed normal-arc union has \(23,628\) edges and source-
multiplicity census

\[
 \{1:17012,\ 2:5088,\ 3:1198,\ 4:262,\ 5:68\}.       \tag{1.2}
\]

These are catalogue fingerprints.  Every branch and every pair consequence
below is conditional on these five hashes, ordinary orientations, the
resident chronology constraints, and parent-supported dummy endpoints.

The canonical H29 DM artifact has

\[
 |A_{29}|=1524,\qquad |N_{H29}(A_{29})|=1495,           \tag{1.3}
\]

with depth census \((81,395,1019)\).  Its frozen witness hash is

```text
d329d6302257dcd31ad83192ea8f88e86b46eb364719b1bb040e75e761ebb6d6
```

Equation (1.3) is the baseline which the global channel must reproduce; it
is not itself a variable-catalogue search result.

## 2. The exact \(19,311\)-cell compiler

Let

\[
       P=(Y_0,Y_1,\ldots,Y_{W-1})                     \tag{2.1}
\]

be any selected directed Hamilton path through \(V\).  For
\(0\le p\le W+2\), define the delay-three erosion mask

\[
 Q_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}Y_i.         \tag{2.2}
\]

For \(h\in\{0,1,2\}\) and \(0\le b\le W+2-h\), the physical
cell \(c=(b,h)\) uses

\[
 I_{b,h}=\{b,b+1,\ldots,b+h\},\qquad
 E_{b,h}=\bigcup_{p=b}^{b+h}Q_p.                       \tag{2.3}
\]

For an occurrence of coordinate \(x\) in \(Y_t\), its complete carrier is

\[
 C(t,x)=\{p\in[t,t+3]\cap[0,W+2]:x\in Q_p\}.          \tag{2.4}
\]

The mandatory mask of the cell is

\[
 M_{b,h}=\{x:\text{some nonempty }C(t,x)\subseteq I_{b,h}\}. \tag{2.5}
\]

### Lemma 2.1 (local convexity)

If \(x\in Q_p\cap Q_r\) and \(0\le r-p\le3\), then
\(x\in Q_j\) for every \(p\le j\le r\).

#### Proof

Let

\[
 J_s=[\max(0,s-3),\min(s,W-1)].
\]

The two assumptions say that every \(Y_i\) with
\(i\in J_p\cup J_r\) contains \(x\).  When \(r-p\le3\), the intervals
\(J_p,J_r\) overlap, and \(J_j\subseteq J_p\cup J_r\) for
\(p\le j\le r\).  Hence every member of the intersection defining \(Q_j\)
contains \(x\).  \(\square\)

### Theorem 2.2 (floor- and endpoint-correct mandatory mask)

For every legal cell,

\[
 \boxed{
 M_{b,h}=
 \begin{cases}
 E_{b,h}\setminus Q_{b+h+1},&b+h<3,\\[1mm]
 E_{b,h}\setminus Q_{b-1},&b\ge W,\\[1mm]
 E_{b,h}\setminus(Q_{b-1}\cap Q_{b+h+1}),&\text{otherwise}.
 \end{cases}}                                          \tag{2.6}
\]

#### Proof

Fix \(x\in E_{b,h}\) and choose \(p\in I_{b,h}\) with \(x\in Q_p\).

Assume first that \(b<W\) and \(x\notin Q_{b+h+1}\).  Choose
\(t=\min(p,W-1)\).  Then \(x\in Y_t\), \(p\in C(t,x)\), and
\(t\ge b\).  Hence the carrier has no point left of \(b\).  If it had a
point \(r>b+h\), then \(r-p\le3\), so Lemma 2.1 would force
\(x\in Q_{b+h+1}\), a contradiction.  Thus \(C(t,x)\) is nonempty and is
contained in the cell.

Assume next that \(b+h\ge3\) and \(x\notin Q_{b-1}\).  Choose
\(t=\max(0,p-3)\).  The carrier has no point right of \(b+h\): if
\(p\ge3\), then \(t+3=p\le b+h\), while if \(p<3\), then
\(t+3=3\le b+h\).  If it had a point \(r<b\), then
\(p-r\le3\), and Lemma 2.1 would force \(x\in Q_{b-1}\).  Again the
carrier is nonempty and contained in the cell.

In the ordinary case, suppose both adjacent masks contain \(x\).  Any
carrier meeting \(I_{b,h}\) but avoiding the true left adjacent position
must have \(t\ge b\); avoiding the true right adjacent position must have
\(t+3\le b+h\).  These inequalities imply \(3\le h\), contrary to
\(h\le2\).  Hence \(x\) is mandatory exactly when at least one adjacent
mask omits it.

If \(b+h<3\), there is no left adjacent position.  A carrier avoiding the
true right adjacent position would require \(t+3\le b+h<3\), impossible
because \(t\ge0\).  Therefore only the right mask occurs in (2.6).
If \(b\ge W\), every occurrence has \(t\le W-1<b\); a carrier avoiding a
true left adjacent position is impossible, so only the left mask occurs.
These observations give all three lines of (2.6).  \(\square\)

A lower target \(T\in\mathcal T\) fits cell \((b,h)\) exactly when

\[
 M_{b,h}\subseteq T\subseteq E_{b,h},\qquad
 T\cap Q_p\ne\varnothing\quad(p=b,\ldots,b+h).         \tag{2.7}
\]

At depth \(h\), there are \(W+3-h\) legal starts.  Consequently the exact
right-cell count is

\[
 \sum_{h=0}^2(W+3-h)
   =(W+3)+(W+2)+(W+1)=3W+6=19311.                      \tag{2.8}
\]

For each depth, starts \(0,\ldots,5\) are the six left cells and the last
six starts are the right cells.  Thus there are \(12\) endpoint cells per
depth and \(36\) altogether.  Formula (2.6) for all left cells uses only
\(Q_0,\ldots,Q_8\), hence only \(Y_0,\ldots,Y_8\).  The reversed last nine
vertices give the right side.  Endpoint identity alone is insufficient:
the exact boundary value is conditioned on this eight-edge collar.

## 3. Exact position channel

Adjoin a dummy vertex \(\partial\).  The selected normal arcs together with
one \(\partial\to Y_0\) and one \(Y_{W-1}\to\partial\) arc form one
`AddCircuit`.  Introduce positions

\[
 \pi_v\in\{0,\ldots,W-1\},\qquad
 \eta_i\in V,
\]

and impose

\[
 \operatorname{AddInverse}((\pi_v)_{v\in V},(\eta_i)_{0\le i<W}),
                                                               \tag{3.1}
\]

\[
 x_{uv}=1\Longrightarrow \pi_v=\pi_u+1,               \tag{3.2}
\]

together with the dummy implications fixing the start at position \(0\)
and the end at position \(W-1\).  Since the circuit is a single cycle
through every physical vertex and the only omitted successor equality is the
dummy jump, (3.1)--(3.2) recover precisely the selected linear chronology.

`Element` constraints expose the 15 coordinate bits of
\(Y_i=\eta_i\).  Boolean conjunctions build every \(Q_p\), Boolean
disjunctions build every \(E_{b,h}\), and Theorem 2.2 builds every mandatory
bit.  In particular this is a position predicate on the actual selected
mixed-parent path; it does not consult a local-pattern producer catalogue.

The deterministic evaluator independently constructs each occurrence
carrier (2.4), unions the coordinates whose complete carriers lie in a cell,
and requires this carrier mask to equal (2.6).  On every moving shore, the
formula cell list and complete-carrier cell list are then required to equal
the native auditor's `dm_cell_indices` list, not merely its cardinality.

## 4. One-way cell claims are exactly the Hall row

Fix a nonempty shore \(A\subseteq\mathcal T\) of distinct targets and an
allowance \(a\) with \(0\le a<|A|\).  For every physical cell \(c=(b,h)\),
introduce

* one claim bit \(z_c\);
* one target selector \(T_c\in A\); and
* for every \(p\in I_{b,h}\), one coordinate selector
  \(u_{c,p}\in[15]\).

Conditioned on \(z_c=1\), impose

\[
 M_c\subseteq T_c\subseteq E_c,\qquad
 u_{c,p}\in T_c\cap Q_p\quad(p\in I_c).               \tag{4.1}
\]

Finally impose

\[
                   \sum_c z_c\ge |A|-a.               \tag{4.2}
\]

The implementation represents \(T_c\) by an `Element` lookup into the
literal list \(A\).  It represents each nonempty intersection in (4.1) by
one coordinate index and two `Element` lookups.  Thus there is no hidden
sum over targets and no projected intersection test.

### Theorem 4.1 (one-way Hall equivalence)

For a fixed selected chronology, (4.1)--(4.2) are feasible if and only if

\[
                         |N_P(A)|\ge |A|-a.            \tag{4.3}
\]

#### Proof

If \(z_c=1\), its selected target satisfies (2.7), so \(c\in N_P(A)\).
There is only one claim bit for each physical cell.  Hence (4.2) certifies
at least \(|A|-a\) distinct neighbour cells.

Conversely, if (4.3) holds, choose \(|A|-a\) distinct fitting cells.  In
each choose one fitting target from \(A\), and for each required erosion row
choose one coordinate in its nonempty intersection with that target.  Set
exactly these cell claims to one.  All conditions attached to a false claim
are vacuous.  This satisfies (4.1)--(4.2).  \(\square\)

No reverse implication `fit implies claim` is required.  The row is an
existential certificate that sufficiently many distinct cells fit.  The same
target may be reused in different cells because \(N_P(A)\) counts right
cells, not an internal matching of \(A\) to those cells.

For reference, the shared global channel has \(787,005\) Boolean and
\(19,305\) integer variables.  One shore row has exactly

\[
 \sum_c|I_c|=6438+2(6437)+3(6436)=38620               \tag{4.4}
\]

row-intersection selectors and contributes \(386,216\) Boolean variables,
\(77,242\) integer variables, and \(772,433\) constraints in the current
encoding.  The repeated target arrays still have size
\(19311|A|\); this is why finite batches of literal shores, rather than
hundreds of motif expansions, are the executable representation.

## 5. The exact all-shore separation oracle

For a chronology \(P\), let

\[
 G_P=(\mathcal T,\mathcal C;E_P)                       \tag{5.1}
\]

be its literal compiler graph, where \(|\mathcal C|=19311\).  Put

\[
 \nu(P)=\nu(G_P),\qquad \delta(P)=16383-\nu(P).        \tag{5.2}
\]

Let \(K=K_{\mathcal T}\mathbin{\dot\cup}K_{\mathcal C}\) be a minimum
vertex cover of size \(\nu(P)\), obtained together with a maximum matching,
and define

\[
                    A_P=\mathcal T\setminus K_{\mathcal T}. \tag{5.3}
\]

### Lemma 5.1 (the returned shore has the full deficiency)

\[
 N_P(A_P)=K_{\mathcal C},\qquad
 |A_P|-|N_P(A_P)|=\delta(P).                           \tag{5.4}
\]

#### Proof

Because \(K\) covers every edge, a neighbour of a target outside
\(K_{\mathcal T}\) must lie in \(K_{\mathcal C}\).  Thus
\(N_P(A_P)\subseteq K_{\mathcal C}\), and

\[
 |A_P|-|K_{\mathcal C}|
 =16383-|K_{\mathcal T}|-|K_{\mathcal C}|
 =16383-\nu(P)=\delta(P).                              \tag{5.5}
\]

Hall's deficiency formula says no shore has gap larger than \(\delta(P)\).
The displayed inclusion would give a gap at least \(\delta(P)\), so equality
holds throughout, proving (5.4).  \(\square\)

### Theorem 5.2 (relocation-proof finite separation)

Fix \(a\ge0\).  Repeat:

1. solve the Hamilton, residence, upper-target, support-branch, and all
   accumulated exact shore rows;
2. compute a fresh maximum matching and minimum cover in \(G_P\);
3. if \(\delta(P)\le a\), return the matching/cover certificate;
4. otherwise add (4.2) for \(A=A_P\) and the same allowance \(a\).

Every nonterminal iteration excludes its incumbent.  No chronology with
\(\delta\le a\) is excluded.  If every carrier subproblem is decided exactly,
the procedure terminates after finitely many iterations with such a
chronology or with infeasibility of the finite carrier family.

#### Proof

If \(\delta(P)>a\), Lemma 5.1 gives

\[
 |N_P(A_P)|=|A_P|-\delta(P)<|A_P|-a,                  \tag{5.6}
\]

so the new exact row rejects \(P\).  Conversely, if \(\delta(Q)\le a\),
Hall's deficiency formula gives

\[
 |N_Q(A)|\ge |A|-a
\]

for every shore \(A\); hence no generated row rejects \(Q\).  The selected
successor-factor family is finite, and each nonterminal iteration removes
at least its current member.  \(\square\)

The theorem is the promised non-relocation guarantee.  Conjugating the old
deficient block, or moving it to another target shore, does not satisfy the
acceptance test: the newly computed matching remains deficient and supplies
another violated exact row.

Two settings have different theorem-level meanings.

* \(a=28\) asks for \(\nu(P)\ge16355\), a strict global improvement over H29.
* \(a=0\) asks for \(\nu(P)=16383\), the complete Hall condition.

For either setting, a positive claim must include a literal matching of the
reported size and an equal-size vertex cover.  For Hall zero, the matching
has \(16,383\) edges.  A fixed-shore gain, a projected score, or a repaired
old zero list is not an acceptance certificate.

## 6. Why catalogue equality is mandatory for motif consumers

Let \(E_{\rm prod}\) be the directed edge table on which a fixed motif file
was exhaustively generated, and let \(E_{\rm cons}\) be the directed table
whose arc variables are consumed by the model.  A completeness claim for
the motif file is a claim about words in \(E_{\rm prod}\).  If
\(E_{\rm prod}\subsetneq E_{\rm cons}\), a selected mixed word using an edge
of \(E_{\rm cons}\setminus E_{\rm prod}\) has no serialized positive-state
record, even when it is a genuine compiler hit.  Likewise, a boundary
maximum over producer collars need not upper-bound the larger consumer
collar language.  Containment therefore does not transport exactness or a
proof-safe boundary upper bound to the larger catalogue.

Accordingly, absent a separate extension theorem, the exact-consumer
contract is

\[
                         E_{\rm prod}=E_{\rm cons}.     \tag{6.1}
\]

This is a validation condition, not merely an optimization.  In the current
canonical data, for example, the five adjacent pair tables have respectively

\[
 11965,\ 10413,\ 12527,\ 11944,\ 10471                 \tag{6.2}
\]

producer edges, all strictly below the \(23,628\)-edge full union.  They
omit mixed-parent words and cannot be installed as globally exact rows.

The live consumers now map every producer edge into the consumer and then
assert equality of the two edge sets for fixed projected, fixed multi-shore,
fixed exact, required-target, and adaptive exact rows.  A pair table remains
valid when that pair face itself is supplied as the consumer catalogue.
Merely retaining all five sources and fixing off-face arc literals to zero
does not change the consumer edge table and therefore does not pass this
equality check.  The global position row of Sections 2--4 needs no motif
equality assertion because it constructs every cell directly from the actual
selected chronology.

This resolves the former ambiguity around
`exactdm_5cycle_boundaryupper`: its UNSAT statements concern the restricted
pair-face architecture encoded there.  They are not a global five-parent
UNSAT theorem and are not used as five fixed global shore predicates below.

## 7. The ten pair escapes and the \(10+5+1\) branch cover

For every selected **augmented** successor arc \(e\), including the two
dummy-cut arcs, let

\[
 \operatorname{src}(e)=\{i:e\text{ is supplied by }P_i\}. \tag{7.1}
\]

The certified pair artifacts prove that no Hall-perfect resident chronology
is supported wholly inside \(P_i\cup P_j\), for every pair
\(\{i,j\}\subset[5]\).  Their endpoint-conditioned boundary value is an
upper relaxation on that same pair catalogue, so infeasibility of the
relaxation excludes the literal pair model.  The frozen ten-run provenance,
including every summary and log hash, is
`scratch/k15_exact_pair_nogos_20260728/MANIFEST.json`; retracted `allow6`
artifacts are explicitly excluded from that bundle.

The only consequence imported into the full union is therefore

\[
 \boxed{
 \bigvee_{e:\operatorname{src}(e)\cap\{i,j\}=\varnothing}x_e,
 \qquad 0\le i<j<5.}                                  \tag{7.2}
\]

The support in (7.2) must include dummy arcs.  Otherwise a chronology could
appear to leave a pair merely by cutting the same normal path at an endpoint
available only to a third parent.

### Theorem 7.1 (lossless canonical branch hierarchy)

Every Hall-perfect chronology in the canonical five-parent union lies in at
least one of the sixteen branches indexed by a set \(S\subseteq[5]\) with
\(|S|\in\{3,4,5\}\), where

\[
 x_e=0\quad\text{if }\operatorname{src}(e)\cap S=\varnothing, \tag{7.3}
\]

and, for each \(p\in S\),

\[
 \bigvee_{\substack{e:p\in\operatorname{src}(e),\\
 \operatorname{src}(e)\cap(S\setminus\{p\})=\varnothing}}x_e. \tag{7.4}
\]

All ten escape clauses (7.2) remain active in every branch.

#### Proof

The finite set of selected augmented arcs has an inclusion-minimal parent
cover \(S\).  Equation (7.3) says \(S\) covers it.  Minimality is equivalent
to (7.4): if (7.4) failed for \(p\), every selected arc supplied by \(p\)
would also be supplied by another member of \(S\), so \(S\setminus\{p\}\)
would still cover the path; the converse is immediate.

If \(|S|\le2\), enlarge \(S\), if necessary, to a pair \(\{i,j\}\).  Every
selected arc then has support meeting that pair, contradicting (7.2).
Hence \(|S|\ge3\), giving exactly ten triple, five quadruple, and one
five-parent possibility.  Conversely every Hall-perfect chronology has such
a minimal cover, so the branches lose none.  All pair escapes remain needed:
minimality of one cover \(S\) does not rule out an incomparable two-parent
cover.  \(\square\)

The normal-arc sizes of the sixteen canonical branches are

| branch | arcs | branch | arcs |
|---|---:|---|---:|
| 034 | 14,510 | 0123 | 19,751 |
| 012 | 15,890 | 0124 | 19,808 |
| 014 | 15,909 | 0134 | 19,823 |
| 013 | 15,920 | 0234 | 20,324 |
| 123 | 16,246 | 1234 | 21,422 |
| 124 | 16,370 | 01234 | 23,628 |
| 023 | 16,382 |  |  |
| 024 | 16,434 |  |  |
| 134 | 17,593 |  |  |
| 234 | 17,890 |  |  |

These branch counts and pair escapes are valid only for the five hashes in
Section 1.  They must not be transferred to the different base-plus-four-
relabels CAA catalogue.

There is also an allowance distinction.  The pair artifacts exclude a
Hall-perfect carrier on a pair; they do not exclude every pair-supported
carrier of deficiency at most \(28\).  Hence (7.2) and the sixteen-branch
cover are lossless for the allowance-zero Hall search.  They may be used as
a restricted positive hunt at allowance \(28\), because any returned
matching improvement remains genuine, but exhaustion of those branches
would not prove that no unrestricted Hall-29 improvement exists.

## 8. Soft homotopy and the hard acceptance boundary

Let \(s_i(x)\) be a fixed scored row and \(t_i\) its threshold.  The legacy
hard max-min mode first imposes

\[
                         s_i(x)\ge t_i\quad\text{for all }i. \tag{8.1}
\]

It then creates

\[
 0\le z\le W,\qquad z\le s_i(x)-t_i,                  \tag{8.2}
\]

and maximizes \(z\).  The lower bound zero is not a bug: it is redundant
after (8.1).  This mode optimizes slack only inside the already hard-feasible
region.

The new `--soft-fixed-homotopy --hint-path FILE` mode has different
semantics.  During its warm phase, the fixed-row builders omit (8.1), create

\[
 -t_{\max}\le z\le W,\qquad z\le s_i(x)-t_i,
 \qquad t_{\max}:=\max_i t_i.                         \tag{8.3}
\]

and maximize \(z\).  Since every score is nonnegative, the displayed lower
bound represents every possible signed margin for the supplied rows.  Literal
shore thresholds satisfy $t_{\max}\le|\mathcal T|=16383$.
In particular the warm phase adds no accidental condition
\(s_i(x)\ge t_i-W\) when \(t_i>W\).
A feasible soft incumbent, even one with positive
margin, is only a path hint.  The code then

1. writes its complete middle path to `FILE`;
2. clears the soft objective;
3. restores every omitted hard row (8.1);
4. replaces earlier hints by the complete soft path; and
5. solves the original hard model.

Persisted global moving-DM rows are installed before this phase and remain
hard throughout.  The implementation also rejects simultaneous competing
objective modes.  Therefore soft homotopy changes search order but cannot
weaken a shore cut, a support escape, or terminal acceptance.

In particular, soft scores from restricted pair tables cannot be used on the
full five-parent model after the catalogue-equality assertions of Section 6.
Any fixed rows used for homotopy must themselves satisfy their declared
producer/consumer contract.

## 9. Executable exact loop and certificate boundary

The current implementation is split into three independently checkable
pieces.

* `scratch/search_k15_directed_parent_union_cpsat.py` builds the selected
  Hamilton path, exact position channel, upper/residence constraints,
  support branches, persisted shore rows, and the soft-to-hard hint phase.
* `scratch/search_k15_caa29_five_parent_benders.py` persists each returned
  shore, hashes every parent/candidate/cut, and refuses the canonical
  pair-escape option unless all five hashes agree with Section 1.
* `scratch/audit_k15_global_five_parent_exact_dm.py` fixes H29 inside the
  \(23,628\)-arc consumer and compares the formula cells, independently
  reconstructed complete-carrier cells, and the native fixed-shore score.

The in-process improvement mode is
`--dynamic-exact-dm --dynamic-dm-allowance 28`.  The outer Benders
orchestrator persists allowance-zero shores and therefore continues to Hall
zero; it does not stop merely because a matching of size \(16,355\) has been
seen.

Every persisted shore must have format
`K15_POSITION_EXACT_DM_SHORE_V1`, allowance zero, a present source-candidate
file with the recorded SHA-256, a duplicate-free in-range cell list, and a
saved deficiency equal to target count minus cell count.  Before loading the
row, the consumer recomputes both formula and complete-carrier cell lists on
that source chronology and requires literal equality with the saved native
list.

For a theorem-level positive output, the following checks are mandatory.

1. The selected path uses only the declared augmented branch catalogue, is
   Hamilton, residence-safe, and has every required upper target.
2. Every dynamically returned DM shore has identical position,
   complete-carrier, and native cell lists on that selected path.  For a
   preloaded fixed shore on a later incumbent, the position and complete-
   carrier lists are identical and their common cardinality equals the native
   fixed-shore total; that native interface does not emit a third cell list.
   A persisted allowance-zero DM shore additionally receives literal saved/
   native/formula/carrier list equality on its own hashed source chronology
   before loading.
3. A strict H29 improvement is certified by a matching of size at least
   \(16,355\) and an equal-size cover in the **full** compiler graph.
4. Hall zero is certified by a \(16,383\)-edge matching and an equal-size
   cover; the independent verifier checks every emitted edge and every cover
   incidence.

For a theorem-level negative output, scope is equally important.

* `UNKNOWN`, timeout, a smoke limit, or a Benders round limit is no
  obstruction.
* `INFEASIBLE` in one branch concerns only that exact parent subset,
  minimal-cover rows, all ten pair escapes, residence/upper constraints, and
  the exact accumulated shore list recorded in its manifest.
* A global canonical-five obstruction requires all sixteen branches to be
  closed.  A restricted-face `INFEASIBLE` result is not such a closure.
* Without a separately checkable proof log, CP-SAT `INFEASIBLE` remains a
  trusted-solver finite certificate rather than a solver-independent formal
  derivation.

The exact cut loop may therefore return one of three mathematically distinct
objects: a global matching improvement; a Hall-zero compiler matching; or a
precisely scoped finite branch obstruction.  It cannot return a projected or
fixed-shore improvement as a substitute.

## 10. H100 run results — intentionally unfilled

This section must be completed only from files produced by the exact H100
run.  At the audited source snapshot no result is claimed.

```text
H100 host / repository:
executed solver SHA-256:
executed Benders SHA-256:
executed Hall-auditor SHA-256:
five parent SHA-256 values:
branch(es):
allowance (28 or 0):
resident/upper settings:
persisted shore count:
terminal solver status:
terminal native matching:
terminal deficiency:
matching certificate path + SHA-256:
cover certificate path + SHA-256:
independent verifier status:
if negative, exact certified scope:
```

No entry such as `FEASIBLE`, `UNKNOWN`, a projected margin, or a fixed-shore
score is sufficient to fill the matching lines.

## 11. Proved and conditional boundary

Proved in this note:

1. the exact endpoint-correct mandatory-mask identity (2.6);
2. the exact \(19,311\)-cell count, including all \(36\) collar cells;
3. equisatisfiability of the one-way target-witness row with the literal Hall
   inequality;
4. exact DM separation and finite non-relocation of deficiency;
5. the catalogue-equality requirement for precomputed motif completeness;
6. the ten pair-escape consequence and the lossless \(10+5+1\) canonical
   minimal-cover hierarchy; and
7. sound separation of signed soft homotopy from hard shore and matching
   acceptance.

Conditional on execution and independent verification:

1. allowance \(28\) can produce a globally certified decrease below Hall
   deficiency \(29\);
2. allowance \(0\) can produce Hall zero; or
3. exact completion of all sixteen branches can produce a finite canonical-
   catalogue obstruction.

None of these three computational outcomes is asserted here.
