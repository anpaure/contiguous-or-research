# `k=16`: seven-orbit seam floor and the exact quota-first Hall gate

Date: 2026-07-30  
Lane: R  
Status: exact finite reduction, sharp four-orbit service lower bound, complete
raw endpoint screen of the minimum orbit class, and independent physical
fixed-width replay of its three raw-perfect examples, followed by a complete
residence-safe completion no-go for those examples.  No
residence/q1-valid `k=16` carrier or word is claimed.

## 1. Authenticated source and the corrected residual target

Throughout this note the source factor is exactly

```text
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204

scratch/k16_asymmetric_len8_orbit_repair_20260730.audit.json
SHA-256 3e9c62c66d85ff6a8c242897a80dc2841eaf4fca9e908f50b8f1f5b697576e87
```

It is a spanning factor on all `12,870` rank-eight states, has `29`
components, cyclic positive residence at least four, and complete lower and
upper q1 palettes.  Its residual objective holes are the seven rotation
orbits

\[
\begin{split}
\mathcal L&=\{33337,33609,34069\},\\
\mathcal U&=\{36343,36599,39791,46811\}.
\end{split}
\tag{1.1}
\]

The first six orbits have size fifteen under rotation of coordinates
`0,...,14`; the orbit represented by `46811` has size three.  Thus (1.1)
means exactly

\[
3\cdot15+(3\cdot15+3)=45+48=93
\tag{1.2}
\]

physical missing masks.  In particular, the old rows `39911` and `40623`
are not residual rows for this source and are nowhere used below.

There is also a size-fifteen fixed upper-q4 hole orbit represented by
`40443`.  It is not part of the `93`-row objective because every one of its
physical rank-twelve masks still has an arbitrary-width union witness (in
fact at width six), so arbitrary-upper replay has no rank-twelve hole.

The lower rows are physical rank-six, old-coordinate rank-five lower-q2
targets and require a three-vertex intersection window.  The upper rows are
rank-eleven targets.  For a
single cross-component seam, the independently audited endpoint-minimal
upper support is exactly widths four and five when widths through eleven
are allowed.

## 2. Exact endpoint catalogue

The rebased directed-seam census gives, for one literal representative in
each row of (1.1), the following positive-residence-safe provider counts.
These counts include all providers at the indicated width, not only
endpoint-minimal ones.

| row | orbit size | minimum width | positive-safe providers at minimum width |
|---|---:|---:|---:|
| `L33337` | 15 | 3 | 98 |
| `L33609` | 15 | 3 | 102 |
| `L34069` | 15 | 3 | 74 |
| `U36343` | 15 | 4 | 164 |
| `U36599` | 15 | 4 | 172 |
| `U39791` | 15 | 4 | 264 |
| `U46811` | 3 | 4 | 300 |

For the four upper representatives, the positive-safe endpoint-minimal
counts at widths `(4,5)` are respectively

\[
(164,8),\quad(172,8),\quad(264,20),\quad(300,30).
\tag{2.1}
\]

The dedicated endpoint audit proves that no endpoint-minimal width outside
`{4,5}` occurs in this one-seam class.  The statement is source-relative:
it does not say that an interacting multi-seam packet has no longer
accepting union path.

The complete fixed-depth record counts are

\[
\begin{array}{c|rrrr|r}
\text{class}&0\text{ hits}&1\text{ hit}&2\text{ hits}&3\text{ hits}&\text{total}\\
\hline
\text{cross-component one seam}
 &2,053,290&62,580&1,980&30&2,117,880\\
\text{locally separated segment seam}
 &3,099,540&87,510&2,610&30&3,189,690.
\end{array}
\tag{2.2}
\]

Here a hit is one of the seven fixed rows in (1.1).  The rotation action on
an ordered record is free because it is free on its rank-eight tail.  Hence
the two universes in (2.2) contain exactly `141,192` and `212,646` full
record orbits.

The records include the two source-component orientation signs.  The
catalogue permits independent orientations while generating candidates; a
global master may not select those signs independently on overlapping
retained segments.  It must first fix a rotation-compatible component
orientation cocycle, or explicitly impose segment-orientation consistency.
Thus `212,646` is an exact candidate-record count, not a claim that all
those columns are simultaneously independent binary choices.

No q1 preservation or global endpoint completion is implicit in (2.1) or
(2.2).

