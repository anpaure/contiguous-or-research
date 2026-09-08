# Isometric hypercube cycle factors and the consecutive-direction covering gate

Date: 2026-07-26

Method: pure mathematics only.  No finite search, solver, program, or web
input is used.

## 0. Exact verdict

Let \(Q_h\) be the cube on \(\mathbb F_2^h\), with edge direction \(i\)
meaning addition of \(e_i\).  Let \(H<h\) be the requested consecutive
depth.

The problem separates into an abstract permutation-design problem and an
integral vertex-tiling problem.

1. An isometric \(2h\)-cycle has cyclic direction word exactly
   \(\pi\pi\), where \(\pi\) is a permutation of \([h]\).
2. A vertex \(2\)-factor by such cycles exists if and only if
   \(h=2^r\ge2\).  A quotient Hamming-code tiling gives an explicit
   factor, but all of its cycles have one common direction order and it is
   useless as a \(q\)-cover.
3. A factor has
   \[
                    N_h=\frac{2^h}{2h}=\frac{2^{h-1}}h             \tag{0.1}
   \]
   cycles.  At every \(1\le q<h\), its total number of distinct
   cycle--\(q\)-block incidences is \(2^{h-1}\), so the balanced target is
   \[
                    \mu_q=\frac{2^{h-1}}{\binom hq}.                \tag{0.2}
   \]
4. Abstractly, exactly \(N_h\) cyclic permutations can be made
   simultaneously \((1+o(1))\)-balanced for every \(q\le A\sqrt h\);
   in fact exponentially small relative error is possible.  Thus there is
   no counting or permutation-word obstruction.
5. There is an exact arbitrary-merge product theorem: any balanced binary
   merge word may be installed independently in each product torus while
   retaining a literal vertex \(2\)-factor.  This is genuine
   de-Bruijn-style scheduling freedom, not a formal word list.
6. This operation gives a literal positive construction through the full
   sub-Gaussian regime \(H=o(\sqrt h)\): there is one exact factor for which, uniformly
   at every \(q\le H\), only an \(o(1)\)-fraction of direction \(q\)-sets
   are absent.
7. Nevertheless, every recursive construction from fixed \(Q_4\) leaf
   factors in one coordinate hierarchy has a sharp Gaussian obstruction.
   If \(q\sim A\sqrt h\), at most an \(e^{-A^2/2}+o(1)\) fraction of the
   \(q\)-subsets can occur, irrespective of all internal merge words and
   phases.  A single fixed affine syndrome is also impossible: it omits
   at least one coordinate pair in every cycle, so it cannot be an exact
   pair-cover.
8. A context-dependent fibrewise product escapes both obstructions.
   Over each right factor cycle one may install an independently
   coordinate-conjugated left Hamming factor, because the corresponding
   right-cycle slabs are vertex-disjoint.  The companion report
   MATH_ATTACK_R_MULTIKERNEL_RAINBOW_TILING_20260726.md proves that one
   resulting exact factor is almost-everywhere strongly balanced
   simultaneously for every \(q\le A\sqrt h\).

Thus the requested combined Gaussian-depth direction factor **is
constructed**.  The fixed-kernel and fixed-leaf results below remain
sharp obstructions to the two natural homogeneous constructions, but not
to context-dependent multikernel fibres.  The separate physical
basepoint-collision problem is not settled here.

## 1. Rigidity of maximum isometric cycles

Let a \(2h\)-cycle have cyclic direction word

\[
                         d_0d_1\cdots d_{2h-1}.        \tag{1.1}
\]

### Theorem 1.1

The cycle is isometric in \(Q_h\) if and only if, up to cyclic rotation
and reversal,

\[
                         d_0\cdots d_{2h-1}=\pi\pi     \tag{1.2}
\]

for a permutation \(\pi\) of \([h]\).

#### Proof

If a cyclic arc of length \(\ell\le h\) repeats a direction, then the
Hamming distance of its endpoints is at most \(\ell-2\), contradicting
isometry.  Hence every \(h\)-term window in (1.1) contains every direction
once.  Comparing the windows beginning at \(i\) and \(i+1\), the direction
removed from the first must equal the one inserted into the second:

\[
                         d_{i+h}=d_i.                  \tag{1.3}
\]

The first \(h\) directions are distinct, proving (1.2).

Conversely, every cyclic subword of length at most \(h\) in \(\pi\pi\)
has distinct letters.  Its endpoint distance therefore equals its length.
The shorter arc between any two cycle vertices has length at most \(h\),
so all cycle distances equal cube distances. \(\square\)

If \(v_i\) is the cycle vertex before direction \(d_i\), then

