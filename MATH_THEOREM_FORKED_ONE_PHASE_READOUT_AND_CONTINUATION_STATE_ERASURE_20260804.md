# Forked one-phase readout and continuation-state erasure

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** exact existential reduction.  A same-parity induction may use
two independent children of one auxiliary parent: a continuation child and
a terminal readout child.  The terminal `Ibc/Ica` phase, its aligned rays,
its antecedent and its compiler do not have to regenerate.  The theorem does
not construct either child uniformly, prove a bounded continuation boundary,
or prove the terminal one-phase Hall bound.

## 0. Outcome

The current concentrated target asks one child simultaneously to

1. contain the coherent ring, protected upper reservoir and actual
   `Ibc/Ica` packet;
2. admit one global one-phase antecedent and a bounded-defect terminal
   compiler; and
3. export the physical state needed by the next same-parity step.

The third requirement need not be imposed on the same child as the first
two.  A mathematical existence certificate can be copied.  Starting from
one auxiliary parent, apply the continuation construction to one copy and
the terminal construction to another.  The two children are different
objects and their resources are never superposed.

Consequently the state carried by the induction consists only of the
complete boundary read by the **continuation** construction.  The following
data are terminal-local whenever they are used only by the one-phase
readout:

* the selected packet phase `epsilon`;
* the packet core, filler order, active labels and planted address;
* the `2(d-1)` aligned ray target--address facts;
* the global terminal antecedent;
* the residual target--cell graph, matching and Hall witnesses;
* the terminal repair family; and
* terminal-only upper-witness, cap and native-socket choices.

Their cardinality may grow with `d`: they are bulk data inside a word of
length `B(k)+O(1)`, not an appended sidecar and not an input to the next
step.  In particular, the aligned ray bank has `Theta(d)` facts but uses
already existing short intervals, so its size creates neither an additive
length charge nor a regenerative-state charge.

This leaves two separate all-dimensional targets:

1. a continuation-only bounded-boundary theorem; and
2. a terminal fork theorem with bounded one-phase readout charge.

No co-instantiation of their child carriers is required.

## 1. The clone-and-fork theorem

Index the auxiliary odd dimensions by

\[
                         o_m=2m+1,
 \qquad                  e_m=2m+2.
\]

Let `G_m` be any family of auxiliary certificates at dimension `o_m`.
These certificates may contain bulk owner factors, protected occurrences,
boundary histories and any declared recursive data.  Define three literal
relations.

* `C_m(g,g')` says that a continuation construction applied to `g in G_m`
  produces `g' in G_(m+1)`.
* `R_m^o(g,w)` says that a terminal construction applied to `g` produces a
  physical word `w` on `o_m` coordinates.
* `R_m^e(g,w)` says that a terminal construction applied to `g` produces a
  physical word `w` on `e_m` coordinates.

Write

\[
 \tau_o(w)=|w|-B(o_m),
 \qquad
 \tau_e(w)=|w|-B(e_m)
\]

for the two terminal charges.  The relations may use entirely different
child carriers, cap states, packet locations, witness occurrences and
compiler matchings.

### Theorem 1.1 (forked odd-spine criterion)

Suppose there are auxiliary certificates `g_m in G_m`, for all
`m>=m_0`, such that

\[
                         C_m(g_m,g_{m+1})                 \tag{1.1}
\]

and, independently, words `w_m^o,w_m^e` such that

\[
 R_m^o(g_m,w_m^o),
 \qquad
 R_m^e(g_m,w_m^e),                                    \tag{1.2}
\]

with

\[
 \sup_{m\ge m_0}
 \max\{\tau_o(w_m^o),\tau_e(w_m^e)\}\le C.             \tag{1.3}
\]

Then

\[
                         \nu(k)\le B(k)+C                 \tag{1.4}
\]

for every `k>=2m_0+1`.

Crucially, neither `w_m^o` nor `w_m^e` has to encode `g_(m+1)`, and the
continuation child in (1.1) need not be terminally compilable.

#### Proof

For odd `k=o_m`, use the word `w_m^o`; for even `k=e_m`, use `w_m^e`.
Equation (1.3) gives (1.4) in both cases.  Equation (1.1) is used only to
ensure that the auxiliary parent required at the next index exists.

There is no resource-sharing issue.  A finite mathematical certificate
`g_m` is immutable data and can be used twice.  Apply the continuation map
to one copy and the terminal map to a second copy.  This is duplication of
an existence witness, not concatenation of two words and not simultaneous
planting of two child resource banks.  Hence it contributes zero physical
positions.  \(\square\)

### Corollary 1.2 (left-total form)

It is enough to have a family `G_m^* subseteq G_m`, one initial
`g_(m_0) in G_(m_0)^*`, and constants `C_o,C_e` such that every
`g in G_m^*` has

