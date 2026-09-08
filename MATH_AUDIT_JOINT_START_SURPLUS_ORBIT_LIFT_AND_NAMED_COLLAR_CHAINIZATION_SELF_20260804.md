# Self-audit: joint-start surplus orbit lift and named collar chainization

**Date:** 2026-08-04  
**Method:** separate line-by-line self-replay; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_JOINT_START_SURPLUS_ORBIT_LIFT_AND_NAMED_COLLAR_CHAINIZATION_20260804.md`

## 0. Verdict

**PASS, with the scope stated in the theorem.**

The theorem proves an exact named-set lift from the finite surplus
transportation table to collar-saturated owner-rooted Boolean flags with
declared type reservations.  It
does not prove that
the table is feasible for the coefficient-one residual inventory, and it
does not serialize the flags into a source word.

The displayed owner-rank hypothesis places the whole collar band in the
nondecreasing half of the Boolean lattice.  This is necessary: the
continuation census below uses `C_t>=C_(t-1)` at every collar rank.

## 1. Census and necessity replay

At the bottom collar rank `t_0`, there are `C_(t_0)` rank-`t_0` vertices and
no continuation demand, so all `C_(t_0)` are possible starts.

At a later rank `t`, including the owner rank `t=r`, every one of the
`C_(t-1)` previous chain tops must
continue into a distinct member of `B_t`.  Exactly

\[
                              C_t-C_{t-1}
\]

rank-`t` vertices remain available as new starts.  Therefore (0.4) and the
column inequalities (0.7) are necessary.  Summing (0.4) telescopes to

\[
                 \sum_{t=t_0}^{r}h_t=C_r=W,
\]

the final number of owner slots.  In particular the last surplus
`C_r-C_(r-1)` is the empty-collar owner bank.  No start capacity is omitted
or counted twice.

## 2. Fractional-load replay

For residual type `a`, one fixed rank-`t` target `T` contains
`binom(t,s_a)` possible tops `S`.  There are `m_a` labelled copies.  Each
sends the fraction

\[
 {x_{a,t}\over m_aC_{s_a}}
 {1\over{k-s_a\choose t-s_a}}.
\]

The total is

\[
 m_a{t\choose s_a}
 {x_{a,t}\over m_aC_{s_a}}
 {1\over{k-s_a\choose t-s_a}}
 ={x_{a,t}\over C_t}.
\]

The cancellation of `m_a` is correct.  The continuation load is

\[
 {t\over k-t+1}={C_{t-1}\over C_t}.
\]

Thus the rank-`t` right load is exactly

\[
 {C_{t-1}+\sum_ax_{a,t}\over C_t}
\]

above the bottom, and `sum_a x_(a,t_0)/C_(t_0)` at the bottom.  Equations
(0.7) make both at most one.  Every left load is exactly one by (0.6).
Bipartite matching integrality therefore applies without a divisibility
assumption on the real `x_(a,t)`.

## 3. Named-chain induction replay

At each collar rank, and finally at the owner rank, right-vertex capacity
makes the following three cases exclusive:

1. continuation of one previous chain;
2. start of one residual-attached chain; or
3. start of one collar-only chain.

Every rank-`t` set belongs to exactly one case.  Induction therefore gives
one chain ending at each rank-`t` set.  At `t=r` the set is an unmarked
owner, not a lower target.  All collar targets occur once.  All
residual flags occur once because their left vertices are saturated, and
their marked banks were assumed disjoint.  Literal containment holds on
every join because it is the edge relation of the matching graph.

If a residual flag begins at rank `t`, its load is at most
`ell_a+(r-t)`, exactly the expression in (0.5).  A collar-only flag has load
`r-t`.  The `t=r` part of the joint matching sends rank-`r-1`
continuations and direct residual starts to distinct owners.  Hence the
owner and load claims are correct.

## 4. Threshold-cut replay

A type of load `ell` can use exactly the start ranks

\[
                       t_0+ell,\ldots,r.
\]

These neighbourhoods are nested suffixes.  For a threshold `q`, the types
with load at least `q` can only use the suffix beginning at `t_0+q` or
later.  The capacity of that suffix is

\[
 \sum_{t=t_0+q}^{r}(C_t-C_{t-1})
                   =C_r-C_{t_0+q-1}.
\]

Conversely, Hall for a bipartite graph with nested neighbourhoods is
equivalent to these suffix inequalities.  Thus (4.2) is exact.

At the largest threshold `q=D`, the suffix is the owner rank alone and has
capacity `C_r-C_(r-1)`.  This is exactly the bank needed by full-load
residual chunks.

For nested suffix neighbourhoods, the exact unit-task deficiency is the
largest suffix overload, which is (4.4).  Requiring every continuation edge
to be saturated defines a face of the ordinary bipartite matching polytope,
so integrality survives.  When each complete type has constant marked weight,
the same integral polytope with objective `w_a` proves (4.6).  Hence the
weighted-defect statement does not confuse omitted chunks with omitted
targets.

## 5. Scope audit

The following are hypotheses, not conclusions:

* complete-layer indexing of every residual type;
* pairwise disjoint marked target banks;
* a type/load histogram satisfying (4.2);
* later physical serialization and aperture compatibility.

The theorem does not claim that every possible owner-flag realization must
be collar-saturated.  Allowing an internal collar chain to terminate and a
new one to start can change the start census; necessity is asserted only on
the face defined before the main theorem.  Nor does it exploit a particular
flag being shorter than its type reservation; such a family must be refined
or accepts the conservative reserved load.

The theorem also does not claim that minimum-piece SCD chunks satisfy (4.2).
It explicitly retains correlated residual rechaining as the scalar/type
gate.  It also does not identify abstract owner flags with endpoint chains
of one word.  These exclusions prevent the named-chain theorem from being
overread as `nu(k)<=B(k)+O(1)`.

## 6. Final audit conclusion

All equalities, capacities, and quantifiers in the stated face replay
correctly.  The proof advances the exact named-set layer: once a compatible
complete-layer chunk histogram is found, there is no further literal
containment Hall problem in choosing the collar starts or rank-`r` owners.
