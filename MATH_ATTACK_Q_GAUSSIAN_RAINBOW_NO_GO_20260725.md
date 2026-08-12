# Lane Q: the Gaussian strict-rainbow no-go

## Exact path concavity, splice capacity, cyclic pigeonholes, and the canonical balanced replacement

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, program,
solver, or long local computation was used.

## 0. Exact outcome

The endpoint-capped/reset-per-block two-sided-rainbow forest cannot be
extended to the band needed for coefficient one while retaining strict
global colour uniqueness. There are three independent exact obstructions.

1. For a spanning family of vertex-disjoint Johnson paths whose every
   depth-\(q\) window is correct-rank and whose lower and upper colours are
   globally injective through depth \(H=o(\sqrt m)\), the optimal
   endpoint-capped erosion excess is

   \[
   \left(\frac13+o(1)\right)\frac{WH^3}{m}.
   \]

   The constant \(1/3\) is exact. Thus the strict-rainbow erosion route has
   the sharp ceiling \(H=o(m^{1/3})\), far below every tail-compatible
   depth.

2. Arbitrary reordering and cross-component splicing do not remove the
   Gaussian obstruction. After a transition transversal hitting every
   nongeodesic or colour-overcapacity window is marked, a strict
   depth-\(H\) schedule on
   \(W-o(W)\) middle vertices has at least

   \[
   \frac{W-N_H-o(W)}H
   \]

   final blocks. At \(H=A\sqrt m\), every literalization paying \(H\) reset
   letters per block has excess at least

   \[
   (1-e^{-A^2}+o(1))W.
   \]

3. Closing the paths into cycles merely restores the seam windows and
   reinstates the colour-slot contradiction. A spanning cycle factor has
   \(W\) cyclic depth-\(q\) occurrences, while there are only
   \(N_q<W\) colours for every \(q\ge1\). Strict cyclic rainbowness is
   impossible already at depth one; at Gaussian depth its unavoidable
   collision mass is linear.

The particular Greene--Kleitman two-sided-rainbow forest also cannot be
rescued by repetitions: every linear or cyclic schedule must either repeat
middle vertices or rematch lower/upper colour pairs with total cost at
least

\[
\frac W4-\operatorname{Cat}_m
=\left(\frac14-o(1)\right)W.
\]

Consequently the advertised endpoint-capped strict-forest and strict
cycle-factor shortcuts are closed. A successful cycle theorem must permit
the arithmetically forced repetitions. Balanced floor/ceiling capacities
give the canonical minimum-spread replacement. For one exact wreath factor,
weighted overload against those capacities gives a literal contiguous-OR
word with all constants explicit. This is a stronger sufficient target;
small hole support can also occur with an unbalanced full-support profile.
Existence of a factor with sublinear weighted balanced overload is precisely
the remaining unlabelled MWB gate; it is not proved here.

This is a no-go for a construction lane, not a lower bound against
unrestricted contiguous-OR words and not a counterexample to the
constant-one conjecture.

## 1. Path windows and the exact boundary profile

Work first on a ground set of size \(2m\). Put

\[
W=\binom{2m}{m},
\qquad
N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\tag{1.1}
\]

Let \(\mathcal P\) be a family of \(p\) vertex-disjoint paths in
\(J(2m,m)\), where

\[
1\le H<m.
\tag{1.2}
\]

Write their positive vertex lengths as

\[
\ell_1,\ldots,\ell_p,
\qquad
v=\sum_{i=1}^p\ell_i\le W.
\tag{1.3}
\]

A depth-\(q\) window is a string of \(q+1\) consecutive middle vertices.
The number of such windows is

\[
w_q=\sum_{i=1}^p(\ell_i-q)_+.
\tag{1.4}
\]

Define the boundary-loss profile

\[
b_q=v-w_q=\sum_{i=1}^p\min(q,\ell_i),
\qquad b_0=0.
\tag{1.5}
\]

It is discretely concave, because

\[
b_q-b_{q-1}
=|\{i:\ell_i\ge q\}|
\tag{1.6}
\]

is nonincreasing in \(q\). Also

\[
b_1=p,
\qquad
b_H\ge\min(v,H).
\tag{1.7}
\]

