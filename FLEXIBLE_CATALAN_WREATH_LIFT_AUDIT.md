# Independent audit: flexible Catalan parent-packet lift

## Scope and verdict

This audit checks the claims in `FLEXIBLE_CATALAN_WREATH_LIFT.md` without
using the fixed-factor obstruction from `Q11_WREATH_INSERTION_SEARCH.md`.

The all-dimensional child-count obstruction is valid.  Its only substantive
hypothesis is parent preservation: every new cyclic row must delete to one
row of a fixed exact old factor.  The old factor itself is arbitrary, so row
reordering and balanced switches do not weaken the conclusion.

The `m=5` three-phase classification is also valid and independently
exhaustible.  No SAT/UNSAT result for the global phase system is asserted in
the theorem.

## 1. Ownership audit

Let `pi` be an old cyclic row on `2m-1` coordinates.

* Removing the unique new coordinate from a one-new length-`m` interval in a
  child of `pi` leaves a consecutive old length-`m-1` interval of `pi`.
* An old length-`m` set is consecutive in `pi` if and only if its old
  complement, of length `m-1`, is consecutive.

Because an exact old factor uses every old `(m-1)`-set in exactly one row,
both assertions give a unique parent to every zero-new and tagged one-new
target.  There is no hidden assumption that the old factor is vertically
complete below its middle layer.

Therefore global exactness really does split into the parentwise equalities
used in Theorem 3.1.

## 2. Arithmetic audit

For one child of type `h`, the counts are

\[
 z=m+1-h,\qquad o=2h,\qquad t=m-h.
\]

For `q` children of one parent, exact one-new coverage gives

\[
 2\sum h_j=2(2m-1).
\]

Exact zero-new coverage gives

\[
 q(m+1)-\sum h_j=2m-1.
\]

Elimination gives

\[
 q=\frac{4m-2}{m+1}=4-\frac6{m+1}.
\]

Thus `q` is integral only if `m+1` divides 6.  For positive `m`, the list is
`m=1,2,5`.  This agrees with the Catalan ratio

\[
 \frac{Cat_m}{Cat_{m-1}}=\frac{2(2m-1)}{m+1},
\]

as it must: summing the uniform parent sizes over `Cat_(m-1)` old rows gives
the correct number `Cat_m` of new rows.

The obstruction is stronger than a fixed-factor Hall witness.  It rejects
the entire parent-preserving architecture in every nonintegral dimension.

## 3. Packet-gluing audit

The new middle layer has three disjoint sectors according to the number of
new coordinates.  Parent saturation handles sectors zero and one.  The
exports are exactly the old projections of sector two.  Therefore the union
is an exact new middle factor exactly when the exports partition
`binom(V,m-2)`.  No upper- or lower-shadow conclusion is implicit here.

In particular, an exact middle factor produced by the phase construction
still needs a separate vertical-coverage check before it can be called fully
vertical or used as an OR construction.

## 4. Independent finite local audit at `m=5`

Run

```text
python3 scratch/verify_flexible_catalan_wreath_lift.py
```

The checker independently constructs all 90 insertions of coordinates 10
and 11 into the generic old row `1,...,9`.  It enumerates all 117,480 triples
of candidates and demands simultaneously:

* all nine zero-new old length-five intervals exactly once;
* all eighteen tagged one-new old length-four intervals exactly once; and
* six distinct two-new old triples.

The result is exactly six realizations.  Their omission histogram is

```text
036: 2
147: 2
258: 2
```

This proves Lemma 5.1 without trusting the search encoder.  Dihedral
symmetry makes the generic-row computation valid for every parent row.

## 5. Encoder audit

The flexible encoder uses a row variable only to aggregate rank-four
exactness and a row-phase variable for each surviving phase.  It fixes one
row and phase by coordinate and dihedral symmetry.  Its two target families
are precisely:

* old rank-four masks, exact once; and
* retained old rank-three masks, exact once.

Selecting two phases of the same row is separately forbidden (and would in
any event duplicate all nine rank-four targets).  The independent
certificate checker reconstructs parent classes by deleting 10 and 11, so a
future SAT certificate does not rely on the CNF implementation for trust.

## 6. Guardrails

The theorem does **not** rule out:

1. cross-parent splices in which deleting the new coordinates does not yield
   one old row;
2. genuinely new rows, such as the 28 type-two rows in the `14+28` ledger;
3. a new exact factor unrelated to any prescribed old factor; or
4. balanced switches applied after a lift if those switches destroy parent
   ownership.

Those are precisely the freedoms an all-dimensional positive construction
must use.  The audit therefore accepts the theorem as a general obstruction
to the intended class, not as an obstruction to vertical wreath factors or
to the main OR conjecture.
