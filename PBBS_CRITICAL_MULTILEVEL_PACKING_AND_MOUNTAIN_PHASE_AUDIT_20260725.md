# Critical PBBS multilevel packing: the exact mountain phase and a descendant-capacity ceiling

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Verdict

Put

\[
 B_r=\operatorname {Cat}_r.
\]

Consider a genuine zero-winding PBBS return of step-two duration/height
\(s\), with first-mountain pruning depth \(p\), and put

\[
 q=s-p,\qquad \partial^pD=M_q=1^q0^q,
 \qquad b=2q-p+1.
\tag{0.1}
\]

The unsaturated condition is \(p<2q\), equivalently \(b\ge2\).  The
critical residual has

\[
 p\asymp q\asymp s\asymp\sqrt r.
\tag{0.2}
\]

This note does not prove the required little-oh packing theorem.  It proves
two exact facts which sharply delimit the remaining argument.

1.  The last inverse fibre above the stopping mountain is a literal cyclic
    rotation action on weak compositions into \(2q+1\) slots.  The tight
    Pascal fan forces one cyclic block of \(p\) slots to be zero.  If the
    terminal curvature is one, there are exactly

    \[
       b=2q+1-p
    \]

    admissible phase anchors.  Under the critical capacity measure,
    terminal curvature one has conditional probability \(1-O(1/p)\).
    Thus the last inverse level is maximally permissive rather than a
    source of an \(o(1)\) phase loss.

2.  The complete triangular descendant fan at all pruning levels is an
    exact stochastic refinement of the original parent interval.  At
    level \(j\), its \(j+1\) descendant intervals have total trace volume
    \((j+1)(s-j)\), but every ancestral top edge is reused as many as
    \(j+1\) times.  For every nonnegative combination of all levelwise
    fibre-capacity inequalities, this multiplicity cancels exactly.  Such
    an argument can never improve the elementary quotient packing scale

    \[
       B_r/s=\Theta(B_r/\sqrt r).
    \]

The result is a genuine no-go for additive multilevel descendant volume,
not for PBBS packing itself.  A proof of coefficient one must use a joint
cross-level non-reuse statistic, a profile--boundary correlation, or a
signed/nonlinear chronology functional.  Merely adding every triangular
descendant and charging it to its ordinary inverse fibre cannot give the
missing little-oh.

## 1. The inverse fibre immediately above a mountain

Let

\[
 K=2q+1.
\tag{1.1}
\]

Every Dyck word \(E\) whose simultaneous peak deletion is \(M_q\) is
obtained by adding one mandatory leaf at the unique leaf of the path and
then distributing a free mass \(y\ge0\) among the \(K\) ordered child
slots.  Write the free weak composition as

\[
 \mathbf z=(z_0,z_1,\ldots,z_{2q}),
 \qquad z_i\ge0,\qquad \sum_i z_i=y.
\tag{1.2}
\]

In contour notation the corresponding word is

\[
 \begin{aligned}
 E(\mathbf z)={}&(10)^{z_0}e_1(10)^{z_1}\cdots
 e_q(10)^{z_q+1}e_{q+1}(10)^{z_{q+1}}\cdots
 e_{2q}(10)^{z_{2q}},
 \end{aligned}
\tag{1.3}
\]

where

\[
 e_1=\cdots=e_q=1,
 \qquad e_{q+1}=\cdots=e_{2q}=0.
\]

The extra one in \((10)^{z_q+1}\) is the mandatory child of the old
path leaf.

### Theorem 1.1 (exact mountain-fibre rotor)

For the step-two PBBS quotient map \(\tau\),

\[
 \boxed{
 \tau E(z_0,z_1,\ldots,z_{2q})
 =E(z_{2q},z_0,z_1,\ldots,z_{2q-1}).}
\tag{1.4}
\]

Thus the complete one-step inverse fibre of \(M_q\) is the cyclic
rotation action on weak \(K\)-compositions of \(y\).

#### Proof

Use the exact first-maximum block rotation

\[
 E=P1R0S,
 \qquad \tau E=S1P0R.
\tag{1.5}
\]

In (1.3), the marked \(1\) is the first up-step in the mandatory peak
after \(e_q\), and the displayed \(0\) in (1.5) is the final core
down-step \(e_{2q}\).  Hence

