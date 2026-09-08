# Vanishing-singleton socket insurance and the full small-bank lift

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional conditional implication.  Fractional feasibility
at depth `D` produces an integral anonymous depth-`D+1` fragmentation whose
entire rounding residue uses fewer than `r` explicitly insured
maximum-capacity collar occurrences.  Consequently the existing named
small-bank Rado theorem applies to the whole rounding residue, not merely
to `O(D)` of its chunks.  Fractional feasibility and the named bulk Rado
gate remain assumptions.

## 0. Setup

Work in `B_(2r)`.  Put

\[
 C_s={2r\choose s},\qquad H_s=C_s-C_{s-1},\qquad
 W=C_r,
\tag{0.1}
\]

and let

\[
 D=d(2r),\qquad t=r-D.
\tag{0.2}
\]

At depth `D`, residual chains beginning at rank `t-1` are the
`H_(t-1)` length-one jobs.  They disappear when the depth is increased to
`D+1`.  Every genuine collar occurrence of old capacity `c` then has new
capacity `c+1`.  There are

\[
 H_r=C_r-C_{r-1}={W\over r+1}
\tag{0.3}
\]

middle-singleton collar occurrences of old maximum capacity `D`, and there
are `D` endpoint-triangle sockets of capacities `1,...,D` which need not
transport through the shift.

Assume `D>=1` and `t>=2`, and define

\[
 h:=D\left\lceil {t-2\over D+1}\right\rceil .
\tag{0.4}
\]

The finite hypotheses used below are

\[
 H_r\ge h
\tag{0.5}
\]

and

\[
 H_{t-1}-D
 \ge hD+{D(D+1)\over2}.
\tag{0.6}
\]

Both hold for every sufficiently large `r`: the left sides are
exponential, whereas the right sides are polynomial.

## 1. Socket insurance

Call an old length-one job **disposable**.  It has no nonempty residual
job after the depth shift.

### Lemma 1.1 (one target socket can be insured)

Let an integral old packing be given, and let `P` be a socket of capacity
`c>=1`.  Suppose sufficiently many disposable jobs occupy distinct other
genuine collar sockets.  One may alter the old packing so that

1. `P` contains a disposable singleton;
2. every non-disposable job remains integrally packed;
3. at most `c` disposable jobs are removed from their former sockets; and
4. no new socket other than those former disposable-job sockets is used.

#### Proof

If `P` already contains a disposable singleton, do nothing.  If it is
empty, move one disposable singleton to `P`; its old socket becomes empty.

Otherwise `P` contains one piece of length `ell<=c` belonging to a
non-disposable job.  Remove `ell` disposable singleton jobs from `ell`
distinct other collar sockets.  Split the old piece into `ell` unit pieces
and put one in each vacated socket.  Put one of the removed disposable
singletons in `P`; leave the other `ell-1` disposable old jobs unpacked.
They have no descendants at depth `D+1`, so this omission is immaterial to
the new packing.  All non-disposable workload and every socket capacity are
preserved.  `square`

The lemma is deliberately an old-packing bookkeeping device.  It does not
claim that the sacrificed old singleton jobs remain covered at depth `D`;
they are precisely targets which move into the new collar at depth `D+1`.

### Lemma 1.2 (simultaneous insurance)

Let `P_1,...,P_q` be distinct old sockets of positive capacities
`c_1,...,c_q`.  If at least `sum_i c_i` integral disposable jobs are
available, then all `P_i` can be insured simultaneously, while every
non-disposable job remains packed.

#### Proof

Apply Lemma 1.1 successively, always choosing disposable donors outside
the target set and outside all previously used donor sockets.  A target
which already contains a disposable job consumes no donor; this exactly
compensates for that job's unavailability as a donor.  Thus the crude
budget `sum_i c_i` suffices.  `square`

## 2. Improved adjacent-depth rounding

### Theorem 2.1 (insured maximum-socket absorber)

Assume the depth-`D` fractional whole-job configuration LP is feasible and
(0.5)--(0.6) hold.  Then the complete nonempty residual histogram has an
integral anonymous interval fragmentation at depth `D+1` with these extra
properties:

1. no surviving piece uses an endpoint-triangle socket;
2. all pieces created from the rounding residue use a prescribed family of
   at most `h<r` genuine middle-singleton collar occurrences;
3. every such occurrence is occupied by a disposable singleton in the old
   bookkeeping packing and is therefore genuinely free with capacity
   `D+1` after the shift.

#### Proof

Take an extreme feasible point of the depth-`D` configuration LP.  The
basic-support theorem leaves at most `D` jobs with more than one positive
configuration; call them `F`.  Every job outside `F` has one integral
configuration, and those configurations inject into distinct old socket
occurrences.

Choose `h` genuine maximum-capacity collar occurrences, possible by
(0.5), and take all `D` endpoint-triangle sockets.  Their total old
capacity is

\[
 hD+1+2+\cdots+D=hD+{D(D+1)\over2}.
\tag{2.1}
\]

