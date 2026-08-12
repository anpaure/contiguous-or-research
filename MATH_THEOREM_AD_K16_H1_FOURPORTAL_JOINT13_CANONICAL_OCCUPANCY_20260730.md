# K16 H1 four-portal joint13 canonical occupancy theorem

Date: 2026-07-30  
Lane: AD  
Status: exact support-restricted equisatisfiable encoding; **UNSOLVED/UNKNOWN**

## 1. Authenticated source and exact portal geometry

Let \(A=(A_0,\ldots,A_{12872})\) be

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

Fresh ending-OR replay gives the unique hole


\[
                         H=11373=\mathtt{0x2c6d}.
\]

The exact provider atlas has 28,805 distinct
`(position,replacement-value)` one-cell provider pairs for \(H\),
none lossless.  Its minimum final hole count is two, attained 153 times in
exactly four families:

| portal | exact replacement family | number | exact new debts |
|---:|---|---:|---|
| (0) | (\mathtt{0x0800}\cup s, s\subseteq\mathtt{0x246d}) | 128 | (18553,26745) |
| (4489) | (\mathtt{0x0024}\cup s, s\subseteq\mathtt{0x2041}) | 8 | (9833,11881) |
| (6440) | (\mathtt{0x0440}\cup s, s\subseteq\mathtt{0x002d}) | 16 | (32877,43117) |
| (12872) | (H) | 1 | (52833,52835) |

The old occurrence ledger of the eight debts is

```text
18553 : [0,0]                         26745 : [0,1]
 9833 : [4487,4489]                  11881 : [4486,4489]
32877 : [6440,6440]                  43117 : [6438,6440]
52833 : [12871,12872]                52835 : [12869,12872],[12870,12872].
```

Consequently the smallest union of the source private-debt witness hulls is

\[
 S=[0,2)\ \dot\cup\ [4486,4490)\ \dot\cup\ [6438,6441)
      \ \dot\cup\ [12869,12873),                                    \tag{1.1}
\]

with (|S|=13).  The position-zero (H)-witness is ([0,3]), but positions
2 and 3 are fixed suffix context and do not belong to the minimal editable
hull.  The other displayed (H)-witnesses are respectively
([4486,4489]), ([6438,6440]), and ([12872,12872]).

The independent geometry audit is

```text
scratch/audit_ad_k16_h1_four_portal_geometry_20260730.py
SHA-256 145c9d16c1b626f8613940bd38d53350e7652b5ee9584df14cf5a13e533d2f28

scratch/ad_k16_h1_four_portal_geometry_20260730.audit.json
SHA-256 3263ab64f540e5552f810f2dbf919d6b18da89310162ff8746c0f099e9b4a9d0
```

The detailed atlas used by the builder is

```text
scratch/k16_reorganized_h1_exact_provider_atlas_v2.audit.json
SHA-256 b216a9da50abe571969049cc5c60b4dff534c6eebba286de1612ef9c124d3c68.
```

It has the same 28,805-move scalar ledger as the original authenticated
atlas and additionally retains all 153 minimum rows.  The geometry audit
independently regenerates the four families from the source.

## 2. Exact safe-gap and local-form reduction

Delete the thirteen editable cells in (1.1).  The three intervening fixed
runs have ORs

\[
 \bigvee A_{[2,4486)}=\mathtt{0x7fff},\qquad
 \bigvee A_{[4490,6438)}=\mathtt{0xffff},\qquad
 \bigvee A_{[6441,12869)}=\mathtt{0xffff}.                           \tag{2.1}
\]

Fixed-only interval replay covers 65,480 of the 65,535 nonzero masks.  The
remaining family (R) has exactly 55 masks:

```text
8805,8813,8933,8941,8949,9325,9833,9837,9965,9981,10349,
10361,10365,10441,10997,11369,11373,11465,11497,11881,11885,
13421,14537,14793,15561,15593,15817,15849,18553,26745,30317,
31177,32877,35938,35943,36070,36071,37997,40166,42093,43117,
43129,43133,44141,46189,48367,52321,52323,52327,52455,52833,
52835,54381,59513,63085.
```

Every (T\in R) contains the common coordinate

\[
                           c=6,qquad 2^c=\mathtt{0x0040}.             \tag{2.2}
\]

No (T\in R) contains any interblock gap OR from (2.1).  Therefore a
literal (T)-interval cannot meet two editable blocks.  Independently
regenerating every distinct fixed suffix OR, internal fixed-gap OR, and fixed
prefix OR gives:

