# A bounded zero-current `D_3` packet needs only one-basis terminal stability

**Date:** 2026-08-06  
**Method:** two-Rado rank perturbation, occurrence-fibre transport, and an
elementary remote-diamond packing argument; no computation or search  
**Status:** unconditional reduction theorem.  It proves that a bounded
terminal `D_3` packet bank requires no Hall theorem of its own for an
additive-constant upper bound.  One transported background common basis,
up to bounded loss, is sufficient.  It also gives two independent routes to
zero terminal loss: a capacity-faithful occurrence transport, or a typed
native-diamond realization of the bounded residual tickets.  The suspended
`D_3` endpoint theorem and zero all-width *value* current do not by
themselves prove either occurrence-level premise.

## 0. Verdict

Let `B` be the transported background **target-ticket** set and let `H` be
the new terminal target-ticket set created by a packet circuit.  Every
omitted label below therefore has one literal mask which may be appended as
one final word letter.  Recursive service, topology, and residence
obligations are not charged this way.  Suppose

\[
                         |H|\le h                              \tag{0.1}
\]

for an absolute constant `h`.

For an additive-constant theorem there is no need to link the tickets in
`H`.  They may all be omitted and appended literally at the terminal word.
The only required common-cap statement is that one occurrence-labelled
common basis for `B` survives, apart from a bounded set.  In particular,
the all-subset condition from the two-Rado theorem is stronger than needed
on this terminal bounded bank.

There are three useful levels.

1. If one simultaneous background bundle family loses at most `kappa`
   logical labels, then terminal deficiency is at most `kappa+h`.
2. If occurrence system `p` changes only through `q_p` exceptional
   unit-capacity resources, then

   \[
        \operatorname {def}_{+}
          \le \operatorname {def}_{-}+q_0+q_1+h.              \tag{0.2}
   \]

3. If the circuit transports the actual terminal compiler occurrence
   ledger value-fibre by value-fibre, then the old literal compiler
   matching transports with zero loss.  No terminal two-coordinate cap is
   needed for target coverage.

For a fixed number of residual tickets, an upper-surjective middle-level
diagonal supplies two remote, pairwise footprint-disjoint native diamonds
per ticket outside any `O(r)` protected `D_3` bank.  This closes the
*combinatorial port selection* row.  It closes the typed common cap only if
those diamonds are accepted complete terminal bundles in the same cap
state and coexist with the background.

## 1. One common basis is the weakest terminal object

Fix a complete final cap/guard/occurrence state `c`.  A **complete paired
bundle** for a logical label `i` consists of all required occurrence paths
in systems `0` and `1`, with their common state, shared capacities and
terminal identities already resolved.  A bundle family is simultaneous
when all its members coexist physically.

### Theorem 1.1 (one-basis terminal stability)

Let the final logical universe be the disjoint union

\[
                              I=B\mathbin{\dot\cup}H.
\]

Suppose one subset `B' subseteq B` has a simultaneous complete paired-bundle
family in `c`, and

\[
                              |B\setminus B'|\le\kappa.
\]

Then the final common-cap deficiency is at most

\[
                              \boxed{\kappa+|H|}.              \tag{1.1}
\]

This conclusion needs no rectangularity or product-closure assertion for
the omitted tickets.

#### Proof

The displayed bundle family is a physically feasible common independent
set of size `|B'|`.  The final universe has size `|B|+|H|`.  Hence its
deficiency is at most

\[
 |B|+|H|-|B'|=|B\setminus B'|+|H|\le\kappa+|H|.
\]

No statement about the unselected labels is used. \(\square\)

Thus, when `|H|=O(1)`, proving Hall for `H` can improve the numerical
constant but is not load-bearing for `B(k)+O(1)`.

## 2. Two-Rado deficiency is Lipschitz under bounded physical loss

We now give a checkable way to obtain the `B'` in Theorem 1.1.  Use the
notation of
`MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`.
Let `N_p^-` and `N_p^+` be the residual occurrence gammoids before and after
the terminal circuit.  Their Rado matroids on the same background label set
`B` are `R_p^-` and `R_p^+`, with ranks `rho_p^-` and `rho_p^+`.

Assume there is an occurrence-labelled injection from the old network into
the new one after deletion of a set `D_p` of unit-capacity vertices or sink
slots, with

