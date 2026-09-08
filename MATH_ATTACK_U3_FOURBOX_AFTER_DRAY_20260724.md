# Third-wave U: four-box fusion after the three-box quadratic gap

Date: 2026-07-25

## 1. Verdict

The now-proved quadratic three-box gap changes the four-box hook route
decisively, but it does not by itself disprove compact four-box fusion.

There are three distinct statements.

1. **Isolated hook children necessarily have cubic aggregate excess.**
   For every compact-balanced four-box parent, the exact largest-pair
   outer-hook drain has
   \[
   \sum_j E_3(C_j)=\Omega(R^3),
   \qquad
   E_3=(g_3-w_3)_+.
   \tag{1.1}
   \]
   This includes the exact diagonal parent.  For
   \((R,R,R,R)\), a completely explicit bound is
   \[
   \sum_jE_3(C_j)
   \ge
   \frac{2\gamma_*}{3}R^3-O(R^2),
   \qquad
   \gamma_*>\frac{91}{1800}>\frac1{20}.
   \tag{1.2}
   \]
   Hence every implementation that pays for the children separately has a
   positive cubic excess.  The earlier \(1/72\) certificate, which charged
   only one of the two alternating child families, is valid but not sharp
   for this drain.

2. **The cubic bill survives arbitrary crossing witnesses as an incidence
   bill.**  Every translated hook child has an exact join-homomorphic
   projection from the parent.  Thus any parent word projects to a valid
   local word in every child.  Summing gives an exact letter--child activity
   ledger.  Independently, the sloped-band endpoint dual uses only the
   target order and physical interval endpoints, so it remains valid when
   witnesses use foreign letters and cross every child seam.  A parent word
   of length \(w_4+o(R^3)\) would therefore need
   \[
   \Omega(R^3)
   \]
   cross-child activity incidences and useful shared-endpoint incidences.

3. **Incidence is not length.**  One position may have nonzero projection
   in \(\Theta(R)\) hook children, and adjacent complementary shells have
   \(\Theta(R^2)\) literal comparable seam pairs.  This is enough raw
   capacity to pay the dual bill.  Hook additivity is genuinely false:
   an exact thin family below saves \(\lfloor c/2\rfloor+1\) letters by
   crossing the hook seam.  Consequently the local three-box theorem and
   the present incidence ledgers do not by themselves establish
   \[
   g_4(R,R,R,R)\ge w_4(R,R,R,R)+\Omega(R^3).
   \]

The exact conclusion is therefore:

\[
\boxed{
\begin{gathered}
\text{separate child service is impossible at constant one;}\\
\text{sparse or bounded-capacity seam repair is also impossible;}\\
\text{dense surface-scale cross-child fusion remains open.}
\end{gathered}}
\tag{1.3}
\]

In particular, adjacent-packet fusion (APF) is not refuted.  It must,
however, share \(\Theta(R^2)\) positions and endpoints in every typical
bad adjacent pair; an \(O(R)\)-length connector cannot work.  No compact
APF, reset-free whole-surface chronology, or unconditional compact
four-box theorem is proved here.

All arguments are integral and literal.  No web search, finite search, or
computation is used.

## 2. Exact inputs

Let
\[
P_h(u)=1+u+\cdots+u^h.
\]
For a \(d\)-chain box, \(g_d\) is the minimum length of a nonzero word
whose contiguous coordinatewise maxima cover every nonzero point, and
\(w_d\) is its width.  Put
\[
E_d(\boldsymbol\ell)
=\bigl(g_d(\boldsymbol\ell)-w_d(\boldsymbol\ell)\bigr)_+.
\tag{2.1}
\]
The positive part matters only for the all-zero abstract box.

### 2.1 Exact outer-hook drain

The literal identity
\[
P_rP_s=P_{r+s}+uP_{r-1}P_{s-1}
\tag{2.2}
\]
decomposes a rectangle into a saturated outer hook and a rank-one
translated residual rectangle.

At every residual four-box, sort the actual chain-segment heights
\[
h_1\le h_2\le h_3\le h_4,
\]
emit
\[
C_j=(x_j,y_j,z_j)=(h_1,h_2,h_3+h_4),
\tag{2.3}
\]
decrement \(h_3,h_4\), retain the forced translation, and re-sort the
actual segments.  Then
\[
z_j\ge2y_j\ge x_j+y_j,
\tag{2.4}
\]
\[
\prod_{i=1}^4P_{\ell_i}(u)
=\sum_j u^jP_{x_j}(u)P_{y_j}(u)P_{z_j}(u),
\tag{2.5}
\]
and
\[
\boxed{w_4(\boldsymbol\ell)=\sum_jw_3(C_j).}
\tag{2.6}
\]
Thus every nondegenerate child lies on or above the full-width
three-box plateau.

### 2.2 The finite sloped-band gap

