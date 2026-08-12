# Audit of the global common-core atlas and the exact tail-order fusion polytope

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Verdict

Let

\[
W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad M=m+H,
\]

and put

\[
s=m-H,\qquad L=s-2H+1=m-3H+1.
\tag{0.1}
\]

Assume \(H=(1+o(1))\sqrt{m\log m}\) and \(m/H\to\infty\). I audited
MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md theorem by
theorem.

The random-core degree formulae, clone-Hall arguments, literal core-safe
path, and aggregate \(O(H^{3/2}N_H)=o(W)\) rankwise-hole ledger are
correct. Section 4 is also correct for the unrestricted catalogue in
which the core is part of the option. Two points require precise scope.

1. The Section 4 catalogue must include tag profiles when signed-rank
   loads are discussed.
2. Its symmetry argument averages over cores. It does not, by itself,
   give exact uniform loads for the fixed good cores from Sections 1 and
   3.

The second point is not fatal. Theorem 2.1 below proves what is needed:
those fixed good cores admit one common fractional distribution on
literal tail orders and nested tag profiles respecting all target
capacities simultaneously.

The integral tight-path fusion remains open. This note proves:

* after targets are assigned to phase/depth cells, fusion into one tail
  order is exactly a bipartite signature-matching problem;
* with every cell exposed, the criterion is an explicit diagonal-shell
  or diamond identity;
* the coordinate-incidence tail-order polytope has a totally unimodular
  assignment extended formulation; but
* the physical target--configuration matrix has determinant-\(2\) minors
  and physical odd conflict triangles.

Thus local tail-order integrality is benign, while global identification
of whole target sets is not TU. No coefficient-one conclusion is claimed.

## 1. Audit of the common-core atlas

### Proposition 1.1 (audited claims)

Under the source hypotheses, its Theorems 1.1, 1.2, 2.1, 3.1, 3.2 and
Proposition 3.3 are valid.

#### Proof

For a fixed middle set \(X\), the random number of tops whose chosen core
lies in \(X\) has mean

\[
\binom mH\frac{\binom m{2H}}{\binom{m+H}{2H}}
=\frac1\Lambda\binom{m-H}{H}.
\tag{1.1}
\]

The threshold exceeds this mean by relative amount
\(\Lambda/L-1=\Theta(H/m)\). Its Chernoff exponent is at least

\[
c\binom{m-H}{H}\frac{H^2}{m^3}\gg m,
\tag{1.2}
\]

so the union bound over fewer than \(4^m\) middle sets is valid. The
clone-Hall proof is also valid: complete every touched top fibre of an
arbitrary clone set; the neighbourhood is unchanged and the number of
clones only increases.

At signed rank \(m+r\), the exact left degree and mean right degree are

\[
d_r=\binom{s}{H-r},\qquad
\mu_r=\frac{d_r}{\Lambda_r},\qquad
\Lambda_r=\frac{N_{|r|}}{N_H}.
\tag{1.3}
\]

If \(b_{|r|}>0\), then \(\Lambda_r-b_{|r|}\ge1\). The Chernoff exponent
at \(d_r/b_{|r|}\) is at least \(c d_r/\Lambda_r^3\). The condition
\(\Lambda_r\ge2\) forces \(H-|r|=\Omega(m/H)\) for \(r>0\), while
\(H-r\ge H\) for \(r<0\). Hence \(d_r/\Lambda_r^3\gg m\), uniformly over
all nonempty ranks. This verifies the simultaneous union bound and the
ensuing clone-Hall theorem.

For the hole ledger, an uncapped rank loses fewer than \(2N_H\) masks.
The cap \(b_q=L-1\) occurs only for \(q=O(\sqrt H)\), and its loss at each
such depth is \(O(HN_H)\). Thus both signs together lose

\[
O(HN_H)+O(H^{3/2}N_H)=O(H^{3/2}N_H)=o(W).
\tag{1.4}
\]

Finally, in a core-safe word, every nonempty deletion interval is an
interval in an injective linear word. Distinct phases give distinct
intervals at the same length. The only repeated zero-length trace is the
top, and the tag-\(H\) restriction permits it at most once. \(\square\)

### Remark 1.2 (scope of the original symmetric point)

When the core varies as part of each option, full coordinate symmetry
makes every target load equal to total occurrence mass divided by layer
size, as asserted in the source. Once the cores are fixed, global
transitivity is lost and exact equality need not hold. The following
theorem supplies the needed inequalities.

## 2. A common fractional point for the fixed good cores

