# Independent audit: period-twenty-one two-sevenths far-ray closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_APERY_PERIOD21_TWO_SEVENTHS_FAR_RAY_COMPLETE_POSITIVITY_20260804.md`  
**Audited theorem SHA-256:**
`20b87ed61065d927c25f8721586cebc42df6c15d9daf56844776ccb4e94e2bb8`  
**Verdict:** **GO.**  The `2/7` rational certificate, ordered `X_6`
dichotomy, theta multiplicities, corrected middle-floor dependency, and
the final `1/100000` margin all replay exactly.  No computation or search
is used.

## 1. Byte and dependency binding

The audited theorem rehashes to the displayed SHA.  Its four frozen
dependencies also rehash exactly:

| role | SHA-256 |
|---|---|
| period-21 anchor/base and corrected middle floor | `4f31625b65431320566e5372e027af3863366aa9482844cf98e220d723fecf45` |
| prefix/ray reduction | `28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e` |
| global and quarter prices | `fb9139813f93d8e5450b8ab3cee0238c289cd573222d0d05fd6174040fdbe601` |
| theta sign theorem | `f974aeda114df4c933a396c06de51596bccd2fea18066412d45f7a18df62a0e3` |

The current middle-floor dependency is the corrected byte lineage: at
`10/21` its leading exponent is `121pi/1764`, not a superseded exponent.
No earlier middle-floor draft is used by the complete theorem.

## 2. The `U_24` majorant

The theorem defines

\[
 U_{24}(x)=\sum_{j=0}^{23}{x^j\over j!}
 +{x^{24}\over24!}{1\over1-x/25}.
\]

For `0<x<25`, the ratio of the term of degree `j+1` to that of degree
`j` is `x/(j+1)<=x/25` from degree 24 onward.  Therefore the last term is
a valid geometric majorant for the complete tail beginning at degree 24,
and it is strict after the first tail term.  Thus `e^x<U_24(x)` is
correct with every denominator positive.

## 3. Independent `2/7` certificate replay

At `x=2/7`, the literal threshold train has adverse exponents

\[
 {25\pi\over196},\quad
 {81\pi\over196},\quad
 {64\pi\over49},\quad
 {529\pi\over196},
\]

followed only by further negative terms.  Replacing `pi` by `22/7`
gives exactly

\[
 {275\over686},\quad
 {891\over686},\quad
 {1408\over343},\quad
 {5819\over686}.
\]

Substitution in the rational `U_24` majorant and clearing the positive
denominators independently gives

\[
\begin{aligned}
 U_{24}(275/686)&<25000/16743,\\
 U_{24}(891/686)&<1250/341,\\
 U_{24}(1408/343)&<20000/329,\\
 U_{24}(5819/686)&<5000.
\end{aligned}
\]

The directions are correct: an upper bound on `e^x` inverts to a strict
lower bound on `e^{-x}`.  Over denominator `100000`, the resulting four
Gaussian numerators are

\[
 4(16743)=66972,
 \qquad80(341)=27280,
 \qquad5(329)=1645,
 \qquad20.
\]

Their sum is

\[
 66972+27280+1645+20=95917.
\]

Hence

\[
 f(2/7)<1-{95917\over100000}
 ={4083\over100000}=V_6.
\]

The improvement over the generic quarter price is exactly

\[
 {1129\over25000}-{4083\over100000}
 ={4516-4083\over100000}
 ={433\over100000}.
\]

The residual deficit is

\[
 {27\over6250}={432\over100000},
\]

so the certificate has the advertised exact surplus `1/100000`.

## 4. Corrected middle-floor lineage

The bound used for the already-closed `u<=8` chambers comes from the
current dependency SHA `4f31625...`.  At `10/21`, its first four exact
adverse exponents are

\[
 {121\pi\over1764},\quad
 {961\pi\over1764},\quad
 {676\pi\over441},\quad
 {5329\pi\over1764}.
\]

