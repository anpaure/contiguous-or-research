# From tensor-packet outer collisions to the contiguous-OR width bound

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Endgame theorem and verdict

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\left\lfloor\frac m4\right\rfloor .
 \tag{0.1}
\]

Choose a power of two \(r\) satisfying

\[
 2\le r\le\frac{3B}{64}.
 \tag{0.2}
\]

The canonical first-\(r\)-eligible tensor packets retain \(G=W-E\)
middle owners, where

\[
 \boxed{
 \frac EW\le
 2(m+1)\exp\!\left(-\frac{3B}{256}\right).}
 \tag{0.3}
\]

Every retained packet has an exact factor into physical \(C_{4r}\)'s.
Using the recursive nonlinear cube factor, both physical signed
depth-\(q\) maps are injective on each whole packet, simultaneously for

\[
 1\le q\le r.
 \tag{0.4}
\]

Consequently every repetition of a physical shadow is a collision between
different packets.

Fix a residual coordinate \(z\) outside the labelled eight-blocks and an
integer

\[
 3\le g\le r.
 \tag{0.5}
\]

The strongest full-collar collision inequality supplied by this certified
occurrence ledger is

\[
 \boxed{
 \nu(2m+1)\le
 W+\frac{(g-1)G}{2r}
 +\mathcal A_{m,g}
 +\Xi_{m,g}
 +2L_m(m-g).}
 \tag{0.6}
\]

Here:

* \(L_m\) is the exact factor-blind product-SCD length;
* \((g-1)G/(2r)\) is the exact optimized tensor-cycle collar;
* \(\mathcal A_{m,g}\) is the exact certified capacity shortage caused by
  the middle leave; and
* \(\Xi_{m,g}\) is the sum of the baseline-corrected physical duplicate
  masses. Packet injectivity makes every term of \(\Xi_{m,g}\) genuinely
  cross-packet.

For all sufficiently large \(m\),

\[
 \boxed{\mathcal A_{m,g}=E,}
 \tag{0.7}
\]

so (0.6) becomes

\[
 \boxed{
 \nu(2m+1)\le
 W+\frac{(g-1)(W-E)}{2r}
 +E+\Xi_{m,g}
 +2L_m(m-g).}
 \tag{0.8}
\]

There is no further seam, leave, parity, or tail-interface charge.

Take

\[
 r_m=
 2^{\left\lfloor\log_2(3B/64)\right\rfloor}.
 \tag{0.9}
\]

Then

\[
 \frac{3B}{128}<r_m\le\frac{3B}{64},
 \qquad r_m=\Theta(m),
 \tag{0.10}
\]

and (0.3) remains valid. Thus the deterministic noncollision part of
(0.8), normalized by \(W\), is

\[
 O\!\left(\frac gm\right)
 +O\!\left(m e^{-3B/256}\right)
 +\frac{2L_m(m-g)}W.
 \tag{0.11}
\]

This yields the clean final conditional theorem.

### Endgame theorem

Assume that, for every fixed \(a>0\), with

\[
 g=\lceil a\sqrt m\rceil,\qquad r=r_m,
 \tag{0.12}
\]

one can choose one certified recursive-factor conjugate in each product
cell (equivalently, one packet factor assembled from those choices) so
that

\[
 \boxed{\Xi_{m,g}=o_a(W).}
 \tag{RSTC}
\]

Then

\[
 \nu(k)=
 \left(1+o(1)\right)
 \binom{k}{\lfloor k/2\rfloor}.
 \tag{0.13}
\]

No uniformity in \(a\) is required. Indeed, the exact fixed-Gaussian tail
profile gives

\[
 \limsup_{m\to\infty}
 \frac{\nu(2m+1)}W
 \le1+T(a),
 \tag{0.14}
\]

where

\[
 \begin{aligned}
 T(a)={}&
 4\left(a^2+\frac12\right)e^{-a^2}\operatorname{erf}(a)
 +\frac{4a}{\sqrt\pi}e^{-2a^2}\\
 &+2\sqrt2\,\operatorname{erfc}(\sqrt2a),
 \end{aligned}
 \tag{0.15}
\]

and \(T(a)\to0\) as \(a\to\infty\). The exact trimmed lift

\[
 \nu(2m+2)\le2\nu(2m+1),
 \qquad
 \binom{2m+2}{m+1}=2W
 \tag{0.16}
\]

transfers the normalized bound to even dimensions without loss.

The standard antichain endpoint injection gives

\[
 \nu(k)\ge\binom{k}{\lfloor k/2\rfloor}.
\]

Combining this established width lower bound with the preceding upper
bounds proves (0.13).

Thus the only new construction gate in this endgame is (RSTC), the
structured outer cross-packet collision theorem. Middle ownership, internal
injectivity, literal compilation, the optimized collar, product-SCD tails,
leave accounting, and parity transfer are all proved.

## 1. The three corrections needed before composition

