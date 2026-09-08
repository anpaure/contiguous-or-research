# K17 SCD minimum-cut rank-ten Benders obstruction and functional-bank comparison

**Date:** 2026-08-01  
**Lane:** AD, SCD cut selection / functional upper service  
**Status:** exact theorem and proof-checked finite certificate.  The unchanged
minimum-residence-cut face is impossible even with arbitrary-width rank-ten
witnesses.  Two extra-split banks close the weaker upper-only singleton rows
but fail after lower-colour and common-orientation coupling.  No claim of a
K17 word, exact chronology, or compiler is made.

## 1. Objects and scope

The authenticated rank-nine SCD forest has

\[
 W={17\choose 9}=24310,
 \qquad C_9=4862
\]

path components.  A minimum depth-three residence fragmentation makes
exactly (1419) cuts and hence

\[
 P=C_9+1419=6281                                      \tag{1.1}
\]

pieces.  Every piece is an ordered Johnson path.  Its two orientations are
kept as distinct states.

For two oriented pieces (A,B), call the endpoint adjacency **ordinary**
when the last owner of (A) and first owner of (B) are distinct adjacent
rank-nine sets.  It has lower colour

\[
 L(A,B)=A_{\rm last}\cap B_{\rm first}
\]

and immediate upper colour

\[
 U(A,B)=A_{\rm last}\cup B_{\rm first}.                \tag{1.2}
\]

The exact two-block necessary residence predicate used below rejects every
locally closed positive run of length at most three.  If either block is
all-one in a coordinate, it leaves that coordinate to the later global age
automaton.  Thus every globally resident chronology passes this predicate,
but passing it is not sufficient for a chronology.

There are two different provider questions.

1. An **upper-only provider** is any necessary-resident Johnson seam with
   union (U).
2. A **joint lower/upper provider** additionally requires its intersection
   to be one of the current missing rank-eight colours.

The second is the relevant atomic q1 seam.  Confusing these two projections
is exactly what made the 18- and 192-split banks look closed prematurely.

## 2. Rank-ten witnesses collapse to an immediate seam

### Lemma 2.1 (rank-ten immediate-seam lemma)

Let (X_a,\ldots,X_b) be a contiguous interval in any literal chronology of
distinct adjacent rank-nine owners.  If

\[
                 \bigcup_{i=a}^{b}X_i=U,
                 \qquad |U|=10,                       \tag{2.1}
\]

then every adjacent pair in the interval satisfies

\[
                         X_i\cup X_{i+1}=U.             \tag{2.2}
\]

In particular, if the witness crosses a piece boundary, its first crossed
seam is an immediate provider of (U).

#### Proof

Every (X_i) is a nine-subset of (U).  Two consecutive owners are
distinct and Johnson adjacent, so their union has size ten.  It is contained
in (U), hence equals (U).  This proves (2.2), including at every crossed
piece boundary.  (square)

### Corollary 2.2

If a selected fragment bank has no context-extendable seam of union (U),
then no arbitrary-width crossing interval can witness (U) in any globally
depth-three-resident ordering of that bank.

This corollary is special to the immediate rank-ten row.  Higher-rank
targets may genuinely require several seams and must be handled by the
accumulated-union automaton.

## 3. All minimum cut patterns are impossible

The complete minimum-fragment atlas has the following exact census:

\[
\begin{array}{c|r}
\text{SCD components}&4862\\
\text{componentwise minimum cut patterns}&8894\\
\text{distinct possible segments}&12672\\
\text{oriented segment states}&25344\\
\text{context-extendable ordinary provider arcs}&554218\\
\text{possible cut upper colours}&4232.
\end{array}                                             \tag{3.1}
\]

For a pattern (p), an incident cut upper colour is called unsupported if
no context-extendable provider arc survives when the segments belonging to
the same component are restricted to the option of (p).  Other components
are deliberately left unrestricted.  Therefore this is an over-relaxation
of every global minimum-cut selection.

### Theorem 3.1 (minimum-cut-only rank-ten no-go)

Among the 8894 patterns, 505 contain an unsupported cut colour.  The
following fourteen components have no supported minimum pattern:

\[
 471,694,779,1000,1187,1209,1282,1574,1587,1630,2177,
 2276,3210,3293.                                      \tag{3.2}
\]

