# The forced K17 `U | YAX` Catalan braid and its fixed-U CSP

Date: 2026-07-31  
Status: exact block theorem, palette ledger, residence reduction, and finite
native CSP proved; no labelled K17 braid or word is claimed

## 0. Verdict

The notation

\[
 U\mid (Y_iA_iX_i)_{i=1}^{1430}
\tag{0.1}
\]

has a literal spanning interpretation.  Here `U` is one path block containing
all 5005 no-new-coordinate owners.  Each (A_i,X_i,Y_i) is a nonempty
**path block**, not one vertex, and each of the three block families contains
6435 vertices in total.  Hence (0.1) contains

\[
 5005+3\cdot6435=24310=\binom{17}{9}
\]

owners.

Three exact conclusions follow.

1.  There is an integral unlabelled block skeleton with 715 block triples of
    sizes
    \((|A|,|X|,|Y|)=(4,5,5)) and 715 of sizes ((5,4,4)).
    Every (x)-run and every (y)-run then has length nine, so the two new
    coordinates contribute

    \[
      (\rho_1,\rho_2,\rho_3)=(0,0,0).
    \]

2.  In the one-hole lower-q1-rainbow class, the sector counts force every
    external macro seam to have no-new-coordinate intersection.  Therefore
    all 1430 macros after (U) have one common orientation.  Once the
    labelled blocks are fixed, their possible order is not a (1430!)
    search: equality of old rank-eight endpoint labels gives a partial
    functional digraph.  For a fixed (U) endpoint there are at most
    (2\cdot9=18) complete after-(U) chronologies to replay.

3.  The fixed-U labelled construction is an exact finite CSP.  In the native
    PBBS-edge subclass it has 148014 candidate directed arcs per chosen
    global orientation, 19305 tail-order integers, and 40755 q1 palette rows,
    besides the fixed-U empty-signature precheck.  Arbitrary upper coverage
    composes by a four-field interval-summary monoid; residence composes by a
    six-state run automaton.  No variable describing the internal (U) search
    is needed after its interface is frozen.

The authenticated PBBS parent clears every marginal deck row, but the coupled
macro/socket/order CSP has not been solved.  In particular, this note does
not prove an upper-complete carrier, the lower common-cap compiler, or
\(\nu(17)=24313\).

## 1. Decks and parameters

Let (E=[15]), add coordinates (x,y), and put

\[
 W=\binom{15}{8}=6435,qquad
 N=\binom{15}{9}=5005,qquad
 b=W-N=1430=C_8.
\tag{1.1}
\]

The four rank-nine owner decks are

\[
 A=C+xy,quad |C|=7;qquad
 X=T+x,quad Y=T+y,quad |T|=8;qquad
 U=V,quad |V|=9.
\tag{1.2}
\]

Fix a directed Johnson path

\[
 \mathcal U=(U_1,\ldots,U_N)
\tag{1.3}
\]

through the complete (U)-deck.  For (1\le i\le b), let

\[
 \mathcal Y_i=(T^Y_{i,1}+y,\ldots,T^Y_{i,y_i}+y),
\]

\[
 \mathcal A_i=(C^A_{i,1}+xy,\ldots,C^A_{i,a_i}+xy),
\]

\[
 \mathcal X_i=(T^X_{i,1}+x,\ldots,T^X_{i,x_i}+x)
\tag{1.4}
\]

be nonempty Johnson paths partitioning their respective decks.  Thus

\[
 \sum_i a_i=\sum_i x_i=\sum_i y_i=W.
\tag{1.5}
\]

The forward and reverse macros are

\[
 B_i^+=\mathcal Y_i\mathcal A_i\mathcal X_i,qquad
 B_i^-=\overleftarrow{\mathcal X_i},
       \overleftarrow{\mathcal A_i},
       \overleftarrow{\mathcal Y_i}.
\tag{1.6}
\]

For (B_i^+), the two internal sockets are Johnson exactly when

\[
 C^A_{i,1}\subset T^Y_{i,y_i},qquad
 C^A_{i,a_i}\subset T^X_{i,1}.
\tag{1.7}
\]

