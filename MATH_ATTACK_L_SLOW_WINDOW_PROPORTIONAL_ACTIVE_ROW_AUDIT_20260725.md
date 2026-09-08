# Slow product-SCD proportional atoms versus active-row no-recycling

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computer experiment is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 \mathsf T=\operatorname{Cat}_m=\frac Wn.
\]

The proposed slow-window reparameterization is arithmetically valid, but
the hierarchy

\[
 H=\sqrt m\,\omega(1+o(1)),\qquad
 H\ll b\ll\sqrt m\log m
\]

must be separated into two different assertions.

Write

\[
 b=\sqrt m\,\eta(1+o(1)),\qquad
 1\ll\omega\ll\eta\ll\log m.
\tag{0.1}
\]

Then the literal proportional-atom reduction works with no further tail
condition: the audited product-SCD word covers the two outer tails in
\(o(W)\) entries whenever \(H/\sqrt m\to\infty\) and \(H=o(m)\).
The raw binomial-tail condition is no longer relevant.

For a uniform, floor-remainder-only guarantee that all atom degrees are
accurate to the required relative \(o(m^{-1/2})\) scale, however, it is
sufficient to impose the additional slow-diagonal condition

\[
 \boxed{e^{\omega^2}\ll\eta.}
\tag{0.2}
\]

It is compatible with (0.1) precisely when
\(e^{\omega^2}=o(\log m)\). Under (0.1)--(0.2), one atom has

\[
 \boxed{\kappa=(\sqrt\pi+o(1))m\eta,}
\tag{0.3}
\]

and, for a matching of size \(p-t\), where

\[
 p=\left\lfloor\frac Wb\right\rfloor,
\]

the unmatched-edge term in the proportional matching-to-word ledger is
\(o(W)\) exactly when

\[
 \boxed{t=o(p/\sqrt m)
       =o\!\left(\frac{W}{m\eta}\right).}
\tag{0.4}
\]

There is one genuine positive composition with an exact factor. Choose
\(b\) in near-divisor form. Then every exact factor splits into

\[
 p-o(p/\sqrt m)
\]

legitimate proportional atoms whose two central target parts are already
pairwise disjoint. Thus the old one-remainder-per-factor-row loss is not a
barrier at the new scale.

The remaining gate is simultaneous off-middle occurrence resolution. If
\(\widetilde\Pi\) is the total pair-collision count of the segmented atoms,
then

\[
 \widetilde\Pi=o(p/\sqrt m)
\tag{0.5}
\]

would suffice by literal conflict deletion. The active-row no-recycling
theorem does **not** prove (0.5). Its target-recycling coefficient at rank
\(m+q\) is

\[
 (m+q)(m+1-q)=\Theta(m^2),
\]

whereas the Johnson spectral release per selected collision is only
\(\Theta(m)\). The resulting local-minimum inequality is algebraically
vacuous even if exact point margins are granted.

There is also a sharp direct obstruction to using the saturated
first-shadow branch. In that branch

\[
 \mu_1=M\mathbf1_{\mathcal A},\qquad
 M=\left\lfloor\frac{m+2}{2}\right\rfloor,
 \qquad |\mathcal A|=\frac WM.
\]

Since the proportional first-lower quota is exactly \(b_{-1}=b-1\), any
factor-contained proportional-atom matching has size at most

\[
 \boxed{
 \left\lfloor\frac{W}{M(b-1)}\right\rfloor
 =(1+o(1))\frac pM.}
\tag{0.6}
\]

Its leave is therefore \((1-o(1))p\), not \(o(p/\sqrt m)\).
The saturated active-row theorem may still produce an energy-decreasing
child factor; what (0.6) proves is that its saturated factor cannot itself
be converted into the required atom matching.

The exact conclusion is consequently negative but sharper than an object-
type warning:

\[
 \boxed{
 \begin{array}{c}
 \text{the product-SCD scale and the exact-factor row-count ledger close,}\\
 \text{but active-row no-recycling does not supply the atom leave;}\\
 \text{a segmented common-owner occurrence-resolution theorem is still needed.}
 \end{array}}
\tag{0.7}
\]

No claim of constant one is made.

---

## 1. Exact floor profile on the slow window

Let

\[
 H=\lceil\sqrt m\,\omega\rceil,
 \qquad b=\sqrt m\,\eta(1+o(1)),
\]

with (0.1). For

\[
 -H\le q\le H+1,
 \qquad N_q=\binom n{m+q},
\]

put

\[
 p=\left\lfloor\frac Wb\right\rfloor,
 \qquad b_q=\left\lfloor\frac{N_q}{p}\right\rfloor.
\tag{1.1}
\]

Write the two exact Euclidean divisions as

\[
 W=pb+u,\qquad 0\le u<b,
 \qquad \varepsilon=\frac up=o(1),
\tag{1.2}
\]

and define

\[
 \rho(q)=\max\{-q,q-1\}.
\tag{1.3}
\]

For \(d\ge0\), let

