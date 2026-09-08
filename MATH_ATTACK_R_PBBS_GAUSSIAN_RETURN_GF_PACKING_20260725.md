# PBBS Gaussian return classification: uniform sparse sectors and the dynamic-root obstruction

Date: 2026-07-25  
Lane: R, constant-one PBBS residence packing  
Method: pure mathematics only; no computation, finite search, SAT, or web search

## 0. Audited outcome

Put

\[
 N=2r+1,
 \qquad
 B=\operatorname{Cat}_r={1\over r+1}\binom{2r}{r}.
\]

Normalize a PBBS middle state as \(0D\), where \(D\) is a Dyck word of
semilength \(r\).  A consecutive return of the omitted physical coordinate
has odd gap \(g\), positive residence

\[
 \ell={g+1\over2},
\]

and a complement-projected trace of

\[
 k={g+3\over2}=\ell+1
\]

transition edges.

For an integer \(H\), let \(\nu_H(P_r)\) be the maximum number of pairwise
projected-edge-disjoint PBBS residence intervals of residence at most
\(H\).  The fixed-window statement required by the residence-only
constant-one reduction is

\[
 \boxed{
 \nu_{\lceil A\sqrt r\rceil}(P_r)=o_A(B)
 }
 \tag{RP_A}
\]

for every fixed \(A>0\).

This report does **not** prove or refute \(RP_A\).  It proves the following
strict advances and corrections.

1. Gap nine is present but exponentially sub-Catalan.  If \(R_9(r)\) is
   the number of normalized roots whose first return has gap nine, then

   \[
    R_9(r)
    =O\!\left(\left({3+\sqrt5\over2}\right)^r\right).
    \tag{0.1}
   \]

   Thus all gaps \(5,7,9\), even with every spatial phase granted, have
   physical packing \(o(B)\).

2. There is an exact all-gap terminal-mountain suspension.  If

   \[
    1\le L\le d,\qquad
    X\in\mathcal D_M,\qquad
    \operatorname{ht}(X)\le L,\qquad M\ge1,
   \]

   then

   \[
    D=X1^{d+L}0^{d+L}
   \]

   has first return gap \(2(d+L)+1\).  This permits arbitrarily large
   twice-pruned rank at fixed gap.

3. The entire Gaussian-range terminal-mountain library is harmless,
   including edge-disjoint packing.  Its total number of physical starts
   is

   \[
    O_A(r^4)e^{-(\pi^2/8)r^{1/3}}B=o(B).
    \tag{0.2}
   \]

4. A stronger proposed zero-winding converse is false.  The condition
   \(d_{\rm step}(D)=1\), even together with height \(3\), does not imply a
   short gap.  For every \(\beta\ge2\), the explicit root

   \[
    D_\beta=(10)^\beta\,1(1100)^\beta0
    \tag{0.3}
   \]

   has semilength \(3\beta+1\), height \(3\), and
   \(d_{\rm step}(D_\beta)=1\), but its first return is

   \[
    g_\beta=6\beta+1=N-2.
    \tag{0.4}
   \]

   This is the exact obstruction to a height/first-sector converse.

5. The literal fixed-spine sector conditions do imply a return of gap
   \(2h+1\), but their generating function has an
   \(\exp(-\Theta(h))\) penalty at the Catalan singularity.  Uniformly
   through \(h\le A\sqrt r\), this entire sufficient class again has only
   \(o(B)\) physical starts.

6. The exact inherited-terminal generating function has full Catalan
   spectral radius and bounded branching moments.  It does not count
   genuine return descents, because a real descent dynamically re-roots the
   pruned word.  The inherited and dynamic terminal products are not
   comparable.

The remaining gate is therefore the exact PBBS predecessor-occurrence
kernel together with quotient-cycle interval conflicts.  Every relaxation
which erases the dynamic root either has full Catalan spectral radius or
misses the long-gap family (0.3).

## 1. Peak lifts and the exact predecessor kernel

Let \(F=\partial D\) be obtained by deleting every peak \(10\) of \(D\).
Write

\[
 |F|_{\rm semi}=d,
 \qquad
 k=\operatorname{pk}(F).
\]

Every inverse lift is uniquely encoded by the \(2d+1\) corner variables

\[
 z_0,z_1,\ldots,z_{2d}\ge0.
\]

Variables at the \(k\) peak vertices of \(F\) are at least one.  The
terminal variable

\[
 t=z_{2d}
\]

is unrestricted.  The number of semilength-\(r\) lifts of this fixed
\(F\) with terminal value \(t\) is

\[
 w_{r,t}(F)
 =\binom{r+d-k-t-1}{2d-1},
 \tag{1.1}
\]

with the binomial-zero convention.  Equivalently,

\[
 \sum_r w_{r,t}(F)x^r
 ={x^{d+k+t}\over(1-x)^{2d}}.
 \tag{1.2}
\]

