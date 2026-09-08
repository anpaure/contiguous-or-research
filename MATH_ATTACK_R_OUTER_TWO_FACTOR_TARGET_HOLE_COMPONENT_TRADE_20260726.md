# Outer trades between two unrelated exact factors

Date: 2026-07-26

Method: pure mathematics only. No web search, computation, finite search,
or solver input is used.

## 0. Outcome

Let \(F^0,F^1\) be two exact owner factors on the same physical owner
universe. They may use unrelated coordinate frames and unrelated internal
orders; no relabelling relation is assumed.

The exact conclusions are as follows.

1. The connected components of the bare owner-overlap graph are exact
   integral owner-trade atoms. They become literal cyclic/multiframe trade
   atoms only after a consistent port closure and a complete additive
   collar ledger have been proved. Under those hypotheses every supported
   hybrid chooses one complete shore in every port-closed group, and
   complementary hybrids together contain exactly the colored row
   multiset \(F^0\sqcup F^1\). Consequently a controlled physical target
   absent from both additive endpoint ledgers can never be created by such
   a two-factor trade.

2. On the remaining targets, the complete simultaneous multidepth
   lower/upper hole functional is exactly a weighted signed coverage
   polynomial. One-child holes are forbidden-subcube clauses;
   complementary-child holes are signed NAE clauses. Multiplicity and
   orbit mass disappear once positivity is taken.

3. There is an exact deterministic product-rounding theorem. If component
   \(K\) is independently switched with probability \(p\), a target with
   \(a\) supporting \(F^0\)-components and \(b\) supporting
   \(F^1\)-components is missed with probability

   \[
   p^a(1-p)^b.                                       \tag{0.1}
   \]

   Successive conditional expectation converts this fractional product
   choice into one literal exact hybrid, with no loss. This is the exact
   certificate inside the independent product-measure family; correlated
   signings may do better.

4. There is also an exact deterministic one-flip drift identity. If
   \(d_t\) is the number of one-sided components capable of serving target
   \(t\), and \(c_t(x)\) is the number currently serving it, then

   \[
   \boxed{
   \sum_K\bigl(\operatorname{Hol}(x\oplus e_K)
                    -\operatorname{Hol}(x)\bigr)
   =
   \sum_{c_t(x)=1}w_t
   -
   \sum_{c_t(x)=0}w_td_t.}                           \tag{0.2}
   \]

   Thus the displayed aggregate inequality is a sufficient deterministic
   descent criterion when component-resolved imports into current holes
   outweigh one-component-fragile current support.

5. For the floor-corrected quadratic collision functional there is a
   stronger genuine coherence theorem. Put

   \[
   A=\left\|\sum_K\delta_K\right\|_w^2,\qquad
   V=\sum_K\|\delta_K\|_w^2,\qquad
   \Gamma=A-V,
   \]

   and \(\Delta=Q(F^1)-Q(F^0)\). If

   \[
   \Gamma>|\Delta|,
   \]

   then one integral exact hybrid beats both seeds by at least

   \[
   \boxed{\frac{(\Gamma-|\Delta|)^2}{4\Gamma}.}       \tag{0.3}
   \]

   Within a physically admissible additive switching cube, this is a true
   two-unrelated-factor descent theorem. It requires aligned
   cross-component profile effects, not merely nonzero orbit motion.

6. No analogous theorem follows from exact ownership and balanced mobility
   axioms alone. An exact abstract \(Q_3\) owner construction below has balanced shore
   masses, nonzero target mobility in every component, and a strict
   one-component local minimum with eight paired holes, although another
   integral hybrid has zero. Disjoint copies give a linear strict trap.
   A second exact family has arbitrarily fine components and target
   residence \(r\), yet every signing has exactly the same hole count.

7. Two independent expansion obstructions remain.

   * If blocks have size \(R\) and every cross-intersection has size at
     most \(\mu\), every overlap component has at least
     \(\lceil R/\mu\rceil\) blocks per shore. Transverse unrelated factors
     therefore have larger, not smaller, trade atoms.
   * At one signed depth, the total target-component residence satisfies

     \[
     \sum_t d_t\le2W.                                \tag{0.4}
     \]

     In the Gaussian band \(q\le A\sqrt m\), the mean residence is only
     \(O_A(1)\). High residence cannot by itself drive the hole count to
     \(o(W)\).

8. The known unrelated suspended-pentagon pair proves genuine mobility:
   it has \(C_{r-4}\) independent five-row components and nonzero literal
   and orbit-projected shadow effects. But its full occurrence action has
   density \(\Theta(1/r)\), and its active carrier is subcritical in the
   audited contiguous-carrier/common-context lift. It does not satisfy the
   new hole-drift or quadratic-coherence gate at coefficient-one scale.

The precise surviving theorem is therefore cyclic and root-scale:
construct two actual critical-scale factors with a proved additive collar
ledger, whose physically legal port-closed overlay is fragmented, whose
union already covers all but \(o(W)\) typed targets, and whose component
effects satisfy either the literal drift inequality
\(G_F>L_F\) until \(o(W)\) holes remain or the coherence inequality
\(\Gamma>|\Delta|\) until the floor-corrected quadratic energy is \(o(W)\).

## 1. Exact owner-overlap components

Let \(\Omega\) be a finite owner set. Let

\[
F^i=\{B^i_1,\ldots,B^i_{b_i}\},\qquad i\in\{0,1\},
\]

be two partitions of \(\Omega\) into legal rows or legal multiframe
blocks. Form the bipartite overlap multigraph \(\mathcal O(F^0,F^1)\):
its vertices are the blocks of the two factors, and each owner
\(X\in\Omega\) gives an edge joining its unique two block owners.

