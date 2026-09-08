# PBBS/alternating switches versus the parity complete-mapping lift

Date: 2026-07-26

Method: pure mathematics only.  No web search, finite search, SAT call, or
computer enumeration is used.

## 0. Exact outcome

Write

\[
 E_r=\{p\in\mathbb F_2^r:|p|\equiv0\pmod2\},\qquad
 O_r=\{p\in\mathbb F_2^r:|p|\equiv1\pmod2\}.
\]

The parity complete-mapping gate asks for selectors

\[
 d_p:Q_r\longrightarrow[r]\qquad(p\in E_r)
\]

such that both

\[
 F_p(x)=x\oplus e_{d_p(x)}                                      \tag{0.1}
\]

and

\[
 T_x(p)=p\oplus e_{d_p(x)}                                      \tag{0.2}
\]

are bijective, the former on (Q_r) for every (p), the latter from
(E_r) to (O_r) for every (x).  For the paired-order application one
also needs every (F_p) to be an isometric (C_{2r})-factor and the
aligned multidepth trace codes to be injective, or to have aggregate
collision excess (o(2^{2r})).

The comparison has the following exact resolution.

1.  The PBBS successor is not a cube-neighbour map.  It has a canonical
    neighbour lift only on the two middle ranks of \(Q_{2m+1}\).  An
    individual length-\(2m+1\) wreath lifts there to an isometric
    \(C_{4m+2}\).  Conditional on an exact all-wreath factor, there are
    exactly \(C_m\) such cycles.  The raw canonical PBBS factor may instead
    have components of length \(\ell(2m+1)\), whose lifts are longer and
    need not be isometric.

2.  That central-slab factor cannot remain intact in any full-cube
    neighbour permutation.  Quantitatively, every full extension must make
    at least

    \[
    2\binom{2m}{m-1}
    =\frac{2m}{2m+1}\binom{2m+1}{m}                    \tag{0.3}
    \]

    central vertices boundary-active, affecting at least

    \[
    \left\lceil\frac{m}{2m+1}C_m\right\rceil           \tag{0.4}
    \]

    wreath rows in any chosen all-wreath partition.  Internal alternating
    \(C_8\) switches cannot alter this rank-imbalance obstruction.

3.  If one first had any full cube neighbour permutation (G), the
    diagonal formula

    \[
    d_p(x)=\delta_G(x\oplus p)                         \tag{0.5}
    \]

    would solve every row and column bijectivity equation exactly.  If its
    first \(d\) directions are distinct, every aligned coarse depth-\(d\)
    trace has multiplicity at least \(2^{d-1}\); in general the same proof
    gives \(2^{|J|-1}\), where \(J\) is the direction support.

4.  There is an ownership-only symmetric-chain solution to (0.1)--(0.2).
    Its chains may be labelled noncanonically by a Catalan object and one
    of \(2m+1\) phase labels, but an even context also needs its position
    inside the chain.  Its rows are only two-cycles and its physical lift
    only four-cycles; even its first aligned coarse trace is noninjective.

5.  There is a genuinely context-dependent nonconstant solution with
    isometric long rows: the corrected common-phase (Q_4) braid, inserted
    into the affine double-factor construction below.  It solves every
    (T_x) exactly, but its coarse depth-two trace map is exactly two-to-one.
    A scalable common-order inverse construction also solves all ownership
    equations, but has multiplicity at least (2^{d-2}) at depth (d\ge3).
    More strongly, Theorem 7.3 gives, for every power of two \(r\), an
    exact fixed-relabel pair with \(2^{r/2}/r\) distinct isometric
    doubled-permutation orders, enough to contain a \(C_{r/4}\)-indexed
    library.  It is a positive long-row \(T_x\) solution with enough order
    values for an arbitrary \(C_{r/4}\)-labelling.  Its realized
    depth-\(d\) support count is only
    \(O(r2^d)\), so its trace collision excess is still asymptotically
    maximal once \(d\gg\log r\).

6.  The natural edgewise correspondence in a PBBS alternating \(C_8\)
    trade does not supply the fixed relabelling needed by the affine
    construction: its two endpoint types have different old-to-new
    omitted-label maps.  This alone does not exclude a cleverly oriented
    global successor pair; that orientation-resolved question remains
    open.  Aggregate four-label balance is not a pointwise \(T_x\) theorem.

7.  The exact surviving Catalan gate is a reciprocal full-cube Latin trade:
    construct a full cube factor with changed-entry density
    \(\Omega(1/d)\), satisfying either the fixed-relabel transversal criterion of
    Theorem 6.2 or the nonlinear cocycle conditions of Theorem 8.1.  A bank
    with only (2^r\operatorname{poly}(r)) changed entries is exponentially
    too sparse: at protected depth (d), trace repair requires

    \[
    |R|\ge
    \frac{(1-2^{1-d}-o(1))2^{2r-1}}{d}.               \tag{0.6}
    \]

An exact long-row ownership solution with an arbitrarily
\(C_{r/4}\)-labelled order library is therefore proved, but no structurally
PBBS-derived or Gaussian-depth trace-recovering solution is proved.
The report gives the exact row/column constructions, the exact trace
criteria, and the obstructions just stated.

## 1. Pointwise form of the complete-mapping equations

The first useful fact is that neither a direction census nor aggregate
balance tests the gate.

### Theorem 1.1 (exact row and column tests)

For selectors (d_p(x)), all row maps (F_p) in (0.1) are bijections if
and only if

\[
 \boxed{
 \sum_{i=1}^r
 \mathbf 1_{\{d_p(y\oplus e_i)=i\}}=1
 \quad(p\in E_r,\ y\in Q_r).}                       \tag{1.1}
\]

All column maps (T_x:E_r\to O_r) are bijections if and only if

\[
 \boxed{
 \sum_{i=1}^r
 \mathbf 1_{\{d_{o\oplus e_i}(x)=i\}}=1
 \quad(x\in Q_r,\ o\in O_r).}                       \tag{1.2}
\]

Equivalently, a column collision occurs precisely when there are
(p\in E_r) and distinct (i,j) such that

\[
 d_p(x)=i,qquad
 d_{p\oplus e_i\oplus e_j}(x)=j.                    \tag{1.3}
\]

#### Proof

The only possible preimages of (y) under (F_p) are
(y\oplus e_i).  Such a point is a preimage exactly when its selected
direction is (i), giving (1.1).  Similarly, the only possible preimages
of (o\in O_r) under (T_x) are (o\oplus e_i), giving (1.2).

If two distinct sources collide, write their selected directions as
(i,j).  Equality of their images says

\[
 p\oplus e_i=p'\oplus e_j.
\]