Fix cores \(Q_U\subset U\), \(|Q_U|=2H\), satisfying all source degree
caps. Put \(S_U=U\setminus Q_U\), so \(|S_U|=s\). Let

\[
b_0=L\ge b_1\ge\cdots\ge b_{H-1}\ge b_H=0
\tag{2.1}
\]

be the quota profile. A tag assignment on the \(L\) phases is admissible
if exactly \(b_q\) phases have tag at least \(q\).

### Theorem 2.1 (fixed-core common-history fractional feasibility)

For every top \(U\), independently choose a uniformly random permutation
of \(S_U\), and a uniformly random admissible tag assignment,
independently of the permutation. Interpret this as one literal
core-safe promotion path on \(U\). Every middle target has expected load
at most \(1\), and every signed internal target at depth \(1\le q<H\)
has expected load at most \(1\).

Consequently, the complete configuration LP for the fixed good cores has
a fractional point saturating every top root and simultaneously
respecting every physical target capacity.

#### Proof

Fix signed rank \(m+r\), put \(\ell=H-r\), and fix
\(Y\in\binom{[2m]}{m+r}\). A top \(U\) can produce \(Y\) only if

\[
Q_U\subseteq Y\subseteq U.
\tag{2.2}
\]

Then \(I=U\setminus Y\subset S_U\) has size \(\ell\). At each fixed
phase, the deletion interval in a uniform random tail order is a uniform
\(\ell\)-subset of \(S_U\). At threshold \(q=|r|\), a fixed phase is
active with probability \(b_q/L\). Hence this top's expected number of
active occurrences of \(Y\) is

\[
L\frac{b_q}{L}\frac1{\binom{s}{\ell}}
=\frac{b_q}{d_r}.
\tag{2.3}
\]

This uses only linearity of expectation. For \(\ell>0\), the phase
intervals are in fact distinct. If \(b_q=0\), the load is zero. If
\(b_q>0\), at most \(d_r/b_q\) tops satisfy (2.2), so the total load is
at most \(1\). At the middle rank, the same
calculation has \(b_0=L\), \(d_0=\binom{s}{H}\), and top degree at most
\(d_0/L\). Every sampled object is one tail order with one nested tag
profile, proving common fractional feasibility. \(\square\)

### Corollary 2.2 (all nonnegative additive duals pass)

For arbitrary nonnegative weights on all signed physical targets, the
sum, over tops, of the cheapest literal fixed-core path is at most the
total target weight.

#### Proof

For each top, its minimum weighted cost is at most its expectation under
Theorem 2.1. Sum over tops and interchange the finite sums. \(\square\)

## 3. Exact fusion after phase cells are fixed

Fix a top \(U\), core \(Q\), and \(S=U\setminus Q\). For
\(1\le j\le L\), \(0\le\ell\le2H\), define

\[
R_{j,\ell}
=\{j+2H-\ell,\ldots,j+2H-1\}\subseteq[s],
\qquad R_{j,0}=\varnothing.
\tag{3.1}
\]

Let \({\cal O}\subseteq[L]\times\{0,1,\ldots,2H\}\) be observed cells.
Suppose the target prescribed in cell \((j,\ell)\) has deletion set

\[
I_{j,\ell}=U\setminus T_{j,\ell}\subseteq S,\qquad
|I_{j,\ell}|=\ell.
\tag{3.2}
\]

For \(a\in S\), \(t\in[s]\), define signatures

\[
\tau(a)=\bigl({\bf1}_{a\in I_{j,\ell}}\bigr)_{(j,\ell)\in{\cal O}},
\qquad
\sigma(t)=\bigl({\bf1}_{t\in R_{j,\ell}}\bigr)_{(j,\ell)\in{\cal O}}.
\tag{3.3}
\]

### Theorem 3.1 (signature-Hall fusion theorem)

The following are equivalent.

1. There is a permutation \(w_1,\ldots,w_s\) of \(S\) with

   \[
   I_{j,\ell}=\{w_t:t\in R_{j,\ell}\}
   \quad((j,\ell)\in{\cal O}).
   \tag{3.4}
   \]

2. The bipartite graph from \(a\in S\) to \(t\in[s]\), with

   \[
   a\sim t\quad\Longleftrightarrow\quad\tau(a)=\sigma(t),
   \tag{3.5}
   \]

   has a perfect matching.

3. For every \(A\subseteq S\),

   \[
   \left|\bigcup_{a\in A}\{t:\sigma(t)=\tau(a)\}\right|\ge|A|.
   \tag{3.6}
   \]

4. For every \(\eta\in\{0,1\}^{\cal O}\),

   \[
   |\{a\in S:\tau(a)=\eta\}|
   =|\{t\in[s]:\sigma(t)=\eta\}|.
   \tag{3.7}
   \]

