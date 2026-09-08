# Audit of the complete radius-one Steiner path on the six-swap `K17` forest

Date: 2026-07-31  
Status: independently replayed finite theorem in the trusted-CP-SAT scope;
no residual `b`-flow, connected carrier, upper-shadow theorem, or compiler
is claimed

## 0. Result

Let `M` be the frozen six-occurrence repaired macro forest in

```text
scratch/k17_sixswap_macro_forest_20260731.flow.json.
```

Its `106` marked components contain `154` macros and `3815` owner tokens;
each marked component is internally `D2>=3,D3>=4` clean.  A radius-one
Steiner packet is either

1. one clean old-`U` connector from one oriented marked component to
   another, or
2. two clean old-`U` connectors through exactly one clean unmarked fixed
   component.

The complete directed catalogue has

```text
marked components                                      106
clean unmarked components                             4817
direct geometric / clean packets                  412 / 312
one-optional geometric packets                         19556
  repeated-U rejection                                  1852
  literal residence rejection                           6484
  endpoint-capacity rejection                               0
one-optional clean packets                              11220
all clean packets                                       11532
optional components represented                          2133
old-U labels represented                                 1286.
```

The exact path master returns

\[
                    \boxed{s_{\min}=28}                 \tag{0.1}
\]

within this complete radius-one catalogue.  Its witness uses `77` direct
packets and `28` one-optional packets.  The selected optional components
are `16` isolated ports and `12` nontrivial components containing `17`
macros and `160` owners.  Literal replay gives one path through all `106`
marked components with

```text
selected old-U owners                      133, all distinct
selected optional components                28, all distinct
expanded owner tokens                     4108, all distinct
internal D2 bad runs                          0
internal D3 bad runs                          0
endpoint-capacity violations                  0.
```

The saved CP-SAT response has `status=OPTIMAL`, objective `28`, and best
bound `28`.  The audit below independently reconstructs the complete
catalogue and checks the exact model and witness.  It does **not** provide
a DRAT/LRAT certificate for the objective-`<=27` face, so (0.1) has the
usual trusted-exact-solver scope rather than proof-producing-SAT scope.

## 1. Complete packet theorem

Every nontrivial fixed component is a port path.  An orientation determines
its head port, tail port, and expanded owner word.  A trivial component is
one isolated port with empty owner word and one orientation.  Two rank-eight
ports `S,T` admit an old-`U` connector precisely when

\[
 |S\mathbin\triangle T|=2,
 \qquad U=S\cup T\in\binom{[15]}9.                      \tag{1.1}
\]

### Theorem 1.1 (catalogue completeness)

The saved `11532` rows are exactly all clean directed packets with zero or
one unmarked internal fixed component, distinct old-`U` labels inside the
packet, and legal endpoint capacity.

### Proof

For each of the two states of a marked component, enumerate every Johnson
neighbour of its tail port.  If the neighbouring port is the head of a
marked state, (1.1) gives every direct packet.  If it is the head of a clean
unmarked state, enumerate every Johnson neighbour of that state's tail and
then every marked state headed there.  This enumerates every radius-one
quotient path and no other geometry.

Reject a two-edge row when its two unions are equal.  Count connector
incidences at every port and compare them with `2-deg_M(T)`.  Finally expand
the entire literal owner word and enumerate every internally bounded
positive run in the owner word and its adjacent-union derivative.  This is
exactly the `D2>=3,D3>=4` test.

An unmarked component having an internal bad run cannot become clean by
adding symbols outside it: both bounding zeroes of that run already lie
inside its owner word.  Hence restricting the intermediate component to the
`4817` independently clean components loses no clean packet.

The independent reconstruction obtains the counts in Section 0 and its
packet-key set is byte-for-byte equal, up to ordering, to the saved packet
key set.  There are no duplicate keys.  \(\square\)

## 2. Exact radius-one marked-path model

Use a Boolean `x_p` for every packet, two orientation Booleans for every
marked component, and one start and one end Boolean for each marked
component.  Add a dummy vertex and use one circuit constraint on

* every packet arc from its left marked component to its right marked
  component;
* every dummy-to-marked start arc; and
* every marked-to-dummy end arc.

No self-loop is supplied.  Thus the circuit consists of one dummy-broken
path containing all `106` marked vertices and exactly `105` packet arcs.
Each packet implies its two endpoint orientations.  For each old-`U` label,
at most one packet containing that label is chosen.  For each unmarked
component, at most one packet using it is chosen.  Minimize the number of
chosen one-optional packets.

The emitted model ledger is

```text
packet variables                                      11532
orientation variables                                   212
start/end variables                                      212
total Boolean variables                                11956
orientation exactly-one rows                             106
orientation implications                              23064
old-U at-most-one rows                                  1286
optional-component at-most-one rows                    2133
one circuit row                                            1
objective literals                                    11220.
```

### Lemma 2.1 (implicit port capacity is exact)

No additional global port-capacity row is missing from this model.

### Proof

Every marked component is nontrivial.  A consistent orientation makes its
incoming packet use its head port and its outgoing packet use its distinct
tail port.  Thus every marked endpoint receives exactly one connector.

A selected nontrivial optional component is traversed once and uses each of
its two endpoint ports once.  A selected isolated optional component uses
its unique port twice; this is checked in the packet row against its
capacity two.  Optional-component all-different prevents another selected
packet from touching either kind of optional component.  Fixed components
partition the port deck, so there can be no cross-component port collision.
\(\square\)

### Lemma 2.2 (local packet cleanliness composes)

If every selected packet is clean and its marked endpoint orientations are
consistent, then their concatenated marked path is clean.