\[
 \begin{aligned}
 P&=(10)^{z_0}e_1(10)^{z_1}\cdots e_q,\\
 R&=0(10)^{z_q}e_{q+1}(10)^{z_{q+1}}\cdots
       e_{2q-1}(10)^{z_{2q-1}},\\
 S&=(10)^{z_{2q}}.
 \end{aligned}
\tag{1.6}
\]

Substitute (1.6) into \(S1P0R\).  The new leading \(1\), followed by
the first \(q-1\) old core up-steps, becomes the new path core.  The last
old core up-step becomes its mandatory leaf peak.  The initial marked
peak down-step in \(R\), followed by the old core down-steps, becomes the
new descending half.  Regrouping the inserted \(10\)-blocks gives exactly

\[
 (z_0',z_1',\ldots,z_{2q}')
 =(z_{2q},z_0,\ldots,z_{2q-1}),
\]

which proves (1.4). \(\square\)

## 2. The exact terminal zero block

At pruning level \(p\), the tight-return fan contains the \(p+1\)
returns whose starts are the consecutive quotient phases

\[
 0,1,\ldots,p.
\tag{2.1}
\]

For each adjacent pair, the right child begins one quotient phase after
the leader child.  The exact equality-particle spacing formula is

\[
 \Delta=2z+1,
\tag{2.2}
\]

where \(z\) is the corresponding free inverse-slot occupancy.  Since the
right child begins at the immediately following quotient phase, its
leader and predecessor have spacing one.  Therefore \(z=0\).

Theorem 1.1 transports these \(p\) phase-local terminal slots to \(p\)
consecutive entries of one fixed composition vector.  Rotating the slot
labels, we may take the condition to be

\[
 \boxed{z_0=z_1=\cdots=z_{p-1}=0.}
\tag{2.3}
\]

This recovers, now with the phase action explicit, the final factor in the
full Pascal-fan envelope.

### Corollary 2.1 (one-anchor and two-anchor fibres)

For fixed free mass \(y\ge1\), the number of mountain-fibre vectors
satisfying (2.3) is

\[
 \boxed{
 A_y(p,q)=\binom{y+b-1}{y}.}
\tag{2.4}
\]

If a second phase anchor is displaced by \(d\), where

\[
 0\le d<b,
\tag{2.5}
\]

then its terminal zero block and (2.3) have union size \(p+d\).  The
number satisfying both terminal blocks is therefore

\[
 \boxed{
 A_y^{(2,d)}(p,q)=\binom{y+b-d-1}{y}.}
\tag{2.6}

At \(d=b\), the two blocks cover all \(K\) slots, so the intersection is
empty because \(y\ge1\).

#### Proof

Condition (2.3) leaves \(K-p=b\) free boxes, giving (2.4).  By the
rotation law (1.4), the second anchor fixes the translate
\(\{d,d+1,\ldots,d+p-1\}\).  Under (2.5) the union is one nonwrapping
block of size \(p+d\), leaving \(b-d\) boxes.  Stars and bars gives
(2.6).  The endpoint case is immediate. \(\square\)

In particular,

\[
 \frac{A_y^{(2,d)}}{A_y}
 =\prod_{i=0}^{d-1}
   \frac{b-1-i}{y+b-1-i}.
\tag{2.7}
\]

For \(y=1\), this becomes the exact linear law

\[
 \boxed{
 \frac{A_1^{(2,d)}}{A_1}=\frac{b-d}{b}.}
\tag{2.8}
\]

Thus two phase anchors a fixed positive fraction of the way across the
available terminal arc still have a fixed positive fraction of their
one-anchor capacity in common.

## 3. Terminal curvature one dominates the critical capacity law

In the exact profile generating function, the last curvature \(y_p\) has
the positive-series factor

\[
 \sum_{y\ge1}\binom{y+b-1}{y}t_p^y
 =(1-t_p)^{-b}-1.
\tag{3.1}
\]

At the critical point,

\[
 t_p=\frac1{(p+1)^2}.
\tag{3.2}
\]

Normalize (3.1) to a probability law.

### Proposition 3.1 (critical last-fibre law)

Uniformly when

\[
 c_1p\le b\le c_2p
\tag{3.3}
\]

for fixed positive constants \(c_1,c_2\),

\[
 \boxed{
 \Pr(y_p=1\mid y_p\ge1)=1-O_{c_1,c_2}(p^{-1}).}
\tag{3.4}

For a unit vector \(\mathbf z\), the number of phase anchors whose
terminal \(p\)-block is zero is exactly

\[
 \boxed{K-p=b.}
\tag{3.5}

#### Proof

The conditional probability in (3.4) equals

\[
 \frac{bt_p}{(1-t_p)^{-b}-1}.
\tag{3.6}
\]

Here \(bt_p=\Theta(1/p)\).  Expanding the positive binomial series gives

\[
 (1-t_p)^{-b}-1
 =bt_p\bigl(1+O(bt_p+t_p)\bigr),
\]

which proves (3.4).  If \(y_p=1\), exactly one slot is positive.  A
cyclic \(p\)-block is zero precisely when it avoids that slot.  There are
\(K-p=b\) such starts, proving (3.5). \(\square\)

This proposition concerns the exact normalized **capacity** measure.  It
does not assert that all the terminally admissible anchors lift through
the upper inverse levels to genuine parent returns.  Its rigorous
consequence is narrower and important: the last inverse level cannot be
the source of the missing little-oh.  On the dominant critical terminal
fibre it permits \(\Theta(p)\) phase anchors, and (2.8) shows constant
two-anchor overlap throughout a fixed fraction of that arc.

## 4. A sharp cyclic-cover obstruction at the last level

The preceding local phase geometry also saturates ordinary interval
packing.  Consider the rotation orbit of a unit composition.  It has
period \(K\), and its terminally admissible anchors form one block of
\(b\) consecutive residues.

Let a top cyclic cover of this orbit have degree \(a\), hence length
\(aK\).  Attach to every admissible anchor a candidate parent trace of
length \(s+O(1)\), as every genuine duration-\(s\) return would have.
Since

\[
 s=p+q<3q<\frac32K,
\tag{4.1}
\]

choosing one fixed admissible residue in every second lap gives

\[
 \boxed{
 \Omega(a)=\Omega(aK/s)}
\tag{4.2}
\]

pairwise edge-disjoint candidate traces, after discarding at most one trace
at the circular seam.  This matches the elementary length upper bound up
to an absolute constant.

The word *candidate* is essential: terminal fan admissibility is necessary,
not sufficient, for a genuine outer PBBS return.  Formula (4.2) proves an
exact obstruction to any argument which uses only

* the stopping-mountain inverse fibre,
* its cyclic-cover degrees, and
* the terminal fan zero block.

Those data alone permit critical, length-saturating edge-disjoint
packings.  Any strict gain must come from upper inverse levels or from the
closed boundary chronology.

## 5. Complete triangular descendants do not enlarge capacity

We now use the entire genuine tight-return fan, rather than only its last
inverse level.

Let \(I\) be a genuine zero-winding quotient return of duration \(s\).
Use the half-open quotient phase block

\[
 P(I)=\{0,1,\ldots,s-1\}
\tag{5.1}
\]

for its \(s\) deficit-carrying step-two edges.  At pruning level
\(0\le j\le p\), the exact fan has the \(j+1\) descendant blocks

\[
 P_{j,a}(I)=\{a,a+1,\ldots,a+s-j-1\},
 \qquad 0\le a\le j.
\tag{5.2}
\]

They all lie in \(P(I)\), and their union is \(P(I)\).  Their total
occurrence volume is

\[
 \boxed{
 \sum_{a=0}^j|P_{j,a}(I)|=(j+1)(s-j).}
\tag{5.3}

Let \(\mathcal P\) be a pairwise quotient-edge-disjoint family of such
parent returns, all with the same \((s,p)\).  For a reduced quotient edge
\(e\), put

\[
 F_j(e)=\#\{D\in\mathcal D_r:\partial^jD=e\}.
\tag{5.4}
\]

The fibres partition the top quotient edge set, so

\[
 \sum_eF_j(e)=B_r.
\tag{5.5}
\]

Let \(L_{j,e}\) be the total traversal multiplicity of \(e\) across all
blocks (5.2), over every parent in \(\mathcal P\).

### Theorem 5.1 (triangular descendant-capacity inequality)

For every \(0\le j\le p\) and every reduced edge \(e\),

\[
 \boxed{L_{j,e}\le(j+1)F_j(e).}
\tag{5.6}
\]

Consequently,

\[
 \boxed{
 |\mathcal P|(j+1)(s-j)\le(j+1)B_r,}
\tag{5.7}
\]

and hence

\[
 \boxed{|\mathcal P|\le\frac{B_r}{s-j}.}
\tag{5.8}

#### Proof

Every occurrence of a reduced edge in a descendant block is the
\(j\)-fold peak-deletion image of the top edge at the same clock phase.
At a fixed level \(j\), one top phase belongs to at most \(j+1\) of the
sliding blocks (5.2).  The parent blocks are pairwise top-edge-disjoint,
so a top edge is used by at most one member of \(\mathcal P\).  Among all
top edges there are exactly \(F_j(e)\) preimages of \(e\).  This proves
(5.6).

Sum (5.6) over \(e\), use (5.5), and compare with the exact per-parent
volume (5.3).  This proves (5.7)--(5.8). \(\square\)

In the unsaturated sector,

\[
 s-j\ge s-p=q>\frac{s}{3}.
\tag{5.9}
\]

Thus every individual descendant level gives only a constant multiple of
the elementary critical bound \(B_r/s\).

### Theorem 5.2 (all nonnegative level combinations remain critical)

For arbitrary nonnegative weights \(w_0,\ldots,w_p\),

\[
 \boxed{
 |\mathcal P|
 \sum_{j=0}^p w_j(j+1)(s-j)
 \le
 B_r\sum_{j=0}^p w_j(j+1).}
\tag{5.10}

If the left coefficient is nonzero, the resulting cardinality upper bound
is

\[
 B_r\,
 \frac{\sum_jw_j(j+1)}
      {\sum_jw_j(j+1)(s-j)}
 \ge\frac{B_r}{s}.
\tag{5.11}

Therefore no proof consisting only of a nonnegative scalar combination of
the complete levelwise descendant-fibre capacities can establish

\[
 |\mathcal P|=o(B_r/s).
\tag{5.12}

#### Proof

Multiply (5.7) by \(w_j\) and sum in \(j\), proving (5.10).  Since
\(s-j\le s\), the denominator in (5.11) is at most \(s\) times its
numerator.  This proves (5.11)--(5.12). \(\square\)

The cancellation is structural.  The triangular fan creates \(j+1\)
descendant intervals at level \(j\), but it also reuses each ancestral
edge up to \(j+1\) times.  Counting the full fan rather than one canonical
lineage therefore supplies no hidden factor of \(p\).

## 6. Exact implication boundary

Theorems 1.1--5.2 remove two plausible shortcuts.

1. **No last-level phase loss.**  At critical \(p,b\asymp\sqrt r\), the
   terminal curvature is one with capacity probability \(1-o(1)\), and
   the mountain-fibre rotor leaves \(\Theta(\sqrt r)\) admissible anchors.
   Its cyclic covers admit length-saturating candidate packings.

2. **No additive descendant amplification.**  Even the complete genuine
   triangular fan, at all \(p+1\) levels and with exact inverse-fibre
   capacities, cannot beat \(B_r/s\) through nonnegative level-volume
   charging.

What remains possible is genuinely joint chronology.  A successful theorem
must prove at least one of the following in the critical sector:

* an upper-level phase transversality statement showing that the
  \(\Theta(p)\) terminally admissible anchors cannot lift through the same
  inverse tower except on an \(o(1)\) fraction of sheets;
* a cross-level non-reuse theorem in which one top edge cannot pay the
  same selected parent at many pruning levels, using data finer than the
  scalar image \(\partial^jD\);
* a joint profile--boundary collision estimate, so that the prescribed
  weak-composition values and the common endpoint word are not marginally
  compatible at critical mass; or
* a signed/nonlinear packing functional which detects the relative
  positions of the triangular descendants rather than only their total
  occurrence volume.

The surviving coefficient-one question is therefore not whether the
Pascal fan has enough descendants.  It has the maximum possible triangular
family.  The issue is whether actual PBBS chronology forces those
descendants to occupy *new joint capacity*, rather than repeatedly using
the same ancestral interval mass.

