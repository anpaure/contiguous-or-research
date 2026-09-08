# Growing `D_s` port factors: exact carrier inequalities and Catalan first-edge balance

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let $F_s$ be the canonical anchored $D_s$ port factor and let $G_s$ be
any other anchored exact factor with the same row endpoints and complete
$X/Y$ ownership ledgers.  Then $F_s\rightsquigarrow G_s$ is legal in
every common aligned port context.  Exact legality is not the remaining
issue.

For every affected ancestor depth $q$, retain the row- and start-resolved
carrier maps and let $D_q$ be the resulting physical new-minus-old target
histogram.  If $u_q$ is the old affected histogram and

\[
                         c_q(T)=(p-\beta_q(T))_+
\tag{0.1}
\]

is the capacity left by the unaffected background, define

\[
\begin{aligned}
 R_q&=\sum_{D_q(T)<0}
   \min\{-D_q(T),(u_q(T)-c_q(T))_+\},\\
 A_q&=\sum_{D_q(T)>0}
   \min\{D_q(T),(u_q(T)+D_q(T)-c_q(T))_+\}.
\end{aligned}
\tag{0.2}
\]

These are, respectively, the old excess actually removed and the new
excess actually created.  They give the exact cap derivative

\[
                    K_p(\beta_q+u_q+D_q)
                    -K_p(\beta_q+u_q)=A_q-R_q.
\tag{0.3}
\]

Put

\[
 W=\binom{2m+1}{m},\qquad N_q=\binom{2m+1}{m-q},
\]

and

\[
 z_q=K_p(\beta_q+u_q)-(W-N_q).
\tag{0.4}
\]

One common integral factor choice reduces multidepth PCap if and only if

\[
 \boxed{
 \sum_q(z_q)_+>
 \sum_q(z_q+A_q-R_q)_+.}
\tag{0.5}
\]

This is the necessary and sufficient carrier inequality.  It includes all
crossing collars, target collisions, inactive PCap floors, and the fact
that the same $G_s$ must serve every depth.

For several phase-disjoint substitutions, first sum their physical
histograms into $D_q$ and use the same formula.  Overlapping or nested
substitutions must be treated as one joint atom before $D_q$ is formed;
separate marginal inequalities are not necessary and sufficient after
their targets collide.

At the distinguished first-insertion boundary, let

\[
 h_H(x)=\#\{P\in D_s:b_1^H(P)=x\},\qquad H\in\{F_s,G_s\}.
\tag{0.6}
\]

The exact canonical statistics are

\[
 \boxed{
 h_{F_s}(2j)=w_j:=\operatorname {Cat}_{j-1}
                     \operatorname {Cat}_{s-j},qquad
 h_{F_s}(2j-1)=0,\quad1\le j\le s.}
\tag{0.7}
\]

The opposite boundary has the same $w_j$ on the odd coordinates.  Under
a transparent ancestor carrier these Catalan terms are unchanged at every
depth; only the exterior core changes.

All balance statements below must also be imposed on the last-deletion
histogram

\[
 \bar h_H(x)=\#\{P\in D_s:a_s^H(P)=x\}
\]

for the opposite boundary.  If the two boundary images collide
physically, their signed histograms must be added before any hinge test.

For one first-edge carrier with multiplicity scale $M_q$, put
$c_{q,x}=c_q(K_q\cup\{\iota(x)\})$ and put
$f_{q,x}=M_qh_{F_s}(x)$, $g_{q,x}=M_qh_{G_s}(x)$.  Every coordinate has a
weakly favourable sign—no addition creates overload—if and only if

\[
 \boxed{
 g_{q,x}>f_{q,x}\quad\Longrightarrow\quad
                         g_{q,x}\le c_{q,x}.}
\tag{0.8}
\]

Every transported unit is fully efficient if and only if

\[
 \boxed{
 g_{q,x}\in
 [\min\{f_{q,x},c_{q,x}\},
  \max\{f_{q,x},c_{q,x}\}]
       \quad\text{for every }q,x.}
\tag{0.9}
\]

