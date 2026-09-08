# Second-wave S: endpoint-potential duals for the dominant three-box ray

Date: 2026-07-24

## 0. Verdict

Let \(g_3(p,q,r)\) be the least length of a nonzero word of points in

\[
 [0,p]\times[0,q]\times[0,r]
\]

whose contiguous coordinatewise maxima contain every nonzero box point.
The proposed dominant-ray assertion was

\[
 g_3(at,bt,ct)=(at+1)(bt+1)+o_{a,b,c}(t^2),
 \qquad 0<a<b,\quad c>2b.                                  \tag{DRAY}
\]

This assertion is false.  In fact, there is an unrestricted integral dual
obstruction throughout the entire closed width plateau

\[
 c\ge a+b.
\]

The simplest strict-plateau form is already enough to refute every ray in
the stated range.  Put

\[
 1\le p\le q,\qquad P=p+q,\qquad r\ge P,\qquad
 W=(p+1)(q+1).
\]

Then

\[
 \boxed{
 g_3(p,q,r)
 \ge W+\left\lceil\frac{W(r-p-q)}{2r}\right\rceil.}          \tag{0.1}
\]

Consequently, if \(p=at,q=bt,r=ct\) and \(c>a+b\),

\[
 \liminf_{t\to\infty}
 \frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
 \ge \frac{ab(c-a-b)}{2c}>0.                                \tag{0.2}
\]

For the original range \(c>2b\),

\[
 \liminf_{t\to\infty}
 \frac{g_3(at,bt,ct)}{(at+1)(bt+1)}
 \ge1+\frac{c-a-b}{2c}
 >1+\frac{b-a}{4b}.                                         \tag{0.3}
\]

Thus every individual DRAY ray has a positive quadratic excess; the failure
is not confined to an extreme subrange of \(c\).

There is also an exact sloped-band strengthening.  For every integer
\(0\le k\le p\),

\[
\boxed{
g_3(p,q,r)-W
\ge
\max\!\left\{
0,
\left\lceil
\frac{
(r-P+2k)W+\dfrac{k(k+1)(k-6P-4)}3
}{2(r+2k)}
\right\rceil
\right\}.}                                                  \tag{0.4}
\]

At the boundary \(r=P\), choosing \(k\) proportional to \(t\) makes the
right side \(\Omega(t^2)\).  More precisely, for every fixed
\(0<a\le b\),

\[
 g_3(at,bt,(a+b)t)
 \ge(at+1)(bt+1)+\Omega_{a,b}(t^2).                          \tag{0.5}
\]

A logically independent literal-witness obstruction has also been
audited.  Let \(0<p<q\), \(r>p+q\), \(M=(p+1)(q+1)\), and define

\[
 h=\left\lfloor\frac{p+q+r}{2}\right\rfloor,
 \quad \varepsilon=p+q+r-2h,
 \quad s_0=p+q+2,
\]

\[
 K=2\left\lfloor\frac{M}{2s_0}\right\rfloor,
 \qquad
 B=s_0+\left\lceil\frac{M-Ks_0}{K}\right\rceil .
\]

When \(K\ge2\), every word of length \(M+D\) satisfies, whenever the
numerator is positive,

\[
 \boxed{
 D\ge
 \left\lceil
 \frac{M((r-\varepsilon)/2-q)-1}{h-1+2B}
 \right\rceil .}                                           \tag{0.6}
\]

Consequently, on every fixed integral DRAY ray, with
\(D=g_3(at,bt,ct)-(at+1)(bt+1)\),

\[
 \liminf_{t\to\infty}\frac{D}{t^2}
 \ge \frac{ab(c-2b)}{c+5a+5b}.                              \tag{0.7}
\]

Combining the independent certificates proved in Sections 4 and 5A gives
the strongest bound established in this report:

\[
 \boxed{
 \liminf_{t\to\infty}\frac{D}{t^2}
 \ge
 \max\!\left\{
 \max_{0\le x\le a}\Gamma_{a,b,c}(x),
 \frac{ab(c-2b)}{c+5a+5b}
 \right\}.}                                                 \tag{0.8}
\]

The second term is to be used in its proved range \(0<a<b,\ c>2b\).
It tends to \(ab\) as \(c\to\infty\), whereas the endpoint-potential
functional tends uniformly to \(ab/2\); thus neither proof quantitatively
subsumes the other.

Hence \(c=a+b\) is the exact threshold at which
\((at+1)(bt+1)\) becomes the box width, but it is not a validity threshold
for a width-plus-subquadratic theorem: the quadratic obstruction is already
present at that boundary and persists above it.

The factor \(2b\) is not the width or validity threshold.  It is selected
by the outer-hook recursion, and it is also exactly where the numerator in
the independent rank-capped-start/short-mesh certificate (0.7) becomes
positive.  The conditional implication from DRAY to the global
contiguous-OR theorem remains formally correct, but its antecedent is now
proved impossible.  This closes the DRAY and uniform compact three-box
product routes.  It does not disprove the global contiguous-OR conjecture,
because those product reductions were only sufficient.

