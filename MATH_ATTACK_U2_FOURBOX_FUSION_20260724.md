# Second-wave U: four-box fusion, dyadic drain rigidity, and literal surface atlases

Date: 2026-07-24

## 1. Verdict

This lane produced two exact positive reductions and two exact scoped construction results, but it did not prove the compact four-box theorem unconditionally.

1. A four-chain local condition, **Dyadic Projective Drain Averaging** (DPDA), is enough to prove the full uniform estimate
   \[
   \sup_{0\le \ell_i\le CR}
   \frac{g_4(\ell_1,\ell_2,\ell_3,\ell_4)-w_4(\ell_1,\ell_2,\ell_3,\ell_4)}{R^3}
   \longrightarrow 0
   \tag{1.1}
   \]
   for every fixed \(C\).  The proof is integral: it uses the exact outer-hook partition inside one four-chain factor and literal child words.

2. An independent audit shows
   \[
   \boxed{\mathrm{DPDA}\iff\mathrm{DRAY}.}
   \tag{1.2}
   \]
   Thus averaging the nonnegative defects of the three-box children is not a genuine weakening of the already isolated dominant-ray theorem.  One bad dominant ray persists on a one-sided neighborhood and contaminates linearly many consecutive drain children.  DPDA is still much narrower than the full compact three-box gate, because it is equivalent only to the strongly dominant cone \(c\ge2b\), not to balanced three-boxes.

3. A structurally weaker **unproved** next gate is adjacent-packet fusion: cover two consecutive translated drain children by one literal word at their combined widths plus \(o(R^2)\).  This gate directly implies (1.1), while making no separate near-width demand on either three-box child.  Its existence remains open, and strict logical separation from DRAY is not proved.

4. For the equal box, every single fixed high/low chamber of the upper rank surface has an explicit literal universal atlas of length
   \[
   |L_{2m-1}|+O(m^2),
   \tag{1.3}
   \]
   with all constants and witnesses given below.  The four chamber atlases use essentially the same \(\Theta(m^3)\) physical layer points in generally different arm orders.  No ordering sharing those occurrences with \(o(m^3)\) repetitions was found.  Consequently (1.3) is not yet a four-chamber surface braid and does not prove \(g_4=w_4+o(R^3)\).

5. A new alternating slice word gives
   \[
   g_3(A,B,C)\le(A+1)(B+C),
   \tag{1.4}
   \]
   improving the elementary slice word by exactly \(A\).  It is optimal in the precisely defined adjacent whole-arm gluing class, but its dominant-ray excess is still \((A+1)(C-1)=\Theta(R^2)\).

All statements labelled **UNPROVED** below are hypotheses or remaining fusion lemmas.  No MWB, labelled synchronization, fractional averaging, additive slab reset, web search, or finite/computational search is used.

## 2. Notation

For \(d\ge1\), let \(g_d(\ell_1,\ldots,\ell_d)\) be the minimum length of a word of nonzero points of
\[
[0,\ell_1]\times\cdots\times[0,\ell_d]
\]
whose contiguous coordinatewise maxima contain every nonzero point of the box.  Let \(w_d(\boldsymbol\ell)\) be the width of the product of chains, namely the largest coefficient of
\[
\prod_{i=1}^dP_{\ell_i}(u),
\qquad P_h(u)=1+u+\cdots+u^h.
\]
Put
\[
E_d(\boldsymbol\ell)=
\bigl(g_d(\boldsymbol\ell)-w_d(\boldsymbol\ell)\bigr)_+\ge0.
\tag{2.1}
\]
The positive part only matters for the all-zero degenerate box, where the
excluded origin gives \(g_d=0<w_d=1\).  On every positive ray used in DRAY,
it equals the ordinary defect.

The crude literal bounds used below are
\[
g_3(x,y,z)+1\le(x+1)(y+z+1)
\le(1+x+y+z)^2
\tag{2.2}
\]
after permuting the sides so that \(x\) is the chosen sliced coordinate, and
\[
g_4(\boldsymbol\ell)+1\le(1+\ell_1+\cdots+\ell_4)^3.
\tag{2.3}
\]
They follow from the standard literal face-by-face construction; no asymptotic theorem is hidden in them.

Chain-box width is coordinatewise monotone.  To see this when one side is enlarged by \(d\), shift every point of a central layer of the smaller box upward in that coordinate by
\[
\left\lfloor\frac{S+d}{2}\right\rfloor-\left\lfloor\frac S2\right\rfloor\in[0,d],
\]
where \(S\) is the old total side sum.  This injects the old central layer into the new central layer.  Iterating proves the assertion.

## 3. Exact outer-hook drain

The starting identity is
\[
P_r(u)P_s(u)=P_{r+s}(u)+uP_{r-1}(u)P_{s-1}(u),
\qquad1\le r\le s.
\tag{3.1}
\]
It is literal: the first term is the saturated outer hook in the (r\)-by-(s) rectangle, while the complement is one rank above a product of chains of heights (r-1,s-1).  The residual shift is total rank one, not two.

Given a residual four-box, sort its actual residual chain segments by height
\[
h_1\le h_2\le h_3\le h_4.
\]
Apply (3.1) to the two largest segments.  Emit
\[
C_j=(x_j,y_j,z_j)=(h_1,h_2,h_3+h_4),
\tag{3.2}
\]
decrement (h_3,h_4), retain the forced rank-one residual translation, and re-sort the actual segments together with their offsets.  Stop with the terminal degenerate child when at most one height is positive.  Denote this drain by
\[
\mathcal D(\boldsymbol\ell)=(C_0,\ldots,C_{N-1}).
\]

### Theorem 3.1 (exact drain calculus — PROVED)

Let (S=\sum_i\ell_i).  Then:

\[
z_j\ge2y_j\ge2x_j,
\qquad
N\le\left\lfloor\frac S2\right\rfloor+1,
\tag{3.3}
\]

\[
\prod_{i=1}^4P_{\ell_i}(u)
=\sum_{j=0}^{N-1}u^jP_{x_j}(u)P_{y_j}(u)P_{z_j}(u),
\tag{3.4}
\]

