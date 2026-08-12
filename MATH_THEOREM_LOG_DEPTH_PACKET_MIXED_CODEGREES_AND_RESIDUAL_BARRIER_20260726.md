# Logarithmic-depth packet pilot: mixed codegrees and the residual-link barrier

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Outcome

Put

\[
 n=2m,\qquad B=2^r,\qquad
 r=\alpha\log _2m+O(1),\quad 0<\alpha<1,
 \qquad 1\le H\le r/4.                                  \tag{0.1}
\]

Assume that \(r\) is an admissible dimension for the chosen simultaneous
cube compiler.  For a compiler restricted to power-of-two dimensions,
all assertions below hold along the corresponding subsequence.  For all
\(m\), one may instead take the largest admissible \(r=\Theta(\log m)\)
below \(\alpha\log _2m\); then \(B=m^{\beta_m}\) with
\(0<\liminf\beta_m\le\limsup\beta_m<1\), and every estimate is unchanged
with \(\alpha\) replaced by \(\beta_m\).

Take the full moving-frame catalogue of physical \(Q_r\) owner packets,
decorate every packet by a simultaneous injective trace factor through
depth \(H\), and use the exact target quota

\[
 p_q={\binom{2m}{m-q}\over\binom{2m}m}.                 \tag{0.2}
\]

The correction in
MATH_THEOREM_Q4_MIXED_FRAME_MOSAIC_POTENTIAL_GAUSSIAN_COVER_20260726.md
is essential: this pilot cannot be carried out inside one frozen product
of four-block mosaics.  That product has the exact Gaussian source
ratio

\[
 {2^q\binom gq\over\binom{u+q}q}\longrightarrow e^{-6A^2}
 \quad\text{at }q=A\sqrt m
\]

on a positive-density target profile.  The present logarithmic pilot
therefore uses genuinely moving \(Q_r\) frames.  It is not a solution of
Gaussian CPM.

For the pilot, the complete pair-codegree calculation is favorable.
Every augmented edge has

\[
 K=(1+2H)B+O(H)=\Theta(BH),                            \tag{0.3}
\]

and, after exact coordinate-orbit balancing, every pair of distinct
resources has normalized codegree at most

\[
 \boxed{\frac{\Delta _2}{D}\le C\,\frac{H+1}{m}.}      \tag{0.4}
\]

The extra factor \(H\) in (0.4) is real: it comes from containment
between traces at adjacent depths.  Thus the depth-one containment value
\(2/(m+1)\) is not by itself the full mixed-codegree table.  Nevertheless

\[
 \boxed{
 K\frac{\Delta _2}{D}
 =O\left({2^rH(H+1)\over m}\right)
 =m^{\alpha-1}(\log m)^{O(1)}=o(1).}                  \tag{0.5}
\]

So there is no static growing-rank codegree obstruction to the
\(c\log m\) pilot.

There is, however, a sharp obstruction to the standard iterative nibble.
Even the richest simple physical catalogue has degree through one owner
at most

\[
 D_{\rm phys}\le
 \binom mr^2r!\;r^B(B+1)^{2H}.                         \tag{0.6}
\]

If \(H=\Theta(\log m)\), then

\[
 \log D_{\rm phys}
 =O(r\log m+B\log r+H\log B)=o(K).                    \tag{0.7}
\]

Retain every genuine resource independently with a fixed probability
\(z<1\).  Conditional on retaining a middle owner, its expected surviving
physical link is at most

\[
 D_{\rm phys}z^{K-1}=o(1).                             \tag{0.8}
\]

Hence all but \(o(1)\) of the retained middle owners lie in no surviving
packet.  More generally, owner-link death already occurs whenever

\[
 (1-z)H/\log r\longrightarrow\infty.                  \tag{0.9}
\]

There can still be exponentially many surviving packets globally,
because \(\log W=\Theta(m)\) while \(K=o(m)\).  They are concentrated on
an asymptotically negligible set of residual vertices.  Global edge
abundance is therefore not hereditary degree control.

Conclusion: the static hypothesis \(K\Delta _2/D=o(1)\) is verified, but
it does not justify a growing-uniformity Pippenger--Spencer or residual
nibble citation.  A logarithmic-depth colored near-factor remains
possible only through a one-shot structured resolution or an absorber
whose remainder is deliberately packet-closed.  No such near-factor is
claimed here.

## 1. Packet coordinates and quota sizes

