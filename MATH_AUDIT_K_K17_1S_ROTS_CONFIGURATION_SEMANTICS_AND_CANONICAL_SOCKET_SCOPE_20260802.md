# K17 `1S-ROTS` configuration semantics and canonical-socket scope

**Date:** 2026-08-02  
**Status:** proof-safe semantic audit and exact scoped obstruction.  This note
does not report a run of the joint master.  It separates the canonical
three-level address model from the deliberately relaxed nine-address launch
projection, and it records the activation conditions required before a relay
column may enter either model.

## 1. Inputs independently authenticated

The launch specification is

```text
MATH_AUDIT_K_K17_RECOUPLED_ROTS_ONE_SHORT_PROJECTION_LAUNCH_SPEC_20260802.md
SHA-256 4fba3434264ddf075050113383af3e9883cd66829cca67fe76571308d2078d07
```

The exact three-level chain theorem is

```text
MATH_THEOREM_K17_THREE_LEVEL_NORMAL_CHAINIZATION_20260802.md
SHA-256 1f285da227549171997362454cf5039ae690cc3f8af5f82033cc2406e2e8d9a4
```

The independent canonical interval/state census is bound to payload table
`029d3be5...`:

```text
source
8869cfb812a56567ef2b47c55d1ad5b7a29c00963daad88b4ca38682401832a9

audit JSON
833161e9c666473cd2f7b1d1a4022756d3382f70e9ee0955b41b2457c8b3cab5

short-socket summary
4749d627cb167caa8820e5c0dc584af7c8ce6bb456566d112a117968e76ae30d

payload table
029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1
```

The authenticated ordinary recoupling seed `seed4015`, itself stronger than
the older deficit-89 launch checkpoint, had:

```text
table       7568c9ac0e7adb8d5694ad3ed334692b9474f0b186346d6dd4b885abe9dacb7b
reroutes    c2672cea075337cc430d592a9b435e85da7bc3817b843b5936c7d3f3f8a4edd0
projection  2cd69b54c1f40d89fccf7d55bdc1606cd653e559179165735949eae7c8102ee7
Hall shore  3269191d22bcf637d1677ced8d997292af017d2da2e860a01ddde0f5fa9ef097
static replay
            ca939e70282d84b1d17feb03132748ea9699eebe49eb29b28812a54d2c6114c3
```

Its relaxed union projection was `16841/16898`, deficiency `57`, with `45`
zero hard heads.  A first independently replayed relay improved the projection
to deficiency `55`; forty-seven further sequential relays then reached the
following exact fixed table:

```text
round047 table
95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735

relay lineage
0dec98167ab23b734a073efbdafe2477c87fb5408348dcbfbfa7606a6da02bd3

independent static table audit
beac8d52b6ecf2098c05b1a9131beb605a99338a35621821ac2f000e523022f4

independent relaxed projection replay
2b79c35507d07be6c1fbb1503ceff0701ebf11184230b030bc3bfec8f761361a

independent lineage verifier / replay
3ae44cfa3d64cc05f548aab020c537157945e4f1c3f98961066169e9d6d83c61
c2bda5e553fbf05e2a4d3c5610a2618da20e3280e3040c0f59f75e4a13e1d13d
```

The table has exact target partition, owner/root bijections and histogram
`(0,7395,16915)`.  Its relaxed union supplier projection is perfect:
`16898/16898`, zero `0`.  The lineage audit reconstructs all forty-seven
post-first-relay tables exactly, touches `93` distinct rows, and binds the
final table.  Thus there are forty-eight accepted exchanges from `seed4015`
when the separately replayed first relay is included.

This closes only the relaxed **union supplier projection** on one static
table.  Section 5.2 proves that the same table is very far from a one-short
common-state configuration.

## 2. The physical address menu is `4/3/2`, not `4/9`

The compressed levels are

\[
 P_0=\bigcup_{r=1}^{6}{[17]\choose r},\qquad
 P_1={[17]\choose7},\qquad
 P_2={[17]\choose8}.
\]

A literal three-cell realization places a `P0` target on one cell, a `P1`
target on one adjacent pair, and a `P2` target on all three cells.  Therefore
the canonical menus are:

* `P0-P1-P2`: four flags `12/1,12/2,23/2,23/3`;
* `P0-P2`: three choices for the singleton cell;
* `P1-P2`: two choices for the adjacent pair.

The nine strict nested pairs of arbitrary nonempty contiguous intervals are
a genuine relaxation: they also permit the named `P0`/`P1` target to occupy
the wrong compressed depth.  They are useful for a fail-fast projection, but
a SAT certificate in that model is not a canonical three-level chronology.

In every minimum-long recoupled table the exact short census is

