# Serial safety reduces the aligned compiler to one terminal phase

**Date:** 2026-08-04
**Method:** pure mathematics; no computation, search, or solver
**Status:** exact conditional reduction, corrected by the fixed-word
functional-occurrence theorem.  The two packet phases need neither a common
compiler nor a common terminal type.  At the final chronology one may choose
one phase and force its literal `Ibc/Ica` ray occurrences.  Once one literal
antecedent is fixed, there is no further residual Hall interaction: the
remaining deficiency is exactly the number of absent strict-lower values.
Global inverse extension follows from the maximal-envelope halo theorem for
an interior resident planting.  Complete lower-deck construction and
regenerative reachability remain open.

## 0. Outcome

Let `Gamma_(k,d)` be the safe-carrier graph from the serial coatom theorem.
Along a walk in this graph, the owner permutation, Johnson topology,
residence, and complete upper interval-union deck are preserved, while the
lower compiler is allowed to fail.  It is solved only at the terminal
carrier.

Suppose a terminal carrier contains one of the two aligned `Ibc/Ica` phases.
For that phase the ambient birail theorem gives `2(d-1)` distinct strict-
lower target occurrences:

\[
 X_j^\epsilon=J\cup\{x_\epsilon\}\cup P_j,
 \qquad
 Y_j^\epsilon=J\cup\{y_\epsilon\}\cup S_j,
 \qquad 1\le j<d.                                      \tag{0.1}
\]

These occurrences themselves form a forced partial compiler matching.  For
their **target-coverage role** in a final word they require neither the
opposite packet phase nor a polarized native terminal socket.  After one
literal antecedent is fixed, each interval address has one OR value, so
distinct target values cannot compete for that address.  Contracting the
forced facts creates zero matching surcharge.  The exact remaining
condition is simply coverage of every residual strict-lower value by some
short interval of the same antecedent.

The resulting sufficient criterion is

\[
 \boxed{
 \nu(k)\le B(k)+u(T_0)+
 \min_{T\in\operatorname{Comp}_\Gamma(T_0)}
 \min_{\epsilon\in\mathcal E(T)}
       \Lambda_{\rm 1ph}(T,\epsilon).}                 \tag{0.2}
\]

Here `E(T)` is the set of aligned phase occurrences present in `T`, and
`Lambda_(1ph)` is the minimum number of absent strict-lower values defined
below.  In particular, a uniform bound `Lambda_(1ph)<=C` on an
upper-complete component implies `nu(k)<=B(k)+C`.

The ideal `(d+1)`-slot theorem already shows that these `O(d)` forced ray
pins cause no asymptotic **containment-SDR** obstruction.  The maximal-
envelope halo theorem further shows that they extend to a global antecedent
inside an interior resident planting.  What remains is physical and
one-copy: choose such an antecedent whose short-interval OR map is
surjective onto the complete strict-lower family.

## 1. One terminal phase and its forced rays

Fix a safe terminal carrier

\[
                         T=(T_0,\ldots,T_{W-1})
\]

and one aligned packet occurrence in phase `epsilon in {0,1}`.  Let
`I_i` be the length-`d+1` source window realizing owner `T_i`, and put

\[
 E_p(T)=\bigcap_{i:p\in I_i}T_i.                       \tag{1.1}
\]

Let `L` be the strict-lower target family and `C_d` the bank of physical
interval addresses of length at most `d`.  The aligned ambient theorem
provides pairwise distinct addresses `C_j^X,C_j^Y` with

\[
 \operatorname{OR}_{A^\epsilon}(C_j^X)=X_j^\epsilon,
 \qquad
 \operatorname{OR}_{A^\epsilon}(C_j^Y)=Y_j^\epsilon.  \tag{1.2}
\]

The targets in (1.2) are distinct.  Indeed, the prefix fillers strictly
increase with `j`, the suffix fillers strictly decrease, and prefix and
suffix targets contain the different active labels `x_epsilon` and
`y_epsilon`.  Since a coatom owner has rank

