# Joint-start surplus orbit lift and exact named collar chainization

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact named-target theorem for complete-layer
residual flag batches.  It chooses the collar chain decomposition and the
residual attachments simultaneously.  On this face, a finite rank/type
transportation table is necessary and sufficient; there is no additional
named-set Hall obstruction.  The theorem does not construct the required
type table, a countdown word, a resident owner chronology, or a complete
lower deck.

## 0. Outcome

Let

\[
                     {\cal B}_s={ [k]\choose s},
                     \qquad C_s=|{\cal B}_s|,
\]

fix an owner rank `r` in the nondecreasing half of the Boolean lattice,

\[
                         1\le r\le\left\lceil{k\over2}\right\rceil,
\]

a depth `D<r`, and put

\[
                            t_0=r-D.                 \tag{0.1}
\]

For each residual type `a`, suppose that there are `m_a` occurrence-labelled
families

\[
       \{F_{a,u,S}:S\in{\cal B}_{s_a}\},
       \qquad 1\le u\le m_a,                         \tag{0.2}
\]

of literal inclusion flags.  The top structural set of `F_(a,u,S)` is
`S`.  Type `a` reserves `ell_a` marked positions (the actual flag may be
shorter), and all marked targets in all the flags (0.2) are pairwise
distinct.  Assume

\[
                            s_a<t_0.                  \tag{0.3}
\]

Thus every residual batch is indexed by a **complete named Boolean layer**;
the flag below its top may depend on `u,S`.  Discard empty marked flags, so
that throughout

\[
                              1\le\ell_a\le D.        \tag{0.3a}
\]

For `t_0<=t<=r`, define the number of available new starts by

\[
 h_t=
 \begin{cases}
     C_{t_0},&t=t_0,\\
     C_t-C_{t-1},&t_0<t\le r.
 \end{cases}                                         \tag{0.4}
\]

At `t=r`, the right vertices are the rank-`r` owners.  Starting a residual
flag there means using an owner with no marked collar target; the available
bank has size `C_r-C_(r-1)`.

Call `(a,t)` load-compatible when

\[
                         ell_a+(r-t)\le D.            \tag{0.5}
\]

Call a realization **collar-saturated joint-start with the declared
reservations** when every type-`a` flag is charged its declared `ell_a`
positions, and, for every
`t_0<t<=r`, every chain whose current top is a rank-`t-1` collar set is
continued to a distinct containing rank-`t` set; all other rank-`t` sets
are new starts, possibly with one residual flag attached below them.  Thus
collar chains never terminate before the owner layer.  The main theorem is
the following exact equivalence on this explicitly defined face.

> There is a collar-saturated joint-start family with the declared
> reservations, consisting of named, target-disjoint owner flags of charged
> load at most `D`, which contains every residual flag
> (0.2) and every collar target of ranks `t_0,...,r-1` if and only if there
> are numbers `x_(a,t)>=0`, supported on load-compatible pairs, such that
>
> \[
>       \sum_{t=t_0}^{r}x_{a,t}=m_aC_{s_a}
>                         \qquad(a\text{ every type}),             \tag{0.6}
> \]
>
> and
>
> \[
>       \sum_a x_{a,t}\le h_t
>                         \qquad(t_0\le t\le r).                    \tag{0.7}
> \]

The numbers in (0.6)--(0.7) may be real.  No divisibility of `x_(a,t)` is
required.  A feasible real table produces an integral matching of the
literal named flags.

The construction simultaneously chooses:

1. which residual chunks begin at each collar rank;
2. the injective containment link from every rank `t-1` target to rank `t`;
3. every literal residual-top-to-collar-bottom containment; and
4. distinct rank-`r` owners for all completed flags.

Consequently, on the complete-layer-batch, collar-saturated face,
**anonymous surplus
transport is already the complete named containment theorem**.  The
arbitrary start-set geometry of a previously frozen SCD disappears because
the collar starts are selected in the same matching as the residual
attachments.

## 1. The joint-start matching graph

Make one bipartite graph `G=(L,R;E)`.

The right shore is a disjoint union of labelled copies of the collar
layers and the owner layer:

\[
                 R=\mathop{\dot\bigcup}_{t=t_0}^{r}R_t,
                 \qquad R_t=\{(t,T):T\in{\cal B}_t\}.              \tag{1.1}
\]

