# `k=17` marker58 quotient residence blockers and frozen round-one CNF

Date: 2026-08-02  
Status: exact finite extraction and byte-replayed CNF.  No solver was
launched.  In arbitrary non-equivariant factors the clauses enforce strong
cyclic residence, but for the intended connected `Z_17`-equivariant subclass
that condition is equivalent to the existence of a depth-three-resident
linear opening.  The quantifier distinction is proved below.

## 1. Run-one exclusion follows from the q1 rainbow

### Lemma 1.1 — facet repetition from a singleton run

Let

\[
T_{i-1},T_i,T_{i+1}
\]

be three consecutive rank-`r` vertices of a simple Johnson chronology.  If a
coordinate `x` is absent from `T_(i-1)`, present in `T_i`, and absent from
`T_(i+1)`, then the two adjacent lower q1 colours are equal:

\[
T_{i-1}\cap T_i=T_i-\{x\}=T_i\cap T_{i+1}.
\]

#### Proof

The first Johnson transition inserts `x`.  Since both sets have rank `r`, it
deletes one coordinate and therefore

\[
T_{i-1}\cap T_i=T_i-\{x\}.
\]

The next transition removes `x`; hence its rank-`r-1` intersection is again
`T_i-{x}`.  QED.

### Corollary 1.2

Any chronology whose adjacent intersections are pairwise distinct has no
cyclic coordinate run of length one.  Thus, for depth three, its only cyclic
residence defects are runs of lengths two and three.

This explains the exact zero run-one count in the connected marker58 host
without appealing to the particular search history.

## 2. Exact local blocker lemma

Let coordinate `x` have a cyclic run of length `ell in {2,3}` on owners

\[
T_s,T_{s+1},\ldots,T_{s+\ell-1}.
\]

Include the entering edge, the `ell-1` internal edges, and the leaving edge;
call this `ell+1`-edge segment `E(R)`.

### Lemma 2.1 — forced-segment blocker

In any degree-two factor retaining every edge of `E(R)`, those owners remain
consecutive with the same coordinate trace, and therefore retain the same
length-`ell` cyclic run.

#### Proof

Every internal owner of the displayed segment is incident with its two
displayed neighbouring edges.  Degree two leaves it no alternative incidence.
The two run-end owners likewise retain their internal edge and their entering
or leaving edge.  Hence the whole local path segment is forced, up to reversal.
Membership of `x` is a property of the fixed owner masks, so its trace on that
forced segment is unchanged.  QED.

Suppose some edges of `E(R)` are protected and fixed, while the remaining
edges are selected quotient options with primary variables `x_e`.  Every
strong cyclic-resident completion must satisfy

\[
\bigvee_{e\in E(R)\setminus P}\neg x_e.                 \tag{2.1}
\]

If every edge is fixed, the protected bank itself has an unconditional cyclic
residence obstruction.

## 3. Why the blockers are necessary in the connected quotient class

In an arbitrary factor, clause (2.1) need not be necessary for the weaker
condition

> there exists one cut after which every internal positive run has length at
> least four.

A retained short cyclic run is legal when the chosen cut lies inside it or on
one of its two flanking edges.  An exact linear-residence encoding requires a
physical cut selector `y_c` and the guarded clause

\[
\left(\bigvee_{e\in E(R)\setminus P}\neg x_e\right)
\vee
\left(\bigvee_{c\in E(R)}y_c\right),                   \tag{3.1}
\]

together with exactly one selected cut.

The current quotient class has additional symmetry which collapses that
distinction.

### Theorem 3.1 — equivariant cut-orbit obstruction

Let a `Z_17`-equivariant degree-two factor on the physical rank-nine owner
layer be connected.  Then it has a depth-three-resident linear opening if and
only if every cyclic coordinate run has length at least four.

#### Proof

The connected factor is a cycle of length

\[
24310=17\cdot1430.
\]

The coordinate rotation generator acts as an automorphism of this cycle.  An
automorphism of odd order cannot be a reflection, so it is a cycle rotation.
The `Z_17` action on rank-nine owners is free; therefore this rotation is
nontrivial and has order seventeen.  Its edge orbits consist of seventeen
edges spaced 1,430 positions apart around the physical cycle.

If a coordinate has a cyclic run of length `ell<=3`, rotating coordinates
produces seventeen translated runs.  The set of cuts which boundary-truncate
one such run consists of its `ell+1<=4` segment edges.  The seventeen
translated cut sets are disjoint because their spacing is 1,430.  One linear
cut cannot hit all seventeen, so at least sixteen translated short runs remain
internal.  No depth-three-resident opening exists.

