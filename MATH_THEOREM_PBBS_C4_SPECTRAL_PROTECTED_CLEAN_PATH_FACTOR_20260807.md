# C4--spectral extension of the complete clean PBBS packet bank

## Status and scope

This note closes the **first protected-factor gate** left open in
`MATH_AUDIT_PBBS_LAG2_BPLUS2_SHORTEST_CHAIN_AND_FIRST_FACTOR_GATE_20260807.md`.

It proves, for all sufficiently large middle-level parameters, that the
entire resource-disjoint bank of complete clean four-edge packet paths is
contained in a spanning two-factor.  In particular, the earlier sufficient
restriction

\[
 4h\le m-1
\]

is not needed for this clean bank.

The result is only a two-factor theorem.  It does **not** connect the factor,
construct a common literal antecedent, prove the arbitrary-width upper deck,
or solve the lower compiler.

## 1. Statement

Let

\[
 G=ML_{m+1}=(X,Y;E)
\]

be the middle-levels incidence graph on a \((2m+1)\)-element ground set:
\(X=\binom{[2m+1]}m\), \(Y=\binom{[2m+1]}{m+1}\), and adjacency is
containment.  Put

\[
 r=m+1,\qquad |X|=|Y|=W.
\]

### Theorem 1.1 (sublinear-slack protected degree-two theorem)

Fix a constant \(0<\alpha<1\).  For all sufficiently large \(m\), the
following holds.

If \(P\subseteq G\) satisfies

\[
 \Delta(P)\le2,\qquad |E(P)|\le2H,\qquad H\le\alpha r,
 \tag{1.1}
\]

then \(P\) is contained in a spanning two-factor of \(G\).

### Corollary 1.2 (complete clean packet bank)

Let \(P\) be the union of the pairwise resource-disjoint complete clean
packet paths

\[
 T_-\subset J_-\supset T_0\subset J_+\supset T_+ .
 \tag{1.2}
\]

If there are \(h\le\binom{d+1}{2}\) such paths and

\[
 \frac{d^2}{m}\longrightarrow\frac\pi4,
 \tag{1.3}
\]

then, for all sufficiently large \(m\), \(P\) is contained in a spanning
two-factor of \(ML_{m+1}\).

Indeed, resource-disjointness makes (1.2) a union of vertex-disjoint
four-edge paths, so

\[
 \Delta(P)\le2,\qquad |E(P)|=4h.
 \tag{1.4}
\]

Set \(H=2h\).  Then

\[
 \frac Hr\le\frac{d(d+1)}{m+1}=\frac\pi4+o(1)<1,
 \tag{1.5}
\]

and Theorem 1.1 applies with any fixed
\(\alpha\in(\pi/4,1)\).

## 2. Exact factor cut

For completeness, recall the exact residual \(b\)-factor condition.  A
spanning two-factor \(F\supseteq P\) exists if and only if, for every
\(A\subseteq X\) and \(B\subseteq Y\),

\[
 \boxed{
 e_G(A,B)+(r-2)(W-|A|-|B|)\ge e_P(A,B).}
 \tag{2.1}
\]

This is the bipartite max-flow/min-cut criterion for the residual demands
\(2-d_P(v)\).  Thus Theorem 1.1 follows once (2.1) is checked.

If \(|A|+|B|\le W\), then (2.1) is immediate: its second term is
nonnegative and \(P\subseteq G\) gives
\(e_G(A,B)\ge e_P(A,B)\).

It remains to consider

\[
 q:=|A|+|B|-W>0.
 \tag{2.2}
\]

Write

\[
 S=X\setminus A,\qquad C=Y\setminus B,
 \qquad s=|S|,\quad c=|C|.
\]

Then \(s+c=W-q\), and regularity gives the exact identity

\[
 e_G(A,B)-(r-2)q=e_G(S,C)+2q.
 \tag{2.3}
\]

The two shores play symmetric roles in all estimates below, so assume
without loss of generality that