At most `D` disposable jobs belong to `F`.  Hence (0.6), Lemma 1.2 and the
integral disposable jobs outside `F` insure every selected maximum socket
and every endpoint socket.  All surviving jobs outside `F` are still
integrally packed, and none uses an endpoint socket.

Increase the depth to `D+1`.  Every insured singleton disappears.  Every
remaining non-disposable integral job loses its terminal cell; the
terminal-cell deletion lemma transports its fragmentation into a subset of
the same genuine collar occurrences.  Thus the `h` selected maximum
occurrences are free and each has new capacity `D+1`.

Only descendants of jobs in `F` remain unpacked.  There are at most `D` of
them and each has length at most `t-2`.  Fragment each into pieces of size
at most `D+1`.  The total number of required pieces is at most

\[
 D\left\lceil {t-2\over D+1}\right\rceil=h,
\tag{2.2}
\]

so the insured maximum sockets absorb all of them.

Finally, `h<r`.  Indeed, if the ceiling in (0.4) is positive, then

\[
 \left\lceil {r-D-2\over D+1}\right\rceil
 <{r-1\over D+1},
\]

and therefore

\[
 h<D{r-1\over D+1}<r.
\tag{2.3}
\]

If the ceiling is zero, the assertion is immediate.  The fragmentation is
interval-respecting because splitting and terminal deletion are performed
consecutively along each suffix job.  `square`

### Corollary 2.2 (eventual anonymous implication)

For every sufficiently large `r`, fractional exact-`B(2r)` configuration
feasibility implies integral anonymous depth-`D+1` fragmentation with a
rounding residue of fewer than `r` chunks, all on actual freed
maximum-capacity occurrences.

#### Proof

We have `D=Theta(sqrt(r))`, `t=Theta(r)`, and hence `h=O(r)`.  Meanwhile

\[
 H_r={W\over r+1},\qquad
 H_{t-1}=\Theta(W/\sqrt r),
\]

so (0.5)--(0.6) hold eventually.  Apply Theorem 2.1.  `square`

## 3. Named consequence

The rounding residue in Theorem 2.1 is now within the exact range of the
named small-bank theorem.  Every exceptional chunk is assigned to start
rank `r`; its socket has old capacity `D` and new capacity `D+1`.  Equation
(2.3) gives fewer than `r` requested starts at that rank.

### Corollary 3.1 (the entire rounding residue has a named lift)

Assume also

\[
                         \binom{t+1}2\ge h.
\tag{3.1}
\]

Suppose, in addition, that after co-choosing the insured maximum
occurrences and their old singleton values as in Theorem 5.1 of the named
small-bank theorem, the transported integral bulk has a named interval
lift satisfying the collar-start Rado cuts on the complement of those
rank-`r` starts **and using none of the endpoint-triangle sockets**.  Then the complete
depth-`D+1` fragmentation, including every chunk arising from the extreme-
point residue, has a named Boolean containment lift on the same collar.

#### Proof

Apply Theorem 5.1 of
`MATH_THEOREM_NAMED_FRAGMENTATION_START_MATROID_RADO_AND_SMALL_FREED_SOCKET_LIFT_20260805.md`
to the `h<r` exceptional chunks and their insured old-singleton/max-socket
pairs.  It co-chooses their named old singleton values, containing
rank-`r` starts, and the same physical occurrences across the depth shift.
The hypotheses of that theorem hold: `b=t-1>=1`; (0.6) gives
`H_b>=h`; and (3.1) is its remaining rank-`b` Hall bound.  The disposable
occupants of the endpoint sockets were only anonymous bookkeeping objects.
Those jobs have no new residual descendants and the sockets themselves are
not transported, so no endpoint naming is required.  The explicit endpoint
exclusion in the hypothesis says precisely that no surviving named bulk
chunk uses them.  Overlay the assumed bulk lift on the complementary starts.
`square`

Thus the adjacent-depth rounding no longer creates a separate large named
exceptional bank.  The only named fragmentation obstruction left is the
already isolated **bulk** interval-lift/Rado correlation.

## 4. Scope

This theorem does not prove the depth-`D` all-price fractional
configuration inequalities.  It does not prove the arbitrary-bulk named
Rado cuts, a resident upper-complete central chronology, topology, or a
safe opening.  Corollary 3.1 is an overlay theorem and explicitly assumes
that the bulk can be placed on the complementary collar starts.

The gain is exact: the old capacity-two absorber used up to
`O(r^(3/2))` small chunks.  Socket insurance replaces it by fewer than `r`
maximum-capacity chunks, precisely inside the proved protected-start range
of the named collar matroids.

## 5. Dependencies

1. `MATH_THEOREM_ONE_DEPTH_SHIFT_FREED_SINGLETON_ABSORBER_20260805.md`;
2. `MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`;
3. `MATH_THEOREM_NAMED_FRAGMENTATION_START_MATROID_RADO_AND_SMALL_FREED_SOCKET_LIFT_20260805.md`.
