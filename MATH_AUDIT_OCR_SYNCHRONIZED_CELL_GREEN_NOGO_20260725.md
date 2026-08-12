# Independent audit of the OCR synchronized-cell Green no-go

Date: 2026-07-25

Audited report:
MATH_ATTACK_OCR_SYNCHRONIZED_CELL_GREEN_NOGO_20260725.md.

Method: pure mathematics only; no computation, search, or solver.

## 0. Verdict

**Pass, with one scope clarification and one complementary source/sink
formula.**

The following claims are exact.

1. The common outer carrier is counted once by the length-\((2m-1)\)
   word \(\mathcal A R_0=R_s\mathcal C\).
2. The synchronized state, cap interval, and separator transitions have
   the stated indices.
3. The full-cell endpoint resolvent is

   \[
   \mathbf G_q(x)
   ={1\over F_{q+1}(x^2)}
   \begin{pmatrix}
   F_q(x^2)&x^q\\
   x^q&F_q(x^2)
   \end{pmatrix}.
   \]

4. After the exit separator, the critical transition has eigenvalues
   \(1\) and \(q/(q+2)\).
5. The exact source factor is

   \[
   {s-2h\over s-h+1},
   \]

   not \(1/(h+3)\).
6. The one-switch corner weight is

   \[
   w_{h,L}
   ={(h+2)(L+2)\over
     (h+L+2)^2(h+L+3)}.
   \]

7. The synchronized capped-carrier relaxation has total critical mass
   \(\Theta(s)\).

The scope clarification is important.  The lower bound counts marked
paths in the exact synchronized **capped relaxation**.  A single physical
\(T_h\) can contain more than one admissible marked prefix, and the
remaining full PBBS transition identities have not been imposed.
Therefore the result is a rigorous no-go for deriving
\(\Psi_s(1/2)=o(s)\) from caps, shared-word equality, and separator
chronology alone.  It is not a construction of \(\Theta(s)\) distinct
actual roots or a counterexample to coefficient one.

## 1. Rank and outer-carrier accounting

The dual endpoint word is

\[
 \mathcal A=(\overline T_{s-1}0)\cdots(\overline T_00).
\]

Since its block lengths sum to \(\delta(D_0)\),

\[
 |\mathcal A|=\delta(D_0).
\]

The canonical root factorization

\[
 D_0=P_01R_00
\]

gives

\[
 |R_0|=2m-\delta(D_0)-1.
\]

Hence

\[
 \boxed{|\mathcal A R_0|=2m-1.}
 \tag{1.1}
\]

Using

\[
 \mathcal A=R_sO,\qquad \mathcal C=OR_0,
\]

one obtains

\[
 \mathcal A R_0=R_sOR_0=R_s\mathcal C.
\]

Thus \(O\) occurs literally once.  Replacing the last zero in each dual
block by one reconstructs \(P_01\), and appending the one omitted final
zero reconstructs \(D_0\).  There is no missing bit or duplicated
carrier in this ledger.

## 2. Synchronized state and transitions

Suppose the forward parser is in \(S_p\) and the dual parser is in
\(\overline T_j\).  Let \(c\) be the height inside \(S_p\) and \(t\)
the height inside \(T_j\).  Their lifted physical heights are

\[
 p-1+c,\qquad s+j-t.
\]

Literal equality therefore gives

\[
 \boxed{t+c=q,\qquad q=s+j-p+1.}
 \tag{2.1}
\]

The caps \(c\le p\) and \(t\le s-1-j\), together with nonnegativity, give

\[
 \boxed{
 \max(0,q-p)\le t\le\min(q,s-1-j).}
 \tag{2.2}
\]

Both endpoints \(t=0\) and \(t=q\) occur exactly when

\[
 \boxed{1\le q\le\min(p,s-1-j).}
 \tag{2.3}
\]

At \(t=0\), consuming a dual separator changes