No web search and no finite or computational search were used.  The
endpoint-potential calculation was independently reconstructed and
adversarially audited three times.  The ordered-witness corridor proof was
independently audited twice.  No unproved lemma remains in (0.1), (0.4), or
(0.6).

## 1. Exact normalization and the width threshold

By coordinatewise closure, one may take every word entry to be a nonzero
box point.  Thus a word is a sequence

\[
 v_i=(x_i,y_i,z_i)
\]

and a target \(T\) is witnessed by an interval \(I\) precisely when

\[
 T=\max_{i\in I}v_i
\]

coordinatewise.  This is the exact range-maximum normal form.

Assume \(p\le q\le r\) and put \(P=p+q\).  Projection to the first two
coordinates shows that every antichain has size at most

\[
 W=(p+1)(q+1),                                               \tag{1.1}
\]

because two points in the same vertical \((x,y)\)-column are comparable.
The product of three chains has a symmetric-chain decomposition, so its
width is its largest rank coefficient.
If \(r\ge P\), every rank

\[
 P,P+1,\ldots,r
\]

contains exactly one point above every \((x,y)\), namely

\[
 (x,y,s-x-y).
\]

Therefore

\[
 \boxed{w_3(p,q,r)=W\quad\Longleftrightarrow\quad r\ge p+q.} \tag{1.2}
\]

The reverse implication in (1.2) can be quantified.  Suppose
\(q\le r<P\) and put \(d=P-r\), so \(0<d\le p\).  At a central rank, the
only missing \((x,y)\)-columns form two opposite triangular corners.  If

\[
 d=2h,
\]

then

\[
 w_3(p,q,r)=W-h(h+1),                                        \tag{1.3}
\]

whereas if

\[
 d=2h+1,
\]

then

\[
 w_3(p,q,r)=W-(h+1)^2.                                      \tag{1.4}
\]

Indeed, a rank coefficient counts the pairs \((x,y)\) lying in one
interval of \(r+1\) consecutive values of \(x+y\).  At the central rank,
the omitted lower and upper triangular sums have the sizes in
(1.3)--(1.4), and symmetry/unimodality makes that coefficient maximal.

Along fixed rays with \(c<a+b\) and \(b\le c\), equations
(1.3)--(1.4) give

\[
 w_3(at,bt,ct)
 =\left(ab-\frac{(a+b-c)^2}{4}\right)t^2+O_{a,b,c}(t).       \tag{1.5}
\]

Thus \(c=a+b\), not \(c=2b\), is the exact width phase transition.  The
new obstruction below shows that the numerical equality in DRAY fails on
the full-plateau side of this transition.

## 2. Endpoint chain partitions

The decisive dual uses both endpoints of the selected witnesses.

### Lemma 2.1 — two orthogonal endpoint partitions

Let \(\mathcal T\) be any target family represented by a word of length
\(n\), and choose one witnessing interval

\[
 I_T=[\ell_T,r_T]
\]

for each \(T\in\mathcal T\).  Group targets first by common left endpoint
and then by common right endpoint.  These are two chain partitions
\(\mathcal L,\mathcal R\), each with at most \(n\) chains, and they are
orthogonal: one \(\mathcal L\)-chain and one \(\mathcal R\)-chain share at
most one target.

#### Proof

At a fixed left endpoint, increasing the right endpoint only enlarges the
witness interval, so its coordinatewise maximum only increases.  The
targets with that left endpoint form a chain.  The same argument, extending
to the left at a fixed right endpoint, gives the right chains.

If one left chain and one right chain shared two targets, both targets would
have the same selected interval \([\ell,r]\).  One physical interval has
one fixed maximum, so the targets would be equal.  Hence the two partitions
are orthogonal. \(\square\)

This lemma is stronger than the width argument only when the two partitions
are coupled.  A one-sided target-weight dual cannot yield any excess.

### Lemma 2.2 — every one-sided chain-weight dual collapses to width

Suppose nonnegative target weights \(\lambda_T\) satisfy

\[
 \sum_{T\in C}\lambda_T\le1
\]

for every poset chain \(C\).  Grouping witnesses by left endpoint gives

\[
 \sum_T\lambda_T\le n.
\]

The largest possible value of the left side is exactly the poset width.
Indeed, a partition into \(w\) chains gives the upper bound \(w\), while
the indicator of a maximum antichain attains \(w\).

Thus a pure target-weight/one-endpoint LP cannot see beyond width.  The
quadratic certificate below comes from orthogonality of the two endpoint
partitions and competition for the same physical coordinate-cover edges.

## 3. The flat-plateau endpoint-potential dual

The easiest decisive form of the argument proves (0.1).

Let

\[
 H=r-P.
\]

For \(0\le j\le H\), define the full plateau layer

\[
 \Lambda_j=
 \{(x,y,P+j-x-y):0\le x\le p, 0\le y\le q\}.                \tag{3.1}
\]

Every \(\Lambda_j\) has \(W\) points.  Choose witnesses for all targets in
their union and form the two endpoint chain partitions.  If the word has
length

\[
 n=W+D,
\]

then either endpoint partition has

\[
 C=W+\delta,\qquad 0\le\delta\le D,                         \tag{3.2}
\]

because each full layer is an antichain of size \(W\), while there are at
most \(n\) physical endpoints.

