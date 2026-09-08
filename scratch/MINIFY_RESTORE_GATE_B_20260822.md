# Compact restoration block: Gate B local conditioning and rooted core

**Insertion.** Insert H.14 immediately after current H.11 and before H.15.
Insert the second theorem immediately after current H.15 and before current
H.16. The archive called the second theorem H.16, but current H.16 is the
Venn-gap theorem; the draft therefore calls it H.15A. All claims below are
[I].

**Notation.** This block uses \(\Gamma_r\) for the blocker graph and
\(\mathsf A,\mathsf B,\mathsf M\) for matrices, avoiding the current
overloading of \(B_r\). It uses \(\Lambda=r+1\), not \(L\), because \(L\)
already denotes the lower shore. Falling factorials are
\((z)_h=z(z-1)\cdots(z-h+1)\), with \((z)_0=1\).

---

## H.14 Uniform all-depth conditioning of the sixteen-atom bank [I]

Put \(b=2r+1\),
\[
 K=r-4,\qquad \Lambda=r+1,\qquad m=j-2,
 \qquad D_M=2r\,r!(r+1)! .                              \tag{H.14.1}
\]
Use the two-pair harmonic projection and the sixteen signed local profiles
\(L_{s,j}(t)\), \(s\in\{r,r-1\}\), defined in H.1 and H.11. Thus the
blocker graph is
\(\Gamma_r=\operatorname{Cay}(\mathbb Z_b,\{\pm1,\pm3\})\), the event
roots are \(0,5\), the sixteen supports are
\(\{0,5,x,y\}\) with
\(x\in\{-3,-1,1,3\}\), \(y\in\{2,4,6,8\}\), and each support contributes
its endpoint matching, minus its full three-edge path when the connector is
present. The six connector pairs are
\[
 (-1,2),(1,2),(1,4),(3,2),(3,4),(3,6).                 \tag{H.14.2}
\]
Terms using either puncture edge
\(\{2t,2t+1\},\{2t,2t+3\}\) are omitted. If
\(\widehat L_{s,j}(t)\) denotes the corresponding unaveraged signed
injection sum, then the boundary average in H.1 is
\[
 L_{s,j}(t)={\widehat L_{s,j}(t)\over(K)_m(\Lambda)_m}.     \tag{H.14.3}
\]
Indeed the \(2^j\) orientations contribute equally after multiplication by
the two harmonic signs and cancel the \(2^j\) in \(|\mathcal B_t|\).
Define the \((2r+1)\)-by-two normalized profile matrix
\[
 (\mathsf A_{r,j})_{t,s}
 ={L_{s,j}(t)\over D_M}
 ={\widehat L_{s,j}(t)\over D_M(K)_m(\Lambda)_m},
 \quad t\in\mathbb Z_b, s\in\{r,r-1\}.                \tag{H.14.3a}
\]

### Theorem H.14.1

For every \(r\ge9\) and \(2\le j\le r-2\),
\[
                 \boxed{\sigma_{\min}(\mathsf A_{r,j})\ge r^{-29}.}
                                                                    \tag{H.14.4}
\]

### Proof

At \(t=3\) neither puncture meets a local atom. Take the two exact defects
\[
 C_{1,s,j}=L_{s,j}(3)-L_{s,j}(r+1),\qquad
 C_{2,s,j}=L_{s,j}(3)-L_{s,j}(r+2).                      \tag{H.14.5}
\]
Writing \((q,a)\) for the rank-\(q\) cyclic interval starting at \(a\),
comparison with the unpunctured bank leaves exactly these four deleted
three-blocker paths:
\[
\begin{array}{c|c|c}
 &\text{first}&\text{second}\\ \hline
C_1&\{(r-1,r),(r,0),(r,r+1)\}&
     \{(r-1,0),(r,r-1),(r,r+1)\}\\
C_2&\{(r-1,r+2),(r,0),(r,r)\}&
     \{(r-1,0),(r-1,r+2),(r,b-1)\}.
\end{array}                                               \tag{H.14.6}
\]
Hence no remote expansion enters these rows.

