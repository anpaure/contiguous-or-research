# The first `k=15` two-state Hall block has an exact interacting deck closure

Date: 2026-07-28

Status: exact finite positive theorem for one controller/deck circuit, together
with an all-path no-go for the distance-eight separated-UNIT architecture.
The circuit exposes one literal new singleton target but is not a Hall-29
completion: it loses eight rank-six lower colours, fourteen rank-seven lower
colours, and three required immediate-upper colours; deeper flags and common
ownership remain unchecked.

## 1. Frozen carrier and arc convention

Let

\[
 T_0,\ldots,T_{6434}\in {[15]\choose 8}
\]

be the frozen complete rank-eight Johnson path in
`scratch/k15_doubletrans_05_213_hall29.json`, and put

\[
 P_p=\bigcap_{i=\max(0,p-3)}^{\min(p,6434)}T_i
 \qquad(0\le p\le6437).
\tag{1.1}
\]

Thus the interior `P_p` have rank five and

\[
                 T_i=P_i\cup P_{i+1}\cup P_{i+2}\cup P_{i+3}.
\tag{1.2}
\]

An ambient UNIT operation is a tuple

\[
                 e=(p,x,y;s,t).
\tag{1.3}
\]

It replaces `P_p` by `P_p-{y}+{x}`.  Literal recomputation of (1.2)
changes precisely `T_s` to the old deck value `T_t`, preserves all middle
ranks and local Johnson adjacencies, and recovers the edited controller by
(1.1).  We orient its **deck arc** from the deleted value to the inserted
value, namely `s -> t`.

The full theoretical UNIT catalogue has 10,370 such operations.  Two
one-state operations are in the audited separated regime when their
controller positions differ by at least eight.  An auxiliary operation is
separated from a composite local block when its position is distance at
least eight from every controller position of that block.  At this
separation the complete dilation, middle-adjacency, and erosion dependency
collars are disjoint, so the locally verified patches compose.

The distance-eight condition is a sufficient compositional condition.  It
is not asserted to be necessary.

## 2. The exact two-commodity formulation

Suppose a verified local block changes two middle deck values and hence has
two arcs

\[
                         s_1\to t_1,\qquad s_2\to t_2.
\tag{2.1}
\]

For an ambient operation `e`, write `a(e),b(e)` for its deck tail and head
and `p(e)` for its controller position.

### Theorem 2.1 (separated two-commodity circulation)

The block (2.1) extends to an exact middle-deck permutation by separated
ambient UNIT operations if and only if, after deleting irrelevant pure
auxiliary cycles, there is a permutation `pi` of `{1,2}` and two directed
paths

\[
                         t_c\leadsto s_{\pi(c)}\qquad(c=1,2)
\tag{2.2}
\]

such that:

1. every auxiliary position is distance at least eight from the local
   block and from every other selected auxiliary position;
2. no auxiliary deck arc is used twice; and
3. after adding the two block arcs, every deck vertex has indegree and
   outdegree at most one.

Equivalently, for one `pi` there are binary variables `f_e^c` and
`y_e=f_e^1+f_e^2` satisfying, at every deck vertex `v`,

\[
 \sum_{a(e)=v}f_e^c-\sum_{b(e)=v}f_e^c
 =\mathbf1_{v=t_c}-\mathbf1_{v=s_{\pi(c)}},
\tag{2.3}
\]

\[
 y_e\le1,qquad y_e+y_f\le1
       \quad\hbox{if }|p(e)-p(f)|<8,
\tag{2.4}
\]

with `y_e=0` when `e` conflicts with the local block, and

\[
 b_{\rm out}(v)+\sum_{a(e)=v}y_e\le1,qquad
 b_{\rm in}(v)+\sum_{b(e)=v}y_e\le1.
\tag{2.5}
\]

Here `b_out(v)` and `b_in(v)` are the numbers of block arcs leaving and
entering `v`.

#### Proof

Every changed middle position deletes its old deck value and inserts one old
deck value.  Exact deck preservation is therefore equivalent to equality of
the number of selected arcs entering and leaving every deck vertex.  Under
(2.5), the block arcs and auxiliary arcs consequently form vertex-disjoint
directed cycles.  Removing the two block arcs from the cycles that contain
them leaves precisely the two paths (2.2); a cycle containing both block
arcs gives the crossed pairing.  Pure auxiliary cycles may be removed.

