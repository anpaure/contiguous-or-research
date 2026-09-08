# Fifth-wave U: an equal-packet surface braid and the remaining pin gate

Date: 2026-07-25

## 0. Verdict

For the equal four-box complementary-shell packet, write

\[
\mathcal A_r=S_r\times H_r,
\qquad
\mathcal B_r=H_r\times I_r,
\]

where

\[
S_r=[0,r]^2,\qquad
H_r=\{(0,j):0\le j\le r\}
\cup\{(i,r):1\le i\le r\},
\]

\[
I_r=\{1,\ldots,r\}\times\{0,\ldots,r-1\}.
\]

Their abstract shapes and aligned widths are

\[
\mathcal A_r\cong(r,r,2r),\qquad
\mathcal B_r\cong(r-1,r-1,2r),
\]

\[
W_r=w(\mathcal A_r)+w(\mathcal B_r)
=(r+1)^2+r^2=2r^2+2r+1.
\tag{0.1}
\]

This is the equal complementary packet \(A_r,B_r\), not the shifted
pairing \(B_r,A_{r-1}\) arising from a different drain tie-breaking.
Uniform APF over all compact parents is already false; the equal PACK
problem studied here is the surviving special case.

This attack gives a positive answer to the incidence part of the
fifth-wave question.

1. There is an explicit reset-free common-lift word
   \(\mathcal E_r\) of length

   \[
   \boxed{
   |\mathcal E_r|
   =2r^2+r-1+\left\lceil\frac r2\right\rceil
   =W_r-\left\lfloor\frac r2\right\rfloor-2.}
   \tag{0.2}
   \]

   It covers two complete adjacent interface faces, displays
   \(4r^2+2r-1\) distinct packet targets, and its displayed witness system
   supplies exactly

   \[
   \boxed{2r^2+r-1}
   \tag{0.3}
   \]

   cross-child shared endpoint positions.  All of these positions are
   doubly active under the exact child projections.

2. The sloped-band seam matching from third-wave U occurs literally
   inside \(\mathcal E_r\).  With
   \(k=\lfloor(r-1)/8\rfloor\), it exposes

   \[
   M_r(k)=r(2k+1)-k(k+1)
   =\frac{15}{64}r^2+O(r)
   \tag{0.4}
   \]

   band-compatible shared endpoint sites.  The two-child endpoint toll is

   \[
   \Gamma_r
   =\frac{289}{1728}r^2+O(r),
   \tag{0.5}
   \]

   and

   \[
   M_r(k)-\Gamma_r
   =\frac{29}{432}r^2+O(r)>0.
   \tag{0.6}
   \]

   Thus the required endpoint incidence can be exposed simultaneously in
   one literal chronology; the matching itself has no left/right
   incompatibility.

3. Translate \(\mathcal E_r\) into every equal-drain packet and concatenate.
   The resulting partial parent word has exact length

   \[
   \boxed{
   M_R-1-2R-\left\lfloor\frac{R^2}{4}\right\rfloor,}
   \tag{0.7}
   \]

where \(M_R=w_4(R,R,R,R)\).  It supplies

   \[
   \left(\frac5{64}+o(1)\right)R^3
   \tag{0.8}
   \]

   band-compatible cross-child endpoint sites, exceeding the certified
   demand

   \[
   \left(\frac{289}{5184}+o(1)\right)R^3.
   \tag{0.9}
   \]

   It also supplies

   \[
   \frac{R(4R^2+9R-1)}6
   =\left(\frac23+o(1)\right)R^3
   \tag{0.10}
   \]

   doubly active letter positions.  This exceeds the cubic coefficient
   certified by the U3 activity ledger; it is not a claim about the unknown
   exact local defects.  Hence the certified cubic child-service incidence
   is geometrically and chronologically realizable with only
   parent-width-scale letters.

4. This does **not** prove the complementary-shell packet lemma (PACK).
   Every interval maximum of \(\mathcal E_r\) remains on its two interface
   faces.  Retaining this module unchanged already forces \(2r-1\) new
   literal axis letters, so exact length \(W_r\) is impossible for
   \(r\ge3\).  The deficit is only \(O(r)\), and therefore does not rule out
   \(W_r+o(r^2)\).

