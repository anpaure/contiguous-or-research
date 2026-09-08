# Early Catalan four-bin splitting is erased at the next parent scale

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Let \(p=2m+1\), and choose the first Catalan scale

\[
 s=\min\{t:\operatorname {Cat}_t\ge p\},\qquad
 d=\operatorname {Cat}_s=\theta p.
 \tag{0.1}
\]

Then

\[
 1\le\theta<4-\frac6{s+1},
 \tag{0.2}
\]

so, as an abstract capacity problem, \(d\) tokens fit into four bins of
capacity \(p\).  This does **not** give a recursive PCap construction.

There are two exact obstructions.

1. The presently available MSW coordinate-component packets cannot make
   four bins even at this one scale.  Every even-pair coordinate move
   preserves the total target mass on each two-point coordinate orbit.
2. More generally, suppose an arbitrary port-valid replacement succeeds
   in labelling or splitting the size-\(s\) child fibre.  If it is installed
   strictly inside that child hole, the next matched parent window contains
   both complementary child boundary states.  Their local intersection is
   empty, so the parent target is independent of the internal replacement.
   All child labels are erased at that next scale.

The Catalan arithmetic makes the loss decisive.  Put

\[
 \gamma_s=\frac{\operatorname {Cat}_{s+1}}
                 {\operatorname {Cat}_s}
          =4-\frac6{s+2}.
 \tag{0.3}
\]

Then the next fibre has size

\[
 \operatorname {Cat}_{s+1}=\gamma_s\theta p,
\qquad
 4-o(1)\le\gamma_s\theta<16-o(1),
 \tag{0.4}
\]

which is exactly the fatal overshoot interval.  Moreover the aligned-context
normalization changes by \(1+o(1)\), so the reappearing demand has the same
leading order:

\[
 H_{m,s+1}\left(\frac{\operatorname {Cat}_{s+1}}2-p\right)
 =(1+o(1))H_{m,s}\operatorname {Cat}_s
   \left(\frac12-\frac1{\gamma_s\theta}\right).
 \tag{0.5}
\]

The coefficient in parentheses ranges asymptotically from \(1/4\) to
\(7/16\).

Thus early four-bin splitting does not propagate upward.  A viable
construction must use a **parent-aligned** packet which changes an entrance
or exit state of the serviced child window.  This is exactly the unresolved
parent-routing gate; same-hole port-valid packets cannot replace it.

## 1. Exact Catalan scale ledger

Write \(C_t=\operatorname {Cat}_t\).  The Catalan quotient is

\[
 \frac{C_t}{C_{t-1}}
 =\frac{2(2t-1)}{t+1}
 =4-\frac6{t+1}.
 \tag{1.1}
\]

Minimality in (0.1) gives \(C_{s-1}<p\le C_s\), and therefore

\[
 1\le\theta=\frac{C_s}{p}
 <\frac{C_s}{C_{s-1}}
 =4-\frac6{s+1}.
 \tag{1.2}
\]

At the next scale,

\[
 \theta^+:=\frac{C_{s+1}}p
 =\left(4-\frac6{s+2}\right)\theta.
 \tag{1.3}
\]

Consequently

\[
 4-\frac6{s+2}\le\theta^+
 <\left(4-\frac6{s+2}\right)
   \left(4-\frac6{s+1}\right)
 =16-O(s^{-1}).
 \tag{1.4}
\]

This is not merely analogous to the later fatal cutoff.  It is that cutoff,
one Catalan level earlier: the first scale at which \(C_s\) reaches \(p\)
is followed immediately by a scale in the \(4p\)-to-\(16p\) overshoot
window.

## 2. Exact context normalization

Let

\[
 H_{m,t}=\frac12\binom{2(m-t)}{m-t}
 \tag{2.1}
\]

be the number of aligned size-\(t\) contexts.  Put \(k=m-s\).  Then

\[
 \frac{H_{m,s+1}}{H_{m,s}}
 =\frac{\binom{2(k-1)}{k-1}}{\binom{2k}{k}}
 =\frac{k}{2(2k-1)}.
 \tag{2.2}
\]

Multiplying by (0.3) gives

\[
 \boxed{
 \frac{H_{m,s+1}C_{s+1}}{H_{m,s}C_s}
 =\frac{k(2s+1)}{(2k-1)(s+2)}.}
 \tag{2.3}
\]

