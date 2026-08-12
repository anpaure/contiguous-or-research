# Regenerative pull cells: endpoint aperture, global overlap guards, and the single-credit reset reduction

**Date:** 2026-08-02  
**Lane:** ROOT, regenerative pull--cell / protected Catalan--pivot host  
**Status:** two unconditional audit repairs, an unconditional one-credit
conservation law, and a conditional bounded-sidecar implication.  The
globally guarded protected history-reset host defined in Section 5 is an
**open hypothesis**; no all-dimensional host or new value of `nu(k)` is
claimed.

## 0. Verdict

Put

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname {Cat}_m,\qquad B=W+d.             \tag{0.1}
\]

The newest protected Catalan--pivot reductions require two load-bearing
repairs before they can be used in a regenerative induction.

1. **Endpoint aperture.**  An unrooted Johnson Hamilton path using all but
   one lower root `o` does not automatically determine a perfect rooted
   phase.  If its owner endpoints are `s,t`, one must have

   \[
                         o\subseteq s\quad\hbox{or}\quad o\subseteq t.
                                                               \tag{0.2}
   \]

   More sharply, a prescribed predecessor phase chooses which of the two
   containments is required.  The closed-shore flow and contracted graphic
   rank do not imply (0.2).

2. **Global overlap guards.**  Full literal `d`-overlap of consecutive
   component blocks does not imply that only consecutive blocks meet.
   Whenever an intermediate component has fewer than `d` depth cells, the
   source intervals of the two nonadjacent blocks overlap.  Consequently
   pairwise port guards do not prove global compiler-address injectivity,
   cap consistency, or the final residence/history state.  These rows must
   be replayed on the one globally placed source word.

After these repairs, the source-length ledger remains exact.  If the unique
`B+1` surplus depth cell is already inside the pivot/reset component, then
**every** Catalan connector must use a full literal `d`-history overlap.  A
separate deficient exterior-reset join would cost another source position
and force at least `B+2`.

The proof-safe remaining hypothesis is therefore one globally guarded,
rooted, reversal-quotient **protected history-reset path**, in which the
unique pivot surplus cell also exports the next aperture state.  Under this
open hypothesis, bounded terminal upper/compiler casualties may be paid
once and need not enlarge the carried sidecar.  If their repair complexity
is at most `c`, the exact conditional conclusion is

\[
                         \nu(k)\le B(k)+1+c.             \tag{0.3}
\]

The case `c=0` is the conditional `B+1` target.  The charged carried
sidecar has one target/interface token.  The full owner factor, literal
`d`-history, witness atlas and endpoint metadata are structured auxiliary
state, not an `O(1)`-sized description.

## 1. Exact endpoint-aperture theorem

Let

\[
              T_0,T_1,\ldots,T_{W-1}                  \tag{1.1}
\]

be a Hamilton path on the rank-`m` owners.  Assume its consecutive
intersections

\[
              L_i=T_i\cap T_{i+1}\qquad(0\le i<W-1)   \tag{1.2}
\]

are distinct and exhaust all rank-`m-1` roots except one root `o`.

### Theorem 1.1 (rooted lift iff the omitted root fits an endpoint)

There is a perfect incidence matching `M_0` and a matching `Q` of size
`W-1` whose alternating incidence path has owner projection (1.1) if and
only if

\[
                         o\subseteq T_0
             \quad\hbox{or}\quad o\subseteq T_{W-1}.   \tag{1.3}
\]

The two rooted phases are exact.

* In the forward-tail phase

  \[
   M_0(L_i)=T_i\quad(0\le i<W-1),\qquad
   M_0(o)=T_{W-1},                                     \tag{1.4}
  \]

  so it exists exactly when `o subseteq T_(W-1)`.
* In the reverse-tail phase

  \[
   M_0(L_i)=T_{i+1}\quad(0\le i<W-1),\qquad
   M_0(o)=T_0,                                         \tag{1.5}
  \]

  so it exists exactly when `o subseteq T_0`.

#### Proof

Assume the final containment in (1.4).  The owners on the right sides of
(1.4) are all distinct and exhaustive, as are the lower roots on the left,
so `M_0` is a perfect incidence matching.  Put

\[
                         Q=\{L_iT_{i+1}:0\le i<W-1\}.
                                                               \tag{1.6}
\]

