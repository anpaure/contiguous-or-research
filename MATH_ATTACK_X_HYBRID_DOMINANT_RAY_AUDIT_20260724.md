# Adversarial audit: hybrid dominant-ray reduction

Date: 2026-07-24

Audited source: `MATH_ATTACK_X_HYBRID_DOMINANT_RAY_REPORT_RAW_20260724.md`

## 1. Overall verdict

The main conditional implication is valid:

\[
\boxed{
\mathrm{DRAY}
\Longrightarrow
\sup_{0\le \ell_i\le CR}
\frac{g_4(\boldsymbol\ell)-w_4(\boldsymbol\ell)}{R^3}\to0
\Longrightarrow
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.}
\]

No fatal error was found in the outer-hook recursion, exact width telescoping, parent-error aggregation, or Boolean product-box implication. The report remains conditional because DRAY itself is unproved.

Six scope or proof corrections are required.

1. The phrase “the valid rays are projectively closed” is not by itself a proof. The positive boundary cases \(a=b\) and \(c=2b\) require an explicit inward strict-ray approximation, gcd reduction, and the limit order “scale first, mesh second.” This repair is given below.
2. The cone is relatively closed only inside the positive projective sector \(a>0\). A zero-coordinate ray is not obtained from DRAY by face extension. Zero-coordinate children are nevertheless harmless by the independent slice bound.
3. The literal residual in the outer-hook step is translated upward by total rank one, with one bottom trim and the opposite top trim. Raising both lower endpoints would give the wrong shift.
4. “Arbitrary Boolean-chain bottom shifts” must mean an arbitrary collectively centered parent bottom \(B\), followed by the forced child bottoms \(B+j\). Independently shifting children invalidates the width identity.
5. The shifted-child anchors used in proving the uniform parent estimate are counted a second time in the global section. This is harmless overcounting, but a clean proof should count them only once.
6. The long-parent bound needs truncated zeroth and third height moments. A pointwise Gaussian height tail alone does not justify a cubically weighted sum.

The final “factor 2 is sharp” statement is valid for the prescribed recursion that always pairs the two largest heights. Its broader wording as a theorem about every conceivable adaptive pair-hook decomposition is unsupported.

## 2. Face extension

### Verdict: VALID

The imported face-extension inequality is

\[
\begin{aligned}
g_3(p,q,r)\le g_3(p_0,q_0,r_0)
&+(p-p_0)(q+r+1)\\
&+(q-q_0)(p_0+r+1)\\
&+(r-r_0)(p_0+q_0+1),
\end{aligned}
\tag{2.1}
\]

for \(p_0\le p,q_0\le q,r_0\le r\). Each new fixed-coordinate face is covered by the elementary rectangle word. The fixed new coordinate is positive, so all appended entries are nonzero and no uncharged origin anchor or separator is needed.

The lemma is one-way: it extends an inner box to a coordinatewise larger box. It does not directly restrict a theorem from a boundary ray to a strict inner ray.

The opening cubic bookkeeping observation is correct in its earlier, non-dominant context. For target \((t,t,t)\), fix \(L\), put \(h=\lfloor t/L\rfloor\), and use the inner ray

\[
((L-1)h,Lh,Lh).
\]

The first-coordinate shell has asymptotic cost \((2/L)t^2\), while the other rounding shells cost \(O_L(t)\). Hence

\[
\limsup_{t\to\infty}
\frac{g_3(t,t,t)-w_3(t,t,t)}{t^2}
\le \frac2L+
\frac1{L^2}\limsup_{h\to\infty}
\frac{g_3((L-1)h,Lh,Lh)-w_3((L-1)h,Lh,Lh)}{h^2}.
\]

This confirms the stated \(2/L\) loss. The source ray is not in DRAY, and the report does not use it as though it were.

## 3. Dominant-ray cone closure

### Raw wording: PROOF OMITTED

### Corrected verdict: VALID on the positive cone

DRAY assumes, for every primitive fixed triple,

\[
0<a<b,\qquad c>2b,
\]

that

\[
g_3(at,bt,ct)=(at+1)(bt+1)+o_{a,b,c}(t^2).
\tag{3.1}
\]

The width formula is exact because

\[
ct>2bt>at+bt.
\]

More generally, throughout the closed dominant sector

\[
0<a\le b,\qquad c\ge2b,
\tag{3.2}
\]

one has \(c\ge a+b\), so the central coefficient lies on the full plateau and

\[
w_3(at,bt,ct)=(at+1)(bt+1).
\]

