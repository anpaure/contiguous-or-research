# PBBS \(G_H+P_H\) transversals at Gaussian depth: frozen adaptive-deletion equivalence and the critical local obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Fix \(A>0\), and put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil .                 \tag{0.1}
\]

After removing quotient \(\tau\)-cycles of length at most \(H+1\), let
\(\mathcal I_H^{G}\) be the minimal short toggle arcs and let
\(\mathcal I_H^{P}\) be the short positive-run arcs in the centered PBBS
owner factor.  Write

\[
 \mathcal I_H=\mathcal I_H^G\cup\mathcal I_H^P . \tag{0.2}
\]

This note proves the following exact statements.

1. For the frozen PBBS arc family, a complete, history-dependent
   left/right deletion history inside one arc is exactly the choice of one
   edge in that arc.  Simultaneously over all fixed arcs, this independent
   adaptive orientation is therefore exactly the integral circular-interval
   transversal problem.  If \(\bar\nu_H\) and \(J_H\) are its packing and
   transversal numbers, then

   \[
      \boxed{\bar\nu_H\le J_H\le2\bar\nu_H.}      \tag{0.3}
   \]

   With capacities, the complete feasibility criterion is the ordinary
   Hall inequality.  This does not cover a dynamic \(AO_A/SDH_A\)
   operation in which an earlier factor switch rewires the owner graph and
   changes the supports presented later.

2. The two shores \(G_H\) and \(P_H\) differ by only an absolute factor.
   If \(\tau_H^P,\nu_H^P\) are the positive-arc transversal and packing
   numbers, then

   \[
      \boxed{
      \tau_H^P\le J_H\le3\tau_H^P\le6\nu_H^P.}   \tag{0.4}
   \]

   Thus the desired adaptive orientation theorem

   \[
      J_H=o_A(B_m/\sqrt m)                         \tag{0.5}
   \]

   is equivalent, up to constants and the negligible short-cycle term, to
   the quotient form of \(ST_A\).  It is not a separate route to \(ST_A\).

3. Strengthening the frozen-support relaxation by the formal
   predecessor-child menus still gives no generic Gaussian-depth
   contraction inside that product-menu model.  Its one-level integral
   minimax port-index load is exactly the terminal-zero layer.  Serially,
   the unavoidable all-zero formal history retains exactly

   \[
      \prod_j {2r_{j+1}\over r_j+r_{j+2}}.        \tag{0.6}
   \]

   This tends to \(1/2\) on harmonic profiles and to
   \(1-O_A(m^{-1/2})\) on an explicit integral
   \(\Theta_A(\sqrt m)\)-level pruning profile.  This is an exact
   obstruction in the unrestricted port-menu relaxation.  Common formal
   port indices across sheets have not been identified with common physical
   PBBS targets, and not every such profile is a compatible passage tower.

4. The fixed-depth zero-slot Pascal envelope is exactly critical in an
   iterated harmonic limit.  First fix \(k\), let the profile scale tend to
   infinity, and only then let \(k\to\infty\).  The resulting triangular
   zero-prescription fraction is

   \[
      \boxed{
      { (k+2)^k\over (k+1)^{k+1}}
      \sim {e\over k}.}                           \tag{0.7}
   \]

   History-adaptive choice of labelled slots does not change this
   iterated-limit fraction when the labels are chosen before the current
   weak composition is exposed.  This is not a diagonal theorem at
   \(k=H=A\sqrt m\).  Moreover, zero slots are not sufficient for actual
   PBBS closure: an explicit semilength-three child cycle has two tight
   gap-five starts, but only one of their terminal-zero parents has the
   tight gap-seven return.

5. There is a genuine retained PBBS local critical packing.  For every
   \(c\in(A/2,A)\), prime-period mountain fibres contain a pairwise
   quotient-edge-disjoint family occupying the asymptotic fraction

   \[
      \boxed{2c^2e^{-2c^2}}                       \tag{0.8}
   \]

   of that fibre's reciprocal-height capacity.  This proves that no
   uniform or fibrewise \(o(1)\) utilization theorem is true.  The fibre
   has only \(\exp(O(\sqrt m\log m))\) roots, however, and so (0.8) is not
   a Catalan-scale lower bound.

6. Direct spectator amplification inside the one-generation,
   deletion-preserving mountain class is impossible.  The hypothesis
   \(\partial D=M_{h-1}\) leaves only height-one leaf bundles, already
   counted by the weak-composition fibre.  A nonempty concatenated Dyck
   spectator leaves the inherited mountain rotation chart before the
   parent mechanism closes.  Even if every accidental active return in the
   whole Gaussian one-block spectator library is granted, that library is
   \(o(B_m/H)\).

Consequently neither

\[
 \nu_H(P_m)=o_A(B_m\sqrt m)                       \tag{0.9}
\]

nor a matching global lower bound is proved here.  What is proved is a
sharp route boundary: frozen-support deletion is the transversal itself;
the formal product-menu relaxation has a Gaussian recourse trap; and the
fixed-depth harmonic fan has a critical iterated-limit envelope.  A
factor-rewiring adaptive orientation, or an actual coefficientwise
Gaussian fan contraction, is not ruled out.  The remaining PBBS input must
control the global, Pascal-weighted chronology of actual
predecessor-active phases on long cycles.

## 1. The exact \(G_H+P_H\) interval system

Write one complement-projected step-two owner cycle as

\[
 X_{i+1}=X_i-\{\alpha_i\}+\{\beta_i\}.            \tag{1.1}
\]

For \(q\ge1\), put

\[
 L_{i,q}=\bigcap_{a=0}^{q}X_{i+a}.                \tag{1.2}
\]

When the adjacent depth-\(q\) shadows are floor-correct, the exact
adjacent-shadow dictionary is

\[
 L_{i,q}=L_{i+1,q}
 \quad\Longleftrightarrow\quad
 \beta_i=\alpha_{i+q}.                            \tag{1.3}
\]

