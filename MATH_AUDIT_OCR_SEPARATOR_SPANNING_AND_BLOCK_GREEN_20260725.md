# Audit of OCR: separator-spanning carriers and the exact block Green operator

Date: 2026-07-25

Method: pure mathematics only; no computation, search, or solver.

## 0. Verdict

The proposed one-block localization

\[
 T_h=X1\overline {S_s}1Y
 \tag{0.1}
\]

is false with the stated quantifiers.  The counterexample in Proposition
4.2 of `MATH_ATTACK_QST_TWO_SEAM_TRANSFER_KERNEL_20260725.md` is correct,
and it extends to a two-parameter family of genuine first zero-winding
returns.  The extension has two useful consequences.

1.  With the overlap fixed, separator spanning persists for arbitrarily
    large durations and lies inside the range (3\ell<s-2) used by the
    shared-boundary collision theorem.
2.  With the overlap growing quadratically in the duration, the examples
    lie in a fixed Gaussian height band (s\asymp\sqrt m).  Thus the
    failure is not a small-rank artefact.

Consequently no injection that assigns every actual root to one local
word (T_h) through (0.1) can prove `OCR_s`.  The proposed weighted
dual-boundary proof is invalid as well.  The numerical inequality

\[
 p_T(e)\ll 4^{-\ell}(h(e)+3)^{-1}
 \tag{0.2}
\]

might conceivably hold for a different reason, but the asserted literal
first-passage factor does not exist for every physical boundary word.

There is nevertheless an exact positive matrix fact.  Once a copied word
really crosses a block separator, its transfer is forced through the
boundary state of a killed path.  This annihilates the order-(s)
central Perron projection in that particular block.  The resulting
boundary factors are computed exactly below.  Their sum is only
logarithmic when the initial cap is bounded, but is still order (s)
when the initial cap and the number of available blocks are both order
(s).  Hence monotonicity of the separator index alone does not give the
required (o(s)) transfer mass.

The conditional coefficient implication in Corollary 5.2 of the transfer
kernel report is correct: a nonnegative synchronized transfer series of
critical mass (o(s)) would close the zero-winding Gaussian-band gate.
What remains missing is precisely a PBBS theorem which removes the
large-initial-cap boundary mode.

## 1. An infinite separator-spanning PBBS family

Fix integers (s\ge4) and (k\ge1), and put

\[
 W=(1100)^k,
 \qquad \overline W=(0011)^k,
 \qquad L=|W|=4k,
 \qquad m=s+L.
 \tag{1.1}
\]

The elementary word identity

\[
 \boxed{\overline W00=00W}
 \tag{1.2}
\]

will be used at the last transition.  Define

\[
 D_0=1^{s-2}\overline W1\overline W1,0^s,
 \tag{1.3}
\]

\[
 D_1=1^{s-1}\overline W1\overline W,0^s,
 \tag{1.4}
\]

and, for (2\le j\le s-1),

\[
 D_j=1^s0^{j-2}\overline W0\overline W0^{s-j+1}.
 \tag{1.5}
\]

Finally put

\[
 D_s=W1^s0^sW.
 \tag{1.6}
\]

### Theorem 1.1

The words in (1.3)--(1.6) are the consecutive canonical iterates of a
genuine first zero-winding return of duration (s):

\[
 \tau D_j=D_{j+1}\qquad(0\le j<s).
 \tag{1.7}
\]

Its endpoint excess is

\[
 \boxed{\Lambda=L=4k.}
 \tag{1.8}
\]

Its staircase data are

\[
 T_0=T_1=S_{s-1}=S_s=W
 \tag{1.9}
\]

and all other (S_j,T_j), including (S_0), are empty.  The mandatory
copied word (0S_s0=0W0) crosses the separator between the
(T_1)- and (T_0)-blocks.  In particular, no (T_h) contains
(1\overline {S_s}1).

#### Proof

The word (overline W) is a concatenation of downward excursions of
depth two.  In (D_0), the first copy is based at height (s-2\ge2),
the following separator up-step reaches height (s-1), the second copy
is based there, and the next up-step first reaches height (s).  The
final (0^s) is the first subsequent return to zero.  Thus the displayed
factorization of (D_0) is canonical and

\[
 \delta(D_0)=s+2L.
 \tag{1.10}
\]