Call the path family **strictly two-sided rainbow through \(H\)** if, for
every \(1\le q\le H\):

* every depth-\(q\) window has intersection rank \(m-q\) and union rank
  \(m+q\);
* all its lower intersections are pairwise distinct;
* all its upper unions are pairwise distinct.

Then both colour supports have size \(w_q\). Their missing counts are

\[
M_q^-=M_q^+=N_q-w_q=N_q-v+b_q,
\tag{1.8}
\]

and necessarily

\[
b_q\ge v-N_q.
\tag{1.9}
\]

Strict lower rainbowness also removes the short-run obstruction in the
erosion theorem. If a coordinate has an internal one-run of length
\(r\le H\), the depth-\(r\) lower intersections of the two adjacent
\((r+1)\)-vertex windows straddling that run are equal: their only possible
set difference would be the run coordinate, which is absent at the
opposite endpoint. This contradicts injectivity of the lower
depth-\(r\) colours. Hence no coordinate has a forbidden short internal
one-run.

The audited endpoint-capped erosion construction emits a literal OR word
of length

\[
W+G_H(\mathcal P),
\qquad
G_H(\mathcal P)
=Hp+\sum_{q=1}^H(M_q^-+M_q^+).
\tag{1.10}
\]

The \(W-v\) omitted middle sets are already included in the base \(W\):
the path blocks use \(v+Hp\) letters and the omitted middles are appended
literally. Thus (1.10) is valid without assuming \(v=W\).

## 2. Exact concave-majorant theorem

The first obstruction is not merely an order estimate. The optimal
arithmetic profile can be calculated exactly.

### Theorem 2.1 (exact global-rainbow erosion toll)

Assume

\[
2(H-1)^2\le m+1.
\tag{2.1}
\]

For \(0\le v\le W\), put

\[
D_v=(v-N_H)_+,
\qquad
S_v=\max\{D_v,\min(v,H)\}.
\tag{2.2}
\]

For an integer \(S=aH+r\), \(0\le r<H\), define

\[
C_H(S)=aH(H+2)+
\begin{cases}
0,&r=0,\\[1mm]
H+(2H+1)r-r^2,&1\le r<H.
\end{cases}
\tag{2.3}
\]

Among all integer path-length profiles satisfying the numerical
strict-rainbow constraints (1.7)--(1.9), the exact minimum of (1.10) is

\[
\boxed{
G_{\min}(v)
=2\sum_{q=1}^H(N_q-v)+C_H(S_v).}
\tag{2.4}
\]

This is an arithmetic minimum. Realizability of its extremal lengths by
actual Johnson paths is not asserted; extra geometry can only increase the
cost.

#### Proof

The binomial layers obey the exact second-difference identity

\[
N_{q-1}-2N_q+N_{q+1}
=
\frac{2(2q^2-m-1)}
{(m-q+1)(m+q+1)}N_q.
\tag{2.5}
\]

Under (2.1), \(N_q\) is concave for \(0\le q\le H\). Hence

\[
e_q=(v-N_q)_+,\qquad e_0=0,
\tag{2.6}
\]

is convex and nondecreasing. Every feasible \(b\) is concave, starts at
zero, majorizes \(e\), and has endpoint at least \(S_v\). Therefore its
least possible real-valued profile is the chord

\[
L_q=\frac qH S_v.
\tag{2.7}
\]

It remains to calculate the integer surcharge. Truncate each component at
length \(H\). A component with truncated length \(t\in[1,H]\) contributes

\[
\begin{aligned}
c_H(t)
&=H+2\sum_{q=1}^H\min(q,t)\\
&=H+(2H+1)t-t^2
\end{aligned}
\tag{2.8}
\]

to \(Hp+2\sum_qb_q\).

Two partial components can always be fused toward the endpoints. If
\(r+s\le H\), replacing \(r,s\) by \(r+s\) saves

\[
c_H(r)+c_H(s)-c_H(r+s)=H+2rs>0.
\tag{2.9}
\]

If \(r+s>H\), replacing them by \(H,r+s-H\) saves

