# Fano seven-router closure: the transported-petal chronology obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

The permutation identity

\[
 (135)^{-1}(245)(236)(034)(146)(056)(012)=1          \tag{0.1}
\]

is algebraically valid but has no realization as a serial composition of
the literal one-petal paired-\(C_6\) moving-exterior routers from
MATH_THEOREM_PAIRED_C6_STAR_TO_STAR_PACKET_20260726.md.

The obstruction is chronology, not monodromy. In the direct star
interface, every active root removes its current petal and inserts the
petal carrying its transported label. If that root is active again, the
second router removes the petal inserted by the first. A Johnson
geodesic cannot contain an insertion followed by a deletion of the same
coordinate.

This gives an order-independent theorem:

\[
\boxed{
\begin{gathered}
\text{the transported root supports of literal direct one-petal routers
must be pairwise disjoint;}\\
\text{hence no nonempty identity word of such routers is globally
geodesic.}
\end{gathered}}                                        \tag{0.2}
\]

Seven Fano lines have \(21\) transported root incidences on seven roots,
so no ordering or choice of orientations can pass this criterion. Under
the chronology in (0.1), every root is active exactly three times and
the failure occurs on every row.

Therefore there is no literal completed factor obtained from this direct
serial one-petal Fano composition on which an all-depth carrier or
completion spill can be evaluated. The local raw carrier is an open-path
quantity and cannot be inserted into the weighted-quota hinge. The only
presently known literal closure of one paired packet is the
all-depth-neutral three-wreath trade; it does not retain a useful carrier.

This theorem does not rule out a genuinely new multipetal or
row-dependent-exterior Fano packet. Such a packet would need new
cross-line re-encoding collars and is not obtained merely by ordering
and orienting the seven given routers.

## 1. Transported supports

Let \(\Omega\) be a finite set of root labels. At stage \(t\), let
\(\rho_t\) be an oriented \(3\)-cycle on the current one-petal star
labels. Put

\[
 \pi_0=1,\qquad \pi_t=\rho_t\pi_{t-1}.                \tag{1.1}
\]

Thus an original root \(x\) carries current label
\(\pi_{t-1}(x)\) immediately before stage \(t\). The roots physically
active at that stage, pulled back to the initial frame, are

\[
 A_t=\pi_{t-1}^{-1}(\operatorname {supp}\rho_t).      \tag{1.2}
\]

In the direct paired-\(C_6\) interface, the row-varying input coordinate
of root \(x\) is

\[
                         a_{\pi_{t-1}(x)}.             \tag{1.3}
\]

If \(x\in A_t\), the **net exposed-petal update across the packet** is

\[
 a_{\pi_{t-1}(x)}
        \longmapsto a_{\pi_t(x)}.                     \tag{1.4}
\]

