# K16 nested Hall-24 DM exits: exact rematch bases and the support-six gate

Date: 2026-07-31  
Status: **PASS exact rematch-basis theorem; PASS scoped occurrence no-go.**
No K16 word and no unrestricted Hall no-go is claimed.

## 1. Scope and verdict

This note continues the three physical defect-one exits in the four
authenticated nested-forward Hall-24 carriers:

| carrier | `(outer,inner)` | word SHA-256 | Hall SHA-256 |
|---|---:|---|---|
| pass33 | `(16,9)` | `2dbb84bc6467047d99019e58b6a33072cbca8f0bc6e62c451954603611fcf2ec` | `73a8538d97fe38a94cba661f8d67e7d20282302c6f97c87df61eda48cc584e8f` |
| pass46 | `(16,13)` | `bf3ee02110f70c168dc9863e1c8258cc54debfa408dd4c97fe5b57c6a4116754` | `fce8c051d7e7d0f3ce7aaf035d6d0d3c0207614c25b1f8b902d5502669a127a8` |
| pass35 | `(18,9)` | `42420e0eea7102a07227b25e49663a127f89219b8c41cb18ee7de699385d9b04` | `b6ba25add99a7d49913f4c5914696970a19574b266a9d2ca9c8ba13542e9ca42` |
| pass55 | `(18,15)` | `e1166c6ae5f6c671c779bfb9f692fa8332aa7b9978cfcd93671b64244c5f1f69` | `a60e4d99a31f6ec73b7e3a973e7ff7e83c831f133a05085f092aa072b99fa65e` |

Every parent is middle-exact, arbitrary-upper complete, has capacity 32063,
and has lower matching `26308/26332`.  Each has the unique physical provider

```text
8000--J31761,  J31761=[12720,12721).
```

The three common physical `4e70` exits are

| port | cell | defect | old mate | shortest augmenting path |
|---|---|---:|---|---|
| A | `J19536=[6607,6609)` | `0010` | `ce40` | `4e70-J19536-ce40-J21197-c640-J27739` |
| B | `J19538=[6608,6610)` | `0040` | `ce30` | `4e70-J19538-ce30-J21028-8a30-J29401` |
| C | `J31749=[12714,12715)` | `0400` | `4a70` | `4e70-J31749-4a70-J3007-0a70-J14208` |

The new conclusions are:

1. After forcing one named `4e70` edge and the existing `8000` edge, the
   exact matching rank under every possible loss subset from its dependency
   packet is a closed form.  The packet has a unique protected core; every
   noncore old matched incidence may be lost simultaneously.
2. Lane A's complete 2,732-row dependency-disjoint packet atlas realizes none
   of the three exits.  Its three all-upper rows are disjoint from every exit
   closure.
3. Across all four parents, the complete class of arbitrary occurrence
   permutations of actual support at most six inside the 22-row union of the
   three exit closures and the `8000` closure has no middle-exact,
   arbitrary-upper-complete row with a named `4e70` port and an `8000`
   provider.  The known six-edit alpha is the sole named-port survivor and
   still owes `4e79`.

The sharp remaining route is the exit-rooted occurrence cycle beginning with
the unique relaxed import `4e72@280 -> row6606` in Section 7.  Support at
least seven, changed-flat schedules, and nonzero-target DM exits are also
outside the finite no-go.

## 2. Forced residual matching is the exact algebra

Let `G=(L,R,E)` be one parent compatibility graph.  For a port `J`, put

```text
e_J = (4e70,J),       p = (8000,31761),
H_J = G + e_J.
```

For any physical edit with incidence losses `D` and gains `A`, require both
named incidences to exist and define

\[
 \mu_J(D,A)=2+\nu\!\left(
 ((H_J-D)+A)-\{4e70,8000,J,31761\}\right).             \tag{2.1}
\]

The notation means delete the two forced left vertices and two forced right
vertices, compute an unrestricted maximum matching on the residual graph,
then insert the two forced edges.  Therefore