First take the connected components forced by owner overlap. If external
ports, collars, or chronology tokens impose further conditions, the
component theorem below applies under the following explicit
**port-compatibility hypothesis**: after orienting every raw component so
that shore \(0\) comes from \(F^0\), the necessary and sufficient extra
conditions for a supported hybrid to be legal are equalities between raw
component choices. Merge components
joined by those equalities. The resulting groups are called
**port-closed**. (Both all-zero and all-one endpoint choices satisfy every
such equality.) A consistent unpinned system of signed binary parity
constraints has an analogous theorem after gauge orientation, but its two
group shores may mix endpoint colors. Unary fixing, inconsistent parity
cycles, and genuinely higher-order chronology constraints are not
silently covered by the theorem.

### Theorem 1.1 (owner trades, literal under port compatibility)

For every port-closed group \(K\), the two shores partition the same
owner subset

\[
\Omega_K
=\bigcup_{B\in F^0_K}B
=\bigcup_{B\in F^1_K}B.                              \tag{1.1}
\]

Consequently, for every \(x\in\{0,1\}^{\mathcal K}\),

\[
F_x=\bigcup_{K\in\mathcal K}F^{x_K}_K               \tag{1.2}
\]

is one exact owner partition. Under the stated port-compatibility
hypothesis it is also a legal supported row/block factor. Conversely,
every exact factor supported on the colored row union
\(F^0\sqcup F^1\), with precisely those declared binary port constraints,
is of the form (1.2).

The complementary factors obey the colored identity

\[
F_x\sqcup F_{\mathbf1-x}=F^0\sqcup F^1.              \tag{1.3}
\]

#### Proof

If an owner belongs to a block on one shore of \(K\), its unique block on
the other shore is joined to it by that owner's edge and lies in the same
component. This proves both inclusions in (1.1). Choosing one partition of
each \(\Omega_K\) proves exactness of (1.2).

For the converse, write a zero-one variable on every colored row. Every
owner edge requires that its two endpoint row variables sum to one.
Propagating this equation along a connected bipartite component forces one
complete shore to be one and the other zero. Under the stated
port-compatibility hypothesis, the remaining conditions only equate these
raw component choices and hence merge them into port-closed groups.
Finally, complementary choices select the two opposite shores in every
group, proving (1.3).
\(\square\)

All target/profile statements from this point onward use the following
standing **additive-ledger hypothesis**. Every controlled interval
occurrence is assigned to one selected complete row, or to a fully
collared block, so that for every admissible hybrid

\[
\mu(F_x)=\mu_{\mathrm{bg}}+\sum_K\mu_K^{x_K}.         \tag{1.4}
\]

In particular, every crossing seam occurrence must already be assigned
inside a block or fixed background. This is automatic when the selected
atoms are complete literal cyclic rows. It is not automatic for path
pieces or multiframe fragments: changing their concatenation can create a
new seam window absent from both endpoint ledgers. In that setting both
port compatibility and (1.4) require separate proofs.

### Corollary 1.2 (immutable union holes)

Under (1.4), at any collection of depths and signs, the sum of the two complementary
target occurrence histograms is independent of \(x\). Their target-support
union is also independent of \(x\). In particular, a target absent from
both \(F^0\) and \(F^1\) is absent from both complementary children for
every component choice.

Thus two-factor trades can redistribute holes between the two children,
but cannot repair literal union holes of the endpoint pair. Any successful
pair must already have endpoint target-union deficit \(o(W)\).

## 2. Spectral and intersection expansion of the overlap

Assume now that both factors have \(B\ge2\) blocks, every block having the same
owner size \(R\). In this section \(\mathcal O(F^0,F^1)\) means the
**raw owner-overlap graph**, before any port constraints are imposed. Put

\[
w_{ij}=|B^0_i\cap B^1_j|,\qquad
P=(w_{ij}/R)_{i,j\le B}.                              \tag{2.1}
\]

Then \(P\) is doubly stochastic.

### Theorem 2.1 (component spectrum)

The number of connected owner-overlap components equals the multiplicity
of singular value \(1\) of \(P\). In particular,

\[
\sigma_2(P)<1
\quad\Longleftrightarrow\quad
\mathcal O(F^0,F^1)\text{ is connected}.             \tag{2.2}
\]

A connected overlay has one switch bit and produces only the two endpoint
factors.

For \(B=1\) the same conclusion is trivial, with no \(\sigma_2\) notation.

If a separately proved port-compatible closure merges raw components, its
number of free trade classes is at most this multiplicity. The spectrum
does not itself certify the port closure.

#### Proof

Jensen's inequality and double stochasticity give

\[
\|Pz\|_2^2
\le\sum_i\sum_jP_{ij}z_j^2
=\|z\|_2^2.                                          \tag{2.3}
\]

Equality holds precisely when \(z_j\) is constant on the support
neighborhood of every row \(i\). Propagating these equalities shows that
\(z\) is constant on every connected support component, and these
component indicators give all equality vectors. Hence the dimension of
the singular-value-one space is the number of components.
\(\square\)

### Theorem 2.2 (intersection-cap expansion)

If \(0<\mu\) and

\[
\max_{i,j}w_{ij}\le\mu,                               \tag{2.4}
\]

then every component contains at least

\[
k_{\min}=\left\lceil\frac R\mu\right\rceil            \tag{2.5}
\]

blocks on each shore, has owner mass at least \(Rk_{\min}\), and the total
number of switch bits is at most

\[
\frac{B}{k_{\min}}.                                  \tag{2.6}
\]

#### Proof

Fix a left block in a component. Its \(R\) owners are distributed among
right blocks, with at most \(\mu\) owners in any one. It therefore meets at
least \(\lceil R/\mu\rceil\) right blocks in the same component. Equality
of the two shore block counts follows by counting the \(R\)-regular owner
edges. Summing the lower bound over disjoint components proves (2.6).
\(\square\)

