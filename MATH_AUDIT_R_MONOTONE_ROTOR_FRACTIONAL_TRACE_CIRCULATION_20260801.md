# Independent audit of the monotone-rotor fractional trace circulation

Date: 2026-08-01

Audited promoted theorem:
`MATH_THEOREM_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md`,
SHA-256
`157f446c9b728b4d54b03202c3add6f32d806261c682c87bfd2c9ac7e7f8435e`.

Audited finite checker:
`scratch/audit_monotone_rotor_fractional_clock_20260801.cpp`, SHA-256
`a45647bc0d8756c9cba998a9364cebc6c5f000ad6fff25852f531dd747da57e6`.

## 0. Verdict

**PASS** for the exact promoted theorem and hash named above:

\[
 \mathcal M_{r,d}\subseteq \mathsf {ST}_{k,r,d}
 \qquad(1\le d\le r-1).
\]

Here `ST` must mean the symmetric, rank-only, fractional marked-trace
projection, equivalently the marked age-composition circulation quotient.
It does not include one-copy owners, occurrence-labelled common-cap rows,
Johnson owner chronology, connectedness, or integral target matching.

The promoted theorem incorporates every correction found in the candidate:

1. Theorem 1 now has the hypothesis `1<=d<=r-1`.  Without it, some displayed
   vertices `v_a` would be undefined and the short clock
   `(r-d,1,...,1)` need not have positive first coordinate.
2. The Ferrers corollary explicitly defines
   \(r=\lceil k/2\rceil\), \(W=\binom kr\), \(\Lambda\), and the minimal
   triangular depth `d`, assumes `k>=3`, and extends the column counts by
   \(b_s=0\) for every \(d<s<r\).
3. The theorem uses the precise literal notation `ST_(k,r,d)` and defines
   it as the symmetric rank-only fractional trace projection.
4. The final uniqueness statement is restricted to a **bijective**
   successor map on the entire core-free positive-composition set.  It does
   not classify arbitrary multivalued stationary flows or rotors with a
   permanent core.
5. The labelled transition wording distinguishes correctly between
   compatibility of a particular labelled pair, equation (1.5), and
   existence of some compatible pair between two types, equation (1.6).

The final conditioned-actuator caveat is also correct.  The theorem gives
an alternative unconditioned realization of the rank vector; it does not
prove that a circulation remains feasible after prescribed
donor/reservoir/actuator occurrence rows are imposed as lower bounds.

Every coefficient, index interval, nonnegativity claim, marginal,
stationary-flow assertion, and stated implication scope checks exactly.

## 1. Clean proof of the labelled biregular lift

Fix adjacent types

\[
 c=(c_0,\ldots,c_d),\qquad c'=(c'_0,\ldots,c'_d)
\]

with positive zeroth coordinates, total `r`, and

\[
                         c'_{i+1}\le c_i\quad(0\le i<d).       \tag{1.1}
\]

For a labelled source partition \(T=C_0\dot\cup\cdots\dot\cup C_d\), a
compatible target is obtained by independently choosing

\[
 C'_{i+1}\subseteq C_i,\qquad |C'_{i+1}|=c'_{i+1},\quad 0\le i<d,
\]

and putting all unchosen elements into `C'_0`.  The latter class has size

