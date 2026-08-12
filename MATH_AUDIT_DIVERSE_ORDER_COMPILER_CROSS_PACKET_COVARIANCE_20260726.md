# Audit of the diverse-order compiler packet factor and its cross-packet covariance gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

The substantive claims of

\[
\texttt{MATH\_THEOREM\_DIVERSE\_ORDER\_COMPILER\_PACKET\_FACTOR\_20260726.md}
\]

are correct, with the coordinate-disjoint Johnson interface stated in
the cited compiler theorem retained literally.

For

\[
 n=4\cdot2^t\asymp\sqrt{mH},\qquad R=2n,
 \qquad H=o(R),\quad R=o(m),                         \tag{0.1}
\]

the parity-complete paired-order compiler factors every \(Q_R\) exactly
into isometric \(C_{2R}\)'s and has injective lower and upper literal
trace maps, in both orientations and from every phase, through every
depth \(q\le H\).  The rank-twisted packet tiling leaves \(o(W/H)\)
owners, and the number of cycles is

\[
                         {G\over2R}=o(W/H).          \tag{0.2}
\]

Thus there are genuinely no within-packet repeats.  The common-order
syndrome obstruction is inapplicable to this factor.

The remaining cross-packet problem has the following exact one-point
kernel.  For a fixed packet and a uniform affine conjugate of its compiler,
every compatible physical \(q\)-face is selected with probability

\[
                         \theta_{R,q}
 = {2^q\over\binom Rq}.                              \tag{0.3}
\]

If \(d_q^\pm(T)\) is the number of retained packets in which \(T\) is a
compatible physical \(q\)-face, its fractional load is

\[
                         \lambda_q^\pm(T)
 =\theta_{R,q}d_q^\pm(T),\qquad
 \sum_T\lambda_q^\pm(T)=G.                          \tag{0.4}
\]

This exact twirl does not solve covariance.  At a fixed Gaussian depth
\(q=A\sqrt m+O(1)\), independent uniform conjugates leave
\(\Omega_A(W)\) targets uncovered with probability

\[
                         1-\exp\{-2^{\,2m-R-o(m)}\}. \tag{0.5}
\]

Hence the required negative covariance must be an order-\(W\), genuinely
correlated effect.

There is also an exact axis-selection warning.  The scale
\(R\asymp\sqrt{mH}\) still permits the localized-axis construction.  If
almost all retained axes are chosen inside one carrier of size
\(\Theta(R)\), then at \(q=A\sqrt m\) both signs miss
\((1-o(1))N_q\) targets, because

\[
                         \exp(-c q^2/R)
 =\exp\!\left(-\Theta\!\left(\sqrt{m/H}\right)\right)=o(1).
                                                               \tag{0.6}
\]

Thus the diverse compiler closes the local factor gate but does not make
an arbitrary rank-twisted axis selector safe.

The sharp remaining constructive object is a dispersed common-block
option array whose Latin column-square term attains the integer-minimal
target variance simultaneously in \(q\) and sign.  Sections 5--6 state
that condition exactly.

## 1. Line-by-line audit of the local and owner claims

Choose \(n=4\cdot2^t\) least with \(n\ge\sqrt{mH}\), and put \(R=2n\).
Then

\[
 \sqrt{mH}\le n<2\sqrt{mH},\qquad
 2\sqrt{mH}\le R<4\sqrt{mH}.                        \tag{1.1}
\]

Since \(H=o(m)\),

\[
 {R\over H}\ge2\sqrt{m/H}\longrightarrow\infty,
 \qquad
 {R\over m}<4\sqrt{H/m}\longrightarrow0.            \tag{1.2}
\]

The cited parity-complete theorem gives an exact \(C_{4n}=C_{2R}\)
factor of \(Q_{2n}=Q_R\).  Its literal physical trace-rainbow range is

\[
                         1\le q\le {n\over2}-1.      \tag{1.3}
\]

