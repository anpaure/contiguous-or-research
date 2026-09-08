# Rank-stratified stabilizer packing closes the isolated-`C8` upper-backup bank

**Date:** 2026-08-05  
**Method:** nested cyclic-interval counting and a rank-ordered probabilistic
greedy argument; no computation or search  
**Status:** unconditional simultaneous vertex-disjoint packing theorem for the
isolated collar.  Every casualty in the old two-cycle internal deck has an
alternative incidence-path witness, and all alternatives can be chosen
pairwise vertex-disjoint and disjoint from the active collar for all
sufficiently large central ranks.  This does not extend the resulting
`O(d^3)` protected path bank to one spanning two-factor, and it does not apply
to the unbounded exterior intervals created after grafting the collar into
PBBS bodies.

## 1. Setup

Let the two old owner cycles of the isolated screen-lattice collar each have
length

\[
                         L=8(d+1),                         \tag{1.1}
\]

and let every owner have rank `r`.  Let `cal D` be the set of upper targets
which occur as cyclic owner-interval unions in one of the two old cycles but
have no witness in the fused collar.  The local collar theorem gives

\[
 |Z|\ge r+2\quad(Z\in{\cal D}),
 \qquad d=\Theta(\sqrt r).                                \tag{1.2}
\]

For `s>=2`, put

\[
              {\cal D}_s=\{Z\in{\cal D}:|Z|=r+s\}.         \tag{1.3}
\]

For every `Z in cal D_s`, choose a shortest cyclic owner interval witnessing
`Z` in the old collar.  If it contains `ell_Z` owners, cut one incidence edge
when it is the whole cycle and regard it as an incidence path `W_Z`.  Then

\[
 p_r(W_Z)=\ell_Z\le L,
 \qquad p_{r-1}(W_Z)=\ell_Z-1\le L.                        \tag{1.4}
\]

The union of the owners of `W_Z` is exactly `Z`.

## 2. Exact rank and span census

### Lemma 2.1 (one value of a fixed rank per cyclic start)

Fix one starting owner on one of the old cycles.  As the cyclic interval is
extended one owner at a time, its union sets form a nested sequence.  Hence,
for every fixed `s`, all intervals starting there whose union has rank `r+s`
have the same union value.

Consequently

\[
                         |{\cal D}_s|\le2L                 \tag{2.1}
\]

and

\[
                  \sum_{Z\in{\cal D}_s}\ell_Z\le2L^2.     \tag{2.2}
\]

Moreover `cal D_s` is empty for `s>=L`.

#### Proof

For a fixed start, increasing the endpoint only adds owner coordinates.  Two
nested finite sets of equal cardinality are equal, proving the first claim.
There are `L` cyclic starts in each of two cycles, which gives (2.1), and
every chosen span is at most `L`, which gives (2.2).

Starting from one rank-`r` owner, each of the next `ell-1` Johnson steps adds
at most one previously unseen coordinate to the interval union.  Hence a
span of at most `L` owners has rank at most `r+L-1`.  This proves the final
claim.  \(\square\)

The literal residue structure of the screen lattice gives a sharper span
identity in the lower excess ranks.

### Lemma 2.2 (exact short-span law)

For every `2<=s<=d` and every `Z in cal D_s`, the chosen shortest witness
has

\[
                           \ell_Z=s+1.                       \tag{2.3}
\]

Consequently

\[
             \sum_{Z\in{\cal D}_s}\ell_Z\le2L(s+1)
             \qquad(2\le s\le d).                           \tag{2.4}
\]

#### Proof

Write the cyclic source letters as `A_t` and the owners as

\[
                         T_t=\bigcup_{i=0}^d A_{t+i}.
\]

The biresidence theorem says that every source occurrence of a fixed
coordinate lies in one residue class modulo `d+1`.  Since
`T_t,T_(t+1)` are loopless Johnson neighbours, let `y_t` be their unique
incoming coordinate.  It occurs in `A_(t+d+1)`.

