# Period twenty-two: nested far-ray anchors and complete positivity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It proves that every
honest exact-first-carry cyclic Apéry clock of period twenty-two has
strictly positive formal Bellman functional.  No computation or search is
used.  The proof combines rational anchors at `2/11`, `3/11`, and `2/7`
with the ordering of the early ray.  The current anchored ledger first
breaks at period twenty-three in the `u=5` chamber; that is a method
frontier, not a nonpositivity claim.

Put

\[
A={\sqrt\pi\over2},\qquad
f(x)=F_A(Ax),\qquad C=F_A(0),\qquad g(x)=\rho(Ax).
\tag{0.1}
\]

Use

\[
L={5503\over125000},\quad
G={1079\over20000},\quad
U={101\over2000},\quad
Q={1129\over25000},\quad
\varepsilon={1\over20000},
\tag{0.2}
\]

and the already-proved two-sevenths bound

\[
f(2/7)<V_7:={4083\over100000}.
\tag{0.3}
\]

## 1. Two new rational anchors

For `0<x<25`, define

\[
U_{24}(x)=\sum_{j=0}^{23}{x^j\over j!}
+{x^{24}\over24!\,(1-x/25)},
\tag{1.1}
\]

so `e^x<U_24(x)`.

### Lemma 1.1 (two-elevenths anchor)

\[
\boxed{
f'(x)<0\quad(2/11\le x\le1/2),
\qquad
f(2/11)<V_4:={513\over10000}.}
\tag{1.2}
\]

#### Proof

Put `h(t)=t exp(-pi t^2/4)`.  At `x=2/11`, the first two
positive/adverse derivative ratios are

\[
{13\over9}e^{-22\pi/121}<{83\over100},
\qquad
{8\over3}e^{-495\pi/484}<{11\over100}.
\tag{1.3}
\]

Beginning with `t=24/11`, every successive positive-term ratio is below
`1/30`.  These are direct positive-Taylor consequences of
`pi>333/106`.  Hence the complete ratio is below

\[
{83\over100}+{11/100\over1-1/30}
={2737\over2900}<1.
\tag{1.4}
\]

Thus `f'(2/11)<0`.  As in the earlier anchor proofs, every individual
positive/adverse ratio has negative logarithmic derivative on
`[2/11,1/2]`; for the first ratio use `2/(1-x^2)<=8/3<pi`, and for all
later ratios use the bound `5/2<3pi/2`.  Therefore `f'<0` throughout.

For the endpoint value, the literal train gives

\[
\begin{aligned}
f(2/11)<1
&-e^{-81\pi/484}-e^{-169\pi/484}\\
&-e^{-144\pi/121}-e^{-1225\pi/484}.
\end{aligned}
\tag{1.5}
\]

Using `pi<22/7` and `U_24`, direct rational substitution gives

\[
e^{-81\pi/484}>{11819\over20000},\qquad
e^{-169\pi/484}>{3337\over10000},
\tag{1.6}
\]

\[
e^{-144\pi/121}>{237\over10000},\qquad
e^{-1225\pi/484}>{7\over20000}.
\tag{1.7}
\]

Their numerator sum over `100000` is

\[
59095+33370+2370+35=94870.
\]

Therefore

\[
f(2/11)<{5130\over100000}={513\over10000}.
\]
\(\square\)

### Lemma 1.2 (three-elevenths anchor)

\[
\boxed{f(3/11)<V_6:={107\over2500}.}
\tag{1.8}
\]

#### Proof

The literal train and four retained adverse terms give

\[
\begin{aligned}
f(3/11)<1
&-e^{-16\pi/121}-e^{-49\pi/121}\\
&-e^{-625\pi/484}-e^{-324\pi/121}.
\end{aligned}
\tag{1.9}
\]

Using `pi<22/7` and (1.1), rational cross multiplication gives

\[
e^{-16\pi/121}>{3299\over5000},\qquad
e^{-49\pi/121}>{7\over25},
\tag{1.10}
\]

\[
e^{-625\pi/484}>{43\over2500},\qquad
e^{-324\pi/121}>{1\over5000}.
\tag{1.11}
\]

Their sum is

\[
{6598+2800+172+2\over10000}
={9572\over10000}.
\]

Thus

\[
f(3/11)<1-{9572\over10000}
={428\over10000}={107\over2500}.
\]
\(\square\)

