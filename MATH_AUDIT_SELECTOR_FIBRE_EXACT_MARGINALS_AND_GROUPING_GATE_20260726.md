# Selector fibres: exact all-depth marginals, the visible-tag obstruction, and the integral grouping gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Verdict

The selector-fibre tiling is an exact and useful owner construction, but an
orthogonal array on its selector words does not by itself round the abstract
balanced nested deletion flags.

Let a product status cell be \(Q_S\).  Freeze \(t\) selector axes \(B\), put

\[
                         E=[S]\setminus B,\qquad |E|=V=S-t,
\]

and for each \(z\in Q_B\) choose an active set

\[
                         A_z\in\binom Er,
\]

together with one affine conjugate \(g_z\) of a fixed return-free compiler
on \(Q_r\).  The packets in the fibre \(x|_B=z\) are the
\(2^{V-r}\) parallel copies obtained by freezing \(E\setminus A_z\).

The exact conclusions are as follows.

1.  The full active-set/affine menu has the correct common all-depth
    fractional target marginal.  For either sign, every tagged depth-\(q\)
    face trace has mean load

    \[
                    \boxed{p_{V,q}={2^q\over\binom Vq}}.
                    \tag{0.1}
    \]

    Indeed, for uniform \(A\in\binom Er\) and a uniform affine compiler
    conjugate,

    \[
      {\binom{V-q}{r-q}\over\binom Vr}
      {2^q\over\binom rq}
      ={2^q\over\binom Vq}.                         \tag{0.2}
    \]

    The same random label is used at every depth, so (0.1) is genuinely a
    common all-depth barycentric law, not a collection of unrelated
    depthwise averages.

2.  Exact deterministic orthogonal-array balance on the \(2^t\) binary
    selector fibres is arithmetically impossible in general.  Even after
    erasing the selector tag, exact uniform depth-\(q\) trace load would
    require

    \[
                         \boxed{\binom Vq\mid2^{t+q}.}             \tag{0.3}
    \]

    If \(V\ge4\) and depths \(1,2\) are both protected, (0.3) always fails
    at one of them: \(q=1\) fails when \(V\) is not a power of two, while
    \(q=2\) fails when \(V\) is a power of two because
    \(\binom V2=2^{a-1}(V-1)\) has the odd factor \(V-1>1\).

3.  There is a stronger geometric obstruction.  Every lower or upper
    target emitted by the fibre \(z\) retains all selector orientations in
    \(B\).  Hence it determines \(z\) exactly.  Target images belonging to
    different selector words in the same status cell are disjoint.  An OA
    or fixed-slice correlation among different \(z\)'s therefore has zero
    target-overlap weight and creates none of the negative covariance
    required by the floor-energy identity.

4.  Abstract nested flags and selector-grouped flags have different
    integrality theories.  Once target frames are fixed, abstract nested
    flags form a layered network-flow polytope and are integral under the
    exact Hoffman cuts.  To come from the selector construction, however,
    every fibre must be a cylinder:

    \[
             \boxed{\Phi_z=(g_zFg_z^{-1})\times
                    \operatorname {Id}_{E\setminus A_z}.}        \tag{0.4}
    \]

    Thus the same active prefix table is repeated on all
    \(2^{V-r}\) parallel packets.  Every active-pattern census is divisible
    by \(2^{V-r}\), and the isometric-cycle support censuses have an
    additional antipodal parity.  These constraints are absent from the
    abstract Hoffman flow.

5.  The correct global selection problem is a multiple-choice
    whole-column Hall problem across different status cells.  If \(i\)
    indexes selector fibres, \(\ell\) indexes their legal active-set/compiler
    labels, and \(a_{i\ell}(T)\) is the complete all-depth signed target
    incidence vector of that label, then the exact fractional one-sided
    Hall criterion is

    \[
      \boxed{
      \sum_i\max_{\ell}\sum_Tw_Ta_{i\ell}(T)
      \ge\sum_Tw_Tb_T
      \quad\hbox{for every }w_T\ge0.}               \tag{0.5}
    \]

    Integral selection additionally asks that the demanded vector lie in
    the integer semigroup of the inseparable label columns.  This matrix is
    not reduced to a network by the selector tiling; grouping into
    isometric cycles already contains a determinant-two minor.

