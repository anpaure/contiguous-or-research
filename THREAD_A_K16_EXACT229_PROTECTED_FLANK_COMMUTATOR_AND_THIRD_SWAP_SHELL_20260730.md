# Exact229 protected-flank commutator and the complete third forward-swap shell

## 1. Scope and verdict

This note concerns only the authenticated K16 word

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
```

of SHA-256

```text
cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974.
```

Let \(\tau_{a,b}^{s}\) denote the forward exchange of the two disjoint
half-open blocks \([a,a+s)\) and \([b,b+s)\).  Put

\[
 a=6611,\qquad b=12718,
\]

and, with the rightmost operation performed first,

\[
Q_{L,\ell}
 =\tau_{a+2,b+3}^{\ell}\tau_{a,b}^{L}Q.
 \tag{1.1}
\]

The following statements are proved below.

1. Among
   \(L\in\{16,18\}\) and \(\ell\in\{9,13,15\}\), exactly

   \[
   (L,\ell)=(16,9),(16,13),(18,9),(18,15)                 \tag{1.2}
   \]

   preserve the fixed-flat middle reconstruction and cover every arbitrary
   upper target.

2. Each of the four words has matching size \(26308\), hence Hall
   deficiency \(24\).  In every case the new augmenting edge is the same:
   the physical singleton cell \([12720,12721)\), labelled by source
   occurrence \((6613)\), hosts lower target `8000` with

   \[
   (\mathrm{allowed},\mathrm{mandatory})=(\mathtt{8a0e},\mathtt{8000}).
   \tag{1.3}
   \]

3. A complete fixed-flat third-forward-swap audit was made in the natural
   three-row rail collars.  It tests every disjoint equal-length pair of
   blocks, on the same rail or on opposite rails, with both blocks contained
   in the expanded rail collars and meeting the corresponding outer support.
   Of \(22334\) cases, \(246\) are middle-exact.  Among those, \(54\) host
   none of the twelve exact229 zero targets, \(192\) host exactly one, and
   none hosts two.  Thus this precise third-swap shell cannot both retain the
   `8000` service and create service for a second exact229 zero target.

The two-zero-provider condition in item 3 is the prescribed necessary gate
for the direct-service architecture.  It is not by itself sufficient for a
second augmentation: two targets may have only a common right neighbour or
remain trapped in a deficient cut.  Nor is it a necessary characterization
of every graph with Hall deficiency at most \(23\).

The last statement is deliberately not a global Hall no-go.  It does not
exclude an augmentation through a target that already had positive degree,
a reversal, unequal blocks, a moving-flat trade, a block leaving the stated
collars, or two further interacting swaps.

## 2. The block-word identity

On occurrence tokens, set

\[
 O_L=\prod_{j=0}^{L-1}(a+j\ \ b+j),\qquad
 I_\ell=\prod_{j=0}^{\ell-1}(a+2+j\ \ b+3+j).            \tag{2.0}
\]

The transpositions within either product commute, but the two products do
not.  Applying the outer exchange and then the inner exchange transports
tokens by \(I_\ell O_L\); equivalently, the final word is the pullback by
\(O_LI_\ell\).  This records the occurrence multiset exactly and prevents
the two overlapping swaps from being mistaken for independent marginal
changes.

Write

\[
 X=Q[a,a+L),\qquad Y=Q[b,b+L).
\]

### Lemma 2.1 (nested exchange normal form)

If \(0\leq\ell\leq L-3\), then the two changed outer blocks of
\(Q_{L,\ell}\) are exactly

\[
\begin{aligned}
 Q_{L,\ell}[a,a+L)
   &=Y[0,2)\;X[3,3+\ell)\;Y[2+\ell,L),\\
 Q_{L,\ell}[b,b+L)
   &=X[0,3)\;Y[2,2+\ell)\;X[3+\ell,L).
                                                        \tag{2.1}
\end{aligned}
\]

In particular, if

\[
 r=L-\ell-3,                                             \tag{2.2}
\]

then the right outer block has an \(X\)-flank of length \(r\) between the
inner terminal seam and the outer terminal seam, while the corresponding
left flank has length \(r+1\).

#### Proof

After the outer exchange, the left block is \(Y\) and the right block is
\(X\).  The inner exchange starts at offsets two and three, so it exchanges
\(Y[2,2+\ell)\) with \(X[3,3+\ell)\).  Concatenating the untouched prefixes
and suffixes gives (2.1).  The suffix lengths are immediate. \(\square\)

The useful cancellation is now visible.  When \(r=0\), the right inner
terminal seam coincides with the right outer terminal seam: the last
\(X\)-flank disappears.  Formula (2.1) reduces to

\[
 Y[0,2)X[3,L)Y[L-1,L),\qquad X[0,3)Y[2,L-1).             \tag{2.3}
\]

When \(r\geq4\), the two terminal dependency collars are separated by a
protected forward flank.  The two accepted long-flank cases have

\[
 (L,\ell,r)=(16,9,4),(18,9,6),                           \tag{2.4}
\]

and the two cancellation cases have

\[
 (L,\ell,r)=(16,13,0),(18,15,0).                         \tag{2.5}
\]

The remaining pairs have \(r=-2\) and \(r=2\), respectively.  Thus the
four observed survivors are not four unrelated finite accidents: they are
exactly the two protected-flank instances and the two common-end
cancellations in the displayed parameter set.

Here `(16,15)` has \(r=-2\), so its inner block overshoots the outer block
and lies outside Lemma 2.1; only the direct replay (3.4), not the normal-form
argument, rejects it.  The pair `(18,13)` is the genuine short-flank
collision with \(r=2\).

## 3. Why endpoint signatures suffice

The only flats of \(Q\), and of all four surviving words, are

\[
 6320,12869,12871.                                       \tag{3.1}
\]

Both rails in (1.1) therefore lie at depth two.  If \(T_i\) denotes the
rank-eight row at position \(i\), its physical cell envelopes in this phase
are

\[
 E_j=T_{j-2}\cap T_{j-1}\cap T_j,                        \tag{3.2}
\]

and exact middle reconstruction is

\[
 T_i=E_i\cup E_{i+1}\cup E_{i+2}.                        \tag{3.3}
\]

Consequently a changed seam can affect only a bounded five-row signature.
An oriented substring moved without reversal retains every internal
signature; only the new concatenation seams require replay.  More generally,
the implementation uses the conservative global radius three, so checking
the two changed block collars proves full replay whenever the flat schedule
is fixed.

For (2.4), the inner and outer terminal collar checks are disjoint.  For
(2.5), there is no intermediate right terminal seam to check.  Direct
substitution into (3.2)--(3.3) verifies all remaining start and left-terminal
signatures.  The two rejected cases fail at the following exact rows:

\[
\begin{array}{c|c|c}
(L,\ell)&\text{row target}&\text{reconstructed value}\\ \hline
(16,15)&6627:\mathtt{4db4}&\mathtt{4da4}\\
       &12735:\mathtt{cd25}&\mathtt{4d25}\\
(18,13)&12734:\mathtt{cd25}&\mathtt{4d25}\\
       &12735:\mathtt{cda4}&\mathtt{4da4}.
\end{array}                                               \tag{3.4}
\]

Thus `(16,15)` is rejected before the upper or Hall gates, and `(18,13)` is
also rejected even though its arbitrary-upper deck happens to remain
complete.  The former additionally loses upper target `cda5`.

For each survivor, arbitrary-upper completeness is checked by the exact
one-pass interval-OR recurrence: keep the distinct ORs of intervals ending
at the previous position, OR each with the new row, add the singleton, and
mark every rank-above-eight value reached.  The terminal marked set contains
every such mask.  This is a full arbitrary-length check, not a bounded-window
test.

## 4. The common `8000` augmentation

The first three rows in the right outer block are independent of \(L\) and
\(\ell\), because the inner exchange begins only at offset three:

\[
 (T_b,T_{b+1},T_{b+2})
   =(\mathtt{ca2e},\mathtt{8a6e},\mathtt{8a4f}).           \tag{4.1}
\]

Therefore

\[
 E_{b+2}=T_b\cap T_{b+1}\cap T_{b+2}=\mathtt{8a0e}.      \tag{4.2}
\]

The complete five-envelope collar is

\[
 (E_b,E_{b+1},E_{b+2},E_{b+3},E_{b+4})
 =(\mathtt{482e},\mathtt{0a2e},\mathtt{8a0e},
   \mathtt{0a4e},\mathtt{024f}).                         \tag{4.2a}
\]

Only owner rows \(b,b+1,b+2\) can make a bit mandatory in the singleton
cell \(b+2\).  For each of these rows, subtracting the union of its other
two carrier envelopes from \(E_{b+2}\) leaves exactly `8000`.  Hence the
union of all forced bits is exactly, not merely at least, `8000`.  This
proves the full mandatory equality in (1.3).  The physical position
\(b+2=12720\) carries the original occurrence at row \(a+2=6613\); hence
the right vertex is \((6613)\).

The exact matching symmetric difference from exact229 contains the common
augmenting path

\[
\mathtt{8000}
 -(6613)-\mathtt{8a0c}
 -(6724)-\mathtt{8e0c}
 -(11217).                                                \tag{4.3}
\]

It raises matching size from \(26307\) to \(26308\).  All four words have

\[
 \text{deficiency}=24,\qquad
 \text{zero-target term}=11,\qquad
 \text{shared-component term}=13.                        \tag{4.4}
\]

For comparison, either outer swap alone, with \(L=16\) or \(L=18\), is
middle-exact and arbitrary-upper-complete but has the unchanged ledger

\[
 (\text{matching},\text{zero term},\text{shared term})
   =(26307,12,13).                                       \tag{4.5}
\]

Thus the outer transport is Hall-neutral.  The nested swap performs exactly
the `8000` augmentation while leaving the shared term fixed.

Their remaining zero targets are

```text
2665 28e9 291d 29a9 2f28 4879 48e9 4e70 6989 6a29 6c70.
```

## 5. Complete third forward-swap shell

Fix one of the four words.  A third move in the audited shell exchanges two
disjoint forward blocks of a common length \(s\).  Each block is contained
in one of

\[
 [a-3,a+L+3),\qquad [b-3,b+L+3),                         \tag{5.1}
\]

and intersects the corresponding core \([a,a+L)\) or \([b,b+L)\).
Both same-rail and cross-rail pairs are included.  The range
\(1\leq s\leq24\) is exhaustive because the larger expanded rail has length
\(18+6=24\).

For completeness, let \(n_L(s)\) be the number of legal starts on one rail.
The half-open intersection inequalities give

\[
n_L(s)=
\begin{cases}
L,&s=1,\\
L+1,&s=2,\\
L+2,&s=3,\\
L+7-s,&4\leq s\leq L+6,\\
0,&s>L+6.
\end{cases}                                               \tag{5.2}
\]

There are \(n_L(s)^2\) cross-rail pairs.  On the two rails together, the
number of same-rail disjoint pairs is

\[
 (n_L(s)-s)_+(n_L(s)-s+1)_+.                             \tag{5.3}
\]

Summing (5.2)--(5.3) gives \(4803\) cases for each \(L=16\) state and
\(6364\) for each \(L=18\) state.  Since there are two accepted values of
\(\ell\) for each \(L\), the exact total is

\[
 2(4803+6364)=22334.                                     \tag{5.4}
\]

### Theorem 5.1 (rail-collar second-zero obstruction)

Within the shell just defined, no third swap produces a fixed-flat
middle-exact word having providers for two distinct members of the twelve
exact229 zero targets.

#### Proof

All \(22334\) block pairs in (5.4) are replayed.  A candidate is retained
only if its flat list remains (3.1) and both changed dependency collars pass
(3.3).  Local replay is full replay: outside the radius-three closures of the
two swapped blocks, every row and every envelope is unchanged.

Exactly \(246\) candidates pass.  For each, every compiler cell in the full
dependency closures of (5.1) is tested against all twelve zero targets by
the exact cell criterion

\[
 M_C\subseteq T\subseteq A_C,
 \qquad E_p\cap T\ne\varnothing\quad(p\in C).             \tag{5.5}
\]

Cells outside those closures are unchanged from exact229 and hence cannot
acquire a provider for a base zero target.  The resulting distinct-target
histogram is

\[
 0^{54},\qquad 1^{192},\qquad (\geq2)^0.                 \tag{5.6}
\]

The exact per-state breakdown is

\[
\begin{array}{c|c|r|r|r|r|r}
L&\ell&\text{tested}&\text{exact}&\text{upper-complete}
 &\text{provider 0}&\text{provider 1}\\ \hline
16&9 &4803&36&7 &11&25\\
16&13&4803&74&8 &15&59\\
18&9 &6364&50&10&13&37\\
18&15&6364&86&6 &15&71.
\end{array}                                               \tag{5.7}
\]

Moreover, in every one-provider row the sole target is still `8000`.
Thus the shell never even shuttles the direct service from `8000` to another
base-zero target; it either retains `8000` or destroys all twelve services.

This proves the claim. \(\square\)

The exact closure scanned on each rail is

\[
 [a-6,a+L+7),\qquad [b-6,b+L+7).                         \tag{5.6a}
\]

Indeed, the last changed target can be at \(a+L+2\); at depth two it can
alter envelopes through \(a+L+4\), and a changed carrier interval can alter
the mandatory signature of a singleton beginning as late as \(a+L+6\).
The left endpoint \(a-6\) follows symmetrically from the first changed
target at \(a-3\).  An earlier production scan ended at the exclusive bound
\(a+L+6\) and was therefore one cell short.  The corrected independent scan
uses (5.6a); the counts in (5.6)--(5.7) are its replayed counts.

The superseded first production pass placed the arbitrary-upper test
downstream of the two-provider gate, so its `upper_complete=0` did not
classify the exact words.  The corrected production v2 and the independent
all-exact replay in (5.7) both show that \(31\) of the \(246\) exact words
are arbitrary-upper-complete; none has a second zero-target provider.

### Corollary 5.2 (the minimal boundary-aligned escape)

Put

\[
 S_4=\tau_{6608,12714}^{3}.
 \tag{5.8}
\]

For each of the four parents \(Q_{L,\ell}\) in (1.2), the word
\(S_4Q_{L,\ell}\) preserves the occurrence multiset, the flat schedule, and
the exact middle reconstruction.  Its compiler graph contains the two
distinct base-zero provider edges

\[
 \mathtt{8000}-(6613),\qquad
 \mathtt{4e70}-(12714,12715),                            \tag{5.9}
\]

and has

\[
 \nu=26309,\qquad
 \operatorname{def}=23,qquad
 (Z,\text{shared})=(10,13).                             \tag{5.10}
\]

It is not an admissible final carrier: its sole arbitrary-upper hole is
`4e79`.

The move (5.8) is outside Theorem 5.1.  Its left block
\([6608,6611)\) ends at, but does not intersect, the left core
\([6611,6611+L)\).  Its right block \([12714,12717)\) starts one position
before the expanded right collar in (5.1), whose left endpoint is
\(12715\), and is separated by the row \([12717,12718)\) from the right
core.  Thus (5.8) is a genuine boundary escape, not a missing case of the
core-meeting census.

Within the fixed-start forward boundary-aligned family

\[
 \tau_{6608,12714}^{s},\qquad s=1,2,3,                  \tag{5.11}
\]

length three is minimal.  For every parent, \(s=1\) fails exact replay at
rows \(6609,6610,12714\), and \(s=2\) fails it at rows
\(6610,12714,12715\).  At \(s=3\) every row replays exactly, and the sole
upper loss is `4e79`.  This is only a minimum in the family (5.11), not a
global minimum over arbitrary third moves.

#### Proof

The length-one and length-two failures are the same for all four parents:

\[
\begin{array}{c|c}
s&\text{failed reconstructions}\\
\hline
1&6609:\mathtt{cc3c}\mapsto\mathtt{4c3c},\quad
  6610:\mathtt{cc2e}\mapsto\mathtt{4c2e},\quad
  12714:\mathtt{ce38}\mapsto\mathtt{4e38},\\
2&6610:\mathtt{cc2e}\mapsto\mathtt{4c2e},\quad
  12714:\mathtt{ce38}\mapsto\mathtt{4e38},\quad
  12715:\mathtt{cc3c}\mapsto\mathtt{4c3c}.
\end{array}                                               \tag{5.12}
\]

At length three the transported endpoint words complete precisely these
three missing high-bit contributions, so the radius-three replay is exact.
The full arbitrary-interval recurrence then finds exactly the missing mask
`4e79`.  Rebuilding the occurrence-labelled compiler graph verifies both
edges in (5.9); the first is the protected edge from Section 4, while the
second is the new occurrence cell with source rows \((12714,12715)\).
Maximum matching gives (5.10).  The exact four-parent replay and the scoped
\(s=1,2,3\) endpoint replay are recorded in the authenticated artifacts
listed in Section 7. \(\square\)

Consequently the sharp next gate is a return move, not another marginal
provider count: it must restore `4e79` while retaining both edges (5.9) and
a size-\(26309\) matching containing them.  This boundary `4e70` service is
distinct from the conditional remote `6a29` halo in (6.2).

## 6. Exact requirement on the next move

Let

\[
 e_0=\bigl(\mathtt{8000},(6613)\bigr)                    \tag{6.0}
\]

be the protected edge.  If \(G'\) is the fully rebuilt compiler graph after
an arbitrary further physical braid, then there is a matching of size at
least \(26309\) **containing** \(e_0\) if and only if

\[
 e_0\in E(G')\quad\hbox{and}\quad
 \nu\bigl(G'-\{\mathtt{8000},(6613)\}\bigr)\ge26308.     \tag{6.1}
\]

Indeed, delete \(e_0\) from such a matching for necessity, and adjoin it to
a matching in the vertex-deleted graph for sufficiency.  Unlike a statement
about an augmenting path relative to the old matching, (6.1) remains exact
when the new braid deletes old edges.

If the braid retains every edge of a chosen size-\(26308\) matching obtained
from (4.3), then Berge's criterion gives the familiar equivalent sufficient
test: create a further augmenting path.  A marginal new provider is still
not enough if the same braid deletes an edge used by (4.3) or by the return
path.

A strong occurrence-labelled sufficient condition under edge preservation is
therefore:

1. retain every edge of one chosen size-\(26308\) matching containing
   \(e_0\), in particular all matching edges selected along (4.3), rather
   than only the local signature at \((6613)\); and
2. create an augmenting path relative to that retained matching, with its
   new service vertices avoiding (4.3), while preserving exact middle replay
   and the arbitrary-upper deck.

Two exact graph-level ports are already known.  If they can be realized by
one physical chronology, then

\[
\begin{aligned}
 &\mathtt{6a29}-(4654,4655,4656),                         \tag{6.2}\\
 &\mathtt{5a29}-(6025,6026,6027)-\mathtt{4a29}
                   -(4655,4656)                          \tag{6.3}
\end{aligned}
\]

are augmenting paths disjoint from (4.3).  Adding either displayed terminal
edge lowers deficiency to \(23\); adding both lowers it to \(22\).  Thus a
successful third nested or crossed braid need not guess an aggregate Hall
score: it must physically realize an occurrence-labelled DM exit of this
kind, or another \(M_1\)-augmenting path, without sacrificing the `8000`
path.

The port (6.2) is the mandated second-zero service: together with
`8000-(6613)` it serves two distinct exact229 zero targets.  The port (6.3)
is different: `4a29` already has positive degree, so it is a nonzero-target
DM exit through the shared deficient component.  It proves why the
two-zero-provider gate is sufficient but not necessary for Hall descent.

Theorem 5.1 shows that a single forward equal-block exchange confined to the
two rail collars cannot do this by serving a second base-zero target.  It
does **not** test every possible nonzero-target DM exit, so it does not rule
out Hall-23 inside the shell by a more subtle rewiring.  The minimum honest
next alternatives are therefore:

* close the sole `4e79` debt of Corollary 5.2 while retaining both provider
  edges in (5.9);
* test the full matching change of the \(246\) exact shell survivors;
* allow one reversed or unequal third block;
* reach the remote `6a29`/`4a29` halo; or
* use two interacting additional swaps.

## 7. Adversarial audit and provenance

The third-swap implementation was checked independently as follows.

* Formula (5.2) reproduces its `tested=22334` count exactly.
* Its start loops are contiguous and duplicate-free, and (5.3) accounts for
  every disjoint same-rail and cross-rail pair.
* The fixed-flat guard makes the inherited depth vector legitimate.
* A changed row can affect only the radius-three closures explicitly
  replayed, so the local/full implication is sound.
* The original production provider scan was one cell short on the right.
  Production v2 and the corrected independent scan both use the exact
  closure (5.6a) and leave the histogram unchanged.
* A local recompilation and replay of the frozen source reproduced

  ```text
  tested=22334 changed=22334 exact=246
  provider_target_hist=0:54,1:192 two_provider=0.
  ```

The principal scope caveat is logical, not computational: “no second zero
target” is only a necessary obstruction to the intended direct-service
architecture.  It is not equivalent to “no second matching augmentation.”

The boundary escape in Corollary 5.2 is independently pinned by the
following scoped artifacts:

```text
scratch/audit_threadA_k16_exact229_boundary_s123_20260730.cpp
  SHA-256 56e761dfc8196cd852b65b1f0b45fa97e1b16d2ba92067ba92eb3fddbae9371a