### 3.1 Adjacent-rank cover edges

For one endpoint partition, let \(A_j\) be the set of its chains occupied
by \(\Lambda_j\).  Then

\[
 |A_j|=W.
\]

Since the partition has only \(W+\delta\) chains,

\[
 |A_j\cap A_{j+1}|\ge W-\delta.                              \tag{3.3}
\]

A common chain contains comparable points in consecutive ranks.  Their
rank difference is one, so they form a genuine box-poset cover edge.
Summing (3.3), the partition uses at least

\[
 H(W-\delta)                                                  \tag{3.4}
\]

cover edges inside the plateau slab.  Chains may skip other ranks; this
does not affect (3.3).

### 3.2 The conserved horizontal potential

Put

\[
 \phi(x,y,z)=x+y,\qquad 0\le\phi\le P.                     \tag{3.5}
\]

Exactly \(W\) chains meet the bottom layer \(\Lambda_0\), and exactly
\(W\) meet the top layer \(\Lambda_H\).  Their bottom and top
\(\phi\)-multisets are both

\[
 \{x+y:0\le x\le p, 0\le y\le q\}.
\]

The remaining \(\delta\) chains begin internally and the remaining
\(\delta\) chains end internally.  Therefore

\[
\begin{aligned}
 \sum_{C}\bigl(\phi(\max C)-\phi(\min C)\bigr)
 &=\sum_{\text{internal ends}}\phi
   -\sum_{\text{internal starts}}\phi\\
 &\le P\delta.                                               \tag{3.6}
\end{aligned}
\]

Every adjacent-rank cover which raises \(x\) or \(y\) raises \(\phi\) by
one.  A vertical \(z\)-cover leaves \(\phi\) unchanged, and every skipped
comparison contributes a nonnegative amount to the total telescoping in
(3.6).  Hence at most \(P\delta\) of the covers counted in (3.4) are
horizontal.  At least

\[
 H(W-\delta)-P\delta
 =HW-r\delta                                                   \tag{3.7}
\]

are vertical \(z\)-covers.

### 3.3 Orthogonality and vertical capacity

Here and below a vertical edge means a cover edge between two target points
in the product poset.  It need not be an adjacency of physical word
positions.

The plateau slab has exactly

\[
 WH
\]

vertical cover edges: one for every \((x,y)\)-column and every adjacent
pair of plateau ranks.  A vertical edge cannot lie in both endpoint
partitions.  If it did, its two endpoint targets would belong to the same
left chain and to the same right chain, contradicting Lemma 2.1.

Apply (3.7) to the left and right partitions.  With defects
\(\delta_L,\delta_R\), disjointness gives

\[
 2HW-r(\delta_L+\delta_R)\le WH.
\]

Since \(\delta_L,\delta_R\le D\),

\[
 WH\le r(\delta_L+\delta_R)\le2rD.                           \tag{3.8}
\]

This proves

\[
 D\ge\left\lceil\frac{WH}{2r}\right\rceil,
\]

which is (0.1).

The proof used arbitrary physical witnesses from an arbitrary universal
range-maximum word.  It is not a fixed-row, raster, chain-SCD, or prescribed
order obstruction.

## 4. Exact sloped-band strengthening

The flat plateau has no vertical thickness when \(r=P\).  To audit the
boundary, include the two sloping shoulders of the rank sequence.

Fix an integer

\[
 0\le k\le p
\]

and use every rank from

\[
 P-k\quad\text{through}\quad r+k.                            \tag{4.1}
\]

Put

\[
 J=r-P+2k,\qquad
 F=\frac{k(k+1)}2,\qquad
 G=\frac{k(k+1)(k+2)}3.                                     \tag{4.2}
\]

There are \(J+1\) layers and \(J\) adjacent-rank transitions.

### 4.1 Exact layer and vertical-edge counts

For \(0\le j\le k\), the layer at rank \(P-j\) omits the upper-right
triangle of \((x,y)\)-pairs with complementary sum below \(j\).  The layer
at rank \(r+j\) omits the lower-left triangle with \(x+y<j\).  In either
case its size is

\[
 W-\frac{j(j+1)}2.                                           \tag{4.3}
\]

The first and last layers therefore have common size

\[
 B=W-F.                                                       \tag{4.4}
\]

Since

\[
 2\sum_{j=1}^k\frac{j(j+1)}2
 =\frac{k(k+1)(k+2)}3=G,
\]

the total number of band targets is

\[
 T=(J+1)W-G.                                                  \tag{4.5}
\]

Every one of the \(W\) vertical columns meets the band in one nonempty
contiguous interval.  Hence the exact number of vertical \(z\)-cover edges
in the band is

\[
 A_v=T-W=JW-G.                                                \tag{4.6}
\]

### 4.2 Exact endpoint-potential difference

Let

\[
 S_k=\sum_{u=0}^{k-1}u(u+1)
 =\frac{k(k-1)(k+1)}3.                                      \tag{4.7}
\]

The bottom boundary omits \(F\) upper-right grid points.  Their total
\(\phi=x+y\) mass is \(PF-S_k\).  The top boundary omits the
\(F\) lower-left points, whose total \(\phi\) mass is \(S_k\).  Thus

