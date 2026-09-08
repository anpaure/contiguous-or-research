# The hashed three-seed \(B_4\) atlas: exact physical tag-Walsh Gram and the remaining covariance

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The three relabelled cyclic \(B_4\) seeds have a genuine negative local
simplex covariance. If \(a_c\) is the indicator of the four middle states
used by seed \(c\in\mathbb Z_3\), then

\[
 \left\langle a_c-\frac23{\bf1},a_d-\frac23{\bf1}\right\rangle
 =
 \begin{cases}
  4/3,&c=d,\\
 -2/3,&c\ne d.
 \end{cases}                                                       \tag{0.1}
\]

Thus a collision-weighted ternary cut really could create negative
cross-packet covariance.

The deterministic anchor hash in
MATH_THEOREM_HASHED_THREE_SEED_B4_FRAME_DIFFUSION_20260726.md does not,
by itself, prove that this happens. The anchor subset is frozen by every
packet and is literally present in every shallow lower and upper target.
Consequently the physical target Hilbert space and the physical Gram
operator split as orthogonal direct sums over exact anchor tags.
Equidistribution of seed vectors between different anchor tags therefore
realizes an average of independent tagged problems; it is not a negative
cross-tag covariance.

For a fixed anchor-cardinality layer, let \(\mu_q^{\theta,\pm}\) be the
complete physical target load of the outside first-eligible factor when
the common seed vector is \(\theta\in\mathbb Z_3^r\). Define

\[
 \widehat\mu_{q,\gamma}^{\pm}
 =3^{-r}\sum_{\theta\in\mathbb Z_3^r}
       \overline{\chi_\gamma(\theta)}\,\mu_q^{\theta,\pm}.          \tag{0.2}
\]

Then the exact context-averaged Gram identity is

\[
 \boxed{
 3^{-r}\sum_\theta
 \left\|\mu_q^{\theta,\pm}
       -\frac{W_k}{N_{k,q}^{\pm}}{\bf1}\right\|_2^2
 =
 \left\|\widehat\mu_{q,0}^{\pm}
       -\frac{W_k}{N_{k,q}^{\pm}}{\bf1}\right\|_2^2
 +\sum_{\gamma\ne0}
       \|\widehat\mu_{q,\gamma}^{\pm}\|_2^2.}                       \tag{0.3}
\]

Here \(W_k\) is the number of starts and \(N_{k,q}^{\pm}\) the number of
signed targets in one anchor sector of cardinality \(k\), up to the
exponentially small scan leave.

The second term in (0.3) is nonnegative. When it is expanded packet by
packet, coefficient one requires negative cross-packet terms of order
\(W\) to cancel the extensive packet self-energy. Neither uniform
fixed-frame diffusion nor packetwise trace-rainbow injectivity estimates
those cross terms.

Accordingly:

* the hashed atlas removes every single-fixed-frame Gaussian cut;
* the actual recursive factor removes every within-packet collision;
* the deterministic context array supplies the exact Walsh average
  (0.3);
* it does **not** yet supply the order-\(W\) negative cross-packet
  covariance needed for \(o(W)\) holes.

The exact remaining condition is displayed in (6.7) below. This is not a
statewise impossibility theorem for the hashed atlas. It says that the
present deterministic array theorem is a one-point/frame theorem, while
the still-unproved assertion is a collision-conditioned physical
two-point theorem.

## 1. The three literal seeds and their local Fourier symbol

Put

\[
\begin{aligned}
 M_0&=12\mid34,&
 \mathcal A_0&=\{13,14,23,24\},\\
 M_1&=13\mid24,&
 \mathcal A_1&=\{12,14,23,34\},\\
 M_2&=14\mid23,&
 \mathcal A_2&=\{12,13,24,34\}.
\end{aligned}                                                       \tag{1.1}
\]

Use the oriented cycles

\[
\begin{aligned}
 C_0&=(13,14,24,23),\\
 C_1&=(14,12,23,34),\\
 C_2&=(12,13,34,24).
\end{aligned}                                                       \tag{1.2}
\]

For an edge \(X\to Y\), its lower port is \(X\cap Y\), and its upper port
is \(X\cup Y\). In all three cycles the lower ports are the four
singletons and the upper ports are the four triples, each exactly once.
Seed \(c\) pairs a lower singleton \(i\) with the upper triple missing
the mate of \(i\) in \(M_c\). Hence the three port bijections are exactly
the three fixed-point-free involutions of \([4]\).

