# K17 FRS chronological zipper: exact protected-fragment obstruction and the GMM interface

Date: 2026-07-31  
Lane: L  
Status: exact scoped obstruction and packet theorem; no K17 word, global
impossibility, or new numerical upper bound is claimed

## 0. Verdict

The authenticated 21-component four-sector factor cannot be repaired by a
K16-sized chronological `D^4` zipper that merely opens the old cycles and
reorders or reverses the retained fragments.

For the fixed one-pivot K17-FRS schedule, every old cyclic run of length two
must be broken.  The exact circular-interval transversal number is

\[
                         \boxed{2996}.              \tag{0.1}
\]

If one imposes the stronger literal request that all 5,973 old runs of
length two or three be broken, the exact number is

\[
                         \boxed{3857}.              \tag{0.2}
\]

The upper-q1 ledger makes (0.1) substantially sharper.  Of the old edges,
15,166 are the unique providers of their rank-ten union.  Among all cut
sets that hit every run-two collar, even allowing arbitrarily many cuts,
at least

\[
                          \boxed{958}                \tag{0.3}
\]

of the deleted edges are unique upper providers.  Thus a viable protected
zipper must re-create at least 958 distinct rank-ten targets while it
transports the deleted lower colours.  The minima (0.1) and (0.3) are
independent lower bounds; this note does not assert that their respective
minimizers are the same.

This is not a global K17 obstruction.  A large correlated alternating
packet may replace internal old edges, and a different chronology produced
from the new GMM endpoint-oriented residual factor need not inherit these
collars.  The new GMM theorem changes the upstream gate exactly as follows:

* the balanced residual `A/X/Y` factor with 1,430 macros now exists
  solver-free;
* in its Johnson-port subclass, pure-`U` insertion plus the joint untagged
  palette is exactly a second tight enumeration with a prescribed deck of
  1,430 directed same-level transitions; in the unrestricted macro class it
  is one integral degree-constrained `b`-flow with exact cut inequalities;
  and
* only after that correlation is solved does the chronology enter the
  upper, residence, top-port, and common-compiler gates studied here.

The old `AA` cap-two existence problem is therefore not an open prerequisite.

## 1. Frozen objects

The K17 factor is

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.components
  SHA 6b24e8ab4c77e3e5711cacab233db29733e1b27c74b735a8fb84c9a1c3643702
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_20260731.audit.json
  SHA c9284dcb1be52464b994636b7d594ee09b21dfbc1706abac228892d64cb92596
  payload 8dbc822e6cf3ed4349baa92159b9b7badd36b6e0eeed339f6490f714466bc567
```

It has 24,310 rank-nine owners and 21 cyclic components.  Its lower-q1
intersections are every rank-eight colour exactly once.  Its rank-ten edge
unions cover the complete upper-q1 palette, with load histogram

\[
             1^{15166}2^{3733}3^{519}4^{29}5^1.     \tag{1.1}
\]

Its cyclic positive-run counts begin

\[
                    (N_1,N_2,N_3)=(0,3705,2268),    \tag{1.2}
\]

and its all-width consecutive-OR atlas has 1,937 holes:

\[
              11:1572,\qquad 12:358,\qquad 13:7.   \tag{1.3}
\]

Their sorted newline-hex list has SHA
`8d8bf37f364145aa1593769953a864995d64e259affadd06fae0ac525c8e0890`.

The exact K17 terminal schedule is in

```text
MATH_THEOREM_K17_TIGHT_STAIRCASE_RAINBOW_GUARD_ORBIT_COMPILER_20260731.md
  SHA 9e8b81652176031790c8b60cac33c6d9062f4d4fad5c3bf61bec28afe7dcab83
```

The K16 chronological fixture is

```text
MATH_THEOREM_AD_K16_LITERAL_D4_ZIPPER_AND_PHASE_JUMP_RULE_20260731.md
  SHA bcc8fb188eeb6f9dd5fc1bbce398dc4179a2b1d9cbbc076cceba936830437153