\[
                         v_{i+h}=v_i+\mathbf1.          \tag{1.4}
\]

Thus every such cycle consists of \(h\) antipodal vertex pairs.

## 2. Consecutive blocks and monotone faces

For \(1\le q<h\), define

\[
 \mathcal B_q(\pi)=
 \left\{
  \{\pi_i,\pi_{i+1},\ldots,\pi_{i+q-1}\}:
  i\in\mathbb Z/h\mathbb Z
 \right\}.                                             \tag{2.1}
\]

These are exactly the direction supports of consecutive \(q\)-edge
segments of the cycle.  Every member occurs twice in the full
\(2h\)-word, at antipodal starts.

### Lemma 2.1

For every \(1\le q<h\),

\[
                         |\mathcal B_q(\pi)|=h,         \tag{2.2}
\]

and

\[
 \mathcal B_{h-q}(\pi)
 =\{[h]\setminus S:S\in\mathcal B_q(\pi)\}.           \tag{2.3}
\]

#### Proof

Because \(\pi\) is a bijection, equality of two direction sets in (2.1)
would imply equality of their two proper cyclic position intervals.
Such intervals have the same initial position, proving (2.2).
The complementary positions to a cyclic \(q\)-interval form the opposite
cyclic \((h-q)\)-interval, proving (2.3). \(\square\)

If a segment starts at \(x\) and has support \(S\), it is a monotone chain
inside the \(q\)-face

\[
                         x+\operatorname {span}\{e_i:i\in S\}.     \tag{2.4}
\]

Thus covering direction \(q\)-sets by consecutive blocks is exactly
covering the possible free-coordinate sets of these monotone faces.  It
does not by itself control their basepoints.

## 3. Factor existence: exact divisibility and a Hamming construction

A vertex factor contains \(N_h\) cycles as in (0.1).  Therefore

\[
                         2h\mid2^h.                    \tag{3.1}
\]

Since the right side has no odd prime divisor, (3.1) forces \(h\) to be a
power of two.

This is sufficient.  Assume \(h=2^r\ge2\), and define

\[
 \delta:\mathbb F_2^h\longrightarrow\mathbb F_2^{h-1},
 \qquad
 \delta(x)_i=x_i+x_{i+1}.                             \tag{3.2}
\]

Its kernel is \(\{0,\mathbf1\}\).  For the standard cycle with word

\[
                         (1,2,\ldots,h)(1,2,\ldots,h),              \tag{3.3}
\]

the quotient image of its vertex set is

\[
                         E=\{0,e_1,\ldots,e_{h-1}\}.   \tag{3.4}
\]

Label the \(h-1=2^r-1\) quotient coordinates by the nonzero vectors
\(a_1,\ldots,a_{h-1}\) of \(\mathbb F_2^r\), and put

\[
 K=\left\{z\in\mathbb F_2^{h-1}:
                 \sum_{j=1}^{h-1}z_ja_j=0\right\}.    \tag{3.5}
\]

### Lemma 3.1

The sets \(k+E\), \(k\in K\), partition \(\mathbb F_2^{h-1}\).

#### Proof

For any \(z\), its syndrome \(\sum_jz_ja_j\) is either zero or equals a
unique nonzero column \(a_i\).  Accordingly, exactly one of \(z\) or
\(z+e_i\) lies in \(K\).  Thus \(z\) lies in a unique translate
\(k+E\). \(\square\)

Choose \(x_k\) with \(\delta(x_k)=k\).  The sets

\[
                         x_k+\delta^{-1}(E),\qquad k\in K,          \tag{3.6}
\]

are translates of the standard isometric cycle and partition
\(\mathbb F_2^h\).  Hence:

\[
 \boxed{\text{A simple isometric \(2h\)-cycle factor exists exactly for
 \(h=2^r\ge2\).}}                                      \tag{3.7}
\]

All cycles in (3.6) have the same cyclic order.  Consequently, for fixed
\(q\), they cover only \(h\) of the \(\binom hq\) possible direction sets.
Factor existence alone gives no design balance.

## 4. Exact incidence ledgers and counting lower bounds

Let \(\mathcal F\) be any isometric \(2h\)-cycle factor, and write
\(\pi_C\) for the cyclic order on component \(C\).  Define

\[
 A_q(S)=
 \#\{C\in\mathcal F:S\in\mathcal B_q(\pi_C)\},
 \qquad S\in\binom{[h]}q.                             \tag{4.1}
\]

Then

\[
 \sum_{|S|=q}A_q(S)=N_hh=2^{h-1},                    \tag{4.2}
\]

