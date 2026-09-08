# K17 planted `B_5`: selected-token address transport and the exact source-history gate

**Date:** 2026-08-02  
**Status:** exact finite audit and typed transport theorem.  The represented
`3,495` selected real-token-to-receiver edges are pointwise common across
`b268` and both planted-module modes.  The apparent ten-token failure is a
token-label/physical-row type collision.  If a later aggregate history also
exports the whole state of the same-number token-source row, ten source-row
states still require an explicit equivariant replay.  No aggregate-history,
reset, residence, supplier, compiler, selected `z=6` witness, or bound on
`nu(k)` is proved here.

## 0. Outcome

There are three different objects whose integer labels had been conflated.

1. A real token label `u` denotes the immutable bottom payload

   \[
                              b(u)=O[u].\mathrm{low},             \tag{0.1}
   \]

   where `O=original.res1972.tsv`.
2. Its actual materialized occurrence address is the receiver row `h` in
   the certified outer edge `M_out(u)=h`.
3. The physical row whose numerical ID also equals `u` is a different
   object.  After materialization it normally carries another token.

Only `572/3,495` selected tokens occupy their same-number row even in the
authenticated `b268` parent.  By contrast, every one of the `3,495` selected
real edges satisfies

\[
 B[h].\mathrm{low}=T^0[h].\mathrm{low}=T^1[h].\mathrm{low}=b(u),          \tag{0.2}
\]

where `B` is `b268` and `T^0,T^1` are the two planted-module modes.  Thus
the selected token identity, payload, and receiver address are fixed
pointwise.

Exactly ten selected token **labels** also happen to be IDs of physical rows
changed by the ambient `b268 -> T^0` rethread.  Following the old lower target
from row `u` to its new row gives the supplied ten-map, but that map follows
the unrelated token currently occupying row `u`; it does not transport token
`u`.  Replacing the ticket field `u` by that destination is invalid.

The exact remaining distinction is therefore:

* the represented token/receiver layer is **PROVED** common; and
* any optional relation attaching a token label to the complete current
  state of physical row `u` is a separate source-history layer and remains
  **UNPROVED** unless it factors through (0.1)--(0.2) or admits the explicit
  address transports below.

## 1. Frozen semantics

The authenticated files are

```text
origin                 original.res1972.tsv
selected tickets       selected_tickets.tsv
outer matching         complete_outer_matching.tsv
materialized parent    private_h_outer_materialized.tsv
planted mode zero      constructed_common_basis_b5_host.tsv
```

The outer verifier defines the real-token shore from hard rows of the
**origin** table.  Its matching check is literally

\[
  \mathrm{payload}(u)=O[u].\mathrm{low},\qquad M_{out}(u)=h,              \tag{1.1}
\]

and a selected ticket requires its named edge `(u,h)` to occur in that
matching.  The independent planted-host replay likewise computes the
expected endpoint bottom from `O[u].low` and checks it at row `h`.  Neither
verifier requires `u=h` or requires the current materialized row `u` to carry
`O[u].low`.

### Theorem 1.1 (pointwise selected token/receiver transport)

All `3,495` real token edges named by the `1,748` selected tickets occur
pointwise in `B`, `T^0`, and `T^1` with the same token label, payload, and
receiver row.  In particular, the planted `B_5` phase change causes zero
selected lower-token/address damage.

#### Proof

The selected edges are pairwise token-injective and are present in the
authenticated outer matching.  Their receiver rows are among the `5,244`
selected short/predecessor/successor-host rows frozen by the planted-host
construction.  The 22 module rows are disjoint from this frozen row set, so
the alternate local mode also fixes every receiver row.  Direct replay gives
(0.2) for all `3,495` edges.  \(\square\)

This theorem is about the represented outer occurrence.  It does not by
itself erase a separately exported source-row or history relation.

## 2. The ten row aliases

The exact affected records are below.  Ordinals are zero-based; `line` is
the physical TSV line including the header.

| ordinal | line | side | token `u` | row readdress `rho(u)` | payload `b(u)` | actual receiver `h` |
|---:|---:|:---:|---:|---:|---:|---:|
| 20 | 22 | pred | 15467 | 15469 | 75408 | 15470 |
| 255 | 257 | succ | 15219 | 14967 | 75811 | 15049 |
| 292 | 294 | succ | 15026 | 14757 | 74096 | 14760 |
| 466 | 468 | succ | 15469 | 15035 | 75396 | 14959 |
| 595 | 597 | succ | 16083 | 16091 | 72080 | 14220 |
| 637 | 639 | succ | 15340 | 15214 | 68753 | 14437 |
| 841 | 843 | pred | 16012 | 16034 | 71809 | 16027 |
| 1181 | 1183 | pred | 15411 | 14903 | 74113 | 14650 |
| 1368 | 1370 | pred | 15531 | 15611 | 77825 | 16239 |
| 1721 | 1723 | succ | 15822 | 15818 | 79040 | 15819 |

