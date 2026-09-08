# Audit of OCR: separator-spanning genuine returns and the synchronized Green boundary

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, or solver

## 0. Verdict

The proposed one-block outer-carrier reconstruction is false.  In
particular, the asserted localization

\[
 T_h=X1\overline {S_s}1Y
 \tag{0.1}
\]

need not exist.  This is not a bounded-rank defect.  For every
\(s\ge4\) and every \(k\ge1\) there is a genuine first zero-winding
return of duration \(s\) and semilength

\[
 m=s+4k
 \tag{0.2}
\]

for which

\[
 T_0=T_1=S_{s-1}=S_s=(1100)^k
 \tag{0.3}
\]

and all other \(T_j,S_j\) are empty.  Its mandatory copied word
\(0S_s0\) starts inside \(\overline T_1\), crosses the separator after
\(\overline T_1\), and ends inside \(\overline T_0\).  Since every
nonempty \(T_j\) has length \(4k\), while
\(1\overline {S_s}1\) has length \(4k+2\), (0.1) is impossible.
Taking \(k\asymp s^2\) places these counterexamples in any prescribed
fixed Gaussian height band.

The correct carrier relaxation is the synchronized two-parser automaton
of `MATH_ATTACK_OCR_SYNCHRONIZED_CELL_GREEN_NOGO_20260725.md`.  I audit
its rank, state, transition, source, and Green-mass calculations below.
They are correct.  In a full cell of unmatched height \(q\), the exact
critical endpoint transfer is

\[
 \frac1{q+2}
 \begin{pmatrix}q+1&1\\1&q+1\end{pmatrix},
 \tag{0.4}
\]

whose invariant and anti-invariant eigenvalues are respectively
\(1\) and \(q/(q+2)\).  The exact marked capped-carrier relaxation has
total critical source-to-sink mass \(\Theta(s)\), not \(o(s)\), even
though the common outer carrier is counted only once.  The source and
sink both have nonzero projection on the invariant mode.

Consequently the shared-boundary collision theorem, the two parser caps,
and separator chronology do not prove \((OCR_s)\).  The exact surviving
statement is an **actual-PBBS anti-corner theorem**: after the four
external one-crossing pieces are fixed, the actual chronology must give
\(o(s)\) total mass to the invariant-mode corner paths.  The genuine
family above disproves the one-block source representation, but, being
only one word for each \((s,k)\), does not disprove that sharper aggregate
projection statement.

## 1. An infinite genuine separator-spanning family

Put

\[
 X=(1100)^k,\qquad \overline X=(0011)^k.
 \tag{1.1}
\]

The elementary rotation identity

\[
 \boxed{\overline X00=00X}
 \tag{1.2}
\]

will be used twice.  Define

\[
 D_0=1^{s-2}(\overline X1)(\overline X1)0^s.
 \tag{1.3}
\]

### Theorem 1.1

For every \(s\ge4\) and \(k\ge1\), the word (1.3) starts a consecutive
zero-winding return of step-two duration \(s\).  Its exact orbit is

\[
 D_1=1^{s-1}\overline X1\overline X0^s,
 \tag{1.4}
\]

\[
 D_j=1^s0^{j-2}\overline X0\overline X0^{s-j+1}
 \quad(2\le j\le s-1),
 \tag{1.5}
\]

and

\[
 D_s=X1^s0^sX.
 \tag{1.6}
\]

Its first-maximum positions are

\[
 \delta(D_0)=s+8k,\qquad
 \delta(D_1)=s+4k,
 \tag{1.7}
\]

\[
 \delta(D_j)=s\ (2\le j\le s-1),
 \qquad \delta(D_s)=s+4k,
 \tag{1.8}
\]

and its first \(s\) deficits are

\[
 d(D_j)=1\quad(0\le j\le s-2),
 \qquad d(D_{s-1})=4k+1.
 \tag{1.9}
\]

#### Proof

In (1.3), both copies of \(\overline X\) are concatenations of
depth-two negative excursions.  The last displayed one is the first bit
which reaches height \(s\).  The subsequent word is \(0^s\).  Hence its
canonical block rotation is (1.4).

