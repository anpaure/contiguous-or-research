# Catalan and extensive-\(C_8\) component spectra versus the superpolynomial correlation scale

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 H=(1+o(1))\sqrt{m\log m},
 \qquad {H^2\over m}=\log m+o(1),
 \qquad
 R_m=\binom mH,
 \qquad
 \frac{(m+H)\binom{2m}{m-H}}{\binom{2m}{m}}=1+o(1).
\tag{0.1}
\]

The block-factor hole theorem in
MATH_THEOREM_PROMOTION_RING_BLOCK_FACTOR_HOLE_FLOOR_20260726.md
proves that any block-product law with uniform single-root frame marginals
and supported on \(o(W)\)-hole promotion-ring selections must have a
genuinely coupled block of size

\[
 (1-o(1))R_m.
\tag{0.2}
\]

Its logarithmic scale is

\[
 \log R_m
 =\left(\frac12+o(1)\right)
   \sqrt m\,(\log m)^{3/2}.
\tag{0.3}
\]

There is **no component-size obstruction** at this scale in either of the
two canonical Catalan mechanisms.

1.  In the complete MSW/PBBS component hierarchy for
    \(F_m\) versus \((2\ 3)F_m\), the exact component side sizes and
    multiplicities are

    \[
    s_j=C_j+C_{j+1},
    \qquad
    k_{m,j}=C_{m-j-2},
    \qquad 0\le j\le m-2.
    \tag{0.4}
    \]

    In particular, the unique top component has side size

    \[
    s_{m-2}=C_{m-2}+C_{m-1}
      =\left(\frac5{16}+o(1)\right)C_m,
    \tag{0.5}
    \]

    and therefore \(s_{m-2}/R_m\to\infty\) exponentially.  More
    strongly, the components whose side size is at least \(R_m\) contain

    \[
    \boxed{\left(\frac58+o(1)\right)C_m}
    \tag{0.5a}
    \]

    roots on either shore.  Thus the correlation-scale part of the
    hierarchy is macroscopic by root mass, not just nonempty.

2.  For \(u\) pairwise disjoint reciprocal-\(C_8\) slots, the root-toggle
    graph has exact cube components.  A root with exactly \(h\) eligible
    slots lies in one \(Q_h\), of size \(2^h\).  The exact number of such
    components is

    \[
    \boxed{
    K_{m,u}(h)=
      \binom uh
      \sum_{r=0}^{u-h}(-1)^r\binom{u-h}{r}
          2^r C_{m-2h-2r}.}
    \tag{0.6}
    \]

    In particular, there are exactly \(C_{m-2u}\) all-active components,
    each of side size \(2^u\).  The all-on exact factor makes each such
    cube one connected ownership-overlay component.

The first hierarchy scale reaching \(R_m\) is

\[
 j_\star
 :=\min\{j:C_j+C_{j+1}\ge R_m\}
 =\left(\frac1{4\log2}+o(1)\right)
   \sqrt m\,(\log m)^{3/2},
\tag{0.7}
\]

and the first all-active \(C_8\) cube scale reaching \(R_m\) is

\[
 u_\star
 :=\left\lceil\log_2R_m\right\rceil
 =\left(\frac1{2\log2}+o(1)\right)
   \sqrt m\,(\log m)^{3/2}.
\tag{0.8}
\]

Both are \(o(m)\).  Thus both constructions contain literal ownership
components larger than \(R_m\), and the extensive \(C_8\) construction
does so even with a sublinear number of disjoint slots.

This positive size comparison does **not** solve the promotion-ring
correlation gate.  The components above couple anchored Catalan wreath
rows, whereas (0.2) couples promotion roots
\(A\in\binom{[2m]}{m-H}\) whose frames have uniform marginals.  No
incidence-preserving map from either component spectrum to those roots is
known.  Moreover, the exact projection barrier says that one ambient
cyclic row certifies at most \(H+1\) starts of one promotion ring, so a
complete ring needs \(\Omega(m/H)\) ambient rows.  Component cardinality
is therefore sufficient in raw magnitude but not in interface,
uniform-marginal, or all-depth chronology.

## 1. The scale required by the block-factor theorem