* 341 changed-interval bases in total, at most 40 for one editable block;
* exactly one inclusion-minimal residual need for every (T\in R) and every
  nonempty subinterval of one block;
* (3+10+6+10=29) local forms per target and (55\cdot29=1595) forms total;
* no compatible cross-block form.

This agrees term-for-term with the pinned unbounded dynamic-substitution
reference model:

```text
reference_parent.cnf   SHA-256 0fc8ab9880a5016cbc404810f74f1b04c54e93903f6b2b7e1ff47e7dc12f8cb7
reference_parent.map   SHA-256 cefb607c2b16278aeafedc865fd74ec86f77bf5dc35b83a2a3fd347c8cdc47e9
reference_parent.stats SHA-256 60fdaf28c87c4d8380cc270e1b3b837f98b0824ff05eebe840c01d3e85fa9d44.
```

That reference has `budget=-1`, 1,816 variables, 35,208 clauses, and 81,990
literals.  It is a semantic reference, not a solver verdict.

## 3. Canonical occupancy variables

Index the cells of (S) in physical order by (i=0,\ldots,12).  For each
(T\in R), introduce:

* (o_{T,i}), saying that the selected literal witness of (T) uses cell
  (i); and
* four block controls (g_{T,b}).

Impose one target ALO row, (o_{T,i}\Rightarrow g_{T,b(i)}), pairwise AMO
on the four controls, and the exact one-run clauses within each block.  For
a width-(w) block the latter forbid two nonadjacent (0\to1) starts and
use (\binom{w-1}{2}) clauses.  Hence each target selects exactly one
nonempty interval in exactly one block.

For every cell (i) and coordinate (q\ne c), introduce an availability
bit (a_{i,q}).  Add

\[
 o_{T,i}\Longrightarrow\neg a_{i,q}\quad(q\notin T),                 \tag{3.1}
\]

and the reverse canonical row

\[
 a_{i,q}\ \vee\!\bigvee_{T\in R:q\notin T}o_{T,i}.                  \tag{3.2}
\]

Together these rows give the exact equivalence

\[
 a_{i,q}=1
 \quad\Longleftrightarrow\quad
 q\in\bigcap\{T:o_{T,i}=1\}.                                       \tag{3.3}
\]

The empty intersection is the full coordinate set.  Coordinate (c) is
omitted from the variables because (2.2) makes it always available.

For a local form (F=(T,[f,l],N)), let (\Sigma_F) be the exact endpoint
and immediate-exterior-neighbour signature asserting that the unique
(T)-run is ([f,l]).  For every (q\in N\setminus\{c}), impose

\[
        \Sigma_F\Longrightarrow\bigvee_{i=f}^{l}a_{i,q}.             \tag{3.4}
\]

If (c\in N), its durable row is automatic because the selected interval
is nonempty and every canonical cell contains (c).

## 4. Exact equivalence theorem

### Theorem 4.1 (joint13 canonical occupancy equivalence)

The CNF in Section 3 is satisfiable if and only if there is a literal
universal length-12,873 word obtained from (A) by changing an arbitrary
subset of the thirteen positions (S) to arbitrary nonzero 16-bit values.

#### Proof: supported word to CNF

Let (C) be such a universal word.  Every (T\in R) has no fixed-only
witness, so choose one actual (T)-interval.  By (2.1) it meets exactly one
editable block, and its editable intersection is one nonempty interval.
If its fixed base gives a dominated residual need, replace that base by an
undominated compatible base for the same editable intersection.  The new
need is a submask of the old need, so the unchanged editable cells still
supply it and the interval remains a literal (T)-witness.  Set the
corresponding occupancies and control.

Set (a_{i,q}) by the right side of (3.3).  If a selected (T)-witness uses
cell (i) and (q\notin T), then (a_{i,q}=0), proving (3.1); (3.2) is true
by construction.  Fix a selected local form with residual need (N).  Each
bit (q\in N) is supplied by some edited cell in its actual witness.  Every
selected target active at that cell contains (q), so (a_{i,q}=1).
Therefore (3.4) holds.  The run constraints are immediate.

#### Proof: CNF to supported word

Recover one local form for each target from its unique occupancy run.  At
cell (i), define

\[
 C_i=\bigcap\{T:o_{T,i}=1\},                                        \tag{4.1}
\]

using (C_i=\mathtt{0xffff}) if no target is active.  Leave every cell
outside (S) unchanged.  Equation (2.2) makes every active intersection in
(4.1) nonzero.  Equations (3.1)--(3.2) say that its noncommon coordinates
are exactly the true (a_{i,q}).