There is no conflict with the separately audited fixed-direction physical
master.  After one displayed orientation is frozen on every source cycle,
that master has `211,604` admissible physical arcs and every arc hits at most
two of the `93` literal demands; hence it has the stronger physical bound
`c>=ceil(93/2)=47`.  The records in (2.2) allow the two incident retained
segments to use independent source orientations, so support three can occur.
Theorem 4.1 proves that even this larger signed-orientation class still needs
four full rotation orbits.  Orientation consistency is a global constraint,
not a discrepancy between the two censuses.

## 3. The one-cut fixed-depth obstruction and the width-five toll

A one-cut-per-component linearization of the `29` source cycles produces
`29` retained path segments and has only `28` new internal seams.  The
complete census (2.2) shows that one seam serves at most three of the
physical fixed lower-q2/upper-q3 holes.

### Theorem 3.1 (one-cut fixed-depth no-go)

No one-cut-per-component path linearization can repair all `93` residual
physical masks using only lower width three and upper width four seam
windows, even in the larger independently oriented record class (2.2).

### Proof

There are at most `28` new internal seams and at most three services per
seam.  Therefore there are at most

\[
28\cdot3=84<93
\]

fixed-depth services.  Each of the `93` missing masks needs at least one
service.  \(\square\)

This is an obstruction to this internal seam architecture, not a no-go for
outer compiler cells or for additional cuts.

### Corollary 3.2 (arbitrary-upper width-five toll)

In the same one-cut architecture, if arbitrary upper witnesses are allowed,
at least nine of the `48` upper masks must have no new width-four witness and
must instead be served at endpoint-minimal width five.  If the whole splice
is `C_15`-invariant, at least fifteen upper masks must be served at width
five.

### Proof

All `45` lower holes still require width three.  If `x` upper masks use no
width-four witness, the other `93-x` masks would have to fit in the
fixed-depth capacity `84`, so `x>=9`.  The endpoint-minimal support theorem
then forces width five for those `x` masks.  Under a fully invariant splice,
the set of masks without a width-four witness is a union of target orbits of
sizes `15,15,15,3`.  The least such union of size at least nine has size
fifteen.  \(\square\)

## 4. A sharp invariant service floor

For a seam record `e`, let `supp(e)` be the subset of the seven rows (1.1)
served by its fixed width-three/four crossing windows.  The complete arrays
behind (2.2) give the following two exact facts.

1. Every support-three record has the same signature

   \[
   \{L34069,U36343,U39791\}.
   \tag{4.1}
   \]

   There are exactly thirty records of this signature in either census.

2. Every support-at-least-two record containing `U46811` has signature

   \[
   \{U39791,U46811\}.
   \tag{4.2}
   \]

These statements were checked from the complete saved hit-at-least-two
arrays, not inferred from examples.

### Theorem 4.1 (four-orbit/sixty-seam floor)

Let a separated `C_15`-invariant packet be assembled from honest single-seam
records in (2.2), so that its fixed lower-q2/upper-q3 ledgers are additive.
If the packet serves every row in (1.1), it contains at least four full seam
orbits, hence at least sixty physical seams.

### Proof

If none of three columns has support three, their union has size at most
`2+2+2=6`.  Otherwise every support-three column has the fixed support
(4.1).  To cover `U46811`, one of the remaining columns must contain it.
By (4.2), that column contributes at most one row not already in (4.1),
namely `U46811`.  The last column contributes at most two further rows.
Thus three columns cover at most

\[
3+1+2=6<7.
\]

At least four columns are necessary.  A free seam orbit has fifteen
physical members, giving sixty physical seams.  \(\square\)

The proof uses the complete raw record universe, so it remains valid after
restricting to positive-safe or q1-safe records.  It is a service lower
bound, not an existence theorem.

Independently, every lower target contains the distinguished coordinate and
can only be supplied by a BB seam in this rail model.  A BB seam supplies at
most two lower-q2 targets.  Consequently at least `ceil(45/2)=23` physical
BB seams are needed, and an invariant packet needs at least two BB seam
orbits, or thirty physical BB seams.

## 5. Exact quota-first Hall theorem

The service floor does not solve endpoint routing.  The correct exact
object is a quota matching.

Fix a cut set `X`.  Assume first that its collars are separated far enough
that every target window under consideration crosses at most one new seam.
Let