Consequently every choice of one minimum residence fragmentation per SCD
component leaves at least fourteen component-local rank-ten provider rows
unsupported.  No unchanged (6281)-piece minimum-cut bank can be made
rank-ten complete by ordering, orientation, or arbitrary-width crossing
witnesses.

#### Proof

For each component (C), impose only the at-least-one clause

\[
                     \bigvee_{p\in\mathcal P_C}x_p.     \tag{3.3}
\]

For each of the 505 provider-infeasible patterns impose the sound no-good

\[
                              \neg x_p.                 \tag{3.4}
\]

No exactly-one constraints, cross-component compatibility, lower palette,
topology, or higher-shadow constraints are used.  Each component in (3.2)
has all its variables forbidden by (3.4), contradicting (3.3).  Lemma 2.1
shows that allowing longer rank-ten intervals cannot restore any such row.
(square)

The emitted core has 8894 variables and

\[
                         4862+505=5367                 \tag{3.5}
\]

clauses.  It is even more transparent at component 471: pattern 956 is its
only option, so the core contains the complementary units (x_{956}) and
(-x_{956}) (DIMACS variable 957).  Kissat returns UNSAT with code 20;
`drat-trim` independently reports `VERIFIED`.  The checked hashes are
recorded in Section 8.

### Exact boundary

Theorem 3.1 proves that **alternative minimum cuts alone do not eliminate
all rank-ten zeros**.  It does not rule out a bank-changing socket, an extra
cut, a split-and-merge rethread, or a different SCD forest.

## 4. The canonical `P-8` count is accidental

For the canonical fragmentation,

\[
 (H_{10},\ldots,H_{15})=(1419,2454,1655,608,122,15),
 \qquad \sum H_r=6273=P-8.                              \tag{4.1}
\]

Thus (H_{10}=1419) and

\[
 H_{11}+\cdots+H_{15}=4854=4862-8.                      \tag{4.2}
\]

These equalities do not define eight boundary or cube liabilities.

* Changing only component 3189 from its cut pattern `[3]` to `[1]` changes
  the number of full-union pieces from eight to nine while the total upper
  hole count remains 6273.
* Changing component 3266 from `[4,8,13]` to `[2,5,11]` gives nine
  full-union pieces and total upper holes 6269, namely (P-12).
* Choosing the first minimum pattern in every component gives only 5818
  holes, namely (P-463); choosing the last reproduces (4.1).
* The eight canonical full-union pieces have IDs
  (0,55,260,2487,2507,3544,3856,4313), but the eight pre-cut rank-fourteen
  holes have complement triples of affine (mathbf F_2)-rank seven, not a
  three-cube.

The general cut identity is the one proved in the independent H3 note:

\[
 P=C_9+t,
 \qquad
 H=t+A(F)+B_F(D),                                      \tag{4.3}
\]

where (A(F)) is the pre-existing deep debt and (B_F(D)) is the
cut-dependent deep collateral.  Hence `6273=6281-8` is an exact census, not
a canonical seven-seam spare bank.

## 5. Exact functional comparison of the split banks

The upper-only split search gave two useful diagnostics:

* an alternative minimum bank with 19 upper-only rank-ten zeros, followed
  by 18 greedy internal splits, has zero upper-only zeros;
* the canonical bank followed by 192 greedy internal splits also has zero
  upper-only zeros.

Both were rebuilt literally.  The following table applies the stricter
joint lower-colour, same-orientation, and rank-ten projections.  `common`
is the number of pieces for which neither orientation has both an incoming
and outgoing necessary-resident joint seam.  `L0` is the number of missing
lower colours with no such seam.  `Mpp` is the tail-piece/head-piece matching
rank.  `U10=0` is the number of rank-ten targets with no joint provider, and
`MLU10` is the lower-colour/rank-ten matching rank.
For a linear (P)-piece braid only (P-1) lower colours are selected, so a
full (P)-matching is stronger by one.  Every deficit below is hundreds,
and this harmless strengthening does not affect any verdict.

