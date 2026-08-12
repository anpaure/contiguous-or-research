# Two-row/two-cut rigidity in a Dyck-port cylinder

Date: 2026-07-26

Method: pure mathematics only.  No finite search, solver, program, or web
input is used.

## 0. Exact outcome

Let

\[
 J=[2s],\qquad \mathcal X=\binom Js,\qquad
 \mathcal Y=\binom J{s+1},\qquad \mathcal D=\mathcal D_s.
\]

Write an exact \(\mathcal D\)-port factor as a partition of the
middle-levels inclusion graph into the rooted paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{s-1}\supset X_s=J\setminus P,qquad P\in\mathcal D.       \tag{0.1}
\]

There are two closely related meanings of a two-row/two-cut move.  Both
are rigid.

1.  If two incidence edges are cut on each of two paths, the noncommon
    boundary is a single alternating \(C_6\) or \(C_8\).  Every
    transplanted old path segment has at most four incidence edges.  Thus
    no long incidence-level reciprocal exchange exists.
2.  If two whole Johnson-state intervals are reciprocally exchanged, the
    exact move is classified by two cancelling seam defects.  Every seam
    is a dipole, a four-colour common-core rectangle, or a four-colour
    octahedral defect.  A forward/forward exchange varies on at most six
    coordinates and has interval width at most four.  Reversing either
    interval still leaves a uniformly bounded atom.

At the root cut, the phase-aligned quota-changing atom is necessarily the
known affine \(J(4,2)\) octahedron.  It changes first deletion and first
insertion histograms in lockstep.  In the canonical MSW factor the only
such atoms at the first two cuts are

\[
                 1100R\longleftrightarrow1010R,
                 \qquad R\in\mathcal D_{s-2}.          \tag{0.2}
\]

Consequently increasing \(s\) adds spectators, not growing two-row
support.  Any new Catalan-scale conveyor must coordinate at least three
strands, more than two cuts on a strand, or several boundary circuits.

## 1. Geodesic and exact-resource preliminaries

Every path in (0.1) has \(2s\) inclusion edges and projects to an
\(s\)-edge Johnson path from \(P\) to \(J\setminus P\).  Its endpoints
have Johnson distance \(s\), so the path and each of its subpaths are
geodesic.  In particular, if \(X_i,X_j\) lie on one rooted row, then

\[
                       d_J(X_i,X_j)=|i-j|.             \tag{1.1}
\]

An exact substitution must preserve both shores literally.  In Johnson
notation this means preservation of the multisets

\[
 \biguplus\{X_t(P)\}=\binom Js,
 \qquad
 \biguplus\{X_t(P)\cup X_{t+1}(P)\}=\binom J{s+1}.    \tag{1.2}
\]

Endpoint pairing is an additional condition: degree preservation alone
may permute complementary tails or create a portless cycle.

## 2. Incidence-edge cuts are bounded circuits

Consider a literal reciprocal reassembly obtained by cutting two
incidence edges on each of two old paths and reconnecting the six
resulting path pieces.  Assume the result is again an exact path factor
with the prescribed two outer port pairs.

### Theorem 2.1 (boundary-circuit classification)

After common edges are cancelled, the changed boundary is one simple
alternating \(C_6\) or \(C_8\) in the inclusion graph \(M(J)\).  If all
four old cut edges really change, it is a \(C_8\).

Every old middle piece transplanted by the reassembly has at most four
incidence edges, hence at most two Johnson transitions.

#### Proof

The old and new factors have the same degree at every \(X\)- and
\(Y\)-vertex.  Their noncommon boundary edges therefore form an
alternating Eulerian graph.  There are at most four old and four new
edges.  The inclusion graph has no \(C_4\): two distinct \(s\)-sets have
at most one common \((s+1)\)-superset.  A nonempty Eulerian component is
therefore a \(C_6\) or a \(C_8\), and there is room for only one component.

The two endpoints of any cut-out old middle piece are vertices of this
boundary cycle.  Their distance in \(M(J)\) is at most four.  The old
piece is a subpath of the geodesic (0.1), so its length equals the graph
distance between its endpoints.  It consequently has at most four
incidence edges.  \(\square\)

This theorem closes the apparently nonlocal version of the reciprocal
two-cut move.  A long displayed middle segment cannot coexist with the
four-edge exact boundary circuit.

## 3. Exact criterion for a Johnson-state interval exchange

Now work in the projected Johnson rows

\[
 A_0,A_1,\ldots,A_s,qquad B_0,B_1,\ldots,B_s.        \tag{3.1}
\]