The repeated coordinate enters at transition \(i\), is present in the
intermediate owners, and leaves at transition \(i+q\).  Its literal
transition-edge support is therefore

\[
 I(i,q)=\{e_i,e_{i+1},\ldots,e_{i+q}\},
 \qquad |I(i,q)|=q+1.                             \tag{1.4}
\]

Equivalently, a consecutive omitted-label gap

\[
 g=2s+1                                             \tag{1.5}
\]

produces on the two step-two parities:

* a minimal toggle arc \(N_i\in\mathcal I_H^G\) with \(s+1\)
  transition edges; and
* the insertion-through-deletion arc
  \(R_i\in\mathcal I_H^P\) of its positive run, with \(s+2\)
  transition edges.

The gap contributes precisely when

\[
 g\le2H-1.                                        \tag{1.6}
\]

Conversely every member of \(\mathcal I_H\) arises from such a gap.  The
boundary edges in (1.4) are essential; omitting either changes both the
transversal and its constants.

Delete quotient cycles of length at most \(H+1\).  Every remaining arc in
\(\mathcal I_H\) is then a proper, nonrepeating circular interval.

## 2. Adaptive adjacent deletion is exactly circular piercing

Let

\[
 I=[a,b]=\{e_a,e_{a+1},\ldots,e_b\}               \tag{2.1}
\]

be a line interval of transition edges.  An adjacent deletion removes the
current leftmost or rightmost edge, and a complete history continues until
one edge remains.  The choice at each step may depend on the entire earlier
history.

### Theorem 2.1 (one-interval terminal set)

The possible terminal edges of complete adjacent-deletion histories on
\(I\) are exactly the members of \(I\).

#### Proof

Every deletion leaves a nonempty subinterval, so the terminal belongs to
\(I\).  To finish at \(e_{a+t}\), delete exactly the \(t\) edges on its
left and the \(b-a-t\) edges on its right.  Any interleaving of those
boundary deletions is legal and has the prescribed terminal. \(\square\)

Let \(\mathcal I\) be a family of proper intervals on a disjoint union of
cycles.  A simultaneous adaptive orientation is one complete history for
each interval.

### Theorem 2.2 (simultaneous adaptive orientation on a frozen arc family)

\[
 \boxed{
 \min_{\text{all simultaneous adaptive histories}}
 |\{\text{distinct terminal edges}\}|
 =\tau(\mathcal I),}                              \tag{2.2}
\]

where \(\tau(\mathcal I)\) is the minimum edge-transversal number.

More generally, for integral edge capacities \(b_e\ge0\), histories can
be chosen so that at most \(b_e\) intervals terminate at \(e\) if and
only if

\[
 |\mathcal F|
 \le\sum_{e\in\bigcup_{I\in\mathcal F}I}b_e
 \qquad(\mathcal F\subseteq\mathcal I).           \tag{2.3}
\]

#### Proof

By Theorem 2.1, the terminal chosen for \(I\) must lie in \(I\); hence the
set of distinct terminals is a transversal.  Conversely, from a
transversal choose one incident edge for each interval and use Theorem 2.1
to realize it by a deletion history.

For capacities, replace edge \(e\) by \(b_e\) clones and apply Hall's
marriage theorem to the interval--edge incidence graph.  Condition (2.3)
is exactly Hall's condition.  Theorem 2.1 converts the matching back into
histories. \(\square\)

This proof includes arbitrary evolution of each interval's own left/right
history.  Earlier choices change its current subinterval, but that state is
completely described by the two numbers of deleted boundary edges.  Its
terminal projection remains exactly the original interval-incidence graph.
The family \(\mathcal I\) is frozen throughout.  The proof says nothing
about an owner-factor switch which changes a later support before that
support's history is defined.

### Theorem 2.3 (sharp circular factor two)

On one active cycle,

\[
 \nu_C\le\tau_C\le\nu_C+1\le2\nu_C.              \tag{2.4}
\]

Consequently, on the disjoint union of all active cycles,

\[
 \boxed{\nu(\mathcal I)\le\tau(\mathcal I)
 \le\nu(\mathcal I)+K_{\rm act}
 \le2\nu(\mathcal I).}                           \tag{2.5}
\]

#### Proof

Choose an edge \(e\) in one member of the family.  The intervals
containing \(e\) are pierced by \(e\).  Cut the cycle at \(e\); the
remaining intervals are line intervals, whose packing and transversal
numbers agree by the greedy earliest-right-end algorithm.  Their packing
number is at most \(\nu_C\), proving \(\tau_C\le\nu_C+1\).  Every active
cycle contributes at least one member to a cyclewise maximum packing, so
\(K_{\rm act}\le\nu(\mathcal I)\). \(\square\)

### Corollary 2.4 (the two shores differ only by constants)

Let \(T\) pierce every positive arc \(R_i\).  In the original one-step
PBBS index, one of the three edges in

\[
 T\cup(T-1)\cup(T+1)                              \tag{2.6}
\]

then pierces the paired toggle arc \(N_i\).  Therefore

\[
 \tau_H^P\le J_H\le3\tau_H^P.                    \tag{2.7}
\]

On each active positive-arc cycle,
\(\tau_C^P\le\nu_C^P+1\).  The number of such cycles is at most the
aggregate positive packing, and hence

\[
 \tau_H^P\le2\nu_H^P.                             \tag{2.8}
\]

Equations (2.7)--(2.8) prove (0.4).  Positive winding changes which pairs
\((N_i,R_i)\) occur, but not any support, deletion, or Hall statement in
this section.

## 3. Quotient-to-physical normalization

Let \(Z_H\) be the number of quotient roots on \(\tau\)-cycles of length
at most \(H+1\).  The voltage-itinerary bound is

\[
 Z_H\le(2H+2)N^{2H+2}
      =\exp(O_A(\sqrt m\log m))
      =o(B_m/m^K)                                 \tag{3.1}
\]

