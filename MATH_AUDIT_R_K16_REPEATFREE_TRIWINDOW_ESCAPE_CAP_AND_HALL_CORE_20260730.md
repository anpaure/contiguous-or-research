# Audit of the repeat-free K16 tri-window collar: exact escape caps and the Hall-core obstruction

Date: 2026-07-30  
Lane: R  
Status: proved parent-specific catalogue completeness and an exact host-selection criterion; no K16 equality construction and no unrestricted no-go claimed

## 1. Scope and verdict

This note audits the length-12,873 fibre

\[
 C^{(0)}\;A\;C^{(1)}\;B\;C^{(2)},
 \qquad (|C^{(0)}|,|C^{(1)}|,|C^{(2)}|)=(4,9,5),                 \tag{1.1}
\]

where, for authenticated length-6,438 K15 parents `X,Y`,

\[
 A=X[6:6436],\qquad B=\{z\}\vee Y[7:6432],\qquad z=2^{15}.     \tag{1.2}
\]

The eighteen collar cells are arbitrary nonempty 16-bit masks.  The two
repeat-free parents are exactly

```text
scratch/k15_repeatfree_parents_20260730/k15seed_1.word
  SHA 93484c945194c628b761f5b9a67111365d00fc1727d7e19839f07b74fee96d49
scratch/k15_repeatfree_parents_20260730/k15seed_5.word
  SHA 4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6
```

The other four authenticated files in that directory each have one middle
repeat and are not called repeat-free here.

The audit verdict is as follows.

1. The arbitrary-extension catalogue and host-intersection theorem in
   `MATH_THEOREM_R_K16_REPEATFREE_COLLAR_ARBITRARY_EXTENSION_AND_CORE_GATE_20260730.md`
   are valid.
2. `maxext=40` is not a consequence of repeat-freeness alone.  Nevertheless,
   for every ordered pair of the two displayed repeat-free parents, every
   useful one-window host has extension at most seven.  Intervals meeting two
   collar windows are redundant for the residual target set.  Therefore the
   existing `maxext=40` DIMACS/implicit catalogue is complete for all four of
   these ordered parent pairs; in fact `maxext=7` suffices.
3. A target-to-host Hall matching is necessary but not sufficient.  The exact
   invariant is the simultaneous intersection core of the selected hosts,
   including the nonzero-cell rows and every required-coordinate row.
4. The model is a literal **free-collar reuse** of two fixed parent bodies.
   It does not impose that the eighteen new cells reconstruct the twenty-one
   deleted parent cells, preserve a parent owner chronology, or arise by a
   legal factor trade.  None of that is needed if literal replay returns a
   universal K16 word, but it must not be advertised as a structural lift.

The single-boundary cyclic-gap no-go remains correctly scoped: it rules out
`A|z|(z+pi(B'))`, not the three-window fibre (1.1).

## 2. Six half-openings and the exact escape parameter

For a fixed body word `G`, let

\[
 \operatorname{Pref}_G(u)=\bigvee_{r=0}^{u-1}G_r,
 \qquad
 \operatorname{Suff}_G(u)=\bigvee_{r=|G|-u}^{|G|-1}G_r,                \tag{2.1}
\]

with value zero at `u=0`.  The six oriented half-openings of (1.1) are

\[
 0,\quad \operatorname{Pref}_A,\quad \operatorname{Suff}_A,
 \quad \operatorname{Pref}_B,\quad \operatorname{Suff}_B,\quad 0.   \tag{2.2}
\]

The two zero chains are the exterior sides of the first and last collar
windows.  These are the exact six openings; only four are nontrivial.

Let `Cov(G)` be the masks realized by nonempty intervals wholly inside `G`,
and define the residual family

\[
 \mathcal T(X,Y)=\bigl(2^{[16]}\setminus\{\varnothing\}\bigr)
       \setminus\bigl(\operatorname{Cov}(A)\cup\operatorname{Cov}(B)\bigr).
                                                                         \tag{2.3}
\]

For a half-opening chain `P` and target `T`, put

\[
 e_P(T)=\max\{u:P(u)\subseteq T\}.                                    \tag{2.4}
\]

This is exactly the number of adjacent fixed cells that a literal interval
with OR `T` can consume on that shore: the next fixed cell has a coordinate
outside `T`.  Define the escape bound

