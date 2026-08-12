# The tight one-to-two augmenter in the prospective `M0` state

Date: 2026-08-01  
Lane: Thread D / off-support torsion escape  
Status: exact typed lift, exact resource ledger, and exact failure of universal
all-cut expansion.  The local augmenter remains a useful primitive; no global
absorber-packing theorem is claimed.

## 0. Verdict

The physical identity in
`MATH_THEOREM_ODD_DIAMOND_TIGHT_ONE_TO_TWO_AUGMENTER_20260801.md`
is correct.  It is not, without typing, the literal Thread-D prospective
`M0` operation.

The frozen host has two anonymous copies of every physical owner.  The
prospective system instead has two **different** owner resources: a tail
corner and a head corner.  Once these roles and the residual predecessor
matching are restored, every physical tight augmenter has exactly two
strict resource-inclusion lifts.  The aligned orientation is the composition
of one protected-safe auxiliary-colour transposition and one target
insertion.  The reversed orientation is instead a bundled `2 x 2`
lower--tail crossing; it is an exact one-to-two move, but it is not one edge
of the previously defined slot-transposition graph.

Thus the aligned half of the catalogue realizes the already isolated
compound service radius two uniformly in every dimension.  Its exact
prospective resource requirement is

* one particular residual predecessor edge, not merely one free lower and
  one free owner independently; and
* one particular unused head.

The physical count with sixteen anonymous slot labels does not survive
unchanged: the strict typed supply per target is

\[
  2(m+1)m(m-2)(m-1),                                   \tag{0.1}
\]

not `16(m+1)m(m-2)(m-1)`.

There are two further role-changing orientations.  They are legal compound
slot transpositions, but they are not resource-inclusion lifts: each requires
two unused heads and releases the old head.

Finally, this local supply does **not** imply fixed-residual direct all-cut
expansion.  The exact `m=3` one-slot blocker has no applicable tight
augmenter with `Y^+=Y-y` in any of the four typed orientations, although a
different two-colour transposition closes it.  Arbitrary simultaneous
rematching of the residual bank can also escape; thus the negative statement
is about the residual-slot criterion, not unrestricted prospective
augmentation.  The tight augmenter is a genuine primitive, not by itself a
complete higher-torsion absorber bank.

## 1. The prospective state

Use the notation of the prospective oriented-diamond theorem.  An integral
partial state `(X,Y)` consists of selected oriented diamonds

\[
                    (R;L,T,V),\qquad T\to V,             \tag{1.1}
\]

and a residual inclusion matching `Y`.  Every lower and every tail resource
occurs exactly once across `X` and `Y`.  Heads occur at most once in `X`; put

\[
                         H_0={\cal O}-V(X).               \tag{1.2}
\]

Assume the selected rooted arcs form a forest and the tight pivot is a
protected subset of `X`.

For one target `R`, use the frozen notation

\[
\begin{array}{lll}
L=R-\{a,b\},&A=L+a,&B=L+b,\\
C=L+c,&L'=(L-x)+c,&D=(L-x)+a+c,\\
&&S=L+a+c.
\end{array}                                             \tag{1.3}
\]

The three physical diamonds are `AC` over `(S,L)`, `AB` over `(R,L)`,
and `CD` over `(S,L')`.

## 2. Exact strict typed lifts

### Theorem 2.1 (two prospective lifts)

There are exactly two orientations of the physical replacement which retain
both old typed owner resources and change `Y` by deleting one edge.

The first is