For a selected form ((T,[f,l],N)), every cell in ([f,l]) is a submask of
(T).  Equation (3.4) supplies every bit of (N\setminus\{c}); coordinate
(c), if needed, is supplied automatically.  Choose the fixed suffix/prefix
base that generated this exact minimal need.  Its OR with the canonical
cells is exactly (T).  Thus every (T\in R) has a literal interval.
Every target outside (R) retains its fixed-only interval, so (C) is
universal.  This proves both directions.  \(\square)

### Corollary 4.2 (precise WLOG boundary)

Inside the fixed support (S), replacing arbitrary feasible cell values by
the intersections (4.1) is WLOG.  It may change how many cells differ from
the source; hence the claim uses `budget=-1` and is not valid for a fixed
edit cardinality without an additional argument.

There is **no** theorem that moves an arbitrary global length-12,873 solution
into (S).  Nor are the portal cells forced to one of the 153 minimum-debt
one-edit values.  Imposing either condition would define only a sufficient
finite subclass.  The emitted model deliberately allows every canonical
value arising from an arbitrary simultaneous assignment on all thirteen
cells.

## 5. Exact model dimensions

The variable ledger is

| family | count |
|---|---:|
| occupancies (o_{T,i}) | (55\cdot13=715) |
| block controls (g_{T,b}) | (55\cdot4=220) |
| noncommon availabilities (a_{i,q}) | (13\cdot15=195) |
| **total** | **1,130** |

The clause ledger is

| family | count |
|---|---:|
| target ALO | 55 |
| occupancy-to-control | 715 |
| control AMO | 330 |
| one-run start AMO | 385 |
| omission forward (3.1) | 5,577 |
| canonical reverse (3.2) | 195 |
| durable rows (3.4) | 10,301 |
| **total** | **17,558** |

There are exactly 67,482 literals.  For comparison, directly removing the
irrelevant change indicators from the reference model and adding all 208
canonical cell rows gives 1,803 variables, 35,195 clauses, and 104,727
literals.  Occupancy compression is therefore exact and substantially
smaller; it is not a relaxation.

## 6. Frozen executable artifacts and status

```text
scratch/build_ad_k16_h1_fourportal_joint13_occupancy_20260730.py
SHA-256 c3f7946a6fffd919c17fa0b7a059d651e0cd2a8102417cb1a0e0ab4aa4d2f2a9

scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.cnf
SHA-256 251229383ec319a744fea37bd2f3f89bdf59e638727677166f0eaa7751ecd9bb

scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.map.json
SHA-256 f624e5684fe58c122d43371c16fbd4e1c8db9b9ae8a84930d3b9cf59a4758f31
payload SHA-256 4f163a37546364532807ef1767b33e3706e921587099d841954d262fe9974e08

scratch/decode_verify_ad_k16_h1_fourportal_joint13_occupancy_20260730.py
SHA-256 bd7a59635c6b37cec867619ed3c501d74428714da5b91feae8f58eef1b7bfc5c
```

The builder independently reconstructs source coverage, bases, needs, the
four atlas families, and the complete reference-map term sequence before
emitting anything.  The decoder accepts only a complete SAT assignment,
checks every clause, reconstructs (4.1), and performs a fresh literal
65,535-target replay before writing a candidate word.

Two solver-free independent audits are frozen:

```text
MATH_AUDIT_AD_K16_H1_FOURPORTAL_JOINT13_OCCUPANCY_INDEPENDENT_20260730.md
SHA-256 98502ef284f899e37e3a870a309382539294512f929edb60f7ba8edacd90e415

MATH_AUDIT_AD_K16_H1_FOURPORTAL_COMPACT_CROSSBUILD_20260730.md
SHA-256 039464bfb4acd1e432443c520031ecef6456e46b1b7b9cf0e4058580c145bb60
```

The first reconstructs this CNF in exact ordered form from the separate
geometry ledger.  The second compares it with an independently emitted
equivalent CNF under within-clause literal canonicalization; both give the
canonical clause-stream SHA-256
`7229e349e6d5dd338b6d119d3d34d28a50ca0ffcb812df39500929dafaba0893`.

No SAT solver was launched for this model.  Its exact status is
**UNSOLVED/UNKNOWN**.  In particular, the CNF is neither a K16 solution nor
an UNSAT certificate and does not alter the authenticated bracket
\(12873\le\nu(16)\le12874\).