\[
 r=|K|+3+(d+1),
\]

one has `|J|=r-d-2`, and hence

\[
 |X_j^\epsilon|=r-d-1+j\le r-2,
 \qquad
 |Y_j^\epsilon|=r-j-1\le r-2.                       \tag{1.2a}
\]

Thus they lie in `L`.

Define the forced ray matching

\[
 \Pi^\epsilon=
 \{(X_j^\epsilon,C_j^X),(Y_j^\epsilon,C_j^Y):1\le j<d\}.
                                                               \tag{1.3}
\]

It has size `2(d-1)`.  No native socket occurrence is included in (1.3).
If a separate topology, compensation, or routing theorem needs the native
socket bank, its noncoalescible footprint must instead be charged as in
Section 4.

## 2. Exact pinned antecedent fibre

For an arbitrary legal partial target-to-cell matching `Pi`, define its
pinned envelope

\[
 E_p^\Pi=E_p(T)\cap
   \bigcap_{(S,C)\in\Pi:\ p\in C}S.                  \tag{2.1}
\]

Let `A(T,Pi)` be the set of words `A=(A_p)` satisfying

\[
 \varnothing\ne A_p\subseteq E_p^\Pi,                \tag{2.2}
\]

\[
 \bigcup_{p\in I_i}A_p=T_i\quad\text{for every owner row }i, \tag{2.3}
\]

and

\[
 \bigcup_{p\in C}A_p=S\quad\text{for every }(S,C)\in\Pi.
                                                               \tag{2.4}
\]

Thus `A(T,Pi)` is the exact **global** nonempty depth-`d` inverse fibre
extending the pins.  It is not merely the collection of pointwise allowed
caps, nor is its nonemptiness implied by the local aligned antecedent alone.
Equations (2.3)--(2.4) include every required owner and pin trace across the
whole carrier.

For `A in A(T,Pi)`, let `H_A^Pi` be the realized residual graph with left
shore `L minus L(Pi)` and right shore `C_d minus C(Pi)`:

\[
 (S,C)\in H_A^\Pi
 \quad\Longleftrightarrow\quad
 C\notin C(\Pi),\ S\notin L(\Pi),\
 \bigcup_{p\in C}A_p=S.                               \tag{2.5}
\]

Every edge in this graph is already exact in the same literal word `A`.
Hence any matching in `H_A^Pi` coexists with all pins; no second common-cap
choice remains.

Define its exact residual deficiency

\[
 \delta(A,\Pi)=
 \max_{Z\subseteq L\setminus L(\Pi)}
 \bigl(|Z|-|N_{H_A^\Pi}(Z)|\bigr)_+.                 \tag{2.6}
\]

Finally put

\[
 \Lambda_{\rm 1ph}(T,\epsilon)=
 \min_{A\in\mathcal A(T,\Pi^\epsilon)}
                    \delta(A,\Pi^\epsilon),          \tag{2.7}
\]

with value `+infinity` when the pinned inverse fibre is empty.

### Theorem 2.1 (one-phase forced-ray terminal compiler)

For any terminal carrier and phase as above, a depth-`d` antecedent
realizing all but `c` strict-lower targets while containing every aligned
ray pin exists if and only if

\[
                     \Lambda_{\rm 1ph}(T,\epsilon)\le c.       \tag{2.8}
\]

#### Proof

Choose `A` in the pinned fibre.  Every physical address has the unique
value `OR_A(C)`, so the families of occurrence addresses of distinct target
values are disjoint.  Choose one address for every residual target which
occurs.  These addresses automatically form a matching, and adjoining
`Pi` covers every pinned target.

Conversely, any compiler containing `Pi` has a realizing antecedent `A` in
the fibre (2.2)--(2.4).  A target not occurring in that word cannot be
covered.  The fixed-word functional-occurrence theorem identifies (2.6)
with the number of absent residual target values.  Minimizing over `A`
proves the equivalence.  \(\square\)

