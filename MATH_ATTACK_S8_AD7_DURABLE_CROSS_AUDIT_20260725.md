# S8: adversarial audit of AD7 and stopped-thread durable obstructions

Date: 2026-07-25

## 0. Exact outcome

Put

\[
n=2m,
\qquad
W=\binom{2m}{m},
\qquad
N_q=\binom{2m}{m-q},
\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed. This report cross-audits
MATH_ATTACK_AD7_CROSS_COMPONENT_SUPPORT_TRACE_OBSTRUCTION_20260725.md
against the exact active-flag/durable-edge formulation of
MATH_ATTACK_S7_DYNAMIC_FLAG_FUSION_20260725.md.

The three requested AD7 arguments survive with the following exact
qualifications.

1. The clean-threading variation identities and their constants are
   correct. The phrase "fixed legal dummy continuation" must mean one
   coherent, shift-compatible, no-short-return continuation on each path.
   Independently chosen ownerwise dummies do not suffice.
2. The capped trace-energy inequality has sharp scalar constant \(1\), and
   the entropy bound has the stated natural-log Pinsker constant \(1/2\):

   \[
   \mathbb E_\sigma\Phi_Z(\sigma\mathcal H)
   \ge
   M\left(1-
   \sqrt{\frac{t}{2n}\log\frac{2^n}{M}}
   \right).
   \]
3. The conditional clean zero-hole word length

   \[
   W+2Hp=W+\frac{2HW}{m+1}
   \]

   is exact under the previously audited augmented
   last-occurrence/unseen-residual convention. A full ordered-partition
   reset convention would instead charge one additional letter per
   component. The report should explicitly include the block-update proof
   given below.

None of these facts supplies the two missing S7 assertions. The reason is
not a small quantitative loss. AD7 uses all \(W\) owners at every depth
and asks only for support-surjective maps, with repetitions. S7 uses the
prescribed active set \(X_q\), of size exactly \(N_q\), and requires a
literal bijection at every depth. The missing operation is a nested common
transversal, not an averaging step.

This report proves four further exact statements.

* Flag-family nonemptiness is equivalent layer by layer to an exact
  stopped-set Hall inequality.
* Odd-cut path geometry and global contiguity alone do not imply
  nonemptiness. Reordering whole complementary-geodesic components can make
  \(\mathfrak F^-_\tau\) empty at the first layer. This is not, by itself,
  an AD7 counterexample because the odd-cut forest's lower first-band
  rainbow property remains unproved.
* Every compatible active flag pair obeys a stopped-thread curvature
  inequality

  \[
  \sum_{j=1}^{H-1}
  \|D_{j+1}-D_j+S_j\|_1
  \le
  2\sum_{j=1}^{H-1}\rho^0_{j+1}+2HK_H.
  \]

  The restitution term \(S_j\) is mandatory.
* The durable-edge formula yields exact portal-cut lower bounds and a
  positive probabilistic sufficient criterion. These sharpen the gate,
  but they do not prove \(K_H^{\min}=o(W/H)\).

Thus the audited endpoint is

\[
\boxed{
\text{AD7's owner marginals, clean variation necessity, and trace entropy
do not supply the active common transversal or a small labelled durable
defect.}}
\]

For a separately frozen component order the two assertions may still be
true. They remain unproved.

---

## 1. Audit of the clean-threading variation bound

Let a directed path forest on the \(W\) middle owners have \(p\)
components. For a full-depth lower owner flag, write \(d_j(v)\) for its
\(j\)-th deletion coordinate and

\[
D_j(x)=|\{v:d_j(v)=x\}|.
\]

Suppose every actual edge \(v\to w\) satisfies

\[
d_j(w)=d_{j+1}(v),
\qquad 1\le j<H.
\tag{1.1}
\]

Let \(\sigma_j\) be the source histogram of \(d_j\), and let
\(\tau_{j+1}\) be the terminal histogram of \(d_{j+1}\). Cancelling the
contributions paired by all internal path edges gives, with the signs in
the AD7 report,

\[
\boxed{D_{j+1}-D_j=\tau_{j+1}-\sigma_j.}
\tag{1.2}
\]

Both boundary histograms have mass \(p\). Therefore

\[
\boxed{\|D_{j+1}-D_j\|_1\le 2p}
\tag{1.3}
\]

and

\[
\boxed{
\sum_{j=1}^{H-1}\|D_{j+1}-D_j\|_1
\le 2p(H-1).}
\tag{1.4}
\]

Since \(D_j=I_{j-1}-I_j\), the incidence-curvature formula follows with
the same constant. There is no missing factor two.

For a two-sided clean threading, the lower boundary differences, the
central \(A_1-D_1\) difference, and the upper boundary differences give
exactly

\[
(H-1)+1+(H-1)=2H-1
\]

histogram norms. Each is at most \(2p\), so

\[
\boxed{\mathfrak V_H\le 2(2H-1)p.}
\tag{1.5}
\]

The terminal-minus-source sign for the lower family and the
source-minus-terminal sign for the upper family in AD7 are correct.

### Dummy-continuation qualification

Equation (1.1) at vertices near a path endpoint is meaningful only if the
dummy slots are chosen coherently along the whole path. A merely legal
Johnson step chosen independently at each owner can violate both the shift
identity and nestedness of the deletion flag.

For an intended complementary no-return path

\[
T_0\to T_1\to\cdots\to T_m=T_0^c,
\]

with departure coordinates \(x_1,\ldots,x_m\) and arrival coordinates
\(y_1,\ldots,y_m\), a coherent continuation is available: after \(T_m\),
depart \(y_1,\ldots,y_m\) while reinserting \(x_1,\ldots,x_m\). Every
window of at most \(m\) successive departures has distinct symbols and is
legal from its starting state. Thus the intended range \(H\le m-1\), and
in particular fixed \(A\) with \(H=\lceil A\sqrt m\rceil\) for all large
\(m\), admits the required coherent continuation.

This repairs the finite wording. It does not change any asymptotic
constant.

---

## 2. Audit of the trace-energy and entropy inequalities

Let the distinct hole family be split into signed-rank layers

\[
\mathcal H=\bigsqcup_\alpha\mathcal H_\alpha.
\]

Fix \(Z\subsetneq[n]\), put \(t=|Z|\), \(d=n-t\), and let
\(h_{\alpha,R}\) and \(h_R\) be the layer and aggregate loads in trace
\(R\subseteq Z\). Put

\[
\ell_R=\nu(d)+\mathbf 1_{R\ne\varnothing}.
\]

### Lemma 2.1 (sharp capped cross-product inequality)

If \(0\le x_i\le L\), then

\[
\boxed{
\sum_{i<j}x_ix_j
\ge L\left(\sum_i x_i-L\right)_+.}
\tag{2.1}
\]

#### Proof

Scale to \(L=1\). For fixed \(x=\sum_i x_i=k+r\), with
\(k=\lfloor x\rfloor\) and \(0\le r<1\), the convex function
\(\sum_i x_i^2\) is maximized by \(k\) ones, one entry \(r\), and zeros.
Hence

\[
\sum_{i<j}x_ix_j
\ge \frac{k(k-1)}2+kr.
\]

For \(k\ge1\), subtracting \(x-1=k+r-1\) leaves

\[
\frac{(k-1)(k-2)}2+r(k-1)\ge0.
\]

The constant \(1\) is sharp, for example at the vector
\((1,r,0,\ldots)\). \(\square\)

For every trace cell in one signed-rank layer,

\[
h_{\alpha,R}
\le \binom d{r_\alpha-|R|}
\le \binom d{\lfloor d/2\rfloor}
\le \nu(d)
\le\ell_R.
\tag{2.2}
\]

Applying Lemma 2.1 inside every trace and using

\[
M-\Phi_Z=\sum_R(h_R-\ell_R)_+
\]

gives

\[
\boxed{
M-\Phi_Z
\le\sum_R\frac{E_R^\times}{\ell_R}
\le\frac{E_Z^\times}{\nu(d)}.}
\tag{2.3}
\]

Both denominator directions are correct. No factor two is missing from
the cross-rank pair energy.

### Theorem 2.2 (entropy bound, audited constants)

Let \(\mathcal H\subseteq2^{[n]}\) have \(1\le M\le W_n\), where

\[
W_n=\binom n{\lfloor n/2\rfloor}.
\]

For fixed \(|Z|=t<n\) and uniform \(\sigma\in S_n\),

\[
\boxed{
\mathbb E_\sigma\Phi_Z(\sigma\mathcal H)
\ge
M\left(1-
\sqrt{\frac{t}{2n}\log\frac{2^n}{M}}
\right).}
\tag{2.4}
\]

Moreover, for every \(\eta>0\),

\[
\boxed{
\Pr_\sigma\{\Phi_Z(\sigma\mathcal H)<(1-\eta)M\}
\le
\frac1\eta
\sqrt{\frac{t}{2n}\log\frac{2^n}{M}}.}
\tag{2.5}
\]

#### Audit proof

Let \(X\) be uniform on \(\mathcal H\), and let \(Y\) be a uniform
\(t\)-subset. Shearer's projection inequality has the direction

\[
\mathbb E_Y H(X\cap Y)\ge\frac tn\log M.
\tag{2.6}
\]

If \(p_Y\) is the trace law and \(u_Y\) is uniform on \(2^Y\), then

\[
\mathbb E_YD(p_Y\|u_Y)
\le\frac tn\log\frac{2^n}{M}.
\tag{2.7}
\]

Natural-log Pinsker and Jensen give

\[
\mathbb E_Y\|p_Y-u_Y\|_{\rm TV}
\le
\sqrt{\frac{t}{2n}\log\frac{2^n}{M}}.
\tag{2.8}
\]

The central-binomial ratios satisfy

\[
2^{-d}W_d\ge 2^{-n}W_n,
\qquad d=n-t,
\]

or equivalently \(W_d\ge2^{-t}W_n\ge2^{-t}M\). Therefore

\[
\begin{aligned}
M-\Phi_Y
&=\sum_R(h_R-\ell_R)_+\\
&\le\sum_R(h_R-W_d)_+\\
&\le M\sum_R(p_Y(R)-2^{-t})_+\\
&=M\|p_Y-u_Y\|_{\rm TV}.
\end{aligned}
\tag{2.9}
\]

A uniform relabelling makes \(\sigma^{-1}Z\) a uniform \(t\)-set. Taking
expectations proves (2.4), and Markov's inequality applied to
\(M-\Phi_Z\) proves (2.5). Thus the square-root constant and all
quantifiers in AD7 are correct.

The optimized identity

\[
\min_{|Z|=t}\Phi_Z(\sigma\mathcal H)
=\min_{|Z|=t}\Phi_Z(\mathcal H)
\]

is also exact: \(Z\mapsto\sigma^{-1}Z\) bijects the marked sets and their
trace cells. The downstream entropy-profile bound in AD7 follows from
the same calculation; its use of \(h_2(\varepsilon/c)\) has the correct
monotonicity on \(0\le\varepsilon/c\le1/2\).

### Scope for the durable problem

The trace theorems start with a nonempty hole family. They do not produce
owner flags. Once an S7 flag system exists, every active rank map is
bijective, so its hole family is empty and the trace deficiency is
identically zero. The entropy theorem is then vacuous and is not invoked,
because its logarithm was stated under \(M\ge1\).
For an AD7 all-owner map, the global hole family is likewise empty, while
the restriction to \(X_q\) can have holes of arbitrary size. Nothing in
the entropy argument transfers providers from inactive owners into
\(X_q\).

Thus trace entropy is a correct obstruction to compressing an already
present aggregate hole family. It is not a nonemptiness theorem and it
does not estimate a labelled durable-edge set.

---

## 3. Audit of the conditional zero-hole length

Let \(F\) be the exact first-band forest with \(p=W/(m+1)\) components.
Suppose a full owner flag family covers every central-band target and,
for every path edge \(v\to w\), satisfies

\[
d_j(w)=d_{j+1}(v)\quad(1\le j<H),
\tag{3.1}
\]

\[
a_1(w)=d_1(v),
\qquad
a_{j+1}(w)=a_j(v)\quad(1\le j<H),
\tag{3.2}
\]

and

\[
d_H(w)\in F^-_{v,H}.
\tag{3.3}
\]

Put \(L_v=F^-_{v,H}\), write

\[
w=v-\{x\}+\{y\},
\qquad x=d_1(v),
\]

and put \(\delta=d_H(w)\). Equations (3.1) and (3.3) give the exact core
update

\[
\boxed{L_w=L_v-\{\delta\}+\{y\}.}
\tag{3.4}
\]

Initialize one component with useful prefix

\[
(L_v,d_H(v),\ldots,d_1(v),a_1(v),\ldots,a_H(v)).
\tag{3.5}
\]

Appending the single nonzero mask \(L_w\) gives useful prefix

\[
(L_w,\delta,d_H(v),\ldots,d_2(v),d_1(v),
  a_1(v),\ldots,a_{H-1}(v)),
\]

which is precisely the prefix required at \(w\) after applying
(3.1)--(3.2). No required upper singleton is erased: the only new
coordinate of \(L_w\setminus v\) is \(y\), and
\(y\ne a_j(v)\) for \(j<H\), because
\(a_{j+1}(w)=a_j(v)\notin w\). The last symbol \(a_H(v)\) may be demoted
to the irrelevant tail.

A component with \(r\) owners therefore costs

\[
(2H+1)+(r-1)=r+2H
\]

letters. Summing over all components gives

\[
\boxed{L_{\rm band}=W+2Hp.}
\tag{3.6}
\]

Every displayed block is nonempty when \(H\le m-1\), and every required
flag is a literal suffix OR. This verifies the conditional zero-band-hole
claim.

The exact count (3.6) uses the accepted augmented
last-occurrence/unseen-residual initialization. If one insists on writing
one additional residual block to initialize a full ordered partition at
every component, the corresponding count is

\[
W+(2H+1)p.
\]

This is a convention qualification, not a hidden asymptotic problem.

For fixed \(A\),

\[
W+\frac{2HW}{m+1}=W+o_A(W).
\]

It is a literal central-band word, not a full universal word and not an
SCD. A coefficient-one conclusion would still require the separately
audited outer-tail step, with \(m\to\infty\) first for fixed \(A\), then
\(A\to\infty\), or a justified diagonal. Most importantly, existence of
flags satisfying (3.1)--(3.3) is conditional; AD7's static owner routing
does not prove it.

---

## 4. The exact common-transversal gap

The static completion theorem used here also passes its audit. Its terminal
owner family has size \(p\le W/2\), and

\[
\frac W2=\binom{2m-1}{m}
\]

is the exact threshold at which the Lovász--Kruskal--Katona lower-shadow
bound gives at least one facet per owner. Hall therefore supplies distinct
terminal facets. The same argument after complementation supplies the
initial upper cofacets. At every deeper rank, an injection of the complete
next layer into the current layer selects one already-present owner token
at each image; the other tokens may move arbitrarily. This proves integral
nested support, but only support. At depth one the \(p\) extra facets are
distinct, so exactly \(p\) targets have load two and every other target has
load one. No corresponding balanced-load claim is proved for \(q\ge2\).

Let an AD7 all-owner flag family be fixed. At depth \(q\), form the
bipartite multigraph \(\Gamma_q\) whose two vertex classes are copies of

\[
Y_q=\binom{[2m]}{m-q},
\]

and in which owner \(v\) contributes the labelled edge

\[
e_v=\bigl(F^-_{v,q},\ [2m]\setminus F^+_{v,q}\bigr).
\tag{4.1}
\]

AD7 support-surjectivity says exactly that \(\Gamma_q\) has no isolated
vertex on either side. It does not say that a prescribed set of \(N_q\)
owner edges is a perfect matching.

### Proposition 4.1 (restriction defect identity)

Let \(f_q:X\to Y_q\) be either one of the all-owner endpoint maps, and let
\(X_q\subseteq X\) have \(|X_q|=|Y_q|=N_q\). Define

\[
h_q=|\{S\in Y_q:f_q^{-1}(S)\cap X_q=\varnothing\}|.
\]

Then

\[
\boxed{
\sum_{S\in Y_q}
\bigl(|f_q^{-1}(S)\cap X_q|-1\bigr)_+=h_q.}
\tag{4.2}
\]

Consequently \(f_q|_{X_q}\) is bijective if and only if \(h_q=0\).

#### Proof

The restricted loads are nonnegative integers summing to \(N_q=|Y_q|\).
For every such load vector, total excess above one equals total deficiency
below one. Since a deficient integral cell has load zero, the deficiency
is exactly \(h_q\). \(\square\)

At \(q=1\), AD7's all-owner load vector has exactly \(p\) double fibres
and all other fibres singleton. If \(I=X\setminus X_1\) has size \(p\),
then the restriction is bijective exactly when \(I\) avoids every
singleton-fibre provider and contains exactly one provider from every
double fibre.

For a prescribed lifetime system, the AD flags restrict to an S7 flag pair
if and only if the fixed owner set \(X_q\) is a perfect matching of
\(\Gamma_q\) for every \(q\), with the restrictions nested across \(q\).
If the lifetime system is itself selectable, this becomes the existence of
nested common transversals

\[
X_H\subset\cdots\subset X_1\subset X_0.
\]

No-isolated-vertex support is strictly weaker than Hall, and neither the
variation statistic nor trace entropy supplies this common transversal.

### Proposition 4.2 (conditional zero-durable-defect bridge)

Suppose, in addition, that the all-owner AD flags obey the clean shift
identities (3.1)--(3.2) on every initial forest edge. If their restrictions
to the prescribed \(X_q\) are bijective at every depth on both signs, then

\[
\boxed{K_H^{\min}=0.}
\tag{4.3}
\]

#### Proof

Nestedness is inherited from the all-owner flags, so the restrictions are
members of \(\mathfrak F^-_\tau\) and \(\mathfrak F^+_\tau\). Along an
edge \(v\to w\), the lower shifts give, for every active level \(h\),

\[
F^-_{v,h+1}=F^-_{v,h}\cap F^-_{w,h}.
\]

Writing \(R_h(v)=[2m]\setminus F^+_{v,h}\), the upper shifts give

\[
R_{h+1}(w)=R_h(v)\cap R_h(w).
\]

Thus every edge in \(E^\circ\) is durable. The exact formula

\[
K_H^{\min}
=|E^\circ|-\max_{\mathbf L,\mathbf R}|E^{\rm dur}(\mathbf L,\mathbf R)|
\]

gives (4.3). Notice that the deepest-core condition (3.3), needed for the
all-owner literal update at depth \(H\), is not needed for S7 durability,
whose last identity is at level \(H-1\). \(\square\)

This proposition is the strongest valid positive bridge from AD7 to the
durable formula. Its common-transversal premise is exactly what remains
unproved.

The deepest-load shadow inequalities in AD7 also have the correct floor
\(W-N_q\): at \(q=H\), duplicate excess minus missing mass is exactly
\(W-N_H\), and at \(q=0\) distinct middle ownership supplies the required
matching into the middle upper shadow. These inequalities remain
necessary owner-marginal tests and do not alter the common-transversal
gap.

---

## 5. Exact stopped-set Hall criteria and a contiguity counterexample

Write

\[
C_0=X\setminus X_1,
\qquad |C_0|=W-N_1=p.
\]

For a family

\[
\mathcal A\subseteq\binom{[2m]}{m-1},
\]

let \(\nabla\mathcal A\) be its family of middle supersets.

### Theorem 5.1 (exact first stopped-layer Hall criterion)

A lower first-layer bijection

\[
L_1:X_1\longrightarrow\binom{[2m]}{m-1},
\qquad L_1(v)\subset v,
\]

exists if and only if

\[
\boxed{
|C_0\cap\nabla\mathcal A|
\le |\nabla\mathcal A|-|\mathcal A|
\quad\text{for every }\mathcal A.}
\tag{5.1}
\]

The upper-complement first layer exists if and only if the same inequality
holds with

\[
C_0^*=\{[2m]\setminus v:v\in C_0\}.
\]

#### Proof

The active providers of the targets in \(\mathcal A\) are exactly

\[
\nabla\mathcal A\setminus C_0.
\]

Hall's theorem, applied on the target side of the equal-size incidence
graph, says that a perfect matching exists exactly when

\[
|\nabla\mathcal A\setminus C_0|\ge|\mathcal A|
\]

for every \(\mathcal A\). This is (5.1). Complementation proves the
upper statement. \(\square\)

More generally, after \(L_h\) has been chosen, put

\[
C_h=L_h(X_h\setminus X_{h+1})
\subseteq\binom{[2m]}{m-h}.
\tag{5.2}
\]

The next lower bijection exists exactly when

\[
\boxed{
|C_h\cap\nabla\mathcal A|
\le |\nabla\mathcal A|-|\mathcal A|}
\tag{5.3}
\]

for every family \(\mathcal A\) in rank \(m-h-1\). This is the same
proof after transporting the owner set through the bijection \(L_h\).
The upper-complement criterion is identical. Hence nonemptiness of the
full flag families is a nested sequence of stopped-set Hall inequalities.

### Theorem 5.2 (globally contiguous odd-cut geometry counterexample)

For every sufficiently large \(m\), there is an ordering of the components
of the exact odd-cut complementary-geodesic forest for which the prescribed
globally contiguous lifetime ledger has

\[
\boxed{\mathfrak F^-_\tau=\varnothing.}
\tag{5.4}
\]

#### Proof

The forest has

\[
p=\frac{W}{m+1}
\]

components, each with \(m+1\) middle vertices. Fix an
\((m-1)\)-set \(S\), and let

\[
\mathcal U(S)=\{S\cup\{x\}:x\notin S\}.
\]

This middle star has \(m+1\) owners. At most \(m+1\) path components meet
it, so all components meeting the star contain at most

\[
(m+1)^2
\]

vertices in total. Since

\[
\frac{W}{m+1}>(m+1)^2
\]

for all sufficiently large \(m\), order all components meeting
\(\mathcal U(S)\) first and then order the remaining components
arbitrarily.

For completeness, the displayed eventual inequality follows elementarily
from

\[
W=\max_r\binom{2m}{r}\ge\frac{4^m}{2m+1};
\]

the exponential lower bound divided by \(m+1\) eventually exceeds
\((m+1)^2\).

The first lifetime block has exact size

\[
c_0=W-N_1=\frac{W}{m+1}=p.
\]

It therefore contains the whole star \(\mathcal U(S)\). Thus no active
owner in \(X_1\) contains \(S\). A lower bijection \(L_1\) would have to
assign \(S\) to an active middle owner containing it, which is impossible.
Equivalently, (5.1) fails for \(\mathcal A=\{S\}\). \(\square\)

Reordering components changes neither the exact odd-cut forest nor its
known join ledger, and the lifetime assignment remains one globally
contiguous prefix/suffix ledger. It proves that equal complementary
geodesics plus global contiguity do not imply S7 nonemptiness.

This is **not** an unconditional AD7-to-S7 counterexample. AD7 Theorem 1.3
also assumes that the edge meets exhaust the complete lower first-band
rank. That property is the unresolved odd-cut meet-rainbow gate. If a
two-sided-rainbow complementary-geodesic factor were proved, the same
component reordering would preserve both ledgers and would then give the
advertised AD7 counterexample. Without that additional theorem, the scope
must stop at odd-cut geometry.

The theorem does **not** assert that a separately fixed canonical component
order is bad. It proves that its order must be used in any positive Hall
proof; it cannot be discarded as irrelevant bookkeeping.

The four-symbol local construction in AD7 was also checked: the
\(2H-2\) common nonanchor ranks and the \(9\), respectively \(12\),
distinct anchor targets give exactly \(2H+7\) for three flags and
\(2H+10\) for four. The resulting Hall gaps \(H-7\) and \(2H-10\) are
correct. Its stated scope is essential: the flags are individually
long-geodesic realizable, but simultaneous occurrence inside one exact
owner-disjoint factor is not proved.

---

## 6. Exact durable-edge obstruction tests

Assume from now on that both active flag families are nonempty, and fix a
pair \((\mathbf L,\mathbf R)\).

### 6.1 Portal-cut inequality

At level \(h\), let \(Q_h\) be the initial edges with common lifetime at
least \(h+1\) which satisfy all durable identities at levels below \(h\).
These are precisely the edges reaching the level-\(h\) active lift.

For

\[
\mathcal A\subseteq\binom{[2m]}{m-h-1},
\]

define the lower portal owners

\[
P_h(\mathcal A)
=\{v\in X_{h+1}:S\subset L_h(v)
\text{ for some }S\in\mathcal A\},
\tag{6.1}
\]

and the bad candidate edges

\[
B_h^-(\mathcal A)
=\{e=v\to w\in Q_h:
v\in P_h(\mathcal A),\
L_h(v)\cap L_h(w)\notin\mathcal A\}.
\tag{6.2}
\]

### Theorem 6.1 (portal-cut lower bound)

For every \(0\le h<H\) and \(\mathcal A\),

\[
\boxed{
K_H(\mathbf L,\mathbf R)
\ge
\left[
|B_h^-(\mathcal A)|-|P_h(\mathcal A)|+|\mathcal A|
\right]_+.}
\tag{6.3}
\]

#### Proof

Because \(L_{h+1}\) is bijective, exactly \(|\mathcal A|\) portal owners
map into \(\mathcal A\). A bad candidate edge that survives level \(h\)
forces its tail to the displayed intersection target outside
\(\mathcal A\). The surviving bad candidates have distinct tails, so at
most

\[
|P_h(\mathcal A)|-|\mathcal A|
\]

of them can survive. Every remaining candidate fails at level \(h\) and
is counted once by the global first-failure formula. \(\square\)

There is an identical upper-complement inequality, using heads and the
forced target \(R_h(v)\cap R_h(w)\).

At \(h=0\), no unknown positive-depth flag occurs. Since
\(Q_0=E^\circ\),

\[
\boxed{
K_H^{\min}
\ge
\max_{\mathcal A}
\left[
\#\{e=v\to w\in E^\circ:
v\in X_1\cap\nabla\mathcal A,\
v\cap w\notin\mathcal A\}
-|X_1\cap\nabla\mathcal A|+|\mathcal A|
\right]_+.}
\tag{6.4}
\]