For wreath rows, \(R=n=2m+1\). In the transverse case \(\mu=1\), every
component has at least \(n\) rows per shore and \(n^2\) owners, and there
are at most

\[
\frac{W}{n^2}                                        \tag{2.7}
\]

switch bits. Hence “unrelated” in the sense of small row intersections is
opposed to the fragmentation needed for fine trade control.

If the factor blocks are precisely the orbit partitions of successor
permutations \(\sigma,\tau\) on the common owner set, the raw overlap
components are exactly the orbits of
\(\langle\sigma,\tau\rangle\). Transitivity therefore implies a connected
raw overlay directly.

## 3. Exact target-support normal form

Let \(\mathcal T\) be the disjoint union of every controlled physical
target layer, with both signs and all protected depths retained. Give
target \(t\) a weight \(w_t\ge0\), and define

\[
\operatorname{Hol}(F)
=\sum_{t\in\mathcal T}w_t\mathbf1_{\{\mu_F(t)=0\}}.
\]

For component \(K\), let

\[
u_{tK},v_{tK}\in\mathbb Z_{\ge0}                     \tag{3.1}
\]

be the occurrence counts of \(t\) on the \(F^0\)- and \(F^1\)-shores.
Any common background may be included separately.

Call \(t\) **anchored** if it is already in the common background or if
\(u_{tK},v_{tK}>0\) for some \(K\). An anchored target is present in every
hybrid.

For a nonanchored target, put

\[
I_t=\{K:u_{tK}+v_{tK}>0\}.                           \tag{3.2}
\]

On every \(K\in I_t\), exactly one of \(u_{tK},v_{tK}\) is positive. Let
\(s_{tK}\in\{0,1\}\) denote that unique owning shore.

### Theorem 3.1 (forbidden-subcube representation)

For every nonanchored target,

\[
t\text{ is a hole of }F_x
\quad\Longleftrightarrow\quad
x_K\ne s_{tK}\quad\text{for every }K\in I_t.          \tag{3.3}
\]

If \(I_t=\varnothing\), the target is an immutable union hole. For
\(I_t\ne\varnothing\), its hole indicator is one forbidden corner on the
subcube indexed by \(I_t\).

For complementary children,

\[
\mathbf1_{\{t\notin F_x\}}
+\mathbf1_{\{t\notin F_{\mathbf1-x}\}}               \tag{3.4}
\]

equals:

* \(2\) if \(I_t=\varnothing\);
* \(1\) if \(|I_t|=1\);
* the signed NAE violation indicator on \(I_t\) if \(|I_t|\ge2\).

#### Proof

An unanchored target is present exactly when at least one active component
chooses its unique owning shore, which is the negation of (3.3). The
complementary factor chooses every opposite shore. Thus for a nonempty
\(I_t\), one child is a hole precisely at one owning-sign corner and the
other precisely at its antipode. For one variable exactly one event holds;
for at least two variables these are the two monochromatic signed
patterns.
\(\square\)

This theorem shows why orbit-mass mobility is only necessary. A component
may change target multiplicities or orbit totals while retaining exactly
the same positive support, in which case it has no hole action.

For a target orbit \(O\), let \(M_O(x)\) be the child occurrence mass and
\(\bar M_O=(M_O(0)+M_O(1))/2\). Since complementary masses sum to
\(2\bar M_O\),

\[
\boxed{
H_O(x)+H_O(\mathbf1-x)
\ge2\bigl(|O|-\bar M_O\bigr)_+.}                     \tag{3.5}
\]

Indeed \(H_O(y)\ge(|O|-M_O(y))_+\), and the positive part is convex. If
every component has zero \(O\)-mass effect, this displayed orbit-mass lower
floor is immutable; the actual orbit hole count need not be.

## 4. Product interpolation and deterministic rounding

Choose every \(F^1\)-shore independently with probability \(p\). For an
unanchored target define

\[
a_t=|\{K:u_{tK}>0\}|,\qquad
b_t=|\{K:v_{tK}>0\}|.                                \tag{4.1}
\]

Thus \(a_t+b_t=|I_t|\).

### Theorem 4.1 (exact Bernstein hole polynomial)

The expected one-child weighted hole count is

\[
\boxed{
\mathbb E_p\operatorname{Hol}(F_X)
=
\sum_{\substack{t\ \mathrm{unanchored}}}
w_t\,p^{a_t}(1-p)^{b_t}.}                            \tag{4.2}
\]

The expected complementary-pair objective is

\[
\boxed{
\mathbb E_p\!\left[
\operatorname{Hol}(F_X)+\operatorname{Hol}(F_{\mathbf1-X})
\right]
=
\sum_{\substack{t\ \mathrm{unanchored}}}w_t
\left[
p^{a_t}(1-p)^{b_t}
+p^{b_t}(1-p)^{a_t}
\right],}                                            \tag{4.3}
\]

where \(a_t=b_t=0\) gives the immutable value \(2w_t\) for an endpoint-union
hole. Powers with exponent zero are empty products, including at
\(p=0,1\). Anchored targets contribute zero and are omitted.

For every \(p\), there is a deterministic literal component choice whose
objective is no larger than the corresponding right side.

#### Proof

To miss \(t\), every \(F^0\)-owning component must be switched, with
probability \(p^{a_t}\), and every \(F^1\)-owning component must remain
unswitched, with probability \((1-p)^{b_t}\). Independence proves (4.2).
Complementation exchanges \(a_t,b_t\), proving (4.3).

More generally, give every component its own probability \(p_K\). The
expectation is multi-affine in each \(p_K\). Reveal the components one at a
time and replace \(p_K\) by whichever endpoint \(0\) or \(1\) does not
increase the current conditional expectation. The final assignment is
integral, literal, and no worse than the starting product expectation.
\(\square\)