The new unconditional three-box theorem states the following.  For
\[
1\le p\le q,\qquad r\ge p+q,\qquad 0\le k\le p,
\]
put
\[
W=(p+1)(q+1)
\tag{2.7}
\]
and
\[
N_k(p,q,r)
=(r-p-q+2k)W
+\frac{k(k+1)(k-6(p+q)-4)}3.
\tag{2.8}
\]
Then
\[
\boxed{
E_3(p,q,r)
\ge
\max\left\{
0,
\left\lceil
\frac{N_k(p,q,r)}{2(r+2k)}
\right\rceil
\right\}.}
\tag{2.9}
\]
No architecture or common-pin assumption occurs in (2.9).

Downward-subbox monotonicity gives
\[
g_3(p,q,r)\ge g_3(p,q,p+q).
\tag{2.10}
\]
The two boxes in (2.10) have the same plateau width \(W\).  Hence every
longer plateau side inherits the boundary gap.

## 3. A uniform local constant

The finite formula gives a convenient uniform coefficient, not merely a
ray-by-ray \(\Omega\)-statement.

Define
\[
F_\lambda(x)
=
\frac{x\bigl(2\lambda-2(1+\lambda)x+x^2/3\bigr)}
     {2(1+\lambda+2x)},
\qquad
\lambda\ge1,\quad0\le x\le1.
\tag{3.1}
\]
Let \(\xi\in(0,1)\) be the unique root of
\[
2\xi^3-9\xi^2-24\xi+6=0,
\tag{3.2}
\]
and put
\[
\gamma_*
=F_1(\xi)
=\frac{\xi^2-8\xi+2}{4}.
\tag{3.3}
\]
The second equality follows after multiplying by \(4(1+\xi)\): the
difference of the two numerators is one third of the cubic in (3.2).
The cubic in (3.2) is strictly decreasing on \([0,1]\), and its values at
the endpoints are \(6,-25\), so this root is unique.  Direct
differentiation gives
\[
F_1'(x)
=
\frac{2x^3-9x^2-24x+6}{12(1+x)^2},
\]
so \(\xi\) is the unique maximizer of \(F_1\) on \([0,1]\).  Moreover
\[
\gamma_*>F_1(1/5)=\frac{91}{1800}>\frac1{20}.
\tag{3.4}
\]

### Lemma 3.1 (uniform plateau gap — PROVED)

For every integer triple
\[
1\le p\le q,\qquad r\ge p+q,
\]
one has
\[
\boxed{
E_3(p,q,r)
\ge
\gamma_*p^2-\frac{67}{12}p.}
\tag{3.5}
\]

#### Proof

By (2.10), reduce to \(r=p+q\).  Put
\[
\lambda=q/p,\qquad k=\lfloor\xi p\rfloor,\qquad\alpha=k/p.
\]
Dividing the real expression inside (2.9) by \(p^2\) gives exactly
\[
F_\lambda(\alpha)
-\frac{\alpha^2}{2(1+\lambda+2\alpha)p}
+\frac{\alpha}{3(1+\lambda+2\alpha)p^2}.
\tag{3.6}
\]
For fixed \(x\in[0,1]\), direct differentiation gives
\[
\frac{\partial F_\lambda}{\partial\lambda}(x)
=
\frac{x(2+4x-13x^2/3)}
     {2(1+\lambda+2x)^2}\ge0;
\tag{3.7}
\]
the quadratic factor is positive on \([0,1]\).  Hence
\[
F_\lambda(\xi)\ge F_1(\xi)=\gamma_*.
\]
Writing \(s=1+\lambda\ge2\), the other derivative is
\[
\frac{\partial F_\lambda}{\partial x}(x)
=
\frac{2\lambda s-4s^2x-3sx^2+4x^3/3}
     {2(s+2x)^2}.
\tag{3.8}
\]
For \(0\le x\le1\), the absolute value of its numerator is at most
\[
2s^2+4s^2+\frac32s^2+\frac13s^2
=\frac{47}{6}s^2.
\]
Since the denominator is at least \(2s^2\), this proves, in particular,
\[
\left|\frac{\partial}{\partial x}F_\lambda(x)\right|
\le\frac{47}{12}<\frac{16}{3}
\qquad(\lambda\ge1,\ 0\le x\le1).
\]
Since \(|\alpha-\xi|<1/p\), we may use the looser displayed constant
\(16/3\) to obtain
\[
F_\lambda(\alpha)\ge\gamma_*-\frac{16}{3p}.
\]
Also \(1+\lambda+2\alpha\ge2\) and \(0\le\alpha\le1\), so the negative
finite correction in (3.6) is at least \(-1/(4p)\), while the last
correction is nonnegative.  Thus the total normalized loss is at most
\[
\frac1p\left(\frac{16}{3}+\frac14\right)
=\frac{67}{12p}.
\]
Multiplication by \(p^2\), followed by (2.9), proves (3.5).  ∎

The exact constant is not important for the qualitative conclusion, but
it makes every later quantifier and aggregate coefficient explicit.

## 4. The hook drain has unavoidable cubic isolated defect

Let
\[
\mathcal A(\boldsymbol\ell)
=\sum_{C_j\in\mathcal D(\boldsymbol\ell)}E_3(C_j).
\tag{4.1}
\]

### 4.1 Isotonicity of the residual peel

For a sorted four-vector \(v\), let \(T(v)\) be the sorted vector obtained
by decrementing its two largest coordinate entries by one (two coordinates
are decremented, even when their values are equal).  The map \(T\) is
isotone in sorted coordinatewise order.

