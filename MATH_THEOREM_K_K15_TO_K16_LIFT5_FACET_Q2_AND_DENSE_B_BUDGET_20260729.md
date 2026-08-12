# `k=15 -> 16`: exact `lift5` facet audit, full lower-q2 ledger, and the corrected dense-`B` budget

Date: 2026-07-29  
Lane: K  
Status: unconditional four-block no-go; exhaustive q1/q2 and full physical
audit of the finite endpoint atlas; exact dense-seam accounting.  No `k=16`
word is claimed.

## 0. Verdict

The hardcoded construction in

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/lift5.py
SHA-256 e7163c172413abefe93d830ddfb58bf5f038d2b7f03c61a1e21ebc020d2bfcba
```

does not use the pointwise-complement rail from the preceding Lane-K theorem.
It uses the Pascal facet rail

\[
 A_i=T_i,
 \qquad
 B_i=\{z\}\cup X_i,
 \qquad
 X_i=T_i\cap T_{i+1}.                              \tag{0.1}
\]

That distinction is decisive.

1. For the audited `6390+45` source, facet erosion turns the `1425` source
   one-runs of length four into `1425` forbidden `B`-runs of length three.
   All lie on the large component.  One opening of the large `B_0` block can
   meet at most three of their closed collars.  Therefore every literal

   \[
   [A_0(a),A_1(b),B_1(b-1),B_0(c)]                \tag{0.2}
   \]

   has at least

   \[
   \boxed{1422}
   \]

   internal residence violations.  This is an exhaustive theorem for every
   `(a,b,c)`, not a failed heuristic search.

2. The missing lower-q2 audit can be written exactly.  An exhaustive
   endpoint enumeration gives `240` AA restoration pairs, `240` forced
   top-upper BB pairs, and `1290` compatible triples.  Exactly `90` pass both
   q1 palettes and both lower-q2 sectors.  Every one of those `90` is then
   materialized and audited literally: all have `12870` distinct rank-eight
   owners, every transition is Johnson, every lower fixed shadow through
   depth seven is complete, and lower q2 has zero holes in both the no-top
   and top sectors.

3. The best shadow profile among those `90` has exactly one missing upper-q3
   target, equivalently one missing arbitrary upper target, and `1426`
   residence defects.  A canonical representative is

   \[
   (a,b,c)=(306,43,1005),
   \qquad\text{missing target }20215.              \tag{0.3}
   \]

   The residence-first Pareto point has `1425` short runs but one upper-q2
   and one upper-q3 hole.  Thus there is no finalist.

4. The often-quoted window `82<=h<=94` combines data from a different rail
   and is valid only in the cross-only specialization.  The value `82` is
   the complement-rail collar transversal.  For the facet rail in (0.1), the
   bare quotient transversals are `60` with every collar edge allowed and
   `79` with only the two boundary edges allowed.

5. More importantly, q1 capacity constrains the **net number of B
   superblocks**, not the gross number of old BB cuts.  If `b` old BB edges
   are deleted and `r` new BB joins are inserted, put

   \[
   g=b-r.                                           \tag{0.4}
   \]

   Then the final quotient contains `429-g` BB edges and hard q1 capacity is
   exactly `g<=94`.  Hence `82<=h<=94` is a genuine twelve-slot window only
   when `r=0` and `h=b=g`, precisely the cross-only complement architecture
   already excluded by the theorem forcing at least sixteen
   cut-set-dependent BB colour restorations.

   This twelve-slot figure is itself pre-topological: its `82` cuts all lie
   on the 426-cycle.  A spanning path must also cut the defect-free
   three-cycle, reducing the cross-only large-cycle window to `82..93`.

   The exact quotient-load-one colour minimum at large-component cut sizes
   `82,83,84,85` is
   respectively `19,18,17,16`.  Thus even the sixteen-restoration ledger is
   only an optimistic relaxation, attainable in this necessary statistic no
   earlier than gross cut size `85` and not sufficient there.

There are two distinct dense continuations: the pointwise-complement
same-rail `BB` rethread governed by the `82`-collar ledger, and a many-block
facet rethread governed by the separate `60/79` collar data.  Both require
exact colour restoration and q2 witness flow.  Neither is the literal
four-block lift, and neither is governed by a twelve-slot gross-cut bound.

## 1. The exact `lift5` construction

Let the two parent components be

\[
 T^0=(T^0_i)_{i\in\mathbb Z/6390},
 \qquad
 T^1=(T^1_i)_{i\in\mathbb Z/45}.                  \tag{1.1}
\]

Put

\[
 X^j_i=T^j_i\cap T^j_{i+1}.                       \tag{1.2}
\]

The source is lower-q1 exact, so the `X^j_i` are all rank-seven subsets of
`[15]`, once each.  Consequently the `A` states in (0.1) are exactly all
rank-eight child states omitting `z`, while the `B` states are exactly all
rank-eight child states containing `z`.

For a cyclic word `C`, write `C(s)` for the opening beginning at `s`.
The literal path is

\[
 T^0(a)\ | T^1(b)\ |
 (z+X^1)(b-1)\ | (z+X^0)(c).                    \tag{1.3}
\]

The word “descent” in `lift5.py` denotes the seam

\[
 T^1_{b-1}\longrightarrow z+X^1_{b-1};           \tag{1.4}
\]

it is not an additional block or owner.

The three nonnative seams are

\[
 T^0_{a-1}\longrightarrow T^1_b,                 \tag{1.5}
\]

\[
 T^1_{b-1}\longrightarrow z+X^1_{b-1},           \tag{1.6}
\]

\[
 z+X^1_{b-2}\longrightarrow z+X^0_c.             \tag{1.7}
\]

The descent (1.6) is always Johnson.  The other two seams must satisfy

\[
 |T^0_{a-1}\cap T^1_b|=7,
 \qquad
 |X^1_{b-2}\cap X^0_c|=6.                        \tag{1.8}
\]

The original `lift5.py` never checks the second rank condition in its final
verifier.  It can therefore accept a non-Johnson `B_1|B_0` jump when neither
lost q1 colour happens to be critical.  The new audit checks all `12869`
transitions literally.

## 2. Facet tower identities and the chronology loss

For every `q>=0`, De Morgan is not involved; direct associativity gives

\[
 \bigcap_{h=0}^{q} B_{i+h}
 =\{z\}\cup\bigcap_{h=0}^{q+1}T_{i+h}.            \tag{2.1}
\]

For `q>=1`, source residence gives

\[
 \bigcup_{h=0}^{q} B_{i+h}
 =\{z\}\cup\bigcup_{h=1}^{q}T_{i+h}.             \tag{2.2}
\]

Thus the cyclic facet rail transports the lower tower down by one parent
depth and the upper tower up by one parent depth.  In particular,

\[
 X_i\cup X_{i+1}=T_{i+1}.                         \tag{2.3}
\]

The usual nonempty source shadow theorem transfers the child `B` lower tower
through depth six.  At child depth seven, the singleton `{z}` asks for an
empty nine-state source intersection and remains a compiler/boundary check;
this caveat is irrelevant to the requested q2 theorem.

On coordinate traces, however, (1.2) is one-step erosion.  A cyclic source
one-run of length `ell` becomes a facet one-run of length `ell-1`.  This is
harmless for `13->14`, because `d(14)=2` and the child threshold is three.
It is fatal for `15->16`, because `d(16)=3` and the threshold is four.

### Theorem 2.1 (uniform four-block residence no-go)

Every literal path (1.3) has at least `1422` internal positive runs of length
below four.

### Proof

The large source component has exactly

\[
 4^{1425}5^{1110}6^{780}7^{540}8^{495}\cdots
\]

one-runs, while the small component has minimum one-run seven.  Erosion
therefore creates exactly `1425` length-three facet runs on the large
component and none on the small component.

For each length-three run mark its closed four-edge collar.  Direct
certificate enumeration gives the number of marked collars incident with a
large-component edge:

\[
 0^{2220}1^{2760}2^{1290}3^{120}.                 \tag{2.4}
\]

The path (1.3) opens the large `B_0` component at only one old edge, `c`.
Every collar not containing that edge remains a literal internal subpath
`0,1,1,1,0`, independent of all three new seams.  By (2.4), at most three
collars meet `c`; at least `1425-3=1422` survive.  `square`

This theorem is stronger than any collar-table rejection and makes a broad
`(a,b,c)` search unnecessary.

## 3. Exact q1 ledger

Define, cyclically within each component,

\[
 Y^j_i=X^j_i\cap X^j_{i+1}
       =T^j_i\cap T^j_{i+1}\cap T^j_{i+2},        \tag{3.1}
\]

\[
 U^j_i=T^j_i\cup T^j_{i+1}.                       \tag{3.2}
\]

The no-top lower-q1 deck is exact.  Opening `A_0` loses `X^0_{a-1}`;
opening `A_1` loses `X^1_{b-1}`.  The descent restores the second colour
exactly, so completeness is equivalent to

\[
 T^0_{a-1}\cap T^1_b=X^0_{a-1}.                  \tag{3.3}
\]

For top-containing lower q1, the exact signed load is

\[
 \mu'_6
 =\mu_6-[Y^1_{b-2}]-[Y^0_{c-1}]
       +[X^1_{b-2}\cap X^0_c].                   \tag{3.4}
\]

Every rank-six value must have positive final load.  The source load
histogram is

\[
 1^{3630}2^{1320}3^{55}                           \tag{3.5}
\]

physically, or

\[
 1^{244}2^{88}3^3                                 \tag{3.6}
\]

on rotation orbits.

For no-top upper q1, the exact signed load is

\[
 \nu'_9
 =\nu_9-[U^0_{a-1}]-[U^1_{b-1}]
       +[T^0_{a-1}\cup T^1_b].                   \tag{3.7}
\]

For top-containing upper q1, the descent restores the small-component cut.
The large cut is restored if and only if

\[
 X^1_{b-2}\cup X^0_c=T^0_c.                      \tag{3.8}
\]

Equation (3.8) also forces the `B_1|B_0` seam to be Johnson.

## 4. The missing full lower-q2 audit

There are

\[
 \binom{16}{6}=8008
\]

child lower-q2 targets: `5005` omit `z` and `3003` contain `z`.

Put

\[
 Z^j_i=X^j_i\cap X^j_{i+1}\cap X^j_{i+2}
       =\bigcap_{t=0}^3T^j_{i+t}.                 \tag{4.1}
\]

### Theorem 4.1 (exact four-block q2 loss/gain equations)

The no-top q2 multiset is the complete source `Y` multiset with signed
change

\[
\begin{aligned}
 -[Y^0_{a-2}]-[Y^0_{a-1}]
 &+[T^0_{a-2}\cap T^0_{a-1}\cap T^1_b]\\
 &+[T^0_{a-1}\cap T^1_b\cap T^1_{b+1}].          \tag{4.2}
\end{aligned}
\]

The two `A_1` triple windows destroyed at the cut are recreated identically
by the two descent-crossing triples:

\[
 T^1_{b-2}\cap T^1_{b-1}\cap(z+X^1_{b-1})=Y^1_{b-2}, \tag{4.3}
\]

\[
 T^1_{b-1}\cap(z+X^1_{b-1})\cap(z+X^1_b)=Y^1_{b-1}. \tag{4.4}
\]

After deleting `z`, the top-containing q2 multiset is the complete source
`Z` multiset with signed change

\[
\begin{aligned}
 &-[Z^1_{b-3}]-[Z^1_{b-2}]
  -[Z^0_{c-2}]-[Z^0_{c-1}]\\
 &+[X^1_{b-3}\cap X^1_{b-2}\cap X^0_c]\\
 &+[X^1_{b-2}\cap X^0_c\cap X^0_{c+1}].         \tag{4.5}
\end{aligned}
\]

The path covers all lower q2 targets if and only if every rank-six target has
positive load after (4.2) and every rank-five target has positive load after
(4.5).  A new intersection of smaller rank is simply irrelevant; it need not
be rejected when all lost rank-five targets retain other witnesses.

### Proof

A three-state window is destroyed exactly when one of its two old edges is
cut.  Each cut destroys the two cyclic triples straddling it.  The only new
three-state windows are the two crossing each new seam.  Listing those
windows in (1.3) gives (4.2)--(4.5).  Equations (4.3)--(4.4) cancel the two
small `A` losses.  Any triple containing an `A` state omits `z`; a
top-containing q2 witness must be an all-`B` triple.  Thus the two sectors are
disjoint and the load conditions are necessary and sufficient.  `square`

This is the check missing from `lift5.py`.

## 5. Exhaustive finite endpoint audit

The exact endpoint equations give:

```text
AA restoration pairs                         240
forced top-upper/Johnson BB pairs             240
joined (a,b,c) triples                       1290
triples passing both q1 and both lower q2       90
```

All `90` survivors are materialized.  No collar table or precomputed witness
claim is trusted.  The audit checks:

1. exactly `12870` distinct rank-eight middle owners;
2. all `12869` transitions Johnson;
3. every internal coordinate run in the final linear path;
4. every lower and upper fixed window at depths `1..7`;
5. arbitrary upper interval coverage.

The six exact profiles, each with multiplicity `15`, are:

| short runs | lower holes `q1..q7` | upper holes | arbitrary upper holes |
|---:|:---:|:---|---:|
| `1425` | all zero | `q2=1,q3=1` | `2` |
| `1425` | all zero | `q2=1,q3=1` | `2` |
| `1426` | all zero | `q3=1` | `1` |
| `1426` | all zero | `q3=1` | `1` |
| `1427` | all zero | `q3=2` | `2` |
| `1427` | all zero | `q3=2` | `2` |

The duplicate rows have different short-run length histograms.  The
representative (0.3) has

\[
 2^1 3^{1425}
\]

short runs.  Therefore its exact gate vector is

\[
\boxed{
\begin{array}{c|c}
\text{middle ownership}&0\text{ defects}\\
\text{Johnson transitions}&0\text{ defects}\\
\text{lower fixed }q1..q7&0\text{ holes}\\
\text{upper fixed }q1,q2,q4..q7&0\text{ holes}\\
\text{upper fixed }q3&1\text{ hole}\\
\text{arbitrary upper}&1\text{ hole}\\
\text{residence}&1426\text{ bad runs.}
\end{array}}
\tag{5.1}
\]

The full lower-q2 audit is positive; chronology is the overwhelming failure.

## 6. Why the facet lift evades the old 16-orbit obstruction

The preceding 16-orbit theorem concerned

\[
 z+([15]\setminus T_i).                            \tag{6.1}
\]

The facet rail (0.1) is nonlocal relative to (6.1): the two BB factors share
only `24/429` quotient edge orbits, or `360/6435` physical edges.  The facet
factor replaces the other `405` edge orbits.

Its BB lower colours are the source lower-q2 values `z+Y_i`; by (3.5) every
top q1 target is present.  Thus no cut-set-dependent unique colour from the
complement theorem is globally absent from the facet bank.  The sixteen
colours are not a fixed universal list: every complement collar transversal
cuts at least sixteen globally unique colours, but their identities depend
on the cut set.  For the explicit sixteen-residue optimum certificate frozen
in the complement audit, the corresponding facet loads are thirteen of load
one and three of load two, with no occurrence on the small 45-state block.
For that certificate, exactly thirteen of the 426 large-block cuts destroy
one of its listed colours without another facet witness.

Thus the facet construction genuinely escapes the **colour** obstruction.
It fails first at the separate erosion chronology theorem, not at q1 supply.

## 7. Correct dense-`B` cut/join accounting

Work on the `Z_15` quotient, with `429` vertices on each rail.  Let

- `b_A,b_B` be the numbers of old AA and BB edges deleted;
- `r_A,r_B` be the numbers of new same-rail AA and BB joins;
- `c` be the number of cross edges in a cyclic reassembly.

Degree sums force

\[
 2b_A=2r_A+c,
 \qquad
 2b_B=2r_B+c.                                     \tag{7.1}
\]

Hence

\[
 g:=b_A-r_A=b_B-r_B={c\over2},                    \tag{7.2}
\]

and

\[
 \#AA=\#BB=429-g,
 \qquad
 \#AB=2g.                                         \tag{7.3}
\]

Here `g` is the net number of A-runs and B-runs, not the gross number of
old edges changed.  For an A-to-B Hamilton path, `#AB=2g-1`; the same-rail
counts remain `429-g`.