5. The remaining obstruction can be stated exactly.  If an arbitrary
   packet word has length \(W_r+e\), let \(a\) count, with left/right type,
   the cross-child band endpoint sites which are also endpoints of the
   aligned packet-middle witnesses.  Then

   \[
   \boxed{4e+a\ge\Gamma_r.}
   \tag{0.11}
   \]

   Consequently an \(o(r^2)\)-excess PACK word must absorb

   \[
   \left(\frac{289}{1728}-o(1)\right)r^2
   \]

   cross-child endpoint sites directly into the two middle endpoint
   queues.  If all shared sites carry letters dominated by no packet-middle
   target—for example, if they all lie above the aligned middle rank—then

   \[
   e\ge
   \left(\frac{289}{6912}-o(1)\right)r^2.
   \tag{0.12}
   \]

The exact surviving gate is therefore not incidence capacity, endpoint
orientation, or reset removal.  It is **pin-compatible middle-queue
absorption while covering the rest of the packet**.  No full
\(W_r+o(r^2)\) packet word and no unrestricted quadratic lower bound is
proved here.

All constructions and obstructions below are literal and integral.  No web
search, finite search, or computational experiment is used.

## 1. Packet geometry

Fix an integer \(r\ge1\).  The endpoint-toll statements in Sections 3
and 7 will additionally assume \(r\ge2\).

Enumerate the outer hook as a chain

\[
h_0<h_1<\cdots<h_{2r},
\tag{1.1}
\]

where

\[
h_t=
\begin{cases}
(0,t),&0\le t\le r,\\
(t-r,r),&r\le t\le2r.
\end{cases}
\tag{1.2}
\]

The two packet middle layers both have ambient local rank \(2r\).  Their
union is an antichain of size \(W_r\).  In particular, every word covering
the packet has length at least \(W_r\).

The interface used below is

\[
F_A=
\{(h_t;0,v):0\le t\le2r,\ 0\le v<r\}\setminus\{0\}
\subset\mathcal A_r,
\tag{1.3}
\]

\[
F_B=
\{(h_t;1,v):0\le t\le2r,\ 0\le v<r\}
\subset\mathcal B_r.
\tag{1.4}
\]

Here a semicolon separates the first and second square factors.  Define

\[
a_{t,v}=(h_t;0,v),\qquad
b_{t,v}=(h_t;1,v),
\tag{1.5}
\]

\[
e=b_{0,0}=(0,0;1,0),
\tag{1.6}
\]

and

\[
J_r=
\{0,\ldots,2r\}\times\{0,\ldots,r-1\}
\setminus\{(0,0)\}.
\tag{1.7}
\]

Thus

\[
N_r:=|J_r|=(2r+1)r-1=2r^2+r-1.
\tag{1.8}
\]

The elementary identity behind the braid is

\[
\boxed{a_{t,v}\vee e=b_{t,v}.}
\tag{1.9}
\]

## 2. The common-lift surface braid

For \(0\le v<r\), define

\[
\mathcal C_v^\downarrow=
\begin{cases}
a_{2r,0},a_{2r-1,0},\ldots,a_{1,0},&v=0,\\
a_{2r,v},a_{2r-1,v},\ldots,a_{0,v},&v>0,
\end{cases}
\tag{2.1}
\]

and let \(\mathcal C_v^\uparrow\) be its reversal.

Pair the \(v\)-indices as \(0,1\), then \(2,3\), and so on.  For every
complete pair output

\[
\mathcal C_{2j}^\downarrow,\ e,\ \mathcal C_{2j+1}^\uparrow.
\tag{2.2}
\]

If \(r\) is odd, finish with

\[
\mathcal C_{r-1}^\downarrow,e.
\tag{2.3}
\]

Call the concatenation \(\mathcal E_r\).

### Theorem 2.1 (common-lift interface braid — PROVED)

The word \(\mathcal E_r\) covers every target in \(F_A\cup F_B\), has
length

\[
\boxed{
|\mathcal E_r|
=N_r+\left\lceil\frac r2\right\rceil,}
\tag{2.4}
\]

and its displayed witness system supplies exactly \(N_r\) cross-child
shared endpoint positions.

#### Proof

Every \(a_{t,v}\) is a displayed singleton.  Suppose first that its chain
lies to the left of the central \(e\).  The interval from \(a_{t,v}\) to
that \(e\) contains, besides \(e\), only

\[
a_{t,v},a_{t-1,v},\ldots
\]

from its decreasing chain.  All these letters are at most \(a_{t,v}\), so
by (1.9)

\[
\bigvee[a_{t,v},\ldots,e]=b_{t,v}.
\tag{2.5}
\]

