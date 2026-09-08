# Independent audit: architecture-free additive-`C` diagonal normalization

**Date:** 2026-08-03  
**Audited theorem:**
`MATH_THEOREM_ARCHITECTURE_FREE_ADDITIVE_C_DIAGONAL_RUN_NORMALIZATION_20260803.md`  
**Audited theorem SHA-256:**
`93bd747e62b84cd423e1ccb31ae161a24e70635561c159142322d47b0dfabbca`  
**Verdict:** **GO after two proof-clarity corrections.**  The theorem's
architecture-free conclusion

\[
  P(A)=\sum_i|A_i|=\Omega_C(rW)
\]

is valid for every universal nonzero OR word of length
`W+d(k)+C`.  The audit found no hidden flat-row, cyclic, Johnson, or
resident-carrier hypothesis.  It does not prove an upper construction.

The two corrections made during this audit are:

1. first witnesses are now explicitly replaced by the *least* right
   endpoint attaining rank `r`, so their proper prefixes are exactly the
   lower cells of the selected column;
2. the informal assertion `epsilon_k<1 up to a negligible correction` is
   replaced by the exact inequality
   \[
      \epsilon_k<1-{1\over W}{d\choose2}<1,
   \]
   and the boundary-marker convention in the clipped-run lemma is stated
   literally.

## 1. First-witness normalization and endpoint order

For every rank-`r` target choose a witnessing interval `[a,b_0]`, and take
the least `b<=b_0` for which the prefix union from `a` has rank `r`.
Because this new union is a subset of the old rank-`r` target and has the
same cardinality, it equals that target.  Every shorter prefix has rank
strictly below `r`.

Two normalized witnesses with the same start are nested, so their
equal-rank values would coincide.  If starts increase while ends fail to
increase, the intervals are again nested and their values again coincide.
Thus the `W` starts and the `W` ends are both strictly increasing.  For an
increasing `W`-tuple in `[W+e]`, its `t`-th entry lies in `[t,t+e]`; hence

\[
 0\le x_t=a_t-t\le e,
 \qquad
 0\le y_t=b_t-t\le e,
\]

with `x_t,y_t` nondecreasing.  Therefore `z_t=e-y_t` is nonincreasing and

\[
 h_t=b_t-a_t=e-x_t-z_t.
\]

This verifies the shortening, strict ordering, and displacement identities.

## 2. The unselected-column cap and exact displacement budget

For a physical start column `i`, let `f_i` be the number of initial
interval cells of rank below `r`, and let its first-rank-`r` deadline be
`F_i=i+f_i` (or the terminal dummy deadline for an all-lower column).
The standard containment argument gives `F_{i+1}>=F_i`.  The `W` distinct
middle targets force at least `W` distinct finite deadlines, and the usual
room-before/room-after argument then gives

\[
 f_i\le e=L-W
\]

for every column.  This applies in particular to every unselected start.

There are exactly `e` unselected starts.  Hence their lower cells number at
most `e^2`.  Any strict-lower target not appearing in a selected column must
be represented in one of these cells.  At a selected start `a_t`, the
lower cells are precisely the `h_t` proper prefixes of its normalized
middle witness.  Consequently

\[
  \sum_t h_t\ge \Lambda-e^2.
\]

Substitution of `h_t=e-x_t-z_t` gives

\[
 \sum_t(x_t+z_t)
 \le eW-\Lambda+e^2
 = (C+\epsilon_k)W+e^2.
\]

For `d=0`, `epsilon_k=0`.  For `d>=1`, minimality of `d` yields

\[
 (d-1)W+{d\choose2}<\Lambda,
 \qquad
 \epsilon_k={dW-\Lambda\over W}
 <1-{1\over W}{d\choose2}<1.
\]

The defining inequality for `d` also bounds `epsilon_k` below by
`-{d+1\choose2}/W`; thus the displayed displacement budget is genuinely
`O_C(W)` with no asymptotic sign convention hidden in it.

Because `{t:z_t>K}` is a prefix and `{t:x_t>K}` a suffix, deleting their
union leaves one index interval and removes at most twice the displacement
budget divided by `K+1`.  On the survivor, the two integer monotone
sequences have at most `2K` total positive jumps.  This verifies the
macroscopic `2K+1` diagonal-block extraction and depth `>=e-2K`.

## 3. Exact diagonal blocks and the right trim

A block boundary is placed whenever the start or end increment exceeds
one.  The total excess of all start increments is at most `e`, as is the
total end excess.  Hence there are at most `2e` cuts and at most `2e+1`
blocks.  Inside a block, both endpoints advance by one, so its depth `h`
is fixed.

For a block with owner indices `p,...,q`, length `m=q-p+1`, retain only
`p,...,q-h`.  The last retained source interval ends at

\[
 b_{q-h}=a_{q-h}+h=a_q,
\]

the final start of the original block.  The next block starts strictly
after `a_q`.  Thus the retained source spans of distinct blocks are
pairwise disjoint.  At most `h` owners, each with `h` proper-prefix cells,
are removed, so the loss is at most `h^2` per block.

It follows that

\[
 N=W-O(e^2),
 \qquad
 Q=\sum_bh_bn_b\ge\Lambda-O(e^3),
\]

and

\[
 \sum_b(e-h_b)n_b=O_C(W)+O(e^3).
\]

