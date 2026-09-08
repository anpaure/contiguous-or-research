# H3: colored-socket rank augmentation is an alternating-surplus packet, not a provider count

Date: 2026-08-01  
Status: exact finite matching theorem and exact guarded bounded-packet
criterion.  Applied here to the decoded `114930` dual fan.  Twelve
zero-265-preserving one-cut children now have a literal different-colour
socket escape, and all 65 compatible unions of two such visible escape moves
remain q1-UNSAT.  None is thereby certified to have positive closed
alternating surplus.  Synergistic two-cut activations invisible in both
single-cut children, visible-arm plus neutral-router packets, and guarded
`C6`/`C8` packets remain outside that finite shell.

## 1. Resource model and protected contraction

Let

\[
                 R=V\mathbin{\dot\cup}{\cal C}
\]

where `V` is the physical-socket set and `C` is the selected lower-colour
set.  A physical seam `e=st` is the three-resource atom

\[
                    \rho(e)=\{s,t,\gamma(e)\}.             \tag{1.1}
\]

Thus a lower-q1-exact socket selection is a matching in this three-uniform
hypergraph.  Occurrence labels may be retained on parallel seam atoms; they
do not alter the resource-disjointness relation.

Fix a matching `M` and a protected submatching `P subset M`.  Protection in
this note is literal: every atom of `P`, and hence every resource it uses,
must survive.  For a matching

\[
 X\subseteq E\setminus M,\qquad
 \rho(X)\cap\rho(P)=\varnothing,                           \tag{1.2}
\]

define its complete incumbent blocker set by

\[
 D_M(X)=\{m\in M:\rho(m)\cap\rho(X)\ne\varnothing\}       \tag{1.3}
\]

and its alternating surplus by

\[
                       \sigma_M(X)=|X|-|D_M(X)|.           \tag{1.4}
\]

Notice that `D_M(X)` is automatically disjoint from `P` under (1.2).

### Theorem 1.1 (protected alternating-surplus identity)

Let `nu_P(H)` be the largest size of a matching in `H` which contains `P`.
For every matching `M` containing `P`,

\[
 \boxed{
 \nu_P(H)=|M|+
 \max_{\substack{X\subseteq E\setminus M\text{ a matching}\\
                  \rho(X)\cap\rho(P)=\varnothing}}
       \bigl(|X|-|D_M(X)|\bigr).}                          \tag{1.5}
\]

In particular, the protected rank rises above `|M|` if and only if there is
a resource-disjoint new family `X` with

\[
                         |X|>|D_M(X)|.                     \tag{1.6}
\]

#### Proof

For every admissible `X`,

\[
                         (M\setminus D_M(X))\cup X         \tag{1.7}
\]

is a matching containing `P`.  Indeed, `X` is internally disjoint, every
old atom meeting it was deleted, and no protected resource is touched.  Its
size is `|M|+sigma_M(X)`, proving the lower bound in (1.5).

Conversely, let `N` be a largest matching containing `P` and put
`X=N\setminus M`.  Then `X` satisfies (1.2), and every member of
`D_M(X)` lies in `M\setminus N`, since `N` cannot contain two atoms sharing
a resource.  Therefore

\[
 \begin{aligned}
 \sigma_M(X)
   &\ge |N\setminus M|-|M\setminus N|\\
   &=|N|-|M|.
 \end{aligned}                                             \tag{1.8}
\]

Together with the first bound this proves equality.  \(\square\)

The theorem is a rank identity, not a claim that three-resource matchings
form a matroid.  The maximization on the right can retain the full
three-dimensional-matching difficulty.

## 2. The exact alternating object can branch

For an admissible `X`, form the bipartite collision multigraph
`A_M(X)`.  Its left vertices are the atoms of `X`, its right vertices are
the atoms of `D_M(X)`, and every shared resource gives an incidence.  Both
sides have degree at most three.

### Corollary 2.1 (connected positive component criterion)

Condition (1.6) holds if and only if some connected alternating collision
component has strictly more new vertices than incumbent vertices.

#### Proof

The difference `|X|-|D_M(X)|` is the sum of the corresponding differences
over the connected components of `A_M(X)`.  A positive sum has a positive
summand.  Conversely, deleting exactly the incumbent vertices of a positive
component and inserting its new vertices is (1.7) for that component.
\(\square\)

This is the correct replacement for an ordinary augmenting path.  A sharp
branching example has three incumbent atoms

\[
                     m_i=\{a_i,b_i,c_i\}\quad(1\le i\le3)
\]

and four pairwise disjoint new atoms

\[
 x_0=\{a_1,a_2,a_3\},\qquad
 x_i=\{b_i,d_i,e_i\}\quad(1\le i\le3).                  \tag{2.1}
\]

All four new atoms together have blocker set
`{m_1,m_2,m_3}` and surplus one.  Every proper subfamily has nonpositive
surplus.  Its collision graph is the branching tree with central vertex
`x_0`, not an alternating path.  Thus a path or ordinary exchange-digraph
criterion is not necessary without an additional functional/two-resource
theorem.

