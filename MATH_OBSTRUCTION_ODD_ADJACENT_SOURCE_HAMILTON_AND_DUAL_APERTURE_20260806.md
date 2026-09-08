# Odd current: the adjacent-source Hamilton route has a dyadic obstruction

**Date:** 2026-08-06  
**Method:** bipartite current on the compressed ternary layer and a literal
root-coordinate audit; no computation or search  
**Status:** unconditional obstruction and corrected recursive target.  It
rules out a one-socket construction using only a Hamilton cycle, Hamilton
path, or near-perfect matching of adjacent compressed-source moves in every
even compressed dimension.  It also proves that the complement pairing
cannot be realized by two copies of the existing forward aperture: its
second route must change scan root or scan phase.

## 1. The compressed adjacent-source graph

Put

\[
 {cal Q}_m={\cal T}_{m,m}
   =\{u\in\{0,1,2\}^{\mathbb Z_m}:\sum_i u_i=m\}.
\tag{1.1}
\]

Let \(G_m\) join two words when one unit is transferred between cyclically
adjacent compressed coordinates.  This is the natural nearest-neighbour
source graph produced by quiet compression.

### Theorem 1.1 (exact even-dimensional current)

If \(m=2s\), then \(G_m\) is bipartite and its two shores have cardinality
difference

\[
 \boxed{
   \Delta_m=[x^s](1+x+x^2)^s=|{\cal T}_{s,s}|.
 }
\tag{1.2}
\]

Consequently every matching of \(G_m\) leaves at least \(\Delta_m\)
vertices unmatched.  The first-nonquiet scan attains this bound, so

\[
                 |{cal Q}_m|-2\nu(G_m)=\Delta_m.
\tag{1.3}
\]

#### Proof

Number the compressed coordinates \(0,1,\ldots,m-1\) and put

\[
                  \chi(u)=\sum_{i=0}^{m-1} i u_i\pmod2.
\tag{1.4}
\]

An internal adjacent transfer changes \(\chi\) by one.  The wrap transfer
between \(m-1\) and zero changes it by \(m-1\), also odd because \(m\) is
even.  Thus every edge reverses \(\chi\).

The signed shore difference is

\[
\begin{aligned}
 \sum_{u\in{cal Q}_m}(-1)^{\chi(u)}
 &= [z^m]
    (1+z+z^2)^s(1-z+z^2)^s\\
 &= [z^m](1+z^2+z^4)^s\\
 &= [x^s](1+x+x^2)^s.
\end{aligned}
\tag{1.5}
\]

This proves the bipartite lower bound on unmatched vertices.  On the other
hand, pair the compressed coordinates and apply the first-nonquiet scan.
The scan matches every nonquiet word and leaves exactly one quiet copy of
\({\cal T}_{s,s}\).  Hence equality holds in (1.3).  \(\square\)

### Corollary 1.2 (no adjacent Hamilton predecessor)

For every even \(m\), \(G_m\) has no Hamilton cycle.  For every even
\(m\ge4\), it has no Hamilton path and no near-perfect matching.

#### Proof

A Hamilton cycle in a bipartite graph uses equally many vertices from the
two shores.  A Hamilton path permits shore difference at most one.  But
\(\Delta_m=|{\cal T}_{m/2,m/2}|\), which is positive for all even \(m\)
and is at least three for \(m\ge4\).  Equation (1.3) gives the matching
claim.  \(\square\)

Thus a last-intersection permutation cannot be made into one Hamilton
cycle by using only adjacent compressed-source moves in all dimensions.
The one-cycle idea can still be used after introducing a nonadjacent
cross-slice operation, but adjacency alone has an exact dyadic defect.

## 2. The correct recursive matching target

The obstruction is self-similar rather than growing unpredictably.  The
optimal scan matching on \({\cal Q}_{2s}\) leaves precisely
\({\cal Q}_s\).  Repeating gives

