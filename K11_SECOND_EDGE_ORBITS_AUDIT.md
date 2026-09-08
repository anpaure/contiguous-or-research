# Independent audit of `K11_SECOND_EDGE_ORBITS.md` and the second-orbit patch

## 1. Verdict

The mathematical four-orbit lemma is correct for the intended unrestricted
ordered fixed-row search on the complete graph `J(11,6)`.  The canonical
prefix

\[
 C=\{0,1,2,3,4\},\qquad
 E=C\cup\{5\},\qquad
 F=E-\{3\}+\{6\}                                  \tag{1.1}
\]

is WLOG for the bit-symmetric final existence problem, and the stabilizer of
this **ordered** prefix has exactly the five coordinate orbits stated in the
source.  After excluding transitions which remove bit `6`, the remaining
second neighbors form exactly four orbits.  The masks

\[
                         126,246,95,215             \tag{1.2}
\]

are the correct representatives.

The implementation also correctly forces the directed arcs

\[
                         F\longrightarrow G_q       \tag{1.3}
\]

despite storing every graph edge with its two **vertex indices** sorted.
The ternary test against `fixed_neighbor` chooses the correct orientation
independently of the input ordering of masks.

The first audited version had one real scope defect in the guard:

```cpp
if(getenv("RECOMBINE_SECOND_ORBIT")&&(!canonicalize||!ordered)) return 9;
```

The boolean `canonicalize` is intentionally also true in some sparse,
seed-dependent candidate graphs when the canonical first edge happens to be
present.  The source comments explicitly say that this sparse use is not a
WLOG symmetry reduction.  Consequently, the first version of the environment
option **could be accepted outside the WLOG full-graph branch**.  For example,
an ordered `ordlazy`, `targetordinc`, or another no-distance sparse mode could pass the
guard if its candidate edge set contains `63--119`; if the requested second
representative is also present, the orbit constraint is silently imposed.

This did not affect the four advertised `allordinc` runs: those use all 462
rank-six masks and all 6930 Johnson edges, so the symmetry argument applies.
It did mean the generic implementation claim “available only inside the
WLOG canonical branch” was false as written.  The source was subsequently
changed to require

```cpp
all_edges && k==11 && rank==6
```

in addition to `canonicalize&&ordered`.  This closes the sparse-mode bug for
the intended 462-mask input.  A literal full-layer check (`n==462` here) is
still an input precondition rather than a code guard.

The final result is therefore:

* **mathematical orbit split:** verified;
* **representatives and directed-arc encoding:** verified;
* **the documented `allordinc` searches:** symmetry-safe;
* **generic option-scope guard:** corrected for sparse modes after the first
  audit; full-layer completeness remains an input precondition.

## 2. Why the existing canonical prefix is WLOG

Assume the intended fixed-row conditions: a Hamilton path through all 462
rank-six masks, 461 pairwise distinct rank-five intersection colors, and
endpoint access to the unique omitted rank-five color.

There are exactly

\[
                         \binom{11}{5}=462           \tag{2.1}
\]

rank-five colors.  The 461 real path edges therefore omit exactly one color,
say `C_0`.  By the endpoint-access condition, one endpoint is a rank-six set

\[
                         E_0=C_0\cup\{e\}.           \tag{2.2}
\]

A permutation of the eleven bit coordinates sends `C_0` to
`{0,1,2,3,4}` and `e` to `5`.  Path reversal then makes this endpoint the
start, giving `C` and `E` in (1.1).

Write the first real transition as

\[
                         E\longrightarrow E-\{r\}+\{s\}. \tag{2.3}
\]

It cannot remove `5`, because that edge would have intersection `C`, the
color declared omitted.  Hence `r` lies in `C`, while `s` lies outside `E`.
The stabilizer of `(C,E)` is transitive on the five coordinates of `C` and
on the five unused coordinates outside `E`.  It can therefore send

\[
                         r\mapsto3,qquad s\mapsto6, \tag{2.4}
\]

which gives

\[
 F=\{0,1,2,4,5,6\}.                                \tag{2.5}
\]

