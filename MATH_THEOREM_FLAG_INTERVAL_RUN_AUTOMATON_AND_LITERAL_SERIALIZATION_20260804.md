# Flag-interval run automata and exact literal serialization

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact serialization theorem for a fixed oriented
coatom factor, fixed named coatom-rooted chains, and fixed suffix-slot
embeddings. The literal countdown problem factors into independent
`d`-state automata on the positive runs of individual coordinates. A
proof-safe lower-waste consequence is included. The theorem does not
construct an accepting flag table, a connected protected factor, a safe
opening, or an upper-complete carrier.

## 0. Outcome

Fix a cyclic simple Johnson walk

\[
 Q_0,Q_1,\ldots,Q_{N-1}\in {[k]\choose r-1},
 \qquad
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\},              \tag{0.1}
\]

with cyclic indices. Its intervening owner is

\[
                         T_{i+1}=Q_i\cup Q_{i+1}.     \tag{0.2}
\]

Assume no coordinate belongs to every `Q_i`. This is automatic when the
walk uses the complete rank-`(r-1)` layer, which is the application below;
it ensures that every positive cyclic run has a genuine entry and
departure.

At every root `Q_i`, prescribe a nonempty strict named flag

\[
 \mathcal S_i:
 S^i_1\subsetneq S^i_2\subsetneq\cdots
       \subsetneq S^i_{m_i}=Q_i,
 \qquad 1\le m_i\le d.                              \tag{0.3}
\]

Choose suffix-threshold addresses

\[
 0\le\theta^i_1<\theta^i_2<\cdots
      <\theta^i_{m_i}=d-1.                           \tag{0.4}
\]

For `x in Q_i`, let `j_i(x)` be the first member of the flag containing
`x`, and put `theta^i_0=-1`. The exact allowed-age interval of `x` at
`Q_i` is

\[
 J_i(x)=
 [\theta^i_{j_i(x)-1}+1,\theta^i_{j_i(x)}]
 \cap\mathbb Z.                                      \tag{0.5}
\]

For each positive cyclic run

\[
 R=(Q_{i_0},Q_{i_1},\ldots,Q_{i_{\ell-1}})           \tag{0.6}
\]

of one coordinate `x`, define reachable age sets by

\[
 \begin{aligned}
 \mathcal R_0(x)&=J_{i_0}(x)\cap\{0\},\\
 \mathcal R_{t+1}(x)&=J_{i_{t+1}}(x)\cap
 \left(\{0\}\cup
  \{a+1:a\in\mathcal R_t(x),\ a<d-1\}\right).
 \end{aligned}                                       \tag{0.7}
\]

Then the prescribed flags have one common literal cyclic depth-`d` source
spelling at the declared addresses if and only if

\[
                 \boxed{d-1\in\mathcal R_{\ell-1}(x)}          \tag{0.8}
\]

for every positive run of every coordinate.

This is an exact bounded-state theorem. There is no product automaton and
no additional cross-coordinate age holonomy. Once one accepting path is
chosen in every run, the source letter appended at a turn is the set of
the newborn coordinate and all surviving coordinates whose chosen next
age is zero.

For the natural right-aligned embedding

\[
                 \theta^i_j=d-m_i+j-1,              \tag{0.9}
\]

put `c_i=d-m_i`. Formula (0.5) becomes

\[
 J_i(x)=
 \begin{cases}
 [0,c_i],&x\in S^i_1,\\
 \{c_i+j-1\},&x\in S^i_j\setminus S^i_{j-1},\quad j\ge2.
 \end{cases}                                         \tag{0.10}
\]

Thus every nonminimal layer has a forced age; only the bottom core carries
age slack. This is the exact literal condition left after the joint-start
theorem has produced named owner flags and after a protected two-factor has
produced the owner/coatom incidence row.

## 1. Age sequences on one coordinate run

An age sequence on the run (0.6) is a sequence

\[
                         a_0,a_1,\ldots,a_{\ell-1}
                         \in\{0,\ldots,d-1\}          \tag{1.1}
\]

