# Conditional \(q=1\) entropy, correlated SCD completion, and physical chronology

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Result

Let

\[
 n=2m+\varepsilon,\qquad \varepsilon\in\{0,1\},
\]

\[
 \mathcal M=\binom{[n]}m,\qquad
 \mathcal L_q=\binom{[n]}{m-q},\qquad
 W=|\mathcal M|,\qquad N_q=|\mathcal L_q|.
\]

Throughout,

\[
 1\le H\le m.
\tag{0.0}
\]

Thus every deletion word and every layer appearing below exists, including
the terminal layer when \(H=m\).

Condition on exact middle ownership and on an owner-labelled lower
depth-one map

\[
 \pi:\mathcal M\longrightarrow\mathcal L_1,\qquad \pi(X)\subset X.
\tag{0.1}
\]

Write

\[
 \lambda(R)=|\pi^{-1}(R)|.
\tag{0.2}
\]

The lower-rainbow hypothesis is

\[
 \lambda(R)\ge1\qquad(R\in\mathcal L_1).
\tag{0.3}
\]

There are three different conditioning levels, and they have opposite
answers.

1. **Abstract nested flags.** Under (0.3), all later lower target layers
   admit a simultaneous integral zero-hole completion. A symmetric-chain
   graft gives this directly. A layered totally-unimodular flow gives the
   stronger statement that one selected occurrence of every \(q=1\)
   target can be extended to \(N_1\) nested paths whose depth-\(q\) loads
   are exactly

   \[
    \left\lfloor\frac{N_1}{N_q}\right\rfloor
    \quad\text{or}\quad
    \left\lceil\frac{N_1}{N_q}\right\rceil.
   \tag{0.4}
   \]

   Thus \(q=1\) surjectivity removes every abstract lower-layer Hall
   obstruction, at every depth simultaneously.

2. **Independent conditional completion.** Give each owner an independent
   uniform deletion order below its fixed first facet. At
   \(q=a\sqrt m+O(1)\), \(a>0\), the expected missing fraction has the
   universal limit

   \[
    \frac{\mathbb E M_q}{N_q}\longrightarrow
    \exp(-e^{a^2}),
   \qquad
    \frac{\mathbb E M_q}{W}\longrightarrow
    \exp(-a^2-e^{a^2}),
   \tag{0.5}
   \]

   independently of how the surplus \(q=1\) owner occurrences are
   distributed. The hole count is concentrated at this linear scale.
   This is a rigorous obstruction to the independent product law only.
   It is not an impossibility theorem, because the correlated construction
   in Item 1 has zero holes.

3. **Ordered physical factor.** Once a directed middle-owner successor and
   its ordered \(q=1\) labels are fixed, every later lower shadow is already
   determined:

   \[
    L_{i,q}
    =\bigcap_{t=0}^{q-1}L_{i+t,1},
    \qquad
    L_{i,q+1}=L_{i,q}\cap L_{i+1,q}.
   \tag{0.6}
   \]

   Hence the conditional entropy of all later physical lower shadows is
   exactly zero. The remaining issue is not entropy but shift coherence:
   can the ordered \(q=1\) word be chosen close to one of the correlated
   nested completions in Item 1?

There is an exact positive interface. If the aggregate mismatch between a
physical ordered factor and a designated SCD tower is \(B_H\), then the
aggregate later lower-hole count is at most \(B_H\). Thus
\(B_H=o(W)\) makes all later lower conditions asymptotically cheap. The
\(q=1\) histogram alone gives no bound on \(B_H\).

There is also a statewise collision certificate. Distinct \(q=1\) facets
can have the same depth-two target. If a physical state contains \(t\)
distinct depth-two targets of multiplicity at least two, then

\[
 M_2\ge\bigl(t-(W-N_2)\bigr)_+
\tag{0.7}
\]

when every start is depth-two valid. This is a genuine obstruction for that
state, but no claim is made that every \(q=1\)-rainbow state has such a
family.

Finally, grouping Boolean SCDs by their paired nonmiddle skeleton gives an
exact central-fiber theorem. The contracted two-corner incidence graph is
a triangle-free pseudoforest, and if \(\gamma\) is its leave-preserving
cyclic switch mass, then

\[
 \log_2 Z\le\frac\gamma4+D\log_2(m+1),
 \qquad D=\operatorname {Cat}_m.
\tag{0.8}
\]

An SCD-to-skeleton count gap of \(N/4-o(W)\) bits would force
\(W-o(W)\) paired mass. Tomon's leading SCD enumeration does not resolve
this width-scale gap: every possible central-fiber regime has the same
Tomon asymptotic. Moreover, near-maximal fiber entropy forces almost all
of that mass into four-cycles, so it does not supply the long central
components, much less the literal physical components, required for
constant one.

## 1. The abstract conditional flag space

For \(X\in\mathcal M\), put \(R_X=\pi(X)\). Once \(R_X\) is fixed, an
abstract nested lower flag through depth \(H\) is specified by an ordered
list of \(H-1\) distinct elements of \(R_X\):

\[
 \sigma_X=(x_2(X),\ldots,x_H(X)).
\]

The resulting targets are

\[
 F_q(X)=R_X\setminus
 \{x_2(X),\ldots,x_q(X)\},
 \qquad 2\le q\le H.
\tag{1.1}
\]

Thus the number of ownerwise abstract completions is exactly

\[
 \boxed{
 |\Omega_H(\pi)|
 =\left((m-1)_{\underline{H-1}}\right)^W,}
\tag{1.2}
\]

where \(x_{\underline r}=x(x-1)\cdots(x-r+1)\). Under the uniform product
law on these completions, its conditional Shannon entropy is

\[
 \boxed{
 {\sf H}(F_2,\ldots,F_H\mid\pi)
 =W\log (m-1)_{\underline{H-1}}.}
\tag{1.3}
\]

