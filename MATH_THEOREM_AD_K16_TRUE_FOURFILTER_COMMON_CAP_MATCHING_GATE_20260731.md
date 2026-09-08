# Genuine four-filter K16: exact common-cap matching gate after the endpoint reroot

**Date:** 2026-07-31  
**Lane:** AD, provenance-correct carrier/compiler audit  
**Status:** exact carrier and common-cap reduction; the finite gate is now SAT and independently decoded to the optimal K16 word

## 1. Provenance and the corrected basin

The source is the genuine four-filter K15 word

```text
scratch/K15_FOURFILTER_SEED_20260731.word
SHA-256 51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4
```

with opening `(5134,0,5,1,0)`.  None of the historically named
`k16_fourfilter_insert_aug*`, `def4`, or `cut1004` orders is used: those
orders are seed0-derived.

For the parent word (w_0,ldots,w_{6437}), put

\[
D^2_i=w_i\vee w_{i+1}\vee w_{i+2},\qquad
D^3_i=w_i\vee w_{i+1}\vee w_{i+2}\vee w_{i+3}.
\]

The sole non-rank-seven member of (D^2) is
(D^2_{6390}=\mathtt{0x13c8}), of rank six.  The other (6435) members
are the complete rank-seven layer on the old coordinates, and (D^3) is
the complete rank-eight layer.  With (z=\mathtt{0x8000}), the natural
K16 chronology is

\[
T=\operatorname{rev}(z\vee D^2[0:6390])
  \;\Vert\;D^3
  \;\Vert\;\operatorname{rev}(z\vee D^2[6391:6436]).
\tag{1.1}
\]

Its canonical SHA-256 is

```text
0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c.
```

The natural order is an exact Johnson Hamilton path but has the six upper
holes

\[
\mathtt{b3cc},\mathtt{d3cc},\mathtt{d3ce},\mathtt{f3cc},
\mathtt{dbce},\mathtt{fbce}.
\tag{1.2}
\]

