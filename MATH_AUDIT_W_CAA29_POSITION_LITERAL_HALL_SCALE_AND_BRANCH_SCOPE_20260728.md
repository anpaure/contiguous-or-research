# Lane W audit: motif scale, the position-literal Hall channel, and the scope of the pair-face decomposition

Date: 2026-07-28

## 0. Verdict

The centered-motif implementation in
`scratch/search_k15_caa29_five_parent_benders.py` is exact, but it is not a
viable iterative Benders representation at the scale now measured by Lane C.
One five-parent DM shore has approximately

\[
  11.8\cdot 10^6\quad\hbox{centered motifs}
\]

and its serialized catalogue is approximately `474 MB`.  The consumer makes
one Boolean conjunction indicator for every motif.  Thus even the first cut
has 11.8 million new Boolean variables and 23.6 million reified Boolean
constraints.  Subsequent cuts grow linearly.  This representation must not be
used for the H100 launch.

The generic directed-parent solver now contains the correct replacement:
`--dynamic-exact-dm` constructs one shared, exact, position-indexed channel
for all 19,311 physical compiler cells and adds a compact literal witness for
each returned DM shore.  The channel is equisatisfiable with the exact Hall
shore inequality.  The native maximum-matching separation then makes the
loop relocation-safe: a moved deficiency is another rejected incumbent, not
an accepted repair.

The replacement is much smaller but not free.  The shared channel has
787,005 Boolean variables and 19,305 integer variables, in addition to the
successor model.  Each DM shore adds exactly 386,216 Boolean variables,
77,242 integer variables, and 772,433 CP-SAT constraints.  Moreover the
shore target array is repeated in 19,311 `Element` constraints.  Therefore a
modest number of in-process cuts is plausible; hundreds of accumulated cuts
are not.  The launch should use the position channel directly, never first
materialize or merge adaptive motif TSV files.

There is a separate scope correction.  The proved `10+5+1` minimal-parent
branch decomposition applies to the five *canonical face parents* in
`MATH_K15_FIVE_FACE_MINIMAL_PARENT_COVER_DECOMPOSITION_20260728.md`.  Its ten
pair-UNSAT premises have not been proved for the CAA catalogue consisting of
the base parent and the four pure coordinate relabels

\[
 (1,12),(3,4),(10,11),(3,13)
\]

(zero-based indices).  Consequently those escape cuts and the omission of
one- and two-parent branches are not yet lossless for CAA.

## 1. Why the adaptive motif channel is not launchable

For an adaptive centered pattern of compiler depth \(h\in\{0,1,2\}\), the
consumer forms the equivalence

\[
 z_M\ \longleftrightarrow\
 \left(\bigwedge_{e\in M}x_e\right)\wedge L_M\wedge R_M,
 \tag{1.1}
\]

where \(|M|=5+h\), and \(L_M,R_M\) are the two endpoint-distance guards.
The implementation of an equivalence is one enforced `BoolAnd` plus one
`BoolOr`.  Hence a catalogue with \(P\) patterns contributes exactly

* \(P\) Boolean variables;
* \(2P\) Boolean constraints; and
* at least \(2\cdot7P\) input-literal incidences, because every conjunction
  has at least seven inputs.

For \(P=11.8\cdot10^6\), this is at least 165.2 million literal incidences.
Even if one counts only four-byte literal indices, those incidences occupy
at least 660.8 MB before variables, constraint headers, protocol-buffer
overhead, names, Python objects, or the 474 MB source text are counted.
The Python parser simultaneously retains split input lines and tuple/list
representations of the patterns, so peak construction memory is necessarily
far above the serialized file size.

The outer CAA script also rebuilds the union of all previous adaptive
catalogues on every Benders round.  Thus the representation cost is
\(\Theta(rP)\) after \(r\) comparable shores.  The batching parameter limits
the number of shores traversed by one projection process; it does not reduce
the final number of indicators or constraints.  This is a representation
obstruction, not merely a need for a longer time limit.

