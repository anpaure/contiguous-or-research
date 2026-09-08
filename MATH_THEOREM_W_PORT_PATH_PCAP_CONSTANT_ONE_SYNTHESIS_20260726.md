# Port-path PCap realization: a sufficient theorem for coefficient one

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

There is a clean sufficient theorem, but the hypothesis is not yet proved.
The exact remaining assertion is a joint **port-path PCap-realization
lemma**.  It has two nonnegative terms:

1. the seed-level phase-capacity obstruction
   \(\operatorname {PCap}_H\); and
2. the excess of the actual multidepth hole count of one legal exact-middle
   row lift over that PCap floor.

Both terms must be \(o(W)\) for the same integral seed and the same row
exponents at all depths.  PCap alone is only a lower bound and is not
sufficient.

The local variables in the lemma are not arbitrary odd-cycle factors.
They are rooted complement-path partitions of middle-levels inclusion
graphs.  This is exactly the corrected \(D\)-**port**-transversal interface.
Ordinary \(D\)-transversality is insufficient.

Conditional on the one lemma stated in Section 6, the exact literal wreath
ledger and the product-SCD tail give

\[
             \nu(k)\le (1+o(1))
             \binom{k}{\lfloor k/2\rfloor}.              \tag{0.1}
\]

No current July 26 theorem proves the lemma.  In particular:

* the uniform anchored rectangle is a genuine port-preserving local atom,
  but its known fixed-scale deployment has insufficient PCap capacity for
  most Catalan overshoots;
* the rooted pentagon is a stronger genuine port-preserving atom, but its
  directly certified parent deployment has density \(1/64+o(1)\), still
  far below the required density;
* the certified nonlocal \(r=4\) Haar packet fails the inherited port
  interface in its present labelling;
* none of the phase-completion, affine-grid, two-seed, or four-arm theorems
  supplies one common legal lift with \(o(W)\) actual holes.

Thus (0.1) remains conditional.  The theorem below is a complete audit of
the implication, not a claim that coefficient one has been proved.

## 1. Global notation

Let

\[
 p=2m+1
\]

be an odd prime, and put

\[
 W=\binom pm,
 \qquad
 \mathcal V_q=\binom{[p]}{m-q},
 \qquad
 N_q=|\mathcal V_q|=\binom p{m-q},                 \tag{1.1}
\]

for \(0\le q\le m\).  The target universe in (1.1) is on all \(p\)
ambient coordinates.  Replacing it by
\(\binom{[2m]}{m-q}\) is an error: already at \(q=0\) that smaller
universe omits every middle owner containing the distinguished coordinate.

An **oriented exact middle wreath factor** \(F\) consists of

\[
                         \frac Wp=\operatorname {Cat}_m
\]

oriented cyclic coordinate orders whose length-\(m\) cyclic intervals
partition \(\binom{[p]}m\).  For \(S\in\mathcal V_q\), let

\[
 \mu_q^F(S)=
 \#\{\text{pointed rows of }F
       \text{ whose length-}(m-q)\text{ interval is }S\}. \tag{1.2}
\]

Every row contributes \(p\) distinct intervals, and therefore

\[
                         \sum_{S\in\mathcal V_q}\mu_q^F(S)=W.    \tag{1.3}
\]

The lower depth-\(q\) hole count is

\[
 M_q(F)=|\{S\in\mathcal V_q:\mu_q^F(S)=0\}|.          \tag{1.4}
\]

The complementary upper depth has exactly the same number of holes.

Let \(\sigma\) be a coordinate \(p\)-cycle.  For an exponent map

\[
                         a:F\longrightarrow\mathbb F_p,
\]

write

\[
                         F_a=\{\sigma^{a(C)}C:C\in F\}. \tag{1.5}
\]

For \(v\in\mathbb F_p\), put

\[
 U_v=\bigsqcup_{C:a(C)=v}M(C),                         \tag{1.6}
\]

where \(M(C)\) is the set of the \(p\) middle windows of row \(C\).
The exact phase-free legality criterion is

\[
 \boxed{
 F_a\text{ is an exact middle factor}
 \quad\Longleftrightarrow\quad
 \{\sigma^vU_v:v\in\mathbb F_p\}
 \text{ partitions }\binom{[p]}m.}                    \tag{1.7}
\]

