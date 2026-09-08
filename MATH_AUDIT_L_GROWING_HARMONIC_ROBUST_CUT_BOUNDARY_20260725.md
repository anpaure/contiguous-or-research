# Cross-audit of the growing-harmonic robust-cut boundary

Date: 2026-07-25

Audited source:
`MATH_ATTACK_L_GROWING_HARMONIC_ROBUST_CUT_BOUNDARY_20260725.md`.

## 1. Verdict

The following parts of the source report are correct with their displayed
constants and quantifiers:

1. the revised first-shadow constant
   \(K'_m=2(2m+1)(2m-1)/(m(m+1))<8\);
2. the uniform low-degree truncation (5.9) and the genuinely growing-degree
   lower bound (5.10);
3. the shallow-\(E_2\) oscillation estimate (6.4); and
4. the fixed-transposition reduced-cut no-go (6.6), with the exact
   quantifier order stated in Section 4 below.

The exact MSW cell used in Sections 5--6 consists throughout of literal
integral exact factors.  No abstract histogram or Gram model enters those
sections.

One scope distinction is necessary in Section 7.  The constructed object is
an integral first-shadow histogram satisfying the enumerated support-level
scalar conditions.  Its run lengths are then completed separately for each
coordinate set.  The report does **not** construct a common system of owner
rows realizing those completions, and it does not prove that such a
realization is impossible.  Consequently the proved no-go concerns the
listed scalar support constraints and separately feasible tails; it is not a
no-go for the full simultaneous all-depth common-row chronology.

No adaptive-transposition theorem and no constant-one theorem follows from
the audited report.

## 2. Audit of the constant \(K'_m\)

Put \(n=2m+1\), \(W=\binom nm\), and \(t=W/n\).  For a pair
\(e=\{a,b\}\), let \(h_e\) be the number of factor rows in which \(a,b\)
have cyclic distance \(m\).  In one row there are exactly \(n\) such pairs,
so

\[
 \frac1{\binom n2}\sum_e h_e
 =\frac{nt}{nm}=\frac tm.
\tag{2.1}
\]

The total number of middle windows containing a fixed pair is

\[
 G_2=\binom{n-2}{m-2}=\frac{m-1}{2}t.
\]

A row in which the pair is not antipodal contains the pair in at most
\(m-1\) middle windows.  Hence at least \(\lceil t/2\rceil\) rows are
nonantipodal, and therefore

\[
 0\le h_e\le \left\lfloor\frac t2\right\rfloor\le\frac t2.
\tag{2.2}
\]

Bhatia--Davis applied to (2.1)--(2.2) gives

\[
 \sum_e\left(h_e-\frac tm\right)^2
 \le \binom n2\frac tm\left(\frac t2-\frac tm\right)
 =\frac{n(m-2)}{2m}t^2.
\tag{2.3}
\]

Exact total and point margins remove Johnson degrees zero and one.  Dividing
(2.3) by the degree-two inclusion singular value

\[
 \alpha_{1,2}=\binom{2m-3}{m-3}
\]

therefore yields

\[
 \|P_{E_2}f_1\|_2^2
 \le \frac{n(m-2)t^2}{2m\alpha_{1,2}}
 =K'_m t.
\]

Indeed,

\[
 \frac{W}{\alpha_{1,2}}
 =\frac{4(2m+1)(2m-1)}{(m+1)(m-2)},
\]

and hence

\[
 \boxed{K'_m=\frac{2(2m+1)(2m-1)}{m(m+1)}}.
\tag{2.4}
\]

Finally,

\[
 8-K'_m
 =\frac{8m(m+1)-2(4m^2-1)}{m(m+1)}
 =\frac{8m+2}{m(m+1)}>0.
\]

Thus the constant in (2.10) is exact for the displayed argument and tends
to eight from below.

## 3. Audit of the high-degree truncation

Fix \(A>0\), let \(H=\lceil A\sqrt m\rceil\), and put

\[
 J=J_m^{\rm cell}
 =\left\lfloor\frac{H}{8\log(108m)}\right\rfloor.
\]

Then \(J\to\infty\) and \(J=o(m)\).  For all sufficiently large \(m\),
the estimates below hold simultaneously for every exact factor \(F\), every
\(q\le H\), and every \(2\le j\le J\).

The run-cap envelope gives

\[
 \|P_{E_j}f_q\|_2^2
 \le
 \frac{\binom nj q^2t^2}{4\alpha_{q,j}},
 \qquad
 \alpha_{q,j}=\binom{n-2j}{m-q-j}.
\tag{3.1}
\]

Since \(\lambda_q=W/N_q>1\), where
\(N_q=\binom n{m-q}\),

\[
 c_q=\lfloor\lambda_q\rfloor\ge\frac{\lambda_q}{2},
 \qquad
 \frac1{c_q}\le\frac{2N_q}{W}.
\tag{3.2}
\]

The factorial cancellation used in the source is exact:

\[
 \frac{N_q}{\alpha_{q,j}}
 =\frac{(n)_{2j}}{(m-q)_j(m+q+1)_j}.
\tag{3.3}
\]

Because \(q,j\le m/4\) eventually, each denominator factor in (3.3) is
at least \(m/2\), whereas each numerator factor is at most \(3m\).
Consequently

\[
 \frac{N_q}{\alpha_{q,j}}\le36^j,
 \qquad
 \binom nj\le(3m)^j.
\tag{3.4}
\]

Combining (3.1)--(3.4), using \(W=nt\), gives

\[
 \frac1{c_q}\|P_{E_j}f_q\|_2^2
 \le\frac{q^2t}{2n}(108m)^j.
\tag{3.5}
\]

For \(108m\ge2\),

\[
 \sum_{q=1}^Hq^2\le H^3,
 \qquad
 \sum_{j=2}^J(108m)^j\le2(108m)^J,
\]

and the definition of \(J\) gives
\((108m)^J\le e^{H/8}\).  Therefore

\[
 \boxed{
 \sum_{q\le H}\sum_{2\le j\le J}
 \frac{\|P_{E_j}f_q(F)\|_2^2}{c_q}
 \le\frac{tH^3}{n}e^{H/8}.}
\tag{3.6}
\]

This proves (5.9) with no hidden dependence on \(F\).

For the MSW-cell minimizer \(G_m\), the private-pair theorem gives

\[
 \mathcal Q_A(G_m)
 \ge L_m:=\frac{t4^H}{1024M_AH^4}.
\tag{3.7}
\]

At every depth, exact total and point margins kill \(E_0,E_1\), while

\[
 \|f_q\|_2^2=Q_q+\beta_q.
\]

Thus

\[
 \sum_{q\le H}\sum_{j\ge2}
 \frac{\|P_{E_j}f_q(G_m)\|_2^2}{c_q}
 =\mathcal Q_A(G_m)+\sum_{q\le H}\frac{\beta_q}{c_q}
 \ge L_m.
\tag{3.8}
\]

The ratio of the right side of (3.6) to \(L_m/2\) is

\[
 \frac{2048M_AH^7e^{H/8}}{n4^H}.
\tag{3.9}
\]

Its logarithm is

\[
 -\left(\log4-\frac18\right)H+7\log H-\log n+O_A(1),
\]

which tends to \(-\infty\), since \(H\asymp_A\sqrt m\) and
\(\log4-1/8>0\).  Hence (3.6)--(3.9) prove, eventually,

\[
 \boxed{
 \sum_{q\le H}\sum_{j>J}
 \frac{\|P_{E_j}f_q(G_m)\|_2^2}{c_q}
 \ge\frac{t4^H}{2048M_AH^4}.}
\tag{3.10}
\]

The high-degree assertion is therefore a theorem about a literal exact
factor, not about the pseudohistogram of Section 7.

## 4. Audit of the reduced-cut no-go

Let \(Q_0=\lfloor m^{1/8}\rfloor\).  For a component signing
\(\varepsilon\) in a fixed transposition cell, both endpoints are complete
exact factors.  Orthogonal midpoint/antisymmetric decomposition gives the
exact degree-two sector identity

\[
 \|P_{E_2}f_q^{G_\varepsilon}\|_2^2
 -\|P_{E_2}f_q^G\|_2^2
 =\frac14\bigl(R_{\tau,q,2}(\varepsilon)-A_{\tau,q,2}\bigr).
\tag{4.1}
\]

The improved two-star estimate in the source gives, for either complete
endpoint,

\[
 R_{\tau,q,2}(\varepsilon),A_{\tau,q,2}
 \le\frac{2q^2(q+1)t^2}{\alpha_q}.
\tag{4.2}
\]

For completeness, the Gaussian-window constant used here follows directly
from

\[
 \frac W{\alpha_q}
 =\lambda_q\frac{(n)_4}
 {(m-q)_2(m+q+1)_2}.
\tag{4.2a}
\]

Uniformly for \(q\le H\), eventually the rational factor in (4.2a) is at
most \(81\).  Moreover

\[
 \log\lambda_q
 =\sum_{i=1}^q
 \log\left(1+\frac{q+1}{m-q+i}\right)
 \le\frac{q(q+1)}{m-q+1}
 \le2(A+3)^2
\]

for all sufficiently large \(m\).  Thus

\[
 \frac W{\alpha_q}\le81e^{2(A+3)^2}=\Gamma_A.
\tag{4.2b}
\]

Since \(c_q\ge1\), \(W=nt\), and (4.2b) holds uniformly for
\(q\le H\), (4.1)--(4.2) imply

\[
 \frac1{c_q}\left|
 \|P_{E_2}f_q^{G_\varepsilon}\|_2^2
 -\|P_{E_2}f_q^G\|_2^2\right|
 \le\Gamma_Aq^2(q+1)\frac tn.
\tag{4.3}
\]

For \(Q_0\ge2\),
\(\sum_{q\le Q_0}q^2(q+1)\le Q_0^4\).  Also

\[
 Q_0^4\le\sqrt m\le\frac HA.
\]

Therefore the displayed oscillation bound is correct:

\[
 \boxed{
 |\mathcal S_{Q_0}(G)-\mathcal S_{Q_0}(G_\varepsilon)|
 \le\frac{\Gamma_A}{A}\frac{Ht}{n}.}
\tag{4.4}
\]

Now choose \(G_m\) to minimize the full potential on the finite intrinsic
MSW cell.  Component persistence ensures that every correlated signing
remains in this same cell, so

\[
 \mathcal Q_A(G_m)-\mathcal Q_A((G_m)_\varepsilon)\le0.
\]

Subtracting the shallow sector and applying (4.4) proves

\[
 \max_\varepsilon\bigl[
 \mathcal Q_A^{\rm red}(G_m)
 -\mathcal Q_A^{\rm red}((G_m)_\varepsilon)\bigr]
 \le\frac{\Gamma_A}{A}\frac{Ht}{n}.
\tag{4.5}
\]

On the other hand,

\[
 \mathcal Q_A^{\rm red}(G_m)
 \ge\frac{t4^H}{1024M_AH^4}
 -\frac{\Gamma_A}{2A}Ht.
\tag{4.6}
\]

For fixed \(B>0\), division of the leading term in (4.6) by
\(m^B Ht/n\) gives

\[
 \frac{n4^H}{1024M_Am^BH^5}\longrightarrow\infty,
\tag{4.7}
\]

because its logarithm is
\(H\log4-(B+3/2+o(1))\log m\to\infty\).
The subtracted term in (4.6) is polynomial and is absorbed by the same
exponential term.  Consequently the exact quantifier form of (6.6) is

\[
 \boxed{
 \begin{gathered}
 \forall A,B,C>0\ \exists m_0\ \forall m\ge m_0\
 \forall\tau\in\binom{[n]}2\ \exists\text{ an exact factor }G_{m,\tau}:\\
 \max_\varepsilon\bigl[
 \mathcal Q_A^{\rm red}(G_{m,\tau})
 -\mathcal Q_A^{\rm red}((G_{m,\tau})_\varepsilon)\bigr]
 \le\frac{\Gamma_A}{A}\frac{Ht}{n}\\
 <m^{-B}\mathcal Q_A^{\rm red}(G_{m,\tau})
 -C\frac{Ht}{n}.
 \end{gathered}}
\tag{4.8}
\]

Conjugating the \((2\,3)\)-cell proves the universal quantifier over the
prescribed \(\tau\); the threshold is independent of \(\tau\).
The factor may depend on \(A,m,\tau\).  It can be chosen independently of
\(B,C\), although the threshold \(m_0\) in (4.8) depends on all three
constants.

Equation (4.8) refutes a lower bound of the specific form

\[
 \text{reduced gain}\ge m^{-B}\mathcal Q_A^{\rm red}
 -C Ht/n
\]

for a transposition prescribed before the factor.  It does not refute an
adaptive choice \(\tau=\tau(F)\), a coefficient smaller than every inverse
polynomial, or a different reduced objective.

## 5. Genuine-factor status of Sections 5--6

The imported MSW cell lemma supplies a partition of the middle layer into
\(\tau\)-invariant component-root unions.  Choosing either shore on each
root union gives an integral squarefree exact factor.  Recomputing the
\(\tau\)-overlay merely reverses shores inside the same root unions, so the
cell is intrinsic at every vertex.

The private target pairs have cell-invariant pair totals at least
\(\operatorname{Cat}_H\).  Since the floor polynomial
\((x-c_H)(x-c_H-1)\) is nonnegative at every integral load, the private-pair
lower bound applies to every cell vertex, including the cell minimizer.
Thus the minimization, the high-degree lower bound, and the reduced-cut
no-go never leave the category of exact factors.

This confirms that Sections 5--6 do not make the abstract-to-exact mistake
which the audit was asked to test.

## 6. Exact scope of the scalar no-go

For \(m\equiv0\pmod6\), Section 7 selects \(t/2\) full translation orbits
of \((m-1)\)-sets and defines \(\mu=2\mathbf1_{\mathcal H}\).  The orbit
regularity proves exactly

\[
 \sum_S\mu(S)=W,
 \qquad
 \sum_{S\ni v}\mu(S)=(m-1)t.
\]

The concentration and deterministic tail arguments in that section do
prove the displayed support capacities (7.3), nesting (7.4), recurrence
(7.5), and support-level three-witness inequality (7.6).  The singular-value
calculation also proves

\[
 \sum_{2\le j\le n/(12\log n)}\|P_{E_j}f\|_2^2=o(t),
 \qquad Q_1=(1-o(1))W.
\]

For each fixed coordinate set \(X\), the capacity interval permits positive
integers

\[
 g_1(X),\ldots,g_{\rho(X)}(X)\le m-|X|+1,
 \qquad \sum_a g_a(X)=G_{|X|},
\]

and hence a separately feasible tail
\(L_{X,q}=\sum_a\min(q,g_a(X))\).  This is all that (7.15) proves.
It does not assign the integers for different \(X\)'s to common owner rows,
does not make the completions jointly monotone, and does not establish the
all-depth three-witness inequality (3.1) simultaneously for those tails.

Accordingly, the sentence that the object “is not an exact factor” should
be read as “no exact-factor realization is supplied.”  Nonrealizability of
the histogram by some exact factor is not proved.  The rigorous conclusion
is nonetheless a valid scalar-model no-go: the explicitly enumerated
support-level constraints, even with separate per-set tail feasibility, do
not by themselves imply a small-energy harmonic conclusion.

## 7. Proved boundary after audit

The audited report rigorously closes the following lane:

*a transposition prescribed independently of the factor cannot satisfy an
inverse-polynomial robust reduced-cut gain theorem for the potential and
cutoff in (6.1).*

It also proves that a genuine locked prescribed cell can place
\(\omega_A(Ht)\) weighted energy above a Johnson degree tending to infinity.

What it does not close is the adaptive statement

\[
 \forall F\ \exists\tau(F)\ \exists\varepsilon
\]

with a productive freshly recomputed component cut.  Nor does the scalar
pseudohistogram remove the common-owner chronology requirement.  Those two
points are the exact surviving boundary; no constant-one conclusion is
audited or obtained here.
