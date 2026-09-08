# Macroscopic nonoverlap strip carriers: sharpness of quotient-edge collision

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, solver, or external input

## 0. Result

The phase-independent corner edge from
`MATH_AUDIT_OCR_CRITICAL_CORNER_QUOTIENT_PACKING_20260725.md` collapses
all phase-pair multiplicity for one fixed strip carrier.  It does **not**
extend to a deterministic collision theorem between different strip
carriers, even after one imposes all of the following simultaneously:

1. a genuine first zero-winding PBBS return;
2. duration of Gaussian order;
3. a macroscopic two-phase nonoverlap corridor; and
4. all intermediate three-phase constraints.

Here is an exact family proving this sharpness.  Fix integers

\[
 q\ge2,\qquad m\ge5q,
 \qquad n=m-5q,
 \tag{0.1}
\]

and put

\[
 s=3q,\qquad K=2q,\qquad t=q-1,\qquad u=2q.
 \tag{0.2}
\]

Let \(\mathcal Y_{q,n}\) be the set of walks \(Y:0\to K\), of length
\(K+2n\), confined to \([0,K]\), and write

\[
 a_{q,n}=|\mathcal Y_{q,n}|.
 \tag{0.3}
\]

Every \(Y\in\mathcal Y_{q,n}\) gives one of the audited genuine corner
returns.  Inside that return, the phases

\[
 a=q,\qquad b=2q-1
 \tag{0.4}
\]

are in the nonoverlap branch with the unique common corridor

\[
 \boxed{Z_Y=0^{2q}Y0^{2q}.}
 \tag{0.5}
\]

It has

\[
 \operatorname {net}(Z_Y)=-2q,
 \qquad |Z_Y|=2m-4q,
 \tag{0.6}
\]

and every intermediate phase \(q\le v\le2q-1\) merely refactors this
same word.  Thus the common corridor has height \(2q=2s/3\), while the
interval of transported phases has order \(q\).

Let \(\Pi^{\rm strip}_{m,q}\) be the maximum quotient-edge-disjoint
subfamily of these returns after requiring their quotient supports to be
nonwrapping.  Let

\[
 \Xi_m(h)=\#\{D\in\mathcal D_m:
                 \text{the \(\tau\)-cycle of \(D\) has length at most }h\}.
 \tag{0.7}
\]

Then

\[
 \boxed{
 {\bigl(a_{q,n}-\Xi_m(3q+2)\bigr)_+\over(3q+2)^2}
 \le \Pi^{\rm strip}_{m,q}
 \le a_{q,n}
 \le2^{2m-8q}.}
 \tag{0.8}
\]

Moreover, fix a sufficiently small constant \(\gamma>0\), and take

\[
 q=\lfloor\gamma\sqrt m\rfloor.
 \tag{0.9}
\]

There is a constant \(c_\gamma>0\) such that, for all sufficiently large
\(m\),

\[
 \boxed{
 c_\gamma {2^{2m-8q}\over q^5}
 \le \Pi^{\rm strip}_{m,q}
 \le2^{2m-8q}.}
 \tag{0.10}
\]

Thus this genuine Gaussian nonoverlap family contains exponentially many
pairwise quotient-edge-disjoint return supports.  In particular, no
universal assertion that two different nonoverlap carriers must share a
quotient edge can be true.

At the same time, with \(B_m=\operatorname {Cat}_m\),

\[
 \boxed{
 {\Pi^{\rm strip}_{m,q}\over B_m/\sqrt m}
 \le (\sqrt\pi+o(1))m^2 2^{-8q}
 \longrightarrow0.}
 \tag{0.11}
\]

Therefore this is a sharp obstruction to **deterministic cross-carrier
collision**, not a counterexample to coefficient one.  A successful
theorem must be an aggregate shifted-incidence estimate for
support-separated carriers; the exact common corner only removes the
phase-pair multiplicity attached to one fixed carrier.

## 1. The exact genuine return family

Fix \(Y\in\mathcal Y_{q,n}\), and put

\[
 \overline T=0^{2q}Y,
 \qquad S=Y0^{2q},
 \qquad L=|\overline T|=|S|=4q+2n=2m-6q.
 \tag{1.1}
\]

Here \(T\) denotes the bit-complement of \(\overline T\), in the usual
dual-block notation.

The literal identity

\[
 \overline T0^{2q}=0^{2q}S
 \tag{1.2}
\]

is the exceptional block rotation.  The specialized roots from the
audited corner construction are

\[
 D_j
 =1^{2q+j}0^{2q}Y1^{q-j}0^{3q}
 \qquad(0\le j\le q-1),
 \tag{1.3}
\]

