# Independent audit: collar-first scheduling is repairable; endpoint-bit and relay-beta claims fail

**Date:** 2026-08-06  
**Files audited:**

* `MATH_THEOREM_ODD_ENDPOINT_BIT_ONE_INTERIOR_REGISTER_20260806.md`;
* `MATH_THEOREM_ODD_COLLAR_FIRST_DOUBLE_HEAD_SCHEDULING_20260806.md`;
* `MATH_THEOREM_ODD_RELAY_CLOCK_TERMINAL_BETA_COLLAR_20260806.md`.

No computation is used.

## Verdicts

1. **Selected-row endpoint-bit theorem: FAIL.**  The endpoint of the active
   selected row is not a freely writable bit at a fixed work checkpoint.
   It is coupled to the parity of physical work moves.  Its decoder also
   uses the active address to recover the microstep and the microstep to
   recover the active address.
2. **Collar-first schedule: correct strategy, but INCOMPLETE AS WRITTEN.**
   The maximal-pair count is true and the fixed-berth guard proves the
   one-cross length-one case.  The displayed cross path has the wrong
   endpoint orientation when the packet approaches the collar from the
   left, and the two-cross case needs one additional guarded three-block
   relay.  That relay has a short explicit macro construction, so this is a
   repair rather than a new asymptotic gate.
3. **Prepared relay-clock beta theorem: FAIL.**  The state `11` of `p_1` is
   selected nonquiet, not quiet.  More fundamentally, the shadow-clock lift
   applies only to work disjoint from the clock, while the displayed beta
   paths change `B_1`, a coordinate of `p_1`.  The forced matching edge
   changes `B_1` again and immediately leaves the displayed path.

Thus the generic one-interior problem can plausibly be removed by a corrected
collar-first schedule, but the terminal beta-collar remains open.

## 1. Why the selected-row endpoint is not a free second bit

At a majority checkpoint, one physical work edge is followed by the selected
matching edge.  The matching edge toggles the endpoint of the selected
`p_1` row.  Therefore

```
endpoint parity = initial endpoint parity XOR number of physical work edges.
```

This is not an independent register: it is the bipartite parity record of the
work route.

The coupling is already visible in the protected boundary register.  At
fixed pass, changing the branch state

```
E_00 <-> E_01    or    E_10 <-> E_11
```

uses one physical edge.  Its directed two-arc lift necessarily toggles the
selected `p_1` endpoint.  Hence, with the rest of the checkpoint fixed,
`branch XOR endpoint` is fixed.  The four formal pairs `(b,e)` do not give
four independently reachable checkpoint states.

One cannot toggle only the selected endpoint by taking its matching edge:
that edge is the forced minority-to-majority half of a directed lift.  An odd
work route can toggle the endpoint, but it leaves the work tape at the other
side of the bipartition.  If that changed work state is retained, it—not the
endpoint alone—is the additional physical marker and it needs its own
decoder and restoration proof.

Accordingly, Section 2's instruction to “choose the required endpoint `e`”
is an unproved operation.

## 2. The endpoint decoder is circular

For a fixed physical address and fixed branch, simplicity of a chosen local
path identifies its microstep from the literal state of the active window.
But the theorem has two possible addresses and introduces the endpoint bit
precisely because the active window is otherwise unlocated.

Its proposed decoder has the cycle

```
address -> extract active local window -> identify microstep/parity
        -> recover initial endpoint -> recover address.
```

To break that cycle one must prove joint injectivity of

```
(address, microstep)
  |-> (full literal work state, current selected-row endpoint),
```

for every path in the finite bank.  Neither simplicity of each local path nor
the parity formula proves this cross-address assertion.

The old checkpoint collision `ABCB -> ACBB` illustrates the issue.  A
freely selectable opposite endpoint can separate that particular completed
block swap because the swap has even token-graph parity.  But the endpoint is
not freely selectable, and the strict states of all address-indexed paths
were not compared.  Thus the example is not repaired by the argument as
written.

The cross-remainder count used in the note is sound: after maximal internal
pairing, at most two packet-to-collar pairs remain.  The packet itself has at
most four extreme blocks, so at most two internal packet pairs exist.  The
two-cross train, however, has a gathering stage and a collar-transport stage;
those stages would need separate literal phase labels if one retained the
endpoint-bit approach.

The endpoint-bit file has correctly been superseded by collar-first
scheduling.

## 3. Exact audit of the maximal collar-first pairing

Let `c` be the signed charge of the two collar blocks and let
`e_1 in {-1,0,1}` be the first-connector charge.  The residual bank has
charge `-(e_1+c)` and consists only of extremes of that sign.  A direct case
split proves the claimed bound.

* If `|c|=0`, an opposite extreme collar pair is used internally.  If
  `e_1=0`, the packet has no extremes.  If `|e_1|=1`, the first connector
  and the unique residual extreme form one opposite pair.
* If `|c|=1`, one collar position is extreme.  Maximal cross-pairing removes
  one opposite packet extreme.  For `e_1` opposite to `c` or zero, nothing
  remains; for `e_1` with the sign of `c`, exactly one opposite packet pair
  remains.
* If `|c|=2`, both collar positions have the same extreme sign.  Cross-
  pairing removes two opposite packet extremes.  Nothing remains unless
  `e_1` has the collar sign, in which case one opposite packet pair remains.

Therefore the conclusion of Lemma 1.1 is true: after the collar is paid,
there is at most one delayed internal packet pair.  The proof in the theorem
should use this packet-specific case split; total charge and a raw size-four
bound alone would allow an abstract four-element balanced packet.

