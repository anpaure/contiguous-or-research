# Independent audit: joint-start orbit lift and named collar chainization

**Date:** 2026-08-04  
**Method:** independent line-by-line proof, census, and scope replay; pure
mathematics; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_JOINT_START_SURPLUS_ORBIT_LIFT_AND_NAMED_COLLAR_CHAINIZATION_20260804.md`  
**Verdict:** **GO after one necessary scope correction.**  The owner rank
is now explicitly assumed to satisfy

\[
                         1\le r\le\left\lceil{k\over2}\right\rceil.
\]

This puts the collar in the nondecreasing half of the Boolean lattice.
Without that hypothesis some displayed surplus capacities could be
negative, so the unqualified arbitrary-rank statement was false.  No
other mathematical correction was needed.

## 1. Collar census and necessity

Write `C_t=binom(k,t)` and `t_0=r-D`.  Under the corrected rank hypothesis,

\[
                         C_{t-1}\le C_t
                         \qquad(t_0<t\le r).
\]

At rank `t_0` there is no continuation demand, giving `C_(t_0)` possible
starts.  At every later rank `t`, all `C_(t-1)` existing collar-chain tops
must be continued into distinct rank-`t` sets.  The exact new-start bank is
therefore

\[
 h_{t_0}=C_{t_0},\qquad h_t=C_t-C_{t-1}\quad(t>t_0).
\]

These capacities telescope to `C_r`.  At the owner layer the last surplus
is exactly the owners not consumed by rank-`r-1` continuations.  Projecting
any named matching to type/start-rank counts consequently gives the row
equalities and column inequalities (0.6)--(0.7).

Because nonempty residual flags have declared load at least one, they do
not actually use the bottom bank `R_(t_0)` on the stated reservation face.
Keeping that harmless zero-supported column makes the telescoping census
uniform; it does not create fictitious usable capacity.

## 2. Fractional orbit lift

For one type `a`, one fixed rank-`t` target contains `binom(t,s_a)`
possible structural tops.  With `m_a` labelled copies, the incoming
residual load at that target is

\[
 m_a\binom{t}{s_a}
 {x_{a,t}\over m_aC_{s_a}}
 {1\over\binom{k-s_a}{t-s_a}}
 ={x_{a,t}\over C_t}.
\]

The multiplicity cancels correctly.  A fixed rank-`t` target contains `t`
rank-`t-1` predecessors, each spreading unit mass over `k-t+1`
successors.  Its continuation load is

\[
 {t\over k-t+1}={C_{t-1}\over C_t}.
\]

Thus every right load is at most one exactly by (0.7), while every left
load is one exactly by (0.6).  This is a fractional matching saturating
the complete left shore.  Ordinary bipartite matching integrality rounds
it to a literal named matching; no divisibility or equivariant integral
matching is being assumed.

## 3. Literal chain induction and owner layer

At each collar rank, right-vertex capacity makes the following mutually
exclusive:

1. continuation of one previous collar chain;
2. a residual-attached new start; or
3. a collar-only new start.

Induction gives one chain ending at every set in each collar layer.  At
rank `r`, the same matching sends all rank-`r-1` continuations and all
direct residual starts to distinct owners; unused owners are empty slots.
Every collar target below rank `r` occurs once, all residual marked banks
remain disjoint by hypothesis, and all joins are literal containments.

A type-`a` flag started at rank `t` has charged load at most

\[
                         \ell_a+(r-t)\le D,
\]

while a collar-only chain has load `r-t<=D`.  A finite strict flag inside
one owner can be realized by an owner ordering: list each successive set
difference as a block, followed by unused owner coordinates.  This proves
the named owner/order conclusion, but not any word-level interval-address
claim.

## 4. Complete-layer SCD batches

For a block `[b,s]` below `t_0`, every member of every rank in the block
lies on an SCD chain which reaches rank `s`.  Indeed the corrected central
rank hypothesis gives `s<=floor(k/2)`, and a symmetric chain containing a
rank at most `s` extends at least to rank `s`.  Distinct rank-`s` tops lie
on distinct SCD chains, so the resulting marked banks are disjoint.  A
width-`w` block may safely declare reservation `w`, even when boundary
chains make some literal flags shorter.

This validates the claimed complete-layer source.  Multiple labelled
copies with one structural top are allowed only under the theorem's
explicit assumption that their **marked** target banks are disjoint; the
structural top need not itself be a repeated marked target.

## 5. Threshold cuts and exact deficiency

A declared load `ell` can start precisely in the suffix

\[
                         t_0+\ell,\ldots,r.
\]

These neighbourhoods are nested.  Hence Hall reduces exactly to

\[
 \sum_{a:\ell_a\ge q}m_aC_{s_a}
 \le\sum_{t=t_0+q}^{r}h_t
 =C_r-C_{t_0+q-1}
 \qquad(1\le q\le D).
\]

For a nested-suffix capacitated graph, maximum cardinality deficiency is
the largest suffix overload, proving (4.4).  Requiring all continuation
vertices to be saturated is an integral face of the bipartite matching
polytope.  Giving every complete type a constant marked-target weight
therefore also proves the weighted identity (4.6): an `O(1)` weighted type
defect introduces no further named-set loss during this lift.

## 6. Exact boundary of the result

The theorem is exact only on the collar-saturated, declared-reservation,
complete-layer-batch face.  It does not prove:

- feasibility of the threshold table for coefficient-one residual chunks;
- a physical endpoint address or aperture;
- a countdown/source-word serialization;
- residence or arbitrary-width upper coverage; or
- compatibility with the protected halo and terminal compiler.

Within that face, however, the conclusion is exact: once the finite
type/load table is feasible, there is no additional named Boolean
containment Hall obstruction.

