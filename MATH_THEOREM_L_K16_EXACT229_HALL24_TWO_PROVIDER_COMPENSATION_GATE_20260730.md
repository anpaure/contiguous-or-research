# Exact229 Hall-24 two-provider compensation gate

Date: 2026-07-30  
Status: **exact algebra and finite join catalogue PASS; the known reciprocal
two-provider pair is rejected before final Hall; no unrestricted successor is
claimed**

## 1. Frozen states and the basin identity

Let `W` be the authenticated exact229 chronology

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
SHA-256 cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974.
```

All rows have rank eight.  The lower compiler has 26,332 targets, maximum
matching 26,307, and deficiency 25.  Its twelve zero-provider targets are

```text
2665 28e9 291d 29a9 2f28 4879
48e9 4e70 6989 6a29 6c70 8000.
```

Write `Z(X)` for the number of these twelve targets still having degree zero
in the literal compiler graph of a chronology `X`, and write `H(X)` for its
number of unrestricted upper holes.  The two sharp Hall-24 trades are:

| state | new lower provider | upper debt | `Z` | `H` | Hall deficiency |
|---|---|---|---:|---:|---:|
| exact229 `W` | none | none | 12 | 0 | 25 |
| alpha / S4 | `4e70` | `4e79` | 11 | 1 | 24 |
| beta / hit14 | `8000` | `4e7e` | 11 | 1 | 24 |

Thus all three have

\[
 Z(X)+H(X)=12,
 \qquad
 \operatorname{def}(G_X)-Z(X)=13.                 \tag{1.1}
\]

The second equality is the shared nonzero-component term.  For a proposed
composition whose residual nonzero-component term is separately certified to
remain 13, closing one upper hole without retaining a second independent lower
augmentation cannot improve Hall beyond deficiency 24.  A Hall-23,
upper-complete descendant in that certified fibre needs at least two of the
twelve zero targets filled simultaneously:

\[
 Z\le 10,\qquad H=0,\qquad \nu(G)\ge26309.        \tag{1.2}
\]

Equation (1.2), rather than upper closure by itself, is the production gate.
If a move closes an upper hole by sacrificing the first provider, it merely
transports the same defect quantum.

The identity (1.1) is authenticated for these three states.  It is not
asserted for an arbitrary chronology whose nonzero Hall components change.
For such a chronology the unconditional condition is the last inequality in
(1.2), checked on the full occurrence-labelled graph.

## 2. Exact two-trade normal form

Use occurrence labels, not just row values.  For an upper mask `u`, let
`I_X(u)` be the occurrence-labelled contiguous intervals of chronology `X`
whose literal OR is `u`.  Given two position permutations `a,b`, the final
witness set partitions exactly into

\[
I_{ab}(u)=K_u\mathbin{\dot\cup}A_u\mathbin{\dot\cup}
            B_u\mathbin{\dot\cup}C_u,              \tag{2.1}
\]

where, in priority order,

\[
\begin{aligned}
K_u&=I_W(u)\cap I_{ab}(u),\\
A_u&=(I_a(u)\setminus I_W(u))\cap I_{ab}(u),\\
B_u&=(I_b(u)\setminus(I_W(u)\cup I_a(u)))\cap I_{ab}(u),\\
C_u&=I_{ab}(u)\setminus(I_W(u)\cup I_a(u)\cup I_b(u)).
\end{aligned}
\]

Thus `K` includes an old occurrence tuple even when a move transports it to
new physical positions; `A,B` are marginally new occurrence tuples, and `C`
are genuinely joint new-seam witnesses.  Hence upper completeness is
exactly

\[
 K_u\cup A_u\cup B_u\cup C_u\ne\varnothing
 \quad\hbox{for every upper }u.                     \tag{2.2}
\]

Marginal debt cancellation is not enough: the advertised witnesses must
coexist in one bijective occurrence order.

For every target row `r` and target bit `j`, let `p_X(r,j)` indicate whether
the compiler envelopes covering row `r` reproduce bit `j`.  Then

\[
 p_{ab}=p_0+(p_a-p_0)+(p_b-p_0)
          +(p_{ab}-p_a-p_b+p_0).                    \tag{2.3}
\]

The last term is the literal interaction correction.  With disjoint
dependency closures it vanishes; otherwise it must be replayed.  Valid flats,
nonzero maximal envelopes, capacity, and every row equation are separate
requirements.

Finally fix a maximum matching `M` of `G_W`.  If every edge of `M` survives
in `G_ab`, then the two-provider condition is

\[
 \rho_M(G_{ab})\ge2,                                \tag{2.4}
\]

where `rho_M` is the maximum number of vertex-disjoint `M`-augmenting paths.
Equivalently, `G_ab` has a matching of size at least 26,309.  Sufficiency
follows by flipping both paths; necessity follows by decomposing the symmetric
difference of `M` with a larger matching.  If an old matching edge is lost,
the path shortcut is invalid and the full graph must be rematched.

Combining (2.2)--(2.4) gives the fail-closed order:

```text
occurrence bijection and exact middle
-> two independent lower augmentations / matching >=26309
-> every unrestricted upper mask witnessed.
```

## 3. Alpha and the 176 upper-side signatures

Alpha swaps, without reversal,

```text
[6608,6611) <-> [12714,12717).
```

It preserves the depth schedule, exact middle replay, capacity 32,063, and
nonzero envelopes.  It creates the unique incidence

```text
4e70 -- source cell (12714,12715),
```

which completes the audited seven-edge augmenting path and changes Hall
deficiency `25 -> 24`.  Its sole upper debt is `4e79`.

Since every row has rank eight, a minimal interval witnessing the rank-nine
mask `4e79` is precisely an adjacent pair of distinct rank-eight facets of
`4e79`.  Alpha has ten physical facet occurrences with nine distinct values,
so there are

\[
 10\cdot9-2=88                                      \tag{3.1}
\]

directed distinct-facet seams that a compensator may create.

Alpha has four new occurrence seams, at cuts after positions

```text
6607 6610 12713 12716.
```

They support 44 new endpoint-minimal intervals on 24 distinct masks.  Only
two of those masks had a unique minimal witness in exact229:

```text
ce78: old [6607,6609), alpha replacement sources (6607,12714);
ce2e: old [6610,6612), alpha replacement sources (6610,12717).
```

The smallest new-seam reciprocal upper catalogue therefore has

\[
 2\cdot88=176                                      \tag{3.2}
\]

signature rows.  Of them, 140 do not use an alpha augmenting-path source row
as one of the proposed `4e79` facets.  That 140 count is only a source filter,
not a Hall certificate.

The strengthened two-provider gate changes the interpretation of this table:
all 176 are **raw upper-side obligations**, and none is a certified candidate
until it also supplies

1. a lower target different from `4e70`;
2. a second augmenting path independent of alpha's path; and
3. a final literal matching of at least 26,309.

The catalogue therefore records `two_provider_eligible=0` for all 176 current
rows.  This is not a 176-row no-go: no physical beta word or provider was part
of those abstract seam/debt rows.

Separately, the complete elementary direct-return class—every one-facet
relocation and endpoint-determined interval reversal joining two physical
`4e79` facets—has 241 distinct words.  Only four remain middle-exact and
zero-free; none is upper-complete.  Hence that scoped class contributes no
two-provider candidate.

## 4. The known marginal two-provider pair is incompatible

There is one particularly sharp partner beta.  Starting from exact229, first
make the neutral swap

```text
[6611,6614) <-> [12717,12720),
```

then swap, without reversal,

```text
[6608,6622) <-> [12715,12729).
```

The result is

```text
scratch/defect_transport_sparse_bad2_20260730/
  pass1_hallswap16/hit_14.targets
