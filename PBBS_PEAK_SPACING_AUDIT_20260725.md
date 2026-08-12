# Exact audit of the inverse peak-spacing identity

Date: 2026-07-25

No computation or external input is used.

## 1. Outcome

The candidate identity

\[
\Delta=2z+1
\]

is correct, provided that \(z\) is identified precisely: it is the number
of newly inserted leaf peaks in the **terminal root corner** of the
normalized pruned plane tree.  In particular, for every nonempty pruned
core this corner is noncompulsory.  The alternative in which the
distinguished corner is an old-leaf corner cannot occur in this application.

More is true.  For a fixed pruned core, the terminal occupancy required by
a physical return is determined exactly by the equality-particle itinerary.
This gives an exact fixed-occupancy fibre formula and an exact return kernel.
It also shows the limitation of the spacing identity by itself: occupancy
zero may have fibre ratio one, so there is no uniform entropy loss at one
pruning step.  Any iterative gain must use the correlation between the
prescribed occupancies and the successive PBBS itineraries.

## 2. Contour expansion of an inverse peak-deletion fibre

Let

\[
E=e_1e_2\cdots e_{2d}
\]

be a nonempty Dyck word.  Its plane tree has \(2d+1\) ordered child
corners.  In contour-word coordinates these are exactly the gaps before,
between, and after the letters of \(E\).  Consequently every Dyck word
\(D\) with \(\partial D=E\) has a unique expression

\[
\boxed{
D=(10)^{z_0}e_1(10)^{z_1}e_2\cdots
e_{2d}(10)^{z_{2d}} .}
\tag{2.1}
\]

Here every \(z_i\) is nonnegative, and

\[
z_i\ge 1
\quad\hbox{whenever the gap }(e_i,e_{i+1})
\hbox{ is a peak }10.
\tag{2.2}
\]

There are no other lower bounds.  In particular, the terminal variable

\[
z_\infty:=z_{2d}
\tag{2.3}
\]

is unconstrained, because it is the child corner of the root after its last
old child.  It is not the corner of an old leaf.

To prove (2.1), observe that adding one leaf child in a specified plane-tree
corner inserts one contour peak \(10\) in the corresponding word gap.
Conversely, every peak deleted by \(\partial\) is such a newly inserted leaf.
An old leaf of the core has one child corner, and at least one leaf must be
inserted there to prevent the old peak of \(E\) itself from being deleted;
this gives exactly (2.2).

## 3. The spacing identity

Normalize the original cyclic PBBS state as \(0D\), with the leading zero
the unique unmatched coordinate.  Let \(a\) be the distinguished equality
particle immediately before that zero, and let \(b=a-1\) be its immediate
cyclic predecessor.  Choose order-preserving integer lifts of their physical
edge positions and put

\[
\Delta=x_a(0)-x_b(0).
\tag{3.1}
\]

### Theorem 3.1 (exact terminal spacing)

With \(z_\infty\) as in (2.3),

\[
\boxed{\Delta=2z_\infty+1.}
\tag{3.2}
\]

#### Proof

Every nonempty Dyck word ends in zero.  In the expanded word (2.1), the
physical segment from the last core letter \(e_{2d}=0\) to the leading
unmatched zero is

\[
0(10)^{z_\infty}0.
\tag{3.3}
\]

The edge entering the first zero in (3.3) is an equality edge.  Indeed, if
the preceding core gap is not expanded, then the preceding core letter is
zero; if it is a core peak, its compulsory inserted block ends in zero.
This equality edge is particle \(b\).

Inside the open segment following that edge, all successive bit pairs
alternate.  The only next equality edge is the final \(00\)-edge entering
the leading unmatched zero, namely particle \(a\).  Their destination-edge
coordinates are separated by the \(2z_\infty\) inserted sites and one final
step.  Hence their lifted separation is \(2z_\infty+1\).  \(\square\)

Thus the ``adjacent'' case is exactly \(z_\infty=0\).  It is also exactly
the word condition that \(D\) ends in \(00\), in agreement with the
gap-seven classification.

## 4. Exact fixed-occupancy fibre

Let the core \(E\) have \(d\) edges and \(k\) leaves, and let the parent
have \(r\) edges.  Put

\[
L=r-d-k,
\qquad
M=L+2d=r+d-k.
\tag{4.1}
\]

After the \(k\) compulsory insertions, \(L\) free leaves are distributed
among \(2d+1\) corners.  Since the terminal root corner is noncompulsory,
fixing \(z_\infty=z\) gives

\[
\boxed{
F_{r,z}(E)=
\binom{r+d-k-z-1}{2d-1}
=\binom{M-z-1}{2d-1}}
\tag{4.2}
\]

