# Correlated C6 cover-down: endpoint permutations and closed socket routing

Date: 2026-07-31  
Lane: AD  
Status: exact endpoint-permutation reduction, exact transposition distance and
socket-group criterion, exact slot-closure obstruction, and an exact
conditional composition with planted C6 cover-down.  This does **not**
construct the required Boolean socket atlas, prove positive-density aligned
planting, regenerate a word-compiler cap, or prove `nu=B`.

## 0. Verdict

The planted C6 and sparse-cycle layers have a further exact separation.

* A planted C6 supplies one unit of matching gain.
* A sparse `C_(2 ell)` switch has zero boundary on both outer palette
  **sets**, but can change the lower-to-upper pairing (hence the local cap
  bijection), physical routing, and literal slots.
* The one-complement-reset-per-augmented-cycle condition is exactly an
  endpoint-permutation identity condition.

If there are `k` complementary reset labels and the augmented factor has
`c` directed cycles, then the exact abstract endpoint debt is

\[
                              k-c.                         \tag{0.1}
\]

This is both the minimum number of unrestricted terminal transpositions and,
when every permutation cycle has a safe pivot star, the exact number of
socket packets needed.  In the three-sector Catalan step,

\[
 k=\operatorname {Cat}_{n+1}-\operatorname {Cat}_n
   ={3P\over n-1},\qquad P={2n\choose n-2}.             \tag{0.2}
\]

Thus endpoint routing has Catalan scale `O(P/n)`, not linear scale `Theta(P)`.

There is, however, a load-bearing slot obstruction.  Once the normalized
side host is perfectly covered, every legal count-neutral replacement has
zero **pointwise** resource displacement.  A single sparse cycle has slot
displacement `chi_P-chi_Q ne 0`, because its old-only and new-only owner
banks are disjoint.  It therefore cannot be applied by itself after C6
completion.  A valid endpoint router must be either

1. used before C6 activation, with the sum of its slot displacements equal
   to the target-slot leave; or
2. packaged into a closed composite whose total literal-slot displacement
   is zero.

This gives the exact next catalogue target: a stateful family of
outer-neutral endpoint-transposition sockets, together with either a
target-slot signature or a zero-slot closure.  Containment of every
permutation cycle in one socket component is necessary and, for a
word-closed atlas, sufficient **only for the permutation projection**.
The joint permutation--slot signature is a separate exact reachability row.
Physical serialization, rooted graphic rank, capacities, cumulative reserve
and the downstream compiler remain literal guards.

## 1. Endpoint permutation of an augmented factor

Let `I` be a set of `k` endpoint labels.  For every `i in I`, fix a start
vertex `s_i`, a terminal vertex `t_i`, and an artificial complementary reset

\[
                         r_i:t_i\longrightarrow s_i.           \tag{1.1}
\]

Let `Z` be a directed two-factor containing every reset exactly once.
Assume that deleting the reset bank

\[
                            R=\{r_i:i\in I\}                    \tag{1.2}
\]

leaves no directed cycle.  This last hypothesis is the reset-free physical
cycle guard; it is not implied by endpoint counts.

### Theorem 1.1 (endpoint-permutation equivalence)

There is a unique permutation `sigma_Z in Sym(I)` such that the physical
part `Z-R` has a directed path

\[
                         s_i\leadsto t_{\sigma_Z(i)}             \tag{1.3}
\]

for every `i`.  The directed cycles of `Z` are in bijection with the cycles
of `sigma_Z`, with the same number of reset arcs.  Consequently

\[
 \begin{split}
 &\text{every augmented directed cycle contains exactly one reset}\\
 &\hspace{35mm}\Longleftrightarrow\quad \sigma_Z=\operatorname{id}_I.
 \end{split}                                                   \tag{1.4}
\]

#### Proof

Deleting all resets removes one incoming arc at every `s_i` and one outgoing
arc at every `t_i`.  Since the remainder has no directed cycle and all other
vertices retain indegree and outdegree one, it is a disjoint union of `k`
directed paths, each beginning at one `s_i` and ending at one `t_j`.
Disjointness makes the start-to-terminal map bijective, giving the unique
permutation.

Traversing `Z` from `s_i`, the physical path ends at
`t_(sigma_Z(i))`, and the next reset enters `s_(sigma_Z(i))`.
Thus successive reset labels follow the orbit of `i` under `sigma_Z`.
This proves the cycle correspondence and (1.4). `square`