SHA-256 9f78f5ac6bd0348d9309985884ec55c5825dfe1921a71b8f2d47494809910536.
```

Beta is middle-exact, has the same flats and capacity, and has sole upper debt
`4e7e`.  Its unique provider for a formerly zero target is the length-one cell

```text
8000 -- cell 31755 = physical [12717,12718), source row 6610.
```

Adding only the `8000` provider edge to beta's neutral precursor `R` raises
its matching from 26,307 to 26,308.  Relative to the deterministic `R`
matching, the shortest displayed augmenting path has three edges; the full
`R`/beta matching exchange has seven.  Alpha's and beta's new provider
targets and cells are distinct, and their marginal path vertices are
disjoint, but the paths are certified relative to different precursor
matchings.  This is **not** a common-base rank-two certificate: any surviving
literal composition would still need the full condition (2.4), or a full
rematch.

Their advertised upper repairs also look reciprocal:

```text
alpha transports 4e7e on [6608,6611), sources (12714,12715,12716);
beta retains    4e79 on [12713,12715), sources (12713,12714).
```

But both fixed witnesses require the single occurrence label `12714` at two
different physical positions.  They cannot coexist in one occurrence
bijection while retaining the advertised provider profiles.  Literal replay
of both position-defined composition orders confirms the obstruction:

| order | bad middle rows | upper holes |
|---|---|---|
| alpha then beta | `6607,6608,12714,12715` | `4e79,ce3c` |
| beta then alpha | `12714..12718` | `4e79,4e7e,ca6e,ca6f,cc3e` |

Both orders fail before a final Hall call.  This rejects only these two fixed
compositions and their advertised witnesses.  A wider braid creating a
different `4e79` witness or different provider paths remains open.

## 5. Reproducibility and exact scope

The light exact reproducer is

```text
scratch/audit_k16_exact229_hall24_two_trade_join_20260730.py
SHA-256 718bce77bd62844bda2ba7b8756fdbb053a79729be7737f27533057b4eedff8e.
```

It writes

```text
scratch/k16_exact229_hall24_two_trade_join_20260730.audit.json
SHA-256 5a0a3c56dd4c70e4c1b0aa2f8dcc91fb0275e673219e8105b967462cd1ab6f17
payload 6bb434946be7a5ce0b99447d647355f9f44b8cce6cd38517699bdec9e421f688;