For a fixed flag pair, if families \(\mathcal A_i\) give positive deficits
\(\delta_i\), every candidate edge belongs to at most \(d\) of the
corresponding bad sets, and \(d\ge1\), double counting gives

\[
\boxed{K_H\ge\left\lceil\frac{\sum_i\delta_i}{d}\right\rceil.}
\tag{6.5}
\]

For \(h>0\), the sets in (6.1)--(6.2) depend on the chosen flags, so these
are fixed-pair dual bounds unless one subsequently minimizes them
uniformly. Only the \(h=0\) specialization (6.4) directly bounds
\(K_H^{\min}\) without an additional minimization.

### 6.2 Exact depth-zero criterion for zero cuts

Let \(G=F_0[X_1]\) have \(b\) path components. A necessary zero-cut
condition is that its \(N_1-b\) internal edges have pairwise distinct
forced lower colours and pairwise distinct forced upper-complement
colours. Assume this injectivity condition, and let \(Y^-_{\rm miss}\) and
\(Y^+_{\rm miss}\) be the two missing colour families, each of size \(b\).

Then all edges of \(G\) survive the first lift if and only if

1. the \(b\) terminal vertices of \(G\) admit a perfect containment
   matching to \(Y^-_{\rm miss}\), and
2. the \(b\) source vertices admit a perfect containment matching to
   \(Y^+_{\rm miss}\).