Let \(a_c={\bf1}_{\mathcal A_c}\in\mathbb R^{\binom{[4]}2}\). Every
two-set belongs to exactly two of the three orientation squares, and two
distinct squares intersect in two states. Therefore

\[
 a_0+a_1+a_2=2{\bf1},\qquad
 \langle a_c,a_d\rangle=
 \begin{cases}4,&c=d,\\2,&c\ne d.\end{cases}                       \tag{1.3}
\]

Putting \(b_c=a_c-\frac23{\bf1}\) proves (0.1). Equivalently, the
untouched-state Gram matrix is

\[
 H_0=(|\mathcal A_c\cap\mathcal A_d|)_{c,d}
 =
 \begin{pmatrix}4&2&2\\2&4&2\\2&2&4\end{pmatrix}
 =2I+2J.                                                          \tag{1.4}
\]

Its ternary Fourier eigenvalues are \(8,2,2\). After centering, the
constant eigenvalue becomes zero and the two nonconstant eigenvalues
remain \(2\).

On a touched block the complete lower image is the set of all four
singletons for every seed, and the complete upper image is the set of all
four triples for every seed. Thus the touched-image Gram is

\[
 H_1=4J,                                                          \tag{1.5}
\]

with Fourier eigenvalues \(12,0,0\). Seed drift lives on the untouched
rank-two trace and on the owner-resolved permutation of the touched
ports; it is not visible in the touched-port marginal.

For two aligned product charts with a common set \(J\) of \(q\) touched
blocks, complete local-phase summation gives the exact overlap

\[
 \langle Z_{\theta,J},Z_{\eta,J}\rangle
 =
 4^q\prod_{i\notin J}|\mathcal A_{\theta_i}
                         \cap\mathcal A_{\eta_i}|.
                                                                    \tag{1.6}
\]

In particular, if \(d_{\bar J}(\theta,\eta)\) is their Hamming distance
on the untouched positions, then

\[
 \frac{\langle Z_{\theta,J},Z_{\eta,J}\rangle}{4^r}
 =2^{-d_{\bar J}(\theta,\eta)}.                                  \tag{1.7}
\]

The recursive trace-rainbow factor uses only a subset of the complete
product traces at a prescribed support, but every literal equality still
obeys the local restrictions used in (1.6). Thus (1.6) is also an upper
kernel for its aligned physical packet images.

## 2. The actual packet and its physical tags

Let \(A\) be the frozen anchor, and write

\[
 u=X\cap A,\qquad \theta(u)=\vartheta(u)\in\mathbb Z_3^r.          \tag{2.1}
\]

The sequential scan selects indices \(I(P)=(i_1,\ldots,i_r)\) and freezes
every skipped block, the blocks after \(i_r\), and the remainder. A packet
tag is therefore

\[
 P=(u,I,c),                                                       \tag{2.2}
\]

where \(c\) is the complete frozen outside context. Its abstract owner
phase is \(x\in Q_{2r}\). The two abstract directions at slot \(j\) are
embedded as the two pair flips of \(M_{\theta_j(u)}\) in \(B_{i_j}\).

Let \(F_P\) be the installed recursive factor. For \(q\le r\), its
dyadic balance law gives a set \(J_q(P,x)\subseteq[r]\) of \(q\) distinct
local slots touched by the window. Write

\[
 \Phi_{P,q}^{u,\pm}(x)\in\mathcal T_q^\pm                         \tag{2.3}
\]

for the literal lower or upper target. On a selected block it is the
local middle state if the slot is untouched and the corresponding
singleton/triple port if it is touched; on every frozen block it is the
frozen state \(c\). Most importantly,

\[
 \Phi_{P,q}^{u,\pm}(x)\cap A=u.                                   \tag{2.4}
\]

Define the physical incidence operator

\[
 A_{P,q}^{u,\pm}(T,x)
 ={\bf1}\{\Phi_{P,q}^{u,\pm}(x)=T\}.                              \tag{2.5}
\]

The recursive trace-rainbow theorem says that every individual packet
image

\[
 Z_{P,q}^{u,\pm}:=A_{P,q}^{u,\pm}{\bf1}                           \tag{2.6}
\]

is a zero-one vector. It makes no assertion that images of two different
packets are disjoint.

## 3. Exact physical tag-Gram operator

For two tagged packet starts define

