# Typed suffix candidate lists: a verifiable private-router theorem

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sufficient theorem.  It derives
the missing simultaneous typed suffix linkage from explicit candidate-path
lists and conflict budgets.  It does not assert that the current parent or
reference matching supplies those lists.

Fix one materialized cap/guard/phase/occurrence state.  Delete the physical
capacities used by one fixed compensation linkage and every interior vertex
of the selected claim-to-port prefixes **as well as every claim start**
(equivalently, delete every prefix vertex other than its terminal port).
Let `D` be the resulting
node-split unit-capacity directed network, `T` its unused typed sink bank,
and

\[
                         P=\{p_1,\ldots,p_m\}
\]

the active physical occurrence-labelled ports.

For every port `p_i`, let `C_i` be a finite nonempty family of literal
directed paths

\[
                         R:p_i\leadsto t(R),
 \qquad t(R)\in T,
\]

such that every `R in C_i` has a terminal type legal for every gain
incident with `p_i`.  Two candidates conflict when they share a physical
unit-capacity vertex (equivalently, a physical capacity) or have the same
sink occurrence.  Unlimited-capacity bookkeeping vertices, if any, are
first split or suppressed and do not count as physical linkage resources.

For `j<i`, put

\[
 \Delta_{ji}=max_{R\in C_j}
       |\{S\in C_i:S\text{ conflicts with }R\}|.
\tag{0.1}
\]

## Theorem 1 (ordered list-conflict router)

If the ports can be ordered so that

\[
                         \boxed{
 |C_i|>\sum_{j<i}\Delta_{ji}
 \quad(1\le i\le m),}
\tag{1.1}
\]

then there are candidates `R_i in C_i` which are pairwise
vertex-disjoint and end at distinct typed sinks.  Consequently

\[
 r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|.
\tag{1.2}
\]

### Proof

Choose the candidates in the displayed order.  After
`R_1,...,R_(i-1)` have been chosen, candidate `R_j` forbids at most
`Delta_(ji)` members of `C_i`.  Hence their union forbids at most

\[
                         \sum_{j<i}\Delta_{ji}<|C_i|
\]

candidates.  Choose an unforbidden `R_i`.  Induction produces one
candidate from every list with no shared physical capacity and no repeated
sink.  These paths are a linkage of the full port set, which is exactly
(1.2). \(\square\)

### Uniform corollary

If every list has size at least `L` and every candidate conflicts with at
most `Delta` candidates in each other list, then

\[
                         L>(m-1)\Delta
\tag{1.3}
\]

is sufficient.  More generally, (1.1) retains nonuniform list sizes and
directional conflict counts, so it is the sharper directly checkable form.

## 2. Composition with a regular incidence factor

Let `B=(G,P;E)` be a left-`h`-regular/right-at-most-`h` incidence factor.
Assume every incidence `gp` has a literal claim-to-port prefix in the same
materialized state.  Assume the prefixes have the privacy required by the
regular-factor theorem: distinct prefixes share no physical capacity except
that prefixes of one gain may share that gain's start and prefixes ending at
one port may share that port.  Assume also that the candidate lists above
were formed only after deleting the fixed compensation linkage and every
prefix vertex other than its terminal port.

### Theorem 2

Under (1.1), every gain in `G` links to a distinct legal sink in the same
materialized state.

### Proof

Theorem 1 supplies one simultaneous private suffix for every active port.
Give every incidence-prefix/port-suffix concatenation weight `1/h`.
Every gain emits one unit, while port `p` and its suffix carry

\[
                         {\deg_B(p)\over h}\le1.
\]

Private prefix interiors carry at most `1/h`.  This is a value-`|G|`
fractional flow in an integral unit-capacity network.  Integral max flow
therefore gives one disjoint legal path from every gain to a distinct
sink. \(\square\)

## 3. One-step Boolean specialization

Suppose each candidate is a typed one-step Boolean extension followed by
a private sink edge.  If every port retains at least `L` candidate upper
occurrences and any fixed candidate at one port conflicts with at most
`mu` candidates in another port list, then

\[
                         L>(m-1)\mu
\tag{3.1}
\]

certifies the full literal suffix router.  In the clean distinct-port
Boolean face, two extension neighbourhoods meet in at most one upper
value.  If each list has at most one candidate over each such upper value
and the candidate-to-sink occurrences are globally injective, this gives
`mu<=1`, so `L>=m` suffices.

This is a capacity-faithful certificate: the candidate paths themselves,
their physical addresses, types, and sink occurrences are the input.  It
does not infer a router from an abstract factor, marginal matching, or
individual port reachability.

## 4. Exact boundary and scope

Condition (1.1) is sufficient, not necessary.  If it fails, the exact
remaining certificate is still the full typed suffix rank or an equivalent
direct max-flow certificate.  A common unit suffix bottleneck can satisfy
every individual-list nonemptiness condition while having rank one; hence
nonempty menus alone cannot replace (1.1).

The theorem closes the router whenever a distributed low-conflict
candidate atlas is exhibited.  It does **not** prove that the current
parent/reference matching has such an atlas, does not authenticate
transported phase one, and does not prove an all-`k` carrier or
`nu(k)<=B(k)+O(1)`.

## 5. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| conditional regular-factor/private-router composition | `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md` | `2d64e2cb36b65706133ae1e68c6bdda80d433ccd428259860382a301538096d0` |
| exact factor-restricted gammoid boundary | `MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md` | `09acd8673956a2e43ec97d1d67ff01d4e3ceb1ea230af0e796a762b84d142906` |
| independent current-byte factor-router audit | `MATH_AUDIT_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_INDEPENDENT_20260804.md` | `e9aed2a8806eaa47dcc3c6f01b207f656f0d6a0f7517a010a98172f54cf7525c` |
