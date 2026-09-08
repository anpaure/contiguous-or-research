# Raw lead report and corrected addendum: multiscale four-box fusion

The product-box/four-box route does not yet prove the conjecture. It yields a sharp conditional reduction, an explicit reset-free portal construction, and a cubic obstruction showing why separate slice or queue resets cannot finish the balanced case.

## 1. Compact four-box reduction

For
\[
Q(\boldsymbol\ell)=\prod_{i=1}^4[0,\ell_i],
\]
let \(g_4(\boldsymbol\ell)\) be the shortest nonzero word whose contiguous coordinatewise maxima contain every nonzero point of \(Q\), and let
\[
w_4(\boldsymbol\ell)=
[z^{\lfloor(\ell_1+\cdots+\ell_4)/2\rfloor}]
\prod_{i=1}^4(1+z+\cdots+z^{\ell_i}).
\]

The exact missing local statement is:

> **Compact balanced four-box lemma (CB4) — UNPROVED.**  
> For every fixed \(0<\delta<C<\infty\),
> \[
> \max_{\delta R\le \ell_i\le CR}
> \frac{(g_4(\boldsymbol\ell)-w_4(\boldsymbol\ell))_+}{R^3}
> \longrightarrow0.
> \tag{CB4}
> \]

### Theorem 1

(CB4) implies
\[
\nu(k)=\bigl(1+o(1)\bigr)\binom{k}{\lfloor k/2\rfloor}.
\]

### Proof

Split the Boolean coordinates into four balanced blocks \(X_i\), choose an arbitrary SCD in each block, and take products of component chains. If the four chain heights are \(\ell_i\), the resulting product box is \(Q(\boldsymbol\ell)\).

If the chain bottoms have total rank \(A\), then
\[
\sum_i\ell_i=k-2A,\qquad
\left\lfloor\frac{k}{2}\right\rfloor-A
=\left\lfloor\frac{\sum_i\ell_i}{2}\right\rfloor.
\]
Thus global-middle points are exactly local-middle points, and exact width additivity gives
\[
\sum_{\text{product boxes}}w_4(\boldsymbol\ell)
=W(k):=\binom{k}{\lfloor k/2\rfloor}.
\tag{1}
\]

Put \(R=\sqrt{k}\). The number \(B\) of product boxes satisfies
\[
B=\prod_{i=1}^4W(|X_i|)
=\Theta\!\left(\frac{W(k)}{k^{3/2}}\right)
=\Theta\!\left(\frac{W(k)}{R^3}\right).
\tag{2}
\]

The audited three-box hook word implies, for every chosen coordinate \(i\),
\[
g_4(\boldsymbol\ell)+1
\le(\ell_i+1)
 \left(1+\sum_{j\ne i}\ell_j\right)^2.
\tag{3}
\]
Every witness stays inside its constant-\(i\)-coordinate slice. In particular,
\[
g_4(\boldsymbol\ell)+1
\le\left(1+\sum_i\ell_i\right)^3.
\tag{4}
\]

For an SCD of an \(s\)-cube,
\[
\#\{C:\ell(C)\ge2d\}
=\binom{s}{\lfloor s/2\rfloor-d},
\]
and hence
\[
\Pr(\ell(C)\ge2d)\le e^{-d^2/s}.
\tag{5}
\]
Discrete integration gives, for fixed \(j\le3\),
\[
\sum_C(1+\ell(C))^j=O(W(s)R^j),
\tag{6}
\]
and
\[
\sum_{\ell(C)>CR}(1+\ell(C))^j
=O(W(s)R^j e^{-cC^2}),
\tag{7}
\]
after absorbing polynomial factors in \(C\) into the Gaussian exponent.

Call a box thin if some \(\ell_i<\delta R\). Writing \(x_i=1+\ell_i\), (3) gives
\[
g_4+1\le3x_i\sum_{j\ne i}x_j^2.
\]
Using (6),
\[
\sum_{\ell_i<\delta R}(g_4+1)
=O\!\left(B(\delta R+1)R^2\right).
\]
After a union bound over \(i\) and using (2),
\[
\text{total thin-box length}
=O(\delta W(k))+O(W(k)/R).
\tag{8}
\]

