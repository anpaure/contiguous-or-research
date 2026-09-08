# Independent audit of `TRIANGULAR_PEAK_SHARING.md`

## 1. Decisive verdict

The principal results are correct.

* The affine triangular reduction and bounding-rectangle criterion are exact.
* The explicit word has length exactly `R(R+1)` and every displayed shortened
  witness remains contiguous and has exactly the claimed maximum.
* The depth-`R` target antichain has exactly
  `floor((R+1)^2/4)` members, so the unrestricted quadratic lower bound is
  valid even with entries outside the canonical alphabet.
* The side-chain argument is valid, and the strengthened formula
  
  \[
     \operatorname{width}(\mathcal A_u)
       =\min(R-u,\lceil R/2\rceil)
  \]
  
  is exact.
* The resulting canonical peak-occurrence lower bound and its
  `(3/16+o(1))R^2` constant are correct.  Summing over `c` gives a genuine
  `Omega(m^3)` lower bound for canonical two-provider occurrences.
* The reverse-complement formulas, join/meet exchange, self-duality, merged
  length `2R^2+R`, and alphabet-disjointness assertion are all correct.

There is one local proof correction.  Lemma 4 invokes Lemma 1, whose stated
hypothesis is that the whole interval consists of arm/peak points.  Theorem 5
is intended to allow arbitrary additional entries.  The lemma nevertheless
remains true: the nearer canonical arm is an entry of the farther target's
witness, hence is coordinatewise at most that target, which directly gives
`r_1<=r_2` and `x_1<=x_2`.  Replacing the citation to Lemma 1 with this
one-line domination argument removes the mismatch without changing any
statement or constant.

The reflection construction is a two-sided **shadow** word: upper targets
are interval joins and reflected lower targets are interval meets.  It is not
by itself one max-word covering both halves by joins.  The source states the
join/meet distinction explicitly, but the shorter phrase "covers both
families" should continue to be read in this shadow sense.

Finally, Theorem 5 is deliberately canonical.  Its shrinking step is valid,
but its lower bound does not apply if a target is witnessed without the
exact pair `P_u,E_(r,x)`.  In particular it does not exclude the stated
three-provider or cross-`c` escape routes.

## 2. Affine reduction

Fix `c` and let `R=m-c`.  For

\[
 0\le u<r\le R,\qquad 0\le x<r,
\]

the points

\[
 P_u=(c+u,m-c,0,m-u),
 \qquad
 E_{r,x}=(c+r,m-c-x,x,m-r)
\]

belong to `[0,m]^4`: the bounds `u,r<=m-c` give `c+u,c+r<=m`, and all
other coordinates are manifestly between zero and `m`.  Also

\[
 E_{r,0}=(c+r,m-c,0,m-r)=P_r.
\]

Since `u<r`, the componentwise maximum is

\[
 E_{r,x}\vee P_u=(c+r,m-c,x,m-u)=Z_{u,r,x}.
\]

The correspondence with the original radius-transfer parameters is exact:
`H=c+r` and `t=r-u`, so `1<=t<=r`, while `0<=x<r`.  Conversely every upper
residual-tail parameter has a unique such triple.

There is an important provider-identity nuance.  `E_(c,r,x)` is an arm point
from the original fan with `H=c+r`, but `P_(c,u)` is the peak of the
**different** radius-`u` fan with `H=c+u`.  It is not the original `V_t`
point of the `H=c+r` fan.  Indeed that original point would be

\[
 V_t=(c+r,m-c-t,0,m-u),\qquad t=r-u,
\]

whereas

\[
 P_{c,u}=(c+u,m-c,0,m-u).
\]

This distinction causes no defect: the displayed coordinatewise join with
`P_(c,u)` is exactly the target.  It means that `F_r` is a new cross-radius
peak-sharing block, not a shortened copy of the original radius-`r` upper
fan.  All subsequent verification must, and does, use the affine join
identity rather than inherit witnesses from the old fan.

Map `E_(s,y)` to `(s,y)` and the additional point `P_0` to `(0,0)`.  For any
nonempty collection of these cells, its coordinatewise maximum is

\[
 \left(c+\max s,\ m-c-\min y,\ \max y,\ m-\min s\right).
\]

Equality with `Z_(u,r,x)` is therefore equivalent to

\[
 \min s=u,\quad \max s=r,\quad \min y=0,\quad\max y=x.
\]