On a genuinely functional face where every minimal positive component is
known a priori to have maximum degree two, Corollary 2.1 reduces to the
usual alternating-path criterion.  That hypothesis is not known for the
Boolean socket atlas and must not be inferred from bounded packet size.

### Corollary 2.2 (closed first shell uses at most four entering seams)

Let `e` be one proposed entering seam and put

\[
                         R_e=D_M(\{e\}).                  \tag{2.2}
\]

Then `|R_e|<=3`.  If `R_e cap P` is empty and there is a matching `C` of
seams outside `M`, disjoint from `e`, such that

\[
                  |C|=|R_e|,
        \qquad D_M(C)\subseteq R_e,                       \tag{2.3}
\]

then `X={e} union C` has alternating surplus one.  Hence it augments `M`
and uses at most four entering seams.

#### Proof

The seam `e` consumes only two socket resources and one colour resource,
and the incumbent is a matching, so at most three incumbent atoms meet it.
Condition (2.3) gives

\[
 D_M(\{e\}\cup C)=R_e,
 \qquad |\{e\}\cup C|=|R_e|+1.
\]

Apply Theorem 1.1.  \(\square\)

This is exact for a completion which never leaves the first blocker shell
of `e`.  Its failure does not exclude a longer alternating cascade.

## 3. Normalize every cut before measuring gain

Suppose the old segmentation has `p` pieces, `p` selected colours, and a
maximum protected matching `M` of size

\[
                          |M|=p-\delta.                    \tag{3.1}
\]

Let a packet make `q` pure refinements.  Assume it has the canonical
transparent lift `M^up` obtained by retaining `M` and inserting the `q` old
factor adjacencies at the new internal socket pairs.  Thus

\[
                         |M^\uparrow|=|M|+q.               \tag{3.2}
\]

Contract the transported protected bank and compute the alternating surplus
in the post-packet hypergraph relative to `M^up`.

### Corollary 3.1 (exact normalized deficiency change)

If `Delta` is the maximum in (1.5) for the post-packet hypergraph relative
to `M^up`, then

\[
 \nu_{P^\uparrow}(H_{\rm packet})=|M|+q+\Delta,
 \qquad
 \delta_{\rm packet}=\delta-\Delta.                       \tag{3.3}
\]

In particular, when the incumbent has deficiency one, a two-cut packet is
a repair exactly when its post-packet matching has surplus one over the
**two-edge canonical lift**.  Counting the two canonical seams as rank gain
would give a false positive: they merely pay for the two new pieces and two
new colours.

#### Proof

The new system has `p+q` colours and capacity `p+q`.  Apply Theorem 1.1 to
`M^up` and subtract its resulting rank from `p+q`.  \(\square\)

The same formula applies to a `C6` or `C8` packet with `q=0`.  A bare
`3`-for-`3` or `4`-for-`4` exchange at the coloured-matching layer has
surplus zero.  Thus the fact that a factor rethread was generated by an
incidence C6 or C8 does not itself imply matching-rank gain.  Such a circuit
may reroute sockets, colours, or topology, but it raises matching rank only
when its rebuilt atlas contains a larger closed component having one more
new atom than deleted atom.

### Corollary 3.2 (two pure cuts plus a closed socket escape)

Suppose `q=2`, both cuts are allowed pure refinements retaining every old
cut, and `e` is a newly legal dual-fan escape seam.  Let

\[
 M^\uparrow=M\mathbin{\dot\cup}\{k_1,k_2\}              \tag{3.4}
\]

be the canonical lift.  If `e` has a first-shell completion (2.3) relative
to `M^up`, then the new protected matching rank is at least

\[
                         \nu_P(H)+3,                     \tag{3.5}
\]

so `delta_3=p-nu_P` decreases by at least one.  Every old relaxed socket
support and rank-ten provider survives, while `k_1,k_2` self-supply the new
socket pairs, lower colours, and factor-upper values.

#### Proof

Pure-refinement monotonicity gives the carrier (3.4) and preserves the old
support rows.  Corollary 2.2 adds one unit beyond its two canonical atoms.
The piece count and carrier rank both rise by two, while the augmenter adds
one further rank unit.  \(\square\)

The two-lock age test determines when two endpoint cuts are necessary to
activate a particular raw seam.  It is a mechanism for this corollary, not a
necessary condition for arbitrary cut relocation or socket-role rethreading.

## 4. Exact bounded-packet criterion with the nonmatching guards retained

Let `Pi` be a fixed bounded packet: two cuts, a `C6`, a `C8`, or a prescribed
union of them.  Let `Omega` be its allowed support.  Start from the normalized
lift `M^up`.  A **guarded exchange pair** is a pair `(D,X)` such that

1. `D subset M^up\P^up` and `X subset E(H_packet)\M^up`;
2. `X` is a matching, avoids every protected resource, and
   `D_M^up(X) subset D`;
3. every changed occurrence lies in `Omega`, so the outside selection is
   literally unchanged;