Three bookkeeping corrections are essential.

### 1.1 Odd signed depths are not symmetric

For an oriented middle-state cycle

\[
 X_0,X_1,\ldots,
 \qquad |X_i|=m,
\]

define

\[
 L_{i,q}=\bigcap_{u=0}^qX_{i+u},
 \qquad
 U_{i,q}=\bigcup_{u=0}^qX_{i+u}.
 \tag{1.1}
\]

Then

\[
 |L_{i,q}|=m-q,\qquad |U_{i,q}|=m+q.
 \tag{1.2}
\]

Thus the complement-paired upper rank \(m+1+q\) is physical
union-depth \(q+1\), not depth \(q\). A finite odd-dimensional theorem

\[
 N_q^-=\binom{2m+1}{m-q},\qquad
 N_q^+=\binom{2m+1}{m+q},
 \tag{1.3}
\]

or shift the upper depth by one. The single-\(N_q\) formula in the raw
internal-injectivity report is not a correct finite odd-dimensional
ledger.

### 1.2 Duplicate mass is not pair energy

For a multiplicity vector \(n(T)\), define

\[
 C=\sum_T(n(T)-1)_+,
 \qquad
 P=\sum_T\binom{n(T)}2.
 \tag{1.4}
\]

Always \(C\le P\), but equality need not hold when a target has load at
least three. The exact raw-collision theorem uses \(C\). A theorem whose
input is \(P\) needs the variational or floor-normalized conversion in
Section 8.

### 1.3 The product tail overlaps its nominal boundary

The odd trimmed lift of the even product-SCD word covers more than the
rank exterior stated in its black-box corollary. This overlap permits the
one-letter-per-cycle improvement in (0.6), and a second one-letter
improvement after splitting cycles by the residual coordinate \(z\).

## 2. Exact tensor packets at a linear dyadic scale

Fix \(B\) disjoint labelled eight-coordinate blocks. In each block the
24-state frame is

\[
 \mathcal V=
 \left\{
 X\cup Y:
 X\in\binom{\{a,b,c,d\}}2,\quad
 Y\in\{uw,ux,vw,vx\}
 \right\}.
 \tag{2.1}
\]

A middle owner is eligible in a block when its restriction belongs to
\(\mathcal V\). The first \(r\) eligible blocks are varied and every
other coordinate is frozen. This partitions all owners having at least
\(r\) eligible blocks into packets isomorphic to \(\mathcal V^r\).

The exact finite leave proof uses only (0.2), not \(r=o(m)\). Before
conditioning on middle rank, the number of eligible blocks is

\[
 \operatorname{Bin}\left(B,\frac3{32}\right),
\]

with mean \(3B/32\). Condition (0.2) puts \(r\) at most half the mean.
Chernoff's inequality and the elementary lower bound on the middle
conditioning probability give (0.3).

### Lemma 2.0 (finite linear-scale extension)

The canonical packet partition, explicit leave bound, tensor-cell
decomposition, and recursive cycle factor remain valid for every dyadic
\(r\) satisfying (0.2), including \(r=\Theta(m)\).

#### Proof

The first-\(r\) rule is an exact equivalence relation for every \(r\le B\).
The leave proof uses only \(r\le3B/64\), as just shown. The tensor-cell
decomposition is a Cartesian identity for every \(r\), and its fixed core
has size

\[
 m-2r\ge0
\]

under (0.2). Finally, the recursive factor needs only that \(2r\) be a
power of two. None of these four finite statements invokes
\(r/m\to0\). \(\square\)

Thus the older \(r=o(m)\) clause is a convenient asymptotic sufficient
regime, not a hypothesis of the finite construction used here.

For every packet, choose one of the six-\(Q_2\) resolutions in each local
block. The packet is partitioned into \(6^r\) physical copies of

\[
 Q_{2r}.
 \tag{2.2}
\]

Since \(2r\) is a power of two, the recursive nonlinear neighbor
permutation factors every cell into isometric \(C_{4r}\)'s. The
face-separation theorem and recursive shadow theorem imply:

### Theorem 2.1 (packet-wide internal injectivity)

For every packet and every \(1\le q\le r\), both maps

\[
 x\longmapsto\bigcap_{u=0}^qF^u(x),
 \qquad
 x\longmapsto\bigcup_{u=0}^qF^u(x)
 \tag{2.3}
\]

are injective on the whole packet, including across distinct product
cells and distinct factor cycles.

This remains true if the recursive factor is independently conjugated by
a cube automorphism in each product cell. Conjugation preserves
within-cell injectivity, while the local face-separation theorem lets a
physical target recover its product cell before the within-cell inverse is
applied.

The retained factor therefore has exactly

\[
 p=\frac{G}{4r}
 \tag{2.4}
\]

cycles. Every physical collision at a certified depth uses occurrences
from distinct packets.

The blocks occupy \(8B\) coordinates. Their complement has odd size

