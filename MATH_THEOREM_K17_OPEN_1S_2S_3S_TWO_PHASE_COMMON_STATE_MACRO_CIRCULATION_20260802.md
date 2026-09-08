# K17 open `1S/2S/3S` two-phase common-state macro circulation and exact accepting-shore gate

**Date:** 2026-08-02  
**Status:** proof-safe finite reduction and certificate contract; no finite
enumeration and no positive or negative verdict.

## 0. Scope and immutable zero catalogue

This note closes the modelling gap left in Section 6 of
`MATH_THEOREM_K17_ALTERNATING_MATCHING_COMPOUND_STATE_AND_THREE_SOCKET_GATE_20260802.md`:
that audit excludes certain closed `2S`, closed `3S`, and short return words,
but explicitly leaves open a directed cycle of open compound columns using at
least four zero shorts.

There are two different objects called “frozen zero” in the current K17
artifacts.  They must not be mixed.

* In this note, `D_0` is the `5,969`-element native one-short common-state
  zero-role list, SHA-256
  `ada18b7eafa26675f6ac52efb997e38b5576c1fd7a3ee98a51665dc57bb52f06`,
  bound to the round-47 table SHA-256
  `95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735`.
* The private-bank theorem also uses a reset-catalogue label
  `frozen_zero`, bound through `short_reset_triples.tsv`; that is a different
  predicate and has a different census.  It may be added as a second label,
  but it cannot replace membership in `D_0` without an explicit conversion
  audit.

Fix two literal transported phase tables `T^0,T^1` and a specified transport
`tau`.  “Common” below means that one selected occurrence has two literal
realisations `c^0,c^1` and the complete certificate of `c^1` is the image of
the certificate of `c^0` under `tau`, including orientation and order.  Two
independent phasewise existential witnesses are not a common occurrence.

The intended terminal gates in this note are:

1. at least four distinct demands in `D_0` are opened;
2. all named demands are disjoint;
3. the bottom pins extend to an outer perfect matching;
4. the declared private bank remains simultaneously realisable; and
5. the owner-dependent supplier graph has matching rank `16,898` in each
   transported phase.

No topology, residence, upper deck, source chronology, common cap, opening,
compiler, or word condition is implied unless its complete literal state is
explicitly inserted into the language and accepting predicate below.

## 1. Literal paired macro records

Let `V` be a finite set of **literal common port states**.  A port state is
not merely `(row,flag)`.  It contains every field on which the next
transition can depend: physical row and role, bottom status, address/flag,
middle/root/owner labels in both phases, port direction, reset/history state
which is declared hard, and the activation context of every conditional
socket row.  Fields omitted from `V` are outside the theorem.

An admitted demand-bearing macro record `c` has arity
`s(c) in {1,2,3}` and contains all of the following data.  The language may
also contain declared `0S` connector records—literal common long--long
transitions, bottom circuits, or other state relays—with `D(c)=emptyset`.
They do not count toward the four-short threshold.  If they are omitted, any
negative result is explicitly scoped against cycles made only from the
listed demand-bearing macros.

1. One ordered microscopic word in each phase, with every physical cell,
   row, owner, root, address, flag, and occurrence identifier named.
2. One tail `a(c) in V` and one head `b(c) in V`.  Every microscopic prefix
   is an actual-tail hard-legal transition in both phases, and the two words
   are paired by `tau`.
3. A demand set `D(c) subseteq D_0` with
   `|D(c)|=s(c)`.  It is the literal short-demand vector of the word, not an
   endpoint boundary which may be telescoped away.
4. Its complete physical row footprint, nonlinear interaction halo, target,
   owner, root and deck deltas, and an internal glue ledger.  Every internal
   interface must cancel literally.  Cancellation after forgetting bottom,
   payload, history, or address labels is insufficient.
5. Its phasewise forced bottom pins, exclusions, private-ticket uses or
   replacement tickets, and its exact delta to every owner-dependent
   supplier adjacency row.

The contraction signature is

\[
       \partial c=e_{b(c)}-e_{a(c)},\qquad
       d(c)=\sum_{q\in D(c)}e_q .                         \tag{1.1}
\]

