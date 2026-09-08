# Fractional configuration feasibility implies a zero-defect named residual collar one depth later

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** exact synthesis theorem after independent correction.  Conditional
on the all-price fractional whole-job configuration inequalities at depth
`D`, the canonical **residual** Boolean histogram one depth later has an
integral, target-once, occurrence-labelled collar realization with no
unmatched residual target.  A separately priced triangular/boundary bank is
not silently re-proved.  The theorem also does **not** serialize this collar
as the suffix system of one upper-complete resident word.

## 1. Parameters and the scalar hypothesis

Work in `B_(2r)`, and assume `D>=1` and `t>=2`.  Put

\[
 C_s={2r\choose s},\qquad H_s=C_s-C_{s-1},\qquad
 W=C_r,\qquad t=r-D,\qquad b=t-1,
 \qquad D^+=D+1.                                    \tag{1.1}
\]

At old depth `D`, take the complete nonempty residual histogram on ranks
`1,...,t-1` and write it as canonical horizontal suffix jobs.  A job born at
rank `a<t` has old length `t-a`, with the punctured bottom-zero chain merged
into the rank-one birth class.  The old collar tails are

\[
 K_q=W-C_{t+q-1}\qquad(1\le q\le D).                \tag{1.2}
\]

The only anonymous packing hypothesis is:

> **Fractional configuration hypothesis `FC_D`.**  The exact whole-job
> configuration LP, whose only aggregate constrained resources are the `D`
> tails (1.2), is feasible.

A configuration is a composition of one whole job into positive pieces of
length at most `D`; its resource vector is the conjugate piece-length tail.
Thus `FC_D` is the complete covering-price system, not merely total work,
piece count, or rank majorisation.

Passing to depth `D+1` performs terminal deletion.  The old rank-`t-1`
singleton jobs disappear and every other job loses its final cell.  The new
residual histogram is therefore on ranks

\[
                         1,\ldots,b-1=t-2.           \tag{1.3}
\]

This off-by-one convention is essential below.

## 2. Exact adjacent-depth closure theorem

Let `L_max<=t-2` be the largest surviving post-deletion job length (take
`L_max=0` if none survives) and put

\[
 h:=D\left\lceil {L_{\max}\over D}\right\rceil<r.  \tag{2.1}
\]

For `1<=g<=D+1`, put

\[
 u_g=b+g,
 \qquad d_g={2r-b+1\choose g+1}.                    \tag{2.2}
\]

### Theorem 2.1 (zero-defect named residual collar at depth `D+1`)

Assume `FC_D`.  Let `Delta_1,...,Delta_(D+1)` be nonnegative integers
satisfying the exact tail-reserve inequalities

\[
 h+\sum_{g=q}^{D+1}\Delta_g\le H_{t+q-1}
       \quad(1\le q\le D),                          \tag{2.3}
\]

\[
 h+\Delta_{D+1}\le H_r,                            \tag{2.4}
\]

and the pointwise-spread inequalities

\[
 {\Delta_g^2d_g\over C_{u_g}H_{u_g}}
 \ge A_0(2r)\qquad(1\le g\le D+1),                \tag{2.5}
\]

where `A_0` is the absolute constant in the MLD--Holder union bound.  Then
there is a realization with all of the following properties.

1. Every target in the new residual ranks `1,...,b-1` occurs in exactly one
   literal inclusion-chain fragment.
2. Every fragment has a capacity mark in `{1,...,D+1}`, fixed before path
   realization, and is eventually assigned to a distinct **actual** Boolean
   collar-chain occurrence of at least that capacity.
3. The top of every fragment is contained in the named bottom of its
   assigned occurrence.
4. Every surviving descendant of a job discarded by basic configuration
   rounding is present; no residual target is exceptional or unmatched.
5. At least `Delta_g` further genuine capacity-`g` occurrences remain unused
   for every `g`.

Hence the canonical residual lower compiler has literal deficiency zero at
depth `D+1`.

#### Proof