Appending each uncovered target as one singleton letter covers it and does
not destroy any old interval witness.  Thus the deficiency in (2.6) is an
actual additive length charge.

### Corollary 2.2 (forced facts are neutral in a fixed word)

Let `H_A` be the full exact target/occurrence graph of the same word before
contracting `Pi`.

Every forced address has the value of its forced target.  Consequently,
for every residual `Z`,

\[
 N_{H_A}(Z)\cap C(\Pi)=\varnothing,
 \qquad
 N_{H_A^\Pi}(Z)=N_{H_A}(Z).                         \tag{2.9}
\]

Hence

\[
 \boxed{
 \delta(A,\Pi)=\delta(A,\varnothing)
 =|L\setminus\operatorname{Deck}_{\le d}(A)|.}       \tag{2.10}
\]

#### Proof

If a forced address were adjacent to a residual target, its unique literal
OR value would equal both that residual target and its forced target,
contrary to target disjointness.  This proves (2.9).  In a functional
occurrence graph the deficiency is exactly the number of target values with
empty occurrence fibre.  Every pinned target occurs at its forced address,
so the absent all-target values are precisely the absent residual values,
proving (2.10).  \(\square\)

Thus every exact forced ray matching extends automatically to a maximum
matching of the fixed-word occurrence graph.  It extends to a saturating
matching exactly when the word's strict-lower deck is complete.  The pins
create no separate `O(d)` matching loss.

## 3. Serial one-phase bound

### Theorem 3.1 (serial terminal-phase reduction)

Let `T_0` be a safe starting carrier.  For every reachable terminal carrier
`T`, let `E(T)` be its aligned packet-phase occurrences for which (1.3) is
available.  Then (0.2) holds.

#### Proof

The serial-safe theorem preserves the full upper interval-union support and
therefore preserves `u(T_0)` along every walk.  Choose a reachable `T`, a
phase occurrence `epsilon`, and `A` attaining (2.7).  Theorem 2.1 gives a
literal lower compiler missing exactly `Lambda_(1ph)` targets.  The exact
word-from-carrier augmentation theorem then gives length

\[
 B(k)+u(T_0)+\Lambda_{\rm 1ph}(T,\epsilon).
\]

Minimize over the reachable choices.  \(\square\)

### Corollary 3.2 (`B+O(1)` criterion)

If, for every sufficiently large `k`, an upper-complete safe component
contains one terminal aligned phase satisfying

\[
                     \Lambda_{\rm 1ph}(T,\epsilon)\le C
\]

for an absolute `C`, then

\[
                              \nu(k)\le B(k)+C.         \tag{3.1}
\]

No condition on a compiler in the opposite phase occurs in this criterion.
The pointwise union of the two phase antecedents need not be exact, and no
phase-common matching or phase-common terminal type is required.

## 4. Fact coalescence and optional native bundles

Suppose a separate theorem retains deterministic native socket bundles.
Inside one fixed phase, contract every bundle occurrence fact which is also
its own ordinary target, owner, or upper witness.  Literal occurrence-fact
coalescence charges such an address once.

Let `E_*` be the resulting forced target/cell facts and let `B_*` be every
remaining noncoalescible occurrence capacity in the selected bundles.  Put
`Pi'=Pi^epsilon union E_*`, after deleting duplicate facts.  Replace (2.5)
by

