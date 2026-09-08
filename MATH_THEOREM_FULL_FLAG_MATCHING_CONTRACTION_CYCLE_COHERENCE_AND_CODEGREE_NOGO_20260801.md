# Contracting a full flag matching does not round root groups: exact cycle coherence and the `k=17` codegree audit

Date: 2026-08-01

Status: unconditional contraction/cycle theorem, exact degree calculations,
and an authenticated obstruction for the deterministic reset-containing
`k=17` full-host matching.  It rules out the proposed order of quantifiers
“perfect-match all flag options, then contract/select roots.”  It does not
rule out choosing a root-coherent matching prospectively.

## 0. Outcome

At depth three, let

\[
                         t=m(m-1)                              \tag{0.1}
\]

be the number of decorated flag orbits at one middle-root orbit.  A perfect
matching `Pi` of the complete flag-option turn graph has `tN` edges, where
`N` is the number of root necklaces.  Contracting flag options to their root
groups produces a three-resource multihypergraph on

\[
                R_{\rm tail}\mathbin{\dot\cup}
                R_{\rm head}\mathbin{\dot\cup}O.             \tag{0.2}
\]

Every tail and head root has degree exactly `t`, and the average owner
degree is `t`.  These attractive marginals are not enough.

The matching `Pi` is a permutation of the decorated flag options after the
two copies of a flag are identified.  A one-flag-per-root chronology using
only edges of `Pi` must be a union of permutation cycles, with each root
group hit exactly once.  Contracting individual edges forgets this invariant
subset condition.

For the deterministic H100 `k=17` matching containing the opened reset:

* tail/head root degree is `t=56`;
* owner degrees range from 18 to 234, despite average 56;
* maximum pair codegrees `(tail,head)`, `(tail,owner)`, `(head,owner)` are
  respectively 9, 36, and 50;
* the permutation has only eight cycles, one of length 36,125;
* only two cycles are root-simple, containing just 18 flag options total.

Thus every root-coherent union of its cycles covers at most 18 of the 1,430
root groups.  The exact root deficiency is at least 1,412.  No independent-
transversal or absorption theorem applied **after this matching is chosen**
can repair it without changing the matching itself.

High-target degrees are regular before root contraction:

\[
 \deg(T_{m-1})=(m+2)(m-1),
 \qquad
 \deg(T_{m-2})=(m+3)(m+2).                           \tag{0.3}
\]

At `m=8` these are exactly 70 and 110.  They do not cure the cycle
coherence obstruction.

## 1. Decorated flag identities

Let `Omega` be the set of rotation orbits of complete depth-three flags

\[
                         f=(q;z_1,z_2),                       \tag{1.1}
\]

one set of identities, not separate tail and head copies.  The root action
is free, so every root orbit `Q` has

\[
                         |\Omega_Q|=m(m-1)=t                 \tag{1.2}
\]

identities: choose the ordered distinct pair `(z_1,z_2)` in a root.

Normalize the tail copy of `f` by rotating `z_2` to zero, and normalize its
head copy by rotating `z_1` to zero.  These are two representations of the
same identity.  Let

\[
                         J:\Omega_{\rm head}\longrightarrow\Omega
                                                                  \tag{1.3}
\]

be the literal identification map.

A perfect matching

\[
                         \Pi:\Omega_{\rm tail}
                         \longrightarrow\Omega_{\rm head}       \tag{1.4}
\]

therefore defines the permutation

\[
                         \sigma=J\circ\Pi\quad\text{on }\Omega.  \tag{1.5}
\]

## 2. Exact root-coherence theorem

### Theorem 2.1 (cycle-union criterion)

There is a directed cycle cover using only edges of `Pi` and using one
common flag identity at every root orbit if and only if there is a
`sigma`-invariant set `S subseteq Omega` such that

\[
                         |S\cap\Omega_Q|=1
                         \qquad(Q\in R).                       \tag{2.1}
\]

