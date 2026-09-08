# Independent cross-check of handoff item 1969

Date: 2026-07-30  
Scope: the PBBS half-cube upper bound, the mandatory run-boundary core,
and the part-profile compiler criterion.  This audit used only proof
inspection and small local replays; no SAT or remote computation.

## Verdict

I found no mathematical gap in the claims made in handoff item 1969.
The six recorded SHA-256 values match the files byte for byte.  In
particular, the following implications are valid with exactly their stated
scope.

1. For odd `k>=3`,
   \[
   \nu(k)\le 2^{k-1}-1+\frac{k+2}{k}
       {k\choose (k-1)/2}.
   \]
2. For even `k>=4`,
   \[
   \nu(k)\le 2^{k-1}-1+\frac{k+1}{k-1}{k\choose k/2}.
   \]
3. On a strict depth-`d`-resident Johnson chronology, pruning a lower
   candidate `(S,I)` by `F(I) subseteq S subseteq P(I)` eliminates every
   unary compiler conflict.
4. The remaining pair conflicts are exactly the three interval-cover
   types in Theorem 3.2 of the run-boundary report.
5. If every retained target part has at least `M>=4` candidates and **all**
   arity profiles obey `D_j<=M^2/16` for `j>=2`, then the part-profile
   local lemma gives a full compiler.  Upper completeness of the chronology
   then gives `nu(k)=B(k)`.

The last item is conditional.  Neither PBBS nor a Pascal chronology is
proved to have the required `M` and `D_j` profile.  In particular, a bound
on `D_2` alone is not enough.

## 1. Odd PBBS word

Write `k=2m+1`, `r=m+1`, and
`W=binom(2m+1,m)`.  The imported facts all refer to the same
complement-projected step-two PBBS factor:

* its `W` rank-`m` edge facets are globally rainbow;
* every upper target is a cyclic interval union in one factor component;
* each component has at least `k` owners, so the component count is at
  most `W/k`.

For a component `(...,T_(i-1),T_i,T_(i+1),...)`, put
`F_i=T_i cap T_(i+1)`.  The two incident facets at `T_i` are distinct
rank-`m` subsets of one rank-`m+1` set, hence

\[
                         T_i=F_{i-1}\cup F_i.
\]

Thus every cyclic owner interval is a cyclic facet interval.  Opening one
facet cycle loses only its closure-crossing intervals.  If the distinct
suffix and prefix union chains have `a` and `b` strict increments, the
collar

\[
 (\Delta L_a,\ldots,\Delta L_1,L^0\cup R^0,
   \Delta R_1,\ldots,\Delta R_b)
\]

realizes every pair `L^p union R^q`.  Since a facet has rank `m`,
`a,b<=k-m=m+1`; hence the collar length is at most

\[
                         2(k-m)+1=k+2.
\]

There are `W` literal facets and at most `W/k` collars.  Appending every
mask of ranks `1,...,m-1` gives

\[
 W+\sum_{s=1}^{m-1}{k\choose s}=2^{k-1}-1,
\]

which proves the odd formula.  No residence or compiler is used here.

As a boundary sanity check, at `k=3` one may take the facet cycle
`(1,2,4)`.  The opened word plus the explicit collar is

```text
1 2 4 | 1 2 5 2 4
```

and its contiguous ORs contain all seven nonzero masks.  Its length is
exactly the displayed upper bound `8`.

## 2. Even doubling

For any universal old word `A`, the literal word

\[
                         A,\{z\},z+A
\]

covers old nonempty targets, `{z}`, and `{z} union S` for every nonempty
old target `S`.  It has length `2|A|+1`.  With

\[
 {k\choose k/2}=2{k-1\choose k/2-1},
\]

substitution of the odd formula gives the even formula exactly.  This
step has no mixed-seam hypothesis.

The formulas exceed the authenticated optima for every `3<=k<=15`, as an
upper bound should.  The first values `(upper bound, optimum)` are
`(8,4)` at `k=3`, `(17,7)` at `k=4`, `(29,12)` at `k=5`, and
`(59,21)` at `k=6`.

The label “all-k” requires only the trivial separate cases `k=1,2`; the
displayed theorem itself correctly starts at odd `k=3` and even `k=4`.

## 3. Mandatory cores and unary conflicts

For a positive coordinate run `[a,b]` in `T`, maximal erosion has source
support

\[
 [a',b'],\qquad
 a'=0\text{ if }a=0\text{ and }a+d\text{ otherwise},\quad
 b'=W+d-1\text{ if }b=W-1\text{ and }b\text{ otherwise}.
\]

Every finite endpoint is the unique permitted occurrence in an extreme
central window, so it is mandatory in every antecedent.  These endpoints
are exactly

\[
 F_p=(P_p\setminus P_{p-1})\cup(P_p\setminus P_{p+1}).
\]

Strict Johnson adjacency plus residence makes consecutive interior
erosion states distinct Johnson neighbors; the two rank ramps handle the
source ends.  Therefore every `F_p` is nonempty.

If `(S,I)` is retained only when `F(I) subseteq S subseteq P(I)`, then all
selected candidates using position `p` contain `F_p`.  Their joint
negative deletion cannot empty the source letter.  A single negative
interval also cannot erase a central coordinate: a truncated allowed
support contains a mandatory finite endpoint, while an untruncated support
has `d+1` positions and a candidate interval has length at most `d`.
Finally, one candidate cannot erase one of its own positive target
coordinates.  These are all unary failure types.

I replayed this directly on the authenticated flat certificates.  For
`k=6,7,9,10,11,12,13,14,15`, maximal erosion satisfies `D^dP=T`, every
`P_p` and `F_p` is nonempty, and `F_p subseteq A_p` at every source
position.  The `k=4,5` retained words are not flat middle permutations,
and the `k=8` carrier is not a strict Johnson path; they are correctly
outside this theorem's hypotheses.

At `k=6`, exhaustive light enumeration gives 35 pruned candidates and no
unary failure.  Among 577 candidate pairs from distinct target parts,
exactly 24 are incompatible, and all 24 (with no false positives) satisfy
one of the three pair-cover conditions in Theorem 3.2.

## 4. Part-profile constants

For a size-`h` conflict edge, uniform independent selection gives event
probability at most `M^{-h}`.  Assigning the local-lemma parameter
`a^h`, and charging at most `hD_j` neighboring size-`j` edges, gives the
exact criterion

\[
 M^{-1}\le a\prod_j(1-a^j)^{D_j}.
\]

Taking `a=2/M` shows it is enough that

\[
 \sum_{j\ge g}D_j(2/M)^j\le\frac12.
\]

If all conflicts have size at least `g` and every `D_j<=D`, geometric
summation gives

\[
 D\le\frac12\left(1-\frac2M\right)(M/2)^g.
\]

For `g=2` and `M>=4`, the stated simpler constant is
`D<=M^2/16`; the sharper common bound is `M(M-2)/8`.  The directions of
all inequalities are correct.

## 5. Exact scope

The package proves a genuine unconditional

\[
                     \nu(k)\le(1/2+O(k^{-1/2}))2^k
\]

construction.  It does not prove the conjectural central-binomial-scale
upper bound.  The sharp remaining compiler statement is not merely
“pairwise compatibility”: it requires nonempty candidate parts and
sufficiently small incident conflict counts at every arity.  The literal
facet barrier is consistent with this conclusion: a deadline-scale proof
must compile almost all PBBS facets as overlapping derivative windows,
rather than retain them as literal source cells.