This is the entropy of the ownerwise flag relaxation. It is not the entropy
of physical cycle factors, because neighbouring physical starts must have
overlapping flag suffixes.

## 2. Exact one-target kernel under independent completion

Fix \(q\ge2\), and abbreviate

\[
 C_q=\binom{m-1}{q-1}.
\tag{2.1}
\]

For \(S\in\mathcal L_q\), define its conditioned incidence degree

\[
 d_\pi(S)=
 \sum_{\substack{R\in\mathcal L_1\\S\subset R}}\lambda(R).
\tag{2.2}
\]

Every occurrence with first facet \(R\supset S\) hits \(S\) at depth \(q\)
with probability \(1/C_q\). Different owner occurrences choose
independently.

### Theorem 2.1 (exact conditional load and hole kernel)

Let \(\mu_q(S)\) be the depth-\(q\) load and \(M_q\) the number of missing
targets under the uniform product law. Then

\[
 \mathbb E\mu_q(S)=\frac{d_\pi(S)}{C_q},
\tag{2.3}
\]

\[
 \operatorname {Var}\mu_q(S)
 =d_\pi(S)\frac1{C_q}\left(1-\frac1{C_q}\right),
\tag{2.4}
\]

and

\[
 \boxed{
 \mathbb E M_q
 =\sum_{S\in\mathcal L_q}
 \left(1-\frac1{C_q}\right)^{d_\pi(S)}.}
\tag{2.5}
\]

For distinct \(S,T\in\mathcal L_q\), put

\[
 d_\pi(S,T)=
 \sum_{\substack{R\in\mathcal L_1\\S\cup T\subset R}}\lambda(R).
\tag{2.6}
\]

Then the same-depth covariance is exactly

\[
 \boxed{
 \operatorname {Cov}(\mu_q(S),\mu_q(T))
 =-\frac{d_\pi(S,T)}{C_q^2}.}
\tag{2.7}
\]

#### Proof

For every owner occurrence \(X\), the depth-\(q\) target is uniform among
the \(C_q\) rank-\((m-q)\) subsets of \(R_X\). Therefore the indicator of
the event \(F_q(X)=S\) is Bernoulli with parameter \(1/C_q\) when
\(S\subset R_X\), and zero otherwise. Summing independent indicators gives
(2.3)--(2.4). A target is missed precisely when all its
\(d_\pi(S)\) eligible occurrences avoid it, proving (2.5).

For \(S\ne T\), one owner occurrence cannot choose both targets at the
same depth. Its covariance is therefore \(-1/C_q^2\) when its facet
contains both, and zero otherwise. Summation proves (2.7). \(\square\)

The negative covariance in (2.7) is exact, but it does not make the product
law a near-cover.

The corresponding hole indicators are also negatively correlated. Put

\[
 I_S=\mathbf 1_{\{\mu_q(S)=0\}}.
\]

For distinct \(S,T\), abbreviate \(C=C_q\),
\(d_S=d_\pi(S)\), \(d_T=d_\pi(T)\), and
\(d=d_\pi(S,T)\). Owner occurrences whose first facet contains both
targets must avoid two distinct choices, whereas occurrences eligible for
only one target must avoid one. Hence

\[
 \boxed{
 \mathbb E(I_SI_T)
 =(1-2/C)^d(1-1/C)^{d_S+d_T-2d}.}
\tag{2.7a}
\]

Since \(1-2/C\le(1-1/C)^2\), this gives

\[
 \operatorname {Cov}(I_S,I_T)\le0,
 \qquad
 \boxed{\operatorname {Var}M_q\le\mathbb E M_q.}
\tag{2.7b}
\]

The last inequality follows by summing covariances and using
\(\operatorname {Var}I_S\le\mathbb E I_S\). This strengthens
concentration around the product-law scale, but, like (2.7), says nothing
statewise about correlated physical completions.

### Cross-depth correlation

Let \(2\le q<r\le H\), \(S\in\mathcal L_q\), and
\(T\in\mathcal L_r\). For one occurrence with first facet \(R\), define

\[
 p_R^{q}(S)=\frac{\mathbf1_{\{S\subset R\}}}{C_q}.
\tag{2.8}
\]

The exact joint kernel is

\[
 p_R^{q,r}(S,T)
 =
 \frac{\mathbf1_{\{T\subset S\subset R\}}}
 {C_q\binom{m-q}{r-q}}.
\tag{2.9}
\]

Consequently

\[
 \boxed{
 \operatorname {Cov}(\mu_q(S),\mu_r(T))
 =
 \sum_R\lambda(R)
 \left[
 p_R^{q,r}(S,T)-p_R^q(S)p_R^r(T)
 \right].}
\tag{2.10}
\]

Thus the only positive conditional correlations in the product law are
the forced nested ones \(T\subset S\); nonnested pairs receive only the
negative exclusivity term.

## 3. A universal product-law hole asymptotic

The two exact degree sums needed below are

\[
 \sum_{S\in\mathcal L_q}d_\pi(S)=W C_q,
\tag{3.1}
\]

and, under the lower-rainbow hypothesis (0.3),

\[
 d_\pi(S)\ge
 D_q:=\binom{n-m+q}{q-1}.
\tag{3.2}
\]

Indeed every owner occurrence contributes to
\(\binom{m-1}{q-1}=C_q\) targets, proving (3.1), while a fixed \(S\) has
exactly \(D_q\) rank-\((m-1)\) supersets and each occurs at least once.
Double counting also gives

\[
 \frac{D_q}{C_q}=\frac{N_1}{N_q}.
\tag{3.3}
\]

### Theorem 3.1 (conditional Jensen squeeze)

For every \(q\ge2\),

\[
 \boxed{
 N_q\left(1-\frac1{C_q}\right)^{C_qW/N_q}
 \le \mathbb E M_q
 \le
 N_q\left(1-\frac1{C_q}\right)^{D_q}.}
\tag{3.4}
\]