\[
 (p,j,q)\longmapsto(p,j-1,q-1).
 \tag{2.4}
\]

At \(t=q\), consuming a forward separator changes

\[
 (p,j,q)\longmapsto(p-1,j,q+1).
 \tag{2.5}
\]

Both formulas preserve (2.1), and both reduce \(p+j\) by one.  Thus the
block automaton is acyclic even though each cell contains an arbitrary
finite-path Green excursion.

## 3. Full-cell resolvent and the unit mode

On the path \(0,1,\ldots,q\), Cramer's rule gives the endpoint Green
matrix

\[
 \boxed{
 \mathbf G_q(x)
 ={1\over F_{q+1}(x^2)}
 \begin{pmatrix}
 F_q(x^2)&x^q\\
 x^q&F_q(x^2)
 \end{pmatrix}.}
 \tag{3.1}
\]

The off-diagonal minor contributes \(x^q\); the endpoint diagonal minor
is \(F_q\).  These indices are correct already at \(q=1\), where

\[
 \mathbf G_1(x)
 ={1\over1-x^2}
 \begin{pmatrix}1&x\\x&1\end{pmatrix}.
\]

The unique exit separator contributes one more factor \(x\).  Since

\[
 F_q(1/4)={q+1\over2^q},
\qquad
 F_{q+1}(1/4)={q+2\over2^{q+1}},
\]

the critical cell transition is

\[
 \boxed{
 \mathbf P_q={1\over2}\mathbf G_q(1/2)
 ={1\over q+2}
 \begin{pmatrix}q+1&1\\1&q+1\end{pmatrix}.}
 \tag{3.2}
\]

Thus

\[
 \mathbf P_q(1,1)^{\mathsf T}=(1,1)^{\mathsf T},
\qquad
 \mathbf P_q(1,-1)^{\mathsf T}
 ={q\over q+2}(1,-1)^{\mathsf T}.
 \tag{3.3}
\]

The invariant eigenvalue is exactly one.  It is not an estimate caused
by discarding a cap.

## 4. Exact source factor

Assume the overlap begins at a zero lying inside \(\overline T_h\).  At
that zero the forward parser enters \(S_s\), so \(p=s\), \(j=h\), and
(2.1) gives

\[
 q=t=h+1.
\]

Immediately before the zero, the prefix of \(T_h\) is an arbitrary path
from zero to \(h\) in the interval

\[
 0\le t\le H,\qquad H=s-1-h.
\]

It is not a first-passage path.  Its exact endpoint resolvent is

\[
 B_{H,h}(x)
 ={x^hF_{H-h}(x^2)\over F_{H+1}(x^2)}.
 \tag{4.1}
\]

Multiplication by the displayed zero and evaluation at \(x=1/2\) give

\[
 \begin{aligned}
 {1\over2}B_{H,h}(1/2)
 &=
 2^{-h-1}
 {F_{s-1-2h}(1/4)\over F_{s-h}(1/4)}\\
 &=\boxed{{s-2h\over s-h+1}.}
 \tag{4.2}
\end{aligned}
\]

The powers of two cancel exactly.  For
\(h\le(1/2-\varepsilon)s\), this quantity is bounded below by a positive
constant depending only on \(\varepsilon\).  Hence the source does not
supply a hidden reciprocal-height loss.

## 5. The one-switch corner weight

Start on the forward endpoint at

\[
 p=s,\qquad j=h,\qquad q=h+1.
\]

Take \(L\) same-side forward exits.  Their weights are

\[
 \prod_{q=h+1}^{h+L}{q+1\over q+2}
 ={h+2\over h+L+2}.
\]

The crossing occurs at \(q=h+1+L\), hence has weight

\[
 {1\over h+L+3}.
\]

After that crossing, exactly \(h\) same-side dual exits consume
\(T_{h-1},\ldots,T_0\).  Their weights are

\[
 \prod_{q=L+1}^{h+L}{q+1\over q+2}
 ={L+2\over h+L+2}.
\]