Cut row \(A\) at \(a<b\), row \(B\) at \(c<d\), and exchange in forward
order the internal state strings

\[
 A_{a+1},\ldots,A_{b-1}quad\hbox{and}\quad
 B_{c+1},\ldots,B_{d-1}.                              \tag{3.2}
\]

Both new paths join complementary ports.  Hence their Johnson lengths
are at least \(s\), while their total length remains \(2s\).  Therefore

\[
                         L:=b-a=d-c.                  \tag{3.3}
\]

Define the signed seam defects

\[
\begin{aligned}
 \delta_\ell={}&e_{A_a\cup A_{a+1}}+e_{B_c\cup B_{c+1}}
 -e_{A_a\cup B_{c+1}}-e_{B_c\cup A_{a+1}},\\
 \delta_r={}&e_{A_{b-1}\cup A_b}+e_{B_{d-1}\cup B_d}
 -e_{A_{b-1}\cup B_d}-e_{B_{d-1}\cup A_b}.
                                                               \tag{3.4}
\end{aligned}
\]

### Theorem 3.1 (necessary and sufficient interval criterion)

The forward exchange (3.2) is an exact anchored substitution if and only
if the four cross pairs

\[
 A_a\sim_J B_{c+1},\quad B_c\sim_J A_{a+1},\quad
 A_{b-1}\sim_J B_d,\quad B_{d-1}\sim_J A_b             \tag{3.5}
\]

are Johnson edges and

\[
                         \boxed{\delta_\ell+\delta_r=0.} \tag{3.6}
\]

#### Proof

The \(X\)-states and every internal adjacent-union colour in the two
exchanged strings are merely permuted.  Only the four boundary
transitions change.  Equation (3.5) is exactly their legality, and (3.6)
is exactly equality of their old and new \(Y\)-multisets.  The outer
shells, the roots, and the complementary endpoints do not move.  These
conditions are therefore both necessary and sufficient.  \(\square\)

## 4. Complete classification of one seam

Let \(L_0,L_1,R_0,R_1\) be four distinct \(s\)-sets such that every
\(L_i\) is Johnson-adjacent to every \(R_j\).  Put

\[
 \delta=e_{L_0\cup R_0}+e_{L_1\cup R_1}
       -e_{L_0\cup R_1}-e_{L_1\cup R_0}.              \tag{4.1}
\]

Because \(R_0\) is a common neighbour,
\(d_J(L_0,L_1)\le2\).  Equality zero is excluded by exact \(X\)-ownership.

### Theorem 4.1 (seam normal forms)

Exactly one of the following occurs.

