# K16 external reserves: new-allele theorem and six-component return gate

Date: 2026-07-30

Status: three exact advances and one exact open finite model.  No
length-12,873 word is constructed.  The global bracket remains

\[
                 12873\le \nu(16)\le12874.
\]

The claims below are source-relative to the named length-12,873 one-hole
words.  Every position is zero-based.

## 1. Frozen lineage and comparison with the closed 54-position bank

Put

\[
 H=\mathtt{2c6d},\qquad P=\mathtt{4879},\qquad Q=\mathtt{6879}.
\]

The three authenticated `H` words used here are

| state | file | SHA-256 | sole hole |
|---|---|---|---|
| canonical `C` | `scratch/k16_upper12874_best_delete.word` | `a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649` | `H` |
| distance-1620 `R` | `scratch/rex3_final_fwd_h11373.word` | `b6ed242d0f098f8511d31027b2d485526c5f6482382cd04c6b31ce1d6576b25b` | `H` |
| h1b3 `B` | `scratch/k16_Hfinal_doubleblocker_h1b3.word` | `445d06607d7074c91be7807769f64d86e6abc5f23a1f999873a09c4d9a42c62f` | `H` |

Let `D54` be the variable-position union of the already closed
canonical/sharp-A/new-A/96-forward-H parent alphabet.  Exact comparison gives

| comparison | Hamming distance | changes in `D54` | changes outside `D54` | support-list SHA-256 |
|---|---:|---:|---:|---|
| `C -> R` | 1620 | 15 | 1605 | `75c32da6e2e1f00997ec2dbfcdeb0f5b774e26ac7fe02c52939f826fd6f3269c` |
| `C -> B` | 2152 | 15 | 2137 | `2e7689847c3d9adf83b23635a8f52c1f6ecf966922c9a0b8a315353527ae6eaf` |
| `R -> B` | 805 | 6 | 799 | `2c6220b485a50b1d48b3b678a7b15be8b1461578fe4bdf51a04a52cad4e84a8c` |

Only 17 positions of `D54` are touched by either new donor.  The union of
`D54`, the `C -> R` support and the `C -> B` support has 2241 positions.
Adjoining the aligned values of `R` and `B` to the closed parent alphabet
adds 2369 distinct position-value pairs on 2201 positions.

The exact `C -> R` edit ledger has SHA-256
`6d2f830bd61049f62b1988e7f3ff39c27d7cddb274df92c486088d7e42206a1e`.
The exact `R -> B` audit has SHA-256
`5ca9eb5e507650af945f8a0dba534cc736ff50a2287fdbd37b68c3bd9d66f7a7`.
There is no separately frozen direct `C -> B` edit ledger; the support and
distance above are reconstructed directly from the two frozen word files.

## 2. External-run obstruction for every aligned saved-value crossover

For each position `i`, let `A_i` be the union of the old closed parent menu
and the two aligned donor values `R_i,B_i`.  Position zero is excluded from
an external witness.  For a target `t`, define

\[
 A_i(t)=\{a\in A_i:a\mathbin{\&}\neg t=0\}.
\]

A `t`-run is a maximal interval `G` in positions `1,...,12872` on which
every `A_i(t)` is nonempty.  Put

\[
 U_t(G)=\bigvee_{i\in G}\ \bigvee_{a\in A_i(t)}a.
\]

### Lemma 2.1 (run-union certificate)

If `U_t(G) != t` for every `t`-run `G`, then no independent aligned choice
`x_i in A_i` has a position-zero-avoiding interval of OR `t`.

#### Proof

If an interval `I` has OR `t`, every selected value on `I` is a submask of
`t`.  Thus `I` lies in one `t`-run `G`, and

\[
 t=\bigvee_{i\in I}x_i\subseteq U_t(G).
\]

Since `U_t(G)` is itself a submask of `t`, this forces `U_t(G)=t`, contrary
to the hypothesis.  \(\square\)

### Theorem 2.2 (expanded aligned bank has no external reserve)

The full independent product of the old saved-parent menus with the aligned
`R` and `B` alleles has no external witness of `P` and no external witness
of `Q`.

#### Exact certificate

For `P`, there are 214 runs, with length histogram

\[
                       1^{200}2^{14}.
\]

The largest run union has six of the seven required bits.  For `Q`, there
are 347 runs, with histogram

\[
                       1^{313}2^{28}3^6,
\]

and the largest run union has seven of the eight required bits.  Every run
has a nonzero deficit.  Lemma 2.1 proves the theorem.

Although the donors contribute 78 new `P`-submask alleles on 72 positions
and 125 new `Q`-submask alleles on 118 positions, none lies in a run whose
possible union reaches its target.  Thus the external-reserve clauses are
already empty before any global coverage SAT is formed.