Thus a single statistic can be fully favourable on a hereditary chain
exactly when it lies in the intersection of the intervals in (0.9).  If
two ancestors put $c_{q,x}$ on opposite sides of $f_{q,x}$, that
intersection is the singleton $\{f_{q,x}\}$: no nontrivial coherent move
at coordinate $x$ is possible.

A simple strong balance condition is

\[
                         M_qh_{G_s}(x)\le c_{q,x}
                         \qquad\text{for every }q,x.
\tag{0.10}
\]

It makes the new first-edge defect zero on every carrier.  The exact
canonical defect removed at depth $q$ is then

\[
 \boxed{
 E^{\rm edge}_{q}(F_s)
 =\sum_{j=1}^s(M_qw_j-c_{q,2j})_+.}
\tag{0.11}
\]

At zero additional background and $M_q=1$, this is

\[
                         \sum_{j=1}^s(w_j-p)_+.
\tag{0.12}
\]

For the fatal child scale $r=s-1$, write

\[
              \theta={\operatorname {Cat}_{s-1}\over p},
              \qquad4\le\theta<16.
\tag{0.13}
\]

The exact saturation threshold of the $j$th Catalan boundary class is

\[
 \boxed{
 \Theta_j(s)={\operatorname {Cat}_{s-1}\over
        \operatorname {Cat}_{j-1}\operatorname {Cat}_{s-j}},
 \qquad
 w_j>p\iff\theta>\Theta_j(s).}
\tag{0.14}
\]

For fixed $j$,

\[
                         \Theta_j(s)\longrightarrow
                         {4^{j-1}\over\operatorname {Cat}_{j-1}}.
\tag{0.15}
\]

Hence the limiting thresholds from either end are

\[
                         1,\quad4,\quad8,\quad{64\over5},
                         \quad{256\over14}>16.
\tag{0.16}
\]

Only the first four classes from each end can be saturated in the whole
fatal range.  A genuinely balanced first-edge histogram, for example

\[
                         h_{G_s}(x)={\operatorname {Cat}_s\over2s}+O(1),
\tag{0.17}
\]

is $o(p)$ per coordinate because
$\operatorname {Cat}_s<64p$ and $s\to\infty$.  Subject to root-incidence
and full-factor realizability, it would place the first-edge mass inside
all carriers having residual margin $p-o(p)$ and remove the complete
Catalan defect (0.12).

Two qualifications are sharp.

1. No nonzero first-edge difference is favourable for every conceivable
   carrier background.  An adversary can saturate its positive support
   and empty its negative support.  Universal background-independent sign
   forces the difference to be zero.
2. First-edge balance controls only one boundary column.  Constant one
   requires (0.5) for the full row/start tensor.  The other
   $2(s-1)-1$ affected starts at the matched child depth, and all
   off-matched prefix/suffix profiles, can reverse the sign.  No marginal
   first-edge statistic implies their inequalities.

Thus the exact open construction problem is a growing anchored
$D_s$-factor whose full carrier tensor satisfies (0.5), with first-edge
statistics satisfying the capacity balance (0.8) or, ideally, (0.10).

## 1. The growing anchored factor and its positional tensor

For $P\in D_s$, write the oriented local geodesic as

\[
 X_t^H(P)=
 (P\setminus\{a_1^H,\ldots,a_t^H\})
 \cup\{b_1^H,\ldots,b_t^H\},qquad0\le t\le s,
\tag{1.1}
\]

and define its coordinate word

\[
 q_H(P)=(a_1^H,\ldots,a_s^H,
         b_1^H,\ldots,b_s^H,\infty).
\tag{1.2}
\]

Anchoring means

\[
                         X_0^H(P)=P,qquad
                         X_s^H(P)=[2s]\setminus P.
\tag{1.3}
\]

The complete state and adjacent-union ledgers are

\[
 \biguplus_{P,t}\{X_t^H(P)\}=\binom{[2s]}s,
 \qquad
 \biguplus_{P,t<s}\{X_t^H(P)\cup X_{t+1}^H(P)\}
                         =\binom{[2s]}{s+1}.
\tag{1.4}
\]

