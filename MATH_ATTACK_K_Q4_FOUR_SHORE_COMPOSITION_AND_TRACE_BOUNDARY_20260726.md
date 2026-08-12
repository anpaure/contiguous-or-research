# The \(Q_4\) four-shore seed: composition law and exact trace boundary

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
                         A=(1\ 3),\qquad B=(2\ 4).
\tag{0.1}
\]

The four local shores

\[
                         I,\ A,\ B,\ AB
\tag{0.2}
\]

are genuine exact \(C_8\)-factors on the same sixteen owners.  The
opposite relative permutation

\[
                         AB=(1\ 3)(2\ 4)
\tag{0.3}
\]

is fixed-point-free.  Consequently this seed removes, on the local
quartet, the hypothesis used by the earlier trace obstruction that every
available opposite shore fixes at least half the directions.  None of the
proved growing atlases removes that hypothesis globally.

Throughout, “fixed-point-free” refers to the relative permutation
\(AB\) of direction labels, not to the fixed-vertex set of a neighbour
map \(G_S\).

It does not remove the full trace obstruction.

There are five exact composition statements.

1. The four shores do **not** automatically suspend with the
   arbitrary-\(k\) carrier.  Their common phase is only modulo four, while
   the standard coloured-cycle suspension needs a common rooted
   \(\mathbb Z_8\) phase.  A separate pair-clustered completion is
   required.
2. On a larger syndrome row-label space, simultaneous row-dependent
   \(A\)- and \(B\)-bits are not a Cartesian four-way switch.  On every
   four-label plane exactly twelve of the sixteen formal pair-field states
   are owner-legal.
3. In the interlaced \(Q_4\) geometry, the same-owner \(AB\) relation
   retains the four plane-constant charts.  These give
   \(2^{N/2}\) local-\(AB\) double-factor states for one embedded
   quartet and \(2^{2^h/32}\) states in the guaranteed \(h/8\)-quartet
   atlas.  In the nested endpoint geometry, all twelve legal charts have
   a unique local fixed-point-free \(AB\)-partner, giving
   \(12^{2^h/64}\) ordered double-factor states.  Both proved growing
   atlases still fix all odd directions.
4. The arbitrary overlapping syndrome braid remains an exact
   frame-changing network with \(N(1-2^{-r})\) independent bits on an
   \(r\)-edge adjacent chain, asymptotically one bit per syndrome cycle.
   But bitwise local opposition across two
   noncommuting layers has relative words \(\tau_2\tau_1\) and
   \(\tau_1\tau_2\), so it does not define one fixed global shore.
5. The one-bit \(Q_4\) banks admit a literal
   \(h/4\)-layer owner-overlapping composition with

   \[
                            {2^h\over16}
   \tag{0.4}
   \]

   independent physical bits and changed-tail density \(1/2\).  Thus
   owner/factor composition at linear information rate is positive.

For a composition which uses only this four-shore cube in one frame, the
surviving obstruction is a fixed-wire invariant.  Every shore in
\(\langle A,B\rangle\) preserves

\[
                         \{1,3\}\mid\{2,4\}.
\tag{0.5}
\]

For any fixed-wire composition generated from one fixed base cyclic order
on \(h\) directions, the complete support library at depth \(d\) has size
at most \(h2^d\), and the aligned trace code has distinct-code proportion
at most

\[
                         \boxed{{2h\over2^d}.}
\tag{0.6}
\]

Hence its collision proportion tends to one whenever
\(d-\log_2h\to\infty\), including the Gaussian protected regime.
No second transverse perfect-matching layer exists in the same \(Q_4\)
phase colouring.  Moreover, bitwise complementation through a
noncommuting sorting braid does not define one fixed global shore.  A
cross-colouring common-owner trade, a frame-changing \(Q_8\) or larger
associator, or a new palindromic partner identity is still needed.

Thus the answer is:

* **yes** to literal composition and linear information rate inside the
  audited syndrome multilayer;
* **yes** to removal of the old fixed-direction hypothesis locally on one
  quartet, but **no** for the proved growing atlases, which retain fixed
  direction density at least \(1/2\);
* **no** to a generic arbitrary-\(k\)-carrier suspension from the stated
  local interface; and
* **no** to removal of the occurrence-resolved trace obstruction by the
  \(A/B\) cube alone.

## 1. The local four-shore cube

Let \(Q:\mathbb F_2^4\to\mathbb F_2^2\) have columns

\[
 Qe_1=Qe_3=\alpha,\qquad Qe_2=Qe_4=\beta.
\tag{1.1}
\]

Let \(\delta_0(x)\in[4]\) be the standard outgoing direction determined
by \(Qx\), in the cyclic syndrome order

\[
                         1,2,3,4.
\tag{1.2}
\]

For \(S\in\langle A,B\rangle\), put

\[
                         G_S(x)=x+e_{S\delta_0(x)}.
\tag{1.3}
\]

Both \(A\) and \(B\) interchange equal syndrome columns.  Therefore

\[
                         Qe_{Su}=Qe_u
\qquad(S\in\langle A,B\rangle).
\tag{1.4}
\]

The syndrome trajectory of every \(G_S\) is the same four-cycle as that
of \(G_I\).  Its first four directions are

\[
                         S(1),S(2),S(3),S(4),
\tag{1.5}
\]

all four directions once, and the next four repeat them.  Hence

\[
                         G_S^4x=x+\mathbf1,\qquad
                         G_S^8x=x.
\tag{1.6}
\]

Every orbit is therefore an isometric \(C_8\), and the orbits partition
all sixteen owners.  The four direction words are

