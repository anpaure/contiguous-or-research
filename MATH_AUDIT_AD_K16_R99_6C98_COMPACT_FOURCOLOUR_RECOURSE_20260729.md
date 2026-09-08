# AD audit: compact four-colour recourse and a cross-cut `6c98` conflict

Date: 2026-07-29

Deployment correction: the 51-literal clause proved here is valid but is
strictly dominated by the 26-node endpoint-cover row, as independently proved
in `MATH_AUDIT_AD_K16_R99_6C98_CUT_DOMINANCE_20260729.md`.  Do not install both.
For this `K_9-e` provider family, the same exact local recourse projection also
has a smaller 36-new-variable endpoint formulation with 41 rows.

This note gives a solver-free necessary projection of the exact integral
degree-plus-q1 add problem.  It is built from the four upper-q1 rows in the
persisted `6c98` fixed-cut core, but it is valid for every binary cut of the
frozen 858-edge source factor.  It also proves a 51-literal signed conflict
that excludes `6c98` and every completion of the same local cut assignment.

The projection is an UNSAT oracle, not a replacement for the full recourse
verifier: a compact-model SAT assignment need not extend to the other q1
colours, exact 99-seam completion, connectivity, voltage, residence, or any
deeper shadow.

## 1. Frozen incidence data

Let `S` be the 858 loopless selected source edges and let `A` be the 26,570
loopless off-source seams in the frozen k16 quotient catalogue.  The source
is degree two on all 858 quotient nodes.

The four upper-q1 colours are

\[
 T=\{(1,1883),(1,1907),(1,3255),(1,5939)\}.
\]

Their respective unique source providers are

\[
 p=(4742,22511,23229,24034).
\]

For `c in T`, let `A_c` be the loopless off-source providers of `c`.  Exact
catalogue reconstruction gives

\[
 |A_c|=35\quad(c\in T),\qquad
 \left|\bigcup_{c\in T}A_c\right|=140.
\]

The four sets are disjoint: every catalogue edge carries exactly one
upper-q1 colour.  Their union has exactly 33 endpoint nodes.  Exactly 59
source edges meet those nodes; 52 meet the 33-node set once and seven meet it
twice.

## 2. The compact model

For each of the 59 relevant source edges `e`, let `x_e` be its binary cut
bit.  For every `a in union_c A_c`, let `z_a` be a binary witness bit.  The
model `W_T(x,z)` has four activation equalities

\[
 \sum_{a\in A_c}z_a=x_{p_c}
 \qquad(c\in T),                                           \tag{2.1}
\]

and, at each of the 33 provider endpoints `v`, one capacity inequality

\[
 \sum_{\substack{a\in\cup_c A_c\\v\in a}}z_a
 \;\leq\!
 \sum_{\substack{e\in S\\v\in e}}x_e.                    \tag{2.2}
\]

All edges here are loopless, so every displayed incidence coefficient is
one.  Parallel seams remain distinct witness variables.  Thus the exact
census is:

| object | count |
|---|---:|
| relevant cut bits | 59 |
| provider-witness bits | 140 |
| binary variables | 199 |
| activation equalities | 4 |
| endpoint-capacity inequalities | 33 |
| constraints | 37 |

There is no branch lock, radius equation, motif row, portal row, or joint
cover row in this model.

### Theorem 2.1 (universal integral projection)

Fix any binary cut vector on `S`.  If there is an integral selection of
loopless off-source seams that restores exact degree at every quotient node
and preserves the complete upper-q1 palette, then `W_T(x,z)` is feasible.

#### Proof

Fix `c in T`.  If `p_c` is retained, set all `z_a`, `a in A_c`, to zero.  If
`p_c` is cut, it was the unique source provider of `c`; upper-q1 completeness
therefore forces at least one selected add seam in `A_c`.  Choose exactly one
such selected seam and set its witness bit to one.  This proves (2.1).

The provider sets are pairwise disjoint, so the chosen witnesses are distinct
selected add seams.  At any endpoint `v`, their incidence is at most the
incidence of all selected add seams.  Exact degree restitution equates the
latter with the incidence of the cut source edges at `v`, which is the right
side of (2.2).  Hence all 33 capacity rows hold.  QED.

No radius-99 or retain/delete assumption occurs in the proof.  In particular,
if this 199-variable model is infeasible under assumptions on some of its 59
cut bits, the resulting no-good is valid for every assignment of the other
799 source cut bits.  Conversely, compact feasibility is only necessary and
must not be promoted to full recourse.

## 3. A solver-free 51-literal conflict

Put

\[
 P^+=\{4742,22511,23229,24034\}.
\]

Let

\[
\begin{split}
 Z=\{&97,208,403,485,502,521,541,546,581,600,606,615,619,\
     &620,623,667,751,757,758,759,761,832,852\}.
\end{split}
\]

The 44 source edges incident with `Z` are