\[
 2(m\bmod4)+1\in\{1,3,5,7\}.
 \tag{2.5}
\]

Fix one coordinate \(z\) in this residual set. It is frozen on every
packet and therefore on every factor cycle.

## 3. Exact product-tail overlap

Let \(V=[n]\setminus\{z\}\), so \(|V|=2m\), and split \(V\) into two
\(m\)-sets for the product-SCD construction.

Use its even parameter

\[
 r_{\rm tail}=m-g.
 \tag{3.1}
\]

The even word covers every nonempty \(S\subseteq V\) satisfying

\[
 |S|\le m-g
 \quad\text{or}\quad
 |S|\ge m+g.
 \tag{3.2}
\]

Its exact trimmed lift has length

\[
 2L_m(m-g).
 \tag{3.3}
\]

Besides every odd-dimensional target of rank at most \(m-g\) or at least
\(m+g+1\), it also covers the two boundary families

\[
 \boxed{
 \begin{aligned}
 \mathcal Q^-_{\partial}
 &=
 \left\{S:|S|=m-g+1,\ z\in S\right\},\\
 \mathcal Q^+_{\partial}
 &=
 \left\{S:|S|=m+g,\ z\notin S\right\}.
 \end{aligned}}
 \tag{3.4}
\]

Indeed, deleting \(z\) from a member of the first family gives an even
target of rank \(m-g\), while a member of the second family is itself an
even target of rank \(m+g\).

Consequently Stage A only needs the following resources:

\[
 \begin{array}{c|c}
 \text{resource}&\text{required targets}\\ \hline
 (-,q),\ 1\le q\le g-2&
 \displaystyle\binom{[n]}{m-q}\\[1mm]
 (+,q),\ 1\le q\le g-1&
 \displaystyle\binom{[n]}{m+q}\\[1mm]
 (-,\partial)&
 \{S:|S|=m-g+1,\ z\notin S\}\\[1mm]
 (+,\partial)&
 \{S:|S|=m+g,\ z\in S\}.
 \end{array}
 \tag{3.5}
\]

The two boundary resource sets have the common size

\[
 Q_g=\binom{2m}{m-g+1}.
 \tag{3.6}
\]

Together with the middle rank, (3.2)--(3.5) partition all nonempty target
ranks by responsibility. No target is left at an interface seam.

## 4. The finite-delay factor and optimized collars

We first record the literal compiler.

### Lemma 4.1 (finite-delay factor)

Let \(T=(T_1,\ldots,T_v)\) be a set-valued sequence such that no coordinate
changes twice among any \(d+1\) consecutive transitions. Define

\[
 A_j=
 \bigcap_{i=\max(1,j-d)}^{\min(v,j)}T_i,
 \qquad 1\le j\le v+d.
 \tag{4.1}
\]

Then

\[
 T_i=\bigcup_{j=i}^{i+d}A_j,
 \tag{4.2}
\]

\[
 \bigcap_{i=a}^bT_i
 =\bigcup_{j=b}^{a+d}A_j
 \qquad(b-a\le d),
 \tag{4.3}
\]

and

\[
 \bigcup_{i=a}^bT_i
 =\bigcup_{j=a}^{b+d}A_j
 \tag{4.4}
\]

with no restriction on \(b-a\) in (4.4).

#### Proof

Fix one coordinate and inspect its zero-one state string. Every internal
positive run has at least \(d+1\) states; a boundary run may use the
truncation in (4.1). If the coordinate is present at \(T_i\), its positive
run contains a defining all-one window whose right endpoint belongs to
\([i,i+d]\), proving (4.2). If it is present throughout \([a,b]\) with
\(b-a\le d\), the same argument places a defining endpoint in
\([b,a+d]\), proving (4.3). Taking the union of (4.2) over
\(a\le i\le b\) gives (4.4). \(\square\)

Let \(\mathscr C_0\) be the retained \(C_{4r}\)'s whose middle owners omit
\(z\), and let \(\mathscr C_1\) be those whose middle owners contain \(z\).
Put

\[
 G_\alpha=4r|\mathscr C_\alpha|,
 \qquad G_0+G_1=G.
 \tag{4.5}
\]

For a cycle \(C\in\mathscr C_\alpha\), choose a copied-prefix length
\(\sigma_C\) in the range

\[
 \begin{array}{c|c|c}
 \alpha&\text{delay }d_\alpha&\text{allowed }\sigma_C\\ \hline
 0&g-1&0\le\sigma_C\le g-1,\\
 1&g-2&0\le\sigma_C\le g.
 \end{array}
 \tag{4.6}
\]

Cut the cycle, copy its first \(\sigma_C\) middle states, and apply
Lemma 4.1 with delay \(d_\alpha\). The resulting factor word has length

\[
 4r+d_\alpha+\sigma_C.
 \tag{4.7}
\]

The asymmetric choice of delays is legal because:

* on a \(z\)-free cycle, Stage A needs lower and upper physical depths
  only through \(g-1\);
* on a \(z\)-containing cycle, it needs lower depth only through \(g-2\),
  while the unrestricted union identity (4.4) reaches upper depth \(g\).

Every certified recursive factor, and every cube-automorphism conjugate of
it, has cycle direction word \(\pi\pi\), where \(\pi\) is a permutation
of the \(2r\) disjoint physical pair directions. Hence a cyclic block of
at most \(2r\) transitions uses each physical coordinate at most once.
Since

\[
 d_0+1=g\le r,\qquad d_1+1=g-1\le r,
\]

no physical coordinate changes twice in the defining delay windows. This
property survives cutting and copying a prefix. Hence both linearized
sequences are delay-safe. The upper identity has no delay restriction.

A physical depth-\(q\) cyclic window is available after the cut precisely
when it uses at most \(\sigma_C\) copied states. Therefore exactly

\[
 (q-\sigma_C)_+
 \tag{4.8}
\]

of its \(4r\) cyclic starts are unavailable.

### Full tail-aligned collars

Choose

\[
 \sigma_C=
 \begin{cases}
 g-1,&C\in\mathscr C_0,\\
 g,&C\in\mathscr C_1.
 \end{cases}
 \tag{4.9}
\]

Every required window in (3.5) is then available. Remarkably, both cycle
types have the same exact cost:

\[
 d_\alpha+\sigma_C=2g-2.
 \tag{4.10}
\]

Thus the complete collar charge is

\[
 \boxed{
 (2g-2)p=\frac{(g-1)G}{2r}.}
 \tag{4.11}
\]

This is two letters per cycle smaller than the naive delay-\(g\),
prefix-\(g\) compiler, and one letter smaller than the usual
odd-asymmetric delay-\((g-1)\), prefix-\(g\) compiler. Both savings come
from the guaranteed boundary families already covered by the trimmed
product tail.

### Partial collars

The variable-\(\sigma_C\) theorem below is exact. Without using actual
target overlap, however, no partial collar has a smaller worst-case
seam-plus-repair charge than (4.10).

For \(C\in\mathscr C_0\), the support-free charge is

\[
 g-1+\sigma_C+
 2\sum_{q=1}^{g-1}(q-\sigma_C)_+.
 \tag{4.12}
\]

It is uniquely minimized at \(\sigma_C=g-1\), with value \(2g-2\).

For \(C\in\mathscr C_1\), it is

\[
 g-2+\sigma_C+
 \sum_{q=1}^{g-2}(q-\sigma_C)_+
 \sum_{q=1}^{g}(q-\sigma_C)_+.
 \tag{4.13}
\]

Its minimum \(2g-2\) occurs at

\[
 \sigma_C\in\{g-1,g\}.
 \tag{4.14}
\]

Thus partial collars improve (4.11) only when the lost occurrences are
already redundant. The master theorem records that possibility exactly.

## 5. Exact cross-packet collision algebra

Let \(\mathcal T\) be any one of the target resource sets in (3.5).
Let \(\Omega\) be the certified available occurrences assigned to it, and
put

\[
 N=|\mathcal T|,\qquad A=|\Omega|.
 \tag{5.1}
\]

For \(T\in\mathcal T\), let \(n(T)\) be its multiplicity and define

\[
 C=\sum_{T\in\mathcal T}(n(T)-1)_+.
 \tag{5.2}
\]

If \(K\) targets occur, then

\[
 C=A-K.
 \tag{5.3}
\]

Hence the number \(M=N-K\) of holes satisfies

\[
 \boxed{M=N-A+C.}
 \tag{5.4}
\]

Define the baseline-corrected duplicate mass

\[
 \boxed{
 X=C-(A-N)_+.}
 \tag{5.5}
\]

Since \(K\le N\), equation (5.3) gives \(C\ge(A-N)_+\), so \(X\ge0\).
Equations (5.4)--(5.5) give the exact identity

\[
 \boxed{
 M=(N-A)_++X.}
 \tag{5.6}
\]

By Theorem 2.1, one packet contributes at most one occurrence to a fixed
resource target. Therefore every unit counted in \(C\), and hence in
\(X\), is a collision between distinct packets.

Moreover the pair energy is exactly