### Corollary 1.2 (exact endpoint excess)

If `c(sigma)` is the number of permutation cycles, the number of resets in
excess of one per augmented cycle is

\[
                  \sum_{C\in\operatorname{cyc}(\sigma)}(|C|-1)
                    =k-c(\sigma).                              \tag{1.5}
\]

For the three-sector residual step, write
`K'=Cat_(n+1)-Cat_n`.  The Catalan ratios give

\[
 K'={3n\over n+2}\operatorname {Cat}_n,qquad
 P={n(n-1)\over n+2}\operatorname {Cat}_n,qquad
 K'={3P\over n-1}.                                             \tag{1.6}
\]

Hence the endpoint excess is always at most `3P/(n-1)-1` when `K'>0`.

## 2. Endpoint-transposition sockets

A **terminal transposition socket** for the unordered label pair `ij` is a
literal count-neutral packet which, on its declared input state,

1. preserves the lower and upper outer palettes pointwise;
2. changes the endpoint permutation from `sigma` to `(i j)sigma`;
3. leaves no reset-free directed cycle;
4. has a declared literal-slot leave displacement `d_(ij)`; and
5. passes its declared physical-capacity, rooted-graphic, reserve and
   protected-compiler guards.

The left action in item 2 means that the packet interchanges the two
terminal labels.  Start-interchanging sockets give the right-action dual.

Let `G_sock` be the graph on `I` whose edges are the available terminal
transpositions.  First ignore state-dependent availability and suppose the
atlas is **word-closed**: every word in the edge transpositions can be
realized sequentially, with the displayed permutation action and additive
slot displacement at every prefix.  This is a strong physical hypothesis,
not a consequence of local sparse-cycle existence.

### Theorem 2.1 (exact permutation-projection socket criterion)

For a word-closed atlas, the **permutation projection** can route `sigma` to
the identity if and only if every connected component of `G_sock` is
invariant under `sigma`.
Equivalently, every cycle of `sigma` lies wholly inside one connected
component of `G_sock`.

#### Proof

Transpositions on the edges of a connected graph generate the full
symmetric group on its vertex set.  Therefore the subgroup generated by
all socket edges is the direct product of the symmetric groups on the
connected components of `G_sock`.  It contains `sigma^(-1)` exactly when
`sigma` preserves every such component.  Word-closure turns an abstract
factorization of `sigma^(-1)` into a literal sequential routing word, but
does not by itself prescribe that word's terminal slot displacement.
`square`

The word-closure qualification is indispensable.  If using one socket
deletes a resource needed by the next, graph connectivity is only a group
relaxation.  Even with word-closure, Theorem 2.1 is only the first projection
of the joint criterion in Theorem 3.3 below.

### Theorem 2.2 (distance, bounded diameter, and pivot stars)

Every terminal-transposition correction of `sigma` uses at least

\[
                              k-c(\sigma)                       \tag{2.1}
\]

transpositions.  If every relevant component of `G_sock` has diameter at
most `Delta`, the algebraic correction has a word of length at most

\[
                 (2\Delta-1)\bigl(k-c(\sigma)\bigr).            \tag{2.2}
\]

If every cycle `C=(c_1 c_2 ... c_r)` of `sigma` has a pivot `c_1` for which
all star edges `c_1c_j`, `2<=j<=r`, are safe and serializable in the needed
order, then the lower bound is attained: exactly `r-1` sockets correct that
cycle, and exactly `k-c(sigma)` correct the whole permutation.

#### Proof

Multiplication by one transposition changes the number of permutation
cycles by exactly one.  Reaching the identity, which has `k` cycles, from a
permutation with `c(sigma)` cycles therefore needs at least (2.1).

Along a graph path of length `a`, conjugating its last edge successively
along the path expresses the transposition of the two path endpoints using
`2a-1` path-edge transpositions.  Express each cycle of `sigma^(-1)` using
`r-1` unrestricted transpositions and replace each by a shortest-path word.
This proves (2.2).

With products applied right-to-left,

\[
 (c_1c_2\cdots c_r)^{-1}
   =(c_1c_2)(c_1c_3)\cdots(c_1c_r).                  \tag{2.3}
\]

Since successive left actions multiply on the left, the physical socket
order is `(c_1 c_r),(c_1 c_(r-1)),..., (c_1 c_2)`.  Thus the pivot-star
packets, applied in that order,
correct the cycle using `r-1` sockets.  Summing over cycles proves the last
claim. `square`