The first maximum of (1.4) is the displayed one between the two copies
of \(\overline X\).  A second block rotation gives (1.5) at \(j=2\).
For \(2\le j\le s-2\), the word after the initial mountain remains
positive until its last zero, and moving that last zero to the beginning
of the terminal corridor changes (1.5) at \(j\) into (1.5) at \(j+1\).

At \(j=s-1\), the first \(s-3\) zeros lower the path to height three;
the first \(\overline X\) stays between heights one and three; the next
separator lowers it to height two.  The first two zeros of the second
\(\overline X\) then give the first return to zero.  What follows that
return is

\[
 11(0011)^{k-1}00=X,
\]

by (1.2).  Thus the terminal suffix is \(X\), and the last block rotation
is

\[
 X1^s0^{s-2}\overline X00=X1^s0^sX,
\]

again by (1.2).  This proves (1.4)--(1.6).

The first-maximum positions in (1.7)--(1.8) are now read directly from
the displayed words.  All terminal suffixes before \(D_{s-1}\) are
empty, while the terminal suffix at \(D_{s-1}\) is \(X\); this proves
(1.9).  Therefore

\[
 \sum_{j=0}^{s-1}d(D_j)
 =(s-1)+(4k+1)=s+4k=\delta(D_s).
 \tag{1.10}
\]

For proper prefixes, the accumulated deficit is \(j\).  It is strictly
less than \(\delta(D_j)\): this is immediate at \(j=1\), and for
\(2\le j<s\) it is \(j<s\).  Hence the return is the first one and has
zero winding. \(\square\)

The length of (1.3) is \(2s+8k\), proving (0.2).  Its canonical suffix
data are

\[
 S_0=\cdots=S_{s-2}=\varnothing,qquad
 S_{s-1}=S_s=X.
 \tag{1.11}
\]

The dual drops

\[
 e_j=\delta(D_j)+d(D_j)-\delta(D_{j+1})
\]

are \(4k+1,4k+1,1,\ldots,1\).  The literal seam identities identify
the two nonempty dual words, giving

\[
 T_0=T_1=X,qquad T_2=\cdots=T_{s-1}=\varnothing.
 \tag{1.12}
\]

The height-two word \(X\) obeys both required caps because \(s\ge4\).

## 2. Exact carrier alignment and rank audit

For the family above,

\[
 \mathcal A=0^{s-2}\overline X0\overline X0,
 \qquad
 \mathcal C=0X0X0^{s-2},
 \tag{2.1}
\]

and

\[
 R_0=R_s=0^{s-1}.
 \tag{2.2}
\]

Write \(\overline X=00Y\).  Identity (1.2) is then exactly

\[
 X=Y00.
 \tag{2.3}
\]

Consequently

\[
 \mathcal A=0^{s-1}\underbrace{(0Y000Y0)}_{O},
 \qquad
 \mathcal C=\underbrace{(0Y000Y0)}_{O}0^{s-1}.
 \tag{2.4}
\]

Thus the common outer carrier is counted literally and has length
\(8k+1\).  Its mandatory prefix is

\[
 0S_s0=0X0=0Y000.
 \tag{2.5}
\]

In the \(\mathcal A\)-parsing, (2.5) consists of all of
\(\overline T_1\) except its first zero, then the separator following
\(\overline T_1\), then the first two zeros of \(\overline T_0\).
It therefore crosses a dual-block boundary.  Since

\[
 |1\overline {S_s}1|=4k+2>|T_0|=|T_1|=4k,
\]

no factorization (0.1) exists for any \(h\).

The endpoint excess is

\[
 \Lambda=\delta(D_0)+\delta(D_s)-2m=4k.
 \tag{2.6}
\]

Writing \(\ell=\Lambda/2=2k\), the independent rank identity checks
without slack:

\[
 \begin{aligned}
 s+\sum_{j=1}^{s-1}|S_j|_e
  +\sum_{j=0}^{s-1}|T_j|_e-\ell
 &=s+2k+4k-2k\\
 &=s+4k=m.
 \end{aligned}
 \tag{2.7}
\]

