# Flat endpoint wrapping: an exact `B+1` no-go and the `B+2` two-stutter palette

Date: 2026-08-01  
Lane: split-pivot endpoint host / additive constant  
Status: exact flat owner-palette theorem and exact local-deck blueprint.  The
`B+2` source/common-cap realization and arbitrary-width upper return remain
open.

## 0. Outcome

The prepared-endpoint wrap cannot be performed in a frozen flat `B+1`
carrier.  The obstruction is only two colours, but it is exact: the wrap
drops the two endpoint coatom owners omitting `f_1` and `f_d`, while every
new seam window contains both `f_1` and `f_d`.  A flat `B+1` row has only one
surplus occurrence, so at most one of those two owners can have a retained
duplicate.

At `B+2`, two core-only stutters give the sharp **new-seam** palette which
the count predicts:

\[
       U,\ D_{d-1},D_{d-2},\ldots,D_2,\ U,                  \tag{0.1}
\]

where `U` is one rank above the middle owner layer and
`D_j=U-{f_j}`.  Relative to the prepared old bank
`D_d,...,D_1`, this is the signed exchange

\[
                       D_1+D_d\longmapsto 2U.               \tag{0.2}
\]

Owner coverage therefore closes at `B+2` only when the untouched bank
retains one extra occurrence of each endpoint coatom `D_1,D_d`.  A stronger
literal dropped/gained-bank equality is available if the old cut is supplied
with an independent second copy of the complete `Q^-|P^+` collar.  That
second seam is an additional host hypothesis, not a consequence of the
prepared global endpoints.

This is a **palette-level boundary design**, not yet a word theorem.  The
two stutter letters must occur in one legal source/common-cap state, and
upper crossing intervals extending beyond the collar still need tickets.

## 1. Flat recut bookkeeping

Let a source word have length

\[
                            L=W+d+c,                         \tag{1.1}
\]

so its flat width-`d+1` row has `W+c` windows.  Assume it covers all `W`
middle owners.  A cyclic block rotation changes only the windows crossing
the old and new cuts; in the endpoint wrap exactly `d` old windows are
dropped and `d` new cyclic windows are gained.

For `c=1`, there is one occurrence beyond the first occurrence of every
middle owner.  This occurrence may be a duplicate owner or a nonmiddle
window, but it can protect at most one owner whose designated boundary
occurrence is dropped.

## 2. The exact `B+1` obstruction

Let `C` be the common active aperture, let

\[
 F=\{f_1,\ldots,f_d\},\qquad
 U=C\cup F,qquad D_j=U-\{f_j\}.                             \tag{2.1}
\]

The full prepared left endpoint has the `d` owner windows which, after the
reverse filler orientation needed by the split seam, are

\[
                         D_d,D_{d-1},\ldots,D_1.             \tag{2.2}
\]

These are the `d` windows dropped when the full prepared prefix is rotated
to the other end.

The new seam has bases

\[
                    Z=A\cup\{f_1\},\qquad
                    T=B\cup\{f_d\},\qquad A\cup B=C.         \tag{2.3}
\]

Every gained width-`d+1` window crosses this seam.  Therefore it contains
both `Z` and `T`, and in particular contains both `f_1` and `f_d`.

### Theorem 2.1 (flat `B+1` endpoint-wrap no-go)

No flat length-`B+1` endpoint wrap with the prepared dropped bank (2.2) can
retain the complete middle-owner palette.

#### Proof

The two dropped owners `D_1` and `D_d` omit `f_1` and `f_d`, respectively.
Every gained window contains both endpoint fillers, so neither gained
window can equal either owner.

If both `D_1` and `D_d` had retained occurrences outside the dropped bank,
the old row would have at least two occurrences beyond the first occurrence
of every one of the `W` owner values.  A `B+1` flat row has only one surplus
window.  Hence at least one of `D_1,D_d` has no retained occurrence and no
gained occurrence.  It is missing after the recut.  \(\square\)

This theorem does not obstruct a nonflat deadline staircase: one of these
owners may survive on a transported interval of width `d+2`, exactly as in
the split-letter theorem.  It forbids only postprocessing a frozen flat
owner row.

## 3. The two-stutter seam

Let `K` be any nonempty subset of the active aperture `C`.  Define two
length-`d` source collars