After the two marked boundary pairs are removed, the normalized signed
injection average of the remaining \(m\) event pairs, when a root has
\(a\) available inside and \(c\) available outside positions, is
\[
 e_m(a,c)=\sum_{h=0}^m(-1)^{m-h}{m\choose h}
 { (a)_h\over(K)_h}{(c)_{m-h}\over(\Lambda)_{m-h}},
 \qquad |e_m(a,c)|\le1.                                  \tag{H.14.7}
\]
The formula follows by choosing the \(h\) pairs whose selected endpoint is
inside and placing all constrained endpoints first. The bound follows
because this is an average of products from \(\{-1,0,1\}\).

Let \(P(a)=(K+1-a)(a+1)\). After division by \(D_M\), the coefficient of
\(e_m(a,s-2-a)\) in the four defect/shore combinations is
\[
\begin{array}{c|c}
G_{1,r}(a)&q_1P(a)+u_1\mathbf1_{a=K}\\
G_{2,r}(a)&q_2P(a)+u_2\mathbf1_{a=K}\\
G_{1,r-1}(a)&q_1P(a)+v_1\mathbf1_{a=K}\\
G_{2,r-1}(a)&q_2P(a)+w_2\mathbf1_{a=K-1}+v_2\mathbf1_{a=K},
\end{array}                                               \tag{H.14.8}
\]
where
\[
\begin{aligned}
q_1&={4(r+2)(2r-3)\over r^3(r-3)(r-2)(r-1)(r+1)},&
u_1&=-{2r-3\over r^3(r-1)(r+1)},\\
q_2&={2(4r^2+6r-15)\over r^3(r-3)(r-2)(r-1)(r+1)},&
u_2&=-{4r-5\over r^3(r-1)(r+1)},\\
v_1&=-{(r+4)(4r^2-13r+8)\over2r^3(r-2)(r-1)(r+1)},&
w_2&=-{(r-4)(4r-5)\over r^3(r-2)(r-1)(r+1)},\\
v_2&=-{4r^3+3r^2-36r+30\over2r^3(r-2)(r-1)(r+1)}.&&
\end{aligned}                                             \tag{H.14.9}
\]
This finite count uses no interpolation. For a blocker triple with Boolean
cell sizes \(c_\eta\) and root occupancies \(u_\eta\), compatible
bijections have weight
\(N_{s,J}(u)\prod_\eta u_\eta!(c_\eta-u_\eta)!\). Up to cell permutation,
the four triples in (H.14.6) have vectors
\[
 (0,1,r,0,2,r-2,0,0),\quad
 (0,r-1,2,0,2,0,r-2,0),\quad
 (3,0,r-2,0,0,r-1,1,0).                                 \tag{H.14.10}
\]
The first two types have \(2b-6\) retained positional tuples and the last
has \(2b-5\). Insert the four marks, sum the \(2r\) retained root starts,
and cancel factorials against \(D_M\). This gives the common quadratic for
\(a<K\); only \(a=K-1,K\) lose starts, giving exactly (H.14.9).

It remains to close the quadratic Hahn sums. Set
\[
 S_d=\sum_{a=0}^KP(a)e_m(a,K+d-a)\quad(d=1,2),             \tag{H.14.12}
\]
and
\[
 E_1=e_m(K,1)={\Lambda-m\over\Lambda},\quad
 E_2=e_m(K,2)={ (\Lambda-m)(\Lambda-m-1)\over\Lambda(\Lambda-1)},
                                                                  \tag{H.14.13}
\]
\[
 E_{12}=e_m(K-1,2)
 ={(\Lambda-m)(K\Lambda-Km-K-\Lambda m+m^2-m)
    \over K\Lambda(\Lambda-1)}.                         \tag{H.14.14}
\]
These sums have no hidden limiting step. Expand (H.14.7), write
\((a)_h(K+d-a)_q=h!q!{a\choose h}{K+d-a\choose q}\), and apply
Vandermonde after expanding the quadratic \(P(a)\) in falling factorials.
For \(d=1\) the omitted endpoint has weight zero; for \(d=2\) the two
omitted endpoints have weights zero and \(-(K+3)\). This finite identity
evaluates (H.14.12) as a rational function of \(r,m\) and yields the
matrix and factorization below by direct collection.

