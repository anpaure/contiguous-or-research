# Selector-fibre affine orthogonal arrays: exact nested marginals and the visible-trace floor obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Consider one rank-twisted product status cell \(Q_S\).  Freeze a selector
set \(B\) of \(t\) flexible axes, put \(P=[S]\setminus B\),
\(V=|P|=S-t\), and, in selector fibre \(z\in Q_B\), tile by parallel
\(Q_r\)'s on an active set \(A_z\subseteq P\).  One affine conjugate of a
fixed \(H\)-return-free \(Q_r\) compiler is used throughout that fibre.

There is an exact positive statement at the fractional level.  Let

\[
 \Lambda_{V,r}=\operatorname {Inj}([r],P)\times Q_r,
 \qquad |\Lambda_{V,r}|=(V)_r2^r.                 \tag{0.1}
\]

The first coordinate chooses and orders the active \(r\)-set, and the
second performs the endpoint-reversal part of the affine conjugation.
Uniform averaging over (0.1) gives, for every fixed owner and
simultaneously for every \(q\le H\),

\[
 \Pr\bigl((J_1,\ldots,J_q)=(j_1,\ldots,j_q)\bigr)
       ={1\over(V)_q}                               \tag{0.2}
\]

for every ordered \(q\)-tuple of distinct payload axes.  Hence every
payload \(q\)-set is the lower deletion support, and also the upper
insertion support, with probability \(1/\binom Vq\).  The same random
ordered \(H\)-tuple supplies all prefixes, so this is a genuinely common
all-depth, two-sign marginal law.

There is also an explicit selector-word near-orthogonal array.  If

\[
 2^t\ge 2^u|\Lambda_{V,r}|,                         \tag{0.3}
\]

list \(2^u\) or more complete copies of \(\Lambda_{V,r}\) on the selector
words and fill the final incomplete copy arbitrarily.  After the selector
trace is forgotten, the total-variation error of every prefix marginal is
at most \(2^{-u}\), and the summed two-sign error through \(H\) is at most

\[
                         4H2^{-u}2^S.               \tag{0.4}
\]

Thus \(u=2\lceil\log _2H\rceil+O(1)\) makes the projected all-depth error
\(o(2^S)\).  The extra selector budget is only \(O(\log H)\).

However, (0.2)--(0.4) do **not** give the required literal target
averaging.  Every selector axis is inactive, so every lower and upper
target retains the complete selector word \(z\).  The target kernels of
two distinct selector fibres have disjoint supports.  Consequently all
cross-fibre derivative Grams vanish exactly, and arbitrary dependence or
an orthogonal-array constraint among the fibre labels creates no negative
literal covariance.

More quantitatively, for one fixed \(z\) the uniform affine mean is
constant on its compatible signed target cylinder, with load

\[
                         \lambda_{V,q}={2^q\over\binom Vq}.     \tag{0.5}
\]

Assuming the certified compiler's usual trace injectivity, every integral
fibre state has binary target load.  Therefore its exact scatter about the
affine mean is

\[
 2^V(1-\lambda_{V,q}).                              \tag{0.6}
\]

For all \(2^t\) fibres this is

\[
 2^S(1-\lambda_{V,q}),                              \tag{0.7}
\]

independently of every coupling among their uniformly distributed labels.
Equation (0.7) is exactly the Bernoulli floor baseline, not a gain below
it.  The selector-fibre orthogonal array is floor-flat before different
status cells are overlaid.

There is a second, independent obstruction if the intended abstract law is
uniform on all \(S\) flexible axes.  The payload-only law has exact total
variation distance

\[
 1-{\binom{S-t}q\over\binom Sq}                    \tag{0.8}
\]

from that law.  Enumerating all active-set/affine labels requires

\[
 t\ge\log _2\bigl((S-t)_r2^r\bigr)
   =(1+o(1))r\log _2S.                              \tag{0.9}
\]

When \(S=\Theta(m)\), \(H=\Theta(\sqrt m)\), and \(H=o(r)\), (0.9) gives

\[
 {Ht\over S}\longrightarrow\infty,
 \qquad
 {\binom{S-t}H\over\binom SH}\longrightarrow0.    \tag{0.10}
\]

Thus at the top protected depth the two support laws are asymptotically
singular, despite \(t=o(S)\).

