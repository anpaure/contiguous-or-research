# The clean lag-two fragmentation is not a compiler-functorial source rewrite

**Date:** 2026-08-07  
**Method:** exact interval-value comparison; no computation or search  
**Status:** unconditional local no-go for the natural ordinary fixed-core
off-state.  Fragmenting an ordinary fixed-core rail into the clean lag-two
collar deletes at least \(d-1\) named strict-lower values.  Therefore the
terminal compiler-transport theorem cannot simply be applied across this
rewrite.  A global construction may still escape by planting backup
occurrences, carrying the fragmented state from the parent, or using a
different lower-deck-bijective packet.

## 1. Ordinary and fragmented phases

Use the data of
`MATH_THEOREM_PBBS_LAG2_FIXED_CORE_RAIL_COLLAR_20260807.md` with \(d\ge2\):

\[
 G=Q\mathbin{\dot\cup}C_0\mathbin{\dot\cup}\{a_0\},
 \qquad |C_0|=d-1,
\]

and a cyclic stream of distinct toggles outside \(G\), containing

\[
 b^-,u,a_1,\ldots,a_{d-1},z,b,v.
 \tag{1.1}
\]

The **ordinary phase** has source letter

\[
 A_t^0=G\cup\{\tau_t\}
 \tag{1.2}
\]

at every toggle position.  The **fragmented phase** agrees outside (1.1)
and replaces that substring by

\[
 C_0+b^-,\quad \{u\},\quad
 Q+a_0+a_1,\ldots,Q+a_0+a_{d-1},\quad
 C_0+z,\quad\{b\},\quad\{v\}.
 \tag{1.3}
\]

For \(d=2\), the last letter may instead be \(Q+a_0+v\), as required by
the literal lower-seam repair.  The argument below is unchanged.

Both phases have the same length-\((d+2)\) owner values on the collar:
fragmentation changes the short source deck while preserving the displayed
owner path.

## 2. Exact lost values

For \(1\le i\le d-1\), put

\[
 V_i=G\cup\{a_i\}
 =Q\cup C_0\cup\{a_0,a_i\}.
 \tag{2.1}
\]

Each \(V_i\) has rank

\[
 |V_i|=|G|+1=m-d-1<m,
 \tag{2.2}
\]

so it is a strict-lower target.

### Theorem 2.1 (\(d-1\) disappearing strict-lower targets)

In the ordinary phase, \(V_i\) has exactly one interval occurrence: the
one-letter cell at the toggle \(a_i\).  In the fragmented phase, \(V_i\)
has no interval occurrence at all.  Consequently there is no exact-value
literal lower transport from the complete ordinary strict-lower deck to
the fragmented deck.

#### Proof

In the ordinary phase, a nonempty interval has value

\[
 G\cup\{\text{all toggles met by the interval}\}.
 \tag{2.3}
\]

The toggles are distinct and all lie outside \(G\).  Equality with
\(V_i=G+a_i\) therefore forces the interval to meet exactly the one toggle
\(a_i\), hence to be its one-letter cell.  This proves existence and
uniqueness before fragmentation.

Now consider an interval in the fragmented phase.

* If it meets an ordinary position, that letter supplies all of \(G\) and
  also its designated noncore toggle.  Equality with \(V_i\) would force
  that toggle to be \(a_i\).  But the unique \(a_i\)-position is
  exceptional, so this is impossible.
* Suppose it is wholly contained in the exceptional substring.  To contain
  \(Q\cup\{a_0\}\), it must meet an internal letter
  \(Q+a_0+a_j\) (or, in the \(d=2\) endpoint convention, the enriched last
  letter).  To contain \(C_0\), it must meet either
  \(C_0+b^-\) or \(C_0+z\).  The first choice introduces \(b^-\notin V_i\),
  and the second introduces \(z\notin V_i\).  Thus equality is again
  impossible.

These cases exhaust all cyclic intervals.  Hence \(V_i\) is absent after
fragmentation.  The values \(V_1,\ldots,V_{d-1}\) are distinct, proving
the stated loss.  A value-preserving occurrence injection cannot map a
cell whose value has disappeared. \(\square\)

## 3. Consequence for terminal compiler transport

Let \(\mu\) be a compiler matching covering every strict-lower target in
the ordinary fixed-core rail.  By Theorem 2.1, \(\mu(V_i)\) is forced to be
the unique one-letter \(a_i\)-cell.  After fragmentation there is no cell
of value \(V_i\), so no map satisfying

\[
 \operatorname{OR}_{A^1}(\Phi(\mu(V_i)))=V_i
 \tag{3.1}
\]

exists.  Thus the clean lag-two collar is absent from the list of
compiler-functorial rewrites in
`MATH_THEOREM_TERMINAL_PBBS_COMPILER_TRANSPORT_BYPASS_AND_COMMON_HISTORY_TREE_GATE_20260806.md`
for a substantive reason, not merely because it had not yet been audited.

For a bank of collars whose values \(V_{j,i}\) are pairwise distinct, the
same argument creates at least

\[
 h(d-1)
 \tag{3.2}
\]

distinct old-target casualties.  This count is conditional on cross-collar
target distinctness; the one-collar lower bound \(d-1\) is unconditional.

## 4. Relation to a same-parity lift

The no-go is exact for the following tempting induction:

1. lift a parent compiler into an ordinary fixed-core child rail;
2. fragment isolated portions of that rail into the clean lag-two
   promotion collars; and
3. invoke terminal compiler functoriality without changing the matching.

Step 2 has no complete literal lower transport, so this implication is
invalid.

The theorem does **not** exclude three different architectures.

1. **Persistent fragmented history.**  The parent-to-child lift may carry
   already fragmented collars, so no ordinary-to-fragmented rewrite is
   performed at the terminal dimension.
2. **Protected backup bank.**  Before fragmentation, one may materialize
   a second occurrence of every \(V_i\) outside the collar and transport
   that occurrence instead.
3. **Deck-bijective packet.**  A different promotion packet may preserve
   the complete old strict-lower occurrence deck while still creating the
   required new boundary chain.

Each escape needs a theorem not currently supplied by the clean fixed-core
collar.

## 5. Exact surviving compiler gate

The new arbitrary-boundary-deletion theorem removes the ordinary Ferrers
capacity correlation, but it does not repair the lost values (2.1).
Capacity says that every residual named target can be assigned to an ideal
owner slot; it does not manufacture a literal interval occurrence.

Therefore a recursion-based escape from sharp global chainization must
prove one of the following exact statements:

* a same-parity occurrence injection that bypasses all fragmented support;
* a backup occurrence atlas for the \(V_i\)'s (and every other changed
  short value) with bounded regenerative state; or
* a modified clean packet having a complete exact-value injection on the
  inherited compiler cells.

Without one of these rows, the terminal compiler cannot be transported
through isolated clean lag-two packets merely by composition.