In the reduced PBBS on \(F\), let \(a\) be the distinguished equality
particle, let \(b=a-1\) be its immediate cyclic predecessor, and write

\[
 T_a(F)=\min\{j>0:\kappa_j=a\}.
\]

Let

\[
 0<B_1(F)<B_2(F)<\cdots
\]

be the positive occurrence times of \(b\).

### Theorem 1.1 (exact terminal-spacing return kernel)

Assume \(F\ne\varnothing\) and

\[
 B_{2t+2}(F)<2r+1.
\]

Then every semilength-\(r\) inverse lift of \(F\) with terminal value \(t\)
has its first outer physical return exactly at

\[
 \boxed{G_F(t)=B_{2t+2}(F).}
 \tag{1.3}
\]

Moreover

\[
 T_a(F)<B_2(F),
 \tag{1.4}
\]

so no additional root-recurrence hypothesis is needed.

#### Proof

In the cyclic word \(0D\), the last core zero, the \(t\) inserted terminal
peaks, and the leading unmatched zero form

\[
 0(10)^t0.
\]

Thus the initial physical spacing between particles \(b\) and \(a\) is

\[
 \Delta=2t+1.
\]

After the time-zero move, particle \(a\) occupies the target edge.  The
first selection of \(b\) moves it into the old edge of \(a\).  It cannot be
selected a second time while \(a\) still occupies the next edge; equality
particles do not collide or overtake.  Hence \(a\) is selected first,
proving (1.4).

Particle \(b\) must be selected \(\Delta+1=2t+2\) times to enter the target.
No other particle can overtake it, and \(a\) cannot make a full outer
circuit before the displayed no-wrap time.  Therefore this entrance is the
first repeated occurrence of the physical coordinate, proving (1.3).
\(\square\)

For \(H\) with \(2H-1<N\), define

\[
 \chi_H(F,t)
 =\mathbf1\{B_{2t+2}(F)\le2H-1\}.
\]

The exact number \(R_r(H)\) of normalized roots with a return gap at most
\(2H-1\) is

\[
 \boxed{
 R_r(H)=
 \sum_{d\ge1}\sum_{F\in\mathcal D_d}\sum_{t\ge0}
 \chi_H(F,t)
 \binom{r+d-\operatorname{pk}(F)-t-1}{2d-1}.
 }
 \tag{1.5}
\]

Its ordinary generating function is

\[
 \boxed{
 \mathcal R_H(x)=
 \sum_{d\ge1}\sum_{F\in\mathcal D_d}\sum_{t\ge0}
 \chi_H(F,t)
 {x^{d+\operatorname{pk}(F)+t}\over(1-x)^{2d}}.
 }
 \tag{1.6}
\]

These are integral identities inside the exact PBBS factor.

Rank one is exceptional.  For \(F=10\),

\[
 T_a(F)=3,
 \qquad
 B_j(F)=3j-1.
 \tag{1.7}
\]

This exception is responsible for several false product and gap exclusions
discussed below.

## 2. Gap nine: a rational uniform bound

The exact earlier classifications give

\[
 R_5(r)=r-1,
 \qquad
 R_7(r)=2^{r-1}-r.
 \tag{2.1}
\]

### Theorem 2.1 (gap-nine generating-function upper bound)

For every \(r\),

\[
 R_9(r)\le[x^r]U_9(x),
 \tag{2.2}
\]

where

\[
\begin{aligned}
 U_9(x)
 &={x^3\over(1-2x)^2}
   +{x(1-x)^2\over(1-2x)^2-x^3}
   -{x(1-x)^2\over(1-2x)^2}.
 \tag{2.3}
\end{aligned}
\]

Consequently

\[
 \boxed{
 R_9(r)
 =O\!\left(\left({3+\sqrt5\over2}\right)^r\right).
 }
 \tag{2.4}
\]

#### Proof

Let \(D\) have a gap-nine return, put \(F=\partial D\), and let \(t\) be
its terminal variable.  By Theorem 1.1,

\[
 B_{2t+2}(F)=9.
\]

If \(t\ge1\), then \(B_4\le9\).  But the three consecutive same-label gaps
from \(B_1\) through \(B_4\) are each at least three, including in rank
one, and \(B_1\ge1\).  Hence

\[
 B_4\ge B_1+3\cdot3\ge10,
\]

a contradiction.  Thus \(t=0\) and \(B_2(F)=9\).

The root particle of \(F\) recurs before time nine.  A gap-three recurrence
forces \(F=10\), but then \(B_2=5\) by (1.7).  Therefore \(F\) is a
gap-five or gap-seven root.  Counting every terminal-zero inverse lift of
both classes is a coefficientwise upper bound; the additional equation
\(B_2=9\) may discard some of them.

