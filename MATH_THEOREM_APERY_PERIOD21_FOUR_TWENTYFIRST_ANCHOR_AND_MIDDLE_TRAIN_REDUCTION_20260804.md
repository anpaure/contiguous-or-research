# Period twenty-one: the four-twenty-first anchor and middle-train reduction

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem and exact residual
reduction.  It proves positivity of every honest exact-first-carry
period-twenty-one cyclic Apéry clock with at most eight reflected pairs.
It moves the first unresolved chamber to `u=9` and reduces that chamber to
one explicit middle-train/overlap scalar.  No computation or search is
used.  It does not claim positivity of the residual `u=9` chamber.

Put

\[
 A={\sqrt\pi\over2},\qquad
 f(x)=F_A(Ax),\qquad C=F_A(0),\qquad g(x)=\rho(Ax).
\tag{0.1}
\]

Retain the rational prices

\[
 L={5503\over125000},\quad
 G={1079\over20000},\quad
 U={101\over2000},\quad
 Q={1129\over25000},\quad
 \varepsilon={1\over20000}.
\tag{0.2}
\]

Thus `f>L` on `[0,1/4]`, `f<G` globally on the half band,
`f(1/5)<U` with decrease from one fifth, `f<Q` from the quarter onward,
and `|g|<epsilon`, with positive `g` from the quarter onward.

## 1. A rational four-twenty-first anchor

For `0<x<25`, define

\[
 U_{24}(x)=\sum_{j=0}^{23}{x^j\over j!}
 +{x^{24}\over24!\,(1-x/25)}.
\tag{1.1}
\]

The exponential-series tail has consecutive ratio at most `x/25` from
degree twenty-four onward, so

\[
 e^x<U_{24}(x).
\tag{1.2}
\]

### Lemma 1.1

\[
 \boxed{
 f'(x)<0\quad(4/21\le x\le1/2),
 \qquad
 f(4/21)<V:={5127\over100000}
 <{25747\over500000}.}
\tag{1.3}
\]

#### Proof

Put `h(z)=z exp(-pi z^2/4)`.  Termwise differentiation gives

\[
 f'(x)={\pi\over2}
 \left(\sum_{q\ge0}h(1+x+q)-h(1-x)\right).
\tag{1.4}
\]

At `x=4/21`, divide by `h(17/21)`.  Positive Taylor lower bounds at
`pi>333/106` give

\[
 {h(25/21)\over h(17/21)}
 ={25\over17}e^{-4\pi/21}<{81\over100},
\tag{1.5}
\]

and

\[
 {h(46/21)\over h(17/21)}
 ={46\over17}e^{-29\pi/28}<{11\over100}.
\tag{1.6}
\]

Beginning with `z=46/21`, every successive positive-term ratio is at
most

\[
 {67\over46}e^{-113\pi/84}<{1\over30}.
\tag{1.7}
\]

For (1.7), `113pi/84>4` and
`(19/7)^4>2010/46`; equations (1.5)--(1.6) follow by substituting
`333/106` in the positive exponential series and clearing denominators.
Thus the complete positive/adverse ratio is smaller than

\[
 {81\over100}+{11/100\over1-1/30}
 ={2679\over2900}<1.
\tag{1.8}
\]

Hence `f'(4/21)<0`.  For

\[
 R_q(x)={h(1+x+q)\over h(1-x)},
\]

one has

\[
 {d\over dx}\log R_q(x)
 ={1\over1+x+q}+{1\over1-x}-{\pi\over2}(q+2)<0
\tag{1.9}
\]

on `[4/21,1/2]`: for `q=0`, the first two terms are at most
`8/3<pi`; for `q>=1`, they are less than `5/2<3pi/2`.
Every ratio therefore decreases, proving `f'<0` on the complete interval.

The literal threshold train gives

\[
\begin{aligned}
f(4/21)<1
&-e^{-289\pi/1764}
-e^{-625\pi/1764}\\
&-e^{-529\pi/441}
-e^{-4489\pi/1764}.
\end{aligned}
\tag{1.10}
\]

Using `pi<22/7`, the four positive exponents are smaller respectively
than

\[
 {3179\over6174},\qquad
 {6875\over6174},\qquad
 {11638\over3087},\qquad
 {49379\over6174}.
\tag{1.11}
\]