Indeed, \(\sigma^vU_v\) is exactly the middle support contributed by the
rows with exponent \(v\), and the total cardinality of all the sets in
(1.7) is already \(W\).  No transversality to the
\(\sigma\)-necklace quotient is assumed in (1.7).

## 2. The corrected local interface

Let \(J\) be a set of \(2r\) local coordinates and let
\(\infty\notin J\).  Let

\[
 D_r\subseteq\binom Jr,
 \qquad |D_r|=\operatorname {Cat}_r,                 \tag{2.1}
\]

be the Dyck boundary sets inherited from an aligned MSW hole.

For a wreath on \(J\sqcup\{\infty\}\), delete its vertices containing
\(\infty\).  The remaining \(r+1\) vertices form a linear Johnson
geodesic.  Its two endpoints are the two core windows adjacent to
\(\infty\); call them the \(\infty\)-ports.

A local exact factor is **\(D_r\)-port-transversal** if every wreath has
exactly one member of \(D_r\) among its two \(\infty\)-ports.

### Theorem 2.1 (rooted complement-path normal form)

There is a bijection between:

1. \(D_r\)-port-transversal exact
   \(C_{2r+1}\)-factors of
   \(KG(J\sqcup\{\infty\},r)\); and
2. vertex partitions of the middle-levels inclusion graph on
   \(\binom Jr\sqcup\binom J{r+1}\) into the paths

   \[
   P=X_0\subset Y_0\supset X_1\subset\cdots
     \subset Y_{r-1}\supset X_r=J\setminus P,
   \qquad P\in D_r.                                    \tag{2.2}
   \]

The initial vertices in (2.2) run through \(D_r\) exactly once.

#### Proof

Cut a port-transversal wreath at \(\infty\), orienting from its selected
port \(P\).  Its avoiding-\(\infty\) windows give

\[
                         P=X_0,X_1,\ldots,X_r=J\setminus P.
\]

Put \(Y_t=X_t\cup X_{t+1}\).  Exact ownership of the vertices avoiding
\(\infty\) says that all \(X\)-vertices partition \(\binom Jr\).
Every intervening odd-graph vertex is

\[
 Z_t=\{\infty\}\cup(J\setminus Y_t).                 \tag{2.3}
\]

Complementation in \(J\), followed by adjoining \(\infty\), bijects
\(\binom J{r+1}\) with the odd-graph vertices containing \(\infty\).
Exact ownership of those vertices therefore says that all \(Y\)-vertices
partition \(\binom J{r+1}\).  This proves one direction.

Conversely, from a path partition (2.2), define \(Z_t\) by (2.3).  Since
\(X_t,X_{t+1}\subset Y_t\), both are disjoint from \(Z_t\), and the
complementary endpoints close the resulting sequence to a
\((2r+1)\)-cycle.  The two vertex partitions give exact ownership of the
two types of odd-graph vertices.  Its ports are \(P,J\setminus P\), so
the factor is port-transversal.  The two constructions are inverse.
\(\square\)

### Theorem 2.2 (exact parent substitution and composition scope)

Suppose an aligned ambient hole has local core
\(J\sqcup\{\infty\}\), common exterior \(O\), and canonical row
boundaries

\[
                         O\cup P,qquad O\cup(J\setminus P)
                         \quad(P\in D_r).             \tag{2.4}
\]

Any path factor (2.2) may replace the canonical local paths.  It fixes
(2.4) row by row and preserves, as multisets, both

\[
                         \biguplus X_t=inom Jr,
 \qquad                  \biguplus Y_t=inom J{r+1}.  \tag{2.5}
\]

Consequently the replacement produces another integral exact ambient
middle factor.

Moreover, finitely many such substitutions may be installed
simultaneously if their open modified row intervals are disjoint; sharing
an unchanged endpoint is harmless.  The resulting global factor is exact.

#### Proof

Adjoining \(O\) to every local state and colour embeds the two partitions
(2.5) into the two ambient ownership ledgers.  The ports in (2.4) make
every rowwise join unchanged.  Hence the ambient state and adjacent-union
multisets are unchanged, which is the exact local replacement criterion.

For several substitutions with disjoint open row intervals, every row is
formed by concatenating unchanged pieces and legal substituted pieces at
unchanged joins.  Each substitution contributes zero to both aggregate
ownership discrepancies.  Their sum is therefore zero. \(\square\)

