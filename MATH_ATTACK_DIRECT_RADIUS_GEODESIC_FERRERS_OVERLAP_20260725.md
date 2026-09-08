# Direct-radius geodesic chunks: the full Ferrers overlap kernel

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad H^2=(1+o(1))m\log m,
 \qquad Q=\lfloor\alpha H\rfloor,
 \tag{0.1}
\]

where \(1/\sqrt2<\alpha<1\).  Give the middle phases the exact
truncated radius law

\[
 c_d=N_d-N_{d+1}\quad(d<Q),\qquad c_Q=N_Q,
 \qquad N_q=\binom{2m}{m-q}.
 \tag{0.2}
\]

This note computes the overlap kernel of the return-free geodesic part and
gives two obstructions to using that computation as a coefficient-one
proof.

1.  The intersection of two full geodesic grids is not necessarily a
    rectangle or an ordinary Ferrers diagram.  After deleting unused rows
    and columns it is exactly a **skew Ferrers interval diagram**.  Formula
    (3.5) below is the exact area generating function of all such diagrams
    which survive pruning of compressed \(s\)-by-\(s\) rectangles.  The
    ordinary, possibly very non-square, Ferrers subseries is the Gaussian
    binomial formula

    \[
      \sum_{r=0}^{s-1}x^{r^2}{a\brack r}_x{b\brack r}_x.
      \tag{0.3}
    \]

2.  Coupling (3.5) to the ordered row- and column-block probabilities gives
    the coefficientwise overlap envelope (4.8).  After deleting the two
    axial sectors (one used row or one used column), its sharp logarithmic
    threshold, for the worst nibble fugacity \(x\asymp\log m\), is

    \[
      \boxed{
      s_{\rm cross}(m)
       ={\log m\over\log(C\log m)}+O(1)
       =(1+o(1)){\log m\over\log\log m}.}
      \tag{0.4}
    \]

    For every fixed \(\varepsilon>0\), taking

    \[
      s\le(1-\varepsilon)s_{\rm cross}(m)
      \tag{0.5}
    \]

    makes the residual genuinely two-dimensional hierarchy summable.
    Taking \(s\ge(1+\varepsilon)s_{\rm cross}(m)\) does not: the surviving
    \(g\)-by-\((s-1)\) Ferrers rectangle is already a nonsummable term.
    Thus square shapes alone give the wrong threshold; the long non-square
    Ferrers shapes determine it.