The exact boundary is therefore as follows.  Selector fibres solve owner
legality and give perfect fractional payload marginals.  They do not by
themselves implement the balanced literal nested-flag flow or the negative
floor covariance.  A positive continuation must make the selector trace
invisible to the target, or couple genuinely transverse status-cell
decompositions whose literal target cylinders overlap.  Merely balancing
the catalogue of labels on the visible words \(z\) cannot work.

## 1. Physical status-cell model

Write the \(S\) flexible matching edges of the status cell as

\[
                         e_i=\{p_i^0,p_i^1\},\qquad i\in[S].    \tag{1.1}
\]

There is a fixed exterior set \(R\), and the owners in the cell are

\[
 X(x)=R\cup\{p_i^{x_i}:i\in[S]\},\qquad x\in Q_S.  \tag{1.2}
\]

Every owner has the same rank.  A move in direction \(i\) exchanges the
two endpoints of \(e_i\).

Let \(F\) be a directed factor on \(Q_r\).  For \(u\in Q_r\), write

\[
 d_1(u),d_2(u),\ldots,d_H(u)                       \tag{1.3}
\]

for its next \(H\) directions.  We assume the audited return-free
property

\[
 d_1(u),\ldots,d_H(u)\text{ are distinct for every }u.          \tag{1.4}
\]

This is the only chronological property needed for the marginal count.
When the exact binary-load statement is used, we additionally assume the
compiler's audited trace injectivity inside each physical \(Q_r\) packet.

Fix \(B\subseteq[S]\), \(|B|=t\), and \(P=[S]\setminus B\), \(|P|=V\).
A label

\[
                         \lambda=(\phi,\varepsilon)
             \in\operatorname {Inj}([r],P)\times Q_r            \tag{1.5}
\]

identifies the abstract axes with the ordered physical active set
\(\phi([r])\), and conjugates by the cube translation \(\varepsilon\).
For a fixed physical owner \(x\), its abstract start is

\[
                         u_i=x_{\phi(i)}\oplus\varepsilon_i.    \tag{1.6}
\]

The ordered physical prefix is therefore

\[
 J_a(x,\lambda)=\phi(d_a(u)),\qquad1\le a\le H.     \tag{1.7}
\]

The associated signed targets at depth \(q\) are

\[
\begin{aligned}
 T_q^-(x,\lambda)
   &=X(x)\setminus
        \{p_{J_a(x,\lambda)}^{x_{J_a(x,\lambda)}}:1\le a\le q\},\\
 T_q^+(x,\lambda)
   &=X(x)\cup
        \{p_{J_a(x,\lambda)}^{1-x_{J_a(x,\lambda)}}:1\le a\le q\}.
\end{aligned}                                                   \tag{1.8}
\]

Distinctness in (1.4) makes these honest rank-\(m-q\) and rank-\(m+q\)
targets.  Formula (1.8) also shows that lower and upper use the same nested
axis flag.

## 2. Exact affine-catalogue marginal

### Theorem 2.1 (uniform ordered nested flag)

Fix \(x\in Q_S\).  If \(\lambda\) is uniform on \(\Lambda_{V,r}\), then
for every \(q\le H\) and every ordered tuple of distinct payload axes
\(\mathbf j=(j_1,\ldots,j_q)\),

\[
 \Pr\bigl(J_a(x,\lambda)=j_a\ (1\le a\le q)\bigr)
                         ={1\over(V)_q}.             \tag{2.1}
\]

The assertion holds jointly: the ordered \(H\)-tuple is uniform, and the
laws at smaller depths are its prefixes.

#### Proof

Fix an abstract start \(u\in Q_r\).  By (1.4), the abstract directions
\(d_1(u),\ldots,d_q(u)\) are distinct.  The number of injections \(\phi\)
such that

\[
                         \phi(d_a(u))=j_a\quad(1\le a\le q)     \tag{2.2}
\]

is exactly \((V-q)_{r-q}\).  Once \(x,\phi,u\) are fixed, (1.6) determines
\(\varepsilon\) uniquely.  Summing over the \(2^r\) possible values of
\(u\), the number of labels producing \(\mathbf j\) is

\[
                         2^r(V-q)_{r-q}.             \tag{2.3}
\]

Division by \(2^r(V)_r\) gives \(1/(V)_q\).  Taking \(q=H\) proves the
joint statement, and all smaller statements follow by taking prefixes.
\(\square\)

