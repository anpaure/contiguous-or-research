# Independent audit of iterated boundary--core rigidity

## Verdict

PASS.  The record-onion theorem and its numerical table are valid
consequences of the audited rank-excess and boundary--core theorems.  The
iteration is explicitly conditional on an exact equality of lengths, and the
write-up does not promote numerical saturability to existence.

The genuinely new conclusions are:

1. the exact recursion gate `h_r=g_r`;
2. the excess/failure budget `e_r=g_r-h_r`;
3. the complete strict-record boundary-cap ledger for `k<20`;
4. the fact that a fully saturated onion is impossible for every
   `6<=k<20`;
5. the three-layer conditional refinement of the `k=11` exceptional
   endpoint-six branch.

None of these conclusions improves the present upper or lower bound on
`nu(11)`.

## Proof audit

Let `beta_j=max_(s<=j)b_s` and choose the least `r` attaining `beta_j`.
Then `b_r=beta_j` and `b_r>beta_(r-1)`, so `r` is a strict record.  A word of
length `beta_j` covering through rank `j` in particular covers through rank
`r`, and therefore satisfies the exact hypotheses of boundary--core
rigidity at rank `r`.

That theorem gives one lower-rank core of length `b_r-h_r`.  Since the core
covers every target below `r`, every rank-count bound below `r` applies to
it, and hence

    b_r-h_r >= beta_(r-1).

This proves `h_r<=g_r`.  The already-audited residual-capacity argument gives
`d_r h_r<=sigma_r`, with no second charge of the same holes.  Combining the
two bounds gives the displayed `H_r`.

The identity

    b_r-h_r=beta_(r-1)+(g_r-h_r)

proves both directions of the recursion gate.  When the excess is zero, the
core has exact lower-envelope length and the next theorem application is
legitimate.  When it is positive, rank-excess stability at a least lower
maximizer `p` applies with precisely `c=e_r`, proving the exceptional-entry
bound.  It gives no contiguity after those exceptional entries are removed;
the main note correctly stops the recursion there.

Induction now gives the nested block order in (5.1).  Boundary entries are
distinct within each peeled rank by the original theorem.  No claim of
distinctness between different ranks is needed.

## Equality-condition audit

The following possible overclaims were specifically checked and are absent:

* A positive active-rank boundary block does not itself trigger recursion.
  Its total mass must equal the complete record gap.
* `H_r=g_r` is only absence of this numerical obstruction; it does not prove
  that an equality word with `h_r=g_r` exists.
* A tied later rank is not treated as an additional zero-width shell.  The
  least maximizer is used, giving the strongest rank ceiling.
* If `h_r<g_r`, the core is not silently replaced by a shortest lower word.
* The two boundary blocks need not have equal sizes, and either may be empty.
* Upper targets need not be hulls of the peeled layers.
* Pin survival, endpoint orthogonality, and the OR growth recurrence remain
  independent construction requirements.

## Arithmetic audit

`scratch/check_iterated_boundary_core_rigidity.py` computes `tau` by its
defining integer inequality, recomputes every `b_r,sigma_r,g_r,H_r`, and
asserts the first blocker for each `1<=k<20`.

It also exhaustively re-enumerates all subarray ORs of the archived exact
words for `k=8,9,10,12` before reporting their diagonal rank profiles.  Those
profiles contain no entry at the active record rank, confirming that the
known constructions occupy the zero-boundary branch.  This empirical fact is
not used in the theorem.

The checker returns `PASS`.

## Scope

The numerical blocker `H_r<g_r` disproves only a completely saturated peel
from that rank to the next record equality.  It does not disprove an optimal
word of length `B(k)`: such a word may have any smaller active-rank boundary
mass, especially zero.  Therefore the all-`k` conjecture remains open.