For any prescribed \(\rho>0\), choosing
\(k=\lfloor s^2/(4\rho^2)\rfloor\) gives

\[
 \frac{s}{\sqrt m}\longrightarrow\rho.
 \tag{2.8}
\]

Hence the separator-spanning failure occurs in every fixed Gaussian band
whose interior contains \(\rho\).

## 3. A true balanced-word estimate which does not repair the parsing

Let \(N_{\ell,h}\) be the number of balanced binary words of length
\(2\ell\) whose running net height has minimum exactly \(-h\).  Reflection
gives

\[
 \begin{aligned}
 N_{\ell,h}
 &=\binom{2\ell}{\ell+h}-\binom{2\ell}{\ell+h+1}\\
 &=\frac{2h+1}{\ell+h+1}\binom{2\ell}{\ell+h}.
 \end{aligned}
 \tag{3.1}
\]

It follows coefficientwise at the counting level that

\[
 \boxed{
 \sum_{h=0}^{\ell}\frac{N_{\ell,h}}{h+3}
 \le \frac{2}{\ell}\sum_{h=0}^{\ell}
       \binom{2\ell}{\ell+h}
 \le \frac{2\,4^\ell}{\ell}.}
 \tag{3.2}
\]

Thus the proposed record-depth average is valid.  What fails is its
attachment to a disjoint local \(T_h\)-piece.  In the family of Section 1
the common boundary has a perfectly well-defined record depth, but its
mandatory copied segment crosses the \(T_1/T_0\) separator.  Charging a
first-passage factor to one \(T_h\) therefore either omits part of the
carrier or counts bits already present in the synchronized crossing
kernel.  Estimate (3.2) cannot be multiplied by the four-strip kernel
without a two-parser injection.

## 4. Independent audit of the synchronized state

The dual staircase gives

\[
 |\mathcal A|=\sum_{j=0}^{s-1}(|T_j|+1)=\delta(D_0).
 \tag{4.1}
\]

Since \(S_0=\varnothing\) and
\(D_0=P_01R_00\),

\[
 |R_0|=2m-\delta(D_0)-1.
\]

Therefore

\[
 \boxed{|\mathcal A R_0|=2m-1.}
 \tag{4.2}
\]

Changing the \(s\) dual separators in \(\mathcal A\) from zero to one
reconstructs \(P_01\), and appending the last zero reconstructs \(D_0\).
Thus

\[
 W:=\mathcal A R_0=R_sOR_0=R_s\mathcal C
 \tag{4.3}
\]

is a length-preserving encoding with exactly one copy of \(O\).

Suppose a common position lies in \(S_p\) in the forward parsing and in
\(\overline T_j\) in the dual parsing.  Let \(c\) be its height inside
\(S_p\), and \(t\) its depth inside \(\overline T_j\).  The two absolute
heights in (4.3) are equal, so

\[
 p-1+c=s+j-t.
\]

Equivalently,

\[
 \boxed{t+c=q,qquad q=s+j-p+1.}
 \tag{4.4}
\]

The caps give the exact cell interval

\[
 \max(0,q-p)\le t\le\min(q,s-1-j).
 \tag{4.5}
\]

Consuming a dual separator sends

\[
 (p,j,q)\mapsto(p,j-1,q-1),
 \tag{4.6}
\]

while consuming a forward separator sends

\[
 (p,j,q)\mapsto(p-1,j,q+1).
 \tag{4.7}
\]

Thus \((j,q)\) is the exact block state, with
\(p=s+j-q+1\).  Every transition decreases \(p+j\), so the marked
automaton is finite and acyclic.  Equations (4.2), (4.4), and
(4.5)--(4.7) certify respectively the rank, synchronization, caps, and
uniqueness accounting.

## 5. The critical cell and the exact slow projection

In a full cell the internal coordinate is the path
\(0,1,\ldots,q\).  Cramer's rule gives its endpoint resolvent

