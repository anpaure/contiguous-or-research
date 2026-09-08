# Rank-one diagonal corridors and the star-router exposure invariant

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Rank-one literalization has two sharply different parts.

First, rank-one adjacency by itself does **not** force the independent
slot generators.  Once a bounded-component diagonal owner matching has
been installed at one lower-token phase, it can be transported through an
arbitrarily long Johnson geodesic corridor.  Every intermediate lower and
upper token has the same diagonal owner matching, so the ownership
components do not grow.  A corridor of \(L\) swaps supplies \(2L\)
literal inclusion edges and \(L\) tagged copies of the diagonal carrier.

Second, the verified paired moving-exterior \(C_6\) cannot provide the
entry and exit of such a corridor inside an anchored factor by a cyclic
finite controller.  The obstruction is stronger than the direct
no-repeat theorem.

For a family of equal-rank checkpoint states \(S_i\), put

\[
 K=\bigcap_i S_i,\qquad b=|S_i\setminus K|.             \tag{0.1}
\]

Thus \(b\) is the row-varying width; a common-core star has \(b=1\).
Suppose \(s\) future nontrivial star routers act on the same transported
strands, and every whole strand is a Johnson geodesic.  Then

\[
                              \boxed{b\ge s.}             \tag{0.2}
\]

Each future router has one input petal on each strand which it later
removes.  Geodesicity forces that coordinate to be already present at the
checkpoint.  The router later inserts the same coordinate on another
strand, so it is absent there at the checkpoint and therefore is not in
the common core.  Distinct future removals on one strand use distinct
coordinates.  This proves (0.2).

Consequences:

1. from a star checkpoint there can be at most one nontrivial paired
   \(C_6\) router anywhere in the future, even after arbitrary collars;
2. one router has nonidentity absolute monodromy, so paired-\(C_6\)-only
   serial composition cannot be an anchored port factor;
3. a bounded-width finite controller supports only \(O(1)\) such routing
   events, while a \(\Theta(k)\)-stage conveyor requires width
   \(\Omega(k)\);
4. if all intermediate states remain ordinary product ports, every
   alternating star cycle lies in a single slot and exposes a one-slot
   owner generator.  For the certified pentagon five-cycle this is
   exactly \(e_i\).

Thus the positive diagonal macro-factor can be literalized through its
long middle corridor, but the verified paired \(C_6\) does not close its
anchored entry/exit.  The surviving construction must use a genuinely
growing-width mixed state or a non-star rank-one absorber.  No bounded
star controller can do it.

## 1. Johnson monotonicity

Let \(\Omega\) be a finite coordinate set.  A lower-state Johnson path is

\[
 X_0-Y_0-X_1-Y_1-\cdots-Y_{L-1}-X_L,                 \tag{1.1}
\]

where \(|X_j|=m\), \(|Y_j|=m+1\), and
\[
                         X_j\subset Y_j\supset X_{j+1}.
\]
It has Johnson length \(L\).  It is geodesic when
\[
                         L=d_J(X_0,X_L)
                           =\tfrac12|X_0\triangle X_L|. \tag{1.2}
\]

### Lemma 1.1 (write-once law)

On a Johnson geodesic, every coordinate of \(X_0\) is present until it is
possibly removed and is absent thereafter.  Every coordinate outside
\(X_0\) is absent until it is possibly inserted and is present
thereafter.  In particular, no coordinate is both inserted and later
removed, or removed and later inserted.

#### Proof

Every Johnson step removes one coordinate and inserts one coordinate.
The endpoint distance counts the minimum possible number of removals.
If a coordinate were changed twice, at least one step would not reduce
the symmetric difference from \(X_L\), and the path length would exceed
(1.2).  Equivalently, the \(L\) removed coordinates are exactly
\(X_0\setminus X_L\) and the \(L\) inserted coordinates are exactly
\(X_L\setminus X_0\). \(\square\)

Two useful time-directed consequences are:

\[
\begin{array}{ll}
q\text{ is removed in the future}
   &\Longrightarrow q\in X_0
      \text{ and }q\text{ is present at every earlier checkpoint};\\
q\text{ is inserted in the future}
   &\Longrightarrow q\notin X_0
      \text{ and }q\text{ is absent at every earlier checkpoint}.
\end{array}                                             \tag{1.3}
\]

