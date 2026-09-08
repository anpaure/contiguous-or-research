# MSW coordinate components as bounded rooted target-splitting packets

Date: 2026-07-26

This note records the exact answer for the boundary coordinate swap and the
uniform small-component answer for every even-pair swap.  The point is not a
full Catalan conveyor.  A component with at most \(p\) rows on either shore
is already a legal rooted packet of the size required by the plateau repair,
and it splits a common Catalan target fibre exactly.

Throughout,

\[
 J=[2r],\qquad N=J\sqcup\{\infty\},\qquad
 B=\operatorname {Cat}_r,
\]

and \(F_r\) is the canonical anchored MSW local factor, with its rows rooted
at \(\mathcal D_r\).  For \(1\le i<r\), put

\[
                         s_i=(2i\ \ 2i+1).
\]

Every \(s_i\) preserves \(\mathcal D_r\), so both \(F_r\) and \(s_iF_r\)
belong to the same anchored fibre.  Consequently every complete ownership
component switch between them is a literal integral, port-valid local
replacement.

## 1. Exact spectrum for the boundary swap

Take \(s_1=(2,3)\).  For \(0\le j\le r-2\), define

\[
 \mathcal A_j=
 \{1u0:u\in\mathcal D_{j+1}\}
 \mathbin{\dot\cup}
 \{10\,1v0:v\in\mathcal D_j\}.
 \tag{1.1}
\]

For \(R\in\mathcal D_{r-j-2}\), put

\[
                    \mathcal K_{j,R}=\{AR:A\in\mathcal A_j\}.
 \tag{1.2}
\]

### Theorem 1.1 (exact rooted component law)

The sets \(\mathcal K_{j,R}\) are exactly the root blocks of the connected
ownership components of \(F_r\) versus \(s_1F_r\).  In particular,

\[
 k_j:=|\mathcal K_{j,R}|
      =\operatorname {Cat}_j+\operatorname {Cat}_{j+1},
 \tag{1.3}
\]

and the number of components of shore size \(k_j\) is

\[
                         \operatorname {Cat}_{r-j-2}.
 \tag{1.4}
\]

Every component may be switched independently, and every resulting local
factor retains the prescribed root and complementary terminal port for each
member of \(\mathcal D_r\).

#### Proof

The component classification, including closure and connectivity, is the
exact Catalan hierarchy proved in
`MSW_COMPONENT_HIERARCHY_REDUCTION.md`.  The coordinate automorphism
\(s_1\in\operatorname {Aut}(\mathcal D_r)\) and the equality of the root
blocks on the two component shores put this hierarchy in the anchored fibre
by the ownership-component theorem in
`MATH_ATTACK_L_DYCK_TRANSVERSAL_FIBRE_RECONFIGURATION_20260726.md`.
Equations (1.3)--(1.4) follow directly from (1.1)--(1.2). \(\square\)

The smallest layer is

\[
 \mathcal K_{0,R}=\{1100R,1010R\},
 \qquad R\in\mathcal D_{r-2},                         \tag{1.5}
\]

so there are \(\operatorname {Cat}_{r-2}\) disjoint two-row packets.
The largest component has shore size

\[
                 \operatorname {Cat}_{r-2}
                    +\operatorname {Cat}_{r-1}
                 =\left(\frac5{16}+o(1)\right)B.     \tag{1.6}
\]

Thus the comparison face is genuinely multiscale, but it contains a
positive-density microscopic sector.

## 2. The exact \(p\)-bounded truncation

For \(p\ge2\), let

\[
 J(p)=\max\{j\ge0:
       \operatorname {Cat}_j+\operatorname {Cat}_{j+1}\le p\}.
 \tag{2.1}
\]

If packet size means total old-plus-new support, replace \(p\) in (2.1)
by \(\lfloor p/2\rfloor\); all formulas below count rows on one shore.

### Theorem 2.1 (linear family of bounded rooted packets)