In (D_1), the first (1^{s-1}) reaches height (s-1); the first
(overline W) returns to that height and the following (1) first
reaches (s).  The remaining (overline W0^s) stays between zero and
(s) and first returns to zero at its last bit.  Hence

\[
 \delta(D_1)=s+L.
 \tag{1.11}
\]

For (2\le j\le s-2), the first (1^s) reaches the maximum.  Read the
remaining word from height (s).  After (0^{j-2}), the first
(overline W) has lower height (s-j\ge2); after the next zero, the
second copy has lower height (s-j-1\ge1).  It then returns to height
(s-j+1), and the last (0^{s-j+1}) first reaches zero at its final
bit.  Therefore the factorization is canonical and

\[
 \delta(D_j)=s\qquad(2\le j\le s-2).
 \tag{1.12}
\]

At (j=s-1), identity (1.2) rewrites the tail as

\[
 0^{s-3}\overline W0\overline W00
 =0^{s-3}\overline W000W.
 \tag{1.13}
\]

Starting from height (s), the first (s-3) zeros leave height three;
(overline W) stays between heights one and three and returns to three;
the next three zeros first reach zero; and the final (W) is a terminal
Dyck suffix.  Thus

\[
 \delta(D_{s-1})=s,
 \qquad S_{s-1}=W.
 \tag{1.14}
\]

The word (D_s) has terminal suffix (W), first reaches height (s)
at the last up-step of its central mountain, and hence

\[
 \delta(D_s)=s+L.
 \tag{1.15}
\]

Canonical block rotation sends (1.3) to (1.4), sends (1.4) to the
(j=2) case of (1.5), and, for (2\le j<s-1), moves one final zero to
the front of the terminal corridor, giving the next word in (1.5).  At
the last step, (1.13) gives

\[
 \tau D_{s-1}=W1^s0^{s-2}\overline W00
             =W1^s0^sW=D_s,
\]

where (1.2) was used again.  This proves (1.7).

For (0\le j<s-1), the canonical terminal suffix is empty, so the
chronological deficit is one.  At (j=s-1), it is (L+1).  Therefore

\[
 \sum_{j=0}^{s-1}d(D_j)=(s-1)+(L+1)=s+L=\delta(D_s).
 \tag{1.16}
\]

Every proper partial sum is (j).  It is strictly below
(delta(D_1)=s+L) for (j=1), and below
(delta(D_j)=s) for (2\le j\le s-1).  The exact strict
first-passage criterion therefore makes (1.7) a first zero-winding
return, not merely a formal orbit segment.

The local transition identity

\[
 S_j1P_j=P_{j+1}1\overline T_j

\]

now recovers (1.9): the first two drops in first-maximum position are
both exactly (L), the last rise is caused by (S_{s-1}=W), and all
intermediate words are empty.  Equivalently, direct cancellation in
(1.3)--(1.6) gives the same tuple.

The endpoint words are

\[
 \mathcal A=0^{s-2}(\overline W0)^2,
 \qquad
 \mathcal C=(0W)^2 0^{s-2}.
 \tag{1.17}
\]

Because (W) is the period-four word ((1100)^k), the suffix of length
(2L+1) of ((\overline W0)^2) is literally the prefix of length
(2L+1) of ((0W)^2).  Call this common word (O).  Since
(overline W) begins in zero and (W) ends in zero, (1.17) gives

\[
 \mathcal A=0^{s-1}O,
 \qquad
 \mathcal C=O0^{s-1}.
 \tag{1.18}
\]

Thus (R_s=R_0=0^{s-1}), (|O|=2L+1), and

\[
 \Lambda=|O|-(|S_s|+1)=L.
\]

The first bit of (O) is the second bit of the first copy of
(overline W) in (1.17).  The word (0W0), of length (L+2), uses
the remaining (L-1) bits of that copy, its separator, and the first two
bits of the next copy.  Hence it crosses the (T_1/T_0) separator.
Since every nonempty (T_h) has length (L<L+2), (0.1) is impossible.
This proves the theorem.  \(□\)

### Corollary 1.2 (both relevant asymptotic regimes)

For fixed (k=1) and (s\to\infty), one has (ell=\Lambda/2=2), so

\[
 3\ell<s-2

\]

for every (s\ge9).  Thus separator spanning persists inside the exact
small-overlap range of the shared-boundary theorem.