Consequently any valid position-zero finish based on these sources requires
at least one value absent from the entire expanded aligned parent alphabet.
This statement concerns literal aligned choices; it does not exclude
reordering, insertion/deletion, or a new chronology.

## 3. Exact arbitrary one-cell escape and its collateral optimum

For a sole-`H` word `w`, position `p>0`, and target `t`, let the left and
right context sets be all ORs of suffixes ending at `p-1` and prefixes
starting at `p+1`, together with the empty context `0`.  A nonzero value `y`
creates an external `t` witness at `p` exactly when

\[
       \ell\vee y\vee r=t                              \tag{3.1}
\]

for some two such contexts.  Equation (3.1) gives every candidate value:
if `s=ell OR r` is a submask of `t`, then

\[
 y=(t\setminus s)\vee z,\qquad z\subseteq s.           \tag{3.2}
\]

Every changed interval contains `p`; multiplying the compressed left/right
context counts therefore gives the exact global coverage delta of `p -> y`.
This is an exhaustive calculation, not a heuristic provider sample.

### Theorem 3.1 (one-cell external-reserve atlas)

For both `R` and `B`, among all positions `p=1,...,12872` and all nonzero
16-bit replacements:

1. exactly 1350 assignments for `R`, on 322 positions, create both external
   `P` and external `Q` witnesses;
2. exactly 1352 assignments for `B`, on 325 positions, do so;
3. every such assignment retains `H` as absent before the position-zero
   finish;
4. the minimum number of other targets lost is exactly three;
5. exactly twelve assignments attain that minimum, identically in both
   words.

The twelve minimum rows are

\[
\begin{array}{c|c|c}
p&\text{new value}&\text{three collateral holes}\\ \hline
1210&\mathtt{0860},\mathtt{0861},\mathtt{4860},\mathtt{4861}
    &\mathtt{48b9},\mathtt{68b9},\mathtt{6cb9}\\
5462&\mathtt{0018},\mathtt{0038},\mathtt{0058},\mathtt{0078},
      \mathtt{0818},\mathtt{0838},\mathtt{0858},\mathtt{0878}
    &\mathtt{486b},\mathtt{686b},\mathtt{6c6b}.
\end{array}
\]

All twelve values are absent from the expanded aligned menus.  Those menus
are `{0x48a1}` at position 1210 and `{0x082a,0x086a}` at position 5462.

The scope of the minimum is important: it is the minimum pre-finish
collateral among one-cell joint external-reserve installers that retain the
original `H` hole.  It is not a lower bound after an arbitrary simultaneous
position-zero change, nor a support lower bound for a universal word.

#### Literal geometry of the donor-exposed optimum

At position 5462, every one of the eight values has the form

\[
                 y=\mathtt{0018}\vee s,qquad
                 s\subseteq\mathtt{0860}.              \tag{3.3}
\]

The fixed following cells give

\[
 [5462,5464]=P,qquad [5462,5465]=Q.                   \tag{3.4}
\]

Before the change, the same nested intervals and their one-step extension
are the unique witnesses

\[
 [5462,5464]=\mathtt{486b},\quad
 [5462,5465]=\mathtt{686b},\quad
 [5462,5466]=\mathtt{6c6b}.                            \tag{3.5}
\]

Thus (3.3) replaces exactly the ladder (3.5) by the two external reserves
(3.4).  Fixing position zero to `0x2c6d` then installs `H`; direct replay for
every value in (3.3), in `C`, `R`, and `B`, leaves exactly the three holes in
(3.5).

The position-1210 fibre has the analogous geometry, with `P,Q` on
`[1210,1212]`, `[1210,1213]` and the destroyed ladder
`0x48b9,0x68b9,0x6cb9` through endpoint 1214.  The fixed finish
`p0=0x2c29` leaves exactly those three holes.

## 4. Two complete local-collar no-go theorems

The exact dynamic substitution encoding was applied to both minimum fibres.
Each live cell is a completely arbitrary nonzero 16-bit value; every other
cell is frozen.  Fixed-only targets are removed, and every remaining target
gets all literal interval terms that meet the editable support.  The frozen
encoding logic has an independent exhaustive truth-table audit.

### Theorem 4.1 (position-1210 forward collar is impossible)

Fix `p0=0x2c29`; allow positions `1210,...,1214` to vary; restrict position
1210 to its exact four-value minimum fibre; leave 1211--1214 arbitrary
nonzero.  No resulting word is universal.

The exact model has 28 repair targets, 144 changed-interval bases, 420
witness terms, 505 variables, and 10,957 clauses after the fourteen fibre
units.  Kissat returned UNSAT.  The 95,742-byte DRAT proof, SHA-256
`e9bc9d53814f1afee02babd6dd60d0f34755cd42edc0d479eb9a80e7ca462056`,
was checked by `drat-trim`, which returned `s VERIFIED`.