#### Proof

The function

\[
 x\longmapsto\left(1-\frac1{C_q}\right)^x
\]

is convex and decreasing. Jensen's inequality and (3.1) give the lower
bound. The pointwise degree lower bound (3.2) gives the upper bound.
\(\square\)

### Corollary 3.2 (Gaussian-depth product-law floor)

Let \(q=a\sqrt m+O(1)\), with fixed \(a>0\). Uniformly for
\(\varepsilon\in\{0,1\}\),

\[
 \frac W{N_q}\longrightarrow e^{a^2},
\qquad
 \frac{N_1}{N_q}\longrightarrow e^{a^2},
\qquad
 C_q\longrightarrow\infty.
\tag{3.5}
\]

Therefore the two sides of (3.4) have the same limit and

\[
 \boxed{
 \frac{\mathbb E M_q}{N_q}\longrightarrow e^{-e^{a^2}},
 \qquad
 \frac{\mathbb E M_q}{W}\longrightarrow
 e^{-a^2-e^{a^2}}.}
\tag{3.6}
\]

#### Proof

The exact ratio is

\[
 \frac W{N_q}
 =\prod_{j=1}^{q}
 \frac{m+\varepsilon+j}{m-q+j}.
\tag{3.7}
\]

Taking logarithms gives \(a^2+o(1)\). Moreover

\[
 \frac{N_1}{W}=\frac{m}{m+\varepsilon+1}\longrightarrow1,
\]

which proves the second limit in (3.5). Now use
\((1-1/C_q)^{C_qx}\to e^{-x}\) in (3.4). \(\square\)

Changing one owner's deletion order changes the fixed-depth hole count by
at most one. McDiarmid's bounded-differences inequality and (3.6) therefore
give, for some \(c_a>0\),

\[
 \Pr(M_q\ge c_aW)\ge1-\exp(-\Omega_a(W)).
\tag{3.8}
\]

There is also an exact counting form of this statement. Let

\[
 L_q:=N_q\left(1-\frac1{C_q}\right)^{C_qW/N_q},
\tag{3.9}
\]

the Jensen lower bound in (3.4). Since \(\mathbb E M_q\ge L_q\), the
lower-tail form of McDiarmid gives

\[
 \boxed{
 \Pr_{\Omega_H(\pi)}\left(M_q\le\frac{L_q}{2}\right)
 \le \exp\left(-\frac{L_q^2}{2W}\right),}
 \qquad q\le H.
\tag{3.10}
\]

