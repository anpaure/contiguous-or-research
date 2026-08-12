# Boundary--core pin coupling and upper-shadow inheritance

## 1. Verdict

Boundary--core rigidity has a genuinely two-sided consequence which is not a
rank count.  At exact rank-count length, the peeled lower core contains every
coordinate and is therefore an OR separator: an interval meeting both active
rank boundary blocks has value `[k]`.  Pin survival fixes the legal positions
of every coordinate on those blocks exactly.  It follows that the lower core
inherits almost all upper masks as well as the complete lower ideal.

If the two boundary blocks have total length `h`, then for **each proper
rank** the core misses at most `h` masks.  In particular it misses at most

    h(k-r)+1

nonempty masks in total.  The final `+1` is the possible full set and is absent
when `h=0`.

For a hypothetical `k=11,n=465` word in the one-literal-six-set branch, the
remaining 464 entries consequently cover at least `2041/2047` masks.  The at
most six losses form one nested prefix chain, with at most one loss in each
rank `6,7,8,9,10,11`.

There is a separate consequence for the principal branch, in which all 465
entries have rank at most five.  Deleting the literal five-set entries leaves
at most two lower-rank components.  If there are two, all literal five-set
occurrences are distinct and at least one lower component contains every
coordinate.

None of these statements assumes a fixed derivative row, Johnson adjacency,
a natural grading, or a chosen central path.

## 2. Setup

Fix `r>=2`, put

    M = C(k,r),
    L = sum_(s=1)^(r-1) C(k,s),

and let `d=tau(k,r)` be the least nonnegative integer satisfying

    L <= dM + C(d+1,2).

Assume a **universal** word `A=(A_1,...,A_(M+d))` exists.  (Only coverage
through rank `r` is used to obtain the decomposition; universality is used
later for the upper-shadow inheritance.)  Boundary--core rigidity gives

    A = P || C || Q,                                      (2.1)

where:

* every entry of `P,Q` is a distinct rank-`r` mask;
* every entry of `C` has rank below `r`;
* `C` represents every nonempty mask of rank below `r`.

Write

    p=|P|, q=|Q|, h=p+q.

Because `r>=2`, the lower ideal includes every singleton `{b}`.  Every such
singleton has a witness inside `C`.  Consequently

    OR(C)=[k].                                             (2.2)

This elementary observation is the source of the two-sided coupling.

## 3. Boundary legal sets are exact

Choose one witness `I_S` for every nonempty target, choosing:

* a witness wholly in `C` when `|S|<r`;
* the singleton cell `[i,i]` for each literal boundary value `S=A_i`.

For coordinate `b`, define the usual legal set

    Z_b=[n] \ union_(S: b notin S) I_S.                    (3.1)

### Lemma 3.1 (exact boundary pins)

For every boundary position `i in P union Q`,

    i in Z_b  iff  b in A_i.                              (3.2)

#### Proof

If `b notin A_i`, the selected singleton witness `[i,i]` for `A_i` is one of
the negative intervals in (3.1), so `i notin Z_b`.

If `b in A_i`, no actual witness for a target omitting `b` can contain `i`,
because its interval OR would then contain the occurrence of `b` in `A_i`.
Thus no negative selected interval deletes `i` from `Z_b`.  Hence `i in Z_b`.
∎

So pin survival has no freedom on the peeled boundary.  All freedom is in the
core hitting sets.

## 4. The coordinate-complete separator

### Lemma 4.1 (proper-witness separation)

No interval representing a proper subset of `[k]` meets both `P` and `Q`.

#### Proof

Such an interval contains the entire core `C`.  Equation (2.2) says its OR
already equals `[k]`. ∎

This is stronger than saying lower-rank witnesses avoid the boundary.  It
applies simultaneously to every proper upper rank.

### Theorem 4.2 (rankwise upper-shadow inheritance)

Let `c_s(C)` be the number of rank-`s` masks represented by intervals wholly
inside `C`.  Then

    c_s(C) = C(k,s)                         (1 <= s < r),   (4.1)
    c_s(C) >= C(k,s)-h                      (r <= s < k).   (4.2)

