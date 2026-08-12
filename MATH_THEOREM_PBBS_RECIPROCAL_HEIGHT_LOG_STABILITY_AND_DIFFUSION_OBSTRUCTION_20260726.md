# PBBS reciprocal-height stability: logarithmic stable blocks are negligible, but height saturation is diffuse

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,\qquad
 H_A=\lceil A\sqrt m\rceil,                                   \tag{0.1}
\]

where \(A>0\) is fixed.  Let \(\mathcal P\) be a pairwise
quotient-edge-disjoint family of nonwrapping PBBS short returns of
step-two duration at most \(H_A\).

There is a new chronology-sensitive little-oh theorem.  For a return
\(I\), let \(G(I)\) be the maximum number of consecutive transitions in
its step-two core over which the transported canonical first-deepest
frame remains canonical.  For every fixed \(0<a<A\), every integer
\(q\le a\sqrt m/2\), and every such family,

\[
 \boxed{
 \#\{I\in\mathcal P:
       a\sqrt m\le h(I)\le A\sqrt m,\ G(I)\ge q\}
 \le C_{a,A}2^{-q}B_m.}                                      \tag{0.2}
\]

Consequently, for every fixed \(\varepsilon>0\), with

\[
 q_m=\left\lceil\left({1\over2}+\varepsilon\right)
                    \log_2m\right\rceil,                     \tag{0.3}
\]

\[
 \boxed{
 \#\{I:a\sqrt m\le h(I)\le A\sqrt m,\ G(I)\ge q_m\}
 =o_{a,A,\varepsilon}(B_m/\sqrt m).}                         \tag{0.4}
\]

Unlike the existing slow-reframing theorem, (0.2) needs only **one**
long stable block.  Arbitrarily many frame changes elsewhere in the
return are allowed.

Combining (0.4) with the audited slow-reframing contraction gives the
following stability statement.  If for some \(c>0\)

\[
                         |\mathcal P|\ge c\,{B_m\over\sqrt m} \tag{0.5}
\]

along a subsequence, then, after discarding \(o(B_m/\sqrt m)\) and an
arbitrarily small fixed fraction, a positive critical subfamily satisfies
simultaneously

\[
 \boxed{
 \begin{gathered}
  a\sqrt m\le h(I)\le A\sqrt m,\\
  R(I)\ge\delta s(I),\\
  G(I)<\left({1\over2}+\varepsilon\right)\log_2m+1,
 \end{gathered}}                                               \tag{0.6}
\]

for constants \(a,\delta>0\).  Thus any counterfamily to
\((QST_A)\), and hence to \((ST_A)\), must concentrate at critical mass
on the chronology class of **linearly and logarithmically densely
reframing returns**.

This is a genuine little-oh gain, but it does not close \((QST_A)\).
The stronger concentration principle proposed in the prompt does not
follow from reciprocal-height stability alone.  The height bound is a
direct sum over invariant height strata.  On every exact Gaussian height,

\[
 \boxed{|\mathcal P_h|\le C_{a,A}{B_m\over m}
        =o(B_m/\sqrt m).}                                     \tag{0.7}
\]

Hence a critical family in (0.5) must occupy
\(\Omega_{a,A,c}(\sqrt m)\) different exact height strata.  Reciprocal
height forces **diffusion**, not an atom in one exact-height chronology
class.  A positive critical family can in principle be spread over many
classes, each individually \(o(B_m/\sqrt m)\).

There is also an exact threshold obstruction.  The one-witness estimate
(0.2) beats \(B_m/\sqrt m\) precisely when

\[
                         q>{1\over2}\log_2m+\omega(1).         \tag{0.8}
\]

Below this half-logarithmic threshold it gives no vanishing factor.
Therefore a complete proof still needs a return-specific compatibility
theorem for the dense-reframing class in (0.6); neither the reciprocal
height sum nor the existing canonical-frame atlas supplies it.

## 1. Canonical stable blocks

Let the step-two core of \(I\) be

\[
 D_0(I),D_1(I),\ldots,D_{s(I)-1}(I).                          \tag{1.1}
\]

For \(0\le j\le s(I)-q-1\), call \(j\) a \(q\)-stable start when the
canonical first-deepest frame of \(D_j(I)\), transported formally through
the next \(q\) applications of the literal sector map, remains canonical
at every displayed phase.

The maximum stable-block length \(G(I)\) is the largest \(q\) for which
such a start exists.  This definition concerns the actual canonical
frames along the PBBS trace.  It is not a static prescribed overlay.

Let \(c_{m,h}^{(q)}\) be the number of semilength-\(m\), height-\(h\)
Dyck roots which are \(q\)-stable.  The exact partial-atlas theorem and
its Gaussian coefficient audit give, uniformly for

\[
                         a\sqrt m\le h\le A\sqrt m,\qquad
                         0\le q\le h/2,                       \tag{1.2}
\]

