# Hall 21: protected legality routers and exact DM-circuit discharge

Date: 2026-07-28

Status: exact protected `H21 -> H21 -> H20` theorem, unconditional abstract
descent theorem, comparison of the five certified router/splitter descents,
and exact Hall-21/Hall-20 component audits.  The final common-`Q` assertion is
critical-shore local: no full global common-word lift is claimed.

## 0. Realized Hall-21 to Hall-20 theorem

The exact new route is

\[
 H21_{z=6}\xrightarrow{\operatorname{RF}(1510,5017,6136)}
 H21^{\rm port}_{z=6}
 \xrightarrow{\operatorname{RF}(885,1393,3668)}H20_{z=6}.       \tag{0.1}
\]

The matching ranks are `16362,16362,16363`; hence the deficiencies are
`21,21,20`.  The common full-profile ranks and contracted boundary ranks are

\[
\begin{array}{c|c|c}
\text{move}&\text{common rank}&\text{contracted boundary rank}\\ \hline
\operatorname{RF}(1510,5017,6136)&16338&24\to24\\
\operatorname{RF}(885,1393,3668)&16345&17\to18.
\end{array}                                                     \tag{0.2}
\]

The exact cross-shore gap matrix is

\[
 \begin{pmatrix}
 21&20&20\\
 20&21&20\\
 20&20&20
 \end{pmatrix}.                                                 \tag{0.3}
\]

Thus the final matching lower bound and a gap-20 Hall shore agree.

Every endpoint is a deck-exact permutation of the 6435 middle masks, a
Johnson path, depth-three resident, complete in every upper support layer
`q=1,...,7`, has four immediate-lower holes, and retains exactly the six zero
targets

\[
 5801,13616,13620,17738,21641,29776.
\]

The full lower-hole vectors are

\[
 (4,18,9,1,0,0,0),\quad(4,18,11,1,0,0,0),\quad
 (4,18,11,1,0,0,0).                                            \tag{0.4}
\]

So, exactly as at the preceding descent, the protected theorem does not claim
all-depth lower-support invariance.

### The exact component mechanism

The neutral router removes the `169/168` component rooted at `1920` and
creates the following `25/24` component rooted at `1801`:

\[
\begin{gathered}
1801,1803,1805,1807,1833,1835,1837,1865,1867,1869,1897,1933,1993,\\
5897,5899,5961,9993,9997,10025,14089,18185,18187,18249,22281,26377.
\end{gathered}                                                   \tag{0.5}
\]

This is component compression, not a graph isomorphism: the old and new
components have different sizes and roots.  Their target sets intersect only
in `1933`; the other 168 old targets leave the critical shore and 24 new
targets enter it.

On the new component, the improving braid has the exact restricted-profile
identity

\[
 \boxed{
 \{1801,1803,1833,1835\}
 \longmapsto
 \{1801,1833\},\ \{1803,1835\}.}                               \tag{0.6}
\]

All other restricted profile copies cancel with multiplicity.  The focal
matching rank rises from 24 to 25.  More concretely, the portal contains the
coarse cell and one pre-existing half-profile

```text
cell 14269: depth 2, start 1394,
P=(810,1578,1067), envelope=1835, mandatory=1793,
shore={1801,1803,1833,1835},
cell 8097: depth 1, start 1659, P=(809,1577),
            envelope=1833, mandatory=1792, shore={1801,1833}.
```

The final carrier has

```text
cell 9334:  depth 1, start 2896, P=(1577,809),
             envelope=1833, mandatory=1792, shore={1801,1833};
cell 9599:  depth 1, start 3161, P=(1577,809),
             envelope=1833, mandatory=1792, shore={1801,1833};
cell 16035: depth 2, start 3160, P=(1067,1577,809),
             envelope=1835, mandatory=1794, shore={1803,1835}.
```

There is one common `{1801,1833}` copy across the endpoints; after complete
profile cancellation, (0.6) is exactly the net one-column-to-two-column
split.  It saturates the `25/24` component, which disappears entirely from
the final positive DM shore.