for every fixed \(K\).

If \(\bar\nu_H^P\) is the positive-arc packing on the retained quotient
cycles and \(\nu_H(P_m)\) is its physical phase-deck packing, then

\[
 \boxed{
 N\bar\nu_H^P
 \le\nu_H(P_m)
 \le2N\bar\nu_H^P+NZ_H.}                         \tag{3.2}
\]

The lower inequality lifts every selected quotient interval through all
\(N\) spatial phases.  The lifts are disjoint above each quotient edge.
For the upper inequality, use Theorem 2.3 to pierce each long quotient
cycle, lift every piercing edge through the deck, and delete all physical
edges above the short quotient cycles.

Since \(N=(2+o(1))m\), equation (3.2) gives the exact equivalence

\[
 \nu_H(P_m)=o_A(B_m\sqrt m)
 \quad\Longleftrightarrow\quad
 \bar\nu_H^P=o_A(B_m/\sqrt m),                    \tag{3.3}
\]

and by (0.4) this is also equivalent, up to absolute constants, to
\(J_H=o_A(B_m/\sqrt m)\).  Thus proving the orientation estimate on these
frozen literal supports is already proving the short-return theorem.  A
dynamic factor-rewiring \(AO_A\) could be stronger only by changing the
later support family, not by choosing left/right histories more cleverly
inside the same arcs.

## 4. Exact integral recourse trap in the formal predecessor-port product

Fix a reduced core of semilength \(d\), and distribute \(y\) free inverse
leaves among its \(2d+1\) slots.  The complete fibre and terminal layers
have sizes

\[
 P(d,y)=\binom{y+2d}{2d},
 \qquad
 K_z(d,y)=\binom{y-z+2d-1}{2d-1}.                \tag{4.1}
\]

A terminal-layer-\(z\) parent has the nested predecessor-port menu

\[
 \Gamma(z)=\{0,1,\ldots,z\}.                     \tag{4.2}
\]

### Theorem 4.1 (one-level integral minimax)

If every individual sheet is assigned integrally to one legal port and
\(L_i\) is port \(i\)'s load, then

\[
 \boxed{
 \min\max_iL_i=K_0(d,y).}                         \tag{4.3}
\]

The same formula holds after restricting the active terminal layers to
any nonempty initial interval \(0\le z\le Z\).

#### Proof

Every layer-zero sheet has the singleton menu \(\{0\}\), so port zero has
load at least \(K_0\).  Conversely assign every layer \(z\) to port \(z\).
Then port \(i\) has load \(K_i\le K_0\). \(\square\)

Fix now an integral pruning profile

\[
 r_0>r_1>\cdots>r_{L+1}>0,
 \qquad y_j=r_j-2r_{j+1}+r_{j+2}\ge0.             \tag{4.4}
\]

At level \(j\), the normalized forced-zero fraction is

\[
 \beta_j={2r_{j+1}\over r_j+r_{j+2}}.             \tag{4.5}
\]

### Theorem 4.2 (adaptive serial minimax)

Even when the orientation at level \(j\) depends on every earlier port
choice, the all-zero history has load at least the product of the
level-zero-layer sizes.  This is sharp, and the normalized minimax history
load is exactly

\[
 \boxed{\prod_{j=0}^{L-1}\beta_j.}                \tag{4.6}
\]

#### Proof

At every level, terminal value zero forces port zero.  Hence every tower
whose terminal value is zero at all levels is sent to the single history
\((0,\ldots,0)\), independently of all adaptive decisions.  The product
fibre gives the lower bound.  Assigning port \(i_j=z_j\) at every level
gives every history load equal to a product of \(K_{j,i_j}\)'s, bounded
by the all-zero product, and proves sharpness. \(\square\)

For the harmonic profile \(r_j=R/(j+1)\),

\[
 \beta_j={ (j+1)(j+3)\over(j+2)^2}
         =1-{1\over(j+2)^2},                      \tag{4.7}
\]

so

\[
 \prod_{j=0}^{L-1}\beta_j
 =\prod_{n=2}^{L+1}\left(1-{1\over n^2}\right)
 ={L+2\over2(L+1)}\longrightarrow{1\over2}.       \tag{4.8}
\]

There is also an entirely integral Gaussian-length profile.  Put

\[
 c_A=\min\{A/2,1/10\},\qquad
 L=\lfloor c_A\sqrt m\rfloor,
\]

\[
 r_j=m-2Lj+\binom j2\qquad(0\le j\le L+1).       \tag{4.9}
\]

Then

\[
 r_j-r_{j+1}=2L-j>0,qquad y_j=1,                 \tag{4.10}
\]

and \(r_{L+1}\ge(0.98-o(1))m\).  To realize the profile, attach \(2L\)
ordered unary branches to one root: one branch of each length
\(1,2,\ldots,L\), \(L-1\) branches of length \(L+1\), and one branch of
length \(L+1+r_{L+1}\).  After \(j\) simultaneous leaf prunings exactly
\(2L-j=r_j-r_{j+1}\) branches survive and exactly \(r_j\) edges remain.
Thus this is an integral realizable pruning profile, and

\[
 \prod_{j<L}\beta_j
 =\prod_{j<L}{2r_{j+1}\over2r_{j+1}+1}
 =1-O_A(m^{-1/2}).                                \tag{4.11}
\]

Theorems 4.1--4.2 concern the unrestricted formal port-menu product.  A
rank profile alone need not carry a compatible decorated PBBS passage at
every level, and equal port indices in different sheets need not denote one
common physical target.  Thus (4.11) is a relaxation obstruction, not PBBS
congestion and not a PBBS counterexample.

## 5. The fixed-depth triangular fan has a critical iterated limit

At inverse level \(j\), let the adjacent ranks be
\(r_{j-1},r_j,r_{j+1}\), and put

\[
 y_j=r_{j-1}-2r_j+r_{j+1}.                        \tag{5.1}
\]

The full weak-composition fibre has size