The first vector is signed and telescopes along a closed directed word.  The
second vector is positive and never telescopes.  This is exactly the
state/demand distinction of the compound-column theorem.

If a purported macro has several independent tails or heads, it is a
directed hyperarc, not a column of a network matrix.  It must first be
serialised into single-port arcs with literal intermediate states, or kept in
an integer hypergraph master.  The network-integrality and Farkas statements
below do not apply directly to an unexpanded multiport hyperarc.

The directed base multigraph is

\[
                 G=(V,C),\qquad c:a(c)\longrightarrow b(c). \tag{1.2}
\]

Parallel arcs are retained: two records with the same endpoint states but
different physical occurrences, pins, phase words, or supplier effects are
different columns.

### Lemma 1.1 (transport and actual-tail necessity)

A base arc is a sound two-phase macro precisely when its paired microscopic
words pass the literal transport and every-prefix tests above.  Equality of
endpoint masks, phasewise existence, or zero aggregate owner/deck delta does
not imply this property.

#### Proof

The endpoint projections forget the occurrence and prefix fields on which
legality depends.  Conversely, a paired record explicitly materialises both
words, verifies the complete transport, and checks every actual tail; hence
it is a legal simultaneous macro on its declared state coordinates.  QED.

## 2. Compact one-cycle master

For `c in C` let `z_c` be its selection bit and for `v in V` let `y_v` say
that the cycle visits `v`.  The basic directed-cycle rows are

\[
 \sum_{c:a(c)=v}z_c=
 \sum_{c:b(c)=v}z_c=y_v\le1\qquad(v\in V).             \tag{2.1}
\]

Demand disjointness and the four-short threshold are

\[
 \sum_{c:q\in D(c)}z_c\le1\quad(q\in D_0),\qquad
 \sum_{c\in C}|D(c)|z_c\ge4.                            \tag{2.2}
\]

Because of the first family in (2.2), the last left side is exactly the
cardinality of the demand union.  It is not merely a multiplicity count.

Rows of the form

\[
                         \sum_{c\in K}z_c\le1            \tag{2.3}
\]

are added for every declared simultaneous conflict set `K`: incompatible
physical occurrences, exclusive pins, private resources, or noncommuting
halos.  Temporal reuse of one row is not automatically a conflict.  It is
allowed only when an explicit actual-tail serialisation is present in the
macro language.

Equations (2.1) alone permit a disjoint union of directed cycles.  For a
fixed selected root `r`, impose `y_r=1` and the directed connectivity cuts

\[
 \sum_{c\in\delta^-(W)}z_c\ge y_v
 \quad\bigl(\varnothing\ne W\subseteq V-\{r\},\ v\in W\bigr). \tag{2.4}
\]

One may enumerate `r`, or use ordinary root-choice auxiliaries.  Under
(2.1), (2.4) is equivalent to saying that every selected arc belongs to the
single directed cycle through `r`: a second selected cycle would give a set
`W` with no entering selected arc.  Thus (2.1)--(2.4), not bare flow
conservation, are the compact one-cycle skeleton.

This skeleton is exact only after the bottom, private, supplier, and
actual-tail activation constraints of Sections 3--4 are attached.  Without
them it is an outer relaxation.

### 2.1 Exact calibration on the currently authenticated open bank

The cited compound-state theorem currently supplies two common open records:

```text
carrier manifest  b99333b131b5ddbf0ab36909ee91dfbdb4dcaeee8686c353f186c5290126eba9
phase-0 table     ac52c0f1a00c91848a0f65f04745aa9a5d5a76d63169ddf3351e44c524f02207
phase-1 table     736fc30c014c7b535f036348380ed46f545c1ef9bf1e409f515660fff2229058
```

\[
\begin{array}{c|c|c|c}
 &a(c)&b(c)&D(c)\\ \hline
 c_2&(13416,0)&(297,0)&\{(298,1),(292,7)\}\\
 c_3&(15767,1)&(1518,1)&\{(2315,7),(2189,7),(2190,7)\}.
\end{array}                                                  \tag{2.5}
\]

The five demands are distinct.  In the language containing only these two
arcs, (2.2) forces `z_(c_2)=z_(c_3)=1`, but

