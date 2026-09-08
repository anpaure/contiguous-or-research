# The protected four-state register carries the odd collar order through beta

**Date:** 2026-08-06  
**Method:** copy-before-erase into the root/boundary register, exact parity
coupling, and the connector-lattice beta junction; no computation or search  
**Status:** **SUPERSEDED FOR TERMINAL USE** by
`MATH_THEOREM_ODD_MONOTONE_TERMINAL_ACCUMULATOR_AND_SEVEN_STATE_REGISTER_20260806.md`.
The collar-order copy below remains valid, but its separate corridor-parity
mark and opposite-occurrence conclusion are unnecessarily strong.  The
seven-state refinement encodes order in either parity class, and the returned
beta copy is used directly as collar compensation in one monotone sweep.

## 1. The collar order has multiplicity at most three

Let the ordered source collar be `(a,b) in {0,1,2}^2` and put `s=a+b`.
The exterior residual/central ledger determines `s`.  The ordered pairs in
each fibre are

```
s=0: (0,0)
s=1: (0,1),(1,0)
s=2: (0,2),(1,1),(2,0)
s=3: (1,2),(2,1)
s=4: (2,2).
```

Thus only a three-valued order-class record is needed once `s` remains
externally readable.

Use three states of the already proved protected root/boundary register:

```
Q0=021,
Q1=012,
Q2=201.
```

All have mass three and avoid the old linkage.  Normalize the register to
`Q0` while the old collar or old `p_1` row is still literal.  Encode each
fibre in the displayed order:

```
s=0: (0,0) -> Q0
s=1: (0,1) -> Q0, (1,0) -> Q1
s=2: (0,2) -> Q0, (1,1) -> Q1, (2,0) -> Q2
s=3: (1,2) -> Q0, (2,1) -> Q1
s=4: (2,2) -> Q0.
```

The writing paths from `Q0` are

```
Q0=021,
Q0=021 <-> Q1=012,
Q0=021 <-> 111 <-> Q2=201.
```

Their physical-edge parities are respectively

```
rho=0,1,0.
```

The fourth state `210` is unnecessary.

### Lemma 1.1 (literal collar-order copy)

While the selected `p_1` row is still the old collar record, the paths above
copy the ordered pair `(a,b)` into `(s,Q_i)` without merging two source
paths.  Once the copy is complete, `(s,Q_i)` remains an injective collar
record even if the `p_1` row changes.

#### Proof

During record writing, the old unordered `p_1` row together with `s`
recovers `(a,b)`.  The register path is at a fixed physical address, and its
current literal state determines the microstep.  Hence two writing paths can
meet only when their old collar records already agree.

At the endpoint, the table above is injective within each fixed `s`.  The
exterior residual/central ledger separates different values of `s`.
Therefore `(s,Q_i)` recovers the ordered collar after the old row is erased.
\(\square\)

## 2. The beta phase frees the old pass and branch semantics

At the beta checkpoint the global phase is already literal:

* the ordinary extreme tape is fully tagged;
* the connector head train is present at its declared berth or at `p_1`;
* the mixed first connector has the beta source value; and
* the residual midpoint/tag ledger is fixed.

These signatures distinguish beta setup, local conversion, marked return,
and target completion.  Consequently the two bits formerly called *pass*
and *branch* are not needed for their old operational meanings during this
bounded phase.  Holding `Q_i` fixed does not remove any decoder used by the
connector-lattice beta paths: their ordered local type is determined by
`a_1`, which follows from the signed residual count and `s`.

The register is disjoint from `p_1`, the connector head train, and the
marked work corridor.  Every register-writing edge therefore has its usual
directed two-arc lift through the still-active `p_1` clock.  Its only effect
on the clock is the known parity `rho` above.

## 3. Exact connector-lattice beta junction

Use consecutive coordinates

```
g,b,v,u,w
```

with

```
p_1=(g,b),
C_1=(b,v),
C_2=(u,w).
```

Keep a second connector head `C_3=H=02` fixed beyond `C_2`.  The exact
full-matching paths are

```
a_1=0:
10202 => 01211 => 11111 => 02201
      => 11210 => 21110 => 12200,

a_1=1:
12002 => 21011 => 12020,

a_1=2:
12002 => 02102 => 11012 => 01112 => 10022.
```

