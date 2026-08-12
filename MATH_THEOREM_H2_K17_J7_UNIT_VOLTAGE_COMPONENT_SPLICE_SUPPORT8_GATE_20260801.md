# The protected J7 path: exact quotient-splice law and a support-eight gate

Date: 2026-08-01  
Lane: H2 / protected J7 physical splice  
Status: **exact bounded obstruction in the frozen MMM quotient cycle.  No
global K17 no-go and no completed owner chronology are claimed.**

## 0. Verdict

Let `C` be the frozen 1430-owner-orbit MMM cycle in
`scratch/k17_mmm_quotient_cycle.tsv`.  It has all 1430 owner orbits once,
all 1430 rank-eight lower-colour orbits once, and total voltage one modulo
17.  Let

\[
 A=7711,\qquad B=8077,\qquad C=13623                 \tag{0.1}
\]

be the orbit representatives of the protected J7 owners

\[
 30844\longrightarrow26750\longrightarrow27246.     \tag{0.2}
\]

Their positions in the frozen cycle are respectively `379,361,896`, so
(0.2) is not already a consecutive block.

There is an exact successor-permutation splice law.  If `sigma` is the old
successor and `S` is the set of tails whose successor changes, every
candidate is a bijection

\[
                       g:S\longrightarrow\sigma(S). \tag{0.3}
\]

It preserves the exact lower rainbow precisely when the new lower labels
on `S` are the old lower labels on `S` as multisets.  Its new permutation is

\[
                       \sigma'=\pi\circ\sigma,       \tag{0.4}
\]

where `pi(sigma(u))=g(u)` on `sigma(S)` and `pi` is the identity elsewhere.
Thus topology is one orbit iff `pi sigma` is one cycle.  If the selected
arc voltages are `delta'_u`, then

\[
 V'=1+\sum_{u\in S}(\delta'_u-\delta_u)\pmod {17}.   \tag{0.5}
\]

In particular one physical lift requires `V' != 0`; preserving the frozen
voltage-one gauge requires the sum in (0.5) to vanish.

The exact finite result is negative before topology, voltage, upper shadows
or residence:

> **No successor exchange changing at most seven tails contains either
> orientation of the J7 path while preserving the frozen owner and
> rank-eight lower-orbit bijections.**

Both path orientations are locally physical: each has a nonempty six-cell
depth-three source with the same certified type triple `(3,7,0)`.  Hence the
obstruction is the global owner/lower splice, not the local J7 source.

The first untested bounded catalogue is therefore the exact support-eight
exchange family.  This is a sharp scoped next gate, not an assertion that a
support-eight exchange exists.

## 1. Labelled quotient arcs

Fix one representative for every owner orbit.  A voltage-labelled quotient
Johnson arc is a triple `(u,v,delta)` for which

\[
                         |u\mathbin\triangle\rho^\delta v|=2. \tag{1.1}
\]

Its lower and upper q1 orbit labels are

\[
 \lambda(u,v,\delta)=[u\cap\rho^\delta v],\qquad
 \upsilon(u,v,\delta)=[u\cup\rho^\delta v].          \tag{1.2}
\]

For a rank-nine owner there are exactly `9*8=72` such labelled moves.  The
frozen cycle supplies a successor `sigma`, one selected voltage `delta_u`
and one lower label `lambda_u` at every tail.  Its `lambda_u` are a
bijection onto the 1430 rank-eight orbits.

### Theorem 1.1 (exact changed-support criterion)

Fix a set `S` and one labelled arc `u -> g(u)` for every `u in S`.  Keep all
old arcs outside `S`.  This gives an owner-bijective, lower-q1-rainbow
quotient cycle exactly when:

1. `g` is a bijection from `S` to `sigma(S)`;
2. the multiset of labels `lambda(u,g(u))`, `u in S`, equals
   `{lambda_u:u in S}`;
3. `pi sigma` from (0.4) has one cycle; and
4. the voltage in (0.5) is nonzero.

If literal residence, type, upper or common-cap states are prescribed, the
chosen arcs must additionally pass those rows; they do not change items
1--4.

#### Proof

Outside `S`, old tails, heads and lower labels are unchanged.  Hence the
new successor is a permutation exactly when the changed heads are precisely
`sigma(S)`, proving item 1 and formula (0.4).  Since the old lower labels
are globally distinct, exact lower coverage is equivalent to replacing the
removed label multiset by itself, proving item 2.  A permutation is a
Hamilton quotient cycle precisely when it has one orbit, proving item 3.
Voltages add around the quotient cycle, and only tails in `S` change, which
gives (0.5).  A quotient cycle over the free `Z_17` action has one physical
lift iff its voltage is nonzero. \(\square\)

## 2. Forced closure of the J7 splice

The exact frozen local data are

| vertex | predecessor | successor | old lower label |
|---|---:|---:|---:|
| `A=7711` | `3983` | `7455` | `3975` |
| `B=8077` | `10211` | `6943` | `6687` |
| `C=13623` | `27243` | `13879` | `7053` |

The forward J7 arcs have voltages `9,7`, lower labels `6687,7053`, and
upper labels `8079,13631`.  The reverse arcs have voltages `10,8` and the
same two palettes in reverse order.

There are two elementary closure rules for any partial exchange.

* If a new arc uses head `v`, then `sigma^{-1}(v)` must lie in `S`, because
  the old occurrence of that head must be removed.
