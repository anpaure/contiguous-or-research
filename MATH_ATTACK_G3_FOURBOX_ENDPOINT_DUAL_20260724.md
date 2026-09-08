# Third-wave G: four-box endpoint-potential dual

## 0. Verdict

The endpoint-potential argument extends to four boxes without a dimensional
failure. The flat plateau proof is dimension-free, and the exact sloped-band
calculation survives after replacing triangular corner deficits by
tetrahedral ones.

Let

\[
Q(p,q,r,s)=[0,p]\times[0,q]\times[0,r]\times[0,s],
\]

let \(g_4(p,q,r,s)\) be the least length of a nonzero word whose contiguous
coordinatewise maxima contain every nonzero point of \(Q\), and let
\(w_4(p,q,r,s)\) be the width. Put

\[
P=p+q+r,\qquad V=(p+1)(q+1)(r+1).
\]

### Main theorem

If \(s\ge P\), then \(w_4(p,q,r,s)=V\). For every integer

\[
0\le k\le\min\{p,q,r\},
\]

one has

\[
\boxed{
\begin{aligned}
2(s+2k)\bigl(g_4(p,q,r,s)-V\bigr)
\ge{}&(s-P+2k)V\\
&+6\binom{k+2}{4}
-(4P+2)\binom{k+2}{3}.
\end{aligned}}
\tag{0.1}
\]

In particular, \(k=0\) gives the flat bound

\[
\boxed{
g_4(p,q,r,s)
\ge
V+\left\lceil\frac{V(s-P)}{2s}\right\rceil .
}
\tag{0.2}
\]

On a fixed ray

\[
(p,q,r,s)=(at,bt,ct,dt),\qquad
A=a+b+c,\qquad d\ge A,
\]

(0.1) yields

\[
\boxed{
\begin{aligned}
\liminf_{t\to\infty}
\frac{g_4(at,bt,ct,dt)-(at+1)(bt+1)(ct+1)}{t^3}
\ge
\max_{0\le x\le\min(a,b,c)}
\frac{
abc(d-A+2x)-\frac23Ax^3+\frac14x^4
}{
2(d+2x)
}.
\end{aligned}}
\tag{0.3}
\]

The right side is positive on every closed dominant ray \(d\ge A\):
use \(x=0\) if \(d>A\), and any sufficiently small fixed \(x>0\) if
\(d=A\). For example,

\[
g_4(t,t,t,4t)
\ge
(t+1)^3+\left(\frac18-o(1)\right)t^3,
\tag{0.4}
\]

while \(k=\lfloor t/2\rfloor\) gives

\[
g_4(t,t,t,3t)
\ge
(t+1)^3+\left(\frac{49}{512}-o(1)\right)t^3.
\tag{0.5}
\]

Consequently the compact balanced four-box lemma CB4 is false. The standard
four-block SCD construction which pays for one independent universal word
per product box has a fixed positive relative overhead. This does not
disprove the global Boolean contiguous-OR conjecture: cross-box fusion and
high-degree global sharing remain possible.

---

## 1. Endpoint-chain normalization

Choose one literal witnessing interval

\[
I_T=[\ell_T,r_T]
\]

for every target in the family under consideration. Group targets by common
left endpoint and, separately, by common right endpoint.

### Lemma 1.1 (orthogonal endpoint partitions)

Each endpoint class is a chain in the coordinatewise order. A left class
and a right class meet in at most one target. Each partition has at most
\(n\) nonempty chains when the physical word has length \(n\).

#### Proof

With a fixed left endpoint, increasing the right endpoint only increases
the interval maximum. The fixed-right statement is symmetric. If two
distinct targets lay in one common left class and one common right class,
their chosen intervals would have both endpoints equal and hence the same
maximum. Empty physical endpoint classes are irrelevant. \(\square\)

The same chosen interval supplies both endpoints. This coupling is not an
extra assumption: the proof works for every arbitrary simultaneous choice
of one witness per target.

When \(s\ge P\), projection to the first three coordinates is injective on
every antichain, so \(w_4\le V\). Rank \(P\) contains

\[
(x,y,z,P-x-y-z)
\]

for every \((x,y,z)\in[0,p]\times[0,q]\times[0,r]\), and hence has \(V\)
points. Therefore

\[
w_4(p,q,r,s)=V.
\tag{1.1}
\]

---

## 2. The flat endpoint-potential theorem

Put

\[
H=s-P.
\]

For \(0\le j\le H\), take the full plateau layer

