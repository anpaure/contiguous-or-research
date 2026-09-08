# Accumulated-union block automaton for the K17 higher-shadow gate

Date: 2026-08-01  
Lane: AD, finite K17 higher shadows after global q1  
Status: exact theorem and finite audit.  The theorem does not require a
Hamilton owner path before higher-shadow selection.  It does not prove a
resident q1-complete K17 carrier, a common lower compiler, or
`nu(17)=24313`.

## 0. Outcome

There is an exact associative boundary state for the upper interval-OR deck
of an arbitrary family of owner blocks.  For one block it consists of:

1. its truncated total OR;
2. the nested chain of truncated prefix ORs;
3. the nested chain of truncated suffix ORs; and
4. its internal interval-OR deck.

When two blocks are concatenated, every new upper witness is exactly a
suffix OR of the left block union a prefix OR of the right block.  This
gives a literal block product and, equivalently, a targetwise
inactive/missing-set/done automaton.  Neither statement assumes that the
blocks are joined by a Johnson edge.  Johnson legality, owner use, q1
palettes, run residence and source/common-cap legality remain separate
transition labels.

For K17 with middle-owner rank `r=9`, the rows not enforced by a q1-only
master are exactly

| target rank | 11 | 12 | 13 | 14 | 15 | 16 | 17 | total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| number of targets | 12376 | 6188 | 2380 | 680 | 136 | 17 | 1 | 21778 |

Thus satisfying all 19,448 rank-ten clauses does not certify or explicitly
enforce the 21,778 higher targets.  Shared cut, packet and orientation
variables can constrain higher coverage indirectly.  This does **not** say
that all 21,778 are missing; it says that their acceptance rows are absent.

The newest J5 three-owner boundary fusion has exact higher signature

```text
owners:  5878,67318,69238
prefix:  5878(r9),71414(r10),73462(r11)
suffix:  69238(r9),69366(r10),73462(r11)
internal higher deck: {73462} at rank11 only.
```

Hence J5 is a literal **locally** double-rainbow q1 macro, but its
higher-shadow effect is not a generic completion: internally it supplies
one rank-eleven mask; all other gain comes from its exact prefix/suffix
interaction with its exterior contexts.  Global palette uniqueness and
exterior residence are separate.

### Owner intervals versus literal source intervals

Suppose a literal source word is `E_0,...,E_(n-1)` and its depth-`h`
owner row is

\[
                        T_i=\bigcup_{j=i}^{i+h}E_j.                \tag{0.1}
\]

Then, for every `a<=b`,

\[
             \bigcup_{i=a}^bT_i=\bigcup_{j=a}^{b+h}E_j.          \tag{0.2}
\]

Thus every owner-interval witness certified below is a literal source
interval.  Conversely, every source interval of length at least `h+1` is
of the form (0.2); source intervals of length at most `h` are an additional
local deck.  Consequently the owner automaton is exact for the long-source
deck and is a proof-safe sufficient test for full upper coverage.  It is
not a no-go for a target that has an explicit short-source witness.

The block product itself uses only set union and therefore also applies
verbatim to actual source-letter blocks.  Carrying the source-letter
signature in parallel makes the full literal deck exact; the sharper
nine-mask chain bound used below is specific to rank-nine owner blocks.

## 1. The truncated interval signature

Let `E` be a `k`-element ground set.  Fix an owner rank `r` and an upper
depth `Q`, with `2<=Q<=k-r`.  A block is a nonempty word

\[
                  X=(X_1,\ldots,X_a),\qquad |X_i|=r.
\]

No adjacency hypothesis is imposed in this section.  Write

\[
             \operatorname{or}(X[i,j])=\bigcup_{t=i}^j X_t.
\]

Define the depth-`Q` signature

\[
       \Sigma_Q(X)=(T_X,P_X,S_X,D_X)
\]

as follows.

* `T_X` is the total union of `X` if it has size at most `r+Q`, and is the
  overflow symbol `top` otherwise.
* `P_X` is the set of unions of nonempty prefixes whose size is at most
  `r+Q`.
* `S_X` is the analogous set of unions of nonempty suffixes.
* `D_X` is the set of all interval unions of ranks `r+2,...,r+Q`.