* If it uses lower label `l`, then the unique old tail carrying `l` must lie
  in `S`, because the old occurrence of that label must be removed.

These rules are necessary independently of chronology or voltage.

### Lemma 2.1 (mandatory changed tails)

For the forward path `A -> B -> C`, every exact exchange contains

\[
             \{A,B,C,\sigma^{-1}(B),\sigma^{-1}(C)\}. \tag{2.1}
\]

For the reverse path `C -> B -> A`, every exact exchange contains

\[
             \{B,C,\sigma^{-1}(B),\sigma^{-1}(A)\}.   \tag{2.2}
\]

#### Proof

The path tails themselves must change.  The predecessor rule adds the old
predecessors of the two new heads.  In the forward direction, new edge
`B -> C` uses label `7053`, whose old occurrence is the outgoing edge of
`C`; this additionally forces `C` (already displayed in (2.1)).  Label
`6687` similarly belongs to `B`.  In the reverse direction both reused
labels already belong to the two forced path tails `B,C`, so (2.2) is
complete. \(\square\)

### Theorem 2.2 (support-seven obstruction)

In the frozen MMM cycle there is no owner/lower-rainbow exchange containing
the forward or reverse J7 path with `|S| <= 7`.

#### Proof

Start from (2.1) or (2.2).  For each unassigned changed tail, enumerate its
72 labelled Johnson moves.  Reject a used head or label and apply the two
closure rules above.  A branch stops when the closure exceeds seven.  When
all tails are assigned, require the changed heads and labels to equal
`sigma(S)` and the old labels on `S` respectively.

This enumeration visits 179 forward states and 3001 reverse states.  Both
have zero accepting assignments.  Completeness follows directly from the
closure rules: along any purported solution of support at most seven, its
arc at the next enumerated tail adds only the old predecessor of its head
and the old owner of its label, both already in the final support.  Thus the
solution determines a nonpruned branch of the enumeration.  Since no branch
accepts, no such solution exists. \(\square\)

The labelled catalogue includes rephasings which retain the same successor
*orbit* with a different voltage or lower label.  Excluding these would not
be proof-safe: a tail forced into the closure by a colour constraint can in
principle keep its head orbit while changing its physical quotient arc.

Notice that the test does not need cycle-count, voltage, upper or residence
filters.  Their addition cannot resurrect an empty owner/lower family.

## 3. Literal local state and residence interface

The forward source is

```text
4096,80,10244,16424,26690,512
```

and the reverse source is

```text
512,66,10244,16424,26704,4096.
```

Their length-four OR windows are respectively

```text
30844,26750,27246
27246,26750,30844
```

and their shared length-three ORs are exactly the corresponding lower q1
colours.  Both source words have age-type IDs `3,7,0`, namely

\[
 (3,3,2,1),(5,2,1,1),(1,5,2,1),                    \tag{3.1}
\]

which occur consecutively at positions `20..22` of the frozen pinned type
word.  All six source cells are nonempty.

For the forward owner word the coordinate traces are

```text
000 : 0,7,8,10,15,16
001 : 9
011 : 1
100 : 12
110 : 4
111 : 2,3,5,6,11,13,14
```

and the reverse word exchanges `001/100` on bits `9/12` and `011/110` on
bits `4/1`.  There is no internal `010` trace, so the block has no internally
bounded positive run.

At residence floor four, the exact forward boundary obligations are:

* left continuation at least 3 on bit 12 and at least 2 on bit 4;
* right continuation at least 3 on bit 9 and at least 2 on bit 1; and
* for each all-one bit `2,3,5,6,11,13,14`, at least one positive exterior
  owner in total across the two sides whenever the run is bounded there.

The reverse orientation swaps the left and right obligations.  These are
boundary states, not a claim that a support-eight connector satisfying them
exists.

## 4. Smallest remaining catalogue

The first unclosed fixed-cycle class consists of all labelled exchanges
`(S,g,delta)` with `|S|=8` such that:

1. `S` contains (2.1) or (2.2), and `g` contains the corresponding two J7
   arcs;
2. the changed-head and changed-lower bijections of Theorem 1.1 hold;
3. `pi sigma` is one cycle and (0.5) is nonzero (or equals one if the old
   gauge is to be retained);
4. every new upper q1 label is charged against the literal removed/provider
   ledger, with the two J7 labels `8079,13631` retained;
5. the boundary states in Section 3 compose at both sides; and
6. the selected type partitions, protected banks, deeper upper witnesses
   and common-cap tickets survive.

Equivalently, support eight adds three auxiliary changed tails to the
forward mandatory set or four to the reverse mandatory set.  Searching this
catalogue is strictly smaller and more exact than another global owner SAT
run.  A different owner cycle, a reselected lower matching, or a forest
embedding lies outside the theorem and may avoid the support-eight floor.

## 5. Reproducibility and scope

The independent lightweight replay is

```text
scratch/audit_h2_k17_j7_unit_voltage_component_splice_20260801.py
scratch/h2_k17_j7_unit_voltage_component_splice_20260801.audit.json
```

It reads only the frozen MMM quotient cycle, the pinned type word and the
prior local J7 audit.  It does not launch a solver or modify the active H100
global master.

The result is a no-go only for successor exchanges of support at most seven
inside this one fixed owner/lower-rainbow cycle.  It proves neither that a
support-eight exchange exists nor that J7 cannot be embedded in another
cycle, a prospectively selected factor, or a larger nonlocal chronology.
