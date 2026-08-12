# Thread D: candidate29 compound-circuit gate at `k=17`

Date: 2026-08-01  
Status: exact finite theorem on the frozen connected debt-two factor.  All
simple one-side circuits through assignment support `13`; all terminal-valid
simultaneous raw `H-C6`/`D-C6` pairs; every state-relative same-side
two-C6 composition; both phase-loop/C6 orientations; and both mixed C6/C10
orientations are exhausted and independently replayed.  Opposite-base atoms,
pair rescue, owner/facet overlap, and literal phase residues are included.
The statement concerns only the two immediate turn palettes, quotient
connectedness, and `Z17` voltage.  It makes no claim about residence, deeper
shadows, opening, or the compiler.

## 0. Frozen state

The input is

```text
scratch/threadD_k17_connected_debt2_repair_20260801/
  second_final.minimum_debt_second_B.factor.tsv
SHA256 aed64bc32992d65f77c4a0bcbcf9189f88d3d835295df517e8ca29f46595fb8a
```

It is candidate `29`, the current-relative `D-C14`

```text
owners    390,116,738,267,214,209,396
old edges 3513,1048,6650,2406,1928,1886,3571
new edges 3510,1049,6647,2409,1931,1884,3568.
```

Let `D,H:O->F` be its two literal incidence perfect matchings on
`|O|=|F|=1430`, and put

\[
                              \pi=H^{-1}D.                    \tag{0.1}
\]

Literal replay gives one quotient `1430`-cycle of voltage `3 mod 17`, hence
one physical `24310`-cycle.  The upper rank-ten and lower rank-seven turn
loads are respectively

\[
 \mu_+:0^1 1^{879}2^{243}3^{19}4^2,
 \qquad
 \mu_-:0^1 1^{877}2^{246}3^{19}4^1,             \tag{0.2}
\]

with unique holes

\[
                         u=0x0355f,
 \qquad                 \ell=0x0062f.                         \tag{0.3}
\]

Thus a terminal repair is not a marginal improvement: it must make both
loads positive while losing no currently unique turn colour.

The independent input and provider audit is

```text
scratch/threadD_k17_connected_debt2_repair_20260801/
  candidate29_provider_independent.audit.json
SHA256 704fd34e7e00e62a6ffd79831297cee0adab3d844c7020ae44144521e1dc238f
```

## 1. Exact compound algebra

An `H` assignment arc `x->y` is a literal incidence from owner `x` to the
facet currently occupied by `H(y)`; a `D` assignment arc is defined
analogously.  A directed simple `t`-cycle gives endpoint permutations
`beta` on `H` or `alpha` on `D`.  For simultaneous changes,

\[
                  D'=D\alpha,\qquad H'=H\beta,
 \qquad            \pi'=\beta^{-1}\pi\alpha.                  \tag{1.1}
\]

Equation (1.1) is an endpoint identity only.  Literal incidence labels are
retained separately, because parallel labels have different voltage and may
give different aligned turns.

### Theorem 1.1 (terminal iff test)

A compound change is a physical immediate-palette repair if and only if:

1. the final literal `D'` and `H'` are perfect matchings and are mutually
   incidence-disjoint;
2. `beta^{-1} pi alpha` is one quotient cycle;
3. direct traversal of its literal incidences has nonzero voltage modulo
   `17`; and
4. after recomputing all `1430` owner intersections and all `1430` facet
   unions from `(D',H')`, every rank-seven and rank-ten target has positive
   multiplicity.

#### Proof

Perfectness and disjointness are exactly the condition that the two selected
incidence sets form an alternating two-factor.  Its contracted owner
successor is (1.1).  A single quotient cycle has one physical lift exactly
when its voltage generates `Z17`, equivalently when the voltage is nonzero.
The two immediate palettes are, by definition, the aligned intersections at
owners and aligned unions at facets.  Recounting those terminal turns is
therefore necessary and sufficient for palette completeness.  \(\square\)

The final recount in condition 4 is essential.  If both sides change at an
owner or facet, the correct contribution is the single final turn.  If
`L(d,h)` denotes a lower turn, the mixed correction relative to isolated
columns is

\[
 [L(d_1,h_1)]-[L(d_1,h_0)]-[L(d_0,h_1)]+[L(d_0,h_0)],          \tag{1.2}
\]

