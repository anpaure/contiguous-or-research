# AD22: dependent vertical-phase rounding at the calibrated top scale

Date: 2026-07-25

Pure mathematics only.  No computation, solver, or web search is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q}.
\tag{0.1}
\]

Let \(H\) be the least positive integer satisfying

\[
 \lambda_H\ge m+H,
 \qquad M=m+H,
 \qquad p=N_H,
 \qquad S=Mp.
\tag{0.2}
\]

Then

\[
 H\sim\sqrt{m\log m},\qquad
 p=(1+o(1)){W\over m},\qquad
 S=W-o(W),\qquad Hp=o(W).
\tag{0.3}
\]

Choose one directed cyclic order on every rank-\(M\) top.  This gives
exactly \(p\) full promotion packets, one per top, and \(S\) flag
occurrences in every proper interval rank.  The hard rows may be truncated
to

\[
 Q=\left\lceil
 \sqrt{m(\log\log m+\gamma(m))}
 \right\rceil,
\tag{0.4}
\]

where

\[
 \gamma(m)\longrightarrow\infty,
 \qquad \gamma(m)=o(\log\log m).
\tag{0.5}
\]

The already proved outer-packet reservoir covers all depths \(Q<q\le H\)
at \(o(W)\) literal cost.  Hence only the \(2Q+1\) rows

\[
 m-Q,m-Q+1,\ldots,m+Q
\tag{0.6}
\]

need correlated integral rounding.

This note proves an exact **dependent-rounding theorem conditional on a
low-variance mean-reverting exchange kernel**.  The condition is local,
integral, preserves one cyclic order at every top, and is directly
checkable on proposed multi-top trades.

For a row load vector \(h\), the exact factorial energy above its balanced
integer minimum is

\[
 \Psi(h)=\sum_T\binom{h_T}{2}-\Phi_{\min}(S,N).
\tag{0.7}
\]

It is nonnegative, and the number of holes beyond the unavoidable scalar
deficit is at most \(\Psi(h)\).  If an integral exchange changes that row
by \(z\), then

\[
 \boxed{\Psi(h+z)-\Psi(h)
 =\langle h-SN^{-1}{\bf1},z\rangle+\frac12\|z\|_2^2.}
\tag{0.8}
\]

Suppose that, after rows already treated are frozen, there is at every
state a probability distribution on legal multi-top exchanges satisfying

\[
 \mathbb E(z\mid h)=-\kappa(h-SN^{-1}{\bf1})+e,
\tag{0.9}
\]

and

\[
 \mathbb E(\|z\|_2^2\mid h)\le\sigma^2.
\tag{0.10}
\]

Then conditional expectation gives an integral descent until

\[
 \boxed{
 \Psi(h)\le
 {\sigma^2\over2\kappa}+{\|e\|_2^2\over2\kappa^2}.}
\tag{0.11}
\]

Consequently, if every hard row has such a kernel with

\[
 \kappa\ge {c\over p},\qquad \sigma^2\le C,
\tag{0.12}
\]

for fixed positive constants \(c,C\), and the squared bias terms sum to
\(o(W)\) after the normalization in (0.11), then sequential rounding gives

\[
 \sum_{|r-m|\le Q}\Psi_r
 =O(Qp)+o(W)=o(W),
\tag{0.13}
\]

because \(Q=o(m)\) and \(p=O(W/m)\).  The calibrated packet word then has
length \(W+o(W)\).

This theorem identifies the exact quantitative gain demanded from
dependence.  Independent single-top heat-bath resampling already has the
ideal unbiased mean reversion

\[
 \kappa={1\over p},\qquad e=0,
\tag{0.14}
\]

but its exact row variance is

\[
 \sigma^2=2M(1-\vartheta_r)=\Theta(m),
\tag{0.15}
\]