On the other hand, choose (k=\lfloor c s^2\rfloor) with fixed
(c>0).  Then

\[
 m=s+4k=(4c+o(1))s^2,
 \qquad
 s=\left({1\over2\sqrt c}+o(1)\right)\sqrt m.
 \tag{1.19}
\]

Hence the same separator-spanning failure occurs on every desired fixed
Gaussian band after choosing (c) appropriately.

## 2. What the first-hit factor would be if the parse were legal

This section is conditional and is included to prevent a second counting
error.  Suppose (0.1) really holds and the two displayed up-steps are the
first hits of heights (h+1) and (h+2).  Then

\[
 X1\overline {S_s}1

\]

is exactly a first-passage path from zero to (h+2).  Its bit-length
generating function is

\[
 \boxed{A_{h+2}(x)={x^{h+2}\over F_{h+2}(x^2)}},
 \qquad
 A_{h+2}(1/2)={1\over h+3}.
 \tag{2.1}
\]

This factor is not independent of the height-difference word already
used in the old form of `OCR_s`.  Put

\[
 a=s-1-h,
 \qquad b=h+1.

\]

The continuant determinant identity gives

\[
 \boxed{
 C_a(z)-C_b(z)
 ={z^{b+1}F_{a-b-1}(z)\over F_{a+1}(z)F_{b+1}(z)}.}
 \tag{2.2}
\]

In the bit variable this factors as

\[
 C_a(x^2)-C_b(x^2)
 =A_{b+1}(x)
  {x^{b+1}F_{a-b-1}(x^2)\over F_{a+1}(x^2)}.
 \tag{2.3}
\]

Thus (A_{h+2}) is already the first-passage factor inside the complete
(T_h)-language (C_{s-1-h}-C_{h+1}).  Multiplying the latter by an
additional (A_{h+2}), without first deleting that prefix from the
(T_h)-encoding, counts the same bits twice.  At the critical point,

\[
 (C_{s-1-h}-C_{h+1})(1/4)
 =2\left({1\over h+3}-{1\over s-h+1}\right),
 \tag{2.4}
\]

which is consistent with (2.1)--(2.3).

## 3. Audit of the shared-boundary theorem

The shared-boundary theorem itself does not use (0.1) and survives the
counterexample.  Its exact rank identity is

\[
 r=s+\sum_{j=1}^{s-1}|S_j|_{m e}
      +\sum_{j=0}^{s-1}|T_j|_{m e}-\ell.
 \tag{3.1}
\]

The two capped arrays contain two presentations of the same (2\ell)-bit
word (E); the subtraction of (ell) in (3.1) removes exactly one
semilength copy.  Conditioning on a common boundary word gives the
Hadamard factor

\[
 O(4^{-\ell}/\sqrt{\ell+1}).
 \tag{3.2}
\]

For the untouched forward blocks, the exact partition function is

\[
 P_{s,\ell,h}(z)
 ={F_{\ell+h+1}(z)\over F_U(z)F_V(z)},
 \qquad |U-V|\le1,
 \quad U+V=s+\ell+1.
 \tag{3.3}
\]

After normalizing at (z=1/4), the path-kernel characteristic-function
bound must be integrated in (L^1):

\[
 \int_{-\pi}^{\pi}
 |\varphi_{P_{s,\ell,h}}(t)|\,dt=O(s^{-2}).
 \tag{3.4}
\]

This gives the largest-atom bound (O(s^{-2})) directly by Fourier
inversion.  An (L^2) estimate of the same numerical order would imply
only (O(s^{-1})) for the largest atom.  The source theorem has now been
patched to (3.4); the separate audit file still writes an (L^2) integral
and should be read with this correction.

Coefficient tilting now gives

\[
 z_{r,s,2\ell}
 \le C4^{r-s+\ell}s^{-2}
       {4^{-\ell}\over\sqrt{\ell+1}}
       F_{s,\ell}(1/4)^2.
 \tag{3.5}
\]

Using

\[
 4^{-(s-\ell)}F_{s,\ell}(1/4)^2
 \le C{4^\ell(\ell+2)^2\over s^4}

\]

in (3.5) yields, with no missing power of four,