For promotion roots \(A\in\binom{[2m]}{m-H}\), a fixed middle target
\(D\in\binom{[2m]}m\) has root star

\[
 \mathcal R(D)=\{A\subset D:|A|=m-H\},
 \qquad |\mathcal R(D)|=R_m=\binom mH.
\tag{1.1}
\]

In a uniform cyclic frame on the top \(U_A=A^c\), the prescribed
\(H\)-set \(D\setminus A\) is a cyclic window with probability

\[
 p_m=\frac{m+H}{\binom{m+H}{H}}.
\tag{1.2}
\]

At the critical covering-side height,

\[
 R_mp_m=1+o(1).
\tag{1.3}
\]

The second condition in (0.1), not merely
\(H=(1+o(1))\sqrt{m\log m}\), is the required critical tuning.  Indeed a
relative \(o(1)\) error in \(H\) can still change \(R_mp_m\) by a
nonconstant factor unless its product with \(\log m\) is controlled.

The block-factor theorem therefore forces block size
\((1-o(1))/p_m=(1-o(1))R_m\).  Stirling's formula, uniformly for
\(H=o(m)\), gives

\[
 \log R_m
 =H\log\frac mH+H
  +O\!\left(\frac{H^2}{m}+\log H\right).
\tag{1.4}
\]

Substitution of (0.1) proves (0.3).

The theorem concerns a probabilistic factorization into independent
blocks.  It does not assert that every deterministic construction must
literally be presented as one component of size \(R_m\).  Nevertheless,
component size is the first necessary comparison for a construction built
by independently selecting component shores.

## 2. Exact MSW/PBBS hierarchy

Let \(F_m\) be the canonical MSW/PBBS wreath factor on \(2m+1\)
coordinates, indexed by \(D_m\), and let \(\tau=(2\ 3)\).  The exact
ownership overlay of \(F_m\) and \(\tau F_m\) has the following
components.

For \(0\le j\le m-2\), define

\[
 \mathcal A_j
 =\{1u0:u\in D_{j+1}\}
   \mathbin{\dot\cup}
   \{10\,1v0:v\in D_j\}.
\tag{2.1}
\]

For every suffix \(Q\in D_{m-j-2}\), the root set

\[
                       \mathcal C_{j,Q}=\{xQ:x\in\mathcal A_j\}
\tag{2.2}
\]

is one connected component on each factor shore, and every component is
obtained uniquely this way.  Hence

\[
 |\mathcal C_{j,Q}|=C_j+C_{j+1}=s_j,
 \qquad
 \#\{Q\}=C_{m-j-2}=k_{m,j}.
\tag{2.3}
\]

Each component has two shores of \(s_j\) wreath rows which partition the
same block of

\[
                         (2m+1)s_j
\tag{2.4}
\]

middle owners.  Choosing either complete shore is one literal binary
exact-factor switch.  Thus \(s_j\), rather than merely an abstract
root-orbit count, is a genuinely coupled ownership-component side size.

The largest type is \(j=m-2\), for which the suffix is empty and the
component is unique.  The exact Catalan ratios are

\[
 \frac{C_{m-1}}{C_m}
 =\frac{m+1}{2(2m-1)},
\tag{2.5}
\]

\[
 \frac{C_{m-2}}{C_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}.
\tag{2.6}
\]

Their sum proves (0.5).  Since

\[
 \log C_m=m\log4+O(\log m)
\tag{2.7}
\]

whereas (0.3) is \(o(m)\), the largest hierarchy component exceeds
\(R_m\) by an exponential factor.

More precisely, for \(j\to\infty\),

\[
 \log(C_j+C_{j+1})
 =j\log4+O(\log j).
\tag{2.8}
\]

Solving \(C_j+C_{j+1}\ge R_m\) using (0.3) proves (0.7).  For every
\(j\ge j_\star\), the hierarchy has exactly \(C_{m-j-2}\) components of
that type.  Consequently the exact number of hierarchy components whose
side size reaches the correlation scale is

\[
 \boxed{
 \sum_{j=j_\star}^{m-2}C_{m-j-2}
 =\sum_{r=0}^{m-j_\star-2}C_r.}
\tag{2.9}
\]

This is far more than existence, although only the component side size,
not its promotion-root interface, is being counted.