\[
c_H(r)+c_H(s)-c_H(H)-c_H(r+s-H)
=2(H-r)(H-s)>0.
\tag{2.10}
\]

Thus the minimizing truncated profile of total \(S=aH+r\) consists of
\(a\) full \(H\)-components and, if \(r>0\), one component of length \(r\).
Its cost is exactly (2.3). The same formula, or adding one unit to a
truncated component, shows that \(C_H(S)\) is increasing in \(S\); hence the
least permitted endpoint \(S_v\) is optimal. If \(v>S_v\), then
\(S_v\ge H\), and all unused
vertices can be added to a full component without changing any \(b_q\) for
\(q\le H\). This proves (2.4). \(\square\)

### Corollary 2.2 (spanning formula and the sharp \(1/3\))

Take \(v=W\), and write

\[
D:=W-N_H=sH+r,\qquad 0\le r<H.
\tag{2.11}
\]

For all sufficiently large \(m\), \(D\ge H\), and

\[
\boxed{
\begin{aligned}
G_{\min}(W)
&=(H+2)(W-N_H)
-2\sum_{q=1}^H(W-N_q)+\delta_H(r),\\
\delta_H(r)
&=
\begin{cases}
0,&r=0,\\
H+r(H-1-r),&r>0.
\end{cases}
\end{aligned}}
\tag{2.12}
\]

Uniformly for \(H=o(\sqrt m)\),

\[
1-\frac{N_q}{W}
=\frac{q^2}{m}
+O\!\left(\frac{q^4+q^2}{m^2}\right).
\tag{2.13}
\]

Consequently

\[
\boxed{
G_{\min}(W)
=\frac{W}{3m}(H^3+3H^2-H)
+O\!\left(
\frac{W(H^5+H^3)}{m^2}+H^2
\right).}
\tag{2.14}
\]

If \(H\to\infty\) and \(H=o(\sqrt m)\), then

\[
\boxed{
G_{\min}(W)
=\left(\frac13+o(1)\right)\frac{WH^3}{m}.}
\tag{2.15}
\]

#### Proof

Equation (2.12) is (2.4) and (2.3) with \(v=W\).
Furthermore,

\[
\frac{N_q}{W}
=\prod_{j=0}^{q-1}\frac{m-j}{m+j+1}.
\tag{2.16}
\]

Taylor expansion of the logarithm, uniformly for \(q=o(\sqrt m)\), gives
(2.13). Substitution in (2.12), using

\[
\sum_{q=1}^Hq^2=\frac{H(H+1)(2H+1)}6,
\tag{2.17}
\]

gives

\[
(H+2)H^2
-\frac{H(H+1)(2H+1)}3
=\frac{H^3+3H^2-H}{3},
\tag{2.18}
\]

and the summed Taylor error in (2.14). The residue
\(\delta_H(r)\) is \(O(H^2)\). This proves the result. \(\square\)

In particular,

\[
\begin{array}{c|c}
H=o(m^{1/3})&G_{\min}(W)=o(W),\\
H\sim c\,m^{1/3}&G_{\min}(W)/W\to c^3/3,\\
m^{1/3}\ll H=o(\sqrt m)&G_{\min}(W)/W\to\infty.
\end{array}
\tag{2.19}
\]

For \(H\ge2\), allowing omitted middle vertices does not change the leading
threshold. Write

\[
D_*=W-N_H=sH+r,\qquad 0\le r<H.
\tag{2.20}
\]

Then the exact minimization of (2.4) over \(0\le v\le W\) is

\[
\boxed{
\min_{0\le v\le W}G_{\min}(v)
=G_{\min}(W)
-\mathbf1_{r>0}(H+r-r^2)_+.}
\tag{2.21}
\]

In particular, omissions improve the spanning value by at most \(H\).
To prove this, write \(D=v-N_H=aH+t\) on the range \(D\ge H\).
The \(v\)-dependent part is

\[
J(D)=C_H(D)-2HD.
\tag{2.22}
\]

At block bases,

\[
J(aH)=aH(2-H),
\tag{2.23}
\]

and for \(1\le t<H\),

\[
J(aH+t)=J(aH)+H+t-t^2.
\tag{2.24}
\]

