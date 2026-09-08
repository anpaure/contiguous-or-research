# Lane Y12: direct PBBS Dyck windows, complete depth two, and the exact Gaussian gates

Date: 2026-07-25

No computation, finite search, or web search is used in this note.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
B=\frac{W}{n}=\operatorname{Cat}_m.
\]

The requested all-depth statement

\[
b_q=O_A(B),\qquad \widehat Q_q=O_A(B)
\quad(1\le q\le A\sqrt m)
\tag{0.1}
\]

on one canonical PBBS factor is **not proved**.  No counterexample to
(0.1) is proved either.  The present attack does prove the first genuinely
higher collision row, with explicit constants, and one further wrong-rank
row:

\[
\boxed{
b_2=E_2=0,\qquad
1\le \mu_2(S)\le10,\qquad
Q_2<48B\quad(m\ge8),
}
\tag{0.2}
\]

and

\[
\boxed{
b_3=E_3\le W-\binom n{m-2}<12B.
}
\tag{0.3}
\]

The new input in (0.2) is a direct five-unmatched-zero Dyck-forest
construction proving **complete depth-two PBBS coverage**.  It closes the
previous depth-two hole gate, rather than assuming it.

At arbitrary depth there are two logically separate remaining problems.

1.  Wrong ranks reduce exactly to short returns of the unmatched root in
    the Dyck skew product.  A first 10-elimination gives a nested,
    PBBS-driven exclusion-current formulation.  The attractive inequality

    \[
    g\ge n-2\operatorname{pk}(D)
    \tag{0.4}
    \]

    is **FALSE**: an explicit all-dimensional family has arbitrarily large
    peak defect and a physical return of gap seven.  The valid pointwise
    theorem is

    \[
    g\ge2\operatorname{ht}(D)+1.
    \tag{0.5}
    \]

    It proves \(b_q,E_q=o(B)\) uniformly only in the sub-Gaussian range
    \(q=o(\sqrt{m/\log m})\).  At \(q=\Theta(\sqrt m)\), wrong-rank
    control is an aggregate Dyck enumeration/clustering problem.

2.  Correct-window collisions reduce exactly to a conditional-completion
    count on target necklaces.  On an aperiodic necklace every unit of
    floor defect costs \(n\), so (0.1) requires floor-perfect fibres on all
    but \(O_A(B/n)\) weighted necklaces among \(\Theta_A(B)\) necklaces.
    Neither stationarity, return control, nor the known fibre cap proves
    this (1/n)-relative completion theorem.

Thus (0.2)--(0.3) are unconditional theorem-level advances, but they do
not compose to constant one.  Finally, the canonical PBBS object is a
point-regular odd-graph 2-factor, not an exact wreath factor: its components
may have length \(\ell n\).  Any constant-one implication must still cut
and literalize its chronology, or integrally rebundle it into actual
length-(n) wreaths.  Nothing below treats the raw PBBS factor as an exact
wreath factor.

## 1. PBBS windows and the correct floor

Let (f) be the canonical parenthesis/PBBS permutation of the middle
(m)-sets.  On one oriented component write

\[
A_i=f^i(A_0),
\]

and let

\[
\lambda_i=[n]\setminus(A_i\cup A_{i+1})
\]

be the omitted edge label.  The complement rule gives

\[
A_{i+1}=A_i^c\setminus\{\lambda_i\}
\]

and hence the exact step-two recurrence

\[
\boxed{
A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.
}
\tag{1.1}
\]

For (1\le q\le m), define the step-two window and its rank excess by

\[
I_q(i)=\bigcap_{h=0}^q A_{i+2h},
\qquad
\eta_{i,q}=|I_q(i)|-(m-q).
\tag{1.2}
\]

Repeated use of (1.1) shows \(\eta_{i,q}\ge0\).  Put

\[
b_q=\#\{i:\eta_{i,q}>0\},
\qquad
E_q=\sum_i\eta_{i,q},
\tag{1.3}
\]

where the sum is over all (W) oriented PBBS states.

For the correct windows, let

\[
\mu_q(S)=\#\{i:I_q(i)=S,\ |S|=m-q\},
\qquad
N_q=\binom n{m-q}.
\tag{1.4}
\]

Their total mass is

\[
T_q=\sum_S\mu_q(S)=W-b_q.
\tag{1.5}
\]

The floor for this mass is not always the floor for (W).  Define

\[
d_q=\left\lfloor\frac W{N_q}\right\rfloor,
\qquad
d_q^*=\left\lfloor\frac{W-b_q}{N_q}\right\rfloor,
\qquad
F_d(x)=\frac{(x-d)(x-d-1)}2.
\tag{1.6}
\]

The genuine floor-corrected collision excess is

\[
\boxed{
\widehat Q_q=\sum_{S\in\binom{[n]}{m-q}}F_{d_q^*}(\mu_q(S)).
}
\tag{1.7}
\]

It is nonnegative, and it vanishes exactly on floor/ceiling load vectors
of total mass (T_q).

### Lemma 1.1 (exact missing-mass floor correction)

Write

\[
W=d_qN_q+\rho_q,\qquad0\le\rho_q<N_q,
\]

and put (k_q=d_q-d_q^*\).  If