The hard q1 palettes contain `335` target orbits, so

\[
 \boxed{g\le94.}                                  \tag{7.4}
\]

This is the correct meaning of the even-q1 capacity theorem.

### 7.1 The conditional twelve-slot window

Let `b_L` and `b_S` be the numbers of old BB cuts on the quotient components
of lengths `426` and `3`, respectively, so `b_B=b_L+b_S`.  For the
pointwise-complement rail, the exact collar theorem gives

\[
 b_L\ge82.                                        \tag{7.5}
\]

If one first ignores the defect-free small component and permits no new BB
seam, then `r_B=b_S=0` and `g=b_L`.  Equations (7.4)--(7.5) give the raw
collar-versus-capacity relaxation

\[
 \boxed{82\le g\le94},                            \tag{7.6}
\]

with twelve gross slots.  At `g=82+s`, `0<=s<=12`, its formal cyclic edge
ledger is

\[
 \#BB=\#AA=347-s,
 \qquad
 \#AB=164+2s.                                     \tag{7.7}
\]

Its hard q1 spare is `12-s`.  If every rail run has at least four states,
the top q2 occurrence count is

\[
 429-2g=265-2s,                                   \tag{7.8}
\]

giving scalar spare `64-2s` over the `201` top-q2 target orbits.

This is not yet a spanning chronology: the three-cycle is untouched.  Any
spanning path must have `b_S>=1`; with `r_B=0`, the actual net count is at
least `g=b_L+1`, so (7.4) sharpens the large-component window to
`82<=b_L<=93`.  The raw twelve-slot reserve has an unavoidable one-slot
topology tax.