and there is an identical four-term formula for upper turns.  Consequently
isolated switch ledgers cannot be added across overlapping supports.

Taking signs in (1.1), a Hamilton-to-Hamilton pair of simple cycles of
lengths `p,q` must satisfy

\[
                              p+q\equiv0\pmod2.                \tag{1.3}
\]

This is only a necessary parity row, not a substitute for (1.1).

## 2. Provider-gap lemma

On each of the `D` and `H` assignment graphs there are exactly ten literal
providers for `u` and ten for `ell`.  Every provider changes its endpoint,
and no incidence provides both holes.  More sharply, writing `t(P),h(P)`
for an assignment arc's tail and head,

\[
\begin{aligned}
 h(P^-)&\cap t(P^+)=\varnothing,\\
 h(P^+)&\cap t(P^-)=\varnothing                         \tag{2.1}
\end{aligned}
\]

on both sides.

### Lemma 2.1

No one-side `C6` can contain providers for both holes.  The first simple
one-side circuit permitted by the provider incidence alone is `C10`; its
two numbers of intervening nonprovider arcs must be `(1,2)` or `(2,1)`.

#### Proof

Two distinguished arcs in a directed `t`-cycle leave `t-2` other arcs,
split between the two directed gaps.  For `t=3`, one gap is empty, forcing
one provider head to equal the other provider tail, contrary to (2.1).  If
both gaps are nonempty, then `t>=5`; at `t=5` the positive parts of `3` are
exactly `(1,2)` and `(2,1)`.  \(\square\)

The literal audit is

```text
scratch/audit_threadD_k17_candidate29_provider_gap_20260801.py
SHA256 18df5e6cd1f2172ef6c7ff921bc29dcc9c348a2894134ad6d4f0f1b23b29016a

scratch/threadD_k17_candidate29_compound_repair_20260801/
  candidate29_provider_gap.audit.json
SHA256 e0acadbd29f9a1f7c111ca8bc1ea1a0ca860558c1463f4efea3712b783defaf2
```

## 3. Complete one-side shells through `C26`

For a single changed side, Hamilton parity forces odd assignment support.
Every terminal repair must contain one provider of each type.  Hence rooting
the search at the smaller provider bank, demanding the other provider, and
retaining only the rotation whose root provider has minimum literal ID is a
complete transversal of all potentially repairing simple circuits.

The exact H100 census gives:

| side | support `t` | targeted circuits | connected, nonzero | upper-safe | lower-safe | both-safe | minimum total holes |
|:---:|---:|---:|---:|---:|---:|---:|---:|
| H | 3 | 0 | 0 | 0 | 0 | 0 | - |
| H | 5 | 0 | 0 | 0 | 0 | 0 | - |
| H | 7 | 0 | 0 | 0 | 0 | 0 | - |
| H | 9 | 143 | 22 | 0 | 0 | 0 | 6 |
| H | 11 | 11,162 | 2,097 | 4 | 0 | 0 | 4 |
| H | 13 | 717,148 | 115,723 | 51 | 0 | 0 | 3 |
| D | 3 | 0 | 0 | 0 | 0 | 0 | - |
| D | 5 | 1 | 1 | 0 | 1 | 0 | 4 |
| D | 7 | 5 | 4 | 1 | 0 | 0 | 2 |
| D | 9 | 373 | 71 | 0 | 3 | 0 | 3 |
| D | 11 | 23,678 | 4,133 | 3 | 6 | 0 | 3 |
| D | 13 | 1,324,427 | 193,753 | 53 | 71 | 0 | 2 |

The `C6` atom census, performed without provider filtering, has `387` valid
`H` atoms and `394` valid `D` atoms; none is upper-safe or lower-safe.
Therefore no simple one-side circuit through assignment support `13`
repairs candidate29.  The first untested simple one-side shell is support
`15`, i.e. bipartite `C30`.

The producer source and compact frozen outputs are

```text
scratch/threadD_k17_candidate29_compound_repair_20260801/
  catalogue_candidate29_compound_repair.cpp
SHA256 26b5430ebb761fcaf19738584cdeb51629714dd5946acf03919b4bf336240994

  single_11_13.audit.json
SHA256 06b08782ef19662cc84e49270e5e99900b76589530c52f00dac2a8a750775ecb

  single_11_13.summary.tsv
SHA256 3c2849561e932213552ccb1962cb99dce3248f2318a1ee005cb6cbad34e2125a

  single_11_13.targeted_odd.tsv.gz
SHA256 56880a8882c04e407254312bb8adc7814d91712b5e6bdf8253ba4715038d4761
```