4. the final selection

   \[
                         N=(M^\uparrow\setminus D)\cup X   \tag{4.1}
   \]

   is one of the packet's allowed modes and passes all imposed residence,
   topology, upper-ticket, and protected-collar predicates.

For a local support task `z`, let `W_z` be its old occurrence set,
`L_Pi(z)` the occurrences invalidated by the packet, and `G_Pi(z)` the new
occurrences.  The exact zero-gate row included in item 4 is

\[
                 (W_z\setminus L_\Pi(z))\cup G_\Pi(z)
                              \ne\varnothing.             \tag{4.1a}
\]

For pure refinement this is automatic at the relaxed socket/rank-ten level.
For a cut relocation or incidence C6/C8 it must be checked on every task
whose occurrence set meets the reconstructed dependency cone.  Rows outside
that cone are literally unchanged.  This is support preservation; selected
upper-ticket coverage is the stronger row (4.3) below.

### Theorem 4.1 (guarded bounded-packet rank augmentation)

The packet has a protected, fully guarded rank augmentation if and only if
it has a guarded exchange pair satisfying

\[
                              |X|>|D|.                     \tag{4.2}
\]

If the normalized incumbent deficiency is one, (4.2) is necessarily
`|X|=|D|+1`, and the resulting selection is a perfect colored-socket
matching.

#### Proof

The forward implication takes `D=M^up\N` and `X=N\M^up` from the asserted
packet output.  The reverse implication is immediate from (4.1), the full
blocker condition in item 2, and the guards in items 3--4.  In deficiency
one, matching capacity bounds the positive difference by one.  A matching
of size `p+q` uses `p+q` distinct colours and `2(p+q)` distinct sockets, so
it is automatically perfect in all three resource classes.  \(\square\)

For the unguarded matching rank one may always take `D=D_M^up(X)`, as in
Theorem 1.1.  This simplification is not valid for the guarded theorem:
topology or a coupled packet mode may deliberately delete an incumbent atom
which does not collide with `X`.  A rank-positive collision component may
also need rank-zero companion circuits to repay tickets or join cycles.

For an additive ticket universe `T`, item 4 has the exact explicit row

\[
 T\subseteq W_{\rm amb}\cup W_{\rm packet}\cup
     \bigcup_{m\in M^\uparrow\setminus D}W(m)\cup
     \bigcup_{x\in X}W(x).                                \tag{4.3}
\]

Equation (4.3) is safe for occurrence-labelled immediate upper tickets.
Arbitrary-width exterior windows, exact cyclic residence, and terminal
compiler witnesses are not automatically edge-additive and must remain in
the full predicate of item 4.

### Corollary 4.2 (concrete three-on/two-off and four-on/three-off gate)

Let a protected C6/C8 rethread have a rank-neutral carrier and pass the
zero-gate row (4.1a).  If its rebuilt atlas contains either

\[
 |X|=3,\quad D_{M^\uparrow}(X)=D,\quad |D|=2,             \tag{4.4}
\]

or

\[
 |X|=4,\quad D_{M^\uparrow}(X)=D,\quad |D|=3,             \tag{4.5}
\]

where `X` is a matching, `D` avoids the protected bank, and the final
replacement passes item 4, then the packet increases protected rank by one.
Conversely, any guarded unit augmenter having respectively three or four
entering atoms and no deliberately deleted nonblocker has exactly the form
(4.4) or (4.5).

Thus the proof-relevant test is the **complete** blocker neighbourhood,
including untouched carrier seams and canonical cut atoms.  Checking only
the three or four factor incidences advertised by the Boolean circuit can
miss collateral blockers.

## 5. The `114930` core starts at a dual-fan escape

Put

\[
 s=L(3669),\qquad t=L(3670),\qquad c_*=114930.            \tag{5.1}
\]

The decoded round02 core has no `st` seam and the colour neighbourhood of
the two independent socket requirements is

\[
                         N_{\cal C}(\{s,t\})=\{c_*\}.      \tag{5.2}
\]

This is a dual fan, not a shortage of `c_*` providers.

### Lemma 5.1 (exact dual-fan breaker)

Let `Y={s,t}` satisfy (5.2).  In any enlarged socket graph in which `s` and
`t` remain required and independent, every rainbow perfect matching uses a
seam of colour different from `c_*` incident with exactly one member of
`Y`.

If independence is not preserved, a direct `st` seam is the other exact
breaker.  If a packet changes which physical socket a central row forces,
that role rethread is a third breaker and must be analysed in the new socket
quotient.

#### Proof

When `s` and `t` are independent, a perfect matching saturates them with two
different seam atoms.  Rainbow exactness gives these two atoms different
colours.  Since every old incident colour is `c_*`, at least one selected
atom is a newly available different-colour escape.  A direct `st` atom can
instead saturate both sockets once, and a role rethread removes the premise
that both old sockets must be saturated.  \(\square\)

### Corollary 5.2 (exact packet criterion for the round02 dual fan)

Assume the protected-contracted incumbent has normalized deficiency one,
the packet keeps `s,t` as independent required sockets, and its outside
selection is frozen.  Then a bounded two-cut/`C6`/`C8` packet repairs the q1
row if and only if it has a guarded exchange pair `(D,X)` with

