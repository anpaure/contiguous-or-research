# K16 tail-fixed state2: upper-complete chronology fails the lower compiler by a singleton Hall core

**Date:** 2026-07-30  
**Status:** exact solver-free no-go for one frozen variable-depth chronology

## 1. Verdict

Let `T` be the length-12,873 rank-eight chronology

```text
scratch/k16_state2_tailfixed_3opt_uppercomplete_20260730/best_targets.txt
SHA-256 9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b
```

and let `E` be its frozen maximal source envelope

```text
scratch/k16_state2_tailfixed_3opt_uppercomplete_20260730/best_envelope.word
SHA-256 57669ee5934872f766cdd1666f5a418d6710040f1edafe2c59f2d8ddf146b54a
```

The chronology is G0, contains every rank-eight target, and its arbitrary
interval unions contain every target of ranks 9 through 16.  Nevertheless it
cannot be compiled to a nonzero physical source word covering all lower
targets.  The rank-seven target

\[
 S=19569=\mathtt{0x4c71}
\]

has no admissible proper-prefix occurrence cell.  Thus the exact candidate
graph has the singleton Hall core

\[
 \{S\}\longmapsto\varnothing,
 \qquad |\{S\}|-|N(\{S\})|=1.
\]

No SAT/CP solve is needed.  This proves infeasibility only for this frozen
chronology and its forced exact-envelope compiler; it is not an unrestricted
K16 no-go.

## 2. Forced variable-depth geometry

The three adjacent repeated middle rows start at positions

```text
3322:  0x4e71,0x4e71
12869: 0xcc63,0xcc63
12871: 0xce61,0xce61.
```

Consequently the remaining first-delivery depth at start `i` is

```text
depth 3: 3323 starts
depth 2: 9547 starts
depth 1: 2 starts
depth 0: 1 start.
```

The scalar proper-prefix capacity is therefore

\[
 3(3323)+2(9547)+1(2)=29065.
\]

For each source position `p`, define its maximal envelope

\[
 E_p=\bigcap_{i:\ i\le p\le i+d_i}T_i.
\]

Independent reconstruction gives no empty envelope and reproduces the frozen
envelope byte for byte.  It also verifies

\[
 T_i=\bigcup_{p=i}^{i+d_i}E_p
\]

for every one of the 12,873 middle rows.  There are 102,984 individual
middle-bit carrier requirements.  The envelope rank histogram is

```text
rank 3: 3
rank 5: 3321
rank 6: 9544
rank 7: 3
rank 8: 2.
```

The complete middle deck has exactly the expected three flat excess rows,
and a direct interval-OR replay of `T` has zero upper holes.

## 3. Exact lower candidate criterion

A lower occurrence beginning at `i` must be a proper prefix

\[
 J=(i,\ell),\qquad 1\le\ell\le d_i,
\]

because the union through position `i+d_i` already has rank eight and OR is
monotone.  These are exactly the 29,065 right vertices used below, ordered by
start and then increasing length.

Put

\[
 U_J=\bigcup_{p\in J}E_p.
\]

For every required middle incidence `(i,b)`, let its possible carrier
positions be

\[
 C_{i,b}=\{p\in[i,i+d_i]:b\in E_p\}.
\]

Define `M_J` to contain `b` whenever some nonempty `C_(i,b)` lies wholly in
`J`.  If a source interval `J` is forced to have OR exactly `R`, then `R` is
individually realizable precisely when

\[
 R\subseteq U_J,
 \qquad M_J\subseteq R,
 \qquad E_p\cap R\ne\varnothing\quad(p\in J).       \tag{3.1}
\]

The first condition says no requested bit lies outside the maximal interval
envelope.  The second prevents erasing the last carrier of a required middle
bit.  The third permits every physical source cell in `J` to remain nonzero.
Sufficiency follows by assigning `A_p=E_p cap R` on `J` and maximal values
elsewhere.

The audit constructs `M_J` directly from all 102,984 carrier rows; it does
not import the production COMP3 implementation.

## 4. Singleton Hall obstruction

For `S=0x4c71`, exhaustive replay classifies every proper-prefix cell.  In
all 29,065 cases already

\[
 S\not\subseteq U_J.                               \tag{4.1}
\]

The exact failure-signature census is

```text
S not subset U_J only                                      3,889
S not subset U_J + mandatory bit outside S                24,498
S not subset U_J + mandatory bit outside S + empty cell      678
                                                        --------
                                                          29,065.
```

Thus no interval passes (3.1), so `N({S})` is empty.  Any lower-universal
physical source would need an occurrence cell for every lower target; in
particular it would induce a map from `{S}` into `N({S})`.  The cardinality
inequality `1>0` is the required Hall contradiction.

As a broader cross-check, independent enumeration of every ranks-1-through-7
candidate incidence gives

```text
lower targets:       26,332
candidate incidences: 361,816
zero-candidate targets: exactly [19569].
```

Hence the singleton is not sampled from a partial target list: it is the sole
zero-degree lower vertex in the complete candidate graph.

## 5. Scope

This no-go closes the lower compiler gate for the authenticated tail-fixed
pattern-4 three-opt chronology.  Its upper layer is already complete, but
upper completion is not the only remaining gate: lower target `0x4c71`
cannot occur in any allowed physical prefix.

The theorem does not exclude another reordering, another defect staircase,
larger length, or an unrestricted length-12,873 K16 word.  It also makes no
claim about the earlier state2 chronology with two upper holes.

## 6. Audited artifacts

```text
scratch/audit_k16_resident_state2_variable_comp3_outcome_20260730.py

scratch/k16_state2_tailfixed_3opt_uppercomplete_20260730/
  lower_hall_singleton_4c71.core.json
  lower_hall_singleton_4c71.independent.audit.json
  lower_comp3_static_independent.audit.json
```

The checker is solver-free.  It authenticates both frozen input hashes,
reconstructs the full geometry, verifies middle and upper coverage, enumerates
the complete candidate graph, recomputes the claimed Hall neighbor set, and
checks the deficiency.  Both audit payload hashes are post-load reproducible.