\[
 \Delta_\phi
 :=\sum_{\rm top}\phi-\sum_{\rm bottom}\phi
 =PF-2S_k.                                                    \tag{4.8}
\]

### 4.3 Covers used by one endpoint partition

Let one endpoint partition use \(C\) chains.  If adjacent band layers have
sizes \(m_i,m_{i+1}\), their occupied chain sets intersect in at least

\[
 m_i+m_{i+1}-C.
\]

Every common chain supplies a genuine rank-one cover.  Summing over all
transitions gives at least

\[
 \sum_{i=0}^{J-1}(m_i+m_{i+1}-C)
 =2T-2B-JC                                                   \tag{4.9}
\]

cover edges.  If an individual intersection lower bound is negative, it is
still a valid lower bound; skipped ranks create no gap in (4.9).

Exactly \(B\) chains start on the bottom boundary and \(B\) end on the top
boundary.  The other \(C-B\) starts and \(C-B\) ends are internal.  By
telescoping \(\phi\) along every chain,

\[
 \sum_C(\phi(\max C)-\phi(\min C))
 \le\Delta_\phi+P(C-B).                                     \tag{4.10}
\]

Therefore the number of horizontal covers in (4.9) is at most the right
side of (4.10), and the number of vertical covers used by this partition is
at least

\[
 2T-2B-\Delta_\phi+PB-(J+P)C.                               \tag{4.11}
\]

### 4.4 Coupling the two endpoint partitions

Let their chain counts be \(C_L,C_R\).  Lemma 2.1 and (4.6) imply

\[
\begin{aligned}
&2\bigl(2T-2B-\Delta_\phi+PB\bigr)
 -(J+P)(C_L+C_R)\\
&\hspace{5cm}\le A_v.                                      \tag{4.12}
\end{aligned}
\]

Both partitions use at most one chain per physical endpoint, so

\[
 C_L+C_R\le2n.
\]

The coefficient of \(C_L+C_R\) in (4.12) is negative.  Consequently
substituting the upper bound \(2n\) has the correct direction and yields

\[
 2\bigl(2T-2B-\Delta_\phi+PB\bigr)
 -2(J+P)n\le A_v.                                            \tag{4.13}
\]

Insert (4.2), (4.4)--(4.8), use \(J+P=r+2k\), and write

\[
 n=W+D.
\]

Direct simplification gives

\[
 2(r+2k)D
 \ge
 (r-P+2k)W+\frac{k(k+1)(k-6P-4)}3.                           \tag{4.14}
\]

Taking the positive part and the integer ceiling proves (0.4).

Every step above is integral.  In particular, no assumption that the
endpoint chains are saturated was made.  Chains that skip band ranks only
make (4.9) and (4.10) more generous.

## 5. Fixed-ray consequences and the sharp threshold audit

Let

\[
 p=at,\qquad q=bt,\qquad r=ct,\qquad s=a+b,
\]

with fixed positive integers \(a\le b\) and \(c\ge s\).  In (0.4), take

\[
 k=\lfloor xt\rfloor,qquad 0\le x\le a.
\]

Dividing by \(t^2\) gives

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
\ge
\max_{0\le x\le a}\Gamma_{a,b,c}(x),}                     \tag{5.1}
\]

where

\[
 \Gamma_{a,b,c}(x)
 =\frac{
 ab(c-s+2x)-2sx^2+x^3/3
 }{2(c+2x)}.                                                  \tag{5.2}
\]

### 5.1 Strict plateau

If \(c>s\), choose \(x=0\).  Then

\[
 \Gamma_{a,b,c}(0)=\frac{ab(c-a-b)}{2c}>0,                  \tag{5.3}
\]

which recovers (0.2).  In particular, \(0<a<b\) and \(c>2b\)
imply

\[
 c-a-b>b-a>0.
\]

This proves the uniform relative separation (0.3) throughout the claimed
DRAY sector.

### 5.2 Width-plateau boundary

Suppose \(c=s=a+b\).  For any sufficiently small fixed \(x>0\),

\[
 \Gamma_{a,b,s}(x)
 =\frac{x(2ab-2sx+x^2/3)}{2(s+2x)}>0.                        \tag{5.4}
\]

One explicit safe choice is

\[
 x_0=\frac{ab}{4s}\le\frac a4.
\]

Since \(ab/s^2\le1/4\), direct substitution gives

\[
 \Gamma_{a,b,s}(x_0)
 \ge\frac{a^2b^2}{6(a+b)^2}.                                \tag{5.5}
\]

Therefore

\[
 \boxed{
 \liminf_{t\to\infty}
 \frac{g_3(at,bt,(a+b)t)-(at+1)(bt+1)}{t^2}
 \ge\frac{a^2b^2}{6(a+b)^2}>0.}                             \tag{5.6}
\]

The constant in (5.6) is only a convenient explicit certificate; optimizing
\(x\) in (5.2) may improve it.

### 5.3 Downward-subbox monotonicity

If

\[
 u\le p,\qquad v\le q,\qquad s\le r,
\]