\[
                              |D_p|=q_p.                       \tag{2.1}
\]

It must preserve direction, terminal type, common state and physical
capacity identity, and it must send every surviving old entry port of a
background ticket to an admitted new entry port of the same ticket.  The
new network may have additional resources.

### Lemma 2.1 (gammoid deletion Lipschitz bound)

For every admitted old port set `X`,

\[
                  r_{N_p^+}(X^+)\ge r_{N_p^-}(X)-q_p,          \tag{2.2}
\]

where `X^+` is its transported surviving image.

#### Proof

Take a maximum old vertex-disjoint linkage from `X` to the typed terminal
bank.  A deleted unit resource belongs to at most one path of this linkage.
Discard every path meeting `D_p`.  At most `q_p` paths are discarded, and
the occurrence injection carries every remaining path to the new network.
This proves (2.2). \(\square\)

### Lemma 2.2 (Rado-rank deletion Lipschitz bound)

For every `S subseteq B`,

\[
                         \rho_p^+(S)\ge\rho_p^-(S)-q_p.        \tag{2.3}
\]

#### Proof

For `J subseteq S`, the Rado formula and Lemma 2.1 give

\[
\begin{aligned}
 |S\setminus J|+r_{N_p^+}(A_p^+(J))
 &\ge |S\setminus J|+r_{N_p^-}(A_p^-(J))-q_p.
\end{aligned}
\]

Here Lemma 2.1 is first applied to the surviving transported image of
`A_p^-(J)`, which is a subset of `A_p^+(J)` by the menu-preservation
hypothesis; monotonicity of gammoid rank then gives the displayed left
side.

Take the minimum over `J`. \(\square\)

### Theorem 2.3 (two-coordinate physical perturbation bound)

Assume the old and new fixed cap states each satisfy the product-closure
and cross-system capacity-separation hypotheses of the exact two-Rado
theorem.  If the old common deficiency on `B` is `beta`, then the new
common deficiency on `B` is at most

\[
                              \boxed{\beta+q_0+q_1}.           \tag{2.4}
\]

After adjoining the bounded packet label set `H`, the deficiency is at
most

\[
                         \boxed{\beta+q_0+q_1+|H|}.            \tag{2.5}
\]

#### Proof

Edmonds' formula and Lemma 2.2 give

\[
\begin{aligned}
 \nu^+
 &=\min_{U\subseteq B}
      \bigl(\rho_0^+(U)+\rho_1^+(B\setminus U)\bigr)\\
 &\ge\min_{U\subseteq B}
      \bigl(\rho_0^-(U)+\rho_1^-(B\setminus U)\bigr)
       -q_0-q_1\\
 &=|B|-\beta-q_0-q_1.
\end{aligned}
\]

This proves (2.4).  Omitting every member of `H` and applying Theorem 1.1
proves (2.5). \(\square\)

The theorem has an even weaker direct-bundle form which does not use
product closure for unselected labels.  Fix one old simultaneous bundle
family covering all but `beta` background labels.  If its system-`p` paths
are pairwise disjoint, at most `q_p` of its logical bundles meet `D_p`.
Deleting the union of those affected labels leaves an explicit new
simultaneous family of size at least `|B|-beta-q_0-q_1`.  This is precisely
Theorem 1.1.

## 3. Exact occurrence transport bypasses the terminal cap

Let `O^-` and `O^+` be the actual capacity-one compiler-cell occurrence
sets before and after a terminal circuit.  An occurrence includes its
physical address exactly once; aliases of one physical cell are not
separate occurrences.  Write `v(o)` for the literal OR value of occurrence
`o`.

### Theorem 3.1 (value-fibre occurrence transport)

Suppose

\[
       |\{o\in O^-:v(o)=S\}|=|\{o\in O^+:v(o)=S\}|             \tag{3.1}
\]

for every strict-lower target value `S`.  Then there is a bijection

\[
                              \Phi:O^-\longrightarrow O^+
\]

with `v(Phi(o))=v(o)`.  Consequently every literal compiler matching in
the old word transports to a literal compiler matching in the new word
with zero deficiency.

#### Proof

For every value `S`, choose an arbitrary bijection between the two finite
fibres in (3.1), and take their disjoint union.  If `mu(S)` is the old cell
assigned to target `S`, then `Phi(mu(S))` has value `S`.  Since `Phi` is
injective, different targets still use different physical cells. \(\square\)

