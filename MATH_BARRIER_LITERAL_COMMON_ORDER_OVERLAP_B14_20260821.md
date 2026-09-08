# Literal common-order overlap has an unavoidable `b^(1/4)` barrier

**Status (2026-08-21).** Every assertion below is proved.  Consider the
literal common-order criterion in
`MATH_THEOREM_CLUSTERED_COMPLEMENTARY_PAYLOAD_ENDPOINT_COVERAGE_20260821.md`.
No choice of tight-cycle factors, orientations, or coherent conjugations can
make its weighted incompatibility `o(W_b)` through a DCC-scale band.  The
obstruction is already forced by the different cardinalities of neighboring
factor banks.

More precisely, if `q/sqrt(b) -> c>0`, then one offset alone has actual
incompatibility at least

\[
 \left(e^{-c^2}-\operatorname{erfc}(c)+o(1)\right)W_b.       \tag{0.1}
\]

If `1 << Q << sqrt(b)`, the actual incompatibility summed over
`1<=q<=Q` is at least

\[
 \left({1+o(1)\over\sqrt\pi}\right)
 {Q^2\over\sqrt b}W_b.                                      \tag{0.2}
\]

Thus the cardinality lower bound can be `o(W_b)` only in the range
`Q=o(b^(1/4))`; even hypothetical maximally nested banks fail at and above
the `b^(1/4)` scale.  This does **not** obstruct a more general
interval-coordinate coupling between nonidentical orders, nor a transport
which uses the one-sided endpoint surplus.  It proves that one of those
stronger mechanisms is necessary away from the complementary diagonal.

## 1. Setup and the cardinality bound

Let `b` tend through odd primes, put

\[
 W_b={2b\choose b},\qquad C_t={b\choose t},\qquad
 f_t={C_t\over b}.                                           \tag{1.1}
\]

Fix `q>=1`.  For every `s` for which factor banks at ranks `s` and `s-q`
are used, let

\[
 K_{q,s}=|F_s\cap F_{s-q}|                                  \tag{1.2}
\]

after arbitrary allowed choices of orientations and conjugations.  Since an
intersection cannot exceed its smaller shore,

\[
 K_{q,s}\le \min(f_s,f_{s-q}).                              \tag{1.3}
\]

The split-profile mass is

\[
 P_{q,s}=C_sC_{s-q}.                                         \tag{1.4}
\]

Consequently the incompatibility term in the literal common-order criterion
obeys the pointwise bound

\[
 P_{q,s}\left(1-{K_{q,s}^2\over f_sf_{s-q}}\right)
 \ge C_sC_{s-q}-\min(C_s,C_{s-q})^2.                         \tag{1.5}
\]

The right side is independent of every structural choice of factors.

## 2. Exact one-offset identity

Define the full formal cardinality loss

\[
 L_{b,q}=\sum_{s=q}^{b}
 \left(C_sC_{s-q}-\min(C_s,C_{s-q})^2\right).                \tag{2.1}
\]

Put `m=floor((b-q)/2)`.  Then

\[
 \boxed{
 L_{b,q}={2b\choose b+q}-A_{b,q},}                           \tag{2.2}
\]

where

\[
 A_{b,q}=
 \begin{cases}
  2\displaystyle\sum_{j=0}^{m}{b\choose j}^2,
       &b-q\text{ odd},\\[6pt]
  2\displaystyle\sum_{j=0}^{m-1}{b\choose j}^2
       +{b\choose m}^2,
       &b-q\text{ even}.
 \end{cases}                                                \tag{2.3}
\]

To prove this, Vandermonde's identity gives

\[
 \sum_{s=q}^{b}C_sC_{s-q}={2b\choose b+q}.                  \tag{2.4}
\]

The binomial row is unimodal and symmetric.  We have
`C_s>=C_(s-q)` exactly when `s<=(b+q)/2`.  On that half the
minimum square is `C_(s-q)^2`; on the other half it is `C_s^2`.
Reflecting the latter index by `j=b-s` gives (2.3), with the displayed
single boundary term when `b-q` is even.  This proves (2.2).

If the endpoint construction retains only central ranks, say