\[
\begin{array}{l|r|r|r|r|r|r|r}
\text{bank}&P&\text{upper holes }10{:}15&L0&Mpp&\text{common}&U10=0&MLU10\\ \hline
\text{canonical}&6281&(1419,2454,1655,608,122,15)&1749&5747&3069&720&676\\
\text{alternative B19}&6281&(1419,2390,1592,566,109,9)&1666&5868&2848&605&743\\
\text{B19 plus 18 splits}&6299&(1437,2410,1603,573,109,9)&1650&5898&2783&581&779\\
\text{canonical plus 192 splits}&6473&(1611,2625,1751,645,134,17)&1577&6098&2558&406&1021.
\end{array}                                             \tag{5.1}
\]

For the 192-split bank, the 1611 rank-ten targets have target-to-arc matching
1205, exactly reflecting its 406 zero rows.  For the 18-split bank the
corresponding values are 1437, 856, and 581.

### Theorem 5.1 (outer-socket localization)

In all four SCD banks in (5.1), every failed common-orientation piece has a
physically dead endpoint inherited from the outer boundary of its supplied
6281-piece base segmentation.  Here `outer` does not mean an endpoint of an
original unsplit SCD component.  No failed refined piece has a dead newly
created split socket.

For the two refined banks the exact necessary-residence counts are

\[
\begin{array}{c|r|r|r}
\text{bank}&\text{failed pieces}&\text{dead outer sockets}&
\text{dead split sockets}\\ \hline
18\text{-split}&2783&3112&0\\
192\text{-split}&2558&2877&0.
\end{array}                                             \tag{5.2}
\]

#### Proof

Each refined piece was mapped back to its unique ordered interval in a base
piece.  A physical front socket is dead exactly when it has neither a
forward incoming nor a reverse outgoing seam; a physical back socket is
dead exactly when it has neither a forward outgoing nor a reverse incoming
seam.  Exhaustive literal enumeration gives (5.2), and every dead socket has
interval offset zero or the terminal base offset.  None lies at an internal
split offset.  (square)

Internal splits can still repair some old endpoints by exposing new mates;
this is why the counts improve down (5.1).  But residual failures remain an
outer-boundary problem.  Alternative minimum cuts or a true rethread can
move those boundaries; merely asserting upper-only support cannot.

## 6. Comparison with the protected dense bank

The original 7612-piece protected dense refinement has perfect relaxed
unoriented `TH`, `TC`, and `CH` q1 projections, but 187 common-orientation
failures and 78 rank-ten zero rows.  Its 187 dead sockets are likewise old
outer endpoints rather than new split sockets.

The subsequently authenticated protected bank (bank SHA prefix
`5b4fe2d1`) has:

* zero common-orientation singleton failures;
* zero relaxed rank-ten singleton rows;
* perfect q1 pairwise projections.

Therefore the protected bank is strictly stronger than every SCD bank in
(5.1) at the current functional-singleton layer.  This comparison is not
based on piece count.  It compares the same necessary two-block residence
predicate and asks for lower compatibility, common orientation, and
rank-ten service together.

The protected result still does not imply the simultaneous
tail/head/colour matching, connectivity, exact product residence, ranks
eleven and above, or a compiler.  The SCD route remains useful as an
independent recuttable construction and as the clean source of Theorem 3.1,
but it is not the leading fixed K17 bank after this comparison.

The SCD evaluator did compute the internal hole histograms at ranks eleven
through fifteen, but it did not compute their provider matchings.  No
higher-shadow comparison between the SCD and protected banks is claimed.

## 7. Correct joint cut/socket master

Let (x_p) choose a component fragmentation pattern, (y_a) choose an
ordinary oriented seam, and (z_g) choose a bank-changing socket or rethread
column.  For every cut rank-ten colour (U) of a selected pattern (p),
the sound Benders row is

\[
 -x_p
 \;\vee\!
 \bigvee_{a\in\mathcal A(p,U)} y_a
 \;\vee\!
 \bigvee_{g\in\mathcal G(p,U)} z_g,                    \tag{7.1}
\]

where (mathcal A(p,U)) contains only context-extendable ordinary seams
whose endpoint segments survive (p).  Every (g) must declare, and the
master must enforce, its exact

* affected cut option(s) and resulting subpieces;
* endpoint owners and orientations;
* newly deleted and restored lower colours;
* immediate and deep upper signed deck delta;
* residence input/output age transition;
* owner, guard, protected-pin, and compiler resources;
* topology edge or path-fragment signature.