Use \(u\) for semilength and \(v\) for peak count.  The exact gap-five
class

\[
 (10)^a1(10)^b0,
 \qquad a\ge0,\quad b\ge1,
\]

has enumerator

\[
 A_5(u,v)={u^2v\over(1-uv)^2}.
 \tag{2.5}
\]

The exact gap-seven class has enumerator

\[
 A_7(u,v)
 ={u\over(1-uv)^2-u^2v}-{u\over(1-uv)^2}.
 \tag{2.6}
\]

A terminal-zero lift substitutes

\[
 (u,v)\longmapsto
 \left({x\over(1-x)^2},x\right).
 \tag{2.7}
\]

Substitution into \(A_5+A_7\) gives (2.3).  Finally

\[
 (1-2x)^2-x^3=(1-x)(1-3x+x^2),
\]

whose least positive zero is

\[
 {3-\sqrt5\over2}.
\]

This proves (2.4). \(\square\)

### Corollary 2.2 (edge-disjoint packing through gap nine)

Let \(\nu_{\le9}(P_r)\) be the largest physical edge-disjoint packing
using only gaps \(5,7,9\).  Then

\[
 \nu_{\le9}(P_r)
 \le N\bigl(R_5(r)+R_7(r)+R_9(r)\bigr)
 =o(B).
 \tag{2.8}
\]

This grants every physical phase and therefore already includes all packing
conflicts.

Gap nine is not empty.  The word

\[
 (10)^M11110000
\]

has first return nine for every \(M\ge1\), as the next theorem shows with
\(L=1,d=3\).

## 3. The exact terminal-mountain suspension

Write

\[
 M_j=1^j0^j.
\]

### Theorem 3.1 (all-gap terminal-mountain family)

Let

\[
 M\ge1,\qquad
 1\le L\le d,\qquad
 X\in\mathcal D_M,\qquad
 \operatorname{ht}(X)\le L.
\]

Set

\[
 D=XM_{d+L},
 \qquad
 r=M+d+L.
\]

Then the first outer return is

\[
 \boxed{g=2(d+L)+1.}
 \tag{3.1}
\]

#### Proof

Peak deletion commutes with concatenation of complete Dyck words and
\(\partial M_j=M_{j-1}\).  Therefore

\[
 \partial^jD=(\partial^jX)M_{d+L-j}
 \quad(0\le j\le L),
 \qquad
 \partial^LD=M_d.
 \tag{3.2}
\]

The rank-\(d\) root \(M_d\) is fixed by \(\phi\) and has voltage \(d\)
modulo

\[
 p=2d+1.
\]

Since

\[
 d^{-1}\equiv-2\pmod p,
 \qquad
 2jd\equiv-j\pmod p,
\]

the terminal-chain particle \(-j\) is selected first at time \(2j\) and
next at time \(p+2j\), for \(1\le j\le L\).  The hypothesis \(L\le d\)
prevents wrap before these first selections.

The final pure descent supplies \(L\) nested adjacent predecessor pairs.
The first cascade at times \(2,4,\ldots,2L\) moves each particle into its
successor's old position.  The second cascade at
\(p+2,p+4,\ldots,p+2L\) first enters the original outer target on its last
move.  No overtaking permits an earlier entry.  Thus the first return is

\[
 p+2L=2(d+L)+1.
\]

Since \(M\ge1\), this is less than \(N=2r+1\). \(\square\)

For \(L=d=3\) and \(X=(111000)^t\), the gap is thirteen while

\[
 |\partial^2D|_{\rm semi}=t+4.
\]

Hence no upper bound on twice-pruned rank can be a function of the return
gap alone.

### Theorem 3.2 (uniform tower spectrum)

For fixed \(d,L\), the number of semilength-\(r\) roots in Theorem 3.1 is

\[
 T_{r;d,L}=C_{r-d-L,\le L},
 \tag{3.3}
\]

where \(C_{m,\le L}\) counts Dyck paths of height at most \(L\).  Its
generating function is

\[
 x^{d+L}C_L(x),
\]

and its exponential growth constant is

\[
 \boxed{4\cos^2{\pi\over L+2}.}
 \tag{3.4}
\]

More precisely,

\[
 C_{m,\le L}
 \le
 4^m\exp\!\left(-{\pi^2m\over(L+2)^2}\right).
 \tag{3.5}
\]

#### Proof

Only \(X\) varies.  Height-\(L\) Dyck paths are closed walks from zero in
the path graph on \(0,1,\ldots,L\), whose adjacency spectral radius is
\(2\cos(\pi/(L+2))\).  Also
\(\log\cos u\le-u^2/2\). \(\square\)

### Corollary 3.3 (the entire Gaussian tower library is packing-negligible)

Fix \(A>0\), let \(H\le A\sqrt r\), and sum over