\[
\boxed{w_4(\boldsymbol\ell)=\sum_{j=0}^{N-1}w_3(C_j),}
\tag{3.5}
\]
and
\[
\boxed{E_4(\boldsymbol\ell)
\le N-1+\sum_{j=0}^{N-1}E_3(C_j).}
\tag{3.6}
\]
Before subtracting widths, the literal construction gives
\[
\boxed{
g_4(\boldsymbol\ell)
\le N-1+\sum_{j=0}^{N-1}g_3(C_j).}
\tag{3.6a}
\]

Moreover the emitted children move monotonically inward.  Whenever (C_j) exists,
\[
C_j\le C_0\quad\hbox{coordinatewise},
\qquad
\boxed{\|C_0-C_j\|_1=2j.}
\tag{3.7}
\]

#### Proof

Dominance (3.3) follows from (h_3,h_4\ge h_2), and each nonterminal peel lowers the residual side sum by two.  Iterating the literal partition (3.1) gives (3.4).  The child at step (j) has side sum (S-2j), so
\[
\left\lfloor\frac S2\right\rfloor-j
=\left\lfloor\frac{S-2j}{2}\right\rfloor.
\]
Taking the coefficient of (u^{\lfloor S/2\rfloor}) in (3.4) proves (3.5) for both parities.  If the Boolean parent has bottom rank (B), the child bottoms are forced to be (B+j); they are not independently shiftable.

Translate a local child word into its literal child subposet.  Every noninitial translated child has a nonzero local origin, so prepend that origin once.  Concatenating the child blocks preserves every internal witness and costs at most \(N-1\) anchors.  Subtracting (3.5) gives the raw-defect inequality; taking positive parts gives (3.6).

At one peel every labelled residual height is unchanged or decreases by one.  Hence every sorted order statistic is nonincreasing, and so are (x_j,y_j,z_j).  Their sum is the residual side sum (S-2j).  Coordinatewise monotonicity therefore makes the (L^1) loss exactly (2j), proving (3.7).  This sharpens the harmless bound (4j) obtained by bounding the three coordinates separately.  ∎

## 4. Dyadic Projective Drain Averaging

Let (\mathcal P_{\rm dyad}) be the set of positive sorted integer four-tuples
\[
\mathbf p=(p_1,p_2,p_3,p_4),
\qquad
p_1+\cdots+p_4=2^q
\tag{4.1}
\]
for some (q\ge2).

> **DPDA — UNPROVED.** For every fixed (\mathbf p\in\mathcal P_{\rm dyad}), if
> \[
> \mathcal D(t\mathbf p)=(C_0(t),\ldots,C_{N(t)-1}(t)),
> \]
> then
> \[
> A_{\mathbf p}(t):=
> \sum_{j=0}^{N(t)-1}E_3(C_j(t))
> =o_{\mathbf p}(t^3)
> \qquad(t\to\infty).
> \tag{DPDA}
> \]

It is enough to test primitive (\mathbf p).  Indeed, if (d=\gcd(p_1,\ldots,p_4)), then (d\mid2^q), hence (d) is a power of two and (\mathbf p/d\) is again dyadic.  The drain of (t\mathbf p) is literally the drain of ((dt)(\mathbf p/d)).

### Proposition 4.1 (sparse-bad form — PROVED)

DPDA is equivalent to
\[
\forall\eta>0,\qquad
\#\{j:E_3(C_j(t))>\eta t^2\}=o_{\mathbf p,\eta}(t)
\tag{4.2}
\]
for every fixed dyadic (\mathbf p).

#### Proof

Put (Q=|\mathbf p|).  Then
\[
N(t)\le Qt/2+1,
\qquad
E_3(C_j(t))\le(Qt+1)^2
\tag{4.3}
\]
by (2.2).  DPDA implies (4.2) by Markov.  Conversely split the sum at \(\eta t^2\):
\[
A_{\mathbf p}(t)
\le\eta t^2(Qt/2+1)+(Qt+1)^2o(t).
\]
Divide by \(t^3\), first let \(t\to\infty\), and then let \(\eta\downarrow0\).  ∎

## 5. Direct dyadic mesh to the four-box theorem

### Lemma 5.1 (four-box face extension — PROVED)

If (\mathbf a\le\boldsymbol\ell) coordinatewise, then
\[
g_4(\boldsymbol\ell)
\le g_4(\mathbf a)
+\sum_{i=1}^4(\ell_i-a_i)
\left(1+\sum_{r<i}\ell_r+\sum_{r>i}a_r\right)^2.
\tag{5.1}
\]
In particular, if (0\le a_i\le\ell_i\le CR),
\[
E_4(\boldsymbol\ell)
\le E_4(\mathbf a)
+\|\boldsymbol\ell-\mathbf a\|_1(3CR+1)^2.
\tag{5.2}
\]

#### Proof

Extend the coordinates in order.  For each new value in coordinate (i), append a three-box word for the corresponding fixed-coordinate face, together with its local face origin.  The fixed new coordinate is positive, so every appended letter is a legal nonzero four-box letter.  Every target outside the old box has some newly extended coordinate and receives a witness wholly inside its corresponding face.  Formula (2.2) bounds that face block by the square in (5.1).  Finally use coordinatewise width monotonicity to pass from the (g_4) inequality to (5.2).  ∎

### Theorem 5.2 (DPDA implies uniform four-box excess — CONDITIONAL)

If DPDA holds, then for every fixed (C>0),
\[
\boxed{
\sup_{0\le\ell_i\le CR}
\frac{E_4(\boldsymbol\ell)}{R^3}\longrightarrow0.}
\tag{5.3}
\]

#### Proof: a small side

Fix (\varepsilon>0).  If (\min_i\ell_i<\varepsilon R), then every drain child has (x_j<\varepsilon R), while (y_j\le CR), (z_j\le2CR), and (N\le2CR+1).  By the pre-subtraction literal inequality (3.6a) and (2.2),
\[
g_4(\boldsymbol\ell)
\le(2CR+1)(\varepsilon R+1)(3CR+1).
\]
Consequently
\[
\limsup_{R\to\infty}
\sup_{\min\ell_i<\varepsilon R}
\frac{E_4(\boldsymbol\ell)}{R^3}
\le6C^2\varepsilon.
\tag{5.4}
\]

