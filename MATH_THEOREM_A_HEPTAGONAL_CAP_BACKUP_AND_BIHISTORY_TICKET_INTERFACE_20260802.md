# Heptagonal cap backups and exact bi-history tickets

**Date:** 2026-08-02  
**Lane:** A, integration of the rooted `C14` circulation with the protected
Pascal/pull-ear recurrence  
**Status:** exact fixed-depth interface and exact conditional composition
theorem.  This note does not prove completed-ticket abundance, a Pascal host,
or an all-`k` construction.

## 0. Result and scope

The rooted heptagonal theorem has removed raw central packet supply as the
principal local gate.  A rooted anchor has `Theta(k^7)` prospective `C14`
circuits, and every nonanchor central token has load `O(k^6)`.  That statement
does **not** yet count the objects which a protected recurrence must choose.

The proof-safe choice is a **completed ticket** consisting of

1. the literal rooted heptagon and its protected support;
2. its cap-change vector, together with either an exact cap return or a
   declared duplicate-cap backup bank;
3. the directed boundary bi-history sockets of its seven retained ears;
4. the entrance domains and output histories of any reset ears;
5. the component permutation and quotient voltage; and
6. every exterior socket which the recurrence requires to be returned.

These data form a closed fixed-depth semigroupoid.  In particular, a
coprime-voltage developed packet needs no additional phase coordinate in its
history state.  Its cap row is different: naive sequential cap transport is
holonomy-obstructed, so it needs a nontrivial cap permutation, active cap
return, or passive duplicate witnesses.

The exact next supply theorem is therefore **joint** completed-ticket
abundance: balanced cap returns/backups and compatible boundary-history
tickets must occur in the same rooted atlas.  The existing `Theta(k^7)` count
and `O(k^6)` load estimate concern only the central projection and do not
prove this joint statement.

## 1. The complete local state of a heptagon

Let `Gamma=<rho>` act on the coordinates.  Let `Z` be a quotient heptagonal
switch with seven old cap occurrences `U_i`, seven new cap occurrences `V_i`,
phase increments `alpha_i`, and voltage

\[
                         h(Z)=\sum_{i=0}^6\alpha_i.       \tag{1.1}
\]

Let `P_i:x_i\leadsto y_(i+1)` be the seven retained oriented ears exposed by
deleting the old rows.  The old factor reads the ears in step-one order; the
new factor reads them in step-two order

\[
                         0,2,4,6,1,3,5.                 \tag{1.2}
\]

For every literal physical cap target `U`, define

\[
 \Delta_Z(U)=\#\{i:V_i=U\}-\#\{i:U_i=U\}.              \tag{1.3}
\]

When the cap orbits involved are free, the same information can be recorded
orbitwise.  In the presence of shortened cap orbits, (1.3) is to be read in
the full physical development; unweighted quotient counts are not a valid
replacement.

Fix residence depth `d`.  Attach to each oriented retained ear its exact
two-sided history signature

\[
       \Sigma_d(P_i)=(M_{P_i},M_{\overleftarrow {P_i}}),           \tag{1.4}
\]

including the whole-component token when topology can create a component of
length at most `d`.  The complete local state is

\[
 \mathfrak T_d(Z)=
 \bigl(
   \operatorname{supp}(Z),\Delta_Z,h(Z),\sigma_Z,
   (\Sigma_d(P_i))_{i=0}^6,\mathcal E_Z
 \bigr),                                                        \tag{1.5}
\]

where `sigma_Z:i\mapsto i+2` is the component-port permutation and
`mathcal E_Z` is the declared protected/exterior socket ledger.  Any reset
ear occurring in a `P_i` is stored with its entrance domain, not only its
constant output.

The coordinates in (1.5) are logically independent.  In particular,
`Delta_Z=0` does not imply history compatibility, and an accepting history
relation does not imply cap closure.

## 2. Exact boundary-ticket criterion

The following is the collar form of the history semigroupoid specialized to
the seven-path rethread.  It is often much smaller than a full `q^d` table.