Equations (1.3)--(1.4) are exactly the aligned substitution interface.
They prove contextual legality for $G_s$ independently of its target
profile.

For any local position set $A\subseteq\mathbb Z_{2s+1}$, put

\[
 d_{P,A}=
 e_{\{q_{G_s}(P)_i:i\in A\}}
 -e_{\{q_{F_s}(P)_i:i\in A\}}.
\tag{1.5}
\]

An affected ancestor occurrence

\[
                         \omega=(C,q,k,P,A)
\tag{1.6}
\]

has exterior carrier $O_\omega$ and inherited injection $\iota_\omega$.
Its exact physical push-forward is

\[
 \boxed{
 \Phi_\omega(e_S)=e_{O_\omega\cup\iota_\omega(S)},
 \qquad
 D_q=\sum_{\omega\in\mathcal A_q}\Phi_\omega d_{P,A}.}
\tag{1.7}
\]

Formula (1.7) is valid with arbitrary row/start-dependent carriers.  One
may sum over rows before applying a carrier only when all terms being
summed have exactly the same $O_\omega$ and $\iota_\omega$.

If an ancestor window contains the whole local geodesic, then its local
intersection contains both $P$ and $P^c$ and is empty.  In that case
$\Phi_\omega$ collapses both shores to the same exterior target and the
row atom vanishes.  Nonzero hereditary action therefore requires a
boundary/frontier occurrence.

## 2. Exact cap derivative on one carrier tensor

Fix one depth $q$.  Remove the old affected slots from the ambient load
and call the remainder $\beta_q$.  Let $u_q$ be the old histogram put
back by $F_s$.  Then

\[
                         \mu_q^{F_s}=\beta_q+u_q,
 \qquad
                         \mu_q^{G_s}=\beta_q+u_q+D_q.
\tag{2.1}
\]

The scalar identity

\[
 (\beta+u-p)_+=(\beta-p)_+
                  +(u-(p-\beta)_+)_+
\tag{2.2}
\]

gives

\[
 K_p(\mu_q^{G_s})-K_p(\mu_q^{F_s})
 =\sum_T\left[(u_q(T)+D_q(T)-c_q(T))_+
                    -(u_q(T)-c_q(T))_+\right].
\tag{2.3}
\]

If $D_q(T)=-d<0$, its summand is

\[
                         -\min\{d,(u_q(T)-c_q(T))_+\};
\tag{2.4}
\]

if $D_q(T)=d>0$, its summand is

\[
                         \min\{d,(u_q(T)+d-c_q(T))_+\}.
\tag{2.5}
\]

Summing (2.4)--(2.5) proves (0.2)--(0.3).

### Theorem 2.1 (necessary and sufficient multidepth carrier test)

For one common integral choice $G_s$ across a protected depth set
$\mathcal Q$, define $R_q,A_q,z_q$ by (0.2) and (0.4).  Then

\[
 \operatorname {PCap}_{\mathcal Q}(G_s)
 -\operatorname {PCap}_{\mathcal Q}(F_s)
 =\sum_{q\in\mathcal Q}
       \left[(z_q+A_q-R_q)_+-(z_q)_+\right].
\tag{2.6}
\]

Consequently strict reduction is equivalent to (0.5).

If $R_q\ge A_q$ at every depth, the exact gain is

\[
 \boxed{
 \sum_{q\in\mathcal Q}
   \min\{R_q-A_q,(z_q)_+\}.}
\tag{2.7}
\]

In particular, a cap-tail improvement at a depth whose PCap floor is
inactive gives no PCap gain.

#### Proof

Equation (0.3) changes the pre-floor cap tail by $A_q-R_q$.  Subtract
$W-N_q$, take a positive part, and sum, proving (2.6).  This gives the
if-and-only-if statement.  When $R_q\ge A_q$, use

\[
                         x_+-(x-d)_+=\min\{d,x_+\}
\]

with $d=R_q-A_q$ to obtain (2.7).  \(\square\)

## 3. Coordinatewise sign conditions

The exact test (0.5) allows favourable and unfavourable carriers to trade
against one another.  A stronger pointwise condition prevents every
unfavourable term.

