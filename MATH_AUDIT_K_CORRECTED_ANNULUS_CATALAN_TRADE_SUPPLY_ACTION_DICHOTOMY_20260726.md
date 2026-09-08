# Audit of the corrected-annulus Catalan supply/action dichotomy

Date: 2026-07-26

Audited report:
`MATH_THEOREM_K_CORRECTED_ANNULUS_CATALAN_TRADE_SUPPLY_ACTION_DICHOTOMY_20260726.md`.

Method: pure mathematics only.  No computation, finite search, solver, web
input, or probabilistic black box is used.

## 0. Verdict

**Final verdict: PASS.**  The patched report has implemented every prior
substantive correction.  In particular:

1. the BTK specialization has been removed, and only the conditional
   low-\(\lambda_H(\mathcal D,\sigma)\) repair obstruction remains;
2. the operadic theorem is restricted to \(t\to\infty\), \(t=o(m)\),
   while the symmetric formula is stated only when
   \(t,m-t\to\infty\), and the root-near regime is expressly left open;
3. the clipped top class is \(\mathcal D_{\ge H}\), and the dependence on
   the fixed annular port assignment \(\sigma\) is retained throughout;
4. the \(3/8\) transposition statement is explicitly conditional on
   full-profile equivariance and is used only as a necessary quotient
   deficit;
5. infinity cutting is no longer treated as an automatic even factor.
   The report states, correctly, the exact complement-multigraph collision
   identity and leaves the prescribed-density sparse-shore problem open.

The packet normalization, the even/odd factor two, all three scalar bank
thresholds, the carrier-local constants, the \(w=9\) pentagon ceiling,
the cyclic top-tag estimate, the operadic constants, the conditional orbit
lemma, and the infinity-cut graph all check exactly.

There are two editorial points, neither a mathematical correction.  Formula
(0.14) would read more cleanly if

\[
 \gamma_{a,b}:=2e^{-(b^2-a^2)}-1
\]

were defined without an \(o(1)\), with the required arc fraction written
as \(\gamma_{a,b}-o(1)\).  The present asymptotic meaning is nevertheless
unambiguous.  Also the sentence at the end of Section 4 saying that the
``complete even owner ledger itself is still missing'' should say that the
**prescribed-density low-collision selected ledger** is missing: Section 7
does provide the complete primary-owner partition and collision identity.

## 1. Corrected active mass and the even/odd factor two

On even ground put

\[
 W_e=\binom{2m}{m}=(m+1)\operatorname {Cat}_m,
 \qquad
 N_q=\binom{2m}{m-q}.
\]

For

\[
 q_0=\lceil a\sqrt m\rceil,
 \qquad
 K=\left\lfloor{N_{q_0}\over2m}\right\rfloor,
\]

the standard ratio expansion gives

\[
 {N_{q_0}\over W_e}=e^{-a^2}+O_a(m^{-1/2}).
\]

Therefore

\[
 \boxed{
 K=\left({e^{-a^2}\over2}+o(1)\right)
       \operatorname {Cat}_m.}
 \tag{1.1}
\]

The factor (1/2) is correct:

\[
 {W_e\over2m\operatorname {Cat}_m}
 ={m+1\over2m}={1\over2}+o(1).
\]

There is no second factor for the upper sign.  One cyclic start supplies a
lower interval and, by complementing the same packet, the corresponding
upper interval.  Thus the active owner-occurrence demand is

\[
                    2mK=(e^{-a^2}+o(1))W_e.
\]

On odd PBBS ground,

\[
 W_o=\binom{2m+1}{m}=(2m+1)\operatorname {Cat}_m.
\]

A same-ground partial design would require

\[
 {e^{-a^2}W_o\over2m+1}
 =(e^{-a^2}+o(1))\operatorname {Cat}_m
\]

rows.  Hence a (delta\operatorname {Cat}_m)-row odd bank passes the
same-ground scalar count only when

\[
                         \delta>e^{-a^2}.
 \tag{1.2}
\]

If one merely counts the ordinary (2m)-start rows obtained after deleting
the odd infinity coordinate, the even demand (1.1) instead gives

\[
                         \delta>{1\over2}e^{-a^2}.
 \tag{1.3}
\]

