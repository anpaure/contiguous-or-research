# Audit of the zero-winding trace-completion obstruction

Date: 2026-07-25

Pure mathematics only. No computation, finite search, solver, or external
input is used.

Audited file:
MATH_ATTACK_K_ZERO_WINDING_TRACE_COMPLETION_OBSTRUCTION_20260725.md.

## Verdict

**Pass after limited but important patches.**

The common-carrier overlap theorem, the overlap-one dynamic construction,
canonicality of every displayed factorization, the exact \(\tau\)-recursion,
injectivity, both formulas for \(K_s\), the Boltzmann mean and macroscopic
window, the diagonal coefficient averaging, and the short-cycle subtraction
are correct.

The audit patched:

- a typographical error in the Boltzmann mass;
- the missing semilength ledger behind the coefficient formula;
- explicit disjointness of the families for different first-return lengths;
- the common integer interval used in the diagonal averaging;
- the implication scope, so chronology is the remaining gain only within
  an \(RP_A\)-based proof, while global literal fusion remains a separate
  fallback; and
- one malformed net-height notation.

There is no hidden parity loss and no uncharged short-cycle term.

## 1. Mandatory overlap

Let

\[
 A=(\overline T_{s-1}0)\cdots(\overline T_00),
 \qquad
 C=(0S_s)(0S_{s-1})\cdots(0S_1).
\]

The dual-tail identity gives one common carrier

\[
 Z=AR_0=R_sC.
\]

Since

\[
 |A|=\delta(D_0),\qquad
 D_0=P_01R_00,\qquad S_0=\varnothing,
\]

one has \(|Z|=2r-1\). The terminal decomposition gives the same length from
\(|R_s|+|C|\).

Each block of \(A\) and \(C\) has net \(-1\), so both have net \(-s\).
If they were disjoint, \(Z=AUC\) and \(R_0=UC\). But

\[
 \operatorname{net}(R_0)=1-s
\]

would force \(\operatorname{net}(U)=1\). As \(U\) is a prefix of the tail
read immediately after the first global maximum, it would rise above that
maximum. This is impossible.

For overlap \(O\),

\[
 A=R_sO,\qquad C=OR_0.
\]

Since \(\operatorname{net}(R_s)=1-s\),

\[
 \operatorname{net}(O)=-s-(1-s)=-1.
\]

Hence \(|O|\) is positive and odd. The proof uses literal carrier order,
not an entropy heuristic.

## 2. Canonical overlap-one construction

The symmetric caps are exactly the two inequalities needed at each side:

\[
 \operatorname{ht}(S_j)\le\min(j,s-j),
 \qquad
 \operatorname{ht}(T_h)\le\min(h,s-1-h).
\]

For

\[
 Q_h=(S_{h-1}1)\cdots(S_01),
\]

the block \(S_j\) begins after \(h-1-j\) earlier separators and cannot
reach height \(h\); the last separator first reaches height \(h\).

In

\[
 V_h=(\overline T_{s-1}1)\cdots(\overline T_h1),
\]

the block \(\overline T_j\) descends by at most \(s-1-j\), the number of
earlier upward separators in \(V_h\). Thus
\(P_h1=Q_hV_h\) first reaches height \(s\) at its last bit.

Reading \(R_h\) from height \(s\):

- in its initial \(T\)-part, \(\overline T_j\) begins at height at least
  \(j+1\) and descends by at most \(j\);
- after that part the height is \(s-h\);
- in the \(S\)-part, \(0S_j\) is based at height \(j-h\ge1\), and its
  height cap keeps it at or below \(s\).

The tail ends at height one. Therefore the displayed zero is the first
subsequent return to zero. The suffix \(S_h\) is Dyck and never exceeds the
already attained height. Every factorization in the construction is
canonical.

The two literal identities

\[
 S_h1P_h=P_{h+1}1\overline T_h,
\qquad
 \overline T_h0R_h=R_{h+1}0S_{h+1}
\]

give

\[
 \tau D_h=D_{h+1}
\]

without a static-spine assumption.

Moreover,

\[
 \sum_{h<s}(|S_h|+1)=|P_s1|=\delta(D_s),
\]

so the return is zero winding. The strict first-passage theorem excludes
every earlier odd return; positivity below \(N\) excludes an earlier even
return. Finally,

\[
 A=R_s0,\qquad C=0R_0,
\]

so the overlap is exactly the single zero.

## 3. Enumeration and \(K_s\)

The canonical dynamics recover every \(S_h\) from \(\tau^hD_0\), and then
recover \(T_h\) from

\[
 S_h1P_h=P_{h+1}1\overline T_h.
\]

Thus the tuple map is injective. Direct length accounting gives

\[
 r=s+\sum_{j=1}^{s-1}|S_j|_{\rm e}
      +\sum_{h=0}^{s-1}|T_h|_{\rm e},
\]

so

\[
 Z_{r,s}^{(1)}=[z^{r-s}]G_s(z).
\]

Different values of \(s\) also give disjoint root families, because every
constructed root has first return gap \(2s+1\).

At \(z=1/4\), write

\[
 f_j={j+1\over j+2},\qquad C_j(1/4)=2f_j.
\]