The `C22/C26` run exited normally after `14:03.63`, used `7,168 KiB`
maximum RSS under a `2 GiB` cap, and is therefore an exact finite result, not
a timeout inference.

An independent C++ implementation regenerated all `781` C6 atoms and
streamed/replayed all `315,804` emitted connected nonzero-voltage rows.  It
recomputed literal bindings, local tickets, all `1430+1430` terminal turns,
topology, voltage, and safe flags without importing the producer evaluator:

```text
scratch/threadD_k17_candidate29_one_side_independent_20260801/
  audit_candidate29_one_side_independent.cpp
SHA256 c0bb91a223adb7bce4ba6c0daafeac1537c98097627ce74381c5d3f8a88e88cc

  audit.json
SHA256 174a20ce2ff3faf36776ae1e3c39ddd4b9789258c7eb33708aa230329b6e8e16
```

The independent replay found `112` upper-safe and `81` lower-safe targeted
rows, with empty intersection in every support/side stratum.  It exited
normally after `1:59.94`, using `9,728 KiB` maximum RSS.

## 4. Complete simultaneous raw `H-C6`/`D-C6` theorem

It is unsound to cross only atoms which are individually valid.  A raw
same-side atom may temporarily select the opposite base edge yet become
legal when the opposite atom moves that edge simultaneously.  The complete
enumerator therefore:

1. retains every literal nonloop assignment arc, including opposite-base
   arcs;
2. enumerates every simple directed triangle and deduplicates by its complete
   terminal owner-to-incidence map;
3. takes the full Cartesian product of the two side banks;
4. rejects only after constructing the final two matchings; and
5. applies Theorem 1.1 to that terminal state.

### Theorem 4.1 (pair-rescued `C6 x C6` no-go)

On candidate29 the raw banks contain `621` distinct `H-C6` terminal maps and
`626` distinct `D-C6` terminal maps.  Of their `388,746` ordered pairs,
`152,809` are terminal-valid.  Exactly `441` are pair-rescued, including
`70` in which both isolated atoms are invalid.  Among all terminal-valid
pairs:

* `43,555` are quotient-connected;
* `42,881` are connected with nonzero voltage;
* zero preserve the upper palette;
* zero preserve the lower palette; and therefore
* zero repair both palettes.

The minimum connected nonzero debt remains two.  Thus the no-go is stronger
than a topology obstruction: no terminal-valid paired atom reaches even one
complete shore.

#### Proof

Every raw simple C6 on a fixed side is exactly a directed triangle in that
side's assignment graph, so steps 1--2 exhaust the side terminal maps.
Different sides change different matching vectors, hence their complete
compound domain is their Cartesian product.  Terminal disjointness is the
only validity condition which can rescue an opposite-base raw atom.  The
remaining tests are the necessary-and-sufficient tests of Theorem 1.1.
The displayed counts and zero safe rows are reproduced by two independent
literal implementations.  \(\square\)

Primary certificate:

```text
scratch/threadD_k17_candidate29_compound_repair_20260801/
  paired_c6_rescued.frozen.source.cpp
SHA256 bbc95c3d3b2776e06f10f68e702255e9ce385dfc78c3e6d057593a88008c6248

  paired_c6_rescued.terminal_valid_paired_c6.audit.json
SHA256 d72d38c87066c6792dd42bb54ecadcb514e4f4c4342bb5fbdcad129546dbfe0f

  paired_c6_rescued.terminal_valid_pairs.tsv.gz
SHA256 08292e3b10980d2310c651bbef1d63de4558525595d931e533ff783b1229572a
```

Independent certificate:

```text
scratch/threadD_k17_candidate29_pair_rescued_independent_20260801/
  audit_candidate29_pair_rescued_independent.cpp
SHA256 46506f653ad125e8734b82c04cd5c8ed2af5b826958e4335cbc2d0ef865319f3

  audit.json
SHA256 2ddadeab8e953ee93111622bfa59594e9b0efe102d1b8bf58a5086d2bebdf41a
```

