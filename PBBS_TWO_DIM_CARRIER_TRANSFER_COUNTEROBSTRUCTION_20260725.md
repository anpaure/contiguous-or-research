# The exact two-coordinate carrier transfer and its stationary-block obstruction

Date: 2026-07-25  
Method: pure mathematics only

## 0. Outcome

The separator-spanning obstruction does lead to a natural exact local
state.  While a common carrier is read, retain

\[
 (a,p)=
 \bigl(\text{number of strict record-minimum delimiters already met},
       \text{height above the current record minimum}\bigr).
\]

This is the promised ``block index plus unmatched height'' state.  In the
initial increasing-cap chamber its transfer can be evaluated exactly.
The evaluation replaces the hoped-for Fourier local limit by an explicit
triangular resolvent:

1. after a fixed balanced overlap word \(E\), allowing the mandatory word
   \(\operatorname {rev}(S_s)0\) to cross as many dual-block separators as
   its record minima require has total critical marked mass bounded away
   from zero (in fact it tends to one);
2. one renewal pair changes the state by a running maximum, not by an
   additive diffusive increment;
3. every prescribed positive block displacement has critical Green mass
   at most one, while zero displacement from incoming record height \(p\)
   has mass at most \(p+2\);
4. the saturated zero-displacement state retains the scalar
   \(\Theta(s)\) Green mode on the correct semilength-\(\Theta(s^2)\)
   Gaussian scale.

Consequently the proposed uniform Fourier-curvature lemma is false: the
eigenvalues of the exact marked transfer do not depend on the Fourier
variable.  The explicit source-sensitive bound is nevertheless stronger
than a local CLT.  It closes every positive-displacement sector, and every
zero-displacement sector with incoming record height \(p=o(s)\).

This does **not** disprove the PBBS coefficient-one gate.  It narrows the
local residual to zero displacement from macroscopic record height
\(p=\Theta(s)\).  Identifying the actual source and sink states of the
renewal segment inside the full carrier equation remains necessary.

## 1. The exact record-minimum automaton

Let

\[
 Q_0(z)=Q_1(z)=1,\qquad Q_{j+1}(z)=Q_j(z)-zQ_{j-1}(z),
 \qquad C_j(z)={Q_j(z)\over Q_{j+1}(z)}.
\]

Fix integers \(L\ge0\) and \(J\ge1\).  Consider a block array

\[
 \mathscr D_L=(0D_1)(0D_2)\cdots,
 \tag{1.1}
\]

where \(D_i\) is a Dyck word of height at most \(L+i\), at least for
\(1\le i\le J\).  Give the blocks independent critical Boltzmann laws

\[
 \Pr(D_i=D)={2^{-|D|}\over C_{L+i}(1/4)}.
 \tag{1.2}
\]

For a prefix \(w\) of (1.1), let \(H_w(t)\) be its bit-height, put

\[
 a(w)=-\min_tH_w(t),\qquad
 p(w)=H_w(|w|)+a(w).
 \tag{1.3}
\]

The delimiter zeroes in (1.1) are exactly the strict record-minimum
steps.  Hence \(a\) is the current block index and \(p\) is the current
height inside that Dyck block.  The exact local transitions are

\[
\begin{array}{c|c}
\text{next bit}&(a,p)\text{ after the bit}\cr\hline
1&(a,p+1),\cr
0,\ p>0&(a,p-1),\cr
0,\ p=0&(a+1,0).
\end{array}
\tag{1.4}
\]

The first move is allowed only below the current cap \(L+a\).  Thus no
unmatched word needs to be stored for membership in the local block
array: \((a,p)\) is an exact state.

The following calculation is the useful exact form of this transfer.

### Theorem 1.1 (fixed-prefix completion formula)

Let \(w\) be a legal prefix of (1.1), let

\[
 y=\operatorname {net}(w),\qquad a=a(w),\qquad p=a+y,
\]

and assume \(a\le J\).  Then

\[
 \boxed{
 \Pr(\mathscr D_L\text{ begins with }w)
 =2^{1-|w|}{L-y+1\over L+2}.}
 \tag{1.5}
\]

In particular the probability is independent of the record depth \(a\)
and of the detailed separator-spanning pattern of \(w\).

#### Proof

Use step variable \(x\), with \(z=x^2\).  A walk currently at height
\(p\) in a Dyck block of cap \(H\) has completion series

\[
 R_{H,p}(x)={x^pQ_{H-p}(z)\over Q_{H+1}(z)}.
 \tag{1.6}
\]