\[
 \text{the edited graph has a matching of size at least }26309
 \text{ containing }e_J,p
 \quad\Longleftrightarrow\quad
 \mu_J(D,A)\ge26309.                                    \tag{2.2}
\]

This is the promised replacement for a frozen-path condition.  Relative to
any residual matching basis, orient unmatched incidences left-to-right and
matched incidences right-to-left.  If `t` basis incidences are broken, the
symmetric-difference theorem says that (2.2) is equivalent to an integral
unit-capacity exchange flow of value `t`: vertex-disjoint alternating paths
must route the newly free left endpoints to distinct free right endpoints in
the edited graph.  The retained-graph positive-cut test is precisely the
special case `t=0` with one new unmatched-left unit.  Once old incidences are
lost, survival of one displayed path remains sufficient but is no longer
necessary.

There are two different notions of “sacrifice” here.  Each displayed shortest
augmentation changes the matching assignment on exactly two old incidences
and inserts three assignments; it deletes **zero graph incidences**.  A
physical occurrence move can truly delete graph incidences, and those losses
must be judged by (2.1), not by comparing against one stored matching.

## 3. Exact dependency packets

For a physical position `x`, let `I(x)` be its incoming middle-row set.  For
a compiler cell `J`, let `R(J)` be the union of `I(x)` over positions of `J`.
The exact two-step profile dependency is

\[
 D(J)=R(J)\cup
 \bigcup_{r\in R(J)}\ \bigcup_{x=r}^{r+d(r)} I(x).       \tag{3.1}
\]

For the authenticated matching `M`, define

\[
 P_J(M)=\{(u,C)\in M:D(C)\cap D(J)\ne\varnothing\}.      \tag{3.2}
\]

Direct reconstruction gives

| port | `D(J)` | `|P_J(M)|` | eligible losses |
|---|---|---:|---:|
| A | rows `6603..6610` | 24 | 24 |
| B | rows `6604..6611` | 24 | 24 |
| C | rows `12710..12716` | 15 | 14 |

For C, the fifteenth overlap is the hypothesis-protected incidence
`p=8000--J31761`; it is never an eligible loss.  The packet identities can
vary with the authenticated parent matching, but the protected cores below
and every rank count are invariant across all four parents.

## 4. The exact all-subset loss theorem

For each port, let `K_J` be the following set of old matching incidences:

```text
K_19536 = {
  0a6e@19546, 866a@19532, 942b@19528,
  b829@19524, cc38@19540
}.

K_19538 = K_19536 union { c255@19552 }.

K_31749 = {
  4a2e@31758, 4a71@31748, 4c2e@31756, 4c38@31753,
  4c3c@31754, 4e38@31752, 8a4e@31762, fc10@31736
}.
```

### Theorem 4.1 (forced-port packet rank)

For every one of the four parents, every named port `J`, and every eligible
loss set `D` contained in `P_J(M)`, with `p` retained,

\[
 \boxed{\ \mu_J(D,\varnothing)=26309-|D\cap K_J|\ }.     \tag{4.1}
\]

In particular, matching at least 26309 survives exactly when

\[
 D\cap K_J=\varnothing.                                 \tag{4.2}
\]

Thus A has the exact split `5 protected + 19 simultaneously
sacrificable`, B has `6+18`, and C has the separately protected `8000` edge
plus `8 protected + 6 simultaneously sacrificable` among its other fourteen
packet incidences.

#### Proof

The audit first deletes every eligible packet incidence.  The forced ranks
are respectively

```text
A: 26304,    B: 26303,    C: 26301.
```

Deleting any one listed core incidence from the full graph lowers forced
rank to 26308; deleting any one noncore incidence leaves 26309.  Conversely,
deleting **all** noncore incidences simultaneously while retaining the core
still gives 26309.