More decisively, `r_B=0` has no mechanism to restore the at least sixteen
cut-set-dependent globally unique complement colours; cross seams are
z-free.  The entire cross-only twelve-slot window is therefore impossible.

### 7.2 The optimistic minimal-restoration ledger

For the total quotient cut set `C_B`, define

\[
 L(C_B)=\#\{R:\hbox{ every old BB witness of colour }R
                    \hbox{ belongs to }C_B\}.                  \tag{7.9}
\]

Every valid reassembly needs

\[
 r_B\ge L(C_B).                                                \tag{7.10}
\]

The unique-colour theorem gives `L(C_B)>=16`; it does not give equality.
There is a sharper exact cardinality interaction.  Let `u_b` be the minimum
number of edges whose q1 colour orbit has quotient load one among
large-component quotient collar transversals of exact size `b`.  A
width-three cyclic transfer DP gives

\[
 u_{82}=19,
 \qquad u_{83}=18,
 \qquad u_{84}=17,
 \qquad u_b=16\quad(85\le b\le110).              \tag{7.11}
\]

Indeed, fix the first three cut bits, scan positions `3..425` with state
`(last three bits,number selected)`, and reject a transition whenever a
collar ending at that position is all zero.  At the end test the wrapping
collars.  All collars have length at most four, so this state is complete.
The frozen audit records attaining edge sets for `b=82,83,84,85` as well as
the matching lower bounds.