The prefix \(w\) contains \(a\) deterministic delimiter zeroes, so it
fixes \(|w|-a\) bits belonging to Dyck blocks.  The generating series of
all completions of \(w\), divided by the partition function of the
unseen later blocks, is therefore

\[
 x^{|w|-a}R_{L+a,p}(x)
 =x^{|w|+y}{Q_{L-y}(z)\over Q_{L+a+1}(z)}.
 \tag{1.7}
\]

The partition function of the first \(a\) complete blocks telescopes:

\[
 \prod_{i=1}^{a}C_{L+i}(z)
 ={Q_{L+1}(z)\over Q_{L+a+1}(z)}.
 \tag{1.8}
\]

After division, the prefix probability at general \(x\) is

\[
 x^{|w|+y}{Q_{L-y}(x^2)\over Q_{L+1}(x^2)}.
 \tag{1.9}
\]

At \(x=1/2\), use

\[
 Q_j(1/4)={j+1\over2^j}
\]

to obtain (1.5).  \(\square\)

As checks, the deterministic first delimiter \(w=0\) has probability
one, and for balanced \(|w|=2\ell\), (1.5) gives

\[
 2\,4^{-\ell}{L+1\over L+2},
\]

the fixed-boundary probability in the audited shared-boundary theorem
when \(L=\ell\).

## 2. Exact separator-spanning extension mass

For a zero-winding return of duration \(s\) and endpoint overlap
\(2\ell\), reverse the dual array:

\[
 \operatorname {rev}V
 =(0\operatorname {rev}\overline T_0)
  (0\operatorname {rev}\overline T_1)\cdots.
 \tag{2.1}
\]

The cap of its \(i\)-th block is

\[
 \min\{s-i,\ell+i\}.
 \tag{2.2}
\]

Consequently the first

\[
 J=\left\lfloor{s-\ell\over2}\right\rfloor
 \tag{2.3}
\]

blocks are exactly in the increasing-cap chamber of Section 1 with
\(L=\ell\).

Let \(E\) be the common balanced boundary word, let

\[
 B=\operatorname {rev}E,\qquad d=-\min H_B,
\]

and assume \(d\le J\).  The suffix identity

\[
 V=R_s(0S_s)E
\]

requires the reverse dual array, after \(B\), to continue with

\[
 W_S=\operatorname {rev}(S_s)0.
 \tag{2.4}
\]

If \(h=\operatorname {ht}(S_s)\), then

\[
 a(BW_S)=\max\{d,h\}.
 \tag{2.5}
\]

Indeed, \(B\) is balanced with record depth \(d\), while
\(\operatorname {rev}(S_s)\) has nonpositive prefixes and minimum
\(-h\); the last zero ends at height \(-1\), and \(d\ge1\).  Thus
\(BW_S\) remains in the increasing-cap chamber whenever
\(\max(d,h)\le J\).

### Theorem 2.1 (no first-hit loss after exact separator spanning)

For every Dyck word \(S\) with \(\operatorname {ht}(S)\le J\),

\[
 \boxed{
 \Pr(W_S\mid B)
 =2^{-|S|-1}{\ell+2\over\ell+1}.}
 \tag{2.6}
\]

Consequently the total **marked** critical mass of all such extensions is

\[
 \boxed{
 \Xi_{\ell,J}
 :={\ell+2\over2(\ell+1)}C_J(1/4)
 ={(\ell+2)(J+1)\over(\ell+1)(J+2)}.}
 \tag{2.7}
\]

In particular

\[
 {2\over3}\le \Xi_{\ell,J}\le {3\over2}
 \qquad(\ell,J\ge1),
 \tag{2.8}
\]

and \(\Xi_{\ell,J}\to1\) whenever \(\ell,J\to\infty\).  In the genuine
common-boundary language the sector \(\ell=1\) is empty; for
\(\ell\ge2\) the upper bound improves to \(4/3\).

Here ``marked'' means that the canonical choice of \(S_s\) is retained.
Different \(S\)'s need not define prefix-free cylinder events, but they
are different marked PBBS data and are counted separately in the local
transfer series.

#### Proof

The word \(B\) has length \(2\ell\) and net zero.  The word \(BW_S\)
has length \(2\ell+|S|+1\) and net \(-1\).  Apply (1.5) to both prefixes
and divide:

\[
 {2^{1-(2\ell+|S|+1)}
       (\ell+2)/(\ell+2)
  \over
  2^{1-2\ell}(\ell+1)/(\ell+2)}
 =2^{-|S|-1}{\ell+2\over\ell+1}.
\]

