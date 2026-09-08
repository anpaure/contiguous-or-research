# Independent audit: left-anchored maximal shadows and the single-switch reservoir

## Verdict

**PASS, with scope qualifications but no mathematical correction to the stated
theorems.**

The following claims were independently derived and checked.

1. For an arbitrary left-anchored schedule

   \[
   I_i=[i,\rho_i],\qquad \rho_1<\cdots<\rho_M,
   \]

   the coordinatewise maximal factor realizes every nonempty consecutive
   central meet on the literal common physical core.  This is exact, not just
   a containment bound.
2. Every factor realizing the central row realizes every consecutive central
   join on the literal hull of the corresponding central intervals.
3. For the canonical one-switch schedule at rank-count length, the short
   cells partition exactly into the `sigma` shortened central cells, the
   nontrivial meet cores, and a boundary reservoir of size `d(d+1)`.
4. The maximal factor collapses that reservoir to at most `3d-1` values.  It
   therefore misses at least `(d-1)^2` lower masks for every `d>=2` under the
   hypotheses of Proposition 3.2.
5. Replacing the maximal factor by a sparser factor cannot damage any upper
   consecutive-join witness, provided the replacement still realizes every
   prescribed central interval exactly.

The `k=11` and `k=14` reservoir cells and all associated counts are correct.
The general portal-height and odd middle-level forest statements in Sections
4--5 also pass a consistency check.

Three qualifications matter.

* The quadratic no-go theorem is for the canonical single-switch schedule
  (3.1), with (3.4)--(3.5), not for every possible variable-band schedule.
* An arbitrary deletion from `A^max` need not preserve upper witnesses.  The
  deletion is safe exactly when the resulting array remains a factor of the
  same central row.
* The `O(kd^2)` statement in Theorem 3.6 counts the affected pin conditions
  after a reservoir labeling has been selected.  It does not count all
  possible reservoir-label assignments and is not an existence theorem for
  such an assignment.

## 1. Exact legal positions for one coordinate

Fix a coordinate `x` and a maximal positive incidence run `[a,b]` in
`C_1,...,C_M`.  When the run is internal, the negative intervals before it
have union

\[
[1,\rho_{a-1}],
\]

and the negative intervals after it begin at `b+1`.  Hence the legal
positions capable of serving this run are exactly

\[
K_{a,b}=[\rho_{a-1}+1,b].                         \tag{1.1}
\]

Every positive interval `I_i`, `a<=i<=b`, meets (1.1) whenever it is
nonempty: strict increase gives

\[
\rho_i\ge\rho_a\ge\rho_{a-1}+1,
\]

and `i<=b`.  Therefore an internal run is realizable exactly when

\[
\rho_{a-1}+1\le b.                               \tag{1.2}
\]

A left-boundary run has no preceding negative interval and a right-boundary
run has no following negative interval, so the corresponding one-sided
versions are always realizable.  Coordinates are independent.  This proves
both necessity and sufficiency of the run condition used in Section 1 of the
source.

It also proves that

\[
A_j^{\max}=\{x:j\notin I_i\text{ for every }i\text{ with }x\notin C_i\}
\]

is the coordinatewise largest factor.  Positions outside every prescribed
central interval, if any, are harmless for the identities below; in the
single-switch schedule the central intervals cover all of `[1,M+d]` anyway.

## 2. Exact meet identity

For `p<=q`, strict increase of the right endpoints gives

\[
J_{p,q}=\bigcap_{i=p}^q I_i=[q,\rho_p].           \tag{2.1}
\]

Assume this core is nonempty, i.e. `q<=rho_p`.

If `x` is absent from some `C_i`, `p<=i<=q`, then every position of
`J_(p,q)` lies in the negative interval `I_i`; hence `A^max` contains no copy
of `x` on the core.

Conversely, suppose `x` belongs to every `C_p,...,C_q`, and let `[a,b]` be
the positive run containing that block.  For an internal run, compare the two
integer intervals

\[
K=[\rho_{a-1}+1,b],\qquad J=[q,\rho_p].
\]

All four cross inequalities hold:

\[
\rho_{a-1}+1\le b                         \quad\text{by factorability},
\]