At \(p=1/2\), Theorem 4.1 gives a signing \(x^{(1)}\) with

\[
\operatorname{Hol}(F_{x^{(1)}})
\le
\sum_{\substack{t\ \mathrm{unanchored}}}
w_t2^{-|I_t|},                                       \tag{4.4}
\]

and, possibly for a different signing \(x^{(2)}\),

\[
\operatorname{Hol}(F_{x^{(2)}})
+\operatorname{Hol}(F_{\mathbf1-x^{(2)}})
\le
\sum_{\substack{t\ \mathrm{unanchored}}}
w_t2^{1-|I_t|}.                                      \tag{4.5}
\]

The pair sum includes \(2w_t\) for \(|I_t|=0\); the one-child sum includes
\(w_t\). Each displayed signing handles all depths and both signs included
in its chosen objective. The theorem does not assert that the same signing
simultaneously attains both different bounds.

The interpolation is not universally convex. For one target,
\(p^2\) is convex whereas \(p(1-p)\) is concave. More exactly, the second
derivative at \(p=1/2\) of the symmetrized \((a,b)\) term is

\[
2^{\,3-a-b}\bigl((a-b)^2-(a+b)\bigr).                \tag{4.6}
\]

For verification, logarithmic differentiation of
\(p^a(1-p)^b\) at \(p=1/2\) gives
\(2^{2-a-b}((a-b)^2-(a+b))\); the term with \(a,b\) exchanged is equal,
which proves (4.6).

Thus no endpoint-independent convexity direction exists.

## 5. Exact literal-hole descent

For a choice \(x\) and every nonanchored target, put

\[
c_t(x)=|\{K\in I_t:x_K=s_{tK}\}|,\qquad
d_t=|I_t|.                                           \tag{5.1}
\]

Thus \(c_t(x)=0\) exactly for a hole among the targets not already covered
by common background. All sums in this section are over those
nonanchored targets. Let \(x^{(K)}=x\oplus e_K\).

### Theorem 5.1 (flip-sum identity)

\[
\boxed{
\sum_K\left(
\operatorname{Hol}(F_{x^{(K)}})
-\operatorname{Hol}(F_x)
\right)
=
\sum_{c_t(x)=1}w_t
-\sum_{c_t(x)=0}w_td_t.}                             \tag{5.2}
\]

Therefore, if

\[
\sum_{\text{holes }t}w_td_t
>
\sum_{c_t(x)=1}w_t,                                  \tag{5.3}
\]

some one-component literal trade strictly reduces the complete weighted
hole functional. Repeating such flips gives finite deterministic descent.

#### Proof

A hole has every active component on its nonowning shore. Flipping any one
of its \(d_t\) components covers it, so it contributes \(-w_td_t\) to the
sum. A covered target becomes a hole after one flip exactly when it has one
currently owning component; it then contributes \(+w_t\). All other
targets contribute zero.
\(\square\)

### Corollary 5.2 (local-minimum residence bound)

In the unweighted case, every one-flip local minimum satisfies

\[
\sum_{\text{holes }t}(d_t+1)\le|\mathcal T|.          \tag{5.4}
\]

If \(h_0\) holes are immutable and every other hole has \(d_t\ge d\), then

\[
\boxed{
\operatorname{Hol}(F_x)
\le\frac{|\mathcal T|+dh_0}{d+1}.}                   \tag{5.5}
\]

This is the direct one-component descent consequence of residence alone.

For the complementary-pair objective, targets of degrees zero and one are
immutable. For \(d_t\ge2\), let a violation mean
\(c_t(x)\in\{0,d_t\}\), and write
\(P(x)=\operatorname{Hol}(F_x)+
\operatorname{Hol}(F_{\mathbf1-x})\). With the following sums restricted
to \(d_t\ge2\), the exact pair flip-sum is

\[
\sum_K\bigl(P(x^{(K)})-P(x)\bigr)
=
\sum_{\text{nonviolated }t}w_t
\left(
\mathbf1_{\{c_t=1\}}+\mathbf1_{\{c_t=d_t-1\}}
\right)
-\sum_{\text{violated }t}w_td_t.
\]

Thus a negative right side forces a strict selective trade. At a
one-flip local minimum,

\[
\boxed{
\sum_{\text{violated }t}w_td_t
\le
\sum_{\text{nonviolated }t}w_t
\left(
\mathbf1_{\{c_t=1\}}+\mathbf1_{\{c_t=d_t-1\}}
\right).}                                            \tag{5.6}
\]

Hence, among the nonimmutable targets, if every active degree is at least
\(d\ge3\), there are at most \(|\mathcal T_{\ge2}|/(d+1)\) unweighted
violations. For degree two the bound is only
\(|\mathcal T_{\ge2}|/2\). The complete pair-hole count must additionally
include exactly twice the degree-zero target weight and once the
degree-one target weight.

#### Proof

At a one-flip local minimum every summand on the left of (5.2) is
nonnegative. Hence
\(\sum_{\mathrm{holes}}d_t\le|\{t:c_t=1\}|\), which is at most the number
of nonholes. This gives (5.4), and separating the \(h_0\) degree-zero
holes gives (5.5).

For the pair objective, a violated degree-\(d_t\) target is repaired by
each of its \(d_t\) flips. A nonviolated target can become violated only
by losing its unique owning component when \(c_t=1\), or by gaining its
unique nonowning component when \(c_t=d_t-1\). Summing all flip
increments and using local minimality gives (5.6). In the unweighted
specialization, write \(P\) for the number of violations. If
\(d_t\ge d\ge3\), the two indicators cannot both occur, so
\(dP\le|\mathcal T_{\ge2}|-P\). For \(d=2\), they both occur at
\(c_t=1\), giving \(2P\le2(|\mathcal T_{\ge2}|-P)\).
\(\square\)