The final DM shore has size `677/657`, is the disjoint union of 20 gap-one
components, and all 657 DM-right cells have pairwise distinct native traces.
One nonzero maximal-erosion word realizes those 657 pins simultaneously.
This is a literal common-`Q` theorem on the final critical shore only; it does
not lift an arbitrary global maximum matching to that same word.

By Theorem 3.1 below, (0.2), (0.3), and the protected endpoint audits prove
the exact Hall-20 claim.

## 1. The authoritative Hall-22 to Hall-21 route

The current route is

\[
 H22_{z=6}\xrightarrow{\operatorname{FF}(1320,5339,6194)}
 H22^{\rm port}_{z=6}
 \xrightarrow{\operatorname{FR}(778,2292,6368)}H21_{z=6}.
\]

The first move has common full-profile rank `16337` and contracted boundary
rank

\[
                         24\longrightarrow24.
\]

The second has common full-profile rank `16344` and contracted boundary rank

\[
                         17\longrightarrow18.
\]

Thus the matching ranks are `16361,16361,16362`, and the deficiencies are
`22,22,21`.  All three states are exact permutations of the 6435 middle
masks, Johnson paths, depth-three resident, complete in every upper support
layer `q=1,...,7`, and have four immediate-lower holes and six zero
candidates.

The neutral step is not a relabelling of a fixed DM circuit.  It removes the
old `160/159` component rooted at `449` and creates a new `24/23` component
rooted at `458`.  The improving step removes that new component.  After
cancelling its 22 unchanged restricted shores, the exceptional old shore

\[
                         \{462,16846\}
\]

is replaced by

\[
                   \{458,462\},\qquad\{16842,16846\}.
\]

The complete-profile contracted boundary rank rises from 17 to 18.  The
final critical shore has size `846/825` and is the disjoint union of 21
unit-defect components.

The deeper lower-support ledger is not invariant: its hole vectors are

\[
 (4,18,6,1,0,0,0),\quad(4,18,8,1,0,0,0),\quad
 (4,18,9,1,0,0,0).
\]

Accordingly, the protected statement here is residence, every upper support
layer, immediate-lower support, and the exact compiler graph.  It does not
silently assert preservation of every lower support layer.

## 2. The common algebra in all five descents

The certified neutral/improving pairs have the following exact contraction
data.  The H25 pair is a certified branch ending at Hall 24; the later rows
are the successive structural motifs used at the lower frontier.

| transition | neutral boundary rank | improving boundary rank | mechanism |
|---|---:|---:|---|
| H25 to H24 | `24 -> 24` | `20 -> 21` | plateau pivot and remote Hall current |
| H24 to H23 | `8 -> 8` | `19 -> 20` | same-component Boolean-diamond refinement |
| H23 to H22 | `10 -> 10` | `17 -> 18` | remote legality router, then `2/1` one-cell split |
| H22 to H21 | `24 -> 24` | `17 -> 18` | component compression, then discharge |
| H21 to H20 | `24 -> 24` | `17 -> 18` | `169/168 -> 25/24` compression, then square split |

The neutral move can therefore do three genuinely different things:

1. rearrange a focal component without changing its rank;
2. act in a remote component solely to make a focal splitter legal; or
3. delete one critical component and create a smaller replacement component.

The invariant theorem is not physical conjugacy of components.  It is exact
rank preservation at the neutral stage followed by a one-unit gain in the
full occurrence-labelled contracted boundary matroid.

## 3. Exact protected router--splitter theorem

Let `L` be a fixed target set of size `N`.  For an exact carrier `X`, let
`G_X=(L,R_X,E_X)` be its occurrence-labelled compiler graph and let
`nu_X` be its matching rank.  A protected carrier assertion may include the
middle deck, Johnson chronology, residence, chosen lower and upper support
ledgers, and specified common-`Q` pins.

### Theorem 3.1 (full-profile contraction descent)

Suppose

\[
                         X_0\xrightarrow r X_1\xrightarrow s X_2
\]

are literal carrier moves with the following properties.