## 2. Exact physical-cell normal form

Let a selected Hamilton chronology be

\[
  P=(P_0,P_1,\ldots,P_{W-1}),\qquad W=6435,
\]

and put, for \(0\le j\le W+2\),

\[
 Q_j=\bigcap_{i=\max(0,j-3)}^{\min(j,W-1)}P_i.
 \tag{2.1}
\]

For \(h\in\{0,1,2\}\) and \(0\le b\le W+2-h\), write

\[
 I_{b,h}=\{b,b+1,\ldots,b+h\},\qquad
 E_{b,h}=\bigcup_{j\in I_{b,h}}Q_j.
 \tag{2.2}
\]

The exact complete-carrier mandatory mask is

\[
 M_{b,h}=
 \begin{cases}
 E_{b,h}\setminus Q_{b+h+1},&b+h<3,\\
 E_{b,h}\setminus Q_{b-1},&b\ge W,\\
 E_{b,h}\setminus(Q_{b-1}\cap Q_{b+h+1}),&\text{otherwise}.
 \end{cases}
 \tag{2.3}
\]

This is the complete-carrier identity used by the native compiler.  A lower
target \(T\) fits the physical cell \((b,h)\) if and only if

\[
 M_{b,h}\subseteq T\subseteq E_{b,h}
 \quad\hbox{and}\quad
 T\cap Q_j\ne\varnothing\quad(j\in I_{b,h}).
 \tag{2.4}
\]

There are exactly

\[
 (W+3)+(W+2)+(W+1)=19,311
 \tag{2.5}
\]

such cells.  Formula (2.3) is also reconstructed independently in
`evaluate_global_exact_shore`: for every occurrence-coordinate pair it
builds the complete carrier and compares the union of carriers wholly
contained in the cell with the formula mask.  For every returned DM shore,
the resulting cell list is required to equal the native auditor's literal
`dm_cell_indices` list, not merely have the same cardinality.

## 3. Equisatisfiability of one position-indexed shore cut

Fix a nonempty shore \(A\) of distinct lower targets and an allowance
\(a\ge0\).  For every physical cell \(c=(b,h)\), the model introduces one
claim bit \(z_c\), one selected target \(T_c\in A\), and, for every
\(j\in I_{b,h}\), one selected coordinate \(u_{c,j}\in[15]\).  Conditional
on \(z_c=1\), it imposes

\[
 M_c\subseteq T_c\subseteq E_c,
 \qquad u_{c,j}\in T_c\cap Q_j\quad(j\in I_c).
 \tag{3.1}
\]

Finally it imposes

\[
             \sum_c z_c\ge |A|-a.                     \tag{3.2}
\]

### Theorem 3.1 (literal Hall equivalence)

For a fixed selected chronology \(P\), the auxiliary variables in
(3.1)--(3.2) have a feasible assignment if and only if

\[
                       |N_P(A)|\ge |A|-a.              \tag{3.3}
\]

#### Proof

If \(z_c=1\), (3.1) and (2.4) prove that the physical cell \(c\) belongs to
\(N_P(A)\).  There is only one claim variable per cell, so (3.2) gives at
least \(|A|-a\) distinct cells in the neighbourhood.

Conversely, suppose (3.3).  Choose \(|A|-a\) distinct fitting cells.  For
each chosen cell select one fitting target \(T_c\in A\).  By (2.4), each
intersection \(T_c\cap Q_j\) is nonempty; choose any coordinate in it as
\(u_{c,j}\).  Set the corresponding claims to one and all other claims to
zero.  All constraints conditional on a false claim are vacuous.  This
constructs the required auxiliary assignment. \(\square\)

Reusing one target for many cells is intentional and sound: Hall's
neighbourhood counts distinct right cells, not a matching inside the fixed
shore.  Conversely, using one claim per cell prevents a cell from being
counted twice.