Here is the exact proof.  For an integer threshold \(t\ge1\), put
\[
n_v(t)=\#\{i:v_i\ge t\},
\qquad
m_v(t)=n_v(t+1).
\]
One peel gives
\[
n_{T(v)}(t)
=
\mathsf F(n_v(t),m_v(t)),
\tag{4.2}
\]
where
\[
\mathsf F(n,m)
=n-\min\{\,n-m,\,(2-m)_+\,\}.
\tag{4.3}
\]
Indeed \(m\) entries are strictly above \(t\); among the top two, exactly
\(\min\{n-m,(2-m)_+\}\) entries equal \(t\) and fall below it.
On \(0\le m\le n\le4\), \(\mathsf F\) is nondecreasing separately in
\(n,m\):

- for \(m\ge2\), \(\mathsf F=n\);
- for \(m=1\), it is \(1\) at \(n=1\) and \(n-1\) for \(n\ge2\);
- for \(m=0\), it is \(\max(n-2,0)\).

Threshold-count dominance is equivalent to sorted coordinatewise
dominance.  Thus \(a\le b\) implies \(T(a)\le T(b)\).

### Theorem 4.1 (uniform aggregate hook gap — PROVED)

Let
\[
L=\min_i\ell_i.
\]
Then the largest-pair outer-hook drain satisfies
\[
\boxed{
\mathcal A(\boldsymbol\ell)
\ge
\gamma_*\frac{2L^3+L}{3}
-\frac{67}{6}L^2.}
\tag{4.4}
\]
Consequently, for every fixed \(\delta>0\) and every integer sequence
\(\boldsymbol\ell(R)\) satisfying \(\min_i\ell_i(R)\ge\delta R\),
\[
\liminf_{R\to\infty}
\frac{\mathcal A(\boldsymbol\ell(R))}{R^3}
\ge
\frac{2\gamma_*}{3}\delta^3.
\tag{4.5}
\]

#### Proof

The initial residual vector dominates \((L,L,L,L)\).  By the isotonicity
above, every later residual dominates the corresponding residual in the
equal-\(L\) drain.

The positive first-short-coordinate sequence in that equal drain is
\[
L,L-1,L-1,L-2,L-2,\ldots,1,1.
\]
Therefore the first \(2L-1\) relevant children of the given drain satisfy
\[
\sum x_j^2
\ge
L^2+2\sum_{r=1}^{L-1}r^2
=\frac{2L^3+L}{3}.
\tag{4.6}
\]
There are fewer than \(2L\) terms and \(x_j\le L\), so
\[
\sum x_j<2L^2.
\tag{4.7}
\]
Every child satisfies \(z_j\ge x_j+y_j\).  Apply Lemma 3.1 only to the
first \(2L-1\) comparison children used in (4.6)-(4.7), and discard every
later nonnegative defect.  Summing (3.5) on those children gives (4.4).
For a sequence in (4.5), the cubic polynomial on the right of (4.4) is
increasing for \(L\ge\delta R\) once \(R\) is large.  Substitute
\(L=\delta R\), divide by \(R^3\), and let \(R\to\infty\) to obtain
(4.5).
∎

Thus the isolated hook bill is cubic for every compact-balanced parent,
including the exact diagonal.  This conclusion no longer depends on the
false DRAY hypothesis.

### 4.2 Exact equal-parent sequence

For \((R,R,R,R)\), the positive children occur in pairs
\[
A_r=(r,r,2r),
\qquad
B_r=(r-1,r-1,2r),
\qquad r=R,R-1,\ldots,1,
\tag{4.8}
\]
followed by the terminal \((0,0,0)\).

For \(r\ge2\), put \(s=r-1\).  The lower subbox
\[
(s,s,2s)=(r-1,r-1,2r-2)
\]
inside \(B_r=(s,s,2s+2)\) has the same plateau width as \(B_r\).  Moreover,
the targets \((0,0,2s+1)\) and \((0,0,2s+2)\) must each occur as a
letter.  From any universal word for \(B_r\), delete every entry outside
\([0,s]^2\times[0,2s]\).  Every witness for a target of this lower subbox
already lies wholly inside the subbox, so all such witnesses survive
compression.  At least the two displayed forced axis occurrences are
deleted.  The retained word is therefore universal for the subbox and has
length at most two less than the original word.  Hence
\[
g_3(s,s,2s+2)\ge g_3(s,s,2s)+2.
\tag{4.9a}
\]
Thus the two extra pure-axis levels strengthen the defect by two.  Also
\[
E_3(0,0,2)=1.
\]
Hence
\[
\boxed{
\mathcal A_R
\ge
\gamma_*\frac{2R^3+R}{3}
-\frac{67}{12}R^2
+2R-1.}
\tag{4.9}
\]

The parent width is exactly
\[
\begin{aligned}
w_4(R,R,R,R)
&=\binom{2R+3}{3}-4\binom{R+2}{3}\\
&=\frac23R^3+2R^2+\frac73R+1.
\end{aligned}
\tag{4.10}
\]
Therefore
\[
\boxed{
\liminf_{R\to\infty}
\frac{\mathcal A_R}{w_4(R,R,R,R)}
\ge\gamma_*>\frac1{20}.}
\tag{4.11}
\]