These incidences form a matching.  Their rooted links are

\[
       L_0\longrightarrow L_1\longrightarrow\cdots
       \longrightarrow L_{W-2}\longrightarrow o,      \tag{1.7}
\]

so expanding `M_0` gives the alternating path with owner order (1.1).
The construction from (1.5) is the reversal of this argument.

Conversely, colour the edges of an alternating incidence lift by its two
matching phases.  Once the phase on the first owner transition is fixed,
alternation forces that phase on the whole connected path.  In one choice,
each `L_i` is matched to `T_i`, leaving only `T_(W-1)` for `o`; in the other,
each `L_i` is matched to `T_(i+1)`, leaving only `T_0`.  Since a matching
edge must be an incidence, the corresponding containment in (1.3) is
necessary. \(\square\)

### Corollary 1.2 (repair to the unrooted closed-shore criterion)

Fix an upper-exact Johnson forest `F_0`, omitted root `o`, and intended
Hamilton endpoints `s,t`.  The closed-shore inequalities

\[
       2I_A(Y)+J_A(Y)\le \sum_{T\in Y}c_T
                     \qquad\hbox{for every owner shore }Y       \tag{1.8}
\]

are necessary and sufficient for the residual root-to-owner **degree**
completion.  Adding contracted graphic rank `C-1` makes the owner graph a
Hamilton path.  It determines a rooted Catalan decomposition only after
adding

\[
                         o\subseteq s\quad\hbox{or}\quad o\subseteq t.
                                                               \tag{1.9}
\]

If a protected pivot fixes the forward-tail phase and is required as the
initial owner segment, the disjunction is no longer free: the omitted root
must lie in the terminal endpoint selected by (1.4).  Reversing the whole
certificate exchanges the two versions.

#### Proof

The max-flow proof of (1.8) selects two containing owners for every
residual root and the graphic-rank row makes their union with `F_0` one
Hamilton path.  Theorem 1.1 is then exactly the missing condition for the
unused root to complete one perfect incidence phase. \(\square\)

Thus the unrooted flow remains valid, but the sentence “the incidence lift
determines `M_0`” is false without (1.9).

## 2. Global placement of overlapping component sources

Let component `i` have `n_i` intended owner depth cells, `g_i` declared
nonowner depth cells, and

\[
                         \ell_i=n_i+g_i>0.              \tag{2.1}
\]

Its literal depth-`d` source block `A^i` has `ell_i+d` letters.  Let the
chosen overlap of blocks `i` and `i+1` have length `o_i`, where
`0<=o_i<=d`.  Define their global starting addresses by

\[
 a_1=0,\qquad
 a_{i+1}=a_i+\ell_i+d-o_i.                              \tag{2.2}
\]

Block `i` occupies the global source interval

\[
             I_i=[a_i,a_i+\ell_i+d-1].                  \tag{2.3}
\]

At every position shared by two blocks, their literal source letters must
be equal.  For variable cap states, this means one common nonempty letter
must satisfy every local constraint placed at that global position.

### Theorem 2.1 (global overlap and address theorem)

For a globally compatible placement (2.2)--(2.3):

1. the final source length is

   \[
    \sum_i\ell_i+d+\sum_i(d-o_i),                       \tag{2.4}
   \]

   and its depth-row length is

   \[
    \sum_i\ell_i+\sum_i(d-o_i);                         \tag{2.5}
   \]

2. for `i<j`, two nonadjacent block images meet exactly when

   \[
    \sum_{q=i}^{j-1}(\ell_q+d-o_q)\le \ell_i+d-1;       \tag{2.6}
   \]

   when every connector has full overlap `o_q=d`, this is

   \[
               \sum_{q=i+1}^{j-1}\ell_q\le d-1;        \tag{2.7}
   \]

3. a local interval cell `[u,v]` of block `i` maps to the global interval

   \[
                         [a_i+u,a_i+v],                  \tag{2.8}
   \]

   and retains its literal OR;
4. selected compiler pins remain a physical matching if and only if their
   images (2.8) are globally distinct after all blocks are placed; and
5. residence, endpoint histories, cap feasibility and any address-sensitive
   upper/compiler guard are valid if and only if they pass on the final
   global word.  They may be checked incrementally by composing the state of
   the **whole built prefix** with the next suffix, but not merely by testing
   two isolated component states at every arc.