\[
\begin{aligned}
 f&=(S;L,A,C),& e&=(R;L,A,B),&g&=(S;L',D,C),             \tag{2.1}\\
 y&=(L',D)\in Y,&&&B&\in H_0 .                          \tag{2.2}
\end{aligned}
\]

The second is the reversed analogue

\[
\begin{aligned}
 f&=(S;L,C,A),& e&=(R;L,B,A),&g&=(S;L',C,D),             \tag{2.3}\\
 y&=(L',B)\in Y,&&&D&\in H_0 .                          \tag{2.4}
\end{aligned}
\]

If `f in X` and the displayed conditions hold, then

\[
                X^+=X-f+e+g,\qquad Y^+=Y-y             \tag{2.5}
\]

satisfies every upper, lower, tail, and head partition row.  It fills `R`,
retains the auxiliary colour `S`, and preserves every other selected
diamond literally.

#### Proof

For (2.1), the old typed resources are lower `L`, tail `A`, and head `C`.
The two new diamonds retain all three and add lower `L'`, tail `D`, and head
`B`.  The residual edge `L'->D` supplies exactly the new lower--tail pair,
while `B in H_0` supplies the new head.  Hence (2.5) preserves every row.
The proof of (2.3) is identical with old tail/head `C,A` and new tail/head
`B,D`.  All four physical owners are distinct by the frozen theorem, so no
hidden collision occurs.

For necessity, suppose the old tail is `A`.  In a one-residual-edge lift it
must remain among the two new tails; only the `AB` diamond contains `A`, so
it must be oriented `A->B`.  Retaining the old head `C` then forces `CD` to
be `D->C`, giving (2.1).  If the old tail is `C`, the symmetric argument
forces (2.3).  \(\square\)

### Corollary 2.2 (aligned state-graph interpretation)

The lift (2.1) is a slot transposition followed by a one-slot insertion.
First reroute

\[
       (S;L,A,C)\longmapsto(S;L',D,C),                  \tag{2.6}
\]

which consumes `(L',D)` and releases `(L,A)`.  Then insert

\[
                         (R;L,A,B).                     \tag{2.7}
\]

Thus an applicable lift of type (2.1) has `r_P=1` and exact compound service
cost `1+r_P=2`.  The protected pivot is preserved whenever `f` is not
protected.

The reversed lift (2.3) is different.  Before the move, the lower--tail
pairs represented by the selected and residual columns are `(L,C)` and
`(L',B)`; afterwards they are `(L,B)` and `(L',C)`.  It therefore performs
a crossed `2 x 2` reassociation of the lower and tail resources.  The whole
one-to-two replacement is exact by Theorem 2.1, but it need not factor
through one application of slot transposition (4.4) in the earlier
residual-slot note.

### Corollary 2.3 (typed count)

The physical parameter tuple `(a,b,c,x)` has

\[
                    (m+1)m(m-2)(m-1)                   \tag{2.8}
\]

choices and is recoverable exactly as in the frozen theorem.  Theorem 2.1
gives two strict oriented lifts per tuple, proving (0.1).

The factor `16` in the frozen count labels four anonymous physical-owner
copies.  Those labels cannot be identified with the Thread-D tail/head
roles: only the two orientations in Theorem 2.1 retain the old typed
resources.

## 3. The two role-changing lifts

If one allows a bundled typed-resource reassociation rather than literal
resource inclusion, two additional predecessor-conserving orientations
exist:

\[
\begin{array}{c|c|c|c}
f&e&g&\hbox{required state}\ \hline
A\to C&A\to B&C\to D&(L',C)\in Y,\ B,D\in H_0,\\
C\to A&A\to B&C\to D&(L',A)\in Y,\ B,D\in H_0.
\end{array}                                             \tag{3.1}
\]

In the first row, head `C` is released and immediately changes role to a
tail; in the second, head `A` does so.  The tail sets are still conserved
with the displayed residual edge, but the typed vertex set of the old edge
is not contained in that of the new pair.  These are valid radius-two
compound moves, and they bring the total predecessor-conserving oriented
menu to four per physical tuple.  They must not be counted as strict lifts
of the anonymous-slot containment assertion.

These four cases are exhaustive: if the old tail is `A`, tail conservation
forces the new `AB` tail to be `A`, and the residual tail is either `C` or
`D`; if the old tail is `C`, it forces the new `CD` tail to be `C`, and the
residual tail is either `A` or `B`.

## 4. Graphic ledger

All four typed cases replace the underlying edge `AC` by `AB,CD`.  If the
old rooted support is a forest, delete `AC`.  The move is graphically legal
iff `AB` and `CD`, added in either order, join distinct current components.
Tail/head injectivity already gives directed indegree and outdegree at most
one; the two union--find tests are the remaining exact graphic guard.

Consequently the augmenter does not automatically preserve the rooted
forest, but graphic feasibility is a constant-size local test.  No palette
or residual-matching resource is missing from the ledger above.

## 5. The exact direct-expansion system

For a missing-colour set `D_0`, form a catalogue whose strict columns are
the applicable instances of (2.1) and (2.3).  A simultaneous direct packet
must be independent by

1. target colour `R`;
2. selected auxiliary switch `f`;
3. residual predecessor edge `y`;
4. newly consumed head; and
5. the bundled forest-exchange condition.

Thus even the strict augmenter packet is a four-partite matching problem
with a bundled forest-exchange constraint.  Write `nu_tight(D')` for the
maximum size of a set of columns, restricted to target colours in
`D' subseteq D_0`, which is injective in the first four resources and for
which deleting all selected switch arcs and adding all paired replacement
arcs leaves a linear forest.  The exact robust all-cut condition is

\[
                         \nu_{\rm tight}(D')=|D'|
                    \qquad(D'\subseteq D_0).             \tag{5.1}
\]

The bundled forest family is not asserted to be a matroid: each column
deletes one old edge and adds two linked new edges.  The projections

\[
 |N_f(D')|\ge|D'|,\quad |N_Y(D')|\ge|D'|,
 \quad |N_{H_0}(D')|\ge|D'|                              \tag{5.2}
\]

are necessary but not sufficient.  The raw polynomial menu count is taken
before imposing `f in X`, `y in Y`, head availability, and the graphic
guard, so it proves none of (5.1)--(5.2).

Role-changing columns from Section 3 may enlarge an alternating state
graph, but they release a head while consuming two others.  They are not
static columns of the direct five-resource system.

## 6. Exact failure of universal all-cut expansion

Use the literal `m=3` state from Proposition 6.1 of the Thread-D residual-
slot note.  It omits `R=1234`, selects

\[
\begin{array}{c|c|c|c}
2345&34&234&345\\
1345&14&134&145\\
1245&12&124&125\\
1235&23&123&235,
\end{array}                                             \tag{6.1}
\]

and has the exact residual matching

\[
13\to135,\ 15\to125,\ 24\to245,\ 25\to235,
\ 35\to345,\ 45\to145.                                \tag{6.2}
\]

Exhausting all `24` physical parameter tuples through `R` and all four
typed orientations gives no applicable tight augmenter which changes the
residual matching only by deleting its consumed edge.  Therefore, for the
fixed-residual direct rank,

\[
                       \nu_{\rm tight}(\{1234\})=0.      \tag{6.3}
\]

This is stronger than failure of a large-set estimate: the singleton cut
already fails.  Nevertheless the different transposition

\[
 (2345;34,234,345)\mapsto(2345;24,245,234)              \tag{6.4}
\]

followed by insertion `(1234;34,234,134)` closes the defect.  Hence the
state has compound service radius two, but that service is outside the
tight family.

There is also no unrestricted prospective obstruction here.  Delete
`(2345;34,234,345)` and insert

\[
 (1234;34,234,134),\qquad (2345;35,235,345).           \tag{6.5}
\]

Together with the other three rows of (6.1), these diamonds admit the
residual perfect matching

\[
 13\to135,\quad15\to145,\quad24\to245,\quad
 25\to125,\quad45\to345.                              \tag{6.6}
\]

Thus an arbitrary residual rematch realizes the same physical tight
replacement even though the required edge `35->235` is absent from the old
`Y`.  Equations (6.3)--(6.4) refute only state-preserving direct expansion;
they leave a joint tight-augmenter plus residual-Hall theorem fully open.

This proves that Theorem (0.1) cannot by itself replace the higher-torsion
absorber criterion or imply fixed-residual all-cut expansion.  Its correct
use is as one explicit, dimension-uniform packet family inside a larger
off-support alternating catalogue or a simultaneous residual-rematching
model.

## 7. Surviving theorem target

After quarantining the isolated-edge order-three bank and retaining the
tight pivot literally, a bounded-total theorem would follow from a state
whose missing-colour shore has full feasible-packet rank in the **union** of

* the strict tight columns of Section 2;
* the role-changing tight columns of Section 3;
* the general protected slot transpositions; and
* the contracted graphic resource.

The local tight count supplies abundant candidate columns but no cut
inequality for that union.  The exact missing assertion remains an
off-support alternating-expansion theorem with `O(1)` exported boundary,
not a consequence of anonymous owner-capacity slack.

## 8. Audit

The symbolic ledger in Sections 2--5 uses only the displayed Boolean set
identities.  The finite singleton-cut statement is replayed by

* `scratch/audit_threadD_tight_one_to_two_typed_lift_20260801.py`;
* `scratch/threadD_tight_one_to_two_typed_lift_20260801.audit.json`.
