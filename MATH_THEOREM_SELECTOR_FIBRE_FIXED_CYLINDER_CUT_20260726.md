# Selector fibres: the exact fixed-cylinder law and the remaining grouped Hall gate

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Result

Let a physical product status cell be (Q_S).  Reserve a fixed set
(B\subseteq[S]) of (t) selector directions, put

\[
                         V=S-t,
\tag{0.1}
\]

and, for every selector word (z\in Q_B), choose an active set
(A_z\in\binom{[S]\setminus B}{r}) and a legal conjugate of an
injective (Q_r) compiler.  All directions in (B) are frozen throughout
every packet.  This gives an exact owner partition, but it has the
following exact target-side restriction.

For every protected depth (q), a trace direction set (J) must satisfy

\[
                         J\cap B=\varnothing.        \tag{0.2}
\]

Under the complete symmetric catalogue of active sets and compiler
conjugates, the normalized direction-set law is exactly

\[
 \boxed{
 \pi_{B,q}(J)=
 \begin{cases}
  \binom Vq^{-1},&J\subseteq[S]\setminus B,\\[2mm]
  0,&J\cap B\ne\varnothing.
 \end{cases}}                                      \tag{0.3}
\]

Consequently its total-variation distance from the uniform law on all
(q)-subsets of the original (S) directions is

\[
 \boxed{
 \left\|\pi_{B,q}-\operatorname{Unif}\binom{[S]}q\right\|_{\rm TV}
 =1-{\binom{S-t}q\over\binom Sq}.}                 \tag{0.4}
\]

In fact (0.4) is the minimum possible distance for *any* labeling using
this fixed selector set, since every resulting law is supported on the
same cylinder (0.2).  Writing

\[
 a_q(S,t):={\binom{S-t}q\over\binom Sq},             \tag{0.5}
\]

we have

\[
 a_q(S,t)
 =\prod_{i=0}^{q-1}{S-t-i\over S-i}
 \le \exp\!\left(-{tq\over S}\right).              \tag{0.6}
\]

This gives an entropy--cylinder incompatibility for the proposed complete
catalogue.  Its number of indexed labels is

\[
 K=\binom Vr2^rr!=2^r(V)_{\underline r}.             \tag{0.7}
\]

If (2^t\ge K), (S=\Theta(m)), (r=o(S)), and the certified compiler
protects (q=H\le r/4-1), then

\[
 {tH\over S}
 \ge {H r\log_2(V-r+1)\over S}.                    \tag{0.8}
\]

In particular, when

\[
 H^2\asymp m\log m,qquad r\ge4(H+1),qquad S=\Theta(m),
\tag{0.9}
\]

the right side of (0.8) is Ω\((\log m)^2\), and hence

\[
                         a_H(S,t)
 \le\exp[-\Omega((\log m)^2)]=o(1).                \tag{0.10}
\]

Thus complete batching is an exact design on the payload directions but
is maximally far from an all-direction design inside the original cell at
Gaussian depth.  This does **not** prove a global Hall deficit: different
product cells may use different selector sets (B_C), and the same
physical target may be rescued by another cell.  It proves that such
cross-cell rescue is indispensable and must occur in the literal Hall
ledger.

The exact fractional load of a physical target (T) is therefore not
merely a constant times its unqualified candidate degree.  If (J_C(T))
is its forced (q)-direction set in a candidate cell (C), then the
complete-catalogue fractional load is

\[
 \boxed{
 \mu_{q}^{\epsilon,\mathrm{frac}}(T)
 =\sum_{C:\,T\text{ is a signed candidate in }C}
 {2^q\over\binom{S_C-t_C}q}
 \mathbf1_{\{J_C(T)\cap B_C=\varnothing\}}.}        \tag{0.11}
\]

Formula (0.11), followed by a grouped integral rounding using one common
nested compiler label per selector fibre, is the minimum remaining
selector theorem.

## 1. Exact owner partition and the selector decoder

Identify

\[
                         Q_S=Q_B\times Q_{[S]\setminus B}.
\tag{1.1}
\]

For (z\in Q_B), choose (A_z\subseteq[S]\setminus B), 
(|A_z|=r).  For each

\[
 y\in Q_{[S]\setminus(B\cup A_z)},
\]

the set

\[
 P_{z,y}=\{x:x|_B=z,
                 x|_{[S]\setminus(B\cup A_z)}=y\} \cong Q_r
\tag{1.2}
\]

is a physical packet.  The packets (1.2) partition the (z)-fibre, and
the (z)-fibres partition (Q_S).  Hence arbitrary choices of (A_z)
and of legal compiler conjugates preserve ownership exactly.

Every selector direction is singleton in every source owner of its fibre
and is never traversed.  Its endpoint therefore remains singleton in both
the lower intersection and the upper union.  A literal target contributed
by this cell recovers

