# The full-endpoint reset is impossible, but a rank-two block queue attains the deadline current exactly

**Date:** 2026-08-07  
**Method:** adjacent-suffix submodularity, phase blocks, and a cyclic
omission rotor  
**Status:** unconditional local theorem and exact reduction.  A fixed-additive
word cannot contain a positive density of full deep endpoints.  The smallest
uniform rolling replacement is a rank-two suffix chain: it preserves a flat
rank-(m) (D^d) owner row, has simple immediate palettes and exact
residence, regenerates after (3(d+1)) positions, and has enough symmetric
fractional target capacity to pay the theta reset deficit.  The integral
target-disjoint block factor and its fusion into the merged PBBS chronology
remain open.

## 1. Parameters and the deadline current

Use the odd merged-PBBS parameters

\[
 n=2m+1,\qquad p=d+1,\qquad s=m-2d,\qquad t=m-d.
\tag{1.1}
\]

For a source word (A), put

\[
 Z_{i,j}=A_{i-j+1}\cup\cdots\cup A_i.
\tag{1.2}
\]

At two adjacent endpoints write

\[
 X=Z_{i,d},\qquad Y=Z_{i+1,d},\qquad H=Z_{i,d-1}.
\tag{1.3}
\]

Suppose the containing (d+1)-letter window is a rank-(m) owner.  Define

\[
 \alpha=|X|-(t-1),\qquad
 \beta=|Y|-(t-1),\qquad
 \gamma=(t-2)-|H|.
\tag{1.4}
\]

The adjacent-endpoint current theorem gives

\[
                         \alpha+\beta+\gamma\ge d.
\tag{1.5}
\]

Equality has a useful exact form.

### Lemma 1.1 (equality normal form)

If equality holds in (1.5), then

\[
 X\cap Y=H,\qquad |X\cup Y|=m.
\tag{1.6}
\]

Writing (L=X\setminus H) and (R=Y\setminus H), one has

\[
 L\cap R=\varnothing,\qquad
 |L|=1+\alpha+\gamma,\qquad
 |R|=1+\beta+\gamma.
\tag{1.7}
\]

In particular, if both top cells retain rank (t-1), then

\[
 |H|=s-2,\qquad |L|=|R|=d+1.
\tag{1.8}
\]

#### Proof

The proof of the current inequality uses

\[
 m=|X\cup Y|\le |X|+|Y|-|H|.
\]

At equality the right side is (m), so equality holds throughout and
(X\cap Y=H).  Equations (1.7)--(1.8) follow by subtraction. \(\square\)

Thus a dense replacement cannot be a bounded perturbation of two full
pieces.  It must move a rank bank of size (d).

## 2. A weighted phase queue

The local construction is clearer in a slightly more general form.  Fix an
integer block weight (h\ge1) and assume

\[
                         ph\le m.
\tag{2.1}
\]

Choose pairwise disjoint sets

\[
 K,S_0,S_1,\ldots,S_{p-1}
\tag{2.2}
\]

with

\[
 |K|=m-ph,\qquad |S_a|=h+1.
\tag{2.3}
\]

Give every (S_a) a cyclic order

\[
 x_{a,0},x_{a,1},\ldots,x_{a,h}.
\]

For (i=qp+a), where (0\le a<p) and (q) is read modulo (h+1), put

\[
                         A_i=K\cup(S_a\setminus\{x_{a,q}\}).
\tag{2.4}
\]

This is a cyclic source word of period

\[
                         L_h=p(h+1).
\tag{2.5}
\]

Its ground-set use is exactly

\[
 |K|+\sum_a|S_a|=m-ph+p(h+1)=m+p\le 2m+1=n,
\tag{2.6}
\]

independent of (h).  Thus the construction is feasible whenever
(2.1) holds.

### Theorem 2.1 (weighted rolling block queue)

The word (2.4) has the following properties.

1. Every (p=d+1) consecutive letters have union rank (m).  Hence
   (D^dA) is a flat rank-(m) owner row.
2. The (L_h) owners are distinct and form a simple Johnson cycle.
3. The immediate lower and upper owner palettes are both simple.
4. Every coordinate of a phase support has an owner gap of exactly (p)
   and an owner run of exactly (hp); the core coordinates are permanent.
5. Every suffix of (j\le p) consecutive source letters has rank

   \[
                           r_j=m-ph+jh=m-(p-j)h.
   \tag{2.7}
   \]

6. For every fixed (1\le j<p), the (L_h) suffix-union targets of
   depth (j) are distinct.  Targets at different depths have different
   ranks.
