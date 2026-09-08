# Exact one-cell star phase selection and the prepared-coatom socket obstruction

Date: 2026-08-01  
Lane: Thread D, physical boundary/compiler ear  
Status: exact conditional phase-selector theorem, exact prepared two-sided
coatom no-go, and exact typed-singleton criterion.  No signed-lattice claim
is used or revisited.

## 0. Verdict

The one-cell seam has a real hidden channel, but it does not make the fan
and crossing banks independent.  With the notation of the frozen local
theorem,

\[
                 Z\cup C_i=L_{i+1}\cup R_{d-i+1}.             \tag{0.1}
\]

This identity has two consequences which must be kept separate.

1. There is an explicit **one-chain** terminal phase selector.  One fan can
   carry the native `NEW` prefix chain, the destroyed crossings carry the
   opposite-phase `OLD` prefix chain, and the prepared endpoint transporter
   can reproduce that family in the same terminal state.  The other
   fan contributes `d` unused physical addresses.  This is an exact local
   OR/matching construction, conditional on literal carrier replay and
   source-disjoint endpoint planting.
2. The proposed **full two-chain prepared-coatom packet** is false.  If the
   two nonsingleton fans carry the complementary prefix and suffix chains,
   every destroyed crossing contains both phase labels and the complete
   filler bank.  It has no incidence to either strict-lower `NEW` chain.
   This obstruction already occurs at `d=2`.  Hence the scalar identity
   `(2d-1)-(d-1)=d` does not provide `d` compiler credits in that fibre.

Even in the positive one-chain model, the `d` unused cells are addresses,
not `d` independently programmable values.  Typing the singleton star
uses one address and leaves `d-1`; it is legal only under the exact
star-envelope/forced-witness test.  A fixed task common to both phases must
pass that test simultaneously in both phase states.  The endpoint-carving
theorem alone proves neither this typed edge nor a phase-common matching.

## 1. Exact seam algebra

Fix `d>=2`, put the inserted source at `0=*`, and write the old flank
sources as `X_(-t),X_(+t)`, `1<=t<=d-1`.  Let `Z=X_0`.  Define

\[
\begin{aligned}
 C_i&=\bigcup_{t=1}^{i}X_{-t}
       \cup\bigcup_{t=1}^{d-i}X_{+t}, &&1\le i\le d-1,\\
 L_j&=Z\cup\bigcup_{t=1}^{j-1}X_{-t},
 &R_j&=Z\cup\bigcup_{t=1}^{j-1}X_{+t}, &&1\le j\le d.
\end{aligned}                                                \tag{1.1}
\]

Then (0.1) is immediate.  Coordinatewise, if `x` first occurs on the left
at distance `lambda_x` and on the right at distance `rho_x`, then

\[
 x\in C_i\iff i\ge\lambda_x\ \text{or}\ i\le d-\rho_x.       \tag{1.2}
\]

Thus the zero set of a crossing trace is an interval.  Conversely, after
the two nested fan chains are fixed, every coordinate outside `Z` has its
crossing trace forced by (0.1), while a coordinate in `Z` can realize
exactly the interval-zero traces by adding threshold copies on the flanks.
This is the exact compatibility theorem of
`MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md`.

Two useful cautions follow.

* Equation (0.1) is a **pair-union** identity.  It does not say that either
  `L_(i+1)` or `R_(d-i+1)` individually realizes `C_i`.
* The integer flank-incidence matrix has a unit lower-triangular left block
  and hence Smith form `I_(d-1)`.  Its formal kernel has rank `d`, but the
  Boolean positive cone is restricted by (1.2).  Formal rank is not a
  collection of `d` programmable sockets.

The smallest failures are exact.  At `d=2`, flank values `{x}` and `{y}`
give `C_1={x,y}` but fans `Z+x` and `Z+y`; neither fan is a provider for
`C_1`.  At `d=4`, prescribing an outside-star coordinate only in `C_2`
violates interval-zero convexity.

## 2. A literal one-chain phase selector

Let `C,{a},{b},{f_1},...,{f_d}` be pairwise disjoint with `C` nonempty,
and put

\[
 B_0=C\cup\{a\},\qquad B_1=C\cup\{b\},\qquad
 F_i=\{f_1,\ldots,f_i\}.                                    \tag{2.1}
\]

For phase `epsilon in {0,1}`, take

\[
\begin{aligned}
 Z^\epsilon&=B_\epsilon,\\
 X_{-t}^\epsilon&=C\cup\{f_t\} &&(1\le t\le d-1),\\
 X_{+1}^\epsilon&=B_{1-\epsilon},\\
 X_{+t}^\epsilon&=C &&(2\le t\le d-1).
\end{aligned}                                                \tag{2.2}
\]

### Theorem 2.1 (asymmetric one-chain selector)

For every `1<=i<=d-1`, the word (2.2) has

