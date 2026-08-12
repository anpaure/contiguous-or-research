# Affine phase arrays for tensor-cell shadow traces

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Let \(d=2r\) be a power of two. A fixed tensor-associator shore has
\(4^r=2^d\) owner-disjoint main cells \(Q_d\) sharing one physical
direction frame. In each cell install an affine conjugate of a cube cycle
factor.

For an arbitrary factor \(F\), an affine conjugate

\[
 g_{\sigma,a}(x)=\sigma x+a,\qquad
 F^{\sigma,a}=g_{\sigma,a}Fg_{\sigma,a}^{-1},
\]

has the following exact depth-\(q\) trace at owner
\(y=g_{\sigma,a}x\):

\[
 \boxed{
 \tau_q^{F^{\sigma,a}}(y)
 =
 \left(
 \sigma D_q^F(x),
 (\sigma x+a)|_{[d]\setminus\sigma D_q^F(x)}
 \right).
 }
\]

Thus translations act only on the outside orientation, while coordinate
permutations act on both the direction set and its orientation labels.

Three conclusions follow.

1. Using every affine conjugate gives exact uniform trace load at every
   depth, for every factor:
   \[
    2^{d+q}q!(d-q)!
   \]
   occurrences of each trace
   \((D,\eta)\in\binom{[d]}q\times Q_{[d]\setminus D}\).
2. Exact uniformity on only the \(2^d\) available main cells is impossible
   in general. Its required load is
   \[
    \lambda_q=\frac{2^{d+q}}{\binom dq}.
   \]
   At \(q=2\) and \(d=2^t\ge4\), the odd factor \(d-1\) in
   \(\binom d2\) proves \(\lambda_2\notin\mathbb Z\).
3. If \(F\) is the recursive half-depth rainbow factor, exact uniformity
   can be replaced by exponentially accurate simultaneous balance. Index
   the \(2^d\) main cells by all translations \(a\in Q_d\). There are
   permutations \(\sigma_a\in S_d\) such that, simultaneously for both
   shadow orientations, every \(q\le d/2\), and every trace \(t\),
   \[
    L_q^\pm(t)
    =(1\pm\varepsilon_d)\lambda_q,
    \qquad
    \varepsilon_d=\left(\frac34\right)^{d/8}.
   \]
   Each affine translation occurs exactly once, every cell remains an exact
   owner partition into isometric \(C_{2d}\)'s, and
   \[
    \sum_{1\le q\le d/2}\sum_{\pm,t}
    |L_q^\pm(t)-\lambda_q|
    =o(2^{2d}).
   \]

This constructs the requested owner-preserving permutation array and
balances direction sets and basepoint phases jointly.

There is also a sharp negative statement for the native one-order Hamming
factor. At depth \(q\) it uses at most \(d\) direction sets, so its shadow
image has size at most \(d2^{d-q}\). Its within-cell collision excess is at
least

\[
 2^d\left(1-\frac d{2^q}\right).
\]

Affine arrays can redistribute these repeated traces but cannot remove
them. Hence the native Hamming factor is unusable beyond logarithmic depth;
the recursive rainbow factor is essential.

The remaining constant-one issue is not affine phase balance inside the
main cells. Their full physical traces also retain distinct reservoir tags,
so their shadow images are already cross-cell disjoint. The unresolved
collisions occur when main and reservoir cell patterns, different
associator shores, and overlapping external tensor packets are combined.

## 1. Labelled traces in one cube

Let \(F:Q_d\to Q_d\) be a neighbor permutation. Write
\(\rho_F(x)\in[d]\) for the coordinate toggled by the edge
\(xF(x)\). For a forward geodesic \(q\)-window, put

\[
 D_q^F(x)=
 \{\rho_F(x),\rho_F(Fx),\ldots,\rho_F(F^{q-1}x)\}.
\tag{1.1}
\]

The lower face produced by the window is encoded by

\[
 \tau_q^{F,+}(x)
 =
 \left(D_q^F(x),x|_{[d]\setminus D_q^F(x)}\right).
\tag{1.2}
\]

The first coordinate records the pair directions made empty; the second
records the unchanged orientations of all other split pairs. Define
\(\tau_q^{F,-}\) analogously from \(F^{-1}\); it encodes the upper face,
with the directions in \(D\) made full.

The trace universe at depth \(q\) is

\[
 \mathcal T_{d,q}
 =
 \{(D,\eta):D\in\binom{[d]}q,\ 
 \eta\in Q_{[d]\setminus D}\},
\tag{1.3}
\]

of size

\[
 |\mathcal T_{d,q}|=\binom dq2^{d-q}.
\tag{1.4}
\]

## 2. Exact affine conjugacy formula

