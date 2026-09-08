# Independent audit of the marker58 double-C6 connected q1 factor

Date: 2026-08-02  
Lane: AD  
Status: **GO** for the exact connected owner/lower-q1/upper-q1 carrier;
**NO-GO** for residence of every one-cut opening of this fixed carrier, and
an exact flat-depth-three all-width upper obstruction.  This is not a source
word or a compiler certificate.

## 1. Exact verdict

The sparse primary certificate

`scratch/ad_k17_marker58_upper_q1_quotient_independent_20260802/c68b.double_fusion.model`

selects a `Z_17`-equivariant quotient two-factor with one quotient cycle and
cycle voltage `4 mod 17`.  Literal development gives one physical cycle on
all `24,310` rank-nine owners.  Its `24,310` Johnson edges use every
rank-eight intersection exactly once and cover all `19,448` rank-ten unions.

The protected bank is not merely equinumerous with the marker bank.  Its
edge set equals exactly the development of the first 58 rows of the frozen
marker witness, with opening type 3: 986 vertex-disjoint four-edge paths,
3,944 protected edges, and 4,930 protected owners.

This positive carrier has an exact fixed-order obstruction:

* it has `5,372` cyclic positive one-runs of lengths below four;
* no linear cut is depth-three resident;
* a best cut clips only three such runs and leaves `5,369` internal;
* at that best cut every maximal depth-three envelope is nonempty, but only
  `12,670/24,310` owner rows are reconstructed, hence `11,640` mismatch;
* its cyclic owner-interval upper deck misses 1,972 rank-11, 510 rank-12,
  and 51 rank-13 targets.  Ranks 14 through 17 are complete.

Thus the connected q1 factor is a genuine positive central carrier and a
fixed-chronology residence no-go.  It also fails the standard owner-interval
upper-shadow gate at ranks 11--13, which is necessary for a flat depth-three
antecedent.  It cannot be used as the final flat depth-three carrier without
changing selected edge orbits.

## 2. Two quotient C6 switches

Let `M_0`, `M_1`, and `M_2` be respectively the original `c68b`, the
single-fusion, and the double-fusion sparse primary selections.  Each has
exactly 1,198 selected residual options.  Together with the 232 immutable
protected quotient edges, every stage has one edge per rank-eight orbit,
degree two at every rank-nine owner orbit, and all 1,144 rank-ten cap orbits
covered.

The first transition removes variables

`{19,150,2935}`

and adds

`{2,178,2941}`.

It acts on facets `{255,495,1977}` and the six distinct owner
representatives

`{511,1279,1981,2041,3955,3961}`.

The red and blue edges are complementary perfect matchings on one simple
six-cycle in the quotient owner graph.  The quotient component count changes
`3 -> 2`.  Its physical development is one alternating `C_102`, not 17
disjoint physical `C_6`s.

The second transition removes

`{1267,19509,19825}`

and adds

`{1269,19510,19816}`.

It acts on facets `{1271,9145,9335}` and owners

`{5085,9147,9463,10169,15257,15273}`,

again one simple alternating six-cycle in the quotient owner graph.  Its
removed and added cap multisets are both `{10171,15289,20341}`, and the
component count changes `2 -> 1`.  Its physical development is 17 disjoint
alternating `C_6`s.

For either switch, if the old edges are

`e_j^-={c_j,d_j}`

and the new edges are

`e_j^+={d_j,c_(j+1)}` with `c_3=c_0`, then

`sum_j(1[v in e_j^+]-1[v in e_j^-])=0`

for every owner `v`.  Thus both switches preserve owner degree; unchanged
facet addresses preserve exact rank-eight use.  Rank-ten coverage is a
separate full-stage fact: the first switch changes its cap multiset from
`{3963,4089,10233}` to `{1535,3963,4083}`, whereas the second preserves its
cap multiset.  Replaying every stage proves that all 1,144 quotient cap
orbits remain covered, although their loads need not remain one.

The 232 protected edges are fixed rather than selected by option variables,
so a switch cannot replace one.  In addition, the twelve switched owner
representatives are disjoint from the 290 protected owner representatives.
Finally, the independent lineage replay set-compares the published final
factor with the literal 17-fold development of `M_2`; the two 24,310-row
sets are identical, including protected bits.  These are the reasons the
protected marker paths survive; facet disjointness alone would not prove
absence of a protected-owner incidence.

## 3. Quotient voltage and physical topology

For a physical mask `X`, write

`X=R^sigma(X) rep(X)`,

where `rep(X)` is its least cyclic rotation.  A quotient edge represented by
physical endpoints `A,B` has signed voltage

`sigma(B)-sigma(A) mod 17`.

The final quotient graph is a single 1,430-edge cycle and its independently
accumulated voltage is `4`.  Since `gcd(17,4)=1`, its voltage prediction is
one lift of length `17*1430=24,310`.  This was not used as a connectivity
assumption: a separate BFS over all developed physical edges also returns
one component of size 24,310.