Summing over height-\(J\) Dyck words and using

\[
 C_J(1/4)={2(J+1)\over J+2}
\]

proves (2.7).  The bounds and limit are immediate.  \(\square\)

This calculation explains exactly why the retracted one-block argument
produced a spurious vanishing first-hit factor.  If the copied word is
forced to remain in one dual block, reaching its internal height costs a
first-passage factor.  In the genuine array it may instead use every new
record minimum as the next deterministic block delimiter.  The telescope
over those separators cancels the first-passage loss completely.

## 3. Exact marked one-pair transfer

Fix a corridor seam \(u\), and put

\[
 A=s-u,\qquad b=u-1.
\]

One extra seam-crossing pair, read from the lower side of the seam, has
the unique form

\[
 L\,1\,U\,0,
 \tag{3.1}
\]

where \(L\) is a loop based at the top of the lower strip
\([0,u-1]\), and \(U\) is a loop based at the bottom of the upper strip
\([u,s]\).  Complementing the lower loop identifies its maximum downward
depth \(h\) with the height of a Dyck word.  Hence the exact-height series
is

\[
 D_h(z)=C_h(z)-C_{h-1}(z),\qquad0\le h\le b,
 \tag{3.2}
\]

where \(C_{-1}=0\).  The upper loop has series \(C_A\), and the two seam
steps contribute \(z\).

Suppose the current record state is \(p\).  The word (3.1) has net zero
and minimum \(-h\), so the exact update and block displacement are

\[
 p'=\max\{p,h\},\qquad \Delta a=p'-p.
 \tag{3.3}
\]

Mark \(\Delta a\) by \(y\).  For \(0\le p,q\le b\), the exact one-pair
matrix is

\[
 \boxed{
 \begin{aligned}
  \mathsf R_{p,p}(z;y)&=zC_A(z)C_p(z),\\
  \mathsf R_{p,q}(z;y)&=zC_A(z)
       \bigl(C_q(z)-C_{q-1}(z)\bigr)y^{q-p},
       &&q>p,\\
  \mathsf R_{p,q}(z;y)&=0,&&q<p.
 \end{aligned}}
 \tag{3.4}
\]

The state \(b\) also represents every saturated incoming height
\(p\ge b\), since no lower loop can then create another record.  Its
diagonal entry is the scalar renewal kernel

\[
 \rho_{s,u}(z)=zC_A(z)C_b(z).
 \tag{3.5}
\]

The matrix (3.4) is an exact coefficientwise marked decomposition of the
scalar kernel: summing its possible next records gives

\[
 zC_A\left(C_p+
  \sum_{q=p+1}^{b}(C_q-C_{q-1})\right)
 =zC_A C_b=\rho_{s,u}.
 \tag{3.6}
\]

### Theorem 3.1 (exact powers and resolvent)

Put \(\lambda_q(z)=zC_A(z)C_q(z)\).  For every \(k\ge1\),

\[
 \boxed{
 (\mathsf R^k)_{p,q}
 =\begin{cases}
   \lambda_p^k,&q=p,\\
   (\lambda_q^k-\lambda_{q-1}^k)y^{q-p},&q>p,\\
   0,&q<p.
  \end{cases}}
 \tag{3.7}
\]

Consequently

\[
 \boxed{
 [(I-\mathsf R)^{-1}]_{p,q}
 =\begin{cases}
  (1-\lambda_p)^{-1},&q=p,\\[1mm]
  \bigl((1-\lambda_q)^{-1}
       -(1-\lambda_{q-1})^{-1}\bigr)y^{q-p},&q>p,\\
  0,&q<p.
 \end{cases}}
 \tag{3.8}
\]

#### Proof

For \(k\) successive pairs with lower-loop depths
\(h_1,\ldots,h_k\), iteration of (3.3) gives

\[
 p_k=\max\{p,h_1,\ldots,h_k\}.
\]

The total series for all \(k\)-tuples with \(p_k\le q\) is
\(\lambda_q^k\).  If \(q>p\), subtract the tuples with
\(p_k\le q-1\), proving (3.7).  The diagonal case is immediate.
Summing the geometric series proves (3.8).  \(\square\)

At the critical point,

\[
 \lambda_q(1/4)
 ={(A+1)(q+1)\over(A+2)(q+2)},
\]

so (3.8) becomes

