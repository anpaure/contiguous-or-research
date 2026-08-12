# Rotating-hole rail: exact Pascal seam ledger and the upper-ticket dichotomy

Date: 2026-08-01  
Lane: K, fixed-defect regenerative upper interface  
Status: exact local theorem and sharp scope boundary. Opening the rail's own
saturated edge costs no exterior upper ticket. Bare-rail endpoint attachment
has a six-ray bounded state; the full plus packet has eleven directed rays
and, once both ends of its short component are joined, one additional
two-sided grid. Planting the rail through an arbitrary interior Pascal cut
can instead destroy a quadratic crossing bank. The lower one-cell triangular
common-cap obstruction is unchanged.

## 0. Setup and result

Use the notation of
MATH_THEOREM_BOOLEAN_HEX_SHORTEST_RESIDENT_RETURN_RAIL_AND_PHASE_DECOUPLING_20260801.md:

\[
 Z=L\cup\{a,d_0,y\},\qquad
 V_i=Z\setminus\{z_i,z_{i+1}\},
\]

where

\[
 z_0=a,\qquad z_1=y,\qquad z_2=d_0,\qquad
 z_{j+3}=x_j\quad(0\le j<h).
\]

The directed rail is

\[
 {\cal R}=(V_1,V_2,\ldots,V_{h+2},V_0),                 \tag{0.1}
\]

of length \(n=h+3\), with endpoints \(V_1=F=L+a\) and
\(V_0=E=L+d_0\). Its omitted wrap edge is \(EF\). Put

\[
                              U=E\cup F=Z-y.             \tag{0.2}
\]

For a required short-window depth \(d\), assume \(h\ge d\).

Three operations must not be conflated.

1. **Saturated self-opening:** delete the wrap edge \(EF\) of the rail
   cycle and retain (0.1).
2. **Endpoint attachment:** concatenate already open path components at
   exposed endpoints; no old child edge is deleted.
3. **Interior planting:** cut an arbitrary edge of a Pascal-child path and
   insert or reconnect the rail there.

Self-opening has zero upper debt at every available depth. Endpoint
attachment removes no old interval and exports a six-ray short-band state.
Interior planting can have quadratic upper debt. Thus the rotating-hole
theorem removes the upper analogue of the triangular obstruction only on
the prepared self-opening/endpoint face.

## 1. Exact saturated self-opening ledger

### Theorem 1.1 (all-depth wrap repayment)

Fix \(1\le q\le h+2=n-1\), so a depth-\(q\) upper trace is the union of
\(q+1\) consecutive rail owners.

* At \(q=1\), the unique cyclic window using the wrap edge has value \(U\).
* At every \(2\le q\le h+2\), exactly \(q\) cyclic windows of length
  \(q+1\) use the wrap edge, and all have value \(Z\).
* After opening the wrap, the linear rail still has exactly

  \[
                              n-q=h+3-q                 \tag{1.1}
  \]

  windows of length \(q+1\), all with value \(Z\).

In the Boolean-hex plus phase the deleted \(q=1\) value is restored by
the new edge \(AF\), because \(A\cup F=U\). Therefore

\[
 \{AB,CD,EF\}\cup{\cal R}
       \longrightarrow
 \{AF,CB,ED\}\cup{\cal R}                                \tag{1.2}
\]

loses no local upper target at any available depth
\(1\le q\le h+2\). No exterior
upper ticket is needed for the rail wrap.

#### Proof

The missing pairs of \(E=V_0\) and \(F=V_1\) are \(\{a,y\}\) and
\(\{y,d_0\}\). Hence \(E\cup F=Z-y=U\). Any cyclic interval of at least
three rail vertices has empty intersection of its missing pairs and union
\(Z\). A fixed cycle edge belongs to exactly \(q\) cyclic intervals of
length \(q+1\).

After opening, a linear word of \(n\) vertices has
\(n-(q+1)+1=n-q\) intervals of that length. They have value \(Z\) when
\(q\ge2\), and (1.1) is positive because \(q\le h+2=n-1\). Finally
\(A=U-b\), \(F=L+a\), and \(b\in L\), so \(A\cup F=U\).
\(\square\)

Inside the rail itself, the multiplicity of the occurrence \(Z\) drops by
\(q\); the appended packet endpoints may create further \(Z\)-occurrences,
but target coverage does not depend on that count. A later
occurrence-labelled compiler must retain this distinction.