Thus the normalization is WLOG for unrestricted bit-symmetric existence.
It is not WLOG relative to Hamming distance from a fixed labeled seed, which
is why the existing source correctly requires `near_limit<0` before enabling
`canonicalize`.

## 3. Exhaustive stabilizer-orbit classification

The coordinate membership signatures in the ordered triple `(C,E,F)` are

\[
\begin{array}{c|c|c}
\text{coordinates}&(1_C,1_E,1_F)&\text{meaning}\\ \hline
\{0,1,2,4\}&(1,1,1)&\text{common undistinguished bits}\\
\{3\}&(1,1,0)&\text{bit removed by the first edge}\\
\{5\}&(0,1,1)&\text{endpoint-special bit}\\
\{6\}&(0,0,1)&\text{bit added by the first edge}\\
\{7,8,9,10\}&(0,0,0)&\text{fresh outside bits}.
\end{array}                                        \tag{3.1}
\]

These signatures are invariant under every coordinate permutation fixing
`C`, `E`, and `F`.  Conversely, arbitrary permutations inside the first and
last four-element classes fix all three sets.  Hence the stabilizer is
transitive on each row of (3.1), and no two rows can merge.

A Johnson neighbor `G` of `F` is obtained by removing one coordinate of

\[
                         F=\{0,1,2,4\}\sqcup\{5\}\sqcup\{6\} \tag{3.2}
\]

and adding one coordinate of

\[
                         [11]\setminus F=\{3\}\sqcup\{7,8,9,10\}. \tag{3.3}
\]

Before applying the rainbow restriction, this gives `3*2=6` stabilizer
orbits.  Their sizes are

\[
\begin{array}{c|cc}
 &\text{add }3&\text{add fresh}\\ \hline
\text{remove common}&4&16\\
\text{remove }5&1&4\\
\text{remove }6&1&4.
\end{array}                                        \tag{3.4}
\]

The sizes sum to

\[
                         4+16+1+4+1+4=30,           \tag{3.5}
\]

which is exactly the degree

\[
                         6(11-6)=30                 \tag{3.6}
\]

of `F` in `J(11,6)`.  Thus there is no missing removal/addition type.

Section 4 below excludes the last row of (3.4), leaving orbit sizes

\[
                         4,16,1,4,                  \tag{3.7}
\]

and exactly four representatives.

Strictly speaking, the relevant group is the stabilizer which fixes each
member of the ordered data `(C,E,F)`.  The phrase “setwise stabilizer of the
prefix” in the source is harmless here, but “ordered-prefix stabilizer” is
more precise.

## 4. Why removing bit `6` is impossible

The first edge has lower color

\[
 E\cap F=\{0,1,2,4,5\},
 \qquad \operatorname{mask}(E\cap F)=55.           \tag{4.1}
\]

If the second transition removes bit `6`, then for either permitted added
coordinate `b` outside `F`,

\[
 F\cap(F-\{6\}+\{b\})=F-\{6\}=E\cap F.            \tag{4.2}
\]

Thus the second transition has exactly the same rank-five intersection
color as the first.  It violates the required rainbow edge-color sequence.

There is a minor implementation-level nuance between the two excluded
addition classes.

* Removing `6` and adding `3` returns to `E`.  This would traverse the same
  undirected edge backwards.  In the SAT encoding it is already impossible
  because one edge cannot select both directed arc variables and the ordered
  Hamilton path cannot revisit `E`.
* Removing `6` and adding a fresh bit gives a genuinely new edge, but the
  pairwise at-most-one clause for lower color `55` conflicts with the fixed
  first edge.

At the abstract path level both are correctly summarized as repeating the
first lower color.  In the concrete CNF, the first subcase is excluded by the
simple directed-path encoding as well as by the intended rainbow property,
whereas the second relies directly on the lower-color at-most-one clauses.

Those clauses are indeed active whenever `canonicalize` is active.  The
definition of `canonicalize` forces `upper_base=false`; consequently the
branch

