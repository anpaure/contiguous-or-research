# Pentagonal rank separation and the exact four-path Catalan connector absorber

Date: 2026-08-01  
Lane: protected rooted Catalan connector / additive-constant finish  
Status: exact no-go for the orbit bank as a connector substitute, exact
conditional four-path absorber, and exact split-letter interface.  The
all-dimensional accessibility hypothesis remains unproved.

## 0. Verdict

The full-rotation pentagonal bank solves the wrong one of the two Catalan
rank rows if it is used by itself.  It can remove cycle nullity from an exact
outer-palette selector, but every cycle-free result still has exactly
`Cat_m` path components.  This is forced by Euler characteristic, not by a
defect of the known finite factors.  A palette-neutral `3<->3` bank preserves
the number of selected edges and therefore cannot supply any of the
`Cat_m-O(1)` additional connector edges in the rooted decomposition.

There is nevertheless a precise absorber role for the local pentagonal
packet.  First choose all but four of the required connector edges.  The
resulting rooted partial permutation has exactly four path components and
some number of cycle components.  Every *root-compatible prepared*
pentagonal packet removes one cycle while retaining exactly four paths and
both outer palettes.  If such a packet is available serially for every
remaining cycle, the process ends in a four-component forest.  A final
four-edge residual matching, containing one prescribed closure, then gives
an upper-surjective q1 factor with at most four components.

Thus the exact surviving all-`m` statement is not “a pentagonal orbit exists.”
It is a correlated **near-perfect connector matching plus serial prepared
pentagonal accessibility plus four-port Hall** theorem.  The frozen orbit
banks do not prove it: the `m=3` cyclic selector has no companion old phase,
and at `m=6` no single packet is in the prepared five-component position;
only the entire rotation orbit works at the upstream acyclicity stage.

Split letters act strictly downstream.  Once the incidence connector and a
protected closure already exist in a compiled reference word, a bounded
number of remaining OR-mask debts can be paid under actual dominating source
letters without losing any old interval.  A split letter cannot create a
missing incidence edge, connector rank unit, or residual closure.

## 1. The common Catalan Euler ledger

The even central selector and the odd rooted connector have the same forced
defect.  In the even central host put

\[
 V_e={2m\choose m},\qquad E_e={2m\choose m-1}.
\]

In the odd rooted host of the connector decomposition put

\[
 V_o=W={2m-1\choose m},\qquad
 E_o=K={2m-1\choose m+1}.
\]

Then in both cases

\[
 V_e-E_e=V_o-E_o
   ={1\over m+1}{2m\choose m}=\operatorname{Cat}_m.       \tag{1.1}
\]

For every spanning graph `G`, write

\[
 \beta(G)=|E(G)|-|V(G)|+c(G)                              \tag{1.2}
\]

for its cycle nullity.  Therefore

\[
 c(G)=|V(G)|-|E(G)|+\beta(G).                            \tag{1.3}
\]

### Theorem 1.1 (pentagonal rank separation)

Let `G` be an exact outer-palette selector in either central ledger above,
and apply any disjoint family of pentagonal `3<->3` exchanges, including a
clean full-rotation orbit bank.  If the resulting graph `G'` is a spanning
linear forest, then

