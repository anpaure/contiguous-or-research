# Fixed-annulus partial cyclic packets: exact collision ledgers and the ungrouped Hall theorem

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,
\tag{0.1}
\]

where \(0<a<b<\infty\) are fixed, and write

\[
 N_q=\binom{2m}{m-q}.
\tag{0.2}
\]

The corrected packet mass is

\[
 K=\left\lfloor\frac{N_{q_0}}{2m}\right\rfloor,
 \qquad M=2mK=N_{q_0}-\rho,\qquad 0\le \rho<2m.
\tag{0.3}
\]

For any \(K\) ordinary directed cyclic-order packets, let \(C_{\rm mid}\)
be the repeated-middle-owner mass and let \(h_q\) be the number of missed
lower rank-\((m-q)\) targets.  Complementation makes \(h_q\) also the
number of missed upper targets.  The exact literal ledger is

\[
 \boxed{
 L\le W+2HK+C_{\rm mid}
          +2\sum_{q=q_0}^{H}h_q.}
\tag{0.4}
\]

Thus no near-full middle factor is required.  The precise integral target is

\[
 C_{\rm mid}=o(W),\qquad
 \sum_{q=q_0}^{H}h_q=o(W).
\tag{0.5}
\]

At every depth, if \(L_q(T)\) is the selected occurrence load and

\[
 c_q=\sum_T(L_q(T)-1)_+,
\tag{0.6}
\]

then the exact capacity identity is

\[
 \boxed{c_q-h_q=M-N_q.}
\tag{0.7}
\]

In particular, at the tight first depth,

\[
 h_{q_0}=c_{q_0}+\rho.
\tag{0.8}
\]

There is also an exact floor-correct second-moment certificate.  If
\(M=s_qN_q+r_q\), \(0\le r_q<N_q\), put

\[
 P_q=\sum_T\binom{L_q(T)}2,
 \qquad
 P_q^{\min}=N_q\binom{s_q}{2}+s_qr_q,
 \qquad
 \Phi_q=P_q-P_q^{\min}.
\tag{0.9}
\]

Then \(\Phi_q\ge0\), and whenever \(s_q\ge1\),

\[
 \boxed{h_q\le
   \frac{\Phi_q}{\binom{s_q+1}{2}}.}
\tag{0.10}
\]

For the fixed annulus, \(s_q=O_{a,b}(1)\).  Hence floor-correct pair
excess \(o(W)\), aggregated over the annulus, suffices for (0.5).  The raw
pair baseline itself is \(\Theta_{a,b}(W\sqrt m)\); the required statement
is an \(o(W)\) error around that baseline, not a small raw second moment.

The main structural conclusion is positive but sharply delimited.  If the
requirement that the \(2m\) marked occurrences belonging to one packet come
from one common cyclic order is relaxed, then the entire incidence problem
has an exact integral solution:

* all \(M\) middle owners are distinct;
* exactly \(\rho<2m\) depth-\(q_0\) targets are missed; and
* every target at every depth \(q_0<q\le H\) is hit.

Moreover every one of these nested owner--target flags is individually a
literal occurrence in an ordinary cyclic-order packet.  Therefore there is
no owner Hall cut, no nested-rank Hall cut, and no local-realizability cut.
The sole remaining integrality condition is to group these locally
realizable flags into blocks of \(2m\) which are the rotations of common
cyclic orders.

The packet incidence geometry supports this diagnosis.  At the tight
rank, the packet hypergraph is regular and its largest relative codegree is

\[
 \frac{2}{(m-q_0)(m+q_0)}=(2+o(1))m^{-2}.
\tag{0.11}
\]

After complementary quotienting, the middle-owner hypergraph has largest
nontrivial relative codegree \(2/m^2\).  Thus the singleton/projective-plane
pair obstruction is absent from the two tight layers.  In contrast, the
uncontracted full annulus has adjacent nested relative codegree
\(2/(m-H+1)=\Theta(m^{-1})\); this is the deterministic thread structure
which a successful grouping theorem must preserve rather than treat as
noise.

Independent packet selection fails at exactly the two required scales: it
has \(\Theta(W)\) middle collision mass and
\(\Theta_{a,b}(W\sqrt m)\) aggregate annular holes.  A switch system starting
from such a diffuse seed must consequently replace \(\Theta(K)\) packets;
an \(o(K)\)-packet perturbation cannot work.

No partial packet family satisfying (0.5) is constructed here, and no
coefficient-one conclusion is claimed.

## 1. Packets and loads

A directed cyclic order \(\pi\) is taken modulo rotation, not reversal.  For
\(j\in\mathbb Z_n\), let

\[
 I_\pi(j,r)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+r-1}\}.
\tag{1.1}
\]

Its middle owners and lower depth-\(q\) targets are