The audit then exhausts every subset `S` of each small core twice: once with
no noncore losses and once with all noncore losses.  Both endpoint graphs
have rank `26309-|S|`.  Any intermediate choice of noncore losses lies
between those two graphs, so matching monotonicity forces the same rank.
This proves (4.1) for all `2^24`, `2^24`, and `2^14` eligible packet loss
sets without enumerating those large powersets.  The audited core tables are
the binomial rows `C(5,s)`, `C(6,s)`, and `C(8,s)` at rank `26309-s`.
\(\square\)

The pair histograms are an immediate visible check:

| port | rank26309 | rank26308 | rank26307 |
|---|---:|---:|---:|
| A | 171 | 95 | 10 |
| B | 153 | 108 | 15 |
| C | 15 | 48 | 28 |

These are exactly `C(n-|K|,2)`, `|K|(n-|K|)`, and `C(|K|,2)` for eligible
packet size `n`.

## 5. Why the actual alpha needs gains as well as tolerance

On every parent, the physical forward swap

```text
[6608,6611) <-> [12714,12717)
```

is middle-exact, creates the physical port `4e70--J19538`, retains
`8000--J31761`, and fully rematches to 26309, but owes upper mask `4e79`.
In occurrence-labelled descriptions the same new cell is labelled by source
rows `(12714,12715)`; that label must not be confused with its physical cell
id `J19538` after the swap.

The swap loses 216 old graph incidences, gains 136, and loses 12 incidences
of the stored 26,308-edge matching.  Of the two old assignments on the
shortest B path, `ce30@19538` is physically lost while `8a30@21028` remains.
Keeping only the losses and the two forced provider edges gives matching
26305; the full alpha graph gives 26309.  Hence the alpha is a concrete
warning against every unsound “number of frozen edges lost” marginal: its
new incidences participate essentially in the rematch.

## 6. Coordination with Lane A's packet atlas

The authenticated pass33 depth-seven compatibility-cycle table has 2,732
occurrence-integral rows.  Exact support intersection with (3.1) gives

```text
disjoint from A,B,C       2658
touches only C              74
touches A                    0
touches B                    0
touches multiple             0
```

Every C contact touches only row12713.  Port C needs bit `0400` in the
intersection of blockers rows12712 and12713, both of which initially lack
it.  Therefore editing row12713 alone cannot install C.  The three all-upper
packet rows 422/461/463 are disjoint from all three closures; their frozen
loss counts are 44/43/44 and their independently full-rematched deficiencies
are 30/34/31 as recorded in item2077.

The direct minimal-import audit was originally phrased with the old mate of
the port cell retained.  That is only a sufficient certificate for the
displayed frozen path; Theorem 4.1 shows that all three old-mate incidences
are noncore.  A separate rematch-aware replay therefore uses only a named
`4e70` edge, retained `8000`, the forced core, and a fresh full matching.  It
gives the corrected result:

* A is forced to edit row6606.  Among seventeen individually middle-exact
  remote imports, exactly `4e72@280 -> row6606` creates `4e70--J19536`.
  It loses the noncore old mate `ce40@J19536`, preserves every forced-core
  incidence and `8000`, and both ordinary and forced matching are 26309.
  It is not occurrence-integral: it duplicates `4e72`, removes `ce62`, and
  has literal coverage holes `{ce62,ce6a,ce6b}` (rank-eight `ce62` plus
  upper masks `ce6a,ce6b`).
* B is forced to edit row6608.  None of its twelve individually middle-exact
  remote imports creates the named port.
* C must edit both rows12712 and12713.  Seven safe `4e70`-superset sources
  give 42 ordered distinct pairs; none is even middle-exact, hence none
  creates the named port.
* All nonidentity occurrence permutations internal to A, B, and C are
  inexact: `40319+40319+5039=85677` tested and zero exact.

This is why the present search is exit-rooted rather than another run of the
halo-first packet lane.

## 7. Complete support-at-most-six occurrence gate

Take the 22 physical rows

```text
6603..6611  union  12710..12722.
```

This is exactly the union of the A/B/C dependencies and the protected
`8000` dependency.  The 22 row values and the four outside boundary values
are occurrence-distinct, so every permutation of this deck preserves the
three-flat depth schedule.  For actual support `s`, the census tests every
derangement on every `s`-subset.  Thus its formal count is

