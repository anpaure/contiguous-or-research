# Odd current: complement already gives the sharp one-socket pairing

**Date:** 2026-08-06  
**Method:** exact endpoint algebra and last-intersection bookkeeping; no
computation or search  
**Status:** unconditional reduction.  The rotation in the previously
proposed source permutation is unnecessary.  Literal complement by itself
gives the required one-socket source matching and is compatible with the
coordinate-zero aperture.  The remaining physical theorem is a directed
dual-aperture-to-partner linkage, with one bounded boundary-one phase
collar.  No existence of that collar is claimed here.

## 1. Setup

At central odd mass put

\[
 Q={\cal T}_{m,m}
   =\{u\in\{0,1,2\}^m:\sum_i u_i=m\}.
\tag{1.1}
\]

Write

\[
                  \mathsf c u=2-u
\tag{1.2}
\]

for compressed complement.  Let

\[
             P_u:q_0(u)\leadsto A(u),\qquad u\in Q,
\tag{1.3}
\]

be the proved pairwise-disjoint aperture linkage from
`MATH_THEOREM_ODD_QUIET_SOURCE_CLOCK_MINOR_AND_BOUNDARY_HANDOFF_GATE_20260806.md`.
Thus every terminal satisfies

\[
                         A(u)_0=1.
\tag{1.4}
\]

Let \(\tau=(0\ \ 2m)\) be the physical boundary transposition and put

\[
                         b(u)=\tau A(u).
\tag{1.5}
\]

Literal complement on physical states is denoted by a bar.  Define the
boundary-swapped complement

\[
                         \Gamma=\tau\,\overline{\phantom{x}}
\tag{1.6}
\]

and the **dual aperture endpoint**

\[
             \boxed{A_*(u)=\Gamma A(\mathsf c u)
                         =\tau\overline{A(\mathsf c u)}.}
\tag{1.7}
\]

The target partner is \(b(u)=\tau A(u)\).  Hence the exact endpoint
problem after the global complemented sweep is

\[
                         A_*(u)\leadsto b(u).
\tag{1.8}
\]

## 2. Complement is already the parity-perfect permutation

### Theorem 2.1 (sharp complement involution)

The permutation \(\mathsf c\) of \(Q\) has exactly one odd orbit.  It is
the fixed point

\[
                         \mathbf1=(1,\ldots,1).
\tag{2.1}
\]

Every other orbit has length two.

#### Proof

If \(\mathsf c u=u\), then \(2-u_i=u_i\) for every coordinate, so
\(u_i=1\) for every \(i\).  Conversely \(\mathbf1\) is fixed.  Since
\(\mathsf c^2=1\), every nonfixed orbit has length two.  \(\square\)

Thus the rotation in
\(\mathsf cR^{2^{v_2(m)}}\) is not needed for the socket count.  It can
still be useful as a geometric routing aid, but it is not part of the
weakest sufficient last-intersection theorem.

Literal complement also preserves the coordinate-zero aperture
hyperplane:

\[
                         x_0=1\quad\Longrightarrow\quad
                   \overline{x}_0=1.
\tag{2.2}
\]

Thus using \(\mathsf c\) as the source permutation does not require
moving the aperture coordinate.  The boundary swap \(\tau\) enters only
because the requested sink is the physical partner \(b(u)\).

### Theorem 2.2 (punctured complement counterflow criterion)

Choose a transversal \(I\) containing one member of every two-element
complement orbit in \(Q\setminus\{\mathbf1\}\).  Suppose that for every
\(u\in I\) there is a directed path \(R_u\) such that

1. \(R_u\) starts for the last time on \(P_{\mathsf c u}\) and ends at
   \(b(u)=\tau A(u)\);
2. after that last intersection, \(R_u\) is disjoint from every path
   \(P_v\); and
3. the paths \(R_u\), \(u\in I\), are pairwise vertex-disjoint.

Then the odd paired-basis gate closes with exactly one socket, namely the
terminal \(A(\mathbf1)\).

#### Proof

The complement pairs form a matching on
\(Q\setminus\{\mathbf1\}\).  For each \(u\in I\), retain the original
source path \(P_u\) to \(A(u)\), and splice the prefix of
\(P_{\mathsf c u}\) at its last intersection with \(R_u\), ending at
\(b(u)\).  Conditions 1--3 make the resulting linkage vertex-disjoint.
Its terminal set is