\[
 N_j=\binom{r_{j-1}+r_{j+1}}{2r_j}.              \tag{5.2}
\]

Prescribing any \(j\) distinct labelled slots to be zero leaves exactly

\[
 N_j^{(0)}
 =\binom{r_{j-1}+r_{j+1}-j}{2r_j-j}.             \tag{5.3}
\]

If the prescribed values have total \(w_j\ge0\), the count is instead

\[
 \binom{r_{j-1}+r_{j+1}-j-w_j}{2r_j-j},          \tag{5.4}
\]

and is at most (5.3), with the binomial-zero convention when the
prescription exceeds the available free mass.

The coordinates of a weak composition are exchangeable.  Therefore, in
the Cartesian/product exposure filtration, if the \(j\) labels are chosen
as an arbitrary function of all earlier levels and orientations but before
the current composition is exposed, the conditional zero fraction is still

\[
 q_j=
 {\binom{r_{j-1}+r_{j+1}-j}{2r_j-j}
  \over
  \binom{r_{j-1}+r_{j+1}}{2r_j}}.                 \tag{5.5}
\]

Take \(r_j=R/(j+1)\) and first let \(R\to\infty\) for fixed \(k\).  Then

\[
 q_j\longrightarrow
 \left({j(j+2)\over(j+1)^2}\right)^j,            \tag{5.6}
\]

and the complete triangular fan fraction telescopes:

\[
 \boxed{
 \prod_{j=1}^{k}q_j
 \longrightarrow
 \prod_{j=1}^{k}
 \left({j(j+2)\over(j+1)^2}\right)^j
 ={(k+2)^k\over(k+1)^{k+1}}
 \sim{e\over k}.}                                \tag{5.7}
\]

Thus, in this iterated limit, even \(k(k+1)/2\) labelled zero equations can
retain the critical \(1/k\) fraction.  By decorating disjoint
\((2k+2)\)-edge abstract interval blocks with these tower data, one
simultaneously saturates all support-edge inequalities and all the
zero-slot counts at order \(\Theta(B/k)\).  Consequently no nonnegative
linear consequence valid uniformly over these abstract harmonic models can
give \(o(B/k)\).

The order of limits is essential.  If \(R=m\) and
\(k=A\sqrt m\), then

\[
 y_j={2m\over j(j+1)(j+2)}<1                     \tag{5.8}
\]

at the upper Gaussian levels, so the rational harmonic profile is not an
integral rank profile there.  The abstract disjoint-block model is not
asserted to be PBBS and does not exclude a fixed-coefficient Gaussian
contraction.  Its role is only to close the uniform fixed-depth harmonic
envelope shortcut.

## 6. Zero prescriptions do not imply actual PBBS closure

The preceding envelope also fails as a converse at the first nontrivial
orientation.

Put

\[
 F_0=110100,\qquad F_1=110010,\qquad F_2=101100.  \tag{6.1}
\]

The exact block rotations give

\[
 \tau F_0=F_1,qquad \tau F_1=F_2,qquad
 \tau F_2=F_0.                                    \tag{6.2}
\]

Their \((\delta,d)\) pairs are

\[
 (2,1),\qquad(2,3),\qquad(4,1).                  \tag{6.3}
\]

A height-two root \(F\) starts the tight gap-five return exactly when

\[
 d(F)+d(\tau F)=\delta(\tau^2F).                  \tag{6.4}
\]

Using (6.3), the two sides at \(F_0,F_1,F_2\) are respectively

\[
 (4,4),\qquad(4,2),\qquad(2,2).                  \tag{6.5}
\]

Thus the tight child phases are \(F_0,F_2\), and the only oriented
adjacent pair of tight phases is \(F_2\to F_0\).

Now consider the two terminal-zero parents

\[
 D_0=1110011000,qquad \partial D_0=F_0,          \tag{6.6}
\]

\[
 D_2=1100111000,qquad \partial D_2=F_2.          \tag{6.7}
\]

The \(\tau\)-orbit beginning at \(D_0\) is

\[
 1110011000\ \longmapsto\ 1110001100
 \ \longmapsto\ 1100111000\ \longmapsto\ D_0, \tag{6.8}
\]

with \((\delta,d)\) pairs

\[
 (3,1),\qquad(3,5),\qquad(7,1).                  \tag{6.9}
\]

At starts \(s=1,2,3\), the zero-winding return equation

\[
 \sum_{i=0}^{s-1}d(\tau^iD_0)=\delta(\tau^sD_0) \tag{6.10}
\]

reads

\[
 1\ne3,qquad 1+5=6\ne7,
 \qquad1+5+1=7\ne3.                              \tag{6.11}
\]

Every displayed quantity is strictly between zero and the circumference
eleven, so no nonzero winding repairs the equation.  Hence \(D_0\) has no
gap-seven return.

Starting instead at \(D_2\), the deficits are \(1,1,5\), and

\[
 1+1+5=7=\delta(\tau^3D_2).                      \tag{6.12}
\]

The two proper-prefix defects are positive, so this is the first tight
gap-seven return.  Therefore

\[
 \boxed{
 \text{tight child start + terminal zero}
 \not\Longrightarrow
 \text{tight parent return}.}                    \tag{6.13}
\]

The ordered adjacent child history is indispensable.  At depth \(j\), a
genuine tight parent projects to \(j+1\) consecutive, correctly oriented
tight child starts.  In set form its anchor lies in

\[
 \bigcap_{a=0}^{j}\tau^{-a}J_j,                  \tag{6.14}
\]

not merely in a product of one-slot marginal events.

## 7. A genuine retained critical packing in one PBBS fibre

Fix

\[
 {A\over2}<c<A.                                   \tag{7.1}
\]

Let \(p\to\infty\) through odd primes and put

\[
 h={p+1\over2},\qquad
 m=\left\lfloor(h/c)^2\right\rceil,
 \qquad y=m-h,qquad L=h+2.                       \tag{7.2}
\]