\[
 \boxed{
 P=\sum_T\binom{n(T)}2
 =\sum_{\mathscr P<\mathscr P'}
 |\operatorname{Im}_{\mathscr P}
   \cap\operatorname{Im}_{\mathscr P'}|.}
 \tag{5.7}
\]

There is no diagonal or same-packet contribution.

## 6. Strongest finite theorem with arbitrary collars

Let

\[
 \mathfrak J_g^\circ=
 \{(-,q):1\le q\le g-2\}
 \cup
 \{(+,q):1\le q\le g-1\}.
 \tag{6.1}
\]

For \((\epsilon,q)\in\mathfrak J_g^\circ\), let
\(\mathcal T_q^\epsilon\) be the full target layer from (3.5). Its
available occurrence count is

\[
 A_q^\epsilon
 =
 \sum_{C\in\mathscr C_0\cup\mathscr C_1}
 \bigl(4r-(q-\sigma_C)_+\bigr).
 \tag{6.2}
\]

For the boundary resources,

\[
 A_\partial^-=
 \sum_{C\in\mathscr C_0}
 \bigl(4r-(g-1-\sigma_C)_+\bigr),
 \tag{6.3}
\]

\[
 A_\partial^+=
 \sum_{C\in\mathscr C_1}
 \bigl(4r-(g-\sigma_C)_+\bigr).
 \tag{6.4}
\]

Define \(N_j,A_j,C_j,X_j,M_j\) for every

\[
 j\in\mathfrak J_g:=
 \mathfrak J_g^\circ\cup\{-,\partial; +,\partial\}
 \tag{6.5}
\]

by Sections 3 and 5.

### Theorem 6.1 (master tensor-collision inequality)

For every packet factor assembled from certified recursive nonlinear
factors and their cube-automorphism conjugates, every allowed family of
copied-prefix lengths, and every \(3\le g\le r\),

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&
 W+
 \sum_{C\in\mathscr C_0\cup\mathscr C_1}
 (d_{\alpha(C)}+\sigma_C)\\
 &+
 \sum_{j\in\mathfrak J_g}
 \bigl((N_j-A_j)_++X_j\bigr)
 +2L_m(m-g).
 \end{aligned}}
 \tag{6.6}
\]

Every object in the constructed word is literal and integral.

#### Proof

The finite-delay factor words have total length

\[
 G+
 \sum_C(d_{\alpha(C)}+\sigma_C).
 \tag{6.7}
\]

Every retained middle owner is represented by (4.2). Append each of the
\(E=W-G\) omitted middle owners once. The baseline becomes exactly

\[
 W+\sum_C(d_{\alpha(C)}+\sigma_C).
 \tag{6.8}
\]

Lemma 4.1 represents every available lower or upper resource window.
Append each missing resource target once. By (5.6), this costs the middle
sum in (6.6). Finally append the product-SCD word from Section 3. It covers
the complement of the Stage-A resources, including both free boundary
families (3.4), at cost \(2L_m(m-g)\).

Every witness is internal to one factor, repair, or tail block.
Concatenation preserves all witnesses, so there is no cross-block seam
charge. \(\square\)

Equation (6.6) is strongest at the level of the certified occurrence
maps: it charges the actual cut-dependent target holes exactly. Accidental
witnesses elsewhere can only shorten the final word.

## 7. Full-collar endgame inequality

Use (4.9). For every interior resource,

\[
 A_q^\epsilon=G.
 \tag{7.1}
\]

At the boundaries,

\[
 A_\partial^-=G_0,\qquad A_\partial^+=G_1.
 \tag{7.2}
\]

Put

\[
 \boxed{
 \begin{aligned}
 \mathcal A_{m,g}:={}&
 \sum_{q=1}^{g-2}
 \left(\binom{n}{m-q}-G\right)_+\\
 &+
 \sum_{q=1}^{g-1}
 \left(\binom{n}{m+q}-G\right)_+\\
 &+
 (Q_g-G_0)_+
 +(Q_g-G_1)_+,
 \end{aligned}}
 \tag{7.3}
\]

and

\[
 \boxed{
 \Xi_{m,g}:=
 \sum_{j\in\mathfrak J_g}X_j.}
 \tag{7.4}
\]

Theorem 6.1 and (4.11) give (0.6).

To prove (0.7), first note

\[
 \binom{n}{m+1}=W.
 \tag{7.5}
\]

This is the \(q=1\) term of the upper sum in (7.3), and it contributes

\[
 W-G=E.
 \tag{7.6}
\]

Every other full target layer in (7.3) has size at most

\[
 \binom{n}{m-1}
 =W\frac{m}{m+2},
 \tag{7.7}
\]

whose gap below \(W\) is \(2W/(m+2)\). The exponential bound (0.3)
eventually makes \(E\) smaller than this gap, so all those positive parts
vanish.

Because \(z\) lies outside the eight-blocks, the total middle masses in
its two fibres are

\[
 W_0=\binom{2m}{m},\qquad
 W_1=\binom{2m}{m-1},
 \tag{7.8}
\]

and

\[
 G_\alpha=W_\alpha-E_\alpha,\qquad
 0\le E_\alpha\le E.
 \tag{7.9}
\]

For \(g\ge3\),

\[
 Q_g=\binom{2m}{m-g+1}
 \le\binom{2m}{m-2}<W_1<W_0.
 \tag{7.10}
\]

The gaps in (7.10) are polynomially larger than the exponential leave.
Thus \(G_0,G_1\ge Q_g\) for all sufficiently large \(m\), and both
boundary positive parts vanish. This proves (0.7) and hence (0.8).

An explicit sufficient finite condition for this simplification is

\[
 \boxed{
 \frac EW\le
 \min\left\{
 \frac2{m+2},
 \frac{3m}{(2m+1)(m+2)}
 \right\}.}
 \tag{7.11}
\]

Indeed, the first term handles every noncentral full layer. For the
boundary fibres, the smallest gap occurs at \(g=3\) on the
\(z\)-containing side, and

\[
 \binom{2m}{m-1}-\binom{2m}{m-2}
 =
 \frac{3m}{(2m+1)(m+2)}W.
 \tag{7.12}
\]

The lower \(z\)-free gap is larger. Thus (7.11) proves
\(\mathcal A_{m,g}=E\) without asymptotic notation.

The middle leave has therefore been fully optimized within this certified
singleton-repair ledger:

* appending omitted middle owners cancels the missing mass in the baseline
  \(G\), leaving \(W\);
* only one additional certified capacity term survives, namely \(E\) in
  the upper rank \(m+1\);
* no factor \(gE\), \(HE\), or \(\sqrt m\,E\) occurs.

### Corollary 7.1 (standard full-layer collision gate)

Some tensor statements are naturally formulated on complete signed
layers. Let \(C_q^\pm\) be the duplicate masses of all \(G\) cyclic starts
at physical depth \(q\), and put

\[
 \widetilde X_q^\pm
 =
 C_q^\pm-(G-N_q^\pm)_+,
 \tag{7.13}
\]

\[
 \boxed{
 \widetilde\Xi_{m,g}
 =
 \sum_{q=1}^{g-1}\widetilde X_q^-
 +
 \sum_{q=1}^{g}\widetilde X_q^+.}
 \tag{7.14}
\]

The required boundary resources are subsets of the two complete boundary
layers, while every omitted complementary boundary target is covered by
the product tail. Therefore their certified missing mass is at most the
missing mass of the complete layers. Under (7.11),

\[
 \boxed{
 \nu(2m+1)\le
 W+\frac{(g-1)G}{2r}
 +E+\widetilde\Xi_{m,g}
 +2L_m(m-g).}
 \tag{7.15}
\]

Thus the standard full-layer outer theorem

\[
 \widetilde\Xi_{m,g}=o(W)
\]

is a clean sufficient substitute for the sharper boundary-resolved
condition (RSTC). Equation (0.8) remains the stronger finite statement.

## 8. Exact conversion from cross-packet pair energy

Suppose the available input is the quadratic pair census \(P\), rather
than the raw duplicate mass \(X\).

For integers \(A,N,P\), define

\[
 K_{\rm ex}(A,N,P)=
 \min\left\{
 K:
 \begin{array}{l}
 0\le K\le\min(A,N),\\
 x_1,\ldots,x_K\in\mathbb Z_{\ge1},\\
 \sum_i x_i=A,\quad
 \sum_i\binom{x_i}{2}=P
 \end{array}
 \right\}.
 \tag{8.1}
\]

For \(A=P=0\), the empty vector with \(K=0\) is allowed. For physical
data the defining family is nonempty. Put

\[
 \Psi(A,N,P)=N-K_{\rm ex}(A,N,P).
 \tag{8.2}
\]

### Theorem 8.1 (sharp scalar pair-energy conversion)

For any resource multiplicity vector with data \((A,N,P)\),

\[
 \boxed{M\le\Psi(A,N,P).}
 \tag{8.3}
\]

No stronger upper bound on \(M\) follows from the three integers
\((A,N,P)\) alone among arbitrary scalar multiplicity vectors. Additional
packet-realizability structure can in principle strengthen it.

#### Proof

The positive multiplicities of the physical vector give one admissible
choice in (8.1), with \(K=N-M\). Hence

\[
 K\ge K_{\rm ex},
\]

which is (8.3). Conversely, a minimizing vector in (8.1), placed on
\(K_{\rm ex}\) of the \(N\) targets, attains equality using only the scalar
data. \(\square\)

Since every \(P_j\) is cross-packet by (5.7), Theorem 6.1 has the
pair-energy corollary

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&
 W+\sum_C(d_{\alpha(C)}+\sigma_C)\\
 &+\sum_{j\in\mathfrak J_g}
 \Psi(A_j,N_j,P_j)
 +2L_m(m-g).
 \end{aligned}}
 \tag{8.4}
