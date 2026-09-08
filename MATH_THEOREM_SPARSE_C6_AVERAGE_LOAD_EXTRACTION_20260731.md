# Sparse C6 average-load extraction: Catalan and central-scale reservoirs

Date: 2026-07-31  
Status: unconditional extraction theorem for the **raw local**
middle-level incidence-C6 catalogue.  It supplies a compatible family on
the Catalan asymptotic scale, and a tuned higher density gives a
raw central-binomial-order reservoir.  It does not attach protected all-width witnesses,
complete common-cap tickets, or prescribed repair tasks, and therefore does
not by itself prove `nu(k) <= B(k)+O(1)`.

## 0. Outcome

The complete incidence-C6 atlas has `m^2` choices at every oriented
middle-level incidence, but its maximum conflict load is cubic.  Thus it
cannot be fed directly to Haxell's independent-transversal theorem.

Nevertheless, the complete atlas contains two useful sparse families.

The larger-family extraction has

\[
             |S|\ge {3I\over4m^2}
\]

and average external conflict at most `72m+216`; it gives a raw independent
transversal for `m>=579`.  A sharper endpoint-disjoint extraction has

\[
             |S|\ge {1\over32m}{2m+1\choose m},
 \qquad       A_e(S)\le16m,
\]

and gives a raw independent transversal already for `m>=128`.  Both have
Catalan order.  The first has the better leading family constant; the
second has an explicit physical-anchor matching and substantially better
load and threshold.

There is also a tunable-density form.  If `R` is the full row energy,
Bernoulli density `p` extracts at least `3pI/4` lists with average conflict
at most `4pR`, and Haxell works once `L>=32pR`.  For the raw row
`R<44m^3`, taking `p=1/(1408m)` produces a compatible endpoint-disjoint
reservoir of size at least

\[
                         {3\over5632}{2m+1\choose m},
\]

which is central-binomial rather than merely Catalan scale.  This stronger
existence statement is still an unprescribed raw reservoir.

The fixed density `m^{-2}` is the density which the Catalan recursion
naturally asks for.  The
number of all oriented incidences is

\[
                   I={2m+1\choose m}(m+1),
\]

so density `m^{-2}` in the incidence atlas has order central-binomial
coefficient divided by `m`, i.e. Catalan order.

The proof uses average conflict rather than maximum token load.  This is
important: at this density a few individual tokens can still have large
load, but high-degree packet choices are deleted separately inside each
list before Haxell is applied.

## 1. Raw catalogue and conflict graph

Let `E` be the set of all oriented incidences

\[
              e=(C,U),\qquad |C|=m,\quad U=C+a.
\]

For each `e`, let `P_e` be its `L=m^2` labelled incidence hexagons, indexed
by

\[
                  b\in C,\qquad c\notin U.
\]

Two candidates in different lists conflict when their raw local supports
share a rank-`m` vertex, a rank-`(m+1)` vertex, or a middle-level incidence.
Within-list conflicts are irrelevant because a transversal chooses only one
candidate from a list.

The exact complete-atlas loads are

\[
 \lambda_{m}=\lambda_{m+1}=3(m+1)m^2,
 \qquad \lambda_{\rm inc}=6m^2.                     \tag{1.1}
\]

Every candidate uses three vertices on each shore and six incidence tokens.
Consequently the number of candidates in the complete atlas which conflict
with one fixed candidate is, by the union bound, at most

\[
 R_*:=6\cdot3(m+1)m^2+6\cdot6m^2
      =(18m+54)m^2.                                  \tag{1.2}
\]

Double counting therefore gives, for every anchor `e`,

\[
 \sum_{f\ne e}\frac1L
   \#\{(p,q)\in P_e\times P_f:p\sim q\}
 \le R_*.                                            \tag{1.3}
\]

Repeated conflict witnesses only make (1.2)--(1.3) smaller; no disjointness
of token neighbourhoods is assumed.

The same role table gives an exact row energy.  For anchors `e,f`, put

\[
 K(e,f)={1\over L}\sum_r a_e(r)a_f(r),                         \tag{1.4}
\]

where `a_e(r)` is the number of candidates in list `e` containing typed
token `r`.  A conflicting candidate pair may share several tokens, so
`K(e,f)` upper-bounds, rather than equals, its average packet-conflict
contribution.

### Lemma 1.1 (exact raw row energy)

For every anchor `e`,