\[
 \binom{22}{s},!s,
\]

and the complete per-parent counts are

| support | formal | middle-exact | named port + `8000` | exact+upper |
|---:|---:|---:|---:|---:|
| 2 | 231 | 1 | 0 | 0 |
| 3 | 3,080 | 1 | 0 | 0 |
| 4 | 65,835 | 1 | 0 | 0 |
| 5 | 1,158,696 | 0 | 0 | 0 |
| 6 | 19,772,445 | 3 | 1 | 0 |

The totals are 21,000,287 rows per parent and 84,001,148 across the four
parents.  The exact rows are identical as positional permutations in all
four carriers.  The unique named-port row is the known six-edit alpha

```text
positions    6608,6609,6610,12714,12715,12716
source map   3,4,5,0,1,2,
```

which retains the original physical `8000` cell and has the sole upper hole
`4e79`.  Hence this entire support-at-most-six class contains no exact,
all-upper Hall-below-24 carrier.  Since no row reaches the exact+upper gate,
there is no candidate requiring a final Hall replay; the alpha full-Hall
control remains 26309 as established independently above.

The earlier 19 paired-old-mate templates are therefore **not** the final
acceptance gate.  The sharp next family is the occurrence-labelled cycle
rooted at

```text
4e72 occurrence 280 -> physical row6606,
displaced value ce62,
literal debts ce62, ce6a and ce6b.
```

It must close both occurrence vacancies through the single-row compatibility
relation, repair both upper debts, retain `8000`, and either avoid the five A
core incidences or pass a fresh full forced rematch.  This root is structurally
different from Lane A's old `3846->4653` halo-first packet.  B and C require a
larger interacting import kernel.  Merely increasing the old halo-first
packet depth cannot address these proved local blockers.

The direct two-cycle `280<->6606` is middle-inexact at row280 because it loses
that row's `8000` carrier.  A complete one-intermediate dependency-disjoint
three-cycle check under the same protected-source rules also has zero exact
closures.  Thus the seven A one-local-compensator templates are the next
interacting layer after this singleton root; the corrected 19-template layer
remains valid with old-mate survival removed from its acceptance predicate.

## 8. Exact artifacts

Primary forced-port/DM audit:

```text
scratch/audit_l_k16_nested_forced_port_dm_loss_basis_20260731.py
  SHA 9cd554a9f789a0a7a3c1647c6a687d9db6319161b57c833e6c5c4d29e8d3a6b5
scratch/l_k16_nested_forced_port_dm_loss_basis_20260731.audit.json
  SHA d4ae1fd8b826a2741f80a67a618e2e9d834567e6e26819c39837d7ae7aa0de9a
  payload ba4af2bca6916e99e0f72ae29578d4b01dfb2910aa70138542c1d08286c7a040
  normalized table ff57c246646e7c80964ce8e0c9ffd75dc70cceb3e2081aa5491975b54a416f17
```

Independent forced-residual implementation:

```text
scratch/audit_k16_nested_dm_exit_rematch_basis_20260731.py
  SHA 6b764bbad5af293fb7660dd26129bd554906da099be6dd058505c8f2388df415
scratch/k16_nested_dm_exit_rematch_basis_20260731.audit.json
  SHA 558b494a17f02682a5dc4cc131b880af437c5e680c8965235f00866bb42420c8
  payload e5002c54812243ca305a2c4704d3a3d91bcc67934fe3e83e6b4eca0e5bc86f67
```

Lane A packet/exit intersection audit:

```text
MATH_AUDIT_K16_PASS33_PACKET_EXIT_CLOSURE_DISJOINTNESS_20260731.md
  SHA fde6f2c28be3c303db648dc5fb4da3d494f95647c34372bb8d623d107c1d9a35
scratch/audit_k16_pass33_packet_exit_closure_overlap_20260731.py
  SHA b5c2afc3d4f2d80b9fccc9d3a8f7740f066e2787186c7e3a63dbe01ee3bbee3a
scratch/k16_pass33_packet_exit_closure_overlap_20260731.audit.json
  SHA b9fceeacd9fff8b36f837ddce4bf7cb3232b77836b28a820f82baa5d6c406ef0
  payload 8aadc9c0099b2a2af7ce46cd562a1bba6b326629187e53edfd2fcd6102cbb1c6
```