\[
 |X|=|D|+1                                                   \tag{5.3}
\]

whose closed exchange contains a seam

\[
 e\in X,\qquad |e\cap\{s,t\}|=1,
          \qquad\gamma(e)\ne114930.                       \tag{5.4}
\]

If a direct `st` seam or a role rethread is allowed, add precisely those two
alternatives from Lemma 5.1.

#### Proof

Theorem 4.1 turns (5.3) into a guarded perfect matching, and Lemma 5.1 forces
(5.4).  Conversely, a guarded pair satisfying (5.3)--(5.4) already gives a
perfect matching by Theorem 4.1; (5.4) identifies how that matching defeats
the named dual-fan certificate.  \(\square\)

The word **closed** is load-bearing.  A new different-colour seam at `s` or
`t` can consume an already used colour and one or two already used sockets.
All displaced atoms must lie in `D`, and the replacements must finish with
one net atom.  The escape alone is necessary but not sufficient.

### Proposition 5.3 (a literal dual-fan escape may have zero rank gain)

Take sockets `s,t,x,y,z,w`, colours `c,d,h`, and old atoms

\[
 m_1=(s,x,c),\qquad m_2=(y,w,d),\qquad
 f=(t,z,c),\qquad g=(x,z,h).                             \tag{5.5}
\]

The old matching rank is two and both `s` and `t` have only colour `c` in
their old stars.  Add the different-colour escape

\[
                              e=(s,y,d).                 \tag{5.6}
\]

Then `e,f` are disjoint and destroy the dual fan, every socket and colour
still has positive support, but the new matching rank remains two.  Relative
to `M={m_1,m_2}`, the entering family `X={e,f}` has

\[
                          D_M(X)=M,\qquad \sigma_M(X)=0. \tag{5.7}
\]

Adding two private canonical cut atoms raises the rank by exactly two and
still leaves the normalized defect unchanged.

#### Proof

Among `m_1,f,g`, every pair conflicts, while `m_2` is disjoint from each;
the old rank is therefore two.  After adding `e`, the pairs `e,f` and `e,g`
are feasible, but every third atom conflicts with one of the pair, so the
rank is still two.  The blocker calculation in (5.7) is immediate.  Private
canonical atoms direct-sum with this instance.  \(\square\)

Likewise, the typed alternating cycles

\[
\begin{array}{c|c|c}
 &\text{incumbent atoms}&\text{alternative atoms}\\ \hline
C_6&(r_1,r_6,c_1),(r_2,r_3,c_2),(r_4,r_5,c_3)&
    (r_1,r_2,c_1),(r_3,r_4,c_2),(r_5,r_6,c_3)\\
C_8&(r_1,r_8,c_1),(r_2,r_3,c_2),(r_4,r_5,c_3),(r_6,r_7,c_4)&
    (r_1,r_2,c_1),(r_3,r_4,c_2),(r_5,r_6,c_3),(r_7,r_8,c_4)
\end{array}                                               \tag{5.8}
\]

are respectively three-for-three and four-for-four perfect exchanges.  They
have zero alternating surplus.  These are abstract typed socket systems,
not asserted Boolean incidences; they show sharply why circuit shape alone
cannot be the rank theorem.

## 6. What the frozen radius-one census does and does not imply

The current facts are:

* the verified core contains 30 directed, hence 15 reverse-paired physical,
  seam literals, all of lower colour `114930`;
* the full incumbent directed degree of that colour is `80`, hence 40
  physical providers before the forced-core contraction;
* `16667` one-coordinate substitutions were replayed: each replaces the
  chosen extra cut by another candidate in the same already-split base
  piece; this is not the universe of all one-cut refinements or rethreads;
* `13043` preserve the relaxed lower/socket/common-orientation/rank-ten
  zero-265 support ledger; and
* none of those `13043` has directed `114930` degree greater than `80`.

The last row is a degree statement, not a provider-set statement.  It permits
a new provider to replace an old provider at equal or lower total degree.
The `13043` row does not test exact q1 matching, exact cyclic residence,
topology, deeper upper ranks, or the compiler.

A corrected socket-role scan of the same `13043` children finds exactly 12
with a non-`114930` seam at `s` or `t`, and zero with a direct shared
`114930` seam.  These 12 destroy the displayed dual-fan proof.  Their full
orientation/socket/lower-colour q1 formulas are all UNSAT, with all 12 text
proofs independently DRAT-verified.  Another 13030 clean noncentral
substitutions retain the dual-fan proof verbatim.

The central base-piece recut family is separately exhausted.  Seven of its
nine candidates have one lower-colour zero.  Of the two CNF-emittable banks,
`1834:9924->9923` is the sole zero-265-clean central recut and is exact-q1
UNSAT; `1835:9933->9932` fails relaxed tail, head, and common-orientation
rows, and its emitted q1 formula is also UNSAT.  Thus radius one is genuinely
closed for the fixed
one-split-per-base one-for-one extra-cut replacement face.