### Theorem 4.2 (position-5462 forward collar is impossible)

Fix `p0=0x2c6d`; allow positions `5462,...,5466` to vary; restrict position
5462 to its exact eight-value minimum fibre; leave 5463--5466 arbitrary
nonzero.  No resulting word is universal.

The exact model has 30 repair targets, 145 bases, 450 terms, 535 variables,
and 11,589 clauses after the thirteen fibre units.  Kissat returned UNSAT.
The 101,165-byte DRAT proof, SHA-256
`46acf9ab296c95f311fce8f3f1fe4a1942ecf44c5a11fcaf48c1f7e83b464458`,
was independently checked and returned `s VERIFIED`.

These theorems close only the two named forward collars.  They do not close
arbitrary repair positions, a two-sided collar, mixtures of the twelve
minimum rows, or any larger rethread.

## 5. The exact six-component remote-return gate

Condition on the position-5462 reserve fibre (3.3).  Its values contain a bit
forbidden by each target in (3.5), so the old witnesses starting at 5462
cannot be recovered by silently restoring the inherited allele.

Applying Lemma 2.1 to the conditioned aligned menus gives

\[
\begin{array}{c|c|c}
t&\text{run histogram}&\max |U_t(G)|\\ \hline
\mathtt{486b}&1^{198}2^{11}&6<7\\
\mathtt{686b}&1^{309}2^{24}3^7&7<8\\
\mathtt{6c6b}&1^{405}2^{60}3^{19}4^8&8<9.
\end{array}                                             \tag{5.1}
\]

Thus aligned donor values cannot repair any member of the ladder.

Among all conditioned admissible runs, exactly six nested **menu-envelope**
components miss the same single bit at all three depths:

\[
\begin{array}{c|c}
\text{nested run endpoints for }\mathtt{486b},\mathtt{686b},\mathtt{6c6b}
 &\text{missing bit}\\ \hline
577{:}578,\ 577{:}579,\ 577{:}580&\mathtt{0040}\\
3330{:}3331,\ 3330{:}3332,\ 3330{:}3333&\mathtt{0008}\\
3495{:}3496,\ 3495{:}3497,\ 3495{:}3498&\mathtt{0001}\\
3839{:}3840,\ 3839{:}3841,\ 3839{:}3842&\mathtt{4000}\\
5463{:}5464,\ 5463{:}5465,\ 5463{:}5466&\mathtt{0002}\\
5972{:}5973,\ 5972{:}5974,\ 5972{:}5975&\mathtt{0020}.
\end{array}                                             \tag{5.2}
\]

Here the envelope ORs all admissible alleles at each position, including
alleles which are mutually exclusive in one actual word.  Thus (5.2) is an
exact missing-bit classification and support selector, not a construction of
the three target witnesses.  Consistent simultaneous realizability and all
collateral are handled by the CNF below.  This is the first exact safe-gap
support for a remote-return search rather than only local ladder repair.

### Lemma 5.1 (two-colour separator)

Use the six editable components

\[
 [577,578], [3330,3331], [3495,3496], [3839,3840],
 [5462,5464], [5972,5973].                              \tag{5.3}
\]

Every one of the five intervening fixed gaps has OR `0x7fff`.  Therefore an
interval meeting two components has OR either `0x7fff` or `0xffff`, according
to whether its editable cells supply the top bit.  Both colours have fixed
witnesses avoiding (5.3), namely `[2,18]` and `[6425,6436]`.  Hence no
critical-target witness crosses a component gap.

This separates interval terms, but not the global cover clauses: two
different components may still provide the same target.

### Theorem 5.2 (exact compact arbitrary-value model)

Fix `p0=0x2c6d`.  Make the thirteen positions

\[
\{577,578,3330,3331,3495,3496,3839,3840,
  5462,5463,5464,5972,5973\}                           \tag{5.4}
\]

editable.  Restrict 5462 to the eight values (3.3), and give every other
listed position the full nonzero 16-bit domain.  Freeze all other cells.

Universality on this face is exactly the satisfiability of the retained CNF

```text
scratch/threadA_k16_external_reserve_min3_20260730/
    sixcomponent.restricted.cnf
SHA-256 c83918c4d0458b14259a9cfd755b5fa955c97ee2ad4fb5f1cab5cb8d3fb62189
```

It has

\[
 117\text{ repair targets},\quad483\text{ bases},\quad2457\text{ terms},
 \quad2678\text{ variables},\quad44595\text{ clauses}. \tag{5.5}
\]

There are exactly 21 terms per target: all nonempty consecutive subblocks of
five two-cell components and one three-cell component,

\[
                       5\binom{3}{2}+\binom{4}{2}=21.
\]