Conversely, if every cyclic positive run has length at least four, every
linear cut has all internal positive runs of length at least four.  The maximal
depth-three erosion therefore restores the carrier.  QED.

### Corollary 3.2

For the target class—connected, `Z_17`-equivariant completions containing the
protected marker bank—every clause (2.1) is a sound necessary condition for
linear depth-three residence.  A factor retaining that local quotient segment
retains all seventeen translated short runs and cannot be repaired by its
choice of opening.

The connectivity requirement remains part of the theorem's scope.  The
clauses may exclude disconnected equivariant factors which are irrelevant to
the desired one-cycle host.  UNSAT of a formula containing these clauses can
refute the connected equivariant marker58 host class, but not non-equivariant
hosts and certainly not `nu(17)=B(17)`.

## 4. Literal extraction from the connected factor

The extractor independently binds every unprotected physical factor edge to
its selected quotient variable by developing all seventeen rotations.  For
every physical short run it records the three/four forced edges, removes fixed
protected edges, sorts the remaining primary variables, and deduplicates the
resulting clause.

The complete result is

```text
physical length-2 runs               2873
physical length-3 runs               2499
physical short runs                  5372
unique Z17 quotient blocker clauses   316
translation orbits of size 17         316
all-fixed short runs                     0
```

The quotient run census is `169` length-two and `147` length-three motifs.
Every blocker has exactly seventeen physical occurrences, giving an
independent check that translate deduplication lost nothing.

After omitting fixed edges, clause arities are

| arity | clauses |
|---:|---:|
| 1 | 37 |
| 2 | 15 |
| 3 | 149 |
| 4 | 115 |

There is no all-fixed obstruction, but the 37 unit clauses show that many
short runs are supported by all but one protected edge and force a specific
residual option to change in the cyclic-resident subclass.

The physical fixed-edge histogram is

| fixed edges on run segment | physical runs |
|---:|---:|
| 0 | 4301 |
| 1 | 323 |
| 2 | 510 |
| 3 | 238 |

The counts sum to 5,372.  A length-three segment has at most four edges; the
absence of an all-fixed row is checked separately rather than inferred from
this aggregate table.

## 5. Frozen round-one CNF

The hardened quotient builder was run with:

* the two sound component cuts extracted from the original three-cycle
  `c68b` factor;
* the 316 strong cyclic-residence clauses above;
* no zero-voltage model block.

The resulting census is

```text
variables                 204167
base clauses              439145
component-cut clauses          2
residence clauses             316
round-one clauses          439463
```

An independent C++ audit verifies that:

1. the first 439,145 clauses agree clause-for-clause with the frozen base CNF;
2. the next two clauses are exactly the option orbits crossing the named
   owner-component cuts, and no fixed edge crosses either cut;
3. the final 316 clauses agree clause-for-clause with the extracted blocker
   file;
4. every blocker literal is a negative primary variable in `1..35713`;
5. the header and all clause/arity counts are exact.

No SAT, UNSAT, chronology, or universal-word claim is attached to round one.

## 6. Frozen artifacts

```text
3dfcde2acb3650121da7a7502bf9a2707c98e9e7b3f61e74b10c764c3bca2acc
  scratch/extract_k17_marker58_quotient_residence_blockers_20260802.cpp
c878f23549e8ea49c6a87c36a1b49036cda30a2107cc98c9b48120ea7340927c
  scratch/audit_k17_marker58_residence_round1_cnf_20260802.cpp
9948bd6152774219b93adf7f5476929ad6e1a8a4338b9ddd38504ce47eaf3e51
  scratch/k17_marker58_residence_round1_20260802/c68b.double_fusion.residence_blocks.cnf
1b71ddf70e6423f91f011006f656772c8ab03bf73b6d84b67254ba6022e25b79
  scratch/k17_marker58_residence_round1_20260802/c68b.double_fusion.residence_block_occurrences.tsv
5c448fb9ab7ce631f2a19c007c5570a5efee1112cbc42e3b2ce27aaf61cb64d0
  scratch/k17_marker58_residence_round1_20260802/c68b.double_fusion.residence_blocks.audit.json
c6638107ba4d1241403f914b5893614d9660a48cde7e43bef495b5fe28ebed52
  scratch/k17_marker58_residence_round1_20260802/marker58_residence_round1.cnf
7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
  scratch/k17_marker58_residence_round1_20260802/marker58_residence_round1.map.tsv
b9e8ed25eae7ccf43500761ffb9abb4e717ffceb2e72482b48a2eb9cc562ec93
  scratch/k17_marker58_residence_round1_20260802/marker58_residence_round1.audit.json
```

H100 audit root:

```text
/home/amodo/or15/work/audit_quotient_k17_marker58_20260802
```