\[
 1\le L\le d,
 \qquad
 d+L\le H-1.
\]

Then, for all sufficiently large \(r=r(A)\),

\[
 \boxed{
 N\sum_{d,L}T_{r;d,L}
 \le
 O_A(r^4)e^{-(\pi^2/8)r^{1/3}}B
 =o(B).
 }
 \tag{3.6}
\]

Thus the maximum physical edge-disjoint packing of all these returns is
also \(o(B)\).

#### Proof

Put \(s=d+L\) and \(m=r-s\).  For large \(r\),

\[
 m\ge r/2,
 \qquad
 s\ge2L.
\]

By (3.5),

\[
 T_{r;d,L}
 \le
 4^{r-s}
 \exp\!\left(-{\pi^2m\over(L+2)^2}\right).
\]

If \(L\ge r^{1/3}\), the factor \(4^{-s}\) is at most
\(\exp(-2(\log4)r^{1/3})\).  If \(L<r^{1/3}\), then
\(L+2\le2r^{1/3}\) and the spectral factor is at most
\(\exp(-(\pi^2/8)r^{1/3})\).  There are at most \(H^2\le A^2r\)
parameter pairs.  Finally,

\[
 B\ge {4^r\over(r+1)(2r+1)}.
\]

Summation and multiplication by all \(N\) phases prove (3.6).
\(\square\)

For a fixed tower class, packing is also explicit.  Its trace length is
\(k=d+L+2\).  After removing quotient cycles of length at most \(H+1\),
greedy interval selection retains at least a \(1/(2k-1)\) fraction of the
starts, and every selected quotient interval has all \(N\) disjoint deck
lifts.  This lower packing calculation does not affect the upper bound
(3.6).

## 4. The sharp failure of the first-sector converse

For

\[
 D=P1R0S
\]

at the first up-step attaining the global maximum, with the displayed zero
the first later return to zero, put

\[
 d_{\rm step}(D)=|S|+1.
\]

A zero-winding return forces

\[
 d_{\rm step}(D)=1,
 \qquad
 g=2\operatorname{ht}(D)+1.
\]

The converse was proposed and is false.

### Theorem 4.1 (all-\(\beta\) height-three counterfamily)

For integers

\[
 M\ge\beta\ge2,
\]

put

\[
 F_\beta=1(10)^\beta0,
\qquad
 D_{M,\beta}=(10)^M\,1(1100)^\beta0.
 \tag{4.1}
\]

Then

\[
 \partial D_{M,\beta}=F_\beta,
 \qquad
 |D_{M,\beta}|_{\rm semi}=M+2\beta+1,
 \qquad
 \operatorname{ht}(D_{M,\beta})=3,
 \qquad
 d_{\rm step}(D_{M,\beta})=1.
 \tag{4.2}
\]

Nevertheless the first return of \(D_{M,\beta}\) is

\[
 \boxed{g_\beta=6\beta+1.}
 \tag{4.3}
\]

For the minimal choice \(M=\beta\), this is \(N-2\).

#### Proof

The word \(F_\beta\) is the defect-one gap-five root

\[
 E(0,\beta,0).
\]

Its three periodic voltages are

\[
 2,\qquad2\beta,\qquad2
\]

modulo

\[
 p=2\beta+3.
\]

The distinguished particle returns at time five.  Direct partial summation
shows that its predecessor occurs first at

\[
 B_1=2
\]

and next at

\[
 B_2=6\beta+1.
\]

 The lift \(D_{M,\beta}\) has terminal value zero.  Theorem 1.1 therefore gives
its first outer return at \(B_2=6\beta+1\).  Since its outer circumference
is

\[
 2(M+2\beta+1)+1,
\]

the return is in the no-wrap range when \(M\ge\beta\).

The identities in (4.2) follow directly by peak deletion and height
inspection.  The first component reaching height three is the final
primitive component, so \(S=\varnothing\) and \(d_{\rm step}=1\).
\(\square\)

Two small primitive counterexamples isolate the error in a proposed sector
proof.

\[
 D=1110011000
\]

has rank five, height three, and \(d_{\rm step}=1\), but its \(\phi\)-orbit
has voltages

\[
 (3,7,3)\pmod{11},
\]

and its first return is thirteen, not seven.

Even uniqueness of the deepest leaf is insufficient:

\[
 D=111100011000
\]

has rank six, a unique height-four maximum, and \(d_{\rm step}=1\), but
its \(\phi\)-orbit voltages

\[
 (4,8,4,4,8)\pmod{13}
\]

do not return at time nine.

The precise error is that off-spine sectors are transported and later
reinserted deeper along the candidate spine.  Being below height \(h\) when
first moved to the root does not keep them below height \(h\) after later
shifts.

### Theorem 4.2 (the full delayed-predecessor Pascal fibre)