For \(\sigma\in S_d\) and \(a\in Q_d\), define the affine cube
automorphism

\[
 g_{\sigma,a}(x)=\sigma x+a
\tag{2.1}
\]

and the conjugate factor

\[
 F^{\sigma,a}
 =g_{\sigma,a}Fg_{\sigma,a}^{-1}.
\tag{2.2}
\]

Here \(\sigma x\) is the coordinate-permuted bit vector.

### Theorem 2.1 (owner-resolved affine trace formula)

If \(y=g_{\sigma,a}x\), then

\[
 D_q^{F^{\sigma,a}}(y)=\sigma D_q^F(x)
\tag{2.3}
\]

and

\[
 \boxed{
 \tau_q^{F^{\sigma,a},+}(y)
 =
 \left(
 \sigma D_q^F(x),
 (\sigma x+a)|_{[d]\setminus\sigma D_q^F(x)}
 \right).
 }
\tag{2.4}
\]

The same formula holds for the reverse trace after replacing \(F\) by
\(F^{-1}\).

#### Proof

Conjugacy gives

\[
 (F^{\sigma,a})^j(y)=g_{\sigma,a}(F^jx).
\]

Translation changes no edge direction, while coordinate permutation sends
direction \(i\) to \(\sigma i\). This proves (2.3). Restricting
\(y=\sigma x+a\) to the complement of that direction set gives (2.4).
\(\square\)

For a physical tensor cell, the affine map acts on its binary phase
coordinates. It need not extend to one global permutation of the ambient
ground coordinates. It is nevertheless an automorphism of the embedded
product cube, maps owners to owners of the same cell, and maps every
one-bit edge to a physical pair-flip edge.

## 3. Translation balance and direction imbalance

For a fixed factor \(F\), define the direction multiplicity

\[
 n_q^F(D)=|\{x\in Q_d:D_q^F(x)=D\}|.
\tag{3.1}
\]

### Proposition 3.1 (all translations balance phases exactly)

