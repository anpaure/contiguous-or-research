# Pinned maximal envelopes, global halo extension, and the exact lower-deck waste identity

**Date:** 2026-08-04
**Method:** pure mathematics; no computation, search, or solver
**Status:** unconditional inverse-fibre and fixed-word counting theorems,
plus an exact halo-patching corollary for the authenticated one-phase
`Ibc/Ica` rays.  The result proves that the displayed ray pins extend to a
global antecedent once their complete affected-owner halo is planted in a
resident flat Johnson carrier.  It does not construct a one-copy antecedent
whose entire strict-lower deck is complete.

## 0. Outcome

For fixed owner requirements and exact target/cell pins, there is a unique
coordinatewise largest possible source word: intersect every owner and pin
label whose interval contains the position.  The pinned inverse fibre is
nonempty if and only if this maximal word is nonempty and realizes every
declared owner and pin.  Thus inverse existence has no hidden search layer.

For a depth-`d` resident flat Johnson carrier the unpinned maximal envelope
is automatically nonempty and realizes every owner.  A local pinned word
therefore patches globally provided it contains the complete halo of every
owner affected by a pin.  Applied to the authenticated `Ibc/Ica` phase, this
proves global extension of all `2(d-1)` forced ray facts under the explicit
halo hypothesis below.

After an antecedent is fixed, the remaining lower gate has an exact scalar
form.  Let `sigma` be the excess number of short intervals over strict-lower
targets.  The number of missing lower targets is

\[
 \boxed{\text{missing}=\text{duplicate lower occurrences}
              +\text{rank-}r\text{ short cells}-\sigma.}       \tag{0.1}
\]

With forced pins, extra occurrences of pinned target values are an
additional waste term.  This is the precise one-copy obstruction left after
the fixed-word Hall collapse.

## 1. The maximal pinned-envelope criterion

Let `P` be a finite position set.  Let

\[
                 (T_i,I_i)\qquad(i\in\mathcal I)              \tag{1.1}
\]

be owner requirements, and let

\[
                 \Pi=\{(S_a,C_a):a\in\mathcal A\}             \tag{1.2}
\]

be exact target/cell pins.  All labels are subsets of one ground set
`Omega`.  Define

\[
 E_p^\Pi=
 \bigcap_{i:p\in I_i}T_i\ \cap\!
 \bigcap_{a:p\in C_a}S_a,                                   \tag{1.3}
\]

where an empty intersection is `Omega`.  A pinned antecedent is a word
`A=(A_p)_(p in P)` satisfying

\[
 \varnothing\ne A_p\subseteq E_p^\Pi,                        \tag{1.4}
\]

\[
 \bigcup_{p\in I_i}A_p=T_i\quad(i\in\mathcal I),
 \qquad
 \bigcup_{p\in C_a}A_p=S_a\quad(a\in\mathcal A).             \tag{1.5}
\]

### Theorem 1.1 (maximal-envelope equivalence)

The pinned antecedent fibre is nonempty if and only if

\[
 E_p^\Pi\ne\varnothing\quad(p\in P),                         \tag{1.6}
\]

\[
 \bigcup_{p\in I_i}E_p^\Pi=T_i\quad(i\in\mathcal I),
 \qquad
 \bigcup_{p\in C_a}E_p^\Pi=S_a\quad(a\in\mathcal A).        \tag{1.7}
\]

When these conditions hold, the maximal word

\[
                            A_p^{\max}=E_p^\Pi                 \tag{1.8}
\]

is itself a pinned antecedent and contains every other pinned antecedent
coordinatewise.

#### Proof

Every pinned antecedent obeys (1.4), so it is contained in (1.8).  Its
nonemptiness gives (1.6).  On an owner interval, (1.3) gives
`E_p^Pi subseteq T_i`; on a pinned interval it gives
`E_p^Pi subseteq S_a`.  Since the antecedent contained in the envelope
already has the required union, the envelope union is squeezed to the same
label.  This proves necessity of (1.7).

Conversely, (1.6)--(1.7) say exactly that (1.8) is nonempty and satisfies
(1.5).  Maximality follows from (1.4).  \(\square\)

### Remark 1.2

The theorem concerns inverse existence only.  A smaller subword of the
maximal envelope can have many more useful strict-lower interval values.
Thus replacing the terminal optimization by `A^max` is not justified.

## 2. An exact local-to-global halo patch

Write `E_p` for the unpinned owner envelope.  Put

\[
 J=\bigcup_{a\in\mathcal A}C_a,
 \qquad
 \mathcal I_J=\{i:I_i\cap J\ne\varnothing\},
 \qquad
 H=J\cup\bigcup_{i\in\mathcal I_J}I_i.               \tag{2.1}
\]

The set `H` is the complete source-position halo of the affected owners.

### Theorem 2.1 (maximal-envelope halo patching)

Assume the unpinned envelope satisfies

\[
 E_p\ne\varnothing\quad(p\in P),
 \qquad
 \bigcup_{p\in I_i}E_p=T_i\quad(i\in\mathcal I).      \tag{2.2}
\]