Consequently the selector construction proves exact owner resolution and
the correct common all-depth fractional marginals.  It does not yet prove
an integral labeling with \(o(W)\) holes.  The missing theorem is a
cross-cell correlated column selection satisfying (0.5), the floor
covariance inequality, and the cylinder/cycle semigroup constraints.  An
OA on the frozen selector bits alone cannot be that theorem.

## 1. Audit of the two new quartet inputs

### 1.1 The full internal-quartet Gaussian Hall cut

The principal statement of
MATH_THEOREM_FULL_INTERNAL_QUARTET_ATLAS_GAUSSIAN_HALL_CUT_20260726.md
is correct.

Partition \([2m]\) into \(c=m/2\) quartets and let \(F(Y)\) count full
quartets in \(Y\).  A Johnson move internal to one quartet preserves every
local rank.  A quartet of local rank four cannot be active, while a quartet
of local rank at most three cannot become full in an intersection.  Hence
every all-internal lower window satisfies

\[
                              F(T)=F(X).             \tag{1.1}
\]

Writing

\[
 h(u)=1+4u+6u^2+4u^3,
\]

the source and target counts at full-quartet profile \(k\) are

\[
 \binom ck[u^{m-4k}]h(u)^{c-k},\qquad
 \binom ck[u^{m-q-4k}]h(u)^{c-k}.                  \tag{1.2}
\]

For the normalized proper-subset rank variable,

\[
 \mu={28\over15},\qquad \sigma^2={176\over225}.
\]

If \(q=A\sqrt m+O(1)\) and
\(k=m/32+y\sqrt m+O(1)\), then