where \(\vartheta_r=M/\binom Mr\).  Formula (0.11) then stops at
\(\Theta(Mp)=\Theta(W)\) in each row, exactly the independent rounding
barrier.  A bounded-support coupled exchange would have
\(\sigma^2=O(1)\), lowering the stopping scale to
\(O(p)=O(W/m)\) per row and completing the theorem after summing through
\(Q\).

No legal family realizing (0.9)--(0.12) is constructed here.  The known
fixed-top four-order rectangles have the right bounded variance and exact
rank selectivity, but are not transitions in the one-order-per-top state
space.  The smallest known one-per-top three-top triangle preserves only
one co-two row and has uncontrolled action elsewhere.  Thus the precise
remaining theorem is now a **low-variance multi-top mean-reversion
kernel**, not an unspecified nibble.

## 1. Exact calibrated and tail ledgers

Minimality in (0.2) gives

\[
 1\le {\lambda_H\over M}
 <{M-1\over m-H+1}
 =1+O(H/m).
\tag{1.1}
\]

The standard uniform expansion

\[
 \log\lambda_h={h^2\over m}
 +O\!\left({h\over m}+{h^3\over m^2}\right)
\tag{1.2}
\]

places the first crossing at \(H\sim\sqrt{m\log m}\).  In particular,

\[
 0\le W-S< {2H-2\over M-1}W=o(W),
\tag{1.3}
\]

and

\[
 Hp={HW\over\lambda_H}\le {H\over M}W=o(W).
\tag{1.4}
\]

At the cutoff (0.4), the exact packet-reservoir theorem applies: after any
core choice of one packet per top, appending

\[
 R=\left\lceil e^{-\gamma(m)/2}{W\over M}\right\rceil=o(W/M)
\tag{1.5}
\]

independent full packets has a deterministic realization leaving only
\(o(W)\) aggregate holes over \(Q<q\le H\), and costs \(o(W)\) including
resets.  The two Boolean tails beyond \(H\) have size \(O(W/H)=o(W)\).

Therefore it is sufficient to make the aggregate excess holes in (0.6)
equal to \(o(W)\).  The extra packets in (1.5) are appended after the core
rounding and need not respect one-per-top ownership.

## 2. The exact balanced factorial potential

Fix one proper rank with

\[
 N=\binom{2m}{r}.
\]

Every one-per-top configuration supplies a load vector

\[
 h=(h_T:T\in\binom{[2m]}r)\in\mathbb Z_{\ge0}^{N},
 \qquad \sum_T h_T=S.
\tag{2.1}
\]

Write

\[
 S=aN+b,
 \qquad a=\lfloor S/N\rfloor,
 \qquad0\le b<N.
\tag{2.2}
\]

The minimum of the factorial collision energy at this fixed total is

\[
 \Phi_{\min}(S,N)
 =(N-b)\binom a2+b\binom{a+1}{2}
 =N\binom a2+ab.
\tag{2.3}
\]

Define

\[
 \boxed{
 \Psi(h)=\sum_T\binom{h_T}{2}-\Phi_{\min}(S,N).}
\tag{2.4}
\]

### Proposition 2.1 (integrality, variance form, and equality)

Let

\[
 \bar h={S\over N},\qquad
 \theta={b\over N}.
\]

Then

\[
 \boxed{
 \Psi(h)
 ={1\over2}\sum_T(h_T-\bar h)^2
 -{1\over2}N\theta(1-\theta).}
\tag{2.5}
\]

In particular \(\Psi(h)\) is a nonnegative integer, and it vanishes
exactly when all loads lie in \(\{a,a+1\}\), with precisely \(b\) high
loads.

#### Proof

Since \(\sum h_T=S\),

\[
 \sum_T\binom{h_T}{2}
 ={1\over2}\sum_T h_T^2-{S\over2}.
\]

The balanced vector has squared norm

\[
 (N-b)a^2+b(a+1)^2
 ={S^2\over N}+N\theta(1-\theta).
\]

Subtraction proves (2.5).  Convex unit transfers from a larger load to a
smaller load strictly reduce the factorial energy until the two values
differ by at most one, proving nonnegativity and the equality statement.
\(\square\)