The full set is the only possible additional loss.  Therefore, if `h>0`,
the core alone covers at least

    (2^k-1) - h(k-r) - 1                                (4.3)

nonempty masks.  If `h=0`, the core is the whole word and has no loss.

#### Proof

Equation (4.1) is part of boundary--core rigidity.

Fix a proper rank `s>=r`.  For every rank-`s` mask not represented inside
`C`, select one witness in the whole word.  By Lemma 4.1 it meets at most one
boundary block.

If it meets `P`, assign it to its left endpoint `i in P`.  For fixed `i`, the
ORs of `[i,j]` form an inclusion chain as `j` increases.  Two distinct members
of an inclusion chain cannot have the same rank.  Thus at most one missing
rank-`s` mask is assigned to each of the `p` left endpoints.

If the witness meets `Q`, assign it to its right endpoint `j in Q`.  As the
left endpoint moves left, these ORs again form an inclusion chain.  At most
one missing rank-`s` mask is assigned to each of the `q` right endpoints.

Hence at most `p+q=h` rank-`s` masks are missing from `C`, proving (4.2).
There are `k-r` proper ranks `r,r+1,...,k-1`; the unique full set accounts for
the final possible loss. ∎

At rank `r`, the proof of boundary--core rigidity already gives the sharper
interpretation that the `h` possible losses are precisely the distinct
literal boundary values; every other rank-`r` mask occurs in `C`.

### Corollary 4.3 (one endpoint gives one loss chain)

If `h=1`, the masks not represented inside `C` form a subchain of the prefix
ORs (or, after reversal, suffix ORs).  There is at most one loss in each rank
`r,r+1,...,k`, and at most

    k-r+1

losses altogether.

Indeed, after orienting the unique boundary entry to the left, every witness
not contained in `C` is `[1,j]`.  These values form one inclusion chain.

## 5. Exact complement rectangles at the two interfaces

Write the left boundary as positions `1,...,p` and the core as
`p+1,...,p+m`.  For `i<=p<j<=p+m`, define

    D_i = [k] \ OR(A_i,...,A_p),
    E_j = [k] \ OR(A_(p+1),...,A_j).

Then De Morgan's law gives the exact factorization

    [k] \ OR(A_i,...,A_j) = D_i intersect E_j.             (5.1)

The family `(D_i)` increases as `i` moves toward the core, while `(E_j)`
decreases as `j` moves through the core.  More explicitly, let

* `ell_b` be the last position of coordinate `b` in the left boundary, with
  `ell_b=0` if it is absent there;
* `f_b` be its first position in the core.  This exists by (2.2).

Then

    b notin OR(A_i,...,A_j)  iff  ell_b < i and j < f_b.   (5.2)

Thus every coordinate occupies one axis-aligned threshold rectangle in the
`(i,j)` crossing grid.  All left-crossing complements are membership patterns
of these `k` rectangles.  In particular there are at most `(k+1)^2` distinct
left-crossing values, independently of the physical block lengths.  The
right interface has the reversed identical description.

This is the exact coordinate version of pin coupling: by Lemma 3.1, `D_i`
is precisely the set of coordinates having no legal boundary pin in the
suffix `A_i,...,A_p`; any required occurrence of one of them must survive in
the core prefix.

### Corollary 5.1 (proper crossing gate)

Suppose some suffix of the left boundary has proper union, and let `i_0` be
the earliest start of such a suffix.  Then

    D_(i_0) != empty,

every boundary entry from `i_0` through `p` avoids every coordinate of
`D_(i_0)`, and no proper crossing interval can start before `i_0`.  Since the
boundary rank-`r` entries are distinct,

    p-i_0+1 <= C(k-|D_(i_0)|,r).                           (5.3)

This identifies the exact coordinate-deficient gate through which every
proper left crossing must pass.  There is an analogous right gate.

## 6. The `k=11` one-six-set branch

At `k=11,r=6`, boundary--core rigidity gives `h<=1`.  In the branch `h=1`,
orient the word as

    T || C,

