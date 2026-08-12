# Independent audit of boundary--core pin coupling

## Verdict

The pin identity, coordinate-complete separator, rankwise upper-shadow
inheritance theorem, complement-rectangle formula, surplus-component
inequality, and the two stated `k=11` corollaries are sound.

The strongest new consequence is not another scalar rank count.  If an exact
rank-count word has `h` literal active-rank boundary entries, its peeled core
misses at most `h` masks in each proper rank.  When `h=1`, all masks lost by
the core form one nested endpoint chain.  In the hypothetical `k=11` endpoint
six-set branch, the 464-entry core must therefore cover at least 2041 of the
2047 nonempty masks.

In the principal `k=11` branch, the independently proved surplus relaxation
does reduce the lower-rank geometry to at most two components after literal
five-sets are deleted.  If there are two, no literal five-set is repeated and
one component has full coordinate support.

These are necessary equality reductions.  They do not establish existence or
nonexistence at length 465.

## 1. Audit of the pin identity

For every peeled boundary cell `[i,i]`, its selected label is the actual entry
`A_i`.  If `b` is absent from `A_i`, this singleton is itself a negative
interval for `b`, so it removes `i` from `Z_b`.  If `b` is present, no actual
witness labelled by a set omitting `b` can include `i`.  Therefore

    Z_b intersect boundary = {i : b in A_i}

exactly.  This uses realizability (or, equivalently, full pin survival), not
merely an arbitrary collection of interval labels.

## 2. Audit of the separator and rankwise deficit

The active rank is assumed at least two.  The peeled core covers every
singleton and hence contains an occurrence of every coordinate.  Its total OR
is `[k]`.  Any interval touching both boundary blocks contains the entire core
and is consequently the full set.  This justifies excluding such intervals
only for proper targets; the note correctly treats rank `k` separately.

For each proper target absent from the core, choose one witness.  A left
witness has a left endpoint in the left boundary.  At a fixed left endpoint,
OR values are nested as the right endpoint increases, so there is at most one
distinct value of any fixed rank.  The same reversed argument holds at fixed
right endpoints in the right boundary.  Assigning each missing target to one
chosen witness proves

    missing_core(rank s) <= |P|+|Q|

without assuming unique witnesses.  There is no double-counting issue because
the chosen witnesses partition into the left and right cases.
The ambient word is assumed universal in this theorem; coverage only through
the active rank would not justify making this choice for every upper mask.

There are `k-r` proper ranks from `r` through `k-1`; adding the possible full
set gives `h(k-r)+1` when `h>0`.  At `h=0` the word and core coincide, as
stated.

For `h=1`, every non-core witness is a prefix after reversal.  All such ORs
belong to one inclusion chain, so the stronger one-per-rank and nesting claims
are valid.

## 3. Audit of complement rectangles and gates

For a left crossing, its boundary part is a suffix and its core part is a
prefix.  De Morgan gives

    complement(boundary_suffix OR core_prefix)
      = complement(boundary_suffix) intersect complement(core_prefix).

A coordinate belongs to the first complement exactly after its last boundary
occurrence, and to the second exactly before its first core occurrence.  This
proves the two-threshold rectangle formula.  Each threshold chain changes at
most `k` times, so the coarse `(k+1)^2` bound is valid.

The earliest suffix having proper union has a nonempty common deficit.  Every
entry in that suffix avoids the complete deficit, and distinct rank-`r`
entries inside a ground set of size `k-|D|` number at most
`C(k-|D|,r)`.  The gate bound follows.  It is only a bound on crossing values,
not on intervals internal to the boundary; the note explicitly preserves
this distinction.

## 4. Audit of the surplus-component inequality

After deleting `h` literal rank-`r` entries with `z` distinct values, the
remaining components must represent at least `M-z` other rank-`r` targets.
Their total interval slack is

    d+c-(h-z)=d+c-x.