The components with \(j\le J(p)\) form an independent cube of dimension

\[
 d_{r,p}=
 \sum_{j=0}^{\min\{J(p),r-2\}}
       \operatorname {Cat}_{r-j-2},                  \tag{2.2}
\]

and their root blocks contain in total

\[
 v_{r,p}=
 \sum_{j=0}^{\min\{J(p),r-2\}}
 (\operatorname {Cat}_j+\operatorname {Cat}_{j+1})
       \operatorname {Cat}_{r-j-2}                  \tag{2.3}
\]

rows.  Every cube coordinate changes at most \(p\) rows on either shore.

If \(J(p)=o(r)\), then uniformly in this range

\[
 \frac{d_{r,p}}B
  =\sum_{j\le J(p)}4^{-j-2}+o(1),                   \tag{2.4}
\]

\[
 \frac{v_{r,p}}B
  =\sum_{j\le J(p)}
   \frac{\operatorname {Cat}_j+\operatorname {Cat}_{j+1}}
        {4^{j+2}}+o(1).                              \tag{2.5}
\]

Consequently, if \(p=p(r)\to\infty\) with
\(J(p)=o(r)\), then

\[
              d_{r,p}=\left(\frac1{12}+o(1)\right)B,
 \qquad
              v_{r,p}=\left(\frac38+o(1)\right)B.   \tag{2.6}
\]

In particular, polynomial \(p\) is more than sufficient:

\[
                         J(p)=\log_4p+O(\log\log p). \tag{2.7}
\]

#### Proof

Equations (2.2)--(2.3) are Theorem 1.1 with the large components omitted.
For \(j=o(r)\),

\[
  \frac{\operatorname {Cat}_{r-j-2}}
       {\operatorname {Cat}_r}=4^{-j-2}(1+o(1)),
\]

uniformly on every logarithmic range, which proves (2.4)--(2.5).  Finally,

\[
 \sum_{j\ge0}4^{-j-2}=\frac1{12},                    \tag{2.8}
\]

while, using \(C(1/4)=2\) for the Catalan generating function,

\[
 \sum_{j\ge0}
   \frac{\operatorname {Cat}_j+\operatorname {Cat}_{j+1}}
        {4^{j+2}}
 =\frac18+\frac14=\frac38.                           \tag{2.9}
\]

The Catalan asymptotic
\(\operatorname {Cat}_j=\Theta(4^j j^{-3/2})\) gives (2.7). \(\square\)

Already \(p=2\) gives

\[
 d_{r,2}=\operatorname {Cat}_{r-2}
       =\left(\frac1{16}+o(1)\right)B,
 \qquad
 v_{r,2}=2\operatorname {Cat}_{r-2}
       =\left(\frac18+o(1)\right)B.                  \tag{2.10}
\]

Thus no growing packet allowance is needed merely to obtain a
positive-density collection of port-valid target splitters.

## 3. A component splits any equivariant common target exactly

The following observation is the direct interface with the Catalan plateau.
Let \(\Theta(C;P)\) be any rooted target extracted from the row \(C\) at
port \(P\), and suppose it is coordinate-equivariant:

\[
        \Theta(gC;gP)=g\Theta(C;P).                   \tag{3.1}
\]

This includes every intersection or union target of a specified rooted
window, with a fixed exterior set adjoined.

### Theorem 3.1 (exact componentwise fibre splitting)

Suppose the canonical local factor has one common target

\[
                         \Theta(C_P;P)=S
             \qquad(P\in\mathcal D_r).               \tag{3.2}
\]

Let \(K\) be an ownership component of \(F_r\) versus \(s_iF_r\), and
let \(\mathcal R_K\subseteq\mathcal D_r\) be its common root block on the
two shores.  Switch precisely this component.  Then the resulting exact
anchored factor has target profile