\[
 E_{\rm esc}(X,Y)=\max_{T\in\mathcal T(X,Y)}
 \max\{e_{\operatorname{Pref}_A}(T),e_{\operatorname{Suff}_A}(T),
       e_{\operatorname{Pref}_B}(T),e_{\operatorname{Suff}_B}(T)\}.     \tag{2.5}
\]

Let `E_cat(X,Y)` be the least integer `E` for which every canonical
one-window signature `(F,Q)` legal for at least one residual target has a
physical representative extending at most `E` fixed cells on each shore.
This definition first identifies OR-profile plateaux and other duplicate
`(F,Q)` signatures.

### Lemma 2.1 (one-window localization)

Suppose

\[
 \bigvee A=0x7fff,\qquad \bigvee B=0xffff.                              \tag{2.6}
\]

Every interval meeting both the first and middle collar windows has OR
`0x7fff` or `0xffff`; every interval meeting both the middle and last collar
windows has OR `0xffff`.  All these masks already lie in
`Cov(A) union Cov(B)`.  Hence every residual target has a witnessing interval
meeting exactly one collar window.

#### Proof

An interval meeting the first two windows contains all of `A`, so it already
contains every old coordinate.  It is `0x7fff` if none of its free cells uses
`z`, and `0xffff` otherwise.  An interval meeting the last two windows
contains all of `B`, hence is `0xffff`.  The whole fixed bodies themselves
are intervals, so the resulting saturated masks are in the fixed cover.
QED.

### Lemma 2.2 (escape-cap completeness)

Under Lemma 2.1, the catalogue which permits `E` fixed cells beyond either
side of each collar window contains every host usable by a residual target
whenever

\[
 E\ge E_{\rm esc}(X,Y).                                                 \tag{2.7}
\]

#### Proof

By Lemma 2.1 only one-window intervals matter.  Such an interval meets a
contiguous subinterval of its collar window.  It can extend into a left fixed
body only when that subinterval begins at the first collar cell, and then the
fixed cells form a body suffix.  The analogous right extension is a body
prefix.  If the interval realizes `T`, its fixed OR is contained in `T`, so
the two extension lengths are bounded by (2.4).  QED.

In general only

\[
 E_{\rm cat}(X,Y)\le E_{\rm esc}(X,Y)                                  \tag{2.8}
\]

is automatic: a long permissible extension can lie on an OR plateau or have
an equivalent shallower signature.  Exact canonical-catalogue equality is
equivalent to `E>=E_cat`, not necessarily to `E>=E_esc`.  For the four
audited pairs below, direct full-profile comparison proves that these two
parameters are equal.

The lemma is source-independent.  It also shows why the fact that a monotone
OR profile has at most seventeen distinct values does **not** imply a
seventeen- or forty-cell extension bound: an OR profile may have arbitrarily
long plateaux.

## 3. Exact cap audit for the repeat-free pair family

For each ordered pair `(i,j)` in `{1,5}^2`, the fixed cover was accumulated
by starting at every body position and extending the OR until saturation.
For every residual target, each of the four chains in (2.2) was scanned until
its first forbidden coordinate.  This is deterministic finite arithmetic,
not a SAT or search result.

The residual counts, rank histograms and global caps are

| `(X,Y)` | `|T|` | residual rank histogram | `E_esc=E_cat` |
|---|---:|---|---:|
| `(1,1)` | 73 | `1:1,5:6,6:10,7:13,8:21,9:14,10:4,11:2,12:2` | 5 |
| `(1,5)` | 70 | `1:1,5:7,6:6,7:12,8:21,9:14,10:4,11:2,12:3` | 6 |
| `(5,1)` | 73 | `1:1,5:4,6:11,7:13,8:21,9:15,10:3,11:3,12:2` | 5 |
| `(5,5)` | 70 | `1:1,5:5,6:7,7:12,8:21,9:15,10:3,11:3,12:3` | 7 |

Here is the full nontrivial-shore certificate.  `U_e` is the cumulative OR
at the displayed maximum, `U_(e+1)` is the next cumulative OR, and the final
column records the residual targets containing `U_(e+1)`.  Thus every upper
bound is certified by a zero in the last column, while the listed target(s)
certify attainment.