For \(H\ge2\), the bases are nonincreasing and the concavity in \(t\)
leaves only the final base or the endpoint as a minimizer. At the last
endpoint the possible improvement is precisely
\((H+r-r^2)_+\).

It remains to check \(D<H\). For \(H\le v\le N_H+H\), one has
\(S_v=H\), so (2.4) decreases with \(v\), attaining its minimum at
\(D=H\). For \(1\le v<H\),

\[
G_{\min}(v)-G_{\min}(H)
=H(H-1)-v(v-1)\ge0,
\tag{2.25}
\]

and for \(v=0\),

\[
G_{\min}(0)-G_{\min}(H)=H(H-2)\ge0.
\tag{2.26}
\]

Thus a strict-rainbow additive erosion theorem cannot reach a
tail-compatible band: every such band contains a subband
\(h\asymp m^{1/3}\), already forcing positive linear excess. Explicitly,
if \(h\le H\), restriction to the first \(h\) depths gives

\[
G_H(\mathcal P)
\ge hp+\sum_{q=1}^h(M_q^-+M_q^+)
\ge G_{\min,h}(v).
\tag{2.27}
\]

## 3. Arbitrary splices do not remove the Gaussian reset toll

The preceding \(1/3\) theorem is for additive endpoint-capped path blocks.
The next count permits arbitrary reordering and arbitrary attempted
cross-component splices.

Let \(n=2m+\varepsilon\), \(\varepsilon\in\{0,1\}\), and put

\[
W=\binom nm,\qquad N_q=\binom n{m-q}.
\tag{3.1}
\]

Start with any final ordering of \(V\) distinct middle sets into strings.
Choose a transition transversal meeting every depth-\(q\) window,
\(q\le H\), which is nongeodesic or would exceed its colour capacity, and
cut at all selected transitions. Let the resulting \(b\) blocks have
positive lengths \(\ell_1,\ldots,\ell_b\).

### Theorem 3.1 (capacity of the seam-free windows)

Suppose every depth-\(q\) window internal to a block is geodesic, and its
lower colour \(S\in\binom{[n]}{m-q}\) is used at most \(a_q(S)\) times.
Then

\[
\boxed{
\sum_{i=1}^b\min(\ell_i,q)
\ge V-\sum_Sa_q(S),}
\tag{3.2}
\]

and therefore

\[
\boxed{
qb\ge V-\sum_Sa_q(S).}
\tag{3.3}
\]

#### Proof

The number of internal depth-\(q\) windows is exactly

\[
\sum_i(\ell_i-q)_+
=V-\sum_i\min(\ell_i,q).
\tag{3.4}
\]

Their total allowed colour capacity is at most \(\sum_Sa_q(S)\). Comparing
the two quantities proves (3.2), and
\(\min(\ell_i,q)\le q\) proves (3.3). \(\square\)

The theorem is independent of the original component ordering. A physical
cross-component splice for which every crossing window through depth \(H\)
is geodesic and capacity-compatible simply creates more counted internal
windows. If any crossing window fails, the transversal must mark some
transition in it. Thus arbitrary splicing does not evade (3.2).

For strict rainbowness, \(a_q(S)=1\), so

\[
b\ge\max_{1\le q\le H}\frac{V-N_q}{q}.
\tag{3.5}
\]

Here

\[
\frac{N_q}{W}
=\prod_{j=0}^{q-1}
\frac{m-j}{m+\varepsilon+j+1}.
\tag{3.6}
\]

Taking logarithms and using Taylor expansion uniformly for
\(q\le A\sqrt m\) gives

\[
\frac{N_q}{W}
=\exp\!\left(-\frac{q^2}{m}+O_A(m^{-1/2})\right).
\tag{3.7}
\]

Hence, if \(V=W-o(W)\) and \(H=\lceil A\sqrt m\rceil\),

\[
\boxed{
Hb\ge
\left(1-e^{-A^2}+o(1)\right)W.}
\tag{3.8}
\]

More sharply,

\[
b\ge
\left(\gamma_A+o(1)\right)\frac W{\sqrt m},
\qquad
\gamma_A=\max_{0<x\le A}\frac{1-e^{-x^2}}x.
\tag{3.9}
\]

