# Gain--Brauer boundary law and a private primitive-voltage tuner

Date: 2026-07-31  
Status: exact finite boundary algebra and conditional all-`m` sufficient
face; no all-`m` private-socket or transparent-gluing-tree existence claim

## 0. Verdict

Let \(A=\mathbb Z_h\).  On one fixed set \(B\) of formal socket
occurrences, the boundary gain-routing of an oriented path forest is
represented exactly by an \(A\)-gain-labelled fixed-point-free involution
\(P\).  If a toggle changes it to \(P'\), its complete fixed-socket
gain-routing transition is

\[
                         T(P,P')=P'P\in A^B\rtimes S_B.       \tag{0.1}
\]

For a sequence on the same labelled sockets and in one compatible gain
gauge these transitions telescope:

\[
 T(P_{k-1},P_k)\cdots T(P_0,P_1)=P_kP_0.             \tag{0.2}
\]

A standard hexagon matching replacement is the gain-labelled version of
two reciprocal three-cycles.  This classifies the local routing change, but
does not preserve a fixed connector closure: exterior paths can turn the
three-break into a merge or split of occurrence cycles.

When boundary occurrences are created, consumed, or identified, (0.1) is
not defined in one permutation group.  The exact replacement is gain--Brauer
stacking: pair boundary ports by internal paths, label every pair by its
oriented gain, stack compatible pairings, and extract the resulting external
pairing and every sealed cycle voltage.  On boundary width \(b\), its pure
path-pairing table has at most

\[
                 2^{O(b\log b+b\log h)}              \tag{0.3}
\]

entries.  This is finite for fixed \((b,h)\), not a dimension-independent
socket alphabet.

There is a positive conditional voltage face.  Suppose an already
one-cycle quotient closure has pairwise resource-disjoint private sockets
whose independent voltage-defect menus are \(G_1,\ldots,G_k\subseteq A\).
Put \(S=G_1+\cdots+G_k\).  For fixed inherited voltage \(v\), primitive
voltage is possible exactly when

\[
                         (v+S)\cap U_h\ne\varnothing,           \tag{0.4}
\]

where \(U_h=\{u:\gcd(u,h)=1\}\).  The weakest exact hypothesis which works
for every inherited \(v\) is

\[
                         \boxed{S+U_h=\mathbb Z_h}.              \tag{0.5}
\]

One private binary knob per prime divisor of \(h\), separated by CRT, is a
uniform sufficient construction.  This voltage theorem is conditional on
the one-cycle topology and on literal private resources.  It does not
construct the missing all-\(m\) Catalan gluing/socket face.

The recursive decoration coordinate has two different composition faces.
A **transparent microstep** preserves one already chosen decoration and is
governed by the exact six-port palette/boundary test of
`MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`.
A **repair macro** may have positive occurrence-matching deficiency at its
input and intermediate states; it is certified only end to end by a final
perfect occurrence matching and its common-core augmenting linkage.  Such a
macro must be treated atomically until its output decoration and every other
boundary coordinate have been re-established.  These two faces cannot be
interchanged merely because their underlying switches are local.

The unmodified standard private-triple family does not instantiate this
face beyond the positive `m=4` base.  The complete standard MMM census at
`m=5` has two Hamilton outputs, but each attains only 81 of 84 turn colours
on both shores and misses the lower period-three orbit
\(\{73,146,292\}\).  Palette repair, a nonstandard switch, or a different
base factor is therefore logically prior to the private socket/voltage
step.  A newly frozen synchronized packet of three vertex-disjoint
Hamilton-safe \(C_{10}\) switches now supplies that palette repair at
`m=5`: its audit proves a forced-port joint decoration, a leaf-peelable gap
forest, thirteen common-core augmenting paths, a forest trace, and the two
private **gap-owner** paths.  A separate literal endpoint audit of the final
repaired state reconstructs a 252-vertex, 210-edge Johnson path forest with
42 components and gives 42 Johnson connector edges whose union with the
forest is one 252-cycle.  Thus final-state socket topology is positive.
What is not supplied is transport of that named endpoint pairing and
connector system through the four-state glue cube, recursive parent
ownership of the physical sockets, or a compiler.  At the full repaired
output, however, the same colour-injective closure now has complete
upper/lower flag support at every depth, with 46 valid cuts.  The remaining
fixed-carrier obstruction is sharper: 31 internal `0-11-0` path runs make
depth-two residence impossible under every intact-path permutation,
reversal and socket choice.  An interior rethread is mandatory.  Moreover,
the ordinary trace-forest row must not be promoted to the stronger run row:
every cube state fails the strict-run guard, and the static two-label
aligned-one-edge face also fails.  Here the clean group has \(h=1\), so
voltage is vacuous after the one-cycle topology has been checked.

## 1. Gain permutations, involutions, and gauge

An \(A\)-gain permutation of a finite occurrence set \(B\) is

\[
       (\sigma,a):(x,g)\longmapsto(\sigma x,g+a_x),
       \qquad \sigma\in S_B,\ a\in A^B.              \tag{1.1}
\]

These maps form the wreath product \(W_A(B)=A^B\rtimes S_B\).  With maps
applied right to left,

\[
 (\sigma,a)(\tau,b)
   =(\sigma\tau,c),\qquad c_x=b_x+a_{\tau x}.        \tag{1.2}
\]

A gain pairing is an element \(P=(p,\lambda)\in W_A(B)\) such that

\[
 p^2=1,\quad p(x)\ne x,\quad
 \lambda_x+\lambda_{p(x)}=0.                         \tag{1.3}
\]

It records the internal path from \(x\) to \(p(x)\); reversal negates its
gain.  Two formal ports at one isolated physical vertex remain distinct and
are paired with gain zero.

Changing quotient representatives by a potential \(r:B\to A\) changes

\[
 \lambda_x\longmapsto
       \lambda_x+r_x-r_{p(x)}.                       \tag{1.4}
\]

Thus gain permutations are conjugated by a diagonal gauge map and closed
walk voltages are unchanged.  Numerical transition labels may be compared
only after both sides have been expressed in the same gauge.

## 2. Fixed-socket transition and closure extraction

### Theorem 2.1 (telescoping transition law)

For gain pairings \(P,P'\) on the same labelled occurrence set, define

\[
                           T(P,P')=P'P.               \tag{2.1}
\]

Its underlying permutation is \(p'p\), and its gain at \(x\) is

\[
                      t_x=\lambda_x+\lambda'_{p(x)}. \tag{2.2}
\]

For \(P_0,\ldots,P_k\) in one compatible gauge, (0.2) holds as an equality
of gain permutations.

#### Proof

Equation (2.2) is (1.2).  Every \(P_i\) is an involution, including its gain
labels.  Hence adjacent factors cancel:

\[
 (P_kP_{k-1})(P_{k-1}P_{k-2})\cdots(P_1P_0)=P_kP_0.
\]

Under one common gauge the two sides are conjugated equally.  If an
intermediate state is re-gauged independently, its explicit change-of-gauge
map must be inserted before cancellation. \(\square\)

Let \(M\) be a gain-labelled connector involution on the same ports.  The
alternating occurrence components of \(P\cup M\) are the paired orbits of

\[
                              \Theta=MP.              \tag{2.3}
\]

If \(O\) is one of the two oriented orbits belonging to a component, its
voltage is

\[
                V_O=\sum_{x\in O}
                  \bigl(\lambda_x+\mu_{p(x)}\bigr).  \tag{2.4}
\]

The companion orbit has voltage \(-V_O\).  The free \(A\)-development of
that quotient component has \(\gcd(h,V_O)\) physical components.  Therefore
the root accepts exactly when (2.3) has one occurrence component and its
voltage is primitive.

The transition \(P'P\) does not imply that \(MP'\) and \(MP\) have the same
cycle type.  It records exactly how to recompute the latter; it is not a
path-pair preservation theorem.

## 3. The local hexagon element

Index six cut ports by \(L=\{\ell_i\}\) and \(U=\{u_i\}\), with indices
modulo three.  Orient the old matching as

\[
       \kappa_0:\ell_i\longmapsto u_i
       \quad\hbox{with gain }\alpha_i,               \tag{3.1}
\]

and the new matching as

\[
       \kappa_1:\ell_i\longmapsto u_{i+1}
       \quad\hbox{with gain }\beta_i.                \tag{3.2}
\]

### Lemma 3.1 (gain-labelled three-break)

The relative element \(R=\kappa_1\kappa_0\) has the two underlying cycles

\[
          (u_0\ u_1\ u_2),\qquad
          (\ell_0\ \ell_2\ \ell_1).                 \tag{3.3}
\]

On \(U\), the step \(u_i\to u_{i+1}\) has gain

\[
                       \delta_i=\beta_i-\alpha_i,    \tag{3.4}
\]

and its three-step voltage is

\[
                  \Delta=\sum_i\beta_i-\sum_i\alpha_i.        \tag{3.5}
\]

The reciprocal \(L\)-cycle has voltage \(-\Delta\).

#### Proof

From \(u_i\), traverse the old edge backwards, of gain \(-\alpha_i\), then
the new edge forwards, of gain \(\beta_i\).  This gives (3.3)--(3.5).  The
calculation on \(L\) is the reverse. \(\square\)

At \(h=1\) this is a pure three-break.  In particular, the `m=3` and `m=4`
transparent examples in
`MATH_THEOREM_CATALAN_PRIVATE_SOCKET_CRT_TUNING_AND_M3_CONNECTOR_OBSTRUCTION_20260731.md`
have the displayed reciprocal three-cycles even though their literal socket
multiplicities agree.

If the exterior consists of three co-oriented through paths \(U\to L\), the
update lies in \(A^3\rtimes S_3\); when both closures are one cycle their
total voltages differ by \(\Delta\).  Without that through-orientation
hypothesis, exterior fragments may reverse and reconnect.  Their exact
component and voltage changes must be extracted by the stacking law below.

### Proposition 3.2 (complete `m=4` endpoint-transition census)

The displayed `m=4` decoration underlying item 2170 has 298 physical
Hamilton closures, 137 of them connector-colour-injective on both shores.
Among the 16 Hamilton-safe incidence-hexagon toggles at that cycle, however,
**none** preserves this displayed decoration.  Thus it is invalid to cross
the 298/137 closure fibre directly with the transparent-toggle rows.

There are six genuine nonempty common-decoration fibres, with 2,412
decoration--toggle incidences in total.  Omitting fixed points, the complete
cycle-type census of the external endpoint transition \(P'P\) is:

\[
\begin{array}{c|c|c|c|c}
H&(a,b,c)&\text{marked hex ports}&\text{common decorations}
  &\text{cycle types of }P'P\\ \hline
10&(0,2,4)&6&576&288\cdot3^4+288\cdot5^2\\
34&(2,3,4)&6&576&384\cdot3^2+192\cdot5^2\\
66&(0,3,4)&6&144&8\cdot3^2+64\cdot3^4+72\cdot5^2\\
20&(1,3,5)&0&144&144\cdot3^2\\
20&(3,5,6)&0&432&432\cdot3^2\\
96&(0,1,4)&6&540&2\cdot2^4+70\cdot2^2\,3^2+468\cdot3^4
\end{array}                                                   \tag{3.6}
\]

Here \(r^s\) means \(s\) nontrivial cycles of length \(r\).  The two
unmarked fibres change one alternating \(C_6\) of physical forest edges;
the four all-marked fibres change two disjoint alternating \(C_6\)'s.
No incidence has \(P'=P\).  The \(5^2\), \(2^4\), and \(2^2 3^2\) rows
show why the local reciprocal three-cycles of Lemma 3.1 cannot simply be
declared to be the external endpoint transition: retained path fragments
must be stacked first.

All these data have \(h=1\), so every audited voltage and voltage change is
zero.  They classify topology only; they provide no nontrivial-voltage
transport evidence.

On the comparable common-decoration fibre at
\(H=20,(a,b,c)=(1,3,5)\), the old and new forests have respectively 559
and 399 Hamilton connector sets.  Every one of the 559 old sets remains
literal-legal and socket-exact after the toggle; 191 remain Hamilton, and
25 of those remain connector-colour-injective on both shores.  The smallest
audited split is \(10+60\), while item 2170's displayed set gives
\(70\longrightarrow24+46\).  Hence transport is neither always false nor
automatic: the relative connector routing is an essential correlated state.

### Proposition 3.3 (smallest frozen topology obstruction)

At `m=2` there is no alternating incidence-hexagon transition.  At `m=3`
the transparent split in
`MATH_THEOREM_CATALAN_PRIVATE_SOCKET_CRT_TUNING_AND_M3_CONNECTOR_OBSTRUCTION_20260731.md`
has

\[
              P_1P_0=(11\ 35\ 49)(13\ 56\ 22).       \tag{3.7}
\]

One common legal connector set changes a physical 20-cycle into cycles of
orders 9 and 11.  Thus `m=3` is the smallest frozen transparent
connector-transport obstruction; `m=4` is only the first with both
middle-level factors Hamiltonian.

## 4. Gain--Brauer stacking when the boundary changes

Assume the no-hidden-reopening convention: every physical occurrence or
literal resource which a later operation may touch is exposed on the named
boundary or in the visible resource footprint.

A path-fragment signature on a named boundary \(B\) consists of:

1. a pairing \(\tau\) of the boundary occurrences joined by internal paths;
2. an antisymmetric oriented gain on every pair; and
3. the voltage, modulo reversal, of every sealed internal cycle; and
4. the use or residual capacity of every literal edge orbit, colour, or
   private resource which an allowed exterior continuation can also see.

For Hamilton recursion a sealed proper cycle is immediately rejecting, so
the third field is normally only used at the root.

To glue signatures on \(B_0\sqcup I_L\) and \(I_R\sqcup B_1\), join each
declared pair \((i_L,i_R)\) by its interface gain.  The resulting degree-at-
most-two graph is a disjoint union of paths and cycles.  Pair the endpoints
in \(B_0\sqcup B_1\), give each resulting path the signed sum of its edge
gains, and record or reject every cycle.  Call this partial product

\[
                              \Sigma_2\odot_I\Sigma_1.            \tag{4.1}
\]

### Theorem 4.1 (exact associative boundary law)

Gain--Brauer stacking is associative whenever the same named interface
occurrences and gauges are used.  Two partial path systems with the same
full signature, including the visible literal-resource footprint, are
interchangeable under every allowed exterior continuation using those
occurrences.  At the root, one sealed cycle of primitive voltage is exactly
the clean-\(A\) Hamilton acceptance condition.

#### Proof

Stack all fragment and interface edges before suppressing degree-two
vertices.  Its connected components, their external endpoints, and their
signed gain sums do not depend on parenthesization.  An exterior continuation
sees an interior path only through these two endpoints and its transport
gain; a sealed cycle can never be re-opened.  Visible resource uses compose
by addition followed by the declared capacity test, also independently of
parenthesization.  The final assertion is the free cyclic voltage-cover
theorem. \(\square\)

### Corollary 4.2 (the exact group-valued through face)

Suppose a boundary is split into equally sized ordered shores
\(L=\{L_i\}_{i=1}^s\) and \(R=\{R_i\}_{i=1}^s\), and every internal path
is a through strand from one \(L_i\) to one \(R_j\).  Its signature is then

\[
             (\sigma,g)\in A^s\rtimes S_s,
             \qquad L_i\longmapsto R_{\sigma(i)}
             \text{ with gain }g_i.                 \tag{4.2}
\]

If a second block has state \((\tau,k)\), serial gluing has the exact law

\[
       (\tau,k)\circ(\sigma,g)
       =\bigl(\tau\sigma,(g_i+k_{\sigma(i)})_{i=1}^s\bigr). \tag{4.3}
\]

Thus this face is the finite wreath group \(A^s\rtimes S_s\), of order
\(h^s s!\), and a tree of through blocks composes by the same associative
law.  A cap, cup, sealed internal cycle, or change in the live boundary
leaves this group face and must be handled by Theorem 4.1.  In particular,
the factorial routing lower bound is not removed; it is represented
explicitly by the \(S_s\) factor.

For \(b=|B|\), the number of perfect gain pairings is

\[
                    (b-1)!!\,h^{b/2}                 \tag{4.4}
\]

when \(b\) is even.  Allowing unpaired ports, before assigning any finite
unused/demand type to them, gives exactly

\[
 \sum_{j=0}^{\lfloor b/2\rfloor}
       \frac{b!}{(b-2j)!2^j j!}\,h^j
       =2^{O(b\log b+b\log h)}.                      \tag{4.5}
\]

Finite degree/demand flags add only a constant-to-the-\(b\) factor.  Literal
edge-orbit, colour, and private-resource capacities remain separate
coordinates; no bound independent of the chosen exterior catalogue is
asserted for that resource ledger.

This upper bound is consistent with the \(n!\) completion-distinguishable
routing states in
`MATH_THEOREM_AD_CATALAN_LEAF_RUN_SOCKET_BOUNDARY_STATE_AND_ROUTING_OBSTRUCTION_20260731.md`:
that theorem lets the live socket boundary grow with \(n\).  Thus (4.5)
does not provide a dimension-independent alphabet.  It also does not replace
item 2171's gap-forest partition or item 2169's global linkage signature.

## 4A. Transparent microsteps and debt-carrying macro routers

Let \(F\) be a middle-levels factor.  Write \({\cal H}(F)\) for its
augmented occurrence graph; perfect matchings of \({\cal H}(F)\) encode
joint alternating decorations.  A fixed choice of marked occurrences
\(D=(D_A,D_B)\) is a separate witness/constraint on such a matching.

### Theorem 4A.1 (exact transparent microstep)

Assume \(D\) is a decoration of \(F\).  Suppose one standard incidence
hexagon replaces its old three-edge matching in \(F\) by the complementary
three-edge matching, producing \(F'\).  The same marked occurrences \(D\)
form a decoration of \(F'\) if and only if:

1. the selected local turn-colour multisets before and after the switch are
   equal separately on the lower and upper shores; and
2. after deleting the old matching, orienting the retained fragments as
   they occur in \(F'\), and discarding fragments with no mark, the last
   marked shore type of each fragment is opposite the first marked shore
   type of the next fragment, separately around every new factor cycle.

If the input gap--colour graph is a forest with its displayed perfect
matching, the same decoration remains leaf-peelable exactly when, after
deleting changed old gap edges and contracting the retained forest, the
changed new gap edges form a loopless acyclic attachment multigraph.

#### Proof

Only the six hexagon neighbour pairs change.  Hence global turn-colour
bijection is preserved exactly when the two local multisets are restored.
Alternation is already valid inside every retained fragment, including
after reversal, so it fails only at a new seam; the boundary types give the
necessary and sufficient seam test.  After the decoration is fixed, the
gap identity is \(\Gamma'=(\Gamma-D_0)+S_0\).  Since
\(\Gamma-D_0\) is a forest, adding \(S_0\) preserves acyclicity exactly
under the contracted loopless-forest test.  These are Theorems 2.1 and 2.3
of the cited authoritative note. \(\square\)

This theorem preserves the decoration coordinate only.  It does not say
that the physical endpoint pairing is fixed.  The `m=3` split
\(20\to9+11\) and the 2,412 comparable `m=4` transitions in Section 3
show that a transparent microstep must still update its gain--Brauer path
signature and literal resource ledger.

### Theorem 4A.2 (atomic repair-macro rule)

Consider a literal packet

\[
             F_0\longrightarrow F_1\longrightarrow\cdots
             \longrightarrow F_t                                      \tag{4A.1}
\]

of physically legal switches on a named footprint.  The intermediate
graphs \({\cal H}(F_i)\) may have positive deficiencies.  Let both shores
have order \(n\), and express \({\cal H}(F_0)\) and \({\cal H}(F_t)\) on
the same canonically labelled balanced occurrence banks.  Put

\[
 K={\cal H}(F_0)\cap{\cal H}(F_t),
 \qquad |N|=n-r                                                   \tag{4A.2}
\]

for a maximum matching \(N\) of the common core, and let \(M_t\) be a
perfect matching of \({\cal H}(F_t)\) realizing every prescribed marked
occurrence/private-collar constraint in the chosen occurrence encoding.
Then
\(N\mathbin\triangle M_t\) consists of exactly \(r\) vertex-disjoint
\(N\)-augmenting paths together with alternating cycles.  Conversely, any
family of \(r\) vertex-disjoint \(N\)-alternating augmenting paths in
\({\cal H}(F_t)\) which joins the full unmatched left bank of \(N\) to its
full unmatched right bank augments \(N\) to a perfect final matching.  When
collar marks are prescribed, the resulting matching must additionally be
checked against those marked-occurrence constraints.

The packet certificate retains the labelled augmenting paths and their
terminal identities, not only the integer \(r\); those paths may traverse
the whole final augmented graph, not merely the common core.  Assume in
addition that the output state explicitly records and passes its gap/trace,
physical path, gain--Brauer endpoint, socket, guard and literal capacity
rows.  If every resource which a later operation may touch is
either exposed on the named boundary or excluded by a private-footprint
condition, then (4A.1) is one exact atomic boundary transition.  It may be
followed on the fixed-decoration private face by a transparent gluing tree
when every later glue is transparent for the **output** decoration, passes
the required gap and trace rows, and composes with the output
gain--Brauer/socket signature.  This is a sufficient exact composition
test, not a claim that no later redecorating macro could work outside that
face.

#### Proof

Because \(N\subseteq K\subseteq{\cal H}(F_t)\) and \(M_t\) is
perfect, every path component of their symmetric difference begins and ends
at vertices unmatched by \(N\).  There are \(r\) unmatched vertices on
each shore, so there are exactly \(r\) disjoint augmenting paths; toggling
them gives a perfect matching.  The converse is ordinary Berge
augmentation.  The remaining coordinates compose by Theorem 4.1 under the
no-hidden-reopening hypothesis.  After the macro boundary, Theorem 4A.1
propagates the fixed output decoration through each transparent glue, while
the gap, trace and gain--Brauer tests propagate their separate coordinates.
No claim is made at an intermediate \(F_i\), where the required decoration
may not exist. \(\square\)

Thus Theorem 4A.2 does not license commuting a debt-carrying packet through
an arbitrary gluing tree or decomposing it into transparent microsteps; in
general either operation can fail.  To certify an interleaving exterior
operation one must expose the full intermediate feasible relation, including
its linkage terminals, path pairing and resource use.

### Corollary 4A.3 (the audited `m=4`/`m=5` boundary)

For the authoritative repaired `ML(7)` fixture there are 31 alternating
hexagons, 16 Hamilton outputs and 10 decorable outputs.  Exactly six of the
16 have a nonempty common-fixed-decoration fibre; the other four decorable
outputs require new representatives and six are undecorable.  The specific
one-hex repair of item 2153 starts from a nondecorable cycle, so it is a
one-switch redecorating repair on the macro side, not a transparent transfer
of a pre-existing decoration.  Its frozen artifact certifies the final
decoration directly; no separate common-core linkage certificate for that
one-switch repair is asserted here.  Across all decorations, the six genuine
transparent rows have 2,412 common-decoration incidences.

At `m=5`, the synchronized three-\(C_{10}\) packet has the stage triples

\[
 (3,3,3)\longrightarrow(2,2,2)\longrightarrow(1,1,1)
 \longrightarrow(0,0,0),                                          \tag{4A.3}
\]

where the coordinates are lower-palette deficit, upper-palette deficit and
joint occurrence-matching deficiency.  It is therefore a repair macro, not
three transparent microsteps.  Its
source/final common core has deficiency 13 and the frozen certificate gives
13 disjoint augmenting paths.  Only after the final decoration is installed
are the two standard private glues audited on their four-state cube.  Their
gap forest and ordinary binary trace pass, while the strict-run row and the
static two-label aligned-one-edge face fail; final physical socket closure
passes only at the separately audited output state.  This is exactly the
scope distinction required by Theorems 4A.1--4A.2.

The final full two-glue closure has since been replayed through the entire
flag tower: 46 cuts preserve all ranks \(5\pm q\), \(q=1,\ldots,5\), and
39 are connector cuts leaving the 42 paths intact.  This is not residence.
Those path interiors contain 31 bounded length-two positive runs, so every
intact-path chronology fails the necessary \(d=2\) run condition.  The
central macro therefore returns an all-depth physical base but still needs
an interior rethread before the lower compiler.

## 4B. Interior rethreads and algebraically forced reachability

The exact local law is frozen in
`MATH_THEOREM_CATALAN_INTERIOR_RETHREAD_GAIN_BRAUER_ACTUATOR_20260731.md`.
Besides the path pairing/gains and literal resources, a rethread collar must
carry separate lower/upper palette ledgers, affected all-depth witness debt,
the coordinate run automaton and directed boundary reachability.  An old
target whose every witness meets the collar must receive a new literal
window; all other old targets retain an unaffected witness.  A two-terminal
atom \(T\to H\) may be contracted exactly when the residual is acyclic and
has no path \(H\leadsto T\).

This reachability row is forced already by the Pascal determinant split.
Two complete canonical parameter-\((m-1)\) parent copies force
\(\operatorname{Cat}_m\) cross edges and hence

\[
 |E|-|V|=\operatorname{Cat}_m-2\operatorname{Cat}_{m-1}
 =\frac{2(m-2)}{m+1}\operatorname{Cat}_{m-1}\ge0,                 \tag{4B.1}
\]

so a cycle is unavoidable.  This excludes scalar preservation of both full
canonical parents, not every Pascal braid.  Any literal two-full-parent
Pascal induction on these canonical rails must instead use boundary-deficient
rails and carry reachability/socket state.

For the authenticated `m=5` forest, every resident final word must omit an
old adjacency from each of 31 three-edge defect collars; their exact old-edge
transversal number is 29.  One omission may be the final opening cut, so the
unconditional rethread-deletion bound is 28, rising to 29 for a connector or
nondefect opening.  A complete fixed-connector census of single connected palette cycles
\(C_4,C_6,C_8,C_{10}\) finds no pairing-private all-depth move which improves
the short-run score.  Since full signature privacy implies pairing privacy,
this also excludes a fully private improver in that class.  One nonprivate
\(C_6\) braid does preserve both palettes,
the fixed colour-injective connectors and 47 all-depth cuts while improving
the short-run histogram from \(1^{13}2^{61}\) to \(1^{13}2^{58}\).  Its
path-pairing transition has type \(3^2\), so the first positive actuator
already requires explicit gain--Brauer transport.

The uniform target is therefore a controlled-debt packet of bounded-port
circuits, followed by an ordered fixed-decoration transparent
leaf-peelable gluing list and an interior rethread.  Packet cardinality may
grow.  Bounded live boundary and exposed linkage debt at each composition
cut are required interface hypotheses, not consequences of bounded circuit
arity.

Item 2188 now proves that a larger 119-partner matching rethread can remove
all internal `m=5` residence defects while retaining both immediate
palettes.  Endpoint-only joining of its 42 fixed paths is nevertheless
solver-free impossible: one length-eight component has pair-safe degree zero
at both sockets, and its two forced short-run collars are edge-disjoint in
every connected closure.  A raw colour-injective one-cycle connector
matching exists, so this new obstruction is specifically the run/socket
correlation, not marginal topology or connector palettes.  The next physical
macro must therefore change an interior socket trace as well as carry the
exported gain--Brauer state.  Here again `h=1`, so this finite result supplies
no nontrivial-voltage evidence.

## 5. Conditional private-socket primitive-voltage face

Start with one directed quotient occurrence cycle of voltage \(v\).  At a
private socket replace a directed seam \(pq\) by a directed, internally
disjoint detour \(pQq\) with the same endpoint occurrences.  Its voltage
defect is

\[
                     d=g(pQq)-g(pq)\in A.            \tag{5.1}
\]

For a legal menu let \(G_i\) be the exact set of its defects.  Assume
explicitly that the menus are jointly independently selectable, that their
literal resource blocks are disjoint, and that every nested replacement
preserves all descendant sockets and their menus.  Replacing an edge of a
directed cycle by a directed path preserves the one-cycle topology.
Induction over the resulting detour tree therefore gives the exact reachable
voltage set

\[
                         v+S,\qquad S=G_1+\cdots+G_k. \tag{5.2}
\]

### Theorem 5.1 (weakest exact gain-set hypothesis)

Within this private-socket face, a primitive lift exists for the fixed base
\(v\) exactly under (0.4).  It exists for every possible inherited base
voltage exactly under (0.5).

#### Proof

Equation (5.2) proves the fixed-base assertion.  Universally,
\(v+s=u\in U_h\) is equivalent to \(v=u-s\), so the condition is
\(U_h-S=A\).  Negate both sides and use \(-U_h=U_h\) to obtain the
equivalent condition \(S+U_h=A\). \(\square\)

Only residues modulo \(\operatorname{rad}(h)\) matter for this primitive
test.  For an explicit universal tuner, for every prime \(p\mid h\) choose
\(\delta_p\in\mathbb Z_h\) with

\[
 \delta_p\not\equiv0\pmod p,
 \qquad \delta_p\equiv0\pmod q
       \quad(q\mid h,\ q\text{ prime},\ q\ne p),                \tag{5.3}
\]

and provide one private menu \(\{0,\delta_p\}\).  CRT supplies (5.3).
Each knob alone changes only its designated prime coordinate; choose it
exactly when the current total is zero there.  The final total is nonzero
modulo every prime dividing \(h\), hence primitive.

This construction is genuinely collective.  For the clean group
\(h=35\), compatible with \(m=18\), take

\[
             G_5=\{0,21\},\qquad G_7=\{0,15\}.       \tag{5.4}
\]

Neither menu contains a primitive nonzero defect, but their sumset contains
\(21+15=1\pmod{35}\), and the two CRT-separated knobs are a universal
tuner.  The exact, generally weaker condition remains (0.5), not the
presence of a primitive choice in one menu.

### Corollary 5.2 (conditional all-\(m\) face)

For each \(m\), suppose independently that the joint decoration,
gap-forest, common-core linkage, physical path, literal capacity, and
one-cycle socket coordinates admit a common witness, and that its clean
\(H_m\cong\mathbb Z_{h_m}\) closure has a private detour tree satisfying
(0.4), or the universal hypothesis (0.5).  Then that witness has a
primitive-voltage physical Hamilton lift.

This is an all-\(m\) implication, not an existence theorem for its
hypotheses.

## 6. Scope

1. Socket multiplicity fixes \(B\), not \(P\); it does not preserve
   occurrence connectivity.
2. Voltage cannot join two quotient occurrence cycles.  Apply Section 5
   only after the gain--Brauer root has one cycle.
3. If menus share a resource, change endpoints, alter path pairing, or are
   not complete free-\(H\) orbits, their reachable set need not be the
   Minkowski sum (5.2).
4. Full \(\mathbb Z_h\) labels are required for exact developed component
   counts.  Reduction modulo \(\operatorname{rad}(h)\) is safe only for the
   yes/no primitive test.
5. The gain--Brauer coordinate is alongside, not instead of, the
   gap-forest, linkage, run, guard, and literal-capacity coordinates.  A
   recursive node carries their correlated feasible relation, not the
   Cartesian product of independently feasible projections.
6. The 298 symmetry-broken `m=4` closures have \(h=1\); they calibrate
   endpoint topology but provide no nontrivial voltage evidence.
7. The standard MMM private-triple induction is already false at `m=5`:
   both Hamilton outputs attain only 81 of 84 turn colours on each shore
   and miss the lower orbit \(\{73,146,292\}\).  Therefore Sections 4--5
   apply only after a palette repair, a nonstandard switch, or a different
   base factor supplies the required global decoration and one-cycle socket
   face.  The three-\(C_{10}\) packet in
   `MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`
   now supplies the palette/gap/linkage/trace part of this prerequisite at
   `m=5`.  The companion endpoint audit supplies a physical 42-path forest
   and one literal 42-connector closure for the final repaired state.  It
   does **not** transport that pairing through the glue cube or establish
   recursive private ownership.  Final full-state all-depth support is now
   proved, but it is not transported to intermediate packet/glue states.
   Residence and the lower compiler are impossible on the intact-path face:
   the final word must omit at least one edge in each defect collar, with
   exact old-edge hitting number 29; after crediting one possible opening
   cut, a rethread must delete at least 28 old forest edges.  Independently,
   every cube state
   fails the strict-run guard and the fixed two-label aligned-one-edge face
   fails, although either singleton glue is an aligned salvage.

## 7. Audit

Run

```text
python3 scratch/audit_catalan_gain_brauer_private_voltage_tuner_20260731.py
```

The audit checks the gain-wreath multiplication, involution and telescoping
laws, gauge covariance, the complete hexagon formula over small cyclic
groups, the pairing-state counts, the exact fixed/universal gain-set tests,
and the CRT-separated construction.  The exact `m=4` transition table is
replayed by
`scratch/audit_catalan_m4_transparent_hex_closure_transport_census_20260731.py`;
the fixed-decoration transparent criterion, leaf-peelable contraction test
and `31/16/10/6` `ML(7)` census used in Section 4A are replayed by
`scratch/audit_decorable_ml7_gluing_20260731.py`;
the smallest `m=3` obstruction and the stronger CRT calibrations are replayed
by
`scratch/audit_catalan_private_socket_crt_tuning_m3_connector_obstruction_20260731.py`;
and the `m=5` standard-family palette failure is replayed by
`scratch/audit_catalan_private_triple_standard_m5_refutation_20260731.py`.
The repaired three-\(C_{10}\) palette/gap/linkage/trace state is replayed by
`scratch/audit_catalan_standard_m5_three_c10_private_repair_20260731.py`.
Its final-state physical path forest and connector cycle are independently
replayed by
`scratch/audit_catalan_m5_three_c10_endpoint_socket_20260731.py`.  The exact
coordinate separation and the component-alignment correction are recorded
in
`MATH_AUDIT_CATALAN_M5_THREE_C10_GAIN_SOCKET_COMPATIBILITY_20260731.md`.
The independent fail-closed strict-run/aligned/linkage replay is
`scratch/threadD_audit_m5_three_c10_state_compatibility_20260731.py`.
The final all-depth/residence separation is replayed by
`scratch/audit_thread_a_m5_three_c10_downstream_state_20260731.py`; the
Pascal-sector and contraction claims by
`scratch/audit_catalan_pascal_sector_determinant_20260731.py`; and the
interior-rethread hitting/census claims by
`scratch/audit_catalan_m5_interior_rethread_actuator_20260731.py`.  The
item-2188 pair-safe socket obstruction and its raw colour-injective topology
control are replayed by
`scratch/audit_catalan_m5_residence_clean_socket_dead_component_h2_20260731.py`.