If the chain lies to the right, use the interval from \(e\) through
\(a_{t,v}\); the intervening chain letters again lie below \(a_{t,v}\).
Any displayed occurrence of \(e\) covers \(b_{0,0}\).

There is one occurrence of every \(a_{t,v}\), \((t,v)\in J_r\), and one
copy of \(e\) per pair of \(v\)-chains.  This proves (2.4).

For a left chain, the singleton witness for \(a_{t,v}\) and the witness
(2.5) for \(b_{t,v}\) have the same physical left endpoint.  For a right
chain, they have the same physical right endpoint.  The \(N_r\) literal
\(a\)-positions are distinct, so this gives exactly \(N_r\) displayed
cross-child shared endpoint sites.

Finally, every letter has first factor in the chain \(H_r\), and its second
factor is either \((0,v)\) or \((1,0)\).  Hence every interval maximum has
second factor \((0,v)\) or \((1,v)\) and remains in \(F_A\cup F_B\).  The
two displayed families are therefore exactly the nonzero maxima covered by
the word. \(\square\)

Since

\[
W_r-|\mathcal E_r|
=\left\lfloor\frac r2\right\rfloor+2,
\tag{2.6}
\]

the complete interface braid fits strictly below the packet-width budget.
It is reset-free: the common \(e\) is an ordinary packet letter, not an
additive separator.

### 2.2 Exact activity

Let \(h_t=(\alpha_t,\beta_t)\).  In the abstract \(\mathcal A_r\)
coordinates,

\[
\pi_A(a_{t,v})=(\alpha_t,\beta_t,v).
\tag{2.7}
\]

In the abstract \(\mathcal B_r\) coordinates, the translated first
increment of \(I_r\) is ignored, and

\[
\pi_B(a_{t,v})=\pi_B(b_{t,v})=(0,v,t).
\tag{2.8}
\]

For \((t,v)\in J_r\), both projections are nonzero.  Thus all \(N_r\)
\(a\)-positions are doubly active.  The lift \(e\) has zero
\(\mathcal B_r\)-projection because it is the translated local origin, so
no additional activity is claimed for its repeated occurrences.  Therefore

\[
\boxed{\Sigma_{\rm let}(\mathcal E_r)\ge N_r.}
\tag{2.9}
\]

## 3. Literal exposure of the sloped-band matching

Fix \(0\le k\le r-1\).  For

\[
-k\le\sigma\le k,\qquad
1\le x\le r,\qquad
0\le v\le r-1,\qquad
x+v=r+\sigma,
\tag{3.1}
\]

put

\[
X_{x,v}=((x,r);0,v)=a_{r+x,v},
\tag{3.2}
\]

\[
Y_{x,v}=((x,r);1,v)=b_{r+x,v}.
\tag{3.3}
\]

Then

\[
X_{x,v}\lessdot Y_{x,v}.
\tag{3.4}
\]

Both targets lie in the corresponding parameter-\(k\) sloped bands of
\(\mathcal A_r,\mathcal B_r\): their abstract coordinates are respectively
\((x,r,v)\) and \((0,v,r+x)\), and (3.1) is exactly the band equation.
The edges form a matching of exact size

\[
\boxed{
M_r(k)=r(2k+1)-k(k+1).}
\tag{3.5}
\]

Indeed, for fixed \(\sigma\), equation (3.1) has \(r-|\sigma|\)
solutions.

### Theorem 3.1 (simultaneous band-compatible exposure — PROVED)

Every edge in (3.4) has, inside the one word \(\mathcal E_r\), a singleton
witness for \(X_{x,v}\) and a witness for \(Y_{x,v}\) sharing the same
left or right endpoint.  Hence \(\mathcal E_r\) exposes
\(M_r(k)\) distinct band-compatible cross-child endpoint sites.

#### Proof

This is the restriction of the witnesses in Theorem 2.1 to the matching
(3.1).  Matching edges have distinct \(X\)-positions, so the shared sites
are distinct.  Since the intervals are actual intervals of one word, their
left and right endpoint partitions are automatically simultaneous and
orthogonal. \(\square\)

For comparison with the endpoint dual, put

\[
k_r=\left\lfloor\frac{r-1}{8}\right\rfloor
\qquad(r\ge2).
\tag{3.6}
\]

The exact two-child endpoint toll is

\[
\Gamma_r=\gamma_A(r)+\gamma_B(r),
\tag{3.7}
\]

where

\[
\gamma_A(r)=
\max\left\{0,
\left\lceil
\frac{
2k_r(r+1)^2+
\dfrac{k_r(k_r+1)(k_r-12r-4)}3
}{2r+2k_r}
\right\rceil\right\},
\tag{3.8}
\]