The left shore has two kinds of vertices.

* For every residual flag there is a vertex

  \[
                     f_{a,u,S}\qquad
                     (S\in{\cal B}_{s_a},\ 1\le u\le m_a).        \tag{1.2}
  \]

* For every `t>t_0`, including `t=r`, and every `A in B_(t-1)`, there is a
  collar-continuation vertex

  \[
                              c_{t,A}.                              \tag{1.3}
  \]

The edges are literal containment edges:

\[
 \begin{aligned}
 f_{a,u,S}&\sim(t,T)
   &&\Longleftrightarrow
     (a,t)\text{ is load-compatible and }S\subset T,\\
 c_{t,A}&\sim(t,T)
   &&\Longleftrightarrow A\subset T.
 \end{aligned}                                                     \tag{1.4}
\]

The continuation vertices consume exactly `C_(t-1)` of the `C_t` rank-`t`
sets.  Hence the residual flags can use at most the surplus (0.4).  At
`t=r`, this is exactly the bank of owners not occupied by a rank-`r-1`
collar chain.  This explains why (0.7), rather than merely a total socket
count, is necessary.

### Theorem 1.1 (joint-start orbit lift)

The graph `G` has a matching saturating its entire left shore if and only
if (0.6)--(0.7) is feasible.

### Proof: necessity

Given a saturating matching, let `x_(a,t)` be the number of residual
vertices of type `a` matched into `R_t`.  Every residual vertex is matched
once, giving (0.6), and unsupported pairs have value zero.

For `t>t_0`, all `C_(t-1)` continuation vertices `c_(t,A)` must use distinct
vertices of the `C_t`-element shore `R_t`.  At most

\[
                           C_t-C_{t-1}=h_t
\]

vertices remain for residual flags.  At `t=t_0` there are no continuation
vertices, so the residual capacity is `C_(t_0)=h_(t_0)`.  This is (0.7).
\(\square\)

### Proof: sufficiency

Fix a feasible table `x`.  Put

\[
             p_{a,t}={x_{a,t}\over m_aC_{s_a}}.                    \tag{1.5}
\]

Every residual vertex of type `a` sends total fractional mass `p_(a,t)`
to layer `R_t`, spread uniformly over the rank-`t` supersets of its top.
Thus every edge

\[
                         f_{a,u,S}\sim(t,T)
\]

receives weight

\[
                 {p_{a,t}\over {k-s_a\choose t-s_a}}.             \tag{1.6}
\]

Equation (0.6) says that every residual vertex sends total mass one.

Every continuation vertex `c_(t,A)` spreads one unit uniformly over its
`k-t+1` rank-`t` supersets.  Hence it also sends total mass one.

Fix `T in B_t`.  The incoming load from residual type `a` is

\[
 \begin{aligned}
 m_a {t\choose s_a}
 {p_{a,t}\over {k-s_a\choose t-s_a}}
 &=m_ap_{a,t}{C_{s_a}\over C_t}\\
 &={x_{a,t}\over C_t}.                              \tag{1.7}
 \end{aligned}
\]

Here we used the elementary identity

\[
        {{t\choose s}\over{k-s\choose t-s}}
                         ={C_s\over C_t}.             \tag{1.8}
\]

When `t>t_0`, the continuation load at `T` is

\[
                 {t\over k-t+1}={C_{t-1}\over C_t}.               \tag{1.9}
\]

Therefore the complete incoming load is at most

\[
 {C_{t-1}+\sum_a x_{a,t}\over C_t}\le1
                  \qquad(t>t_0),                                  \tag{1.10}
\]

and at the bottom rank it is

\[
                 {\sum_a x_{a,t_0}\over C_{t_0}}\le1.             \tag{1.11}
\]

We have constructed a fractional matching saturating the entire left
shore.  The bipartite matching polytope is integral, so `G` has an integral
matching saturating that shore.  \(\square\)

The proof is an orbit lift, but it does not require an equivariant integral
matching.  Symmetry is used only to construct the fractional point; ordinary
bipartite integrality performs the named rounding.

## 2. From the matching to literal named flags

### Theorem 2.1 (exact named collar chainization)

Under (0.2)--(0.7), all marked targets in the residual bank and every named
target in the collar layers

\[
                       {\cal B}_{t_0},\ldots,{\cal B}_{r-1}       \tag{2.1}
\]