At Catalan parameters, a constant-support pivot-star route therefore uses
only `O(P/n)` packet occurrences.  This is a scalar reserve calculation;
the packets sharing a pivot are not resource-private merely because their
number is small.

### Corollary 2.3 (uniform private-support scalar sufficient condition)

Suppose instead that a routing word is realized by packets with pairwise
disjoint old phases of at most `b` matching atoms each.  The host has scalar
room for the worst endpoint debt whenever

\[
                    b{3P\over n-1}\le P,
 \qquad\text{equivalently}\qquad n\ge3b+1.             \tag{2.4}
\]

Thus an old-phase-5 `C10`-sized socket passes this scalar test for `n>=16`;
a closed pair costing ten old atoms passes it for `n>=31`.  These thresholds
do not construct sockets, prove zero-slot closure, or handle a pivot bank
whose packets intentionally share endpoint resources.

#### Proof

Pairwise-disjoint old phases use at most `P` atoms.  Corollary 1.2 bounds the
required packet count by `3P/(n-1)`.  Multiplication by `b` gives (2.4).
`square`

## 3. Slot closure is mandatory

Write `inc(M)` for the pointwise typed-resource incidence vector of a host
matching `M`.

### Lemma 3.1 (perfect-state displacement obstruction)

Let `M` and `M'=(M-A) union B` be perfect matchings of the same normalized
typed host.  Then

\[
                              \operatorname{inc}(A)
                                =\operatorname{inc}(B)           \tag{3.1}
\]

pointwise on every lower, upper and literal-slot resource.

Consequently, a count-neutral packet between perfect states has zero
pointwise slot displacement.  In particular, one sparse Boolean
`C_(2 ell)` switch from the authoritative sparse-cycle theorem cannot be
applied alone after exact completion: its old-only slots `P_i` and new-only
slots `Q_i` are disjoint, so

\[
                 \sum_i\chi_{P_i}-\sum_i\chi_{Q_i}\ne0.         \tag{3.2}
\]

#### Proof

Both perfect matchings have incidence vector equal to the all-one supply
vector of the host.  Subtract their common retained part.  This gives
(3.1).  The sparse-cycle distinctness theorem says all displayed `P_i,Q_i`
are distinct, so (3.2) is nonzero. `square`

### Corollary 3.2 (the two legal routing modes)

Let `M` be a precompletion matching whose lower and upper leaves already
equal a planted C6 target bank `T_I`.  A serializable sparse-cycle socket
word `W` may precede C6 activation only if

\[
       L_S(M)+\sum_{w\in W}d_w=S(T_I),                         \tag{3.3}
\]

with the sign convention that `d_w` is the slot-leave displacement.
Alternatively, a simultaneous composite router acting between completed
perfect states must obey

\[
                              \sum_{w\in W}d_w=0.                \tag{3.4}
\]

Equation (3.4) is necessary, not sufficient: actual old phases, new-phase
compatibility, physical rank and protected guards remain to be checked.

### Theorem 3.3 (joint permutation--slot reachability)

Let `mathcal S` be the literal slot-resource set.  Fix a literal input state
`X` and let `W(X)` be its set of serializable socket words.  For
`w in W(X)`, record

\[
                \Psi_X(w)=(g_w,d_w)
                    \in\operatorname {Sym}(I)\times\mathbb Z^{\mathcal S},
                                                                         \tag{3.5}
\]

where `g_w` is the certified left action on the **decoded** endpoint
permutation and `d_w` is the pointwise slot-leave displacement.  In the
precompletion mode the certification includes the decoder-equivariance
square

\[
       \sigma\bigl({\cal D}_I(wX)\bigr)
           =g_w\,\sigma\bigl({\cal D}_I(X)\bigr),              \tag{3.6}
\]

and asserts that the decoder is defined, all required off phases remain
installed, and all on phases remain mutually compatible.

If `sigma_0=sigma(D_I(X))` and

\[
                         b=S(T_I)-L_S(X),                        \tag{3.7}
\]

then a precompletion socket correction exists exactly when

\[
                         (\sigma_0^{-1},b)\in\Psi_X(W(X)).      \tag{3.8}
\]

A postcompletion correction exists exactly when

\[
                         (\sigma_0^{-1},0)\in\Psi_X(W(X))       \tag{3.9}
\]