If every child is realized by its own local word, then
\[
\sum_jg_3(C_j)
\ge w_4+\mathcal A_R-1,
\tag{4.12}
\]
where the \(-1\) is the all-zero terminal child.  Translated-origin anchors
can only increase a separately concatenated construction.  Thus separate
hook concatenation has a positive cubic excess, with leading coefficient
at least \(2\gamma_*/3>91/2700>1/30\).

## 5. Exact letter--child activity ledger

The preceding cubic sum is not automatically a lower bound for a single
word on the whole parent.

### Lemma 5.1 (join projection onto a hook child — PROVED)

Let \(C\) be any translated child emitted by the exact hook drain.  It is
a product of three saturated chains.  For one chain, write its translated
bottom as \(B_0\) and its ordered variable increments as
\[
e_1,e_2,\ldots,e_h.
\]
For any parent point \(X\), define
\[
\pi_C(X)
=\max\bigl(\{t:e_t\in X\}\cup\{0\}\bigr),
\tag{5.1}
\]
ignoring all atoms already present in \(B_0\).  Do this in each of the
three child chains.

Then
\[
\pi_C(X\vee Y)
=\max\{\pi_C(X),\pi_C(Y)\}
\tag{5.2}
\]
coordinatewise, and \(\pi_C\) is the identity in local coordinates on
\(C\).

#### Proof

Membership of an increment atom in \(X\vee Y\) is the logical OR of its
memberships in \(X,Y\), so the largest present increment index is the
maximum of the two largest indices.  A point at local chain coordinate
\(t\) contains exactly the first \(t\) variable increments, proving the
retraction property.  The argument also applies to the outer-hook chain:
its ordered increments are simply the successive atoms along the
saturated hook path.  ∎

### Theorem 5.2 (activity sharing ledger — PROVED)

Let
\[
\mathcal W=(V_1,\ldots,V_n)
\]
be any universal word for the parent.  For position \(i\), let
\[
d_i=\#\{C_j:\pi_{C_j}(V_i)\ne0\}.
\tag{5.3}
\]
Put
\[
Z=\#\{i:d_i=0\},
\qquad
\Sigma_{\rm let}=\sum_i(d_i-1)_+.
\tag{5.4}
\]
Let \(\tau\in\{0,1\}\) indicate whether the terminal child is the all-zero
abstract singleton.  Then
\[
\boxed{
n-w_4(\boldsymbol\ell)
\ge
\mathcal A(\boldsymbol\ell)
-\Sigma_{\rm let}+Z-\tau.}
\tag{5.5}
\]

#### Proof

Fix a child \(C\).  Project every letter of \(\mathcal W\) by \(\pi_C\)
and delete every zero image.  A parent witness for a child target projects,
by (5.2), to the same local target.  Deleting zeros only compresses the
interval, so its retained images remain consecutive.  The projected word
is therefore a valid local word, and
\[
g_3(C)\le\#\{i:\pi_C(V_i)\ne0\}.
\]
Summing over children gives
\[
\sum_Cg_3(C)\le\sum_i d_i=n-Z+\Sigma_{\rm let}.
\tag{5.6}
\]
Exact width telescoping gives \(\sum_Cw_3(C)=w_4\).  Every child raw defect
equals \(E_3(C)\), except that the all-zero terminal contributes \(-1\).
Thus
\[
\sum_Cg_3(C)=w_4+\mathcal A-\tau.
\]
Combine this with (5.6).  ∎

For the equal parent, (4.9) and (5.5) imply
\[
n=w_4+o(R^3)
\quad\Longrightarrow\quad
\Sigma_{\rm let}
\ge
\left(\frac{2\gamma_*}{3}-o(1)\right)R^3.
\tag{5.7}
\]
The local gap has not disappeared: it has become a cubic letter--child
sharing requirement.

### Corollary 5.3 (sparse portal no-go — PROVED)

Suppose only \(P\) word positions have \(d_i\ge2\), and every such position
has
\[
d_i\le D.
\]
Then
\[
\boxed{
n-w_4
\ge
\mathcal A-1+Z-(D-1)P.}
\tag{5.8}
\]
Consequently:

- bounded-degree sharing on \(o(R^3)\) positions cannot give
  \(w_4+o(R^3)\);
- even degree \(D=O(R)\) requires \(P=\Omega(R^2)\);
- one \(O(R)\)-long bounded-degree seam for each of \(O(R)\) child
  boundaries has only \(O(R^2)\) activity capacity and cannot cancel the
  cubic bill.

The degree qualification is essential.  The parent top point, if used as
a letter, has nonzero projection in every nondegenerate drain child, so
degrees of order \(R\) are geometrically available.

## 6. The endpoint dual survives crossing intervals

The letter ledger counts raw activity.  The endpoint ledger counts actual
selected witness service.

