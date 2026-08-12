# Physical duplicate/root readiness for an exposed-root native forest

Date: 2026-07-28

Status: exact polynomial-time criterion for one native-retaining Hall unit,
plus a deterministic checker and an exact Hall-20 to Hall-19 calibration.
The criterion works for a forest with any number of exposed roots, but fills
only one root at a time.  It does not identify incidence rank with literal
common-word feasibility and does not claim a full compiler.

## 1. Setup

Let `P=(P_p)` be one pointwise nonempty controller word on a finite ordered
position set.  Every physical cell `c` has an interval `I_c` and native trace

\[
                         \tau_P(c)=\bigcup_{p\in I_c}P_p.       \tag{1.1}
\]

Let `(X,Y)` be an exposed-root native forest: for some exposed set
`R subset X`, the native traces of the cells in `Y` are distinct and equal
to `X minus R`.  More generally, let `T` be the complete set of native labels
which must be retained.  In an application `T` contains `X minus R`, and may
also contain the native labels of every other protected DM component; assume
`T` is disjoint from `R`.

For `t in T`, put

\[
                    O_t=\{c:\tau_P(c)=t\}.                    \tag{1.2}
\]

The restriction to `O_t` is deliberate.  This is the **native-retaining**
architecture: old protected targets remain on cells on which they are native
under `P`.  Arbitrary nonnative reassignment is a different problem.

Fix a root `rho in R` and a cell `c` with `tau_P(c) in T`.  Exactness of the
new root pin forces the coordinatewise maximal candidate word

\[
 P^{\rho,c}_p=
 \begin{cases}
 P_p\cap\rho,&p\in I_c,\\
 P_p,&p\notin I_c.
 \end{cases}                                                    \tag{1.3}
\]

Call `(rho,c)` a **central-feasible port** if (1.3) is pointwise nonempty,
all central windows remain exact, and
`tau_{P^{rho,c}}(c)=rho`.  Equivalently, `(rho,c)` is an edge of the exact
compiler incidence graph built from `P`.

For every protected label define its surviving native bank

\[
 O_t(\rho,c)=\{z\in O_t\setminus\{c\}:
                    \tau_{P^{\rho,c}}(z)=t\}.                  \tag{1.4}
\]

## 2. Exact one-unit theorem

### Theorem 2.1 (physical duplicate/root readiness)

For an exposed-root native forest with any `s=|R|`, a central-feasible port
`(rho,c)` supplies one literal native-retaining root unit under one common
word if and only if

\[
                 \boxed{O_t(\rho,c)\ne\varnothing
                         \quad\hbox{for every }t\in T.}         \tag{2.1}
\]

When (2.1) holds, choose one cell from every `O_t(rho,c)` and use `c` for
`rho`.  All chosen cells are automatically distinct.

#### Proof

The root pin's negative requirements force every letter in `I_c` to be a
subset of `rho`.  Thus (1.3) is the unique coordinatewise maximal word
compatible with the central constraints and the root pin.  Central
feasibility says that this maximal word already realizes the root and all
central windows.

For a protected native label `t`, a native-retaining realization can use
exactly a cell in (1.4).  If (1.4) is empty, passing to a smaller word cannot
restore a deleted coordinate, so no such realization exists.  Conversely,
if every bank is nonempty, choose one survivor from each bank.  A physical
cell has only one native trace under `P`, so banks for distinct labels are
disjoint; excluding `c` also keeps the root cell distinct.  The selected
pins and the root pin are therefore realized simultaneously by (1.3).
\(\square\)

Define the exact readiness defect

\[
 \delta(\rho,c)=|\{t\in T:O_t(\rho,c)=\varnothing\}|.          \tag{2.2}
\]

Then `delta=0` is readiness, not a heuristic.  A port with

\[
 \delta(\rho,c)=1,
 \qquad\{t:O_t(\rho,c)=\varnothing\}=\{\tau_P(c)\}             \tag{2.3}
\]

is a clean **one-duplicate obligation**: creating one additional native
occurrence of `tau_P(c)` which survives (1.3) would make that port ready.
Condition (2.3) does not assert that a legal braid creating the occurrence
exists.

### Corollary 2.2 (a prescribed multi-root assignment)

For an injective assignment `phi:R_0 -> C` of any chosen exposed roots to
physical cells, form

\[
 P^\phi_p=P_p\cap
   \bigcap_{\rho:\,p\in I_{\phi(\rho)}}\rho.                    \tag{2.4}
\]