\[
\Lambda_j=
\{(x,y,z,P+j-x-y-z):
0\le x\le p,\ 0\le y\le q,\ 0\le z\le r\}.
\tag{2.1}
\]

Every layer has \(V\) targets.

Fix one endpoint partition and suppose it has

\[
C=V+\delta,\qquad 0\le\delta\le D,
\qquad D=n-V.
\]

If \(A_j\) is the set of endpoint chains occupied by \(\Lambda_j\), then

\[
|A_j\cap A_{j+1}|\ge V-\delta.
\]

A common chain contains comparable targets in adjacent ranks, hence a
genuine box-poset cover. Across the \(H\) adjacent layer pairs, this
partition therefore uses at least

\[
H(V-\delta)
\tag{2.2}
\]

covers.

Use the horizontal potential

\[
\phi(x,y,z,w)=x+y+z,\qquad 0\le\phi\le P.
\tag{2.3}
\]

The bottom and top layers have identical \(\phi\)-multisets. Exactly
\(\delta\) endpoint chains start internally and \(\delta\) end internally.
Telescoping \(\phi\) along every chain gives

\[
\sum_C\bigl(\phi(\max C)-\phi(\min C)\bigr)\le P\delta.
\tag{2.4}
\]

Every cover in one of the first three directions raises \(\phi\) by one.
A fourth-coordinate cover leaves \(\phi\) fixed. Rank skips have
nonnegative potential increase. Thus at most \(P\delta\) covers in (2.2)
are horizontal, and the partition uses at least

\[
H(V-\delta)-P\delta
=HV-s\delta
\tag{2.5}
\]

vertical covers.

The plateau contains exactly \(HV\) vertical covers. The left and right
endpoint partitions cannot use the same vertical edge: its two targets
would then lie in one common left class and one common right class, contrary
to Lemma 1.1. Applying (2.5) to both partitions gives

\[
2HV-s(\delta_L+\delta_R)\le HV.
\]

Since \(\delta_L,\delta_R\le D\),

\[
HV\le2sD.
\tag{2.6}
\]

This proves (0.2). The scarce objects are target-poset cover edges, not
physical word adjacencies or coordinate occurrences.

The proof is dimension-free: with \(m-1\) short coordinates, replace
\(V\) by their level product and \(P\) by their side sum.

---

## 3. Exact four-dimensional sloped band

The flat slab has zero thickness at \(s=P\). The sloped shoulders restore a
positive obstruction there.

Fix

\[
0\le k\le\min\{p,q,r\}
\]

and retain every rank from \(P-k\) through \(s+k\). Put

\[
J=s-P+2k.
\tag{3.1}
\]

There are \(J+1\) layers and \(J\) adjacent-rank transitions.

### 3.1 Tetrahedral shoulder counts

At depth \(j\), either shoulder omits the corner

\[
\{(u_1,u_2,u_3)\in\mathbb Z_{\ge0}^3:
u_1+u_2+u_3<j\},
\]

whose size is

\[
F_j=\binom{j+2}{3}.
\tag{3.2}
\]

The restriction \(j\le k\le\min(p,q,r)\) prevents truncation by a side.
Define

\[
F=\binom{k+2}{3},
\qquad
E=\sum_{j=1}^{k}F_j=\binom{k+3}{4}.
\tag{3.3}
\]

The two boundary layers have common size

\[
B_0=V-F,
\tag{3.4}
\]

and the total band population is

\[
T=(J+1)V-2E.
\tag{3.5}
\]

Every vertical base column meets the band in one nonempty contiguous
interval. Hence the exact number of vertical target-poset covers is

\[
A_v=T-V.
\tag{3.6}
\]

### 3.2 Boundary potential

The low-corner \(\phi\)-mass is

\[
\begin{aligned}
S
&=\sum_{x+y+z<k}(x+y+z)\\
&=3\binom{k+2}{4}.
\end{aligned}
\tag{3.7}
\]

Indeed, the number of triples of sum \(m\) is \(\binom{m+2}{2}\), and

\[
m\binom{m+2}{2}=3\binom{m+2}{3}.
\]

The bottom boundary omits the complementary high corner, of potential mass
\(PF-S\). The top boundary omits the low corner, of mass \(S\). Therefore

\[
\Delta_\phi
:=\sum_{\rm top}\phi-\sum_{\rm bottom}\phi
=PF-2S.
\tag{3.8}
\]

### 3.3 Covers used by one endpoint partition

