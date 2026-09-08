# Support libraries of the valid recursive context array: exact recursion, hierarchical orthogonal resolution, and the depth-one/depth-two cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Let

\[
                         n=4\cdot2^t,
 \qquad L=n/4=2^t,
\tag{0.1}
\]

and use the parity-alternating context array of
`MATH_ATTACK_S_PARITY_COMPLETE_MAPPING_TRACE_ENTROPY_CUT_20260726.md`.
For an aligned window of coarse depth \(q\le L\), write
\(\mathcal J_{n,q}\) for the set of its possible direction supports,
allowing every even context and every source state.

This note proves four exact statements.

1.  The library \(\mathcal J_{n,q}\) is the decorated-prefix library of a
    constrained binary rotor.  The constraint is important: the rotor bit
    at an internal node is the xor of the phase bits in all descendant
    \(Q_4\) leaves.  Thus the library is smaller than the family of all
    recursively balanced \(q\)-sets.  An exact phase-refined recursion is
    given below.
2.  If \(b_{t,q}\) is the number of undecorated leaf supports in that
    recursion, then

    \[
                             |\mathcal J_{n,q}|=4^q b_{t,q}.
    \tag{0.2}
    \]

    In particular

    \[
      \mathcal J_{n,1}=\binom{[n]}1,
      \qquad
      \mathcal J_{n,2}=E(K_{n/2,n/2})\quad(n\ge8),
      \qquad
      |\mathcal J_{n,L}|=4^L.
    \tag{0.3}
    \]

3.  There is an exact recursive permutation orthogonal array.  Recursively
    choosing the image of each dyadic half and then recursing in both
    halves produces every member of \(S_n\) exactly once.  Consequently,
    for every \(q\)-set \(D\),

    \[
      \#\{\pi\in S_n:D\in\pi\mathcal J_{n,q}\}
       =\lambda_{n,q}
       :=q!(n-q)!\,|\mathcal J_{n,q}|.
    \tag{0.4}
    \]

    This holds simultaneously for all \(q\le L\).  Moreover the incidence
    at each fixed depth decomposes into \(\lambda_{n,q}\) integral
    quota-one transversals by bipartite edge colouring.
4.  Whole, unthinned libraries cannot themselves be a simultaneous
    quota-one design.  Depth one forces total frame weight one, whereas
    depth two then leaves at least

    \[
                             {n(n-2)\over4}
    \tag{0.5}
    \]

    pairs uncovered, asymptotically one half of all pairs.  Thus the
    orthogonal resolution necessarily uses depth-dependent accepted
    occurrences (equivalently, dump variables).  It cannot be promoted to
    one integral all-depth owner selection merely by calling the frame
    catalogue an orthogonal array.

The coordinate-disjoint local decoder gives an exact lift of this
distinction.  It turns a literal target into its support and exterior
trace code, so support transversals introduce no hidden local collision.
Averaging legal whole packet atlases over physical coordinate conjugates
therefore gives an exact fractional literal cover at every protected
depth.  What remains open is the integral common-column rounding which
must choose one owner-disjoint packet system simultaneously at all
depths.

## 1. The constrained rotor on the \(Q_4\) leaves

Identify the \(L=2^t\) bottom \(Q_4\) blocks with the leaves
\(\{0,1\}^t\) of a rooted binary tree.  The four coarse directions in a
leaf \(a\) are denoted

\[
                              (a,1),(a,2),(a,3),(a,4).
\tag{1.1}
\]

For a source \(x\), let \(s_a\in\mathbb F_2\) be the parity of its
restriction to leaf \(a\).  If \(v\) is an internal tree node, put

\[
                         r_v=\bigoplus_{a\succeq v}s_a.
\tag{1.2}
\]

The recursion moves the left child when the present subtree parity is
zero and the right child when it is one.  Each visit toggles that parity.
Write an integer \(k\in\{0,\ldots,L-1\}\) in least-significant-bit-first
form as \((k_0,\ldots,k_{t-1})\).  Define a leaf

\[
             \phi_s(k)=a_1a_2\cdots a_t
\tag{1.3}
\]

recursively by

\[
 a_j=k_{j-1}\oplus r_{a_1\cdots a_{j-1}}
                  \qquad(1\le j\le t).
\tag{1.4}
\]

The empty prefix is used when \(j=1\).

### Lemma 1.1 (exact visit order)

For the first \(L\) parent moves, the \(k\)-th visited \(Q_4\) leaf is
\(\phi_s(k)\).  The map \(\phi_s\) is a permutation of the leaves.