\[
 4862\text{ rows of type }P_0\!\to P_2,\qquad
 2533\text{ rows of type }P_1\!\to P_2.
\]

Indeed the `4862` rows comprise `3114` old `P0-P2` rows plus `1748`
converted free rows; the `2533` rows comprise `785` old `P1-P2` rows plus
`1748` shortened donors.  Thus a fixed physical table has

\[
 4(16915)+3(4862)+2(2533)=\boxed{87312}
\]

address literals, not `134215`.

For a joint, factorized master before recoupling is selected, the address
variable count is

\[
 18646(4+2)+17\cdot4+3114\cdot3+785\cdot2+1748\cdot3
 =\boxed{128100}.                                      \tag{2.1}
\]

This is in addition to the `401754` recoupling bits.  An explicit
configuration linearization `w_(f,d,q)=x_(f,d) AND z_(f,q)` would add
`3*401754=1205262` variables.  It is unnecessary if every arc/hyperarc
directly implies both `x_(f,d)` and `z_(f,q)`.

For comparison, the relaxed joint model has

\[
 18646(4+9)+17\cdot4+3899\cdot9+1748\cdot9
 =\boxed{293289}
\]

factorized address variables, or `9*401754=3615786` additional explicit
free-row `(f,d,q)` configurations if that product is linearized.  Consequently
the launch specification's fixed-table count must not be used as a resource
estimate for the joint master.  In both models the direct-record count is
`|C_LL|` and the common-state socket count is `|C_S|`; neither has been
authenticated for a variable recoupling and no memory estimate may replace
their fail-closed census.

The completed fixed-round047 fail-fast census gives the concrete relaxed
resource upper bound

```text
address variables             134215
direct long-state arcs          42490
socket hyperarcs                 2188
exactly-one rows                65535
exactly-one incidences         225759
Sinz auxiliaries, upper bound  160224
CNF variables, upper bound     339117
CNF clauses, upper bound       637751
raw bytes at 32/row, upper      20408032
```

Its size ledger has SHA-256
`5305db1627ef5348c676b92be5befe8fc0cc019ecacf277dfc830d4e47e16cbc`.
No fixed-table SAT run is warranted: Section 5.2 finds `5969` empty socket
rows before emission.  These numbers do not estimate the variable
`x+p`/relay outer master.

## 3. Exact dynamic row identities

Let `F` be the `1748` original singleton rows and `D` the `18646` eligible
hard donors.  For `fd` in the `401754`-edge containment graph, selecting
`x_(f,d)` changes exactly

\[
 f:(R_f)\mapsto(B_d,R_f),\qquad
 d:(B_d,M_d,R_d)\mapsto(M_d,R_d).                    \tag{3.1}
\]

Put `u_d=sum_f x_(f,d)`.  A proof-safe factorization uses

\[
\begin{aligned}
 &\sum_d x_{fd}=1,\quad \sum_f x_{fd}\le1,\\
 &\sum_{a=0}^{3}z^L_{d,a}=1-u_d,\qquad
   \sum_{q=0}^{1}z^S_{d,q}=u_d,\\
 &\sum_{q=0}^{2}z^F_{f,q}=1.
\end{aligned}                                        \tag{3.2}
\]

Every record using the dynamic free row must also imply its actual donor
choice `x_(f,d)`: its bottom target is `B_d`, so free rows with different
donors are different literal states even when their abstract address index is
the same.  Every long record incident with donor `d` implies `u_d=0`; every
donor-short record implies `u_d=1`.

The `17` rank-one-bottom long rows are fixed long rows.  They were omitted
only from the old **hard-head Hall diagnostic**.  A cycle-cover master must
give all

\[
                   \boxed{16915}
\]

long roles one incoming and one outgoing contracted arc, including these
seventeen rows.  Using `16898` degree rows would not be a `1S-ROTS` cycle
cover.

### 3.1 Exact static `x+p` normal form, and its missing sequential row

Let `H` be the `18646` original hard donors.  Choose the ordinary donor
injection

\[
 x:F\longrightarrow D\subset H,\qquad |F|=|D|=1748,
 \quad B_{x(F)}\subset R_F,                         \tag{3.3}
\]

and let `S` be the `1748` hard donors that are short in the final table.
After the `B_D` tokens have been sent to the free rows, the exact remaining
static choice is a perfect matching

\[
 p:H\setminus D\longrightarrow H\setminus S,
 \qquad B_A\subset M_{p(A)}.                       \tag{3.4}
\]

This is **equivalent** to a static target-exact recoupled table.  Given
`(x,p)`, put