\[
 \partial(c_2+c_3)=e_{(297,0)}+e_{(1518,1)}
                   -e_{(13416,0)}-e_{(15767,1)}\ne0.          \tag{2.6}
\]

Indeed, let `pi` be one on the two displayed heads and zero on both tails
and every other state.  Then
`pi*partial(c_2)=pi*partial(c_3)=1`, whereas `pi` annihilates every
circulation.
This is an exact signed-potential no-go for the two-record authenticated
bank.  It is not a no-go after adding any unenumerated `1S/2S/3S` record,
long-only return, bottom relay, or other `0S` connector.

## 3. Bottom pins and private compatibility

### 3.1 Exact outer matching lift

For each phase `epsilon`, let `G_out^epsilon(z)` be the literal bottom-token
to host graph after the selected macros are materialised.  Introduce binary
matching variables `m^epsilon_(u,h)` for every edge in the declared finite
edge universe, give it the exact availability predicate
`A^epsilon_(u,h)(z)`, and impose

\[
\begin{aligned}
 \sum_h m^\epsilon_{u,h}&=1 &&(u\text{ a real token or declared dummy}),\\
 \sum_u m^\epsilon_{u,h}&=1 &&(h\text{ a required host}),\\
 m^\epsilon_{u,h}&\le A^\epsilon_{u,h}(z),\\
 z_c&\le m^\epsilon_{u,h}
     &&((u,h)\text{ is forced by }c).
\end{aligned}                                               \tag{3.1}
\]

Baseline forced edges are imposed directly.  Conflicting forced pins make
(3.1) infeasible.  Provided the exact availability predicates suppress every
selected-short host use, this single matching formulation also enforces that
one host has one bottom assignment, different hard hosts use different real
tokens, and selected shorts are not silently reused as long hosts.
Every macro whose physical word assumes a particular assignment must imply
that assignment variable in (3.1); if two assignments produce different
literal words, they are different occurrence records.  Thus the bottom table
is not chosen independently after the macro incidence has been forgotten.

For a phase-common physical table the two displayed matching systems are
replays of one decision, not independent recourses.  Impose the transport
equalities

\[
                 m^1_{\tau(u),\tau(h)}=m^0_{u,h}              \tag{3.1a}
\]

on every transported outer edge (or identify the variables when `tau` fixes
the bottom layer).  If a target intentionally permits phase-dependent outer
tables, (3.1a) may be dropped, but the conclusion is no longer a common-table
certificate.

Equivalently, after verifying that all forced pins form a partial matching,
delete their incident vertices.  The residual instance is feasible exactly
when

\[
             |N_{G_{out}^\epsilon(z)-P^\epsilon(z)}(X)|
             \ge |X|                                      \tag{3.2}
\]

for every residual token shore `X`.  A minimum cut separates (3.2).

The same test is the ordinary matching oracle underlying the cotransversal
`M_short` rank formula.  Fundamental-circuit exchange in `M_short` is thus an
exact static bottom-basis pricing oracle.  It is not by itself a macro
certificate: a `2S` or `3S` column is one coupled hyper-ticket, and its
occurrence, phase, pin, private, and supplier fields do not reduce to a
ground-set weight on the short basis.

In the notation of the frozen outer theorem this oracle is explicitly

\[
 r_{\rm short}(S)
 =|S|-18646+r_M\bigl(F\cup(H-S)\bigr),                       \tag{3.2a}
\]

so ranks and fundamental circuits require only ordinary maximum matching.
Formula (3.2a) prices the outer basis exchange; Sections 3.2--5 are the
necessary lift for the correlated macro witness.

### 3.2 Private bank

There are two proof-safe modes.

* **Frozen-private mode.**  Every macro footprint, long host, token, and
  short is disjoint from the authenticated private witness and its transported
  copy.  The old private certificate then survives literally.