7. After (L_h) positions every omission and every age state returns to
   its initial value.  The construction is a literal zero-length-charge
   rolling reset: it occupies owner positions but appends no reset position.

#### Proof

Every (p)-letter window contains exactly one letter from every phase.
The phase supports are disjoint, each displayed block has size (h), and
all letters contain (K).  Its union therefore has rank

\[
                         |K|+ph=m.
\]

Moving the window one step updates exactly one phase.  In that phase the
old block (S_a-x_{a,q-1}) is replaced by (S_a-x_{a,q}).  The two blocks
differ by one deletion and one insertion.  Hence consecutive owners are
Johnson adjacent.

During one period each phase is updated (h+1) times.  Before the full
period, at least one phase has advanced a nonzero number smaller than
(h+1), so its omitted coordinate has not returned.  Thus the owner states
have exact period (p(h+1)), proving simplicity.

At an owner edge, one phase support is complete in the union palette and
has two omitted coordinates in the intersection palette.  This uniquely
identifies the updated phase.  The omissions in the other phases determine
the rotor time, so no two lower or upper colours coincide.

A coordinate (x\in S_a) is absent precisely while phase (a) omits it.
One omission state persists for the (p) owner steps between successive
updates of phase (a).  The other (h) omission states persist for (hp)
steps altogether.  This proves the exact gap and run lengths.

If (j\le p), a (j)-letter suffix meets (j) different phase supports.
Equation (2.7) follows.  For (j<p), its set of active phase supports is a
proper cyclic interval and therefore recovers the endpoint phase.  The
visible omissions then recover the rotor time.  This proves target
distinctness.  Finally all phase rotors return after (2.5), proving literal
regeneration. \(\square\)

## 3. Why rank two is the minimal uniform replacement

The phase weights need not be equal.  If phase (a) uses a block of size
(h_a), take (|S_a|=h_a+1) and

\[
                         |K|=m-\sum_a h_a.
\tag{3.1}
\]

The proof of Theorem 2.1 is unchanged: every owner contains one block from
every phase, and updating a phase swaps one coordinate.  A suffix rank is
(|K|) plus the sum of the weights of its active phases.

### Lemma 3.1 (full endpoint is one exceptional heavy phase)

In a positive-weight phase queue, an endpoint has the full base-(s),
depth-(d) profile exactly when its (d) active phase weights are all one and
the unique excluded phase has weight (p=d+1).

#### Proof

Successive suffix-rank increments of a full endpoint are one, so every
active phase weight is one.  Its singleton rank is (s), hence
(|K|=s-1).  The owner has rank (m), so the excluded weight is

\[
 m-(s-1)-d=m-s-d+1=d+1=p.
\]

The converse follows by substituting these weights into the suffix sums.
\(\square\)

Thus a fixed phase-weight vector has at most one full endpoint phase.  A
dense queue must distribute the exceptional weight among the phases rather
than retain a full profile.

At adjacent endpoints of the weighted queue, (2.7) gives

\[
 |X|=|Y|=m-h,qquad |H|=m-2h.
\tag{3.2}
\]

Relative to the full two-rail profile,

\[
 \alpha=\beta=p-h,qquad \gamma=2h-p-1.
\tag{3.3}
\]

Therefore

\[
                         \alpha+\beta+\gamma=p-1=d.
\tag{3.4}
\]

Every weighted queue attains the deadline-current inequality with equality.
The current is paid by distributing the former exceptional guard bank over
all (p) phases.

The full endpoint profile corresponds instead to phase weights

\[
                         (p,1,1,\ldots,1):
\tag{3.5}
\]

the excluded heavy phase supplies the top depth-(d) cell and every included
phase supplies one saturated step.  It can be full at only one phase out of
(p).  This is the queue form of the fixed-additive density obstruction.

Among uniform integer phase weights, (h=1) is the ordinary rolling owner
queue.  Its marked suffix ranks are

\[
                         t,t+1,\ldots,m-1,
\tag{3.6}
\]

so it does not enter the top deep slab (s,\ldots,t-1).  The smallest
uniform weight which does is therefore

\[
                         \boxed{h=2}.
\]

For (h=2), the period is (3p), and the (d) proper suffix ranks are