For a child
\[
C=(p,q,r),\qquad 1\le p\le q,\quad r\ge p+q,
\]
choose witnesses for the sloped band used in the proof of (2.9).  Let
\(C_L(C)\) and \(C_R(C)\) be the numbers of distinct physical left and
right endpoints among those witnesses.  The witnesses may cross every
child boundary and may use arbitrary foreign letters.

### Lemma 6.1 (translated endpoint certificate — PROVED)

With \(N_k\) as in (2.8),
\[
\boxed{
C_L(C)+C_R(C)-2w_3(C)
\ge
\gamma_k(C),}
\tag{6.1}
\]
where
\[
\gamma_k(C)
=
\max\left\{
0,
\left\lceil
\frac{N_k(p,q,r)}{r+2k}
\right\rceil
\right\}.
\tag{6.2}
\]

#### Proof

Targets with a common left endpoint form a chain under inclusion, as do
targets with a common right endpoint.  The two partitions are orthogonal:
one left chain and one right chain cannot contain two distinct targets,
because that would assign two unions to one physical interval.

The sloped-band proof counts cover edges used by the two endpoint
partitions, telescopes the transverse potential \(x+y\), and uses their
orthogonality.  Before substituting
\[
C_L+C_R\le2n,
\]
its exact inequality is precisely (6.1).  Translation of the child is an
order isomorphism.  No step refers to the locations of the word letters,
only to the child targets and their physical endpoints.  ∎

### Theorem 6.2 (endpoint sharing ledger — PROVED)

For every child with positive first short side choose a band parameter
\(k_j\) and corresponding witnesses.  For every ineligible child
\(p=0\), choose witnesses for all targets in one local middle antichain of
size \(w_3(C_j)\) and assign certificate \(0\); the two endpoint
partitions then contribute the baseline \(2w_3(C_j)\), because one
endpoint class is a target-poset chain and hence meets that antichain at
most once.  A translated
all-zero singleton is a required nonzero parent point in every positive
parent considered here; the wholly zero parent is outside the compact
regime.  At a physical position \(i\), let \(d_i^L,d_i^R\) be the
numbers of selected child target families using \(i\) as a left or right
endpoint.  Put
\[
\Sigma_\partial
=
\sum_i\bigl((d_i^L-1)_++(d_i^R-1)_+\bigr),
\tag{6.3}
\]
and let \(Z_L,Z_R\) count positions unused as selected left or right
endpoints.  With
\[
\Gamma=\sum_j\gamma_{k_j}(C_j),
\tag{6.4}
\]
one has
\[
\boxed{
2(n-w_4)
\ge
\Gamma+Z_L+Z_R-\Sigma_\partial-2\tau_0,}
\tag{6.5}
\]
where \(\tau_0=1\) only when the selected terminal point is the excluded
global zero, and \(\tau_0=0\) otherwise.

#### Proof

Sum (6.1) and use \(\sum_jw_3(C_j)=w_4\).  Double counting gives
\[
\sum_jC_L(C_j)=n-Z_L+\sum_i(d_i^L-1)_+,
\]
and the analogous right-endpoint identity.  Omitting an excluded global
zero removes one baseline chain from each endpoint partition, giving the
displayed \(2\tau_0\) correction.  Rearrangement yields (6.5).
∎

For the equal drain, choosing \(k\sim\xi p\) in both children of every
large pair gives
\[
\Gamma
\ge
\left(\frac{4\gamma_*}{3}-o(1)\right)R^3.
\tag{6.6}
\]
For a simpler rational certificate, \(k=\lfloor p/8\rfloor\) gives
\[
\Gamma
\ge
\left(\frac{289}{5184}-o(1)\right)R^3
>
\left(\frac1{18}-o(1)\right)R^3.
\tag{6.7}
\]
Thus
\[
n=w_4+o(R^3)
\quad\Longrightarrow\quad
\Sigma_\partial=\Omega(R^3).
\tag{6.8}
\]
Crossing witnesses do not erase the endpoint dual; they can only pay it by
reusing physical endpoints across child target families.

For one adjacent bad pair with sides of order \(R\), (5.5) and (6.5)
similarly imply:

> a packet of length \(w_0+w_1+o(R^2)\) must have
> \(\Theta(R^2)\) doubly active positions and shared endpoint incidences.

Hence APF cannot be implemented by an \(o(R^2)\) portal set, in particular
not by an \(O(R)\)-length boundary connector.

## 7. Adjacent complementary shells have enough raw surface capacity

The endpoint ledger does not itself refute APF.

Before the equal-drain pair \(A_r,B_r\), the actual translated residual box
is
\[
Q_r=[R-r,R]\times[0,r]\times[R-r,R]\times[0,r].
\tag{7.1}
\]
The first child hooks coordinates \(3,4\); the next hooks coordinates
\(1,2\).

Fix \(0\le k\le r-1\).  For
\[
-k\le\sigma\le k,\qquad
1\le a\le r,\qquad
0\le v\le r-1,\qquad
a+v=r+\sigma,
\]
put
\[
X=(R-r+a,r,R-r,v)\in A_r
\tag{7.2}
\]
and
\[
Y=X+e_3=(R-r+a,r,R-r+1,v)\in B_r.
\tag{7.3}
\]
Then
\[
X\lessdot Y
\tag{7.4}
\]
is an ambient cover crossing the child seam, and both targets lie in the
corresponding selected sloped bands.