\[
 \mathcal O(\pi)=\{I_\pi(j,m):j\in\mathbb Z_n\},
 \qquad
 \mathcal E_q(\pi)=
 \{I_\pi(j,m-q):j\in\mathbb Z_n\}.
\tag{1.2}
\]

All sets in either displayed family are distinct.  Indeed, two distinct
cyclic intervals of a fixed length at most \(m\) have different first
boundary blocks and therefore cannot have the same support.  Also

\[
 I_\pi(j+m,m)=I_\pi(j,m)^c.
\tag{1.3}
\]

Let \(\Pi\) be a multiset of \(K\) packets.  Define

\[
 U(X)=|\{\pi\in\Pi:X\in\mathcal O(\pi)\}|,
\tag{1.4}
\]

\[
 L_q(T)=|\{\pi\in\Pi:T\in\mathcal E_q(\pi)\}|.
\tag{1.5}
\]

Since each packet contributes exactly \(n\) occurrences at each displayed
rank,

\[
 \sum_XU(X)=M,
 \qquad
 \sum_TL_q(T)=M.
\tag{1.6}
\]

Put

\[
 D_{\rm mid}=|\{X:U(X)>0\}|,
 \qquad
 C_{\rm mid}=\sum_X(U(X)-1)_+=M-D_{\rm mid},
\tag{1.7}
\]

and

\[
 D_q=|\{T:L_q(T)>0\}|,
 \qquad h_q=N_q-D_q.
\tag{1.8}
\]

The equality in (1.7) is the exact meaning of middle collision mass.  It
counts the number of repeated occurrences, not merely the number of owner
cells with multiplicity at least two.

## 2. Exact compiler and capacity ledgers

### Theorem 2.1 (partial-packet literal ledger)

The packets in \(\Pi\), supplemented by singleton repairs, produce a literal
middle-plus-fixed-annulus word of length at most (0.4).

#### Proof

The ordinary erosion block of one cyclic order has length \(n+2H\) and
realizes every lower and upper interval through depth \(H\).  Concatenating
the \(K\) blocks costs

\[
 K(n+2H)=M+2HK.
\tag{2.1}
\]

Exactly \(W-D_{\rm mid}\) middle masks have not yet appeared.  Appending
them singly changes the first two terms to

\[
 M+2HK+W-D_{\rm mid}
 =W+2HK+C_{\rm mid}.
\tag{2.2}
\]

At depth \(q\), append each missed lower target and its complement, which is
the corresponding missed upper target.  Explicitly,

\[
 I_\pi(j,m+q)^c=I_\pi(j+m+q,m-q),
\]

so complementation bijects the selected upper support with the selected
lower support.  This costs \(2h_q\).  Summing gives
(0.4).  All witnesses are internal to a packet block or are singleton
repairs, so concatenation cannot destroy them. \(\square\)

Since \(K\le N_{q_0}/n\le W/n\),

\[
 2HK\le\frac HmW=O_{a,b}(W/\sqrt m)=o(W).
\tag{2.3}
\]

Thus (0.5), rather than a near-factor condition, is the exact sufficient
gate.

### Lemma 2.2 (capacity identity)

For every \(q\), (0.7) holds.

#### Proof

For any nonnegative integer load,

\[
 L=\mathbf1_{\{L>0\}}+(L-1)_+.
\]

Summing this identity over all \(N_q\) targets gives

\[
 M=D_q+c_q=N_q-h_q+c_q,
\]

which rearranges to (0.7). \(\square\)

In particular, the first annular layer has no collision reserve: since
\(M=N_{q_0}-\rho\), every repeated tight-layer occurrence creates one
additional hole, on top of the unavoidable \(\rho\) rounding holes.

## 3. The exact floor-correct pair certificate

### Theorem 3.1 (pair excess above the balanced baseline)

Let \(M=sN+r\), \(0\le r<N\), and let \((z_i)_{i=1}^N\) be nonnegative
integer loads with sum \(M\).  Then

\[
 \sum_i\binom{z_i}{2}
 -\left(N\binom{s}{2}+sr\right)
 =\frac12\sum_i(z_i-s)(z_i-s-1)\ge0.
\tag{3.1}
\]

If \(s\ge1\) and \(h=|\{i:z_i=0\}|\), then

\[
 h\binom{s+1}{2}\le
 \sum_i\binom{z_i}{2}
 -\left(N\binom{s}{2}+sr\right).
\tag{3.2}
\]

#### Proof

The algebraic identity follows from

\[
 \binom z2-sz+\binom{s+1}{2}
 =\frac12(z-s)(z-s-1)
\tag{3.3}
\]

and \(M=sN+r\).  For integral \(z-s\), the product of two consecutive
integers \((z-s)(z-s-1)\) is nonnegative.  This proves (3.1).  A zero load
contributes

\[
 \frac12s(s+1)=\binom{s+1}{2}
\]