The 16,667-row closure and all 12 proof manifests are frozen in
`MATH_THEOREM_L_K17_ROUND02_DUALFAN_COMPLETE_SINGLE_RECUT_NOGO_20260801.md`.
The index-free central-socket and escape replay is
`MATH_AUDIT_THREAD_D_K17_MASK114930_DUALFAN_PHYSICAL_SOCKET_ESCAPE_20260801.md`.

There are 65 compatible unordered pairs of the 12 individually visible
noncentral escape replacements: the sixty-sixth formal pair uses two
different replacements in the same base piece and is not a cut bank.  Every
one of the 65 literal two-replacement q1 formulas is UNSAT, and all 65 text
proofs are independently DRAT-verified.

### Corollary 6.1 (visible-arm pairs do not form the next augmenter)

No q1 repair on the audited visible-pair face is obtained by taking two of
the already exposed socket-escape replacements, even when they address
opposite central sockets and have different colours.

Consequently any next candidate must leave the visible-arm-pair menu.  One
important remaining class, with the two central roles fixed, is a
**joint-only** seam:
for two changes `g,h`,

\[
 e\in E(H_{g,h})\setminus
       \bigl(E(H_g)\cup E(H_h)\cup E(H)\bigr),           \tag{6.1a}
\]

and `e` must be an off-tight different-colour arm or the direct central
seam.  Pure endpoint cuts for which neither child activates `e` are the
two-lock realization of this condition.  Other untested classes include one
visible arm plus an arbitrary neutral blocker-rerouting recut, and a genuine
incidence C6/C8 rethread which changes a forced socket role.  In every case
the final seam or role change must still lie in a protected closed
positive-surplus exchange satisfying Theorem 4.1.

#### Proof

The 65 exact q1 UNSAT verdicts exhaust the compatible unions of the twelve
visible replacements, proving the first claim and rejecting a pair chosen
entirely from that menu.  Equation (6.1a) defines the joint-only fixed-role
activation class; it is not a classification of every two-change packet.
The blocker-surplus and guard requirements are Theorem 4.1.  \(\square\)

This corollary does not enumerate an arbitrary visible arm plus a longer
neutral blocker-rerouting packet; such a packet lies outside the audited
65-pair menu and remains subject to the general surplus theorem.

### Theorem 6.2 (exact fixed-role Hamming-two anchor cover)

Let `C` be the round02 cut bank and let `g,h` be valid one-for-one recuts in
distinct base pieces.  Write `C_g,C_h,C_{gh}` for the two single children and
the joint child, and write `B_i` for the base piece changed by recut `i`.
Anchor the central sockets by their owner occurrences,
not by mutable piece numbers, and keep their two required socket roles fixed.
A joint child which changes either forced role is a separate **role-relocation
exit** and is not an incidence breaker covered by this theorem.  Assume the
standard locality property:

* a recut changes endpoint states and all other non-colour local
  availability guards only inside its own base piece; and
* after forced contraction, a physical central--leaf seam belongs to the
  residual atlas exactly when every non-colour predicate holds (endpoint
  roles/states, Johnson/age, leaf-socket survival and fixed local resource
  guards) and its lower colour is selected by the global cut bank; and
* the compatible one-for-one bank obeys lower-rainbow injectivity, so recut
  `i` removes its unique old colour `o_i`, adds its unique new colour `n_i`,
  and the two-recut palette has the literal update displayed in (6.1c0).

If `C_{gh}` destroys the round02 dual fan, then at least one of the following
holds.  Reading the cases in the displayed priority order makes them
disjoint: first remove central recuts, then single-child escapes, and call
the remaining case cross-activation.

1. `g` or `h` recuts one of the central bases `1834,1835`, so a central state
   or forced role must be rebuilt literally.
2. One single child `C_g` or `C_h` already contains the same local socket
   escape and that occurrence survives in `C_{gh}`.
3. There is a central--leaf seam `e` and an ordering `(i,j)` of `(g,h)` such
   that the complete non-colour availability predicate for `e` is true in
   `C_i`, but

   \[
       \gamma(e)\notin K(C_i),\qquad
       \gamma(e)=n_j\in K(C_{gh})\setminus K(C_i),
       \qquad \operatorname{leaf}(e)\in B_i,
       \qquad e\notin E(H_C)\cup E(H_{C_j}),             \tag{6.1b}
   \]

   where `n_j` is the unique lower colour added by recut `j`.  Thus the other
   recut jointly selects the seam colour, and `e` occurs in the joint atlas
   but in neither one-change atlas.

Here `K(D)` is the selected lower-colour set of bank `D`.  Case 3 is the
exact off-tight jointly activated seam omitted by a single-child incidence
scan under the displayed locality hypothesis.  The factorization below
remains exact if a forced contraction adds a nonlocal availability guard,
but the one-leaf-base identity (6.1c) need not: the exact master must then
retain a separate joint non-colour-availability response before applying the
debt test (6.1d).  Such a guard cannot be silently absorbed into a
geometry-only singleton scan.

