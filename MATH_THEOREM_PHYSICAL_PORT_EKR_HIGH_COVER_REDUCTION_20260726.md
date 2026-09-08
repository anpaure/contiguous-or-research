# Physical strip ports: pair sparsification and the high-cover EKR gate

> **Kupavskii--Zakharov audit (2026-07-26).** The all-order physical
> codegree profile can be proved, including an \(O(1/m)\) factor per
> member of a nested comparable flag. However, exact target regularity
> forces a selected \(s\times s\) crossing-flag grid of conditional
> density \(\Omega(1/[s(m)_s^2])\). For \(s=m^{1/5}\), this makes the
> relative spread parameter \(r=1+o(1)\), already on
> \(m^{2/5+o(1)}\) targets. Thus the \((r,q)\)-spread hypothesis of the
> published spread-approximation theorem fails far below the high-cover
> scale. See
> MATH_AUDIT_KZ_SPREAD_APPROXIMATION_PHYSICAL_PORT_HIGH_COVER_20260726.md.
> The high-cover theorem below remains open; it now specifically requires
> a flag-compressed replacement for ordinary cardinality spreadness.

## 0. Purpose and scope

Work on the \(2m\)-element product-SCD ground set, and let

\[
 H=\sqrt m\,m^{o(1)},\qquad h=m^{2/3+o(1)},
 \qquad H=o(h),
\]