### Proposition 2.2 (factorial energy dominates excess holes)

Let \(H(h)=|\{T:h_T=0\}|\).  Then

\[
 \boxed{
 H(h)-(N-S)_+\le\Psi(h).}
\tag{2.6}
\]

#### Proof

If \(S<N\), then \(a=0\), \(\Phi_{\min}=0\), and

\[
 H(h)-(N-S)
 =\sum_T(h_T-1)_+
 \le\sum_T\binom{h_T}{2}=\Psi(h).
\]

If \(S\ge N\), the left side is \(H(h)\).  Starting from \(h\), fill
each zero coordinate by moving one unit from a coordinate of load at least
two.  Such a donor always exists until all holes are filled, because the
total is at least \(N\).  Each transfer lowers
\(\sum_T\binom{h_T}{2}\) by at least one.  Continuing to a balanced vector
shows that the initial energy excess is at least the number of filled
holes.  This proves (2.6). \(\square\)

The unavoidable scalar term, summed over the rows in (0.6), is already
\(o(W)\).  Indeed, if \(N_q>S\), then \(q=O(\sqrt H)\), and each deficit
is at most \(W-S=O(WH/m)\).  Hence

\[
 (W-S)+2\sum_{q=1}^{Q}(N_q-S)_+
 =O\!\left({WH^{3/2}\over m}\right)=o(W).
\tag{2.7}
\]

Thus (2.6) reduces the hard-window theorem to

\[
 \sum_{|r-m|\le Q}\Psi_r=o(W).
\tag{2.8}
\]

## 3. Exact one-step energy calculus

Let an integral legal exchange send one configuration to another and
change the current row by

\[
 z=h'-h\in\mathbb Z^N.
\]

The packet count is unchanged, so

\[
 \sum_Tz_T=0.
\tag{3.1}
\]

Put

\[
 g=h-\bar h{\bf1}.
\tag{3.2}
\]

### Proposition 3.1 (exact increment identity)

For every mass-preserving integral exchange,

\[
 \boxed{
 \Psi(h+z)-\Psi(h)
 =\langle g,z\rangle+{1\over2}\|z\|_2^2.}
\tag{3.3}
\]

#### Proof

Use the variance form (2.5).  The constant balanced correction cancels,
and (3.1) makes \(z\) orthogonal to the all-ones vector.  Expanding
\(\|g+z\|_2^2-\|g\|_2^2\) proves (3.3). \(\square\)

For an elementary four-target rectangle

\[
 z=e_A+e_D-e_B-e_C,
\tag{3.4}
\]

formula (3.3) is

\[
 \Delta\Psi=h_A+h_D-h_B-h_C+2.
\tag{3.5}
\]

Thus a rectangle orientation is strictly improving exactly when the two
negative-diagonal loads exceed the two positive-diagonal loads by at least
three.  Signed-lattice generation alone does not imply such an applicable
orientation at a nonnegative packet state.

## 4. Benchmark: exact independent heat-bath drift

For a top \(U\), let

\[
 p_U\in\{0,1\}^{\binom{[2m]}r}
\]