This theorem does **not** say that lower-depth histograms add.  One
depth-\(q\) window can meet two disjoint substituted intervals and its
intersection is then a joint nonlinear function of both choices.
Cross-scale nested substitutions are also not covered: an outer
substitution can destroy the canonical inner slab and its inherited
ports.  Such regions must be treated by a genuinely joint ledger theorem.

### Why ordinary transversality fails

At \(r=2\), the two orders

\[
 (0,1,2,3,4),\qquad(0,2,4,1,3)                       \tag{2.6}
\]

form an exact factor.  With \(D=\{23,24\}\), each row contains exactly
one member of \(D\).  Nevertheless the first row's avoiding-zero path is

\[
                         12,23,34,                    \tag{2.7}
\]

whose ports are \(12,34\); its distinguished set \(23\) is internal.
No orientation turns (2.7) into a path from \(23\) to its complement
\(14\).  Thus ordinary \(D\)-transversality does not provide the parent
interface.

The uniform internal rectangle construction does satisfy the stronger
condition: it changes only internal states and fixes both endpoint states
row by row.  The certified nonlocal \(r=4\) Haar factor does not satisfy
the standard inherited port condition in its current labelling.

## 3. PCap and its exact logical scope

For an exact seed \(F\), define

\[
 K_q(F)=\sum_{S\in\mathcal V_q}(\mu_q^F(S)-p)_+,       \tag{3.1}
\]

\[
 \Delta_q=W-N_q,                                      \tag{3.2}
\]

and

\[
 \boxed{
 \operatorname {PCap}_H(F)=
 \sum_{q=1}^{H}\bigl(K_q(F)-\Delta_q\bigr)_+.}        \tag{3.3}
\]

The notation \(\Delta_q\) is used for the duplicate budget; it must not
be confused with the balanced quota
\(\lfloor W/N_q\rfloor\).

### Proposition 3.1 (phase-capacity lower bound)

For every exponent map \(a:F\to\mathbb F_p\), whether or not \(F_a\)
is exact at the middle layer,

\[
 \boxed{
 \sum_{q=1}^{H}M_q(F_a)
 \ge \operatorname {PCap}_H(F).}                     \tag{3.4}
\]

#### Proof

Fix \(q\) and a source target \(S\).  All
\(\mu_q^F(S)\) occurrences can move only among the \(p\) translates in
the \(\sigma\)-orbit of \(S\).  Since \(p\) is prime and
\(0<|S|<p\), that orbit has size \(p\).  Hence these occurrences cover
at most \(\min\{\mu_q^F(S),p\}\) targets.  Taking the union over source
targets can only reduce the covered set, so

\[
 \#\{\text{covered depth-}q\text{ targets}\}
 \le \sum_S\min\{\mu_q^F(S),p\}=W-K_q(F).             \tag{3.5}
\]

Therefore

\[
 M_q(F_a)\ge N_q-W+K_q(F)
             =K_q(F)-\Delta_q.                         \tag{3.6}
\]

Take positive parts and sum. \(\square\)

Thus PCap is a necessary seed statistic for a row-power proof.  It is not
sufficient.  Even \(K_q=0\) does not imply few holes.

For example, at \(q=1\), partition \(\mathcal V_1\) into full
\(\sigma\)-orbits.  Put load two on half the orbits and zero on half
(using one load-one orbit if their number is odd), and then distribute the
extra \(\Delta_1=W-N_1\) units by adding one on complete already-positive
orbits.  Since \(N_1\) and \(W\) are divisible by \(p\), this can be done
orbitwise.  For large \(m\), all loads are at most three, so \(K_1=0\),
while \((1/2+o(1))N_1\) targets are holes.  Complete orbits also have
uniform point margins.  This is a histogram counterexample, not an
asserted wreath-factor realization; it is enough to disprove any purely
algebraic implication from PCap and point margins to hole control.

Whenever \(F_a\) is a legal exact-middle lift, define its nonnegative
**realization slack**

\[
 \boxed{
 \mathcal R_H(F,a)=
 \sum_{q=1}^{H}M_q(F_a)-\operatorname {PCap}_H(F)\ge0.} \tag{3.7}
\]

The two exact missing quantities in the row-power architecture are now
\(\operatorname {PCap}_H(F)\) and \(\mathcal R_H(F,a)\).

The slack \(\mathcal R_H\) contains four effects not measured by PCap:

1. joint concentration of several source targets in one
   \(\sigma\)-orbit;