\[
 \sum_{\substack{|S|=q\\i\in S}}A_q(S)=N_hq
 \qquad(i\in[h]),                                     \tag{4.3}
\]

and

\[
                         A_q(S)=A_{h-q}([h]\setminus S).           \tag{4.4}
\]

Indeed, a cyclic order has \(h\) \(q\)-intervals, and each coordinate lies
in exactly \(q\) of them.  Equation (4.4) is (2.3).

Thus the only possible uniform load is \(\mu_q\) from (0.2).  If a family
of \(M\) cyclic orders covers every \(q\)-set at least \(\lambda_q\) times,
then

\[
 \boxed{
 M\ge
 \left\lceil\frac{\lambda_q\binom hq}{h}\right\rceil.}             \tag{4.5}
\]

For simultaneous depths \(q\le H\), take the maximum of (4.5).
At factor size \(M=N_h\), once-covering has no counting obstruction exactly
when

\[
                         \binom hq\le2^{h-1}.           \tag{4.6}
\]

The physical \(2h\)-word contains every incidence counted in \(A_q(S)\)
twice.  Hence all physical block multiplicities are even.

We use two notions of approximation:

* weak \(\varepsilon\)-covering means that at most an
  \(\varepsilon\)-fraction of the \(q\)-sets have \(A_q(S)=0\);
* strong \(\varepsilon\)-balance means
  \[
                         |A_q(S)-\mu_q|\le\varepsilon\mu_q
                                                               \tag{4.7}
  \]
  for every \(S\).

## 5. The abstract permutation problem is overwhelmingly positive

Assume \(h=2^r\), so \(N_h\) is an integer.  Take \(M=N_h\) independent
uniformly random cyclic orders.  For fixed
\(S\in\binom{[h]}q\),

\[
 \Pr(S\in\mathcal B_q(\pi))=\frac h{\binom hq},        \tag{5.1}
\]

so

\[
 A_q(S)\sim\operatorname {Bin}\left(
        N_h,\frac h{\binom hq}\right),
 \qquad \mathbb EA_q(S)=\mu_q.                        \tag{5.2}
\]

Let

\[
                         K_H=\sum_{q=1}^H\binom hq,
 \qquad H\le h/2.                                     \tag{5.3}
\]

### Theorem 5.1 (simultaneous abstract balance)

If

\[
             2K_H\exp\left(-\frac{\varepsilon^2\mu_H}{3}\right)<1,
                                                               \tag{5.4}
\]

then a deterministic list of exactly \(N_h\) cyclic orders satisfies
(4.7) simultaneously for every \(q\le H\).

#### Proof

For \(q\le H\le h/2\), one has \(\mu_q\ge\mu_H\).  The multiplicative
Chernoff bound gives failure probability at most
\(2\exp(-\varepsilon^2\mu_H/3)\) for each pair \((q,S)\).  Union bound over
the \(K_H\) pairs proves that positive probability remains. \(\square\)

For every fixed \(A\), if \(H\le A\sqrt h\), then

\[
 \log K_H=O\left(H\log\frac{eh}{H}\right)=o(h),
 \qquad
 \mu_H=2^{h-o(h)}.                                    \tag{5.5}
\]

Therefore \(\varepsilon_h=2^{-h/4}\) satisfies (5.4) for all sufficiently
large \(h\).  The abstract word family is much more balanced than the
constant-one application asks for.

A single de Bruijn word cannot stitch these orders while retaining
isometry.  If every \(h\)-window in a cyclic word is a permutation of
\([h]\), comparison of adjacent windows again gives

\[
                         w_{i+h}=w_i,                  \tag{5.6}
\]

so the word is \(h\)-periodic and contains only one cyclic order.  A
de Bruijn or universal-cycle mechanism can schedule a **list** of cycle
orders, but cannot concatenate them into one isometric direction word.

## 6. Exact vertex ownership is a rainbow-tile problem

Quotient antipodal vertices:

\[
                         G=\mathbb F_2^h/\langle\mathbf1\rangle.   \tag{6.1}
\]

For a cyclic order \(\pi\), put

\[
 T_\pi=
 \left\{
 0,\bar e_{\pi_1},
 \bar e_{\pi_1}+\bar e_{\pi_2},\ldots,
 \sum_{j=1}^{h-1}\bar e_{\pi_j}
 \right\}\subseteq G.                                 \tag{6.2}
\]

### Theorem 6.1 (exact realization criterion)

A prescribed list \(\pi_1,\ldots,\pi_{N_h}\) is realized by an isometric
cycle factor if and only if there are \(x_1,\ldots,x_{N_h}\in G\) such
that

\[
                         G=\bigsqcup_{a=1}^{N_h}(x_a+T_{\pi_a}).   \tag{6.3}
\]