\[
\Gamma_X=(L_X,R_X;E_X)
\tag{5.1}
\]

be the bipartite multigraph of legal terminal-to-initial seam records.  The
parallel edges retain their phase voltages.  Let

\[
b_X(T)=\#\{\text{old witnesses for }T\text{ wholly retained after }X\}
\tag{5.2}
\]

and let `a_T(e)` be the nonnegative number of new single-seam witnesses for
`T` created by `e`.  Define

\[
\mathcal D_X=\{T:b_X(T)=0\}.
\tag{5.3}
\]

Crucially, `D_X` includes not only the seven old deficit rows but every q1
or deeper target whose last old witness is cut.

### Theorem 5.1 (quota bank first, ordinary Hall second)

Suppose `|L_X|=|R_X|`.  There is a perfect matching `M` of `Gamma_X` such
that

\[
b_X(T)+\sum_{e\in M}a_T(e)\ge1
\qquad\text{for every required target }T
\tag{5.4}
\]

if and only if there is a partial matching `Q` such that

\[
b_X(T)+\sum_{e\in Q}a_T(e)\ge1
\qquad(T\in\mathcal D_X)
\tag{5.5}
\]

and the residual graph `Gamma_X-V(Q)` satisfies Hall:

\[
|N(S)|\ge |S|
\qquad(S\subseteq L_X-V(Q)).
\tag{5.6}
\]

Moreover, when every demand in (5.5) has threshold one, `Q` can be chosen
with

\[
|Q|\le |\mathcal D_X|.
\tag{5.7}
\]

### Proof

If `Q` satisfies (5.5) and the residual graph satisfies Hall, Hall's theorem
completes `Q` to a perfect matching.  All coefficients `a_T(e)` are
nonnegative, so adding residual edges cannot destroy a covered row.

Conversely, let `M` satisfy (5.4), and choose an inclusion-minimal subset
`Q` of `M` satisfying (5.5).  Then `M-Q` is a perfect matching of the
residual vertices and witnesses (5.6).  Finally, every edge of a minimal
`Q` has a private demand row that would fail if that edge were deleted.  A
threshold-one row cannot be private to two different edges, so private rows
inject the edges of `Q` into `D_X`, proving (5.7).  \(\square\)

### Why ordinary Hall alone is insufficient

In `K_(2,2)`, put quota `A` on the two diagonal edges and quota `B` on the
two off-diagonal edges.  Hall holds and both quotas have providers, but the
two perfect matchings cover `A` and `B` separately; neither covers both.
Thus marginal provider abundance plus endpoint Hall is not a quota theorem.

### Exact signed rows

For an actually selected cut set, the coverage row is

\[
\mu_T-L_X(T)+\sum_e a_T(e)z_e\ge1,
\tag{5.8}
\]

where `L_X(T)` is the exact union-counted number of old witnesses meeting at
least one cut.  Summing individual cut losses is invalid when cut windows
overlap.  If seams are not separated, new witnesses can cross several
seams; then (5.8) must be replaced by the accepting-path constraints of the
assembled accumulated-union/intersection automaton.  The single-seam
catalogue remains only a candidate generator in that regime.

## 6. Orbit and voltage refinements

After fixing a consistent quotient orientation (or retaining the sign
double cover explicitly), a fully invariant cut set satisfies the exact
port equations

\[
\sum_{e:\operatorname{tail}(e)=a}z_e=c_a,
\qquad
\sum_{e:\operatorname{head}(e)=a}z_e=c_a
\tag{6.1}
\]

for every selected cut-transition orbit `a`.  These are the quotient
perfect-matching equations.  The seven scalar service rows are exact only
because both the source and the selected packet are invariant.

Without invariant selection, retain one row for every physical phase.  The
current residual system then has exactly `93` rows, not seven average rows.
For the short orbit `46811`, congruences are taken modulo three, so a
fifteen-member seam orbit may contribute five times to each physical mask.

Endpoint equations produce a factor, not necessarily one physical cycle.
If a quotient cycle `C` has total phase voltage

\[
v(C)=\sum_{e\in C}\theta(e)\pmod {15},
\tag{6.2}
\]

then its lift has `gcd(15,v(C))` physical cycles.  Connectivity and voltage
are therefore obligations after quota Hall; neither follows from it.