Without the injectivity condition, zero cuts are impossible. Under it,
every nonterminal lower slot and every nonsource
upper-complement slot is forced by an internal edge. The two stated
boundary matchings are therefore necessary, and they independently fill
all remaining targets, so they are sufficient. This is the exact
first-layer zero-cut gate hidden by owner-marginal support.

### 6.3 Stopped-thread curvature

For \(1\le j\le H\), define the lower deletion coordinate on the active
owners by

\[
d_j(v)=L_{j-1}(v)\setminus L_j(v),
\qquad v\in X_j,
\]

and let \(D_j\) be its coordinate histogram. For \(1\le j<H\), let
\(S_j\) be the histogram of \(d_j(v)\) over owners stopping at depth \(j\):

\[
v\in X_j\setminus X_{j+1}.
\]

For \(1\le j<H\), let

\[
G_{j+1}=F_0[X_{j+1}]
\]

be the structural active forest and put

\[
a_j=|E(G_{j+1})|,
\qquad
\rho^0_{j+1}=N_{j+1}-a_j.
\tag{6.6}
\]

Thus \(\rho^0_{j+1}\) is the number of components, including isolated
vertices, of the structural active path forest. Use canonical maximal
retention for the fixed flags, and let \(F^{\rm surv}_{j+1}\) be the actual
survivor forest after enforcing **both** durable identities at every level
\(0,\ldots,j\). Put