The source-capacity premise is literal here.  An ambient operation at
controller position `p` changes a middle source in `[p-3,p]`.  Hence
distance-eight auxiliary positions have distinct middle sources, and
separation from the local block also separates its two changed sources.
This proves the outgoing half of (2.5); exact multiplicity balance forces
the matching incoming half.

Conversely, (2.2)--(2.5) make the selected arcs and the block arcs a union
of directed cycles, hence they permute the complete middle deck exactly.
The distance-eight conditions make all auxiliary dependency collars
disjoint from one another and from the already verified composite block.
Thus simultaneous dilation is the disjoint union of the verified local
recomputations; all middle ranks, Johnson adjacencies, and maximal-erosion
identities compose.  This proves both directions.  \(\square\)

For a nonseparated collection, the advertised isolated arcs need not remain
the actual joint deck changes: overlapping four-windows can create
interaction terms.  Equations (2.3)--(2.5) remain necessary only after
simultaneous recomputation confirms that the actual changed-deck map is the
advertised arc multiset, as it is in Theorem 5.1.  In general one must impose
balance and capacity on the actual recomputed old-to-new map.  Local legality
must likewise be checked simultaneously; the last paragraph of the proof no
longer applies.

## 3. Exact two-state census

Exhausting all pairs of distinct theoretical UNIT positions at gap at most
seven, with at least one advertised Hall-service pin, gives

\[
\begin{array}{c|r}
\text{raw swap pairs}&1,011,150\\
\text{controller-Johnson legal}&30,442\\
\text{middle-rank legal}&28,379\\
\text{fully local legal}&27,838\\
\text{locally exact-deck}&0\\
\text{retaining an advertised target envelope}&59.
\end{array}
\tag{3.1}
\]

Exactly three of the 59 pass the relaxed test that both exported deck arcs
are separately reachable in the ambient UNIT graph:

\[
\begin{array}{c|c|c}
\text{controller edits }(p,+x,-y)&\text{exported arcs}&
\text{literal singleton cell}\\ \hline
(3151,12,13),(3152,11,13)&3148\to685,\ 3149\to4452&3152\\
(3266,12,6),(3267,11,6)&3263\to3120,\ 3264\to3121&3267\\
(3268,2,6),(3269,12,6)&3268\to2236,\ 3269\to2237&3268.
\end{array}
\tag{3.2}
\]

In every row, the edited rank-five controller at the displayed cell is
exactly

\[
                     6308=\{2,5,7,11,12\}.
\tag{3.3}
\]

Thus the maximal literal choice `A=P'` realizes target 6308 on that
singleton cell.  This statement concerns that one cell; it does not assert
simultaneous preservation of the other selected physical cells or their
owners.

## 4. No row has a separated all-path closure

### Theorem 4.1

None of the three rows of (3.2) satisfies Theorem 2.1.  This is an all-path
statement, not a shortest-path statement.

#### Proof for row A

Delete all ambient arcs whose controller position lies within distance seven
of 3151 or 3152.  The vertices reachable from inserted deck value 4452 are
exactly

\[
 R=\{461,1732,3153,4452,4499,4726,5100,5738,5752\}.
\tag{4.1}
\]

The only ambient arcs leaving this set before deletion are

\[
 (3153,2,12;3153,3609),\qquad
 (3156,14,4;3153,2792),
\tag{4.2}
\]

where the semicolon separates `(p,x,y)` from `(tail,head)`.  Both positions
3153 and 3156 conflict with the local block, so the allowed graph has no arc
leaving `R`.

For completeness, summing exact deck balance over `R` gives

\[
 \operatorname{out}_F(R)-\operatorname{in}_F(R)
 =\#\{i:t_i\in R\}-\#\{i:s_i\in R\}=1,
\tag{4.3}
\]

because `4452 in R` while `685,3148,3149` are outside.  The left side is at
most zero since `R` has no allowed outgoing arc.  This contradiction rules
out both pairings and paths of every length.

#### Proof for row B

The unique ambient arc entering deleted deck value 3264 is

\[
                       (3124,6,11;3121,3264).
\tag{4.4}
\]

Since the block already has one arc leaving 3264, exact deck balance and
vertex capacity force (4.4).  It balances the block arc entering 3121.
The other inserted block value 3120 must emit one auxiliary arc, but its
complete outgoing list is

