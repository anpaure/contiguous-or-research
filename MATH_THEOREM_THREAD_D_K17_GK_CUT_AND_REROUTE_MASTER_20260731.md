# The exact K17 Greene--Kleitman cut-and-reroute master

Date: 2026-07-31  
Status: fixed-base NO-GO proved; cut-and-reroute master exact; no feasible cut selection or K17 word is claimed.

## 1. Frozen seed

Let `F` be the two-cut Greene--Kleitman forest on the rank-seven layer of
`B_17`.  Its exact parameters are

\[
 |E(F)|=10152,\qquad |V(F)|=15376,\qquad
 \kappa(F)=5224.
\]

It has 10,448 endpoints, 4,928 internal vertices, 4,072 unused rank-seven
vertices, 10,152 distinct rank-eight edge unions, and 4,928 distinct
rank-nine internal turns.  The component-size distribution is

\[
 2^{2184}3^{1716}4^{876}5^{349}6^{83}7^{15}8^1.
\]

There are 2,224 rank-six colours absent from the seed.  Of these, 674 have
no original endpoint as a rank-seven superset, and 294 have all eleven
rank-seven supersets unused by the seed.

## 2. Why the advertised short-ear schedule is impossible

Consider an immutable-base ear completion.  Every new edge which is not
unused--unused meets an original endpoint.  Hence each of the 674 colours
with no endpoint superset must occur on an unused--unused edge.  If `x_j`
is the number of `j`-edge ears, then

\[
 \sum_jx_j=5223,\qquad
 \sum_j(j-1)x_j=1535,
\]

and the number of unused--unused edge slots is

\[
 \sum_{j\ge3}(j-2)x_j=x_1-3688.                 \tag{2.1}
\]

Consequently every fixed-base completion satisfies

\[
 \sum_{j\ge3}(j-2)x_j\ge674,
 \qquad x_1\ge4362.                              \tag{2.2}
\]

The proposed vector

\[
 (x_1,x_2,x_3,x_4)=(4024,905,252,42)
\]

has only `252+2*42=336` unused--unused slots, so it violates (2.2) by 338.
The `252/42` split is correct only inside the 294-row all-unused subfamily;
it is not a global schedule.

The complete local census is stronger.  Among all 674 no-endpoint rows,
266 admit a clean three-edge ear, another 128 admit a clean four-edge ear
but no clean three-edge ear, and 280 admit no clean ear of length at most
four.  Over all 2,224 missing colours, the cumulative zero-provider counts
for maximum ear length `1,2,3,4` are respectively

\[
 1930,\quad 938,\quad 644,\quad 488.             \tag{2.3}
\]

Here clean means: different seed components at the ends; distinct unused
internal vertices; fresh and mutually distinct rank-eight unions; and all
rank-nine turns, including the two boundary turns, of rank nine, fresh, and
mutually distinct.

There is also a compact arbitrary-length relaxation.  Its vertices are
fresh Johnson edges between original endpoints/unused vertices and
compatible rank-nine wedges at unused vertices.  Peeling unsupported
edge/wedge states leaves 145,117 edges and 4,194,675 wedges.  In the
bipartite projection from missing rank-six colours to fresh rank-eight
unions, the maximum matching has rank `1780/2224`.  Its canonical
Dulmage--Mendelsohn witness has 584 left rows and only 140 right resources,
so its deficiency is 444.  Every immutable-base ear completion maps into
this relaxation.  Thus even arbitrary ear length cannot repair the fixed
forest while retaining distinct rank-eight unions and legal turns.

### A hand singleton obstruction

Let

\[
 D=0x2ab=\{0,1,3,5,7,9\}.
\]

Its eleven supersets have profile `(endpoint,internal,unused)=(0,9,2)`.
The only unused supersets are

\[
 X=0x3ab,\qquad Y=0x6ab,
\]

and `X union Y=0x7ab`.  Each of `X,Y` has exactly one original-endpoint
neighbour through a seed-rank-eight-fresh edge, namely `E=0x5ab`, but

\[
 X\cup E=Y\cup E=X\cup Y=0x7ab.
\]

Therefore a length-at-most-four ear containing the central edge `XY` must
repeat the adjacent rank-eight union on at least one side; the intervening
triple has rank eight, not rank nine.  This is a one-row Hall certificate.

## 3. Exact bookkeeping for an arbitrary cut set

Let `C` be any vertex-disjoint set of seed edges and write `c=|C|`.  Terminal
and internal cuts must be distinguished.  Define

\[
 \delta(C)=|\{v:\deg_F(v)=2\text{ and }v\text{ is incident with }C\}|,
\]

the number of destroyed old turns.  Then the exact invariant counts are

\[
\begin{array}{c|c}
\text{object}&\text{count}\\ \hline
\text{retained seed edges}&10152-c\\
\text{retained-seed components}&5224+c\\
\text{new edges needed for one final path}&6758+c\\
\text{surviving old turns}&4928-\delta(C)\\
\text{new turns needed}&11981+\delta(C).
\end{array}                                      \tag{3.1}
\]

The often quoted `11981+2c` is valid only when every cut has two internal
ends.  A terminal--internal cut destroys one turn, not two.  If `a` cuts are
terminal--internal and `b` are internal--internal, with `a+b=c`, then

\[
 \delta(C)=a+2b.                                  \tag{3.2}
\]

The old vector `(4024+c,905,252,42)` is one bounded-ear scalar face, not a
property of a general reroute.  Its `336` unused--unused slots give the valid
conditional lower bound

\[
 674\le336+2c,qquad c\ge169,                     \tag{3.3}
\]

but (3.3) is not a universal cut lower bound once longer unused paths or a
different internal-slot ledger are allowed.  The exact internal-cut Rado
audit in fact closes that `c=169/336` face by deficiency 35.