\[
\gamma_B(r)=
\max\left\{0,
\left\lceil
\frac{
(2+2k_r)r^2+
\dfrac{k_r(k_r+1)(k_r-12r+8)}3
}{2r+2k_r}
\right\rceil\right\}.
\tag{3.9}
\]

At \(x=1/8\),

\[
2x-4x^2+\frac{x^3}{3}=\frac{289}{1536},
\qquad
2(1+x)=\frac94.
\]

Floors alter each quotient by \(O(r)\), and ceilings by \(O(1)\).  Hence

\[
\gamma_A(r)=\frac{289}{3456}r^2+O(r),
\qquad
\gamma_B(r)=\frac{289}{3456}r^2+O(r),
\tag{3.10}
\]

and

\[
\Gamma_r=\frac{289}{1728}r^2+O(r).
\tag{3.11}
\]

On the other hand,

\[
M_r(k_r)=\frac{15}{64}r^2+O(r).
\tag{3.12}
\]

Subtracting gives

\[
\boxed{
M_r(k_r)-\Gamma_r
=\frac{29}{432}r^2+O(r).}
\tag{3.13}
\]

Thus, for all sufficiently large \(r\), one literal word below the packet
width exposes more band-compatible shared endpoint positions than the
entire certified two-child endpoint toll.  This is a capacity and
chronology theorem for the selected interface targets.  It does not yet
extend the remaining band witnesses or cover the rest of the packet.

## 4. Cubic incidence across the full equal drain

The equal-cube packet decomposition is

\[
[0,R]^4
=\{\tau_0\}
\mathbin{\dot\cup}
\bigdotcup_{r=1}^R
\tau_r(\mathcal A_r\mathbin{\dot\cup}\mathcal B_r),
\qquad
\tau_r=(R-r,0,R-r,0).
\tag{4.1}
\]

Here

\[
M_R=\frac23R^3+2R^2+\frac73R+1.
\]

Translate \(\mathcal E_r\) by \(\tau_r\) and concatenate the translated
words, without separators.  All witnesses above stay inside one block.

### Theorem 4.1 (width-scale cubic incidence atlas — PROVED)

The concatenated interface word has exact length

\[
\boxed{
\sum_{r=1}^R|\mathcal E_r|
=M_R-1-2R-\left\lfloor\frac{R^2}{4}\right\rfloor.}
\tag{4.2}
\]

It contains

\[
\sum_{r=1}^R N_r
=\boxed{\frac{R(4R^2+9R-1)}6}
\tag{4.3}
\]

doubly active adjacent-child positions.  Moreover,

\[
\sum_{r=2}^R M_r(k_r)
=\frac5{64}R^3+O(R^2)
\tag{4.4}
\]

of its cross-child endpoint sites are compatible with the rational
sloped-band certificates, whereas

\[
\sum_{r=2}^R\Gamma_r
=\frac{289}{5184}R^3+O(R^2).
\tag{4.5}
\]

The positive capacity margin is

\[
\boxed{
\sum_{r=2}^R\bigl(M_r(k_r)-\Gamma_r\bigr)
=\frac{29}{1296}R^3+O(R^2).}
\tag{4.6}
\]

#### Proof

The packet widths telescope as

\[
M_R=1+\sum_{r=1}^R W_r.
\]

By (2.6),

\[
\sum_{r=1}^R|\mathcal E_r|
=M_R-1-\sum_{r=1}^R
\left(\left\lfloor\frac r2\right\rfloor+2\right).
\]

The elementary identity

\[
\sum_{r=1}^R\left\lfloor\frac r2\right\rfloor
=\left\lfloor\frac{R^2}{4}\right\rfloor
\]

gives (4.2).  Summing (1.8) gives (4.3).  Finally,
\(\sum_{r\le R}r^2=R^3/3+O(R^2)\); summing
(3.11)--(3.13) proves (4.4)--(4.6). \(\square\)

This theorem answers the incidence-capacity question sharply enough for
the known U3 ledgers.  The word uses only
\((2/3+o(1))R^3\) letters, the parent-width scale, while supplying cubic
letter-child and endpoint-child incidence.  It is nevertheless only a
partial universal word.

## 5. Optimality and local chronology taxes

The common-lift construction is optimal in the natural class which keeps
the \(a\)-interface literal and uses it as the selected endpoint for every
\(b\)-target.

### Theorem 5.1 (common-lift optimum — PROVED)