#### Proof

Quotienting one isometric cycle by (1.4) gives exactly one translate of
(6.2).  Vertex-disjoint cycles give disjoint tiles, and their cardinalities
sum to \(|G|\).  Conversely, lifting every tile restores its two antipodal
copies and the direction word \(\pi_a\pi_a\), hence an isometric cycle.
\(\square\)

Fourier transforming the indicator identity in (6.3), every nonzero
character gives

\[
 \sum_{a=1}^{N_h}(-1)^{u\cdot x_a}
 \sum_{t=0}^{h-1}
 (-1)^{u\cdot(\bar e_{\pi_{a,1}}+\cdots+\bar e_{\pi_{a,t}})}
 =0,                                                  \tag{6.4}
\]

where \(u\in\mathbb F_2^h\) has nonzero even weight.  For
\(u=e_p+e_q\), the inner sum is

\[
                         \pm\bigl(h-2d_{\pi_a}(p,q)\bigr),         \tag{6.5}
\]

where \(d_{\pi_a}(p,q)\) is one of the two oriented cyclic separations.
Thus interval counts alone do not imply vertex ownership: the translations
must cancel all signed separation modes (6.4).

Uniform fractional weight on all translated rainbow tiles is a perfect
fractional matching, and coordinate symmetry gives every \(q\)-set its
exact fractional quota \(\mu_q\).  Hence the obstruction is integral, not
linear or counting.

## 7. Arbitrary balanced merges are literal factor operations

Let \(C=(c_i:i\in\mathbb Z_{2d})\) and
\(D=(d_j:j\in\mathbb Z_{2d})\) be oriented isometric cycles on disjoint
\(d\)-coordinate cubes.  Let

\[
                         \sigma\in\{L,R\}^{2d},
 \qquad |\sigma|_L=|\sigma|_R=d.                      \tag{7.1}
\]

For \(0\le t\le2d\), let \(a_t,b_t\) be the numbers of \(L,R\) symbols
before position \(t\), and extend them by

\[
 a_{t+2d}=a_t+d,\qquad b_{t+2d}=b_t+d.                \tag{7.2}
\]

Fix a phase \(\theta\in\mathbb Z_{2d}\).  For \(0\le r<d\), define

\[
 \Gamma_r(t)=
 \bigl(c_{a_t+r},d_{b_t-r+\theta}\bigr),
 \qquad 0\le t<4d.                                    \tag{7.3}
\]

### Theorem 7.1 (arbitrary-merge torus factor)

The \(d\) cycles \(\Gamma_r\) partition \(V(C)\times V(D)\), each has
length \(4d\), and each is isometric in \(Q_{2d}\).  Its first-half
direction permutation is the \(\sigma\)-merge of one full cyclic shift of
the direction permutation of \(C\) and one of \(D\).

#### Proof

At an \(L\)-step, (7.3) advances once on \(C\); at an \(R\)-step it
advances once on \(D\).  During the first \(2d\) steps, every parent is
advanced \(d\) times, so every left and right coordinate direction occurs
once.  The second half repeats the same directions because parent
direction words have period \(d\).  Theorem 1.1 proves isometry once
vertex partition is checked.

Given \((c_i,d_j)\), equation \(a_t+b_t=t\) forces

\[
                         t\equiv i+j-\theta\pmod{2d}.              \tag{7.4}
\]

Choose that residue \(t\), and solve

\[
                         r\equiv i-a_t\pmod{2d}.       \tag{7.5}
\]

If \(0\le r<d\), this gives its unique occurrence.  If \(d\le r<2d\),
replace \((r,t)\) by \((r-d,t+2d)\); (7.2) gives the same vertex.
This is unique and accounts for all \(4d^2\) vertices. \(\square\)

Thus arbitrary balanced, blocky, or de-Bruijn-inspired merge schedules
are exactly legal independently in every product torus.

There is also an exact amplification formula in the regime \(q<d\), which
contains (7.10).  Let \(A_L(S_L)\) and
\(A_R(S_R)\) be the parent interval counts, and let
\(A_{\rm out}(S)\) denote the number of output cycles in whose first-half
cyclic direction order \(S\) is an interval.  Choose \(\sigma,\theta\)
independently and uniformly in each torus; the word \(\sigma\) is repeated
periodically in the second half.  If

\[
                         a=|S_L|,\quad b=|S_R|,\quad q=a+b,        \tag{7.6}
\]

with \(0<a,b<d\), then

\[
 \mathbb E A_{\rm out}(S)
 =
 \frac{2\binom da\binom db}{\binom{2d}q}
 A_L(S_L)A_R(S_R).                                    \tag{7.7}
\]

