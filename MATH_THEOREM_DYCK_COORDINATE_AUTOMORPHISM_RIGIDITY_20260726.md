# Dyck coordinate-rigidity: the full automorphism group and the universal coordinate-conjugate minimax theorem

Date: 2026-07-26

Method: hand mathematics only.  No finite search, solver, or web input is
used.

Let

\[
 {\cal D}_s=\left\{P\in\binom{[2s]}s:
       2|P\cap[t]|-t\geq0\quad(0\leq t\leq2s)\right\}
\]

be the family of Dyck \(s\)-subsets.  Write \(C_n=\operatorname{Cat}_n\),
and put

\[
 H_s=\left\langle(2i\ \ 2i+1):1\leq i\leq s-1\right\rangle.
 \tag{0.1}
\]

The purpose of this note is to determine the whole coordinate automorphism
group, rather than merely exhibit the subgroup (0.1).

## 0. Result

### Theorem 0.1 (full coordinate automorphism group)

For every \(s\geq1\),

\[
 \boxed{\operatorname {Aut}({\cal D}_s)=H_s\cong(C_2)^{s-1}.}
 \tag{0.2}
\]

There are no small-rank exceptions.  For \(s=1\), both sides of (0.2) are
trivial.  If one includes \(s=0\), both sides are again trivial.

In fact, coordinate degrees alone prove the theorem; no pair-codegree
refinement is needed.  If

\[
 d_s(t)=|\{P\in{\cal D}_s:t\in P\}|,
 \tag{0.3}
\]

then

\[
\begin{aligned}
 d_s(1)&=C_s,\\
 d_s(2i)=d_s(2i+1)
   &=C_s-\sum_{k=0}^{i-1}C_kC_{s-1-k}
     =\sum_{k=i}^{s-1}C_kC_{s-1-k}
       &&(1\leq i\leq s-1),\\
 d_s(2s)&=0.
\end{aligned}
\tag{0.4}
\]

For \(s\geq2\), these values satisfy the strict chain

\[
 d_s(1)>d_s(2)=d_s(3)>d_s(4)=d_s(5)>\cdots>
 d_s(2s-2)=d_s(2s-1)>d_s(2s).
 \tag{0.5}
\]

Consequently, for \(s\geq2\), the degree fibres are exactly

\[
 \{1\},\quad \{2,3\},\quad\{4,5\},\ldots,
 \quad\{2s-2,2s-1\},\quad\{2s\}.
 \tag{0.6}
\]

### Corollary 0.2 (all-block is universal among coordinate conjugates)

Let \(F_s\) be the canonical anchored exact \({\cal D}_s\)-port seed.  A
coordinate conjugate of \(F_s\) is again an anchored exact
\({\cal D}_s\)-port seed if and only if its coordinate permutation lies in
\(H_s\).  Therefore the adjacent-block grammar already exhausts **all**
coordinate-conjugate exact seeds.

In particular, combine Theorem 0.1 with the sharp common-core and quota
theorems for

\[
 \eta_s=\prod_{i=1}^{s-1}(2i\ \ 2i+1).
 \tag{0.7}
\]

If \(s\geq3\), then

\[
 \min_{\substack{\sigma\in\operatorname {Sym}([2s])\\
                  \sigma F_s\text{ is an exact }{\cal D}_s\text{ seed}}}
 \ \max_{j,k}M_{jk}^{(s)}(\sigma)
       =a_{s-1},
 \tag{0.8}
\]

where

\[
 \sum_{n\geq0}a_nz^n={1\over1-z(C(z)-1)}.
 \tag{0.9}
\]

Every coordinate conjugate has at least \(a_{s-1}\) rows in the top-root,
first-target-\(2s\) cell, and the all-block conjugate (0.7) has largest
cell exactly \(a_{s-1}\).  Thus it is minimax-optimal among every
coordinate-conjugate exact seed, not only among a provisionally chosen
grammar.

The only numerical small-rank qualification is \(s=2\): here
\(a_1=0\), while the minimax value is \(1\); both the identity and the
all-block swap are minimizers.  At \(s=1\), the minimax value is
\(1=a_0\).  This is a qualification of formula (0.8), not an exception to
the automorphism theorem.

The corollary concerns coordinate conjugates only.  It does not assert the
same lower bound for arbitrary non-conjugate exact factors or for a new
exterior-moving packet.