\[
 \exists g'\in G_{m+1}^*\ C_m(g,g'),                    \tag{1.5}
\]

\[
 \exists w^o\ R_m^o(g,w^o),\quad \tau_o(w^o)\le C_o,  \tag{1.6}
\]

and

\[
 \exists w^e\ R_m^e(g,w^e),\quad \tau_e(w^e)\le C_e.  \tag{1.7}
\]

Then (1.4) holds with `C=max(C_o,C_e)`.

The witnesses in (1.5)--(1.7) are three independent existential choices.
The stronger quantifier

\[
 \exists z\,[\mathsf{Continue}(g,z)\wedge
              \mathsf{ReadOdd}(g,z)\wedge
              \mathsf{ReadEven}(g,z)]                 \tag{1.8}
\]

is unnecessary.  For example, one child mode may be the unique terminal
mode while a different child mode is the unique regenerative mode; (1.5)--
(1.7) still compose, whereas (1.8) fails.

### Corollary 1.3 (finite-horizon leaf readout)

An infinite spine whose every vertex is terminally readable is stronger
than necessary.  Fix one base auxiliary certificate `g_(m_0)`.  Suppose
that for every terminal horizon `M>=m_0` there is a finite continuation path

\[
 g_{m_0}^{(M)}=g_{m_0},
 g_{m_0+1}^{(M)},\ldots,g_M^{(M)},
 \qquad
 C_j(g_j^{(M)},g_{j+1}^{(M)})                       \tag{1.9}
\]

and that only its leaf has odd and even readouts of charge at most `C`:

\[
 R_M^o(g_M^{(M)},w_M^o),\qquad
 R_M^e(g_M^{(M)},w_M^e),
 \qquad
 \max\{\tau_o(w_M^o),\tau_e(w_M^e)\}\le C.          \tag{1.10}
\]

Then (1.4) holds in every dimension from the base onward.  The paths for
different `M` may be different, and terminalizing the leaf may destroy
every continuation interface there.

#### Proof

For requested odd dimension `o_M`, use `w_M^o`; for requested even
dimension `e_M`, use `w_M^e`.  The finite path (1.9) proves the existence
of the leaf input required by (1.10).  No later child is needed after the
requested word is produced.  Repeat this independent finite construction
for every `M`.  \(\square\)

Thus even one compatible infinite auxiliary path is not logically required
for the dimensionwise upper bound.  Arbitrarily long bounded-state
continuation paths with uniformly cheap terminal leaves suffice.  This does
not give an online or nested construction, and it does not follow from
unbounded path length unless the cheap terminal-leaf condition is also
proved at every horizon.

## 2. Exact specialization to the one-phase terminal compiler

For a terminal branch at dimension `k`, let `chi` be the number of physical
positions already used beyond `B(k)` before terminal repair.  Let `T_0` be
its safe starting carrier, let `T` be a reachable terminal carrier, and let
`epsilon` be one aligned `Ibc/Ica` phase in `T`.  Its literal forced ray
matching is

\[
 \Pi^\epsilon=
 \{(X_j^\epsilon,C_j^X),(Y_j^\epsilon,C_j^Y):1\le j<d\}.
                                                               \tag{2.1}
\]

For a global nonempty antecedent

\[
                  A\in\mathcal A(T,\Pi^\epsilon),       \tag{2.2}
\]

let `delta(A,Pi^epsilon)` be the exact residual Hall deficiency in the
same realized word.  Define the readout charge of an auxiliary certificate
`g` by

\[
\begin{aligned}
 \Theta_k^{\rm 1ph}(g)=\min\{\;&
       \chi+u(T_0)+\delta(A,\Pi^\epsilon):\\
   &\text{the displayed terminal branch is constructible from a copy of }g
   \}.
                                                               \tag{2.3}
\end{aligned}
\]

The minimum is `+infinity` if no such branch exists.  Equivalently, one may
minimize `chi+u(T_0)+Lambda_(1ph)(T,epsilon)` over constructible branches.

### Corollary 2.1 (forked one-phase criterion)

In Theorem 1.1, it is enough that the odd and even readout branches satisfy

\[
                    \Theta_{o_m}^{\rm 1ph}(g_m)\le C_o,
 \qquad
                    \Theta_{e_m}^{\rm 1ph}(g_m)\le C_e. \tag{2.4}
\]

Then

\[
                    \nu(k)\le B(k)+\max\{C_o,C_e\}.     \tag{2.5}
\]

#### Proof

The one-phase terminal theorem leaves exactly
`delta(A,Pi^epsilon)` residual lower targets and at most `u(T_0)` retained
upper targets.  Append those masks literally.  This gives the two relations
`R^o,R^e` with the charges in (2.3).  Apply Theorem 1.1.  \(\square\)

