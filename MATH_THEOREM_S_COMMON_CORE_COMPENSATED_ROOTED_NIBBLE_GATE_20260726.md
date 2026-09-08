# Common-core physical paths: exact repaired-ring normal form and the compensated rooted-nibble gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome and scope

Put

\[
 W=\binom{2m}{m},\qquad
 N=N_H=\binom{2m}{m-H},\qquad
 M=m+H,
\]

\[
 \Lambda=\frac{W}{N},\qquad
 L=m-3H+1,\qquad
 n_0=L+H-1=m-2H.
\tag{0.1}
\]

Assume

\[
 H=(1+o(1))\sqrt{m\log m},\qquad m>5H,
\tag{0.2}
\]

and, for fixed constants \(c_0,C_0>0\),

\[
 L+c_0H\le \Lambda\le m+C_0H.
\tag{0.3}
\]

Define

\[
 \rho=\frac{L}{\Lambda},\qquad
 \delta=1-\rho=\frac{\Lambda-L}{\Lambda}.
\tag{0.4}
\]

Then

\[
 \delta=\Theta(H/m),\qquad
 LN=\rho W=W-o(W).
\tag{0.5}
\]

This report proves the following exact local results.

1. After complementing middle owners, the simple physical common-core
   catalogue is exactly the repaired-ring catalogue with

   \[
   r=L,\qquad k=M-L=4H-1,\qquad u=k-H+1=3H.
   \tag{0.6}
   \]

2. The simple hypergraph has exact root degree, owner degree, and
   distance-\(d\) owner codegrees

   \[
   \boxed{R=\frac{M!}{2(3H)!}},\qquad
   \boxed{D=\rho R=
   \frac{L(m!)^2}{2(m-H)!(3H)!}},
   \tag{0.7}
   \]

   \[
   \boxed{\frac{d(X,Y)}D
   =\frac{2(L-d)}{L\binom md^2}}
   \qquad(1\le d<H),
   \tag{0.8}
   \]

   and

   \[
   \boxed{\frac{d(X,Y)}D
   =\frac{(L-H)(L-H+1)}
          {L\binom mH^2}}
   \qquad(d=H).
   \tag{0.9}
   \]

   The codegree is zero for \(d>H\).

3. The exact path geometry defeats the crude factor-\(L\) union bound.
   For every physical edge \(e\) and every external owner \(X\notin e\),

   \[
   \boxed{
   \frac{a_X(e)}D
   \le
   \frac{6(L-1)}{Lm^2}+O(m^{-4})
   =\frac{6+o(1)}{m^2}.}
   \tag{0.10}
   \]

   The leading constant six is attainable. Thus the distance-one
   consecutive-window spike is real but remains on the \(m^{-2}\)
   influence scale.

4. There is an exact root-preserving compensated proposal lemma. Given a
   probability distribution on the available paths of each root, propose
   at most one path per root, retain only isolated proposals, and thin
   isolated proposals so that every root has exactly the same acceptance
   probability. If every owner has normalized load at most one,
   independent owner waste gives roots and owners the same one-step
   deletion marginal. No root is discarded merely to compensate an
   owner.

5. At time zero, uniform root distributions give every owner load
   exactly \(\rho<1\). If every root proposes with probability
   \(a=\gamma/L\), where \(0<\gamma<1\) is fixed, then every proposed
   path has isolation probability

   \[
   \exp(-\gamma\rho+O(m^{-2})).
   \tag{0.11}
   \]

   One compensated bite therefore accepts

   \[
   \left(e^{-\gamma\rho}+O(m^{-2})\right)
   \frac{\gamma N}{L}
   \tag{0.12}
   \]

   roots in expectation, while preserving the one-choice-per-root
   integrality exactly.