for the catalogue of literal perfect-to-perfect composites.  If all reverse
packets are certified and signatures are state-independent, the reachable
signatures form a subgroup of the direct product.  Otherwise they are only
a reachable language (or monoid), and replacing them by a lattice or group
is a relaxation.

#### Proof

The final endpoint permutation is `g_w sigma_0` by (3.6), so it is the
identity exactly when `g_w=sigma_0^(-1)`.  Slot-leave displacements telescope
pointwise.  Before activation the terminal leave must be `S(T_I)`, giving
`d_w=b`; between perfect states Lemma 3.1 forces `d_w=0`.  These conditions
are also sufficient by the definition of `W(S)`, which already contains
literal serializability and decoder compatibility. `square`

Theorem 2.1 is precisely the projection of (3.8)--(3.9) onto
`Sym(I)`.  It cannot certify the required slot coordinate.

In the reversible state-independent case, let

\[
 \Gamma=\langle(g_e,d_e):e\in E(G_{\rm sock})\rangle
      \le\operatorname {Sym}(I)\times\mathbb Z^S,
\qquad
 \Lambda_0=\{d:(\operatorname{id},d)\in\Gamma\}.       \tag{3.9a}
\]

Choose any word `w_0` whose permutation is `sigma_0^(-1)`.  Then the joint
criterion is equivalently

\[
                         b-d_{w_0}\in\Lambda_0.        \tag{3.9b}
\]

Indeed, two signatures with the same permutation differ by an identity-word
voltage, and conversely such a voltage may be appended.  This is generally
stronger than testing socket-graph connectivity and membership of `b` in
the unrestricted lattice generated by the `d_e` separately.

For example, take two endpoint labels and one reversible transposition
socket with scalar voltages `+1` and `-1`.  The socket graph is connected,
but every word with endpoint action `(12)` has odd voltage.  Hence the
postcompletion signature `((12),0)` is impossible.  More generally, if a
mod-two slot functional `lambda` has `lambda(d_e)=1` for every transposition
generator, then every reachable signature satisfies the mixed invariant

\[
                         \operatorname{sgn}(g)
                              =(-1)^{\lambda(d)}.       \tag{3.9c}
\]

If a pointwise outer pairing/cap state is protected, the complete signature
has a third nonabelian coordinate:

\[
 \widetilde\Psi_X(w)=(g_w,\gamma_w,d_w)
   \in\operatorname {Sym}(I)\times\operatorname {Sym}(D)
                  \times\mathbb Z^{\mathcal S},
                                                               \tag{3.9d}
\]

where `gamma_w` is the relative lower-to-upper pairing permutation.  Exact
routing is membership of

\[
                   (\sigma_0^{-1},\gamma_{\rm req},b)           \tag{3.9e}
\]

in this reachable signature set.  A fully frozen pointwise cap has
`gamma_req=id`; a cap protected only on `Z subseteq D` requires the terminal
pairing to agree on `Z`; and an existential local Boolean cap imposes no
prescribed `gamma_req`.  Thus avoiding every edited protected bottom is a
sufficient guard, not a necessary one: several packets may cancel their
outer-pairing actions.  Compiler chronology is not represented by
(3.9d).

### Lemma 3.4 (virtual balanced normalization)

Let `M` have complete typed leave equal to the disjoint C6 target bank
`T_I`, and suppose `O_i subseteq M`.  Put

\[
                          \overline M=M\cup T_I.                 \tag{3.10}
\]

Then `overline M` is a perfect host matching, and simultaneous C6 activation
is the balanced exchange

\[
       \bigcup_{i\in I}(O_i\cup\{T_i\})
             \longrightarrow \bigcup_{i\in I}N_i.              \tag{3.11}
\]

Conversely, deleting the target atoms from any such perfect old state gives
the planted deficient state.  If the physical projection of `overline M`,
together with a legal root-star set, is a rooted spanning tree `T`, let `A`
be the old labelled physical/root edges removed by the full C6/rerouter
packet and `E` its new labelled edges.  The final rooted state is legal
exactly when

\[
       |A|=|E|,qquad
       \det_{\mathbb F_2}
       \bigl(\mathbf1[a\in C_T(e)]\bigr)_{a\in A,e\in E}=1.     \tag{3.12}
\]

If the packets can be ordered so this matrix is block upper triangular,
the determinant is the product of the diagonal packet determinants.

#### Proof

The target bank is exactly the leave, so (3.10) is perfect.  The C6 resource
identity says