If \(a=0\) and \(0<b<d\), then

\[
 \mathbb E A_{\rm out}(S)
 =
 \frac{2d\binom db}{\binom{2d}b}
 N_dA_R(S_R),                                         \tag{7.8}
\]

and symmetrically when \(b=0\).

To prove (7.7), fix one left parent interval occurrence, one right parent
interval occurrence, a merge word \(\sigma\), and a start \(t\) at which
the next \(q\) symbols of \(\sigma\) contain \(a\) letters \(L\) and \(b\)
letters \(R\).  The left starting phase determines one value of
\(r\pmod d\).  For that value there are exactly two values of
\(\theta\pmod {2d}\) aligning the proper right interval: its two
antipodal occurrences in the parent \(2d\)-cycle.  Averaging over
\(\theta\) therefore gives contribution \(1/d\) from this start.

For a uniform balanced word, the expected number among the \(2d\) cyclic
starts whose following \(q\) positions have this split is

\[
             \frac{2d\binom da\binom db}{\binom{2d}q}.            \tag{7.8a}
\]

Multiplying (7.8a) by \(1/d\), and then by the two parent occurrence
counts, proves (7.7).  If \(a=0\), the left interval is empty and the
left phase \(r\) is free.  The factor \(1/d\) is consequently replaced
by \(1\), while (7.8a) with \(a=0\), followed by summation over all
\(N_d\) left parent cycles, proves (7.8).  The restriction \(q<d\)
excludes the full-child boundary cases, where antipodal occurrences
coalesce differently and the displayed coefficients are not asserted.

In particular, for \(q<d\), perfectly uniform parent ledgers produce the
perfectly uniform output expectation \(2^{2d-1}/\binom{2d}q\).

Each product torus contributes between zero and \(d\) to a fixed
\(A_{\rm out}(S)\).  There are \(N_d^2\) independent tori.  Hoeffding and
a union bound give simultaneous additive error at most

\[
 2^{d-1}
 \sqrt{\frac12\log\left(
       \frac{2\sum_{q\le H}\binom{2d}q}{\eta}\right)}              \tag{7.9}
\]

with probability at least \(1-\eta\).  This is concentration around the
conditional expectation in (7.7)--(7.8).  If both child ledgers have
relative error at most \(\varepsilon\), the interior conditional
expectation has relative error at most \(2\varepsilon+\varepsilon^2\);
the one-empty-side case has error at most \(\varepsilon\).
For fixed, or otherwise non-exponentially tiny, \(\eta\), the fluctuation
in (7.9) is \(o(1)\) relative to the depth-\(H\) uniform mean whenever

\[
                         H=o\left(\frac d{\log d}\right),          \tag{7.10}
\]

in particular throughout \(H=O(\sqrt d)\), **provided the two child
ledgers already have the required balance**.

The qualification is decisive: merging cannot create a child interval
which was absent in the child factor.

### 7.2 A literal weak covering construction with one logarithmic loss

The amplification theorem nevertheless gives a nontrivial exact-factor
construction.  Its exceptional sets can be counted without any
independence assumption.

### Theorem 7.2 (block-transversal exact factor)

Let \(h=2^r\) tend to infinity.  Let \(B=B(h)\) be the least power of two
such that

\[
                         B\ge \max\{32,8\log_2 h\}.                \tag{7.11}
\]

Partition \([h]\) into \(h/B\) coordinate blocks of size \(B\).  There is
an isometric \(2h\)-cycle factor \(\mathcal F_h\) and a number
\(\delta_h=o(1)\) such that, for every nonempty set \(S\subseteq[h]\)
meeting each block in at most one coordinate,

\[
 \left|A_{|S|}(S)-\frac{2^{h-1}}{\binom h{|S|}}\right|
 \le
 \delta_h\frac{2^{h-1}}{\binom h{|S|}}.             \tag{7.12}
\]

Consequently, for every \(1\le q\le h/B\), the fraction of direction
\(q\)-sets absent from this one factor is at most

\[
                 \frac{q(q-1)(B-1)}{2(h-1)}.         \tag{7.13}
\]

In particular, one exact factor is a simultaneous weak \(o(1)\)-cover
at every \(q\le H\) whenever

\[
                 \frac{H^2B}{h}=o(1).                \tag{7.14}
\]

Since \(B<16\log_2h\) for all sufficiently large \(h\), this includes

\[
                         H=o\!\left(\sqrt{h/\log h}\right).       \tag{7.15}
\]

#### Proof