Assume every `P_i` has at least `d` transitions and is internally positive
depth-`d` resident.  In the canonical frame at its right endpoint let

\[
 I^+(P_i)=(p_{i,1},\ldots,p_{i,d})                       \tag{2.1}
\]

be its last `d` insertions, newest first.  In the canonical frame at the left
endpoint of `P_j`, let

\[
 D^+(P_j)=(a_{j,1},\ldots,a_{j,d})                       \tag{2.2}
\]

be its first `d` deletions.  Before comparing labels, transport them into the
same endpoint frame.

Let the new connector from `P_i` to `P_j`, where `j=i+2 mod 7`, delete `a`
and insert `b`.  Define `G_d^+(P_i,e,P_j)` to be the conjunction

\[
\begin{aligned}
 a&\ne p_{i,s} &&(1\le s\le d),\\
 b&\ne a_{j,t} &&(1\le t\le d),\\
 p_{i,s}&\ne a_{j,t} &&(s+t\le d).
\end{aligned}                                                \tag{2.3}
\]

Define `G_d^-` by applying the same formula to the deletion-history dual,
equivalently by interchanging present/absent events and using the literal
dual collars.  Put

\[
                  G_d=G_d^+\wedge G_d^-.                \tag{2.4}
\]

### Theorem 2.1 (seven-ear bi-history ticket)

Under the hypotheses above, the rethreaded heptagon is internally positive
and negative depth-`d` resident if and only if

\[
          G_d(P_i,e_i,P_{i+2})\quad\hbox{holds for every }i.      \tag{2.5}
\]

If a declared exterior collar is opened rather than closed, (2.5) remains
the exact internal test and the two exposed endpoint collars are the exported
bi-history ticket.

#### Proof

The old and new factors use every retained ear, with the same orientation,
exactly once.  Hence every run wholly internal to an ear is unchanged.  The
only new runs cross one of the seven new connectors.  Formula (2.3) is the
literal insertion-to-next-deletion criterion for such a seam: the connector
deletion is checked against the predecessor tail, its insertion against the
successor head, and the old tail labels against the old head labels at their
new separation.  The dual formula does the same for negative runs.  These
seven seam neighborhoods are disjoint as logical transition positions, so
their conjunction is necessary and sufficient.  The exposed-collar claim is
the ordinary path-composition rule.  \(\square\)

For ears shorter than `d`, or for a pull which reverses a retained ear,
Theorem 2.1 must be replaced by the full signatures (1.4).  A reversed ear
uses `M_(reverse P)`, not the forward tail/head collars with their order
silently exchanged.

## 3. Coprime voltage does not add a history phase

Suppose the rank-owner action is free.  Let `M_Z` be the min-plus product of
the seven retained-ear and new-connector morphisms in the order (1.2).

### Theorem 3.1 (developed history closure)

The developed packet has a consistent cyclic depth-`d` history exactly when

\[
                         M_Z(\Omega,\Omega)<\infty        \tag{3.1}
\]

for some canonical-frame bi-history socket `Omega`; its exact event cost is
the minimum diagonal value, with the developed whole-component correction
added separately.  This statement is unchanged when `h(Z)` is coprime to the
group order.

After one quotient lap the physical owner and every absolute history label
are shifted by `rho^(h(Z))`.  Re-expression in the new canonical frame
cancels that common shift.  Thus coprime voltage changes the number and
length of developed components, but creates no independent history phase.

The cap row is not analogous.  Under sequential retained-label transport a
cap label would have to satisfy `z=rho^(h(Z))z`; for a free coordinate action
this is impossible when `h(Z)` is nonzero.  Hence (3.1) can hold while the
naive cap rotor fails.

#### Proof

The history statement is the equivariant directed-history fixed-point
theorem applied to the product around the quotient component.  The cap
obstruction is the product of the seven sequential transport identities.
\(\square\)

For the authenticated `k=17` terminal heptagon, `h=5 mod 17`.  Its history
and residence replay is accepting, but three removed cap orbits are retained
only because their old load is two.  This is a finite witness for the backup
alternative, not a uniform backup-planting theorem.