Let one endpoint partition have \(C\) nonempty chains, and let the layer
sizes be \(m_0,\ldots,m_J\). Adjacent occupied-chain sets intersect in at
least \(m_i+m_{i+1}-C\). Summing over all transitions gives at least

\[
2T-2B_0-JC
\tag{3.9}
\]

band covers. A negative individual intersection bound remains a valid
lower bound.

Exactly \(B_0\) chains meet each boundary. The other \(C-B_0\) chain starts
and ends are internal. Telescoping \(\phi\) gives

\[
\sum_C\bigl(\phi(\max C)-\phi(\min C)\bigr)
\le
\Delta_\phi+P(C-B_0).
\tag{3.10}
\]

Consequently the partition uses at least

\[
2T-2B_0-\Delta_\phi+PB_0-(J+P)C
\tag{3.11}
\]

vertical covers.

### 3.4 Coupling the partitions

For the left and right endpoint partitions, orthogonality and (3.6) give

\[
\begin{aligned}
2\bigl(2T-2B_0-\Delta_\phi+PB_0\bigr)
-(J+P)(C_L+C_R)
\le A_v.
\end{aligned}
\tag{3.12}
\]

Both chain counts are at most \(n\). Since the coefficient of
\(C_L+C_R\) is negative, substituting

\[
C_L+C_R\le2n
\]

has the correct direction:

\[
2\bigl(2T-2B_0-\Delta_\phi+PB_0\bigr)
-2(J+P)n
\le A_v.
\tag{3.13}
\]

Write \(n=V+D\) and note \(J+P=s+2k\). Substitution gives

\[
2(s+2k)D
\ge
JV-6E+4S+4(1-P)F.
\tag{3.14}
\]

Finally,

\[
-6E+4S+4(1-P)F
=6\binom{k+2}{4}-(4P+2)\binom{k+2}{3}.
\tag{3.15}
\]

Equations (3.14)--(3.15) prove (0.1). Since \(D\) is a nonnegative integer,
the exact finite statement is

\[
\boxed{
D\ge
\max\left\{
0,\
\left\lceil
\frac{
(s-P+2k)V
+6\binom{k+2}{4}
-(4P+2)\binom{k+2}{3}
}{
2(s+2k)
}
\right\rceil
\right\}.
}
\tag{3.16}
\]

No saturation of endpoint chains is assumed. A chain which skips ranks
only weakens (3.9) and contributes nonnegative unused potential.

---

## 4. Fixed rays and the exact boundary

Let

\[
(p,q,r,s)=(at,bt,ct,dt),\qquad
A=a+b+c,\qquad d\ge A,
\]

and choose

\[
k=\lfloor xt\rfloor,\qquad
0\le x\le\min(a,b,c).
\]

The numerator in (3.16) is

\[
\left(
abc(d-A+2x)-\frac23Ax^3+\frac14x^4
\right)t^4+O(t^3),
\tag{4.1}
\]

while the denominator is

\[
2(d+2x)t+O(1).
\tag{4.2}
\]

This proves (0.3). The floor in \(k\) changes the quotient by only
\(O(t^2)\), negligible after normalization by \(t^3\).

If \(d>A\), \(x=0\) gives

\[
\frac{abc(d-A)}{2d}>0.
\tag{4.3}
\]

If \(d=A\), the numerator is

\[
2abc\,x-\frac23Ax^3+\frac14x^4,
\tag{4.4}
\]

which is positive for every sufficiently small \(x>0\). Hence every closed
dominant plateau ray has positive cubic excess.

For \((a,b,c,d)=(1,1,1,3)\) and \(x=1/2\), (4.4) equals \(49/64\), while
the denominator in (0.3) is \(8\). This gives \(49/512\), proving (0.5).

The compact hypothesis CB4 requires \(o(R^3)\) excess uniformly on every
fixed compact aspect-ratio window. The single ray \((1,1,1,3)\) already
contradicts it.

---

## 5. Independent literal-witness corroboration

The ordered-middle-witness proof also extends. This is independent of the
endpoint-potential certificate and becomes stronger on very long rays.

Assume

\[
1\le p\le q\le r,\qquad s>P.
\]

Put

\[
h=\left\lfloor\frac{P+s}{2}\right\rfloor,
\qquad
\epsilon=P+s-2h,
\qquad
M=V.
\]

The rank-\(h\) layer is the full base graph and has \(M\) targets. The
number of nonzero targets below it is

\[
L_{<h}=M\frac{s-\epsilon}{2}-1.
\tag{5.1}
\]

Ordering one middle witness per target by its left endpoint gives