\[
e_j=|E(F^{\rm surv}_{j+1})|,
\qquad
b_j=a_j-e_j,
\qquad
\kappa_{j+1}=N_{j+1}-e_j
             =\rho^0_{j+1}+b_j.
\tag{6.7}
\]

Here \(\kappa_{j+1}\) is exactly the component count of the actual survivor
forest, not a histogram surrogate. Let
\(\tau^{\rm term}_{j+1}\) be the \(d_{j+1}\)-histogram on its terminals,
and let \(\sigma^{\rm src}_j\) be the \(d_j\)-histogram on its sources.

### Theorem 6.2 (stopped-thread variation inequality)

For every \(1\le j<H\), the exact active restitution identity is

\[
\boxed{
D_{j+1}-D_j+S_j
=\tau^{\rm term}_{j+1}-\sigma^{\rm src}_j.}
\tag{6.8a}
\]

Both boundary histograms have mass \(\kappa_{j+1}\). Consequently,

\[
\boxed{
\|D_{j+1}-D_j+S_j\|_1
\le2\kappa_{j+1}
=2(\rho^0_{j+1}+b_j).}
\tag{6.8b}
\]

Consequently,

\[
\boxed{
\sum_{j=1}^{H-1}
\|D_{j+1}-D_j+S_j\|_1
\le
2\sum_{j=1}^{H-1}\rho^0_{j+1}+2HK_H.}
\tag{6.9}
\]