There are \(2s-1\) Catalan factors, so the fixed separator term contributes
an overall factor \(1/2\) after multiplication by \(4^{-s}\).

For \(s=2t\), the cap multiplicities give

\[
 K_{2t}
 ={1\over2}f_0^2
   \left(\prod_{j=1}^{t-1}f_j\right)^4f_t
 ={2\over(t+1)^3(t+2)}.
\]

For \(s=2t+1\),

\[
 K_{2t+1}
 ={1\over2}f_0^2
   \left(\prod_{j=1}^{t-1}f_j\right)^4f_t^3
 ={2\over(t+1)(t+2)^3}.
\]

Hence \(K_s\asymp s^{-4}\), with no parity-dependent loss beyond the
displayed constants.

## 4. Boltzmann window

For one height cap,

\[
 \Pr(X_j=n)
 ={[z^n]C_j(z)\,4^{-n}\over C_j(1/4)}.
\]

Independent multiplication gives exactly

\[
 Z_{r,s}^{(1)}
 =4^rK_s\Pr(Y_s=r-s).
\]

Logarithmic differentiation of

\[
 C_j(z)=(1-zC_{j-1}(z))^{-1}
\]

at \(1/4\) yields

\[
 \mu_j={j\over j+2}(1+\mu_{j-1}),\qquad\mu_0=0,
\]

and therefore

\[
 \mathbb E X_j={j\over3}.
\]

The sum of the caps in \(G_s\) is \(\Theta(s^2)\), proving
\(\mathbb EY_s=\Theta(s^2)\).

For each of \(\Theta(s)\) factors with
\(s/4\le j\le s/2\), the \(q=1\) spectral term gives uniformly for
\(\alpha s^2\le n\le\beta s^2\)

\[
 [z^n]C_j(z)\ge c\,{4^n\over s^3}.
\]

There are \(\Theta(s^2)\) such integers \(n\), so one factor lands in that
macroscopic interval with probability \(\Omega(1/s)\). Independence across
\(\Theta(s)\) factors makes the probability that at least one does so
bounded below by a positive constant. Markov's inequality, using the mean
bound, supplies a constant upper cutoff. Thus

\[
 \Pr(a_0s^2\le Y_s\le b_0s^2)\ge c_0.
\]

No local limit theorem is used.

## 5. Diagonal averaging and short cycles

For \(S\le s\le2S\), define the common integer interval

\[
 I_S=
 [\,\lfloor a_0S^2+S\rfloor,\,
    \lceil4b_0S^2+2S\rceil\,]\cap\mathbb Z.
\]

Every event
\[
 a_0s^2\le Y_s\le b_0s^2
\]
maps into \(I_S\) after setting \(r=Y_s+s\). Hence

\[
 \sum_{s=S}^{2S}\sum_{r\in I_S}
 \Pr(Y_s=r-s)\ge c_0S.
\]

Since \(|I_S|=O(S^2)\), some \(r=r(S)\asymp S^2\) satisfies

\[
 \sum_{s=S}^{2S}\Pr(Y_s=r-s)\ge {c\over S}.
\]

Together with \(K_s\ge c/S^4\), this gives

\[
 \sum_{s=S}^{2S}Z_{r,s}^{(1)}
 \ge c\,{4^r\over S^5}.
\]

Wallis gives

\[
 {\operatorname{Cat}_r\over2r+1}
 \asymp {4^r\over r^{5/2}}
 \asymp {4^r\over S^5}.
\]

Because \(r\asymp S^2\), fixed constants \(a,b\) place every
\(s\in[S,2S]\) inside \([a\sqrt r,b\sqrt r]\). Letting \(S\to\infty\)
forces \(r(S)\to\infty\), so infinitely many ranks result.

There is no lattice parity restriction: \(z\) records Dyck semilength, and
every nonnegative integer \(r-s\) is an admissible coefficient index.

Choose the short-cycle cutoff larger than \(b\sqrt r+2\), the maximum
quotient interval length in this band. The standard itinerary estimate
removes at most

\[
 \exp(O(\sqrt r\log r))=\exp(o(r))
\]

quotient roots. The lower bound is
\[
 \operatorname{Cat}_r/(2r+1)
 =\exp(r\log4-O(\log r)),
\]
so short-cycle deletion preserves a constant fraction of the lower bound.

## 6. Implication scope

The theorem proves \(\Omega(B/N)\) actual zero-winding starts on an infinite
subsequence, for a fixed Gaussian band. Therefore a universal
terminal-completion estimate asserting \(o(B/N)\) such starts is false.
For any fixed \(A>b\), the constructed band lies within the \(H_A\) window
for all large ranks on that subsequence.

It does not prove an \(\Omega(B/N)\) edge-disjoint quotient packing. Greedy
selection can lose \(O(\sqrt r)\), and stronger clustering is not excluded.
Thus \(RP_A\) remains open.

Within a proof that continues through \(RP_A\), the remaining possible gain
must use trace chronology, Pascal-slot dispersion, or another mechanism
which acts after interval overlap is imposed. A global owner-injective
literal fusion may instead bypass \(RP_A\). Neither constant one nor a
global fusion is proved or refuted here.
