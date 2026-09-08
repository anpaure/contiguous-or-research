# The Hall-19 neutral portfolio has a rigid two-unit exterior common-compiler tax

Date: 2026-07-29  
Lane: R  
Status: proved structural reduction and frozen seven-carrier exact census; no upper bound below 6,458

## 1. Result and scope

The frozen portfolio consists of seven distinct Hall-19 carrier middle paths
after deduplicating its aliases by their 6,435-state middle sequence:

```text
authoritative, c0440, c0520, c0668, c0530, c0526, c0434.
```

All seven have outer compiler matching number 16,364 on the 16,383 lower
targets.  On the exact common-word compiler, every frozen CP-SAT run ends
`OPTIMAL` with objective and bound both 16,362.  Thus every carrier has
machine-certified common-prefix deficit 21 and compatibility tax

\[
                  21-19=2.                                      \tag{1.1}
\]

The effect is not located in the carrier's deficient DM components.  In every
saved optimum, each DM component loses exactly its ordinary Hall gap; both
additional losses are outside the whole DM shore.  The authoritative exterior
pair is `{685,7267}` and the other six use `{1581,7267}`.  This remains true
while the DM shore changes from `516/497` to `330/311` and the outer edge
count ranges from 133,848 to 133,914.

Every saved residual has size 21, inclusion width 20, and exactly one
nontrivial residual OR identity,

\[
                  9524\mathbin\lor13616=13620.                  \tag{1.2}
\]

Consequently every saved prefix has shortest possible appended completion of
length exactly 20, even allowing intervals which cross the prefix/suffix seam.
Seven independently decoded length-6,458 words pass exhaustive verification
of all 32,767 nonempty masks, and the first 6,438 letters of each reconstruct
its advertised carrier under `D^3`.

None of these seven stored optimal prefixes or completed words is better than
the others.  The exact negative result is about these seven solver optima and
their stored words.  It does not exclude another optimum on the same carrier
with a residual outside
the audited portfolio pool, a deliberately lower-coverage prefix with a more
compressible completion, or a different carrier.

The solver statuses are frozen exact-model results, but no DRAT, Farkas, or
standalone CP-SAT proof log was emitted.  Thus the explicit 6,458 words and all
solver-free structural theorems below are independently checkable; the word
`OPTIMAL` in the numerical census retains its ordinary solver-status scope.

## 2. Exact common-compiler formulation

Fix a depth-`d` middle carrier

\[
                       T=(T_0,\ldots,T_{W-1})
\]

and its maximal erosion

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i,
 \qquad 0\le p<W+d.                                      \tag{2.1}
\]

Let

\[
                 \Omega=\{(p,x):x\in P_p\}.                    \tag{2.2}
\]

An outer compiler action is a target/cell pair `a=(X,I_a)`, where `I_a` is a
physical interval of length at most `d`.  Its blocker set is

\[
 B(a)=\{(p,x)\in\Omega:p\in I_a,\ x\notin X\}.            \tag{2.3}
\]

For an action matching `S` put

\[
 \Omega(S)=\Omega\setminus\bigcup_{a\in S}B(a).           \tag{2.4}
\]

There are three kinds of positive support:

\[
 M_{i,x}=\{(p,x):i\le p\le i+d,\ x\in P_p\},
 \qquad x\in T_i,                                        \tag{2.5}
\]

\[
 N_p=\{(p,x):x\in P_p\},                                 \tag{2.6}
\]

and, for `a=(X,I_a)` and `x in X`,

\[
 W_{a,x}=\{(p,x):p\in I_a,\ x\in P_p\}.                 \tag{2.7}
\]

### Theorem 2.1 (forbidden-circuit common compiler)

An action matching `S` is realizable by one common nonzero source word with
middle row `T` if and only if

\[
 M_{i,x}\cap\Omega(S)\ne\varnothing,
 \quad N_p\cap\Omega(S)\ne\varnothing,
 \quad W_{a,x}\cap\Omega(S)\ne\varnothing                \tag{2.8}
\]

for every applicable `i,x,p,a`.

