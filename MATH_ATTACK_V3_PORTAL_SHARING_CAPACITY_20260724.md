# Third-wave lane V: portal sharing capacity across product boxes

Date: 2026-07-24

## 0. Outcome

This report proves an unconditional endpoint-capacity theorem for the
three-block symmetric-chain product decomposition.  It addresses exactly the
case in which a witness interval is allowed to cross arbitrary concatenation
seams.

The decisive fact is elementary but rigid:

\[
 \boxed{\text{targets with one fixed oriented endpoint form an inclusion
 chain.}}
\]

Consequently, if the selected targets occupy \(q\) common global ranks, one
physical left endpoint or one physical right endpoint can serve at most \(q\)
different product boxes.  This conclusion is independent of how many seams
the intervals cross and of which foreign letters occur inside them.

For three equal Boolean blocks of even size \(s\), put

\[
 W_s=\binom{s}{s/2},\qquad
 W=\binom{3s}{3s/2}.
\]

There are \(W_s^3\) product boxes and their widths sum exactly to \(W\).  If a
universal word has length \(n=W+d\), a common \(h+1\)-rank central subband of
the dominant product boxes gives an exact portal bound

\[
 \boxed{
 P_h\ge
 \left\lceil\frac{(Q_s(h)-2d)_+}{2h}\right\rceil .}
 \tag{0.1}
\]

Here \(P_h\) is the number of physical positions used as a same-orientation
endpoint by at least two selected boxes, and

\[
 Q_s(h)=
 \sum_{\substack{\text{product boxes with a unique long side }r\\
                  r\ge p+q+h}}
 \left\lceil\frac{(p+1)(q+1)h}{p+q+h}\right\rceil .
 \tag{0.2}
\]

Every oriented endpoint in this certificate serves at most \(h+1\) boxes.
The factor (2) in (0.1) is necessary because one physical position may be a
left-sharing and a right-sharing portal simultaneously.

If \(d=o(W)\), choose \(h=o(\sqrt s)\) adaptively as in Section 7.  Then

\[
 \boxed{
 P_h\ge
 \left[
 \frac{9\sqrt\pi}{16}
 \left(\log 3-\frac{28}{27}\right)-o(1)
 \right]W_s^3\sqrt s.}
 \tag{0.3}
\]

Equivalently, \(P_h=\Omega(W/\sqrt s)\), even though each relevant oriented
endpoint serves only \(o(\sqrt s)\) selected boxes.  If all shared physical
endpoints are covered by at most \(u_s\) designated positions per product
box, then

\[
 \boxed{
 \liminf_{s\to\infty}\frac{u_s}{\sqrt s}
 \ge
 \frac{9\sqrt\pi}{16}
 \left(\log 3-\frac{28}{27}\right)>0.}
 \tag{0.4}
\]

There is a distinct, stronger conclusion for a per-served-box membership
budget.  If every box has its own set of positions at which that box may
participate in endpoint sharing, then the full plateaux force

\[
 \boxed{u_s\ge(2/15-o(1))s.}
 \tag{0.5}
\]

Thus two portal notions must not be conflated:

* a union budget for distinct physical portal positions has the intrinsic
  lower scale \(\sqrt s\) per product box;
* a membership budget charging every box which a portal serves has the
  surface-scale lower bound \(s\) per dominant box.

Finally, an explicit seam-crossing construction shows that the \(O(h)\)
degree cap is sharp in order using only rank, product-box, and seam
information.  Any stronger cap needs extra chronology, locality, or
contamination hypotheses.

No finite search, computational experiment, or external source is used.
Every statement below is integral inside the fixed product decomposition and
concerns literal OR witnesses in one word.

## 1. Product boxes and selected witnesses

Split \(3s\) Boolean coordinates into three disjoint blocks

\[
 X_1\sqcup X_2\sqcup X_3,
 \qquad |X_i|=s,
\]

where \(s\) is even.  Fix an arbitrary saturated symmetric-chain
decomposition in each \(2^{X_i}\).  A factor chain of edge height \(p\) is

\[
 C_0\subset C_1\subset\cdots\subset C_p,
\]

and its bottom and top ranks are \((s-p)/2\) and \((s+p)/2\).  Hence every
factor-chain height is even.

A triple of factor chains gives a product box

\[
 \mathcal B=[0,p]\times[0,q]\times[0,r]
\]

embedded literally in \(2^{X_1\sqcup X_2\sqcup X_3}\).  The product boxes
partition the Boolean lattice.  Write \(w_{\mathcal B}\) for the width of the
box.  Its local middle layer is the global rank-\(3s/2\) layer, and therefore

\[
 \boxed{\sum_{\mathcal B}w_{\mathcal B}=W.}
 \tag{1.1}
\]

Indeed, each product box contributes exactly its width to the global middle
layer, and the boxes partition that layer.  The number of product boxes is

\[
 \mathscr B_s=W_s^3.
 \tag{1.2}
\]

Let

\[
 A=(A_1,\ldots,A_n),\qquad A_j\subseteq X_1\sqcup X_2\sqcup X_3,
\]

be a universal contiguous-OR word.  For every selected target \(T\), fix an
arbitrary witnessing interval