\[
 C_i^\epsilon=B_{1-\epsilon}\cup F_i=:\operatorname{OLD}_i^\epsilon,
 \qquad
 L_{i+1}^\epsilon=B_\epsilon\cup F_i=:
       \operatorname{NEW}_i^\epsilon.                        \tag{2.3}
\]

Moreover,

\[
 R_1^\epsilon=B_\epsilon,\qquad
 R_j^\epsilon=B_0\cup B_1\quad(2\le j\le d).                \tag{2.4}
\]

Hence the destroyed crossings encode the complete opposite-phase `OLD`
prefix chain, the left nonsingleton fan carries the native `NEW` prefix
chain by identity caps, and all `d` right-fan addresses are unused by these
assignments.  Mirroring gives the suffix version.

If a prepared endpoint carve supplies the opposite-phase `OLD` family in
terminal state `epsilon`, and if its source positions are disjoint from the star
collar, then the native/fan and endpoint assignments coexist as a terminal
matching.  This conclusion is phase-specific: the two terminal phases may
use different source words and different matchings.

#### Proof

Every crossing `I_i` contains `+1`, hence contains `B_(1-epsilon)`, and
contains precisely the left filler increments `f_1,...,f_i`; the other
positive flank sources add only `C`.  This gives the first formula in
(2.3).  The star and the first `i` negative sources give the second.
Formula (2.4) is immediate.  All selected left-fan targets contain the star
payload `B_epsilon`, so their simultaneous identity caps do not shrink the
shared source.  The endpoint theorem supplies one literal word for the
opposite-phase `OLD` family in the same terminal state; disjoint source
supports make the two carvings
coexistent, subject to the stated carrier-replay hypothesis. \(\square\)

This theorem is deliberately one-sided.  It does not realize the second
packet chain in the unused fan while retaining the same crossing bank.
Also, `R_2,...,R_d` all have the same value `B_0 union B_1`; their physical
addresses are distinct, but their literal target-value menu has rank one.

## 3. The full prepared two-chain packet is obstructed

Let `G,{a},{b},F` be pairwise disjoint and prescribe the two old coatom
chains

\[
\begin{aligned}
 O_h^L&=G\cup\{a,f_1,\ldots,f_h\},\\
 O_h^R&=G\cup\{b,f_{d-h+1},\ldots,f_d\},
             &&1\le h\le d-1.                               \tag{3.1}
\end{aligned}
\]

Suppose the nonsingleton fans satisfy

\[
                  L_{h+1}=O_h^L,\qquad R_{h+1}=O_h^R.         \tag{3.2}
\]

### Theorem 3.1 (crossing bank has zero `NEW` incidence)

Every realization of (3.2) satisfies

\[
 Z\subseteq G,qquad
 \{a,b,f_1,\ldots,f_d\}\subseteq C_i
                  \quad(1\le i\le d-1).                     \tag{3.3}
\]

Consequently no destroyed crossing cell can carry any member of the
phase-swapped new chains

\[
\begin{aligned}
 N_h^L&=G\cup\{b,f_1,\ldots,f_h\},\\
 N_h^R&=G\cup\{a,f_{d-h+1},\ldots,f_d\}.
                                                                  \tag{3.4}
\end{aligned}
\]

In the canonical endpoint-transporter glue all `C_i` equal the same full
rank owner

\[
                         U=G\cup\{a,b\}\cup F.               \tag{3.5}
\]

The obstruction begins at `d=2`, where the sole crossing already contains
both `a` and `b`, while each candidate `NEW` target omits one of them.

#### Proof

The shared singleton lies in every target in (3.2), whose intersection is
`G`, proving `Z subseteq G`.  Since `a` appears in `L_2` but not at the
star, it is forced at `-1`; similarly `b` is forced at `+1`.  These two
positions lie in every crossing.

For an internal filler `f_t`, left nestedness forces a copy at `-t`, while
right nestedness forces a copy at `+(d+1-t)`.  The first belongs to `I_i`
when `i>=t`, and the second when `i<=t-1`; these cases partition all `i`.
The endpoint fillers are forced at the nearest corresponding positions.
This proves (3.3), and (3.4) then gives the zero-incidence claim.  The
literal endpoint-transporter sources contain all of `G` in every crossing,
giving (3.5). \(\square\)

Thus the conditional ledger in which the `d-1` destroyed pins are repaid
by native `NEW` cells is not instantiated by the prepared two-sided coatom
glue.  Its `2(d-1)` chain targets consume every nonsingleton fan, leaving
only the singleton star.  The net interval count `d` is still correct, but
it is not a matching-credit theorem.  A positive full packet needs a
basis-changing collar, a fan realization outside the pinned twisted-cube
catalogue, or an exterior ear.

## 4. Exact typed-singleton criterion

Fix all nonstar source letters in one phase `epsilon`.  Index by `j` every
exact carrier row, protected pin, or already assigned compiler row whose
source window contains the star.  Let `T_j^epsilon` be its required value
and `U_j^epsilon` the union of its nonstar source letters.  Define