\[
Q_{q,d_q}=\sum_SF_{d_q}(\mu_q(S)),
\]

then

\[
\boxed{
Q_{q,d_q}-\widehat Q_q
=k_q(d_qN_q-T_q)-\frac{N_qk_q(k_q-1)}2.
}
\tag{1.8}
\]

In particular, if (b_q<N_q), then

\[
\boxed{
\widehat Q_q=Q_{q,d_q}-(b_q-\rho_q)_+.
}
\tag{1.9}
\]

#### Proof

For one integer (x), direct expansion gives

\[
F_{d}(x)-F_{d-k}(x)
=-k(x-d)-\frac{k(k-1)}2.
\]

Sum this identity and use \(\sum_S\mu_q(S)=T_q\) to obtain (1.8).
If (b_q<N_q), then (d_q^*\) is (d_q) or (d_q-1).  It drops by one
exactly when (b_q>\rho_q), and (1.9) follows.  \(\square\)

Formula (1.9) is essential at arbitrary depth.  Using (Q_{q,d_q})
without the subtraction overcharges holes forced solely by removing the
wrong-rank mass.

## 2. Exact Dyck skew product and short-return ledger

Use (1) for an up-step and (0) for a down-step.  Every middle state has
a unique forward-unmatched zero.  Rotate that zero to coordinate (u); the
remaining word is a Dyck word (D\in\mathcal D_m), so the state is
represented uniquely as

\[
(u,D)\in\mathbb Z_n\times\mathcal D_m.
\]

Display the first up-step reaching the global maximum of (D) as

\[
D=P\,1\,Q
\]

and define

\[
\delta(D)=|P|+1,
\qquad
\phi(D)=\overline Q\,0\,\overline P,
\tag{2.1}
\]

where the bar complements bits without reversing their order.

### Lemma 2.1 (exact rooted-Dyck PBBS map)

The word \(\phi(D)\) is Dyck and

\[
\boxed{
(u,D)\longmapsto(u+\delta(D)\pmod n,\phi(D)).
}
\tag{2.2}
\]

#### Proof

Suppose the marked step first reaches height (H).  Along (Q), the old
height never exceeds (H) and ends at zero.  Therefore \(\overline Q\),
read from height zero, has nonnegative partial sums and ends at height
(H).  The displayed zero lowers this to (H-1).  Every prefix of (P)
has height at most (H-1), so \(\overline P\), read from height (H-1),
stays nonnegative and ends at zero.  Thus \(\phi(D)\) is Dyck.

The PBBS update fixes the unmatched zero and complements every bit of
(D).  In (0\overline D), the complemented marked up-step is precisely
the new unmatched zero.  Cutting there reads \(\overline Q0\overline P\)
and shifts the root by \(\delta(D)\).  \(\square\)

Put

\[
D_t=\phi^tD,
\qquad
s_t(D)=\sum_{j=0}^{t-1}\delta(D_j)\pmod n.
\tag{2.3}
\]

Thus the omitted labels along the trajectory from \((0,D)\) are exactly
\(s_t(D)\).

### Lemma 2.2 (exact wrong-window and gap formulas)

Let

\[
\mathcal B_q=
\left\{D\in\mathcal D_m:
\exists\,0\le a\le j\le q-1,
\ s_{2a}(D)=s_{2j+1}(D)
\right\}.
\tag{2.4}
\]

Then

\[
\boxed{b_q=n|\mathcal B_q|.}
\tag{2.5}
\]

Every consecutive same-label gap is odd and at least three.  If (M_s)
is the global number of consecutive gaps (2s+1), then

\[
\boxed{
E_q=\sum_{s\ge1}(q-s)_+M_s.
}
\tag{2.6}
\]

Consequently

\[
\boxed{b_q\le E_q\le(q-1)b_q.}
\tag{2.7}
\]

#### Proof

In the (h)-th use of (1.1), the label \(\lambda_{i+2h}\) is inserted
and \(\lambda_{i+2h+1}\) is deleted.  An insertion is absent from an
earlier sampled state, so it never enters the full intersection.  A
deletion fails to lower the running intersection exactly when it deletes
a label inserted earlier in the same block.  This is precisely the
equality in (2.4), proving (2.5).

After an edge labelled (x), coordinate (x) is absent at two consecutive
states and then toggles at every step until the next (x)-edge.  Hence a
consecutive gap is odd; gap one would repeat a factor state and is
impossible.  A gap (2s+1) lies inside exactly (q-s) of the relevant
length-(2q) windows, proving (2.6).  Finally every bad excess is an
integer in \([1,q-1]\), which gives (2.7).  \(\square\)

Equivalently, if

\[
T(D)=\min\{t\ge1:s_t(D)=0\},
\]

then (T(D)) is the next same-label gap from the normalized root and

\[
M_s=n\#\{D:T(D)=2s+1\}.
\tag{2.8}
\]

## 3. Two-sided distinguished deletions

The next lemma is the structural core of the complete depth-two theorem.

Let a middle state (A) be normalized as (0_rD), where (r=r_+(A))
is its forward-unmatched zero.  Factor (D) into primitive Dyck factors

\[
D=C_1C_2\cdots C_t.
\]