Equivalently, the exact compiler optimum is the maximum size of an ordinary
target/cell matching which avoids every inclusion-minimal action family whose
blockers cover one support in (2.5)--(2.7), with the selected action itself
adjoined for a support of type (2.7).

At `k=15,d=3`, every such forbidden circuit has rank at most eight.  Middle
circuits have rank at most four; an anchored target-positive circuit has rank
at most four; and a point-nonzero circuit has rank at most eight.

#### Proof

For a selected action matching define the entrywise-maximal surviving word

\[
                 A_p(S)=\{x:(p,x)\in\Omega(S)\}.                \tag{2.9}
\]

Every bit outside a selected target is deleted on its assigned interval by
construction.  The `W` conditions give every target bit, so the assigned
interval OR is exactly its target.  The `M` conditions are exactly the
coordinatewise equations `D^d A=T`, and the `N` conditions are exactly source
nonzeroness.  Conversely any realization can use only incidences which
survive every selected negative window, so all three conditions are
necessary.

If an inclusion-minimal action family covers a finite support `H`, each
action has a private element of `H`; choosing one private element per action
is injective.  Hence the family has size at most `|H|`.  Supports (2.5) have
size at most `d+1`, supports (2.6) have size at most `max_p |P_p|=8`, and
supports (2.7) have size at most `d`; adjoining their anchored action gives
rank at most `d+1`.  Individual outer admissibility excludes a one-action
failure.  This proves the asserted ranks.  \(\square\)

One useful corollary is that the model objective equals actual short-target
coverage at an optimum.  If an unselected target occurred accidentally, its
actual interval could not be selected for a different target, and selecting
it would add no blocker not already zero.  It could therefore be added,
contradicting optimality.

### Lemma 2.2 (short occurrence and maximal normalization)

For the `k=15,d=3` carrier problem, every literal occurrence of a lower
target uses at most three source letters.  Moreover, every literal prefix
with `D^3A=T` which covers the exact optimum of 16,362 lower targets has the
same lower-target residual as the maximal word `A(S)` in (2.9), where `S`
selects one occurrence of each covered target.  Consequently the exact
model and its forced-actual-absence faces range over all literal
16,362-target optima, not only over words already presented in maximal form.

#### Proof

Every lower target is a nonempty subset of `[15]` of rank at most seven.
Every interval of four or more source letters contains four consecutive
letters `A_i,A_{i+1},A_{i+2},A_{i+3}`, whose OR is the rank-eight middle
state `T_i`.  Its full interval OR therefore has rank at least eight and
cannot be a lower target.  Thus every lower occurrence has length at most
three and is one of the modeled cells.

Now choose one such cell for every target covered by a literal optimum `A`,
forming an action matching `S`.  Since `D^3A=T`, every source incidence of
`A` lies in the maximal erosion (2.1), and the chosen target windows impose
exactly the blockers (2.3).  Hence `A` is entrywise contained in `A(S)`.
The three support conditions (2.8) hold because `A` itself witnesses them,
so Theorem 2.1 makes `A(S)` a nonzero exact prefix with the same carrier and
with every target selected by `S`.  If `A(S)` acquired any further lower
target, its occurrence would be an unused modeled cell and its selector
could be added without a new blocker, contradicting the exact optimum
16,362.  Thus maximalization changes no lower-target residual.  \(\square\)

## 3. Exact localization of the compatibility tax

Let the canonical deficient DM components be `(L_j,R_j)` and put

\[
 g_j=|L_j|-|R_j|,
 \qquad h=\sum_jg_j.                                      \tag{3.1}
\]

Here isolated zero-degree targets are included as `1/0` components.  If
`R(A)` is the set of lower targets missed by one compatible word, then every
component loses at least its gap, because the realized target/cell incidences
form an ordinary matching.

### Proposition 3.1 (tax decomposition)

Writing `D_L` for the union of the deficient left shores,

\[
 |R(A)|-h
 =|R(A)\setminus D_L|
  +\sum_j\bigl(|R(A)\cap L_j|-g_j\bigr).                 \tag{3.2}
\]