where `T` is a six-set and `|C|=464`.

The core covers:

* all `1023` masks of ranks one through five;
* the other `461` six-sets;
* at least `329,164,54,10` masks of ranks `7,8,9,10` respectively.

Therefore

    1023+461+329+164+54+10 = 2041.                         (6.1)

So the 464-term core covers at least `2041/2047` nonempty masks.  Its possible
losses are a nested chain containing:

* the literal six-set `T`;
* at most one set of each rank `7,8,9,10`;
* possibly `[11]`.

If `f_b` is the first occurrence in `C` of one of the five coordinates
outside `T`, then the endpoint prefix chain is exactly

    T union {b outside T : f_b <= j}.                      (6.2)

Thus this entire branch can be searched as a six-hole, rank-stratified core
completion problem, rather than as an unrestricted 465-position problem.

## 7. A surplus component theorem

The principal `k=11` branch has no six-set entry, so the exact rank-six peel
is empty.  Applying rank five instead leaves one extra position over its
rank-count bound.  The following general necessary inequality controls that
situation.

Let a word of length

    M+d+c

cover every mask through rank `r`, and assume every entry has rank at most
`r`.  Delete all literal rank-`r` entries.  Let

* `h` be their number;
* `z` the number of distinct literal values;
* `x=h-z` their repetition excess;
* `s` the number of nonempty lower-rank components.

### Proposition 7.1 (surplus component capacity)

Necessarily

    0 <= x <= c.                                           (7.1)

Moreover, for at least one integer `x in [0,c]`, put

    T = d+c-x,
    u = T-s+1,
    z_0 = max(0,s-1-x).

Then `T>=s` and

    L <= u(M-z_0) + C(u+1,2) + s-1.                        (7.2)

#### Proof

Every rank-`r` target except the `z` distinct literal values has a witness
inside one of the lower components.  The selected equal-rank witnesses in
those components have total count `M-z`, while the component lengths total
`M+d+c-h`.  Their total interval slack is therefore

    T=(M+d+c-h)-(M-z)=d+c-x.

If `x>c`, then `T<d`.  The side-capacity lemma and superadditivity would fit
all `L` lower targets with slack below the defining minimum `d`, a
contradiction.  This proves (7.1).

In component `j`, let `q_j` selected rank-`r` witnesses live in `n_j`
positions and put `t_j=n_j-q_j`.  Every `t_j` is positive: equality zero
would force all `q_j=n_j` incomparable equal-rank witnesses to be singleton
cells, but every entry in the component has rank below `r`.  Hence `T>=s`.

The largest `t_j` is at most `u=T-s+1`, and

    sum_j t_j q_j <= u(M-z).

Convexity, with positive integers `t_j` summing to `T`, gives

    sum_j C(t_j+1,2) <= C(u+1,2)+s-1.

At least `s-1` deleted positions separate the components, so `h>=s-1` and

    z=h-x >= max(0,s-1-x)=z_0.

Summing the side capacities of all components and replacing `z` by its least
possible value proves (7.2). ∎

### Proposition 7.2 (coordinate transversal condition)

Let `V_j` be the union of all entries in lower component `j`, and put

    D_j=[k]\V_j.

Every nonempty set of fewer than `r` coordinates is disjoint from some
`D_j`.  Equivalently, the family of nonempty deficits `(D_j)` has transversal
number at least `r`.

In particular, if `s<r`, then at least one component is coordinate-complete:

    V_j=[k].                                               (7.3)

#### Proof

Every nonempty `H subseteq [k]` with `|H|<r` is itself a lower target, so its
witness lies in one component.  All entries in that witness are in the same
component, hence `H subseteq V_j`, equivalently `H intersect D_j=empty`.

If all `D_j` were nonempty, choosing one coordinate from each would produce
a hitting set of size at most `s`.  When `s<r`, that hitting set is a lower
target yet is contained in no `V_j`, a contradiction. ∎

## 8. The principal `k=11` branch