Equivalently,

\[
\boxed{
K_H
\ge\frac1{2H}
\left[
\sum_{j=1}^{H-1}\|D_{j+1}-D_j+S_j\|_1
-2\sum_{j=1}^{H-1}\rho^0_{j+1}
\right]_+.}
\tag{6.10}
\]

The same three formulas hold for the upper-complement deletion
histograms.

#### Proof

The histogram \(D_j-S_j\) consists exactly of the \(d_j\)-contributions
from continuing owners \(X_{j+1}\), so it and \(D_{j+1}\) both have mass
\(N_{j+1}\). Every edge \(v\to w\) of \(F^{\rm surv}_{j+1}\) obeys the durable
coordinate shift

\[
d_{j+1}(v)=d_j(w).
\tag{6.11}
\]

Cancel the equal contribution of every survivor edge. What remains from
\(D_{j+1}\) is exactly the terminal histogram, and what remains from
\(D_j-S_j\) is exactly the source histogram. This proves (6.8a).
Each survivor component, including an isolated vertex, has one terminal
and one source, so both boundary histograms have mass
\(N_{j+1}-e_j=\kappa_{j+1}\). The triangle inequality gives

\[
2\kappa_{j+1}
=2(\rho^0_{j+1}+b_j).
\]

This proves (6.8b). An initial edge which first fails once can belong to
\(b_j\) only from that failure level until one endpoint stops. It is
therefore counted in at most \(H\) of the \(b_j\)'s. Hence

