# Freeze-after-rectangle private Pascal splice

**Date:** 2026-08-02  
**Status:** unconditional exact composition theorem for a frozen sufficient
support of the lower owner/target-labelled rotor row, with an exact
ordered-port interface and a sharp boundary showing why the stationary
pull-clock and static SCD marginals do not supply that interface
automatically.  The zero-charge conclusion is for the postselection
restricted support; unused physical options may still exist.  No
upper-shadow, residence, exterior-window, or common-cap/compiler assertion
is made.

## 0. Result

There is a regenerative positive face of the Hall-safe tree problem which
is stronger than merely having a cycle cover.

A **private-rooted Hamilton table** consists of a one-cycle predecessor
selection and one distinguished closing role.  Every other selected role
has a singleton legal tail list.  Deleting the closing arc leaves a
spanning directed path made entirely from zero-charge roles.

Suppose two disjoint private-rooted tables expose closing arcs

\[
 h_{p_0}\longrightarrow h_{g_0},\qquad
 h_{p_1}\longrightarrow h_{g_1}.                         \tag{0.1}
\]

If both crossed assignments

\[
 h_{p_1}\longrightarrow h_{g_0},\qquad
 h_{p_0}\longrightarrow h_{g_1}                          \tag{0.2}
\]

are literal and retain the old role payloads, switch (0.1) to (0.2), then
**freeze one crossed role to its selected tail**.  The result is again a
private-rooted Hamilton table: the other crossed role is the new closing
role.  Thus the certificate is closed under a binary Pascal splice.  A
binary hierarchy of such compatible ports gives one Hamilton rotor and a
zero-charge singleton-tail spanning path, using one rectangle per internal
node and no lower sidecar.

This does not contradict the fact that a nontrivial atomic rectangle cannot
itself have singleton lists.  Before the switch, both rectangle roles have
at least two options.  Privacy is imposed only after the internal matching
choice is fixed; equivalently, the rectangle is first contracted and its
chosen external socket is then frozen.

For a depth-\(d\) Boolean flag table the exact exported port is not a rotor
type.  It is the literal record

\[
                 (w;c\mid P,T),                         \tag{0.3}
\]

where \(w\) is the ordered \((d-1)\)-letter rail, \(c\) is the leading
letter of the selected predecessor token, and \([P,T]\) is the role's
Boolean cap interval.  Two closing ports cross if and only if their rail
words agree and each leading letter belongs to the opposite cap interval.
The stationary pull clock records none of these literal correlations.

The protected SCD theorem does show that the two portal flags can be
planted without losing a named lower target: quarantine them unmarked, or
retain pairwise-distinct forced target occurrences.  It does not provide
their predecessor tokens, owner caps, or common ordered rail.

The independent all-high audit at \((k,d)=(5,2)\) gives the sharp first
boundary.  Every balanced owner-exact strict table has the forced cover
\(C_5(+1)\mathbin{\dot\cup}C_5(+2)\), and every realized predecessor list
is already singleton.  Hence no nontrivial rectangle is available to start
the freeze operation.  A same-parity recursion must export an open port,
use a non-all-high role, or construct a matching-closed macro before
freezing.

## 1. Fixed-head labelled tables

Let \(I\) be a finite occurrence-role set and let

\[
                         h_i\in V\qquad(i\in I)          \tag{1.1}
\]

be pairwise-distinct fixed head states.  Role \(i\) has a full physical
legal-tail list \(\widehat N(i)\subseteq V\).  A **frozen sufficient
support** chooses a nonempty sublist

\[
                         N(i)\subseteq\widehat N(i).     \tag{1.1a}
\]

Any selector in the frozen support is a selector in the physical table.
Its owner, every declared named lower target, and every protected lower-row
label are fixed on the whole physical list.
Thus choosing \(t_i\in N(i)\) selects the directed state edge

\[
                         t_i\longrightarrow h_i.         \tag{1.2}
\]