| pair | shore | `e` | maximizing residual targets | `U_e` | `U_(e+1)` | contain next |
|---|---|---:|---|---|---|---:|
| 1,1 | A head | 4 | `0x356d,0xb54d,0xb56d` | `0x354d` | `0x35cd` | 0 |
| 1,1 | A tail | 5 | `0x77bc,0xe73c,0xf7bc` | `0x673c` | `0x673d` | 0 |
| 1,1 | B head | 3 | `0xb54d,0xb56d` | `0xb50d` | `0xb58d` | 0 |
| 1,1 | B tail | 4 | `0xe673,0xe77b` | `0xc673` | `0xce73` | 0 |
| 1,5 | A head | 4 | `0x356d` | `0x354d` | `0x35cd` | 0 |
| 1,5 | A tail | 5 | `0x77bc` | `0x673c` | `0x673d` | 0 |
| 1,5 | B head | 6 | `0xf3bd` | `0xf3b9` | `0xf7b9` | 0 |
| 1,5 | B tail | 4 | `0xab6b` | `0xaa6b` | `0xae6b` | 0 |
| 5,1 | A head | 5 | `0xf7bc` | `0x739c` | `0x739d` | 0 |
| 5,1 | A tail | 5 | `0x3bde` | `0x1b5e` | `0x1b7e` | 0 |
| 5,1 | B head | 3 | `0xb54d,0xb56d` | `0xb50d` | `0xb58d` | 0 |
| 5,1 | B tail | 4 | `0xe673,0xe77b` | `0xc673` | `0xce73` | 0 |
| 5,5 | A head | 7 | `0xf3bd` | `0x73bd` | `0x77bd` | 0 |
| 5,5 | A tail | 5 | `0x3bde,0xbbde` | `0x1b5e` | `0x1b7e` | 0 |
| 5,5 | B head | 6 | `0xf3bd` | `0xf3b9` | `0xf7b9` | 0 |
| 5,5 | B tail | 4 | `0xab6b` | `0xaa6b` | `0xae6b` | 0 |

Both retained `A` bodies have total OR `0x7fff`, and both marked `B` bodies
have total OR `0xffff`.  Lemmas 2.1--2.2 therefore prove:

The direct distinct-profile comparison is

| pair | full useful signatures | useful at `E-1` | omitted at `E-1` | useful at `E` |
|---|---:|---:|---:|---:|
| 1,1 | 188 | 177 | 11 | 188 |
| 1,5 | 212 | 203 | 9 | 212 |
| 5,1 | 182 | 169 | 13 | 182 |
| 5,5 | 227 | 223 | 4 | 227 |

Thus the displayed values are the exact minimum `maxext` values for equality
of the target-useful canonical signature catalogues, not merely sufficient
escape bounds.

> **Corollary 3.1.** For all four ordered pairs of authenticated repeat-free
> parents, the physical residual-target catalogue equals its `maxext=7`
> catalogue after target-useless signatures are discarded.  In particular,
> the current `maxext=40` catalogue is complete for these four pairs.

For the live self-pair `(5,5)`, the saved map independently records 70
residual targets, 395 canonical truncated signatures, and 6,081 target-host
witness variables.  Exactly 227 of those signatures occur in at least one
legal host row.  The excess signatures are harmless target-useless profile
values.

This corollary must not be generalized to another parent merely from
repeat-freeness.  That parent needs its own fixed-cover, saturation and escape
audit, or the complete arbitrary-extension catalogue.

## 4. Exact host-selection theorem

Let `Q={1,...,18}` index the free cells.  A canonical host signature is a
pair

\[
 h=(F_h,Q_h),\qquad \varnothing\ne Q_h\subseteq Q,                      \tag{4.1}
\]

where `Q_h` is the consecutive set of free cells met by a literal interval
and `F_h` is the OR of its fixed cells.  It is legal for a residual target
`T` when `F_h subseteq T`.

Choose one legal host `h(T)` for every residual target.  For a collar cell
`q`, define

\[
 K_q=\bigcap_{T:q\in Q_{h(T)}}T,                                       \tag{4.2}
\]

with an empty intersection interpreted as the full 16-coordinate mask.

### Theorem 4.1 (necessary and sufficient core criterion)