## 2. A positive rank-one diagonal corridor

This section records why there is no blanket rank-one exposure theorem.

Let \(I\) be a finite row-label set and let
\[
                              \pi\in\operatorname{Sym}(I)          \tag{2.1}
\]
be an owner matching at a shared lower-token phase.  Thus a lower token
\(X_i\) has old owner \(i\) and new owner \(\pi(i)\).

Choose pairwise disjoint coordinate sets
\[
 A=\{a_1,\ldots,a_L\},\qquad B=\{b_1,\ldots,b_L\},     \tag{2.2}
\]
such that every \(X_i\) contains \(A\) and is disjoint from \(B\).
For \(0\le j\le L\), put
\[
 E_j=(A\setminus\{a_1,\ldots,a_j\})
          \cup\{b_1,\ldots,b_j\},                     \tag{2.3}
\]
\[
 X_{i,j}=(X_i\setminus A)\cup E_j,\qquad
 Y_{i,j}=X_{i,j}\cup\{b_{j+1}\}\quad(j<L).             \tag{2.4}
\]
Then
\[
 X_{i,j}\subset Y_{i,j}\supset X_{i,j+1},             \tag{2.5}
\]
and the exchange is \(a_{j+1}\mapsto b_{j+1}\).

### Theorem 2.1 (diagonal corridor persistence)

Assign every token \(X_{i,j},Y_{i,j}\) old owner \(i\) and new owner
\(\pi(i)\).  Then:

1. both owner maps are bijections at every lower and upper phase;
2. the two shores have exactly the same complete token ledgers;
3. every path (2.5) is a literal Johnson geodesic of length \(L\);
4. after identity owner edges are contracted, the corridor adds only the
   generator \(\pi\), repeated \(2L+1\) times.  It adds no new ownership
   generator and cannot enlarge the components of
   \(\langle\pi\rangle\).

#### Proof

The set map \(i\mapsto X_{i,j}\), and likewise \(i\mapsto Y_{i,j}\), is
the same token catalogue on both shores; only its owner is changed by the
bijection \(\pi\).  This proves the first two statements.  Equations
(2.3)--(2.5) replace each \(a_j\) once by \(b_j\), proving geodesicity by
Lemma 1.1.  Finally every owner edge is the same permutation \(\pi\), so
the generated ownership group is unchanged. \(\square\)

For the diagonal five-cycle
\[
 \pi(x_0,\ldots,x_{k-1})
       =(x_0+1,\ldots,x_{k-1}+1),                     \tag{2.6}
\]
the components in Theorem 2.1 have five rows.  Taking \(L=k\) gives
\(2k\) inclusion edges while retaining five-row components.  With
distinct position tags, any row-resolved carrier present at the entry
matching is repeated \(k\) times.  Thus an already-installed diagonal
matching can cross a literal corridor of the required length.

This statement must not be confused with gluing five literal tuple
displacements end to end.  For the original product ports,
\[
 d_J(P_x,P_{x+d})=k,\qquad P_{x+d}=P_{\pi(x)}.          \tag{2.7}
\]
Five geodesics \(P_x\leadsto P_{x+d}\) around one diagonal orbit have
their terminal lower tokens equal to the next geodesics' initial tokens.
Counted separately they duplicate those tokens; glued together they form
a closed Johnson walk, not one anchored root-to-complement geodesic.
Theorem 2.1 therefore proves persistence through the long middle, not
anchored entry/exit or port completion.

The missing point is anchored installation: an exact port factor has
identity owner matching at both its root and complementary endpoint
phases.  It must create \(\pi\) before the corridor and cancel it after
the corridor.  The next sections prove that a bounded serial
star-controller, including the verified paired \(C_6\), cannot perform
both operations geodesically.

## 3. Product intermediates expose one slot

Let the coordinate universe be partitioned into disjoint slot blocks
\(\Omega_1,\ldots,\Omega_k\).  A pure product port has the form
\[
                         P_x=\bigsqcup_{r=1}^kP^{(r)}_{x_r}.       \tag{3.1}
\]
Join two port labels when the corresponding sets have Johnson distance
one.  The resulting graph is a Cartesian product of the slot port
graphs.

### Lemma 3.1 (Cartesian triangle)

Every triangle in a Cartesian product of graphs is contained in one
factor: all three of its edges change the same slot.

