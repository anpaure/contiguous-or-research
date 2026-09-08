# Missing-mask potential in an interaction-component cube

## 1. Setup and outcome

Put

\[
        n=2m+1,\qquad \Omega_m=\binom{n}{m}=n\operatorname{Cat}_m.
\]

Let (F) be an exact factor of the middle layer by wreaths, let
(\tau) be a coordinate transposition, and form the interaction graph
between (F) and (\tau F).  Each connected component can be switched
independently.  This note records the exact missing-mask potential in that
Boolean cube.

The main conclusions are:

1.  A component cube acts independently on the one- and two-element
    orbits of (\tau) in each Boolean layer.  Fixed targets are frozen
    component by component.
2.  On a moved orbit (\{S,\tau S\}), either one component contains an
    occurrence of both targets, in which case neither can ever be missing,
    or the expected number missing after fair switching is exactly
    (2^{1-d}), where (d) is the number of components met by the two
    occurrence families.
3.  At fixed depth from the middle, the total occurrence budget is only
    (1+O(1/m)) per target.  Consequently, fair switching can have
    (o(N_r)) expected misses only if all but (o(N_r)) targets already
    have a **two-sided occurrence inside one component**.  Large
    flexibility counts by themselves cannot prove low excess.
4.  A single transposition freezes asymptotically half of a central layer.
    The family of disjoint contextual MSW transpositions has only an
    exponentially small common fixed set, but its cubes cannot presently be
    applied simultaneously.  This is the exact place where recursive
    stability or an adaptive multi-transposition argument is needed.
5.  The heat-bath quadratic ledger has a sharp first-shadow obstruction for
    the audited MSW transposition ((2\ 3)): through (m=10), the fair cube
    expands rank (m-1) energy and contracts every deeper rank for (m\ge5).
    At rank (m-1), every Catalan component-size class is individually
    neutral; the expansion comes entirely from cross-class cancellation.

These statements show that component fragmentation is useful only when it
is paired with the correct occurrence geometry.  Merely having a
high-dimensional legal cube is not enough.

## 2. The interaction graph is transposition-stable

Identify the right-hand vertex (\tau C\in\tau F) with its preimage
(C\in F).  If (M) is a middle mask, its interaction edge joins

\[
       C_F(M)\quad\hbox{to}\quad C_F(\tau M).
\]

The edge belonging to (\tau M) is the reverse edge.  Thus, after this
identification, the interaction graph is an undirected multigraph on the
wreaths of (F).  A component is a set (K\subseteq F), and its two
sides are exactly

\[
                   L_K=K,\qquad R_K=\tau K.             \tag{2.1}
\]

For a rank-(r) target (S), let

\[
 a_K(S)=\#\{C\in K:S\text{ is a cyclic }r\text{-interval of }C\}.
\]

The occurrence count on the other side is therefore

\[
                    b_K(S)=a_K(\tau S).                 \tag{2.2}
\]

Equation (2.2), rather than component size alone, controls the missing-mask
potential.

## 3. Exact orbit formula

### Theorem 1 (one target)

Choose the two sides of all interaction components by independent fair
coins.  If some component satisfies

\[
                         a_K(S)>0,qquad b_K(S)>0,
\]

then (S) is present for every cube vertex.  Otherwise put

\[
 d_S=\#\{K:\text{exactly one of }a_K(S),b_K(S)\text{ is positive}\}.
\]

Then

\[
              \Pr(S\text{ is missing})=2^{-d_S}.       \tag{3.1}
\]

#### Proof

All component contributions are nonnegative.  If both sides of one
component contain (S), that component guarantees (S).  Otherwise every
one-sided component forces one specified value of an independent fair coin
for (S) to be absent, and components with two zero sides impose no
condition.  This gives (3.1).  QED.

The transposition symmetry sharpens this to a two-target statement.

### Theorem 2 (exact transposition-orbit potential)

If (\tau S=S), then the count of (S) is constant at every cube vertex.

If (T=\tau S\ne S), write

\[
                       x_K=a_K(S),\qquad y_K=a_K(T).
\]

If (x_K,y_K>0) for some (K), both (S) and (T) occur at every cube
vertex.  Otherwise let

\[
                 d_{\{S,T\}}=\#\{K:x_K+y_K>0\}.        \tag{3.2}
\]

Then