If `x>c`, this is below `d`, and side-capacity superadditivity contradicts the
definition of `d`.  Thus `x<=c`.

Each nonempty lower component has positive slack.  A zero-slack component
would place as many incomparable equal-rank witnesses as positions, forcing
all of them to be singleton cells, contrary to the component's entry-rank
ceiling.  With `s` positive slacks summing to `T`, the largest is at most
`u=T-s+1`.  The two independent maximizations

    sum t_j q_j <= u(M-z),
    sum C(t_j+1,2) <= C(u+1,2)+s-1

are valid upper bounds even if their equality allocations do not coincide.
At least `s-1` deleted positions separate the components, giving
`z>=s-1-x`.  Replacing `z` by the smaller nonnegative lower bound yields the
displayed necessary inequality.

For `k=11,r=5,d=2,c=1`, exact substitution gives:

* `s=3,x=0`: capacity 463, below `L=561`;
* `s=3,x=1`: total slack 2, so three positive components are impossible;
* `s=2,x=1`: capacity 464, again below 561.

Hence at most two components exist, and the two-component case forces
`x=0`.

With `s=2,x=0`, the total component slack is three, so the two positive
slacks are one and two.  In the slack-one component of length `m`, the
assigned rank-five witness count is `m-1`.  The equal-rank endpoint normal
form confines all selected witnesses to adjacent pairs; singleton witnesses
are excluded by the entry-rank ceiling.  Hence all `m-1` adjacent pairs are
distinct rank-five values, and every lower target represented there must be a
singleton.  Corollary 8.2 is therefore valid.

## 5. Audit of the coordinate transversal

If `V_j` is the coordinate union of component `j`, every nonempty target
`H` of size below `r` is represented in one component and therefore satisfies
`H subseteq V_j`.  If all deficits `[k]\V_j` were nonempty, choosing one point
from each would produce a hitting set `H` of size at most `s`.  When `s<r`,
that `H` is itself a lower target but is contained in no `V_j`, contradiction.
Thus some component is coordinate-complete.  Coordinate-complete means total
OR `[k]`; it does not imply universality, and the main note correctly avoids
that stronger claim.

## 6. Numerical audit

The independent checker

    python3 scratch/check_boundary_core_pin_coupling.py

passes on all stored exact certificates from `k=0` through `k=10` and at
`k=12`.  For every maximizing active rank at least two it:

* exhaustively verifies universality;
* reconstructs boundary blocks and the core;
* selects witnesses and recomputes every legal set `Z_b`;
* verifies full pin survival and exact boundary pins;
* checks every crossing complement rectangle;
* checks per-rank and total core losses.

It also evaluates the component-capacity relaxation symbolically through
`k<20`.  The recorded `k=11` arithmetic is exact:

    b_6(11)=465, b_5(11)=464,
    M_6=462, d_6=3, sigma_6=369, h_6<=1,
    guaranteed 464-core coverage in Case II = 2041.

The nontrivial certificate sanity check is `k=4`:

    [10,9,5] || [1,2,4,8].

Its core misses exactly three rank-two and two rank-three values, satisfying
the boundary budget `h=3` at each proper rank.

## 7. Scope and remaining gap

The core-shadow theorem does not classify which upper masks are lost, except
in the one-endpoint branch where they form a chain.  A 464-entry word covering
2041 masks is not ruled out by any current interval-capacity theorem.  In the
main branch, a coordinate-complete component can still have complicated
internal OR behavior.  The surplus-component inequality is necessary, not
sufficient, and does not impose a fixed row.

The valid search/theory reductions are therefore:

1. endpoint-six-set branch: a rank-stratified nested completion of an
   at-least-2041-mask 464-core;
2. no-six-set branch: one or two lower components, with distinct literal
   five-sets, a coordinate-complete component, and one exact adjacent-pair
   rank-five path in the two-component case.

No exact-value bound changes yet.