\[
 \mathcal R_d
 =\frac{N_{-d}}W
 =\prod_{i=0}^{d-1}\frac{m-i}{m+2+i}.
\tag{1.4}
\]

Binomial symmetry gives \(N_{-d}=N_{d+1}\). Therefore the proportional
floor profile is exactly

\[
 \boxed{
 b_q=\left\lfloor(b+\varepsilon)
                  \mathcal R_{\rho(q)}\right\rfloor,}
\tag{1.5}
\]

and

\[
 b_{-d}=b_{d+1},\qquad b_0=b_1=b
\tag{1.6}
\]

for all sufficiently large \(m\). The last equality uses \(p>b\), so
\(0\le u/p<1\).

For \(d\le H\), Taylor expansion in the exact product (1.4) gives,
uniformly,

\[
 \log\mathcal R_d
 =-\frac{d(d+1)}m+O\!\left(\frac{d^3}{m^2}\right).
\tag{1.7}
\]

Indeed, the linear contribution is

\[
 -\frac1m\sum_{i=0}^{d-1}(2i+2)
 =-\frac{d(d+1)}m,
\]

and the sum of all higher Taylor terms is bounded by the error in (1.7)
because \(H=O(\sqrt m\log m)=o(m)\). Hence

\[
 \mathcal R_H=e^{-\omega^2+o(1)}.
\tag{1.8}
\]

The exact minimum quota is

\[
 \boxed{
 b_{\min}
 =\left\lfloor(b+\varepsilon)\mathcal R_H\right\rfloor.}
\tag{1.9}
\]

Thus the floor cannot be erased under (0.1) alone. The three relevant
thresholds are distinct:

\[
 b_{\min}\ge1
 \iff (b+\varepsilon)\mathcal R_H\ge1,
\tag{1.10}
\]

\[
 b_{\min}\to\infty
 \quad\hbox{follows from}\quad
 \sqrt m\,\eta e^{-\omega^2}\to\infty,
\tag{1.11}
\]

and, under (0.2),

\[
 \boxed{
 b_{\min}=(1+o(1))\sqrt m\,\eta e^{-\omega^2}
 \gg\sqrt m.}
\tag{1.12}
\]

Zero edge quotas do not invalidate the literal reduction: if \(b_q=0\),
then \(N_q<p\), and the whole part is charged to the exact floor remainder.
They do invalidate an assertion of uniform near-regularity.

Condition (0.2) can be imposed together with (0.1) iff

\[
 e^{\omega^2}=o(\log m).
\tag{1.13}
\]

For example, one may take

\[
 \omega=\sqrt{\log\log\log m},
 \qquad \eta=(\log\log m)^2.
\tag{1.14}
\]

Then \(e^{\omega^2}=\log\log m\ll\eta\ll\log m\).

### Exact first shallow quota

The first noncentral quota has a useful exact value. Since

\[
 N_{-1}=N_2=\frac m{m+2}W
\]

and

\[
 \varepsilon=\frac up<\frac bp=o(b/m)
\]

(indeed \(p\) is exponential in \(m\)), while \(b=o(m)\), one has
eventually

\[
 b-1<\frac{N_{-1}}p
 =\frac m{m+2}(b+\varepsilon)<b.
\]

Therefore

\[
 \boxed{b_{-1}=b_2=b-1.}
\tag{1.15}
\]

Every proportional atom deletes exactly one of its \(b\) central columns
at the first lower and first noncentral upper depths.

---

## 2. Atom rank, degrees, and exact fractional mass

The number of rank parts is \(2H+2\), and the atom rank is

\[
 \kappa=\sum_{q=-H}^{H+1}b_q.
\tag{2.1}
\]

From (1.1),

\[
 \frac1p\sum_qN_q-(2H+2)<\kappa
 \le\frac1p\sum_qN_q.
\tag{2.2}
\]

Since \(H/\sqrt m\to\infty\), Chebyshev's inequality for a
\(\operatorname{Bin}(n,1/2)\) variable already gives

\[
 \sum_{q=-H}^{H+1}N_q=(1-o(1))2^n.
\tag{2.3}
\]

Stirling's formula gives

\[
 \frac{2^n}{W}=(\sqrt\pi+o(1))\sqrt m.
\tag{2.4}
\]

Also \(p=(1+o(1))W/b\), while the floor error \(O(H)\) in (2.2) is
\(o(b\sqrt m)\). Consequently

\[
 \boxed{
 \kappa=(\sqrt\pi+o(1))b\sqrt m
       =(\sqrt\pi+o(1))m\eta.}
\tag{2.5}
\]

Let

\[
 L=m+b+H.
\]

There are exactly

\[
 E=(n)_L=\frac{n!}{(n-L)!}
\tag{2.6}
\]

labelled injective words. Put \(D=E/p\). If

\[
 N_q=pb_q+R_q,
 \qquad 0\le R_q<p,
\tag{2.7}
\]

coordinate transitivity gives the exact labelled degree

\[
 d_q^{\rm edge}=\frac{b_qE}{N_q},
\tag{2.8}
\]

and hence