\[
 P_*^\epsilon=\bigcap_jT_j^\epsilon,qquad
 M_*^\epsilon=\bigcup_j(T_j^\epsilon\setminus U_j^\epsilon). \tag{4.1}
\]

### Lemma 4.1 (forced-mask interval)

A nonempty star payload `Z` replays all affected carrier rows exactly if
and only if both

\[
 U_j^\epsilon\subseteq T_j^\epsilon\quad\hbox{for every affected row }j
                                                                  \tag{4.2}
\]

and

\[
                 M_*^\epsilon\subseteq Z\subseteq P_*^\epsilon. \tag{4.3}
\]

If a literal lower target `S_tau` is assigned to the singleton fan, then
`Z=S_tau`; hence the typed singleton exists in phase `epsilon` exactly when

\[
       \varnothing\ne S_\tau,\qquad
       U_j^\epsilon\subseteq T_j^\epsilon\ (\hbox{all }j),\qquad
       M_*^\epsilon\subseteq S_\tau\subseteq P_*^\epsilon,    \tag{4.4}
\]

and the fan/crossing pins with `Z=S_tau` satisfy the compatibility theorem
of Section 1.  A single literal target common to both phases must satisfy

\[
 U_j^\epsilon\subseteq T_j^\epsilon
       \quad(\epsilon\in\{0,1\},\ \hbox{all }j),\qquad
 M_*^0\cup M_*^1\subseteq S_\tau
       \subseteq P_*^0\cap P_*^1.                             \tag{4.5}
\]

#### Proof

First, `U_j union Z=T_j` forces `U_j subseteq T_j`.  The star cannot
contain a coordinate outside any affected owner, giving the upper
inclusion.  Any coordinate of `T_j` absent from the other source letters
is forced at the star, giving the lower inclusion.  Conversely, row
containment together with the two star inclusions implies
`U_j union Z=T_j` for every row.  A singleton interval has value exactly
`Z`, proving (4.4)--(4.5). \(\square\)

If `tau` denotes an abstract packet task rather than a lower target value,
the exact condition is instead that the star address belong to the task's
guarded address set in the **same** cap state.  Neither address membership
nor (4.4) follows from the scalar fan count.

In the full two-sided coatom glue, (3.3) gives the sharper local menu

\[
                   \varnothing\ne S_\tau=Z\subseteq G.        \tag{4.6}
\]

It contains no native rank-`(r-1)` `q1` target.  Thus the star is one fixed-
core typed possibility, not a programmable packet socket.

## 5. Correct address ledger and weakest live theorem

One inserted position creates `2d-1` fans and destroys `d-1` crossings.
The untyped scalar net is `d`.  If a construction has already supplied an
explicit pre/post basis bijection for the destroyed assignments, and its
two chain banks use the `2d-2` nonsingleton fans, then the singleton is the
unique fan surplus.  Assigning a typed task there consumes it, so at most
`d-1` other addresses remain.  Those addresses are useful only to the
extent certified by that separate basis bijection.

The prepared two-sided coatom glue has no such bijection by Theorem 3.1.
Therefore it supplies only the literal singleton menu (4.6), not `d-1`
additional compiler credits.

The weakest exact positive full-packet lemma is now:

1. plant a source-disjoint prepared boundary carve and an interior star
   collar which replay the carrier in each terminal phase;
2. make the two desired fan chains and all destroyed crossing pins satisfy
   the star-hidden criterion (0.1)--(1.2);
3. exhibit distinct native providers for the destroyed pins and a matching
   of all nonsingleton fan targets in the same cap state; and
4. certify either (4.4) for a literal singleton target or guarded membership
   of the star in the packet task's address set.

Only under these four hypotheses is the one-cell phase selector and typed
ear proved.  The current prepared complementary coatom glue already fails
item 2; item 3 is never reached.
No all-`k`, additive-constant, or signed-lattice conclusion is made here.

## 6. Audit

The independent replay

```text
scratch/audit_threadD_one_cell_star_phase_selector_20260801.py
scratch/threadD_one_cell_star_phase_selector_20260801.audit.json
```

checks the seam identity and interval-zero law, the asymmetric construction
(2.2)--(2.4), the two-sided obstruction (3.3)--(3.5), literal carrier
stuttering for the canonical glue, the forced-mask equivalence, and the
`1,d-1,d` address ledger.  It hash-pins and validates the two authoritative
source audits.

Dependencies:

* `MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md`;
* `MATH_THEOREM_COATOM_TWO_PHASE_BOUNDARY_CHAIN_CARVING_20260801.md`;
* `MATH_AUDIT_AD_ONE_CELL_TWO_FAN_COATOM_GLUE_AND_CROSSING_OBSTRUCTION_20260801.md`; and
* `MATH_THEOREM_AD_ONE_CELL_TWO_FAN_EXACT_EAR_HALL_CUT_20260801.md`.