\[
\begin{split}
 E_S(Z)=\{&4228,4936,6266,8589,9539,12452,14906,16183,17976,18185,\
 &18647,18659,19351,19570,19757,20142,20164,20328,20359,20822,\
 &21481,21573,21581,22078,22144,22307,22391,22632,22648,22770,\
 &22775,22790,22847,22858,23414,24140,24153,24399,25817,26145,\
 &26268,26299,26314,26367\}.
\end{split}
\]

Define

\[
 P^-=E_S(Z)\cup\{21391,22520,22692\}.
\]

Thus `|P^-|=47`, `P^+` and `P^-` are disjoint, and the following clause has
51 literals:

\[
 \boxed{
 \sum_{e\in P^+}(1-x_e)+\sum_{e\in P^-}x_e\geq1.}
                                                               \tag{3.1}
\]

### Theorem 3.1 (cross-cut validity of (3.1))

Every integral full degree-plus-q1 recourse satisfies (3.1).  The conclusion
is valid for every binary cut of the frozen source, independently of branch
and radius.

#### Proof

Suppose (3.1) is false.  Then all four bits in `P^+` equal one and all 47 bits
in `P^-` equal zero.  The four activation equalities therefore each demand
one witness.  Every node in `Z` has source-cut capacity zero, so every witness
touching `Z` is forbidden by (2.2).  Exact reconstruction leaves the following
11 possible witnesses:

| colour | surviving provider seams |
|---|---|
| `(1,1883)` | `4737,4740,18552,18555,21385` |
| `(1,1907)` | `18171,18172` |
| `(1,3255)` | `21408,21411` |
| `(1,5939)` | `22529,22530` |

Both surviving `(1,3255)` providers use endpoint 576.  Its capacity is

\[
 x_{18158}+x_{21391}\leq1,
\]

so that colour consumes all available capacity there (or is already
impossible if the capacity is zero).  Both surviving `(1,5939)` providers use
endpoint 611.  Its capacity is

\[
 x_{22511}+x_{22520}=1,
\]

so endpoint 611 is saturated.  The two `(1,1907)` providers have endpoint
pairs `(490,611)` and `(490,617)`.  The first is now impossible, hence the
second is chosen and uses endpoint 617.  But

\[
 x_{22511}+x_{22692}=1,
\]

so 617 is saturated as well.  Every one of the five remaining `(1,1883)`
providers uses 576 or 617.  Its activation equality cannot be met, a
contradiction.  Therefore `W_T` satisfies (3.1).  Theorem 2.1 transfers the
clause to every full integral recourse.  QED.

The discovery cut `6c98` has all four `P^+` bits equal to one and all 47
`P^-` bits equal to zero, so its violation is exact.  The clause is strictly
more portable than the full 99-edge candidate no-good: it is indifferent to
the remaining 807 source bits not named in (3.1).

## 4. Reproducible artifacts

The build and independent replay artifacts are:

* `scratch/build_k16_r99_6c98_fourcolour_compact_recourse_20260729.py`,
  SHA-256 `7b9c6990f459c105f7b373a1d344af72acf47e3e5caebf53ce752782997c54e3`;
* `scratch/k16_r99_6c98_fourcolour_compact_recourse_20260729.model.json`,
  SHA-256 `a0b0498550564cadba58ce91c6fd4cf118840a145c8ca9a2e5f4e48da4cd71f8`;
* canonical sparse-model SHA-256
  `4c2d2087da9a895a8f1558a619b858b7f58fb872d24eadb28c2b86414d3535a6`;
* canonical 51-literal conflict SHA-256
  `c64650b2df4664b4861d1bce06dbd1f80628b58a5089e55fc7f804773a63f3f8`;
* `scratch/audit_k16_r99_6c98_fourcolour_compact_recourse_20260729.py`,
  SHA-256 `7281c2de752cf44066fd8525677a15e43cb3840acdc1a5aaf841438e48f3cdca`;
* `scratch/k16_r99_6c98_fourcolour_compact_recourse_20260729.audit.json`,
  SHA-256 `d3af84437fdf100a9d9f5d4dd6b50d708025bea8eb9aeee92f35b0e461e842a2`.

The builder and auditor both pin the source, catalogue module, discovery cut,
and persisted four-row core.  The auditor does not import the builder: it
independently reconstructs every variable registry, every activation row,
every endpoint-capacity row, and the forcing proof for (3.1).  Both scripts
invoke no solver.

## 5. Exact scope and deployment rule

The proved output is:

1. a 199-variable, 37-row necessary projection valid across all binary cuts
   of the frozen source;
2. a solver-free 51-literal Benders/no-good clause excluding an entire local
   cut cylinder containing `6c98`;
3. an exact compact assumption interface from which further cut-bit cores may
   be extracted.

This layer must not be duplicated inside a master that already contains the
full add-seam degree and q1 recourse lift: the full lift implies it.  Its use
is as a smaller first-tier recourse oracle or as a source of generalized
assumption conflicts.  An `UNKNOWN` result proves nothing, and a `SAT` result
must be escalated to full exact recourse.  Only an independently replayed
UNSAT/core result, or a solver-free conflict such as (3.1), may be learned by
the cut master.
