# An affine hash makes every geodesic strip row rainbow at once

Date: 2026-07-25

Method: pure mathematics only.

## 0. Result

The protected diagonal-strip targets of a geodesic grid admit an exact
low-entropy simultaneous hash.  Let (p) be prime and let

\[
 h:[2m]\longrightarrow\mathbb F_p
\]

be any coordinate labeling.  Suppose a buffered geodesic has departure
and arrival coordinates satisfying

\[
 h(a_i)=A+\alpha i,
 \qquad
 h(b_i)=B+\alpha i
 \qquad(1\le i\le g),
 \tag{0.1}
\]

for some (alpha\ne0).  Put (delta=B-A), and hash a Boolean target by

\[
 \chi(S)=\sum_{x\in S}h(x).
 \tag{0.2}
\]

Then every protected lower row is an arithmetic progression of step
(delta-alpha q), and every protected upper row is an arithmetic
progression of step (delta+alpha q).  Thus, if

\[
 {delta\over\alpha}\notin\{-Q,-Q+1,\ldots,Q\},
 \tag{0.3}
\]

all (2Q+1) rows are simultaneously hash-injective through any block of
at most (p) consecutive physical phases.  For a block of exactly (p)
phases, each row uses every hash value exactly once.

This is not yet a matching theorem.  It gives a common global partition
of the target universe in which every affine-labeled candidate chunk has
at most one claimed target in each rank--hash part.  It is a concrete
algebraic condition capable of seeing singleton intersections, which the
width-two nonlinear moment deliberately subtracts.

## 1. Exact calculation

Use grid notation

\[
 G_{i,j}
 =C\cup\{a_{i+1},\ldots,a_g\}
    \cup\{b_1,\ldots,b_j\}.
\]

For a physical phase (t), the lower and upper targets are

\[
 L_q(t)=G_{t+q,t},
 \qquad
 U_q(t)=G_{t-q,t}.
 \tag{1.1}
\]

Moving from (t) to (t+1), the lower target loses
(a_{t+q+1}) and gains (b_{t+1}).  Therefore

\[
\begin{aligned}
 \chi(L_q(t+1))-\chi(L_q(t))
 &=h(b_{t+1})-h(a_{t+q+1})\\
 &=\delta-\alpha q.
\end{aligned}
 \tag{1.2}
\]

Likewise the upper target loses (a_{t-q+1}) and gains (b_{t+1}), so

\[
 \chi(U_q(t+1))-\chi(U_q(t))
 =\delta+\alpha q.
 \tag{1.3}
\]

At (q=0), this is the owner row and its step is (delta).  Condition
(0.3) makes every step in (1.2)--(1.3) nonzero.  A nonzero arithmetic
progression in (mathbb F_p) is injective for at most (p) consecutive
terms and is a permutation of (mathbb F_p) for exactly (p) terms.
This proves the assertion. \(\square\)

## 2. Buffered physical blocks

Take (p) physical phases and (Q) certificate phases on both sides.
The affine label sequences in (0.1) then have length (p+2Q).  Labels may
repeat modulo (p), but the physical coordinates need not: it is enough
that every label class of (h) supplies the at most two coordinates used
by each of the two strings.  A balanced labeling has class size

\[
 (2+o(1)){m\over p}\longrightarrow\infty
\]

when (p\asymp g=m^{1/2+o(1)}).  Hence the buffer creates no local
existence obstruction.

If priorities retain only (c_q\) of the (p) phase columns at depth
(q), the retained row is still hash-rainbow.  Thus every decorated path
is a transversal of the global parts

\[
 \{S:|S|=m\pm q,\ \chi(S)=r\},
 \qquad r\in\mathbb F_p, 0\le q\le Q,
\]

using at most one target in each part.

## 3. Exact remaining algebraic gate

To turn the lemma into coefficient one, one would need a global balanced
labeling (h) and a large affine-labeled subcatalogue satisfying both:

1. all but (o(W)) tag/target capacity survives the affine restriction;
2. the induced transversal design obeys the weighted matching-dispersal
   inequality excluding truncated-projective-plane/Berge-cycle
   obstructions.

The first point is an entropy and hypergeometric-balance problem.  The
second is not automatic from partiteness: truncated projective planes are
themselves uniform partite intersecting systems.  Additional affine
parallel-class structure, if present in the actual grid catalogue, must be
used explicitly.