On every \(B\)-block take any factor supplied by Section 3.  Arrange the
blocks as the leaves of a balanced binary tree.  At each internal node,
merge the two already constructed child factors by Theorem 7.1, choosing
the merge word and phase independently and uniformly in each product
torus before fixing one successful realization.

Consider a node on \(2d\) coordinates, where each child has \(d\)
coordinates and \(d\ge B\).  A block-transversal subset of that node has
size at most \(2d/B<d\), so (7.7)--(7.8) apply at every node.  The number
of all such subsets is at most

\[
                         K_d=(B+1)^{2d/B},             \tag{7.16}
\]

because each base block contributes either no coordinate or one of its
\(B\) coordinates.  Use (7.9) with failure parameter \(1/2\), and divide
its additive error by the smallest relevant uniform mean.  Since
\(q\mapsto\binom{2d}q\) is increasing for
\(q\le2d/B\le d\), the resulting relative fluctuation is at most

\[
 \rho_d=
 2^{-d}\binom{2d}{\lfloor2d/B\rfloor}
 \sqrt{\frac12\log(4K_d)}.                            \tag{7.17}
\]

(If \(2d/B\) is integral, as it is here, the floor is redundant.)

Let \(\delta_d\) be a common relative-error bound for every nonempty
block-transversal subset in either child factor.  Equations (7.7)--(7.8)
say that the conditional expectation at the parent has relative error at
most \(2\delta_d+\delta_d^2\); when one side is empty the sharper bound is
\(\delta_d\).  Hence a realization exists with

\[
                 \delta_{2d}\le
                 2\delta_d+\delta_d^2+\rho_d.         \tag{7.18}
\]

At a leaf, the only nonempty block-transversal sets are singletons, and
every cyclic order contains every singleton.  Thus

\[
                         \delta_B=0.                  \tag{7.19}
\]

For \(B\ge32\),

\[
 \binom{2d}{2d/B}
 \le(eB)^{2d/B}\le2^{d/2}.                            \tag{7.20}
\]

Combining (7.16)--(7.20) gives

\[
 \rho_d\le
 2^{-d/2}
 \sqrt{(d/B)\log(B+1)+\log2}.                         \tag{7.21}
\]

As long as \(\delta_d\le1\), (7.18) is at most
\(3\delta_d+\rho_d\).  If \(L=\log_2(h/B)\), iteration therefore gives

\[
 \delta_h
 \le
 \sum_{j=0}^{L-1}3^{L-1-j}\rho_{2^jB}
 \le
 C3^L2^{-B/2}\sqrt{\log(B+1)}                         \tag{7.22}
\]

for an absolute constant \(C\); the doubly exponential decay in
\(2^jB\) absorbs the remaining square-root factors.  Now
\(3^L=(h/B)^{\log_2 3}\), while (7.11) gives
\(2^{-B/2}\le h^{-4}\).  The right side of (7.22) tends to zero.  This
also verifies retrospectively that \(\delta_d\le1\) at every stage for
all sufficiently large \(h\), and proves (7.12).

It remains only to count the discarded sets.  Among the \(\binom h2\)
coordinate pairs, exactly

\[
                         \frac hB\binom B2
\]

lie within one base block.  For a uniform \(q\)-subset, the expected
number of contained within-block pairs is therefore

\[
 \frac hB\binom B2
 \frac{\binom{h-2}{q-2}}{\binom hq}
 =\frac{q(q-1)(B-1)}{2(h-1)}.                         \tag{7.23}
\]

Every nontransversal set contains at least one such pair, so Markov's
inequality (equivalently, the union bound) gives (7.13).  Every
transversal set occurs by (7.12), because \(\delta_h<1\).  Equations
(7.14)--(7.15) follow. \(\square\)

The near-balance demand in Theorem 7.2 costs the logarithm.  If only
covering is required, a much softer lower-load induction reaches every
sub-Gaussian depth.

### Theorem 7.3 (full sub-Gaussian weak covering)

Let \(B,h\) be powers of two with \(h\ge B\ge32\), and partition
\([h]\) into \(h/B\) blocks of size \(B\).  There is an exact isometric
\(2h\)-cycle factor such that every nonempty block-transversal set
\(S\), with \(q=|S|\), satisfies

\[
 A_q(S)\ge
 2^{-(h/B-1)}\frac{2^{h-1}}{\binom hq}>0.             \tag{7.24}
\]

It follows that for every integer sequence \(H=H(h)=o(\sqrt h)\), with
\(h\) restricted to powers of two, there is one exact factor whose
uncovered fraction is \(o(1)\), uniformly for every \(q\le H\).

#### Proof

