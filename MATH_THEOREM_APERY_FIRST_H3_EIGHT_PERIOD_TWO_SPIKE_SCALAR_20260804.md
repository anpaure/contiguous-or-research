# First depth-three multidefect Apéry geometry: period eight and the two-spike scalar

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical classification and reduction. It
proves that reflected-ray overlap depth three first becomes possible at
period eight, gives the exact gap inequalities, constructs a genuine
two-defect example, and reduces its endpoint comparison to an explicit
two-parameter scalar. It closes a nontrivial scalar subchamber, but not
every depth-three word or universal Bellman positivity.

## 1. Setup and overlap criterion

Let

\[
 0=s_0<s_1<\cdots<s_{h-1}<P,\qquad
 P+s_1=A,\qquad A={\sqrt\pi\over2}
\tag{1.1}
\]

be an honest cyclic Apéry table at exact first carry. Write

\[
 \gamma_1=s_1,\qquad
 \gamma_j=s_j-s_{j-1}\ (2\le j<h),\qquad
 \gamma_h=P-s_{h-1},\qquad a=\gamma_1.
\tag{1.2}
\]

Every gap is at least \(a\). Let \(u\) be the number of shifts above
\(A/2\), and define

\[
 X_i={s_{i+1}\over A},\qquad
 Y_i={A-s_{h-i}\over A},\qquad
 I_i=[X_i,Y_i)\quad(1\le i\le u).
\tag{1.3}
\]

The endpoints are increasing, \(X_i\le Y_i\), and

\[
 u+1<h-u,\qquad
 H=\max_t\#\{i:t\in I_i\}.
\tag{1.4}
\]

### Lemma 1.1

For increasing endpoints,

\[
 H\ge r
 \quad\Longleftrightarrow\quad
 X_{i+r-1}<Y_i
 \quad\hbox{for some }1\le i\le u-r+1.
\tag{1.5}
\]

#### Proof

For a consecutive block of \(r\) intervals, the latest left endpoint is
\(X_{i+r-1}\) and the earliest right endpoint is \(Y_i\). Any \(r\)
intersecting intervals contain such a consecutive block. This proves both
directions. \(\square\)

For \(r=3\), (1.5) is

\[
 s_{i+3}+s_{h-i}<A=P+s_1,
\]

or, in gap coordinates,

\[
 \boxed{
 \gamma_{h-i+1}+\cdots+\gamma_h
 >
 \gamma_2+\cdots+\gamma_{i+3}.}
\tag{1.6}
\]

Thus depth three means that a terminal block of \(i\) gaps outweighs an
initial block containing two additional gaps.

## 2. Period eight is first

### Theorem 2.1

If \(H\ge3\), then

\[
                         \boxed{h\ge8.}
\tag{2.1}
\]

At \(h=8\), necessarily \(u=3\). Put

\[
 L=\gamma_2+\gamma_3+\gamma_4,\qquad T=\gamma_8.
\tag{2.2}
\]

Then \(H=3\) holds exactly when

\[
 \boxed{
 T>L,\qquad
 L+\gamma_5>T+\gamma_6+\gamma_7.}
\tag{2.3}
\]

Every such word has at least two exceptional gaps:

\[
                         \boxed{\gamma_8>3a,\qquad\gamma_5>2a.}
\tag{2.4}
\]

#### Proof

Depth three requires \(u\ge3\). From \(u+1<h-u\), one gets \(h\ge8\).
At \(h=8\), the same inequalities force \(u=3\). The three intervals have
a common point exactly when

\[
 X_3<Y_1
 \quad\Longleftrightarrow\quad
 s_4+s_7<A.
\]

Since \(s_4=a+L\), \(s_7=P-T\), and \(A=P+a\), this is \(T>L\).
For the converse, that inequality gives

\[
 A-2s_4=\gamma_5+\gamma_6+\gamma_7+T-L>0,
\]

so \(s_4<A/2\). The remaining condition \(u=3\) is \(s_5>A/2\). Using

\[
 s_5=a+L+\gamma_5,\qquad
 A=2a+L+\gamma_5+\gamma_6+\gamma_7+T,
\]

this is the second inequality in (2.3). Finally
\(L\ge3a\) and \(\gamma_6+\gamma_7\ge2a\) prove (2.4). \(\square\)

Hence the universal assertion \(H\le2\) is false, and its first failure
cannot be a disguised one-defect long wrap.

## 3. The sparsest period-eight face

Consider

\[
 \boxed{
 (\gamma_1,\ldots,\gamma_8)=(a,a,a,a,b,a,a,t).}
\tag{3.1}
\]

### Lemma 3.1

The word (3.1) is honest if and only if

\[
                         t\ge b\ge a.
\tag{3.2}
\]

Within that face, \(u=H=3\) if and only if

\[
                         \boxed{t>3a,\qquad b>t-a.}
\tag{3.3}
\]

#### Proof