Assume a length-465 universal word has no rank-six entry.  Every entry then
has rank at most five.  At rank five,

    M=C(11,5)=462,
    L=sum_(t=1)^4 C(11,t)=561,
    d=2,
    c=1.

Proposition 7.1 leaves at most two lower-rank components.  Indeed:

* `s=3` forces `x=0,T=3,u=1,z_0=2`, whose right side in (7.2) is only
  `463<561`;
* larger `s` are impossible because `T<=3`.

If `s=2` and `x=1`, then `T=2,u=1,z_0=0`, and (7.2) gives only
`464<561`.  Therefore:

### Corollary 8.1

In the no-six-set branch, deleting all literal five-set entries leaves either
one or two lower-rank components.  If there are two, every literal five-set
occurrence is distinct.  Since `2<5`, Proposition 7.2 says that at least one
of the two components has union `[11]`.

Thus the main branch has the unconditional physical form

    P_5 || C_1 || R_5 || C_2 || Q_5                       (8.1)

with either `C_2` absent or one of `C_1,C_2` coordinate-complete.  Here the
three five-set blocks may be empty except that `R_5` is nonempty in the
two-component case.  This is a globally WLOG reduction, not a central-row
ansatz.

There is additional rigidity in the two-component case.  Its total selected
rank-five interval slack is three and both component slacks are positive, so
they are exactly `1` and `2`.

### Corollary 8.2 (one exact adjacent-pair component)

In the two-component branch, one of `C_1,C_2`, say a segment of length `m`,
has the following exact form:

* its `m-1` adjacent-pair ORs are `m-1` different five-sets;
* every rank-at-most-four target represented in that segment occurs as a
  literal entry.

#### Proof

The slack-one component is assigned `m-1` distinct rank-five witnesses.  The
ordered-antichain normal form puts all of them in windows of length at most
two.  None is a singleton because every component entry has rank at most four.
There are exactly `m-1` adjacent pairs, so the selected witnesses are all of
them.  Every interval of length at least two contains one of these rank-five
pairs; hence a lower-rank witness inside the component must be a singleton. ∎

Thus even the two-component escape contains one fully rigid local derivative
row.  The other component has slack two and carries all nonliteral lower
targets assigned to it.

## 9. Verification

The independent checker

    python3 scratch/check_boundary_core_pin_coupling.py

does the following.

1. It enumerates every interval OR in the stored exact certificates for
   `k=0,...,10` and `k=12` (where certificate files are available for the
   larger cases).
2. At every maximizing active rank `r>=2`, it reconstructs the literal
   boundary blocks, verifies the lower core, recomputes one complete selected
   witness schedule and all `k` legal pin sets, and checks (3.2).
3. It checks the rankwise deficit bound (4.2), the total bound (4.3), and every
   complement rectangle (5.1).
4. It evaluates Proposition 7.1 exactly for all active ranks with `k<20`, and
   checks the two `k=11` symbolic conclusions.

All checks pass.  The nontrivial stored equality example with an actual
active-rank boundary is `k=4`:

    [10,9,5] || [1,2,4,8].

The three rank-two boundary entries peel off, the four-singleton core is
coordinate-complete, and the core misses only three rank-two and two
rank-three masks, within the theorem's per-rank boundary budget.

## 10. Scope

The theorem does **not** prove `nu(11)=465`.  In the main branch, one of the
one or two lower components may still carry a very complicated set of upper
intervals.  In the endpoint-six-set branch, covering 2041 masks in 464
positions is a strong necessary condition but is not presently contradictory.

The `(k+1)^2` crossing bound concerns intervals that actually cross a
boundary/core interface; it says nothing about intervals wholly inside a
long boundary block.  Proposition 7.1 is a necessary component relaxation,
not a sufficient construction theorem.  Finally, coordinate completeness of
one component means its total OR is `[k]`; it does not say that component is
itself universal.

The useful advance is exact localization.  Boundary pins are fixed, proper
upper losses are rankwise bounded endpoint chains, and the principal `k=11`
branch has at most two lower components with a coordinate-complete separator;
in the two-component escape, one component is an exact adjacent-pair
rank-five path.