\[
 s\le c.
 \tag{2.4}
\]

Since

\[
 |B|=W-c=q+s\le q+c=|A|,
\]

the degree and total-edge bounds on \(P\) imply

\[
 e_P(A,B)\le 2\min(q+s,H).
 \tag{2.5}
\]

Therefore it is enough to prove

\[
 e_G(S,C)+2q\ge2\min(q+s,H).
 \tag{2.6}
\]

## 3. The elementary cut regimes

If \(q\ge H\), then (2.6) follows from
\(e_G(S,C)\ge0\).

Assume henceforth that \(q<H\), and put

\[
 t=H-q>0.
 \tag{3.1}
\]

### 3.1. The small-shore regime \(s\le t\)

Here \(|B|=q+s\le H\).  Each vertex of \(S\) has at most \(|B|\)
neighbours outside \(C\), so

\[
 e_G(S,C)\ge s(r-q-s)\ge s(r-H).
 \tag{3.2}
\]

Because \(H\le\alpha r\), for all sufficiently large \(r\) we have
\(r-H\ge2\).  Hence \(e_G(S,C)\ge2s\), and

\[
 e_G(S,C)+2q\ge2(s+q)
 =2\min(q+s,H).
 \tag{3.3}
\]

### 3.2. The remaining regime \(s>t\)

Now (2.5) is at most \(2H\), so it is enough to prove

\[
 e_G(S,C)\ge2t.
 \tag{3.4}
\]

Put \(b=|B|=q+s\).  If \(b\le r-2\), write
\(s=t+u\).  Since \(q=H-t\),

\[
 b=H+u,
 \qquad 0\le u\le r-H-2.
\]

Again using the elementary degree bound,

\[
 e_G(S,C)\ge s(r-b)
 =(t+u)(r-H-u).
 \tag{3.5}
\]

The expression on the right is concave in \(u\).  At the endpoints of
the displayed interval it equals respectively

\[
 t(r-H)\ge2t,
 \qquad
 2(t+r-H-2)\ge2t.
\]

Thus (3.4) holds whenever \(b\le r-2\).

The only cut regime still open is therefore

\[
 q<H\le\alpha r,qquad s>t,qquad b=q+s\ge r-1.
 \tag{3.6}
\]

In particular,

\[
 s\ge r-1-q\ge(1-\alpha)r-1.
 \tag{3.7}
\]

The next two sections handle (3.6), first up to quadratic shore size by
the absence of four-cycles, and then above quadratic size by the exact
middle-levels spectral gap.

## 4. C4-free control up to quadratic size

Two distinct vertices of \(X\) have at most one common neighbour in
\(Y\): if two distinct \(m\)-sets possess a common \((m+1)\)-superset,
that superset is their unique union.  Thus \(G\) is \(C_4\)-free.

For \(y\in Y\), put

\[
 d_y=|N_G(y)\cap S|.
\]

The \(C_4\)-free property gives

\[
 \sum_{y\in Y}\binom{d_y}{2}\le\binom{s}{2}.
\]

Since \(\sum_y d_y=rs\),

\[
 \sum_{y\in Y}d_y^2
 =rs+2\sum_y\binom{d_y}{2}
 \le rs+s(s-1)\le s(r+s).
 \tag{4.1}
\]

Cauchy--Schwarz on \(B\) now yields

\[
 e_G(S,B)\le\sqrt{b\,s(r+s)},
\]

and hence

\[
 e_G(S,C)
 \ge rs-\sqrt{(s+q)s(r+s)}
 =rs\bigl(1-\sqrt R\bigr),
 \tag{4.2}
\]

where

\[
 R=\frac{(s+q)(r+s)}{r^2s}
 =\frac{s}{r^2}+\frac1r+\frac{q}{r^2}+\frac{q}{rs}.
 \tag{4.3}
\]

Choose

\[
 \kappa=\frac{1+\alpha}{2},
 \qquad \alpha<\kappa<1.
 \tag{4.4}
\]

