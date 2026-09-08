# K17 Y=61423 orbit-closed protected-bank residence-core no-go

Date: 2026-08-02  
Status: exact scoped theorem; independently replayed; DRAT-verified UNSAT with
a three-clause input core.  This theorem concerns the frozen marker58
`Z_17`-equivariant quotient face.  It does **not** exclude a non-equivariant
completion which protects only the 90 listed physical edges, and it makes no
global claim about K17.

## 0. Result

The authenticated `Y=61423` singleton-hole bank consists of 76 physical
rank-nine owners and 90 physical Johnson edges.  As a physical partial support
it forces no positive coordinate run of length one, two, or three.

That statement does not survive equivariant orbit closure.  Mapping the 90
physical edges into the frozen marker58 quotient gives seven already-fixed
edges and 83 optional edge orbits.  Two of the required optional primaries are

```text
x_8810 = 1,
x_18036 = 1.
```

The authenticated residence master already contains the sound clause

```text
-18036 -8810 0
```

because those two developed orbits, together with one fixed edge, force a
positive run of length two.  The occurrence ledger contains exactly 17 such
runs, one for every coordinate translate.  Consequently the orbit closure of
the bank has no depth-three-resident completion even before topology, voltage,
or the requirement that `Y` remain missing is imposed.

Equivalently, the complete protected-completion formula is UNSAT by the input
core

```text
p cnf 324661 3
-18036 -8810 0
8810 0
18036 0
```

This is a local residence-core theorem on an equivariant face, not evidence
that the underlying 90-edge physical bank is intrinsically impossible.

## 1. Exact quotient projection of the bank

For a physical unoriented Johnson edge `{A,B}`, define its quotient key by

\[
  \kappa(A,B)=\min_{g\in\mathbb Z_{17}}
     \operatorname{sort}(\rho^g A,\rho^g B).
\]

The frozen v3 arc map has exactly 35,937 forward edge-orbit rows.  Mapping all
90 support edges by `kappa` gives

```text
bank_support_edges=90
already_fixed_edges=7
optional_orbit_primaries=83
```

In particular, the bank contains the physical representatives

```text
primary  8810: 19433--84961
primary 18036: 19433--25577
```

and therefore its orbit-closed realization entails the two unit clauses
`8810` and `18036`.

The distinction between physical support and orbit closure is essential.  The
earlier partial-residence audit inspected exactly the 90 listed physical
edges and correctly found no fully selected short-run interval.  A quotient
primary selects all 17 rotations of its representative.  Those additional
translated edges are what close the bad residence interval.

## 2. Human-checkable residence contradiction

The marker58 compact-Horn base is

```text
/home/amodo/or15/work/root_k17_compact_horn_v3_20260802/
  marker58_compact_horn_v3.cnf
```

with header

```text
p cnf 314651 1833776
```

and SHA256

```text
cff3acda560916bdb846fb2f7026c0e4c514de54da4672f48d18f24ce02c103c
```

An independent parser checked all 1,833,776 input clauses and found exactly
one occurrence of the binary clause `{-18036,-8810}`.  The frozen occurrence
ledger independently has exactly 17 rows with

```text
run_length=2
fixed_edges=1
selected_primaries=8810,18036
```

and their coordinate column is precisely `{0,1,...,16}`.  Hence the binary
clause is the developed form of one bad run in every translate.

The protected bank imposes both positive units, so ordinary unit propagation
derives the empty clause.  No solver search or higher-level construction
assumption is involved.

## 3. Exact full-Y rejection encoding (logically downstream)

For completeness, the protected master also encoded the requested condition
that no selected `Y`-clean component have union `Y`.

There are

\[
  \binom{14}{9}=2002
\]

rank-nine owners contained in `Y`.  Every such owner omits exactly five
coordinates of `Y`.  Introduce a Boolean variable `h_(U,y)` for each omitted
coordinate and impose exactly one label per clean owner.  For every selected
developed clean-clean edge `UV`, propagate equality of the label on its two
ends.  There are 10,010 label variables, 31,846 developed clean-clean edges,
and 318,460 directed propagation clauses.