\[
 \boxed{
 \frac{d_q^{\rm edge}}D
 =\frac{pb_q}{N_q}
 =1-\frac{R_q}{N_q}.}
\tag{2.9}
\]

In particular,

\[
 0\le1-\frac{d_q^{\rm edge}}D
 \le\min\left\{1,\frac p{N_q}\right\},
\tag{2.10}
\]

and

\[
 \max_q\frac p{N_q}
 =(1+o(1))\frac{e^{\omega^2}}{\sqrt m\,\eta}.
\tag{2.11}
\]

Thus (0.2) implies the target-scale uniform estimate

\[
 \boxed{
 \max_q\left|1-\frac{d_q^{\rm edge}}D\right|
 =o(m^{-1/2}).}
\tag{2.12}
\]

Equation (2.11) is an upper bound, not an asymptotic equality for the
actual degree error, because an integer remainder \(R_q\) may vanish.
The important logical point is that (0.1) alone does not imply (2.12).

No degree strengthening is needed for fractional feasibility. Assigning
weight \(p/E\) to every labelled atom has total mass exactly \(p\), and
every vertex in part \(q\) receives load

\[
 d_q^{\rm edge}\frac pE
 =\frac{pb_q}{N_q}\le1.
\tag{2.13}
\]

Thus all floor profiles admit the exact uniform fractional matching; the
open issue is integral, column-correlated rounding.

---

## 3. Overlap and codegree ledger

Every designated position interval has length \(m+O(H)\), and two slots
have position differences at most \(b+2H+1=o(m)\). For slots \(P,Q\), put

\[
 a=|P\setminus Q|,\qquad c=|Q\setminus P|.
\]

Conditioned on a prescribed target occupying \(P\), the exact conditional
probability that a compatible prescribed target occupies \(Q\) is

\[
 \frac1{\binom{|P|}a\binom{n-|P|}c}.
\tag{3.1}
\]

The audited binomial series therefore remains uniform in the new regime:

\[
 \boxed{
 \sum_{Q\ne P}
 \frac1{\binom{|P|}{|P\setminus Q|}
          \binom{n-|P|}{|Q\setminus P|}}
 =O(m^{-1}).}
\tag{3.2}
\]

After excluding every pair with \(a+c=1\),

\[
 \boxed{
 \sum_{a+c\ge2}
 \frac{(a+c+1)^2}
      {\binom{|P|}a\binom{n-|P|}c}
 =O(m^{-2}).}
\tag{3.3}
\]

The first-order term is genuine. Let \(v\) be an \(m\)-set and \(w\) an
\((m+1)\)-set with \(v\subset w\). Since \(b_0=b_1=b\), exact slot
counting gives

\[
 \boxed{
 \frac{\deg(v,w)}{\deg(v)}
 =\frac{2b-1}{b(m+1)}.}
\tag{3.4}
\]

The same-start and adjacent-start contributions are respectively

\[
 \frac1{m+1},\qquad
 \frac{b-1}{b(m+1)}.
\tag{3.5}
\]

Relative to \(D=E/p\),

\[
 \frac{\deg(v,w)}D
 =\frac{p(2b-1)}{W(m+1)}
 =\frac{2+o(1)}m.
\tag{3.6}
\]

The second-order scale is also attained. By (1.15), a same-start
\(m\)-set/\((m+2)\)-set pair has

\[
 \frac{\deg_{\rm ss}(v,u)}{\deg(v)}
 =\frac{b-1}{b\binom{m+1}2},
\tag{3.7}
\]

and hence

\[
 \boxed{
 \frac{\deg_{\rm ss}(v,u)}D
 =\frac{p(b-1)}{W\binom{m+1}2}
 =\frac{2+o(1)}{m^2}.}
\tag{3.8}
\]

Thus the \(O(m^{-2})\) post-cover scale is sharp.

For the homogeneous proportional atom, take the canonical nested start
sets

\[
 I_q=\bigcup_{d\ge\rho(q)}J_d.
\tag{3.9a}
\]

Under this nested choice, the cover terms cannot simply be contracted
away. The central slot graph
contains the path

\[
 P_0-Q_0-P_1-Q_1-\cdots-P_{b-1}-Q_{b-1},
\tag{3.9}
\]

where \(P_j\) is the central \(m\)-slot and \(Q_j\) the central
\((m+1)\)-slot. Every other designated slot attaches to this ladder
through its vertical chain. Hence the full \(a+c=1\) overlay is connected;
contracting all first-order pairs contracts the whole atom.

---

## 4. Exact matching-to-word ledger with the product-SCD tail

Suppose the atom hypergraph has a matching of size \(p-t\). For every
selected atom emit the \(b+2H+1\) base windows from the proportional
reduction. The selected-row contribution is exactly

\[
 (p-t)(b+2H+1).
\tag{4.1}
\]

At rank \(m+q\), the number of missing targets is

\[
 N_q-(p-t)b_q=R_q+t b_q.
\tag{4.2}
\]

Appending all of them literally gives the exact band bound

\[
 \ell_{\rm band}
 =(p-t)(b+2H+1)+\sum_qR_q+t\kappa.
\tag{4.3}
\]