Consequently the following `r_B=16` table is an **optimistic scalar
relaxation**, not a proved schedule.  It is impossible for
`b_L=82,83,84` by (7.11), and for `b_L>=85` it is conditional on finding a
cut set with exactly sixteen total lost colours and sixteen legal
colour-restoring joins.  Nonunique colours whose last witnesses are all cut
can make `L(C_B)>u_b`.  The three small-cycle edge-colour loads are
`1,3,1`; the table chooses its load-three edge and additionally assumes its
two large-component witnesses survive.

Under that explicit relaxation, write

\[
 b_L=82+s,
 \qquad b_S=1,
 \qquad b_B=83+s,
 \qquad r_B=16,
 \qquad g=67+s.                                   \tag{7.12}
\]

For `0<=s<=12`, a minimal A-to-B path implementation can delete `g` AA
edges and add no AA joins.  Its exact edge counts are

\[
 \#AA=\#BB=362-s,
 \qquad
 \#AB=133+2s.                                     \tag{7.13}
\]

The q1 spare table, displaying both symmetric deck pairs, is

\[
\begin{array}{c|cc}
&\text{top-lower/no-top-upper hard palettes}
&\text{no-top-lower/top-upper easy palettes}\\ \hline
\text{spare}&27-s&66+s.
\end{array}                                       \tag{7.14}
\]

