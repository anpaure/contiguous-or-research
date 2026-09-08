# The connected `K17` OPTIMAL28 quotient: exact deep-shadow and common-cap cuts

Date: 2026-07-31  
Lane: R  
Status: exact fixed-carrier audit and exact cut formulation; the frozen
chronology fails before common-cap Hall, and no `K17` word is claimed

## 0. Verdict

The connected residual assignment

```text
scratch/ad_k17_opt28_residual_connected_bflow_20260731.json
```

really closes the topology gate.  It expands to one Johnson cycle through
all `24310` rank-nine owners, and its `24310` adjacent intersections are
exactly all rank-eight colours.  The OPTIMAL28 marked bank is one contiguous
arc of `4108` owners; its complementary arc has `20202` owners.

The canonical two-bank zipper is much sharper than the raw cycle, but is
still not a compiler.  It has

```text
rank-nine marked rows                         4108
distinct rank-eight facet rows               20203
total D2 rows                                 24311
maximal-envelope positions                   24313
scalar short-cell slack                        3293.
```

Every maximal envelope position is nonempty.  Nevertheless, `3759`
row-bit obligations have no envelope host, so `3568` exact `D2` replay
equations fail.  All failures lie on the complementary facet shore.  One
literal certificate is

```text
row i=4127:       Z_i = 0x0348f
E_i,E_{i+1},E_{i+2} = 0x02487,0x03087,0x03087
their union          = 0x03487,
```

which omits bit `3` of `Z_i`.  Thus no nonempty physical word has this
fixed `D2` row, independently of any target matching.

The complete long-interval upper audit of this same row is

| target rank | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| holes | 1900 | 911 | 128 | 0 | 0 | 0 | 0 | 0 |

Hence topology, middle ownership, and lower `q1` are closed on this
artifact.  The fixed row has nonempty interval-provider sets at ranks `13`
through `17`; because the row is not invertible, this is conditional
provider support, not a physical word.  Its exact live repair requires regenerated
complementary component, partial-macro, or broader nonflat actuator columns
which preserve the marked bank and the two quotient sockets while repairing:

1. global `D2` inversion/residence;
2. the first three upper ranks while preserving or re-auditing ranks
   `13` through `17`; and
3. one common cap on the resulting chronology.

The direct radius-two occurrence path is now only a fallback.

## 1. The one-cycle quotient is exact

Let

\[
 \mathcal T={ [15]\choose8},\qquad
 \mathcal U={ [15]\choose9}.
\]

The fixed macro-plus-packet forest has

\[
 |\mathcal T|=6435,\qquad |E_F|=1430+133=1563,\qquad
 c(F)=4872.                                             \tag{1.1}
\]

Its residual port demand has profile

\[
             0^{691}1^{1744}2^{4000}                   \tag{1.2}
\]

and total `9744`.  The saved assignment uses each of the remaining `4872`
old-`U` owners once, chooses two distinct literal facets of each owner, and
meets (1.2) exactly.  After contracting `F`, the selected graph has `4872`
vertices and `4872` edges, degree two everywhere, no loop, and one connected
component.  It is therefore one cycle.  No residual rectangle was needed:
the selected max-flow attempt was already connected.

Uncontracting gives one cycle on all `6435` rank-eight ports.  Literal
expansion gives

\[
 \{T_i:0\le i<24310\}={ [17]\choose9},
 \qquad
 \{T_i\cap T_{i+1}:0\le i<24310\}={ [17]\choose8}.    \tag{1.3}
\]

Indices in (1.3) are cyclic.  Thus middle ownership and lower `q1` are
bijective.

The immutable marked object path has `304` edges and `305` ports.  Exactly
two residual objects cross its cut:

\[
\begin{array}{c|c}
U&\text{rank-eight ports}\\ \hline
22778&(6394,22762),\\
18294&(18230,18290).
\end{array}                                            \tag{1.4}
\]

Consequently its `4108` expanded owners form one strict cyclic interval.
The complementary interval has `6131` objects and `20202` owners.  At
depth `q`, exactly `2q` cyclic starts cross the two bank boundaries.  These
are the complete quotient seam halos; all other depth-`q` owner windows lie
inside one bank.

## 2. The forced two-bank zipper