Equivalently, some union of cycles of `sigma` hits every root group exactly
once.

#### Proof

Suppose one flag `f_Q` is selected at every root.  Its outgoing turn in
`Pi` enters the head flag `sigma(f_Q)`.  Head/root consistency says that
this must be the selected identity at the head root.  Hence the selected
identity set is closed under `sigma`; finiteness makes it invariant.  The
one-per-root equations are exactly (2.1).

Conversely, if `S` is invariant and satisfies (2.1), restrict `Pi` to the
tail identities in `S`.  Invariance makes its head identities exactly `S`.
Thus every selected flag has one outgoing and incoming turn, and every root
has one common selected flag. \(\square\)

### Corollary 2.2 (eligible-cycle exact cover)

A cycle of `sigma` which visits one root group twice can never be selected.
Call a cycle **root-simple** when its root groups are all different.  The
rounding problem after `Pi` is frozen is the exact cover of all root groups
by root-simple `sigma`-cycles.

Owner exactness adds the requirement that the turn edges on the selected
cycles have distinct owner colours.  High-target exactness adds the
requirement that their flag vertices offer every required target, after
which one occurrence may be marked.  These are constraints on whole cycles,
not on independent edges.

In particular, if `sigma` is one cycle and `t>1`, no nonempty proper
invariant set exists and selecting the whole cycle uses all `t` flags at
every root.  Such a matching is maximally unroundable despite perfect local
degrees.

## 3. Degrees after edge contraction

Contract each edge `e=(f,g)` of `Pi` to

\[
             (Q_{\rm tail}(f),Q_{\rm head}(g),[q(f)\cup q(g)]).
                                                                  \tag{3.1}
\]

Let `H_Pi` be the resulting three-partite multihypergraph.

### Proposition 3.1 (universal degree ledger)

For every `Pi`,

\[
 \deg_{H_\Pi}(Q^-)=t,
 \qquad
 \deg_{H_\Pi}(Q^+)=t,                                \tag{3.2}
\]

and

\[
                 \sum_{O\in\mathcal O}\deg_{H_\Pi}(O)=tN,
 \qquad
                 {1\over N}\sum_O\deg(O)=t.           \tag{3.3}
\]

#### Proof

Every root group contains `t` tail identities and `Pi` matches all of them;
this gives the first equation.  It also saturates all `t` head identities
at every root, giving the second.  Every matched edge has one owner colour,
so summing owner degrees counts all `tN` edges. \(\square\)

There is no corresponding owner-regularity theorem for an arbitrary perfect
matching.  Nor is there a useful universal small-codegree bound: any pair
of contracted resources can share as many as `t` selected edges, the full
degree of a root group.

Thus the standard near-regular/small-codegree hypotheses used by matching
nibbles or exact absorbers are not inherited merely from regularity of the
uncontracted flag graph.

## 4. High-target mark degrees

Every flag identity (1.1) offers

\[
                 A(f)=q-\{z_1\},
 \qquad          B(f)=q-\{z_1,z_2\}.                         \tag{4.1}
\]

### Proposition 4.1 (exact full-host target degrees)

Every named rank-`m-1` target is offered by exactly