If every superblock has length at least four, the lower-q2 occurrence
spares are

\[
\begin{array}{c|cc}
&z\text{-containing}&z\text{-free}\\ \hline
\text{cells}&295-2s&561+2s\\
\text{target orbits}&201&335\\
\text{spare}&94-2s&226+2s.
\end{array}                                       \tag{7.15}
\]

Thus same-rail restorations change the net run count rather than consuming a
fixed twelve-slot reserve.  The optimistic `r_B=16` relaxation gives
`g<=94` exactly when `s<=27`; hence it permits total gross cuts through
`b_B=110`, or large-component cuts through `b_L=109`.  This is not an
existence claim.  The interval `b_L=82..94` is merely the requested
conservative first tranche, not a hard upper window.

For the facet rail, the bare collar lower bounds are different:

\[
 \tau_{\rm full}=60,
 \qquad
 \tau_{\rm boundary}=79.                          \tag{7.16}
\]

The `95` facet defect orbits and the complement value `82` cannot be combined
without an additional admissibility condition.  Any future claim of an
`82` facet optimum must state and audit that extra condition explicitly.

## 8. Exact dense q2 flow

Let `C_A,C_B` be deleted old edge sets and let the new seam schedule be fixed.
For a source A triple of colour `Y_i`, the old witness survives exactly when