Fix \(\beta\ge2\) and an outer rank \(r\ge3\beta+1\).  Every terminal-zero
inverse lift of

\[
 F_\beta=1(10)^\beta0
\]

has first return

\[
 g=6\beta+1.
 \tag{4.4}
\]

The exact number of these normalized roots is

\[
 \boxed{
 K_{r,\beta}=\binom r{2\beta+1}.
 }
 \tag{4.5}
\]

The full terminal-zero lift enumerator (before imposing the no-wrap lower
bound on \(r\)) is

\[
 \sum_{r\ge0}K_{r,\beta}x^r
 ={x^{2\beta+1}\over(1-x)^{2\beta+2}}.
 \tag{4.5a}
\]

Consequently, for every fixed \(A>0\), the union of all these fibres with

\[
 6\beta+1\le2A\sqrt r-1
\]

has, even after granting all \(N\) physical phases,

\[
 \exp(O_A(\sqrt r\log r))=o(B)
 \tag{4.6}
\]

possible starts.  Its edge-disjoint packing is therefore \(o(B)\).

#### Proof

The predecessor time \(B_2(F_\beta)=6\beta+1\) was proved in Theorem 4.1.
Theorem 1.1 applies because

\[
 6\beta+1<2r+1
\]

under the stated rank hypothesis.

The core has semilength \(d=\beta+1\) and peak count \(k=\beta\).
Substituting \(t=0\) into (1.1) gives

\[
 K_{r,\beta}
 =\binom{r+(\beta+1)-\beta-1}{2(\beta+1)-1}
 =\binom r{2\beta+1}.
\]

For \(\beta\le A\sqrt r/3\), use

\[
 \binom r{2\beta+1}
 \le
 \left({er\over2\beta+1}\right)^{2\beta+1}.
\]

There are \(O_A(\sqrt r)\) values of \(\beta\), so the logarithm of the
sum, even after multiplication by \(N\), is
\(O_A(\sqrt r\log r)=o(r)\).  Since
\(B=\exp((\log4+o(1))r)\), (4.6) follows. \(\square\)

## 5. A literal stable-spine sector and its uniform spectral bound

The failed converse has a rigorous surviving subclass.

Let the first-deepest spine of a height-\(h\) plane tree have ordered
forests \(A_i\) before and \(B_i\) after its spine child at depth
\(0\le i<h\).  Thus

\[
 D=A_0 1A_1 1\cdots1A_{h-1}1
   0B_{h-1}0\cdots0B_1 0B_0.
 \tag{5.1}
\]

### Theorem 5.1 (stable-spine sufficient criterion)

Assume

\[
 A_i=\varnothing\quad(0\le i<h),
 \qquad
 \operatorname{ht}(B_i)\le\min(i,h-i).
 \tag{5.2}
\]

Then the displayed spine remains the first deepest spine through the first
\(h\) applications of \(\tau=\phi^2\), and \(D\) has a zero-winding first
return

\[
 \boxed{g=2h+1.}
 \tag{5.3}
\]

#### Proof

One block rotation sends the sector arrays to

\[
 A_0'=B_0,
 \qquad
 A_i'=A_{i-1}\ (1\le i<h),
\]

and

\[
 B_i'=B_{i+1}\ (0\le i<h-1),
 \qquad
 B_{h-1}'=\varnothing.
\]

An original \(B_j\) first moves toward the root and later enters an
\(A\)-sector, moving one level deeper at each subsequent shift.  Its
original global-height restriction gives
\(\operatorname{ht}(B_j)\le h-j\), while (5.2) gives
\(\operatorname{ht}(B_j)\le j\).  At every intermediate location their
minimum keeps its absolute height below \(h\).  All original \(A_i\) are
empty, so no pre-spine sector can overtake after being shifted deeper.
Thus the marked spine and its height stay fixed for \(h\) shifts.

For \(0\le j<h\), the transported arrays are

\[
 B_i^{(j)}=
 \begin{cases}
 B_{i+j},&i+j<h,\\
 \varnothing,&i+j\ge h,
 \end{cases}
\]

and

\[
 A_i^{(j)}=
 \begin{cases}
 B_{j-1-i},&0\le i<j,\\
 \varnothing,&j\le i<h.
 \end{cases}
\]

Consequently, with

\[
 C_j=\sum_{t=0}^{j-1}d_{\rm step}(D_t),
\]

one has

\[
 C_j=j+2\sum_{t=0}^{j-1}|B_t|,
\qquad
 \delta(D_j)=h+2\sum_{t=0}^{j-1}|B_t|,
\]

and hence

\[
 \delta(D_j)-C_j=h-j>0
 \qquad(j<h).
\]

At \(j=h\), the \(A\)-sectors are
\(B_{h-1},B_{h-2},\ldots,B_0\), so

