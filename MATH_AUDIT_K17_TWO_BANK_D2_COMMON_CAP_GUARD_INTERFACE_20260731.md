# Audit of the `K17` two-bank `D2` common-cap guard interface

Date: 2026-07-31  
Verdict: **PASS, conditional scope enforced**

Audited theorem:
`MATH_THEOREM_K17_TWO_BANK_D2_COMMON_CAP_GUARD_INTERFACE_20260731.md`.

## 1. Inversion and boundary semantics

For a proposed `D2` row `Z` of length `L-2`, every realizing base letter at
position `p` is contained in the intersection of all three-windows through
`p`.  Hence the envelope in (1.2) is genuinely maximal, including the
truncated first two and last two positions.  Taking the envelope itself
proves sufficiency.  No cyclic identification is legal after opening.

Coordinatewise, three-window erosion followed by three-window dilation
recovers precisely the endpoint-touching runs and the internal runs of
length at least three.  Thus the run formulation is exact, but it does not
imply envelope nonemptiness: that is correctly retained as a separate row.

At a bank or socket cut between `Z_(c-1)` and `Z_c`, only envelope positions
`c,c+1` mix the two sides, but those positions occur in four row equations.
The theorem correctly requires replay of rows `c-2,...,c+1` rather than
pasting two bankwise inversions.

## 2. Count audit

The nonempty lower ideal through rank eight has

\[
 \sum_{r=1}^{8}{17\choose r}=65535,
 \qquad
 \sum_{r=1}^{7}{17\choose r}=41225.
\]

If `Z` has `a` owner rows and `W+1-a` distinct facet rows, the uncovered
rank-eight population is

\[
 {17\choose8}-(W+1-a)=a-1.
\]

Therefore the residual population is `41224+a`.  A word of length
`L=24313` has `L` singleton and `L-1` adjacent-pair cells, totaling `48625`,
so the difference is exactly `7401-a`.

For the repaired forest, the frozen materialization has `3815` owners in
`106` marked components.  A path uses `105` connector owners, giving the
conditional value `a=3920`; hence

\[
 41224+a=45144,
 \qquad
 48625-45144=3481.
\]

This arithmetic does not prove the path exists.  It is correctly stated as
the compiler ledger **if** the exact marked/complement flow succeeds.
The independently frozen endpoint audit in fact forces at least four
noncatalogue socket actuators.  Therefore `a=3920` is only the one-token,
token-neutral baseline: a net increase of `delta` owner rows changes the
slack to `3481-delta`, while a more general rank-profile change must be
recounted from the number of distinct direct facets.

The Johnson zipper identity was checked separately.  If the marked path
`P` and complementary path `Q` form one lower-rainbow cyclic owner order,
their `a-1` internal `P` intersections and `b+1` cross/`Q` intersections
partition the complete rank-eight palette.  Consecutive cross/`Q` facets
are two distinct facets of the same owner, so their union gives that owner;
the marked/facet concatenation therefore differentiates to the stated
upper turns, one repeated boundary owner, and all complement owners.  This
is precisely the extra palette condition which ordinary degree b-flow does
not supply.

## 3. Why only short residual cells remain

Every length-three cell is one displayed row `Z_i`.  Every cell of length at
least four contains two adjacent displayed rows.  Under the stated adjacent
union-rank guard its OR has rank at least nine.  Hence an uncovered target of
rank at most eight can use only a singleton or adjacent pair.  This argument
would fail if a direct facet row were duplicated or if an adjacent pair had
union rank at most eight; both are explicit hypotheses.

## 4. Common-cap equivalence and rank

For a selected matching, intersecting the envelope with all labels whose
cells cover a position gives the unique coordinatewise maximal possible
word.  Nonemptiness and exact replay of `D2`, prepins, and selected targets
are therefore necessary and sufficient.  There is no missing forbidden-bit
row: the intersections impose it automatically.

At most three residual cells meet one position: singleton, left pair, right
pair.  A `D2` row has three hosts and a selected short target has at most two.
Consequently all inclusion-minimal failures have size at most three.  The
three labels

\[
 {2,3},\quad{1,3},\quad{1,2}
\]

through an envelope `{1,2,3}` show that the empty-cap bound three cannot be
reduced to two.  Thus marginal matching/Hall is not the exact theorem.

## 5. Guarded Hall audit

The permanent position bit proves cap nonemptiness.  A fixed host for every
`D2`/prepin bit proves those rows.  For a selected candidate and required
bit, the candidate itself contains the bit and the pairwise closure rule
forces every co-selected candidate through its chosen host to contain it.
This proves the selected-target row.  Therefore every saturating matching in
the guarded graph is exact, and ordinary Hall is sufficient.

The guard is deliberately stronger than necessary.  Rank three alone does
not bound dependency, so the theorem correctly draws no generic LLL,
nibble, or total-unimodularity conclusion.

## 6. Scope corrections retained

1. The old `190`-macro frozen closure is not a live calibration: it has the
   independently proved `32` internal `D2` defects in six components.
2. The six occurrence swaps repair that residence obstruction and reduce the
   closure to `154` macros/`3815` owners.  They do not prove labelled path
   existence, complementary connectivity, facet injectivity, upper coverage,
   or common-cap Hall.  The fixed-endpoint clean connector graph has five
   components, so at least four noncatalogue actuators are required.
3. The detached three-path/`5810`-owner construction is only a fallback and
   carries two non-port socket obligations.
4. If a socket option changes `Z` or a short cap, its port and compiler
   choices cannot be optimized separately.  The theorem's exported guard
   tuple must be rebuilt for that option.
5. Once `D2` is exact, every interval of length at least three is fixed.
   Independent constraints on singleton/pair values are not fixed and must
   appear as prepins or candidate restrictions.

No `K17` word, numerical upper bound, or all-dimension theorem follows from
the audited result.
