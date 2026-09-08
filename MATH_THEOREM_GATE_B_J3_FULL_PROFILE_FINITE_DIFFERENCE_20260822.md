# Gate B: an exact finite difference certifies the full `j=3` local profile

**Date:** 2026-08-22

**Status.**  This note closes the previously open fixed-`j=3` conditioning
problem for the sixteen four-vertex zero-avoidance atoms.  The two large
puncture rows need not be evaluated separately: all nonrational factorial
tails cancel in their difference.  If `A_(r,3)` is the full `(2r+1)`-by-two
shore matrix, normalized by `D_M(r-4)(r+1)`, then, for every `r>=9`,

\[
                 \boxed{\sigma_{\min}(A_{r,3})
                         \ge {1\over1000r^4}.}               \tag{0.1}
\]

The proof is exact.  It gives a closed formula for the difference of the
rows at `t=r+1,r+2`, pairs that difference with the central row
`t=ell=r+3`, and proves that the resulting determinant is at least
`2/(3r^8)`.

This is a fixed-depth local theorem.  It neither proves a bound uniform in
`2<=j<=r-2` nor transfers the local profile to the full exposure.  The known
remote dressing is only an absolute `O(D_M/r^2)` estimate, two powers larger
than the local singular scale certified here.

## 1. The local profile and its exact coefficient formula

Put

\[
 b=2r+1,\qquad k=r-2,\qquad \ell=r+3,
 \qquad D_M=2r\,r!(r+1)!,\qquad A_3=(r-4)(r+1).     \tag{1.1}
\]

After multiplication of boundary cuts by `-2 modulo b`, the boundary graph
is the punctured Cayley graph with steps `+/-1,+/-3`, and the two event
roots are `0,5`.  The sixteen four-vertex supports are

\[
\begin{array}{rrrr}
(-3,0,2,5),&(-3,0,4,5),&(-3,0,5,6),&(-3,0,5,8),\\
(-1,0,2,5),&(-1,0,4,5),&(-1,0,5,6),&(-1,0,5,8),\\
(0,1,2,5),&(0,1,4,5),&(0,1,5,6),&(0,1,5,8),\\
(0,2,3,5),&(0,3,4,5),&(0,3,5,6),&(0,3,5,8).
\end{array}                                                   \tag{1.2}
\]

An induced matching contributes its two-blocker codegree.  An induced
three-edge path contributes its endpoint-matching codegree minus its
three-blocker codegree.  Terms using either omitted target are deleted.
Let `L_(s,3)(t)`, for `s in {r,r-1}`, be the resulting signed boundary
profile at event start `t`.

For completeness, here is the finite factorial calculation used below.
Fix a labelled blocker tuple `J=(T_1,...,T_m)`, where `m` is two or three.
Let `C_eta`, `eta in {0,1}^m`, be its Boolean cells and let
`c_eta=|C_eta|`.  For an admissible positional tuple consisting of a
rank-`s` root interval and blocker intervals of the ranks in `J`, let
`u_eta` be the root count in the corresponding positional cell.  Write
`N_(s,J)(u)` for the number of retained positional tuples with this data.

For a label root `S`, put

\[
\begin{split}
 h_t(S)={}&(\mathbf1_{t\in S}-\mathbf1_{t-1\in S})
 (\mathbf1_{t+k-1\in S}-\mathbf1_{t+k\in S}),\\
 a_t(S)={}&|S\cap(I_k(t)-\{t,t+k-1\})|,\\
 c_t(S)={}&|S\cap(I_k(t)^c-\{t-1,t+k\})|.
                                                               \tag{1.3}
\end{split}
\]

After the two boundary pairs have been fixed, the remaining distinguished
pair has signed injection numerator

\[
                 \psi_t(S)=(r+1)a_t(S)-(r-4)c_t(S).           \tag{1.4}
\]

Define the finite cell sum

\[
 \mathcal H^{(3)}_{J,t}(u)=
 \sum_{\substack{S:\ |S\cap C_\eta|=u_\eta\ \forall\eta}}
                         h_t(S)\psi_t(S).
\]

Cellwise bijection counting gives the exact normalized contribution

\[
 \boxed{
 {\Omega_{s,J,t}\over A_3}={1\over A_3}
 \sum_uN_{s,J}(u)\mathcal H^{(3)}_{J,t}(u)
       \prod_\eta u_\eta!\,(c_\eta-u_\eta)! .}              \tag{1.5}
\]

Indeed, after the positional intervals and the label root are fixed, a
compatible word is an independent bijection in every root-refined Boolean
cell, giving the factorial product.  Conversely every compatible retained
word has a unique positional tuple and label root.  Formula (1.4) is the
two possible placements of the final distinguished pair: inside first gives
`(r+1)a_t(S)`, while outside first gives `-(r-4)c_t(S)`.  Thus (1.5) is an
identity, not a sampling or interpolation rule.

