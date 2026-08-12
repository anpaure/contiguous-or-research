# Unrelated two-seed overlays at growing scale: an exact bulk cube and the carrier-locality ceiling

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Decision

Throughout,

\[
                         p=2m+1,\qquad W=\binom{p}{m},
 \qquad C_t=\operatorname {Cat}_t.                    \tag{0.0}
\]

Overlaying two unrelated exact rooted factors gives genuine integral
trades.  No coordinate relabelling is needed, and the component choices can
change higher shadow fibres and any target-orbit mass on which the component
profile has nonzero projection.

There is an exact growing-scale bulk construction.  Let `F_r,G_r` be any
two rooted `D_r`-port exact factors.  Insert their direct ownership overlay
at the first size-`r` fringe subtree of every size-`m` Catalan root.  The
nonavoiding roots split into classes of exactly `C_r` fillings, and every
local overlay component lifts to an independently switchable global
component of the same size.  If `a_(m,r)` is the number of roots with no
size-`r` fringe subtree, then

\[
 {a_{m,r}\over C_m}
 \le C m^{3/2}\exp\!\left(-c{m\over r^{3/2}}\right).  \tag{0.1}
\]

Thus the construction covers `1-o(1)` of all wreath rows whenever

\[
                         {m\over r^{3/2}}\gg\log m.    \tag{0.2}
\]

In particular it remains a bulk construction at the genuinely growing
scale `r=Theta(sqrt(m))`.

The exact global size-biased component second moment is inherited from the
local overlay.  If the local component sizes are `s_1,...,s_J`, put

\[
                         \chi_r={1\over C_r}\sum_j s_j^2.          \tag{0.3}
\]

Then the lifted global overlay has

\[
 \boxed{
 \chi_m={a_{m,r}\over C_m}
 +\left(1-{a_{m,r}\over C_m}\right)\chi_r.}           \tag{0.4}
\]

So bounded local components really do give bounded global rounding
variance on a positive-density bank.

This is not merely conditional.  Suspending the rooted pentagon once and
right-concatenating every `B in D_(r-4)` gives two explicit exact size-`r`
factors with `C_(r-4)` independent five-row components.  Their complete
depth-one shadow histograms differ in `l_1` norm `18C_(r-4)`, their
`H_r`-orbit masses differ in `l_1` norm `16C_(r-4)`, and

\[
                              \chi_r\longrightarrow{69\over64}.  \tag{0.4a}
\]

Thus unrelated two-seed overlays genuinely escape frozen orbit mass and
give a positive-density row/component bank with genuine complete-shadow
motion at every growing local scale.  Its density in the full cyclic
occurrence ledger is smaller and is quantified in Section 6.

The canonical flip-every-slot amplification is also classified exactly:
tensorizing the same packet over every eligible fringe slot raises tagged
shadow action to constant occurrence density, but a class with `k` slots
becomes one `5^k`-row component and

\[
                         \chi_r\ge5^{(5/256+o(1))r}.   \tag{0.4b}
\]

Thus this natural bounded-core tensorization encounters an exponential
action--fragmentation tradeoff; this is not asserted for every conceivable
correlated amplification.

There is also an exact statewise obstruction with the correct locality
scale.  Suppose the two local seeds,
after insertion in a common row context, differ only by reordering one
contiguous carrier block of `b` coordinates.  Every component signing then
satisfies

\[
 \boxed{
 \sum_{q\le H}{1\over2}
   \|\mu_q^{\rm child}-\mu_q^{F}\|_1
 \le {2bH\over2m+1}W.}                               \tag{0.5}
\]

The same right side bounds the total change of every projected orbit-mass
vector and of every scalar floor-corrected cap potential of the form in
Theorem 5.2.  Consequently

\[
                              bH=o(m)                 \tag{0.6}
\]

is statewise incapable of repairing any `Omega(W)` shadow/cap defect,
irrespective of how unrelated the two factors are or how their overlay is
signed.

For a size-`r` one-hole factor, `b=2r+1`.  Hence at a Gaussian window
`H=Theta(sqrt(m))`, every `r=o(sqrt(m))` strict one-hole two-seed fringe
architecture is closed.  The first scale not ruled out is

\[
                              r=Omega(sqrt(m)).        \tag{0.7}
\]

The audited `D_4` pair-transfer factors illustrate both sides.  Their
fringe bank covers almost every Catalan row and has fourteen-row exact
components which change literal higher carrier profiles.  Nevertheless
`b=9`, so its total action over `H=O(sqrt(m))` depths is `o(W)`.  Positive
row density is therefore not positive shadow capacity.

The exact surviving constant-one object is now an unrelated pair with
`r=Omega(sqrt(m))` and active carrier width `b=Omega(sqrt(m))`;
`r=Theta(sqrt(m))` is the minimal critical scale, where this means genuinely
root-scale-active.  Neither statement forces an upper scale.  The pair must
also have a fragmented local overlay and must support either a favourable
directed full-profile sign or a correlated selection theorem which evades
the protected-mass dual.  The explicit pentagon pair has the right
fragmentation and orbit motion but only a bounded active carrier, so no pair
satisfying these requirements is constructed here.

## 1. Arbitrary rooted ownership overlays are literal trades

Write `C_r=Cat_r`.  A rooted `D_r`-port factor has one complement path

\[
 P=X_0,X_1,\ldots,X_r=\overline P,
 \qquad P\in D_r,                                     \tag{1.1}
\]

