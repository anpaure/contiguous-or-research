# The `K17` OPTIMAL28 carrier: an immutable macro-residence floor and the complete marked-preserving exchange master

Date: 2026-07-31  
Lane: AD, complementary rethread after connected packet fusion  
Status: exact fixed-skeleton obstruction and exact marked-preserving repair
reduction; no residence-clean or upper-complete carrier, common cap, or `K17`
word is claimed

## 0. Verdict

The authenticated OPTIMAL28 construction has already solved the owner-level
topology problem.  It gives one Johnson cycle on all

\[
             {17\choose9}=24310
\]

rank-nine owners, every rank-eight intersection exactly once, and one
contiguous marked bank of `4108` owners.  The marked bank has no internal
`D2<3` or `D3<4` run.

The forced two-bank row

\[
                     Z=P\,F(Q)
\]

has `4108` rank-nine marked entries and `20203` distinct rank-eight facet
entries.  Its `4107` marked turns and its facet entries partition all
`24310` rank-eight colours.  The current chronology nevertheless has

```text
strict D2 bad runs                              2392
strict D3 bad runs                              2392
maximal-envelope empty positions                  0
maximal-envelope replay failures                3568
upper holes at ranks 10,11,12,13+       1900,911,128,0.
```

Two stronger facts close every repair that changes only the residual
`U`-to-port pairing.

1. Among the complement macros not used by the marked packet path, `141`
   individual immutable macro words contain `227` strict internal
   old-coordinate owner runs of length three.  Even splitting the complement
   at **every** old-coordinate port leaves these runs intact.  Their facet
   traces have strict length-two runs, so exact `D2` inversion is impossible.
2. Exhausting every locally possible residual pair choice leaves `218`
   rank-ten targets with no possible adjacent provider.  Since every
   rank-ten interval of a Johnson owner word has an adjacent rank-ten pair
   with the same union, this is a full upper-`q1` obstruction, not a
   short-window proxy.

Thus the saved pairing is not the issue.  A finishing construction must
change complement **interior owner adjacencies**.

There is also an exact positive interface.  Every one of the `218` static
upper holes has between `10` and `45` complement-only new Johnson edges
whose displaced lower colour currently also lies inside the complement.
The same is true for all `1900` upper-`q1` holes of the saved cycle.  Hence
none of these rows has a marked-bank-forcing obstruction at the level of its
individual column domain; simultaneous extension remains open.

The complete marked-preserving, lower-rainbow edge-exchange catalogue has

```text
complement lower colours                       20201
exchange columns                              545721
columns serving the 218 static holes             6419
columns serving all 1900 current holes           66223.
```

Theorem 4.1 gives an exact integral master on these columns.  It is the
smallest current repair object that can simultaneously change the immutable
macro interiors, preserve the marked path and lower palette, and expose
residence/upper/common-cap separation.

## 1. Frozen carrier and zipper

Write the oriented owner cycle as

\[
       P_1,\ldots,P_a,Q_1,\ldots,Q_b,P_1,
       \qquad a=4108,\quad b=20202,
\]

where `P` is the fixed marked packet path.  Put

\[
\begin{aligned}
 F_0&=P_a\cap Q_1,\\
 F_i&=Q_i\cap Q_{i+1}\quad(1\le i<b),\\
 F_b&=Q_b\cap P_1,
\end{aligned}
\qquad
 Z=(P_1,\ldots,P_a,F_0,\ldots,F_b).
\]

The connected lower-rainbow audit proves:

* `P` and `Q` partition all rank-nine owners;
* the `F_i` are `20203` distinct rank-eight sets;
* the `4107` colours `P_i cap P_(i+1)` are distinct and disjoint from the
  `F_i`; and
* these two colour families partition the full rank-eight layer.

Hence `Z` has length `24311`, rank profile `9^4108 8^20203`, and scalar
common-cap slack

\[
                         7401-4108=3293.             \tag{1.1}
\]

Equation (1.1) is only a count.  The current row fails exact inversion, so
there is not yet a common-cap instance whose feasibility could finish the
construction.

## 2. The immutable macro-residence theorem

### Lemma 2.1 (one-unit residence tax)

Let `q_0,...,q_(s-1)` be a linear owner word and put

\[
                         f_i=q_i\cap q_{i+1}.
\]

If one coordinate has a strict owner run

\[
                         0\,1^r\,0
\]

wholly inside the word, then its facet trace has the strict run

\[
                         0\,1^{r-1}\,0.
\]

#### Proof

The coordinate belongs to `f_i` exactly when it belongs to both adjacent
owners.  Intersecting consecutive positions erodes each strict positive run
by one at its right/left boundary.  The two bounding zeros remain inside the
same word.  \(\square\)

