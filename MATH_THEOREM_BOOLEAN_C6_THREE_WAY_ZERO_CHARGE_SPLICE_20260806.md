# A Boolean C6 gives the first resource-disjoint zero-charge splice

## Status

**Superseded.**  The rank-correct literal collar construction and audited
version of this argument is
`MATH_THEOREM_THREE_WAY_C6_VORTEX_STATE_SPLICE_20260806.md`.  Retain this
file only as the abstract tensor derivation; cite the refined theorem.

The exact two-cut boundary tensor is too rigid for joining two factors that
are disjoint on both the owner and immediate-lower shores: a nontrivial
two-edge trade would be a `C4` in the middle-level incidence graph, and that
graph has no `C4`.

This note gives the correct minimal replacement.  Three opened source
components whose cumulative collars differ only by a cyclic three-label
pattern admit a length-preserving cyclic splice.  Every affected interval-OR
value is preserved as an occurrence multiset.  At the owner/root boundary the
six old and new incidences are exactly one Boolean `C6`, so the splice can join
three resource-disjoint components without repeating an owner or a root.

The theorem includes the exact occurrence-ticket transport and a sharp
capped-age condition.  It does **not** prove that the phase-adaptive vortex
factor and the exterior factor expose three such compatible collars.  That
planting statement is the remaining port theorem.

## 1. The general three-cut tensor

Let

\[
 C^{(t)}=(C^{(t)}_s)_{s\in\mathbb Z/N_t\mathbb Z},
 \qquad t\in\mathbb Z/3\mathbb Z,
\]

be three cyclic source components, each opened immediately before position
zero.  Define

\[
 L_i^{(t)}=\bigcup_{h=1}^i C^{(t)}_{-h},
 \qquad
 R_j^{(t)}=\bigcup_{h=0}^{j-1}C^{(t)}_h,
 \tag{1.1}
\]

with `L_0=R_0=emptyset`.  Replace the three old successor arcs by the cyclic
reconnection

\[
        \text{left side }t\longrightarrow\text{right side }t+1.
 \tag{1.2}
\]

No source position is inserted or deleted.

### Theorem 1.1 (exact three-cut criterion)

Fix a protected crossing width `G` and assume `N_t>=G` for all three
components, so an interval of protected width meets at most one changed
arc.  The splice (1.2) preserves the complete
boundary interval-OR multiset through width `G` if and only if, for every
`i,j>=1` with `i+j<=G`,

\[
 \boxed{
 \{\!\{L_i^{(t)}\cup R_j^{(t)}:t\in\mathbb Z/3\}\!\}
 =
 \{\!\{L_i^{(t)}\cup R_j^{(t+1)}:t\in\mathbb Z/3\}\!\}.}
 \tag{1.3}
\]

For occurrence-labelled preservation, (1.3) must be refined to a bijection
between equal-valued old and new cells carrying the same tickets.  Residence
is preserved if and only if the three new joins pass the corresponding
capped head/tail run and gap tests.

#### Proof

Every interval avoiding the three changed successor arcs is literally
unchanged.  For fixed `(i,j)`, the old crossing values are the left multiset
in (1.3), and the new crossing values are the right multiset.  This proves
the value assertion and, after retaining occurrence labels, the ticket
assertion.  A changed coordinate run or gap is obtained by concatenating one
old tail with one old head, so the usual capped-age test is also necessary
and sufficient.  No other interval or coordinate state changes. \(\square\)

## 2. The cyclic three-label tensor

Choose distinct labels

\[
                         a_0,a_1,a_2.                    \tag{2.1}
\]

Suppose that, for every relevant `i,j>=1`, there are common cumulative
profiles `Lambda_i,P_j`, none containing an active label, such that

\[
 L_i^{(t)}=\Lambda_i\cup\{a_t\},
 \qquad
 R_j^{(t)}=P_j\cup\{a_{t+1}\}.                          \tag{2.2}
\]

### Theorem 2.1 (Boolean-C6 zero-charge tensor)

Under (2.2), the cyclic splice (1.2) preserves every boundary interval-OR
value through the range in which (2.2) holds.  More precisely, for every
`i,j`, both the old and new multisets are

