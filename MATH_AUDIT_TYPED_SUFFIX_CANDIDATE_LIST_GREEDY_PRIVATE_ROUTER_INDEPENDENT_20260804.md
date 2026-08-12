# Independent audit: typed suffix candidate-list greedy private router

**Date:** 2026-08-04  
**Verdict:** **PASS after an exact privacy clarification.**  The ordered
list-conflict argument and its regular-factor composition are correct under
the literal fixed-state, capacity, type, and prefix-privacy hypotheses now
stated in the theorem.  They are sufficient certificates, not necessary
characterizations of routability.

## 1. Audited bytes

| role | file | SHA-256 |
|---|---|---|
| audited theorem, corrected current bytes | `MATH_THEOREM_TYPED_SUFFIX_CANDIDATE_LIST_GREEDY_PRIVATE_ROUTER_20260804.md` | `4f5c3687f785173977853050fc7c6097115a46b15a205cc2b540a90f1c4697fb` |
| regular-factor composition used by the theorem | `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md` | `2d64e2cb36b65706133ae1e68c6bdda80d433ccd428259860382a301538096d0` |
| exact factor-restricted boundary | `MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md` | `09acd8673956a2e43ec97d1d67ff01d4e3ceb1ea230af0e796a762b84d142906` |
| prior independent factor-router audit | `MATH_AUDIT_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_INDEPENDENT_20260804.md` | `e9aed2a8806eaa47dcc3c6f01b207f656f0d6a0f7517a010a98172f54cf7525c` |

The supplied pre-audit theorem hash was
`f878fea79fb1418349d85cfabbf3d3640110a425b031848c38a1fe0affc0addc`.
The correction deletes every nonterminal prefix vertex, including claim
starts, from the suffix network; it also makes the one-step Boolean
injectivity premise literal.  No conclusion or inequality changed.

## 2. Directional greedy replay

For a previously chosen candidate `R_j`, the definition

\[
 \Delta_{ji}=\max_{R\in C_j}
 |\{S\in C_i:S\text{ conflicts with }R\}|
\]

implies that `R_j` removes at most `Delta_(ji)` members of `C_i`.  The
forbidden members arising from distinct earlier lists may overlap, so the
union bound gives the valid upper bound

\[
 \left|\bigcup_{j<i}F_{ji}(R_j)\right|
 \le \sum_{j<i}\Delta_{ji}.
\]

The strict inequality in (1.1) therefore leaves at least one member of
`C_i`.  Induction gives one candidate per port with no common
unit-capacity vertex and no repeated sink occurrence.  Because the ports
are distinct starts and all physical vertex capacities have been
node-split, this is a full strict-gammoid linkage and proves

\[
 r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|.
\]

The asymmetry of `Delta_(ji)` is intentional and harmless: only the load
of an already selected `C_j` candidate on the future list `C_i` is needed.
The uniform consequence follows immediately from
`Delta_(ji)<=Delta` and `i-1<=m-1`.

## 3. Capacity-faithful factor composition replay

Fix the suffix `R_p` selected for every active port.  On every incidence
`gp`, send `1/h` along the concatenation `Q_(gp) R_p`.

The complete load ledger is:

1. the source arc of gain `g` carries `h(1/h)=1`;
2. a private prefix interior carries `1/h`;
3. an allowed common gain start carries one unit in total;
4. port `p`, every vertex of `R_p`, and its sink arc carry
   `deg_B(p)/h<=1`;
5. distinct selected suffixes share no unit capacity and have distinct
   sinks;
6. suffixes meet no prefix vertex except their own terminal port, because
   every other prefix vertex was deleted before the candidate lists were
   formed;
7. the fixed compensation linkage is disjoint because all of its capacities
   and sinks were deleted first.

Thus the displayed mixture is a feasible single-commodity flow of value
`|G|` in an integral unit-capacity network.  Integral max flow has the same
value.  Since the `|G|` source arcs have total capacity `|G|`, each is
saturated; unit sink arcs then give distinct terminal occurrences.  Any
integral reassignment at a port remains type-correct because every selected
suffix type at that port is legal for every incident gain.

The original wording deleted prefix interiors but did not explicitly
delete claim starts.  A suffix traversing a claim start would invalidate
the above load ledger.  The corrected theorem now uses the exact condition
from the regular-factor theorem: the suffix network deletes every prefix
vertex other than its terminal port.

## 4. Exact sufficiency and non-necessity scope

The logical implications actually proved are

\[
 \text{ordered list-conflict inequality}
 \Longrightarrow r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|
 \Longrightarrow \text{all gains routable through the fixed factor}.
\]

Neither arrow is an equivalence in general.

- The greedy inequality is only a list-order certificate.  A full suffix
  linkage can exist when every ordering violates it.
- Linking every active port is stronger than necessary for routing the
  gains when the integral factor flow can use only a subset of ports.
- Individual nonempty menus are insufficient: a common unit suffix
  bottleneck can leave every port individually reachable while the full
  port rank is one.
- Prefix privacy is a sufficient clean load condition.  It may be replaced
  by a separate verified congestion calculation, but cannot simply be
  omitted.
- All prefixes, candidates, guards, occurrence identities, compensation
  deletions, and sink types must coexist in one materialized state.  The
  theorem cannot combine alternatives from different phases or parent
  realizations.
- The Boolean `mu<=1` specialization additionally needs at most one
  candidate over each upper value in each list and global injectivity of
  the private sink occurrences.  Without those hypotheses, `mu` must be
  counted on the literal candidate atlas.

## 5. Final verdict

The corrected theorem is a valid, directly checkable sufficient router
certificate.  It does not prove that the current parent supplies its
candidate lists, does not authenticate transported phase one, and does not
imply an all-dimensional carrier or `nu(k)<=B(k)+O(1)`.