\[
 D_{q-1+k}
 =1^{3q}0^{2q+k-1}Y0^{3q-k+1}
 \qquad(1\le k\le q+1),
 \tag{1.4}
\]

and

\[
 D_{2q+k}
 =1^{k-1}Y0^{2q}1^{3q-k+1}0^{3q}
 \qquad(1\le k\le q+1).
 \tag{1.5}
\]

They have length \(2m\), and the canonical first-maximum block rotation,
using (1.2) at the exceptional phase, gives

\[
 \tau D_j=D_{j+1}\qquad(0\le j\le3q).
 \tag{1.6}
\]

The cap checks are visible directly.  In (1.3), the walk \(Y\) is read
from height \(j\) and stays below \(j+2q<3q\); the following ones first
reach height \(3q\).  In (1.4), the initial mountain reaches height
\(3q\), and the translated copy of \(Y\) stays in \([0,3q]\).  In
(1.5), \(Y\) is read from height \(k-1\) and reaches at most
\(2q+k-1\le3q\).  Hence every displayed word is Dyck of height exactly
\(3q\).

Only the staircase blocks

\[
 T_{q-1}=T,
 \qquad S_{2q}=S
 \tag{1.7}
\]

are nonempty among \(T_0,\ldots,T_{3q-1}\) and
\(S_0,\ldots,S_{3q-1}\).  Their common length is \(L\).

For completeness, the first-return chronology is exact.  Put

\[
 c_j=|S_j|+1.
\]

Then \(c_j=1\) except for \(c_{2q}=L+1\), and the first-maximum positions
are

\[
 \delta(D_j)=
 \begin{cases}
  3q+L,&0\le j\le q-1,\\
  3q,&q\le j\le2q,\\
  3q+L,&2q+1\le j\le3q.
 \end{cases}
 \tag{1.8}
\]

The accumulated deficit before phase \(j\) is

\[
 C_j=\sum_{i<j}c_i
 =\begin{cases}
   j,&j\le2q,\\
   j+L,&j\ge2q+1.
  \end{cases}
 \tag{1.9}
\]

Thus \(C_j<\delta(D_j)\) for every \(1\le j<3q\), while

\[
 C_{3q}=3q+L=\delta(D_{3q})<2m+1.
 \tag{1.10}
\]

This proves that (1.3)--(1.6) give a genuine **first** return and that its
winding is zero.  Its endpoint overlap excess is

\[
 \boxed{
 \Lambda=\delta(D_0)+\delta(D_{3q})-2m=L.}
 \tag{1.11}
\]

## 2. A macroscopic internal nonoverlap corridor

Use the canonical factorization

\[
 D_j=P_j1R_j0S_j.
\]

For the middle roots (1.4), the terminal words are

\[
 R_{q-1+k}=0^{k-1}\overline T0^{3q-k}
 \qquad(1\le k\le q+1).
 \tag{2.1}
\]

At the phases \(a=q\) and \(b=2q-1\), this gives

\[
 R_a=\overline T0^{3q-1},
 \qquad
 R_b=0^{q-1}\overline T0^{2q}.
 \tag{2.2}
\]

All \(T_j,S_j\) strictly between these phases are empty.  Therefore the
two transported collars are

\[
 A_{a,b}=C_{a,b}=0^{q-1}.
 \tag{2.3}
\]

Define

\[
 Z_Y=\overline T0^{2q}=0^{2q}Y0^{2q}.
 \tag{2.4}
\]

Equations (2.2)--(2.4) give the literal nonoverlap factorization

\[
 \boxed{
 R_b=A_{a,b}Z_Y,
 \qquad
 R_a=Z_YC_{a,b}.}
 \tag{2.5}
\]

The phase separation is \(b-a=q-1\), so the transported corridor height
is

\[
 3q-(q-1)-1=2q.
 \tag{2.6}
\]

This agrees with (0.5)--(0.6).

The same conclusion follows from the exact outer ledger.  There are
\(2q\) omitted outer phases.  Both exceptional blocks in (1.7) lie
outside \([a,b]\), so

\[
 B_{a,b}=2q+2L.
 \tag{2.7}
\]

Together with \(\Lambda=L\), this gives

\[
 \Delta=B_{a,b}-\Lambda=2q+L=|Z_Y|>0,
 \tag{2.8}
\]

which is exactly the nonoverlap branch.

For every intermediate phase \(a\le v\le b\), (2.1) also gives

\[
 \boxed{
 R_v=0^{v-a}Z_Y0^{b-v}.}
 \tag{2.9}
\]

Hence every internal third phase is a refactorization of the same word;
there is no additional condition on \(Y\).

## 3. What the common corner does and does not identify

The full quotient support of this return is

\[
 Q(Y)=\{e_{D_0(Y)},e_{D_1(Y)},\ldots,e_{D_{3q+1}(Y)}\}.
 \tag{3.1}
\]