The same conclusion is robust under \(o(W)\) collisions. If the internal
depth-\(q\) lower-colour loads are \(\mu_q\), put

\[
E_q=\sum_S(\mu_q(S)-1)_+
\tag{3.10}
\]

for their duplicate excess. Taking
\(a_q(S)=\max\{1,\mu_q(S)\}\) in Theorem 3.1 gives

\[
\boxed{
qb\ge V-N_q-E_q.}
\tag{3.11}
\]

Thus \(V=W-o(W)\) and \(E_H=o(W)\) still force the linear bound (3.8).

Therefore every reset/erosion literalization paying \(H\) boundary entries
per final block has linear excess at every fixed Gaussian depth.

This remains an architectural reset lower bound. It is not a theorem that
an arbitrary contiguous-OR word must pay \(H\) letters for every bad seam.

## 4. Cyclic closure and the Greene--Kleitman skeleton

### 4.1 Strict cyclic colours are impossible

A cyclic component of length greater than \(q\) has one cyclic
depth-\(q\) window per middle vertex. Thus cyclic components containing
\(V\) middle vertices and respecting multiplicity caps \(a_q(S)\) satisfy

\[
\boxed{V\le\sum_Sa_q(S).}
\tag{4.1}
\]

For strict colours this is \(V\le N_q\). In particular, a spanning exact
cycle factor has \(V=W>N_q\) for every \(q\ge1\), so strict cyclic
rainbowness is impossible already at depth one.

If \(\mu_q\) is its cyclic colour load, then

\[
\sum_S(\mu_q(S)-1)_+
=W-|\operatorname{supp}\mu_q|
\ge W-N_q.
\tag{4.2}
\]

At \(q=A\sqrt m\), the right side is

\[
\left(1-e^{-A^2}+o(1)\right)W.
\tag{4.3}
\]

Thus even \(o(W)\)-collision strict rainbowness is impossible across a
Gaussian band. Cyclic closure restores the seam windows but not the missing
colour capacity.

### 4.2 The Greene--Kleitman forest requires linear global rematching

Let \(G_m\) be the proved Greene--Kleitman two-sided-rainbow forest on the
\(W=\binom{2m}{m}\) middle sets. It has

\[
E=W-\operatorname{Cat}_m,
\qquad
\operatorname{Cat}_m=\frac W{m+1},
\tag{4.4}
\]

and exactly \(W/2\) vertices have indegree zero. Put

\[
\Sigma_m=\sum_v(\deg_{G_m}(v)-2)_+.
\tag{4.5}
\]

Since

\[
\sum_v(\deg(v)-2)=-2\operatorname{Cat}_m
\tag{4.6}
\]

and every indegree-zero vertex has total degree at most one, the negative
part of the sum in (4.6) is at least \(W/2\). Hence

\[
\Sigma_m\ge\frac W2-2\operatorname{Cat}_m.
\tag{4.7}
\]

### Theorem 4.1 (repetition/rematching tradeoff)

Take any linear or cyclic middle-state schedule containing every middle
vertex once and \(x\) additional repeated occurrences. If \(R\) edges of
\(G_m\) are not realized as consecutive schedule transitions, then

\[
\boxed{
R+x\ge\frac W4-\operatorname{Cat}_m.}
\tag{4.8}
\]

#### Proof

Let \(x_v\) be the number of extra occurrences of vertex \(v\), and let
\(r_v\) be the number of incident forest edges not retained. The retained
incident edges at \(v\) are at most the schedule degree capacity
\(2(1+x_v)\). Therefore

\[
(\deg_{G_m}(v)-2)_+\le r_v+2x_v.
\tag{4.9}
\]

Summing, using \(\sum_vr_v=2R\), \(\sum_vx_v=x\), and (4.7), gives

\[
\frac W2-2\operatorname{Cat}_m
\le2R+2x.
\]

This is (4.8). \(\square\)