Choose an extreme point of `FC_D`.  There is one equality row for each
abstract whole job and only `D` independent aggregate tail rows.  The
support-rank argument leaves at most `D` jobs with more than one positive
configuration.  Retain the unique integral configuration of every other old
job and apply terminal deletion: remove the final cell, shortening or
deleting its final piece.  Terminal deletion cannot increase a conjugate
piece tail.  Thus the aggregate transported ordinary tails satisfy

\[
 A_q\le K_q\quad(1\le q\le D),\qquad A_{D+1}=0.    \tag{2.6}
\]

The new bottom is `b=t-1`.  Its exact capacity tails are

\[
 K_q^+=W-C_{b+q-1}\qquad(1\le q\le D+1),           \tag{2.7}
\]

and therefore

\[
 K_q^+-K_q=H_{t+q-1}\quad(1\le q\le D),
 \qquad K_{D+1}^+=H_r.                              \tag{2.8}
\]

Every exceptional old singleton disappears.  Split each other exceptional
descendant consecutively into pieces of length at most `D`.  There are at
most `h` such pieces by (2.1).  Delete `h` genuine capacity-`D+1`
occurrences and another `Delta_g` occurrences of exact capacity `g`.  For
every `q<=D`, equations (2.3), (2.6), and (2.8) give

\[
 A_q\le K_q
 \le K_q^+-h-\sum_{g=q}^{D+1}\Delta_g.             \tag{2.9}
\]

At `q=D+1` there is no ordinary demand.  The conjugate-tail matching
criterion therefore injects every ordinary piece into the remaining
capacity multiset.  Put the exceptional pieces on distinct members of the
reserved maximum-capacity bank.  This is an exact capacity-type assignment
and leaves the declared reserve.

The terminal-deletion map, piece lengths, and capacity types are fixed from
deterministic birth counts, extreme-point configuration counts, and collar
multiplicities before any Boolean path is exposed.  Refine each new-depth
birth/configuration cohort uniformly by these complete marked vectors, and
only then realize the independent uniform augmented Boolean matchings up to
cutoff `b-1`.  The cohort-stable multinomial-Laplace theorem preserves MLD.
Cutting the paths according to their marks gives literal target-disjoint
fragments covering every new residual target exactly once.

Named Boolean bottoms were not fixed in the preceding step.  For a fixed
socket rank `u` and owner `T`, every marked fragment-top family at a lower
rank is a union of MLD labels.  Generalized Holder combines the one-rank
binomial Laplace bounds without assuming cross-rank independence.  Equation
(2.5) and a union bound give all pointwise Hall inequalities simultaneously.
The pointwise-codegree matching theorem then attaches all ordinary and
exceptional requests, in one matching, to distinct containing genuine
collar bottoms.  This proves items 1--5. `square`

### Corollary 2.2 (the required reserve exists in the coefficient-one regime)

Suppose `D=Theta(sqrt(r))` (more generally, the same argument works when
`D->infinity` and `D=O(sqrt(r))`).  For a sufficiently large absolute
constant `A`, set

\[
 \Delta_g=
 \left\lceil A\sqrt{rC_{u_g}H_{u_g}/d_g}\right\rceil. \tag{2.10}
\]

Then, for all sufficiently large `r`, equations (2.3)--(2.5) hold.

#### Proof

Equation (2.10) gives (2.5) after increasing `A`.  Also `h<r`, while
uniformly for `t<=s<=r`,

\[
                         H_s\gg W/r\gg r.            \tag{2.11}
\]

The adjacent-tail reserve estimate gives

\[
 \sum_{g=q}^{D+1}\Delta_g=o(H_{t+q-1})\quad(q\le D),
 \qquad \Delta_{D+1}=o(H_r).                        \tag{2.12}
\]

Equations (2.3)--(2.4) follow. `square`

## 3. Exact implication for the word problem

For even dimension `k=2r`, put `D=d(2r)` and `B(2r)=W+D`.  The adjacent
short-row geometry would live at physical length