delete from a universal word every entry not lying in the lower subbox
\([0,u]\times[0,v]\times[0,s]\).  Every witness for a target in that
subbox contains only entries dominated by its target, so its entire interval
survives and remains contiguous.  Hence

\[
 \boxed{g_3(p,q,r)\ge g_3(u,v,s).}                            \tag{5.7}
\]

More sharply, the outer pure-axis targets force distinct deleted literal
entries, giving

\[
 g_3(p,q,r)
 \ge g_3(u,v,s)+(p-u)+(q-v)+(r-s).                            \tag{5.8}
\]

Taking \((u,v,s)=(p,q,p+q)\), (5.6) propagates its quadratic
obstruction to every larger long side.  Conversely, before the obstruction
was known, (5.7) showed that a width-plus-subquadratic theorem on any
cofinal family of long-side coefficients would imply it on the entire
plateau below.  Thus the cutoff \(2b\) could never have been an intrinsic
lower threshold for the local problem.

The exact threshold conclusion is now:

\[
\boxed{
\begin{gathered}
c=a+b\text{ is the onset of the full width plateau,}\\
\text{but every fixed ray on or above that plateau has quadratic excess.}
\end{gathered}}                                               \tag{5.9}
\]

Any surviving local width-plus-subquadratic statement must lie in the
nonplateau sector \(c<a+b\), where its main term is not
\((at+1)(bt+1)\).  This report makes no positive claim in that sector.

## 5A. Independent audit of the ordered-witness corridor theorem

The finite bound (0.6) was supplied independently in
MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md after the endpoint-potential
proof was complete.  This section reconstructs every implication needed
for it.  The audit verdict is **PASS**: there is no invalid
ordered-witness, valley, multipin, or congestion step.

Throughout this section, let \(p,q,r\) be positive integers satisfying

\[
 0<p<q,\qquad r>p+q,
\]

and require all witnessing factors to be nonempty.  Put

\[
 P=p+q,\qquad M=(p+1)(q+1),\qquad
 h=\left\lfloor\frac{P+r}{2}\right\rfloor,\qquad
 \varepsilon=P+r-2h.                                      \tag{F.1}
\]

Let \(N=M+D\) be the length of an arbitrary universal range-maximum word.
For the block argument also put

\[
 s_0=P+2,\qquad
 K=2\left\lfloor\frac{M}{2s_0}\right\rfloor,\qquad
 R=M-Ks_0,                                                  \tag{F.2}
\]

and assume

\[
 K\ge2,
\]

equivalently \(M\ge2s_0\).  This finite-size condition is automatic for all
sufficiently large points on a fixed positive ray.  Finally define

\[
 B=s_0+\left\lceil\frac{R}{K}\right\rceil.                  \tag{F.3}
\]

### 5A.1 The full middle layer and rank-capped starts

The inequalities \(P\le h\le r\) imply that the rank-\(h\) layer is

\[
 \mathcal S_h
 =\{(x,y,h-x-y):0\le x\le p,\ 0\le y\le q\},               \tag{F.4}
\]

and has exactly \(M\) points.  The exact number of nonzero targets of rank
strictly below \(h\) is

\[
\begin{aligned}
 L_{<h}
 &=\sum_{x=0}^{p}\sum_{y=0}^{q}(h-x-y)-1\\
 &=M\left(h-\frac P2\right)-1
 =M\frac{r-\varepsilon}{2}-1.                              \tag{F.5}
\end{aligned}
\]

Choose one witness \(I_i=[\ell_i,r_i]\) for every target
\(T_i\in\mathcal S_h\), ordered by increasing left endpoint.  The left
endpoints are distinct: intervals with the same left endpoint are nested,
whereas two distinct equal-rank maxima are incomparable.  Their right
endpoints are then strictly increasing as well.  Indeed, if
\(\ell_i<\ell_j\) but \(r_i\ge r_j\), then \(I_j\subset I_i\), again making
the two maxima comparable.

The order statistics of \(M\) distinct positions in a word of length
\(M+D\) therefore give

\[
 \ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,                    \tag{F.6}
\]

where

\[
 0\le\alpha_1\le\cdots\le\alpha_M\le D,\qquad
 0\le\beta_1\le\cdots\le\beta_M\le D.                       \tag{F.7}
\]

Write

\[
 d_i=r_i-\ell_i=\beta_i-\alpha_i\ge0.
\]

Now choose one witness for every nonzero target below rank \(h\) and group
them by left endpoint.  At the selected start \(\ell_i\), such a witness
must end before \(r_i\); otherwise it contains \(I_i\), so its maximum
dominates the rank-\(h\) target \(T_i\), impossible for a target of smaller
rank.  There are only \(d_i\) possible earlier endpoints.  Exactly \(D\)
word positions are not among the selected starts.  At any one of those
starts, the distinct maxima obtained by increasing the right endpoint form
a strict chain and can occupy at most the nonzero ranks
\(1,\ldots,h-1\).  Hence

\[
 \boxed{
 L_{<h}\le\sum_{i=1}^{M}d_i+(h-1)D.}                        \tag{F.8}
\]

No target or witness injectivity beyond the chosen left endpoint is used.

### 5A.2 Valley and short-run audit