The local aligned-ambient theorem proves that, once the actual packet is
present, all facts in (2.1) are literal and pairwise address-disjoint.  It
does **not** prove (2.2), bounded residual Hall, the upper-complete terminal
host, or construction from an arbitrary auxiliary parent.  Those remain
the content of the terminal fork theorem.

## 3. Continuation-only boundary erasure

The fork has an important consequence for state compression.  A complete
boundary need separate only the child-local bulk used by the continuation
construction from the next continuation exterior.  It need not separate
terminal compiler variables from anything, because the terminal child has
no descendant.

For the continuation branch write

* `X` for child-local bulk variables;
* `Y` for the proposed carried boundary; and
* `Z` for the next-step exterior.

Let `F_m^to(X,Y,Z)` be the full literal continuation predicate.  Assume
there are predicates `I_m^to,E_m^to` such that

\[
 \mathcal F_m^\to(X,Y,Z)
 \quad\Longleftrightarrow\quad
 \mathcal I_m^\to(X,Y)\wedge\mathcal E_m^\to(Y,Z).      \tag{3.1}
\]

Every aggregate coordinate in `Y` must have a proved composition law, and
every actual address, capacity-one occurrence, history or guard relation
crossing from `X` to `Z` must factor through `Y`.  Put

\[
 Q_m^\to(Y)\quad\Longleftrightarrow\quad
                 \exists X\ \mathcal I_m^\to(X,Y).      \tag{3.2}
\]

For an independent terminal copy, let

\[
 Q_m^{\rm term}(Y;C)
\]

mean that some terminal bulk realization compatible with the parent
boundary `Y` has one-phase charge at most `C`.  That terminal realization
may use a different child carrier and different bulk variables from (3.2).
It may also use a different parent-interior representative over `Y`: in this
section the induction state is the existential boundary certificate `Y`,
not one fixed interior `X`.  If a proposed recursion instead consumes a
specified literal parent interior, this replacement is legal only after
proving that the interior can be rematerialized from `Y`, or after proving
the two fork relations left-total on every retained representative.

### Theorem 3.1 (continuation-only separator criterion)

Suppose `Y_m` has uniformly bounded literal serialization and:

1. `Q_m^to(Y_m)` holds;
2. `E_m^to(Y_m,Y_(m+1))` holds and realizes the next auxiliary boundary;
3. `Q_m^term(Y_m;C_o)` and the analogous even predicate with charge `C_e`
   hold.

Then `Y_m` is a sufficient carried state and (2.5) follows.

No factorization of the terminal predicate through a future exterior is
required.  In particular, terminal variables may have an unbounded
dependency graph internally without enlarging `Y_m`.

#### Proof

By (3.1)--(3.2), existentially quantifying `X` produces a valid
continuation child and the boundary `Y_(m+1)`.  On a separate copy of the
same parent boundary, the two terminal predicates produce the odd and even
readouts.  Theorem 1.1 now applies.  Since no descendant is attached to a
terminal child, there is no terminal `Z` and hence no terminal separator
condition to verify.  \(\square\)

This is strictly weaker than demanding a complete boundary for one child
which is simultaneously terminal and regenerative.  It does not weaken
(3.1) inside the continuation branch: a hidden bulk-to-future edge there
still invalidates the proposed state.

## 4. The exact exported-state ledger

The smallest proof-safe carried object is therefore the complete
continuation boundary `Y`, not the complete terminal certificate.  In the
current architecture its possible fields are exactly the fields actually
read by the next same-parity construction:

| field | carry it exactly when ... |
|---|---|
| topology/root/opening ports | the next child glues to those literal occurrences rather than rematerializing them |
| positive and negative boundary histories | a crossing run is continued rather than reset before the next seam |
| cap reserve/current/debt | upper support in the next child uses inherited reserve rather than a fresh support certificate |
| protected pull/reservoir occurrences | the next pull criterion consumes those same capacity-one facts |
| provider/socket identities | the continuation router uses them as literal sources or sinks |
| unresolved target identities | the next transition promises to repair them rather than paying them in a terminal branch |
| phase or orientation metadata | the continuation relation distinguishes it and no proved conjugacy erases it |

Every omitted field needs one of three proofs: child-local rematerialization,
an exact compositional aggregate, or a literal reset.  Merely having few
formal coordinates is not enough; their physical serialization and every
cross-boundary dependency must be bounded.

By contrast, on the direct-ray terminal branch the following are erased
unconditionally from the **continuation** state once their terminal
existence is proved:

\[
 \epsilon,\quad (K,F,a,b,c,\infty,s),\quad
 \Pi^\epsilon,\quad A,\quad H_A^{\Pi^\epsilon},\quad
 M_{\rm term},\quad H_{\rm repair}.                    \tag{4.1}
\]