\[
q\le\rho_p                               \quad\text{by core nonemptiness},
\]

\[
\rho_{a-1}+1\le\rho_p                    \quad\text{because }a\le p,
\]

and

\[
q\le b                                   \quad\text{because }q\le b.
\]

Thus `K intersect J` is nonempty.  A legal copy of `x` occurs on the common
core.  Boundary runs only remove one obstruction and give the same
conclusion.  Coordinatewise,

\[
\boxed{
 \bigcup_{j=q}^{\rho_p}A_j^{\max}
   =\bigcap_{i=p}^q C_i
}
\]

whenever `q<=rho_p`.  There is deliberately no assertion when the physical
core is empty.

## 3. Exact hull/join identity for every factor

The intervals `I_p,...,I_q` overlap or abut in the integer line, so

\[
H_{p,q}=\bigcup_{i=p}^qI_i=[p,\rho_q].            \tag{3.1}
\]

Let `A` be any factor realizing all central intervals exactly.  Since every
`I_i` lies in `H_(p,q)`, central realization gives

\[
\bigcup_{i=p}^q C_i\subseteq\bigcup_{j\in H_{p,q}}A_j.
\]

Conversely, every physical position `j` of the hull lies in at least one
`I_i`, `p<=i<=q`.  Exact realization forces `A_j subseteq C_i`; otherwise
that central target would be contaminated.  Hence

\[
\boxed{
 \bigcup_{j=p}^{\rho_q}A_j
   =\bigcup_{i=p}^q C_i
}.                                               \tag{3.2}
\]

This proves the upper-shadow preservation claim in its exact scope.  A sparse
repair may delete any occurrences it likes, but it must continue to realize
each `I_i` as `C_i`.  Under that condition no individual upper witness needs
to be protected separately.

## 4. Single-switch run rule and feasible cores

For

\[
\rho_i=\begin{cases}
i+d-1,&i\le\sigma,\\
i+d,&i>\sigma,
\end{cases}
\]

condition (1.2) becomes

\[
|[a,b]|\ge
\begin{cases}
d,&a\le\sigma+1,\\
d+1,&a\ge\sigma+2,
\end{cases}
\]

for internal runs.  This agrees with the independently proved mixed-delay
criterion in `K11_PORTAL_EMBEDDING_MATH_NEXT.md` when `d=3`.

Likewise a core beginning at central index `p` remains nonempty through
exactly

\[
q-p\le d-1\quad(p\le\sigma),
\qquad
q-p\le d\quad(p>\sigma).
\]

No off-by-one error occurs at the switch: a run beginning at `sigma+1`
still sees the shortened preceding interval and therefore needs only `d`
positive targets.

## 5. Exact short-cell partition

Assume `0<=sigma<=M-d`.  Early starts `p<=sigma` have `d-1` nontrivial
meet cores.  Late starts `sigma<p<=M-d` have `d`, and the final `d` starts
have `d-1,d-2,...,0`.  Therefore

\[
\begin{aligned}
N_{\rm meet}
 &=\sigma(d-1)+(M-d-\sigma)d+\binom d2\\
 &=dM-\sigma-\binom{d+1}{2}.                     \tag{5.1}
\end{aligned}
\]

At rank-count length,

\[
\sigma=dM+\binom{d+1}{2}-L,
\]

so

\[
N_{\rm meet}=L-d(d+1).                           \tag{5.2}
\]

The number of all physical intervals of lengths at most `d` in
`n=M+d` positions is

\[
d(M+d)-\binom d2=dM+\binom{d+1}{2}=L+\sigma.
\]

After removing the `sigma` shortened central cells and the meet cores, the
remainder has

\[
(L+\sigma)-\sigma-[L-d(d+1)]=d(d+1)              \tag{5.3}
\]

cells.

The geometric description is also exact.  The central right endpoints omit

\[
1,2,\ldots,d-1,\quad\sigma+d.
\]

Short cells ending at these omitted endpoints number

\[
\binom d2+d=\binom{d+1}{2}.
\]