Since \(R_q<p\), there are \(2H+2\) parts, and \(pb\le W\),

\[
 \boxed{
 \ell_{\rm band}
 \le W+(4H+3)p+t\kappa.}
\tag{4.4}
\]

The selected-row collar is

\[
 (2H+1)p=(2+o(1))W\frac\omega\eta
\tag{4.5}
\]

and the worst-case accumulated floor-remainder allowance is

\[
 \sum_qR_q<(2H+2)p
 =(2+o(1))W\frac\omega\eta
\tag{4.6}
\]

The allowance and the collar are both \(o(W)\) because
\(\omega/\eta\to0\).

The audited symmetric-chain product construction appends a word of length

\[
 2L_m(m-H-1)=o(W)
\tag{4.7}
\]

covering both outer tails. Its hypotheses are exactly

\[
 H/\sqrt m\to\infty,\qquad H=o(m).
\]

In particular, no condition such as
\(\sqrt m e^{-\omega^2}/\omega\to0\), which belongs to raw mask
enumeration, is needed here.

Finally, (2.5) gives

\[
 \frac{p\kappa}{W}=(\sqrt\pi+o(1))\sqrt m.
\tag{4.8}
\]

Therefore

\[
 \frac{t\kappa}{W}
 =(\sqrt\pi+o(1))\frac tp\sqrt m,
\tag{4.9}
\]

which proves the exact little-\(o\) equivalence

\[
 \boxed{
 t\kappa=o(W)
 \iff t=o(p/\sqrt m).}
\tag{4.10}
\]

Since

\[
 p=(1+o(1))\frac{W}{\sqrt m\,\eta},
\tag{4.11}
\]

this is (0.4).

Whenever this odd-dimensional construction is obtained for every large
\(m\), the standard trimmed one-coordinate lift

\[
 \nu(2m+2)\le2\nu(2m+1),
 \qquad
 \binom{2m+2}{m+1}=2\binom{2m+1}{m}
\tag{4.12}
\]

gives the same constant-one conclusion in even dimension.

---

## 5. Near-divisor cutting of every exact factor

An arbitrary admissible integer \(b\) need not be compatible with the
atom leave when one starts from a fixed exact factor. The arithmetic can,
however, be chosen inside the allowed scale.

Let \(\eta\) satisfy (0.1), and define

\[
 G=\left\lfloor\frac{n}{\sqrt m\,\eta}\right\rfloor,
 \qquad
 b=\left\lfloor\frac nG\right\rfloor,
 \qquad
 r=n-Gb.
\tag{5.1}
\]

Then

\[
 G=(2+o(1))\frac{\sqrt m}{\eta},
 \qquad
 b=(1+o(1))\sqrt m\,\eta,
 \qquad 0\le r<G<b.
\tag{5.2}
\]

In particular, \(\lfloor n/b\rfloor=G\), and all conclusions of Sections
1--4 are unchanged.

### Theorem 5.1 (exact factor segmentation)

Every exact wreath factor splits into

\[
 s_0=G\mathsf T
\tag{5.3}
\]

legitimate proportional atoms whose rank-\(m\) and rank-\((m+1)\) targets
are pairwise disjoint. Moreover,

\[
 \boxed{
 \Delta_0:=p-s_0
 =\left\lfloor\frac{r\mathsf T}{b}\right\rfloor
 <\frac{W}{b^2}
 =o(p/\sqrt m).}
\tag{5.4}
\]

The unused middle-owner count is

\[
 r\mathsf T<\frac Wb=o(W/\sqrt m).
\tag{5.5}
\]

#### Proof

Orient and root every one of the \(\mathsf T\) cyclic rows. Partition its
first \(Gb\) starts into \(G\) consecutive blocks of \(b\) starts and
leave the final \(r\) starts unused. Since

\[
 m+b+H<n
\]

eventually, the coordinate word of length \(m+b+H\) attached to each block
is injective, so every block is a genuine proportional atom with the fixed
radius profile.

Distinct starts in one cyclic row give distinct fixed-rank intervals. At
rank \(m\), exactness of the factor gives distinct targets across rows as
well. At rank \(m+1\), the complement of a cyclic \((m+1)\)-window is a
cyclic \(m\)-window in the same row. Equality of two upper-central targets
would therefore force equality of two middle targets. Thus both central
parts are pairwise disjoint.

Since \(W=n\mathsf T=(Gb+r)\mathsf T\),

\[
 p=\left\lfloor\frac{W}{b}\right\rfloor
 =G\mathsf T+\left\lfloor\frac{r\mathsf T}{b}\right\rfloor,
\]

which proves the equality in (5.4). As \(r<G\le n/b\),

\[
 \frac{r\mathsf T}{b}<\frac{n\mathsf T}{b^2}=\frac{W}{b^2}.
\]

Finally,

\[
 \frac{W/b^2}{p/\sqrt m}
 =(1+o(1))\frac{\sqrt m}{b}
 =(1+o(1))\frac1\eta\to0,
\]