#### Proof

Let \(x,y,z\) be a triangle.  If \(x\) and \(y\) differ in slot \(r\)
and \(y\) and \(z\) differ in a different slot \(s\), then \(x\) and
\(z\) differ in both \(r\) and \(s\), so they are not adjacent.  Hence
the two slots agree, and the third edge lies in that factor as well.
\(\square\)

The three lower vertices of every simple alternating \(C_6\) form a
Johnson triangle.  Therefore:

### Corollary 3.2 (pure-product exposure)

If a rank-one refinement uses only pure product ports, every alternating
\(C_6\) switch acts in one slot.  Its owner permutation is a one-slot
generator.  A certified five-petal \(C_{10}\) similarly exposes the
pentagon translation \(e_r\) in that slot.  Retaining an identity
endpoint matching gives the corresponding two-edge closed-walk voltage.

Consequently a pure-product refinement of every slot regenerates the
independent product holonomy.  Avoiding it requires genuinely mixed
states outside the product-port manifold.

## 4. Star routers and transported strands

Fix \(h\ge3\) geodesic paths, called strands.  All router labels below are
transported back to these fixed root strands; this removes irrelevant
conjugations between successive packets.

A nontrivial star router \(r\) has an input checkpoint
\[
                         S_i^r=K_r\cup\{p_i^r\},
                         \qquad i\in\mathbb Z_h,         \tag{4.1}
\]
and a fixed-point-free cyclic permutation \(\sigma_r\) such that the path
on input strand \(i\) removes \(p_i^r\), while the coordinate
\(p_i^r\) is inserted by the path on the distinct strand
\(\sigma_r^{-1}(i)\).  Common exterior exchanges may occur as well.

The verified paired moving-exterior \(C_6\) is exactly (4.1) with \(h=3\)
and \(\sigma_r=\tau\) or \(\tau^{-1}\).  The same definition covers the
common-core \(C_{2h}\) generalization.

At an arbitrary earlier checkpoint \(t\), let its strand states be
\[
                              S_i(t),\qquad
 K(t)=\bigcap_iS_i(t),\qquad
 b(t)=|S_i(t)\setminus K(t)|.                          \tag{4.2}
\]
All sets have equal size, so \(b(t)\) is independent of \(i\).

## 5. The rank-one exposure/storage invariant

### Theorem 5.1 (future-router width bound)

Suppose \(s\) nontrivial star routers occur after checkpoint \(t\), counting
a router at \(t\) itself.  If every complete strand is a Johnson
geodesic, then
\[
                              \boxed{b(t)\ge s.}          \tag{5.1}
\]

#### Proof

Fix one future router \(r\) and one transported root strand \(i\).  Let
\(q_{r,i}\) be the input petal which router \(r\) removes from that
strand.  By the first implication in (1.3),
\[
                              q_{r,i}\in S_i(t).          \tag{5.2}
\]

The same coordinate is inserted at router \(r\) on a distinct strand
\(j\), because \(\sigma_r\) has no fixed point.  By the second implication
in (1.3),
\[
                              q_{r,i}\notin S_j(t).       \tag{5.3}
\]
Hence \(q_{r,i}\notin K(t)\).  Thus every future router supplies one
coordinate of \(S_i(t)\setminus K(t)\).

For fixed \(i\), the coordinates \(q_{r,i}\) are distinct as \(r\)
varies.  Otherwise the path on strand \(i\) would remove the same
coordinate at two different routers, contradicting Lemma 1.1.  Therefore
\[
            |S_i(t)\setminus K(t)|
                \ge |\{q_{r,i}:r\text{ future}\}|=s,
\]
which is (5.1). \(\square\)

The proof permits arbitrary gaps, arbitrary common collars, arbitrary
conjugations of the strand labels, and reuse of one physical coordinate
on different strands.  It only counts the distinct
\((\text{strand},\text{removed coordinate})\) pairs forced by
geodesicity.

### Corollary 5.2 (global no-repeat theorem)

After a star checkpoint, at most one nontrivial star router can occur
anywhere on the same geodesic strands.

#### Proof

At a star checkpoint \(b(t)=1\).  Two routers, including the current one,
would contradict (5.1). \(\square\)

This strictly strengthens the direct no-repeat theorem for the paired
moving-exterior \(C_6\): separating the packets by a long collar, changing
the common hub, absorbing some output coordinates, or conjugating the
next three-cycle does not help.