For every line in the table,

\[
               B[u].\mathrm{low}=T^0[\rho(u)].\mathrm{low}.              \tag{2.1}
\]

Equation (2.1), not `b(rho(u))=b(u)`, is what the supplied map certifies.
For example,

```text
token 15026:  b(15026)=74096, actual receiver=14760;
row transport: B[15026].low=74352=T0[14757].low;
token 14757:  b(14757)=73776.
```

The real-token payloads in the origin hard shore are distinct.  Hence a
payload-preserving token relabelling `u -> v` forces `v=u`.  Replacing the ten
ticket fields by `rho(u)` has the following exact audit:

```text
rewritten records                         10
endpoint containment still legal           1
rewritten record in retained witness bank   0
```

Thus the ten-map cannot be used as a ticket-token relabelling.  It is only a
row-location transport for a different relation.

## 3. Exact lower-location transport squares

Let `L` be the common set of all `21,777` targets of rank at most six.  For
`x in L`, let

\[
 \mu_B(x),\quad\mu_0(x),\quad\mu_1(x)                                  \tag{3.1}
\]

be the unique physical row containing `x` in `B,T^0,T^1`, respectively.

### Theorem 3.1 (ambient value-following transport)

The row permutation

\[
                         \rho=\mu_0\mu_B^{-1}                             \tag{3.2}
\]

satisfies

\[
                         \rho\mu_B=\mu_0                                 \tag{3.3}
\]

on every `x in L`.  It has support `134` and seven nontrivial cycles of
lengths

\[
                         7,8,13,14,18,36,38.                              \tag{3.4}
\]

For every selected token edge `(u,h)`,

\[
                    \mu_B(b(u))=\mu_0(b(u))=h,\qquad \rho(h)=h.           \tag{3.5}
\]

#### Proof

Each table contains every member of `L` exactly once, so (3.2) is a
permutation and (3.3) is definitional.  Direct cycle decomposition gives
(3.4).  Equation (0.2) gives (3.5).  \(\square\)

The complete nontrivial cycle list, in old-location to new-location
orientation, is

```text
(57 14644 15079 13200 15801 16218 1058)
(13391 15155 15100 15060 16011 16083 16091 14369)
(5761 5950 16232 14441 15365 15400 14878 14898 12992 12874 15540 16012 16034)
(581 15605 16078 16077 2636 15078 15351 15369 15404 15026 14757 14630 14645 12902)
(12957 15534 15606 13672 12974 14765 15144 14636 14818 15339 16227 14422 13512 13046 13900 15799 15541 13662)
(90 14696 15612 15531 15611 16018 14125 879 14897 15346 15219 14967 18259 15150 15076 15141 15280 15289 14640 1928 15149 16087 14365 13651 13176 14772 1377 1381 14826 15340 15214 15467 15469 15035 14766 12871)
(64 14820 15808 15810 15812 15879 14115 13855 13721 14589 14891 15406 13466 13474 14887 14892 14616 13139 15143 15411 14903 14829 15804 15820 15822 15818 13878 2199 5930 2849 1073 305 326 656 671 626 2313 2327)
```

### Theorem 3.2 (local `B_5` phase transport)

The token-gauge row permutation

\[
                         \kappa=\mu_1\mu_0^{-1}                            \tag{3.6}
\]

satisfies `kappa mu_0=mu_1` and has exactly the two cycles

\[
 (15351\ 16083\ 16227\ 15411\ 16087),\qquad
 (2849\ 16218\ 16232).                                                    \tag{3.7}
\]

Equivalently, in physical-root gauge define

\[
             \alpha_{root}(x)=T^1[\mu_0(x)].\mathrm{low}.                 \tag{3.8}
\]

Then

\[
                         \mu_1\alpha_{root}=\mu_0,                        \tag{3.9}
\]

which is `beta mu_0=mu_1 alpha_root` with `beta=id`.  Its support has eight
lower values and it fixes every selected payload `b(u)`.

#### Proof

The coefficient-one equality of the old and new lower decks makes both
maps permutations.  Direct substitution gives (3.6) and (3.9).  The eight
changed module rows yield (3.7).  Since every selected payload is at a
frozen receiver outside the module, both gauges fix its selected occurrence.
\(\square\)

Only two selected token **numbers**, `15411` and `16083`, lie in the eight
changed physical rows.  The forced physical-root seed transports their
typed row fields as follows:

| row | upper | fixed head | old lower -> new lower | old tail -> new tail |
|---:|---:|---:|:---|:---|
| 15411 | 77201 | 77185 | 76161 -> 76929 | 76177 -> 76945 |
| 16083 | 80273 | 80017 | 80001 -> 75921 | 80257 -> 76177 |

These are source-row decorations, not the payloads of selected tokens
`15411` and `16083`; their actual payloads remain at receiver rows `14650`
and `14220`.

## 4. The exact source-history dichotomy