\[
 I_T=[a_T,b_T],\qquad \bigcup_{j=a_T}^{b_T}A_j=T.
 \tag{1.3}
\]

No condition is placed on which seams \(I_T\) crosses.  Since the product
boxes partition the Boolean lattice, selected target families belonging to
different boxes are disjoint.

For a selected family \(\mathcal T_{\mathcal B}\) in a box, define

\[
 L_{\mathcal B}=\{a_T:T\in\mathcal T_{\mathcal B}\},\qquad
 R_{\mathcal B}=\{b_T:T\in\mathcal T_{\mathcal B}\},
 \tag{1.4}
\]

and put

\[
 C_L(\mathcal B)=|L_{\mathcal B}|,
 \qquad C_R(\mathcal B)=|R_{\mathcal B}|.
 \tag{1.5}
\]

At a physical position \(j\), let

\[
 \ell_j=\#\{\mathcal B:j\in L_{\mathcal B}\},\qquad
 r_j=\#\{\mathcal B:j\in R_{\mathcal B}\}.
 \tag{1.6}
\]

These are endpoint--box incidence degrees, not letter-projection degrees.

## 2. The seam-invariant endpoint rank theorem

### Theorem 2.1 -- endpoint rank injection

Let the selected targets of each box \(B\) have global ranks in a set \(Q_B\).
Fix a physical position \(j\) and one endpoint orientation, left or right.
Then the boxes served at that oriented endpoint admit an injection

\[
 B\longmapsto q_B\in Q_B.
 \tag{2.1}
\]

In particular, if every \(Q_B\subseteq Q\), then

\[
 \boxed{\ell_j\le |Q|,\qquad r_j\le |Q|.}
 \tag{2.2}
\]

Thus one physical position serves at most \(2|Q|\) oriented box roles when
left and right roles are combined.

#### Proof