The same proof works with `>=` in (3.1), using an injection.  It is purely
terminal: it proves target coverage, not a recursive typed service state.

### Corollary 3.2 (proof obligation for a zero-current `D_3` circuit)

Suppose a simple endpoint-sealed `D_3` circuit is realized in an ordinary
source word and its complete signed current vanishes on the **capacity-
faithful terminal compiler occurrence ledger**, including every crossing
occurrence.  Then the circuit preserves every old strict-lower compiler
matching exactly.  Its terminal lower common-cap deficiency is zero.

The qualification is essential.  The current identities in the present
`D_3` and Tamari notes are identities of owner-path chord values.  The
endpoint-sealed pentagon theorem proves exactness of the common-tail factor
resources.  Neither statement alone identifies those value occurrences
with the final antecedent cells or proves preservation of cap flags,
terminal types, or conjunctions of two physical occurrence coordinates.
Thus Corollary 3.2 becomes applicable only after an occurrence-level source
lift, not merely after a formal zero-current identity.

There is, however, one part of that lift which follows automatically from
the resident maximal-antecedent row identity.

### Theorem 3.3 (top-`d` intersection-current lift)

For `epsilon in {-,+}`, let `T^epsilon` be a cyclic `d`-resident owner
trace and let

\[
 P_p^\epsilon=\bigcap_{t=0}^{d}T_{p-t}^\epsilon
\]

be its maximal antecedent.  The statement below is literal for cyclic
components.  For a disjoint union of owner paths, restrict to source cells
whose defining owner intervals are untruncated interiors, or first pad and
price the endpoint collars; a component tag alone does not repair a clipped
endpoint identity.  Suppose that, for every `1<=q<=d`, the two phases have
the same **value multiset** of owner-intersection occurrences

\[
 \left\{\!\left\{
       \bigcap_{j=0}^{q}T_{i+j}^-:i
 \right\}\!\right\}
 =
 \left\{\!\left\{
       \bigcap_{j=0}^{q}T_{i+j}^+:i
 \right\}\!\right\}.                                      \tag{3.2}
\]

Then the corresponding maximal antecedents have a width- and
value-preserving occurrence bijection on the source cells

\[
                         J^\epsilon(i,q)=[i+q,i+d],
                         \qquad1\le q\le d.                   \tag{3.3}
\]

Consequently every compiler matching supported on the top `d` lower fan
layers transports with zero loss.

#### Proof

The maximal-antecedent row identity gives

\[
 \bigcup_{p=i+q}^{i+d}P_p^\epsilon
       =\bigcap_{j=0}^{q}T_{i+j}^\epsilon.                    \tag{3.4}
\]

The equality in (3.2) is equality of finite value fibres indexed by their
available occurrence addresses; it is not equality of literal
`(value,address)` pairs across the two phases.  The pair `(i,q)`, together
with its cyclic-component tag, determines one physical source interval,
and different pairs give different addressed intervals.
For fixed `q` and target value, match the equal finite fibres in (3.2).
Taking the disjoint union over `q` produces a width- and value-preserving
bijection of the cells (3.3).  Compose any old matching with this
bijection. \(\square\)

Thus a complete zero **intersection** current of an endpoint-sealed `D_3`
circuit already transports the canonical top-`d` compiler bank, provided
the current includes the global crossing occurrences and both phases use
their maximal antecedents.  What it does not transport automatically is:

* a nonmaximal thinning used to realize deeper targets;
* ranks below `r-d`;
* typed suffix paths attached to the same cells; or
* cross-component intervals omitted from the current ledger.

This is the precise part of the terminal common cap which the all-width
factor current really does remove.

### Theorem 3.4 (read-only owner coordinate removes the two-Rado coupling)

Suppose the pre-circuit owner factor contains, for every strict-lower target
`S`, a named owner interval `K_S^-` with

\[
                         \bigcap_{j\in K_S^-}T_j^-=S.          \tag{3.5}
\]

Suppose the complete zero intersection current of the circuit includes
these widths and hence leaves at least the same multiplicity of every
intersection value in the post-circuit owner factor.  Choose one resulting
owner interval `K_S^+` for every `S`.  Treat these owner intervals as
read-only witnesses: they may overlap and consume no selectable terminal
capacity.

