# Global reversal needs a boundary torsor: exact opening, pin, and Pascal-interface audit

**Date:** 2026-08-01  
**Lane:** K / reversal-quotient regeneration  
**Status:** exact interface theorem and scoped counterexamples

## 0. Verdict

The global-reversal quotient is exact for an existential same-parity
construction, but only after **all occurrence-labelled boundary data are
reversed with the word**.  It removes the demand for a fixed-address
intersection of the two phase compiler graphs.  It does not permit one to
forget which endpoint, cut, socket, parent copy, or prepared pin carries a
certificate.

The smallest useful exported object is therefore not an unoriented list of
marginal resources.  It is a **boundary torsor**

\[
   [\mathsf S]=\{\mathsf S,\mathcal R\mathsf S\},             \tag{0.1}
\]

where `S` contains the complete occurrence-labelled matching, witness,
opening, endpoint, parent-embedding, and named-socket data.  When several
parent copies or components are glued through locally feasible binary
reversal interfaces, their orientation bits satisfy an exact binary
constraint system.  On that face, the only global obstruction is its cycle
holonomy.

Consequently:

* one oriented complete host plus its reflected certificate is sufficient;
* a common fixed-address compiler and a common two-phase exterior are not
  required;
* named one-sided sockets and several parent copies still impose real
  relative-orientation constraints;
* the support-at-least-three exact-q1 connector obstruction is unchanged;
  and
* the `d(2d-1)` opening collateral is unchanged, value by value.  Only one
  oriented ambient repayment bank is required, because it too reflects.

## 1. Literal reversal transport

Let `A=(A_0,...,A_{n-1})` and let

\[
  (\mathcal RA)_i=A_{n-1-i}.
\]

For a linear interval `I=[i,j]`, put

\[
  I^*=[n-1-j,n-1-i].                                      \tag{1.1}
\]

Then

\[
 \bigcup_{t\in I}(\mathcal RA)_t=\bigcup_{t\in I^*}A_t,
 \qquad
 (D^q\mathcal RA)_i=(D^qA)_{n-q-1-i}.                    \tag{1.2}
\]

Thus a target--cell edge `(S,I)` is carried to `(S,I*)`.  A matching,
upper witness, protected owner, or cap assignment transports exactly when
its **occurrence address** is changed by (1.1).  This proves existence in
the reflected incidence graph, not at the same numerical address.

If reversal is accompanied by a fresh-coordinate permutation `sigma`, the
correct transport is

\[
                     (S,I)\longmapsto(\sigma S,I^*).        \tag{1.3}
\]

In particular, swapping fresh coordinates `x,y` does rename targets that
contain them.  Such a swap is a gauge only when the child target system and
all named pins are also transported by `sigma`.  It fixes old targets, but
not all child targets pointwise.

There is a second, independent typing issue.  If compiler rows distinguish
prefix from suffix, predecessor from successor, or left-padded from
right-padded erosion cells, reversal induces a type involution `tau`.  The
literal equivariance condition is then

\[
 G(\mathcal R\mathsf S)= (\tau\text{ on typed rows})
                         \times(\mathcal R\text{ on cells})\,G(\mathsf S).
                                                                    \tag{1.4}
\]

A set-valued target can be fixed while its typed role is exchanged.  A
transition which freezes the role name but not its reflected mate is not
covered by the quotient theorem.

## 2. Exact fixed-address and one-sided counterexamples

### Proposition 2.1 (fixed-address intersection is strictly stronger)

Let a target `s` have the unique occurrence cell `i` in one representative.
In the reflected representative its unique occurrence is `n-1-i`.  If
`i != n-1-i`, both representatives have a perfect matching on this row,
while their same-address intersection has no edge for `s`.

Hence a terminal existential compiler needs one matching modulo reflection.
A construction which pins `s` to numerical address `i` in both phases is a
different, strictly stronger problem.

### Proposition 2.2 (endpoint marginals do not determine a valid quotient)