## 4. Cap returns and passive backups are different interfaces

Let an ambient host have physical cap multiplicity `L(U)`.  For a set `S`
of simultaneously applied, support-compatible packets, literal cap support
after the packets is complete if and only if

\[
                     L(U)+\sum_{Z\in S}\Delta_Z(U)\ge1
                 \quad\hbox{for every }U.               \tag{4.1}
\]

The cap **multiset** is returned exactly if and only if

\[
                         \sum_{Z\in S}\Delta_Z(U)=0
                 \quad\hbox{for every }U.               \tag{4.2}
\]

Equation (4.1) is the exact duplicate-backup inequality.  Equation (4.2) is
the exact cap-circulation equation.  Passive duplicate witnesses can prove
(4.1); they cannot prove (4.2).

It is useful to reverse the sign and write the cap deficit

\[
              \partial Z(U)=-\Delta_Z(U)
                =\#\{i:U_i=U\}-\#\{i:V_i=U\},          \tag{4.3}
\]

and the incumbent spare capacity `s(U)=L(U)-1`.  Then (4.1) is exactly

\[
                         \sum_{Z\in S}\partial Z(U)\le s(U)
                    \quad\hbox{for every }U.             \tag{4.4}
\]

For one heptagon, form the directed cap-transfer multigraph with its seven
arcs `U_i->V_i`.  Decompose it into directed cycles and maximal open paths.
The cycles require no backup.  The source of every open path contributes one
positive unit to `partial Z`, and its sink contributes one negative unit.
Consequently the minimum number of duplicate units needed by the packet is

\[
            b(Z)=\sum_U(\partial Z(U))_+
                ={1\over2}\lVert\partial Z\rVert_1.      \tag{4.5}
\]

The equality uses `sum_U partial Z(U)=0`, which holds because a heptagon
deletes and adds seven cap occurrences.  The authenticated `k=17` packet of
voltage five has four transported cap rows and three open paths, hence
`b(Z)=3`; its three source caps `13783,27447,28075` have incumbent load two.
The three added caps are `13727,28331,43755`.  Thus this packet is
support-exact, not cap-multiset-exact.

If backups are frozen occurrence-labelled witnesses, let `B(U)` be the
candidate old occurrences of `U` which are outside the protected bank.  A
declared backup choice `b(U) in B(U)` is valid for packet set `S` precisely
when

\[
                    b(U)\notin\bigcup_{Z\in S}\operatorname{supp}^-(Z)
                                                                  \tag{4.6}
\]

for every endangered `U`, and (4.1) holds.  Thus backup selection and packet
selection are correlated even though cap multiplicity itself is a scalar
row.  If an active return module can serve several possible cap debts, its
occurrence-labelled assignment is an ordinary capacitated bipartite
matching.  More generally, if each required backup clone has a menu of
physical sockets and the sockets have capacities, a simultaneous assignment
exists exactly when the clone-to-socket graph satisfies capacitated Hall.
No Hall condition should be asserted for passive copies when the exact
problem is already the coordinatewise inequality (4.1) and their physical
occurrences have been fixed.

### Lemma 4.1 (cap-state composition)

On a disjoint-support or literal symmetric-difference ledger, cap-change
vectors add.  Equivalently, export the cap-surplus vector

\[
                              s=L-\mathbf 1.             \tag{4.7}
\]

The exact recurrence is

\[
                  (s,\Delta)\longmapsto s+\Delta,        \tag{4.8}
\]

with support acceptance `s+Delta>=0` coordinatewise.  This is a closed state
coordinate for pull-ear composition.  A protected Pascal recurrence may
accept either this support face or the stronger return face (4.2), but it
must declare which one it uses; consuming a duplicate now must be visible as
one unit less surplus in the exported child state.

For an ordered accepting chain `Z_1,...,Z_t`, put

\[
                 s_j=s_0+\sum_{i=1}^j\Delta_{Z_i}.       \tag{4.9}
\]

