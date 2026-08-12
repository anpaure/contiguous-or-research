# K16 multi-basin crossover: safe-gap provider collapse

Date: 2026-07-30

Status: exact solver-free no-go for the maximal saved-parent alphabet;
independent replay of every input; auxiliary coherent-packet census on one
capped H100 CPU.  No length-12,873 word is claimed.

## 1. Frozen words and the actual geometry

Put

```text
C = scratch/k16_upper12874_best_delete.word
SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
```

The length of `C` is `12873` and its sole missing mask is

\[
                    H=\mathtt{2c6d}=11373.              \tag{1.1}
\]

There are two useful previously saved representatives of the opposite
one-hole phase.  The sharp representative

```text
S = scratch/k16_optimal_onehole_phase_a86d.word
SHA-256 e9f4935cbbba9300190d552c9f418328d16913d59a7f6832a4f20fe1f7662792
```

differs from `C` only at position `6440`.  The joint representative

```text
J = scratch/k16_upper12874_delete_radius2_best1_43117.word
SHA-256 09a60d48584a737f452a5d53c8fadec9b26cdad354f36926fbc5b1b1ceb4d166
```

differs at `6439,6440`.  Both have sole hole

\[
                    A=\mathtt{a86d}=43117.               \tag{1.2}
\]

The structurally new `A` word is

```text
N = scratch/k16_compound_rev_provider_auth.h1.0.word
SHA-256 a92509fd4f60490588973e7a70d457b369e4b0192a65f3de7adef105727e33fa
```

It differs from `C` at exactly 44 positions.  Its authentication manifest has
SHA-256
`7daae83366f61fbdabbfa93131c6630c6acc4b3eb4745cd65adaad1e9f77d4e9`.

Finally, the 96 authenticated forward-`H` words are the rows of

```text
scratch/k16_compound_fwd_provider_auth.authentication.json
SHA-256 804e41ac465c6e46e208f352b5c40e985fde1f3a404080ede985dc410432e1e9
```

Every row is distinct, has length `12873`, and has sole hole `H`.  An exact
lineage audit gives the following important correction to the informal
description “96 basins”: all 96 rows share the same ten-edit backbone and
differ from one another only at position `12872`.  Thus they form one
96-state endpoint fibre, not 96 independent edit directions.  One row is at
distance 10 from `C`, and the other 95 are at distance 11.  The common
backbone support is

\[
\{2062,2855,4903,5291,5810,6187,6440,6567,6784,8008\}. \tag{1.3}
\]

There is separately a genuinely far annealed word
`scratch/rex3_final_fwd_h11373.word`, SHA-256
`b6ed242d0f098f8511d31027b2d485526c5f6482382cd04c6b31ce1d6576b25b`,
at distance 1620 from `C`; it is a single word and is not one of these 96
rows.  Its exact edit ledger has SHA-256
`6d2f830bd61049f62b1988e7f3ff39c27d7cddb274df92c486088d7e42206a1e`.
It is outside the theorem below.

## 2. The maximal saved-parent alphabet

For every position `i`, let

\[
 M_i=\{P_i:P\in\{C,S,N\}\cup\mathcal H_{96}\}.          \tag{2.1}
\]

The joint representative `J` contributes no new position value: its value at
`6439` is already supplied by `N`, and its value at `6440` is supplied by
`S`.  Hence (2.1) also contains every cell of `J`.

Let

\[
 \mathcal X=\{X:X_i\in M_i\text{ independently for every }i\}. \tag{2.2}
\]

This is the maximal literal parent-alphabet crossover family.  In particular,
it contains every packet-coherent, component-coherent, one-cut, multicut, or
phase-preserving crossover made solely from saved parent values.

Exactly 54 positions have a nontrivial menu.  The complete menu histogram is

\[
             1^{12819},\qquad2^{52},\qquad4^1,\qquad96^1. \tag{2.3}
\]

The exceptional menus are

\[
M_{6440}=\{\mathtt{0449},\mathtt{046d},
            \mathtt{8040},\mathtt{806d}\}               \tag{2.4}
\]