\[
 m\longmapsto\lfloor m/2\rfloor
   \longmapsto\lfloor m/4\rfloor\longmapsto\cdots,
\tag{2.1}
\]

ending at the single all-one socket.  Therefore a source-pairing proof
does not need a Hamilton cycle.  It needs the following smaller physical
statement.

> **Recursive synchronized-pair aperture.**  Every source edge selected
> by the first-nonquiet matching of one compressed layer has a two-source
> linkage ending at both endpoints of one private physical boundary edge;
> these linkages are disjoint within the layer and avoid the recursively
> embedded quiet residue.

If this statement is available at every level, the scan pairs all sources
except the recursively compressed bank, and induction leaves exactly one
socket.  The exact source-matching arithmetic is therefore already solved;
the missing content is the synchronized physical lift.

## 3. Why two forward apertures cannot be synchronized

The existing forward aperture sends every quiet source to a terminal
\(a\in A_\partial\) satisfying

\[
                      a_0=1,
 \qquad               (a_{2m},a_0)\in\{01,21\}.
\tag{3.1}
\]

Its physical boundary partner is

\[
                      \tau(a),\qquad \tau=(0\ \ 2m),
\tag{3.2}
\]

and therefore

\[
                 \tau(a)_{2m}=1,
 \qquad          \tau(a)_0\in\{0,2\}.
\tag{3.3}
\]

### Proposition 3.1 (forward-forward no-go)

No two terminals produced by the existing forward aperture are the two
endpoints of one physical boundary edge.

#### Proof

Every forward terminal has coordinate zero equal to one by (3.1), whereas
the partner of any forward terminal has coordinate zero equal to zero or
two by (3.3).  Hence the partner is not in the forward terminal bank.
\(\square\)

Thus a synchronized source pair requires one genuinely dual route, not
two independent applications of the proved aperture.

## 4. The root-coordinate obstruction to a local dual aperture

In the boundary-last scan used for the contracted digraph, coordinate

\[
                         r=2m-1
\tag{4.1}
\]

is unpaired and initially has value one.  Every selected scan edge fixes
this root coordinate.

To create the partner condition \(t_{2m}=1\) from a quiet boundary value
\(t_{2m}\in\{0,2\}\) using the nonboundary edge
\(\{2m-1,2m\}\), the unique physical transfer changes

\[
 (t_{2m-1},t_{2m})=(1,0)\longmapsto(0,1)
\tag{4.2}
\]

or

\[
 (t_{2m-1},t_{2m})=(1,2)\longmapsto(2,1).
\tag{4.3}
\]

### Proposition 4.1 (no two-arc same-root dual)

There is no analogue of the proved two-arc forward aperture consisting of
one physical transfer across \(\{2m-1,2m\}\) followed by one selected
edge of the fixed scan and ending at \(\tau(a)\).

#### Proof

The physical transfer in (4.2) or (4.3) changes the unpaired root away
from one.  The following selected scan edge fixes the root.  But
\(\tau(a)\) agrees with \(a\) at every nonboundary coordinate, including
the root, so its root value is one.  The two-arc route cannot end there.
\(\square\)

Any dual aperture must therefore use at least one additional physical
edge incident with the root, or hand the construction to a scan with a
different unpaired root.  This is the exact cross-slice/root-handoff gate.

## 5. Complement pairing: perfect arithmetic, nonlocal physics

The compressed complement

\[
                       C(u)=2-u
\tag{5.1}
\]

pairs every source in \({\cal Q}_m\) except \(1^m\).  It is therefore an
ideal abstract one-socket source matching.

It does not preserve the literal quiet bank of the fixed scan under
coordinatewise digit complement.  Locally,

\[
 00\longleftrightarrow22,
 \qquad 20\longmapsto02,
\tag{5.2}
\]

and \(02\) is active rather than quiet in the chosen mass-two scan phase.
The local reflection-complement

\[
                       (x,y)\longmapsto(2-y,2-x)
\tag{5.3}
\]