#### Proof: the positive compact sector

After a common coordinate permutation, assume
\[
\varepsilon R\le\ell_1\le\ell_2\le\ell_3\le\ell_4\le CR,
\qquad S=\sum_i\ell_i,
\]
and put
\[
\kappa=\left\lceil\frac{4C}{\varepsilon}\right\rceil.
\tag{5.5}
\]
Fix a dyadic (Q=2^q), large enough that positive order-preserving largest-remainder rounding is available.  Choose sorted positive integers (p_i) satisfying
\[
\sum_ip_i=Q,
\qquad
\left|p_i-\frac{Q\ell_i}{S}\right|<1.
\tag{5.6}
\]
Set
\[
h=\left\lfloor\frac{S}{Q+\kappa}\right\rfloor.
\tag{5.7}
\]
Because (S\le\kappa\ell_i),
\[
hp_i
\le\frac{S}{Q+\kappa}
\left(\frac{Q\ell_i}{S}+1\right)
\le\ell_i.
\tag{5.8}
\]
The opposite rounding inequalities give
\[
\ell_i-hp_i
\le\frac{C(\kappa+4)}{Q+\kappa}R+Q,
\]
hence
\[
\|\boldsymbol\ell-h\mathbf p\|_1
\le\frac{4C(\kappa+4)}{Q+\kappa}R+4Q.
\tag{5.9}
\]

At fixed (\varepsilon,C,Q),
\[
h\ge\frac{4\varepsilon}{Q+\kappa}R-1\longrightarrow\infty.
\]
Only finitely many positive compositions of \(Q\) occur.  Thus the pointwise \(o_{\mathbf p}(h^3)\) in DPDA is uniform over this finite catalogue.  Equation (3.6) gives
\[
E_4(h\mathbf p)
\le N(h\mathbf p)-1+A_{\mathbf p}(h)
=o_{\varepsilon,C,Q}(R^3)
\tag{5.9a}
\]
uniformly over that catalogue.  Equations (5.2), (5.9), and (5.9a) yield
\[
\limsup_{R\to\infty}
\sup_{\varepsilon R\le\ell_i\le CR}
\frac{E_4(\boldsymbol\ell)}{R^3}
\le
\frac{36C^3(\kappa+4)}{Q+\kappa}.
\tag{5.10}
\]

The order of limits is essential:

1. fix (C,\varepsilon,Q);
2. let (R\to\infty);
3. let the fixed dyadic (Q\to\infty);
4. let (\varepsilon\downarrow0).

Combining (5.4) and (5.10) proves (5.3).  No rate uniformity across an infinite ray catalogue was assumed.  ∎

### Corollary 5.3 (constant one — CONDITIONAL)

DPDA implies
\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{5.11}
\]

#### Scope of the implication

Split the Boolean coordinates into four balanced blocks, take arbitrary SCDs, and write (R=\sqrt{k}).  The number of four-chain parents is (\Theta(W(k)/R^3)).  Equation (5.3) contributes (o_C(W(k))) on parents of height at most (CR).  Parent-minimum anchors contribute (O(W/R^3)).  Long parents are disposed of by the established truncated zeroth and third SCD height moments, giving (O(e^{-cC^2}W)); a pointwise Gaussian tail alone would not suffice.  First let (k\to\infty), then (C\to\infty).  Exact parent widths add to (W(k)), and every local word is literal inside its exact factor.

## 6. Rigidity: DPDA is exactly DRAY

Recall the sole dominant-ray hypothesis from the first wave.

> **DRAY — UNPROVED.** For every fixed primitive integer triple
> \[
> 0<a<b,\qquad c>2b,
> \]
> one has
> \[
> E_3(at,bt,ct)=o_{a,b,c}(t^2).
> \tag{DRAY}
> \]

In this cone (ct\ge at+bt), so
\[
w_3(at,bt,ct)=(at+1)(bt+1).
\]

### Theorem 6.1 (DPDA-DRAY equivalence — PROVED)

\[
\boxed{\mathrm{DPDA}\iff\mathrm{DRAY}.}
\tag{6.1}
\]

#### DRAY implies DPDA

Fix a dyadic parent (\mathbf p), put (Q=|\mathbf p|), and fix (\varepsilon>0).  Children with (x_j<\varepsilon t) have total defect at most
\[
(Qt/2+1)(\varepsilon t+1)(Qt+1)
=O_Q(\varepsilon t^3+t^2)
\tag{6.2}
\]
by the slice word.

Every other child lies in
\[
\varepsilon t\le x_j\le y_j\le z_j/2,
\qquad z_j\le Qt.
\tag{6.3}
\]
The scale-first, mesh-second closure of strict DRAY gives, uniformly on (6.3),
\[
E_3(C_j)\le\eta_{\varepsilon,Q}(t)t^2,
\qquad\eta_{\varepsilon,Q}(t)\to0.
\tag{6.4}
\]
Here are the details.  Fix \(L>10/\varepsilon\), put
\[
s_L=\lfloor t/L\rfloor,
\]
and, for a triple \((x,y,z)\) in (6.3), set
\[
A=\lfloor x/s_L\rfloor-4,\qquad
B=\lfloor y/s_L\rfloor-2,\qquad
D=\lfloor z/s_L\rfloor.
\tag{6.4a}
\]
For all large \(t\),
\[
0<A<B,\qquad D>2B,\qquad
s_L(A,B,D)\le(x,y,z)
\tag{6.4b}
\]
coordinatewise, and
\[
\|(x,y,z)-s_L(A,B,D)\|_1<9s_L=O(t/L).
\tag{6.4c}
\]
The coefficient triples in (6.4a) range over a finite set depending only
on \(\varepsilon,Q,L\).  Divide each by its gcd and apply DRAY at the
corresponding integer dilation.  Three-box face extension pays
\(O_Q(t^2/L)\) for (6.4c).  First let \(t\to\infty\) at fixed \(L\), then
let \(L\to\infty\); this proves (6.4).  Zero short sides are handled by
(6.2), not by projective closure.  Summing (6.4) over \(O_Q(t)\) children
and then sending \(\varepsilon\downarrow0\) proves DPDA.