To obtain a boundary ray from strict DRAY, fix an integer \(L\) and trim coordinates inward before applying face extension. For example:

- if \(a=b,c>2b\), use coefficients \((aL-1,bL,cL)\);
- if \(a<b,c=2b\), use \((aL,bL-1,cL)\);
- if \(a=b,c=2b\), use \((aL-2,aL-1,2aL)\).

Put \(h=\lfloor t/L\rfloor\). These are positive strict dominant triples for large \(L\), lie coordinatewise below \((at,bt,ct)\) after the harmless rounding gaps are included, and have shell cost

\[
O_{a,b,c}(t^2/L)+O_{a,b,c,L}(t).
\]

If an inner coefficient triple has gcd \(d\), divide it by \(d\) and apply primitive DRAY at scale \(dh\). For fixed \(L\), \(dh\to\infty\). Width monotonicity gives

\[
g_3(\text{target})-w_3(\text{target})
\le
g_3(\text{inner})-w_3(\text{inner})
+\text{shell cost}.
\]

First let \(t\to\infty\) at fixed \(L\), then let \(L\to\infty\). This proves DRAY on every positive boundary ray in (3.2).

The correct wording is therefore:

\[
\boxed{\text{Strict DRAY extends to the relatively closed positive dominant cone.}}
\]

It does not extend by this argument to \(a=0\). For a zero ray, however, the slice word independently gives, for \(b\le c\),

\[
g_3(0,bt,ct)\le (b+c)t,\qquad
w_3(0,bt,ct)=bt+1,
\]

and hence

\[
g_3(0,bt,ct)-w_3(0,bt,ct)\le ct-1=O(t)=o(t^2).
\tag{3.3}
\]

Thus zero-coordinate children are harmless, but not because they are in the projective closure supplied by DRAY.

## 4. Uniform dominant-cone estimate for moving children

### Verdict: VALID AFTER INSERTING THE MESH PROOF

Fix \(\varepsilon,C>0\), and consider integer triples satisfying

\[
\varepsilon R\le x\le y\le z/2,\qquad z\le2CR.
\tag{4.1}
\]

Fix an integer \(L\ge4/\varepsilon\), put \(h=\lfloor R/L\rfloor\), and define

\[
A=\lfloor x/h\rfloor,\qquad
B=\lfloor y/h\rfloor,\qquad
D=\lfloor z/h\rfloor,
\]

\[
a=A-2,\qquad b=B-1,\qquad c=D.
\tag{4.2}
\]

For all sufficiently large \(R\),

\[
a>0,\qquad a<b,\qquad c>2b.
\]

Indeed \(A\le B\), while \(z\ge2y\) gives \(D\ge2B\). The inner box \((ah,bh,ch)\) is coordinatewise below \((x,y,z)\), with

\[
\Delta x<3h,\qquad
\Delta y<2h,\qquad
\Delta z<h.
\tag{4.3}
\]

Using \(y\le CR,z\le2CR\), the face-extension shell is bounded explicitly by

\[
\begin{aligned}
S_{\rm shell}
&<3h(3CR+1)+2h(3CR+1)+h(2CR+1)\\
&=17ChR+6h.
\end{aligned}
\tag{4.4}
\]

For \(R\ge2L\), the possible triples \((a,b,c)\) lie in a finite set depending only on \(L,\varepsilon,C\); for example \(A,B\le2CL\) and \(D\le4CL\). After gcd reduction, DRAY is uniform over this finite set. Hence

\[
\limsup_{R\to\infty}
\sup_{(4.1)}
\frac{g_3(x,y,z)-w_3(x,y,z)}{R^2}
\le\frac{17C}{L}.
\tag{4.5}
\]

Now let \(L\to\infty\). Therefore there is a function \(\eta_{\varepsilon,C}(R)\to0\) such that

\[
g_3(x,y,z)-w_3(x,y,z)
\le\eta_{\varepsilon,C}(R)R^2
\tag{4.6}
\]

uniformly on (4.1). This is the uniform estimate required later in the report.

The essential order of limits is:

1. fix \(\varepsilon,C,L\);
2. let \(R\to\infty\), using only finitely many primitive rays;
3. then refine \(L\to\infty\).

No rate uniformity between infinitely many fixed rays is assumed.

## 5. Outer-hook identity and literal partition

### Verdict: VALID, WITH A TRANSLATION CLARIFICATION

For \(1\le r\le s\), define the saturated chain