It contains \(3q+2\) edges when the quotient cycle is longer than this
support.  At phase \(a=q\), formula (1.4) with \(k=1\) gives the audited
corner

\[
 \boxed{C_Y=D_q(Y)=1^{3q}0^{2q}Y0^{3q}.}
 \tag{3.2}
\]

Every path \(Y:0\to2q\) in the strip begins and ends with a one.  Thus
the initial one-run, the following zero-run, and the terminal zero-run in
(3.2) have exact lengths \(3q,2q,3q\), respectively.  Consequently

\[
 C_Y=C_{Y'}\quad\Longrightarrow\quad Y=Y'.
 \tag{3.3}
\]

For fixed \(Y\), the common-corner theorem says that all admissible
phase-pair descriptions collide at \(e_{C_Y}\).  Equation (3.3) shows why
that theorem supplies no collision between two different carrier words.
The next section proves that this is not merely a failure of the chosen
charge: exponentially many different carriers can have their **entire**
supports selected disjointly.

## 4. Conflict degree and nonwrapping deletion

For each fixed support phase \(0\le j\le3q+1\), the map

\[
 Y\longmapsto D_j(Y)
 \tag{4.1}
\]

is injective.  Indeed, in each of the literal formulas (1.3)--(1.5), the
position and length of the displayed \(Y\)-substring are fixed once
\(j,m,q\) are fixed, so that substring recovers \(Y\).

It follows that any one quotient edge belongs to at most \(3q+2\) of the
supports (3.1): for each possible phase index \(j\), there is at most one
carrier \(Y\) producing that edge at phase \(j\).

Discard every \(Y\) for which \(D_0(Y)\) belongs to a \(\tau\)-cycle of
length at most \(3q+2\).  The map \(Y\mapsto D_0(Y)\) is injective, so at
most \(\Xi_m(3q+2)\) carriers are discarded.  Every remaining support is
nonwrapping and has \(3q+2\) distinct edges.

Make a conflict graph on the remaining carriers, joining two carriers
when their supports share an edge.  One support has \(3q+2\) edges, and
each such edge lies in at most \(3q+1\) other supports.  Hence the maximum
degree is at most

\[
 (3q+2)(3q+1).
 \tag{4.2}
\]

The greedy independent-set bound therefore gives

\[
 \Pi^{\rm strip}_{m,q}
 \ge
 {a_{q,n}-\Xi_m(3q+2)
  \over (3q+2)(3q+1)+1}
 \ge
 {a_{q,n}-\Xi_m(3q+2)\over(3q+2)^2},
 \tag{4.3}
\]

with positive parts understood.  This proves the lower bound in (0.8).

The exact short-cycle coding theorem from the residence-packing reduction
gives, harmlessly enlarging its parameter by one if necessary,

\[
 \boxed{
 \Xi_m(3q+2)
 \le (6q+6)(2m+1)^{6q+6}.}
 \tag{4.4}
\]

Only its logarithmic consequence will be used:

\[
 \log\Xi_m(3q+2)=O(q\log m).
 \tag{4.5}
\]

Finally, (3.3) maps every edge-disjoint selected interval injectively to
its carrier path, so \(\Pi^{\rm strip}_{m,q}\le a_{q,n}\).  Since a path
is a binary word of length

\[
 K+2n=2m-8q,
 \tag{4.6}
\]

one has \(a_{q,n}\le2^{2m-8q}\).  This completes (0.8).

## 5. Spectral lower bound for the strip carriers

Put

\[
 K=2q,
 \qquad \ell=K+2n=2m-8q,
 \qquad \theta={\pi\over K+2}.
 \tag{5.1}
\]

The number \(a_{q,n}\) is the \((0,K)\) entry of the \(\ell\)-th power
of the adjacency matrix of the path graph on
\(\{0,1,\ldots,K\}\).  Its exact spectral expansion is

\[
 a_{q,n}
 ={2\over K+2}
 \sum_{j=1}^{K+1}
 (-1)^{j+1}\sin^2(j\theta)
 \bigl(2\cos(j\theta)\bigr)^\ell.
 \tag{5.2}
\]

Both \(K\) and \(\ell\) are even.  Pairing the eigenvalues with indices
\(j\) and \(K+2-j\), and discarding the zero central eigenvalue, gives

\[
 a_{q,n}
 ={4\over K+2}
 \sum_{j=1}^{K/2}
 (-1)^{j+1}\sin^2(j\theta)
 \bigl(2\cos(j\theta)\bigr)^\ell.
 \tag{5.3}
\]

For \(2\le j\le K/2\),

\[
 {\sin^2(j\theta)\over\sin^2\theta}\le j^2,
 \tag{5.4}
\]

and

\[
 \begin{aligned}
 \log{\cos(j\theta)\over\cos\theta}
 &=-\int_\theta^{j\theta}\tan x\,dx\\
 &\le-\int_\theta^{j\theta}x\,dx
 =-{(j^2-1)\theta^2\over2}.
 \end{aligned}
 \tag{5.5}
\]

Therefore the absolute value of all terms after the first, divided by the
first term, is at most

\[
 \sum_{j=2}^{\infty}
 j^2\exp\!\left(-{\ell\theta^2\over2}(j^2-1)\right).
 \tag{5.6}
\]

Take \(q=\lfloor\gamma\sqrt m\rfloor\), where \(\gamma>0\) is fixed
and sufficiently small.  Then

\[
 \ell\theta^2\longrightarrow {\pi^2\over2\gamma^2}.
 \tag{5.7}
\]

Choose \(\gamma\) so that the sum in (5.6) is at most \(1/2\) for all
sufficiently large \(m\).  Equations (5.3)--(5.6) then give

\[
 a_{q,n}
 \ge {2\over K+2}\sin^2\theta
       \bigl(2\cos\theta\bigr)^\ell.
 \tag{5.8}
\]

For large \(m\), \(\theta\le1/2\), and the elementary inequalities

\[
 \sin\theta\ge {2\theta\over\pi}={2\over K+2},
 \qquad
 \cos\theta\ge e^{-\theta^2}
 \tag{5.9}
\]

apply.  Since \(\ell\theta^2=O_\gamma(1)\), (5.8)--(5.9) imply

\[
 \boxed{
 a_{q,n}\ge c_\gamma {2^{2m-8q}\over q^3}.}
 \tag{5.10}
\]

On the other hand, (4.4) gives

\[
 \log\Xi_m(3q+2)=O_\gamma(\sqrt m\log m),
 \tag{5.11}
\]

whereas (5.10) gives

\[
 \log a_{q,n}
 \ge (2m-8q)\log2-O_\gamma(\log m).
 \tag{5.12}
\]

Thus \(\Xi_m(3q+2)=o(a_{q,n})\).  Substituting (5.10) in (4.3), and
using \(3q+2=\Theta(q)\), proves the lower bound in (0.10).

## 6. Exact asymptotic boundary

The lower and upper bounds in (0.10) show that

\[
 \log\Pi^{\rm strip}_{m,q}
 =(2m-8q)\log2+O_\gamma(\log m).
 \tag{6.1}
\]

Thus deterministic cross-carrier collision fails on a family with the
full exponential scale allowed by its literal collars.

Those collars are nevertheless fatal at the coefficient-one scale.  The
Catalan asymptotic is

\[
 B_m
 ={4^m\over\sqrt\pi\,m^{3/2}}(1+o(1)),
 \tag{6.2}
\]

so (0.8) gives

\[
 \begin{aligned}
 {\Pi^{\rm strip}_{m,q}\over B_m/\sqrt m}
 &\le
 {2^{2m-8q}\over4^m/(\sqrt\pi\,m^2)(1+o(1))}\\
 &=(\sqrt\pi+o(1))m^2 2^{-8q}.
 \end{aligned}
 \tag{6.3}
\]

For \(q=\gamma\sqrt m+O(1)\), the last expression is

\[
 \exp\bigl(-8\gamma(\log2)\sqrt m+O(\log m)\bigr)=o(1).
 \tag{6.4}
\]

This proves (0.11).

## 7. Proved and residual boundary

The theorem proves exactly the following.

1. The audited corner construction contains a macroscopic **nonoverlap**
   chart, even though the original exceptional phase pair lies in the
   overlap branch.
2. Every internal third phase in that chart telescopes into the same word
   \(Z_Y\).
3. The phase-independent edge \(e_{C_Y}\) collapses every phase-pair
   description at fixed \(Y\), but different carriers have different
   corner edges.
4. After short-cycle deletion, exponentially many different carriers can
   be selected with their complete quotient supports pairwise disjoint.
5. The whole family is nevertheless exponentially smaller than
   \(B_m/\sqrt m\).

Consequently the general aligned-support collision theorem is best
possible as a deterministic statement.  A noncommuting constraint cannot
come from another phase of the same return, and one cannot force two
different carriers to align at a quotient edge.  The exact surviving
object is therefore the support-separated shifted intersection of two
genuine return languages, linked by exterior re-canonicalization under
\(\tau^g\), as isolated in
`MATH_ATTACK_OCR_FINITE_PHASE_TELESCOPE_AND_CROSS_INTERVAL_RESIDUAL_20260725.md`.

No little-oh theorem for that aggregate shifted incidence is proved here,
and no coefficient-one conclusion is claimed.