#### Inward persistence lemma

Let (\mathbf v=(an,bn,cn)) and (\mathbf u\le\mathbf v).  Three-box face extension and width monotonicity give
\[
E_3(\mathbf u)
\ge E_3(\mathbf v)-K_{a,b,c}n\|\mathbf v-\mathbf u\|_1,
\qquad
K_{a,b,c}=b+c+1.
\tag{6.5}
\]
Indeed every face coefficient is at most ((b+c)n+1\le K_{a,b,c}n).  Thus a defect (E_3(\mathbf v)\ge\gamma n^2) persists, with at least (3\gamma n^2/4), throughout the coordinatewise-inner (L^1)-ball of radius
\[
\delta n,
\qquad
\delta\le\frac{\gamma}{4K_{a,b,c}}.
\tag{6.6}
\]

#### DPDA implies DRAY

Fix a strict dominant integer triple
\[
\mathbf q=(a,b,c),
\qquad0<a<b,\quad c>2b,
\]
and suppose DRAY fails.  Then for some (\gamma>0) and (n_r\to\infty),
\[
E_3(an_r,bn_r,cn_r)\ge\gamma n_r^2.
\tag{6.7}
\]
Put (M=a+b+c).  Choose
\[
0<\sigma<\frac{c-2b}{2}
\]
and consider the strictly sorted positive parent profile
\[
(a,b,b+\sigma,c-b-\sigma).
\tag{6.8}
\]
For a sufficiently large dyadic (Q), define
\[
p_1=\left\lfloor\frac{Qa}{M}\right\rfloor,
\quad
p_2=\left\lfloor\frac{Qb}{M}\right\rfloor,
\quad
p_3=\left\lfloor\frac{Q(b+\sigma)}{M}\right\rfloor,
\quad
p_4=Q-p_1-p_2-p_3.
\tag{6.9}
\]
Then (0<p_1<p_2<p_3<p_4), so (\mathbf p\in\mathcal P_{\rm dyad}).  Its first drain child has coefficient triple
\[
\mathbf f=(p_1,p_2,p_3+p_4)
=(p_1,p_2,Q-p_1-p_2),
\tag{6.10}
\]
and
\[
\frac{\mathbf f}{Q}\longrightarrow\frac{(a,b,c)}M.
\tag{6.11}
\]

Set
\[
\lambda_Q=\min\left\{\frac a{f_1},\frac b{f_2},\frac c{f_3}\right\},
\qquad
h_r=\lfloor\lambda_Qn_r\rfloor.
\tag{6.12}
\]
Then (h_r\mathbf f\le n_r\mathbf q) coordinatewise, while
\[
D_Q:=\sum_{i=1}^3(q_i-\lambda_Qf_i)\longrightarrow0
\qquad(Q\to\infty).
\tag{6.13}
\]
Choose (Q) so large that (D_Q<\delta/4), where
\[
\delta=\min\left\{1,\frac{\gamma}{4K_{a,b,c}}\right\}.
\]
For all large (r),
\[
\|n_r\mathbf q-h_r\mathbf f\|_1\le\frac\delta2n_r.
\tag{6.14}
\]

Drain the one fixed dyadic ray (h_r\mathbf p).  By (3.7), the first (\rho n_r) children, for any fixed
\[
0<\rho\le
\min\left\{\frac\delta4,\frac{p_1\lambda_Q}{4}\right\},
\tag{6.15}
\]
exist for large (r), are coordinatewise below (n_r\mathbf q), and lie within (\delta n_r) of it.  The second term in (6.15) keeps all four residual segments positive; the first combines (6.14) with the exact motion (2j).

The inward persistence lemma now gives
\[
E_3(C_j)\ge\frac{3\gamma}{4}n_r^2
\qquad(0\le j\le\rho n_r).
\tag{6.16}
\]
Therefore
\[
A_{\mathbf p}(h_r)
\ge\frac{3\gamma\rho}{4}n_r^3-O(n_r^2).
\tag{6.17}
\]
Since (h_r/n_r\to\lambda_Q>0), (6.17) contradicts DPDA for this single fixed (\mathbf p).  Hence DRAY holds.  ∎

### Consequences of the rigidity theorem

1. A dense aspect catalogue does not weaken DRAY: inward persistence turns one bad ray into a positive interval of bad catalogue rays.

2. The present face-extension interpolation cannot replace all integer
   dilations by only \(t=2^r\).  Consecutive scales have a fixed relative
   gap, and this interpolation pays \(\Theta(t^3)\) after summing the drain.
   This is not a logical impossibility theorem for every conceivable
   dyadic-scale construction.  DPDA uses dyadic aspect denominators but all
   integer dilations \(t\to\infty\).

3. A full-support projective or Gaussian average of the separate child
   defects also collapses to DRAY.  Precisely, suppose probability measures
   \(\mu_R\) on positive integer four-tuples satisfy, for every open box
   \(U\) with compact closure in \((0,\infty)^4\),
   \[
   \liminf_{R\to\infty}
   \mu_R\{\boldsymbol\ell:\boldsymbol\ell/R\in U\}>0.
   \tag{6.18a}
   \]
   If
   \[
   \mathbb E_{\mu_R}\left[R^{-3}
   \sum_{C\in\mathcal D(\boldsymbol\ell)}E_3(C)\right]\to0,
   \tag{6.18}
   \]
   then DRAY holds.  Indeed, under failure at \(n_r(a,b,c)\), choose
   \(0<\sigma<(c-2b)/2\) and a small \(\theta>0\).  The parent profile
   \[
   (1-\theta)(a,b,b+\sigma,c-b-\sigma)
   \tag{6.18b}
   \]
   has first child \((1-\theta)(a,b,c)\), strictly coordinatewise below the
   bad target.  Choose \(\theta(a+b+c)<\delta/4\), and then a fixed small
   open box \(U\) around (6.18b).  Every parent
   \(\boldsymbol\ell/n_r\in U\) has its first child coordinatewise inside
   the \(\delta n_r/2\) inward neighborhood and has all four residual
   heights at least \(c_0n_r\) for some fixed \(c_0>0\).  By (3.7), its
   first \(\rho n_r\) children stay in the \(\delta n_r\) neighborhood for
   a fixed \(\rho>0\).  Thus (6.5) gives a drain sum
   \(\Omega(n_r^3)\) throughout \(U\), contradicting (6.18) and (6.18a).

   The four-SCD height law has this local full-support property.  Its
   one-coordinate masses are exactly
   \[
   \Pr(L_s=\ell)=
   \frac{\binom{s}{(s-\ell)/2}-\binom{s}{(s-\ell)/2-1}}
   {\binom{s}{\lfloor s/2\rfloor}},
   \]
   on the appropriate parity lattice.  Stirling's formula gives the limit
   density \(x e^{-x^2/2}\) for \(L_s/\sqrt{s}\), positive at every finite
   \(x>0\).