### Corollary 1.2 (local phase monotonicity)

For \(q\ge2\), the old local upper deck is \(\{Z\}\). The plus long path
has local values

\[
                         Z,\qquad Z-a+c,\qquad Z+c.       \tag{1.3}
\]

Immediate upper colours agree by the four-resource identity. Thus the
local actuator has no upper last-witness loss at any available depth.
This is an upper-shadow statement, not a lower source-pin statement.

## 2. Exact exterior interface

Let a left exterior path end immediately before \(V_1\), and a right
exterior path start immediately after \(V_0\). Write

\[
 S_u=\text{union of the last \(u\) left-exterior owners},\qquad
 P_v=\text{union of the first \(v\) right-exterior owners}. \tag{2.1}
\]

The rail prefix and suffix unions are

\[
 \Pi_r=
 \begin{cases}
 F,&r=1,\\
 Z-d_0,&r=2,\\
 Z,&r\ge3,
 \end{cases}
 \qquad
 \Sigma_r=
 \begin{cases}
 E,&r=1,\\
 Z-a,&r=2,\\
 Z,&r\ge3.
 \end{cases}                                               \tag{2.2}
\]

### Theorem 2.1 (three--three--one interface normal form)

Every interval meeting the rail has exactly one of the following forms:

\[
\begin{array}{c|c}
\text{geometry}&\text{union}\\ \hline
\text{contained in the rail}&
 \text{one owner, one rail-edge union, or }Z\\
\text{enters from the left only}&S_u\cup\Pi_r\\
\text{exits to the right only}&\Sigma_r\cup P_v\\
\text{spans the whole rail}&S_u\cup Z\cup P_v.
\end{array}                                                 \tag{2.3}
\]

For windows of length at most \(d+1\), with \(h\ge d\), the last case is
impossible. The complete exterior interface in this short band consists
of six directed ray families:

\[
 S_u\cup F,\quad S_u\cup(Z-d_0),\quad S_u\cup Z,\qquad
 E\cup P_v,\quad (Z-a)\cup P_v,\quad Z\cup P_v.             \tag{2.4}
\]

There are at most \(3d-3\) distinct indexed values on each side, hence at
most \(6d-6\) total: the three ray lengths on either side are
\(d,d-1,d-2\).

For a larger maximum width \(D\), intervals spanning both exteriors first
appear when

\[
                              u+v+n\le D+1.                 \tag{2.5}
\]

If \(R=D+1-n\), and both exterior fragments have at least \(R-1\)
owners, the number of positive ordered pairs \((u,v)\) in this full-span
grid is

\[
 \begin{cases}
 0,&R\le1,\\
 R(R-1)/2,&R\ge2.
 \end{cases}                                               \tag{2.6}
\]

#### Proof

Intersecting the missing pairs of the first one, first two, or first at
least three rail vertices gives (2.2); reversal gives the suffix formula.
An interval spanning the rail contains at least three rail vertices and
therefore receives the fixed contribution \(Z\). This proves (2.3).

A window meeting both exterior shores has at least
\(n+2=h+5>d+1\) vertices. For the left interface, \(r=1\) allows
\(1\le u\le d\), \(r=2\) allows \(1\le u\le d-1\), and some
\(r\ge3\) exists exactly for \(1\le u\le d-2\). This gives \(3d-3\);
the right side is symmetric. Finally, when the exterior lengths do not
truncate the bank, the positive pairs with \(u+v\le R\) number
\(1+2+\cdots+(R-1)=R(R-1)/2\). Shorter exteriors only delete pairs.
\(\square\)

The rail therefore exports a bounded **signature alphabet**, not a
bounded number of target occurrences. In the \(d\)-band it exports six
complete ray relations. At arbitrary width it exports those six rays plus
one two-sided \(S\cup Z\cup P\) grid relation.

### Corollary 2.2 (the full plus packet has eleven rays plus a short grid)

For the actual Boolean-hex plus phase, the long component is

\[
                   A,V_1,\ldots,V_{h+2},V_0,D,             \tag{2.7}
\]

and the other component is \(C,B\). The prefix states of (2.7), before
the opposite endpoint can be reached, are

\[
                              A,\qquad U,\qquad Z,           \tag{2.8}
\]

and its suffix states are

