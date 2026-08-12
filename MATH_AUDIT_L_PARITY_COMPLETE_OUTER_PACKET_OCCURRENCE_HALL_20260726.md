# Independent audit of the parity-complete outer occurrence Hall report

Date: 2026-07-26

Audited source:
`MATH_ATTACK_L_PARITY_COMPLETE_OUTER_PACKET_OCCURRENCE_HALL_20260726.md`.

Method: pure mathematics only.

## 0. Verdict

The outer suffix Hall theorem is correct. The coupled LP, histogram capacity
bound, factor-two exceptional ledger, Gaussian normalization, explicit
constant

\[
 \delta_A=e^{-A^2}\Phi(-A\sqrt{2/3})
          -\Phi(-2A\sqrt{2/3})>0,
\]

and constant-one consequence all check.

Four scope/wording corrections are required:

1. Cross-cell physical separation of all \(6^r\) completed-carrier cells is
   not part of the proved local parity-complete gate. It may be granted as an
   additional conditional hypothesis, but the report must not attribute it
   to the local trace code. The suffix obstruction needs no intra- or
   cross-cell injectivity.
2. The LP coefficient \(A_{P,\theta,q}^\epsilon(T)\in\{0,1\}\) is the
   binary set-cover incidence “state \(\theta\) emits \(T\) at least once”
   whether or not traces are injective. Replace the statement that trace
   injectivity makes it a binary indicator. If occurrence multiplicities are
   used instead, denote them by an integer coefficient; this only enlarges
   the relaxed capacity and the suffix occurrence bound still applies.
3. The raw four-block theorem with exceptional term \(U_m\) permits only
   owner-preserving states of the fixed support \(\mathcal A^r\). If
   “arbitrary trace-coded seed” includes states importing owners from the
   other two \(B_4\) supports, replace \(U_m\) by the audited envelope
   \[
      U_{\rm eff}=U_m^{\rm leave}+(3/2)^rU_m^{\rm bad}.
   \]
   The completed \(\mathcal V^r\) carrier needs no such correction because
   its shores resolve one common owner set.
4. Restrict the claim in item 7.6 to the specifically audited replicated
   \(Q_4\) braid bank. The estimate \(O(qW/h)\) is not proved for every
   possible parity-complete braid/state library and is unnecessary for the
   suffix theorem.

One optional proof addition is needed if (6.9) is retained: convergence of
the positive-part histogram sum requires a uniform local hypergeometric CLT
plus a tail domination argument. The CDF limits (6.3)--(6.4) alone prove the
tail dual and all main conclusions, but do not by themselves prove (6.9).

## 1. Local trace and face claims

One parity-complete lifted factor has \(4^r\) phase starts, not a separate
supply on each parity shore. This normalization is correct. Likewise, a
completed carrier has \(6^r4^r=24^r\) owner starts; the cells partition this
capacity.

For the physical pair-preserving cube automorphism group

\[
 \mathbb F_2^{2r}\rtimes(S_2\wr S_r),
\]

the type-\(c\) face count

\[
 2^{2r-q}\binom rc\binom{r-c}{q-2c}2^{q-2c}
\]

is correct. In a paired direction word, an odd \((2t+1)\)-window contains
exactly \(t\) completed pairs, while an even \(2t\)-window contains \(t\)
or \(t-1\) according to boundary parity. Thus (2.4)--(2.7) are correct under
the explicitly conditional trace-injectivity hypothesis.

The finite check \(r=4,q=4,c=2\) is also correct:

\[
 M_{4,2}=128>96=N_{4,4,2}.
\]

It shows that the finite double-factor seed cannot already possess the full
all-depth trace gate. The report appropriately treats the growing trace-code
family as granted, not proved.

The phrase “full trace-code gate includes cross-cell physical separation”
should instead read:

> Even if one additionally grants cross-cell physical separation among all
> \(6^r\) completed-carrier cells, the outer theorem applies. If separation
> fails, distinct-target support only decreases.

## 2. LP and fractional language

The all-depth, coupled two-sign primal (3.2) and dual (3.4) are exact. The
same packet state variable is used at every rank and sign, and singleton
columns give precisely the caps \(0\le y\le1\).

The report correctly defines fractional uncovered mass by

\[
 D_q^\epsilon=\sum_T(1-\ell_q^\epsilon(T))_+.
\]

No correction to the fractional conclusion is needed. For integral loads,
this is exactly the hole count.

Injectivity is irrelevant to the definition of the binary set-cover matrix:

\[
 A_{P,\theta,q}^\epsilon(T)
 =\mathbf1_{\{T\text{ occurs at least once in state }\theta\}}.
\]

If a noninjective state emits \(T\) several times, the binary coefficient
remains one. The occurrence proof may pessimistically count all
multiplicities; because this gives an upper bound on distinct coverage, the
Hall lower bound remains valid.

## 3. Exceptional and suffix-class capacities

For every normal component, one phase owner in suffix class \(z\) produces
one lower and one upper occurrence in that same class. Exact owner weight
therefore bounds each signed load in class \(z\) by \(B_z\). This proves

\[
 \sum_z[(L_z-B_z)_++(U_z-B_z)_+]
\]

before exceptional restoration.

One exceptional weighted owner occurrence can contribute at most one target
per sign. Hence the losses \(-U_m\) separately and \(-2U_m\) jointly are
correct. For owner-importing raw mixed-seed components, the same proof uses
\(U_{\rm eff}\) instead.

The two-tail dual (5.6) is also exact. Its lower and upper owner events are
complementary tails of equal size \(B_{\le a}\); each sign has its own one
occurrence per owner ledger, giving combined capacity \(2B_{\le a}\), not
\(B_{\le a}\) and not \(4B_{\le a}\).

## 4. Explicit Gaussian constant

With

\[
 v=3/32,qquad d=A\sqrt{2/3},qquad
 a=s/2-2d\sqrt{vm}+O(1),
\]

the middle standardized threshold is \(-2d\). The lower target suffix mean
is shifted down by \(A\sqrt m/4=d\sqrt{vm}\), so its standardized threshold
is \(-d\). The upper statement is complementary. Therefore

\[
 B_{\le a}/W\to\Phi(-2d),
 \qquad
 |\mathcal Z_{q,a}^\pm|/W\to e^{-A^2}\Phi(-d).
\]

Positivity is proved exactly as written. Since \(A^2=3d^2/2\),

\[
 \log\frac{e^{-A^2}\phi(x+d)}{\phi(x)}
 =-d(x+2d)>0\qquad(x<-2d).
\]

Integrating proves \(\delta_A>0\) for every fixed \(A>0\).

The claim that \(-2d\) is the unique density crossing is correct. To turn it
into the positive-part limit (6.9), add a uniform local CLT on
\(|z-s/2|\le K\sqrt m\), then let \(K\to\infty\) using hypergeometric
Chernoff tails.

## 5. Constant-one implication and escape boundary

The coefficient-one conclusion is correctly scoped. A fixed Gaussian depth
has \(\Omega_A(W)\) holes. An additional \(o(W/h)\) strips supply at most
\(o(W)\) occurrences because each contributes \(2h\) per sign. Singleton
repair costs \(\Omega_A(W)\).

This disproves only the fixed exact-owner packet architecture. The listed
escapes—moving atlases, physical suffix transitions, cross-fibre splices, or
unrestricted SCI owner recycling—are necessary categories, not claimed
sufficient. That boundary is correct.