The elements of `P_X` form one inclusion chain, as do the elements of
`S_X`.  Every strict change adds at least one coordinate.  Consequently

\[
                   |P_X|,|S_X|\le Q+1\le k-r+1.      \tag{1.1}
\]

At K17, `r=9`, so each chain has at most nine distinct masks.

### Theorem 1.1 (exact block product)

For two nonempty blocks `X,Y`, the signature of the literal concatenation
`XY` is given by

\[
\begin{aligned}
 T_{XY}&=T_X\cup T_Y,                                             \tag{1.2}\\
 P_{XY}&=P_X\cup\{T_X\cup p:p\in P_Y\},                          \tag{1.3}\\
 S_{XY}&=S_Y\cup\{s\cup T_Y:s\in S_X\},                          \tag{1.4}\\
 D_{XY}&=D_X\cup D_Y\cup
          \{s\cup p:s\in S_X, p\in P_Y\}.                     \tag{1.5}
\end{aligned}
\]

In (1.2)--(1.5), a union is retained only at the rank allowed by the
definition of the corresponding row; any expression containing `top` is
overflow and is discarded.  In particular, the cross term in (1.5) is
kept only when its rank lies in `r+2,...,r+Q`.

The operation defined by (1.2)--(1.5) is associative on signatures, and

\[
       \Sigma_Q(X^{\rm rev})=(T_X,S_X,P_X,D_X).                   \tag{1.6}
\]

#### Proof

Every interval of `XY` is of exactly one of three types: it is wholly in
`X`, wholly in `Y`, or crosses their common boundary.  A crossing interval
is uniquely a nonempty suffix of `X` followed by a nonempty prefix of `Y`,
so its union is exactly one term `s union p` in (1.5).  This proves the deck
identity.

A prefix of `XY` is either a prefix of `X` or all of `X` followed by a
prefix of `Y`, proving (1.3).  The suffix proof is dual.  Total unions give
(1.2).  If `T_X` has already overflowed, adjoining further owners cannot
reduce it, so discarding every continuation containing `top` is exact.

The displayed operation is associative because either parenthesization is
the signature of the same literal word `XYZ`.  Reversal interchanges
prefixes and suffixes and leaves total and internal interval unions
unchanged.  QED

### Corollary 1.2 (bounded cross-deck exposure)

At K17, one binary block concatenation creates at most

\[
                         9\cdot9=81                 \tag{1.7}
\]

candidate cross-boundary masks over **all** upper ranks.  This is an upper
bound with multiplicity removed after union; it is not an assertion that
81 new required targets are delivered.  A binary gluing tree on `b` blocks
therefore has at most `81(b-1)` cross-product entries before
deduplication, while the exact internal decks are inherited without loss.

This is the useful compression: one need not enumerate arbitrary owner
intervals at every master node.  One carries two chains of length at most
nine and a target bitset, then applies (1.2)--(1.5).

## 2. Equivalent targetwise automaton

Fix a target `U` of rank `r+q`, where `2<=q<=Q`.  Scan a literal owner word
from left to right.  The state set is

\[
 \{\bot,\checkmark\}\ \cup\
 \{M: \varnothing\ne M\subseteq U, |M|\le q\}.                  \tag{2.1}
\]

Here `bottom` means that the current suffix contains no owner lying inside
`U`; `M` is the set of target coordinates still missing from the current
maximal `U`-compatible suffix; and `checkmark` means that a witness has
already occurred.

For the next rank-`r` owner `V`, the transition is:

\[
\begin{array}{c|c}
\text{condition}&\text{new state}\\ \hline
\checkmark&\checkmark\\
V\not\subseteq U&\bot\\
V\subseteq U,\ \text{old state }\bot&U-V\\
V\subseteq U,\ \text{old state }M&M\cap(U-V),
\end{array}                                                     \tag{2.2}
\]

with the empty missing set interpreted as `checkmark`.

### Theorem 2.1 (target automaton equivalence)

The final state is `checkmark` if and only if some contiguous owner
interval has OR exactly `U`.

#### Proof

Delete every owner not contained in `U`.  These owners separate the word
into maximal `U`-compatible runs.  Within one such run, after reading its
current prefix, the missing set is exactly