\[
 \{e_i,e_{i+1}\}\cap C_A=\varnothing.             \tag{8.1}
\]

For a source facet-B triple of old colour `Z_i`, the top witness survives
exactly when

\[
 \{e_i,e_{i+1}\}\cap C_B=\varnothing.             \tag{8.2}
\]

When every superblock has length at least four, seam collars are disjoint and
every new seam contributes the two crossing triples formed with its immediate
left and right neighbours.  For an arbitrary schedule with adjacent seams,
the gain multisets below are instead defined by one global enumeration of new
three-state windows, so a shared triple is counted only once.  A triple
containing an A state is z-free; only a BBB triple can restore a z-containing
q2 target.  Therefore the exact dense gate is, target by target,

\[
 \lambda'_6(S)=lambda_6(S)-D_A(S)+G_A(S)\ge1
 \quad(S\in\tbinom{[15]}6),                       \tag{8.3}
\]

\[
 \lambda'_5(Q)=lambda_5(Q)-D_B(Q)+G_B(Q)\ge1
 \quad(Q\in\tbinom{[15]}5).                       \tag{8.4}
\]

Here `D_A,D_B` count destroyed native windows under (8.1)--(8.2), while
`G_A` counts rank-six intersections of new AAA or mixed triples and `G_B`
counts rank-five intersections of new BBB triples.  Equations (8.3)--(8.4),
not the ample scalar spares in (7.15), are necessary and sufficient for
lower q2.