These four extrema are in turn equivalent to containment in
`[u,r] times [0,x]` together with attainment of every side of that bounding
rectangle.  Lemma 1 is correct for intervals whose entries lie in the
triangular alphabet.

## 3. Explicit construction and witness shrinking

For each `r`, the block

\[
 \mathcal F_r=(E_{r,r-1},E_{r,r-2},\ldots,E_{r,0},
                 P_{r-1},P_{r-2},\ldots,P_0)
\]

has `r+r=2r` entries.  For a target `(u,r,x)`, the displayed interval

\[
 E_{r,x},E_{r,x-1},\ldots,E_{r,0}=P_r,
 P_{r-1},\ldots,P_u
\]

is a contiguous subinterval of this block, including the edge cases
`x=0`, `u=0`, and `u=r-1`.  Its cells satisfy

\[
 \min s=u,\quad\max s=r,\quad\min y=0,\quad\max y=x,
\]

so its maximum is exactly `Z_(u,r,x)`.  No intervening point can contaminate
the target.  The total length is

\[
 \sum_{r=1}^R2r=R(R+1).
\]

The occurrence counts are also exact.  Every `E_(r,x)` with `x>0` appears
once, giving

\[
 \sum_{r=1}^R(r-1)={R(R-1)\over2}
\]

nonpeak occurrences.  The point `P_0` appears once in each block, and for
`1<=u<=R`, `P_u` occurs once as `E_(u,0)` and in each later peak spine:

\[
 \operatorname{occ}(P_0)=R,
 \qquad
 \operatorname{occ}(P_u)=1+(R-u)=R-u+1.
\]

Thus peak occurrences total

\[
 R+\sum_{u=1}^R(R-u+1)={R^2+3R\over2},
\]

and the peak plus nonpeak totals sum to `R(R+1)`.

### The canonical shrinking step is valid

Suppose an arbitrary witnessing interval for `Z_(u,r,x)` contains a selected
occurrence of `P_u` and a selected occurrence of `E_(r,x)`.  The closed
physical interval between these occurrences is a subinterval of the original
witness.  Every entry of the original witness is coordinatewise at most its
maximum `Z_(u,r,x)`.  The two retained endpoints already have maximum
`Z_(u,r,x)`.  Hence the shortened interval has maximum both at least and at
most `Z_(u,r,x)`, and therefore exactly that target.

This argument does not require the intervening entries to lie in the
triangular alphabet.  It justifies every later use of the physical interval
between the two canonical providers.

## 4. Exact depth-`R` antichain count

The coordinate sum of a target is

\[
 (c+r)+(m-c)+x+(m-u)=2m+(r-u+x),
\]

so its upper depth is `d=r-u+x`.  At depth `R`, set `a=r-u`; then
`x=R-a`.  The original inequalities are equivalent to

\[
 1\le a\le R,
 \qquad
 \max(a,R-a+1)\le r\le R.
\]

Indeed, `r>=a` is `u=r-a>=0`, and `r>=R-a+1` is the integral form of
`x=R-a<r`.  For fixed `a`, the number of choices is

\[
 R-\max(a,R-a+1)+1=\min(a,R-a+1).
\]

The triples are distinct because `r`, `x`, and `u` can be recovered from
the first, third, and fourth target coordinates.  Therefore the exact count
is

\[
 \sum_{a=1}^R\min(a,R-a+1)
 =\left\lfloor{(R+1)^2\over4}\right\rfloor.
\]

For `R=2t` this is `t(t+1)`; for `R=2t-1` it is `t^2`, agreeing with the
floor formula.

All these targets have the same coordinate sum, and distinct comparable
points in a product of chains have strictly different sums.  They therefore
form an antichain.  For each physical right endpoint, interval maxima of
suffixes ending there form an increasing chain as the left endpoint moves
left.  It can contain at most one target from this antichain.  Thus distinct
targets require distinct right endpoints, proving

\[
 n\ge\left\lfloor{(R+1)^2\over4}\right\rfloor.
\]

This proof uses neither canonical providers nor the triangular alphabet.
In the Boolean prefix encoding it is the same inclusion-chain argument, so
arbitrary additional mask entries do not evade it.

## 5. Canonical side chains and exact width

