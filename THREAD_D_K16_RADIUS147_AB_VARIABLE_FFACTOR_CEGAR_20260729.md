# Thread D: exact radius-147 AB-variable f-factor CEGAR

Date: 2026-07-29  
Scope: canonical `k=16` top-bi-resident Hamilton quotient scaffold, its
certified 147-motif packing, quotient degree two, both `q1` palettes, and
two-sided residence.  `AddCircuit` is intentionally absent.

## 1. Frozen inputs

The construction is pinned to:

- scaffold SHA-256
  `f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5`;
- motif-audit SHA-256
  `bf762af0339ec581d01e9c48991610425e51a864e065be23b8d23d21efbbf1f6`;
- reconstructed catalogue digest
  `e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3`.

The audit reconstructs 226 old positive-residence motifs.  The certified
packing has 147 pairwise edge-disjoint motifs and union `U` of size 476.
Their intersection-size histogram with `U` is

\[
 |M\cap U|:\quad 1^{21},2^{39},3^{102},4^{64}.
\]

This histogram exposes an important correction: 56 old motifs are not
contained in `U`.  Their exact row is

\[
  \sum_{e\in M\cap U}r_e\ge 1,
\]

because every source edge in `M\setminus U` is fixed selected.  Indexing a
cut variable for every edge of `M` is invalid; the earlier variable-cross
prototype crashed on precisely such an edge.

## 2. Exact radius face

For every `e in U`, let `r_e` say that source edge `e` is removed.  For every
off-source nonloop catalogue edge `f` whose endpoints lie among the 586
vertices incident with `U`, let `a_f` say that `f` is inserted.  There are

\[
476\text{ removal variables},\qquad
12,320=5,758\ AA+1,550\ AB+5,012\ BB
\]

insertion variables.

The endpoint restriction is complete.  If `v` is not incident with `U`, no
source edge at `v` can be removed.  Since the source and replacement both
have degree two,

\[
 \deg_A(v)=\deg_R(v)=0,
\]

so no inserted edge can touch `v`.

The base model consists of:

1. one equality `sum_{e in P_i} r_e = 1` for each of the 147 packed motifs;
2. all 226 exact old-motif rows above;
3. the explicit equality `sum_f a_f=147`;
4. 858 incidence-balance equations `deg_A(v)=deg_R(v)`;
5. 797 nontrivial provider rows, 396 lower and 401 upper, after rows already
   met by a fixed source provider are removed.

Thus the frozen base proto has 12,797 variables including OR-Tools' constant
and 2,029 constraints.  No row forces an AB removal.  The certified
six-AB transversal is only a solver hint.  This matters because the prior
fixed-AB no-go is a trusted CP-SAT transcript, not a proof certificate.

Quotient loops are omitted.  This is exact for the Hamilton target: a
selected quotient loop saturates its quotient vertex and is an isolated
quotient component.  Consequently an UNSAT result has the stated
**loopless/Hamilton-target** scope, not the larger disconnected multigraph
scope that admits the 19 induced off-source quotient loops.

## 3. Complete two-sided residence separation

For a current physical short positive run of length `ell<4`, retain the
entering edge, its internal edges, and the exiting edge.  If `D` is the set
of their quotient edge-orbit IDs, persistence of these literal physical
edges gives the necessary clause

\[
 \sum_{e\in D}x_e\le |D|-1.                 \tag{3.1}
\]

The ordinary catalogue oracle emits (3.1) for positive runs in all sixteen
coordinates.  That oracle alone is incomplete after dropping `AddCircuit`:
an all-AA component can be a short all-zero run of the top coordinate and
has no positive top boundary.  The new oracle repeats the physical-cycle
extraction on the complemented top trace and emits the same literal clause.
Therefore every rejected incumbent has a fresh positive or complemented-top
clause.  This includes monochromatic components, which the older dynamic
boundary/reach gadget did not exclude.

An all-fixed fresh motif would be a solver-free obstruction to the entire
radius face and is preserved explicitly.  Otherwise (3.1) is added and the
factor solve is repeated.

## 4. Topology audit

No connectivity row is present.  Every feasible incumbent is lifted
literally, and the artifact records:

- all quotient components;
- each component voltage modulo 15;
- `gcd(15,voltage)` through its lift-component count;
- physical component count and lengths;
- positive residence and complemented-top residence.

A resident result is a valid degree-two intermediate certificate.  It is a
Hamilton carrier exactly when the lift has one physical component; for one
quotient component this is equivalent to unit voltage.

## 5. Certificate and negative scope

The primary source is
`scratch/search_k16_dynamic_cross_radius147_cut_seam_20260729.py`; the
solver-free positive replay is
`scratch/audit_threadD_k16_radius147_ab_ffactor_cegar_20260729.py`.

Every run freezes the exact final `CpModelProto`, source/module/input hashes,
OR-Tools version, command, parameters, and round ledger.  A positive result
is independently checkable from its selected edge IDs: the replay verifies
radius 147, the 147 packing equalities, all 226 motif hits, quotient degree,
both `q1` palettes, all positive and complemented-top residence motifs, and
the complete component/voltage ledger.

CP-SAT `INFEASIBLE` is not by itself a rigorous UNSAT proof.  It is retained
as reproducible trusted-solver evidence only.  A proof-grade negative must
translate the frozen Boolean/PB model to CNF or OPB and verify a DRAT/LRAT or
VeriPB proof, or supply a solver-free obstruction.

## 6. Build audit

The H100 CPU build-only run used OR-Tools `9.15.6755` and reproduced exactly:

```text
cut variables       476
add variables       12320
candidate vertices  586
q1 rows              797
proto variables      12797
base constraints     2029
```

Its frozen model proto SHA-256 is
`a8d060bbb990234c0a87d01eed488e0f9dc859c10259371d323baad517e6aeaf`.
The local solver-free provenance replay passes.  The earlier no-hard-top
relaxation ended `UNKNOWN` after 300 seconds and has no mathematical
negative content.