\[
                 U-\bigcup\{\text{owners read in that run}\}.   \tag{2.3}
\]

This is the invariant of (2.2).  If it becomes empty, that run prefix is a
literal interval of union `U`.  Conversely, every interval of union `U`
lies inside one compatible run, and by its final letter the missing set is
empty.  QED

For a block `B`, precompute the deterministic transfer map `F_(B,U)` on
(2.1).  Then a chosen block chronology

\[
 B_{i_1}^{\epsilon_1},\ldots,B_{i_t}^{\epsilon_t}
\]

accepts `U` exactly when the composed transfer sends `bottom` to
`checkmark`.  This remains true if rank-`r` owner connector macros are
inserted: they are simply additional blocks with their own transfer maps.
A reset between components cannot be assumed for free; if a reset collar
is used, its actual owner word must be included in the product.  A
lower-rank source collar belongs instead to the source-letter signature and
does not inherit the compressed state bound (2.1).

## 3. Factor-before-Hamilton consequence

### Theorem 3.1 (owner-accumulated higher completion from a block forest)

Let `B_1,...,B_b` be pairwise owner-disjoint literal owner blocks.  For each
block allow a stated set of orientations, and let a connector catalogue
specify which oriented block pairs may be chronologically adjacent and what
rank-`r` owner connector block, if any, is inserted.  A lower-rank
source-letter collar is not an owner connector: it must be carried in the
parallel source-letter signature described after (0.2), and the compressed
state family (2.1) need not be closed for its letters.

For any selected chronology, the following are equivalent.

1. Every upper target of ranks `r+2,...,r+Q` has a contiguous owner-interval
   witness in the chronology.
2. The signature product of Theorem 1.1 contains every such target.
3. Every target automaton of Theorem 2.1 accepts.

These equivalences require neither a Johnson Hamilton path nor even
Johnson adjacency at the bare block boundaries.  Those are possible
restrictions on the connector catalogue, not hypotheses of upper
coverage.

If the owner chronology is realized as one depth-`h` row, (0.2) turns every
accepted owner interval into a literal source interval.  Conversely, the
only literal source witnesses not represented by this owner automaton are
the intervals of length at most `h`; those may be added as a separately
audited local deck or handled by the source-letter version of Theorem 1.1.

If the union of the internal decks `D_(B_i)` is already complete, then any
later literal concatenation preserves higher coverage.  In that special
case topology and higher shadows truly decouple.  Otherwise the order and
the connector words matter, but they can be selected jointly by the finite
transfer system without first finding a Hamilton carrier.

#### Proof

The equivalence of 1 and 2 follows by repeated application of Theorem 1.1.
The equivalence of 1 and 3 follows target by target from Theorem 2.1.
Internal owner intervals remain owner intervals after any exterior
concatenation; (0.2) then makes them literal source intervals whenever the
owner chronology has a common source realization.  This proves the last
assertion.  QED

### Proposition 3.2 (edge-local higher-provider clauses are incomplete)

Let `K` be any eight-set and let `a,b,c` be three distinct coordinates
outside `K`.  The three rank-nine singleton owner blocks

\[
                 K+a,\qquad K+b,\qquad K+c             \tag{3.1}
\]

have adjacent unions `K+a+b` and `K+b+c`, both of rank ten.  Nevertheless
their complete three-block interval has union

\[
                         U=K+a+b+c                     \tag{3.2}
\]

of rank eleven.  Therefore a catalogue which credits only one-boundary
seams has no provider for `U`, although the literal accumulated chronology
does.  Inserting any owner containing a coordinate outside `U` destroys
this witness by resetting the target automaton.

Thus ranks 11 and above cannot in general be reduced to independent
edge-delivery ALO clauses.  The accumulated state is necessary even before
residence or compiler constraints enter.

### Theorem 3.3 (augmentation of the protected ordered-Hall connector)

Fix an admissible rooted state `sigma` in the sense of the protected
boundary-macro ordered-Hall theorem.  Give every rooted component its
literal owner block, and give every allowed free-port arc its complete
rank-`r` owner connector block (possibly empty only when the physical
adjacency itself is the connector).  Any lower-rank source collar is checked
by the parallel source signature and is not silently fed to the compressed
owner DFA.