This proves the report's factor-two distinction.  Equation (1.3) alone is
not a transfer theorem.  The patched Section 7 does prove that the
nonwrapping primary owners partition the even middle layer and gives an
exact formula for the collisions contributed by the other \(m-1\)
windows.  It does not prove that a prescribed-density row selection has
small collision, nor does it control the hereditary target ledgers.

### 1.1 Scalar thresholds

Substitution in (1.3) gives exactly

\[
\begin{array}{c|c}
\text{odd row density }\delta&\text{strict projected scalar range}\\ \hline
3/8&a^2>\log(4/3),\\
1/8&a^2>\log4,\\
5/256&a^2>\log(128/5).
\end{array}
\tag{1.4}
\]

Indeed, for example,

\[
 {3\over8}>{1\over2}e^{-a^2}
 \quad\Longleftrightarrow\quad
 e^{-a^2}<{3\over4}.
\]

The (5/256) row density is also normalized correctly: the explicit
unrelated pentagon pair has (operatorname {Cat}_{r-4}) components of
five changed rows per shore, and

\[
 {5\operatorname {Cat}_{r-4}\over\operatorname {Cat}_r}
 ={5\over256}+o(1).
\]

At equality in (1.4) the available (o(1)) errors have no certified sign,
so the report correctly claims no slack.

## 2. Carrier-local histogram constants

Let two cyclic orders be (w)-carrier-local.  At a fixed interval length,
an interval changes only if at least one of its two boundary cuts lies in
the interior of the carrier.  There are fewer than (w) possible starts
for either boundary, so at most (2w) occurrences change.

Replacing one occurrence (A) by (B) changes the histogram by
(e_B-e_A), whose half-(ell^1) norm is one.  Consequently, for (R)
paired packet replacements,

\[
 {1\over2}\|\mu_q-\mu_q'\|_1\le2wR.
 \tag{2.1}
\]

For equal-mass nonnegative integral histograms,

\[
 \bigl||\operatorname {supp}x|-|\operatorname {supp}y|\bigr|
 \le {1\over2}\|x-y\|_1.
\]

Applying this to rank-((m-q)) targets and to middle owners proves

\[
 |h_q-h_q'|\le2wR,
 \qquad
 |C_{\rm mid}-C_{\rm mid}'|\le2wR.
 \tag{2.2}
\]

There is no missing factor two.  With
(D=H-q_0+1), the compiler objective has one middle term and two signed
hole terms, so

\[
 |\Delta(C_{\rm mid}+2\sum_qh_q)|
 \le (4D+2)wR.
 \tag{2.3}
\]

Since (R\le K=(e^{-a^2}+o(1))W_e/(2m)), (2.2) gives

\[
 |h_{q_0}-h_{q_0}'|
 \le(e^{-a^2}+o(1)){w\over m}W_e,
 \tag{2.4}
\]

and, because (D=\Theta(\sqrt m)), (2.3) is

\[
                         O_{a,b}(wW_e/\sqrt m).
 \tag{2.5}
\]

Thus (w=o(m)) cannot repair a positive-density entrance defect, while
(w=o(\sqrt m)) has (o(W)) aggregate annulus action.  These are
statewise comparison bounds, not claims that either shore has a defect.

## 3. The pentagon (w=9) conclusion

The explicit growing pentagon pair is formed by suspending the size-three
pentagon once and right-concatenating an arbitrary Dyck suffix.  The two
orders differ only in the once-suspended core, whose carrier has nine
coordinate positions.  Right concatenation grows the nominal local factor
but does not enlarge this carrier.  Hence (w=9) is exact (and remains a
valid upper bound after deleting infinity from the cyclic word).

Equations (2.4)--(2.5) therefore specialize to

\[
 |h_{q_0}-h_{q_0}'|=O(W/m),
 \qquad
 |\Delta(C_{\rm mid}+2\sum_qh_q)|=O(W/\sqrt m)=o(W).
 \tag{3.1}
\]

Accordingly the pentagon cannot turn a reference with an
(Omega(W)) entrance or annulus defect into a successful family.  It may
still alter an already-(o(W)) remainder, and the locality theorem does
not say that a pentagon shore cannot happen to belong to some independently
constructed successful family.  This is the precise meaning of its
``invisibility.''