Suppose an oriented state has an `X` socket and an old prepared anchor at
its left endpoint.  Its reflection has both at the right endpoint.  The
marginal assertion “there is an `X` socket and there is a prepared anchor”
does not imply the mixed demand

\[
                  \text{`X at the right and anchor at the left'}.          \tag{2.1}
\]

Neither representative satisfies (2.1).  Therefore endpoint resources must
be exported as the joint ordered pair

\[
                 ((L,\Pi_L),(R,\Pi_R))                     \tag{2.2}
\]

modulo simultaneous swap, not as two independent unoriented inventories.

This is the precise scope of a named one-sided socket: a theorem accepting
only a right socket is valid on the quotient iff every admissible orbit has
some representative with that socket on the right **and all other pins in
their required reflected positions**.

## 3. Openings and collateral

Let `c` be a cut gap of a cyclic word, and let `c*` be its reflected gap.
For every width `w`, reversal bijects the crossing intervals at `c` with
the crossing intervals at `c*` and preserves their union values.  Therefore

\[
                         \mathcal L_{c,w}=\mathcal L^R_{c^*,w}              \tag{3.1}
\]

as target-value multisets.  In the reset--return packet this gives, for
every cut,

\[
 \sum_{w=2}^{2d}(w-1)=d(2d-1)                             \tag{3.2}
\]

internally unique lost values in either representative.

### Corollary 3.1 (what the quotient actually saves)

One need not find the same ambient witness cells in both orientations.  If
an oriented exterior repays every value in the cut family, its complete
reflection repays the reflected family automatically.  But reversal does
not create a witness in the first orientation and does not change (3.2).

Thus the safe-opening task becomes:

> find one oriented cut plus one occurrence-labelled ambient repayment bank,
> and reflect the completed linear certificate.

It does not become “choose any cut”, nor does it become an `O(1)` ledger.

## 4. The Pascal boundary-torsor theorem

Consider a prospective child assembled from parent copies or protected
components indexed by the vertices of a graph `Gamma`.  Give copy `v` an
orientation bit

\[
                         \epsilon_v\in\mathbb F_2,           \tag{4.1}
\]

where adding one means reflecting that entire copy and all of its
certificates.  Suppose an interface edge `e=uv` is physically compatible
exactly when

\[
                         \epsilon_u+\epsilon_v=b_e           \tag{4.2}
\]

for its prescribed endpoint types.  A named one-sided socket is a unary
constraint `epsilon_v=s_v`.

### Theorem 4.1 (reversal holonomy)

With no unary constraints, the interface system (4.2) is feasible iff

\[
                         \sum_{e\in C}b_e=0                  \tag{4.3}
\]

for every cycle `C` of `Gamma`.  On each connected component, the solutions
then form one orbit under simultaneous reversal.  In particular:

1. a tree of Pascal copies has no further orientation obstruction once each
   local interface admits one of the two binary alignments;
2. a connected gluing graph has a unique relative orientation assignment
   modulo global reversal;
3. a cycle with odd sum in (4.3) is an exact obstruction invisible to every
   separate endpoint marginal; and
4. unary socket constraints are feasible iff they agree with the relative
   orientation forced along every path between pinned vertices.

#### Proof

Summing (4.2) around a cycle cancels every `epsilon_v`, proving necessity.
If (4.3) holds, choose one root orientation and propagate (4.2) along a
spanning forest.  Every non-tree edge is consistent precisely by (4.3).
Changing the root orientation adds one to all bits in that connected
component.  The unary statement follows by the same path propagation.
\(\square\)

The smallest obstruction is already three copies on a triangle with
`b_e=1` on all three interfaces: every pairwise port marginal is feasible,
but their sum would give `0=1` in \(\mathbb F_2\).  This is a literal
marginally compatible but globally unrealizable reversal state.

### Corollary 4.2 (minimal Pascal export)

For a binary reversal interface, the minimal proof-safe recursive state is:

1. the complete occurrence-labelled state modulo global reflection;
2. the ordered endpoint/socket pair as a two-element torsor;
3. the cut and ambient repayment bank modulo reflection;
4. the parent-copy embedding map modulo reflection;
5. the relative phase class on disconnected components; and
6. the involution on directed compiler/erosion row types; and
7. any unary orientation imposed by a named old-coordinate socket.

Forgetting item 4 makes the elementary append-only recursion already fail:

\[
                    C(A)=A\,u,
 \qquad
                    \mathcal R C(A)=u\,\mathcal RA,          \tag{4.4}
\]

whereas `C(RA)=RA u`.  A recursion offering only the right-append formula is
not reversal-equivariant.  It becomes equivariant by also allowing the
left-prepend formula (or by proving that the two sector roles may be
exchanged).  This is the exact issue for a Pascal construction with a
distinguished fresh coordinate or distinguished parent sector.

If two fresh coordinates are semantically unordered, reflecting the sector
order and swapping them repairs the interface.  If one is a named old
coordinate, the swap is not available and both oriented transition formulas
must be included explicitly.

## 5. Consequences for the reset-return host lane

### 5.1 What can now be deleted

For an existential one-component induction it is unnecessary to require:

* a fixed-address matching in \(G^+\cap G^-\);
* the same exterior cells in both orientations;
* a common-undirected two-phase host solely to compare a component with its
  reversal; or
* a local three-return role converter solely to change the global
  orientation representative.

Construct one oriented complete child, including its opening, exterior
witnesses, upper bank, and compiler, and reflect the whole certificate.

### 5.2 What remains unchanged

The following are reversal-invariant and therefore survive verbatim.

1. **Host existence and topology.**  One oriented carrier must still have
   the required path/cycle topology.  Reversal preserves its component
   count.
2. **Exact-q1 joining.**  A nondegenerate ordinary two-edge cross-splice
   between components of a squarefree upper-q1 factor still cannot preserve
   the upper palette.  The connector still needs support at least three or
   global palette compensation.  It need not additionally realize a common
   two-phase undirected edge set.
3. **Opening collateral.**  The `d(2d-1)` self-supply loss (3.2) is
   unchanged.  Its ambient repayment only has to be built in one orientation.
4. **Relative phases.**  With `c` independently orientable components,
   global reversal removes one diagonal bit and leaves `c-1` relative bits,
   or equivalently the holonomy state of Section 4.
5. **Defects.**  Upper holes, Hall deficiency, unsupported targets, and
   sidecar size are invariant under reflection.

### 5.3 Clean revised gate

The exact prospective target is therefore:

> Build one oriented, connected, resident and upper-complete host containing
> the reset-return packet; choose one legal opening and an ambient witness
> bank repaying its cut family; construct one occurrence-labelled common-cap
> compiler; and export its complete boundary torsor.  Once every local port
> pair is feasible in one binary alignment, a Pascal gluing tree may orient
> its copies freely.  A cyclic gluing scheme must additionally have zero
> reversal holonomy.

This statement makes no claim about a named one-sided socket, a local
phase-changing augmentation, or a frozen parent exterior.  Those remain
relative-phase problems.

## 6. Dependencies and scope

This audit uses the exact reversal and packet theorems:

* `MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md`;
* `MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`;
* `MATH_THEOREM_RESET_OPEN_PATH_PHASE_COMMON_Q1_HOST_20260801.md`;
* `MATH_THEOREM_RESET_RETURN_RAIL_LINEARIZATION_COLLATERAL_20260801.md`; and
* `MATH_THEOREM_K_RESET_RETURN_RAIL_CATALAN_Q1_PACKING_AND_COMPLETE_REVERSAL_HOST_GATE_20260801.md`.

No existence of the oriented host, ambient repayment bank, Pascal gluing
tree, or common-cap compiler is asserted.