\[
                         c_{m,h}^{(q)}
                         \le C_{a,A}4^m2^{-q}h^{-4}.           \tag{1.3}
\]

Summing over the Gaussian band yields

\[
 \boxed{
 \sum_{\lceil a\sqrt m\rceil\le h\le\lfloor A\sqrt m\rfloor}
 c_{m,h}^{(q)}
 \le C_{a,A}2^{-q}B_m.}                                      \tag{1.4}
\]

The factor \(2^{-q}\) is coefficient-correct; it comes from the exact
two-strip kernels for the partial canonical atlas.

## 2. One stable block gives an injective witness

### Theorem 2.1 (long stable-block packing contraction)

Under the hypotheses of (0.2), inequality (0.2) holds.

#### Proof

For every counted interval \(I\), choose the earliest \(q\)-stable start
\(j(I)\) and mark the root \(D_{j(I)}(I)\).  Pairwise
quotient-edge-disjointness makes all roots occurring in all selected
cores globally distinct.  Hence the marked roots are distinct.

Height is invariant under the normalized PBBS map, so every marked root
has height \(h(I)\).  It belongs to the \(q\)-stable atlas counted in
(1.4).  The injection

\[
                         I\longmapsto D_{j(I)}(I)              \tag{2.1}
\]

therefore gives

\[
 |\{I:a\sqrt m\le h(I)\le A\sqrt m,\ G(I)\ge q\}|
 \le
 \sum_{a\sqrt m\le h\le A\sqrt m}c_{m,h}^{(q)}
 \le C_{a,A}2^{-q}B_m.                                       \tag{2.2}
\]

This proves the theorem. \(\square\)

### Corollary 2.2 (the half-logarithmic little-oh gain)

For \(q_m\) as in (0.3), the left side of (0.4) is at most

\[
 C_{a,A}2^{-q_m}B_m
 \le C_{a,A}B_m m^{-1/2-\varepsilon}
 =o(B_m/\sqrt m).                                             \tag{2.3}
\]

The same conclusion holds for any

\[
                         q_m-{1\over2}\log_2m\longrightarrow+\infty.
                                                                    \tag{2.4}
\]

No assumption on the total number \(R(I)\) of frame changes is used.

## 3. The critical chronology concentration that is actually proved

The previous diffuse-reframing theorem supplies two facts.

1. There is a function \(\eta(a)\downarrow0\) such that all returns of
   height below \(a\sqrt m\) have packing capacity at most

   \[
                         \eta(a){B_m\over\sqrt m}+o(B_m/\sqrt m).
                                                                    \tag{3.1}
   \]

2. For every fixed Gaussian band and every \(\gamma\downarrow0\), the
   family with

   \[
                         R(I)\le\gamma s(I)                    \tag{3.2}
   \]

   has normalized packing mass tending to zero as
   \(\gamma\downarrow0\).  Quantitatively, its limsup is bounded by
   \(C_{a,A}2^{-c/\gamma}\).

### Theorem 3.1 (critical dense-reframing stability)

Assume (0.5) along an infinite sequence of \(m\)'s.  Fix
\(\varepsilon>0\).  Then there are constants \(a,\delta,\kappa>0\),
depending only on \(A,c,\varepsilon\), and subfamilies
\(\mathcal P_m^\star\subseteq\mathcal P_m\) such that

\[
                         |\mathcal P_m^\star|
                         \ge\kappa {B_m\over\sqrt m},          \tag{3.3}
\]

and every \(I\in\mathcal P_m^\star\) satisfies (0.6).

#### Proof

Choose \(a>0\) so small that the small-height bound (3.1) is at most
\(cB_m/(4\sqrt m)\) along the subsequence.  Since \(s(I)\le H_A\) and
the height-gap theorem gives \(h(I)\le s(I)\), no height exceeds
\((A+o(1))\sqrt m\).

Next choose \(\delta>0\) so small that the audited slow-reframing bound
for \(R(I)\le\delta s(I)\), on the remaining Gaussian band, is at most
\(cB_m/(4\sqrt m)\).

Finally Corollary 2.2 shows that the family with
\(G(I)\ge q_m\) is \(o(B_m/\sqrt m)\), where \(q_m\) is given by
(0.3).  Remove these three families.  For all sufficiently large \(m\),
at least

\[
                         {c\over3}{B_m\over\sqrt m}            \tag{3.4}
\]

members remain.  They satisfy (0.6), after harmless adjustment of floors.
Take any fixed \(\kappa<c/3\). \(\square\)

Theorem 3.1 is the rigorous reciprocal-height stability statement
available from the present chronology technology.  A critical
near-saturator must reframe on a positive fraction of transitions and
cannot contain even one stable block longer than the half-logarithmic
threshold, except on a little-oh subfamily.

## 4. Height stability is diffuse, not atomic

Write