\[
                         c(G')=\operatorname{Cat}_m.      \tag{1.4}
\]

In particular, when used as an internal reselecting bank on `Q0` and
required to return another forest, no such exchange supplies any of the
`Cat_m-s` **additional-edge** connector units needed for an `s`-component
rooted factor.

#### Proof

Every pentagonal exchange cyclically reassigns three upper colours over the
same three lower colours.  Hence it replaces three selected physical edges
by three selected physical edges and preserves the two outer palettes.  A
disjoint bank has the same property by addition.  Thus `G'` has the same
vertex and edge counts as the exact selector.  Since `G'` is a forest,
`beta(G')=0`; (1.1)--(1.3) give (1.4).

The rooted Catalan forest already has `E_o=V_o-Cat_m` edges.  An
`s`-component forest has `V_o-s` edges, so it needs exactly `Cat_m-s`
additional selected incidences.  Cardinality-preserving exchanges add none.
\(\square\)

This theorem explains the frozen positive rows exactly.  The `m=6` clean
bank ends in `Cat_6=132` paths and the `m=8` bank ends in
`Cat_8=1430` paths.  Those banks construct or repair the **rooted Catalan
forest scale**; they do not perform the Catalan connector stage.

## 2. Rotation closure and rooting are different interfaces

The full orbit-bank theorem is stated on the even ground `[2m]` with the
action of `C_(2m)`.  The rooted connector theorem is stated on `[2m-1]`
relative to a fixed perfect incidence matching `M0`.  Deleting one
distinguished coordinate does not turn a complete `C_(2m)` packet orbit into
a palette-neutral odd-ground bank: rotation moves the deleted coordinate,
so the surviving packets are not a union of full orbits.

The local five-label pentagonal formula does embed on `[2m-1]`, but it has a
new literal condition.  At each of its three lower colours, the old and new
physical edges share exactly one endpoint.  A rooted use relative to `M0`
is possible only when this shared endpoint is precisely the endpoint chosen
by `M0` at that lower colour.  Call this **root alignment**.  It is not a
consequence of outer-palette equality or of the even rotation-bank theorem.

Consequently the exact implications are

\[
 \begin{array}{c}
 \text{clean even rotation bank}\\
 \Downarrow\\
 \text{exact central linear forest with Cat_m paths}
 \end{array}
 \qquad\text{but not}\qquad
 \begin{array}{c}
 \text{rooted odd connector bank}\\
 \text{or fixed-}M_0\text{ accessibility}.
 \end{array}                                             \tag{2.1}
\]

This is a type separation, not a claim that a future suspension or descent
cannot transport a bank.  Such a theorem would have to transport the three
shared `M0` endpoints, the unmatched port sets, and the protected closure
literally.

There is also an exact invariant inside the rooted odd host.  Let `X,Y` be
the unused tail and head banks of a rooted matching.  An aligned pentagonal
pivot keeps `X` fixed and replaces two unused heads `G,H` by `B,C`, where

\[
                         \chi(B)+\chi(C)=\chi(G)+\chi(H). \tag{2.2}
\]

Consequently every coordinate port gap

\[
                         g_i=d_i(Y)-d_i(X)                \tag{2.3}
\]

is invariant under every aligned packet.  A residual perfect incidence
matching requires `g_i>=0` for every coordinate; a protected residual edge
which adds coordinate `i` requires `g_i>=1`.  For a rooted Catalan forest,

\[
                         g_i=\operatorname{Cat}_{m-1}-a_i, \tag{2.4}
\]

where `a_i` counts its selected edges adding coordinate `i`.  Thus the full
addition-load vector is a packet invariant, not merely the scalar edge
count.

This gives a literal post-hoc no-go.  An upper-exact rooted `m=4` forest has
14 components and port-gap vector

\[
                         (4,2,2,3,3,1,-1).                \tag{2.5}
\]

Its residual matching rank is only `11/14`.  It has exactly one live
forest-preserving aligned pentagonal pivot; (2.5) and rank `11/14` remain
unchanged afterward.  Hence

\[
 \boxed{\text{rooted Catalan forest + aligned pentagonal pivots}
        \not\Longrightarrow \text{residual connector completion}.}    \tag{2.6}
\]

The obstruction is to universal repair of an already chosen fibre.  It
does not refute choosing `Q0` and the residual high-rank matching jointly in
a different degree-admissible fibre.

The upstream rotation theorem removes two false scalar objections.  When
`m` is odd its nonfree antipodal outer sector has an automatic invariant
linear forest, so only the full-orbit sector remains.  Moreover every exact
cap-two central selector has endpoint slack `y_T=2-d(T)` satisfying

\[
 \sum_Ty_T=2\operatorname{Cat}_m,
 \qquad \sum_{T\ni i}y_T=\operatorname{Cat}_m             \tag{2.7}
\]

for every coordinate `i`.  Thus total and coordinatewise *central endpoint
supply* are exactly balanced.  What is not automatic is its rooted division
into tail and head ports: (2.3)--(2.5) show that choosing `M0,Q0` can turn a
balanced undirected slack bank into an impossible directed addition fibre.
The all-`m` selector must preserve (2.7) while enforcing all rooted gaps and
the protected closure margin simultaneously.

For completeness, one packet can change relative graphic rank by at most
three.  Hence `t` packets gain at most `3t`, and one full rotation orbit of
at most `2m` packets gains at most `6m`.  Since `Cat_m` is exponential in
`m`, one orbit cannot repair a generic `Cat_m-O(1)` subtour/rank deficit.
The successful finite orbit banks start from highly correlated factors; they
are not evidence for a rank reset from an arbitrary selector.

## 3. Residual ports and the exact four-path state

Fix a rooted Catalan forest `Q0` in the odd host.  Its `Cat_m` link
components are directed paths.  Each has one unused tail port and one unused
head port.  The residual incidence graph `B0` on these ports is the graph in
the exact high-rank matching criterion.

More generally, let `Q` be a rooted incidence matching of size `W-s` whose
link graph is a spanning partial permutation.  Every link component is a
directed path or directed cycle.  If it has `p` path components and `z`
cycle components, then

\[
 |Q|=W-p,\qquad \beta(\lambda(Q))=z.                    \tag{3.1}
\]

Hence `p=s` independently of `z`.  In particular, a size-`W-4` connector
state always has exactly four path components; every other component is a
cycle.

A full perfect matching of `B0` gives a cycle cover on the `Cat_m`
components.  Ordinary Hall proves only that this cycle cover exists.  The
desired `O(1)` result is the high-graphic-rank condition

\[
 r_{\bar G}(F)\ge \operatorname{Cat}_m-O(1),             \tag{3.2}
\]

or equivalently that the cover has `O(1)` cycles.  The pentagonal packet is
a possible subtour surgery after this matching row has nearly been paid; it
does not replace the matching row.

## 4. Exact conditional pentagonal absorber

Fix `M0` containing the first protected shore `P0`, a protected second-shore
path seed `P1`, and a protected residual incidence edge `e_*`.  Call a
pentagonal exchange on a rooted partial
matching `Q` **admissible** when:

1. its three old selected incidences and three new incidences are root
   aligned with `M0`, and replacing old by new leaves an incidence matching;
2. its old target edge lies on a link-cycle component;
3. its two companion old edges lie on two distinct link-path components;
4. its two new-only endpoints lie on the other two link-path components,
   all five named components being distinct before the exchange;
5. its old and new supports avoid `P1` and `e_*`; and
6. the old and new three-atom phases have the same lower and paired-upper
   multisets.

Rows 2--4 are the prepared topology of the pentagonal path-bank theorem;
row 1 is the extra rooted matching condition.

### Theorem 4.1 (serial four-path absorber)

Suppose there is a rooted matching `Q` with the following properties:

* `|Q|=W-4`, `P1 subset Q`, and its paired-upper labels cover the complete
  rank-`(m+1)` layer;
* its link graph has four path components and `z` cycle components; and
* whenever `z>0`, the current state has an admissible pentagonal exchange.

Then after exactly `z` exchanges there is a rooted matching `Q*` of size
`W-4` such that:

1. `P1 subset Q*` and the complete paired-upper palette is unchanged;
2. `lambda(Q*)` is a spanning forest with exactly four path components; and
3. the protected edge `e_*` has not been used.

If the four unmatched vertices on each incidence shore admit a residual
perfect matching `R subset ML_m-M0` containing `e_*`, then

\[
                         M_1=Q^*\mathbin{\dot\cup}R       \tag{4.1}
\]

is a perfect second incidence matching, and `M0 union M1` is an
upper-surjective q1 factor with at most four components containing the
protected seed and closure.

#### Proof

One admissible exchange has the exact old/new outer palettes and preserves
matching cardinality.  The prepared five-component topology replaces one
cycle and four paths by four paths.  Thus it lowers `z` by one and changes
neither the number four of path components nor the protected resources.
Induction terminates after exactly `z` steps at a four-path forest.  This
proves 1--3.

The residual matching completes `Q*` to a perfect second matching.  The
forest links of `Q*` already have graphic rank `W-4`; adding four links
cannot lower rank, so the completed permutation has at most four cycles.
Its upper palette was already complete before the residual edges were
added, and all lower q1 colours occur once because `M1` is perfect.  The
containments of `P1,e_*` are literal. \(\square\)

Four is the anchor count of this clean prepared criterion: its local state
uses four distinct path components.  No minimality is claimed among all
possible pentagonal or collective absorbers.  Indeed a different collective
orbit-bank surgery may need fewer anchors, as the frozen `m=6` result
demonstrates, but no dimension-uniform rooted version of that collective
effect is known.

The theorem is a genuine absorber reduction, not an all-`m` existence
proof.  It leaves three exact host rows:

1. choose a protected rooted `Q0` whose residual graph has a matching of
   size `Cat_m-4` and a four-edge residual completion;
2. prove serial root-aligned pentagonal accessibility for every cycle of
   the resulting partial permutation; and
3. preserve the prescribed `e_*` in the final four-port Hall instance.

The finite orbit census sharply prevents deleting row 2.  The frozen
`m=3` cyclic selector has no companion old pentagonal phase, while the
`m=6` selector has no individually prepared packet even though its whole
orbit bank succeeds.  Hence neither exact palettes nor rotation symmetry
implies the local accessibility hypothesis.

### Theorem 4.2 (smallest rooted direct-toggle obstruction)

On the authenticated insured rooted targets, the complete bank of
root-aligned, protected-lower-disjoint pentagonal packets has the following
exact census:

\[
\begin{array}{c|c|c|c|c}
(m,h)&\text{packets}&\text{direct matching toggles}
 &\text{correlated reselection passes}&\text{forced collisions}\\ \hline
(4,1)&1&0&0&1\\
(5,1)&11&0&9&2\\
(5,2)&11&0&9&2.
\end{array}                                             \tag{4.2}
\]

Every one of the 23 literal three-edge toggles fails the head-bijection row.
For five packets the failure is absolute: a new packet incidence and a
protected collar incidence force two distinct lower rows to the same head.
The unique `m=4` packet is the smallest such fixture.  In it the protected
row `50->54` and the new packet row `52->54` collide.

For 18 of the 22 `m=5` packets, a correlated reselection of the rest of the
second matching succeeds.  Every positive has:

* the fixed first matching and all protected collar incidences;
* the fixed upper-transparent residual closure;
* a rooted `Q0` with `Cat_5=42` components;
* contracted connector rank `41=Cat_5-1`; and
* the complete paired-upper palette.

#### Proof

The independent replay enumerates the full root-aligned packet bank.  It
checks the direct head map before invoking any completion.  In each negative
case the displayed duplicated head is forced by one packet row and one
protected row, so no completion can remove it.  For every positive it
reconstructs the complete second matching and audits every incidence,
protected edge, upper colour, `Q0` component, contracted connector edge,
graphic rank, and the fixed residual closure. \(\square\)

This theorem refutes the prospective implication

\[
 \boxed{\text{root aligned + protected-lower-disjoint}
        \Longrightarrow \text{locally selectable pentagonal packet}.} \tag{4.3}
\]

It also shows the correct escape: the packet and the Catalan connector must
be selected **correlatively**.  The `m=5` positives are finite evidence for
that joint selector, not an all-dimensional construction.  A scalar
split-letter repair cannot cure the negative rows, because it can create a
mask value but cannot give two incidence rows distinct heads.

## 5. The split-letter finish and its type boundary

Assume the owner/incidence construction of Theorem 4.1 has already been
compiled into a reference OR word and the protected closure has a named
realizing interval.  Require the named compiler certificate to be
**contraction-stable** for the proposed insertions: every transported
deadline has the required slack, and every asserted common-cap/common-`Q`
row is retained under the same block transport.  This is extra data; it does
not follow from OR containment alone.

Let `T_1,...,T_b` be the remaining terminal OR-mask debts, with `b=O(1)`.
If they can be partitioned among actual nonzero source letters
`X_1,...,X_a` so that every task assigned to `X_j` is contained in `X_j`,
replace

\[
 X_j\quad\longmapsto\quad X_j,T_{j,1},\ldots,T_{j,b_j}.   \tag{5.1}
\]

The block union is still `X_j`.  Block contraction therefore transports
every old interval, including the named protected closure, and realizes all
tasks as singleton cells.  Under the declared contraction-stable compiler
state, the named deadline/cap rows transport as well.  The total length
increase is `b=O(1)`.  If a whole debt family is one direct nested ray
satisfying the one-column criterion, one split letter can service that full
ray instead.

There is a weaker simultaneous pivot face.  A task `T` may be inserted at a
cut `A_c|A_(c+1)` whenever

\[
                         T\subseteq A_c\cup A_{c+1}.       \tag{5.2}
\]

Every old interval crossing the cut already contains that union, while
intervals on one side do not see the inserted letter.  Hence arbitrary
bounded banks may be inserted at one or several such cuts with the same
literal OR-preservation conclusion, again subject to the separately declared
deadline/cap slack.  For this natural transport the containment condition is
also necessary: the minimal old interval crossing the cut has union
`A_c union A_(c+1)`, so an inserted task outside that union changes its OR.

This finish cannot be moved before the connector theorem.  Splitting a
source letter refines one word position and preserves old interval values;
it does not choose an unused lower port and owner port, create an incidence
edge between them, or increase the graphic rank of the component-port
cover.  In particular, inserting a singleton whose mask equals a missing
paired-upper colour does not manufacture the two middle owners whose union
has that colour.  The residual closure and its common-cap/compiler state
must already exist.

Thus the exact division of labour is

\[
 \boxed{
 \text{rooted connector + protected closure first}
 \quad\Longrightarrow\quad
 \text{bounded split-letter OR-debt finish}.}            \tag{5.3}
\]

## 6. Audited finite and algebraic rows

The companion replay checks:

* both Catalan identities in (1.1) for `2<=m<=16`;
* the literal pentagonal lower/upper identity and its three forced root
  alignment endpoints for `3<=m<=12`;
* the exact four-path/nullity ledger for zero through six cycles;
* the frozen `m=6,m=8` clean-bank outputs, including exactly `Cat_m` final
  paths;
* the `m=4` Catalan decomposition rank ledger; and
* all 23 rooted packet rows in (4.2), including the five forced head
  collisions and all 18 correlated `m=5` completions;
* the authenticated split-letter payload.

Run

```text
python3 scratch/audit_catalan_pentagonal_connector_rank_separation_20260801.py
```

Expected status:

```text
PASS_CATALAN_PENTAGONAL_CONNECTOR_RANK_SEPARATION
```

The replay is an audit of the exact identities and frozen inputs.  It does
not assert serial accessibility in dimensions not covered by a supplied
host certificate.

Frozen companion artifacts:

* `scratch/audit_catalan_pentagonal_connector_rank_separation_20260801.py`,
  SHA `529ad1c312d5ca5c93dd850f005352449aaa23b41f62bdb40a871563de69ef3e`;
* `scratch/catalan_pentagonal_connector_rank_separation_20260801.audit.json`,
  SHA `7d7522bc6b1ecc755efdcc234c7da4fca5457a98f50b4c32966bdf6118ce4338`,
  payload `39bc5a7fcb6378235b2d9d8860f70aeb5fca96a826c63594cb93b0b9f6a55b90`;
* `MATH_THEOREM_CATALAN_PENTAGONAL_ROOTED_PORT_PIVOT_AND_LOAD_OBSTRUCTION_20260801.md`,
  SHA `9e2e33c1df56989e24bd2414096dc35a2a1d867132b4498ee02f19fcaf4da9e3`;
* `scratch/catalan_pentagonal_rooted_port_pivot_20260801.audit.json`,
  SHA `ca10637da5a69f52dd2436a69acf47295ef7249270747bca2fd32d5b7ec74253`,
  payload `04a5df5ece1eea46d4a5bd16f1ceadba9141bc60b8f1c226f697b28bd955b285`;
* `MATH_AUDIT_O1_PENTAGONAL_ROOTED_CONNECTOR_FINITE_20260801.md`,
  SHA `6cb04d4c9408ff2f5e494bd70e199bbcfbf28e33f129e665beb344eb17546eed`;
* `scratch/o1_pentagonal_rooted_connector_finite_20260801.audit.json`,
  SHA `82324deb6f1e94947a9b1413c471d316e26446d9ab1dfe114e094406350eab2e`,
  payload `b6a034b305f53f56d8d99bff90641e675a65b850c8bbd050dd1192a42ba7535d`;
* `MATH_THEOREM_H1_SPLIT_LETTER_PROTECTED_CATALAN_FINISH_AND_COMPONENT_TYPE_GATE_20260801.md`,
  SHA `a1755503aff4a5c8fdbf64c92602d50b8b341179726c39aec53fdf05718c677b`;
* `scratch/audit_h1_split_letter_protected_catalan_finish_20260801.py`,
  SHA `ebe7a8dc7ebb679bc118172f6990e53d724a614340c6d71f8efca8b87b0629d8`.