Rotate and orient (1.3) so that

\[
       P=(P_1,\ldots,P_a),\quad a=4108,
       \qquad Q=(Q_1,\ldots,Q_b),\quad b=20202.        \tag{2.1}
\]

Put

\[
\begin{aligned}
 F_0&=P_a\cap Q_1,\\
 F_j&=Q_j\cap Q_{j+1}\quad(1\le j<b),\\
 F_b&=Q_b\cap P_1,
\end{aligned}                                        \tag{2.2}
\]

and define the linear row

\[
       Z=(P_1,\ldots,P_a,F_0,\ldots,F_b).             \tag{2.3}
\]

The `20203` facets in (2.2) are distinct.  Moreover the `4107` internal
marked turns \(P_i\cap P_{i+1}\) and the facets in (2.2) partition
all `24310` rank-eight colours.  Thus (2.3) has length `24311`, rank profile

\[
                         9^{4108}8^{20203},           \tag{2.4}
\]

and every adjacent union has rank at least nine.

For a prospective physical word `A` of length `24313`, define the maximal
envelope

\[
 E_p=\bigcap_{\max(0,p-2)\le i\le\min(p,24310)}Z_i.
                                                               \tag{2.5}
\]

### Theorem 2.1 (exact inversion cut)

There is a nonempty word `A` with `D^2 A=Z` if and only if

\[
 E_p\ne\varnothing\quad(0\le p<24313)                \tag{2.6}
\]

and

\[
                 E_i\cup E_{i+1}\cup E_{i+2}=Z_i
                 \quad(0\le i<24311).                \tag{2.7}
\]

Equivalently, for every bit `x in Z_i`, at least one of the three positions
`p=i,i+1,i+2` must have `x in E_p`.  Each failed pair `(i,x)` is therefore
an exact row-bit host cut.

#### Proof

Any realizing letter `A_p` is contained in every `Z_i` whose three-window
contains `p`, hence \(A_p\subseteq E_p\).  Conditions (2.6)--(2.7) are
necessary.  Conversely, `A=E` realizes `Z` when they hold.  The bit-host
form is simply (2.7) coordinate by coordinate.  \(\square\)

For (2.3), all `24313` rows (2.6) pass, but `3759` bit-host cuts fail,
distributed over `3568` rows.  There are zero failures in the marked
shore and all `3759` in the facet shore.  Its internal short-run form is

\[
                    1^{1025}2^{1367},                \tag{2.8}
\]

so `2392` strict positive runs are shorter than three.  The first failed
row is the certificate in Section 0.  This proves fixed-row impossibility
before Hall, not a no-go for changing `Q` or for a genuinely different
schedule.

### 2.2 The fixed-component repair face is empty

The `4871` fixed complementary forest components contain `724` strict
component-internal owner runs of length below four:

\[
                       2^{320}3^{404},               \tag{2.9}
\]

spread over `257` components.  Facetization shortens each run by one, so it
creates a strict run of length one or two wholly inside the corresponding
facet block.  Component reversal, component ordering, and residual
old-`U` re-pairing alter only the outside seams and cannot touch either
internal zero boundary.  Therefore this entire fixed-component face fails
Theorem 2.1.

If the marked bank must stay at exactly `4108` owners and variants are
component-local, all `257` defective components need a nonidentity option.
If whole length-three-only components may instead migrate into an enlarged
owner bank, the exact optimistic slot calculation still forces at least
`106` component variants.  These floors do not apply to partial-macro or
multi-component actuators, and `724` is not a move-count lower bound; they
identify why another residual matching is not a live repair.

## 3. Exact deep-shadow cuts

### 3.1 Physical interval providers

For any row `Z` and upper target `Y`, put

\[
 \mathcal I_Z(Y)=\left\{[s,t]:
       \bigcup_{i=s}^{t}Z_i=Y\right\}.               \tag{3.1}
\]

### Theorem 3.1 (long-provider criterion)

Suppose `D^2 A=Z`.  A target `Y` has a physical witness of length at least
three if and only if

\[
                         \mathcal I_Z(Y)\ne\varnothing. \tag{3.2}
\]

Once such a witness exists, every later cap which still realizes `Z`
preserves it.

#### Proof

For every physical interval `[s,t+2]` of length at least three,