#### Proof

If (3.4) holds and \(w_t=a\), membership of \(a\) in every observed
deletion set equals membership of \(t\) in the corresponding positional
interval. Thus the word gives a perfect matching in (3.5). Conversely,
a perfect matching assigns each coordinate a distinct position; reading
matched coordinates in positional order gives (3.4).

The equivalence of (2) and (3) is Hall's theorem. The graph in (3.5) is
a disjoint union of complete bipartite graphs, one per signature, and
has a perfect matching exactly when both shores of every component have
equal size. This is (4). \(\square\)

Thus, once targets are placed into phase/depth cells, there is no further
local odd-set obstruction. The obstruction is exactly (3.7). The open
choice is to place separately matched targets into cells so these common
signatures arise while global physical capacities remain respected.

### Corollary 3.2 (exact Boolean-atom identities)

Every fusible phase-labelled assignment satisfies, for
\({\cal A},{\cal B}\subseteq{\cal O}\),

\[
\left|
\bigcap_{\alpha\in{\cal A}} I_\alpha
\cap\bigcap_{\beta\in{\cal B}}(S\setminus I_\beta)
\right|
=
\left|
\bigcap_{\alpha\in{\cal A}} R_\alpha
\cap\bigcap_{\beta\in{\cal B}}([s]\setminus R_\beta)
\right|.
\tag{3.8}
\]

In particular,

\[
|I_{j,\ell}\cap I_{k,r}|=|R_{j,\ell}\cap R_{k,r}|.
\tag{3.9}
\]

For middle deletions,

\[
|I_{j,H}\cap I_{k,H}|=(H-|j-k|)_+.
\tag{3.10}
\]

Thus middle assignments, after phase ordering, must form an isometric
tight path, not merely a Johnson path with adjacent intersections
\(H-1\).

#### Proof

The bijection in (3.4) preserves every Boolean combination and its
cardinality. Formula (3.10) is the overlap of two length-\(H\) intervals
whose starts differ by \(|j-k|\). \(\square\)

Pairwise identities alone are not asserted sufficient. The full
signature ledger, equivalently all Boolean atoms in (3.8), is exact.

## 4. Complete arrays and the diamond law

Assume every cell \((j,\ell)\), \(1\le j\le L\),
\(0\le\ell\le2H\), is displayed. Put

\[
D_{j,\ell}=I_{j,\ell}\setminus I_{j,\ell-1}
\qquad(1\le\ell\le2H).
\tag{4.1}
\]

### Theorem 4.1 (complete tail-order criterion)

The array comes from one permutation of \(S\) if and only if:

1. \(I_{j,0}=\varnothing\);
2. \(I_{j,\ell-1}\subset I_{j,\ell}\), with every
   \(D_{j,\ell}\) a singleton;
3. the diamond identities

   \[
   D_{j,\ell}=D_{j+1,\ell+1}
   \qquad(1\le j<L,\ 1\le\ell<2H)
   \tag{4.2}
   \]

   hold; and
4. shells on distinct diagonals differ: if

   \[
   j+2H-\ell\ne k+2H-r,
   \tag{4.3}
   \]

   then \(D_{j,\ell}\ne D_{k,r}\).

The inducing permutation is then unique and

\[
D_{j,\ell}=\{w_{j+2H-\ell}\}.
\tag{4.4}
\]

#### Proof

Necessity follows from (3.1). Increasing \(\ell\) adds the coordinate in
position \(j+2H-\ell\), and the same position is shell
\((j+1,\ell+1)\) in the next phase.

Conversely, \(t=j+2H-\ell\) ranges through all \(1\le t\le s\).
Conditions (3) and (4) define \(s\) distinct coordinates \(w_t\in S\),
hence a permutation. Conditions (1) and (2) give

\[
I_{j,\ell}=\bigcup_{r=1}^{\ell}D_{j,r}
=\{w_{j+2H-\ell},\ldots,w_{j+2H-1}\}.
\tag{4.5}
\]

Uniqueness follows from (4.4). \(\square\)

The diamond equality is the smallest exact joint equality erased by
separate rankwise Hall. Violating one diamond precludes a common tail
order although every individual target can remain core-compatible and
every separate rank globally injective.

## 5. The local convex hull is integral

For \(t\in[s]\), \(a\in S\), introduce \(z_{t,a}\), with

\[
\sum_{a\in S}z_{t,a}=1,\qquad
\sum_{t=1}^s z_{t,a}=1,\qquad z_{t,a}\ge0.
\tag{5.1}
\]