Let (H) be the global height of (D).  Define:

- (p_+(D)): the first up-step ending at height (H);
- (p_-(D)): the initial up-step of the **last** primitive factor whose
  height is (H);
- (v(D)): the down-step immediately after the rightmost occurrence of
  height (H).

### Lemma 3.1 (two-sided distinguished deletion lemma)

For every middle state (A=0_rD),

\[
\boxed{
f^2(A)=(A\cup\{r\})\setminus\{p_+(D)\},
\qquad
A\cap f^2(A)=A\setminus\{p_+(D)\},
}
\tag{3.1}
\]

and

\[
\boxed{
f^{-2}(A)=(A\cup\{v(D)\})\setminus\{p_-(D)\},
\qquad
f^{-2}(A)\cap A=A\setminus\{p_-(D)\}.
}
\tag{3.2}
\]

For (m\ge2),

\[
\boxed{p_+(D)\ne p_-(D).}
\tag{3.3}
\]

#### Proof

Write

\[
D=P\,1_{p_+}\,Q.
\]

In (f(A)), the coordinate (p_+) is zero and, when rooted there, the
word is

\[
0_{p_+}\,\overline Q\,0_r\,\overline P.
\]

The height calculation in Lemma 2.1 shows that the suffix is Dyck.
Therefore (r_+(fA)=p_+).  Since
(fA=A^c\setminus\{r\}), applying (f) again proves (3.1).

For the backward statement write

\[
D=P\,0_v\,Q,
\]

where (v=v(D)).  The prefix (P) ends at height (H); after the
displayed down-step, (Q) stays at height at most (H-1).  Reverse
matching gives (r_-(A)=v).  Put

\[
C=f^{-1}(A)=A^c\setminus\{v\}.
\]

Rooting (C) at (v) gives

\[
0_vE,
\qquad
E=\overline Q\,1_r\,\overline P.
\tag{3.4}
\]

The word (E) is Dyck: \(\overline Q\) rises from zero to (H-1),
(1_r) reaches (H), and along \(\overline P\) the height is
(H-h_P(a)\ge0\).

Let (C_{j_*}) be the last primitive factor of (D) of height (H).
Write (P=LR), where (L=C_1\cdots C_{j_*-1}) and (R) is the nonempty
prefix of (C_{j_*}) ending immediately before (v).  In (3.4),
\(\overline Q\) never reaches (H).  After (1_r), the height during
\(\overline P\) is (H-h_P(a)\), so it returns to (H) exactly at prefixes
of (P) ending at height zero.  The last such prefix is (L), because
(R) lies strictly inside the primitive factor (C_{j_*}).  The next
symbol is the complement of the initial up-step of (C_{j_*}), hence a
down-step.  Thus the reverse-unmatched zero of (C) is (p_-(D)).
Applying (f^{-1}) once more gives (3.2).

For (3.3), if the first and last primitive factors attaining (H) differ,
the two positions lie in different factors.  If they are the same and
(H\ge2), (p_-) reaches height one whereas (p_+) reaches height
(H).  If (H=1), every primitive factor is (10); for (m\ge2) there
are at least two such factors, so the first and last tallest factors differ
after all.  \(\square\)

As an immediate consequence, for every (m\ge2),

\[
f^{-2}(A)\cap A\cap f^2(A)
=A\setminus\{p_-(D),p_+(D)\}
\]

has rank (m-2).  This proves pointwise that PBBS has no gap-three root
return; it is stronger than an aggregate gap count.

## 4. Complete depth-two PBBS coverage

### Theorem 4.1 (every rank-\((m-2)\) target occurs)

For every (m\ge2) and every

\[
S\in\binom{[2m+1]}{m-2},
\]

there is a middle state (A) such that

\[
\boxed{
f^{-2}(A)\cap A\cap f^2(A)=S.
}
\tag{4.1}
\]

#### Proof

Assume first (m\ge3).  Forward parenthesis matching of the deficit-five
word of (S) leaves five unmatched zeros.  In cyclic order write

\[
0_{z_0}D_0\,
0_{z_1}D_1\,
0_{z_2}D_2\,
0_{z_3}D_3\,
0_{z_4}D_4,
\tag{4.2}
\]

where every (D_j) is a possibly empty Dyck word.  Some (D_j) is
nonempty because \(|S|=m-2\ge1\).  Choose (i) such that

\[
H_i=H:=\max_jH_j,
\]

where (H_j) is the height of (D_j).  Let (u) be the down-step
immediately after the rightmost occurrence of height (H) in (D_i).
Write

\[
D_i=P\,0_u\,Q,
\qquad
D_i^{\uparrow}=P\,1_u\,Q.
\tag{4.3}
\]

Then (D_i^{\uparrow}) is a nonnegative ballot path of total height two.
Its maximum is (H+1), first reached at (u), and it ends at height two.

Set

\[
A=S\cup\{z_i,u\}.
\tag{4.4}
\]

Indices below are modulo five.  Rooting (A) at (z_{i+4}), its word is

\[
\begin{aligned}
0_{z_{i+4}}\;&D_{i+4}\,
1_{z_i}D_i^{\uparrow}\,
0_{z_{i+1}}D_{i+1}\,
0_{z_{i+2}}D_{i+2}\,\\
&0_{z_{i+3}}D_{i+3}.
\end{aligned}
\tag{4.5}
\]