Call a box long if some \(\ell_i>CR\). From
\[
\left(\sum_i x_i\right)^3\le16\sum_i x_i^3
\]
and (6)–(7),
\[
\text{total long-box length}
=O(e^{-cC^2}W(k)).
\tag{9}
\]

Every remaining box lies in the compact window. By (CB4), its error is at most
\(\eta_{\delta,C}(R)R^3\), where \(\eta_{\delta,C}(R)\to0\). Summing over at most \(B\) boxes gives
\[
O(\eta_{\delta,C}(R)W(k)).
\tag{10}
\]

A Boolean product box may have a nonempty common minimum. Adding that minimum to every local letter transfers local maxima to literal Boolean ORs; prepending it once covers the local origin. This costs at most
\[
B=O(W(k)/R^3).
\tag{11}
\]

Concatenating all box words needs no separator because every selected witness is internal to its box. From (1), (8)–(11),
\[
\frac{\nu(k)}{W(k)}
\le1+O(\delta)+O(R^{-1})+O(e^{-cC^2})
 +O(\eta_{\delta,C}(R))+O(R^{-3}).
\]
Fix \(\delta,C\), let \(k\to\infty\), and only then send
\(\delta\downarrow0\), \(C\uparrow\infty\). This proves the theorem. ∎

The \(R^3\) normalization is sharp: there are \(\Theta(W/R^3)\) compact boxes, each of width \(\Theta(R^3)\). Merely proving \(O(R^3)\) local error would aggregate to \(O(W)\), not \(o(W)\).

## 2. Explicit reset-free seam fusion

The following local mechanism is unconditional.

### Lemma 2: complementary portal

