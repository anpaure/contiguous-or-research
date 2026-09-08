# One central resource rank is enough before graphic Hall completion

**Status (2026-08-21).**  The reduction below is proved.  It strictly
weakens the previously stated parity-matching gate: the paths need be
matched in only one middle rank.  Every other band rank, including ranks of
the same parity, may be postponed to the exact Hall/graphic completion.
This does not construct the required one-rank path matching or bound the
resulting graphic deficiencies.

## 1. General block system

Let

\[
 n=2m+1,\qquad W={n\choose m},
\]

let `K` be the retained rank band, and suppose there are `b` selected legal
blocks.  After discarding already charged checkpoint observations, every
block has `a` retained post-move observations at every rank.  Let `B_ch`
be the number of discarded rank-incidences; each is charged once when the
retained ledger is returned to the physical path.  Put

\[
 A=ba,
 \qquad M_k={n\choose k}.                              \tag{1.1}
\]

Every rank deck

\[
 U_{i,k}=\{C_k(\pi_{i,t}):1\le t\le a\}               \tag{1.2}
\]

is an `a`-set.  At the two middle ranks `m,m+1`, use real quota `a` and no
dummies.  At an outer rank assume `M_k<=A`, and choose integer quotas

\[
 r_{i,k}+h_{i,k}=a,
 \qquad
 \sum_i r_{i,k}=M_k,
 \qquad
 \sum_i h_{i,k}=A-M_k.                                \tag{1.3}
\]

Once the paths have been selected, let

\[
 \delta_k=\max_{I\subseteq[b]}
 \left(\sum_{i\in I}r_{i,k}
       -\left|\bigcup_{i\in I}U_{i,k}\right|\right)_+ \tag{1.4}
\]

be the exact capacitated Hall deficiency.

## 2. The single-resource reduction

### Theorem 2.1 (one central matching suffices)

Suppose one legal path has been selected in every block so that the
rank-`m` decks `U_(i,m)` are pairwise disjoint.  Then all other ranks can be
decorated so that their retained-ledger real-target collision plus leave is
at most

\[
 2(W-A)+2\sum_{k\in K\setminus\{m\}}\delta_k.          \tag{2.1}
\]

The full charged claimed-resource defect, after restoring the discarded
incidences, is at most the right-hand side of (2.1) plus `B_ch`.  This is a
ledger defect bound; it does not count unrelated raw physical-path events.

Consequently, if

\[
 W-A=o(W),
 \qquad B_{\rm ch}=o(W),
 \qquad \sum_{k\in K\setminus\{m\}}\delta_k=o(W),   \tag{2.2}
\]

the selected common paths give a full-band defect selection with `o(W)`
collision and leave.  No matching at the other ranks of the parity of `m`
is required.

#### Proof

At rank `m`, the `A` observations are distinct, so only the unavoidable
`W-A` middle-layer targets are left.  Fix `k\ne m`.  The defect form of
Hall's theorem gives `sum_i r_(i,k)-delta_k` distinct real claims.  Fill the
`delta_k` unmatched left clones with arbitrary further observations from
their own block decks.  This creates at most `delta_k` repeated claim
occurrences.

At an outer rank the real demand is `M_k`; hence at most `delta_k` real
targets are left and collision plus leave is at most `2delta_k`.  At the
other middle rank the demand is `A`, so its leave is at most
`W-A+delta_k`, and collision plus leave is at most
`W-A+2delta_k`.  Dummy labels at outer ranks are then partitioned according
to (1.3), exactly as in the fixed-endpoint palette construction.  Summing
over ranks proves (2.1).  Restoring one discarded physical observation can
add at most one repeated claim occurrence (or can fill a leave), so charging
each discarded rank-incidence once adds at most `B_ch`.  \(\square\)

The proof uses only the actual selected decks.  Parity reconstruction is
unnecessary once the full legal paths, including their checkpoint seed
states, are known.

## 3. Graphic completion at every postponed rank

Temporally order `U_(i,k)`, attach one private root to its first target, and
form the augmented `a`-edge deck path.  This private root is solely an
auxiliary vertex of the graphic matroid: it is not a palette target, consumes
no resource, and contributes neither collision nor leave.  Let `epsilon_k`
be its graphic Rado
quota deficiency, as in
`MATH_CANDIDATE_CYCLOMATIC_HALL_GRAPHIC_ROUNDING_20260821.md`.  The exact
comparison there gives

\[
 \epsilon_k\le\delta_k\le\epsilon_k+b.                \tag{3.1}
\]

### Corollary 3.1 (one-resource/common-graphic target)

If the rank-`m` decks form a matching and

\[
 W-A=o(W),\qquad B_{\rm ch}=o(W),
 \qquad
 \sum_{k\in K\setminus\{m\}}\epsilon_k=o(W),
 \qquad |K|b=o(W),                                    \tag{3.2}
\]

then (2.2) holds.  Thus the remaining integral theorem may be stated as:

> select one common legal path per block whose rank-`m` decks are disjoint
> and whose postponed-rank augmented deck paths have total graphic quota
> deficiency `o(W)`.

This is a strictly smaller initial resource hypergraph than the earlier
one-parity formulation.  Its postponed graphic constraints still use the
same paths, so it is not a relaxation of the final DCC requirement.

#### Proof

Sum the upper inequality in (3.1) over the `|K|-1` postponed ranks and use
(3.2), then apply Theorem 2.1.  \(\square\)

## 4. Linear-checkpoint accounting

The common-transformation bundle permits the reduction at the scale where
same-rank codegrees are potentially useful.  Take microblock physical
length

\[
 \ell=\lceil Cn\rceil\qquad(C>1),                     \tag{4.1}
\]

and discard the final checkpoint observation of every microblock at every
rank.  Thus `a=ell-1`, and the discarded checkpoint charge is exactly

\[
 B_{\rm ch}=|K|b.                                     \tag{4.2}
\]

Tile identity backbones up to physical length
`N_phys<=W`, with

\[
 W-N_{\rm phys}=e^{o(n)},
 \qquad b={N_{\rm phys}\over\ell}=(1+o(1)){W\over\ell}. \tag{4.3}
\]

The retained ledger volume is

\[
 A=b(\ell-1)=N_{\rm phys}-b,
 \qquad
 |K|(W-A)=o(W),
 \qquad |K|b=B_{\rm ch}=o(W).                         \tag{4.4}
\]

For all sufficiently large `n`, every outer band layer satisfies `M_k<A`.
Indeed the largest outer layer has

\[
 {M_{m-1}\over W}={M_{m+2}\over W}
 ={m\over m+2}=1-{2\over m+2},                        \tag{4.5}
\]

whereas `(W-A)/W=(1+o(1))/ell<2/(m+2)` because `C>1`.
Thus the quotas (1.3) exist, and all unavoidable checkpoint and tiling loss
in Theorem 2.1 is `o(W)`.

Under a uniform seed and a branch law independent of that seed, each
retained microblock has the exact occurrence marginal

\[
 \Pr(S\text{ occurs away from its checkpoint})
 ={\ell-1\over {n\choose k}}.                         \tag{4.6}
\]

This marginal statement does not survive arbitrary adaptive conditioning
and is not an integral selector.  The unresolved theorem is precisely the
one-resource/common-graphic selection in Corollary 3.1.