These covers form a matching of exact size
\[
M_r(k)
=r(2k+1)-k(k+1).
\tag{7.5}
\]
Indeed, for a fixed \(\sigma\), there are \(r-|\sigma|\) solutions, and
sum over \(-k\le\sigma\le k\).

Put \(k\sim xr\).  The matching coefficient is
\[
m(x)=2x-x^2.
\tag{7.6}
\]
The endpoint certificate of the two children has coefficient
\[
2e(x),
\qquad
e(x)=
\frac{[\,2x-4x^2+x^3/3\,]_+}{2(1+x)}.
\tag{7.7}
\]
Whenever the numerator is positive,
\[
\boxed{
m(x)-2e(x)
=
\frac{x^2(5-\frac43x)}{1+x}>0.}
\tag{7.8}
\]
Thus even the optimized endpoint certificate is smaller than the available
band-compatible seam matching.

At \(x=1/8\),
\[
m(x)=\frac{15}{64},
\qquad
2e(x)=\frac{289}{1728},
\]
leaving the positive margin
\[
\frac{29}{432}.
\tag{7.9}
\]

This is a capacity theorem, not an APF construction.  The matching can be
split arithmetically between prospective shared-left and shared-right
service, but one still has to expose the chosen seam covers in two
compatible orthogonal endpoint-chain systems and realize all of them in
one uncontaminated literal chronology.

A simpler literal capacity family is also useful.  In unshifted local
coordinates put
\[
H=\{(0,v):0\le v\le r\}
\cup\{(u,r):1\le u\le r\},
\]
\[
I=\{1,\ldots,r\}\times\{0,\ldots,r-1\}.
\]
The pair is
\[
A=[0,r]^2\times H,\qquad B=H\times I.
\tag{7.10}
\]
For every \(h\in H\) and \(0\le v<r\), define
\[
a_{h,v}=(h;0,v)\in A,
\qquad
b_{h,v}=(h;1,v)\in B.
\tag{7.11}
\]
Then \(a_{h,v}\lessdot b_{h,v}\), and the two-letter segment
\[
a_{h,v},b_{h,v}
\]
uses the same physical left endpoint for the singleton \(A\)-target and
the \(B\)-target witnessed by the whole segment.  There are exactly
\[
(2r+1)r=\Theta(r^2)
\tag{7.12}
\]
such literal seam covers.  Surface-order cross-child service is therefore
geometrically real, not merely a dimension count.

## 8. Exact literal nonadditivity: the diamond packet

The smallest hook already disproves any unconditional additivity theorem.
The following one-parameter family shows a leading-order thin saving.

Let
\[
D_c=[0,1]^2\times[0,c],
\]
and write
\[
Z_j=(0,0,j),\quad
X_j=(1,0,j),\quad
Y_j=(0,1,j).
\]

### Theorem 8.1 (diamond packet — PROVED)

For every \(c\ge0\),
\[
\boxed{
g_3(1,1,c)
=c+\left\lceil\frac c2\right\rceil+2.}
\tag{8.1}
\]

The outer-hook decomposition of \([0,1]^2\) has a three-point chain of
edge height \(2\) and the translated singleton \((1,0)\).  After taking
the product with \([0,c]\), separate optimal service costs
\[
(c+2)+(c+1)=2c+3.
\tag{8.2}
\]
Thus literal fusion saves exactly
\[
\boxed{\left\lfloor\frac c2\right\rfloor+1.}
\tag{8.3}
\]

#### Upper construction

For \(c=0\), the word \(X_0,Y_0\) has length \(2\) and is optimal.
Assume below that \(c\ge1\).

First suppose \(c=2m\).  Choose alternating pivots
\[
P_i\in\{X_i,Y_i\},
\qquad1\le i\le m,
\]
ending with \(P_m=Y_m\).  Output
\[
P_1,Z_{m+1},P_2,Z_{m+2},\ldots,P_m,Z_{2m},
\tag{8.4}
\]
then output, in decreasing \(i\), every \(Z_i\) for which \(P_i=Y_i\);
then \(X_0,Y_0\); then, in increasing \(i\), every \(Z_i\) for which
\(P_i=X_i\).  The length is
\[
2m+m+2=3m+2.
\]

If \(c=2m+1\), put \(s=m+1\), choose alternating
\[
P_1,\ldots,P_s,\qquad P_s=Y_s,
\]
and output
\[
P_1,Z_{s+1},P_2,Z_{s+2},\ldots,P_m,Z_{s+m},P_s,
\tag{8.5}
\]
followed by the same decreasing-\(Y\), \(X_0,Y_0\), increasing-\(X\)
low tail.  Its length is
\[
(2m+1)+(m+1)+2=3m+4.
\]