There is also an exact root-mass limit.  Let

\[
 \mathsf M_m(R_m)
 :=\sum_{j=j_\star}^{m-2}
       (C_j+C_{j+1})C_{m-j-2}
\tag{2.10}
\]

be the number of roots on one shore which lie in hierarchy components of
side at least \(R_m\).

### Proposition 2.1 (large-component root mass)

\[
 \boxed{\frac{\mathsf M_m(R_m)}{C_m}
        =\frac58+o(1).}
\tag{2.11}
\]

#### Proof

The component classification partitions all \(C_m\) roots, so it is
enough to evaluate the complementary mass with \(j<j_\star\).  Since
\(j_\star\to\infty\) and \(j_\star=o(m)\), the Catalan asymptotic gives,
uniformly for \(0\le j<j_\star\),

\[
 \frac{C_{m-j-2}}{C_m}
 =(1+o(1))4^{-j-2}.
\tag{2.12}
\]

Moreover

\[
 (C_j+C_{j+1})4^{-j-2}=O((j+1)^{-3/2}),
\tag{2.13}
\]

so dominated convergence applies.  Therefore

\[
\begin{aligned}
 \frac1{C_m}\sum_{j<j_\star}
   (C_j+C_{j+1})C_{m-j-2}
 &\longrightarrow
 \sum_{j\ge0}(C_j+C_{j+1})4^{-j-2}\\
 &=\frac1{16}\sum_{j\ge0}C_j4^{-j}
   +\frac14\sum_{k\ge1}C_k4^{-k}\\
 &=\frac18+\frac14=\frac38,
\end{aligned}
\tag{2.14}
\]

because the Catalan generating function has value
\(\sum_{j\ge0}C_j4^{-j}=2\).  The complementary mass is \(5/8+o(1)\),
proving (2.11). \(\square\)

Thus the large MSW hierarchy components are not a negligible exceptional
sector.  This remains a statement about Catalan roots, not promotion-root
stars.

For completeness, (2.9) also has the asymptotic census

\[
 \sum_{r=0}^{m-j_\star-2}C_r
  =\left(\frac43+o(1)\right)C_{m-j_\star-2}
  =\left(\frac{1+o(1)}{12\,4^{j_\star}}\right)C_m.
\tag{2.15}
\]

Since minimality of \(j_\star\) and
\(C_j+C_{j+1}=\Theta(4^j/j^{3/2})\) give
\(4^{j_\star}=\Theta(R_mj_\star^{3/2})\), the number in (2.15) is

\[
             \Theta\!\left(
               \frac{C_m}{R_mj_\star^{3/2}}
             \right).
\tag{2.16}
\]

## 3. Exact extensive-\(C_8\) root-cube census

Fix \(u\) pairwise disjoint four-coordinate slots.  At slot \(i\), the
two eligible fillings are

\[
                         1100\longleftrightarrow1010.
\tag{3.1}
\]

Let \(J(x)\subseteq[u]\) be the eligible-slot set of a Dyck root
\(x\in D_m\).  Toggling a slot preserves its eligibility and does not
change eligibility at a disjoint slot.  Therefore \(J(x)\) is invariant
along the root-toggle graph, and the connected component of \(x\) is

\[
                         Q_{|J(x)|}.
\tag{3.2}
\]

In particular its size is exactly \(2^{|J(x)|}\).

For every specified slot set \(S\subseteq[u]\), simultaneous deletion of
the marked four-bit blocks gives the exact Catalan census

\[
 |\{x:S\subseteq J(x)\}|=2^{|S|}C_{m-2|S|}.
\tag{3.3}
\]

Fix \(T\subseteq[u]\), \(|T|=h\).  Inclusion--exclusion over the slots
outside \(T\) gives

\[
\begin{aligned}
 |\{x:J(x)=T\}|
 &=\sum_{S:T\subseteq S\subseteq[u]}
   (-1)^{|S|-h}2^{|S|}C_{m-2|S|}\\
 &=2^h\sum_{r=0}^{u-h}(-1)^r\binom{u-h}{r}
          2^rC_{m-2h-2r}.
\end{aligned}
\tag{3.4}
\]