If upper completeness is protected at every intermediate step, the exact
condition is `s_j>=0` for every prefix `j`.  If temporary cap holes are an
explicitly allowed debt, only the declared terminal inequality is imposed.
Exact multiset regeneration is `s_t=s_0`.  Active cap-creation modules are
included through their own `Delta`; a passive backup is already counted in
`s_0` and must not be credited a second time.

#### Proof

Every changed row deletes one literal old cap occurrence and adds one literal
new occurrence.  Counting those signed occurrences gives (4.8).  The two
acceptance faces are exactly their definitions.  \(\square\)

## 5. Reset ears: output reset is not entrance compatibility

Consider a length-`d` reset ear whose deletion bank in its entrance frame is

\[
                         A=(A_1,\ldots,A_d)              \tag{5.1}
\]

and whose insertion bank is disjoint from `A`.  Its output history is the
fixed newest-first insertion tuple `H_out`.  Its exact positive entrance
domain is

\[
 \mathcal G_A=
 \{(h_1,\ldots,h_d):
       A_t\notin\{h_1,\ldots,h_{d-t+1}\}
       \text{ for }1\le t\le d\}.                       \tag{5.2}
\]

Suppose a connector `e` immediately precedes the reset.  In the reset frame
write

\[
                 U_e(H)=(b,\varphi h_1,\ldots,
                                  \varphi h_{d-1}).       \tag{5.3}
\]

### Theorem 5.1 (exact connector-to-reset ticket)

The connector followed by the reset is positive depth-`d` legal on incoming
history `H` if and only if

\[
\begin{aligned}
 a_e&\notin\{h_1,\ldots,h_d\},\\
 A_t&\ne b &&(1\le t\le d),\\
 A_t&\ne\varphi h_j &&(1\le j\le d-t).
\end{aligned}                                                \tag{5.4}
\]

Whenever (5.4) holds, the outgoing history is `H_out`, independent of `H`.
The negative/reverse ticket is obtained from the literal reverse reset and
has its own triangular domain.  Consequently a proof-safe orientation-free
reset ticket is

\[
  (\mathcal G_A,H_{out};
     \mathcal G_{A^{rev}},H_{out}^{rev}),                \tag{5.5}
\]

not merely `H_out`.

#### Proof

The first row of (5.4) is the connector's own deletion guard.  Substituting
(5.3) into (5.2), the newest entry `b` is tested by every reset deletion,
and the transported entry `varphi h_j` remains visible through reset step
`t` exactly when `j<=d-t`.  This gives the other two rows.  After `d` reset
transitions every incoming entry has shifted out.  Apply the same argument
to the reversed literal transition word.  \(\square\)

The stronger disjointness condition

\[
              \{A_1,\ldots,A_d\}\cap
              (\{b\}\cup\{\varphi h_1,\ldots,
                                      \varphi h_{d-1}\})=\varnothing
                                                                  \tag{5.6}
\]

is sufficient but not necessary.  Counting only reset outputs discards the
load-bearing entrance constraints in (5.4).

## 6. Closed completed-ticket composition theorem

Let a protected Pascal/pull-ear construction expose finitely many ports.
At each port retain the state

\[
 \mathfrak S_d=
 \bigl(
   \text{factor/port roles},\ s,\ h,\ \sigma,
   \mathcal R_d^+,\mathcal R_d^-,
   \text{whole-component tokens},
   \text{protected/exterior ledger}
 \bigr).                                                       \tag{6.1}
\]

Here `s=L-1` is the literal cap-surplus vector on the targets controlled by
the packet, `h` is quotient voltage, `sigma` is the component-port permutation,
and the two relations include all reset domains and outputs.

### Theorem 6.1 (fixed-depth heptagon/Pascal closure)

Suppose a finite family of rooted heptagons, pull ears, active cap returns,
and passive backup occurrences satisfies all of the following.

1. Its final symmetric difference is a legal owner/facet factor and avoids
   the protected bank.