6. Section 6 states a precise conditional dynamic regeneration theorem.
   Its numerical ledger closes down to any

   \[
   z_*=o(1),\qquad z_*\log m\longrightarrow\infty.
   \tag{0.13}
   \]

   Under that condition one obtains one physical path at every root with
   total repeated-middle-owner mass \(o(W)\), and hence middle support
   \(W-o(W)\).

The dynamic regeneration condition is not proved here. Equal one-vertex
survival marginals do not control the joint survival of all
\(L\asymp m\) owners of a path. The exact unresolved invariant is a
rootwise load polytope coupled to a typical upper-link-influence
trajectory. Accordingly, this report is an exact positive reduction,
not a near-perfect matching theorem.

It also does not prove the stronger corrected-annulus requirement that
the selected states fuse into length-\(2m\) cycles or that their signed
traces at every depth are simple. The conclusion of the conditional
theorem is exactly a middle-owner partial design. This scope distinction
is essential.

## 1. Exact physical normal form

Use roots

\[
 \mathcal A=\binom{[2m]}{m-H}.
\]

For \(A\in\mathcal A\), put

\[
 U=[2m]\setminus A,\qquad |U|=M.
\tag{1.1}
\]

A physical common-core middle path is determined by an injective word

\[
 w=(t_1,\ldots,t_{n_0})
\tag{1.2}
\]

in \(U\), up to reversal. Its original middle owners are

\[
 X_j
 =U\setminus\{t_j,t_{j+1},\ldots,t_{j+H-1}\},
 \qquad 1\le j\le L.
\tag{1.3}
\]

Complementing the owners gives

\[
 Y_j=X_j^c
 =A\cup\{t_j,t_{j+1},\ldots,t_{j+H-1}\}.
\tag{1.4}
\]

Complementation is a bijection of the middle layer and preserves
Johnson distance, support size, and collision multiplicity. Hence the
owner set of a physical path is a tight path of \(L\) consecutive
\(H\)-windows over root \(A\).

### Theorem 1.1 (physical catalogue equals the repaired-ring quotient)

The simple unoriented physical path hypergraph is isomorphic to the
repaired-ring hypergraph with parameters (0.6). Every simple physical
edge has exactly

\[
 \boxed{\mu=2(3H)!}
\tag{1.5}
\]

directed cyclic-order/deleted-block representations.

#### Proof

The word exposed by the \(L\) consecutive windows has length

\[
 L+H-1=m-2H=n_0.
\]

There are \(M-n_0=3H\) unused labels. Complete the word to a directed
cyclic order of \(U\). The retained window starts form one cyclic block
of length \(L\), so the deleted start block has length

\[
 k=M-L=4H-1.
\]

The standard repaired-ring unidentified block therefore has size

\[
 u=k-H+1=3H.
\]

Conversely, deleting \(4H-1\) consecutive starts from such a ring
exposes precisely a word of the form (1.2). Once an orientation of the
physical path is chosen, the only invisible datum is the order of the
\(3H\) unused labels. Reversal gives the other orientation. Thus every
simple unoriented physical edge has \(2(3H)!\) representations.
\(\square\)

The common \(2H\)-core is not an additional restriction after taking
this quotient. Given (1.2), choose any \(2H\) of the \(3H\) unused
labels as the core and place the remaining \(H\) unused labels before
the exposed word. This reconstructs a literal core-safe partial
promotion path. Thus every simple edge counted here has a literal local
realization; the quotient merely forgets redundant core and order data.

## 2. Exact degrees and codegrees

### Theorem 2.1 (root and owner degrees)

The degrees are exactly (0.7). Under the uniform distribution on the
simple paths at each root, every owner has total rootwise load
\(\rho=L/\Lambda\).

#### Proof

At one root there are \(M!\) cyclic-order/deleted-block representations:
\((M-1)!\) directed cyclic orders and \(M\) block positions. Dividing by
(1.5) gives

\[
 R=\frac{M!}{2(3H)!}.
\]

