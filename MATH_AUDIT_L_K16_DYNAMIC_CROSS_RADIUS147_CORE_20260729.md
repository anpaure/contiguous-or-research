# Audit of the k16 dynamic-cross radius-147 cut/seam core

Date: 2026-07-29

## 1. Frozen objects and scope

Let `F` be the rotational quotient factor in

```text
scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
```

and let the interval-packing certificate be

```text
scratch/k16_qfactor_q1_topresident_hamilton_residence_motifs_20260729.audit.json.
```

The audited byte and structural digests are

```text
scaffold SHA-256       f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5
motif-audit SHA-256    bf762af0339ec581d01e9c48991610425e51a864e065be23b8d23d21efbbf1f6
catalogue digest       e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3
```

The source has 858 distinct nonloop quotient edge orbits, sector histogram

\[
                     389\,AA+80\,AB+389\,BB,
\]

one quotient cycle of voltage 11 modulo 15, one physical cycle of length
12,870, and both 764-colour q1 palettes.  It is top-bi-resident but has 226
old-coordinate positive-residence motif orbits.

This note concerns the **loopless rotational deletion radius-147 face**.
Radius means

\[
 |F\setminus F'|=|F'\setminus F|=147,               \tag{1.1}
\]

not symmetric-difference size; the latter is 294.  Each quotient orbit has
15 physical copies, so (1.1) changes 2,205 old and 2,205 new physical edges.

Loops are excluded.  This is sound for a Hamilton target: a selected quotient
loop consumes both incidences of its quotient vertex and isolates that
vertex, so it cannot be the quotient of a connected physical Hamilton cycle.
No claim is made about non-Hamilton looped 2-factors.

## 2. Exact packing face

Let `P_1,...,P_147` be the certified pairwise edge-disjoint original motifs,
and put

\[
                         U=\bigcup_{i=1}^{147}P_i.
\]

The frozen census is

```text
packing sizes       2^20 3^72 4^55
|U|                 476
U sectors           AA233 AB36 BB207
incident vertices   586
```

Let `d_e` be the deletion bit for `e in U`.  Every resident radius-147 repair
must meet each `P_i`; disjointness and (1.1) therefore force

\[
                 \sum_{e\in P_i}d_e=1
                 \qquad(1\le i\le147).               \tag{2.1}
\]

Conversely, (2.1) gives exactly 147 deletions, all inside `U`; every source
edge outside `U` stays fixed.

Equations (2.1) do not by themselves hit all 226 source motifs.  For example,
original motif 10 is

\[
                         \{7264,11193\}.
\]

It meets the packing only through edge 7264 in packed motif 155, whose other
choices include 4761, 7271 and 15060.  Choosing one of those leaves motif 10
untouched.  Therefore every nonpacked original motif `H` needs

\[
                    \sum_{e\in H\cap U}d_e\ge1.       \tag{2.2}
\]

There are 79 such rows.  The 147 instances of (2.2) for packed motifs are
redundant with (2.1).

## 3. Exact seam universe and degree rows

Let `V_U` be the 586 quotient vertices incident with `U`.  If an off-source
edge selected by `F'` met a vertex outside `V_U`, it would increase final
degree at a vertex with no deletable source incidence.  Thus every possible
addition has both endpoints in `V_U`.

Conversely every off-source nonloop Johnson edge orbit with both endpoints in
`V_U` is a legitimate seam candidate.  Their exact census is

\[
             12320=5758\,AA+1550\,AB+5012\,BB.       \tag{3.1}
\]

Let `a_f` be its addition bit.  Since the source has degree two, final degree
two is exactly

\[
 \sum_{e\in U}\iota_v(e)d_e
   =\sum_{f\in A}\iota_v(f)a_f
 \qquad(v\in V_U),                                  \tag{3.2}
\]

where `iota_v` is endpoint incidence.  Only the 586 rows indexed by `V_U`
are nontrivial.  Summing (3.2) and using looplessness gives

\[
                       \sum_fa_f=\sum_ed_e=147,       \tag{3.3}
\]

so an explicit addition-count row is redundant.

Parallel quotient orbit IDs remain distinct throughout: they may have
different phase, voltage and q1 data.

## 4. Both exact q1 palettes

For a lower or upper q1 colour `c`, let `Prov(c)` be its complete quotient
provider list.  If some provider belongs to fixed `F\setminus U`, its row is
automatic.  Otherwise the exact row is