\[
 \delta(D_h)=h+2\sum_{t=0}^{h-1}|B_t|=C_h.
\]

Both sides are below \(N\).  The even-time roots are
\(u-C_j\), and the next odd step adds \(\delta(D_j)\); therefore the
displayed equality at \(j=h\) is the first modular return.  This proves
(5.3). \(\square\)

Let \(C_j(x)\) count Dyck forests of height at most \(j\), with
\(C_0(x)=1\), and let \(Q_j(x)\) be defined by

\[
 Q_0=Q_1=1,
 \qquad
 Q_{j+1}=Q_j-xQ_{j-1},
 \qquad
 C_j={Q_j\over Q_{j+1}}.
\]

### Theorem 5.2 (exact stable-spine generating function)

The semilength generating function for the height-\(h\) class in
Theorem 5.1 is

\[
 S_h(x)
 =x^h\prod_{i=0}^{h-1}C_{\min(i,h-i)}(x).
 \tag{5.4}
\]

Writing \(h=2s\) or \(2s+1\),

\[
 \boxed{
 S_{2s}(x)={x^{2s}\over Q_s(x)Q_{s+1}(x)},
 \qquad
 S_{2s+1}(x)={x^{2s+1}\over Q_{s+1}(x)^2}.
 }
 \tag{5.5}
\]

At the Catalan singularity,

\[
 S_h(1/4)\le2^{1-h}.
 \tag{5.6}
\]

#### Proof

Under (5.2), only the independent forests \(B_i\) vary, proving (5.4).
The sequence of bounds \(\min(i,h-i)\) is symmetric.  Telescoping the
products \(C_j=Q_j/Q_{j+1}\) gives (5.5).

The standard closed form gives

\[
 Q_j(1/4)={j+1\over2^j}.
\]

Substitution in (5.5) yields

\[
 S_{2s}(1/4)
 ={2^{1-2s}\over(s+1)(s+2)},
\]

and

\[
 S_{2s+1}(1/4)
 ={2^{-2s}\over(s+2)^2}.
\]

Both imply (5.6). \(\square\)

### Corollary 5.3 (uniform Gaussian stable-spine sparsity)

Fix \(A>0\).  The total number of physical starts supplied by
Theorem 5.1 with

\[
 h+1\le A\sqrt r
\]

is \(o(B)\).  More precisely it is at most

\[
 O_A(r^4)e^{-c r^{1/3}}B
 \tag{5.7}
\]

for an absolute \(c>0\).

#### Proof

For a fixed \(h\), nonnegativity and (5.6) give

\[
 [x^r]S_h(x)\le4^rS_h(1/4)\le2^{1-h}4^r.
 \tag{5.8}
\]

Independently, every member has height \(h\), so the path-graph bound gives

\[
 [x^r]S_h(x)
 \le4^r\exp\!\left(-{\pi^2r\over(h+2)^2}\right).
 \tag{5.9}
\]

If \(h\ge r^{1/3}\), use (5.8).  If \(h<r^{1/3}\), use (5.9) and
\(h+2\le2r^{1/3}\).  Thus every summand is at most

\[
 2\cdot4^r e^{-c r^{1/3}},
 \qquad
 c=\min\{\log2,\pi^2/4\}.
\]

There are \(O_A(\sqrt r)\) heights.  Multiply by all \(N\) physical phases
and use

\[
 B\ge {4^r\over(r+1)(2r+1)}.
\]

This proves (5.7). \(\square\)

Thus the literal sector condition strong enough to make the naive
first-spine proof valid is stretched-exponentially too sparse.  Allowing
spine changes is unavoidable in any aggregate Gaussian theorem.

## 6. The inherited-terminal generating function is a sharp relaxation

For completeness, this section records the exact full-dependence
generating function which fails to retain dynamic re-rooting.

Let

\[
 D^{(0)}=D,
 \qquad
 D^{(i+1)}=\partial D^{(i)},
\]

and let \(t_i\) be the terminal inverse variable in the inherited lift from
\(D^{(i+1)}\) to \(D^{(i)}\).  Define

\[
 J_{\rm inh}(D)=|\{i:t_i>0\}|,
 \qquad
 K_{\rm inh}(D)=\prod_i(2t_i+1).
\]

Let

\[
 C(a,b)=\sum_Da^{|D|_{\rm semi}}b^{\operatorname{pk}(D)}.
\]

### Theorem 6.1 (exact inherited products)

With \(q=ab\),

\[
 C(a,b)
 ={1\over1-q}
 C\!\left({a\over(1-q)^2},q\right).
 \tag{6.1}
\]

Start with \((a_0,b_0)=(x,1)\), and put

\[
 a_{i+1}={a_i\over(1-a_ib_i)^2},
 \qquad
 b_{i+1}=a_ib_i,
 \qquad
 q_i=a_ib_i.
\]