### Corollary 5.3 (no paired-\(C_6\)-only anchored closure)

No anchored exact port-factor trade can create and later cancel a
nontrivial owner matching using only serial paired \(C_6\) star routers on
the same strands.

#### Proof

One paired router has absolute monodromy \(\tau\) or \(\tau^{-1}\), hence
does not have the identity endpoint routing required by an anchored
factor.  Cancellation needs at least a second nontrivial router.
Corollary 5.2 forbids it on geodesic strands. \(\square\)

For three \(C_6\)'s, the formal norm
\(1+\tau+\tau^2\) may vanish, but there is no literal serial geodesic on
which those three star routers can be placed.  The obstruction precedes
the formal norm calculation.

### Corollary 5.4 (finite-controller width cost)

If a controller exposes at most \(b_0\) row-varying coordinates at every
checkpoint, it can support at most \(b_0\) future star-routing events.
In particular, a conveyor with \(\Theta(k)\) nontrivial paired-\(C_6\)
steps requires row-varying width \(\Omega(k)\).

This is a statewise integral bound.  It is unaffected by fractional
averaging, component recolouring, or the number of unused ambient
coordinates.

The same count does not require every router to use one fixed group of
strands.

### Theorem 5.5 (interaction-component version)

Let \(\mathscr C\) be a set of root strands containing, with every future
star router that meets it, all strands of that router.  At checkpoint
\(t\), put
\[
 K_{\mathscr C}(t)=\bigcap_{j\in\mathscr C}S_j(t),\qquad
 b_i^{\mathscr C}(t)=|S_i(t)\setminus K_{\mathscr C}(t)|.
                                                               \tag{5.4}
\]
If strand \(i\) participates in \(s_i\) future nontrivial star routers,
then
\[
                              b_i^{\mathscr C}(t)\ge s_i.          \tag{5.5}
\]

#### Proof

For each future router containing \(i\), let \(q_{r,i}\) be the petal
removed from strand \(i\).  It is present on \(i\) at checkpoint \(t\).
The same coordinate is inserted by that router on a distinct strand
\(j\in\mathscr C\), so it is absent on \(j\) at \(t\).  Hence
\(q_{r,i}\notin K_{\mathscr C}(t)\).  The pairs on strand \(i\) are
distinct by the write-once law, giving (5.5). \(\square\)

Thus regrouping strands can evade the literal width-one statement only by
making the controller's interaction component carry growing noncommon
state.  If every strand participates in \(\Theta(k)\) routing stages,
the component width is \(\Omega(k)\).

## 6. Exact implication for the diagonal macro-factor

There are now three rigorously separated regimes.

1. **Pure product schedule.**  Lemma 3.1 exposes one coordinate action at
   every alternating-cycle switch.  Across all slots this regenerates the
   independent product group.
2. **Installed diagonal matching.**  Theorem 2.1 carries it through
   \(2k\) literal inclusion edges with the same five-row components and
   \(\Theta(k)\) tagged carrier.  There is no middle-corridor obstruction.
3. **Paired-\(C_6\) entry/exit.**  Theorem 5.1 prevents a bounded star
   controller from both installing and cancelling the matching inside
   anchored geodesic rows.

Accordingly the exact unresolved object is not another cyclic schedule of
the verified paired packet.  It is one of:

* a rank-one mixed-state absorber whose controller checkpoint has
  row-varying width \(\Omega(k)\);
* a non-star finite controller in which the cancellation of monodromy
  does not remove a second input-petal bank on the same strands; or
* a complete growing \(D_s\)-port factor which installs a diagonal owner
  matching once, carries it through a long corridor as in Section 2, and
  cancels it through a different, non-star ownership circuit.

The corridor construction is an exact Boolean path packet for an
installed matching, but an anchored completion of the cyclic tuple
displacement is not supplied here.  What is
proved is the requested rank-one exposure invariant:

\[
\boxed{
\begin{array}{c}
\text{product-coded intermediates expose one-slot generators};\\
\text{serial paired star routers require width at least their remaining
number};\\
\text{bounded diagonal components survive an arbitrary rank-one corridor,
but need a new non-star entry/exit absorber.}
\end{array}}                                               \tag{6.1}
\]