and the 96-state endpoint `M_12872`.  The latter is a subset of

\[
 \{\mathtt{0200}\vee s:s\subseteq\mathtt{cc61}\};       \tag{2.5}
\]

the seven free bits give 128 states, of which exactly 32 are forbidden.
Consequently

\[
                 |\mathcal X|=2^{52}\cdot4\cdot96
                              =3\cdot2^{59}.             \tag{2.6}
\]

Any direct selector encoding needs at least
\(\lceil\log_2|\mathcal X|\rceil=61\) primary bits.

## 3. A general coverage-safe gap lemma

Let `C` be any fixed word and `D` any editable-position set.  Write

\[
 \mathcal F=\{\operatorname{OR}_C(I):I\text{ is an interval and }
                                      I\cap D=\varnothing\},
 \qquad
 \mathcal K=\{1,\ldots,2^k-1\}\setminus\mathcal F.     \tag{3.1}
\]

For two consecutive positions of `D`, let `G` be the intervening fixed gap
and put `g=OR_C(G)`.  Call the gap coverage-safe when

\[
                \{T:g\subseteq T\}\subseteq\mathcal F. \tag{3.2}
\]

Cut the ordered set `D` at all coverage-safe gaps.  This gives blocks `b`.
For a permitted local state `s` of block `b`, let
\(P_b(s)\subseteq\mathcal K\) be the critical colours of all intervals whose
intersection with `D` is nonempty and contained in `b`.

### Lemma 3.1 (exact block-provider criterion)

A crossover state `X` is universal if and only if

\[
                     \mathcal K\subseteq
                     \bigcup_b P_b(X|_b).                \tag{3.3}
\]

#### Proof

Every colour in `F` has an interval witness avoiding all editable positions,
so it survives every crossover.  Suppose an interval of a critical colour
`T` crosses a safe gap.  It contains every cell of `G`, hence `g` is a subset
of `T`.  Condition (3.2) then gives `T` in `F`, contradicting criticality.
Thus every critical-colour interval meets editable positions in one block,
and its colour belongs to that block's provider set.  Conversely, every
member of a provider set is witnessed by its defining literal interval.
These two implications prove (3.3).  \(\square\)

Lemma 3.1 gives an exact multiple-choice cover CNF: choose one state in each
block and impose one provider clause for every critical target.  It uses no
interval-witness variables.

## 4. Complete collapse for the K16 bank

For the 54-position set in Section 2, fixed-only intervals cover exactly

\[
                       |\mathcal F|=64908,
 \qquad                |\mathcal K|=627.                \tag{4.1}
\]

Exactly 50 of the 53 internal gaps are safe.  The three unsafe gaps are

\[
\begin{array}{c|c}
\text{end positions}&g\\ \hline
6439,6440&\mathtt{0000},\\
10209,10211&\mathtt{d08c},\\
12369,12374&\mathtt{bc6c}.
\end{array}                                              \tag{4.2}
\]

Thus there are 51 blocks: 48 one-position blocks and three two-position
blocks.  Their local-state histogram is

There are 47 blocks with two states, two blocks with four states, one block
with eight states, and one block with 96 states.  Thus there are only 206
local states in total.  The exact catalogue has
2228 local interval forms and 6156 form-state evaluations.

### Theorem 4.1 (maximal saved-parent crossover no-go)

No word in `X` is universal.

#### Proof

For each local state the catalogue computes `P_b(s)` by literal interval OR,
with the full fixed suffix and prefix on its side of the adjacent safe gaps.
For every one of the 50 noncentral blocks, all local states have exactly the
same provider set.  Hence their choices disappear from (3.3).

Only the block `{6439,6440}` is state-dependent.  It has three distinct
provider sets among its eight states.  After adjoining the invariant provider
sets of all other blocks, its exact residual table is