\[
 \{A(u),b(u):u\in I\}\ \dot\cup\ \{A(\mathbf1)\}.
\tag{2.3}
\]

It therefore consists of complete boundary pairs plus one socket and is
a surplus basis.  Equivalently, its counterflow support graph is the
perfect matching formed by the complement pairs, with the unique fixed
point unmatched.  The exact deficiency is one.  \(\square\)

This is weaker than constructing a deterministic counterflow for every
ordered sink: only one orientation of each complement pair is needed.

## 3. Exact boundary algebra of the dual aperture

Put

\[
 \beta(t)=\begin{cases}0,&t=0,\\2,&t=1,2.\end{cases}
\tag{3.1}
\]

### Lemma 3.1 (boundary label of the proved aperture)

For every \(u\in Q\), the ordered physical boundary pair
\((2m,0)\) at the aperture terminal is

\[
                         A(u)_{(2m,0)}=(\beta(u_m),1).
\tag{3.2}
\]

#### Proof

Before the aperture extension the boundary pair is the quiet code
\(q_0(u_m)\).  Its first entry is \(\beta(u_m)\).  The deterministic
internal activation and zipper do not use either boundary coordinate.
The aperture extension changes coordinate zero to one and does not
change coordinate \(2m\).  This gives (3.2), including the two direct
branches of the aperture theorem.  \(\square\)

### Corollary 3.2 (only the boundary-one row disagrees)

The dual endpoint and desired partner have boundary pairs

\[
 \begin{aligned}
 A_*(u)_{(2m,0)}
    &=(1,\,2-\beta(2-u_m)),\\
 b(u)_{(2m,0)}
    &=(1,\,\beta(u_m)).
 \end{aligned}
\tag{3.3}
\]

They agree for \(u_m=0\) and \(u_m=2\).  For \(u_m=1\), they are
respectively

\[
                         10\quad\hbox{and}\quad12.
\tag{3.4}
\]

#### Proof

On an ordered boundary pair, \(\Gamma\) is

\[
                         (x,y)\longmapsto(2-y,2-x).
\tag{3.5}
\]

Apply (3.5) to (3.2) with \(u\) replaced by \(2-u\), and compare with
the swap of (3.2).  Direct substitution of \(u_m=0,1,2\) proves the
last assertion.  \(\square\)

Corollary 3.2 is only a statement about the physical boundary pair.  It
does not assert that the interior coordinates of \(A_*(u)\) and \(b(u)\)
already agree.  Those coordinates carry the dual scan phase and the
zipper records and must be restored by the directed reflected sweep.

## 4. Why \(\Gamma\), rather than complement alone, is the natural lift

Let \(M_0\) be the original phase-zero first-nonquiet scan and let
\(M_*\) use phase one on every internal mass-two row while keeping phase
zero on the physical boundary row.

### Proposition 4.1 (exact scan conjugacy, but not fixed-current symmetry)

The physical involution \(\Gamma=\tau\overline{\phantom{x}}\) satisfies

\[
                         \Gamma M_0\Gamma^{-1}=M_*.
\tag{4.1}
\]

It preserves the three **local boundary rows**.  It does not, in general,
preserve the installed first-nonquiet boundary-current edge set, because
it changes the internal quiet phase.  On quiet sources,

