# Stage B in one fixed pair frame: exact cycle-face multiplicities and the orbit obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, script, solver, search, or
web input is used.

## 0. Verdict

Fix one perfect matching of the \(2m\) Boolean coordinates. Suppose every
orientation-cube fibre is partitioned into isometric pair-flip cycles, and
use every middle owner once. The depth-\(q\) lower-shadow multiplicity of
an individual target has an exact face-incidence formula, but its
pair-type average is forced independently of the chosen cycle factors.

A rank-\((m-q)\) target with \(f\) full coordinate pairs has

\[
 f+q\text{ empty pairs},\qquad m-2f-q\text{ split pairs}.           \tag{0.1}
\]

The exact target and source counts are

\[
\boxed{
 T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!}\,2^{m-2f-q},}           \tag{0.2}
\]

\[
\boxed{
 V_f
 =\frac{m!}{f!^2(m-2f)!}\,2^{m-2f}.}                  \tag{0.3}
\]

Every target of type \(f\) has exactly

\[
                         \binom{f+q}{q}                \tag{0.4}
\]

candidate source faces. For any fixed resolution by isometric cycles, its
actual multiplicity is the sum of the selected face-occurrence
multiplicities over those candidates; see Theorem 2.1.

After summing over the whole type orbit, one obtains the resolution-free
identity

\[
             \sum_{L:\,f(L)=f}\mu_q^-(L)=V_f.          \tag{0.5}
\]

Consequently the exact orbit-average multiplicity is

\[
\boxed{
 \lambda_{f,q}:={V_f\over T_{f,q}}
  ={2^q\binom{f+q}{q}\over\binom{m-2f}{q}}
  ={2^q(f+1)^{\overline q}\over
                 (m-2f)_{\underline q}}.}             \tag{0.6}
\]

No choice of cycle factors can transfer unused starts between different
values of \(f\), because emptying split pairs preserves the source
full-pair count. Therefore every one-frame resolution misses at least

\[
\boxed{
 D_{m,q}:=\sum_f(T_{f,q}-V_f)_+}                       \tag{0.7}
\]

lower targets at depth \(q\), and the same number of upper targets.

This obstruction is macroscopic in the Gaussian window. If

\[
                         q=x\sqrt m+o(\sqrt m),
 \qquad x>0,                                           \tag{0.8}
\]

then

\[
\boxed{
 {D_{m,q}\over W}\longrightarrow
 e^{-x^2}\Phi(x/2)-\Phi(-3x/2)>0,}                    \tag{0.9}
\]

where \(W=\binom{2m}{m}\) and \(\Phi\) is the standard normal distribution
function. Thus a single resolution class already misses
\(\Theta_x(W)\) targets at the single depth \(q=x\sqrt m\).

At the top of the proposed Stage-B range,

\[
 q\asymp\sqrt{m\log m},
 \qquad
 \lambda_{f,q}=m^{-\Theta(1)}
 \tag{0.10}
\]

on \(1-o(1)\) of the target layer, so every fixed-pair resolution misses
\(1-o(1)\) of that layer.

Hence:

\[
\boxed{\text{one fixed-pair resolution class cannot cover all but }
       o(W)\text{ targets through }q\le\sqrt{m\log m}.}              \tag{0.11}
\]

The obstruction is an orbit-capacity obstruction, not a defect of a
particular isometric cycle factor. Mixing coordinate pairings, or leaving
the fixed-pair architecture, is necessary.

## 1. Pair types and orientation cubes

Fix a perfect matching

\[
                         \mathcal P=\{P_1,\ldots,P_m\},
 \qquad |P_i|=2.                                      \tag{1.1}
\]

For \(X\subseteq[2m]\), write

\[
\begin{aligned}
 F(X)&=\{i:P_i\subseteq X\},\\
 E(X)&=\{i:P_i\cap X=\varnothing\},\\
 S(X)&=\{i:|P_i\cap X|=1\}.                            \tag{1.2}
\end{aligned}
\]

If \(|X|=m\), then

\[
                         |F(X)|=|E(X)|=:f,\qquad
                         |S(X)|=m-2f.                  \tag{1.3}
\]

After the three pair-index sets \(F,E,S\) are fixed, the choice of one
coordinate from each split pair is an orientation cube

\[
                         Q_s=\{0,1\}^S,\qquad s=m-2f.  \tag{1.4}
\]