The frozen rank-eight transition action has `858=12870/15` free cut orbits.
Before q1/collar filtering, the locally separated catalogue in (2.2) gives
`212,646` directed signed candidate-record orbits.  A sound finite invariant
master for the separated audited horizon has:

1. cut-orbit variables and (6.1);
2. legal seam-record variables with phase voltage and global
   orientation/segment consistency;
3. the seven residual quota rows, plus every signed q1 and collateral row
   from (5.8);
4. cut-distance/collar compatibility constraints;
5. residual Hall, or the matching equations themselves;
6. quotient connectivity and the voltage condition if one carrier cycle is
   required;
7. a final literal compiler/source-selector replay.

This is an exact seam-orbit skeleton justified by the present catalogue.
For full arbitrary-depth upper preservation, item 3 must be replaced or
augmented by the accumulated-union accepting-path constraints; the
single-seam fixed-depth ledger is not sufficient.  Dropping item 3 to the
seven positive rows is already unsound.  The authenticated joint q1 edge
load histogram is

\[
(1,1)^{7365}(1,2)^{2445}(1,3)^{300}
(2,1)^{2445}(2,2)^{15}(3,1)^{300}.
\tag{6.3}
\]

Thus `12,855` of the `12,870` old edges are unique on at least one q1 shore;
only the fifteen `(2,2)` edges are redundant on both.  Any selected cut set
must charge its actual q1 losses rather than assume the seven positive rows
are the whole ledger.

## 7. A literal four-orbit quota bank and its Hall failure

The lower bound of Theorem 4.1 is attained at the level of service rows.
The following four directed records use the format

```text
(left tail, left cut mate, right cut mate, right head,
 left source sign, right source sign).
```

| record | fixed services |
|---|---|
| `(58818,58594,50634,52674,-1,+1)` | `L34069,U36343` |
| `(48514,48513,63682,48322,-1,-1)` | `L33337,U36343` |
| `(47944,62280,40536,47704,+1,+1)` | `L33609,U36599` |
| `(13907,12887,46614,46674,+1,-1)` | `U39791,U46811` |

Each record occurs in the complete locally separated hit-at-least-two
array.  Taking all fifteen rotations gives:

```text
four seam orbits             60 distinct Johnson seams
source cut support           120 distinct old edges
minimum cyclic cut gap       12
residual rows covered        all seven
```

The exact inward-collar replay proves every one of the sixty seams
positive-residence-safe.  Gap twelve makes their depth-three/four local
ledgers simultaneous.  This is therefore an integral, literal quota bank,
not an abstract profile.

It cannot, however, be completed without further cuts while retaining those
cuts and seams.
After deleting the 120 old edges and adding the 60 quota seams, the partial
graph has degree histogram

\[
2^{12750},\qquad1^{120}.
\tag{7.1}
\]

Among the 120 degree-one endpoints, exhaustive direct Hamming-distance-two
testing finds only thirty raw Johnson edges and seventy-five isolated
endpoints.  In particular, endpoint `4795` has no raw residual neighbour:

\[
S=\{4795\},\qquad |N(S)|=0<1=|S|.
\tag{7.2}
\]

This raw residual graph is deliberately over-permissive: it ignores q1,
residence, and already-used-colour restrictions on completion edges.
Therefore (7.2) is an unconditional perfect-matching obstruction for this
fixed bank.  If one retains the oriented terminal/initial bipartition, it is
also the singleton Hall obstruction.

The obstruction does **not** rule out a different four-orbit quota bank,
additional cut orbits, replacing one of the four service seams, or a
nonseparated interacting packet.  Nor has this bank been asserted to
preserve q1 collateral.

## 8. Complete raw endpoint screen for four disjoint quota orbits

The entire target-induced class of four mutually disjoint quota/service
orbits has now been screened.  In this screened class, the eight cut-port
orbits are required to be mutually distinct.  The four primary seam orbits
therefore leave 120 physical halfports and require sixty completion edges,
or four orbit-equivalents; those completion edges are allowed to be
noninvariant.  Its exact scope is:

1. single-seam records induced by the seven representatives (1.1);
2. closure under full `C_15` rotation and reversal;
3. positive collar on every rotated primary seam;
4. four quota records with eight mutually distinct cut-port orbits whose
   service supports cover all seven rows;
5. mutual cyclic source-cut gap at least four; and
6. completion using arbitrary raw Johnson edges between the 120 residual
   degree-one endpoints.