\[
       \bigcup_{p=s}^{t+2}A_p
       =\bigcup_{i=s}^{t}Z_i.                        \tag{3.3}
\]

The three-windows on the right cover precisely the positions on the left.
This proves both directions and cap invariance.  \(\square\)

Thus the exact fixed-row deep-shadow cut for `Y` is simply

\[
                 \sum_{I\in\mathcal I_Z(Y)}h_{Y,I}\ge1.\tag{3.4}
\]

For a fixed chronology the variables in (3.4) are only witness selectors;
if the index set is empty, (3.4) is the literal contradiction `0 >= 1`.
For a variable rethread, a valid interval column must carry both exact
conditions: no row in it contains a blocker outside `Y`, and its rows cover
every bit of `Y`.  A width-only or fixed-depth proxy is insufficient.

The exhaustive linear audit of (2.3) gives the table in Section 0.  Three
explicit empty-provider cuts are

\[
 \mathcal I_Z(\mathtt{0x007bf})=
 \mathcal I_Z(\mathtt{0x007ff})=
 \mathcal I_Z(\mathtt{0x03efe})=\varnothing,         \tag{3.5}
\]

at ranks `10`, `11`, and `12`, respectively.  All targets of ranks `13`
through `17` pass (3.2).

### 3.2 Integral quotient partition cuts

There is also an exact cut system directly on an integral selected owner
factor.  Let `x_e` be its selected Johnson edges.  For an upper target `Y`,
put

\[
             V_Y=\{T\in{[17]\choose9}:T\subseteq Y\}.\tag{3.6}
\]

Call a partition `Pi` of `V_Y` **bad** if every block `B in Pi` has

\[
                    \bigcup_{T\in B}T\subsetneq Y.   \tag{3.7}
\]

### Theorem 3.2 (upper owner-block partition theorem)

A simple spanning owner path or cycle which uses every rank-nine owner
exactly once has a consecutive owner block with union `Y` if and only if,
for every bad partition `Pi`,

\[
 \sum_{\substack{e=ST:\ S,T\in V_Y\\
                  S,T\text{ in different blocks of }\Pi}}x_e\ge1.
                                                               \tag{3.8}
\]

For an opened cycle replace the deleted opening edge by zero in (3.8).

#### Proof

The maximal consecutive blocks of selected owners contained in `Y` are the
components of the selected graph induced by `V_Y`.  If one component has
union `Y`, it cannot lie within one block of a bad partition; its
connectedness supplies a selected crossing edge.  Conversely, if every
component has proper union, partition `V_Y` into those components.  This is
a bad partition with no selected crossing edge.  \(\square\)

At rank ten, two distinct rank-nine subsets of `Y` already have union `Y`,
so (3.8) reduces to the ordinary upper-`q1` edge row

\[
                   x(E(V_Y))\ge1.                   \tag{3.9}
\]

There is a dual lower owner-block theorem: replace \(T\subseteq Y\) by
\(L\subseteq T\), block union by block intersection, and require each bad
block to have intersection strictly larger than `L`.

Equations (3.8)--(3.9) certify owner-block shadows.  The physical compiler
uses all intervals of the mixed-rank row (2.3), so (3.1)--(3.4), not one
fixed owner depth, are authoritative for literal upper coverage.

## 4. Deep holes and the common cap share the short-cell budget

Let `d_8(Z)` be the number of distinct rank-eight rows in a valid `D2` row,
and let

\[
 H^+(Z)=\{Y:|Y|\ge9,\ \mathcal I_Z(Y)=\varnothing\}.\tag{4.1}
\]

Every lower target not among the direct rank-eight rows must use a singleton
or adjacent-pair physical cell.  By Theorem 3.1 the same is true of every
target in `H^+(Z)`.  These families are rank-disjoint.  Since a length
`24313` word has exactly

\[
                       24313+24312=48625             \tag{4.2}
\]

singleton/pair cells, any completion obeys the sharp scalar cut

\[
 65535-d_8(Z)+|H^+(Z)|+s_{\rm aux}\le48625,          \tag{4.3}
\]

where `s_aux` counts distinct short intervals made unavailable and not
simultaneously witnessing a charged target in these two families.
Equivalently,