2. the fact that one exponent controls all occurrences in a row;
3. the middle exactness equations (1.7); and
4. the requirement that the same exponents work at every depth.

## 4. Correct coherent parent-library duals

This section records a precise way to test prospective port-path
libraries.  It is not an existence theorem.

A **product-compatible atom atlas** consists of atoms \(C\), each with a
finite library \(\mathscr L_C\) of joint port-path assignments, such that
choosing one member of every library in an arbitrary combination always
produces one global exact factor.  In addition, assign every affected
rooted window to the unique atom containing all substitutions on which
its target depends.  Regions coupled by a window at any serviced depth
must therefore be grouped into one joint atom.

For \(G\in\mathscr L_C\), let \(u_{C,G,q}\) be the full histogram of
the depth-\(q\) windows assigned to \(C\), including both crossing
collars.  Let \(\lambda_q\) be the histogram of all unaffected windows.
Then every integral choice \(\mathbf G=(G_C)\) has

\[
 \mu_q^{\mathbf G}=\lambda_q+
                    \sum_Cu_{C,G_C,q}                 \tag{4.1}
\]

simultaneously for all \(q\le H\).

Choose a probability distribution \(\pi_C\) on each library and put

\[
 \bar\mu_q=\lambda_q+
       \sum_C\sum_{G\in\mathscr L_C}\pi_C(G)u_{C,G,q}. \tag{4.2}
\]

The same \(\pi_C\) is used at every depth.

### Theorem 4.1 (correct multidepth fractional PCap dual)

Let

\[
 \Phi_H^{\rm P}=
 \min_{(\pi_C)}
 \sum_{q\le H}\bigl(K_p(\bar\mu_q)-\Delta_q\bigr)_+. \tag{4.3}
\]

Then

\[
\boxed{
\begin{aligned}
 \Phi_H^{\rm P}
 =\max_{0\le\gamma_q\le1}\Bigg\{&
 \sum_{q\le H}
 \left[
  \langle\gamma_q,\lambda_q-p\mathbf1\rangle
  -\Delta_q\|\gamma_q\|_\infty
 \right]\\
 &+\sum_C\min_{G\in\mathscr L_C}
       \sum_{q\le H}\langle\gamma_q,u_{C,G,q}\rangle
 \Bigg\}.
\end{aligned}}                                             \tag{4.4}
\]

All vectors in (4.4) are indexed by the corrected universe
\(\mathcal V_q=\binom{[p]}{m-q}\).

#### Proof

For a nonnegative real load \(x\) and \(\Delta\ge0\),

\[
 (K_p(x)-\Delta)_+
 =\max_{0\le\gamma\le1}
 \left[
   \langle\gamma,x-p\mathbf1\rangle
   -\Delta\|\gamma\|_\infty
 \right].                                                \tag{4.5}
\]

Indeed, first dualize \(K_p\) coordinatewise and then multiply it by the
outer scalar \(0\le\theta\le1\); putting
\(\gamma=\theta\alpha\) gives (4.5), with the least possible
\(\theta\) equal to \(\|\gamma\|_\infty\).

Substitute (4.2), sum (4.5) over depths, and interchange the minimum over
the finite product of probability simplexes with the maximum over the
compact target-weight cubes.  The payoff is bilinear apart from the
concave term \(-\Delta_q\|\gamma_q\|_\infty\), so finite-dimensional
minimax applies.  For fixed \((\gamma_q)\), one atom is minimized by one
library member common to all depths.  This gives the last line of (4.4).
\(\square\)

Indicator target sets do not suffice in (4.4); all fractional weights are
required.

### Theorem 4.2 (a sufficient integral PCap rounding condition)

For the same distributions, select atom states independently and define

\[
 V_q(S)=\sum_C\operatorname {Var}_{\pi_C}
                    u_{C,G,q}(S).                         \tag{4.6}
\]

Some integral product choice satisfies

\[
 \boxed{
 \operatorname {PCap}_H(F_*)
 \le
 \operatorname {PCap}_H(\bar\mu)
 +\frac12\sum_{q\le H}\sum_{S\in\mathcal V_q}
                         \sqrt{V_q(S)}.}                  \tag{4.7}
\]

#### Proof

Let \(Y_q=\mu_q^{F_*}-\bar\mu_q\).  Each integral and fractional
histogram has total mass \(W\), so \(\sum_SY_q(S)=0\).  Hence