Fix `u` and one occurrence of `P_u`.  Assign a canonical target using that
occurrence to the left or right side according to the selected occurrence of
its arm `E_(r,x)`.  Along one side, let `E_(r_1,x_1)` be nearer the peak than
`E_(r_2,x_2)`.  By the valid shrinking argument, the interval from `P_u` to
the farther arm is itself a witness for `Z_(u,r_2,x_2)` and contains the
nearer arm.  Consequently

\[
 E_{r_1,x_1}\le Z_{u,r_2,x_2}.
\]

Comparison of coordinates directly gives

\[
 r_1\le r_2,\qquad x_1\le x_2.
\]

Thus each oriented side of each `P_u` occurrence is a chain in

\[
 \mathcal A_u=\{(r,x):u<r\le R,\ 0\le x<r\}
\]

under componentwise order.  This direct comparison is the needed local
repair to the source proof: citing Lemma 1 would require every intervening
entry to belong to the triangular alphabet, whereas the domination argument
allows arbitrary entries.

Assign each target once to one selected peak occurrence and one side.  The
result is a partition into at most `2k_u` chains, so Dilworth's chain-cover
form gives

\[
 2k_u\ge\operatorname{width}(\mathcal A_u).
\]

### Exact width calculation

Let `h=ceil(R/2)`.  The diagonal

\[
 r+x=R
\]

inside `A_u` has

\[
 \min(R-u,h)
\]

members: its integer range is

\[
 \max(u+1,\lfloor R/2\rfloor+1)\le r\le R.
\]

Along it, increasing `r` decreases `x`, so it is an antichain.

Conversely, let an antichain have `q` members.  Equal `r` values are
comparable, so order them with

\[
 r_1<r_2<\cdots<r_q.
\]

Incomparability forces

\[
 x_1>x_2>\cdots>x_q\ge0,
\]

whence `x_1>=q-1`.  Since `x_1<r_1`, integrality gives `r_1>=q`; strict
integer increase gives `r_q>=r_1+q-1>=2q-1`.  As `r_q<=R`,

\[
 q\le\left\lfloor{R+1\over2}\right\rfloor
   =\left\lceil{R\over2}\right\rceil=h.
\]

There are only `R-u` possible `r` rows, so also `q<=R-u`.  The lower and
upper bounds coincide:

\[
 \boxed{\operatorname{width}(\mathcal A_u)=\min(R-u,h).}
\]

No Ferrers-poset boundary case is missing from this argument.

## 6. Canonical peak lower bound and constants

Summing `2k_u>=min(R-u,h)` for `u=0,...,R-1` and putting `q=R-u` gives

\[
\begin{aligned}
 \sum_{u=0}^{R-1}k_u
 &\ge {1\over2}\sum_{q=1}^R\min(q,h)\\
 &={1\over2}\left({h(h+1)\over2}+(R-h)h\right)\\
 &={1\over2}\left(hR-{h(h-1)\over2}\right).
\end{aligned}
\]

The parity forms of this displayed real-valued lower bound are

\[
 \begin{cases}
 (3R^2+2R)/16,&R\text{ even},\\
 (3R^2+4R+1)/16,&R\text{ odd}.
 \end{cases}
\]

Hence its leading constant is exactly `3/16`.  Since each `k_u` is integral,
one may strengthen the finite bound by summing
`ceil(min(R-u,h)/2)`, but the source's weaker displayed inequality is fully
valid.

Across `c=0,...,m-1`, the radii are `R=m-c=1,...,m`.  Peak labels belonging
to different pairs `(c,u)` are distinct: equality of

\[
 P_{c,u}=(c+u,m-c,0,m-u)
\]

first forces equality of `c` from the second coordinate and then equality of
`u`.  Thus a physical occurrence cannot satisfy two different peak counts,
and summing the per-`c` bounds is legitimate.  More precisely,

\[
 \sum_{R=1}^m(3/16+o(1))R^2
 ={1\over16}m^3+O(m^2)
\]

for the displayed nonintegrally-rounded lower bound.  In particular the
source's `Omega(m^3)` conclusion is correct.

Only

\[
 \sum_{R=1}^mR={m(m+1)\over2}=O(m^2)
\]

distinct provider peak labels `P_(c,u)`, `0<=u<R`, participate in this
lower bound.  Therefore, in an architecture already containing every middle
point once, all but `O(m^2)` of the forced `Omega(m^3)` occurrences are
genuine repetitions.

### Scope