and (5.5) is identical. \(\square\)

### Why the near-divisor choice is necessary for this composition

For a general \(b\), write

\[
 n=G_b b+r_b,\qquad 0\le r_b<b.
\]

The same cutting gives exactly

\[
 p-G_b\mathsf T
 =\left\lfloor\frac{r_b\mathsf T}{b}\right\rfloor,
\tag{5.6}
\]

and

\[
 \frac{p-G_b\mathsf T}{p/\sqrt m}
 =(1+o(1))\frac{r_b\sqrt m}{n}.
\tag{5.7}
\]

An uncontrolled remainder \(r_b=\Theta(b)\) makes (5.7)
\(\Theta(\eta)\), much larger than one. The slow scale alone does not
remove this floor; (5.1) does.

---

## 6. The exact remaining gate inside a segmented factor

Fix the \(s_0\) atoms from Theorem 5.1. For every band rank let
\(\lambda_q(S)\) be the number of these atoms containing target \(S\), and
put

\[
 \widetilde\Pi_q
 =\sum_{S\in\binom{[n]}{m+q}}
       \binom{\lambda_q(S)}2,
 \qquad
 \widetilde\Pi=\sum_q\widetilde\Pi_q.
\tag{6.1}
\]

The two central contributions vanish by Theorem 5.1.

### Lemma 6.1 (collision deletion)

The segmented family contains a proportional-atom matching of size at
least

\[
 \boxed{s_0-\widetilde\Pi.}
\tag{6.2}
\]

Consequently,

\[
 \widetilde\Pi=o(p/\sqrt m)
\tag{6.3}
\]

is sufficient for the matching required in Section 4.

#### Proof

Form the conflict graph on the \(s_0\) atoms. Every graph edge is a pair of
atoms sharing at least one target. If a target has load \(k\), it counts
all \(\binom k2\) atom pairs sharing that target. Thus the number of
distinct conflict edges is at most \(\widetilde\Pi\). Choose one endpoint
of every conflict edge and delete the union of the chosen endpoints. This
deletes at most \(\widetilde\Pi\) atoms and leaves an independent set,
which is exactly an atom matching. Combine with (5.4). \(\square\)

There is also an exact necessary support condition. Let

\[
 \mathcal S_q(F)
 =\{S:\mu_q^F(S)>0\}
\tag{6.4}
\]

be the support of all cyclic rank-\((m+q)\) occurrences in the carrier
factor. Suppose \(D_0\) segmented atoms are deleted and the remaining
family is a matching. Every selected target belongs to \(\mathcal S_q(F)\),
so

\[
 (s_0-D_0)b_q\le|\mathcal S_q(F)|.
\]

Using \(s_0=p-\Delta_0\) and (2.7), this is equivalent to the necessary
inequality

\[
 \boxed{
 N_q-|\mathcal S_q(F)|
 \le R_q+(\Delta_0+D_0)b_q.}
\tag{6.5}
\]

Under (0.2), (1.12) gives \(b_q\ge b_{\min}\gg\sqrt m\). Hence

\[
 R_q<p=o(N_q/\sqrt m)
\tag{6.6}
\]

uniformly. If

\[
 \Delta_0+D_0=o(p/\sqrt m),
\]

then (6.5) forces

\[
 \boxed{
 N_q-|\mathcal S_q(F)|=o(N_q/\sqrt m)
 \quad\hbox{at every band rank}.}
\tag{6.7}
\]

This support property is necessary, not sufficient: it does not select the
occurrences in one common system of tight rows.

---

## 7. What active-row no-recycling gives after segmentation

The active-row moves remain literal on the segmented object. For every
full factor row \(C\), let \(z_{C,q}\) be the indicator of the
\(G b_q\) marked rank-\((m+q)\) targets carried by its \(G\) blocks. A
coordinate transposition transports both the row and its marked block
positions. A signing of genuine ownership components therefore produces
another exact factor carrying the same number of legitimate atom blocks.

For rank \(r_q=m+q\), put

\[
 \mathfrak d_q=r_q(n-r_q)=(m+q)(m+1-q).
\tag{7.1}
\]

For a transposition \(\tau\), define the selected-row effects exactly as
in the active-row theorem:

\[
 \widetilde R_{\tau,q}
 =\sum_C\|z_{C,q}-\tau z_{C,q}\|_2^2,
\tag{7.2}
\]

\[
 \widetilde A_{\tau,q}
 =\|\lambda_q-\tau\lambda_q\|_2^2,
\tag{7.3}
\]

and, summing rows inside each genuine ownership component \(K\),

\[
 \widetilde V_{\tau,q}
 =\sum_K
 \left\|\sum_{C\in K}(z_{C,q}-\tau z_{C,q})\right\|_2^2.
\tag{7.4}
\]

The target-charging proof of active-row no-recycling applies verbatim and
gives

\[
 \boxed{
 \sum_\tau
 (\widetilde V_{\tau,q}-\widetilde R_{\tau,q})_+
 \le4\mathfrak d_q\widetilde\Pi_q.}
\tag{7.5}
\]

