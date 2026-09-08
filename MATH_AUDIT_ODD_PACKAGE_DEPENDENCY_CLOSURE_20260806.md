# Dependency-closure audit of the odd package

**Date:** 2026-08-06  
**Scope:** composition of balanced midpoint setup, marked/LIFO corridors,
collar-first setup, fixed double-head transport, connector-lattice beta, and
the monotone terminal accumulator  
**Method:** theorem-scope and quantifier audit; no computation or search  
**Verdict:** the **post-beta odd terminal is closed**, but the whole odd
package is not yet unconditional.  One pre-beta anchored-head bootstrap is
still missing.  The dependency is now circular in exactly one place:
the bulk visible-cart theorem assumes a fixed protected double head, while
the only claimed fixed-berth construction of that head invokes a guardable
fully tagged tape produced by the bulk visible-cart theorem.

## 1. Rows which compose without a new hypothesis

The following statements survive the audit.

### 1.1 Midpoint algebra and local paths

`MATH_THEOREM_ODD_BALANCED_MIDPOINT_PACKET_ELIMINATES_RESERVOIR_20260806.md`
and its independent audit prove:

* the exact signed residual count \(t\le3\);
* the packet--collar charge identity;
* all displayed source-to-midpoint and midpoint-to-complement paths; and
* source recovery at every macro checkpoint.

They deliberately leave occurrence-labelled remote transport separate.

### 1.2 Marked/LIFO transport after a cart exists

The corrected stationary-corridor theorem proves every corridor of length at
least two.  A length-one corridor at the common collar is guarded by its two
fixed endpoints.  The corrected two-cross relay

```
X | H | Z -> H | X | Z -> H | M | H -> M | H | H
```

is independently audited.  The noncrossing deletion order and reverse LIFO
finalization ensure that no already finalized target extreme is crossed.

### 1.3 Double-head transport

Once a literal \(H|H=02|02\) is installed at a source-independent protected
berth with its displaced source data recorded, the double-head theorem gives
an occurrence-labelled cart through every macro block.  At each of its two
successive block swaps one head remains fixed.  This closes the finite local
branch collisions found in the old unmarked recoder.

This theorem is an implication **from** a fixed protected head.  It does not
construct that head.

### 1.4 Connector beta

`MATH_THEOREM_ODD_CONNECTOR_LATTICE_BETA_PAIR_20260806.md` gives exact paths
on the true connector lattice for all three first-digit branches.  It needs
no scan-lattice rethread, opposite occurrence, or relay clock.  Its uniform
endpoint is

\[
                   C^*(a_1)\mid C(a_1)\mid H.
\tag{1.1}
\]

### 1.5 Post-beta accumulator

`MATH_THEOREM_ODD_MONOTONE_TERMINAL_ACCUMULATOR_AND_SEVEN_STATE_REGISTER_20260806.md`
proves, from the fully tagged checkpoint and (1.1), one monotone sweep which
consumes the \(t\le3\) residual \(M\)-blocks right-to-left.  It leaves every
completed target behind, ends at exact target-collar mass, orders the collar
at its named berth, and restores every ordinary mark.  The complete
non-guardable endpoint table has six rows, all in nonextreme six-coordinate
mass layers.

Thus there is no surviving **post-beta** opposite-occurrence, residual
placement, one-interior, or collar-order problem.

## 2. The claimed pre-head setup does not yet compose

The load-bearing claim is Theorem 5.1 of
`MATH_THEOREM_ODD_COLLAR_FIRST_DOUBLE_HEAD_SCHEDULING_20260806.md`.
For each external increment it says:

> shuttle only its remote work block to the fixed collar berth; a corridor
> of length at least two uses stationary marks.

The stationary theorem requires every crossed stationary block to lie in

\[
                        \mathcal G=\{20,01,21\}.
\tag{2.1}
\]

Theorem 5.1 does not prove this premise before the double head exists.

### Proposition 2.1 (two-residual ordering obstruction)

Suppose two residual extremes occur at addresses \(x_1<x_2\) measured from
the fixed berth, with only guardable blocks elsewhere.

* If \(x_1\) is processed first, it is returned to its address as
  \(M=11\).  The later shuttle to \(x_2\) crosses this \(M\), which is not
  in (2.1).
* If \(x_2\) is processed first, its outward shuttle crosses the still raw
  extreme at \(x_1\), which is \(00\) or \(22\), again not in (2.1).

Hence no choice of the two processing orders makes both quoted applications
of the stationary-corridor theorem legal.

#### Proof