\[
             d_8(Z)-|H^+(Z)|-s_{\rm aux}\ge16910.   \tag{4.4}
\]

For a zipper with `a` distinct rank-nine rows and all other rows distinct
of rank eight, (4.3) becomes

\[
                   a+|H^+(Z)|+s_{\rm aux}\le7401.   \tag{4.5}
\]

The current row has

\[
 a=4108,\qquad |H^+(Z)|=1900+911+128=2939,          \tag{4.6}
\]

so charging the upper holes to short cells would leave only

\[
                       7401-4108-2939=354            \tag{4.7}
\]

units of scalar reserve.  This is necessary capacity, not Hall and not a
common-cap construction.  Repairing one long upper provider returns one
unit of reserve only when `d_8`, `s_aux`, and every other member of `H^+`
remain unchanged.

## 5. Exact common-cap cuts after inversion

Assume now that a repaired `Z` passes Theorem 2.1.  Fix all provider cells
and a jointly cap-compatible family of singleton/pair prepins; remove every
prepin-occupied cell from the unused-cell set (equivalently, include it in
the cell-capacity rows).  Let `B_p` be the resulting maximal envelope.  The
exact short-target family is

\[
 \mathcal R^*(Z)=
 \left(\mathcal L^-\setminus D_8(Z)\right)\mathbin{\dot\cup}H^+(Z),
                                                               \tag{5.1}
\]

where `D_8(Z)` is the set of direct rank-eight rows.  For `S in R^*(Z)` and
an unused singleton/pair cell `J`, make a candidate `e=(S,J)` exactly when

\[
 B_p\cap S\ne\varnothing\quad(p\in J),
 \qquad
 S\subseteq\bigcup_{p\in J}B_p.                    \tag{5.2}
\]

Let `y_e` be binary.

If a fixed prepin already discharges a target in (5.1), delete that target
from `R^*(Z)` together with its occupied cell before forming candidates.
Thus `R^*(Z)` below denotes the still-unassigned residual family.

### Theorem 5.1 (matching plus rank-three clutter)

With `Z`, the provider positions, and the jointly compatible prepins fixed,
and with every variable cell a singleton or adjacent pair, one common
nonempty cap realizes every target in (5.1), while preserving `Z` and every
fixed prepin, if and only if

\[
 \sum_{e\in D_S}y_e=1\quad(S\in\mathcal R^*(Z)),
 \qquad
 \sum_{e:J(e)=J}y_e\le1\quad(J),                    \tag{5.3}
\]

and, for every inclusion-minimal cap obstruction `F`,

\[
                         \sum_{e\in F}y_e\le|F|-1.  \tag{5.4}
\]

The obstruction families are exactly:

1. two candidates using one cell;
2. selected labels with empty intersection at one position;
3. selected labels deleting every host of a required `D2` row bit;
4. the analogous deletion of a fixed-prepin bit; and
5. one selected target anchor plus selected labels deleting every host of
   one of its required bits.

Every minimal `F` has size at most three, and rank three is sharp.

#### Proof

For a selection `M`, intersect `B_p` with every selected target whose cell
contains `p`.  This coordinatewise maximal cap is nonempty and replays all
declared rows exactly if and only if none of the five failures occurs.
Only the singleton, left pair, and right pair meet a position, so a minimal
position or row-bit blocker has size at most three.  Conversely every failed
cap equation contains an inclusion-minimal obstruction of the listed type.
Target rank is irrelevant, so the proof applies unchanged to upper masks in
`H^+(Z)`.  \(\square\)

The fixed-prepin compatibility hypothesis excludes a zero-variable
obstruction already present before `y` is chosen.

Ordinary Hall for the candidate graph is necessary but not sufficient.
A permanent-bit and fixed-host pruning can make every saturating matching
cap-safe, in which case Hall becomes sufficient; no such guarded subgraph
has been proved for the present chronology.

The exact rank-three statement does not extend unchanged to variable socket
or provider positions; those choices must remain in the outer rethread
columns, where rank-four obstructions can occur.

The current row never reaches (5.3)--(5.4): the row-bit certificate in
Section 2 already contradicts `D^2` replay.

## 6. Exact post-connectivity Benders order

Let `R` range over regenerated complementary-component, partial-macro, or
compound rethreads which preserve:

* the `4108`-owner marked word and its internal order;
* all `24310` owner and lower-`q1` labels;
* the one-cycle quotient and the two exported socket incidences; and
* every protected fixed witness declared immutable.

For each `R`, form the literal row `Z(R)`.  Within this protected class, a
literal optimal-length completion exists if and only if there are `R` and
`y` satisfying, in order:

1. the inversion/row-bit cuts (2.6)--(2.7);
2. every long-provider cut (3.4), or else the corresponding short target is
   included in (5.1);
3. the scalar cut (4.3); and
4. the exact common-cap system (5.3)--(5.4).

This gives a lossless separation scheme:

```text
candidate rethread
    -> failed row-bit host cut
    -> failed upper interval-provider cut
    -> scalar short-cell cut
    -> Hall cut or bad-pair/bad-triple common-cap cut.
```

The connected residual `b`-flow has already discharged the degree and
quotient-cut subproblems.  Merely reordering, reversing, or re-pairing its
fixed complement is ruled out by (2.9).  Direct radius-two occurrence
changes remain a fallback source of genuine variant columns, not a
prerequisite for topology.

## 7. Frozen evidence and scope

```text
scratch/ad_k17_opt28_residual_connected_bflow_20260731.json
SHA-256 b3cbb0663409463cb24a2ed78db154cc88a042b633e979cba3506ba74e610ef6
payload a117a304f277a7746405814786fd3f593dffe5073443431582eb711641e7319a

scratch/ad_k17_opt28_residual_connected_bflow_20260731.audit.json
SHA-256 95e8b27426d9ac62ccbe490a55c2a1e256e63faa1bc561a5d5a0462380870cfd

scratch/k17_opt28_connected_owner_cycle_20260731.word
SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa

scratch/k17_opt28_connected_owner_cycle_20260731.audit.json
SHA-256 f28924a629a6e858571119538639adf3ecbd4d186c1014a475e353fe5b719280
payload 6988b37a414a516e4645f81b1dac87618c1949bc636a1190462c5f8520639d7a

scratch/ad_k17_opt28_twobank_d2_row_20260731.zrow
SHA-256 18675acb0083aa7fea8e1505f871cc70b23a9261e6f59662cb9df87ca703a211

scratch/ad_k17_opt28_twobank_d2_row_20260731.audit.json
SHA-256 81f0e403367ee0e32c0ac63404cebd2e87a3a2a9602475b01b3a3927c4c9cf20
payload 591ef216c6c4d818e604ccad9d149ab6ab66c0fa6a124a3d8bc5382c2185726d

scratch/audit_r_k17_opt28_onecycle_deep_common_cuts_20260731.py
SHA-256 78cfed96643fa13041eb9adb0d58c78e542ed4a15fb8381fd4eaa578f638b39f

scratch/r_k17_opt28_onecycle_deep_common_cuts_20260731.audit.json
SHA-256 38b1a1fe8ef845501eb8f3c2d69f8606027323b0ac08841c46fbc40f92402853
payload 71f9bd3a76c61978792f5e06e0a79756a5e85e5ab9a8ca3fe99a9b5ab1142b2f

MATH_THEOREM_THREAD_D_K17_OPT28_COMPONENT_CAP_PHYSICALIZATION_GATE_20260731.md
SHA-256 e1f56cd564304452a40beaaa669ab0ae1dd4724232639254f9c5792a4955980e

scratch/threadD_k17_opt28_component_cap_floor_20260731.audit.json
SHA-256 48bc1e3302e8b05b7d320f78454e63a8bd71268358655a503c2a9b525d25eeda
payload 98753c506595f0b0cf3978d03b315b08b9b6c31d9ab9da40e94cf6033e0f8b3e
```

The independent R audit authenticates the literal cycle, reconstructs the
marked/facet zipper, scans all `618182` relevant linear intervals, gives the
complete physical upper table, the owner fixed-depth diagnostic table, and
the literal row-bit witness above.

The `OPTIMAL28` objective value itself is solver scope; existence of the
saved path and all statements about the displayed factor are independently
replayed.  Nothing here excludes a different connected residual assignment,
a complementary rethread, another packet path, or a nonflat compiler.  No
claim about `nu(17)` follows.