### Theorem 5.3 (quantitative endpoint-biased descent)

At the endpoint \(F^0\), define

\[
G_0
=\sum_{\mu_{F^0}(t)=0}w_tb_t,                        \tag{5.7}
\]

\[
L_0
=\sum_{\substack{t\ \mathrm{unanchored}\\a_t=1}}w_t, \tag{5.8}
\]

and

\[
C_0
=
\sum_{\mu_{F^0}(t)=0}w_t\binom{b_t}{2}
+
\sum_{\substack{t\ \mathrm{unanchored}\\a_t\ge2}}w_t.
                                                               \tag{5.9}
\]

For every \(p\in[0,1]\),

\[
\mathbb E_p\operatorname{Hol}(F_X)
\le
\operatorname{Hol}(F^0)
-p(G_0-L_0)+p^2C_0.                                  \tag{5.10}
\]

Consequently \(G_0>L_0\) forces a strict literal exact child. If
\(\gamma=G_0-L_0>0\) and \(C_0>0\), one child improves by at least

\[
\boxed{
\min\left\{\frac{\gamma^2}{4C_0},\frac{\gamma}{4}\right\}.}
                                                               \tag{5.11}
\]

If \(C_0=0\), taking \(p=1\) gives the sharper guaranteed decrease
\(\gamma\).
Every global hole minimizer must therefore obey \(G_0\le L_0\) against
every unrelated comparison factor for which all component hybrids are
physically admissible and satisfy the additive-ledger hypothesis.

#### Proof

For a current hole \(a_t=0\), Bonferroni gives

\[
(1-p)^{b_t}
\le1-b_tp+\binom{b_t}{2}p^2.                         \tag{5.12}
\]

For \(a_t=1\), its term is at most \(p\); for \(a_t\ge2\), it is at most
\(p^2\). Summing gives (5.10). If \(C_0>0\), choose
\(p=\min\{1/2,\gamma/(2C_0)\}\) and use conditional expectation. If
\(C_0=0\), use \(p=1\).
\(\square\)

## 6. Quadratic coherence descent

Let the full depth/sign target profile lie in the weighted Hilbert space
with fixed layer weights \(w_j>0\) and

\[
\|z\|_w^2=\sum_{j,T}w_jz_j(T)^2.                     \tag{6.1}
\]

Write the raw additive profile as

\[
\phi_F=\phi_{\mathrm{bg}}+\sum_K\phi^{x_K}_K,
\]

where \(\phi_{\mathrm{bg}}\) is factor-independent. Subtract any fixed
factor-independent baseline \(g\) and put \(f_F=\phi_F-g\). For component
\(K\), define the intrinsically meaningful raw contribution difference

\[
\delta_K=\phi^1_K-\phi^0_K.                          \tag{6.2}
\]

Then

\[
f_{F^1}=f_{F^0}+\sum_K\delta_K.
\]

Let \(Q(F)=\|f_F\|_w^2-B\), where \(B\) is any fixed floor subtraction.
Define

\[
A=\left\|\sum_K\delta_K\right\|_w^2,\qquad
V=\sum_K\|\delta_K\|_w^2,\qquad
\Gamma=A-V,                                          \tag{6.3}
\]

and

\[
\Delta=Q(F^1)-Q(F^0).                                \tag{6.4}
\]

### Theorem 6.1 (common-bias coherence descent)

Under independent common-bias switching,

\[
\boxed{
\mathbb E_pQ(F_X)
=(1-p)Q(F^0)+pQ(F^1)-p(1-p)\Gamma.}                  \tag{6.5}
\]

If

\[
\Gamma>|\Delta|,                                     \tag{6.6}
\]

then

\[
p_*=\frac{\Gamma-\Delta}{2\Gamma}\in(0,1)            \tag{6.7}
\]

and some integral exact child obeys

\[
\boxed{
Q(F_x)
\le
\min\{Q(F^0),Q(F^1)\}
-\frac{(\Gamma-|\Delta|)^2}{4\Gamma}.}               \tag{6.8}
\]

Conversely, the minimum of the common-bias expectation over
\(0<p<1\) beats both endpoints if and only if (6.6) holds. Let
\(\mathscr F\) be a factor class closed under every admissible
port-compatible hybrid cube under consideration. If \(F_*\) globally
minimizes \(Q\) on \(\mathscr F\), then every \(G\in\mathscr F\) forming
such a cube with \(F_*\) must satisfy

\[
\boxed{
A(F_*,G)-V(F_*,G)
\le Q(G)-Q(F_*).}                                    \tag{6.9}
\]

#### Proof

The random child has mean profile

\[
\mathbb Ef=f_{F^0}+p\sum_K\delta_K
\]

and total coordinate variance \(p(1-p)V\). Hence

\[
\mathbb E\|f\|_w^2
=\left\|f_{F^0}+p\sum_K\delta_K\right\|_w^2
+p(1-p)V.
\]

Expanding the squared norm and using the two endpoint values gives (6.5).
The right side minus \(Q(F^0)\) is

\[
p(\Delta-\Gamma)+\Gamma p^2.
\]

Under (6.6) its minimizer is (6.7). Comparing the resulting value with the
lower endpoint gives (6.8). An expectation is an average of literal exact
children, so one child is no worse. Moreover,

\[
\mathbb E_pQ-Q(F^0)
=p\bigl(\Delta-(1-p)\Gamma\bigr),
\]

while

\[
\mathbb E_pQ-Q(F^1)
=(1-p)\bigl(-\Delta-p\Gamma\bigr).
\]

Both are negative for some \(p\in(0,1)\) exactly when
\(-\Delta/\Gamma<p<1-\Delta/\Gamma\) is feasible with
\(\Gamma>0\), equivalently \(\Gamma>|\Delta|\). At a global minimizer,
the derivative at \(p=0\) must be nonnegative, giving (6.9).
\(\square\)