Every exact-\(T\) component has \(2^h\) vertices.  Dividing (3.4) by
\(2^h\) and summing over the \(\binom uh\) choices of \(T\) proves the
component census (0.6).  We use the convention \(C_t=0\) for \(t<0\).

For \(h=u\), (0.6) reduces to

\[
                         K_{m,u}(u)=C_{m-2u}.
\tag{3.5}
\]

Hence all-active cubes exist whenever \(2u\le m\).  In the extensive
regime \(u=\lfloor\alpha m\rfloor\), \(0<\alpha<1/2\), their size obeys

\[
 \log 2^u=(\alpha\log2+o(1))m\gg\log R_m.
\tag{3.6}
\]

Even the minimal choice \(u=u_\star\) in (0.8) satisfies
\(u_\star=o(m)\), and therefore supplies \(C_{m-2u_\star}\) components
of size at least \(R_m\).

At this minimal choice the large cubes are nevertheless sparse in root
mass.  Since \(h\le u_\star\), the only components reaching \(R_m\) are
the all-active ones, and their total root mass is

\[
 2^{u_\star}C_{m-2u_\star}.
\tag{3.7}
\]

As \(u_\star=o(m)\),

\[
 \frac{2^{u_\star}C_{m-2u_\star}}{C_m}
 =(1+o(1))\,2^{u_\star}16^{-u_\star}
 =R_m^{-3+o(1)}=o(1).
\tag{3.8}
\]

Thus the minimal sublinear slot count proves existence of
superpolynomial components but not positive root coverage.  In contrast,
for \(u=\lfloor\alpha m\rfloor\), the audited first two moments give
\(|J(x)|=\Theta(m)\) for all but \(O(C_m/m)\) roots, so \(1-o(1)\) of
the roots lie in components much larger than \(R_m\).

## 4. Root cubes are literal ownership components

It remains to distinguish a root-toggle orbit from a completed-factor
ownership component.

Let \(F^0\) be the canonical factor and \(F^1\) the all-on factor which
performs every eligible reciprocal replacement.  Fix one exact-active
root cube \(Q_h\).  In the ownership overlay:

* the fixed ports join the old and new copies of every root \(x\);
* for every cube edge \(\{x,x\oplus e_i\}\), the exchanged internal
  primary token gives a cross-owner edge between the corresponding old
  and new root copies.

After contracting the diagonal port edges, the overlay contains exactly
the \(h\)-cube edge graph.  Conversely, disjoint chronology slabs have no
other cross-owner token.  Therefore the overlay component is connected
and has exactly

\[
                    2^h\text{ rows on each shore}.
\tag{4.1}
\]

Thus (3.2)--(3.5) are also the exact nontrivial ownership-component
spectrum of the canonical/all-on two-factor overlay.

