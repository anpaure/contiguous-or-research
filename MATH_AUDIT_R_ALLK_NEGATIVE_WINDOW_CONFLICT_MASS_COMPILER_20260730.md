# Adversarial audit of the negative-window conflict-mass compiler theorem

Date: 2026-07-30  
Audited file:
`MATH_THEOREM_R_ALLK_NEGATIVE_WINDOW_CONFLICT_MASS_COMPILER_20260730.md`  
Method: proof audit only; no search, SAT, or numerical enumeration.

## 0. Verdict

The collision identity, partial-atlas equivalence, bounded-rank conflict
hypergraph, exact deficiency identity, product-mass alteration, and
separated-seam ledger are valid under their stated hypotheses.

The decisive point is that conflict edges are defined only among
**transversal** candidate families.  This makes their probabilities products
over distinct target parts and makes target deletion a monotone operation.
Without that word, Theorem 6.1 would be false as written because a
hyperedge containing two alternatives for one target can never occur in the
sampled selector.

The result is a conditional `B(k)+O(1)` theorem, not an unconditional
all-dimensional bound.  Its unproved hypothesis is the existence of one
upper-complete resident chronology with bounded independent-transversal
deficiency, or of one candidate product distribution with bounded conflict
mass.

## 1. Audit of the deadline/collision identity

Let `I=[a,b]` have length at most `d` in a word of length `W+d`.  The set of
middle-window starts containing it is

\[
 [\max(0,b-d),\min(a,W-1)]\cap\mathbb Z.
\]

It is nonempty: `b-d<=a`, `b-d<=W-1` because `b<=W+d-1`, and
`0<=a`.  Thus every short interval lies in a `(d+1)`-window and its OR has
rank at most `r`.

There are exactly

\[
 \sum_{j=1}^d(W+d-j+1)=dW+{d+1\choose2}=\Lambda+\sigma
\]

short interval occurrences.  If `h` lower values are absent, the lower
occurrence mass is `Lambda-h+C_<`; the remaining occurrence mass is exactly
`R_=`.  Therefore

\[
 h=C_<+R_=-\sigma.
\]

No injectivity or equality-case assumption enters this count.  Appending
the `h` absent lower masks is safe because all old intervals remain
contiguous.  Hence Corollary 2.2 is valid.

## 2. Audit of the partial negative-window criterion

For a chosen target interval `theta(S)`, every coordinate outside `S` must
be absent at every position of that interval.  Intersecting all such
negative demands with the maximal erosion gives exactly `Q_x(theta)`.

Necessity is sound: an actual antecedent is contained in this maximal word,
so it supplies the positives in every middle window and target interval and
supplies a coordinate at every source position.

Sufficiency is also sound:

* containment in `P` forbids every coordinate outside a prescribed middle
  state;
* (3.5) supplies every prescribed middle coordinate;
* the negative windows delete every coordinate outside a selected target;
* (3.6) supplies every coordinate inside it; and
* (3.7) is exactly source nonemptiness.

Deleting a selected target removes one negative interval and one positive
obligation.  It can therefore only enlarge every surviving `Q_x` and cannot
invalidate another selected target.  The asserted downward closure is
valid.

## 3. Audit of the hypergraph rank

Every incompatibility is one of three types.

1. A middle requirement loses its allowed occurrences in at most `d+1`
   positions.  One selected negative interval per position gives an
   incompatible subfamily of size at most `d+1`.
2. A selected target coordinate loses its allowed occurrences on an
   interval of length at most `d`.  Its own candidate plus one negative
   interval per position gives size at most `d+1`.
3. A source position is emptied.  One selected interval deleting each
   coordinate of `P_p` gives size at most `|P_p|`.

An inclusion-minimal incompatible family equals the corresponding chosen
subfamily, proving rank at most
`max(d+1,max_p |P_p|)`.  The reduction to at most `r` uses both `d<r` and
`P_p subseteq T_i` for at least one middle window, hence `|P_p|<=r`.