More explicitly, for an anchored central socket `y`, let `R_D(y)` be its
arm set satisfying all non-colour availability predicates after forced
contraction, but before the lower-colour guard, and put

\[
             E_D(y)=\{e\in R_D(y):\gamma(e)\in K(D)\}.
\]

Write `o_i,n_i` for the lower colours removed and added by recut `i`.  The
load-bearing factorization and palette identities are

\[
 \mathbf 1_{e\in E_D(y)}=
 \mathbf 1_{e\in R_D(y)}\mathbf 1_{\gamma(e)\in K(D)},
 \qquad
 K(C_{gh})=(K(C)\setminus\{o_g,o_h\})\cup\{n_g,n_h\}
           \subseteq K(C_g)\cup K(C_h).                  \tag{6.1c0}
\]

and, when the leaf of `e` lies in the base changed by `g`,

\[
 e\in R_{C_{gh}}(y)\Longleftrightarrow e\in R_{C_g}(y),
 \qquad
 e\in R_{C_h}(y)\Longleftrightarrow e\in R_C(y),         \tag{6.1c1}
\]

with the symmetric identities after exchanging `g,h`.  Define the
joint-only arms by

\[
 J_{gh}(y)=E_{C_{gh}}(y)\setminus
 \bigl(E_C(y)\cup E_{C_g}(y)\cup E_{C_h}(y)\bigr).
\]

When neither recut is central, fixed-role locality gives the exact identity

\[
 J_{gh}(y)=
 \mathop{\dot\bigcup}_{(i,j)\in\{(g,h),(h,g)\}}
 \left\{e\in R_{C_i}(y):
 \begin{array}{l}
   \operatorname{leaf}(e)\in B_i,\\
   \gamma(e)=n_j\in K(C_{gh})\setminus K(C_i),\\
   e\notin E_C(y)\cup E_{C_j}(y)
 \end{array}\right\}.                                    \tag{6.1c}
\]

Moreover every new final arm decomposes as

\[
\begin{aligned}
E_{C_{gh}}(y)\setminus E_C(y)={}&
 \bigl(E_{C_g}(y)\setminus E_C(y)\bigr)\cap E_{C_{gh}}(y)\\
&\cup
 \bigl(E_{C_h}(y)\setminus E_C(y)\bigr)\cap E_{C_{gh}}(y)
 \cup J_{gh}(y).                                         \tag{6.1c2}
\end{aligned}
\]

The first two terms are the unary channel, including an individually dirty
child whose arm survives in the joint bank.  The last term is the genuinely
two-resource channel: recut `i` is the
**geometry mover**, recut `j` is the **colour supplier**, and the pair is
admissible only if their signed changes to every guarded local support row
cancel all debt:

For a common occurrence/activity row universe let `z_r(D)` be the provider
count, `a_r(D)` the active demand, and

\[
                         w_r(D)=z_r(D)-a_r(D).
\]

The universe includes new fragment, socket, colour and common-orientation
demands, not merely the old 265 row names; an inactive demand has
`a_r(D)=0`.  Define

\[
\begin{aligned}
 \Delta_r(g)&=w_r(C_g)-w_r(C),\\
 \Delta_r(h)&=w_r(C_h)-w_r(C),\\
 \Delta_r^{\rm int}(g,h)
   &=w_r(C_{gh})-w_r(C_g)-w_r(C_h)+w_r(C).
\end{aligned}
\]

Then the exact local-debt condition is

\[
 w_r(C_{gh})=w_r(C)+\Delta_r(g)+\Delta_r(h)+
              \Delta_r^{\rm int}(g,h)\ge0
 \quad\hbox{for every row active in }C_{gh}.              \tag{6.1d}
\]

The interaction term records cross-created or destroyed witnesses and
changes of row activity, including the cross-activated seam in (6.1c).
Individual cleanliness is neither sufficient nor necessary for (6.1d): a
second recut may destroy the first child's witness or activate a new demand,
and conversely it may cancel the first child's local debt.  Individual
cleanliness becomes sufficient only with the additional survival condition
that every witnessing occurrence survives the other recut and every final
active demand was checked.  Equations (6.1c)--(6.1d), followed by the full
q1 test, are the correct Hamming-two anchor condition.  They are deliberately
fixed-role statements; a central-state change or forced-role relocation is
a separate channel.  This nonmonotonicity is the exact two-cut guard loss
proved in
`MATH_AUDIT_L_K17_TWO_CUT_SUPPORT_CENSUS_AND_GUARDED_SELECTION_GATE_20260801.md`:
a unary witness assumes its old neighbour remains intact, seam colour has an
activity guard, and the second cut changes the active demand set.

#### Proof

If a recut meets a central base, this is case 1.  Otherwise the two anchored
central endpoint states, their ages, and the direct central seam predicate
are unchanged.  Any new joint escape is therefore a central--leaf seam.