3.  There is **no value of \(s\ge2\)** for which uncontracted target-wise
    overlaps become summable.  A \(1\)-by-\(2\) Ferrers chain survives every
    \(s\)-square pruning.  Under (0.2), the vertical and shifted-Pascal
    cover pairs contribute on average

    \[
      \Omega\!\left({g\over\sqrt m}\right)
      =\Omega(\sqrt{\log m})
      \tag{0.6}
    \]

    to the normalized second overlap moment when \(g=\Theta(H)\), before
    its additional \((c/z)^2\) weight.  Calling those cover pairs
    `successor compatible' does not remove (0.6).  One needs an actual
    chain contraction/gluing theorem.

4.  The rectangle conflicts at the threshold (0.4) are statically tiny:

    \[
      \beta_s
      \le \exp\!\left[-(2+o(1)){(\log m)^2\over\log\log m}\right].
      \tag{0.7}
    \]

    Hence excluding the rectangle-conflict neighbourhood of any fixed
    grid retains \((1-o(1))D_g\) of its orbit, where

    \[
      D_g={1\over2}\binom{m+H}{m}(m)_g(H)_g,
      \qquad \log D_g=\Theta(g\log m).
      \tag{0.8}
    \]

    This is a static entropy statement, not hereditary residual control.

5.  Finally, direct \(Q=\alpha H\) is incompatible with a purely
    return-free geodesic realization.  A two-sided radius-\(d\) phase in a
    return-free carrier path needs \(2d\le H\).  The missing depths above
    \(H/2\) have total occurrence mass

    \[
      \sum_{H/2<q\le Q}N_q
       \ge W\,{m^{1/4+o(1)}\over\sqrt{\log m}}
       \gg W.
      \tag{0.9}
    \]

    They cannot be appended as an \(o(W)\) repair.  Therefore the present
    method proves a sharp cross-overlap theorem for the low-radius
    geodesic part, but it does not prove coefficient one.  What is still
    needed is a joint theorem which both contracts the axial Ferrers chains
    and realizes the returnful \(d>H/2\) columns inside the same integral
    extraction.

## 1. Exact radius mass and return-free chunks

The radius law (0.2) is forced by the tail equations

\[
 \sum_{d=q}^Qc_d=N_q.                                  \tag{1.1}
\]

Its first moment is

\[
 \boxed{\sum_{d=0}^Q d\,c_d=\sum_{q=1}^QN_q.}        \tag{1.2}
\]

At the calibrated height and for \(Q/\sqrt m\to\infty\), the local
central estimate gives

\[
 {1\over W}\sum_{q=1}^QN_q
   =\left({\sqrt\pi\over2}+o(1)\right)\sqrt m.        \tag{1.3}
\]

Consider a return-free monotone Johnson geodesic

\[
 X_t=C\cup\{a_{t+1},\ldots,a_g\}
          \cup\{b_1,\ldots,b_t\},\qquad 0\le t\le g. \tag{1.4}
\]

Its union has size \(m+g\).  If a central interval of \(\ell\) phases is
buffered to radius \(d\), its first and last certificate owners are
separated by \(\ell+2d-1\) transitions.  Hence containment in a carrier of
size \(m+H\) forces

\[
 \boxed{\ell+2d-1\le H.}                              \tag{1.5}
\]

This condition is independent of how the MTF state is written: every one
of the \(\ell+2d-1\) arrivals in a return-free geodesic is a new member of
the union.

For radii \(d\le(1/2-\varepsilon)H\), one may take
\(\ell_d\ge\varepsilon H\).  The separate-radius reset estimate then is

\[
 \begin{aligned}
 R_{\rm geo}
 &\le \sum_{d\le(1/2-\varepsilon)H}
       {(2d+1)c_d\over\ell_d}+O(H^2)\\
 &\le {C_\varepsilon\over H}
       \left(W+2\sum_{q\le Q}N_q\right)+O(H^2)\\
 &=O_\varepsilon\!\left({W\over\sqrt{\log m}}\right)=o(W).
                                                               \tag{1.6}
 \end{aligned}
\]

Thus the exact radius profile does solve the reset ledger on the portion
where return-free chunks exist.  It does not remove the upper-radius
barrier proved next.

## 2. The direct-radius barrier

### Proposition 2.1 (return-free radius ceiling)

If one phase of a carrier path has a return-free geodesic certificate of
radius \(d\) on both sides, then \(2d\le H\).

#### Proof

The certificate contains \(2d\) consecutive geodesic transitions.  Their
arrival coordinates are pairwise distinct and none belongs to the first
owner.  The union of these \(2d+1\) owners consequently has size
\(m+2d\).  It lies in a carrier of size \(m+H\), so \(2d\le H\). \(\square\)

The radius law requires \(N_q\) phase columns to reach depth \(q\).  Put
\(q_0=\lfloor H/2\rfloor+1\).  Uniformly for \(q=O(H)\),

\[
 {N_q\over W}=\exp\!\left(-{q^2\over m}+o(\log m)\right).  \tag{2.1}
\]

In particular,

\[
 N_{q_0}=Wm^{-1/4+o(1)}.                              \tag{2.2}
\]

For \(0\le j\le c m/H\), the exact consecutive-layer ratio

\[
 {N_{q+1}\over N_q}={m-q\over m+q+1}                 \tag{2.3}
\]

shows that \(N_{q_0+j}\ge e^{-C c}N_{q_0}\).  Since
\(Q-q_0\gg m/H\), summing the first \(\lfloor c m/H\rfloor\) terms gives

\[
 \sum_{q_0\le q\le Q}N_q
 \ge c'{m\over H}N_{q_0}
 =W\,{m^{1/4+o(1)}\over\sqrt{\log m}}.                \tag{2.4}
\]

This proves (0.9).  Notice the distinction between starts and targets:
\(N_{q_0}=o(W)\) high-radius starts exist, but their nested columns contain
much more than \(W\) high-depth target occurrences in total.  A nongeodesic
joint trajectory could still compile them cheaply.  A literal repair or a
pure return-free geodesic decomposition cannot.

## 3. Exact shape generating function

Write one full geodesic grid as

\[
 G_{i,j}=C\cup\{a_{i+1},\ldots,a_g\}
              \cup\{b_1,\ldots,b_j\},
 \qquad 0\le i,j\le g.                                \tag{3.1}
\]

After reversing the first coordinate, meet and join are coordinatewise
minimum and maximum.  If \({\cal G}'\) is a second grid, then
\({\cal L}={\cal G}\cap{\cal G}'\) is a sublattice.

### Lemma 3.1 (compressed intersections are skew Ferrers diagrams)

Delete every unused row and column of \({\cal L}\).  If the compressed
diagram has \(a\) rows and \(b\) columns, there are integers

\[
 1=l_1\le l_2\le\cdots\le l_a\le b,
 \qquad
 1\le r_1\le r_2\le\cdots\le r_a=b                 \tag{3.2}
\]

such that

\[
 {\cal L}=\{(i,j):l_i\le j\le r_i\}.                 \tag{3.3}
\]

Moreover \(l_i\le r_i\), and every column is used, equivalently

\[
 l_{i+1}\le r_i+1\quad(1\le i<a).                    \tag{3.4}
\]

Conversely, every diagram satisfying (3.2)--(3.4) is a sublattice of a
product of two chains.

#### Proof

Suppose row \(i\) contains columns \(p<q\), and column \(j\), with
\(p<j<q\), is used in another row.  Meeting or joining that point with
\((i,p)\) or \((i,q)\), according to which side its row lies on, produces
\((i,j)\).  Hence every row section is an interval in the compressed
columns.

If \(i<i'\) but \(l_i>l_{i'}\), meeting and joining the two left endpoints
produce a point in row \(i\) strictly to the left of \(l_i\), a
contradiction.  Thus the left endpoints are nondecreasing.  The same
argument applies to the right endpoints.  Compression gives \(l_1=1\),
\(r_a=b\), and (3.4).

For the converse, take \((i,p)\) and \((i',q)\), with \(i<i'\).  The
monotonicity of both boundaries shows that
\((i,\min\{p,q\})\) and \((i',\max\{p,q\})\) lie in the displayed row
intervals.  Thus the diagram is closed under meet and join. \(\square\)

For \(s\ge2\), the diagram contains a compressed \(s\)-by-\(s\) rectangle
if and only if some \(s\) row intervals have at least \(s\) common
columns.  Monotonicity makes consecutive rows extremal.  Therefore it
survives the pruning precisely when

\[
 r_i-l_{i+s-1}+1\le s-1\qquad(1\le i\le a-s+1).      \tag{3.5a}
\]

Define the exact compressed-shape polynomial

\[
 \boxed{
 {\sf S}^{(<s)}_{a,b}(x)
 =\sum_{(l,r)\ {m satisfying}\ (3.2)-(3.5a)}
   x^{\sum_{i=1}^a(r_i-l_i+1)}.}                      \tag{3.5}
\]

This is a finite transfer formula for the complete residual intersection
catalogue.  It counts ordinary Ferrers diagrams, skew Ferrers diagrams,
hooks, non-square rectangles, and disconnected diagonal contacts.  No
shape is replaced by its bounding square.

For comparison, the ordinary Ferrers subseries inside an \(a\)-by-\(b\)
box has the familiar exact Durfee decomposition

\[
 \boxed{
 {\sf F}^{(<s)}_{a,b}(x)
  =\sum_{r=0}^{s-1}x^{r^2}{a\brack r}_x{b\brack r}_x.} \tag{3.6}
\]

Indeed, after removing the \(r\)-by-\(r\) Durfee square, the part to its
right fits in an \(r\)-by-\((b-r)\) rectangle and the part below it fits in
an \((a-r)\)-by-\(r\) rectangle.  If exact height \(a\) and exact width
\(b\) are desired, inclusion-exclusion gives

\[
 {\sf F}^{(<s),\mathrm{ex}}_{a,b}
 ={\sf F}^{(<s)}_{a,b}-{\sf F}^{(<s)}_{a-1,b}
  -{\sf F}^{(<s)}_{a,b-1}+{\sf F}^{(<s)}_{a-1,b-1}.  \tag{3.7}
\]

Formula (3.6), rather than the single term \(x^{s^2}\), is the missing
non-square Ferrers contribution.

## 4. Coupling shapes to the geodesic orbit

Choose \(a\) compressed rows of the first grid.  If the successive
physical row gaps are

\[
 \delta=(\delta_1,\ldots,\delta_{a-1}),\qquad
 \delta_i\ge1,qquad |\delta|\le g,                  \tag{4.1}
\]

then there are \(g-|\delta|+1\) translations of this profile.  Sharing all
used rows identifies, in order, the disjoint departure blocks of sizes
\(\delta_1,\ldots,\delta_{a-1}\).  Conditional on one anchor cell, their
orbit probability is at most

\[
 {\prod_i\delta_i!\over(m-g)_{|\delta|}}.             \tag{4.2}
\]

The analogous assertion holds for the column gaps.  This is stronger than
using only the two endpoints: an endpoint estimate has the larger factor
\(1/\binom{m-g}{|\delta|}\) and loses the boundary-order information.

For completeness, define

\[
 P_{g,1}=g+1,                                         \tag{4.3}
\]

and, for \(a\ge2\),

\[
 \boxed{
 P_{g,a}
 =\sum_{\substack{\delta\in\mathbb N^{a-1}\\|\delta|\le g}}
   (g-|\delta|+1)
   {\prod_i\delta_i!\over(m-g)_{|\delta|}}.}         \tag{4.4}
\]

### Lemma 4.1 (ordered boundary pinning)

In the fully labelled geodesic orbit, fix one grid \({\cal G}\).  For an
embedded compressed intersection diagram with \(a\) used rows, \(b\) used
columns, and prescribed physical gap profiles \(\delta,\epsilon\), the
proportion of grids in any fixed tag orbit which realize that diagram is
at most

\[
 4\,{\prod_i\delta_i!\over(m-g)_{|\delta|}}
    {\prod_j\epsilon_j!\over(m-g)_{|\epsilon|}}.      \tag{4.5}
\]

#### Proof

Follow a monotone boundary walk of the compressed diagram.  It visits every
used row and column.  Across a row jump, the set difference exposes the
corresponding block of \(a\)-coordinates; across a column jump it exposes
the corresponding block of \(b\)-coordinates.  A simultaneous diagonal
jump exposes the two blocks separately as the two directed set
differences.  Thus the physical cells determine all the ordered disjoint
blocks in (4.1) and its column analogue.

Conditioned on the anchor, the stabilizer of that Boolean set is transitive
on ordered disjoint blocks of the prescribed sizes.  Their number is

\[
 {(r)_{|\delta|}\over\prod_i\delta_i!}
 \quad\hbox{and}\quad
 {(2m-r)_{|\epsilon|}\over\prod_j\epsilon_j!},        \tag{4.6}
\]

where \(m-g\le r,2m-r\).  Inverting (4.6) gives the displayed bound
conditional on the anchor.  The unconditional tag-orbit proportion is no
larger, since the probability of containing the anchor is at most one.
The factor four allows the two grid orientations and reversal of the
geodesic presentation.  The same calculation, with the anchor probability
left in rather than discarded, is the normalized one-cell link bound.
\(\square\)

Let \(x\ge1\).  Intersecting a radius-profile strip with another strip can
only remove cells from the intersection of the two full grids.  After
normalizing by the tag-orbit degree (or, in the regular replicated
catalogue, by the common one-cell reference degree), the following is a
coefficientwise upper generating function for all strip collisions after
\(s\)-square pruning:

\[
 \boxed{
 {\mathfrak C}_{g,s}(x)
 =4\sum_{a=1}^{g+1}\sum_{b=1}^{g+1}
       P_{g,a}P_{g,b}{\sf S}^{(<s)}_{a,b}(x).}         \tag{4.7}
\]

The singleton term is
\(4(g+1)^2x\).  The genuine overlap polynomial is therefore

\[
 \boxed{
 {\mathfrak C}^{(\ge2)}_{g,s}(x)
 ={\mathfrak C}_{g,s}(x)-4(g+1)^2x.}                  \tag{4.8}
\]

Equations (3.5), (4.4), and (4.8) are the requested complete
profile-boundary collision envelope.  It is an upper envelope rather than
an equality because a pair of grids can contain several certified
subdiagrams; all coefficients are nonnegative, so this overcount is safe.
No marginal owner and shadow probabilities have been multiplied: (4.5) is
one joint stabilizer-orbit count.

## 5. The axial sector: an obstruction for every \(s\)

For every \(s\ge2\),

\[
 {\sf S}^{(<s)}_{1,2}(x)=x^2.                         \tag{5.1}
\]

Also

\[
 P_{g,2}
 =\sum_{u=1}^g(g-u+1){u!\over(m-g)_u}
 =(1+o(1)){g\over m},                                \tag{5.2}
\]

because the ratio after the first summand is at most
\((u+1)/(m-g-u)=o(1)\) throughout the relevant initial range, while the
remaining tail is smaller geometrically.  Thus the \(1\)-by-\(2\) term in
(4.8) is

\[
 (8+o(1))x^2{g^2\over m}.                             \tag{5.3}
\]

This already diverges for \(g=\Theta(H)\), even at \(x=1\).  The same
phenomenon remains after restricting from the full grid to the exact
radius-profile strip.

### Proposition 5.1 (profile axial lower bound)

Fix any cutoff \(d_0\) with \(d_0/\sqrt m\to\infty\) and \(d_0=o(H)\), and
partition the phases of radii \(d\le d_0\) into balanced return-free chunks
of average central length \(g(1+o(1))\), where \(g=\Theta(H)\).  Let
\(\Psi_2(P)\) be the normalized second overlap moment of a chunk.  Averaged
over the chunks,

\[
 \boxed{
 \Psi_2(P)\ge(c+o(1)){g\over\sqrt m}.}                \tag{5.4}
\]

In particular, for \(g=\Theta(H)\), the right side is
\(\Omega(\sqrt{\log m})\).

#### Proof

A radius-\(d\) phase column contains \(2d\) vertical Boolean cover pairs.
Across the truncated low-radius part of the exact law their total number is

\[
 2\sum_{d\le d_0}d c_d
 =2\sum_{q=1}^{d_0}N_q-2d_0N_{d_0+1}
   =(\sqrt\pi+o(1))W\sqrt m.                          \tag{5.5}
\]

Here the boundary term is \(o(W\sqrt m)\), and the truncated Gaussian sum
already has its full asymptotic because \(d_0/\sqrt m\to\infty\).

The fully labelled orbit has the following exact slot property.  Given an
internal grid cell \(X\), its prescribed vertical successor or predecessor
coordinate is uniform among \(m+O(g)\) eligible Boolean coordinates.
Consequently a fixed template cover pair has relative codegree
\((1+o(1))/m\).  One can also see this by counting the grids with
\(G_{i,j}=X\): the count depends only on the rank \(m-i+j\), so the slots
on one rank diagonal have equal weight, and fixing the next coordinate
costs exactly one factor \(m+O(g)\).

There are \((1+o(1))W/g\) chunks.  Hence (5.5) gives average axial-pair
count \(\Theta(g\sqrt m)\) per chunk.  Multiplication by the joint
relative codegree \((1+o(1))/m\) proves (5.4). \(\square\)

The shifted horizontal cover pairs give another nonnegative contribution.
This lower bound survives the rectangle conflict.  Indeed, condition on a
fixed axial cover pair.  A compressed square containing that pair needs at
least one further prescribed boundary block, whose conditional orbit mass
is

\[
 O\!\left(\sum_{u=1}^g{u!\over(m-g)_u}\right)=O(1/m). \tag{5.6}
\]

A square disjoint from the prescribed pair has total conditional mass at
most \(O(P_{g,2}^2)=O(g^2/m^2)=o(1)\); conditioning on two already exposed
coordinates changes this by only \(1+o(1)\).  Every \(s\)-square contains a
compressed \(2\)-square, so the same estimate applies for every \(s\ge2\).
Thus a \((1-o(1))\)-fraction of the axial link is still rectangle-free.
Therefore no threshold \(s\) can make the uncontracted hierarchy
summable.

The only legitimate way to discard (5.4) would be a theorem saying that a
shared axial chain is one mergeable chronology object and incurs only one
defect.  Such a theorem must include both the vertical phase columns and
the shifted Pascal successor links.  It is not a consequence of marginal
radius balance or of the word `compatible'.