\[
\begin{array}{c|c}
I&1234\,1234\\
A&3214\,3214\\
B&1432\,1432\\
AB&3412\,3412.
\end{array}
\tag{1.7}
\]

The syndrome phase \(c_4(x)\in\mathbb Z_4\) is common to all shores, and
(1.6) is the common half-cycle port.  This is weaker than one common
rooted \(\mathbb Z_8\) colouring and is not, by itself, enough for the
standard common-phase suspension.

In fact the bare cube has no common \(\mathbb Z_8\) refinement.  To see
this, suppose that \(c:Q_4\to\mathbb Z_8\) increased by one on every
shore.  Modulo four, \(c-c_4\) is invariant under every shore edge.  The
union of the four shore graphs contains every edge of \(Q_4\), so it is
connected; after adding a constant we may therefore write

\[
                         c(x)=c_4(x)+4r(x),
             \qquad r(x)\in\mathbb F_2.             \tag{1.8}
\]

On syndrome phase zero, the two allowed first moves are \(e_1,e_3\).
Thus \(r\) is unchanged by either move and is invariant under
\(e_1+e_3\) on that phase fibre.  On the next fibre the two allowed moves
are \(e_2,e_4\); hence \(r\) is also invariant under
\(e_2+e_4\).  It follows successively that \(r\) is constant on each of
the four syndrome fibres, with the same constant through the first three
phase transitions.  The last transition, from phase three to phase zero,
would have to change \(r\) by one because \(3+1=4\) in \(\mathbb Z_8\).
This is a contradiction.  Thus the missing phase refinement is an
intrinsic interface failure, not merely an omitted choice of roots.

At the same owner \(x\), the outgoing directions on shores \(I\) and
\(AB\) are related by the fixed-point-free permutation (0.3).  The same
relation holds for incoming directions after shifting one common phase
back.  Thus the local pair is a genuine same-vertex double factor.

## 2. The arbitrary-\(k\) carrier interface is not automatic

The arbitrary-\(k\) carrier has a genuinely common cyclic phase for all
of its local factor corners.  The four \(Q_4\) shores have only the
coarser datum

\[
                         c_4(G_Sx)=c_4(x)+1,
\qquad G_S^4x=x+\mathbf1.
\tag{2.1}
\]

There is, in general, no one \(\mathbb Z_8\) owner colouring cyclic on all
four shores.  The standard \(C_{2n}\) coloured-cycle suspension
distinguishes first-half phases \(1,2,3\) from antipodal phases
\(5,6,7\) when assigning tail fibres.  A common \(\mathbb Z_4\) class and
the common half-port do not determine that distinction.  Therefore:

### Proposition 2.1 (phase-interface obstruction)

The existing common-phase suspension theorem cannot be invoked to compose
the \(I,A,B,AB\) shore cube with the arbitrary-\(k\) carrier.  Such a
composition requires either

1. an explicit common \(\mathbb Z_8\) refinement, which the bare shore
   cube does not possess; or
2. a separately proved pair-clustered/doubled lift specifying the owner
   fibre over both members of every antipodal phase pair.

The nonlinear parity-complete \(Q_8\) construction in the source theorem
is an example of a special additional completion, not a consequence of
the generic suspension interface.

The syndrome multilayer constructions in Sections 3--4 avoid this gap:
they are built directly as exact \(C_{2h}\)-factors by phasewise Latin
owner maps.  Thus the two-bit primitive composes inside that explicit
outer syndrome carrier.  Its insertion into the arbitrary-\(k\) carrier
remains conditional on writing the missing pair-clustered fibre.

More precisely, the arbitrary-\(k\) theorem suspends genuinely
four-phased \(Q_2\) cells.  The bare \(Q_4\) colour \(c_4\) is two-to-one
on each \(C_8\), so substituting the four-shore cube would leave the two
antipodal occurrences of every colour unresolved.  For a proper growing
syndrome embedding, a valid plug would additionally require each literal
carrier component to contain complete
\(\langle\delta,\gamma\rangle\)-planes, invariance of its tags and frozen
exterior under those translations, one common full cyclic phase, and
pointwise root/antipode splice ports.  These properties have not been
proved for the support \(\mathcal U_k\) of the arbitrary-\(k\) carrier.
Taking a Cartesian tensor only gives disjoint product tori; it does not
prove the required fused-cycle owner factor.

Even if that fibre is supplied, the local shore group does not mix the two
wire blocks in (0.5).  Frozen carrier tags, buffers, and seed sectors
cannot by themselves invalidate the fixed-wire trace cut in Section 6.

## 3. The exact \(12/16\) overlapping-layer law

The local four constant shores do not imply that two row-dependent pair
banks are freely independent.  In this section the endpoints have the
interlaced order

\[
             a<b<c<d,\qquad A=(a\ c),\quad B=(b\ d),              \tag{3.0}
\]

which is the geometry of the actual \(Q_4\) seed
\(A=(1\ 3),B=(2\ 4)\).

Let \(\delta,\gamma\) be the cycle-label displacements associated with
two commuting, disjoint-coordinate transpositions.  Assume a phase prefix
cuts both coordinate pairs.  On one affine plane

\[
                         k+\langle\delta,\gamma\rangle
\tag{3.1}
\]

write a label as \((x,y)\in\mathbb F_2^2\), with addition of
\(\delta\) changing \(x\) and addition of \(\gamma\) changing \(y\).
Pair constancy forces the two bit fields to have the form

\[
                         \varepsilon(x,y)=a(y),\qquad
                         \beta(x,y)=b(x).
\tag{3.2}
\]

At the common cut phase, the owner-label map is

