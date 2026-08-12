# Directed-history port monoid and the one-aperture pivot reset

**Date:** 2026-08-02  
**Status:** unconditional all-`k` finite-state composition theorem for the
positive-residence row of literal directed Johnson paths, cycles, and
protected port splices.  Quotient lifts are phase-free on free owner
orbits; periodic owner orbits require a stabilizer-coset state.  The
asymmetric one-aperture pivot is an exact history-reset packet.  The theorem
gives a closed recursive state interface; it does not prove that a
canonical Pascal host realizes the required state, and it makes no
upper-shadow, source-envelope, topology, or compiler claim.

## 0. Outcome

Raw short-run blockers can be replaced by one exact finite relation.

For a directed rank-`r` Johnson transition

\[
                         T\longrightarrow T-a+b,
\tag{0.1}
\]

remember the last `d` inserted coordinate labels, newest first.  The
transition is depth-`d` positive-resident exactly when `a` is absent from
that ordered history; its new history is obtained by shifting in `b`.

Thus every directed path `P` carries a partial history map `Phi_P`.
Concatenation is ordinary composition, a directed cycle is resident exactly
when its map has a fixed point, and a freeze-after-rectangle splice is
resident exactly when the two child path maps and the two crossed-edge maps
have a common fixed point.  The exact private closing-port state therefore
extends from

\[
                         (w;c\mid P,T)
\]

to

\[
                         (w;c\mid P,T;\mathcal R_d),
\tag{0.2}
\]

where `mathcal R_d` is the endpoint history relation.  These states are
closed under composition.  Rail/cap compatibility and residence
compatibility remain separate coordinates of the state.

For an equivariant quotient on free owner orbits, a directed option already
records the unique relative frame change.  Apply that frame change to every
shifted history label.  No independent phase variable is needed.  Periodic
owner orbits instead require the stabilizer-coset correction in Section 2.
At `k=17,d=3` all nontrivial owner orbits are free, and this specializes
exactly to the three canonical-frame labels in
`MATH_THEOREM_K17_PHASE_FREE_DIRECTED_HISTORY_MASTER_20260802.md`.

The asymmetric pivot from
`MATH_THEOREM_K_ONE_APERTURE_PASCAL_PIVOT_BPLUS1_BRIDGE_20260802.md`
is especially useful.  Its deletion bank and insertion bank are disjoint,
and after its `d` owner transitions the output history is fixed,
independently of the input.  It is therefore a literal history reset, with
one explicit triangular input guard.  This is the residence state which a
regenerative aperture/Pascal theorem should export.

## 1. The history automaton

Let `Omega` be the coordinate set and let

\[
                    \mathsf H_d=\Omega^d
\tag{1.1}
\]

be the ordered history space.  Repetitions may be retained formally; on a
valid depth-`d` resident Johnson walk the actual last `d` insertions are
distinct.

For a transition label `(a,b)`, define the partial map

\[
 \tau_{a,b}(h_1,\ldots,h_d)
   = (b,h_1,\ldots,h_{d-1})
\tag{1.2}
\]

if

\[
                         a\notin\{h_1,\ldots,h_d\},
\tag{1.3}
\]

and leave it undefined otherwise.

### Theorem 1.1 (exact positive-residence automaton)

Let

\[
 T_0\xrightarrow{(a_1,b_1)}T_1
       \xrightarrow{(a_2,b_2)}\cdots
       \xrightarrow{(a_m,b_m)}T_m
\tag{1.4}
\]

be a directed Johnson path.  Given the actual last-`d` insertion history
`H` before the first transition, the concatenated owner chronology has no
positive coordinate run of length at most `d` if and only if

\[
 \Phi_P(H):=\tau_{a_m,b_m}\circ\cdots\circ
                    \tau_{a_1,b_1}(H)
\tag{1.5}
\]

is defined.

#### Proof

A coordinate deleted on the current transition has a positive owner run of
length at most `d` exactly when its most recent insertion is one of the
previous `d` transitions.  Those labels are exactly the entries of the
current history.  Condition (1.3) excludes precisely this event, while
(1.2) records the new last-`d` insertion list.  Induct along (1.4).
\(\square\)

This is the transition-label version of the insertion-to-next-deletion
flip-gap theorem.  It checks only positive residence.  Negative residence
uses the dual automaton obtained by exchanging insertions and deletions.

### Corollary 1.2 (path and cycle relations)

Define