The number of such strata is

\[
                         {m!\over f!f!s!},             \tag{1.5}
\]

and each contains \(2^s\) middle owners. This proves (0.3).

Now let \(L\) have rank \(m-q\). From

\[
 2|F(L)|+|S(L)|=m-q,\qquad
 |F(L)|+|E(L)|+|S(L)|=m,                              \tag{1.6}
\]

one gets

\[
                         |E(L)|-|F(L)|=q.              \tag{1.7}
\]

Writing \(f=|F(L)|\) gives (0.1). To count such targets:

1. choose the \(f\) full pair indices;
2. choose the \(f+q\) empty pair indices;
3. orient every remaining split pair.

This gives (0.2). Summing over \(f\) gives

\[
                         \sum_fT_{f,q}=\binom{2m}{m-q}.              \tag{1.8}
\]

Complementation exchanges full and empty pairs, so the same number
\(T_{f,q}\) counts rank-\((m+q)\) targets having \(f\) empty and \(f+q\)
full pairs.

The pairing-preserving group

\[
                         G_{\mathcal P}=C_2^m\rtimes S_m             \tag{1.9}
\]

acts transitively on targets with a fixed \(f\), and cannot change \(f\).
These are the pair-type orbits relevant to Stage B.

## 2. Exact individual multiplicities

Let

\[
                         L=(F,E,S,\eta)               \tag{2.1}
\]

denote a lower target, where

\[
 |F|=f,\qquad |E|=f+q,\qquad |S|=m-2f-q,              \tag{2.2}
\]

and \(\eta\in\{0,1\}^S\) is its split-pair orientation.

For every \(D\in\binom Eq\), define the candidate source stratum

\[
 \sigma_D(L)=\bigl(F,\ E\setminus D,\ S\cup D\bigr).   \tag{2.3}
\]

It has \(f\) full, \(f\) empty, and

\[
                         s=|S|+|D|=m-2f              \tag{2.4}
\]

split pairs. Inside its orientation cube define the affine \(q\)-face

\[
 \mathcal F_D(L)
 =\{x\in Q_{S\cup D}:x|_S=\eta\}.                     \tag{2.5}
\]

The coordinates in \(D\) are free; all other split orientations are fixed.

Suppose the chosen resolution partitions every orientation cube into
isometric pair-flip cycles. For a \(q\)-face \(\mathcal F\) in a source
stratum \(\sigma\), let

\[
 a_{\sigma,q}(\mathcal F)
 =\#\{\text{forward depth-}q\text{ cycle windows spanning }\mathcal F\}.
                                                                  \tag{2.6}
\]

If a large orientation cube is first partitioned into coordinate
\(Q_h\)-fibres and every fibre receives an isometric \(2h\)-cycle factor,
(2.6) is summed over those fibres. Thus the notation covers exactly the
construction in the question.

### Theorem 2.1 (exact lower-shadow incidence formula)

For every lower target \(L=(F,E,S,\eta)\),

\[
\boxed{
 \mu_q^-(L)
  =\sum_{D\in\binom Eq}
       a_{\sigma_D(L),q}\bigl(\mathcal F_D(L)\bigr).}   \tag{2.7}
\]

In particular, \(L\) has exactly \(\binom{f+q}{q}\) candidate source faces.

#### Proof

Consider a forward geodesic \(q\)-window in a pair-flip cycle. Let \(D\)
be its set of \(q\) flipped pair coordinates. Its lower intersection:

* makes every pair in \(D\) empty;
* leaves every source-full pair full;
* leaves every source-empty pair empty; and
* retains the orientation of every unflipped split pair.

Therefore its lower target is \(L\) if and only if:

1. \(D\subseteq E(L)\);
2. the source empty set is \(E(L)\setminus D\);
3. the source full set is \(F(L)\); and
4. the residual orientation on \(S(L)\) is \(\eta\).

These conditions say precisely that the window spans
\(\mathcal F_D(L)\) in the source stratum \(\sigma_D(L)\). Distinct
\(D\)'s give distinct source strata. Summing their occurrence
multiplicities proves (2.7). \(\square\)

The upper formula is its complement. If
\(U=(E,F,S,\eta)^c\) has rank \(m+q\), its multiplicity is the analogous
sum over \(q\)-subsets of its full-pair set, using reverse windows.