1. All three endpoints satisfy the declared geometric protection conditions.
2. `r` is matching-neutral: `nu_1=nu_0=N-h`.
3. In the full occurrence-profile multisets of `G_1,G_2`, cancel only
   physically distinct cell copies having identical complete target shores.
   If the common bank has rank `mu`, then

   \[
       \nu_1=\mu+b,\qquad \nu_2=\mu+b+1.
   \]
4. `G_2` has a target shore of gap `h-1`.

Then `G_2` has deficiency exactly `h-1`.

#### Proof

Condition 3 gives `nu_2=nu_1+1=N-h+1`, so the deficiency is at most
`h-1`.  The shore in condition 4 gives a Hall lower bound `h-1`.  Hence
equality holds.  The protection assertions hold because they are endpoint
hypotheses on literal moves; no scalar matching calculation is used to infer
them.  \(\square\)

The cancellation must retain multiplicity.  Cancelling target incidences or
set-theoretic shore types without physical cell multiplicity can create a
spurious rank unit.

### Theorem 3.2 (unit-component discharge with exterior survival)

Let `C` be a positive-DM component of `G_1` such that

\[
 |C|=|N_{G_1}(C)|+1,
 \qquad
 \nu\bigl(G_1[C,N_{G_1}(C)]\bigr)=|C|-1.
\]

Put `n=nu_1=N-h`.  Suppose `G_2` contains a matching `Q` saturating all of `C`
and an exterior matching `M_ext` of size `n-(|C|-1)` whose target and cell
endpoints are disjoint from `Q`.  Then

\[
                         \nu_2\ge n+1.
\]

If, in addition, `G_2` has a shore of gap `h-1`, its deficiency is exactly
`h-1`.

#### Proof

A maximum matching of `G_1` internally matches all `|C|-1` right vertices of
the positive-DM component; deleting those edges leaves an exterior matching
of size `n-(|C|-1)`.  At the endpoint, `Q` and `M_ext` are disjoint, so their
union has size

\[
 |C|+n-(|C|-1)=n+1.
\]

The final equality follows from the displayed Hall shore, as in Theorem 3.1.
\(\square\)

The exterior matching is part of the certificate.  A local component rank
gain alone is insufficient when changed cells also serve exterior targets.

### Theorem 3.3 (literal common-`Q` lift)

In the setting of Theorem 3.2, let `P_2` be the maximal erosion controller of
`X_2`, and let `A_2` be a nonzero word with `A_{2,p}\subseteq P_{2,p}` at
every position.  Assume explicitly that

\[
              \bigcup_{p=i}^{i+D}A_{2,p}=X_{2,i}
              \qquad\text{for every central row }i.
\]

Suppose every edge of `Q\cup M_ext` is assigned to a distinct physical cell
and the union of the letters of `A_2` on that cell interval is exactly its
assigned target.  Then the one word `A_2` realizes all these pins
simultaneously while reconstructing the central middle chronology.

#### Proof

Each selected cell interval has the required OR by hypothesis.  All pins use
the same word, not independently thinned copies, and the displayed central
identity reconstructs the middle chronology.  \(\square\)

This is stronger than Hall matching, but it is still scoped to the selected
pin family.  A native certificate on one critical shore does not imply that
an arbitrary global maximum matching has a common-word lift.

## 4. Exact Hall-21 component atlas

For `scratch/k15_segment_braid_hall21_zero6.json`, independent compiler
reconstruction gives

\[
 |S|=846,\qquad |N(S)|=825,
\]

and exactly 21 connected components, each of target excess one:

| type | roots |
|---|---|
| `169/168` | `1920` |
| `161/160` | `960,8217,24610` |
| `160/159` | `8218` |
| `5/4` | `4213,7504` |
| `3/2` | `1103,18970` |
| `2/1` | `2420,2575,2676,9524,17683,19568` |
| `1/0` | `5801,13616,13620,17738,21641,29776` |

Every one of the 825 DM-right cells has a distinct native trace.  Reserving
those 825 native target-cell pairs—deleting both endpoints—leaves exterior
matching rank `15537`, and