does send \(q(u)\) to \(q(2-u)\), but applying (5.3) independently on
every scan pair is not an automorphism of the physical coordinate cycle:
a connector edge between successive pairs is sent to a nonedge.

The parity-perfect permutation

\[
                       J=C R^{2^{v_2(m)}}
\tag{5.4}
\]

therefore remains an excellent source-level target, but realizing it
physically necessarily changes the scan phase or the scan root.  Neither
the complement pairing nor (5.4) is a same-clock corollary of the current
zipper.

## 6. Sharpened frontier

The source-level choices are now exact:

1. recursively use the first-nonquiet matching, whose defect is precisely
   the next central ternary layer; or
2. use complement (or complement-rotation) to pair every source except the
   all-one socket in one step.

Both reduce the labelled current to the same physical lemma:

\[
 \boxed{\text{construct a matching-faithful cross-root dual aperture.}}
\tag{6.1}
\]

The first formulation asks for it only on the scan matching edges and
then recurses.  The second asks for it on complement-dual pairs and avoids
the recursion.  The present forward clock/zipper proves neither, and
Propositions 3.1 and 4.1 show exactly why a same-root local duplication
cannot do so.

## 7. Exact two-phase scan audit

There is nevertheless a macroscopic phase-doubled linkage inside the
contracted digraph.  It shows that the obstruction is concentrated at the
boundary phase rather than throughout the zipper.

On a nonboundary scan pair define two mass-two phases

\[
\begin{array}{c|c|c}
 &\text{selected row}&\text{quiet state}\\ \hline
0&02\leftrightarrow11&20,\\
1&20\leftrightarrow11&02.
\end{array}
\tag{7.1}
\]

The mass-one and mass-three rows are unchanged.  Let \(M_0\) be the
original first-nonquiet scan.  Let \(M_*\) use phase one on every
nonboundary pair but retain phase zero on the physical boundary pair.
Both scans use the same pair order.

For a compressed word \(u\), write \(q_0(u)\) for its original quiet
literal state and \(q_*(u)\) for the state obtained by replacing
\(20\) by \(02\) at every internal digit one, while leaving the boundary
pair unchanged.

### Theorem 7.1 (boundary-locked phase linkage)

The union \(M_0\cup M_*\) contains pairwise vertex-disjoint alternating
paths

\[
                         q_0(u)\leadsto q_*(u)
                         \qquad(u\in{\cal Q}_m).
\tag{7.2}
\]

Relative to the orientation defined by the nonboundary part of \(M_0\),
these paths are directed.  They avoid the deleted endpoint set of the
installed boundary current.  Consequently

\[
                         Q_*:=\{q_*(u):u\in{\cal Q}_m\}
\tag{7.3}
\]

is another explicit basis of the contracted strict gammoid.

#### Proof

The union of two matchings is a disjoint union of alternating paths and
cycles.  Along a component starting at \(q_0(u)\), every pair whose code
is zero or two remains respectively \(00\) or \(22\): the two scans agree
there and neither matching acts.  At an internal code-one position the
component uses only the three-state path

\[
                         20-11-02.
\tag{7.4}
\]

Thus the frozen zero/two positions and the positions of the code-one
digits are invariants of the component.  Within that invariant fibre
there is exactly one endpoint unmatched by \(M_0\), namely \(q_0(u)\),
and exactly one endpoint unmatched by \(M_*\), namely \(q_*(u)\).
They are therefore the two endpoints of the same component.  If there is
no internal digit one, they coincide and the path is trivial.

Different compressed words have different invariant data, so their
components are disjoint.  Starting on the majority shore, an \(M_*\)
edge is nonmatching relative to \(M_0\), and the next \(M_0\) edge is a
matching edge; hence the alternating path is directed in the strict-
gammoid orientation.

The boundary pair is unchanged throughout (7.2) and is quiet in both
scans.  No vertex of the path is therefore an endpoint of an \(M_0\)
edge selected on the physical boundary.  The entire linkage survives the
contraction, proving the basis assertion.  \(\square\)