\[
 (S,C)\in H_{A,B_*}^{\Pi'}
 \Longleftrightarrow
 (S,C)\in H_A^{\Pi'}\text{ and }C\notin B_*.          \tag{4.1}
\]

The exact deficiency remains (2.6) with this graph.  This is precisely the
forced-edge contraction theorem.  There is no extra capacity charge for a
coalesced semantic role, but every route interior or exclusive occurrence
in `B_*` remains charged.  Even here, after `A` and `B_*` are fixed, the
graph is functional on its surviving right addresses.  Its deficiency is
the number of residual target values having no surviving occurrence; there
is still no competition between two different values for one address.

The strongest final compiler reduction is the direct-ray face `B_*=emptyset`:
if native sockets serve no independent physical purpose, omit them and use
the literal ray pins (1.3) themselves.  In the present gain/compensation
architecture those sockets were introduced to help prove complementary
compiler coexistence, so this face is a genuine alternative branch, not an
automatic simplification of that router proof.

## 5. Pre-word guard pruning versus fixed-word coverage

The fibre formulation above can be stated without presupposing the final
word.  Fix the pinned envelope (2.1), and let `G^Pi` be any marginal
target/cell graph built from it.  For an admissible nonempty guard word `A`
satisfying (2.3)--(2.4), retain exactly its realized edges, obtaining
`H_A^Pi subseteq G^Pi`.  Put

\[
 \sigma_{G^\Pi}(Z)=|N_{G^\Pi}(Z)|-|Z|,
\qquad
 \ell_A(Z)=|N_{G^\Pi}(Z)\setminus N_{H_A^\Pi}(Z)|.    \tag{5.1}
\]

Then

\[
 \boxed{
 \delta(A,\Pi)\le C
 \iff
 \ell_A(Z)\le\sigma_{G^\Pi}(Z)+C
 \quad\text{for every residual target set }Z.}       \tag{5.2}
\]

This is only the algebraic identity

\[
 |N_{H_A^\Pi}(Z)|=|N_{G^\Pi}(Z)|-\ell_A(Z).
\]

Before a literal word is chosen, this identity can be useful for selecting
a compatible guard word from a multivalued candidate graph.  It is not an
additional acceptance gate afterward.  Once `A` is fixed, every right
address has its unique OR value and all cuts collapse to singleton target
absence:

\[
 \delta(A,\Pi)
 =|\{S\in L\setminus L(\Pi):
       S\notin\operatorname{Deck}_{\le d}(A)\}|.     \tag{5.3}
\]

Thus guard pruning is a construction language for the terminal word.  The
remaining theorem is literal lower-deck surjectivity of one pinned word,
not a further all-cut Hall bound.

## 6. Ideal-pin robustness: what is already removed

The two ray families have a legal realization in the ideal `(d+1)`-slot
owner graph.  In the notation of the ambient theorem, the largest prefix
address is

\[
 [s+d+2,s+2d]\subseteq[s+d+1,s+2d+1],               \tag{6.0a}
\]

the source window of owner `O_(d+1)` in the first block.  The largest
suffix address is

\[
 [s'+1,s'+d-1]\subseteq[s',s'+d],                    \tag{6.0b}
\]

the source window of owner `O_0` in the second block.  Every smaller ray is
nested inside the corresponding largest address, so its target is contained
in that owner.  Assign the `d-1` prefix targets to distinct slots of the
first owner and the `d-1` suffix targets to distinct slots of the second.
Since each owner has `d+1` slots, this gives a legal ideal partial matching
of size

\[
                              |\widehat\Pi|=2(d-1).    \tag{6.1}
\]

Let

\[
 \rho={1\over W}\sum_{s<r}\binom ks,
 \qquad q=d+1.
\]

The arbitrary-ideal-pins theorem extends this partial matching whenever

\[
                2(d-1)\le(q-\rho)(k-r+1).             \tag{6.2}
\]

Because `q-rho>=1-O(d^2/W)` and `d=Theta(sqrt(k))`, (6.2) holds for all
sufficiently large `k`.

Therefore the aligned ray bank creates no asymptotic obstruction at the
level of target containment, owner counts, or ideal slot Hall.  This does
**not** imply that the assigned targets are nested endpoint chains or that
one global source chronology has a complete strict-lower deck.  The maximal-
envelope halo theorem does prove global inverse extension for an interior
resident planting.  The unresolved gap is therefore exactly the passage

```text
ideal owner slots with O(d) pins
        -> one prefix-realizable physical chainization
        -> one pinned global antecedent/guard word
        -> all but O(1) strict-lower values in its literal short deck.
```

For a fixed pinned antecedent the exact defect is the waste identity

\[
 \text{missing}=D_A^\Pi+Q_A^\Pi+R_A^\Pi-\sigma,      \tag{6.3}
\]

where `D` counts duplicate residual lower values, `Q` counts extra
occurrences of pinned values, `R` counts rank-`r` short cells, and `sigma`
is the scalar short-cell slack.

## 7. Is terminal typing still necessary?

### 7.1 Final direct-ray proof: no

For one chosen terminal phase, every aligned target identity is retained at
its exact ray occurrence.  The terminal object is a literal word, and its
definition contains no type predicate.  The direct-ray compiler of Sections
1--3 therefore needs no native terminal type at all.

If deterministic native bundles are retained, their cut/polarity labels are
passive metadata provided they add no physical constraint and have no future
consumer.  They can be reconstructed from the ticket and complete physical
record or erased.

### 7.2 Nondeterministic routing or regeneration: sometimes yes

Typing cannot be erased when it selects a physical sink or controls a later
transition.  Take two tickets `1,2`, starts `s_1,s_2`, and terminal
occurrences `t_1,t_2`.  Suppose the only disjoint routes are

\[
                         s_1\longrightarrow t_2,
 \qquad                  s_2\longrightarrow t_1.      \tag{7.1}
\]

The untyped linkage has value two.  If ticket `i` is required to end at
the externally prescribed type of `t_i`, the typed linkage has value zero.
Thus a Rado/max-flow theorem which chooses among alternative terminals must
retain type.  The same applies when a child lift distinguishes phase,
polarity, endpoint class, guard state, or continuation rule.

Serial terminal readout bypasses this no-go because it chooses one complete
physical phase and its exact ray occurrences before solving the compiler;
there is no representative or sink permutation left to optimize.

## 8. Exact frontier

The two-phase typed common-cap gate is not intrinsic to a **final**
`B+O(1)` proof.  It was required by the stronger architecture which asked
one compiler/router state to survive both packet phases or to export a
typed continuation.  Under serial safety the strongest proof-safe target is
instead:

> Construct one reachable terminal phase and one global nonempty antecedent
> extending its `2(d-1)` literal ray pins such that all but `O(1)` strict-
> lower values occur in its short-interval OR deck.

The parts still open are:

1. global physical chainization/prefix realization with the displayed pins
   and short-cell waste at most `sigma+O(1)`;
2. reachability/regeneration of such a terminal state in every dimension;
3. any active terminal type needed by a future lift, but not by final
   direct-ray readout.

No common matching for phases `P,Q`, no exactness of their pointwise-union
cap, and no polarized terminal-acceptance axiom belongs to the weakest final
criterion.

## 9. Dependencies

- `MATH_THEOREM_SERIAL_COATOM_SAFE_SEARCH_AND_FINAL_COMPILER_REDUCTION_20260801.md`
- `MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`
- `MATH_THEOREM_LITERAL_OCCURRENCE_FACT_COALESCENCE_AND_IBC_ICA_BACKGROUND_REDUCTION_20260804.md`
- `MATH_THEOREM_PASSIVE_TERMINAL_TYPE_ELIMINATION_AND_DIRECT_IBC_ICA_CLOSURE_20260804.md`
- `MATH_THEOREM_FIXED_WORD_FUNCTIONAL_OCCURRENCE_AND_ONE_PHASE_HALL_COLLAPSE_20260804.md`
- `MATH_THEOREM_PINNED_MAXIMAL_ENVELOPE_GLOBAL_EXTENSION_AND_WASTE_IDENTITY_20260804.md`
- `MATH_THEOREM_L_PINNED_TRIANGULAR_ROOTED_TRACE_AND_PRIVATE_COMMONCAP_20260801.md`
- `MATH_THEOREM_R_COMMON_CAP_GUARD_PRUNING_ROBUST_HALL_LIFT_20260731.md`