and adjacent-union tokens

\[
                         Y_i=X_i\cup X_{i+1}.          \tag{1.2}
\]

Across all rows, the `X` tokens enumerate every `r`-subset of `[2r]` and
the `Y` tokens enumerate every `(r+1)`-subset, once each.

Let `F_r,G_r` be two arbitrary rooted factors with the same prescribed
ports.  Their ownership overlay is the bipartite graph whose left vertices
are the rows of `F_r`, whose right vertices are the rows of `G_r`, and
whose edges are the common physical `X/Y` tokens.  Every vertex has degree
`2r+1`.

### Theorem 1.1 (port-compatible component trade)

For every connected overlay component `K`:

1. its two shores contain the same number `s_K` of rows;
2. the two shores own exactly the same physical token set;
3. the set of root labels on the two shores is the same; and
4. either complete shore may replace the other while preserving exact
   `X/Y` ownership and every root/complement port.

Every independent choice of one shore from every component is therefore
one literal integral rooted factor.

#### Proof

Regularity gives equal shore sizes in each connected component.  An edge
cannot leave a component, so each shore owns exactly the edge-token set of
that component.  The initial token `X_0=P` is owned by the row rooted at
`P` on both sides; it gives a diagonal edge between those two rows.  Hence
a component contains the left row labelled `P` if and only if it contains
the right row labelled `P`.  Choosing one shore therefore retains exactly
one row at every root in that common root set, with the same complementary
endpoint.  Its token ledger is unchanged.  Components have disjoint token
sets, so all shore choices compose. \(\square\)

This theorem is not a relabelling construction.  `F_r` and `G_r` may have
different target-orbit masses and different shadow profiles.

Equivalently, if `M_0` is the owned-token/row incidence matrix and

\[
                         \tau_K=\mathbf1_{G_K}-\mathbf1_{F_K},   \tag{1.2a}
\]

then

\[
                              M_0\tau_K=0.             \tag{1.2b}
\]

Thus every component is a box-feasible unit-coefficient integral kernel
trade.  Lower-shadow maps send it to the genuine effect
`M_q tau_K=delta_(K,q)`.  Unlike partial translate-orbit selection, no
real-nullity lifting is needed once the second exact seed is supplied; the
entire ownership component is already an integral trade atom.

If a more general recursive interface uses port tokens which are not among
the owned `X/Y` tokens, one must add an edge between the two candidate rows
for every such common external port and then take connected components of
this augmented graph.  These **port-closed components** are the true
independent atoms.  The same proof applies because port edges merely merge
ordinary ownership components.  Conversely, the equations saying that
every owned token and every external port chooses exactly one compatible
row force a hybrid to be constant on each augmented component.  In the
rooted `D_r` setting above, the ports `P,bar P` are already owned `X`
tokens, so no extra closure is needed.

For a complete fixed-depth cyclic target histogram, let `u_K,v_K` be the
two component-shore loads and put

\[
                              \delta_K=v_K-u_K.        \tag{1.3}
\]

The universal linear constraints on this complete cyclic profile are

\[
             \sum_T\delta_K(T)=0,
 \qquad
             \sum_{T\ni x}\delta_K(T)=0
             \quad(x\text{ a coordinate}).           \tag{1.4}
\]

Indeed both shores have the same number of cyclic rows, every row
contributes the same number of targets, and a coordinate occurs in the same
number of fixed-length cyclic intervals in every row.  Thus component
effects have no degree-zero or degree-one part.  There is no corresponding
universal degree-two invariant: the audited unrelated `D_4` factors have
nonzero length-two and length-three carrier profiles.

For a boundary-resolved subprofile rather than all cyclic starts, even the
point-margin identity need not hold; its omitted complementary starts must
be retained separately in the full occurrence tensor.

If a group `Gamma` acts on the target set, the component changes the mass
of an orbit `O` by

\[
                              \sum_{T\in O}\delta_K(T).            \tag{1.5}
\]

Hence unrelated overlays change orbit mass exactly when (1.5) is nonzero;
there is no orbit conservation unless supplied by an actual symmetry of
the two component shores.

## 2. Exact first-fringe packetization

Identify `D_m` with ordered binary trees having `m` nodes.  Let
`a_(m,r)` count size-`m` trees which contain no fringe subtree of size
exactly `r`.

For every nonavoiding tree, select its first size-`r` fringe root in
preorder.  Replacing the subtree at that root by any other size-`r` tree
leaves every outside fringe size and every ancestor size unchanged; the
marked root itself still has size `r`.  Nodes internal to the replacement
come later in preorder, so none can precede the marked root as a size-`r`
fringe root.  Therefore the nonavoiding trees split into exact equivalence classes

\[
                              \mathcal C=C[ D_r]       \tag{2.1}
\]

of size `C_r`, indexed by one-hole tree contexts `C[ ]`.  In particular

\[
                    P_{m,r}:={C_m-a_{m,r}\over C_r}   \tag{2.2}
\]

is an integer.

Install `F_r` on every class (2.1), keeping the canonical rows on the
avoiding family, and call the resulting global factor `widehat F`.
Installing `G_r` instead gives `widehat G`.

### Theorem 2.1 (growing exact bulk overlay)

The two global objects `widehat F,widehat G` are exact rooted `D_m`-port
factors.  Their direct ownership overlay consists of:

* one lifted copy of every local `F_r/G_r` overlay component in every one
  of the `P_(m,r)` contexts; and
* `a_(m,r)` diagonal singleton components on the avoiding rows.

All lifted components are independently switchable.  If a local component
has a nonzero carrier profile, its lift changes the corresponding literal
shadow fibre after adjoining the context's exterior carrier.

#### Proof

The rooted context functor preserves rowwise ports and transports equal
local `X/Y` ledgers to equal global ledgers.  Hence replacing the complete
`C_r`-row packet in one class preserves exactness.  The root classes in
(2.1) are disjoint, so all replacements compose.

Within one class, the two shores own the same global token set: outside the
hole their row pieces agree, while inside the hole equality is the local
exact ledger.  Therefore no ownership edge joins two different classes.
The common outside pieces add only diagonal same-root edges, already forced
by the common local ports, so the component partition inside a class is
exactly the local one.  Avoiding rows are identical on the two seeds and
give singleton components.  The carrier-profile assertion is the literal
context push-forward of (1.3). \(\square\)

This is a positive bulk trade theorem: it constructs an exact integral
switching cube from genuinely unrelated seed factors.  It does not assert
that all component signs have a favourable cap direction.

## 3. The growing fringe reservoir is asymptotically complete

Let

\[
                         A_r(z)=\sum_{m\ge0}a_{m,r}z^m.            \tag{3.1}
\]

A tree is empty or consists of a root and two avoiding children, except
that every one of the `C_r` trees of total size `r` must be removed.  Thus

\[
                         A_r(z)=1+zA_r(z)^2-C_rz^r,    \tag{3.2}
\]

and

\[
 A_r(z)={1-\sqrt{1-4z+4C_rz^{r+1}}\over2z}.          \tag{3.3}
\]

### Theorem 3.1 (uniform growing-fringe bound)

There are absolute constants `c,C>0` such that, for all sufficiently large
`r` and all `m>=2r`,

\[
 \boxed{
 {a_{m,r}\over C_m}
 \le C m^{3/2}\exp\!\left(-c{m\over r^{3/2}}\right).} \tag{3.4}
\]

Consequently `a_(m,r)=o(C_m)` under (0.2).

#### Proof

Use the standard absolute Catalan bounds

\[
 c_0{4^r\over r^{3/2}}\le C_r
 \le c_1{4^r\over r^{3/2}}.                           \tag{3.5}
\]

Choose a fixed sufficiently small `eta>0` and put

\[
                         z_r={1+\eta r^{-3/2}\over4}.  \tag{3.6}
\]

At `z_r`, the discriminant in (3.3) is

\[
 -\eta r^{-3/2}
 +{C_r\over4^r}(1+\eta r^{-3/2})^{r+1}>0             \tag{3.7}
\]

when `eta<c_0/2`.  Its derivative is

\[
 -4+4(r+1)C_rz^r=-4+O(r^{-1/2})<0                    \tag{3.8}
\]

throughout `[0,z_r]`.  Hence the discriminant is positive on the entire
real interval `[0,z_r]`.  If the Taylor series of `A_r` had radius at most
`z_r`, Pringsheim's theorem (the coefficients are nonnegative) would force
a singularity at a positive real point in that interval.  Formula (3.3)
and the strict discriminant inequality exclude such a singularity.
Therefore the radius is larger than `z_r`; moreover (3.3) gives
`A_r(z_r)<2`.  Nonnegative coefficients give

\[
                         a_{m,r}\le2z_r^{-m}.          \tag{3.9}
\]

Divide by the lower Catalan bound
`C_m>=c_0 4^m/m^(3/2)` and use

\[
 (1+\eta r^{-3/2})^{-m}
 \le\exp(-c m/r^{3/2}).                               \tag{3.10}
\]

This proves (3.4). \(\square\)

## 4. Exact inheritance of component fragmentation

Let the local component sizes be `s_1,...,s_J`.  They satisfy

\[
                              \sum_js_j=C_r.           \tag{4.1}
\]

An exact middle factor on `2m+1` coordinates has `C_m=W/(2m+1)` wreath
rows.  Therefore the size-biased component parameter of the lifted overlay
is

\[
\begin{aligned}
 \chi_m
 &={1\over C_m}\left(a_{m,r}+P_{m,r}\sum_js_j^2\right)\\
 &={a_{m,r}\over C_m}
  +\left(1-{a_{m,r}\over C_m}\right)
       {1\over C_r}\sum_js_j^2,
\end{aligned}                                          \tag{4.2}
\]

which is (0.4).

Thus if `chi_r=O(1)`, then `chi_m=O(1)`.  The general two-seed fair-rounding
identity then gives component variance `O(W)` at each depth.  If the local
overlay is connected, `chi_r=C_r`, and the bulk cube has one `C_r`-row bit
per fringe context; fair variance need not be small.  This is an exact
fragmentation criterion, not a relabelling-energy argument.

There is a complementary overlap cost.  In a global ownership component
`K`, let

\[
 \lambda_K=\max\{|C\cap D|:C\text{ a first-shore wreath},
                         D\text{ a second-shore wreath in }K\},  \tag{4.3}
\]

where the intersection counts common owned middle sets.  Since one
first-shore row has `2m+1` middle sets and each opposite row receives at
most `lambda_K` of them,

\[
 \boxed{
                  s_K\ge\left\lceil{2m+1\over\lambda_K}\right\rceil.}
                                                                  \tag{4.4}
\]