\[
                         T(x,y)=(x+a(y),\,y+b(x)).
\tag{3.3}
\]

Every Boolean function of one bit is affine:

\[
                         a(y)=a_0+A y,\qquad
                         b(x)=b_0+B x.
\tag{3.4}
\]

The linear part of (3.3) is

\[
                         \begin{pmatrix}1&A\\B&1\end{pmatrix},
\tag{3.5}
\]

whose determinant over \(\mathbb F_2\) is \(1+AB\).  Hence:

### Theorem 3.1 (commuting two-layer classification)

The two row-dependent layers give an exact owner partition on (3.1) if
and only if

\[
\boxed{
\bigl(\varepsilon(k)+\varepsilon(k+\gamma)\bigr)
\bigl(\beta(k)+\beta(k+\delta)\bigr)=0.}
\tag{3.6}
\]

Equivalently, the two fields may not both vary transversely on the same
four-label plane.  Exactly twelve of the sixteen formal choices
\((a(0),a(1),b(0),b(1))\) are legal.

The four constant choices are precisely \(I,A,B,AB\), so the supplied
four-shore seed passes this test.  What fails are four attempted
context-dependent combinations in which both bits cross their opposite
pair matching.

There is a second, stricter issue when these factors are to be used as a
same-vertex affine double factor.  The formal candidate complements both
selectors,

\[
                         \alpha'=1+\alpha,\qquad
                         \beta'=1+\beta.
\tag{3.7}
\]

At the level of a fixed row label this changes its direction permutation
by \(AB\).  At a fixed physical owner, however, the two factors can assign
different row labels to that owner.  Comparing the outgoing directions at
the two active boundary phases gives:

### Proposition 3.2 (interlaced same-vertex opposite criterion)

For the interlaced order (3.0), a legal second chart can satisfy

\[
 d_{\alpha',\beta'}^\pm(y)
       =AB\,d_{\alpha,\beta}^\pm(y)
 \qquad\text{for every physical owner }y
\tag{3.8}
\]

if and only if both \(a\) and \(b\) in (3.2) are constant; in that case
the second chart is their complement (3.7).

Here \(d^+\) and \(d^-\) denote the outgoing and incoming physical
direction functions.  The boundary comparison below proves necessity
already from \(d^+\).  Constant complementary charts are global Klein
shores, so the same calculation one phase backward gives \(d^-\) as
well.

Indeed, comparison at the phase before the first active direction forces
the second \(A\)-selector to be \(1+a\).  At the \(B\)-boundary the two
factor states assign the same physical owner to row labels differing by
\(\delta\), so the same-owner direction identity forces
\(b(x+\!1)=b(x)\).  The symmetric last boundary forces the second
\(B\)-selector to be \(1+b\), and the middle/\(A\)-boundary then forces
\(a(y+\!1)=a(y)\).  These conditions are sufficient because both shores
then use one global Klein twist on the whole four-label plane.

Thus the twelve-state menu is an exact factor menu, but only its four
constant charts retain the fixed-point-free same-vertex \(AB\) relation.
High row entropy and the affine opposite-shore identity must not be
conflated.

The interlacing hypothesis is essential.  The nested geometry has a
complete positive classification.

### Theorem 3.3 (nested twelve-state fixed-point-free double)

Let

\[
             a<b<c<d,\qquad A=(a\ d),\quad B=(b\ c).              \tag{3.8a}
\]

On one \(H=\langle\delta,\gamma\rangle\)-plane, write the selectors as
\(U(y),V(x)\).  The five successive prefix maps, after suppressing
repeated phases, are

\[
 I,\quad F_U(x,y)=(x+U(y),y),\quad
 T(x,y)=(x+U(y),y+V(x)),\quad F_U,\quad I.            \tag{3.8b}
\]

Consequently the chart is exact if and only if \(U\) or \(V\) is
constant: again exactly twelve of sixteen charts are legal.  Every legal
chart has the unique same-physical-owner incoming/outgoing \(AB\)-partner

\[
                 U'(y)=1+U(y),\qquad
                 V'(x)=1+V(x+1).                                \tag{3.8c}
\]