\[
 \boxed{
 \begin{aligned}
  [(I-\mathsf R)^{-1}]_{p,p}(1/4)
   &={(A+2)(p+2)\over A+p+3}\le p+2,\\
  [(I-\mathsf R)^{-1}]_{p,q}(1/4)
   &={(A+2)(A+1)\over
      (A+q+3)(A+q+2)}\le1,\qquad q>p.
 \end{aligned}}
 \tag{3.9}
\]

Thus every prescribed positive displacement has bounded Green mass.
Only zero displacement remembers the incoming record height.

### Proposition 3.2 (the saturated zero-displacement mode)

Assume \(\epsilon s\le u\le(1-\epsilon)s\).  At the saturated state
\(p=b\),

\[
 [(I-\mathsf R)^{-1}]_{b,b}(1/4)
 ={(u+1)(s-u+2)\over s+2}=\Theta_\epsilon(s).
 \tag{3.10}
\]

For fixed \(0<\eta<M<\infty\), its layers

\[
 \sum_{\eta s\le k\le Ms}\rho_{s,u}(1/4)^k
 =\Theta_{\epsilon,\eta,M}(s)
 \tag{3.11}
\]

have zero block displacement.  One pair has exact critical mean
semilength

\[
 \left.z{d\over dz}\log\rho_{s,u}(z)\right|_{1/4}
 ={s+2\over3},
 \tag{3.12}
\]

so (3.11) lies on semilength scale \(s^2\).

#### Proof

Equations (3.10)--(3.11) follow from (3.9) and a geometric sum.  The
critical continuant expansion gives

\[
 \left.z{d\over dz}\log C_a(z)\right|_{1/4}={a\over3}.
\]

Apply this to \(zC_A C_b\), noting \(A+b=s-1\).  \(\square\)

## 4. The full corridor resets the record state and sums every displacement

The entrywise bounds in (3.9) would be useful only if the outside carrier
words prescribed one value of \(q\).  The exact first-passage pieces do
not do this.  They erase the intermediate record height.

Call a word \(F_d\) a downward top-to-bottom first passage of depth \(d\)
if

\[
 \operatorname {net}(F_d)=-d,qquad
 -d\le H_{F_d}(t)\le0,
\]

and its endpoint is the first visit to \(-d\).  The upper bound zero is
the fact that the path starts at the top wall and cannot cross it.

### Lemma 4.1 (record reset)

If the current record height is \(p\le d\), then appending
\(\operatorname {rev}F_d\) gives final record height zero.  The block
index increases by exactly \(d-p\).

#### Proof

A prefix of \(\operatorname {rev}F_d\) is a suffix of \(F_d\).  If the
complementary prefix of \(F_d\) has net \(x\le0\), that suffix has net
\(-d-x\ge-d\).  Thus every reversed prefix has net at least \(-d\), and
the full reversed word ends at \(-d\).  Starting at height \(p\), the
new global minimum is lower by \(d-p\), and the endpoint is that minimum.
\(\square\)

Now use the exact scalar seam decomposition.  In forward order, a
corridor from height \(s\) to zero is

\[
 F_A\,0\,
 (L_1,1,U_1,0)\cdots(L_k,1,U_k,0)\,F_b,
 \tag{4.1}
\]

where \(A=s-u\), \(b=u-1\), and the displayed zero after \(F_A\) is the
first downcrossing of the seam.  In the reversed carrier order this is

\[
 \operatorname {rev}F_b\,
 (0\operatorname {rev}U_k1\operatorname {rev}L_k)\cdots
 (0\operatorname {rev}U_11\operatorname {rev}L_1)\,
 0\operatorname {rev}F_A.
 \tag{4.2}
\]

The middle factors in (4.2) have net zero.  If \(U_i\) has height
\(h_i-1\), then the factor has minimum \(-h_i\).  Thus its record update is
again a running maximum, now with

\[
 1\le h_i\le A+1.
\]

The reverse-oriented marked matrix is consequently (3.4) with the index
shift

\[
 \widehat\lambda_q(z)=zC_b(z)C_{q-1}(z),qquad
 1\le q\le A+1,qquad \widehat\lambda_0=0.
 \tag{4.3}
\]

Its resolvent entries are

\[
 \widehat G_{0,0}=1,qquad
 \widehat G_{0,q}
 ={1\over1-\widehat\lambda_q}
  -{1\over1-\widehat\lambda_{q-1}}
 \quad(q\ge1).
 \tag{4.4}
\]

### Theorem 4.2 (exact telescoping restoration of the scalar Green mode)

