# Audit of the reflected-chart Haar block and a three-reflection Johnson frame

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or probabilistic experiment is used. Random signs denote finite
averages of literal integral exact factors.

## 0. Verdict

The reflected-chart construction in
`MATH_ATTACK_C_REFLECTED_CHART_HAAR_CONTRACTION_20260725.md` is valid after
one reachability wording correction: every corner uses at most two fresh
cuts, while the extracted decreasing mixed corner uses exactly two nonempty
proper cuts. The empty corner does not use two proper cuts. Its Haar identity
retains the integer floor exactly, and its quantitative
bounds

\[
 A_{\rm bun}>
 \frac{B4^H}{128M_AH^4},
 \qquad
 V_{\rm bun}<32HB
 \tag{0.1}
\]

are correct. Thus

\[
 \frac{V_{\rm bun}}{A_{\rm bun}}
 <\frac{4096M_AH^5}{4^H}=o_A(1),
 \tag{0.2}
\]

and the claimed strict full-floor-energy decrease follows.

There is one notational point worth making explicit. The correlated bundle
variance and the ordinary direct-overlay component variance are different:

\[
 V_{\rm bun}
 =\sum_R\|d_R-\sigma d_R\|_H^2<32HB,
 \tag{0.3}
\]

whereas the direct \(F^*/\sigma F^*\) overlay has two components per
selected \(R\), and therefore

\[
 V_{\rm dir}
 =\sum_R\bigl(\|d_R\|_H^2+\|\sigma d_R\|_H^2\bigr)
 =2\sum_R\|d_R\|_H^2<16HB.
 \tag{0.4}
\]