Fix a complemented owner \(Y\). Choose a root \(A\subset Y\) in
\(\binom mH\) ways. For fixed \(A\), the residual \(H\)-set
\(Y\setminus A\) may occupy any of the \(L\) window positions. Order it
in \(H!\) ways and fill the other \(n_0-H=L-1\) word positions from the
remaining \(m\) labels. The number of oriented words is

\[
 L H!\frac{m!}{(3H)!}.
\]

Divide by two for reversal and multiply by \(\binom mH\). This gives

\[
 D
 =\binom mH\frac{LH!m!}{2(3H)!}
 =\frac{L(m!)^2}{2(m-H)!(3H)!}.
\]

Finally

\[
 \Lambda=\frac{M!(m-H)!}{(m!)^2},
\]

so \(D/R=L/\Lambda=\rho\). Giving each root path weight \(1/R\)
therefore gives every owner total load \(D/R=\rho\).
\(\square\)

For later use, if \(A\subset Y\), then the root-owner codegree obeys

\[
 \boxed{\frac{d(A,Y)}R=\frac{L}{\binom MH}},
\qquad
 \boxed{\frac{d(A,Y)}D=\frac1{\binom mH}}.
\tag{2.1}
\]

It is zero if \(A\not\subset Y\).

### Theorem 2.2 (exact owner-pair sequence)

Let \(X,Y\) be distinct complemented middle owners and put

\[
 d=d_J(X,Y).
\]

Then (0.8), (0.9), and the zero statement for \(d>H\) hold.

#### Proof

Suppose \(1\le d<H\). A common root \(A\) must be an
\((m-H)\)-subset of \(X\cap Y\), so there are

\[
 \binom{m-d}{H-d}
\]

choices. Relative to a fixed common root, the two residual \(H\)-sets
overlap in \(H-d\) labels. In a common injective word their starts must
differ by \(d\). There are two directions and \(L-d\) placements. The
union of the two windows may be ordered in

\[
 (d!)^2(H-d)!
\]

ways, and the remaining positions may be filled in

\[
 \frac{(m-d)!}{(3H)!}
\]

ways. After dividing by two for reversal, the pair degree is

\[
 d(X,Y)
 =\frac{(L-d)(d!)^2((m-d)!)^2}
        {(m-H)!(3H)!}.
\]

Dividing by \(D\) gives (0.8).

If \(d=H\), the common root is forced and the two residual windows are
disjoint. The number of ordered pairs of nonoverlapping start positions
is

\[
 (L-H)(L-H+1).
\]

Ordering both windows, filling the remaining word positions, and
dividing by reversal gives

\[
 d(X,Y)
 =\frac{(L-H)(L-H+1)(H!)^2(m-H)!}
        {2(3H)!}.
\]

Division by \(D\) gives (0.9). If \(d>H\), then
\(|X\cap Y|=m-d<m-H\), so no common root exists.
\(\square\)

In particular,

\[
 \frac{\Delta_2}{D}
 =\frac{2(L-1)}{Lm^2}
 =\frac{2+o(1)}{m^2}.
\tag{2.2}
\]

For one physical path \(e\), there are \(L-d\) phase pairs at separation
\(d<H\). Therefore

\[
 \sum_{\{X,Y\}\subset e}\frac{d(X,Y)}R
 =
 \frac{2\rho(L-1)^2}{Lm^2}+O(m^{-3})
 =O(m^{-1}).
\tag{2.3}
\]

The \(d=H\) contribution is superpolynomially smaller. Thus even though
the edge has \(L\asymp m\) owners, its whole internal pair-overlap mass
is only \(O(m^{-1})\) on the root-degree scale.

## 3. Exact external influence

For a vertex \(v\notin e\), define

\[
 a_v(e)=
 |\{f:v\in f,\ f\cap e\ne\varnothing\}|.
\tag{3.1}
\]

### Lemma 3.1 (linear-path sphere bound)

Let \(E=\{X_1,\ldots,X_L\}\) be the owner path of one physical edge. For
every middle owner \(X\) and every \(1\le d<H/2\),