Let a physical packet have core \(F\), \(|F|=m-r\), and disjoint active
pairs

\[
 E_1,\ldots,E_r.
\]

An owner chooses one endpoint of every active pair.  Thus the owner set
is an affine \(Q_r\) of size \(B=2^r\).

For each \(q\le H\), the simultaneous compiler selects \(B\) distinct
affine \(q\)-faces.  Their lower traces have rank \(m-q\), their upper
traces have rank \(m+q\), and both trace maps are injective.

The elementary product expansion

\[
 p_q=\prod_{j=0}^{q-1}{m-j\over m+j+1}
     =1-O(q^2/m)                                      \tag{1.1}
\]

is uniform for \(q\le H=O(\log m)\).  Since \(B=m^{\alpha+o(1)}\),

\[
 B(1-p_q)=O(BH^2/m)=o(1).                             \tag{1.2}
\]

Consequently an integral quota marking at a signed depth claims either
\(B\) or \(B-1\) traces.  The augmented edge therefore has

\[
 B+2H(B-1)\le K\le B+2HB,                             \tag{1.3}
\]

which proves (0.3).  A fractional mixture of the two quota sizes gives
the exact marginal \(Bp_q\).

## 2. Orbit normalization

Write \(0\) for the owner class, \(L_q\) for lower targets of rank
\(m-q\), and \(U_q\) for upper targets of rank \(m+q\).  Take the full
coordinate orbit of any finite library of decorated base packets and
clear the quota denominators.  All genuine resource classes then have
one common degree \(D\).

For two resource types \(a,b\), of ranks \(s_a,s_b\), and intersection
size \(t\), let

\[
 {\cal S}_{a\to b}(t)
 =\binom{s_a}{t}\binom{2m-s_a}{s_b-t}                 \tag{2.1}
\]

be the physical shell around a fixed first resource.  Let
\(\overline c_{ab}(t)\) be the average number of claimed second base
resources in that shell, conditional on a claimed first base resource.
The coordinate-orbit double count gives the exact identity

\[
 \boxed{
 {d_{ab}(t)\over D}
 ={\overline c_{ab}(t)\over{\cal S}_{a\to b}(t)}.}     \tag{2.2}
\]

This remains true with arbitrarily correlated all-depth quota markings.
Indeed a pair can be claimed only when its first member is claimed, so
the conditional base count can only decrease from the unmarked geometric
count.  Thus it is enough to compute the face-pair census in one cube.

## 3. Owner--owner and owner--target codegrees

Two owners at Johnson distance \(a\) lie in the same packet in
\(\binom ra\) relative positions.  Therefore

\[
 \boxed{
 {d_{00}(m-a)\over D}
 ={\binom ra\over\binom ma^2}.}                       \tag{3.1}
\]

Now fix a lower \(q\)-trace.  It fixes one endpoint on \(r-q\) active
pairs and is empty on the other \(q\).  An owner can disagree with the
fixed endpoints on \(h\) of the \(r-q\) pairs.  There are exactly

\[
 2^q\binom{r-q}{h}                                    \tag{3.2}
\]

such owners.  The corresponding physical shell has size

\[
 \binom{m-q}{h}\binom{m+q}{q+h}.                      \tag{3.3}
\]

Hence

\[
 \boxed{
 {d_{L_q,0}(m-q-h)\over D}
 ={2^q\binom{r-q}{h}\over
   \binom{m-q}{h}\binom{m+q}{q+h}}.}                  \tag{3.4}
\]

Complementation gives the identical formula for \(0,U_q\).  At
\(q=1,h=0\), (3.4) is exactly

\[
                         {2\over m+1}.                 \tag{3.5}
\]

Uniformly for \(q\le H\), all the other terms in (3.4) are
\(O(1/m)\), and the owner--owner maximum in (3.1) is \(r/m^2\).

## 4. Same-sign cross-depth target pairs

Represent a lower affine \(q\)-face by

\[
 (D,a),\qquad |D|=q,\qquad
 a\in\{0,1\}^{[r]\setminus D}.                        \tag{4.1}
\]