\[
 \Theta'(P)=
 \begin{cases}
     s_iS,&P\in\mathcal R_K,\\
     S,&P\notin\mathcal R_K.
 \end{cases}                                          \tag{3.3}
\]

Hence, whenever \(s_iS\ne S\), a component of shore size \(k\) gives the
literal multiplicity split

\[
                         B\longrightarrow(B-k)+k.     \tag{3.4}
\]

For an arbitrary set \(\mathcal I\) of components, \(k\) in (3.4) is
replaced by \(\sum_{K\in\mathcal I}|\mathcal R_K|\).

#### Proof

The row on the \(s_iF_r\)-shore rooted at \(P\) is

\[
                         s_iC_{s_i^{-1}P}.
\]

By (3.1)--(3.2), its target is

\[
 \Theta(s_iC_{s_i^{-1}P};P)
   =s_i\Theta(C_{s_i^{-1}P};s_i^{-1}P)=s_iS.
\]

The ownership-component theorem says that the two shores have the same
root block and that either complete shore can be chosen while preserving
exactness and every port.  This gives (3.3), and counting roots gives
(3.4). \(\square\)

Combining Theorems 2.1 and 3.1, the single comparison
\(F_r\) versus \(s_1F_r\) contains
\((1/12+o(1))B\) independently selectable packets of shore size at most
any growing polynomial \(p\).  They can move the common target on
\((3/8+o(1))B\) roots, in arbitrary component blocks, while every
intermediate object remains one exact anchored factor.

## 4. Uniform two-row packets for every even-pair swap

The complete component spectrum for an interior \(s_i\) is not needed to
obtain bounded packets.  Let

\[
 P\in\mathcal D_{i-1},\qquad
 R\in\mathcal D_{r-i-1}.
\]

### Theorem 4.1 (shifted two-row component family)

For every \(1\le i<r\), the two roots

\[
                         P1100R,\qquad P1010R          \tag{4.1}
\]

form the old shore of one sealed two-row ownership component of
\(F_r\) versus \(s_iF_r\).  For fixed \(i\), these components are pairwise
disjoint, and their number is exactly

\[
             \operatorname {Cat}_{i-1}
             \operatorname {Cat}_{r-i-1}.             \tag{4.2}
\]

Thus they involve

\[
        2\operatorname {Cat}_{i-1}
          \operatorname {Cat}_{r-i-1}                 \tag{4.3}
\]

canonical roots.  If \(i\) is fixed while \(r\to\infty\), the fraction
of all roots in these two-row packets tends to

\[
               \frac{2\operatorname {Cat}_{i-1}}{4^{i+1}}.
 \tag{4.4}
\]

#### Proof

The MSW concatenation identity makes the four-coordinate rectangle
\(1100\leftrightarrow1010\) literal after any complete Dyck prefix and
before any complete Dyck suffix.  The four omitted-label orders on the two
shores have the same middle support in pairs, so the two roots form a
closed component.  Distinct \((P,R)\) give disjoint root pairs.  This is
the contextual-selector theorem in `MSW_TRANSPOSITION_COMPONENTS.md`;
(4.2) is the number of choices of \(P,R\), and (4.4) follows from the
Catalan ratio. \(\square\)

The sum of the counts (4.2) over all boundaries is

\[
 \sum_{i=1}^{r-1}
   \operatorname {Cat}_{i-1}\operatorname {Cat}_{r-i-1}
 =\operatorname {Cat}_{r-1}.                         \tag{4.5}
\]

Components belonging to different \(i\)'s overlap and are not one common
cube, but (4.5) shows that the bounded splitter is present at every
Catalan recursion boundary.  One may choose the boundary whose coordinate
swap actually moves the common target \(S\).

## 5. Exact limitation