\[
\ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
\]

with nondecreasing \(\alpha_i,\beta_i\in[0,D]\), and

\[
L_{<h}\le\sum_i(r_i-\ell_i)+(h-1)D.
\tag{5.2}
\]

### Lemma 5.1 (sharp four-coordinate mesh)

An internal positive coordinate-threshold run is an interval \([u,v]\)
with \(1<u\le v<m\) for which some coordinate and integer threshold
\(\lambda\ge1\) are attained throughout \([u,v]\) and are strictly missed
at \(u-1\) and \(v+1\).

Every order of \(P+2\) distinct points in the full middle layer has an
internal positive coordinate-threshold run of edge length at most \(q+r\).
The constants \(P+2\) and \(q+r\) are sharp.

#### Proof

If a nonnegative scalar sequence has no internal positive threshold run,
it is valley-shaped. Suppose all four coordinate sequences are valleys and
order their turns as

\[
\tau_A\le\tau_B\le\tau_C\le\tau_D.
\]

Constant sum and distinctness force \(\tau_A=1\) and \(\tau_D=m\).
Respectively charge the three intervening phases to the strict increase of
\(A\), the strict increase of \(A+B\), and the strict decrease of \(D\).
The charges telescope:

\[
\begin{aligned}
m-1
&\le A_{\tau_B}-A_1
 +(A+B)_{\tau_C}-(A+B)_{\tau_B}
 +D_{\tau_C}-D_m\\
&=h-\bigl(A_1+B_{\tau_B}+C_{\tau_C}+D_m\bigr)\\
&\le P.
\end{aligned}
\tag{5.3}
\]

The last inequality uses the four coordinatewise lower bounds, whose sum
on the full middle layer is \(h-P\). Thus \(P+2\) points force an internal
run.

Inside a forced run take a maximal plateau at its largest active-coordinate
value. It is an internal positive run. If its edge length exceeds \(q+r\),
it contains \(q+r+2\) consecutive points in one fixed-coordinate
three-box slice. The three-coordinate version of (5.3) bounds any no-run
subsequence there by one plus the sum of the two smallest remaining side
lengths. Explicitly, for remaining sides \(u\le v\le w\) at rank \(a\),
the valley proof gives

\[
m-1\le
a-\sum_{i=1}^3
\max\left(0,a-\sum_{j\ne i}u_j\right)
\le u+v.
\]

The last inequality follows directly if \(a\le u+v\), while for
\(a>u+v\) the \(w\)-coordinate lower bound contributes \(a-u-v\).
Here \(u+v\le q+r\). Hence this subwindow contains a second internal run,
of edge length at most \(q+r-1\).

Sharpness is witnessed by

\[
(i,0,0,h-i),\qquad 0\le i\le p-1,
\]

followed by

\[
(p,j,0,h-p-j),\qquad 0\le j\le q,
\]

then

\[
(p,q,k,h-p-q-k),\qquad 1\le k\le r,
\]

and finally

\[
(p-1,q,r,h-P+1).
\]

Only the \(x=p\) plateau is an internal positive run; it has edge length
\(q+r\). Deleting the final point gives a no-run sequence of length
\(P+1\). \(\square\)

The literal one-pin gap and balanced block-pair congestion argument are
dimension-free. Define

\[
s_0=P+2,\qquad
K=2\left\lfloor\frac{M}{2s_0}\right\rfloor,
\qquad
B=s_0+\left\lceil\frac{M-Ks_0}{K}\right\rceil .
\]

When \(K\ge2\), they give

\[
\sum_i(r_i-\ell_i)\le(q+r)M+2BD.
\tag{5.4}
\]

Combining (5.1), (5.2), and (5.4) yields

\[
\boxed{
D\ge
\frac{
M\bigl((s-\epsilon)/2-(q+r)\bigr)-1
}{
h-1+2B
}
}
\tag{5.5}
\]

whenever the numerator is positive. On a ray

\[
(p,q,r,s)=(at,bt,ct,dt),\qquad a\le b\le c,\quad d>2(b+c),
\]

this becomes

\[
\boxed{
\liminf_{t\to\infty}\frac{D}{t^3}
\ge
\frac{abc(d-2b-2c)}{d+5a+5b+5c}.
}
\tag{5.6}
\]

The four-dimensional degradation is precise: a fixed coordinate level may
contain \(\Theta(R^2)\) targets, so the three-box level-cardinality shortcut
does not transfer. The recursive valley argument repairs this and retains
an exact \(O(R)\) mesh. Thus there is no dimensional obstruction to the
literal route either.