The primary run used `15,360 KiB` maximum RSS and `32.15 s`; the independent
run used `9,728 KiB` and `43.31 s`.  Both ran as one O3 H100 CPU process and
exited normally under `2 GiB`.

## 5. Complete phase-loop/C6 theorem

The full parallel-incidence audit finds no `H` phase loop and one `D` phase
loop,

\[
       (owner,facet)=(425,295),\qquad 3825\longrightarrow3829.              \tag{5.1}
\]

Alone, (5.1) preserves endpoints, changes voltage from `3` to `11`, and
leaves the two holes.  Crossing it with all `621` raw `H-C6` terminal maps
gives `387` terminal-valid rows, `179` connected rows, and `177` connected
nonzero-voltage rows.  Zero are upper-safe, zero are lower-safe, and zero
repair both palettes.  The minimum debt is still two.

There is exactly one owner-overlap row and one different facet-overlap row.
Both are disconnected and both retain the original two holes, so the only
nonlinear overlap representatives do not hide a terminal repair.

Primary and independent artifacts are

```text
scratch/threadD_k17_candidate29_compound_repair_20260801/
  phase_c6.frozen.source.cpp
SHA256 b2bc007d1ee5de6fcbb7061864fe061e79aff962d43cf2fdf7c94cf93a89f5e5

  phase_c6.phase_c6_rescued.audit.json
SHA256 e81be0fa0356a1becc68b174835c315982d3761b73cb7edc7d059b9d241bde01

  phase_c6.independent.audit.json
SHA256 1efe2dd3f9ad25d14205cf557f2330d6fb4e61692bbfdd9d105161f670abcf9e

scratch/audit_threadD_k17_candidate29_phase_c6_rescued_20260801.py
SHA256 0ceee012cce135bc43b4d7e276b7384ae7aaf90af552508eaff22a46507e39a9
```

## 6. Two sequential same-side C6 normal form

Let two state-relative 3-cycles have owner supports `A,B`.  The exact product
classification, including overwritten intermediate literals, is:

| `|A intersect B|` | terminal endpoint type | terminal class |
|---:|:---:|---|
| 0 | `(3)(3)` | disjoint C6+C6 |
| 1 | `(5)` | already a literal C10 |
| 2, aligned | `(2)(2)` | new interlacing double rectangle |
| 2, opposite | `(3)` plus one fixed owner | C6, possibly with one phase residue |
| 3, equal | `(3)` | already a literal C6 |
| 3, inverse | identity | at most three phase residues |

The key literal qualification is that an incidence installed by the first
C6 on `A intersect B` is overwritten by the second.  It may be an
opposite-matching incidence without invalidating the atomic terminal move.
Conversely a fixed endpoint in the product may retain a nonbase parallel
label, changing palettes and voltage despite having trivial endpoint delta.
Thus a complete enumeration must key by its full terminal incidence vector.

The classification and its `1,600`-product six-label audit are

```text
MATH_THEOREM_THREAD_D_TWO_SEQUENTIAL_C6_TERMINAL_NORMAL_FORM_20260801.md
SHA256 bc4c5c336b73ba795bc3b73d70bd9e419ec49a84f60e4ec4098d527247f871ca

scratch/audit_threadD_two_sequential_c6_normal_form_20260801.py
SHA256 43514ce9e0f73eb38008c7e9f5280ffe97ca9dca9f4b21b8f8fd63dace818940

scratch/threadD_k17_candidate29_compound_repair_20260801/
  two_sequential_c6_normal_form.audit.json
SHA256 558bd468c0c7235ec60c5a8651a6b270562358e08ca81df00632b8fcdace51c4
```

Accordingly, after the already closed direct C6/C10 and phase-only shells,
the genuinely new terminal types are the disjoint `(3)(3)` pair and the
aligned-overlap-two `(2)(2)` rectangle; the candidate's sole D phase also
leaves a small same-side phase+C6 residue bank.

The disjoint bank is already completely closed.  Among the `152,112`
unordered pairs of base-valid same-side C6 atoms, exactly `151,343` have
disjoint owner supports.  Direct terminal replay finds zero upper-safe and
zero lower-safe rows; the minimum debt remains two.  The `7:00` H100 run used
about `14 MiB` RSS.  Its certificates are