\[
 D,\qquad L\cup\{c,d_0\},\qquad Z-a+c,\qquad Z+c.           \tag{2.9}
\]

The two orientations of the short path \(C,B\) each have two states:
\[
       C,\ C\cup B\qquad\text{and}\qquad B,\ C\cup B.       \tag{2.10}
\]

Consequently a terminal all-plus packet with all four physical sockets
exposed has at most

\[
                               3+4+2+2=11                  \tag{2.11}
\]

directed short-band **ray** relations, independent of \(d\). This is not
yet the complete interface. Once both ends of the two-vertex component
\(C,B\) are joined to exterior fragments, its spanning intervals form the
additional grid

\[
                         S_u\cup(C\cup B)\cup P_v.          \tag{2.12}
\]

Already in the depth-\(d\) band the positive pairs satisfy
\(u+v\le d-1\), so (when the exterior fragments are long enough) this grid
has

\[
                              {d-1\choose2}                 \tag{2.13}
\]

indexed entries. Thus the full short-band packet state is eleven directed
ray relations plus one compound grid relation. At unrestricted width the
long component contributes a second compound grid relation. The number six
is the bare-rail ray interface; the complete full-packet relation counts are
twelve in the short band and thirteen at unrestricted width.

#### Proof

The first two unions at the left of (2.7) are
\(A\) and \(A\cup F=U\); adding the next rail vertex supplies \(y\) and
gives \(Z\). From the right, the first two states are \(D\) and
\(D\cup E=L+c+d_0\). Adding \(Q\) gives \(Z-a+c\), and the next rail
vertex supplies \(a\), giving \(Z+c\). Equation (2.10) is immediate.
Because \(h\ge d\), no window in the \(d\)-band reaches both ends of the
long component. A window meeting both exteriors of \(C,B\), however, has
length \(u+2+v\), which is at most \(d+1\) exactly when
\(u+v\le d-1\). Counting positive pairs proves (2.13). \(\square\)

### Corollary 2.3 (deck-matched planting needs no exterior ticket)

Let \(X\) be a prepared Pascal-child fragment which is to be replaced by
the bare rail \({\cal R}\). Write \(\mathcal P,\mathcal S,\mathcal I\)
for its nonempty prefix-, suffix-, and internal-interval union decks. If

\[
\begin{aligned}
 \mathcal P(X)&\subseteq\{F,Z-d_0,Z\},\\
 \mathcal S(X)&\subseteq\{E,Z-a,Z\},\\
 \mathcal I(X)&\subseteq\mathcal I({\cal R}),\\
 \bigcup X&=Z,
\end{aligned}                                               \tag{2.14}
\]

then replacing \(X\) by \({\cal R}\) preserves every old interval-union
target in every exterior context. It needs zero exterior upper tickets at
all widths.

#### Proof

The three rail prefix and suffix states are (2.2), its total union is
\(Z\), and the internal-deck inclusion is assumed. The compressed
prefix/suffix replacement theorem applies verbatim. \(\square\)

This is the exact prepared-host escape from the grid obstruction. In
particular, another fragment with the same labelled three-state boundary
signature and dominated internal deck may be rethreaded into the rail
without paying targetwise returns. The direct edge \((F,E)\) is not on
this face: its total union is \(U=Z-y\), not \(Z\).

## 3. What bounded upper tickets can and cannot mean

A **targetwise ticket** is an additional unaffected or newly constructed
interval witnessing one named target. A **ladder ticket** is one
simultaneous occurrence-labelled certificate for every target in one ray
of (2.4).

### Lemma 3.0 (exact two-sided cut transport)

Suppose the rail replaces an adjacency \(FE\) in a child path. If an old
cut-crossing interval uses \(u\) exterior owners to the left and \(v\) to
the right, its old and rail-spanning unions are

\[
\begin{aligned}
 T^-_{u,v}&=S_u\cup U\cup P_v,\\
 T^+_{u,v}&=S_u\cup Z\cup P_v
            =T^-_{u,v}\cup\{y\}.
\end{aligned}                                               \tag{3.0a}
\]

The rail-spanning occurrence has length \(u+n+v\). Under a maximum
allowed window length \(D+1\), the old occurrence is directly repaid by
its convex-hull rail occurrence if and only if