If its leaf endpoint state is unchanged from `C`, only its selected-colour
status can be new; whichever recut selects that colour already creates the
same seam in its single child, giving case 2.  Otherwise the changed leaf
lies in exactly one of the two recut bases, say the base of `i`.  Raw
Johnson adjacency and residence then depend only on the unchanged central
state and the `i`-child leaf state.  If its colour is selected in `C_i`, the
seam is already a single-child escape, again case 2.  If not, joint
existence forces the other recut `j` to select that colour, which is exactly
(6.1b); uniqueness of factor-gap colours identifies it with `n_j`.  If the
seam were already present in `C_j`, case 2 would hold, so the remaining case
also has the final condition in (6.1b).  These cases exhaust a seam incident
with an anchored central socket.

For the sharpened identity, let `e` lie in `J_gh(y)`.  Its raw state must
change in exactly one noncentral base, say `B_i`; otherwise its final colour
supplier would already expose it in a single child.  Locality gives (6.1c1),
and the palette law forces `gamma(e)=n_j` for the other recut.  Absence from
both single atlases gives the last line of (6.1c).  Conversely every arm on
the right side of (6.1c) is raw in the joint child, has a selected joint
colour, and is absent from the base and both single children, so it lies in
`J_gh(y)`.  The union is disjoint because the two leaf bases are distinct.
Equation (6.1c2) then partitions new final arms into those inherited from at
least one single child and `J_gh(y)`.  Finally (6.1d) is the inclusion--
exclusion identity for the literal slack functions, and its inequalities are
exactly the final local-row guards.  \(\square\)

### Corollary 6.3 (the 21-anchor reduction is conditional)

Let `A_21` consist of the nine central-base recuts and the twelve
zero-265-clean visible noncentral escape recuts.  A Hamming-two dual-fan
incidence breaker is forced to meet `A_21` only under all three additional
hypotheses:

1. the two central forced roles remain fixed;
2. the palette--geometry cross-activation (6.1b) is absent; and
3. every noncentral single-child escape which participates in a jointly
   zero-265 pair is itself zero-265-clean, so no local debt of that child is
   cancelled only by the other recut.

Indeed, Theorem 6.2 then leaves either a central recut, which is one of the
nine, or a clean unary escape, which the complete radius-one census places
among the twelve.  This proves the conditional 21-anchor reduction.

A convenient stronger sufficient hypothesis is that both single children
are zero-265-clean.  In that case the central alternative sharpens to the
sole clean central recut `1834:9924->9923`, and the anchor set has only
thirteen members: that recut plus the twelve visible escapes.  The central
recut `1835:9933->9932` is exact-q1 UNSAT but is not in this clean
thirteen-anchor conclusion: it fails relaxed tail, head, and
common-orientation rows.

Without item 3, a recut can expose an escape while failing a local row which
the other recut later repairs; it is then absent from the twelve-row clean
list.  Without item 2, one recut can expose a raw central--leaf seam and the
other can select its lower colour.  Therefore both the proposed twelve-row
and 21-anchor reductions are not logically valid without their displayed
qualifications; no successful round02 pair is asserted here.
An unfiltered post-contraction non-colour availability atlas, the
cross-colour incidence relation, and the joint local-debt ledger (6.1d) form
the exact Hamming-two search object.

Even in the clean thirteen-anchor regime, the 65 visible--visible pair
audit does not exhaust the conclusion: the second recut may be a neutral
router rather than another visible escape.  Such mixed pairs still require
literal joint zero-265 and full-q1 replay.

The same proof shows that a noncentral recut pair cannot create the direct
`s--t` seam: both of its endpoint age states and its already selected colour
`114930` remain fixed.  Direct-seam activation at Hamming two must therefore
use a central recut or leave the one-for-one recut model.

### Corollary 6.4 (the frozen face discharges the conditional anchor rows)

Thread D's complete unfiltered projection finds 67 noncentral geometry
movers and 154 new raw unselected seam occurrences, no dirty noncentral
selected escape, and no compatible nonanchor geometry--colour supplier
pair.  Therefore the abstract qualifications of Corollary 6.3 are verified
on the frozen face: every old-fan-breaking Hamming-two bank contains one of
the 21 anchors.

The exact product has 349,642 compatible banks and 169,426 passing the joint
local ledger.  The role-changing `1835:9933->9932` move has no jointly clean
partner.  The seven dirty base-1834 anchors have seven compensating partners
each; all 49 resulting exact-q1 formulas are UNSAT.  Hence dirty-single
compensation is closed and the remaining

\[
                         169426-49=169377                 \tag{6.1e}
\]

banks all contain one of the thirteen individually clean anchors.

For a clean anchor `a` and authenticated occurrence-labelled core `K`, let
`Dist_K(a,h)` record any final change of a core occurrence/role, literal
clause, effective positive-row provider set, resource capacity, named
dead-atom blocker, geometry--palette cross atom, or two-endpoint cross atom.
If `Dist_K(a,h)` is false, the core embeds clause-for-clause (or as its
guarded minor) and the final bank is q1-UNSAT.  Therefore a bank needs a
fresh q1 formula only if it disturbs every stored core of every clean anchor
it contains.  This persistence filter has no false rejection and is
complete relative to the stored core library, not for all q1 infeasibility.