The suffix is Dyck.  The block (D_{i+4}) returns to height zero; after
that the successive baselines are (1,3,2,1,0), and every inserted
(D)-block is nonnegative at its baseline.

In the primitive factorization of the suffix in (4.5), the central factor

\[
C=
1_{z_i}D_i^{\uparrow}
0_{z_{i+1}}D_{i+1}
0_{z_{i+2}}D_{i+2}
0_{z_{i+3}}
\tag{4.6}
\]

is primitive: after its initial up-step it stays strictly above zero until
its final displayed down-step.  Its height is exactly (H+2).  The step
(u) first reaches that height.  The (D_{i+1})-part starts at baseline
two and has height at most (H); the (D_{i+2})-part starts at baseline
one and has height at most (H).  Every primitive factor outside (C)
lies in (D_{i+4}) or (D_{i+3}) and has height at most (H).

Hence (C) is the unique tallest primitive factor of (4.5), its initial
up-step is (z_i), and the first up-step reaching the global maximum is
(u).  Lemma 3.1 gives

\[
p_-(A)=z_i,
\qquad
p_+(A)=u.
\]

Therefore

\[
f^{-2}(A)\cap A\cap f^2(A)
=A\setminus\{z_i,u\}=S,
\]

as required.

For (m=2), the target is (S=\varnothing).  Take the rooted word
(0,1100).  Its sole primitive factor has (p_-) equal to its first
up-step and (p_+) equal to its second, so Lemma 3.1 again gives (4.1).
\(\square\)

The states

\[
f^{-2}A,f^{-1}A,A,fA,f^2A
\]

contain the canonically oriented parity window

\[
f^{-2}A,A,f^2A.
\]

Thus (4.1) is a literal PBBS window, not a reversed or abstract path.

### Corollary 4.2 (exact depth-two rank and collision bounds)

For every (m\ge2),

\[
\boxed{b_2=E_2=0}
\tag{4.7}
\]

and every rank-\((m-2)\) target has load

\[
\boxed{1\le\mu_2(S)\le\binom52=10.}
\tag{4.8}
\]

For (m\ge8),

\[
\boxed{Q_2<48B.}
\tag{4.9}
\]

#### Proof

Equation (4.7) follows from Lemma 3.1, and the lower bound in (4.8) is
Theorem 4.1.  For the upper bound, in any correct window the two initial
extras over (S) are precisely the two distinct labels subsequently
deleted.  Parenthesis monotonicity puts both in the five reverse-unmatched
zeros of (S).  Their two-set determines the initial middle state, and
PBBS then determines the path.  Hence there are at most \(\binom52=10\)
occurrences.

For (m\ge8),

\[
d_2=1,
\qquad
W-N_2
=\frac{6(m+1)}{(m+2)(m+3)}W.
\tag{4.10}
\]

Since all loads lie in \([1,10]\),

\[
\begin{aligned}
Q_2
&=\sum_S\frac{(\mu_2(S)-1)(\mu_2(S)-2)}2\\
&\le4\sum_S(\mu_2(S)-1)\\
&=4(W-N_2)\\
&=\frac{24(m+1)}{(m+2)(m+3)}W
<48B.
\end{aligned}
\tag{4.11}
\]

There is no missing-mass correction because (b_2=0).  \(\square\)

## 5. The next wrong-rank row is also Catalan

For a depth-two occurrence put

\[
T_i=I_2(i).
\]

Then

\[
I_3(i)=T_i\cap T_{i+2}.
\tag{5.1}
\]

Both children have rank (m-2).  Since rank excess is always
nonnegative, an unequal pair has intersection of rank exactly (m-3),
whereas an equal pair gives excess one.  Thus

\[
b_3=E_3=\#\{i:T_i=T_{i+2}\}.
\tag{5.2}
\]

### Lemma 5.1 (a target cannot fill a whole step-two PBBS cycle)

Assume (m\ge3).  No nonempty target (S) can occur at every vertex of
one step-two PBBS cycle.

#### Proof

Let the underlying (f)-component have length (L=\ell n).  If (L) is
odd, the step-two cycle contains every (f)-state.  A target common to all
its windows would lie in every (A_i), impossible because adjacent
(f)-states are disjoint.

If (L) is even, (f^2) splits the component into its two parity cycles,
each of length (L/2).  If a coordinate (x\in S) lay in every state of
one parity cycle, it would occur at least (L/2) times in the full
component.  PBBS coordinate homomesy gives exactly

\[
\frac{Lm}{n}=\ell m
\]

occurrences of each coordinate.  But (L/2=\ell n/2>\ell m\), a
contradiction.  \(\square\)

### Theorem 5.2 (depth-three wrong-rank bound)

For (m\ge3),

\[
\boxed{
b_3=E_3\le W-N_2
=\frac{6(m+1)}{(m+2)(m+3)}W
<12B.
}
\tag{5.3}
\]

#### Proof

On one step-two cycle, (k) occurrences of a fixed target span at most
(k-1) adjacent equal pairs unless they fill the whole cycle.  Lemma 5.1
excludes the latter.  Summing over cycles and then targets gives