The comparison with one coordinate conjugate does not move every row by a
small packet.  In the \(s_1\) hierarchy, packets of subexponential (in
\(r\)) shore size account asymptotically for at most \(3/8\) of the roots;
the remaining \(5/8\) lie in the sparse macroscopic end of the Catalan
hierarchy.  Therefore the present theorem proves a positive-density exact
splitter and supplies bounded absorbers.  It does not, by itself, flatten
an entire Catalan fibre to bounded multiplicity.  Iteration with other
boundaries or with newly recomputed comparison factors is a separate
quantitative problem.

## 6. The parent-window ledger: apparent many-target routing collapses to one pair

There is a sharper limitation in the actual parent context used by the
plateau repair.  Put \(m=r+1\), and inspect the canonical depth-\(r\)
parent window.  For a first-return root

\[
                         x=1u0v,
\]

its distinguished even target is the local coordinate

\[
                         2(|u|_s+1),                   \tag{6.1}
\]

where \(|u|_s\) is the semilength of \(u\).  Thus all roots \(10v\),
\(v\in\mathcal D_r\), form the Catalan fibre at target \(2\), of size

\[
                         d=\operatorname {Cat}_r.      \tag{6.2}
\]

Consider one \(s_1=(2,3)\) component \(\mathcal K_{j,R}\) in
\(F_{r+1}\).  Its two root arms are

\[
 \begin{aligned}
  \mathcal I_{j,R}&=\{1u0R:u\in\mathcal D_{j+1}\},\\
  \mathcal {II}_{j,R}&=\{10\,1v0R:v\in\mathcal D_j\}.
 \end{aligned}                                        \tag{6.3}
\]

The first arm has distinguished target

\[
                         z_j=2j+4,                     \tag{6.4}
\]

and the second has target \(2\).  Among the
\(\operatorname {Cat}_{j+1}\) roots in the first arm, exactly
\(\operatorname {Cat}_j\) have \(u=10v\); these are exchanged by
\(s_1\) with the second arm.  The remaining
\(\operatorname {Cat}_{j+1}-\operatorname {Cat}_j\) roots begin with
`111` and are fixed as roots by \(s_1\).

### Proposition 6.1 (exact marked conveyor inside one component)

On the distinguished parent-window occurrence, switching
\(\mathcal K_{j,R}\) has the following action:

\[
 \begin{array}{c|c|c}
 \text{number of roots}&\text{old target}&\text{new target}\\ \hline
 \operatorname {Cat}_j&2&z_j\\
 \operatorname {Cat}_j&z_j&3\\
 \operatorname {Cat}_{j+1}-\operatorname {Cat}_j&z_j&z_j.
 \end{array}                                          \tag{6.5}
\]

In particular the intermediate target \(z_j\) is refilled exactly.  The
signed **marked-occurrence** ledger of the component is

\[
              \operatorname {Cat}_j(e_3-e_2),          \tag{6.6}
\]

independent of \(R\); the apparently different coordinates \(z_j\) do
not furnish independent output capacity.

#### Proof

For \(x=10\,1v0R\), swapping positions two and three gives

\[
             s_1x=1(10v)0R\in\mathcal I_{j,R}.         \tag{6.7}
\]

The canonical target of \(x\) is \(2\), while that of \(s_1x\) is
\(z_j\).  In the reanchored conjugate factor, the row rooted at \(x\) is
\(s_1\) applied to the old row rooted at \(s_1x\); since \(z_j\ge4\),
its new target is still \(z_j\).  Conversely, the row rooted at
\(s_1x\) is \(s_1\) applied to the old row rooted at \(x\), so its target
becomes \(s_1(2)=3\).

If \(u\) does not begin with `10`, then the Dyck word \(u\) begins with
`11`.  The corresponding root \(1u0R\) is fixed by \(s_1\), and both its
target \(z_j\) and the target coordinate itself are fixed.  This proves
(6.5)--(6.6). \(\square\)

Equation (6.6) concerns the distinguished occurrences.  Other cyclic arms
of the same physical targets also move.  For the full histogram there is
an even stronger, arm-independent obstruction.