For a nonnegative integral sequence \(u_1,\ldots,u_m\), call
\([s,t]\) an internal positive threshold run if, for some integer \(k\ge1\),

\[
 u_i\ge k\ (s\le i\le t),\qquad
 u_{s-1}<k,\qquad u_{t+1}<k,\qquad 1<s\le t<m.              \tag{F.9}
\]

Its edge length is \(t-s\).

If a sequence has no such run, it is valley-shaped.  To see this, choose a
global minimum at \(\tau\).  Any rise before \(\tau\) produces a positive
superlevel component separated from the left end by the lower earlier
value and from the right end by \(u_\tau\).  Any fall after \(\tau\)
produces the symmetric component.  In the absence of either event, the
sequence is nonincreasing through \(\tau\) and nondecreasing afterward.

Suppose \(m\) distinct points of \(\mathcal S_h\) have all three coordinate
sequences valley-shaped.  Order the three valley turns as
\(\tau_X\le\tau_Y\le\tau_Z\).  Before \(\tau_X\), all coordinates are
nonincreasing; constant coordinate sum and distinctness force
\(\tau_X=1\).  Similarly \(\tau_Z=m\).  From \(\tau_X\) to \(\tau_Y\),
\(X\) strictly increases at every step, and from \(\tau_Y\) to
\(\tau_Z\), \(Z\) strictly decreases at every step.  Therefore

\[
\begin{aligned}
 m-1
 &\le X_{\tau_Y}-X_{\tau_X}
     +Z_{\tau_Y}-Z_{\tau_Z}\\
 &=h-Y_{\tau_Y}-X_{\tau_X}-Z_{\tau_Z}
 \le p+q.                                                   \tag{F.10}
\end{aligned}
\]

The last inequality uses that the three coordinatewise lower bounds on
\(\mathcal S_h\), in any relabeling, sum to \(h-p-q\).

Consequently every ordering of \(P+2\) distinct middle targets has an
internal positive coordinate-threshold run.  Inside any such run, take a
maximal consecutive plateau at the maximum coordinate value achieved on
the run.  Its two immediate neighbors are strictly lower, so it remains an
internal run at that exact positive threshold.  An \(x\)-fiber contains
\(q+1\) middle points, a \(y\)-fiber contains \(p+1\), and a \(z\)-fiber
contains at most \(p+1\).  Since \(p<q\), the plateau has at most \(q+1\)
indices.  Thus every ordering of \(s_0=P+2\) middle targets contains an
internal run \([u,v]\) with

\[
 \boxed{v-u\le q.}                                         \tag{F.11}
\]

This is the only source of the \(q\)-mesh, and hence of the positivity
threshold \(c>2b\), in this proof.

### 5A.3 Literal multipin gap

Fix the coordinate and threshold producing a run \([u,v]\), and write
\(b_i=1\) when \(T_i\) is at or above that threshold.  Choose one physical
word position \(s\in I_u\) at which the coordinate reaches the threshold.
The negative witness \(I_{u-1}\) contains no such position.  Because
\(s\ge\ell_u>\ell_{u-1}\), this forces \(s>r_{u-1}\).  Likewise
\(I_{v+1}\) is negative; since \(s\le r_u<r_{v+1}\), it forces
\(s<\ell_{v+1}\).  Integrality yields

\[
 r_{u-1}+2\le\ell_{v+1},
\qquad
 \boxed{\beta_{u-1}-\alpha_{v+1}\le v-u.}                  \tag{F.12}
\]

Only one literal occurrence in one positive witness was used.  Other
positive witnesses may use different pins, the threshold may occur at
arbitrarily many word positions, and different block runs may reuse a pin.
No common-pin or run-factorability assertion occurs.

Combining (F.11), (F.12), and the monotonicity in (F.7) gives

\[
 d_i\le q+\alpha_{v+1}-\alpha_i\quad(i<u),\qquad
 d_i\le q+\beta_i-\beta_{u-1}\quad(i>v).                    \tag{F.13}
\]

### 5A.4 Block-pair congestion

By (F.2), \(0\le R<2s_0\), and \(K\) is even.  Partition the ordered \(M\)
middle targets into \(K\) consecutive blocks, distributing the \(R\)
excess indices as evenly as possible.  Every block has size between
\(s_0\) and \(B\).  In the first \(s_0\) points of each block, choose the
run supplied by (F.11).  Both negative neighbors remain inside that
subblock, so the run is also internal in the full middle ordering.

Pair consecutive blocks.  Write one pair as

\[
 C=[a_0,b_0],\qquad C'=[b_0+1,c_0].
\]