\[
 \boxed{
 z_{r,s,2\ell}
 \le C4^r{(\ell+2)^2\over s^6\sqrt{\ell+1}}.}
 \tag{3.6}
\]

The valid aggregate range remains

\[
 L\log r=o(r^{1/5}).
 \tag{3.7}
\]

The proposed extension

\[
 L=o\!\left({r^{1/4}\over(\log r)^{5/4}}\right)

\]

depended on the false one-block parse and is retracted.  Its algebraic
equivalence to
(L^2(\log r)^{5/2}=o(\sqrt r)) was correct; its PBBS premise was not.

## 4. The exact bit/block transfer operator

Let a parsed carrier traverse blocks whose Dyck caps are

\[
 a_0,a_1,\ldots,a_q.

\]

The exact state while reading bits is ((i,y)), where (i) is the
current block index and (0\le y\le a_i) is the height above the most
recent record minimum.  A (1)-bit raises (y), a (0)-bit lowers it
when (y>0), and a (0)-bit read at (y=0) is the separator and moves
to the next block.  Exceeding a cap kills the path.

At the critical bit weight (1/2), let (K_a) be the killed-path matrix
on (\{0,1,\ldots,a\}):

\[
 K_a(y,z)={1\over2}{\bf1}_{\{|y-z|=1\}}.
 \tag{4.1}
\]

Let

\[
 J={1\over2}e_0e_0^{\mathsf T}
 \tag{4.2}
\]

be the separator transition.  The full monotone block operator is the
upper-bidiagonal matrix

\[
 \mathsf M=
 \begin{pmatrix}
 K_{a_0}&J&0&\cdots\\
 0&K_{a_1}&J&\ddots\\
 \vdots&\ddots&\ddots&\ddots\\
 0&\cdots&0&K_{a_q}
 \end{pmatrix}.
 \tag{4.3}
\]

This is the exact finite-state transfer for a word parsed into capped
(0D)-blocks, after reversing/complementing a dual array when necessary.
The phase flag saying whether the next zero is a separator is already
encoded by (y=0).

### Theorem 4.1 (exact block Green formula)

Put (G_a=(I-K_a)^{-1}) and
(\mathsf G=(I-\mathsf M)^{-1}).  Then

