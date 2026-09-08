# Nonanchored uniform caps admit exact two-socket neutralization

**Date:** 2026-08-05  
**Method:** pure mathematics; uniform joint mixability and compact measure
transport; no search or solver  
**Status:** unconditional exact local construction and complete transport
dual.  Every nonanchored socket-uniform layer can be absorbed in a
two-socket packet using one anchored socket layer and one lower-anchored job
layer.  Simultaneous absorption of an arbitrary cap bank is exactly one
compact one-dimensional resource transport with a complete price dual.
For the first Rayleigh residual this isolates the entire endpoint-decreasing
socket bank; the required domination/price inequalities are not yet proved.

## 1. Exact one-cap packet

Fix a common ceiling `B>0`.  Let

\[
 C=[a,d]\subseteq[0,B],\qquad d<B
\]

be a nonanchored socket interval, let

\[
 A_c=[c,B]
\]

be an anchored socket interval, and let

\[
 J_z=[B,z]
\]

be an anchored job interval.

### Theorem 1.1 (one-cap pair criterion)

Uniform random variables

\[
 X\sim U_{J_z},\qquad Y\sim U_C,\qquad Z\sim U_{A_c}
\]

can be coupled with

\[
 X=Y+Z\quad\text{almost surely}                  \tag{1.1}
\]

if and only if

\[
 \boxed{
 B+a\le z\le B+d,
 \qquad c=z-a-d.}                                \tag{1.2}
\]

### Proof

Midpoint equality forces

\[
 {B+z\over2}={a+d\over2}+{c+B\over2},
\]

which is exactly `c=z-a-d`.

Under that identity the three interval widths are

\[
 z-B,\qquad d-a,\qquad B-z+a+d,                  \tag{1.3}
\]

and their sum is `2d`.  The uniform joint-mixability polygon condition is
therefore equivalent to requiring every width in (1.3) to be at most `d`.
The middle width already is.  The other two inequalities are

\[
 z\le B+d,
 \qquad z\ge B+a.
\]

They also imply `B-d<=c<=B-a`, so `A_c` is a valid socket interval.  The
uniform joint-mixability theorem now gives (1.1).  Necessity follows from
the same midpoint and width conditions. `square`

Thus every internal layer has a nonempty continuum of legal pair packets;
its legal job endpoint interval has length `d-a`.

### Corollary 1.2 (canonical midpoint packet)

Put

\[
 m={a+d\over2},\qquad z=B+m,qquad c=B-m.         \tag{1.4}
\]

Then (1.2) holds.  Hence every cap layer `U[a,d]` has the explicit packet

\[
 U[B,B+m]
 \quad\longleftrightarrow\quad
 U[a,d]+U[B-m,B].                                \tag{1.5}
\]

This deterministic choice is useful as a simple domination test, although
the full interval of choices in (1.2) is strictly more flexible.

## 2. Cap and anchored layer banks

Let `g` be a continuous socket density on `[0,B]`.  Fix any exact uniform-
interval barycenter representation of `g(y)dy` and split its layer measure
as

\[
 \Lambda_g=\Lambda_{\rm anc}+\Lambda_{\rm cap},  \tag{2.1}
\]

where `Lambda_anc` consists of components whose right endpoint is `B`, and
`Lambda_cap` consists of all components `[a,d]` with `d<B`.

The canonical superlevel decomposition is one permissible choice.  Another
important choice is to write `g=h+k`, decompose a nondecreasing `h`
canonically into anchored layers, and decompose a two-endpoint-zero cap `k`
canonically into internal layers.  Only the barycenter identity is used
below; the combined layer measure need not be the canonical decomposition
of `g` itself.

Let `f` be decreasing on `[B,infinity)`.  Its canonical job-layer measure
`Lambda_f` is supported on intervals `[B,z]`.  Only the compact restriction
`B<=z<=2B` can participate in Theorem 1.1.

A **cap transport** is a measure `Pi` on pairs `([a,d],z)` supported on

\[
 B+a\le z\le B+d,                                \tag{2.2}
\]

such that

1. its cap marginal is exactly `Lambda_cap`;
2. its job-endpoint marginal is dominated by `Lambda_f`;
3. under `c=z-a-d`, its anchor-endpoint marginal is dominated by
   `Lambda_anc`.