For `0<=i<=d-1`, if `y_(t+i)` also lay in the first owner `T_t`, its unique
possible source position there, by the residue law, would be `A_(t+i)`.
It would then occur in both the outgoing letter `A_(t+i)` and the incoming
letter `A_(t+i+d+1)` at that transition, so it could not be an incoming
owner coordinate.  Hence every `y_(t+i)` is absent from `T_t`.

If `0<=i<j<=d-1` and `y_(t+i)=y_(t+j)`, the two displayed incoming source
occurrences differ by `j-i`, strictly between zero and `d+1`, contradicting
the residue-class property.  Thus over any `d` consecutive transitions the
incoming coordinates are distinct and absent from the first owner.  It
follows that every interval of `ell<=d+1` owners has union rank

\[
                              r+\ell-1.                     \tag{2.5}
\]

An interval of rank `r+s`, `s<d`, therefore cannot contain more than `d+1`
owners, since its first `d+1` owners already have rank `r+d`; (2.5) then
forces `ell=s+1`.  If `s=d`, the first `d+1` owners already have the same
rank as the whole interval, so their nested unions are equal and a shortest
witness again has length `d+1=s+1`.  Equation (2.4) follows from (2.1).
\(\square\)

There are only four changed owner edges in the rethread, so actual
casualties satisfy a still sharper low-rank count.

### Lemma 2.3 (four-cut rank--span casualty count)

Let

\[
 {\cal D}_{s,\ell}=\{Z\in{\cal D}_s:\ell_Z=\ell\}.
\]

For every `s` and `2<=ell<=L`,

\[
               |{\cal D}_{s,\ell}|
                    \le \min\{2L,4(\ell-1)\}.              \tag{2.6}
\]

For `2<=s<=d`,

\[
                         |{\cal D}_s|\le4s,                 \tag{2.7}
\]

and hence

\[
                 \sum_{Z\in{\cal D}_s}\ell_Z
                    \le4s(s+1).                            \tag{2.8}
\]

#### Proof

An old owner interval not crossing one of the four changed hinge edges lies
inside one unchanged continuation segment and survives literally after the
rethread.  Therefore every old witness of an actual casualty crosses at
least one changed edge.

A span-`ell<L` cyclic interval has `ell-1` internal edges.  For one fixed
changed edge there are exactly `ell-1` cyclic starts whose interval contains
that edge, and there are four changed edges.  Lemma 2.1 says that one start
gives at most one rank-`(r+s)` value.  This proves the `4(ell-1)` bound; the
independent `2L` bound is (2.1).  When `ell=L`, each old cycle has only one
full-cycle union, so the displayed bound is immediate.  For `s<=d`, Lemma 2.2 forces
`ell=s+1`, giving (2.7)--(2.8).  \(\square\)

The former bound `|cal D|<=2L^2` forgot the rank stratification.  Lemma 2.1
shows that the `Theta(r^2)` stabilizer denominator at the critical excess
rank two competes with only `O(L)` targets and `O(L^2)` total previous path
mass.

## 3. Simultaneous stabilizer packing

We use the one-target avoidance lemma from the relative-`C8` graft theorem.
For convenience, if `Z` has rank `z`, a witness path with `p_r` owners and
`p_(r-1)` facets has a stabilizer copy avoiding forbidden vertex banks
`Q_r,Q_(r-1)` whenever

\[
 {p_r|Q_r|\over {z\choose r}}+
 {p_{r-1}|Q_{r-1}|\over {z\choose r-1}}<1.                 \tag{3.1}
\]

### Theorem 3.1 (rank-stratified isolated-backup packing)

For all sufficiently large `r`, the paths `W_Z`, `Z in cal D`, have
stabilizer images `widetilde W_Z` such that

1. every `widetilde W_Z` still has owner union `Z`;
2. the paths `widetilde W_Z` are pairwise vertex-disjoint; and
3. every `widetilde W_Z` is vertex-disjoint from the complete active collar.