\[
 G_a(y,z)
 ={2(\min(y,z)+1)(a+1-\max(y,z))\over a+2}.
 \tag{4.4}

Moreover,

\[
 \mathsf G_{ii}=G_{a_i},
 \tag{4.5}
\]

and for (i<j),

\[
 \boxed{
 \mathsf G_{ij}(y,z)
 ={1\over2}G_{a_i}(y,0)G_{a_j}(0,z)
 \prod_{r=i+1}^{j-1}{a_r+1\over a_r+2}.}
 \tag{4.6}
\]

In particular,

\[
 0\le \mathsf G_{ij}(y,z)
 \le2\prod_{r=i+1}^{j-1}{a_r+1\over a_r+2}.
 \tag{4.7}
\]

#### Proof

Formula (4.4) is the unique solution of the discrete Green equation with
zero boundary values at (-1) and (a+1).  Equivalently it is the path
Green formula on (a+1) interior vertices after the shift (y\mapsto
y+1).

Because (4.3) is block upper triangular, its inverse has diagonal blocks
(G_{a_i}).  For (i<j), block multiplication gives

\[
 \mathsf G_{ij}
 =G_{a_i}JG_{a_{i+1}}J\cdots JG_{a_j}.
 \tag{4.8}
\]

The rank-one form (4.2), together with

\[
 G_a(0,0)={2(a+1)\over a+2},
 \qquad
 0\le G_a(y,0)={2(a+1-y)\over a+2}\le2,
 \tag{4.9}
\]

reduces (4.8) to (4.6) and proves (4.7).  \(□\)

### 4.1 Exact Perron accounting

The eigenvalues and normalized eigenvectors of (K_a) are

\[
 \lambda_r=\cos{\pi r\over a+2},
 \qquad
 \phi_r(y)=\sqrt{2\over a+2}
  \sin{\pi r(y+1)\over a+2}
 \quad(1\le r\le a+1).
 \tag{4.10}
\]

For (y=\lfloor a/2\rfloor), the Perron term alone is

\[
 {\phi_1(y)^2\over1-\lambda_1}
 =\left({4\over\pi^2}+o(1)\right)a.
 \tag{4.11}
\]

Thus a same-block central source and sink retain an order-(a) slow
mode.  At the boundary, however,

\[
 {\phi_1(0)^2\over1-\lambda_1}
 ={4+o(1)\over a},
 \tag{4.12}
\]

while \(G_a(0,0)<2\).  A genuine separator crossing therefore forces the
source-to-sink transfer through a vector whose projection onto the
normalized slow Perron mode is \(O(a^{-3/2})\), and (4.6) removes the
order-\(a\) factor
from that block exactly.

### 4.2 The physical source and sink of the reversed overlap

For the actual dual endpoint word, put

\[
 D_j^\vee=\operatorname {rev}(\overline T_j).
\]

This is a Dyck word with the same height cap as \(T_j\), and

\[
 \operatorname {rev}(\mathcal A)
 =(0D_0^\vee)(0D_1^\vee)\cdots(0D_{s-1}^\vee).
 \tag{4.13}
\]

Since \(\mathcal A=R_sO\), the word \(\operatorname {rev}(O)\) is one
literal prefix of (4.13).  This is the exact reason to use the monotone
block operator (4.3).

Let \(r\) be the number of separator zeros met by this prefix, including
its first bit.  After the first separator, the source is \(e_0\) in
layer zero.  The prefix ends in layer \(r-1\).  If its final within-block
height is \(y\), then its ordinary net height is \(y-r\).  But
\(\operatorname {net}(O)=-1\), so

\[
 \boxed{y=r-1.}
 \tag{4.14}
\]

Thus the physical source and sink are not arbitrary:

\[
 \boxed{
 \text{source}=e_0\text{ in layer }0,\qquad
 \text{sink}=e_{r-1}\text{ in layer }r-1.}
 \tag{4.15}
\]

The initial separator has critical weight \(1/2\).  Consequently the
critical mass of all cap-valid reversed overlap words spanning exactly
\(r\) blocks is bounded by the exact matrix entry

\[
 \boxed{
 w_r={1\over2}\,
 \mathsf G_{0,r-1}(0,r-1).}
 \tag{4.16}
\]

This encoding contains \(O\) once: it is one prefix of
\(\operatorname {rev}(\mathcal A)\).  It does not also insert the copy
of \(O\) in \(\mathcal C=OR_0\).  Therefore (4.16) has no duplicated
outer carrier.  What is not yet proved is a disjoint reconstruction of
all the remaining root bits into the four factors of
\(K^\times\); (4.16) by itself is a one-sided carrier bound, not
OCR_s.

For endpoint excess \(2\ell\), the audited shifted cap is

\[
 a_j=\min\{s-1-j,j+1+\ell\}.
 \tag{4.17}
\]

On its increasing branch,

\[
 a_j=a_0+j,\qquad a_0=\ell+1.
 \tag{4.18}
\]

Substituting (4.18) and the physical sink \(r-1\) into (4.6) gives,
for every \(r\) which stays in this branch,

\[
 \begin{aligned}
 w_r
 &={(\,a_0+1\,)^2\over
       (a_0+r)(a_0+r+1)}. 
 \end{aligned}
 \tag{4.19}
\]

Indeed

\[
 G_{a_0}(0,0)={2(a_0+1)\over a_0+2},
\]

\[
 G_{a_0+r-1}(0,r-1)
 ={2(a_0+1)\over a_0+r+1},
\]

and the intermediate boundary factors telescope to

\[
 \prod_{j=1}^{r-2}{a_0+j+1\over a_0+j+2}
 ={a_0+2\over a_0+r}.
\]

Formula (4.19) also holds for \(r=1\), by direct evaluation.
Therefore

\[
 \boxed{
 \sum_{r=1}^{q}w_r
 =(a_0+1)^2
 \left({1\over a_0+1}-{1\over a_0+q+1}\right)
 ={q(a_0+1)\over a_0+q+1}.}
 \tag{4.20}
\]

This is the exact source/sink projection bound for the physical
one-sided carrier relaxation.

### 4.3 Why monotone block index still does not prove OCR_s

For comparison, if the final height is discarded and all possible exit
states are summed independently, Formula (4.6) contains
the exact telescope

\[
 \prod_{r=1}^{d-1}{a_0+r+1\over a_0+r+2}
 ={a_0+2\over a_0+d+1}.
 \tag{4.21}
\]

Consequently the mass obtained by summing over all possible later exit
blocks through distance \(q\) has order

\[
 \boxed{
 (a_0+2)\sum_{d=1}^{q}{1\over a_0+d+1}
 =\Theta\!\left((a_0+2)
   \log\left(1+{q\over a_0+2}\right)\right).}
 \tag{4.22}
\]

The physical endpoint constraint improves (4.22) to (4.20).  In
particular it gives \(O(1)\), rather than \(O(\log q)\), when
\(a_0=O(1)\).  But if

\[
 a_0\asymp q\asymp s,
\]

then (4.20) is still \(\Theta(s)\), not \(o(s)\).  Thus even the exact
physical source/sink projection and monotone separator coordinate do not
eliminate the critical large-initial-cap sector.  The obstruction is no
longer one within-block Perron vector; it is the diffuse sum over
\(\Theta(s)\) possible terminal block indices.

This calculation identifies the exact remaining matrix statement.  The
actual PBBS entry and exit vectors \(b_{s,i},c_{s,j}\) in the synchronized
forward/dual operator must satisfy a genuinely stronger estimate, for
example

\[
 \sum_{i\le j}
 \langle b_{s,i},\mathsf G_{ij}c_{s,j}\rangle=o(s),
 \tag{4.23}
\]

uniformly on the relevant Gaussian ranks.  Formula (4.20) proves that
(4.23) cannot follow merely from monotonicity, cap validity, and one
separator boundary projection.  It must use the full two-sided PBBS
chronology or quotient packing.

## 5. Audit of the conditional `OCR_s` implication

Choose deterministic central seams (t_s,u_s), and suppose a class of
actual starts is coefficientwise bounded by

\[
 K^\times_{s,t_s,u_s}(x)\Psi_s(x),
 \qquad \Psi_s(x)\succeq0.
 \tag{5.1}
\]

The normalized one-crossing coefficient bound is

\[
 \sup_n2^{-n}[x^n]K^\times_{s,t_s,u_s}(x)\le C s^{-6}.
 \tag{5.2}
\]

Convolution with the nonnegative series (Psi_s) therefore gives

\[
 [x^{2m}]K^\times_{s,t_s,u_s}\Psi_s
 \le C4^m s^{-6}\Psi_s(1/2).
 \tag{5.3}
\]

If, uniformly for (a\sqrt m\le s\le A\sqrt m),

\[
 \Psi_s(1/2)\le\eta_m s,
 \qquad \eta_m\longrightarrow0,

\]

then each height contributes at most
(C\eta_m4^m s^{-5}).  There are (O(\sqrt m)) heights and
(s\asymp\sqrt m), so the band total is

\[
 O(\eta_m4^m m^{-2})
 =o(B_m/\sqrt m).
 \tag{5.4}
\]

All rank powers and the final Catalan normalization are therefore
correct.  The unproved premise is exactly the (o(s)) transfer mass in
(5.1), not the coefficient extraction in Corollary 5.2.

## 6. Precise proved and conditional boundary

Proved here:

1. The one-block two-first-hit parse fails for an infinite family of
   genuine returns, including both the small-overlap range and fixed
   Gaussian height bands.
2. Conditional on a legal one-block parse, the first-passage series is
   (A_{h+2}), and it is already a factor of the height-difference series
   (C_{s-1-h}-C_{h+1}).
3. The shared-boundary theorem and its rank exponents survive; its
   Fourier step requires the patched (L^1) integral.
4. The exact monotone bit/block Green operator is (4.3), with resolvent
   (4.6).  Separator crossing removes the central Perron factor exactly.
5. The exact physical source/sink sum is \(O(1)\) for bounded initial
   cap, but can be \(\Theta(s)\) in the large-overlap sector.
6. Corollary 5.2 has the correct coefficient and Catalan accounting.

Not proved:

1. The pointwise weighted boundary inequality (0.2) by some method not
   using the false parse.
2. A coefficientwise synchronized transfer bound with critical mass
   (o(s)).
3. The zero-winding contribution to coefficient one in the residual
   large-overlap sector.

Thus the exact next statement is (4.23), with the actual PBBS source and
sink vectors and all separator-spanning states specified.  The old
one-\(T_h\) `OCR_s` injection is closed as a proof lane.