\[
\sum_jb_j\le HK_H.
\]

Summing (6.8b) proves (6.9), and rearrangement proves (6.10). The
upper-complement proof uses the reversed tail/head shift and is identical.
\(\square\)

For the global suffixes of the \(p=W/(m+1)\) odd-cut paths,

\[
\rho^0_{j+1}\le p,
\qquad
\sum_{j<H}\rho^0_{j+1}\le Hp=O_A(W/\sqrt m)=o_A(W).
\tag{6.12}
\]

Therefore the desired estimate would force the new exact necessary
condition

\[
\boxed{
K_H=o(W/H)
\Longrightarrow
\sum_{j=1}^{H-1}\|D_{j+1}-D_j+S_j\|_1=o(W),}
\tag{6.13}
\]

and the same condition upstairs.

The \(+S_j\) term is essential. Without it, \(D_j\) and \(D_{j+1}\) have
masses \(N_j\) and \(N_{j+1}\), so

\[
\|D_{j+1}-D_j\|_1\ge N_j-N_{j+1}.
\]

Summing inserts \(N_1-N_H=\Theta_A(W)\) of artificial stopping mass. AD7's
full-owner curvature has no such term because all \(W\) owners persist to
every depth. It cannot be transplanted unchanged to active SCD flags.

Finally, (6.9) has only the displayed direction. Small corrected
variation gives no upper bound on \(K_H\). Two failed labelled edges can
swap coordinates \(x,y\), contributing \(e_x-e_y\) and \(e_y-e_x\), and
therefore disappear completely from the aggregate histogram. The AD7
curvature statistic forgets precisely the labelled edge agreement counted
by the durable formula. A reverse stability theorem, not currently
proved, would be needed to deduce small \(K_H\) from small curvature.