The normalized two-by-two defect matrix is therefore
\[
 \mathsf B_{r,j}=
 \begin{pmatrix}
 q_1S_2+u_1E_2&q_1S_1+v_1E_1\\
 q_2S_2+u_2E_2&q_2S_1+w_2E_{12}+v_2E_1
 \end{pmatrix}.                                          \tag{H.14.18}
\]
Let \(x=r-m-4\ge0\). Substitution gives
\[
 \det\mathsf B_{r,j}
 ={(r-m)(r-m+1)^2\Phi_m(x)\over\mathcal D(r,m)},          \tag{H.14.19}
\]
where
\[
\mathcal D=r^8(2r-m)(m+1)(m+2)(m+3)(r-2)(r-1)^2
(r+1)^4(2r-m-1)(2r-m+1).                                 \tag{H.14.20}
\]
The numerator has these four exhaustive forms:
\[
\begin{aligned}
\Phi_0(x)&=2(x+4)^2(2x+7)(2x+9)H_0(x),\\
H_0(x)&=40x^4+485x^3+1977x^2+3308x+1950,\\
\Phi_2(x)&=4(x+5)(2x+9)(2x+11)H_2(x),\\
H_2(x)&=40x^5+1245x^4+13508x^3+67422x^2+158710x+143316.
\end{aligned}                                             \tag{H.14.21}
\]
For odd \(m\),
\[
 \Phi_m(x)=-(m+1)(m+3)(m+2x+8)H_o(m,x),                  \tag{H.14.22}
\]
\[
\begin{aligned}
H_o={}&4m^8+(36x+119)m^7+(136x^2+912x+1467)m^6\\
&+(280x^3+2846x^2+9299x+9834)m^5\\
&+(340x^4+4628x^3+22901x^2+49207x+39053)m^4\\
&+(244x^5+4135x^4+27343x^3+88945x^2+143584x+92750)m^3\\
&+(96x^6+1924x^5+15810x^4+68904x^3+169743x^2
   +225672x+126443)m^2\\
&+(16x^7+364x^6+3544x^5+19526x^4+66867x^3
   +142873x^2+173845x+90190)m\\
&+8x^6+249x^5+2755x^4+14656x^3+40322x^2+54490x+27840.
\end{aligned}                                             \tag{H.14.23}
\]
For even \(m\ge4\), put \(y=m-4\); then
\[
 \Phi_m(x)=-(y+6)(2x+y+11)(2x+y+13)H_e(y,x),              \tag{H.14.24}
\]
\[
\begin{aligned}
H_e={}&(8y^2+48y+24)x^6
 +(44y^3+606y^2+2084y+651)x^5\\
&+(100y^4+2191y^3+15770y^2+38654y+10423)x^4\\
&+(120y^5+3632y^4+40713y^3+202416y^2+396813y+120432)x^3\\
&+(80y^6+3098y^5+47527y^4+362939y^3+1401929y^2
   +2359307y+852174)x^2\\
&+(28y^7+1322y^6+25825y^5+267951y^4+1569184y^3
   +5028592y^2+7582719y+3125836)x\\
&+4y^8+223y^7+5301y^6+69776y^5+551539y^4
   +2644354y^3+7324827y^2+10144976y+4525360.
\end{aligned}                                             \tag{H.14.25}
\]
Every coefficient in \(H_0,H_2,H_o,H_e\) is positive. Thus
\(\det\mathsf B_{r,j}\ne0\). Its numerator in (H.14.19) is a nonzero
integer, every denominator factor is positive, and for
\(r\ge9,0\le m\le r-4\),
\[
 \mathcal D(r,m)\le512r^{21},\qquad
 |\det\mathsf B_{r,j}|\ge r^{-24}.                        \tag{H.14.26}
\]
Indeed \(r^3\ge512\). Also (H.14.7)--(H.14.9) imply
\(|S_d|\le\sum_aP(a)\le r^3\), every entry of \(\mathsf B\) has
absolute value at most \(2r^3\), and
\[
 \|\mathsf B_{r,j}\|_F\le4r^3,\qquad
 \sigma_{\min}(\mathsf B_{r,j})\ge{1\over4r^{27}}.       \tag{H.14.27}
\]
Let \(T\) take the two row differences in (H.14.5). Then
\(TT^{\mathsf T}=\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\),
so \(\|T\|=\sqrt3\), and \(\mathsf B=T\mathsf A\). Hence
\[
 \sigma_{\min}(\mathsf A_{r,j})
 \ge{1\over4\sqrt3\,r^{27}}\ge r^{-29},                 \tag{H.14.28}
\]
proving the theorem. \(\square\)