For an arbitrary family of \(k\) distinct rank-\(r_q\) sets,

\[
 \sum_\tau\|\mathbf1_{\mathcal A}
                  -\tau\mathbf1_{\mathcal A}\|_2^2
 \le2k\mathfrak d_q,
\]

because each selected target is moved by exactly \(\mathfrak d_q\)
transpositions, and a leaving target is counted on both shores of the
symmetric difference. Summing over rows, whose total marked mass is

\[
 T_q=s_0b_q,
\]

gives

\[
 \sum_\tau\widetilde R_{\tau,q}
 \le2\mathfrak d_qT_q.
\tag{7.6}
\]

Combining (7.5)--(7.6),

\[
 \boxed{
 \sum_\tau\widetilde V_{\tau,q}
 \le2\mathfrak d_qT_q
    +4\mathfrak d_q\widetilde\Pi_q.}
\tag{7.7}
\]

This is a valid selected-row no-recycling theorem. It is not the desired
descent theorem.

### The coefficient obstruction at a selected-collision local minimum

Because \(s_0\le p\),

\[
 T_q=s_0b_q\le pb_q\le N_q.
\tag{7.8}
\]

The selected collision energy is

\[
 \widetilde Q_q
 =\sum_S\lambda_q(S)(\lambda_q(S)-1)
 =2\widetilde\Pi_q.
\tag{7.9}
\]

Fair component signs satisfy the exact antipodal identity

\[
 \mathbb E
 [\widetilde Q_q(F)-\widetilde Q_q(F_\varepsilon)]
 =\frac{\widetilde A_{\tau,q}
       -\widetilde V_{\tau,q}}4.
\tag{7.10}
\]

Even grant a factor which is cut-local for this one-rank objective. Then
\(\widetilde A_{\tau,q}\le\widetilde V_{\tau,q}\) for every \(\tau\).
Let

\[
 f_q=\lambda_q-\frac{T_q}{N_q}\mathbf1.
\]

The exact Johnson transposition spectrum gives

\[
 \sum_\tau\widetilde A_{\tau,q}
 =2\sum_{j\ge1}j(n-j+1)\|P_jf_q\|_2^2
 \ge2n\|f_q\|_2^2.
\tag{7.11}
\]

Moreover,

\[
 \begin{aligned}
 \|f_q\|_2^2
 &=\sum_S\lambda_q(S)^2-\frac{T_q^2}{N_q}\\
 &=2\widetilde\Pi_q
   +T_q\left(1-\frac{T_q}{N_q}\right)
 \ge2\widetilde\Pi_q.
 \end{aligned}
\tag{7.12}
\]

Consequently the strongest direct combination of cut-locality,
(7.7), and the generic spectrum is only

\[
 \boxed{
 4n\widetilde\Pi_q
 \le2\mathfrak d_qT_q
    +4\mathfrak d_q\widetilde\Pi_q.}
\tag{7.13}
\]

This supplies no upper bound because
\(\mathfrak d_q=\Theta(m^2)\) while \(n=\Theta(m)\).

Even if one separately proves exact point margins for the marked profile,
so that \(P_1f_q=0\), (7.11) improves only to

\[
 \sum_\tau\widetilde A_{\tau,q}
 \ge4(n-1)\|f_q\|_2^2
 \ge8(n-1)\widetilde\Pi_q.
\tag{7.14}
\]

The coefficient \(4\mathfrak d_q\) in (7.7) is still larger by order
\(m\). Thus the sharp zero-point-margin spectral correction does not
repair the selected-collision comparison.

There are two further losses relative to the full active-row theorem:

1. the exact full-row boundary identity
   \(\sum_\tau R_{\tau,q}=2W(\mathfrak d_q-2)\) becomes only (7.6);
2. the general alternating-path identity still applies to selected
   submatchings, but selection does not preserve the maximum-load
   saturated specialization, zero high--high restitution, exact point
   margins, or forced \(1\)-design Johnson boundary used in the positive
   saturated branch.

Accordingly, no proved active-row inequality forces (6.3).

---

## 8. Exact saturated-support obstruction

The failure of the saturated branch is stronger than the coefficient
comparison.

Use the active-row depth notation at rank \(m-1\). Suppose

\[
 \mu_1=M\mathbf1_{\mathcal A},
 \qquad
 M=\left\lfloor\frac{m+2}{2}\right\rfloor.
\tag{8.1}
\]

Since the total number of cyclic first-shadow occurrences is \(W\),

\[
 |\mathcal A|=\frac WM.
\tag{8.2}
\]

Every rank-\((m-1)\) target of every atom cut from this factor lies in
\(\mathcal A\). By (1.15), every proportional atom contains exactly
\(b-1\) distinct targets at that rank. Therefore every factor-contained
atom matching of size \(s\) satisfies

\[
 s(b-1)\le\frac WM.
\tag{8.3}
\]

This proves

\[
 \boxed{
 s\le\left\lfloor\frac{W}{M(b-1)}\right\rfloor
 =(1+o(1))\frac pM.}
\tag{8.4}
\]