This conclusion assumes every target has a selected witness containing its
exact canonical pair `P_u,E_(r,x)`.  It allows arbitrary ordering, duplicated
arms, duplicated peaks, and arbitrary extra entries.  It does **not** apply
to a witness using a nonpeak cell with first coordinate `u` to supply
`min s=u` and a different peak to supply `min y=0`.  Nor does it forbid
cross-`c` coupling or realization below a factored middle row.  The scope
statements in the source are accurate.

## 7. Reflection and alphabet disjointness

The map

\[
 \vartheta(a,b,d,e)=(m-b,m-a,m-e,m-d)
\]

is an involution, reverses componentwise order, and satisfies

\[
 \vartheta(X\vee Y)=\vartheta(X)\wedge\vartheta(Y).
\]

Direct substitution gives exactly

\[
\begin{aligned}
 \vartheta(E_{c,r,x})&=(c+x,m-c-r,r,m-x),\\
 \vartheta(P_{c,u})&=(c,m-c-u,u,m),\\
 \vartheta(Z_{u,r,x})&=(c,m-c-r,u,m-x).
\end{aligned}
\]

For fixed `r`, independent `u,x in {0,...,r-1}` give the entire reflected
lower fibre.  Reversal preserves physical contiguity, so applying
`vartheta` to a reversed upper witnessing interval turns its join into the
claimed lower meet.  The sequence

\[
 W\Vert\vartheta(\operatorname{rev}W)
\]

is fixed by reverse-complement because this operation is an involution and
interchanges its two halves.

For `W=W_R^+`, its length is `2R(R+1)`.  A sharper blockwise concatenation
places `F_r` immediately before `vartheta(rev F_r)`.  The former ends in
`P_(c,0)` and the latter begins in the same fixed point, so the two identical
occurrences may be merged without damaging an upper interval ending there
or a lower interval beginning there.  This saves one occurrence for each
radius and gives

\[
 \sum_{r=1}^R(4r-1)=2R^2+R.
\]

This blockwise merged sequence need not have the global self-dual ordering
of the unmerged two-half sequence; the source claims only its shorter
coverage and length.

These are the **new** cross-radius blocks `F_r` from (3.1) and their
reflected reverses.  Calling them the original upper and lower fan blocks
would be false: their peak spines deliberately borrow peaks from radii
`r-1,...,0`.  The revised wording in the source is therefore necessary and
is now correct.

### Disjointness

If an upper arm equals a reflected arm, even allowing two different
`c,c'`, then