The case (i=j) would give (p=p'); otherwise
(p'=p\oplus e_i\oplus e_j), which is (1.3).  The converse is immediate.
\(\square\)

Thus (T_x) is a perfect matching of the parity cube at every individual
phase (x).  PBBS point-regularity or preservation of the global omitted
label multiset is strictly weaker.

## 2. What PBBS actually supplies

Put

\[
 n=2m+1,qquad \Omega_m=\binom{[n]}m.
\]

Let (sigma:\Omega_m\to\Omega_m) be an oriented odd-graph factor, so
(A\cap\sigma(A)=\varnothing).  Its omitted label is

\[
 \lambda(A)=[n]\setminus(A\cup\sigma(A)).            \tag{2.1}
\]

### Theorem 2.1 (exact PBBS incidence lift)

The odd-graph successor satisfies

\[
 \sigma(A)=\bar A\setminus\{\lambda(A)\}
 =A\oplus(\mathbf1\oplus e_{\lambda(A)}),             \tag{2.2}
\]

and hence

\[
 d_H(A,\sigma(A))=2m=n-1.                             \tag{2.3}
\]

It is therefore not a cube-neighbour map.

It has the following canonical neighbour lift on the middle incidence
slab

\[
 \mathcal M=\binom{[n]}m\sqcup\binom{[n]}{m+1}:
\]

\[
 \widehat\sigma(A)=\overline{\sigma(A)}
 =A\cup\{\lambda(A)\},qquad |A|=m,                  \tag{2.4}
\]

and

\[
 \widehat\sigma(B)=\sigma(\bar B)
 =B\setminus\{\lambda(\bar B)\},qquad |B|=m+1.     \tag{2.5}
\]

This is a neighbour permutation of (mathcal M).

If

\[
 A_0,A_1,\ldots,A_{n-1},A_0                         \tag{2.6}
\]

is a PBBS wreath and its omitted-label word is
(lambda_0,\ldots,\lambda_{n-1}), then its lift is

\[
 A_0,\bar A_1,A_2,\bar A_3,\ldots                    \tag{2.7}
\]

continued for (2n) vertices, with direction word

\[
 \lambda_0\lambda_1\cdots\lambda_{n-1}
 \lambda_0\lambda_1\cdots\lambda_{n-1}.             \tag{2.8}
\]

Because a PBBS wreath uses every omitted label once, this is an isometric
\(C_{2n}\).  An exact all-wreath factor gives exactly

\[
 \frac1n\binom nm=C_m                                \tag{2.9}
\]

such central-slab cycles.  This final count is conditional on an
all-wreath factor.  The canonical PBBS permutation may have components of
length \(\ell n\), and Theorem 2.1 then only asserts the central incidence
lift, not a decomposition into the cycles counted in (2.9).

#### Proof

Two disjoint (m)-sets inside an (n=2m+1) element universe omit one
coordinate, proving (2.2)--(2.3).  Equations (2.4)--(2.5) each toggle the
displayed omitted coordinate.  The lower-to-upper map
(A\mapsto\overline{\sigma(A)}) and the upper-to-lower map
(B\mapsto\sigma(\bar B)) are bijections because (sigma) and
complementation are.  Hence their union is a neighbour permutation.

If (sigma(A_t)=A_{t+1}), then

\[
 A_t\longrightarrow\bar A_{t+1}
\]

toggles (lambda_t), while

\[
 \bar A_{t+1}\longrightarrow A_{t+2}
\]

toggles (lambda_{t+1}).  Since (n) is odd, the first traversal of
the (n) labels ends on the opposite rank and the second returns to the
initial vertex.  This proves (2.7)--(2.8).  The PBBS point-regular wreath
property makes the labels a permutation, proving isometry.  Finally,
(|\Omega_m|/n=C_m).  \(\square\)

### Corollary 2.2 (the maximal literal PBBS extraction is partial)

Let (delta_{\widehat\sigma}) denote the direction in (2.4)--(2.5).  One
may define

\[
 d_p(x)=\delta_{\widehat\sigma}(p\oplus x)            \tag{2.10}
\]

only when \(p\oplus x\in\mathcal M\).  For fixed \(p\), this gives a
neighbour permutation of the translated slab \(p\oplus\mathcal M\), which
has \(2\binom nm\) phases.  For fixed \(x\), it gives a bijection on exactly
\(\binom nm\) even contexts and exactly that many odd outputs.  The covered
fraction of a row or a column is

\[
 \frac{\binom nm}{2^{n-1}}
 \sim\sqrt{\frac8{\pi n}}.                           \tag{2.11}
\]

Thus raw PBBS is a vanishing-density partial Latin system, not a solution
of (0.1)--(0.2) on the full domain.

#### Proof

For fixed \(p\), translation preserves adjacency and the size of the
slab.  For fixed \(x\), the condition \(p\in E_n\) fixes the parity of
\(p\oplus x\), so exactly one of the two middle ranks is available; it has
\(\binom nm\) vertices.  The incidence lift bijects that rank with the
other.  The asymptotic follows from the central binomial coefficient.
\(\square\)

## 3. The central-slab extension obstruction

### Theorem 3.1 (no intact full-cube extension)

No neighbour permutation of (Q_{2m+1}) can agree with
(\widehat\sigma) on all of (mathcal M).

#### Proof

If (mathcal M) remains invariant, its complement splits into the lower
and upper regions.  The lower region

\[
 L=\{y\in Q_{2m+1}:|y|\le m-1\}                     \tag{3.1}
\]

would itself have to admit a neighbour permutation.  Its parity-shore
imbalance is

\[
 \begin{aligned}
 \left|\sum_{k=0}^{m-1}(-1)^k\binom{2m+1}{k}\right|
 &=\binom{2m}{m-1}>0.                                \tag{3.2}
 \end{aligned}
\]

Here the alternating partial-sum identity follows from Pascal's identity:

\[
 \sum_{k=0}^{s}(-1)^k\binom Nk=(-1)^s\binom{N-1}s.
\]

A bipartite graph with unequal shores has no neighbour permutation, since
the restriction from either parity shore to the other would have to be a
bijection.  This contradicts invariance.  \(\square\)

### Theorem 3.2 (quantitative boundary activity)

Set

\[
 W=\binom{2m+1}{m},\qquad
 D=\binom{2m}{m-1}
 =\frac{m}{2m+1}W=mC_m.                              \tag{3.3}
\]

Every full neighbour permutation of (Q_{2m+1}) has at least (D)
distinct rank-(m) vertices incident with its routing between the lower
region and the central slab, and at least (D) distinct rank-((m+1))
vertices incident with its routing between the central slab and the upper
region.  Consequently at least (2D) central vertices are boundary-active.
If the central vertices are initially partitioned into lifted wreaths,
at least

\[
 \left\lceil\frac D{2m+1}\right\rceil
 =\left\lceil\frac{m}{2m+1}C_m\right\rceil           \tag{3.4}
\]

wreaths are affected.  The final row count is conditional on this
all-wreath partition; the \(D\) and \(2D\) boundary-activity bounds are
unconditional.

#### Proof

Apply the bipartite matching equation separately to either directed shore
map of a full neighbour permutation.  Inside (L), the majority shore has
(D) more vertices than the minority shore by (3.2), so at least (D)
matching incidences must cross from (L) to rank (m).  Distinct matching
incidences use distinct rank-(m) vertices.  The two directed shore maps
may reuse those central vertices, but their union still contains at least
(D) distinct ones.  Complementation gives the identical assertion at the
upper boundary.  The two central ranks are disjoint, proving the (2D)
bound.  Each lifted wreath has exactly \(2m+1\) rank-\(m\) vertices,
so (3.4) follows.  \(\square\)

### Corollary 3.3 (same-dimension divisibility obstruction)

For odd (n>1), (Q_n) has no factor all of whose cycles are (C_{2n}),
because such a factor would contain

\[
 \frac{2^n}{2n}=\frac{2^{n-1}}n                     \tag{3.5}
\]

cycles, which is not integral.  Hence the central PBBS (C_{2n})'s cannot
be completed to the row factors required by the paired-order theorem in
the same coarse dimension.

This is a same-dimension obstruction.  It does not rule out encoding PBBS
orders in a larger cube of admissible dimension.

## 4. The universal diagonal solution and its trace gauge

### Theorem 4.1 (diagonal complete mapping)

Let (G:Q_r\to Q_r) be any full neighbour permutation,

\[
 G(y)=y\oplus e_{\delta(y)}.                          \tag{4.1}
\]

Define, for every (p\in E_r),

\[
 d_p(x)=\delta(p\oplus x).                           \tag{4.2}
\]

Then every row and every column is bijective.  More precisely,

\[
 F_p(x)=p\oplus G(p\oplus x),                        \tag{4.3}
\]

and

\[
 T_x(p)=x\oplus G(p\oplus x).                        \tag{4.4}
\]

#### Proof

Equation (4.3) makes (F_p) a translation conjugate of (G).  For fixed
(x), the map (p\mapsto p\oplus x) identifies (E_r) with one parity
shore.  The neighbour permutation (G) bijects that shore to the other,
and final translation by (x) identifies it with (O_r).  This proves
(4.4) and column bijectivity.  \(\square\)

Theorem 4.1 says exactly what would happen if PBBS admitted a full-cube
extension: diagonal extraction would solve ownership automatically.
Theorem 3.1 says the canonical central extension cannot be retained.

### Theorem 4.2 (exact diagonal trace obstruction)

Assume the first (d) directions of the (G)-orbit from

\[
 y=p\oplus x                                             \tag{4.5}
\]

are distinct, and let their support be (J\), (|J|=d\).  In the physical
paired coordinates

\[
 a=x,\qquad b=x\oplus p=y,                              \tag{4.6}
\]

the aligned physical depth-(2d) trace produced by (4.2) has multiplicity
at least

\[
 \boxed{2^{d-1}.}                                      \tag{4.7}
\]

The bound holds for both lower-intersection and upper-union traces and is
independent of any internal trace recovery possessed by (G).

#### Proof

For every even vector (z) supported on (J), put

\[
 p_z=p\oplus z,qquad x_z=x\oplus z.                   \tag{4.8}
\]

Then (p_z\in E_r) and

\[
 p_z\oplus x_z=p\oplus x=y.                            \tag{4.9}
\]

All (2^{d-1}) starts therefore use the identical direction itinerary.
Their (b)-vectors are identical, their (a)-vectors agree outside (J),
and they differ only in (a|_J).  During the (d) completed pair moves,
both physical coordinates (a_j,b_j) are toggled for every (j\in J).
Consequently the lower trace omits both coordinates of every completed
pair and the upper trace contains both, independently of their initial
values.  Outside (J) all starts agree.  Hence all starts in (4.8) have
the same signed physical trace.  \(\square\)

If (N=|E_r||Q_r|=2^{2r-1}) is the number of aligned starts, Theorem 4.2
alone gives collision excess at least

\[
 N-\frac{N}{2^{d-1}}
 =(1-2^{1-d})N.                                       \tag{4.10}
\]

Thus dependence only on the diagonal variable (p\oplus x) is a complete
no-go for Gaussian-depth trace recovery.

## 5. An SCD ownership solution with Catalan-labelled chains

The ownership equation by itself has the following exact symmetric-chain
solution.  Catalan data label its chains only; an even context also needs
its position inside the chain.  This distinction separates a cardinal
Catalan labelling from a Catalan paired-order construction.

### Lemma 5.1 (symmetric-chain perfect matching)

For odd (n=2m+1), the Boolean lattice (Q_n) has a perfect matching

\[
 M:E_n\longrightarrow O_n                               \tag{5.1}
\]

along cube edges.  Its matching chains are indexed by the rank-\(m\)
sets.  Since their number is \(nC_m\), choose any bijective labelling by
pairs

\[
 (D,t),\qquad D\in\mathcal D_m,\quad t\in\mathbb Z_n, \tag{5.2}
\]

where \(|\mathcal D_m|=C_m\).  This labelling is noncanonical unless a
particular exact wreath factor or rotation-quotient bijection is supplied.

#### Proof

For completeness, construct a symmetric-chain decomposition inductively.
Suppose a symmetric chain of (Q_{n-1}) is

\[
 X_k\subset X_{k+1}\subset\cdots\subset X_{n-1-k}.
\]

In (Q_n), replace it by

\[
 X_k\subset\cdots\subset X_{n-1-k}
 \subset X_{n-1-k}\cup\{n\},                          \tag{5.3}
\]

and, when nonempty,

\[
 X_k\cup\{n\}\subset\cdots\subset
 X_{n-2-k}\cup\{n\}.                                 \tag{5.4}
\]

These two chains are disjoint, exhaust the two copies of the original
chain, and are symmetric.  Starting from (Q_0) proves existence for all
(n).

When (n=2m+1), every symmetric chain from rank (k) to rank (n-k)
has

\[
 n-2k+1=2(m-k+1)                                      \tag{5.5}
\]

vertices, an even number.  Pair consecutive vertices in each chain.  This
is a perfect matching between the parity shores.  Every symmetric chain
contains a unique rank-\(m\) set, so the chains are indexed by
\(\binom nm=nC_m\) central sets.  Therefore an arbitrary bijection gives
(5.2).  A matching edge is specified by \((D,t)\) together with the
position of its source inside the corresponding symmetric chain.
\(\square\)

### Theorem 5.2 (ownership-only symmetric-chain solution)

Let (mu(p)) be the direction of the matching edge from (p\in E_n) in
Lemma 5.1, and set

\[
 d_p(x)=\mu(p).                                        \tag{5.6}
\]

Then every (T_x) is the same bijection (M:E_n\to O_n), and every row

\[
 F_p(x)=x\oplus e_{\mu(p)}                             \tag{5.7}
\]

is a neighbour involution.  Thus (0.1)--(0.2) hold exactly.

However, every row cycle has length two, the paired physical lift has
cycles of length four, and the first aligned coarse trace is noninjective:
for fixed (p), the starts (x) and (x\oplus e_{\mu(p)}) have the same
support and the same outside data.  Hence this construction cannot be used
as a (C_{2n})-row or trace-recovery solution.

#### Proof

Equation (5.6) gives (T_x(p)=M(p)), independently of (x).  Toggling a
fixed coordinate is an involution, proving row bijectivity.  The remaining
cycle and trace assertions follow directly from (5.7).  \(\square\)

The chains have Catalan-phase labels, but the contexts require the
additional chain-position coordinate and no PBBS order is used.  This must
not be cited as a Catalan paired-order theorem.

## 6. A nonconstant affine solution and its exact trace criterion

### Theorem 6.1 (affine double-factor lemma)

Let (S\in\operatorname{Sym}([r])), acting as a coordinate permutation
on (Q_r).  Let (G_0,G_1) be neighbour permutations with direction
functions (delta_0,delta_1), and suppose

\[
 \delta_1(y)=S\delta_0(y)\qquad(y\in Q_r).             \tag{6.1}
\]

For (p\in E_r), define

\[
 \boxed{d_p(x)=\delta_0(Sp\oplus x).}                 \tag{6.2}
\]

Then every (F_p) and every (T_x) is bijective.  If (G_0) is an
isometric (C_{2r})-factor, every (F_p) is one also.

#### Proof

Put (y=Sp\oplus x).  Then

\[
 Sp\oplus F_p(x)=G_0(y),                              \tag{6.3}
\]

so each row is an affine conjugate of (G_0).  Moreover,

\[
 ST_x(p)\oplus x
 =y\oplus e_{S\delta_0(y)}
 =G_1(y).                                             \tag{6.4}
\]

As (p) ranges over (E_r), (y=Sp\oplus x) ranges over one parity
shore.  The neighbour permutation (G_1) maps it bijectively to the other,
and the affine map on the left of (6.4) identifies that shore with (O_r).
This proves column bijectivity.  Affine coordinate permutations preserve
cycle length and isometry.  \(\square\)

The next theorem completely audits aligned trace recovery for (6.2).

### Theorem 6.2 (exact affine trace fibres)

Fix a coarse depth (1\le\ell\le r).  For (y\in Q_r), let

\[
 J_\ell(y)=
 \{\delta_0(y),\delta_0(G_0y),\ldots,
   \delta_0(G_0^{\ell-1}y)\}.                         \tag{6.5}
\]

Assume these directions are distinct on the starts under consideration.
For each realized (ell)-set (J), put

\[
 A_J=\{y:J_\ell(y)=J\}.                               \tag{6.6}
\]

Let (V_J\) be the coordinate subspace supported on (J), (V_J^0) its
even-weight subspace, and define

\[
 L_J:V_J\times V_J^0\longrightarrow Q_r,qquad
 L_J(\alpha,\beta)=\alpha\oplus S\beta,               \tag{6.7}
\]

with image (E_J(S)).  For any fixed aligned code

\[
 (J,\ x|_{J^c},\ p|_{J^c}),                           \tag{6.8}
\]

the number of starts producing it is exactly

\[
 \boxed{
 |\ker L_J|\,
 |A_J\cap(y_0+E_J(S))|,}                              \tag{6.9}
\]

where (y_0+E_J(S)) is the affine coset determined by the outside data.
If

\[
 k_J=|J\cap S^{-1}J|,                                 \tag{6.10}
\]

then

\[
 \boxed{|\ker L_J|=2^{\max(k_J-1,0)}.}               \tag{6.11}
\]

Consequently the aligned trace code is injective if and only if, for every
realized (J),

\[
 |J\cap S^{-1}J|\le1                                 \tag{6.12}
\]

and

\[
 |A_J\cap(y+E_J(S))|\le1
 \quad\text{for every }y\in Q_r.                     \tag{6.13}
\]

#### Proof

Fix one representative ((p_0,x_0)) of the outside data.  Every other
representative has

\[
 x=x_0\oplus\alpha,qquad p=p_0\oplus\beta,           \tag{6.14}
\]

where \(\alpha\in V_J\) and \(\beta\in V_J^0\); the even condition on
\(\beta\) is exactly what preserves \(p\in E_r\).  Its coarse starting
point is

\[
 Sp\oplus x
 =Sp_0\oplus x_0\oplus L_J(\alpha,\beta).            \tag{6.15}
\]

It produces support \(J\) exactly when this point belongs to \(A_J\).
Every point in the intersection in (6.9) has exactly
\(|\ker L_J|\) preimages, proving (6.9).

A kernel vector satisfies \(\alpha=S\beta\).  The requirements
\(\alpha\in V_J\) and \(\beta\in V_J\) say that \(\beta\) is supported on
\(J\cap S^{-1}J\), and it must have even weight.  The even subspace on
\(k_J\) coordinates has size \(2^{k_J-1}\) for \(k_J\ge1\), and has one
element for \(k_J=0\).  This proves (6.11).  Finally, (6.9) equals one for
every realized code exactly under (6.12)--(6.13).  \(\square\)

### Corollary 6.3 (universal support-count bound)

Let (mathscr J_\ell) be the realized (ell)-supports.  The aligned
collision excess satisfies

\[
 \boxed{
 \operatorname{CollEx}_\ell
 \ge 2^{2r-1}-|\mathscr J_\ell|\cdot2^{2r-2\ell}.}   \tag{6.16}
\]

Thus near-injectivity requires

\[
 |\mathscr J_\ell|\ge(1-o(1))2^{2\ell-1}.            \tag{6.17}
\]

#### Proof

For fixed (J), the two outside restrictions in (6.8) have at most
(2^{r-\ell}) possibilities each.  Hence (J) contributes at most
(2^{2r-2\ell}) distinct codes.  Subtract their total from the
(2^{2r-1}) starts.  \(\square\)

## 7. Exact tests on the common-phase (Q_4) braid

The corrected braid has two (C_8)-factors (G_0,G_1) on (Q_4).  A
common phase colouring (c(a_j)=c(b_j)=j\pmod8) gives direction tables

\[
\begin{array}{c|cccccccc}
j&0&1&2&3&4&5&6&7\\ \hline
\delta_0&1&2&3&4&1&2&3&4\\
\delta_1&1&4&3&2&1&4&3&2.
\end{array}                                           \tag{7.1}
\]

The vertices are

\[
\begin{array}{c|cccccccc}
j&0&1&2&3&4&5&6&7\\ \hline
a_j&0000&1000&1100&1110&1111&0111&0011&0001\\
b_j&0101&1101&1001&1011&1010&0010&0110&0100.
\end{array}                                           \tag{7.2}
\]

The (G_0)-cycles are the two rows of (7.2).  The (G_1)-cycles are

\[
 (a_0,a_1,b_2,b_3,a_4,a_5,b_6,b_7)                   \tag{7.3}
\]

and

\[
 (b_0,b_1,a_2,a_3,b_4,b_5,a_6,a_7).                  \tag{7.4}
\]

With

\[
 S=(2\ 4),                                            \tag{7.5}
\]

one has (delta_1=S\delta_0) at every vertex.

### Theorem 7.1 (a genuine nonconstant (T_x) solution)

The selector

\[
 \boxed{d_p(x)=\delta_0(Sp\oplus x)}                 \tag{7.6}
\]

solves every row and column equation for (r=4).  Every row is an
isometric (C_8)-factor.  Its aligned coarse depth-one trace code is
injective, but its depth-two trace code is exactly two-to-one.

At depth two the support classes are

\[
\begin{array}{c|c}
J&A_J\\ \hline
12&\{a_0,b_0,a_4,b_4\}\\
23&\{a_1,b_1,a_5,b_5\}\\
34&\{a_2,b_2,a_6,b_6\}\\
41&\{a_3,b_3,a_7,b_7\}.
\end{array}                                           \tag{7.7}
\]

Moreover,

\[
 E_{12}=E_{41}=\langle e_1,e_2,e_4\rangle,qquad
 E_{23}=E_{34}=\langle e_2,e_3,e_4\rangle.            \tag{7.8}
\]

Each (A_J) has two points in each of the two corresponding cosets.
Hence all (64) possible depth-two codes occur, each exactly twice, among
the (8\cdot16=128) starts; the collision excess is exactly (64).

#### Proof

The row and column statements follow from Theorem 6.1 and (7.1)--(7.5).
At depth one, a support class (A_{\{i\}}) cannot contain both endpoints
of an (i)-edge: that would make the neighbour permutation (G_0) contain
a directed two-cycle on that edge, contrary to its (C_8)-cycles.  The
depth-one instance of Theorem 6.2 is therefore injective.

Reading two consecutive directions in (7.1) gives (7.7).  Applying (6.7)
with (S=(2\ 4)) gives (7.8).  Directly from the displayed strings in
(7.2), the two cosets in the first pair are distinguished by bit (3),
and those in the second pair by bit (1); every listed (A_J) has two
vertices of each value.  Formula (6.9) now gives multiplicity two.  The
start and code counts follow.  \(\square\)

Thus the \(Q_4\) braid is a nontrivial ownership seed, but not a
half-depth trace-rainbow seed.

### Theorem 7.2 (scalable common-order solution and exact failure)

For every power of two \(r\ge4\), let \(G_0\) be a common-order isometric
\(C_{2r}\)-factor with word \(\pi\pi\).  Let \(S\) send each direction of
\(\pi\) to its cyclic predecessor, and put \(G_1=G_0^{-1}\).  Then
\(\delta_1=S\delta_0\), so (6.2) gives a genuinely context-dependent
solution of every row and column equation.

For an \(\ell\)-window support

\[
 J=\{\pi_t,\ldots,\pi_{t+\ell-1}\},                  \tag{7.9}
\]

for \(1\le\ell<r\), one has

\[
 |J\cap S^{-1}J|=\ell-1.                             \tag{7.10}
\]

At \(\ell=r\), \(J=[r]\) and the intersection has size \(r\).
Consequently every aligned code has multiplicity at least

\[
 \boxed{2^{\ell-2}\quad(\ell\ge3),}                  \tag{7.11}
\]

and collision excess at least

\[
 (1-2^{2-\ell})2^{2r-1}.                             \tag{7.12}
\]

At \(\ell=r\), the stronger respective bounds are \(2^{r-1}\) and
\((1-2^{1-r})2^{2r-1}\).

Conversely, suppose \(G_1=G_0^{-1}\) and one fixed \(S\) obeys
\(\delta_1=S\delta_0\).  If \(a_t\) is the outgoing direction at phase
\(t\) on a \(G_0\)-cycle, then

\[
 a_{t-1}=Sa_t.                                       \tag{7.13}
\]

If the cycle is an isometric \(C_{2r}\), \(S\) is one \(r\)-cycle on the
directions and every factor cycle has the same cyclic order up to rotation.
Thus the inverse-factor construction cannot carry genuinely varying
Catalan/PBBS orders.

#### Proof

The common-order factor exists for every \(r=2^t\).  To see this
directly, enumerate \(\mathbb F_2^t\) as
\(g_0=0,g_1,\ldots,g_{r-1}\), and define the linear syndrome map
\(\phi:\mathbb F_2^r\to\mathbb F_2^t\times\mathbb F_2\) by
\[
 \phi(e_j)=(g_j+g_{j-1},0)\quad(1\le j<r),\qquad
 \phi(e_r)=(g_{r-1},1).                               \tag{7.14}
\]
The successive prefixes of the word \(1,2,\ldots,r,1,2,\ldots,r\)
have syndromes
\[
 (g_0,0),(g_1,0),\ldots,(g_{r-1},0),
 (g_0,1),\ldots,(g_{r-1},1),                          \tag{7.15}
\]
which are all distinct and exhaust the quotient.  The translates by
\(\ker\phi\) of this base \(C_{2r}\) are therefore disjoint and exhaust
\(Q_r\).  The doubled-permutation word makes them isometric.

The selector is genuinely context-dependent.  If \(v_t\) is a phase-\(t\)
vertex of a \(G_0\)-cycle, then
\[
 v_t\oplus v_{t+2}=e_{\pi_t}\oplus e_{\pi_{t+1}}\in E_r.
 \tag{7.16}
\]
At \(x=v_t\), compare \(p=0\) with
\[
 p'=S^{-1}(v_t\oplus v_{t+2}).
\]
The corresponding coarse starting points are \(v_t\) and \(v_{t+2}\), so
their selected directions are \(\pi_t\) and \(\pi_{t+2}\), which are
distinct for \(r\ge4\).

On a \(G_0\)-cycle, the outgoing direction of the inverse permutation is
the preceding \(G_0\)-direction, proving (7.13).  The common-order
construction therefore satisfies (6.1).  For \(1\le\ell<r\), all but one
direction of the interval (7.9) remain after intersecting with its
one-step shift, proving (7.10).  At \(\ell=r\), the support is all of
\([r]\).  Equations (6.11) and (6.9) give the stated multiplicities;
grouping \(N\) starts by fibres gives the collision bounds.

In the converse direction, the first \(r\) directions on an isometric
\(C_{2r}\) are distinct.  Recurrence (7.13) therefore makes them a complete
orbit of one \(r\)-cycle \(S\).  Every cycle follows this same orbit, up to
its initial phase.  \(\square\)

### Theorem 7.3 (paired-syndrome order library of Catalan cardinality)

For every power of two \(r=2^t\ge4\), there are two neighbour
permutations \(G_0,G_1\) of \(Q_r\) and one coordinate involution \(S\)
such that:

1. \(\delta_1(y)=S\delta_0(y)\) for every \(y\);
2. both \(G_0\) and \(G_1\) are factors into isometric \(C_{2r}\)'s;
3. with the common quotient phase \(0\) as root, the \(G_0\)-cycles
   realize exactly

   \[
   2^{r/2-t}=\frac{2^{r/2}}r                         \tag{7.17}
   \]

   distinct oriented, phase-rooted doubled-permutation direction words for
   a suitable choice of the construction parameters; and
4. those words contain a sublibrary indexed by the Catalan family
   \(\mathcal D_{r/4}\), because

   \[
   C_{r/4}\le\frac{2^{r/2}}r.                        \tag{7.18}
   \]

Consequently

\[
 \boxed{d_p(x)=\delta_0(Sp\oplus x)}                 \tag{7.19}
\]

is an exact, genuinely context-dependent solution of every row and column
equation, with isometric \(C_{2r}\) rows and an order library large enough
for an arbitrary \(C_{r/4}\)-labelling.

This is a solution of the concrete long-row \(T_x\) gate.  It is not a
trace solution: at every depth \(1\le\ell\le r\),

\[
 |\mathscr J_\ell|
 \le r\min\{2^\ell,2^{r/2-t}\}
 \le r\,2^\ell,                                      \tag{7.20}
\]

and therefore its aligned collision excess obeys

\[
 \boxed{
 \operatorname{CollEx}_\ell
 \ge
 2^{2r-1}\left(1-\frac{2r}{2^\ell}\right).}          \tag{7.21}
\]

In particular, if \(\ell/\log_2r\to\infty\), the collision excess is
\((1-o(1))2^{2r-1}\).  The construction proves that exact ownership is
compatible with an order library large enough for arbitrary Catalan
labelling, while isolating multidepth support entropy as the remaining
failure.

The Catalan indexing in item 4 is an injection into a syndrome-generated
swap library.  These are not asserted to be the actual PBBS/MSW order
words, and the construction is not an extraction of the PBBS central-slab
successor.

#### Proof: the quotient phase path

Let

\[
 g_0,g_1,\ldots,g_{r-1}                              \tag{7.22}
\]

be the reflected binary Gray Hamilton path through \(\mathbb F_2^t\),
starting at \(g_0=0\) and ending at one basis vector \(g_{r-1}=e_*\).
Its transition multiset has the following parity property:

* the direction \(e_*\) occurs an odd number of times, in fact once;
* every other Gray direction occurs an even number of times.

This follows inductively from the reflected construction: the new
coordinate occurs once at the join, while every old transition list is
traversed twice.

Put \(\Gamma=\mathbb F_2^t\times\mathbb F_2\), and define \(r\) quotient
increments

\[
 \eta_j=(g_j\oplus g_{j-1},0)\quad(1\le j<r),
 \qquad
 \eta_r=(g_{r-1},1).                                 \tag{7.23}
\]

Their prefix sums are

\[
 (g_0,0),(g_1,0),\ldots,(g_{r-1},0),(0,1).           \tag{7.24}
\]

Repeating the same increment list translates the first \(r\) prefix
states by \((0,1)\).  Thus the \(2r=|\Gamma|\) cyclic prefix states are
all distinct.

Assign the \(r\) physical cube coordinates bijectively to the \(r\)
positions in (7.23); write the resulting first-half coordinate word as

\[
 \pi_1,\ldots,\pi_r.                                 \tag{7.25}
\]

Define a surjective linear map

\[
 \phi:\mathbb F_2^r\longrightarrow\Gamma,\qquad
 \phi(e_{\pi_j})=\eta_j,                              \tag{7.26}
\]

and put \(K=\ker\phi\).  Then

\[
 \dim K=r-t-1.                                       \tag{7.27}
\]

By the parity property above, exactly two values in the multiset
\(\{\eta_1,\ldots,\eta_r\}\) have odd multiplicity: the singleton Gray
increment \(e_*\) and the final increment with last coordinate one.  Pair
the coordinate positions having each other common increment value.  Let
\(S\) swap the two coordinates in every pair and fix the two singleton
coordinates.  Hence

\[
 \phi(e_i)=\phi(e_{Si})\qquad(i\in[r]).               \tag{7.28}
\]

For every transposition orbit \(s=\{i,Si\}\), put

\[
 u_s=e_i\oplus e_{Si}.                               \tag{7.29}
\]

The vectors \(u_s\) have disjoint supports, lie in \(K\) by (7.28), and
are independent.  If \(U\) is their span, then

\[
 \dim U=\frac{r-2}{2},\qquad
 \dim(K/U)=\frac r2-t.                               \tag{7.30}
\]

#### Proof: the two exact factors

Let

\[
 w_0=0,\qquad
 w_j=e_{\pi_1}\oplus\cdots\oplus e_{\pi_j}
 \quad(1\le j\le r),                                 \tag{7.31}
\]

and extend by \(w_{r+j}=w_r\oplus w_j\).  The phase classes

\[
 \mathcal C_j=w_j+K,\qquad j\in\mathbb Z_{2r},        \tag{7.32}
\]

partition \(Q_r\), because their \(\phi\)-images are the \(2r\) distinct
prefix states from (7.24) and its translate.

For each transposition orbit \(s\), choose an arbitrary bit function

\[
 b_s:K/U\longrightarrow\mathbb F_2.                  \tag{7.33}
\]

At a vertex \(y=w_j\oplus k\in\mathcal C_j\), let the scheduled base
coordinate be

\[
 i_j=\pi_{(j\bmod r)+1}.                              \tag{7.34}
\]

If \(i_j\) is fixed by \(S\), set \(\delta_0(y)=i_j\).  Otherwise let \(s\)
be its transposition orbit and set

\[
 \delta_0(y)=S^{\,b_s(k+U)}i_j,\qquad
 \delta_1(y)=S\delta_0(y).                            \tag{7.35}
\]

Equation (7.28) shows that either selected direction moves
\(\mathcal C_j\) to \(\mathcal C_{j+1}\).

Relative to the representatives \(w_j,w_{j+1}\), the \(G_0\)-map on the
fibre \(K\) is

\[
 P_s(k)=k\oplus b_s(k+U)u_s                          \tag{7.36}
\]

at either occurrence of the orbit \(s\), and is the identity at a fixed
coordinate.  Since \(b_s\) depends only on \(k+U\), every \(P_s\) is an
involution.  All \(P_s\)'s commute: each changes \(k\) by an element of
\(U\), so none changes any bit \(b_{s'}(k+U)\).  Every transposition orbit
occurs exactly twice among the first \(r\) positions, so its \(P_s\) is
applied twice.  The first-half fibre monodromy is therefore the identity.
The same is true in the repeated second half.

For \(G_1\), the corresponding fibre map is

\[
 P'_s(k)=k\oplus(1-b_s(k+U))u_s.                     \tag{7.37}
\]

These maps are again commuting involutions, each used twice per half, so
the \(G_1\) monodromy is also the identity.

Every orbit advances through the \(2r\) distinct quotient phases before
returning, so both factors have cycles of length exactly \(2r\).  In the
first half, each transposition orbit contributes its two coordinates once
each: changing \(b_s\) merely swaps their two phase positions.  The two
fixed coordinates also occur once.  Since the fibre coset \(k+U\) is
unchanged along the cycle, the second half repeats the first-half order.
Thus every direction word is \(\rho\rho\) for a permutation \(\rho\) of
\([r]\), proving isometry.  Equation (7.35) gives
\(\delta_1=S\delta_0\), so Theorem 6.1 proves (7.19).

The selector in (7.19) genuinely depends on \(p\).  Take any cycle vertex
\(y\) and put \(y'=G_0^2(y)\).  The vector \(y\oplus y'\) has even weight,
so
\[
 p'=S^{-1}(y\oplus y')\in E_r.
\]
At the common phase input \(x=y\), the contexts \(p=0\) and \(p=p'\)
produce coarse starts \(y\) and \(y'\).  Their outgoing directions are
distinct because the \(G_0\)-cycle is isometric and the two phases differ
by two, proving nonconstant context dependence.

#### Proof: order count and Catalan injection

Choose the vector map

\[
 B=(b_s)_s:K/U\longrightarrow
 \mathbb F_2^{(r-2)/2}                               \tag{7.38}
\]

to be linear and injective; this is possible by (7.30).  Distinct values
of \(B\) swap different subsets of the coordinate pairs in (7.25), and
hence give distinct oriented words rooted at common phase \(0\).  There
are exactly

\[
 |K/U|=2^{r/2-t}=\frac{2^{r/2}}r
\]

such values, proving (7.17).

Put \(s=r/4\).  The elementary induction

\[
 \frac{4^{s+1}}{\binom{2s+2}{s+1}}
 =
 \frac{4^s}{\binom{2s}s}\,
 \frac{2(s+1)}{2s+1}                                 \tag{7.39}
\]

starting at \(s=1\) proves

\[
 \binom{2s}s\le
 4^s\frac{s+1}{4s}.                                  \tag{7.40}
\]

Indeed, if the reciprocal central-binomial ratio is at least
\(4s/(s+1)\), multiplication by \(2(s+1)/(2s+1)\) makes it at least
\(4(s+1)/(s+2)\), since \(s\ge1\).  Dividing (7.40) by \(s+1\) gives

\[
 C_s\le\frac{4^s}{4s}.                               \tag{7.41}
\]

For \(s=r/4\), the right side is \(2^{r/2}/r\), proving (7.18).
Select any injection of \(\mathcal D_{r/4}\) into the order values of
\(B\).

#### Proof: trace-support obstruction

At a fixed cyclic phase, each one of the \(\ell\) scheduled coordinate
positions has at most two possible labels, namely \(i\) and \(Si\).
Hence varying all cycle fibres produces at most \(2^\ell\) support sets
from that phase, and never more than the total \(2^{r/2-t}\) order values.
Phases \(j\) and \(j+r\) have identical direction windows because every
word is doubled.  Thus only \(r\) distinct phase positions contribute,
proving (7.20).  Substitute (7.20) into Corollary 6.3:

\[
\begin{aligned}
 \operatorname{CollEx}_\ell
 &\ge
 2^{2r-1}-(r\,2^\ell)2^{2r-2\ell}\\
 &=2^{2r-1}\left(1-\frac{2r}{2^\ell}\right).
\end{aligned}
\]

This proves (7.21) and the theorem. \(\square\)

## 8. Nonlinear translation offsets and reciprocal Latin trades

The fixed-relabel construction is not the only way to solve the columns.
The next theorem states an exact nonlinear gate.

### Theorem 8.1 (translation-offset cocycle criterion)

Let (G(y)=y\oplus e_{\delta(y)}) be a neighbour permutation, and put

\[
 V_i=\{y\in Q_r:\delta(y)=i\}.                        \tag{8.1}
\]

For an arbitrary map (alpha:E_r\to Q_r), define

\[
 d_p(x)=\delta(x\oplus\alpha(p)).                     \tag{8.2}
\]

Every row (F_p) is a translation conjugate of (G).  Every column is
bijective if and only if

\[
 \boxed{
 \alpha(p)\oplus\alpha(p\oplus e_i\oplus e_j)
 \notin V_i\oplus V_j}                               \tag{8.3}
\]

for every (p\in E_r) and every pair (i\ne j).

If (J) is a realized depth-(d) support, a necessary condition for
aligned trace injectivity is

\[
 \boxed{
 \bigl(\alpha(p)\oplus\alpha(p\oplus u)\bigr)|_{J^c}
 \ne0}                                                \tag{8.4}
\]

for every nonzero even (u) supported on (J).

Condition (8.4) is only necessary: collisions with distinct coarse starts
may impose additional conditions.

#### Proof

Translation conjugacy gives row bijectivity.  By Theorem 1.1, a possible
column collision has sources (p) and
(p'=p\oplus e_i\oplus e_j), selecting (i,j).  Set
(y=x\oplus\alpha(p)).  The two direction conditions are

\[
 y\in V_i,qquad
 y\oplus\alpha(p)\oplus\alpha(p')\in V_j.             \tag{8.5}
\]

There exists an (x), equivalently a (y), satisfying (8.5) exactly when
(alpha(p)\oplus\alpha(p')\in V_i\oplus V_j).  This proves (8.3).

For (8.4), suppose instead that the displayed difference is supported on
(J).  Take (p'=p\oplus u) and choose

\[
 x'=x\oplus\alpha(p)\oplus\alpha(p').                \tag{8.6}
\]

Then (x'\oplus\alpha(p')=x\oplus\alpha(p)), so the two starts have the
same coarse orbit and support (J).  Since both (u) and (x\oplus x')
are supported on (J), their (p)- and (x)-restrictions outside (J)
also agree.  Their aligned codes coincide, a contradiction.  \(\square\)

### Lemma 8.2 (literal reciprocal rectangle)

Suppose a direction array (d(p,x)) already satisfies every row and column
bijection.  Let

\[
 p_1=p_0\oplus e_i\oplus e_j,qquad
 x_1=x_0\oplus e_i\oplus e_j                         \tag{8.7}
\]

with (i\ne j), and suppose all four entries

\[
 d(p_a,x_b),\qquad a,b\in\{0,1\},                    \tag{8.8}
\]

equal (i).  Replacing all four entries in (8.8) by (j) preserves every
row and column bijection.

#### Proof

In either affected row, the two old targets of (x_0,x_1) are
(x_0\oplus e_i) and (x_0\oplus e_j).  Changing (i) to (j) swaps
them.  In either affected column, the two old targets of (p_0,p_1) are
(p_0\oplus e_i) and (p_0\oplus e_j); these too are swapped.  No other
entry changes.  \(\square\)

### Corollary 8.3 (conditional full context entropy is compatible with ownership)

Start from a context-independent array (d^0_p(x)=\delta(x)).  Suppose
(x_1=x_0\oplus u), (u=e_i\oplus e_j), and
(delta(x_0)=\delta(x_1)=i).  Activate the (i\to j) two-entry row
switch for precisely those contexts with (b(p)=1), where

\[
 b(p)=b(p\oplus u).                                   \tag{8.9}
\]

Then all rows and columns remain bijective.  Pairwise entry-disjoint
\(x\)-squares commute.  For a square of displacement \(u_s\), every linear
activation bit \(b_s(p)=\ell_s(p)\) with \(\ell_s(u_s)=0\) is legal.
Consequently, if the base factor contains at least \(r-1\) pairwise
entry-disjoint suitable squares and one can choose
\[
 \ell_s\in u_s^\perp
 \quad\text{with}\quad
 \langle\ell_s:s\rangle=E_r^*,                       \tag{8.10}
\]
their activation signatures encode all \(r-1\) independent context bits.
For overlapping squares, (8.10) is not enough and a separate joint
compatibility proof is required.  Existence of either kind of square bank
is an additional geometric hypothesis; it is not asserted for arbitrary
\(G\).

Under the stated square-supply hypothesis, this shows that the pointwise
Latin equations themselves do not impose a context-entropy obstruction.
The corollary does not prove that a given cube factor supplies that square
bank, that the switched rows remain one \(C_{2r}\)-factor, that they remain
isometric, or that they recover traces.

#### Proof

Condition (8.9) makes the active context set a union of the reciprocal
\(u\)-pairs in Lemma 8.2.  Apply that lemma to each pair.  Linear forms
annihilating a prescribed nonzero even \(u\) form a codimension-one dual
subspace.  The explicit choice in (8.10), one form per entry-disjoint
square, gives the asserted spanning family.
\(\square\)

## 9. What a PBBS alternating \(C_8\) does and does not prove

Every simple alternating (C_8) in (KG(2m+1,m)) has four-label normal
form.  With inactive cores (X,Y) and a directed four-cycle (sigma) on
(A=\{a,b,c,d\}), its two matchings are

\[
 M_\sigma\quad\text{and}\quad M_{\sigma^{-1}},        \tag{9.1}
\]

where the edge incident with

\[
 X_u=X\cup\{u\}                                      \tag{9.2}
\]

in (M_\sigma) omits (sigma(u)).

### Proposition 9.1 (endpoint-dependent edgewise relabelling)

Under the switch (M_\sigma\leftrightarrow M_{\sigma^{-1}}), the
old-to-new omitted-label map at an (X)-endpoint is

\[
 i\longmapsto\sigma^{-2}(i),                          \tag{9.3}
\]

whereas at the corresponding (Y)-endpoint it is

\[
 i\longmapsto\sigma^{-1}(i).                          \tag{9.4}
\]

Consequently the natural correspondence between the replaced undirected
matching edges does not furnish a single coordinate permutation \(S\).

#### Proof

At (X_u), the old omitted label is (i=\sigma(u)), while the reverse
matching omits (sigma^{-1}(u)=\sigma^{-2}(i)).  The old (Y)-endpoint
omits the pair ({u,\sigma(u)}).  In the reverse matching the same
endpoint is indexed by (v=\sigma(u)), and its new omitted label is
(sigma^{-1}(v)=u=\sigma^{-1}(i)).  The two maps differ.  \(\square\)

An oriented successor factor uses the replaced matching edge as the
outgoing edge at only one endpoint; at the other endpoint that edge may be
incoming, and the retained edge may be outgoing.  Proposition 9.1 therefore
does **not** rule out every possible orientation of globally reconnected
old and new factors satisfying (6.1).  It proves only that the local
undirected edge correspondence supplies no fixed \(S\).  Preservation of
one copy of each label is an aggregate ledger and does not imply column
bijectivity; an orientation-resolved global proof would still be required.

The following exact hybrid criterion makes the failure more explicit.

### Theorem 9.2 (alternating-component criterion for context switches)

Let (H^0,H^1) be full neighbour permutations of (Q_r), with direction
functions (delta^0,delta^1), and let
\(\varepsilon:E_r\to\{0,1\}\).  Define

\[
 d_p(x)=\delta^{\varepsilon(p)}(p\oplus x).            \tag{9.5}
\]

Every row is legal.  Fix (x) and put (S_x=x\oplus E_r).  The two
restrictions of (H^0,H^1) from (S_x) to the opposite parity shore are
perfect matchings.  Their union is a disjoint union of shared edges and
alternating even cycles.  The column (T_x) is bijective if and only if

\[
 y\longmapsto\varepsilon(y\oplus x)                   \tag{9.6}
\]

is constant on the source vertices of every nontrivial alternating cycle.

#### Proof

On one alternating component, index sources and targets so that

\[
 H^0(y_i)=z_i,qquad H^1(y_i)=z_{i+1}.                \tag{9.7}
\]

Write \(\varepsilon_i=\varepsilon(y_i\oplus x)\).  The chosen hybrid gives
(z_i) exactly

\[
 (1-\varepsilon_i)+\varepsilon_{i-1}                 \tag{9.8}
\]

preimages.  This equals one for every (i) exactly when
\(\varepsilon_i=\varepsilon_{i-1}\) around the whole component.  Shared
edges impose no condition.  \(\square\)

In particular, changing one factor in only one context row destroys at
least one column: an old target becomes a hole and the new target duplicates
its unchanged predecessor.  Making the identical switch in every context
passes the column test but returns to diagonal dependence and Theorem 4.2.

## 10. The density cost of repairing the diagonal trace gauge

### Theorem 10.1 (changed-entry lower bound)

Let a base direction array have every row \(F_p\) a permutation.  On its
\(N=2^{2r-1}\) aligned starts, suppose every coarse depth-\(d\) trace fibre
has size at least \(2^{d-1}\).  Let \(R\) be the set of direction-array
entries changed in a new array.  If the new depth-\(d\) collision excess
is \(o(N)\), then

\[
 \boxed{
 |R|\ge
 \frac{(1-2^{1-d}-o(1))N}{d}.}                       \tag{10.1}
\]

If the changes are made by four-entry reciprocal rectangles, their number
is at least

\[
 \boxed{
 \frac{(1-2^{1-d}-o(1))2^{2r-1}}{4d}.}               \tag{10.2}
\]

#### Proof

Call a start untouched if none of the (d) base array entries in its
depth-(d) window belongs to (R).  Two untouched starts from the same
base trace fibre follow their unchanged base itineraries and still have the
same trace.  Therefore, apart from the (o(N)) collision excess, at most
one start from each base fibre may be untouched.  Since the number of base
fibres is at most (N/2^{d-1}), at least

\[
 (1-2^{1-d}-o(1))N                                   \tag{10.3}
\]

starts must be touched.  One changed array entry belongs to at most (d)
depth-(d) windows in its row, proving (10.1).  A reciprocal rectangle
changes four entries, proving (10.2).  \(\square\)

At \(d=\Theta(\sqrt r)\), the required scale is
\(\Theta(2^{2r}/\sqrt r)\).  Consequently an unreplicated bank with only
\(2^r\operatorname{poly}(r)\) changed entries is exponentially too sparse.
The theorem proves total changed-entry density \(\Omega(1/d)\).  Since one
context row contains \(2^r\) entries, it also forces at least
\[
 (1-o(1))\,\frac{2^{r-1}}d                            \tag{10.4}
\]
affected context rows, but without a per-row change cap it does not force
almost every context row to be affected.

## 11. Catalan census and the exact surviving fixed-relabel gate

The cardinal identity

\[
 nC_m=\binom nm                                      \tag{11.1}
\]

allows the central \(m\)-sets to be labelled by \(C_m\) Catalan objects
and \(n=2m+1\) phase labels.  This is a set-theoretic labelling, not a claim
that the canonical PBBS factor has \(C_m\) wreath components.  The parity
context shore has size

\[
 |E_n|=2^{n-1}=4^m,                                  \tag{11.2}
\]

and therefore

\[
 \frac{|E_n|}{nC_m}
 =\frac{4^m}{\binom{2m+1}{m}}
 \sim\frac{\sqrt{\pi m}}2.                           \tag{11.3}
\]

Thus a Catalan label plus one of \(n\) phases under-indexes all parity
contexts by a \(\Theta(\sqrt m)\) factor; an additional
height/flaw/SCD-position coordinate is needed.  The abstract family of
\(C_m\) Catalan labels has exponentially more entropy than the
\(O(\sqrt n)\) bits erased by one Gaussian-depth window; whether a
particular exact factor realizes those labels as suitably distinct order
types is an additional structural question.  The obstruction identified
here is exact full-cube matching and trace transversality, not merely the
raw number of labels.

Theorem 7.3 closes the fixed-relabel ownership part with a
\(C_{r/4}\)-labelled order library, but fails the support-count test by an
exponential factor at Gaussian depth.  The cleanest remaining positive
target is therefore the following strengthened finite theorem.

### Open Gate 11.1 (Catalan trace-rainbow fixed-relabel mate)

Construct, in an admissible coarse dimension (r), a full cube factor

\[
 G_0(y)=y\oplus e_{\delta_0(y)}                       \tag{11.4}
\]

whose cycles carry a growing Catalan-indexed family of doubled orders,
together with one coordinate permutation (S), such that

\[
 G_1(y)=y\oplus e_{S\delta_0(y)}                      \tag{11.5}
\]

is also a neighbour permutation.  Pointwise, (11.5) is equivalent to

\[
 \boxed{
 \sum_{i=1}^r
 \mathbf1_{\{\delta_0(z\oplus e_i)=S^{-1}i\}}=1
 \quad(z\in Q_r).}                                   \tag{11.6}
\]

For exact pointwise trace injectivity at every protected depth \(\ell\),
it must additionally satisfy

\[
 |J\cap S^{-1}J|\le1,                                \tag{11.7}
\]

\[
 |A_J\cap(y+E_J(S))|\le1,                            \tag{11.8}
\]

and

\[
 |\mathscr J_\ell|\ge2^{2\ell-1}.                    \tag{11.9}
\]

Equations (11.6)--(11.8) are exact necessary and sufficient
ownership/trace conditions for the affine family (6.2).  Equation (11.9)
is a redundant necessary support-count consequence.

For the aggregate relaxation, let \(c\) range over distinct aligned code
values and let \(J(c)\) and \(y_c+E_{J(c)}(S)\) denote its support and
associated coset.  The exact condition is
\[
 \boxed{
 \sum_c
 \left(
 |\ker L_{J(c)}|\,
 |A_{J(c)}\cap(y_c+E_{J(c)}(S))|-1
 \right)_+
 =o(2^{2r}).}                                        \tag{11.10}
\]
Equivalently, one may delete exceptional starts and form trimmed sets
\(A'_J\subseteq A_J\), but the deletion must be charged with multiplicity
and the coset-transversal condition must be imposed on the trimmed sets.
Merely saying that the untrimmed conditions fail on few supports or cosets
is not sufficient.

Alternatively, a nonlinear Catalan construction may solve (8.3)--(8.4)
using a dense system of reciprocal rectangles.  The density must obey
Theorem 10.1, and the final rows must still be proved to be integral
isometric (C_{2r})-factors.

Raw PBBS supplies none of (11.6)--(11.10) on a full cube.  Its
central-slab factor, its alternating-\(C_8\) legality, and its
omitted-label balance do not imply them.

## 12. Precise proved/conditional boundary

The following statements are proved without qualification.

* Raw PBBS gives an exact central-slab neighbour permutation and no direct
  full-cube selector \(d_p(x)\).  Each wreath component lifts isometrically;
  the count \(C_m\) of such cycles is conditional on an all-wreath factor.
* Preserving that slab in a full extension is impossible, with exact
  boundary-activity constants (3.3)--(3.4).
* Diagonal extraction from any full cube factor solves both row and column
  bijectivity.  On a window with distinct support \(J\) it has the
  \(2^{|J|-1}\) trace gauge, in particular \(2^{d-1}\) for an isometric
  depth-\(d\) window.
* A symmetric-chain matching gives an exact solution of the literal
  \(T_x\) gate, with Catalan-labelled chains plus a chain-position
  coordinate, but only involution rows and noninjective traces.
* The affine double-factor lemma gives nonconstant long-row solutions; the
  (Q_4) seed is exactly two-to-one at depth two, and the scalable
  common-order inverse family has exponential multidepth trace fibres.
* The paired-syndrome construction gives an exact \(C_{r/4}\)-labelled
  library of isometric long-row solutions to every \(T_x\).  Its support
  bound \(|\mathscr J_\ell|\le r2^\ell\) forces asymptotically maximal
  collision excess for \(\ell\gg\log r\).
* PBBS \(C_8\) reversal has endpoint-dependent relabelling under the
  natural correspondence of replaced undirected edges.  Whether some
  coherently oriented global pair satisfies the fixed-\(S\) hypothesis is
  not settled by that local calculation.
* The nonlinear cocycle test, reciprocal rectangle trade, trace expansion
  condition, support count, and dense-repair lower bound are exact.

The following statement remains unproved.

> There is no known Catalan-indexed full-cube family with isometric
> (C_{2r}) rows that satisfies every (T_x) and has (o(2^{2r}))
> aggregate collision excess throughout the protected Gaussian depth band.

Accordingly, raw PBBS/alternating-switch structure does not itself solve
the concrete long-row \(T_x\) gate.  The paired-syndrome construction does
solve that ownership gate with a growing Catalan-labelled library, but not
trace recovery.  The remaining theorem is a dense reciprocal full-cube
realization satisfying the pointwise Latin equations and one of the exact
trace-transversal systems above.