\[
H_{r,s}
=\{(0,t):0\le t\le s\}
\cup\{(i,s):1\le i\le r\}
\subseteq[0,r]\times[0,s].
\]

Its rank polynomial is \(P_{r+s}(u)\). Its complement is

\[
\{(i,t):1\le i\le r,\ 0\le t\le s-1\}
=(1,0)+([0,r-1]\times[0,s-1]),
\]

with rank polynomial \(uP_{r-1}(u)P_{s-1}(u)\). Hence

\[
P_r(u)P_s(u)
=P_{r+s}(u)+uP_{r-1}(u)P_{s-1}(u).
\tag{5.1}
\]

The residual translation has total rank one. Literally, one paired chain is bottom-trimmed and the other is top-trimmed. Interpreting the residual as \([1,r]\times[1,s]\) would shift by two and is false; already

\[
P_1(u)^2=P_2(u)+u,
\]

not \(P_2(u)+u^2\).

Multiplying the literal hook partition by the other two chain factors produces a literal three-chain child and a translated residual four-chain box. Re-sorting is valid provided one re-sorts the actual chain segments together with their bottom offsets, not merely the four numerical heights.

## 6. Recursive decomposition

### Verdict: VALID

At step \(j\), sort the actual residual chain segments by heights

\[
h_1\le h_2\le h_3\le h_4.
\]

If \(h_3>0\), apply (5.1) to \(h_3,h_4\). Emit the literal child

\[
(x_j,y_j,z_j)=(h_1,h_2,h_3+h_4),
\]

and retain a residual four-box with heights

\[
h_1,h_2,h_3-1,h_4-1.
\]

The residual minimum rank rises by one, and its maximum rank falls by one. Every emitted child satisfies

\[
z_j=h_3+h_4\ge2h_2=2\max(x_j,y_j).
\tag{6.1}
\]

If \(h_3=0\), at most one height is positive. Include the residual chain as the terminal degenerate child \((0,0,h_4)\), including \((0,0,0)\) when the residual is a singleton.

If \(T\) peeling steps occur and \(S=\sum_i\ell_i\), then

\[
S-2T\ge0,
\]

so

\[
N=T+1\le\left\lfloor\frac S2\right\rfloor+1.
\tag{6.2}
\]

The children form a disjoint literal partition of the original four-box.

At time \(j\), the residual bottom shift is exactly \(j\), and its side sum is \(S-2j\). Therefore the exact polynomial identity is

\[
\prod_{i=1}^4P_{\ell_i}(u)
=
\sum_{j=0}^{N-1}
u^jP_{x_j}(u)P_{y_j}(u)P_{z_j}(u).
\tag{6.3}
\]

## 7. Exact width telescoping

### Verdict: VALID, WITH BOTTOM-SHIFT SCOPE CORRECTED

Let

\[
r=\left\lfloor\frac S2\right\rfloor.
\]

For every child,

\[
x_j+y_j+z_j=S-2j,
\]

and therefore

\[
r-j
=\left\lfloor\frac{S-2j}{2}\right\rfloor
=\left\lfloor\frac{x_j+y_j+z_j}{2}\right\rfloor.
\tag{7.1}
\]

Taking the coefficient of \(u^r\) in (6.3) gives, for both parities of \(S\),

\[
\boxed{
w_4(\boldsymbol\ell)
=\sum_{j=0}^{N-1}w_3(x_j,y_j,z_j).}
\tag{7.2}
\]

If the original parent has Boolean bottom rank \(B\), then child \(j\) has the forced bottom rank \(B+j\). Consequently every child central rank is

\[
B+j+\left\lfloor\frac{S-2j}{2}\right\rfloor
=B+\left\lfloor\frac S2\right\rfloor.
\tag{7.3}
\]

For a four-chain parent formed from symmetric chains in a \(k\)-cube,

\[
2B+S=k,
\]

so (7.3) is exactly \(\lfloor k/2\rfloor\).

Thus arbitrary original Boolean chain-bottom sets are harmless because they satisfy the collective centering relation. The children may not be shifted independently. For example, in

\[
P_1^2=P_2+u,
\]

moving the forced terminal shift from \(u\) to \(u^2\) destroys the central coefficient identity.

The claim that (7.2) is integral rather than fractional is correct: it arises from the literal disjoint hook partition.

## 8. Literal word concatenation and anchors

### Verdict: VALID

Every child is a literal product of three saturated Boolean chain segments on disjoint increment supports. Translation by its child origin preserves coordinatewise maxima, so a local contiguous-maximum word becomes a literal Boolean OR word.

