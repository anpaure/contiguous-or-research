# A context-dependent multikernel rainbow tiling of the hypercube

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Result

For every fixed \(A>0\) and all sufficiently large powers of two
\(h=2^r\), there is an exact vertex \(2\)-factor of \(Q_h\) into
isometric \(2h\)-cycles with the following property.  If \(A_q(S)\)
is the number of factor cycles whose cyclic direction permutation has
\(S\) as a consecutive \(q\)-set, and

\[
             \mu_{h,q}:=\frac{2^{h-1}}{\binom hq},
\]

then, simultaneously for every \(1\le q\le A\sqrt h\), all but at most
the following proportion of the \(q\)-subsets,

\[
 \boxed{
  \binom{d_0}{2}\frac{q(q-1)}{h(h-1)}
       +2r h^{-8}}
                                                        \tag{0.1}
\]

satisfy

\[
 \boxed{
      A_q(S)=(1\pm\varepsilon_h)\mu_{h,q},\qquad
      \varepsilon_h\le 2r\,2^{-d_0/8}.}               \tag{0.2}
\]

Here

\[
 \ell=\lceil3\log _2r\rceil,
 \qquad d_0=2^\ell,
 \qquad r^3\le d_0<2r^3.                              \tag{0.3}
\]

In particular, the uncovered proportion at every depth
\(q\le A\sqrt h\) is

\[
                  O_A\!\left(\frac{(\log h)^6}{h}\right)=o_A(1). \tag{0.4}
\]

This is an integral rainbow-tile construction, not an abstract list of
permutations.  It escapes the fixed-kernel obstruction by choosing a
different coordinate-conjugated Hamming factor in each right-cycle
fibre.  It escapes the fixed \(Q_4\)-leaf hierarchy obstruction because
those conjugations mix all coordinates of the current left half and
depend on the exterior right cycle.

The conclusion is almost-everywhere strong balance of the direction
ledgers.  It does not by itself control the physical basepoints of the
corresponding monotone faces, so the later contiguous-OR collision gate
is not claimed here.

**Subsequent physical audit.**  The original use of a parallel Hamming
factor on every refreshed left fibre creates a deterministic physical
basepoint plateau: at a sub-Gaussian depth it misses
\(W-o(W)\) literal targets after ordinary mixed-frame embedding.  The
weaker \(1/2-o(1)\) bound already follows without using the direction
balance proved here.
See
MATH_OBSTRUCTION_R_MULTIKERNEL_PHYSICAL_BASEPOINT_PLATEAU_20260726.md.
Replacing those Hamming factors by the recursive half-depth trace-rainbow
factor preserves every direction conclusion in this report and removes
the internal plateau after an aggregate \(o(W)\) occurrence quarantine.
The outer cross-cell Gram cancellation remains open.

The restriction to powers of two is necessary: an isometric factor has
\(2^h/(2h)\) cycles, so \(2h\mid2^h\), which forces \(h\) to be a power
of two.

## 1. Input facts and notation

Write

\[
                  N_d=\frac{2^{d-1}}d.                \tag{1.1}
\]

For every power of two \(d\ge2\), the quotient Hamming construction gives
an exact isometric \(2d\)-cycle factor \(\mathcal P_d\) of \(Q_d\) in
which every cycle has one common cyclic direction order.  A uniform
coordinate permutation \(\rho\in S_d\) gives another exact factor
\(\rho\mathcal P_d\), again with one common order, now a uniform random
cyclic order.  Consequently, for a fixed
\(U\in\binom{[d]}a\), \(1\le a<d\),

\[
 \Pr_\rho\bigl(U\text{ is an interval of the common order}\bigr)
             =p_{d,a}:=\frac d{\binom da}.             \tag{1.2}
\]

If it is an interval, it is an interval in all \(N_d\) cycles; otherwise
it is in none.  Therefore its expected cycle load is exactly

\[
                  N_dp_{d,a}=\frac{2^{d-1}}{\binom da}
                  =:\mu_{d,a}.                        \tag{1.3}
\]