Suppose a word contains every \(a_{t,v}\), \((t,v)\in J_r\), literally,
and a selected witness for \(b_{t,v}\) uses that occurrence as one of its
endpoints.  Then the word contains at least

\[
\boxed{N_r+\left\lceil\frac r2\right\rceil}
\tag{5.1}
\]

positions.  Equality is attained by \(\mathcal E_r\).

#### Proof

Starting at the selected \(a_{t,v}\)-endpoint, traverse its
\(b_{t,v}\)-witness and truncate at the first occurrence whose third
coordinate is \(1\).  The truncated interval still has maximum
\(b_{t,v}\): the endpoint supplies \(h_t\) and \(v\), and the final
occurrence supplies the missing third-coordinate value.

Fix one such lift occurrence \(q\) and one side of \(q\).  If
\(a_{t,v}\) is nearer to \(q\) than \(a_{t',v'}\), then the former
occurrence lies in the latter's truncated witness.  Consequently

\[
a_{t,v}\le b_{t',v'},
\]

so

\[
t\le t',\qquad v\le v'.
\tag{5.2}
\]

Thus the indices assigned to one side of one lift occurrence form a chain
in the product order on \(J_r\).  A lift has two sides and supports at most
two such chains.

The poset \(J_r\) has width exactly \(r\).  The fixed-\(v\) sets give an
\(r\)-chain cover, while

\[
\{(r-v,v):0\le v<r\}
\tag{5.3}
\]

is an \(r\)-element antichain.  Therefore at least
\(\lceil r/2\rceil\) lift occurrences are necessary.  They are distinct
from all \(a\)-occurrences because their third coordinate is \(1\).
Together with the \(N_r\) forced literal interface positions this proves
(5.1). \(\square\)

This result rules out a chronology obstruction at quadratic scale inside
the common-lift model: only \(O(r)\) lift occurrences are needed.

### Proposition 5.2 (adjacent-lift tax — PROVED)

If every \(b_{t,v}\)-witness must instead be a two-letter interval
containing its literal \(a_{t,v}\) and an adjacent lift, the exact minimum
length is

\[
\boxed{
L_{\rm adj}(r)
=N_r+\left\lceil\frac{N_r}{2}\right\rceil.}
\tag{5.4}
\]

Consequently

\[
\boxed{
L_{\rm adj}(r)-W_r
=r^2-\left\lceil\frac r2\right\rceil-2.}
\tag{5.5}
\]

#### Proof

One lift occurrence has only two neighbours and therefore serves at most
two literal \(a\)-positions.  This proves the lower bound.  Pair arbitrary
\(a\)-indices and use blocks