\[
 \boxed{
 \{\!\{
  (\Lambda_i\cup P_j)\cup\{a_0,a_1\},
  (\Lambda_i\cup P_j)\cup\{a_1,a_2\},
  (\Lambda_i\cup P_j)\cup\{a_2,a_0\}
 \}\!\}.}                                               \tag{2.3}
\]

The old occurrence in component `t` has the same value as the new
occurrence indexed by `t+1`.  Hence occurrence tickets transport exactly by

\[
                            t\longmapsto t+1.             \tag{2.4}
\]

If, in addition, every one-sided active-label run or gap exposed at the six
cut sides is already saturated at the required capped age, and the common
profiles have identical capped-age data and constant-coordinate flags in
the three components, then the splice is residence-safe.

#### Proof

The old cell in component `t` equals

\[
 (\Lambda_i\cup P_j)\cup\{a_t,a_{t+1}\}.                \tag{2.5}
\]

The new cell indexed by `t` equals

\[
 (\Lambda_i\cup P_j)\cup\{a_t,a_{t+2}\}.                \tag{2.6}
\]

As `t` ranges modulo three, both (2.5) and (2.6) enumerate the three
two-subsets of the active-label set, proving (2.3).  In (2.6) with index
`t+1`, the active pair is `{a_(t+1),a_t}`, proving (2.4).

Common coordinates see the same capped boundary states at every join.
For an active coordinate, every newly completed one-sided run or gap was
already saturated, while concatenating two saturated pieces can only remain
legal.  The constant flags rule out mistaking a component-long run or gap
for an ordinary capped segment.  This is exactly the capped-age test of
Theorem 1.1. \(\square\)

The saturation assumption is only a convenient local sufficient condition.
For a concrete carrier it may be replaced by the exact three capped-age
tests from Theorem 1.1.

## 3. The owner/root trade is exactly a Boolean C6

Let `S` have rank `r-2` and be disjoint from the three active labels.  Put

\[
 Q_t=S\cup\{a_t\},
 \qquad
 O_t=S\cup\{a_t,a_{t+1}\}.                              \tag{3.1}
\]

The old three incidences are

\[
                         Q_t\subset O_t,                 \tag{3.2}
\]

and the new three incidences are

\[
                         Q_t\subset O_{t-1}.             \tag{3.3}
\]

Together they form the alternating cycle

\[
 Q_0,O_0,Q_1,O_1,Q_2,O_2,Q_0.                           \tag{3.4}
\]

Thus the C6 splice preserves three distinct roots and three distinct owners
exactly.  If the three old factor edges lie on three distinct cycles, the
cyclic reconnection (1.2) merges those three source components into one.

Indeed, after traversing the unchanged interior of old component `t` from
its right side to its left side, (1.2) enters the right side of component
`t+1`.  The induced permutation of the three old components is the
three-cycle `t->t+1`, so the reconnected source word has one component.

### Proposition 3.1 (minimality)

There is no nontrivial two-edge owner/root trade in the Boolean
middle-level incidence graph.  Consequently a resource-disjoint exact
splice cannot first occur on fewer than three factor edges; the Boolean C6
above is minimal.

#### Proof

A nontrivial two-edge trade would require distinct roots `Q_1,Q_2` and
distinct owners `O_1,O_2` with all four containments `Q_i subset O_j`.
But two distinct rank-`r-1` roots contained in a rank-`r` owner have union
of rank `r`, and that union uniquely determines the owner.  Hence `O_1=O_2`,
a contradiction.  Equivalently, the adjacent-rank Boolean incidence graph
has no `C4`.  Its first alternating circuit is (3.4). \(\square\)

## 4. Exact remaining port theorem

The local phase-adaptive antipodal ring supplies owner phase when the
ambient and intrinsic deadlines agree and root phase when they differ by
one.  The present theorem shows the boundary object it must expose in order
to join a resource-disjoint exterior factor at zero length:

> **Prepared C6 port.**  Plant three opened, phase-appropriate decorated
> source components whose cumulative left and right collars have the form
> (2.2), whose occurrence tickets obey (2.4), and whose capped ages pass the
> three new joins.

Once such a port is present, all protected crossing OR values, the owner and
root resources, the occurrence tickets, and residence survive a
length-neutral three-way merge.  The unresolved content is now the
simultaneous planting of this C6 collar in the integral coloured
vortex/exterior cover-down.  Neither scalar deadline arithmetic nor a
two-cut equality condition remains in that gate.