For the empty set it is convenient to define its compatible-cycle count
to be \(N_d\).

We also use the exact arbitrary-merge torus factor.  If \(C,D\) are
isometric \(2d\)-cycles on disjoint coordinate halves, a uniformly
random balanced word \(\sigma\in\{L,R\}^{2d}\), together with a uniformly
random phase, factors \(C\times D\) into \(d\) isometric \(4d\)-cycles.
If fixed nonempty sets of sizes \(a,b\) are intervals in \(C,D\), and
\(a+b<d\), the expected number of those \(d\) output cycles in which
their union is an interval equals

\[
        \alpha_{d;a,b}
        =\frac{2\binom da\binom db}{\binom{2d}{a+b}}.  \tag{1.4}
\]

If \(a=0<b<d\), the corresponding expectation per compatible cycle pair
is

\[
        \beta_{d;0,b}
        =\frac{2d\binom db}{\binom{2d}b},              \tag{1.5}
\]

and symmetrically for \(b=0<a<d\).  These are the exact formulas from
the arbitrary-merge theorem, applied to one parent-cycle pair.

## 2. The fibrewise multikernel product

Let \(L,R\) be disjoint coordinate sets of size \(d\).  Suppose
\(\mathcal F_R\) is any exact isometric factor on \(Q_R\).  For every
right cycle \(D\in\mathcal F_R\), independently choose a coordinate
permutation \(\rho_D\in\mathfrak S(L)\) and put on \(Q_L\) the parallel Hamming
factor

\[
                         \mathcal P_L(D):=\rho_D\mathcal P_d.     \tag{2.1}
\]

The conjugation in (2.1) acts on the entire factor--all cycle vertices,
translations, and direction orders--not merely on its displayed
direction word.

For each \(C\in\mathcal P_L(D)\), independently choose a balanced merge
word and phase and apply the arbitrary-merge factor to \(C\times D\).

### Lemma 2.1 (exact ownership)

The resulting cycles form an exact isometric \(4d\)-cycle factor of
\(Q_{L\sqcup R}\).

#### Proof

The cycles \(D\) partition \(Q_R\).  For a fixed \(D\), the cycles in
\(\mathcal P_L(D)\) partition all of \(Q_L\), even though this left
factor is allowed to depend on \(D\).  Hence the tori

\[
       \{C\times D:D\in\mathcal F_R, C\in\mathcal P_L(D)\}
\]