Here the probability is uniform on the ownerwise product flag space. At
\(q=a\sqrt m+O(1)\), the right side is \(\exp(-c_a'W)\) for a constant
\(c_a'>0\). Consequently, if a probability law \(P\) on
\(\Omega_H(\pi)\) is supported on the event in (3.10), then

\[
 \boxed{
 D_{\rm KL}(P\Vert U_{\Omega_H(\pi)})
 =\log|\Omega_H(\pi)|-{\sf H}(P)
 \ge\frac{L_q^2}{2W}.}
\tag{3.11}
\]

Indeed the uniform measure of the support is at most the right side of
(3.10), and the uniform conditional law on a given support maximizes
entropy. Thus an abstract completion with \(o(W)\) holes at a Gaussian
depth has a linear conditional entropy deficit relative to the product
flag law. This is a counting inequality inside the relaxation, not an
impossibility statement for the much smaller, highly correlated class of
physical factors.

Equations (3.6)--(3.8) are statements about the independent conditional
product law only. They cannot be promoted to a statewise obstruction:
Section 4 constructs a deterministic correlated completion with zero
holes.

## 4. Exact correlated completion after \(q=1\)

### 4.1 A direct SCD graft

Fix a symmetric-chain decomposition of \(2^{[n]}\). Restrict every chain
at rank \(m-1\); the lower portions partition all sets of ranks at most
\(m-1\), and every \(R\in\mathcal L_1\) is the top of exactly one such
restricted chain.

By (0.3), choose one primary owner

\[
 X_R\in\pi^{-1}(R)
\tag{4.1}
\]

for every \(R\). Attach to \(X_R\) the successive lower members of the
restricted SCD chain ending at \(R\). If that chain terminates before depth
\(H\), extend the deletion order arbitrarily; give all nonprimary owners
arbitrary nested flags.

### Theorem 4.1 (SCD conditional zero-hole theorem)

The resulting owner flags are nested and, simultaneously for every
\(1\le q\le H\), cover every target in \(\mathcal L_q\).

#### Proof

Every \(S\in\mathcal L_q\) belongs to a unique symmetric chain. Since
\(|S|=m-q\le m-1\), that chain crosses rank \(m-1\) in a unique set
\(R(S)\). The primary owner \(X_{R(S)}\) receives the restricted chain
containing \(S\), so its depth-\(q\) flag equals \(S\). Nestedness is
inherited from the chain. \(\square\)

Thus exact \(q=1\) support makes every later lower condition exactly free
inside the abstract nested-flag relaxation. This conclusion is stronger
than an entropy estimate.

### 4.2 Balanced nested paths by total unimodularity

The SCD graft guarantees coverage but does not balance the \(N_1\) primary
paths at later layers. The latter also has an exact solution.

Form the layered inclusion network with vertex layer
\(\mathcal L_q\) at time \(q\), and arcs

\[
 S\longrightarrow S\setminus\{x\}
\quad
(S\in\mathcal L_q,\ x\in S)
\tag{4.2}
\]

from layer \(q\) to \(q+1\). Supply one unit at every vertex of
\(\mathcal L_1\). At a vertex of layer \(q\), impose the integral
throughput interval

\[
 \ell_q=
 \left\lfloor\frac{N_1}{N_q}\right\rfloor,
 \qquad
 u_q=
 \left\lceil\frac{N_1}{N_q}\right\rceil.
\tag{4.3}
\]

### Theorem 4.2 (balanced conditional chain extension)

There is an integral flow of value \(N_1\) in this network. It decomposes
into \(N_1\) nested paths, one starting at each \(R\in\mathcal L_1\), and
every target at depth \(q\) lies on exactly \(\ell_q\) or \(u_q\) paths.

#### Proof

Start one unit at every rank-\((m-1)\) set and, fractionally, delete a
uniformly random remaining coordinate at each step. Symmetry makes the
throughput at every vertex of layer \(q\) exactly \(N_1/N_q\), which lies
in (4.3). Thus the network with the stated integral lower and upper node
capacities has a fractional feasible flow.

Split every node into an in-node and out-node joined by one capacity arc.
The resulting constraint matrix is a directed-network matrix. Integral
lower and upper capacities and integral supplies imply an integral feasible
flow. Since each source supplies one unit, the integral flow decomposes
into \(N_1\) source-to-final-layer paths. Their node throughputs are
integers in the interval (4.3), hence are \(\ell_q\) or \(u_q\).
\(\square\)

Because \(N_1\ge N_q\), every \(\ell_q\ge1\); hence this is again a
simultaneous zero-hole completion. Attach the path beginning at \(R\) to
the chosen primary owner \(X_R\). The remaining \(W-N_1\) owners may be
completed arbitrarily without creating holes.

Theorem 4.2 preserves the fixed \(q=1\) owner map, integrality, nesting, and
all lower target supports. It does not impose a physical successor order,
upper flags, or cycle completion.

### 4.3 Exact propagation of a \(q=1\) support defect

The balanced flow also gives a quantitative near-rainbow theorem. Suppose
the \(q=1\) map misses exactly

\[
 h=|\{R\in\mathcal L_1:\lambda(R)=0\}|
\tag{4.4}
\]

targets. Add one virtual primary owner at every missing root, run Theorem
4.2 on all \(N_1\) roots, and then delete the \(h\) virtual paths. Put

\[
 c_q^*=\left\lfloor\frac{N_1}{N_q}\right\rfloor.
\tag{4.5}
\]

### Theorem 4.3 (conditional defect contraction)

The surviving actual primary owners admit nested flags with

\[
 \boxed{
 M_q^{\rm abs}\le
 \left\lfloor\frac{h}{c_q^*}\right\rfloor
 \qquad(1\le q\le H).}
\tag{4.6}
\]

More generally, suppose a physical realization is compared with these
reference paths and \(B_q\) surviving primary roots disagree with their
reference depth-\(q\) target. Then its actual hole count satisfies

\[
 \boxed{
 M_q^{\rm phys}\le
 \left\lfloor\frac{h+B_q}{c_q^*}\right\rfloor.}
\tag{4.7}
\]

Consequently

\[
 \boxed{
 \sum_{q=1}^{H}M_q^{\rm phys}
 \le
 \sum_{q=1}^{H}
 \left\lfloor\frac{h+B_q}{c_q^*}\right\rfloor.}
\tag{4.8}
\]

#### Proof

In the full balanced flow, every depth-\(q\) target has at least
\(c_q^*\) reference paths. After deleting the virtual paths, an abstractly
missing target must have all of its reference witnesses among the \(h\)
deleted paths. At a fixed depth, each deleted path supplies only one
witness, so distinct missing targets consume disjoint groups of at least
\(c_q^*\) deleted witnesses. This proves (4.6).

For a physical realization, also discard every primary path whose actual
depth-\(q\) trace disagrees with its reference target. There are \(B_q\)
such paths. If a target is physically missing, all of its at least
\(c_q^*\) reference witnesses lie among the \(h+B_q\) discarded paths.
The same disjoint counting proves (4.7), and summation gives (4.8).
Extra nonprimary owners can only add witnesses. \(\square\)

This is the sharp conditional counting form useful for \(L^1\) coverage:
the \(q=1\) defect and the chronological disagreement are discounted by
the later reference multiplicity \(c_q^*\). No floor-energy statement is
implied.

## 5. Ordered physical \(q=1\) data has zero residual entropy

Let \(s:\mathcal M\to\mathcal M\) be a directed owner permutation whose
arcs are Johnson edges. Put

\[
 R_X=X\cap s(X)\in\mathcal L_1.
\tag{5.1}
\]

For \(q\ge1\), define the physical lower trace

\[
 L_q(X)=\bigcap_{j=0}^{q}s^j(X).
\tag{5.2}
\]

### Theorem 5.1 (ordered first-shadow determinism)

For every \(X\) and \(q\ge1\),

\[
 \boxed{
 L_q(X)=\bigcap_{j=0}^{q-1}R_{s^j(X)}.}
\tag{5.3}
\]

Equivalently, along an oriented component,

\[
 \boxed{
 L_{i,q+1}=L_{i,q}\cap L_{i+1,q}.}
\tag{5.4}
\]

Consequently

\[
 {\sf H}\bigl((L_q(X))_{X,\ q\ge2}\mid
              s,(R_X)_X\bigr)=0.
\tag{5.5}
\]

#### Proof

The intersection of the adjacent pair intersections

\[
 (X\cap sX)\cap(sX\cap s^2X)\cap\cdots
 \cap(s^{q-1}X\cap s^qX)
\]

is exactly the intersection of the \(q+1\) owner states. This proves
(5.3); (5.4) is the same identity with overlapping windows. Equation
(5.5) follows because all later traces are deterministic functions of the
conditioned data. \(\square\)

Thus, if a \(q=1\) theorem already outputs the directed physical factor,
there is no later entropy to spend. Later coverage must be engineered in
the ordering of the \(q=1\) labels or changed by legal refactorization.

## 6. Exact physical correlation after the \(q=1\) histogram

Define the deletion label

\[
 a(X)=X\setminus R_X.
\tag{6.1}
\]

If the physical component is return-free through depth \(q\), then

\[
 L_q(X)
 =R_X\setminus
 \{a(sX),a(s^2X),\ldots,a(s^{q-1}X)\}.
\tag{6.2}
\]

Therefore the physical depth-\(q\) load is the exact sliding correlation

\[
 \boxed{
 \mu_q(S)=
 \sum_{\substack{R\in\mathcal L_1\\S\subset R}}
 \ \sum_{\substack{X\in\mathcal M\\R_X=R}}
 \mathbf1\!\left\{
  \{a(s^jX):1\le j\le q-1\}=R\setminus S
 \right\}.}
\tag{6.3}
\]

At depth two this specializes to

\[
 \boxed{
 \mu_2(P)=
 \sum_{x\notin P}
 \#\{X:R_X=P\cup\{x\},\ a(sX)=x\}.}
\tag{6.4}
\]

The histogram \(\lambda(R)\) controls only the outer cardinalities in
(6.3). It contains no information about the successor correlations inside
the indicator. This is the precise reason that \(q=1\) balance does not
automatically propagate.

### 6.1 Exact hereditary run formula

Write one oriented physical component's cyclic first-shadow word as

\[
 C_0,C_1,\ldots,C_{\ell-1},
 \qquad C_i=X_i\cap X_{i+1}.
\]

Fix \(T\in\mathcal L_q\), and form the cyclic binary word

\[
 \xi_i(T)=\mathbf1_{\{T\subset C_i\}}.
\tag{6.5}
\]

Assume every rooted \(q\)-window under consideration has the correct rank.
If (6.5) is not identically one and its cyclic runs of ones have lengths
\(\ell_1,\ldots,\ell_r\), then this component contributes exactly

\[
 \boxed{
 \sum_{j=1}^{r}(\ell_j-q+1)_+}
\tag{6.6}
\]

occurrences of \(T\) at depth \(q\). If (6.5) is identically one, the
contribution is instead the component length \(\ell\). Summing these
contributions over components gives \(\mu_q(T)\).

Indeed a depth-\(q\) lower trace is the intersection of \(q\) consecutive
first-shadow facets by (5.3). It contains \(T\) exactly when the
corresponding \(q\) binary entries are all one; the correct-rank hypothesis
then forces equality with \(T\).

At \(q=2\), let \(d_\pi(T)\) be the total number of first-shadow
occurrences containing \(T\), and let \(r_T\) count their cyclic
one-runs, with an identically-one component assigned run count zero.

\[
 \boxed{\mu_2(T)=d_\pi(T)-r_T.}
\tag{6.7}
\]

Thus \(T\) is missing exactly when all its eligible first-shadow
occurrences are isolated. In the exactly-once \(q=1\) core,

\[
 d_\pi(T)=
 \binom{n-m+2}{1}=n-m+2
\tag{6.8}
\]

for every \(T\in\mathcal L_2\). The inventory is perfectly regular; only
the cyclic run statistic decides depth-two coverage.

## 7. SCD mismatch gives an exact positive repair inequality

Use the SCD graft of Section 4.1. Every target \(S\in\mathcal L_q\) has a
designated primary owner

\[
 \iota_q(S)=X_{R(S)}.
\tag{7.1}
\]

For a physical successor \(s\), put

\[
 B_q(s)=
 |\{S\in\mathcal L_q:L_q(\iota_q(S))\ne S\}|,
\qquad
 B_H(s)=\sum_{q=2}^{H}B_q(s).
\tag{7.2}
\]

### Theorem 7.1 (conditional SCD repair bound)

For every physical state,

\[
 \boxed{
 \sum_{q=2}^{H}M_q\le B_H(s),}
\tag{7.3}
\]

where \(M_q\) is its actual lower target-hole count.

#### Proof

Every target \(S\) has one designated owner. If that owner's physical
trace equals \(S\), then \(S\) is covered. Therefore every missing target
belongs to the mismatch set counted in (7.2). Sum over depths. \(\square\)

Write the SCD deletion labels on the primary tower as

\[
 R,\quad
 R-\{\delta_2(R)\},\quad
 R-\{\delta_2(R),\delta_3(R)\},\ldots.
\]

For a return-free physical state, the depth-\(q\) designated flag is good
exactly when

\[
 \{\delta_2(R),\ldots,\delta_q(R)\}
 =
 \{a(sX_R),\ldots,a(s^{q-1}X_R)\}.
\tag{7.4}
\]

Thus \(B_H=o(W)\) is a rigorous sufficient condition making every later
lower layer asymptotically cheap. Equality of complete deletion orders is
unnecessary; only the prefix sets in (7.4) matter. The \(q=1\) rainbow
property itself supplies no estimate on \(B_H\).

If the balanced TU paths of Theorem 4.2 are used as the reference system,
Theorem 4.3 gives the sharper weighted sufficient condition

\[
 \sum_{q=1}^{H}\frac{h+B_q}{c_q^*}=o(W).
\tag{7.5}
\]

Here \(h\) is the \(q=1\) support defect and \(B_q\) is the number of
depth-\(q\) chronological disagreements. This is the exact sense in which
later lower conditions become cheaper as the reference multiplicity
\(c_q^*\) grows.

## 8. A statewise collision obstruction, with exact scope

### Lemma 8.1 (complete \(q=1\) star with one \(q=2\) target)

Let \(S\) be an \((m-2)\)-set, list distinct outside elements cyclically as

\[
 x_0,x_1,\ldots,x_{\ell-1},
 \qquad \ell\ge4,
\]

and put

\[
 X_i=S\cup\{x_i,x_{i+1}\}.
\tag{8.1}
\]

Then \((X_i)_{i\in\mathbb Z_\ell}\) is a simple physical Johnson cycle.
Its depth-one lower targets are

\[
 X_i\cap X_{i+1}=S\cup\{x_{i+1}\},
\tag{8.2}
\]

and are all distinct, whereas every depth-two lower target equals \(S\).
In particular, if the list contains every point outside \(S\), then

\[
 \ell=n-m+2=m+\varepsilon+2
\tag{8.3}
\]

and the cycle uses every rank-\((m-1)\) extension of \(S\) exactly once
at depth one while giving \(S\) multiplicity \(\ell\) at depth two.

#### Proof

Consecutive owners in (8.1) differ by exchanging \(x_i\) for
\(x_{i+2}\), so they are Johnson-adjacent. The unordered adjacent pairs
\(\{x_i,x_{i+1}\}\) are distinct, so the cycle is simple. Formula (8.2)
is immediate, and three consecutive owners have no common outside element,
so their intersection is \(S\). \(\square\)

This is a physical, owner-injective, \(q=1\)-injective component with
maximal depth-two concentration on its hereditary star. It refutes an
implication from those local properties to \(q=2\) coverage, but it is not
a global factor obstruction. Its repeat excess is \(\ell-1\), but it has
only one distinct repeated target; by itself it does not meet the
distinct-target threshold in Corollary 8.3.

Here “physical Johnson cycle” means a genuine successor cycle on distinct
middle owners with one-coordinate exchanges. The lemma does not assert the
stronger return-free/isometric contiguous-OR strip condition, so it cannot
be imported as a literal factor obstruction without an embedding theorem.

### Lemma 8.2 (two disjoint \(q=1\) pairs with one \(q=2\) target)

Assume \(m+\varepsilon\ge6\). Let \(P\) be an \((m-2)\)-set and choose
eight distinct elements outside \(P\),

\[
 a,b,c,d,a',b',c',d'.
\]

The two physical Johnson triples

\[
 Pab,\ Pbc,\ Pcd
\tag{8.4}
\]

and

\[
 Pa'b',\ Pb'c',\ Pc'd'
\tag{8.5}
\]

have four distinct depth-one lower targets

\[
 Pb,\ Pc,\ Pb',\ Pc',
\tag{8.6}
\]

but both have depth-two lower target \(P\).

#### Proof

Consecutive displayed middle sets differ by one exchange, so both triples
are physical Johnson geodesics. Their adjacent intersections are (8.6),
while each threefold intersection is \(P\). \(\square\)

This proves that even local physicality plus depth-one injectivity does not
force depth-two injectivity. It is a finite correlation witness, not an
asymptotic no-go.

For any state at depth \(q\), let \(G_q\) be the number of valid rooted
occurrences, let

\[
 R_q=\sum_{S\in\mathcal L_q}(\mu_q(S)-1)_+,
\tag{8.7}
\]

and let \(M_q\) be the number of holes. The exact identity is

\[
 \boxed{M_q=N_q-G_q+R_q.}
\tag{8.8}
\]

Indeed the number of occupied targets is \(G_q-R_q\).

### Corollary 8.3 (collision certificate)

Suppose all \(W\) starts are valid at depth two, and there are \(t\)
distinct targets \(P\) with \(\mu_2(P)\ge2\). Then

\[
 \boxed{
 M_2\ge\bigl(t-(W-N_2)\bigr)_+.}
\tag{8.9}
\]

Thus a family with \(t\ge W-N_2+\alpha W\) certifies
\(M_2\ge\alpha W\) in that state. Lemmas 8.1--8.2 show how this
certificate can be invisible to \(q=1\); they do not prove that a
positive-density certificate is unavoidable in a complete factor.

## 9. Exact implication boundary

The conditional question now has a complete answer at the three natural
levels.

* A complete \(q=1\) lower ledger has no abstract multidepth Hall or
  integrality obstruction. Theorems 4.1 and 4.2 produce simultaneous
  integral nested zero-hole flags.

* Independent conditional choices are quantitatively wrong:
  Theorem 3.1 gives the exact Gaussian product-law hole constant, and
  (3.8) gives concentration. This closes independent completion as a proof
  method, not as a state space.

* After a physical successor is fixed, later lower shadows have conditional
  entropy zero by Theorem 5.1. Their loads are the sliding correlations
  (6.3), which are absent from the \(q=1\) histogram.

* SCD structure becomes physically useful precisely through shift
  coherence. The exact sufficient statistic is the mismatch ledger
  \(B_H\), not the entropy of ownerwise deletion orders. Proving
  \(B_H=o(W)\), together with the already separate component, cooldown,
  upper-shadow, and seam conditions, would make later lower shadows
  asymptotically free.

* Conversely, a rigorous obstruction must exhibit actual ordered collision
  excess, such as (8.8)--(8.9), or a hereditary lower bound on
  \(B_H\). Entropy or independent-sampling calculations alone cannot be
  promoted to impossibility because the correlated SCD/TU completion has
  zero abstract holes.

The remaining theorem is therefore an ordered realization problem:
construct a physical \(q=1\)-rainbow owner factor whose cyclic first-shadow
word is \(o(W)\)-close, in the prefix-set metric (7.4), to a correlated
SCD/TU path system. This is strictly stronger than \(q=1\) rainbow and
strictly weaker than prescribing every full deletion order in advance.

## 10. Nonmiddle SCD skeletons: exact central fibers and the enumeration barrier

This section specializes to the even Boolean lattice \(B_{2m}\). Put

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal M=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}{m+1},
\]

\[
 W=|\mathcal M|,\qquad
 N=|\mathcal L|=W-D,\qquad
 D=\frac{W}{m+1}=\operatorname {Cat}_m.
\tag{10.1}
\]

Delete the middle member of every chain in a Boolean SCD, but retain the
pairing between the lower and upper fragments of each positive-radius
chain. Call the resulting object its **paired nonmiddle skeleton**. Such a
skeleton \(\Sigma\) has \(N\) flags

\[
 f=(R_f,U_f),\qquad R_f\in\mathcal L,\qquad
 U_f\in\mathcal U,\qquad R_f\subset U_f,
\tag{10.2}
\]

using every \(R\) and every \(U\) once. If
\(U_f\setminus R_f=\{a_f,b_f\}\), the two possible central members are

\[
 R_f+a_f,\qquad R_f+b_f.
\tag{10.3}
\]

Thus the flag--middle incidence graph is left degree two. A central
completion is a matching saturating every flag; it is not a perfect
matching on all middle sets, because exactly \(D\) middle sets become
singleton chains. After an attainable \(D\)-set singleton leave is fixed,
it is precisely a perfect matching between the flag shore and the
remaining \(N\) middle sets.

Contract each flag vertex to an edge between its two middle candidates.
This gives a simple graph \(G_\Sigma\) on the \(W\) middle sets, with
\(N\) edges. Orient an edge toward the middle set selected by the
completion. The matching condition is exactly

\[
 d^-_{G_\Sigma}(X)\le1\qquad(X\in\mathcal M).
\tag{10.4}
\]

### Theorem 10.1 (exact central-fiber pseudoforest formula)

Let \(\Sigma\) be a realized paired nonmiddle skeleton. Then:

1. \(G_\Sigma\) is a simple, triangle-free pseudoforest. It has exactly
   \(D\) tree components, with isolated vertices included as one-vertex
   trees. Write their vertex counts as \(t_1,\ldots,t_D\), and let \(c\)
   be the number of unicyclic components.
2. The number of central completions over \(\Sigma\) is exactly

   \[
    \boxed{Z(\Sigma)=2^c\prod_{i=1}^D t_i.}
   \tag{10.5}
   \]

3. Let \(\gamma(\Sigma)\) be the number of flag-edges lying on the unique
   core cycles of the unicyclic components. For any fixed attainable
   singleton leave, there are exactly \(2^c\) completions. Two such
   completions differ on an arbitrary union of core cycles. Consequently
   \(\gamma(\Sigma)\) is exactly the maximum number of flags on which two
   same-leave completions can use opposite middle corners.
4. A full opposite-corner paired SCD with the same singleton leave in both
   decompositions exists over \(\Sigma\) if and only if
   \(\gamma(\Sigma)=N\); equivalently, \(G_\Sigma\) is a disjoint union
   of cycles and \(D\) isolated vertices.

#### Proof

One central completion orients every edge with indegree at most one.
Therefore every subgraph has at most as many edges as vertices, so every
connected component is a tree or is unicyclic. Since

\[
 \sum_C(|V(C)|-|E(C)|)=W-N=D,
\]

there are exactly \(D\) tree components.

In a tree on \(t\) vertices, a completion has one unmatched vertex. Once
that root is chosen, every edge is forced to point away from it; hence the
tree contributes exactly \(t\) completions. In a unicyclic component,
every vertex has indegree one. The core cycle has either of its two cyclic
orientations, and every attached tree is then forced to point away from
the core. This proves (10.5).

Fixing the singleton leave fixes the root and hence every orientation in
each tree component. In a unicyclic component the two orientations differ
exactly on its core cycle; attached trees do not change. This proves Item
3. It also shows that using opposite corners on every flag, while
preserving the leave, is possible exactly when every edge is on a core
cycle, proving Item 4.

It remains to justify the first two adjectives in Item 1. Two middle
corners determine their intersection and union, so parallel flag-edges
cannot occur. In a Johnson triangle, the three edges either have a common
rank-\((m-1)\) intersection color or a common rank-\((m+1)\) union color.
The flags of a skeleton use both color layers injectively, so a triangle
is impossible. \(\square\)

### Corollary 10.2 (cyclic-mass entropy inequality)

Every core cycle has length at least four, and therefore

\[
 c\le\frac{\gamma(\Sigma)}4.
\tag{10.6}
\]

The tree components contain at most \(N-\gamma(\Sigma)\) edges in total;
the other noncore edges, if any, are attached to unicyclic components.
Hence AM--GM and (10.1) give the sharper bound

\[
 \prod_{i=1}^D t_i
 \le
 \left(1+\frac{N-\gamma(\Sigma)}D\right)^D
 \le\left(\frac{W}{D}\right)^D=(m+1)^D.
\tag{10.7}
\]

Consequently

\[
 \boxed{
 \log_2 Z(\Sigma)
 \le\frac{\gamma(\Sigma)}4
 +D\log_2\left(1+\frac{N-\gamma(\Sigma)}D\right)
 \le\frac{\gamma(\Sigma)}4+D\log_2(m+1).}
\tag{10.8}
\]

Let \(\mathsf T_m\) be the total number of SCDs of \(B_{2m}\), and let
\(\mathsf K_m\) be the number of realized paired nonmiddle skeletons. Since

\[
 \mathsf T_m=\sum_\Sigma Z(\Sigma),
\tag{10.9}
\]

we obtain the exact forcing inequality

\[
 \boxed{
 \max_\Sigma\gamma(\Sigma)
 \ge
 4\log_2\frac{\mathsf T_m}{\mathsf K_m}
 -4D\log_2(m+1).}
\tag{10.10}
\]

In particular, the central-scale estimate

\[
 \log_2\frac{\mathsf T_m}{\mathsf K_m}
 \ge\frac N4-o(W)
\tag{10.11}
\]

would force a skeleton with

\[
 \gamma(\Sigma)=N-o(W)=W-o(W).
\tag{10.12}
\]

This is a rigorous sufficient skeleton-count criterion for an
almost-everywhere paired central completion. It is one-way: a skeleton
with one very long core cycle has large \(\gamma\) but only one cyclic bit,
so large paired mass need not give a large fiber.

The entropy-chain version is equally exact. If an SCD is uniform and
\(\boldsymbol\Sigma\) is its skeleton, then

\[
 \log_2\mathsf T_m
 =H_2(\boldsymbol\Sigma)
  +\mathbb E\log_2 Z(\boldsymbol\Sigma),
\tag{10.13}
\]

and (10.8) implies

\[
 \boxed{
 \mathbb E\gamma(\boldsymbol\Sigma)
 \ge4H_2(\text{central completion}\mid\boldsymbol\Sigma)
   -4D\log_2(m+1).}
\tag{10.14}
\]

The fiber entropy itself splits exactly. For a fixed skeleton, there are
\(\prod_i t_i\) attainable singleton leaves, and every such leave supports
exactly \(2^c\) completions. Hence

\[
 H_2(\text{completion}\mid\Sigma)
 =\sum_{i=1}^D\log_2t_i+c,
\tag{10.14a}
\]

\[
 H_2(\text{leave}\mid\Sigma)=\sum_{i=1}^D\log_2t_i,
 \qquad
 H_2(\text{completion}\mid\Sigma,\text{leave})=c.
\tag{10.14b}
\]

For a fixed attainable leave \(L\), let
\(\mathcal C_{\Sigma,L}\) be its completion fiber. Then

\[
 \sum_L|\mathcal C_{\Sigma,L}|
       (|\mathcal C_{\Sigma,L}|-1)
 =Z(\Sigma)(2^c-1).
\tag{10.14c}
\]

Two independent uniform members of \(\mathcal C_{\Sigma,L}\) disagree on
each core cycle with probability \(1/2\), and nowhere else. Their expected
opposite-corner Hamming mass is therefore exactly

\[
 \boxed{\frac{\gamma(\Sigma)}2.}
\tag{10.14d}
\]

Choosing the antipodal orientation on every core realizes the maximum
\(\gamma(\Sigma)\). Thus the unconditioned first moment \(Z(\Sigma)\)
mixes leave entropy with cyclic entropy; a leave-conditioned,
distance-weighted pair count is the statistic that directly measures the
paired-SCD resource.

There is also a quantitative typical-skeleton form of (10.10). For fixed
\(0<\delta<1/2\), the number of SCDs lying over skeletons with
\(\gamma(\Sigma)\le N-\delta W\) is at most

\[
 \mathsf K_m\,
 2^{(N-\delta W)/4+D\log_2(m+1)}.
\tag{10.14e}
\]

Consequently, if the hypothetical sharp gap (10.11) holds, their
probability under a uniform SCD is at most

\[
 2^{-\delta W/4+o(W)}.
\tag{10.14f}
\]

This is a genuine counting implication: a near-maximal central entropy
gap would force \(W-o(W)\) cyclic mass not merely for one skeleton, but
with exponentially high SCD-weight. It remains conditional on (10.11).

### 10.1 What Tomon's count does and does not force

Tomon's asymptotic enumeration has logarithmic main scale

\[
 \log_2\mathsf T_m
 =(1+o(1))\,4^m\log_2(2m).
\tag{10.15}
\]

Only this scale, not the inessential normalization inside its lower-order
term, is used here. On the other hand,

\[
 W\sim\frac{4^m}{\sqrt{\pi m}},
 \qquad
 D\log_2(m+1)=o(W),
\tag{10.16}
\]

and (10.8) gives the uniform fiber bound

\[
 1\le Z(\Sigma)
 \le2^{N/4+D\log_2(m+1)}=2^{W/4+o(W)}.
\tag{10.17}
\]

It follows rigorously that

\[
 \mathsf T_m\,2^{-W/4-o(W)}
 \le\mathsf K_m\le\mathsf T_m,
 \qquad
 \log_2\mathsf K_m=\log_2\mathsf T_m+O(W).
\tag{10.18}
\]

Every possible central-fiber regime therefore has exactly the same Tomon
asymptotic (10.15). The leading SCD count is carried by the choice of the
nonmiddle skeleton and is insensitive to a multiplicative
\(2^{\Theta(W)}\) central factor. Thus (10.15), together with the
universal fiber bounds alone, yields no positive lower bound on cyclic
mass and certainly does not imply (10.12). This is an information
limitation, not a nonexistence claim. To use (10.10), one needs an
independent skeleton enumeration resolving

\[
 \log_2\mathsf T_m-\log_2\mathsf K_m
\]

to additive \(o(W)\) and showing that this gap is near \(N/4\). This is the
precise information missing from the entropy argument.

There is a second, orthogonal warning. At the abstract degree-two fiber
level, completion count does not determine cyclic mass. A \(C_4\) with a
long attached tree and one bare long cycle both have two completions, but
their core masses are respectively \(4\) and the full cycle length. This
example is not asserted to be a realizable Boolean skeleton; it proves
only that the matching entropy statistic itself cannot substitute for the
statewise core-mass statistic.

At the opposite extreme, under (10.11) choose a skeleton \(\Sigma\) with

\[
 \log_2 Z(\Sigma)\ge
 \log_2\frac{\mathsf T_m}{\mathsf K_m}
 \ge\frac N4-o(W).
\]

For every such high-fiber skeleton, equations (10.5)--(10.8) force

\[
 c=\frac N4-o(W),
 \qquad
 \gamma=N-o(W),
 \qquad
 \gamma-4c=o(W).
\tag{10.19}
\]

So almost all cyclic mass lies in four-cycles. This gives the desired
paired central mass but \(\Theta(W)\) central Johnson components, before
literal physical-strip validation, rather than the required \(o(W/H)\).
A separate cycle-fusion and chronological-prefix theorem is still
necessary. SCD enumeration can certify central pairing only through the
sharp gap (10.11); it cannot make the later physical shadow conditions
cheap by entropy alone.