### Corollary 2.2 (face-multiplicity bounds)

Assume \(q<h\) in every active \(Q_h\)-fibre.

1. For every cycle factor,

   \[
                         a_{\sigma,q}(\mathcal F)\le2^q.             \tag{2.8}
   \]

2. If, additionally, distinct windows spanning one face are
   vertex-disjoint—as they are when each standard
   \(\pi\pi\) tile is face-simple at depth \(q\)—then

   \[
             a_{\sigma,q}(\mathcal F)
                \le\left\lfloor{2^q\over q+1}\right\rfloor.         \tag{2.9}
   \]

3. If the factor is lower-rainbow at depth \(q\), then
   \(a_{\sigma,q}(\mathcal F)\in\{0,1\}\).

#### Proof

Every occurrence spanning \(\mathcal F\) starts at one of its \(2^q\)
vertices, and a factor gives one forward start at each owner. This proves
(2.8). Under the extra disjointness hypothesis, the corresponding
geodesic paths each consume \(q+1\) different vertices of the face, proving
(2.9). The last assertion is the definition of lower-rainbow injectivity.
\(\square\)

These bounds may improve an individual target's multiplicity, but they do
not change the orbit totals below.

## 3. Exact orbit totals

Let \(\mathcal L_{f,q}\) be the set of all lower targets of type \(f\).
Every middle owner in a type-\(f\) orientation stratum has one forward
depth-\(q\) window whenever its active cycle has at least \(q\) distinct
next directions. Emptying those directions does not change its \(f\) full
pairs.

### Theorem 3.1 (resolution-free type incidence)

For every \(f,q\) represented by the cycle factors,

\[
\boxed{
 \sum_{L\in\mathcal L_{f,q}}\mu_q^-(L)=V_f.}           \tag{3.1}
\]

Consequently the average multiplicity on the type orbit is exactly
\(\lambda_{f,q}=V_f/T_{f,q}\), namely (0.6).

#### Proof

There are \(V_f\) middle owners of type \(f\). Every owner is in exactly one
cycle and supplies exactly one forward depth-\(q\) window. Its lower target
has the same full-pair set and hence the same full-pair count \(f\).
Conversely every term counted on the left comes from one such owner-window.
This is a bijective double count, proving (3.1).

Dividing by \(|\mathcal L_{f,q}|=T_{f,q}\) gives the first expression in
(0.6). Direct division of (0.3) by (0.2) gives

\[
 {V_f\over T_{f,q}}
 =2^q\,{(f+q)!\over f!}\,{(m-2f-q)!\over(m-2f)!}
 ={2^q\binom{f+q}{q}\over\binom{m-2f}{q}}.
\]

\(\square\)

There is also an exact candidate-face double count. The total number of
candidate faces for type-\(f\) targets is

\[
\begin{aligned}
 T_{f,q}\binom{f+q}{q}
 &=\frac{m!}{f!^2q!(m-2f-q)!}\,2^{m-2f-q}.            \tag{3.2}
\end{aligned}
\]

On the source side there are

\[
                         {m!\over f!^2(m-2f)!}         \tag{3.3}
\]

orientation strata of dimension \(s=m-2f\), and each has

\[
                         2^{s-q}\binom sq              \tag{3.4}
\]

affine \(q\)-faces. Multiplying (3.3) and (3.4) gives (3.2). Thus every
candidate incidence in Theorem 2.1 is accounted for exactly.

## 4. Deterministic coverage obstruction

Let

\[
                         C_{f,q}
 =\#\{L\in\mathcal L_{f,q}:\mu_q^-(L)>0\}.             \tag{4.1}
\]

### Theorem 4.1 (pair-orbit capacity)

Every resolution confined to the fixed matching satisfies

\[
                         C_{f,q}\le\min\{T_{f,q},V_f\}.              \tag{4.2}
\]

Therefore its number \(M_q^-\) of uncovered lower targets obeys

\[
\boxed{
 M_q^-\ge D_{m,q}
        =\sum_f(T_{f,q}-V_f)_+.}                       \tag{4.3}
\]

The same statement holds for upper targets.

#### Proof

Every covered target consumes at least one occurrence. The total number of
occurrences available in its type orbit is \(V_f\) by Theorem 3.1, proving
(4.2). Summing \(T_{f,q}-C_{f,q}\) over \(f\) proves (4.3).
Complementation proves the upper statement. \(\square\)