1. **Distance two.**  There are an \((s-2)\)-set \(C\) and distinct
   \(a,b,c,d\notin C\) with
   \[
       L_0=Cab,\qquad L_1=Ccd.                         \tag{4.2}
   \]
   Each \(R_j\) chooses one element of \(\{a,b\}\) and one of
   \(\{c,d\}\).  Adjacent choices give a dipole \(e_Y-e_{Y'}\);
   opposite choices give the four-facet octahedral defect.  All states
   lie in \(C\cup\{a,b,c,d\}\).
2. **Distance one.**  There are an \((s-1)\)-set \(H\) and distinct
   \(a,b\notin H\) with
   \[
                      L_0=Ha,\qquad L_1=Hb.            \tag{4.3}
   \]
   Every common neighbour is either
   \[
        O(c)=Hc\quad(c\notin H\cup\{a,b\}),
        \qquad I(h)=(H-\{h\})ab\quad(h\in H).         \tag{4.4}
   \]
   Two outside states give the four-colour rectangle
   \[
       e_{Hac}+e_{Hbd}-e_{Had}-e_{Hbc}.                \tag{4.5}
   \]
   One inside and one outside state give a dipole.  Two inside states
   give \(\delta=0\), but then both old edges own the same colour
   \(Hab\), which is impossible in an exact factor.

#### Proof

For distance two write the disjoint differences of \(L_0,L_1\) as
\(\{a,b\}\) and \(\{c,d\}\).  A common Johnson neighbour must retain
their common \((s-2)\)-core and select one element from each difference.
The two-by-two grid gives the two stated defects by direct union.

For distance one, write (4.3).  A common neighbour either retains all of
\(H\), in which case it is \(Hc\), or contains both \(a,b\), in which
case it must omit one \(h\in H\).  Direct union gives (4.5), the dipole,
and the zero case.  This exhausts the common-neighbour list.  \(\square\)

## 5. Uniform support bound

### Theorem 5.1 (no growing forward rectangle)

Every legal forward/forward two-row/two-cut exchange is a suspension of a
trade on at most six genuinely varying coordinates.  Its interval width
satisfies

\[
                              \boxed{L\le4.}           \tag{5.1}
\]

Thus at most three internal \(X\)-states per row are exchanged.

#### Proof

Exactness excludes a zero seam, so (3.6) says that the two nonzero seam
defects are negatives of the same signed vector.

For a dipole, its two \((s+1)\)-colours have union of size \(s+2\).
Each realizing seam has only the two visible dipole labels and a
two-label hinge; the hinges at the two ends may differ.  Hence at most
six labels vary in the whole trade.  The two inner endpoints lie in one
\((s+2)\)-set, so their Johnson distance is at most two.

For an octahedral four-colour defect, its support fixes the common
\((s-2)\)-core and four active labels.  The same is true at both seams.
For the outside/outside rectangle, its support fixes the common
\((s-1)\)-core and four active labels; its inner seam states have the form
\(H+x\) and hence distance at most one.

The inner part of row \(A\) from \(A_{a+1}\) to \(A_{b-1}\) is a
geodesic of length \(L-2\).  The preceding bounds give \(L-2\le2\) in
the dipole and octahedral cases and \(L-2\le1\) in the outside/outside
case.  No geodesic introduces a coordinate outside the union of its
endpoints.  This proves both assertions.  \(\square\)

Reversing one or both exchanged strings does not open a growing regime.

### Lemma 5.2 (orientation audit)

A reciprocal reassembly of the two strings in arbitrary orientations has

\[
\begin{array}{c|c}
\text{orientation}&\text{maximum }L\\ \hline
\text{forward/forward}&4\\
\text{forward/reverse or reverse/forward}&4\\
\text{reverse/reverse}&3\\
\text{self-reversal}&2.
\end{array}                                             \tag{5.2}
\]

#### Proof

Write

\[
 A=A_a,\ A'=A_{a+1},\ C=A_{b-1},\ E=A_b
\]

and similarly \(B,B',D,F\) on the second row.  The four old boundary
colours are

\[
                         AA',\ BB',\ CE,\ DF,          \tag{5.3}
\]

where juxtaposition denotes union.

For reverse/reverse exchange the new colours are

\[
                         AD,\ BC,\ B'E,\ A'F.          \tag{5.4}
\]

If \(L\ge4\), geodesicity makes the two endpoints of each reversed old
string too far apart to share a colour.  The only possible colour
bijection therefore has

\[
                         \{AD,A'F\}=\{AA',DF\}.        \tag{5.5}
\]

In the direct pairing the two colours in (5.5) both contain the distinct
\(s\)-sets \(A',D\), forcing them to be the same \((s+1)\)-set.  In the
crossed pairing the same argument uses \(A,F\).  Either conclusion repeats
an old \(Y\)-colour, impossible in an exact factor.  Hence \(L\le3\).

For a mixed exchange, with the \(B\)-string forward and the \(A\)-string
reversed, the new colours are

\[
                         AB',\ BC,\ DE,\ A'F.          \tag{5.6}
\]

For \(L\ge4\), an equality between one of (5.6) and one of (5.3) must
match an endpoint on the same side; otherwise it would place two
Johnson-distance-at-least-two states in one \((s+1)\)-set.  Following
these forced endpoint incidences around the four colours leaves only the
identity pairing and one cyclic shift.  The cyclic shift puts \(A,B\) in
one \((s+1)\)-set, contradicting
\(d_J(A,B)\ge L-2\ge2\).  Under the identity pairing,
\(A',B',C,D\) form a Johnson four-cycle, so

\[
                         L-2=d_J(A',C)\le2.            \tag{5.7}
\]

Thus \(L\le4\).  The other mixed orientation is symmetric.  Finally a
self-reversed string needs \(A_a\sim_JA_{b-1}\).  Geodesicity gives
\(d_J(A_a,A_{b-1})=L-1\), hence \(L\le2\).  \(\square\)

The mixed cases are fixed-base suspensions on at most twenty varying
coordinates; the forward case has the sharp six-coordinate bound.  The
only fact used later is the uniformity in \(s\).

## 6. First-edge quota action

Write the first Johnson exchange on a rooted row as

\[
             X_1=X_0-\{a_1\}+\{b_1\}.                \tag{6.1}
\]

Let \(D(j)\) and \(I(j)\) be the first-deletion and first-insertion
histograms.  For a phase-zero two-row assignment swap,

\[
\begin{aligned}
 \Delta I={}&e_{R_1\setminus L_0}+e_{R_0\setminus L_1}
             -e_{R_0\setminus L_0}-e_{R_1\setminus L_1},\\
 \Delta D={}&e_{L_0\setminus R_1}+e_{L_1\setminus R_0}
             -e_{L_0\setminus R_0}-e_{L_1\setminus R_1}.
                                                               \tag{6.2}
\end{aligned}
\]

The incidence identity

\[
 \mathbf1_{R_0}+\mathbf1_{R_1}-\mathbf1_{L_0}-\mathbf1_{L_1}
       = I_{\rm old}-D_{\rm old}=I_{\rm new}-D_{\rm new}       \tag{6.3}
\]

implies

\[
                              \boxed{\Delta I=\Delta D.}       \tag{6.4}
\]

The seam normal forms sharpen this as follows.

* outside/outside gives zero aggregate first-edge motion;
* a dipole gives a unit transfer \(e_z-e_y\);
* the opposite distance-two square gives a two-for-two vector such as
  \(e_a+e_d-e_b-e_c\).

For a one-phase, two-adjacent-cut move, exactness forces the six-state
octahedron

\[
\begin{array}{c|ccc}
\text{old }P&Kxy&Kxw&Kzw\\
\text{old }Q&Kxz&Kyz&Kyw
\end{array}
\quad\longmapsto\quad
\begin{array}{c|ccc}
\text{new }P&Kxy&Kyz&Kzw\\
\text{new }Q&Kxz&Kxw&Kyw.
\end{array}                                             \tag{6.5}
\]

Its exact quota action is

\[
                         \Delta I=\Delta D=e_z-e_y.    \tag{6.6}
\]

In the canonical MSW first two cuts, recursion forces precisely (0.2).
The corresponding root graph is a disjoint matching with \(C_{s-2}\)
edges.  Choosing \(n\) of them gives

\[
             \Delta I=\Delta D=n(e_3-e_2),
             \qquad 0\le n\le C_{s-2}.                \tag{6.7}
\]

The active-root fraction and maximum transferred fraction are exactly

\[
 \frac{2C_{s-2}}{C_s}\longrightarrow\frac18,
 \qquad
 \frac{C_{s-2}}{C_s}\longrightarrow\frac1{16}.        \tag{6.8}
\]

There are no other canonical first-two-cut rectangles.

## 7. A universal endpoint invariant

Although middle coordinates can move, every exact \(\mathcal D_s\)-port
factor has one rigid extreme quota.

### Theorem 7.1

Exactly \(C_{s-1}\) rows insert coordinate \(2s\) first.  They are
exactly the rows which delete coordinate \(1\) last:

\[
 \boxed{\#\{P:b_1(P)=2s\}=C_{s-1}.}                   \tag{7.1}
\]

#### Proof

Every Dyck root contains \(1\) and omits \(2s\).  In one row let \(u\)
be the insertion time of \(2s\), and \(d\) the deletion time of \(1\).
The number of its \(X\)-states containing both coordinates is
\((d-u)_+\).  The number of its \(Y\)-states containing both is
\(d-u+1\) when \(u\le d\), and zero otherwise.  Exact ownership gives

\[
 \sum(d-u)_+=\binom{2s-2}{s-2}=(s-1)C_{s-1},          \tag{7.2}
\]

and, after subtracting the two shore counts,

\[
 \#\{u\le d\}
 =\binom{2s-2}{s-1}-\binom{2s-2}{s-2}=C_{s-1}.        \tag{7.3}
\]

Every one of these \(C_{s-1}\) rows has \(d-u\le s-1\), while their
sum is \((s-1)C_{s-1}\).  Equality forces \(u=1,d=s\) on every counted
row.  This proves (7.1).  \(\square\)

No analogous conservation law holds for the middle pair \(\{2,3\}\):
the audited complete \(D_4\) replacement changes its first-insertion
counts from \((5,2,2)\) to \((5,1,3)\).  That replacement is a fourteen-row
factor substitution, not a completed two-row atom.

## 8. Proved boundary

The two-row/two-cut lane is closed as a source of growing support.
First-edge quotas can move, but only through bounded finite-coordinate
atoms, and the canonical first-cut family is exactly the leaf matching.

This does not rule out:

* a positive-density packing of many bounded atoms at separated cuts;
* a three-or-more-strand alternating circuit;
* more than two cuts on one strand; or
* a coordinated packet whose several boundary circuits cancel monodromy.

Those are genuinely different mechanisms.