Fix \(\sigma\in S_d\), and use every translation \(a\in Q_d\) once. For
every trace \((D',\eta)\),

\[
 \sum_{a\in Q_d}
 \#\{y:\tau_q^{F^{\sigma,a},+}(y)=(D',\eta)\}
 =2^q n_q^F(\sigma^{-1}D').
\tag{3.2}
\]

#### Proof

Fix a base start \(x\) with
\(D_q^F(x)=\sigma^{-1}D'\). Equation (2.4) has prescribed outside
orientation \(\eta\) precisely when the \(d-q\) outside coordinates of
\(a\) take prescribed values. Its \(q\) coordinates in \(D'\) are free,
giving \(2^q\) translations. Sum over the
\(n_q^F(\sigma^{-1}D')\) starts. \(\square\)

Thus translations solve the basepoint phase problem exactly but preserve
the direction histogram. Coordinate permutations are genuinely necessary
for joint trace balance.

## 4. The full affine orbit is exactly uniform

Let

\[
 {\rm Aff}(d)=Q_d\rtimes S_d.
\]

### Theorem 4.1 (exact affine trace resolution)

Use every \(g_{\sigma,a}\in{\rm Aff}(d)\) once. For every factor \(F\),
every depth \(q\), and every trace
\(t\in\mathcal T_{d,q}\), the aggregate forward load is

\[
 \boxed{
 2^{d+q}q!(d-q)!.
 }
\tag{4.1}
\]

The reverse load has the same value, simultaneously for every \(q\).

#### Proof

Fix \(t=(D',\eta)\). By Proposition 3.1, a base direction set \(D\)
contributes \(2^qn_q^F(D)\) for each permutation satisfying
\(\sigma D=D'\). There are exactly \(q!(d-q)!\) such permutations.
Therefore the total load is

\[
 2^qq!(d-q)!\sum_Dn_q^F(D)
 =
 2^{d+q}q!(d-q)!,
\]

because every one of the \(2^d\) owners has one depth-\(q\) direction set.
The reverse proof is identical. \(\square\)

This is a simultaneous affine orthogonal array on face traces. It is exact
but has \(2^dd!\) rows of factor conjugates, far more than the \(2^d\)
main tensor cells.

## 5. Exact finite-array divisibility obstruction

Suppose \(M\) owner-disjoint \(Q_d\) cells each carry one exact factor, and
their aggregate load is exactly constant on \(\mathcal T_{d,q}\). Since
each cell has \(2^d\) starts, the constant must be

\[
 \lambda_{q,M}
 =
 \frac{M2^d}{\binom dq2^{d-q}}
 =
 \frac{M2^q}{\binom dq}.
\tag{5.1}
\]

### Proposition 5.1 (necessary divisibility)

Exact trace balance at depth \(q\) requires

\[
 \boxed{\binom dq\mid M2^q.}
\tag{5.2}
\]

In the tensor main-cell array, \(M=4^r=2^d\). If
\(d=2^t\ge4\), exact balance already fails at \(q=2\), because

\[
 \binom d2=2^{t-1}(d-1)
\]

contains the odd factor \(d-1>1\), whereas \(M2^2\) is a power of two.
\(\square\)

This obstruction is independent of the chosen factor and independent of
owner-preserving conjugacy. Floor/ceiling or asymptotic balance is the
strongest possible target on the available number of cells.

## 6. The native one-order Hamming obstruction

Consider a translate Hamming factor in which every cycle has one common
direction word \(\pi\pi\). At depth \(q<d\), only the \(d\) cyclic
\(q\)-sets of \(\pi\) can occur. More exactly, if
\(\mathcal I_q(\pi)\) is that family, then

\[
 n_q^F(D)=
 \begin{cases}
  2^d/d,&D\in\mathcal I_q(\pi),\\
  0,&D\notin\mathcal I_q(\pi).
 \end{cases}
\tag{6.1}
\]

Indeed, every \(2d\)-cycle contains each cyclic \(q\)-set twice, and the
factor has \(2^d/(2d)\) cycles. Proposition 3.1 therefore gives the exact
translation-orbit trace load

\[
 \frac{2^{d+q}}d
\]

on the \(d\) permitted direction fibers and zero on every other direction
fiber.

In particular,

\[
 |\tau_q^{F,+}(Q_d)|
 \leq d2^{d-q}.
\tag{6.2}
\]

### Proposition 6.1 (deep Hamming collision excess)

Every affine conjugate of the one-order factor has forward and reverse
collision excess at least

\[
 \boxed{
 2^d-d2^{d-q}
 =
 2^d\left(1-\frac d{2^q}\right).
 }
\tag{6.3}
\]

#### Proof

Equation (6.2) bounds the image of a map with domain \(2^d\). Affine
conjugacy only relabels its domain and trace universe, so it preserves image
size and collision excess. The reverse word has the same direction
catalogue. \(\square\)

For \(q-\log_2d\to\infty\), the collision excess is
\((1-o(1))2^d\) in every cell. Summing owner-disjoint cells only adds these
nonnegative collision excesses. Thus no phase/permutation array can turn a
native one-order Hamming factor into a Gaussian-depth near-resolution.

## 7. A translation-complete near-balanced permutation array

Now let \(F=F_d\) be the recursive half-depth rainbow factor. For every
\(q\leq d/2\), both trace maps are injective on \(Q_d\).

Index the \(M=2^d\) main tensor cells by the translation vectors
\(a\in Q_d\). Independently choose a uniform permutation
\(\sigma_a\in S_d\), and install

\[
 F^{\sigma_a,a}
\tag{7.1}
\]

on cell \(a\). Every translation is used exactly once.

For a trace \(t\in\mathcal T_{d,q}\), let \(Z_{a,t}^\pm\) be the indicator
that \(t\) lies in the corresponding forward or reverse trace image of
cell \(a\). Injectivity makes this a zero-one variable. The variables over
different \(a\)'s are independent.

### Lemma 7.1 (uniform expected load)

For every \(q\leq d/2\), sign, and trace \(t\),

\[
 \mathbb E\sum_{a\in Q_d}Z_{a,t}^\pm
 =
 \lambda_q:=
 \frac{2^{d+q}}{\binom dq}.
\tag{7.2}
\]

#### Proof

Average over the independent uniform \(\sigma_a\)'s and sum over all
translations \(a\). This is \(1/d!\) times the complete affine-orbit load
in Theorem 4.1:

\[
 \frac{2^{d+q}q!(d-q)!}{d!}
 =
 \frac{2^{d+q}}{\binom dq}.
\]

\(\square\)

The mean is exponentially large uniformly over the full half-depth range.
Indeed,

\[
 \frac{\binom dq}{2^q}
 \leq
 \sum_{j=0}^d\binom dj2^{-j}
 =\left(\frac32\right)^d,
\]

so

\[
 \boxed{\lambda_q\geq\left(\frac43\right)^d.}
\tag{7.3}
\]

### Theorem 7.2 (simultaneous affine phase array)

For all sufficiently large powers of two \(d\), there is a deterministic
choice of \((\sigma_a)_{a\in Q_d}\) such that, with

\[
 \varepsilon_d=\left(\frac34\right)^{d/8},
\tag{7.4}
\]

one has simultaneously

\[
 \boxed{
 |L_q^\pm(t)-\lambda_q|
 \leq\varepsilon_d\lambda_q
 }
\tag{7.5}
\]

for every \(q\leq d/2\), both signs, and every
\(t\in\mathcal T_{d,q}\).

#### Proof

For fixed \(q,\pm,t\), the load is a sum of independent, not necessarily
identically distributed, Bernoulli variables with mean \(\lambda_q\).
The multiplicative Chernoff bound gives

\[
 \Pr\bigl(|L_q^\pm(t)-\lambda_q|
          >\varepsilon_d\lambda_q\bigr)
 \leq
 2\exp\left(-\frac{\varepsilon_d^2\lambda_q}{3}\right).
\tag{7.6}
\]

By (7.3)--(7.4),

\[
 \varepsilon_d^2\lambda_q
 \geq
 \left(\frac43\right)^{3d/4}.
\tag{7.7}
\]

The total number of signed traces over all depths is at most

\[
 2\sum_{q=0}^d\binom dq2^{d-q}
 =2\cdot3^d.
\tag{7.8}
\]

The union of the failure probabilities in (7.6) is therefore less than
one for all sufficiently large \(d\). A deterministic choice satisfying
all inequalities exists. \(\square\)

### Corollary 7.3 (aggregate trace discrepancy)

For the array in Theorem 7.2,

\[
\begin{aligned}
 &\sum_{1\leq q\leq d/2}\sum_{\pm}
 \sum_{t\in\mathcal T_{d,q}}
 |L_q^\pm(t)-\lambda_q|\\
 &\qquad\leq
 d\varepsilon_d\,2^{2d}
 =o(2^{2d}).
\end{aligned}
\tag{7.9}
\]

#### Proof

At every depth and sign,

\[
 \lambda_q|\mathcal T_{d,q}|
 =2^{2d},
\]

the total number of starts in all \(2^d\) cells. Sum (7.5) through the
at most \(d\) signed depth rows. \(\square\)

Thus the affine array gives the strongest asymptotic substitute compatible
with the divisibility obstruction in Proposition 5.1.

## 8. Physical tensor interpretation

A main tensor cell is indexed by one of four reservoir orientations in
each associator block. These \(4^r=2^d\) tags can be identified with the
translation vectors \(a\in Q_d\).

All cycles in a main cell flip only the common special-pair directions
\(\mathcal D\). The reservoir tag is unchanged by every forward and reverse
window. Consequently the complete physical trace produced in cell \(a\)
is

\[
 \boxed{
 \left(
 a;\
 \sigma_aD_q^F(x),\
 (\sigma_ax+a)|_{\mathcal D\setminus\sigma_aD_q^F(x)}
 \right),
 }
\tag{8.1}
\]

after the fixed identification of its cube coordinates with
\(\mathcal D\).

The first entry is a genuine physical spectator orientation. Different
main cells therefore have disjoint physical shadow images, while
Theorem 7.2 balances their quotient traces after this spectator tag is
forgotten. In particular:

* within a main cell, recursive rainbowness gives exact injectivity;
* between main cells, the retained reservoir tag gives exact separation;
* after quotienting by the tag, the affine permutation array gives
  exponentially accurate direction/basepoint balance.

So the phase/basepoint problem is completely solved on the all-main tensor
sector.

This sector contains \(16^r\) of the \(24^r\) tensor owners, a fraction
\((2/3)^r\). It is not a full-mass constant-one core when \(r\to\infty\).
The remaining product cells use reservoir directions in at least one
block. Their fixed tags and active frames differ, and shadows from different
activity patterns can coincide physically.

## 9. Exact remaining gate

The present theorem separates the outcomes sharply.

### Closed

1. Exact owner preservation under arbitrary affine conjugacy.
2. Exact classification of every conjugated target face.
3. Exact phase balance under the full translation orbit.
4. Exact all-affine balance at every depth.
5. Exponentially accurate joint direction/phase balance on the available
   \(2^d\) main cells.
6. Exact physical shadow separation throughout the all-main sector.

### Obstructed

1. Exact uniform balance on \(2^d\) cells is arithmetically impossible,
   already at \(q=2\).
2. Native one-order Hamming factors retain almost-total within-cell
   collision excess beyond logarithmic depth; no affine array repairs it.

### Open

> Partition or couple all \(6^r\) tensor cells across their activity
> patterns and associator shores so that the affine arrays remain
> owner-exact and the physical shadow images of different patterns have
> total collision excess \(o(24^r)\) through every fixed Gaussian window.

The all-main phase array cannot be discarded as a negligible technical
detail—it proves the correct affine mechanism—but its owner mass is
exponentially small relative to the full tensor packet. The next theorem
must transport this affine balance across main/reservoir activity patterns,
not refine the already optimal phase array inside one common-frame family.