2. Component permutations compose to the declared output topology and the
   sum of voltages has the declared lift gcd.
3. The literal cap vector satisfies (4.1), or (4.2) when exact multiset
   return is required; every declared passive backup satisfies the untouched
   occurrence condition (4.6).
4. Ear relations and connector morphisms compose to fixed cyclic
   bi-histories on every closed output component and to the declared
   relations on every open port.  Every reset entrance satisfies (5.4).
5. Full history cost includes the developed whole-component correction, and
   every declared exterior socket is returned or transported by an explicit
   relation.

Then the family transports the state (6.1) exactly.  Conversely, on a fixed
literal fragment table, each of rows 1--5 is necessary for the corresponding
factor, topology/voltage, cap, residence, or exterior claim.

If all ears lie in one common compatible-history graph `G_h`, their event
costs are linear and the prepared two-pull/MST theorem applies after adding
the cap vector and component-token weights.  Without a common history, the
correct recurrence is a relation-labelled gluing-tree dynamic program; a
scalar pull weight is not defined before the boundary ticket is chosen.

#### Proof

Factor symmetric difference, port permutations, and voltages give rows 1
and 2.  Lemma 4.1 gives row 3.  The min-plus ear semigroupoid, Theorem 2.1,
and Theorem 5.1 give rows 4 and 5.  These coordinates share occurrence
resources but their semantic updates are direct products, proving closure.
Necessity follows by reading the corresponding literal ledger from any
claimed output.  The common-`G_h` statement is the fixed-history circuit
lemma; otherwise connector costs depend on their input histories and must be
composed relationally.  \(\square\)

Deeper upper shadows, source/erosion, and the common compiler are not encoded
in (6.1).  They may be appended as additional returned relations, but do not
follow from this theorem.

### Corollary 6.2 (exact completed-ticket circulation)

Expand every prospective rooted packet into one arc for each literal choice
of

\[
  (\text{input bi-history},\text{output bi-history},
    \text{backup/return sockets})                       \tag{6.2}
\]

which passes Theorem 2.1 and Theorem 5.1.  Label the arc by its cap deficit,
protected resources, port permutation, voltage, and whole-component cost.
For a fixed finite catalogue, a regenerative closed selection is equivalent
to a zero-one circulation satisfying

\[
\begin{aligned}
 &\sum_{a\in\mathcal A_t}x_a=1
       &&\text{for every required private task }t,\\
 &\sum_{a:\operatorname{head}(a)=\omega}x_a
      =\sum_{a:\operatorname{tail}(a)=\omega}x_a
       &&\text{for every internal bi-history state }\omega,\\
 &\sum_a x_a\,\partial a(U)\le s(U)
       &&\text{for every cap target }U,                 \tag{6.3}\\
 &\sum_{a\ni q}x_a\le\operatorname{cap}(q)
       &&\text{for every occurrence-labelled resource }q,
\end{aligned}
\]

together with the declared final topology and voltage rows.  Replace the
third line by equality zero when exact cap-multiset return is required.
Open recursive ports replace flow conservation at their two boundary states
by the corresponding unit source/sink imbalance.  When one composed root
cycle or path is required, the selected history arcs must additionally have
the corresponding connected/root-reachable support; mere balance can encode
several closed history components.

This is an exact finite formulation, not an integrality theorem: the task,
cap, resource, topology, and connectedness rows can destroy ordinary
network-flow integrality.  Its LP dual supplies a valid obstruction only to
the relaxation; an integral no-go may need an odd-set or general integer
certificate.  The formulation nevertheless isolates the joint obstruction:
separate central-packet counts cannot rule out history, cap/resource,
topology/voltage, or integer-correlation failure.

#### Proof

Choosing a literal pair in each relation turns relational composition into
head-to-tail equality.  Flow conservation closes the internal history
sockets, and the added support condition chooses the declared composition
components.  The first row chooses the required packet tasks, the third is
(4.4), and the fourth is literal occurrence capacity.  Theorem 6.1 proves
sufficiency after topology and voltage are imposed; reading any completed
construction gives all the displayed rows, proving necessity.  \(\square\)