\[
 \sum_{f\ne e}K(e,f)
   =18m^3+51m^2-4m-5=:R_m<44m^3\qquad(m\ge2).        \tag{1.5}
\]

#### Proof

On either vertex shore the global typed-token load is `3(m+1)m^2`.
One local list has `3m^2` occurrences and squared local multiplicity

\[
                         m^4+m^3+m^2:                         \tag{1.6}
\]

one fixed token has multiplicity `m^2`, `m` one-free tokens have
multiplicity `m`, and `m^2` zero-free tokens have multiplicity one.  The
two shores therefore contribute

\[
 2\,{3m^2\,3(m+1)m^2-(m^4+m^3+m^2)\over m^2}
 =18m^3+16m^2-2m-2.                                      \tag{1.7}
\]

An incidence token has global load `6m^2`.  The local list has `6m^2`
incidence occurrences and squared multiplicity

\[
                         m^4+2m^3+3m^2.                         \tag{1.8}
\]

Thus incidences contribute

\[
 {6m^2\,6m^2-(m^4+2m^3+3m^2)\over m^2}
 =35m^2-2m-3.                                           \tag{1.9}
\]

Adding (1.7) and (1.9) proves the equality.  The last inequality follows
by direct subtraction for `m>=2`. \(\square\)

## 2. Sparse extraction

For `S subset E` and `e in S`, define the average external packet degree of
the list `P_e` inside `S` by

\[
 A_e(S)=\frac1L\sum_{p\in P_e}
     \#\{q\in\bigcup_{f\in S\setminus\{e\}}P_f:p\sim q\}.
                                                               \tag{2.1}
\]

### Theorem 2.1 (Catalan-scale average-load extraction)

For every `m>=2`, there is a set `S' subset E` with

\[
              |S'|\ge \frac{3I}{4m^2}                         \tag{2.2}
\]

such that every `e in S'` satisfies