### 6.4 Positive averaging criterion

Suppose both active flag families are nonempty. Let \(\mu^-\) and
\(\mu^+\) be arbitrary probability measures on them. For
\(e\in E^\circ\), let \(p_e^-\) be the probability that \(e\) fails some
lower identity before stopping, and define \(p_e^+\) analogously.

Choose the two flags independently. The exact union formula and the union
bound give

\[
\mathbb E K_H
\le\sum_{e\in E^\circ}(p_e^-+p_e^+).
\]

Hence some integral pair satisfies

\[
\boxed{
K_H^{\min}
\le\sum_{e\in E^\circ}(p_e^-+p_e^+).}
\tag{6.14}
\]

Thus it is enough to construct separate random **integral active
bijective** flag systems whose total eventual lower and upper failure
masses are each \(o(W/H)\). They need not be coupled during their
construction. AD7's owner-marginal routing does not define probability
measures on these flag families, so (6.14) is a genuine remaining target
rather than a completed argument.

---

## 7. Precise proved and conditional boundary

### Proved after cross-audit

1. AD7's one-sided clean variation constant is \(2p(H-1)\), and its
   two-sided constant is \(2(2H-1)p\), provided dummy continuations are
   coherent.
2. The trace-energy constant \(1\), the denominator
   \(\nu(n-|Z|)\), the entropy square-root constant \(1/2\), and the
   relabelling quantifiers are correct.