Here

\[
\Gamma
=2\sum_{K<L}\langle\delta_K,\delta_L\rangle_w        \tag{6.10}
\]

is genuine cross-component coherence. A connected overlay or pairwise
orthogonal component effects gives \(\Gamma=0\), so nonzero orbit mobility
alone does not trigger Theorem 6.1.

### Proposition 6.2 (floor energy controls literal holes)

At one physical layer, let \(N\) be the number of targets, \(W\) the total
occurrence mass, and

\[
\lambda=W/N=c+\theta,\qquad c=\lfloor\lambda\rfloor\ge1.
\]

For an integral load vector \(\mu\), put \(z_T=\mu(T)-c\). Then the exact
floor-corrected quadratic excess is

\[
\begin{aligned}
Q_{\mathrm{fl}}(\mu)
&=\sum_T(\mu(T)-\lambda)^2-N\theta(1-\theta)\\
&=\sum_Tz_T(z_T-1)\ge0.                              \tag{6.11}
\end{aligned}
\]

Every hole contributes \(c(c+1)\), and therefore

\[
\boxed{
\#\{T:\mu(T)=0\}
\le\frac{Q_{\mathrm{fl}}(\mu)}{c(c+1)}.}             \tag{6.12}
\]

For several layers \(j\), if
\(Q_H=\sum_jw_jQ_{\mathrm{fl},j}\) with \(w_j>0\), then the exact
consequence is

\[
\sum_j h_j
\le
\left(\max_j\frac1{w_jc_j(c_j+1)}\right)Q_H.         \tag{6.13}
\]

Thus \(Q_H=o(W)\) implies \(o(W)\) aggregate holes whenever the displayed
maximum is \(O(1)\). In the standard normalization \(w_j=1/c_j\), it is at
most \(1/2\). Arbitrarily small layer weights do not support the
implication. The converse need not hold.

## 7. Residence and component-expansion obstructions

Fix one signed depth. Both endpoint factors have exactly \(W\) target
occurrences. Let \(\mathcal S_{\mathrm{ov}}\) be the targets anchored by a
two-sided selectable component, and let \(\mathcal S_{\mathrm{bg}}\) be
the remaining targets anchored only by factor-independent common
background. For every vulnerable, nonanchored target let
\(d_t=|I_t|\); extend \(d_t=0\) on anchored targets.

### Theorem 7.1 (support-residence budget)

\[
\boxed{
2|\mathcal S_{\mathrm{ov}}|
+\sum_{t\ \mathrm{unanchored}}d_t
\le2W.}                                              \tag{7.1}
\]

In particular,

\[
\sum_td_t\le2W.                                      \tag{7.2}
\]

#### Proof

For each target in \(\mathcal S_{\mathrm{ov}}\), choose one component on
which both shore counts are positive and charge one occurrence on each
shore. Background-only anchors are not charged. For every
unanchored incidence \((t,K)\), charge one occurrence from its unique
positive shore. The charged occurrences are distinct target-component-shore
triples and are bounded by the \(2W\) total occurrences.
\(\square\)

For the odd middle layer,

\[
\lambda_q
=\frac{\binom{2m+1}{m}}{\binom{2m+1}{m-q}}
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.                 \tag{7.3}
\]

For every fixed \(A>0\), uniformly over integers
\(0\le q\le A\sqrt m\) for all sufficiently large \(m\),

\[
\lambda_q\le
\exp\!\left(\frac{q(q+1)}{m-q+1}\right)
=O_A(1).                                             \tag{7.4}
\]

Thus mean target residence in a two-factor cube is at most
\(2\lambda_q=O_A(1)\). Therefore \(d_t\to\infty\) cannot hold on almost
every member of any vulnerable family of positive target density. (It is
not excluded on an \(o(N)\) vulnerable residue when almost all targets are
already anchored.) This blocks the naive use of growing residence to make
(4.4)--(4.5) vanish.

More quantitatively, put

\[
S_{\mathrm{ov}}=|\mathcal S_{\mathrm{ov}}|,\qquad
S_{\mathrm{bg}}=|\mathcal S_{\mathrm{bg}}|,\qquad
V=N-S_{\mathrm{ov}}-S_{\mathrm{bg}}.
\]

If \(V>0\), fair complementary signing has expectation

\[
\sum_{t\ \mathrm{vulnerable}}2^{1-d_t}
\ge
2V\,2^{-(2W-2S_{\mathrm{ov}})/V}.                   \tag{7.5}
\]

For \(V=0\) there is no vulnerable contribution. For \(V>0\), (7.5)
follows from Jensen and (7.1). If
\(S_{\mathrm{ov}}+S_{\mathrm{bg}}=o(N)\) in a Gaussian layer, the right
side is \(\Theta_A(N)=\Theta_A(W)\). Independent component signing
therefore has a linear plateau. A special correlated signed-NAE solution
may still do better.

### Theorem 7.2 (giant-component rigidity)

For a component put

\[
\rho_K=\sum_{t:K\in I_t}w_t.                         \tag{7.6}
\]

Suppose \(K_0\) is a component and

\[
R_{\mathrm{res}}=\sum_{K\ne K_0}\rho_K.              \tag{7.7}
\]

Then every hybrid satisfies

\[
\boxed{
\operatorname{Hol}(F_x)
\ge
\min\{\operatorname{Hol}(F^0),\operatorname{Hol}(F^1)\}
-R_{\mathrm{res}}.}                                 \tag{7.8}
\]

For complementary children,

\[
\boxed{
\operatorname{Hol}(F_x)+\operatorname{Hol}(F_{\mathbf1-x})
\ge
\operatorname{Hol}(F^0)+\operatorname{Hol}(F^1)
-2R_{\mathrm{res}}.}                                \tag{7.9}
\]