scratch/ad_k16_literal_d4_zipper_phase_rule_20260731.audit.json
  SHA 6b79652f47d512cee53913f397cc56a2cafaaeb592756b04b631b19e4aa8509b
  payload 066477d7912cfd9bc4e622615d75fb21000fb581ac8bd56cf6aeed82e13a6f3a
```

The new upstream theorem is

```text
MATH_THEOREM_K17_GMM_ENDPOINT_ORIENTED_RESIDUAL_FACTOR_20260731.md
  SHA 20d37788b9927df7fe6c4f2e41597bec9158c432917d270b4e43c5ac28e2d5bd
```

## 2. What the K16 zipper actually proves

The K16 substitution has 49 omitted owners and 49 literal shifted facet
occurrences.  Value containment alone gives a 128-edge bipartite graph and
does not select the physical phase.  Requiring the same displayed `D^3`
occurrence to extend by one literal cell on its left or right gives a
96-edge graph

\[
                         P_8\ \dot\cup\ P_{90}.      \tag{2.1}
\]

It has a unique perfect matching: four right/head extensions on the long
collar and 45 left/tail extensions on the opened short cycle.  The final
right extension of the short cycle would start at `D4[12869]`, which does
not exist in the linear word.  Removing that wrap edge turns the alternating
cycle into `P_90` and forces the phase.

Two lessons are load-bearing.

1. A facet value is not a chronological port.  The added cell, side,
   physical occurrence, and linear boundary belong to the matching row.
2. Uniqueness appears only after the literal chronology is imposed.
   Marginal containment is too weak.

For the K17 factor, the naive facet-occurrence/owner incidence graph has one
left node for every old edge colour and one right node for every owner, with
the edge-colour node adjacent to its two endpoint owners.  It is just the
barycentric subdivision of the 21 source cycles.  Hence it has 21 even-cycle
components and exactly

\[
                         2^{21}=2,097,152            \tag{2.2}
\]

perfect matchings.  There is no analogue of the K16 boundary-forced phase
until actual cycle openings and literal side extensions are supplied.

## 3. The protected-collar theorem

Let one source component be

\[
                    C=(v_0,v_1,\ldots,v_{n-1})
\]

with old edge `e_i=v_i v_(i+1)` modulo `n`.  For a coordinate whose cyclic
trace has a bounded positive run of length `ell` beginning at `v_a`, define
its edge collar by

\[
              \Gamma(a,\ell)=
              \{e_{a-1},e_a,\ldots,e_{a+\ell-1}\}. \tag{3.1}
\]

For an all-one coordinate on a triangle, the source audit records one cyclic
run of length three; its opening collar is all three edges.

### Lemma 3.1 (collar persistence)

Suppose a rethread deletes a set `D` of old edges and retains every other
old edge inside path fragments, which may then be reordered and reversed.
If

\[
                         D\cap\Gamma(a,\ell)=\varnothing,
\]

then the final chronology still contains the consecutive trace

\[
                              0\,1^\ell\,0.          \tag{3.2}
\]

#### Proof

Every edge between the two bounding zero vertices and through the positive
run belongs to (3.1).  If none is cut, all of those vertices lie in one
retained fragment in their old order.  Reversal only reverses (3.2), which
is the same binary word.  External seams cannot enter its interior.  \(\square\)

### Lemma 3.2 (FRS forbids a bounded run two)

Put `P=7401`.  In the one-pivot K17-FRS schedule, one coordinate satisfies

\[
 t_i=\bigvee_{j=i}^{i+2}q_j\quad(i<P),\qquad
 t_i=\bigvee_{j=i}^{i+3}q_j\quad(i\ge P).            \tag{3.3}
\]

Every occurrence `q_j=1` away from a global end contributes a consecutive
owner interval of length at least three.  This remains true across the
pivot: `j=P` contributes at `P-2,P-1,P`, and `j=P+1` contributes at
`P-1,P,P+1`.  Unions of such intervals have no bounded component of length
two.  The only length-two truncations can touch a global endpoint.

Consequently, a retained `0 11 0` block is impossible in K17-FRS.  By
Lemma 3.1 every run-two collar of the old factor must meet `D`.

### Theorem 3.3 (exact circular stabbing)

For any finite family of circular intervals, force one selected root edge
`r` in a fixed interval.  Discard every interval containing `r`, cut the
circle at `r`, and greedily stab the remaining ordinary intervals by their
earliest right endpoints.  This is optimal conditional on `r`.  Every
nonempty transversal contains some edge of the fixed interval, so minimizing
over its possible roots is globally exact.

The source components are disjoint, so their minima add.  In literal
component-file order, the run-two minima are

\[
\begin{split}
(247,907,1174,8,2,1,1,1,1,2,1,1,1,1,2,{}&490,135,14,2,1,4),
\end{split}                                                       \tag{3.4}
\]

which sum to 2,996.  For run lengths two and three jointly they are

\[
\begin{split}
(317,1144,1455,9,2,1,1,1,1,2,1,1,1,1,2,{}&682,208,19,2,2,5),
\end{split}                                                       \tag{3.5}
\]

which sum to 3,857.

Equation (3.4) is FRS-necessary.  Equation (3.5) is the stronger
all-old-short-runs condition requested for a uniformly residence-clean
carrier.  It is not FRS-necessary: an old length-three run may be legal when
its final start lies in the length-three corridor.  Neither condition is
sufficient, because new seams can create new short runs.

### Corollary 3.4 (958 forced literal upper debts)

Call an old edge upper-private if its rank-ten union has load one in (1.1).
There are 1,089 coordinate-labelled run-two collar occurrences all of whose
edges are upper-private.  Selecting every nonprivate edge for free leaves
exactly these all-private constraints.  Their exact circular-interval
transversal numbers by component are

\[
 (77,288,388,2,1,0,0,0,0,1,0,0,0,0,2,156,37,3,1,1,1),          \tag{3.6}
\]

which sum to 958.  Therefore every set hitting all run-two collars deletes
at least 958 upper-private edges.  Conversely, (3.6), together with all
nonprivate edges, hits every run-two collar, so 958 is exact when only the
number of upper-private deletions is minimized.

The 958 unions are distinct by upper privacy.  Any upper-q1-preserving
packet must add at least one new edge with each of those unions.  For the
strict run-two/three collar family the analogous exact number is 1,262.

## 4. Exact lower/upper packet ledger

For a Johnson edge `e=uv`, write

\[
                         \lambda(e)=u\cap v,
             \qquad     \mu(e)=u\cup v.             \tag{4.1}
\]

Let `F` be the old 21-cycle factor, let `D` be deleted old edges, and let
`A` be added Johnson seams.  Suppose the uncut edges are retained and the
result is one Hamilton path `T` on all 24,310 owners, required to retain the
lower-q1 rainbow and upper-q1 coverage in the linear one-hole sense.  Cancel
any edge appearing in both edit lists, so `D` and `A` are normalized and
disjoint.

### Theorem 4.1 (protected chronological packet conditions)

The following rows are necessary.

1. **Topology.**
   \[
                         |D|=|A|+1.                 \tag{4.2}
   \]
2. **Lower q1.**  Since `F` uses every rank-eight colour once, a final
   lower-rainbow path has a unique missing edge colour `b` and
   \[
             \{\lambda(a):a\in A\}
              =\{\lambda(d):d\in D\}\setminus\{b\} \tag{4.3}
   \]
   as occurrence-labelled sets.  In an FRS lift, `b` must be supplied by
   the separately certified non-edge top port; palette equality alone does
   not identify that occurrence.
3. **Upper q1.**  For every rank-ten target `U`,
   \[
      \operatorname{load}_F(U)
       -|\{d\in D:\mu(d)=U\}|
       +|\{a\in A:\mu(a)=U\}|\ge1.                 \tag{4.4}
   \]
4. **Old and new residence.**  `D` hits every run-two collar.  In addition,
   the endpoint-state composition across every new seam must satisfy the
   actual one-pivot FRS run language; collar hitting alone does not prevent
   seam-created `010` or `0110`.
5. **Full deep replay.**  Every one of the 41,226 masks of rank greater than
   nine has a literal consecutive interval of `T` whose OR is that mask.
   In particular, each of the 1,937 old holes needs a new witness crossing
   at least one edge of `A`, because the old cyclic atlas contains no witness
   for it.  The other 39,289 masks must also be revalidated: deleting old
   edges may destroy all of their previously available witnesses.
6. **Physical top ports.**  The 24,310 rank-eight top cells occupy distinct
   maximal same-start occurrences.  Three other starts have lower-rank
   tops.  Any use of an old factor edge as a top port must name the actual
   start occurrence and side; an abstract copy of its colour is not enough.
7. **Common compiler.**  The same chronology admits nonempty
   `Q_0,...,Q_24312` satisfying (3.3) and the exact 65,535-cell FRS atlas.
   No marginal q1, residence, or upper ledger implies this row.

Conversely, if a packet gives the Hamilton chronology, the literal full
all-width replay in row 5, and an exact K17-FRS assignment on that same
chronology, the exact compiler theorem constructs a universal word of length
24,313.  Thus these rows are an exact terminal checklist, while rows 1--6
without row 7 are only necessary projections.

The useful finite column for a future zipper catalogue is therefore not a
bare Johnson seam.  It must carry

\[
 (\text{old edge occurrences},\lambda\text{-transport},
   \mu\text{-debts/restoration},\text{endpoint run map},
   \text{full upper-witness ledger},\text{top-port eligibility}).\tag{4.5}
\]

The packet chooses correlated columns satisfying (4.2)--(4.5).  This is the
K17 analogue of the K16 chronological graph.

## 5. Literal owner-aligned top-port dichotomy

The following small lemma records the strongest safe simplification of row
6.  It is conditional on the **owner-aligned face**: starts `0,...,W-1`,
where `W=24310`, carry all `W` rank-eight top cells, and the three terminal
starts carry the lower-rank tops.

Put

\[
 H_i=Q_i\vee Q_{i+1}\quad(i<P),\qquad
 H_i=Q_i\vee Q_{i+1}\vee Q_{i+2}\quad(i\ge P),      \tag{5.1}
\]

for `0<=i<W`.  For `1<=i<W`, `i != P`, equation (3.3) gives

\[
                        H_i\subseteq T_{i-1}\cap T_i.\tag{5.2}
\]

If `T` is a Johnson path and `H_i` has rank eight, equality holds.  The
pivot `i=P` is exceptional because the owner window changes length.

Assume additionally that the path-edge colours are distinct and miss `b`.
Let \(e_P=T_{P-1}\cap T_P\).  The `W-2` nonexceptional `H_i` are the
corresponding incoming edge colours.  Comparing the complete rank-eight
top-cell deck with the path-edge deck gives the exact two-element identity

\[
                         \{H_0,H_P\}=\{b,e_P\}.     \tag{5.3}
\]

Thus the boundary and pivot ports are either aligned or swapped.  If any
of the three lower-rank top cells occurs at an owner start, this reduction
is invalid and one must retain the full occurrence-labelled port matching.

## 6. Rebase on the GMM residual factor

The GMM endpoint-oriented theorem proves that the authenticated `6390+45`
K15 parent has a balanced residual `A/X/Y` path factor consisting of exactly

\[
                         \operatorname{Cat}_8=1430  \tag{6.1}
\]

macros.  The proof is solver-free: tight enumeration supplies the residual
forest, and endpoint orientation reduces to the degree-at-least-two
condition on the two contracted parent cycles.

In the Johnson-port subclass, its Theorem 6.1 gives the exact next gate.
The complete pure-`U` deck and the 1,430 oriented macros can be arranged in
one colour-bijective cycle if and only if an upper tight enumeration realizes
the 1,430 ordered macro endpoint pairs as its direct same-level transitions.
Existence of the two tight enumerations separately is not enough; their
direct-transition decks must agree.

For unrestricted macros, Theorems 7.1 and 8.1 remove the Johnson-port
condition under their stated distinct-port hypotheses.  If `m_T` is the
number of macro ports labelled by the rank-eight old colour `T`, put
`d_T=2-m_T`.  Pure-`U` insertion and the complete
untagged palette exist as a (possibly disconnected) two-factor exactly when
the rank-nine/rank-eight containment graph has an integral subgraph with

\[
                 \deg(U)=2,\qquad \deg(T)=d_T.       \tag{6.2}
\]

Equivalently, every family `S` of pure-`U` owners satisfies

\[
  2|S|\le\sum_T
   \min\bigl(d_T,|\{U\in S:T\subset U\}|\bigr).     \tag{6.3}
\]

The complementary form needs only port-weighted full stars and unported
stars missing one member.  Network integrality is automatic.  If every
physical macro may be reversed, connectivity of the completed two-factor is
the sole remaining owner/q1 row after a feasible flow.  If macro directions
are frozen, the selected cycles must additionally satisfy the theorem's
macro-coherence condition.  Neither row is implied by the scalar cuts.

The frozen 21-component factor is a useful positive local fixture for the
numerical insertion ledger.  Its pure `U` shore is a forest of 737 paths:

\[
   \underbrace{4268}_{U\text{-internal}}
   +\underbrace{1474}_{737\ X\!-\!U+737\ U\!-\!Y\text{ ports}}
   +\underbrace{693}_{\text{direct }Y\!-\!X}
   =6435.                                                        \tag{6.4}
\]

Every `U` path has exactly one `X` port and one `Y` port, and all 6,435
untagged lower colours occur.  This authenticates the component-neutral
palette mechanism, but not its transplantation to the GMM macros.  The GMM
residual skeleton and this 737-path port fixture are separate certificates;
endpoint correlation, chronology, and the single-cycle condition are not
inherited.

There are therefore two exact live routes.

1. **GMM-first:** choose the endpoint-oriented residual macros, solve the
   exact integral `b`-flow, connectivity, and any required directed
   macro-coherence row (or use the stronger prescribed-transition second
   tight enumeration), open one seam, and then test the resulting chronology
   for upper service, FRS residence, top ports, and the common compiler.
2. **Frozen-factor repair:** retain the present q1-complete 21-cycle factor
   and use a genuinely global correlated packet.  On the protected-fragment
   face it must satisfy at least (0.1) and (0.3); internal alternating
   replacement can escape those numerical bounds but must still satisfy the
   literal packet rows of Theorem 4.1.

The first open upstream gate is now `U`-deck/macro endpoint correlation and
the joint untagged palette, not `AA` cap-two existence.  The downstream
upper/residence/compiler problem is common to both routes.

## 7. Audit certificate and exact scope

The deterministic replay is

```text
scratch/audit_k17_frs_chronological_zipper_collar_obstruction_20260731.py
  SHA bc208aefc8f0e2fa521d7d34e3b52b00d02f8de9e004488f8d297cc8313342d1
scratch/k17_frs_chronological_zipper_collar_obstruction_20260731.audit.json
  SHA 6c808ef12af84ea1b24a2485fc97848765f675eba32085fa1ae86b3cff164182
  payload 7cec83df1f3e1fdf338e6cd193a3f9c3a5f14f46504436123966fbdcd833b41e
```

It independently replays the owners, both q1 palettes, upper load profile,
all 1,937 deep holes, the 737-path `U` ledger, both circular stabbing
problems, the 958/1,262 forced-private upper-debt problems, and the K16
chronological fixture.  The full literal cut witnesses are stored in the
JSON.

The proved negative scope is only:

> no cut/reorder/reverse rethread retaining every uncut edge of the frozen
> `6b24e8ab...` factor can satisfy one-pivot K17-FRS after fewer than 2,996
> old-edge cuts, and every such rethread deletes at least 958 old edges that
> are unique upper-q1 providers.

No claim is made against internal alternating circuits, a different GMM
chronology, an unrestricted K17-FRS schedule, or K17 itself.