No interval-Helly claim is used.  In particular, the theorem does not say
that pairwise compatibility is sufficient.

## 4. Audit of the exact deficiency identity

From any antecedent, selecting one actual witness for each covered lower
value gives an independent partial transversal, so `tau<=h`.  From any
independent partial transversal, the maximal negative-window construction
gives an antecedent covering at least its selected targets, so `min h<=tau`.
These two inequalities have the correct directions and prove equality.

The equality is fixed-chronology only.  It neither classifies universal
words with positive deadline slack nor says that a length-`B+c` word has a
length-`B` flat prefix.

## 5. Audit of the product-mass alteration

Because every edge uses distinct target parts,

\[
 \Pr(E\text{ is selected})=\prod_{v\in E}\pi(v).
\]

Linearity of expectation gives `E Z=Psi` without any independence between
different conflict events.  Some integer outcome has
`Z<=floor(Psi)`.

Deleting one target part from each present edge removes at most `Z` target
parts.  If the remainder were incompatible, it would contain an
inclusion-minimal conflict edge.  That edge was present before deletion and
was supposed to have been hit, a contradiction.  Thus alteration produces
one integral compatible selector; no LP rounding is present.

The zero-mass representation of `tau` is also exact.  One direction uses
the preceding sampling with `Z=0`; the other uses Dirac measures on an
optimal independent partial transversal.

The asymmetric local criterion is the standard finite conditional
induction, but its dependency graph is valid here for a specific reason:
each target part contributes one independent random variable, and two
conflict events with disjoint target-part sets are jointly independent even
if their physical intervals overlap.  The displayed induction conditions
only on smaller families, so the denominator is bounded by the product of
`1-y_F`; no unjustified mutual independence of neighboring events is used.
The symmetric constant in (6.11) is the exact value obtained from
`y=1/(Delta+1)`.

The ordinary-Hall specialization needs the full protected sandwich stated
in (7.0): every fixed interval has the same union in `C` and `P`, or the
upper envelope has first been intersected with every active fixed-pin label
and its central and protected upper equalities have then been reverified.
Merely knowing that `C` realizes a protected interval would not suffice,
because raising an unmatched position from `C_p` to an unrestricted `P_p`
could add a forbidden coordinate.  With (7.0), the sandwich argument is
valid.

## 6. Audit of the seam identity

At a separated seam with at least `d-1` letters available on each side, a
crossing interval of length `j` is determined by choosing `1,...,j-1`
letters on the left.  Hence the exact count is

\[
 \sum_{j=2}^d(j-1)={d\choose2}.
\]

Separation by at least `d` ensures that no short interval crosses two seams.
Therefore every short interval is internal or belongs to one seam ledger,
and the hole identity (8.2) follows literally.  If these separation or
piece-length hypotheses fail, the report correctly retains only the full
multi-seam interval ledger and withdraws the closed count.

The bound `B+s binom(d,2)` assumes an old lower-complete assembly with the
same internal pieces.  It is not a theorem from `s` seams alone.  The exact
condition for `B+O(1)` is service of all but constantly many internally
exposed target values.

Likewise, the seam ledger does not create the physical prefix.  Theorem 8.1
is conditional on an already supplied common `A` satisfying `D^dA=T`; an
owner-piece rethreading without such an antecedent has no compiler
consequence.

## 7. Final scope

Validated:

* exact unrestricted `COMP_d(T)` countercondition via a bounded-rank
  independent transversal;
* exact fixed-chronology lower-hole number `tau(T)`;
* rigorous conflict-mass implication `B+|O|+floor(Psi)`;
* exact seam-provider condition.

Unsupported and not claimed:

* automatic bounded conflict mass from PBBS support;
* automatic bounded conflict mass from constant seam count;
* a uniform all-`k` chronology satisfying the criterion;
* necessity of `tau(T)<=C` for arbitrary length-`B+C` words.

The theorem therefore supplies a precise reusable compiler target and a
sharp scoped obstruction, but not yet the conjectural all-`k` upper bound.