As \(M\sim m/2\),

\[
 p-s=(1-o(1))p.
\tag{8.5}
\]

Thus the saturated factor violates the necessary support condition (6.7)
by a linear amount. The active-row saturated theorem is a constructive
energy escape conditional on split and survival; it is not an atom-
extraction theorem. Repeated children might conceivably leave the saturated
regime and acquire large support, but no such convergence theorem has been
proved.

There is also a baseline warning in the opposite, perfectly supported
case. Among all integer first-shadow histograms of total mass \(W\) on

\[
 N_{-1}=\frac m{m+2}W
\]

targets, the minimum ordinary pair collision is attained by loads in
\(\{1,2\}\) and equals

\[
 \Pi_1^{\min}=W-N_{-1}=\frac{2W}{m+2}.
\tag{8.6}
\]

Relative to the atom leave scale,

\[
 \boxed{
 \frac{\Pi_1^{\min}}{p/\sqrt m}
 =(2+o(1))\eta\to\infty.}
\tag{8.7}
\]

Hence charging one atom deletion to every collision of the **full** factor
cannot work even for a floor-perfect factor. One must resolve the
\(c_q\)-fold owner packets by selecting occurrences synchronously; full-
histogram collision reduction is not that selection.

---

## 9. A terminal full-energy bound would still miss the support scale

At the first lower shadow the exact floor is \(c_1=1\), and the active-row
floor energy is

\[
 Q_1(F)=\sum_S(\mu_1(S)-1)(\mu_1(S)-2).
\tag{9.1}
\]

If \(h_1\) targets are unsupported, every hole contributes exactly two,
so

\[
 Q_1(F)\ge2h_1.
\tag{9.2}
\]

Even grant the stronger conclusion, not proved by active-row no-recycling,

\[
 Q_1(F)\le C H\mathsf T.
\tag{9.3}
\]

Then only

\[
 h_1=O(H\mathsf T)
 =O\!\left(\frac{\omega W}{\sqrt m}\right)
\tag{9.4}
\]

follows, while (6.7) requires

\[
 h_1=o(W/\sqrt m).
\tag{9.5}
\]

The factor \(\omega\to\infty\) is in the wrong direction. Even the
formal conversion \(h_1/b\) to a segment count would give only

\[
 O\!\left(\frac{\omega\mathsf T}{\eta}\right),
\]

whereas

\[
 p/\sqrt m=(2+o(1))\frac{\mathsf T}{\eta}.
\tag{9.6}
\]

Thus an \(O(H\mathsf T)\) terminal ledger would not prove the required
little-\(o\) atom leave.

The fixed-window quantifier is not the decisive issue. The combinatorial
target-charging identities are valid depthwise for \(H=o(m)\). The shallow
chronology comparison in the active-row theorem was stated for fixed
\(A\), with

\[
 \Gamma_A=81e^{2(A+3)^2},\qquad
 \delta_m=\Gamma_AQ_0^4\frac{\mathsf T}{n},
 \qquad Q_0=\lfloor m^{1/8}\rfloor.
\tag{9.7}
\]

One may choose \(\omega(m)\) staircase-slowly so every fixed-\(A\)
threshold is respected. Even under the provisional substitution
\(A=\omega\),

\[
 \frac{\delta_m}{p/\sqrt m}
 =O\!\left(
 \frac{\eta e^{2(\omega+3)^2}}{\sqrt m}\right)=o(1)
\tag{9.8}
\]

under (0.1)--(0.2), after taking the diagonal sufficiently slowly.
Therefore the shallow chronology error can be made smaller than the atom
leave. What remains missing is the support/occurrence-resolution theorem,
not a better choice of \(\omega\).

---

## 10. Conventional matching ledgers remain out of range

The smaller rank (2.5) does not put a standard growing-rank matching
theorem in range. From (2.6),

\[
 \log E=(1+o(1))m\log m,
 \qquad
 \log D=(1+o(1))m\log m.
\tag{10.1}
\]

Even after hypothetically removing every cover codegree, the explicit pair
in (3.8) gives

\[
 \frac{C_*}{D}\ge\frac{2+o(1)}{m^2}.
\tag{10.2}
\]

Hence the standard growing-rank hypothesis

\[
 e^{2\kappa}C_*\log D=o(D)
\]

fails exponentially, since

\[
 \log\left(e^{2\kappa}\frac{C_*}{D}\log D\right)
 =2\sqrt\pi\,m\eta-\log m+O(\log\log m)
 \longrightarrow\infty.
\tag{10.3}
\]

With the genuine cover pairs, \(C_*/D\ge(2+o(1))/m\), which is worse.

An independently retained residual also dies too early. If every target
vertex is kept with probability \(z\), its expected surviving atom count
is \(Ez^\kappa\). The threshold \(z_*\) defined by \(Ez_*^\kappa=1\)
satisfies

\[
 -\log z_*
 =\frac{\log E}{\kappa}
 =(1+o(1))\frac{\log m}{\sqrt\pi\,\eta},
\tag{10.4}
\]

so