Reverse the inclusive prefix `[0,6388]` and inclusive suffix
`[12826,12869]`.  The resulting target order is

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.
```

It contains all (12870) middle targets once, has every q1 colour, and
literal interval replay has no upper hole at any rank.  The two new boundary
q1 colours are `d3cc` and `b3cc`; the corresponding longer boundary
intervals supply the other four masks in (1.2), and exhaustive replay loses
no old upper mask.

## 2. Exact live P/Q schedule

The exact all-schedule singleton-host event DAG requires a literal
`0x8000` cell and ranges over every monotone depth-three P/Q schedule with
three omitted starts and three omitted deadlines.  Its optimum is

\[
X=\{12870,12871,12872\},\qquad
Y=\{0,1,6388\},
\tag{2.1}
\]

with selected proper-prefix area (32224).  The singleton is installed at
physical position (6389).  The uniform omitted-start credit gives
(32233), while the endpoint-exact credit is (3+2+1=6), so there are
exactly

\[
32224+6=32230
\tag{2.2}
\]

physical lower cells.  Capping position (6389) to `0x8000` leaves every
middle row exact.

For schedule (2.1), the complete individual-pin graph built from the
uncapped maximal envelope has

```text
lower targets       26,332
physical cells      32,230
incidences         347,734
zero-host targets        0
maximum matching    26,332.
```

The singleton target `0x8000` has exactly one edge, to cell `(6389,1)`.
Consequently every perfect matching selects that edge and the common-cap
test itself enforces the singleton cap.  If position (6389) is capped
before graph generation, the graph has (347678) incidences and still has
matching (26332); reserving the singleton target and cell first leaves
(347677) incidences and a perfect (26331)-matching.

Thus the genuine four-filter endpoint reroot passes middle ownership,
all upper shadows, scalar capacity, the singleton host, and marginal Hall.
This is not yet common-cap sufficiency.

## 3. Exact maximal common-cap theorem

The following statement applies to any fixed integral P/Q schedule.

Let (I_i=[s_i,d_i]) be the physical interval assigned to middle target
(T_i), and let

\[
E_p=\bigcap_{i:p\in I_i}T_i
\tag{3.1}
\]

be the maximal middle envelope.  Let ({\cal C}) be the selected-start
proper-prefix cells together with the allowed omitted-start cells.  Suppose
an injective assignment (M) sends every lower target (S) to one of its
individually feasible cells (C=M(S)\in{\cal C}).  Define

\[
A_p(M)=E_p\cap
       \bigcap_{S:p\in M(S)} S.
\tag{3.2}
\]

An empty intersection of active middle rows or assigned lower masks is, by
convention, the full coordinate set.  In the concrete schedule (2.1), every
position is covered by an active middle row.

### Theorem 3.1 (maximal common cap)

The matching (M) admits one physical word realizing every assigned lower
target and every middle row if and only if all three conditions hold:

1. (A_p(M)\ne\varnothing) for every physical position (p);
2. \(\bigvee_{p\in I_i}A_p(M)=T_i\) for every middle row (i);
3. \(\bigvee_{p\in M(S)}A_p(M)=S\) for every lower target (S).

When they hold, the word (A(M)) itself is a realizing word.

#### Proof

Let (B) be any simultaneous realization.  Middle legality gives
(B_p\subseteq E_p).  If (p\in M(S)), exact realization of (S) gives
(B_p\subseteq S).  Hence (B_p\subseteq A_p(M)) pointwise.  Because
(B) is nonempty and supplies every required coordinate in every middle
and lower interval, the larger word (A(M)) satisfies conditions 1--3.

Conversely, (3.2) is contained in every active middle target and in every
assigned lower target whose cell contains (p).  Conditions 1--3 therefore
say exactly that (A(M)) is nonempty and has the required OR on every
middle and lower interval.  No forbidden coordinate can occur.  Hence it is
a simultaneous realization.  □

For (2.1), consecutive middle intervals have no physical gap.  Since the
reroot chronology is upper-complete, any word passing Theorem 3.1 is already
universal: every upper target is the OR of a consecutive block of middle
rows, and the union of their physical row intervals is contiguous.  Thus the
only remaining gate is to find a perfect lower matching passing conditions
1--3.

The lower-cell catalogue is complete for this schedule.  Every selected
physical start (s_i) first reaches its assigned rank-eight row at (d_i),
so every lower interval beginning there is one of the proper prefixes
already in ({\cal C}).  The only omitted starts are the terminal positions
(12870,12871,12872); all their physically possible intervals have lengths
(1..3), (1..2), and (1), respectively, and all six are included.
Hence any universal word in this fixed P/Q fibre induces an injective
assignment of all lower targets to the master catalogue.

## 4. Complete matching-only CEGAR

Theorem 3.1 gives an exact finite Benders/CEGAR algorithm with no fractional
or fixed-matching assumption.

Use one Boolean (y_{S,C}) for every one of the (347734) authenticated
individual incidences.  The master consists of

\[
\sum_{C\in N(S)}y_{S,C}=1\quad(S\text{ lower}),
\qquad
\sum_{S:C\in N(S)}y_{S,C}\le1\quad(C\in{\cal C}).
\tag{4.1}
\]

Given an integral master matching, form (3.2) and replay it.  Every failure
has a small exact no-good.

### 4.1 Empty-position cut

If (A_p(M)=\varnothing), choose an inclusion-minimal set (B) of selected
incidences whose assigned masks already have empty intersection with (E_p).
Add

\[
\sum_{e\in B}y_e\le |B|-1.
\tag{4.2}
\]

Minimality injects the members of (B) into distinct coordinates of (E_p),
so (|B|\le |E_p|\le8).

### 4.2 Middle-bit cut

If coordinate (b\in T_i) is absent from the OR on (I_i), the selected
incidences whose masks omit (b) cover the complete host set

\[
H_{i,b}=\{p\in I_i:b\in E_p\}.
\]

Take an inclusion-minimal covering subfamily (B) and add (4.2).  Because
(|I_i|\le4), one may choose (|B|\le4).

### 4.3 Assigned-lower-bit cut

Suppose (e_0=(S,C)) is selected and coordinate (b\in S) is missing from
the realized OR on (C).  Other selected incidences whose masks omit (b)
cover

\[
H_{C,b}=\{p\in C:b\in E_p\}.
\]

For an inclusion-minimal covering family (B), add

\[
y_{e_0}+\sum_{e\in B}y_e\le |B|.
\tag{4.3}
\]

Here (|C|\le3), so (|B|\le3).  Extra bits cannot cause a failure because
(3.2) is already contained in (S).

Every cut excludes the current matching and only matchings that have the
same literal obstruction.  Conversely, Theorem 3.1 says that a matching
with no such failure is a literal solution.  Since the master has finitely
many integral matchings, repeated separation either returns a universal
word or proves this schedule infeasible.  This is an exact integral
algorithm, not a heuristic relaxation.

## 5. First deterministic matching was not decisive; the joint model is SAT

An independently generated Hopcroft--Karp perfect matching was capped by
(3.2).  It has no zero letter, but it leaves (1808) middle rows and (5045)
assigned lower cells nonexact.  This is useful only as the first CEGAR
separation batch.  It is **not** a common-cap no-go, because another perfect
matching may avoid all of those conflicts.

Before the joint solve, the exact boundary was:

> The provenance-correct upper-complete carrier and schedule (2.1) pass every
> marginal gate.  A length-12873 word exists in this fibre exactly when the
> matching master (4.1), separated by (4.2)--(4.3), has a surviving integral
> matching.

That gate is now closed positively.  The direct Boolean form of Theorem 3.1
has 1,055,230 variables and 4,513,893 clauses.  Its SAT assignment decodes to

```text
scratch/k16_optimal_12873_20260731.word
SHA-256 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe.
```

An independent direct-word checker, which does not trust the matching or SAT
metadata, replays all 65,535 nonempty masks.  Together with the deadline lower
bound, this gives `nu(16)=12873`.

## 6. Frozen evidence

```text
target chronology
  scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
  SHA c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906