There is a boundary-compatible, owner/q1-valid and owner-accumulated
higher-complete connector if and only if there are:

1. an allowed component order `prec`;
2. a matching `A` of size `C-1` in the forward split-copy graph
   `B_(sigma,prec)`; and
3. acceptance of every target automaton after expanding the unique directed
   path defined by `A` into its component and connector blocks.

#### Proof

By the ordered-Hall theorem, items 1 and 2 are equivalent to one directed
Hamilton path on the rooted components with the declared boundary macro at
its prescribed end or ends.  Expanding its labelled arcs gives one unique
literal block chronology.  Theorem 3.1 says that item 3 is equivalent to
owner-accumulated higher completeness of that chronology.  Conversely any
such connector has its path order `prec`, its `C-1` arcs form the required
matching, and its higher deck makes every automaton accept.  QED

Theorem 3.3 is a finite exact augmentation, not a new Hall min--max: the
automata couple many consecutive arcs, as Proposition 3.2 shows.  It can be
implemented by a state-expanded path DP or by CEGAR which replays the full
block product and adds one missing-target cut at a time.  If the rooted
forest's internal decks are already complete, item 3 is automatic and the
ordinary ordered-Hall condition remains sufficient for topology.

### Required product state

Theorem 3.1 addresses only upper unions.  A construction-valid transition
must carry the direct product of:

* the accumulated-union signature above;
* exact owner-use and q1 cut/delivery ledgers;
* the complete coordinate run-age state at every joined chain;
* component/path topology; and
* eventually the source-envelope/common-cap state.

Pairwise nonconflict of these labels is not automatically globally
compositional.  In particular, the current global-q1 replay proves that
pairwise residence is not enough when a middle fragment is used in both
provider roles.

## 4. Exact K17 state sizes

The worst-case number of target-automaton states in (2.1) is

\[
                 2+\sum_{i=1}^q {9+q\choose i}.                 \tag{4.1}
\]

The exact K17 values are:

| rank | `q` | targets | states per target |
|---:|---:|---:|---:|
| 11 | 2 | 12376 | 68 |
| 12 | 3 | 6188 | 300 |
| 13 | 4 | 2380 | 1094 |
| 14 | 5 | 680 | 3474 |
| 15 | 6 | 136 | 9950 |
| 16 | 7 | 17 | 26334 |
| 17 | 8 | 1 | 65537 |

Expanding every state for every target would give 9,530,423 states per
active scan layer.  That is exact but unnecessary.  The block signature
uses at most nine prefix and nine suffix masks, and a lazy master need
instantiate only currently missing target rows.

For example, the authenticated support-7115 double-rainbow factor has
cycle-internal higher-hole vector

\[
                   (1496,329,13,0,0,0,0)              \tag{4.2}
\]

at ranks 11 through 17.  Restricting (4.1) to those 1,838 rows gives

\[
        1496\cdot68+329\cdot300+13\cdot1094=214650   \tag{4.3}
\]

worst-case target states, before block-transfer minimization.  This factor
is not resident and (4.2) is its cyclic internal-deck census, so (4.3) is a
model-size calibration, not a K17 construction.

The supporting cyclic-interval audit is
`scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.audit.json`,
SHA-256
`08f018f137a5c8e5a53e1227383afd066afe019f9dc1293298f5968ba2c5da4a`,
payload
`c8a091333429973fb145e14f4a72fb567a5fef819b6c982f95bd842d7a9f0221`.

## 5. Exact boundary-macro signatures

### 5.0 J4 calibration

The earlier local native fusion `8152,8090,69530` has

\[
 P=(8152,8154,73690),\qquad
 S=(69530,73626,73690),\qquad
 D_{\ge11}=\{73690\}.                                \tag{5.0}
\]

As with J5, this is a local two-edge double-rainbow statement.  It says
nothing by itself about collisions with the exterior global palettes.

### 5.1 J5, the newest native double-rainbow fusion

The literal word

\[
                        5878,67318,69238               \tag{5.1}
\]

