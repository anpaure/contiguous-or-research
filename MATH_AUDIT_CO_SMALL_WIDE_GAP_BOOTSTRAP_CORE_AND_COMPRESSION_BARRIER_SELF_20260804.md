# Self-audit: wide-gap optional bootstrap core and compression barrier

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_CO_SMALL_WIDE_GAP_BOOTSTRAP_CORE_AND_COMPRESSION_BARRIER_20260804.md`

No computation or finite search is used.

## 1. Forbidden-bank scale and trace separation

Owners with `h` `K`-coordinates number

\[
 \binom{m-1}h\binom mh.
\]

Multiplication by `m` overcounts their lower facets, so (1.2) is safe.
For `d=O(sqrt m)`, its binary logarithm is `O(d log m)=o(m)`.

A lower facet under `h<d` has at least `m-h-1>=m-d` external
coordinates.  Low noninterval paths use trace size at most `m-d-1`, so
they are disjoint.  The high greedy packing already allows a much larger
forbidden bank.  Thus the strengthened avoidance does not reuse or alter
the probabilistic spread proof.

## 2. Top cyclic count

Top lower colours have proper cyclic-interval external traces of lengths
`1,...,m-2`.  For owner trace `S`, at most one top colour has trace `S`.
For external deletion `e`, a top colour can occur only if `S-e` is one
cyclic interval.  Equivalently, `(E setminus S) union {e}` is a cyclic
interval.  A fixed nonempty set has at most two one-coordinate interval
completions: the two endpoints if it is already an interval, and at most
one missing internal point otherwise.  Hence at most two external
deletions contribute.  The exceptional `h=0` traces have sizes
`m,m-1`, outside the top lower palette.  Therefore `z_U<=3` is valid for
the entire newly forbidden range, not just `h<=2`.

For `h>=d`, the prior exact-trace argument gives `z_U<=m-h+2`, so in both
ranges `g_U>=d-2`.

## 3. Bootstrap degree

At the minimal optional maximizer, deleting one vertex must strictly
decrease `Psi`.  Since deletion refunds two units and removes one overflow
unit per active owner, at least three active owners are necessary.

In one active owner,

\[
 b_U\ge g_U-c_U+1\ge g_U-1.
\]

After excluding `x`, at least `g_U-2>=d-4` other optional facets of that
owner remain in the bank.  They are Johnson neighbours.  Neighbour sets
from distinct owners over `x` are disjoint because `x union y` uniquely
determines their common owner.  The factor three and (3.4) are therefore
exact.  No expansion conclusion stronger than minimum degree is inferred.

For the bouquet statement, the `b_U` selected optional facets of one owner
are exactly the rank-`m-1` interval between `C_U=U setminus R_U` and `U`.
Distinct owners over `x` share no other rank-`m-1` facet, so the three
petals meet only at `x`.  The petal size lower bound is `g_U-1>=d-3`.

For a block deletion `D`, the overflow identity

\[
 (b-s)_+-(b-e-s)_+=\min(e,(b-s)_+)
\]

is valid for `0<=e<=b`.  Strict minimality therefore gives (3.10).
Because the cut surplus is integral, deletion of one owner token leaves
ordinary non-strict Hall.  Bipartite `b`-matching integrality proves the
robust internal matching statement.  Two lower vertices determine at
most one common owner, so the active incidence graph is indeed
`C_4`-free.

For the quadratic bound, total positive owner capacity is `2n+delta` and
each owner capacity is at most two, so there are at least `n+1` positive
owners.  Each has at least `D=d-3` incident core vertices.  Since a point
pair occurs in at most one owner, pair counting gives

\[
 (n+1)\binom D2\le\binom n2,
\]

whose least integral solution is `n>=D(D-1)+2`.

At equality the numerical pair-count slack is exactly one.  Any additional
owner or any owner degree above `D` would consume more than that slack, so
there are exactly `n+1` degree-`D` owners and exactly one non-co-owned point
pair.  Removing one endpoint leaves a Johnson clique.  A top clique forces
every block containing three clique members to have the same owner; a
star clique lets one owner contain at most two clique members.  With only
one outside point, both contradict owner degree `D>=4`.  Thus the Boolean
bound improves to `D(D-1)+3`.

## 4. Exchange identity

For `f_U(b)=(b-s_U)_+`, removal of `x` changes `f_U` by minus one exactly
when `b>=s_U+1`; addition of `y` after the removal changes it by plus one
exactly when the new occupancy is at least `s_U`.  The `-2|B|` term is
unchanged by an exchange.  This proves (4.3).

At a global maximizer the exchange difference cannot be positive.  At a
lexicographically minimal maximizer, equality is impossible for a
downward replacement.  Hence the strict locked-inversion inequality is
correct.

Only optional elements can be exchanged this way.  The theorem now
states separately that shiftedness of the complete complement also
requires all shifted images of forced `Z`-elements to be present.  It does
not infer shiftedness from the optional exchange criterion alone.

## 5. Scope

The theorem proves a stronger reservoir can be selected and classifies a
remaining positive optional obstruction as a wide-gap bootstrap core with
an exact compression barrier.  It does not prove:

* absence of that core;
* shiftedness or colex form of a maximizer;
* residual factor extension;
* the all-dimensional OR-word theorem.

**Self-audit verdict:** GO within the stated scope.