partition all vertices of \(Q_L\times Q_R\).  The arbitrary-merge
factor partitions every one of these tori into isometric cycles.  No
cross-fibre compatibility is needed because distinct tori are
vertex-disjoint.  Explicitly, every \(\rho_D\) is a coordinate
automorphism of the same left cube \(Q_L\), not a relabelling of a
different cube.  A left vertex may belong to different left cycles for
two choices \(D\ne D'\), but the product vertices have right coordinates
in the disjoint sets \(V(D)\) and \(V(D')\).  Thus neither basepoints nor
ownership can conflict across fibres. \(\square\)

This elementary observation is the integrality mechanism.  The kernel
or coordinate frame in (2.1) may vary independently with the exterior
cycle \(D\).

## 3. Exact packet expectation

Fix \(S=S_L\sqcup S_R\), with

\[
            a=|S_L|,\qquad b=|S_R|,\qquad 1\le a+b<d.             \tag{3.1}
\]

Let \(M\) be the number of right cycles in which \(S_R\) is an interval;
when \(b=0\), put \(M=N_d\).  For a fixed right cycle \(D\) compatible
with \(S_R\), let \(Z_D(S)\) be the total number of output cycles over
the tori \(C\times D\) in which \(S\) is an interval.

The variables \(Z_D(S)\), as \(D\) ranges over compatible right cycles,
are independent after conditioning on \(\mathcal F_R\), and

\[
                    0\le Z_D(S)\le dN_d=2^{d-1}.      \tag{3.2}
\]

There are exactly \(M\) such packets.  Each packet contains exactly
\(N_d\) product tori and therefore exactly \(dN_d=2^{d-1}\) output
cycles.  The packets are independent because the coordinate conjugation
and every torus merge are sampled independently for different right
cycles \(D\).  The cycles inside one packet are not asserted to be
independent.

As a count check, all \(N_d\) right packets contain
\(N_d\cdot dN_d=dN_d^2=N_{2d}\) output cycles in total.

### Lemma 3.1 (packet mean)

If \(b>0\), then

\[
 \boxed{
       \mathbb E Z_D(S)
       =\lambda_{d;a,b}
       :=\frac{2^d\binom db}{\binom{2d}{a+b}}.}       \tag{3.3}
\]

This formula includes \(a=0\).  If \(b=0<a\), then

\[
 \boxed{
       \mathbb E Z_D(S)
       =\lambda_{d;a,0}
       :=\frac{d\,2^d}{\binom{2d}a}.}                 \tag{3.4}
\]

Consequently, if \(b>0\),

\[
 \boxed{
   \mathbb E\bigl(A_{a+b}(S)\mid\mathcal F_R\bigr)
      =\frac{M}{\mu_{d,b}}\,\mu_{2d,a+b}.}            \tag{3.5}
\]

If \(b=0\), the conditional expectation is exactly
\(\mu_{2d,a}\).

#### Proof

Suppose first that \(a,b>0\).  The random parallel left factor is
compatible with \(S_L\) with probability \(p_{d,a}\); when compatible,
all \(N_d\) left cycles are compatible.  Equations (1.2), (1.4) give

\[
 \mathbb EZ_D
 =p_{d,a}N_d\alpha_{d;a,b}
 =\frac d{\binom da}\frac{2^{d-1}}d
   \frac{2\binom da\binom db}{\binom{2d}{a+b}},
\]

which is (3.3).  If \(a=0<b\), every left cycle is compatible, and
(1.1), (1.5) give

\[
 N_d\beta_{d;0,b}
 =\frac{2^{d-1}}d\frac{2d\binom db}{\binom{2d}b},
\]

again (3.3).  Summing (3.3) over the \(M\) compatible right cycles and
using \(\mu_{d,b}=2^{d-1}/\binom db\) proves (3.5).

If \(b=0<a\), there are all \(N_d\) right cycles.  For one such cycle,
(1.2), (1.3), and the symmetric version of (1.5) give

\[
 \mathbb EZ_D
 =\mu_{d,a}\frac{2d\binom da}{\binom{2d}a}
 =\frac{d2^d}{\binom{2d}a}.
\]

Multiplication by \(N_d\) gives
\(2^{2d-1}/\binom{2d}a=\mu_{2d,a}\). \(\square\)

Equation (3.5) is the decisive exact composition identity.  It uses
dependencies in packets of mass \(2^{d-1}\); it does not pretend that
individual output cycles have independent signs.

## 4. Recursive construction and simultaneous concentration

Assume \(h=2^r\), with \(r\) sufficiently large, and define \(d_0\) by
(0.3).  Put

\[
                  t=r-\ell,\qquad d_j=2^jd_0\quad(0\le j\le t),  \tag{4.1}
\]

so \(d_t=h\).  Partition the coordinates into a nested right spine

\[
 R_0\subset R_1\subset\cdots\subset R_t=[h],
 \qquad |R_j|=d_j,                                    \tag{4.2}
\]

where

\[
                  R_{j+1}=L_j\sqcup R_j,\qquad |L_j|=d_j.         \tag{4.3}
\]

Start on \(R_0\) with the parallel Hamming factor \(\mathcal F_0=
\mathcal P_{d_0}\).  Given \(\mathcal F_j\) on \(R_j\), construct
\(\mathcal F_{j+1}\) on \(L_j\sqcup R_j\) by the random fibrewise
multikernel product of Section 2.  Lemma 2.1 makes every
\(\mathcal F_j\) a literal exact factor.

For fixed \(A\), define

\[
 u_j=\left\lceil\frac{4eA d_j}{\sqrt h}+8r\right\rceil
 \quad(0\le j\le t).                                  \tag{4.4}
\]

Call \(T\subseteq R_j\) spine-sparse if

1. \(|T\cap R_0|\le1\);
2. \(|T\cap L_i|\le u_i\) for every \(0\le i<j\);
3. \(|T\cap R_i|\le u_i\) for every \(1\le i\le j\).

For large \(h\), uniformly in \(j<t\),

\[
             2u_j<d_j,                                \tag{4.5}
\]

and

\[
 \zeta_h:=\max_{0\le j<t}
       \frac{2u_j\log_2(2d_j)}{d_j}=o_A(1).           \tag{4.6}
\]

Indeed, \(d_0\ge r^3\), while the two terms in (4.6) are bounded by
\(O_A(r/2^{r/2})\) and \(O(r\log r/r^3)\).

### Theorem 4.1 (balance on every spine-sparse set)

There is a deterministic outcome of the recursive construction such
that, simultaneously for every \(0\le j\le t\) and every nonempty
spine-sparse \(T\subseteq R_j\),

\[
 \left|\frac{A^{\mathcal F_j}_{|T|}(T)}{\mu_{d_j,|T|}}-1\right|
 \le\varepsilon_j,                                    \tag{4.7}
\]

where

\[
 \varepsilon_0=0,\qquad
 1+\varepsilon_{j+1}=(1+\varepsilon_j)
                          (1+2^{-d_j/8}).              \tag{4.8}
\]

In particular,

\[
                \varepsilon_t\le2t\,2^{-d_0/8}.       \tag{4.9}
\]

#### Proof

At level zero, every permitted nonempty set is a singleton.  Every
cycle contains every singleton, and

\[
                  A^{\mathcal F_0}_1(\{i\})=N_{d_0}=\mu_{d_0,1},
\]

so (4.7) is exact.

Assume (4.7) through level \(j\), write \(d=d_j\), and fix a
spine-sparse \(S\subseteq R_{j+1}\).  Put

\[
                   a=|S\cap L_j|,\qquad b=|S\cap R_j|.            \tag{4.10}
\]

Then \(a,b\le u_j\), so (4.5) permits Lemma 3.1.  If \(b>0\), the
induction hypothesis and (3.5) show that the conditional mean
\(\Lambda=\mathbb EA_{a+b}(S)\) obeys

\[
              \Lambda=(1\pm\varepsilon_j)\mu_{2d,a+b}.           \tag{4.11}
\]

If \(b=0\), the same assertion holds with zero error.

Condition on \(\mathcal F_j\).  The desired load is a sum of \(M\)
independent right-cycle packets \(Z_D\), each bounded by

\[
                         B_d=2^{d-1}.                  \tag{4.12}
\]

For \(b>0\), the induction hypothesis, (4.6), and
\(\binom db\le d^b\) give, for all large \(h\),

\[
       M\ge\frac12\mu_{d,b}
        \ge 2^{d-2-b\log_2d}
        \ge 2^{(1-\zeta_h)d-O(1)}.                    \tag{4.13}
\]

For \(b=0\), the same lower bound follows from \(M=N_d\).
Equations (3.3), (3.4), and \(a+b\le2u_j\) give uniformly

\[
             \frac{\mathbb EZ_D}{B_d}
                \ge(2d)^{-(a+b)}
                \ge2^{-\zeta_h d}.                   \tag{4.14}
\]

Hoeffding's inequality, with \(\delta_j=2^{-d/8}\), now yields

\[
 \Pr\bigl(|A_{a+b}(S)-\Lambda|>\delta_j\Lambda
          \mid\mathcal F_j\bigr)
 \le
 2\exp\left(
 -\frac{2\delta_j^2\Lambda^2}{M B_d^2}
 \right)
 \le 2\exp(-2^{d/2})                                  \tag{4.15}
\]

for all sufficiently large \(h\).  The last inequality follows from
(4.13)--(4.14) and \(\zeta_h=o(1)\).  Combining (4.11) and the successful
event in (4.15) gives exactly the error recurrence (4.8).

There are fewer than \(2^{2d}\) candidate sets at this step.  Therefore
the conditional probability that any spine-sparse candidate fails is at
most

\[
                         2^{2d+1}\exp(-2^{d/2}).       \tag{4.16}
\]

Summing (4.16) over \(j<t\) gives less than one for all large \(h\),
because the smallest dimension is \(d_0\ge r^3\).  Hence one outcome
satisfies every level simultaneously.  Finally,

\[
 \varepsilon_t
 \le \exp\left(\sum_{j<t}2^{-d_j/8}\right)-1
 \le2t\,2^{-d_0/8},
\]

which proves (4.9). \(\square\)

## 5. Counting the exceptional sets

Fix \(1\le q\le A\sqrt h\), and choose a uniform
\(S\in\binom{[h]}q\).  First,

\[
 \Pr(|S\cap R_0|\ge2)
 \le \mathbb E\binom{|S\cap R_0|}{2}
 =\binom{d_0}{2}\frac{q(q-1)}{h(h-1)}.                \tag{5.1}
\]

Let \(B\) be any one of the blocks \(L_j\) or \(R_j\), of size
\(d_j\le h/2\), and put \(X=|S\cap B|\).  For every integer \(u\),

\[
 \Pr(X\ge u)
 \le\mathbb E\binom Xu
 =\binom{d_j}{u}\frac{(q)_u}{(h)_u}.                  \tag{5.2}
\]

Here \((m)_u=m(m-1)\cdots(m-u+1)\) is the falling factorial.

For \(u=u_j\), if \(u_j\le q\), then \(u_j=o(h)\) and

\[
 \binom{d_j}{u_j}\frac{(q)_{u_j}}{(h)_{u_j}}
 \le
 \left(\frac{2e d_jq}{u_jh}\right)^{u_j}
 \le2^{-u_j}\le h^{-8}.                              \tag{5.3}
\]

If \(u_j>q\), the probability is zero.  There are at most \(2t\) blocks
appearing in the spine-sparsity conditions.  Hence the proportion of
non-spine-sparse \(q\)-sets is at most

\[
 \binom{d_0}{2}\frac{q(q-1)}{h(h-1)}+2t h^{-8}.       \tag{5.4}
\]

Theorem 4.1 balances every other set, proving (0.1)--(0.2).  Since
\(d_0<2r^3\), the first term in (5.4), uniformly for
\(q\le A\sqrt h\), is at most

\[
                 \frac{2A^2r^6}{h-1},                \tag{5.5}
\]

which proves (0.4).

## 6. Exact scope and relation to the earlier obstructions

1. **Integrality.**  Every operation partitions a literal product torus,
   so the quotient sets are genuine translates of rainbow path tiles and
   tile \(\mathbb F_2^h/\langle\mathbf1\rangle\) exactly.

2. **Why the fixed-kernel obstruction does not apply.**  The left factor
   over a right cycle \(D\) uses the conjugated Hamming kernel belonging
   to \(\rho_D\).  The choices for different \(D\)'s are independent.
   There is no single syndrome map to which all final rainbow tiles are
   transversals.

3. **Why the fixed-leaf Gaussian obstruction does not apply.**  The
   coordinate conjugation \(\rho_D\) acts on the entire current left
   half and depends on the exterior cycle \(D\).  Thus there is no fixed
   partition into \(Q_4\) leaves whose two forbidden pairs constrain
   every output cycle.  Only the small right-spine anchor is never
   refreshed; a Gaussian-size random direction set hits that anchor
   twice with probability (5.1).

4. **What is proved.**  The direction words of one exact factor give an
   approximate simultaneous \(q\)-cover for every \(q\le A\sqrt h\), and
   almost every \(q\)-set has its correct cycle multiplicity up to the
   vanishing relative error (0.2).

5. **What is not proved.**  Direction-set coverage does not locate the
   starting vertex of a consecutive segment.  Any use toward the sharp
   contiguous-OR constant still needs a separate theorem controlling
   basepoint collisions and the exact target capacities.