The fail-closed enumeration reports

```text
raw target-induced candidates       72,000
canonical candidates                23,292
valid full-orbit records                612
DFS nodes                       28,517,607
unique admissible four-banks            524
banks with no isolated endpoint            3
raw-perfect four-banks                       3
```

The run finished before every time, memory, and bank cap and records
`complete=true`.  Edmonds matching was called on the three isolated-free
residual graphs and returned size sixty in all three.  Thus raw endpoint
matching is **not** a universal obstruction in this four-quota class.

A separately written auditor reconstructed each saved certificate as a
simple spanning degree-two Johnson factor, rechecked all four primary seam
orbits, and replayed positive runs and every natural fixed-width shadow.  The
exact replays are:

| candidate records | cut gap | components | residence defects | q1 holes `(lower,upper)` | q2 holes `(lower,upper)` | q3 holes `(lower,upper)` |
|---|---:|---:|---:|---:|---:|---:|
| `224,346,436,602` | 17 | 44 | 75 | `(75,115)` | `(16,105)` | `(0,15)` |
| `346,436,511,602` | 15 | 24 | 90 | `(45,115)` | `(16,135)` | `(0,15)` |
| `346,436,541,602` | 15 | 23 | 90 | `(45,115)` | `(1,135)` | `(0,15)` |

Each also has fifteen fixed upper-q4 holes; deeper fixed rows through q7 are
complete.  None of the three saved completions is q1-complete,
residence-four, or fixed-shadow complete.  Candidate 2 is closest only on
the lower-q2 coordinate, with one remaining lower hole; it still has the
large upper and q1 debts shown in the table.  Arbitrary-width upper replay
was not certified by this auditor and remains mandatory before any carrier
claim.

The independent auditor replayed the three saved matchings; it did not
independently re-enumerate the 524 banks.  Failure of one saved matching
alone would not prove that every raw perfect matching in the same residual
graph fails.  Residence can, however, be decided on the complete residual
edge sets, as follows.

### Theorem 8.1 (residence-safe completion obstruction)

For each of the three raw-perfect banks, filter every raw residual Johnson
edge by the exact length-four inward collar of its two retained segments.
The raw edge counts `105,105,120` all reduce to the same fifteen pairwise
disjoint safe edges.  In every case the safe residual graph has

\[
120\text{ vertices},\qquad 15\text{ edges},\qquad
0^{90}1^{30}\text{ as its degree histogram}.
\tag{8.1}
\]

Its matching number is therefore exactly fifteen, whereas a completion
requires sixty edges.  In particular, ninety endpoints are isolated, giving
explicit singleton perfect-matching obstructions (and singleton Hall
obstructions whenever the oriented port bipartition is retained).  Hence
none of the three banks has any residence-four endpoint completion.

### Proof

The independent audit reconstructs the retained segment incident to every
one of the 120 halfports.  It tests all raw Johnson pairs and applies the
same exact inward positive-run collar used for the primary records.  The
complete retained edge list is common to all three banks and has fifteen
pairwise disjoint entries.  Thus every matching has size at most fifteen,
and taking all entries attains fifteen.  Since sixty are required, no safe
perfect matching exists.  \(\square\)

Combining the exhaustive raw screen with Theorem 8.1 proves a residence no-go
for the declared four-quota-orbit/eight-disjoint-cut class.  It does not
exclude four service columns sharing cut ports, a bank with additional cut
orbits, or a packet that changes the retained segment interiors.

## 9. Proved boundary and remaining gate

The corrected seven-row conclusion is:

1. one-cut-per-component fixed-depth repair is impossible (`84<93`);
2. arbitrary-upper one-cut repair pays at least nine width-five masks, or
   at least fifteen under full rotation symmetry;
3. every separated invariant fixed-q2/q3 repair needs at least four seam
   orbits (`60` physical seams), including at least two BB seam orbits;
4. four service orbits are locally attainable with positive collars and
   gap twelve;
5. the first exhibited attainment fails raw endpoint matching, but a complete
   screen finds exactly three other disjoint four-quota banks with raw
   perfect matchings;
6. all residual edges in those three banks admit an exact collar audit, and
   none has a residence-safe perfect matching (matching number `15<60`);
7. the saved raw completion for each also fails q1 and fixed-shadow replay;
   arbitrary-width replay was not reached.