We prove the following statement at every node of a balanced merge tree.
If the node has dimension \(D=nB\), where \(n\) is a power of two, then
one can choose a factor for which

\[
 A_k(S)\ge
 2^{-(n-1)}\frac{2^{D-1}}{\binom Dk}                 \tag{7.25}
\]

for every nonempty block-transversal \(S\subseteq[D]\), \(k=|S|\).
For \(n=1\), the only such sets are singletons and (7.25) is equality.

Suppose the two children have dimension \(d=D/2\) and \(n/2\) base
blocks.  Conditional on their factors, choose all torus merge words and
phases independently and uniformly.  If \(S\) meets both children,
(7.7) and the induction hypothesis give

\[
 \mathbb E A_k(S)\ge
 2^{-(n-2)}\frac{2^{D-1}}{\binom Dk}.                 \tag{7.26}
\]

If one child intersection is empty, (7.8) gives the stronger normalized
factor \(2^{-(n/2-1)}\), so (7.26) remains valid.

There are at most

\[
                         K=(B+1)^n                  \tag{7.27}
\]

block-transversal subsets.  Since \(k\le n=D/B\le D/2\), (7.26) is
uniformly at least

\[
 E_*=
 2^{-(n-2)}\frac{2^{D-1}}{\binom Dn}
 \ge
 2^{\,D-n+1}(eB)^{-n}.                               \tag{7.28}
\]

For a fixed \(S\), its output load is a sum over the \(N_d^2\) product
tori, each summand lying in \([0,d]\).  Thus the sum of squared ranges is

\[
                         N_d^2d^2=2^{D-2}.            \tag{7.29}
\]

Hoeffding's lower-tail inequality and (7.28) give

\[
 \Pr\!\left(A_k(S)<\tfrac12\mathbb EA_k(S)\right)
 \le
 \exp\!\left(-\frac{E_*^2}{2^{D-1}}\right).           \tag{7.30}
\]

For \(B\ge32\),

\[
 \gamma_B:=
 1-\frac{2(1+\log_2(eB))}{B}\ge\frac12,               \tag{7.31}
\]

and therefore

\[
                         \frac{E_*^2}{2^{D-1}}
                         \ge2^{\gamma_BD+3}
                         \ge2^{D/2+3}.                \tag{7.32}
\]

Also

\[
                         \log K=\frac DB\log(B+1)\le\frac D4.     \tag{7.33}
\]

Consequently \(K\exp(-2^{D/2+3})<1\).  The union bound shows that one
choice of all torus schedules simultaneously has
\(A_k(S)\ge\frac12\mathbb EA_k(S)\) for every relevant \(S\).
Together with (7.26), this is precisely (7.25).  Induction proves
(7.24).

Now let \(H=o(\sqrt h)\), so \(R_h=h/H^2\to\infty\).  Choose a power of
two \(B=B(h)\) such that

\[
                         B\to\infty,\qquad B=o(R_h).                \tag{7.34}
\]

For example, for large \(h\), take the least power of two at least
\(\max\{32,\sqrt{R_h}\}\).  Then \(BH^2/h=o(1)\), and also
\(H\le h/B\).  Apply the construction above.  Equation (7.23), uniformly
for \(q\le H\), bounds the uncovered fraction by

\[
                         \frac{H(H-1)(B-1)}{2(h-1)}=o(1).          \tag{7.35}
\]

This is one literal integral factor, not a fractional mixture.
\(\square\)

## 8. Two sharp obstructions to the natural constructions

### 8.1 One fixed syndrome kernel

Let \(h=2^r\), let \(L:G\to\mathbb F_2^r\) be onto, and suppose every
rainbow tile used is an \(L\)-transversal.  Put

\[
                         \ell_i=L(\bar e_i).            \tag{8.1}
\]

Every \(\ell_i\) is nonzero, since a zero step would repeat a syndrome
coset.  There are \(h\) directions but only \(h-1\) nonzero syndromes, so
some \(i\ne j\) satisfy

\[
                         \ell_i=\ell_j.                 \tag{8.2}
\]

The directions \(i,j\) cannot be consecutive in any transversal order:
two such steps would give

\[
                         y,\quad y+\ell_i,\quad
                         y+\ell_i+\ell_j=y,             \tag{8.3}
\]

repeating a syndrome.  Therefore every fixed-kernel affine/Latin family
misses the pair \(\{i,j\}\).  It is not even an exact \(q=2\) cover.

This applies as well to reciprocal rectangle switches for which every
resulting tile remains an \(L\)-transversal.

### 8.2 One fixed recursive product hierarchy