\[
                         825+15537=16362.
\]

Thus the complete current DM native atlas extends to a global maximum
matching as an incidence statement.  The 15537 exterior matching edges are
not thereby proved native under the same word.

## 5. Alternative clean circuit and persistent Hall-20 gate

Among the six `2/1` components, exactly one is isolated at the level of the
**full**, not merely DM-restricted, physical cell profile:

\[
                         C_* = \{17683,21779\}.
\]

Its sole cell is

```text
cell = 15761
depth = 2
start = 2886
controller triple = (5394,21762,20739)
envelope = 21779
mandatory = 17683
full target shore = {17683,21779}.
```

Both targets have degree one, and both are adjacent only to cell 15761.
Deleting the two targets and this cell leaves exact matching rank `16361`.
Consequently, any protected endpoint which retains or reroutes an exterior
matching of rank 16361 and supplies two distinct focal cells has matching
rank at least

\[
                         16361+2=16363,
\]

which is Hall deficiency at most 20.

Here

\[
                         21779=17683\cup\{12\},
\]

where coordinate 12 is zero-based.  There is already an exact literal
common-`Q` **half-splitter**.  Delete coordinate 12 from all three controller
letters:

```text
(5394,21762,20739) -> (1298,17666,16643).
```

The new triple has union 17683.  Direct audit proves that every central
depth-three row is unchanged, the other 824 selected DM native pins are
unchanged, and every controller letter remains nonzero.  Thus cell 15761 can
be reassigned literally from 21779 to 17683 in one common word.

This rebase alone is not a rank gain.  The old native occurrence of 21779 is
unique among all 19,311 cells, so the rebase loses 21779 exactly when it gains
17683.  The sharp decorated router target is therefore a second physical cell
for 21779 which remains valid under the same rebased word.  Together with cell
15761 assigned to 17683, that second provider activates Theorem 3.2.

There is also a sufficient all-native maximal-erosion normal form:

\[
 \begin{array}{c|c|c}
 \text{target}&\text{proposed interior depth}&\text{native trace}\\ \hline
 17683&1&17683\\
 21779&2&21779.
 \end{array}
\]

All three letters of the current triple contain coordinate 12, so neither
current adjacent pair has union 17683.  If one insists on a nested one-collar
all-native realization, the new collar must satisfy either

\[
 P_s\cup P_{s+1}=17683,
 \qquad
 P_s\cup P_{s+1}\cup P_{s+2}=21779,
\]

or the analogous right-pair equations hold, with the exact mandatory-mask
conditions.  This is a second sufficient completion, not a necessary form for
an arbitrary endpoint with separated focal cells.

### Corollary 5.1 (strict focal replacement closes Hall 20)

Suppose a protected endpoint has two distinct cells which match 17683 and
21779 separately, retains or reroutes an exterior matching of rank 16361
disjoint from those cells, and has exactly 826 physical neighbours on the old
846-target critical shore.  Then the endpoint has deficiency exactly 20.

Indeed, the exterior and focal matchings have total size 16363, while the old
shore has gap 20.  The matching lower bound and Hall upper bound agree.  A
particularly transparent sufficient occurrence ledger is that the other 824
old-shore neighbours persist and the sole focal neighbour is replaced by two
focal neighbours.  Since every literal carrier has a fixed number of cells,
any second focal cell must come from a simultaneously changed spare profile;
its effect on the exterior matching is included in the rank-16361 hypothesis.

If one reconstructing nonzero final controller assigns the two cells to
17683 and 21779 and preserves the other 824 DM pins, that one word also
supplies the exact 826-pin old-shore certificate.  The corollary is a
sufficient local theorem; a real braid may change other collar cells, so
both the exterior-rank and shore-current hypotheses must be audited literally.

The other five `2/1` cells have larger full shores:

```text
{2420,2932}:   {2416,2420,2928,2932}
{2575,2607}:   {519,527,551,559,2567,2575,2599,2607}
{2676,10868}:  {2672,2676,10864,10868}
{9524,9588}:   {1332,1396,9524,9588}
{19568,27760}: {19536,19568,27728,27760}.
```