be the incidence vector of its \(M\) cyclic rank-\(r\) intervals in the
currently selected order.  Let \(\pi'_U\) be a uniformly random directed
cyclic order of \(U\), and let \(p'_U\) be its interval vector.  Put

\[
 \vartheta_r={M\over\binom Mr}.
\tag{4.1}
\]

Every rank-\(r\) subset of \(U\) occurs in a uniform order with probability
\(\vartheta_r\).  Thus

\[
 \overline p_U:=\mathbb E p'_U
 =\vartheta_r{\bf1}_{\binom Ur}.
\tag{4.2}
\]

Choose a top uniformly from the \(p=N_H\) tops, replace only its order by
\(\pi'_U\), and put

\[
 z=p'_U-p_U.
\]

### Theorem 4.1 (exact independent mean and variance)

For every current one-order-per-top configuration,

\[
 \boxed{
 \mathbb E(z\mid h)=-{1\over p}
   (h-\bar h{\bf1})=-{g\over p}.}
\tag{4.3}
\]

Moreover,

\[
 \boxed{
 \mathbb E(\|z\|_2^2\mid h)
 =2M(1-\vartheta_r).}
\tag{4.4}
\]

Consequently

\[
 \boxed{
 \mathbb E(\Delta\Psi\mid h)
 =-{1\over p}\|g\|_2^2+M(1-\vartheta_r).}
\tag{4.5}
\]

#### Proof

Summing (4.2) over all tops gives a coordinate-symmetric vector of total
mass \(Mp=S\).  Hence

\[
 \sum_U\overline p_U=\bar h{\bf1}.
\]

Since \(\sum_Up_U=h\), averaging \(p'_U-p_U\) over the uniform top proves
(4.3).

Both \(p_U\) and \(p'_U\) have squared norm \(M\).  Also every one of the
\(M\) targets in \(p_U\) has inclusion probability \(\vartheta_r\) in
\(p'_U\), so

\[
 \mathbb E\langle p_U,p'_U\rangle=M\vartheta_r.
\]

This proves (4.4), and substitution into (3.3) proves (4.5).
\(\square\)

### Proposition 4.2 (the exact independent-row law)

If the cyclic orders at distinct tops are chosen independently and
uniformly, then, for each fixed rank-\(r\) target \(T\),

\[
 Z_T\sim\operatorname{Bin}(K_r,\vartheta_r),
 \qquad K_r=\binom{2m-r}{M-r},
 \qquad K_r\vartheta_r=\bar h={S\over N}.
\tag{4.6}
\]

Consequently, if \(\theta=\bar h-\lfloor\bar h\rfloor\), then

\[
 \boxed{
 \mathbb E\Psi_r
 ={S\over2}(1-\vartheta_r)
   -{N\over2}\theta(1-\theta),}
\tag{4.7}
\]

and

\[
 \boxed{
 \mathbb E\sum_T\binom{Z_T}{2}
 =N\binom{K_r}{2}\vartheta_r^2.}
\tag{4.8}
\]

In particular, uniformly for \(|r-m|\le Q\),

\[
 \mathbb E\Psi_r=\Theta(W).
\tag{4.9}
\]

#### Proof

Exactly \(K_r\) calibrated tops contain \(T\).  Their choices are
independent, and each hits \(T\) with probability \(\vartheta_r\), which
proves (4.6).  Summing

\[
 \operatorname{Var}(Z_T)=K_r\vartheta_r(1-\vartheta_r)
\]

over all \(N\) targets and using \(NK_r\vartheta_r=S\) gives

\[
 \mathbb E\sum_T(Z_T-\bar h)^2=S(1-\vartheta_r).
\]

Formula (2.5) proves (4.7), and the binomial second factorial moment proves
(4.8).  In the hard window, \(S=(1-o(1))W\), \(N\le W\), and
\(\vartheta_r=o(1)\).  Since \(\theta(1-\theta)\le1/4\), (4.7) lies
between \((3/8-o(1))W\) and \((1/2+o(1))W\), proving (4.9).
\(\square\)

Since \(\|g\|_2^2=2\Psi+N\theta(1-\theta)\), (4.5) becomes nonnegative
at a potential of order \(Mp=S=\Theta(W)\).  Thus conditional-expectation
derandomization of independent top resampling cannot yield \(o(W)\)
energy in even one hard row.

The exact same-rank packet codegrees do not alter (4.4).  In the central
window, a fixed packet satisfies

\[
 {1\over D_r}
 \sum_{\{A,B\}\subseteq p_U}\operatorname{codeg}_r(A,B)
 ={2+o(1)\over m},
\tag{4.10}
\]

and the maximum diffuse same-rank ratio is \(2/m^2+o(m^{-2})\).  These
facts are favorable for constructing a coupled kernel, but the trace
variance of replacing a whole independent packet remains \(\Theta(M)\).
Across adjacent ranks, the nested-column conditional codegree is
\(2/(m+O(Q))=\Theta(1/m)\), so rows cannot be treated as independent
decorations of one packet.

## 5. The low-variance mean-reversion theorem

Order the hard rows arbitrarily as

\[
 r_1,r_2,\ldots,r_J,
 \qquad J=2Q+1.
\tag{5.1}
\]

A **legal stage-\(j\) exchange** is an integral transition between two
one-order-per-top configurations such that:

1. it replaces cyclic orders at finitely many tops and retains exactly one
   cyclic order at every top;
2. it preserves the complete load vector at every earlier row
   \(r_1,\ldots,r_{j-1}\); and
3. its current-row difference \(z\) has total mass zero.

No restriction is placed on later rows; they will be repaired later.

### Hypothesis \(\mathrm{LVMR}(c,C,\varepsilon)\)

For every sufficiently large \(m\), every stage \(j\), and every current
configuration, there is a finite probability distribution on legal
stage-\(j\) exchanges, allowing the identity exchange, for which

\[
 \mathbb E(z\mid h)=-\kappa_j g+e_j,
\tag{5.2}
\]

with

\[
 \kappa_j\ge {c\over p},
 \qquad
 \mathbb E(\|z\|_2^2\mid h)\le C,
\tag{5.3}
\]

and there are deterministic numbers \(\beta_j=\beta_j(m)\ge0\), independent
of the current state, such that

\[
 {\|e_j\|_2^2\over\kappa_j^2}\le\beta_j(m)
 \quad\hbox{for every admissible current state},
 \qquad
 \sum_{j=1}^{J}\beta_j(m)\le\varepsilon(m)W,
 \qquad \varepsilon(m)\longrightarrow0.
\tag{5.4}
\]

The distribution and the bias may depend on the complete current state.
The coefficient \(\kappa_j\) may also depend on that state.  The constants
\(c,C\) do not depend on \(m,j\), or the state, and the bounds \(\beta_j\)
are deterministic.  Thus (5.4) holds throughout every possible descent,
not merely along a path selected after seeing its terminal state.

### Theorem 5.1 (dependent vertical-phase rounding)

If \(\mathrm{LVMR}(c,C,\varepsilon)\) holds, then there is an integral
choice of exactly one cyclic order at every calibrated top such that

\[
 \boxed{
 \sum_{j=1}^{J}\Psi_{r_j}
 \le {C\over2c}Jp+{1\over2}\varepsilon(m)W
 =o(W).}
\tag{5.5}
\]

Consequently the selected packet family, the outer packet reservoir, and
literal completion give a contiguous-OR word of length \(W+o(W)\).

#### Proof

At stage \(j\), (3.3), (5.2), and (5.3) give

\[
 \mathbb E(\Delta\Psi_j\mid h)
 \le-\kappa_j\|g\|_2^2
      +\langle g,e_j\rangle+{C\over2}.
\]

Young's inequality gives

\[
 \langle g,e_j\rangle
 \le {\kappa_j\over2}\|g\|_2^2
     +{\|e_j\|_2^2\over2\kappa_j}.
\]

Since \(\|g\|_2^2\ge2\Psi_j\),

\[
 \mathbb E(\Delta\Psi_j\mid h)
 \le-\kappa_j\Psi_j
   +{\|e_j\|_2^2\over2\kappa_j}+{C\over2}.
\tag{5.6}
\]

Whenever

\[
 \Psi_j>
 {C\over2\kappa_j}+{\|e_j\|_2^2\over2\kappa_j^2},
\tag{5.7}
\]

the conditional expected change is negative.  Therefore at least one
exchange in the finite support strictly lowers the nonnegative integer
potential.  Repeatedly choose such an exchange.  The process terminates
with the reverse inequality in (5.7).

Legal stage-\(j\) exchanges leave all earlier rows unchanged, so this
descent can be performed successively for \(j=1,\ldots,J\).  Sum the
terminal bounds, use \(\kappa_j\ge c/p\), and apply (5.4):

\[
 \sum_j\Psi_j
 \le {C\over2c}Jp
 +{1\over2}\sum_j\beta_j(m),
\]

which is (5.5).  Finally,

\[
 Jp=O(QW/m)=o(W).
\]

Proposition 2.2 and (2.7) give \(o(W)\) hard-row holes.  Equations
(1.3)--(1.5), the outer packet reservoir, and the Boolean tails add only
\(o(W)\) letters and resets.  Every selected packet and every appended
mask is literal. \(\square\)

### Theorem 5.2 (simultaneous vertical mean reversion; no frozen rows)

The exact preservation of earlier rows in Theorem 5.1 is not necessary.
For the current one-order-per-top configuration, write \(h_j,g_j,z_j\) for
the load, centered load, and update in row \(r_j\), and put

\[
 \Psi_\Sigma=\sum_{j=1}^{J}\Psi_j.
\tag{5.8}
\]

Suppose that, at every configuration and for all sufficiently large \(m\),
there is a finite distribution on legal integral exchanges which retains
exactly one cyclic order at every top and satisfies, for state-dependent
coefficients \(\kappa_j>0\),

\[
 \mathbb E(z_j\mid h)=-\kappa_j g_j+e_j
 \quad(1\le j\le J),
 \qquad \kappa_*:=\min_j\kappa_j\ge {c\over p},
\tag{5.9}
\]

and

\[
 \mathbb E\left(\sum_{j=1}^{J}\|z_j\|_2^2\,\middle|\,h\right)
 \le C_m.
\tag{5.10}
\]

Here \(c>0\) is absolute and \(C_m\) is deterministic; both bounds hold
uniformly at every integral state.  Every exchange in the support is a
physical change of the selected top orders, so it preserves the row totals
and the nested vertical packet structure.  Assume also that there is a
deterministic \(\beta(m)\) such that, at every configuration,

\[
 \sum_{j=1}^{J}{\|e_j\|_2^2\over\kappa_j\kappa_*}
 \le\beta(m).
\tag{5.11}
\]

Then an integral one-order-per-top configuration exists with

\[
 \boxed{
 \Psi_\Sigma\le {C_mp\over2c}+{\beta(m)\over2}.}
\tag{5.12}
\]

In particular, the coefficient-one conclusion follows whenever

\[
 C_m=o(M),\qquad \beta(m)=o(W).
\tag{5.13}
\]

#### Proof

Sum the exact increment identity (3.3) over all hard rows.  Equations
(5.9)--(5.10) give

\[
 \mathbb E(\Delta\Psi_\Sigma\mid h)
 \le-\sum_j\kappa_j\|g_j\|_2^2
 +\sum_j\langle g_j,e_j\rangle+{C_m\over2}.
\]

Rowwise Young inequalities give

\[
 \sum_j\langle g_j,e_j\rangle
 \le{1\over2}\sum_j\kappa_j\|g_j\|_2^2
 +{1\over2}\sum_j{\|e_j\|_2^2\over\kappa_j}.
\]

Because
\(\sum_j\kappa_j\|g_j\|_2^2
\ge2\kappa_*\Psi_\Sigma\),

\[
 \mathbb E(\Delta\Psi_\Sigma\mid h)
 \le-\kappa_*\Psi_\Sigma
 +{1\over2}\sum_j{\|e_j\|_2^2\over\kappa_j}
 +{C_m\over2}.
\tag{5.14}
\]

Whenever

\[
 \Psi_\Sigma>{C_m\over2\kappa_*}
 +{1\over2}\sum_j{\|e_j\|_2^2\over\kappa_j\kappa_*},
\]

some exchange in the finite support strictly lowers the nonnegative integer
\(\Psi_\Sigma\).  Repetition terminates below the uniform bound in (5.12),
by (5.9) and (5.11).  Finally \(Mp=S=(1-o(1))W\), so (5.13) makes
\(C_mp=o(W)\). \(\square\)

Theorem 5.2 is quantitatively suited to a genuinely vertical bounded trade:
if an exchange changes only \(O(1)\) target flags in each hard row, then
\(C_m=O(J)=O(Q)=o(M)\).  It allows later rows to disturb earlier ones and
therefore avoids the exact-freezing gate in Theorem 5.1.  The common
physical exchange distribution in (5.9) remains essential; unrelated
rankwise mean identities from different exchanges do not compose
automatically.

### Exact conditional boundary

The theorem remains valid with row-dependent \(C_j,c_j\) provided

\[
 \sum_{j=1}^{J}{C_jp\over c_j}=o(W)
\tag{5.15}
\]

and the bias sum in (5.4) is \(o(W)\).  Thus bounded variance is convenient
but not logically necessary.  For example \(C_j=o(m/Q)\) uniformly and
\(c_j\) bounded below already suffice.

## 6. Martingale and variance audit

The proof of Theorem 5.1 uses conditional expectation and therefore needs
no concentration theorem.  If the kernels are actually sampled, one gets
the following exact variance control.

Suppose additionally that every current-row update satisfies

\[
 \|z\|_2\le B.
\tag{6.1}
\]

Put \(\Delta=\Psi(h+z)-\Psi(h)\).  By (3.3),

\[
 |\Delta|\le\|g\|_2\|z\|_2+{1\over2}\|z\|_2^2,
\]

and therefore

\[
 \boxed{
 \mathbb E(\Delta^2\mid h)
 \le2C\|g\|_2^2+{B^4\over2}.}
\tag{6.2}
\]

Indeed \((x+y)^2\le2x^2+2y^2\),
\(\mathbb E\langle g,z\rangle^2
\le\|g\|_2^2\mathbb E\|z\|_2^2\le C\|g\|_2^2\), and
\(\|z\|_2^4\le B^4\).

After subtracting the predictable drift in (5.6), the stopped potential is
a supermartingale with predictable quadratic variation bounded by the sum
of (6.2).  Standard truncation of the process at (5.7), followed by the
exponential supermartingale proof of the Freedman bound, gives
high-probability descent whenever desired.  This concentration refinement
is not needed for existence: selecting a support point no larger than the
conditional mean already gives the deterministic integral sequence.

The exact independent kernel has \(B^2\le2M\) and \(C=2M(1-\vartheta_r)\),
so (6.2) again has the wrong \(M\)-scale.  A bounded-size multi-top trade
affecting at most \(b\) target flags in the current row has

\[
 B^2\le2b,
 \qquad C\le2b,
\tag{6.3}
\]

and is at the correct variance scale when \(b=O(1)\).

## 7. What the exact codegrees do and do not prove

At every shallow central row, the selected interval columns have exact
same-row pair ratios

\[
 {2\over\binom rd\binom{2m-r}{d}}
\qquad(1\le d<M-r),
\tag{7.1}
\]

with the audited boundary value at \(d=M-r\).  For one packet,

\[
 {1\over D_r}
 \sum_{\{A,B\}\subseteq P_r}\operatorname{codeg}_r(A,B)
 ={2+o(1)\over m}.
\tag{7.2}
\]

Thus a bounded-support coupled exchange has a very large diffuse reservoir
of possible relabellings; same-row concentration is not the apparent
barrier.

The vertical columns are different.  For a prescribed nested pair
\(A\subset B\) at adjacent ranks, the exact conditional packet codegree is

\[
 {2\over |B|}=\Theta(1/m).
\tag{7.3}
\]

One packet contains \(2M\) such cover incidences between two consecutive
rows.  Their total normalized mass is \(4+o(1)\), not \(o(1)\).  Hence a
kernel cannot be assembled by independently coupling the rows; the whole
vertical phase column must remain intact.  Hypothesis LVMR is formulated
on physical multi-row packet exchanges for precisely this reason.

The codegrees support the scale \(\kappa\asymp1/p\): under complete
coordinate averaging, a target discrepancy is seen by a fraction
\(1/p\) of a uniform one-top update.  They do not prove that the update
can be decomposed into bounded-variance legal exchanges while freezing
earlier rows.  That decomposition is the missing integral statement.

## 8. Exact obstruction to the currently known trades

The fixed-top four-order selector uses two disjoint adjacent swaps and has
signed packet vector

\[
 e_{\pi_{00}}+e_{\pi_{11}}
 -e_{\pi_{10}}-e_{\pi_{01}}.
\tag{8.1}
\]

It changes only two complementary interval lengths and has an elementary
four-target square at each.  Hence it has the ideal row support for LVMR.
But either sign of (8.1) contains two packets in the same top.  It is not a
transition in the one-order-per-top configuration space.

Moreover the two orders on either diagonal differ by two adjacent swaps
and share at least \(M-4\) middle owners.  Thus even a temporary doubled-
top interpretation spends \(\Theta(M)\) owner collisions per available
cell.  A positive-density reservoir of such cells is incompatible with a
middle near-transversal.

There is a genuine one-order-per-top three-top adjacent-swap triangle on
tops \(R-i,R-j,R-k\), for an \((M+1)\)-set \(R\).  Its three packet
differences cancel exactly in the co-two row.  At all other ranks, including
the middle, the three adjacent-swap ladders generally do not cancel.  It
therefore supplies neither a stage kernel preserving prior rows nor the
mean identity (5.2).

Finally, summing fixed-top selector rectangles over many tops does not
escape the obstruction.  Each summand conserves packet count and middle
incidence separately in its own top.  If both signs are required to use at
most one packet in every top, middle-packet rigidity forces the two orders
to agree up to reversal, making the interval effect zero at every rank.

## 9. Precise remaining theorem

The coefficient-one theorem follows from the following statement.

> **Low-variance multi-top phase theorem.**  At the calibrated depth and
> cutoff (0.4), the one-order-per-top state space admits, for some ordering
> of its \(2Q+1\) hard rows, legal stage kernels satisfying
> \(\mathrm{LVMR}(c,C,\varepsilon)\) for fixed \(c,C>0\) and
> \(\varepsilon(m)\to0\).

Theorem 5.1 proves the implication with exact constants and quantifiers.
The weaker row-dependent condition (5.15) is also sufficient.  Alternatively,
Theorem 5.2 removes the row-freezing requirement if one physical exchange
has simultaneous mean reversion and total vertical variance \(o(M)\).

### Proved

1. The exact balanced factorial potential and its variance form.
2. Excess holes are at most factorial energy.
3. The exact update identity (3.3).
4. The exact independent heat-bath mean reversion and variance.
5. Independent rounding stalls at \(\Theta(W)\) energy per row.
6. LVMR with \(\kappa\ge c/p\), bounded row variance, and negligible bias
   yields \(O(p)\) energy per row.
7. Summing \(O(p)\) through \(2Q+1=o(m)\) rows gives \(o(W)\).
8. The deterministic conditional-expectation descent and the martingale
   variance ledger.
9. The exact codegree and legality boundaries for constructing the kernel.
10. Simultaneous vertical mean reversion with total variance \(o(M)\)
    suffices without freezing any row.

### Unproved

1. A legal low-variance mean-reverting multi-top kernel.
2. Any ordering of the hard rows for which previously corrected rows can
   be frozen while retaining mean reversion in the current row.
3. A bounded-support owner-safe circuit spanning the needed discrepancy
   directions.
4. A simultaneous physical kernel satisfying (5.9)--(5.13).

Thus the dependent-rounding route is quantitatively complete once LVMR is
supplied.  The missing step is sharply smaller than an unspecified
all-ranks matching theorem: it asks for bounded-variance integral exchange
kernels with exact vertical chronology and mean-reversion rate
\(\Theta(1/N_H)\).