\[
                         (m+2)(m-1)                           \tag{4.2}

flag identities.  Every named rank-`m-2` target is offered by exactly

\[
                         (m+3)(m+2)                           \tag{4.3}

flag identities.

When the relevant rotation actions are free, the same numbers are the
degrees of the target necklaces in the quotient flag-option set.

#### Proof

Fix a rank-`m-1` target `A`.  Choose the extra root coordinate `z_1`
outside `A` in `m+2` ways and choose `z_2 in A` in `m-1` ways.  This gives
(4.2).

Fix a rank-`m-2` target `B`.  Choose the ordered distinct pair `(z_1,z_2)`
from its complement, whose size is `m+3`.  This gives (4.3). \(\square\)

At the physical level, a fixed incident root/target pair has codegree
`m-1` at rank `m-1` and codegree two at rank `m-2`.  A nested pair
`B subset A` of the two target ranks has codegree `m+2`.  Quotient alignment
can combine several physical incidences, so its codegrees can be larger.

These target vertices are coverage resources, not exact one-use shores:
the final selector may offer a target several times and mark one occurrence.
Consequently adjoining them to (3.1) does not turn the problem into a
uniform perfect-hypergraph matching.

## 5. Authenticated `k=17` contraction

The deterministic full-host matching used by the reset-extension audit has
the following exact contracted ledger:

\[
\begin{array}{c|c}
\text{quantity}&\text{value}\\ \hline
\text{tail/head root degree}&56\\
\text{owner degree min/max}&18/234\\
\text{missing owner colours}&0\\
\Delta_2(\text{tail,head})&9\\
\Delta_2(\text{tail,owner})&36\\
\Delta_2(\text{head,owner})&50\\
\text{rank-7 target degree}&70\\
\text{rank-6 target degree}&110\\
\Delta_2(\text{root,rank-7 target})&14\\
\Delta_2(\text{root,rank-6 target})&6\\
\Delta_2(\text{rank-7,rank-6 targets})&20.
\end{array}                                                   \tag{5.1}
\]

In particular,

\[
             {\Delta_2(\text{head,owner})\over
               \deg(\text{head})}={50\over56},               \tag{5.2}
\]

so this contracted object is nowhere near a small-codegree regime.

Its permutation has cycle ledger

\[
 \#\text{cycles}=8,
 \qquad\ell_{\min}=4,
 \qquad\ell_{\max}=36125.                            \tag{5.3}
\]

Only two cycles are root-simple and together contain 18 vertices.  By
Corollary 2.2, every root-coherent union covers at most 18 roots.  Therefore

\[
                         \text{root deficiency}\ge1430-18=1412. \tag{5.4}
\]

This is an exact obstruction for this `Pi`, not a heuristic failure of an
algorithm.

## 6. Consequence for asymptotic rounding

The proposed order of operations was:

\[
 \text{perfect-match the complete flag host}
 \longrightarrow
 \text{contract root groups}
 \longrightarrow
 \text{round one edge per root/owner/target}.          \tag{6.1}
\]

Theorem 2.1 shows that (6.1) has discarded the decisive constraint.  The
correct atoms after `Pi` is frozen are its root-simple permutation cycles,
not its individual matched edges.  In the audited instance their total
supply is only 18 vertices.

Therefore no standard independent-transversal theorem on the contracted
edge hypergraph can be sound: it may choose outgoing and incoming edges
which correspond to two different flags at the same root.  Nor can a
near-regular small-codegree absorber apply to the audited contraction, by
(5.1)--(5.2).

A viable asymptotic theorem must reverse the quantifier:

> choose `Pi` together with a root-transversal invariant set, or construct
> `Pi` so that it already has a spanning system of root-simple cycles,
> while simultaneously balancing owner colours and high-target marks.

That is exactly the root-coloured circulation/three-resource problem.  The
complete-host biregularity is useful fractional supply, but choosing an
arbitrary perfect matching first destroys the flexibility needed to round
it.

## 7. Audit artifacts

The updated H100 `-O3` audit is

`scratch/audit_k17_full_flag_host_reset_extension_20260801.cpp`

with frozen transcript

`scratch/audit_k17_full_flag_host_reset_extension_20260801.txt`.

It reconstructs the complete graph, fixes the opened reset path, computes
the perfect matching, identifies the two normalized copies of every flag,
forms `sigma`, and replays every degree, codegree, target mark, and cycle
statistic in (5.1)--(5.4).

SHA-256:

* source: `95147c5b5b863c4124c06cf70669bc2d94400fa31194008ec8bab05e6bc0cec4`;
* transcript: `7df38c16d545258febecd57000a9493691aa1d39188b1d411bb7ba3d7cc0337a`.