This encoding is exact:

* a satisfying label is constant on each selected clean component and names
  a coordinate absent from every owner of that component, so its union is a
  proper subset of `Y`;
* conversely, every proper clean component has at least one coordinate absent
  from all its owners, which supplies a constant label.

The resulting formula has

```text
p cnf 324661 2174341
```

but its full-Y clauses are irrelevant to UNSAT: DRAT trimming reduces the
proof to the three residence clauses displayed in Section 0.  The same is
true of any one-cycle, voltage, or upper-shadow strengthening added on top of
this face.

## 4. Proof artifacts and independent replay

Remote root:

```text
/home/amodo/or15/work/longrun_k17_y61423_protected_completion_20260802/
```

Principal SHA256 values:

```text
89a9121c97e4258ce947d39ef2554bd342d4f9c2dcdaead7738949aed9572350  bank.tsv
e58574c284fc97e7cd2072b89811aa5f4ac18199860f032553253770cfb452ed  protected_completion.cnf
e3443a8e0f42ae1af9c6276b4acb0eb88c791fd2f8c2b2751f142eca2447f473  protected_completion.map.tsv
84ae9c1441a87965e3a7293ccb87bde803ebe6810bb9fd9fad62f93877766d07  protected_completion.drat
a50e0997bb114336baac449f55f61279e4c2486ef1d4d946bc8df0919eb48272  protected_completion.core.cnf
46fb6f2825d1f6c4e7fd15c7037087d578e74c0bed846741e54b8d5c27d9da84  protected_completion.lrat
333129d1a098243cf650d63ceb4e09739933f30f5fda8e69fe26006153370733  drat_trim.out
0fc0e7bf83594a3bff3a47eb4e0a2eaf4e867675742aaabf7df14263e9a6299b  protected_completion.solver.out
7131ceceeca2dc6a5db0d6a55f31b8f5e028d2014af08c5d570d51e6770347c5  protected_completion.resource.txt
```

Kissat 4.0.4 returned `UNSATISFIABLE` after 0.23 seconds with zero conflicts
and zero decisions.  `drat-trim` reported

```text
UNSAT via unit propagation on the input instance
3 of 2174341 clauses in core
1 of 22263 lemmas in core using 3 resolution steps
0 RAT lemmas in core
s VERIFIED
```

The independent C++ replay is

```text
6c8df5a1b38fff16d4582d1760f1f258ce1fa749a1b78b1f17b8dc35ff933498
  scratch/audit_k17_y61423_protected_bank_residence_core_20260802.cpp
```

It reconstructs the quotient orbit keys rather than trusting the builder,
parses the entire base CNF, and checks the translated occurrence ledger.  Its
authenticated output is

```text
PASS_K17_Y61423_PROTECTED_BANK_RESIDENCE_CORE_AUDIT
bank_support_edges=90 optional_orbits=83 core_units=8810,18036
core_clause=-18036,-8810 translated_length2_runs=17 coordinates=17
physical_bank_edges_on_8810=1 physical_bank_edges_on_18036=1
```

Additional input/output hashes are recorded in
`scratch/k17_y61423_orbit_closed_protected_bank_residence_core_20260802.audit.json`.

## 5. Exact conclusion and next scope

The resolved question is:

> Can the orbit closure of the authenticated 90-edge bank lie in the frozen
> marker58 depth-three-resident quotient face?

No.  The answer is solver-free once the quotient projection is made.

The unresolved question is strictly different:

> Can a non-equivariant owner-once exact-facet factor contain just these 90
> physical edges, attain positive residence floor four, and make every
> `Y`-clean component proper?

The three-clause core says nothing about that unrestricted physical problem.
It does, however, eliminate this bank from every equivariant completion lane
and explains exactly why the physical partial-support audit and quotient
master appeared to disagree.