Every term on the right is nonnegative.  Thus compatibility tax splits
canonically into exterior tax and excess internal tax.

#### Proof

Partition `R(A)` into its exterior part and its intersections with the
disjoint component shores, then subtract (3.1).  Nonnegativity follows from
ordinary Hall on each component.  \(\square\)

For every row in the census below, the internal sum in (3.2) is zero and the
exterior term is two.

## 4. Seven-carrier exact portfolio census

All source positions and intervals below are zero-based.  Every carrier is a
rank-eight Johnson path of length 6,435, is depth-three resident, has complete
upper support at every depth, and has the same six zero-degree lower targets.

| carrier | move/provenance | outer edges | DM shore | exact objective/bound | exterior residual | last prefix letter | verified 6,458-word SHA-256 |
|---|---|---:|---:|---:|---|---:|---|
| authoritative | `FR(123,722,4710)` | 133852 | 516/497 | 16362/16362 | `{685,7267}` | 7682 | `7e11fafa57b96daec59e29067e809b06fc4992d1e4c4c1a7d8d9e0d5e24d546d` |
| c0440 | `FR(3814,4556,5539)` | 133880 | 380/361 | 16362/16362 | `{1581,7267}` | 7680 | `fd5975db8d372e0c5b10ad1b70dcd3dd07aaa1d71c4748961c71eba9e427383c` |
| c0520 | `RF(688,2636,2650)` | 133848 | 485/466 | 16362/16362 | `{1581,7267}` | 7681 | `05f3b997bc06ddc0f4809a34e3fd94e9607f0a8a3469a50dd7483d49e31e8c58` |
| c0668 | relay `RF(3176,4522,5948)` | 133860 | 361/342 | 16362/16362 | `{1581,7267}` | 7681 | `c2b2d65851e92f597821a97f8bc162f51528722c9863078140fbd29399e40592` |
| c0530 | commuting `A+B` | 133876 | 349/330 | 16362/16362 | `{1581,7267}` | 7682 | `9e811367aa22f62a66b656423d1b8b1c71912b99ebe9842879cd8e7488929632` |
| c0526 | commuting `B+C` | 133856 | 330/311 | 16362/16362 | `{1581,7267}` | 7680 | `4abfaf527e0907f3f16b9077ff7363635ac3253660c3ffd970c3c6651d648325` |
| c0434 | same-root extension | 133914 | 382/363 | 16362/16362 | `{1581,7267}` | 7682 | `a061508dee53966539b1c7c5f85352026add73cbc3903010c3f86839a045aa8b` |

The carrier-file SHA-256 values in the same order are

```text
authoritative 86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
c0440         a51f8631a9b2394405b8304c949bf9606d3b43f897f51ad9474de725df34584a
c0520         897ab99092552874c0b66203bc4bbe1a4e4b68e349d58521b53ebf21dd126c39
c0668         2c024151a93eb5f2e36cd113b90d38b89685a14026d66b03788c5a683f83913f
c0530         79a4d1dbf5b8c40fea6086d1cd7820f74ccd058518b53f35a2e6d830fa163451
c0526         2a266531b92aeed3cf662d556699ff102f83b331e53655923af42c25373e1d7c
c0434         8e894909a2c83cdc5449bcf03d092c841cffb82e026ab8ef3568cc03b5bc2012
```

The complete residuals are:

```text
authoritative:
685,964,1103,2420,2575,2676,5237,5801,7267,7504,8729,9524,
11802,13616,13620,17683,17738,18970,19568,21641,29776

c0440:
1103,1581,2420,2575,2676,4469,5801,7267,7504,8217,9524,12314,
13616,13620,17683,17738,18970,19568,21641,29584,29776

c0520:
1359,1581,2420,2575,2676,4469,5801,7267,7504,9524,10393,13616,
13620,17683,17738,19098,19568,21641,24730,25568,29776

c0668:
1581,2420,2575,2676,4469,5048,5199,5801,7267,7504,9524,11802,
12825,13616,13620,17683,17738,18970,19568,21641,29776

c0530:
1359,1581,2420,2575,2676,4469,5801,7267,7504,9140,9273,9524,
10330,13616,13620,17683,17738,18970,19568,21641,29776

c0526:
1103,1581,2420,2575,2676,4469,5048,5801,7267,7504,8222,8761,
9524,13616,13620,17683,17738,19098,19568,21641,29776

c0434:
1103,1581,2420,2575,2676,5237,5801,7267,7504,9104,9245,9524,
10330,13616,13620,17683,17738,18970,19568,21641,29776
```