satisfying

\[
 a_0=0,\qquad a_{\ell-1}=d-1,\qquad
 a_{t+1}\in\{0,a_t+1\}
 \quad(0\le t<\ell-1),                               \tag{1.2}
\]

where `a_t+1` is allowed only when `a_t<d-1`.

The first equality says that the entering coordinate is newborn. A
surviving coordinate is either refreshed, returning to age zero, or is not
refreshed, increasing its age by one. The last equality says that the
departing coordinate occurs in the oldest of the `d` source letters.

### Lemma 1.1 (run automaton)

There is an age sequence (1.1)--(1.2) with

\[
                              a_t\in J_{i_t}(x)       \tag{1.3}
\]

for all `t` if and only if (0.8) holds.

### Proof

The set of ages reachable at the first state is exactly
`J_(i_0)(x) cap {0}`. If the reachable set at time `t` is
`mathcal R_t(x)`, the legal ages at the next state are exactly zero and
the successors `a+1` of nonterminal ages in that set. Intersecting with
the next allowed interval gives (0.7). Induction therefore identifies
`mathcal R_t(x)` with the complete reachable-age set at time `t`.
Requiring terminal age `d-1` gives (0.8). Backtracking through the
recurrence constructs a witnessing sequence. \(\square\)

In the unmarked case `J_i(x)=[0,d-1]`, the recurrence accepts exactly when
the run length is at least `d`, recovering the exact minimum-run criterion.

## 2. Exact flag-serialization theorem

For an ordered age partition

\[
 Q_i=C^i_0\mathbin{\dot\cup}\cdots
        \mathbin{\dot\cup}C^i_{d-1},                 \tag{2.1}
\]

write

\[
                         F^i_t=\bigcup_{u=0}^tC^i_u. \tag{2.2}
\]

### Theorem 2.1 (flag-interval literal serialization)

The following are equivalent.

1. There is a cyclic source word whose last-`d` union at state `i` is
   `Q_i`, whose next length-`(d+1)` owner is `T_(i+1)`, and for which

   \[
                         F^i_{\theta^i_j}=S^i_j
                         \qquad(1\le j\le m_i).       \tag{2.3}
   \]

2. Every positive coordinate run satisfies (0.8).

Moreover, when these conditions hold, one source word can be reconstructed
independently from accepting paths of the run automata.

### Proof: necessity

Given a source word, let `a_i(x)` be the age of `x` in the last-`d` state
`Q_i`. Entry, survival, refresh, and departure give (1.2) on every
positive run.

Fix `x in Q_i`, and let `j=j_i(x)`. Equation (2.3) says that `x` is absent
from `F^i_(theta^i_(j-1))` when `j>1`, and present in
`F^i_(theta^i_j)`. Since `F^i_t` is exactly the set of coordinates of age
at most `t`,

\[
             \theta^i_{j-1}<a_i(x)\le\theta^i_j.     \tag{2.4}
\]

For `j=1` the lower inequality is vacuous and `theta^i_0=-1` gives the
same formula. Thus `a_i(x) in J_i(x)`. Lemma 1.1 proves (0.8).

### Proof: sufficiency and reconstruction

For every positive run of every coordinate, choose one accepting path
from Lemma 1.1. At state `i`, put a present coordinate `x` in `C^i_t`
exactly when its selected age is `t`. The positive runs of one coordinate
are disjoint, and different coordinates do not share age variables, so
these choices define the partitions (2.1) simultaneously.

At the transition `Q_i -> Q_(i+1)`, the departing coordinate `alpha_i` is
at the end of its positive run and therefore has age `d-1`. Every
surviving coordinate either has next age zero or has next age one larger
than its old age. The entering coordinate `beta_i` begins its run with age
zero. Define the next source letter by

\[
 B_{i+1}=\{\beta_i\}\cup
 \{x\in Q_i\cap Q_{i+1}:a_{i+1}(x)=0\}.             \tag{2.5}
\]