* `(B_D,R_F)` on free row `F` when `x(F)=D`;
* `(M_v,R_v)` on every `v in S`;
* `(B_A,M_v,R_v)` on `v notin S` when `p(A)=v`;
* leave all old short rows and all 17 soft long rows unchanged.

Every original bottom token occurs once by the two disjoint domains `D` and
`H\D`; every final hard long slot receives one bottom by bijectivity of `p`.
The containment rows make every chain strict.  Conversely, the bottom of
each final hard long row uniquely identifies its original donor `A`, thereby
recovering `p`; the bottoms placed on the free rows recover `x`.  Hence this
construction preserves the full target partition and forces

\[
 3899+1748+1748=7395\text{ short rows},\qquad
 18646-1748+17=16915\text{ long rows}.              \tag{3.5}
\]

The equivalent transfer graph has edges `D->F` and, for
`p(A)=v != A`, edges `A->v`.  A fixed point `p(A)=A` is an unchanged donor,
not a physical relay edge.  Deleting fixed points gives exactly

\[
 \deg^-(v),\deg^+(v)\le1,qquad \deg^+(v)\ge\deg^-(v),
 \qquad \deg^-(F)=1.                               \tag{3.6}
\]

Equations (3.6) alone do **not** imply rooted paths.  The literal candidate
menu contains the mutual pair

\[
 0\longrightarrow495\longrightarrow0,qquad
 B_0=63\subset M_{495}=4159,quad
 B_{495}=7\subset M_0=127.                         \tag{3.7}
\]

That two-cycle is a legal static permutation of bottom tokens.  It has no
sequential ordinary-plus-relay provenance: no vertex of the cycle is the
initial short donor on which the first relay can act.  Therefore an outer
master advertised as the closure of sequential relays needs the additional
exact row

\[
 \sum_{\substack{A,v\in C\\A\ne v}}p_{Av}\le |C|-1
 \quad\text{for every nonempty }C\subseteq H,       \tag{3.8}
\]

or an equivalent topological-order formulation.  Fixed points are omitted
from (3.8).  Under (3.8), every nonfixed component reaches a donor in `D`
and then its free sink.  A path

\[
 s\to v_1\to\cdots\to d\to F
\]

is realized sequentially by the ordinary move `d->F`, followed by relays in
reverse path order.  Thus (3.8) is precisely the extra distinction between
static simultaneous bottom permutation and sequential relay legality.

The round047 table was independently reconstructed in both forms.  Its exact
statistics are

```text
candidate donor arcs excluding self  2110837
candidate free arcs                    401754
rooted paths                             1748
internal donors                            48
isolated/fixed donors                    16850
maximum donor edges in one path              3
|D intersect S|                          1701
nontrivial p cycles                          0
```

The `48` nonfixed `p` arcs equal the `48` replayed relay steps.  In particular,
row `520` is internal on the exact path

\[
 29\longrightarrow520\longrightarrow2117\longrightarrow F_{15856},
\]

carrying original bottoms `158,4174,330`.  The materialized rows are
`29:(446,958)`, `520:(158,4318,4574)`,
`2117:(4174,12622,12638)`, and `15856:(330,79178)`.

```text
independent donor-path/x+p source
e3839337d6eb5ab194d269bf1db863e4d8766a758b62d8dd17e2a5152477abc7

independent donor-path/x+p audit
daec0a1de6c3b2ef6043c2c8afdddb54b403b30bc8a5a266d0958b2493516028

original table / ordinary reroutes / full 48-step ancestry
db960ce5b51e0fdea7b048d35d48ca737096b16ee73a20df873beb0517e5f185
c2672cea075337cc430d592a9b435e85da7bc3817b843b5936c7d3f3f8a4edd0
3147322549ebb532ce863ff251eec780e8a81fe3e3db88c7bf003342995267e5
```

### 3.2 One augmented perfect matching is the same static problem

There is an exact one-matching formulation of (3.3)--(3.4).  Its left shore
is the disjoint union of the `18646` real bottom tokens `H` and a set
`Delta` of `1748` identical dummy tokens.  Its right shore is the disjoint
union of the `1748` free slots `F` and the `18646` hard-donor slots `H`.
The edge sets are

\[
\begin{array}{rcl}
 A\in H&\longrightarrow&F \quad\Longleftrightarrow\quad B_A\subset R_F,\\
 A\in H&\longrightarrow&v\in H\quad\Longleftrightarrow\quad B_A\subset M_v,\\
 \delta\in\Delta&\longrightarrow&v\in H \quad\text{for every }\delta,v,
\end{array}                                           \tag{3.9}
\]

and there are no dummy-to-free edges.

