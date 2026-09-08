# The distinct-target gain budget of intact-fragment recomposition

Date: 2026-09-07. Coordinator deduction from the collar-protected
recomposition theorem of chat04. Pure proof, no computation.

## 1. Precise model

A Johnson geodesic trace on the middle layer of [2b] has ell vertices
T_0,...,T_(ell-1). Its designated square-pair targets at rank b-q are

    T_i intersect T_(i+q),   (T_i union T_(i+q))^c,
    0<=i<ell-q,

and the rank b+q bank is the complement family. At rank b the bank is
the trace and its complements. These are designated targets, not all
accidental interval unions of any compiled word.

Take t old traces. Cut c old edges into f=t+c intact, occurrence-disjoint
fragments. Reassemble every fragment exactly once into t' genuinely
geodesic traces, permitting reversal or complementation of a whole
fragment but no shared-endpoint identification. Thus the number of newly
added joining edges is

    j = f-t' = t+c-t'.                                  (1)

Write U_old(s), U_new(s) for the distinct designated rank-s banks.

## 2. Exact new-support bound

For every integer q>=1,

    |U_new(b-q) \ U_old(b-q)| <= 2qj,
    |U_new(b+q) \ U_old(b+q)| <= 2qj.                    (2)

The middle banks are identical.

Proof. A q-apart endpoint pair lying in one intact fragment already
occurred in the old trace. Reversal preserves its meet/union, and
complementation swaps the two designated lower-rank formulas above.
Thus such a pair supplies no new designated target.

Every new target therefore comes from an endpoint pair q edges apart
crossing at least one newly added joining edge. For a fixed join after
position a, the possible first endpoints i satisfy

    i<=a<i+q,

so there are at most q such pairs, even if the pair crosses other joins
too. Each pair contributes at most two targets at either specified rank.
Summing this union bound proves (2). The folded middle multiset was
preserved, so the middle support is unchanged. QED.

This conclusion does not require the old bank to be a middle packing,
nor any ambient multiplicity bound. Reusing a label as a separate
occurrence cannot defeat the union bound.

## 3. Consequence for individually insured cheap rewiring

Let W=binom(2b,b). Suppose the parameter H satisfies H/sqrt(b)->infinity,
and a sequence of such recompositions satisfies

    H(t+c)=o(W).                                        (3)

Since j<=t+c, j=o(W/H). For every fixed T>0, summing (2) over the two
ranks b±q with 1<=q<=floor(T sqrt(b)) bounds all new designated targets
in this central region by

    4j sum_(q=1)^floor(T sqrt(b)) q = O(T^2 b j).

The elementary central-binomial estimate W*sqrt(b)=Theta(4^b) and (3)
give

    b*j/4^b = O(j*sqrt(b)/W)=o(sqrt(b)/H)=o(1).          (4)

Outside this region, the number of targets is bounded by the binomial
tail, at most 2*4^b*exp(-T^2+o(1)). First take b to infinity for each
fixed T, then T to infinity. Thus

    |(union_s U_new(s)) \ (union_s U_old(s))|=o(4^b).     (5)

Likewise each fixed Gaussian-offset rank gains only o(W) targets.

A retained collar is a subtrace of an old trace and adds no new designated
targets beyond the old bank. Therefore adding the old collars for
preservation does not change (5).

## 4. What this rules out, and the constructive escape

The collar theorem gives a literal word of length M+2Ht'+6Hc preserving
all old designated band targets and all new square band targets. If its
new insurance cost is o(W) and the old fragmentation also satisfies
Ht=o(W), then (3) holds. Such a one-round operation cannot turn a
constant-density designated bank into a density-one bank. The same
bound applies to many rounds by summing their newly added joins, if the
total retained insurance budget remains negligible.

This does not invalidate the genuine local non-containment gains proved
by chat04 and its audit. It quantifies their limited total size under
the stated budget. Nor does it rule out:

- globally reselecting the initial bank;
- many rewires with shared/absorbed protection, rather than paying H
  separately for every cut;
- accepting controlled losses and proving a positive net-coverage drift;
- new accidental interval witnesses not represented by the square bank;
- an already density-one starting family needing only o(4^b) gains.

For a route to the full conjecture, actual distinct-target gain, not
merely preservation of the previous certificate, remains the main issue.

## 5. Audited canonical-compiler refinement

Chat06 subsequently bounded incidental targets for the specific standard
derivative-block compiler. For n blocks of sides H<ell<=b, H>=2, and
|q|<=Q<=H, its actual rank-(b+q) support outside the designated bank has
size at most (13H+3Q+1)n. The proof counts at most2|q| internal zero/two-cap
extras per block, at mostH+q+1 targets at a long-block seam by nested suffix
unions, and at most twice the total length of short blocks by endpoints.
Root read and checked all three cases. The full proof is in
/Users/amir.nuriyev/.codex/worktrees/c3da/problem/research_round1/collar_recomposition_density_capacity.md, Section4.

Thus Hn=o(W) and H/sqrt(b)->infinity also make incidental cube coverage
o(4^b) for this compiler. Under the negligible paid-collar budget, canonical
recompilation cannot bypass the designated-density obstruction using its
accidental intervals. Arbitrary different serializers remain outside this
additional statement. The join-count proof above itself was independently
audited by chats03,04,06 and the root proof-audit agent.