The prescribed assignment and all protected native labels coexist under one
word if and only if (2.4) is nonempty, preserves every central window,
realizes each root on its assigned cell, and every `t in T` has a native
occurrence outside `phi(R_0)` whose trace under `P^phi` is still `t`.

This is again necessary and sufficient by maximality and disjointness of the
native banks.  It is polynomial for a specified `phi`.  The theorem does not
claim that choosing `phi` from an unbounded candidate family is a matching
problem; overlapping root intervals create genuine higher-order
interactions.

### Complexity

For every root-cell port, construct (1.3) and scan the native occurrence
banks.  The direct running time is polynomial, for example
`O(|R| |C|^2 h)` for maximum cell length `h`; coordinate carrier prefix
tables reduce this further.  No SAT solver or carrier enumeration is
involved.

A fixed assignment of several root cells is also checkable in polynomial
time by intersecting all their root masks and applying the overlap-safe
common-word criterion.  Selecting the assignment itself is an interacting
multi-root problem and is not covered by Theorem 2.1.

## 3. The three gates are different

### Gate I: incidence rank

The occurrence-labelled compiler graph asks only whether target-cell edges
admit a matching.  The induced rank of `X` can be computed by one bipartite
matching.  It does not say that the selected edges coexist under one word.

If Theorem 2.1 holds, its displayed cells give an incidence matching of one
more unit.  The converse is false in general because a matching may use
nonnative edges or individually feasible edges whose blocker requirements
are incompatible.

Here is a two-position counterexample even with a literal duplicate.  Let

```text
P_1={x,y},  P_2={y};
c=[1],      z=[1,2];
a={x,y},    rho={y}.
```

Both `c` and `z` have native trace `a`.  The incidence graph has the matching
`rho-c, a-z`, so its rank is two.  But realizing `rho` on `c` deletes `x`
from position 1, after which `z` has trace `{y}`, not `a`.  Reversing the two
cells also fails.  Thus duplicate multiplicity plus incidence rank is not a
physical-readiness criterion; the survivor condition (2.1) is essential.

In particular, on a fixed positive DM component of a Hall-19 state, a
zero-defect port would already increase its matching rank.  Therefore every
Hall-19-neutral state has zero exact ready ports on its unchanged critical
component.  Ranking neutral states merely by the number of `delta=0` ports
is vacuous.  The useful prospective statistic is instead the exact defect
profile, especially the number of clean ports satisfying (2.3).

### Gate II: shore-local common word

Theorem 2.1 is exact at this level.  The protected set `T` must be stated
explicitly.  Protecting only the focal component can give a false positive
if the shrink destroys a native pin in another critical component.  The
checker therefore protects the candidate state's entire DM-native basis by
default.

There are two non-equivalent ranking lanes.  A **fixed-shore** census keeps
the old `(X,R)` while the carrier changes; this detects a remote discharge
such as root `24610`.  An **intrinsic** census rebuilds every candidate's own
DM components and scores their exposed sets; this detects root migration or
component splitting.  The theorem applies to both, but neither lane subsumes
the other.

### Gate III: full compiler

After fixing a ready port one may:

1. reserve its shore-local physical pins and compute a maximum exterior
   **incidence** matching; and
2. compute which lower targets happen to occur under the forced word (1.3).

Neither diagnostic is the missing full theorem.  An exterior incidence
matching need not be common-word realizable.  Conversely, failure of the
maximal forced word to cover every lower target does not rule out a further
coordinated thinning.  For a *specified* complete pin family, the blocker
criterion is again polynomial and exact; choosing the complete matching and
word together remains the global compiler problem.

## 4. Exact H20 to H19 calibration

Use the root-`24610` `161/160` component of

```text
scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json
```

as the reference forest, and score it in the final carrier

```text
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json.
```

Protect both its 160 nonroot targets and all 497 native targets of the final
Hall-19 DM shore, so `|T|=657`.  The exact results are

\[
\begin{array}{c|c}
\text{reference native rank}&160\\
\text{final induced rank on the 161 targets}&161\\
\text{final physical neighbours}&162\\
\text{native multiplicities on }T&655\cdot1+2\cdot2\\
\text{central-feasible root ports}&77\\
\text{ready ports }(\delta=0)&3\\
\text{clean one-duplicate ports }(\delta=1)&74.
\end{array}                                                       \tag{4.1}
\]