A balanced one-copy selection is a permutation of the head bank: there is
a permutation \(\pi\) of \(I\) such that

\[
                         t_i=h_{\pi(i)}\in N(i).          \tag{1.3}
\]

The selected token components are the cycles of \(\pi\).

### Definition 1.1 (private-rooted Hamilton table)

A selected frozen support \((\mathcal F,\pi,g)\) is private-rooted when

1. \(\pi\) is one cycle on \(I\);
2. \(g\in I\) is a distinguished closing role; and
3. every other role is private at its selected predecessor:

   \[
                         N(i)=\{h_{\pi(i)}\}
                         \qquad(i\ne g).                \tag{1.4}
   \]

Write \(p=\pi(g)\).  The exported closing port is the selected arc

\[
                         h_p\longrightarrow h_g.         \tag{1.5}
\]

The role \(g\) is deliberately not required to be private.  Its unused
options are the only options needed by the next recursive splice.

### Lemma 1.2 (zero-charge path certificate)

In a private-rooted Hamilton table the assignments on

\[
                         R=I\setminus\{g\}               \tag{1.6}
\]

form a spanning directed path on the head bank.  They have escape charge

\[
                         \chi_R(Y)=0
                         \qquad(Y\subseteq V).           \tag{1.7}
\]

The one residual role \(g\) closes that path.

#### Proof

Deleting one arc from a directed Hamilton cycle leaves a spanning directed
path.  Every role in \(R\) has a singleton list, so

\[
 t_i\in Y\quad\Longrightarrow\quad N(i)\subseteq Y.
\]

Every summand in the cut-charge definition is therefore zero.  The removed
arc (1.5) closes the path by construction. \(\square\)

Consequently (1.6) is precisely a Hall-safe tree of the cut-charge theorem
in the frozen sufficient instance: it spends no Hall slack on any shore.
This proves physical existence because of (1.1a), but it does not assert
that omitted physical options disappeared.  A hereditary physical
singleton claim requires an additional guard or a literal macro
contraction.

## 2. Exact binary splice

Let \((\mathcal F_0,\pi_0,g_0)\) and
\((\mathcal F_1,\pi_1,g_1)\) be private-rooted Hamilton tables on disjoint
head-token banks.  Put

\[
                         p_\epsilon=\pi_\epsilon(g_\epsilon)
                         \qquad(\epsilon=0,1).          \tag{2.1}
\]

View both tables inside one parent physical menu in which all inherited
options remain legal.  Assume the two **cross options**

\[
 h_{p_1}\in N(g_0),\qquad h_{p_0}\in N(g_1)             \tag{2.2}
\]

are literal and preserve the complete fixed payload of their respective
roles.

### Theorem 2.1 (freeze-after-rectangle splice)

Replace the two selected closing assignments by

\[
 \pi'(g_0)=p_1,qquad \pi'(g_1)=p_0,                    \tag{2.3}
\]

and leave every other predecessor unchanged.  Then:

1. \(\pi'\) is one cycle on \(I_0\mathbin{\dot\cup}I_1\);
2. every owner and every declared named target is unchanged;
3. after restricting

   \[
                         N'(g_0)=\{h_{p_1}\},            \tag{2.4}
   \]

   while leaving \(g_1\) as the distinguished role, the parent is again a
   private-rooted Hamilton table; and
4. the parent private path has

   \[
               (|I_0|-1)+(|I_1|-1)+1
                 =|I_0|+|I_1|-1                         \tag{2.5}
   \]

   singleton-tail edges and zero cut charge.

The roles \(g_0,g_1\) may be interchanged in item 3, so either child port
may survive as the parent port.

#### Proof

Deleting the old closing arc of child \(\epsilon\) leaves a directed path
\(P_\epsilon\) from \(h_{g_\epsilon}\) to
\(h_{p_\epsilon}\).  With (2.3), the concatenation is

\[
 h_{g_1}\ P_1\ h_{p_1}
   \longrightarrow h_{g_0}\ P_0\ h_{p_0}
   \longrightarrow h_{g_1}.                             \tag{2.6}
\]

Hence \(\pi'\) is one cycle.  Membership (2.2) makes both crossed arcs
literal; payload constancy on each role list preserves every owner and
named target.

All inherited path roles were already private.  Restriction (2.4) makes
the first crossed role private as well.  The only unforced role is now
\(g_1\).  Removing its crossed arc from (2.6) leaves
\(P_1\), the first crossed arc, and \(P_0\) as one spanning path.  Its edge
count is (2.5), and Lemma 1.2 gives zero cut charge. \(\square\)

### Why freezing does not invalidate the construction

Before the switch, the two roles in (2.2) each have at least the old and
crossed physical options, so they are not private.  This is the atomic
singleton--rectangle incompatibility.  But after (2.3), the selected cycle
itself witnesses feasibility of the restricted table (2.4).  Restriction
cannot alter a payload which was constant on the old menu.  Thus privacy is
a valid **postselection contraction**, not a property falsely attributed
to the unfixed rectangle.  If a later Pascal embedding reopens the frozen
support, the zero-charge statement must be re-established; the explicit
selected Hamilton cycle remains a valid physical certificate regardless.

### Lemma 2.2 (atomic privacy is impossible)

If distinct tail states \(u,v\) and distinct roles \(i,j\) support the
four corners of a nondegenerate tail-exchange rectangle, then

\[
                    u,v\in\widehat N(i)\cap\widehat N(j). \tag{2.7}
\]

In particular neither role is physically singleton-tail.

#### Proof

The four rectangle corners are precisely the four memberships displayed in
(2.7).  Since \(u\ne v\), both physical lists have size at least two.
\(\square\)

Thus Theorem 2.1 is a compound operation: select the matching phase, then
freeze or contract.  It is not a claim that one atomic option is
simultaneously a free rectangle and a physical singleton socket.

### Corollary 2.3 (binary Pascal closure)

Consider a rooted binary hierarchy of leaf tables whose fixed payloads
partition the desired parent owner/target banks.  Suppose every leaf is
private-rooted and, at every internal node, the two exported closing ports
obey (2.2) in the parent alphabet.  Choose one child port to survive at
every node.  Then the root table has

* one owner/target-exact Hamilton predecessor cycle;
* one distinguished exported closing role; and
* a spanning path of singleton-tail roles with identically zero Hall
  charge.

Exactly one rectangle is used at every internal node.  Hence the family is
closed for arbitrarily many recursion levels.

#### Proof

Induct on the binary hierarchy and apply Theorem 2.1 at every internal
node.  The payload partition makes the owner/target union exact, and the
surviving port is the distinguished role required by the next node.
\(\square\)

This is a genuine same-parity induction step, but it is an interface
theorem: it does not prove that canonical Pascal children export compatible
ports.  If the depth changes between the two dimensions, the child states
must first be lifted to the parent trace order; all port equations below
are imposed after that lift.

## 3. The literal Boolean port record

For a depth-\(d\) role \(i\), write its fixed head as

\[
                         h_i=(A_{i,1},\ldots,A_{i,d}),  \tag{3.1}
\]

and put

\[
 \lambda_i=(A_{i,1},\ldots,A_{i,d-1}),\qquad
 P_i=T_i\setminus\bigcup_{s=1}^d A_{i,s}.              \tag{3.2}
\]

If predecessor token \(p\) has

\[
 h_p=(c_p,\ldots),\qquad
 \rho_p=(\text{last }d-1\text{ letters of }h_p),       \tag{3.3}
\]

then the literal predecessor identity is

\[
 h_p\in \widehat N(i)\qquad\Longleftrightarrow\qquad
 \rho_p=\lambda_i,qquad P_i\subseteq c_p\subseteq T_i. \tag{3.4}
\]

Thus a selected closing port exports

\[
             \mathfrak p(i,p)
                 =\bigl(\lambda_i;c_p\mid P_i,T_i\bigr). \tag{3.5}
\]

### Theorem 3.1 (exact port-comparator equation)

Two selected closing ports \((g_0,p_0)\), \((g_1,p_1)\) satisfy the cross
condition (2.2) if and only if

\[
 \lambda_{g_0}=\lambda_{g_1}=\rho_{p_0}=\rho_{p_1}     \tag{3.6}
\]

and

\[
 P_{g_0}\subseteq c_{p_1}\subseteq T_{g_0},\qquad
 P_{g_1}\subseteq c_{p_0}\subseteq T_{g_1}.            \tag{3.7}
\]

#### Proof

The two old selected assignments give
\(\rho_{p_\epsilon}=\lambda_{g_\epsilon}\).  Apply (3.4) to the two
crossed assignments.  Their rail equalities force the common value (3.6),
and their remaining conditions are exactly (3.7).  Conversely
(3.6)--(3.7) and (3.4) make both crossed assignments literal. \(\square\)

The common rail is an ordered word of actual Boolean blocks, not merely a
rank sequence.  The cap tests are actual containments, not degree bounds.

### Corollary 3.2 (sector-signature obstruction)

Let a Pascal split use a new coordinate \(z\).  If the two child port
families have different membership signatures

\[
 \bigl(1_{z\in A_{1}},\ldots,1_{z\in A_{d-1}}\bigr),    \tag{3.8}
\]

then no port from one family can form the rectangle (2.2) with a port from
the other.  Changing only the leading or terminal letter cannot repair the
failure: a portal must rethread at least one internal rail position.

#### Proof

Different signatures make the ordered words \(\lambda\) unequal, while
(3.6) is necessary.  The leading and terminal letters lie outside
\(\lambda\), so changing only those letters leaves the obstruction.
\(\square\)

This is the sharp boundary for a separated-sector Pascal lift.  It does not
rule out a mixed-spine portal or a larger alternating macro.

## 4. What SCD exactness supplies

At \(k=2m+1\), the protected SCD selector permits arbitrary depth-\(d\)
flags at any \(h\le m+1\) distinct roots while covering every named lower
target exactly once and leaving the protected suffixes unmarked.  Therefore
one binary splice may prescribe its two portal flags without any lower
target sidecar.

More generally, if selected portal suffix occurrences are required to stay
marked, the occurrence-labelled SCD theorem says that they extend exactly
when their named targets are pairwise distinct.  Hence the **static target
row** of one binary portal is unconditional.

This does not imply (3.6)--(3.7): the SCD construction does not choose the
predecessor tokens \(p_0,p_1\), does not attach the required owners to the
portal roles, and does not balance the literal rail.  The antichain-top SCD
owner lift also closes only the two-endpoint Middle Levels projection; its
independently filled age cells need not satisfy (3.4).

Accordingly the exact same-parity export state is

\[
 \boxed{
   (\text{exact payload partition},\ 
    \text{private spanning path},\ 
    g,p,\lambda_g,c_p,P_g,T_g).}                       \tag{4.1}
\]

A scalar statement that the child is Hamilton is insufficient, because it
does not retain an admissible closing port for its parent.

## 5. Why stationary rotor types do not close the port

The corrected pull clock supplies a stationary rational circulation of
rotor **types** and exact rank marginals.  Its symmetrization averages over
owners, core choices, private-label orders, and block placements.  The
record (3.5) is lost under every one of those projections.

There is a literal obstruction in every depth \(d\ge2\).  Choose distinct
nonempty sets \(X,Y\) of the same cardinality.  Let one one-role table have
the loop state

\[
                         h_X=(X,X,\ldots,X)             \tag{5.1}
\]

and owner \(X\), with empty marked payload; let the second be the analogous
loop on

\[
                         h_Y=(Y,Y,\ldots,Y).             \tag{5.2}
\]

Both tables have the same cell-rank and age type, are balanced, and are
private-rooted (their private path is empty).  But their exported rails are
\(X^{d-1}\) and \(Y^{d-1}\).  By Theorem 3.1 no cross rectangle exists.

Thus no induction theorem stated only in terms of the stationary type
histogram can imply even one binary private splice.  The missing datum is
literal ordered-spine alignment together with the two cap containments.

## 6. Sharp first canonical boundary

The independent note

`MATH_AUDIT_K_PRIVATE_SOCKET_PASCAL_RECURSION_AND_K5_TWO_CYCLE_BOUNDARY_20260802.md`

proves the following solver-free classification.

### Theorem 6.1 (strict all-high \(k=5,d=2\) boundary)

Every balanced owner-exact strict all-high depth-two flag table on five
coordinates is, up to relabelling, the regular tournament.  Its owner rows
force the predecessor cover

\[
                         C_5(+1)\mathbin{\dot\cup}C_5(+2). \tag{6.1}
\]

Every realized predecessor list is singleton.  Consequently:

1. the table has no Hamilton predecessor cycle;
2. its private edges do not span the ten state tokens; and
3. it has no nontrivial atomic rectangle on which Theorem 2.1 could start.

The positive private Hamilton base at \(k=3,d=1\) therefore does not lift
to \(k=5,d=2\) inside the strict all-high face.  A successful same-parity
recursion must change at least one of the following interface choices:

* export an open two-ended path instead of a closed child cycle;
* use a boundary-deficient or non-all-high role;
* use a compound matching-closed macro and freeze only its contracted
  socket; or
* reassign the static owner/target association.

This is a boundary of the strict face, not a no-go for nonflat triangular
tables or for the known finite optimum at \(k=5\).

## 7. Exact remaining constructive lemma

The lower recursive problem is reduced to the following literal statement.

> **Private closing-port Pascal lemma.**  At each same-parity Pascal node,
> choose the two child owner/target-exact tables and their surviving closing
> roles so that their exported records (3.5) satisfy (3.6)--(3.7), after
> any correction bank has been included as further leaves of the same
> binary hierarchy, and make the frozen support hereditary under the parent
> embedding (or contract the chosen rectangle to a literal private macro).

Theorem 2.1 then supplies the Hamilton cycle and zero-charge tree
automatically.  The SCD theorem removes the lower-target cost of a bounded
portal but does not prove the lemma.  The pull clock supplies the correct
fractional type masses but not the literal port records.  The \(k=5\)
boundary proves that the strict all-high Pascal face cannot satisfy it
without an open or compound portal.

This note concerns only the lower labelled rotor row.  It does not assert
that the frozen splice preserves:

1. arbitrary-width upper interval-union coverage;
2. residence or exterior crossing windows;
3. quotient voltage or an ambient opening; or
4. the terminal common-cap/compiler matching.

Those data must be included in the role payload before (2.2), or proved in
a separate guarded lifting theorem.

## 8. Proof audit

The permutation splice can be checked without enumeration.  Before the
switch there are two cycles and two removed arcs.  After (2.3), each old
predecessor token and each old head token still occurs once.  Formula (2.6)
is one cycle.  After freezing, exactly one of the
\(|I_0|+|I_1|\) roles remains nonprivate; the other
\(|I_0|+|I_1|-1\) selected arcs form the path (2.6) with its last arc
removed.  Hence every shore has escape charge zero.

The ordered-port equation was independently derived from the literal
predecessor identity in
`MATH_THEOREM_K_BOOLEAN_RAIL_INTERVAL_HALL_AND_COMPLETE_TRANSITION_EULER_FUSION_20260802.md`.
The atomic singleton--rectangle incompatibility and the complete
\(k=5,d=2\) boundary were independently derived in the audit cited in
Section 6.  No finite search or numerical evidence is used in this note.