The complete inverse peak-deletion fibre over the mountain
\(M_{h-1}=1^{h-1}0^{h-1}\) is

\[
 \Omega_{m,p}=
 \left\{(n_0,\ldots,n_{p-1})\in\mathbb Z_{\ge0}^p:
              \sum_i n_i=y\right\}.             \tag{7.3}
\]

PBBS quotient time cyclically rotates these \(p=2h-1\) coordinates.
Define

\[
 \mathcal S_{m,p}=
 \{n\in\Omega_{m,p}:n_0=0, n_1,\ldots,n_L\ge1\}.
                                                               \tag{7.4}
\]

### Theorem 7.1 (isolated-zero mountain packing)

Every vector in \(\mathcal S_{m,p}\) starts a genuine first
zero-winding return of gap

\[
 g=p+2=2h+1,                                      \tag{7.5}
\]

whose complete quotient support has \(L=h+2\) transition edges.  These
supports are pairwise quotient-edge-disjoint and lie on retained quotient
cycles.  Moreover

\[
 |\Omega_{m,p}|=\binom{y+p-1}{p-1},
 \qquad
 |\mathcal S_{m,p}|=\binom{y-L+p-2}{p-2},         \tag{7.6}
\]

\[
 \boxed{
 {|\mathcal S_{m,p}|\over|\Omega_{m,p}|}
 ={2ce^{-2c^2}+o(1)\over\sqrt m},}               \tag{7.7}
\]

and

\[
 \boxed{
 {|\mathcal S_{m,p}|\over|\Omega_{m,p}|/(h+2)}
 \longrightarrow2c^2e^{-2c^2}>0.}               \tag{7.8}
\]

#### Proof

For terminal occupancy \(n_0=0\), the exact mountain predecessor times
give (7.5), with quotient support length \(h+2\).

Suppose two rotations of one composition both satisfied (7.4).  If their
oriented separation were at most \(L\), the second zero would lie among
the \(L\) coordinates required positive by the first.  If the reverse
separation were at most \(L\), the first zero would similarly violate the
second condition.  But

\[
 p=2h-1<2(h+2)=2L,                                \tag{7.9}
\]

so one of the two directed separations is at most \(L\).  Hence each
rotation orbit contributes at most one selected start.  Starts from
different rotation orbits lie on different quotient cycles, proving
edge-disjointness.

Every selected vector is nonconstant.  Since \(p\) is prime, its rotation
period is exactly \(p\).  Also

\[
 {p\over\sqrt m}\to2c>A,
 \qquad {h+1\over\sqrt m}\to c<A.                \tag{7.10}
\]

Thus eventually \(p>H+1\), while \(g\le2H-1\).  The selected cycles are
retained and the return is active.

After setting \(n_0=0\) and subtracting one from the next \(L\)
coordinates, \(y-L\) units remain in \(p-1\) variables, proving (7.6).
Division gives

\[
 {|\mathcal S_{m,p}|\over|\Omega_{m,p}|}
 ={p-1\over y+p-1}
  \prod_{i=0}^{L-1}{y-i\over y+p-2-i}.            \tag{7.11}
\]

Now

\[
 \log\prod_{i=0}^{L-1}{y-i\over y+p-2-i}
 =-\sum_{i=0}^{L-1}
   \log\left(1+{p-2\over y-i}\right)
 \longrightarrow-2c^2,                           \tag{7.12}
\]

because \(pL/y\to2c^2\).  The total Taylor error is

\[
 O\left({Lp^2\over y^2}+{L^2p\over y^2}\right)=o(1). \tag{7.13}
\]

Finally

\[
 {p-1\over y+p-1}={2c+o(1)\over\sqrt m}.         \tag{7.14}
\]

Equations (7.11)--(7.14) prove (7.7), and multiplication by
\(h+2=(c+o(1))\sqrt m\) proves (7.8). \(\square\)

The fibre is nevertheless small:

\[
 |\Omega_{m,p}|=\exp(O(\sqrt m\log m))
 =o(B_m/m^K)                                      \tag{7.15}
\]

for every fixed \(K\).  Thus Theorem 7.1 is a literal local saturation
and not a global counterexample to \(ST_A\).

For completeness, terminal occupancy \(z\ge1\) in the same fibre has

\[
 g_z=2+(2z+1)p.                                   \tag{7.16}
\]

Activity then implies \(3p+2\le2H-1\), hence \(p<H+1\); the entire
positive-winding mountain orbit is deleted by the retained-cycle cutoff.

## 8. Deletion-preserving and explicitly passive spectator grammars are subcritical

The mountain mechanism in Section 7 uses two exact properties:

1. simultaneous peak deletion gives the fixed core \(M_{h-1}\); and
2. the induced quotient action is cyclic rotation of its
   \(p=2h-1\) free-gap coordinates.

### Theorem 8.1 (one-generation deletion-preserving spectator rigidity)

Every rank-\(m\) Dyck root satisfying

\[
 \partial D=M_{h-1}                                \tag{8.0}
\]

belongs to the weak-composition fibre (7.3), on which the induced action
is the coordinate rotation used in Section 7.  In plane-tree language,
every attached
component outside the mountain core must disappear after one simultaneous
leaf deletion, and hence is only a height-one leaf bundle.  Therefore the
complete passive-graft class has exactly

\[
 \binom{m+h-2}{2h-2}                              \tag{8.1}
\]

members, and its terminal-zero subclass has exactly

\[
 \binom{m+h-3}{2h-3}.                             \tag{8.2}
\]

For \(h=\Theta(\sqrt m)\), both are
\(\exp(O(\sqrt m\log m))\).

#### Proof

Under the displayed deletion-preserving hypothesis, the inverse
peak-deletion theorem says that all such roots are obtained by the
compulsory leaf expansion followed by a
weak composition of the remaining free leaves among the
\(2(h-1)+1=p\) ordered slots.  A graft of height at least two leaves a
nonempty edge after leaf deletion and changes the core.  This proves the
classification.  Stars and bars gives (8.1)--(8.2). \(\square\)