all-schedule singleton-host DP
  scratch/audit_r_k16_true_fourfilter_endpoint_reroot_host8000_dp_20260731.py
  SHA f9be14541e8956267a9773fa1c088bfee9aa062a56fa68102f3d0ce4a58e7216
  scratch/k16_true_fourfilter_endpoint_reroot_host8000_dp_20260731.audit.json
  SHA eb3b607cacb166d79d7963e033c9da3f580bf72c148dd185616c3f86ea1b9766
  payload cbf4fe763f250a5e6c4c5c2eedd76c2a949cb78e6b5b565985facdae1c1ed81c

perfect marginal Hall
  scratch/k16_true_fourfilter_endpoint_reroot_host8000_maxpq_hall_20260731.audit.json
  SHA 725a9cfbc5f7d1bb4c7c8f5e9ae06ceef4bbaae873332a8dc244a12179f12c8d
  payload 09896b296606ad7e4b98b2f5d8cacdff79301131d392b97d721c57930a4599a3

independent AD singleton/Hall stdout
  scratch/ad_k16_genuine_fourfilter_natural_20260731/reroot_8000.stdout
  SHA eb6cd38c070ca77ea9e0f2bb88a1e3bc8cca608c205c997098f354ada90898f7
  scratch/ad_k16_genuine_fourfilter_natural_20260731/reroot_8000_hall.stdout
  SHA ec799404335c9b81461b92709634aad4ab463bbd9a7c5eb4d3960d43a3a868bd

first deterministic common-cap replay
  scratch/ad_k16_genuine_fourfilter_natural_20260731/reroot_8000_commoncap.stdout
  SHA 79b614e190508e965a357d96e18a6757b67f7e8462fc0edb69cdfe772e921d1e
```

All claims are source-relative to the displayed genuine parent, reroot
chronology, and schedule.  No seed0 no-go is transferred and no non-P/Q
construction is excluded.  The literal equality claim is recorded separately
in `MATH_CERTIFICATE_K16_OPTIMAL_12873_20260731.md`.