Define

\[
x_{j,\ell,a}=\sum_{t\in R_{j,\ell}}z_{t,a}.
\tag{5.2}
\]

### Theorem 5.1 (TU extended formulation)

The projection of (5.1)--(5.2) onto \(x\) is exactly the convex hull of
coordinate-incidence arrays of literal tail orders. It is integral, and
(5.1) is a totally unimodular extended formulation.

#### Proof

The matrix in (5.1) is the bipartite vertex--edge incidence matrix of
\(K_{s,s}\), hence TU. Its polytope is the Birkhoff polytope. Equation
(5.2) is linear, so its image is the convex hull of integral
coordinate-incidence arrays of permutations. Every vertex of that image
is one of those integral image points. \(\square\)

This does not linearize the physical capacity assertion that two whole
target subsets are unequal. That assertion treats an entire
\(0\)-\(1\) incidence vector as one resource. The resulting
target--configuration matrix is not TU.

## 6. A physical determinant-two minor and odd conflict triangle

### Theorem 6.1 (non-TU occurs in the literal catalogue)

Assume \(m\ge4H\). The middle-target incidence matrix of the literal
core-safe path catalogue contains

\[
\begin{pmatrix}
1&0&1\\
1&1&0\\
0&1&1
\end{pmatrix},
\tag{6.1}
\]

whose determinant has absolute value \(2\). The three columns can also
be realized on three distinct top roots, where they form a physical
target-conflict triangle.

#### Proof

First fix one top and core. Since \(s\ge3H\), choose disjoint
\(H\)-sets \(A,B,C\subset S\). There is a tail word whose middle subword
contains \(A,B\) as consecutive \(H\)-blocks and omits all of \(C\);
similarly for \(B,C\) and \(C,A\). On target rows
\(U\setminus A,U\setminus B,U\setminus C\), the three configurations
have exactly (6.1).

For distinct roots, take disjoint sets

\[
|C_0|=m-H,\qquad |A_1|=|A_2|=|A_3|=H
\tag{6.2}
\]

inside \([2m]\), possible since their union has size \(m+2H\le2m\).
Put

\[
U_1=C_0\cup A_1\cup A_2,\quad
U_2=C_0\cup A_2\cup A_3,\quad
U_3=C_0\cup A_3\cup A_1.
\tag{6.3}
\]

Choose each core inside \(C_0\). On \(U_1\), choose a path containing
deletion windows \(A_1,A_2\); on \(U_2\), one containing \(A_3,A_2\);
and on \(U_3\), one containing \(A_1,A_3\). The middle subword has
length \(m-2H\ge2H\), so these choices are literal. The paths pairwise
collide on

\[
C_0\cup A_2,\qquad C_0\cup A_3,\qquad C_0\cup A_1,
\tag{6.4}
\]

respectively. \(\square\)

If \(y_1,y_2,y_3\) are these variables, the three displayed
target-capacity inequalities yield only

\[
y_1+y_2+y_3\le\frac32,
\tag{6.5}
\]

whereas every integral target-simple selection obeys

\[
y_1+y_2+y_3\le1.
\tag{6.6}
\]

This is a precise joint odd-clique obstruction to TU. It is not a
counterexample to the unrestricted atlas: every root has many
alternatives outside the triangle. A successful theorem must bypass such
odd meshes with aggregate \(o(W)\) loss or control their stable-set cuts.

## 7. Exact remaining boundary

The separate Hall assignments can be fused after phase labelling if and
only if, at every top, their deletion sets pass (3.7). For a complete
latent trace array this is equivalent to the diamond law. Nothing in
separate rankwise Hall enforces these identities.

The minimum sufficient global assertion is:

> **Joint tail-order rounding.** For the fixed good cores, select one
> literal tail order and one admissible nested tag profile per top so
> that aggregate physical collision excess over the middle and both
> signed ranks through \(H\) is \(o(W)\).

The deterministic quota deficit is \(O(H^{3/2}N_H)=o(W)\), so this
assertion gives aggregate physical holes \(o(W)\). The \(N_H\) promotion
paths have seam cost

\[
HN_H=O(WH/m)=o(W).
\tag{7.1}
\]

Thus the existing one-baseline reduction would yield coefficient one.
Theorems 2.1 and 5.1 give a common fractional point and show there is no
local tail-order integrality defect. Theorem 6.1 proves that global
physical target identification creates genuine odd cuts. No argument
here proves that all such cuts have only \(o(W)\) total effect. That
global odd-mesh/rounding assertion is the minimum remaining hypothesis.