Both high-harmonic variances are \(o(A_{\rm bun})\). Equation (0.3), not
(0.4), is the variance in the correlated pairwise Haar identity.
The comparison involution \(\sigma\) is nonlocal; this ratio is therefore a
nonlocal correlated analogue of shield burnout, not one of the individual
transposition-renewal terms for the two physical cuts \(\tau,\tau'\).

The same packet pairs also admit a literal **diagonal** coupling. Every
diagonal corner is fixed by \(\sigma\), and from the higher-energy one of
its two coherent endpoints some two-cut corner has energy smaller by at
least

\[
 \frac{B4^H}{1024M_AH^4}.
 \tag{0.5}
\]

Thus a comparably large coherent chart mode can be burned wholly inside the
reflection-invariant subspace; see Theorem 3.1. This does not yet contract
the invariant diagonal midpoint.

On the harmonic side, three explicit conjugate fixed-point involutions form
a polynomial quantitative frame on every centered Johnson layer. If
\(P_g=(I+g)/2\), then for the involutions \(s,r,t\) constructed in Section 4,

\[
 \boxed{
 \sum_{g\in\{s,r,t\}}\|(I-P_g)v\|^2
 \ge \frac1{100n^6}\|v\|^2
 }
 \tag{0.6}
\]

for every centered vector on every nontrivial subset layer, and hence for
the whole weighted Gaussian-window direct sum. Consequently, if the three
corresponding exact Haar kernels were simultaneously available at every
current state and each contracted its anti-invariant part by a factor
\(\delta\), a uniformly random one of the three kernels would contract the
full centered Gaussian-window norm by

\[
 \boxed{
 1-\frac{1-\delta}{300n^6}.
 }
 \tag{0.7}
\]

The present literal chart construction supplies that kernel only for one
reflection at its specially prepared state. Conjugating the construction
also conjugates the state, so after pulling back it attacks the same old
anti-invariant subspace. Thus (0.6) removes the *representation-theoretic*
invariant-residue obstruction, but (0.7) is not yet a literal iteration
theorem. No constant-one conclusion is asserted.

## 1. Audit of root disjointness and literal chronology

Let \(F^0\) be the canonical MSW factor and let

\[
 \sigma(i)=n-i\quad(1\le i\le2m),\qquad \sigma(n)=n.
 \tag{1.1}
\]

The exact MSW reflection identity is

\[
 \sigma C_w=C_{\mu(w)},
 \qquad
 \mu(w)=\overline{\operatorname{rev}(w)},
 \tag{1.2}
\]

so \(\sigma F^0=F^0\). For the initial chart packet \(K_R\), reflection
changes its two old indices from

\[
 1100R,\ 1010R
 \quad\hbox{to}\quad
 \mu(R)1100,\ \mu(R)1010.
 \tag{1.3}
\]

If \(R\) does not end in \(1100\) or \(1010\), no row in the first pair in
(1.3) can equal a row in any reflected selected pair: equality would force
the last four symbols of \(R\) to be one of those gadgets. Since distinct
rows of \(F^0\) own disjoint middle-root sets, all selected roots

\[
 U_R,\quad \sigma U_R
 \tag{1.4}
\]

are pairwise disjoint.

Each \(U_R\) is invariant under \(\tau=(2\ 3)\), and each \(\sigma U_R\)
is invariant under

\[
 \tau'=\sigma\tau\sigma=(2m-2\ \ 2m-1).
 \tag{1.5}
\]

Switching selected \(U_R\)'s cannot alter any row on a reflected root.
Moreover, invariance of \(\sigma U_R\) under \(\tau'\) prevents a fresh
\(\tau'\)-ownership edge from entering or leaving that root. Hence the
terminal chart on \(\sigma U_R\) remains one complete component after the
first cut. This proves the claimed two-cut chronology without a stale-overlay
assumption.

The direct comparison of \(F^*\) and \(\sigma F^*\) has, on every selected
pair, precisely the two connected components

\[
 \tau K_R/K_R\quad\hbox{on }U_R,
 \qquad
 \sigma K_R/\sigma\tau K_R\quad\hbox{on }\sigma U_R.
 \tag{1.6}
\]

All other rows agree because \(\sigma F^0=F^0\). Thus the pairwise
opposite signing is a genuine restriction of the direct comparison cube,
and Section 1 of the attacked report is exact.

## 2. Audit of the Haar, Catalan, and high-harmonic estimates

Let \(d_R\) be the stacked lower-window effect of switching \(K_R\), put

\[
 h_R=d_R-\sigma d_R,
 \qquad D=\sum_Rd_R,
 \tag{2.1}
\]

and let \(f^0=f(F^0)\). Since \(f^0=\sigma f^0\), the corner with bundle
signs \(\varepsilon_R\in\{\pm1\}\) has the exact load

\[
 f(F_\varepsilon)
 =f^0+\frac{D+\sigma D}{2}
   +\frac12\sum_R\varepsilon_Rh_R
 =P_\sigma f(F^*)+\frac12\sum_R\varepsilon_Rh_R.
 \tag{2.2}
\]

The first summand is \(\sigma\)-invariant and the second is
\(\sigma\)-anti-invariant, so they are orthogonal. Fair independent signs
give

\[
 \mathbb E\|(I-P_\sigma)f(F_\varepsilon)\|_H^2
 =\frac14\sum_R\|h_R\|_H^2,
 \tag{2.3}
\]

whereas

\[
 \|(I-P_\sigma)f(F^*)\|_H^2
 =\frac14\left\|\sum_Rh_R\right\|_H^2.
 \tag{2.4}
\]

At every depth the load total is \(W\). Therefore the exact floor
polynomial differs from the squared norm centered at \(W/N_q\) only by a
factor-independent constant. Subtracting (2.4) from (2.3) proves

\[
 \mathbb E[\mathcal Q_H(F_\varepsilon)-\mathcal Q_H(F^*)]
 =\frac{V_{\rm bun}-A_{\rm bun}}4.
 \tag{2.5}
\]

There is no fractional-floor error in (2.5).

For the coherent lower bound, put \(d=m-H-2\). If

\[
 R=UV_0,qquad U\in\mathcal D_H,quad V_0\in\mathcal D_d,
 \tag{2.6}
\]

the private arm contributes one identically oriented unit dipole for each of
the \(\operatorname{Cat}_H\) choices of \(U\). If \(V_0\) does not end in
either four-letter gadget, all indices in (2.6) are selected. The number of
such suffixes is exactly

\[
 L^\circ=\operatorname{Cat}_d-2\operatorname{Cat}_{d-2}.
 \tag{2.7}
\]

Indeed, a Dyck word ending in either zero-net Dyck gadget must be at height
zero before that gadget, so deletion gives a unique member of
\(\mathcal D_{d-2}\). The two terminal families are disjoint.

The original private targets contain \(2m,n\) and omit \(1\); their
reflections contain \(1,n\) and omit \(2m\). They are disjoint, and all
nonprivate arms omit the marker \(n\). Hence one obtains, without a hidden
cross-arm cancellation,

\[
 A_{\rm bun}
 \ge \frac{4L^\circ\operatorname{Cat}_H^2}{c_H}.
 \tag{2.8}
\]

For \(d\ge3\), \(L^\circ\ge\operatorname{Cat}_d/2\). The elementary exact
Catalan estimates

\[
 \operatorname{Cat}_H\ge\frac{4^H}{4H^2},
 \qquad
 \operatorname{Cat}_{m-H-2}>\frac{B}{4^{H+2}},
 \qquad c_H\le M_A
 \tag{2.9}
\]

then give the first inequality in (0.1).

The universal four-arm profile gives

\[
 \|d_R\|_H^2
 =\frac4{c_1}+8\sum_{q=2}^H\frac1{c_q}<8H.
 \tag{2.10}
\]

Consequently (0.3) follows from
\(\|d_R-\sigma d_R\|^2\le4\|d_R\|^2\), while (0.4) follows directly from
isometry. This proves every constant in (0.1)--(0.2).

For completeness, let \(P_{>J}\) be the sum of Johnson degrees above the
growing cutoff. Exact factors have zero degree-zero and degree-one centered
parts. The uniform run-cap estimate therefore gives

\[
 \|P_{\le J}(f(F^*)-\sigma f(F^*))\|_H^2\le4U,
 \qquad
 U=\frac{BH^3}{n}e^{\gamma H}.
 \tag{2.11}
\]

Thus

\[
 A_{\rm bun}^{>J}\ge A_{\rm bun}-4U,
 \qquad
 V_{\rm bun}^{>J}\le V_{\rm bun}<32HB,
 \tag{2.12}
\]

and also \(V_{\rm dir}^{>J}<16HB\). Since
\(\gamma<\log4\), both variance-to-coherent ratios tend to zero. This
validates the harmonic burnout assertion, with the distinction between
bundle and direct variances stated in (0.3)--(0.4).

## 3. A literal diagonal block inside the reflection-invariant subspace

The reflected packet pairs also give a second positive block, distinct from
the anti-invariant block in the attacked report. For each selected \(R\),
couple the two physical chart phases in the **same** direction. The two
choices on the paired roots are

\[
 (K_R,\sigma K_R)
 \quad\hbox{and}\quad
 (\tau K_R,\sigma\tau K_R).
 \tag{3.1}
\]

Choose these phases independently over \(R\), leaving every unlisted root
on its \(F^0\)-row. Every resulting factor is literal and exact by root
disjointness. It is also fixed by \(\sigma\), because reflection interchanges
the two roots in a pair and the phases in (3.1) agree.

Put

\[
 g_R=d_R+\sigma d_R,
 \qquad G=\sum_Rg_R,
 \qquad
 A_+=\|G\|_H^2,
 \qquad V_+=\sum_R\|g_R\|_H^2.
 \tag{3.2}
\]

Let \(F_-:=F^0\), let \(F_+\) be the factor in which every pair uses the
second phase in (3.1), and let \(F_{\rm hi}\) be the endpoint of larger
floor energy.

### Theorem 3.1 (reflection-invariant chart-mode contraction)

For every fixed \(A>0\) and all sufficiently large \(m\), some literal
\(\sigma\)-fixed diagonal corner \(F_{\rm dec}\) is reachable from
\(F_{\rm hi}\) by the same two freshly recomputed chart cuts and satisfies

\[
 \boxed{
 \mathcal Q_H(F_{\rm dec})
 \le \mathcal Q_H(F_{\rm hi})
 -\frac{B4^H}{1024M_AH^4}.
 }
 \tag{3.3}
\]

Moreover, relative to the common diagonal midpoint, fair signs contract the
entire coherent invariant chart mode by

\[
 \boxed{
 \frac{V_+}{A_+}
 <\frac{4096M_AH^5}{4^H}=o_A(1).
 }
 \tag{3.4}
\]

#### Proof

Write a diagonal corner using signs \(\eta_R\in\{\pm1\}\). Its exact
centered load is

\[
 f(F_\eta)
 =f^0+\frac G2+\frac12\sum_R\eta_Rg_R.
 \tag{3.5}
\]

Fair signs therefore give

\[
 \mathbb E_\eta\mathcal Q_H(F_\eta)
 =\frac{\mathcal Q_H(F_-)+\mathcal Q_H(F_+)}2
  -\frac{A_+-V_+}{4}.
 \tag{3.6}
\]

This is the parallelogram identity; as before, the integer floor contributes
only a factor-independent constant.

On every original private target and every reflected private target, the
vectors \(D+\sigma D\) and \(D-\sigma D\) have coefficients of the same
absolute value, because the two private target families are disjoint.
Nonprivate arms cannot meet either family. Thus the proof of (2.8)--(2.9)
applies unchanged and gives

\[
 A_+>\frac{B4^H}{128M_AH^4}.
 \tag{3.7}
\]

Also

\[
 V_+
 =\sum_R\|d_R+\sigma d_R\|_H^2
 \le4\sum_R\|d_R\|_H^2
 <32HB.
 \tag{3.8}
\]

Since \(\mathcal Q_H(F_{\rm hi})\) is at least the average of the two
endpoint energies, (3.6)--(3.8) imply

\[
 \mathbb E_\eta\mathcal Q_H(F_\eta)
 \le\mathcal Q_H(F_{\rm hi})
 -\frac{B4^H}{512M_AH^4}+8HB.
 \tag{3.9}
\]

For large \(m\), the last two terms are at most the negative quantity in
(3.3), so some diagonal corner is \(F_{\rm dec}\). Starting from either
coherent endpoint, select exactly the packet pairs on which its phase and
the desired corner differ. The first \(\tau\)-cut changes the initial
roots and the second fresh \(\tau'\)-cut changes the reflected roots.
Section 1 proves legality. Finally, (3.4) follows from (3.7)--(3.8).
Since the floor polynomial is nonnegative on integral loads, (3.3) also
forces
\[
 \mathcal Q_H(F_{\rm hi})
 \ge\frac{B4^H}{1024M_AH^4}.
\]
Thus \(F_{\rm hi}\) is itself a literal high-energy reflection-fixed state,
not merely the larger member of an uncontrolled pair.
\(\square\)

Theorem 3.1 burns an exponentially coherent direction lying wholly in the
\(\sigma\)-invariant subspace. It does not contract the invariant diagonal
midpoint \(f^0+G/2\); consequently it is not, by itself, a contraction of
the complete invariant residue left by the anti-invariant block.

## 4. A quantitative frame of three conjugate reflections

Identify the coordinate set with \(\mathbb Z_n\), where \(n=2m+1\), and
define

\[
 s(x)=-x,
 \qquad r(x)=1-x.
 \tag{4.1}
\]

Let \(u=(0\ 1)\) and put

\[
 t=usu.
 \tag{4.2}
\]

Each of \(s,r,t\) is an involution with one fixed point and \(m\)
transpositions, so all three belong to the same conjugacy class as the MSW
reflection.

### Lemma 4.1 (generated group and diameter)

Let \(G=\langle s,r,t\rangle\). Then

\[
 G=
 \begin{cases}
 A_n,&m\text{ even},\\
 S_n,&m\text{ odd},
 \end{cases}
 \tag{4.3}
\]

and the word diameter of \(G\) in \(\{s,r,t\}\) is less than \(7n^3\).

#### Proof

The products

\[
 c=rs:x\mapsto x+1,
 \qquad g=ts
 \tag{4.4}
\]

are respectively an \(n\)-cycle and a three-cycle on
\(\{-1,0,1\}\). Therefore the conjugates

\[
 c^igc^{-i}
 \tag{4.5}
\]

include a three-cycle, with either orientation, on every three consecutive
positions of the linear order \(0,1,\ldots,n-1\).

These adjacent three-cycles generate \(A_n\). Here is a diameter proof that
will also be used below. View a permutation as a list. After positions
\(0,\ldots,k-1\) have been fixed, locate the symbol required at position
\(k\). A three-cycle on consecutive positions can move it two places to the
left; if it finishes one place to the right of \(k\), one final three-cycle
on positions \(k,k+1,k+2\) puts it at \(k\). Repeat for
\(k=0,\ldots,n-3\). Fewer than \(n^2\) adjacent three-cycles are used. The
last two positions are then correct because the remaining permutation is
even.

Each cycle in (4.5), or its inverse, is a word of length at most \(4n+2\)
in \(s,r,t\). Hence every element of \(A_n\) has word length less than
\(6n^3\). The parity of each fixed-point involution is \((-1)^m\). If
\(m\) is even, the generated group is contained in \(A_n\), and hence is
exactly \(A_n\). If \(m\) is odd, it contains both \(A_n\) and the odd
permutation \(s\), and hence equals \(S_n\); one extra letter handles the
odd coset. This proves (4.3) and the stated diameter bound. \(\square\)

### Theorem 4.2 (three-reflection frame)

Let \(\mathcal H_r\) be the real permutation module on the \(r\)-subsets of
\(\mathbb Z_n\), where \(1\le r\le n-1\). If
\(v\in\mathcal H_r\) has coordinate sum zero, then

\[
 \boxed{
 \sum_{a\in\{s,r,t\}}\|(I-P_a)v\|_2^2
 \ge\frac1{100n^6}\|v\|_2^2.
 }
 \tag{4.6}
\]

The same estimate holds after summing arbitrary nonnegative weights over
different subset layers.

#### Proof

Both \(A_n\) and \(S_n\) act transitively on the \(r\)-subsets. Thus the
\(G\)-average of a centered \(v\) is zero, and

\[
 \frac1{|G|}\sum_{h\in G}\|v-hv\|_2^2=2\|v\|_2^2.
 \tag{4.7}
\]

Put

\[
 \mathcal E(v)=
 \|v-sv\|_2^2+\|v-rv\|_2^2+\|v-tv\|_2^2.
 \tag{4.8}
\]

If \(h=a_1\cdots a_\ell\), where
\(a_i\in\{s,r,t\}\) and \(\ell\le D<7n^3\), telescoping and
Cauchy--Schwarz give

\[
 \|v-hv\|_2^2
 \le \ell\sum_{i=1}^\ell\|v-a_iv\|_2^2
 \le D^2\mathcal E(v).
 \tag{4.9}
\]

Average (4.9) and use (4.7). Since \(D^2<49n^6\),

\[
 \mathcal E(v)>\frac{2}{49n^6}\|v\|_2^2.
 \tag{4.10}
\]

Finally \(I-P_a=(I-a)/2\), so the left side of (4.6) is
\(\mathcal E(v)/4\). The constant \(1/100\) is smaller than
\(1/98\), proving (4.6). Layerwise application proves the weighted direct
sum statement. \(\square\)

### Corollary 4.3 (conditional full-window contraction)

Suppose that, at one current exact state with centered stacked load \(v\),
there are three literal random exact-factor blocks \(K_a\),
\(a\in\{s,r,t\}\), satisfying

\[
 P_av'=P_av\quad\text{almost surely},
 \qquad
 \mathbb E[\|(I-P_a)v'\|_H^2\mid a]
 \le\delta\|(I-P_a)v\|_H^2
 \tag{4.11}
\]

for the output \(v'\) of \(K_a\). Choosing \(a\) uniformly gives

\[
 \boxed{
 \mathbb E\|v'\|_H^2
 \le
 \left(1-\frac{1-\delta}{300n^6}\right)\|v\|_H^2.
 }
 \tag{4.12}
\]

#### Proof

For fixed \(a\), the invariant and anti-invariant pieces are orthogonal, so
(4.11) gives

\[
 \mathbb E[\|v'\|_H^2\mid a]
 \le\|v\|_H^2-(1-\delta)\|(I-P_a)v\|_H^2.
 \tag{4.13}
\]

Average over the three choices and apply Theorem 4.2 on every depth. \(\square\)

## 5. Exact compositional boundary

For the state \(F^*\) of the reflected-chart theorem and the reflection
\(s=\sigma\), equations (2.2)--(2.4) verify (4.11) with

\[
 \delta=\frac{V_{\rm bun}}{A_{\rm bun}}
 <\frac{4096M_AH^5}{4^H}=o_A(1).
 \tag{5.1}
\]

Thus the first of the three desired kernels is literal and has exponentially
strong anti-invariant contraction.

However, conjugating this construction by \(h\) replaces both the reflection
and the state:

\[
 (F^*,s)\longmapsto(hF^*,hsh^{-1}).
 \tag{5.2}
\]

After pulling the whole construction back by \(h^{-1}\), it is again the
old \(s\)-kernel. It does not furnish an \(hsh^{-1}\)-kernel based at the
unchanged state \(F^*\). Moreover, a mixed first-block endpoint no longer
has the canonical/reflected chart pair decomposition needed in Section 1
for either of the other two physical reflections.

Therefore Theorem 4.2 proves that no harmonic common-invariant subspace
survives three suitable reflections, but the current exact-factor geometry
does not realize the three hypotheses in (4.11) at one state. The next exact
positive statement is a **common-base three-reflection chart theorem**:
construct, at every endpoint of the first reflected block, fresh disjoint
chart pairs for \(r\) and \(t\) which satisfy (4.11), with the curvature
factor still \(o_A(1)\). Corollary 4.3 would then give a literal polynomial
full-window contraction block.