\[
\#\{i:T_i=T_{i+2}\}
\le\sum_S(\mu_2(S)-1).
\]

Complete depth-two coverage and total mass (W) give

\[
\sum_S(\mu_2(S)-1)=W-N_2.
\]

Now use (5.2) and (4.10).  Finally,

\[
6(m+1)(2m+1)<12(m+2)(m+3),
\]

which proves the last inequality.  \(\square\)

The theorem controls the rank of depth three.  It does **not** control the
floor-corrected collision energy of the correct depth-three targets; that
still requires a rank-\((m-3)\) completion/hole theorem.

## 6. Exact target-necklace collision reduction

For a good normalized root (D\notin\mathcal B_q), the target is

\[
\Theta_q(D)
=X(0,D)\setminus\{s_1(D),s_3(D),\ldots,s_{2q-1}(D)\},
\tag{6.1}
\]

where (X(0,D)) is the middle set represented by (0D).  Let

\[
\Psi_q(D)=[\Theta_q(D)]
\]

be its necklace under coordinate rotation.

For a target necklace \(\mathcal O\), put

\[
h_{\mathcal O}=|\operatorname{Stab}(\mathcal O)|,
\qquad
R_{\mathcal O}
=\#\{D\notin\mathcal B_q:\Psi_q(D)=\mathcal O\}.
\tag{6.2}
\]

Then \(|\mathcal O|=n/h_{\mathcal O}\).

### Theorem 6.1 (exact necklace-fibre formula)

For every (S\in\mathcal O),

\[
\boxed{
\mu_q(S)=h_{\mathcal O}R_{\mathcal O}.
}
\tag{6.3}
\]

Consequently

\[
\boxed{
\widehat Q_q
=\sum_{\mathcal O}\frac n{h_{\mathcal O}}
F_{d_q^*}(h_{\mathcal O}R_{\mathcal O}).
}
\tag{6.4}
\]

#### Proof

Each normalized root (D) has (n) spatial translates.  If its target
has orbit \(\mathcal O\), these translates distribute equally over the
\(n/h_{\mathcal O}\) targets in that orbit.  Thus each target receives
exactly (h_{\mathcal O}) translates from that normalized root.  Summing
over the (R_{\mathcal O}) roots proves (6.3), and summing their floor
energies proves (6.4).  \(\square\)

### Corollary 6.2 (the exact Gaussian conditional-completion gate)

Fix (A<\infty) and assume (q\le A\sqrt m).  Periodic target necklaces
contribute (o_A(B)) to (6.4).  Hence an (O_A(B)) collision theorem is
equivalent, up to (o_A(B)), to

\[
\boxed{
\sum_{\substack{\mathcal O\\|\mathcal O|=n}}
F_{d_q^*}(R_{\mathcal O})
=O_A(B/n).
}
\tag{6.5}
\]

#### Proof

Because (n) is odd, every nontrivial stabilizer has order at least three.
There are at most

\[
n\,2^{n/3}
\]

periodic binary targets.  The correct-fibre cap is

\[
\mu_q(S)\le\binom{2q+1}{q}=\exp(O_A(\sqrt m)),
\tag{6.6}
\]

while (d_q^*=O_A(1)) in the Gaussian window.  Thus the entire periodic
contribution is

\[
n2^{n/3}\exp(O_A(\sqrt m))=o(B).
\]

On an aperiodic orbit (h_{\mathcal O}=1), so (6.4) is exactly (n)
times the sum in (6.5).  \(\square\)

This is much stronger than ordinary occupancy.  There are \(\Theta_A(B)\)
aperiodic target necklaces, and every nonzero integer floor defect costs a
whole factor (n).  The desired (O_A(B)) bound permits only
(O_A(B/n)) weighted defective necklaces.  Return-time control does not
imply this conditional-completion estimate.

## 7. First 10-elimination, the height theorem, and false peak vacancy

Let (k(D)=\operatorname{pk}(D)) be the number of peaks (10) in (D),
and put

\[
d(D)=m-k(D),
\qquad
p_1(D)=n-2k(D)=2d(D)+1.
\tag{7.1}
\]

### Lemma 7.1 (equal-edge interpretation and invariance)

In the rooted cyclic word (0D), (p_1(D)) is exactly the number of equal
adjacent pairs.  It is invariant under PBBS.

#### Proof

The cyclic word has (k(D)) edges of type (10) and (k(D)) of type
(01), so the other (n-2k(D)) edges are equal.

Immediately before the unmatched root the pattern is (00), and
immediately after it the pattern is (01).  PBBS complements every bit
except the root.  Hence the preceding (00)-edge becomes unequal, the
following (01)-edge becomes (00), and every other edge preserves its
equality status.  One equal edge is removed and one is created.  \(\square\)

There is a stronger labelled statement.  Put a particle on every equal
edge, typed (0) for (00) and (1) for (11).

### Theorem 7.2 (exact first-elimination semiconjugacy)

The (p_1(D)=2d(D)+1) equality particles consist of (d(D)+1) type-zero
particles and (d(D)) type-one particles.  In cyclic particle order,
starting with the particle immediately before the unmatched root, their
type word is