The reverse macro uses the same two undirected sockets.  A forward
macro-to-macro seam is Johnson exactly when

\[
 T^X_{i,x_i}=T^Y_{j,1};
\tag{1.8}
\]

the equality is forced because an (X)-owner and a (Y)-owner are adjacent
only when their old rank-eight projections coincide.  The initial seam is
Johnson exactly when

\[
 T^Y_{i,1}\subset U_N
\tag{1.9}
\]

in the forward orientation, with (X,Y) interchanged in the reverse
orientation.

## 2. Exact unlabelled Catalan skeleton

### Theorem 2.1 (length-nine tag skeleton)

There are positive block lengths satisfying (1.5) for which every (x)-run
and every (y)-run in (0.1) has length nine.

### Proof

Take 715 values (a_i=4) and 715 values (a_i=5), and put

\[
 x_i=y_i=9-a_i.
\tag{2.1}
\]

Then

\[
 \sum_i a_i=715(4+5)=6435
\]

and the same identity holds for (x_i,y_i).  In a forward macro, the
(x)-run is (mathcal A_i\mathcal X_i) and the (y)-run is
(mathcal Y_i\mathcal A_i); both have length nine.  In a reverse macro the
same two runs occur in reverse order.  The pure (U)-prefix contains neither
new coordinate, and consecutive macros are separated from one another in
both tag traces.  Hence there is no internal positive (x)- or (y)-run of
length at most eight.  In particular their three K17 staircase frontiers are
zero.  \(\square\)

This is an unlabelled construction.  A labelled PBBS block cover need not
have the prescribed component-length multiset; imposing (2.1) is a strong
finite CSP constraint, not a consequence of the deck counts.
The assertion that every run has length nine refers to the common forward
orientation in (0.1), or its full reversal.  With mixed macro orientations
some tag runs merge to length eighteen; the zero-frontier conclusion still
holds, but the exact length-nine statement does not.

## 3. The forced lower-q1 ledger

The internal and intra-macro edge counts are independent of the block
lengths:

\[
 \#UU=N-1=5004,qquad
 \#AA=\#XX=\#YY=W-b=N=5005,
\tag{3.1}
\]

and there are (b) `YA` sockets and (b) `AX` sockets.  The path has one
(U)-to-tail seam and (b-1) macro-to-macro seams, hence (b=1430)
external seams in total.

The possible seam signatures are