#### Proof

At the root, the selected side on move \(k\) is
\(k_0\oplus r_\varnothing\), because root choices alternate.  Each root
child has previously been visited exactly \(\lfloor k/2\rfloor\) times
when it is selected on move \(k\).  Hence its selected child is
\(k_1\oplus r_{a_1}\).  Iterating gives (1.4): at depth \(j-1\), the
current subtree has previously been visited \(\lfloor k/2^{j-1}\rfloor\)
times, whose parity is \(k_{j-1}\).

The equations can be inverted successively:

\[
                         k_{j-1}=a_j\oplus r_{a_1\cdots a_{j-1}}.
\tag{1.5}
\]

Thus distinct \(k\)'s give distinct leaves. \(\square\)

The labels \((r_v)\) are not independent tree-automorphism switches.
They satisfy, at every non-bottom internal node,

\[
                              r_v=r_{v0}\oplus r_{v1}.
\tag{1.6}

This is the exact cochain constraint inherited from the fact that the
branch bit is a genuine cube parity.  Ignoring (1.6) overstates the
support library.

## 2. Exact support-library theorem

Let

\[
 \mathscr P_{t,q}
  =\left\{\{\phi_s(0),\ldots,\phi_s(q-1)\}:s\in\mathbb F_2^L\right\}
       \subseteq\binom{\{0,1\}^t}{q}.
\tag{2.1}
\]

Equivalently, there is a completely intrinsic phase-refined recursion.
For \(\rho\in\mathbb F_2\), let
\(\mathscr P_{t,q}^{\rho}\) be the leaf supports obtainable when the
initial total parity is \(\rho\).  At \(t=0\), for both values of
\(\rho\),

\[
 \mathscr P_{0,0}^{\rho}=\{\varnothing\},
 \qquad
 \mathscr P_{0,1}^{\rho}=\{\{\varnothing\}\}.
\tag{2.2}
\]

For \(t\ge1\), put

\[
 q_0(\rho)=
 \begin{cases}\lceil q/2\rceil,&\rho=0,\\
               \lfloor q/2\rfloor,&\rho=1,
 \end{cases}
 \qquad q_1(\rho)=q-q_0(\rho).
\tag{2.3}
\]

Then

\[
\begin{split}
 \mathscr P_{t,q}^{\rho}
 =\bigcup_{\rho_0\oplus\rho_1=\rho}
 \bigl\{0A_0\cup1A_1:
 &A_0\in\mathscr P_{t-1,q_0(\rho)}^{\rho_0},\\
 &A_1\in\mathscr P_{t-1,q_1(\rho)}^{\rho_1}\,\bigr\},
\end{split}
\tag{2.4}
\]

and

\[
                    \mathscr P_{t,q}
                     =\mathscr P_{t,q}^{0}\cup
                       \mathscr P_{t,q}^{1}.
\tag{2.5}
\]

Here \(iA=\{ia:a\in A\}\).  Formula (2.4), including the xor condition
on the two child phases, is an exact finite characterization; it does not
silently replace the physical parity rotor by independent abstract rotor
bits.

### Theorem 2.1 (decorated-prefix characterization)

For every \(0\le q\le L\), in either trajectory orientation,

\[
 \boxed{
 \mathcal J_{n,q}
 =\left\{
       \{(a,c_a):a\in A\}:
       A\in\mathscr P_{t,q},\ c_a\in[4]
   \right\}.}
\tag{2.6}
\]

The same library is obtained if the context is allowed to range over all
of \(Q_n\) or is restricted to the even contexts \(E_n\).  Consequently,
with \(b_{t,q}=|\mathscr P_{t,q}|\),

\[
                         |\mathcal J_{n,q}|=4^q b_{t,q}.
\tag{2.7}
\]

#### Proof

Lemma 1.1 gives the visited leaves.  Since \(q\le L\), no leaf is visited
twice.  On its one visit, the \(Q_4\) seed can expose any of its four
directions: for a prescribed source state and prescribed direction, the
context equation

\[
                         \delta(Sp\oplus x)=i
\tag{2.8}
\]

has a solution because every direction class is a nonempty coset of the
seed kernel.  The leaf contexts are independent.  This proves (2.6) when
all contexts are allowed, and also proves the recursion (2.4).

If \(q<L\), some leaf is unvisited.  Changing a context bit in that leaf
changes the total context parity without changing the window, so every
support has an even-context realization.  If \(q=L\), every leaf is
visited once, but the unordered leaf support is the complete leaf set.
Let \(c_i\) be the common parity of the coset \(\delta^{-1}(i)\).  For a
prescribed direction \(i_a\) in leaf \(a\), (2.8) forces

\[
                    |p_a|\equiv c_{i_a}+s_a\pmod2.
\]

Consequently

\[
                    |p|\equiv\sum_a c_{i_a}+\sum_a s_a\pmod2.
\]

The phase vector \(s\) is otherwise arbitrary: changing it changes the
visit order, but all leaves are still visited once.  Choose its total
parity to make \(p\) even.  This also covers \(t=0\).

For a fixed row cycle, a reverse \(q\)-support from \(x\) is the same set
of directions as the forward \(q\)-support from \(F^{-q}x\).  Since the
start ranges over the whole row, the forward and reverse libraries agree.
Finally, the direction decorations on distinct visited leaves are
independent, which gives (2.7). \(\square\)

### Corollary 2.2 (the first two libraries)

For every \(t\ge0\), \(\mathcal J_{n,1}\) consists of all \(n\)
singletons.  For \(t\ge1\), let \(H_0,H_1\) be the two root halves of
the coordinate set.  Then

\[
 \mathcal J_{n,2}
   =\{\{u,v\}:u\in H_0, v\in H_1\},
 \qquad |\mathcal J_{n,2}|={n^2\over4}.
\tag{2.9}
\]

At full protected depth,

\[
 \mathcal J_{n,L}
 =\{J:|J\cap(\{a\}\times[4])|=1\text{ for every leaf }a\},
 \qquad |\mathcal J_{n,L}|=4^L.
\tag{2.10}
\]

#### Proof

One move can be routed to any leaf and can use any seed direction.  Two
moves visit opposite root halves once each; conversely arbitrary chosen
leaves in the two halves are compatible because their child phase xor
merely decides which half is visited first.  In \(L\) moves Lemma 1.1
visits every leaf exactly once. \(\square\)

### Remark 2.3 (balanced is necessary but not sufficient)

Every member of \(\mathscr P_{t,q}\) is recursively balanced: at each
tree node the numbers selected in its two children differ by at most one.
The converse is false because of (1.6).

For example, at \(t=3,q=3\), the leaf set

\[
                              \{000,010,110\}
\tag{2.11}
\]

is recursively balanced.  The two selected leaves in the left root half
force its initial phase to be zero, while the selected leaf \(110\) in
the right half forces that child's initial phase to be one.  Their xor is
one, so the root visits the right half twice, contrary to (2.11), which
requires two visits to the left.  Thus (2.11) is not in
\(\mathscr P_{3,3}\).  This is the first small warning against using an
independent-branch support count.

## 3. A recursive permutation orthogonal array

The support library is sparse in \(\binom{[n]}q\), but its full coordinate
orbit has an exact hierarchical resolution.

For \(\pi\in S_n\), conjugate the entire context array by \(\pi\): relabel
the source, context, and outgoing direction coordinates together.  Row
factors, full-column bijectivity, context parity, and joint trace
injectivity are invariant under this operation.  In the paired physical
lift, the same conjugation relabels the whole blocks \((b_i,a_i)\), so it
is a legal frame conjugate rather than a formal support permutation.

Define \(\Gamma_4=S_4\).  Having defined \(\Gamma_h=S_h\), form
\(\Gamma_{2h}\) as follows.  Choose an ordered equipartition

\[
                             [2h]=A\mathbin{\dot\cup}A^c,
 \qquad |A|=h,
\tag{3.1}
\]

map the canonical left half bijectively to \(A\) by one member of
\(\Gamma_h\), and map the canonical right half bijectively to \(A^c\) by
another member of \(\Gamma_h\).

### Lemma 3.1 (hierarchical array is the full permutation array)

Every permutation of \([n]\) occurs exactly once in \(\Gamma_n\).

#### Proof

A permutation uniquely determines the image \(A\) of the canonical left
half and its two restricted child bijections.  Induction gives uniqueness
inside the children.  Equivalently,

\[
                 |\Gamma_{2h}|=\binom{2h}{h}(h!)^2=(2h)!.
\tag{3.2}
\]

Thus \(\Gamma_{2h}=S_{2h}\) without repetition. \(\square\)

This is a recursive permutation orthogonal array of every strength: for
each \(q\), the image of any fixed \(q\)-set is uniform on
\(\binom{[n]}q\).

### Theorem 3.2 (simultaneous exact support multiplicities)

Put \(L_{n,q}=|\mathcal J_{n,q}|\).  For every \(D\in\binom{[n]}q\),

\[
 \#\{\pi\in\Gamma_n:D\in\pi\mathcal J_{n,q}\}
       =q!(n-q)!L_{n,q}.
\tag{3.3}
\]

The same single hierarchical frame catalogue satisfies (3.3)
simultaneously for every \(q\le L\).

#### Proof

For each \(J\in\mathcal J_{n,q}\), exactly \(q!(n-q)!\) permutations
send \(J\) to \(D\).  Distinct \(J\)'s give distinct incidences for a
fixed permutation.  Sum over \(J\), and use Lemma 3.1. \(\square\)

Thus giving every frame the depth-dependent weight

\[
                              w_q={1\over\lambda_{n,q}}
\tag{3.4}
\]

gives every \(q\)-set load exactly one.  The total frame mass is

\[
 |S_n|w_q={\binom nq\over L_{n,q}}.
\tag{3.5}
\]

This normalization is not independent of \(q\): it is one at depth one
and \(2(n-1)/n\) at depth two.  The hierarchical catalogue is therefore
simultaneously uniform, but its quota-one normalization is necessarily
depth-dependent.

### Theorem 3.3 (integral quota-one resolution after thinning)

For fixed \(q\), form the bipartite incidence graph with frame side
\(\Gamma_n\), target side \(\binom{[n]}q\), and edge

\[
                         \pi\sim D
 \quad\Longleftrightarrow\quad
                         D\in\pi\mathcal J_{n,q}.
\tag{3.6}
\]

Its frame degree is \(L_{n,q}\), and its target degree is
\(\lambda_{n,q}=q!(n-q)!L_{n,q}\).  Its edge set decomposes into
\(\lambda_{n,q}\) matchings, each of which saturates every target
\(q\)-set exactly once and uses every frame at most once.

#### Proof

The degree statements are Theorem 3.2.  Since
\(q!(n-q)!\ge1\), the maximum degree is \(\lambda_{n,q}\).  Kőnig's
line-colouring theorem gives a proper edge colouring with exactly that
many colours.  A target vertex has degree \(\lambda_{n,q}\), so its
incident edges receive every colour exactly once.  Hence every colour
class saturates the target side.  Properness gives frame degree at most
one inside a colour class. \(\square\)

Theorem 3.3 is the exact support-level design promised by the frame
catalogue.  Its qualification “after thinning” is not cosmetic: a colour
selects one support occurrence from a frame, not the frame's entire
library.

## 4. Sharp no-go for unthinned simultaneous quota one

Consider any finite family of coordinate-conjugate frames, with arbitrary
nonnegative weights \(w_\alpha\).  Let

\[
                              s=\sum_\alpha w_\alpha.
\tag{4.1}
\]

Every conjugate depth-one library contains every singleton.  Thus every
singleton has load exactly \(s\).  If depth one is quota one up to total
\(o(n)\) error, then

\[
                              s=1+o(1).
\tag{4.2}
\]

Every conjugate depth-two library is the edge set of a balanced complete
bipartite graph and therefore contains \(n^2/4\) pairs.  The total
depth-two incidence mass is \(sn^2/4\).  Even if no two of those
incidences collide, the number of uncovered pairs is at least

\[
 \binom n2-{sn^2\over4}
   ={n(n-2)\over4}-o(n^2).
\tag{4.3}
\]

This is

\[
                         \left({1\over2}-o(1)\right)\binom n2.
\tag{4.4}
\]

### Theorem 4.1 (depth-one/depth-two interface toll)

No weighted family of whole coordinate/frame-conjugate support libraries
is simultaneously quota one, or even quota one up to vanishing relative
error, at depths one and two.  In particular no unweighted family
partitions all \(q\)-sets simultaneously.

At depth two alone, an exact unweighted partition is already excluded by

\[
 {\binom n2\over n^2/4}={2(n-1)\over n}\notin\mathbb Z
                         \qquad(n>2).
\tag{4.5}
\]

#### Proof

Equations (4.2)--(4.4) prove the weighted assertion, and (4.5) is the
divisibility condition for an unweighted partition. \(\square\)

Thus a successful outer compiler must distinguish three notions:

1. choosing a whole frame, which exposes all of its libraries at once;
2. accepting a depth-dependent subfamily of the resulting occurrences;
3. paying only for owner packets, not for the accepted/dumped target
   ledger.

The recursive orthogonal array solves the second problem exactly.  It
does not solve the first and third problems integrally.

## 5. Lift through the coordinate-disjoint local decoder

For one aligned occurrence, the valid context theorem supplies the code

\[
 \mathcal C_{n,q}^{\pm}(p,x)
   =\bigl(J,p|_{J^c},x|_{J^c}\bigr),
\tag{5.1}
\]

which is injective for \(q\le L\).  In the coordinate-disjoint paired
Johnson realization, a literal signed target determines this code:

* a completed physical swap pair has occupancy zero in a lower target
  and two in an upper target;
* an untouched pair has occupancy one and displays its retained endpoint;
* an unaligned boundary pair identifies both its coarse mate and its
  physical phase.

### Lemma 5.1 (support/exterior collision reduction)

For every protected aligned or certified half-step window, equality of
two literal targets implies equality of their physical support and their
exterior code (5.1).  Inside one legal packet option, it therefore implies
equality of the source occurrence.

Consequently:

1. occurrences assigned to different support sets cannot collide
   literally;
2. after fixing a support, the only remaining outer collision question is
   equality of the exterior owner code; and
3. any quota-one design for the full pairs
   \((J,p|_{J^c},x|_{J^c})\) lifts verbatim to a quota-one literal-target
   design.

#### Proof

The physical occupancy rule recovers the varied directions and all
untouched orientation bits.  The half-step completion rule recovers the
missing aligned boundary data.  This is exactly the local decoder, after
which joint trace injectivity recovers \((p,x)\). \(\square\)

The lemma also marks the limit of a support-only argument: a partition of
the \(J\)'s does not, by itself, partition the exterior codes.

There is nevertheless an exact fractional literal lift once full physical
coordinate conjugation is allowed.  Let a legal base packet atlas contain
\(G\) owner occurrences, and conjugate the entire legal atlas—not its
individual cells—by every member of \(S_{2m}\).  Give each conjugate
weight

\[
                              {W\over G(2m)!},
 \qquad W=\binom{2m}{m}.
\tag{5.2}
\]

### Theorem 5.2 (common all-depth fractional literal cover)

Every middle owner then has total load one.  At either sign and every
protected depth \(q\), every literal rank-\((m\mp q)\) target has load

\[
             {W\over N_q},
 \qquad N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\tag{5.3}
\]

The same frame weights work simultaneously at all depths.  Accepting the
common fraction \(N_q/W\) of the depth-\(q\) occurrences and dumping the
forced surplus gives exact unit target demand.

#### Proof

The physical symmetric group is transitive on middle owners and on each
target rank.  Double counting conjugates of the \(G\) owner occurrences
gives owner multiplicity \((2m)!G/W\), which (5.2) normalizes to one.
There are also exactly \(G\) literal target occurrences at each fixed
sign and depth.  By target-rank transitivity, every target occurs
\((2m)!G/N_q\) times in the full conjugate list, and (5.2) gives (5.3).
Lemma 5.1 makes each local packet incidence binary; different packet
occurrences are retained with their honest multiplicity.  Multiplying
each depth-\(q\) accepted incidence by \(N_q/W\) gives unit load. \(\square\)

Theorem 5.2 is the literal counterpart of Theorems 3.2--3.3.  The surplus
\(W-N_q\) is forced by exact middle ownership and is not an interface
defect.

## 6. Exact remaining gate

The support problem is now separated into a proved catalogue statement
and an unproved common-choice statement.

### Proved

1. The valid context array has the exact constrained-prefix libraries
   (2.6), not the larger independent balanced-tree libraries.
2. Recursive coordinate conjugation gives exact uniform multiplicity at
   every depth and an integral quota-one resolution of accepted support
   occurrences at each fixed depth.
3. The local decoder lifts full support/exterior resolutions to literal
   targets, and full physical conjugation gives a common all-depth
   fractional literal cover.
4. Whole unthinned frame libraries cannot be simultaneous quota-one
   objects; the obstruction already occurs between depths one and two.

### Not proved

The edge-colour matchings in Theorem 3.3 are chosen independently at
different depths.  They need not be the traces of one owner-disjoint set
of whole packet columns.  Likewise, the symmetric point in Theorem 5.2 is
a convex combination of legal whole atlases, not an integral atlas.

The remaining coefficient-one lemma is therefore precisely:

> Round the common all-depth symmetric atlas point to one owner-disjoint
> family of whole legal packet columns while leaving only \(o(W)\)
> uncovered literal targets after the forced depthwise surplus is dumped.

Any proof must use the packet/owner incidence, not only the support
orthogonal array.  Any no-go must exhibit a cut in that common-column
incidence beyond the depth-one/depth-two raw-library toll proved here.