\[
                         \mathcal P_h=\{I\in\mathcal P:h(I)=h\}. \tag{4.1}
\]

The height-local edge-capacity inequality is

\[
                         (h+2)|\mathcal P_h|\le b_{m,h},       \tag{4.2}
\]

where \(b_{m,h}\) is the number of semilength-\(m\) Dyck roots of exact
height \(h\).

At \(q=0\), estimate (1.3) is the Gaussian local-height bound

\[
                         b_{m,h}\le C_{a,A}4^mh^{-4}
                         \le C'_{a,A}{B_m\over\sqrt m}         \tag{4.3}
\]

for \(a\sqrt m\le h\le A\sqrt m\).  Combining (4.2)--(4.3) gives

\[
                         |\mathcal P_h|
                         \le C''_{a,A}{B_m\over m}.            \tag{4.4}
\]

### Proposition 4.1 (no exact-height concentration)

If a Gaussian-band family has size at least \(cB_m/\sqrt m\), then it
meets at least

\[
                         {c\over C''_{a,A}}\sqrt m             \tag{4.5}
\]

different exact height strata.

#### Proof

Each height stratum contributes at most (4.4).  Divide the assumed total
by that maximum contribution. \(\square\)

Thus the reciprocal-height inequality has no stability principle forcing
a positive critical fraction into one exact height, or into any
chronology partition which refines exact height.  It forces a critical
family to spread across order \(\sqrt m\) individually negligible
classes.

More generally, define the utilization

\[
                         \theta_{m,h}
 ={(h+2)|\mathcal P_h|\over b_{m,h}}\in[0,1].                  \tag{4.6}
\]

If the total packing has positive critical mass, a layer-cake argument
does imply that \(\theta_{m,h}\) is bounded below on a set of height
levels carrying positive reciprocal spectral mass.  It does not imply an
atom at one height.  This is exactly the direct-sum geometry of the
height-spectrum proof.

## 5. The sharp half-logarithmic boundary

Theorem 2.1 uses one distinct \(q\)-stable witness per interval.  Its
right side is \(C2^{-q}B_m\).  Relative to the critical target
\(B_m/\sqrt m\), the resulting factor is

\[
                         C\sqrt m\,2^{-q}.                     \tag{5.1}
\]

It tends to zero precisely in the range (2.4).  At

\[
                         q={1\over2}\log_2m+O(1),              \tag{5.2}
\]

it remains only \(O(1)\); below (5.2) it is larger than the original
critical big-oh bound.

The exact Boltzmann retention identity for one prescribed stable block is

\[
 2^{-q}{(h+1)(h+2)\over
 (w+1)(w+2-\mathbf1_{\{q\ {\rm odd}\}})},
 \qquad w=h-\lfloor q/2\rfloor.                               \tag{5.3}
\]

For \(q=o(h)\), this is \((1+o(1))2^{-q}\).  Since a Gaussian trace has
\(\Theta(\sqrt m)\) possible starts, the crossover
\(\sqrt m\,2^{-q}\asymp1\) is exactly (5.2).  Formula (5.3) is a
calibration of the atlas; it does not assert independence between
overlapping starts.

Consequently there is no overlap between the range where a single stable
block is forced by a naive binary-word argument and the range where
(0.2) is little-oh.  Any improvement at the boundary must use
compatibility among successive **frame changes**, or the actual PBBS
return equations, rather than only the inventory of frame-preserving
windows.

## 6. Exact boundary for \(ST_A\)

The proved gain is:

\[
 \boxed{
 \text{long stable block, sublinear reframing, small height, and short
 quotient-cycle sectors are all }o_A(B_m/\sqrt m).}           \tag{6.1}
\]

Thus a failure of \(QST_A\) can be assumed, at positive critical mass, to
lie in the dense chronology class (0.6), as well as in the previously
audited long-period, linear-defect Pascal-saddle sector.

What is not proved is

\[
 \#\{I:\ R(I)\ge\delta s(I),\
          G(I)<({1\over2}+\varepsilon)\log_2m\}
                         =o_A(B_m/\sqrt m).                    \tag{6.2}
\]

The reciprocal-height spectrum by itself cannot prove (6.2), because it
sees only the direct sum of invariant height-edge capacities.  The exact
partial atlas supplies (5.3) for preserving windows but no negative
correlation or Hall expansion among the changing windows.

Accordingly, a full little-oh theorem now needs one of:

1. an entropy loss for the complete dense-reframing itinerary;
2. a return-specific incompatibility between the endpoint passage
   equations and logarithmically dense frame changes; or
3. a trace-overlap theorem showing that roots in the class (6.2) cannot
   attain positive utilization simultaneously across
   \(\Omega(\sqrt m)\) height strata.

No one of these three final statements is proved here.  Therefore the
note advances \(ST_A\) by a new little-oh chronology sector and gives a
quantitative obstruction to the proposed stronger concentration step,
but it does not prove coefficient one.
