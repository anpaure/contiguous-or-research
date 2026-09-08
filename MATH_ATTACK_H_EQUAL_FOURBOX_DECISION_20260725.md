# Mathematical attack H: equal four-box decision

Date: 2026-07-25

## 0. Verdict

For a finite product of chains \(Q\), let \(g(Q)\) be the least length of
a word of nonzero points of \(Q\) whose nonempty contiguous
coordinatewise maxima contain every nonzero point of \(Q\).  For

\[
Q_t=[0,t]^4
\]

write

\[
W_t=w(Q_t)
=[z^{2t}](1+z+\cdots+z^t)^4
=\frac{2t^3+6t^2+7t+3}{3}.
\tag{0.1}
\]

Indeed,
\[
W_t=\binom{2t+3}{3}-4\binom{t+2}{3}
\]
by inclusion-exclusion.  The rank sequence is symmetric and unimodal
(also a consequence of Lemma 3.2), so this central coefficient is the
width.

This attack proves neither

\[
g(Q_t)=W_t+o(t^3)
\tag{0.2}
\]

nor

\[
g(Q_t)\ge W_t+\Omega(t^3).
\tag{0.3}
\]

It does give a stable decision on the two most immediate equal-point
mechanisms.

1. The complementary packet has an exact body-centred-cube normal form.
   Its aligned middle layer is a checkerboard square, and its concentric
   square rings alternate between the two packet types.

2. The natural construction which keeps those rings as intact epochs is
   impossible.  It misses at least

   \[
   \frac{r^3}{800}-O(r^2)
   \tag{0.4}
   \]

   literal upper-shoulder targets in the \(r\)-th packet.  This permits
   either radial direction, arbitrary cuts and orientations of every
   ring, and one repeated cut endpoint.  Every interval witness is checked
   literally.

3. Same-left and same-right pairings between two fixed-rank antichains
   form an alternating forest.  However, when the whole middle layer is
   retained, the component credit visible in the static comparability
   graph never exceeds the width deficit.  Static disconnectedness alone
   cannot prove (0.3).

4. Every single moving-plateau endpoint certificate is also decided.  For
   \([0,t]^3\times[0,dt]\), the whole family is subcritical on

   \[
   1\le d\le d_*:=3-\delta_*,
   \qquad
   5\delta_*^3-18\delta_*^2+24=0,
   \quad \frac32<\delta_*<2.
   \tag{0.5}
   \]

   At equality \(d=1\), the best-placed plateau of fixed relative height
   \(0<\alpha\le1\) misses width by

   \[
   \left(
   \frac{\alpha}{6}
   +\frac{\alpha^2}{2}
   +\frac{\alpha^3(1-\alpha)}{24}
   \right)t^3+o(t^3).
   \tag{0.6}
   \]

   For \(d_*<d<3\), the one-sided derivative reverses and recovers the
   known bridge-band obstruction.  Thus (0.5) is the sharp sign threshold
   for this carrier family.

The result in item 2 is a positive-density obstruction to an explicit
architecture, not an unrestricted lower bound for \(g(Q_t)\).  Its exact
message is that a successful packet braid must create same-colour
cross-radius corridors.  Alternating separate radius epochs cannot work.

No web search, finite search, or computational experiment is used.

---

## 1. Exact checkerboard coordinates for the complementary packet

Let

\[
S_r=[0,r]^2
\]

and define the saturated boundary chain

\[
h_r(j)=
\begin{cases}
(0,j),&0\le j\le r,\\
(j-r,r),&r\le j\le2r.
\end{cases}
\tag{1.1}
\]

Thus

\[
H_r=\{h_r(j):0\le j\le2r\}.
\tag{1.2}
\]

Put

\[
I_r=\{1,\ldots,r\}\times\{0,\ldots,r-1\},
\tag{1.3}
\]

\[
\mathcal A_r=S_r\times H_r,
\qquad
\mathcal B_r=H_r\times I_r.
\tag{1.4}
\]

These are the two disjoint packets in the complementary-shell peel.  Let

\[
\Lambda_r=
\{(a,b,c)\in[-r,r]^3\cap\mathbb Z^3:a\equiv b\pmod2\}.
\tag{1.5}
\]

### Theorem 1.1 (body-centred-cube packet form)

Define

\[
\Phi_r:\Lambda_r\longrightarrow
\mathcal A_r\mathbin{\dot\cup}\mathcal B_r
\tag{1.6}
\]

by

\[
\Phi_r(a,b,c)=
\begin{cases}
\left(
\dfrac{a+r}{2},\dfrac{b+r}{2},h_r(c+r)
\right),
&a\equiv b\equiv r\pmod2,\\[3mm]
\left(
h_r(c+r),\dfrac{a+r+1}{2},\dfrac{b+r-1}{2}
\right),
&a\equiv b\not\equiv r\pmod2.
\end{cases}
\tag{1.7}
\]

