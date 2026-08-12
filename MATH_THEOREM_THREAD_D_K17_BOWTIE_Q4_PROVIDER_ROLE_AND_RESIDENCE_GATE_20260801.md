# `k=17`: the two bow-tie incidence-C8s are respectively role-neutral and nonresident

Date: 2026-08-01  
Lane: Thread D, one-copy coloured-Euler rounding  
Status: exact support-changing parity theorem; complete protected incidence-C8
census containing both bow-tie colours; literal path/state/provider replay; and
an exact provider-cone completeness lemma. This closes only a single-C8 repair
of the certified q1 bow tie. It does not exclude one-colour circuits, compound
circuits, recutting, the full resident q-port, deeper shadows, or the compiler.

## 1. Open reversal and incidence-C8 are different operations

For

\[
 V_0=K+x+z,\quad V_1=K+x+y,\quad
 V_2=K+y+w,\quad V_3=K+z+w,
\]

the open paths

\[
 V_1\to V_2\to V_3\to V_0,
 \qquad
 V_0\to V_3\to V_2\to V_1
\]

have the same undirected support. Their reversal current is

\[
 2(e_{V_1}-e_{V_0}),
\]

so a balanced reversal cannot fuse weak components. When completed inside a
directed one-factor, its relative successor permutation is even and component
parity is fixed.

The incidence-C8 switch is different. Put

\[
 L_i=K+p_i,qquad O_i=K+p_i+p_{i+1}\quad(i\bmod4).
\]

It replaces the four incidences

\[
 L_iO_{i-1}\longleftrightarrow L_iO_i.                 \tag{1.1}
\]

This changes undirected support. Cutting the four old incidences and recording
the residual fragments, (1.1) changes their endpoint pairing by a 4-cycle.
Hence the circuit-partition sign changes by

\[
 (-1)^{4-1}=-1.                                         \tag{1.2}
\]

Thus every legal incidence-C8 changes the number of components by an odd
integer. More generally a support-`q` incidence switch changes component-count
parity by `q-1 mod 2`. This is the genuine parity actuator; it must not be
identified with reversal of the open square.

## 2. Frozen bow-tie core

The exact zero/zero bank has lower colours

\[
 c=18782=0x495e,qquad d=19038=0x4a5e,qquad
 K=c\cap d=18526=0x485e.
\]

Its four core atoms are

\[
 x:A^+\to B^+\;(c),\quad z:B^-\to A^-\;(c),
\]

\[
 y:C^-\to B^+\;(d),\quad w:B^-\to C^+\;(d),           \tag{2.1}
\]

all with upper mask `19326`. The relevant endpoint owners are

\[
 a=18814,qquad b=19294,qquad c_0=19070.                \tag{2.2}
\]

The q1-CNF artifact numbers the three pieces `1330,7017,2538`. The literal
cycle-cut rebuild used below numbers the same endpoint states
`1331,7018,2539`; the one-step shift is only a builder enumeration convention.
The masks and four atoms in (2.1) agree literally.

## 3. Complete two-colour C8 census

Any incidence-C8 containing both `c=K+8` and `d=K+9` has core exactly `K`
and active labels `{8,9,s,t}`, where `s,t` are chosen from the other eight
labels outside `K`. Modulo dihedral symmetry there are three cyclic orders and
two phases. The complete number of oriented keys is therefore

\[
 {8\choose2}\cdot3\cdot2=168.                           \tag{3.1}
\]

A key is called **protected legal** when every old incidence belongs to the
frozen factor, every new incidence is absent, and no deleted incidence is
protected. Exact enumeration leaves precisely two keys:

| core | cyclic order | phase | numeric cut pattern | cut bits `i=0,1,2,3` |
|---:|---|---:|---:|---|
| 18526 | `(5,9,8,15)` | 1 | 7 | `1110` |
| 18526 | `(7,9,8,10)` | 1 | 6 | `0110` |

The convention is important: the integer is