There is a useful refinement.  The edge-coherent exact-factor theorem
permits an arbitrary bit on every elementary rectangle edge.  For any
chosen edge set \(E'\) inside a root cube, the completed-factor ownership
components are exactly the vertex components of \((Q_h,E')\), with the
same side sizes.  Indeed, selected rectangle edges give precisely the
cross-owner links above, and unselected edges give none.  In particular,
choosing a spanning tree of \(Q_h\) gives one literal component of side
size \(2^h\), while choosing no edges leaves \(2^h\) inert singleton
components.

This also explains the distinction between two uses of the extensive
bank:

1. independent elementary rectangle bits have microscopic primitive
   variables but may have a giant root dependency component;
2. comparing the canonical factor with one all-on endpoint turns that
   whole root cube into one binary shore switch.

At the ambient ownership-overlay level, either interpretation disproves
any universal component-size upper bound below \(R_m\).  Neither statement
by itself constructs a promotion-root dependency block.

The exact component assertion uses more than equality of the aggregate
incidence columns.  Its local justification is as follows.  Every
nonfixed resource changed by the construction lies in the interior of a
unique chronology slab and, after all other disjoint slabs are frozen,
in a unique elementary reciprocal rectangle edge.  If that edge bit is
one, the two endpoint rows exchange the resource and give the
corresponding cross-shore cube edge.  If it is zero, its ownership is
diagonal.  Slab-boundary resources, including the ports, are fixed and
also give only diagonal edges.  Hence no cross-owner link can join two
different vertex components of \((Q_h,E')\).  This proves the converse
component containment used in the refinement, rather than inferring it
from exactness alone.

## 5. Why the positive census does not discharge the correlation theorem

The block-factor theorem concerns the \(N_H\) promotion roots

\[
                         A\in\binom{[2m]}{m-H},
\tag{5.1}
\]

and requires every individual root frame to have the uniform cyclic-frame
marginal.  The Catalan components instead couple Dyck-rooted wreath rows.
Equality of their cardinality scales supplies no map

\[
 \{\text{Catalan rows in one component}\}
 \longrightarrow
 \{\text{promotion roots in one block}\}
\tag{5.2}
\]

which preserves top containment, middle-target incidence, or the uniform
frame marginal.

There is an exact targetwise form of this missing interface.  Suppose a
partition \(\mathscr P\) of the promotion roots is obtained from some
component partition, and choices in distinct blocks are independent with
the uniform single-root cyclic-frame marginal.  For
\(D\in\binom{[2m]}m\), put

\[
 r_B(D)=|B\cap\mathcal R(D)|,qquad
 \alpha_D=p_m\max_{B\in\mathscr P}r_B(D).
\tag{5.3}
\]

The proof of the block-factor theorem works target by target and gives

\[
 \boxed{
 \Pr(D\text{ is missed})
 \ge \exp\!\left(-\frac{R_mp_m}{1-\alpha_D}\right)}
 \qquad(\alpha_D<1).
\tag{5.4}
\]

Indeed, the mean number of providers for \(D\) in block \(B\) is
\(p_mr_B(D)\), these means sum to \(R_mp_m\), and the same Markov-product
argument applies.  Consequently an \(o(W)\)-hole block-product law must,
for every fixed \(\varepsilon>0\), have

\[
 \#\left\{D:
   \max_{B\in\mathscr P}r_B(D)
       \le(1-\varepsilon)R_m
 \right\}=o(W).
\tag{5.5}
\]

Thus almost every promotion root-star must be almost wholly contained in
one dependency block.  A block whose *total* cardinality exceeds \(R_m\)
does not automatically have this hereditary alignment.

For calibration, a block \(B\) of \(b\) promotion roots satisfies the
exact double count

\[
 \frac1W\sum_{D\in\binom{[2m]}m}r_B(D)
 =\frac{b}{W}\binom{m+H}{H}
 =\frac{bR_m}{N_H}.
\tag{5.6}
\]

Hence a hypothetical image of the unique top Catalan component, of
density \(5/16+o(1)\) among the \(N_H=(1+o(1))C_m\) promotion roots,
meets a random root-star in only \((5/16+o(1))R_m\) roots on average.
This does not prove that no incidence-preserving assignment exists, but it
shows exactly why the cardinality theorem is only the first gate: a
positive construction must prove the near-monochromatic star condition
(5.5), not merely exhibit one large component.

For the disjoint fixed-slot \(C_8\) bank, the natural transported
interface can be bounded exactly.  Let

\[
 \Gamma=\langle(\beta_i\ \gamma_i):1\le i\le u\rangle
\tag{5.7}
\]

be its group of disjoint coordinate swaps.  If
\(A\in\mathcal R(D)\), let \(t(A,D)\) be the number of generator pairs
which are contained in \(D\) and split by \(A\).  Independence of the
disjoint generators gives

\[
 \boxed{
 |\Gamma A\cap\mathcal R(D)|=2^{t(A,D)}\le2^H.}
\tag{5.8}
\]

Indeed, a split pair contained in \(D\) may be flipped freely while
remaining below \(D\); a split pair meeting \(D\) once admits only the
shore using its point of \(D\); and a nonsplit pair fixes \(A\).  Every
freely flippable pair consumes a distinct element of
\(D\setminus A\), whose size is \(H\), proving the last inequality.

A rooted cyclic packet has \(2m\) marked starts.  Transporting those
starts through a fixed-slot Boolean ownership component therefore gives
at most

\[
                    \boxed{2m\,2^H=o(R_m)}
\tag{5.9}
\]

direct providers in any one promotion root-star.  The last comparison is
exponential on the logarithmic scale, since

\[
 \log R_m=(1/2+o(1))\sqrt m(\log m)^{3/2},
 \qquad \log(2m2^H)=O(\sqrt{m\log m}).
\tag{5.10}
\]

Consequently, under the specific controller hypothesis that promotion
roots are partitioned among independently sampled fixed-slot components,
that each block acts only through these transported traces, and that the
individual frame marginals are uniform, one has
\(\alpha_D=o(1)\) in (5.4) for every \(D\).  The block theorem then gives

\[
                      \boxed{\mathbb E Z\ge(e^{-1}-o(1))W.}
\tag{5.11}
\]

This is a rigorous closure of the direct component-product controller.
It is not a no-go for a global mask (whose one latent choice couples all
components), for rowwise ECAP packet selection, or for a controller in
which several components jointly determine one promotion root; those
dependency blocks must first be merged and may become global.

The same distinction applies to a mesoscopic Catalan component.  Suppose
a proposed closure acts only on a fixed coordinate set \(S\), \(|S|=c\),
and fixes root membership outside \(S\).  For \(A\subset D\), every
orbit point below \(D\) has the same outside part as \(A\), so, writing
\(j=|(D\setminus A)\cap S|\le H\), its star intersection is at most

\[
              \boxed{\binom{|D\cap S|}{j}
                  \le\max_{0\le i\le H}\binom ci.}
\tag{5.12}
\]

If \(c=o(m)\), this is \(o(R_m)\), even when the abstract Catalan state
count already exceeds \(R_m\).  More sharply,

\[
 \frac{\binom{|D\cap S|}{H}}{\binom mH}
 \le\left(\frac{|D\cap S|}{m}\right)^H;
\tag{5.13}
\]

making this ratio \(1-o(1)\) requires

\[
                  m-|D\cap S|=o(m/H).
\tag{5.14}
\]

Thus the first hierarchy scale \(j_\star=o(m)\) passes raw cardinality
but not the natural fixed-support star gate.  The unique top component,
whose support is genuinely root-scale, is not covered by this local
bound; its promotion incidence and completion remain the live
cross-interface problem.

The literal projection barrier makes this mismatch quantitative.  If
\(\pi\) is one ambient cyclic row and \(U\) is a promotion top of size
\(m+H\), then

\[
                     |E_m(\pi|_U)\cap E_m(\pi)|\le H+1.
\tag{5.15}
\]

A promotion ring has \(m+H\) middle starts, so certifying one complete
ring from ambient owner rows needs at least

\[
                    \left\lceil\frac{m+H}{H+1}\right\rceil
                    =\Omega(m/H)
\tag{5.16}
\]

ambient rows.  Thus an inheritance using disjoint ambient certificates
for different promotion rings would require \(\Omega(R_mm/H)\) ambient
rows for an \(R_m\)-root correlation block.  This count is not asserted
without disjointness: one ambient row might serve starts belonging to
several tops, and controlling such reuse is part of the missing braid.

This larger raw cardinality is still available:

* the top MSW component is exponential in \(m\);
* a \(C_8\) cube reaches it after

  \[
  u=\left\lceil\log_2(R_mm/H)\right\rceil
    =u_\star+O(\log m)=o(m)
  \tag{5.17}
  \]

  slots.

Hence (5.4) is an interface obstruction, not a component-size
obstruction.  What remains unproved is a literal multirow braid assigning
those ambient rows to promotion roots while preserving:

1. every top and owner ledger;
2. the uniform single-root frame marginal after symmetrization;
3. the nested traces through all protected depths; and
4. global exact-factor completion.

## 6. Exact boundary

The requested component-size question is settled positively:

\[
\boxed{\text{both the canonical MSW hierarchy and the extensive }
C_8\text{ bank contain literal components of size }\ge\binom mH.}
\tag{6.1}
\]

The exact spectra are (0.4) and (0.6).  Therefore the new
superpolynomial correlation theorem cannot be used to rule out these
Catalan mechanisms by component cardinality.

It still rules out every implementation which factorizes into genuinely
independent promotion-root blocks smaller than \((1-o(1))R_m\).  To use
the large Catalan components positively, one must prove a new
cross-interface theorem converting their ambient row coupling into
promotion-root frame coupling.  No such conversion follows from the
component census alone.