The row-count statement and the action statement are independent.  The
pentagon bank can pass the scalar (5/256) threshold while remaining
carrier-local with (w=9).

## 4. Operadic skeleton supply

The port-interface source proves that a shape-respecting (t)-node
skeleton packet can pass the common-coordinate port test only when

\[
 A_0\text{ is a mountain},
 \qquad A_1=\cdots=A_{t-2}=\varnothing.
\]

The number of eligible spectator tuples is therefore at most

\[
 B_{m-t}=[z^{m-t}]{C(z)^2\over1-z}
 =\left({16\over3}+o(1)\right)
     \operatorname {Cat}_{m-t},
 \tag{4.1}
\]

provided (m-t\to\infty).  If also (t\to\infty), then

\[
 {\operatorname {Cat}_t\operatorname {Cat}_{m-t}
       \over\operatorname {Cat}_m}
 =\left({1\over\sqrt\pi}+o(1)\right)
 {m^{3/2}\over t^{3/2}(m-t)^{3/2}}.
 \tag{4.2}
\]

Thus the general eligible-root bound in this range is

\[
 \left({16\over3\sqrt\pi}+o(1)\right)
 {m^{3/2}\over t^{3/2}(m-t)^{3/2}}
 \operatorname {Cat}_m.
 \tag{4.3}
\]

When (t=o(m)), (4.3) reduces to the audited report's

\[
 \left({16\over3\sqrt\pi}+o(1)\right)
 {\operatorname {Cat}_m\over t^{3/2}}.
 \tag{4.4}
\]

Dividing by (1.1) gives exactly

\[
 \left({32e^{a^2}\over3\sqrt\pi}+o(1)\right)t^{-3/2}
 \tag{4.5}
\]

in that domain.  Hence the constants in (0.10)--(0.11) pass.

The patched quantifier is correct.  Equations (4.1)--(4.5) prove an
\(o(K)\) supply when \(t,m-t\to\infty\), with (4.5) specifically requiring
\(t=o(m)\).  They do not prove the same assertion when \(m-t=O(1)\).
At the extreme (t=m), the spectator tuple is empty and the single full
skeleton edge already contains all (operatorname {Cat}_m) roots.  This
root-near regime is not excluded and is naturally part of the new
root-scale-factor gate.

## 5. Top-tag cycle cut

Fix both an SCD \(\mathcal D\) and an annular port assignment \(\sigma\).
The clipped top class is

\[
 \Omega_H=\mathcal D_{\ge H},
 \qquad |\Omega_H|=N_H.
\]

Suppose \(M=N_{q_0}-\rho\) selected states are partitioned into \(K\)
rotor cycles of length \(2m\).  At least \(N_H-\rho\) selected states lie
in \(\Omega_H\), and at most \(N_{q_0}-N_H\) selected states lie outside
it.  Write \(M_H,M_O\) for the two used counts.  In each cyclic binary
word the number of \(H\to O\) transitions equals the number of
\(O\to H\) transitions and is at most the number of \(O\)-vertices.
Consequently the number of actually used top-to-top cycle arcs satisfies

\[
 e_{HH}^{\circ}
 =M_H-\#(H\to O)
 \ge M_H-M_O
 \ge2N_H-N_{q_0}-\rho.                              \tag{5.1}
\]

This stronger cyclic estimate also covers an all-top cycle.  Deleting at
most one top-to-top edge from each all-top cyclic component makes all the
remaining top-to-top arcs a vertex-disjoint directed linear forest.
Top-class bridge rigidity makes them genuine rotor arcs, so

\[
 \boxed{
 \lambda_H(\mathcal D,\sigma)
 \ge2N_H-N_{q_0}-\rho-K.}
 \tag{5.2}
\]

Thus the patched \(-K\) occurs only in the passage from cyclic arcs to a
linear forest, not in the used-arc estimate.  Using
\(N_H/W=e^{-b^2+o(1)}\), \(N_{q_0}/W=e^{-a^2+o(1)}\), and
\(K+\rho=o(W)\), (5.2) gives

\[
 \lambda_H(\mathcal D,\sigma)
 \ge(2e^{-b^2}-e^{-a^2}-o(1))W.
 \tag{5.3}
\]

The coefficient is positive precisely when

\[
                         b^2-a^2<\log2.
\]