The chosen host system is realizable by nonempty collar cells if and only if

\[
 K_q\ne\varnothing\quad\hbox{for every used cell }q,                   \tag{4.3}
\]

and, for every residual target `T` and every coordinate
`b in T minus F_(h(T))`,

\[
 \text{some }q\in Q_{h(T)}\text{ has }b\in K_q.                        \tag{4.4}
\]

Unused cells may be assigned any nonempty mask.  Equivalently, because the
empty-intersection convention makes their core the full mask, one may impose
`K_q nonempty` on all eighteen cells.  When (4.3)--(4.4) hold, the maximal
canonical assignment

\[
 C_q=K_q                                                               \tag{4.5}
\]

for used cells, with arbitrary nonempty values at unused cells, realizes all
chosen hosts simultaneously.

#### Proof

In any realizing assignment, a cell used by target `T` is a nonempty subset
of `T`.  Hence `C_q subseteq K_q` and (4.3) is necessary.  Every coordinate
of `T` not already in the fixed mask must occur in some used collar cell;
that cell is contained in `K_q`, proving (4.4).

Conversely, assign (4.5).  Every `K_q` in the selected host of `T` is a
subset of `T`, so the resulting interval OR is contained in `T`.  Its fixed
mask supplies `F_h`, and (4.4) supplies every remaining coordinate, so its OR
is exactly `T`.  Nonemptiness follows from (4.3).  Unused cells lie in no
selected host and therefore cannot spoil these equalities.  QED.

For a fixed bit `b`, let `D_b` be the union of the selected host intervals of
targets omitting `b`.  Then (4.4) says exactly

\[
 Q_{h(T)}\not\subseteq D_b
 \quad\text{for every }b\in T\setminus F_{h(T)}.                       \tag{4.6}
\]

Thus the corrected invariant is a sixteen-colour guarded interval
transversal, not a scalar-capacity flow.

Every failure has a bounded certificate.  A zero core needs at most sixteen
selected rows, one omitting each coordinate.  A failed demand `(T,b)` needs
the root row plus at most one blocking row per collar cell, hence at most
nineteen rows.  The exact problem is consequently a one-host-per-target
independent-transversal problem with forbidden hyperedges of rank at most
nineteen.

In the saturated `4/9/5` fibre, every residual host is contained in one
window.  A failed demand therefore needs the root plus at most nine blockers,
so its rank is at most ten.  Together with the zero-core bound, the complete
forbidden-option hypergraph has rank at most sixteen.

## 5. Hall and pairwise compatibility are not exact

For a fixed assignment, one host signature has one OR value.  Distinct
targets therefore require distinct selected signatures, so Hall's condition
on the target/signature incidence graph is necessary.  It is not sufficient.

### Proposition 5.1 (minimal local Hall obstruction)

Use three coordinates `a,b,c`, one nonempty free cell `x`, and one adjacent
fixed cell `{b}`.  The two residual targets

\[
 T_1=\{a\},\qquad T_2=\{b,c\}                                         \tag{5.1}
\]

have the two distinct hosts

\[
 h_1=[x],\quad F_{h_1}=\varnothing;
 \qquad h_2=[x,\{b\}],\quad F_{h_2}=\{b\}.                             \tag{5.2}
\]

The target/signature graph has a perfect matching.  But `h_1` forces
`x={a}`, while `h_2` forces `c in x subseteq {b,c}`.  No common nonempty
cell exists.  Both targets are residual because the fixed body alone covers
only `{b}`.

One free cell and two targets are the minimum possible sizes of a failure of
Hall sufficiency; three ground coordinates are also minimal for this
one-fixed-shore residual construction.  With only two coordinates, a target
strictly extending the fixed singleton can require only the other coordinate,
which is compatible with the singleton target on the free cell.

Pairwise host compatibility also does not suffice in general: total target
intersections can be empty despite all pair intersections being nonempty.
Theorem 4.1 retains precisely the missing all-row intersection information.

## 6. Audit of the DIMACS, implicit model and decoder

The DIMACS builder correctly enforces, for each selected witness `(T,h)`,

1. every used free cell omits every coordinate outside `T`;
2. each coordinate in `T minus F_h` occurs in at least one used free cell;
3. every free cell is nonempty; and
4. every residual target selects at least one witness.