\[
                   \boxed{\Gamma q_0(\mathsf c u)=q_*(u).}
\tag{4.2}

#### Proof

On an internal pair, \(\tau\) acts trivially and literal complement
interchanges the mass-one and mass-three selected rows.  It maps the
phase-zero mass-two row

\[
                         02\leftrightarrow11
\]

to the phase-one row

\[
                         20\leftrightarrow11.
\]

On the physical boundary pair, \(\Gamma\) is the reflected complement
(3.5).  It interchanges the selected mass-one and mass-three rows and
fixes the selected mass-two row setwise.  Hence the boundary phase and
all three local boundary rows are preserved.  At every earlier internal
pair, phase-zero quiet states are sent to phase-one quiet states, so the
first-nonquiet index is preserved after the phase change.  This proves
(4.1).

For an internal quiet code, (4.2) is the literal table

\[
  q_0(2)\mapsto00,\qquad q_0(1)=20\mapsto02,
       \qquad q_0(0)\mapsto22.
\]

At the boundary, the extra swap keeps the code-one state equal to
\(20\), exactly as in the definition of \(q_*\).  \(\square\)

If \(P_0\) is the installed boundary-current set for \(M_0\), then

\[
                         \Gamma(P_0)=P_*,
\tag{4.3}
\]

where \(P_*\) is the boundary-current set obtained when the earlier
internal pairs are tested with phase-one quietness.  Usually
\(P_*\ne P_0\): an internal code-one prefix is \(20\) for \(P_0\) and
\(02\) for \(P_*\).  Thus one may not apply \(\Gamma\) to a proved path
and infer that its image survives the original contraction.  Avoidance
of \(V(P_0)\) is a separate, load-bearing part of the two-root collar.

Here (4.1) is a conjugacy of the **scan matching edge sets**.  The
coordinate transposition \(\tau=(0\ \ 2m)\) is not an automorphism of
the full nonwrap coordinate path (it sends, for example, the edge
\(\{0,1\}\) to a nonedge).  Consequently (4.1) is not a license to map
arbitrary directed paths by \(\Gamma\).

This proposition identifies the true remaining directedness issue.
Applying \(\Gamma\) to a phase-zero construction produces a phase-one
internal construction; it is not automatically a directed construction
in the original phase-zero contraction.  The boundary-locked phase
linkage and the reflected zipper give the required macroscopic state
space, but a two-root clock junction must orient the return linkage.

## 5. Reordering and terminal collars cannot fake the source permutation

### Proposition 5.1 (last-intersection conjugacy invariant)

Suppose an ambient automorphism \(g\) sends an indexed source linkage
\(P_u\) to another indexed source linkage \(P'_{\sigma u}\).  If a
counterflow family has last-intersection permutation \(\pi\), its image
under \(g\) has last-intersection permutation

\[
                         \sigma\pi\sigma^{-1}.
\tag{5.1}
\]

In particular, changing the scan root or scan order can conjugate a
genuine source permutation, but it cannot turn the identity into
complement.  Conjugacy also preserves the number of odd cycles.

#### Proof

The route indexed by \(u\) last meets \(P_{\pi(u)}\).  Its image, indexed
by \(\sigma u\), last meets \(P'_{\sigma\pi(u)}\).  This is exactly
(5.1).  The remaining statements are elementary properties of conjugate
permutations.  \(\square\)

### Proposition 5.2 (terminal-only collar obstruction)

Let \(K_u\) be a family of collars beginning at \(A(u)\), and suppose
that after leaving \(A(u)\), \(K_u\) is disjoint from every original
source path \(P_v\).  Then the last-intersection permutation of the
family is the identity, regardless of its terminal labels.

Consequently a route \(A(u)\leadsto\tau A(u)\), even if perfectly marked
and pairwise disjoint, cannot close the odd paired-basis gate.  To realize
complement, the route for sink \(u\) must literally start for the last
time on \(P_{\mathsf c u}\), or else cross that path later.

#### Proof

The last vertex of the original linkage met by \(K_u\) is its initial
vertex \(A(u)\in P_u\).  The disjointness hypothesis excludes every
later meeting.  Thus \(\pi(u)=u\) for every \(u\).  \(\square\)

There is also a fixed-point warning.  A globally complement-equivariant
aperture satisfying

\[
                         A(\mathsf c u)=\overline{A(u)}
\tag{5.2}
\]

would force \(A(\mathbf1)\) to be the literal all-ones state.  This is
incompatible with the proved aperture normal form (3.2), whose boundary
pair is always \(01\) or \(21\).  The unique fixed source must therefore
be treated as the socket; complement covariance is needed, at most, on
the punctured set \(Q\setminus\{\mathbf1\}\).

## 6. Exact disjointness interface supplied by the ternary zipper

The endpoint identity alone is not enough: Theorem 2.2 requires literal
last intersections and disjoint route interiors.  The existing marker
theorem reduces this to a bounded collar check.

### Theorem 6.1 (marked complement-counterflow reduction)

Fix a complement transversal \(I\).  Suppose that for each \(u\in I\)
one constructs a route from \(A(\mathsf c u)\) to \(b(u)\) with the
following form.

1. Immediately after \(A(\mathsf c u)\), the root-buffered handoff
   changes a root coordinate from one to a flag in \(\{0,2\}\).
2. Until a bounded terminal collar, the route is a delimiter-equipped
   ternary zipper with reversible tail work as in the tagged
   time-expansion lemma, and the flagged root is not touched.
3. Every nonterminal state of the terminal collar either retains that
   root flag or retains a counterflow-only delimiter from which
   \((u,\text{stage})\) is recovered.
4. The terminal collar ends at \(b(u)\), meets no original aperture path,
   and its states for distinct \(u\) have distinct decoded signatures.

Then all these counterflow routes are pairwise vertex-disjoint, and after
their initial vertices they avoid every original aperture path.  Hence
they satisfy Theorem 2.2 and close the odd current with one socket.

#### Proof

Every vertex of every original promotion/aperture path has the unpaired
root coordinate equal to one: none of the activation, zipper, or
coordinate-zero aperture moves touches that root.  During the long
counterflow interior the root flag is zero or two, so no such vertex lies
on an original path.

At every majority-shore zipper vertex, the first clock, its records, the
delimiter, the untouched suffix and the prescribed local time recover
the unique source \(\mathsf c u\), hence \(u\), and the route stage.
Every minority vertex is the unique scan mate of its following majority
vertex.  Thus two long interiors cannot meet.  Hypothesis 3 extends the
same decoding through every nonterminal collar state, and Hypothesis 4
handles the terminal endpoints and excludes a new intersection with the
old linkage.  Therefore the routes are mutually disjoint and their only
intersections with the old linkage are the prescribed initial terminals
\(A(\mathsf c u)\).  Apply Theorem 2.2.  \(\square\)

The root flag therefore proves the global matching-faithfulness once the
bounded terminal collar is written down.  No separate macroscopic
packing theorem is needed for the complement pairs.

## 7. The exact remaining bounded theorem

The source rotation and a full deterministic permutation bank are no
longer required.  A sufficient remaining statement is:

> **Complement-dual two-root collar.**  For one orientation of every
> complement pair, start at \(A(\mathsf c u)\), perform the marked
> complemented sweep to the dual endpoint \(A_*(u)\), orient the
> phase-one-to-phase-zero return with a second root/clock, and finish at
> \(b(u)=\tau A(u)\).  Preserve the root/delimiter signature until the
> last step and satisfy the four collar conditions in Theorem 6.1.

The literal endpoint discrepancy at the physical boundary is already
known exactly: it vanishes for boundary digits zero and two and is
\(10\to12\) for boundary digit one.  Because \(\Gamma\) preserves the
local boundary rows but sends the installed current \(P_0\) to the
different current \(P_*\), the collar must also avoid \(V(P_0)\).  This
is a phase-direction/contraction problem, not a new boundary-colour or
cycle-parity problem.

What remains open is the directed realization of that collar in the
fixed phase-zero contraction, together with its collision-free terminal
restoration.  Complement alone settles the source permutation and socket
count; scan reordering and a terminal-only collar cannot substitute for
the required cross-source last intersection.

Equivalently, the exact remaining predicate is the existence of a
complement transversal \(I\) and paths

\[
 R_u:A(\mathsf c u)\leadsto \tau A(u)\qquad(u\in I)
\tag{7.1}
\]

in the fixed digraph \(D'=D(M_0)-V(P_0)\), such that

\[
 R_u\cap\Bigl(\bigcup_{v\in Q}P_v\Bigr)
       =\{A(\mathsf c u)\},
 \qquad
 R_u\cap R_v=\varnothing\quad(u\ne v).
\tag{7.2}
\]

The marked zipper proves (7.2) throughout the flagged macroscopic
interiors.  The unproved part is precisely a bounded entry/exit collar
which (a) converts the root-adjacent clock to the reflected phase and
back, (b) stays outside \(V(P_0)\), including the boundary-one row, and
(c) retains an injective counterflow signature until the final partner.