There is also a chronology obstruction to concatenating an arbitrary
Dyck block while hoping that it remains passive.

### Theorem 8.2 (first-deepest block intrusion)

Let \(X\ne\varnothing\) be a Dyck word of height \(a<d\), and put

\[
 T_j=1^jX1^{d-j}0^d.                              \tag{8.3}
\]

While \(j+a<d\),

\[
 \boxed{\tau T_j=T_{j+1}.}                       \tag{8.4}
\]

At \(j=d-a\), the first global maximum occurs inside \(X\), so the
mountain factorization and the rotation law (8.4) cease.  Moreover

\[
 \tau(M_dX)=XM_d=T_0.                             \tag{8.5}
\]

Thus every nonempty suffix or prefix spectator leaves this inherited
mountain chart after at most \(d\) quotient phases, strictly before the
\((d+1)\)-phase parent mechanism over \(M_d\) would close.

#### Proof

When \(j+a<d\), the first maximum is reached at the last up-step in the
final mountain segment.  In the factorization \(D=P1R0S\), one has

\[
 P=1^jX1^{d-j-1},\qquad R=0^{d-1},\qquad S=\varnothing.
\]

The exact block rotation \(\tau D=S1P0R\) gives (8.4).  At
\(j=d-a\), \(X\) reaches height \(d\) before the final mountain does, so
the marked first-maximum step lies inside \(X\).  Finally, direct
factorization of \(M_dX=1^d0^dX\) gives (8.5). \(\square\)

If \(\operatorname {ht}(X)\ge d\), the inherited mountain chart is absent
already for the prefix \(XM_d\), and after the first update for the suffix
\(M_dX\).  Thus the omitted height range only makes intrusion earlier.

Theorems 8.1--8.2 do not rule out a new return whose spectator changes the
core and participates dynamically.  Indeed, a descending one-block
placement can retain a different tight return even though it has left the
parent chart.  The theorems prove only that such a construction is not an
amplification of the prime mountain rotor and needs a fresh all-phase
chronology proof.

Even granting every such new return does not rescue a decorated one-block
library.  Allow arbitrary leaf bundles in all \(p=2d+1\) corners and one
arbitrary Dyck block in one chosen corner.  This overcounts the library by

\[
 p[z^{m-d}](1-z)^{-(2d+1)}C(z).                  \tag{8.5a}
\]

Nonnegative coefficient evaluation at \(z=1/4\) gives

\[
 p[z^{m-d}](1-z)^{-(2d+1)}C(z)
 \le {8\over3}\,p\,4^m\left({4\over9}\right)^d. \tag{8.5b}
\]

Uniformly in the active Gaussian range

\[
 c\sqrt m\le d\le H=O_A(\sqrt m),                \tag{8.5c}
\]

the ratio of (8.5b) to \(B_m/H=\Theta_A(4^m/m^2)\) is at most
\(O_A(m^{5/2}(4/9)^d)=o(1)\).  Thus the complete decorated one-block
family is \(o(B_m/H)\), without using any return test, period test, or
conflict estimate.

There is a stronger entropy bound even if every apparently safe
descending-side corner is granted an arbitrary spectator.

### Theorem 8.3 (passive multi-corner entropy bound)

Let \(M_d\) have \(p=2d+1\) inverse corners.  Consider the deliberately
generous passive grammar in which

* arbitrary height-one leaf bundles may be placed in all \(p\) corners;
  and
* arbitrary Dyck forests may additionally be placed in all \(d+1\)
  descending or baseline corners,

while no surviving forest is allowed in an ascending corner whose
first-maximum intrusion occurs before phase \(d+1\).  The number of
rank-\(m\) objects in this grammar is at most

\[
 [z^{m-d}](1-z)^{-(2d+1)}C(z)^{d+1},              \tag{8.6}
\]

and hence

\[
 \boxed{
 [z^{m-d}](1-z)^{-(2d+1)}C(z)^{d+1}
 \le {8\over3}\,4^m\left({8\over9}\right)^d.}    \tag{8.7}
\]

Consequently, uniformly for \(d\ge c\sqrt m\) with fixed \(c>0\), the
whole passive grammar has

\[
 o(B_m/H)                                          \tag{8.8}
\]

objects, even after summing over \(O(\sqrt m)\) possible mountain depths.

#### Proof

Leaf bundles have generating function \((1-z)^{-1}\) per corner, and an
ordered Dyck forest has generating function \(C(z)\).  Granting both
choices independently gives the coefficient upper bound (8.6).  All
coefficients are nonnegative, so evaluation at \(z=1/4\), where
\(C(1/4)=2\), gives

\[
 [z^{m-d}](1-z)^{-(2d+1)}C(z)^{d+1}
 \le
 4^{m-d}\left({4\over3}\right)^{2d+1}2^{d+1},
\]

which simplifies to (8.7).  Since
\(B_m/H=\Theta_A(4^m/m^2)\), the factor
\(m^2(8/9)^d\) tends to zero uniformly for \(d\ge c\sqrt m\), and the
geometric tail absorbs the allowed depth sum. \(\square\)

This remains a passive-grammar theorem.  Synchronized multi-pruning
spectators could change the marked factorization and later compensate for
that change; such a mechanism lies outside (8.6) and needs a new period and
return proof.

## 9. The exact remaining global two-point gate

Let \(E_H\) be the set of genuine retained quotient starts whose first
return is at most \(2H-1\), and put

\[
 R_H=|E_H|,
 \qquad
 \mathcal C_H=
 \sum_{u=1}^{H+1}|E_H\cap\tau^{-u}E_H|.           \tag{9.1}
\]

The conflict graph has vertex set \(E_H\); two starts are adjacent when
their residence supports share an edge.  Every conflict occurs at a lag
at most \(H+1\) in one of the two directions.  Hence its degree sum is at
most \(2\mathcal C_H\).  Cauchy--Schwarz in the Caro--Wei bound gives