#### Proof

The last block ends at `a_s+ell_s+d-1`.  Substitute (2.2) and add one to
obtain (2.4); subtracting `d` gives (2.5).  Since starts and ends in (2.3)
are strictly increasing, `I_i` and `I_j` meet exactly when the start of the
latter is no larger than the end of the former.  Substitution gives (2.6),
and setting every `o_q=d` gives (2.7).

The embedding of each block is translation by `a_i`, so a local interval
maps to (2.8).  Global compatibility identifies only equal source letters;
the OR on that translated interval is therefore unchanged.  Two selected
pins consume the same physical cell exactly when their translated endpoint
pairs agree, proving item 4.

Finally, the glued object is one ordinary linear source word.  Coordinate
runs, source caps and address guards are predicates of that word, so replay
on it is necessary and sufficient.  Incremental replay is exact when the
stored state is the associative state of the complete prefix.  An isolated
middle component can be shorter than `d` or all-one in a coordinate, in
which case its left-boundary state alone does not contain the run age
inherited through the earlier prefix. \(\square\)

### A minimal nonadjacent-collision example

Take `d=3`, three blocks with `ell_1=ell_2=ell_3=1`, and full overlaps.
Then

\[
 I_1=[0,3],\qquad I_2=[1,4],\qquad I_3=[2,5].          \tag{2.9}
\]

Thus blocks 1 and 3 share global positions `2,3`.  A pin at local singleton
`[2,2]` of block 1 and a pin at local singleton `[0,0]` of block 3 are the
same physical cell, even if block 2 carries no pin.  Both adjacent pairwise
pin tests can therefore pass while the global matching fails.

This directly refutes the assertion that no nonadjacent blocks are
identified.  A sufficient way to avoid the phenomenon is to require every
intermediate `ell_i>=d`, but Catalan forests can have isolated or short path
components, so that restriction cannot be assumed in the intended theorem.

### Corollary 2.2 (corrected full-overlap composition)

The conclusions claimed by an iterated literal-overlap connector hold when
the selected component order satisfies all of the following **global**
conditions:

1. the endpoint-aperture condition of Theorem 1.1;
2. one compatible placement (2.2) of all literal letters and caps;
3. global injectivity of every capacity-one occurrence address;
4. acceptance of the final coordinate traces and endpoint histories; and
5. replay of every declared upper witness and compiler pin in the final
   word.

Pairwise overlap edges remain useful candidate generators, but a static
Hamilton path in their graph is not by itself a physical certificate when
short components occur.

## 3. The one-credit conservation law

Let the component blocks contain all `W` owners once.  From (2.5), define
the literal source-position charge

\[
             \chi=\sum_i g_i+\sum_i(d-o_i).             \tag{3.1}
\]

The final source has length `B+chi`.

### Theorem 3.1 (single-credit exterior reset)

Assume the pivot/reset component already contains one controlled nonowner
depth cell and no other component contains one:

\[
                         \sum_i g_i=1.                   \tag{3.2}
\]

Then the source has length `B+1` if and only if

\[
                         o_i=d\qquad\hbox{for every connector }i.   \tag{3.3}
\]

Consequently an exterior reset can coexist with the pivot at cost one only
if it is exported inside the already charged pivot/boundary state and all
component joins remain full-history overlaps.  A separate reset which uses
one additional nonowner cell or one `(d-1)`-overlap connector forces

\[
                         \chi\ge2                         \tag{3.4}
\]

and hence source length at least `B+2`.

#### Proof

Every summand in (3.1) is a nonnegative integer.  Under (3.2), equality
`chi=1` is therefore equivalent to the vanishing of every `d-o_i`, which
is (3.3).  Either additional reset mechanism contributes another unit to
(3.1), proving (3.4). \(\square\)

### Corollary 3.2 (one-in/one-out charged sidecar)

The literal one-aperture Pascal relay proves locally that an incoming
rank-`m-1` interface token `Hhat` may be realized by one fan while exactly
one outgoing token `J` is exported.  If a global host places that relay in
the unique component of (3.2), supplies the owner-preserving rethread which
makes its deficient aperture transition the unique omitted path edge, sets
`J=o` for the endpoint root in Theorem 1.1, and realizes that boundary token
in the same globally guarded state, then the charged target/interface
sidecar obeys