Every perfect matching of (3.9) induces `(x,p)` uniquely up to dummy labels.
Indeed, all free slots must be matched to real tokens; those tokens form `D`
and recover `x`.  The hard slots matched to dummies form `S`.  The remaining
real-to-hard edges are exactly the perfect matching
`p:H\D -> H\S`.  Conversely, `(x,p)` plus an arbitrary bijection
`Delta -> S` is a perfect matching of (3.9).  Thus the labelled augmented
matching fibre over one static table has exactly `1748!` dummy permutations.

The dummy quotient is simpler: match all `18646` real tokens into
`F union H`, saturating every real token and every free slot, with right-hard
capacity one.  Exactly `16898` hard slots are then occupied and the other
`1748` slots are `S`; a dummy completion is automatic.  This quotient removes
the entire dummy-label symmetry without changing the static feasible set.

For K17 the exact graph sizes are

```text
left and right shore size          20394
real-to-free edges                401754
real-to-hard edges               2129483
dummy-to-hard edges             32593208
labelled augmented total        35124445
```

The real-to-hard count includes all `18646` identity edges.  These are the
fixed points of `p` and must again be treated as retained donors rather than
one-edge relay cycles.

The node-edge incidence matrix of (3.9) is bipartite and totally unimodular.
Hence the **static** fractional assignment polytope, every face obtained by
fixing protected assignment edges, and the dummy-quotiented rectangular
matching all have integral vertices.  This TU statement ends there.  It does
not impose the sequential acyclicity row (3.8), one common incoming/outgoing
address, a five-cell short socket, selected chronology topology, residence,
upper decks, or compiler constraints.

The symmetric difference of two labelled augmented perfect matchings is an
even alternating-cycle decomposition.  Cycles involving only dummy labels
are gauge moves with no table effect.  Real-to-hard alternating cycles change
`p`; relative to the identity matching, a nontrivial `p` cycle is exactly
such an alternating circuit.  It preserves the static target partition but
can violate sequential relay provenance.  This is not hypothetical on the
warm table: rows `0` and `495` are both fixed, lie outside `D union S`, and
the swap

\[
 p(0)=495,\qquad p(495)=0                         \tag{3.10}
\]

is compatible by (3.7).  Replacing their two identity edges by (3.10)
produces another perfect augmented matching and a valid static table with a
donor two-cycle.  Therefore neither perfect matching nor TU makes the relay
chronology sequential; (3.8) remains load-bearing whenever sequential
provenance is required.

The round047 augmented matching has `1748` real-to-free edges, `1748` dummy
slots, `16850` fixed real-to-hard edges and `48` nonfixed real-to-hard edges.
It is an exact static warm start, but Section 5.2 shows that its induced table
has `5969` short roles with no relaxed common socket.  Thus augmented matching
solves the static allocation row and no part of the `1S` configuration gate.

The emitted dummy-quotiented warm selection was independently decoded from
its variable numbers, checked against all `39040` exact-one rows, and
materialized back to round047 byte-for-byte:

```text
builder / size JSON / warm selection
f2cf43c7e44d16e15ee6449587bc2e4a1c0cc8a37f6351c5726e8ce4e0867324
f1600a3e65fa3597f60affc919bea79e8e2bfe8cdd52bd850f21a0658f841cad
d56126ff3d1d8fde67dd6a6446c0974ded36921993fd093edc94a279c0e5a5b9

independent selection decoder / audit
2647112cdb5bb7f7f76a4579e81dcca35b40ab9361dda3f338bf35fca8ed939e
1786192390363b754a8f5477844892f36bf80549787d3cc283244b5ee5cc6d61
```

The quotient has `2549883` primary variables, `39040` exactly-one rows and
`5081120` incidences.  A direct Sinz encoding would have `7591963` variables
and `15126240` clauses before any configuration rows.  This is a resource
audit, not a recommendation to emit that static formula before the socket
pruning below.

### 3.3 Exact global dummy-socket menu and safe deletion

For a real-to-hard placement `A->j`, write

\[
 L(A,j)=(B_A,M_j,R_j).
\]

Let `Lstar` be the set of every possible long boundary state: all such
dynamic placements, together with the 17 fixed rank-one-bottom long rows.
A dynamic state has outer support `{y_Aj}`; a fixed soft-long state has empty
outer support.  Including these 17 rows is essential: a valid short socket
may use one of them as predecessor or successor.

If hard slot `v` is occupied by a dummy, its short row is

\[
 S(v)=(M_v,R_v).
\]

Fix either the relaxed-nine short address menu or the canonical physical
menu; they must not be mixed.  Let `Phi` be the exact coordinatewise
five-cell predicate used in Section 5.2, including both owner insertions,
both cover equations, nonempty cells, a common short address and the declared
socket direction `b<=a`.