\[
 (3120,0,9;3120,2325),\qquad
 (3123,11,7;3120,4788).
\tag{4.5}
\]

Both controller positions conflict with 3124.  Hence no feasible pair of
paths exists.

#### Proof for row C

Each of the two inserted values 2236 and 2237 must emit one auxiliary arc.
Their complete outgoing lists have controller positions

\[
                 \{2236,2239\},\qquad\{2237,2240\},
\tag{4.6}
\]

respectively.  Every cross-pair in (4.6) has distance at most four.  The two
required first arcs therefore conflict.  \(\square\)

## 5. The conflicts of row A are jointly legal

Theorem 4.1 is sharp with respect to its separated architecture.

### Theorem 5.1 (exact 20-state interacting circuit)

The first row of (3.2) has a nonseparated exact controller/deck completion
which retains the literal singleton target 6308.

#### Certificate

In addition to the two local edits in row A, use the following 18 ambient
operations `(p,x,y;tail,head)`:

\[
\begin{aligned}
&(688,13,0;685,3149),\\
&(4452,9,10;4452,4726),(4726,8,2;4726,5100),\\
&(5103,13,7;5100,5738),(5738,7,8;5738,461),\\
&(461,6,3;461,3153),(3156,14,4;3153,2792),\\
&(2795,3,5;2792,4096),(4096,4,12;4096,901),\\
&(901,12,7;901,6079),(6079,0,13;6079,4710),\\
&(4713,13,3;4710,3170),(3170,5,6;3170,4359),\\
&(4359,8,11;4359,1429),(1432,7,14;1429,2095),\\
&(2095,10,9;2095,3196),(3196,2,8;3196,686),\\
&(686,3,12;686,3148).
\end{aligned}
\tag{5.1}
\]

The resulting changed deck values form the single directed cycle

\[
\begin{aligned}
3148&\to685\to3149\to4452\to4726\to5100\to5738\to461\\
&\to3153\to2792\to4096\to901\to6079\to4710\to3170\\
&\to4359\to1429\to2095\to3196\to686\to3148.
\end{aligned}
\tag{5.2}
\]

#### Proof

Apply all 20 controller swaps simultaneously, then define `T'` by the four-
window union (1.2).  Direct exact recomputation gives:

1. the 20 changed controller positions are

   \[
   \begin{gathered}
   461,686,688,901,1432,2095,2795,3151,3152,3156,3170,3196,\\
   4096,4359,4452,4713,4726,5103,5738,6079;
   \end{gathered}
   \]

2. exactly the 20 middle positions in (5.2) change, and their old-to-new
   values are precisely the arcs of that cycle;
3. every `T'_i` has rank eight and every consecutive pair has symmetric
   difference two;
4. the controller ranks retain the profile `8,7,6,5,...,5,6,7,8`, every
   equal-rank consecutive pair has symmetric difference two, and every
   boundary rank change is a one-element inclusion;
5. `P'_p=intersection(T'_i:p-3<=i<=p)` at every boundary and interior
   position; and
6. `P'_{3152}=6308`.

Item 2 proves exact middle-deck preservation.  Items 3--5 prove the full
Johnson chronology, dilation, and maximal-erosion laws.  Since every
controller letter is nonempty, taking the literal source word `A'=P'`
gives `D^3A'=T'`; item 6 realizes target 6308 on singleton cell 3152.

The only distance-eight violations are the clusters `(686,688)` and
`(3151,3152,3156)`.  The simultaneous computation above, rather than the
false disjoint-collar inference, verifies both clusters.  \(\square\)

## 6. Exact shadow loss and the remaining gate

For a middle chronology `X`, put

\[
 U_1(X)=\{X_i\cup X_{i+1}:0\le i<6434\},\qquad
 L_1(X)=\{X_i\cap X_{i+1}:0\le i<6434\}.
\tag{6.1}
\]

For a controller word `Q`, also put

\[
                C_\ell(Q)=\left\{\bigcup_{j=i}^{i+\ell-1}Q_j:i\right\}
                \qquad(1\le\ell\le4),
\tag{6.2}
\]

with the natural range of starts.

### Proposition 6.1

For the circuit of Theorem 5.1,