Assume that the incoming record height before (4.2) is at most \(b\).
Then the first word \(\operatorname {rev}F_b\) resets it to zero.  After
the renewal pairs, the state is some \(q\le A+1\).  The last word
\(0\operatorname {rev}F_A\) is a record-reset word of depth \(A+1\), so
it resets **every** such \(q\) to zero.  (It need not itself first hit its
minimum only at the endpoint; Lemma 4.1 uses only the lower prefix bound
and the endpoint.)  Hence the physical
sink accepts all intermediate states, and

\[
 \boxed{
 \sum_{q=0}^{A+1}\widehat G_{0,q}(z)
 ={1\over1-zC_b(z)C_A(z)}
 ={1\over1-\rho_{s,u}(z)}.}
 \tag{4.5}
\]

At \(z=1/4\) and a central seam, (4.5) is \(\Theta(s)\).

#### Proof

The two reset statements are Lemma 4.1.  Formula (4.5) is the telescoping
sum of (4.4), since

\[
 \widehat\lambda_{A+1}=zC_bC_A=\rho_{s,u}.
\]

All series have nonnegative coefficients, so the identity is also a
coefficientwise marked-language identity.  \(\square\)

For the height-\(J\) extension subclass in Section 2, choose a central seam
with \(b\ge J=\lfloor(s-\ell)/2\rfloor\).  Immediately before the full
corridor \(\operatorname {rev}(R_s0)\), the record state coming from
\(\operatorname {rev}E\operatorname {rev}(S_s)\) is at most \(J\).
The first bit of \(\operatorname {rev}(R_s0)\) is the last zero in the
word \(W_S\) of Section 2; it is not counted twice.  Thus the hypothesis
of Theorem 4.2 holds throughout that subclass.  Its marked critical mass
is \(\Xi_{\ell,J}=\Theta(1)\), so it is already enough to rule out a
uniform local-reset gain.  Returns with \(\operatorname {ht}(S_s)>J\)
are not covered by this reset statement and would require a separate
outer-height estimate.

## 5. Fourier audit and exact conclusion

Both marked matrices are upper triangular.  Their eigenvalues are
independent of the Fourier marker \(y=e^{i\theta}\); in particular the
saturated eigenvalue is always \(\rho_{s,u}(1/4)\).  Therefore no norm can
satisfy

\[
 \|\mathsf R(1/4;e^{i\theta})\|
 \le\rho_{s,u}(1/4)e^{-c\theta^2}
\]

with \(c>0\).  More decisively, Theorem 4.2 shows that the actual
first-passage source and sink sum all block displacements and restore the
scalar Green series exactly.  There is no local-limit gain to extract.

This is a precise no-go for the proposed two-dimensional carrier shortcut,
not for coefficient one.  A remaining proof must use information absent
from the free corridor transfer, for example:

* simultaneous compatibility with another phase whose first-passage reset
  is not aligned with this one;
* the exact PBBS canonical chronology outside the local carrier equation;
  or
* quotient-edge-disjoint packing restrictions on the scalar Green sector.

The shared-boundary theorem remains valid, including its
\(\Lambda=o(r^{1/5})\) packing range.  The present calculation shows that
the next gain cannot come solely from marking the dual-block index of one
seam renewal.

## 6. Joint transported phases with a common atomization still telescope

The preceding no-go is not an artifact of using only one record
coordinate.  There is a product-poset identity which covers any fixed
collection of transported phases **provided their renewal scans have a
common atomization**.  Genuinely interlaced atomizations are discussed at
the end of the section.

Let \(\Omega\) be the set of possible one-pair words, with nonnegative
weight \(w(\omega)\).  Suppose \(d\) transported carrier scans assign to
\(\omega\) the vector of record depths

\[
 h(\omega)=(h_1(\omega),\ldots,h_d(\omega))
 \in P:=\prod_{i=1}^d\{0,1,\ldots,B_i\}.
\]

The joint record state is updated by coordinatewise maximum,

\[
 p'=p\vee h(\omega).
 \tag{6.1}
\]

No independence between the coordinates of \(h\) is assumed.  Define the
cumulative one-pair series

\[
 K(q)=\sum_{\omega:\,h(\omega)\le q}w(\omega),
 \qquad q\in P.
 \tag{6.2}
\]

### Theorem 6.1 (product-record resolvent)

Starting from the zero record vector, the series of \(k\)-pair words whose
final joint record is at most \(q\) is exactly \(K(q)^k\).  Hence the
series whose final record is exactly \(q\) is