\[
\begin{array}{c|c|c}
X_{6439}&X_{6440}&\text{missing colours}\\ \hline
\mathtt{206c}&\mathtt{0449}&\{\mathtt{a86d}\}\\
\mathtt{206c}&\mathtt{046d}&\{\mathtt{a86d}\}\\
\mathtt{206c}&\mathtt{8040}&\{\mathtt{2c6d},\mathtt{a46d}\}\\
\mathtt{206c}&\mathtt{806d}&\{\mathtt{2c6d}\}\\
\mathtt{206d}&\mathtt{0449}&\{\mathtt{a86d}\}\\
\mathtt{206d}&\mathtt{046d}&\{\mathtt{a86d}\}\\
\mathtt{206d}&\mathtt{8040}&\{\mathtt{2c6d}\}\\
\mathtt{206d}&\mathtt{806d}&\{\mathtt{2c6d}\}.
\end{array}                                              \tag{4.3}
\]

Every row is nonempty.  Criterion (3.3) therefore fails for every member of
`X`.  \(\square\)

The proof audit independently hash-checks and literally replays all 99 input
words, reconstructs all menus, all fixed coverage, every gap, every local
form and every provider set.  It then asserts all counts and the complete
table (4.3).  It does not invoke a SAT solver.

## 5. Independent finite cross-check and the H44 proof

As a separate check, the coherent-atom subfamily was exhausted on one H100
CPU with a 512 MiB address-space cap.  It permits the 42-position new-A
remote packet, the nine-position forward-H remote packet, the left phase,
the four hub alleles, and all 96 endpoint alleles.  Its 3072 words have hole
histogram

\[
                         1^{2688},\qquad2^{384};         \tag{5.1}
\]

the only one-hole labels are `0x2c6d` and `0xa86d`.

The previously frozen binary `C/N` theorem covers all \(2^{44}\) choices of
the two parent values.  Its 23,907-variable, 362,147-clause CNF is UNSAT; the
106,188-byte DRAT proof checks.  A fresh bounded `drat-trim` replay extracted
a 139-clause core and again returned `s VERIFIED`.  Theorem 4.1 strictly
subsumes that binary face and, unlike the old bundle, is reconstructed
directly from the word files without depending on a missing pre-restriction
CNF map.

## 6. Exact remaining boundary

Theorem 4.1 closes every literal recombination that uses, position by
position, only values present in the saved canonical/new-A/96-H parent bank.
It is stronger than a component-crossover no-go and makes a new SAT solve for
that bank unnecessary.

A successful length-12,873 construction must now do at least one of the
following:

1. introduce at some support position a value absent from every saved parent;
2. edit a position outside the 54-position union;
3. change order, length allocation, or chronology rather than merely choosing
   parent values.

The active arbitrary-value 44-position CNF is not touched: it permits the
first escape.  The single distance-1620 `H` word is also not touched: adding
its alphabet changes `D`, the safe-gap decomposition, and the provider
catalogue, so it is a genuinely new crossover direction rather than another
copy of the 96-state endpoint fibre.

## 7. Frozen artifacts

```text
scratch/audit_threadA_k16_multibasin_block_provider_collapse_20260730.py
SHA-256 0327df1d0448a204dfa4266eb87a0f2fd4c59e9f936bcb65cffc3865a90fb4d7

scratch/threadA_k16_multibasin_block_provider_collapse_20260730.certificate.audit.json
SHA-256 438ed98ef668fe4d0c8ab303013f1f63936475ab067ac492547f038233871191
payload 7c323e489a48d3f18e6f68295130333560ef99ebefb998eba1b3bd405f1dbd5c

scratch/threadA_k16_multibasin_component_crossover_20260730.cpp
SHA-256 8645308b1fcfcca36627c535cd37af1bc112600d117bac04388f56a932cc3805

scratch/threadA_k16_multibasin_crossover_20260730/component_hull_v2.audit.json
SHA-256 d725883350db1500a877d0f9740dcdb3b91ce41973d0900d403f3c11ddaa9de5

scratch/threadA_k16_multibasin_crossover_20260730/H44.core.cnf
SHA-256 ed215cfb82bd8ed201e0c02558504fcdef558eb4941d165df834e2c6839ea973

scratch/threadA_k16_multibasin_crossover_20260730/H44.corecheck
SHA-256 974acaa314c643f237d8f42d1ed7df6673598c16970ea51103b6b0ab99833215
```