At dimension four, the two cycles of any isometric factor have one common
cyclic direction order up to reversal.  Indeed, in
\(G=\mathbb F_2^4/\langle\mathbf1\rangle\cong\mathbb F_2^3\), translate
the first tile to

\[
                         T=\{0,v_1,v_2,v_3\},
\]

where \(v_1,v_2,v_3\) form a basis.  Its complement is
\((v_1+v_2+v_3)+T\), so the second tile is its translate.  The coordinate
Cayley graph induced on \(T\) is the same labeled four-cycle, up to
reversal.

Relative to a four-coordinate leaf, the locally possible interval sets
therefore have enumerator

\[
                         f(x)=1+4x+4x^2+4x^3+x^4.     \tag{8.4}
\]

The missing terms at size two are the two opposite pairs of the local
four-cycle.

In every arbitrary merge, the restriction of a consecutive parent block
to either child is a consecutive child block.  Iterating through a fixed
hierarchy with \(h/4\) four-coordinate leaves, every globally occurring
\(q\)-set must be locally permitted in every leaf.  Consequently the
number of potentially coverable \(q\)-sets is at most

\[
                         [x^q]f(x)^{h/4}.              \tag{8.5}
\]

### Theorem 8.1 (Gaussian fixed-leaf-hierarchy deficit)

Suppose a factor is built recursively by Theorem 7.1 from one fixed
isometric \(Q_4\)-factor on each member of a fixed partition of the
coordinates into four-sets.  Arbitrary merge words, rotations, and phases
may be chosen separately in every internal product torus.  If
\(q/\sqrt h\to A\in[0,\infty)\), then

\[
 \frac{[x^q]f(x)^{h/4}}{\binom hq}
                         \longrightarrow e^{-A^2/2}.  \tag{8.6}
\]

Hence for \(A>0\), every such fixed-leaf product hierarchy leaves at least

\[
                         1-e^{-A^2/2}-o(1)             \tag{8.7}
\]

of the \(q\)-subsets uncovered, regardless of all merge schedules,
rotations, and phases.

#### Proof

Choose a uniform \(q\)-subset \(S\).  In each four-leaf let a bad event
mean that \(S\) meets the leaf in exactly one of its two opposite pairs.
Let \(Z\) be the number of bad leaves.  Then the probability \(Z=0\) is
the left side of (8.6).

For fixed \(k\), its factorial moment is

\[
 \mathbb E(Z)_k
 =
 \left(\frac h4\right)_{\!k}2^k
 \frac{\binom{h-4k}{q-2k}}{\binom hq}.                \tag{8.8}
\]

If \(q\sim A\sqrt h\), (8.8) tends to \((A^2/2)^k\).
The factorial moments therefore converge to those of
\(\operatorname {Poisson}(A^2/2)\), giving
\(\Pr(Z=0)\to e^{-A^2/2}\).  The case \(A=0\) follows by the same moments
or Markov's inequality. \(\square\)

Thus arbitrary merge words remove the earlier dyadic-balance obstruction
but cannot repair the finite-scale \(Q_4\) defect.  For
\(q=o(\sqrt h)\), this particular obstruction has density \(o(1)\); this
does not by itself prove that every remaining set is covered.

## 9. Consequence for the constant-one lane

For a cycle segment, a consecutive direction set is exactly the free
coordinate set of its monotone face (2.4).  A balanced permutation bank
therefore has more than enough abstract shallow-face supply.  The exact
factor must additionally solve the tile ownership equations (6.3), and a
constant-one application must still control physical basepoint collisions.

The proved boundary is:

* exact isometric factors exist at every power-of-two dimension;
* abstract simultaneous \(q\)-covering designs exist with enormous slack
  through \(H=O(\sqrt h)\);
* arbitrary de-Bruijn-style merge words are legitimate exact factor
  operations and amplify any already balanced child design;
* a recursively merged exact factor weakly covers all depths
  \(q\le H=o(\sqrt h)\), with the quantitative block-transversal
  construction in Theorem 7.3;
* one fixed syndrome kernel cannot cover all pairs;
* one fixed hierarchy recursively built from fixed \(Q_4\) leaf factors
  loses a positive fraction at every Gaussian depth
  \(q\sim A\sqrt h\);
* the context-dependent multikernel fibre construction in the companion
  report reaches every \(q\le A\sqrt h\) with uncovered fraction
  \(O_A((\log h)^6/h)\) and vanishing relative ledger error.

The fibrewise construction does leave both obstructed classes: it varies
the entire left Hamming factor with the exterior right cycle, while the
right-cycle slabs remain disjoint and therefore retain the integral
tiling (6.3).  This closes the inner direction-cover gate.  A
constant-one application would still have to control the physical
basepoint collisions noted above.