4. This argument does **not** rule out an average of genuinely fused (g_4-w_4) costs.  Cross-child intervals can avoid paying the separate nonnegative quantities (E_3(C_j)).

## 7. Candidate fused gate with a weaker stated demand

The collapse theorem identifies the first candidate local statement not reduced to DRAY by the separate-child argument.

> **Adjacent-packet fusion — UNPROVED.** Fix (C).  For every four-box parent with (0\le\ell_i\le CR), group consecutive children of its exact drain as
> \[
> (C_0,C_1),(C_2,C_3),\ldots.
> \]
> For every pair, in its actual translated position inside the one exact parent factor, there is a single literal word covering all nonzero targets in the union of the two child subposets, of length at most
> \[
> w_3(C_{2r})+w_3(C_{2r+1})+\epsilon_C(R)R^2,
> \qquad\epsilon_C(R)\ge0,\quad\epsilon_C(R)\to0,
> \tag{APF}
> \]
> uniformly over the parent and the pair.

### Proposition 7.1 (APF implies the four-box theorem — CONDITIONAL)

APF implies (5.3).

#### Proof

There are \(P=\lfloor N/2\rfloor=O_C(R)\) pairs.  Concatenate their
literal pair words; witnesses stay inside their pair blocks.  The exact
width identity (3.5) gives
\[
E_4(\boldsymbol\ell)
\le P\epsilon_C(R)R^2
+\mathbf1_{N\ {\rm odd}}
\bigl(g_3(C_{N-1})+1-w_3(C_{N-1})\bigr).
\tag{7.1}
\]
The leftover term is \(O_C(R^2)\) by (2.2), while the first term is
\(o_C(R^3)\).  An alternative convention that does not include translated
pair origins in APF adds only \(O(1)\) per pair, hence \(O_C(R)\).
Thus \(E_4=o_C(R^3)\) uniformly.  ∎

APF does not ask for a near-width word for either constituent child separately and permits intervals crossing their common hook boundary.  It is therefore structurally weaker in its stated local demand than the compact three-box gate and is not covered by the DPDA-DRAY collapse proof.  A strict logical nonimplication is not proved.  No APF construction is proved here.
The full uniform compact three-box gate does imply APF: concatenate the two
separate child words and add their \(O(1)\) translated origins.  Thus APF is
a weaker consequence in the formal implication sense, although strictness
is open.

## 8. A near-once universal atlas for one equal-box chamber

This section is unconditional and literal, but it covers one chamber of the upper surface rather than the whole four-box.

Fix (m\ge1), put (R=2m-1), and let
\[
L_R=\{x\in[0,m]^4:\ |x|=R\}.
\]
Work in the chamber
\[
\mathcal C=\{y\in[0,m]^4:y_1\ge y_2,\ y_3\ge y_4\}.
\tag{8.1}
\]
For integers (A,B,t), define
\[
X_t(A,B)=(m-A-t,B+t,m-B-1,A),
\tag{8.2}
\]
\[
Y_t(A,B)=(m-A-1,B,m-B-t,A+t).
\tag{8.3}
\]
Whenever their coordinates are legal, these are points of (L_R).

### Theorem 8.1 (one-chamber portal theorem — PROVED)

Let (y\in\mathcal C) have rank
\[
|y|=R+s,
\qquad s\ge1.
\]
Write uniquely
\[
y=(m-A,a,m-B,b),
\qquad m-A\ge a,\quad m-B\ge b,
\tag{8.4}
\]
and put
\[
d=a-B,\qquad e=b-A.
\]
Then (d+e=s-1), so at most one of (d,e) is negative.  Apart from the two extreme corner targets discussed after the proof, exactly one of the following literal intervals represents (y).

1. If (d,e\ge0), then
   \[
   y=\bigvee[\,X_d(A,B),\ldots,X_0(A,B),
   Y_0(A,B),\ldots,Y_e(A,B)\,].
   \tag{8.5}
   \]

2. If (d=-h<0), then
   \[
   y=\bigvee_{t=h}^{h+s}Y_t(A-1,a).
   \tag{8.6}
   \]
   When (A=0), the legal boundary ray is interpreted literally as
   \[
   Y_t(-1,a)=(m,a,m-a-t,t-1),
   \qquad t\ge1.
   \tag{8.7}
   \]

3. If (e=-h<0), then
   \[
   y=\bigvee_{t=h}^{h+s}X_t(b,B-1).
   \tag{8.8}
   \]
   When (B=0), use the legal boundary ray
   \[
   X_t(b,-1)=(m-b-t,t-1,m,b),
   \qquad t\ge1.
   \tag{8.9}
   \]

Every interval has exactly (s+1) letters.

#### Proof

For (8.5), coordinatewise maximization gives
\[
\bigvee[\,X_d,\ldots,X_0,Y_0,\ldots,Y_e\,]
=(m-A,B+d,m-B,A+e)=y.
\]
Its length is (d+e+2=s+1).  The chamber inequalities give all arm bounds.
More explicitly, \(d,e\ge0\) implies \(A+B\le m\), and
\[
0\le d,e\le m-A-B\le m-\max(A,B).
\tag{8.5a}
\]
Thus every letter of the two arms is legal unless \(A=m\) or \(B=m\);
those two extreme cases are handled below.