\[
 \boxed{
  \mathbb E\bigl[\#\text{ missing targets in }\{S,T\}\bigr]
        =2^{1-d_{\{S,T\}}}.}                          \tag{3.3}
\]

The formula includes (d=0), when both targets are missing.

#### Proof

For a fixed target, (2.2) says that switching component (K) exchanges the
pair of contributions

\[
                           (x_K,y_K)\longleftrightarrow(y_K,x_K).
\]

If (S=T), this changes nothing component by component.  Suppose (S\ne T).
If one component has (x_K,y_K>0), that component supplies both targets in
either orientation.  Otherwise, each of the (d) relevant components
supplies exactly one member of the pair.  The target (S) is missing for
one prescribed outcome of all (d) coins, and (T) is missing for the
opposite outcome.  Each event has probability (2^{-d}), proving (3.3).
QED.

### Missing-duplicate repair

Suppose initially

\[
                           c_S(F)=0,\qquad c_T(F)=t>0.
\]

Let (g) be the number of interaction components containing the (t)
occurrences of (T).  Then (d_{\{S,T\}}=g), and

\[
        \mathbb E[\#\text{ missing in }\{S,T\}]=2^{1-g}. \tag{3.4}
\]

For (t=1), necessarily (g=1), and switching merely moves the hole from
one endpoint to the other.  For (t\ge2), a genuine expected repair occurs
only when the duplicate occurrences meet at least two components.  This is
the precise sense in which component fragmentation creates useful
flexibility.

## 4. The exact missing/excess identity

Every wreath contains exactly (n) cyclic intervals of each nontrivial
rank.  Hence every exact middle factor has, at every rank (r), exactly

\[
                         \sum_{|S|=r}c_S(F)=\Omega_m    \tag{4.1}
\]

occurrences.  Put (N_r=\binom nr) and

\[
                         M_r(F)=\#\{S:|S|=r,c_S(F)=0\}.
\]

Then

\[
 \boxed{
 M_r(F)=\sum_{|S|=r}(c_S(F)-1)_+-(\Omega_m-N_r).}       \tag{4.2}
\]

Indeed, the sum of (c_S-1) over covered targets is total occurrences minus
the number of covered targets.  Thus minimizing missing masks is exactly
minimizing excess multiplicity; perfect uniform multiplicities are stronger
than necessary.

## 5. An incidence-budget obstruction to uniform random switching

Call a target **robust in the cube** if one component contains it on both
sides.  Let (H) be the number of robust rank-(r) targets, let
(U=N_r-H), and use (d_S) for every nonrobust target as in Theorem 1.

Each robust target consumes at least two side-occurrences, and every
one-sided component counted by (d_S) consumes at least one.  The two sides
of all components contain (2\Omega_m) rank-(r) occurrences in total.
Therefore

\[
                    2H+\sum_{S\text{ nonrobust}}d_S
                         \le 2\Omega_m.                \tag{5.1}
\]

Since (x\mapsto2^{-x}) is convex, Theorem 1 and Jensen's inequality give

\[
 \boxed{
 \mathbb E M_r
   \ge U\,2^{-\,2(\Omega_m-H)/U}.}                    \tag{5.2}
\]

For (r=m-q),

\[
 \lambda_q:=\frac{\Omega_m}{N_{m-q}}
  =\frac{(m-q)!(m+q+1)!}{m!(m+1)!}
  =1+\frac{q(q+1)}m+O_q(m^{-2}).                      \tag{5.3}
\]

Consequently, for every fixed (q):

> If fair component switching has (o(N_{m-q})) expected misses, then all
> but (o(N_{m-q})) targets must be robust in one component.

To see this, if (U\ge\varepsilon N_{m-q}), then (5.2)--(5.3) give

\[
                 \mathbb E M_{m-q}\ge(1/4-o(1))U.
\]

In particular, if no target is robust, the expected missing fraction is at
least

\[
                         2^{-2\lambda_q}=1/4-o(1).     \tag{5.4}
\]

This rules out the tempting argument that a large number of independent
one-sided choices, by itself, should yield a low-excess factor.  The average
flexibility budget is asymptotically only two.  Almost-everywhere two-sided
pairing, or an adaptive deterministic scheme using several transpositions,
is necessary.

## 6. The frozen-target obstruction and how many transpositions are needed

For one transposition, the number of fixed rank-(r) masks is

\[
 N_r^{\rm fix}
   =\binom{n-2}{r}+\binom{n-2}{r-2},                  \tag{6.1}
\]

and the fixed fraction is

\[
 \alpha_{n,r}
  =\frac{r(r-1)+(n-r)(n-r-1)}{n(n-1)}.               \tag{6.2}
\]

For (r=m-q) with fixed (q), (\alpha_{n,r}=1/2+O_q(1/m)).  Every
missing fixed target survives every vertex of that component cube.

There is a useful positive counterpart.  The contextual MSW transpositions

\[
                     (2s+2\ \ 2s+3),\qquad0\le s\le m-2,
\]

act on (m-1) disjoint coordinate pairs, leaving three coordinates
unpaired.  A mask fixed by all of them must contain either both or neither
coordinate in each pair.  Hence the number of common fixed rank-(r) masks
is

\[
 [x^r](1+x)^3(1+x^2)^{m-1}.                           \tag{6.3}
\]

For central (r), (6.3) is at most (2^{m+2}), whereas
(N_r=\Theta_q(4^m/\sqrt m)).  Thus their common fixed fraction is

\[
                         O_q(\sqrt m\,2^{-m}).         \tag{6.4}
\]

The invariant-target obstruction is therefore a one-transposition
obstruction, not an obstruction to the whole contextual family.  What is
missing is legality under composition: charts at different boundaries
overlap, and after one switch the next MSW chart need not survive.  This is
exactly the recursive-stability clause in the proposed Catalan absorption
theorem.

## 7. The best orbit-wise correction allowed by one transposition

Every cube vertex preserves the total occurrence mass on each orbit of
(\tau).  Define the orbit floor

\[
 \Psi_\tau(c)
   =\sum_{O\in\binom{[n]}r/\langle\tau\rangle}
      \left(|O|-\sum_{S\in O}c_S\right)_+.            \tag{7.1}
\]

Every factor in the cube has at least (\Psi_\tau(c)) missing rank-(r)
targets.  If

\[
          Z=\{S:c_S=0\},\qquad D=\{S:c_S\ge2\},
\]

then

\[
                         \Psi_\tau(c)=M_r(c)-R_\tau(c), \tag{7.2}
\]

where (R_\tau(c)) is the number of moved pairs (\{S,\tau S\}) with one
endpoint in (Z) and the other in (D).  Such a pair is the only orbit on
which occurrence mass is sufficient to fill an existing hole.

Let (J(n,r)) be the Johnson graph.  Every Johnson edge is the moved pair
of exactly one coordinate transposition.  Averaging (7.2) over all
transpositions gives the exact formula

\[
 \boxed{
 \mathbb E_\tau\Psi_\tau(c)
   =M_r(c)-\frac{e_{J(n,r)}(Z,D)}{\binom n2}.}          \tag{7.3}
\]

Thus the next deterministic descent theorem has two clean parts:

1. prove that missing masks and duplicate masks have many Johnson edges
   between them, using the exact zero point-marginal constraints of a wreath
   factor;
2. prove that on many of those edges the duplicate occurrences are split
   among at least two interaction components, so that (3.4) realizes a
   positive fraction of the orbit-wise repair.

No generic expansion statement currently proves either assertion for the
MSW factor, but (7.3) identifies the exact graph quantity.

## 8. Detailed balance and the quadratic heat ledger

For fixed (\tau), all factors obtained from one interaction cube have the
same component decomposition.  From every cube vertex, fair resampling
returns the uniform distribution on that cube.  Hence the heat-bath kernel
is symmetric and reversible with respect to counting measure on the exact
factor fibre.

Let

\[
 f_r=c_r(F)-\mu_r{\bf1},\qquad
 \mu_r=\Omega_m/N_r,
\]

and

\[
 \Delta_{K,r}=B_r({\bf1}_{R_K}-{\bf1}_{L_K}).
\]

Put

\[
 A_{\tau,r}=\|\tau c_r(F)-c_r(F)\|_2^2,
 \qquad
 V_{\tau,r}=\sum_K\|\Delta_{K,r}\|_2^2.              \tag{8.1}
\]

The exact conditional ledger is

\[
 \boxed{
 \mathbb E\|c_r(G)-\mu_r{\bf1}\|_2^2
  =\|f_r\|_2^2+\frac14(V_{\tau,r}-A_{\tau,r}).}       \tag{8.2}
\]

For a uniform coordinate transposition, the mean is the lazy
random-transposition walk on the Johnson layer.  Its eigenvalue on Johnson
harmonic (j) is

\[
             1-\frac{j(n-j+1)}{2\binom n2}.           \tag{8.3}
\]

Every exact-factor discrepancy has zero total and zero point marginals, so
only (j\ge2) occurs.  Therefore

\[
 \mathbb E_\tau\left\|\frac{f_r+\tau f_r}{2}\right\|_2^2
       \le\left(1-\frac2n\right)\|f_r\|_2^2.          \tag{8.4}
\]

Combining (8.2)--(8.4), a sufficient all-rank bulk theorem is the component
variance bound

\[
        \mathbb E_\tau V_{\tau,r}
             \le (8/n-o(1/n))\|f_r\|_2^2.            \tag{8.5}
\]

The continuous smoothing is already complete; (8.5) is the integral gate.

## 9. The exact ((2\ 3)) MSW ledger and its class reduction

For the explicit MSW factor and (\tau=(2\ 3)), remote exact enumeration
gives the following first-shadow values.  No enumeration was run on the
local Mac.

\[
\begin{array}{c|rrrrrrrr}
m&3&4&5&6&7&8&9&10\\ \hline
A_{\tau,m-1}&4&20&76&292&1104&4152&15596&58676\\
V_{\tau,m-1}&8&28&96&340&1228&4492&16580&61648\\
A-V&-4&-8&-20&-48&-124&-340&-984&-2972
\end{array}                                             \tag{9.1}
\]

Thus the fair ((2\ 3)) heat bath expands first-shadow quadratic energy in
every audited dimension.  In contrast, for every (m\ge5), all audited
ranks (2\le r\le m-2) have (A_{\tau,r}-V_{\tau,r}>0).  For example, at
(m=10) the gaps from ranks (2) through (9) are

\[
 37131936,13725044,3946552,1197228,358564,97096,14156,-2972.
                                                               \tag{9.2}
\]

There is a sharper structural pattern.  Group the conjectured interaction
components by their Catalan atom size

\[
                     s_j=\operatorname{Cat}_j+operatorname{Cat}_{j+1}.
\]

Let

\[
             D_{j,r}=\sum_{K:\,|K|=s_j}\Delta_{K,r}.
\]

At rank (m-1), through (m=10), every size class separately satisfies

\[
 \boxed{
       \|D_{j,m-1}\|_2^2
          =\sum_{K:\,|K|=s_j}\|\Delta_{K,m-1}\|_2^2.} \tag{9.3}
\]

Equivalently, the component effects within one atom-size class have zero
total cross inner product.  Consequently the whole sign problem reduces
exactly to

\[
 A_{\tau,m-1}-V_{\tau,m-1}
       =2\sum_{i<j}\langle D_{i,m-1},D_{j,m-1}\rangle. \tag{9.4}
\]

The negative values in (9.1) come entirely from cancellation between
different Catalan scales, not from fragmentation within a scale.

Equation (9.4) is the correct symbolic target.  A proof should use the
candidate component classification (\{AR:A\in\mathcal A_j\}) and classify
when rank-((m-1)) boundary flags from two different atom lengths encode the
same target.  The data strongly suggest a signed Catalan convolution, but no
all-(m) sign proof is claimed here.

## 10. Flexibility supplied by the contextual size-two charts

For a fixed Dyck boundary (s), the contextual theorem supplies

\[
               h_s=\operatorname{Cat}_s
                    \operatorname{Cat}_{m-s-2}        \tag{10.1}
\]

independent two-for-two components.  At rank (m-1), their four-entry
effect supports are disjoint.  Hence a target has local action load at most
one.  In particular, a currently missing target has (d_S\le1) in this
local cube, and a fair switch repairs it with probability at most (1/2).

Across all contextual boundary occurrences,

\[
                  \sum_{s=0}^{m-2}h_s=\operatorname{Cat}_{m-1}. \tag{10.2}
\]

The total first-shadow action incidence is therefore
(4\operatorname{Cat}_{m-1}).  Since

\[
 N_{m-1}=\frac{m}{m+2}(2m+1)\operatorname{Cat}_m,
\]

its average action load is

\[
 \frac{4\operatorname{Cat}_{m-1}}{N_{m-1}}
  =\frac{2(m+1)(m+2)}{m(2m-1)(2m+1)}
  =\frac1{2m}+O(m^{-2}).                              \tag{10.3}
\]

At every fixed deeper rank (m-q), (q\ge2), each local trade has support
eight, so the corresponding average action load is still (O_q(1/m)).
For a currently missing target, one-sided flexibility is bounded by this
action load.  Thus the contextual size-two charts can alter only
(O(\operatorname{Cat}_m)=O(\Omega_m/m)) target occurrences in one complete
atlas.  They are a sparse absorber, not a bulk random frame.

## 11. Consequence for the global programme

Repeated fair switching for one transposition cannot establish a low-miss
factor at fixed depth:

* asymptotically half the targets are frozen;
* the occurrence budget forces almost-everywhere robust two-sided pairing
  before the expected miss can be (o(N_r));
* in the explicit MSW cube, the first lower shadow has the wrong quadratic
  drift sign.

The viable alternatives are therefore sharply limited:

1. an adaptive sequence of different transpositions that routes holes to
   duplicate neighbors and uses component fragmentation to split the
   duplicate mass, quantified by (3.4) and (7.3);
2. a nonlocal component theorem proving almost-everywhere two-sided
   occurrence pairing at each fixed depth;
3. a weighted multirank descent in which the strong contraction below the
   first shadow pays for its much smaller first-shadow expansion, followed
   by a reserved local absorber.

This is a stronger and more honest target than merely proving that the
component cube has many dimensions.
