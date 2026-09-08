# Independent audit: passive terminal elimination and direct `Ibc/Ica` rays

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Audited source SHA-256:**
`4d9d64199a47eb3f171095f5f49c65f466557fc716b09a58ea5c95f1e75ca506`
  
**Corrected source:**
`MATH_THEOREM_PASSIVE_TERMINAL_TYPE_ELIMINATION_AND_DIRECT_IBC_ICA_CLOSURE_20260804.md`

## Verdict

`GO WITH A REQUIRED SCOPE CORRECTION`.

The conservative-extension theorem and direct literal-terminal theorem are
correct.  Corollary 3.2 is also correct: in one fixed phase the
`2(d-1)` displayed aligned ray facts form a genuine target-simple,
occurrence-simple matching, so their native sockets are unnecessary **for
that final target-coverage row**.

The conclusion must not be promoted to a deletion of the sockets from the
current global common-cap architecture.  In that architecture the native
ports/suffixes perform a non-target service: they carry the two physical
occurrence coordinates in a gain/compensation linkage used to prove the
complementary compiler.  Their terminal type can therefore remain active.
The direct-ray corollary replaces that router only after a complementary
literal matching has been proved by some other argument.

The audited theorem has been amended to state this boundary explicitly.

## 1. Conservative-extension audit

Definition 1.1 is the exact sufficient hypothesis.  If `tau(b)` is a
deterministic annotation of the already fixed physical record and every
downstream predicate factors through that record, then adjoining `tau(b)`
adds neither a choice nor a literal/capacity constraint.  Projection and
unique relabelling are inverse operations.

There are two important qualifications.

1. The extension is a labelled extension of the state; it does not prove an
   old externally prescribed allowed-type predicate.  The original phrase
   "declare ... accepted" could be read as changing such a predicate.  It
   has been replaced by "record ... in a newly adjoined bookkeeping field."
2. Determinism alone does not imply passivity.  A deterministic terminal
   label may select an allowed sink, guard, or next transition.  Such a
   label violates Definition 1.1(4) and cannot be erased.

For the one-bundle-per-labelled-ticket application, using the indexed
ticket labels retains multiplicity, so the displayed projection is indeed
bijective.  If one allowed several indistinguishable records per ticket,
the set in (1.4) would need to be read as an indexed family or multiset; that
case is not used here.

## 2. Direct literal-terminal theorem

Theorem 2.1 is forced-edge contraction in the literal target/occurrence
graph.  Let `E_*` be target- and occurrence-disjoint and let `M_0` be the
matching on the residual graph.  Then

\[
                         M=E_*\mathbin{\dot\cup}M_0
\]

is a matching saturating the whole target shore.  Fact coalescence is sound
because all roles retained at an occurrence assert the same address, value,
and literal state.  Every noncoalescible capacity is charged in `B_*`.

No terminal signature occurs in the definition of this final matching.
Thus the theorem is correct, but its residual-matching hypothesis already
contains the unresolved global compiler content.  It is not a construction
of that matching.

## 3. Exact check of Corollary 3.2

Fix one phase `epsilon`.  The ray targets are

\[
 X_j^\epsilon=J\cup\{x_\epsilon\}\cup P_j,
 \qquad
 Y_j^\epsilon=J\cup\{y_\epsilon\}\cup S_j,
 \qquad 1\le j<d.
\]

They are pairwise distinct for three independent reasons.

1. `P_1 subset ... subset P_(d-1)`, so the `X_j` are distinct.
2. `S_1 supset ... supset S_(d-1)`, so the `Y_j` are distinct.
3. `x_epsilon != y_epsilon`; every `X_j` contains `x_epsilon` and excludes
   `y_epsilon`, while every `Y_j` contains `y_epsilon` and excludes
   `x_epsilon`.  Hence no prefix target equals a suffix target.

Their addresses are also pairwise distinct.  Prefix addresses lie in the
first block and have different right endpoints; suffix addresses lie in the
second block and have different left endpoints.  The two blocks are
disjoint.  The aligned ambient theorem proves all displayed OR equalities
in one literal antecedent `A^epsilon`.

Therefore

\[
 E_{\rm ray}^\epsilon
 =\{(X_j^\epsilon,e^X_j),(Y_j^\epsilon,e^Y_j):1\le j<d\}
\]

is a sound matching of size `2(d-1)`.  Calling these edges "forced" means
that the proof designates them before solving the complementary matching;
it does not mean that every possible compiler must select them.

This proves the precise claim of Corollary 3.2.

## 4. Does the global architecture use sockets for a non-target service?

Yes.

The terminal common-cap theorem does not introduce native socket
occurrences merely as witnesses of `X_j,Y_j`.  Its two systems are the two
physical occurrence coordinates required by every logical ticket, after a
background/compensation linkage has been protected.  The port-to-sink
paths certify simultaneous linkability in a fixed cap state.

Likewise, the regular-incidence factor theorem begins after fixing one
compensation linkage and uses private claim-to-port prefixes plus typed
port-to-sink suffixes to link all gain claims.  This is routing service, not
the assertion `OR(e)=X_j` or `OR(e)=Y_j`.

Accordingly there are two distinct proof branches.

### Direct-literal final branch

Preselect `E_ray^epsilon`, prove a complementary literal target/cell
matching, and present their union as the final compiler.  The native socket
and its type are unnecessary unless another theorem consumes them.

### Existing common-cap router branch

Use the native socket as an occurrence-labelled route for gain/compensation
or two-coordinate linkage.  Here a sink type, guard, endpoint class, or
future state may affect legality.  The type is active until the route and
its accepted terminal have been proved.  Pairwise-disjoint deterministic
bundles remove representative ambiguity but do not turn a rejected terminal
into an accepted one.

The two branches may ultimately certify the same final word, but the first
cannot be cited as proof of the second's routing premise.

## 5. Regeneration boundary

At a final OR word, a polarity annotation with no remaining consumer is
passive.  At a same-parity induction boundary it is passive only if every
child continuation factors through the type-free physical record.  If the
next lift distinguishes the two polarities, terminal type is an exported
state variable and Proposition 4.2 applies.

Thus Corollary 3.2 does not establish regeneration.  Nor does it remove a
socket used as a topology connector, compensation path, or next-state
boundary.

## 6. Correct frontier

The strongest proof-safe conclusion is

\[
\boxed{
\begin{array}{l}
\text{the aligned ray targets need no native socket for final literal
coverage;}\\
\text{their direct matching still needs a complementary matching in the
same state;}\\
\text{the existing route-based common-cap proof still needs its sockets
and active types.}
\end{array}}
\]

This is a useful semantic simplification, not closure of the common-cap or
regenerative row.

## 7. Sources checked

- `MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`
- `MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`
- `MATH_THEOREM_LITERAL_OCCURRENCE_FACT_COALESCENCE_AND_IBC_ICA_BACKGROUND_REDUCTION_20260804.md`
- `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`
- `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`
- `MATH_SYNTHESIS_PURE_MATH_FRONTIER_20260804.md`