```cpp
else if(!upper_base)
    for(auto& list:by_lower) ... clause({-list[i],-list[j]});
```

adds pairwise at-most-one constraints for every lower color.  Clause order is
irrelevant: these constraints may be emitted after the fixed-prefix clauses
without weakening them.

## 5. Representative-mask audit

In decimal,

\[
                         F=119.                     \tag{5.1}
\]

The four code choices give:

\[
\begin{array}{c|c|c|c|c|c}
q&\text{remove}&\text{add}&G_q&F\cap G_q&F\cup G_q\\ \hline
0&0&3&119\mathbin\oplus1\mathbin\oplus8=126&118&127\\
1&0&7&119\mathbin\oplus1\mathbin\oplus128=246&118&247\\
2&5&3&119\mathbin\oplus32\mathbin\oplus8=95&87&127\\
3&5&7&119\mathbin\oplus32\mathbin\oplus128=215&87&247.
\end{array}                                        \tag{5.2}
\]

Each `G_q` has popcount six and differs from `F` in exactly two bits, so
each is a Johnson neighbor.  The two possible lower colors `118` and `87`
are both different from the first lower color `55`.  The table in
`K11_SECOND_EDGE_ORBITS.md` and the bit constants in the C++ patch agree
exactly.

The code constants specialize as follows:

```text
rank                 = 6
common_remove        = 0
endpoint_special     = rank-1 = 5
first_removed        = rank-3 = 3
fresh_outside        = rank+1 = 7
canonical_neighbor   = 119
```

Therefore `orbit<2` chooses the common removal class, `orbit>=2` chooses
the endpoint-special class, parity chooses the two addition classes, and
the orbit numbering matches the document.

## 6. Directed-arc and vertex-index audit

The array `masks` is not sorted numerically.  A mask is translated to a
vertex index by

```cpp
index[mask]
```

and `add_edge` stores an edge as `(min(index_u,index_v),
max(index_u,index_v))`.  Its arc variables have the fixed meanings

```text
arc[id][0] : edges[id].u -> edges[id].v
arc[id][1] : edges[id].v -> edges[id].u.
```

For the second edge, the patch performs the same sorting for lookup and then
uses

```cpp
clause({second_edge.u==fixed_neighbor ?
        arc[second_id][0] : arc[second_id][1]});
```

If the index of `F` is the smaller endpoint, this selects `arc[0]`; if it is
the larger endpoint, it selects `arc[1]`.  In both cases the selected arc is
exactly `F -> G_q`.  No assumption about numeric mask order or input-path
order is present.

As a concrete check in `k11_lower956_upper549.txt`, the zero-based vertex
indices are

```text
mask 63  -> 461
mask 119 -> 460
mask 126 -> 363
mask 246 -> 193
mask 95  -> 267
mask 215 -> 268
```

Thus the stored first edge is `(460,461)`, and the conditional chooses
`arc[1]`, namely `63 -> 119`.  Each stored representative edge has its
representative index first and index `460` second, so the conditional again
chooses `arc[1]`, namely `119 -> representative`.  This concrete ordering is
not needed for correctness; it merely confirms the intended branch on the
current seed.

The selected second arc is genuinely the second transition.  The dummy arc
is fixed as `dummy -> E`, the first real arc is fixed as `E -> F`, and every
vertex has one selected incoming and one selected outgoing arc.  Hence the
fixed outgoing arc from `F` must be the transition immediately following
`E -> F`.  Binary path positions eliminate any disconnected directed
subtour or wraparound interpretation.

## 7. Scope guard and post-audit correction

The existing boolean is

```cpp
const bool canonicalize=near_limit<0&&
    !upper_base&&!lower_base&&!both_base&&
    !rainbow_lower_runs&&
    (all_edges||pairs.count({canonical_u,canonical_v}));
```

The final disjunction has two deliberately different meanings.

1. `all_edges` gives the complete Johnson graph on the supplied rank layer.
   For the intended `k=11` input, the 462 distinct rank-six masks are the
   entire layer, so bit permutations preserve the candidate graph.  This is
   the WLOG branch.