\[
       \operatorname{inc}(N_i)
        =\operatorname{inc}(O_i)+\operatorname{inc}(T_i),
\]

which proves (3.11) and the converse.  For (3.12), row-reduce the labelled
graphic representation of the old rooted tree to the identity.  A new edge
has column equal to its fundamental-cycle incidence vector, so the balanced
basis replacement is a tree exactly when the displayed minor is
nonsingular.  Block-triangular factorization is ordinary determinant
multiplication. `square`

The virtual normalization removes the unequal-size distraction but not the
graphic correlation.  Even when both three-edge C6 phases are matchings,
an exterior forest can make the exchange minor singular.

### Proposition 3.5 (universal finite graphic/root boundary state)

Let `B` be the port set of one packet and `F` the retained exterior forest.
The exact unrooted graphic state seen by the packet is the partition
`Pi_F` of `B` into intersections with components of `F`.  If every retained
component contains at most one selected root, add one root bit to each
partition block.  An attachment graph `H` on the ports is legal exactly
when

1. `H/Pi_F` is loopless and acyclic; and
2. every component of `H/Pi_F` has root-bit sum exactly one.

Components of `F` disjoint from `B` must already contain exactly one root.
For a six-port C6 packet there are `Bell(6)=203` unrooted partition states
and

\[
                         \sum_{j=1}^6 S(6,j)2^j=2430           \tag{3.13}
\]

partition-plus-root-bit states before rejecting illegal root sums.

#### Proof

Contract every component of the forest `F`.  A new edge whose ports lie in
one block becomes a loop, and a family of new edges creates a cycle exactly
when its quotient family does.  Root bits add under quotient component
merger; exact one-root legality is therefore item 2.  Boundary-free
components are unaffected and must be legal in advance.  The state counts
are the Bell number and the Stirling-number sum in (3.13). `square`

For the universal class of arbitrary port-graph attachments, the partition
is necessary, not merely sufficient: if two exterior forests induce
different partitions, choose two ports connected in one and not the other.
Adding their boundary edge is a loop in the first quotient and a nonloop in
the second.  A restricted Boolean socket catalogue may identify two states
when the distinguishing attachment is unavailable.  Moreover, raw resource
privacy does not factor the
graphic row when retained components meet ports of several packets; two
individually safe quotient edges can become parallel and form a cycle.
Component privacy, or the block-triangular fundamental-path condition in
Lemma 3.4, is the proof-safe factorization condition.

### Proposition 3.6 (outer-pairing parity obstruction)

Fix the same lower and upper outer banks and identify every perfect outer
pairing with a permutation.  Relative to its old pairing,

* a full C6 phase toggle acts by a 3-cycle; and
* a sparse `C_(2\ell)` phase toggle acts by an `ell`-cycle.

Therefore a catalogue using only planted/full C6 toggles and odd-`ell`
sparse rerouters preserves the sign of the outer pairing.  In particular,
C6 plus the first sparse `ell=5` (`C10`) catalogue cannot reach a target
pairing of opposite parity.  The authoritative sparse construction first
offers a parity-changing even case at `ell=6`, under its sufficient range
`n>=2ell-2=10`.

#### Proof

The two C6 phases are the two cyclic perfect matchings of three lower and
three upper resources, so their relative permutation is a 3-cycle.  The
sparse switch replaces `D_i--V_i` by `D_(i+1)--V_i`, an `ell`-cycle on the
pairing.  A cycle of length `r` has sign `(-1)^(r-1)`.  Hence the displayed
odd cycles are even permutations, while every even-`ell` cycle is odd.
`square`

This parity is an invariant of the outer **pairing**, not of the endpoint
permutation in Theorem 1.1.  The two states must not be conflated.

## 4. Correlated planting plus endpoint routing

The following theorem discharges the formerly opaque one-reset row under an
explicit socket hypothesis.  It composes with the authoritative correlated
planting theorem but does not prove its positive-density antecedent.

### Theorem 4.1 (endpoint-routed planted-C6 completion)

Fix one common basis `Q`, one normalized side host, and a precompletion
matching `M` of order `P-h`.  Assume:

1. **Coherent outer leave.**  The lower and upper leave of `M` is the outer
   projection of a matching `T_I` of `h` planted-C6 targets.