partition into inclusion flags of marked load at most `D`, with distinct
rank-`r` owners.

### Proof

Use the integral matching from Theorem 1.1 and construct the collar flags
in increasing rank order, continuing through the owner layer `t=r`.

At rank `t_0`, a set `T` is matched to at most one residual flag.  If it is,
start the chain by concatenating that flag with `T`; the matching edge gives
`top(F) subset T`.  Otherwise start the singleton structural chain `(T)`.
Thus there is exactly one chain ending at every `T in B_(t_0)`.

Inductively suppose there is exactly one chain ending at every
`A in B_(t-1)`.  The matching edge incident with `c_(t,A)` extends that
chain to a distinct containing `T in B_t`.  A rank-`t` set not used by a
continuation either receives one residual flag and starts a new chain, or
starts a new singleton chain.  Right-vertex capacity makes these cases
disjoint.  Hence, after rank `t`, there is again exactly one chain ending
at every member of `B_t`.  When `t=r`, these last sets are owner labels and
are not marked lower targets; an unmatched owner is simply an empty slot.

Every collar target occurs once, because for `t<r` it is the unique
structural/marked rank-`t` member of the chain ending there at stage `t`.
Every residual flag
occurs once, and their marked target banks were pairwise disjoint.  A chain
which starts with residual type `a` at rank `t` has marked load at most

\[
                             ell_a+(r-t)\le D.         \tag{2.2}
\]

A collar-only chain starting at `t` has load `r-t<=D`.

The `t=r` part of the same joint matching sends every rank-`r-1`
continuation and every direct residual start to a distinct owner.  Every
finite strict inclusion flag inside an owner is a prefix subflag of an
ordering of that owner, obtained by listing successive set differences and
then the unused owner coordinates.  \(\square\)

This theorem is genuinely named: it assigns the actual sets, not only their
ranks.  It is also occurrence coherent at the owner-flag level: one ordering
of one distinct owner realizes every marked target in its assigned flag.

## 3. Complete-layer residual batches from arbitrary SCD rank blocks

The hypothesis (0.2) has a standard literal source which does not freeze the
collar.

Fix any symmetric chain decomposition `S_R` of the Boolean lattice and a
rank block

\[
                              I=[b,s]\subset[1,t_0-1].             \tag{3.1}
\]

For every `S in B_s`, take the members in `I` of the unique SCD chain
containing `S`.  This gives a (possibly shorter) literal inclusion flag
`F_S` with structural top `S`; the collection is indexed by the complete
rank-`s` layer.  If several disjoint rank blocks are used, their marked
target banks are disjoint.  Every flag from a block of width `w` has marked
load at most `w`.

Consequently, any disjoint block decomposition of the residual ranks gives
types satisfying (0.2), with

\[
                         s_a=\max I_a,
                         \qquad ell_a\le|I_a|.         \tag{3.2}
\]

Theorem 2.1 then says:

\[
\boxed{
 \begin{array}{c}
 \text{if the complete-layer chunk types admit the surplus table}
 \ (0.6)\text{--}(0.7),\\
 \text{then every named residual and collar target has an exact}
 \ D\text{-flag realization.}
 \end{array}}
                                                               \tag{3.3}
\]

The collar chain decomposition is not fixed in advance.  Its start sets are
exactly the rank-`t` vertices left by the joint matching after all
continuations and residual attachments have been chosen.

## 4. Exact type-cut form

The support in (0.5) is an interval condition.  A residual type of load
`ell_a` may start only at ranks

\[
                         t\ge r-D+ell_a=t_0+ell_a.    \tag{4.1}
\]

Thus the type graph has nested suffix neighbourhoods.  The transportation
table exists exactly when its threshold cuts pass:

\[
 \boxed{
 \sum_{a:\,ell_a\ge q}m_aC_{s_a}
 \le
 \sum_{t=t_0+q}^{r}h_t
 =C_r-C_{t_0+q-1}
 \qquad(1\le q\le D),}                              \tag{4.2}
\]

where `C_r=W`.  In particular, at `q=D` the right side is
`C_r-C_(r-1)`, exactly the number of owners with no rank-`r-1` collar
target.