### Proof

A bad run meeting only one side of a shared marked word is already internal
to the corresponding incoming or outgoing packet and was rejected.  A run
which crosses both sides must contain that entire marked word.  The shortest
marked word has eight owners.  Such an owner run therefore has length at
least eight, and the corresponding adjacent-union run has length at least
seven; neither can violate thresholds three and four.  A zero inside the
marked word separates the two sides.  Thus no new short run is created by
composition.  \(\square\)

### Theorem 2.3 (model equivalence)

Feasible solutions of the Boolean model are in bijection with simple clean
radius-one packet paths through all marked components, with distinct old-`U`
labels and distinct optional components.  The objective is exactly the
number of optional components used.

### Proof

The dummy circuit supplies one ordered path through every marked vertex.
The implications give one consistent orientation at each vertex.  The two
families of at-most-one rows enforce precisely the non-port resources, and
Lemma 2.1 supplies port capacity.  Lemma 2.2 supplies literal cleanliness.
Conversely, orient and order any such physical packet path; its arcs plus
the two dummy arcs satisfy the circuit and all resource rows.  Each packet
contains at most one optional component, and those components are distinct,
so the objective is their number.  \(\square\)

## 3. The optimum-28 witness and its limit

The saved solution selects `105` packet indices and orders all `106` marked
nodes without repetition.  Independent expansion checks the endpoint
orientations, all `133` old-`U` labels, all `28` optional components, every
port load, and every owner token.  The expanded word has SHA-256

```text
b0eda9200ff287c6406d880b958c66521371d9b4a44b6b4c1db1dbc8473063e3
```

under canonical JSON serialization and has zero internal `D2/D3` debt.

The solver log raises its lower bound through

```text
0, 2, 16, 25, 27, 28
```

and terminates with objective and bound both `28`.  This proves (0.1) in the
trusted CP-SAT scope because Theorem 2.3 proves the model is exact for the
radius-one class.  It is important not to silently upgrade this to a
proof-producing lower certificate.

For comparison, the direct clean graph alone has five connected components
of sizes

```text
99, 2, 2, 2, 1
```

and degree profile containing `23` leaves and one isolated marked vertex.
Even after optimally placing the two path endpoints, these vertices force at
least `23` optional incidences, hence at least `12` optional packet edges.
This elementary bound is valid but far weaker than `28`; it does not explain
the full integral correlation detected by the exact path master.

## 4. Capacity-neutral residual ledger

The selected path contains `106+28=134` fixed components and uses
`105+28=133` old-`U` connectors.  Therefore

\[
 \begin{aligned}
 \#\text{remaining old-}U\text{ owners}&=5005-133=4872,\\
 \#\text{remaining fixed components}&=5005-133=4872,\\
 \sum_T d(T)&=10010-2(133)=9744=2(4872).
 \end{aligned}                                           \tag{4.1}
\]

So the Steiner enlargement remains scalar capacity-neutral.  Equation
(4.1) is not a residual matching theorem.  The next exact tests are:

1. conditioned owner-to-halfport Hall for these specific `133` deleted
   owners and connector incidences;
2. selection of pairs, rather than only half-incidences;
3. connected quotient closure of the remaining `4872` components; and
4. upper/deep service, complementary chronology, and one common-cap
   compiler.

## 5. Frozen files and hashes

```text
scratch/k17_sixswap_macro_forest_20260731.flow.json
SHA-256 4e3129d2604d3e41c226efa3bea71a203180538710dd97272cc734e23412441b
payload f1ab56555d744d2e527325c8617c2af1ee0f463ad13666f153d56efc588624db

scratch/solve_ad_k17_sixswap_oneoptional_marked_path_20260731.py
SHA-256 6f151aab87eae0df6be0ee9d1fbbcb0d131df9f7c28ee580250216cd06e52444

scratch/ad_k17_sixswap_oneoptional_catalogue_20260731.json
SHA-256 b803899bbf07b3cbc82e995c9fd1f6231e6eba679d6a60e4a447cb36c08e71f2
payload 58beedb46ec289b1059b11c095fc86e1e174fab8ad150a854c2c53eb7fe5ea0b

scratch/ad_k17_sixswap_oneoptional_marked_path_20260731.result.json
SHA-256 b60341b5cee0de1884d3af6561d8247722bad879d7b5322ca21d94f60472e351
payload 2440ee4a506932c4e7903dc327a6c8445c5c3c7b310c0e748d4520566c14ffae

scratch/ad_k17_sixswap_oneoptional_marked_path_20260731.stdout.log
SHA-256 9f4b2d8b0b5821321c335c55adceed6bdb3dc9da36bd8116329b560e2ab90675

scratch/ad_k17_sixswap_oneoptional_marked_path_20260731.stderr.log
SHA-256 516ebcf09345956e36e8eaaf905583bff3d197fe936523f06f9b34e4338bfcff

scratch/audit_ad2_k17_sixswap_full_radius1_steiner_path_20260731.py
SHA-256 3a2f40110bd9f2777f9674cc23eb285de52c46f39b9a84d25ca9f7c426270e59

scratch/ad2_k17_sixswap_full_radius1_steiner_path_20260731.audit.json
SHA-256 46f14750ef52060a39c609b2499dc1c4cadf8034a7e847ceeecdaf66ba35b7ad
payload f6d1b2bce709085c1d0ee019c9abd60e3bfe8c8f7bb16ac2ecc5ddda78b71be2
```

The audit script imports neither the catalogue builder nor OR-Tools.  It
reconstructs the full packet key set from the fixed forest and separately
replays the saved path.