\[
 \begin{aligned}
  Q^-&=(\{f_{d-1}\},\{f_{d-2}\},\ldots,\{f_2\},K,Z),\\
  P^+&=(T,K,\{f_{d-1}\},\{f_{d-2}\},\ldots,\{f_2\}).       \tag{3.1}
 \end{aligned}
\]

The `K` immediately before `Z` is a left-ray stutter; the `K` immediately
after `T` is a right-ray stutter.  The owner-window calculation below needs
only `K subset C`.  The exclusive rays retain the canonical bases `A` and
`B` **if and only if** `K subset A intersection B`; otherwise their bases
are enlarged to `A union K` and `B union K`.  Under the shared-core
condition, ignoring the repeated value created by each stutter, the rays
still contain every canonical target

\[
                       A\cup P_q,\quad B\cup S_q,
                         \qquad2\le q\le d.                  \tag{3.2}
\]

### Theorem 3.1 (exact crossing palette)

The `d` consecutive width-`d+1` windows crossing the seam `Q^-|P^+` have,
in order, the values

\[
       \boxed{U,D_{d-1},D_{d-2},\ldots,D_2,U.}              \tag{3.3}
\]

#### Proof

The first window contains all of `Q^-` and the first letter `T`, hence is
`U`.  After one shift, `f_(d-1)` has left the window while only the core
stutter `K` has entered from the right, giving `D_(d-1)`.  At each following
shift, `f_j` leaves on the left exactly one step before it enters on the
right, so the unique hole walks through

\[
                       f_{d-1},f_{d-2},\ldots,f_2.
\]

At the last shift `f_2` has entered and the window is again `U`.
\(\square\)

There are now two distinct completion modes.

* In the **prepared-bank mode**, the old cut drops
  `D_d,...,D_1`; the new seam gains (3.3), and the untouched bank must retain
  one additional `D_1` and `D_d`.
* In the stronger **identical-bank mode**, an independent second literal
  `Q^-|P^+` collar is planted at the old cut, so the dropped and gained banks
  are both (3.3).

For the second mode a convenient block layout is:

* the rotation block begins with `P^+` and ends with `Q^-`;
* the block after the old cut begins with another `P^+`; and
* the global suffix ends with another `Q^-`.

The old cut and the new wrap seam then see the same literal `Q^- P^+`
collar.  In a collar-disjoint realization this requires a `Q^-` and `P^+`
block at each of the two seams; the one prepared global suffix and prefix do
not supply all four blocks by themselves.

### Corollary 3.2 (`B+2` prepared-bank palette count closes exactly)

If the untouched middle part contains every owner except
`D_2,...,D_(d-1)` and contains retained occurrences of `D_1,D_d`, then
replacing the prepared old boundary bank by the new one keeps all `W`
owners.  Before the recut `D_1,D_d` are the two duplicate-surplus owner
occurrences; afterward they are the unique endpoint coatoms, while the two
`U` windows are the two nonmiddle surplus windows available at length
`B+2`.

This is an exact owner-palette statement.  It does not assert that the
required three collar occurrences coexist in a simple carrier or in one
integral common cap.

## 4. Stronger interval-deck audit

In the stronger identical-bank mode, because the old and new seam words are
literally the same concatenation `Q^- P^+`, much more than the owner row is
preserved locally.  The following paragraph and Corollary 4.1 are conditional
on that second literal seam; they do not follow from prepared-bank owner
coverage alone.

Let an old crossing cell use `a` letters on the left of its cut and `b`
letters on the right.  If

\[
                              a\le d,\qquad b\le d,           \tag{4.1}
\]

then the corresponding new-seam cell has exactly the same source letters
and the same OR.  In particular every crossing cell of width at most
`d+1` is preserved, because `a,b>=1` and `a+b<=d+1` imply (4.1).

### Corollary 4.1 (no local lower or owner damage)

Under a rank-graded depth-`d` compiler, the identical stutter collars cause
no lower-row damage and no middle-owner damage.  The first uncontrolled
crossing addresses have width

\[
                              d+2.                            \tag{4.2}
\]

They are the two exterior Ferrers strips

\[
 \{(a,b):a>d,\ b\ge1\}\ \cup\
 \{(a,b):a\ge1,\ b>d\}.                                    \tag{4.3}
\]

In a rank-graded word these are upper-side obligations only.  Their exact
old/new value sets are