Then \(\Phi_r\) is a bijection and

\[
\boxed{
|\Phi_r(a,b,c)|-2r=\frac{a+b}{2}+c.}
\tag{1.8}
\]

Consequently the aligned packet middle layer is

\[
c=-\frac{a+b}{2}.
\tag{1.9}
\]

After suppressing \(c\), it is the checkerboard square

\[
\{(a,b)\in[-r,r]^2:a\equiv b\pmod2\}
\tag{1.10}
\]

of cardinality

\[
(r+1)^2+r^2.
\tag{1.11}
\]

For \(s\ge1\), its square ring

\[
\mathcal R_s=
\{(a,b):\max(|a|,|b|)=s,\ a\equiv b\pmod2\}
\tag{1.12}
\]

has \(4s\) points.  It lies in \(\mathcal A_r\) exactly when
\(s\equiv r\pmod2\), and otherwise lies in \(\mathcal B_r\).

#### Proof

On the first parity class the inverse map is

\[
(x,y,h_r(j))\longmapsto(2x-r,2y-r,j-r).
\tag{1.13}
\]

On the other parity class it is

\[
(h_r(j),u,v)
\longmapsto(2u-r-1,2v-r+1,j-r).
\tag{1.14}
\]

If \(a\equiv r\pmod2\), then \((a+r)/2\in[0,r]\).  If
\(a\not\equiv r\pmod2\), its extreme possible values are
\(-r+1\) and \(r-1\), so

\[
1\le\frac{a+r+1}{2}\le r.
\]

The same calculation gives

\[
0\le\frac{b+r-1}{2}\le r-1.
\]

Thus (1.13) and (1.14) are inverse bijections onto
\(\mathcal A_r\) and \(\mathcal B_r\), respectively.

The chain rank of \(h_r(j)\) is \(j\).  In either parity class the
coordinate sum of (1.7) is

\[
r+\frac{a+b}{2}+r+c,
\]

which proves (1.8).  Equation (1.9) follows.

On \(\mathcal R_s\), one of \(a,b\) is \(s\) or \(-s\).  Since
\(a\equiv b\pmod2\), both have parity \(s\), proving the type
alternation.  The allowed values on one side of the step-two square are
\(-s,-s+2,\ldots,s\); its boundary therefore has \(4s\) points.  Finally,

\[
1+\sum_{s=1}^r4s
=2r^2+2r+1
=(r+1)^2+r^2.
\]

This proves (1.11). \(\square\)

### Corollary 1.2 (exact constructive gate)

Suppose that, for every \(r\), there is one word of nonzero ambient
points of \([0,r]^4\), of length

\[
(r+1)^2+r^2+e_r,
\tag{1.15}
\]

such that every nonzero \(\Phi_r(a,b,c)\) is the coordinatewise maximum
of one actual contiguous interval.  If \(e_r=o(r^2)\), then

\[
g(Q_R)=W_R+o(R^3).
\tag{1.16}
\]

#### Proof

The checkerboard coordinates are only a bijective relabelling; no
abstract join is substituted for a physical interval.

The packet peel is

\[
[0,r]^4
=\mathcal A_r\mathbin{\dot\cup}\mathcal B_r
\mathbin{\dot\cup}(I_r\times I_r).
\tag{1.17}
\]

For a final cube of side \(R\), translate level \(r\) by

\[
\tau_r=(R-r,0,R-r,0).
\]

Since

\[
\tau_r+(I_r\times I_r)
=\tau_{r-1}+([0,r-1]^2\times[0,r-1]^2),
\]

the translated packets, together with the terminal point, partition the
cube.  Concatenating the translated packet words preserves every internal
witness.  The \(R-1\) noninitial translated local zeros and the terminal
point cost \(R\) singleton positions.  Therefore the length is at most

\[
(W_R-1)+\sum_{r=1}^Re_r+R
=W_R+\sum_{r=1}^Re_r+R-1.
\]

Weighted Cesàro summation gives
\(\sum_{r\le R}e_r=o(R^3)\). \(\square\)

---

## 2. A cubic literal shoulder obstruction to intact ring epochs

For each nonzero \(\mathcal R_s\), choose either orientation of its square
boundary and cut it at an arbitrary point.  Write each ring point once;
repeating the cut point once at the opposite end is allowed.  Concatenate
the rings in either radial order

\[
\mathcal R_0\Vert\mathcal R_1\Vert\cdots\Vert\mathcal R_r
\tag{2.1}
\]