\[
 |\{i:d_J(X,X_i)=d\}|\le 2d+1.
\tag{3.2}
\]

For \(d=1\), the upper bound three is attainable with \(X\notin E\).

#### Proof

If \(X_i\) and \(X_j\) both have distance \(d\) from \(X\), the triangle
inequality gives \(d_J(X_i,X_j)\le2d\). Along a tight window path,

\[
 d_J(X_i,X_j)=\min\{|i-j|,H\}.
\]

Since \(2d<H\), all qualifying indices lie in an interval of diameter at
most \(2d\), proving (3.2).

For attainability at \(d=1\), take three consecutive \(H\)-windows with
starts \(0,1,2\). Replace the two end labels of the middle window by the
two adjacent outside labels. The resulting \(H\)-set is distinct from
the path windows and has Johnson distance one from all three.
\(\square\)

### Theorem 3.2 (sharp external owner influence)

Uniformly over all physical edges \(e\) and owners \(X\notin e\),
(0.10) holds. Conversely, some \(X,e\) attain its leading term.

#### Proof

Let \(A_e\) be the root of \(e\) and \(E\) its owner path. A union bound
over the vertices of \(e\) gives

\[
 a_X(e)
 \le
 \mathbf 1_{A_e\subset X}\,d(A_e,X)
 +\sum_{Y\in E}d(X,Y).
\tag{3.3}
\]

The root term divided by \(D\) is at most \(1/\binom mH\). By Lemma
3.1 and (0.8), the distance-one shell contributes at most

\[
 3\,\frac{2(L-1)}{Lm^2}.
\]

The shells \(2\le d<H/2\) contribute \(O(m^{-4})\), using (3.2) and the
successive binomial ratios in (0.8). The at most \(L\) terms with
\(d\ge H/2\), including (0.9), are superpolynomially smaller than
\(m^{-4}\) under (0.2). This proves the upper bound.

Use the three-window construction in Lemma 3.1. The three distance-one
pair links cannot have a common physical edge in adjacent pairs; any
remaining double count is bounded by a distance-two codegree
\(O(Dm^{-4})\). Inclusion-exclusion therefore gives

\[
 a_X(e)
 \ge
 3\,\frac{2(L-1)}{Lm^2}D-O(Dm^{-4}),
\]

which proves sharpness.
\(\square\)

### Lemma 3.3 (external root influence)

For a root \(B\ne A_e\),

\[
 \boxed{\frac{a_B(e)}R
 \le \frac{HL}{\binom MH}.}
\tag{3.4}
\]

The right side is superpolynomially smaller than \(m^{-2}\).

#### Proof

In the original, uncomplemented top picture, an owner of \(e\) is
compatible with the other root \(B\) precisely when the coordinate
difference between the two tops is contained in its omitted
\(H\)-window. A fixed nonempty set of positions belongs to at most
\(H\) length-\(H\) windows of a linear word. For each compatible owner,
(2.1) says that a uniform path at \(B\) contains it with probability
\(L/\binom MH\). Union-bound over the at most \(H\) compatible owners.
\(\square\)

## 4. Exact root-preserving compensation

The next lemma is independent of the common-core catalogue.

### Lemma 4.1 (balanced rooted proposal and owner waste)

Let a hypergraph have root part \(\mathcal A\), owner part
\(\mathcal X\), exactly one root in every edge, and exactly \(L\) owners
in every edge. For each root \(A\), let \(w_A\) be a probability
distribution on its currently available edges. Put

\[
 \lambda_X
 =\sum_{A\in\mathcal A}\sum_{e\ni X}w_A(e).
\tag{4.1}
\]

Independently for every root, with probability \(a\) propose one edge
sampled from \(w_A\), and otherwise propose nothing. For every supported
edge \(e\), let