Thus Hamming two remains the minimal live radius.  No Hamming-three or
C6/C8 lower bound follows until all 169,377 remaining banks are rejected.

The provider-only census by itself proved neither a support-two lower bound
nor C6/C8 necessity: the 12 escapes show why.  The later exact-q1 replay is
the load-bearing closure.  It proves Hamming distance at least two only
inside the displayed fixed replacement face.  One added pure-refinement
cut, a cut deletion plus compensation elsewhere, other base-cut changes,
and incidence C6/C8 or other rethreads are outside that face and remain live.

Nor does q1-UNSAT alone say that every child has zero *rank gain* relative
to the incumbent when the incumbent matching deficiency may exceed one.  If
a separate maximum-matching certificate gives normalized deficiency one,
then the radius-one q1 no-go excludes every surplus-one completion on this
face.  Without that certificate it excludes perfection, while a child could
in principle gain one rank unit and expose another defect.

For a prospective two-cut or circuit packet, the exact proof target is now
finite and invariant:

\[
 \boxed{\text{find a protected closed exchange of normalized surplus one
 containing a joint-only dual-fan breaker or role relocation and all guards.}}
                                                               \tag{6.2}
\]

Failure of all individual breakers is a support obstruction.  Existence of
a breaker but q1-UNSAT is a coloured-socket closure obstruction.
Failure only of item 4 in the guarded definition is a residence, topology,
upper-ticket, or compiler obstruction and must be named as such.

## 7. Sharp scope

The alternating-surplus identity is unconditional and valid for arbitrary
finite hypergraph matchings.  Its application here still assumes a literal
post-packet candidate atlas and a transparent baseline lift.  It does not
show that the Boolean/Johnson atlas has bounded alternating diameter, that a
positive component fits in `C6` or `C8`, or that protected contraction
preserves enough candidates.

The decoded dual fan proves that protected perfect rank is impossible on
that constrained face; it does not by itself prove that the maximum rank is
exactly one below perfect.  The deficiency-one premise in Corollary 5.2
therefore requires its own maximum-matching certificate.  If the deficiency
is larger, (1.5) remains exact, but one surplus-one packet only removes one
unit of it.

Finally, literal contraction applies only when the protected bank is a
fixed disjoint seam submatching.  Protected owner positions, forbidden cut
gaps, residence collars, or occurrence tickets which are not themselves
fixed seam atoms belong in the guarded predicate of Theorem 4.1; treating
them as contracted matching resources would be an additional, presently
unproved modelling step.

Likewise, physical socket perfection gives a union of alternating cycles,
not one Hamilton cycle.  Exact residence beyond the local seam predicate,
all-width exterior OR witnesses, seven-component joining, and the terminal
compiler remain separate guards.  No lower/compiler gate is claimed closed
here.

## 8. Hereditary bounded regeneration

Let

\[
                         \delta_3(H)=p-\nu_P(H)           \tag{8.1}
\]

after contracting only the fixed protected seam submatching.  Call a packet
`kappa`-closed when its complete changed owner, cut, incidence, support-row,
collar, ticket, and guarded-exchange footprint has size at most `kappa`.

### Theorem 8.1 (bounded alternating-surplus descent)

Assume hereditarily that every reachable state with `delta_3>0` has a
`kappa`-closed two-cut/C6/C8 packet which has a normalized carrier and a
guarded exchange pair of surplus at least one.  Assume each packet adds at
most two cuts.  Then a protected coloured socket perfect matching is reached
after at most

\[
                         \delta_3(H)                     \tag{8.2}
\]

packets, at most `2 delta_3(H)` additional cuts, and total charged protected
support at most

\[
                         \kappa\delta_3(H).              \tag{8.3}
\]

#### Proof

If a packet adds `q` pieces, its normalized carrier has old rank plus `q`.
The positive alternating surplus adds at least one more rank unit.  Hence the
piece count and matching rank satisfy

\[
                p' = p+q,\qquad
                \nu_P(H')\ge\nu_P(H)+q+1,
\]

so `delta_3` falls by at least one.  Repeat until the nonnegative integer
vanishes.  The cut and support bounds add over the same packet sequence.
\(\square\)

This is the concrete bounded regenerative theorem.  Its hereditary premise
is precisely the live Boolean expansion statement: every positive-defect
Johnson socket atlas must expose a guarded positive-surplus component of
bounded physical support.  On the fixed round02 replacement face, all 12
local escapes and the sole zero-265-clean central recut are exact-q1 UNSAT;
the other eight central recuts fail a local zero row.  Thus no radius-one
packet reaches perfection there.  If the incumbent defect
is separately certified to be one, this also excludes radius-one positive
surplus.  Added pure cuts, two-replacement packets, and circuit rethreads
remain outside the finite closure.  Among the first two-replacement targets,
all 65 compatible pairs of individually visible escape arms are also
exact-q1 UNSAT.  This rejects only a pair selected entirely from the visible
arm menu.  A jointly activated off-tight seam invisible in both one-change
children, a visible arm plus a neutral global rerouter, or a true C6/C8
forced-role relocation remains live.