\[
                         \boxed{s,s+2,s+4,\ldots,m-2.}
\tag{3.7}

Thus every endpoint carries (d) named-address slots, the same scalar load
as a full SCD piece, but it is a rank-two chain cutting transversely across
the old depth-(d) slabs.  It has no full endpoint and hence is not covered
by the full-endpoint density no-go.

## 4. Exact price in the merged PBBS ledger

Let

\[
 \theta=2\sigma-1=4\sum_{a\ge1}e^{-4\pi a^2}.
\tag{4.1}
\]

The merged full-piece theorem leaves a reset deficit

\[
                         (\theta+o(1))W
\tag{4.2}
\]

endpoint positions.  Replacing (H) full-piece-plus-private-reset pairs by
(H) rank-two queue endpoint chains has the following exact local ledger:

\[
\begin{array}{c|c|c}
 &\text{private full-piece realization}&\text{rank-two queue realization}\\ \hline
\text{named lower cells}&Hd&Hd\\
\text{payload endpoints}&H&H\\
\text{private reset endpoints}&H&0\\
\text{extra appended positions}&0&0.
\end{array}
\tag{4.3}
\]

Hence (H=(\theta+o(1))W) such queue endpoints would close the theta
endpoint deficit with zero local length charge.  This is a rechainization,
not a literal replacement of the same SCD targets: the old saturated pieces
and the new rank-two chains use different rank profiles.

The rings have (3p) endpoints.  A final partially used ring causes no
additive-position remainder: its unused endpoints may carry other eligible
rank-two chains.  What is not free is global component fusion; a bank of
(H) endpoints has (\Theta(H/d)) protected rings before splicing.

## 5. Symmetric fractional block factor

Let

\[
                         \mathcal R_2=\{s,s+2,\ldots,m-2\}.
\tag{5.1}
\]

Form a hypergraph whose vertices are all named targets in the layers
(\binom{[n]}r), (r\in\mathcal R_2), and whose edge is the complete
marked target set of one rank-two ring.  Every edge contains exactly (3p)
targets in every one of the (d) layers.

Average uniformly over every labelled choice of (K), the disjoint triples
(S_a), their cyclic omission orders, and all coordinate permutations.
If the total fractional ring mass is (T), symmetry gives load

\[
                         {3pT\over {n\choose r}}
\tag{5.2}

at every rank-(r) target.  The layers in (5.1) increase toward the middle,
so the smallest is rank (s).  Therefore

\[
                         \boxed{T\le {1\over3p}{n\choose s}}
\tag{5.3}
\]

is a fractional matching.  It covers (3pT\le{n\choose s}) queue
endpoints.

At the optimal deadline,

\[
                         {{n\choose s}\over W}\longrightarrow e^{-\pi}.
\tag{5.4}
\]

Consequently the endpoint capacity ratio is

\[
                         {e^{-\pi}\over\theta}>3000.
\tag{5.5}
\]

Thus the rank-two replacement has more than three orders of magnitude of
fractional target capacity beyond the reset deficit.  Unlike the old full
pair, it also passes the literal flat-owner, Johnson, residence, and
regeneration rows.

## 6. The exact integral gate

The remaining assertion is not another scalar inequality.

> **Rank-two rolling block-factor theorem.**  Select target-disjoint
> rank-two rings containing ((\theta+o(1))W) endpoints; partition the
> residual lower ideal into the remaining merged endpoint chains; and fuse
> the ring owners into the prescribed PBBS owner chronology while retaining
> the coordinate-cover and common-compiler rows.

The symmetric point (5.3) proves fractional target feasibility.  It does
not round the growing (3pd=\Theta(d^2)=\Theta(n))-uniform ring edges, prove
that the residual named targets retain an integral chain partition, or fuse
(\Theta(W/d)) ring components.  Those are correlated occurrence-level
conditions.

There is nevertheless an exact abstract chain check.  In any symmetric-chain
decomposition of (B_n), every rank-(s) set lies on a chain crossing all
ranks in (5.1).  Taking every second member from rank (s) through rank
(m-2) gives exactly

\[
                         {n\choose s}
\tag{6.1}
\]

pairwise target-disjoint rank-two chains.  Thus integral rank-two
chainization itself has ample capacity.  The surviving difficulty is to
choose the special cyclic block-union chains of Theorem 2.1 and the residual
PBBS chart in one common factor.

## 7. Verdict

The rolling rank-(t) full-endpoint queue cannot be repaired: the
fixed-additive density theorem rules out even an abstract positive-density
bank of its full endpoints.  The smallest uniform replacement is not a
guarded full pair but the (h=2) block queue.  It pays the forced rank
current exactly, preserves (D^d) rank (m), and has zero local position
charge.

This proves a viable local recurrence and a large fractional target margin.
It does not yet prove the rank-two rolling block-factor theorem or
\(\nu(k)\le B(k)+O(1)\).