\[
 s,s-q\in[b/4,3b/4],                                        \tag{2.5}
\]

then deleting the other terms changes `L_(b,q)` by at most
`exp(-Omega(b))W_b`, uniformly for `q=O(sqrt(b))`.  Hence all asymptotics
below hold unchanged for the actual central factor banks.

## 3. The Gaussian obstruction at one offset

Suppose

\[
 {q\over\sqrt b}\longrightarrow c\in(0,\infty).            \tag{3.1}
\]

The first term of (2.2) has the standard central ratio

\[
 {{2b\choose b+q}\over W_b}\longrightarrow e^{-c^2}.       \tag{3.2}
\]

For the second term, the probability mass

\[
 \Pr(J=j)={{b\choose j}^2\over W_b}                         \tag{3.3}
\]

is hypergeometric with mean `b/2` and variance

\[
 \operatorname{Var}J={b^2\over4(2b-1)}\sim {b\over8}.       \tag{3.4}
\]

The cutoff in (2.3) is `(b-q)/2+O(1)`.  The hypergeometric
central limit theorem therefore gives

\[
 {A_{b,q}\over W_b}\longrightarrow
 2\Phi(-c\sqrt2)=\operatorname{erfc}(c).                    \tag{3.5}
\]

Combining (2.2), (3.2), and (3.5),

\[
 \boxed{{L_{b,q}\over W_b}\longrightarrow
 e^{-c^2}-\operatorname{erfc}(c).}                          \tag{3.6}
\]

The limit is strictly positive for every `c>0`, because

\[
 \operatorname{erfc}(c)
 ={2\over\sqrt\pi}e^{-c^2}
   \int_0^\infty e^{-u^2-2cu}\,du
 <{2\over\sqrt\pi}e^{-c^2}
   \int_0^\infty e^{-u^2}\,du
 =e^{-c^2}.                                                 \tag{3.7}
\]

For example, at `c=1` it is approximately `0.210578`.
Equations (1.5), (2.5), and (3.6) prove (0.1).

## 4. The aggregate `b^(1/4)` threshold

Uniformly for `q=o(sqrt(b))`, the same local central-limit estimates and
the Taylor expansions at zero give

\[
 {L_{b,q}\over W_b}
 ={2q\over\sqrt{\pi b}}
  +O\left({q^2\over b}+{1\over\sqrt b}\right).              \tag{4.1}
\]

Let `Q->infinity` with `Q=o(sqrt(b))`.  Summing (4.1) yields

\[
 \sum_{q=1}^{Q}L_{b,q}
 ={Q(Q+1)\over\sqrt{\pi b}}W_b
 +O\left(\left({Q^3\over b}+{Q\over\sqrt b}\right)W_b\right)
 =\left({1+o(1)\over\sqrt\pi}\right)
 {Q^2\over\sqrt b}W_b.                                     \tag{4.2}
\]

This proves (0.2).  In particular:

* if `Q=o(b^(1/4))`, the cardinality obstruction is `o(W_b)`;
* if `Q` is of order `b^(1/4)`, it is of order `W_b`;
* if `b^(1/4)<<Q<<sqrt(b)`, it is `omega(W_b)`;
* if `q` itself is of order `sqrt(b)`, one offset already costs
  `Theta(W_b)` by (3.6).

The DCC endpoint band has `H/sqrt(b)->infinity`, so the literal criterion
cannot close that band.

## 5. Exact surviving gate

The complementary construction works because `s+(s-q)=b`, making
`f_s=f_(s-q)` and allowing the two ranks to use the same orders by literal
complementation.  Away from that diagonal, the size mismatch in (1.3)
cannot be repaired by a more clever choice of exact factors.

Therefore the remaining endpoint theorem must exploit at least one of:

1. interval-coordinate couplings between nonidentical cyclic orders;
2. a cross-rank factor whose neighboring-rank interval decks form a
   controlled multi-cover, rather than literal bank intersection;
3. the one-sided scalar surplus in the constant-origin capacity formula,
   with an integral transport assigning that surplus to uncovered targets.

This barrier is scoped only to literal common-order overlap.  It is not a
no-go theorem for any of the three mechanisms above.