#### Proof

According to its choice on \(K_0\), \(F_x\) agrees there with one endpoint.
It differs from that endpoint only on residual components. Flipping
component \(K\) changes the weighted hole count by at most \(\rho_K\).
Triangle inequality proves (7.8). The complementary child agrees on the
giant component with the opposite endpoint, giving (7.9).
\(\square\)

If every owner contributes at most weighted target mass \(J\) on each
shore, and the giant component omits \(r\) owners, then
\(R_{\mathrm{res}}\le2Jr\). (For an unweighted incidence bound \(J_0\),
replace \(J\) by \(J_0\max_tw_t\).) Hence a component containing
\(W-o(W/J)\) owners blocks an \(O(W)\) improvement over two bad endpoints.

## 8. Exact generic countermodels

The next two constructions are exact in the abstract owner/target-incidence
model but carry no coordinate action, so “coordinate relabelling” is not
defined for them. They refute deductions from overlap components, balanced
margins, and target residence alone; they do not refute a theorem that
uses additional literal cyclic geometry or coordinate-unrelatedness.

### Theorem 8.1 (strict \(Q_3\) descent trap)

For every integer \(m\ge1\), there are two abstract exact owner factors with eight
independently switchable connected components satisfying all of the
following.

1. Every component has two rows per shore, and every row owns exactly
   \(n=2m+1\) middle owners and \(n\) target occurrences.
2. Every component has nonzero target-support motion and equal total target
   mass on its two shores.
3. One integral signing is a strict one-component local minimum with eight
   complementary-child holes.
4. Another integral signing has zero complementary-child holes.

Disjoint copies give a linear strict local-minimum gap.

#### Construction and proof

Index the components by \(v\in Q_3\). Within component \(v\), take two rows
on each shore with middle-owner intersection matrix

\[
\begin{pmatrix}m+1&m\\m&m+1\end{pmatrix}.            \tag{8.1}
\]

Every row has \(n\) owners, both shores partition the same \(2n\) owners,
and the \(K_{2,2}\) support is connected.

For every cube edge \(e=uv\), introduce targets \(t_e^+,t_e^-\).
Put \(t_e^+\) on the \(F^1\)-shore at both endpoints and \(t_e^-\) on the
\(F^0\)-shore at both endpoints. Every component has three mobile target
occurrences on each shore. Add \(2n-3\) private targets appearing on both
shores of that component, and split the resulting \(2n\) distinct
occurrences into two \(n\)-target rows per shore.

For a signing \(x:Q_3\to\{0,1\}\),

\[
\operatorname{Hol}(F_x)+\operatorname{Hol}(F_{\mathbf1-x})
=2\,|\{uv\in E(Q_3):x(u)=x(v)\}|.                    \tag{8.2}
\]

The signing \(x(v)=v_1\oplus v_2\) has four monochromatic
direction-three edges and objective eight. Flipping one vertex turns two
bichromatic edges monochromatic and one monochromatic edge bichromatic, so
the objective increases by exactly two. It is a strict local minimum. The
parity signing \(x_*(v)=v_1\oplus v_2\oplus v_3\) makes every edge
bichromatic and has objective zero.
\(\square\)

This is an abstract exact target-incidence factor, not a cyclic-window
realization. It proves that exact ownership, balanced shore masses,
fragmentation, and genuine target mobility do not imply one-component
descent.

### Theorem 8.2 (fine mobility with a flat hole functional)

For integers \(k\ge r\ge2\), put

\[
D=2^{r-1}\binom{k-1}{r-1},\qquad L=D/2.
\]

Define

\[
W_{\mathrm{abs}}=2kD,\qquad
N_{\mathrm{abs}}=2^{r+1}\binom kr.                  \tag{8.3}
\]

Then \(W_{\mathrm{abs}}/N_{\mathrm{abs}}=r/2\).

There are two transversal exact owner factors with \(k\) independent
components, every component having owner mass
\(2D=W_{\mathrm{abs}}/k\), such that:

* every row has \(D\) owners and \(D\) target occurrences;
* every target is one-sided active in exactly \(r\) components;
* for every component signing,

\[
\boxed{
\operatorname{Hol}(F_x)=2\binom kr
=2^{-r}N_{\mathrm{abs}};}                            \tag{8.4}
\]

* every one-component derivative is zero.

#### Construction and proof

For \(i\in[k]\), let

\[
\Omega_i=\{0,1\}^2\times[L].
\]

The \(F^0\)-rows are

\[
\{a\}\times\{0,1\}\times[L],\qquad a\in\{0,1\},
\]

and the \(F^1\)-rows are

\[
\{0,1\}\times\{b\}\times[L],\qquad b\in\{0,1\}.
\]

Their local overlap is a connected \(K_{2,2}\) with \(L\) parallel owner
edges.

Targets are triples

\[
(I,s,u),\qquad I\in\binom{[k]}r,\quad
s\in\{0,1\}^I,\quad u\in\{0,1\}.
\]

Put \((I,s,u)\) in the \(F^0\)-row \((i,u)\) when \(i\in I,s_i=0\), and
in the \(F^1\)-row \((i,u)\) when \(i\in I,s_i=1\). Each row receives
exactly \(D\) distinct targets. For a fixed \(I,u\) and signing \(x\),
exactly one sign word \(s=\mathbf1-x|_I\) is missed. There are
\(2\binom kr\) choices of \(I,u\), proving (8.4). All signings have the
same value, so every derivative is zero.
\(\square\)

This saturates the fair-product bound (4.4). For every prescribed finite
\(r\), it rules out strict repair theorems based only on exactness,
arbitrarily fine component mass, equal row margins, and residence \(r\).
It does not obstruct a separate growing-residence conclusion, since