### Theorem 6.2 (coordinate-orbit floor; six stages cannot iterate the split)

Let \(H_r=\langle(2,3),(4,5),\ldots,(2r,2r+1)\rangle\) act on the local
targets, with the exterior coordinates fixed.  Along every sequence of
ownership-component switches between a current factor and one of its
\(H_r\)-coordinate conjugates, the total load on each \(H_r\)-orbit of
targets is invariant.

In particular the two local singleton targets \(2,3\) form one orbit, so

\[
                         \mu(2)+\mu(3)                 \tag{6.8}
\]

is invariant.  Canonically,

\[
 \mu(2)=d=\operatorname {Cat}_r,
 \qquad
 \mu(3)=e=\operatorname {Cat}_{r-1}.                  \tag{6.9}
\]

Every factor reachable by any number of such coordinate-component stages
therefore satisfies

\[
 \max\{\mu(2),\mu(3)\}
 \ge {d+e\over2}
 =d\,{5r-1\over4(2r-1)}
 =\left({5\over8}+o(1)\right)d.                       \tag{6.10}
\]

Consequently a cap \(p=d/\theta\) cannot be reached by this entire move
class whenever

\[
                 \theta>{8r-4\over5r-1}
                         ={8\over5}+o(1).              \tag{6.11}
\]

This includes the plateau regime \(4\le\theta<16\).  Six successive
``\(5/8\)--\(3/8\)'' component stages do not shrink the surviving fibre by
\((5/8)^6\): after the first apparent split, all further coordinate moves
remain trapped in the same two-cell orbit.  The intermediate destinations
\(z_j\) in (6.5) are exactly balanced by displaced canonical occurrences.

#### Proof

Every component switch removes rows and replaces them by coordinate images
under an element of \(H_r\).  For a target orbit \(O\), equivariance gives

\[
 \sum_{T\in O}v(gC;T)=
 \sum_{T\in O}v(C;T),
\]

row by row.  Summing over the switched rows proves orbit-mass invariance;
this is the coordinate-orbit census theorem specialized to the parent
window.  The canonical values (6.9) are the two boundary Catalan counts.
The pigeonhole bound gives (6.10), and solving
\((d+e)/2>p=d/\theta\) gives (6.11). \(\square\)

Thus the exact component hierarchy does provide many bounded, port-valid
packets, but coordinate conjugation alone cannot route them into the
sixteen genuinely different physical target classes required at the fatal
cutoff.  A successful next stage must cross the \(H_r\)-target orbits.  A
mixed-context rooted pentagon, a non-coordinate ownership component, or a
new higher rooted packet can do this in principle; another even-pair
coordinate conjugate cannot.

## 7A. Phase-owner permutations give the components exactly

There is a useful phase-free way to recover the ownership components.  It
also records the inert singleton components which must not be counted as
movable mass.

Let

\[
             \xi_t(P)\qquad(P\in\mathcal D_r,\ 0\le t<2r+1)
\tag{6.1}
\]

be the odd-graph vertex in phase (t) of the canonical row rooted at
(P).  For a coordinate permutation (s) which preserves the phase
transversals, define the phase-owner permutation \(\kappa_t\) by

\[
 s\xi_t(P)\text{ belongs to the canonical row rooted at }
 \kappa_t(P).                                           \tag{6.2}
\]

The even-pair swaps (s_i=(2i\ 2i+1)) have this property: they preserve
every Chung--Feller flaw layer, and the complementary phase transversals
are preserved at the same time.

### Proposition 6.1 (owner-orbit normal form)

The root blocks on the (sF_r)-shore of the ownership overlay
(\Gamma(F_r,sF_r)) are precisely the orbits of

\[
 \boxed{
 G_s=\left\langle
       \kappa_t\kappa_0^{-1}:0\le t<2r+1
      \right\rangle\le\operatorname {Sym}(\mathcal D_r).}
 \tag{6.3}
\]