Then the final strict-lower compiler problem is only the ordinary
one-coordinate problem

\[
  \text{inject }S\longmapsto I_S
  \quad\text{with}\quad
  \bigcup_{p\in I_S}A_p^+=S.                                \tag{3.6}
\]

There is no common-cap correlation between `K_S^+` and `I_S` beyond their
common target label `S`.  In particular, Theorem 3.3 supplies (3.6)
automatically for ranks `r-d,...,r-1`; only the deeper relative source
payload atlas remains.

#### Proof

Equality of the intersection-value multiplicities supplies each witness
`K_S^+`.  Witnesses for set containment in one fixed owner factor are not
routes through a unit-capacity terminal network; the same owner edge may
certify arbitrarily many target identities.  Thus their mutual overlap is
irrelevant.

The actual OR word needs one distinct source interval of value `S` for
each target.  Those are exactly the injectivity and equality requirements
in (3.6).  Once `I_S` is chosen, the pair

\[
                              S\longmapsto(K_S^+,I_S)
\]

is automatic, because its first coordinate is already present and
read-only.  Theorem 3.3 gives the claimed top-`d` source intervals.
\(\square\)

This theorem applies only when the owner coordinate is genuinely a witness
rather than a typed, capacity-consuming recursive service.  It is the
terminal PBBS/read-only-section quantifier, not a statement about an active
child continuation.

## 4. A constant bank has remote native diamonds by elementary expansion

The following closes the abstract port-selection row without a large Hall
theorem.

Let `n=2r-1`.  In an upper-surjective flat `q1` diagonal, use the native
diamonds

\[
 p_i-o_i-q_i,\qquad p_i-o_{i+1}-q_i,
 \qquad R_i=v(q_i)\in{[n]\choose r+1}.                         \tag{4.1}
\]

Its physical footprint is

\[
                              \Xi_i=\{p_i,o_i,o_{i+1},q_i\}.   \tag{4.2}
\]

Let `F` be the forbidden set of **all** indices `i` for which `Xi_i` meets
a capacity occupied by the protected `D_3` circuit or by any
non-coinstantiable background role.  Thus `i notin F` means that the whole
diamond footprint, not merely its owner edge, avoids the protected bank.

### Theorem 4.1 (constant-bank remote-diamond packing)

Let `x_1,...,x_h` be labelled tickets, repetitions of values allowed, with

\[
                              1\le |S(x_j)|\le r-1.
\]

If

\[
             {r\choose2}>|F|+3(2h-1),                         \tag{4.3}
\]

then one can assign two indices to every ticket so that

1. `S(x_j) subseteq R_i` at both assigned indices;
2. no assigned index lies in `F`; and
3. all `2h` footprints `Xi_i` are pairwise disjoint.

#### Proof

Fix a ticket value `S` of rank `s<=r-1`.  The number of rank-`r+1` sets
containing it is

\[
                 {2r-1-s\choose r+1-s}
                 ={r+(r-1-s)\choose 2+(r-1-s)}
                 \ge {r\choose2}.                            \tag{4.4}
\]

Upper surjectivity supplies a distinct diagonal index for every one of
these upper values.  Hence the raw index menu of every labelled clone has
size at least `binom(r,2)`.

Choose the `2h` indices greedily.  One previously selected cycle edge
forbids at most its own index and the two adjacent indices, because
nonadjacent owner edges have disjoint footprints (4.2).  Before the final
choice, at most `3(2h-1)` menu indices are forbidden by earlier choices,
in addition to `F`.  Inequality (4.3) leaves an admissible index. \(\square\)

### Corollary 4.2 (bounded suspended packet banks do not exhaust ports)

If a bounded simple endpoint-sealed `D_3` circuit occupies `O(1)` suspended
rows, its rowwise `q1` footprint has size `O(r)`.  Assume, as in the native
diagonal model of Theorem 4.1, that each protected physical capacity belongs
to only `O(1)` of the footprints `Xi_i`.  Then the induced forbidden index
set `F` also has size `O(r)`.  Therefore, for fixed `h`, condition (4.3)
holds for all sufficiently large `r`, even after forbidding that entire
footprint and any additional `O(r)` private halo.

Endpoint sealing matters here because it prevents an additional
unaccounted terminal-tail bank from being charged outside the displayed
row footprints.  The conclusion is only port abundance and disjointness.