\[
 c_d+\sum_{i=0}^{d-1}(c_i-c'_{i+1})
 =r-\sum_{i=1}^d c'_i=c'_0.                           \tag{1.2}
\]

Thus the source degree is

\[
 d^+(c,c')=\prod_{i=0}^{d-1}{c_i\choose c'_{i+1}}.    \tag{1.3}
\]

Conversely, for a fixed labelled target, partition `C'_0` into old leftover
classes of sizes

\[
 c_0-c'_1,\ldots,c_{d-1}-c'_d,c_d.
\]

The target degree is therefore

\[
 d^-(c,c')={c'_0!\over c_d!\prod_{i=0}^{d-1}(c_i-c'_{i+1})!}. \tag{1.4}
\]

Both degrees are independent of the labelled partition.  Hence the
compatibility graph is biregular.  If a type arc carries mass `f(c,c')`,
put mass `f(c,c')/|E(c,c')|` on each labelled arc.  Each labelled source
then emits `f(c,c')/|P_c|`, and each labelled target receives
`f(c,c')/|P_c'|`.  Type conservation therefore becomes literal-state
conservation.  Since `c'_0>0`, the appended source letter is nonempty.

This verifies the part of the theorem that the finite checker cannot test.

## 2. The monotone polytope and all of its vertices

Put `q_0=0`.  For a nondecreasing vector

\[
 0\le q_1\le\cdots\le q_{r-1}\le1
\]

define

\[
 \alpha_\ell=q_{r-\ell}-q_{r-\ell-1},
                  \qquad 1\le\ell\le r-1.             \tag{2.1}
\]

Then

\[
 q=\sum_{\ell=1}^{r-1}\alpha_\ell v_\ell,
 \quad \sum_\ell\alpha_\ell=q_{r-1},
 \quad \sum_\ell\ell\alpha_\ell=\sum_{s=1}^{r-1}q_s. \tag{2.2}
\]

This proves both uniqueness and the equivalence with

\[
 \alpha\ge0,qquad \sum\alpha_\ell\le1,qquad
 \sum\ell\alpha_\ell\le d.                           \tag{2.3}
\]

A vertex has at most two positive coordinates.  The complete list for
`1<=d<=r-1` is

\[
 0,\quad e_a\ (1\le a\le d),\quad {d\over b}e_b\ (d<b\le r-1), \tag{2.4}
\]

and

\[
 {b-d\over b-a}e_a+{d-a\over b-a}e_b
       \quad(1\le a<d<b\le r-1).                      \tag{2.5}
\]

Mapping `e_l` to `v_l` gives exactly the candidate's displayed vertices.
All coefficients in (2.5) are nonnegative and sum to one.

## 3. Long-rotor coefficient audit

Fix `d<b<=r-1`.  A positive composition of `b+1` into `d+1` blocks is
equivalent to choosing `d` cuts among `b` internal cut positions.  There are

\[
                           {b\choose d}                \tag{3.1}
\]

such compositions.  A specified cut occurs in

\[
                           {b-1\choose d-1}             \tag{3.2}
\]

of them, so its exact marginal is

\[
                  {{b-1\choose d-1}\over {b\choose d}}={d\over b}. \tag{3.3}
\]

Adding a permanent core of size `r-b-1` translates the possible suffix
ranks to precisely

\[
                          r-b,r-b+1,\ldots,r-1.         \tag{3.4}
\]

The cyclic block rotation is a permutation of the positive compositions,
so the uniform type measure is stationary.  Its legality is termwise:
after rotation, target class `i+1` equals source mobile block `i` for every
`0<=i<d` (and at `i=0` the source also contains the nonnegative core).
Consequently its marked vector is exactly `(d/b)v_b`.

## 4. Mixed-rotor coefficient and interface audit

Let

\[
 D=d-a,\qquad L=b-a,\qquad R=r-a,\qquad 1\le a<d<b.    \tag{4.1}
\]

Then `1<=D<L<=R-1`.  The reduced rotor contains
`binom(L,D)` positive compositions and offers each of its `L` ranks with
probability

\[
                            {D\over L}={d-a\over b-a}. \tag{4.2}
\]

Appending `a` terminal singleton age classes adds the ranks

\[
                            r-a,\ldots,r-1             \tag{4.3}
\]

with probability one.  At the only new interface the required inequality
is

\[
             1\le x_D,                                \tag{4.4}
\]

where `x_D` is the last block of a positive reduced composition.  All later
inequalities are `1<=1`.  Thus the exact vector is

\[
 {b-d\over b-a}v_a+{d-a\over b-a}v_b,                \tag{4.5}
\]

because the coefficient of `v_b` is `D/L` and the last `a` ranks receive
the additional mass `1-D/L=(b-d)/(b-a)`.

## 5. Ferrers specialization

For `k>=3`, put

\[
 r=\lceil k/2\rceil,\quad W={k\choose r},\quad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},
\]

and let `d` be the least positive integer satisfying

\[
                  dW+{d+1\choose2}\ge\Lambda.         \tag{5.1}
\]

Since every `binom(k,s)<=W` for `s<r`, one has `1<=d<=r-1`.  Let

\[
                         h=(\Lambda-dW)_+.
\]

Fill the columns of
`{(i,s):1<=s<=i<=d}` from `s=1` upward, with at most the last used column
partial.  If `b_s` is the number of selected cells in column `s`, then

\[
 b_1\ge\cdots\ge b_d\ge0,\qquad \sum_{s=1}^d b_s=h.   \tag{5.2}
\]

Define `b_s=0` for `d<s<r` and

\[
                         q_s={{k\choose s}-b_s\over W}. \tag{5.3}
\]

Nonnegativity follows from `b_s<=d<=r-1<=k<=binom(k,s)` on used columns.
Also `q_s<=1`, since `binom(k,s)<=W`.  Finally

\[
 q_{s+1}-q_s=
 {{k\choose{s+1}}-{k\choose s}+b_s-b_{s+1}\over W}\ge0, \tag{5.4}
\]

where central binomial monotonicity is valid through rank `r-1`, and

\[
 \sum_{s=1}^{r-1}q_s={\Lambda-h\over W}\le d.         \tag{5.5}
\]

Thus `q` lies in the monotone polytope.  For a fixed rank-`s` target, the
rotor contribution is

\[
 { {k-s\choose r-s}\over {r\choose s}}q_s
 ={Wq_s\over {k\choose s}}
 =1-{b_s\over {k\choose s}},                         \tag{5.6}
\]

which is exactly complementary to the boundary mass.

## 6. Audit of the O3 checker and final scope

The checker independently tests, with exact 64-bit integer identities,

* `3<=r<=28`;
* `1<=d<=min(8,r-1)`;
* `d<b<=min(17,r-1)`;
* every long-rotor edge and every suffix marginal; and
* every mixed rotor with `1<=a<d`, including the appended-singleton
  interface and every suffix marginal.

Its expected identities are exactly (3.3) and (4.2); its index tests agree
with (3.4) and (4.3).  Its signed quantities are stored in `int64_t` and
are far below overflow on the audited range.  The source itself is sound.
No saved stdout/JSON transcript accompanies the source, so the checker is
supporting evidence rather than an independently authenticated execution
certificate.  The proof above supplies the all-parameter result.

Finally, on the core-free positive-composition set, let `sigma` be a
bijective legal successor.  Summing

\[
                    (\sigma a)_{i+1}\le a_i
\]

over every composition gives equality, because coordinate sums are equal
by symmetry and `sigma` is a permutation.  Hence equality holds termwise,
`(sigma a)_(i+1)=a_i`, and the zeroth coordinate is forced by the total.
Thus `sigma` is the cyclic rotation.  This last observation is valid, but
only in the bijective core-free scope stated in Verdict item 4.

The invariant fractional trace gate is therefore closed.  The surviving
gate is integral occurrence-labelled owner/target rotor fusion (including
the guarded common-cap and physical topology), not another fractional
rank-profile inequality.