If (d=-h), then (a=B-h) and (b=A+s+h-1).  The maximum of the increasing interval in (8.6) is
\[
(m-A,a,m-a-h,A-1+h+s)
=(m-A,a,m-B,b).
\]
The inequality \(b\le m-B\) gives
\[
h+s\le m-A-B+1\le m-A+1.
\tag{8.6a}
\]
Also \(a=B-h\), and \(A+h\ge1\), give
\[
h+s\le m-a.
\tag{8.6b}
\]
Thus, when \(A\ge1\), the interval lies in the full ordinary
\((A-1,a)\)-block.  When \(A=0\), negativity of \(d\) gives \(h\ge1\),
and (8.6b) places every point in the boundary range (8.7).  The proof of
(8.8) is symmetric.

The direct case (d,e\ge0) can have (A=m) only for the unique target ((0,0,m,m)), and can have (B=m) only for ((m,m,0,0)).  They are represented by the dedicated two-letter corner intervals
\[
(0,0,m-1,m),(0,0,m,m-1)
\tag{8.10}
\]
and
\[
(m-1,m,0,0),(m,m-1,0,0),
\tag{8.11}
\]
respectively.  ∎

### Corollary 8.2 (explicit near-once chamber word — PROVED)

There is one word (W_m^{\mathcal C}) over (L_R) that represents every point of (\mathcal C) of rank at least (R), and
\[
\boxed{|W_m^{\mathcal C}|\le |L_R|+3m^2-m+4.}
\tag{8.12}
\]

#### Construction and count

For every (0\le A,B\le m-1), put (T_{A,B}=m-\max(A,B)) and output the full block
\[
X_{T_{A,B}}(A,B),\ldots,X_0(A,B),
Y_0(A,B),\ldots,Y_{T_{A,B}}(A,B).
\tag{8.13}
\]
Output also every boundary ray (8.7), with
\[
0\le a\le m-1,\qquad 1\le t\le m-a,
\tag{8.13a}
\]
in increasing \(t\), and every boundary ray (8.9), with
\[
0\le b\le m-1,\qquad 1\le t\le m-b,
\tag{8.13b}
\]
in decreasing \(t\).  Output the two corner blocks (8.10)-(8.11).
Finally append once every point of \(L_R\) not already output.  Rank-\(R\)
targets are then singleton witnesses, and Theorem 8.1 supplies every higher
target with an interval internal to one displayed block or ray.

The (X)-letters are injectively parametrized among themselves, as are the (Y)-letters.  A cross collision satisfies
\[
X_t(A,B)=Y_v(C,D)
\Longrightarrow
C=A+t-1,\quad D=B+t,\quad t+v=1.
\tag{8.14}
\]
Thus only \((t,v)=(0,1)\) and \((1,0)\) occur.  The ordinary catalogue has exactly
\[
2m(m-1)
\tag{8.15}
\]
such repeated occurrences.  The two boundary-ray families contain in total
\[
2\sum_{r=1}^m r=m(m+1)
\tag{8.16}
\]
occurrences.  Charging every boundary occurrence and all four corner letters as excess, even when already present, gives
\[
|W_m^{\mathcal C}|
\le|L_R|+2m(m-1)+m(m+1)+4,
\]
which is (8.12).

### Exact remaining fusion problem

Coordinate swaps give four chamber words, according to which member of each pair \(\{1,2\}\), \(\{3,4\}\) is designated high.  Together the four chambers cover the upper surface, but the four catalogues overlap on \(\Theta(m^3)\) physical points and demand different full-ray orders.  Naive concatenation costs about \(4|L_R|\).  The missing literal theorem is:

> **Four-chamber order fusion — UNPROVED.** Find a common superword of the four chamber atlases with only \(o(m^3)\) repeated physical occurrences, while retaining one of the certified intervals for every upper target.

The one-chamber theorem proves no lower-rank pinning and no arbitrary-aspect compact theorem.  Even a four-chamber upper braid would still need an integral lower-factor construction or a direct whole-box word.

## 9. Repaired odd inward transfer and the surviving parity obstruction

The following local transfer repairs an unsupported first-wave step.  It does not solve four-chamber fusion.

Let (A+B=2r) and put
\[
p_j=(m-A-1,r,m-B-j,r+j).
\tag{9.1}
\]
For every (s\ge1),
\[
\bigvee_{j=0}^sp_j
=(m-A-1,r,m-B,r+s).
\tag{9.2}
\]
provided the displayed letters lie in \([0,m]^4\).  To state the receiving
portal without confusing it with the swapped-baseline letters (8.2)-(8.3),
define, whenever \(A'+B'=c'+d'\),
\[
\mathsf X_t(A',B';c',d')
=(m-A'-t,c'+t,m-B'-1,d'),
\tag{9.3}
\]
\[
\mathsf Y_t(A',B';c',d')
=(m-A'-1,c',m-B'-t,d'+t).
\tag{9.4}
\]
Then the same maximum in (9.2) is the cross interval
\[
\mathsf X_0(A+1,B;r,r+1),
\mathsf Y_0(A+1,B;r,r+1),\ldots,
\mathsf Y_{s-1}(A+1,B;r,r+1)
\tag{9.5}
\]
in the neighboring canonical odd portal.  In particular it is legal when
\[
0\le A\le m-2,\qquad
0\le B,\qquad
s\le m-B,\qquad r+s\le m.
\tag{9.6}
\]

