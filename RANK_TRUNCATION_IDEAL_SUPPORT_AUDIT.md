# Audit: rank truncation, ideal support, and run--zeta constraints

## Verdict

The principal theorems are valid for a zero-free universal word.  They add
sound all-dimensional entry-rank and support-run restrictions, but they do not
construct a new word or improve the numerical lower bound `B(k)` by
themselves.

## 1. Rank truncation

For

\[
b_s(k)=\binom ks+\tau(k,s),
\]

where `tau(k,s)` is the rank-count slack at rank `s`, every zero-free universal
word `A` satisfies

\[
p_s(A):=\#\{i:|A_i|\le s\}\ge b_s(k).
\]

Proof: delete every entry of rank greater than `s`.  A witness for a target of
rank at most `s` contains only nonempty submasks of that target, so it survives
the compression.  The rank-count proof at rank `s` uses no targets above rank
`s` and applies unchanged.

Consequently, if `n=B(k)=b_r(k)`, every entry has rank at most `r`, and

\[
\#\{i:|A_i|>s\}\le B(k)-b_s(k).
\]

For `k=11,n=465`, this gives the especially useful exact cuts

\[
|A_i|\le6\quad(1\le i\le465),
\qquad
\#\{i:|A_i|=6\}\le1.
\]

The generic form is now encoded in `exact_or_sat.cpp` using exact per-entry
cardinality thresholds and aggregate tail bounds.  The modified encoding was
compiled and SAT/decode-regression-tested on the certified optimum lengths
`(k,n)=(3,4),(4,7),(5,12)`.

For odd `k=2m+1`, if the sharp length is the upper-middle rank-count value,
then at most one entry has rank `m+1`.  The relation between the two central
slacks is `d in {t,t+1}`.  When `t=0`, the lower inequality is trivial rather
than an invocation of the failed value `t-1`.

## 2. Ideal-support inequality

Let `F` be a punctured down-set of masks of ranks below a chosen rank `r`, and
let `P_F={i:A_i in F}` have run lengths `g_1,...,g_rho`.  If
`n=binom(k,r)+d`, then

\[
|F|\le\sum_j f_d(g_j)\le f_d(|P_F|),
\]

where

\[
f_d(g)=\sum_{ell=1}^d(g-ell+1)_+.
\]

Also `|P_F|>=w(F)`.  Both statements follow by assigning short witnesses to
physical intervals inside the support runs; an antichain supplies distinct
right endpoints.

The inverse bound

\[
|P_F|\ge\max\{w(F),\Phi_d(|F|)\}
\]

and the run penalty

\[
|F|\le d|P_F|-(d-1)\rho
\]

are correct.  The qualitative few-run conclusion needs `d>1`.

This does **not** subsume the full dimension-restriction or earlier local
density theorems.  For example, with `k=100,r=50,d=6`, a punctured five-cube
has `w(F)=10` and `Phi_6(31)=8`, so this bound gives only 10 positions, whereas
the exact five-bit restriction requires 12.  It should be described as a
compatible weaker support bound, not as containing every earlier theorem.

## 3. Literal central entries

If equality holds at rank `r`, set

\[
sigma=d\binom kr+\binom{d+1}{2}-\sum_{j<r}\binom kj.
\]

For `d>=1,r>=2`, the number `h` of literal rank-`r` entries obeys

\[
h\le\min\left\{B(k)-b_{r-1}(k),\left\lfloor\frac{sigma}{d}\right\rfloor\right\}.
\]

The apparently missing condition `n-h>=d` follows from the minimality of `d`:
otherwise the lower ideal would fit into at most `binom(d,2)` short cells,
contradicting the failure of slack `d-1`.

## 4. Exact run--zeta system

After selecting one short witness for every lower mask, let the remaining
`sigma` short intervals have OR multiplicities `c_T`.  For
`P_Q={i:A_i subseteq Q}`,

\[
R_d(P_Q)=\sum_{s<r}\binom{|Q|}{s}+\sum_{T\subseteq Q}c_T,
\qquad
P_Q\cap P_R=P_{Q\cap R}.
\]

Möbius inversion gives nonnegative integral `c_T`.  This is exact and useful,
but is essentially the existing hole-spectrum theorem expressed through
physical support runs.

## 5. Window moments

The total OR-rank sequence by window length is discretely concave, and every
coordinate-avoidance moment is discretely convex.  The zero-run hinge proof is
valid for positive lengths.  The boundary at length zero needs a separate
one-line check: if a binary word has `z` zeros in `rho` zero-runs, then
`z+rho<=n+1`; dually the number of length-two windows containing a fixed bit is
at most twice its number of occurrences.

With that repair, the displayed rank-moment and avoidance-moment inequalities
are correct.  They have been numerically checked at maximizing ranks through
`k=100`, but they do not contradict the conjectured equality.

## Bottom line

The rank-tail constraints are the most immediately valuable part because they
are lossless SAT cuts for the unrestricted problem.  The support-run and
run--zeta systems sharpen the structural ledger, but no new exact value or
all-dimensional construction follows yet.  It is too strong to conclude that
*no possible* scalar inequality can work; only the scalar tests audited here
have been shown insufficient.