### Corollary 2.2 (exact signed target marginal for one owner)

For a fixed owner \(X(x)\), a compatible lower target is specified by a
\(q\)-set \(D\subseteq P\): make the pairs in \(D\) empty and retain the
owner orientation on every other pair.  A compatible upper target is
specified analogously by making the pairs in \(D\) full.  Under the
uniform affine catalogue, every such signed target has probability

\[
                         {1\over\binom Vq}.           \tag{2.4}
\]

#### Proof

Every unordered \(D\) has \(q!\) orderings.  Sum (2.1) over them and use
\((V)_q=q!\binom Vq\).  Formula (1.8) identifies the resulting lower and
upper targets. \(\square\)

This is exactly the uniform nested deletion/insertion law on the payload
axes.  It is not a collection of independently chosen depthwise laws.

## 3. Exact target-cylinder mean and the floor baseline

Fix a selector word \(z\in Q_B\).  Let
\(\mathcal T_{z,q}^-\) be the lower targets which

* have the single endpoint prescribed by \(z_i\) on every \(i\in B\);
* have exactly \(q\) empty pairs in \(P\); and
* have one endpoint on every other payload pair.

Define \(\mathcal T_{z,q}^+\) in the same way with \(q\) full payload
pairs.  In either sign,

\[
                         |\mathcal T_{z,q}^{\pm}|
                       =2^{V-q}\binom Vq.            \tag{3.1}
\]

For a label \(\lambda\), let \(K_{z,\lambda}^{q,\pm}(T)\) be the number
of owner starts in the whole selector fibre \(x|_B=z\) whose depth-\(q\)
target is \(T\).

### Lemma 3.1 (constant affine mean)

For every \(T\in\mathcal T_{z,q}^{\pm}\),

\[
 \overline K_z^{q,\pm}(T)
 :={1\over|\Lambda_{V,r}|}\sum_{\lambda}K_{z,\lambda}^{q,\pm}(T)
 ={2^q\over\binom Vq}=\lambda_{V,q}.                \tag{3.2}
\]

The mean is zero outside \(\mathcal T_{z,q}^{\pm}\).

#### Proof

Fix a lower target \(T\) and let \(D\subseteq P\) be its empty-pair set.
Its orientations off \(D\) determine the owner there.  On each pair of
\(D\), either owner endpoint is possible, giving exactly \(2^q\)
compatible owners.  By Corollary 2.2, each compatible owner uses \(D\)
with probability \(1/\binom Vq\).  This proves (3.2).  Complementation
proves the upper statement. \(\square\)

The total mass checks exactly:

\[
 |\mathcal T_{z,q}^{\pm}|\lambda_{V,q}
 =2^{V-q}\binom Vq{2^q\over\binom Vq}=2^V,          \tag{3.3}
\]

the number of owners in the selector fibre.

### Lemma 3.2 (binary integral fibre state)

Assume the compiler trace is injective inside each installed \(Q_r\).
Then

\[
                         K_{z,\lambda}^{q,\pm}(T)\in\{0,1\}    \tag{3.4}
\]

for every \(z,\lambda,q,\pm,T\), and

\[
                         \|K_{z,\lambda}^{q,\pm}\|_2^2=2^V.   \tag{3.5}
\]

#### Proof

For fixed \(z\) and active set \(A=\phi([r])\), the parallel packets are
indexed by the frozen word on \(P\setminus A\).  Targets from two different
parallel packets retain different frozen words and hence are distinct.
Inside one packet, (3.4) is the certified trace injectivity.  There is one
target occurrence per owner, so the binary vector has \(2^V\) ones.
\(\square\)

### Theorem 3.3 (exact affine scatter)

For a uniform label in one selector fibre,

\[
 \sum_T\operatorname {Var}K_{z,\lambda}^{q,\pm}(T)
                         =2^V(1-\lambda_{V,q}).      \tag{3.6}
\]

#### Proof

By Lemma 3.2, the expected squared norm is \(2^V\).  By (3.1)--(3.2),

\[
 \|\overline K_z^{q,\pm}\|_2^2
 =2^{V-q}\binom Vq
       \left({2^q\over\binom Vq}\right)^2
 =2^V\lambda_{V,q}.                                \tag{3.7}
\]