\[
 E_{c,r,x}=\vartheta(E_{c',s,y})
\]

forces, from the third and fourth coordinates, `s=x` and `y=r`; the first
coordinate then forces `c=c'`.  The domain inequalities would require both
`x<r` and `r<s=x`, a contradiction.  An upper arm cannot equal a reflected
peak because the latter has fourth coordinate `m`, while every upper arm has
fourth coordinate `m-r<m`.  Dually, an upper peak cannot equal a reflected
nonpeak arm.  Finally,

\[
 P_{c,u}=\vartheta(P_{c',v})
\]

forces `u=v=0` from the third and fourth coordinates and then `c=c'`.

Thus the upper and reflected canonical alphabets are globally disjoint
except for the fixed boundary labels `P_(c,0)` (one for each fixed
`c`-diagonal).  Within the fixed-`c` problem this is exactly the single point
claimed in the source.

## 8. Final length accounting and theorem ledger

Summing the explicit one-sided word over `c`, equivalently over
`R=1,...,m`, gives

\[
 \sum_{R=1}^mR(R+1)
 =\sum R^2+\sum R
 ={m(m+1)(m+2)\over3},
\]

so (7.1) and its cubic order are correct.

| Item | Verdict | Qualification |
|---|---|---|
| Lemma 1, affine bounding box | proved | Applies directly to intervals in the triangular alphabet. |
| Cross-radius provider identity | proved with revised wording | `P_(c,u)` is the peak at `H=c+u`, not the original `V_t` of the radius-`r` fan; the coordinate join is nevertheless exact. |
| Theorem 2, `R(R+1)` word | proved | Every proposed shortened interval is contiguous and uncontaminated. |
| Theorem 3, exact depth-`R` antichain count | proved | Unrestricted with respect to word alphabet and witnesses. |
| Canonical provider shrinking | proved | Uses endpoint join plus containment in the original witness. |
| Lemma 4, one-side chain | proved after a one-line proof repair | Use direct domination, not Lemma 1, when arbitrary intervening entries are allowed. |
| Exact `width(A_u)` | proved | Equals `min(R-u,ceil(R/2))`. |
| Theorem 5, peak multiplicity | proved | Applies only when each selected witness contains its exact canonical pair. |
| Summed cubic obstruction | proved | Distinct `c,u` peak labels prevent cross-counting; leading displayed constant is `1/16` after summing over `c`. |
| Proposition 6, reflection | proved | Uses the new `F_r` blocks and their reflected reverses; produces meets for the lower family, not joins. |
| Alphabet disjointness | proved | One fixed boundary label per `c`; no cross-`c` exception. |
| Lengths (3.4), (3.6), (6.5), (7.1) | proved | All constants and parity cases check. |

The fixed-`c` triangular problem is therefore genuinely `Theta(R^2)`, and
canonical two-provider peak sharing cannot have only `O(R)` peak
occurrences.  The audit does not extend this obstruction to noncanonical
three-provider witnesses, cross-`c` intervals, or factor-level realizations;
those remain legitimate escape routes.

## 9. Addendum: audit of Proposition 3a

### Verdict

Proposition 3a is correct provided its first sentence is read literally as:

> the word is a permutation of the triangular alphabet `T_R`, with each
> triangular cell occurring once and with no additional entries.

This is what the title, proof, and phrase "exact-once triangular
permutation" intend.  The wording "a word containing every triangular cell
exactly once" is otherwise logically too broad: it could also contain
arbitrary additional nontriangular entries, and the proof would no longer
force an all-peak block.  Under the permutation interpretation, the proof
has no gap.

### Peak-block forcing

For `x=0`, the bounding-rectangle criterion forces every entry in a target
witness to have second cell coordinate `y=0`; these are exactly the peak
cells `P_s`.  Moreover, a witness for `(u,r,0)` must contain the unique
occurrences of both `P_u` and `P_r`.

The target `(0,R,0)` therefore makes the entire physical interval between
`P_0` and `P_R` peak-only.  For every intermediate `s`, the targets
`(0,s,0)` and `(s,R,0)` make the intervals from `P_s` to both endpoints
peak-only.  Taking their union shows that the convex hull of all peak
positions contains only peaks.  Since the word is a permutation and there
are exactly `R+1` peaks, all

\[
 P_0,P_1,\ldots,P_R
\]

form one contiguous block.  This justifies the step at (4.6), including the
case where an intermediate `P_s` initially lies physically outside the
interval between `P_0` and `P_R`.

For each `i`, a witness for `(i,i+1,0)` can contain only peak labels with
index in `[i,i+1]`, and it must contain both unique extremes.  Hence `P_i`
and `P_(i+1)` are adjacent.  A linear order on `R+1` vertices has exactly
`R` adjacency slots, and all `R` edges of the path

\[
 P_0-P_1-\cdots-P_R
\]

are required.  The peak block is consequently this order or its reverse;
there is no alternative interleaving.

### Interior-target contradiction

Assume the order is `P_0,...,P_R`.  Every nonpeak lies strictly outside the
peak block.  Any interval containing a left-side nonpeak and a peak must
cross `P_0`, so its bounding box has minimum first cell coordinate zero.
Any interval containing a right-side nonpeak and a peak must cross `P_R`, so
its maximum first cell coordinate is `R`.  An interval meeting both sides
has both defects.  The reversed peak order exchanges left and right and has
the same conclusion.

Every target with `x>0` needs a nonpeak to attain `max y=x` and a peak to
attain `min y=0`.  For `R>=3`, the valid target

\[
 (u,r,x)=(1,2,1)
\]

has neither boundary value `u=0` nor `r=R`, so none of the three physical
placements of its necessary nonpeak(s) can witness it.  The contradiction is
complete and has no endpoint loophole.

The threshold is natural: for `R=2`, the same target has `r=R` and does not
contradict the boundary geometry.  Indeed the exact-once order

\[
 E_{2,1},P_2,P_1,P_0
\]

covers every triangular target for `R=2`, providing a useful sanity check.

Thus Proposition 3a proves that repetition (or use of entries outside the
triangular alphabet) is necessary for `R>=3`, even when witnesses need not
use the canonical provider pair.  It does not prove a quantitative
repetition lower bound, exactly as the source states.