\[
 \sum_{r\le q}\mu_P(r,q)K(r)^k,
 \tag{6.3}
\]

where \(\mu_P\) is the Möbius function of the product of chains.  After
summing over every \(k\ge0\), the exact-state Green series is

\[
 G(q)=\sum_{r\le q}{\mu_P(r,q)\over1-K(r)}.
 \tag{6.4}
\]

For every down-set rectangle

\[
 [0,B']=\prod_i\{0,\ldots,B'_i\}\subseteq P,
\]

the accepted Green mass telescopes to

\[
 \boxed{
 \sum_{q\le B'}G(q)={1\over1-K(B')}.}
 \tag{6.5}
\]

#### Proof

After \(k\) pairs the record vector is the coordinatewise maximum of the
\(k\) feature vectors.  It is at most \(q\) exactly when every feature
vector is at most \(q\), proving the cumulative formula.  Möbius inversion
gives (6.3), and summing in \(k\) gives (6.4).  Summing (6.4) over the
rectangle cancels every Möbius term except the top cumulative value,
which is (6.5).  \(\square\)

### Corollary 6.2 (common-atom finite-phase reset no-go)

For each transported phase, the first-passage word after the renewal
segment resets every record value up to its physical strip depth \(B_i\).
Thus the intersection of the \(d\) accepted sink sets is the full product
rectangle \([0,B]\).  Every physical one-pair word has
\(h(\omega)\le B\), so

\[
 K(B)=\sum_{\omega\in\Omega}w(\omega)=\rho_{s,u}.
\]

The joint accepted resolvent is therefore

\[
 \boxed{
 \sum_{q\in P}G(q)={1\over1-\rho_{s,u}},}
 \tag{6.6}
\]

the same \(\Theta(s)\) scalar Green mass as before.  Correlation between
the transported block decompositions does not change this identity as
long as the one-pair words can be indexed by the same renewal atoms.

Even if an additional argument shrinks the accepted rectangle to
\([0,B']\), a gain follows only if

\[
 1-K(B')\gg {1\over s}.
 \tag{6.7}
\]

A fixed number of central soft record caps normally leaves
\(1-K(B')=\Theta(1/s)\), and hence still has Green mass \(\Theta(s)\).
This is the block-reset analogue of the audited two-soft-height-seam
calculation.

Therefore finitely many transported carrier equations with a common
renewal atomization, used only through their record maxima and their
complete first-passage reset sink sets, cannot remove the diagonal mode.

For two genuinely nonaligned phases, crossings of the two marked height
seams can interlace, so there need not be one common sequence
\(\omega_1,\ldots,\omega_k\) to which Theorem 6.1 applies.  The exact
joint state must then also retain which phase's renewal atom is currently
open.  The product-poset telescope does **not** by itself settle that
interlaced automaton.  This is the smallest surviving two-phase question:
does interlacing force a non-down-set sink condition with
\(1-K\gg1/s\), or can its states be regrouped into larger common atoms and
restore (6.6)?

## 7. Annealed versus actual PBBS state

There is one final scope distinction.  The state \((a,p)\) is exact for
parsing a word into capped blocks, and (3.4) is an exact coefficientwise
decomposition after summing over all possible lower and upper loop words.
It is therefore an **annealed** transfer.  Once an actual PBBS root has
selected the current block word, the next separator location also depends
on the unconsumed residual word.  Two actual histories can have the same
\((a,p)\) and different next marked endpoints; this is the memory
obstruction proved in
`MATH_ATTACK_OCR_ACTUAL_MARKOV_MEMORY_AND_FOURIER_TEST_20260725.md`.

Accordingly, the exact hierarchy is:

1. one phase, annealed record state: scalar mass is restored by Theorem
   4.2;
2. finitely many phases with common annealed atoms: scalar mass is restored
   by Theorem 6.1;
3. two interlaced transported phases with residual-word memory: open.

The synchronized forward/dual endpoint relaxation has already been solved
at the annealed level in
`MATH_ATTACK_OCR_SYNCHRONIZED_CELL_GREEN_NOGO_20260725.md`: its full-cell
matrix has a unit invariant mode and an explicit corner family of total
mass \(\Theta(s)\).  Known genuine separator-spanning families alternate
sides and therefore do not load that corner.  Thus the cleanest surviving
statement is an **actual-PBBS anti-corner theorem**: histories with long
same-side runs, while retaining their residual block words and an
intermediate transported cut, must have total projected mass \(o(s)\).