This basis has a clean complement description.  If \(\overline t=2-t\)
denotes literal digit complement and \(\tau=(0\ \ 2m)\), then

\[
                         q_*(u)=\tau\,\overline{q_0(2-u)}.
\tag{7.5}
\]

The boundary swap is exactly what keeps the boundary mass-two quiet state
equal to \(20\) rather than converting it to \(02\).

### Proposition 7.2 (the full phase double hits the contracted current)

Let \(M_1\) use phase one on the boundary pair as well.  The alternating
component from \(q_0(u)\) to the fully phase-one quiet state meets the
deleted endpoint set whenever the boundary compressed digit \(u_m=1\).
The number of such source components is

\[
             [z^{m-1}](1+z+z^2)^{m-1}.
\tag{7.6}
\]

#### Proof

Changing the boundary local state from \(20\) to \(02\) inside
\(M_0\cup M_1\) necessarily traverses

\[
                         20-11-02.
\tag{7.7}
\]

The edge \(11-02\) is precisely the phase-zero scan edge on the physical
boundary.  When it is selected, its endpoints belong to the installed
boundary-current endpoint set, which was deleted in forming the
contraction.  Conversely, if \(u_m\ne1\), the boundary state is \(00\) or
\(22\) and never changes, so this collision does not occur.  Fixing
\(u_m=1\) leaves total mass \(m-1\) on the other \(m-1\) compressed
digits, giving (7.6).  \(\square\)

Theorem 7.1 is the maximal same-root phase doubling that survives the
installed current.  It creates a large noncanonical basis, but its
boundary pair remains quiet, so it does not yet give the physical pairs
\(a,\tau(a)\).  Proposition 7.2 identifies the exact shared-vertex
obstruction to the naive full complement phase: an exponentially large
boundary-one slice, not a bounded socket bank.  A successful complement-
dual aperture must move that phase change through another root before it
returns to the physical boundary.

## 8. Root-slide parity and the forbidden direct slide

For an odd coordinate cycle of length \(n\), define the cut-open parity
rooted at coordinate \(j\) by

\[
                  \chi_j(t)=\sum_{p=0}^{n-1}p\,t_{j+p}\pmod2.
\tag{8.1}
\]

### Lemma 8.1 (root-slide scalar identity)

If the total mass is \(R\), then

\[
                  \chi_{j+1}(t)-\chi_j(t)
                    \equiv R-t_j\pmod2.
\tag{8.2}
\]

In particular, at odd mass a root slide across a coordinate of value one
preserves the majority shore.

#### Proof

Reindexing the first sum gives

\[
 \chi_{j+1}
  =\sum_{q=1}^{n-1}(q-1)t_{j+q}+(n-1)t_j.
\]

Subtracting \(\chi_j\) yields

\[
 -(R-t_j)+(n-1)t_j=-R+nt_j\equiv R-t_j\pmod2,
\]

because signs agree modulo two and \(n\) is odd.  \(\square\)

This removes a scalar parity objection to sliding a root along a corridor
of literal ones.  It does not say that the corresponding alternating
components avoid the contracted boundary current.

Take the actual root \(r=2m-1\).  The adjacent-root scan leaving
coordinate \(2m\) pairs every other coordinate and omits the coordinate
edge \(\{2m-1,2m\}\).  Its union with the original scan has only one
coordinate-edge support incident with coordinate \(2m\), namely the
physical boundary \(\{2m,0\}\).

### Proposition 8.2 (direct root handoff is fully contracted)