Suppose there is a local word `(L_p)_(p in H)` such that

\[
 \varnothing\ne L_p\subseteq E_p^\Pi\quad(p\in H),    \tag{2.3}
\]

\[
 \bigcup_{p\in I_i}L_p=T_i\quad(i\in\mathcal I_J),
 \qquad
 \bigcup_{p\in C_a}L_p=S_a\quad(a\in\mathcal A).     \tag{2.4}
\]

Then the global pinned fibre is nonempty; in fact its maximal envelope
`E^Pi` is a global pinned antecedent.

#### Proof

For `p in H`, (2.3) proves `E_p^Pi` nonempty.  If `p notin H`, then
`p notin J`, so no pin contains `p` and `E_p^Pi=E_p`, which is nonempty by
(2.2).

For an affected owner, (2.3)--(2.4) and
`E_p^Pi subseteq T_i` squeeze the envelope union to `T_i`.  For an
unaffected owner, `I_i cap J` is empty, hence `E_p^Pi=E_p` throughout
`I_i`, and (2.2) applies.  The same squeeze using (2.4) proves every pin
union.  Theorem 1.1 finishes.  \(\square\)

### Boundary warning

It is not enough to specify a local word only on the pin cells `J`.  To use
Theorem 2.1 one must verify (2.3) on the whole set `H` and (2.4) for every
owner whose window meets a pin.  When a local packet word is imported from
a finite template, every global owner window containing a position used by
that local word must agree with the template owner.  Equivalently, the
template must contain the complete owner-of-source halo, not merely the
visible two ray intervals.  This is the exact opening-boundary interface.

## 3. Resident flat Johnson carriers have exact maximal envelopes

Let the source positions be `0,...,W+d-1`, and put

\[
                         I_i=[i,i+d]\qquad(0\le i<W).  \tag{3.1}
\]

Suppose each `T_i` has rank `r`, consecutive owners differ by at most one
deletion and one insertion, `d<r`, and every positive run of every
coordinate in the owner-incidence word has length at least `d+1`.

### Theorem 3.1 (resident Johnson maximal inverse)

The unpinned maximal envelope

\[
                         E_p=\bigcap_{i:p\in I_i}T_i   \tag{3.2}
\]

is nonempty at every source position and realizes every owner:

\[
                         \bigcup_{p\in I_i}E_p=T_i.   \tag{3.3}
\]

#### Proof

The owner indices whose windows contain a fixed `p` form a consecutive
interval of length at most `d+1`.  Across each owner transition at most one
coordinate is deleted.  Their intersection therefore has rank at least
`r-d>0`, proving nonemptiness.

Fix `x in T_i`, and let `[alpha,beta]` be its positive owner run containing
`i`.  A source position `p` can belong to the envelope of this run whenever

\[
 p\in P_x=[\ell_x,u_x],\qquad
 \ell_x=\begin{cases}0,&\alpha=0,\\ \alpha+d,&\alpha>0,\end{cases}
 \quad
 u_x=\begin{cases}W+d-1,&\beta=W-1,\\ \beta,&\beta<W-1.
 \end{cases}                                           \tag{3.4}
\]

Indeed, every owner window containing such a `p` has index in
`[alpha,beta]`.  Residence gives `beta-alpha+1>=d+1` for an internal run.
More directly, `ell_x<=i+d` and `u_x>=i`, so

\[
                         I_i\cap P_x\ne\varnothing.   \tag{3.5}
\]

Choose `p` in this intersection.  Then `x in E_p`, proving that the union
in (3.3) contains `T_i`; the reverse containment follows from (3.2).
\(\square\)

### Corollary 3.2 (global extension of one aligned `Ibc/Ica` phase)

Let a carrier satisfy Theorem 3.1 and contain one authenticated aligned
`Ibc/Ica` phase.  Let `Pi^epsilon` be its `2(d-1)` exact ray pins.  Assume
the planted expanded packet includes the complete halo `H` in (2.1), and
the authenticated local antecedent restricted to `H` respects every global
owner window covering a position of `H`.

Then

\[
                         \mathcal A(T,\Pi^\epsilon)\ne\varnothing. \tag{3.6}
\]

In particular, this holds for an interior planting whose full owner-of-
source halo agrees with the complete expanded packet chronology.  It is
not asserted for an opening that clips that halo unless the clipped owner
rows are checked separately.

#### Proof

Theorem 3.1 gives (2.2).  The ambient `Ibc/Ica` theorem supplies a nonempty
exact local antecedent realizing all ray pins and every affected owner.
The stated full-halo compatibility makes its letters subsets of the global
pinned envelopes, so (2.3)--(2.4) hold.  Apply Theorem 2.1.  \(\square\)

## 4. Functional occurrence waste

Continue with the flat setting (3.1), and let

\[
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad \Lambda=|\mathcal L|.                         \tag{4.1}
\]

Let `C_d` be all physical intervals of lengths `1,...,d`.  Their number is

\[
 N_d=d(W+d)-\binom d2=dW+\binom{d+1}{2}
     =\Lambda+\sigma,                                 \tag{4.2}
\]