The model file is a sparse custom primary witness, not a complete DIMACS
assignment.  It lists 1,198 positive primaries and omits 34,515 false
primaries and all 168,454 sequential-counter auxiliaries.  The exact primary
resource equations and their literal lift pass; the `SATISFIABLE` token must
not be cited as a full clause-by-clause solver model.

## 4. Protected-path preservation

For each of the first 58 frozen base masks `x`, put

`U_x={0,1,2,3,4,5} union supp(x)`, and define `v_i=i+1` for
`i in Z_5`.

Opening the native five-cycle at edge 3 orders its owners as

`C_4,C_0,C_1,C_2,C_3`,

where `C_i=U_x-{v_(i-1 mod 5)}`.  The four consecutive edges are exactly the
232 fixed quotient rows, in file order.  Developing all 17 shifts gives
exactly `232*17=3,944` protected edges.  The replay verifies both the fixed
row sequence and equality of the developed edge set.  Thus the two quotient
C6 switches preserve all 986 protected paths literally.

This does **not** bind the marker theorem's source/buffer occurrences to
positions of a source word.  It binds only owner incidences and their
rank-eight/rank-ten edge colours.

## 5. Fixed-order residence and flat erosion no-go

The unique physical cycle is determined up to rotation and reversal.  For
each old coordinate it has 1,430 positive runs.  The short-run census is

| run length | physical runs | `Z_17` run orbits |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 2,873 | 169 |
| 3 | 2,499 | 147 |

Therefore the total is `5,372 = 17*(169+147)`.  Exhausting all 24,310
possible cuts gives zero resident openings.  The best residual is 5,369;
272 cuts attain that value.

At the recorded best cut, let `T_0,...,T_(W-1)` be the linear owner row and
define its maximal depth-three antecedent

`E_j = intersection {T_i : max(0,j-3)<=i<=min(W-1,j)}`,

for `0<=j<W+3`.

All `W+3` envelopes are nonempty.  Their ranks have histogram

`6:21435, 7:2874, 8:2, 9:2`.

Nevertheless

`T_i != E_i union E_(i+1) union E_(i+2) union E_(i+3)`

at 11,640 indices.  Since every possible depth-three source letter at
position `j` is contained in `E_j`, failure of the maximal row proves that
this particular opening has no flat depth-three antecedent.  The 11,640
number is **not** claimed to be minimized over all cuts; residence already
fails for every cut.

## 6. Exact deeper-upper boundary

A separate accumulated-union scan of the fixed physical cycle gives

| rank | covered | total | holes |
|---:|---:|---:|---:|
| 11 | 10,404 | 12,376 | 1,972 |
| 12 | 5,678 | 6,188 | 510 |
| 13 | 2,329 | 2,380 | 51 |
| 14 | 680 | 680 | 0 |
| 15 | 136 | 136 | 0 |
| 16 | 17 | 17 | 0 |
| 17 | 1 | 1 | 0 |

These are exactly the cyclic owner-interval unions of this order.  They show
that rank-ten completeness does not propagate to ranks 11--13.  Moreover,
they are necessary for every flat depth-three antecedent of a linear opening:
an interval of at most three source letters has union rank at most nine,
whereas every interval of at least four source letters is exactly a union of
consecutive owner windows.  A mask absent from the cyclic owner-interval deck
therefore remains absent after every cut.  Completeness of the cyclic deck at
ranks 14--17 is not by itself a certificate for a particular cut or source,
and a genuinely nonflat compiler is outside this implication.

## 7. Residence-aware strengthening

The current quotient master already has the correct protected fixed rows,
one option per residual facet, weighted owner degree two, and eager rank-ten
cover rows.

There is an important scope distinction.  Generic linear-opening residence
uses an explicit opening/seam variable.  On the target face here—one
connected, nonzero-voltage `Z_17` lift—no such variable is needed.  Indeed a
short `(coordinate,run)` has a free orbit of size 17.  Its bracketing path
contains at most four edge occurrences.  For a fixed physical cut edge and
each occurrence of its quotient edge orbit in that path, at most one group
translate contains the cut.  Hence one cut can boundary-clip at most four of
the 17 translated short runs.  It cannot make the other members legal.
Consequently, on this connected equivariant one-cut face, a resident linear
opening exists if and only if the cyclic lift has no short run.  Before
connectivity and nonzero voltage are imposed, the variable-only rows below
are only the stricter cyclic-residence face; a generic multi-component
opening model must retain its opening terms.

The exact zero-new-variable cyclic layer is a lazy labelled-walk separator
on the existing primary variables.

For every selected physical bracket walk

`X_0,X_1,...,X_(ell+1)`, `ell in {1,2,3}`,

whose internal owners contain a coordinate and whose two exterior owners do
not, let `supp(P)` be its set of selected quotient edge-orbit variables.
Add