---

## 6. Four-block SCD aggregation

Let the global Boolean dimension be \(N=4n\), split the coordinates into
four equal blocks, and choose arbitrary symmetric-chain decompositions in
the blocks. Put

\[
R=\sqrt N,
\qquad
W(m)=\binom{m}{\lfloor m/2\rfloor}.
\]

The multiset of chain heights in an SCD of \(B_n\) is fixed. For
\(\ell\equiv n\pmod2\), the number of height-\(\ell\) chains is

\[
a_n(\ell)
=
\binom{n}{(n-\ell)/2}
-\binom{n}{(n-\ell)/2-1}.
\tag{6.1}
\]

### Lemma 6.1 (Gaussian height windows)

For fixed \(0<u<v<\infty\),

\[
\frac{
\#\{C:uR\le\ell(C)\le vR\}
}{
W(n)
}
\longrightarrow
e^{-2u^2}-e^{-2v^2}>0.
\tag{6.2}
\]

#### Proof

Uniformly for \(\ell=x\sqrt n\) in a fixed positive compact interval,
Stirling's formula and (6.1) give

\[
\frac{a_n(\ell)}{W(n)}
=\frac{2x}{\sqrt n}e^{-x^2/2}+o(n^{-1/2}).
\]

The allowed heights have spacing two. Since \(R=2\sqrt n\), the resulting
Riemann sum over \(\ell/R\in[u,v]\) is (6.2). \(\square\)

Select product boxes whose first three heights lie in

\[
[0.1R,0.2R]
\]

and whose fourth height lies in

\[
[0.7R,0.8R].
\]

By Lemma 6.1, these form a fixed positive fraction of all product boxes.
Every selected box satisfies

\[
\ell_4-(\ell_1+\ell_2+\ell_3)\ge0.1R,
\qquad
V_{\rm box}\ge0.001R^3.
\]

The flat bound (0.2) therefore gives local excess at least

\[
\left(1-o(1)\right)
\frac{0.001R^3\cdot0.1R}{2\cdot0.8R}
=\left(1-o(1)\right)\frac{R^3}{16000}.
\tag{6.3}
\]

The number of product boxes is \(W(n)^4\), and central-binomial
asymptotics give

\[
W(n)^4R^3=\Theta(W(N)).
\tag{6.4}
\]

Widths add exactly over the product boxes:

\[
\sum_{\mathcal B}w_4(\mathcal B)=W(N).
\tag{6.5}
\]

Let

\[
\mathcal L_{\rm sep}(N)
=\sum_{\mathcal B}\bigl(g_4(\mathcal B)+1\bigr)-1
\]

be the fully anchored length obtained by paying independently for one local
word per box; the subtraction removes the unnecessary anchor in the unique
box whose common minimum is the global zero. Equations (6.2)--(6.5) imply
that some absolute
\(\kappa>0\) satisfies

\[
\boxed{
\mathcal L_{\rm sep}(N)\ge(1+\kappa)W(N)
}
\tag{6.6}
\]

for all sufficiently large \(N\) divisible by four.

The positive constant does not come from the anchors. After decreasing
\(\kappa\), the same bound holds for \(\sum_{\mathcal B}g_4(\mathcal B)\):
all nondegenerate boxes satisfy \(g_4\ge w_4\), while the all-zero boxes
have total count \(o(W(N))\).

Thus:

1. CB4 is false.
2. Its Gaussian-averaged replacement with \(o(R^3)\) expected local excess
   is also false.
3. Every balanced four-block SCD implementation which concatenates
   separately universal local box words has fixed relative overhead.

The boundary cone \(s=P\) alone has zero limiting height-distribution mass.
The strict dominant cone in (0.2) has positive volume and is what makes
(6.6) a global aggregation obstruction.

The same argument works for any fixed positive-proportion four-block split.

---

## 7. What cross-box sharing would have to do

The local lower bound does not prohibit a global word from serving many
product boxes simultaneously. Two exact incidence ledgers quantify this
escape.

### 7.1 Letter activity

For a factor chain

\[
C_0\subset C_1\subset\cdots\subset C_h,
\qquad
C_j=C_0\cup\{e_1,\ldots,e_j\},
\]

define

\[
\pi_C(Y)=\max\bigl(\{j:e_j\in Y\}\cup\{0\}\bigr).
\]

Apply the four coordinate projections to each global Boolean letter.
Projection commutes with union. If a global interval witnesses a nonzero
local target, at least one projected letter in that interval is nonzero;
after filtering zero projections, its surviving indices remain consecutive.
Thus a global word covering the box becomes a local range-maximum word.

