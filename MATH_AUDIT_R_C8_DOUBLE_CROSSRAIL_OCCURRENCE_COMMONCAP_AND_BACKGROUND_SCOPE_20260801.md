# Audit of the double-crossrail occurrence, common-cap, and background scope

Date: 2026-08-01  
Verdict: `LOCAL BRIDGE VALID; INCUMBENT TRANSPORT REMAINS CONDITIONAL`  
Audited file:
`MATH_THEOREM_C8_DOUBLE_CROSSRAIL_RESIDENT_BRIDGE_AND_PHASE_ENDPOINT_CORRECTION_20260801.md`

## 1. Exact positive verdict

The dimension-uniform bridge in Sections 2--3 is literal.  For every
`d>=2`, its owner word has `2d+4` distinct rank-`r` vertices, consecutive
owners are Johnson adjacent, all `2d+3` lower colours are distinct, and its
internal run floor is `d+1`.

The source word `Q` is also one genuine source state.  Each replacement
letter in the two rails is nonempty and contained in the owner maximal
envelope `E_p`, and `D^d Q=T`.  The two rails occupy disjoint position
blocks.  Their prefix/suffix intervals give exactly `4d-4` distinct physical
cell addresses and exactly `4d-4` distinct strict-lower masks.  Consequently
both cross banks coexist literally in this one source; they are not obtained
by identifying the two authenticated endpoint phases.

They are new occurrence addresses, not typed transports of the endpoint
cells.  Bridge prefixes have width `j` and bridge suffixes width `d-j`; the
authenticated endpoint suffix carrying the same mask has width `d-j+1`.
Thus the positive statement is literal mask coverage in the bridge.  An
exact-width, phase, or address guard needs an explicit retyping rule.

There is no hidden local source-cap failure.  Put into one row family all
owner windows and all `4d-4` cross cells, with cap `E_p` at position `p`.
The displayed `Q` is contained pointwise in those caps and realizes every
row.  Therefore, with

\[
 K_p=E_p\cap\bigcap_{R:p\in J_R}S_R,
\]

every `K_p` is nonempty and every row satisfies

\[
 S_R=\bigcup_{p\in J_R}K_p.
\]

Thus the bridge has one exact local common-cap state, not merely two
marginal ray identities.

The maximal letters can be written explicitly.  They are

\[
 K_p^*=K\cup\{z,a_1,f_s\}\quad(p=d+s),\qquad
 K_p^*=K\cup\{z,a_3,f_s\}\quad(p=2d+2+s),
\]

for `1<=s<=d`, and `K_p^*=E_p` off the rails.  Therefore the exact local
lower-bound test is `L_p subseteq K_p^*`.  A phase/common lower forcing
`a_3` at a left-rail address or `a_1` at a right-rail address is an immediate
source-row failure even though both marginal banks exist.

The thirteen-component extension in Section 4 is valid only after one
literal correction now applied to the theorem: the common core `K` must be
adjoined to every upper target in (4.1)--(4.2), and hence to every auxiliary
facet.  As originally written, the claim was false whenever `K` was
nonempty.  The smallest failure is `d=2, |K|=1`: a displayed high target had
size `d+4=6` instead of `r+1=7`, and its facets had rank five instead of
`r=6`.  The original replay used `K=empty` and could not see this.  With `K`
restored, active signatures give the claimed distinct rank-`r` owners and
lower colours.  This forest still has no one concatenated source word or
exterior common cap; those remain part of protected embedding.

## 2. Matching semantics

Let `F_cross` be the `4d-4` displayed cross-cell addresses and let `U_cross`
be their target masks.  The masks are pairwise distinct: the two rails are
separated by `a_1` versus `a_3`, while within one rail a nonempty proper
filler prefix cannot equal a nonempty proper filler suffix.  Hence, in the
ordinary one-target-per-mask compiler, all vertices in `U_cross` must be
released from an incumbent target matching before the cross cells are used.

Suppose an old matching `M_0` is accompanied by an injective addressed map

\[
 \tau:\operatorname{cells}(M_0|_{L\setminus U_{cross}})
       \longrightarrow \operatorname{cells}(Q)
\]

such that every image cell has the same literal OR and passes its width,
deadline, boundary, chronology, and phase guard.  Then the retained image is
automatically disjoint from `F_cross`: a cross cell has value in `U_cross`,
whereas a retained target does not.  Therefore

\[
 \tau(M_0|_{L\setminus U_{cross}})
 \;\dot\cup\;
 \{(S,c_S):S\in U_{cross}\}
\]

is one complete literal matching.  With all of these addressed rows added
to the owner/cross row family, the same literal source `Q` proves one
simultaneous common cap.

For genuine occurrence-labelled duplicate targets, target-value separation
does not imply cell separation: the release set must contain every relevant
occurrence ID, or avoidance of `F_cross` must be checked explicitly.

## 3. What is not transported

The bridge is prospectively planted below a newly chosen owner path.  It is
not a pure refinement of an incumbent source and Sections 2--3 define no
old-to-new interval map `tau`.  Thus they do **not** transport an arbitrary
old matching.  A one-cell counterexample is immediate: put a fresh label
`g` in an incumbent singleton matching cell at a position later occupied by
the left rail.  The planted bridge contains no `g`, so that matching edge has
no image anywhere, although every owner and cross-bank assertion of the
bridge still holds.