\[
                         W+D+1=B(2r)+1.              \tag{3.1}
\]

Theorem 2.1 makes the **residual** lower side conditionally exact at that
depth: it creates no append-only residual casualty or growing residual
sidecar.  It is not itself a word construction.  One still needs a protected
serialization map which co-realizes the named collar forest—and any
separately priced triangular/boundary bank—with one chronology satisfying

1. every central owner exactly once and one connected physical order;
2. a depth-`D+1` antecedent (equivalently, on the flat owner face, the
   corresponding owner-run residence floor `D+2`);
3. complete arbitrary-width upper interval-OR coverage;
4. every collar bottom/capacity and every residual attachment above; and
5. every strict-lower target not included in the residual histogram, if a
   boundary bank was removed before `FC_D` was formed.

A Boolean collar-chain occurrence is not automatically a suffix occurrence
of a separately chosen central word, and conditioning the MLD path cover on
an upper carrier is not known to preserve MLD.

### Corollary 3.1 (precise even-dimensional `B+1` reduction)

For all sufficiently large even `k=2r`, the conjunction of

* `FC_(d(k))`;
* a literal realization of every separately priced boundary target, when
  applicable; and
* the protected serialization map above

implies

\[
                         \nu(k)\le B(k)+1.           \tag{3.2}
\]

The deadline lower bound then leaves only `B(k)` and `B(k)+1`.  No odd
conclusion follows from this even-layer argument without a separate odd
analogue.

## 4. Exact same-depth boundary

The one-depth increment supplies both the adjacent-tail occurrence bank and
the physical short-window row in which those occurrences would live.  The
bank cannot simply be carved out at old depth.  If a retained integral
selection saturates an old tail `A_q=K_q`, deleting even one socket of
capacity at least `q` makes that fixed selection infeasible.

More generally, if `p_a^0` are the retained ordinary Ferrers vectors,
`S=K-sum_a p_a^0` is their residual tail slack, and `F` is the exceptional
family, same-depth completion is exactly the problem of finding alternative
ordinary configurations `p_a` and exception configurations `q_f` with

\[
 \sum_a(p_a-p_a^0)+\sum_{f\in F}q_f\le S
 \quad\hbox{coordinatewise}.                        \tag{4.1}
\]

Thus `C=0` needs an integer augmentation/normality theorem jointly
reconfiguring ordinary and exceptional jobs, not merely a relocation of the
adjacent bank.

There is an independent chronology obstruction.  On an even complete pair
slice, exact fractional owner/target marginals and connected support can
still require linearly many cross-slice incidences to form one Euler object.
This rules out a universal bounded-**support** serializer.  It does **not**
rule out `C=0`: a jointly designed full carrier may provide distributed
parity leakage at zero additional word length.  The present results prove a
no-go for naive internalization, not a no-go theorem for exact coefficient
one.

## 5. Dependencies and exact scope

This theorem composes:

1. `MATH_THEOREM_BOOLEAN_COHORT_STABLE_MULTINOMIAL_LAPLACE_INDUCTION_20260805.md`;
2. `MATH_THEOREM_MLD_BIRTH_CONFIGURATION_CHAINIZATION_AND_WEIGHTED_HALL_GATE_20260805.md`;
3. `MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`;
4. `MATH_THEOREM_MLD_EXCEPTIONAL_BANK_ADJACENT_TAIL_RESERVE_AND_JOINT_NAMED_LIFT_20260805.md`;
5. `MATH_THEOREM_SPREAD_TOP_NAMING_POINTWISE_CODEGREE_AND_RANDOM_PARTITION_20260805.md`;
6. `MATH_THEOREM_COMPLETE_PAIR_SLICE_TARGET_EXACT_PARITY_AND_LINEAR_LEAKAGE_NOGO_20260805.md`.

It proves no all-price inequality, no separately removed boundary bank, and
no upper/resident serialization.  It must not be cited as an unconditional
`B(k)+1`, `B(k)+O(1)`, or exact coefficient-one theorem.