At every physical intermediate, `p_1` is selected nonquiet, and the next
arrow is exactly its forced selected edge.  Directly reading endpoints gives

```
C_1 = C*(a_1),
C_2 = C(a_1),
C_3 = H,
p_1 = c(B_1*).
```

Thus the first connector is restored to its exact complemented code and the
connector-aligned return train is

```
C(a_1) | H.
```

The `a_1=1` and `a_1=2` paths share their initial local state.  They are
still disjoint globally because the fixed signed residual count and the
collar-order register recover `a_1`; these values are not changed by the
local junction.

## 4. Coupling register parity to corridor parity

Every swap of a two-block train past one two-coordinate block has even
weighted token-position parity.  Every stationary mark

```
Y -> mu(Y),   Y in {20,01,21},
```

is one physical edge and has odd parity.  Hence only the number of written
marks changes the endpoint of the selected `p_1` row.

Let `L` be the number of ordinary guardable blocks crossed by the outward
head train.  When `L>=1`, choose either all `L` blocks or all but the
berth-adjacent block to be marked.  These two choices have opposite parity.
Choose the marked count `h` so that

```
rho + h = 0 mod 2.
```

The outward double head safely crosses the optional unmarked endpoint block.
On return, the named fixed berth guards the corresponding last unmarked
train/block interchange.  For a marked corridor of length at least two use
the stationary-corridor train theorem; marked lengths zero and one are the
already bounded fixed-end cases.

If `L=0` and `rho=1`, store one reversible mark on any disjoint fully tagged
ordinary block.  It cannot preempt the beta matching: every physical
intermediate of the connector-lattice junction has `p_1` nonquiet.  For all
sufficiently large odd instances, the bounded beta/collar support leaves an
ordinary tagged block available; the finitely many smaller instances are
already inside the verified finite range.

### Lemma 4.1 (literal beta entry and return endpoint)

After writing `Q_i`, the parity choice above brings the connector head train
to the local beta source with the literal required endpoint of `p_1`.  The
connector-lattice junction therefore applies exactly.  Returning
`C(a_1)|H` across the still-marked corridor uses only even train/block swaps,
so at the returned-train checkpoint `p_1` is still at its literal target
endpoint.

#### Proof

The record path contributes `rho`; the outward train swaps contribute zero;
the `h` marks, including the optional isolated mark, contribute `h`.  By
construction their sum is even.  The local beta path begins at the required
literal source.

No mark is erased before the return train reaches the berth.  Every return
train/block swap is even, so the local target endpoint persists through that
checkpoint.  The fixed register and un-erased marks still record source and
stage.  \(\square\)

## 5. Copy is erased only after the target collar is literal

At the returned-train checkpoint retain both `Q_i` and every parity/corridor
mark.  The pair `(s,Q_i)` still recovers the ordered source collar, while the
train supplies the compensating value `C(a_1)` and one remaining head.

Run the final bounded compensating-occurrence assignment.  Only after it has
written the complete literal target collar

```
C*(a) | C*(b)
```

may the register be returned to its idle state.  Erase the record path and
the retained marks in the parity-paired order.  Their total parity is

```
rho+h=0 mod 2,
```

so, apart from the already fixed parity of the final bounded assignment,
they do not disturb the target endpoint of `p_1`.

This is copy-before-erase in the literal sense: the old `p_1` row labels the
write, `(s,Q_i)` labels beta and the return, and the target collar labels the
record erasure.

## 6. Exact remaining gate

The theorem proves all of the following without an anonymous reservoir or
external relay clock:

1. a three-state literal copy of the ordered collar;
2. exact directed beta paths on the true connector lattice;
3. endpoint-parity-correct outward and return transport; and
4. preservation of the record until the target collar is available.

What it does **not** prove is the final bounded assignment itself.  One must
still:

1. choose the opposite source occurrence whose complemented target is
   `C(a_1)`;
2. route the returned `C(a_1)` to that occurrence while routing the last
   `H` and every midpoint/interface exception to their target states; and
3. keep the physical corridor guardable, or give a finite visible-cart table
   for the bounded non-guardable exceptions.

Global charge proves that a target occurrence of the required sign exists.
It does not by itself give the occurrence-labelled routing in items 2--3.
This bounded compensating-occurrence router is the sole remaining odd row.