```text
scratch/threadD_k17_candidate29_compound_repair_20260801/
  catalogue_candidate29_same_side_disjoint_c6.cpp
SHA256 91e2eb4406a48e1b142fb57bab45e1bc486e9e11651cf30552f79b5f214e3e3a

  same_side_disjoint.disjoint_pairs.audit.json
SHA256 c60d732abbaa0a5a47ffb5759004ed54406aef1885aebe2f90bb5f799b41844f

  same_side_disjoint.disjoint_pairs.tsv
SHA256 8dab392c24dab926dc779ad96f9f566a6e2f4122c4adc9214b834d345cd89ad9
```

The complete state-relative census closes the overlap classes as well.  It
regenerates the second raw C6 after every first raw C6, permits an invalid
intermediate collision when the second switch overwrites it, and deduplicates
only complete terminal incidence maps.  Its exact ledger is:

```text
ordered state-relative histories                  777,751
terminal-valid histories                          306,066
terminal histories with invalid midpoint              934
unique terminal literal states                    153,411
unique rescue-only states                             439
unique states with disjoint history               151,343
support histogram              0^2 1^1 3^121 4^1 5^1943 6^151343
upper-safe states                                         0
lower-safe states                                         0
minimum total debt                                        2
```

Thus **every composition of two state-relative same-side C6 switches** is
closed, including all interlacing `(2)(2)` rectangles and every phase residue
reachable through overlapping C6 histories.  The primary run exited normally
after `3.87 s` with `33,252 KiB` maximum RSS:

```text
scratch/threadD_k17_candidate29_compound_repair_20260801/
  catalogue_candidate29_same_side_sequential_c6.cpp
SHA256 17d00068a1f29dd00f1ff9330fb4dcaec7fe90911b437148965ae10ff9fb1592

  same_side_sequential.sequential_c6.audit.json
SHA256 e8ff9a2557c2f77760aeb72cf652b2e16b4a158d6ab695a76ed027883cc3720b

  same_side_sequential.terminal_states.tsv
SHA256 05dd0cee56c24d4c1b1ede60837f74f01a8ca48d9a54184e08bc322d16bbf1bb
```

An independent atlas/regenerator reproduced all `777,751` histories, all
`153,411` literal terminal keys, the complete primary TSV, and the zero safe
counts.  It additionally replayed topology for every state, finding `43,883`
connected and `43,200` connected nonzero-voltage terminal states.  The sole
aligned-overlap-two rectangle is present and is not palette-safe.

```text
scratch/audit_threadD_k17_candidate29_same_side_sequential_independent_20260801.cpp
SHA256 933b8c6081c38df79602c9a37f66eeb5bf4512fe64b2dd4d0e67047028cc7f42

scratch/threadD_k17_candidate29_same_side_sequential_independent_20260801/
  independent.audit.json
SHA256 f951b1aae669b974782f6421035e3e224a706d1a02ca2647a5ff2190f3e7ef84
```

The independent H100 run exited normally in `20.33 s` with `27,648 KiB`
maximum RSS.

Finally, the explicit same-side phase+C6 bank is also closed.  There is no H
phase.  The unique D phase (5.1), crossed with all `626` raw D-C6 maps, has
`625` genuine outside-support compounds; `393` are terminal-valid, `189`
connected, and `184` connected with nonzero voltage.  Zero are upper-safe and
zero are lower-safe, with minimum debt two.  The sole overlap has
phase-then-C6 equal to the standalone C6, while C6-then-phase is
terminal-invalid.  The exact artifacts are

```text
scratch/threadD_k17_candidate29_compound_repair_20260801/
  catalogue_candidate29_same_side_phase_c6.cpp
SHA256 ac885919d315782c031cce0a3d253452f2c270318b06dd8e04d035564ba13298

  same_side_phase_c6.same_side_phase_c6.audit.json
SHA256 a9c12ca770ee6c09e72bf7e7a0eece81a71063855cd5103b410b6fa329e30e77

  same_side_phase_c6.same_side_phase_c6.tsv
SHA256 4599ffec29c651984e127560533c40dad30834b3491cedb47a1b6f7c70aac690
```

An independent atlas and literal replay reproduces all `627` persisted rows
and every headline count:

```text
scratch/audit_threadD_k17_candidate29_same_side_phase_c6_independent_20260801.cpp
SHA256 9a807cb19c6205801b6e8847cb18c9e41fdaf665cd0f89933b7c54b60570a0bd

scratch/threadD_k17_candidate29_same_side_sequential_independent_20260801/
  phase_independent.audit.json
SHA256 b69de7c7982adf8d77b43d351a2944022bb22fd0d50ffd906e5c94a2e20f67a6
```

It exited normally in `0.05 s` with `7,168 KiB` maximum RSS.

## 7. Complete mixed C6/C10 shell

The next mixed shell is

\[
            H\text{-C6}\times D\text{-C10}
 \quad\text{or}\quad
            H\text{-C10}\times D\text{-C6}.                  \tag{7.1}
\]

Its raw-bank completeness, pair-rescue criterion, independent owner/facet
cross terms, and sound mixed-provider clauses are proved in

```text
MATH_THEOREM_THREAD_D_MIXED_C6_C10_TERMINAL_COMPLETENESS_20260801.md
SHA256 ff8d99867ae363aed0ecb53152da0bfc7b61fc98f20eb1824a1cf0009d47235e

scratch/threadD_k17_candidate29_compound_repair_20260801/
  mixed_c6_c10_terminal_completeness.spec.json
SHA256 951d4f822fe0ce83a82342c1bb44b6fe821fa453d98d999fc3cbdf0f9db177c4
```

The important pruning correction is that lower cross rows are the owner
overlap, while upper cross rows are the independent facet overlap.  Hence a
hole may be supplied only by a mixed terminal incidence pair; requiring an
isolated one-side provider is incomplete.

The complete raw banks have sizes

\[
 |H_3|=621,\quad |D_3|=626,\quad |H_5|=8045,\quad |D_5|=8068. \tag{7.2}
\]

The exact terminal census is:

| orientation | Cartesian | terminal-valid | pair-rescued | connected/nonzero | upper-safe | lower-safe | both-safe | minimum connected debt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| H3 x D5 | 5,010,228 | 1,601,958 | 6,837 | 343,795 | 2 | 56 | 0 | 2 |
| H5 x D3 | 5,036,170 | 1,625,253 | 6,750 | 365,727 | 63 | 0 | 0 | 3 |

Thus all `10,046,398` raw pairs and all `3,227,211` terminal-valid pairs are
closed.  The primary O3 run took `22.34 s` and `8,704 KiB`; an independent
enumerator/replayer took `14.86 s` and `8,192 KiB` and again found empty
intersection of the two palette-safe sets.

```text
scratch/threadD_k17_candidate29_mixed_c6_c10_20260801/
  audit_candidate29_mixed_c6_c10.cpp
SHA256 1b4e5ef6ec94cd14456b23c7a475ea9b753a555c40bfaa36c8b13a94dc95dc0f

  mixed.audit.json
SHA256 f63f15733e132b2798bb6f55ddddb9d3b3be81c46e84ee7a98b4a0d631560461

  audit_candidate29_mixed_c6_c10_independent.cpp
SHA256 339f66a4314ffb21d390686164997f0dc5cae3c0fe74c38f9e38531fb5083a66

  independent.audit.json
SHA256 4ff185bb4388b7a1edd1218e9ad30e90361062693ccef43b8f39ba089c9e4dfe
```

## 8. Exact surviving gate

The following candidate29 classes are now closed:

* every simple one-side circuit through `C26`;
* every simultaneous terminal-valid raw `H-C6/D-C6` pair, including all
  overlap and pair-rescue terms; and
* the unique phase-loop crossed with every opposite-side or same-side raw
  C6; and
* every composition of two state-relative C6 switches on the same side; and
* both mixed C6/C10 orientations, with all pair-rescue and mixed-provider
  terms.

The immediate live classes are therefore:

1. the next mixed two-circuit shells, beginning with C6/C14 and C10/C10;
2. a single one-side circuit of assignment support at least `15` (`C30`);
   or
3. packets with three or more nontrivial assignment circuits.

Any such search must preserve the exact terminal discipline of Theorem 1.1.
In particular it must generate the second circuit state-relatively or key by
the complete terminal pair `(D',H')`; adding precomputed palette columns is
not proof-safe on overlaps.