to the right side, while every other contribution remains nonnegative.
This proves (3.2). \(\square\)

Applying the theorem to (1.5) proves (0.9)--(0.10).  At the rounded tight
layer \(s_{q_0}=0\), one instead has the exact and sufficient estimate

\[
 h_{q_0}=\rho+c_{q_0}\le
 \rho+\sum_T\binom{L_{q_0}(T)}2.
\tag{3.4}
\]

For all sufficiently large \(m\), \(M>N_{q_0+1}\), so \(s_q\ge1\) at
every later controlled depth.  Indeed,

\[
 N_{q_0}-N_{q_0+1}
 =N_{q_0}\frac{2q_0+1}{m+q_0+1}>2m>\rho.
\tag{3.5}
\]

The last strict inequality holds eventually because \(N_{q_0}\) is
exponential in \(m\), whereas the remaining factor is of order
\(m^{-1/2}\).

For the middle layer, define

\[
 P_{\rm mid}=\sum_X\binom{U(X)}2.
\tag{3.6}
\]

Since \(u-1\le\binom u2\) for every positive integer \(u\),

\[
 C_{\rm mid}\le P_{\rm mid}.
\tag{3.7}
\]

Consequently the explicit condition

\[
 P_{\rm mid}
 +\sum_T\binom{L_{q_0}(T)}2
 +\sum_{q=q_0+1}^{H}
   \frac{\Phi_q}{\binom{s_q+1}{2}}
 =o(W)
\tag{3.8}
\]

implies (0.5).  The term \(\rho=O(m)=o(W)\) is harmless.

### Proposition 3.2 (Gaussian scale of the raw pair baseline)

Uniformly for \(q=x\sqrt m+O(1)\), \(a\le x\le b\),

\[
 \frac{N_q}{W}=e^{-x^2+O_{a,b}(m^{-1/2})},
 \qquad
 \frac{M}{N_q}=e^{x^2-a^2+O_{a,b}(m^{-1/2})}.
\tag{3.9}
\]

Moreover

\[
 \sum_{q=q_0}^{H}P_q^{\min}
 =\bigl(\mathcal P_{a,b}+o(1)\bigr)W\sqrt m,
\tag{3.10}
\]

where, with \(\lambda(x)=e^{x^2-a^2}\) and
\(s(x)=\lfloor\lambda(x)\rfloor\),

\[
 \mathcal P_{a,b}
 =\int_a^b e^{-x^2}
 \left[
  \binom{s(x)}2+s(x)(\lambda(x)-s(x))
 \right],dx>0.
\tag{3.11}
\]

#### Proof

The product formula

\[
 \frac{N_q}{W}=\prod_{i=1}^{q}\frac{m-i+1}{m+i}
\tag{3.12}
\]

gives

\[
 \log\frac{N_q}{W}
 =-\frac1m\sum_{i=1}^{q}(2i-1)
   +O\left(\frac1{m^2}\sum_{i=1}^{q}i^2\right)
 =-\frac{q^2}{m}+O_{a,b}(m^{-1/2}).
\tag{3.13}
\]

This proves (3.9), since \(M/N_{q_0}=1+o(1)\).  At all \(x\) for which
\(\lambda(x)\) is not an integer, \(s_q=s(x)\) eventually, and

\[
 \frac{P_q^{\min}}W
 =e^{-x^2}
 \left[
  \binom{s(x)}2+s(x)(\lambda(x)-s(x))
 \right]+o(1).
\tag{3.14}
\]

There are only finitely many integer-threshold points on the compact
interval, and all summands are uniformly bounded.  Riemann summation proves
(3.10)--(3.11).  The integrand is positive except at the left endpoint and
possibly isolated threshold points, so the integral is positive. \(\square\)

Thus a successful partial packet construction must control pair collisions
to absolute error \(o(W)\) around a \(\Theta(W\sqrt m)\) floor baseline.
Raw pair-smallness is the wrong target beyond the tight first layer.

## 4. Diffuse packet selection fails, and sparse switching cannot repair it

Choose \(K\) packets independently and uniformly from all directed cyclic
orders, allowing repetitions.  A fixed middle owner belongs to one packet
with probability \(n/W\), while a fixed depth-\(q\) target belongs with
probability \(n/N_q\).  Therefore

\[
 \mathbb E C_{\rm mid}
 =M-W\left[1-\left(1-\frac nW\right)^K\right],
\tag{4.1}
\]

and

\[
 \mathbb E h_q
 =N_q\left(1-\frac n{N_q}\right)^K.
\tag{4.2}
\]

Put \(\alpha=e^{-a^2}\).  Equations (3.9), (4.1), and (4.2) give

\[
 \frac{\mathbb E C_{\rm mid}}W
 \longrightarrow \alpha-1+e^{-\alpha}>0,
\tag{4.3}
\]