2. **Installed off states.**  After a declared precompletion rerouter word,
   every two-atom off phase `O_i`, `i in I`, is present and the selected
   on-state supports are cross-compatible.  The word is serializable: at
   each step its old phase is present, its new phase is free, and every
   exposed prefix is a literal host matching.  Required off phases remain
   installed until their C6 activation.
3. **Slot equation.**  The same word satisfies (3.3).
4. **Physical side row.**  Let `M_pre` be the actual terminal
   preactivation matching after the serialized word, and form its virtual
   perfect completion `overline M_pre=M_pre union T_I`.  Choose a legal old
   root set so its labelled physical projection is a rooted spanning tree.
   Let `M_fin` be the actual terminal matching after C6 activation and every
   closed postcompletion socket composite, with its candidate terminal root
   set.  Cancel common labelled physical/root edges between these two
   **net endpoint states** and require the single fundamental-cycle minor
   of Lemma 3.4 to be nonsingular.  The terminal host matching also respects
   ordinary degree two and anchor degree one.  Transient atoms which are
   added and later removed are not counted in this net test; their prefix
   legality remains part of hypotheses 2 and 5.  Separate local socket
   audits do not replace the joint terminal minor.
5. **Endpoint path row.**  Fix the literal decoder `D_I` which performs the
   selected C6 activations.  First form the provisional decoded state obtained
   after the declared **non-endpoint** rerouters and the replacements (4.1).
   Its augmented residual graph has no reset-free directed cycle; write
   `sigma_0` for its endpoint permutation.  This **decoded** state has a
   word-closed socket graph satisfying Theorem 2.1.  The selected correction
   has certified decoded action `tau sigma_0=id` and is realized in one of
   the two proof-safe ways of Corollary 3.2:

   * as precompletion sockets satisfying the decoder-equivariance equation
     (3.6), so that their decoded action is `tau`, and
     whose slot displacements are included in (3.3); or
   * as one zero-slot, resource-balanced postcompletion composite.

   Every physical prefix which is semantically exposed is audited.
6. **Recursive/guard row.**  Every deliberately exported prefix passes the
   two cumulative occurrence-reserve systems.  The terminal outer-pairing
   action agrees with every protected pointwise cap on its declared domain
   (packet avoidance is one sufficient way to ensure this), and the
   downstream compiler state has zero aggregate displacement or an
   independently proved regeneration.

Then, after the declared sequence of precompletion routing, simultaneous
replacements

\[
                      O_i\longrightarrow N_i\qquad(i\in I),    \tag{4.1}
\]

and any declared closed postcompletion correction, the normalized side host
is covered exactly by `P` atoms; its physical
support is a forest with the declared root state; every augmented residual
cycle contains exactly one complementary reset; and the exact side row has
an existential local Boolean common cap.  The resulting oriented endpoint
bank is a valid next recursive state whenever the remaining declared
three-sector rows hold.

#### Proof

Sparse sockets preserve both outer leaves pointwise.  Hypotheses 1 and 3
therefore say that immediately before (4.1) the complete typed leave is
exactly `T_I`.  The installed identities

\[
       \operatorname{inc}(N_i)
        =\operatorname{inc}(O_i)\mathbin{\dot\cup}
          \operatorname{inc}(T_i)                              \tag{4.2}
\]

then show that (4.1) covers every host resource once and raises the matching
order from `P-h` to `P`.

The physical side conclusion is hypothesis 4 and the standard
delete-contract-add graphic criterion.  By hypothesis 5, the literal
endpoint socket word acts on the provisional **decoded** permutation and
sends `sigma_0` to the identity.  Theorem 1.1 therefore proves the one-reset
conclusion; no endpoint-neutrality of an individual C6 activation was
assumed.
Exact outer saturation, literal-slot matching and physical acyclicity give
the local Boolean common cap.  Hypothesis 6 supplies the logically stronger
recursive reserve and word-compiler assertions. `square`

### Corollary 4.2 (closed-socket postcompletion face)

In Theorem 4.1, endpoint correction may instead occur after C6 activation
provided it is one simultaneous resource-balanced composite satisfying
(3.4), its old and new unions are both literal host matchings, and its full
graphic/root/guard audit passes.  A list of isolated sparse cycles with
canceling formal displacement is not enough unless their union is an actual
legal composite.

## 5. Exact obstruction and the remaining theorem

For any proposed record, the following are rigorous scoped no-go
certificates.

1. A reset-free directed physical cycle exists outside the socket supports.
2. Some cycle of `sigma_0` meets two connected components of the word-closed
   socket graph.