Thus genuinely low-overlap unrelated seeds (`lambda_K=O(1)`) cannot have
bounded components: every nontrivial component has `Omega(m)` rows.  In
particular the small-component sufficient theorem below forces substantial
row overlap; unrelatedness of the endpoint factors is not the same as
pairwise disjointness of their wreaths.

## 4A. Full-profile positive rounding and the exact hinge dual

The component cube admits a sharper formulation directly in cap space.
This is useful because it includes collars and background occurrences,
whereas a marked carrier profile alone does not.

Throughout this section the controlled cyclic interval at depth `q` is
nondegenerate: its length lies in `{1,...,2m}`.  Thus one labelled cyclic
row contributes at most once to any fixed physical target.  This is the
range used by the lower/upper shadow ledgers.  The empty and full interval
levels are deterministic and must be deleted before applying the
`l_infinity` estimates below.

Write

\[
                         K_p(x)=\sum_S(x(S)-p)_+.      \tag{4A.0}
\]

Let `K` run over the port-closed components of any unrelated global
overlay.  At depth `q`, write `u_(K,q),v_(K,q)` for its two complete
occurrence histograms and let `lambda_q` be the unaffected background.  If
`x_K` is zero on the first shore and one on the second, then

\[
 \mu_q(x)=\lambda_q+
       \sum_K\bigl((1-x_K)u_{K,q}+x_Kv_{K,q}\bigr).    \tag{4A.1}
\]

The same `x_K` occurs at every depth.  Any window depending on several
local choices must first merge those choices into one joint port-closed
block; after that closure, (4A.1) is literal.

For a component containing `b_K` wreath rows per shore, define its action

\[
 A_{K,q}={1\over2}\|v_{K,q}-u_{K,q}\|_1
 = (2m+1)b_K-\sum_S\min\{u_{K,q}(S),v_{K,q}(S)\}.     \tag{4A.2}
\]

Then

\[
 \|v_{K,q}-u_{K,q}\|_\infty\le b_K,
 \qquad
 \|v_{K,q}-u_{K,q}\|_2^2\le2b_KA_{K,q},             \tag{4A.3}
\]

and

\[
                              \sum_KA_{K,q}\le W.     \tag{4A.4}
\]

The paired upper-depth effect is determined by complementation: the
complement of a length-`m-q` cyclic interval is the corresponding
length-`m+1+q` interval.  Hence upper action, variance, and protected-mass
certificates are the coordinate-complements of the lower ones and require
no second choice vector.

### Theorem 4A.1 (safe fractional mean gives an exact bulk child)

Choose the component states independently with
`P(x_K=1)=t_K`.  Suppose the resulting mean satisfies

\[
                         \overline\mu_q(S)\le p-\gamma_q(S)       \tag{4A.5}
\]

for positive margins `gamma_q(S)`.  For nonnegative depth weights
`omega_q`, some exact integral port-legal child obeys

\[
 \boxed{
 \sum_q\omega_qK_p(\mu_q)
 \le\sum_{q,S}{\omega_qV_q(S)\over4\gamma_q(S)},}    \tag{4A.6}
\]

where

\[
 V_q(S)=\sum_Kt_K(1-t_K)
                   (v_{K,q}(S)-u_{K,q}(S))^2.         \tag{4A.7}
\]

If `gamma_q(S)>=alpha_q p` and `b_K<=b_max`, then

\[
 \boxed{
 \sum_q\omega_qK_p(\mu_q)
 \le {b_{\max}W\over8p}
             \sum_q{\omega_q\over\alpha_q}.}         \tag{4A.8}
\]

#### Proof

For a centered scalar fluctuation `Y` and `gamma>0`,

\[
                         (Y-\gamma)_+\le {Y^2\over4\gamma}.       \tag{4A.9}
\]

Apply this coordinatewise to
`mu_q-overline(mu_q)` and take expectations.  Independence gives (4A.7),
so the expected cap tail is at most the right side of (4A.6); one integral
outcome is no worse.  Moreover `t(1-t)<=1/4`, and (4A.3)--(4A.4) give

\[
 \sum_SV_q(S)
 \le{1\over4}\sum_K\|v_{K,q}-u_{K,q}\|_2^2
 \le{b_{\max}\over2}\sum_KA_{K,q}
 \le{b_{\max}W\over2}.                               \tag{4A.10}
\]

Substitution proves (4A.8). \(\square\)

Thus a positive bulk theorem really follows from a safe fractional mean
and small port-closed action variance.  If the margins are uniformly
proportional and
`sum_q omega_q/alpha_q=O(sqrt(p))` (in particular, bounded weights over
`H=O(sqrt(p))` depths), the sufficient component scale is
`b_max=o(sqrt(p))`.  Near a floor hinge where `gamma=O(1)`, this generic
variance argument is not enough.  One then needs additional structure,
for example a directed exact hinge sign or a genuinely correlated
discrepancy theorem; the protected-mass dual below is the corresponding
exact obstruction test.

There is an exact obstruction dual with no probabilistic loss.  Put

\[
 \Phi_{\rm frac}=min_{0\le x_K\le1}
       \sum_q\omega_qK_p(\mu_q(x)).                  \tag{4A.11}
\]

### Theorem 4A.2 (protected-mass hinge dual)