More generally, let (h,u\ge0), (B\ge h), and (h+u\ge1).  The interval (p_{-h},\ldots,p_u) is represented by the balanced portal label
\[
(A+1,B-h).
\]
Writing
\[
c'=\left\lfloor\frac{2r+1-h}{2}\right\rfloor,
\qquad
d'=\left\lceil\frac{2r+1-h}{2}\right\rceil,
\]
the required (X)- and (Y)-parameters are
\[
r-c',\qquad r+u-d'.
\tag{9.7}
\]
Equivalently, for (h=2k) they are
\[
(k,k+u-1),
\tag{9.8}
\]
and for (h=2k+1) they are
\[
(k,k+u).
\tag{9.9}
\]
Here the receiving interval is the corresponding
\(\mathsf X\)-arm down to \(\mathsf X_0\), followed by
\(\mathsf Y_0\) up the stated \(\mathsf Y\)-parameter.  Besides
\[
0\le h\le\min(B,r),\qquad
0\le u\le\min(m-B,m-r),\qquad
h+u\ge1,
\tag{9.10}
\]
one must impose the literal legality inequalities
\[
0\le A\le m-2,\qquad 0\le B-h\le m-1,
\tag{9.11}
\]
\[
0\le r-c'\le\min(m-A-1,m-c'),
\tag{9.12}
\]
\[
0\le r+u-d'\le\min(m-B+h,m-d').
\tag{9.13}
\]
The qualification \(h+u\ge1\) makes the second parameter in the even-\(h\)
formula nonnegative when \(h=0\).  Subject to (9.10)-(9.13), these are exact
literal identities; they only move the ordering problem to neighboring
blocks.

In the established portal regime
\[
2\le q\le\lfloor m/3\rfloor,
\tag{9.13a}
\]
consider an architecture that retains, for every selected even/odd seam,
both specified balanced portal strings: their distinct predecessors and
their common tail \(p_1,\ldots,p_L\), with either orientation allowed.
Same orientation shares no tail occurrence; opposite orientation can share
only the turning occurrence \(p_L\).  Distinct selected seams lie on
distinct physical lines.  The resulting robust repetition ledger is
\[
D'_q=
\sum_{r=0}^{\lfloor(q-2)/2\rfloor}
(2r+1)(q-2-r),
\tag{9.14}
\]
with
\[
D'_{2t}=\frac{t(8t^2-9t+1)}6,
\qquad
D'_{2t+1}=\frac{t(8t^2-3t+1)}6,
\tag{9.15}
\]
and hence
\[
D'_q=\frac16q^3+O(q^2).
\tag{9.16}
\]
The reduction by one point per ray from the earlier \(D_q\) is forced by the legal one-point hairpin obtained after reversing one block.  This is only a lower bound within the all-balanced literal-block architecture.  Every target used to force (9.14) is already in the swapped hard core, so (9.14) is not a lower bound against a hybrid atlas or against the one-chamber construction of Section 8.

## 10. Alternating three-box slice fusion

The second literal construction attacks DRAY directly but stops at a sharp whole-arm barrier.

Let (0\le A\le B\le C), and define
\[
X_s=(s,0,0),\qquad Y_r=(0,r,0),\qquad Z_r=(0,0,r).
\]
For (Q\in\{Y,Z\}), let
\[
M_d(Q)=Q_1,Q_2,\ldots,Q_d,Q_{d-1},\ldots,Q_1
\tag{10.1}
\]
be the two-sided rainbow of length (2d-1).

Construct (W_{A,B,C}) by starting with
\[
Y_B,Y_{B-1},\ldots,Y_1.
\]
For (s=1,\ldots,A), append (M_C(Z),X_s) when (s) is odd and append (M_B(Y),X_s) when (s) is even.  Finish with (Y_1,\ldots,Y_B) if (A) is odd, and with (Z_1,\ldots,Z_C) if (A) is even.  For (A=0), use simply
\[
Y_B,\ldots,Y_1,Z_1,\ldots,Z_C.
\]

### Theorem 10.1 (alternating slice word — PROVED)

Every nonzero point of ([0,A]\times[0,B]\times[0,C]) is a contiguous maximum of (W_{A,B,C}), and
\[
\boxed{|W_{A,B,C}|=(A+1)(B+C).}
\tag{10.2}
\]

#### Proof

Regard the (x=0) slice as a virtual seam between the initial decreasing (Y)-arm and the increasing half of the first (Z)-mountain.  For (x=0), an interval between levels (y,z) has maximum ((0,y,z)); one-zero targets use a singleton and the all-zero target is excluded.

For (1\le s\le A), the hub (X_s) has one adjacent (Y)-half-arm and one adjacent (Z)-half-arm.  The interval from the chosen (y)-level through (X_s) to the chosen (z)-level has maximum exactly ((s,y,z)), and crosses no other positive hub.

Before gluing, the (A+1) slice vertices have total transverse arm incidence ((A+1)(B+C)).  Each of the (A) shared mountains replaces two (d)-arms by (2d-1) letters, saving one, while the (A) positive hubs restore exactly one each.  This proves (10.2).  ∎

This improves the earlier bound
\[
(A+1)(B+C+1)-1
\]
by exactly \(A\).  If \(C\ge A+B\) and \(C\ge1\), then
\[
w_3(A,B,C)=(A+1)(B+1),
\]
so the exact excess of this word is
\[
\boxed{|W_{A,B,C}|-w_3(A,B,C)=(A+1)(C-1).}
\tag{10.3}
\]
For (A=at,B=bt,C=ct), this is
\[
ac\,t^2+(c-a)t-1.
\tag{10.4}
\]
Thus the construction does not prove DRAY.

### Theorem 10.2 (optimality in the adjacent whole-arm class — PROVED, SCOPED)

Consider constructions with the \(A+1\) canonical slice vertices arranged
on a path.  Each virtual slice vertex has one private \(B\)-arm and one
private \(C\)-arm, and each \(d\)-arm must realize all \(d\) positive record
levels.  Arm interiors are disjoint except that, in each adjacent-vertex
gap, at most one pair of facing equal-coordinate whole arms may merge into
one segment.  The \(A\) positive hubs are additional letters.
Mixed-coordinate, fragmented, or nonlocal identifications are excluded.
Every such construction has length at least
\[
(A+1)(B+C),
\tag{10.5}
\]
and the alternating word is optimal.