Their seven-way intersection has 14 masks,

```text
2420,2575,2676,5801,7267,7504,9524,13616,13620,17683,17738,
19568,21641,29776,
```

and their union has 41 masks.  The exact full union is frozen in
`scratch/k15_h19_common_compiler_portfolio_20260729/all_seven_residual_union.json`.

This census gives two sharp non-predictors.  Increasing the raw outer edge
count to 133,914 does not change the common optimum.  Compressing the DM
shore from 516/497 to 330/311 does not change it either.  The colored
forbidden-circuit clutter of Theorem 2.1, not a scalar Hall or DM statistic,
is the correct exact invariant.

## 5. The two exterior losses

### Proposition 5.1 (universal left boundary circuit)

For every carrier in the portfolio, the outer candidate intervals are

\[
 \Gamma(685)=\{[1,1]\},
 \qquad
 \Gamma(1581)=\{[1,1],[1,2],[1,3]\}.                   \tag{5.1}
\]

No common word can cover both targets.  By Lemma 2.2 these are the complete
literal candidate lists, not merely the cells exposed by a maximal-word
encoding.

#### Proof

If `[1,1]` witnesses 685 then `A_1=685`.  The bit 128 belongs to
`685\setminus1581`.  Every possible 1581 witness contains position 1, so its
OR contains bit 128 and cannot equal 1581.  \(\square\)

Both targets are exterior to every canonical DM shore.  The authoritative
stored optimum misses 685; the six neutral carriers miss 1581.

### Proposition 5.2 (right endpoint geometry)

Put

\[
 Q=7267=\{1,2,6,7,11,12,13\},
 \qquad
 R=7683=\{1,2,10,11,12,13\},                            \tag{5.2}
\]

where coordinate notation is one-based.  The common final erosion is

\[
 P_{6435}=1635,\quad P_{6436}=3683,\quad P_{6437}=7779. \tag{5.3}
\]

The complete outer candidate family of `Q` is

\[
 [6437,6437],\quad[6436,6437],\quad[6435,6437],          \tag{5.4}
\]

with `(cell,envelope,mandatory)` equal respectively to

```text
(6437,7779,4096), (12874,7779,6144), (19310,7779,6208).
```

In every stored optimum, `[6436,6437]` is the unique literal short witness
of `R`.  It is incompatible with all three intervals (5.4) by nested-interval
monotonicity: `Q` and `R` are incomparable, with

\[
                    Q\setminus R=96,\qquad R\setminus Q=512.    \tag{5.5}
\]

Changing only the last letter to `Q` preserves nonzeroness and `D^3A=T` in
all seven words, but changes the missing set exactly by