\[
 \mathcal R_d(P)=
   \{(H,H'): \Phi_P(H)=H'\}.
\tag{1.6}
\]

For concatenable paths,

\[
 \mathcal R_d(PQ)=\mathcal R_d(Q)\circ\mathcal R_d(P).
\tag{1.7}
\]

A directed cyclic word `C` is depth-`d` positive-resident if and only if

\[
                         (H,H)\in\mathcal R_d(C)
\tag{1.8}
\]

for its actual cyclic history `H` (equivalently, for some consistent
history fixed point).

The reverse orientation is handled by reversing the transition order and
replacing every `(a,b)` by `(b,a)`.  Cyclic run lengths are preserved by
reversal, although the forward history tuple itself is not generally the
same tuple.

### Theorem 1.3 (explicit boundary-collar recurrence)

Let `P,Q` be internally depth-`d` positive-resident directed Johnson paths,
each having at least `d` transitions.  If

\[
 P:(a_1,b_1),\ldots,(a_m,b_m),
\]

define the ordered boundary collars

\[
 D(P)=(a_1,\ldots,a_d),\qquad
 I(P)=(b_m,b_{m-1},\ldots,b_{m-d+1}).                 \tag{1.9}
\]

Thus `I_i(P)` is the `i`-th most recent insertion at the right endpoint,
whereas `D_j(P)` is the `j`-th deletion after the left endpoint.  If the
end of `P` is the start of `Q`, then `PQ` is internally resident exactly
when

\[
              I_i(P)\ne D_j(Q)
              \qquad(i+j\le d+1).                    \tag{1.10}
\]

If instead a connector transition `e=(a,b)` is inserted between the two
paths, then `PeQ` is internally resident exactly when

\[
\begin{aligned}
 a&\ne I_i(P) &&(1\le i\le d),\\
 b&\ne D_j(Q) &&(1\le j\le d),\\
 I_i(P)&\ne D_j(Q) &&(i+j\le d).
\end{aligned}                                         \tag{1.11}
\]

In either case the outer state is

\[
 D(PQ)=D(P),\quad I(PQ)=I(Q),
 \qquad
 D(PeQ)=D(P),\quad I(PeQ)=I(Q).                       \tag{1.12}
\]

Reversal exchanges the collars:

\[
                         D(\overleftarrow P)=I(P),
              \qquad I(\overleftarrow P)=D(P).        \tag{1.13}
\]

#### Proof

An insertion `I_i(P)` occurs `i-1` transitions before the end of `P`.
The deletion `D_j(Q)` is the `j`-th transition after that end, so their
edge-index difference is `i+j-1`.  This gives (1.10).  With a connector,
its deletion is `i` transitions after `I_i(P)`, its insertion is `j`
transitions before `D_j(Q)`, and the old cross pair is separated by
`i+j` transitions.  These are exactly (1.11).  Because both paths have at
least `d` transitions, the first collar comes wholly from `P` and the last
wholly from `Q`, proving (1.12).  Reversing an edge swaps its deletion and
insertion and reverses edge order, which gives (1.13). \(\square\)

For shorter correction fragments, formulas (1.9)--(1.13) must be replaced
by the full relation (1.6), or equivalently by the first and last `d`
transition pairs together with the fragment length capped at `d`.  Keeping
only the two collars in (1.9) is not closed under concatenation when a
fragment has fewer than `d` transitions.

## 2. Equivariant frame transport

Let a group `Gamma` act on `Omega`, and assume here that the owner orbits in
use are free (more generally, that every directed option carries a unique
chosen frame change).  A directed quotient option from canonical owner `u`
to canonical owner `v` carries a frame change `gamma_e in Gamma`, together
with deletion/insertion labels `(a_e,b_e)` in the frame at `u`.  Define

\[
 \tau_e(h_1,\ldots,h_d)=
 \bigl(\gamma_e^{-1}b_e,
       \gamma_e^{-1}h_1,\ldots,
       \gamma_e^{-1}h_{d-1}\bigr)
\tag{2.1}
\]

when `a_e` is absent from the input history.

### Theorem 2.1 (phase-free quotient history)

Under the free-orbit/unique-frame hypothesis, the fixed-point and
composition statements of Section 1 remain exact with the maps (2.1).  In
particular a quotient directed cycle cover is
depth-`d` positive-resident in every physical lift if and only if one can
assign one canonical-frame history to every quotient owner so that every
selected arc applies (2.1).

#### Proof

In the physical frame the update is (1.2).  Re-expressing the inserted
label and all retained history entries in the canonical frame at `v`
applies `gamma_e^{-1}` componentwise, giving (2.1).  Around a quotient
component, the physical occurrence and all absolute labels acquire the
same accumulated group shift.  Returning to the canonical frame cancels
that shift, so one state at the quotient owner is sufficient.  Conversely,
propagating a canonical assignment by (2.1) gives consistent histories on
every physical translate. \(\square\)

For the `Z_17` convention in the finite master, `gamma_e^{-1}` is
subtraction by the voltage `delta`.  At `d=3`, (2.1) is exactly

\[
 h_1(v)=b-\delta,\qquad
 h_j(v)=h_{j-1}(u)-\delta\quad(j=2,3),
\]

together with deletion exclusion.  This proves the interface-level match;
it does not promote any SAT status to an all-`k` existence theorem.

If an owner has a nontrivial stabilizer, the quotient endpoint does not
determine one frame change.  Then (2.1) must be augmented by the relevant
stabilizer coset/phase state.  Dropping that field is not valid in general.
For the nontrivial ranks under the prime cyclic `Z_17` action, the owner
orbits are free, so the finite master needs no such augmentation.

## 3. Exact history state for a private port splice

Cut the distinguished closing edge of a private-rooted directed child
cycle.  Let `P_epsilon` be the resulting directed path and let `e_01,e_10`
be the two crossed transitions used to splice two children.  In the cyclic
order induced by the splice, put

\[
 \Phi_{\rm splice}
   =\tau_{e_{10}}\circ\Phi_{P_1}\circ
      \tau_{e_{01}}\circ\Phi_{P_0},
\tag{3.1}
\]

with frame transports inserted when the children use different canonical
frames.

### Theorem 3.1 (history-ported rectangle calculus)

Assume the ordinary port square is literal: the rails agree and both
crossed Boolean cap incidences exist.  Then the spliced directed cycle is
depth-`d` positive-resident if and only if `Phi_splice` has a consistent
fixed history.  If one crossed edge is left open instead, the resulting
path exports exactly the relation of the corresponding composition with
that edge omitted.

Consequently the state (0.2) is closed under every private Pascal splice.
A bounded correction packet transports residence by relational
composition; it need not re-enumerate raw short-run motifs.

#### Proof

Every transition internal to a child occurs in `Phi_(P_epsilon)`, and the
only new transitions are `e_01,e_10`.  Equation (3.1) is therefore the
complete transition word of the spliced cycle.  Apply Corollary 1.2.
Omitting one edge gives the path statement. \(\square\)

### Corollary 3.2 (two-seam collar test and regenerative state)

Assume each cut child path has at least `d` transitions.  Then

\[
                       P_0e_{01}P_1e_{10}              \tag{3.2}
\]

is resident if and only if (1.11) holds for both triples

\[
                         (P_0,e_{01},P_1),
                  \qquad(P_1,e_{10},P_0).              \tag{3.3}
\]

If `e_10` is retained as the new closing port, the open parent path exports

\[
                         (D(P_0),I(P_1));               \tag{3.4}
\]

retaining `e_01` instead exports `(D(P_1),I(P_0))`.  Hence two children
with one common collar pair `(D,I)` regenerate that pair whenever every
used crossed connector passes (1.11).  More generally the endpoint-state
recurrence is the same cross-product rule as the port-box recurrence:

\[
               (D_0,I_0),(D_1,I_1)
                    \longmapsto (D_0,I_1)
                    \quad\hbox{or}\quad(D_1,I_0).       \tag{3.5}
\]

Two fresh copies of a target collar pair therefore reset both endpoint
coordinates in two splices, provided all four literal connector tests pass.
This is a residence theorem for a supplied guarded box, not a theorem that
the Pascal child menus contain such a box.

The theorem is exact but not an existence assertion.  The rail/cap square
may have no history-compatible fixed point, and a static walk in the port
`C4` complex need not have fresh catalyst occurrences or compatible
history relations.

## 4. The one-aperture pivot is a reset

For the asymmetric pivot owner path, list its transition labels in order:

\[
\begin{aligned}
 (a_1,\ldots,a_d)
   &=(\ell,\lambda_{d-1},\ldots,\lambda_1),\\
 (b_1,\ldots,b_d)
   &=(\rho_1,\rho_2,\ldots,\rho_{d-1},\mu).
\end{aligned}
\tag{4.1}
\]

The two banks are disjoint.

### Theorem 4.1 (exact pivot reset map)

For an incoming history `H=(h_1,...,h_d)`, the pivot map is defined if and
only if

\[
 a_t\notin\{h_1,\ldots,h_{d-t+1}\}
                  \qquad(1\le t\le d).
\tag{4.2}
\]

Whenever it is defined,

\[
 \Phi_{\rm pivot}(H)
             =(\mu,\rho_{d-1},\ldots,\rho_1),
\tag{4.3}
\]

independent of `H`.

#### Proof

Before transition `t`, the history consists of the `t-1` most recent local
insertions followed by `h_1,...,h_(d-t+1)`.  The current deletion label
`a_t` is disjoint from every local insertion label, so the exclusion test
reduces exactly to (4.2).  After all `d` transitions, all incoming entries
have shifted out and the newest-first local insertion word is (4.3).
\(\square\)

The strong sufficient guard

\[
              \{a_1,\ldots,a_d\}\cap
                 \{h_1,\ldots,h_d\}=\varnothing
\tag{4.4}
\]

makes the reset legal.  The triangular condition (4.2) is the exact weaker
test.

Under fixed-depth rank suspension, the added coordinate belongs to the
persistent core `X` and never labels a transition, so (4.1)--(4.3) are
unchanged.  Under a one-step depth suspension, one new deletion and one new
insertion extend the two banks and the reset length by one.  Hence the
aperture/pivot module exports a regenerative history relation as well as a
regenerative cap/rail state.

### Corollary 4.2 (minimal reset-port history field)

For this `d`-transition packet the full relation is determined by

\[
 \bigl((a_1,\ldots,a_d),
       (\mu,\rho_{d-1},\ldots,\rho_1)\bigr)
\tag{4.5}
\]

and the triangular test (4.2).  The persistent ordered rail supplies
`rho_1,...,rho_(d-1)`; the terminal insertion `mu` is one indispensable
additional field.  Same rail and Boolean cap containment alone are
insufficient: a following edge may delete `mu`, or may delete a `rho_j`
before it leaves the history.

### Proposition 4.3 (source-letter pivot guard is separate)

The reset theorem concerns the directed owner path (4.1).  A monotone
source-letter insertion

\[
                        A_L\mid A_R
                \longmapsto A_L,X,A_R,
        \qquad X\subseteq A_L\cup A_R                 \tag{4.6}
\]

preserves every old interval OR, but does not automatically preserve
positive source-letter residence.  For

\[
                   x\in(A_L\cap A_R)\setminus X,       \tag{4.7}
\]

the insertion splits one old positive run into its left and right pieces.
It is depth-`d` resident exactly when both pieces have length at least
`d+1` for every `x` in (4.7), in addition to the old word being resident.
No other coordinate creates a new or shorter positive run.  Hence

\[
                        A_L\cap A_R\subseteq X
                        \subseteq A_L\cup A_R          \tag{4.8}
\]

is the uniform no-split sufficient condition; the weaker exact condition
is decided by the two one-sided run ages, capped at `d+1`.

Thus the owner-history reset (4.2)--(4.3) and the physical source-word
collar guard (4.7) are separate coordinates of a proof-safe recursive
state.  Neither follows from the other.

## 5. The all-`k` closed state and its remaining gate

A proof-safe recursive protected port may export

\[
 \boxed{
   (\text{payload},\ w;c\mid P,T,\
    \mathcal R_d^+,\mathcal R_d^-,\
    \text{opening/topology state}) .}
\tag{5.1}
\]

Here `mathcal R_d^+` is the insertion-history relation above and
`mathcal R_d^-` is its deletion-history dual.  Keeping both makes the state
stable under orientation reversal and controls positive and negative runs.
Every ordinary rectangle splice, bounded packet, and path opening updates
(5.1) by exact relation composition.

This answers the interface question: residence can be transported as a
finite directed-history state rather than rediscovered as raw run blockers.
The one-aperture pivot gives a particularly simple constant-output relation.

What remains is an existence theorem:

> construct the Pascal children and their protected port/correction bank so
> that the rail/cap square, payload partition, topology opening, and the two
> history relations in (5.1) are simultaneously compatible.

The state has `O(d)` labels but exponentially many possible values if
tabulated naively.  The pivot reset compresses its output to one tuple;
its input domain is the triangular avoidance system (4.2).  No theorem here
proves that the canonical child menus contain such a compatible reset, nor
that upper shadows or the terminal common-cap compiler survive it.

## 6. Exact scope relative to `k=17`

The finite `k=17` master eagerly enforces the positive half of (5.1) with
`d=3` on every selected quotient arc.  The cyclic group has prime order
seventeen, so a rank-nine subset has trivial rotational stabilizer: a
nontrivial rotation is transitive on the coordinates and can fix only the
empty or full set.  Thus no stabilizer-coset field is missing.  The master
also keeps its separately audited owner, lower-q1, and rank-ten base
clauses.  A satisfying model would still need quotient connectivity,
nonzero voltage, physical replay, deeper upper shadows, source envelopes,
and the complete compiler.

Accordingly the finite master is an exact calibration of the general
history state, not evidence that the all-`k` recursive existence lemma is
already true.