The seam selection then needs one common orientation per piece, one incoming
and outgoing incidence with the linear boundary exception, exact missing-
lower use, all rank-ten ALOs, and subtour/path constraints.  Higher ranks are
lazy accumulated-union cuts, not scalar rows.

A pure extra split increases both the piece count and raw missing-lower count
by one.  Hence a repair that literally preserves (P=6281) must include a
compensating merge or be encoded as one zero-net rethread column.  Moreover,
Theorem 4.1 shows that recutting does not preserve the old 6273 upper bank;
every socket option must carry its signed upper ledger.  There is no sound
master in which a split is appended while the canonical (P)/upper rows are
kept frozen.

The exact unconditional lower bound is one genuinely bank-changing column:
zero such columns is ruled out by Theorem 3.1.  Fourteen is only the bound
for an architecture in which each socket repairs at most one of the fourteen
dead component rows; a nonlocal packet may repair several.  No exact minimum
socket count is proved here.

## 8. Reproducible artifacts

All heavy enumeration and proof checking ran on H100 CPU.  The main local
artifacts are:

```text
scratch/build_ad_k17_scd_allmin_rank10_benders_core_20260801.cpp
  b5a3d28a1d9555388a36c6d2d5ef7dc436bbb94476b2b58a0f2eeb5e1139d368

scratch/ad_k17_scd_allmin_rank10_benders_core_20260801/allmin_rank10_core.cnf
  2d92ff97b2b106e9b84ddd3c252100d3aba226ba33a40ffc4186dc15112f1c76
scratch/ad_k17_scd_allmin_rank10_benders_core_20260801/allmin_rank10_core.drat
  9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
scratch/ad_k17_scd_allmin_rank10_benders_core_20260801/core.dratcheck.out
  91ceec673a4bf26bf4715a98714708ca3fcc1b87d94b3dab009831b6d6396469

scratch/audit_ad_k17_scd_refined_functional_projections_20260801.cpp
  27e057be1a9d6bd8bdcb55b5de84d07e55c8d15c23ce4d8c62018564a910c470
scratch/ad_k17_scd_functional_compare_20260801/split18.audit.json
  821be13453eb3dc1070b390e9fd4e12d2968ea3492f6d17be0b3a898bc04b490
scratch/ad_k17_scd_functional_compare_20260801/split192.audit.json
  fe6a4685837a66d9cd36281cf83e8b4e68ec9d7761043c49c2b7a890eaf7c1ea
scratch/ad_k17_scd_functional_compare_20260801/split192_pieces.json
  ec163236a28b468105d6994d29b70d568d5f28a67eeaaa81a1ed1e7d8487e486
scratch/ad_k17_scd_functional_compare_20260801/MANIFEST.md
  7f3f8750a847fb46ffdb9788c3617495cc9108b60a2bfdc4e4ca2a0fccffcb6b

scratch/audit_ad_k17_scd6281_pminus8_noninvariance_20260801.py
  4a09926fdb2c5a2b05a663311bfbc8e243d2e8cc962fe0b4878d606dd109c234
scratch/ad_k17_scd6281_pminus8_noninvariance_20260801.audit.json
  e4589048f78acd5ef95914ac3b6ae0195da7d838c8928468907053f6d8613fb4
```

`core.status` records `kissat_rc=20` and `drat_trim_rc=0`.  The proof checker
finds the complementary unit at DIMACS variable 957 and reports `s VERIFIED`.

## 9. Precise remaining boundary

Proved:

1. the canonical 322 upper-only zero count is a fixed-bank obstruction;
2. every unchanged all-minimum-cut bank is impossible at rank ten;
3. the canonical `P-8` equality is not invariant;
4. the 18- and 192-split upper-only closures fail the stricter functional
   comparison, with exact counts in (5.1);
5. all their residual common-orientation failures are inherited outer
   sockets;
6. the protected zero/zero bank is the stronger present K17 singleton host.

Open:

* the exact three-resource q1 matching on the protected zero/zero bank;
* a zero-net bank-changing SCD socket/rethread master satisfying (7.1);
* global age chronology, connectivity, ranks eleven through seventeen, the
  generalized lower compiler, and literal universal-word extraction.