\[
 K_p(\bar\mu_q+Y_q)-K_p(\bar\mu_q)
 \le\sum_SY_q(S)_+=\frac12\|Y_q\|_1.                  \tag{4.8}
\]

Subtracting \(\Delta_q\) and taking a positive part preserves the same
one-sided bound.  Independence gives

\[
                         \mathbb E|Y_q(S)|\le\sqrt{V_q(S)}.
\]

Sum and choose an outcome no worse than its expectation. \(\square\)

The square-root condition in (4.7) is a sufficient condition for this
particular independent rounding; it is not necessary for every possible
correlated or direct integral choice.  The distributions which make
(4.4) small must be the same distributions used in (4.6).

### Theorem 4.3 (direct-hole dual and rounding)

Define the fractional direct-hole value

\[
 \Phi_H^{\rm hole}=
 \min_{(\pi_C)}
 \sum_{q\le H}\sum_{S\in\mathcal V_q}
                      (1-\bar\mu_q(S))_+.               \tag{4.9}
\]

Then

\[
\boxed{
 \Phi_H^{\rm hole}
 =\max_{0\le\alpha_q\le1}
 \left\{
  \sum_{q\le H}\langle\alpha_q,
                              \mathbf1-\lambda_q\rangle
  -\sum_C\max_{G\in\mathscr L_C}
       \sum_{q\le H}\langle\alpha_q,u_{C,G,q}\rangle
 \right\}.}                                            \tag{4.10)
\]

For the same distributions and the variances (4.6), some integral exact
factor satisfies

\[
 \boxed{
 \sum_{q\le H}M_q(F_*)
 \le \Phi_H^{\rm hole}
       +\sum_{q\le H}\sum_{S\in\mathcal V_q}
                               \sqrt{V_q(S)}.}           \tag{4.11}
\]

#### Proof

The scalar identity

\[
                         (1-x)_+=max_{0\le\alpha\le1}
                                      \alpha(1-x)
\]

and minimax give (4.10).  The minus sign makes the minimizing distribution
choose a library member which maximizes weighted coverage, hence the
\(\max_G\) in (4.10).

For integral loads,

\[
                         \sum_S(1-\mu_q(S))_+=M_q.
\]

The map \(x\mapsto(1-x)_+\) is one-Lipschitz, so independent rounding
and \(\mathbb E|Y_q(S)|\le\sqrt{V_q(S)}\) give (4.11). \(\square\)

Consequently, proving the right side of (4.11) to be \(o_A(W)\) is one
direct, strictly stronger way to prove the missing lemma below with
\(a=0\).  Current port-path libraries do not satisfy such an audited
multidepth estimate.

## 5. Exact literal central-band and SCD-tail ledger

For an oriented exact factor \(G\), fix \(1\le H<m\).  In each row
\(\pi\), put

\[
                         E_j=I_\pi(j,m-H).
\]

Emit

\[
 E_0,E_1,\ldots,E_{p-1},E_0,E_1,\ldots,E_{2H}.       \tag{5.1}
\]

This block has length \(p+2H+1\), and every relevant consecutive OR is

\[
 \bigvee_{s=0}^{t-1}E_{j+s}
        =I_\pi(j,m-H+t-1)\qquad(1\le t\le2H+2).       \tag{5.2}
\]

Thus all cyclic intervals of lengths

\[
                         m-H,\ldots,m+H+1             \tag{5.3}
\]

are represented literally.  Concatenating the row blocks and appending
each missing lower and upper band target as one literal letter gives the
central length

\[
 W+\frac{2H+1}{p}W+2\sum_{q=1}^{H}M_q(G).             \tag{5.4}
\]

There is no factorability or pinning assumption in (5.4): the displayed
intervals are actual consecutive OR witnesses.

For the outer tails, put

\[
 A_m(a)=\binom ma-\binom m{a-1},                       \tag{5.5}
\]

\[
 w_m(0)=m,
 \qquad w_m(a)=m-2a+1\quad(a>0),                       \tag{5.6}
\]

and

\[
 C_m(t)=
 \begin{cases}
  0,&t<0,\\
  \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0.
 \end{cases}                                           \tag{5.7}
\]

The product of two symmetric-chain decompositions of disjoint
\(m\)-sets gives an explicit word of exact constructed length

\[
 \boxed{
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
              A_m(a)w_m(a)C_m(r-a)}                    \tag{5.8}
\]