Subtract (3.7) from \(2^V\). \(\square\)

In the regime \(q\le H=o(V)\), \(\lambda_{V,q}=o(1)\).  The scatter is
therefore asymptotic to the entire owner mass of the fibre.

## 4. An explicit repeated-catalogue selector design

Let \(R_B=2^t\), \(L=|\Lambda_{V,r}|\), and write

\[
                         R_B=aL+b,\qquad0\le b<L.    \tag{4.1}
\]

Order \(Q_B\) and \(\Lambda_{V,r}\) lexicographically.  Assign the first
\(aL\) selector words to \(a\) complete copies of the affine catalogue,
and assign arbitrary labels to the final \(b\) words.  This is a fully
deterministic list.

### Proposition 4.1 (projected all-depth discrepancy)

Fix the payload orientation \(x|_P\), and forget the single-endpoint trace
on \(B\) after forming the target.  For every signed depth \(q\le H\), the
empirical distribution over \(z\in Q_B\) differs in total variation from
the uniform payload \(q\)-flag law by less than \(1/a\).  Summed over all
payload words, both signs, and all protected depths, the \(\ell^1\) target
mass discrepancy is at most

\[
                         {4H\over a}2^S.             \tag{4.2}
\]

In particular, (0.3) gives \(a\ge2^u\) and hence (0.4).

#### Proof

Every complete copy of \(\Lambda_{V,r}\) has the exact joint law of
Theorem 2.1.  The empirical label law in (4.1) is

\[
                         {aL\over R_B}U
                      +{b\over R_B}\nu,             \tag{4.3}
\]

where \(U\) is uniform on the complete catalogue and \(\nu\) is some
probability law.  Since \(b<L\),

\[
                         {b\over R_B}< {1\over a}.   \tag{4.4}
\]

Pushing forward (4.3) to any prefix or signed target cannot increase
total variation.  With the convention that \(\ell^1\) distance is twice
total variation, a fixed signed depth contributes at most
\(2a^{-1}2^S\).  Sum over two signs and \(H\) depths. \(\square\)

Proposition 4.1 is the strongest conclusion obtainable merely by listing
the labels evenly on visible selector words.  The projection in its
statement is essential.

## 5. Visible selector trace and vanishing cross-Gram

For every target \(T\in\mathcal T_{z,q}^{\pm}\), the restriction of \(T\)
to each selector pair is a singleton and records \(z\).  Therefore