Both statements follow directly from the linear order of the two addresses.
The stationary theorem's alphabet is exact, and none of \(11,00,22\) belongs
to it.  Scalar fixed-mass connectivity cannot replace the missing occurrence
decoder during that non-guardable crossing.  \(\square\)

The explicit collar-first two-cross relay does not prove Theorem 5.1 in this
scope.  It handles the two packet-to-collar pairs of the unsplit pairing
schedule at the named berth.  The protected zipper setup additionally has
the \(G_1\) half-payment and can have three residual midpoint occurrences.
No theorem turns that whole source-indexed family into guardable corridors
before the head is available.

## 3. The same issue appears as a dependency cycle

The marked-corridor visible-cart theorem reduces the bulk tape recoder to the
finite collar lemma \(\mathsf{DH}\): install a protected fixed \(H|H\), use
it to label all bulk rewrites, and retire it afterward.

The collar-first setup attempts to establish \(\mathsf{DH}\) by first
creating the residual/tagged checkpoint and then using its guardable
corridors to pay for \(H|H\).  But the occurrence-labelled construction of
that checkpoint invokes the visible cart supplied by \(H|H\).  In symbols,

\[
 \boxed{
 \text{fixed protected }H|H
   \Longrightarrow \text{labelled bulk/checkpoint}
   \Longrightarrow \text{guardable fixed-berth setup of }H|H .}
\tag{3.1}
\]

No cited theorem breaks (3.1).

The source-internal bootstrap does not do so: it constructs a stationary
double head at a source-dependent berth, and its own Proposition 3.2 gives
the exact collision

\[
                         ACB\to HHB\to BHH,
             \qquad      BAC\to BHH.
\tag{3.2}
\]

Thus moving both heads away from that adaptive berth without a persistent
origin marker is not occurrence-injective.

The older fixed-collar copy-before-erase construction also does not break
the cycle.  It explicitly assumes an occurrence-labelled private
mass-reservoir path bank, while only scalar component connectivity was
proved.

## 4. Register audit

The seven-state terminal register is sufficient **after** the fixed head or
fully tagged beta signature exists.  Its parity classes

\[
 \{021,201,120,102\},\qquad \{012,210,111\}
\tag{4.1}
\]

each contain at least three states and therefore encode collar order in
either setup parity.

There is one timing caveat.  The states \(120\) and \(102\) are not separated
from the old linkage by the root/boundary coordinates alone.  The terminal
theorem separates them using the fixed-head/fully-tagged phase signature.
It does not yet prove that an arbitrary source can write one of those states
**before** the head/checkpoint exists while remaining disjoint from the old
linkage.  A valid bootstrap may instead:

1. keep the old three safe order states until the fixed head is literal;
2. transfer the record into the required parity class under the new phase
   signature; or
3. supply an independent protected setup parity edge.

This is part of the same pre-head bootstrap, not a post-beta defect.

## 5. Exact remaining theorem

The complete odd package is reduced to the following single row.

### Anchored pre-head bootstrap lemma \(\mathsf{APH}\)

For every decoded odd source, construct pairwise source-disjoint directed
paths which, before invoking double-head transport,

1. install \(H|H\) at a persistent source-independent berth **or** install
   it at an adaptive berth together with a persistent injective origin
   marker;
2. retain the ordered source collar and the setup parity without entering
   the old promotion/aperture linkage;
3. preserve the active \(p_1\) row while performing the protected
   \(G_1\)-half payment;
4. leave every displaced source block occurrence-decodable; and
5. export the fixed cart required by the marked/LIFO bulk theorem.

The construction may use a bounded train containing all at most three
residual extremes, or a persistent marked origin trail.  What it may not do
is invoke the fixed-head visible-cart theorem whose premise it is creating.

### Corollary 5.1 (conditional closure)

If \(\mathsf{APH}\) holds, then the odd package is closed.

#### Proof

Use \(\mathsf{APH}\) to obtain the protected head and order/parity record.
The double-head theorem and marked/LIFO cancellation give the fully tagged
checkpoint.  Transport the head to the connector lattice, apply the exact
beta path, and invoke the monotone terminal accumulator.  The accumulator
writes every residual target and the exact ordered target collar.  Its
seven-state parity theorem retains the literal target endpoint.  Reverse the
remaining LIFO bulk finalizations and apply the already proved root/aperture
retirement.  Every cited theorem now has its hypotheses supplied.  \(\square\)

Without \(\mathsf{APH}\), the implication chain begins at an assumed fixed
cart and is circular.  Therefore the current proof-safe status is

\[
 \boxed{
   \text{odd post-beta terminal: CLOSED};\qquad
   \text{full odd package: OPEN only at }\mathsf{APH}.}
\]