\[
 \boxed{
 z_*=m^{-1/(\sqrt\pi\eta)+o(1/\eta)}
 \gg m^{-1/2}.}
\tag{10.5}
\]

At the required residual density \(z=m^{-1/2}\),

\[
 \log(Ez^\kappa)
 =-\left(\frac{\sqrt\pi}{2}+o(1)\right)
   m\eta\log m\to-\infty.
\tag{10.6}
\]

Thus neither near-regularity nor an independent-residual nibble supplies
the matching leave.

There is a separate aggregate-collision route: the complete-column twin
rounding theorem gives a literal \(W+o(W)\) word if its invariant two-cover
pair floor is \(B=o(W)\). Near-divisor cutting and its
\(O(WH/b)=o(W)\) signing action are already valid in the present scale.
But active-row no-recycling proves neither \(B=o(W)\) nor an exact factor
with first-shadow duplicate excess \(o(W)\). This weaker constant-one route
therefore remains conditional as well; it does not turn (7.7) into (6.3).

---

## 11. Clean final lemma and proved/conditional boundary

### Theorem 11.1 (slow-window exact-factor extraction criterion)

Assume

\[
 1\ll\omega\ll\eta\ll\log m,
 \qquad e^{\omega^2}\ll\eta,
\]

take \(H=\lceil\sqrt m\omega\rceil\), and choose \(G,b\) by (5.1).
For every exact factor \(F\), choose roots and orientations and form the
\(s_0\) proportional atoms of Theorem 5.1.

If the choices and a sequence of literal exact-factor component switches
can be made so that

\[
 \sum_{q=-H}^{H+1}\sum_S
 \binom{\lambda_q(S)}2
 =o(p/\sqrt m),
\tag{11.1}
\]

then

\[
 \nu(2m+1)\le W+o(W).
\tag{11.2}
\]

Conversely, any matching obtained by deleting
\(o(p/\sqrt m)\) atoms from a segmented family carried by a final factor
\(F_{\rm fin}\) must satisfy

\[
 N_q-|\mathcal S_q(F_{\rm fin})|=o(N_q/\sqrt m)
\tag{11.3}
\]

at every band rank.

#### Proof

Theorem 5.1 loses \(\Delta_0=o(p/\sqrt m)\) atoms before collision
resolution. Lemma 6.1 and (11.1) delete another \(o(p/\sqrt m)\), producing
a matching of size \(p-o(p/\sqrt m)\). Equations (4.4), (4.7), and (4.10)
then give a literal contiguous-OR word of length \(W+o(W)\). The converse
is (6.5)--(6.7). \(\square\)

### Audited boundary

The following are proved.

1. All proportional floors, the sharp atom-rank constant \(\sqrt\pi\),
   the degree estimate, and the exact fractional matching remain valid on
   the slow product-SCD window.
2. The literal row collar, floor repair, unmatched-edge repair, and outer
   tail are all \(o(W)\) under the displayed scales.
3. A near-divisor choice of \(b\) cuts every exact factor into
   \(p-o(p/\sqrt m)\) central-disjoint proportional atoms.
4. The selected-row form (7.5)--(7.7) of active-row no-recycling is legal
   and integral.
5. The saturated active-row branch is quantitatively incompatible with
   direct factor-contained atom extraction, by (8.4).

The following are not proved.

1. No theorem gives (11.1), or even the necessary support estimate
   (11.3), after active-row descent.
2. The \(\Theta(m^2)\) target-recycling coefficient in (7.7) prevents the
   current local-minimum argument from bounding selected collisions at the
   \(o(p/\sqrt m)\) scale.
3. The general star-path identity transfers to thinned columns, but its
   maximum-load saturated specialization, zero high--high restitution,
   and forced design boundary do not follow for the selected profiles.
4. No conventional growing-rank matching theorem or independent-residual
   argument fills this gap.

Therefore the active-row no-recycling theorem, as presently proved, does
not give the required atom leave after the slow-window reparameterization.
The exact missing positive statement is (11.1), or a stronger synchronized
packet-resolution theorem implying it while preserving one common system
of literal tight rows.

### Independent audit record

The decisive steps were checked independently in two audits.

1. The floor/degree/overlap/matching audit verified (1.5), (1.7)--(1.12),
   the \(\sqrt\pi\) constant in (2.5), codegrees (3.6) and (3.8), the
   \(4H+3\) band constant, the factor \(2L_m(m-H-1)\), (4.10), the
   exponent in (10.3), and the residual threshold (10.5). Its four local
   corrections—zero-quota inequality strictness, the \(\varepsilon\)
   estimate in (1.15), explicit nestedness in (3.9a), and the distinction
   between actual and worst-case floor remainder—are incorporated above.
2. The exact-factor audit verified Theorems 5.1 and 6.1, equations
   (7.5)--(7.14), and the saturated bound (8.4). Its scope corrections—the
   survival of the general star identity, failure only of its saturated
   specialization, and application of (11.3) to the final carrier—are also
   incorporated above.

No remaining mathematical error was reported in the stated conclusions.