## 4. The single-cross fixed-berth guard passes, with an orientation correction

For one intervening block, the support has the fixed physical form

```
packet X | interior Y | collar Z.
```

While a simple fixed-mass path swaps `X|Y`, the untouched `Z` at a named
physical berth locates the active four-coordinate window.  After the cross
conversion, the collar head at that same berth guards the inverse shuttle of
the packet midpoint.  Local mass and the existing branch distinguish the
ordered endpoint type; simplicity then gives the microstep.  This is a valid
visible-cart proof in both directions.

However, after the packet reaches the collar, its order is `X|Z`.  The
midpoint must be

```
X|Z -> M|H,
```

so that `M` occupies the packet-side position and `H` occupies the collar
berth.  The displayed paths in the midpoint theorem are written as
`A|C -> H|M` and `C|A -> H|M`; those have `H` in the first position.  One
must use the appropriate spatially reflected branch to obtain `M|H` when
the packet approaches from the left.  Without this correction, the sentence
“the new H remains fixed at the collar berth” is false.

## 5. The two-cross collar case needs one explicit relay

If both collar extremes are cross-paired and the work tape approaches an
adjacent two-block collar from one side, processing the nearer collar block
first leaves

```
... | H | Z
```

at the berth.  The second packet block cannot reach `Z` through a word over
only `20,01,21`, because the first `H` lies between the work tape and `Z`.
Thus Theorem 2.1 as currently written does not cover its own second cross
operation.

There is a short repair.  Once the second packet extreme `X` has reached the
near side, use the guarded macro route

```
X | H | Z
 -> H | X | Z
 -> H | M | H
 -> M | H | H.
```

In the first interchange, the literal far collar `Z` is fixed; in the cross
conversion, the left `H` is fixed; in the last interchange, the right `H` is
fixed.  Every active fixed-mass token graph is nonextreme.  Choosing the
cross branch with endpoint `M|H` gives the required midpoint.  These three
fixed guards provide the occurrence label at every strict state.  Reversing
the route gives the teardown of the far cross pair; the remaining near cross
pair is then the single-cross case.

Adding this relay, the orientation correction in Section 4, and an explicit
statement that the far pair is torn down first would make the collar-first
schedule proof-safe.  The delayed packet-packet pair is correctly processed
while the literal double head still exists.

## 6. The relay-clock classification is wrong

The three selected nonquiet rows are

```
01 <-> 10,
02 <-> 11,
12 <-> 21.
```

In particular, `11` is selected **nonquiet**.  It is not a quiet state at
which priority passes from `p_1` to `p_2`.  Therefore the central assertion
of Lemma 2.1 in the relay-beta note contradicts the exact scan matching.

There is an even more direct failure.  The shadow-clock compilation theorem
requires the physical work support to be disjoint from the scan prefix
through the selected clock.  The paths

```
020 -> 011 -> 002,
022 -> 112 -> 121 -> 211 -> 220
```

change `B_1`, which is a coordinate of `p_1`; they are not eligible shadow-
clock work paths.

The forced matching dynamics leave the displayed paths immediately:

* On the `a_1=0` branch, the physical edge `020 -> 011` makes
  `p_1=11`.  Since `11` is first nonquiet, its matching edge is
  `11 -> 02`.  At the next majority checkpoint the local three-coordinate
  value is `012`, not `011`, so the advertised next edge `011 -> 002` is
  unavailable.
* On the `a_1=2` branch, the physical edge `022 -> 112` leaves
  `p_1=12`.  Its matching edge is `12 -> 21`, changing `B_1` from two to
  one.  The next majority local value is `111`, not `112`, so the
  advertised next edge is again unavailable.

Preparing `p_2` does not repair either branch because `p_1` never becomes
quiet at the claimed handoff.  The statement that the two rows have freely
choosable starting endpoints is also incompatible with the fixed source
state `p_1=(1,B_1)`.

## 7. Additional relay prerequisites are not supplied

Even apart from the fatal local dynamics, the note does not construct:

1. a source-decodable path which puts `p_2` into a chosen selected row while
   preserving its old literal value for later restoration;
2. a proof that all scan pairs between `p_1` and the relay are quiet;
3. a schedule reconciling “complete every other collar conversion near
   `p_1`” with the collar-first teardown at the fixed berth; or
4. a target-collar return corridor containing only `20,01,21`.

The fourth point is load-bearing.  Finalizing the delayed packet pair or a
cross-paired packet before returning the collar can place literal target
extremes `00` or `22` in that corridor.  The stationary-corridor theorem
does not allow those values in its guard alphabet.  An ordering or a new
visible-cart return must prove that they are absent or can be crossed.

The raw source-decoding arithmetic in Section 3 is otherwise sound: the
local mass distinguishes the two nontrivial `a_1` branches, and the signed
residual count plus one physically ordered target collar digit recovers the
other collar digit.  That informational fact does not create a directed
path.

## 8. Proof-safe frontier

After the explicit two-cross correction, collar-first scheduling removes the
generic one-interior shuttle without an endpoint register.  The terminal
beta-collar is still a finite problem, but it needs a genuine path in the
full matching contraction.  It cannot be obtained by lifting a physical
path that touches `p_1` through `p_1` itself.

The correct remaining task is a literal finite-state beta handoff which
either makes `p_1` genuinely quiet before touching `B_1`, or installs an
earlier protected clock whose support is disjoint from the beta work, and
then gives an occurrence-labelled collar return in the actual teardown
order.