\[
                    u+n+v\le D+1
       \quad\text{and}\quad y\in T^-_{u,v}.                 \tag{3.0b}
\]

Equivalently, the set condition is \(Z\subseteq T^-_{u,v}\). If (3.0b)
fails, repayment needs an unaffected duplicate or an exterior ticket.

#### Proof

The rail adds all of \(Z\), while its endpoints already supplied
\(U=Z-y\), proving (3.0a). The convex hull contains the \(u\) left
owners, all \(n\) rail owners, and the \(v\) right owners. Its union equals
the old target exactly when \(Z\subseteq T^-_{u,v}\). \(\square\)

For the rail's own wrap, every crossing interval of length at least three
already contains \(y\) and has value \(Z\); this is why Theorem 1.1 is
safe. For a generic Pascal edge, neither condition in (3.0b) is automatic.

### Theorem 3.1 (endpoint-positive / interior-cut-negative dichotomy)

1. Opening the rail's own wrap uses zero targetwise exterior tickets.
2. Concatenating the open rail to already exposed path endpoints deletes no
   old interval. It therefore uses zero tickets merely to preserve the old
   upper deck; the six rays in (2.4) are additions.
3. If attachment instead cuts an arbitrary internal Pascal-child edge, no
   absolute targetwise bound follows from the rail theorem. At depth \(d\),
   old windows using that cut are indexed by

   \[
             (u,v),\qquad u,v\ge0,\qquad u+v\le d-1,        \tag{3.1}
   \]

   and number \(d(d+1)/2\). There are literal Johnson path contexts,
   including a Johnson edge at the planted cut, in which their unions are
   pairwise distinct and each is a last witness. A **bare** rail longer than
   \(d+1\) destroys them all, so \(d(d+1)/2\) targetwise tickets are
   necessary. In the full packet the native edge \(AF\) and a chosen socket
   orientation can repay the immediate target and at most the boundary-axis
   ladders in this fixture; the strict two-sided interior still has
   \({d-1\choose2}\) entries. Thus the full packet also has quadratic
   worst-case targetwise debt.

Consequently, a fixed bank of \(H\) prepared self-openings or bare-rail
endpoint attachments has zero local preservation debt and only \(6H\)
short-band ray relations. If all four sockets of each full plus packet are
exposed, replace this by \(11H\) rays plus \(H\) short-component grids.
An arbitrary-cut bank may require

\[
                         \Omega(Hd^2)                       \tag{3.2}
\]

targetwise upper returns.

#### Proof

Items 1 and 2 are immediate. For item 3, choose a common set \(C\), of
size at least \(2d\),
containing pairwise-distinct
\(p_1,\ldots,p_d,q_1,\ldots,q_d\), and put

\[
                         X_0=C+x,\qquad Y_0=C+y.             \tag{3.3}
\]

On the standard ground of size \(2m+1\), one may take \(|C|=m-1\) and
\(m\ge2d+2\); the remaining \(m+2\) coordinates then accommodate the
fresh \(x,y,\eta,c,\ell_i,r_i\) labels used below.  This includes the
asymptotic Pascal regime \(d=O(\sqrt m)\).

Thus \(X_0Y_0\) is a Johnson edge. Choose fresh coordinates
\(\ell_i,r_i\), and define

\[
\begin{aligned}
 X_u&=(X_0-\{p_1,\ldots,p_u\})
          \cup\{\ell_1,\ldots,\ell_u\},\\
 Y_v&=(Y_0-\{q_1,\ldots,q_v\})
          \cup\{r_1,\ldots,r_v\}.
\end{aligned}                                               \tag{3.4}
\]

Both displayed sequences are Johnson paths. Their suffix/prefix unions
through the cut are
\(X_0\cup\{\ell_1,\ldots,\ell_u\}\) and
\(Y_0\cup\{r_1,\ldots,r_v\}\). The cut-crossing union is

\[
C\cup\{x,y\}\cup\{\ell_1,\ldots,\ell_u\}
                   \cup\{r_1,\ldots,r_v\},                 \tag{3.5}
\]

so all pairs in (3.1) are different.  In the finite Johnson word

\[
 X_{d-1},\ldots,X_1,X_0,Y_0,Y_1,\ldots,Y_{d-1},
\]

