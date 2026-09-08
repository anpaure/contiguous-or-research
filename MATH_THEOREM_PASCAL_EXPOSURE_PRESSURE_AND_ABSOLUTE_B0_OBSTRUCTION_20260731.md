# Pascal exposure pressure and the obstruction to an automatic absolute sidecar

Date: 2026-07-31  
Status: exact odd same-parity scalar theorem, exact physical-seam lower
bound for the edge-local lift, and an exact common-guard matching
counterexample.  A prospectively guarded `b0=3` theorem is proved
conditionally.  Existence of the required prospective guards in the
Boolean/Pascal construction remains open.

## 0. Verdict

The proposed inheritance row

\[
                       |U|\le 4\Phi+b_0                    \tag{0.1}
\]

does **not** follow from the current meaning of “fully guarded”: present
residence, present upper coverage, and a present common-cap matching do not
control what the next Pascal contraction deletes.

There is nevertheless a sharp positive normal form.  On an odd
same-parity step `k -> k+2`, only three lower targets are genuinely born.
If the parent state is guarded *prospectively*—its residence margin already
passes the child facet tax, its protected upper witnesses avoid the chosen
future seams, and one common-cap matching avoids the complete Pascal/collar
deletion bank—then

\[
                       \boxed{|U|\le4\Phi+3}.          \tag{0.2}
\]

Thus `b0=3` is the correct aspirational constant on the odd no-jump face.
The missing result is the existence of that prospective state, not any
further scalar arithmetic.

Two exact obstructions explain why the prospective adjective is
load-bearing.

1. Current matching feasibility plus enough scalar unused cells does not
   imply a matching avoiding the future deleted cells.  A disjoint
   common-guard gadget has current defect zero, deletion-bank size equal to
   scalar slack, and arbitrarily large post-deletion defect.
