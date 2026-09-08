# OCR actual-memory audit: variable separator blocks and Fourier curvature

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, or solver

## 0. Outcome

The synchronized state \((j,q)\), where \(j\) is the current dual-block
index and \(q\) is the unmatched height, is Markov for the **annealed
capped relaxation**.  It is not a quenched Markov state for an actual
PBBS carrier after its block words have been selected.  The missing datum
is at least the residual word, or residual semilength, in the current
\(T_j\)-block.

This is proved by an exact variable-block family.  For fixed \(s,r\) and
fixed total semilength, two genuine first zero-winding returns have

\[
 (p,j,q,\text{side})=(s,r-1,r,F),
 \tag{0.1}
\]

the same endpoint corridors

\[
 R_s=R_0=0^{s-1},
 \tag{0.2}
\]

and the same total rank, but their next marked dual separator occurs after
different literal words and different numbers of bits.  Thus a transition
conditioned on actual history cannot be a function of \((j,q)\) alone.
The matrix in
`MATH_ATTACK_OCR_SYNCHRONIZED_CELL_GREEN_NOGO_20260725.md` is correctly
interpreted as the result of summing over all possible residual block
words and all possible marked endpoints.

The same family also tests the Fourier issue sharply.  Its physical
separator sequence alternates sides at every cell.  It therefore pays
only off-diagonal entries

\[
 b_q=\frac1{q+2}
 =\frac12\left(1-\frac q{q+2}\right)
 \tag{0.3}
\]

of the critical cell matrix.  For \(r\) dual exits and \(r-1\) forward
exits, the total capped-relaxation mass available to that fixed side
itinerary is

\[
 b_r^r b_{r-1}^{r-1}
 =(r+2)^{-r}(r+1)^{-(r-1)}.
 \tag{0.4}
\]

Hence the genuine separator-spanning examples disprove the one-block
parsing but do not load the slow invariant corner.  They have maximal
endpoint-switching curvature.  The exact remaining gate is still an
aggregate actual-PBBS anti-corner theorem for histories with long
same-side runs.

## 1. Variable periodic blocks

Fix integers

\[
 r\ge2,qquad s\ge2r,
 \tag{1.1}
\]

and positive integers \(k_0,\ldots,k_{r-1}\).  Put

\[
 X_i=(1^r0^r)^{k_i},
 \qquad
 \overline X_i=(0^r1^r)^{k_i}.
 \tag{1.2}
\]

Every \(X_i\) is Dyck of height \(r\), and

\[
 \boxed{\overline X_i0^r=0^rX_i.}
 \tag{1.3}
\]

Define

\[
 D_0=1^{s-r}
      (\overline X_{r-1}1)
      (\overline X_{r-2}1)\cdots
      (\overline X_01)0^s.
 \tag{1.4}
\]

Write \(L_i=|X_i|=2rk_i\).

### Theorem 1.1 (exact variable-block return)

The word (1.4) starts a consecutive zero-winding return of duration
\(s\) and semilength

\[
 \boxed{m=s+r\sum_{i=0}^{r-1}k_i.}
 \tag{1.5}
\]

Its dual and forward blocks are

\[
 \boxed{T_i=X_i\quad(0\le i<r),}
 \qquad
 T_i=\varnothing\quad(r\le i<s),
 \tag{1.6}
\]

and

\[
 \boxed{S_{s-r+1+i}=X_i\quad(0\le i<r),}
 \tag{1.7}
\]

with all remaining \(S_j\) empty.  In particular \(S_s=X_{r-1}\).

#### Proof

For the first \(r\) rotations, the exact words are

\[
 \begin{aligned}
 D_j={}&1^{s-r+j}
 (\overline X_{r-1}1)\cdots(\overline X_j1)
 \overline X_{j-1}0\overline X_{j-2}0\cdots
 0\overline X_0,0^{s-j+1}
 \end{aligned}
 \tag{1.8}
\]

for \(1\le j\le r\), with the evident omission of an empty product.
The last remaining displayed one is the first bit reaching height \(s\),
so canonical block rotation gives (1.8) inductively.

After \(j=r\), the first maximum is the last bit of the initial mountain
\(1^s\).  Until \(j=s-r+1\), each rotation moves one terminal zero to
the beginning of the descending corridor:

\[
 D_j=1^s0^{j-r}\overline X_{r-1}0\overline X_{r-2}
       0\cdots0\overline X_0,0^{s-j+1}
 \quad(r\le j\le s-r+1).
 \tag{1.9}
\]

At \(j=s-r+1\), the last block \(\overline X_0\) begins at height
\(r\).  Its first \(r\) zeros give the first return to zero.  The
remaining suffix, followed by the terminal \(0^r\), is \(X_0\) by
(1.3).

More generally, after \(b\) such suffixes have been extracted,
\(0\le b\le r-1\), one has

\[
 \begin{aligned}
 D_{s-r+1+b}
 ={}&(X_{b-1}1)(X_{b-2}1)\cdots(X_01)1^{s-b}\\
 &\quad 0^{s-2r+1+b}
 \overline X_{r-1}0\overline X_{r-2}0\cdots
 0\overline X_b,0^r,
 \end{aligned}
 \tag{1.10}
\]

again omitting the first product when \(b=0\).  The first return in the
last remaining block is followed by \(X_b\), and (1.3) turns the next
block rotation into (1.10) with \(b+1\).  This proves the orbit and
(1.7).  At \(b=r-1\), (1.10) ends in

\[
 0^{s-r}\overline X_{r-1}0^r=0^sX_{r-1},
\]

which also verifies the endpoint suffix.

The first-maximum positions are

\[
 \delta(D_j)=s+\sum_{i=j}^{r-1}L_i
 \quad(0\le j\le r),
 \tag{1.11}
\]

\[
 \delta(D_j)=s
 \quad(r\le j\le s-r+1),
 \tag{1.12}
\]

and

\[
 \delta(D_{s-r+1+b})
 =s+\sum_{i=0}^{b-1}L_i
 \quad(0\le b\le r-1).
 \tag{1.13}
\]

The deficits are one up to time \(s-r\), and are \(L_b+1\) at time
\(s-r+1+b\).  Therefore at the proper late time indexed by
\(0\le b<r-1\),

\[
 \delta(D_{s-r+1+b})
 -\sum_{j<s-r+1+b}d(D_j)=r-1-b>0.
 \tag{1.14}
\]

All earlier strict inequalities are immediate from (1.11)--(1.12), and
at the endpoint equality holds.  This proves first return and zero
winding.  Finally, the dual drops in (1.11) have sizes \(L_i+1\) for
\(i<r\) and one thereafter; the literal dual seam identities give
(1.6).  The length of (1.4) proves (1.5). \(\square\)

## 2. The common carrier and its state

Write

\[
 \overline X_i=0^rY_i,
 \qquad X_i=Y_i0^r,
 \qquad Z_i=0Y_i0.
 \tag{2.1}
\]

The second identity follows from (1.3).  The endpoint arrays are

\[
 \mathcal A=0^{s-r}
 (\overline X_{r-1}0)\cdots(\overline X_00),
 \tag{2.2}
\]

\[
 \mathcal C=(0X_{r-1})(0X_{r-2})\cdots(0X_0)0^{s-r}.
 \tag{2.3}
\]

Since

\[
 \overline X_i0=0^{r-1}Z_i,
 \qquad 0X_i=Z_i0^{r-1},
\]

literal cancellation gives

\[
 \mathcal A=0^{s-1}O,
 \qquad
 \mathcal C=O0^{s-1},
 \tag{2.4}
\]

where

\[
 \boxed{
 O=Z_{r-1}0^{r-1}Z_{r-2}0^{r-1}\cdots
   0^{r-1}Z_0.}
 \tag{2.5}
\]

Thus \(R_s=R_0=0^{s-1}\), and the outer carrier is counted once.  It
starts at the last zero in the initial \(0^r\) of
\(\overline T_{r-1}\).  Immediately after that zero the synchronized
state is

\[
 \boxed{(p,j,q,\mathrm{side})=(s,r-1,r,F).}
 \tag{2.6}
\]

The next marked separator is the dual separator at the end of
\(Z_{r-1}\).  Measured from the initial source bit and including both
ends, the literal source-cell word has length

\[
 \boxed{|Z_{r-1}|=2rk_{r-1}-r+2.}
 \tag{2.7}
\]

Since the state (2.6) is taken immediately after the initial source bit,
the unconsumed distance through the next separator is

\[
 \boxed{|Z_{r-1}|-1=2rk_{r-1}-r+1.}
 \tag{2.8}
\]