\[
0\,\partial D,
\tag{7.2}
\]

where \(\partial D\) is the Dyck word obtained by deleting every adjacent
peak (10) of (D).

Under one original PBBS step:

1. the selected type-zero particle immediately before the root moves one
   physical edge clockwise, from the edge before the root to the edge
   after it;
2. the selected particle remains type zero and every other particle type
   is complemented;
3. in their fixed cyclic identity order, the selected particle identities
   follow exactly the canonical PBBS unmatched-root process on

   \[
   KG(2d(D)+1,d(D)).
   \]

#### Proof

Write (D) in alternating runs.  Deleting the last (1) and first (0)
at every peak leaves a Dyck word of semilength (m-k(D)=d(D)).  Within a
one-run, every surviving adjacency is an equality edge of type one; within
a zero-run, every surviving adjacency is an equality edge of type zero.
Starting at the equal (00)-edge immediately before the root, direct run
inspection gives exactly the word (0\partial D).  This proves the count
and (7.2).

The local update at the root is

\[
00\,1\longmapsto10\,0.
\]

Thus the preceding equality edge is removed and the following one is
created; it is the same labelled particle moved one edge clockwise, and it
still has type zero.  Every other equal edge has both endpoint bits
complemented, so its type is complemented.  This is exactly the PBBS rule
on the particle type word: complement all types except its unmatched zero.
Repeating the run identification at the next state shows that the next
selected identity is the next unmatched root of that smaller PBBS process.
\(\square\)

Therefore a physical root return is exactly a repeated current across one
directed physical bond in this PBBS-driven exclusion lift.  Two exact
conclusions follow.  The first is a valid pointwise height theorem; the
second refutes the stronger peak-defect bound.

### Theorem 7.3 (return gap dominates Dyck height)

If a normalized root \(D\) starts a consecutive omitted-label return of
gap \(g\), then

\[
\boxed{g\ge2\operatorname{ht}(D)+1.}
\tag{7.3}
\]

#### Proof

Induct on the odd integer \(g\).  If \(g\ge n\), then
\(\operatorname{ht}(D)\le m\le(g-1)/2\), so assume \(g<n\).

At time zero, an equality particle \(a\) moves into the physical edge
whose crossing is to recur.  Before another particle can make the final
entry through that edge, \(a\) must vacate it.  Let \(h\) be the first
subsequent time at which \(a\) is selected.  By Theorem 7.2, \(h\) is a
consecutive omitted-label return in the reduced PBBS with normalized Dyck
root \(\partial D\).  Same-label gaps are odd and at least three.  Also
\(h<g\), so

\[
h\le g-2.
\tag{7.4}
\]

The induction hypothesis in the reduced system gives

\[
\operatorname{ht}(\partial D)\le\frac{h-1}{2}.
\]

Deleting every peak of a nonempty Dyck path lowers its height exactly one:
under the plane-tree contour bijection, this is simultaneous deletion of
all leaf edges.  Hence

\[
\operatorname{ht}(D)
=\operatorname{ht}(\partial D)+1
\le\frac{h+1}{2}
\le\frac{g-1}{2}.
\]

This proves (7.3).  \(\square\)

### Corollary 7.4 (sub-Gaussian all-depth wrong-rank theorem)

Uniformly for

\[
q=o\!\left(\sqrt{\frac{m}{\log m}}\right),
\tag{7.5}
\]

the canonical PBBS factor satisfies

\[
\boxed{b_q=o(B),\qquad E_q=o(B).}
\tag{7.6}
\]

#### Proof

A bad depth-\(q\) start contains a root return of gap at most \(2q-1\).
Theorem 7.3 forces the normalized root at the start of that return to have
height at most \(q-1\).  Shifting a bad window to such a return start loses
at most a factor \(q\), because the insertion position can be any one of
the \(q\) step-two transitions.

The number of Dyck paths of semilength \(m\) and height at most \(h\) is
at most the number of length-\(2m\) closed walks from zero in the path
graph on \(0,1,\ldots,h\).  Its adjacency spectral radius is

\[
2\cos\frac{\pi}{h+2},
\]

so, for an absolute \(c>0\), the count is at most

\[
4^m\exp(-cm/h^2).
\tag{7.7}
\]

After this factor \(q\) and the \(n\) spatial roots are included, and
\(B=\operatorname{Cat}_m\asymp4^m/m^{3/2}\), the ratio to \(B\) is at
most

\[
O\!\left(qm^{5/2}e^{-cm/q^2}\right)=o(1)
\]

under (7.5).  The exponential saving also absorbs the factor \(q\) in
\(E_q\le(q-1)b_q\).  \(\square\)

Theorem 7.3 is sharp as a height statement, but height is typically of
order \(\sqrt m\); it cannot reach the fixed Gaussian window in (0.1).

### Theorem 7.5 (peak-defect vacancy is false)

For integers \(d\ge2\) and \(m\ge2d-1\), define

\[
D_{m,d}
=(10)^{m-(2d-1)}(1100)^{d-2}111000.
\tag{7.8}
\]

Then \(D_{m,d}\) is a Dyck word of semilength \(m\), has height three and
peak defect

\[
m-\operatorname{pk}(D_{m,d})=d,
\]