\[
 S_e=
 \Pr(e\text{ meets no other proposed edge}\mid e\text{ is proposed}).
\tag{4.2}
\]

Suppose

\[
 0<s_0\le\min_e S_e,\qquad
 \lambda_X\le1\quad(X\in\mathcal X),\qquad
 0<h:=as_0<1.
\tag{4.3}
\]

Retain an isolated proposed edge \(e\) with additional probability
\(s_0/S_e\), independently over isolated proposals. Then:

1. the retained edges form a matching;
2. every root is covered with exact probability \(h\);
3. every owner \(X\) is covered with exact probability \(h\lambda_X\);
4. if an uncovered owner \(X\) is independently waste-deleted with
   conditional probability

   \[
   q_X=\frac{h(1-\lambda_X)}{1-h\lambda_X},
   \tag{4.4}
   \]

   then every root and every owner has total deletion probability
   exactly \(h\).

No root is discarded unless a path at that root is retained.

#### Proof

There is at most one proposal at each root. Isolated proposals are
pairwise disjoint, so their thinned subfamily is a matching. For an edge
\(e\) at root \(A\),

\[
 \Pr(e\text{ retained})
 =a w_A(e)S_e\frac{s_0}{S_e}
 =h w_A(e).
\tag{4.5}
\]

Summing over the edges at \(A\) proves the root assertion. Retained-edge
events through one owner are mutually exclusive, so summing (4.5) over
all edges through \(X\) gives \(h\lambda_X\). Finally,

\[
 h\lambda_X+(1-h\lambda_X)q_X=h.
\]

The number in (4.4) lies in \([0,1]\) because
\(0\le\lambda_X\le1\) and \(0<h<1\).
\(\square\)

There is a useful degree certificate. Suppose, for one common scale
\(R_t\),

\[
 d_t(A)\ge(1-\eta)R_t
 \quad(A\in\mathcal A_t),
\]

\[
 d_t(X)\le(\rho+\eta)R_t
 \quad(X\in\mathcal X_t),
\qquad
 2\eta\le1-\rho.
\tag{4.6}
\]

Uniform root distributions \(w_A(e)=1/d_t(A)\) then obey

\[
 \lambda_X
 \le\frac{\rho+\eta}{1-\eta}\le1.
\tag{4.7}
\]

Moreover, if

\[
 Q(e)=
 \sum_{B\ne A(e)}
 \sum_{\substack{f\text{ at }B\\f\cap e\ne\varnothing}}w_B(f),
\tag{4.8}
\]

then

\[
 Q(e)\le\sum_{X\in e}\lambda_X\le L.
\tag{4.9}
\]

For \(a=\gamma/L\), the union bound gives \(S_e\ge1-\gamma\). Thus one
may always take \(s_0=1-\gamma\), and

\[
 h=\frac{\gamma(1-\gamma)}L.
\tag{4.10}
\]

This is an exact integral one-bite certificate: it never chooses two
edges at one root and never discards a root to repair owner imbalance.

## 5. The exact first compensated bite

Use the full physical catalogue and uniform root distributions. Then
\(\lambda_X=D/R=\rho\) for every owner.

Fix a physical edge \(e\). For a root \(B\ne A(e)\), let

\[
 q_B(e)=
 \Pr(\text{a uniform path at }B\text{ meets }e).
\]

Put

\[
 Q(e)=\sum_{B\ne A(e)}q_B(e).
\tag{5.1}
\]

The first incidence moment is

\[
 F=L^2\left(
 \frac1\Lambda-\frac1{\binom MH}
 \right).
\tag{5.2}
\]

Indeed, each of the \(L\) owners has total load \(\rho\), while its
same-root contribution is \(L/\binom MH\). Bonferroni and Theorem 2.2
give

\[
 F-S\le Q(e)\le F,
\tag{5.3}
\]

where