They must be solved simultaneously with the q1 colour flow

\[
 \mu'_R=\mu_R-c_R+y_R\ge1,                        \tag{8.5}
\]

the seam Johnson/core equations, residence collars, component voltage,
higher upper witnesses, and finally `COMP_3`.  This is the precise
BB-restoration/seam scheduling problem left by the audit.

## 9. Comparison with the direct quotient benchmark

The new benchmark

```text
scratch/k16_connected_q1_lower2_hamilton_20260729.json
SHA-256 16fc3739b8b4df5bed71c44b2f2e148f4839753cab6b9ea308e78d17ee9c32d8
```

is one physical Hamilton cycle with exact **quotient-orbit** audit vector

```text
q1 lower holes       2
q1 upper holes       0
q2 orbit holes      89
arbitrary-upper orbit holes
                    129
short runs        3420
```

The four-block source lift has the following literal physical-path vector:

```text
q1 lower holes       0
q1 upper holes       0
lower q2 holes       0
arbitrary upper      1
short runs        1426
```

The shadow-hole columns are not numerically commensurate: the benchmark
reports missing rotation orbits, whereas the four-block audit reports
literal physical targets.  Nevertheless the zero lower-q1/q2 entries and
the single physical arbitrary-upper hole make the four-block a useful exact
shadow seed.  The chronology counts also use different boundary conventions:
the benchmark reports cyclic short runs, while the four-block audit reports
internal runs of a linear path.  This distinction cannot affect the no-go,
because `1422` untouched internal collars survive before any boundary count.
Its `1426` physical short runs still rule it out as a carrier.
The dense-B generalization remains the residence-focused competitor only
after the net-cut/restoration and q2 flow of Sections 7--8 are solved.

## 10. Frozen audits and proved boundary

The source-structure and budget audit is

```text
scratch/audit_k15_to_k16_lift5_facet_budget_20260729.py
SHA-256 c5c2f9517526fb542f4ee000ae17f7bcfad90c457318d1e4de905934d60b13c6

scratch/k15_to_k16_lift5_facet_budget_20260729.audit.json
SHA-256 2a44e8bdcb18073ebbe1b8ff331785df6d34d017cba70c64ad77ed4af0409496
```

Two independent exhaustive endpoint audits agree on `1290` triples, `90`
q1/q2 survivors, the six full profiles, and no finalist:

```text
scratch/audit_k16_dense_fourblock_lift_20260729.py
SHA-256 8faf26ee8b967d5a632303552fade759483356f7224a8eb643555cb76bb2e3e8

scratch/k16_dense_fourblock_lift_20260729.audit.json
SHA-256 915e3cbe7d8fab874056c46449c503b174582b54fa2da12c11e16918d2a3de7d

scratch/audit_k15_to_k16_lift5_fourblock_exact_20260729.py
SHA-256 5b1097d855be7204eefac0fad4a1885d37d25871289e29dcc0fdb111aabb4829

scratch/k15_to_k16_lift5_fourblock_exact_20260729.audit.json
SHA-256 7ac74def2de25ec745695affdf28acbebee375613f2a419d6e43dcd8017fd3c6
```

The final proved boundary is

\[
\boxed{
\begin{array}{l}
\text{literal }[A_0,A_1,B_1,B_0]\text{ lift: impossible, at least 1422 short runs};\\
\text{full lower q2 on its exact endpoint atlas: complete for 90 candidates};\\
\text{facet bank: evades the complement 16-colour no-go but suffers erosion};\\
\text{cross-only }82..94\text{ complement window: colour-impossible};\\
\text{dense complement/facet same-rail BB restoration with exact q1/q2 flow: open.}
\end{array}}
\]