\[
\frac{\operatorname{Hol}(F_x)}{W_{\mathrm{abs}}}
=\frac{2^{1-r}}r.
\]

Actual cyclic interval geometry must exclude this signed-clause holonomy.

## 9. Actual multiframe specialization and genuine mobility

For two perfect pair frames \(M,N\) on \([2h]\), write their matching union
as alternating coordinate cycles

\[
M\cup N=B_1\sqcup\cdots\sqcup B_c.
\]

For complete pair-status partitions and their orientation flips, the
coarse occupancy supports on the middle layer are

\[
U_{\boldsymbol\kappa}
=\{X:|X\cap B_j|=\kappa_j\text{ for every }j\}.       \tag{9.1}
\]

Every such complete frame transition preserves
\(\boldsymbol\kappa\). For a literal geodesic depth-\(q\) face, a lower
target \(T\) can be served from only those coarse occupancy supports with

\[
\kappa_j=|T\cap B_j|+q_j,\qquad
q_j\ge0,\qquad\sum_jq_j=q.                           \tag{9.2}
\]

Thus it meets at most

\[
\binom{q+c-1}{c-1}                                   \tag{9.3}
\]

coarse occupancy supports \(U_{\boldsymbol\kappa}\). This does not count
refined cycle-overlay components. Upper geodesic targets have the
analogous subtraction formula. When \(c=1\), there is only one global
coarse shore bit and hence no selective coarse mobility. An internal cycle
factor may still fragment the single support
\(U_{\boldsymbol\kappa}\); frame connectivity alone does not prove that
the actual exact-factor overlay is connected. Any additional mobility must
come from that internal fragmentation. Arbitrary packetwise frame
substitutions and nongesodesic windows are not covered by (9.1)--(9.3).

Indeed, for a lower geodesic face the middle owner is
\(X=T\sqcup Q\) with \(|Q|=q\). Setting
\(q_j=|Q\cap B_j|\) gives (9.2), and every possible support is indexed by
a weak composition of \(q\) into \(c\) parts. There are exactly
\(\binom{q+c-1}{c-1}\) such compositions. The upper case applies the same
argument to the deleted set.

We now use two previously proved, independently audited inputs from
MATH_ATTACK_K_TWO_SEED_GROWING_FRINGE_TRADE_20260726.md: the exact
suspended-pentagon component counts and the contiguous-carrier action
theorem. They are imported here rather than reproved.

There is genuine mobility in that unrelated rooted pair. For every
\(r\ge4\), the suspended-pentagon construction supplies
\(C_{r-4}\) independent five-row components, with

\[
\|\mu_1(F^1)-\mu_1(F^0)\|_1=18C_{r-4}                \tag{9.4}
\]

and orbit-projected \(L^1\)-motion \(16C_{r-4}\). Its size-biased component
moment tends to \(69/64\). Hence unrelated exact seeds really can evade
orbit-mass rigidity.

But the full depth-one occurrence-action density is only
\(\Theta(1/r)\), and its active carrier remains bounded under the
first-fringe common-context lift. More precisely, if corresponding cyclic
rows agree outside one contiguous carrier of \(b\) positions and \(H\)
is the number of controlled signed target layers, the statewise
carrier-locality estimate gives aggregate half-\(\ell_1\) action, relative
to an endpoint, at most

\[
\frac{2bH}{2m+1}W.                                   \tag{9.5}
\]

For \(bH=o(m)\), every hybrid differs from an endpoint by only \(o(W)\) in
those controlled layers. Equal-mass hole count is \(1\)-Lipschitz under
half-\(\ell_1\) transport, so such a lift cannot repair a linear
Gaussian-band hole deficit. This conclusion uses the stated
contiguous-carrier/common-context hypothesis; it is not asserted for an
arbitrary pentagon lift. For the displayed suspended pentagon, \(b=9\).

## 10. Precise surviving gate

The two-factor lane is not closed, but its generic form is.

The following are proved:

* unrelated exact factors give unconditional integral owner-component
  trades; they give literal cyclic/multiframe trades under the proved
  port-compatibility and additive-ledger hypotheses;
* target-union holes of the additive endpoint pair are immutable;
* product interpolation, conditional expectation, flip-sum descent, and
  the quadratic coherence theorem are exact and simultaneous over all
  depths and signs;
* transverse owner overlap and phase transitivity enlarge components and
  reduce switch mobility;
* mean target residence is only \(O_A(1)\) in a Gaussian layer;
* fine components, equal shore masses, active-degree expansion, and nonzero
  orbit motion do not generically imply literal-hole descent.

What remains unproved is a cyclic-window-specific critical pair satisfying
all of:

1. the physical target union of the two seeds has only \(o(W)\) aggregate
   holes;
2. the owner overlay has enough fragmented components after a physically
   legal packet system has been constructed and its signed-affine port
   constraints (or any genuinely higher-order chronology constraints)
   have been classified; unsigned graph closure is insufficient;
3. the components have root-scale physical action rather than merely a
   marked or bounded-carrier effect;
4. throughout descent, either

   \[
   G_F-L_F>0                                         \tag{10.1}
   \]

   with a quantitative margin until \(o(W)\) holes remain, or

   \[
   \Gamma>|\Delta|                                   \tag{10.2}
   \]

   until the floor-corrected quadratic energy is \(o(W)\);
5. actual cyclic interval signs exclude both the strict \(Q_3\) trap and
   the flat signed-clause construction.

This is the exact deterministic boundary. Two unrelated factors supply
owner integrality, and particular pairs such as the suspended pentagon can
supply genuine orbit-mass mobility. They do not, without the stated
legality, additive-collar, and cyclic expansion/coherence inputs, supply
coefficient-one target-hole repair.