where `sigma>=0` is the scalar short-cell slack.  Fix any nonempty exact
antecedent `A` of the rank-`r` owner row.  Every cell in `C_d` is contained
in some length-`d+1` owner window, so its OR has rank at most `r`.

For `S in L`, let `m_A(S)` be its number of occurrences in `C_d`.  Define

\[
 M_A=|\{S\in\mathcal L:m_A(S)=0\}|,\qquad
 D_A=\sum_{S\in\mathcal L}(m_A(S)-1)_+,               \tag{4.3}
\]

and let `R_A` be the number of cells in `C_d` whose OR has rank exactly
`r`.

### Theorem 4.1 (exact lower-deck waste identity)

\[
                         \boxed{M_A=D_A+R_A-\sigma.}   \tag{4.4}
\]

Consequently `D_A+R_A>=sigma`, and the strict-lower deck is complete if
and only if

\[
                              D_A+R_A=\sigma.          \tag{4.5}
\]

#### Proof

Every short cell has either a strict-lower value or a rank-`r` value.  The
number of strict-lower-valued cells is

\[
 \sum_{S\in\mathcal L}m_A(S)
   =(\Lambda-M_A)+D_A.                                \tag{4.6}
\]

Hence

\[
 \Lambda+\sigma=N_d=(\Lambda-M_A)+D_A+R_A,
\]

which rearranges to (4.4).  \(\square\)

## 5. Forced-ray waste identity

Let `Pi subseteq H_A` be an exact partial matching of size `p`, with target
set `L_*` and cell set `C_*`.  Delete those targets and cells.  For a
residual target `S in L minus L_*`, put

\[
 m_A^\Pi(S)=
 |\{C\in\mathcal C_d\setminus C_*:\operatorname{OR}_A(C)=S\}|. \tag{5.1}
\]

Define

\[
 M_A^\Pi=|\{S\in\mathcal L\setminus L_*:m_A^\Pi(S)=0\}|,
 \quad
 D_A^\Pi=\sum_{S\in\mathcal L\setminus L_*}
                  (m_A^\Pi(S)-1)_+,                  \tag{5.2}
\]

\[
 Q_A^\Pi=
 |\{C\in\mathcal C_d\setminus C_*:
              \operatorname{OR}_A(C)\in L_*\}|,      \tag{5.3}
\]

and let `R_A^Pi` count the remaining rank-`r` short cells.

### Theorem 5.1 (exact pinned waste identity)

\[
             \boxed{M_A^\Pi=D_A^\Pi+Q_A^\Pi+R_A^\Pi-\sigma.} \tag{5.4}
\]

For the one-phase ray matching, the left side is exactly the terminal
compiler deficiency.  Thus the one-phase lower gate has no residual Hall
term: it is the construction of a pinned antecedent with

\[
             D_A^\Pi+Q_A^\Pi+R_A^\Pi\le\sigma+C.      \tag{5.5}
\]

#### Proof

After deleting the `p` forced cells there are
`Lambda-p+sigma` cells.  They split into

* `(Lambda-p-M_A^Pi)+D_A^Pi` residual-target occurrences;
* `Q_A^Pi` extra occurrences of forced target values; and
* `R_A^Pi` rank-`r` cells.

Equating the two counts gives (5.4).  The fixed-word functional-occurrence
theorem identifies `M_A^Pi` with the residual matching deficiency, proving
(5.5).  \(\square\)

## 6. What the earlier relaxations do and do not prove

The arbitrary ideal `(d+1)`-slot theorem proves that the ray pins do not
violate containment Hall.  The stationary rotor and pull-clock theorems
prove that the required rank marginals have balanced fractional literal
trace circulations.  The guard-pruning theorem exactly characterizes a
candidate bank before one literal word is selected.

After Corollary 3.2 and Theorem 5.1, none of those results leaves a second
post-selection Hall gate.  Their unresolved common content is the same
integral one-copy problem:

> choose one owner-coloured rooted trace/Euler realization extending the
> ray pins whose literal short-cell waste is at most `sigma+O(1)`.

Fractional rank balance does not control the duplicate terms
`D_A^Pi,Q_A^Pi`, and ideal slots do not control `R_A^Pi` or physical
prefix/suffix chainization.  Equation (5.4) is the sharp decomposition of
the remaining obstruction.

## 7. Dependencies

- `MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`
- `MATH_THEOREM_SERIAL_ONE_PHASE_FORCED_RAY_TERMINAL_REDUCTION_20260804.md`
- `MATH_THEOREM_FIXED_WORD_FUNCTIONAL_OCCURRENCE_AND_ONE_PHASE_HALL_COLLAPSE_20260804.md`
- `MATH_THEOREM_L_PINNED_TRIANGULAR_ROOTED_TRACE_AND_PRIVATE_COMMONCAP_20260801.md`
- `MATH_THEOREM_R_COMMON_CAP_GUARD_PRUNING_ROBUST_HALL_LIFT_20260731.md`
- `MATH_THEOREM_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md`