## 4. Exact size of the new encoding

The shared global order/compiler channel creates the following Booleans:

\[
\begin{array}{c|r}
\text{family}&\text{count}\\ \hline
\text{middle-set bits}&6435\cdot15=96,525\\
\text{compact endpoint allowed bits}&2\cdot9\cdot15=270\\
\text{left/right interior guards}&2\cdot6435=12,870\\
\text{compact endpoint envelope/mandatory/blocker bits}&1,440\\
\text{global }Q_j\text{ bits}&6438\cdot15=96,570\\
\text{global cell envelope and mandatory bits}&19311\cdot30=579,330
\end{array}
\]

for a total of 787,005.  It also creates 6,435 position variables, 6,435
inverse-position variables, and 6,435 middle-mask variables, hence 19,305
integer variables.

For one shore, the exact counts are

\[
 \sum_c |I_c|=6438+2(6437)+3(6436)=38,620.             \tag{4.1}
\]

Thus one cut has

\[
\begin{aligned}
\text{Booleans}
 &=19,311+15(19,311)+2(38,620)=386,216,\\
\text{integers}
 &=2(19,311)+38,620=77,242.                            \tag{4.2}
\end{aligned}
\]

The exact constraint count in `add_global_exact_dm_constraint` is

\[
 32(19,311)+4(38,620)+1=772,433.                       \tag{4.3}
\]

There is a hidden constant-array cost: each of the 19,311 target-selection
`Element` constraints stores the shore's target list.  For \(|A|=1524\),
this is 29,429,964 integer entries, or about 117.7 MB at four bytes per entry,
before protocol-buffer overhead.  For larger moving shores this term grows
as \(19,311|A|\).  The position channel remains decisively smaller than the
11.8-million-motif expansion, but this term is the principal reason not to
accumulate hundreds of shores in one CP-SAT model.

## 5. Moving-DM separation cannot accept relocated deficiency

Let \(G_P\) be the exact lower-target/physical-cell compiler graph of a
chronology \(P\).  A native maximum matching and equal-size Koenig cover
give both \(\nu(G_P)\) and, when the deficiency is positive, a DM shore
\(A_P\) satisfying

\[
 |A_P|-|N_P(A_P)|=16383-\nu(G_P).                      \tag{5.1}
\]

Run the following loop with allowance zero.

1. Solve the current Hamilton, residence, upper, and accumulated shore
   model.
2. Independently compute \(\nu(G_P)\).
3. If \(\nu(G_P)=16383\), stop and emit the matching/cover certificate.
4. Otherwise add the exact position cut \(|N(A_P)|\ge|A_P|\) and repeat.

Every nonterminal round excludes its incumbent, because that incumbent
violates its newly added cut by (5.1).  An incumbent that moves the defect to
a new shore still has matching size below 16,383 and therefore returns to
step 4.  It cannot be accepted.  Since the successor-factor space is finite,
an exact unlimited loop eventually finds a Hall-perfect chronology or proves
the accumulated model infeasible.  A timeout, `UNKNOWN`, or a finite round
limit proves neither outcome.

This is precisely the all-shore certificate required by the rollback score:
the terminal value is the independently certified matching size, not the
number of old shores repaired.

## 6. Exact pair-face branch clauses

For completeness, here is the lossless branch theorem in its correct scope.
Let five parent arc sets be \(E_0,\ldots,E_4\), and let

\[
 \operatorname{src}(e)=\{p:e\in E_p\}.
\]

For a proposed inclusion-minimal cover \(S\subseteq[5]\), impose

\[
 x_e=0\quad\text{if }\operatorname{src}(e)\cap S=\varnothing,             \tag{6.1}
\]

and, for every \(p\in S\),

\[
 \bigvee_{\substack{e:\ p\in\operatorname{src}(e),\\
          \operatorname{src}(e)\cap(S\setminus\{p\})=\varnothing}}
 x_e.                                                                     \tag{6.2}
\]