Dividing by the selected arc mass
\(M=(e^{-a^2}+o(1))W\) in the stronger cyclic estimate (5.1) gives the
aggregate required fraction

\[
 \boxed{
  2e^{-(b^2-a^2)}-1-o(1).}
 \tag{5.4}
\]

Equivalently, the average packet has at least

\[
 2m\bigl(2e^{-(b^2-a^2)}-1-o(1)\bigr)
\]

top-to-top arcs.  It is cleaner to define

\[
 \gamma_{a,b}:=2e^{-(b^2-a^2)}-1>0
\]

and state the required fraction as (gamma_{a,b}-o(1)).

The patched report makes no low-\(\lambda_H\) claim for BTK.  It retains
only the valid conditional statement

\[
 \lambda_H(\mathcal D,\sigma)=o(W)
 \quad\Longrightarrow\quad
 \text{every (w=o(m)) paired repair fails in the narrow annulus.}
\]

Indeed, changing at most \(cw\) relevant adjacency incidences in each of
\(K\) packets changes the available edge set by at most \(cwK=o(W)\).
After removing at most one arc per new cycle, (5.1) would give a linear
forest of \(\Omega(W)\) genuine new top arcs, contradicting the assumed
\(o(W)\) reference forest bound.  This is a repair obstruction only; it
does not say that both shores of every small trade are defective.

## 6. Conditional \(3/8\)-bank orbit lemma

The patched statement has the right quantifier.  Let \(\tau\) be the
coordinate transposition and let \(u_{J,q},v_{J,q}\) be the complete
depth-\(q\) occurrence histograms of the two shores of an ownership
component \(J\).  The report assumes, rather than infers,

\[
                         v_{J,q}=\tau u_{J,q}          \tag{6.1}
\]

for every selected component and every protected depth.  This assumption
is essential: root-owner closure or transport of the internal \(X/Y\)
ledger does not by itself identify every exported Gaussian-depth trace.

For a common component signing \(\varepsilon\),

\[
 \mu_q^\varepsilon
 =\sum_{J\in\mathcal J}\tau^{\varepsilon_J}u_{J,q}.
\]

If \(O\) is a one- or two-point \(\tau\)-orbit, then (6.1) gives

\[
 \sum_{T\in O}\mu_q^\varepsilon(T)
 =\sum_{J\in\mathcal J}\sum_{T\in O}u_{J,q}(T)
 =:s_{q,O}(\mathcal J),                              \tag{6.2}
\]

independently of every shore choice.  Since the histogram is integral, an
orbit of size \(|O|\) and total mass \(s\) supports at most
\(\min\{|O|,s\}\) targets.  Therefore

\[
 h_q(\mu^\varepsilon)
 \ge\sum_{O\in\mathcal T_q/\langle\tau\rangle}
        (|O|-s_{q,O}(\mathcal J))_+.                 \tag{6.3}
\]

This proves (2.12)--(2.13), including fixed points of \(\tau\).  It is a
lower bound only; surplus mass in one orbit cannot compensate for a
deficient orbit.  Thus (2.14), together with its projected middle-owner
analogue, is necessary.  It is not asserted sufficient: after quotient
dispersion, the same component signs must orient the two-point orbits at
all depths simultaneously.  The report also correctly says that neither
the premise (6.1) nor these quotient near-factor estimates are currently
proved for the full \(3/8\) Gaussian tail bank.

## 7. Infinity-cut complement graph

This new part is exact.  Rotate an anchored odd-factor row to

\[
                         (\infty,a_1,\ldots,a_{2m})
\]

and define its nonwrapping primary windows

\[
 P_{x,j}=\{a_j,\ldots,a_{j+m-1}\},
 \qquad1\le j\le m+1.                               \tag{7.1}
\]

Exactly \(m+1\) length-\(m\) windows of the odd cyclic row avoid
\(\infty\).  Exact odd middle ownership therefore makes all the
\(P_{x,j}\), over all Catalan rows, a partition of
\(\binom{[2m]}m\); the count is

\[
                 (m+1)\operatorname {Cat}_m=W.
\]

After deleting \(\infty\), the ordinary \(2m\)-cycle has these \(m+1\)
windows and the additional \(m-1\) windows

\[
                         P_{x,j}^{\,c},
                         \qquad2\le j\le m.          \tag{7.2}
\]

The two port windows obey

\[
                         P_{x,1}^c=P_{x,m+1}.         \tag{7.3}
\]

Consequently complementation preserves the global set of port primaries.
It also preserves the set of nonport primaries: if the complement of a
nonport primary were a port, complementing once more and using (7.3)
would make that same set a port primary, contrary to uniqueness of the
primary-owner partition.  No two nonport primaries in one row are
complements, since their start indices lie in \(\{2,\ldots,m\}\) and two
opposite starts differ by \(m\) modulo \(2m\).

Pair complementary nonport primaries and join their unique owner rows.
The resulting multigraph \(G_F\) is therefore loopless.  Every row owns
exactly \(m-1\) nonports, so its degree, with parallel edges counted, is
exactly \(m-1\).

For selected rows \(S\), all selected primary occurrences are distinct,
and all selected extra occurrences in (7.2) are distinct because
complementation is injective.  A collision can occur only between an
extra occurrence and a selected primary occurrence.  An internal graph
edge \(xy\), represented by complementary nonports \(P\) in row \(x\)
and \(P^c\) in row \(y\), creates exactly the two duplications

\[
 P_x^{\rm primary}=P_y^{\rm extra},
 \qquad
 (P^c)_y^{\rm primary}=(P^c)_x^{\rm extra}.
\]

Edges not internal to \(S\) create none, and distinct complement pairs
involve disjoint target pairs.  Hence

\[
 \boxed{
  2m|S|-\left|\bigcup_{x\in S}E_m(\pi_x)\right|
  =2e_{G_F}(S).}                                     \tag{7.4}
\]

This verifies looplessness, regularity, the factor two, and the absence of
hidden triple collisions in (7.1) of the report.  The conclusion is not
that infinity cutting automatically solves even ownership.  It reduces
that issue exactly to finding a prescribed-density row set with
\(e_{G_F}(S)=o(W)\), while all lower-depth interval-union conditions
remain additional.

## 8. Corrected implication boundary

In its patched form, the report proves the following.

1.  The even corrected annulus needs
    \((e^{-a^2}/2+o(1))\operatorname {Cat}_m\) ordinary packet rows.
2.  The odd \(3/8,1/8,5/256\) banks have enough **numerical projected row
    supply** in exactly the ranges (1.4).  Infinity cutting gives literal
    rows and the exact middle collision formula (7.4), but not the needed
    sparse row shore or hereditary target dispersion.
3.  A \(w=o(m)\) row-paired trade cannot repair an \(\Omega(W)\)
    tight-layer defect; \(w=o(\sqrt m)\) has only \(o(W)\) total annulus
    action.
4.  The pentagon pair has \(w=9\), so it cannot be the source of a
    macroscopic repair despite its positive row count.
5.  Common-interface operadic skeletons cover only \(o(K)\) roots when
    \(t,m-t\to\infty\); Theorem 5.1 uses the stated specialization
    \(t=o(m)\), and the root-near regime remains open.
6.  For a fixed annular port assignment, the narrow-annulus top-tag cut is
    (5.1)--(5.2), and a reference with
    \(\lambda_H(\mathcal D,\sigma)=o(W)\) requires root-scale
    repair action.
7.  Subject to full-profile equivariance, the \(3/8\) bank has the exact
    orbit-total invariant (6.2) and the necessary quotient deficit (6.3).
    No unconditional Gaussian-profile conclusion is drawn from it.

What is not proved is equally important.  No known Catalan bank has been
shown to contain a prescribed-density row shore with \(o(W)\) collisions;
no bank is known to make the rank-\(q_0\) intervals a near-factor; no
hereditary all-depth path-colour dispersion theorem is available; the
full-profile equivariance needed for the conditional \(3/8\) orbit lemma
is unproved; and no universal theorem says that a successful family must
arise as a large change from a defective reference.

Thus the safe final conclusion is:

> Known Catalan banks pass the corrected scalar row count in explicit
> ranges, and infinity cutting gives an exact complement-graph middle
> ledger.  A prescribed-density sparse-shore plus hereditary dispersion
> theorem, or a genuinely new root-scale repair, is still required.
> Root-scale action is necessary only when the trade must remove a
> macroscopic entrance/top-tag defect from the chosen reference.