A paired lower/upper forest colour determines its Johnson edge uniquely:
if \(S\subset U\), \(|S|=m-1\), \(|U|=m+1\), then the two middle endpoints
are \(S\cup\{a\}\) and \(S\cup\{b\}\), where
\(U\setminus S=\{a,b\}\). Thus (4.8) says that a cyclic completion must
either repeat linearly many middle states or globally rematch linearly many
paired colours. Component closure is not the missing \(o(W)\) operation.

## 5. Balanced capacities are the canonical sufficient replacement

Return to the exact odd-wreath setting

\[
n=2m+1,\qquad
W=\binom nm,\qquad
N_q=\binom n{m-q},\qquad
B=\frac Wn.
\tag{5.1}
\]

Write

\[
W=c_qN_q+r_q,
\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\qquad
0\le r_q<N_q.
\tag{5.2}
\]

A balanced integral quota is a vector

\[
\beta_q(S)\in\{c_q,c_q+1\},
\qquad
\sum_S\beta_q(S)=W.
\tag{5.3}
\]

It has the upper value on exactly \(r_q\) targets.

For a lower cyclic-shadow load \(\mu_q\) of total \(W-U\), define its
overload relative to \(\beta_q\) by

\[
O_q^\beta
=\sum_S(\mu_q(S)-\beta_q(S))_+.
\tag{5.4}
\]

### Lemma 5.1 (exact integral capacity deficit)

If \(M_q=|\{S:\mu_q(S)=0\}|\), then

\[
\boxed{
M_q\le\frac{U+O_q^\beta}{c_q}.}
\tag{5.5}
\]

For a full exact factor \(U=0\). If \(O_q^\beta=0\), then
\(\mu_q=\beta_q\) pointwise.

#### Proof

The total quota is \(W\), while the total load is \(W-U\). Hence

\[
\sum_S(\beta_q(S)-\mu_q(S))_+
=U+\sum_S(\mu_q(S)-\beta_q(S))_+
=U+O_q^\beta.
\tag{5.6}
\]

Every hole contributes at least \(c_q\) to the left side. This proves
(5.5). If \(U=O_q^\beta=0\), both nonnegative discrepancy parts vanish.
\(\square\)

This shows why balanced quotas are the canonical minimum-spread
capacitation. A uniform cap \(\mu_q(S)\le c_q+1\) has excess total capacity
and can coexist with many holes. A balanced quota has total capacity exactly
equal to the occurrence mass. Balance is sufficient, not logically
necessary for literal conversion: an unbalanced full-support profile has
no holes and already converts.

For a full exact factor, define the optimized balanced overload

\[
O_q(F)=\min_{\beta_q}O_q^\beta(F).
\tag{5.6a}
\]

If

\[
D_q(F)=\sum_S(c_q-\mu_q(S))_+,
\qquad
t_q(F)=|\{S:\mu_q(S)\ge c_q+1\}|,
\tag{5.6b}
\]

then

\[
\boxed{
O_q(F)=D_q(F)+(r_q-t_q(F))_+.}
\tag{5.6c}
\]

Indeed, each of the \(r_q\) upper quota bonuses should be placed on a
distinct target already above the floor whenever possible. Conservation of
total mass gives the displayed identity.

### Theorem 5.2 (literal capacitated cycle-to-word conversion)

Let \(F\) be one exact wreath factor, and let \(O_q^\beta(F)\) be its lower
depth-\(q\) overload relative to any balanced integral quotas. For every
\(1\le H<m\),

\[
\boxed{
\begin{aligned}
\nu(2m+1)\le{}&
W+(2H+1)B
+2\sum_{q=1}^H\frac{O_q^\beta(F)}{c_q}\\
&+2\sum_{r=0}^{m-H-1}\binom{2m+1}{r}-1.
\end{aligned}}
\tag{5.7}
\]

#### Proof

For every cyclic row \(\pi\) of \(F\), emit its \(n\) cyclic intervals of
rank \(m-H\), followed by copies of its first \(2H+1\) entries. A union of
between one and \(2H+2\) consecutive emitted entries is the corresponding
cyclic interval. Thus the blocks cover every shadow supplied by \(F\) in
the complement-closed rank band

\[
[m-H,m+H+1].
\tag{5.8}
\]

The \(B\) blocks cost

\[
B(n+2H+1)=W+(2H+1)B.
\tag{5.9}
\]