Every shallow owner with `h_b<e/2` spends more than `e/2` of this deficit.
Hence shallow blocks contain `O_C(W/e)` owners and only `O_C(W)` lower
cells.  Removing them, together with the unselected-column and trim losses,
leaves all but `O_C(W)` named lower targets represented in the deep rows.
If `H` is the total coordinate--cell incidence mass of those rows, then

\[
 H\ge M-O_C(kW).
\]

This step uses only that a missing target has rank at most `r-1`; repeated
cells cannot invalidate the lower bound.

## 4. Independent check of the clipped-run formula

Fix a depth-`h` row

\[
 T_j=\bigcup_{i=j}^{j+h}A_i,
 \qquad 1\le j\le n.
\]

For an internal positive coordinate run `[s,t]`, absence at `s-1` and
presence at `s` force an actual source marker at `s+h`; presence at `t`
and absence at `t+1` force one at `t`.  Therefore the run length is at
least `h+1`.  Between consecutive retained markers at distance `g`, owner
positivity forces `g<=h+1`, and the gap lengths sum to

\[
 t-(s+h)=L-h-1.
\]

For proper-prefix length `q`, a marker at source position `z` serves starts
in `[z-q+1,z]`.  A gap of length `g` therefore misses exactly
`(g-q)_+` potential starts.  Since `g<=h+1`,

\[
 \sum_{q=1}^h(g-q)_+={g\choose2}.
\]

Summing the no-gap baseline over `q=1,...,h` gives

\[
 h\left(L-{h+1\over2}\right)-\sum_g{g\choose2}.
\]

For a run meeting the left boundary, insert the canonical virtual marker
at `s+h`; for one meeting the right boundary, insert it at `t`.  Actual
markers discarded outside those canonical endpoints can affect only the
first or last `h` starts in each of the `h` prefix rows.  Hence the total
boundary correction is at most `2h^2`.  An internal run shorter than
`h+1` is impossible; a short boundary run has at most `hL<h(h+1)`
incidences.

There are at most two boundary runs per coordinate per block.  Since there
are at most `2e+1` blocks, all short/clipped corrections total
`O(ke^3)=o(W)`.  This verifies the finite-row lemma including its boundary
scope.

## 5. Run bound and retained rank mass

The deep rows contain `W-O_C(W/e)` rank-`r` owners.  Removing their short
boundary runs costs only a polynomial number of incidences, so the total
long-run owner length is

\[
 L_+=rW-O_C(eW),
\]

using `r/e=Theta(e)` for fixed `C`.  Summing the clipped-run upper bound,
discarding its nonnegative convex loss, and using `h>=e/2` yields

\[
 H\le erW-{e^2\over8}R+O(ke^3).
\]

Also

\[
 r\Lambda-M=O(kW).
\]

Indeed, after division by `2^k` this is bounded by the first absolute
central moment of a `Bin(k,1/2)` variable, which is `O(sqrt k)`; Wallis
gives `2^k=O(sqrt k W)`.  Since `eW-\Lambda=O_C(W)`, it follows that
`erW-M=O_C(kW)`.  Comparing the upper and lower bounds on `H`, and using
`e^2=Theta(k)`, proves

\[
 R=O_C(W).
\]

The short boundary runs add only `O(ke)`.  Every transition between
distinct equal-rank owners creates at least one new positive run, so the
retained rows have `O_C(1)` births per transition on average.  No claim of
Johnson adjacency or one birth per transition is used.

## 6. Convexity and injection into literal occurrence mass

For each augmented long run,

\[
 \sum g=L-h-1.
\]

Thus, over all such runs,

\[
 S=L_+-\sum_\rho(h_\rho+1)
   =rW-O_C(eW)
   =(1-o(1))rW.
\]

Retaining the convex loss in the incidence inequality gives

\[
 J=\sum_g{g\choose2}\le erW-H+O(ke^3)=O_C(kW).
\]

For `G` positive integer gaps, Cauchy--Schwarz gives

\[
 J={1\over2}\left(\sum g^2-S\right)
 \ge {1\over2}\left({S^2\over G}-S\right),
\]

and hence

\[
 G\ge {S^2\over S+2J}=\Omega_C(rW).
\]

The augmented marker count is `R+G`.  At most two virtual markers are
added to each boundary run, so only `O(ke)` of these markers are virtual.
Within one block, the canonical source intervals belonging to distinct
positive runs of a coordinate are disjoint; different coordinates give
different literal incidences.  Across blocks, Section 3's trimmed source
spans are disjoint.  Therefore every retained actual marker is a distinct
pair `(source position, coordinate)` and is counted at most once in
`P(A)`.  Consequently

\[
 P(A)\ge R+G-O(ke)=\Omega_C(rW).
\]

This verifies both the virtual-marker subtraction and the absence of
cross-block or cross-run double counting.

## 7. Exact scope

The proof establishes a necessary density property for arbitrary
`B(k)+C` words.  It does **not** establish:

* one global depth-`e` resident row;
* a cyclic or Johnson carrier;
* `W+O_C(1)` positive runs;
* the sharp resident-factor density constant;
* a named lower compiler, upper deck, or common-cap router;
* `nu(k)<=B(k)+C` for any fixed `C`.

Those exclusions are essential.  Subject to them, the theorem is
independently proof-safe.