## 6. The cross sector and its sharp threshold

Remove from (4.8) the terms with \(a=1\) or \(b=1\), and denote the result
by \({\mathfrak C}^{\times}_{g,s}(x)\).  This is the part left after a
hypothetical, proved axial-chain contraction.

If a compressed diagram has width \(r\), Dilworth gives

\[
 |L|\le r(a+b-1).                                     \tag{6.1}
\]

The number of pairs of monotone boundaries in an \(a\)-by-\(b\) box is at
most \(16^{a+b}\).  Moreover, from (4.4), uniformly for \(a\le g+1\),

\[
 P_{g,a}
 \le g\exp\!\left(O(g^2/m)\right)
       \left({1+o(1)\over m}\right)^{a-1}.            \tag{6.2}
\]

To prove (6.2), use

\[
 (m-g)_u\ge m^u\exp(-O(g^2/m))                       \tag{6.3}
\]

and sum the positive compositions through

\[
 \sum_{d=1}^g{d!\over m^d}={1+o(1)\over m}.          \tag{6.4}
\]

Stratify (4.8) by the actual width \(r<s\).  Equations (6.1)--(6.4) show
that each added used row or column has ratio at most

\[
 {C x^r\over m}.                                      \tag{6.5}
\]

The harmless factor \(\exp(O(g^2/m))=m^{O(1)}\) occurs once per boundary
profile, not once per added row.  For bounded \(r\) the first terms can be
checked directly; for growing \(r\), the compulsory inequalities
\(a,b\ge r\) make the factor \(m^{-2(r-1)}\) dominate this polynomial.
It follows that, uniformly for \(1\le x\le C_0\log m\),