\]

For a closed-form relaxation, let

\[
 a=\left\lfloor\frac AN\right\rfloor.
 \tag{8.5}
\]

If \(a=0\), then

\[
 \boxed{M\le N-A+P.}
 \tag{8.6}
\]

Indeed \(M=N-A+C\) and \((t-1)_+\le\binom t2\).

If \(a\ge1\), define the exact balanced floor

\[
 P_{\rm bal}(A,N)
 =aA-\binom{a+1}{2}N.
 \tag{8.7}
\]

Then

\[
 \boxed{
 M\le
 \left\lfloor
 \frac{P-P_{\rm bal}(A,N)}
 {\binom{a+1}{2}}
 \right\rfloor.}
 \tag{8.8}
\]

To prove (8.8), sum the nonnegative integer polynomial

\[
 (n(T)-a)(n(T)-a-1)
\]

over all \(N\) targets. The result is

\[
 2(P-P_{\rm bal}),
\]

and each hole contributes \(a(a+1)=2\binom{a+1}{2}\).

Equations (8.6)--(8.8) must use the floor determined by the actual
resource occurrence mass \(A\), not automatically by \(W\) or \(G\).
This matters at cut boundaries and in the two \(z\)-fibres.

## 9. Optimizing the packet scale and window

### 9.1 Packet scale