\[
 S=
 \frac2\Lambda
 \sum_{d=1}^{H-1}
 \frac{(L-d)^2}{\binom md^2}
 +
 \frac{((L-H)(L-H+1))^2}
 {2\Lambda\binom mH^2}.
\tag{5.4}
\]

The \(d=1\) term is \((2+o(1))/m\), and every remaining term is
\(o(1/m)\). Hence, uniformly in \(e\),

\[
 Q(e)=L\rho+O(m^{-1}).
\tag{5.5}
\]

Now let every root propose with probability \(a=\gamma/L\). Proposals
at distinct roots are independent, so

\[
 S_e=\prod_{B\ne A(e)}(1-aq_B(e)).
\tag{5.6}
\]

Lemma 3.3 gives

\[
 \max_B q_B(e)\le \frac{HL}{\binom MH},
\tag{5.7}
\]

which is superpolynomially small. Therefore

\[
 \begin{aligned}
 \log S_e
 &=-aQ(e)
   +O\!\left(a^2\sum_Bq_B(e)^2\right)\\
 &=-\gamma\rho+O(m^{-2}).
 \end{aligned}
\tag{5.8}
\]

This proves (0.11), uniformly in \(e\). Choose a uniform

\[
 s_0=\exp(-\gamma\rho-Cm^{-2})
\]

with a sufficiently large fixed \(C\). Lemma 4.1 then gives (0.12).
The adjacent-window spike enters \(Q(e)\) only through the
\(O(m^{-1})\) Bonferroni correction and hence enters the isolation
exponent only at order \(O(m^{-2})\).

## 6. A sufficient conditional dynamic theorem

This section separates the favorable numerical ledger from the unproved
regeneration statement.

Run repeated compensated bites with fixed \(0<\gamma<1\), using
(4.10), and put

\[
 h=\frac{\gamma(1-\gamma)}L,\qquad
 z_t=(1-h)^t.
\tag{6.1}
\]

Stop at the first \(T\) such that \(z_T\le z_*\). Let \(d_t(v)\) denote
the available degree of an active vertex. For predictable scales
\(R_t>0\), put

\[
 Y_t(A)=\log\frac{d_t(A)}{R_t},
\qquad
 Y_t(X)=\log\frac{d_t(X)}{\rho R_t}.
\tag{6.2}
\]

For an active vertex \(v\notin e\), define the residual external
influence

\[
 a_{v,t}(e)
 =
 |\{f\in\mathcal L_t(v):f\cap e\ne\varnothing\}|,
\tag{6.3}
\]

where \(\mathcal L_t(v)\) is the available link of \(v\).

### Condition CDIR\((z_*)\)

There is a predictable culling-and-exposure rule with the following
properties until time \(T\).

1. Vertices are stopped and culled when

   \[
   |Y_t(v)|>\delta/8.
   \tag{6.4}
   \]

   Any additional structural culls have total expected size \(o(N)\) on
   the root side and \(o(W)\) on the owner side. Their entire effect on
   the remaining links is included in the increments below.

2. Whenever an unculled active vertex satisfies (6.4) with
   \(\le\) in place of \(>\), every external available edge obeys

   \[
   \frac{a_{v,t}(e)}{d_t(v)}
   \le\kappa_t,\qquad
   \kappa_t\le\frac{C}{m^2z_t}
   \tag{6.5}
   \]

   for one absolute \(C\).

3. Conditional on the vertex surviving the bite, expose root proposals,
   isolation-thinning coins, owner-waste coins, and structural-cull
   effects one at a time. For the stopped process \(Y_t(v)\), the total
   conditional drift during bite \(t\) has absolute value
   \(O(\kappa_t)\), the total conditional quadratic variation is
   \(O(\kappa_t)\), and every individual jump has absolute value
   \(O(\kappa_t)\), uniformly in \(v,t\).

Condition CDIR is not asserted here. It is the exact typical-trajectory
regeneration statement still required.

### Theorem 6.1 (CDIR gives one path per root with \(o(W)\) middle collision)

