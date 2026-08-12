# Audit of Mathematical Attack D: sparse Boolean-\(E_2\) stability

Date: 2026-07-24

## Verdict

**PASS, with two minor domain/wording repairs.**

I independently checked the harmonic representation, the exact slice moments,
the fourth-moment argument, the Boolean skew separation, the rounding lemma,
and the conversion to the component-noise ledger.  I found no counterexample
and no defect in the claimed cutoff

\[
\theta_* = \frac{3-\sqrt6}{6}.
\]

The proof really does establish a uniform positive
\(E_1\oplus E_{\ge3}\) projection gap on every compact density interval
\(I\subset(0,\theta_*)\), uniformly throughout a fixed central
\(O(\sqrt n)\) rank window.  Its application really does force

\[
R_H-4(n-1)B_H=\Omega_A(nW\sqrt m)
\]

at every global minimizer of the same fixed Gaussian-window objective.  Thus
the proposed near-baseline gate
\(R_H\le 4(n-1)B_H+o(nW)\) is impossible in that setting.

The two recommended source repairs are:

1. In Sections 2--4, explicitly impose the nondegenerate slice range
   \(2\le r\le n-2\) (or simply the central range used later).  Without this
   qualification the representation in Lemma 3.1 is not injective at a
   degenerate slice, because its norm coefficient vanishes.  This does not
   affect any application in the note.
2. In Section 2, write the Johnson decomposition as
   \(E_0\oplus\cdots\oplus E_{\min(r,n-r)}\), unless the standing convention
   \(r\le n/2\) is declared.  Again, every rank used in Section 10 satisfies
   \(r<n/2\).

These are scope corrections only; no constant or conclusion changes.

## 1. Harmonic-matrix representation

For a symmetric zero-diagonal matrix \(A=(a_{ij})\), the row-sum map on the
edge space of \(K_n\) has rank \(n\) over \(\mathbb R\) for \(n\ge3\).  Hence

\[
\dim\{A:A\mathbf1=0\}=\binom n2-n=\dim E_2.
\]

If

\[
h(S)=\sum_{i<j}a_{ij}\mathbf1_{\{i,j\}\subseteq S},
\]

then the zero row sums imply both \(\sum_{i<j}a_{ij}=0\) and orthogonality to
every coordinate indicator.  The positive second-moment formula gives
injectivity whenever \(2\le r\le n-2\).  Thus Lemma 3.1 is correct in its
intended central range.

## 2. Exact second and third moments

Writing \(Y_i=X_i-x\), the harmonicity identity is exact:

\[
\sum_{i<j}a_{ij}X_iX_j=\sum_{i<j}a_{ij}Y_iY_j.
\]

In the second moment, only a repeated edge survives.  In the third moment,
the only multigraphs with no degree-one vertex are a triply repeated edge and
a triangle.  This gives exactly

\[
\mathbb Eh^2=(\pi_2-2\pi_3+\pi_4)S_2
\]

and

\[
\mathbb Eh^3=
(\pi_2-6\pi_3+13\pi_4-12\pi_5+4\pi_6)C_3
+(\pi_3-3\pi_4+3\pi_5-\pi_6)T_3.
\]

The two factorizations were also checked directly:

\[
\alpha_{n,r}=\frac{(r)_2(n-r)_2}{(n)_4},
\qquad
b_{n,r}=\frac{(r)_3(n-r)_3}{(n)_6}.
\]

Conditioning after forcing two selected and two unselected coordinates gives

\[
\frac{a_{n,r}}{\alpha_{n,r}}
=\frac{(n-2r)^2-(n-4)}{(n-4)(n-5)},
\]

so (4.9) is correct as well.

## 3. The sharp skew comparison

The coefficient bounds

\[
|C_3|\le S_2^{3/2},
\qquad
|T_3|\le (2S_2)^{3/2}
\]

follow respectively from \(\ell_3\le\ell_2\) for the edge coefficients and
for the eigenvalues of the real symmetric matrix \(A\).  Uniformly when
\(|r-n/2|=O(\sqrt n)\),

\[
\alpha_{n,r}=\frac1{16}+O(n^{-1}),\qquad
b_{n,r}=\frac1{64}+O(n^{-1}),\qquad
a_{n,r}=O(n^{-1}).
\]

Therefore

\[
\frac{|\mathbb Eh^3|}{(\mathbb Eh^2)^{3/2}}
\le 2\sqrt2+O(n^{-1}).
\]

There is no hidden small-influence assumption.  Concentrated matrices are
already covered by the two elementary norm inequalities.

For a centered Boolean indicator of density \(\theta\), the standardized
third moment is

\[
\frac{1-2\theta}{\sqrt{\theta(1-\theta)}}.
\]

It exceeds \(2\sqrt2\) exactly when

\[
(1-2\theta)^2>8\theta(1-\theta),
\]

whose lower root is

\[
\theta_*=\frac{3-\sqrt6}{6}.
\]

Thus the threshold and its strict endpoint convention are correct.  No
claim is made at \(\theta=0\) or \(\theta=\theta_*\), and compactness away
from those endpoints is genuinely needed.

## 4. Fourth moment and stability conversion

The fourth-moment proof is valid.  After grouping the expansion by endpoint
equality patterns and applying partition-lattice Mobius inversion, every
nonzero unrestricted quotient multigraph has minimum degree at least two.
With four edges, its nontrivial components reduce to the five types listed
in the source.  Each homomorphism sum is bounded by
\((\sum_{ij}a_{ij}^2)^2\).  The number of patterns and all Mobius
coefficients are absolute constants, and the central-slice coefficient
\(\alpha_{n,r}\) is bounded below.  Hence