## 1. Every adjacent even-odd swap preserves the Dyck family

Encode \(P\) by its word \(w_1\cdots w_{2s}\), where \(w_t=1\) means
\(t\in P\), and define

\[
 h_w(t)=\sum_{u\leq t}(2w_u-1).
 \tag{1.1}
\]

Fix \(1\leq i\leq s-1\), and swap the letters in positions \(2i\) and
\(2i+1\).  All prefix heights except possibly the height after position
\(2i\) are unchanged.  The height \(h_w(2i-1)\) is a nonnegative odd
integer, hence is at least one.  If the two letters are equal there is
nothing to check.  If they are mixed, changing \(10\) to \(01\) lowers
the one possibly affected height from \(h_w(2i-1)+1\) to
\(h_w(2i-1)-1\geq0\); changing \(01\) to \(10\) raises it.  Thus the
swap preserves the Dyck condition.  It is an involution, so it preserves
\({\cal D}_s\) bijectively.  Hence

\[
                         H_s\leq\operatorname {Aut}({\cal D}_s).
 \tag{1.2}
\]

## 2. Exact coordinate degrees

The useful local identity is

\[
 d_s(t)-d_s(t+1)=
 \begin{cases}
 C_iC_{s-i-1},&t=2i+1,\quad0\leq i\leq s-1,\\
 0,&t\text{ even}.
 \end{cases}
 \tag{2.1}
\]

To prove it, the left side of (2.1) is

\[
 \#\{w:w_tw_{t+1}=10\}-\#\{w:w_tw_{t+1}=01\}.
 \tag{2.2}
\]

Swapping these two adjacent letters pairs every Dyck word having \(01\)
with a Dyck word having \(10\), except precisely when the \(10\) begins
at height zero.  Indeed, away from height zero the swap is legal in both
directions, while a \(10\) at height zero would become a down-step below
zero.

The height before position \(t\) can be zero only when \(t-1\) is even.
Thus there is no exception for even \(t\).  If \(t=2i+1\), every
exceptional word has the unique form

\[
                         A\,10\,B,
 \tag{2.3}
\]

where \(A\) and \(B\) are arbitrary Dyck words of semilengths \(i\) and
\(s-i-1\), respectively.  This gives \(C_iC_{s-i-1}\) exceptions and
proves (2.1).

Every Dyck word begins with \(1\), so \(d_s(1)=C_s\).  Iterating (2.1)
therefore gives the first expression in (0.4).  The Catalan convolution

\[
                         C_s=\sum_{k=0}^{s-1}C_kC_{s-1-k}
 \tag{2.4}
\]

gives the second expression and also \(d_s(2s)=0\).  Finally,

\[
\begin{aligned}
 d_s(1)-d_s(2)&=C_{s-1}>0,\\
 d_s(2i+1)-d_s(2i+2)&=C_iC_{s-i-1}>0
       &&(1\leq i\leq s-2),\\
 d_s(2s-1)-d_s(2s)&=C_{s-1}>0,
\end{aligned}
\tag{2.5}
\]

which proves the strict degree-fibre statement (0.5)--(0.6).  At \(s=1\)
the two degree fibres are simply \(\{1\}\) and \(\{2\}\).

## 3. Rigidity and the minimax deduction

Every coordinate automorphism preserves coordinate degrees.  By (0.6),
it must fix \(1\) and \(2s\), and it must preserve each pair
\(\{2i,2i+1\}\) setwise.  Hence it belongs to

\[
 \prod_{i=1}^{s-1}\operatorname {Sym}(\{2i,2i+1\})=H_s.
 \tag{3.1}
\]

Together with (1.2), this proves Theorem 0.1.

Finally, coordinate conjugation transports the canonical root-port family
\({\cal D}_s\) to \(\sigma({\cal D}_s)\).  The transported seed has the
same anchored root-port family exactly when

\[
                         \sigma({\cal D}_s)={\cal D}_s.
 \tag{3.2}
\]

By Theorem 0.1, (3.2) is equivalent to \(\sigma\in H_s\).  The previously
proved common-core lower bound for every member of \(H_s\), and equality
for \(\eta_s\), therefore range over all coordinate-conjugate exact seeds.
This proves Corollary 0.2.