Native sockets and their typed state are also erased when they serve no
continuation purpose.  If they are used to prove the continuation router,
they move back to the first table and must be included in `Y` or
rematerialized there.  The same qualification applies to any upper witness,
cap occurrence or ring reservoir used in both roles.

### Corollary 4.1 (leaf-only packet planting)

For the additive-constant programme, it is sufficient to plant the actual
`Ibc/Ica` packet only in the terminal fork.  Its deadline-dependent filler
order, its `2(d-1)` ray bank and its clipped residence boundary need not be
regenerated at the next dimension.  The exact local template-regeneration
theorem remains available, but it is not a logical prerequisite on this
forked route.

Under Corollary 1.3 the statement is weaker still: intermediate auxiliary
states need not contain any terminal packet at all.  For each requested
horizon, plant it only in the terminal leaf.  This is conditional on a
terminal planting theorem from that leaf; it is not a claim that every
current auxiliary carrier already has a suitable slot.

This corollary does not say that packet planting in the terminal host is
easy.  That child must still be globally resident and upper-complete and
must satisfy the one-phase inverse/Hall gate.

## 5. Revised shortest missing theorem

Within the present architecture, the former one-child target can be
replaced by the following two-child statement.

### Forked regenerative guarded extension `FRGE(C_o,C_e)`

There is a uniformly bounded family of auxiliary continuation boundaries
such that every selected parent boundary has:

1. **Continuation child.**  A possibly nonterminal child satisfying the
   complete continuation factorization (3.1), exporting another boundary
   in the same family.  It carries all topology, residence, cap, pull and
   provider data actually read by the next step, but no terminal compiler
   data.
2. **Odd terminal fork.**  On an independent copy of the parent, an
   upper-complete globally resident carrier with a coherent ring, protected
   upper reservoir and actual `Ibc/Ica` occurrence satisfying the forced
   graphic/cographic pull criterion, together with one global nonempty
   antecedent extending one phase's forced rays and one guard-pruned
   residual matching of total charge at most `C_o`.
3. **Even terminal fork.**  An independent even child with the analogous
   charge at most `C_e`.

Then

\[
                    \nu(k)\le B(k)+\max\{C_o,C_e\}      \tag{5.1}
\]

from the first valid dimension onward.

The two forks share only the auxiliary parent certificate or its proved
complete continuation boundary.  Their child carriers, packet parameters,
pull phases, cap states, antecedents and matchings may all differ.

## 6. Exact caveats

The theorem removes a correlation, not an existence problem.

1. Cloning is logical reuse of a finite certificate.  It does not put two
   child factors on one physical word and proves no simultaneous resource
   disjointness.
2. The continuation child must still satisfy every exported row in one
   literal state.  Terminal erasure cannot hide a continuation dependency.
3. A terminal fork must be constructible from the declared parent state.
   Existence of an unrelated good carrier at the same dimension is not a
   transition theorem unless the auxiliary state was deliberately defined
   to permit such rematerialization.
   Likewise, the continuation-only quotient of Section 3 uses existential
   boundary-state semantics; it cannot silently replace a recursion which
   consumes a fixed literal parent interior.
4. Bounded formal state cardinality is insufficient if its literal
   serialization, history matrix, cap reserve or dependency closure grows
   with `d`.
5. The odd and even readout relations are separate.  An odd-only fork gives
   no even-dimensional conclusion.
6. The terminal `Theta(d)` ray facts cost no additional positions only
   because they are realized at distinct intervals already present in the
   terminal antecedent.  Appended packet cells or extra split positions
   remain part of `chi`.
7. The present local `Ibc/Ica` theorem supplies neither a global terminal
   antecedent nor bounded guard-pruned Hall.  The bare three-ring and upper
   reservoir theorems likewise do not construct an initially
   upper-complete resident terminal carrier.

Thus `FRGE` is not yet proved.  Its gain is exact: terminal one-phase
compiler data and packet regeneration are deleted from the auxiliary
same-parity state, and the former same-child extension theorem splits into
two independent child constructions.

## 7. Dependencies

* `MATH_THEOREM_SERIAL_ONE_PHASE_FORCED_RAY_TERMINAL_REDUCTION_20260804.md`;
* `MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`;
* `MATH_THEOREM_BOUNDED_COMPILER_EVICTION_AND_PHASE_DECOUPLING_20260801.md`;
* `MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md`;
* `MATH_THEOREM_FRESH_TICKET_BOUNDARY_ERASURE_AND_BOUNDED_RESET_STATE_20260802.md`;
* `MATH_THEOREM_LITERAL_OCCURRENCE_FACT_COALESCENCE_AND_IBC_ICA_BACKGROUND_REDUCTION_20260804.md`; and
* `MATH_SYNTHESIS_PURE_MATH_FRONTIER_20260804.md`.