\[
\boxed{
\begin{aligned}
 \Phi_{\rm frac}
 =\max_{0\le z_q(S)\le\omega_q}\Bigg\{&
 \sum_{q,S}z_q(S)(\lambda_q(S)-p)\\
 &+\sum_K\min\bigl(
       \langle z,u_K\rangle,
       \langle z,v_K\rangle\bigr)\Bigg\}.
\end{aligned}}                                        \tag{4A.12}
\]

Every integral hybrid has cap objective at least (4A.12).

#### Proof

Use

\[
 \omega_q(\mu_q(S)-p)_+
 =\max_{0\le z_q(S)\le\omega_q}
                    z_q(S)(\mu_q(S)-p).               \tag{4A.13}
\]

The domains are compact convex and the resulting expression is bilinear in
`x,z`, so minimax interchanges minimum and maximum.  For fixed `z`, each
`x_K` independently selects the smaller of its two shore pairings, giving
the last sum in (4A.12). \(\square\)

For one target family `A`, the elementary specialization is exact:

\[
 \min_{\text{hybrids}}\mu_q(A)
 =\lambda_q(A)+\sum_K
               \min\{u_{K,q}(A),v_{K,q}(A)\}.         \tag{4A.14}
\]

Therefore every hybrid obeys

\[
 \sum_{S\in A}(\mu_q(S)-p)_+
 \ge\left[
 \lambda_q(A)+\sum_K\min\{u_{K,q}(A),v_{K,q}(A)\}
                         -p|A|\right]_+.              \tag{4A.15}
\]

Taking `A` to be a union of target orbits or a protected shadow fibre gives
a statewise no-go certificate.  Port closure can only strengthen this
simple certificate, because merging components replaces a sum of minima by
the minimum of two sums.  A connected port-closed overlay leaves only the
two endpoint factors.

More quantitatively, suppose one component contains all but `rho` wreath
rows per shore.  Every hybrid agrees on that component with one of the two
seeds and differs from that seed on at most `rho` rows.  At each depth,

\[
 \min_{E\in\{F,G\}}\|\mu_q^{\rm hybrid}-\mu_q^E\|_\infty\le\rho,
 \qquad
 \min_{E\in\{F,G\}}{1\over2}
       \|\mu_q^{\rm hybrid}-\mu_q^E\|_1\le(2m+1)\rho. \tag{4A.16}
\]

Consequently

\[
 K_p(\mu_q^{\rm hybrid})
 \ge\min\{K_p(\mu_q^F),K_p(\mu_q^G)\}-(2m+1)\rho.    \tag{4A.17}
\]

Thus an almost-connected overlay cannot conceal a radically better third
state unless its exceptional row set is already large on the scale of the
required cap correction.

## 5. Carrier locality gives a statewise action ceiling

Call the pair `b`-carrier-local if, after insertion in every common row
context, the two cyclic coordinate words with the same root agree outside
one common contiguous block of `b` positions and use the same coordinate
set inside that block.  A size-`r` one-hole substitution is
`b=2r+1` carrier-local; wrapping may reverse the block but does not make it
noncontiguous.

### Lemma 5.1 (two-boundary interval count)

For one pair of `b`-carrier-local cyclic rows and one fixed interval length,
at most `2b` cyclic intervals have different target sets.

#### Proof

A cyclic interval has two boundary cuts.  If neither cut lies inside the
carrier block, the interval contains either all carrier coordinates or none
of them.  Its target set is then unchanged because the outside order and
the carrier coordinate set agree.  Each boundary can lie in the block for
at most `b` starts. \(\square\)

### Theorem 5.2 (statewise local-trade obstruction)

Let `F'` be any component signing between the two lifted seeds.  For every
depth set `Q`,