Child \(0\) has the abstract parent origin, which \(g_4\) is not required to cover. Every child \(j\ge1\) has relative origin rank \(j>0\); prepend that origin once. All other witnesses remain wholly inside their translated child word. Therefore

\[
\boxed{
g_4(\boldsymbol\ell)
\le(N-1)+\sum_{j=0}^{N-1}g_3(x_j,y_j,z_j).}
\tag{8.1}
\]

Concatenating child blocks requires no connector because all selected witnessing intervals remain internal to their own blocks. If the Boolean parent minimum itself is nonempty, prepend it once; the unique global empty target is not required.

This also handles a one-point terminal child: its local \(g_3\)-word is empty, while its shifted origin is supplied by the anchor.

## 9. Uniform parent error

### Verdict: VALID

For \(0\le\ell_i\le CR\),

\[
S\le4CR,\qquad N\le2CR+1,\qquad z_j\le2CR.
\]

For every child with \(x_j<\varepsilon R\), the exact slice word gives

\[
g_3(x_j,y_j,z_j)+1
\le(x_j+1)(y_j+z_j+1)
\le(\varepsilon R+1)(3CR+1).
\]

Hence

\[
\sum_{x_j<\varepsilon R}
(g_3(x_j,y_j,z_j)+1)
\le
(2CR+1)(\varepsilon R+1)(3CR+1)
=O_C(\varepsilon R^3+R^2).
\tag{9.1}
\]

Every remaining child lies in (4.1), so (4.6) gives total excess

\[
\le(2CR+1)\eta_{\varepsilon,C}(R)R^2
=o_{\varepsilon,C}(R^3).
\tag{9.2}
\]

The remaining shifted origins cost at most \(N-1=O_C(R)\). Using exact width telescoping,

\[
\limsup_{R\to\infty}
\sup_{0\le\ell_i\le CR}
\frac{(g_4(\boldsymbol\ell)-w_4(\boldsymbol\ell))_+}{R^3}
=O_C(\varepsilon).
\]

Letting \(\varepsilon\downarrow0\) proves

\[
\boxed{
\sup_{0\le\ell_i\le CR}
\frac{(g_4-w_4)_+}{R^3}\to0.}
\tag{9.3}
\]

No lower compactness cutoff on the parent heights is needed. Children with \(x_j=0\), which are not consequences of DRAY, are included in (9.1).

## 10. Global Boolean aggregation

### Verdict: VALID AFTER TWO BOOKKEEPING CLARIFICATIONS

Split \([k]\) into four blocks of sizes \(s_i\) differing by at most one, and choose arbitrary SCDs. The number of four-chain parents is exactly

\[
B_4=\prod_{i=1}^4\binom{s_i}{\lfloor s_i/2\rfloor}.
\]

Stirling gives, for \(R=\sqrt{k}\),

\[
B_4
=\Theta\!\left(\frac{2^k}{k^2}\right)
=\Theta\!\left(\frac{W(k)}{k^{3/2}}\right)
=\Theta\!\left(\frac{W(k)}{R^3}\right).
\tag{10.1}
\]

For a parent with Boolean bottom rank \(B\) and side sum \(S\), \(2B+S=k\). Thus global-middle and local-middle ranks agree exactly. Products of the four SCDs partition the Boolean cube, and (7.2) partitions every recursively treated parent. Therefore

\[
\sum_{\rm long\ parents}w_4
+\sum_{\rm nonlong\ children}w_3
=W(k).
\tag{10.2}
\]

For fixed \(C\), (9.3) and (10.1) give

\[
\sum_{\rm nonlong\ parents}(g_4-w_4)_+
\le B_4o_C(R^3)=o_C(W(k)).
\tag{10.3}
\]

### 10.1 Anchor correction

The shifted-child anchors were already included when deriving (9.3). Counting

\[
O_C(B_4R)=O_C(W(k)/R^2)
\]

again in the global section is harmless double counting. A clean proof using (9.3) should add only the Boolean parent-minimum anchors:

\[
B_4=O(W(k)/R^3)=o(W(k)).
\tag{10.4}
\]

Alternatively, one may sum raw child errors and then add the shifted origins separately. One should not do both.

### 10.2 Long-parent correction

The pointwise Gaussian tail must be upgraded to truncated height moments because the crude word has cubic weight. Let

\[
x_i=1+\ell_i,\qquad
B_i=\binom{s_i}{\lfloor s_i/2\rfloor}.
\]