\[
 \mathbf G_q(x)=\frac1{F_{q+1}(x^2)}
 \begin{pmatrix}F_q(x^2)&x^q\\x^q&F_q(x^2)\end{pmatrix}.
 \tag{5.1}
\]

The next marked separator contributes \(x\).  Since

\[
 F_r(1/4)=\frac{r+1}{2^r},
\]

one obtains (0.4).  Hence

\[
 \mathbf P_q(1,1)^T=(1,1)^T,
 \qquad
 \mathbf P_q(1,-1)^T=\frac q{q+2}(1,-1)^T.
 \tag{5.2}
\]

If the overlap starts in \(\overline T_h\), its initial forward
separator leaves \(q=h+1\).  The prefix of \(T_h\) preceding that bit is
an arbitrary confined walk from zero to \(h\), not a first-passage word.
With \(H=s-1-h\), its resolvent entry is

\[
 B_{H,h}(x)=\frac{x^hF_{H-h}(x^2)}{F_{H+1}(x^2)}.
 \tag{5.3}
\]

Including the displayed zero gives exactly

\[
 \boxed{xB_{H,h}(x)\big|_{x=1/2}
       =\frac{s-2h}{s-h+1}.}
 \tag{5.4}
\]

This is bounded away from zero for
\(h\le(1/2-\varepsilon)s\).  The source is one endpoint vector and the
terminal sink is the other; each has scalar product \(1/\sqrt2\) with
the normalized invariant vector.  There is therefore no source or sink
orthogonality to the unit mode.

For completeness, choose

\[
 s/10\le h,L\le s/8.
\]

Starting at the forward endpoint of the \(h\)-cell, make \(L\) same-side
forward exits, one crossing, and then \(h\) same-side dual exits.  All
visited cells satisfy (4.5).  With

\[
 a_q=\frac{q+1}{q+2},\qquad b_q=\frac1{q+2},
\]

the exact path weight is

\[
 \begin{aligned}
 w_{h,L}
 &=\left(\prod_{q=h+1}^{h+L}a_q\right)
   b_{h+1+L}
   \left(\prod_{q=L+1}^{h+L}a_q\right)\\
 &=\frac{(h+2)(L+2)}
        {(h+L+2)^2(h+L+3)}
 =\Theta(1/s).
 \end{aligned}
 \tag{5.5}
\]

There are \(\Theta(s)\) admissible \(L\)'s for each of
\(\Theta(s)\) source blocks \(h\).  Thus these paths have total marked
mass \(\Omega(s)\).  Conversely every full-cell matrix is stochastic,
every truncated cell is substochastic, and \(p+j\) decreases at every
separator.  First-arrival mass from any fixed source is at most one, and
there are at most \(s\) sources.  Hence the total mass is \(O(s)\).

This proves

\[
 \boxed{\mathcal G_s^{F\to D}=\Theta(s).}
 \tag{5.6}
\]

## 6. Exact remaining theorem

Let \(\alpha_s\) and \(\beta_s\) be the actual PBBS source and sink
vectors after the four external one-crossing pieces have been fixed, and
let \(\mathsf M_s(x)\) be the synchronized killed-cell transition matrix.
The residual series is the projected renewal

\[
 \Psi_s(x)=\beta_s^{\!*}(I-\mathsf M_s(x))^{-1}\alpha_s.
 \tag{6.1}
\]

The capped marked relaxation has \(\Psi_s(1/2)=\Theta(s)\).  Therefore
the exact sufficient PBBS statement is

\[
 \boxed{
 \beta_s^{\!*}(I-\mathsf M_s(1/2))^{-1}\alpha_s=o(s),}
 \tag{6.2}
\]

where \(\alpha_s,\beta_s\) retain the complete inter-time
\(\tau\)-chronology.  Equivalently, actual chronology must suppress the
corner family (5.5), or give vanishing aggregate projection on the
invariant cell mode.  Neither the common-boundary collision estimate nor
the scalar caps imply (6.2).

No coefficient-one conclusion follows from the present audit.