2. The canonical edge-local four-sector lift has `W` runs of length two for
   each new coordinate.  Any resident rethread changes

   \[
    2\left(W-\left\lfloor{2W\over d'+1}\right\rfloor\right)
   \]

   or more physical seams.  This is `Omega(W)`, so a bounded-seam collar
   proof cannot repair that lift.

The second statement is literal Boolean/Johnson chronology arithmetic.  The
first is an exact counterexample in the fixed-common-guard matching
abstraction; it is not asserted to be a realized all-ranks Pascal word.

## 1. Exact odd same-parity pressure

Let `k=2r-1`, and put

\[
 W={k\choose r},\qquad
 \Lambda=\sum_{j=1}^{r-1}{k\choose j},\qquad
 t_d={d+1\choose2},\qquad
 \sigma=dW+t_d-\Lambda,                              \tag{1.1}
\]

where `d=d(k)`.  Write

\[
                         c=\operatorname {Cat}_r.
\]

The exact same-parity recurrence is

\[
 W'=4W-c,\qquad \Lambda'=4\Lambda+3,
 \qquad d'\in\{d,d+1\}.                              \tag{1.2}
\]

Suppose first that the deadline does not jump, `d'=d`.  Four parent short
atlases contain

\[
                         4(dW+t_d)                    \tag{1.3}
\]

cells, whereas the child atlas contains

\[
 dW'+t_d=4dW-dc+t_d.                                 \tag{1.4}
\]

Therefore the Pascal contraction deletes exactly

\[
                         D=dc+3t_d                    \tag{1.5}
\]

source cells from the four-copy ledger.  At the same time (1.2) creates
exactly three new lower targets.  Consequently the exact scalar pressure is

\[
                         G=D+3=dc+3t_d+3,             \tag{1.6}
\]

and

\[
                         \sigma'=4\sigma-G.           \tag{1.7}
\]

The no-jump condition is precisely `4 sigma >= G`.  Thus scalar capacity
says that the four parent copies have enough unused cells to contain the
whole deletion bank and still host the three births.  It says nothing about
whether one common-cap matching can choose those unused cells.

On a jump step, the extra row supplies `W'+d+1` cells and the corresponding
identity is

\[
             \sigma'=4\sigma-G+W'+d+1.               \tag{1.8}
\]

That step is a recompilation/reset face, not a deletion-only transport, and
needs its own prospective state.

## 2. Exact compiler pressure

Let `H=(L,C;E)` be one fixed common-guard compiler graph and let
`D subset C` be the complete bank of physical cells removed by the chosen
Pascal contraction and rethread collar.  Define

\[
 \delta_D(H)=|L|-\nu(H-D)
 =\max_{X\subseteq L}\bigl(|X|-|N_H(X)\setminus D|\bigr). \tag{2.1}
\]

This is the exact number of formerly satisfiable target sources exposed
after the deletion.  Equation (2.1) is just deficient Hall.  In particular,

\[
 \delta_D(H)=0
 \quad\Longleftrightarrow\quad
 H-D\text{ has a target-saturating matching}.         \tag{2.2}
\]

Neither `nu(H)=|L|` nor `|D|<=|C|-|L|` implies (2.2).

### Theorem 2.1 (proof-safe exposure decomposition)

Suppose an accepted odd state has literal carried task mass at most `Phi`,
and every old task has at most four passive descendants in the two-new-
coordinate child.  For one specified child construction let

* `R` be the number of fresh residence/compensation packets;
* `P` be the number of fresh upper-provider casualties not already
  descendants of old tasks; and
* `T` be the number of fresh component/connector/topology tasks not already
  charged as descendants of carried tokens; and
* `delta_D(H)` be the compiler pressure (2.1), measured in one final common
  guard after all controller and seam cells have been identified.

Then the pre-repair source set may be chosen with

\[
 \boxed{
 |U|\le4\Phi+3+R+P+T+\delta_D(H).}                  \tag{2.3}
\]

#### Proof

Partition the child tasks into five disjoint origins.  Passive descendants
of old tasks contribute at most `4 Phi`.  Equation (1.2) contributes three
new lower labels.  The fresh residence and provider families contribute
`R`, `P`, and `T`.  Restrict a maximum old common-guard matching to the stable
child graph; deficient Hall (2.1) leaves exactly `delta_D(H)` compiler
sources.  Their union is a legal exposed source set, proving (2.3).  Any
overlap only improves the bound.  \(\square\)

### Corollary 2.2 (prospectively guarded absolute exposure)

If the selected lift has

\[
                         R=P=T=\delta_D(H)=0,          \tag{2.4}
\]

then (0.2) holds.  Hence an absolute exposure theorem is equivalent, on
this face, to a uniform prospective-guard theorem for the three fresh
pressures in (2.4).

This is stronger than a current fully guarded state.  Condition (2.4)
looks through the next Pascal step and names its actual seams and deleted
cells.

## 3. A sharp matching-level counterexample

For each `i=1,...,t`, take targets `a_i,b_i` and cells `p_i,q_i,z_i`, with

\[
 N(a_i)=N(b_i)=\{p_i,q_i\}.                           \tag{3.1}
\]

All copies are disjoint, and every cell uses one fixed, compatible guard.
The present graph has a matching of size `2t`; thus its current compiler
defect is zero.  It has `t` scalar unused cells, the `z_i`.

Delete

\[
                         D=\{p_1,\ldots,p_t\}.         \tag{3.2}
\]

Then `|D|=t` equals the scalar slack, but only `q_i` remains adjacent to the
two targets in copy `i`.  Therefore

\[
                         \delta_D(H)=t.               \tag{3.3}
\]

Taking `t` arbitrarily large proves that no absolute `b0` follows from
current common-guard feasibility plus the scalar inequality `|D|<=slack`.

This counterexample lies inside the fixed-guard matching/gammoid interface
used by the contraction theorem.  It is not a claim that every such graph
is realizable by Boolean erosion envelopes.  A positive Boolean theorem
must use precisely that extra geometry.

## 4. The edge-local Pascal lift needs a global rethread

Consider the compressed four-sector child cycle

\[
             [U_i\text{ when present}],Y_i,A_i,X_i
             \qquad(i\in\mathbb Z_W).                \tag{4.1}
\]

For each of the two new coordinates, (4.1) has exactly `2W` marked owners
split into exactly `W` cyclic runs, every one of length two.

Let `D_*=d'+1` be the required minimum residence run, and let `T'` be any
cyclic rethread of the same labelled owner set which is resident for that
coordinate.  It can have at most

\[
                         \left\lfloor{2W\over D_*}\right\rfloor \tag{4.2}
\]

marked runs.

### Theorem 4.1 (exact changed-seam lower bound)

If

\[
 s=|E(T)\setminus E(T')|=|E(T')\setminus E(T)|,
\]

then

\[
 \boxed{
 s\ge2\left(
 W-\left\lfloor{2W\over d'+1}\right\rfloor
 \right).}                                           \tag{4.3}
\]

In particular, once `d'>=2`,

\[
                         s\ge {2W\over3}-2.           \tag{4.4}
\]

#### Proof

In a cyclic binary trace the number of bichromatic edges is twice the
number of positive runs.  Every common physical edge contributes the same
bichromatic indicator before and after the rethread.  The difference of the
two bichromatic counts is therefore the difference of two sums, each over
`s` one-sided changed edges, and has absolute value at most `s`.  Decreasing
the run count by `R` decreases the bichromatic count by `2R`, so `s>=2R`.
Use `R>=W-floor(2W/D_*)`.  \(\square\)

Thus the direct edge-local lift cannot be repaired by a bounded number of
seams.  A successful same-parity theorem must construct a globally batched
resident braid or perform a genuine reset.

## 5. Exact collar charge

For two physical chronologies on the same owner occurrences, delete the
`s` old-only seams.  If the common fragments have vertex orders
`n_1,...,n_s`, the exact number of old and new boundary windows of edge span
`ell` is

\[
               b_\ell=\sum_{j=1}^s\min\{\ell,n_j\}
                      \le \ell s.                    \tag{5.1}
\]

For one width-`h` compiler cell type at erosion depth `d`, the potentially
changed right-vertex bank has exact size

\[
                         b_{d+h-1}.                   \tag{5.2}
\]

For `a_h` types at every start, the safe total is

\[
                 \sum_h a_h b_{d+h-1}
                 \le s\sum_h a_h(d+h-1).             \tag{5.3}
\]

These are boundary-column counts, not automatically exposed targets.  A
prospective matching may avoid every column.  Without such a matching,
(5.3) is the exact additive term missing from (0.1).

The bound is not vacuous in the bad direct lift: `b_ell>=s` for every
positive `ell`, and (4.4) makes even the raw boundary bank `Omega(W)`.

The literal two-cut `J(8,4)` collar from the AD--RSB theorem attains
`b_2=2s=4` and deletes the sole envelope occurrence of target `17` while
all displayed depth-two rank and wall tests continue to pass.  Hence local
rank legality is not a substitute for prospective occurrence or compiler
guards.

## 6. Exact remaining theorem

The shortest positive statement left by the audit is:

> **Prospective same-parity guard theorem.**  Every reachable accepted odd
> sidecar has a child braid and one child common guard such that (i) all
> facet residence taxes are discharged inside the braid, (ii) every upper
> target has a protected occurrence avoiding the chosen future seam set,
> (iii) the owner/component topology and its connector chronology are built
> into the protected baseline rather than born as fresh tasks, (iv) the
> transported four-copy compiler has a common-cap matching
> avoiding the complete Pascal/collar deletion bank, and (v) the three
> newborn lower targets augment into distinct remaining cells.

This theorem gives `|U|<=4 Phi+3` by Corollary 2.2 and can be combined with
the existing guarded Rado contraction.  It is not currently proved.

The important change of emphasis is that an absolute `b0` is not a local
collar estimate.  The raw collar is necessarily large for the canonical
lift.  An absolute theorem must make the large collar **invisible to one
prospectively selected global witness/matching system** or rebuild the
child state from scratch.

## 7. Audit

Run

```text
python3 scratch/audit_pascal_exposure_pressure_20260731.py
```

The audit checks the exact odd recurrence through `k=51`, the three-target
birth and deletion-pressure identities, the direct-lift status traces and
seam lower bound, the replicated Hall counterexample, and the literal
`J(8,4)` collar.  Its frozen output is

```text
scratch/pascal_exposure_pressure_20260731.audit.json
```

Scope exclusions are explicit in that JSON.  No unconditional
`nu(k)<=B(k)+O(1)` theorem is claimed.