It is nonempty. Shifting the old `d` letters and appending (2.5) produces
exactly the new age partition: nonrefreshed survivors shift up one age,
refreshed survivors return to zero, `alpha_i` leaves with the dropped
oldest letter, and `beta_i` is born. Hence the last-`d` union is `Q_(i+1)`
and the intervening length-`(d+1)` union is

\[
                         Q_i\cup\{\beta_i\}=T_{i+1}. \tag{2.6}
\]

It remains to verify the named flags. If `x in S^i_j`, then
`j_i(x)<=j`, so (0.5) gives `a_i(x)<=theta^i_j`. If
`x in Q_i-S^i_j`, then `j_i(x)>j`, so
`a_i(x)>theta^i_j`. Therefore the coordinates of age at most
`theta^i_j` are exactly `S^i_j`, proving (2.3). \(\square\)

### Corollary 2.2 (right-aligned forced-tail criterion)

Under (0.9), every difference block

\[
                         S^i_j\setminus S^i_{j-1}
                         \qquad(j\ge2)               \tag{2.7}
\]

has the forced age `c_i+j-1`. Therefore, if a surviving coordinate belongs
to a nonminimal block at the next root, its positive forced age must be
exactly one more than its old age. A reset is possible only when zero lies
in the next allowed interval. All other positive-to-positive age changes
are impossible.

The bottom core `S^i_1` is not unstructured: its coordinates still have to
follow the run recurrence inside the interval `[0,c_i]`. The recurrence,
not a separate rank count, is the complete compatibility test.

## 3. Relation to joint-start flags and protected factors

The joint-start orbit theorem produces literal named inclusion flags in
distinct owners. On the odd central face, complete coatom use assigns one
flag to every `Q in binom([k],r-1)`, and ordinary middle-level incidence
matching assigns distinct rank-`r` owners. A protected spanning two-factor
then chooses predecessor/successor incidences.

Those facts do not yet imply a source word. After orienting the factor,
Theorem 2.1 says that the exact remaining serialization premise is:

\[
 \boxed{
 \begin{array}{c}
 \text{choose one suffix-slot embedding of every named flag so that}\\
 \text{every coordinate-run automaton (0.7) accepts.}
 \end{array}}                                        \tag{3.1}
\]

If the protected factor has several cycles, (3.1) spells one cyclic source
component on each factor component. It does not join those components.
One-copy chronology additionally requires either one factor component or
literal, owner-palette-preserving component exchanges whose new arcs also
pass (0.7). Thus protected two-factor extension and literal serialization
are distinct exact rows.

Condition (3.1) has bounded local state: each automaton has only `d` ages,
and the automata are independent after the flag addresses and factor are
fixed. It is not a claim that the simultaneous choice of the factor,
flags, and addresses is easy or always feasible.

## 4. Exact lower-waste transfer

Let

\[
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},
 \qquad |\mathcal L|=\Lambda,                        \tag{4.1}
\]

and suppose a selected family of prescribed flags is target-disjoint and
contains at least `Lambda-C` members. Theorem 2.1 realizes every one of
those members as a literal short suffix occurrence.

Now make the following additional, explicit linear-opening assumptions.

1. The cyclic spelling is opened and, if needed, modified by the mandatory
   two-sided collar construction without changing a declared bank of at
   least `Lambda-C` marked occurrences. Any destroyed mark has already
   been replaced by a distinct declared boundary occurrence inside that
   bank.
2. The final owner path has `W>2d`, `r>=2d`, and the residence and halo
   hypotheses of the two-sided desaturation theorem.
3. Any protected pin halo is disjoint from the opening collars as required
   by that theorem.

### Theorem 4.1 (serialization-to-waste transfer)

Under these assumptions the final linear antecedent `A` satisfies

\[
                         \boxed{D_A\le\sigma+C}.      \tag{4.2}
\]

Equivalently, its strict-lower endpoint-chain support has size at least
`Lambda-C`.

### Proof

The mandatory collar theorem gives `R_A=0`. The zero-local-plateau theorem
makes every fixed-right-endpoint family a strict chain and gives