### Theorem 2.2 (macro-interior floor)

Fix the OPTIMAL28 marked path and preserve every unselected `A/X/Y` macro
word as a contiguous word, allowing arbitrary residual owner pairing,
component order, component reversal, and cuts at every exposed port.  Then
the resulting two-bank row cannot satisfy exact `D2` inversion.

More precisely, `141` preserved complement macro words contain `227`
strict internal owner runs of length three, all on old coordinates
`0,...,14`.  Each forces a strict length-two facet run.

#### Proof

The independent scan reconstructs each of the `1430` macro words from the
parent chronology, removes every macro belonging to the marked closure or
one of the `28` selected optional components, and applies the literal run
test separately to each remaining macro word.  It finds exactly `227`
length-three rows in `141` words.

By Lemma 2.1 each row becomes a strict length-two run in `F(Q)`.  Its two
bounding zeros are internal to the same immutable macro word, so changing an
outside connector, reversing the word, or splitting at any macro endpoint
cannot change it.  Exact `D2` inversion requires every strict internal run
of `Z` to have length at least three.  \(\square\)

The larger fixed-component audit finds `724` owner runs of lengths two or
three in `257` complement components.  Theorem 2.2 sharpens its physical
meaning: `227` of those obligations survive even after every component seam
is made available.  Therefore at least the `141` listed macro interiors must
be altered if repair packets are confined to individual macro words.  A
single nonlocal actuator may alter several words, so `141` is not asserted
as a lower bound on the number of arbitrary global switches.

## 3. Exhaustive upper-`q1` provider theorem

Let `M` be the fixed macro-plus-marked-packet forest on the `6435` old
rank-eight ports.  Its residual demand profile is

\[
                        0^{691}1^{1744}2^{4000}.       \tag{3.1}
\]

The residual pure-old owners are the `4872` unused members of
`binom([15],9)`.

Every adjacent owner pair occurs at exactly one port.  All possible
upper-`q1` providers under an arbitrary residual pairing are therefore of
the following three types.

1. At a demand-zero port, the two fixed endpoint owners give one fixed
   union.
2. At a demand-one port `t`, its fixed endpoint owner `w_t` and any unused
   owner `u supseteq t` give `w_t union u`.
3. At a demand-two port `t`, any two distinct unused owners `u,v supseteq t`
   give `u union v`.

Together with the unions internal to every fixed macro word, these are all
adjacent pairs.

### Lemma 3.1 (rank-ten intervals reduce to adjacent pairs)

If a nontrivial interval of rank-nine Johnson owners has union `S` of rank
ten, then every adjacent pair in that interval has union `S`.

#### Proof

Two adjacent distinct rank-nine Johnson owners have rank-ten union.  That
union is contained in the union `S` of the whole interval.  Equal finite
ranks force equality.  \(\square\)

### Theorem 3.2 (fixed-skeleton upper obstruction)

The three provider families above cover only `19230` of the `19448`
rank-ten targets.  Exactly `218` targets have no provider under **any**
residual owner-to-port pairing.  Their tag profile is

\[
                   116\text{ `X`-only},\qquad
                   102\text{ `Y`-only}.             \tag{3.2}
\]

No untagged or doubly tagged target occurs in this zero-support set.

Consequently no residual b-flow, connected or disconnected, can make the
fixed skeleton upper-`q1` complete.

#### Proof

The literal audit enumerates the fixed internal and demand-zero unions, all
`39353` admissible unused-owner/positive-demand incidences, all demand-one
turns, and all `80449` unordered owner pairs at demand-two ports.  The union
of their rank-ten labels has size `19230`.  Lemma 3.1 converts absence from
this exhaustive adjacent list into absence from every interval.  \(\square\)

For comparison, the canonical width-three lower-`q2` pair-column census has
`165` zero-support targets.  This is not asserted as an obstruction to the
final nonflat compiler: its literal lower witnesses are not restricted to
the canonical owner triples enumerated by that census.

## 4. Complete marked-preserving lower-colour exchange

Let `C` be the saved lower-rainbow owner cycle and let `E_P` be the `4107`
edges internal to the marked owner path.  The two bank-crossing edges are
also frozen.  For every rank-eight colour `c`, let `e_c={a_c,b_c}` be the
unique edge of `C` with intersection `c`.

A **safe exchange column** is a tuple

\[
                       e=(u,v;c,a_c,b_c)             \tag{4.1}
\]

such that

* `u,v` are distinct complement owners;
* `u cap v=c` and `uv` is not already the edge `e_c`; and
* both endpoints of `e_c` are complement owners.