The coordinate on the right is inserted at the first \(C_6\) exchange;
the terminal \(C_6\) removes the coordinate on the left and inserts the
common hub \(k'\). Thus the net exposed-petal update is (1.4). Since
\(\rho_t\) is a \(3\)-cycle, the two petals are distinct.

### Theorem 1.1 (transported-support chronology criterion)

Assume every direct connector literally preserves the exposed physical
petal on every transported strand, including a strand active at the next
stage; equivalently, from one active occurrence until the next there is
no petal re-encoding. In any serial composition of literal direct
one-petal paired-\(C_6\) routers contained in global Johnson geodesics,
the sets

\[
                         A_1,A_2,\ldots,A_s             \tag{1.5}
\]

are pairwise disjoint.

If, in addition, \(\pi_s=1\), then every \(A_t\) is empty. Hence no
nonempty identity word of direct one-petal routers is physically
geodesic.

#### Proof

Suppose \(x\in A_r\cap A_t\) with \(r<t\), and take \(t\) to be the
first active stage for \(x\) after \(r\). At stage \(r\), equation (1.4)
inserts \(a_{\pi_r(x)}\). At every intermediate stage \(j\), the root is
inactive, so

\[
                         \pi_j(x)=\pi_r(x).            \tag{1.6}
\]

The direct-connector hypothesis preserves the exposed physical petal
during those inactive stages. Consequently its one-petal input at stage
\(t\) is the same coordinate \(a_{\pi_r(x)}\). Equation (1.4) removes
it. The row has therefore inserted and later removed one coordinate.

Along a Johnson geodesic, every removed coordinate belongs to the initial
state and every inserted coordinate belongs to the final state. No
coordinate can be inserted and subsequently removed. Thus no such
\(x\) exists, proving pairwise disjointness.

Now assume \(\pi_s=1\). If \(x\) belongs to exactly one \(A_t\), its label
changes nontrivially at that stage and is fixed at every later stage.
Hence \(\pi_s(x)\ne x\), a contradiction. Pairwise disjointness says no
root can be active twice, so no root can be active at all. Every support
is empty. \(\square\)

### Corollary 1.2 (capacity of a direct one-petal bank)

On \(N\) roots, at most \(\lfloor N/3\rfloor\) nonidentity direct
one-petal routers can occur in one globally geodesic serial composition.
If the final monodromy is the identity, the maximum is zero.

For \(N=7\), at most two nonidentity stages are possible before closure is
imposed.

#### Proof

Each \(A_t\) has size three and the sets are disjoint by Theorem 1.1.
The identity assertion is its second conclusion. \(\square\)

## 2. The displayed Fano identity

Use the usual rightmost-first chronology in (0.1):

\[
\begin{aligned}
 \rho_1&=(012),&
 \rho_2&=(056),&
 \rho_3&=(146),\\
 \rho_4&=(034),&
 \rho_5&=(236),&
 \rho_6&=(245),&
 \rho_7&=(153).
\end{aligned}                                         \tag{2.1}
\]

The pulled-back active-root triples from (1.2) are

\[
\boxed{
 012,\quad256,\quad045,\quad036,\quad146,\quad234,\quad135.}         \tag{2.2}
\]

Every root occurs in exactly three triples. Its transported label
trajectory at its active stages is

\[
\begin{array}{c|c}
0&0\longmapsto1\longmapsto4\longmapsto0\\
1&1\longmapsto2\longmapsto3\longmapsto1\\
2&2\longmapsto0\longmapsto5\longmapsto2\\
3&3\longmapsto4\longmapsto5\longmapsto3\\
4&4\longmapsto6\longmapsto2\longmapsto4\\
5&5\longmapsto6\longmapsto1\longmapsto5\\
6&6\longmapsto0\longmapsto3\longmapsto6 .
\end{array}                                           \tag{2.3}
\]

Thus every row has the forbidden membership chronology

\[
 1\longrightarrow0
 \quad\text{for the petal inserted at its first active router,}       \tag{2.4}
\]

and its third active router also reinserts the petal removed at the
first. Both facts violate global geodesicity.

#### Verification

Equation (2.2) follows successively from
\(A_t=\pi_{t-1}^{-1}(\operatorname {supp}\rho_t)\).
Reading the image of each root only at the three stages in which it lies
in \(A_t\) gives (2.3). The last entry in every row is its initial label,
which also verifies \(\pi_7=1\). \(\square\)

The explicit trace is an audit of (0.1), not a special obstruction tied
to this ordering. Theorem 1.1 rules out every ordering and every choice
of orientations whose product is the identity.

## 3. Independent parallel placement also fails exact ownership

One might try to avoid chronology by placing several Fano routers in one
phase. This is impossible for the direct clean-\(C_6\) interface.

### Proposition 3.1 (same-side selected-edge obstruction)

Two distinct same-phase outgoing clean routers, or two distinct
same-phase incoming clean routers, which share a root, use the same
selected incidence edge there, and prescribe distinct replacement
incidences cannot be toggled independently with an exact \(X/Y\)
incidence ledger.

#### Proof

The initial matching contains one copy of the shared selected edge.
The two independent signed toggles subtract two copies and add two
different alternatives. The resulting edge coefficient or lower-state
degree is invalid. Thus the selected-edge ownership ledger fails before
collars are considered. \(\square\)

For independent direct Fano toggles, color a router by whether it uses
the incoming or outgoing selected side. At every Fano point three lines
meet, so two have the same color and use the same selected edge there.
Linearity gives different remaining line labels and hence distinct
replacement incidences. Proposition 3.1 rejects that pair.

This statement does not classify a new joint alternating circuit formed
by overlapping cycles. Such a circuit would be a different packet with
its own complete degree and collar proof. Combining independent
same-phase toggles with direct serial stages does not evade Theorem 1.1.

## 4. Complete collar and carrier audit

Each individual paired-\(C_6\) packet has the exact local lower, upper,
and three-collar ledgers

\[
 \mathcal X_{\rm loc}=\{S_i,T_i,A_i,B_i:i\in\mathbb Z_3\},
 \qquad
 \mathcal Y_{\rm loc}=\{U_i,V_i,Z_i:i\in\mathbb Z_3\}.               \tag{4.1}
\]

Those ledgers cannot simply be added over the seven Fano lines.

1. At one phase, Proposition 3.1 gives a repeated selected-edge demand.
2. At distinct phases, Theorem 1.1 gives an inserted-then-removed petal
   on the first repeated root.

Hence the proposed direct seven-line object never becomes a family of literal
root-to-complement wreath rows. In particular, the complete physical
histograms

\[
                         \mu_q^{\rm Fano}              \tag{4.2}
\]

do not exist as final exact-factor histograms in the category required by
the serial weighted-quota theorem. Formal open-stage tensors can be
written, but without literal connectors they are noncanonical and cannot
enter Car+Spill. Applying a mobile-quota hinge to their formal sum would
be invalid.

The known aligned cyclic completion of one paired packet does not rescue
the proposal. That completion closes each affected row immediately and
satisfies

\[
                         \Delta_q=0
 \qquad(0\le q\le m-1)                                \tag{4.3}
\]

after its three rows are summed. It removes the open Fano label action
instead of transporting it to the next line. Wherever independent copies
of that completed trade are legal, they have zero weighted-quota effect.
Overlapping seven such global completions on the Fano supports would be a
new interacting construction, not a composition theorem.

Therefore neither branch retains a nonzero useful shallow carrier:

\[
\boxed{
\begin{array}{c|c|c}
\text{branch}&\text{literal global rows}&\text{final carrier}\\ \hline
\text{open Fano identity}&\text{no}&\text{not an exact-factor carrier}\\
\text{known aligned closure}&\text{yes}&0 .
\end{array}}                                          \tag{4.4}
\]

No completion spill can repair the open branch merely by adding disjoint
rows: the already selected strands are not literal rooted rows. A
positive-density bank of such open blocks would require
\(\Theta(\operatorname {Cat}_m)\) roots to participate in a new global
reconnection, rather than the
\(o(\operatorname {Cat}_m/\sqrt m)\) completion permitted by the clean
serial theorem.

## 5. Exact scope and minimum escape

The obstruction uses the direct one-petal star interface:

\[
 \text{current label }y
 \quad\longleftrightarrow\quad
 \text{unique row-varying coordinate }a_y.            \tag{5.1}
\]

Assigning a fresh petal system to every Fano line does not by itself give
a composition. Between two lines sharing a root, one would need a
literal connector which re-encodes the transported label into the fresh
petal system. If it removes the previously inserted petal, Theorem 1.1
still applies. If it stores that petal and exposes a different one, the
next three-row boundary has at least two row-varying coordinates unless
additional row-dependent exterior transfers make the stored coordinate
common. Those transfers require new states, upper owners, and crossing
collars not present in the seven paired packets.

Thus a genuine escape must prove one joint theorem:

> **Multipetal Fano packet.** Construct seven globally ordered line
> routers together with re-encoding connectors such that every row
> coordinate has a monotone membership history, every active line has one
> common-core star boundary, all lower/upper/crossing-collar resources
> have one owner, the transported product is identity, and the final
> collision-summed shallow carrier has a nonzero favourable mobile-quota
> component.

This is strictly stronger than ordering and orienting the seven given
paired-\(C_6\) packets. No such re-encoding or collar theorem is presently
known.

Accordingly the Fano identity closes the abstract permutation ledger but
not the literal moving-exterior packet. It supplies no coefficient-one
advance.
