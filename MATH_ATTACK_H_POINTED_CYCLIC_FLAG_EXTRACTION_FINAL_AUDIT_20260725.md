# Final audit: pointed cyclic-flag extraction

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
long-running computation was used.

## 0. Verdict

The core extraction package is valid after four finite-form corrections and
two scope clarifications, all of which have been inserted in
`MATH_ATTACK_H_POINTED_CYCLIC_FLAG_EXTRACTION_20260725.md`.

The verified conclusion is an incidence-extraction theorem inside one
unchanged exact factor.  It does **not** construct compatible balanced quota
vectors at different depths, a common nested flag flow, a survival-closed
exceptional owner family, or a cover of the directed crossing packets.
Consequently it does not prove \((\mathrm{CA}_A)\).

The corrections are:

1. the collision sum is restricted to \(1\le g\le2H+1\), and its ratio
   estimate to \(1\le g\le2H\);
2. the relabelling is chosen using the full uncapped collision graph before
   any relabelling-dependent cap is selected;
3. Corollary 4.1 now records the missing deduction \(s\le d\);
4. Theorem 3.3 quantifies \(D\ge1\) and checks Hall for arbitrary partial
   clone sets;
5. Proposition 5.2 assumes both rankwise density and the parent-extension
   hypothesis (2.3);
6. right vertices are explicitly signed targets \((a,S)\).

No theorem-level failure remains after these repairs.

## 1. Signed flags and exact spill

For \(a=q+1\),

\[
[K]\setminus Z_a(\pi,j)
=I_\pi(j+m+a,m-q).
\]

The shift of \(j\) is a permutation of the \(K\) pointed starts in each
wreath.  Hence the upper signed slot \(a=q+1\) has exactly the complemented
depth-\(q\) lower histogram, not merely the same average.  The lower signed
slot \(a=-q\) has that histogram directly.  Thus (1.5)--(1.6) and the doubled
spill identity

\[
\mathcal E_{D_H}(F)=2\sum_{q=1}^H O_q(F)
\]

are exact.

For a minimizing balanced quota \(\beta_q\), both \(\mu_q^F\) and
\(\beta_q\) have total mass \(W\).  Therefore

\[
\sum_S(\mu_q^F(S)-\beta_q(S))_+
=\sum_S(\beta_q(S)-\mu_q^F(S))_+.
\]

This proves (1.11).  There is one deficit/spill term, not two.  Notice,
however, that the minimizing vectors \(\beta_q\) are chosen independently
at different depths; nothing here makes them the node loads of one common
nested resolution.

## 2. Fibre cap

Let \(\widehat\mu_q(S)=\min\{\mu_q^F(S),u_q\}\).  Since every balanced
quota obeys \(\beta_q(S)\le u_q\), one in fact has the equality

\[
(\beta_q(S)-\widehat\mu_q(S))_+
=(\beta_q(S)-\mu_q^F(S))_+.
\tag{2.1}
\]

Indeed, if \(\mu_q(S)\le u_q\) the two arguments coincide, while if
\(\mu_q(S)>u_q\), both positive parts vanish.  Thus, for every target family
\(\mathcal U\),

\[
\sum_{S\in\mathcal U}\widehat\mu_q(S)
\ge
\beta_q(\mathcal U)
-\sum_{S\in\mathcal U}(\beta_q(S)-\mu_q^F(S))_+.
\tag{2.2}
\]

Taking \(\beta_q(S)\ge c_q\) and enlarging the localized deficit sum to the
whole rank gives Lemma 3.1 exactly.  Formula (2.2) is a strictly stronger
localized version of that lemma.  Complementation transports it unchanged
to an upper signed slot.

The cap selects at most \(u_q\) candidate occurrences in a fibre.  It does
not delete an owner, alter a wreath, or declare that fibre high in a common
quota flow.

## 3. Same-parent collision

Fix one pointed pair of signed slots \(a<a'\), put \(g=a'-a\), and condition
on the relabelled lower target.  Its upper target is uniform among exactly

\[
\binom{m+1-a}{g}
\]

rank-\(g\) supersets.  Property (2.3) permits at most
\(\binom{g+b-1}{b-1}\) supersets in the same product parent.  Therefore the
full prescribed incidence graph has expected collision count at most