They remain valid candidates, and `{2575,2607}` has the most developed
graded-collar tooling.  But `C_*` is the unique `2/1` target for which the
old component cell consumes no exterior target capacity at all.

All six pairs have the same audited half-splitter: delete the unique added
coordinate from all three letters of the sole depth-two cell.  This rebases
the atom pin to the component core while preserving the central chronology,
the other 824 selected pins, and nonemptiness.  In every case the atom's old
native occurrence is unique, so every such rebase is one-for-one until a
neutral router supplies a second atom/provider cell.  The special advantage
of `C_*` is full-profile isolation, not the existence of the rebase itself.

The realized Hall-20 route does not consume `C_*`.  In the final carrier it
persists with exactly the same full profile and controller triple, transported
to

```text
cell 16881, depth 2, start 4006,
P=(5394,21762,20739), envelope=21779, mandatory=17683,
full shore={17683,21779}.
```

Deleting these two targets and cell 16881 from the Hall-20 graph leaves exact
matching rank 16362.  The same rebase

```text
(5394,21762,20739) -> (1298,17666,16643)
```

preserves every central row, the other 656 final DM native pins, and
nonemptiness.  Hence the sharp local Hall-20-to-Hall-at-most-19 target is now
a second `21779` provider compatible with this rebase and residual rank
16362.  A final gap-19 shore would make the value exact.

### Common-`Q` target at `C_*`

After removing cell 15761, the other 824 current DM-right cells have 824
pairwise distinct native traces, none equal to either focal target.  Therefore
one final reconstructing nonzero controller word which preserves or reroutes
those 824 pins and realizes the two focal pins realizes

\[
                         824+2=826
\]

pins on the old 846-target shore.  This gives a selected-pin deficit of 20
on that shore.  If the same shore is certified to have final neighbourhood
size 826, the common-`Q` gap is exactly 20; without that upper bound the
statement is only the explicit 826-pin lower bound.  This is the correct
pin-level target for the splitter: a scalar Hall-20 endpoint without these
simultaneous 826 pins does not certify it.

At the realized Hall-20 endpoint the corresponding current target is
`656+2=658` simultaneous pins on its 677-target shore, a selected-pin deficit
of 19.  As before, exact common-`Q` gap 19 additionally requires the
neighbourhood upper certificate.

## 6. Reusable exact certificate for Hall 20 to Hall 19

A proposed neutral-router/splitter pair from the realized Hall-20 carrier must
certify
all of the following.

1. **Literal chronology.**  Each child is the declared signed segment
   permutation of its parent, has all 6435 middle masks once, and every new
   seam is a Johnson edge.
2. **Residence.**  The complete depth-three run audit passes; checking only
   the three endpoint Johnson tests is insufficient.
3. **Upper tower.**  Every union layer `q=1,...,7` remains support-complete.
   If immediate-lower holes four and zero count six are claimed, audit them
   separately.  Do not infer deeper lower support from these conditions.
4. **Neutral rank.**  The intermediate graph has matching rank 16363 and a
   certified gap-20 shore.
5. **Full-profile splitter rank.**  Cancel identical complete cell shores
   with multiplicity, compute the common rank, and certify contracted
   boundary rank `b -> b+1`.
6. **Exterior survival.**  For `C_*`, after deleting its two targets and the
   two reserved final cells, the endpoint residual graph has matching rank at
   least 16362.  This is one ordinary forced-pair max-flow/min-cut check.
7. **Exact Hall value.**  Exhibit a final shore of gap 19; the matching lower
   bound alone proves only deficiency at most 19.
8. **Common-`Q`.**  In one nonzero reconstructing final controller word, list
   656 preserved or rerouted outside pins and two distinct focal cells whose
   interval ORs are 17683 and 21779.  For a global word claim, additionally
   certify the remaining exterior matching pins under that same word.

The neutral router is allowed to act remotely or to replace the focal DM
component, as the preceding exact routes demonstrate.  What matters is the
endpoint protected ledger and the complete occurrence-level rank/current
certificate.