and

\[
 \frac1{W\sqrt m}
 \sum_{q=q_0}^{H}\mathbb E h_q
 \longrightarrow
 \int_a^b
 e^{-x^2-e^{x^2-a^2}}\,dx>0.
\tag{4.4}
\]

The convergence is uniform because \(n/N_q\) is exponentially small and
\(K(n/N_q)^2=o(1)\) throughout the fixed annulus.  Thus independent
selection loses a constant fraction of middle collision mass and a constant
fraction of every annular target layer.

There is also a deterministic edit lower bound.  Suppose two \(K\)-packet
multisets differ by replacing \(t\) packets.  A replacement changes the
middle support size by at most \(n\), and changes the support size at each
depth by at most \(n\).  Hence

\[
 |C_{\rm mid}(\Pi)-C_{\rm mid}(\Pi')|\le nt,
\tag{4.5}
\]

\[
 \left|
  \sum_{q=q_0}^{H}h_q(\Pi)
 -\sum_{q=q_0}^{H}h_q(\Pi')
 \right|
 \le n(H-q_0+1)t.
\tag{4.6}
\]

Consequently a diffuse seed exhibiting the scales (4.3)--(4.4) cannot be
repaired by \(o(W/n)=o(K)\) packet replacements.  Any two-seed component
construction based on such a seed must switch a positive proportion of its
packet columns.  This does not obstruct a genuinely macroscopic correlated
overlay.

## 5. Exact ungrouped Hall feasibility

We now remove only one condition: the \(n\) marked occurrences are not yet
required to come in rotation classes of a common cyclic order.

### Lemma 5.1 (rank-surjective deletion maps)

For every \(0\le r<m\), there is a map

\[
 f_{r+1}:\binom{[n]}{r+1}\longrightarrow\binom{[n]}r
\tag{5.1}
\]

such that \(f_{r+1}(A)\subset A\) and \(f_{r+1}\) is onto.

#### Proof

In the inclusion bipartite graph between ranks \(r\) and \(r+1\), every
lower vertex has degree \(n-r\), and every upper vertex has degree \(r+1\).
For a lower family \(\mathcal A\), edge counting gives

\[
 (n-r)|\mathcal A|\le(r+1)|N(\mathcal A)|.
\tag{5.2}
\]

Since \(r<m=n/2\), the right-neighborhood has size at least
\(|\mathcal A|\).  Hall's theorem gives an injection

\[
 j_r:\binom{[n]}r\hookrightarrow\binom{[n]}{r+1},
 \qquad A\subset j_r(A).
\tag{5.3}
\]

Set \(f_{r+1}(j_r(A))=A\), and send every unmatched upper set to any one
of its \(r\)-subsets.  The resulting map is onto. \(\square\)

### Lemma 5.2 (distinct middle extensions)

Every family \(\mathcal A\subseteq\binom{[n]}{m-q_0}\) can be injected into
the middle rank by a containment map

\[
 g:\mathcal A\hookrightarrow\binom{[n]}m,
 \qquad T\subset g(T).
\tag{5.4}
\]

#### Proof

In the containment bipartite graph, a lower vertex has degree

\[
 d_- =\binom{m+q_0}{q_0},
\]

and a middle vertex has degree

\[
 d_+=\binom m{q_0}.
\]

For \(\mathcal B\subseteq\mathcal A\), edge counting gives

\[
 d_-|\mathcal B|\le d_+|N(\mathcal B)|.
\tag{5.5}
\]

Here

\[
 \frac{d_-}{d_+}=\frac W{N_{q_0}}>1,
\tag{5.6}
\]

by the total edge count in the full two ranks.  Thus Hall's condition holds
and proves the injection. \(\square\)

### Theorem 5.3 (zero-collision, zero-deeper-hole ungrouped flags)

For all sufficiently large \(m\), there are \(M\) nested flags

\[
 X(T)\supset T_{q_0}(T)\supset T_{q_0+1}(T)\supset
 \cdots\supset T_H(T),
\tag{5.7}
\]

with \(|X(T)|=m\), \(|T_q(T)|=m-q\), having the following properties.

1. The \(X(T)\)'s are all distinct.
2. The \(T_{q_0}(T)\)'s are all distinct and miss exactly \(\rho\) members
   of rank \(m-q_0\).
3. For every \(q_0<q\le H\), the multiset of \(T_q(T)\)'s covers the
   entire rank \(m-q\).
4. Every individual flag (5.7) occurs at one marked start of an ordinary
   directed cyclic-order packet.

#### Proof

Put \(r_0=m-q_0\) and \(r_1=r_0-1\).  By (3.5),

\[
 M\ge N_{q_0+1}
\tag{5.8}
\]

for all sufficiently large \(m\).  Choose the Hall injection \(j_{r_1}\)
from Lemma 5.1 and select an \(M\)-set

\[
 \mathcal A_0\subseteq\binom{[n]}{r_0}
\]

which contains its image.  The corresponding surjection \(f_{r_0}\)
therefore maps \(\mathcal A_0\) onto the whole rank \(r_1\).

For \(T\in\mathcal A_0\), set

\[
 T_{q_0}(T)=T,
 \qquad
 T_{q+1}(T)=f_{m-q}(T_q(T)).
\tag{5.9}
\]

The first image is the whole rank \(r_1\).  Inductively, whenever all sets
of rank \(m-q\) occur, the surjectivity of \(f_{m-q}\) implies that all sets
of rank \(m-q-1\) occur at the next depth.  This proves properties 2 and 3.

Apply Lemma 5.2 to \(\mathcal A_0\), and put \(X(T)=g(T)\).  This proves
property 1.

It remains to verify literal local realizability.  List the \(q_0\) elements
of \(X(T)\setminus T_{q_0}(T)\) in any order.  For
\(q_0\le q<H\), let \(z_q\) be the unique element of

\[
 T_q(T)\setminus T_{q+1}(T).
\]

Around a directed circle, place consecutively:

1. the ordered elements of \(X(T)\setminus T_{q_0}(T)\);
2. \(z_{q_0},z_{q_0+1},\ldots,z_{H-1}\);
3. the elements of \(T_H(T)\), in any order; and
4. the elements outside \(X(T)\), in any order.

At the start of the first block, the length-\(m\) interval is \(X(T)\).
After shifting the start by \(q\) positions and shortening the interval to
length \(m-q\), the interval is exactly \(T_q(T)\).  Thus one marked start
of this cyclic order realizes (5.7). \(\square\)

The theorem is deliberately stronger than fractional feasibility: after
ungrouping, it has exact integral owner disjointness and exact deeper-rank
coverage.  It also identifies the remaining condition exactly.  One must
partition the \(M\) marked flags into \(K\) classes of size \(n\) such that
the flags in each class are all cyclic rotations of one common order.  The
local embeddings constructed in the proof need not agree away from their
marked starts, so they do not supply that partition.

## 6. Exact tight-layer packet codegrees

The following count records why no ordinary pair-codegree cut appears at
the two tight incidence layers.

### Lemma 6.1 (two equal-length cyclic intervals)

Let \(1\le r<m\), and let \(A,B\) be distinct \(r\)-sets.  Put
\(d=|A\setminus B|\).  A fixed \(r\)-set occurs as an interval in

\[
 D_r=r!(n-r)!
\tag{6.1}
\]

directed cyclic orders modulo rotation.  If \(1\le d<r\), the normalized
codegree of \(A,B\) is

\[
 \frac{D(A,B)}{D_r}
 =\frac{2}{\binom rd\binom{n-r}d}.
\tag{6.2}
\]

If \(d=r\), then

\[
 \frac{D(A,B)}{D_r}
 =\frac{n-2r+1}{\binom{n-r}r}.
\tag{6.3}
\]

#### Proof

Contracting the prescribed interval gives (6.1).  Condition on \(A\) being
the anchored interval.  If \(0<|A\cap B|<r\), the interval \(B\) must cross
one of the two boundaries of \(A\).  For either boundary, its prescribed
\(r-d\) elements in \(A\) occupy the corresponding end block with
probability \(1/\binom rd\), and its prescribed \(d\) outside elements
occupy the adjacent block with probability \(1/\binom{n-r}d\).  The two
events are disjoint, proving (6.2).

If \(A\cap B=\varnothing\), the set \(B\) can occupy any of the
\(n-2r+1\) consecutive length-\(r\) position blocks in the linear
complement of \(A\).  These events are disjoint and each has probability
\(1/\binom{n-r}r\), proving (6.3). \(\square\)

For \(r=m-q_0\), the product of binomial coefficients in (6.2) is at least
\(r(n-r)\), with equality at \(d=1\).  Since \(q_0\to\infty\), (6.3) is
smaller for all sufficiently large \(m\).  Therefore the rank-\(q_0\)
packet hypergraph is \(n\)-uniform, regular, and has exact maximum relative
codegree

\[
\frac{2}{r(n-r)}
=\frac{2}{(m-q_0)(m+q_0)}.
\tag{6.4}
\]

This hypergraph also has the exact fractional point at the corrected packet
mass.  Assign every directed cyclic order weight \(1/D_r\).  Every tight
target then has load one, while the total packet weight is

\[
 \frac{(n-1)!}{D_r}=\frac{N_{q_0}}n.
\tag{6.4a}
\]

A fixed middle owner has load

\[
 \frac{(m!)^2}{D_r}=\frac{N_{q_0}}W
 =e^{-a^2+o(1)}<1.
\tag{6.4b}
\]

Thus the uniform fractional tight-layer cover already respects every
middle-owner capacity with constant slack.  The missing statement is
integral grouping, not a fractional owner overload.

At the middle rank one must first identify \(X\) with \(X^c\), since every
packet contains both.  On complementary atoms the packet has size \(m\).
For two distinct atoms represented by middle sets at Johnson distance
\(d<m\), the same count gives relative codegree

\[
 \frac{2}{\binom md^2}\le\frac2{m^2}.
\tag{6.5}
\]

For a tight target \(T\subset X\), the owner--target codegree is

\[
 D(X,T)=(q_0+1)(m-q_0)!q_0!m!,
\tag{6.6}
\]

so, relative respectively to target and owner degree, it is

\[
 \frac{q_0+1}{\binom{m+q_0}{q_0}},
 \qquad
 \frac{q_0+1}{\binom m{q_0}}.
\tag{6.7}
\]

These are much smaller than \(m^{-2}\) at Gaussian \(q_0\).  Thus pair
overlap does not supply a two-layer Hall obstruction.

There is, however, a deterministic distinction between the tight two-layer
problem and the full annulus.  A target of size \(m-q\) nested immediately
inside a target of size \(m-q+1\) has relative packet codegree

\[
 \frac2{m-q+1}.
\tag{6.8}
\]

Maximizing over \(q\le H\) gives \(2/(m-H+1)\).  These large codegrees are
exactly the left/right continuations of one interval thread.  A generic
one-shot matching theorem on the union of all annular target vertices sees
them as collisions, although a desired packet must contain them.  The
appropriate remaining theorem must first retain or contract the nested
threads and then solve the common-cycle grouping problem.

## 7. Tight-layer cycle normal form and the exact two-seed overlay

The common-cycle grouping condition can be written entirely at the tight
target rank.  Put \(r_0=m-q_0\), and for one packet define

\[
 V_j=I_\pi(j+q_0,r_0),\qquad j\in\mathbb Z_n.
\tag{7.1}
\]

Thus \((V_j)\) is the packet's cyclic list of tight targets, with the index
chosen so that \(V_j\) belongs to the owner starting at \(j\).

### Lemma 7.1 (all deeper targets and owners are forced by the tight cycle)

For \(0\le d\le H-q_0\),

\[
 I_\pi(j+q_0+d,r_0-d)
 =\bigcap_{t=0}^{d}V_{j+t},
\tag{7.2}
\]

and

\[
 I_\pi(j,m)
 =\bigcup_{t=0}^{q_0}V_{j-q_0+t}.
\tag{7.3}
\]

If \(a_j=\pi_{j+q_0}\), then \((a_j)_{j\in\mathbb Z_n}\) is a cyclic
permutation of \([n]\) and

\[
 V_j=\{a_j,a_{j+1},\ldots,a_{j+r_0-1}\},
 \qquad
 V_{j+1}=V_j-a_j+a_{j+r_0}.
\tag{7.4}
\]

Conversely, every cyclic permutation \((a_j)\) and the window rule (7.4)
produce one ordinary cyclic-order packet, and (7.2)--(7.3) recover all of
its controlled targets and owners.

#### Proof

The intervals \(V_j,\ldots,V_{j+d}\) have successively increasing left and
right endpoints.  The largest left endpoint is \(j+q_0+d\), while the
smallest right endpoint is \(j+m-1\).  Their intersection is therefore the
interval between those endpoints, proving (7.2).  The
intervals \(V_{j-q_0},\ldots,V_j\) have union from \(j\) through
\(j+m-1\), proving (7.3).  Equation (7.4) is immediate from the definition
of \(a_j\), and its converse reconstructs the cyclic coordinate order.
\(\square\)

Hence the partial-family problem is exactly a special cycle-decomposition
problem on rank \(r_0\): partition almost all tight targets into
length-\(n\) sliding-window cycles, while requiring the consecutive
intersection supports (7.2) and consecutive union supports (7.3) to have
the defects in (0.5).

There is a physical two-seed component overlay at precisely this level.

### Proposition 7.2 (common-tight-base two-seed component switches)

Let \(\mathscr A\) and \(\mathscr B\) each consist of \(K\) packets, and
suppose that within each family the tight target sets are disjoint and that
both families cover the same tight target set \(\mathcal S\) of size
\(M=nK\).  Form the bipartite multigraph \(G\) whose left vertices are the
packets of \(\mathscr A\), whose right vertices are the packets of
\(\mathscr B\), and whose edge labelled \(T\in\mathcal S\) joins the unique
packets containing \(T\).

Then every vertex of \(G\) has degree \(n\).  In each connected component
\(C\), the number of left packet vertices equals the number of right packet
vertices.  Independently for every component, choose either all its left
packets or all its right packets.  The selected packets then:

1. number exactly \(K\);
2. partition \(\mathcal S\) at the tight target layer; and
3. form a literal physical partial cyclic-packet family whose middle and
   deeper loads are given by (7.2)--(7.3).

#### Proof

A packet contains exactly \(n\) tight targets, so \(G\) is \(n\)-regular
on both shores.  If a connected component has \(u\) left vertices and
\(v\) right vertices, counting its labelled target edges from both shores
gives \(nu=nv\), hence \(u=v\).  Every target edge lies wholly inside one
component.  Choosing one shore therefore selects its label exactly once.
Summing \(u=v\) over components preserves the packet count \(K\).  Each
selected column is an unchanged ordinary packet, so literal legality and
(7.2)--(7.3) are automatic. \(\square\)

This is the exact partial-family analogue of a two-factor component switch;
it does not require a middle wreath factor.  It also gives a sharp warning.
If \(G\) is connected, the overlay has only its two endpoint families and
cannot create a third target profile.  Useful averaging requires many
components or more than two common-tight-base decompositions.  Conversely,
any such component choice keeps the tight-layer collision and hole terms
identically fixed, so all available freedom acts directly on the middle
unions and deeper consecutive intersections which remain to be balanced.

The resulting floor-correct contraction test is completely explicit.  For
a component \(C\), let \(u_C^A,u_C^B\) be its two middle-owner load vectors,
and let \(f_{C,q}^A,f_{C,q}^B\) be its two depth-\(q\) target-load vectors.
Put

\[
 \bar u=\frac12\sum_C(u_C^A+u_C^B),\qquad
 \delta_C^0=u_C^A-u_C^B,
\tag{7.5}
\]

\[
 \bar f_q=\frac12\sum_C(f_{C,q}^A+f_{C,q}^B),\qquad
 \delta_C^q=f_{C,q}^A-f_{C,q}^B.
\tag{7.6}
\]

### Theorem 7.3 (baseline-correct common-base contraction criterion)

Choose the two shores of the components independently and fairly.  Then

\[
 \mathbb E P_{\rm mid}
 =\frac12(\|\bar u\|_2^2-M)
   +\frac18\sum_C\|\delta_C^0\|_2^2,
\tag{7.7}
\]

and, for every \(q_0<q\le H\),

\[
 \mathbb E\Phi_q
 =\frac12(\|\bar f_q\|_2^2-M)-P_q^{\min}
   +\frac18\sum_C\|\delta_C^q\|_2^2.
\tag{7.8}
\]

Every right side is nonnegative.  If

\[
 \frac12(\|\bar u\|_2^2-M)
 +\frac18\sum_C\|\delta_C^0\|_2^2
 +\sum_{q=q_0+1}^{H}
  \frac{
   \frac12(\|\bar f_q\|_2^2-M)-P_q^{\min}
   +\frac18\sum_C\|\delta_C^q\|_2^2
  }{\binom{s_q+1}{2}}
 =o(W),
\tag{7.9}
\]

then some integral component choice satisfies

\[
 C_{\rm mid}=o(W),\qquad
 h_{q_0}=\rho<2m,\qquad
 \sum_{q=q_0+1}^{H}h_q=o(W).
\tag{7.10}
\]

It consequently gives a literal fixed-annulus word of length \(W+o(W)\).

#### Proof

Write the random middle load as

\[
 u=\bar u+\frac12\sum_C\varepsilon_C\delta_C^0,
\]

where the \(\varepsilon_C\)'s are independent uniform signs.  Since every
component has equally many packets on its two shores, every child has total
middle load \(M\).  Hence

\[
 P_{\rm mid}=\frac12(\|u\|_2^2-M).
\]

Orthogonality of the independent signs proves (7.7).  The same argument at
depth \(q\), followed by subtraction of the constant \(P_q^{\min}\), proves
(7.8).  Both random variables on the left are nonnegative, proving the
asserted nonnegativity of the right sides.

Let

\[
 Z=P_{\rm mid}
  +\sum_{q=q_0+1}^{H}
    \frac{\Phi_q}{\binom{s_q+1}{2}}.
\]

Equation (7.9) says \(\mathbb EZ=o(W)\), so at least one integral shore
choice has \(Z=o(W)\).  Equations (3.7) and (0.10) then prove every term in
(7.10) except the tight one.  Proposition 7.2 partitions a fixed
\(M\)-element tight base for every shore choice, so its tight hole count is
always \(N_{q_0}-M=\rho\).  The compiler conclusion follows from Theorem
2.1. \(\square\)

Criterion (7.9) is physical and baseline-correct: it subtracts the exact
balanced pair count \(P_q^{\min}\), while its variance terms are computed
from literal owner unions and consecutive target intersections.  It is not
satisfied merely by having many components.  A construction still has to
make the barycentric terms and all component scatter terms jointly cancel
to \(o(W)\).

There is a sharper equality audit when the two endpoint ledgers are
simple.  It explains how strong the required component alignment is.

### Proposition 7.4 (exact simple-target alignment law)

Assume the two seed families are middle-simple: no middle owner occurs
twice within either seed.  For a middle owner \(X\) occurring in both
seeds, let \(C_A(X)\) and \(C_B(X)\) be the overlay components containing
its two packet occurrences.  Under independent fair component choices,

\[
 \boxed{
 \mathbb E C_{\rm mid}
 ={1\over4}
 \bigl|\{X:X\hbox{ occurs in both seeds and }
              C_A(X)\ne C_B(X)\}\bigr|.}
\tag{7.11}
\]

Fix a deeper depth \(q\), and suppose additionally that the load of every
target is zero or one in each seed.  Partition the targets into four
classes:

\[
\begin{aligned}
 Z_q&=\{T:T\hbox{ occurs in neither seed}\},\\
 E_q&=\{T:T\hbox{ occurs in exactly one seed}\},\\
 D_q&=\{T:T\hbox{ occurs once in both seeds, in different components}\},\\
 S_q&=\{T:T\hbox{ occurs once in both seeds, in the same component}\}.
\end{aligned}
\tag{7.12}
\]

Then

\[
 \boxed{\mathbb E h_q=|Z_q|+\frac12|E_q|+\frac14|D_q|.}
\tag{7.13}
\]

In particular, product component heat has aggregate middle collision and
simple-target holes \(o(W)\) only if all but \(o(W)\) of the shared
occurrences are paired inside the same ownership component, while the
one-seed-only and zero-seed target classes have total size \(o(W)\).

#### Proof

If \(X\) occurs in both seeds in the same component, choosing either shore
selects exactly one of its two occurrences.  If the occurrences lie in
different components, their two selection indicators are independent fair
bits, so both are selected with probability \(1/4\).  An owner occurring in
only one seed can never collide.  Summation proves (7.11).

For a target in \(Z_q\), the miss probability is one.  In \(E_q\), its
unique occurrence is selected with probability \(1/2\).  In \(D_q\), the
two occurrence indicators belong to different components; both are absent
with probability \(1/4\).  In \(S_q\), either shore of the common component
contains the target, so it is never missed.  This proves (7.13). \(\square\)

The law remains restrictive even for individually floor-balanced seeds.
Suppose \(1\le M/N_q<3/2\) and each seed has only loads one and two at
depth \(q\).  Exactly \(2N_q-M\) targets have load one in each seed.
Therefore at least

\[
 (3N_q-2M)_+
\tag{7.14}
\]

targets have load one in both seeds.  On the fixed interval of Gaussian
depths satisfying

\[
 e^{q^2/m-a^2}<3/2,
\tag{7.15}
\]

the sum of the lower bound (7.14) is \(\Theta_{a,b}(W\sqrt m)\), provided
that interval has positive length.  Hence an \(o(W)\) product-heat proof
must align the common components of all but \(o(W)\) among a
\(\Theta(W\sqrt m)\)-sized collection of unique target occurrences.
Uniform first marginals or mere fragmentation do not imply this alignment.

## 8. Precise boundary

Proved here:

1. the exact partial-family compiler ledger (0.4);
2. the exact collision--hole identity (0.7);
3. the floor-correct pair-excess certificate (0.10), including its
   \(\Theta(W\sqrt m)\) raw baseline;
4. the \(\Theta(W)\) middle and \(\Theta(W\sqrt m)\) annular failure of
   independent packet selection;
5. the necessity of \(\Theta(K)\)-scale switching from a diffuse seed;
6. an exact integral solution of all owner, nesting, coverage, and local
   cyclic-realizability constraints after relaxing common-cycle grouping;
7. exact tight-layer degrees and codegrees, showing no pairwise Hall cut;
   and
8. the tight-cycle normal form and an exact common-base two-seed component
   switch which preserves the minimal tight-layer packet mass; and
9. the exact baseline-correct contraction criterion (7.9) for that physical
   overlay class; and
10. the simple-target component-alignment identities (7.11)--(7.13).

Not proved here:

1. a grouping of the ungrouped flags into \(K\) common cyclic orders;
2. a two-seed component switch which performs that grouping while preserving
   the floor baseline at every annular depth; or
3. a partial packet family satisfying (0.5).

Accordingly the sharp next statement is a **common-cycle grouping theorem**:
group \(M=N_{q_0}+O(m)\) locally realizable nested flags into
\(K=N_{q_0}/(2m)+O(1)\) rotation classes, with \(o(W)\) discarded or
duplicated middle owners and \(o(W)\) total loss of target support.  No
weaker statewise Hall, pair-codegree, or independent-rounding statement can
close the fixed-annulus gate.