Rematch-aware relaxed-import audit:

```text
scratch/audit_k16_pass33_dm_exit_relaxed_import_roots_20260731.py
  SHA 04166c7b5a530991cc3291521de3fb3b02f7e051306829f4cbc411380d4df0fe
scratch/k16_pass33_dm_exit_relaxed_import_roots_20260731.audit.json
  SHA c8f87f0b2dfc735e058032f8d51725f4672a6777512fcaa7f5a427de545376b4
  payload 45aec1e7317026ba8b179fda9f15b3c5ca17c9dc00acea90440e9cef06147d91
```

Primary rematch-aware addendum, including the two-/three-cycle closure gate:

```text
MATH_AUDIT_K16_PASS33_MINIMAL_IMPORT_REMATCH_ADDENDUM_20260731.md
  SHA 5d97a9ac0e252ce989a577f4338f5e34cb329e27f467efcab3d15b71ff528a77
scratch/audit_k16_pass33_minimal_import_rematch_addendum_20260731.py
  SHA c79da02f02ebd2b5329f5d95b9dc1fd3a73706e722314da8536f94e3ce97ba01
scratch/k16_pass33_minimal_import_rematch_addendum_20260731.audit.json
  SHA c3fc6e2af5e23e62a60edf9f338ed2960f8d6ca5f6f7766adb04b617f52bc900
  payload c6b2f33f129620413dcffb4c5063203174e67d0c04f9b7ec47e61fdc1e6aec7c
```

Support-six census and sparse independent replay:

```text
MATH_AUDIT_L_K16_HALL24_CLOSURE_SUPPORT6_20260731.md
  SHA af92796d1c68907db41217583dd79387862e1613cbfa4588bea2c4025145a6ea
scratch/laneL_k16_hall24_closure_support6_census_20260731.cpp
  SHA dd4142035ec752705da43006ded7a184ad0f88eb4e4610c39616e7bcb551fa3b
scratch/audit_laneL_k16_hall24_closure_support6_20260731.py
  SHA 9ab22707de809da828fa088045db7acf9f199e8a8ed1ebadcf54e7ef989b11d3
scratch/laneL_k16_hall24_closure_support6_20260731.audit.json
  SHA 88df8f26573dd4db9711cb66d2a970ab00d248c82875536f76880b026f11a1dd
  payload 8d0ca73b46ed1c4c31eeb175ce0eb0286142fd83ca587d68752d958904a1bb85
```

The bounded native replay used 9.150516 seconds wall, 9.107229 seconds user,
and 13,369,344 bytes maximum RSS locally; it was a light finite run, with no
H100/SSH use.  The independent Python audit did not duplicate the 84-million
enumeration: it fully rebuilt and rematched all 24 exact rows and replayed 180
deterministic negative controls.  Its full-matching histogram on the exact
rows is `{26306:8,26307:12,26309:4}`.  Exhaustive authority for the negative
class is the native trace together with the exact `binom(22,s)!s` partition.

## 9. Scope boundary

The rank formula (4.1) is exact for **every** subset of the stated old
matching dependency packets after an abstract named port is activated and
`8000--J31761` is forced.  It does not say that an arbitrary incidence-loss
set is physically realizable, nor does it cover gains or losses outside the
packet without a fresh application of (2.1).

The occurrence no-go is complete only for arbitrary permutations of actual
support at most six inside the stated 22-row deck.  It does not cover a
remote occurrence import, support seven or larger, a changed flat schedule,
or a different/nonzero-target DM exit.  The packet theorem is complete only
for the frozen pass33 depth-seven table and its direct minimal-import tests.
No conclusion about `nu(16)` follows.