If

\[
 x={1\over4\cosh^2\theta},
\]

then

\[
 q_i(x)
 =\left({\sinh\theta\over\sinh((i+2)\theta)}\right)^2.
 \tag{6.2}
\]

Furthermore

\[
 \sum_Dx^{|D|_{\rm semi}}y^{J_{\rm inh}(D)}
 =C(x)\prod_{i\ge0}\bigl(1-(1-y)q_i(x)\bigr),
 \tag{6.3}
\]

and, for fixed \(0\le y\le1\),

\[
 { [x^r]\sum_Dx^{|D|_{\rm semi}}y^{J_{\rm inh}(D)}
  \over\operatorname{Cat}_r}
 \longrightarrow
 {\sin(\pi\sqrt{1-y})\over\pi\sqrt{1-y}}.
 \tag{6.4}
\]

In particular,

\[
 \mathbb E J_{\rm inh}\longrightarrow{\pi^2\over6},
 \qquad
 \Pr(J_{\rm inh}=1)\longrightarrow{1\over2}.
 \tag{6.5}
\]

For fixed \(\lambda\ge0\), put

\[
 R_\lambda(q)
 =(1-q)\sum_{t\ge0}(2t+1)^\lambda q^t.
\]

Then

\[
 \sum_Dx^{|D|_{\rm semi}}K_{\rm inh}(D)^\lambda
 =C(x)\prod_{i\ge0}R_\lambda(q_i(x)),
 \tag{6.6}
\]

and

\[
 {\sum_{D\in\mathcal D_r}K_{\rm inh}(D)^\lambda
  \over\operatorname{Cat}_r}
 \longrightarrow
 3^\lambda\prod_{n=2}^{\infty}R_\lambda(n^{-2})<\infty.
 \tag{6.7}
\]

For \(\lambda=1\),

\[
 \mathbb E K_{\rm inh}
 \longrightarrow{3\sinh\pi\over\pi}.
 \tag{6.8}
\]

#### Proof

For a core of rank \(d\) with \(k\) peaks, inverse insertion contributes

\[
 a^d{q^k\over(1-q)^{2d+1}},
\]

which proves (6.1).  Iteration gives (6.2).  Marking whether the terminal
variable is positive replaces its factor \((1-q_i)^{-1}\) by

\[
 {1-(1-y)q_i\over1-q_i},
\]

proving (6.3).  Weighting terminal value \(t\) by
\((2t+1)^\lambda\) proves (6.6).

The coefficient transfer uses the following uniform product lemma.  If
\(R(q)=1+cq+O(q^2)\) near \([0,1/4]\), then

\[
 { [x^r]C(x)\prod_{i\ge0}R(q_i(x))
  \over\operatorname{Cat}_r}
 \longrightarrow
 (1+c)\prod_{n=2}^{\infty}R(n^{-2}).
 \tag{6.9}
\]

To prove it, take \(\theta\) in a fixed dented sector at zero.  Uniformly
there,

\[
 \sum_{n\ge2}
 \left[
 \left({\sinh\theta\over\sinh(n\theta)}\right)^2
 -{1\over n^2}
 \right]
 =-\theta+O(\theta^2).
 \tag{6.10}
\]

Euler summation applies to
\(\operatorname{csch}^2z-z^{-2}\), whose integral is

\[
 \int_0^\infty(\operatorname{csch}^2u-u^{-2})\,du=-1.
\]

Thus the product equals

\[
 P_R(1-c\theta+O(\theta^2)),
 \qquad
 P_R=\prod_{n\ge2}R(n^{-2}).
\]

Since

\[
 C(x)=1+e^{-2\theta}=2-2\theta+O(\theta^2),
\]

square-root singularity transfer proves (6.9).

Apply (6.9) to \(R(q)=1-(1-y)q\) and use Euler's sine product to obtain
(6.4).  Apply it to \(R_\lambda\), for which

\[
 R_\lambda(q)=1+(3^\lambda-1)q+O(q^2),
\]

to obtain (6.7).  Finally

\[
 R_1(q)={1+q\over1-q}
\]

and Euler's hyperbolic-sine product give (6.8). \(\square\)

These theorems imply that inherited terminal multiplicities, with their
full dependence across levels, impose no Catalan spectral loss.

They do not give a necessary condition for a genuine PBBS return.  After a
shortest predecessor interval is chosen, the next root is

\[
 \phi^j(\partial D)
\]

for a time-dependent \(j\), not the inherited root \(\partial D\).
Consequently \(K_{\rm inh}\) and the dynamic branching product use
different terminal variables and are not comparable.

## 7. Correct dynamic product bounds

Suppose a real return at level \(i\) has gap \(g_i\) and terminal variable
\(t_i\).  Then