\[
 \boxed{
 \bar\nu_H^P
 \ge {R_H^2\over R_H+2\mathcal C_H}.}             \tag{9.2}
\]

Therefore, if for some \(\kappa_A>0\) and \(\chi_A<\infty\),

\[
 R_H\ge\kappa_A{B_m\over H},
 \qquad
 \mathcal C_H\le\chi_AR_H,                       \tag{9.3}
\]

then

\[
 \bar\nu_H^P
 \ge{\kappa_A\over1+2\chi_A}{B_m\over H},        \tag{9.4}
\]

and the deck lift gives

\[
 \nu_H(P_m)\ge
 \left({2\kappa_A\over A(1+2\chi_A)}+o_A(1)\right)
 B_m\sqrt m.                                      \tag{9.4a}
\]

This is the matching critical lower bound and refutes \(ST_A\).  On the
other hand, \(ST_A\), together with critical one-point mass, forces

\[
 \mathcal C_H/R_H\longrightarrow\infty.           \tag{9.5}
\]

This divergence is necessary, not sufficient, for the upper theorem.

The exact peak-deletion reduction makes (9.1) fully explicit.  For a
reduced root \(F\in\mathcal D_d\) with \(k\) peaks, put

\[
 P_m(F)=\binom{m+d-k}{2d},                        \tag{9.6}
\]

and let \(B_2(F)\) be the time of the second positive selection of the
immediate predecessor of the time-zero particle.  Define

\[
 a_H(F)=\mathbf1_{\{B_2(F)\le2H-1\}},             \tag{9.7}
\]

\[
 S_{m,H}=\sum_FP_m(F)a_H(F),                      \tag{9.8}
\]

\[
 K_{m,H}=\sum_{u=1}^{H+1}\sum_F
 P_m(F)a_H(F)a_H(\tau^uF).                        \tag{9.9}
\]

The exact Pascal transport and its saddle constants give

\[
 (3/4-o(1))S_{m,H}-o(B_m/H)
 \le R_H\le S_{m,H}+o(B_m/H),                    \tag{9.10}
\]

\[
 (1/2-o(1))K_{m,H}-o(B_m/H)
 \le\mathcal C_H\le K_{m,H}+o(B_m/H).            \tag{9.11}
\]

Thus neither an outer Pascal factor nor an adjacent-deletion choice can
decide (9.3) or (9.5).  The unresolved object is exactly the weighted
short-lag autocorrelation (9.9) of the genuine predecessor-active set on
long reduced PBBS cycles.

### 9.1 Exact adjacent-label alternation and the residual coboundary

There is a sharper orbitwise normal form for the predicate in (9.7).
Work on one particle-augmented reduced PBBS orbit \(\mathcal O\) of length
\(L\), with \(p=2d+1\) persistent equality-particle labels.  Component
homomesy gives

\[
 q={L\over p}                                      \tag{9.12}
\]

selections of every label.  Fix adjacent labels \(b,a=b+1\).  Let
\(t_{b,i}\) be the cyclically ordered \(b\)-selection times and

\[
 g_{b,i}=t_{b,i+1}-t_{b,i}.                       \tag{9.13}
\]

At every \(a\)-phase, no overtaking gives

\[
 T_a<B_2,                                          \tag{9.14}
\]

where \(T_a\) is the next \(a\)-selection and \(B_2\) is the second
future \(b\)-selection.  Thus an interval between consecutive
\(a\)-selections contains at most one \(b\)-selection.  Since both labels
occur exactly \(q\) times, every such interval contains exactly one.
The two selection sets therefore strictly alternate around the orbit.

Let \(s_{b,i}\) be the unique \(a\)-selection in

\[
 t_{b,i-1}<s_{b,i}<t_{b,i},                       \tag{9.15}
\]

and define the terminal residual

\[
 r_{b,i}=t_{b,i}-s_{b,i}.                         \tag{9.16}
\]

Then

\[
 1\le r_{b,i}\le g_{b,i-1}-1,                    \tag{9.17}
\]

and the exact predecessor time is

\[
 \boxed{
 B_2(s_{b,i})-s_{b,i}=r_{b,i}+g_{b,i}.}           \tag{9.18}
\]

If \(h_{b,i}=s_{b,i+1}-s_{b,i}\) is the corresponding successor-label
gap, then

\[
 \boxed{
 h_{b,i}=g_{b,i}+r_{b,i}-r_{b,i+1}.}              \tag{9.19}
\]

Thus the active count on \(\mathcal O\) is exactly

\[
 \boxed{
 A_G(\mathcal O)=
 \sum_{b,i}\mathbf1_{\{r_{b,i}+g_{b,i}\le2H-1\}}.} \tag{9.20}
\]

This is the count on the particle-augmented orbit.  Its contribution to
the unaugmented Pascal census is normalized by the augmentation degree:

\[
 {P_m\over p}A_G(\mathcal O).                    \tag{9.20a}
\]

The unknown is an integral residual-phase coboundary, not an unmarked
renewal-gap histogram.

For one Pascal cell of total mass \(\mathsf M_m(d,k)\), the exact weighted
Kac identities are

\[
 \sum_{\mathcal O}{P_m\over p}\sum_{b,i}1
 =\mathsf M_m(d,k),                               \tag{9.21}
\]

\[
 \sum_{\mathcal O}{P_m\over p}\sum_{b,i}g_{b,i}
 =p\,\mathsf M_m(d,k).                            \tag{9.22}
\]

Hence the mean same-label renewal gap \(g\) is exactly \(p\), including
\(p=m+O(\sqrt{m\log m})\) in the saddle tube.  This scalar mean does not
control the lower tail of the predecessor-passage delay \(r+g\) in
(9.18).

The loss of information is exact even after strict alternation is imposed.
Let \(p\ge5\), put