for \(0\le z\le L\), and zero otherwise.  Relative to the full fibre

\[
F_r(E)=\binom{M}{2d},
\tag{4.3}
\]

the exact mass is

\[
\boxed{
\frac{F_{r,z}(E)}{F_r(E)}
=\frac{2d}{M}
\prod_{j=0}^{z-1}\frac{L-j}{M-1-j}.}
\tag{4.4}
\]

Equivalently, the exact tail is

\[
\boxed{
\Pr_E(z_\infty\ge s)
=\frac{\binom{M-s}{2d}}{\binom{M}{2d}}
=\prod_{j=0}^{s-1}\frac{L-j}{M-j}.}
\tag{4.5}
\]

Formula (4.2) is stars and bars after fixing one of the \(2d+1\) free
coordinates.  Formulae (4.4)--(4.5) follow by division.

The case \(z=0\) recovers

\[
\frac{F_{r,0}(E)}{F_r(E)}=\frac{2d}{r+d-k}.
\tag{4.6}
\]

There is no uniform contraction here: (4.6) equals one whenever
\(r=d+k\), that is, whenever every inserted leaf is compulsory.

## 5. Exact matching with the particle itinerary

Let \(\kappa_t(E)\) be the omitted-coordinate itinerary of the pruned PBBS,
labelled so that \(\kappa_0=a\), and put \(b=a-1\).  Define

\[
h(E)=\min\{t>0:\kappa_t(E)=a\},
\tag{5.1}
\]

and let \(T_j(E)\) be the time of the \(j\)-th occurrence of \(b\) after
time zero.

There is a useful universal ordering fact:

\[
\boxed{h(E)<T_2(E).}
\tag{5.2}
\]

Indeed, take any inverse expansion with terminal occupancy zero.  Such an
expansion always exists because the terminal root corner is noncompulsory.
After the time-zero move, the first selection of \(b\) moves it into the
old edge of \(a\).  A second selection of \(b\) cannot occur while \(a\)
still occupies the next edge.  Since equality particles never collide or
overtake, \(a\) must first be selected and vacate that edge.  The particle
itinerary depends only on \(E\), so (5.2) holds independently of the chosen
inverse expansion.

For \(g<2r+1\), set

\[
\mathcal Z_g(E)=
\{z\ge0:T_{2z+2}(E)\le g\}.
\tag{5.3}
\]

### Theorem 5.1 (exact return-occupancy criterion)

An inverse expansion \(D\) of \(E\), with terminal occupancy
\(z_\infty=z\), starts a consecutive physical omitted-label return by time
\(g\) if and only if

\[
\boxed{z\in\mathcal Z_g(E).}
\tag{5.4}
\]

The return time is then exactly \(T_{2z+2}(E)\).

#### Proof

At time zero particle \(a\) enters the returned edge.  It vacates that edge
at time \(h(E)\).  By order preservation, the next possible entrant is
\(b\).  If its initial lifted distance is \(\Delta\), then it must be
selected \(\Delta\) times before reaching the edge immediately behind the
target, and its next selection enters the target.  Thus the return time is
the \((\Delta+1)\)-st selection of \(b\).  Theorem 3.1 gives
\(\Delta+1=2z+2\).  By (5.2), the target has already been vacated before
\(T_{2z+2}(E)\).  Since \(g<2r+1\), particle \(a\) cannot
make a full physical circuit, and no other particle can overtake \(b\).
Therefore this entrance is the first repeated occurrence of the physical
label.  The converse is the same argument read backwards.  \(\square\)

Consequently the former passage upper bound can be sharpened to the exact
kernel

\[
\boxed{
|\mathcal R_g(r)|
=\sum_{d=1}^{r-1}\ \sum_{E\in\mathcal D_d}
  \sum_{\substack{z\in\mathcal Z_g(E)\\z\le r-d-\operatorname{pk}(E)}}
  \binom{r+d-\operatorname{pk}(E)-z-1}{2d-1}.}
\tag{5.5}
\]

The case \(d=0\) contributes nothing when \(g<2r+1\), because its unique
equality particle needs a full physical circuit to return.

The allowed occupancies form an initial interval.  If

\[
B_g(E)=\#\{1\le t\le g:\kappa_t(E)=b\},
\qquad
s_g(E)=\left\lfloor\frac{B_g(E)}2\right\rfloor-1,
\tag{5.6}
\]

then \(\mathcal Z_g(E)=\{0,1,\ldots,s_g(E)\}\), with the convention that
this set is empty when \(s_g(E)<0\).  Hence the contribution of a fixed
core can also be written exactly as

\[
\boxed{
F_r(E)-\binom{M-s-1}{2d},
\qquad s=\min\{L,s_g(E)\},}
\tag{5.7}
\]