The **global socket menu** of candidate dummy slot `v` is

\[
\begin{split}
 \mathcal G_v=\{&(\ell,a;q;r,b):
 \ell,r\in\mathcal L^*,\ \operatorname{slot}(\ell),
 \operatorname{slot}(r)\ne v,\\
 &P(\ell)\cup P(r)\text{ is a partial matching},\ b\le a,\\
 &\Phi(\ell,a;S(v),q;r,b)=1\}.
                                                               \tag{3.11}
\end{split}
\]

When the two boundary states use the same long role, they must be the same
literal state and the one-address row forces `a=b`; otherwise their physical
roles are distinct.  On two dynamic states, partial-matching compatibility
means that two distinct placements share neither token nor hard slot.  Fixed
soft-long states consume no outer placement.  This convention includes a
same-long predecessor/successor only when it is a genuine single long state.

### Theorem 3.3 (safe zero-menu deletion)

If `G_v` is empty, no exact `1S` configuration can select hard slot `v` as a
dummy/short slot.  Hence `s_v=0` is a valid outer-master unit, equivalently
all labelled dummy-to-`v` edges may be deleted.

**Proof.**  In any exact configuration with `s_v=1`, the selected predecessor
and successor long roles are occupied by compatible real tokens in the outer
matching.  Their selected addresses and the selected short address realize
one common five-cell word, and therefore form an element of `G_v`, a
contradiction.  This proof uses the union over **all** legal real-token
placements, not a fixed-table neighborhood.  \(\square\)

The converse is false.  Put

\[
 d_v=|\mathcal G_v|,
 \qquad
 d_v(Y)=|\{g\in\mathcal G_v:P(g)\subseteq Y\}|,       \tag{3.12}
\]

where `Y` is a selected outer matching and `P(g)` is the set of one or two
real-to-hard placement edges required by `g`.  The global number `d_v` is an
**optimistic degree**.  Even `d_v>0` may rely on a token placement excluded by
`Y`, or several selected dummy slots may require competing tokens, slots,
flags, or contracted degrees.  The fixed-table number `d_v(Y)` is the exact
common-state socket count for that table, but a physical witness is selected
only after one menu element participates in equations (4.1)--(4.2).

Thus a min-cost augmented matching may safely assign infinite cost to every
zero-menu dummy edge and may use any finite robustness weight derived from
`d_v` for search order.  Such a weighted bipartite matching remains TU, but
the finite weights are pricing only.  They do not certify `1S`.

There is also an exact greedy formulation for costs that depend only on the
identity of the dummy slot.  On the right-host ground set `F union H`, let
`T` be the transversal matroid in which a host set is independent iff it can
be matched injectively to the `18646` real bottom tokens.  The mandatory free
set `F` is independent.  Therefore the admissible real-occupied hard-slot
sets `I` are exactly the rank-`16898` bases of the contraction `T/F`, and

\[
 S=H\setminus I,\qquad
 \min\sum_{v\in S}c_v
 =\sum_{v\in H}c_v-\max\sum_{v\in I}c_v.            \tag{3.13}
\]

Matroid greedy, ordering hard slots by decreasing `c_v` and testing each
insertion by an exact augmenting path, solves (3.13).  A proved zero-menu set
is handled by first contracting those hard slots as forced-real elements;
failure of that contraction is an exact Hall obstruction to avoiding all of
them.  This proves optimality for the declared **slot costs**.  It does not
choose which real-token placement realizes the eventual socket, and two
outer matchings with the same real-occupied slot set have the same objective.
Thus global-degree costs remain optimistic even though their weighted basis
optimization is exact.

### Theorem 3.4 (exact Hall test for a restricted dummy bank)

Let `Acal` be a declared set of admissible hard slots for the `1748` dummy
tokens.  For a real-token set `X subset H`, let `N_F(X)` and `N_H(X)` be its
neighbors on the free and hard-slot right shores.  The augmented matching
with every dummy adjacent exactly to `Acal` has a perfect matching if and only
if, for every `X subset H`,

\[
 |N_F(X)|+|N_H(X)|\ge |X|,                          \tag{3.14a}
\]

and

\[
 |N_F(X)|+|N_H(X)\cup\mathcal A|
 \ge |X|+1748.                                     \tag{3.14b}
\]

In particular, (3.14b) at `X=emptyset` says
`|Acal|>=1748`.

**Proof.**  Apply Hall to a left subset `X union Y`, where `X` consists of
real tokens and `Y` of dummies.  If `Y` is empty its neighborhood gives
(3.14a).  If `Y` is nonempty, every dummy has the same neighborhood `Acal`,
so

\[
 N(X\cup Y)=N_F(X)\ \dot\cup\ (N_H(X)\cup\mathcal A).
\]