Direct substitution in (1.1), followed by positive-denominator cross
multiplication, gives the rational inequalities

\[
\begin{aligned}
U_{24}(3179/6174)&<{5000\over2987},\\
U_{24}(6875/6174)&<{125\over41},\\
U_{24}(11638/3087)&<{1000\over23},\\
U_{24}(49379/6174)&<{100000\over33}.
\end{aligned}
\tag{1.12}
\]

Equations (1.2), (1.11), and (1.12) imply

\[
e^{-289\pi/1764}>{2987\over5000},\qquad
e^{-625\pi/1764}>{41\over125},
\tag{1.13}
\]

\[
e^{-529\pi/441}>{23\over1000},\qquad
e^{-4489\pi/1764}>{33\over100000}.
\tag{1.14}
\]

Their sum is

\[
 {59740+32800+2300+33\over100000}
 ={94873\over100000}.
\]

Equation (1.10) proves

\[
 f(4/21)<1-{94873\over100000}
 ={5127\over100000}.
\]

Finally

\[
 {5127\over100000}={25635\over500000}
 <{25747\over500000}.
\]
\(\square\)

Lemma 1.1 gives the pair price

\[
 f(X)-f(Y)+g(Y)>L-V-\varepsilon
 \qquad(Y>4/21).
\tag{1.15}
\]

Indeed, if `X<4/21`, then `f(X)>L` and monotonicity gives
`f(Y)<f(4/21)<V`.  If `X>=4/21`, monotone decrease makes the compact
difference nonnegative; the absolute theta bound is stronger than
`L-V-epsilon`, since `L-V<0`.

## 2. A rational middle-train floor

For `x>0`, put

\[
 L_{24}(x)=\sum_{j=0}^{24}{x^j\over j!}<e^x.
\tag{2.1}
\]

### Lemma 2.1

\[
 \boxed{f(10/21)>{1\over250}.}
\tag{2.2}
\]

#### Proof

Using `pi>333/106`, the first four adverse exponents at `10/21` exceed

\[
 {40293\over186984},\qquad
 {320013\over186984},\qquad
 {225108\over46746},\qquad
 {1774557\over186984}.
\tag{2.3}
\]

Positive-series substitution in (2.1), followed by rational cross
multiplication, gives

\[
\begin{aligned}
L_{24}(40293/186984)&>{2000\over1613},\\
L_{24}(320013/186984)&>{1000\over181},\\
L_{24}(225108/46746)&>{5000\over41},\\
L_{24}(1774557/186984)&>10000.
\end{aligned}
\tag{2.4}
\]

Consequently

\[
e^{-121\pi/1764}<{1613\over2000},\qquad
e^{-961\pi/1764}<{181\over1000},
\tag{2.5}
\]

\[
e^{-676\pi/441}<{82\over10000},\qquad
e^{-5329\pi/1764}<{1\over10000}.
\tag{2.6}
\]

The remaining tail begins with `n=4`.  Its first exponent exceeds `15`,
and each successive exponent increases by more than `7`.  The elementary
bound `e>19/7` gives

\[
 e^{15}>2000000,
 \qquad e^7>1000.
\]

Therefore the complete residual tail is smaller than

\[
 {1/2000000\over1-1/1000}<{1\over1000000}.
\tag{2.7}
\]

The adverse upper ledger is now

\[
 {806500+181000+8200+100+1\over1000000}
 ={995801\over1000000}.
\tag{2.8}
\]

Hence

\[
 f(10/21)>{4199\over1000000}>{4000\over1000000}
 ={1\over250}.
\]
\(\square\)

Since `f` decreases on `[1/5,1/2]`, Lemma 2.1 and the pre-quarter floor
imply the uniform consequence

\[
 \boxed{f(t)>{1\over250}
 \qquad(0\le t\le10/21).}
\tag{2.9}
\]

## 3. Period-twenty-one geometry

For an honest period-twenty-one exact-first-carry table, define `X_i,Y_i`
as usual.  Then

\[
 u\le9,
 \qquad
 Y_i>{i\over21}.
\tag{3.1}
\]

Thus

\[
 Y_4>{4\over21},\qquad
 Y_5>{5\over21}>{1\over5},\qquad
 Y_i>{i\over21}>{1\over4}\quad(i\ge6).
\tag{3.2}
\]