\[
 \mathcal T_{z,q}^{\pm}\cap\mathcal T_{z',q}^{\pm}=\varnothing
                         \qquad(z\ne z').            \tag{5.1}
\]

### Theorem 5.1 (block-diagonal literal kernel)

For \(z\ne z'\) and arbitrary affine labels
\(\lambda,\lambda',\mu,\mu'\),

\[
 \left\langle
 K_{z,\lambda}^{q,\pm}-K_{z,\lambda'}^{q,\pm},
 K_{z',\mu}^{q,\pm}-K_{z',\mu'}^{q,\pm}
 \right\rangle=0.                                  \tag{5.2}
\]

More generally, let \(\Lambda_z\) be random affine labels with uniform
marginals, under an arbitrary joint law, and put

\[
                         Z^{q,\pm}=\sum_{z\in Q_B}
                                  K_{z,\Lambda_z}^{q,\pm}.      \tag{5.3}
\]

Then

\[
 \sum_T\operatorname {Var}Z^{q,\pm}(T)
 =2^S(1-\lambda_{V,q}).                            \tag{5.4}
\]

The right side is independent of all dependence among the labels.

#### Proof

Equation (5.1) proves (5.2).  Expanding the variance in (5.3), every
off-diagonal \(z,z'\) term is an expected inner product of vectors on
disjoint supports and is zero.  The diagonal term is (3.6).  There are
\(2^t\) fibres, so their sum is

\[
                         2^t2^V(1-\lambda_{V,q})
                       =2^S(1-\lambda_{V,q}).
\]
\(\square\)

The exact floor interpretation is worth recording.  The full signed target
cylinder of the cell has size

\[
                         N_{S,t,q}=2^t2^{V-q}\binom Vq,          \tag{5.5}
\]

and mean load \(\lambda_{V,q}\).  Hence its Bernoulli floor variance is

\[
 N_{S,t,q}\lambda_{V,q}(1-\lambda_{V,q})
                         =2^S(1-\lambda_{V,q}),      \tag{5.6}
\]

exactly (5.4).  Thus even a fixed-slice, Latin, or orthogonal-array
coupling of the labels cannot move this isolated cell below its balanced
floor baseline.  It has no cross-fibre target overlap on which negative
covariance could act.

This does not say that a deterministic label cannot interact favourably
with target load already supplied by other status cells.  It says exactly
that such a gain is a **cross-cell** joined-kernel statement.  It cannot be
deduced from selector-label balance inside the cell.

There is an equivalent Hall formulation.  The literal incidence graph of
the cell is the disjoint union

\[
                         \mathcal G=\mathop{\dot\bigcup}_{z\in Q_B}
                                      \mathcal G_z.               \tag{5.7}
\]

Balancing how often the different labels occur among the components does
not verify a Hall cut inside any one component.  An abstract fractional
flow which mixes labels separately in every \(\mathcal G_z\) cannot be
rounded by assigning its different mixture terms to other selector words,
because those words belong to different connected target components.
This is the exact integral grouping obstruction.

## 6. The frozen-selector support cut

Let \(U_{S,q}\) be the uniform law on all \(q\)-subsets of the \(S\)
flexible axes, and let \(U_{P,q}\) be the uniform law on the \(q\)-subsets
of \(P\), viewed as a law on \(\binom{[S]}q\).  The latter is the support
law of Theorem 2.1 after order is forgotten.

### Proposition 6.1 (exact support distance)

\[
 \boxed{
 \|U_{P,q}-U_{S,q}\|_{\rm TV}
       =1-{\binom{S-t}q\over\binom Sq}.}             \tag{6.1}
\]

#### Proof

Let \(E=\{D:D\subseteq P\}\).  The law \(U_{P,q}\) is precisely
\(U_{S,q}\) conditioned on \(E\), while

\[
                         U_{S,q}(E)={\binom{S-t}q\over\binom Sq}.
\]

The total variation distance between a law and its conditioning on an
event of probability \(p\) is \(1-p\). \(\square\)

The small relative selector dimension \(t/S=o(1)\) is not sufficient at
mesoscopic depth.  Indeed

\[
 {\binom{S-t}q\over\binom Sq}
 =\prod_{j=0}^{q-1}\left(1-{t\over S-j}\right)
 \le \exp\left(-{qt\over S}\right).                \tag{6.2}
\]

Thus \(qt/S\to\infty\) makes (6.1) tend to one.

### Proposition 6.2 (label entropy forces singularity at Gaussian depth)

Assume

\[
 S=\Theta(m),\qquad H=\Theta(\sqrt m),\qquad H=o(r),
 \qquad r=o(S),\qquad t=o(S),                       \tag{6.3}
\]

and require enough selector words to contain every active-set/affine
label:

\[
                         2^t\ge (S-t)_r2^r.          \tag{6.4}
\]

Then

\[
                         {Ht\over S}\to\infty       \tag{6.5}
\]

and the distance (6.1) at \(q=H\) tends to one.

#### Proof

Put \(V=S-t\).  From (6.4),

\[
 t\ge r+\log _2(V)_r
   \ge r+r\log _2(V-r+1).                           \tag{6.6}
\]

Under (6.3), \(V-r=(1-o(1))S\), so

\[
                         t\ge(1-o(1))r\log _2S.      \tag{6.7}
\]

Consequently

\[
 {Ht\over S}
 \ge(1-o(1)){H^2\over S}{r\over H}\log _2S.        \tag{6.8}
\]

The first factor \(H^2/S\) is bounded below by a positive constant, the
second tends to infinity, and \(\log S\to\infty\).  This proves (6.5).
Now apply (6.2). \(\square\)

The same proof applies whenever

\[
                         {H^2\over S}{r\over H}\log S\to\infty, \tag{6.9}
\]

so (6.3) is only the coefficient-one specialization.

Proposition 6.2 does not resurrect the fixed-quartet Hall cut.  Every
active payload axis may still be a physical cross-quartet axis, and every
return-free \(q\)-window then contains \(q\) such axes.  The obstruction is
instead that the proposed selector encoding removes too many otherwise
flexible axes from the nested flag law.

There is an exact entropy form of the obstruction to simply making those
selector axes active.  Consider any generalized coordinate-subcube tiling
whose option label depends only on the selector word.  Write
\(L:Q_B\to\mathcal L\) for that label and let
\(C_\ell\subseteq B\) be the selector directions which are active under
label \(\ell\).

### Proposition 6.3 (selector entropy versus active grouping)

Exact owner tiling forces

\[
 L(z)=\ell\quad\Longrightarrow\quad
 L(z+v)=\ell\quad(v\in Q_{C_\ell}).                 \tag{6.10}
\]

Consequently, for uniform \(Z\in Q_B\),

\[
 \boxed{
 H_2(L(Z))+\mathbb E|C_{L(Z)}|\le t.}              \tag{6.11}
\]

In particular, if \(M\) option labels occur equally often, then

\[
 \mathbb E|C_{L(Z)}|\le t-\log _2M.                \tag{6.12}
\]

#### Proof

If a packet uses a selector direction \(b\), it contains both endpoints
of every edge in that direction.  Its option label and active coordinate
set therefore cannot change when the selector bit \(b\) is flipped.
Closure under all active selector directions gives (6.10).

For every nonempty label fibre
\(F_\ell=L^{-1}(\ell)\), equation (6.10) makes \(F_\ell\) a union of
cosets of \(Q_{C_\ell}\).  Hence
\(|F_\ell|\ge2^{|C_\ell|}\).  Conditional on \(L=\ell\), the uniform
word \(Z\) is uniform on \(F_\ell\), and so

\[
 H_2(Z\mid L=\ell)=\log _2|F_\ell|
                    \ge |C_\ell|.
\]

Average in \(\ell\) and use
\(H_2(L)=H_2(Z)-H_2(Z\mid L)=t-H_2(Z\mid L)\) to obtain (6.11).
For an equiprobable \(M\)-label catalogue, \(H_2(L)=\log _2M\), giving
(6.12). \(\square\)

Thus the nearly minimal selector budget used to encode
\(M=(S-t)_r2^r\) affine labels leaves only
\(t-\log _2M\) selector directions active on average.  Reproducing the
incidence of a uniform \(r\)-subset of all \(S\) axes would instead require
mean selector incidence \(rt/S\).  Any hidden-selector variant of this
form therefore needs the necessary entropy slack

\[
                         t-\log _2M\ge {rt\over S}.              \tag{6.13}
\]

This does not rule out a grouped construction with extra slack.  It states
the exact price of consuming selector bits: the same bits cannot
simultaneously carry independent option entropy and serve as active packet
directions.

## 7. Exact proved boundary and next statement

Proved:

1. The full active-set/affine catalogue has the exact uniform ordered
   nested-prefix law (2.1), simultaneously at all \(q\le H\) and for both
   signs.
2. Its fixed-selector target mean is exactly (3.2).
3. Complete-catalog repetitions on the selector cube give an explicit
   projected near-orthogonal array with all-depth error (4.2).
4. Literal targets retain \(z\), so the fibre kernels are orthogonal and
   every uniformly marginalized selector coupling has the exact floor
   scatter (5.4), equal to the baseline (5.6).
5. If one asks for the all-\(S\)-axis balanced flag law, the full label
   entropy forces asymptotic singularity at Gaussian depth.
6. Any attempt to activate selector directions while keeping a
   selector-word label obeys the exact entropy tradeoff (6.11); option
   entropy and active selector dimension consume the same \(t\)-bit
   budget.

Not proved, and not implied by the selector construction:

1. a negative joined-target covariance between different rank-twisted
   status cells;
2. an integral assignment satisfying the Hall cuts inside every visible
   selector component;
3. a transverse decomposition in which the same literal target lies in
   several independently steerable selector cylinders; or
4. the coefficient-one theorem.

The next exact constructive lemma must therefore have one of the following
forms.

* **Hidden-selector retileability:** packet trades may cross selector
  fibres while preserving ownership, so that the target forgets enough of
  the label-carrying word and the corresponding target kernels overlap.
* **Transverse-cell covariance:** two or more owner resolutions with
  different selector sets admit one integral common-block recombination,
  and their joined literal derivative Gram has the required negative
  off-diagonal mass.

An orthogonal array on the visible \(z\)'s, without either property, has
zero off-diagonal Gram and is therefore exhausted as a route to the floor
covariance gate.