\[
a_j,e,a_{j'}.
\]

For an unpaired index use \(a_j,e\).  The two adjacent intervals have the
required maxima by (1.9), proving equality.  Substitution of
\(N_r=2r^2+r-1\) gives (5.5). \(\square\)

If the specified adjacent letter must be \(b_{t,v}\) itself, the disjoint
cover edges force exact length

\[
2N_r+1=4r^2+2r-1,
\tag{5.6}
\]

an excess \(2r^2-2\) above \(W_r\).  Nonlocal monotone batching is
therefore essential.

## 6. Why the interface is not PACK

Theorem 2.1 covers no target outside \(F_A\cup F_B\).  Among nonzero packet
targets, the exact missing counts are

\[
\boxed{
|\mathcal A_r^*\setminus F_A|
=(2r+1)(r^2+r+1),}
\tag{6.1}
\]

\[
\boxed{
|\mathcal B_r\setminus F_B|
=(2r+1)r(r-1).}
\tag{6.2}
\]

These cubic target counts are not length lower bounds.

There is a small exact completion obstruction.  The missing axis targets

\[
((x,0);h_0),\qquad1\le x\le r,
\tag{6.3}
\]

and

\[
(h_0;(x,0)),\qquad2\le x\le r,
\tag{6.4}
\]

must occur literally.  For example, every letter in a witness for the
first target has all coordinates except the first equal to zero, and some
letter must attain first coordinate \(x\); that letter is the target
itself.  The second family is symmetric.

None of these \(2r-1\) points occurs in \(\mathcal E_r\).  Hence every
completion which retains \(\mathcal E_r\) as an immutable subword needs at
least \(2r-1\) new positions.  Since its unused exact-width allowance is
only \(\lfloor r/2\rfloor+2\), such a completion cannot have length \(W_r\)
for \(r\ge3\).

This is only a linear deficit:

\[
2r-1=o(r^2).
\]

It neither disproves PACK nor prevents modifying the interface letters
while retaining their endpoint function.

## 7. The exact middle-queue absorption obstruction

The next theorem permits arbitrary ambient letters, crossing intervals,
and unbounded endpoint degree.

### Theorem 7.1 (middle-queue invariant — PROVED)

Let \(r\ge2\), and let an arbitrary word covering
\(\mathcal A_r\cup\mathcal B_r\) have length

\[
n=W_r+e.
\tag{7.1}
\]

Choose arbitrary witnesses for the two parameter-\(k_r\) sloped-band
families used in (3.8)--(3.9).  Let \(L_A,R_A,L_B,R_B\) be their sets of
physical left and right endpoint sites, and put

\[
S_L=L_A\cap L_B,\qquad S_R=R_A\cap R_B.
\tag{7.2}
\]

Independently choose witnesses for all \(W_r\) targets in the two aligned
packet-middle layers.  Let \(Q_L,Q_R\) be their left and right endpoint
sets.  Define the side-typed absorption count

\[
a=|S_L\cap Q_L|+|S_R\cap Q_R|.
\tag{7.3}
\]

Then

\[
\boxed{4e+a\ge\Gamma_r.}
\tag{7.4}
\]

#### Proof

The endpoint certificates give

\[
|L_A|+|R_A|+|L_B|+|R_B|
\ge2W_r+\Gamma_r.
\tag{7.5}
\]

Each left or right union uses at most \(n\) sites.  Therefore

\[
2W_r+\Gamma_r
\le2n+|S_L|+|S_R|,
\]

and

\[
|S_L|+|S_R|\ge\Gamma_r-2e.
\tag{7.6}
\]

Distinct aligned-middle targets are incomparable.  Targets with one common
left endpoint have nested intervals and hence comparable maxima.  Thus the
middle left endpoints are all distinct; the same holds on the right:

\[
|Q_L|=|Q_R|=W_r.
\tag{7.7}
\]

Exactly \(e=n-W_r\) word positions lie outside each middle queue.  Hence

\[
|S_L|\le|S_L\cap Q_L|+e,
\qquad
|S_R|\le|S_R\cap Q_R|+e.
\tag{7.8}
\]

Combining (7.6)--(7.8) proves (7.4). \(\square\)

Left and right types are counted separately.  A physical site belonging to
both \(S_L\) and \(S_R\) contributes twice, exactly as the endpoint dual
requires.  The proof is a two-child theorem; with three or more children,
set intersections must be replaced by endpoint multiplicity excess.

### Corollary 7.2 (off-middle portal no-go — PROVED)

Suppose every site in \(S_L\cup S_R\) carries a physical word letter
dominated by no target in the aligned packet-middle antichain.  Then

\[
\boxed{
e\ge\left\lceil\frac{\Gamma_r}{4}\right\rceil
=\left(\frac{289}{6912}+o(1)\right)r^2.}
\tag{7.9}
\]

In particular, this holds if every shared band-endpoint letter has rank
strictly above the aligned middle rank \(2r\).

#### Proof

If a site lies in a selected middle witness, its physical letter is at
most that middle target.  Under the hypothesis no shared site belongs to
\(Q_L\) or \(Q_R\), so \(a=0\).  Apply (7.4). \(\square\)

Thus high-letter connector surfaces cannot complete PACK at
subquadratic excess.  A surviving surface braid must place a positive
density of its shared endpoints directly into the middle endpoint queues,
with letters lying below the corresponding middle targets.

At one absorbed left site, the selected \(\mathcal A_r\)-band target,
\(\mathcal B_r\)-band target, and middle target all lie in one target-poset
chain.  The common physical letter lies below all three.  This is the exact
pin-compatible absorption requirement which remains open.

## 8. An onion-blocked quadratic no-go

The common-lift braid crosses not only the child seam but also the natural
onion-chain labels.  The necessity of doing so is exact.

Define

\[
C_i=(i,0)+H_{r-i},
\qquad0\le i\le r.
\tag{8.1}
\]

Then

\[
S_r=\bigsqcup_{i=0}^rC_i,\qquad
I_r=\bigsqcup_{i=1}^rC_i,
\tag{8.2}
\]

and \(C_i\) has edge height

\[
p_i=2(r-i).
\tag{8.3}
\]

Put

\[
R_i=C_i\times H_r\subset\mathcal A_r
\qquad(0\le i\le r),
\tag{8.4}
\]

and, only for \(1\le i\le r\),

\[
Q_i=H_r\times C_i\subset\mathcal B_r.
\tag{8.4a}
\]

### Theorem 8.1 (aligned onion-block obstruction — PROVED)

Suppose

\[
\mathcal W=\mathcal W_0\Vert\mathcal W_1\Vert\cdots\Vert\mathcal W_r,
\]

where \(\mathcal W_0\) uses letters in \(R_0\) and internally covers
\(R_0\setminus\{0\}\), while for \(i\ge1\), the block
\(\mathcal W_i\) uses letters in \(R_i\cup Q_i\) and every target of that
union has an internal witness.  Then

\[
\boxed{|\mathcal W|\ge5r^2+3r.}
\tag{8.5}
\]

In particular, its excess above \(W_r\) is at least

\[
\boxed{3r^2+r-1.}
\tag{8.6}
\]

#### Proof

For two chains of edge heights \(p,q\), a word restricted to their
rectangle has minimum \(p+q\) when the rectangle minimum is the excluded
zero, and \(p+q+1\) when that minimum is demanded.  Both coordinate axes
are forced literally.  Conversely, a decreasing copy of the first axis
followed by the minimum and an increasing copy of the second axis covers
the rectangle; omit the minimum in the zero-excluded case.

Thus \(R_0=H_r\times H_r\) costs \(4r\).

Fix \(i\ge1\).  In \(R_i\), the axes

\[
C_i\times\{h_0\},
\qquad
\{c_{i,0}\}\times H_r
\]

do not both remain wholly forced after cross-child joins.  The following
subfamilies do.

First, every point of \(C_i\times\{h_0\}\) is forced literally: no
\(Q_i\)-letter has second factor at most \(h_0\).  This gives \(p_i+1\)
points.

Second, on \(\{c_{i,0}\}\times H_r\), every vertical-hook point
\[
(c_{i,0};(0,j)),\qquad0\le j\le r,
\]
and every horizontal-hook point
\[
(c_{i,0};(x,r)),\qquad1\le x<i,
\]
is forced.  Indeed, a \(Q_i\)-letter below such a target would have first
factor \(h_0\) and second factor in \(C_i\); but every point of \(C_i\) has
first coordinate at least \(i\), so it lies below neither \((0,j)\) nor
\((x,r)\) with \(x<i\).  The remaining eligible letters lie in \(R_i\),
and the chain axis forces the target itself.

The two displayed \(R_i\)-families intersect in one point and therefore
force

\[
(p_i+1)+(r+i)-1=p_i+r+i=3r-i
\tag{8.7}
\]

literal positions.  The symmetric argument gives \(3r-i\) forced
positions in \(Q_i\).  The two collections are disjoint because
\(C_i\cap H_r=\varnothing\).

Consequently

\[
|\mathcal W_i|
\ge2(3r-i).
\tag{8.8}
\]

Summing gives

\[
|\mathcal W|
\ge4r+\sum_{i=1}^r2(3r-i)
=5r^2+3r.
\]

Subtracting (0.1) gives (8.6). \(\square\)

The omitted horizontal targets really can evade the literal-axis count.
For \(x\ge i\),

\[
(c_{i,0};(x,r))
=
(c_{i,0};(0,r))
\vee
(h_0;(x,r-i)),
\tag{8.9}
\]

and \((x,r-i)\in C_i\).  Thus the formerly tempting
\(6r^2+4r\) lower bound is false.  Here is an explicit full-word
counterexample to that putative bound.  In the terminal block \(i=r\), put
\(c=(r,0)\) and retain the \(4r\) literals

\[
(c;h_t),\ (h_t;c),
\qquad0\le t<2r.
\tag{8.10}
\]

Order \((c;h_r),(h_0;c)\) adjacently and also
\((h_r;c),(c;h_0)\) adjacently.  Their joins are respectively

\[
(c;h_{2r}),\qquad(h_{2r};c),
\tag{8.11}
\]

the two omitted top targets.  Thus this block has length \(4r\), two less
than its separate-rectangle length \(4r+2\).  Use the separate rectangle
words in every earlier block.  The resulting valid onion-blocked word has
length \(6r^2+4r-2\).

Separate rectangle words still give the simpler upper bound \(6r^2+4r\);
the exact blocked minimum between (8.5) and the improved upper bound is not
determined.

This theorem is strictly architecture-scoped.  It proves that a successful
PACK word must cross onion labels as well as the child seam; it is not an
unrestricted packet lower bound.

## 9. Exact remaining theorem

The raw incidence-capacity and selected-interface chronology problems are
now solved, but PACK remains:

> **Pin-compatible packet absorption — UNPROVED.**  For every \(r\),
> construct one ambient word covering all nonzero targets in
> \(\mathcal A_r\cup\mathcal B_r\), of length
> \[
> W_r+\varepsilon(r)r^2,
> \qquad
> \varepsilon(r)\to0,
> \]
> while absorbing \(\Gamma_r-o(r^2)\) side-typed cross-child band endpoint
> sites into the aligned middle endpoint queues.

The common-lift braid proves that the required number of portals, their
simultaneous left/right chronology, and nonlocal reset-free batching all
fit inside the width scale.  Theorem 7.1 proves that appending those portals
outside a middle construction cannot work.  The missing operation is to
replace a positive-density subset of the middle carriers by common-lift
portal carriers while preserving:

1. all four coordinate pins of every affected middle target;
2. the remaining sloped-band target witnesses;
3. coverage of the packet targets outside \(F_A\cup F_B\); and
4. one acyclic physical interval order.

No lemma above proves that this replacement exists or is impossible.

## 10. Audit and implication ledger

### Proved

- the common-lift word and every witness in Theorem 2.1;
- its exact length, target count, endpoint sharing, and activity count;
- simultaneous exposure of the sloped-band seam matching;
- the exact full-drain length and cubic incidence totals;
- optimality in the common-lift class;
- the sharp adjacent-lift quadratic tax;
- the \(2r-1\) immutable-module completion deficit;
- the exact middle-queue invariant and off-middle corollary;
- the aligned onion-blocked quadratic lower bound.

### Unproved

- a full \(W_r+o(r^2)\) packet word;
- pin-compatible absorption of the interface portals into the middle
  endpoint queues;
- an unrestricted \(\Omega(r^2)\) packet excess;
- the equal four-box constant-one theorem.

### Independent audits

1. A construction audit reconstructed every interval in
   \(\mathcal E_r\), both child projections, the matching embedding, and
   all constants in (3.10)--(4.6).  It also reconstructed the
   common-lift and adjacent-lift lower bounds and the middle-queue
   invariant.  Verdict: pass.

2. A separate endpoint audit rederived (7.5)--(7.8) from distinct
   endpoint-site sets, checked that high endpoint degree creates no hidden
   multiplicity term for two children, and verified both exact
   \(\gamma\)-formulae and the \(289/6912\) corollary.  It required the
   explicit hypotheses \(r\ge2\) and that **every** shared band-endpoint
   site, rather than merely a named portal subset, satisfy the off-middle
   condition.  Those qualifications are present in Section 7.

3. The first onion-block audit found a genuine false step in the proposed
   \(6r^2+4r\) lower bound: horizontal axis targets with \(x\ge i\) factor
   across \(R_i,Q_i\) as in (8.9).  The report therefore retains that
   number only as an upper construction and uses the independently
   rechecked forced subfamilies yielding \(5r^2+3r\).  No sharpness is
   claimed.  The terminal-block word (8.10)--(8.11) independently confirms
   that the discarded lower bound is actually false, not merely unproved.

4. A final cross-audit rederived the first-lift truncation in Theorem 5.1,
   verified \(\operatorname{width}(J_r)=r\), and rechecked the repaired
   \(5r^2+3r\) count.  It also caught the domain point that \(Q_i\) belongs
   to \(\mathcal B_r\) only for \(i\ge1\); (8.4)--(8.4a) now state this
   explicitly.  Verdict after repair: pass.

### Logical scope

\[
\boxed{
\begin{gathered}
\text{cubic isolated child bill}\\
\Longrightarrow
\text{cubic sharing demand}\\
\xRightarrow[\text{Theorems 2.1--4.1}]
{\text{literal construction}}
\text{width-scale incidence atlas}.
\end{gathered}}
\tag{10.1}
\]

Therefore no obstruction based only on the quantity of shared sites,
left/right endpoint orientation within the selected interface matching,
or additive reset cost can rule out the equal surface braid.  Complete
sloped-band endpoint partitions have not been embedded.

On the other hand,

\[
\boxed{
\text{near-width PACK}
\Longrightarrow
\Theta(r^2)\text{ middle-queue absorption}.}
\tag{10.2}
\]

The implication in (10.2) is an exact pin/chronology condition, not a
construction.  Resolving that absorption step is the theorem left open by
fifth-wave U.