\[
 P=2p,\qquad \ell=2p-3,                           \tag{9.23}
\]

and place the two \(b\)-visits at \(0,\ell\).  Compare the two strictly
alternating \(a\)-visit sets

\[
 a_{\rm early}=\{1,\ell+1\},
 \qquad
 a_{\rm late}=\{\ell-1,\ell+2\}.                 \tag{9.24}
\]

For both labels in both systems, the complete ordered cyclic gap sequence
is \((\ell,3)\), up to cyclic shift.  Nevertheless the two
second-predecessor-time pairs are

\[
 (\ell+2,\ell+2)
 \quad\hbox{and}\quad
 (4,\ell+1),                                      \tag{9.25}
\]

respectively.  Hence for every

\[
 4\le G<\ell+1,                                   \tag{9.26}
\]

the early coupling has no active phase and the late coupling has exactly
one.  The latter active phase \(\ell-1=2p-4\) is even, so the distinction
survives passage from the one-step map to \(\tau=\phi^2\).

This last construction is an abstract alternating adjacent-label coupling,
not a claim of realization by a whole PBBS orbit.  It proves sharply that
even both complete marginal renewal cycles and all their Kac scalars do not
determine (9.20).  A global proof must control the actual PBBS residuals
\(r_{b,i}\), their cross-label alignment, and the even-phase restriction.

## 10. Audit of constants, floors, and implication scope

1. **Largest allowed gap.**  A return gap \(2s+1\le2H-1\) has
   \(s\le H-1\).  Its positive run has \(s+1\le H\) owner states and its
   complete positive arc has \(s+2\le H+1\) transition edges.

2. **Short-cycle cutoff.**  Length at most \(H+1\) is the correct cutoff:
   on longer quotient cycles every active support is proper and has
   distinct quotient edges.

3. **Circular constant.**  The additive one in
   \(\tau_C\le\nu_C+1\) is paid once per active cycle, and the number of
   active cycles is at most the aggregate packing.  This gives exactly
   the factor two in (2.5).

4. **Two-shore constant.**  The three shifted copies in (2.6) give
   \(J_H\le3\tau_H^P\), and circular piercing gives
   \(\tau_H^P\le2\nu_H^P\).  Hence the combined constant is six, not
   three.

5. **Deck scale.**  \(NB_m=\binom{2m+1}{m}\).  Dividing the physical
   target \(o(B_m\sqrt m)\) by \(N\sim2m\) gives the quotient target
   \(o(B_m/\sqrt m)\), equivalently \(o(B_m/H)\) for fixed \(A\).

6. **Mountain support length.**  The return (7.5) has quotient duration
   \(h\), positive residence \(h+1\), and full transition support
   \(h+2=L\).  The definition (7.4) requires \(L\) following positives,
   which is sufficient but not minimal; replacing \(L\) by any
   \(h+O(1)\) isolation length gives the same asymptotic constant.

7. **Mountain retention.**  Activity needs \(h+1\le H\), while retention
   needs \(p=2h-1>H+1\).  The strict range \(A/2<c<A\) is a uniform
   sufficient range; the two boundary values are floor-sensitive.

8. **Mountain constant.**  The zero-coordinate density contributes
   \(2c/\sqrt m\), isolation contributes \(e^{-2c^2}\), and reciprocal
   support length contributes \(c\sqrt m\).  Their product is
   \(2c^2e^{-2c^2}\).

9. **No global lower claim.**  Equation (7.15) is stretched exponential,
   whereas \(B_m=\exp((\log4+o(1))m)\).  Neither phase lifting nor prime
   period changes this exponential gap.

10. **No profile-to-PBBS claim.**  Equations (4.8) and (4.11) are formal
    product-menu statements, while (5.7) is an iterated fixed-\(k\)
    harmonic limit.  A decorated PBBS return tower must additionally
    satisfy the ordered phase intersections (6.14); no diagonal
    \(k=A\sqrt m\) claim is made.

11. **Renewal marginal caveat.**  Equations (9.23)--(9.26) preserve the
    full cyclic gap sequences of both adjacent labels and strict
    alternation, but change the active count.  They are an information
    obstruction, not a synthetic PBBS orbit.

## 11. Final proved boundary

Proved:

* exact equivalence of fully adaptive left/right histories on a frozen arc
  family and integral circular-interval transversals;
* exact capacitated Hall feasibility and the factor-two circular bound;
* constant-factor equivalence of the full \(G_H+P_H\) and positive-only
  gates;
* exact one-level and serial formal port-index minimax loads;
* critical \(e/k\) saturation in the iterated fixed-\(k\) harmonic
  zero-slot limit;
* an explicit PBBS failure of the zero-slot-to-return converse;
* a literal retained prime-period PBBS packing occupying a positive
  fraction of local reciprocal capacity;
* exact obstruction to one-generation deletion-preserving and explicitly
  defined passive-grammar spectator amplifications of that packing; and
* the exact adjacent-label alternation/coboundary normal form
  (9.18)--(9.20), and reduction of the remaining global decision to
  (9.8)--(9.11).

Not proved:

* \(\bar\nu_H^P=o_A(B_m/H)\), hence \(ST_A\);
* \(\bar\nu_H^P=\Omega_A(B_m/H)\) on the full Catalan family;
* boundedness or divergence of \(K_{m,H}/S_{m,H}\) on long Pascal-saddle
  cores;
* a recursive multi-pruning spectator construction satisfying all actual
  phase identities; or
* a factor-rewiring evolving \(AO_A/SDH_A\) whose earlier switches change
  later support graphs.

The frozen-support interval-piercing and local product-menu route is
therefore exhausted at the critical scale.  A factor-rewiring evolving
\(AO_A/SDH_A\), and diagonal Gaussian fixed-coefficient correlations, remain
open.  Any proof which keeps the same frozen literal intervals must add a
genuinely global PBBS chronology theorem; reorienting those intervals or
their formal local ports cannot supply the missing little-oh factor.