This theorem remains valid if:

* every \(Q_h\)-fibre has a different isometric cycle factor;
* all factors are nonlinear and two-sided rainbow;
* their choices are coupled across every source stratum; or
* repeated faces are eliminated completely.

All these operations remain inside the same \(G_{\mathcal P}\)-orbits and
cannot move a start from source type \(f\) to a target of another type.

### Corollary 4.2 (symmetrized resolution multiplicity)

Average any fixed resolution over \(G_{\mathcal P}\). Every target of type
\(f\) then has fractional multiplicity exactly \(\lambda_{f,q}\).

#### Proof

The group is transitive on \(\mathcal L_{f,q}\), so the averaged
multiplicity is constant there. Its total is still \(V_f\) by (3.1);
division by \(T_{f,q}\) gives \(\lambda_{f,q}\). \(\square\)

Thus when \(\lambda_{f,q}<1\), even the completely symmetrized
one-resolution measure supplies less than one unit per target in that
orbit. The excess average multiplicity in rare orbits cannot be transferred
to the deficient ones.

## 5. Exact likelihood ratio and the Gaussian deficit

The likelihood ratio between the type-\(f\) target and source counts is

\[
\boxed{
 {T_{f,q}\over V_f}
 ={(m-2f)_{\underline q}\over
                 2^q(f+1)^{\overline q}}
 =\prod_{i=0}^{q-1}{m-2f-i\over2(f+1+i)}.}             \tag{5.1}
\]

It is strictly decreasing in \(f\). Hence the deficient source orbits
\(T_{f,q}>V_f\) form one initial interval in \(f\), determined exactly by

\[
                         (m-2f)_{\underline q}
                          >2^q(f+1)^{\overline q}.      \tag{5.2}
\]

The finite obstruction (4.3) is therefore completely explicit.

For its Gaussian form, let \(q=x\sqrt m+o(\sqrt m)\), \(x>0\), and put

\[
                         Z_m={f-m/4\over\sqrt m}.       \tag{5.3}
\]

Under the source weights \(V_f/W\),

\[
                         Z_m\Longrightarrow N(0,1/16),              \tag{5.4}
\]

while under the target weights
\(T_{f,q}/N_q\), \(N_q=\binom{2m}{m-q}\),

\[
                         Z_m\Longrightarrow N(-x/2,1/16).           \tag{5.5}
\]

Uniform Stirling expansion on bounded \(Z_m\)-ranges gives

\[
 \log{T_{f,q}\over V_f}
                         =-8xZ_m-3x^2+o(1).            \tag{5.6}
\]

The crossing \(T_{f,q}=V_f\) is consequently at

\[
                         Z_m=-{3x\over8}+o(1).         \tag{5.7}
\]

Also

\[
                         {N_q\over W}\longrightarrow e^{-x^2}.      \tag{5.8}
\]

### Theorem 5.1 (positive Gaussian orbit deficit)

For every fixed \(x>0\), under (0.8),

\[
\boxed{
 {D_{m,q}\over W}
 \longrightarrow
 e^{-x^2}\Phi(x/2)-\Phi(-3x/2)>0.}                    \tag{5.9}
\]

The convergence is uniform for \(x\) in a compact subinterval of
\((0,\infty)\).

#### Proof

By monotonicity, the positive part in (0.7) is supported on
\(Z_m<-3x/8+o(1)\). Therefore

\[
\begin{aligned}
 {D_{m,q}\over W}
 &={N_q\over W}
   \Pr_{\rm target}\!\left(
       Z_m<-{3x\over8}+o(1)\right)\\
 &\qquad
 -\Pr_{\rm source}\!\left(
       Z_m<-{3x\over8}+o(1)\right).                   \tag{5.10}
\end{aligned}
\]

Under (5.5), standardizing the first threshold gives

\[
 {(-3x/8)-(-x/2)\over1/4}={x\over2};
\]

under (5.4), standardizing the second gives

\[
 {(-3x/8)-0\over1/4}=-{3x\over2}.
\]

Equations (5.4), (5.5), and (5.8) yield (5.9).