\[
 \boxed{
 \sum_{q\in Q}{1\over2}\|\mu_q^{F'}-\mu_q^{\widehat F}\|_1
 \le2b|Q|C_m={2b|Q|\over2m+1}W.}                     \tag{5.1}
\]

If `Pi_q` is any partition of the depth-`q` targets into orbit classes,
then the same bound holds after replacing each load vector by its orbit-mass
push-forward.  Moreover, for `K_p` from (4A.0) and any factor-independent
floor subtraction `d_q`,

\[
\begin{aligned}
 &\left|\sum_{q\in Q}(K_p(\mu_q^{F'})-d_q)_+
 -\sum_{q\in Q}(K_p(\mu_q^{\widehat F})-d_q)_+\right|\\
 &\hspace{45mm}\le {2b|Q|\over2m+1}W.                \tag{5.3}
\end{aligned}
\]

#### Proof

The common root-port edge puts the same root labels on the two shores of
each component.  Hence a mixed child is compared row by row with
`widehat F`.  Lemma 5.1 bounds the number of changed occurrences by `2b`
per row and depth.  A changed occurrence contributes at most two to the
histogram `l_1` difference, proving (5.1) after summing the `C_m` rows.

Summing coordinates inside orbit classes is an `l_1` contraction.  Finally,
the two load vectors have equal total mass.  Therefore

\[
                         |K_p(x)-K_p(y)|
                         \le{1\over2}\|x-y\|_1.       \tag{5.4}
\]

The outer positive part is one-Lipschitz, so (5.3) follows. \(\square\)

### Corollary 5.3 (subcritical growing scale is closed)

If `|Q|=H` and `bH=o(m)`, every state in the full unrelated-seed switching
cube changes the aggregate shadow/orbit/cap ledger by `o(W)`.  It cannot
remove an `Omega(W)` defect.

For one-hole size `r`, this condition is

\[
                              rH=o(m).                 \tag{5.5}
\]

At `H=Theta(sqrt(m))`, all `r=o(sqrt(m))` local two-seed trades are
therefore statewise insufficient.  This conclusion uses neither endpoint
energy equality nor a coordinate-conjugacy invariant.

## 6. A concrete growing pair with five-row orbit-changing components

The abstract bulk theorem has a literal unrelated pair at every growing
root scale.  Let

\[
\begin{aligned}
 T_1&=111000,&T_2&=110100,&T_3&=110010,\\
 T_4&=101010,&T_5&=101100
\end{aligned}                                          \tag{6.1}
\]

be the five `D_3` roots.  Start with the rooted pentagon packet on these
five rows, suspend it once by `J(x)=1x0`, and then right-concatenate a
fixed `B in D_(r-4)`.  Its five size-`r` roots are

\[
                         1T_i0B,\qquad1\le i\le5.      \tag{6.2}
\]

The rooted context theorem preserves the complete `X/Y` ledgers and every
row endpoint.  Distinct suffixes `B` give disjoint root sets and disjoint
owned token packets.  Hence all `C_(r-4)` packets may be installed
simultaneously in the canonical size-`r` factor.

### Theorem 6.1 (explicit non-row-power bulk trade)

For every `r>=4`, there are two exact rooted `D_r`-port factors
`P_r^-,P_r^+` whose direct port-closed overlay has

\[
                              C_{r-4}                  \tag{6.3}
\]

nontrivial components of size five per shore; all other components are
diagonal singletons.  Every five-row component is independently
switchable and changes a fixed `H_r=Aut(D_r)`-invariant orbit census.

More precisely, suppress the two fixed suspension coordinates and the
common suffix carrier in the first unequal wrapped lower-state column.
The old and new palettes are

\[
 \{23,24,12,13,14\},
 \qquad
 \{23,12,15,35,13\}.                                  \tag{6.4}
\]

The three relevant `H_r`-invariant pair-support classes are:

* one coordinate from the first local pair and one from the second;
* one from the first pair and one from the third; and
* one from the second pair and one from the third.

On these classes, (6.4) has signed census

\[
                              \boxed{(-2,+1,+1)}       \tag{6.5}
\]

per suffix `B`.  Consequently the total orbit-family transfer is

\[
                 (-2C_{r-4},C_{r-4},C_{r-4}),         \tag{6.6}
\]

with `l_1` mass `4C_(r-4)=(1/64+o(1))C_r`.

The same component has the marked two-state intersection profile

\[
                  \Delta_{\rm pent}=2e_3+e_5-e_4-2e_2.            \tag{6.7}
\]

The suffix is a fixed spectator, so distinct `B` label disjoint physical
fibres.  Thus the bank has literal marked-shadow `l_1` action

\[
                 6C_{r-4}=\left({3\over128}+o(1)\right)C_r.       \tag{6.8}
\]

There is also a complete, unmarked cyclic depth-one effect.  Let `a,b` be
the two suspension coordinates and `star` the local infinity coordinate.
Suppressing the common suffix, direct intersection of all changed adjacent
windows gives

\[
\begin{aligned}
 \Delta_A={}&
 (e_{a15}+e_{a35}-e_{a24}-e_{a14})\\
 &+(e_{b24}+e_{b26}-e_{b35}-e_{b36})\\
 &+(e_{ab3}+e_{ab4}-e_{ab5}-e_{ab2}),\\
 \Delta_C={}&e_{\star36}+e_{\star25}+e_{\star14}
              -e_{\star34}-e_{\star26}-e_{\star15}.
\end{aligned}                                          \tag{6.8a}
\]

All displayed targets are distinct, so

\[
 \|\Delta_A+\Delta_C\|_1=18.                         \tag{6.8b}
\]

Appending `B` sends the `A` targets injectively to `A union B` and the
`C` targets to `C union (L setminus B)`; `star` separates the two groups.
Consequently

\[
 \boxed{
 \|\mu_1(P_r^+)-\mu_1(P_r^-)\|_1=18C_{r-4}.}         \tag{6.8c}
\]

The full `H_r`-orbit-mass projection of this complete profile has
`l_1` norm `16C_(r-4)`.  Hence both a literal complete shadow histogram
and a genuine coordinate-orbit mass change, not merely a marked phase
palette, are present.

Relative to the full cyclic depth-one occurrence mass
`(2r+1)C_r`, these effects have densities

\[
 {18C_{r-4}\over(2r+1)C_r}\sim {9\over256r},
 \qquad
 {16C_{r-4}\over(2r+1)C_r}\sim {1\over32r}.          \tag{6.8d}
\]

They therefore vanish as fractions of all cyclic occurrences even though
the independently switchable row bank has positive density.

#### Proof

Aggregate exactness and rowwise ports follow from suspension and right
concatenation in the rooted context functor.  The original pentagon owner
routing contains a five-cycle.  Suspension exchanges its internal `X/Y`
roles but retains that five-cycle in the wrapped owned-token overlay, so
the five rows form one connected component.  No token edge can leave its
fixed suffix packet, proving independent legality.

After suppressing `{a,b}` and the suffix, the first two internal wrapped
lower states on the five rows are

\[
\begin{array}{c|ccccc}
-&(23,25)&(24,34)&(12,26)&(13,16)&(14,15)\\
+&(23,34)&(12,16)&(15,14)&(35,25)&(13,36).
\end{array}                                             \tag{6.12}
\]

Their intersections are respectively

\[
                         (2,4,2,1,1),
 \qquad                 (3,1,1,5,3),                 \tag{6.13}
\]

which proves (6.7).  For the complete cyclic depth-one profile, the changed
windows are the four adjacent intersections of wrapped lower states and the
three adjacent intersections of the complementary `star` states.  The two
joining windows are fixed by the common endpoint colours.  Taking the seven
differences gives exactly (6.8a).  Its eighteen displayed signed units are
on distinct targets.  Right concatenation is injective on both target
types, proving (6.8b)--(6.8c).

Under `H_r`, the six active local coordinates split into three fixed
two-coordinate blocks.  In (6.4), the old palette has four members of the
first cross-pair class and one full-pair member `12`; the new palette has
two members of that first cross class, one member in each of the other two
cross classes, and the same full-pair member.  This proves (6.5).  Summing
over suffixes proves (6.6).  Applying the same pair-occupancy classification
to the four separated outer-coordinate groups in (6.8a) gives orbit
`l_1` mass sixteen per suffix.  For `r>4`, let `c` be the first suffix
coordinate.  The ambient pair group pairs `b` with `c`, and every Dyck
suffix contains `c`.  The `a`-, `b`-, `ab`-, and `star`-groups therefore
have distinct invariant signatures: `a/star` presence together with
occupancies `1,2,2,0` in `{b,c}`.  They cannot merge under orbit projection.
Suffixes in one orbit contribute identical signed local-class vectors, so
suffix-orbit collisions add rather than cancel.  Each group contributes
orbit `l_1` mass four, giving sixteen in total.  The case `r=4` is the same
finite table before adjoining `c`.  This completes the proof. \(\square\)

The two factors cannot be related by a port-preserving coordinate
relabeling: every such relabeling lies in `H_r` and preserves the census in
(6.5).  Thus Theorem 6.1 is a genuine two-seed/non-row-power escape.

Its component second moment is explicitly

\[
 \boxed{
 \chi_r={C_r-5C_{r-4}+25C_{r-4}\over C_r}
       =1+20{C_{r-4}\over C_r}\longrightarrow{69\over64}.}       \tag{6.9}
\]

This gives a positive-density row bank, bounded component size, and genuine
orbit/shadow motion at every growing `r`; the full-occurrence action density
is only `Theta(1/r)` by (6.8d).  It is not yet a cap theorem.  The marked
profile (6.7) is boundary-resolved and cannot be hinged alone; the complete
profile (6.8a) has a certified nonzero sign vector but still needs the
actual canonical background and cross-context collision ledger.

Most importantly, the actual changed carrier is only the once-suspended
size-three core: `b=9`, independent of `r`.  Right concatenation makes the
root scale grow but does not make the trade nonlocal.  Theorem 5.2 therefore
bounds every component signing in its strict one-hole/first-fringe lift
over `H=O(sqrt(m))` depths by `o(W)`.

There are two different ambient deployments, and they must not be
conflated.  The disjoint first-fringe deployment of Theorem 2.1 has exactly

\[
                         P_{m,r}C_{r-4}               \tag{6.9a}
\]

independently switchable five-row components.  Since each local component
has intrinsic complete depth-one `l_1` variation eighteen, the exact sum
of its **tagged local** half-`l_1` budgets is

\[
                    9P_{m,r}C_{r-4}=O(C_m)=O(W/m).   \tag{6.9b}
\]

This is not asserted to equal a global physical-depth action: lifting
through an arbitrary first-fringe context introduces collars and can merge
physical targets.  The occurrence-resolved context ledger is required for
that equality.  Formula (6.9b) is an exact intrinsic/tagged packet budget.

By contrast, the full aligned size-`r` carrier atlas contains
`H_(m,r)C_(r-4)` component appearances, where

\[
                         H_{m,r}={1\over2}
                                  \binom{2(m-r)}{m-r}.             \tag{6.9c}
\]

Since

\[
                         {H_{m,r}C_r\over W}=\Theta(r^{-3/2})    \tag{6.10}
\]

uniformly on bounded Gaussian scales `r=O(sqrt(m))`, the raw sum of the
single-appearance complete `l_1` variations is

\[
                    18H_{m,r}C_{r-4}=\Theta(Wr^{-3/2})=o(W).     \tag{6.11}
\]

This atlas sum is not an independently switchable global overlay: aligned
occurrences overlap in rows, and indeed its displayed number can exceed
`C_m`.  Equation (6.11) is therefore only an occurrence-atlas
triangle-inequality quantity, not an exact component count or a coherent
deployment theorem.  The exact disjoint deployment is (6.9a)--(6.9b).
A constant-one use therefore needs a coherent nonlocal amplification, not
merely more suffix copies of this packet.

### Theorem 6.2 (dense tensorization destroys fragmentation)

There is a canonical way to amplify the same packet to constant
occurrence-resolved density, but it makes the overlay components
exponentially large.

Let

\[
                         \mathcal E=\{1T_i0:1\le i\le5\}          \tag{6.12a}
\]

be the five suspended size-four shapes.  In a size-`r` tree, mark every
fringe root whose size-four filling lies in `E`.  Equal-size fringe
subtrees are disjoint.  Replacing one marked filling by another member of
`E` neither moves any marked root nor creates a new size-four root.
Collapsing all marked roots therefore partitions `D_r` into skeleton
classes of size

\[
                              5^k,                     \tag{6.12b}
\]

where `k` is the number of marked slots in that skeleton.

Install the old suspended pentagon at every slot on one shore and the new
one at every slot on the other.  Apply the unary rooted-context theorem
successively to the disjoint holes.  Each step preserves the remaining
equal-size holes, so induction gives two literal exact port factors; the
substitutions commute because their row intervals and token ledgers are
disjoint.  The two shores of each skeleton class own the same aggregate
token ledger, so uniqueness of ownership prevents any overlay edge from
leaving that class.  In a `k`-slot class, root
tokens give the identity row matching and the wrapped pentagon token in
slot `h` gives the coordinate-`h` five-cycle.  These cycles generate the
full Cartesian product, so the entire `5^k` rows form one connected overlay
component.

The total number of marked-slot occurrences over all `D_r` roots is

\[
 \sum_{T\in D_r}k(T)
 =5[z^{r-4}](1-4z)^{-1/2}
 =5\binom{2r-8}{r-4}.                                 \tag{6.12c}
\]

Hence, for a uniform Catalan root,

\[
                         \mathbb E k
 =\left({5\over256}+o(1)\right)r.                    \tag{6.12d}
\]

The size-biased component moment is

\[
 \chi_r=\mathbb E(5^k)
 \ge5^{\mathbb E k}
 =5^{(5/256+o(1))r}.                                  \tag{6.12e}
\]

On the other hand, a `k`-slot class contains `k5^(k-1)` one-slot packets
after the other fillings are fixed.  Therefore its total tagged complete
depth-one `l_1` variation, summed over all skeletons, is

\[
 \mathcal L^{\rm tag}_1
 =18\binom{2r-8}{r-4},                                \tag{6.12f}
\]

and

\[
 {\mathcal L^{\rm tag}_1\over(2r+1)C_r}
 \longrightarrow {9\over256}.                        \tag{6.12g}
\]

Its half-`l_1` action density is consequently `9/512+o(1)`.  Thus this
canonical flip-every-slot tensor amplification reaches constant
occurrence-resolved action density only by making the component second
moment exponential in `r`.  Physical target aggregation can still cancel
some tagged action, so this is an exact action--fragmentation obstruction
for this tensorization, not a cap lower bound or a universal obstruction to
every possible correlated amplification of a bounded packet.

## 6B. The audited `D_4` bank is bulk in rows but subcritical in action

For the canonical/noncanonical `D_4` pair, the direct local ownership
overlay is connected on all fourteen roots.  Thus its local component
parameter is

\[
                              \chi_4=14.               \tag{6B.1}
\]

The first-size-four fringe construction gives

\[
 P_{m,4}={C_m-a_{m,4}\over14}
                    =\left({1\over14}+o(1)\right)C_m \tag{6B.2}
\]

independently switchable fourteen-row components.  Its carrier profiles at
local lengths two and three are nonzero, with positive masses nineteen and
twenty-two.  Hence these are genuine shadow-changing, non-relabeling
trades.

But the carrier block has `b=9`.  Theorem 5.2 gives, for `H<=A sqrt(m)`,

\[
 \sum_{q\le H}{1\over2}\|\mu_q^{F'}-\mu_q^{F}\|_1
 \le {18H\over2m+1}W
 =O_A\!\left({W\over\sqrt m}\right)=o(W).             \tag{6B.3}
\]

Thus neither the full fourteen-row `F/G` atom nor the smaller exact `F/H`
components can close the constant-one gate through strict fringe
deployment.  Their local orbit changes are real; their total physical
action is too small.

## 7. Exact surviving scale

Theorems 2.1 and 3.1 show that packet supply is not the obstruction at
`r=Theta(sqrt(m))`: almost every Catalan row still belongs to a growing
fringe packet.  Theorem 5.2 shows simultaneously that this is the first
scale where a one-hole carrier can have `Theta(W)` aggregate action over a
Gaussian window.

A viable critical pair must therefore satisfy all of the following.

1. `F_r,G_r` are genuinely unrelated rooted exact factors at
   `r=Omega(sqrt(m))`, not coordinate relabellings.  The order
   `Theta(sqrt(m))` is the minimal critical scale; the present argument
   does not exclude larger `r`.
2. Their local overlay has bounded size-biased component moment, or an
   affine discrepancy theorem strong enough to replace it.
3. Their rowwise difference has active carrier width
   `b=Omega(sqrt(m))`.  At the minimal scale `r=Theta(sqrt(m))` this is
   `Theta(r)` activity; for larger `r`, Theorem 5.2 does not require
   `Theta(r)`.  An outer hole with `b=o(sqrt(m))` remains subject to (5.5)
   and (6B.3).
4. Its occurrence-resolved carrier profiles support either a favourable
   directed cap sign after all collars/backgrounds are included, or a
   correlated multicomponent selection theorem which succeeds despite
   mixed state-dependent signs.
5. Every such route must make the exact fractional protected-mass dual in
   Theorem 4A.2 `o(W)` on the controlled ledger.  The safe-mean variance
   theorem 4A.1 is one sufficient way to do this, not a necessary one.

The present theorem proves exact integrality, bulk packet coverage, and the
exact subcritical no-go.  It does not construct the critical root-scale
pair, so no coefficient-one conclusion is claimed.
