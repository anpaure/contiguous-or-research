# The exact q1 compiler capacity at `k=16` and the PBBS-shore pivot

## 0. Verdict

The canonical `429`-wreath MSW shore cannot occur in an optimal
`15 -> 16` lift, even if rotations, orientations, ports, the old shore, and
the **unrestricted** depth-three compiler are chosen optimally.  Its rank-six
q1 palette has `837` holes, whereas any exact depth-three antecedent can
repair at most two missing internal q1 colours.

The correct replacement seed is the centered PBBS factor on rank-seven
subsets of `[15]`.  It has all `5005` rank-six q1 colours and all `6435`
rank-eight union colours.  Its remaining defect is chronology rather than
coverage: it has `945` positive coordinate runs of length less than four.
Exactly `75` of those runs are protected by two unique q1 colours.  Thus the
finite lift problem has collapsed to a small protected-rethreading problem,
not a rotation/port problem on the MSW wreaths.

## 1. A dimension-free q1 boundary-capacity theorem

Let

\[
 T=(T_0,\ldots,T_{W-1}),\qquad |T_i|=r,
\]

be a Johnson path, and suppose that a nonempty source word

\[
 A=(A_0,\ldots,A_{W+d-1})
\]

satisfies

\[
 T_i=A_i\cup\cdots\cup A_{i+d}\qquad(0\le i<W).
\tag{1.1}
\]

Write

\[
 {cal C}_1(T)=\{T_i\cap T_{i+1}:0\le i<W-1\}.
\]

### Theorem 1.1 (two-boundary capacity)

At most two rank-`(r-1)` sets outside `C_1(T)` can occur as interval unions
of `A`.  In particular, universality of `A` implies

\[
 \binom{k}{r-1}-|{cal C}_1(T)|\le2.
\tag{1.2}
\]

### Proof

Let a rank-`(r-1)` target `S` be witnessed by the source interval
`I=[a,b]`.  Its length is at most `d`: any source interval of length at
least `d+1` contains one of the windows (1.1), whose union already has rank
`r`.

Suppose first that `I` uses neither extreme source position, so

\[
 1\le a\le b\le W+d-2.
\]

There is an integer

\[
 \max(0,b-d)\le i\le\min(W-2,a-1).
\]

Indeed, `b-d<=a-1`, `b-d<=W-2`, and `a-1>=0`.  For this `i`,

\[
 I\subseteq[i+1,i+d]
       =[i,i+d]\cap[i+1,i+d+1].
\]

Consequently

\[
 S=\bigcup_{p\in I}A_p
   \subseteq T_i\cap T_{i+1}.
\]

Both sets have rank `r-1`, hence equality holds and `S` belongs to
`C_1(T)`.

Every palette-absent target must therefore use source position `0` or
source position `W+d-1`.  All intervals using the left extreme are prefix
intervals and their unions are nested; at most one of them can have a given
rank `r-1` without being equal.  The same holds for suffix intervals at the
right extreme.  Hence there is capacity for at most one new rank-`(r-1)`
target at each end.  This proves (1.2).  `square`

This theorem uses neither the maximal erosion word nor the optional
one-core condition `DA=DP`.  It is a necessary condition for the full
integral compiler `COMP_d(T)`.

## 2. Application to the canonical MSW shore

Let `z` be the sixteenth coordinate.  The MSW candidate partitions all
rank-seven subsets of `[15]` into `429` cyclic wreaths of length `15`.
Inside a wreath, consecutive lifted states have the form

\[
 (\{z\}\cup R_t)\cap(\{z\}\cup R_{t+1})
   =\{z\}\cup Q_t,
 \qquad |Q_t|=6.
\]

The independently reproduced rank-six load census is

\[
\begin{array}{c|ccccc}
\text{load}&0&1&2&3&4\\ \hline
\#\text{ colours}&837&2117&1845&196&10.
\end{array}
\tag{2.1}
\]

Both checks close exactly:

\[
 837+2117+1845+196+10=5005=\binom{15}{6},
\]

\[
 2117+2(1845)+3(196)+4(10)=6435=429\cdot15.
\]

Thus the cyclic support is only

\[
 5005-837=4168.
\]

Opening, rotating, or reversing the fixed wreaths cannot add a q1 colour.
Moreover, a cross edge from a lifted `z`-state to an old rank-eight state
has an intersection omitting `z`; it cannot supply a target `z+Q`.
Therefore any chronology using only internal MSW-wreath edges for its
`z`-shore misses at least `837` child q1 colours.