\[
                         z=T|_B                    \tag{1.3}
\]

uniquely.  This is a decoder, not an averaged label.  For a target with
forced cell-direction set (J), occurrence under the row label
λ\(_z\) has the form

\[
 m_{C,q}^{\epsilon}(T)
 =\mathbf1_{\{J\cap B=\varnothing\}}
  \mathbf1_{\{R_C(T)\in\mathcal F_q^\epsilon(\lambda_z)\}},
\tag{1.4}
\]

where (R_C(T)) is the corresponding payload affine face.  In
particular, summing labels over other selector rows says nothing
targetwise about (1.4).

## 2. Pointed and unpointed marginals

Fix a payload owner (v\in Q_V) and an ordered (q)-tuple
δ\(=(i_1,\ldots,i_q)\) of distinct payload directions.  Choose an indexed
label ((A,g)) uniformly from

\[
 \binom{[V]}r\times(\mathbb F_2^r\rtimes\mathfrak S_r).
\tag{2.1}
\]

The probability that (A) contains all directions in δ is

\[
 {\binom{V-q}{r-q}\over\binom Vr}
 ={(r)_{\underline q}\over(V)_{\underline q}}.       \tag{2.2}
\]

Conditional on this event, the uniform axis permutation sends the
return-free ordered compiler prefix to δ with probability
(1/(r)_{\underline q}).  Endpoint translations make the basepoint
uniform but do not alter the direction count.  Therefore

\[
 \boxed{
 \Pr\{\text{the pointed prefix at }v\text{ is }\delta\}
 ={1\over(V)_{\underline q}}.}                      \tag{2.3}
\]

The prefixes for different (q\)'s are the truncations of one label, so
(2.3) is a genuinely nested law.

Now fix one affine (q)-face (R\subseteq Q_V).  Trace injectivity says
that two different starts cannot select the same lower trace face (and
similarly above).  The (2^q q!) pointed start/order descriptions of
(R) are therefore disjoint events.  Summing (2.3) yields

\[
 \boxed{
 \Pr\{R\text{ is a selected signed trace face}\}
 ={2^qq!\over(V)_{\underline q}}
 ={2^q\over\binom Vq}.}                             \tag{2.4}
\]

Both signs have (2.4); they are coupled by the same compiler chronology
and are not independent.

For a face of the original (Q_S), (2.4) applies only if its direction
set avoids (B).  This proves the targetwise fractional formula
(0.11).  After normalizing by total selected traces, symmetry makes the
direction law uniform over β\(\binom{[S]\setminus B}q\), proving (0.3).

## 3. Proof and scale of the fixed-cylinder cut

Every selected (q)-trace uses only active directions in (A_z), and
(A_z\cap B=\varnothing).  Hence every possible direction law is
supported on

\[
 \mathcal C_{B,q}=\{J\in\tbinom{[S]}q:J\cap B=\varnothing\}.
\tag{3.1}
\]

The uniform law on all (q)-sets gives this cylinder mass

\[
 U_{S,q}(\mathcal C_{B,q})
 ={\binom{S-t}q\over\binom Sq}=a_q(S,t).            \tag{3.2}
\]

Any probability measure supported on Ω\(\mathcal C_{B,q}\) has total
variation distance at least (1-a_q(S,t)) from (U_{S,q}).  The complete
catalogue is uniform on Ω\(\mathcal C_{B,q}\), so equality holds.  This
proves (0.4).

Taking the product in (0.5) and using

\[
 1-{t\over S-i}\le e^{-t/(S-i)}\le e^{-t/S}
\]

proves (0.6).

Finally, (0.7) and (V\ge r) give

\[
 \log_2K
 =r+\sum_{i=0}^{r-1}\log_2(V-i)
 \ge r+r\log_2(V-r+1).                             \tag{3.3}
\]

Thus (t\ge\log_2K) implies (0.8).  Under (0.9), (r\ge4H),
(V-r=\Theta(m)), and (S=\Theta(m)), so

\[
 {tH\over S}
 \ge(4+o(1)){H^2\log_2m\over S}
 =\Omega((\log m)^2).
\tag{3.4}
\]

Together with (0.6), this proves (0.10).

The same issue remains if one omits compiler conjugates and tries merely
to make every payload (H)-set eligible under some active set.  The
covering count

\[
 2^t\binom rH\ge\binom VH                            \tag{3.5}
\]

is necessary, hence

\[
 t\ge\log_2{\binom VH\over\binom rH}.               \tag{3.6}
\]

At the Gaussian scale and for polynomially sublinear (r), (3.6) again
makes (tH/S=\Omega((\log m)^2)).  This is not a contradiction: (3.5)
balances directions across different selector cylinders, whereas a
literal target belongs to only one cylinder.