\[
P_{\mathcal A}^{\#}
=W\sum_{\substack{a<a'\\a,a'\in\mathcal A}}
\frac{\binom{a'-a+b-1}{b-1}}
     {\binom{m+1-a}{a'-a}}.
\tag{3.1}
\]

Since \(a+g\le H+1\), its denominator is at least
\(\binom{m-H}{g}\).  Grouping by \(g\) gives the printed
\(P_{\mathcal A}\), now with the finite range \(1\le g\le2H+1\).
For

\[
a_g=\frac{\binom{g+b-1}{b-1}}{\binom{m-H}{g}},
\]

the ratio

\[
\frac{a_{g+1}}{a_g}=\frac{g+b}{m-H-g}
=O_{A,b}(m^{-1/2})
\]

is needed only for \(1\le g\le2H\).  Together with
\(a_1=b/(m-H)\), this gives

\[
P_{\mathcal A}=O_{A,b}(HW/m)=o(W).
\]

The order of choices is important.  Choose a relabelling whose **full**
uncapped collision count is at most (3.1), and only then cap its fibres.
Every capped collision is a full collision, so an arbitrary cap rule cannot
invalidate the expectation argument.

## 4. Finite extraction and Hall integrality

After capping and keeping one edge per endpoint--parent cell, a cell of size
\(r\) loses

\[
r-1\le\binom r2
\]

edges.  Hence the collision bound pays for all parent pruning, while the
right degree remains at most \(\Delta_A\).  This verifies (3.8).

Let \(J\) be \(p\) starts of degree at least \(s\), and put
\(b_s=\lfloor s/\Delta_A\rfloor\).  For every \(X\subseteq J\),

\[
s|X|\le e(X,N(X))\le\Delta_A|N(X)|,
\]

so \(|N(X)|\ge b_s|X|\).  Clone every start \(b_s\) times.  For an arbitrary
set \(Y\) of clones, if \(X\) is its set of original starts, then

\[
|Y|\le b_s|X|\le|N_G(X)|=|N(Y)|.
\]

Thus Hall applies to every partial clone set and gives an integral matching.
For \(D\ge1\) and \(p=\lceil D/b_s\rceil\),

\[
p\le D\le b_sp.
\]

One may therefore thin the matched edges to exactly \(D\), leaving at least
one at every chosen start.  The targets remain globally distinct, and the
cell pruning makes them parent-rainbow at each start.  The exact sharing
excess is \(D-p\).

All edges remain literal intervals beginning at original pointed
occurrences in one relabelled exact-factor word.  The appended prefix of the
wreath portal word suffices even at the final original start.  Capping and
matching never create a seam or a new word occurrence.

## 5. Corollaries 4.1--4.3

Each signed slot contributes at most \(W\) to \(S_{\mathcal T}\), so

\[
S_{\mathcal T}\le dW.
\]

Thus (4.1) implies \(d\ge\varepsilon H\), validating
\(s=\lfloor\varepsilon H/2\rfloor\le d\).  The remaining estimates give

\[
M_s=\Omega_\varepsilon(W),
\qquad b_s=\Theta_{A,\varepsilon}(H).
\]

The finite theorem actually permits a variable demand: whenever
\(1\le D_m\le b_sM_s\), it returns

\[
p_m=\left\lceil D_m/b_s\right\rceil
=O_{A,\varepsilon}(D_m/H+1)
\tag{5.1}
\]

starts.  In particular, \(D_m=o(W)\) gives \(p_m=o(W/H)\).  This useful
quantitative strengthening still covers only the prescribed signed-target
incidences; it does not say that those starts hit survival or crossing
packets.

The finite contrapositive and the subsequential obstruction (4.6)--(4.7)
then follow exactly as printed.

## 6. Collision functional and audited-parent transfer

For a uniform \(p\)-subset of starts, the hit probability of a fibre of load
\(\mu\) is exactly the hypergeometric expression in (5.3).  If \(X\) is its
selected occurrence count and \(x=p\mu/W\), then

\[
\Pr(X>0)\ge\frac{(\mathbb EX)^2}{\mathbb EX^2}
\ge\frac{x}{1+x}.
\]

Engel-form Cauchy--Schwarz, \(\sum x=2Hp\), and

\[
\sum\mu^2=2HW+2\mathfrak K_H(F)
\]

give (5.6).  If \(\mathfrak K_H(F)\le C_AH^2W\) and
\(p/W=H^{-1}+o(H^{-1})\), the lower bound is

\[
\Phi_p(F)\ge\left(\frac2{1+C_A}-o(1)\right)W.
\]

Proposition 5.2 is valid only when the audited subbands satisfy both:

1. the rankwise density (5.13); and
2. a parent partition obeying (2.3) for fixed \(b\).

Density alone supplies audited globally distinct targets after a random
relabel, but it does not justify the parent-rainbow pruning or the sharing
claim (5.16).

## 7. Superconcentration and the extension ceiling

The light-fibre calculation in Theorem 6.1 gives

\[
M_{\rm light}=O(\sqrt{\epsilon_m}\,HW)=o(HW).
\]

Distributing \(2\binom\mu2\) over the \(\mu\) occurrences in one fibre
assigns \(\mu-1\) to each occurrence.  Hence the heavy mass forces

\[
\mathfrak K_H(F)=\omega(H^2W).
\]

The uniform-over-all-factors paragraph additionally needs both audited
subband hypotheses from Section 6 before failure of pointed extraction can
be converted into \(\epsilon_m^*\to0\).

Lemma 7.1 is exact.  An occurrence of a depth-\(q\) target lies in \(q+1\)
distinct middle windows of its row; different wreath occurrences produce
disjoint groups of such middle windows.  There are
\(\binom{m+q+1}{q}\) possible middle supersets, proving

\[
\mu_q^F(S)le
\left\lfloor\frac1{q+1}\binom{m+q+1}{q}\right\rfloor.
\]

This ceiling is far too large beyond depth one and supplies no balancing or
common-cover theorem.

## 8. Exact boundary for the CA lane

The extraction theorem may be imported only in the following form:

> Given one fixed exact factor and prescribed signed target families with
> retained capped incidence \(\Omega(HW)\), it integrally packs any
> \(D_m=o(W)\) globally distinct prescribed targets onto \(o(W/H)\) literal
> pointed starts, with parent-rainbow sharing.

The directed crossing-packet theorem requires something different: the
selected exceptional owners must meet every survival packet and every
owner set

\[
\mathcal C_q(\mathcal A)
=\{X:\Gamma_{q-1}(X)\in N_q(\mathcal A),
          \ \Gamma_q(X)\notin\mathcal A\}
\]

to its exact demanded multiplicity.  The extraction caps are independent
rankwise multiplicity truncations, not the high/low node loads of one common
balanced flow.  Global distinctness of signed targets and parent-rainbow
sharing imply neither survival coverage nor crossing-family coverage.

Therefore a valid combination needs a new compatibility theorem embedding
the repair tokens of the directed packet system into the prescribed
signed-target incidence graph.  The audited extraction theorem proves the
integral packing step once such an embedding with \(o(W)\) tokens and
\(\Omega(HW)\) retained support is supplied; it does not provide that
embedding.