### Corollary 4.3 (conditional exact residual routing)

Under Theorem 4.1, suppose additionally that, in one fixed cap state,

1. every selected containing diamond is a legal **complete** terminal
   route for the assigned occurrence coordinate of its ticket;
2. its finite footprint is available after the background, or every shared
   role is literally coinstantiated;
3. the two coordinates of one ticket accept the selected pair; and
4. disjoint footprints remove every remaining cross-ticket and
   cross-system coupling.

Then every ticket in `H` is routed in both coordinates and contributes zero
terminal deficiency.

#### Proof

Treat the two occurrence coordinates as two labelled clones of each
ticket.  Theorem 4.1 gives disjoint complete routes for all clones.  The
four extra hypotheses give global product closure and legal pairing, so
their union is a common independent set covering `H`. \(\square\)

This is the fixed-`h` elementary specialization of the polynomial native-
diamond router.  It shows exactly what symmetric middle-level expansion
does prove.  It does **not** turn containment `S subseteq R_i` into a typed
claim-to-port prefix, and it does not release a port occupied incompatibly
by the transported background.

## 5. Sharp consequence for the assumed `D_3` current circuit

Assume now that a bounded, simple, endpoint-sealed, zero-all-width `D_3`
current circuit has been constructed.

### Additive-constant conclusion

If one old background common basis transports through the circuit with at
most `kappa=O(1)` lost logical labels, and the circuit creates at most
`h=O(1)` residual packet labels, then

\[
                    \boxed{\operatorname {def}_{\rm terminal}
                                  \le\kappa+h=O(1).}           \tag{5.1}
\]

No Hall or gammoid expansion condition is required on the residual packet
bank.  Append its omitted masks together with the `kappa` background
casualties once, at the requested terminal dimension.

One sufficient way to obtain `kappa` is Theorem 2.3 with

\[
                         \kappa=\beta+q_0+q_1.                 \tag{5.2}
\]

Another is a direct value-preserving occurrence injection on all but
`kappa` cells of one old literal compiler matching.

### Zero-defect upgrades

Either of the following removes the bounded packet charge as well.

1. The all-width circuit lifts to the capacity-faithful occurrence
   transport in Theorem 3.1 and carries the full old compiler.
2. The background transports exactly and the residual packets satisfy the
   typed native-diamond hypotheses of Corollary 4.3.

The first is a terminal compiler-transport theorem; the second is a typed
router theorem.  They should not be conflated.

## 6. Why protected-factor expansion alone cannot prove the cap row

A symmetric middle-level factor proves owner and immediate-palette
incidence.  It may also provide many abstract ports.  It does not assign a
literal prefix from a compiler claim to a physical port, reserve a typed
suffix to a sink, or certify a two-coordinate product bundle.

The standard bottleneck example remains decisive.  Give `m` nonzero
tickets distinct abstract factor incidences but force every complete
physical route through one common unit vertex.  Every ticket has a port and
an individual route, while the gammoid rank of the whole bank is one and
the deficiency is `m-1`.  Thus abstract factor expansion cannot imply
typed common-cap expansion.

For the bounded residual bank this obstruction is harmless for
`B(k)+O(1)`, because `m=h=O(1)` and all such labels may be omitted.  It is
still decisive for the transported background: an unpriced source/cap
change can destroy a growing number of background assignments even when
the owner current is zero.  Hence one of the following must remain
explicit:

* a transported simultaneous background bundle family;
* a bounded physical-resource perturbation as in Theorem 2.3;
* a capacity-faithful compiler-occurrence injection; or
* a genuine typed all-cut theorem for the background.

## 7. Exact remaining gate

After a bounded simple zero-all-width `D_3` current circuit, the terminal
common-cap problem is no longer a large two-ray Hall problem.  Its weakest
additive-constant form is

> **Background one-basis transport.**  Carry one occurrence-labelled
> simultaneous compiler basis through the circuit, losing only `O(1)`
> logical labels.

The endpoint-sealed pentagon matchings close the terminal endpoint columns,
and Theorem 4.1 gives ample remote ports for any bounded residue.  What is
not yet automatic is the identification of the formal all-width factor
current with an actual source-cell or typed-bundle transport.  Proving that
identification would give zero terminal compiler loss; proving it outside
only `O(1)` bundles already suffices for `B(k)+O(1)`.