For fixed `X` the largest right-hand side of Hall occurs when `Y` contains
all `1748` dummies, giving (3.14b).  These two cases exhaust all left subsets,
so the inequalities are also sufficient.  \(\square\)

This theorem has an exact compressed flow realization: give every real token
unit supply, give one dummy-bank node supply `1748`, connect that bank node
with unit-capacity arcs to `Acal`, retain the real-to-free and real-to-hard
edges, and put unit capacity on every right slot.  A flow of value `20394`
is equivalent to the augmented perfect matching; a deficient min cut is an
exact violated family in (3.14a) or (3.14b).  Additive dummy-slot costs go on
the bank-to-slot arcs, so min-cost max-flow is exact.  Equivalently, force
`H\Acal` real in the contracted transversal matroid and apply the weighted
basis rule (3.13) on the remaining slots.

If `Acal={v:G_v is nonempty}` is obtained from the **complete** menu (3.11),
failure of (3.14) is an exact necessary no-go for `1S`: every valid dynamic
short slot would have to lie in `Acal`.  Passing (3.14) proves only that a
static outer matching can avoid all globally socketless dummy slots.  It does
not select compatible elements of the menus, and is not sufficient for
common-state sockets.  If `Acal` came from an approximate or fixed-table
degree census, even that global no-go interpretation is invalid; the Hall
theorem then applies only to the explicitly declared restricted bank.

An exact integrated linearization uses one activation bit `r_g` per retained
menu element and the rows

\[
 \sum_{g\in\mathcal G_v}r_g=s_v,
 \qquad r_g\le y_e\quad(e\in P(g)),                 \tag{3.15}
\]

together with the long flag and directed-degree equations (4.1)--(4.2).
This is a placement-labelled hypergraph extension of matching, not an
ordinary weighted-matching face and not covered by the TU claim of Section
3.2.  Logic-based Benders is equivalent: choose the outer matching, compute
all `G_v(Y)` and the full fixed-table configuration oracle, then learn only
cuts pulled back through the placement supports.

The exact menu can be indexed without scanning all donor pairs:

1. For each hard slot `j`, enumerate the at most `128` subsets of its
   seven-set `M_j` and look up the unique bottom token.  This generates all
   `2129483` real-to-hard placements exactly.
2. Add the 17 fixed soft-long states, then for each `(v,q)` build exact
   four-cell incoming and outgoing records from the resulting boundary-state
   catalogue.
3. Join only records with the same `(v,q)` and `b<=a`, then run the exact
   five-cell predicate.  Every five-cell witness appears in both marginal
   lists, so this loses nothing.
4. Identical marginals may be grouped by the collision-free boundary profile
   consisting of their three lower masks and three upper masks, plus the
   relevant owner insertion.  Retain the underlying placement-edge list for
   activation.  More aggressive memoization may key the combined
   coordinate-pattern histogram, but coordinate-labelled resources must not
   be quotient-identified merely because their histograms agree.

The maximal-box test is constant-time on 17-bit masks and exact by the cover
argument in Section 5.2; the independent 32-pattern coordinate DP remains the
replay oracle.

Finally, `G_v` addresses only the `1748` dynamic donor-short roles.  A full
joint master also needs menus for the `1748` free short rows, whose lower
target depends on the selected real-to-free edge, and for the `3899` old
short rows.  Deleting zero-menu dummy edges cannot by itself close those
other `5647` socket equations.

## 4. Configuration equations

For a fixed selected table let

* `C_LL` contain every accepted flag-labelled direct record
  `(j,a)->(i,b)`;
* `C_S` contain every accepted common-state record
  `(j,a)->(s,q)->(i,b)`.

The short record belongs to `C_S` only when one literal five-cell merge
simultaneously realizes both transitions and the short cover equation.  The
intersection of an incoming mask and an outgoing mask is not sufficient.

With direct variables `e_c`, socket variables `r_c`, and long flag variables
`z_(v,a)`, the clean shared-flag equations are

\[
\begin{aligned}
 \sum_{c\in C_{LL}:\operatorname{tail}(c)=(v,a)}e_c
 +\sum_{c\in C_S:\operatorname{tail}(c)=(v,a)}r_c &=z_{v,a},\\
 \sum_{c\in C_{LL}:\operatorname{head}(c)=(v,a)}e_c
 +\sum_{c\in C_S:\operatorname{head}(c)=(v,a)}r_c &=z_{v,a}.       \tag{4.1}
\end{aligned}
\]

For every short address configuration,

\[
       \sum_{c\in C_S:\operatorname{short}(c)=(s,q)}r_c=z_{s,q}.   \tag{4.2}
\]