\[
 \boxed{
 (s-1)\log(Cx)\le(1-\varepsilon)\log m
 \quad\Longrightarrow\quad
 {\mathfrak C}^{\times}_{g,s}(x)=o(1).}               \tag{6.6}
\]

This proves the sufficient half of (0.4).

It is sharp on the logarithmic scale.  Put \(r=s-1\), and take the ordinary
Ferrers rectangle with \(g+1\) consecutive used rows and \(r\) consecutive
used columns.  It survives \(s\)-square pruning, has area \((g+1)r\), and
its joint orbit coefficient is, up to a subexponential factor,

\[
 {x^{(g+1)r}\over(m-g)_g(m-g)_{r-1}}.                \tag{6.7}
\]

Hence

\[
 \log(6.7)
 =g\bigl(r\log x-\log m+o(\log m)\bigr).              \tag{6.8}
\]

If \(r\log x\ge(1+\varepsilon)\log m\), this single non-square Ferrers
coefficient diverges exponentially in \(g\).  This proves the necessary
half and (0.4).

At the nibble endpoint \(z=1/\log m\), the fugacity is \(x=c/z\le
C\log m\).  Thus the explicit safe choice is

\[
 \boxed{
 s=\left\lfloor(1-\varepsilon)
       {\log m\over\log(C\log m)}\right\rfloor.}      \tag{6.9}
\]