\[
 \operatorname{Miss}(A')
 =\bigl(\operatorname{Miss}(A)\setminus\{7267\}\bigr)
   \cup\{7683,A_{6437}\}.                                \tag{5.6}
\]

Thus the local edit changes 21 misses to 22.  The old last value is 7682 for
`authoritative,c0434,c0530`, 7680 for `c0440,c0526`, and 7681 for
`c0520,c0668`.

Equation (5.6) is not by itself a global no-go: target 7683 has interior
candidate cells.  The exact conclusion is that serving 7267 requires a
nonlocal alternating relocation of both 7683 and the old last singleton.

### Exact forced-face census

The full exact compiler was therefore rerun on every carrier with 7267
forced covered.  Every run ended

```text
status OPTIMAL, objective 16361, bound 16361, residual size 22.
```

Hence 7267 is absent from every 16,362-target exact optimum in all seven
models.  Together with Proposition 5.1 and the 19 ordinary DM gap units, this
explains the two-unit exterior tax statewise.  This last implication uses the
frozen solver optimality statuses and the maximal-normalization conclusion of
Lemma 2.2; (5.1)--(5.6) themselves are solver-free.

## 6. Exact fixed-prefix suffix theorem

Let a fixed prefix have residual family `R`, and append `q` nonzero letters.
Every new witness of a previously missing mask ends at one of the `q` new
positions.  For one fixed endpoint, the ORs obtained by moving the start left
form an inclusion chain, including intervals which cross the old/new seam.
Assign each newly covered residual mask to the endpoint of one witness.  The
residual is therefore the union of at most `q` chains, so

\[
                         q\ge\operatorname{width}(R).            \tag{6.1}
\]

For each of the seven residuals in Section 4, the only strict containments
are

\[
                  9524<13620,qquad13616<13620.                  \tag{6.2}
\]

Thus `R\setminus{13620}` is an antichain of size 20, and (6.1) gives
`q>=20`.  Conversely append the other 18 residual masks literally and then
append `9524,13616`.  The last two singleton intervals witness the operands
and their two-letter union witnesses 13620.  Hence

\[
                  \boxed{\text{shortest suffix}=20}             \tag{6.3}
\]

for every stored prefix.  This proof already includes crossing witnesses;
the additional audited fact that the last prefix letter is a subset of no
residual is not needed for the lower bound.

The seven resulting literal words all have length 6,458 and passed two
independent exhaustive checks: the H100 verifier and the local portfolio
auditor.  In each case the first 6,438 letters, rather than the full completed
word, have `D^3` equal to the 6,435-state carrier.  This revalidates the known
bound

\[
                         6438\le\nu(15)\le6458,                  \tag{6.4}
\]

but does not improve it.

## 7. Alternate-optimum width/suffix probes

The seven stored residuals do not by themselves classify other points of the
same exact-optimal face.  To obtain a finite but carrier-wide statement, let
`P_41` be the 41-mask union of all seven residuals.  Its strict-inclusion
digraph has exactly the following 15 arcs:

```text
1103<1359, 1103<5199,
8217<8729, 8217<8761, 8217<9245, 8217<9273,
8217<10393, 8217<12825, 8729<8761, 8729<12825,
9104<9140, 9104<29584,
9524<13620, 13616<13620, 18970<19098.
```

Consider an exact optimum whose 21-mask residual is contained in `P_41`.
Lemma 2.2 permits maximal normalization without changing that residual, so
the forced-actual-absence faces below apply to every literal optimum under
this hypothesis.  
The forced-face theorem makes 7267 one exterior miss, and Proposition 5.1
forces one of 685 and 1581 as the other.  Equation (3.2) then leaves no
further exterior miss and no excess miss inside any DM component.

For c0526 and c0530, every displayed comparable pair except

\[
                       9524<13620,qquad13616<13620             \tag{7.1}
\]

is either an additional exterior casualty or lies wholly in a gap-one DM
component.  The two surviving arcs share their right endpoint, so their
maximum bipartite inclusion matching has size one.  Dilworth therefore gives
residual width at least `21-1=20` for every exact optimum contained in
`P_41`.  This argument also applies to c0520.

For c0434, the root-8216 component has gap two, so eight additional arcs in
that component survive this budget test:

```text
8217<8729, 8217<8761, 8217<9245, 8217<9273,
8217<10393, 8217<12825, 8729<8761, 8729<12825.
```

Each of the eight faces was solved with both endpoint masks forced *actually
absent* from every short interval, not merely left unassigned in the selector
model.  Every run ended `OPTIMAL` with objective and bound 16,361 and 22
actual misses.  Thus no c0434 exact optimum can contain any of these eight
comparable pairs.  Its only possible inclusion arcs in `P_41` are again the
two edges (7.1), and its residual width is at least 20.

### Theorem 7.1 (four-carrier 41-mask width obstruction)

For each of `c0520,c0434,c0526,c0530`, every exact-optimal 16,362-target
prefix whose residual lies in `P_41` has residual width at least 20.  Hence
no 19-letter append can complete it, even using intervals which cross the
seam.

This theorem supersedes the need to infer anything from the stopped
suffix-only feasibility jobs for these three carriers.  It combines the
solver-free DM budget with the frozen 7267 and c0434 forced-face solver
statuses.  No negative status from an interrupted or `UNKNOWN` job is used.

The correct interpretation of any negative pool result is restricted.  It
does not exclude an exact-optimal residual using a mask outside the pool, nor
a prefix of deficit 22 or more whose final completion is nevertheless
shorter.  A positive result would be unconditional only after direct
exhaustive verification of the decoded whole word.

## 8. Frozen artifacts

Principal report and audit files:

```text
MATH_THEOREM_K15_H19_COMMON_COMPILER_PORTFOLIO_EXTERIOR_TAX_20260729.md
scratch/audit_k15_h19_common_compiler_portfolio.py
scratch/audit_k15_h19_boundary_tax_invariants.py
scratch/audit_k15_h19_forced7267_portfolio.py
scratch/audit_k15_h19_residual_pool_width_budget.py
scratch/audit_k15_h19_c0434_comparable_pair_faces.py
scratch/k15_h19_common_compiler_portfolio_20260729/portfolio_manifest.json
scratch/k15_h19_common_compiler_portfolio_20260729/portfolio_audit_dm.json
scratch/k15_h19_common_compiler_portfolio_20260729/boundary_tax_audit.json
scratch/k15_h19_common_compiler_portfolio_20260729/forced7267_portfolio_audit.json
scratch/k15_h19_common_compiler_portfolio_20260729/residual_pool_width_budget_audit.json
scratch/k15_h19_common_compiler_portfolio_20260729/c0434_comparable_pair_faces_audit.json
scratch/k15_h19_common_compiler_portfolio_20260729/all_seven_residual_union.json
```

Exact model and probe scripts:

```text
scratch/optimize_k15_exact_compiler_maxcoverage.py
scratch/probe_k15_exact_compiler_forced_target.py
scratch/probe_k15_exact_compiler_forced_missing_pair.py
scratch/solve_k15_exact_compiler_with_suffix_v2.py
scratch/search_k15_h19_optimal_residual_width19.py
```

The seven complete words and their per-word exhaustive verifier outputs are
stored as

```text
scratch/k15_h19_common_compiler_portfolio_20260729/*.suffix20.word
scratch/k15_h19_common_compiler_portfolio_20260729/*.suffix20.verify.json.
```

As a final independent validation, all five deterministic audit JSONs listed
above were regenerated locally from the frozen carriers, words, and solver
outputs and compared byte-for-byte with the stored versions.  The Python
audit/probe scripts also passed bytecode compilation.  A separate adversarial
mathematical audit checked the constants, the 15 inclusion arcs, the eight
c0434 forced faces, seam-crossing suffix logic, and the literal/maximal-word
interface; Lemma 2.2 and the portfolio-scope wording incorporate its required
corrections.  This validation rechecks decoded witnesses and implications; it
does not turn the CP-SAT `OPTIMAL` statuses into standalone proof certificates.

All CP-SAT optimization and feasibility runs used only H100 CPU.  Local work
was limited to parsing, deterministic small audits, report generation, and
independent exhaustive word checks.

## 9. Sharp remaining boundary

The saved neutral family cannot be ranked by outer edge count, DM shore mass,
or canonical component compression.  All three statistics move substantially
while the exact objective, tax localization, residual width, and final word
length stay fixed.

The first unit of tax is the explicit rank-two boundary circuit
`{685,1581}`.  The second is the exact 7267 forced-face obstruction, whose
stored-word geometry demands a nonlocal alternating relocation through the
7683 witness bank.  A useful next carrier move must therefore change the
colored forbidden-circuit structure at one of the two ends, or create an
exact-optimal residual outside the current 41-mask atlas with width at most
19 and a compatible OR--Pascal completion.  Another neutral compression of
the internal DM shore, by itself, has no evidential force.