* **Flexible-private mode.**  Retain one variable `u_g` for every complete
  occurrence-labelled private ticket in the declared bank.  Require exactly
  one ticket per protected short, separate capacity one on the predecessor
  and successor occurrences of every host, host--token consistency when one
  physical host is used on both sides, injectivity of real tokens across
  distinct hard hosts, and mutually exclusive address state; add
  `u_g+z_c<=1` for every genuine macro/ticket conflict and forbid every
  selected short from serving as a selected long host.  A stricter subbank
  may simply require all long hosts across both sides to be distinct.  If
  phase 1 is
  obtained by transport, the complete ticket and resource record—not just
  its short label—must be transported, and paired ticket bits are identified
  by `u_(tau g)=u_g`.

Writing `s(g),p(g),h(g),u_p(g),u_h(g)` for the ticket fields, the core rows
are, phasewise or on exact transported ticket pairs,

\[
\begin{aligned}
 \sum_{g:s(g)=q}u_g&=1 &&(q\text{ protected}),\\
 \sum_{g:p(g)=v}u_g&\le1 &&(v\text{ a predecessor host}),\\
 \sum_{g:h(g)=v}u_g&\le1 &&(v\text{ a successor host}),
\end{aligned}                                               \tag{3.3}
\]

together with the host--token consistency, token injectivity, short/host
disjointness, address, and macro-conflict rows just listed.  Dropping those
additional rows changes the problem.

For each real endpoint token used by `g`, the same ticket bit must also imply
the corresponding outer edge, for example

\[
 u_g\le m^\epsilon_{u_p(g),p(g)},\qquad
 u_g\le m^\epsilon_{u_h(g),h(g)},                            \tag{3.4}
\]

with the fixed-soft endpoint represented by its literal fixed state rather
than a fictitious real token.  Equations (3.3) without (3.1),(3.4) would
permit a private ticket and an incompatible outer matching to use different
bottom assignments.

The flexible system is a finite exact-cover/set-packing problem.  Its
separate host/token projections are not, in general, a sufficient Hall
test.  A projection matching therefore cannot be substituted for a common
ticket selection.  The known `1,748`-ticket theorem is phase-0; it supplies a
two-phase bank only after its complete witness is transported or separately
replayed.

## 4. Supplier matching and proof-safe Benders cuts

Let `xi` denote the complete materialised decision on which supplier
incidence depends: selected macro occurrences, the chosen outer matching and
private tickets, and the resulting literal phase table.  For each phase
`epsilon`, materialise the exact owner-dependent supplier graph

\[
              G_{sup}^\epsilon(\xi)=
              (Q^\epsilon,H^\epsilon;E^\epsilon(\xi)),
              \qquad |Q^\epsilon|=16898.                     \tag{4.1}
\]

Acceptance requires a matching saturating all `16,898` supplier demands in
each phase.  Direct matching variables give the exact polynomial recourse
once the edge-availability predicates are encoded.  The equivalent Hall
family is

\[
          |N_{G_{sup}^\epsilon(\xi)}(X)|\ge |X|
          \qquad(X\subseteq Q^\epsilon).                      \tag{4.2}
\]

It is separated by one maximum matching/minimum cut.  Static payload
transport does not imply (4.2): the supplier incidence depends on the
selected owner occurrences and must be rebuilt phasewise.

There are three sound lazy-cut forms.

1. If every edge-availability Boolean `a^epsilon_(q,h)` has an exact CNF/PB
   definition, introduce for a failed shore `X`

   \[
      n_h^X\longleftrightarrow
      \bigvee_{q\in X}a^\epsilon_{q,h},\qquad
      \sum_h n_h^X\ge |X|.                                  \tag{4.3}
   \]

   This is a globally valid Hall cut, not an incumbent-only no-good.
2. If the adjacency decoder is external, add a guarded shore cut whose guard
   `G_X` fixes every selector/state coordinate on which all edges out of `X`
   depend.  The exact implication is

   \[
                G_X\Longrightarrow |N(X)|\ge |X|.             \tag{4.3a}
   \]

   When the guard fixes the deficient incumbent neighbor set completely,
   (4.3a) simplifies to `not G_X`.  Omitting one adjacency dependency from
   the guard makes the cut unsound.