\[
\begin{aligned}
 K_{P,P',q}^{u,v,\pm}(x,y)
 &:=
 \left((A_{P,q}^{u,\pm})^*A_{P',q}^{v,\pm}\right)(x,y)\\
 &={\bf1}\{\Phi_{P,q}^{u,\pm}(x)
             =\Phi_{P',q}^{v,\pm}(y)\}.                            \tag{3.1}
\end{aligned}
\]

Equation (2.4) gives the exact block law

\[
 \boxed{
 K_{P,P',q}^{u,v,\pm}=0\quad\text{when }u\ne v.}                   \tag{3.2}
\]

Let

\[
 A_{u,q}^{\pm}=[A_{P,q}^{u,\pm}]_{P\in\mathscr P_u}.
\]

Then the complete physical Gram, including every cross-packet collision,
is

\[
 \boxed{
 \mathcal K_q^\pm
 =(A_q^\pm)^*A_q^\pm
 =\bigoplus_{u\subseteq A}
       (A_{u,q}^{\pm})^*A_{u,q}^{\pm}.}                            \tag{3.3}
\]

This is the first indispensable correction to an untagged seed census.
The hash is balanced after summing different \(u\)'s, but those \(u\)'s
belong to orthogonal physical target spaces.

There are further packet tags in \(c\). They cannot simply be discarded:
if two packets freeze a common physical block differently, that block
already makes their Gram entry zero. If a block is frozen in one packet
and selected in the other, equality is governed by the corresponding
active-versus-frozen incidence table. Formula (3.1), not an untagged
direction word, retains all of these cases.

## 4. Ternary Walsh form

It is useful first to work with a formal common catalogue containing all
seed vectors \(\theta\in\Theta=\mathbb Z_3^r\). Illegal scan histories
may be included with zero incidence; this avoids assuming that the packet
partitions for two seed vectors have the same owner sets.

For a fixed anchor-cardinality layer \(k\), delete the frozen anchor
coordinates and identify all anchor sectors of size \(k\) with one common
outside target space. Let

\[
 \mu_{k,q}^{\theta,\pm}
\]

be the complete outside load of the sequential first-eligible factor with
seed vector \(\theta\). Its Fourier transform is

\[
 \widehat\mu_{k,q,\gamma}^{\pm}
 =3^{-r}\sum_{\theta\in\Theta}
      \overline{\chi_\gamma(\theta)}
      \mu_{k,q}^{\theta,\pm},\qquad
 \chi_\gamma(\theta)=
 e^{2\pi i\langle\gamma,\theta\rangle/3}.                         \tag{4.1}
\]

Fourier inversion gives

\[
 \mu_{k,q}^{\theta,\pm}
 =\sum_{\gamma\in\Theta}
       \chi_\gamma(\theta)\widehat\mu_{k,q,\gamma}^{\pm}.          \tag{4.2}
\]

The exact load Gram is therefore

\[
 \boxed{
 \left\langle\mu_{k,q}^{\theta,\pm},
                 \mu_{k,q}^{\eta,\pm}\right\rangle
 =
 \sum_{\gamma,\delta}
  \chi_\gamma(\theta)\overline{\chi_\delta(\eta)}
  \left\langle\widehat\mu_{k,q,\gamma}^{\pm},
                 \widehat\mu_{k,q,\delta}^{\pm}\right\rangle.}    \tag{4.3}
\]

At the owner-resolved level, replace each \(\mu\) by the incidence
operator \(A\). The corresponding physical tag-Walsh Gram block is

\[
 \widehat{\mathcal K}_{k,q}^{\pm}(\gamma,\delta)
 =
 3^{-2r}\sum_{\theta,\eta}
  \overline{\chi_\gamma(\theta)}\chi_\delta(\eta)
 (A_{k,q}^{\theta,\pm})^*A_{k,q}^{\eta,\pm}.                       \tag{4.4}
\]

Equations (3.3) and (4.4) are the exact requested operator: (4.4)
resolves the three-seed modes, while (3.3) restores the literal anchor
tag which the seed census forgets.

## 5. What the deterministic hash actually averages

Fix \(k\). Every anchor subset \(u\in\binom Ak\) has the same number

\[
 W_k=\binom{2m-|A|}{m-k}                                         \tag{5.1}
\]

of middle completions before the exponentially small scan leave. Its
lower and upper target sectors have respective sizes

\[
 N_{k,q}^-=\binom{2m-|A|}{m-q-k},\qquad
 N_{k,q}^+=\binom{2m-|A|}{m+q-k}.                                \tag{5.2}
\]

Thus the layerwise equitable hash really does assign, up to its
exponentially small rounding error, equally many mutually orthogonal
anchor sectors to every \(\theta\in\Theta\).

For either sign, write

\[
 W_k=c_{k,q}^\pm N_{k,q}^\pm+\rho_{k,q}^\pm,\qquad
 \xi_{k,q}^\pm=\rho_{k,q}^\pm/N_{k,q}^\pm.                        \tag{5.3}
\]

The integral balanced collision excess in one sector is

\[
 \Delta_{k,q}^{\theta,\pm}
 =\frac12\left(
   \left\|\mu_{k,q}^{\theta,\pm}
       -\frac{W_k}{N_{k,q}^\pm}{\bf1}\right\|_2^2
   -N_{k,q}^\pm\xi_{k,q}^\pm(1-\xi_{k,q}^\pm)\right).             \tag{5.4}
\]

Parseval applied to (4.2) proves

\[
\boxed{
\begin{aligned}
 2\,3^{-r}\sum_{\theta}\Delta_{k,q}^{\theta,\pm}
 ={}&
 \left\|\widehat\mu_{k,q,0}^{\pm}
       -\frac{W_k}{N_{k,q}^\pm}{\bf1}\right\|_2^2\\
 &+\sum_{\gamma\ne0}
       \|\widehat\mu_{k,q,\gamma}^{\pm}\|_2^2
 -N_{k,q}^\pm\xi_{k,q}^\pm(1-\xi_{k,q}^\pm).
                                                                    \tag{5.5}
\end{aligned}}
\]

The deterministic anchor array realizes the left side of (5.5), summed
over \(k\), modulo the equitable-partition and scan errors. For the
mesoscopic choice \(r\gg q\log m\), those errors remain \(o(W)\): a
depth-\(q\) target has at most
\(\binom{m+q}{q}=\exp(O(q\log m))=\exp(o(r))\) middle extensions,
whereas the anchor discrepancy is \(\exp(-\Omega(r))\).

Formula (5.5) is not negative covariance. It is the exact nonnegative
Fourier energy which a covariance theorem must subsequently control.

## 6. Packet expansion and the missing order-\(W\) term

Use the common zero-padded packet catalogue from Section 4 and write

\[
 \mu_{k,q}^{\theta,\pm}
 =\sum_P Z_{P,k,q}^{\theta,\pm}.                                  \tag{6.1}
\]

Fourier transforming packetwise gives

\[
 \widehat\mu_{k,q,\gamma}^{\pm}
 =\sum_P\widehat Z_{P,k,q,\gamma}^{\pm}.                          \tag{6.2}
\]

Therefore

\[
\boxed{
\begin{aligned}
 \sum_{\gamma\ne0}\|\widehat\mu_{k,q,\gamma}^{\pm}\|_2^2
 ={}&
 \sum_P\sum_{\gamma\ne0}
       \|\widehat Z_{P,k,q,\gamma}^{\pm}\|_2^2\\
 &+2\operatorname {Re}\sum_{P<P'}\sum_{\gamma\ne0}
   \left\langle\widehat Z_{P,k,q,\gamma}^{\pm},
                 \widehat Z_{P',k,q,\gamma}^{\pm}\right\rangle.
                                                                    \tag{6.3}
\end{aligned}}
\]

The first line is packet self-energy. The second is the physical
cross-packet covariance. It is the only possible source of cancellation.

The local seed symbol shows that the self-energy is not negligible. For
one aligned carrier packet of size \(S=4^r\), choose two seed vectors
\(\theta,\eta\) independently and uniformly. If a common target uses
the same \(q\) touched slots, (1.6) and

\[
 \mathbb E_{c,d}|\mathcal A_c\cap\mathcal A_d|
 =\frac13\,4+\frac23\,2=\frac83                                  \tag{6.4}
\]

give

\[
 \mathbb E_{\theta,\eta}
 \langle Z_{P,q}^{\theta,\pm},Z_{P,q}^{\eta,\pm}\rangle
 \le
 4^q(8/3)^{r-q}
 =S(2/3)^{r-q}.                                                  \tag{6.5}
\]

If the touched supports differ, local rank already makes the target
images disjoint on a differing block, so (6.5) remains an upper bound.
Consequently

\[
 3^{-r}\sum_\theta
 \|Z_{P,q}^{\theta,\pm}
        -\widehat Z_{P,q,0}^{\pm}\|_2^2
 \ge S\bigl(1-(2/3)^{r-q}\bigr).                                 \tag{6.6}
\]

For \(q=o(r)\), this is \((1-o(1))S\). Summed over a packet catalogue of
total owner mass \(W-o(W)\), the diagonal scale is therefore \(W-o(W)\).
Any coefficient-one proof must cancel essentially all of it against the
second line of (6.3), up to the integral floor in (5.5).

The exact missing condition is

\[
\boxed{
\begin{aligned}
 &2\operatorname {Re}
 \sum_{k}\sum_{q\le H}\sum_{\pm}w_q
 \sum_{P<P'}\sum_{\gamma\ne0}
 \left\langle\widehat Z_{P,k,q,\gamma}^{\pm},
               \widehat Z_{P',k,q,\gamma}^{\pm}\right\rangle\\
 &\qquad\le
 -\sum_{k}\sum_{q\le H}\sum_{\pm}w_q
   \sum_P\sum_{\gamma\ne0}
       \|\widehat Z_{P,k,q,\gamma}^{\pm}\|_2^2
 +\sum_k\sum_{q\le H}\sum_{\pm}w_q
    N_{k,q}^\pm\xi_{k,q}^\pm(1-\xi_{k,q}^\pm)
 +o(W).
                                                                    \tag{6.7}
\end{aligned}}
\]

One may include the constant-mode bias from (5.5) on the right with a
minus sign; omitting it only weakens the necessary inequality.

No result presently proved for the hashed atlas establishes (6.7).
Frame diffusion controls the number of windows internal to a prescribed
global pairing. Trace-rainbow injectivity says each
\(Z_{P,k,q}^{\theta,\pm}\) is zero-one. Neither statement evaluates the
inner products between two different physical packet tags in (6.7).

At first ternary harmonic, (0.1) gives an equivalent weighted three-cut
interpretation. If \(w_{P,P'}\) is the relevant physical collision
weight, then a local seed coordinate contributes

\[
 \frac43 W_{\rm same}-\frac23W_{\rm different}
 =2W_{\rm same}-\frac23W_{\rm total}.                            \tag{6.8}
\]

Negative drift requires more than \(2/3\) of the collision weight, not
merely more than \(2/3\) of all packet pairs, to cross seed classes. The
anchor hash balances vertex mass. It does not prove this
collision-weighted three-cut inequality.

## 7. Audit of the fixed-four-block side-size argument

There is a tempting but invalid shortcut. Fix the even local-rank data
and an odd-block set \(J\) of size \(s\). Lower and upper targets may
have cardinalities proportional to

\[
 \binom sk,\qquad \binom{s}{k+q}.                                  \tag{7.1}
\]

Unequal side sizes do **not** by themselves force their absolute
difference to remain uncovered. A family of edges in a bipartite graph
can cover both unequal shores by repeating vertices on the smaller shore.
For example, two edges from two distinct vertices on the larger shore to
one common vertex on the smaller shore cover all three vertices.

This is precisely the phenomenon under audit: distinct packets may emit
the same lower target and different upper targets, or conversely.
Packetwise injectivity forbids repetition inside one packet, but it does
not forbid it across packets. Hence the inference

\[
 M_q^-+M_q^+
 \ge\sum_{\mathfrak c}
   \left|\binom{s(\mathfrak c)}{k(\mathfrak c)}
          -\binom{s(\mathfrak c)}{k(\mathfrak c)+q}\right|         \tag{7.2}
\]

is not valid without an additional component occurrence-capacity bound.
The assertion that “one occurrence covers one vertex on each side” is
insufficient: the number of occurrences in a component may exceed its
smaller shore.

The three \(B_4\) port bijections make this issue concrete. Varying the
seed pairs a fixed singleton with triples missing each of the other three
coordinates. Thus repeated use of one lower port can genuinely feed
several different upper ports. Any fixed-four-block obstruction must
bound the available middle starts or prove a Hall cut in the full labelled
inclusion graph; shore cardinality alone is not such a bound.

## 8. Exact remaining theorem

The hashed atlas has passed the two previous statewise audits:

1. there is no dominant fixed coordinate pairing; and
2. there is no within-packet shadow collision through depth \(r\).

The next theorem cannot be another unweighted seed census. It must prove
one of the following equivalent physical statements:

* the collision-conditioned ternary Walsh inequality (6.7);
* a simultaneous weighted three-cut in which more than the critical
  fraction of every relevant physical overlap kernel crosses seed
  classes;
* or directly
  \[
    \sum_{q\le H}\sum_\pm M_q^\pm=o(W)
  \]
  for the loads \(\mu_{k,q}^{\theta,\pm}\) averaged by the equitable
  anchor array.

The packet tags \(u,I,c\), the recursive phase, the touched support, and
the literal singleton/triple port labels must all remain in that theorem.
Forgetting any of them returns only a quotient Gram and cannot establish
(6.7).