3. Under clean full-owner shifts and deepest-core legality, the direct
   literal central-band word has exact augmented-prefix length \(W+2Hp\).
4. Active-flag nonemptiness is governed exactly by the nested stopped-set
   Hall inequalities (5.1)--(5.3), not by owner-level support.
5. An exact odd-cut forest can be given a globally contiguous component
   order for which \(\mathfrak F^-_\tau\) is empty. This closes an
   order-free implication from odd-cut path geometry, not from the full
   two-sided-rainbow AD7 premise.
6. The portal bounds (6.3)--(6.5), depth-zero boundary criterion, stopped
   restitution and curvature (6.8a)--(6.13), and averaging criterion
   (6.14) are exact
   consequences of the durable-edge formula.

### Conditional

If one clean all-owner AD threading also has the prescribed active sets as
nested common transversals on both signs, then every structural edge is
durable and \(K_H^{\min}=0\). This would be stronger than the required
\(o(W/H)\) estimate.

Alternatively, it suffices to construct probability measures on the two
nonempty integral active flag families satisfying the right side of
(6.14) with \(o(W/H)\) total mass.

### Still unproved

For the separately frozen intended component order, neither

\[
\mathfrak F^-_\tau\ne\varnothing,
\qquad
\mathfrak F^+_\tau\ne\varnothing
\]

nor

\[
K_H^{\min}=o(W/H)
\]

has been proved. The stopped-curvature theorem is a lower-bound
obstruction, not an upper-bound mechanism. Trace entropy is vacuous after
exact rankwise bijectivity and cannot recover labelled edge agreement.

No coefficient-one theorem, MWB, labelled common-owner synchronization,
or full literal universal word is claimed.

---

## 8. Independent audit record

The decisive steps were reconstructed independently in three ways.

1. The variation/entropy audit rederived every boundary sign, the
   \(2p\) and \(2(2H-1)p\) constants, the capped-product constant \(1\),
   Shearer's direction, natural-log Pinsker's \(1/2\), and the
   central-binomial comparison.
2. The zero-hole audit reconstructed the one-core block update, identified
   the augmented-prefix convention behind \(W+2Hp\), and independently
   isolated the all-owner-surjection versus active-bijection mismatch.
3. The durable audit independently derived the stopped-set Hall criterion,
   the component-order star counterexample, the portal dual, and the
   stopped-thread restitution formula. The cancellation proof of
   (6.8a)--(6.8b) was checked with both tail/head orientations and stopped
   owners included.

The first invalid implication in any attempted AD7-to-S7 proof is now
exact: replacing an all-\(W\)-owner support-surjection by its restriction
to the \(N_q\) prescribed active owners and treating that restriction as a
bijection. Equation (4.2) measures this failure exactly.