Indeed, this is Hall for the nested type transportation graph: a chunk of
load at least `q` has a weakly smaller start menu than a shorter chunk, so
the only minimal cuts are the suffixes (4.2).  Equivalently, sort residual
loads decreasingly and collar-start capacities decreasingly and use the
usual greedy threshold matching.

Equation (4.2) is now both, on the collar-saturated joint-start face with
the declared reservations:

* the complete anonymous capacity test for this face; and
* the complete named Boolean containment test.

There is no second, exponentially large family of named-target cuts.

### Corollary 4.1 (exact chunk deficiency)

Put

\[
 A_q=\sum_{a:\,\ell_a\ge q}m_aC_{s_a},
 \qquad
 K_q=C_r-C_{t_0+q-1}.                                \tag{4.3}
\]

If all collar continuations are required, the minimum number of residual
flags which must be omitted is exactly

\[
                  \boxed{\delta_{\rm chunk}
                  =\max_{1\le q\le D}(A_q-K_q)_+.}   \tag{4.4}
\]

Indeed, the residual type graph is a nested-suffix capacitated matching
problem, whose exact Hall deficiency is (4.4).  Spread an optimal fractional
type flow over the named containment blocks as in (1.6).  The face of the
bipartite matching polytope which saturates every continuation vertex is
integral, so the same residual cardinality is attained by a literal named
matching.

There is also a target-weighted version.  Suppose every flag in a complete
type `a` has exactly `w_a` marked targets.  Maximize

\[
                        \sum_{a,t}w_ax_{a,t}           \tag{4.5}
\]

subject to the row upper bounds, the column bounds (0.7), and the support
(0.5), without requiring the row equalities (0.6).  Then

\[
 \boxed{
 \text{minimum omitted named-target weight}
 =\sum_am_aC_{s_a}w_a-\operatorname{OPT}(4.5).}       \tag{4.6}
\]

Necessity follows by projecting a named matching to its type counts.
Sufficiency follows from the same uniform block lift and weighted
bipartite-matching integrality.  Thus an `O(1)` weighted deficiency in the
finite type transportation is automatically an `O(1)` **named-target**
deficiency; no further occurrence-level loss appears in this chainization
step.

## 5. Exact scope and the surviving gate

The theorem removes a real quantifier obstruction in the two-decomposition
route.  Previously, an anonymous chunk-to-socket schedule still had to be
lifted through a separately frozen SCD whose actual start sets could violate
containment Hall.  Here the starts and attachments are selected together,
so uniform Boolean incidence plus bipartite integrality performs that lift
exactly.

It does **not** prove that the threshold inequalities (4.2) hold for the
naive minimum-piece residual chunks at coefficient-one depth.  In fact the
known Gaussian high-capacity ledger shows that simple whole-chunk recipes
can fail (4.2) by positive density even when total socket count and total
capacity both have slack.  Passing (4.2) still requires correlated
rechainization, splitting, and merging of the residual target bank.

It also does not provide:

1. the one-copy countdown/source-word serialization of these owner flags;
2. the exact physical interval addresses `(j,q)`;
3. the aperture collars `K_(j,q) subseteq S subseteq E_(j,q)`;
4. the simultaneous interval-cover condition for a fixed carrier;
5. residence or arbitrary-width upper witnesses; or
6. compatibility with the protected `Ibc/Ica` halo.

Thus (3.3) is an exact **named owner/order chainization theorem**, not yet a
universal OR word.  The remaining lower-side construction can now be split
cleanly into two tasks:

* produce complete-layer residual flag batches whose load histogram passes
  (4.2) with at most bounded marked defect; and
* serialize the resulting owner flags into one resident chronology with the
  required literal apertures.

## 6. Dependencies and relation to earlier results

The proof uses only Boolean incidence double counting and bipartite matching
integrality.  It strengthens the one-socket-layer construction in
`MATH_THEOREM_CROSS_SCD_SPARSE_TOP_COLLAR_ATTACHMENT_20260803.md` by allowing
all collar start ranks simultaneously and, crucially, choosing the collar
continuation matching in the same graph as the residual attachments.

It is also a concrete specialization of the general orbit-transport
principle in
`MATH_THEOREM_EQUIVARIANT_SAME_PARITY_TAP_DECORATED_ORBIT_FLOW_INDUCTION_20260803.md`.
The new content is the explicit joint-start graph, the exact surplus vector
`h_t`, the named collar-chain induction, and the threshold equivalence
(4.2).