Therefore

\[
 \boxed{
 w_{h,L}
 ={(h+2)(L+2)\over
   (h+L+2)^2(h+L+3)}.}
 \tag{5.1}
\]

There is no off-by-one factor: the first product has \(L\) terms, the
last has \(h\) terms, and the crossing denominator is \(h+L+3\).

If

\[
 {s\over10}\le h,L\le{s\over8},
\]

then all forward cells satisfy

\[
 h+1+L\le s-1-h,\qquad h+1+L\le s-L.
\]

After the crossing, \(q\) decreases, the dual cap increases, and
\(p=s-L\) stays fixed, so every dual cell remains full.  In this rectangle

\[
 w_{h,L}\asymp s^{-1}.
\]

For each of the \(\Theta(s)\) sources \(h\), summing over
\(\Theta(s)\) choices of \(L\) gives order-one mass.  Hence

\[
 \mathcal G_s^{F\to D}\ge c s.
 \tag{5.2}
\]

Conversely, every full-cell matrix is stochastic, every truncated cell is
substochastic, and \(p+j\) decreases at every separator.  From one source,
the total first-arrival sink mass is at most one.  There are at most \(s\)
sources, so

\[
 \mathcal G_s^{F\to D}\le s.
 \tag{5.3}
\]

This proves the exact \(\Theta(s)\) capped-relaxation mass.

## 6. Complementary one-sided physical source/sink formula

There is a compatible direct check using only the reversed dual carrier.
Put

\[
 D_j^\vee=\operatorname {rev}(\overline T_j).
\]

Then

\[
 \operatorname {rev}(\mathcal A)
 =(0D_0^\vee)(0D_1^\vee)\cdots(0D_{s-1}^\vee),
\]

and \(\operatorname {rev}(O)\) is one literal prefix.  If that prefix
meets \(r\) separators, including its first bit, it ends in layer \(r-1\).
If its final within-block height is \(y\), then its ordinary net height is
\(y-r\).  Since \(\operatorname {net}(O)=-1\),

\[
 \boxed{y=r-1.}
 \tag{6.1}
\]

Thus the source is the boundary state \(e_0\) in layer zero and the sink
is \(e_{r-1}\) in layer \(r-1\).  This pins the physical sink; it is not
an arbitrary-height sum.

For caps on the increasing branch

\[
 a_j=a_0+j,\qquad a_0=\ell+1,
\]

the killed-path block Green formula gives the exact critical upper mass

\[
 \boxed{
 w_r={(\,a_0+1\,)^2\over
 (a_0+r)(a_0+r+1)}.}
 \tag{6.2}
\]

Summing over \(1\le r\le q\) telescopes:

\[
 \boxed{
 \sum_{r=1}^{q}w_r
 ={q(a_0+1)\over a_0+q+1}.}
 \tag{6.3}
\]

This is \(O(1)\) for bounded \(a_0\), but is \(\Theta(s)\) when
\(a_0\asymp q\asymp s\).  It independently confirms the exact boundary
of the matrix method: separator projection removes the within-cell slow
mode, yet the diffuse sum over terminal block indices remains critical
for large initial cap.

This one-sided encoding contains \(O\) once.  It still does not construct
a disjoint four-kernel encoding of all remaining root bits, so (6.3) is a
carrier bound, not a proof of OCR.

## 7. Precise boundary

The synchronized-cell report is certified as an exact no-go for the
capped carrier relaxation.  It proves that:

\[
 \text{caps + shared literal word + separator parsing}
 \quad\not\Rightarrow\quad
 \Psi_s(1/2)=o(s).
\]

A successful coefficientwise OCR theorem must impose a further physical
condition which kills the invariant corner family or gives its actual
source/sink vectors vanishing invariant projection.  The remaining
statement must be proved after the four external one-crossing pieces are
fixed; otherwise the common outer carrier can be duplicated again.

No constant-one conclusion follows from this audit.