3. Without a proved dependency guard, add the whole-selector no-good

   \[
      \bigvee_{c:z_c^*=1}\neg z_c\ \vee\
      \bigvee_{c:z_c^*=0}z_c .                               \tag{4.4}
   \]

   It is weaker but always valid after the oracle has proved that **no**
   bottom/private/supplier recourse exists for that selected cycle.  Failure
   of one greedy recourse witness does not justify (4.4).  If variables
   outside `z` can change the materialised cycle, their full assignment must
   be included in the no-good.

The same alternatives apply to a failed residual outer matching.  A
supplier Hall shore from one phase and an outer Hall shore from another may
not be satisfied by different occurrence choices: both recourses are
conditioned on the same `z` and the same materialised paired macros.

## 5. Exact finite accepting graph

The compact master is useful for pricing, but the cleanest exact cycle/no-go
theorem is ordinary reachability in a finite expanded graph.

For every possible starting port `r`, form states

\[
 \Omega=(r,v,U_D,U_R,T^0_{cur},T^1_{cur},P^0,P^1,\Lambda,b). \tag{5.1}
\]

Here `v` is the current port, `U_D` is the used demand set, `U_R` is the
complete used/exclusive resource state, `T^epsilon_cur` are the literal
materialised paired table states (or an injective finite encoding of their
patch), `P^epsilon` are the accumulated pins, `Lambda` is every declared
private/supplier/activation dependency not recoverable from the preceding
fields, and `b` records that at least one physical macro has been used.

There is an arc labelled `c` from `Omega` exactly when

1. `a(c)=v` at the actual materialised tail;
2. `D(c) cap U_D` is empty;
3. every exclusive resource and pin is compatible;
4. every microscopic prefix of `c^0,c^1` is hard-legal at these actual
   tails; and
5. the head state is the exact literal materialisation after `c`.

The arc updates all fields in (5.1), with
`U_D'=U_D disjoint_union D(c)` and `b'=1`.  Gates intended to hold at every
prefix are tested on the arc.  Gates intended only at commitment are tested
by the accepting predicate; the choice must be declared in the language.

Add a source `s` with arcs to the empty state `(r,r,emptyset,...)` for every
admitted `r`.  Add an arc to a sink `t` precisely from a state satisfying

* `v=r`, `b=1`, and `|U_D|>=4`;
* the final demand and absolute-cover equations;
* one joint exact outer-matching/private-ticket realisation from Section 3;
  and
* supplier matching rank `16898` in both phases for those same materialised
  choices.

The graph is finite because K17, the macro catalogue, all bit masks, and all
declared resource/state ranges are finite.  It may be exponentially large;
this is a finiteness and correctness theorem, not a polynomial-size claim.

### Theorem 5.1 (cycle/path/flow equivalence)

Relative to a complete declared macro language, the following are
equivalent.

1. There exists one literal two-phase closed common-state macro cycle made
   from `1S/2S/3S` columns and any declared `0S` connectors, opening at least
   four distinct demands in `D_0` and passing all declared bottom, private,
   and supplier gates.
2. The sink `t` is reachable from `s` in the expanded graph.
3. With `N` the head-minus-tail incidence matrix and
   `d=e_t-e_s`, the system

   \[
                         Nf=d,\qquad f\ge0              \tag{5.2}
   \]

   is feasible.

Moreover, an integral unit path can be extracted from any feasible instance.

#### Proof

An admitted physical cycle can be cut at any one of its port states.  Reading
its macros in order supplies an `s-t` path because the expanded state records
every demand, resource, materialisation, and recourse dependency.  Conversely,
an `s-t` path begins and ends at the same named port `r`; its transition
records give the ordered literal macro cycle, and the sink predicate gives
all terminal gates.  This proves (1) iff (2).

A path has incidence `d`, so (2) implies (3).  Any nonnegative flow with
incidence `d` decomposes into one or more `s-t` paths plus directed
circulations; hence it contains an `s-t` path.  Equivalently, directed graph
incidence is totally unimodular and an integral extreme point exists.  Thus
(3) implies (2).  QED.

The port closes in (1); the whole materialised table need not return to its
baseline.  The final table is the patched table stored in the accepting
state.  Requiring the complete table coordinate to return would incorrectly
erase the desired augmentation.

### Corollary 5.2 (exact scoped no-go certificate)

If `t` is unreachable, let `R` be the expanded states reachable from `s`.
Then `s in R`, `t notin R`, and no retained arc leaves `R`.  Therefore