Together with the conditional one-hot equations, (4.1) forces the same long
flag on the incoming and outgoing sides; implications to a one-hot flag are
equivalent only if both degree equalities remain present.  Equation (4.2)
forces one common physical short state rather than two unrelated marginal
states.

`1S` means one short role per socket, not one global socket.  Hence every
solution selects exactly

\[
 7395\text{ socket hyperarcs},\qquad16915-7395=9520
 \text{ direct long arcs}.                            \tag{4.3}
\]

Direct long records satisfy `a<=b`.  Restricting sockets to `b<=a` is a
sufficient subface, not a without-loss-of-generality theorem.  On that
subface, flag balance on every selected cycle automatically gives the three
reset-cut equations.

The chosen adjacency variables define a directed **cycle cover**.  They do
not define one chronology unless subtour elimination or an independently
replayed component-joining step is added.

Finally, (4.1) shares only an address family.  It need not share the same
literal long cells on both sides.  Therefore `PASS_1S_ROTS_FLAG_PROJECTION`
requires a later literal cyclic-cell replay and is not a physical chronology
certificate.

## 5. Three scopes which must not be merged

### 5.1 Canonical ordinary no-go on the `029d` owner phase

The independent `029d` census exhausts every canonical `4/3/2` common-state
socket against all `18663` original long rows.  It finds `2162` short roles
with no socket, of which exactly

\[
                         \boxed{1741}
\]

are original length-two rows.

Ordinary bottom-transfer recoupling leaves every old length-two row unchanged
and only removes/shortens original long donors; it creates no new long state.
Thus those `1741` rows remain socketless under every ordinary recoupling of
this owner phase.  Since (4.2) requires every short role once, canonical
ordinary `1S-ROTS` is UNSAT on table `029d3be5...`.

### 5.2 Exact relaxed-nine no-go on the round047 warm table

The fixed round047 table `95dee6e...` was exhaustively recensused with all
`16915` long roles, the nine-address short relaxation, and the sufficient
socket direction `b<=a`.  It has

\[
  2188\text{ accepted five-cell socket hyperarcs},\qquad
  \boxed{5969}\text{ short roles with no socket}.       \tag{5.1}
\]

Consequently (4.2) contains `5969` empty degree rows.  The fixed round047
table is therefore solver-free UNSAT for this relaxed `1S` cycle-cover face.
Since the physical `3/2` short flags occur literally among the nine relaxed
flags, the same fixed table is also UNSAT for the canonical physical menu.

The census and its independently written exact coordinate-pattern replay are
bound as follows:

```text
producer / census JSON
b3bed193dbbed859b8f24f9bd82d56a716f2493dba616e8a2d606d89de03505e
df461acc30c5eef12ca8f889b247ca36db32bc6631f0fd420d1a56f19b10431b

socket triples / per-short summary / zero list
381a29b7d83dec652ac0da7bf63f7ae9b5bdb515ab325ac66ffe2d1409ea1e97
3bbf173f17164bed8ca49eb3f4e017e02dec6a2df9f26c35bfdd15fb56bb99d5
ada18b7eafa26675f6ac52efb997e38b5576c1fd7a3ee98a51665dc57bb52f06

independent coordinate-DP source / audit
e77bd070b16897f71e77edd734732c8cc2c14fe8f1a94f02f711cd7c49024029
3758def1349ad9be02daa126ca01ca6e22edb7b93a69b89981397369f44e6085
```

The independent oracle enumerates the 32 bit-patterns on the five merged
cells for each of the 17 coordinates.  Its 32-state DP enforces both exact
short cover equations and global nonemptiness of all five cells.  It replays
all `2188` emitted triples, verifies that they are unique and feasible, and
tests every candidate induced by the exhaustive marginal lists for all
`5969` zero roles.  The producer's outgoing file intentionally omitted the
17 soft long heads; the independent audit reconstructs those candidates by a
separate exact four-cell coordinate DP before comparing each summary degree.
It finds `2211` marginally compatible zero-role combinations and rejects all
of them in the common five-cell oracle.

For completeness, the producer's maximal-box exact-cover test is exact here:
for interval boxes
\(\mathrm{lo}_p\subseteq X_p\subseteq\mathrm{hi}_p\), an exact cover of
`T` exists iff all lower bits lie in `T` and the participating upper boxes
have union exactly `T`; choosing each participating cell equal to its upper
box realizes the cover.  The independent coordinate DP avoids relying on
this argument and obtains the same answer.

This is a **fixed-table** no-go.  It does not close the joint outer choice of
recoupling and relays.  That master must alter the long/short states enough to
give every short role a common predecessor--successor socket.

