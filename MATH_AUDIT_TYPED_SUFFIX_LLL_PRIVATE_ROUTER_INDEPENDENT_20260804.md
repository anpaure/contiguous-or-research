# Independent audit: typed suffix Haxell/LLL private-router specialization

**Date:** 2026-08-04  
**Verdict:** **GO after proof-safety corrections.**  The standard
independent-transversal input, the self-contained local-lemma fallback, the
typed-linkage interpretation, and the regular-factor flow composition are
correct under the literal fixed-state hypotheses now stated in the theorem.
The result is a sufficient router certificate only; it does not construct
the candidate atlas and does not prove an all-dimensional carrier or
`nu(k)<=B(k)+O(1)`.

## 1. Audited source and dependencies

| role | file | SHA-256 |
|---|---|---|
| audited theorem | `MATH_THEOREM_TYPED_SUFFIX_LLL_PRIVATE_ROUTER_20260804.md` | `2d3b24f7dc0ad85147593f3a6f65bebc95f28d5c1ad1c1179bf0257891fdd6f9` |
| prior Haxell/LLL packet selector | `MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md` | `35ae0a3cdc827bc5365d6c2e6f0cfb11ff3123f74bbca624cf3d3fa611af5f2a` |
| fixed-state factor/router composition | `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md` | `2d64e2cb36b65706133ae1e68c6bdda80d433ccd428259860382a301538096d0` |

The selector itself is not new here.  Haxell's independent-transversal
theorem gives the primary threshold `L>=2 Delta`; the typed suffix and
factor-flow specialization is the content of the audited file.

## 2. Independent-transversal check

Let `H` be the simple multipartite graph whose parts are the nonempty lists
`C_i`, and whose cross-part edges are exactly the literal suffix conflicts.
Its maximum degree is `Delta` and every part has size at least `L`.

Under `L>=2 Delta`, Haxell applies directly to the unequal original parts
and produces an independent transversal.  Equality is allowed.  When
`Delta=0`, nonemptiness of every part makes the conclusion immediate.  The
source was corrected to state `M>=1` and list nonemptiness explicitly; without
that correction an empty list would have made the old `Delta=0` sentence
false.

The physical conclusion is exact because conflict includes every residual
unit-capacity resource and equality of sink occurrence.  Pairwise
nonconflict therefore means that the selected literal paths are globally
vertex/capacity-disjoint and terminate at distinct physical sink
occurrences.  This implication uses the fixed-atlas hypothesis.  A
candidate-dependent rematerialization or a genuinely higher-order
acceptance constraint is not represented by `H` and is explicitly excluded.

## 3. Local-lemma dependency count

For the fallback proof, truncate every part to the minimum size `L`.
Deletion cannot increase maximum degree.  If `xy` is a conflict edge, the
event selecting both endpoints has probability

\[
                              p=L^{-2}.
\]

A fixed part contains `L` vertices, each of degree at most `Delta`, so at
most `L Delta` bad events mention that part.  An event using parts `i,j`
can depend only on events mentioning `i` or `j`.  The event itself is counted
in both part totals.  Hence the number of *other* dependent events is at
most

\[
 (L\Delta)+(L\Delta)-1-1=2L\Delta-2.
\]

Thus, with `D<=2L Delta-2`,

\[
 ep(D+1)
 \le {e(2L\Delta-1)\over L^2}
 < {2e\Delta\over L}
 \le1
\]

under `L>=2e Delta`.  The symmetric Lovasz local lemma is therefore applied
correctly.  No hidden factor equal to the number of parts occurs: `Delta`
already counts conflicts with candidates in **all other lists combined**.

## 4. Typed/gammoid interpretation

The independent transversal is first and foremost an explicit simultaneous
typed linkage of every active physical port.  It may be written as

\[
             r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|
\]

only after terminal legality has been materialized in one fixed typed
suffix network: type-homogeneous blocks or a proved identity gadget with a
common physical capacity-one port gate.  Merely attaching an external
port-dependent legality predicate does not define an ordinary untyped strict
gammoid.  This caveat is now explicit in the theorem.

The audit also checked the physical conflict boundary.  Sharing a Boolean
value is irrelevant unless it aliases one physical capacity; conversely,
every shared physical vertex/capacity and every repeated sink occurrence
must be an edge of `H`.  Any additional global cap, witness, topology, or
identity condition must be encoded by capacities/pairwise conflicts or
proved separately before the theorem is invoked.

## 5. Regular-factor composition

Let `B=(G,P;E)` have left degree exactly `h`, right degree at most `h`, and
`P=N_B(G)`.  Under the corrected hypotheses:

1. every incidence prefix lies in the network residual to the fixed
   compensation linkage;
2. prefix interiors are private, except for the priced common claim starts
   and common terminal ports;
3. selected suffixes avoid every prefix except at their own terminal port;
4. all objects coexist in one materialized occurrence state; and
5. each selected port suffix ends in a type legal for every adjacent gain.

Send `1/h` along every incidence-prefix/selected-suffix concatenation.  The
loads are exactly:

\[
 \operatorname{load}(s_g)=1,
 \qquad
 \operatorname{load}(\text{private prefix interior})=1/h,
 \qquad
 \operatorname{load}(p)=
 \operatorname{load}(R_p)={\deg_B(p)\over h}\le1.
\]

Distinct selected sinks have load at most one.  This is a value-`|G|`
fractional flow in the displayed integral node-split subnetwork.  Integral
max flow saturates every unit super-source-to-claim arc and yields one
capacity-disjoint path per gain to distinct sinks.  Single-commodity
rounding does not lose terminal legality because every selected suffix at a
port is legal for every gain incident with that port.  Deletion of the fixed
compensation capacities gives coexistence with that linkage.

## 6. Quantitative corollary

The original draft used `m` both for the number of active ports and for the
central-layer scale.  That collision was substantive because the relation
`d=Theta(sqrt(m))` concerns the latter, not an arbitrary port count.  The
corrected theorem writes

\[
 M=|P|,
 \qquad n=\text{central-layer scale},
 \qquad d=d(n).
\]

If

\[
 L\ge\alpha n^2,
 \qquad
 \Delta\le\beta n d(n),
\]

then Haxell is available once

\[
                         {n\over d(n)}\ge {2\beta\over\alpha},
\]

and the self-contained LLL fallback once

\[
                         {n\over d(n)}\ge {2e\beta\over\alpha}.
\]

Both hold eventually when `d(n)=Theta(sqrt(n))`.  There is no extra factor
`M`, but this statement is valid only because `Delta` is a **global**
cross-list candidate degree.  A bound `O(n d(n))` per other list would not
imply the corollary.

## 7. Corrections made during the audit

The theorem was patched to:

1. acknowledge the prior and sharper Haxell `2 Delta` selector, retaining
   the verified `2e Delta` LLL argument only as a self-contained fallback;
2. require nonempty candidate lists and distinguish `M=|P|` from the
   central scale `n`;
3. require all physical suffix conflicts and exclude unmaterialized
   higher-order constraints;
4. state the typed-network/identity-gadget premise needed for strict-gammoid
   notation; and
5. restore the full prefix/compensation privacy and type-coherence premises
   needed by the integral-flow composition.

After these corrections, no mathematical defect was found in the stated
sufficient theorem or its asymptotic consequence.