This partner map is an involution and partitions the twelve legal charts
into six unordered double-factor pairs.  Formula (3.8c) is independent of
the chosen affine origin on the \(H\)-plane: replacing \(x\) by \(x+1\)
conjugates both \(V\) and \(V'\) by the same translation.

To prove the same-owner assertion, before the first \(A\)-endpoint the
two row labels agree, forcing \(U'=1+U\).  Before the first
\(B\)-endpoint they differ by \((1,0)\), forcing
\(V'(x+1)=1+V(x)\).  At the central map, the row-label correspondence is

\[
 (x,y)\longleftrightarrow
 \begin{cases}
 (x+1,y+1),&U\text{ constant},\\
 (x,y+1),&U\text{ nonconstant},
 \end{cases}                                                     \tag{3.8d}
\]

and in the second case legality forces \(V\) to be constant.  These
relations give the \(AB\)-direction identity at the second \(B\)-endpoint
as well.  The outer \(A\)-endpoint is symmetric.  Reading the same four
boundaries immediately after rather than immediately before each edge
proves the incoming identity.  The first two boundary comparisons also
show uniqueness.

Thus a rooted nested quartet retains all twelve states and a
fixed-point-free physical opposite.  The standard \(Q_4\) seed is
interlaced, and rerooting or applying one of its four Klein shores
preserves that crossing type.  Theorem 3.3 becomes available only after a
larger carrier changes the rooted direction order; it is the first
positive primitive left outside the interlaced no-go.  On one fixed
rooted four-position order, however, the nested matching is unique
(outer endpoints paired and inner endpoints paired), and all its shores
preserve those two wires.  Repeating this gate on the same closed carrier
does not itself re-pair them.

There is nevertheless a positive linear-rate double subatlas even in the
interlaced geometry.  Partition \(K_0\) into the
\(\langle\delta,\gamma\rangle\)-planes (3.1).  On each plane \(Q\), choose
two constants

\[
                         (u_Q,v_Q)\in\mathbb F_2^2                 \tag{3.8e}
\]

independently, and use the constant chart \(a\equiv u_Q,b\equiv v_Q\).
Define the opposite factor by the complementary chart
\((1+u_Q,1+v_Q)\) on that same plane.  Proposition 3.2 applies plane by
plane, so the two exact factors have the same-owner incoming and outgoing
\(AB\) relation everywhere.  The number of first-factor states is

\[
                         4^{N/4}=2^{N/2}.                         \tag{3.8f}
\]

Here \(N=|K_0|\).
Thus fixed-point-free opposition and linear row information do coexist;
what fails is the larger twelve-state entropy, not all row entropy.
For \(t\) coordinate-disjoint, phase-disjoint quartets, this construction
composes and gives

\[
                         2^{tN/2}                                \tag{3.8g}
\]

 choices of the first factor in ordered double-factor states, with global
relative permutation
\(\prod_{j=1}^t A_jB_j\).  In the guaranteed \(t=h/8\) atlas of Section 4,
the count is \(2^{2^h/32}\), but the relative permutation still fixes all
odd ambient directions.  The partner involution has no fixed parameter
array, so unordered pairs number \(2^{tN/2-1}\).

For completeness, the cross-block same-owner identity is local, not an
implicit independence assumption.  Write

\[
 \sigma_k=\prod_j A_j^{u_{j,k+H_j}}B_j^{v_{j,k+H_j}},
 \qquad
 \bar\sigma_k=\left(\prod_jA_jB_j\right)\sigma_k.                 \tag{3.8h}
\]

At any phase, all prefix displacements vanish except possibly that of the
unique closed slab containing the phase.  If this is slab \(j\), the two
row labels assigned to one physical owner differ by an element of \(H_j\)
and therefore use the same constants \(u_{j,Q},v_{j,Q}\).  Every other
block fixes the adjacent physical direction.  Proposition 3.2 then gives
the \(A_jB_j\), hence the global \(\prod_\ell A_\ell B_\ell\), relation
for both adjacent directions.  Outside all slabs the two phase maps are
the identity and the global relation is immediate.  The antipodal half is
identical.  This also proves that variation between different planes and
different blocks does not invalidate (3.8g).

For the isolated \(Q_4\) seed the two displacements differ by the
antipode:

\[
                         \delta+\gamma=\mathbf1.
\tag{3.9}
\]

The four-label plane therefore double-counts antipodal roots.  Descent to
literal \(C_8\) cycles forces both selectors to be constant, leaving
exactly the four global shores \(I,A,B,AB\).  Theorem 3.1 is the law for
an embedded proper quartet in a larger syndrome carrier where
\(\mathbf1\notin\langle\delta,\gamma\rangle\); it must not be applied as
a sixteen-chart root model of the bare \(Q_4\).  The same proper-embedding
qualification applies to the twelve-state conclusion of Theorem 3.3.

## 4. The proved high-rate multilayer composition

The exact owner/factor composition gate is already positive without
crossing phase slabs.  Let \(h=2^a\), and use the parity-alternating
syndrome factor with

\[
                         \Psi(e_{2t})=z
\tag{4.1}
\]

for all even positions.  Put

\[
r={h\over4},\qquad
\tau_j=(4j\ 4j+2),\qquad
\delta_j=e_{4j}+e_{4j+2}
\quad(0\le j<r).
\tag{4.2}
\]

Choose a common phase complement \(K_0\) containing all \(\delta_j\);
then

\[
                         N=|K_0|={2^h\over2h}.
\tag{4.3}
\]

For every \(j\), choose an arbitrary field

\[
\varepsilon_j:K_0/\langle\delta_j\rangle
                         \longrightarrow\mathbb F_2
\tag{4.4}
\]

and define

\[
\sigma_k=\prod_{j=0}^{r-1}
              (4j\ 4j+2)^{\varepsilon_j(k)}.
\tag{4.5}
\]

The prefix displacement of layer \(j\) is nonzero only at

\[
                         I_j=\{4j+1,4j+2\}.
\tag{4.6}
\]

These intervals are pairwise disjoint.  Thus the phase-\(i\) row-label
map is either the identity or the single matching

\[
                         k\longmapsto
                         k+\varepsilon_j(k)\delta_j.
\tag{4.7}
\]

Pair constancy makes (4.7) a permutation.  It follows phase by phase that

\[
                         \{\sigma_kP+k:k\in K_0\}
\tag{4.8}
\]

is an exact factor into isometric \(C_{2h}\)'s.  Installing the layers
one at a time exchanges literal phase owners inside each selected
\(\{k,k+\delta_j\}\) pair, so every intermediate factor is exact.

The number of independent owner-component bits is

\[
\boxed{
r{N\over2}
={h\over4}{2^h\over4h}
={2^h\over16}.}
\tag{4.9}
\]

Every bit is recoverable from the rooted final direction word, so there
are exactly \(2^{2^h/16}\) distinct factors.  If every bit is on, the
successor map differs from the reference on exactly

\[
                         2^{h-1}
\tag{4.10}
\]

owner tails, density \(1/2\).  Thus the one-bank
\(O(1/h)\)-action ceiling and its logarithmic-depth occurrence cut do not
extend to the multilayer atlas.

The \(A/B\) seed can be inserted as a four-shore local state wherever both
wire transpositions are available.  Theorem 3.1 is the exact extra
compatibility condition when their prefix slabs overlap.  It does not
upgrade (4.9) to two completely independent bits on every crossing
four-label plane.

There is also a guaranteed growing four-shore atlas.  Here
\(h=2^a\ge8\).  Use the same parity-alternating syndrome map and, for
\(0\le j<h/8\), take

\[
 (a_j,b_j,c_j,d_j)
 =(8j,\,8j+2,\,8j+4,\,8j+6).
\tag{4.11}
\]

All four positions are even and hence have one syndrome column.  The
two active prefix intervals inside one quartet overlap, so Theorem 3.1
gives twelve rather than sixteen charts on each coset of

\[
H_j=\langle e_{a_j}+e_{c_j},e_{b_j}+e_{d_j}\rangle.
\tag{4.12}
\]

For this atlas choose the phase complement \(K_0\) anew so that it
contains \(\sum_jH_j\).  Such a complement exists: this entire span is
supported on the even coordinates and hence does not contain the all-one
vector.  Its cardinality is still \(N=2^h/(2h)\).

The closed slabs \([8j,8j+6]\) are disjoint for different \(j\), so their
phasewise Latin equations factor.  Since each \(H_j\)-coset contains four
cycle labels, the exact state count is

\[
\boxed{
\#\mathcal F_{\rm four}
=12^{(h/8)(N/4)}
=12^{\,2^h/64}.}
\tag{4.13}
\]

Every state is sequentially realizable: on a legal label plane, install
\(A\) first when its selector is constant transversely, and install \(B\)
first in the symmetric branch.  Activating \(AB\) on every block and
every label plane changes one half of all directed owner tails; a uniform
legal chart has mean changed density \(1/4\).

This atlas acts only on the even directions.  Its local opposite is
fixed-point-free on each active quartet, but its guaranteed global
opposite still fixes every odd direction.  A full-coordinate
fixed-point-free high-rate embedding is not supplied by (4.11).

The same physical coordinate slots admit a stronger **nested double
atlas**.  Replace the crossing pair frame in block \(j\) by

\[
             A_j^{\rm n}=(a_j\ d_j),\qquad
             B_j^{\rm n}=(b_j\ c_j),\qquad
 H_j^{\rm n}=\langle e_{a_j}+e_{d_j},e_{b_j}+e_{c_j}\rangle .
                                                                    \tag{4.13a}
\]

All four coordinates have the same syndrome column, so both nested
transpositions are legal.  Choose \(K_0\) to contain
\(\sum_jH_j^{\rm n}\).  Theorem 3.3 and disjointness of the closed slabs
give:

### Theorem 4.1 (growing nested local-\(AB\) double atlas)

For \(h=2^a\ge8\), there are exactly

\[
                         12^{\,2^h/64}                            \tag{4.13b}
\]

choices of the first rooted exact syndrome factor in the nested atlas.
Every one has a unique partner in the same atlas whose incoming and
outgoing directions at every physical owner are related by the fixed
coordinate permutation

\[
 R_{\rm n}=\prod_{0\le j<h/8}
       (a_j\ d_j)(b_j\ c_j).                                    \tag{4.13c}
\]

The partner is obtained independently on every
\(H_j^{\rm n}\)-plane by

\[
                         U'_j=1+U_j,\qquad
                         V'_j(x)=1+V_j(x+1).                     \tag{4.13d}
\]

The proof is phase-local: inside one slab it is Theorem 3.3, every other
block fixes the adjacent direction, and outside all slabs every prefix
displacement vanishes.  Thus arbitrary chart variation between planes
and blocks is allowed.  The partner operation is an involution.  The
relative shore \(R_{\rm n}\) moves every even direction and fixes every
odd direction, so its moved and fixed densities are both exactly
\(1/2\), and the two partner factors differ on exactly one half of all
outgoing owner tails.  If unordered pairs are counted instead, their number is
\(\tfrac12\,12^{2^h/64}\).

In fact the whole coordinate-disjoint, phase-disjoint architecture has a
strict coverage ceiling in the growing setting \(h\ge8\).  The four
syndrome columns of one quartet sum to zero:

\[
 \Psi(e_a)+\Psi(e_b)+\Psi(e_c)+\Psi(e_d)=0.                       \tag{4.14}
\]

Every four-position slab is then a proper cyclic arc.  If its closed
prefix slab contained only those four coordinate positions,
the syndrome prefix immediately after the slab would equal the prefix
immediately before it, contradicting the syndrome-transversal property.
Every quartet slab therefore contains at least one additional separator
coordinate.  Pairwise disjoint closed slabs consequently satisfy

\[
                         5t\le h.                                \tag{4.15}
\]

### Proposition 4.2 (disjoint-slab fixed-direction ceiling)

For \(h\ge8\), any disjoint-slab atlas of equal-column four-shore
quartets moves at most
\(4h/5\) ambient directions in its global \(AB\)-opposite and fixes at
least \(h/5\).  Hence this clean architecture cannot remove the old
fixed-direction averaging obstruction globally.  Escaping (4.15)
requires genuinely overlapping slabs or a non-syndrome completion.

Quantitatively, if \(k_s\) is the number of fixed directions in the
cyclic \(d\)-window starting at phase \(s\), then
\(h^{-1}\sum_s k_s\ge d/5\).  Since \(k_s\le d\), at least \(1/9\) of
the windows satisfy \(k_s\ge d/10\).  Thus the old invisible-subgroup
proof still gives exponentially large fibres on a fixed positive
fraction whenever \(d\to\infty\).

There is a separate obstruction when the arbitrary multilayer braid uses
noncommuting transpositions to change wire frames.  Let
\(\tau_1,\tau_2\) be two involutive switches and let the row word be

\[
             \sigma_{\epsilon_1,\epsilon_2}
                 =\tau_2^{\epsilon_2}\tau_1^{\epsilon_1}.        \tag{4.16}
\]

If complementing both switch bits were to give one fixed left shore
\(S\), then

\[
             \sigma_{1+\epsilon_1,1+\epsilon_2}
                         =S\sigma_{\epsilon_1,\epsilon_2}
             \quad\text{for all }\epsilon_1,\epsilon_2.          \tag{4.17}
\]

The state \((0,0)\) forces \(S=\tau_2\tau_1\).  The state \((0,1)\)
then forces

\[
                         \tau_1=\tau_2\tau_1\tau_2,               \tag{4.18}
\]

so \(\tau_1\tau_2=\tau_2\tau_1\).  Conversely, commutation makes
(4.17) true.  Thus:

### Proposition 4.3 (noncommuting complement obstruction)

For a two-switch row-word cube, bitwise complementation defines a fixed
global relative coordinate shore if and only if the two switches
commute.  In particular the adjacent transpositions used to re-pair wires
in the arbitrary overlapping sorting braid do not acquire a fixed shore
merely by replacing each local switch with the four-shore \(A/B\) seed.

This is already a word-level necessary condition.  Physical same-owner
compatibility imposes the additional row-label conditions of Proposition
3.2.  A specially designed non-complementary partner or a palindromic
network identity is not ruled out.

This negative statement concerns the fixed opposite, not exact-factor
frame mixing.  The audited nested-invariance braid remains positive.  For
an adjacent chain of \(r\) equal-syndrome transpositions with independent
displacements \(\gamma_1,\ldots,\gamma_r\), impose at layer \(j\)
invariance under

\[
                         D_j=\langle\gamma_j,\ldots,\gamma_r\rangle.
                                                                    \tag{4.18a}
\]

Writing \(N=|K_0|\), the exact number of free component bits is

\[
 \sum_{j=1}^r|K_0/D_j|
   =N\sum_{q=1}^r2^{-q}
   =N(1-2^{-r}).                                      \tag{4.18b}
\]

Every intermediate state is a literal exact isometric factor, and the
adjacent swaps generate \(S_{r+1}\), so this network genuinely changes
wire frames at rate \(1-o(1)\) per syndrome cycle.  Since
\(N=2^h/(2h)\), this is \(\Theta(2^h/h)\), not a constant bit rate per
owner of \(Q_h\).  What Proposition 4.3 proves is
that naive local opposition does not turn this positive braid into one
same-owner fixed-\(S\) double factor.  After the first noncommuting
overlap, the next active endpoints also occupy row-dependent phase
positions and are no longer a uniform nested four-shore gate.

There is one literal way to force a fixed shore after an arbitrary
variable braid, but it quantifies the entropy cost.  Let

\[
                         R=\rho_s\cdots\rho_1,                    \tag{4.19}
\]

where every \(\rho_j=(a_j\ b_j)\) is an equal-syndrome transposition, and
put

\[
 D_R=\left\langle e_{a_j}+e_{b_j}:1\le j\le s\right\rangle
                         \le K_0,\qquad r_R=\dim D_R.             \tag{4.20}
\]

If every bit field of the preceding variable braid is \(D_R\)-invariant,
then the fixed layers \(\rho_1,\ldots,\rho_s\) may be appended one at a
time.  At each layer, the old and new row fields are constant on the
relevant displacement pair, so the literal pair-layer lemma gives an
exact owner trade and, at the same physical owner,

\[
                         d_{\rm new}^{\pm}=\rho_jd_{\rm old}^{\pm}.
                                                                    \tag{4.21}
\]

The endpoint factor is therefore an exact same-owner \(R\)-shore of the
original factor.

### Proposition 4.4 (fixed-suffix action--entropy tradeoff)

Let \(N=|K_0|\), and suppose the variable braid has \(L\) Boolean row
fields.  Under the sufficient fieldwise \(D_R\)-invariance imposed by
this fixed-suffix construction, its number \(B\) of free Boolean
parameters satisfies

\[
                         B\le {LN\over2^{r_R}}.                  \tag{4.22}
\]

Indeed each field is a function on a quotient of \(K_0/D_R\).  For the
rank claim, form the graph whose edges are the transpositions in (4.19).
Its edge differences span the componentwise even subspace, while \(R\)
preserves every graph component.  Hence
\(\operatorname{im}(R-I)\subseteq D_R\), so

\[
                         r_R\ge\operatorname{rank}(R-I).          \tag{4.23}
\]

If \(R\) is fixed-point-free on \(h\) directions, every cycle of \(R\)
has length at least two and
\(\operatorname{rank}(R-I)=h-\#\operatorname{cycles}(R)\ge h/2\).
Consequently every \(L=2^{o(h)}\)-layer fixed-suffix compiler has

\[
                         B=o(N),                                 \tag{4.24}
\]

so it loses the desired linear information rate.

For the particular fixed-point-free involution sought from \(AB\)-blocks,
the obstruction is stronger.  If
\(R=(a_1\ b_1)\cdots(a_{h/2}\ b_{h/2})\), then

\[
 \sum_{j=1}^{h/2}(e_{a_j}+e_{b_j})=\mathbf1\in D_R,               \tag{4.25}
\]

contradicting \(D_R\le K_0\).  Thus no common-rooted-phase fixed-suffix
construction of this type exists for a full perfect-matching shore at
all; the entropy estimate (4.24) is relevant to other fixed-point-free
cycle types or partial shores for which \(\mathbf1\notin D_R\).

The phase-local
disjoint-slab double atlas avoids global \(D_R\)-invariance, but
Proposition 4.2 shows that it necessarily leaves a positive fixed
direction density.  These two theorems isolate the remaining possibility:
an overlapping, phase-local partner identity rather than a global
invariance suffix.  Proposition 4.4 is a ceiling for this explicit
suffix architecture, not for every possible correlated partner.

## 5. What fixed-point-free \(AB\) removes

The affine fixed-shore trace bound for a relative coordinate permutation
\(S\) uses

\[
                         J\cap S^{-1}J.
\tag{5.1}
\]

Every fixed direction of \(S\) lying in a completed support \(J\)
automatically belongs to (5.1).  For the old one-bit \(B\)-shore,
\[
                         |\operatorname{Fix}B|=2.
\tag{5.2}
\]

After tensoring, the fixed-direction density remains \(1/2\), forcing a
positive fraction of windows to have large (5.1) and hence exponentially
large trace fibres.

For the opposite four-shore pair,

\[
                         |\operatorname{Fix}(AB)|=0.
\tag{5.3}
\]

Therefore the fixed-direction averaging argument has zero right-hand
side and gives no obstruction.  In this exact and limited sense the new
seed solves the fixed-shore trace problem on one quartet.  The global
relative shore \(R_{\rm n}\) in Theorem 4.1 still fixes all odd
directions, so the earlier positive-density averaging theorem continues
to apply to that proved growing atlas: at least one third of its cyclic
\(d\)-windows contain at least \(d/4\) fixed directions.

Proposition 3.2 is essential here.  A nonconstant twelve-state row field
need not have a same-vertex \(AB\)-opposite at all.  Thus one cannot apply
\(|\operatorname{Fix}(AB)|=0\) to the whole high-rate menu merely by
complementing its formal row bits.

It does not force \(J\cap(AB)^{-1}J\) to be small.  If \(J\) contains
both endpoints of a wire, that whole pair lies in the intersection.  More
importantly, every available shore remains in the fixed-wire group

\[
                         \langle A,B\rangle
   =\operatorname{Sym}\{1,3\}\times
    \operatorname{Sym}\{2,4\}.
\tag{5.4}
\]

The resulting support-entropy obstruction is independent of fixed points.

There is also a stronger obstruction for a **globally constant** shore.
In the ambient syndrome factor, let \(K\) be the syndrome kernel and let
\(E\) be the even context space.  For a completed support \(J\), every

\[
                         e\in E\cap K\cap\mathbb F_2^J             \tag{5.5}
\]

gives the aligned collision

\[
                         p'=p+e,\qquad y'=y+ABe.                   \tag{5.6}
\]

In the standard \(h=2^a\) carrier,

\[
 \dim(E\cap K\cap\mathbb F_2^J)
                         \ge |J|-\log_2h-1.                       \tag{5.7}
\]

This calculation never used a fixed coordinate of \(AB\).  Nonconstant
row fields can destroy the translation identity (5.6), so (5.5) is not a
universal invariant of the twelve-state atlas.  The fixed-wire theorem
below is the obstruction which survives all such row dependence.

## 6. The fixed-wire trace invariant

Let a growing construction fix **each member setwise** of a partition
\(\mathcal P\) of the \(h\) directions into two-point wires; equivalently,
every shore lies in
\(\prod_{P\in\mathcal P}\operatorname{Sym}(P)\).  Merely permuting the
wires as blocks is not covered.  Assume also that all row orders are
obtained from one fixed base cyclic order by such shores.  Allow arbitrary
Boolean control functions, arbitrary repeated layers, and arbitrary
choices from the two swaps on every wire.  For a completed support \(J\) with
\(|J|=d\), \(0\le d\le h\), put

\[
                         s(J)=
\#\{P\in\mathcal P:|J\cap P|=1\}.
\tag{6.1}
\]

The complete wire-count vector

\[
                         (|J\cap P|:P\in\mathcal P)
\tag{6.2}
\]

is shore-invariant.  A split wire has two images; a wire met zero or twice
has one.  Hence

\[
                         |\operatorname{Orb}(J)|=2^{s(J)}
                         \le2^{|J|}.
\tag{6.3}
\]

There are at most \(h\) cyclic base intervals of size \(d\).  Therefore
the support library of any fixed-wire atlas has size at most

\[
                         L_d\le h2^d.
\tag{6.4}
\]

An aligned trace also records two outside bit strings on \(J^c\), giving
at most

\[
                         h2^d\,2^{2(h-d)}
\tag{6.5}
\]

trace codes.  The aligned even-context start set has size

\[
                         2^{2h-1}.
\tag{6.6}
\]

Consequently:

### Theorem 6.1 (one-base-order fixed-wire trace cut)

For every fixed-wire composition satisfying the one-base-order hypothesis
above, the proportion of distinct aligned trace codes at depth \(d\) is at
most

\[
                         \boxed{{2h\over2^d}.}
\tag{6.7}
\]

Thus the collision excess is at least

\[
                         \left(1-{2h\over2^d}\right)_+
                         2^{2h-1}.
\tag{6.8}
\]

In particular it is \(1-o(1)\) of all aligned starts whenever
\(d-\log_2h\to\infty\).

More generally, if the construction begins with a library of \(L_0\)
unrelated base cyclic orders, then (6.4) becomes

\[
                         L_d\le L_0h2^d,                          \tag{6.9}
\]

and the right side of (6.7) becomes \(2L_0h/2^d\).  Thus an exponential
base-order library is a genuine way to leave Theorem 6.1; fixed-wire
invariance alone does not bound \(L_0\).

The interlaced and nested atlases proved above have \(L_0=1\): every row
is \(\sigma_kP\) for the same rooted base order \(P\), with \(\sigma_k\)
in the relevant fixed-wire group.  The frame-changing adjacent braid of
Section 4 is outside Theorem 6.1 precisely because its shores do not fix
the wire blocks setwise.

The support-library bound (6.4) survives after freezing arbitrary carrier
tags, cell identity, exterior context, and phase fibre, provided those
data do not change the physical wire-count vector.  The normalized trace
ratio (6.7) transfers fibrewise only under an additional product-fibre
hypothesis: every frozen fibre must be a complete or equidense copy of
the \(2^{2h-1}\) aligned even-context domain, and the trace must expose no
extra internal datum beyond the support and the two outside strings.
An arbitrary sparse carrier fibre can be injective, so no unconditional
arbitrary-\(k\) transfer is claimed here.  A carrier operation which
changes the wire frame also falls outside the theorem.

## 7. No transverse second frame inside \(Q_4\)

The fixed-wire cut could be escaped by changing the wire matching between
layers.  The same \(Q_4\) phase colouring cannot do this.

Let \(C_i\) be the owner class whose base outgoing direction is \(i\).
If both the identity and \((i\ j)\) are valid twists of one colouring,
comparison of the two translated partitions forces

\[
C_i+(e_i+e_j)=C_i,\qquad
C_j+(e_i+e_j)=C_j.
\tag{7.1}
\]

Suppose one twist bank contained

\[
I,\quad(1\ 3),\quad(2\ 4),\quad
(1\ 2),\quad(3\ 4).
\tag{7.2}
\]

For each \(i\), equation (7.1) gives two independent even periods.  Hence
every nonempty \(C_i\) has size at least four.  The four classes partition
sixteen owners, so every \(C_i\) is one affine two-plane contained wholly
in one parity shore.

The four direction subspaces forced by (7.2) are pairwise distinct.
But two affine planes in one three-dimensional parity shore are disjoint
only if they are parallel, hence have the same direction subspace.  Each
parity shore would have to contain two disjoint \(C_i\)'s, a
contradiction.

### Theorem 7.1 (transverse-frame no-go)

No full-direction \(Q_4\) colouring has both perfect-matching twist banks

\[
                         \{13,24\}\quad\text{and}\quad
                         \{12,34\}
\tag{7.3}
\]

together with the identity.

Thus \(AB=BA\) is a commuting square, not a Yang--Baxter relation that
re-pairs wires.  A transverse Beneš layer cannot be made by selecting
another shore of this same four-shore cube.  The other transverse perfect
matching \(\{14,23\}\) is conjugate to \(\{12,34\}\) under \(A\) (or
\(B\)); equivalently, the same affine-plane proof excludes any two
distinct perfect matchings of the four direction labels.

## 8. Exact boundary

Proved:

1. the four local shores and fixed-point-free opposite relation;
2. the exact phase-interface obstruction to a generic
   arbitrary-\(k\)-carrier suspension;
3. the \(12/16\) owner-legality law for interlaced and nested commuting
   pair fields;
4. the interlaced criterion leaving only four plane-constant
   same-owner \(AB\) charts, and the nested theorem pairing all twelve
   legal charts;
5. an interlaced growing exact atlas and a nested growing same-owner
   double atlas, each with \(12^{2^h/64}\) choices of the first factor;
6. the disjoint-slab ceiling \(t\le h/5\), hence a positive fixed
   direction density in every such global opposite;
7. a separate literal \(h/4\)-layer owner-level braid with
   \(2^h/16\) independent bits and constant action density;
8. removal of the old fixed-direction trace step on the local constant
   \(AB\) opposite, but not on the proved growing atlases;
9. positive exact frame mixing with \(N(1-2^{-r})\) bits, together with
   failure of naive bit complementation through noncommuting layers and
   the \(B\le LN/2^{\dim D_R}\) fixed-suffix tradeoff (with the stronger
   \(\mathbf1\in D_R\) phase failure for a full matching shore);
10. the one-base-order fixed-wire support-entropy cut (and its
    \(L_0\)-base generalization), with the exact extra hypothesis needed
    for normalized arbitrary-carrier fibre transfer; and
11. impossibility of a transverse second wire frame in the same \(Q_4\)
   phase partition.

Not proved:

* a pair-clustered common-owner lift coupling the four shores to the
  arbitrary-\(k\) carrier;
* a full-coordinate, fixed-point-free, linear-rate multilayer family with
  changing wire frames;
* an overlapping phase-local partner identity which escapes both the
  disjoint-slab ceiling and the fixed-suffix entropy loss;
* a \(Q_8\) associator satisfying the needed frame-change and
  predecessor identities;
* a complete/equidense frozen-fibre decomposition transferring the
  normalized trace cut through the arbitrary-\(k\) carrier;
* balanced lower/upper protected collars for the dense braid atlas;
* all-depth occurrence rounding; or
* coefficient one.

The four-shore seed is therefore a real improvement, but not the final
trace compiler.  The next finite primitive must couple a wire-frame
change to one same-owner opposite and a completed antipodal phase fibre;
merely choosing among \(I,A,B,AB\) in a fixed frame is insufficient.
