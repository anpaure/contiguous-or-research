# The \(Q_8\) carousel has an unavoidable quadratic literal turnaround collision

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The phasewise owner splice in
\[
\texttt{MATH\_THEOREM\_Q8\_CAROUSEL\_PHASE\_SPLICE\_SPARSE\_SEAM\_MACRO\_20260726.md}
\]
remains valid.  Its four shores give one exact isometric \(C_{16}\)-factor
on all \(Q_8\) owners.

The displayed sparse-seam suspension, however, has a literal collision
which is stronger than the quarantine audit.  At the boundary between
the two copies of its doubled direction word, the payload changes from
an increasing traversal to a decreasing traversal.  For every depth
\(q\le L\), all \(q\) starts whose window straddles that boundary have
one identical upper target.  At the complementary cyclic boundary, all
\(q\) starts have one identical lower target.

Hence one macrocycle has aggregate signed collision excess at least

\[
                 2\sum_{q=1}^{H}(q-1)
                 =H(H-1).                           \tag{0.1}
\]

No decoder can repair identical literal targets.  This proves that the
naive macro cannot have \(O(H)\) aggregate seam collision.

The obstruction is stable under every bounded rerouting of the seam.
If a controller of \(B\) edges is placed between a long increasing
payload run and a long decreasing payload run, then at depth \(q>B\)
there is a literal target fibre of size at least \(q-B+1\).  Consequently

\[
 \sum_{q=1}^{H}\operatorname {Exc}_q
 \ \ge\
 { (H-B)(H-B+1)\over2}.                             \tag{0.2}
\]

For a \(Q_8\)-only isometric controller, \(B\le8\) in one half, so (0.2)
is \(\Theta(H^2)\).  Achieving \(O(H)\) by a local collar requires

\[
                         B\ge H-O(\sqrt H),           \tag{0.3}
\]

or a different physical interface whose literal target already recovers
the varied support.  Thus the two-sided \(Q_8\) primitive closes owner
splicing and frame holonomy, but it cannot by itself close the literal
seam gate.

## 1. Literal trace convention

For a path of Boolean owners

\[
                         X_0,X_1,\ldots,X_q,
\]

write

\[
 L(X_0,\ldots,X_q)=\bigcap_{i=0}^qX_i,\qquad
 U(X_0,\ldots,X_q)=\bigcup_{i=0}^qX_i.              \tag{1.1}
\]

Equivalently, these are the coordinatewise AND and OR words.  No varied
support tag is included.  This is the raw literal interface for which an
untouched \(00\) pair can imitate a completed lower pair and an untouched
\(11\) pair can imitate a completed upper pair.

For a fixed depth and sign, the collision excess of a family of directed
starts is

\[
                         \operatorname {Exc}
   =\#\{\text{starts}\}-\#\{\text{distinct targets}\}. \tag{1.2}
\]

A target fibre of cardinality \(r\) contributes \(r-1\) to (1.2).

## 2. The two literal turnaround fibres

Use the macro word from the owner-splice theorem:

\[
 \Pi=
 w_0,\rho_0,w_1,\rho_1,\ldots,w_7,\rho_7,           \tag{2.1}
\]

followed by a second copy of \(\Pi\).  Each payload word

\[
                         \rho_t=(d_{t,1},\ldots,d_{t,L})
\]

uses a fresh block \(D_t\).  At the beginning of the first copy all
payload bits are zero.  The first traversal of every \(\rho_t\) therefore
changes its block from \(0^L\) to \(1^L\).  In the second copy the same
directions change it back from \(1^L\) to \(0^L\).

Consider the central boundary

\[
 \rho_7^{\uparrow}\ \big|\ w_0\ \big|\
 \rho_0^{\downarrow},                               \tag{2.2}
\]

where the arrows record increasing and decreasing payload traversals.
Fix \(q\le L\).  For every

\[
                         a=0,1,\ldots,q-1,
\qquad                  b=q-1-a,                    \tag{2.3}
\]

take the \(q\)-edge window consisting of

1. the final \(a\) edges of \(\rho_7^\uparrow\);
2. the seam edge \(w_0\); and
3. the first \(b\) edges of \(\rho_0^\downarrow\).

### Theorem 2.1 (central upper fibre)

The \(q\) windows in (2.3) have one identical literal upper target.

#### Proof

Before these windows, every payload block other than the displayed
partial blocks has one fixed value throughout.  On \(D_7\), the prefix
preceding the window is already one, while every coordinate in the
traversed suffix is zero before its move and one after it.  The union is
therefore \(1^L\), independently of \(a\).

On \(D_0\), all coordinates are one before the decreasing traversal.
Deleting any prefix does not alter their union, so its union is also
\(1^L\), independently of \(b\).  Every other payload coordinate has the
same fixed value in all \(q\) windows.

The base \(Q_8\) part of every window is the same two endpoints of the
single edge \(w_0\).  Its union is independent of \(a,b\).  Hence the
full upper target is identical for all choices in (2.3). \(\square\)

At the cyclic boundary the orientations are reversed:

\[
 \rho_7^{\downarrow}\ \big|\ w_0\ \big|\
 \rho_0^{\uparrow}.                                 \tag{2.4}
\]

### Theorem 2.2 (cyclic lower fibre)

The analogous \(q\) windows across (2.4) have one identical literal lower
target.

#### Proof

On the decreasing suffix of \(D_7\), every traversed coordinate attains
zero, while its earlier prefix is already zero.  The intersection on
\(D_7\) is therefore \(0^L\).  On the increasing prefix of \(D_0\), every
coordinate begins at zero, so its intersection is \(0^L\).  The remaining
payload restrictions and the base intersection of the edge \(w_0\) are
independent of the split \(a+b=q-1\). \(\square\)

Each theorem supplies collision excess at least \(q-1\).  The two fibres
belong to different signed targets, so their contributions add.  Summing
over \(q\le H\) proves (0.1).

This is an actual collision lower bound, not the pessimistic disposal
upper bound in the aggregate-seam audit.

## 3. A bounded-controller no-go

The preceding calculation does not depend on the controller having one
edge.

### Theorem 3.1 (turnaround controller bound)

Let a path contain, consecutively,

1. the terminal part of an increasing path on a fresh payload block;
2. a fixed controller path \(Z_0,\ldots,Z_B\) of \(B\) edges on disjoint
   controller coordinates; and
3. the initial part of a decreasing path on another fresh payload block.

Assume both payload runs have length at least \(H\).  Then for every
\(B<q\le H\), the upper depth-\(q\) trace map has a fibre of cardinality
at least

\[
                         q-B+1.                     \tag{3.1}
\]

The lower trace has the same conclusion when decreasing and increasing
are interchanged.

#### Proof

Choose nonnegative integers \(a,b\) with

\[
                         a+b=q-B.                   \tag{3.2}
\]

There are \(q-B+1\) choices.  Start \(a\) edges before the controller,
traverse all \(B\) controller edges, and then traverse \(b\) decreasing
payload edges.

Exactly as in Theorem 2.1, the upper target on the increasing suffix is
the all-one word, independently of \(a\), and the upper target on the
decreasing prefix is the all-one word, independently of \(b\).  The
controller contribution is

\[
                         \bigcup_{i=0}^{B}Z_i,
\]

the same for every split in (3.2).  All exterior coordinates are fixed.
Thus all \(q-B+1\) starts have one upper target.  Complementing the
argument proves the lower statement. \(\square\)

### Corollary 3.2 (aggregate lower bound)

Under the hypotheses of Theorem 3.1,

\[
\begin{aligned}
 \sum_{q=1}^{H}\operatorname {Exc}_q^+
 &\ge \sum_{q=B+1}^{H}(q-B)\\
 &= { (H-B)(H-B+1)\over2}.                          \tag{3.3}
\end{aligned}
\]

The complementary turnaround gives the same lower-sign bound.

In particular, \(B=O(1)\) gives \(\Omega(H^2)\).  If the desired
aggregate bound is \(O(H)\), equation (3.3) forces
\(H-B=O(\sqrt H)\), which is (0.3).

## 4. Why the \(Q_8\) frame data cannot decode the offset

The successor/predecessor identities

\[
                         \Xi_j^-=\Xi_{j+1}^+
\]

certify which frame is legal on each side of a seam.  They do not record
the split parameter \(a\) in (2.3).  Every one of the \(q\) colliding
windows:

* traverses the same \(Q_8\) edge;
* has the same base intersection or union;
* has the same exterior owner tag;
* has the same literal payload target; and
* differs only in how many erased moves lie to the left or right.

Thus neither a deterministic decoder nor conditional expectation can
separate them.  A rerouting confined to a contiguous controller using
only the eight Q8 directions has width at most eight before an isometric
component repeats a direction.  Theorem 3.1 then gives

\[
                         \Omega((H-8)^2)
\]

aggregate excess.  Spreading those directions across
\(\Theta(H)\) payload positions is not covered by this bounded-controller
sentence; it is precisely an \(H\)-wide collar of the kind listed below.

## 5. Exact escape boundary

The obstruction applies to the raw literal Boolean interface and to every
bounded-controller macro having opposite monotone payload collars.  It
does not contradict either of the following stronger interfaces.

1. In a coordinate-disjoint Johnson realization where local occupancy
   itself reveals every varied pair, the target supplies the erased
   support.  The fibres in Theorems 2.1--2.2 then split.
2. A genuinely \(H\)-wide literal collar may encode the split \(a\).
   Theorem 3.1 shows that width \(H-O(\sqrt H)\), not a bounded Q8 cell,
   is the correct scale for a worst-case local turnaround repair.

There are three viable continuations:

1. prove that the outer packet embedding always uses the
   support-revealing coordinate-disjoint Johnson interface;
2. build an \(H\)-scale literal seam chart and charge its owner support,
   rather than treating Q8 as the complete seam; or
3. cover the colliding seam targets from other macrocycles in one global
   target matching.

Accordingly, the valid Q8 owner splice should be retained as a
frame-change port, but the coefficient-one proof cannot use it as a
standalone literal seam decoder.