Indeed a private (d)-arm needs (d) record levels.  A shared segment serving all prefix maxima (1,\ldots,d) from its left endpoint and all suffix maxima (1,\ldots,d) from its right endpoint needs at least (2d-1) letters: before the first (d) it needs (d-1) distinct prefix records, and after the last (d) it needs (d-1) distinct suffix records.  Sharing saves at most one per internal path gap, at most (A) total, and the (A) positive hubs cost (A).  This proves (10.5).

### Lemma 10.3 (common-carrier spacing — PROVED, SCOPED)

Let \(K\ge1\), and let \(S\) be \(K\) distinct positive sliced-coordinate values.  Suppose a word has a chosen carrier
\[
p_s=(s,0,0)
\]
for each (s\in S), and every target ((s,y,z)), (0\le y\le B), (0\le z\le C), has a witness interval containing that chosen carrier.  If (B\le C), then
\[
\boxed{n\ge K(B+1)+C.}
\tag{10.6}
\]

For a fixed carrier, left-suffix and right-prefix transverse maxima are two chains whose joins cover ([0,B]\times[0,C]).  Every ((y,0)) and every ((0,z)) must occur in one of the chains.  A chain cannot contain positive points from both axes, so, after swapping sides, one chain contains the whole (y)-axis and the other the whole (z)-axis.  The carrier needs usable side lengths (B,C).

Order the carriers spatially.  Each internal and exterior carrier gap has at least (B) positions: a smaller sliced value cannot use a witness crossing a larger carrier.  At the carrier with minimum selected sliced value, one adjacent or exterior gap has at least (C) positions.  Thus
\[
n\ge K+(K+1)B+(C-B)=K(B+1)+C.
\]

Routing every positive (z)-slice through ((0,0,z)) gives
\[
n\ge C(A+1)+B,
\]
whose leading ratio to dominant width is at least \(c/b\ge2\) on the
DRAY cone \(c\ge2b\).  Routing the \(A\) positive \(x\)-slices through
\(X_s\) gives only
\[
n\ge A(B+1)+C,
\]
which is compatible with DRAY at leading order.  Neither (10.5) nor (10.6) rules out mixed carriers, multiple carriers, fragmented profiles, or a nonlocal literal braid.

## 11. Final theorem and gap ledger

### Proved unconditionally in this report

- the exact drain motion identity (\|C_0-C_j\|_1=2j);
- the sparse-bad formulation of DPDA;
- the four-box face-extension inequality with explicit shell;
- DPDA (\Rightarrow) uniform (E_4=o_C(R^3)), with the limit order and constants (5.4), (5.10);
- DPDA (\Leftrightarrow) DRAY by one-sided defect amplification;
- collapse of every locally full-support average of separate child defects;
- APF (\Rightarrow) the compact four-box theorem;
- the one-chamber universal surface atlas and the explicit bound (8.12);
- the repaired odd inward transfer (9.2)-(9.13);
- the alternating slice word (10.2);
- optimality of that word in the adjacent whole-arm class;
- the scoped common-carrier lower bound (10.6).

### Unproved

- DRAY, equivalently DPDA;
- adjacent-packet fusion APF;
- four-chamber order fusion with (o(m^3)) repeated occurrences;
- a lower-factor/pinning construction completing the equal-box upper atlas;
- any unconditional compact four-box estimate or new unconditional coefficient-one theorem.

### Exact implication scope

\[
\mathrm{APF}
\Longrightarrow
\sup_{0\le\ell_i\le CR}E_4/R^3\to0
\Longrightarrow
\nu(k)=(1+o(1))W(k),
\tag{11.1}
\]
and
\[
\mathrm{DPDA}
\Longleftrightarrow
\mathrm{DRAY}
\Longrightarrow
\sup_{0\le\ell_i\le CR}E_4/R^3\to0
\Longrightarrow
\nu(k)=(1+o(1))W(k).
\tag{11.2}
\]

The first chain is the candidate fused four-chain route left open by this
attack; its stated local demand is weaker, but strict logical separation is
not proved.  The second chain is a complete audit of why nonnegative
child-defect averaging cannot supply such a weakening.  The one-chamber
atlas gives a separate literal surface advance, but its four-way physical
order fusion remains exactly the unresolved cubic step.

## 12. Independent audit record

Three independent proof audits were run after the first complete draft.
Their decisive checks were as follows.

1. The drain audit verified the literal hook partition, forced rank-one
   shifts, both-parity width telescoping, the exact motion
   \(\|C_0-C_j\|_1=2j\), the finite-catalogue uniformity, the constants
   \(6C^2\varepsilon\) and
   \(36C^3(\kappa+4)/(Q+\kappa)\), and the quantifier order in Theorem 5.2.

2. The rigidity audit independently reconstructed the dyadic parent
   (6.8)-(6.10), checked \(D_Q\to0\), verified the inward shell constant
   \(K_{a,b,c}=b+c+1\), and confirmed that one bad ray forces
   \(\Theta(n)\) consecutive children with \(\Theta(n^2)\) defect.  It also
   found the need for strict inward slack in the Gaussian argument; this is
   the reason for the contraction \(1-\theta\) in (6.18b).

3. The literal-atlas audit checked every coordinate maximum and every arm
   endpoint in Section 8.  It found the two extreme targets
   \((0,0,m,m)\), \((m,m,0,0)\), which are now covered by (8.10)-(8.11),
   and independently obtained the exact ordinary collision count
   \(2m(m-1)\) and boundary charge \(m(m+1)\).

4. The same audit rejected an earlier ambiguous use of the swapped-baseline
   \(X,Y\) notation in the odd transfer.  Section 9 now uses the distinct
   balanced-arm symbols \(\mathsf X,\mathsf Y\), and (9.6),
   (9.10)-(9.13) state the literal legality ranges.  Without this repair,
   the transfer would be false unless \(A=B=r\).

5. The slice-braid audit verified the alternating word by both parity
   counts and checked the lower bounds only under their displayed class
   hypotheses: at most one whole-arm merger per adjacent gap for Theorem
   10.2, and \(K\ge1\) plus a fixed common carrier for Lemma 10.3.

After these repairs, no auditor found a remaining substantive error.  The
unproved statements remain exactly DRAY/DPDA, APF, four-chamber order
fusion, and lower-factor completion; none is promoted by the audit.