\[
 \begin{aligned}
  \mathcal R_{\rm old}
   &=\{\operatorname{OR}(\operatorname{suf}_a R)
        \cup\operatorname{OR}(\operatorname{pre}_b MQ):
                   \max(a,b)>d\},\\
  \mathcal R_{\rm new}
   &=\{\operatorname{OR}(\operatorname{suf}_a MQ)
        \cup\operatorname{OR}(\operatorname{pre}_b R):
                   \max(a,b)>d\}.                            \tag{4.4}
 \end{aligned}
\]

The stutters alone do **not** identify (4.4).  Full interval-language
preservation still requires

\[
 \mathcal R_{\rm old}\subseteq
   \operatorname{Deck}(R)\cup\operatorname{Deck}(MQ)
      \cup\mathcal R_{\rm new}.                             \tag{4.5}
\]

Thus the stronger audit is positive through the complete lower/owner band
and stops exactly at arbitrary-width upper witnesses.

There is a clean sufficient condition which would remove that last stop.

### Lemma 4.2 (signature-conjugate block swap)

Let `R,S` be two source blocks satisfying

\[
 \begin{aligned}
  \operatorname{Deck}(R)&=\operatorname{Deck}(S),\\
  \{\operatorname{OR}(\operatorname{pre}_iR)\}_i
    &=\{\operatorname{OR}(\operatorname{pre}_iS)\}_i,\\
  \{\operatorname{OR}(\operatorname{suf}_iR)\}_i
    &=\{\operatorname{OR}(\operatorname{suf}_iS)\}_i.       \tag{4.6}
 \end{aligned}
\]

Then

\[
                         \operatorname{Deck}(RS)
                           =\operatorname{Deck}(SR).          \tag{4.7}
\]

#### Proof

The internal interval languages agree by the first row of (4.6).  The
crossing language of `RS` is every union of a suffix value of `R` and a
prefix value of `S`; the crossing language of `SR` uses the same two value
sets in the opposite order.  Set union is commutative, so the two grids are
equal.  \(\square\)

Therefore a full solution of the upper-ticket row would follow from two
signature-conjugate blocks which both begin with `P^+` and end with `Q^-`.
Their old and new seams are then literally the same stutter collar, while
Lemma 4.2 controls every longer crossing interval.  The authenticated
mixed-coatom phase blocks already have equal prefix, suffix, and interval
OR signatures at the **owner-word** level.  It is not yet proved that this
equivalence lifts to source blocks carrying the required `K` stutters; that
is the exact strengthened host target.

## 5. What remains for a word theorem

Three distinct gates remain after the exact palette calculation.

1. **Source legality.**  In prepared-bank mode, plant the two core stutters
   and the retained endpoint-coatom occurrences in one nonzero
   source/common-cap state.  In identical-bank mode, plant both complete
   seam instances (four collar blocks when their supports are disjoint).
2. **Carrier simplicity/topology.**  Complete the untouched `W-(d-2)`
   owner occurrences without repetitions and with the required path forest.
3. **Upper tickets.**  Prove (4.5), or carry alternate witnesses for every
   target in the two residual Ferrers strips.

The `B+1` flat route is closed.  The `B+2` construction has the correct
owner palette and complete short-band language, but not yet the full upper
deck or the integral cap.

## 6. Audit

Run

```text
python3 scratch/audit_h1_flat_endpoint_wrap_bplus1_bplus2_20260801.py
```

It verifies (2.2)--(2.3), the exact list (3.3), all `d^2` local crossing
addresses, and exhausts the two stutter positions for `2<=d<=8`; the
symbolic construction is replayed for `2<=d<=40`.  It reports

```text
PASS_FLAT_ENDPOINT_WRAP_BPLUS1_NOGO_BPLUS2_PALETTE
```

with canonical payload SHA-256

```text
0e631e192f406b2115b7b93657f1e33c56b8ddf6d2efa7917ee94b4193f892f3
```

Files:

```text
scratch/audit_h1_flat_endpoint_wrap_bplus1_bplus2_20260801.py
scratch/h1_flat_endpoint_wrap_bplus1_bplus2_20260801.audit.json
```

Dependencies:

* `MATH_THEOREM_H1_COATOM_SPLIT_HOST_ENDPOINT_WRAP_AND_LOCAL_EAR_NOGO_20260801.md`;
* `MATH_THEOREM_COATOM_TWO_PHASE_BOUNDARY_CHAIN_CARVING_20260801.md`.