2. `pairs.count(...)` can enable canonicalization in a sparse union of seed
   edges.  A coordinate permutation generally changes that candidate graph,
   so this is only a deliberately restricted portfolio component, not a WLOG
   reduction.

The originally audited guard tested only `canonicalize&&ordered`.  Therefore
the second case passed.  A concrete mode pattern was

```text
RECOMBINE_SECOND_ORBIT=q  ...  ordlazy
```

with a supplied sparse path containing edge `63--119`.  Here

```text
all_edges    = false
ordered      = true
near_limit   = -1
canonicalize = true
```

If the requested representative edge was absent, the later lookup returned
status 9.  If it was present in the sparse candidate union, the clauses were
added with no warning that the decomposition was not WLOG.

After this audit, the source guard was tightened to

```cpp
if(getenv("RECOMBINE_SECOND_ORBIT")&&
   (!canonicalize||!ordered||!all_edges||k!=11||rank!=6)) return 9;
```

Thus `ordlazy`, `targetordinc`, and all other non-`all` modes are now rejected,
as are other dimensions and ranks.  The concrete sparse-mode defect is fixed.

A maximally self-checking guard for this specifically documented feature
would additionally use a boolean such as

```cpp
const bool full_rank_layer = /* every rank-six mask is present */;
const bool second_orbit_wlog =
    ordered && canonicalize && all_edges && full_rank_layer &&
    k==11 && rank==6;
```

The current `all_edges` check is enough for the actual input because it has
462 distinct rank-six masks, necessarily the complete layer.  The program
does not generally verify that fact: `all_edges` means all Johnson edges
**induced by the supplied vertices**, not independently all masks of the
layer.  Adding `n==462` (unique rank-six masks are already checked) would make
the complete-layer scope self-enforcing.

The existing rejection of unordered modes is correct: `!ordered` returns 9
before any orbit clause is added.  Distance modes also remain rejected because
`near_limit>=0` makes `canonicalize=false`.

## 8. Symmetry and the initial target `958`

The advertised run additionally sets

```text
RECOMBINE_TARGETS=k11_initial_targets.txt
```

whose current content is the single rank-eight mask `958`.  A general bit
permutation does not fix this individual decimal mask.  Therefore the
canonicalization is not, by itself, an orbit decomposition of the set of all
**partial base-CNF models which happen only to witness 958**.

This does not invalidate the intended final existence search.  A successful
fixed-row solution must cover every rank-eight mask.  Bit permutation and path
reversal preserve complete rank-eight coverage, so a canonical image of a
genuine final solution still covers `958`.  Likewise, all later run and
complete-shadow gates are bit-symmetric.  Thus four-branch UNSAT of the
advertised full searches can exclude the final fixed-row object even though
the intermediate one-target formula is not itself fully symmetric.

This qualification matters only if one tries to state a theorem about the
round-zero formula in isolation.  The four-orbit result is a theorem about the
ultimate bit-symmetric fixed-row existence problem.

## 9. Final ledger

### Verified

* WLOG normalization of omitted color, containing endpoint, path direction,
  and first real edge for unrestricted fixed-row existence;
* exhaustive stabilizer membership signatures;
* four allowed second-edge orbits after excluding removal of bit `6`;
* masks `126`, `246`, `95`, and `215`;
* correct directed-arc selection after vertex-index sorting;
* lower-color rainbow enforcement in every mode where `canonicalize` is true;
* absence checks for representative vertices and sparse candidate edges; and
* correctness of the described `allordinc` four-way search split.

### Qualification after the implementation correction

* Sparse and wrong-dimension modes are now rejected.  The code still assumes,
  rather than explicitly checks, that the supplied `k=11`, rank-six vertex
  list contains all 462 masks.

### Scope not established by this split

* unrestricted monotone-band solutions;
* central-forest solutions outside the fixed-row ansatz; or
* the original Boolean-array conjecture.

The mathematical four-orbit idea and the corrected guard are ready for proof
use in the specified full `allordinc` search.  A one-line full-layer check
would remove the last avoidable input-scope assumption.