when \(s_g(E)\ge0\), and as zero otherwise.  This is the hockey-stick sum
of (4.2).

## 6. What this does and does not give iteratively

Equation (5.5) is a genuine strengthening: the inverse terminal occupancy
is not merely empty or nonempty; it must match one exact odd passage count
in the smaller PBBS.  Nevertheless no one-step \(1/r\) saving follows.
The largest term is usually \(z=0\), its mass is (4.6), and that mass can
even be one.

There is a clean exact interpretation of repeated \(z=0\).  In a plane
tree, terminal occupancy zero means that the root's rightmost child is not
a newly deleted leaf.  Requiring terminal occupancy zero for \(J\)
successive pruning levels is equivalent to requiring the rightmost root-to-
leaf branch to have at least \(J+1\) edges.  The number of \(r\)-edge plane
trees with rightmost branch length at least \(s\) is

\[
\boxed{
T_{r,s}=[x^{r-s}]C(x)^{s+1}
=\frac{s+1}{2r-s+1}\binom{2r-s+1}{r-s}.}
\tag{6.1}
\]

Indeed an arbitrary prefix forest may precede each distinguished rightmost
spine child, giving the generating function

\[
(xC(x))^s C(x).
\tag{6.2}
\]

Uniformly for \(s=o(\sqrt r)\),

\[
\frac{T_{r,s}}{\operatorname{Cat}_r}
=(1+o(1))(s+1)2^{-s}.
\tag{6.3}
\]

Thus a long all-zero occupancy lineage does carry real entropy.  But this is
not yet a bound for returns: positive occupancies are allowed, and after
summing over all possible terminal profiles one recovers the entire class of
trees of the relevant height.  The exact gain can only come from showing
that the predecessor-selection count \(B_g(E)\) is usually too small to
capture the high-mass part of the kernel (4.4), or from using the two
endpoint lineages simultaneously.

In particular, the spacing identity alone does not establish an iterative
Catalan saving.  Its rigorous contribution is the exact arithmetic matching
(5.3)--(5.7), which is the correct starting point for such a proof.

## 7. Exact harmonic-tower obstruction to a seam-only induction

There is an even sharper reason that the identity alone cannot be iterated
as a product of empty-slot savings.  Let

\[
D_j=\partial^jD_0,
\qquad |D_j|=2r_j.
\tag{7.1}
\]

At the inverse step \(D_{j+1}\mapsto D_j\), the core \(D_{j+1}\) has

\[
\operatorname{pk}(D_{j+1})=r_{j+1}-r_{j+2}.
\tag{7.2}
\]

Therefore its full inverse fibre, conditional on the three ranks, has size

\[
\binom{r_j+r_{j+2}}{2r_{j+1}},
\tag{7.3}
\]

whereas the subfibre with terminal occupancy zero has size

\[
\binom{r_j+r_{j+2}-1}{2r_{j+1}-1}.
\tag{7.4}
\]

The exact conditional ratio is consequently

\[
\frac{2r_{j+1}}{r_j+r_{j+2}}.
\tag{7.5}
\]

Now choose an integer \(R\) divisible by \(1,2,\ldots,J+2\), and put

\[
r_j=\frac{R}{j+1}
\qquad(0\le j\le J+1).
\tag{7.6}
\]

All inverse free masses are nonnegative because

\[
r_j-2r_{j+1}+r_{j+2}
=\frac{2R}{(j+1)(j+2)(j+3)}>0,
\tag{7.7}
\]

and a bottom Dyck root with the required peak count exists.  Prescribing
terminal occupancy zero at every one of the \(J\) inverse levels retains
the exact fraction

\[
\begin{aligned}
\prod_{j=0}^{J-1}\frac{2r_{j+1}}{r_j+r_{j+2}}
&=\prod_{j=0}^{J-1}
  \frac{(j+1)(j+3)}{(j+2)^2}\\
&=\boxed{\frac{J+2}{2(J+1)}}
\longrightarrow\frac12.
\end{aligned}
\tag{7.8}
\]

The first two lower ranks are

\[
r_1=R/2,
\qquad r_2=R/3,
\tag{7.9}
\]

so the first inverse step lies at the critical Pascal saddle
\((d,k)=(R/2,R/6)\).

Thus even an unbounded tower of prescribed empty terminal seams need not
have vanishing **conditional fibre** mass.  This does not construct PBBS
passages on the harmonic tower, so it is not a counterexample to residence
packing.  It does prove that no argument multiplying only the spacing-slot
probabilities can close the theorem.  A successful iteration must use the
dynamical predecessor-passage condition in (5.6), or a capacity/clustering
statement coupling the two endpoint descendants.