If \(d_j\) is the number of product boxes in which global letter \(j\) has
nonzero projection, then

\[
\sum_jd_j\ge\sum_{\mathcal B}g_4(\mathcal B).
\tag{7.1}
\]

The positive-density family above makes the right side

\[
W(N)+\Omega(W(N)).
\tag{7.2}
\]

Here the only possible deficit from summing \(g_4-w_4\) occurs for the
all-zero local box. The number of such product boxes is
\(o(W(N))\), since the proportion of height-zero chains in one block is
\(O(1/n)\), so the all-zero-height box fraction is \(O(n^{-4})\). Thus it
cannot absorb the selected \(\Omega(W(N))\) excess.

Thus a word of length \(W(N)+o(W(N))\) would need

\[
\sum_j(d_j-1)_+=\Omega(W(N)).
\tag{7.3}
\]

Up to the harmless positions with \(d_j=0\), this is exact double counting.

### 7.2 Endpoint activity

For a dominant product box with width \(w\), long height \(s\), and
\(H=s-P\), choose global witnesses for all its plateau targets. Let
\(C_L,C_R\) be the numbers of distinct physical left and right endpoints
used. The flat proof applies even when the intervals leave the box:

\[
\boxed{
(C_L-w)+(C_R-w)\ge\frac{wH}{s}.
}
\tag{7.4}
\]

Select middle-layer witnesses for the remaining product boxes. If
\(\ell_j\) and \(r_j\) count how many boxes use physical position \(j\) as
a left or right endpoint, then the same positive-density family gives

\[
\sum_j\bigl((\ell_j-1)_++(r_j-1)_+\bigr)
\ge
\Omega(W(N))-2\bigl(n_{\rm word}-W(N)\bigr).
\tag{7.5}
\]

Hence any width-scale global word must realize \(\Omega(W(N))\) units of
letter-box or endpoint-box sharing. A sublinear set of portal positions of
uniformly bounded box degree cannot amortize the gap.

This is a repair-capacity theorem, not a global impossibility theorem.
Positions of unbounded box degree, genuinely global corridors, abandonment
of the fixed product partition, or a growing number of blocks remain
possible escapes.

---

## 8. Adversarial audit

The following failure modes were checked independently.

1. **Witness choice.** The same arbitrary chosen interval supplies both
   endpoint partitions. No canonical or shortest witness is assumed.
2. **Orthogonality.** A target-poset vertical edge cannot occur in both
   partitions because that would give two common targets to one left class
   and one right class.
3. **Rank skips.** Meeting two adjacent ranks already forces a genuine
   cover. Other skips only contribute nonnegative potential.
4. **Shoulder truncation.** The condition
   \(k\le\min(p,q,r)\) makes every tetrahedral corner count exact.
5. **Boundary-potential sign.** The bottom omits high-\(\phi\) points and
   the top omits low-\(\phi\) points, giving
   \(\Delta_\phi=PF-2S\).
6. **Chain-count substitution.** The coefficient of \(C_L+C_R\) in
   (3.12) is negative, so replacing it by the upper bound \(2n\) has the
   direction used in (3.13).
7. **Finite integrality.** The denominator \(2(s+2k)\) is positive; the
   positive part and ceiling in (3.16) are necessary for negative small-box
   numerators.
8. **Boundary versus SCD mass.** The sloped theorem closes the local
   boundary \(s=P\), but the separate-box global obstruction uses an open
   strict cone of positive limiting SCD mass.
9. **Aggregation scope.** Equation (6.6) concerns separately paid local
   words. Equations (7.3)--(7.5) identify cross-box sharing as the exact
   remaining escape and do not rule it out.

## 9. Revised four-box target

The compact local target

\[
g_4(\boldsymbol\ell)=w_4(\boldsymbol\ell)+o(R^3)
\]

is impossible, even on the dominant-plateau boundary ray
\((1,1,1,3)\). The
standard four-block independent product aggregation is therefore closed.

The smallest surviving four-block replacement is a cross-parent sharing
theorem:

> Construct one global word whose letters or physical endpoints have
> \(\Omega(W(N))\) total product-box sharing, while keeping total physical
> length \(W(N)+o(W(N))\) and preserving literal uncontaminated witnesses.

No such theorem is proved here. The endpoint dual shows that any successful
fixed-four-block route must be genuinely global rather than a better
standalone four-box construction.