or its reverse, and replace \((a,b)\) by
\(\Phi_r(a,b,-(a+b)/2)\).  Call any such word an **intact alternating
ring row**.

### Theorem 2.1 (positive-density ring-shoulder obstruction)

Let

\[
T=(x,y,k,r)\in\mathcal A_r,
\qquad1\le k\le r,
\tag{2.2}
\]

and put

\[
A=2x-r,
\qquad B=2y-r.
\tag{2.3}
\]

Suppose

\[
k>\max\{|A|,|B|\},
\qquad
k\not\equiv r\pmod2,
\tag{2.4}
\]

and

\[
y+k\le r,
\qquad
x+y+k\ge r.
\tag{2.5}
\]

Then \(T\) is not the coordinatewise maximum of any contiguous interval
in any intact alternating ring row.

There are at least

\[
\boxed{\frac{r^3}{800}-O(r^2)}
\tag{2.6}
\]

such upper-shoulder targets.

#### Proof

We check an arbitrary literal interval.

First, no aligned-middle point of \(\mathcal B_r\) lies below \(T\).
Such a point has the form

\[
P=(h_r(j),u,v),
\qquad
j+u+v=2r,
\qquad
(u,v)\in I_r.
\tag{2.7}
\]

If \(P\le T\), then \(y+k\le r\) and \(k\ge1\) give \(y<r\).
Consequently \(j<r\), because the second coordinate of \(h_r(j)\) is
\(r\) when \(j\ge r\).  Thus

\[
h_r(j)=(0,j),
\qquad j\le y.
\]

Also \(u\le k\), while \(v\le r-1\).  Equation (2.7) would give

\[
2r=j+u+v
\le y+k+r-1
\le2r-1,
\]

a contradiction.

Every letter in an interval with maximum \(T\) must be at most \(T\).
Hence such an interval cannot meet a \(\mathcal B_r\)-ring.  Two
\(\mathcal A_r\)-rings are separated in (2.1) by a nonempty
\(\mathcal B_r\)-ring, so every putative witness lies in one
\(\mathcal A_r\)-ring.

Let that radius be \(s\).  An aligned-middle \(\mathcal A_r\)-point with
centred coordinates \((a,b)\) has hook deviation

\[
c=-\frac{a+b}{2}.
\]

It lies below \(T\) exactly when

\[
a\le A,
\qquad
b\le B,
\qquad
a+b\ge-2k.
\tag{2.8}
\]

For an interval maximum to equal \(T\), the interval must also satisfy
the three literal pin equations

\[
\max a=A,
\qquad
\max b=B,
\qquad
\min(a+b)=-2k.
\tag{2.9}
\]

All points on an \(\mathcal A_r\)-ring have
\(a\equiv b\equiv r\pmod2\).  Since
\(k\not\equiv r\pmod2\), a solution of \(a+b=-2k\) cannot be
\((-k,-k)\).  Therefore one coordinate has absolute value at least
\(k+1\), and

\[
s\ge k+1.
\tag{2.10}
\]

By (2.4), \(|A|,|B|<k<s\).  The only legal ring point which can pin the
first coordinate without violating \(b\le B\) is

\[
P_A=(A,-s);
\tag{2.11}
\]

the other point \((A,s)\) has \(s>B\).  Similarly the only possible
second-coordinate pin is

\[
P_B=(-s,B).
\tag{2.12}
\]

The southwest boundary arc from \(P_A\) to \(P_B\) contains
\((-s,-s)\), whose sum is

\[
-2s<-2k,
\]

contradicting (2.8).  The complementary arc crosses the top or right
side and therefore contains a point with \(a=s>A\) or \(b=s>B\), again
contradicting (2.8).  Both cyclic arcs contaminate.  Hence no linear
interval in any cut or orientation of the once-around boundary works;
repeating the cut point does not create another arc.

For the count, restrict to

\[
\frac{2r}{5}\le k\le\frac r2,
\qquad
k\not\equiv r\pmod2,
\tag{2.13}
\]

\[
\frac{7r}{20}\le x\le\frac{3r}{5},
\qquad
\frac{7r}{20}\le y\le\frac{9r}{20}.
\tag{2.14}
\]

Then

\[
|2x-r|,|2y-r|\le\frac{3r}{10}<k,
\]

\[
y+k\le\frac{19r}{20}<r,
\qquad
x+y+k\ge\frac{11r}{10}>r.
\]

Thus all these triples satisfy (2.4)--(2.5).  Their numbers of choices
are, respectively,

\[
\frac r{20}+O(1),
\qquad
\frac r4+O(1),
\qquad
\frac r{10}+O(1).
\]

Multiplication proves (2.6). \(\square\)