### 5.3 The global recoupling/relay master remains open

The recoupling launch is based on table `db960ce5...` (and alternate phase
`aee4ebf7...`), not on `029d3be5...`.  The target chains and roots agree, but
`15257` of the `24310` owner assignments differ between `029d` and `db960`.
Socket feasibility uses the owner bits.  Therefore the `1741`-row no-go
cannot be transferred to res1972 without a new canonical common-socket
census.

Moreover a status relay may create a genuinely new long state and can give a
previously dead short row new predecessor or successor support.  The
relay-augmented physical model is therefore a separate open scope.  Neither
the `029d` canonical obstruction nor the round047 fixed-table relaxed
obstruction is a no-good on all `401754` recouplings.

## 6. Proof-safe optional relay columns

The audited one-status relay has the local form

\[
\begin{array}{rcl}
 F:(B_D,R_F)&\longmapsto&(B_D,R_F),\\
 A:(B_A,M_A,R_A)&\longmapsto&(M_A,R_A),\\
 D:(M_D,R_D)&\longmapsto&(B_A,M_D,R_D),
\end{array}                                           \tag{6.1}
\]

where the ordinary recoupling already selected `x_(F,D)=1` and
\(B_A\subsetneq M_D\).  A relay column may be enabled only after checking all
of the following.

1. **Recoupling dependency:** it implies `x_(F,D)=1`, `u_A=0`, and `u_D=1`.
2. **Role conflicts:** without a separately proved composition law, selected
   relay columns are pairwise disjoint on every affected physical row
   `F,A,D`.
3. **Partition replay:** the multiset of named targets on the three rows is
   exactly unchanged; all chains remain strict; roots and owners remain
   fixed; the global histogram stays `(0,7395,16915)`.
4. **Head activation:** the hard long head `A` is disabled and the hard long
   head `D` with bottom `B_A` is enabled.
5. **Supplier activation:** every old supplier record of `A` or `D` is
   disabled.  The short menu `(M_A,R_A)` and the long menu
   `(B_A,M_D,R_D)` are regenerated exactly.
6. **Socket activation:** all sockets using `A` as a long role or `D` as a
   short role are disabled; sockets using `A` as the new short role or `D`
   as the new long role are generated with one shared state and their full
   flag endpoints.
7. **Degree contribution:** (4.1)--(4.2) is applied to the activated modes,
   so the column cannot count an old and a new state of one role
   simultaneously.
8. **Hall dependency:** any cut learned before the relay is activated must be
   pulled back through the complete changed-row/head/socket halo.  A frozen
   head-neighborhood cut is not automatically valid after (6.1).

An enumeration which checks only the new union supplier graph is a pricing
oracle, not a master column certificate.  The round047 static lineage, target
partition and union matching are now independently replayed and hash-bound,
so those forty-eight sequential exchanges are load-bearing for the static
table and union-projection claims in Section 1.  They are **not** certified
configuration columns: the fixed table's exact common-socket census instead
gives the obstruction (5.1).  A proof-producing joint solve must regenerate
and activate the full relay-dependent configuration records listed above;
it may not import the perfect union matching as a `1S` witness.

## 7. Pulled-back Hall cuts and exact replay

The deficit-89 and deficit-57 shores are historical warm starts, and the
round047 zero-defect union matching is still not a fixed fibre for the joint
master.  A valid learned Hall cut must be expressed in active
**configuration** variables and include every recoupling or relay choice
capable of changing:

* membership of a demanded long head;
* the literal target/owner of that head;
* a predecessor's long/short status or payload;
* the selected flag of either endpoint; or
* the common-state socket bank touching the shore.

The full-table no-good

\[
       \sum_f x_{f,d_f^{\rm current}}\le1747          \tag{7.1}
\]

is valid only when the fixed-table oracle exhausts every address/socket
choice allowed at that `x`.  If optional relay columns are present, (7.1) is
valid only when the oracle also exhausts every relay selection compatible
with that same `x`; otherwise the no-good must include the relay/configuration
assignment.

A projection SAT replay must independently verify, in this order:

1. input hashes and all `401754` recoupling incidences;
2. the exact target partition, root/owner bijections, and dynamic row modes;
3. one legal address flag per active mode;
4. every direct four-cell transition and every socket five-cell witness;
5. equations (4.1)--(4.3), including all `16915` long roles and all `7395`
   shorts;
6. `a<=b` on direct arcs, the declared socket direction restriction, and all
   three flag-cut balances;
7. the complete component profile of the selected cycle cover;
8. a literal cyclic-cell replay before any claim of a physical chronology.

Residence, upper shadows, connected topology, source chronology, common-cap,
compiler extraction, and a word remain outside this audit.