`sum_(e in supp(P)) x_e <= |supp(P)|-1`.

Also add the analogous no-good for a selected constant-one triangle.  On the
full exact-facet, simple developed two-factor face above, these
width-at-most-four clauses are equivalent to strict cyclic residence at least
four; weighted degree two alone would not suffice.  No age relaxation is
involved.

For this incumbent an independent support projection finds exactly 316
distinct violated clauses: 169 from length-two runs and 147 from
length-three runs.  Every support occurs in exactly 17 physical rotations.
After substituting immutable fixed edges as true, their width histogram is

`width 1:37, width 2:15, width 3:149, width 4:115`.

There is no empty clause, so this incumbent separator round does not by
itself prove the protected fibre residence-infeasible; however, 37 currently
selected option variables are individually forbidden.  Global feasibility
of the protected fibre remains open.  These 316 clauses are only the first
CEGAR round, not a complete static catalogue.  Future candidates must be
decoded and separated again.  Connectivity cuts and a nonzero-voltage check
must remain in the loop, because residence clauses do not imply one physical
component.  Conversely topology and voltage do not imply residence.

Every new flat candidate and opening must replay its nonwrapping accumulated-
union deck at ranks 11--17; only the current incumbent has holes solely at
ranks 11--13.  The lower target/cell Hall instance should be promoted only
after residence, exact nonempty erosion, and this upper-deck replay all pass.
A nonflat compiler is not excluded by this audit, but no nonflat source
positions, common-cap matching, or literal OR word are supplied.

## 8. Frozen artifacts and scope

Authoritative positive witness:

```text
70f48c248ab7e8fb7d08895048fcf7d5b27fca5ff6f389832e5c4f35cf25adb6  c68b.double_fusion.model
7d39e3aee641521df2d441d0342a2bd060dafb05cc7f5703ef206f53b6d21e3c  c68b.double_fusion.factor.tsv
85ae3d42671eea04fb016988b9095cb79fd20217ea6eec02d480910403bfe31b  c68b.double_fusion.audit.json
```

Independent lineage and lift replay:

```text
52ea33d9ac4b74de4cc4a5927a76f80579657c1e15f2561d40ae2ff5da27d3a9  audit_ad_k17_marker58_double_c6_lineage_20260802.py
c7ba66574f7d2c6f8fdf5a2e40c5b36776d2c7c72daf0fd3add665821279b9d3  double_fusion.two_c6_lineage.independent.audit.json
4e622d145c51b65d75ef455361ed6348cd7327e8fd7f2d6937af6075a9cae21b  replay_marker58_c68b_physical_voltage_exact_independent_20260802.py
33731d36f4d2df10106fbe8f7c006b6d0718fc5902a22206d82f694d9241b645  double_fusion.physical_voltage_exact_independent_20260802.audit.json
```

Residence and upper-deck replay:

```text
3a84b4a1334d088e67595e4597eabd1c10a2c2e2d6bb5062bb994cc7fa8baeba  audit_k17_double_fusion_residence_20260802.cpp
7066ad573f3acb18fa583a9eb701f38cc16598d8d47187ce4dd901b9eceb81dd  c68b.double_fusion.residence.audit.txt
e885f32bab18d4f493f0cb4ed1738d5bfd71534c33c281a1859b7a6858a5c806  audit_k17_marker58_connected_cycle_residence_compiler_20260802.cpp
a6d39ff89c9425a829eeb1b68b50dca0fbc0a4b928211ba407bce39ed33e718f  double_fusion.residence_compiler_independent_20260802.audit.json
5457fd42dbef8a59f54551f36b2307a1859bdf928aacc8f768a6318e3b4ec8e8  audit_ad_k17_marker58_connected_deep_upper_20260802.py
75d47529d45bc22126dc4049c1c8665a483357b43cba694bcf2b4edc2b756fee  double_fusion.connected_deep_upper.ad_independent.audit.json
c4afd0e954a43128f07c9388d04d303d09c503c9a9af2181c6bae261153db586  double_fusion.connected_deep_deck.holes.tsv
3a632bf28d007bd4da11bf169a2401695934aab14005d96500091d38e190d331  audit_ad_k17_marker58_residence_clause_supports_20260802.py
cb19a609d805fd95d2125d057869922e9b9d100b817afef43f0585f3bdd9fdaf  double_fusion.residence_lazy_clauses.independent.tsv
8101637517f8f454483661386f10fa319170043361a43b8145081f5b67f0e312  double_fusion.residence_lazy_clauses.independent.audit.json
```

The exact proved object is one connected, voltage-four,
owner/lower-q1/upper-q1 factor containing the frozen marker paths.  The exact
negative is restricted to that fixed factor/order.  Source/buffer binding,
residence-aware reselection, ranks 11--13 repair, any nonflat compiler,
common-cap Hall, and a universal contiguous-OR word remain open.