\[
 C_1(P)\subset C_1(P'),\qquad C_1(P')\setminus C_1(P)=\{6308\},
\tag{6.3}
\]

\[
 C_2(P')\subset C_2(P),qquad
 C_2(P)\setminus C_2(P')=
 \{2488,8380,12460,13089,19152,23064,29344,31296\},
\tag{6.4}
\]

and

\[
\begin{aligned}
C_3(P)\setminus C_3(P')=\{&3000,4796,5301,7352,10992,12476,13217,15144,\\
                           &19160,23065,31280,31297,31304,31392\},
\end{aligned}
\tag{6.5}
\]

with \(C_3(P')\subset C_3(P)\) and \(C_4(P')=C_4(P)\).  At the upper adjacent
shadow,

\[
 U_1(T')\subset U_1(T),\qquad
 U_1(T)\setminus U_1(T')=\{9661,23257,31457\},
\tag{6.6}
\]

and

\[
\begin{aligned}
L_1(T)\setminus L_1(T')=\{&3000,4796,5301,7352,10992,12476,13217,15144,\\
                          &19160,23065,31280,31297,31304,31392\}.
\end{aligned}
\tag{6.7}
\]

Moreover `|U_1(T)|=5005`, `|U_1(T')|=5002`, `|L_1(T)|=6431`, and
`|L_1(T')|=6417`.

#### Proof

Evaluate the 6,434 adjacent unions and intersections before and after the
literal recomputation in Theorem 5.1, remove repetitions, and compare the
two integer-mask sets.  Do the same for every one-, two-, three-, and
four-letter controller interval.  The inclusions, cardinalities, and
complete differences are exactly (6.3)--(6.7).  The accompanying verifier
performs these set equalities literally.  \(\square\)

Because all 5,005 rank-nine colours occurred before the edit, the three
losses in (6.6) already prevent Theorem 5.1 from being a complete upper
shadow factor.  No conclusion about deeper flags can repair a missing
depth-one colour.

Thus the circuit is an exact signed shallow-palette exchange: it creates the
new rank-five singleton colour 6308 and destroys no old singleton colour,
but it loses eight rank-six lower colours, fourteen rank-seven lower colours,
and three rank-nine upper colours.  Its present palette tax is 25.

The smallest necessary positive replacement is therefore:

> **Shadow-compatible interacting-circulation gate.**  Find a simultaneous
> controller circuit containing one target-safe two-state block, with exact
> dilation, maximal erosion, Johnson chronology, and middle-deck
> permutation, which retains the advertised singleton and satisfies
> \(U_1(T'')={[15]\choose9}\).  For the current protected architecture it must
> additionally retain every required old lower colour and then pass the
> common physical-cell/owner and all-depth flag tests.

This is strictly smaller than the original compensated-controller CSP and
strictly stronger than a two-commodity reachability or deck-circulation
test.  Theorem 5.1 closes the controller/deck part for one Hall address; the
three masks in (6.6) are the first exact unresolved obstruction.

## 7. Scope audit

1. Theorem 4.1 rules out every path length, but only in the distance-eight
   separated-UNIT catalogue.  Theorem 5.1 is an explicit counterexample to
   extending that no-go to interacting patches.
2. The deck-cycle identity alone would not prove controller legality.
   Theorem 5.1 uses a fresh simultaneous dilation/erosion and adjacency
   check.
3. Realizing singleton 6308 with `A'=P'` does not preserve the 1,489 fixed
   target/cell occurrences, the six old residual cells, a trace-two owner
   assignment, or any chosen 29-address package.
4. Immediate shadows are not the full flag tower.  Here even the necessary
   immediate upper condition fails, so no deeper claim is made.
5. The census (3.1) is exhaustive only for two theoretical UNIT controller
   states at gap at most seven and at least one retained Hall-service pin.
   Non-UNIT moves, larger interacting blocks, and a different carrier are
   outside it.

## 8. Reproduction

Run

```text
python3 scratch/audit_k15_two_state_service_export.py
python3 scratch/audit_k15_position_conflict_two_commodity_cuts.py
```

The first verifier reconstructs (3.1)--(3.3).  The second reconstructs the
10,370-arc ambient graph, verifies the three all-path separating cuts,
recomputes the interacting circuit (5.1) simultaneously, and checks the
exact palette and shadow differences (6.3)--(6.7).