## 2. Exact cancellation of the two far rows

For a support `V` in (1.2), let `F_t(V)` be its two-shore contribution,
divided by `D_MA_3`.  In the comparison `t=r+1` against `t=r+2`, twelve
supports are fixed:

\[
\begin{split}
\mathcal S_0=\{&(-3,0,2,5),(-3,0,4,5),(-3,0,5,6),(-3,0,5,8),\\
&(-1,0,2,5),(-1,0,4,5),(-1,0,5,6),(-1,0,5,8),\\
&(0,1,5,6),(0,1,5,8),(0,2,3,5),(0,3,5,8)\}.
                                                               \tag{2.1}
\end{split}
\]

Formula (1.5), after a permutation of Boolean cells, gives

\[
 F_{r+1}(V)=F_{r+2}(V)\quad(V\in\mathcal S_0),               \tag{2.2}
\]

and reflection `x -> 5-x` gives the two crossed identities

\[
\begin{split}
 F_{r+1}(0,1,2,5)&=F_{r+2}(0,3,4,5),\\
 F_{r+1}(0,3,4,5)&=F_{r+2}(0,1,2,5).                         \tag{2.3}
\end{split}
\]

Here is a direct verification of the cell permutation assertion.  Increasing
`t` by one translates every label interval, the four boundary marks, and
the inside pool by one.  For every support in `S_0`, its retained blocker
tuple translates with them and no blocker crosses the omitted start.
Consequently its blocker ranks, Boolean-cell sizes, marked cells, inside
cell sizes, and positional multiplicities `N_(s,J)(u)` in (1.5) agree.
For the two supports in (2.3), reflection fixes the event roots as a set,
interchanges the two boundary pairs, preserves their product, and gives the
same five pieces of data.  This proves (2.2)--(2.3) without evaluating the
common contributions.

Only

\[
                       U=(0,1,4,5),\qquad V=(0,3,5,6)        \tag{2.4}
\]

remain.  If `(q,a)` denotes the cyclic interval of rank `q` and start `a`,
their surviving inclusion--exclusion terms are

\[
\begin{array}{c|c|c}
 &U&V\\ \hline
t=r+1&\{(r,r-1),(r,r+1)\}&
 \{(r,b-2),(r-1,r+1)\}-
 \{(r,b-2),(r-1,r+1),(r-1,b-1)\}\\
t=r+2&\{(r,r),(r,r+2)\}-
 \{(r,r),(r,r+2),(r-1,1)\}&
 \{(r,b-1),(r-1,r+2)\}.
\end{array}                                                   \tag{2.5}
\]

Substitution of these four finite rows in (1.5), followed only by cancelling
factorials, gives

\[
\begin{array}{c|c|c}
&F_t(U)_r&F_t(U)_{r-1}\\ \hline
t=r+1&{2(r-1)\over3r^3(r+1)^2}&
{2(2r^3-3r^2-6r+4)\over
r^3(r-2)(r-1)(r+1)^2}\\[3pt]
t=r+2&{1\over3r^3(r+1)^2}&
{2\over r^3(r-1)(r+1)}
\end{array}                                                   \tag{2.6}
\]

and

\[
\begin{array}{c|c|c}
&F_t(V)_r&F_t(V)_{r-1}\\ \hline
t=r+1&{1\over2r^3(r+1)^2}&
{3(r-3)\over2r^2(r-2)(r-1)(r+1)^2}\\[3pt]
t=r+2&{2(r-1)\over r^3(r+1)^2}&
{6(r-3)\over r^2(r-2)(r+1)^2}.
\end{array}                                                   \tag{2.7}
\]

Equations (2.2)--(2.7) prove that all factorial-ratio tails cancel.  With

\[
 \Delta_r={L_{\bullet,3}(r+2)-L_{\bullet,3}(r+1)\over D_MA_3}
          =(\delta_r,\varepsilon_r),                         \tag{2.8}
\]

direct subtraction gives the exact formulas

\[
 \boxed{\delta_r={8r-9\over6r^3(r+1)^2},\qquad
 \varepsilon_r={4r^3-35r^2+65r-24\over
 2r^3(r-2)(r-1)(r+1)^2}.}                                  \tag{2.9}
\]

## 3. A positive rational determinant

The normalized central row at `t=ell` is `(c_r,d_r)`, where the same finite
formula (1.5) gives

\[
 c_r=-{4r^5-173r^4+820r^3-1385r^2+1084r-260
 \over6r^3(r-2)^2(r-1)^2(r+1)^2},                           \tag{3.1}
\]