\[
 \sum_{e\in Prov(c)\cap U}(1-d_e)
 +\sum_{f\in Prov(c)\cap A}a_f\ge1.                  \tag{4.1}
\]

No shore-count surrogate is used.  The complete census of nonautomatic rows
is

\[
                    396\text{ lower}+401\text{ upper}.\tag{4.2}
\]

Equations (2.1), (2.2), (3.2) and (4.1) are necessary and sufficient for a
loopless radius-147 repair which has quotient degree two, both q1 palettes,
and destroys every original residence motif.

After mechanically deleting tautologies and duplicate implications, the
smallest explicit core obtained here has

```text
Boolean variables: 476 cut + 12320 add = 12796
hard rows:         147 packing equalities
                  +79 other old-motif rows
                  +586 degree rows
                  +396 lower-q1 rows
                  +401 upper-q1 rows
                  =1609.
```

“Smallest” here means after the displayed exact mechanical eliminations; it
does not assert polyhedral irredundancy of all 1,609 remaining rows.

## 5. The AB correction

The first dynamic driver imposed

\[
                    \sum_{e\in U\cap AB}d_e\ge1.      \tag{5.1}
\]

This is unjustified.  The fixed-cross no-go freezes all old AB edges **and**
forbids every new AB edge.  A changed cross pattern can instead retain all 80
old AB edges and add new AB seams while deleting only AA/BB.  Shore-degree
balance gives only

\[
                         a_{AB}\equiv d_{AB}\pmod2,    \tag{5.2}
\]

so `d_AB=0,a_AB=2` is permitted.  Indeed 1,125 of the 1,550 addable AB
orbits join two old interior vertices.

The exact predicate “the final AB bank differs” would be

\[
            \sum_{e\in U\cap AB}d_e+\sum_{f\in A\cap AB}a_f\ge1,\tag{5.3}
\]

but the base model does not need it.  Omitting (5.3) also avoids importing a
trusted CP-SAT fixed-cross transcript as if it were a proof-checked theorem.

## 6. What is deliberately post-audited

The hard core does not impose quotient connectivity, voltage or absence of
new residence motifs.  A primal candidate is literally lifted and audited.

For an oriented quotient cycle `C`, if an edge traversed from endpoint phase
`alpha_u` to `alpha_v` contributes `alpha_v-alpha_u`, define

\[
 V(C)=\sum_{u\to v\in C}(\alpha_v-\alpha_u)\pmod {15}.\tag{6.1}
\]

A quotient cycle of length `L` lifts to

\[
 \gcd(15,V(C))\text{ physical cycles, each of length }
 \frac{15L}{\gcd(15,V(C))}.                           \tag{6.2}
\]

Hence a quotient factor gives one physical Hamilton cycle exactly when it
has one quotient cycle and its voltage is a unit modulo 15.  The independent
auditor also constructs the literal lift and checks that (6.2) predicts its
component count.

Hitting the 226 old motifs is not full residence: new seams can create new
positive short runs, and AB changes can create new top-zero short runs.
Therefore:

- core SAT plus failed topology or residence is `target UNKNOWN`;
- core SAT plus one physical component and full literal residence is target
  SAT;
- core INFEASIBLE excludes every target in this exact loopless radius face,
  but absent a proof log it is recorded only as a trusted CP-SAT transcript;
- timeout is UNKNOWN; `MODEL_INVALID` is ERROR.

The larger live CEGAR driver now adds exact no-goods for new positive runs in
all coordinates and complemented-top runs.  It is a sound continuation but
retains 420 mechanically redundant base rows.  A resident 2-factor from that
driver is still only a relaxation SAT unless the one-cycle/unit-voltage
post-audit passes.

## 7. Machine result

The row-minimal core was run only on H100 CPU, pinned to eight cores, with
seed 16847 and a 900-second CP-SAT bound.  It returned `OPTIMAL` (feasibility
model) after 862.32 solver wall seconds.  The retained H100 environment is
OR-Tools 9.15.6755 under Python 3.12.3:

```text
hard-model verdict     SAT
target verdict         UNKNOWN
variables              12,796
constraints            1,609
branches               2,949,834
conflicts              53,216
```

The witness has 147 deletions and 147 additions with sector profiles

```text
removed  AA78 AB6  BB63
added    AA69 AB24 BB54.
```

Thus it is a genuine dynamic-cross solution, selecting 98 final AB edge
orbits.  Independent replay verifies:

- exactly one deletion in every packed motif;
- all 226 original motifs hit;
- quotient degree two at all 858 vertices;
- all 764 lower and all 764 upper q1 colours; and
- the exact source-cut-plus-seam identity.

The topology/voltage and residence post-audit fails sharply.  The quotient
factor has six cycles:

| quotient length | voltage mod 15 | lift components | physical cycle length |
|---:|---:|---:|---:|
| 80 | 12 | 3 | 400 |
| 446 | 14 | 1 | 6,690 |
| 250 | 10 | 5 | 750 |
| 69 | 3 | 3 | 345 |
| 9 | 14 | 1 | 135 |
| 4 | 1 | 1 | 60 |

Hence there are 14 physical cycles, with lengths

```text
60, 135, 345,345,345, 400,400,400,
750,750,750,750,750, 6690.
```

There are 2,295 newly present positive short runs,

```text
length 1: 240
length 2: 855
length 3: 1200,
```

and top biresidence also fails.  Therefore this is **SAT for the requested
hard core** and **UNKNOWN for a resident physical Hamilton target**.  It is
not a k16 carrier and not a word.

The selected-ID digest is

```text
4b5b48c34ed024576f0dec60ca5c14f50082917c9a5d03b446fec8fbb257be89.
```

The raw solver artifact exposed one operational defect in the executed
driver: it hashed the in-memory payload before JSON converted integer
histogram keys to strings, so its embedded digest does not replay from the
saved bytes.  The raw file itself is frozen under SHA-256

```text
946adcc0270ebbcb311e3435584a382588d90c5314f1826592f61362d792b144.
```

The independent audit records
`PASS_PRIMAL_WITH_RAW_ARTIFACT_DIGEST_BUG`, replays the entire primal and
post-audit, and freezes the exact executed driver (SHA
`7ce2464dbc1803c8b823f3ac8505e4104509acf1bbacc8ba7a5df8f081c4d761`).
An additional adversarial solver-free replay found no discrepancy in the
face, palettes, motif hits, degree ledger, voltages, lift, or run census.
The current driver canonicalizes through JSON before hashing, so future
artifacts do not have this defect.  No solver rerun is needed to validate the
primal witness.

## 8. Dualrail evidence barrier

The live Claude engine

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/dualrail.py
```

was separately audited.  Its current SHA-256 is

```text
b4cec5ee93ecc7e41c68cbb573a59b7a35df0a3f126ff81eaad84cd77cd2ccc2.
```

The reported subtour error has been corrected in that snapshot.  If `c_e`
is a rail-cut indicator, the selected boundary term is `1-c_e`, and the
valid lazy cut is

\[
 \sum_{e\in\delta_{rail}(S)}(1-c_e)
 +\sum_{e\in\delta_{rung}(S)}y_e\ge1.                 \tag{8.1}
\]

Using `c_e` makes the incumbent row vacuous because incumbent boundary rail
edges are precisely cut edges.  The coefficient one in (8.1) is sharp for
the moving-endpoint path formulation.

Nevertheless the current engine is not exact:

1. its input assertions disappear under `python -O`;
2. `b>=2` does not force the required marked internal four-state B ear—two
   terminal B segments satisfy the scalar row with no internal ear;
3. its final audit checks middle, Johnson, q1 and positive internal
   residence, but not arbitrary-width upper coverage, COMP3/lower coverage,
   or literal replay of all 65,535 nonempty masks;
4. `MASTER PASS` and the saved field `cycle` therefore overstate a path
   candidate; and
5. solver failure and lazy-budget statuses are not fail-closed.

Thus no `dualrail.py` PASS is evidence for this note.  The strongest current
meaning would be `CARRIER_Q1_RESIDENCE_PASS_NO_COMP3`, after replacing all
input assertions by explicit validation and adding the exact marked-ear row.

## 9. Audited implementation

The row-minimal driver and solver-free primal verifier are

```text
scratch/search_k16_dynamic_cross_radius147_core_20260729.py
scratch/audit_k16_dynamic_cross_radius147_core_20260729.py
scratch/search_k16_dynamic_cross_radius147_core_s16847_executed_20260729.py
scratch/k16_dynamic_cross_radius147_core_s16847_20260729.json
scratch/k16_dynamic_cross_radius147_core_s16847_20260729.audit.json.
```

The original/live larger driver is not used for the machine verdict in this
note.