## 3. Same state and rank, different actual futures

Fix \(s,r\) as in (1.1).  Compare the two exponent vectors

\[
 (k_0,k_1,\ldots,k_{r-2},k_{r-1})
 =(2,1,\ldots,1,1)
 \tag{3.1}
\]

and

\[
 (1,1,\ldots,1,2).
 \tag{3.2}
\]

They have the same sum, hence (1.5) gives the same semilength \(m\).
Equations (2.4) and (2.6) give the same endpoint corridors and the same
synchronized source state.  Nevertheless, by (2.8), the next marked dual
separator occurs after respectively

\[
 r+1
 \qquad\hbox{and}\qquad
 3r+1
 \tag{3.3}
\]

bits.  The corresponding literal words \(Z_{r-1}\) are also different.

This proves the promised memory obstruction.  Conditional on an actual
history, the next legal marked transition is not determined by
\((j,q)\).  One must retain the unconsumed part of \(T_j\), or at least
enough information to locate its marked endpoint.  The Green matrix
\(x\mathbf G_q(x)\) is still an exact **annealed** transfer for the capped
relaxation: it sums all possible internal words and all possible endpoint
locations.  What is invalid is treating that annealed kernel as the
conditional transition law of actual PBBS chronology.

Equivalently, an actual Markov reduction requires a renewal-closure
theorem saying that histories and futures with equal \((j,q)\) may be
spliced while preserving every \(\tau\)-identity.  The examples above
show that the marked endpoint itself is extra state; no such closure
follows from the two scalar coordinates.

## 4. Fourier-curvature test of the genuine family

Formula (2.5) displays both block parsings.  In the dual parsing, the
first partial block is \(Z_{r-1}\), and each subsequent block is
\(0^{r-1}Z_i\).  In the forward parsing, each complete block is
\(Z_i0^{r-1}\).  Consequently the encountered marked separators have
the side sequence

\[
 F,D,F,D,\ldots,F,D.
 \tag{4.1}
\]

There are \(r\) dual exits and \(r-1\) forward exits.  Immediately before
each dual exit the unmatched height is \(r\); immediately before each
forward exit it is \(r-1\).  All these cells are full under \(s\ge2r\).

For a full cell, the critical endpoint matrix is

\[
 \mathbf P_q=\frac1{q+2}
 \begin{pmatrix}q+1&1\\1&q+1\end{pmatrix}.
 \tag{4.2}
\]

Every exit in (4.1) switches endpoints, so the corresponding term lies
in the off-diagonal kernel

\[
 b_q=\frac1{q+2}
 =\frac12\left(1-\frac q{q+2}\right).
 \tag{4.3}
\]

Consequently the total critical mass available to this fixed side
itinerary in the capped relaxation is

\[
 \boxed{
 b_r^r b_{r-1}^{r-1}
 =(r+2)^{-r}(r+1)^{-(r-1)}.}
 \tag{4.4}
\]

Each particular genuine carrier is one coefficient term inside these
off-diagonal kernels, so its normalized critical weight is at most
(4.4), not equal to the whole Green entry.  Formula (4.3) is the
difference between the invariant and anti-invariant cell modes at every
transition.  The upper bound (4.4) is superpolynomially small when
\(r\to\infty\).  Hence the family gives no lower bound on the slow
same-side corner mass.

Taking \(r=\lfloor\theta s\rfloor\), with
\(0<\theta<1/2\), and bounded positive \(k_i\), equation (1.5) gives
\(m=\Theta(s^2)\).  Thus even central-source Gaussian examples can be
separator-spanning while remaining entirely in the high-curvature
alternating sector.

## 5. Exact remaining boundary

The correct hierarchy is now:

1. the literal common word and caps give an exact annealed cell kernel;
2. that kernel has a unit invariant mode and total marked mass
   \(\Theta(s)\);
3. actual PBBS transitions are not Markov on \((j,q)\), because their
   marked block endpoints carry residual-word memory;
4. the explicit genuine separator-spanning families alternate sides and
   therefore do not saturate the unit mode.

The remaining theorem must control actual histories with long same-side
runs after the external four-kernel pieces have been fixed.  Equivalently,
it must prove an \(o(s)\) bound for the actual projected renewal while
retaining the residual block memory.  Neither a two-coordinate Markov
assumption nor the examples in this note settle that theorem.

No coefficient-one conclusion is claimed.