## 4. Orthogonal arrays, divisibility, and grouping

Put (M=2^t).  For a list of active sets (A_z\in\binom{[V]}r), define

\[
 c_q(J)=|\{z:J\subseteq A_z\}|.                     \tag{4.1}
\]

Exact uniform (q)-incidence would require

\[
 c_q(J)=M{\binom rq\over\binom Vq}.                 \tag{4.2}
\]

Thus the right side of (4.2) must be an integer.  At (q=1), this is

\[
                         {2^tr\over V}\in\mathbb Z. \tag{4.3}
\]

Odd factors of (V/\gcd(V,r)) cannot be cleared by increasing the number
of binary selector coordinates.  Exact higher-strength designs have the
usual derived divisibilities

\[
 2^t{\binom{r-i}{H-i}\over\binom{V-i}{H-i}}
 \in\mathbb Z\qquad(0\le i\le H).                  \tag{4.4}
\]

Floor/ceiling balance avoids exact divisibility but not nesting.  The
counts obey the integral flow identities

\[
 \sum_{x\notin J}c_{q+1}(J+x)=(r-q)c_q(J).          \tag{4.5}
\]

Nor is the incidence matrix automatically integral: on three directions,
the columns for the three two-subsets give

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
 \qquad\det=-2.                                    \tag{4.6}
\]

Most importantly, even a perfect solution of (4.2)--(4.5) balances sums
over (z).  The summands correspond to different literal target
cylinders because of decoder (1.3).  It cannot change a zero in (1.4)
for one prescribed row.

There is also a packet-grouping constraint.  All (2^{V-r}) packets in
one selector fibre use the same active support (A_z).  Therefore any
prescribed nested flag table realizable by this construction must satisfy

\[
 \boxed{
 \left|\bigcup_{v\in Q_V}D_H(z,v)\right|\le r}      \tag{4.7}
\]

for each (z).  If one conjugate is common to the whole fibre, its prefix
function must additionally be independent of the inactive word.  Allowing
a separate conjugate for every packet (P_{z,y}) removes this latter
condition and can remove the (2^rr!) term from the selector-bit budget,
but it does not remove (0.2), (1.3), or (4.7): the target also decodes its
relevant frozen packet cylinder.

Finally, a literal (C_{2r}) context compiler requires the previously
audited admissible packet dimension (in the current construction,
(r=8\cdot2^u) and (H\le r/4-1)).  The owner subcube partition itself
has no such restriction, but compiler divisibility cannot be supplied by
an orthogonal array.

## 5. Exact global integral program

Index retained product cells by (C).  For a candidate target (T), let
(z_C(T)) be its decoded selector word and let (J_C(T)) be its forced
direction set.  For a legal row label λ, define

\[
 a_{C,z,\lambda}^{q,\epsilon}(T)\in\{0,1\}
\tag{5.1}
\]

to record literal occurrence, including rank-twisted compatibility,
the fixed-cylinder condition, and the compiler chronology.  The variables
are

\[
 x_{C,z,\lambda}\in\{0,1\},\qquad
 \sum_\lambda x_{C,z,\lambda}=1.                   \tag{5.2}
\]

The target loads are

\[
 \boxed{
 \mu_q^\epsilon(T)=
 \sum_{C:\,T\text{ candidate in }C}
 \sum_\lambda
 a_{C,z_C(T),\lambda}^{q,\epsilon}(T)
 x_{C,z_C(T),\lambda}.}                            \tag{5.3}
\]

One variable in (5.2) controls all depths and both signs.  Complete
batches or orthogonal arrays control column sums after summing over every
(z); (5.3) takes one prescribed row from each candidate cell.  This is
the exact integral grouping obstruction.

A positive selector theorem must therefore prove both:

1. the selector-conditioned fractional Hall inequalities, beginning with
   (0.11), including enough cross-cell avoidance of every (B_C); and
2. an integral rounding of (5.2)--(5.3) preserving the common nested
   lower/upper chronology.

The first condition is not implied by potential reachability, and the
second is not implied by an OA or by total unimodularity.

## 6. Boundary

Proved here:

* the exact pointed and affine-face marginals at every depth;
* the exact fixed-selector cylinder law and its total-variation deficit;
* the Gaussian-scale entropy--cylinder incompatibility of complete
  catalogue batching;
* the binary divisibility and nested incidence-flow constraints; and
* the literal row-decoder/grouping formulation.

Not proved:

* a global deficit, since selector sets may vary between product cells;
* the selector-conditioned cross-cell Hall inequality;
* integral common-owner rounding; or
* coefficient one.

The selector-fibre lever is therefore a genuine exact owner
derandomization, but a fixed selector set is not a locally symmetric
target derandomization.  Its only possible Gaussian use requires an
explicit cross-cell cylinder-cover theorem.