Shared cell-bit variables preserve overlapping-window/overlapping-interval
consistency.  Canonicalizing physical intervals by `(F_h,Q_h)` is exact,
because two intervals with that same pair have the same OR under every collar
assignment.  The implicit search uses the same shared-cell semantics.

The following scope distinctions are essential.

* A score-zero implicit state or SAT assignment followed by literal replay is
  a sound positive certificate even if `maxext` were incomplete.
* UNSAT of a truncated catalogue is an arbitrary-extension no-go only after
  a completeness proof such as Corollary 3.1.
* A `STATIC_DEAD` target is a full physical obstruction only after the same
  completeness proof.  The builder records dead targets rather than emitting
  an empty clause.
* The decoder checks every nonempty mask by literal replay.  Therefore a
  `VERIFIED_UNIVERSAL` output is sound.  For stronger provenance hygiene it
  should additionally reject parent-hash drift, conflicting duplicate solver
  literals and mapping-payload drift; literal replay already prevents any of
  these bookkeeping issues from creating a false universal word.

Most importantly, the only source constraint in this fibre is cell
nonemptiness.  This is exactly sufficient for a literal contiguous-OR word.
It is not a certificate that the free cells constitute legal parent-opening
replacements, preserve middle ownership, or arise from a parent factor trade.

## 7. Exact implication boundary

Proved:

1. all six half-openings are explicitly represented;
2. for the four ordered repeat-free parent pairs, `maxext=7` is complete and
   body-spanning hosts are residual-redundant;
3. Theorem 4.1 is an exact constructive iff for arbitrary nonempty collar
   cells;
4. ordinary target/signature Hall and pairwise compatibility are insufficient;
5. every obstruction to a fixed host selection has rank at most nineteen in
   general and at most sixteen in the saturated `4/9/5` fibre.

Not proved:

1. existence of a host selection satisfying Theorem 4.1 for any parent pair;
2. infeasibility of the complete host-selection system;
3. a WLOG reduction of every K16 equality word to this three-window fibre;
4. preservation of parent ownership, shadows, residence or factor structure;
5. a source-independent constant extension cap for arbitrary repeat-free
   parents.

The exact bracket remains

\[
 12873\le \nu(16)\le12874.
\]

## 8. Audited sources

```text
MATH_THEOREM_K16_REPEATFREE_CYCLIC_GAP_RELATIVE_PERM_NOGO_20260730.md
  SHA 4d56643413f020575c07697faee05bef8c76763b6dbbcf2751fcbbec96ed76d2
MATH_THEOREM_R_K16_REPEATFREE_COLLAR_ARBITRARY_EXTENSION_AND_CORE_GATE_20260730.md
  SHA d9f0df5c8bab43c48cfe6440bd229a5c7521aae075b30196e2605117663a87b2
scratch/build_k16_triwindow_dimacs_20260730.py
  SHA a14198849c66d6612262742b9ac83f5a7992ac6fcf506fc5667f61d7756fcf9e
scratch/search_k16_triwindow_implicit_csp_20260730.cpp
  SHA 86af19e948a1d86c6683c02783df0b5091c63981752b6cfb78d91e6b78740f83
scratch/decode_k16_triwindow_dimacs_20260730.py
  SHA e46bbc4c0efc458e26ce0f01c2a1e044ea7db746e095acc9329391a37afc69ae
scratch/k16_triwindow_rf495_lead_20260730/model/model.map.json
  SHA af3818bcc249b84cb3f99e8fd0b90aca7c4031e57bd2013570514beb4377a6b0
scratch/k16_triwindow_rf495_lead_20260730/model/model.stats.json
  SHA 62561f184eafe8d97ee8e8e9c9048d69ce2cf5841be0c91eafe1f03477149664
scratch/audit_k16_repeatfree_triwindow_escape_caps_20260730.py
  SHA b0da94dc40bfe465becd2e7593c09c63beeb26b192692e5f52efcf053cae9718
scratch/k16_repeatfree_triwindow_escape_caps_20260730.audit.json
  SHA 04481ed445e2dea2108b2907e31047a7b1a7e08067904573ee0cd599f95e67cf
  payload 489fa1feefddb0d21d76d03b7d7782ed6561a5932b6a8a1f808f9e54fa14d513
```