If \(s\le\kappa r^2\), then (3.7), \(q\le\alpha r\), and (4.3)
give

\[
 R\le\kappa+o(1).
 \tag{4.5}
\]

Consequently there is a constant \(\varepsilon_1>0\), depending only on
\(\alpha\), such that for all sufficiently large \(r\),

\[
 e_G(S,C)\ge\varepsilon_1rs=\Omega_\alpha(r^2).
 \tag{4.6}
\]

This is larger than \(2t\le2H\le2\alpha r\), proving (3.4) throughout
the range \(s\le\kappa r^2\).

## 5. Spectral control above quadratic size

Let \(M\) be the \(X\)-by-\(Y\) incidence matrix of \(G\).  Then

\[
 MM^{\mathsf T}=rI+A(J(2m+1,m)).
\]

The Johnson eigenvalues show that the singular values of \(M\) are

\[
 r,r-1,\ldots,1.
\]

In particular the second singular value is exactly \(r-1\).  Bipartite
expander mixing therefore gives

\[
 e_G(S,C)\ge
 \frac{rsc-(r-1)\sqrt{sc(W-s)(W-c)}}{W}.
 \tag{5.1}
\]

Because \(W-s=c+q\) and \(W-c=s+q\), this is

\[
 e_G(S,C)\ge
 \frac{sc}{W}
 \left[
 r-(r-1)
 \sqrt{\left(1+\frac qs\right)
       \left(1+\frac qc\right)}
 \right].
 \tag{5.2}
\]

Assume now that \(s>\kappa r^2\).  Since \(c\ge s\) and
\(q\le\alpha r\), put \(x=q/s\), \(y=q/c\); then

\[
 0\le y\le x\le\frac{\alpha}{\kappa r}.
\]

Using \(\sqrt{1+z}\le1+z/2\),

\[
 \sqrt{(1+x)(1+y)}
 \le1+\frac{x+y+xy}{2}
 \le1+x+\frac{x^2}{2}.
 \tag{5.3}
\]

It follows that the bracket in (5.2) is at least

\[
 1-(r-1)\left(x+\frac{x^2}{2}\right)
 \ge 1-\frac\alpha\kappa-o(1).
 \tag{5.4}
\]

The right side is bounded below by a positive constant
\(\varepsilon_2=\varepsilon_2(\alpha)\) for all sufficiently large
\(r\), because \(\alpha<\kappa\).

Finally, \(s+c=W-q\) and \(c\ge s\), so \(c/W\ge1/3\) for all
sufficiently large \(m\).  Hence

\[
 e_G(S,C)
 \ge\varepsilon_2\frac{sc}{W}
 \ge\frac{\varepsilon_2}{3}s
 >\frac{\varepsilon_2\kappa}{3}r^2.
 \tag{5.5}
\]

Again this is larger than \(2t\le2\alpha r\).  This proves (3.4) in
the last cut regime.

Combining Sections 2--5 verifies every cut (2.1), and the residual
\(b\)-factor criterion proves Theorem 1.1. \(\square\)

## 6. What this removes, and what remains

For the selected complete clean packet bank, the implication

\[
 \boxed{
 \text{resource-disjoint clean packet paths}
 \Longrightarrow
 \text{protected spanning middle-levels two-factor}}
 \tag{6.1}
\]

is now unconditional for every sufficiently large optimal parameter.

The proof uses only:

1. the exact residual factor cut;
2. the degree-two and total-size ledger of the packet bank;
3. the \(C_4\)-free property of middle-levels incidence; and
4. its exact second singular value \(r-1\).

No randomness or co-selection of the packet paths is needed after their
resource-disjointness has been established.

The next gate is genuinely later: one must turn the protected two-factor
into the required chronology and decorate the unprotected factor edges by
one common literal history while retaining residence, the full upper deck,
and terminal lower compilation.  The theorem here makes no claim about
that correlated decoration problem.