\[
                       A_e(S')\le72m+216.                       \tag{2.3}
\]

#### Proof

Choose each anchor independently with probability

\[
                              p=m^{-2},
\]

and call the resulting set `S`.  Conditional on `e in S`, equations
(1.3) and linearity give

\[
              \mathbb E[A_e(S)\mid e\in S]
                 \le pR_*=18m+54.                              \tag{2.4}
\]

Call `e` bad when `e in S` and

\[
                        A_e(S)>4(18m+54).
\]

Markov's inequality makes the conditional bad probability at most `1/4`.
Hence

\[
 \mathbb E\bigl[|S|-\#\{\hbox{bad anchors}\}\bigr]
       \ge pI-\frac14pI=\frac{3I}{4m^2}.             \tag{2.5}
\]

Some outcome attains at least its expectation.  Delete every bad anchor in
that outcome and call the survivor set `S'`.  Deleting lists cannot increase
any external degree, so every survivor obeys (2.3), and (2.5) proves
(2.2).  \(\square\)

This alteration is deliberately one-sided.  It does not claim that a
uniform sparse set has bounded maximum token load, which would be false at
the same strength without further balancing.

There is a second alteration which explicitly removes shared physical
anchor endpoints.  Two oriented incidence anchors are endpoint-adjacent
when they share their rank-`m` or rank-`(m+1)` endpoint.  Every anchor has
exactly `2m` such neighbours, so there are `Im` unordered adjacent pairs.

### Theorem 2.2 (endpoint-disjoint exact-energy extraction)

For every `m>=2`, there is an endpoint-disjoint anchor family `A` with

\[
               |A|\ge {1\over32m}{2m+1\choose m}                 \tag{2.6}
\]

and

\[
               \sum_{f\in A\setminus\{e\}}K(e,f)\le16m
               \qquad(e\in A).                                  \tag{2.7}
\]

#### Proof

Choose anchors independently with probability

\[
                              p={1\over16m^2}.                    \tag{2.8}
\]

Let `X` be the number of selected endpoint-adjacent pairs and

\[
                         Z=\sum_{\{e,f\}\subseteq S}K(e,f).
\]

Then

\[
 \mathbb E|S|=pI,\qquad
 \mathbb EX=p^2Im,\qquad
 \mathbb EZ\le {p^2IR_m\over2}.                                \tag{2.9}
\]

Delete at most one anchor for every endpoint-adjacent pair.  Then delete
every remaining anchor of weighted degree greater than `16m`.  Weighted
degree sums to at most `2Z`, so the second deletion removes at most
`2Z/(16m)` anchors.  The expected survivor count is at least

\[
 pI-p^2Im-{p^2IR_m\over16m}
 >pI\left(1-{1\over32}-{11\over64}\right)>{pI\over2},             \tag{2.10}
\]

where `1/(16m)<=1/32` and `R_m<44m^3` were used.  Some outcome therefore
has at least `pI/2` survivors.  Finally

\[
 {pI\over2}={W(m+1)\over32m^2}\ge {W\over32m}.
\]

The deletion rules give endpoint-disjointness and (2.7). \(\square\)

### Theorem 2.3 (tunable row-energy extraction)

Let

\[
                 R=\max_e\sum_{f\ne e}K(e,f).                    \tag{2.11}
\]

For every `0<p<=1`, there is an anchor family `S_p` with

\[
                         |S_p|\ge {3pI\over4}                     \tag{2.12}
\]

and

\[
                 \sum_{f\in S_p\setminus\{e\}}K(e,f)\le4pR
                 \qquad(e\in S_p).                               \tag{2.13}
\]

#### Proof

Sample every anchor with probability `p`.  Conditional on selecting `e`,
the expected weighted external degree is at most `pR`.  Mark `e` bad when
its degree exceeds `4pR`; Markov makes its conditional bad probability at
most `1/4`.  Hence the expected number of selected nonbad anchors is at
least `3pI/4`.  Delete the bad anchors.  Deletion cannot increase a
survivor's degree, proving (2.12)--(2.13). \(\square\)

If two raw anchors share a physical endpoint, every candidate in one list
conflicts with every candidate in the other, so their mutual contribution
to (2.13) is `L=m^2`.  Therefore any choice with `4pR<L` makes the extracted
family automatically endpoint-disjoint.  For complete guarded packets this
conclusion is valid only when the shared anchor endpoint remains a mandatory
token in every candidate.

## 3. One compatible C6 at every retained anchor

### Theorem 3.1 (raw compatible reservoir)

For every `m>=579`, the set `S'` in Theorem 2.1 has a choice

\[
                         p_e\in P_e\qquad(e\in S')
\]

such that the chosen raw C6 supports are pairwise token-disjoint.

#### Proof

The packet-conflict graph is partitioned into the lists `P_e`, each of size
`L=m^2`.  By (2.3), every part has average external degree at most

\[
                         \overline\Delta=72m+216.
\]

Delete from each list the candidates of external degree greater than
`2 overlineDelta`.  Markov retains at least half of every list.  The induced
conflict graph has maximum degree at most `2 overlineDelta`, while every
part has size at least `L/2`.  Haxell applies provided

\[
 \frac{m^2}{2}\ge2(2\overline\Delta),
 \quad\hbox{equivalently}\quad
 m^2\ge8(72m+216).                                    \tag{3.1}
\]

The latter holds for `m>=579`.  Its independent transversal is the desired
choice.  \(\square\)

The numerical threshold is immaterial asymptotically; it is recorded only
to keep every constant explicit.  Finitely many lower dimensions can be
handled separately in an eventual additive-constant induction.

### Theorem 3.2 (endpoint-disjoint raw reservoir)

For every `m>=128`, the family in Theorem 2.2 admits one raw C6 per anchor
such that all selected raw supports are pairwise token-disjoint.

#### Proof

Equation (2.7) bounds the average external packet degree of each list by
`16m`.  Delete candidates of external degree greater than `32m`; Markov
retains at least `m^2/2` candidates in every list and the induced maximum
degree is at most `32m`.  Haxell applies when

\[
                         {m^2\over2}\ge2(32m),                    \tag{3.2}
\]

equivalently `m>=128`. \(\square\)

### Theorem 3.3 (tunable Haxell criterion)

Suppose every retained part has size at least `L_min`.  The family in
Theorem 2.3 has an independent transversal whenever

\[
                              L_{min}\ge32pR.                      \tag{3.3}
\]

Indeed, prune candidates of external degree greater than `8pR`.  Equation
(2.13) and Markov retain at least half of every part, while the induced
maximum degree is at most `8pR`.  Haxell asks for
`L_min/2>=2(8pR)`, which is (3.3).

For the raw catalogue take `L_min=m^2`, `R=R_m<44m^3`, and

\[
                              p={1\over1408m}.                     \tag{3.4}
\]

Then `32pR<m^2`, `4pR<m^2`, and Theorems 2.3 and 3.3 give an
endpoint-disjoint compatible raw reservoir of size

\[
 {3pI\over4}
   ={3W(m+1)\over5632m}
   \ge {3W\over5632}.                                             \tag{3.5}
\]

This deliberately uses a small universal constant.  Asymptotically any
`p=c/m` with `c<1/576` passes the sharp leading Haxell inequality coming
from `R_m~18m^3`.

## 4. Abstract buffered extension

The same alteration has a useful abstract form.  Suppose every anchor list
has at least `alpha m^2` complete packets and, in the full anchor atlas, the
directed average external row energy

\[
 K_{full}(e,f)={1\over|P_e|}
   \#\{(x,y)\in P_e\times P_f:x\sim y\}
\]

has row sum at most

\[
                              K D_m m^3,                         \tag{4.1}
\]

where `D_m` measures the effective protected dependency span and the row
energy includes all typed conflicts.  The fixed density `p=m^{-2}` gives
`Omega(W/m)` retained lists of average degree `O(D_m m)` and works directly
only when `D_m=o(m)` (or when the exact constants pass Haxell).

The tunable form is stronger.  If (4.1) holds with constant `K`, choose

\[
              p=\min\left\{1,{\alpha\over64K D_m m}\right\}.       \tag{4.2}
\]

In the nontrivial second branch, `32pR<=alpha m^2/2`, so the same
rowwise Markov/Haxell proof as Theorem 3.3 applies with room, and

\[
                |S_p|\ge {3\alpha I\over256K D_m m}
                         =\Omega\!\left({W\over D_m}\right).       \tag{4.3}
\]

If the minimum in (4.2) selects `p=1`, the direct bound is instead
`|S_p|>=3I/4`, which is only stronger than the intended asymptotic use.

Thus even `D_m=Theta(m)` would yield a Catalan-scale compatible reservoir,
provided the complete-packet row energy (4.1), quadratic guarded list
supply, and compositional conflict model were actually proved.  No
protected-upper compression is needed for this **dispersed-reservoir
existence** implication; compression may still be needed by the separate
bounded-collar or prescribed-task routes.

If all candidates retain their source-anchor endpoints, two anchors sharing
one endpoint contribute at least `alpha m^2` to each other's normalized row.
Under (4.2), the retained threshold is at most `4pR<=alpha m^2/16`, so such
pairs are automatically deleted.  If buffering can replace or omit the
anchor endpoint, this source-collision conclusion must instead be included
in the full ticket conflict relation.

Equation (4.1) must include complete common-cap paths, sinks, protected
replacement witnesses, and topology tickets.  The raw local loads (1.1)
do not imply it for those global resources.  Nor does (4.3) assign a
prescribed leave task to one of the retained anchors.

## 5. What this changes, and what it does not

The full-atlas cubic-load obstruction and the present theorem are
compatible:

* density one gives external degree `Theta(m^3)` against lists of size
  `m^2`;
* density `m^{-2}` gives average external degree `Theta(m)`, leaving a
  factor `Theta(m)` before buffering;
* density `Theta(1/m)` with a sufficiently small constant still passes the
  raw Haxell inequality and gives `Theta(W)` compatible actuators; and
* for a buffered row `R=O(D_m m^3)`, adaptive density
  `Theta(1/(D_m m))` gives `Theta(W/D_m)` compatible packets.

So the raw C6 geometry contains enough mutually compatible local actuators
at exactly the scale required by the asymptotic physical-forest leave.
This removes the claim that the cubic full-atlas load alone rules out a
Catalan-sized reset reservoir.  The endpoint-disjoint version additionally
shows that source-anchor collisions can be removed at constant-factor cost;
it does not prescribe which anchors survive.

It does **not** yet prove that:

1. the retained anchors correspond to a prescribed defect family;
2. each raw C6 lifts to a resident, arbitrary-width-upper-transparent
   packet;
3. the complete cap tickets satisfy the buffered row (4.1);
4. the reservoir absorbs every leave rather than merely existing; or
5. the regenerated sidecar stays in a bounded invariant family.

In particular, neither extraction may be applied to a prescribed task bank
without a separate task-to-anchor matching/distribution theorem.  Nor may
raw token-disjointness be read as compatibility of protected upper rays,
complete common-cap paths, sinks, or graphic/topology tickets.

Those are now the exact remaining correlations for the dispersed-reservoir
route to `B(k)+O(1)`.