\[
 d_r={155r^5-1233r^4+3401r^3-3813r^2+1982r-384
 \over2r^3(r-3)(r-2)^2(r-1)^2(r+1)^2}.                     \tag{3.2}
\]

Let

\[
                    B_r=\begin{pmatrix}
                    \delta_r&\varepsilon_r\\c_r&d_r
                    \end{pmatrix}.                          \tag{3.3}
\]

Exact simplification yields

\[
 \boxed{\det B_r={P(r)\over
 3r^6(r-3)(r-2)^3(r-1)^3(r+1)^4},}                          \tag{3.4}
\]

where

\[
\begin{split}
P(r)={}&4r^9+90r^8-722r^7+49r^6+12115r^5-42338r^4\\
      &+66300r^3-53696r^2+20700r-2952.                      \tag{3.5}
\end{split}
\]

There is no numerical sign inference in (3.4).  If `x=r-6`, the coefficients
of `P(r)-4r^9`, from degree eight to zero, are

\[
 (90,3598,60445,556687,3054052,10064388,18789064,
   16502556,3182976),                                       \tag{3.6}
\]

so `P(r)>=4r^9` for every `r>=6`.  Also `r+1<=(7/6)r`, whence the denominator
in (3.4) is at most `(2401/432)r^17`.  Therefore

\[
 \boxed{\det B_r\ge {1728\over2401r^8}>{2\over3r^8}.}       \tag{3.7}
\]

## 4. The full-profile singular bound

For an explicit norm bound, coefficientwise estimates in (2.9), (3.1), and
(3.2), using

\[
 r-3\ge r/2,\quad r-2\ge2r/3,\quad r-1\ge5r/6,
 \quad r+1\ge r,                                           \tag{4.1}
\]

give, for `r>=6`,

\[
 |\delta_r|\le {4\over3r^4},\qquad
 |\varepsilon_r|\le {11\over r^4},\qquad
 |c_r|\le {35\over r^4},\qquad
 |d_r|\le {257\over r^4}.                                 \tag{4.2}
\]

For example, the absolute coefficient sums in the numerators of (3.1) and
(3.2) are at most `63r^5` and `475r^5`; their denominators are at least
`(50/27)r^9` and `(25/81)r^10`.  Thus

\[
                         \|B_r\|_F\le {300\over r^4}.       \tag{4.3}
\]

The product of the two singular values is `det B_r`, so (3.7)--(4.3) imply

\[
                         \sigma_{\min}(B_r)
                         \ge {1\over450r^4}.                 \tag{4.4}
\]

Let `T` take the difference of rows `r+2,r+1` and retain row `ell` from the
full profile.  These three indices are distinct, and hence `||T||=sqrt(2)`.
Since `B_r=T A_(r,3)`,

\[
 \sigma_{\min}(A_{r,3})\ge {\sigma_{\min}(B_r)\over\sqrt2}
                         >{1\over1000r^4},                   \tag{4.5}
\]

which proves (0.1).  The leading matrix is

\[
 r^4B_r\longrightarrow
 \begin{pmatrix}4/3&2\\-2/3&0\end{pmatrix},               \tag{4.6}
\]

so this particular two-functional certificate has the sharper asymptotic

\[
 \sigma_{\min}(B_r)=
 {\sqrt{28-8\sqrt{10}}\over3r^4}(1+O(r^{-1})).              \tag{4.7}
\]

## 5. Scope

The theorem proves a polynomial two-shore inverse for the complete sixteen-
atom local bank at the fixed level `j=3`.  In particular, the previously
observed `Theta(r^-4)` full-profile improvement no longer depends on finite
data or a factorial-tail asymptotic.

It does not yet prove the Gate-B zero-avoidance scalar.  Three separate
issues remain:

1. the analogous conditioning must be controlled uniformly over all
   harmonic depths, including `j=2` and growing `j`;
2. the remote blocker dressing must be estimated in the same row-difference
   geometry, or relatively to the local columns, rather than by its present
   absolute `O(D_M/r^2)` bound;
3. after that scalar step, the simultaneous multidepth inverse and stopped
   stability still have to be coinstantiated.

## 6. Authentication

The exact checker is

`scratch/verify_gate_b_j3_full_profile_finite_difference_20260822.py`.

Its SHA-256 digest is

`eadd91a5a77abcd73dda8ab19934c12f971628b21bcfecf60c72c31e2123d6d7`.

It authenticates the underlying Venn/Hahn evaluator chain, checks the
twelve fixed atoms, the reflected pair, and all four exceptional formulas,
replays (2.9) against the full local rows, and verifies the determinant and
shifted-coefficient positivity.  Its finite replay is confirmation of the
displayed exact calculation, not a premise of the proof.
