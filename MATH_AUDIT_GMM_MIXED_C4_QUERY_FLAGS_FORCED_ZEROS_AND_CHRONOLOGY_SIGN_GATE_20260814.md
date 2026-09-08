# Hostile audit of the GMM mixed-C4 query-flow and chronology gate

**Date:** 2026-08-14  
**Verdict:** **PASS, with the stated reduction-only scope.**

Audited source:

`MATH_REDUCTION_GMM_MIXED_C4_QUERY_FLAGS_FORCED_ZEROS_AND_CHRONOLOGY_SIGN_GATE_20260814.md`

H100 SHA-256:

```text
f3eddf3ea4ab9309c55ebb8694f9a30b8487d1e8f82783856f237be20d77d72a
```

## 1. Incidence audit

For a source query `q=(B;b,p,a)`, the identities

```text
P = B-b+p,
P+b = B+p,
P+a = B-b+p+a
```

give exactly the two negative selected edges in the mixed-C4 packet.  Thus
the continuation count is

```text
deg_(H_P)(a) - 1[{a,b} is an edge of H_P],
```

and grouping it proves the displayed flag decomposition.  The query count
has the factors two edge orientations, `m-1` choices of `b`, and
`sum_(d(B)>0) ell_B=D+|supp d|`; no unordered/ordered factor is missing.

The stronger owner-fibre identity also passes.  For fixed `(P,c)`, every
query is a distinct selected incidence

```text
P+c -- P-p+c+a
```

at the one owner `P+c`, and conversely every surplus-coloured incidence
there whose lower colour is not `P` yields exactly one such query.  The
remaining capacity is therefore exactly `2-deg_(H_P)(c)`.  Summing these
capacities over all fibres gives `2(m-1)W`, so the source correctly states
that the unstructured scalar double count reduces to the tautological
inclusion of surplus-coloured selected edges among all selected edges.

## 2. Zero-occurrence audit

Every bracket in the occurrence sum is nonnegative.  At target degree two
it is at least `mu(P,a)`; at a leaf it vanishes only when every query uses
the unique neighbour as its exceptional label.  Such an aligned leaf query
and its continuation share owner `P+c`, so only one source incidence is
available after the leaf edge.  At an isolated flag, summing the exact
owner-fibre capacities over the `m+1` possible exceptional labels gives
`mu(P,a)<=2(m+1-ell_P)`.

For fixed surplus `B`, the target flag recovers `b`, `p`, and `a`, hence the
query-to-flag map is injective.  The total leaf-exception budget is
`sum_p(2-deg_(H_B)(p))=2c_B` over the nontrivial path components.  Therefore
the forced-zero count

```text
2((m-1)ell_B-c_B) >= 2(m-2)ell_B
```

is exact.  The equivalent owner-local statement was also checked: the only
possible leaf exception is literally the second selected incidence at that
owner, and it must have the same entering label.

## 3. Chronology audit

In packet order `1,2,3,4`, the old matching is `12,34` and the proposed new
matching is `23,41`.  After orienting the Hamilton cycle, equal old-edge
directions close the two retained paths separately, while opposite
directions join them into one cycle.  Hence the legal sign is exactly

```text
epsilon_B(p,a) epsilon_P(a,c) = -1.
```

If either positive edge were already selected, the four ports would occur
as one local three-edge path and the two old signs would agree.  Thus
opposite signs also imply the two positive edges are absent.  The relation-
component reformulation follows immediately: zero legal moves means every
relation edge joins equal signs.

## 4. Finite near-obstruction replay

The compact `m=4` certificate was replayed independently on H100 with:

```text
scratch/verify_gmm_mixed_c4_zero_twofactor_certificate_20260814.py
SHA-256 fd97f188852ab2f25630bef4c736261fbc5593504fb2bb93c603b380f4fb5ed3
```

Exact output:

```text
PASS m=4 vertices=126 components=21 lengths=3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,5,5,8,14,44 lower_colours=84 surplus_mass=42 A_occ=0 colour_cycle_defects=2 point_surplus=13,14,13,13,14,18,16,14,11 cross_component_johnson_reconnections=335 lower_complete_reconnections=165 zero_occ_reconnections=0
```

Output SHA-256:

```text
ef28c2f042f71f672a74e041b8f1390adf33f48f5f1b6b6405165231a273b52b
```

The checker verifies every Johnson edge, degree-two coverage of all 126
owners, all 84 lower colours, surplus mass 42, zero mixed occurrence count,
the exact two monochromatic triangle defects, the point-surplus vector, and
all 335 cross-component Johnson reconnections (165 lower-complete, none
remaining in the zero-occurrence fibre).

## 5. Scope boundary

The source does **not** prove an all-`m` positive outgoing-move theorem.
The finite certificate is a disconnected two-factor and its two cyclic
lower-colour defects violate the path-forest consequence of Hamiltonicity.
What is frozen is the exact owner-fibre/forced-zero cut and the independent
chronology sign gate.  A positive theorem still has to use the placement of
isolated flags together with global one-cycle connectivity; neither total
capacity nor the finite near-obstruction resolves that gate.