The intervals wholly contained in `[M+1,M+d]` form the other triangle of
size `binom(d+1,2)`.  The condition `sigma<=M-d` keeps the two pieces
disjoint.  Every other short cell has a unique central right endpoint and is
either its shortened central interval or the core `[q,rho_p]` of a unique
nontrivial central block.  This proves an actual partition, not just a count.

## 6. Maximal boundary collapse

The three reservoir pieces behave as follows in the maximal factor.

* At the left boundary,

  \[
  A_t^{\max}=C_1\cap\cdots\cap C_t,
  \qquad1\le t\le d-1.
  \]

  These entries decrease with `t`, so every interval inside `[1,d-1]` has
  OR equal to its leftmost entry.  There are at most `d-1` values.
* At the terminal boundary,

  \[
  A_{M+s}^{\max}=\bigcap_{i=M+s-d}^M C_i,
  \qquad1\le s\le d.
  \]

  These entries increase with `s`, so every interval inside
  `[M+1,M+d]` has OR equal to its rightmost entry.  There are at most `d`
  values.
* The omitted switch-endpoint column contains exactly `d` physical cells, so
  it contributes at most `d` additional values.

Thus the entire reservoir assumes at most

\[
3d-1                                                   \tag{6.1}
\]

distinct OR-values.  All rank-below-`r` masks must use intervals of length at
most `d`: any interval of length at least `d+1`, starting at `a`, contains
the selected rank-`r` witness `I_a`.  Therefore the number of distinct lower
masks obtainable from `A^max` is at most

\[
[L-d(d+1)]+(3d-1)=L-(d-1)^2.                    \tag{6.2}
\]

This proves the claimed deficit.  It is a worst-case upper bound; collisions
between meet cores and reservoir values can make the actual deficit larger.
For every `d>=2`, the canonical maximal factor is consequently non-universal.

The conclusion must not be exported to arbitrary monotone schedules: the
proof uses both the exact single-switch partition and the two nested boundary
triangles.

## 7. Sparse repair and the residual pin gate

Assign the missing `d(d+1)` lower masks bijectively to the reservoir.  For a
coordinate `x`, deleting every reservoir interval whose new label omits `x`
changes the central legal set only inside

\[
\Omega=[1,d-1]\cup[\sigma+1,\sigma+d]\cup[M+1,M+d],
\qquad|\Omega|\le3d-1.
\]