The SCD height multiset, independent of the selected SCD, satisfies

\[
\sum_{C_i}x_i^3=O(B_iR^3),
\tag{10.5}
\]

and, for \(j=0,3\),

\[
\sum_{C_i:\ell_i>CR}x_i^j
=O\!\left(B_iR^j(1+C)^{j+1}e^{-c_0C^2}\right).
\tag{10.6}
\]

Since

\[
g_4(\boldsymbol\ell)+1
\le(1+\sum_i\ell_i)^3
\le(\sum_i x_i)^3
\le16\sum_i x_i^3,
\]

factorization over chain choices and a union bound over the long coordinate give

\[
\begin{aligned}
\sum_{\max_i\ell_i>CR}(g_4+1)
&=O\!\left(B_4R^3(1+C)^4e^{-c_0C^2}\right)\\
&=O(e^{-cC^2}W(k))
\end{aligned}
\tag{10.7}
\]

after decreasing the absolute constant \(c>0\). This proves the report’s long-parent estimate. Merely citing a pointwise tail without (10.5)–(10.6) is insufficient.

Charging the full long-parent cost while retaining its width in the global \(W(k)\) baseline is an overcount, not an omission.

Combining (10.2)–(10.7),

\[
\nu(k)
\le W(k)+o_C(W(k))
+O(e^{-cC^2}W(k))
+O(W(k)/R^3).
\tag{10.8}
\]

For fixed \(C\), let \(k\to\infty\), and then let \(C\to\infty\). The central antichain gives \(\nu(k)\ge W(k)\). Therefore

\[
\boxed{
\mathrm{DRAY}\Longrightarrow
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.}
\tag{10.9}
\]

No uniformity in a moving \(C=C(k)\) is used.

## 11. Sharpness claim

### Prescribed two-largest recursion: VALID

Starting from \((R,R,R,R)\), the prescribed recursion emits successively

\[
(r,r,2r),
\]

then, from residual \((r-1,r-1,r,r)\),

\[
(r-1,r-1,2r),
\]

and returns to \((r-1,r-1,r-1,r-1)\). Thus \(\Theta(R)\) children have dominance ratio exactly \(2\), and another \(\Theta(R)\) approach \(2\). Replacing the threshold by \(2+\eta\) in this construction leaves \(\Theta(R)\) macroscopic children outside the hypothesized sector; paying their slice-word excess costs \(\Theta(R^3)\).

### All recursive pair-hook decompositions: UNSUPPORTED

The equal-box calculation proves sharpness for the stated “always pair the two largest” recursion. It does not classify every adaptive choice of pairs, every alternative hook orientation, or every more general recursive partition. The opening sentence of the sharpness section should be narrowed accordingly.

## 12. Final valid/corrected/unsupported ledger

### Valid

- exact face extension;
- the opening cubic \(2/L\) bookkeeping observation in its stated earlier context;
- extension of strict DRAY to the positive boundary after the proof in Sections 3–4;
- the outer-hook polynomial identity and its literal chain partition;
- recursive re-sorting when actual chain segments and offsets are retained;
- dominance \(z_j\ge2\max(x_j,y_j)\);
- child count \(N\le\lfloor S/2\rfloor+1\);
- exact polynomial decomposition;
- exact width telescoping for both parities;
- literal child-to-Boolean word transfer and the \(N-1\) anchor bound;
- uniform \(o_C(R^3)\) parent error with no lower parent cutoff;
- four-box count \(B_4=\Theta(W/R^3)\);
- exact global width additivity;
- the corrected long-tail aggregation;
- the order of limits and final conditional implication;
- factor-2 sharpness for the prescribed two-largest recursion.

### Corrected

- “projectively closed” means relatively closed in the positive sector and requires inward trimming, gcd reduction, and two ordered limits;
- zero rays are handled by the slice word, not by DRAY closure;
- the residual hook translation has total rank one;
- bottom shifts are forced \(B+j\), not independently arbitrary;
- shifted-origin anchors should be counted once;
- Gaussian tail language must be replaced by truncated moments through degree three;
- the factor-2 sharpness claim must be restricted to the stated recursion.

### Unsupported / unproved

- DRAY itself;
- any claim that DRAY supplies a zero-coordinate ray by face extension;
- universal factor-2 sharpness for all adaptive pair-hook decompositions;
- any unconditional conclusion for \(\nu(k)\) from this route.

With these corrections, the raw report is a valid theorem-level conditional reduction. Its sole constructional gap is still the dominant local theorem DRAY.