3. The target-slot vector minus the current slot leave is outside the
   integer lattice generated by available socket displacements; Smith
   normal form gives the exact torsion rows.  Binary/stateful reachability is
   still stronger than lattice membership.  Even when the separate
   permutation and lattice tests pass, the joint signature can fail, as in
   (3.9c).
4. A postcompletion routing proposal has nonzero total slot displacement.
5. A selected socket word fails a rooted fundamental-cycle determinant,
   owner capacity, occurrence-reserve prefix, or compiler guard.

The second item is exact only for the declared word-closed transposition
atlas; without word-closure, the exact object is the finite state graph whose
vertices record the matching, endpoint permutation, slot leave and guard
state.

### Proposition 5.1 (private-bank alignment density)

Let a resource-disjoint planted target bank of order `T` induce the partial
bijection `pi` between its lower and upper target resources.  For deficiency
`t<=T`, it supports exactly

\[
                              {T\choose t}                       \tag{5.1}
\]

ordered outer-leave pairs, namely `(L,pi(L))`.  If the lower and upper
`t`-subsets are independent and uniform in full banks of order `P`, their
alignment probability is

\[
                          {{T\choose t}\over {P\choose t}^2}.    \tag{5.2}
\]

Conditioned on both shores lying in the target bank, the probability is
`1/binom(T,t)`.  More generally, for any record distribution satisfying

\[
        \max_{L,U}\Pr(U\mid L)\le\gamma                         \tag{5.3}
\]

on the relevant `t`-subset face, the alignment density of this private bank
is at most `gamma`.

#### Proof

Choosing `L subseteq dom(pi)` forces the sole compatible upper set
`pi(L)`, proving (5.1).  Divide by the number `binom(P,t)^2` of independent
ordered leave pairs to obtain (5.2), and by `binom(T,t)^2` after
conditioning.  In the general distribution, sum
`Pr(L)Pr(U=pi(L)|L)` over the eligible `L` and use (5.3). `square`

Thus a linear private bank has ample cardinality but typically negligible
alignment density when `t` grows.  A positive `a_n` requires engineered
cross-shore correlation or an overlapping target graph; raw packet packing
alone cannot provide it.

The remaining positive all-parameter theorem is now concrete:

> Along one recursively chosen endpoint-bank chain, construct a
> positive-density correlated planted-C6 record together with a
> constant-support endpoint-transposition socket atlas whose relevant
> socket components contain the cycles of the record's endpoint
> permutation, whose total slot signature solves (3.3), and whose selected
> `O(P/n)` routing word passes the rooted graphic, cumulative-reserve and
> compiler guards.

The planted-C6 packing and sparse-cycle construction supply the local
ingredients separately.  They do not prove that a sparse cycle acts as the
required endpoint transposition in the actual exterior state, that the
socket atlas is word-closed, or that the final same-cell/maximal-envelope
compiler cap survives.

## 6. Inputs and scope audit

The exact inputs are:

* `MATH_THEOREM_CATALAN_SUSPENDED_TRANSPARENT_HEX_ABSORBER_AND_BLOCKERS_20260731.md`:
  literal planted `2 -> 3` C6 gain;
* `MATH_THEOREM_CATALAN_SPARSE_FIVE_CYCLE_PHYSICAL_SWITCH_20260731.md`:
  zero-outer-boundary sparse rerouters and their exact slot displacement;
* `MATH_THEOREM_H2_CATALAN_CORRELATED_C6_PLANTING_AND_REROUTER_CUT_20260731.md`
  and
  `MATH_THEOREM_H2_CATALAN_CORRELATED_HEX_PLANTING_AND_SPARSE_REROUTER_GATE_20260731.md`:
  exact outer-coherence, planting, slot, graphic and density interfaces;
* `MATH_THEOREM_CATALAN_THREE_SECTOR_FIXED4_ATOMS_AND_COVERDOWN_GATE_20260731.md`:
  one-reset-per-augmented-cycle residual topology; and
* `MATH_THEOREM_H2_CATALAN_ROOTED_SIDE_TREE_AND_COMMON_CAP_SCD_GATE_20260731.md`:
  rooted graphic bases, fundamental-cycle packet tests, and local common-cap
  scope.

No claim is made here that the direct global Joos--Mubayi--Smith theorem
applies.  Its authoritative exponent obstruction is independent of the
conditional endpoint-router theorem above.