\[
\begin{array}{c|c|c|c}
(\epsilon,\epsilon')&\text{socket}&\text{intersection tag}&\text{union tag}\\ \hline
(+,+)&X\to Y&00&xy\\
(+,-)&X\to X&x&x\\
(-,+)&Y\to Y&y&y\\
(-,-)&Y\to X&00&xy.
\end{array}
\tag{3.2}
\]

The seam adjacent to (U) always has lower tag (00).

### Theorem 3.1 (macro orientation is forced)

Assume all 24309 path-edge intersections are distinct.  Then every external
macro seam has lower tag (00), so all macros in the after-(U) packet have
one common orientation.  The lower palette has exact signature sizes

\[
\begin{array}{c|c|c}
\text{signature}&\text{edge slots}&\text{target count}\\ \hline
xy&W-b=5005&\binom{15}{6}=5005\\
x&(W-b)+b=6435&\binom{15}{7}=6435\\
y&(W-b)+b=6435&\binom{15}{7}=6435\\
00&(N-1)+b=6434&\binom{15}{8}=6435.
\end{array}
\tag{3.3}
\]

Consequently the (xy,x,y) families are complete exactly once and the
(00) family is complete except for one boundary colour.

### Proof

Before macro-to-macro seams, (3.1) and the `YA/AX` sockets already give
5005 (xy)-tagged edges and 6435 edges of each one-tag type.  These equal
the total numbers of colours of their signatures.  An additional (x)- or
(y)-tagged seam would put 6436 distinct edges into a 6435-colour family,
contradicting the assumed rainbowness.  Table (3.2) therefore permits only
equal adjacent orientations, proving constancy.  All (b) external seams
then have tag (00), and (3.3) follows.  Since the total number of edges is
one below the complete lower layer, distinctness gives the stated palette.
\(\square\)

This orientation theorem is exact for the block-preserving one-hole
lower-rainbow class.  It is not WLOG if repeated q1 colours or external
lower-compiler repair are allowed.

Writing only old projections, the exact lower multisets in the forward
orientation are

\[
\begin{aligned}
\mathcal L_{xy}&=
 \{C^A_{i,t}\cap C^A_{i,t+1}\},\\
\mathcal L_x&=
 \{T^X_{i,t}\cap T^X_{i,t+1}\}\sqcup\{C^A_{i,a_i}\},\\
\mathcal L_y&=
 \{T^Y_{i,t}\cap T^Y_{i,t+1}\}\sqcup\{C^A_{i,1}\},\\
\mathcal L_{00}&=
 \{U_t\cap U_{t+1}\}\sqcup\{T^Y_{1,1}\}
 \sqcup\{T^X_{i,x_i}:i<b\}.
\end{aligned}
\tag{3.4}
\]

Thus (3.4), not a scalar count, is the exact q1 lower replay.

## 4. Exact upper-q1 signatures

For the forward orientation (U\mid YAX\cdots YAX), the upper-q1 slot
ledger is

\[
\begin{array}{c|c|c}
\text{signature}&\text{edge slots}&\text{target count}\\ \hline
00&N-1=5004&\binom{15}{10}=3003\\
x&W-b=5005&\binom{15}{9}=5005\\
y&(W-b)+1=5006&\binom{15}{9}=5005\\
xy&(W-b)+3b-1=9294&\binom{15}{8}=6435.
\end{array}
\tag{4.1}
\]

The reverse orientation interchanges the (x)- and (y)-rows.  Targetwise,
the forward multisets are

\[
\begin{aligned}
\mathcal U_{00}&=\{U_t\cup U_{t+1}:t<N\},\\
\mathcal U_x&=\{T^X_{i,t}\cup T^X_{i,t+1}\},\\
\mathcal U_y&=\{T^Y_{i,t}\cup T^Y_{i,t+1}\}\sqcup\{U_N\},\\
\mathcal U_{xy}&=
 \{C^A_{i,t}\cup C^A_{i,t+1}\}
 \sqcup\{T^Y_{i,y_i}:1\le i\le b\}\\
&\hspace{18mm}\sqcup\{T^X_{i,1}:1\le i\le b\}
 \sqcup\{T^X_{i,x_i}:1\le i<b\}.
\end{aligned}
\tag{4.2}
\]

It follows that:

* every no-new q1 target must be supplied inside (U);
* the (x)-only internal (X)-edges must be an exact occurrence transversal
  of the 5005 old rank-nine targets;
* the (y)-only internal edges together with the entrance value (U_N)
  must cover those same 5005 targets; and
* (xy)-coverage is the targetwise support condition on the last line of
  (4.2), not a consequence of its 2859 surplus slots.

These statements are necessary and sufficient for upper-q1 completeness of
the displayed braid.

## 5. All-depth upper signature theorem

### Theorem 5.1 (tag-separated interval providers)

In the forward braid:

1. an interval has tag (00) iff it lies wholly inside (U);
2. it has tag (x) iff it lies wholly inside one (X_i);
3. it has tag (y) iff it lies wholly inside one (Y_i), or it is a suffix
   of (U) followed by a nonempty prefix of (Y_1); and
4. every other interval meeting the tail has tag (xy).

For the reverse braid interchange (x) and (y).

### Proof

The status word is

\[
 00^N\,(01^{y_i}11^{a_i}10^{x_i})_{i=1}^b.
\]

An interval containing an (A)-state has both tags.  An interval crossing
between two tail sector blocks also either meets (A) or crosses an
(X|Y) boundary, and hence has both.  The only boundary involving the
tag-zero prefix is (U|Y_1), which gives the additional (y)-only class.
The four cases are exhaustive.  \(\square\)

This classification is for the linear common-orientation braid.  Mixed
orientations add `X|X` and `Y|Y` crossing intervals, while cyclically closing
the word adds a wrap collar.  The summary algebra below remains valid for
either extension when fed the actual literal order.

There is a compact exact evaluator for the old-coordinate OR condition.  For
a fixed target (S), summarize a word (Q) by

\[
 \Sigma_S(Q)=(H_S(Q),G_S(Q),P_S(Q),R_S(Q)),
\tag{5.1}
\]

where (H_S) records whether an interval has OR exactly (S), (G_S)
records whether every state is contained in (S), and (P_S,R_S) are the
ORs of the maximal (S)-contained prefix and suffix, with an empty marker.
Then

\[
 G_S(QR)=G_S(Q)G_S(R),
\tag{5.2}
\]

\[
 P_S(QR)=
 \begin{cases}P_S(Q)\cup P_S(R),&G_S(Q),\\P_S(Q),&\text{otherwise},\end{cases}
\tag{5.3}
\]

\[
 R_S(QR)=
 \begin{cases}R_S(Q)\cup R_S(R),&G_S(R),\\R_S(R),&\text{otherwise},\end{cases}
\tag{5.4}
\]

and

\[
\begin{aligned}
 H_S(QR)=H_S(Q)\vee H_S(R)\vee
 \bigl(&R_S(Q),P_S(R)\ne\varnothing\\
       &\text{ and }R_S(Q)\cup P_S(R)=S\bigr).
\end{aligned}
\tag{5.5}
\]

Equations (5.2)--(5.5) are associative because they are exact summaries of
literal concatenation.  Hence, after precomputing summaries for (U) and
each oriented macro, arbitrary upper completeness is an exact finite replay
with no interval-witness variables.  In particular, **all** no-new upper
depths are a fixed-U obligation.
For a variable-order SAT encoding, equivalent summary-state transition
variables are still required; “no interval-witness variables” refers to
replay after a candidate order is fixed.

## 6. New-coordinate residence and old-coordinate staircase

For arbitrary forward block lengths, the exact conditions for the stronger
**strict min-run-four subclass** are

\[
 y_i+a_i\ge4\quad(1\le i\le b),
\tag{6.1}
\]

\[
 a_i+x_i\ge4\quad(1\le i<b).
\tag{6.2}
\]

The final (x)-run is a right-boundary run and imposes no condition.  In the
reverse orientation interchange (x,y).  Theorem 2.1 satisfies these with
margin five.  Equations (6.1)--(6.2) are sufficient, not necessary, for the
general monotone staircase: an early short run can be legal.  The exact CSP
runs the automaton below on (x,y) as well as the fifteen old coordinates and
imposes their common frontier budget.

The old coordinates have a much sharper position constraint.  The tail
begins at absolute position

\[
 N=5005.
\]

### Lemma 6.1 (late-tail staircase exclusion)

Under the K17 budget

\[
 \rho_1+\rho_2+\rho_3\le7401,
\tag{6.3}
\]

no old coordinate may have an internal tail run of length one or two.  A
tail run of length three beginning at absolute position `s` must satisfy

\[
 s\le7401-\rho_1-\rho_2\le7401,
\tag{6.4}
\]

so its tail-local start is at most 2396.

### Proof

A length-one run starting at `s >= 5005` contributes `s` to all three
frontiers, forcing their sum to be at least `3*5005=15015`.  A length-two
run contributes to `rho_2,rho_3`, forcing at least `2*5005=10010`.  Both
exceed 7401.  A length-three run contributes `s` to `rho_3`, giving (6.4).
\(\square\)

For the frozen PBBS parent, direct replay gives:

\[
 \minrun(T)=4,qquad \minrun(C)=3;
\tag{6.5}
\]

there are exactly 1425 length-four `T`-runs and 1425 corresponding
length-three `C`-runs, exactly 95 of each per old coordinate.  If all four
native edges incident with such a `C`-run are retained, its two zero
boundaries and three positive vertices remain internal to one `A`-block.
When its actual oriented child position is late, this is a literal forbidden
run.  Let `lambda_R=1` exactly for that late-placement case, and zero
otherwise.  With `a_e` denoting undirected native-edge retention, the exact
guarded cut row is

\[
 \sum_{e\in\operatorname{Inc}(R)}(1-a_e)\ge\lambda_R.
\tag{6.6}
\]

In the directed arc model, `a_uv=z_uv+z_vu`.  The lateness test uses
the run's actual position after block orientation; reversing a block moves
the start from the first to the last positive source vertex.  Applying
(6.6) unconditionally to all 1425 runs is only a stronger sufficient
subclass.  Equivalently, (6.6) may be separated lazily whenever replay finds
a late untouched run.

The exact edge-to-run incidence histogram is

\[
 0^{2265}1^{2760}2^{1290}3^{120}.
\tag{6.7}
\]

Condition (6.6) is not sufficient: split boundary fragments must still merge
correctly.  The exact test is a deterministic weighted run automaton.  For
each coordinate its six control states are

\[
 \mathsf B,\mathsf Z,\mathsf R_1,\mathsf R_2,\mathsf R_3,\mathsf R_4,
\tag{6.8}
\]

Here `B` is the uncharged initial boundary run, `Z` ends in zero, and `R_j`
records an eligible positive run with length capped at four.  The automaton
also carries the current run start and the three maximum registers
`rho_1,rho_2,rho_3`.  Closing `R_ell`, for `ell <= 3`, updates every
register `rho_j`, `j >= ell`, with that start.  No terminal zero is appended,
so the right boundary is correctly exempt.  A fixed `U` contributes its
fifteen control states together with their accumulated registers; the braid
CSP then processes macro transitions and imposes (6.3).

## 7. The finite fixed-U braid CSP

### 7.1 The exact U interface

The internal (U) search may be frozen to

\[
 \Xi(U)=
 \bigl(U_N,\mathcal L_U^-,
       (\Sigma_S(U))_S,
       ((\rho^U_{z,1},\rho^U_{z,2},\rho^U_{z,3},\mathsf s_z))_{z\in E}
       \bigr),
\tag{7.1}
\]

where `L_U^-` is its internal intersection multiset, `Sigma_S(U)` is the
full family of interval summaries from Section 5,
and the last tuple records both the accumulated frontiers and terminal run
state for every old coordinate.  The suffix fields inside `Sigma_S(U)`
handle the unique mixed entrance family.  The fixed prechecks are:

* `L_U^-` is simple; its complement has size 1431;
* every no-new upper target has `H_S(U)=1`; and
* the `U` endpoint has a legal rank-eight facet socket into the first
  macro.

After (7.1), no U-internal choice variable occurs in the braid CSP.

### 7.2 Fixed blocks: at most eighteen orders

Suppose the (b) legal triples ((\mathcal Y_i,\mathcal A_i,\mathcal X_i))
are fixed.  In the forward orientation define

\[
 \ell_i=T^Y_{i,1},\qquad r_i=T^X_{i,x_i},
\]

and put

\[
 i\longrightarrow j\quad\Longleftrightarrow\quad r_i=\ell_j.
\tag{7.2}
\]

The (ell_i)'s are distinct, as are the (r_i)'s, because the (X,Y)
blocks partition their owner decks.  Thus (7.2) has indegree and outdegree
at most one.  A spanning after-(U) order exists only if this partial
functional graph is one directed path, or one directed cycle that can be
opened at the entrance.  A rank-nine endpoint (U_N) has only nine
rank-eight facets, so at most nine starts are entrance-compatible.  Including
the reverse orientation gives at most eighteen complete orders.

For each candidate order, equations (3.4), (4.2), (5.2)--(5.5), and the run
automaton are unary deterministic replays.  This is the smallest exact
quotient after the blocks are fixed.

### 7.3 Constructing the blocks from native PBBS edges

There is also an exact pre-quotient CSP.  Restrict internal (A)-arcs to
the two frozen (C)-cycles and internal (X,Y)-arcs to the two frozen
(T)-cycles.  For one chosen global orientation, allow all directed:

\[
\begin{array}{c|r}
\text{arc family}&\text{candidates}\\ \hline
AA,XX,YY\text{ native internal}&38610\\
YA\text{ containment}&51480\\
AX\text{ containment}&51480\\
XY\text{ equality}&6435\\
U_NY\text{ endpoint}&9\\ \hline
\text{total}&148014.
\end{array}
\tag{7.3}
\]

Use one Boolean per candidate arc and 19305 tail order integers.  Every tail
vertex has indegree one; every tail vertex has outdegree one except for one
selected `X`-vertex of outdegree zero; and `U_N` has one selected arc to the
tail.  Conditional order increments on selected arcs exclude subtours.
Together with the allowed arc directions, these equations make one directed
path of the form `U | (YAX)^b`.  The exact q1 rows are

\[
 \sum_{AA:\,P\cap Q=Z}z_{PQ}=1
 \qquad\left(Z\in\binom E6\right),
\tag{7.4}
\]

\[
 \sum_{XX,AX:\,P\cap Q=C}z_{PQ}=1,qquad
 \sum_{YY,YA:\,P\cap Q=C}z_{PQ}=1
 \qquad\left(C\in\binom E7\right),
\tag{7.5}
\]

and, with one one-hot missing colour (h_T),

\[
 m_U^-(T)+\sum_{\text{external }e:\,P_e\cap Q_e=T}z_e
   =1-h_T
 \qquad\left(T\in\binom E8\right).
\tag{7.6}
\]

For upper q1 impose ALO rows from the exact union table, while the no-new
rows are the fixed-U precheck.  Equations (7.4)--(7.6) and the three
nonempty upper signature families give 40755 palette rows.  Connectivity,
the run automaton, and upper-summary acceptance complete an exact finite CSP
for the native fixed-U braid.

This formulation is exact only inside the native-edge, block-preserving,
one-hole-rainbow architecture.  It is a sufficient subclass, not WLOG for a
braid which changes (U), splits blocks, uses off-native internal edges, or
pays repeated lower colours through the compiler.

## 8. Frozen PBBS marginal audit

For

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    from3_markov_s7_merge.components.json
SHA-256 f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151
```

the (T_i) and (C_i=T_i\cap T_{i+1}) each enumerate their complete
6435-element layers once.  The native upper and depth-two occurrence fibres
are

\[
 V_i=T_i\cup T_{i+1}:\quad1^{3675}2^{1230}3^{100},
\tag{8.1}
\]

\[
 Z_i=C_i\cap C_{i+1}:\quad1^{3630}2^{1320}3^{55}.
\tag{8.2}
\]

Thus every marginal occurrence row needed to select 5005 (XX/YY) edges
and 5005 (AA) edges is nonempty.  This does not compose the selectors or
prove the socket matching.

The deterministic audit is

```text
scratch/audit_ad_k17_forced_u_yax_catalan_braid_20260731.py
  SHA-256 565ad73a4a61c506339883ce2a58476768b64d7827ab0dfbf9125539b5badccd
scratch/ad_k17_forced_u_yax_catalan_braid_20260731.audit.json
  SHA-256 7ebcad6941f6f9c8a4ca399abb71a56f9d7a127d690312c0a0c3bb19ffede608
  payload 4afd66493edbb81d5adfa7483f2239ebab8f3ea375a958e28b470c1681cb8728
```

No solver, stochastic search, web access, or long local computation was
used.

## 9. Exact remaining boundary

The following are proved:

* the literal 24310-owner block interpretation and balanced length-nine
  new-tag skeleton;
* the forced constant macro orientation and exact lower/q1-upper ledgers;
* the exact all-depth signature separation and associative upper evaluator;
* the late-tail old-coordinate staircase exclusions;
* the at-most-eighteen fixed-block quotient; and
* the finite native fixed-U CSP and its exact scope.

The following remain unproved:

1. a fixed (U)-path passing every no-new upper depth and its lower palette
   interface;
2. simultaneous native (A,X,Y) forest selectors with legal macro sockets;
3. a functional endpoint graph which is one (U)-compatible spanning path;
4. old-coordinate staircase acceptance and every signed upper target on the
   same candidate; and
5. the maximal-common-cap lower compiler after the carrier is fixed.

Thus the Catalan braid is now a precise finite construction problem
independent of the (U)-internal search, but it is not yet a K17 carrier.