\[
 g_i=B_{2t_i+2}.
\]

The \(2t_i+1\) intervals between

\[
 B_1,B_2,\ldots,B_{2t_i+2}
\]

are consecutive predecessor returns.  Choosing a shortest one gives

\[
 g_{i+1}
 <{g_i\over2t_i+1}.
 \tag{7.1}
\]

Iterating to the terminal rank-one gap-three return gives

\[
 \boxed{
 K_{\rm dyn}<g_0/3.
 }
 \tag{7.2}
\]

If the last parent multiplier leading into that rank-one child is omitted,
the preceding parent gap is at least five, and

\[
 \boxed{
 K_{\rm dyn}^{\rm pre}\le g_0/5.
 }
 \tag{7.3}
\]

The stronger full-product claim \(K_{\rm dyn}\le g_0/5\) is false.  For
\(F=10\), (1.7) gives \(B_4=11\).  The terminal-one lift

\[
 (10)^M110010,
 \qquad M\ge3,
\]

has first outer return eleven, but its multiplier is

\[
 2t+1=3>{11\over5}.
\]

## 8. Edge-disjoint packing and the exact remaining inequality

Let \(\tau=\phi^2\) act on the \(B\) Dyck quotient edges.  For a quotient
cycle \(C\), let \(\mathcal I_H(C)\) be its actual return intervals of
trace length at most \(H+1\).  Put

\[
 \overline\nu_H
 =\sum_C\alpha(\mathcal I_H(C)),
 \tag{8.1}
\]

where \(\alpha\) is edge-interval packing on \(C\).

Let \(Z_H\) be the number of quotient edges on quotient cycles of length at
most \(H+1\).  The voltage-itinerary rigidity theorem gives

\[
 Z_H\le(2H+2)N^{2H+2}.
 \tag{8.2}
\]

For \(H\log N=o(r)\),

\[
 NZ_H=o(B).
\]

The exact deck reduction is

\[
 N\overline\nu_H
 \le\nu_H(P_r)
 \le2N\overline\nu_H+NZ_H.
 \tag{8.3}
\]

There is also an exact root-count lower bound.  After discarding starts on
the short quotient cycles, every remaining trace is a nonwrapping interval
of at most \(H+1\) edges.  One selected interval conflicts with starts at
at most \(2H\) other quotient edges.  Greedy selection and all \(N\) deck
lifts therefore give

\[
 \boxed{
 \nu_H(P_r)
 \ge {N\over2H+1}\bigl(R_r(H)-Z_H\bigr).
 }
 \tag{8.3a}
\]

In particular, at \(H=\lceil A\sqrt r\rceil\), \(RP_A\) requires

\[
 R_r(H)=o_A(B/\sqrt r).
 \tag{8.3b}
\]

The universal height-gap theorem supplies the uniform spectral estimate

\[
 R_r(H)
 \le
 \left(2\cos{\pi\over H+1}\right)^{2r}
 \le
 4^r\exp\!\left(-{\pi^2r\over(H+1)^2}\right).
 \tag{8.3c}
\]

At \(H=A\sqrt r+O(1)\), however, (8.3c) is only of Catalan order after
the exact path-graph prefactor is restored; it does not approach the
necessary \(o_A(B/\sqrt r)\) scale in (8.3b).  Sections 3 and 5 prove the
needed stronger loss only for two explicit structural sectors.

Therefore \(RP_A\) is equivalent to

\[
 \boxed{
 \overline\nu_{\lceil A\sqrt r\rceil}
 =o_A(B/N).
 }
 \tag{8.4}
\]

The exact root formula (1.5) and the packing functional (8.1) identify the
remaining theorem.  One must control

\[
 \mathbf1\{B_{2t+2}(F)\le2H-1\}
\]

under the inverse-Pascal weight (1.1), while retaining the dynamically
re-rooted PBBS state and the overlap pattern of the resulting intervals on
each \(\tau\)-cycle.

The results above prove that the following routes cannot close (8.4).

* A pointwise bound on first or second pruning rank is false by
  Theorem 3.1.
* The first-sector condition \(d_{\rm step}=1\) does not control the gap,
  by Theorem 4.1.
* The literal fixed-spine subclass is stretched-exponentially sparse, by
  Corollary 5.3.
* Inherited terminal multiplicities retain full Catalan spectral radius,
  by Theorem 6.1.
* Independent branching signs are invalid because every child is
  dynamically re-rooted.

What remains unproved is a genuinely dynamic occurrence-order
generating-function or spectral-radius inequality for (1.5), or an
equivalent quotient-cycle clustering theorem strong enough to yield
(8.4).

No claim of \(RP_A\), coefficient one, MWB, labelled synchronization, or a
literal contiguous-OR construction is made here.  All proved packing
statements concern exact integral intervals in the canonical PBBS factor.