each displayed occurrence is unique.  Indeed, an interval realizing (3.5)
must contain both \(x\) and \(y\), hence cross \(X_0Y_0\).  Presence of
\(\ell_u\) and absence of \(\ell_{u+1}\) fixes its left endpoint to
\(X_u\) (with absence of \(\ell_1\) fixing \(X_0\) when \(u=0\)); the
reflected statement fixes its right endpoint to \(Y_v\).  Thus these are
literal last witnesses in this local context. A replacement rail of
\(n=h+3>d+1\) vertices separates the exterior shores too far for an
allowed window to see both. The rail may be chosen with
\(L=C,a=x,d_0=y\) and rail-exterior label \(\eta\) outside (3.5);
then every \(Z\)-state contains \(\eta\), while the one- and two-vertex
states miss one of \(x,y\). Thus no one-sided new ray equals (3.5).
Hence every displayed target needs another occurrence for the bare rail.

For the full packet use its old edge \(AB\), not the now-internal rail
endpoints. Put

\[
 J=A\cap B=(L-\{b\})\cup\{a\},\qquad
 A=J+d_0,\qquad B=J+c.                                  \tag{3.6}
\]

Choose distinct \(p_i,q_i\in J\) and fresh \(\ell_i,r_i\), and extend
outward from \(A,B\) by the same cumulative swaps as in (3.4).  Join the
left exterior at the exposed plus socket \(A\) and the right exterior at
the exposed plus socket \(B\).  The old \(AB\)-crossing targets are

\[
 J\cup\{d_0,c\}\cup\{\ell_1,\ldots,\ell_u\}
                    \cup\{r_1,\ldots,r_v\}.              \tag{3.7}
\]

They are unique by the same endpoint argument.  In the plus phase the two
sockets lie on different local paths,

\[
 A-F-\mathcal R-E-D,qquad C-B.                           \tag{3.8}
\]

Any final chronology joining these paths from the \(A\)-shore to the
\(B\)-shore must traverse \(F\) (and then \(D\)) on the first path before
reaching the second.  Both \(F=L+a\) and \(D=L+c\) contain \(b\), whereas
every target in (3.7) omits \(b\).  A one-sided interval lacks one of the
two private \(\ell/r\) shore families.  Hence no strict target with
\(u,v\ge1\) is locally repaid.  (The new edge \(CB\) may repay the origin
and one boundary-axis ladder.)  The number of strict pairs under
\(u+v\le d-1\) is \({d-1\choose2}\).  All socket joins used here are
literal: \(A,B\) themselves are the exposed endpoints in (3.8). \(\square\)

### Corollary 3.2 (exact sufficient upper export)

For a prepared bare-rail endpoint attachment in the \(d\)-band, six
complete ladder certificates, one for each family in (2.4), are a
sufficient finite boundary state. For a full plus packet use the eleven
directed families and the short-component grid in Corollary 2.2. For
unrestricted widths, add the long-component full-span grid as well. A
certificate may instead state that every target in its family has an
unchanged witness away from all cuts.

This does not say that six named masks suffice. One ray may contain \(d\)
distinct unique targets, and the full-span bank may have the quadratic
size (2.6). The missing Pascal theorem is exactly the existence of these
complete ladder/grid certificates, or a duplicate-witness dominance
theorem making them vacuous.

## 4. Exact common-cap and nonzero row

The rotating-hole owner identity and the terminal lower compiler live on
different incidence systems. The rail has the explicit cyclic erosion
source

\[
 K=L\setminus\{x_0,\ldots,x_{h-1}\},\qquad
 W_j=K\cup\{z_j\}.                                      \tag{4.1}
\]

Since \(h\le m-2\), \(K\ne\varnothing\). More strongly, the linear source
word

\[
        Q_t=W_{\,t+3\pmod n}\qquad(0\le t<n+h)             \tag{4.2}
\]

is nonzero and satisfies

\[
                         D^hQ=(V_1,V_2,\ldots,V_0).         \tag{4.3}
\]

Indeed, its owner-\(t\) window is

\[
 \bigcup_{s=0}^{h}W_{t+3+s}=V_{t+1\pmod n}.
\]

Thus the bare linear rail and every interval union internal to it coexist
in one literal antecedent. This removes an internal common-\(Q\) concern.
It does not prove that the padded source (4.2), an exterior Pascal
antecedent, and selected lower compiler pins can be glued.