covering both tails

\[
                         |S|\le r,
 \qquad                  |S|\ge2m-r.                  \tag{5.9}
\]

Indeed, pair two half-cube chains whose minimum ranks \(a,b\) satisfy
\(a+b\le r\), write the reverse increment word of the first followed by
the forward increment word of the second, and use a crossing interval.
The symmetric upper endpoints of the same chains prove the upper-tail
claim directly; no complementation of an OR witness is used.  Counting
the half-chains by their minimum ranks gives (5.8).

After the audited one-coordinate tail lift, every odd-dimensional target
outside (5.3) is covered in at most

\[
                         2L_m(m-H-1)                    \tag{5.10}
\]

letters.  Uniformly whenever

\[
                         \frac H{\sqrt m}\longrightarrow\infty,
 \qquad                  H\le\frac m2,                 \tag{5.11}
\]

one has

\[
                         L_m(m-H-1)=o\!\binom{2m}m=o(W). \tag{5.12}
\]

At fixed \(H=A\sqrt m\), (5.12) is not an \(o_m(W)\) statement: its
normalized value is an \(A\)-dependent tail.  One must first choose a
diagonal \(A=A(m)\to\infty\).

Combining (5.4) and (5.10) gives the exact finite inequality

\[
\boxed{
 \nu(2m+1)\le
 W+\frac{2H+1}{2m+1}W
 +2\sum_{q=1}^{H}M_q(G)
 +2L_m(m-H-1).}                                      \tag{5.13}
\]

## 6. The one minimal remaining lemma

The following statement is unproved.

### Lemma PPR\(_A\) (port-path PCap realization) — **UNPROVED**

For every fixed integer \(A\ge1\), and every sufficiently large odd prime
\(p=2m+1\), put

\[
                         H_A=\lceil A\sqrt m\rceil.     \tag{6.1}
\]

There exist:

1. a globally compatible collection of rooted complement-path factors
   (2.2), installed in aligned **parent** contexts of the canonical exact
   factor, with every substitution satisfying the port interface and the
   two exact ownership ledgers;
2. one integral choice of those local factors, producing one exact seed
   \(F_{A,m}\); and
3. one exponent map
   \(a_{A,m}:F_{A,m}\to\mathbb F_p\), common to every serviced depth,
   for which the phase-free partition equations (1.7) hold,

such that

\[
 \boxed{
 \operatorname {PCap}_{H_A}(F_{A,m})=o_A(W),
 \qquad
 \mathcal R_{H_A}(F_{A,m},a_{A,m})=o_A(W).}           \tag{6.2}
\]

Here \(o_A(W)/W\to0\) as \(m\to\infty\) for each fixed \(A\); no
uniformity in \(A\) is required.  Any substitution credited with splitting
a size-\(r\) full-window plateau must be performed in a size-\(r+1\)
parent, since a closed substitution inside the same hole cannot change
that hole's full intersection.

This is one joint lemma, not two independently selectable witnesses.  The
same integral seed and exponent map must satisfy both estimates in (6.2)
and must serve every \(q\le H_A\).

Lemma PPR\(_A\) is not MWB in different notation.  MWB is an unlabelled
balanced-overload assertion over arbitrary exact factors.  PPR\(_A\) is
a construction-restricted assertion: it demands an
exact seed assembled from prescribed rooted middle-levels path factors,
one common integral row exponent per wreath, the exact middle partition
equations, and actual near-surjectivity at all depths.  It implies the
raw-hole condition needed for coefficient one, but it does **not** presently
imply the balanced-overload statement MWB: its cap is \(p=2m+1\), whereas
the fixed-window MWB floors \(c_q\) are bounded.  A hole-free histogram
can still have linear balanced overload.  Conversely MWB does not supply
the prescribed path-factor/phase realization.  Thus no implication
between these two construction statements should be asserted without an
additional structural theorem.

The split (6.2) is minimal inside this architecture.  Proposition 3.1
proves both summands are nonnegative and that

\[
 \sum_{q\le H_A}M_q((F_{A,m})_{a_{A,m}})
 =\operatorname {PCap}_{H_A}(F_{A,m})
  +\mathcal R_{H_A}(F_{A,m},a_{A,m}).                \tag{6.3}
\]

Deleting the first condition permits the hereditary Catalan capacity
obstruction.  Deleting the second permits zero-PCap histograms with a
linear number of holes and ignores exact phase realization.