\[
                         |\Xi_{m+1}|=|\Xi_m|=1.          \tag{3.5}
\]

The simultaneous placement just stated is **not proved** by the separate
sharp-pivot, Catalan-connector, or one-aperture notes.  It is one of the open
clauses in Section 5.

## 4. Exact terminal repair after the corrected host

Fix one final oriented word and cap state.  Let `M_ref` be a reference
matching of old lower targets.  Let the hard packet tasks use distinct
certified cells `b_1,...,b_h`, after deduplicating any repeated logical
target.  Assume the old targets together with those genuinely new tasks
exhaust the required strict-lower bank.  Let `D` be a complete literal
damage set for `M_ref` in this final state, and require

\[
                         b_i\notin D\qquad(1\le i\le h).       \tag{4.0}
\]

Define the certified compiler casualty set

\[
 H_{\rm comp}=
 \{S:\text{the }M_{\rm ref}\text{-cell of }S
               \text{ lies in }D\cup\{b_1,\ldots,b_h\}\}.       \tag{4.1}
\]

Let `H_up` be the required upper targets without a certified final
occurrence, `H_ray` the unmatched literal ray targets, and `H_ap` the
singleton boundary/aperture target if its promised pin is absent.  Put

\[
                 H=H_{\rm up}\cup H_{\rm comp}
                         \cup H_{\rm ray}\cup H_{\rm ap}.       \tag{4.2}
\]

For a finite target family `H`, let `R(H)` be the minimum length of a
repair word covering it, with `R(emptyset)=0`; literal listing gives
`R(H)<=|H|`.

### Theorem 4.1 (terminal cost and nonaccumulation)

Suppose a corrected globally guarded host has `chi=1`, covers every middle
owner, and satisfies every exported recursive row.  Then

\[
                         \nu(k)\le B(k)+1+R(H).          \tag{4.3}
\]

If the canonical simple-positive birail is realized by two literal cross
matchings in the same accepted state, then `H_ray` is empty.  If the host is
an admissible contraction-exact full-block refinement, its transported
background matching adds no separate Hall term; otherwise every affected
reference cell must already be represented in `D`.

The terminal deficiencies in `H` do not enlarge the carried sidecar exactly
when the auxiliary successor independently satisfies every exported row
associated with those targets, so the fact that the terminal plus choice
misses them is absent from the fields read by the next transition.  If an
`H` deficiency persists in an exported row, it must instead be added to the
carried state and bounded there.

#### Proof

The bounded-eviction lemma deletes from `M_ref` only edges whose cells lie
in `D union {b_i}` and then adds the hard task edges.  Thus every hard task
and every old lower target outside `H_comp` is matched.  By definition the
upper, ray and aperture rows are complete outside their three displayed
sets.  The source already has length `B+1`; append a shortest repair word
for their union `H`.  Appending destroys no old witness, proving (4.3).

The zero-block birail theorem makes ray deficiency exactly the number of
zero--zero pairs; the two literal cross matchings avoid all such pairs.
The full-block transport conclusion and its qualifications give the next
sentence.

Finally, the successor relation reads only its declared exported fields.
The auxiliary child may certify an exported row using a different
occurrence, matching or cap from the terminal plus choice.  Appending targets
to the terminal physicalization then changes no successor, so the repair is
paid once.  Conversely, forgetting a deficiency which remains in an
exported row would not produce an admissible successor.  This proves the
exact nonaccumulation criterion. \(\square\)

The terminal compiler and witness banks need not occupy the same addresses
in both reversal representatives.  Global reversal transports one complete
oriented certificate to the other.  This does not apply to a selective
packet flip against a frozen exterior.

## 5. The exact open protected history-reset hypothesis

The following is a single combined hypothesis.  Every existence clause
`OPEN-1`--`OPEN-6` below is **unproved**.

### `RQPHR_c(m,d)` -- reversal-quotient protected history reset

For one reachable incoming reversal orbit with charged sidecar
`Xi={Hhat}`, choose one representative and construct:

1. **`OPEN-1`, rooted protected forest.**  A perfect incidence matching
   `M_0` and an upper-exact rooted Catalan forest `Q_0` containing the
   protected monotone-pivot phase.  If this is obtained from an unrooted
   owner path, its omitted root satisfies the phase-specific endpoint
   aperture in Theorem 1.1.
2. **`OPEN-2`, globally guarded component path.**  One literal block for
   every component of `Q_0` and a free-port Hamilton order.  Their starts
   are the global addresses (2.2); all source letters, capacity-one pins,
   cap rows, coordinate histories and upper occurrences pass the global
   replay of Corollary 2.2.  A pairwise port-graph check is not substituted.
3. **`OPEN-3`, co-located one-credit reset.**  Exactly one nonowner depth
   cell occurs, in the protected pivot/boundary component; every connector
   has full `d` overlap.  The same component realizes `Hhat`, uses the
   owner-preserving rethread which makes the deficient aperture transition
   the unique omitted owner edge, identifies its colour `J` with the omitted
   endpoint root `o` in the phase-specific containment of Theorem 1.1,
   realizes `o` in the boundary nonowner cell, and exports `J` plus the
   accepted next `d`-history.  No second reset aperture is used.  The
   existence of this rethread is part of `OPEN-3`, not a consequence of the
   local pivot formulas.
4. **`OPEN-4`, exported closure.**  Every upper witness, residence state,
   topology/root field, compiler/cap field and guard actually read by the
   next same-parity transition is complete in the auxiliary child.  Its
   only charged target/interface sidecar is `{J}`.
5. **`OPEN-5`, bounded terminal plus state.**  A terminal physicalization
   on a globally replayed source chronology of length `B+1`, possibly with
   a different matching, cap and witness selection from the auxiliary
   state, has repair family `H` from (4.2) with

   \[
                              R(H)\le c.                \tag{5.1}
   \]

   The damage set in (4.1) is complete, and every abstract birail cross edge
   used here is expanded to its two distinct addressed assignments.
6. **`OPEN-6`, quotient regeneration.**  The output belongs to the same
   declared state class at the next same-parity dimension; the construction
   is equivariant under simultaneous reversal of the whole word, all
   occurrence addresses, endpoints and sidecar.  The analogous even
   terminal child exists when a conclusion on both parities is desired.

This is weaker than a fixed-address phase-common compiler/exterior theorem:
one oriented complete certificate and its reflection suffice.  It is
stronger than a phase-common undirected `q1` host, because literal histories,
addresses, upper witnesses and reset closure are included.

### Theorem 5.1 (conditional regenerative pull--cell implication)

Assume that, from some base dimension onward, there is one compatible
infinite odd spine of `RQPHR_c(m,d_m)` certificates, with the even terminal
children in `OPEN-6`.  Then the charged carried sidecar has cardinality one
throughout and

\[
                         \nu(k)\le B(k)+1+c             \tag{5.2}
\]

for every subsequent odd and even terminal dimension.  If `c=0`, then

\[
                         \nu(k)\le B(k)+1.              \tag{5.3}
\]

#### Proof

`OPEN-2`--`OPEN-3` and Theorem 3.1 give a source of length exactly `B+1`.
Corollary 3.2 and `OPEN-4` give one admissible outgoing charged token and no
other carried defect.  Theorem 4.1 and `OPEN-5` bound each terminal charge
by `1+c` relative to `B`.  `OPEN-6` continues the auxiliary odd spine and
supplies the even terminals.  Apply the bounded-cost odd-spine theorem;
terminal repairs are compiled afresh and are not added to later lengths.
\(\square\)

The weakest logical hypothesis is the existence of this one compatible
infinite spine.  Left-totality for every admissible sidecar orbit is a
stronger, more convenient induction statement and is not asserted here.

## 6. Independent audit of the decisive step

The decisive `B+1`/bounded-sidecar implication survives the audit only with
all of the following qualifications.

1. **The endpoint aperture is not optional.**  The owner-degree flow can
   return a Hamilton path whose omitted root lies in neither endpoint.  Such
   a path has no perfect alternating incidence phase by Theorem 1.1.
2. **Pairwise literal ports are not a certificate.**  Equation (2.9) gives
   an explicit nonadjacent physical-cell collision.  The global address and
   history replay in `OPEN-2` is load-bearing.