The blocks on the (F_r)-shore are their corresponding inverse images.
In particular, the number of inert singleton components is exactly

\[
 \boxed{
 \left|\bigcap_t
       \operatorname {Fix}(\kappa_t\kappa_0^{-1})\right|.}
 \tag{6.4}
\]

#### Proof

The overlay edge supplied by the phase-(t) token of the left row (P)
joins (P) to the right row indexed by \(\kappa_t(P)\): indeed

\[
 \xi_t(P)\in sC_Q
 \quad\Longleftrightarrow\quad
 s\xi_t(P)\in C_Q
 \quad\Longleftrightarrow\quad Q=\kappa_t(P).
 \tag{6.5}
\]

Starting at a right root (Q), traverse a phase-(0) edge backwards and
a phase-(t) edge forwards.  The resulting right root is
(\kappa_t\kappa_0^{-1}Q).  Conversely, every two-edge segment in the
overlay has this form with two phases, and

\[
 \kappa_u\kappa_t^{-1}
 = (\kappa_u\kappa_0^{-1})
   (\kappa_t\kappa_0^{-1})^{-1}.
\]

Thus connectedness on the right shore is exactly orbit equivalence under
(G_s).  A shore orbit has size one precisely when every displayed
generator fixes it, proving (6.4). \(\square\)

For (s=s_1), Theorem 1.1 evaluates these orbits completely.  Formula
(1.3) starts at (k_0=2), so

\[
 \boxed{
 \Gamma(F_r,s_1F_r)\text{ has no singleton component}.} \tag{6.6}
\]

This is important: all of the mass counted below is genuinely movable.

## 7B. The critical Catalan-overshoot row-mass truncation

Section 2 treated packet bounds with (J(p)=o(r)).  At the fatal plateau
scale the packet allowance is much larger and a sharper evaluation is
available.  Put

\[
 d=\operatorname {Cat}_r,
 \qquad \theta={d\over p},
 \qquad 4\le\theta<16,                                \tag{7.1}
\]

and let (V_{r,p}) be the number of canonical roots lying in components
of shore size at most (p).  The exact component law gives

\[
 \boxed{
 V_{r,p}=
 \sum_{\substack{0\le j\le r-2\\
        \operatorname {Cat}_j+\operatorname {Cat}_{j+1}\le p}}
 (\operatorname {Cat}_j+\operatorname {Cat}_{j+1})
 \operatorname {Cat}_{r-j-2}.}                       \tag{7.2}
\]

Equivalently put (k=r-j-2).  The component family at suffix depth (k)
has multiplicity \(\operatorname {Cat}_k\) and shore size

\[
 b_{r,k}=\operatorname {Cat}_{r-k-2}
          +\operatorname {Cat}_{r-k-1}.                \tag{7.3}
\]

For every fixed (k),

\[
 {b_{r,k}\over d}
   ={5\over4^{k+2}}+O_k(r^{-1}),
 \qquad
 {\operatorname {Cat}_k b_{r,k}\over d}
   ={5\operatorname {Cat}_k\over4^{k+2}}+O_k(r^{-1}).
 \tag{7.4}
\]

### Theorem 7.1 (uniform (p)-bounded movable mass)

Uniformly for (4\le\theta<16),

\[
 \boxed{
 V_{r,p}\ge
 d-\operatorname {Cat}_{r-1}
   -2\operatorname {Cat}_{r-2}
   -\operatorname {Cat}_{r-3}
 =\left({39\over64}+o(1)\right)d.}                  \tag{7.5}
\]

More precisely, define

\[
 \theta_{1,r}:=
 {\operatorname {Cat}_r
  \over\operatorname {Cat}_{r-3}+\operatorname {Cat}_{r-2}}
 ={64\over5}+O(r^{-1}).                               \tag{7.6}
\]

Away from an (O(r^{-1})) neighbourhood of (64/5),