The exact missing finite theorem is consequently not provider supply.  It
is one of the following:

- use shared cut ports, extra cut/quota orbits, or a different retained-
  segment decomposition so that the residence-safe residual graph can have
  a perfect matching, with signed q1/all-depth constraints imposed during
  that matching; or
- construct an interacting packet for which multi-seam accepting paths add
  services unavailable in the separated single-seam columns, and audit its
  full assembled chronology.

No claim that the three banks exhaust nonseparated/interacting packets is
made.  No global infeasibility, all-depth completion, exact compiler
completion, or `k=16` word is claimed.

## 10. Replayable artifacts

```text
scratch/run_ad_k16_len8_seam_census_all_max_examples_20260730.py
SHA-256 3ada0fdfeb920ca7f583db8ee82f9e4aeabd8dc0538e9b5946a62c79b973c60e

scratch/ad_k16_len8_seam_provider_widths_allmax_20260730.audit.json
SHA-256 69ea0ee9841f62e4e1c8d7758cfb01bd1c5fffef7936e0c6c47bf4d8b59284c4

scratch/run_ad_k16_len8_seam_census_highhit_records_20260730.py
SHA-256 06d3e374c51424287c9d2d6915c56be1ee860f8d2192999674f4cfd0ca1608e9

scratch/ad_k16_len8_seam_provider_widths_highhit_20260730.audit.json
SHA-256 5841d9a10b439b55d09c6d3e23cb64afa760bc556f44461192b409c78c96bdf7

scratch/run_ad_k16_len8_endpoint_minimal_widths_20260730.py
SHA-256 97e38fdaee298d4c5e9024ff3ab2fddd820102654701fc2a1da2b2f8b118d382

scratch/ad_k16_len8_endpoint_minimal_widths_20260730.audit.json
SHA-256 d7d94fa425b7e41d1de3feadfba2a241eac07424c6a2c39051a084e178a05937

scratch/audit_k16_len8_residual_orbit_seam_capacity_20260730.py
SHA-256 01f3b6aef060f5398ced0f8f4eb1be915a408fada62887e4ea3d0761a8e1e17e

scratch/k16_len8_residual_orbit_seam_capacity_20260730.audit.json
SHA-256 e8f0e8f236f567c2e223cd5186dcb79ab56f5be66eec2017c23962c2182ee47e

scratch/audit_k16_len8_four_orbit_quota_bank_20260730.py
SHA-256 e484e8eec8b2f30f7b8afadd7b92074b6c85d5f8c26efdec3bbc29b0a5faf628

scratch/k16_len8_four_orbit_quota_bank_20260730.audit.json
SHA-256 93303978cbe3eefb09ea7bc4107b05b074572d8df2951049dfad5bc575859160

scratch/search_k16_len8_target_quota_bank_endpoint_matching_20260730.cpp
SHA-256 0e602da4a0bc28ac94211096be7d757f777cce48dbe4206bd29fb8d0d578930b

scratch/k16_len8_target_quota_bank_endpoint_matching_20260730.audit.json
SHA-256 a582a55cde1469dd34addf7b49ffe16e21c1bbe6831976921f0030a415e7a49a

scratch/audit_k16_len8_target_quota_bank_endpoint_matching_20260730.py
SHA-256 70d37684e5fe71649542a86b6eb7a99bb6e30fff819d1cf54d07e48f04990410

scratch/k16_len8_target_quota_bank_endpoint_matching_20260730.independent.audit.json
SHA-256 57797eba91aa93b076e980a336aa7d25b4595b1ba5605542c3977d242fcfc4dd

scratch/audit_k16_len8_raw_perfect_banks_residence_safe_completion_20260730.py
SHA-256 0de5286f2a1dd93650c5b8226495f014a431b80119f6181d86aa572b38d44870

scratch/k16_len8_raw_perfect_banks_residence_safe_completion_20260730.audit.json
SHA-256 22929149f35bfe8350cf21edccaef66caa62b2a7942ad3ab30c7b5208ce3b323
```

The four-orbit lower-bound checker and the explicit quota-bank/Hall checker
were independently audited against the authenticated factor and complete
high-hit arrays.  The complete raw-screen source received a separate
adversarial logic audit, and all three saved certificates were independently
replayed.  The final residence-safe residual-edge audit also received an
independent proof review.  All passed within the scopes stated above.