Here \(D\) is the set of varied directions.  Fix a first face
\((D,a)\), and let \((E,b)\) be a \(q'\)-face.  Put

\[
 d=|D\setminus E|,\qquad
 e=|E\setminus D|=q'-q+d,                             \tag{4.2}
\]

and let \(h\) be the number of disagreements of \(a,b\) outside
\(D\cup E\).  The number of all affine \(q'\)-faces with these
parameters is exactly

\[
 C_{q,q'}(d,h)
 =\binom qd\binom{r-q}{e}2^d
   \binom{r-q-e}{h}.                                  \tag{4.3}
\]

Their lower traces have intersection

\[
                         t=m-q-e-h,                   \tag{4.4}
\]

so the physical shell is

\[
 S_{--}(q,q';d,h)
 =\binom{m-q}{e+h}\binom{m+q}{d+h}.                   \tag{4.5}
\]

The compiler-selected faces are a subset of all affine faces.  Therefore
the exact orbit codegree satisfies

\[
 \boxed{
 {d_{L_q,L_{q'}}(t)\over D}
 \le {C_{q,q'}(d,h)\over
        S_{--}(q,q';d,h)}.}                           \tag{4.6}
\]

The left side is exactly the marked selected-face pair census divided by
the denominator in (4.5); (4.6) replaces that census by its complete
affine upper bound.  Complementation gives the same formula for two
upper target classes.

There is a useful sharper bound in the potentially largest orbit.
Assume \(q'=q+\delta\).  A deeper lower trace is contained in a shallower
one precisely when \(d=h=0\).  Every affine \(q'\)-face has only

\[
                         2^\delta\binom{q'}q           \tag{4.7}
\]

affine \(q\)-subfaces.  Since the compiler selects exactly \(B\) faces
at each depth, double counting selected containment pairs gives

\[
 \boxed{
 {d_{L_q,L_{q+\delta}}(m-q-\delta)\over D}
 \le
 {2^\delta\binom{q+\delta}{q}\over
  \binom{m-q}{\delta}}.}                              \tag{4.8}
\]

For \(\delta=1\), this is at most

\[
                         {2(q+1)\over m-q}.            \tag{4.9}
\]

The two consecutive \(q\)-subwindows of every selected
\((q+1)\)-window show that the aggregate containment census is at least
\(2B\).  Thus adjacent-depth codegrees genuinely have scale \(1/m\);
they cannot be omitted from the mixed table.

Using (4.3)--(4.8), \(q,q'\le H\le r/4\), and \(r=O(\log m)\), one gets
uniformly

\[
 \max_{q\ne q',t}{d_{L_q,L_{q'}}(t)\over D}
 =O(H/m),                                             \tag{4.10}
\]

while for two distinct targets at one fixed signed depth,

\[
 \max_t{d_{L_q,L_q}(t)\over D}
 =O(Hr/m^2).                                          \tag{4.11}
\]

The same estimates hold on the upper side.

For completeness, (4.10) follows by taking
\(\delta=|q-q'|\).  The term \(d=h=0\) is bounded by (4.8).  Every
positive \(d\) creates two additional physical shell choices and costs
a factor \(O(Hr/m^2)\); every positive \(h\) also creates two shell
choices and costs \(O(r/m^2)\).  The resulting geometric sums are
uniform because \(Hr/m^2=o(1)\).

## 5. Opposite-sign target pairs

Fix a lower \(q\)-face \((D,a)\) and an upper \(q'\)-face \((E,b)\), with
\(d,e,h\) as in (4.2).  Their physical traces have intersection

\[
                         t=m-q-h.                     \tag{5.1}
\]

Different values of \(d\) now belong to the same physical orbit.  The
complete affine count in that orbit is

\[
 C_{-+}(q,q';h)
 =\sum_{\substack{0\le d\le q\\
                  0\le q'-q+d\le r-q}}
   \binom qd\binom{r-q}{q'-q+d}2^d
   \binom{r-q' -d}{h}.                                \tag{5.2}
\]

The physical shell is

\[
 S_{-+}(q,q';h)
 =\binom{m-q}{h}
  \binom{m+q}{q+q'+h}.                                \tag{5.3}
\]

Therefore

\[
 \boxed{
 {d_{L_q,U_{q'}}(m-q-h)\over D}
 \le {C_{-+}(q,q';h)\over S_{-+}(q,q';h)}.}           \tag{5.4}
\]

In the logarithmic range,

\[
 \max_{q,q',h}{d_{L_q,U_{q'}}(m-q-h)\over D}
 =O(r/m^2).                                           \tag{5.5}
\]

Indeed the smallest denominator exponent occurs at
\(q=q'=1,h=0\), where the numerator is \(1+2(r-1)\) and the denominator
is \(\binom{m+1}{2}\).  Increasing either depth adds at least one power
of \(m\), whereas (5.2) adds only powers of \(r\) and \(H\); increasing
\(h\) adds two powers of \(m\).

Equations (3.1), (3.4), (4.6), (4.8), and (5.4) constitute the complete
mixed pair ledger.  They prove (0.4), and (0.3) then proves (0.5).

## 6. Why the static codegree test does not yield a nibble

The degree in a matching theorem must count distinct physical options.
Parallel coordinate-orbit indices do not create new surviving links.
We therefore upper-bound even the richest simple physical catalogue.

Fix an owner \(X\).  The number of physical \(Q_r\) packets containing
\(X\) is

\[
                         D_{m,r}=\binom mr^2r!.        \tag{6.1}
\]

On one packet, a directed 2-factor is specified by choosing at each of
the \(B\) owners one of its \(r\) cube neighbors.  Ignoring bijectivity
only enlarges the count, so there are at most

\[
                         r^B                           \tag{6.2}
\]

factor decorations.  By (1.2), a quota mark at one signed depth is
either all \(B\) traces or all but one, giving at most \(B+1\) choices.
Across all signed depths there are at most

\[
                         (B+1)^{2H}                    \tag{6.3}
\]

joint marks.  Multiplication proves (0.6).

Now assume \(H\asymp r\asymp\log m\).  Since \(B=m^{\alpha+o(1)}\),

\[
\begin{aligned}
 \log D_{\rm phys}
 &\le O(r\log m)+B\log r+2H\log(B+1)\\
 &=O((\log m)^2+B\log\log m),                         \tag{6.4}\\
 K&=\Theta(B\log m).
\end{aligned}
\]

Thus (0.7) follows.

Let \(R_z\) be a product residual on the disjoint union of all owner and
typed target resources.  Conditional on retaining a fixed middle owner
\(v\), a physical augmented edge through \(v\) survives only if its
other \(K-1\) resources survive.  Hence

\[
 {\mathbb E}\bigl[d_{R_z}(v)\mid v\in R_z\bigr]
 \le D_{\rm phys}z^{K-1}.                             \tag{6.5}
\]

For fixed \(z<1\), (6.4) makes the logarithm of (6.5)

\[
 o(K)+(K-1)\log z=-\Omega(K).                         \tag{6.6}
\]

Markov's inequality proves (0.8).  If \(z=1-\theta\) with
\(\theta=o(1)\), the same proof works provided

\[
 \theta BH\gg B\log r+(\log m)^2,
\]

which is (0.9).

This local statement is compatible with global survival.  Even one
option per raw packet gives

\[
 |{\cal E}|={W D_{m,r}\over B},
\]

and therefore

\[
 \log\bigl(|{\cal E}|z^K\bigr)
 =\Theta(m)-O(K)=\Theta(m)                            \tag{6.7}
\]

for fixed \(z<1\), because \(K=m^{\alpha+o(1)}=o(m)\).
So the expected total number of surviving edges is exponential, while
the expected link of a typical retained middle owner is \(o(1)\).

## 7. Exact boundary of the pilot

The following are proved.

1. Frozen four-block product cells remain impossible at Gaussian depth
   by their exact source-capacity ratio.  The present pilot necessarily
   uses moving packet frames.
2. All owner--owner, owner--target, same-sign cross-depth, and
   opposite-sign target codegrees have the exact orbit formulae and
   affine bounds in Sections 3--5.
3. In the logarithmic range the true static parameter satisfies
   \(K\Delta _2/D=o(1)\).
4. The full simple physical catalogue has
   \(\log D_{\rm phys}=o(K)\), so every product-like positive-density
   residual has empty links at almost every retained middle owner.

The following are not proved.

1. A \(c\log m\) simultaneous-band colored packet matching.
2. A one-shot edge-coloring theorem with sufficiently strong dependence
   on \(K,\Delta _2/D\) and no product-residual conclusion.
3. A packet-closed absorber or a structured resolution preserving all
   signed-depth quotas.

Thus the logarithmic pilot passes the complete static mixed-codegree
test but fails the hereditary residual test needed by a standard
iterated nibble.  The next valid positive route is a structured
near-resolution followed by absorption inside packet-closed reservoirs,
not a citation based only on \(K\Delta _2/D=o(1)\).