There are two rigorous ways a future proof could establish PPR\(_A\):

* prove the corrected coherent PCap dual (4.4) and an integral rounding
  estimate such as (4.7), then prove a common legal phase realization with
  \(\mathcal R_H=o(W)\); or
* prove the direct-hole dual and rounding bound (4.10)--(4.11), in which
  case one may take \(a=0\) and both terms in (6.2) follow at once.

Neither route is currently complete.

## 7. Sufficient theorem for coefficient one

### Theorem 7.1 (PPR at every fixed Gaussian window implies constant one)

Assume Lemma PPR\(_A\) for every fixed integer \(A\ge1\).  Then

\[
 \boxed{
 \nu(k)\le(1+o(1))\binom{k}{\lfloor k/2\rfloor}.}       \tag{7.1}
\]

#### Proof

For fixed \(A\), let

\[
                         G_{A,m}=(F_{A,m})_{a_{A,m}}.
\]

Equations (6.2)--(6.3) give

\[
                         \sum_{q\le H_A}M_q(G_{A,m})=o_A(W). \tag{7.2}
\]

The factor \(G_{A,m}\) is integral and exact at the middle layer by
(1.7), and the same exponent map produced (7.2) at all depths.

We now diagonalize.  For each integer \(j\ge1\), choose an increasing
threshold \(T_j\) so that, for every prime \(p=2m+1\) with
\(m\ge T_j\), the normalized left side of (7.2) is at most \(1/j\).
Enlarge \(T_j\) so that \(m\ge j^{12}\).  Along the prime dimensions put

\[
 A(m)=\max\{j:T_j\le m,\ j\le m^{1/12}\},
 \qquad H_m=\lceil A(m)\sqrt m\rceil.                \tag{7.3}
\]

Then

\[
 A(m)\longrightarrow\infty,
 \qquad H_m\le m^{7/12}+1=o(m),
 \qquad \sum_{q\le H_m}M_q(G_{A(m),m})=o(W).          \tag{7.4}
\]

The seam term in (5.13) is

\[
                         \frac{2H_m+1}{2m+1}W=o(W).    \tag{7.5}
\]

Since \(H_m/\sqrt m\to\infty\), the product-SCD theorem (5.12) gives

\[
                         L_m(m-H_m-1)=o(W).             \tag{7.6}
\]

Substituting (7.4)--(7.6) into the literal finite inequality (5.13)
proves

\[
                         \nu(p)\le W(p)+o(W(p))          \tag{7.7}
\]

along odd primes \(p\).

To pass to arbitrary dimensions, choose an odd prime \(p\le k\) with
\(p/k\to1\), which exists by the prime number theorem, and apply the
trimmed one-coordinate lift repeatedly:

\[
                         \nu(k)\le2^{k-p}\nu(p).         \tag{7.8}
\]

The central-binomial asymptotic gives

\[
 \frac{2^{k-p}W(p)}{W(k)}
 =(1+o(1))\sqrt{\frac{k}{p}}=1+o(1).                  \tag{7.9}
\]

Equations (7.7)--(7.9) prove (7.1). \(\square\)

The ordinary parity lift alone transfers an odd result only to the next
even dimension.  The prime-gap argument in (7.8)--(7.9) is what transfers
a prime-subsequence theorem to all dimensions.

## 8. Quantitative audit of the currently known port atoms

Let \(r\) be minimal with

\[
                         d=\operatorname {Cat}_r\ge4p,
 \qquad                  \theta=d/p.                    \tag{8.1}
\]

Then

\[
                         4\le\theta<16-\frac{24}{r+1},
 \qquad                  r=\Theta(\log p).               \tag{8.2}
\]

Write

\[
                         H_{m,s}=\frac12
                         \binom{2(m-s)}{m-s}.             \tag{8.3}
\]

The certified fixed-scale rectangle family has

\[
 T_{m,r}=H_{m,r+1}\operatorname {Cat}_{r-1},            \tag{8.4}
\]

and exactly

\[
 \frac{T_{m,r}}{H_{m,r}d}
 =\frac{(m-r)(r+1)}
 {4(2(m-r)-1)(2r-1)}
 =\frac1{16}+o(1).                                      \tag{8.5}
\]

The certified one-depth plateau demand is