### Theorem 2.1 (cap-neutralization lift)

Every cap transport gives an exact packet coagulation of the complete
nonanchored socket-layer bank.  Removing those packets leaves only
lower-anchored job layers and upper-anchored socket layers, with equal
remaining work.

### Proof

Apply Theorem 1.1 to every point of `Pi` and measurably select a uniform
joint mix.  The exact cap marginal uses every internal layer once; the two
dominated resource marginals use available job and anchored-socket layers.
Integrating packet laws gives the claimed literal marginals.  Packetwise
sum equality preserves work, so subtracting the used layers leaves equal
work.  By definition every remaining socket layer is anchored. `square`

The residual anchored pair is then governed exactly by the endpoint-
composition theorem.

## 3. Complete compact price dual

The cap transport has a closed one-dimensional dual.  Let `phi(z)>=0` be a
continuous price on job endpoints `z in[B,2B]`, and let `psi(c)>=0` be a
continuous price on anchor endpoints `c in[0,B]`.  Define

\[
 \Xi_{\phi,\psi}(a,d)
 =\min_{B+a\le z\le B+d}
   \bigl[\phi(z)+\psi(z-a-d)\bigr].               \tag{3.1}
\]

### Theorem 3.1 (cap-transport price criterion)

A cap transport exists if and only if

\[
 \boxed{
 \int\Xi_{\phi,\psi}(a,d)\,d\Lambda_{\rm cap}(a,d)
 \le
 \int\phi(z)\,d\Lambda_f(z)
 +\int\psi(c)\,d\Lambda_{\rm anc}(c)}           \tag{3.2}
\]

for every pair of continuous nonnegative prices `phi,psi`, where the job
integral may be restricted to `[B,2B]`.

### Proof

Necessity follows by applying (3.1) to every selected packet and integrating
the two resource marginals.

For sufficiency, measures with fixed cap marginal on the compact relation
(2.2) form a compact convex set.  Map each to its pair of job and anchor
resource marginals.  The target set of pairs dominated coordinatewise by
`(Lambda_f,Lambda_anc)` is also compact and convex.  If the two sets were
disjoint, strong separation would give continuous resource prices.  The
coordinatewise downward closure lets both prices be taken nonnegative.
Minimizing the separated price over a legal `z` for each fixed cap gives
exactly (3.1), by compact measurable selection.  The strict separator would
therefore contradict (3.2). `square`

Thus (3.2) is not merely a necessary family of Hall cuts; it is the complete
fractional cap-resource criterion.

## 4. Two explicit sufficient constructions

### 4.1 A deterministic midpoint test

Let `T_J([a,d])=B+(a+d)/2` and
`T_A([a,d])=B-(a+d)/2`.  Corollary 1.2 gives:

\[
 (T_J)_\#\Lambda_{\rm cap}\le\Lambda_f,
 \qquad
 (T_A)_\#\Lambda_{\rm cap}\le\Lambda_{\rm anc} \tag{4.1}
\]

implies cap-transport feasibility.  The inequalities are measure
domination, not only total-mass comparisons.  Failure of (4.1) would not
disprove (3.2), because the free endpoint `z` may be routed anywhere in
the full interval (2.2).

### 4.2 Uniform spreading gives an exact reflected cap demand

There is a more natural kernel which uses the complete legal interval.
For every cap layer `I=[a,d]`, choose `x` uniformly on `I` and put

\[
 z=B+x,
 \qquad
 c=B-a-d+x.                                      \tag{4.2}
\]

Then `z in[B+a,B+d]` and `c=z-a-d`, so Theorem 1.1 applies.  Reflection
`y=a+d-x` shows that `c=B-y`, where `y` is also uniform on `I`.

Let `k` be the cap density whose canonical layer measure is
`Lambda_cap`.  The job-endpoint marginal demanded by (4.2) is exactly

\[
 k(z-B){\bf1}_{[B,2B]}(z)\,dz,                  \tag{4.3}
\]

and the anchor-endpoint marginal is exactly