The source's set `Z'_x` is exactly the legal set after these extra negative
constraints.  The three positive-pin families in (3.15) are then precisely
the coordinatewise interval-stabbing criterion for the central cells, the
selected meet cores, and the new reservoir labels.  Negative meet-core
constraints are redundant: if `x` is absent from a central intersection,
some central interval in that block already forbids it on the entire core.

Any positive central or meet-core interval disjoint from `Omega` retains its
old maximal-factor pin automatically.  Only `O(d)` central intervals and
`O(d^2)` physical short cores intersect three zones of total length `O(d)`.
Thus there are `O(kd^2)` affected coordinate/interval tests after the
reservoir labels have been chosen.  This is a localization theorem, not a
proof that a suitable bijection of masks to reservoir cells exists.

Once these local pins pass, equation (3.2) proves that all upper joins survive
without further constraints.

## 8. Finite arithmetic checks

### `k=11`

Here

\[
(M,d,\sigma,L)=(462,3,369,1023).
\]

The counts are

\[
\begin{array}{c|r}
\text{object}&\text{count}\\ \hline
\text{all length-at-most-three cells}&465+464+463=1392\\
\text{shortened central triples}&369\\
\text{nontrivial meet cores}&1023-3\cdot4=1011\\
\text{reservoir}&12
\end{array}
\]

and `369+1011+12=1392`.  The reservoir is exactly

\[
[1,1],[1,2],[2,2],
\]

\[
[370,372],[371,372],[372,372],
\]

together with the six intervals in `[463,465]`.  Its maximal-factor values
number at most

\[
3d-1=8.
\]

Consequently `A^max` covers at most `1011+8=1019` of the `1023` lower masks:
at least four are missing, agreeing with `(d-1)^2=4`.

The local modification zone is

\[
[1,2]\cup[370,372]\cup[463,465],
\]

of exact size eight.

### `k=14`

Here

\[
(M,d,\sigma,L)=(3432,2,392,6475).
\]

The counts are

\[
\begin{array}{c|r}
\text{object}&\text{count}\\ \hline
\text{all singleton/pair cells}&3434+3433=6867\\
\text{shortened central pairs}&392\\
\text{nontrivial meet cores}&6475-2\cdot3=6469\\
\text{reservoir}&6
\end{array}
\]

and `392+6469+6=6867`.  The six cells are

\[
[1,1],\quad[393,394],[394,394],
\]

\[
[3433,3433],[3433,3434],[3434,3434].
\]

The reservoir has at most `3d-1=5` maximal-factor values, so at least one of
the `6475` lower masks is absent.  The exact local zone is

\[
[1,1]\cup[393,394]\cup[3433,3434],
\]

of size five.

These checks are structural arithmetic, not constructions of optimal arrays.

## 9. Spot-check of the saturated portal consequences

Under the stronger assumption that every short-window value is distinct and
the short band consists of all lower masks plus the `sigma` selected
rank-`r` masks, the family in (4.2) has exactly `M+1` cells.  Any short cell
outside that family can be strictly enlarged while remaining a noncentral
short cell, so its rank is at most `r-2`.  Hence all rank-`(r-1)` masks lie in
that family and exactly

\[
\delta=M+1-\binom{k}{r-1}
\]

of its cells are lower defects.

For adjacent early or late rank-`r` central values, a shared candidate cell
of rank `r-1` is their exact intersection, forcing their union to have rank
`r+1`.  Across both blocks only `delta` internal transitions can exceed that
height.  The portal capacity inequality

\[
\sigma\le\binom{k}{r+1}+\delta+1
\]

therefore follows.  In odd dimension at the upper middle rank, `delta=1`.
Deleting the unique lower candidate defect from the two alternating physical
paths leaves two components when it was an endpoint and three when it was
internal.  The edge and vertex counts in Section 5 are correct.

These are consequences of short-band saturation.  They do not apply to the
weaker maximal-shadow construction theorem unless those extra distinctness
and grading hypotheses are imposed.

## 10. Status ledger

| Claim | Audit status |
|---|---|
| Left-anchored run criterion | proved |
| Maximal factor realizes every feasible consecutive meet | proved |
| Every factor realizes every consecutive central join | proved |
| Single-switch mixed run lengths and meet depths | proved |
| Exact `d(d+1)` reservoir partition | proved under (3.4)--(3.5) |
| Maximal factor has at most `3d-1` reservoir values | proved |
| Maximal factor misses at least `(d-1)^2` lower masks | proved in the canonical single-switch setting |
| Central-preserving sparse repair preserves all upper joins | proved |
| Reservoir repair is localized to `O(kd^2)` pin tests | proved after fixing a reservoir assignment |
| A valid reservoir assignment always exists | unproved |
| Required central rows exist for every `k` | unproved |
| `nu(k)=B(k)` for all `k` | unresolved |

## 11. Audited artifacts

The source was frozen during this audit.  SHA-256 values are:

```text
fa6ee6c12bcb8c0967579ca9f4fa99a57c1877d1c66735e84ebe614e26e86608  SINGLE_SWITCH_MAXIMAL_SHADOW_THEOREM.md
255f90b2d84b85901d2817986daefdce6a0fe5b4a66852d9580bad13cb887993  SINGLE_SWITCH_PORTAL_INDEPENDENT_AUDIT.md
7d820348e42f2461809189027cd48d94c86a872e4c9115eee5d0bd9ee62fedb7  BANDED_DOUBLE_CHAIN_INDEPENDENT_AUDIT.md
b6636e15a4c5107c6314cec6ec1c26a535d83d10ed00247b2f75b784e44bc992  K11_PORTAL_EMBEDDING_MATH_NEXT.md
5ff3c98aebe3bc7fef43347c5a740e2bb80ac5f52c8f8d56c4a9e332fcc201b5  PORTAL_RIGIDITY_K11_NEXT.md
c9321894a25cffcde57ba499b433c96e1a00229705ea1c5f557fb5b53f6f4c9b  GLOBAL_PINNING.md
```

This audit made no changes to the source theorem or to
`MATHEMATICAL_HANDOFF.md`.