Subtract the common baseline \(a\). The only positive excesses occur at
positions five and eight, with weights \(b-a\) and \(t-a\). Prefixes of
length at most four have zero excess. Prefixes of lengths five through
seven contain only the position-five excess, while every cyclic block of
those lengths contains at least one of the two excess positions. Hence
all prefix-minimum inequalities hold exactly when \(t-a\ge b-a\). These
inequalities are equivalent to carry-aware superadditivity.

Now (2.3) has \(L=3a\), \(\gamma_6+\gamma_7=2a\), and \(T=t\), giving
exactly (3.3). \(\square\)

The choice

\[
                         b=t=4a
\tag{3.4}
\]

is an explicit honest, genuinely two-defect, depth-three word.

## 4. Exact two-parameter scalar

Write

\[
 v={t\over a}>3,\qquad
 \eta={t-b\over a},\qquad
 0\le\eta<1,\qquad
 D=7+2v-\eta.
\tag{4.1}
\]

Exact first carry gives

\[
 a={A\over D},\qquad
 P=(6+2v-\eta)a.
\tag{4.2}
\]

The seven shifts are

\[
 a,2a,3a,4a,(4+v-\eta)a,(5+v-\eta)a,(6+v-\eta)a.
\tag{4.3}
\]

Put

\[
 F(w)=\sum_{q\ge0}K(qA+w),\qquad
 f(x)=F(Ax),\qquad g(x)=\rho(Ax),\qquad C=F(0).
\tag{4.4}
\]

Reflecting the last three shifts and pairing \(F(a)+F(P)=\rho(a)\)
gives the exact endpoint-period scalar

\[
\boxed{
\begin{aligned}
 \mathcal E(v,\eta)
 ={}&C+g(1/D)
 +\sum_{j=2}^{4}f(j/D)
 -\sum_{j=1}^{3}f((v+j)/D)\\
 &+\sum_{j=1}^{3}g((v+j)/D).
\end{aligned}}
\tag{4.5}
\]

The exact first carry is a legal size-\(9\) configuration of value \(A\).
Repeating it and using monotonicity of \(K\) above \(A\) gives

\[
                         \boxed{\Phi(W)\ge\mathcal E(v,\eta).}
\tag{4.6}
\]

Thus the sparsest first depth-three obstruction is the explicit
two-variable scalar (4.5) on \(v>3,\ 0\le\eta<1\).

## 5. A closed scalar subchamber

### Theorem 5.1

If

\[
                         3<v\le {9+\eta\over2},
\tag{5.1}
\]

then

\[
 \boxed{
 \mathcal E(v,\eta)>{333\over140000}>0,
 \qquad \Phi(W)>0.}
\tag{5.2}
\]

#### Proof

Condition (5.1) is \(D\le16\), so \(4/D\ge1/4\). Also \(D>12\), so
\(2/D,3/D<1/4\). Since \(v>3\),

\[
 {v+1\over D}>{1\over4},
\]

and all three reflected points lie below \(1/2\). The compact train
decreases on \([1/4,1/2]\), whence

\[
                         f(4/D)\ge f((v+1)/D).
\tag{5.3}
\]

The authenticated bounds give

\[
 f(2/D),f(3/D)>{57\over1400},\qquad
 f((v+2)/D),f((v+3)/D)<{61\over1000}.
\tag{5.4}
\]

The theta error is positive on \([1/4,1/2]\), so all three reflected theta
terms are positive, while

\[
                         g(1/D)>-{1\over20000}.
\tag{5.5}
\]

Therefore

\[
\begin{aligned}
 \mathcal E(v,\eta)
 &>{43\over1000}
   +2{57\over1400}
   -2{61\over1000}
   -{1\over20000}\\
 &={333\over140000}>0.
\end{aligned}
\]

Equation (4.6) completes the proof. \(\square\)

The witness \(b=t=4a\) has \((v,\eta)=(4,0)\), \(a=A/15\), and belongs
to this closed subchamber. It disproves \(H\le2\) but is not a Bellman
counterexample. The unresolved two-spike scalar is confined to

\[
                         \boxed{v>{9+\eta\over2}.}
\tag{5.6}
\]

## 6. Scope and frozen dependencies

The theorem classifies the first possible depth-three period and the
sparsest two-spike face. It does not prove that every period-eight
depth-three word compresses to that face, and it does not address
\(h>8\), \(H>3\), threshold overshoot, later first crossing, or the finite
shoulder between a physical clock and its formal Apéry clock.

| role | file | SHA-256 |
|---|---|---|
| prefix-minimum and reflected-ray theorem | MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md | 28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e |
| independent audit | MATH_AUDIT_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_INDEPENDENT_20260804.md | afcbe9eb2bf84c609e7654df49e8a90b6895f4e72fa9aea8b5b1be851a962f8d |
| compact train bounds and quarter-half decrease | MATH_THEOREM_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_20260804.md | 4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0 |
| compact-train audit | MATH_AUDIT_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_INDEPENDENT_20260804.md | 1045aba0ab3a372f0e822f9e61702e600240c73eee61faa1916676a4790c7f8b |
| theta half-interval monotonicity | MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md | f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3 |