Let \(p\) range over the live source positions, \(P_p\) be the carrier
cap, and each protected row \(J\) have target \(T_J\) and frozen exterior
union \(E_J\). Define

\[
 Q_p^{\max}=P_p\cap\bigcap_{J\ni p}T_J.                    \tag{4.4}
\]

### Theorem 4.1 (rail attachment common-cap criterion)

One nonzero common source word exists for the declared carrier, rail-ray,
ticket, and lower-pin rows if and only if

\[
 E_J\subseteq T_J,\qquad Q_p^{\max}\ne\varnothing,\qquad
 T_J=E_J\cup\bigcup_{p\in J}Q_p^{\max}                    \tag{4.5}
\]

for every row \(J\) and source position \(p\). When feasible,
\(Q_p=Q_p^{\max}\) works.

If every target meeting the rail contains \(K\), and every corresponding
cap contains \(K\), then nonzeroness is automatic. Exact positive coverage
is not: each active label \(z_j\) demanded by a row must survive at some
position of that row. One exterior screen can erase every such provider
while leaving all signature counts unchanged.

#### Proof

Every feasible source letter at \(p\) lies in its carrier cap and every
target row containing \(p\), hence in (4.4). This proves necessity.
Conversely, the maximal letters (4.4) are nonempty, cap-legal, introduce
no forbidden coordinate, and reconstruct every target by (4.5).
\(\square\)

Thus a complete six-ray upper certificate does not imply common-\(Q\);
it must be checked occurrence by occurrence together with the lower pins.

## 5. Relation to the one-cell triangular collar

The safe wrap opening is an owner-chronology statement. The one-cell
theorem concerns old **source** intervals crossing an inserted source
value \(Z_*\):

\[
        \widehat C_{u,v}=C_{u,v}\cup Z_*
        \qquad(u,v\ge1,\ u+v\le d-1).                    \tag{5.1}
\]

Nothing in the rail identities changes (5.1). If a selected lower pin
omits a coordinate of \(Z_*\), it still needs a return; the complete
possible collateral is still the triangle of size

\[
                              {d-1\choose2}.                \tag{5.2}
\]

Therefore the rotating-hole rail:

* collapses the **upper wrap-seam triangle**, because every wrap window of
  length at least three has value \(Z\), which survives internally;
* does not collapse the **lower common-cap triangle** created by a one-cell
  source insertion; and
* gives a bounded six-ray state for prepared endpoint attachment in the
  \(d\)-band, but no bounded targetwise-ticket theorem for arbitrary
  Pascal cuts or unrestricted two-sided widths.

### Corollary 5.1 (sharp fixed-\(H\) conditional statement)

Let \(H\) be fixed. Suppose a Pascal child exports \(H\) resource-private
rotating-hole cycles, each opened only at its saturated \(EF\) edge and
attached only through exposed endpoints. Suppose further that:

1. every needed upper target on the applicable bare-rail or full-packet
   rays and grids has an unchanged witness or a complete exterior
   ladder/grid certificate;
2. the terminal chronology passes residence and every endpoint join; and
3. all upper certificates and lower compiler pins pass (4.5).

Then resetting all \(H\) packets adds no upper target debt. The exported
bare-rail state has at most \(6H\) short-band ladder relations
(\(7H\) when its full-span grid is retained as one typed relation). If all
four sockets of the full plus packets remain exposed, the correct complete
short-band bound is \(12H\): eleven directed ladders and the \(C,B\) grid.
At unrestricted width it is \(13H\), after adding the long-component grid.

Without prepared endpoints, Theorem 3.1 gives a reachable
\(\Omega(Hd^2)\) obstruction. Without item 3, the one-cell triangular
compiler gate remains. This is an upper-interface theorem, not an
unconditional \(B(k)+O(1)\) construction.

## 6. Independent replay

The dependency-free checker

    scratch/audit_k_rotating_hole_rail_pascal_upper_ticket_20260801.py

reconstructs the rail for \(2\le d\le h\le20\), verifies every cyclic
wrap-loss and linear-survivor count, the three--three spectra, the six-ray
counts, the full-packet short-grid correction, and the arbitrary-width
full-span count. It also replays the literal nonzero antecedent and the
fresh-coordinate Johnson-path construction in Theorem 3.1. The frozen
summary is

    scratch/k_rotating_hole_rail_pascal_upper_ticket_20260801.audit.json