Equation (1.2) implies \(H\le n/2-1\) for all large \(m\).  Therefore
every protected lower and upper trace is injective on all \(2^R\)
packet owners.  This verifies

\[
                         |I_{P,q}^\pm|=2^R.          \tag{1.4}
\]

The coordinate-disjoint qualification is essential but satisfied:
the active axes of a rank-twisted product cell are disjoint physical
matching edges.  A varied edge contributes neither endpoint to a lower
intersection and both endpoints to an upper union, so the literal target
recovers the varied directions and the outside orientations exactly.

Because \(R=o(m)\), the low-dimensional product cells in the
rank-twisted decomposition contain \(2^{m+o(m)}=o(W/H)\) middle owners.
Every retained \(Q_S\), \(S\ge R\), partitions exactly into parallel
\(Q_R\)'s.  Installing the exact compiler in each fibre gives

\[
                         G=W-o(W/H)                 \tag{1.5}
\]

covered owners, with no internal completion leave.

Finally, \(R\) is a power of two and \(2R\mid2^R\).  The cycle count is

\[
                         M={G\over2R},\qquad
 {M\over W/H}={H\over2R}{G\over W}=o(1).            \tag{1.6}
\]

Thus an \(O(H)\)-per-cycle interface charge would be \(o(W)\).  This is
an accounting statement only; no interface operation is needed inside
the already complete factors.

## 2. Exact affine-twirl kernel for one packet

Fix a retained physical packet \(P\cong Q_R\), one sign, and one
\(q\le H\).  Let \(F_{P,q}^\pm\) be the target image of one installed
compiler factor.  By (1.4),

\[
                         |F_{P,q}^\pm|=2^R.          \tag{2.1}
\]

The physical \(q\)-faces of \(Q_R\) form one orbit under

\[
                         \Gamma_R=\mathbb F_2^R\rtimes S_R.      \tag{2.2}
\]

Their number is

\[
                         \binom Rq2^{R-q}.           \tag{2.3}
\]

Double-counting pairs \((g,Q)\) with
\(Q\in gF_{P,q}^\pm\) gives, for every physical face \(Q\),

\[
 {|\{g\in\Gamma_R:Q\in gF_{P,q}^\pm\}|\over|\Gamma_R|}
 ={2^R\over\binom Rq2^{R-q}}
 ={2^q\over\binom Rq}
 =\theta_{R,q}.                                     \tag{2.4}
\]

The same conjugate is a legal exact owner factor at all depths and both
signs.  Equation (2.4) is a simultaneous marginal identity, not
permission to choose a different conjugate for every target.

For a global literal target \(T\), let

\[
 b_{P,q}^\pm(T)=
 \begin{cases}
 1,&T\text{ is a physical signed }q\text{-face of }P,\\
 0,&\text{otherwise}.
 \end{cases}                                        \tag{2.5}
\]

If \(g_P\) is uniform on \(\Gamma_R\), then

\[
 \Pr(T\in g_PF_{P,q}^\pm)
 =\theta_{R,q}b_{P,q}^\pm(T).                       \tag{2.6}
\]

Writing

\[
 d_q^\pm(T)=\sum_Pb_{P,q}^\pm(T),\qquad
 \lambda_q^\pm(T)=\theta_{R,q}d_q^\pm(T),            \tag{2.7}
\]

and summing first over targets and then over packets yields

\[
 \sum_T\lambda_q^\pm(T)
 =\sum_P|F_{P,q}^\pm|
 =G.                                                \tag{2.8}
\]

At \(q=A\sqrt m+O(1)\),

\[
 {1\over N_q}\sum_T\lambda_q^\pm(T)
 ={G\over N_q}
 =e^{A^2+o(1)}.                                     \tag{2.9}
\]

This verifies the complete fractional mass, but says nothing about the
lower tail of \(\lambda_q^\pm(T)\) or integral coverage.