yet starts a consecutive physical omitted-label return of gap seven.
Therefore

\[
g\ge n-2\operatorname{pk}(D)
\tag{7.9}
\]

fails for every \(d\ge4\), and in every semilength \(m\ge7\).

#### Proof

Every displayed factor in (7.8) is Dyck.  Its number of peaks is

\[
m-(2d-1)+(d-2)+1=m-d.
\]

Deleting every peak gives

\[
\partial D_{m,d}=E_d:=(10)^{d-2}1100.
\tag{7.10}
\]

Put \(p=2d+1\).  Every defect-one Dyck path of semilength \(d\) has a
unique form

\[
E(a,b,c)=(10)^a\,1(10)^b0\,(10)^c,
\qquad
a,c\ge0,\ b\ge1,\ a+b+c=d-1.
\]

Direct substitution in the skew product gives

\[
\phi E(a,b,c)=E(b-1,c+1,a),
\qquad
\delta(E(a,b,c))=2(a+1).
\tag{7.11}
\]

For \(E_d=E(d-2,1,0)\), the first eight selected equality-particle labels
are therefore

\[
0,\quad p-3,\quad p-1,\quad1,\quad p-2,\quad0,
\quad2,\quad p-1.
\tag{7.12}
\]

The word \(D_{m,d}\) ends in \(000\), so the distinguished equality
particle and its cyclic predecessor occupy adjacent physical edges.  At
time zero particle \(0\) enters the returned edge.  The predecessor
\(p-1\) moves into the edge immediately behind it at time two.  Particle
\(0\) first moves again at time five and vacates the returned edge.
Particle \(p-1\) next moves at time seven and enters it.  It cannot enter
earlier while particle \(0\) occupies the edge, and after time five it is
the particle immediately behind.  Thus the physical root gap is exactly
seven.  For \(d\ge4\), \(2d+1>7\), disproving (7.9).  \(\square\)

The counterfamily is exponentially sparse on the Catalan scale.  In fact
the gap-seven roots admit an exact classification.

### Theorem 7.6 (exact gap-seven classification and count)

A Dyck root \(D\) of semilength \(m\) starts a consecutive gap-seven
return if and only if, for some \(d\ge2\),

\[
\boxed{
\partial D=(10)^{d-2}1100
\quad\text{and}\quad
D\text{ ends in }00.
}
\tag{7.13}
\]

Consequently the exact number of normalized gap-seven roots is

\[
\boxed{R_7(m)=2^{m-1}-m.}
\tag{7.14}
\]

#### Proof

For necessity, the leading equality particle must be selected again before
its predecessor makes the final entry.  In a seven-step physical return,
its first repeat in the reduced PBBS has odd gap three or five.  Gap three
is impossible except in reduced rank one, whose time-seven selected label
is the successor rather than the predecessor.  Thus the reduced repeat has
gap five.  The no-gap-three theorem one level lower forces the reduced root
to have peak defect one, so write it as \(E(a,b,c)\).

Using (7.11), the first five reduced voltages sum modulo \(p=2d+1\) to

\[
1+2(a+1)+2b=p-2c.
\]

It vanishes exactly when \(c=0\).  The selected label at time seven is the
predecessor exactly when

\[
2a+4=p-1=2d,
\]

so \(a=d-2\) and \(b=1\).  The predecessor equality particle starts
immediately behind the distinguished particle exactly when the original
root ends in \(00\).  This proves necessity; (7.12) proves sufficiency.

For the count, use the plane-tree contour bijection.  Fix the pruned core
\((10)^{d-2}1100\), which has \(d\) edges and \(d-1\) leaves.  Every
preimage is obtained by attaching ordered new leaf children in the child
slots of the \(d+1\) core vertices, with at least one attachment at each
core leaf.  The total number of slots is \(2d+1\).  The terminal \(00\)
condition forbids the final root slot, so the attachment generating
function is

\[
\frac{z^{d-1}}{(1-z)^{2d}}.
\]

The number of semilength-\(m\) preimages is

\[
[z^{m-d}]\frac{z^{d-1}}{(1-z)^{2d}}
=\binom m{2d-1}.
\]

Summing over \(d\ge2\) gives all odd binomial coefficients except
\(\binom m1\):

\[
\sum_{d\ge2}\binom m{2d-1}=2^{m-1}-m.
\]

This proves (7.14).  \(\square\)

Thus gap seven supplies \(\Theta(n2^m)=o(B)\) physical short-return starts.
It decisively refutes pointwise peak-defect control without obstructing the
desired Catalan aggregate bound.  At Gaussian depth the remaining wrong-rank
problem is an aggregate enumeration or packing theorem for growing gaps.

## 8. Fixed-depth rolling recursion and why it stops

There is an exact recursion which explains both Theorem 5.2 and the failure
of a naive induction to Gaussian depth.  A depth-\((q+1)\) window is wrong
if one of its two rolling depth-(q) children is wrong, or if both children
are correct and equal.  Thus

\[
b_{q+1}\le2b_q+a_q,
\tag{8.1}
\]

where (a_q) counts adjacent equal correct depth-(q) targets.