The collar in (0.8) decreases monotonically with \(r\), while the proved
uniform leave envelope (0.3) is unchanged throughout (0.2). Therefore the
largest dyadic \(r\), namely (0.9), optimizes the known collar-plus-leave
terms and gives \(r=\Theta(m)\). It need not optimize the unknown
collision term \(\Xi_{m,g}\) or the geometry of the available factor menu.

The historical restriction \(r=o(m)\) is not used by the finite leave
proof or the tensor factor. It is sufficient, but not necessary. The
linear choice (0.9) is still far below the mean eligible-block count and
leaves a positive exterior core.

### 9.2 A single growing window

For

\[
 \sqrt m\le g=o(m^{2/3}),
\]

the sharp audited product-SCD estimate gives

\[
 L_m(m-g)
 \le
 C_1\left(1+\frac{g^2}{m}\right)
 \binom{2m}{m-g},
 \tag{9.1}
\]

and

\[
 \frac{\binom{2m}{m-g}}{\binom{2m}{m}}
 \le
 \exp\!\left(-\frac{g^2}{m+g}\right).
 \tag{9.2}
\]

Since

\[
 W=\frac{2m+1}{m+1}\binom{2m}{m},
\]

the explicit noncollision envelope in (0.8) is

\[
 O\!\left(\frac gm\right)
 +
 O\!\left(
 \left(1+\frac{g^2}{m}\right)
 e^{-g^2/(m+g)}
 \right)
 +e^{-\Omega(m)}.
 \tag{9.3}
\]

Put \(x=g^2/m\). Ignoring fixed absolute prefactors, differentiating

\[
 \frac{\sqrt x}{\sqrt m}+(1+x)e^{-x}
 \tag{9.4}
\]

gives

\[
 e^{-x}x^{3/2}\asymp m^{-1/2}.
 \tag{9.5}
\]

Thus the asymptotically optimized known noncollision window satisfies

\[
 \boxed{
 x=
 \frac12\log m+
 \frac32\log\log m+O(1),}
 \tag{9.6}
\]

or

\[
 g=
 \sqrt{
 m\left(
 \frac12\log m+
 \frac32\log\log m+O(1)
 \right)}.
 \tag{9.7}
\]

For a completely explicit choice, one may take

\[
 g_*=
 \left\lceil
 \sqrt{m\left(\frac12\log m+2\log\log m\right)}
 \right\rceil.
 \tag{9.8}
\]

Then the known noncollision error is

\[
 O\!\left(\sqrt{\frac{\log m}{m}}\right).
 \tag{9.9}
\]

This optimizes only the proved collar-plus-tail envelope. The total
optimum can shift if the eventual theorem for \(\Xi_{m,g}\) has its own
nontrivial dependence on \(g\).

### 9.3 Fixed-window diagonalization is logically weaker

A final proof need not establish (RSTC) uniformly at the growing scale
(9.8). It is enough to prove it for every fixed

\[
 g=\lceil a\sqrt m\rceil.
\]

The collar and leave then vanish for fixed \(a\), while the exact tail
has the fixed profile \(T(a)\). First let \(m\to\infty\), then
\(a\to\infty\). This proves (0.13) with strictly weaker collision
quantifiers.

## 10. Exact parity transfer

Let

\[
 U=(U_1,\ldots,U_s)
\]

be a universal word of nonempty subsets of \([k]\), and let \(z\) be a
new coordinate. The trimmed lift

\[
 U_1,\ldots,U_s,\{z\},
 U_1\cup\{z\},\ldots,U_{s-1}\cup\{z\}
 \tag{10.1}
\]

has exactly \(2s\) entries and is universal on \([k]\cup\{z\}\).

Old targets retain their witnesses. The singleton \(\{z\}\) is explicit.
If \(U_i,\ldots,U_j\) witnesses \(S\) and \(j<s\), use the corresponding
interval in the transformed copy for \(S\cup\{z\}\). If \(j=s\), use

\[
 U_i,\ldots,U_s,\{z\}.
\]