Multiplication by the lower enclosure `333/106` gives exactly

\[
 {40293\over186984},\quad
 {320013\over186984},\quad
 {225108\over46746},\quad
 {1774557\over186984}.
\]

The certified upper ledger for the corresponding exponentials and the
remaining tail is

\[
 {1613\over2000}+{181\over1000}+{82\over10000}
 +{1\over10000}+{1\over1000000}
 ={995801\over1000000}.
\]

Thus

\[
 f(10/21)>{4199\over1000000}>{1\over250}.
\]

Together with the pre-quarter floor and decrease from `1/5`, this gives
the claimed uniform middle credit through `10/21`.  The period-21 base
ledger and its `112/500000` margin therefore rest on the corrected
middle-floor bytes.

## 5. Ordered `X_6` dichotomy and theta audit

The prefix/ray dependency supplies the complete geometry

\[
 0<X_6<X_7<X_8<X_9<1/2,
 \qquad
 X_i\le Y_i<1/2,
 \qquad
 Y_i>{i\over21}.
\]

The shorter display (0.4) in the audited theorem omits `Y_i<1/2`, but the
proof explicitly invokes it and the frozen dependency supplies it.  This
is not a missing premise.

### Case `X_6<1/4`

Here `f(X_6)>L`.  Since `Y_6>2/7>1/5` and `f` is strictly decreasing from
`1/5`,

\[
 f(Y_6)<f(2/7)<V_6.
\]

Also `Y_6>1/4`, so the theta term `g(Y_6)` is strictly positive.  Pair six
therefore has the strict price `L-V_6`.

For `i=7,8,9`, one has `Y_i>i/21>1/4`.  If `X_i<1/4`, the pair has price
strictly above `L-Q`; if `X_i>=1/4`, quarter-band decrease gives
`f(X_i)>=f(Y_i)` and positive theta makes the pair strictly positive.
Since `L-Q<0`, both alternatives imply the claimed generic `L-Q` lower
price.

### Case `X_6>=1/4`

Strict ordering gives `X_i>=1/4` for all `i>=6`.  Both endpoints then lie
in the decreasing quarter-to-half band, so `f(X_i)>=f(Y_i)`, while each
theta term is strictly positive.  All four far pairs are strictly
positive.

Thus the theorem never charges the positive `L-V_6` anchor price in the
post-quarter case.  This validates the ordering and case split requested
for special scrutiny.

The base `112/500000` is the complete through-pair-five ledger from the
frozen reduction; its six potentially adverse theta allowances have
already been debited there.  Every far theta term is positive by
`Y_i>1/4`.  Hence there is neither a seventh hidden adverse theta charge
nor a double-counted positive theta credit.

## 6. Final margin and middle train

In the anchor branch, over denominator one million,

\[
 {112\over500000}={224\over1000000},
\]

\[
 L-V_6={44024-40830\over1000000}
 ={3194\over1000000},
\]

and

\[
 3(L-Q)=3{44024-45160\over1000000}
 =-{3408\over1000000}.
\]

Therefore

\[
 E(s)>{224+3194-3408\over1000000}
 ={10\over1000000}={1\over100000}>0.
\]

The remaining middle train may be discarded in this branch.  In the
post-quarter branch, the base margin is already positive and all four far
pairs are positive; the sole middle train is positive on the closed half
band, including the half-shift endpoint.  Finally `Phi(W)>=E(s)`, so both
branches are strictly positive.

## 7. Scope verdict

The theorem closes exactly the honest exact-first-carry formal period-21
branch.  It does not claim threshold-overshoot, later-first-crossing,
finite-shoulder, or arbitrary-clock closure.

Within that stated scope, every dependency, rational direction, ordered
case, theta count, and the exact `1/100000` margin passes.  The independent
verdict is therefore

\[
                         \boxed{\textbf{GO}.}
\]