Selecting the column means deleting `a_cb_c` and adding `uv`.  It preserves
the owner set, the lower colour `c`, and every marked/cross edge.  There are
`20201` eligible complement colours and `545721` columns.  If `k_c` is the
number of complement rank-nine supersets of `c`, the colour profile is

```text
k_c      3     4     5      6      7      8      9
colours 15   129   454   1601   3836   6748   7418.
```

For a rank-ten hole `S`, a column serves `S` when `u union v=S`.  The `218`
static holes have `6419` serving columns, with support between `10` and `45`
per target.  All `1900` current rank-ten holes have `66223` serving columns,
again with support between `10` and `45`.  Thus no current rank-ten hole
has a one-row column-domain obstruction.  This does **not** prove that a
serving column extends to a degree-balanced connected factor.

### Theorem 4.1 (exact exchange-factor master)

Let `X` be any set of safe columns using each colour at most once, and define

\[
 E(X)=\left(E(C)\setminus\{e_{c(e)}:e\in X\}\right)
       \cup\{u(e)v(e):e\in X\}.                     \tag{4.2}
\]

Then `E(X)` is a marked-preserving lower-rainbow two-factor if and only if

\[
 \sum_{e\in X}
 \left({\bf1}_{w\in\{u(e),v(e)\}}
      -{\bf1}_{w\in\{a_{c(e)},b_{c(e)}\}}\right)=0  \tag{4.3}
\]

for every complement owner `w`.  It is one cycle if and only if, in
addition, `E(X)` satisfies every ordinary nontrivial component cut.

Conversely, every lower-rainbow two-factor which has the same marked and
cross edges as `C` is uniquely represented by such a set `X`.

#### Proof

Each column removes and restores the same unique lower colour.  Colour
all-different prevents a repeated deletion, and distinct added Johnson edges
have their displayed colours.  Thus every rank-eight colour remains once.
Equation (4.3) is exactly the condition that every complement owner loses as
many incident old edges as it gains new ones; marked degrees are unchanged.
Hence all owner degrees are two, which is precisely a two-factor.  The usual
component cuts are necessary and sufficient for a two-factor to be one
cycle.  Explicitly, if `Q_1` is the complement endpoint joined to `P_a` and
`y_f(X)` is the final selected-edge indicator, the rooted complement cuts are

\[
 \sum_{f\in\delta_Q(R)}y_f(X)\ge1
 \quad(\varnothing\ne R\subseteq Q\setminus\{Q_1\}).       \tag{4.4}
\]

Degree balance makes `Q_1,Q_b` the only complement vertices of internal
degree one, so (4.4) is equivalent to the complement being one `Q_1`--`Q_b`
Hamilton path.  The cuts apply to final edge indicators, not to change
variables alone.

For the converse, compare the new factor with `C`.  Every new edge has a
unique lower colour `c`; lower-rainbow equality forces deletion of the
unique old edge `e_c`.  Frozen marked/cross edges make the resulting column
safe.  This correspondence is unique colour by colour.  \(\square\)

For the linear zipper, let `L_Z^0(S)` be the load of `S` among the linear
owner adjacencies

\[
 P_1P_2,\ldots,P_{a-1}P_a, P_aQ_1,
 Q_1Q_2,\ldots,Q_{b-1}Q_b.                         \tag{4.5}
\]

The cyclic closing edge `Q_bP_1` is omitted.  Each marked edge is a literal
adjacent pair in `Z`; the first cross edge is represented by
`(P_a,F_0,F_1)`; and every complement edge `Q_iQ_(i+1)` is represented by
`(F_(i-1),F_i,F_(i+1))`.  Simplicity of the owner cycle makes each displayed
facet triple have union exactly `Q_i union Q_(i+1)`.  Conversely every
rank-ten interval in `Z` contains one of these canonical providers.
Therefore upper-`q1` preservation is exactly the signed row

\[
 L_Z^0(S)+\sum_e
 \left({\bf1}_{u(e)\cup v(e)=S}
      -{\bf1}_{a_{c(e)}\cup b_{c(e)}=S}\right)x_e\ge1
                                                               \tag{4.6}
\]

for every rank-ten target `S`.  Counting the cyclic closing edge would be
unsound: its label `88314` has cyclic owner-edge load two but only one
canonical linear-zipper provider in the incumbent.  Every current hole needs
at least one gaining column.  Since one column has one gain label, covering
the `218` static holes also gives the exact elementary floor `|X|>=218`.
A selected set serving only the missing targets is not automatically legal:
it must also satisfy degree balance (4.3), colour all-different, the loss
terms in (4.6), and connectivity (4.4).

## 5. Residence, deeper shadows, and cap recourse