and use the physical \(C_{2h}\)-strip catalogue and the exact
target-regular independent port construction of
`MATH_THEOREM_LAMINAR_PORT_STAR_SPARSIFICATION_AND_LAYERED_HALL_GATE_20260726.md`.
Write \(D_1\) for the common degree of every signed nonmiddle target and
\(e_C^\#\) for the selected port edge of a strip \(C\).  Middle targets
are included without thinning and have degree \(D_0\le D_1\).

The abstract off-edge-star condition is not by itself an EKR theorem:
projective planes are counterexamples to such an abstract implication.
This note records what the **physical cyclic pair kernel** adds.  It gives
three rigorous conclusions.

1. The ports may be chosen so that every distinct target pair has selected
   codegree at most \((4+o(1))D_1/m\), simultaneously with exact target
   degrees, the width bound, and off-edge-star sparsity.
2. Every non-star intersecting strip family whose target-cover number is
   \(o(m^{1/3})\) has size \(o(D_1/\sqrt m)\).  Consequently any EKR
   obstruction at the precision required by the annulus compiler must
   have target-cover number at least \(m^{1/3-o(1)}\).
3. The scale \(D_1/m\) is real: there are physical non-star intersecting
   families of size \((2+o(1))D_1/m\).  Thus a correct theorem must be a
   Hilton--Milner stability theorem, not the assertion that every
   intersecting family is literally a star.

This does **not** finish the fractional edge-colouring gate.  It rules out
all bounded-order and all low-cover projective-plane analogues and isolates
one precise remaining possibility: a genuinely high-cover physical
linear-space obstruction.

The exponent \(2/3\) is only the convenient parameter choice made in the
laminar-port note.  The same proofs work whenever

\[
 H=o(h),\qquad h=o(m),\qquad h\sqrt m\gg m\log m,                  \tag{0.1}
\]

the last condition being exactly what is needed for the simultaneous
width union bound.  In that flexible range

\[
 \widehat\rho_m=O(m^{-1}+h m^{-3/2})+o(m^{-A})
\]

for every fixed \(A\).  Thus \(h\) can be optimized later; \(m^{2/3}\)
is not intrinsic.

## 1. A simultaneous selected-pair bound

For signed targets \(S,T\), let \(d(S,T)\) be their raw physical-strip
codegree.  If

\[
 |S|=m+a,\quad |T|=m+b,\quad
 i=|S\setminus T|,\quad j=|T\setminus S|,
\]

then the cyclic pair kernel gives

\[
 {d(S,T)\over D_a}
 ={n_{a,b}(i,j)\over
   \binom{m+a}{i}\binom{m-a}{j}}.                 \tag{1.1}
\]

For a nonmiddle rank put

\[
 \theta_a={D_1\over D_a}\le1,
\]

and put \(\theta_0=1\) for the unthinned middle rank.

### Theorem 1.1 (physical selected-pair sparsification)

The exact target-regular ports can be chosen simultaneously with all the
conclusions of Theorem 3.3 of the laminar-port note and with

\[
 \boxed{
 \Delta_2(\mathcal H^\#)
 :=\max_{S\ne T}\#\{C:S,T\in e_C^\#\}
 \le { (4+o(1))D_1\over m}.}                       \tag{1.2}
\]

The same outcome can be required to satisfy the sharper pairwise form

\[
 d^\#(S,T)\le2\mathbb E d^\#(S,T)+C_1m
 \qquad(S\ne T),                                   \tag{1.2a}
\]

where \(C_1\) is an absolute constant chosen sufficiently large.

#### Proof

Choose, independently at every nonmiddle target of signed rank \(a\), a
uniform \(D_1\)-subset of its \(D_a\) incident raw strips.  This is the
same experiment as in Theorem 3.3, so every nonmiddle target degree is
exactly \(D_1\).

Fix distinct targets \(S,T\).  If both are nonmiddle, the expected
selected codegree is

\[
 d(S,T)\theta_a\theta_b.
\]

If one is middle, omit the corresponding factor \(\theta_0=1\); if both
are middle, the codegree is deterministic.  Orient the pair from a
nonmiddle target when possible.  Dividing by \(D_1=D_a\theta_a\), (1.1)
and the three cases of the cyclic pair lemma give the following.

* For a comparable pair at rank gap \(r\ge1\),

  \[
  {\mathbb E d^\#(S,T)\over D_1}
  \le {r+1\over\binom{m-H}{r}}
  \le {2+o(1)\over m}.                              \tag{1.3}
  \]

* For a noncomparable overlapping pair,

  \[
  {\mathbb E d^\#(S,T)\over D_1}
  \le {2\over(m-H)^2}.                              \tag{1.4}
  \]

* For an active-disjoint pair the bound in (1.8) of the laminar-port
  note is superpolynomially smaller than \(m^{-2}\) in the present
  parameter range.

For two middle targets only the last two cases occur, and \(D_0\le D_1\),
so the same upper bound is valid.  Thus every pair has expectation at
most \((2+o(1))D_1/m\).

For two independently selected target stars the common selected strips
form a two-stage hypergeometric variable.  Hypergeometric negative
association and the usual Chernoff bound therefore give

\[
 \Pr\left(d^\#(S,T)>4D_1/m\right)
 \le \exp[-\Omega(D_1/m)] .                         \tag{1.5}
\]

The same estimate, with an even smaller right side, follows from an
additive Chernoff bound when the mean is \(o(D_1/m)\).  Now

\[
 D_1={(m+1)!(m-1)!\over2(m-h)!^2}
\]

is exponential in \(h\log m\), whereas the logarithm of the number of
ordered target pairs is \(O(m)\).  Hence (1.5) survives a union bound over
all pairs.  More precisely, Bernstein's hypergeometric bound with
additive deviation \(C_1m\) gives (1.2a): if the mean is at least
\(C_1m\), use a factor-two multiplicative deviation; if it is smaller,
use the additive deviation.  Taking \(C_1\) larger than the exponential
growth constant for the number of target pairs makes the union bound
summable.  The width and off-edge-star failures in Theorem 3.3 also have
summable probability, so one outcome avoids all failures simultaneously.
This proves (1.2).  \(\square\)

## 2. Intersecting families and target covers

Call \(\mathcal F\) an *intersecting strip family* if

\[
 e_C^\#\cap e_{C'}^\#\ne\varnothing
 \qquad(C,C'\in\mathcal F).
\]

Its target-cover number is

\[
 \tau(\mathcal F)
 =\min\{|X|:X\text{ is a target set and }
             X\cap e_C^\#\ne\varnothing\ \forall C\in\mathcal F\}.
                                                               \tag{2.1}
\]

Thus \(\tau=1\) means precisely that \(\mathcal F\) is contained in a
target star.

Let

\[
 \widehat\rho_m
 =O\left({1\over m}+{h\over m^{3/2}}\right)
  +O(h^2\sqrt m)
    \left({h+H\over m-H}\right)^{2(h-H)}
 =m^{-5/6+o(1)} .                                  \tag{2.2}
\]

The port outcome of Theorem 1.1 satisfies, whenever \(S\notin e_E^\#\),

\[
 \#\{C:S\in e_C^\#,\ e_C^\#\cap e_E^\#\ne\varnothing\}
 \le2\widehat\rho_mD_1.                           \tag{2.3}
\]

### Theorem 2.1 (cover-number EKR reduction)

Every intersecting strip family with \(\tau=\tau(\mathcal F)\ge2\)
satisfies

\[
 \boxed{|\mathcal F|\le2\tau\widehat\rho_mD_1.}   \tag{2.4}
\]

In particular, if

\[
 \tau(\mathcal F)=o\left({1\over\widehat\rho_m\sqrt m}\right)
 =o(m^{1/3-o(1)}),                                  \tag{2.5}
\]

then

\[
 |\mathcal F|=o(D_1/\sqrt m).                       \tag{2.6}
\]

#### Proof

Take a minimum target cover

\[
 X=\{x_1,\ldots,x_\tau\}.
\]

Its minimality implies that for every \(i\) there is an edge
\(E_i\in\mathcal F\) satisfying

\[
 e_{E_i}^\#\cap X=\{x_i\};                         \tag{2.7}
\]

otherwise \(X\setminus\{x_i\}\) would still cover \(\mathcal F\).
Partition \(\mathcal F\) into classes \(\mathcal F_i\) by assigning each
edge to one cover target it contains.  For each \(i\), choose
\(j\ne i\).  Every edge in \(\mathcal F_i\) contains \(x_i\) and, since
\(\mathcal F\) is intersecting, meets \(E_j\).  But (2.7) says that
\(x_i\notin e_{E_j}^\#\).  Therefore (2.3) gives

\[
 |\mathcal F_i|\le2\widehat\rho_mD_1.
\]

Summing over \(i\) proves (2.4), and (2.5) gives (2.6). \(\square\)

### Corollary 2.2 (where a physical projective plane would have to live)

Any non-star intersecting family of size not
\(o(D_1/\sqrt m)\) has target-cover number

\[
 \tau(\mathcal F)\ge m^{1/3-o(1)}.                 \tag{2.8}
\]

Consequently no bounded-order projective plane, no bounded-cover odd-set
gadget, and no union of a bounded number of target stars can obstruct the
fractional-colouring precision needed by the annulus compiler.

The statement is statewise and uses the physical cyclic kernel; it is not
an inference from abstract maximum degree or from cardinality.

### Corollary 2.3 (optimized strip scale)

For the Gaussian annulus take, for example,

\[
 H=\sqrt{m\log m}\,m^{o(1)},\qquad
 h=\sqrt m\,\log m\,L_m,qquad L_m\to\infty,
\]

where \(L_m=m^{o(1)}\).  Then (0.1) holds and

\[
 \widehat\rho_m=O\left({\log m\,L_m\over m}\right).
\]

Consequently every obstruction of size not \(o(D_1/\sqrt m)\) must have

\[
 \boxed{
 \tau(\mathcal F)
 \ge {\sqrt m\over (\log m)L_m}\,m^{-o(1)}.}        \tag{2.9}
\]

Optimizing the physical strip width therefore pushes the possible
projective-plane order from \(m^{1/3-o(1)}\) to essentially \(\sqrt m\),
up to a polylogarithmic factor.

## 3. Multistar linear spaces

The preceding reduction can also be stated directly for the standard
way a projective-plane obstruction is embedded.

Let \(\mathcal B\) be a pairwise-intersecting family of \(t\)-subsets of
the target vertex set, with empty total intersection.  Put

\[
 \mathcal F(\mathcal B)
 =\bigcup_{B\in\mathcal B}\{C:B\subseteq e_C^\#\}.  \tag{3.1}
\]

This is an intersecting strip family: if \(B\cap B'\ne\varnothing\),
then every strip containing \(B\) meets every strip containing \(B'\).

### Proposition 3.1 (bounded-block projective planes collapse to pairs)

For the port system of Theorem 1.1,

\[
 \boxed{|\mathcal F(\mathcal B)|
 \le t^2\Delta_2(\mathcal H^\#)
 \le{(4+o(1))t^2D_1\over m}.}                      \tag{3.2}
\]

#### Proof

Choose \(B_0\in\mathcal B\).  Since the total intersection is empty,
for each \(x\in B_0\) choose \(B_x\in\mathcal B\) with \(x\notin B_x\).
For any \(B\in\mathcal B\), choose \(x\in B\cap B_0\), and then choose
\(y\in B\cap B_x\).  Necessarily \(y\ne x\).  Thus every strip
containing \(B\) contains one of the at most \(t^2\) target pairs
\(\{x,y\}\), where \(x\in B_0\) and \(y\in B_x\).  Hence (3.1) is
contained in the union of at most \(t^2\) pair-stars.  Apply (1.2).
\(\square\)

For example, the full multistar family arising from the lines of a
projective plane of order \(r\) has \(t=r+1\).  Proposition 3.1 rules it
out at the required scale whenever \(t=o(m^{1/4})\), while Theorem 2.1,
using a blocking set of size \(O(t)\), rules it out whenever
\(t=o(m^{1/3-o(1)})\).  Thus an actual projective-plane-like obstruction
would have to be a growing-order object of order at least
\(m^{1/3-o(1)}\), not a hidden triangle or Fano-plane gadget.

The apparent large-order escape can also be closed for a genuine
projective-plane multistar construction, using the geometry inside one
physical strip.

### Lemma 3.2 (metric packing inside a strip)

Let \(\mathcal A\) be \(t\) distinct raw band targets of one physical
strip.  Then two members \(S,T\in\mathcal A\) satisfy

\[
 |S\setminus T|+|T\setminus S|\ge c\sqrt t          \tag{3.3}
\]

for an absolute \(c>0\).

#### Proof

After deleting the common strip core, a target is specified by its signed
rank \(a\in[-H,H]\) and the starting point of an interval of length
\(h+a\) in the \(2h\)-cycle.  Fix one such interval.  If another interval
has set-difference sum at most \(s<h-H\), then the rank difference is at
most \(s\), and, after taking the unique overlapping lift of the two
cyclic intervals, the displacement of their starting points is also at
most \(s\).  There are therefore at most

\[
 (2s+1)^2
\]

targets in this metric ball.  Taking \(s=c\sqrt t\) with a sufficiently
small absolute \(c\) proves (3.3).  Notice that
\(t\le2h(2H+1)\); since \(H=o(h)\), this choice has
\(s=O(\sqrt{hH})=o(h-H)\), so the overlapping-lift argument always
applies. \(\square\)

### Lemma 3.3 (large block multicodegree)

If \(B\) is a \(t\)-set of distinct targets contained in some physical
port edge and \(s=\lfloor c\sqrt t\rfloor\ge1\), then

\[
 \#\{C:B\subseteq e_C^\#\}
 \le
 4hD_1\left({C\sqrt t\over m-H}\right)^{c\sqrt t}
 +C_1m.                                             \tag{3.4}
\]

#### Proof

Choose \(S,T\in B\) from Lemma 3.2 and put
\(i=|S\setminus T|\), \(j=|T\setminus S|\), \(r=i+j\).
The cyclic pair numerator is at most \(2h\) in all three pair-orbit
cases.  After the independent target thinning, its expected selected
pair degree is at most \(D_1\) times the resulting normalized kernel.
Moreover,

\[
 \binom{m-H}{i}\binom{m-H}{j}
 \ge\left({m-H\over r}\right)^r.                  \tag{3.5}
\]

Equations (1.1), (3.3), and (3.5) bound that expectation by

\[
 2hD_1\left({r\over m-H}\right)^r.
\]

The function \((r/(m-H))^r\) is decreasing throughout
\(r=o(m)\).  Hence \(r\ge c\sqrt t\) gives the first term in (3.4).
Finally apply the simultaneous deviation bound (1.2a).  Since every
strip containing \(B\) contains the pair \(\{S,T\}\), this proves
(3.4). \(\square\)

### Corollary 3.4 (no physical projective-plane multistar obstruction)

Let \(\mathcal B\) be the lines of a projective plane of order \(r\),
viewed as \((r+1)\)-sets of physical target vertices, and suppose each
line is contained in at least one physical port edge.  Then

\[
 \left|
 \bigcup_{B\in\mathcal B}\{C:B\subseteq e_C^\#\}
 \right|=o(D_1/\sqrt m).                            \tag{3.6}
\]

#### Proof

Put \(t=r+1\).  A line of the plane is a target cover of the multistar
family, since it meets every line.  If

\[
 t=o\bigl((\widehat\rho_m\sqrt m)^{-1}\bigr),
\]

Theorem 2.1 gives (3.6).  Otherwise \(t\) is at least
\(m^{1/3-o(1)}\) under the default parameters, and at least
\(\sqrt m/\operatorname{polylog}m\) at the optimized scale.  The plane
has \(t^2-t+1\) lines, while Lemma 3.3 bounds every line-multistar.
Consequently the left side of (3.6) is at most

\[
 (t^2-t+1)\,4hD_1
 \left({C\sqrt t\over m-H}\right)^{c\sqrt t}
 +O(t^2m)
 =o(D_1/\sqrt m).                                  \tag{3.7}
\]

The last estimate is superpolynomial: its negative logarithm is
\(\Omega(\sqrt t\log(m/\sqrt t))\), whereas the prefactor is polynomial
in \(m\). \(\square\)

Thus there is no actual physical projective-plane obstruction of the
standard “one multistar per line” form, at **any** order.  What remains
open is more distributed: an intersecting strip family of high cover
number need not be the union of full multistars indexed by a linear
space.

## 4. The exact adaptive-kernel inequality

There is a general cover-number expansion which makes precise why the
pair kernel settles projective-plane blow-ups but not yet every
high-cover clique.

For a target set \(A\), write

\[
 d^\#(A)=\#\{C:A\subseteq e_C^\#\}.
\]

### Proposition 4.1 (adaptive witness tree)

Let \(\mathcal F\) be intersecting, let
\(\tau(\mathcal F)>t\), and let \(K=\max_C|e_C^\#|\).  There is a rooted
tree of depth \(t\) whose nodes at depth \(r\) are \(r\)-sets of targets,
whose branching factor is at most \(K\), and whose leaves
\(\mathcal L_t\) satisfy

\[
 \boxed{
 |\mathcal F|\le\sum_{A\in\mathcal L_t}d^\#(A).}     \tag{4.1}
\]

In particular,

\[
 |\mathcal F|\le K^t\Delta_t^\#,\qquad
 \Delta_t^\#=\max_{|A|=t}d^\#(A).                  \tag{4.2}
\]

#### Proof

Choose \(E_\varnothing\in\mathcal F\), and partition \(\mathcal F\) by
one selected target in its intersection with \(E_\varnothing\).  At a
node \(A\) of depth \(r<t\), the inequality
\(r<\tau(\mathcal F)\) supplies an edge
\(E_A\in\mathcal F\) disjoint from \(A\).  Every member of the branch is
in \(\mathcal F\), hence intersects \(E_A\); partition that branch by one
target in this intersection and append it to \(A\).  Because
\(E_A\cap A=\varnothing\), the target set grows at every step.  At depth
\(t\), every remaining branch lies in the corresponding \(t\)-star.
Summing the leaf bounds proves (4.1), and at most \(K^t\) leaves gives
(4.2). \(\square\)

Combining (4.2) with Lemma 3.3 gives the valid but non-closing estimate

\[
 |\mathcal F|
 \le K^t\left[
 4hD_1\left({C\sqrt t\over m-H}\right)^{c\sqrt t}
 +C_1m\right].                                      \tag{4.3}
\]

The factor \(K^t\) overwhelms the \(\exp[-\Omega(\sqrt t\log m)]\)
metric decay.  This is not evidence that a high-cover obstruction
exists; it identifies the exact missing physical input.  One needs a
**weighted adaptive-kernel theorem**

\[
 \sum_{A\in\mathcal L_t}d^\#(A)=o(D_1/\sqrt m)      \tag{4.4}
\]

for the witness trees generated by cyclic strip edges, rather than the
false replacement of the sum by \(K^t\Delta_t^\#\).  A projective plane
has a highly redundant witness tree, which is why Corollary 3.4 bypasses
the \(K^t\) loss.  An arbitrary high-cover family is not yet known to
have comparable redundancy.

## 5. The \(D_1/m\) Hilton--Milner scale is attained

The high-cover gate cannot be replaced by the claim that every
non-star intersecting family is empty or polynomially small.

### Proposition 5.1 (a physical non-star triangle)

For \(h\ge3\) and all sufficiently large \(m\), the unthinned
middle/first-shadow part of the physical port hypergraph contains a
non-star intersecting family of size

\[
 {2D_1\over m+1}+O(1).                             \tag{5.1}
\]

#### Construction and proof

Choose nested targets

\[
 S\subset T\subset U,\qquad
 |S|=m-1,\quad |T|=m,\quad |U|=m+1.                \tag{5.2}
\]

There are physical strips \(E,C_0\) such that

\[
 T,U\in e_E^\#,\quad S\notin e_E^\#,
 \qquad
 S,U\in e_{C_0}^\#,\quad T\notin e_{C_0}^\#.      \tag{5.3}
\]

To see this explicitly, fix a common \((m-h)\)-core inside \(S\).
For \(E\), make the unique element of \(T\setminus S\) an interior
point of the active \(h\)-interval for \(T\), and extend that interval at
an endpoint to obtain \(U\).  Deleting the interior point does not leave
an \((h-1)\)-interval, so \(E\) avoids \(S\).  For \(C_0\), order the two
points of \(U\setminus S\) consecutively on the same side of the active
\((h-1)\)-interval for \(S\), putting the point of \(T\setminus S\)
farther away.  Then \(S,U\) are intervals but \(T\) is not.  Complete
both active orders arbitrarily with unused points.  This proves (5.3).

Let

\[
 \mathcal A=\{E,C_0\}
 \cup\{C:S,T\in e_C^\#\}.                          \tag{5.4}
\]

Any two members of the last class share \(S,T\); each of them meets
\(E\) at \(T\) and \(C_0\) at \(S\); and \(E,C_0\) meet at \(U\).
Thus \(\mathcal A\) is intersecting.  It has no common target: \(E\)
avoids \(S\) and \(C_0\) avoids \(T\).  More explicitly, the intersection
of the raw target sets of **all** strips through the flag \(S\subset T\)
is exactly \(\{S,T\}\).  Indeed the stabilizer of the flag has cells
\(S\), \(T\setminus S\), and \([2m]\setminus T\); varying the core inside
\(S\) and permuting the last cell moves every band target other than
\(S,T\).  (The only other unions of stabilizer cells in the band are
avoided by choosing the unused part of the active set.)  Hence no target
can lie in every member of (5.4).  In particular one may also see this
directly by choosing a strip through \(S,T\) avoiding \(U\).

Finally, the comparable gap-one case of (1.1) gives

\[
 \#\{C:S,T\in e_C^\#\}
 ={2D_1\over m+1},                                 \tag{5.5}
\]

because first-shadow and middle incidences are unthinned.  Equations
(5.4)--(5.5) prove (5.1). \(\square\)

This construction is the physical Hilton--Milner lower bound.  Its size
is \(o(D_1/\sqrt m)\), so it is harmless for the annulus compiler, but it
shows that the natural non-star scale is at least \(D_1/m\).

## 6. Exact remaining theorem

The present EKR lane is now reduced to the following genuinely physical
statement.

> **High-cover physical EKR theorem (open).** Every intersecting family
> of selected physical strip edges with target-cover number
> at least \(1/(\widehat\rho_m\sqrt m)\) has size
> \(o(D_1/\sqrt m)\).  At the optimized strip scale this begins at
> \(\sqrt m/\operatorname{polylog}m\).

Equivalently, one must exclude a growing-order linear-space design whose
"lines" are actual cyclic strip-port edges and whose target blocking
number is at least \(1/(\widehat\rho_m\sqrt m)\).  The exact pair kernel proves that no
bounded projective plane and no bounded multistar construction can do
this.  It does not yet exclude a highly distributed growing design.

Even that theorem would settle only the clique/odd-set part of the
fractional edge-colouring gate.  A complete proof of

\[
 \chi_f'(\mathcal H^\#)
 \le D_1+o(D_1/\sqrt m)
\]

must additionally control non-clique fractional matching-polytope
obstructions.  The gain here is a rigorous physical localization: any
counterexample can no longer be a small odd-cycle, Fano plane, or local
laminar flag gadget.  It must be a macroscopic high-cover construction.