\[
 \sum_{i=0}^3 2^i\,1_{L_i\text{ is cut}},               \tag{3.2}
\]

whereas the displayed string is read in the order `i=0,1,2,3`. Thus the first
row is integer `7` but displays `1110`; it is not a discrepancy with the usual
most-significant-bit rendering `0111`.

## 4. The residence-safe key fuses a factor component but not the bow tie

For `(5,9,8,15)`, phase 1, the exact four incidences are

| `i` | lower | cut | other owner | old owner | new owner |
|---:|---:|---:|---:|---:|---:|
| 0 | 18558 | 1 | 26750 | 51326 | 19070 |
| 1 | 19038 | 1 | 19166 | 19070 | 19294 |
| 2 | 18782 | 1 | 26974 | 19294 | 51550 |
| 3 | 51294 | 0 | 116830 | 51550 | 51326 |

Only the last incidence is internal to the selected cut forest. Its literal
rebuild affects two pieces, of owner lengths five and two, and both are
depth-3 resident. Every lower, tail, head, common-orientation and rank-ten
singleton row remains nonzero. The full factor component count changes

\[
 7\longrightarrow6,                                     \tag{4.1}
\]

with new component lengths

```text
22920,1362,18,4,3,3.
```

This realizes the odd parity change predicted by (1.2). The retained-internal
upper current is

\[
 +[116862]-[117086],                                     \tag{4.2}
\]

and creates no rank-ten hole.

The current (4.2) is nonzero. Thus the move preserves rank-ten **support** by
redundancy, but it does not preserve the named upper occurrence multiset. If
the coloured-Euler interface requires coefficientwise upper equality rather
than survival, this key is already inadmissible before the bow-tie test.

The exact q1 effect is subtler. No old `c` or `d` atom is removed, and exactly
two `c` atoms are added. If `D` denotes the new endpoint piece with owner
`51550`, they are

\[
 D^-\to B^+,qquad B^-\to D^+,                           \tag{4.3}
\]

both with lower `18782` and upper `52062`. Thus the `c` degree rises from two
to four, while the `d` degree remains two.

### Theorem 4.1 (socket-role obstruction)

Suppose every provider of colour `c` either enters the one incoming socket of
`B+` or leaves the one outgoing socket of `B-`, while colour `d` has precisely

\[
 C^-\to B^+,qquad B^-\to C^+.
\]

Then no common-orientation coloured cycle cover can choose one provider of
each colour, regardless of the number of `c` providers of the two displayed
roles.

#### Proof

If the selected `c` atom enters `B+`, it excludes `C- -> B+` by incoming
capacity, so `d` must use `B- -> C+`; the two selected atoms require opposite
orientations of `B`. If the selected `c` atom leaves `B-`, it excludes
`B- -> C+`, so `d` must use `C- -> B+`, with the same orientation
contradiction. These cases exhaust the `c` row. \(\square\)

The new atoms (4.3) have exactly these old roles. Hence this C8 genuinely
fuses a factor component and doubles the numerical `c` degree, but the q1
bow-tie contradiction survives unchanged.

## 5. The role-changing key is nonresident

For `(7,9,8,10)`, phase 1, the incidence table is

| `i` | lower | cut | other owner | old owner | new owner |
|---:|---:|---:|---:|---:|---:|
| 0 | 18654 | 0 | 84190 | 19678 | 19166 |
| 1 | 19038 | 1 | 19070 | 19166 | 19294 |
| 2 | 18782 | 1 | 26974 | 19294 | 19806 |
| 3 | 19550 | 0 | 20062 | 19806 | 19678 |

Ignoring residence for one line, its new endpoint `E=19806` would create four
new `c` atoms:

\[
 A^+\to E^+,quad E^-\to A^-,quad
 E^-\to B^+,quad B^-\to E^+.                            \tag{5.1}
\]

The first pair is genuinely `B`-free and would break Theorem 4.1's role
hypothesis. Their upper masks are respectively `19838` and `20318`.