\[
\mathbb Eh^4\le K(\mathbb Eh^2)^2
\]

with an absolute \(K\).

For \(g=\mathbf1_{\mathcal B}-\theta\), \(h=P_{E_2}g\), and \(u=g-h\),
the cubic transfer estimate is also sound:

\[
|\mathbb Eg^3-\mathbb Eh^3|
\le \sqrt{\mathbb Eu^2}\,
(\|g^2\|_2+\|gh\|_2+\|h^2\|_2).
\]

Here

\[
\|g^2\|_2\le\sqrt{\theta(1-\theta)},\quad
\|gh\|_2\le\sqrt{\mathbb Eh^2},\quad
\|h^2\|_2\le\sqrt K\,\mathbb Eh^2.
\]

This yields a uniform \(O(\sqrt\delta)\) error, where
\(\delta=\|P_{E_1\oplus E_{\ge3}}g\|_{2,\mathrm{prob}}^2\).  The strict
skew gap on a compact \(I\subset(0,\theta_*)\) then gives exactly the
positive constant asserted in (7.7).  There is no missing control of the
residual fourth moment.

## 5. Integer rounding audit

For the pointwise adjacent-integer rounding \(b\),

\[
(\mu(S)-b(S))^2
\le (\mu(S)-c)(\mu(S)-c-1)
\]

holds on both sides of the interval \(\{c,c+1\}\).  The mass discrepancy
obeys

\[
\Delta\le\sqrt{N\mathcal E}.
\]

There are always at least \(\Delta\) entries available to flip in the
required direction, because the desired number of upper entries is
\(\theta N=W-cN\).  Consequently

\[
\|\mu-(c\mathbf1+\mathbf1_{\mathcal B})\|_2^2
\le2\mathcal E+2\sqrt{N\mathcal E}
\]

is correct.  The convention that \(\mathcal E\) is the full floor energy,
twice the pair-collision excess, is consistent with both comparison notes.

## 6. Gate conversion and scale

For a fixed \(A>0\), one may choose fixed

\[
0<u<v<\min\{A,\sqrt{\log(17/16)}\}.
\]

At every integer depth in \([u\sqrt m,v\sqrt m]\),

\[
\lambda_q=e^{q^2/m+o(1)},\qquad c_q=1,
\]

and \(\theta_q=\lambda_q-1\) lies in a fixed compact subinterval of
\((0,1/16)\).  This avoids both the zero-density endpoint and the
\(1/16\) endpoint uniformly.  Also \(N_q=\Theta_{u,v}(W)\).

The projection triangle inequality and the rounding lemma give

\[
\varepsilon_I N_q
\le2\mathcal H_q+4\mathcal E_q
+4\sqrt{N_q\mathcal E_q}.
\]

The stated dichotomy follows with room to spare:

\[
\mathcal H_q\ge\frac{\varepsilon_I}{4}N_q
\quad\text{or}\quad
\mathcal E_q\ge\frac{\varepsilon_I^2}{256}N_q.
\]

At a global minimizer, the audited three-slack identity gives

\[
R_H-4(n-1)B_H
\ge4(n-1)\sum_q\frac{\mathcal E_q}{c_q}
+2\sum_q\frac1{c_q}\sum_{j\ge3}
(j-2)(n-j-1)\|f_q^{(j)}\|_2^2.
\]

Since \(j\le r_q\le m\),

\[
(j-2)(n-j-1)\ge n-4\qquad(j\ge3).
\]

Thus each of the \(\Theta(\sqrt m)\) selected depths contributes
\(\Omega_I(nW)\), independently of which side of the dichotomy holds.
Summing proves

\[
R_H-4(n-1)B_H=\Omega_A(nW\sqrt m).
\]

The normalization agrees exactly with both
`GLOBAL_COMPONENT_NOISE_GATE_NO_GO_20260724.md` and
`COMPONENT_NOISE_OVERLAP_IDENTITY_20260724.md`: \(R_H\) is the unscaled
sum over unordered transpositions, the first admissible harmonic is
\(E_2\), and its coefficient is \(4(n-1)\), not \(2n\).

## 7. Counterexample and nonuniformity checks

The following possible failure modes were checked and do not apply:

* **Sparse endpoint:** the theorem excludes \(\theta\to0\); the gate uses a
  fixed positive \(u\), so its density interval remains compactly away from
  zero.
* **Cutoff endpoint:** the proof uses
  \(v<\sqrt{\log(17/16)}\), so it does not rely on a statement at density
  \(1/16\).
* **Integer crossings:** the selected subwindow lies wholly in \(1<\lambda<
  17/16\), so \(c_q=1\) throughout and no floor crossing occurs.
* **Concentrated quadratic forms:** the skew and fourth-moment estimates are
  uniform in the matrix coefficients.
* **Residual \(E_1\):** Boolean rounding can create an \(E_1\) part, but the
  stability theorem controls \(E_1\oplus E_{\ge3}\), and the full rounding
  error bounds that projection.
* **Wrong factor:** nonnegativity of the switching slack is used only at a
  global minimizer of the same \(H\)-window objective, exactly as required
  by the three-slack ledger.

## Final audit status

After the two harmless domain clarifications above, the source theorem is
ready to merge.  In particular, the formerly open Sparse Boolean-\(E_2\)
stability problem from the component-noise no-go note is resolved, and the
corrected near-baseline component-noise route is rigorously ruled out on
every fixed nonzero Gaussian window.  This is a no-go result for that
sufficient gate only; it does not disprove MWB or the contiguous-OR
conjecture.