The last inequality in (2.5) gives
\(|T|=x+y+k+r\ge2r\), so the counted family is genuinely an upper
shoulder.  The theorem rules out intact radius epochs, not arbitrary
cross-radius interleavings or non-middle letters.

---

## 3. Alternating endpoint chronology and its static ceiling

### Lemma 3.1 (alternating endpoint forest)

Let \(A,B\) be disjoint antichains in a product of chains.  Assume every
comparable cross-pair is oriented \(a<b\), with \(a\in A\), \(b\in B\);
this holds in particular for two fixed ranks with \(A\) below \(B\).
Choose one actual witnessing interval

\[
I_x=[\ell_x,r_x]
\]

for every \(x\in A\cup B\), and use this same witness in both endpoint
partitions.  Put an \(L\)-edge \(ab\) when \(\ell_a=\ell_b\), and an
\(R\)-edge when \(r_a=r_b\).

Then each colour is a matching, the colours are edge-disjoint, and their
union is a spanning forest.  If \(c\) is its number of components,
including isolated vertices, every word of length \(n\) satisfies

\[
\boxed{2n\ge |A|+|B|+c.}
\tag{3.1}
\]

#### Proof

Targets with one fixed left endpoint form a chain, because increasing
the right endpoint enlarges the interval and its maximum.  An endpoint
class therefore contains at most one point from each antichain.  Thus
each colour is a matching.  A pair cannot carry both colours: its two
targets would then have the same interval and the same maximum.

If a cycle existed, its colours would alternate.  Label it

\[
a_i\mathbin{-_L}b_i\mathbin{-_R}a_{i+1}
\qquad(i\bmod q).
\]

Since \(a_i<b_i\) and their intervals have the same left endpoint,
their distinct maxima force

\[
r(a_i)<r(b_i)=r(a_{i+1}).
\]

Going around the cycle gives

\[
r(a_1)<r(a_2)<\cdots<r(a_q)<r(a_1),
\]

a contradiction.

Put \(v=|A|+|B|\), and let \(e_L,e_R\) be the matching sizes.  The
numbers of restricted endpoint classes are \(v-e_L\) and \(v-e_R\), each
at most \(n\).  Since the union is a forest,

\[
c=v-e_L-e_R.
\]

Adding the two class bounds proves (3.1). \(\square\)

We include the normality fact needed for the static comparison.

### Lemma 3.2 (normalized matching for products of chains)

Let

\[
P=\prod_{h=1}^d[0,t_h],
\qquad p_j=|P_j|.
\]

For \(r<s\), \(S\subseteq P_s\), and

\[
N_r(S)=\{x\in P_r:x\le y\text{ for some }y\in S\},
\]

one has

\[
\boxed{\frac{|N_r(S)|}{p_r}\ge\frac{|S|}{p_s}.}
\tag{3.2}
\]

#### Proof

A normalized flow between adjacent ranks \(P_k,P_{k+1}\) is a
nonnegative weight \(f(x,y)\), supported on covers, with every row sum
\(1/p_k\) and every column sum \(1/p_{k+1}\).  Composing such flows from
rank \(r\) to rank \(s\) gives weights \(F(x,y)\), supported on
\(x\le y\), with uniform marginals.  Then

\[
\frac{|S|}{p_s}
=\sum_{y\in S,x}F(x,y)
\le\sum_{x\in N_r(S),y}F(x,y)
=\frac{|N_r(S)|}{p_r}.
\tag{3.3}
\]

It remains to construct adjacent flows.  We prove closure under products.
Suppose ranked posets \(P,Q\) already have normalized flows and have
log-concave rank sequences \(p_i,q_j\) without internal zeros.  Put

\[
r_k=\sum_i p_iq_{k-i}.
\]

The normalized masses of source cell \(P_i\times Q_{k-i}\) and target
cell \(P_i\times Q_{k+1-i}\) are

\[
A_i=\frac{p_iq_{k-i}}{r_k},
\qquad
B_i=\frac{p_iq_{k+1-i}}{r_{k+1}}.
\tag{3.4}
\]

Log-concavity gives

\[
\sum_{j\le i-1}A_j
\le\sum_{j\le i}B_j
\le\sum_{j\le i}A_j.
\tag{3.5}
\]

Indeed,
\[
\frac{A_i}{B_i}
=\frac{r_{k+1}}{r_k}\frac{q_{k-i}}{q_{k+1-i}}
\]
is nonincreasing in \(i\), while
\[
\frac{A_{i-1}}{B_i}
=\frac{r_{k+1}}{r_k}\frac{p_{i-1}}{p_i}
\]
is nondecreasing.  Each likelihood ratio crosses \(1\) at most once, and
summing before and after that crossing gives the two prefix inequalities.
Zeros at the ends of the supports are handled by deleting the zero terms
before taking ratios; they contribute the corresponding endpoint
inequalities directly.