\[
 D_A=(\Lambda+\sigma)-
       \left|\bigcup_j\mathcal K_j\right|.           \tag{4.3}
\]

Every retained marked target is a member of that union, and the marks are
target-disjoint. Therefore the support in (4.3) is at least
`Lambda-C`, proving (4.2). Exact distinct lower pins only reclassify the
same duplicate term and do not change the conclusion. \(\square\)

The opening premise in item 1 is load-bearing. A cyclic spelling followed
by an arbitrary cut or collar replacement can destroy marked suffix
occurrences near the cut. The theorem does not infer a collar-compatible
opening from target counts, factor connectedness, or run acceptance.

## 5. Endpoint apertures are not sufficient

The run recurrence detects a real obstruction missed by birth/departure
pins. Take `d=2` and one turn

\[
 Q=\{1,2,4\},\qquad Q'=\{1,3,4\}
             =Q-\{2\}+\{3\}.                       \tag{5.1}
\]

Use the full right-aligned flags

\[
                  \{1\}\subset Q,
             \qquad\{3\}\subset Q'.                \tag{5.2}
\]

The departing coordinate `2` lies in the terminal difference
`Q-{1}`, and the newborn `3` lies in the next birth core `{3}`. Thus the
usual endpoint aperture conditions pass.

However coordinate `4` has forced age one at both states. Since it
survives the turn, its next age must reset to zero; the formal increment
would be two and is forbidden at depth `d=2`. Neither gives the required
age one. Equivalently, the new positive-age block `{1,4}` is
not contained in the old zero-age block `{1}`. Hence (0.7) rejects this
turn.

The obstruction is local: once these two flags and this directed turn are
fixed, choices on all other turns cannot repair the failed transition.
Therefore any implication which retains only the rows displayed below is
false without (3.1):

\[
 \text{named owner flags + resident protected two-factor
       + endpoint birth/departure pins}
 \Longrightarrow \text{literal source word}.        \tag{5.3}
\]

## 6. Proof-safe frontier

The named containment and serialization rows now separate exactly:

\[
 \begin{array}{c}
 \text{surplus type table}\\
 \Downarrow\\
 \text{exact named owner flags (joint-start orbit lift)}\\
 \Downarrow\quad\text{requires (3.1)}\\
 \text{literal source component(s) (this theorem)}\\
 \Downarrow\quad\text{requires connectedness and a safe opening}\\
 \text{one linear desaturated chronology with }D_A\le\sigma+O(1).
 \end{array}                                         \tag{6.1}
\]

Theorem 2.1 removes any hidden global age holonomy after the factor, flag
addresses, and named flags are fixed. It does not prove the correlated
selection (3.1). That is the exact remaining physical-aperture theorem:

> co-select the complete-layer named flag matching and the protected
> oriented owner/coatom factor so that all coordinate-run automata accept,
> the selected factor has one or boundedly repairable components, and one
> collar-compatible opening retains `Lambda-O(1)` distinct marks.

No rank-only transportation theorem, ordinary owner Hall theorem, or
endpoint aperture test implies this statement.

## 7. Dependencies

- `MATH_THEOREM_JOINT_START_SURPLUS_ORBIT_LIFT_AND_NAMED_COLLAR_CHAINIZATION_20260804.md`;
- `MATH_THEOREM_AGE_FLAG_RUN_CRITERION_AND_FULL_FLAG_REFINEMENT_20260802.md`;
- `MATH_THEOREM_ODD_ONECOPY_COATOM_MIDDLELEVELS_PATH_NORMAL_FORM_20260802.md`;
- `MATH_THEOREM_PINNED_MAXIMAL_ENVELOPE_GLOBAL_EXTENSION_AND_WASTE_IDENTITY_20260804.md`;
- `MATH_THEOREM_TWO_SIDED_MANDATORY_COLLAR_DESATURATION_AND_ZERO_RANK_LEAKAGE_20260804.md`;
- `MATH_THEOREM_ZERO_LOCAL_PLATEAU_AND_CROSS_ENDPOINT_COLLISION_NORMAL_FORM_20260804.md`.