At every lower depth \(q\), append the \(M_q\) missing masks literally.
Complementation within each cyclic row gives the same missing count in the
paired upper rank. Lemma 5.1 with \(U=0\) gives

\[
2\sum_{q=1}^HM_q
\le2\sum_{q=1}^H\frac{O_q^\beta(F)}{c_q}.
\tag{5.10}
\]

Finally append every nonempty target outside (5.8). The lower and upper
tails have the same size; subtract one for the empty lower target. This
proves (5.7). Every witness described is a literal contiguous union inside
the emitted word. \(\square\)

For example, taking

\[
H=(1+\varepsilon)\sqrt{m\log m}
\tag{5.11}
\]

makes the seam and literal-tail terms in (5.7) \(o(W)\). Therefore a
single sequence of exact factors satisfying

\[
\sum_{q=1}^H\frac{O_q^\beta(F)}{c_q}=o(W)
\tag{5.12}
\]

at such a depth proves the sharp constant-one theorem directly.

For completeness, the tail assertion follows by successive binomial
ratios: uniformly once \(H=o(m)\),

\[
\sum_{r=0}^{m-H-1}\binom{2m+1}{r}
\le
O\!\left(\frac mH\right)\binom{2m+1}{m-H},
\tag{5.12a}
\]

while

\[
\frac{\binom{2m+1}{m-H}}W
\le\exp\!\left(-\frac{H^2}{m+H+1}\right).
\tag{5.12b}
\]

At (5.11) their product is \(o(1)\).

The weights themselves have the useful exact-scale bound

\[
\boxed{
\sum_{q=1}^m\frac1{c_q}
\le\sqrt{\pi(m+1)}.}
\tag{5.13}
\]

Indeed, \(c_q\ge(W/N_q)/2\), while

\[
\log\frac W{N_q}
\ge\frac{q(q+1)}{m+1}
\ge\frac{q^2}{m+1}.
\tag{5.14}
\]

Thus

\[
\frac1{c_q}\le2e^{-q^2/(m+1)},
\tag{5.15}
\]

and comparison with the Gaussian integral proves (5.13).

Alternatively, the frozen project logic says that proving the fixed-\(A\)
weighted overload theorem for every \(A\), inside one exact factor for each
\(A\), gives MWB by slow diagonalization and hence constant one via the
already audited outer-tail transfer. No labelled common-owner
synchronization is inferred.

## 6. Exact lane closure and audit

The proved conclusions are:

1. the exact strict-rainbow erosion toll (2.4), including all short
   components and the sharp constant \(1/3\);
2. the universal strict splice-capacity inequality (3.2);
3. impossibility of strict cyclic rainbowness by (4.1)--(4.3);
4. the linear repetition/rematching lower bound (4.8) for the literal
   Greene--Kleitman skeleton;
5. the integral balanced-capacity deficit identity, optimal-overload
   identity, and literal cycle-to-word theorem (5.5)--(5.7).

Three independent proof audits separately rederived:

* the concavity, Ferrers integrality, residue term, and \(1/3\) asymptotic;
* the arbitrary-splice capacity count and its Gaussian constant;
* the cyclic pigeonhole, Greene--Kleitman degree ledger, balanced deficit,
  and literal conversion constants.

The following are not claimed:

* no lower bound against arbitrary contiguous-OR words is proved;
* repeated balanced colours are not obstructed;
* no exact factor with (5.12), or with fixed-window MWB, is constructed;
* no common-owner labelled synchronization theorem follows;
* the result does not refute the constant-one conjecture.

The strict endpoint-capped/reset-per-block forest lane and the strict cyclic
factor lane are closed in the required quantitative sense. Before the
Gaussian band the former already pays a linear concavity toll; arbitrary
splicing still leaves a linear block count; cyclic closure violates strict
colour capacity; and the existing Greene--Kleitman skeleton needs linear
rematching. This does not exclude a noncanonical shared connector scheme
costing \(o(H)\) per final block. Any surviving colored cycle-factor theorem
must permit repeated colours. It may target hole support directly; balanced
weighted overload is the canonical stronger sufficient target, not a
necessary condition for literal conversion.