scratch/threadA_k16_exact229_boundary_s123_20260730.audit.tsv
  SHA-256 02a5bd2b08cad5330e118e1b65fc1cb232cab283ee47c61ed9e39f9ea593aed5
scratch/k16_nested_hall24_commutator_and_third_swap_20260731.audit.json
  SHA-256 882063eeda7e94d10d4918225d7f779f78210b844da34b3e3d1064401752c1cf
```

The first two prove only the fixed-start \(s=1,2,3\) reconstruction and
upper-deck statements.  The third supplies the four separate Hall-23
replays after composition with the accepted parents; this distinction
prevents the standalone `S4` Hall-24 audit from being misread as the
three-swap Hall ledger.

To avoid concurrent hash drift in the upstream audit, the principal bytes
used here were copied into the frozen bundle

```text
scratch/threadA_k16_exact229_commutator_frozen_20260730/
```

whose manifest is

```text
SHA256SUMS
  SHA-256 c19144e651536c9a9a0b83e7d1d65edc3c182bcc1377df695bba2cf4884276d7
```

The C++ audit sources and both transitive C++ helpers are present in this
bundle.  The frozen Python audit is a byte snapshot, not a self-contained
Python environment: its imported compiler/Hall helpers remain at their
canonical project paths.  The JSON result and the independent C++ replays
are frozen separately, so no claim below treats that Python snapshot as a
standalone reproducer.

Principal frozen inputs and outputs:

```text
third_forward_swap.cpp
  SHA-256 358183cbdf6b2dbb260912d268b096ab198bb3e786b20f90224685f4668629c1