Equation (6.1) says that \(S\) covers the chosen arcs, and (6.2) says that
deleting \(p\) destroys that cover.  Every finite selected arc set has at
least one inclusion-minimal cover, although it may have several; these
branches form an exhaustive union, not necessarily a disjoint partition.

If, in addition, every two-parent union \(E_i\cup E_j\) is proved incapable
of a terminal carrier, then every terminal carrier obeys the ten escape cuts

\[
 \boxed{\quad
 \bigvee_{e:\operatorname{src}(e)\cap\{i,j\}=\varnothing}x_e,
 \qquad 0\le i<j<5.\quad}                              \tag{6.3}
\]

It follows that some inclusion-minimal cover has size at least three, so the
16 branches

\[
             \binom53+\binom54+\binom55=10+5+1         \tag{6.4}
\]

are exhaustive for terminal carriers.  Clauses (6.3) should remain active in
every branch; minimality alone does not imply all pair escapes when a path
has different incomparable minimal covers.

The authoritative ten UNSAT summaries are in
`scratch/k15_exact_pair_nogos_20260728/` and have exactly the hashes recorded
in handoff item 1466.  They concern

\[
\begin{array}{ll}
P_0=&\texttt{k15_doubletrans_05_213_hall29.json},\\
P_1=&\texttt{k15_outer2_p1_h30_bridge.json},\\
P_2=&\texttt{k15_trans1113_balanced_hall31.json},\\
P_3=&\texttt{k15_transposition_parent_winner.json},\\
P_4=&\texttt{k15_accumulated_zero_parent_winner.json}.
\end{array}
\]

For that canonical catalogue, the normal-arc counts of the 16 branches are

\[
\begin{array}{c|r@{\qquad}c|r}
S&|E_S|&S&|E_S|\\ \hline
034&14510&0123&19751\\
012&15890&0124&19808\\
014&15909&0134&19823\\
013&15920&0234&20324\\
123&16246&1234&21422\\
124&16370&01234&23628\\
023&16382&&\\
024&16434&&\\
134&17593&&\\
234&17890&&
\end{array}
\tag{6.5}
\]

These counts are catalogue fingerprints, not estimates; they must not be
reused as CAA branch counts.

They do **not** certify pair escape for the CAA parent list.  To apply
(6.3)--(6.4) to CAA without losing solutions, one must first run and certify
all ten pair models for the exact five CAA parent hashes, with the same
terminal Hall semantics.  Until then, CAA needs the singleton and pair
minimal-cover branches as well, or no support branching at all.

The implemented branch model uses parent-only dummy endpoints.  Accordingly,
`src` in (6.1)--(6.3) includes dummy-to-start and end-to-dummy arcs, and every
escape clause is formed from full augmented parent support.

There is a second, independent scope restriction.  The pair fixed-DM motif
tables have producer catalogues strictly smaller than the 23,628-arc
five-parent consumer, and their endpoint maxima range only over pair collars.
They are therefore not five globally exact fixed-shore predicates.  Their
pair-UNSAT results justify (6.3) for a terminal Hall-perfect target, but the
five-parent moving-DM model must score every shore on the actual full/branch
chronology.  The position channel does this; pair-local motif sums cannot be
substituted.

## 7. Deployment boundary

The theorem-level safe launch configuration is therefore:

* use the exact five CAA parent hashes and explicitly interpret every listed
  transposition as zero-based;
* use the shared 19,311-cell `--dynamic-exact-dm` channel with allowance zero;
* retain the native matching/Koenig-cover audit as the only terminal Hall
  test;
* do not materialize adaptive centered motif catalogues;
* treat any finite Benders exhaustion or CP-SAT `UNKNOWN` as inconclusive;
* do not import the canonical five-face escape cuts or `10+5+1` branch
  deletion into CAA until its own ten pair premises are certified.

No Hall-zero carrier and no CAA pair-UNSAT theorem is claimed here.