But the literal rebuild has an affected 18-owner piece whose coordinate `3`
trace contains a bounded positive run starting at zero-based position seven
and having length exactly three. Depth-3 residence requires every bounded
positive run to have length at least four. Therefore this key is illegal. Its
full-factor topology is a split

\[
 7\longrightarrow8,                                     \tag{5.2}
\]

again having the odd parity change of (1.2), but it cannot enter the resident
one-copy model. Its raw internal upper current is also nonzero:

\[
 +[20190]-[20318]+[84702]-[85214].                       \tag{5.3}
\]

## 6. Exact scoped no-go

Among all 168 protected incidence-C8 keys containing both bow-tie colours:

1. the only resident/path-valid key adds providers but preserves their fatal
   `B` socket roles; and
2. the only key creating a `B`-free provider has an exact internal length-3
   residence defect.

Consequently no single protected incidence-C8 containing both `c` and `d`
repairs the fixed bow tie while preserving the current depth-3 cut forest.
Under exact named-upper occurrence preservation, the first key is excluded
independently by (4.2), so there is likewise no single two-colour C8 fusion on
that stricter coloured-Euler face.

This is not a no-go for:

* an incidence-C8 containing only one of the two colours;
* two overlapping or interlacing C8s whose joint rebuild removes the short
  run or changes the `B` roles;
* a C6/C10 or full resident q-port packet;
* a changed cut bank; or
* any downstream rank-11--17, topology, voltage, or compiler condition.

## 7. Completeness of the provider-cone prefilter

For a target lower colour `l`, let `P_l` be the baseline pieces containing an
owner `U` with `l subseteq U`. The broad census retains a move whenever one of
its affected baseline pieces lies in `P_c union P_d`.

### Lemma 7.1 (provider-cone lemma)

If a literal cut-forest move changes the set of q1 providers of `c` or `d`,
then it affects a piece in `P_c union P_d`. This remains true when the target
colour degree is unchanged because one provider is removed and another is
added.

#### Proof

A provider of `l` joins endpoint owners `U,V` with

\[
 U\cap V=l.
\]

Hence both endpoint owners contain `l`. If a provider is added or removed,
at least one of its endpoint states changes; otherwise its two endpoints and
the exact residence predicate are unchanged. The changed state belongs to an
affected piece and its endpoint owner contains `l`. Owner vertices themselves
are never created or deleted by the incidence switch, so the baseline piece
containing that owner lies in `P_l` and is one of the pieces collected for the
literal rebuild. Thus the prefilter retains the move.

If every toggled lower is already a cut, the path decomposition and all
endpoint states are unchanged, so the q1 provider set is unchanged as well.
This proves the omitted case and the lemma. \(\square\)

The extra explicit test for the central `B` piece is harmless and useful for
role diagnostics, but it is not needed to make provider-set changes complete.

## 8. Reproducibility and scope

Focused source:

```text
scratch/audit_threadD_k17_bowtie_two_q4_keys_20260801.cpp
SHA-256 21503e8d88a3f7023b3feda043ac8ef9ca93c4b590dd14582fba8f4c739d3a42
```

Focused output:

```text
scratch/threadD_k17_zerozero_bowtie_q4_20260801/two_keys.audit.tsv
SHA-256 b8e55eb3a6fb9a25243d347ad13553c1d5022fcc0ba5177bc63deb251c4264b5
```

Inputs:

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA-256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
scratch/k17_dense_refinement_zerozero_bank_20260801.tsv
SHA-256 5b4fe2d1a0125ea25f6fbb4b9259a6d2ee2007cd4ba55ac0aa4a6f23aa6bad8f
```

The executable checks the 168-key count and the two-key protected census,
rebuilds every affected path, regenerates the complete `c/d` seam atom set,
checks the internal residence traces, and recomputes full-factor components
and rank-ten singleton survival. It does not solve the complete q1 CNF after a
move; Theorem 4.1 proves directly that the sole resident candidate still
contains the fatal local core.