has lower q1 colours `1782,67190`, upper q1 colours `71414,69366`, and
total union `73462`.  Its exact depth-eight signature is:

\[
\begin{aligned}
 P&=(5878,71414,73462),\\
 S&=(69238,69366,73462),\\
 D_{\ge11}&=\{73462\}.                                \tag{5.2}
\end{aligned}
\]

Let `L` and `R` denote the complete accumulated left and right contexts at
the moment J5 is attached, not merely the immediately adjacent primitive
blocks.  Every higher interval using J5 has exactly one of three occurrence
types, with mask in the corresponding family:

\[
\begin{aligned}
 &\{s\cup p:s\in S_L, p\in P_{J5}\},\\
 &\{s\cup p:s\in S_{J5}, p\in P_R\},\\
 &\{s\cup73462\cup p:s\in S_L, p\in P_R\}.          \tag{5.3}
\end{aligned}
\]

together with the one internal mask `73462`.  The three interval occurrence
types are disjoint, although their resulting mask sets in (5.3) can
overlap.  Formula (5.3) is an exact finite interface; it replaces the
unsound assertion that q1 attachment automatically helps every higher
rank.

The separately audited boundary children `6134,73334,83702` have nonempty
q1 provider menus.  That fact does not decide any row in (5.3), because the
chosen provider fragments change the actual suffix/prefix chains.

### 5.2 The open shared-bank J6 path

For comparison, the internally resident eleven-owner J6 opening has higher
deck counts

\[
                         (9,8,6,5,1,0,0)              \tag{5.4}
\]

at ranks 11 through 17.  Its distinct prefix and suffix ranks are each

\[
                         9,10,11,12,13,14,15.          \tag{5.5}
\]

Its total union is `32767` of rank 15.  Hence it is a substantially richer
higher-shadow boundary macro than J5, but it still supplies no internal
rank-16 or rank-17 witness and its opening exports the separately proved
nested residence continuation.  It is not selected by the authenticated
global-q1 SAT regression.

There is also a sharp directionality consequence.  Any interval which
enters J6 from the left and exits it on the right contains the whole macro,
so its union has rank at least 15.  Therefore J6 can affect ranks 11--14
only internally or through **one** exterior side; no two-sided J6 interval
can repair a target at those ranks.  At ranks 15--17 the exact two-sided
candidate family is

\[
             \{s\cup32767\cup p:s\in S_L, p\in P_R\},          \tag{5.6}
\]

where again `L,R` are the complete accumulated exterior contexts.

This rank floor is an immediate consequence of the total-OR row in
Theorem 1.1 and is independent of topology or residence.

## 6. What the current q1 SAT regressions do and do not prove

### 6.1 Fully audited run3

The separately frozen semantic/CNF reconstruction of run3 reports:

```text
1,440,814 variables; 7,015,468 clauses;
67 sockets; 1,815 providers; 1,890 cuts; one macro;
19,448 exact global rank-ten clauses satisfied.
```

At nominal provider ranges it had 143 bad chains and 172 short internal
runs.  Expanding each selected range to the actual maximal fragment under
the selected cuts strengthens the physical failure to

```text
1,333 provider path components; zero provider cycles;
230 bad path components; 276 short internal positive runs.
```

The latter is the construction-relevant count.  It is not an edit lower
bound: one rethread can repair several runs.

### 6.2 Newer J5 regression

The newer J5/cap-expanded model has:

```text
2,203,027 variables; 10,756,782 clauses;
68 sockets; 1,820 providers; 1,911 cuts; one macro;
24,310 owner resources and 19,448 global q1 clauses.
```

Its saved scalar summary reports a passing full-CNF assignment replay.  Its
actual-fragment summary gives

```text
1,288 provider path components; zero provider cycles;
239 bad path components; 296 short internal positive runs.
```

Therefore neither SAT assignment is a resident owner forest.  Calling
either one a K17 carrier is presently invalid.

Even after residence is repaired, a q1-only SAT carrier still needs four
separate closures:

1. **Higher target acceptance.**  In the owner-accumulated route, all
   21,778 rows in the first table must pass Theorem 1.1 or 2.1;
   alternatively a row may be discharged by an explicit short-source
   witness.  The q1 CNF contains neither kind of row.