\[
 {V_{r,p}\over d}=
 \begin{cases}
  {11\over16}+o(1),&4\le\theta<64/5,\\[1mm]
  {39\over64}+o(1),&64/5<\theta<16.
 \end{cases}                                           \tag{7.7}
\]

#### Proof

The sizes in (1.3) increase with (j).  The largest family, (k=0), has
size ratio (5/16+o(1)), and is therefore larger than (p/d\le1/4).
The second family, (k=1), has ratio (5/64+o(1)), and crosses the cap
exactly at (7.6).  The third family, (k=2), has ratio
(5/256+o(1)<1/16).  Hence, uniformly on (7.1), every family with
(k\ge2) has shore size at most (p).  Omitting only (k=0,1) gives
(7.5).  If (k=1) is also admitted, only (k=0) is omitted, giving

\[
 1-{5\over16}={11\over16}.
\]

If it is not admitted, the omitted mass is

\[
 {5\over16}+{5\over64}={25\over64},
\]

which gives (39/64). \(\square\)

The quantity \(V_{r,p}\) is **row mass**, not marked plateau action.  It
must not be compared directly with the fatal matched-child demand.  In the
actual size-\((r+1)\) parent, Proposition 6.1 shows that a component
\((j,R)\) moves only \(\operatorname {Cat}_j\) marked occurrences, even
though its shore has
\(\operatorname {Cat}_j+\operatorname {Cat}_{j+1}\) rows.  Moreover all
those marked vectors are parallel to \(e_3-e_2\).  The coordinate-orbit
floor in Theorem 6.2, not the row count (7.5), is therefore decisive for
the fatal plateau.

## 7C. Full affected histograms of a bounded component

The distinguished target calculation of Theorem 3.1 is not the whole
PCap ledger.  Nevertheless, the same component-size cutoff gives the exact
pointwise bound needed for atomwise rounding.

### Proposition 8.1 (component (L^\infty) bound)

Fix a shadow depth (q), an ownership component (K) with (k) rows on
each shore, and either shore state \(\varepsilon\in\{0,1\}\).  Let
(u_{K,\varepsilon,q}(S)) count the affected rooted depth-(q) windows in
that state whose target is (S).  Then

\[
 \boxed{
 0\le u_{K,\varepsilon,q}(S)\le k
 \quad\text{for every }S,\qquad
 \|u_{K,1,q}-u_{K,0,q}\|_\infty\le k.}              \tag{8.1}
\]

In particular every component retained in (V_{r,p}) satisfies the
atomwise bound (L^{\max}\le p) simultaneously at every depth.

#### Proof

In one cyclic order, cyclic intervals of one fixed proper length are all
distinct.  Thus one row contributes at most one occurrence to a fixed
depth-(q) target.  Restricting to the windows affected by a parent
substitution cannot increase that multiplicity.  Summing over the (k)
rows on one shore proves the first inequality, and subtracting the two
shore histograms proves the second. \(\square\)

If all local cyclic starts are retained, the accompanying coarse total
variation bound is

\[
 \|u_{K,1,q}-u_{K,0,q}\|_1
 \le2(2r+1)k,                                         \tag{8.2}
\]

and a parent affected-window restriction only decreases the right side.
The pointwise estimate (8.1), rather than (8.2), is the relevant rounding
input.

What remains is a routing theorem.  One comparison (F_r\) versus
(s_1F_r) sends the common target only to (s_1S); it does not by itself
provide all (4) to (16) residual destinations forced by Catalan
overshoot, nor does (8.1) determine the signs of the crossing-window
collateral.  The exact surviving gate is to combine several coordinate
conjugates (or recomputed comparison factors) so that the componentwise
target splits satisfy the full multidepth residual-capacity dual.  The
count, integrality, anchoring, and atomwise (p)-fragmentation sides of
that gate are settled by Theorems 3.1, 7.1, and Proposition 8.1.