For a target with \(\mu_q(S)\) good occurrences, Lemma 5.1's argument
gives at most \((\mu_q(S)-1)_+\) adjacent equal pairs.  Hence

\[
a_q\le\sum_S(\mu_q(S)-1)_+.
\tag{8.2}
\]

For every fixed (q), eventually (d_q=1),

\[
W-N_q=O_q(B),
\]

and the fibre cap \(\mu_q\le\binom{2q+1}{q}\) is a constant.  Therefore a
Catalan bound on the non-forced holes at that fixed depth controls both
\(\widehat Q_q\) and the next wrong-rank row.  Theorem 4.1 supplies exactly
that input at (q=2).

At (q=\Theta(\sqrt m)), however,

\[
W-N_q=\Theta_A(W),
\qquad
d_q=\Theta_A(1)
\]

with (d_q) no longer necessarily one.  Adjacent occurrences at the floor
load can create a wrong next-depth window while contributing zero floor
energy.  Thus (8.1)--(8.2) do not iterate to (0.1).  The Gaussian theorem
requires the necklace-level completion estimate (6.5), not merely the
fixed-depth fibre cap.

## 9. Exact proved/conditional boundary

### 9.1 Independent audit of the decisive new step

The complete depth-two construction was independently rederived from the
square normal form

\[
\phi^2(A\,P'1R'0\,B)=B\,1\,A\,P'0R'.
\tag{9.1}
\]

The audit checked all of the following points.

1. In (4.5), the successive baselines after
   \(D_i^{\uparrow}\) are \(3,2,1,0\), so the displayed root really is
   forward-unmatched and the suffix is Dyck.
2. Ties among the original tallest \(D_j\)'s are harmless.  The selected
   central primitive has height \(H+2\), while every primitive outside it
   has height at most \(H\), so the primitive itself is uniquely tallest.
3. The flipped step \(u\) is the first step reaching height \(H+2\);
   later ties in the rest of \(D_i^{\uparrow}\) or in \(D_{i+1}\) do not
   affect the forward deletion.
4. The backward deletion is the initial up-step \(z_i\) of that unique
   tallest primitive, either by Lemma 3.1 or directly from (9.1).
5. The case \(m=2\), where all five forest blocks are empty, is correctly
   separated.
6. The centered triple is a forward canonical parity window, not an
   illicit reversal.
7. The constants \(d_2=1\) for \(m\ge8\),
   \(\mu_2\le10\), and \(Q_2<48B\) are unchanged.

The same audit tried the direct deficit-seven analogue.  It does not yield
an unconditional \(q=3\) coverage theorem.  After two rightmost-descent
flips, the intended marked ladder can be overtopped by the next Dyck block,
which sits at a higher baseline; equality of two original block heights is
already enough.  This is a failure of that proposed construction, not a
counterexample to depth-three coverage.  It shows exactly why the
one-backward/one-forward graft in Theorem 4.1 cannot simply be iterated.

The gap-seven counterfamily and classification were also independently
audited.  The audit rederived the pruned core (7.10), every selected label
in (7.12), the physical adjacency supplied by the terminal \(000\), the
absence of an earlier re-entry, the necessity conditions in (7.13), and
the leaf-attachment coefficient \(\binom m{2d-1}\).  It confirmed both
the refutation of (7.9) for \(d\ge4\) and the exact total
\(2^{m-1}-m\).  Hence no unproved pointwise vacancy assertion is used in
the final boundary.

The unconditional results of this note are:

1. the exact Dyck skew product and all-depth short-return ledger;
2. the exact missing-mass floor correction;
3. the two-sided distinguished-deletion lemma;
4. complete depth-two target coverage;
5. (b_2=E_2=0), (1\le\mu_2\le10), and (Q_2<48B);
6. (b_3=E_3<12B);
7. the exact necklace-fibre formula and the aperiodic (O_A(B/n))
   completion gate;
8. the first-10-elimination semiconjugacy to a nested PBBS-driven exclusion
   current;
9. the sharp height bound \(g\ge2\operatorname{ht}(D)+1\) and the
   sub-Gaussian wrong-rank theorem;
10. an all-dimensional gap-seven family refuting peak-defect vacancy, and
    the exact count \(R_7(m)=2^{m-1}-m\).

The following statements remain unproved:

1. the fixed-Gaussian-window wrong-rank bound
   \(b_q=O_A(B)\) for \(q\le A\sqrt m\);
2. the required aggregate enumeration/clustering theorem for growing
   return gaps or their iterated pruned cores;
3. complete or near-floor conditional completion at depths (q\ge3);
4. the aperiodic necklace estimate (6.5) uniformly through
   (q\le A\sqrt m);
5. an integral literalization or exact-wreath rebundling of the raw PBBS
   2-factor at Catalan cost.

The pointwise vacancy-current route is not merely unproved; Theorem 7.5
refutes it.  Even a different proof of Gaussian wrong-rank rarity would
not settle the collision fibres.  Conversely, stationarity or a balanced
correct-target histogram would not rule out short-return rank defects.
These are genuinely separate all-depth gates.

Accordingly, no constant-one claim is made here.  The sharp new theorem is
the complete depth-two PBBS shadow with the constants in (0.2), together
with the forced depth-three rank bound (0.3).