In the intended regime \(s=\Theta(\log p)=o(m)\), the right side is
\(1+o(1)\).  Hence the next-scale plateau is not suppressed by the
one-quarter loss in context count: the approximately fourfold Catalan
growth cancels it.

The certified plateau demand at the next scale is

\[
 D_{s+1}
 =H_{m,s+1}\left(\frac{C_{s+1}}2-p\right).
 \tag{2.4}
\]

Using (2.3),

\[
 \boxed{
 \frac{D_{s+1}}{H_{m,s}C_s}
 =
 \frac{k(2s+1)}{(2k-1)(s+2)}
 \left(\frac12-\frac1{\gamma_s\theta}\right).}
 \tag{2.5}
\]

Equations (1.4) and (2.5) prove (0.5).  Uniformly through the asymptotic
overshoot interval, the coefficient lies between \(1/4-o(1)\) and
\(7/16+o(1)\).

The plateau theorem applies with this same size-\((s+1)\) invisible block
at every protected depth

\[
                         s+1\le q\le Q\le m/2.
\tag{2.6}
\]

Consequently, if the inner four-bin labels are erased and no
parent-aligned repair is made, the hereditary cap ledger retains at least

\[
 (Q-s)\,
 H_{m,s+1}\left(\frac{C_{s+1}}2-p\right)
 =\Omega\!\left(\frac{QW}{s^{3/2}}\right).
\tag{2.7}
\]

For the coefficient-one window \(Q=p^{1/4}\) and
\(s=\Theta(\log p)\), the right side is not \(o(W)\); indeed its ratio to
\(W\) tends to infinity.  Thus erasure at one parent level is enough to
defeat the proposed hereditary recursion, not merely one isolated depth.

## 3. Same-hole label erasure

Consider an aligned size-\(s\) child hole with local ground set \(J\).
Every rooted port-valid local factor has, in the row rooted at
\(P\in\mathcal D_s\), the two prescribed boundary states

\[
                         P,\qquad J\setminus P.
 \tag{3.1}
\]

Let a larger matched parent window contain the complete child slab,
including both states in (3.1).  Write \(O\) for the fixed exterior part
of its intersection target.

### Theorem 3.1 (full-child erasure)

For every internal port-valid replacement of the child hole, the local
contribution to the matched parent intersection is empty, and the physical
parent target is exactly \(O\).  In particular it is independent of

* the internal path through the child;
* the local factor chosen in the hole;
* every shorter-window target label created inside the hole; and
* every ownership-component choice used to create that label.

#### Proof

The parent intersection contains both boundary states in (3.1).  Hence its
local part is contained in

\[
 P\cap(J\setminus P)=\varnothing.
 \tag{3.2}
\]

Conversely all coordinates in \(O\) occur outside the replaced slab and
are unchanged.  Thus the complete intersection is \(O\), independently of
all internal states. \(\square\)

There is a dual union statement: a parent union containing both ports has
local contribution

\[
 P\cup(J\setminus P)=J,
 \tag{3.3}
\]

again independent of the child replacement.

### Corollary 3.2 (four labels do not persist)

Suppose a size-\(s\) child replacement partitions its distinguished
shorter-window occurrences among any number of labels, four in particular.
After embedding the replacement strictly inside the next matched parent
context, all those labels induce the same full-parent target.  Thus the
labelling cannot lower the next-scale plateau in (2.4).

This is a statewise obstruction, not an entropy or typicality argument.
It applies to arbitrary integral port-valid child factors, not only to
MSW coordinate conjugates.

### Corollary 3.3 (zero-channel tower)

Consider any finite tower of strict one-hole substitutions in which every
descendant replacement preserves its two prescribed complementary ports.
For an ancestor matched window containing the complete descendant slab,
the ancestor target is independent of **all** choices made below that
descendant boundary.

#### Proof

Apply Theorem 3.1 at the lowest boundary crossed completely by the ancestor
window.  The entire descendant is replaced, as far as the intersection is
concerned, by the empty local contribution (or by \(J\) for the union
dual).  Repeating upward removes every deeper choice. \(\square\)

Thus ordinary port substitution has zero information capacity from an
internal label to a full-ancestor matched target.  Adaptively choosing
among more internal factors does not help.  Information can leave the hole
only by changing the exported boundary state or by enlarging the interface.

## 4. The stronger obstruction for the present coordinate packets

The available bounded component packets compare the canonical MSW factor
with an even-pair coordinate conjugate.  Let