Thus every isolated-collar casualty has a simultaneous alternative witness.

#### Proof

Process the nonempty strata

\[
                    {\cal D}_2,{\cal D}_3,\ldots,
                    {\cal D}_{L-1}                          \tag{3.2}
\]

in increasing order of `s`; use any order within one stratum.  At each step,
let `Q_r,Q_(r-1)` consist of all owner and facet vertices of the active collar
and all previously selected backup paths.  The active two-cycle collar uses
at most `2L` vertices on each shore.

Consider first `s=2`.  Before any particular target in this stratum is
selected, Lemmas 2.1--2.3 give the sharper bounds

\[
 |Q_r|<2L+24,
 \qquad |Q_{r-1}|<2L+16.                                  \tag{3.3}
\]

Since `z=r+2`, `p_r=3`, and `p_(r-1)=2`, the left side of (3.1) is at most

\[
 {3(2L+24)\over {r+2\choose2}}+
 {2(2L+16)\over {r+2\choose3}}
 =O\!\left({L\over r^2}\right)
  +O\!\left({L\over r^3}\right)=o(1),                   \tag{3.4}
\]

because `L=O(sqrt r)`.

Now let `s>=3`.  There are fewer than `L` nonempty excess-rank strata.  By
(2.2), all already selected paths together use at most `2L^3` vertices on
either shore.  Hence

\[
 |Q_r|,|Q_{r-1}|\le2L+2L^3.                               \tag{3.5}
\]

The binomial denominators are increasing with `s`, so

\[
 {r+s\choose r}\ge {r+3\choose3},
 \qquad
 {r+s\choose r-1}\ge {r+3\choose4}.                       \tag{3.6}
\]

The left side of (3.1) is therefore at most

\[
 {L(2L+2L^3)\over {r+3\choose3}}+
 {L(2L+2L^3)\over {r+3\choose4}}
 =O\!\left({L^4\over r^3}\right)
  +O\!\left({L^4\over r^4}\right)=o(1).                  \tag{3.7}
\]

Again `L=O(sqrt r)`.  Thus (3.1) holds at every greedy step for all
sufficiently large `r`.  Apply a stabilizer permutation of the current
target `Z`, select the resulting path, and add its vertices to the forbidden
banks.  Induction proves all three conclusions.  \(\square\)

### Corollary 3.2 (general scale boundary)

Without using the special residue-class span law of Lemma 2.2, the same
nested-interval argument works for two rank-`r` cycles of length `L=L(r)`
whenever

\[
                         L^3=o(r^2),
 \qquad                  L^4=o(r^3).                        \tag{3.8}
\]

The first condition is the critical scale in this greedy argument exposed by
the excess-two stratum;
the second pays all higher strata under only the nested-interval census.
In the OR-word regime `L=Theta(sqrt r)`, both have polynomial room.

## 4. Exact scope

The theorem closes the **simultaneous occurrence selection** row which was
left open by the pointwise stabilizer argument.  The union of all selected
paths is a 2-bounded disjoint union of incidence paths, and its total length
is still only bounded by `O(L^3)=O(d^3)`.

Two further statements do not follow:

1. the available small protected-factor theorem extends only protected
   banks of at most `m-2` incidence edges, while `O(d^3)` may exceed that
   threshold; and
2. after the collar is opened and grafted into external PBBS bodies, crossing
   intervals have unbounded exterior span and no `2L`-per-rank census.

Thus isolated-collar upper **witness packing** is solved, but one common
q1-factor containing the full backup bank and arbitrary-exterior upper
protection remain separate gates.

## 5. Dependencies

The literal two-cycle collar and the old bound `|cal D|<=2L^2` are in

`MATH_THEOREM_BIRESIDENT_COMPOUND_C8_SCREEN_LATTICE_20260805.md`.

The pointwise stabilizer-avoidance lemma is in

`MATH_THEOREM_C8_RELATIVE_PBBS_ALTERNATING_GRAFT_AND_UPPER_BACKUP_20260805.md`.