## 3. Independent conjugates have a linear hole count

We now prove a pointwise no-go for the most natural random rounding of
the twirl.

### Theorem 3.1 (independent-twirl Poisson floor)

Fix \(q=A\sqrt m+O(1)\le H\), \(A>0\), and any retained packet family
with arbitrary physical axes and frozen labels.  Choose the affine
compiler conjugates independently and uniformly in the different
packets.  Then, for either sign, there is a constant \(c_A>0\) such that

\[
 \Pr(M_q^\pm\ge c_AW)
 \ge1-\exp\{-2^{\,2m-R-o(m)}\}.                     \tag{3.1}
\]

#### Proof

First,

\[
 \theta_{R,q}
 ={2^q\over\binom Rq}
 \le\left({2q\over R-q+1}\right)^q=o(1),             \tag{3.2}
\]

because \(q/R=O(H^{-1/2})\to0\).

Put \(\bar\lambda=G/N_q=e^{A^2+o(1)}\).  By (2.8), at least \(N_q/2\)
targets satisfy

\[
                         \lambda_q^\pm(T)\le2\bar\lambda.        \tag{3.3}
\]

For such a target, independence and (2.6) give

\[
 \begin{aligned}
 \Pr(T\text{ is missed})
 &=(1-\theta_{R,q})^{d_q^\pm(T)}\\
 &\ge\exp\!\left(-{\lambda_q^\pm(T)\over1-\theta_{R,q}}\right)\\
 &\ge\exp(-2e^{A^2}-o(1)).                          \tag{3.4}
 \end{aligned}
\]

Consequently

\[
                         \mathbb E M_q^\pm\ge c'_AW \tag{3.5}
\]