Here is the literal verification.  In the even case, for
\(j=m+i<2m\), the high singleton \(Z_j\) lies between the opposite-colour
pivots \(P_i,P_{i+1}\).  The two adjacent two-letter intervals have maxima
\(X_j,Y_j\), and the three-letter interval has maximum \(T_j=(1,1,j)\).
For \(j=2m\), the terminal high singleton follows \(P_m=Y_m\); the
interval from \(Z_{2m}\) through the decreasing uncoloured tail to
\(X_0\) supplies \(X_{2m}\), while adjoining \(P_m\) supplies
\(T_{2m}\).  The interval \(P_m,Z_{2m}\) supplies \(Y_{2m}\).

In the odd case, every high singleton has the form \(Z_{s+i}\),
\(1\le i\le m\), and lies between the opposite-colour pivots
\(P_i,P_{i+1}\); the same two- and three-letter intervals give its three
coloured targets.

It remains to check a low height \(i\).  If \(P_i=X_i\), then its copy of
\(Z_i\) lies in the increasing tail to the right of \(Y_0\).  The interval
from \(Y_0\) to that copy has maximum \(Y_i\), and adjoining \(X_0\) gives
\(T_i\); \(X_i\) is the pivot singleton.  If \(P_i=Y_i\), its copy of
\(Z_i\) lies in the decreasing tail to the left of \(X_0\).  The interval
from that copy to \(X_0\) has maximum \(X_i\), and adjoining \(Y_0\) gives
\(T_i\); \(Y_i\) is the pivot singleton.  In either tail, every intervening
\(Z\)-height is at most \(i\), so the asserted maxima are exact.  Together
with every \(Z_i\) singleton, these intervals cover all nonzero targets.
Thus the word is universal, and its length is the right side of (8.1).

#### Lower bound

Every word must contain occurrences of
\[
Z_1,\ldots,Z_c,X_0,Y_0.
\tag{8.6}
\]
Write
\[
n=c+2+e.
\]
Write \(T_j=(1,1,j)\).  Call a positive height \(j\) exceptional if
\(Z_j\) is repeated or a letter \(X_j,Y_j\), or \(T_j\) occurs.  There
are at most \(e\) exceptional heights.

For every nonexceptional \(j\), the unique \(Z_j\) lies in both a pure
\(X_j\)-witness and a pure \(Y_j\)-witness.  Their \(X\)- and \(Y\)-colour
providers must occur on opposite sides of \(Z_j\); otherwise the farther
witness contains the wrong colour.  Hence \(Z_j\) occupies a distinct gap
between consecutive opposite-colour positions and is the exact maximum
height in that gap.

Let \(q\) be the number of pure \(X\)- or \(Y\)-coloured positions.  If
the word has no singleton letter \(T_0\), a witness for \((1,1,0)\) must
join opposite pure colours through a gap containing no positive
\(Z\)-letter.  At least one of the \(q-1\) coloured gaps is therefore
unavailable, while \(q\le e+2\); the number of nonexceptional heights is
at most
\[
q-2\le e.
\]
If \(T_0\) occurs, it consumes one of the \(e\) extra positions.  Then
only the weaker gap bound \(q-1\) is needed, but
\[
q\le(e-1)+2=e+1,
\]
so again there are at most \(e\) nonexceptional heights.  Positive
top-colour letters \(T_j\) were already charged as exceptional and cannot
enter either pure \(X_j\)- or pure \(Y_j\)-witness.
Since at most \(e\) heights are exceptional,
\[
c\le2e.
\]
Therefore
\[
n\ge c+2+\lceil c/2\rceil,
\]
matching the construction.  ∎

The diamond is thin: it proves literal nonadditivity and a linear saving,
not the \(R^2\)-per-pair cancellation needed in the compact four-box
problem.

## 9. What is now ruled out

The following consequences are unconditional.

1. **Separate outer-hook concatenation.**  It pays the cubic amount in
   Theorem 4.1, and on the equal parent at least the explicit amount in
   (4.9).

2. **Lower-order seam repair.**  Keeping the child words and adding
   \(o(R^3)\) connectors cannot remove their existing occurrences.

3. **Sparse bounded-degree fusion.**  Formula (5.8) rules it out.

4. **Boundary-length APF.**  A typical adjacent packet has a quadratic
   local bill.  A connector or shared-position set of size \(o(R^2)\)
   cannot pay it.

5. **Endpoint-disjoint crossing.**  Allowing witnesses to cross children
   while giving each child its own endpoint positions still leaves the
   positive cubic lower bound through (6.5).

The following are not ruled out.

1. A pair word with a positive fraction of its \(\Theta(R^2)\) positions
   active in both children.
2. A whole-surface word with \(\Theta(R^2)\) high-degree portals, each
   serving \(\Theta(R)\) children.
3. A direct four-box word not organized by the drain.
4. The Gaussian-averaged fused four-box gate.

## 10. Exact remaining theorem

The natural concrete target remains:

> **Adjacent packet fusion (APF) — UNPROVED.**  For every
> \(0<\delta\le C<\infty\), there is a function
> \(\varepsilon_{\delta,C}(R)\ge0\), tending to \(0\), such that the
> following holds.
> If
> \[
> \delta R\le\ell_i\le CR\qquad(1\le i\le4),
> \]
> then, for every adjacent pair \(C_{2j},C_{2j+1}\) in its translated
> outer-hook drain, construct one literal parent-alphabet packet word
> covering both full embedded child target sets (including a translated
> local origin whenever it is a nonzero parent point) and having length at
> most
> \[
> w_3(C_{2j})+w_3(C_{2j+1})
> +\varepsilon_{\delta,C}(R)R^2.
> \tag{10.1}
> \]