Lemma 5.1 proves that no cross-component term is omitted.  Fixed positions
5465 and 5466 occur in the endpoint bases, so the deeper ladder witnesses are
represented even though those cells are not editable.

The model was run for 300 seconds on one H100 CPU core, under a 2 GiB address
space cap.  It exited 124.  Therefore its disposition is exactly

\[
                         \boxed{\text{UNKNOWN}}.
\]

The 337,641,472-byte partial DRAT stream is retained remotely with SHA-256
`348076f2533d0faf4a8dcb4282a7f03bc364f3a8541b90abd107a89145ba5334`.
It is not a certificate and was not passed to a proof checker.  No SAT or
UNSAT conclusion is drawn from it.

The model is exact only for (5.4).  In particular, fixing 5465 and 5466 is an
intentional restriction, not a maximal-component theorem.

## 6. Relation to the H38 causal-support no-go

The separate H38 external-ready word has singleton external witnesses at
positions 111 and 6522.  The exact arbitrary-value CNF on its twelve traced
causal positions is DRAT-UNSAT.  Its correct semantic consequence is:

> With position zero and every cell outside those twelve positions frozen,
> no reassignment of the twelve cells is universal.

It does not show that a cell outside `{p0} union causal12` is necessary after
an independently allowed position-zero finish.

The repaired audit
`MATH_AUDIT_K16_EXTERNAL_READY_H38_CAUSAL12_UNSAT_20260730.md`, SHA-256
`6c2ca2f0c6f18d80f1fa07b28141cae01783d355b61f5461a20a33df1418fb4a`,
now binds the on-disk compressed proof SHA-256
`53b207e7172271b1b15f5a5b7db0ad2e73cd9c4468557a89a50268d4010a740c`
and decompressed content SHA-256
`51790b463bd39b834465a1418965c694439da235636f9553eab62cbd78965726`.
Its lineage audit therefore passes.  Theorems 2.2--5.2 use independent
artifacts.

## 7. Exact remaining gate

The aligned saved-value branch is closed even after adjoining the far and
h1b3 donors.  A single genuinely new cell is both necessary and sufficient
to install the two external reserves, but every such one-cell installation
creates at least three collateral holes.  The two natural forward local
collars cannot repair those holes.  The smallest currently isolated remote
return architecture is the six-component face (5.4), whose exact model is
open.

Thus the next proof or computation must do one of the following:

1. decide the exact six-component CNF;
2. enlarge (5.4), most naturally by freeing 5465--5466 or adding another
   common-deficit component; or
3. use a non-aligned/global chronology change outside this crossover model.

Nothing here proves or refutes `nu(16)=12873`.

## 8. Frozen Lane-A artifacts

```text
scratch/audit_threadA_k16_external_reserve_augmented_menu_20260730.py
SHA-256 ad72094374618320ce9f749c65df52608d97422ee36e45ec9f2dae5a4b1f88c5

scratch/threadA_k16_external_reserve_augmented_menu_safe_components_frozen_20260730.audit.json
SHA-256 e81889976e875343e8570e450b8b846b98a69f76c480944a159c937e38a4faf8
payload 11dca000636ef6e0a8a2c137d2823b03bb66b81144bd1267560d36adac32919c

scratch/audit_threadA_k16_external_reserve_onecell_atlas_20260730.py
SHA-256 362e4751c53bd032fb3b7ab087387ddd48a9e8870b154c48a96265f61b4bcf38

scratch/threadA_k16_external_reserve_onecell_atlas_20260730.audit.json
SHA-256 5b7d4c333c73d34ee6d7dd76b0e3e2c65fc7974837c7ae62ddf8a3a02eab98ef
payload e939fb62d7fe7a39c8a5ec20bd80e23562f624bda570cd41eb0fb907c0d45feb

scratch/audit_threadA_k16_external_reserve_min3_faces_20260730.py
SHA-256 a46d20a5ac98c7a612695f31955056685e4855550665a560cab4ad72af0e280f

scratch/threadA_k16_external_reserve_min3_faces_20260730.audit.json
SHA-256 cdec0cb01c87696d479796233d798ae15523b084bf6f906ac339da572f957209
payload e7553d607d17eed8c9650da7229b6cce4b70f5ba9a61efed3003cec003d9a958

scratch/audit_threadA_k16_external_reserve_sixcomponent_model_20260730.py
SHA-256 c18306e3736da78469c0ea38a9eba4e9ce0fb310e02f056c8c31d1c6bc951042

scratch/threadA_k16_external_reserve_sixcomponent_model_20260730.audit.json
SHA-256 6fba5f2a09530ed2c8ff4487132694b2ea25b804c501e8ea6246a76574c4ba1b
payload 563167e77aec21b52068e34431ccddd2a3339c3e042155c0dc454ebf744c1e0a
```