for some \(c'_A>0\).

Changing the conjugate in one packet can alter the missed/not-missed
status of at most \(2^{R+1}\) targets.  There are \(G/2^R\) packets.
McDiarmid's inequality therefore gives

\[
 \Pr\!\left(M_q^\pm\le{\mathbb EM_q^\pm\over2}\right)
 \le
 \exp\!\left(
 -\Omega_A\!\left({W^2\over(G/2^R)2^{2R}}\right)\right)
 =\exp\{-2^{\,2m-R-o(m)}\}.                         \tag{3.6}
\]

Take \(c_A=c'_A/2\).  \(\square\)

The theorem does not rule out a correlated deterministic choice.  It
proves that marginal regularity plus independent packet rounding cannot
be the missing argument.

## 4. A legal cross-packet Hall catastrophe remains

The diverse compiler does not repair an axis selector whose packets all
live in one small coordinate carrier.

Assume the protected band contains \(q=A\sqrt m+O(1)\).  At the present
scale,

\[
                         R=\Theta(\sqrt{mH}),\qquad
 {q^2\over R}=\Theta(\sqrt{m/H})\longrightarrow\infty.           \tag{4.1}
\]

Choose a union \(E\) of the first logarithmic macroblocks with
\(|E|=\Theta(R)\), large enough that almost every product cell has at
least \(R\) split axes inside \(E\).  Retain those axes whenever possible.
The split-count concentration used in the physical Hall audit shows that
exceptional middle owners have size \(o(W)\).

Every nonexceptional packet now preserves the exterior subset
\([2m]\setminus E\).  For a typical lower target fibre with fixed exterior
set and \(t=|T\cap E|\), the source has inside size \(t+q\).  Hence the
exact target/source capacity ratio is

\[
                         {\binom{|E|}{t+q}\over\binom{|E|}t}
 \le\exp(-c q^2/R)=o(1).                            \tag{4.2}
\]

For the upper sign the ratio is

\[
                         {\binom{|E|}{u-q}\over\binom{|E|}u}
 \le\exp(-c q^2/R)=o(1).                            \tag{4.3}
\]

The typical fibres contain \(1-o(1)\) of both target layers.  Thus,
regardless of compiler conjugates or their correlations, this legal axis
selection misses \((1-o(1))N_q\) targets on both signs.

This does not refute the existence of a dispersed selector.  It proves
that the owner theorem's arbitrary deterministic \(R\)-axis choice cannot
be used in the covariance step without an additional dispersion theorem.

## 5. Exact correlated covariance condition

The packet owners themselves are already disjoint common blocks.  This
allows the Latin construction to be stated directly at packet level.

Let the \(b=G/2^R\) retained \(Q_R\) packets be
\(P_1,\ldots,P_b\).  For every packet \(i\) and label \(a\in[b]\), choose
one legal affine compiler conjugate \(g_{ia}\).  Labels may repeat when
\(b>|\Gamma_R|\).  For a signed target \(T\), define

\[
 d^{q,\pm,T}_{ia}
 ={\bf1}\{T\in g_{ia}F_{P_i,q}^\pm\}.               \tag{5.1}
\]

Within-packet injectivity makes every entry binary.  Put

\[
 \begin{aligned}
 S_{q,\pm,T}&=\sum_{i,a}d^{q,\pm,T}_{ia},\\
 r_{i;q,\pm,T}&=\sum_a d^{q,\pm,T}_{ia},\\
 s_{a;q,\pm,T}&=\sum_i d^{q,\pm,T}_{ia}.
 \end{aligned}                                      \tag{5.2}
\]

Choose a permutation \(\pi\in S_b\) and install \(g_{i,\pi(i)}\) in
packet \(i\).  The resulting target load is

\[
                         Z_{q,\pm,T}(\pi)
 =\sum_i d^{q,\pm,T}_{i,\pi(i)}.                    \tag{5.3}
\]

For uniform \(\pi\),

\[
                         \mathbb EZ_{q,\pm,T}={S_{q,\pm,T}\over b},        \tag{5.4}
\]

and direct inclusion--exclusion gives

\[
 \boxed{
 \mathbb E[Z_{q,\pm,T}(Z_{q,\pm,T}-1)]
 ={S_{q,\pm,T}^2-\sum_i r_{i;q,\pm,T}^2
       -\sum_a s_{a;q,\pm,T}^2+S_{q,\pm,T}
   \over b(b-1)}.}                                  \tag{5.5}
\]

The last term is \(S\), rather than
\(\sum_{i,a}d_{ia}^2\), because the entries are binary.

Let

\[
 \lambda_q={G\over N_q}=c_q+\alpha_q,\qquad
 c_q=\lfloor\lambda_q\rfloor.                       \tag{5.6}
\]

The integer-minimal factorial second moment at mean \(\lambda_q\) is

\[
 \mu_{2,q}^{\min}
 =(1-\alpha_q)c_q(c_q-1)+\alpha_qc_q(c_q+1)
 =2c_q\lambda_q-c_q(c_q+1).                         \tag{5.7}
\]

If the one-point arrays satisfy

\[
                         S_{q,\pm,T}=b\lambda_q      \tag{5.8}
\]

and

\[
 \sum_{\pm}\sum_{q\le H}\sum_T
 \left[
 {S_{q,\pm,T}^2-\sum_i r_{i;q,\pm,T}^2
       -\sum_a s_{a;q,\pm,T}^2+S_{q,\pm,T}
  \over b(b-1)}
 -\mu_{2,q}^{\min}
 \right]
 =o(W),                                             \tag{5.9}
\]

then some deterministic permutation \(\pi\) has total floor energy
\(o(W)\), and hence total target holes \(o(W)\).

Equation (5.9) is the exact cross-packet covariance condition after the
diverse-order theorem.  Once a row-wise option catalogue has fixed the
packet marginals \(r_i\), its remaining negative covariance term is

\[
                         -\sum_a s_{a;q,\pm,T}^2.    \tag{5.10}
\]

Thus the needed effect is column alignment: for each target, occurrences
from different compatible packets must be concentrated into common option
labels.  Without a prescribed row catalogue, both negative square terms
in (5.5) remain design variables.

There is a further warning: taking every row to be a uniform complete
affine catalogue does not make the Latin averaging argument work.  Suppose,
in the ideal exactly divisible form, that a target is compatible with
\(d\) packet rows, every such row contains it in exactly
\(b\theta_{R,q}\) columns, and its mean load is

\[
                         \lambda=d\theta_{R,q}.      \tag{5.11}
\]

Then

\[
 \sum_i r_i^2=d\,b^2\theta_{R,q}^2=b^2\lambda\theta_{R,q}.       \tag{5.12}
\]

Also every column sum is at most \(d\), so

\[
                         \sum_a s_a^2\le dS=db\lambda.           \tag{5.13}
\]

At Gaussian depth,

\[
 \theta_{R,q}=e^{-o(m)},\qquad
 b={G\over2^R}=2^{2m-o(m)},\qquad
 {d\over b}={\lambda\over b\theta_{R,q}}=o(1).       \tag{5.14}
\]

Substitution in (5.5) gives

\[
 \mathbb E[Z(Z-1)]\ge\lambda^2-o(1).                \tag{5.15}
\]

If \(\lambda=c+\alpha\), the gap above the integer-minimal moment is

\[
 \lambda^2-\mu_2^{\min}=c+\alpha^2.                 \tag{5.16}
\]

Thus even the perfectly balanced complete-row catalogue has
\(\Omega(W)\) expected floor energy under a uniform Latin permutation.
Equivalently, a target sees only \(d=o(\sqrt b)\) relevant rows, so
sampling their columns without replacement is asymptotically the same as
independent sampling; its miss probability remains
\(e^{-\lambda}+o(1)\).  The usual bounded-difference inequality for a
random permutation then gives a linear hole count with overwhelming
probability, just as in Theorem 3.1.

This does not exclude an exceptional deterministic Latin permutation.
It proves that complete affine row catalogues plus random
without-replacement alignment do not supply Gate B.  A successful option
array must be strongly nonuniform at row level—effectively assigning
targets to a small set of home packets/labels—while satisfying all target
constraints simultaneously.

Exact equality (5.8) is stronger than necessary.  An \(o(W)\) aggregate
\(L^1\) error in the one-point means, together with the corresponding
reserve-corrected version of (5.9), is sufficient.  This relaxation does
not alter the structural requirement (5.10).

## 6. The remaining theorem

The diverse-order compiler has removed:

1. common-order support sparsity;
2. within-packet repeats;
3. payload and seam collisions;
4. owner conflicts inside retained packets; and
5. excessive component count.

What remains is exactly the following two-stage cross-packet statement.

### Gate A: dispersed fractional Hall

Choose the rank-twisted retained axes so that the weighted loads
\(\lambda_q^\pm(T)\) in (2.7) satisfy the reserve form of the weighted
outer Hall inequalities for arbitrary target weights, simultaneously in
depth and sign.  In particular, the construction must exclude every
localized carrier cut of Section 4.  Total mass (2.8) and coarse-profile
reservoir estimates are not sufficient.

### Gate B: integral Latin alignment

On the resulting fixed owner packets, construct legal conjugate option
tables \(g_{ia}\) satisfying the one-point balance and column-square
condition (5.9).  One common permutation of the columns must work for all
protected depths and both signs.

Theorem 3.1 proves that replacing Gate B by independent conjugates leaves
\(\Omega(W)\) holes.  Section 4 proves that solving Gate B without Gate A
can still leave \((1-o(1))N_q\) holes.  Conversely, Gates A and B together
would prove the coefficient-one target statement while preserving the
exact owner factor.

No current rank-twisted or compiler theorem supplies either the arbitrary-
weight dispersion in Gate A or the column alignment in Gate B.  These,
and only these, are the cross-packet residuals after the diverse-order
factor.