The useful anchor credits are

\[
L-V_6={44024-42800\over1000000}
={1224\over1000000},
\tag{1.12}
\]

and

\[
L-V_7={44024-40830\over1000000}
={3194\over1000000}.
\tag{1.13}
\]

## 2. Period-twenty-two base ledger

For an honest period-twenty-two table,

\[
u\le10,
\qquad
Y_i>{i\over22}.
\tag{2.1}
\]

In particular,

\[
Y_4>{2\over11},\qquad
Y_5>{5\over22}>{1\over5},
\tag{2.2}
\]

\[
Y_6>{3\over11}>{1\over4},qquad
Y_7>{7\over22}>{2\over7}.
\tag{2.3}
\]

Price the first three pairs globally, pair four at `2/11`, and pair five
at one fifth.  Six theta allowances remain.  Through pair five the exact
rational lower margin is

\[
\begin{aligned}
B_{22}
&:=6L-3G-V_4-U-6\varepsilon\\
&={132072-80925-25650-25250-150\over500000}\\
&={97\over500000}>0.
\end{aligned}
\tag{2.4}
\]

This closes every chamber with `u=5`, and the earlier `u=3,4` ledgers are
strictly stronger.

## 3. Nested ordered-ray dichotomy

It remains to append pairs six through `u`, where `u<=10`.

If `X_6>=1/4`, every pair from six onward is strictly positive by ordered
early rays, quarter-band decrease, and positive theta.  Thus `B_22`
closes the table.

Suppose `X_6<1/4`.  Since `Y_6>3/11` and `f` decreases from one fifth,
pair six is larger than

\[
L-V_6={1224\over1000000}.
\tag{3.1}
\]

If `X_7>=1/4`, every later pair is positive and again the sum is positive.
Finally suppose `X_7<1/4`.  The two-sevenths bound makes pair seven larger
than

\[
L-V_7={3194\over1000000}.
\tag{3.2}
\]

Every remaining pair has the generic quarter price

\[
L-Q=-{1136\over1000000}.
\tag{3.3}
\]

The worst case is `u=10`, with three generic pairs after pair seven.
Using `B_22=194/1000000`, the total is

\[
\begin{aligned}
E(s)&>{194+1224+3194-3(1136)\over1000000}\\
&={1204\over1000000}
={301\over250000}>0.
\end{aligned}
\tag{3.4}
\]

No middle train is needed.

## 4. Complete closure and next scalar frontier

### Theorem 4.1

Every honest exact-first-carry period-twenty-two cyclic Apéry clock
satisfies

\[
\boxed{\Phi(W)>0.}
\tag{4.1}
\]

#### Proof

If `H<=2`, then `u<=10` and

\[
360H+\tau\le720+11=731<860,
\]

so the reflected-depth theorem applies.  If `H>=3`, the base ledger and
the nested dichotomy in Sections 2--3 exhaust every `3<=u<=10`.
Finally `Phi(W)>=E(s)`. \(\square\)

At period twenty-three, `u<=10`, but

\[
Y_4>{4\over23},\qquad {4\over23}<{2\over11}.
\]

The current prices therefore revert to four global pairs in the first new
`u=5` row, giving

\[
6L-4G-U-6\varepsilon
=-{307\over125000}.
\tag{4.2}
\]

Thus `(h,u)=(23,5)` is the first chamber not closed by the present anchor
set.  A sufficient next scalar is an anchor bound

\[
\boxed{f(4/23)<{25747\over500000},}
\tag{4.3}
\]

or an equal middle/overlap credit.  No period-twenty-three nonpositivity is
asserted.

## 5. Scope and frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| complete period-twenty-one closure and `2/7` anchor | `MATH_THEOREM_APERY_PERIOD21_TWO_SEVENTHS_FAR_RAY_COMPLETE_POSITIVITY_20260804.md` | `20b87ed61065d927c25f8721586cebc42df6c15d9daf56844776ccb4e94e2bb8` |
| prefix minimum, ray identity, and depth theorem | `MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md` | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| compact monotonicity and standard prices | `MATH_THEOREM_APERY_PERIOD11_12_GLOBAL_QUARTER_LEDGER_COMPLETE_POSITIVITY_20260804.md` | `fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601` |
| compact lower floor | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
