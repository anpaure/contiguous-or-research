# Adversarial audit: PBBS half-cube word and run-boundary conflict girth

Date: 2026-07-30  
Method: proof audit only; no finite search, SAT, web access, or remote job.

Audited files:

* `MATH_THEOREM_R_ALLK_PBBS_FACET_HALF_CUBE_UPPER_BOUND_20260730.md`;
* `MATH_THEOREM_R_ALLK_RUN_BOUNDARY_CONFLICT_GIRTH_TWO_20260730.md`;
* `MATH_THEOREM_R_ALLK_INTERVAL_CONFLICT_PROFILE_TRANSVERSAL_20260730.md`.

## 0. Verdict

The three new implications are valid under their stated hypotheses.

1. The PBBS facet construction is one literal physical word and proves the
   unconditional bounds

   \[
   \nu(k)\le2^{k-1}-1+{k+2\over k}W_k
   \quad(k\text{ odd}),                              \tag{0.1}
   \]

   \[
   \nu(k)\le2^{k-1}-1+{k+1\over k-1}W_k
   \quad(k\text{ even}).                             \tag{0.2}
   \]

2. Mandatory run-boundary cores make source nonemptiness automatic and
   exclude every singleton conflict in a strict resident Johnson atlas.
3. The interval-profile local lemma then gives the exact sufficient
   quadratic condition `D_j<=M^2/16` for `M>=4`.

None of these statements proves `B(k)+O(1)`.  The half-cube word avoids the
flat compiler by writing the deep lower ideal literally; the girth theorem
does not supply the required candidate multiplicity or codegree estimate.

## 1. Audit of the PBBS input scope

The q1-rainbow deck, all-depth upper support, and component bound belong to
the same complement-projected step-two PBBS factor.  In the notation of
`THREAD_A_COMPOSITE_ODD_PBBS_TWO_MATCHING_SHADOW_FACTOR_20260729.md`:

* Theorem 1.1(4) says every rank-`m` facet occurs exactly once.
* Theorem 2.2 supplies every upper target as a cyclic owner-window union.
* Corollary 2.3 gives at most `W/k=Cat_m` components.

The last count has the correct parity factor.  An `f`-orbit has length
`ell*k`; its `f^2` cycles have length

\[
                         {\ell k\over\gcd(2,\ell k)}. \tag{1.1}
\]

Since `k` is odd, this is `ell*k` for odd `ell` and `(ell/2)k>=k` for
even `ell`.  Hence every projected component has at least `k` owner edges
and their number is at most `W/k`.

No connectivity, Hamiltonization, voltage, residence, or compiler theorem
is imported.

## 2. Audit of the facet word

At owner `T_i`, the two incident edge colours

\[
 F_{i-1}=T_{i-1}\cap T_i,
 \qquad F_i=T_i\cap T_{i+1}                           \tag{2.1}
\]

are distinct rank-`m` facets because the global q1 deck is squarefree.
Thus

\[
                         F_{i-1}\cup F_i=T_i.         \tag{2.2}
\]

Taking unions proves that an owner interval `T_a,...,T_b` has the same
union as the facet interval `F_(a-1),...,F_b`.  If the owner interval is
the full component, the written cyclic range repeats one endpoint facet;
deleting that repetition leaves the full facet cycle and does not change
the union.  Thus every middle and upper PBBS witness is a cyclic interval
of the one facet word.

Opening a facet cycle loses precisely its closure-crossing facet intervals.
The compressed collar applies with initial letter rank `m`, not owner rank
`m+1`.  Its two strict boundary chains each have at most `k-m` increments,
so its exact safe length bound is

\[
                         2(k-m)+1=k+2.                \tag{2.3}
\]

The collar includes the cut owner itself through the central letter
`F_(L-1) union F_0`.  Hence no middle target is silently lost at the cut.
Appending collars after all opened paths and then appending the deeper
lower masks cannot destroy a retained witness.

## 3. Audit of the length arithmetic

The facet paths contain `W=binom(2m+1,m)` letters, one for every rank-`m`
target.  Appending ranks `1,...,m-1` gives

\[
 W+\sum_{s=1}^{m-1}{2m+1\choose s}=2^{2m}-1.         \tag{3.1}
\]

The collar total is at most `(k+2)W/k`, proving (0.1).  This coefficient is
integral because `W/k=Cat_m`.

More generally, appending any word for the complete lower ideal gives
`W+mu(k,m-1)+c(k+2)`.  This modular interface is literal and valid.  The
separate rank-separation theorem shows only that it cannot be a
deadline-scale construction while all `W` facet cells remain literal; it
does not invalidate the interface as an upper bound.

For the even lift, the word

\[
                         A,\{z\},z+A                 \tag{3.2}
\]

covers respectively the old nonempty targets, `{z}`, and every
`{z} union S` with nonempty old `S`.  It has length `2|A|+1`.  For even
`k`,

\[
 {k\choose k/2}=2{k-1\choose k/2-1},                 \tag{3.3}
\]

and substituting the odd bound gives (0.2) exactly.

## 4. Audit of the run-boundary core

For one positive coordinate run `[a,b]` in the owner path, maximal erosion
has source support

\[
 [a',b'],\qquad
 a'=0\text{ if }a=0\text{ and }a+d\text{ otherwise},
\]

\[
 b'=W+d-1\text{ if }b=W-1\text{ and }b\text{ otherwise}.\tag{4.1}
\]

Every finite support endpoint is the only allowed occurrence in one
extreme central window and is therefore mandatory in every antecedent.
This proves `F_p subseteq A_p`.  Strict Johnson transitions and depth-`d`
positive-run residence make consecutive erosion states distinct; the rank
ramps handle the source ends.  Hence every position has nonempty `F_p`.

If every retained candidate `(S,I)` obeys `F(I) subseteq S`, then all pins
using position `p` contain `F_p`.  Their joint intersection therefore
cannot empty that source letter.  This excludes source-nonemptiness
conflicts of every size.

For a central requirement `(i,x)`, its allowed set is the intersection of
`[i,i+d]` with one eroded `x`-run.  If that set is truncated, it contains a
finite eroded-run endpoint, which no negative candidate can contain while
omitting `x`.  If it is not truncated, it has all `d+1` positions and one
candidate interval of length at most `d` cannot cover it.  Thus a singleton
cannot kill a central coordinate.  It also cannot kill its own positive
target coordinate.  Conflict girth is therefore at least two.

The conclusion is sharp in scope: two different candidates may cover the
two remaining portions of a central support, exactly as in the audited
two-pin example.

The pair normal form is also exact.  With two selected candidates, the
only possible bad rows are a central coordinate row or a positive row
anchored at one of those two candidates; source nonemptiness has already
been excluded.  This gives precisely (3.4)--(3.6) in the theorem note.
The mandatory endpoint argument additionally forces every central pair
cover to act on an untruncated `d+1` window.  Hence the residual arity-two
gate is a literal interval-cover graph, not an abstract relaxation.

## 5. Audit of the quadratic profile implication

The interval-profile theorem is a partite asymmetric-local-lemma argument.
With conflict girth `g`, minimum part size `M>=4`, and common incident-edge
bound `D`, its elementary criterion is

\[
                         D\le{1\over4}(M/2)^g.        \tag{5.1}
\]

Substituting `g=2` gives `D<=M^2/16`.  Here `D` must bound every `D_j`,
not merely pair conflicts.  Under this hypothesis the sampled selector has
positive probability of containing no conflict edge, and the exact
negative-window theorem converts it into one deterministic common
antecedent.  Upper completeness is still a separate required hypothesis.

The local lemma is only sufficient.  The authenticated `k=11,13,15`
compilers may pass without these particular sublists satisfying (5.1), and
the length-`B(16)+1` word supplies no named flat atlas to which it could be
applied.

## 6. Final boundary

The unconditional half-cube bound discharges owner topology and upper
shadows at a cost `O(W_k)` beyond the literal strict lower half.  Reaching
the deadline scale still requires replacing those exponentially many
literal deep masks by a flat compiler.

For that coefficient-one route, unary conflicts are now ruled out.  The
first unresolved obstruction level is therefore arity two.  A concrete
sufficient condition is genuine quadratic expansion: large candidate parts
together with sufficiently small pair and higher conflict incidence.  This
profile inequality is not necessary.  A negative result against this route
must exhibit empty parts or repeated pair/higher conflict banks; residence
alone no longer supplies a unary obstruction.
