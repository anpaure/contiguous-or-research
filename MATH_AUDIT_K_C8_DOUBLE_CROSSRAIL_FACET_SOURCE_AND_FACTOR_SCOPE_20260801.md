# Audit of the C8 double crossrail: facets, source signature, and protected-factor scope

Date: 2026-08-01  
Lane: K, independent local/factor audit  
Verdict: **GO at the stated local scope.**  The isolated-facet census and
the all-`d` source formulas are exact.  The protected incidence cost is
`4d+30`, and residence of the twelve auxiliary edges is only
componentwise until their endpoint runs are extended.

## 1. Authenticated endpoint correction

For the split endpoint

\[
 \{z,b\},\{z,c\},\{z,c,f_d\},\ldots,\{z,c,f_1\},
\]

the overlooked interval families

\[
 I^S_j=[1,d-j+1],\qquad I^P_j=[d-j+2,d+1]
 \quad(1\le j<d)                                      \tag{1.1}
\]

are adjacent and disjoint within each ticket, and have values

\[
 \{z,c\}\cup F[j+1,d],\qquad
 \{z,c\}\cup F[1,j].                                  \tag{1.2}
\]

The `2(d-1)` interval addresses in one endpoint bank are distinct.  The
first authenticated seam carries `P_0<->S_1` in its old phase; the
`a_1<->a_3` symmetry seam carries `P_1<->S_0` in its new phase.  The other
phase of either fixed seam is not a cross bank.  This is an exact finite
statement for `2<=d<=12`, not an assertion that both banks inhabit one of
those endpoint phases.

After releasing the prefix target masks, the target-labelled transported
background avoids all cells in (1.1).  This uses one left vertex per target
mask.  It does not preserve multiple protected occurrences of one mask or
unrecorded width/deadline/chronology guards.

## 2. Dimension-uniform bridge and source signature

The owner path

\[
 G_1,\ldots,G_d,B,A,H_1,\ldots,H_d,D,E                \tag{2.1}
\]

has `2d+4` distinct rank-`r` vertices and `2d+3` Johnson transitions.  Its
intersections are the seven symbolic classes displayed in the theorem;
boundary filler and active-label signatures separate the classes, and the
omitted filler pair separates each sweep.  Hence all lower colours are
distinct.  Its upper multiset has four values with multiplicities

\[
                         d,\ 1,\ d+1,\ 1.             \tag{2.2}
\]

The internal-run calculation is exact: every wholly internal positive run
has length at least `d+1`.

The maximal-envelope source has `3d+4` positions.  Its two modified rail
blocks are

\[
 [d+1,2d],\qquad[2d+3,3d+2].                          \tag{2.3}
\]

Every replacement letter is nonempty and lies below its envelope.  The
unchanged anchor envelopes together with the two rail prefixes/suffixes
recover every owner, so `D^dQ=T` exactly.  Prefix/suffix carving in (2.3)
gives `2(d-1)` tickets on `4(d-1)` distinct interval addresses, with the
two desired constant-union banks.  Cells from different tickets are nested
and may overlap; only the two cells of one ticket are support-disjoint.

This is one literal local common-cap state for the owner and cross rows.
It is not a transport map for an arbitrary incumbent exterior matching.
The common-cap maxima on a left rail are exactly
`K union {z,a_1,f_s}`, and on a right rail exactly
`K union {z,a_3,f_s}`; off the rails they remain the owner envelopes.
Thus an extra pointwise lower bound is compatible precisely when it lies
inside those displayed maxima before any exterior row is added.

There is also a typed-width distinction.  A bridge prefix/suffix ticket has
widths `j` and `d-j`, whereas the authenticated endpoint occurrence carrying
the same suffix mask has width `d-j+1`.  Equality of target masks does not
identify these physical occurrences under an exact-width, phase, or address
guard.

## 3. Exact twelve-facet census

The common core `K` is load-bearing in every upper target.  With it included,
the eight high values and eight boundary values all have rank `r+1`.
The bridge already supplies two high values and the two boundary values
with active signature `za_1a_3`.

For each of the six remaining high values, deleting `f_0` and `f_(d+1)`
gives one Johnson edge.  For each of the six remaining boundary values,
deleting `f_1` and `f_2` gives one Johnson edge.  Thus there are exactly
twelve auxiliary components and twenty-four auxiliary owners.

They are pairwise distinct and disjoint from the bridge:

* the six unused two-active signatures distinguish the high components;
* the three unused three-active signatures together with
  `b in {f_0,f_(d+1)}` distinguish the six boundary components; and
* the only bridge pair signatures are `za_1,za_3`, while its only relevant
  triple is `za_1a_3`, precisely the excluded signatures.

Their lower colours are respectively

\[
 K\cup A\cup F^\circ,
 \qquad
 K\cup R\cup(F^\circ-\{f_1,f_2\})\cup\{b\},          \tag{3.1}
\]

so active cardinality/signature and then `b` separate them from one another
and from the bridge palette.  Therefore the completed Johnson forest has

\[
 13\text{ components},\qquad 2d+28\text{ owners},\qquad
 2d+15\text{ Johnson edges/lower colours}.             \tag{3.2}
\]

Its upper support is exactly the sixteen canonical values.

## 4. Protected incidence and residence scope

For use in the middle-levels incidence graph, every Johnson edge in (3.2)
must be subdivided through its lower colour.  The literal protected bank
therefore has

\[
                         2(2d+15)=4d+30                \tag{4.1}
\]

incidence edges, not `2d+15`.  Its two alternating classes each have
`2d+15` edges.  Consequently the small protected-factor theorem applies to
one copy only under

\[
                             4d+30\le m-2,             \tag{4.2}
\]

and to `H` resource-disjoint copies under `H(4d+30)<=m-2`, before pricing
any additional boundary incidences.

The sixteen protected upper representatives can consist of the twelve
auxiliary incidences, the two chords, one `M_+` occurrence, and one `M_-`
occurrence.  The other `2d-1` protected non-perfect-class incidences then
carry repeated upper colours and must remain compatible with the connector
bank.  Neither the protected-factor theorem nor marginal upper Hall proves
that graphic/free-port correlation.

The bridge itself is internally depth-`d` resident.  Each auxiliary
two-owner edge is resident only because all its runs meet a component
boundary.  Joining those components arbitrarily can turn a length-one or
length-two clipped run into an internal short run.  A global embedding must
extend those endpoint runs or retain the relevant component boundaries.

Finally, the displayed maximal-envelope source realizes only the bridge.
The twelve auxiliary Johnson edges have no simultaneous source/cap
realization in this theorem.  Graph containment preserves their owner turn
and upper witness once both incidences are protected, but it does not create
their source occurrences or transport the exterior compiler.

## 5. Artifact authentication

The four artifacts cited by the theorem have the stated SHA-256 hashes:

```text
bc635c1401b7abe71c977dd96247062611ef58e165489a87a4ccf4ce30dbc146
  scratch/audit_c8_actual_phase_two_ray_crossbank_20260801.py
a802b7c3de50985e3026f65e70ce9da0f6effa5a33d9b777d676b147368323db
  scratch/c8_actual_phase_two_ray_crossbank_20260801.audit.json
23be11a67d06218dc9869004605766e3d5984426728b49a00c2d78879e682f3e
  scratch/audit_c8_double_crossrail_resident_bridge_20260801.py
e9e1ec35c45bf569085f68a109f0971d06ba1a19c4303a0727519cca15f576bc
  scratch/c8_double_crossrail_resident_bridge_20260801.audit.json
```

The matching authoritative remote directories are

```text
/home/amodo/or15/work/c8_prefix_bank_20260801/scratch/
/home/amodo/or15/work/c8_double_crossrail_20260801/scratch/
```

Their hashes agree byte-for-byte with the local files.  A stale,
non-authoritative duplicate endpoint script exists at
`/home/amodo/or15/work/scratch/c8_prefix_bank_20260801/` with SHA-256
`211f991177b7256ba8ac28e09151b6956a8c90967793b737a5495e824a938826`;
it is not the cited artifact.

The JSON payload hashes also recompute exactly:

```text
PASS_C8_ACTUAL_PHASE_TWO_RAY_CROSSBANK
  ac6c416e2236eeeede948a9802183c439061be2462ef0e2e4ebaccb299d78a07
PASS_C8_DOUBLE_CROSSRAIL_RESIDENT_BRIDGE
  778f2a833db1a032268ebcbd2e49a7b38dad1dcf6203a4bb08ad5ceec85bb067
```

The first replay imports the folded-factor and one-ray modules and reads the
frozen one-ray certificate; its top-level script/JSON pair is therefore not
a self-contained provenance bundle.  The relevant direct dependency hashes
are

```text
9dc3c06e00ff0d6586cd2176d448e44c88065e3d016ef48acebfacc006e300a2
  scratch/audit_c8_folded_hamilton_two_ray_lift_20260801.py
0a2b73a46f89c937c61ffe2ab7ccd095373d2604ab67574f456eb95be6de7929
  scratch/audit_c8_one_ray_upper_support_seam_20260801.py
e8834f6b830268fd887e1abf4a477765d4c8ec986815caf2bc7c0f319fdd9619
  scratch/c8_one_ray_upper_support_seam_20260801.audit.json
```

The endpoint replay is finite (`2<=d<=12`).  The bridge replay checks
`2<=d<=64`, in the normalized `K=emptyset` specialization.  The all-`d`,
arbitrary-`K` conclusion rests on the symbolic formulas above, not on
extrapolating that finite range.  A separate semantic replay checks
`|K|=1`, the corrected facets, and the common-cap/background boundary:

```text
0a430485f0b603ddb53d3e7b32b2429b1539d62849a90ff4268d06fcee637bea
  scratch/audit_r_c8_double_crossrail_commoncap_background_scope_20260801.py
ab33f9918bebf61bb8c73d650ef1f8ae2107143f452a6d10278f6dbfae7f6443
  scratch/r_c8_double_crossrail_commoncap_background_scope_20260801.audit.json
PASS_LOCAL_COMMONCAP_BACKGROUND_TRANSPORT_REMAINS_CONDITIONAL
  payload df82573c9b6a0a83ac3403d0a31a77586e0d1ad64e5ef5e49ec8ed924c38806f
```

No H100 log or host manifest is needed for the proof, and none is present
in the JSON files; their mathematical contents and hashes, rather than
remote execution provenance, are what is authenticated here.