\[
 k(B-c){\bf1}_{[0,B]}(c)\,dc.                   \tag{4.4}
\]

Indeed, the layer measure of `I` is `|I|dt`, while the uniform choice of
`x` has density `1/|I|`.  For a test function `phi`, Tonelli gives

\[
\begin{aligned}
 &\int_0^\infty\sum_{I\subset\{k>t\}}
   \int_I\phi(B+x)\,dx\,dt\\
 &=\int_0^B\phi(B+x)
   \left(\int_0^{k(x)}dt\right)dx
 =\int_0^B\phi(B+x)k(x)\,dx.
\end{aligned}                                    \tag{4.5}
\]

The anchor formula follows from the measure-preserving reflection
`x mapsto a+d-x` inside every interval layer.

### Corollary 4.1 (two one-dimensional domination rows)

The complete cap bank is neutralized if

\[
 \boxed{
 k(z-B)\,dz\le d\Lambda_f(z)
 \quad(B\le z\le2B)}                             \tag{4.6}
\]

and

\[
 \boxed{
 k(B-c)\,dc\le d\Lambda_{\rm anc}(c)
 \quad(0\le c\le B).}                           \tag{4.7}
\]

When the anchored densities are differentiable, their canonical endpoint
layer measures are

\[
 d\Lambda_f(z)=-(z-B)f'(z)\,dz,
 \qquad
 d\Lambda_{\rm anc}(c)=(B-c)h'(c)\,dc.          \tag{4.8}
\]

Thus (4.6)--(4.7) become the pointwise inequalities

\[
 k(y)\le-y f'(B+y),
 \qquad
 k(y)\le y h'(B-y),
 \qquad0<y<B.                                    \tag{4.9}
\]

In general (4.8) is read as a Stieltjes identity.  Equations
(4.6)--(4.9) are sufficient, not necessary; the full flexible criterion
remains (3.2).

## 5. Rayleigh consequence and exact frontier

For the first transformed Rayleigh pair:

* `f_2=u'` is strictly decreasing on `(b,infinity)`, so every canonical job
  layer is `[b,z]`;
* `g_2=-K'-u'` decreases near `b`, so its canonical layer measure has a
  positive nonanchored bank `Lambda_cap`.

Taking `B=b`, Theorems 2.1 and 3.1 show that this entire cap bank has no
remaining packetwise joint-mixability obstruction.  Its exact unresolved
content is the two-resource inequality (3.2).  The uniform-spreading kernel
reduces a concrete sufficient proof to the two explicit derivative/
Stieltjes rows (4.6)--(4.9).  If either that sufficient test or the full
price criterion holds, the cap disappears into literal two-socket packets
and the rest of the continuum problem reduces to bounded endpoint
composition of anchored layers.

This does not yet prove (3.2) for the Rayleigh layer measures, nor the final
anchored endpoint composition.  It does replace an arbitrary nonanchored
uniform-packet search by one compact scalar interval transport.

## 6. Primary reference

The local packet criterion uses the uniform case of Bin Wang and Ruodu
Wang, *Joint Mixability*, Mathematics of Operations Research **41** (2016),
808--826:
<https://www.math.uwaterloo.ca/~wang/papers/2015Wang-Wang-MOR.pdf>.

## 7. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_UNIFORM_LAYER_PACKET_TRANSPORT_AND_EQUAL_SPLIT_GATE_20260805.md`,
   SHA at use
   `38cd384bfc1f92a3108204d5e5fb87507d991881cc2c911b583a099825e12784`.
2. `MATH_THEOREM_ANCHORED_UNIFORM_PACKET_ENDPOINT_COMPOSITION_20260805.md`,
   SHA at use
   `664a85fd2f9162d33304f635764598d32479aa1c9697481767afd473430114f0`.
3. `MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_JOB_DENSITY_DECREASE_20260805.md`,
   SHA at use
   `a93f28d2364a84f4c4a5d3a1581c11c22419db3059ac8ea8fbbebf8684db5afa`.
4. `MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_SOCKET_ENDPOINT_DECREASE_NOGO_20260805.md`,
   SHA at use
   `78e017354f77b21e6ba0c53301027e25cec3ffd020872727cbe9aab8802469c7`.