### Proposition 3.1 (weak and fully efficient carrier signs)

At a fixed depth and target, put $f=u_q(T)$,
$g=u_q(T)+D_q(T)$, and $c=c_q(T)$.

1. The coordinate contributes no positive cap change if and only if

   \[
   g>f\quad\Longrightarrow\quad g\le c.
   \tag{3.1}
   \]

2. Every changed unit is fully efficient—an added unit uses slack and a
   removed unit removes overload—if and only if

   \[
   \boxed{g\in[\min\{f,c\},\max\{f,c\}].}
   \tag{3.2}
   \]

3. The new coordinate has zero residual defect if and only if $g\le c$.

#### Proof

If $g\le f$, monotonicity of the hinge makes its change nonpositive.  If
$g>f$, the hinge is unchanged exactly when both values are at most $c$,
which is equivalent to (3.1).  For full efficiency, addition must stop no
later than $c$ and removal must stop no later than reaching $c$ from
above.  These are precisely the two cases in (3.2).  The last assertion is
the definition of the residual hinge.  \(\square\)

For one common factor choice across depths, (3.2) becomes

\[
 g_{q,T}\in
 \bigcap_{q\in\mathcal Q(T)}
 [\min\{f_{q,T},c_{q,T}\},
  \max\{f_{q,T},c_{q,T}\}],
\tag{3.3}
\]

after identifying the relevant hereditary carrier chain.  In the usual
transparent case the local old/new statistics are depth-independent and
only the exterior target name changes.  If some carrier has $c<f$ and
another has $c>f$, the intervals in (3.3) meet only at $f$.  Therefore
coherent full efficiency forces $g=f$ on that local coordinate.

## 4. The exact Catalan boundary background

At matched child depth $s-1$, the two intrinsic windows of a row have
local targets $a_s(P)$ and $b_1(P)$.  In the canonical factor, first-return
decomposition gives

\[
                         w_j=\operatorname {Cat}_{j-1}
                                  \operatorname {Cat}_{s-j}.
\tag{4.1}
\]

The $b_1$ boundary has $w_j$ rows at target $2j$ and none at target
$2j-1$.  The $a_s$ boundary has $w_j$ rows at target $2j-1$ and none at
$2j$.  Since

\[
                         \sum_{j=1}^sw_j=\operatorname {Cat}_s,
\tag{4.2}
\]

these are the complete first-edge and last-edge histograms.

For a transparent one-sided ancestor chain with exterior core $K_q$, the
physical cells are

\[
                         K_q\cup\{2j\},qquad
                         K_q\cup\{2j-1\},
\tag{4.3}
\]

and the intrinsic multiplicities remain exactly $w_j$ at every depth.
Let $\eta_{q,x}$ be all additional physical load already present on such
a cell.  Its full old loads are therefore

\[
\begin{aligned}
 \lambda^+_{q,2j}&=M_qw_j+\eta_{q,2j},\\
 \lambda^+_{q,2j-1}&=\eta_{q,2j-1}
\end{aligned}
\tag{4.4}
\]

for the first-insertion boundary, with odd/even interchanged on the
opposite boundary.

The exact first-edge old-minus-new gain is

\[
\begin{aligned}
 \mathcal G_q^{\rm edge}
 =\sum_x\bigl[&
 (\eta_{q,x}+M_qh_{F_s}(x)-p)_+\\
 &-(\eta_{q,x}+M_qh_{G_s}(x)-p)_+\bigr].
\end{aligned}
\tag{4.5}
\]

This is the Catalan specialization of (0.2).  It is exact and includes
collisions with other contexts through $\eta$.

### Proposition 4.1 (exact Catalan saturation thresholds)

Put $d=\operatorname {Cat}_{s-1}$ and $\theta=d/p$.  Then

\[
                         {w_j\over p}={\theta\over\Theta_j(s)},
 \qquad
 \Theta_j(s)={d\over w_j}.
\tag{4.6}
\]

For fixed $j$,

\[
                         \Theta_j(s)\to
                         {4^{j-1}\over\operatorname {Cat}_{j-1}}.
\tag{4.7}
\]