Assign all indices of \(C\) to the run \([u',v']\) in \(C'\).  They lie
before that run, so the first inequality in (F.13) gives

\[
\begin{aligned}
 \sum_{i\in C}d_i
 &\le q|C|+\sum_{i\in C}
          (\alpha_{v'+1}-\alpha_i)\\
 &\le q|C|+B(\alpha_{c_0}-\alpha_{a_0}).                    \tag{F.14}
\end{aligned}
\]

Assign all indices of \(C'\) to the run \([u,v]\) in \(C\).  They lie
after that run, and the second inequality in (F.13) gives

\[
 \sum_{i\in C'}d_i
 \le q|C'|+B(\beta_{c_0}-\beta_{a_0}).                      \tag{F.15}
\]

The index spans of different block pairs are disjoint.  Since
\(\alpha,\beta\) are nondecreasing and lie in \([0,D]\),

\[
 \sum_{\rm pairs}(\alpha_{c_0}-\alpha_{a_0})\le D,\qquad
 \sum_{\rm pairs}(\beta_{c_0}-\beta_{a_0})\le D.            \tag{F.16}
\]

This is the entire congestion argument.  It charges monotone endpoint
increments, not physical pins, so overlapping witnesses and repeated pins
cannot be overcounted.  Summing (F.14)--(F.16) proves

\[
 \boxed{\sum_{i=1}^{M}d_i\le qM+2BD.}                       \tag{F.17}
\]

Finally, insert (F.5) and (F.17) into (F.8):

\[
 M\frac{r-\varepsilon}{2}-1
 \le qM+(h-1+2B)D.
\]

Solving and using integrality of \(D\) proves (0.6).

### 5A.5 Ray constant and comparison with the endpoint dual

For \(p=at,q=bt,r=ct\), with fixed positive integers
\(0<a<b\) and \(c>2b\),

\[
 \frac{M}{t^2}\to ab,\qquad
 \frac ht\to\frac{a+b+c}{2},\qquad
 \frac Bt\to a+b.
\]

Thus (0.6) gives exactly (0.7).

For comparison, let

\[
 e=\frac{ab(c-a-b)}{2c},
\qquad
 f=\frac{ab(c-2b)}{c+5a+5b}.
\]

These are the flat endpoint coefficient and the corridor coefficient.
On \(c>2b\), the sign of \(f-e\) is the sign of

\[
 Q(c)=c^2-4(a+2b)c+5(a+b)^2.
\]

The smaller root of \(Q\) lies below \(2b\), because

\[
 (-a^2+6ab+11b^2)-4(a+b)^2
 =(b-a)(7b+5a)>0.
\]

Hence the unique crossover in the DRAY range is

\[
 c_*=2a+4b+\sqrt{-a^2+6ab+11b^2}.                           \tag{F.18}
\]

The flat endpoint bound is larger for \(2b<c<c_*\), and the corridor
bound is larger for \(c>c_*\).  The optimized sloped-band functional
\(\max_x\Gamma(x)\) can improve the first of these two terms, so (F.18)
is not asserted to be the crossover of the fully optimized bound.
Nevertheless \(f\to ab\), while \(\max_x\Gamma(x)\to ab/2\) as
\(c\to\infty\); the corridor proof supplies a genuine far-dominant
quantitative improvement.

## 6. Companion duals and why they were insufficient

The endpoint-potential obstruction is not visible in the standard scalar
tests.  Their exact outcomes help identify the new ingredient.

### 6.1 Plateau rank-slack is only linear

For every plateau rank \(P\le s\le r\), the layer size is \(W\), and the
number of nonzero targets below it is exactly

\[
 L_s=W\left(s-\frac P2\right)-1.                            \tag{6.1}
\]

Indeed, for every \((x,y)\), there are \(s-x-y\) admissible values of
\(z\) below rank \(s\), and the global zero target is then removed.

The box rank-slack theorem applied at \(s=r\) says that a word of length
\(W+D\) must satisfy

\[
 DW+\binom{D+1}{2}
 \ge W\left(r-\frac P2\right)-1.                            \tag{6.2}
\]

On a fixed ray this yields only

\[
 D\ge\left(c-\frac{a+b}{2}\right)t-O_{a,b,c}(1).             \tag{6.3}
\]

This is a genuine necessary boundary term and shows that an
\(o(t)\)-error claim is impossible.  It is nevertheless compatible with
\(o(t^2)\), so rank slack alone cannot detect the failure of DRAY.

### 6.2 Subbox width plus outer axes is also only linear

Equation (5.8) and the width lower bound give, for every lower subbox,

\[
 g_3(p,q,r)
 \ge w_3(u,v,s)+(p-u)+(q-v)+(r-s).                            \tag{6.4}
\]

Taking \((u,v,s)=(p,q,P)\) gives only

\[
 g_3(p,q,r)\ge W+r-P.                                       \tag{6.5}
\]

Optimizing (6.4) over a single threshold box does not produce a quadratic
excess.  The same retained positions can serve nested lower boxes, so their
costs cannot be summed independently.

### 6.3 Scalar interval count is below width scale

There are \(W\) targets at each of \(r-P+1\) plateau ranks.  Merely assigning
distinct intervals gives

\[
 \binom{n+1}{2}\ge W(r-P+1),                                \tag{6.6}
\]

which is only \(n=\Omega(t^{3/2})\) on a fixed ray.  It is dominated by
the width lower bound \(n\ge W=\Theta(t^2)\).

### 6.4 The decisive extra datum

One endpoint alone sees only a chain cover and hence only width.  Rank
counts see only the number of available short intervals.  The new dual
retains simultaneously:

1. both endpoint chain partitions;
2. their orthogonality;
3. the conserved transverse potential \(x+y\); and
4. the finite supply of long-coordinate cover edges.

The potential forces every near-width endpoint partition to consume many
of the same vertical edges.  Orthogonality forbids the two partitions from
sharing any such edge.  This is the missing two-sided collision inequality
that the scalar and one-endpoint duals discard.

## 7. Implication scope

The proved logical consequences are:

\[
 \boxed{\text{DRAY is false for every one of its stated rays.}}          \tag{7.1}
\]

and, more strongly,

\[
 \boxed{
 c\ge a+b
 \quad\Longrightarrow\quad
 g_3(at,bt,ct)
 \ge w_3(at,bt,ct)+\Omega_{a,b,c}(t^2).}                    \tag{7.2}
\]

The exact logical wording matters.  The fixed-ray equality RAY fails on
every integral ray in the stated DRAY sector (indeed, on every ray in the
closed width plateau).  DRAY is the conjunction of those fixed-ray
statements, so it is false.  CB is a single compact-uniform assertion, not a
predicate that separately “fails on each ray”; since CB implies RAY on
every primitive positive integral ray, any one of the displayed ray
failures refutes CB.

Consequently:

- the proposed dominant-ray sufficient gate cannot be used to prove the
  contiguous-OR width conjecture;
- the uniform compact three-box hypothesis
  \(g_3=w_3+o(R^2)\) is false, because its raywise consequence includes
  these plateau rays;
- the outer-hook theorem “DRAY implies a width-plus-\(o(R^3)\) four-box
  theorem” may remain a correct conditional implication, but its antecedent
  is impossible;
- the factor \(2\) in the hook children is not a local feasibility
  threshold; and
- a positive product-box strategy must change the local main term, avoid
  three-box plateau children, fuse their excess across parents, or work in a
  different geometry.

There is also a concrete architecture-level consequence for the prescribed
outer-hook recursion that always pairs the two largest sides.  Starting
from the balanced four-box \((R,R,R,R)\), it emits a child

\[
 (r,r,2r)
\]

once for every \(r=R,R-1,\ldots,1\).  Equation (5.6) with \(a=b=1\)
gives a sequence \(\eta_r\to0\) such that

\[
 g_3(r,r,2r)-(r+1)^2
 \ge\left(\frac1{24}-\eta_r\right)r^2.
\]

Therefore any implementation of that recursion which realizes each child
by a separate three-box word and concatenates the child words has total
local excess at least

\[
 \sum_{r=1}^{R}\left(\frac1{24}-\eta_r\right)r^2
 =\left(\frac1{72}-o(1)\right)R^3.                          \tag{7.3}
\]

Thus the prescribed separately concatenated outer-hook architecture itself
cannot yield a width-plus-\(o(R^3)\) four-box word.  This statement is
deliberately narrower than a lower bound for \(g_4\): an unrestricted
four-box word may fuse witnesses across child boundaries and need not
decompose into independent child words.

The theorem does **not** imply a stronger lower bound for unrestricted
Boolean contiguous-OR words.  Product-box aggregation says that good local
three-box words would be sufficient globally; it does not say that every
global word decomposes into those boxes.  Nor does this argument concern
MWB, exact middle wreath factors, or labelled common-owner synchronization.

## 8. Audit ledger

### Unconditional theorems proved here

- the exact width threshold and the deficit formulas (1.2)--(1.4);
- the two orthogonal endpoint partitions, Lemma 2.1;
- collapse of every one-sided chain-weight dual to width, Lemma 2.2;
- the strict-plateau lower bound (0.1);
- the exact sloped-band lower bound (0.4);
- the independently audited ordered-witness corridor bound (0.6);
- the combined ray coefficient (0.8);
- the fixed-ray lower functional (5.1)--(5.2);
- positive quadratic excess at the boundary \(c=a+b\), equation (5.6);
- positive quadratic excess on the entire closed plateau, equation (7.2);
- the exact plateau rank-slack count (6.1)--(6.3);
- lower-subbox monotonicity and its outer-axis strengthening
  (5.7)--(5.8); and
- the cubic local-excess obstruction (7.3) for separately concatenating the
  prescribed balanced outer-hook children.

### Refuted assertions

- DRAY for \(0<a<b,c>2b\);
- the claim that the stated dominant sector is a plausible unresolved local
  width theorem;
- any interpretation of \(2b\) as the intrinsic three-box threshold; and
- the uniform compact three-box estimate across all fixed aspect ratios.

### Still open after this obstruction

- sharp asymptotics of \(g_3(at,bt,ct)\) in the plateau sector beyond the
  lower constants in (5.1);
- numerical or width-relative asymptotics in the nonplateau sector
  \(c<a+b\);
- whether a four-box construction can fuse or amortize the unavoidable
  three-box plateau excess rather than summing local words independently;
- every unrelated literal-word, exact-factor, MWB, and labelled
  synchronization route; and
- the global contiguous-OR width conjecture itself.

The decisive conclusion is exact:

\[
\boxed{
\begin{gathered}
\text{The primitive dominant-ray three-box gate is closed.}\\
\text{Every full-plateau ray has a positive quadratic endpoint-potential
obstruction.}
\end{gathered}}
\]