The exact alternatives are:

1. export and prove the injective literal guard-preserving map `tau` above;
   or
2. solve a fresh residual matching in `Q` after deleting `F_cross` and
   `U_cross`.

In alternative 2, ordinary Hall is the remaining incidence gate.  Once a
literal matching is found, common-cap feasibility is automatic from the one
word `Q`; it is not a second independent Hall problem.

The word “literal” is essential.  Edgewise owner-cap admissibility is not
enough.  At `d=2`, the left rail positions are `3,4`, with cross singleton
targets

\[
 K\cup\{z,a_1,f_1\},\qquad K\cup\{z,a_1,f_2\}.
\]

Add a background row on `[3,4]` with target `K union {f_1,f_2}`.  That row
is compatible with the owner envelopes by itself, but jointly it removes
`z,a_1` from both maximal letters and destroys both cross singleton rows.
Thus an old matching/address theorem must prove the exact OR of every mapped
cell in the displayed `Q`, not just owner-cap membership or distinct cells.

The authenticated endpoint correction of Section 1 has a narrower positive
transport statement.  There an explicit full-block map exists: suffix cells
are outside its image and every image collision at a prefix address has the
released prefix target value.  This proves literal-equality,
one-vertex-per-mask cell disjointness after prefix release.  It is false for
a mere containment graph, where two distinct target supersets can use two
equal-core cells that the map merges.  It also does not by itself prove
target-shore disjointness:
every suffix mask already saturated by the old matching must also have its
old edge released.  The address map is not occurrence-injective.  Already at
`d=2`, old cells `[1,1]` and `[1,2]` have the same OR and land on one cell;
the old width-one cell also becomes width two.  Thus duplicate target
occurrences and exact-width/deadline/chronology guards require a separate
retained-edge replay.

## 4. Exact ambient cap and guard interface

For an ambient installation, export:

* the complete addressed source `Q`, owner path `T`, caps `E_p`, both rail
  blocks, `F_cross`, and target-node set `U_cross`;
* the old matching cells, release set, and either `tau` or a residual Hall
  matching;
* every target ID/value and every fixed exterior contribution;
* pointwise ambient lower bounds and caps; and
* a guard map for width/type, deadline, boundary, chronology, phase, and
  occurrence multiplicity.

Writing `P_p=E_p intersect C_p^ext` and including every outside fixed-address
row `R=(S_R,J_R,B_R)`, the complete test is

\[
 K_p=P_p\cap\bigcap_{R:p\in J_R}S_R,
\]

with `L_p subseteq K_p != empty` and

\[
 S_R=B_R\cup\bigcup_{p\in J_R}K_p
\]

for every row.  The displayed `Q` proves this criterion only for rows it
literally realizes.

The exact ambient cap condition is simply that every displayed source
letter remains below the ambient cap after all outside rows are intersected.
For example, the first left-rail endpoint position is `p=d+1` and its source
letter contains `K union {z,a_1,f_1}`.  An outside cap omitting `a_1` kills
the installation while leaving all local owner/cross identities true.  This
is the first possible source-cap failure; none occurs in the theorem's local
row family.  Dually, an ambient lower bound must lie inside the explicit
`K_p^*` above.

The authenticated endpoint banks (0.1)--(0.2) remain in different seam/
phase states.  The bridge is a new two-rail state, not a cap gluing of those
addresses.  Already at `d=2`, imposing left singleton targets
`K+za_1+f_1` and `K+za_3+f_1` at one common address leaves intersection
`K+zf_1` and reconstructs neither target.  The two rails must therefore be
address-private or connected by an explicit address pairing.

Finally, “distinct cells” means distinct interval vertices, not disjoint
source support.  For example at `d=3`, left prefixes `[4,4]` and `[4,5]`
overlap.  Any guard demanding support-disjoint packet cells fails.  Only the
two cells inside each individual ticket are adjacent and support-disjoint.

## 5. Independent replay

The existing formula replay authenticates owner, palette, residence, source
dilation, and both banks for every `2<=d<=64`, but only on `K=empty`.  A new
independent semantic replay uses `|K|=1`, adds the common-cap rows, verifies
the corrected sixteen-target forest, proves target/address distinctness,
checks fresh-background disjointness after release, and records the sharp
arbitrary-incumbent and ambient-cap controls:

```text
scratch/audit_r_c8_double_crossrail_commoncap_background_scope_20260801.py
scratch/r_c8_double_crossrail_commoncap_background_scope_20260801.audit.json
```

No conclusion about a spanning carrier, exterior compiler transport,
thirteen-component source concatenation, or regeneration follows.

Authenticated semantic replay:

```text
scratch/audit_r_c8_double_crossrail_commoncap_background_scope_20260801.py
  SHA-256 0a430485f0b603ddb53d3e7b32b2429b1539d62849a90ff4268d06fcee637bea
scratch/r_c8_double_crossrail_commoncap_background_scope_20260801.audit.json
  SHA-256 ab33f9918bebf61bb8c73d650ef1f8ae2107143f452a6d10278f6dbfae7f6443
  payload  df82573c9b6a0a83ac3403d0a31a77586e0d1ad64e5ef5e49ec8ed924c38806f
```