If CDIR\((z_*)\) holds for some

\[
 z_*=o(1),\qquad z_*\log m\to\infty,
\tag{6.6}
\]

then one can choose one physical common-core path at every root so that

\[
 C_{\mathrm{mid}}
 :=\sum_X(c_X-1)_+
 =o(W),
\tag{6.7}
\]

where \(c_X\) is the number of chosen paths containing owner \(X\).
Consequently the chosen paths contain \(W-o(W)\) distinct middle
owners, and all missing middle owners can be appended as \(o(W)\)
singletons.

#### Proof

For all sufficiently large \(m\), (6.4) implies

\[
 d_t(A)\ge(1-\delta/4)R_t,\qquad
 d_t(X)\le(\rho+\delta/4)R_t.
\tag{6.8}
\]

Take \(\eta=\delta/4\). Since \(2\eta\le\delta=1-\rho\), (4.7) gives
\(\lambda_X\le1\). Thus Lemma 4.1 applies at every good stage and the
retained paths over all stages form a matching.

Geometric summation gives

\[
 \sum_{t<T}\kappa_t
 \le
 \frac{C}{m^2}\sum_{t<T}\frac1{z_t}
 =O\!\left(\frac{L}{m^2z_*}\right)
 =O\!\left(\frac1{mz_*}\right).
\tag{6.9}
\]

Because

\[
 \delta^2=\Theta(H^2/m^2)
 =\Theta(\log m/m),
\tag{6.10}
\]

the accumulated drift in (6.9) is \(o(\delta)\). Freedman's inequality,
applied to the stopped exposure martingale at threshold \(\delta/8\),
gives for each fixed vertex

\[
 \Pr(v\text{ crosses the threshold before }T)
 \le
 2\exp\{-c z_*\log m\}=o(1).
\tag{6.11}
\]

The individual-jump term in Freedman's denominator is smaller than the
quadratic-variation term here. Summing (6.11) over each vertex class
shows that the expected threshold-cull fractions are \(o(1)\). Together
with the structural-cull budget in CDIR, there is an outcome with
\(o(N)\) culled roots and \(o(W)\) culled owners.

At every nonculled active root, Lemma 4.1 gives exact conditional
survival probability \(1-h\). Culling can only reduce the number of
active roots. Hence the expected number of roots still active at time
\(T\) is at most \(z_TN\). Choose an outcome in which the total number
\(s\) of culled or still-active roots satisfies

\[
 s=o(N).
\tag{6.12}
\]

Choose an arbitrary physical path at each of these \(s\) roots. The
paths selected during the compensated process were owner-disjoint.
Adding one path can increase \(C_{\mathrm{mid}}\) by at most \(L\).
Therefore

\[
 C_{\mathrm{mid}}\le Ls=o(LN)=o(W),
\]

which proves (6.7).

There are exactly \(LN\) chosen middle occurrences. The identity

\[
 |\{X:c_X>0\}|=LN-C_{\mathrm{mid}}
\]

and (0.5) now give

\[
 |\{X:c_X>0\}|=W-o(W).
\tag{6.13}
\]

Thus the number of unrepresented middle owners is \(o(W)\); append each
of them once as a singleton.
\(\square\)

The arbitrary completion in the last paragraph is legitimate only
because the corrected objective allows an \(o(W)\) collision/leave
ledger. It would not produce an exact owner-disjoint factor.

## 7. Symbolic test of the dynamic scales

At time zero, Theorems 2.1 and 3.2 give

\[
 d_0(A)=R,\qquad d_0(X)=\rho R,\qquad
 \kappa_0\le\frac{6+o(1)}{m^2}.
\tag{7.1}
\]

Thus the load gap and influence requirements begin with room
\(\delta=\Theta(H/m)\).

There is also no numerical obstruction in the ideal synchronized product
residual. If every root and owner is independently retained with
probability \(z\), then, conditional on the displayed vertex surviving,