\[
 \lambda=-\mathbf1_R,\qquad N^T\lambda\le0,
 \qquad d^T\lambda=1                                      \tag{5.3}
\]

is an exact Farkas infeasibility certificate for (5.2).  A checker needs
the independently regenerated complete vertex/arc catalogue, the reachable
bit set, and the three relations in (5.3).  Merely hashing an unverified arc
list does not prove that a language arc or accepting edge was not omitted;
the frozen generator/replay and every nontrivial terminal-recourse rejection
must therefore be bound into the completeness manifest.

This is a no-go only for the enumerated language and state range.  An SCC
obstruction in the unexpanded port graph, a supplier Hall shore at one
incumbent, or failure of separately projected phase matchings is not an
equivalent global no-go.

## 6. Minimum complete enumeration language

A negative result may cite Corollary 5.2 only if its frozen language manifest
contains at least the following.

1. Exact baseline table, phase, transport, native-zero-list, private-bank,
   bottom-graph, and supplier-decoder hashes.
2. A finite grammar or explicit bound for every allowed microscopic word,
   including all serial orders of `1S`, `2S`, and `3S` columns and every
   admitted `0S` long/state/bottom connector.  Completeness may instead be
   proved by exhaustive simple paths in a finite primitive state automaton.
   Excluding connectors is permitted, but the resulting no-go has exactly
   that restricted scope.
3. Every demand tuple from `D_0` admitted by that grammar.  Representative
   tuples are enough only under a proved action preserving every field below.
4. Every physical cell/payload assignment and every address/flag choice;
   all changed rows and nonlinear halo rows.
5. Both occurrence-labelled phase words and their exact transport pairing.
   Parallel witnesses with the same projected geometry must remain distinct.
6. Exact tail/head port signatures and every intermediate actual-tail state.
7. The internal cancellation ledger for bottom-labelled long states, short
   demands, owners, roots, targets, histories, and every other declared
   ticket.
8. All forced/excluded bottom pins and the exact availability changes in the
   outer matching graph.
9. All private-ticket resources or a literal proof that the frozen private
   witness is untouched, in both phases.
10. All supplier parent/owner identities and exact phasewise adjacency
    changes, not merely the old matching or its cardinality.
11. Every cross-macro conflict and activation predicate, together with its
    literal replay rule.
12. The full accepting predicate, specifying which gates are prefix-hard and
    which are terminal recourse.

In particular, genuine `2S/3S` words with a shared donor, repair, pin, or
state interaction must be enumerated jointly.  They are not the Cartesian
product of unary `1S` existence rows unless an independence theorem proves
that factorisation.  Likewise, a sequence of open macros may reuse a
physical row only through an explicit legal serialisation; blanket
set-disjointness is a sound restriction but yields only a scoped sublanguage
no-go.

## 7. Fail-closed implementation contract

A proof-safe finite driver may use the compact master (2.1)--(2.4) with
matching/private auxiliaries and lazy cuts.  For every integer incumbent it
must:

1. decode one ordered cycle, not a disconnected circulation;
2. rebuild both transported tables after every macro prefix;
3. replay demand disjointness and all bottom pins;
4. replay or reselect the private tickets jointly;
5. rebuild both supplier graphs and verify rank `16898/16898`; and
6. either accept the complete literal certificate or add one of the sound
   cuts in Section 4.

A positive frozen certificate consists of the ordered macro IDs, both
phase-word replays, exact start/head closure, disjoint demand union of size at
least four, final table hashes, bottom matchings, private ticket selection,
both supplier matchings, and all input/source/manifests hashes.

A negative frozen certificate consists of a complete language manifest plus
the expanded reachable shore (5.3), or an independently checkable exact
SAT/ILP proof for an equivalent fully encoded master.  A list of failed local
rows, marginal Hall shores, or absence in a nonexhaustive catalogue is not a
global certificate.

This note does not assert that the existing open `2S` and `3S` witnesses lie
on one such cycle, nor that no cycle exists.  It gives a proof-safe finite
interface which can establish either conclusion without
silently dropping transport, pin, private, or supplier correlation.