Consider all selected targets whose witnessing intervals begin at \(j\).  If
their right endpoints satisfy \(b\le b'\), then

\[
 \bigcup_{i=j}^{b}A_i\subseteq\bigcup_{i=j}^{b'}A_i.
\]

Hence their target unions form an inclusion chain.  Targets attributed to
different boxes are distinct, and a chain of distinct sets contains at most
one set of each cardinality.  Choose one target for every box served at \(j\);
their ranks are distinct and give (2.1).  The right-endpoint proof is the
same, ordering the intervals \([a,j]\) by their left endpoints.  No step uses
the number or location of crossed seams.  \(\square\)

### Corollary 2.2 -- Hall and multiscale forms

For every subfamily \(\mathcal S\) of boxes served at one oriented endpoint,

\[
 \boxed{|\mathcal S|\le\left|\bigcup_{B\in\mathcal S}Q_B\right|.}
 \tag{2.3}
\]

Thus the chosen target ranks form a system of distinct representatives for
the allowed rank sets.  If the allowed sets are centered intervals

\[
 Q_B=[M-a_B,M+a_B]\cap\mathbb Z,
\]

then, for every integer \(t\ge0\),

\[
 \boxed{
 \#\{B\text{ served at the endpoint}:a_B\le t\}\le2t+1.}
 \tag{2.4}
\]

For these nested rank intervals, (2.4) is exactly Hall's rank-support
condition.  It is not asserted to be sufficient for the existence of the
required OR intervals; it is the complete restriction obtainable from the
rank supports alone.

### Corollary 2.3 -- opposite-endpoint or exit capacity

Suppose an architecture permits intervals beginning at \(j\) to end only in
a set \(E_j^+\), and intervals ending at \(j\) to begin only in a set \(E_j^-\).
Then

\[
 \ell_j\le\min\{|Q|,|E_j^+|\},\qquad
 r_j\le\min\{|Q|,|E_j^-|\}.
 \tag{2.5}
\]

Indeed, two distinct targets with the same left endpoint cannot have the same
right endpoint, and conversely.  Consequently a shared left slot has surplus
capacity at most

\[
 \min\{|Q|-1,|E_j^+|-1\},
 \tag{2.6}
\]

with the symmetric statement on the right.  Crossing many seams creates no
extra endpoint capacity unless it also creates many allowable opposite
endpoints.

## 3. Exact abstract portal accounting

Put

\[
 I_L=\sum_B C_L(B)=\sum_{j=1}^n\ell_j,
 \qquad
 I_R=\sum_B C_R(B)=\sum_{j=1}^n r_j.
 \tag{3.1}
\]

Let

\[
 P_L=\#\{j:\ell_j\ge2\},\quad
 P_R=\#\{j:r_j\ge2\},\quad
 P=\#\{j:\ell_j\ge2\text{ or }r_j\ge2\}.
 \tag{3.2}
\]

### Theorem 3.1 -- portal positions from endpoint demand

Assume all selected targets lie in a common rank set \(Q\), with
\(q=|Q|\ge2\).  Then

\[
 \boxed{
 P_L\ge\left\lceil\frac{(I_L-n)_+}{q-1}\right\rceil,
 \qquad
 P_R\ge\left\lceil\frac{(I_R-n)_+}{q-1}\right\rceil.}
 \tag{3.3}
\]

Consequently,

\[
 \boxed{
 P\ge
 \max\left\{
 \left\lceil\frac{(I_L-n)_+}{q-1}\right\rceil,
 \left\lceil\frac{(I_R-n)_+}{q-1}\right\rceil
 \right\},}
 \tag{3.4}
\]

and, when only \(I_L+I_R\) is known,

\[
 \boxed{
 P\ge
 \left\lceil
 \frac{(I_L+I_R-2n)_+}{2(q-1)}
 \right\rceil.}
 \tag{3.5}
\]

If \(q=1\), no same-orientation sharing is possible and feasibility requires
\(I_L,I_R\le n\).

#### Proof

By Theorem 2.1,

\[
 I_L=\sum_j\ell_j
 \le(n-P_L)+qP_L=n+(q-1)P_L,
\]

which proves the left inequality in (3.3); the right inequality is
symmetric.  At a nonportal physical position, \(\ell_j+r_j\le2\), while at a
portal it is at most \(2q\).  Therefore

\[
 I_L+I_R\le2(n-P)+2qP=2n+2(q-1)P,
\]

which gives (3.5).  \(\square\)

### Corollary 3.2 -- width baseline and local excess

Suppose each box has a baseline \(w_B\), with

\[
 W_0=\sum_Bw_B,
\]

and the selected targets force

\[
 C_L(B)\ge w_B,\qquad C_R(B)\ge w_B,
 \tag{3.6}
\]

and

\[
 C_L(B)+C_R(B)\ge2w_B+\gamma_B,
 \qquad \gamma_B\in\mathbb Z_{\ge0}.
 \tag{3.7}
\]

Put \(\Gamma=\sum_B\gamma_B\) and \(n=W_0+d\).  Then

\[
 \boxed{
 P\ge
 \left\lceil\frac{(\Gamma-2d)_+}{2(q-1)}\right\rceil.}
 \tag{3.8}
\]

The subtraction \(2d\) and the factor (2) are both essential when only
combined left-plus-right demand is controlled.  Each surplus word position
can absorb one unshared left incidence and one unshared right incidence.

## 4. Local plateau-subband excess

Consider a grid box

\[
 \mathcal P=[0,p]\times[0,q]\times[0,r],
 \qquad r\ge p+q.
\]

Its plateau layers are the local ranks \(p+q,p+q+1,\ldots,r\), each of size

\[
 w=(p+1)(q+1).
 \tag{4.1}
\]

### Lemma 4.1 -- exact \(h\)-band endpoint excess

Choose any \(h+1\) consecutive plateau layers, where

\[
 1\le h\le r-p-q.
\]

Choose arbitrary ambient-word witnesses for all targets in these layers, and
let \(C_L,C_R\) be their distinct left- and right-endpoint counts.  Then

\[
 \boxed{
 C_L+C_R\ge
 2w+\left\lceil\frac{wh}{p+q+h}\right\rceil.}
 \tag{4.2}
\]

The witnesses may cross arbitrarily many seams.

#### Proof

Group targets by common left endpoint.  Each group is an inclusion chain.
Every selected layer is an antichain of size \(w\), so the number of left
chains is \(C_L=w+\delta_L\), where \(\delta_L\ge0\).

For each pair of adjacent selected layers, the two sets of occupied left
chains both have size \(w\) inside a universe of \(w+\delta_L\) chains.  At
least \(w-\delta_L\) chains meet both layers.  The two targets in each such
chain differ in rank by one and hence form a genuine grid cover.  Across the
\(h\) adjacent layer pairs, the left partition therefore contains at least

\[
 h(w-\delta_L)
 \tag{4.3}
\]

grid covers.

Put \(\phi(x,y,z)=x+y\), so \(0\le\phi\le p+q\).  The bottom and top selected
layers have identical \(\phi\)-multisets.  Exactly \(w\) left chains meet
each boundary layer; the remaining \(\delta_L\) chains start internally and
the remaining \(\delta_L\) chains end internally.  Telescoping \(\phi\) from
the first to the last target of every chain cancels the two boundary
multisets.  The internal ends contribute at most
\((p+q)\delta_L\), and the internal starts contribute nonnegatively.
Therefore the number of horizontal covers counted in (4.3) is at most

\[
 (p+q)\delta_L.
 \tag{4.4}
\]

It follows that the left partition contains at least

\[
 wh-(p+q+h)\delta_L
 \tag{4.5}
\]

vertical covers.  The right partition analogously contains at least

\[
 wh-(p+q+h)\delta_R,
 \qquad C_R=w+\delta_R.
 \tag{4.6}
\]

The endpoint partitions are orthogonal.  If two distinct targets belonged
to one common left group and one common right group, their chosen intervals
would have the same two endpoints and hence the same OR, a contradiction.
Thus no vertical cover can occur in both endpoint partitions.  The selected
slab has exactly \(wh\) vertical covers, so (4.5)--(4.6) imply

\[
 2wh-(p+q+h)(\delta_L+\delta_R)\le wh.
\]

Hence

\[
 \delta_L+\delta_R\ge\frac{wh}{p+q+h}.
\]

The left side is integral, proving (4.2).  Notice that only target unions and
their physical endpoints entered the proof.  \(\square\)

For \(h=r-p-q\), the denominator is \(r\), giving the full-plateau form

\[
 C_L+C_R-2w\ge
 \left\lceil\frac{w(r-p-q)}r\right\rceil.
 \tag{4.7}
\]

## 5. The exact three-block portal theorem

Let

\[
 M=3s/2.
\]

For an integer \(h\ge1\), use the common global rank band

\[
 Q_h=
 \{M-\lfloor h/2\rfloor,\ldots,M+\lceil h/2\rceil\},
 \qquad |Q_h|=h+1.
 \tag{5.1}
\]

Call a product box \(h\)-dominant if one of its three heights, denoted \(r\),
satisfies

\[
 r\ge p+q+h,
 \tag{5.2}
\]

where \(p,q\) are the other two heights.  The long coordinate is unique.
The bottom global rank of this box is

\[
 M-\frac{p+q+r}{2}.
\]

Its full plateau maps to the global ranks

\[
 M-\frac{r-p-q}{2},\ldots,
 M+\frac{r-p-q}{2}.
 \tag{5.3}
\]

Because all heights are even, (5.2) ensures that this plateau contains
\(Q_h\).

For every \(h\)-dominant box select all targets in \(Q_h\).  For every other
box select only its global-middle layer.  Define

\[
 Q_s(h)=
 \sum_{\mathcal B\ h\text{-dominant}}
 \left\lceil
 \frac{(p_{\mathcal B}+1)(q_{\mathcal B}+1)h}
 {p_{\mathcal B}+q_{\mathcal B}+h}
 \right\rceil.
 \tag{5.4}
\]

All selected targets lie in the common band \(Q_h\).

### Theorem 5.1 -- exact physical portal lower bound

Let \(A\) be any universal word of length

\[
 n=W+d.
\]

For every choice of witnesses for the selected targets, let \(P_h\) be the
number of physical positions \(j\) for which \(\ell_j\ge2\) or \(r_j\ge2\).
Then

\[
 \boxed{
 P_h\ge
 \left\lceil\frac{(Q_s(h)-2d)_+}{2h}\right\rceil.}
 \tag{5.5}
\]

Moreover,

\[
 \boxed{\ell_j,r_j\le h+1\quad\text{for every }j.}
 \tag{5.6}
\]

#### Proof

The selected middle layer of any box is an antichain of size
\(w_{\mathcal B}\).  Thus either endpoint partition needs at least
\(w_{\mathcal B}\) chains.  Lemma 4.1 supplies the additional summand in
(5.4) for every \(h\)-dominant box.  Using (1.1),

\[
 \sum_{\mathcal B}
 \bigl(C_L(\mathcal B)+C_R(\mathcal B)\bigr)
 \ge2W+Q_s(h).
 \tag{5.7}
\]

All selected targets lie in \(h+1\) global ranks, so Theorem 2.1 gives
(5.6).  Apply Corollary 3.2 with \(q=h+1\), \(\Gamma=Q_s(h)\), and
\(n=W+d\).  This gives (5.5).  \(\square\)

### Theorem 5.2 -- charged endpoint--box graph

There is a set of at least

\[
 \boxed{(Q_s(h)-2d)_+}
 \tag{5.8}
\]

charged oriented endpoint--box incidences with the following properties:

1. every charged incidence belongs to an \(h\)-dominant box;
2. every charged incidence is at a same-orientation shared endpoint;
3. an oriented endpoint has at most \(h\) charged incidences;
4. a physical position has at most \(2h\) charged incidences.

#### Proof

Form the bipartite incidence graph between product boxes and oriented physical
slots \((L,j)\), \((R,j)\).  Equation (5.7) says that it has at least
\(2W+Q_s(h)\) edges.  At any fixed oriented slot, at most one nondominant box
can occur: every nondominant selected target has the single global rank \(M\),
while targets sharing an oriented endpoint form a strict chain.

At every nonempty oriented slot delete one edge, choosing its nondominant
edge if one exists.  There are at most \(2n\) nonempty oriented slots, so at
least \(Q_s(h)-2d\) edges remain when this quantity is positive.  All remaining
edges belong to dominant boxes, and every remaining slot was originally
incident to at least two boxes.  Its original degree was at most \(h+1\), so
its remaining degree is at most \(h\).  Combining the two orientations gives
the physical-position cap \(2h\).  \(\square\)

This charged form localizes the excess to the boxes which generated it; it is
stronger than merely knowing the scalar sharing sum.

## 6. SCD height law and the exact asymptotic constant

Let \(a_s(t)\) be the number of height-\(t\) chains in an SCD of \(2^{[s]}\).
For \(t\equiv s\pmod2\),

\[
 a_s(t)=
 \binom{s}{(s-t)/2}-
 \binom{s}{(s-t)/2-1},
 \tag{6.1}
\]

and \(a_s(t)=0\) otherwise.  This distribution is independent of the chosen
SCD, and

\[
 \sum_ta_s(t)=W_s.
\]

### Lemma 6.1 -- Rayleigh height limit

If a chain is chosen uniformly among the \(W_s\) chains and \(H_s\) is its
height, then

\[
 \frac{H_s}{\sqrt s}\Longrightarrow X,
 \qquad f_X(x)=xe^{-x^2/2}\quad(x>0).
 \tag{6.2}
\]

All fixed moments are uniformly bounded and converge.

#### Proof

Telescoping (6.1) gives, with the parity adjustment implicit,

\[
 \mathbb P(H_s\ge t)
 =\frac{\binom{s}{(s-t)/2}}{\binom{s}{s/2}}.
 \tag{6.3}
\]

For \(t/\sqrt s\to x\), the central-binomial ratio tends to
\(e^{-x^2/2}\), the Rayleigh tail.  For \(s=2m\) and \(t=2u\), the exact product

\[
 \begin{aligned}
 \frac{\binom{2m}{m-u}}{\binom{2m}{m}}
 &=\prod_{i=0}^{u-1}\frac{m-i}{m+i+1}\\
 &\le
 \exp\left(-\sum_{i=0}^{u-1}
 \frac{2i+1}{m+i+1}\right)
 \le \exp\left(-\frac{u^2}{m+u}\right)
 \le \exp\left(-\frac{t^2}{4s}\right).
 \end{aligned}
 \tag{6.4}
\]

Here \(\log(1-y)\le-y\), \(\sum_{i<u}(2i+1)=u^2\), and
\(m+u\le2m=s\).  This Gaussian tail gives uniform integrability of every
fixed power and completes the proof.  \(\square\)

### Theorem 6.2 -- asymptotics of the truncated plateau demand

Let \(h=h_s\ge1\) satisfy

\[
 \frac h{\sqrt s}\longrightarrow0.
 \tag{6.5}
\]

Then

\[
 \boxed{
 \frac{Q_s(h)}{h\sqrt s\,W_s^3}\longrightarrow3J,}
 \tag{6.6}
\]

where, for independent standard Rayleigh variables \(X,Y,Z\),

\[
 \begin{aligned}
 J
 &=\mathbb E\left[
 \frac{XY}{X+Y}\mathbf1_{\{Z>X+Y\}}
 \right]\\
 &=\frac{3\sqrt\pi}{8}
 \left(\log3-\frac{28}{27}\right)>0.
 \end{aligned}
 \tag{6.7}
\]

#### Proof

Choose a product box uniformly among the \(W_s^3\) chain triples.  Its three
heights are independent copies \(P,Q,R\) of \(H_s\).  The three possible
long-coordinate events are disjoint, and symmetry gives

\[
 \frac{Q_s(h)}{h\sqrt s\,W_s^3}
 =3\,\mathbb E\left[
 \mathbf1_{\{R\ge P+Q+h\}}
 \frac1{h\sqrt s}
 \left\lceil\frac{(P+1)(Q+1)h}{P+Q+h}\right\rceil
 \right].
 \tag{6.8}
\]

The ceiling error is at most \(1/(h\sqrt s)=o(1)\).  By Lemma 6.1 and
(6.5), the remaining integrand converges away from the null boundary
\(Z=X+Y\) to

\[
 \frac{XY}{X+Y}\mathbf1_{\{Z>X+Y\}}.
\]

Uniform integrability follows from

\[
 \frac{(P+1)(Q+1)}{\sqrt s(P+Q+h)}
 \le\frac{\min(P+1,Q+1)}{\sqrt s}
 \tag{6.9}
\]

and the uniform moment bound in Lemma 6.1.  This proves the first equality in
(6.7) and the limit (6.6).

It remains to evaluate \(J\).  Integrating the Rayleigh tail of \(Z\) gives

\[
 J=\int_0^\infty\int_0^\infty
 \frac{x^2y^2}{x+y}
 e^{-(x^2+y^2+xy)}\,dx\,dy.
 \tag{6.10}
\]

Set \(x=uv\), \(y=u(1-v)\), with \(u>0\), \(0<v<1\).  Since the Jacobian is
\(u\),

\[
 J=\frac{3\sqrt\pi}{8}
 \int_0^1
 \frac{v^2(1-v)^2}{(v^2-v+1)^{5/2}}\,dv.
 \tag{6.11}
\]

For completeness, put \(t=2v-1\) and then \(t=\sqrt3\tan\theta\).  The last
integral becomes

\[
 \frac{2}{9}\int_0^{\pi/6}
 \left(
 \cos^3\theta-6\sin^2\theta\cos\theta
 +9\frac{\sin^4\theta}{\cos\theta}
 \right)d\theta.
 \tag{6.12}
\]

Using

\[
 \frac{\sin^4\theta}{\cos\theta}
 =\sec\theta-2\cos\theta+\cos^3\theta,
\]

evaluation at \(\theta=\pi/6\) gives

\[
 \int_0^1
 \frac{v^2(1-v)^2}{(v^2-v+1)^{5/2}}\,dv
 =\log3-\frac{28}{27}.
 \tag{6.13}
\]

The original integral is strictly positive, so the displayed constant is
positive.  This proves (6.7).  \(\square\)

Finally, central-binomial asymptotics give

\[
 \boxed{
 \frac{sW_s^3}{W}\longrightarrow\frac{2\sqrt3}{\pi}.}
 \tag{6.14}
\]

## 7. Adaptive subbands force many low-degree portals

First note that every universal word has \(n\ge W\): the global middle-layer
targets form an antichain, while targets with a common right endpoint form a
chain.  Thus \(d=n-W\ge0\).

Assume now

\[
 d=o(W),\qquad \varepsilon_s=d/W.
\]

Choose

\[
 h_s=
 \max\left\{1,\left\lceil\sqrt s\,\sqrt{\varepsilon_s}\right\rceil\right\}.
 \tag{7.1}
\]

Then

\[
 \frac{h_s}{\sqrt s}\to0
 \tag{7.2}
\]

and, by (6.14),

\[
 \frac{d}{h_s\sqrt s\,W_s^3}\longrightarrow0.
 \tag{7.3}
\]

### Theorem 7.1 -- adaptive physical-portal theorem

For the band \(Q_{h_s}\), every selection of witnesses satisfies

\[
 \boxed{
 P_{h_s}\ge
 \left[
 \frac{9\sqrt\pi}{16}
 \left(\log3-\frac{28}{27}\right)-o(1)
 \right]W_s^3\sqrt s.}
 \tag{7.4}
\]

Every oriented endpoint in this certificate serves at most

\[
 h_s+1=o(\sqrt s)
 \tag{7.5}
\]

selected boxes.

#### Proof

Combine Theorem 5.1, Theorem 6.2, and (7.3):

\[
 \begin{aligned}
 P_{h_s}
 &\ge\frac{Q_s(h_s)-2d}{2h_s}\\
 &=\left(\frac{3J}{2}-o(1)\right)W_s^3\sqrt s.
 \end{aligned}
\]

Insert the value of \(J\) from (6.7).  Equation (7.5) is (5.6).  \(\square\)

Using (6.14), the equivalent width normalization is

\[
 \boxed{
 P_{h_s}\ge
 \left[
 \frac{9\sqrt3}{8\sqrt\pi}
 \left(\log3-\frac{28}{27}\right)-o(1)
 \right]\frac{W}{\sqrt s}.}
 \tag{7.6}
\]

### Corollary 7.2 -- union-of-physical-corridors lower bound

Suppose all physical positions counted by \(P_{h_s}\) lie in a union of
designated portal sets, one set of size at most \(u_s\) for each of the
\(W_s^3\) product boxes.  No ownership of a portal by the box whose set
contains it is assumed.  Then

\[
 P_{h_s}\le u_sW_s^3,
\]

and hence

\[
 \boxed{
 \liminf_{s\to\infty}\frac{u_s}{\sqrt s}
 \ge
 \frac{9\sqrt\pi}{16}
 \left(\log3-\frac{28}{27}\right).}
 \tag{7.7}
\]

Thus \(u_s=o(\sqrt s)\) is impossible.  This theorem does not exclude
\(u_s=\Theta(\sqrt s)\).

### Corollary 7.3 -- nonuniform exits

In the setting of Theorem 5.1, suppose a left portal \(j\) has only
\(e_j^+\) allowable right exits, and a right portal has only \(e_j^-\)
allowable left exits.  Then the exact endpoint demand obeys

\[
 \begin{aligned}
 Q_s(h)-2d
 \le{}&
 \sum_{j\in P_L}\min\{h,e_j^+-1\}_+\\
 &+\sum_{j\in P_R}\min\{h,e_j^--1\}_+.
 \end{aligned}
 \tag{7.8}
\]

This is the heterogeneous capacity form: a construction must pay through
rank span, through many exits, or through many endpoint positions.

## 8. Full plateaux and per-served-box membership

The physical-union budget in Corollary 7.2 differs from a budget which
charges a portal to every box it actually serves.  The latter has a stronger
lower bound.

Use the admissible even heights satisfying the real inequalities

\[
 \sqrt s\le p,q\le1.1\sqrt s,
 \qquad
 3\sqrt s\le r\le3.1\sqrt s.
 \tag{8.1}
\]

Take all three choices of the high coordinate.  Let \(\mathscr D_s\) be this
family of dominant boxes.  From (6.1)--(6.2),

\[
 |\mathscr D_s|
 =(3\kappa_L^2\kappa_H+o(1))W_s^3,
 \tag{8.2}
\]

where

\[
 \kappa_L=e^{-1/2}-e^{-121/200}>0,
 \qquad
 \kappa_H=e^{-9/2}-e^{-961/200}>0.
 \tag{8.3}
\]

For every such box, put

\[
 H_B=r-p-q,
 \qquad w_B=(p+1)(q+1).
\]

The defining windows give, for all sufficiently large \(s\),

\[
 \frac{H_B}{r}\ge\frac4{15},
 \qquad w_B\ge s,
 \qquad H_B\le1.1\sqrt s.
 \tag{8.4}
\]

Select the full plateau of every \(B\in\mathscr D_s\), and select only the
middle layer of every \(B\notin\mathscr D_s\).
Define

\[
 Q_s^*=
 \sum_{B\in\mathscr D_s}
 \left\lceil\frac{w_BH_B}{r_B}\right\rceil.
 \tag{8.5}
\]

Then

\[
 \boxed{Q_s^*\ge\frac4{15}s|\mathscr D_s|.}
 \tag{8.6}
\]

All selected ranks lie in a common interval of at most
\(1.1\sqrt s+1\) ranks.  Hence the full-plateau physical portal set satisfies

\[
 P^*\ge
 \left\lceil
 \frac{(Q_s^*-2d)_+}{2H_*}
 \right\rceil,
 \qquad
 H_*:=\max_{B\in\mathscr D_s}H_B\le1.1\sqrt s.
 \tag{8.7}
\]

This again gives \(P^*=\Omega(W/\sqrt s)\) for \(d=o(W)\).

Now assign to every box \(B\in\mathscr D_s\) a physical portal-membership set
\(\Pi_B\).  Assume that whenever \(B\) participates in same-orientation
endpoint sharing at \(j\), one has \(j\in\Pi_B\).  Apply the charged graph
argument of Theorem 5.2 to the full plateau.  It leaves at least
\(Q_s^*-2d\) charged incidences, all on boxes in \(\mathscr D_s\).  A physical position
can contribute at most two oriented incidences to a fixed box, so

\[
 Q_s^*-2d\le2\sum_{B\in\mathscr D_s}|\Pi_B|.
 \tag{8.8}
\]

### Theorem 8.1 -- per-served-box portal lower bound

If \(|\Pi_B|\le u_s\) for every \(B\in\mathscr D_s\) and \(d=o(W)\), then

\[
 \boxed{
 u_s\ge\frac{Q_s^*-2d}{2|\mathscr D_s|}
 \ge\left(\frac2{15}-o(1)\right)s.}
 \tag{8.9}
\]

#### Proof

The first inequality is (8.8).  Equations (8.2), (8.6), and (6.14) imply

\[
 \frac d{|\mathscr D_s|}=o(s),
\]

which gives the second inequality.  \(\square\)

If left and right memberships are budgeted as separate oriented slots, the
factor (2) in (8.8) disappears and the lower constant becomes \(4/15\).
Conversely, an \(\Omega(s)\) conclusion does not follow from a mere union of
unowned physical portal positions; Corollary 7.2 gives the correct intrinsic
conclusion in that model.

There is one useful intermediate case.  Suppose the full-plateau selection
also satisfies the explicit endpoint-degree hypothesis

\[
 \ell_j,r_j\le D_0
 \qquad(D_0\ge2)
\]

at every physical position.  Then each physical portal carries at most
\(2(D_0-1)\) units of sharing excess, so

\[
 P^*\ge\frac{Q_s^*-2d}{2(D_0-1)}.
 \tag{8.10}
\]

If \(d=o(W)\) and these physical portals are covered by \(u_sW_s^3\)
positions, (8.2) and (8.6) give

\[
 \boxed{
 u_s\ge
 \left(
 \frac{2\kappa_L^2\kappa_H}{5(D_0-1)}-o(1)
 \right)s.}
 \tag{8.11}
\]

Thus bounded selected endpoint degree also restores the surface-scale union
bound.  The degree hypothesis concerns endpoint--box incidences of the
selected witnesses; physical adjacency alone does not imply it, and it says
nothing about the potentially much larger projection degree of a letter.

## 9. Order-sharpness of the endpoint degree cap

The rank theorem gives an \(h+1\) per-orientation cap for an \(h+1\)-rank
band.  This order cannot be improved from SCD geometry and seam crossing
alone.

### Proposition 9.1 -- one portal serves \(\Theta(h)\) dominant boxes

Let \(h=h_s\to\infty\) be even, with \(h\le\sqrt s/2\), and use arbitrary
SCDs in the three \(s\)-blocks.  There are an integer
\(D\ge(\kappa_L+o(1))h\), a literal Boolean word segment, and a physical
position \(j\) such that

\[
 \ell_j,r_j\ge D,
 \tag{9.1}
\]

the incident selected targets lie in distinct dominant boxes and in one
common central \(h+1\)-rank band, and each of these \(2D\) incident witnesses
crosses exactly one of two adjacent concatenation seams.

#### Proof

In the first block, let \(\mathcal L_s\) be the SCD chains with heights in
\([\sqrt s,1.1\sqrt s]\).  By the Rayleigh height law,

\[
 \frac{|\mathcal L_s|}{W_s}\to\kappa_L.
 \tag{9.2}
\]

Choose a uniformly random maximal Boolean chain

\[
 F_0\subset F_1\subset\cdots\subset F_s
\]

and inspect \(h+1\) consecutive ranks centered at \(s/2\).  Every chain in
\(\mathcal L_s\) spans this band.  At an inspected rank \(u\), precisely one
set from each chain in \(\mathcal L_s\) occurs, so

\[
 \mathbb P(F_u\text{ lies in }\mathcal L_s)
 =\frac{|\mathcal L_s|}{\binom su}
 \ge\frac{|\mathcal L_s|}{W_s}.
\]

The expected number \(X\) of low-chain hits is therefore

\[
 \mathbb EX\ge(\kappa_L+o(1))h.
 \tag{9.3}
\]

Let \(Y\) count pairs of inspected ranks whose points lie in the same chain
of \(\mathcal L_s\).  For ranks \(u<v\), with gap \(a=v-u\), a random maximal
chain has a uniformly distributed comparable pair, and hence

\[
 \mathbb P(F_u,F_v\text{ lie in the same low SCD chain})
 =\frac{|\mathcal L_s|}
 {\binom su\binom{s-u}{a}}
 \le\frac1{\binom{s-u}{a}}.
 \tag{9.4}
\]

Throughout the central band, \(s-u\ge s/3\) for large \(s\).  The gap-one
terms in \(\mathbb EY\) total \(O(h/s)\).  For \(a\ge2\), since
\(a\le h\le\sqrt s/2\),

\[
 \binom{s-u}{a}\ge\binom{s-u}{2},
\]

so all remaining terms total \(O(h^2/s^2)\).  Thus \(\mathbb EY=o(1)\).
If \(D\) is the number of distinct low SCD chains hit, then

\[
 D\ge X-Y,
\]

because \(m-1\le\binom m2\) for every hit multiplicity \(m\).  Some maximal
chain therefore hits

\[
 D\ge(\kappa_L+o(1))h
 \tag{9.5}
\]

distinct low-window SCD chains, at nested points which we relabel

\[
 F_1\subset\cdots\subset F_D.
\]

In the second block choose two distinct low-window SCD chains and let \(U,U'\)
be their central members.  In the third block choose a chain of height in
\([3\sqrt s,3.1\sqrt s]\), with central member \(V\).  The targets

\[
 T_i^-=F_i\cup U\cup V,
 \qquad
 T_i^+=F_i\cup U'\cup V
 \tag{9.6}
\]

belong to \(2D\) distinct dominant product boxes.  Their offsets from global
rank \(3s/2\) are at most \(h/2\le\sqrt s/4\).  Every such dominant plateau
has half-gap at least

\[
 \frac{3\sqrt s-1.1\sqrt s-1.1\sqrt s}{2}=0.4\sqrt s,
\]

so all targets lie in the common plateau subband.

Put \(E_i=F_i\setminus F_{i-1}\) for \(i\ge2\).  Consider the literal word
segment

\[
 E_D,\ldots,E_2,F_1\cup U
 \ \Vert\ 
 V
 \ \Vert\ 
 F_1\cup U',E_2,\ldots,E_D.
 \tag{9.7}
\]

Every letter is nonempty.  For each \(i\), \(T_i^-\) is the union of a suffix
ending at \(V\), and \(T_i^+\) is the union of a prefix beginning at \(V\).
The former crosses exactly the left displayed seam and the latter exactly the
right displayed seam.  Thus the physical position occupied by \(V\) is a
right endpoint for \(D\) distinct boxes and a left endpoint for \(D\) other
distinct boxes.  Equation (9.1) follows from (9.5).  Appending any universal
word embeds this segment in a universal word without destroying the selected
witnesses.  \(\square\)

This is a sharpness example for endpoint capacity, not a near-width
construction and not a concatenation of independently box-confined local
words.

## 10. Implication scope and exact remaining geometry

The proved implications are architecture-level necessities:

\[
 \text{local plateau gaps}
 \Longrightarrow
 \text{endpoint--box incidence demand}
 \Longrightarrow
 \text{many portals or large portal capacity}.
\]

More precisely:

1. Arbitrary seam crossing does not invalidate the local endpoint dual.
   Every selected witness is still charged to its two physical endpoints.
2. One oriented endpoint serving targets in \(q\) global ranks serves at most
   \(q\) boxes.  This is the intrinsic, seam-independent capacity.
3. For a width-plus-\(o(W)\) word, adaptive subbands force
   \(\Omega(W/\sqrt s)\) distinct shared physical endpoints while keeping
   their selected-box degree \(o(\sqrt s)\).
4. A mere physical-union corridor budget must have length
   \(\Omega(\sqrt s)\) per product box.  It may still succeed at that scale.
5. A portal budget charged to every box actually served must have
   \(\Omega(s)\) positions per dominant box on average, and uniformly if all
   boxes have the same cap.
6. Bounded opposite-endpoint sets sharpen the rank cap through (2.5)--(2.6).
7. Proposition 9.1 shows that no \(o(h)\) degree bound follows from rank and
   seam geometry alone.

The report does **not** prove a coefficient-one OR word, a chronology for
combining boxwise words, or an impossibility theorem for globally braided
portals.  A construction with \(\Theta(W/\sqrt s)\) coherently coordinated
physical portals remains open.  Conversely, to strengthen this obstruction
one must prove additional geometry limiting opposite endpoints, controlling
letter contamination, or coupling portal use across time.  No labelled
common-owner synchronization statement is used or obtained.

There are no unproved lemmas in the endpoint-capacity and portal bounds above.
The only open issue is whether an actual global construction can realize the
remaining \(\Theta(W/\sqrt s)\)-portal escape route at near-width cost.