Let \(i,i',j,j'\) be distinct coordinates and suppose
\[
A_u=v-ue_i+ue_{i'}\quad(0\le u\le a),
\qquad
B_z=v+ze_j-ze_{j'}\quad(0\le z\le b)
\]
are legal box points. Then the literal word
\[
A_a,A_{a-1},\ldots,A_1,v,B_1,\ldots,B_b
\]
has, for every \(u,z\), the exact witness
\[
\bigvee[A_u,\ldots,v,\ldots,B_z]
=v+ue_{i'}+ze_j.
\tag{12}
\]

Indeed, coordinates \(i,j'\) are maximized at \(v\), while \(i',j\) are maximized at \(A_u,B_z\). Thus one physical seam simultaneously serves an \((a+1)\times(b+1)\) rectangle across all depths, without a reset.

For the equal box \([0,m]^4\), this assembles into an explicit near-once portal core. Put \(R=2m-1\) and \(q\le m/3\). For \(A+B\le q-1\), define
\[
X_u=(m-A-u,B+u,m-B-1,A),
\]
\[
Y_z=(m-A-1,B,m-B-z,A+z).
\]
Use the block
\[
X_{q-1-B},\ldots,X_0,Y_0,\ldots,Y_{q-1-A}.
\tag{13}
\]

Every target
\[
y=(m-A,a,m-B,b)\in L_{R+s}
\]
missed by both complementary complete-line systems satisfies
\[
A+B=a+b-s+1,\qquad
u=a-B,\quad z=b-A,\quad u+z=s-1.
\]
Equation (12) applied to (13) gives exactly \(y\).

Within one high/low orientation, same-type portal letters are distinct and the only cross-type coincidences have total count \(q(q-1)\). The four orientations are disjoint because their low coordinates are at most \(q-1\), while their high coordinates are at least \(m-2q+2>q-1\). Appending every unused rank-\(R\) point once therefore produces a word of exact length
\[
|L_{2m-1}|+4q(q-1)
\tag{14}
\]
covering the entire doubly-missed family through depth \(q\).

This is a genuine multiscale fusion theorem. It is not a full upper-band word: moving the line arms destroys some previously intact “easy” line witnesses.

## 3. Unconditional obstruction to separate resets

The principal new negative result is uniform over every compact aspect-ratio window.

### Theorem 3: separated-epoch obstruction

Fix \(0<\delta<C\). For all sufficiently large \(R\), let
\[
\delta R\le\ell_1\le\ell_2\le\ell_3\le\ell_4\le CR,
\quad
S=\sum_i\ell_i,
\quad r=\lfloor S/2\rfloor.
\]
There exist constants \(\alpha,\kappa>0\), depending only on \(\delta,C\), such that, with \(t=\lfloor\alpha R\rfloor\) and
\[
\mathcal B=\{x:|x|=r,\ x_1<t\},
\]
one has
\[
\boxed{|L_{r-t}|+|\mathcal B|
\ge w_4(\boldsymbol\ell)+\kappa R^3.}
\tag{15}
\]

#### Boundary count

Fix \(x_1=a<t\). After complementing the final three coordinates, restrict each complemented coordinate to a common subinterval of height
\(\ell_1\). The required sum becomes
\[
u_2+u_3+u_4=\ell_1+a+\theta,
\qquad \theta\in\{0,1,2\}.
\]
Because \(t\le\ell_1/4\), the relevant coefficient of
\((1+\cdots+z^{\ell_1})^3\) is
\[
\binom{\ell_1+a+\theta+2}{2}
-3\binom{a+\theta+1}{2}
\ge\frac{\ell_1^2}{128}.
\]
Hence
\[
|\mathcal B|
\ge\frac{\delta^2}{128}\,tR^2.
\tag{16}
\]

Choosing the shortest coordinate is essential; for an arbitrary coordinate the boundary family can be empty in an unequal box.

#### Central-layer loss

Let
\[
F(z)=\prod_i(1+z+\cdots+z^{\ell_i}),
\qquad p_j=[z^j]F(z).
\]
Then
\[
p_j-2p_{j-1}+p_{j-2}
=[z^j]\frac{\prod_i(1-z^{\ell_i+1})}{(1-z)^2}.
\]
Inclusion–exclusion gives
\[
|p_j-2p_{j-1}+p_{j-2}|
\le16(S+1).
\tag{17}
\]
Using symmetry at the central rank and telescoping (17),
\[
w_4(\boldsymbol\ell)-|L_{r-t}|
\le8(S+1)t(t+1)
\le16(4C+1)Rt^2.
\tag{18}
\]
Taking \(\alpha>0\) sufficiently small compared with
\(\delta^2/C\), the linear term (16) dominates the quadratic-in-\(\alpha\) term (18), proving (15). ∎

Now suppose a word uses core epochs containing all rank-\((r-t)\) points and auxiliary reset epochs of total length \(A\), with \(s\) epoch boundaries.

No member of \(\mathcal B\) is represented inside one fixed coordinate-\(\{1,2\}\) core line: a rank-\(r\) line join from rank \(r-t\) requires endpoint separation \(t\), forcing its first-coordinate maximum to be at least \(t\).

An auxiliary word of length \(A\) represents at most \(A\) members of the antichain \(\mathcal B\). At one seam, suffix joins and prefix joins are two chains; their pairwise joins form a product of two chains. Therefore one seam represents at most \(S+1=O(R)\) members of \(\mathcal B\). Consequently
\[
|\mathcal B|\le A+s(S+1).
\tag{19}
\]
The total length \(n\) obeys
\[
n\ge |L_{r-t}|+A
\ge w_4+\kappa R^3-s(S+1).
\tag{20}
\]

Thus
\[
n=w_4+o(R^3)\quad\Longrightarrow\quad s=\Omega(R^2).
\tag{21}
\]
If every productive seam pays a separate reset of length \(\Omega(R)\), then (19) forces \(A=\Omega(R^3)\). Separate resets are therefore fatal.

This obstruction is architecture-specific. It does not apply after cutting and globally interleaving the core lines. The exact mechanistic replacement is:

> **Reset-free surface-braid lemma — UNPROVED.**  
> Embed \(\Theta(R^2)\) productive complementary-line seams into one near-once compact-box core with \(o(R^3)\) extra letters, while preserving all required uncontaminated witnesses.

This lemma is necessary for the line-spine architecture but is not alone sufficient for all lower and tail targets. The smallest fully sufficient statement remains (CB4).

## 4. Integration of the fixed-window exact-ownership reduction

For fixed \(A\), put \(K_A=\lceil A\sqrt m\rceil\). Uniformly for \(q\le K_A\),
\[
\log\frac{W}{N_q}
=\frac{q^2}{m}+O_A(m^{-1/2}),
\]
so
\[
1\le c_q\le C_A
\tag{22}
\]
for a constant depending only on \(A\).

Therefore, for one exact factor \(\mathcal F\) and one common balanced nested resolution \(P\),
\[
\frac1{C_A}\sum_{q\le K_A}e_q(\mathcal F,P)
\le
\sum_{q\le K_A}\frac{e_q(\mathcal F,P)}{c_q}
\le
\sum_{q\le K_A}e_q(\mathcal F,P).
\tag{23}
\]

Hence the labelled fixed-window theorem is exactly equivalent to
\[
\boxed{
\sum_{q\le A\sqrt m}
\#\{X:L_q^{\mathcal F}(X)\ne P_q(X)\}
=o(W).}
\tag{BF\(_A\)}
\]

This must use the same exact factor and the same nested flow at every depth. Separate rankwise factors, independent quota vectors, or unlabelled seam rectangles do not establish \((\mathrm{BF}_A)\). One consequence of (23) is that all but \(o(W)\) owners have no mismatch anywhere in the fixed window.

If \((\mathrm{BF}_A)\) holds for every fixed \(A\), choose a diagonal \(A=A(m)\to\infty\) sufficiently slowly that
\[
A(m)=o(\sqrt m),\qquad
\sum_{q\le A(m)\sqrt m}\frac{e_q}{c_q}=o(W).
\]
Put \(H=A(m)\sqrt m\). The \(W/n\) exact wreath blocks have total length
\[
\frac Wn(n+2H+1)
=W+O(WH/m)=W+o(W).
\tag{24}
\]
A missing depth-\(q\) target accounts for at least \(c_q\) mismatched owners, so
\[
M_q\le e_q/c_q.
\tag{25}
\]
Appending missing lower targets and their complements costs
\[
2\sum_{q\le H}M_q=o(W).
\tag{26}
\]
Because \(H/\sqrt m=A(m)\to\infty\), the audited symmetric-chain product tail costs \(o(W)\). Equations (24)–(26) imply the final contiguous-OR bound.

This exact-ownership route remains unproved. The direct product-box theorem is an alternative literal route and must not be cited as evidence for \((\mathrm{BF}_A)\).

The factor-independent overload tail may additionally be discarded beyond any cutoff satisfying
\[
\frac{Q^2}{m}\ge
\frac12\log m-\frac12\log\log m+\omega(1).
\]
In particular \(Q=\alpha\sqrt{m\log m}\) is safe for fixed
\(\alpha>1/\sqrt2\). Writing only
\((1/\sqrt2+o(1))\sqrt{m\log m}\) is insufficient without specifying a one-sided second-order approach. This tail fact does not remove the fixed-window fusion obstruction above.

## 5. Adversarial audit

Three independent audits attacked the strongest claims.

- **Aspect ratios:** The first boundary-count attempt fails if an arbitrary coordinate is used. Selecting the shortest side and embedding the explicit central three-cube repairs this; it yields (16) uniformly.
- **Parity:** Both \(S\) even and odd were checked in deriving (18). For odd \(S\), the two central coefficients coincide; for even \(S\), central symmetry bounds the first difference by half a second difference.
- **Hidden resets:** Thin/long product boxes use internal witnesses, and the only cross-box charge is one common-minimum anchor per box. No seam is silently assumed.
- **Seam capacity:** A portal has quadratic capacity across all depths but only \(O(R)\) capacity at one fixed rank. Thus it really takes \(\Omega(R^2)\) productive seams to defeat (15).
- **Scope:** Theorem 3 does not lower-bound unrestricted \(g_4\); cutting and braiding lines escapes it. The portal core covers only the doubly-missed upper family and supplies neither all easy upper witnesses nor a lower-factor/pinning construction.
- **Ownership:** Equation (23) is asserted only for one common pair \((\mathcal F,P)\). It gives no license for depthwise quota selection. The known \(n=9\) Hall failure confirms that this qualification is substantive.
- **Overload versus labelled error:** The overload fixed-window theorem is weaker. The report uses labelled \((\mathrm{BF}_A)\) only as a sufficient exact-ownership theorem and does not claim an overload-to-labelled converse.

Therefore the stable conclusion is negative but sharp: separate product-box or queue resets are provably critical-order, genuine reset-free seams exist, and the entire direct route is now isolated to the single compact lemma (CB4).

---

## Corrected addendum

The cross-audit’s three corrections are accepted. They do not change the portal length, CB4 aggregation, or the architecture-specific obstruction.

### 1. Direct proof of the portal block

The block
\[
X_{q-1-B},\ldots,X_0,Y_0,\ldots,Y_{q-1-A}
\]
does not literally instantiate Lemma 2 because \(X_0\ne Y_0\). Its seam identity must be proved directly.

For
\[
X_u=(m-A-u,B+u,m-B-1,A),
\]
\[
Y_z=(m-A-1,B,m-B-z,A+z),
\]
one has
\[
\bigvee_{h=0}^{u}X_h
=(m-A,B+u,m-B-1,A)
\]
and
\[
\bigvee_{h=0}^{z}Y_h
=(m-A-1,B,m-B,A+z).
\]
Therefore the literal contiguous interval satisfies
\[
\boxed{
\bigvee[X_u,\ldots,X_0,Y_0,\ldots,Y_z]
=(m-A,B+u,m-B,A+z).}
\tag{A1}
\]

For a target
\[
y=(m-A,a,m-B,b),
\]
take
\[
u=a-B,\qquad z=b-A.
\]
The previously proved inequalities make \(u,z\) legal, and (A1) gives exactly \(y\). Thus the portal coverage and exact length
\[
|L_{2m-1}|+4q(q-1)
\]
remain valid.

### 2. Orientation disjointness

The safe uniform lower bound for every designated high coordinate is
\[
\boxed{m-2q+1,}
\]
not \(m-2q+2\). Since \(q\le m/3\),
\[
m-2q+1>q-1.
\]
Every portal point therefore still reveals, within each coordinate pair, which coordinate is high and which is low. The four orientation classes remain disjoint, so the collision and length ledger is unchanged.

### 3. Exact scope of the epoch obstruction

The rank inequality
\[
|L_{r-t}|+|\mathcal B|
\ge w_4(\boldsymbol\ell)+\kappa R^3
\tag{A2}
\]
is unconditional.

Its conversion into a word-length obstruction requires the following architecture.

> Every core epoch consists solely of rank-\((r-t)\) points on one fixed \(\{1,2\}\)-coordinate line; collectively, the core epochs contain every point of \(L_{r-t}\). All other epochs are auxiliary reset epochs.

Under this hypothesis, no member of
\[
\mathcal B=\{x:|x|=r,\ x_1<t\}
\]
has a witness internal to a core epoch. Indeed, if a segment on a fixed line has first-coordinate extrema \(p\le q\), its join has rank
\[
(r-t)+(q-p).
\]
Rank \(r\) forces \(q-p=t\), hence \(q\ge t\), contradicting \(x_1<t\).

If the auxiliary epochs have total length \(A_{\rm aux}\) and there are \(s\) epoch boundaries, then:

- internal auxiliary witnesses cover at most \(A_{\rm aux}\) members of the antichain \(\mathcal B\);
- crossing witnesses at one boundary cover at most \(S+1\) such members, because suffix joins and prefix joins are chains and their product has width at most \(S+1\).

Thus
\[
|\mathcal B|\le A_{\rm aux}+s(S+1),
\]
and
\[
n\ge |L_{r-t}|+A_{\rm aux}.
\]
Combining with (A2),
\[
\boxed{
n\ge w_4(\boldsymbol\ell)+\kappa R^3-s(S+1).}
\tag{A3}
\]

Consequently \(n=w_4+o(R^3)\) forces \(s=\Omega(R^2)\) only within this fixed-line core-epoch architecture. If every productive seam additionally pays a separate \(\Omega(R)\) reset, the overhead is \(\Omega(R^3)\).

No unrestricted lower bound on \(g_4\) is claimed. Cutting and globally interleaving the line cores can evade (A3), which is precisely why the reset-free surface-braid lemma remains the mechanistic open target.