For \(Z<-3x/8\), the limiting likelihood ratio
\(\exp(-8xZ-3x^2)\) is strictly larger than one, and this interval has
positive limiting source mass. Hence the positive-part integral over that
interval is strictly positive. Equivalently, the strictly decreasing
finite likelihood ratio (5.1) crosses one once, and its limiting initial
interval in (5.10) has a strict excess. \(\square\)

Taking, for example, \(x=1\) gives

\[
                         D_{m,\lfloor\sqrt m\rfloor}
                               =(\kappa+o(1))W,\qquad \kappa>0.      \tag{5.11}
\]

Thus failure by \(o(W)\) is already impossible at one depth inside every
range extending to \(\sqrt{m\log m}\).

## 6. Growing Gaussian depth

For a uniformly random rank-\((m-q)\) target, the type \(f\) is
concentrated in an \(O(\sqrt m)\) window about

\[
                         f_*={(m-q)^2\over4m}.          \tag{6.1}
\]

For \(q=O(\sqrt{m\log m})\), expansion of (0.6) at this saddle gives

\[
\boxed{
 \log\lambda_{f_*,q}
   =-{q^2\over m}
      +O\left({q\over m}+{q^3\over m^2}\right).}        \tag{6.2}
\]

Moreover, throughout any \(a_m\sqrt m\) type window,

\[
 \left|\log\lambda_{f,q}-\log\lambda_{f_*,q}\right|
                         =O\left({a_mq\over\sqrt m}\right).         \tag{6.3}
\]

### Theorem 6.1 (almost-total target-layer failure)

Suppose

\[
 {q\over\sqrt m}\longrightarrow\infty,\qquad
 q=O(\sqrt{m\log m}).                                  \tag{6.4}
\]

Then every fixed-pair resolution covers only \(o(N_q)\) lower targets and
only \(o(N_q)\) upper targets:

\[
\boxed{
 M_q^\pm=(1-o(1))N_q.}                                 \tag{6.5}
\]

#### Proof

Choose \(a_m\to\infty\) sufficiently slowly that

\[
                         {a_mq\over\sqrt m}
                                  =o(q^2/m).            \tag{6.6}
\]

The corresponding type window contains \(1-o(1)\) of the target layer.
Equations (6.2)--(6.3) give

\[
                         \lambda_{f,q}
                          =\exp(-(1+o(1))q^2/m)=o(1)   \tag{6.7}
\]

uniformly there.

For each type orbit, (4.2) gives

\[
                         {C_{f,q}\over T_{f,q}}
                              \le\min\{1,\lambda_{f,q}\}.             \tag{6.8}
\]

Summing (6.8) over the central target window gives \(o(N_q)\) covered
targets there; the complement contains only \(o(N_q)\) targets. This proves
the lower statement. Complementation proves the upper statement.
\(\square\)

For \(q=\sqrt{m\log m}\), (6.2) gives

\[
                         \lambda_{f_*,q}=m^{-1+o(1)}.  \tag{6.9}
\]

The source occurrence supply in a typical type orbit is therefore smaller
than its target demand by a factor \(m^{1-o(1)}\).

## 7. Consequence for Stage B

Let \(H=\lfloor\sqrt{m\log m}\rfloor\). A single fixed-pair resolution
class cannot satisfy any of the following:

1. cover all but \(o(W)\) lower targets simultaneously for \(q\le H\);
2. cover all but \(o(W)\) upper targets simultaneously for \(q\le H\);
3. give an \(o(W)\) aggregate lower-plus-upper hole count through that
   band; or
4. realize the depth census of one Boolean SCD inside the fixed frame.

Indeed item 1 already fails at \(q=\lfloor\sqrt m\rfloor\) by (5.11);
the others are stronger. At growing multiples of \(\sqrt m\), Theorem 6.1
shows that the failure occupies almost the entire target layer.

The conclusion does not depend on:

* which isometric \(2h\)-cycle factor is used in a \(Q_h\)-fibre;
* whether different fibres use unrelated factors;
* whether every factor is face-simple or two-sided rainbow;
* whether the fibre resolutions are chosen adversarially or jointly; or
* whether cuts are avoided by prefix collars.

All such constructions retain the same global matching \(\mathcal P\), and
therefore the invariant type-flow equation (3.1).

To evade the obstruction, Stage B must mix coordinate matchings at the
owner/block level or use a construction whose lower windows can change the
full-pair type. A new tiling theorem confined to the same \(Q_h\) fibres,
however strong locally, cannot do so.