Thus

\[
 \boxed{\nu(k+1)\le2\nu(k)}
 \tag{10.2}
\]

with no additive endpoint or seam term.

If an odd theorem gives the finite bound

\[
 \nu(2m+1)\le W+\mathcal E_m,
\]

then

\[
 \boxed{
 \nu(2m+2)
 \le
 \binom{2m+2}{m+1}+2\mathcal E_m,}
 \tag{10.3}
\]

because

\[
 \binom{2m+2}{m+1}=2W.
\]

Equivalently,

\[
 \frac{\nu(2m+2)}{\binom{2m+2}{m+1}}
 \le
 \frac{\nu(2m+1)}{\binom{2m+1}{m}}.
 \tag{10.4}
\]

Every odd leave, collision, collar, and tail term doubles in absolute
size and is unchanged after width normalization. The lift must be applied
after the odd word is completed; it does not erase an unrepaired leave.

## 11. Precise implication boundary

The following statements are proved.

1. Lemma 2.0 extends the canonical packet construction and explicit
   exponential leave (0.3) to the linear dyadic scale (0.9).
2. The recursive nonlinear factor gives packet-wide two-sided internal
   injectivity through depth \(r\).
3. The trimmed product-SCD tail supplies the boundary overlap (3.4).
4. The finite-delay compiler and the \(z\)-fibre split reduce the exact
   full collar to \(2g-2\) letters per \(C_{4r}\).
5. The arbitrary-collar inequality (6.6), the full-collar inequality
   (0.6), and the simplified exact endgame (0.8) are literal.
6. Raw duplicate excess gives the exact hole identity (5.6).
7. Pair energy gives the sharp scalar inverse (8.3) and the audited
   floor relaxations (8.6)--(8.8).
8. The packet scale, tail/collar window, and odd-to-even transfer are
   optimized as stated.

The following statement remains unproved.

> Choose one legal recursive-factor conjugate in every canonical product
> cell so that the assembled packet factors have aggregate
> baseline-corrected physical cross-packet collision mass
> \(\Xi_{m,\lceil a\sqrt m\rceil}=o_a(W)\), simultaneously at all required
> signed depths.

Independent uniform factor conjugation does not prove this: the outer
collision hypergraph has average load near one at shallow ranks, and
Jensen's inequality leaves an asymptotic \(e^{-1}\) fraction of targets
uncovered. The missing theorem must be a structured multiple-choice
covering, discrepancy, or exact-cut theorem.

No conclusion from first marginals, packetwise injectivity alone, or raw
pair energy without subtracting its integral floor may be substituted for
(RSTC).

## 12. Audit checklist

1. The packet cycle length is \(4r\), so the component count is
   \(G/(4r)\).
2. Lower physical depth \(q\) has rank \(m-q\); upper physical depth \(q\)
   has rank \(m+q\).
3. The product tail \(2L_m(m-g)\) leaves full lower depths only through
   \(g-2\) and full upper depths only through \(g-1\); its two guaranteed
   boundary halves are treated in (3.4).
4. The \(z\)-free compiler uses delay and prefix \(g-1,g-1\); the
   \(z\)-containing compiler uses \(g-2,g\). Both cost \(2g-2\).
5. The union identity is unrestricted in interval length, so upper depth
   \(g\) on the \(z\)-containing cycles is legal with delay \(g-2\).
6. The collar charge is \((g-1)G/(2r)\), not
   \(HG/r\), \(2HG/r\), or an unspecified \(O(HW/r)\).
7. The omitted middle mass is appended once in the baseline. Its only
   additional eventual capacity charge is the upper-middle shortage \(E\).
8. \(C=\sum(n-1)_+\) and
   \(P=\sum\binom n2\) are never identified.
9. All \(C\) and \(P\) terms are cross-packet because same-packet
   injectivity is exact.
10. The tail block is factor-blind and creates no Stage-A seam charge.
11. The even lift has exactly twice the completed odd length and exactly
    twice the odd width.
12. The certified MSW or tensor construction is not claimed to satisfy
    (RSTC); that is the sole final gate.

Supporting proved inputs are:

* MATH_THEOREM_CANONICAL_TENSOR_ASSOCIATOR_PACKETS_20260726.md;
* MATH_THEOREM_TENSOR_PACKET_CONSECUTIVE_WINDOW_DESIGN_20260726.md;
* MATH_THEOREM_TENSOR_PACKET_INTERNAL_SHADOW_INJECTIVITY_20260726.md;
* MATH_THEOREM_CANONICAL_PACKET_OUTER_COLLISION_HYPERGRAPH_20260726.md;
* MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md;
* MATH_ATTACK_N_UNIFORM_PRODUCT_SCD_TAIL_INTERFACE_20260726.md; and
* MATH_ATTACK_N_PRODUCT_SCD_TAIL_UNIFORM_ASYMPTOTIC_20260726.md.