## 7. Raw audit evidence

Authoritative Hall-21 to Hall-20 carriers and generic audit:

```text
1a6985b38d9ae85f957a98a2b05d154e6c21e878a72826fec98fe2490655f394
  scratch/k15_h21_h20_root1801_chain/router/candidate_0000.json
0740f2a73b6bf2b01a5f30713e69c636f60bf8cf8c47c8bbb798d69787fc43be
  scratch/k15_h21_h20_root1801_chain/final/candidate_0000.json
b730c31f963d60fbfa09b63e1f8caaa02be0762574304d9be2e9308f7def6d03
  scratch/audit_k15_h21_to_h20_root1801_chain.json
```

Independent component/splitter reconstruction:

```text
efa659245062fb8956a2ab17ec1fd2a6f0a90810afd95ed44c268488eaa42427
  scratch/audit_k15_h21_h20_root1801_structure.py
84e0ba2786e493259dc8da16c1516b06036ccd48490494c3e97b473294fb2ca5
  scratch/audit_k15_h21_h20_root1801_structure.json
```

Authoritative H22 to H21 audit:

```text
cc862804ea8910371283e8fdb42c1ac94ce9ed1cb5e0d3b5cdd94e8d74211e5c
  scratch/audit_k15_segment_braid_hall22_to21.json
1e2ad82979d747853fcf0b2a2c4e87aa1101a144ee2201474e7688f7cc3ebfdf
  scratch/audit_k15_segment_braid_descent.py
```

Independent route reconstruction:

```text
595e2b9a3cafc73812c9129b4d8ab9dc84db996b7f16b932633d283f210c88e8
  scratch/audit_k15_h21_zero6_independent.py
2812bb93955be5164650efc27787f1939c556bfcd5b69aa39ce60675fefc8b20
  scratch/audit_k15_h21_zero6_independent.json
```

Carrier hashes:

```text
bb3f8b922e7e741329c4cff551363a9bc244a4c77dcc1fd70d6accc7b8c91778
  scratch/k15_segment_braid_hall22_zero6.json
0f8b287ad290139e61a4387e90cf5c7eaaa3166a2e20ac642815ce9604e974ea
  scratch/k15_segment_braid_hall22_portal_to21.json
8a294110b530ba016b790f08f59c9d5bca3471af732867e27b0cb4a0b628b447
  scratch/k15_segment_braid_hall21_zero6.json
```

Hall-21 component reconstruction:

```text
5b6ac90b3beb3eb96efd977257da222a8710b623734e3b425e4d40cfeab74999
  scratch/audit_k15_h21_dm_components.py
eb33370c853bed9fa8df325c24a9ec5eac52024281cbd7fc2d6bc7a7939d18e7
  scratch/audit_k15_h21_dm_components.json
```

Clean-circuit reconstruction:

```text
ca15d6fbc3ed88ffa6e165d7cc07ad977a81ef299141f93670ec8dcf34f97843
  scratch/audit_k15_h21_clean_circuit_target.py
89515e3581550e1da1b7f59cb6af8b7efb1bf34dbbce1feaef97a5e3766eec98
  scratch/audit_k15_h21_clean_circuit_target.json
```

The structural scripts perform no braid search.  They reconstruct fixed
compiler graphs, decompose DM shores, and run ordinary matching calculations.

## 8. Sharp remaining boundary

The proved result now includes the exact Hall-20 carrier.  The next missing
statement is constructive:

> Find a protected neutral braid composition which supplies a second cell for
> `21779` compatible with the audited Hall-20 cell-16881 rebase to `17683`,
> while preserving 656 outside pins and an exterior rank-16362 matching.  An
> all-native depth-one/depth-two split is an alternative sufficient endpoint.
> Otherwise prove that the protected braid groupoid cannot hit either
> decorated splitter germ.

No transitivity of neutral braids, no Hall-19 carrier, and no global
length-6438 word is asserted here.  The final 657-pin common-`Q` certificate
remains critical-shore local.