Each peel lowers the sum of the four residual heights by two, so there are
at most \(2CR+1\) children.  The proved alternating-slice
bound
\[
g_3(a,b,c)\le(a+1)(b+c)\qquad(0\le a\le b\le c)
\]
gives an \(O_{\delta,C}(R^2)\) treatment of a possible unpaired child.
Adding the translated origin of that one child if necessary, and handling
the excluded/global terminal convention, costs only \(O_{\delta,C}(1)\)
more letters.  Exact width telescoping and packet concatenation would
therefore turn (10.1) into
\[
g_4(\boldsymbol\ell)
\le w_4(\boldsymbol\ell)
+O_{\delta,C}(R)\varepsilon_{\delta,C}(R)R^2
+O_{\delta,C}(R^2)
=w_4(\boldsymbol\ell)+o_{\delta,C}(R^3).
\tag{10.1a}
\]
Thus APF has exactly the strength needed by the four-box fusion route.

After the present audit, APF must additionally satisfy:

- \(\Theta(R^2)\) doubly active positions per typical bad pair;
- \(\Theta(R^2)\) shared left/right endpoint incidences;
- two compatible orthogonal endpoint-chain systems;
- one chronology in which the required cross intervals are not
  contaminated by the other packet targets.

The first two requirements have enough raw complementary-shell capacity by
Section 7.  The third and fourth are the genuine missing steps.

An alternative sufficient theorem is the averaged fused four-box estimate
\[
\mathbb E\,E_4(L_1,L_2,L_3,L_4)=o(k^{3/2})
\tag{10.2}
\]
for four independent SCD heights in balanced Boolean blocks.  The local
three-box theorem neither proves nor refutes (10.1) or (10.2).

## 11. Implication and audit ledger

### Proved

- the explicit uniform plateau bound (3.5);
- cubic isolated child excess for every compact-balanced parent, (4.4);
- the sharpened equal-parent constant (4.9)-(4.11);
- exact join projections for all translated hook children;
- the letter--child activity ledger (5.5);
- survival of the sloped-band dual under arbitrary seam crossing;
- the endpoint--child sharing ledger (6.5);
- failure of every sparse/boundary-length repair within the hook packet
  ledgers;
- the band-compatible adjacent-seam matching and its positive capacity
  margin;
- the exact diamond packet (8.1), proving hook additivity false.

### Unproved

- APF;
- simultaneous exposure of the two orthogonal endpoint systems;
- a compact reset-free surface braid;
- \(g_4=w_4+o(R^3)\), uniformly or on average;
- the constant-one contiguous-OR theorem.

### Independent proof audits

Three audits were carried out independently of the derivations above.

1. The aggregate audit reconstructed the \(67/12\) finite loss, the
   threshold-count proof of peel isotonicity, the full \(A_r,B_r\) equal
   drain, the \(B_r\) outer-axis \(+2\), and the terminal \(-1\).  It also
   checked the activity projection and the repaired \(T_j\)-aware diamond
   lower bound.  Verdict: pass.

2. The endpoint audit reconstructed the denominator \(r+2k\), the sign in
   (6.5), the \(p=0\) and translated-terminal baselines, and the constants
   \(4\gamma_*/3\), \(289/5184\), \(289/1728\), \(15/64\), and \(29/432\).
   It independently checked the seam-cover membership and exact count
   (7.5).  Verdict: pass.

3. The cross-child audit checked that projection followed by deletion of
   zero images preserves contiguity, that arbitrary foreign letters do not
   invalidate the endpoint certificate, that only the actual excluded
   global zero costs \(2\tau_0\), and that the diamond proves only literal
   hook nonadditivity, not a compact asymptotic escape.  Verdict: pass.

The audits exposed five real edge cases: \(p=0\) children, the
excluded-zero endpoint correction, \(c=0\), a possible singleton \(T_0\)
in the diamond lower bound, and the need in (4.9a) to delete every letter
outside the lower subbox rather than only the two forced axis letters.  All
five are explicitly incorporated above.

### Final logical scope

\[
\boxed{
\begin{aligned}
\text{local three-box gap}
&\Longrightarrow
\text{cubic isolated hook bill}\\
&\Longrightarrow
\begin{cases}
\text{cubic physical excess},&\text{if sharing is sparse},\\
\text{cubic sharing demand},&\text{in general}.
\end{cases}
\end{aligned}}
\tag{11.1}
\]

The step from cubic sharing demand to cubic physical excess is not
justified by these ledgers without an additional degree or chronology
hypothesis.  The diamond packet is an exact counterexample to unconditional
hook additivity, while the complementary surface matching shows that the
compact adjacent pair has enough raw capacity.  This does not prove formal
nonimplication of the compact three-box theorem and a four-box lower bound.
Whether the capacity can be organized into APF is the theorem left open by
third-wave U.