Every alternating component transporting a quiet source from root
\(2m-1\) to root \(2m\) uses an installed phase-zero boundary edge and
therefore meets \(V(P)\).  No such direct adjacent-root transport path
survives in \(D'\).

#### Proof

At a source rooted at \(2m-1\), coordinate \(2m\) is the first coordinate
of a quiet boundary pair and hence is zero or two.  At a quiet endpoint
rooted at \(2m\), that coordinate equals one.  Along the union of the two
scan matchings, the only selected coordinate support capable of changing
coordinate \(2m\) is \(\{2m,0\}\).  Hence the component contains a state
edge of the original scan supported on the physical boundary.  Such an
edge belongs to \(P\), and both its endpoints are deleted in forming
\(D'\).  \(\square\)

Therefore the required root repair cannot be the one-step adjacent-root
bijection.  It must carry the root the long way around the nonwrap
coordinate path, use a different scan phase while the boundary is
internal, and return.  Lemma 8.1 shows that a corridor whose successive
root digits are one has the correct shore parity; the still-open content
is a vertex-disjoint literal realization of that long root-slide chain.

## 9. A raw long-way phase convoy exists

There is no ambient token-graph obstruction to replacing the forbidden
boundary phase edge by a long nonwrap route.  Let

\[
                   v_0,v_1,\ldots,v_L
\tag{9.1}
\]

be a coordinate path with \(L\ge3\).  Consider the two endpoint states

\[
 x=(2,1,\ldots,1,0),
 \qquad
 y=(0,1,\ldots,1,2).
\tag{9.2}
\]

### Theorem 9.1 (two-chip long-way transporter)

There is a simple adjacent-transfer path from \(x\) to \(y\), supported
only on the path edges in (9.1), which never visits the all-one state.

#### Proof

Move one chip from \(v_0\) to \(v_1\), and then from \(v_1\) to
\(v_2\).  Now move the second chip from \(v_0\) to \(v_1\).  The two
extra chips occupy \(v_1,v_2\), while both endpoints have value zero.

Inductively, when the two extra chips occupy \(v_{j-1},v_j\), first move
the front chip from \(v_j\) to \(v_{j+1}\), then move the rear chip from
\(v_{j-1}\) to \(v_j\).  Continue until they occupy
\(v_{L-1},v_L\), and finally move the rear chip into \(v_L\).

Every move inside the corridor enters a coordinate of value one.  The
front chip enters \(v_L\) when it has value zero, and the last move enters
\(v_L\) when it has value one.  Thus all coordinates remain in
\(\{0,1,2\}\).  Because \(L\ge3\), when the second chip leaves \(v_0\)
the front chip is only at \(v_2\), so the terminal \(v_L\) is still zero;
afterward \(v_0\) is zero until the end.  Hence the all-one state never
occurs.  The ordered
positions of the one or two travelling excess chips recover the stage,
so no state repeats.  \(\square\)

Taking \(v_0=2m\), \(v_L=0\), and (9.1) to be the long coordinate path

\[
             2m,2m-1,\ldots,1,0
\]

gives a literal replacement for \(20\to02\) on the physical boundary
without using the boundary edge \(\{2m,0\}\).  It also bypasses the
three-site separator by keeping a second travelling defect alive.

This is an ambient path theorem only.  In a general root-clock terminal,
the long corridor is not all ones, and the fixed scan orientation may
turn some convoy edges the wrong way.  The remaining physical lemma is
therefore narrower than existence of a detour:

\[
 \boxed{\text{prepare a one-valued root corridor and lift the convoy as
 a matching-faithful directed counterflow bank in \(D'\).}}
\tag{9.3}
\]

Lemma 8.1 supplies the shore consistency along such a corridor; Theorem
9.1 supplies the raw boundary-free path.  Corridor preparation and
macroscopic disjoint packing remain open.

The disjointness qualification is essential even before orientation.  On
the four-coordinate path, the canonical all-one-corridor route begins

\[
                         2011\longrightarrow2020.
\tag{9.4}
\]

But \(2020\) is itself the initial endpoint (9.2) for the different
interior background \((0,2)\).  Thus raw convoy paths for different
backgrounds can meet another source immediately.  A macroscopic theorem
must retain a readable private marker or choose the routes jointly; the
single-path construction cannot simply be copied independently for every
quiet source.