third_forward_swap.run.stderr
  SHA-256 b1bca0e82dbae87e43db6cc9c7497d30c479dcfac59ab3cebb1f2667046b694e
third_forward_swap.audit.json
  SHA-256 9063a9fa4e5a5c57eb73b26caa8f371887e87b16c2c9a1b4ed0d5fd98bb59386
six_case.audit.cpp
  SHA-256 f5280fa8b4785ec17244ef57c2d3544f559fe5b6960faaae3093a15bdb1fb1e6
six_case.audit.tsv
  SHA-256 c188b003ebeb9f6e8221816c8954ef5eaf8729547d74b4b6f0e7ade9240f03ae
third_breakdown.audit.cpp
  SHA-256 4467b435dd2c5fc61aeddda04b1a7e1cef189661b6198e1a6cead3ea81326e7f
third_breakdown.audit.tsv
  SHA-256 6d1bc6fb50492d9571111e7775d3b36da164213fc34d6b2e056577887485e4fe
nested_swap_three_path_port.audit.py
  SHA-256 3bde8f687b758b4e262e4cc52429e3e1d670653bd5d25d4e2b57cee05616aebb
nested_swap_three_path_port.audit.json
  SHA-256 69263c9b13e1b811480a0d45a78a81dd049af4d621d25e9b3bfdab899f4f8da3
```