The first two ready ports are the known depth-zero `25634` cells `1212` and
`4713`.  The criterion finds a third exact port which the earlier two-socket
audit did not enumerate:

```text
root        24610
root cell   11671
depth/start 1 / 5233
old trace   26146
companion   11150 (also native trace 26146)
```

Shrinking cell `11671` to `24610` preserves every central window and all 657
protected native pins.  Its forced-word SHA-256 digest is

```text
dd6545e6383f9c44fa0bec775538409ff550f6106b1e4973512f2f3d9b835fd7
```

The protected-shore incidence system extends to global rank `16364`, exactly
as for the two depth-zero ports.  Yet the forced word itself contains only
`14413` of the `16383` lower targets, leaving `1970` holes.  This is a
concrete calibration of the separation between shore-local common-word
readiness, global incidence extension, and a complete literal compiler.

Before the improving braid, the router's root-`24610` component has

```text
76 central-feasible ports, 0 ready ports, 76 clean one-duplicate obligations.
```

The improving braid changes this to the `3 + 74` profile in (4.1).  This is
the exact physical signature of the rank unit.

For the current final Hall-19 `321/319` forest exposed at
`{8217,8218}`, the baseline score is

```text
148 central-feasible ports;
0 ready ports;
147 clean one-duplicate obligations;
1 port of readiness defect 2.
```

Thus the exact test correctly refuses to call the Hall-19 state ready while
exposing a large, sharply defined one-duplicate frontier for prospective
neutral routers.

An exact remote-CPU census of all 689 canonical Hall-19-neutral one-braid
states found

```text
ready states:                    0 / 689
minimum readiness defect:       1 in every state
base clean one-duplicate ports: 147
best clean one-duplicate ports: 149
```

The three best fixed-shore states are

```text
c0089  FF(806,1487,6427)
c0509  RF(576,2557,6235)
c0416  FR(2824,5198,5628).
```

For these three, neither fixed root is a protected native label and both
`8217,8218` remain exposed.  Thus their score is within Theorem 2.1's scope.
This proves that one neutral braid in the enumerated beam never creates an
already-ready fixed-forest socket.  It does not rule out an intrinsic
root-migrated socket, a two-braid route, or a braid outside the enumerated
move class.

## 5. Checker and frozen outputs

Run the deterministic audit with

```text
python3 scratch/check_k15_physical_root_readiness.py \
  scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json \
  --reference scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json \
  --root 24610 \
  --output scratch/k15_h20_h19_physical_readiness_calibration.json
```

The final Hall-19 two-root baseline is

```text
python3 scratch/check_k15_physical_root_readiness.py \
  scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json \
  --root 8217 \
  --output scratch/k15_h19_root8216_physical_readiness_baseline.json
```

Current SHA-256 values are

```text
8f777320171c02d6bc6bcd136be3b4dba7fcc09690e1d8326a34410b2d95f8e2
  scratch/check_k15_physical_root_readiness.py
4ed024f9b74499d0614f7614464cc318f7ad40c4b515e3ced11f1c37ed019a53
  scratch/k15_h20_h19_physical_readiness_calibration.json
406d6838091573c1729b5b591c184ee93596a5a4311f07a95826ac24987bfd25
  scratch/k15_h19_root8216_physical_readiness_baseline.json
```

The script reconstructs one or two frozen compiler graphs.  It performs no
braid search, SAT call, or production enumeration.  A large neutral-state
beam should be enumerated and scored only on the `h100` CPU host.

The remote beam artifact is

```text
24fbceea139c8e1d8325878f77b0f823e9dc80bcbe8f9bfd2597b74b5731861d
  /dev/shm/k15_rotation/h19_neutral_profile_20260728/physical_readiness.json
```

and its deterministic batch generator is
`scratch/census_k15_h19_physical_readiness.py`.

## 6. Exact proved boundary

Proved:

* Theorem 2.1 is necessary and sufficient for one native-retaining root unit
  under one controller, for any number of exposed roots.
* The readiness defect and clean one-duplicate frontier are polynomial-time
  computable.
* The H20-to-H19 endpoint has three, not merely two, protected-shore literal
  root sockets.
* The current two-root Hall-19 forest is not ready and is one duplicate away
  at 147 individually certified ports.

Not proved:

* that any Hall-19 neutral braid creates a required surviving duplicate;
* simultaneous completion of both roots `8217,8218`;
* a common word for an exterior maximum matching; or
* Hall 18, Hall 0, or `nu(15)=6438`.