The theorem is local. Together with H.11 it removes the local
harmonic-depth and rank-two conditioning issue; it does not transfer the
inverse to the complete zero-avoidance exposure. In normalized units the
known absolute remote error \(O(r^{-2})\) can exceed the deliberately
crude \(r^{-29}\) inverse.

---

## H.15A Exact \(j=2\) six-vertex rooted-core determinant [I]

Put
\[
 b=2r+1,\qquad
 \Gamma_r=\operatorname{Cay}(\mathbb Z_b,\{\pm1,\pm3\}),
 \qquad p=0,\quad q=5,\quad D_M=2r\,r!(r+1)!.            \tag{H.15A.1}
\]
At event shift \(t\), puncture
\(\mathcal P_t=\{\{2t,2t+1\},\{2t,2t+3\}\}\). An edge set \(J\) is
**rooted** if \(\{p,q\}\subseteq V(J)\), \(|V(J)|\le6\), and every
connected component of \(J\) contains \(p\) or \(q\). Edges of cyclic
length one and three carry, respectively, the original rank-\(r\) and
rank-\((r-1)\) interval tags. Let
\(C_s^{(6)}(t)\) be the signed \(j=2\) harmonic contribution on shore
\(s\in\{r,r-1\}\) of rooted sets using at least one edge restored from
\(\mathcal P_t\), with inclusion--exclusion sign \((-1)^{|J|}\). The
complete rooted sum is translation invariant, so
its retained profile satisfies
\[
 L_s^{(6)}(u)-L_s^{(6)}(t)=C_s^{(6)}(t)-C_s^{(6)}(u).       \tag{H.15A.2}
\]
Define
\[
 X_s={C_s^{(6)}(r)-C_s^{(6)}(r+1)\over D_M},\qquad
 Y_s={C_s^{(6)}(r+2)-C_s^{(6)}(r+3)\over D_M},             \tag{H.15A.3}
\]
\[
 \mathsf M_r^{(6)}=\begin{pmatrix}X_r&X_{r-1}\\Y_r&Y_{r-1}\end{pmatrix}.
                                                                    \tag{H.15A.4}
\]

### Theorem H.15A.1

For every \(r\ge23\),
\[
 \boxed{\det\mathsf M_r^{(6)}={P(r)\over12Q(r)^2}>0,\qquad
 \det\mathsf M_r^{(6)}\ge2^{-187}r^{-6},}                \tag{H.15A.5}
\]
and
\[
 \det\mathsf M_r^{(6)}={4\over3}r^{-6}-6r^{-7}
 +{1169\over12}r^{-8}+O(r^{-9}).                          \tag{H.15A.6}
\]

### Proof

For an ordered blocker tuple, index Boolean cells by \(\eta\). Let
\(c_\eta\) be the cell size, \(m_\eta\) the number of the four event
labels in it, and \(u_\eta\) the root-interval occupancy of the
corresponding positional cell. If \(\sigma\) chooses one label from each
event pair, with product sign \(\operatorname{sgn}\sigma\), and
\(h_\eta(\sigma)\) selected labels lie in cell \(\eta\), then the exact
signed bijection weight is
\[
\begin{aligned}
&\sum_\sigma\operatorname{sgn}(\sigma)
 \prod_\eta {c_\eta-m_\eta\choose u_\eta-h_\eta(\sigma)}
 u_\eta!(c_\eta-u_\eta)!\\
&\quad=\prod_\eta(c_\eta-m_\eta)!
 \sum_\sigma\operatorname{sgn}(\sigma)
 \prod_\eta(u_\eta)_{h_\eta(\sigma)}
 (c_\eta-u_\eta)_{m_\eta-h_\eta(\sigma)}.               \tag{H.15A.7}
\end{aligned}
\]
Thus, after common factorials are removed, the marked-label factor has
degree four. Fix the first positional blocker at relative start zero. If
the other starts and root start are \(d_1,\ldots,d_a,u\), exactly
\[
 b-|\{0,-d_1,\ldots,-d_a,-u\}|                            \tag{H.15A.8}
\]
translates retain every displayed start.