\[
                         H_{m,r}\left(\frac d2-p\right)
 =H_{m,r}d\left(\frac12-\frac1\theta\right).          \tag{8.6}
\]

Even granting four perfect units of cap decrease to every rectangle, the
ideal supply-to-demand ratio is

\[
                         \frac{\theta}{2(\theta-2)}+o(1). \tag{8.7}
\]

The exact finite raw-capacity threshold is

\[
 \theta\le
 \frac{2(2(m-r)-1)(2r-1)}
 {(2(m-r)-1)(2r-1)-2(m-r)(r+1)}
 =4+\frac6r+O(r^{-2}+m^{-1}).                         \tag{8.8}
\]

Thus for every fixed \(\varepsilon>0\), the known rectangle family is
too small whenever \(\theta\ge4+\varepsilon\), even under perfect
routing.  At its own depth the two marked intrinsic arms have exactly
zero cap gain; the signs of the other arms at larger depths are not
controlled.

The rooted five-row pentagon is a genuine
\(D_3\)-port-transversal path-factor trade.  Its intrinsic signed target
vector is

\[
                         2e_3+e_5-e_4-2e_2.             \tag{8.9}
\]

Common one-hole contexts preserve its exact ledgers.  Dense same-hole
copies do not change the full-window plateau of that same hole.  The
directly certified parent deployment has

\[
 P_{m,r}^{\rm par}=H_{m,r+1}\operatorname {Cat}_{r-2},
 \qquad
 \frac{P_{m,r}^{\rm par}}{H_{m,r}d}=\frac1{64}+o(1).   \tag{8.10}
\]

Even crediting all three negative units perfectly gives only
\((3/64+o(1))H_{m,r}d\), below the minimum demand
\((1/4)H_{m,r}d\).  Hence the pentagon also does not prove PPR\(_A\).

The full anchored local-factor fibre is connected under ownership-component
switches, but the known path may use components of unbounded support and
has no monotone multidepth estimate.  The conjugated leaf-rectangle graph
remains disconnected for every \(r\ge4\).  These statements remove a
topological-invariant obstruction; they do not supply the quantitative
library required in (6.2).

## 9. Implication audit

The valid implication chain is exactly

\[
\begin{array}{c}
\text{rooted complement-path factors with port-compatible global ledgers}
\\[1mm]\Downarrow\quad\text{Theorems 2.1--2.2}\\[1mm]
\text{one integral exact seed }F
\\[1mm]\Downarrow\quad\text{PPR}_A\text{, still unproved}\\[1mm]
\operatorname {PCap}_H(F)=o(W)
\text{ and one exact legal lift with }\mathcal R_H=o(W)
\\[1mm]\Downarrow\quad\text{identity (6.3)}\\[1mm]
\sum_{q\le H}M_q(F_a)=o(W)
\\[1mm]\Downarrow\quad\text{literal inequality (5.13)}\\[1mm]
W+o(W)+\text{product-SCD tail}
\\[1mm]\Downarrow\quad\text{fixed-}A\text{ diagonal and prime lift}\\[1mm]
\nu(k)\le(1+o(1))W(k).
\end{array}                                             \tag{9.1}
\]

Every arrow other than the PPR\(_A\) arrow is proved in this note.  The
following tempting shortcuts are invalid.

1. Ordinary \(D\)-transversality does not imply a legal context
   substitution; the selected Dyck set must be a port.
2. A local path factor does not compose across overlapping or nested slabs
   without a joint endpoint and two-ledger proof.
3. Separating one distinguished Catalan child fibre does not control
   collisions between unrelated contexts or crossing windows.
4. PCap \(=o(W)\) does not upper-bound holes.
5. A relaxed orbit floor does not choose one exponent per row.
6. One-depth phase assignments, local choices, or additive thinnings may
   not be chosen separately at different depths.
7. Port substitution does not preserve transversality to a later
   \(\sigma\)-necklace partition.  The specialized \(\pm t\),
   \(p+2\)-component, and affine-grid reductions therefore cannot be
   composed automatically after parent substitution; only the general
   phase-free criterion (1.7) is unconditional.
8. Fixed \(A\) does not make the SCD tail \(o_m(W)\); the slowly growing
   diagonal must be chosen first.
9. A theorem only on odd primes reaches all dimensions only after the
   prime-gap/repeated-lift argument, not by the single parity lift alone.

This is the precise proved/conditional boundary as of the current July 26
files.