Set

\[
x_i=\sum_{j\le i}(A_j-B_j).
\]

Then (3.5) says \(0\le x_i\le A_i\).  Send mass \(x_i\) from source
cell \(i\) to target cell \(i+1\) by incrementing \(P\), and mass
\(A_i-x_i\) to target cell \(i\) by incrementing \(Q\).  Target cell
\(i\) receives

\[
(A_i-x_i)+x_{i-1}=B_i.
\tag{3.6}
\]

Lift the first transfer with weight

\[
\frac{x_i}{q_{k-i}}f_P(u,u')
\]

on \(((u,v),(u',v))\), and the second with weight

\[
\frac{A_i-x_i}{p_i}f_Q(v,v')
\]

on \(((u,v),(u,v'))\).  Each source row sum is \(1/r_k\), and (3.6)
makes each target column sum \(1/r_{k+1}\).  Thus products preserve
normalized flows.

A chain has trivial normalized flows and rank sequence
\((1,\ldots,1)\).  Convolution preserves log-concavity without internal
zeros: equivalently, the Toeplitz matrix is totally positive of order
two; Toeplitz matrices multiply under convolution, and Cauchy--Binet
preserves every \(2\times2\) minor.  Induction on the chain factors
completes the proof. \(\square\)

### Theorem 3.3 (static component credit never beats width)

Let \(t\ge1\), and let

\[
M=(Q_t)_{2t},
\qquad |M|=W_t,
\]

and let \(B\subseteq(Q_t)_s\) for one rank \(2t<s\le4t\).  In the
static bipartite graph \(H(M,B)\), join every comparable pair.  Then

\[
\boxed{c(H(M,B))\le W_t-|B|.}
\tag{3.7}
\]

Hence substituting only the static component count into Lemma 3.1 never
gives a lower-bound right-hand side exceeding \(2W_t\).

#### Proof

Let \(B_j\cup N_j\) be a nontrivial connected component.  Lemma 3.2
gives

\[
\frac{|N_j|}{W_t}
\ge\frac{|B_j|}{|(Q_t)_s|}.
\tag{3.8}
\]

The rank numbers of \(Q_t\) are strictly increasing through rank \(2t\).
For \(0\le q<2t\), inclusion-exclusion gives

\[
|(Q_t)_q|
=\binom{q+3}{3}-4\binom{q-t+2}{3},
\tag{3.9}
\]

with the second binomial zero when its upper argument is below \(3\).
For \(q=t+u\), \(0\le u\le t-1\), the forward difference is

\[
\binom{t+u+3}{2}-4\binom{u+2}{2}.
\tag{3.10}
\]

This is a concave quadratic in \(u\) and is positive at both endpoints:
at \(u=t-1\) it is \(t+1\), while at \(u=0\) it is
\(\binom{t+3}{2}-4>0\).  Below \(t\), strict increase is immediate.
Rank symmetry therefore gives

\[
|(Q_t)_s|<W_t.
\tag{3.11}
\]

Equations (3.8)--(3.11) imply

\[
|N_j|\ge|B_j|+1.
\tag{3.12}
\]

If there are \(q\) nontrivial components, then
\(|N(B)|\ge|B|+q\).  The other \(W_t-|N(B)|\) middle vertices are
isolated.  There are no isolated vertices on the \(B\)-side: any target
of rank above \(2t\) can be decreased coordinatewise to total rank
\(2t\).  Hence

\[
c(H(M,B))
=W_t-|N(B)|+q
\le W_t-|B|.
\]

The static contribution to the right side of (3.1) is therefore at most

\[
W_t+|B|+(W_t-|B|)=2W_t.
\]

This proves the theorem. \(\square\)

The actual endpoint forest is only a spanning subgraph of \(H(M,B)\) and
may have more components.  The theorem rules out static disconnectedness,
not an actual chronology or coordinate-pin obstruction.

---

## 4. Exact moving-plateau ledger

Let \(t\ge1\), and let

\[
Q=[0,t]^3\times[0,s],
\qquad s\ge1.
\]

Choose integers

\[
0\le H\le s,
\qquad
L=s-H,
\]

and choose an integer \(a\) such that

\[
[a,a+L]\subseteq[0,3t],
\qquad
a+L>0.
\]

Put

\[
S=\{x\in[0,t]^3:a\le|x|\le a+L\},
\qquad B=|S|,
\tag{4.1}
\]

and define

\[
T_{x,j}=(x,a+L-|x|+j),
\qquad
x\in S,\quad0\le j\le H.
\tag{4.2}
\]

### Theorem 4.1 (finite moving-plateau bound)

Every universal literal word for \(Q\) has length

\[
\boxed{
n\ge B+\left\lceil\frac{HB}{2s}\right\rceil
\ge B\left(1+\frac{H}{2s}\right).}
\tag{4.3}
\]

The selected witnesses may cross arbitrary seams; no localization or
canonical interval choice is assumed.

#### Proof

The fourth coordinate in (4.2) lies in \([0,s]\), and \(a+L>0\)
ensures that every selected target is nonzero.  Each \(j\)-layer has
constant rank \(a+L+j\) and cardinality \(B\).

Choose one actual witness for each target.  In one endpoint orientation,
restrict its endpoint classes to these targets and write their number as

\[
C=B+\delta.
\]

If \(A_j\) is the set of classes meeting layer \(j\), then
\(|A_j|=B\), and hence

\[
|A_j\cap A_{j+1}|\ge B-\delta.
\tag{4.4}
\]

Two comparable targets in adjacent ranks form a cover.  Summing (4.4),
the partition uses at least \(H(B-\delta)\) selected covers.

Let

\[
\phi(x)=|x|-a,
\qquad0\le\phi\le L.
\]

A cover in one of the first three coordinates raises \(\phi\) by one;
a fourth-coordinate cover leaves it fixed.  Along every endpoint class
\(\phi\) is nondecreasing.  The bottom and top layers have the same
\(\phi\)-multiset.  If
\[
\Phi=\sum_K\bigl(\phi(\max K)-\phi(\min K)\bigr),
\]
then cancellation gives the exact telescoping identity

\[
\Phi
=\sum_{K\text{ misses top}}\phi(\max K)
-\sum_{K\text{ misses bottom}}\phi(\min K)
\le L\delta
\tag{4.5}
\]

for the total available transverse increase.  Thus at most \(L\delta\)
of the covers counted in (4.4) are transverse.  The number \(v\) of
used vertical covers satisfies

\[
v\ge H(B-\delta)-L\delta
=HB-s\delta.
\tag{4.6}
\]

Apply (4.6) to the left and right endpoint partitions.  They cannot both
use one vertical target cover, because its two targets would then have
the same left and right endpoints, hence the same witnessing interval
and the same maximum.  There are exactly \(HB\) vertical covers.  Hence

\[
s(\delta_L+\delta_R)\ge HB.
\tag{4.7}
\]

Each restricted endpoint class occupies a physical endpoint position, so

\[
B+\delta_L\le n,
\qquad
B+\delta_R\le n.
\]

Therefore \(2s(n-B)\ge HB\).  Integrality of \(n-B\) gives (4.3).
\(\square\)

---

## 5. Sharp optimization of every moving plateau

For \(0\le\lambda\le3\), define

\[
b(\lambda)=
\begin{cases}
\dfrac{3\lambda}{4}-\dfrac{\lambda^3}{12},
&0\le\lambda\le1,\\[2mm]
1-\dfrac{(3-\lambda)^3}{24},
&1\le\lambda\le3.
\end{cases}
\tag{5.1}
\]

### Lemma 5.1 (maximal three-cube slab mass)

Among intervals of length \(\lambda\) in \([0,3]\), the largest volume
of

\[
\{x\in[0,1]^3:|x|\text{ lies in the interval}\}
\]

is \(b(\lambda)\).  Consequently, for fixed \(d\in[0,3]\),

\[
w([0,t]^3\times[0,dt+O(1)])
=(b(d)+o(1))t^3,
\tag{5.2}
\]

and a moving plateau with \(s/t\to d\), \(H/t\to\alpha\), has

\[
B\le(b(d-\alpha)+o(1))t^3.
\tag{5.3}
\]

#### Proof

The density of the sum of three independent uniform \([0,1]\) variables
is symmetric about \(3/2\) and increases up to \(3/2\).  Sliding an
interval toward \(3/2\) cannot decrease its mass, so a centred interval
is optimal.

For \(0\le\lambda\le1\), direct integration over the centred interval
gives

\[
b(\lambda)=\frac{3\lambda}{4}-\frac{\lambda^3}{12}.
\]

For \(1\le\lambda\le3\), the two omitted tails each have length
\((3-\lambda)/2\le1\).  A lower tail of length \(u\le1\) has volume
\(u^3/6\), so

\[
b(\lambda)
=1-2\frac{((3-\lambda)/2)^3}{6}
=1-\frac{(3-\lambda)^3}{24}.
\]

A rank of \([0,t]^3\times[0,s]\) counts triple lattice points whose sum
lies in an interval of length \(s\).  After scaling by \(t^{-1}\), only
\(O(t^2)\) lattice cells meet the finitely many planar slab boundaries.
Thus the lattice count is its volume times \(t^3+O(t^2)\), uniformly for
fixed \(d\).  Maximizing proves (5.2), and using slab length \(s-H\)
proves (5.3). \(\square\)

### Theorem 5.2 (sharp collapse on the survivor interval)

Let \(\delta_*,d_*\) be as in (0.5).  For

\[
1\le d\le d_*,
\qquad
0\le\alpha\le d,
\]

one has

\[
\boxed{
b(d-\alpha)\left(1+\frac{\alpha}{2d}\right)\le b(d),}
\tag{5.4}
\]

strictly when \(\alpha>0\).  Thus Theorem 4.1 cannot exceed the width
leading term anywhere in this interval.

At \(d=1\),

\[
\boxed{
\frac23-b(1-\alpha)\left(1+\frac\alpha2\right)
=\frac\alpha6+\frac{\alpha^2}{2}
+\frac{\alpha^3(1-\alpha)}{24}>0}
\tag{5.5}
\]

for \(0<\alpha\le1\).

For \(d_*<d<3\), every sufficiently small fixed \(\alpha>0\) reverses
(5.4).

#### Proof

Put

\[
\lambda=d-\alpha,
\qquad
G_d(\lambda)=(3d-\lambda)b(\lambda).
\tag{5.6}
\]

Since

\[
1+\frac{\alpha}{2d}=\frac{3d-\lambda}{2d},
\]

(5.4) is exactly

\[
G_d(\lambda)\le G_d(d).
\tag{5.7}
\]

For \(0\le\lambda\le1\),

\[
12G_d'(\lambda)
=27d-9d\lambda^2-18\lambda+4\lambda^3.
\tag{5.8}
\]

For \(d\ge1\), this is bounded below by its value at \(d=1\).  That
cubic decreases on \([0,1]\) and equals \(4\) at \(\lambda=1\), so
(5.8) is positive.

For \(1\le\lambda\le d\), put \(z=3-\lambda\).  Then

\[
24G_d'(\lambda)
=9(d-1)z^2+4z^3-24.
\tag{5.9}
\]

The right side increases with \(z\).  Since \(z\ge3-d\), it is bounded
below by its value at \(z=3-d\), namely

\[
-\bigl(5(3-d)^3-18(3-d)^2+24\bigr).
\tag{5.10}
\]

The polynomial

\[
p(z)=5z^3-18z^2+24
\]

has \(p(3/2)=3/8\), \(p(2)=-8\), and

\[
p'(z)=3z(5z-12)<0
\qquad(0<z<2).
\]

It therefore has the unique root \(\delta_*\in(3/2,2)\).  If
\(1\le d\le3-\delta_*\), expression (5.10) is nonnegative.  Hence
\(G_d\) increases on \([0,d]\), strictly on every proper subinterval
ending at \(d\), proving (5.4).

At \(d=1\),

\[
b(1-\alpha)
=\frac23-\frac\alpha2-\frac{\alpha^2}{4}
+\frac{\alpha^3}{12}.
\]

Multiplication by \(1+\alpha/2\) gives (5.5).

If \(d>d_*\), then \(G_d'(d)<0\), so for all sufficiently small fixed
\(\alpha>0\),

\[
G_d(d-\alpha)>G_d(d).
\]

This reverses (5.4). \(\square\)

The cubic gap assertion concerns fixed macroscopic \(\alpha>0\).  It is
not a uniform cubic gap for \(H=o(t)\).

---

## 6. Exact remaining lemmas and audit

### 6.1 Positive route

The smallest sufficient statement within the complementary-shell route is
still the following.

> **Checkerboard PACK lemma — UNPROVED.**  For every \(r\), construct one
> word \(Z^{(r)}\) of nonzero ambient points of \([0,r]^4\), of length
> \[
> (r+1)^2+r^2+e_r,
> \qquad e_r=o(r^2),
> \]
> such that, for every nonzero \((a,b,c)\in\Lambda_r\), there are physical
> indices \(i(a,b,c)\le j(a,b,c)\) with
> \[
> \bigvee_{q=i(a,b,c)}^{j(a,b,c)}Z_q^{(r)}
> =\Phi_r(a,b,c).
> \]

This requires one literal word for
\(\mathcal A_r\cup\mathcal B_r\).  Separate factors, separate reset
budgets, fractional endpoint assignments, or an unextendible almost-word
do not satisfy it.  Corollary 1.2 proves that it implies (0.2).

Theorem 2.1 adds an unavoidable architectural feature: if the aligned
middle row is used, it must interleave radii to create same-parity
\(\mathcal A_r\) corridors and simultaneously create the parity-reversed
\(\mathcal B_r\) corridors at common physical positions.

### 6.2 Negative route

Lemma 3.1 isolates the smallest endpoint-only replacement exposed here.
Let

\[
M=(Q_t)_{2t},
\qquad
B=(Q_t)_{2t+k},
\qquad
k=\Theta(t).
\]

In the comparability graph \(H(M,B)\), consider two edge-disjoint
matchings, coloured \(L,R\), whose union is acyclic.

> **Macroscopic alternating-factor deficiency — UNPROVED.**  There are
> fixed \(\theta,\eta>0\) such that, for
> \(k=\lfloor\theta t\rfloor\) and every \(D\le\eta t^3\), no such pair
> of matchings leaves at most \(D\) vertices of \(B\) unmatched in each
> colour.

Indeed, a word of length \(W_t+D\) would give \(W_t\) distinct
middle-anchored classes in each endpoint partition.  At most \(D\)
shoulder targets could be unanchored in either orientation.  The actual
same-endpoint pairings would be the two matchings above, and Lemma 3.1
would make their union acyclic.  The unproved deficiency would therefore
imply a positive-density lower bound.

Theorem 3.3 shows why static components cannot replace this lemma.  What
is needed is a deficiency for two simultaneous near-saturating matchings
under the alternating-cycle prohibition, or a stronger coordinate-pin
obstruction.

### 6.3 Adversarial audit

1. **Literal ring witnesses.**  Theorem 2.1 first proves that no
   \(\mathcal B_r\) middle point lies below \(T\).  It then checks both
   cyclic arcs between the only possible \(a\)- and \(b\)-pins.  No
   abstract join is treated as a word interval.

2. **Cuts and orientations.**  Checking both cyclic arcs is stronger than
   checking a chosen linear cut.  Reversing a ring or the radial order,
   moving a cut, or repeating its endpoint cannot create a third arc.

3. **Parity.**  The step \(s\ge k+1\) uses
   \(k\not\equiv r\pmod2\).  Without it, \((-k,-k)\) lies on radius \(k\),
   and the proof does not apply.

4. **Density.**  The three fixed intervals in (2.13)--(2.14) contain
   \(r/20+O(1)\), \(r/4+O(1)\), and \(r/10+O(1)\) admissible choices.
   Thus (2.6) is cubic, not a boundary-size family.

5. **Architecture scope.**  Theorem 2.1 allows intact rings only.  An
   unrestricted word may interleave radii, repeat more points, or use
   non-middle letters.  Hence (2.6) is not an unrestricted
   \(\Omega(t^3)\) lower bound.

6. **Forest hypotheses.**  Lemma 3.1 requires disjoint antichains, one
   common chosen witness per target for both endpoint partitions, and the
   fixed orientation \(A<B\).  Components include isolated vertices.

7. **Static versus actual forest.**  The actual endpoint forest is a
   spanning subgraph of the static graph and may have more components.
   Theorem 3.3 excludes only a witness-independent static-component proof.

8. **Zero target.**  The condition \(a+L>0\) in Theorem 4.1 is essential.
   Without it, the selected bottom family can contain the forbidden zero
   target and the class count is false.

9. **Plateau seams.**  Theorem 4.1 selects arbitrary global witnesses and
   only then restricts their endpoint classes.  Witnesses may cross every
   external seam.  The sole exclusivity input is that the same vertical
   target cover cannot occur in both endpoint partitions.

10. **Plateau range.**  The optimization is stated for \(0\le d\le3\),
    exactly the domain in which a length-\(d\) interval fits in the
    three-cube sum range.  The survivor theorem only uses
    \(1\le d\le d_*<3\).

11. **Threshold endpoint.**  At \(d=d_*\), \(G_d'(d)=0\), but \(G_d\) is
    strictly increasing before \(d\).  Every fixed positive plateau height
    remains strictly subcritical.  The sign statement for \(d>d_*\) is
    explicitly one-sided.

12. **Independent audit.**  An independent proof audit verified the
    ring interval calculation, the alternating-forest constant, the
    normalized-matching use, the exact ceiling in (4.3), and both
    derivatives (5.8)--(5.9).  It caught and corrected the disjointness,
    common-witness, zero-target, integrality, and fixed-\(\alpha\) scopes
    recorded above.

The final status is:

> Intact alternating square-ring fusion fails on a positive-density
> literal shoulder family, while every static two-layer component dual and
> every single moving-plateau dual collapses at equality.  The remaining
> constructive task is a genuinely cross-radius, two-colour literal packet
> braid; the remaining endpoint-only negative task is a simultaneous
> alternating-matching deficiency, not another one-plateau count.