## 7. Rectangle conflicts and retained scalar degree

A shared compressed \(s\)-by-\(s\) rectangle has two ordered boundary
profiles of length \(s-1\).  Summing their joint orbit probabilities gives

\[
 \beta_s\le4P_{g,s}^2.                                \tag{7.1}
\]

At (6.9), (4.4) and (6.2) yield

\[
 \begin{aligned}
 \log\beta_s
 &\le2\log g-2(s-1)\log m+O(\log m)\\
 &=-\,(2+o(1)){(\log m)^2\over\log\log m}.           \tag{7.2}
 \end{aligned}
\]

Thus adding these rectangles as conflicts is statically cheap.  In
particular, relative to any fixed already chosen grid, a tag retains
\((1-\beta_s)D_g=(1-o(1))D_g\) candidates.  Also

\[
 \log D_g=\Theta(g\log m)
 \gg { (\log m)^2\over\log\log m},                   \tag{7.3}
\]

so both the orbit and every nonempty conflict neighbourhood remain
enormous in absolute size.

There are two limits to this statement.  First, excluding the union of
many adaptively chosen conflict neighbourhoods requires a hereditary
degree theorem; (7.2) alone is not one.  Second, greedily demanding a
pairwise rectangle-free code only guarantees a colour class of size about
\(1/\beta_s\), which is superpolynomial but need not retain the product
entropy required by a very high-rank nibble.  No stronger retention claim
is used here.

## 8. Final implication for coefficient one

The joint calculation now has a clean separation.

* The exact radius law makes the low-radius reset ledger \(o(W)\).
* The full skew-Ferrers generating function is (3.5).
* Its joint, non-marginal orbit coupling is (4.4)--(4.8).
* After an actual axial-chain quotient, the remaining two-dimensional
  hierarchy has the sharp threshold (6.9), and the corresponding square
  conflicts have negligible static density.
* Without that quotient, the \(1\)-by-\(2\) term (5.4) is nonsummable for
  every \(s\).
* Even with the quotient, return-free chunks cannot carry the direct
  \(q>H/2\) columns, whose target mass is \(\gg W\).

Therefore rectangle pruning does not by itself close the coefficient-one
lane.  The exact remaining assertion is not another common-matching
estimate.  It is a **returnful axial-gluing theorem**: choose the direct
high-radius trajectory columns so that every shared vertical or
shifted-Pascal Ferrers chain is merged at one chronology cost, while the
cross part obeys (6.9).  Until such a theorem is proved, multiplying a
radius marginal by a geodesic-overlap marginal would repeat the correlation
gap this calculation was designed to avoid.