Also $w_{s+1-j}=w_j$.  Therefore, uniformly for
$4\le\theta<16$ and large $s$, only the four classes at each end can
exceed $p$.  Their limiting thresholds are (0.16).

#### Proof

Equation (4.6) is algebra.  For fixed $j$,

\[
 {\operatorname {Cat}_{s-j}\over
  \operatorname {Cat}_{s-1}}\longrightarrow4^{-(j-1)},
\]

which proves (4.7).  Symmetry is immediate from (4.1).  Since the fifth
threshold tends to $256/14>16$, all later fixed classes are below cap;
log-convexity and symmetry place the minimum weights toward the centre and
exclude further saturated classes.  \(\square\)

At zero additional background and unit scale, the exact canonical
first-edge cap defect is

\[
 \boxed{
 \mathcal E_s^{\rm can}(p)
   =\sum_{j=1}^s
       (\operatorname {Cat}_{j-1}\operatorname {Cat}_{s-j}-p)_+.}
\tag{4.8}

For fixed overshoot $\theta$ away from the thresholds, its leading form is

\[
 {\mathcal E_s^{\rm can}(p)\over p}
 =2\left[
   (\theta-1)_+
  +\left({\theta\over4}-1\right)_+
  +\left({\theta\over8}-1\right)_+
  +\left({5\theta\over64}-1\right)_+
       \right]+o(1).
\tag{4.9}
\]

## 5. Balanced first-edge statistics

Let $h=h_{G_s}$ be a proposed first-insertion histogram.  Necessarily

\[
                         h(x)\in\mathbb Z_{\ge0},qquad
                         \sum_{x=1}^{2s}h(x)=\operatorname {Cat}_s.
\tag{5.1}
\]

For a hereditary carrier family, define its common available capacity

\[
                         c_*(x)=\min_{q\in\mathcal Q}c_{q,x}.
\tag{5.2}
\]

### Theorem 5.1 (first-edge balance criteria)

For the first-edge sector alone:

1. $h$ has zero new residual defect on every carrier if and only if

   \[
                           M_qh(x)\le c_{q,x}
                           \qquad(q\in\mathcal Q,x\in[2s]).
   \tag{5.3}
   \]

2. In the common-scale case $M_q=M$, an abstract integer histogram with
   zero defect can exist only if

   \[
                           M\operatorname {Cat}_s
                              \le\sum_x c_*(x).
   \tag{5.4}
   \]

   The exact necessary and sufficient condition for an unconstrained
   integer histogram is the stronger floor inequality

   \[
               \operatorname {Cat}_s
                   \le\sum_x\left\lfloor{c_*(x)\over M}\right\rfloor.
   \tag{5.5}
   \]

3. Such a histogram makes every first-edge carrier weakly favourable and
   removes its entire canonical residual defect (0.11).

#### Proof

The new residual defect is

\[
                         \sum_x(M_qh(x)-c_{q,x})_+.
\]

It vanishes exactly under (5.3).  Summing (5.3) gives the necessary
capacity inequality.  Integer boxes of capacities
$\lfloor c_*(x)/M\rfloor$ contain a vector of prescribed total precisely
when their total capacity is at least that total, proving (5.5).  The last
claim follows by subtracting zero new defect from the old defect.  \(\square\)

The unconstrained sufficiency in Theorem 5.1 is not a port-factor
existence theorem.  Since $b_1(P)\in[2s]\setminus P$, even the assignment
of first edges must satisfy the capacitated Hall inequalities

\[
 \boxed{
 |\mathcal R|
 \le\sum_{x\in N(\mathcal R)}
       \left\lfloor{c_*(x)\over M}\right\rfloor
 \quad(\mathcal R\subseteq D_s),
 \qquad
 N(\mathcal R)=\bigcup_{P\in\mathcal R}([2s]\setminus P).}
\tag{5.6}
\]

They are necessary and sufficient for a capacitated first-edge assignment,
but the complete $X/Y$ ledgers impose further path-factor constraints.

The identical assertions hold for the opposite boundary after replacing
$h$ by $\bar h$ and interchanging the odd and even canonical cells.  To
make both boundary arms sign-safe, both capacitated Hall systems must be
satisfied with their actual carrier capacities; common physical targets
must be combined before applying (5.3).

### Corollary 5.2 (asymptotically uniform balance)

At the fatal parent scale,

\[
 \operatorname {Cat}_s
 =\left(4-{6\over s+1}\right)
                     \operatorname {Cat}_{s-1}<64p.
\tag{5.7}
\]

Therefore an abstract almost-uniform histogram satisfies

\[
                         \max_xh(x)\le
                         \left\lceil{32p\over s}\right\rceil.
\tag{5.8}
\]

In a unit-scale carrier family, if every hereditary first-edge carrier has
the exact margin

\[
                         c_{q,x}\ge
                         \left\lceil{\operatorname {Cat}_s\over2s}
                         \right\rceil,
\tag{5.9}
\]

then this statistic is cap-safe at every depth.  It removes the whole
canonical first-edge defect (4.8), subject to realization by an anchored
exact factor.

## 6. Exact PCap gain under balanced first edges

Assume for the moment that all other affected profiles vanish or are
separately cap-neutral, and that (5.3) holds.  Then at depth $q$ the cap
tail falls by exactly

\[
                         D_q^{\rm edge}
 =\sum_x(M_qh_{F_s}(x)-c_{q,x})_+.
\tag{6.1}
\]

With $z_q$ as in (0.4), the exact PCap gain is

\[
 \boxed{
 \sum_{q\in\mathcal Q}
       \min\{D_q^{\rm edge},(z_q)_+\}.}
\tag{6.2}
\]

For a transparent chain of $L$ depths with zero additional background,
unit scale, and active floors of slack at least
$\mathcal E_s^{\rm can}(p)$, this becomes

\[
                         L\,\mathcal E_s^{\rm can}(p),
\tag{6.3}
\]

with the exact Catalan term (4.8).

In the real substitution the other carrier profiles do not vanish.  If
their physical supports are disjoint from the first-edge support, let
$A_q^{\rm coll},R_q^{\rm coll}$ be their created and removed excess.
Only under this disjoint-support hypothesis may one write

\[
 A_q=A_q^{\rm coll},
 \qquad
 R_q=D_q^{\rm edge}+R_q^{\rm coll}.
\tag{6.4}
\]

and the full necessary and sufficient condition becomes

\[
 \sum_q(z_q)_+>
 \sum_q\left(z_q+A_q^{\rm coll}
                    -D_q^{\rm edge}-R_q^{\rm coll}\right)_+.
\tag{6.5}
\]

Without support disjointness, edge and collar coefficients can cancel at
the same physical target before the hinge is applied.  One must first sum
the full $D_q$ in (1.7) and then use (0.2)--(0.5).  Thus even a perfectly
balanced first edge proves PCap descent only when the complete physical
collar tensor passes the exact carrier test.

## 7. Why no first-edge statistic is universally sufficient

### Proposition 7.1 (adversarial carrier obstruction)

Let $d=h_{G_s}-h_{F_s}$ be a nonzero equal-mass first-edge difference.
There are residual backgrounds for which its cap change is positive and
backgrounds for which it is negative.  Hence no nonzero statistic has a
background-independent favourable sign.

#### Proof

Choose a coordinate $x_+$ with $d(x_+)>0$ and one $x_-$ with
$d(x_-)<0$.  Give the positive support zero residual capacity and give the
negative support capacity at least its old load.  Additions then create
overload while removals remove none, so the change is positive.  Reversing
the capacity assignments exposes the negative support and hides the
positive support, giving negative change.  \(\square\)

There is a second obstruction.  A legal $D_s$ replacement changes the
whole positional tensor (1.5), not only $b_1$.  Two exact factors may have
the same first-edge histogram and different collars, or favourable first
edges and unfavourable collars.  Therefore the only necessary and
sufficient factor-level statement is (0.5).  Balanced first-edge
statistics are a quantitatively important boundary condition, not a
replacement for the full carrier audit.