For `u>=5`, price the first three pairs globally, pair four by Lemma 1.1,
pair five at one fifth, and every later pair at the quarter.  Exactly six
theta allowances can be adverse.  Before retaining middle trains,

\[
\boxed{
E(s)>(u+1)L-3G-V-U-(u-5)Q-6\varepsilon
+\sum_{r=u+2}^{20-u}f(s_r/A).}
\tag{3.3}
\]

At `u=5`, the ray numerator over `500000` is

\[
\begin{aligned}
6L-3G-V-U-6\varepsilon
&=132072-80925-25635-25250-150\\
&=112,
\end{aligned}
\tag{3.4}
\]

so

\[
 E(s)>{112\over500000}={7\over31250}>0.
\tag{3.5}
\]

Each additional quarter pair subtracts `568/500000`.

For `u=6,7,8`, the first middle residue is respectively `8,9,10`.
Prefix averaging gives

\[
 {s_{u+2}\over A}
 \le {u+2\over21}{P\over A}
 <{u+2\over21}\le{10\over21}.
\tag{3.6}
\]

Hence (2.9) supplies one middle-train credit greater than
`1/250=2000/500000`.  The resulting margins are

\[
\begin{array}{c|c}
u&\text{strict numerator over }500000\\ \hline
6&112-568+2000=1544\\
7&112-2(568)+2000=976\\
8&112-3(568)+2000=408.
\end{array}
\tag{3.7}
\]

All are positive.

The chambers `u=3,4` are also positive.  At `u=3`, the three global
pairs give `7023/500000`.  At `u=4`, three global pairs and the new
four-twenty-first pair give

\[
 {5L-3G-V-5\varepsilon}
 ={3375\over500000}>0.
\tag{3.8}
\]

## 4. Closure through eight rays and the residual ninth ray

### Theorem 4.1

Every honest exact-first-carry period-twenty-one cyclic Apéry clock with
`u<=8` satisfies

\[
 \boxed{\Phi(W)>0.}
\tag{4.1}
\]

#### Proof

If `H<=2`, then `u<=9` and

\[
360H+\tau\le720+10=730<860,
\]

so the prior reflected-depth theorem applies.  For `H>=3`, one has
`u>=3`.  Equations (3.5), (3.7), and (3.8) close every value
`3<=u<=8`.  Finally `Phi(W)>=E(s)`. \(\square\)

At `u=9`, the sole middle residue is `r=11`.  The independent ray ledger
in (3.3) has numerator

\[
 112-4(568)=-2160,
\]

so the exact surviving sufficient scalar is

\[
\boxed{
 f(s_{11}/A)+\mathcal C>{2160\over500000}
 ={27\over6250}.}
\tag{4.2}
\]

Here `mathcal C` denotes any improvement obtained by pricing the compact
pairs or theta block jointly rather than independently.  With
`mathcal C=0`, (4.2) is exactly the remaining middle-train gate.

Location alone cannot prove (4.2): midpoint splitting gives only
`s_11/A<=1/2`, while the certified half-shift value is smaller than
`1/40000`.  Thus the next proof must use overlap correlation, theta
spacing, or a stronger honesty relation tying `s_11` to the bad ray
pairs.  No negative clock is asserted.

## 5. Scope and frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| prefix minimum, ray identity, and depth theorem | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| terminal-suffix and prefix-average envelopes | `MATH_LEMMA_APERY_TERMINAL_SUFFIX_MAXIMUM_AND_QUARTER_CUTOFF_20260804.md` | `6ef133e15f8635db9a91fb837ef2df65fadedc6a52ff923b0b5895f215324639` |
| global, one-fifth, and quarter bounds | `MATH_THEOREM_APERY_PERIOD11_12_GLOBAL_QUARTER_LEDGER_COMPLETE_POSITIVITY_20260804.md` | `fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601` |
| one-mode critical-point classification | `MATH_THEOREM_COMPLEMENTARY_PAIR_TRAIN_AND_H4_INERT_SCALAR_REDUCTION_20260804.md` | `fc8b2dee92dd3bb9afab390c8507db51fec05c6ca4e9d46ac4948c7422d042a7` |
| compact endpoint bounds | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| theta sign and absolute bound | `MATH_LEMMA_THETA_HALF_INTERVAL_MONOTONICITY_AND_HALF_ROOT_SUMS_20260804.md` | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |
