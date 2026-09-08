# Pair-omission tokens: exact positive cross-Gram for adjacent-priority run charts

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
long-running job is used.

## 0. Outcome

This note computes the joined-owner Gram form for one explicit
block-correlated interpolation between two different low-run
first-avoided-pair matchings.

Let

\[
 n=2m+1,
 \qquad P_1,\ldots,P_m
\]

be disjoint coordinate pairs, with one coordinate left over.  Fix adjacent
priorities

\[
 A=P_j,\qquad B=P_{j+1},
\]

and let \(\theta\) exchange the two coordinates of \(A\) with the two
coordinates of \(B\), in a fixed pairing, while fixing every other
coordinate.  Choose an exact local factor \(F_A\) on \([n]\setminus A\)
and take

\[
 F_B=\theta F_A.
\]

Compare the first-avoided matchings for the two priority orders

\[
 \cdots,A,B,\cdots
 \qquad\hbox{and}\qquad
 \cdots,B,A,\cdots .
\]

Their difference domain is exactly

\[
 \mathcal D_j={S:|S|=m-1,\ S\cap(A\cup B)=\varnothing,
                   \ S\cap P_h\ne\varnothing\ (h<j)\}.
\tag{0.1}
\]

The overlay on this domain splits into one-lower-vertex alternating paths
or parallel two-cycles.  Consequently arbitrary choices of the two phases
remain a central matching.  Correlate those choices by assigning one bit to
each maximal consecutive \(\mathcal D_j\)-run in a physical row of
\(F_A\).  This gives an exact long-block atlas, not tokenwise rounding.

For \(1\le q\le H\le m-2\), let \(w_q^-,w_q^+>0\) be arbitrary lower
and upper depth weights.  In the eventual full-word energy one may take
\(w_q^\pm=1/c_q^\pm\), where the denominators are computed from the full
word mass \(W\) and are positive.  One must not form an autonomous upper
token-core floor at \(q=1\): its mass is
\(\binom n{m-1}<\binom n{m+1}=W\), so that denominator would be zero.
The Gram theorem itself has no such singularity because it is stated for
positive weights.  If \(d_S\) is the complete signed flag innovation of
the token at \(S\in\mathcal D_j\), then

\[
 \boxed{
 \langle d_S,d_T\rangle_H
 =2\sum_{q=1}^Hw_q^+
   {\bf1}_{\{U_q(S)=U_q(T),\ U_q(S)\cap B\ne\varnothing\}}
 \ge0.}
\tag{0.2}
\]

Every lower-depth contribution is zero.  Moreover different starts of one
physical row have different \(U_q\)'s.  Hence grouping an arbitrarily long
run loses **no** variance:

\[
 \boxed{
 \left\|\sum_{S\in I}d_S\right\|_H^2
 =\sum_{S\in I}\|d_S\|_H^2}
\tag{0.3}
\]

for every run block \(I\).  If

\[
 \mu_{q,U}=|\{S\in\mathcal D_j:U_q(S)=U\}|,
\tag{0.4}
\]

and \(\mathfrak A_j,\mathfrak V_j\) denote respectively the coherent
distance and the independent-run variance of this atlas, then

\[
 \boxed{
 \begin{aligned}
 \mathfrak A_j
 &=2\sum_{q=1}^Hw_q^+
   \sum_{U:U\cap B\ne\varnothing}\mu_{q,U}^2,\\
 \mathfrak V_j
 &=2\sum_{q=1}^Hw_q^+
   \sum_{U:U\cap B\ne\varnothing}\mu_{q,U},\\
 \mathfrak A_j-\mathfrak V_j
 &=2\sum_{q=1}^Hw_q^+
   \sum_{U:U\cap B\ne\varnothing}\mu_{q,U}(\mu_{q,U}-1).
 \end{aligned}}
\tag{0.5}
\]

Thus every activated duplicate has the correct, strictly positive joined
Gram sign.  Fair independent run bits lower the average of the two coherent
endpoint energies by exactly

\[
 \frac12\sum_{q=1}^Hw_q^+
   \sum_{U:U\cap B\ne\varnothing}\mu_{q,U}(\mu_{q,U}-1).
\tag{0.6}
\]

There is also a genuinely overlapping repair which uses a different
partner pair for each occurrence of one common upper spike.  For every
\(q\le H\) and every \(s\) with \(s(q+1)\le m+q\), Proposition 7.2 builds
literal innovations \(d_1,\ldots,d_s\) with

\[
 \boxed{
 \|d_i\|_H^2=2\sum_{p=1}^Hw_p^+,
 \qquad
 \langle d_i,d_k\rangle_H=\sum_{p=q}^Hw_p^+\quad(i\ne k).}
\tag{0.6a}
\]

Thus

\[
 \boxed{
 \mathfrak A-\mathfrak V
 =s(s-1)\sum_{p=q}^Hw_p^+>0}
\tag{0.6b}
\]

after releasing at most \(2s\) lower endpoints and adding only \(O(s)\)
row boundaries.  With
\(s=\lfloor(m+q)/(q+1)\rfloor\), its exact curvature per boundary is of
order

\[
 \frac mq\sum_{p=q}^Hw_p^+.
\tag{0.6c}
\]

This explicitly burns the disjoint-missing collision which no
single-common-partner chart can see.

The number of run variables is at most

\[
 \boxed{2j\operatorname{Cat}_{m-1}.}
\tag{0.7}
\]

In particular it is \(o(W/H)\) whenever \(jH=o(m)\), because

\[
 \frac{\operatorname{Cat}_{m-1}}W
 =\frac{m(m+1)}{(2m-1)(2m)(2m+1)}.
\tag{0.8}
\]

This proves a genuine positive-along-rows, repulsive-across-equal-targets
rounding block.  It does not by itself prove constant one.  Its exact
remaining coverage boundary is stated in Section 7: the chart is identically
zero on all lower flags and on upper flags avoiding \(B\).  A full theorem
must recombine several pair swaps, including a dual lower-flag atlas; one
adjacent chart cannot span the full signed defect space.

All adjacent charts may be placed at one common base.  Choose \(F_{P_1}\)
arbitrarily and, successively, set

\[
 F_{P_{j+1}}=\theta_jF_{P_j}\qquad(1\le j<m),
\tag{0.9}
\]

where \(\theta_j\) exchanges \(P_j,P_{j+1}\).  Then the theorem applies
simultaneously as a menu of \(m-1\) separate charts based at the same
first-avoided matching.  For the first \(t\) adjacent positions their total
number of run variables is at most

\[
 \sum_{j=1}^t2j\operatorname{Cat}_{m-1}
 =t(t+1)\operatorname{Cat}_{m-1}.
\tag{0.10}
\]

Consequently the whole first-\(t\) menu has cumulative catalog size
\(o(W/H)\)
provided

\[
 Ht^2=o(m).
\tag{0.11}
\]

In particular \(t=O(\log m)\) is admissible throughout
\(H=O(\sqrt{m\log m})\).

This is a menu of separate cubes sharing one endpoint, not one joint cube:
no simultaneous choice of bits belonging to different adjacent positions
is asserted.

## 1. The two first-avoided endpoints differ on exactly one domain

For a cyclic row

\[
 \pi=(x_0,\ldots,x_{2m-2})
\]

in a local factor, use the token convention

\[
 S_i=I_\pi(i,m-1),\qquad Y_i=I_\pi(i-1,m),
\tag{1.1}
\]

and

\[
 L_q(i)=I_\pi(i+q-1,m-q),\qquad
 U_q(i)=I_\pi(i-1,m+q).
\tag{1.2}
\]

Let \(M^-\) be the first-avoided matching for the order with \(A\) before
\(B\), and let \(M^+\) use the order with \(B\) before \(A\).  Use the same
factor attached to every pair in both constructions, in particular
\(F_B=\theta F_A\).

### Lemma 1.1 (exact difference domain)

A lower target changes its assigned phase between \(M^-\) and \(M^+\) if
and only if it lies in \(\mathcal D_j\).  Such a target moves from phase
\(A\) in \(M^-\) to phase \(B\) in \(M^+\).

#### Proof

A target meeting every earlier pair is assigned to \(A\) before the swap
if it avoids \(A\).  After the swap it is assigned to \(B\) precisely when
it also avoids \(B\).  If it avoids \(A\) but meets \(B\), it remains in
phase \(A\).  The symmetric statement holds for a target which avoids
\(B\) and meets \(A\); it remains in phase \(B\).  Targets failing an
earlier pair, or meeting both \(A,B\), are unaffected.  This is exactly
(0.1). \(\square\)

For \(S\in\mathcal D_j\), let \(e_A(S)\) be its token in \(F_A\).  If it
occurs at start \(i\) in a row \(\pi\), then \(S\cap(A\cup B)=\varnothing\)
gives

\[
 \theta S=S.
\tag{1.3}
\]

The row \(\theta\pi\) belongs to \(F_B\), and the same start has lower
window \(S\).  Hence the phase-\(B\) token is exactly

\[
 \boxed{e_B(S)=\theta e_A(S).}
\tag{1.4}
\]

## 2. The overlay has singleton owner components

### Lemma 2.1 (arbitrary phase choices remain a matching)

The symmetric difference of \(M^-\) and \(M^+\), restricted to
\(\mathcal D_j\), is a disjoint union of alternating paths with one lower
vertex and of parallel two-cycles.  In particular, for every subset
\(E\subseteq\mathcal D_j\), replacing \(e_A(S)\) by \(e_B(S)\) exactly for
\(S\in E\) preserves both lower saturation and middle injectivity.

#### Proof

Lower endpoints are unchanged.  It remains to check that two different
lower targets cannot be joined through a common middle endpoint across the
two phases.  Suppose

\[
 Y_A(S)=Y_B(T)=\theta Y_A(T).
\tag{2.1}
\]

The left side avoids \(A\), while the right side avoids \(B\).  Their common
value therefore avoids both pairs and is fixed by \(\theta\).  Applying
\(\theta\) to (2.1) gives

\[
 Y_A(S)=Y_A(T).
\]

The length-\(m\) windows of one exact local factor are all distinct, so
\(S=T\).  Thus a common middle endpoint can occur only between the two
tokens belonging to the same lower target.  Otherwise both middle endpoints
are private to that one lower vertex.  This proves the component assertion
and arbitrary-choice legality. \(\square\)

This lemma is the common-base fact needed for block correlation.  The
blocks below are correlations among already independent literal alternating
components; no fractional or nonphysical interpolation is introduced.

## 3. Exact tokenwise cross-Gram

Let \(\mathcal H_H\) be the orthogonal direct sum of all lower and upper
flag-coordinate spaces through depth \(H\), with

\[
 \|v\|_H^2
 =\sum_{q=1}^H
   \bigl(w_q^-\|v_q^-\|_2^2+w_q^+\|v_q^+\|_2^2\bigr).
\tag{3.1}
\]

Write \(\phi_A(S),\phi_B(S)\) for the stacked unit flag vectors of the two
tokens and put

\[
 d_S=\phi_B(S)-\phi_A(S).
\tag{3.2}
\]

Since every lower flag is contained in \(S\), (1.3)--(1.4) give

\[
 L_q(e_B(S))=\theta L_q(e_A(S))=L_q(e_A(S)).
\tag{3.3}
\]

Thus

\[
 (d_S)_q^-=0,
 \qquad
 (d_S)_q^+
 =\delta_{\theta U_q(S)}-\delta_{U_q(S)},
\tag{3.4}
\]

where from now on \(U_q(S)=U_q(e_A(S))\).

The following elementary identity supplies the sign.

### Lemma 3.1 (pair-swap unit-vector identity)

For subsets \(T,T'\subseteq[n]\setminus A\),

\[
 \boxed{
 \left\langle
  \delta_{\theta T}-\delta_T,
  \delta_{\theta T'}-\delta_{T'}
 \right\rangle
 =2{\bf1}_{\{T=T',\ T\cap B\ne\varnothing\}}.}
\tag{3.5}
\]

#### Proof

Expansion gives

\[
 2{\bf1}_{\{T=T'\}}
 -{\bf1}_{\{\theta T=T'\}}
 -{\bf1}_{\{T=\theta T'\}}.
\tag{3.6}
\]

If \(T=T'\) and \(T\cap B=\varnothing\), then \(T\) avoids both \(A\)
and \(B\), so \(\theta T=T\), and (3.6) is zero.  If \(T=T'\) meets
\(B\), then \(T\) avoids \(A\) whereas \(\theta T\) meets \(A\), so the
two negative indicators vanish and (3.6) is two.

Finally, if \(T=\theta T'\), then the left side avoids \(A\), while the
right side avoids \(B\).  Hence the common set avoids both pairs, is fixed
by \(\theta\), and satisfies \(T=T'\).  This is exactly the already counted
zero case.  The other cross equality is identical. \(\square\)

Combining (3.4)--(3.5), and using orthogonality of different ranks, proves
(0.2).

## 4. Long physical blocks lose no curvature

In each row \(\pi\) of \(F_A\), break the starts belonging to
\(\mathcal D_j\) into maximal consecutive intervals.  Call the resulting
family \(\mathscr I_j\).  The corresponding starts in \(\theta\pi\) form
the identical intervals, because their lower windows are fixed pointwise by
\(\theta\).

For \(I\in\mathscr I_j\), define the block innovation

\[
 z_I=\sum_{S\in I}d_S.
\tag{4.1}
\]

Assign one sign to every \(I\): one sign uses all phase-\(A\) tokens on the
interval and the other uses all phase-\(B\) tokens.  Lemma 2.1 shows that
every sign vector is a literal central matching.

### Lemma 4.1 (exact within-block orthogonality)

For every \(I\in\mathscr I_j\),

\[
 \|z_I\|_H^2=\sum_{S\in I}\|d_S\|_H^2.
\tag{4.2}
\]

#### Proof

For fixed \(q\le H\le m-2\), the sets \(U_q(S)\) along one cyclic row are
the length-\((m+q)\) cyclic windows.  Their length is strictly less than
the row length \(2m-1\), so distinct starts give distinct targets.  Equation
(0.2) therefore makes \(d_S\) and \(d_T\) orthogonal whenever \(S,T\) are
different starts in the same row.  Summing gives (4.2). \(\square\)

This is the point at which block correlation and target repulsion cease to
compete: an interval may be arbitrarily long, yet it introduces no internal
joined variance beyond the tokenwise variance.

## 5. Exact Haar drift and activated collision curvature

Put

\[
 \mathfrak A_j=\left\|\sum_{I\in\mathscr I_j}z_I\right\|_H^2,
 \qquad
 \mathfrak V_j=\sum_{I\in\mathscr I_j}\|z_I\|_H^2.
\tag{5.1}
\]

For a target \(U\) of upper rank \(m+q\), define \(\mu_{q,U}\) by (0.4).
Equation (0.2) gives

\[
 \mathfrak A_j
 =2\sum_{q=1}^Hw_q^+
   \sum_{U:U\cap B\ne\varnothing}\mu_{q,U}^2.
\tag{5.2}
\]

Lemma 4.1 says that each occurrence contributes separately to
\(\mathfrak V_j\), so

\[
 \mathfrak V_j
 =2\sum_{q=1}^Hw_q^+
   \sum_{U:U\cap B\ne\varnothing}\mu_{q,U}.
\tag{5.3}
\]

Subtraction proves all of (0.5).

Let \(f^-\) and \(f^+\) be the two coherent endpoint load profiles,
including the common tokens outside \(\mathcal D_j\).  A fair independent
sign \(\varepsilon_I\in\{-1,+1\}\) on each run has profile

\[
 f_\varepsilon
 =\frac{f^-+f^+}{2}
  +\frac12\sum_{I\in\mathscr I_j}\varepsilon_Iz_I.
\tag{5.4}
\]

Independence kills cross terms, whence

\[
 \mathbb E\|f_\varepsilon\|_H^2
 =\left\|\frac{f^-+f^+}{2}\right\|_H^2
  +\frac{\mathfrak V_j}{4}.
\tag{5.5}
\]

The average coherent endpoint norm is

\[
 \frac{\|f^-\|_H^2+\|f^+\|_H^2}{2}
 =\left\|\frac{f^-+f^+}{2}\right\|_H^2
  +\frac{\mathfrak A_j}{4}.
\tag{5.6}
\]

Every corner has the same number of flags at every signed depth.  Therefore
all fixed linear terms are corner-independent.  Equations (5.5)--(5.6)
therefore apply to every positive weighted quadratic defect.  After the
token core is completed to a full word, they also apply exactly to the
adjacent-integer floor energy with the full-word denominators
\(w_q^\pm=1/c_q^\pm\).  No autonomous \(q=1\) upper token-core floor is
being invoked.  Their difference, together with (0.5), is precisely (0.6).
For the autonomous token statement below, \(\mathcal Q_w\) denotes instead
the doubled factorial floor excess

\[
 \mathcal Q_w(M)
 =2\sum_qw_q^+\left[
   \sum_U\binom{\mu_q^M(U)}2-P_{q,\min}\right]
\]

plus the unchanged lower contribution.  This definition remains valid at
the first upper rank, where the token quotient is \(c_1^+=0\) and
\(P_{1,\min}=0\).

In particular, if

\[
 \mathcal C_j=\frac12\sum_{q=1}^H w_q^+
   \sum_{U:U\cap B\ne\varnothing}\mu_{q,U}(\mu_{q,U}-1),
\]

then some literal runwise corner satisfies

\[
 \mathcal Q_w(M_\varepsilon)
 \le \mathcal Q_w(M^-)-\mathcal C_j
 =\mathcal Q_w(M^+)-\mathcal C_j.
\]

Here the endpoint equality is rankwise and floor-exact.  Every upper flag
has the same first-avoided category as its lower endpoint.  The union of
the \(A\)- and \(B\)-target strata is disjoint from the other strata, and
\(\theta\) permutes the complete endpoint load on that union; lower loads
are identical and middle loads are injective.  Thus the global
pair-symmetric swap is energy-flat, while the independently mixed interval
corner is not a global coordinate image.  Equivalently, the global bit has
variance \(\mathfrak A_j\), whereas the interval bits have variance
\(\mathfrak V_j\); their difference is exactly the activated duplicate
descent above.

If a later common completion is not \(\theta\)-symmetric on the affected
stratum, the average-versus-endpoints identity remains exact but the two
completed endpoint energies need not be equal.  The displayed descent
below both endpoints is asserted for the autonomous token matching, or for
a completion preserving that stratum symmetry.

## 6. Exact run accounting

The number of rows of one local factor on \(2m-1\) coordinates is

\[
 R_m=\frac1{2m-1}\binom{2m-1}{m-1}
 =\operatorname{Cat}_{m-1}.
\tag{6.1}
\]

In one row of \(F_A\), membership in \(\mathcal D_j\) says that the
length-\((m-1)\) window meets each of \(P_1,\ldots,P_{j-1}\) and avoids
both coordinates of \(B\).  For one coordinate pair, the starts whose
window avoids the pair form at most two circular intervals.  Consequently
the boundary set for all \(j\) conditions has at most \(4j\) changes, and
the selected set has at most \(2j\) circular components.  Thus

\[
 |\mathscr I_j|\le2j\operatorname{Cat}_{m-1},
\tag{6.2}
\]

which is (0.7).

Turning one block from its \(A\)-phase to its \(B\)-phase can split the
selected set in the old row at at most two endpoints and creates one
interval in the paired new row.  Hence its run-boundary charge is bounded
by two.  In particular

\[
 J(M_\varepsilon)-J(M^-)
 \le2|\mathscr I_j|
 \le4j\operatorname{Cat}_{m-1}.
\tag{6.2a}
\]

Finally,

\[
 \operatorname{Cat}_{m-1}
 =\frac{(2m-2)!}{m!(m-1)!},
 \qquad
 W=\binom{2m+1}{m},
\]

and direct division gives (0.8).  Therefore

\[
 \frac{H|\mathscr I_j|}{W}
 \le
 \frac{2jHm(m+1)}{(2m-1)(2m)(2m+1)}
 =O\!\left(\frac{jH}{m}\right).
\tag{6.3}
\]

This tends to zero under the exact condition \(jH=o(m)\).

There is also a uniform count for the complete adjacent-swap menu.  Let
\(N_j\) be the number of lower targets whose first avoided pair is
\(P_j\).  The first-avoided tail estimate gives, for an absolute constant
\(C\),

\[
 N_j\le C\sqrt m\binom{2m-1}{m-1}(3/4)^{j-1}.
\tag{6.4}
\]

Since \(|\mathcal D_j|\le N_j\), the number of nonempty run blocks is at
most \(N_j\).  With \(t=\lceil20\log m\rceil\), (6.2)--(6.4) yield

\[
 \begin{aligned}
 \sum_{j=1}^{m-1}|\mathscr I_j|
 &\le 2\operatorname{Cat}_{m-1}\sum_{j\le t}j
       +\sum_{j>t}N_j\\
 &=O\!\left(\frac{W\log^2m}{m}\right)+O(Wm^{-2})\\
 &=O\!\left(\frac{W\log^2m}{m}\right).
 \end{aligned}
\tag{6.5}
\]

The displayed \(O(Wm^{-2})\) is deliberately weaker than the exponent
obtained directly from \(20\log(4/3)>5\).  Therefore the cumulative
carrier catalog of all separate adjacent charts has

\[
 \boxed{
 \sum_j|\mathscr I_j|=o(W/H)}
\tag{6.6}
\]

uniformly whenever \(H=o(m/\log^2m)\), in particular throughout the
Gaussian range used in the token reduction.

This is not the boundary count of a product cube: mutual middle
disjointness between alternatives from different adjacent charts has not
been proved.

## 7. Proved boundary and the next exact statement

The theorem above is a genuine positive curvature theorem with the required
predecessor correlation: inside every maximal physical run the conditional
probability of retaining the predecessor is one, and only the
\(O(j\operatorname{Cat}_{m-1})\) endpoints can fail it.  At the same time,
equal activated upper targets are repulsive through the strictly positive
term (0.5).

It is not a full multidepth contraction theorem.  Two invariant sectors are
visible directly in the exact formula:

1. every lower flag is fixed because \(L_q(S)\subseteq S\) and
   \(\theta S=S\);
2. an upper flag contained in \([n]\setminus(A\cup B)\) is fixed by
   \(\theta\).

Thus one adjacent-priority atlas cannot span every excess-energy direction.
In fact even the union of all charts which fix both lower endpoints and use
one common partner pair has an exact physical blind spot.

### Proposition 7.1 (disjoint-missing collision is invisible to a common-pair swap)

Fix \(1\le q\le m-2\).  In the coordinate-symmetric orbit token system
there are two literal tokens with distinct lower and middle endpoints and
the same upper depth-\(q\) target \(U\), such that no coordinate pair \(B\)
satisfies simultaneously

\[
 B\cap S=B\cap T=\varnothing,
 \qquad B\cap U\ne\varnothing.
\tag{7.1a}
\]

Consequently their duplicate pair occurs in none of the positive Gram sums
(0.5), even if every possible partner pair \(B\) is offered.

#### Proof

Choose an \((m+q)\)-set \(U\) and disjoint \((q+1)\)-sets

\[
 D_1,D_2\subset U;
\]

this is possible because \(2q+2\le m+q\) is equivalent to \(q\le m-2\).
Put

\[
 S=U\setminus D_1,\qquad T=U\setminus D_2.
\]

Both have size \(m-1\), and

\[
 U\setminus(S\cup T)=D_1\cap D_2=\varnothing.
\tag{7.1b}
\]

If a pair \(B\) obeyed (7.1a), an element of \(B\cap U\) would belong to
\(U\setminus(S\cup T)\), contradicting (7.1b).

It remains to certify physicality.  Choose an omitted pair
\(A\subseteq U^c\), possible because \(|U^c|=m+1-q\ge3\).  Order the
coordinates of \(U\) so that \(S\), respectively \(T\), is the central
length-\((m-1)\) window and the \(q+1\) coordinates of \(D_1\), respectively
\(D_2\), occupy its predecessor and upper-suffix positions.  Complete each
order arbitrarily on \([n]\setminus A\).  The resulting literal pair-row
tokens have upper flag \(U_q=U\).  Choosing the predecessor in \(D_i\)
gives different middle owners, since
\(D_1\setminus\{d_1\}\ne D_2\setminus\{d_2\}\).  Every prescribed cyclic
row occurs in a coordinate image of an exact local factor, so both tokens
belong to the symmetric orbit token system. \(\square\)

Proposition 7.1 does not negate the positive theorem.  It identifies the
required recombination precisely: the two occurrences must be moved with
different partner pairs and aligned through their common negative target,
or a chart must be allowed to change the lower endpoints.  A direct sum of
single-common-pair charts is not a full-mode frame.

The first of these two repairs can itself be made completely explicit.

### Proposition 7.2 (overlapping-partner chart burns a common upper spike)

Fix \(1\le q\le H\le m-2\), and let \(s\) satisfy

\[
 s(q+1)\le m+q.
\tag{7.2a}
\]

In the coordinate-symmetric orbit token system there is a partial
\(s\)-component atlas with innovations \(d_1,\ldots,d_s\) such that, with

\[
 C_H=\sum_{p=1}^Hw_p^+,
 \qquad
 C_{q,H}=\sum_{p=q}^Hw_p^+,
\tag{7.2b}
\]

one has exactly

\[
 \boxed{
 \|d_i\|_H^2=2C_H,
 \qquad
 \langle d_i,d_k\rangle_H=C_{q,H}\quad(i\ne k).}
\tag{7.2c}
\]

Consequently

\[
 \boxed{
 \mathfrak V=2sC_H,\qquad
 \mathfrak A=2sC_H+s(s-1)C_{q,H},\qquad
 \mathfrak A-\mathfrak V=s(s-1)C_{q,H}.}
\tag{7.2d}
\]

Therefore fair independent component bits lower the average of the two
coherent endpoint quadratic energies by exactly

\[
 \boxed{\frac{s(s-1)}4\,C_{q,H}.}
\tag{7.2e'}
\]

The atlas uses different partner pairs for its different components.  It
therefore has positive curvature even when the missing sets of the old
occurrences are pairwise disjoint, exactly the case missed by Proposition
7.1.  It embeds in a global matching which releases at most \(2s\) lower
vertices and adds \(O(s)\) source-row runs.  No exact lower-saturating
extension is asserted.

#### Proof

Choose an \((m+q)\)-set \(U\), an omitted phase pair \(A\subset U^c\), and
pairwise disjoint \((q+1)\)-sets

\[
 D_1,\ldots,D_s\subset U.
\]

Condition (7.2a) permits this.  Choose them so that each \(D_i\) contains
a different coordinate pair \(B_i\), and put

\[
 S_i=U\setminus D_i.
\tag{7.2e}
\]

This choice is compatible with the fixed pair partition: (7.2a) gives
\(s\le m-1\), so choose \(A,B_1,\ldots,B_s\) as distinct partition pairs,
place every \(B_i\) inside \(D_i\), extend the \(D_i\)'s disjointly to
size \(q+1\), and then fill the remaining positions of \(U\) outside \(A\).

Thus \(S_i\) avoids both \(A\) and \(B_i\).  Let \(\theta_i\) exchange
\(A\) and \(B_i\) coordinatewise and fix all other coordinates.

Order \(D_i\) with the two coordinates of \(B_i\) first.  Prescribe an old
phase-\(A\) token at \(S_i\) whose upper chain is

\[
 U_p^{(i)}=S_i\cup D_i[1,p+1]\qquad(1\le p<q),
 \qquad U_q^{(i)}=U.
\tag{7.2f}
\]

Choose a common ordered tail \(C_1,\ldots,C_{H-q}\) in
\([n]\setminus(U\cup A)\), and continue with

\[
 U_p^{(i)}=U\cup\{C_1,\ldots,C_{p-q}\}\qquad(q<p\le H).
\tag{7.2g}
\]

There are enough tail coordinates because

\[
 |[n]\setminus(U\cup A)|=m-1-q\ge H-q.
\]

Complete the cyclic row arbitrarily.  As in Proposition 7.1, every such
row occurs in an orbit copy of an exact local factor.  Take as the alternate
token \(\theta_i e_i\).  Its lower endpoint and every lower flag are fixed,
while its upper innovation is

\[
 (d_i)_p^+=\delta_{\theta_iU_p^{(i)}}-\delta_{U_p^{(i)}}.
\tag{7.2h}
\]

All prescribed old and alternate middle owners are distinct.  Indeed, old
owners avoid \(A\), alternate owners meet \(A\), and for \(i\ne k\) the
\(i\)-th alternate owner contains \(B_k\), whereas the \(k\)-th alternate
owner does not.  Hence arbitrary component choices form a literal matching.

This partial atlas embeds in a global matching with the exact relaxed
quantifiers of the clustered-token target.  Start with a clustered
first-avoided matching \(M_0\) in the symmetric orbit token system.  Delete
the \(M_0\)-edges at \(S_1,\ldots,S_s\), and also delete every remaining
\(M_0\)-edge whose middle endpoint is one of the \(2s\) prescribed old or
alternate middle owners.  Insert all \(s\) old tokens.  The resulting
matching misses at most \(2s\) lower vertices: deletion at \(S_i\) is
repaired immediately, and at most one other lower vertex was using each
reserved middle owner.  Every prescribed old/alternate owner is now absent
from the unchanged background, so every atlas corner remains a matching.
Deleting or inserting one token changes the source-row run count by at most
an absolute constant.  Thus the surgery adds \(O(s)\) runs.  Since
\(s\le m-1\), both the \(2s\) released lower vertices and the \(O(s)\)
new runs are \(o(W/H)\) in the Gaussian range.

Every \(U_p^{(i)}\) contains \(B_i\), so (7.2h) has squared norm two at
every depth.  This proves the first identity in (7.2c).  If \(p<q\), then
\(U_p^{(i)}\) contains all of \(D_k\) but omits part of \(D_i\), while
\(U_p^{(k)}\) has the reverse property.  Their old targets are distinct;
their two images are also distinct because the \(i\)-image still contains
\(B_k\), whereas the \(k\)-image does not.  Every old/image cross equality
is impossible because an image meets \(A\) and an old target avoids \(A\).
Thus

\[
 \langle(d_i)_p^+,(d_k)_p^+\rangle=0
 \qquad(p<q).
\tag{7.2i}
\]

For \(p\ge q\), the two old targets coincide by (7.2f)--(7.2g), while
their images remain distinct by the \(B_i,B_k\) test.  Hence

\[
 \langle(d_i)_p^+,(d_k)_p^+\rangle=1
 \qquad(p\ge q).
\tag{7.2j}
\]

Weighting (7.2i)--(7.2j) gives the second identity in (7.2c).  Expanding
the coherent square proves (7.2d).  Finally each component uses two
literal singleton row intervals, so the total run-boundary charge is at
most an absolute constant times \(s\). \(\square\)

Taking

\[
 s=\left\lfloor\frac{m+q}{q+1}\right\rfloor
\]

shows that the exact curvature-per-boundary ratio of this spike chart is
of order

\[
 \frac{m}{q}C_{q,H}.
\tag{7.2k}
\]

For \(q=o(m/H)\) this is already super-\(H\) when \(C_{q,H}\) is bounded
below.  The construction is therefore quantitatively capable of repairing
low and mesoscopic upper-depth spikes within the \(o(W/H)\) boundary
budget.  It does not yet pack these overlapping charts disjointly across
an arbitrary load profile, nor does it treat the lower invariant sector.

The exact next statement needed for constant one is a common-base family of
pair swaps and a dual lower-flag family satisfying a charged coverage bound
of the form

\[
 \sum_{\mathcal C}
 \sum_{q=1}^Hw_{\mathcal C,q}
 \sum_U \mu_{\mathcal C,q,U}
       (\mu_{\mathcal C,q,U}-1)
 \ge
 \eta_m\bigl(\mathcal E_H-C_AH\operatorname{Cat}_m\bigr),
\tag{7.1}
\]

while the union of their physical run endpoints is \(o(W/H)\).  Formula
(0.5) then supplies the joined-owner curvature in (7.1) exactly; it is no
longer an abstract Gram hypothesis.  What remains unproved is the charged
coverage of the two invariant sectors, not the sign or the long-block
rounding of the activated sector.

No constant-one conclusion is claimed.