3. **One credit cannot be spent twice.**  With the pivot nonowner already
   present, a distinct deficient reset join gives `chi>=2`.  Therefore
   regeneration must be co-located as in `OPEN-3` for a `B+1` conclusion.
4. **Terminal eviction is not carried repair.**  The family `H` may be
   forgotten only when the auxiliary successor independently closes every
   exported row associated with it.  Otherwise the claimed singleton
   sidecar is false.
5. **Phase-common fixed addresses are unnecessary only globally.**  Whole-
   state reversal transports a completed certificate.  It does not switch
   one packet while holding its exterior fixed and cannot improve any
   reversal-invariant defect.
6. **Sidecar cardinality is not metadata size.**  The one charged token does
   not make the literal history, forest, atlas or address ledger bounded-
   description objects.

These checks are independent of the fractional pull-clock.  That theorem
proves a stationary marginal circulation; it supplies none of `OPEN-1`--
`OPEN-6`.

## 7. Why the remaining clauses are real

The present proved ingredients close the following local rows.

* The sharp monotone pivot has zero old arbitrary-width OR damage and an
  exact singleton/two-ray compiler ledger.
* The birail southwest Hall family collapses to zero--zero cross matching.
* The corrected pull clock supplies fractional rank/age feasibility.
* Bounded compiler eviction gives the exact terminal casualty superset.
* The protected Catalan decomposition and full-history length accounting
  are exact after the repairs above.

They do not prove the open host.

* Dropping targetwise exterior witnesses is unsound: one legal local rail
  can destroy `Theta(m)` or `Theta(m^2)` uniquely witnessed exterior upper
  targets.
* Dropping global residence is unsound: three individually clipped-clean
  Johnson components can concatenate to an internal run of length exactly
  `d`.
* Dropping complete compiler damage is unsound: a common-cap shrinkage can
  invalidate remote cells not visible in an isolated ticket.
* Dropping the rooted endpoint aperture is exactly the failure repaired by
  Theorem 1.1.
* Dropping global overlap guards is exactly the collision in (2.9).

Thus the smallest proof-safe combined target in this architecture is
`RQPHR_c`: a rooted forest, one globally placed full-history component path,
one co-located pivot/reset credit, complete exported rows, bounded terminal
damage, and quotient regeneration.  This is an exact remaining hypothesis,
not a proved phase-common protected-host lemma.

## 8. Dependency and scope ledger

Proved inputs used here:

* `MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`;
* `MATH_THEOREM_A_MONOTONE_PIVOT_INSERTION_ZERO_DAMAGE_COMMONQ_20260801.md`;
* `MATH_THEOREM_ZERO_BLOCK_BIRAIL_COLLAPSE_AND_C8_CROSSMATCH_GATE_20260801.md`
  together with its independent audit;
* `MATH_THEOREM_TRIANGULAR_PULL_CLOCK_CORRECTED_20260801.md`, only for its
  fractional statement;
* `MATH_THEOREM_BOUNDED_COMPILER_EVICTION_AND_PHASE_DECOUPLING_20260801.md`;
* `MATH_THEOREM_K_ONE_APERTURE_PASCAL_PIVOT_BPLUS1_BRIDGE_20260802.md`
  together with its correction audit, only for the local one-in/one-out
  aperture relay;
* `MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md`;
* `MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md`;
* the exact exterior blocker identities in
  `MATH_THEOREM_L_RESET_OPEN_PATH_EXTERIOR_SAFE_CUT_BLOCKER_MINMAX_20260801.md`;
* `MATH_AUDIT_K_PROTECTED_CATALAN_PIVOT_BIRTH_LITERAL_OVERLAP_20260802.md`,
  whose independent endpoint-aperture and nonadjacent-overlap audit agrees
  with Sections 1--2; and
* the owner-layer Catalan decomposition and the source-length identity from
  the new Catalan--pivot notes, only in the corrected forms proved in
  Sections 1--3 above.

Not proved here:

* any clause `OPEN-1`--`OPEN-6`;
* existence of `RQPHR_c` for one unbounded sequence of dimensions;
* a phase-common fixed-exterior compiler or local phase switch;
* a `k=17` word or improvement of any finite upper bound; or
* `nu(k)<=B(k)+1` unconditionally.