\[
 \mathbb E d_z(A)=Rz^L,\qquad
 \mathbb E d_z(X)=Dz^L.
\tag{7.2}
\]

An owner-pair or root-owner link has one fewer unconditioned resource, so
its normalized codegree is amplified by \(z^{-1}\). The proof of
Theorem 3.2 therefore gives the ideal scale

\[
 \kappa(z)\le\frac{6+o(1)}{m^2z}.
\tag{7.3}
\]

The previously audited higher-codegree reserve \(m/H\) is likewise
reduced only to \(zm/H\). For the concrete stopping choice

\[
 z_*=(\log m)^{-1/3},
\tag{7.4}
\]

one has

\[
 \frac{z_*m}{H}\to\infty,\qquad
 \frac{\sum_{t<T}\kappa_t}{\delta^2}
 =O\!\left(\frac1{z_*\log m}\right)=o(1).
\tag{7.5}
\]

The ideal residual degrees are still enormous:

\[
 \log(Rz_*^L)
 =(1+o(1))m\log m-O(m\log\log m)\to\infty.
\tag{7.6}
\]

Therefore the root one-choice constraint, the edge size \(L\sim m\),
the distance-one spike, and stopping with an \(o(1)\) root fraction do
not create a scalar or codegree obstruction.

The first boundary visible to this influence/Freedman ledger is

\[
 z\asymp\frac1{\log m}.
\tag{7.7}
\]

There the exponent in (6.11) is only \(\Theta(1)\), so this method
cannot force even an \(o(1)\) exceptional fraction. This is a
proof-method boundary, not a matching counterexample. Stopping at
(7.4) occurs earlier and would already suffice for Theorem 6.1.

## 8. Exact obstruction and remaining invariant

The compensated residual is not a product residual. Lemma 4.1 equalizes
all one-vertex survival marginals, but a root degree counts whole
\(L\)-owner paths. Equal marginals do not control these \(L\)-way
survival events.

The audited reachable-exceptional-link construction supplies a matching
of \(o(N)\) paths after which almost every root and almost every owner
has its expected ambient degree, while a sparse owner family has lost a
fixed fraction of its link and its **static containment** neighbourhood
meets almost every root family. It therefore rules out a statewise
regeneration theorem whose exceptional-link clause is measured in the
original containment graph. It does not by itself refute a typical
unbiased trajectory theorem or a clause measured by literal surviving
root--owner pair-links.

That construction does not directly refute Lemma 4.1 or the one-sided
form of CDIR. A low-degree owner has \(\lambda_X<1\), and owner waste can
compensate it. Two-sided owner regularity and an unweighted
exceptional-incidence prohibition are stronger than the actual local
need.

The exact surviving invariant is the rootwise load polytope

\[
 \boxed{
 \sum_{e\in\mathscr P_A}w_A(e)=1,\qquad
 \sum_A\sum_{e\ni X}w_A(e)\le1,\qquad
 w_A(e)\ge0,}
\tag{8.1}
\]

together with typical preservation of

\[
 \boxed{
 \frac{a_{v,t}(e)}{d_t(v)}
 =O\!\left(\frac1{m^2z_t}\right).}
\tag{8.2}
\]

Initial symmetry proves (8.1), and the exact formulas above prove the
initial and ideal-product forms of (8.2). They do not prove that
(8.1)--(8.2) regenerate after conditioning on earlier accepted paths,
isolation thinning, and owner waste.

Thus the common-core compensated nibble has:

- an exact physical simple-hypergraph model;
- exact degrees, all owner-pair codegrees, and sharp external influence;
- an exact integral root-safe one-bite operation;
- a favorable quantitative ledger down to \(z_*\log m\to\infty\); and
- one precisely isolated unproved dynamic invariant.

No typical-trajectory theorem, \(2m\)-cycle fusion, simultaneous
all-depth trace simplicity, or coefficient-one conclusion is claimed.