\[
 H_s=\langle(2\,3),(4\,5),\ldots,(2s\,\,2s+1)\rangle.
 \tag{4.1}
\]

Every component switch replaces rows by their images under \(H_s\).
Therefore, for every \(H_s\)-orbit \(\mathcal O\) of physical targets,

\[
                         \sum_{T\in\mathcal O}\mu(T)
 \tag{4.2}
\]

is invariant.

For the first distinguished singleton pair, the canonical masses are

\[
 \mu(2)=C_s,\qquad \mu(3)=C_{s-1}.
 \tag{4.3}
\]

Thus every factor reachable by any sequence of these coordinate-component
moves satisfies

\[
 \boxed{
 K_p\big|_{\{2,3\}}
 \ge \big(C_s+C_{s-1}-2p\big)_+.}
 \tag{4.4}
\]

Equivalently, with

\[
 \alpha_s=\frac{C_{s-1}}{C_s}
          =\frac{s+1}{2(2s-1)}
          =\frac14+O(s^{-1}),
 \tag{4.5}
\]

the right side is

\[
 p\big(\theta(1+\alpha_s)-2\big)_+.
 \tag{4.6}
\]

It vanishes only for

\[
 \theta\le\frac2{1+\alpha_s}
          =\frac85+O(s^{-1}).
 \tag{4.7}
\]

So in most of the early Catalan overshoot interval the current packet menu
cannot form four bins even before the parent-erasure theorem is invoked:
the target orbit containing the source has only two cells.

## 5. Why distinct successive contexts do not evade erasure

One might try to send different first-generation packet blocks into
different parent contexts.  Two exact structural facts prevent this from
being an automatic recursion.

1. An ownership component of the \(s_1\) comparison has root block

   \[
   \mathcal A_jR
   =
   \{1u0R:u\in\mathcal D_{j+1}\}
   \mathbin{\dot\cup}
   \{10\,1v0R:v\in\mathcal D_j\}.
   \tag{5.1}
   \]

   This is not a complete one-hole context fibre \(C[\mathcal D_t]\).
   Hence the port-substitution theorem cannot be recursively applied inside
   one component as though it were an independent child hole.
2. Component partitions for different even-pair swaps are not laminar.
   Already on \(\mathcal D_3\), the \(s_1=(2\,3)\) partition

   \[
   \{110010,101010\}\ \dot\cup\
   \{111000,110100,101100\}
   \tag{5.2}
   \]

   and the \(s_2=(4\,5)\) partition

   \[
   \{101010,101100\}\ \dot\cup\
   \{111000,110100,110010\}
   \tag{5.3}
   \]

   cross in all four intersections.

Thus a second component stage cannot, from port-validity alone, act inside
one first-generation label class.  It mixes those labels.  If the stages
are nested in one physical hole, Theorem 3.1 erases them at the parent
scale; if they are placed in overlapping parents, their complete
lower-shadow profiles form one joint atom unless an additional product
theorem is proved.

## 6. Exact surviving theorem

The early-scale idea would become valid only with a parent-aligned library
having all of the following properties.

1. It changes an entrance or exit state of the serviced size-\(s\) child
   window, so Theorem 3.1 does not apply.
2. Its distinguished target map uses at least

   \[
                  \left\lceil C_{s+1}/p\right\rceil
   \tag{6.1}
   \]

   genuinely different residual target classes.
3. The complete crossing-window histograms, not merely the distinguished
   labels, satisfy the multidepth residual-capacity dual.
4. Its independently rounded joint atoms have target multiplicity
   \(O(p)\).

These are precisely the parent-transversal dispersion and fragmentation
conditions already isolated in the residual-capacity theorem.  The
early-scale four-bin proposal does not weaken them: without a
boundary-changing parent packet, its labels are erased before the fatal
scale is reached.

## 7. Decision

\[
\boxed{
\begin{minipage}{0.88\linewidth}
Port-valid four-bin splitting strictly inside the first Catalan
\(p\)-scale cannot bootstrap to coefficient-one PCap.  The next Catalan
level lies in the fatal \(4p\)-to-\(16p\) range at unchanged normalized
mass, while the matched parent window contains both fixed child ports and
therefore forgets every internal label.  Coordinate-component packets are
additionally trapped in two-point target orbits.  A new parent-aligned,
boundary-changing packet is necessary.
\end{minipage}}
\tag{7.1}
\]