2. **One literal chronology.**  The selected provider digraph is a path
   forest, not the final source order.  Higher cross-component witnesses are
   undefined until actual blocks and connectors are ordered.  A Hamilton
   Johnson path is not necessary, but a literal chronology is.
3. **Lower restitution.**  The q1 master protects upper rank ten.  It does
   not certify the final distinct lower rank-eight deck after 1,890 or
   1,911 cuts and all replacement adjacencies.
4. **One integral compiler.**  Maximal source caps, lower targets at all
   depths, schedules, and common-cell capacity are absent.

Thus the exact next finite object is not another rank-ten provider cover.
It is a joint block-selection/order master whose transition label is the
product state listed after Theorem 3.1.  Higher coverage can be enforced
before Hamiltonization, but it cannot be inferred from q1 SAT.

## 7. Independent finite audit

The audit script exhausts all 11,110 words of lengths one through four over
the ten rank-two owners of `[5]`.  It checks every 32,100 binary split
against Theorem 1.1 and all 66,660 target-DFA instances against Theorem 2.1.
It also independently reconstructs the J4, J5 and J6 signatures above.

```text
scratch/audit_ad_k17_accumulated_union_block_automaton_20260801.py
  SHA-256 6df6e58a5e35b64d2a11fe6807453861bcfbe7b0a2eab66ba5a293d79738aaee

scratch/ad_k17_accumulated_union_block_automaton_20260801.audit.json
  SHA-256 4a0d578bbfb2699274a15d960d572ea57e18d4e2ac79eb78f3657fdd9c1fdc7f
  payload 4f6168920fac6cdab085fcfa23368dc13d137d7f277204d979d9a934253e0760
  status PASS_ACCUMULATED_UNION_MONOID_AND_TARGET_DFA
```

The H100 run used one low-priority Python process, a 120-second wall cap and
a 512 MiB address-space cap; it exited zero.

The frozen q1-scope scalar summaries copied from the existing H100 runs
are:

```text
scratch/ad_k17_global_q1_j5_base_model_replay_20260801.audit.json
  SHA-256 06f020b4e2512bdf1a1d9804c254e537ceb3f9b3270934aa712a6f4ab84df5c9

scratch/ad_k17_global_q1_j5_actual_residence_20260801.audit.json
  SHA-256 3c71f163ef34f1185e9b40a332fc8b1c637aaa189c8e66a83f6f8f72dd775fb6

scratch/ad_k17_global_q1_run3_actual_fragments_20260801.audit.json
  SHA-256 a7fb4d4c8a7c39bbc1ea3e2e58779b6ba17081fe48042268f461ffea7581d7d2
```

These three small JSON files authenticate the quoted scalar summaries, not
the complete CNF/model/map/input packages.  Certificate provenance remains
in the upstream global-q1 audit package.  The local independent checker
sources used there are

```text
scratch/audit_k17_global_q1_master_semantics_20260801.cpp
  SHA-256 2d7fadbf89ca1ecc1a5ec0fe0f04f2587017b80b5a20122fdf7c424e6cae7186

scratch/audit_k17_global_q1_actual_provider_fragments_20260801.cpp
  SHA-256 27b2248602697b0b5f23391f7d6348889d2d790665a8ad6ab8ec1d48b0e130ee

MATH_AUDIT_K17_GLOBAL_Q1_MASTER_SEMANTICS_AND_CHAIN_RESIDENCE_20260801.md
  SHA-256 f4d2ed67e237ff3a357e3cb7dbd5dfbfbc4add6d08c55dcbb9501a129a042432
```

## 8. Sharp remaining boundary

Proved here:

* exact accumulated-union composition for arbitrary owner blocks;
* an equivalent target automaton;
* factor-level higher completion without a prior Hamilton restriction;
* exact K17 state counts and J5/J6 higher signatures; and
* the precise construction-invalid and unconstrained rows of the current
  q1 SAT assignments.

Not proved:

* existence of a resident q1-complete K17 forest accepted by all higher
  automata;
* simultaneous block ordering with owner/q1/run guards;
* lower all-depth/common-cap compilation; or
* a length-24,313 K17 word.