For \(r\ge23\), five \(\{\pm1,\pm3\}\)-steps from \(\{0,5\}\) lift
without modular collision. Under the inverse cut relabelling
\[
 \phi_r(2h)=-h,\qquad \phi_r(2h+1)=r-h\pmod b,            \tag{H.15A.9}
\]
even and odd cuts form two bounded clusters. Every blocker joins opposite
parities, so its two complementary long gaps have different membership
vectors. Every Venn signature therefore has exactly two macroscopic cells,
of sizes \(r+a,r+c\), with all remaining cells bounded.

There are twenty macroscopic-factor types. For each, factor the two
macroscopic factorials and the bounded-cell factorials in (H.15A.7).
The remaining coefficient has degree at most six: four from
(H.15A.7), one from (H.15A.8), and at most one from summing the
piecewise-polynomial root start. Expanding these twenty explicitly gives
\[
 Q(r)=(r-7)(r-6)\prod_{h=1}^5(r-h)^2r^3(r+1),              \tag{H.15A.10}
\]
and, with \(x=r-23\),
\[
 P(r)=\sum_{i=0}^{26}a_ix^i,                              \tag{H.15A.11}
\]
where the coefficients in increasing order are
\[
\begin{aligned}
(a_0,\ldots,a_{26})={}&(
62981083599956614478115107174154240,
83731019301859283369193624773455872,\\
&53503167323082065050576460728060416,
21874508927965046394283771602943488,
6426381234586609560264944170832256,\\
&1444365103196196379308996566942592,
258170481804935360887224705464448,
37662599276106501292922749610480,\\
&4566280031383604538889761516544,
466127777416902336699609774388,
40438710544492245034672425456,\\
&3001278408729229165219406704,
191400833973788705746237666,
10515008159209256633718591,\\
&498043778207751522889761,
20322149467297451253335,
712577696918492023585,\\
&21377614697429068690,
545129461736876970,
11706023019295518,
208959527775844,\\
&3045080777091,35300366213,313170763,1997129,8152,16).
\end{aligned}                                             \tag{H.15A.12}
\]
Equations (H.15A.7)--(H.15A.9) are an exact finite evaluator for every
term; collecting its twenty types gives
\(\det\mathsf M_r^{(6)}=P(r)/(12Q(r)^2)\). Every coefficient in
(H.15A.12) and every denominator factor is positive for \(r\ge23\),
proving the sign. Exact division also gives (H.15A.6).

For the uniform bound, \(P(r)\ge16(x^{26}+1)\ge
2^{-21}(x+1)^{26}\), while \(x+1=r-22\ge r/23\),
\(23^{26}<2^{130}\), every one of the sixteen linear factors of \(Q\)
is at most \(2r\), and \(12<2^4\). Substitution in (H.15A.5) gives
\(\det\mathsf M_r^{(6)}\ge2^{-187}r^{-6}\). \(\square\)

The rooted hypothesis cannot be discarded by a norm perturbation. Adding
all radius-five six-vertex sets containing both roots, including components
meeting neither root, gives a finite augmented matrix \(\widetilde{\mathsf
M}_r\) with
\[
 \det\widetilde{\mathsf M}_r
 =-3r^{-7}+{929\over12}r^{-8}+O(r^{-9});                  \tag{H.15A.13}
\]
both the \(r^{-5}\) and \(r^{-6}\) terms cancel. This finite bank is not
the full remote dressing, so it is not a counterexample. It proves only
that the remaining full-exposure theorem must resum all rootless
components or find an invariant stable under their common-shore action.