## 7. The exact abundance target and two minimal obstructions

For each private defect anchor `t` and accepted incoming port state `omega`,
let

\[
 \mathcal A(t,\omega)=
 \{\text{rooted heptagons completed by cap and bi-history tickets}}.
                                                                  \tag{7.1}
\]

The central theorem proves only the size and token loads of the projection
which forgets `omega`, backups, and reset guards.  A sufficient fixed-`H`
planting theorem would be:

\[
 |\mathcal A(t,\omega)|\ge c k^7,
 \quad |\operatorname{supp}_{nonanchor}(A)|\le C_0d,
 \quad
 \max_{\text{one nonanchor resource }q}
       \#\{A:q\in A\}\le C_1k^6,                        \tag{7.2}
\]

uniformly over the admitted boundary states, together with an exact cap
return/backup assignment.  One chosen ticket then conflicts with at most
`C_0C_1 d k^6` tickets in another anchor atlas, so greedy planting works for
`Hd=o(k)`.  Equivalently, the last two bounds may be replaced by the direct
total conflict-degree bound `O(dk^6)`.  None of these completed-ticket bounds
is currently proved.

There is a further atlas distinction.  The proved `O(k^6)` nonanchor load
belongs to the fixed-`z`, phasewise cap-exact rooted atlas.  In the raw
coprime-voltage twisted-geodesic atlas, fixing one moving-geodesic token can
still leave `Theta(k^7)` labelled completions.  Therefore the twisted count
cannot be inserted into (7.2) without first privatizing/matching the moving
geodesic skeleton or extracting a genuine `O(k^6)`-load subatlas.

Two one-line obstructions show why it cannot be inferred from the central
projection.

1. **Entrance obstruction.**  At `d=1`, a reset whose first deletion is `a`
   rejects incoming history `(a)`, regardless of its constant output.  Thus
   a centrally legal, cap-safe heptagon can have an empty completed-ticket
   fibre over a prescribed predecessor history.
2. **Cap obstruction.**  For nonzero coprime voltage, the sequential
   fixed-label rotor forces `z=rho^h z` and is impossible under a free action.
   Passive duplicates may preserve support through (4.1), but cannot return
   the cap multiset in (4.2).  An exact-multiset recurrence needs a nontrivial
   cap permutation or an active balanced return.

There is also an unavoidable correlation: an occurrence reserved as a cap
backup may lie in the support or entrance collar of another selected packet.
Therefore separate marginal abundance of central heptagons, backups, and
history tickets is insufficient.  The remaining theorem is a joint
completed-ticket matching/packing statement.

## 8. Provenance

This note uses the following frozen inputs.

- `MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md`,
  SHA-256
  `be97340b7983a558958117f94f063e913c1b250ab0f32cf6f146ee36e32cd0ef`;
- `MATH_THEOREM_A_EQUIVARIANT_DIRECTED_HISTORY_EAR_SEMIGROUPOID_AND_PULL_TRANSPORT_20260802.md`,
  SHA-256
  `a14ffb4c80af92fc4a1dcc3475e1d34f52d58c5ce29601c3fccc6f7ffe70f6b5`;
- `MATH_THEOREM_A_MIDDLE_LEVELS_PULL_EAR_GAP_MONOID_AND_PREPARED_TREE_DESCENT_20260802.md`,
  SHA-256
  `60f0248ab5e78becb26514fc780c46ed25c66caa09d59ea172e4a8b1686bce36`;
- `MATH_THEOREM_K_DIRECTED_HISTORY_PORT_MONOID_AND_PIVOT_RESET_20260802.md`,
  SHA-256
  `62610a0f2b7f5a9f01bf7331af6d73e57c3481cc072f3d1e08e8e1b7140163d9`.

The finite `k=17` long-run circuits certify that accepting history tickets
and duplicate-cap backups can coexist.  They do not prove the uniform fibre
bound (7.2), a protected Pascal embedding, or regeneration at growing depth.