## 4. A general variable-length edge--turn master

There is a cleaner exact formulation which does not guess ears or freeze
palettes before the cut choice.  Use the entire Johnson graph `J(17,7)`.

* For every Johnson edge `e={A,B}`, let `x_e` say that it belongs to the final
  tail path.  For a seed edge `f`, its cut variable is `r_f=1-x_f`.
* Every one of the 15,376 seed vertices is mandatory.  For each of the 4,072
  unused rank-seven vertices, let `y_v` indicate selection and impose
  `sum y_v=1535`.
* Let `b_v` indicate a final endpoint, with `sum b_v=2` and `b_v<=y_v`
  for unused vertices (mandatory vertices have implicit `y_v=1`).
* For every selected internal vertex `v` and every rank-nine `H` with
  `v subset H`, let `t_{v,H}` select the turn at `v`.  For a final endpoint,
  endpoint-addition variables select its single incident direction.

For a rank-seven vertex `v` and coordinate `a` outside `v`, define

\[
 g_{v,a}=\sum_{e=vw:\,a\in w\setminus v}x_e.      \tag{4.1}
\]

Rank-eight injectivity below makes `g_{v,a}` Boolean.  Link edges and turns by

\[
 g_{v,a}=s_{v,a}+\sum_{H:\,H\setminus v\ni a}t_{v,H},             \tag{4.2}
\]

where `sum_a s_{v,a}=b_v`, and impose

\[
 \sum_{H\supset v}t_{v,H}=y_v-b_v                 \tag{4.3}
\]

for unused `v`, or `1-b_v` for mandatory `v`.  Thus an internal selected
vertex has two incident edges whose two added coordinates determine one
rank-nine turn, while an endpoint has one incident edge and no turn.

The palette rows are simply

\[
 \sum_{e:\,A\cap B=D}x_e\ge1
       \quad(D\in\tbinom{[17]}6),                 \tag{4.4}
\]

\[
 \sum_{e:\,A\cup B=Q}x_e\le1
       \quad(Q\in\tbinom{[17]}8),                 \tag{4.5}
\]

and

\[
 \sum_{v\subset H}t_{v,H}\le1
       \quad(H\in\tbinom{[17]}9).                \tag{4.6}
\]

Equations (4.4)--(4.6) automatically implement dynamic release of deleted
seed colours: a retained seed edge/turn occupies its row, while a destroyed
one does not.  No separate covariance assumption is used.

Finally add lazy graphic cuts excluding every selected cycle.  The degree
equations give exactly 16,911 selected vertices, two degree-one vertices and
16,910 edges.  Acyclicity therefore makes the result one spanning path.

### Exactness

Every literal rank-seven tail path induces these variables and satisfies
(4.1)--(4.6).  Conversely, the link equations give the required degrees and
literal turn at every selected vertex; the graphic cuts make the selected
graph a single path.  Hence this is an iff encoding of the owner/lower-q1/
rank-eight/rank-nine tail gate with arbitrary cuts and arbitrary-length
reroutes.  It is not merely a relaxation of a preselected ear catalogue.

The uncompressed dimensions are 680,680 edge states and
`C(17,7) C(10,2)=875,160` turn states.  The fixed-base edge/wedge peel in
Section 2 is a much smaller projection, while a practical dynamic solver
should install cut/colour/provider rows first and generate turn and graphic
rows lazily.

## 5. The frozen `c=312` exposure certificate

The current cut-assignment optimizer reports a lexicographic optimum of 312
cuts for exposing the 380 non-all-unused no-endpoint colours.  Its literal
certificate has the degree-type split

\[
 90\text{ terminal--internal}+222\text{ internal--internal}=312, \tag{5.1}
\]

not the provisional `214/98`.  Its separate assignment occupancy is

\[
 244\text{ one-colour}+68\text{ two-colour}=312,\qquad
 244+2\cdot68=380.                                 \tag{5.2}
\]

Thus `delta(C)=90+2*222=534`.  The exact scalar ledger is

\[
\begin{array}{c|c}
\text{retained edges}&9840\\
\text{components}&5536\\
\text{new joins}&5535\\
\text{new edges}&7070\\
\text{new turns}&12515.
\end{array}                                      \tag{5.3}
\]

The bounded-ear count vector `(4336,905,252,42)` has naive turn sum 12,605;
the 90 isolated terminal vertices remove one duplicate boundary count,
giving 12,515.  The dependency-free replay certifies the 312 cuts and all
380 assignments.  It records, but does not independently prove, the CP-SAT
lower bound 312.

The fixed assignment is nevertheless physically impossible.  Its complete
dynamic local catalogue contains 670 q8/h9-legal first-neighbour options and
no zero row, but the partner graph has matching rank

\[
                         368/380.                  \tag{5.4}
\]

The canonical DM witness is `77>65`.  The q8 and h9 projections separately
have full rank 380, so the defect is specifically the shared rank-seven
partner shore.  This no-go applies to the one frozen cut/assignment
certificate, not to every 312-cut solution.

## 6. Remaining compiler gates

The exact live finite object must choose cuts, hard-colour assignments and
first-neighbour partners jointly before imposing the remaining q8/h9 and
graphic rows of Section 4.  If that succeeds, non-designated rank-six edge
occurrences still need an injective rank-five Boolean-diamond assignment;
rank-six coverage alone does not supply it.

The prefix has 7,401 length-three owner windows and the tail has 16,909
length-four owner windows.  They are not one uniform length-four row.
Cross-seam owners, upper ranks, residence, common cap, and literal replay of
a 24,313-letter word remain downstream.  No K17 upper bound follows here.