Suppose a stronger carried signature contains an additional relation
`Src(u,r)` tying token label `u` to a current physical source-row state.
The frozen ticket and outer-matching artifacts do not define this relation.
Three cases must be distinguished.

1. **Receiver-factorized history.**  If every history consumer of the token
   factors through `(u,b(u),h)` and the state at receiver `h`, Theorem 1.1
   transports the complete token/address substructure by identity.
2. **Literal same-number source state.**  If the complete tuple at physical
   row `u` is exported through an injective frozen decoder, literal replay
   fails on exactly ten source occurrences.  The exact counts are

   | comparison | equal source rows | full literal tickets |
   |:---|---:|---:|
   | `B -> T^0` | 3485 / 3495 | 1738 / 1748 |
   | `B -> T^1` | 3485 / 3495 | 1738 / 1748 |
   | `T^0 -> T^1` | 3493 / 3495 | 1746 / 1748 |

   In the last line the typed physical-root seed repairs the two row-field
   changes only if that decoder is declared equivariant under the seed; raw
   literal equality still fails.
3. **Value-following source address.**  If `Src` follows the physical
   location of a lower value, then its forced ambient action is `rho`.  The
   ten row aliases meet five `rho`-cycles of lengths `8,13,14,36,38`, whose
   union has `109` rows.  If the **complete bijective location relation**
   (including its inverse) is exported, closure therefore carries all 109
   rows.  If only one selected certificate carries ten address objects,
   full orbit closure is not automatic: it is enough that their ten images
   are unused or compatibly transported and that every selected relation is
   preserved.  The ten images are distinct and avoid both the 5,244 frozen
   rows and all 22 module rows, but their history/capacity use is not
   represented.

Thus `109` is a sharp full-location-bijection closure count, not an automatic
sidecar charge for the weaker selected-certificate problem.

## 5. Precise replay criterion

Let `D_B(w),D_0(w_0),D_1(w_1)` be the recursively used selected dependency
closures, with the mutable B5 topology predicate omitted but every exported
equality, address, history, reset, residence and capacity relation retained.
At the token/source boundary, a proof-safe transport exists exactly when
there are sort-preserving maps which:

1. fix every selected token label `u`, payload `b(u)`, receiver `h`, and
   forced outer edge `(u,h)` as in Theorem 1.1;
2. extend either the token-gauge equations (3.3),(3.6) or the compatible
   physical-root seed (3.9) on every lower/tail occurrence actually used;
3. if `Src` is exported, carry its used source-row objects under the chosen
   gauge, preserve every relation incident to them, and remain injective on
   all used physical addresses and capacity-one cells; and
4. fix the declared exterior pointwise.

Necessity is restriction of any selected-certificate isomorphism.  Conversely
these maps glue precisely when they agree on overlaps and have disjoint
images off overlaps; then they transport the complete selected token/source
substructure.  This is a criterion, not an existence proof for the aggregate
history closure.

The smallest remaining hypothesis is therefore exact:

> Aggregate histories either factor through the certified receiver
> occurrence `(u,b(u),h)`, or admit one exterior-fixed equivariant extension
> of `rho` for the ambient planting and of the forced physical-root seed (or
> `kappa`) for the local phase on every used source-row dependency.

## 6. Proof status

The following are **PROVED** on the frozen K17 artifacts.

1. The ten supplied readdresses are row-location moves, not token moves.
2. All `3,495` selected token identities, payloads, receiver addresses and
   forced outer edges are pointwise common across `B,T^0,T^1`.
3. The exact ambient and local transport-square equations, cycle lists and
   supports in Section 3.
4. Token relabelling by the ten-map is invalid: nine rewritten endpoints
   fail containment and none of the ten rewritten records belongs to the
   retained witness bank.
5. Literal optional source-row equality and full-ticket counts in Section 4.

The following remain **UNPROVED**.

1. Whether the selected aggregate history actually exports `Src` and, if
   so, which address gauge it uses.
2. An exterior-fixed history/reset/residence/supplier/compiler isomorphism
   extending the exact token-layer maps.
3. A phase-specific selected occurrence witness at `z=6` and hence
   `6 in A^sel_(16,2)`.
4. A clone-good regenerative bank, an all-`k` theorem, or any new bound on
   `nu(k)`.

## 7. Audit binding

```text
scratch/audit_k17_b5_selected_token_address_transport_20260802.py
  SHA-256 51749eeccfb084472272feb8057fd11d1335e64b0d5e74a720d207d25db9eeca

scratch/k17_common_basis_b5_protected_host_20260802/
  selected_token_address_transport.audit.json
  SHA-256 6be85e48a24e6a6199cf141817efba61bbf4c6eaa2345cb9a557aef2ec79e8e0
```

The audit independently reconstructs the alternate B5 mode from the
published coordinate data, verifies every selected outer edge, computes
both lower-location permutations and the physical-root value action, checks
the ten invalid rewrites against the retained witness file, and emits every
scope limitation above.