\[
 \log {\#\text{sources at }k\over\#\text{targets at }k}
 ={15A^2+64Ay\over11}+o(1).                         \tag{1.3}
\]

At \(y=-A/4\), this is \(-A^2/11+o(1)\).  The relevant
\(\Theta_A(\sqrt m)\)-window is a fixed distance on the conditional
Gaussian scale because

\[
                  \operatorname {Var}(F\mid |T|=m-q)
                  ={11m\over512}+O(\sqrt m).        \tag{1.4}
\]

Thus the window has positive target density and gives a linear Hall
deficit.  Since \(N_q/W\to e^{-A^2}\), the conversion to
\(\Omega_A(W)\) noninternal windows is also correct.

For an owner-disjoint isometric \(Q_r\)-packet decomposition, a crossing
axis occurs in a \(q/r\) fraction of cyclic starts.  The weighted average
crossing-axis toll \(\Omega_A(r/q)\) follows.  This last statement uses the
explicit packet/isometric hypotheses; the architecture-free conclusion is
the linear number of cross-quartet based windows.

### 1.2 The two-sign cross-quartet transport

The exact calculations in
MATH_THEOREM_TWO_SIGN_CROSS_QUARTET_PROFILE_TRANSPORT_20260726.md
are also correct.

Against the large-layer internal shore, the cross shore preserves the
lower profile and changes the upper profile on sectors \(k=1,2,3\).  Its
owner mass is

\[
 2\sum_{k=1}^3\binom4k\binom4{k-1}=104,
\]

or \(13/32\) of the local \(256\) owners.  Against the small-layer shore,
the cross shore preserves the upper profile and changes the lower profile
on \(k=2,3,4\), again on mass \(104\).  Tensoring with \(Q_{r-1}\) gives
whole \(Q_r\)-packet trades without a seam.

The two \(13/32\) statements are separate signwise marginals.  They do not
give one common choice transporting both signs on \(13/32\).  In the
overlap sectors \(k=2,3\), a whole owner can choose the large shore or the
small shore, not both.  The sector masses are

\[
                              8,48,48,8.
\]

Choosing the large shore in one central sector and the small shore in the
other, together with the two extreme sectors, transports each sign on

\[
                              8+48=56
\]

owners, namely \(7/32\).  This is the sharp equal-sign density within the
three-shore local menu.  It is an exact common local state, but density
alone says nothing about the global all-depth floor covariance.

The rank-twisted macroblock packets have all \(r\) axes crossing the two
macroblock halves, so—when the halves are aligned as unions of the old
quartets—they meet the Gaussian crossing-axis toll maximally.  The rest of
this audit tests the target and common-selection gate rather than inferring
balance from that density.

## 2. Exact target code in one selector fibre

Let \(F\) be a fixed compiler factor on \(Q_r\), return-free in both
directions through depth \(H\le r\).  For a signed depth \(q\le H\), its
local trace at \(u\in Q_r\) consists of

\[
                         (D,\xi),
 \qquad D\in\binom{[r]}q,
 \qquad \xi\in Q_{[r]\setminus D}.                \tag{2.1}
\]

For the lower sign, the physical pairs in \(D\) are made empty.  For the
upper sign, they are made full.  The orientations \(\xi\) of all untouched
pairs remain visible.

Fix \(z\in Q_B\), a label \((A_z,g_z)\), and a payload word

\[
                         y\in Q_{E\setminus A_z}.
\]

The packet is

\[
        P_{z,y}=\{x:x|_B=z,\ x|_{E\setminus A_z}=y\}\cong Q_r.   \tag{2.2}
\]

A signed target from this packet has the exact local code

\[
                         (z,D,\eta),
 \qquad D\in\binom{A_z}q,
 \qquad \eta\in Q_{E\setminus D}.                 \tag{2.3}
\]

Here \(\eta|_{E\setminus A_z}=y\), while its restriction to
\(A_z\setminus D\) is the active compiler trace.

For a conjugate \(F^g=gFg^{-1}\), let

\[
 n_{g,q}^{\epsilon}(D,\xi)
 =\#\{u\in Q_r:\tau_q^{F^g,\epsilon}(u)=(D,\xi)\}.               \tag{2.4}
\]

After identifying \(A_z\) with \([r]\), the exact load of the tagged trace
\(\theta=(z,D,\eta)\) under the label \((A_z,g_z)\) is

\[
 \boxed{
 L_{z,q}^{\epsilon}(D,\eta)
 =\mathbf1_{\{D\subseteq A_z\}}
   n_{g_z,q}^{\epsilon}
     \bigl(D,\eta|_{A_z\setminus D}\bigr).}         \tag{2.5}
\]

The inactive word \(y\) is forced by \(\eta\), so there is no missing
multiplicity in (2.5).  For a shadow-injective compiler, the right side is
zero or one.

Equation (2.5) is the literal target formula which the axis-incidence
census in the selector-fibre theorem does not contain.

## 3. Exact common all-depth affine marginal

Let

\[
                         \Gamma_r=Q_r\rtimes S_r,
 \qquad |\Gamma_r|=2^rr!,                          \tag{3.1}
\]

be the cube-affine group generated by endpoint reversals and axis
permutations.

### Lemma 3.1 (complete affine trace orbit)

For either sign, every depth-\(q\) trace in \(Q_r\) has total multiplicity

\[
                         2^{r+q}q!(r-q)!             \tag{3.2}
\]

over all pairs \((g,u)\in\Gamma_r\times Q_r\).

#### Proof

Every conjugate has \(2^r\) based occurrences.  Return-freeness makes each
one a \(q\)-face trace.  The affine group is transitive on the

\[
                         \binom rq2^{r-q}
\]

signed traces of a fixed sign.  Hence every trace has the same orbit load,
equal to

\[
 {|\Gamma_r|2^r\over\binom rq2^{r-q}}
 =2^{r+q}q!(r-q)!.
\]

The reverse factor gives the same argument for the other sign. \(\square\)

Dividing (3.2) by \(|\Gamma_r|\) gives

\[
 {1\over|\Gamma_r|}\sum_{g\in\Gamma_r}
 n_{g,q}^{\epsilon}(D,\xi)
 ={2^q\over\binom rq}.                             \tag{3.3}
\]

### Theorem 3.2 (exact selector-fibre target marginal)

Choose \(A\) uniformly from \(\binom Er\) and \(g\) uniformly from
\(\Gamma_r\).  For every \(z\in Q_B\), every signed depth \(q\le H\), and
every tagged trace \((z,D,\eta)\) with \(D\in\binom Eq\),

\[
 \boxed{
 \mathbb E_{A,g}L_{z,q}^{\epsilon}(D,\eta)
 ={2^q\over\binom Vq}.}                            \tag{3.4}
\]

#### Proof

The probability that \(D\subseteq A\) is

\[
 {\binom{V-q}{r-q}\over\binom Vr}
 ={\binom rq\over\binom Vq}.                       \tag{3.5}
\]

Conditional on this event, (3.3) gives mean active trace multiplicity
\(2^q/\binom rq\).  Their product is (3.4). \(\square\)

One draw of \((A,g)\) specifies the whole factor, so all the traces in
(3.4) are nested prefixes of the same compiler simultaneously in \(q\).
There is no depthwise reselection hidden in the theorem.

If an ambient literal target \(T\) has geometric candidate selector fibres
\(\mathscr C_q^\epsilon(T)\), possibly with different payload dimensions
\(V_i\), the symmetric menu therefore gives the exact fractional load

\[
 \boxed{
 \mu_q^\epsilon(T)
 =\sum_{i\in\mathscr C_q^\epsilon(T)}
     {2^q\over\binom{V_i}q}.}                       \tag{3.6}
\]

When all \(V_i=V\), this is \(p_{V,q}d_q^\epsilon(T)\).  Formula (3.6)
is an exact first moment.  It does not imply a lower-tail estimate for the
candidate degrees, a weighted Hall inequality, or integral coverage.

## 4. Exact OA and divisibility obstructions

The bound

\[
 t\gtrsim\log_2\binom Vr+\log_2(2^rr!)              \tag{4.1}
\]

shows that there are enough binary selector words to list every menu
label at least once.  It does not make uniform repetition exact.  The menu
size normally has odd factors, whereas \(2^t\) does not.

There are two useful unavoidable divisibility tests.

### Proposition 4.1 (support-design divisibility)

Suppose the multiset \((A_z)_{z\in Q_B}\) has exact uniform incidence on
all \(s\)-subsets of \(E\).  Then

\[
 \boxed{
 \lambda_s^{\rm supp}
 ={2^t\binom rs\over\binom Vs}\in\mathbb Z.}        \tag{4.2}
\]

#### Proof

Count pairs \((z,D)\) with \(D\in\binom{A_z}s\).  Counting first by \(z\)
gives \(2^t\binom rs\); counting first by \(D\) gives
\(\lambda_s^{\rm supp}\binom Vs\). \(\square\)

Thus a strength-\(H\) active-set design requires (4.2) for every
\(s\le H\).  Already at \(s=1\), it requires \(V\mid2^tr\).  Choosing \(t\)
large does not remove an odd prime of \(V/\gcd(V,r)\).

### Proposition 4.2 (full trace-census divisibility)

Collapse the selector tag \(z\), and ask that all depth-\(q\) payload face
traces \((D,\eta)\) have the same integral load after summing the
\(2^t\) selector fibres.  Then necessarily

\[
 \boxed{
 \Lambda_{t,V,q}={2^{t+q}\over\binom Vq}\in\mathbb Z.}          \tag{4.3}
\]

#### Proof

Every selector fibre has \(2^V\) owners and therefore emits \(2^V\)
based traces at the fixed sign and depth.  The total number of occurrences
is \(2^{t+V}\).  The collapsed trace universe has size

\[
                         \binom Vq2^{V-q}.
\]

Uniform integral load forces their ratio (4.3). \(\square\)

### Corollary 4.3 (binary depth-one/depth-two no-go)

If \(V\ge4\), no deterministic array on exactly \(2^t\) selector words can
have an unthinned exact uniform collapsed trace census at both depths one
and two.

#### Proof

If \(V\) is not a power of two, its odd part prevents
\(V\mid2^{t+1}\), so (4.3) fails at \(q=1\).  If \(V=2^a\ge4\), then

\[
                         \binom V2=2^{a-1}(V-1),
\]

whose odd factor \(V-1>1\) prevents it from dividing \(2^{t+2}\). \(\square\)

This corollary is stronger than a failure to enumerate the whole affine
menu uniformly: it rules out every possible deterministic label list with
an exact unthinned uniform trace census.  Floor/ceiling loads or
depth-dependent dumped occurrences can evade the divisibility, but then
the accepted occurrences must themselves be selected and grouped
coherently.  That is a new integral problem, not an OA consequence.

## 5. The selector tag is visible to every target

### Lemma 5.1 (visible-tag separation)

For either sign and every \(q\le H\), a literal target emitted from a
selector fibre determines its selector word \(z\).  Consequently, inside
one status cell,

\[
 \operatorname {Im}\tau_{z,q}^{\epsilon}
 \cap
 \operatorname {Im}\tau_{z',q}^{\epsilon}
 =\varnothing
 \qquad(z\ne z').                                  \tag{5.1}
\]

#### Proof

No active set \(A_z\) meets \(B\).  In a lower target, completed active
pairs are empty, while every selector pair remains split and displays its
selected endpoint.  In an upper target, completed active pairs are full,
while every selector pair again remains split and displays its selected
endpoint.  Thus the target recovers all bits \(x|_B=z\). \(\square\)

This has a direct floor-covariance consequence.  Let \(\ell,\ell'\) be two
label options and let

\[
 K_q\bigl((z,\ell),(z',\ell')\bigr)
 =|A_q(z,\ell)\cap A_q(z',\ell')|                  \tag{5.2}
\]

be their literal target-overlap kernel.  Lemma 5.1 gives

\[
 K_q\bigl((z,\ell),(z',\ell')\bigr)=0
 \qquad(z\ne z')                                   \tag{5.3}
\]

within one status cell.

Therefore a fixed-slice or OA law which makes the labels at different
selector words negatively correlated contributes exactly zero to

\[
 \sum_{(z,\ell)\ne(z',\ell')}
 K_q\bigl((z,\ell),(z',\ell')\bigr)
 \operatorname {Cov}(I_{z,\ell},I_{z',\ell'}).     \tag{5.4}
\]

It may balance a catalogue histogram, but it does not create the negative
overlap-weighted covariance required by the floor-energy theorem.

For a fixed ambient target, at most one selector word in a given status
cell is relevant.  To correlate two candidate occurrences of that target,
one must coordinate labels in different status cells or in a construction
whose selector bits are themselves erased by the window.  The present
frozen-selector OA does neither.

### Lemma 5.2 (exact independent-label hole law)

Choose the full symmetric label independently in every candidate selector
fibre, and assume the compiler is shadow-injective through depth \(H\).
For a fixed signed target \(T\), let its candidate fibres have payload
dimensions \(V_i\).  Then

\[
 \boxed{
 \Pr(T\text{ is missed})
 =\prod_{i\in\mathscr C_q^\epsilon(T)}
   \left(1-{2^q\over\binom{V_i}q}\right).}          \tag{5.5}
\]

If

\[
 \max_i {2^q\over\binom{V_i}q}=o(1),
 \qquad
 \sum_i {2^q\over\binom{V_i}q}\longrightarrow\lambda,
                                                               \tag{5.6}
\]

then the miss probability tends to \(e^{-\lambda}\).

#### Proof

Theorem 3.2 gives the exact hit probability in candidate fibre \(i\).
Shadow injectivity makes this a zero-one event.  Independent fibre labels
make the events independent, proving (5.5).  Taking logarithms and using
\(\log(1-p)=-p+O(p^2)\) proves the limit under (5.6). \(\square\)

Thus at critical mean \(\lambda=1+o(1)\), independent symmetric labels
miss an \(e^{-1}+o(1)\) fraction of any target family obeying the uniform
conditions.  This is the precise Poisson barrier.  Avoiding it requires
dependent choices across candidate fibres of the same physical targets;
the within-cell OA dependence excluded by (5.3) is in the wrong overlap
directions.

## 6. Abstract nested-flow integrality versus fibre grouping

There is a positive theorem before packet grouping.  Fix integral target
frame assignments.  Make a layered DAG whose level-\(q\) states are the
rank-\((m-q)\) targets and whose arcs delete one legal split-pair endpoint.
Split every state vertex to impose its integral throughput bounds.  The
resulting constraint matrix is a directed node--arc incidence matrix.
Hence Hoffman's circulation inequalities are necessary and sufficient,
and every feasible fractional flow has an integral realization by nested
owner-rooted flags.

The selector construction demands more.

### Theorem 6.1 (exact cylinder grouping criterion)

Fix one selector word \(z\).  A complete table of forward and reverse
owner flags in its \(Q_V\) payload fibre is realized by one selector label
\((A_z,g_z)\) if and only if there are

\[
 A_z\in\binom Er,\qquad g_z\in\Gamma_r,             \tag{6.1}
\]

such that, after writing an owner as \((u,y)\in Q_{A_z}\times
Q_{E\setminus A_z}\), its successor map is

\[
 \boxed{
 \Phi_z(u,y)=\bigl(g_zFg_z^{-1}(u),y\bigr),}        \tag{6.2}
\]

and the prescribed signed flags are the forward and reverse prefixes of
this map through depth \(H\).

#### Proof

In the selector tiling, \(y\) indexes the parallel packet and is frozen.
Every packet carries the same conjugate \(g_zFg_z^{-1}\), so (6.2) and all
its prefix consequences are necessary.

Conversely, if (6.2) holds, the fibres with fixed \(y\) are exactly the
packets \(P_{z,y}\).  Installing \(g_zFg_z^{-1}\) on each of them realizes
the displayed successor map and all its forward and reverse nested
prefixes. \(\square\)

The theorem exposes three constraints absent from abstract target
marginals.

1. Every used direction belongs to one common \(r\)-set \(A_z\).
2. The direction/prefix table depends only on \(u\), never on the frozen
   word \(y\).
3. The identical table is repeated on all \(2^{V-r}\) values of \(y\).

In particular, if \(\alpha\) is any active prefix type which ignores the
inactive word \(y\), then

\[
 \boxed{
 \#\{\text{owners of type }\alpha\text{ in fibre }z\}
 \equiv0\pmod{2^{V-r}}.}                           \tag{6.3}
\]

If the compiler is a factor of isometric \(C_{2r}\)'s and \(q<r\), every
cyclic \(q\)-direction support occurs at antipodal starts in the word
\(\pi\pi\).  Thus support-only censuses satisfy the stronger congruence

\[
 \boxed{
 \#\{\text{owners with a fixed active }q\text{-support}\}
 \equiv0\pmod{2^{V-r+1}}.}                         \tag{6.4}
\]

An integral Hoffman flow can prescribe counts violating (6.3) or (6.4),
so the projection from grouped compiler factors to integral nested flags is
not surjective.

Allowing the conjugate to depend on \(y\) would remove the large repetition
factor in (6.3), while preserving exact ownership.  It would not remove
the visible selector tag, the active-set constraint, or the global
whole-cycle grouping problem.  It is a genuine enlargement of the stated
\(z\mapsto(A_z,g_z)\) architecture and should not be silently assumed.

### Proposition 6.2 (cycle grouping is not totally unimodular)

For every \(r\ge3\), the owner incidence matrix of the allowed isometric
\(C_{2r}\) catalogue contains a determinant-two minor.

#### Proof

Let \(e_1,\ldots,e_r\) be the cube basis, put

\[
 p_0=0,\qquad p_j=e_1+\cdots+e_j,
\]

and let

\[
 P=\{p_0,\ldots,p_{r-1},\mathbf1+p_0,\ldots,
                   \mathbf1+p_{r-1}\}
\]

be the vertex support of the standard isometric cycle.  Take the three
translates

\[
                         C_0=P,\quad C_1=P+e_1,
                         \quad C_2=P+e_2.
\]

On the owner rows \(0,e_1+e_2,e_2\), their incidence matrix is

\[
 \begin{pmatrix}
  1&1&0\\
  1&0&1\\
  0&1&1
 \end{pmatrix},
 \qquad\det=-2.                                     \tag{6.5}
\]

Thus the three exact-cover equations have the fractional solution
\((1/2,1/2,1/2)\) and no integral solution. \(\square\)

Proposition 6.2 concerns the stage which groups an already constructed
abstract flag flow into complete compiler cycles.  If a whole compiler
factor is fixed first, that grouping is already built into the label, but
then Theorem 6.1 says that the abstract flags must match one inseparable
factor column.  In neither direction does ordinary network integrality
perform the grouping.

## 7. The exact global Hall problem

Let \(I\) index all selector fibres in all retained rank-twisted product
status cells.  For \(i\in I\), let \(\mathcal L_i\) be its legal menu of
active-set/compiler labels.  Let \(\mathcal T\) contain all tagged physical
targets at both signs and every protected depth.  A label has the complete
incidence column

\[
 a_{i\ell}\in\mathbb Z_{\ge0}^{\mathcal T}.          \tag{7.1}
\]

Choosing one label in every fibre asks for

\[
 x_{i\ell}\in\{0,1\},\qquad
 \sum_{\ell\in\mathcal L_i}x_{i\ell}=1.             \tag{7.2}
\]

Let \(b_T\) be the desired one-sided demand after any explicitly declared
dump or quarantine.

### Theorem 7.1 (weighted Hall criterion for fractional fibre labels)

There are fractional choices

\[
 x_{i\ell}\ge0,\qquad
 \sum_\ell x_{i\ell}=1,
 \qquad
 \sum_{i,\ell}a_{i\ell}(T)x_{i\ell}\ge b_T
 \quad(T\in\mathcal T)                             \tag{7.3}
\]

if and only if, for every nonnegative target weight vector \(w\),

\[
 \boxed{
 \sum_{i\in I}\max_{\ell\in\mathcal L_i}
       \langle w,a_{i\ell}\rangle
 \ge\langle w,b\rangle.}                           \tag{7.4}
\]

#### Proof

The attainable fractional load vectors form the compact convex Minkowski
sum

\[
 K=\sum_{i\in I}\operatorname {conv}
       \{a_{i\ell}:\ell\in\mathcal L_i\}.           \tag{7.5}
\]

Its support function at \(w\) is the left side of (7.4).  Feasibility is
equivalent to \(K\cap(b+\mathbb R_{\ge0}^{\mathcal T})\ne\varnothing\).
If the two convex sets are disjoint, separation from the upward orthant
gives a nonnegative normal \(w\) violating (7.4).  Conversely, every
feasible load vector makes (7.4) immediate. \(\square\)

The symmetric affine point of Theorem 3.2 is one particular member of
\(K\).  Formula (3.6) gives all its coordinate marginals exactly.  It does
not by itself prove the candidate-degree lower tail needed for that point
to meet \(b\), and a coordinatewise first moment does not analyze a
different point of \(K\).

The integral problem replaces every simplex in (7.5) by one of its
vertices.  It is a multiple-choice hypergraph cover with columns coupling
all depths and both signs.  The support-design congruences, the cylinder
congruences, and Proposition 6.2 show why fractional feasibility does not
imply integral feasibility by total unimodularity.

For the coefficient-one floor target, one needs more than one-sided
coverage: the selected loads should lie at the two adjacent integers
\(c_q,c_q+1\) with the prescribed totals.  This adds upper rows and dump
variables to (7.2), but does not change the inseparability of a label
column.  Equivalently, one must establish the negative overlap-weighted
covariance missing from (5.4).

## 8. Consequences for HCRT and the next construction target

The selector-fibre construction changes the positive side of the ledger:

* owner overlap is exactly zero;
* active sets and affine compiler states can vary over an exponentially
  large menu while \(t=o(m)\);
* dense rank-twisted packets meet the cross-quartet occurrence toll; and
* the full menu has the exact common all-depth marginal (3.4).

It does not close HCRT or the floor-covariance theorem:

* the separate \(13/32\) upper and lower transport densities are not one
  common \(13/32\) state;
* frozen selector words label disjoint target families, so a local OA on
  those words has no useful overlap covariance;
* binary exact trace uniformity is blocked already at depths one and two;
* abstract integral nested flows need not satisfy the cylinder and cycle
  semigroup constraints; and
* the full internal-quartet Hall cut requires the crossing windows to move
  mass between the deficient profiles, not merely to contain crossing
  axes.

The sharp remaining route is therefore:

1. build the global candidate-fibre incidence columns \(a_{i\ell}\) for
   the rank-twisted compatibility kernel;
2. verify the common all-depth weighted cuts (7.4), or a stronger explicit
   candidate-degree/covariance estimate;
3. coordinate labels across different status cells which share physical
   targets, rather than only across \(z\)'s inside one cell; and
4. prove semigroup saturation or construct an absorber for the residual
   support-design, cylinder, and cycle congruences.

Until those steps are supplied, the selector fibres are an exact
owner-side option compiler and an exact fractional marginal realization,
not an integral no-Poisson-hole theorem.