scratch/k16_exact229_hall24_two_trade_join_20260730.catalogue.tsv
SHA-256 ef99de5486bff05d63131a562cb32dfeb2ab3e26e7b1a2d930f04b1e6ebfb489.
```

The beta Hall artifact is

```text
scratch/defect_transport_sparse_bad2_20260730/
  pass1_hallswap16/hit_14.hall.json
SHA-256 61e5dba14486b4a177328079420354a9e2fce1ee66a17f68ff95bf5b35c824f9
payload 756c06e2050ffc9104e16b1fb411595e6219a73aa7fa506d60148843c209457c.
```

The standalone independent beta/composition replay is

```text
scratch/audit_k16_exact229_hit14_tradeB_occurrence_composition_independent_20260730.py
SHA-256 34d6ef4af573d20c89d2d9316fe7c2fb0b0af891b9329d6d73a4b96380f01019;

scratch/k16_exact229_hit14_tradeB_occurrence_composition_independent_20260730.audit.json
SHA-256 34d5711a0e959936cbd16292697a1a32695a9cdf948c6b17de14ce8dd80c9193
payload 2ecf6dfe91989cfdcf499c12cdcc3ed1e97d1d0ea989164daaa95002b9caadb4.
```

The reproducer authenticates all inputs, reconstructs both occurrence
permutations, replays exact middle and all upper masks, rebuilds zero-provider
sets, checks the stored matchings, regenerates the 176-row TSV, and replays
both rejected compounds.  It performs no SAT solve and launches no H100 job.

The conclusion is scoped to the exact229 chronology, the declared alpha and
beta moves, the 176 new-seam reciprocal signatures, and the 241 elementary
direct-return moves.  It does not close other transported old witnesses,
larger cycles, unequal packets, alternative upper witnesses, or unrestricted
K16 equality.