Theorem 4.1 removes the fixed-component restriction and can cut inside the
`141` bad macro words.  It still needs three exact layers.  In each layer the
variable object is the **whole** row `Z(X)` obtained after orienting the
selected complement path between the two frozen cross-bank sockets; checking
the complement in isolation would miss both joins.

1. **Residence and exact inversion.**  Every strictly internal positive run
   of every coordinate in `Z(X)` must have length at least three, and every
   maximal-envelope cell must be nonempty.  These two conditions are
   necessary and sufficient for exact linear `D2` inversion.  For a run
   wholly inside the complement owner path, the run condition equivalently
   forbids owner patterns `0 1^r 0` with `r=2` or `3`, because passing to
   consecutive facets erodes the run by one.  On an incumbent factor this
   gives a sound local no-good on the selected path edges; an exact model can
   instead use the four-state row-run automaton `0,1,2,3+` plus the literal
   envelope rows.  The two bank joins are checked in `Z(X)`, not inferred
   from the complement automaton.  Once exact `D2` inversion holds, the
   associated `D3` residence condition is redundant.
2. **Upper ranks 11 and 12.**  For a target `S`, run the accumulated-union
   automaton along the whole row `Z(X)`, resetting whenever a row is not
   contained in `S` and accepting when the accumulated union is `S`.  This
   is exact for arbitrary interval width.  The current deficits are `911`
   and `128`; ranks `13` through `17` already have no holes, but full
   accumulated-union preservation rows are still required if their witnesses
   are touched.
3. **Common cap.**  Once the repaired `Z` is fixed and passes maximal
   inversion, compute its actual envelope and solve the exact rank-three
   obstruction-clutter matching.  The scalar margin remains `3293` while
   the marked owner count and `20203` distinct facet rows are preserved.
   It is not valid to freeze the current envelope, because the current `Z`
   fails replay.

These layers, together with (4.3)--(4.6), form an exact finite
marked-preserving repair master.  A restricted packet catalogue is a
sufficient subclass; the `545721`-column exchange catalogue is complete for
all marked-preserving lower-rainbow factor rethreads.

## 6. Provenance and exact boundary

Primary connected carrier:

```text
scratch/k17_opt28_connected_owner_cycle_20260731.word
SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa
```

Two-bank audit:

```text
scratch/audit_ad_k17_opt28_twobank_z_row_20260731.py
scratch/ad_k17_opt28_twobank_d2_row_20260731.audit.json
```

Static provider/exchange audit:

```text
scratch/audit_ad_k17_opt28_static_shadow_provider_master_20260731.py
SHA-256 1f3462406f157861af8a549904540608320c9e1df0a6ec9f84994172804f9503
scratch/ad_k17_opt28_static_shadow_provider_master_20260731.audit.json
SHA-256 cb10e939bcdb1e73f08f0cca0b6318c52487acd283a49c63be821c9488d2f857
payload e4b23438a5bb315323fdd72567f14819029986777ff3833dac6b0206b96d5593
```

Independent local-provider census:

```text
scratch/audit_ad_k17_opt28_depth2_local_provider_state_20260731.py
SHA-256 b6a5e4091ac661e577586ca49df289279e17cf9700981ed933c06ce086111e9a
scratch/ad_k17_opt28_depth2_local_provider_state_20260731.audit.json
SHA-256 bcaa076f8844787093b4b5aad98db0186289f5cea66ebc83e45ce20f2eadbbc0
payload fe9bcb8ae361e02be1782d37ff89244bea3779f60b8ee055b568233684229418

MATH_AUDIT_H3_AD_K17_OPT28_STATIC_SHADOW_PROVIDER_NO_GO_20260731.md
scratch/h3_independent_audit_ad_k17_opt28_static_shadow_provider_no_go_20260731.py
SHA-256 44b5e841...
scratch/h3_ad_k17_opt28_static_shadow_provider_no_go_20260731.audit.json
SHA-256 c1c31f76..., payload 1a45c98a...
```

Proved:

* a `227`-run/`141`-macro obstruction to every port-only re-pairing;
* a `218`-target upper-`q1` obstruction to every fixed-skeleton residual
  pairing;
* individual marked-preserving exchange support for every current
  upper-`q1` hole; and
* an exact complete exchange-factor theorem preserving owners, the marked
  bank, and all lower-`q1` colours.

Unproved:

* an integral exchange selection satisfying residence, all signed upper
  rows and connectivity;
* upper completeness at ranks `11` and `12` after rethreading;
* exact `D2` inversion and common-cap feasibility of the repaired row; and
* a literal word of length `24313` or `nu(17)=24313`.