For the child problem,

\[
 \binom{16}{7}=\binom{15}{7}+\binom{15}{6}=6435+5005=11440.
\]

Even granting perfect coverage of all `6435` q1 colours omitting `z`, its
full q1 support is at most

\[
 6435+4168=10603,
\]

well below the necessary `11438`.  Theorem 1.1 therefore proves

\[
 \boxed{\text{canonical MSW shore + arbitrary ports + full `COMP_3` is impossible}.}
\]

The literal same-edge insertion enumerator fails even earlier: only
`361/429` wreaths can be matched, across `800` candidate port edges, and one
wreath has no candidate edge at all.  That is a separate, narrower
obstruction; (2.1) rules out every port assignment in the entire fixed-MSW
class.

There is also a quantitative lower bound on any attempted MSW rethread.
If `j` selected B--B edges are allowed outside the fixed MSW edge catalogue,
then their total rank-six support is at most `4168+j`.  Reaching the compiler
threshold `5003` therefore forces

\[
 j\ge5003-4168=835.
\tag{2.2}
\]

In particular this is not a bounded local repair of the `429` wreaths.  If
one insists on opening every wreath into a separate path and then makes
`j` genuinely new B--B joins, edge accounting requires at least `429+j`,
hence at least `1264`, deleted MSW edges.  Any surviving MSW-based model is
a global rethread in substance.

## 3. Exact PBBS replacement seed

Let `f` be the canonical PBBS permutation of the rank-seven subsets of
`[15]`.  For each center `X`, form the centered Johnson edge

\[
 e_X=\{f^{-1}(X),f(X)\}.
\]

The PBBS first-shadow theorem says these edges form a spanning 2-factor of
`J(15,7)`, every rank-six intersection colour occurs between one and three
times, and every rank-eight union colour occurs exactly once.

The executable independent audit

```text
python3 scratch/audit_k16_pbbs_shore_20260729.py
```

returns

\[
\begin{array}{c|l}
\text{quantity}&\text{exact value}\\ \hline
\text{vertices}&6435\\
\text{physical components}&73\\
\text{component lengths}&15^5,45^9,75^{21},105^{26},135^{11},165^1\\
\text{rank-six support}&5005/5005\\
\text{rank-six load histogram}&1^{3630}2^{1320}3^{55}\\
\text{rank-eight union support}&6435/6435.
\end{array}
\tag{3.1}
\]

So PBBS closes exactly the compiler-facing obstruction that kills MSW.

## 4. The remaining finite protected-rethreading core

For depth `d=3`, every internal positive coordinate run in the rank-seven
shore must have length at least four.  The PBBS run census is

\[
 \#\{\text{runs of length }2\}=90,
 \qquad
 \#\{\text{runs of length }3\}=855.
\tag{4.1}
\]

Hence the raw PBBS shore has `945` residence violations.

To open a short cyclic run, a cut must hit one of its internal edges.  A
cut preserves the q1 palette without replacement when its colour has
another retained occurrence.  Exact enumeration gives:

* all `90` length-two runs have a repeat-coloured internal edge;
* `780` of the `855` length-three runs have a repeat-coloured internal edge;
* the remaining `75` length-three runs have **both** internal q1 colours of
  load one.

Those `75` protected motifs split into exactly five free `Z_15`-orbits.
Their ten internal q1-colour orbits are the finite core that a legal trade
must rethread.  This also explains the persistent floor `residence3=75` in
the saved q1-preserving PBBS trade certificates: ordinary safe cuts remove
everything except the protected motifs.

Thus the valid search order is now forced:

1. choose/rethread a rank-seven factor with q1 support at least `5003`,
   preferably the full PBBS support `5005`;
2. eliminate or open the five protected motif orbits while retaining that
   support;
3. choose cuts and old/new-sector rungs with a direct feasible compiler
   selector for the source singleton `{z}` (a four-state `z`-run is one
   strong candidate channel, but is neither necessary nor sufficient);
4. audit arbitrary-width upper completeness;
5. invoke unrestricted `COMP_3`, and finally exhaustively verify all
   `2^16-1` targets.

The open object is therefore a protected alternating trade (or a
dual-resident factor) on a quotient-sized state space.  It is no longer an
MSW rotation problem.
