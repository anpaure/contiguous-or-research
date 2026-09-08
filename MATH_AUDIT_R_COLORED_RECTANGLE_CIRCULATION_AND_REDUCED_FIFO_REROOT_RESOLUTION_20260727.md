# Audit: colored rectangle circulation and the reduced FIFO re-root resolution

Date: 2026-07-27

Method: adversarial hand audit only. No computation, finite search,
solver, web input, or certificate data is used.

Audited source:
`MATH_THEOREM_R_COLORED_RECTANGLE_CIRCULATION_AND_REDUCED_FIFO_REROOT_RESOLUTION_20260727.md`.

## 0. Verdict

The following mathematical cores are valid as stated:

* the reduced-scale calibration (1.1)--(1.5);
* the sign normalization (2.4)--(2.6);
* the balanced and unbalanced Smith forms in Theorem 2.1;
* the orientation and signs of the Hoffman cuts (2.17);
* the middle coboundary identity (3.2);
* the seam holonomy identities (4.4)--(4.5);
* the short-collar inequality \(t\rho\ge2H\), with exactly the hypotheses
  of Theorem 5.1;
* the \(H\) versus \(H-1\) safety convention in Section 6;
* the splice location, slot-cycle lengths, and exact closure alternative
  \(g=1\) or \(s_0\mid k\) in Section 7; and
* the one-top-lap obstruction in Theorem 8.1.

The source requires seven substantive scope/quantifier corrections and
three minor precision corrections.  In particular, it does **not** prove
arbitrary colored-flow integrality, chronological installability, a
physical calibrated \(F_\rho\)-catalogue for every \(m\), general
adjacent-length floor repair impossibility, global owner completion, or
a universal fixed-column-histogram gate.

## 1. Hoffman integrality is only for the balanced incidence matrix

### Source claim requiring correction

Outcome Item 1 and the paragraph after Theorem 2.2 describe the complete
system as a bounded “colored-flow” network to which Hoffman cuts and
integrality apply simultaneously.

### Exact correction

Theorem 2.2 applies to

\[
                         D_\Sigma x=b,
       \qquad \ell_e\le x_e\le u_e,                          \tag{1.1}
\]

on a **balanced** signed component.  It does not apply to arbitrary
independent color, target, tag, owner-capacity, port-use, queue-use, or
resource rows appended to \(D_\Sigma\).

Endpoint-potential colors are harmless in the following exact sense.
If \(R:\mathbb Z^V\to A\) is a homomorphism and every edge-color column
factors as

\[
                         r_e=R d_e,                           \tag{1.2}
\]

then

\[
                         \sum_e r_ex_e
       =R D_\Sigma x=Rb.                                    \tag{1.3}
\]

Such a color adds only the compatibility condition that its requested
total equal \(Rb\); it adds no independent cut row.  The middle identity
(3.2) is precisely this statement with \(R=M_0\).

An independent color row can destroy total unimodularity.  Take the
balanced directed triangle with incidence columns

\[
 d_{12}=e_1-e_2,qquad d_{23}=e_2-e_3,qquad
 d_{31}=e_3-e_1,                                             \tag{1.4}
\]

and append one tag-consumption row \((1,1,1)\).  Using vertex rows one
and two gives the square matrix

\[
 \begin{pmatrix}
  1&0&-1\\
 -1&1& 0\\
  1&1& 1
 \end{pmatrix},                                             \tag{1.5}
\]

whose determinant is \(3\).  For right side \((0,0,1)^T\), the unique
solution is

\[
                         x_1=x_2=x_3={1\over3},               \tag{1.6}
\]

and there is no integral solution.  Thus arbitrary “colored” feasibility
needs a separate network extension or matrix theorem.

There is a second component qualification.  A component with a nonzero
collar is automatically balanced, as proved.  A zero-collar component
may be unbalanced; its Smith factor \(2\) and the displayed determinant-
two example show that ordinary Hoffman/TU integrality does not apply.
Outcome Item 1 must therefore say “every balanced component,” not the
complete system without qualification.

## 2. Integral formal flow is not chronological installability

### Source claim requiring correction

Outcome Item 2 says static cycle augmentation can repair congestion or
chronology.  Sections 2--3 also risk identifying an integral normalized
flow with an installed exact-factor trade.

### Exact correction

A kernel vector of \(D_\Sigma\) changes a formal bounded edge multiset.
It may reroute the formal flow or alter edge congestion.  Neither Smith
integrality nor Hoffman cuts prove:

* one current shore at every top;
* Boolean mutual exclusion among incident occurrences;
* owner or target capacity;
* a simultaneous exact-factor completion;
* an acyclic precedence relation among paired rectangles; or
* a chronological walk through the literal state graph.

Chronology requires a separate state-graph lift.  Therefore replace the
chronology sentence by:

> Balanced-cycle augmentation may change a formal bounded-flow
> representative while preserving its divergence.  Chronological
> installability is an additional theorem.

The middle-null identity remains exact: every literal chronology made
solely from the certified two-endpoint \(K_2\) columns projects to a
formal chain, and a closed projected chain has zero middle action.

The phrase “complete static two-top rectangle system” also needs an
explicit hypothesis.  Equations (2.1)--(2.3) model the certified
intrinsic boundary-\(K_2\) library, in which collar and middle differences
are fixed endpoint potentials.  They do not automatically include
context-dependent rectangles, exterior-moving connectors, higher-arity
packets, or general two-factor trades.

## 3. The Smith and holonomy signs are valid

No correction is needed to the following formulas.

The normalization

\[
 d_e=e_u-\sigma_e e_v,qquad
 a_e=m_u-\sigma_e m_v                              \tag{3.1}
\]

correctly changes both the variable and its bounds.  On a balanced
component, gauging by \(G=\operatorname{diag}(g_v)\) gives an ordinary
incidence matrix and

\[
 \operatorname{im}D_\Sigma
   =\{b:g^Tb=0\}.                                            \tag{3.2}
\]

On an unbalanced connected component, the image is exactly the
even-total lattice and the Smith form is

\[
                         1^{n_K-1},2.                         \tag{3.3}
\]

With tail coefficient \(+1\), summing over \(S\) gives

\[
 x(\delta^+(S))-x(\delta^-(S))=\widehat b(S),                \tag{3.4}
\]

so the two inequalities in (2.17) have the correct orientation.

The reverse-seam convention

\[
                         s_{\bar e}=-\sigma_es_e              \tag{3.5}
\]

and the transported identity

\[
 (1-P_C)c_{v_0}=-\sum_iP_i s_{e_i}                           \tag{3.6}
\]

are also correct.

The sentence that the integral kernel is generated by balanced cycles
and tight/loose handcuffs is standard and appears correct, including
coefficient two on a loose connecting path.  It is not proved by the
Smith calculation alone.  Add a support-minimal signed-flow
decomposition or mark this sentence as imported.  It is not needed for
Theorem 3.1.

## 4. Calibration is valid; one explanatory sentence should move

The exact ratio is

\[
 \lambda={W\over N}
 =\prod_{j=1}^{H}{m+j\over m-j+1}.                           \tag{4.1}
\]

A sharper expansion is

\[
 \log\lambda
 ={H^2\over m}-{H^2\over2m^2}
 +O\!\left({H^4\over m^3}\right).                           \tag{4.2}
\]

The source's looser (1.2) is valid.  Its explanation should be adjusted:
the \(O(H/m)\) floor error is not a Taylor remainder for fixed integer
\(H\); it enters when comparing \(H^2/m\) with \(\log\log m\).

For

\[
 H=\lfloor\sqrt{m\log\log m}\rfloor,
\]

one indeed gets

\[
 \log\lambda=\log\log m+o(1/\log m),
 \qquad \lambda=\log m+o(1),                                \tag{4.3}
\]

and

\[
 \rho=\lfloor\lambda\rfloor=\log m+O(1),qquad
 \rho N=W-\{\lambda\}N=W-o(W).                              \tag{4.4}
\]

Only \(\rho\sim\log m\), not \(\rho=\log m+o(1)\), follows.
The source uses the correct weaker statement.

## 5. The short-collar inequality is exact but mechanism-specific

The proof of Theorem 5.1 is valid.  The two displayed collar intervals
have overlap

\[
                         L=2H-\rho.                           \tag{5.1}
\]

The exclusive label \(x_i\) moves left by \(\rho\) positions at every
seam identification.  If \(t\rho<2H\), periodicity puts \(x_i\) in
\(C_i\subseteq B_i\), contradicting \(x_i\notin B_i\).  Hence

\[
                         \boxed{t\rho\ge2H}.                 \tag{5.2}
\]

Equality is allowed; the constant is not \(2H-1\).  Here \(t\) is the
number of carrier tops.  It should not be denoted by \(k\), which is
already \(m-H\).

The implication is only for the seamwise overlapping-collar mechanism
specified by (5.6)--(5.7).  It does not rule out arbitrary
exterior-moving connectors or a different aggregate cancellation.
For \(t=4\), it does rule out that exact mechanism eventually because
\(4\rho<2H\).

Minor notation: Section 5 introduces an undefined generic \(M\)-set.
Replace \(M\) there by \(\ell=m+H\), or explicitly declare a generic
top size \(M\).

## 6. The \(H\) versus \(H-1\) correction is valid

Physical safety through depth \(H\) means every interval of at most
\(H\) transitions is geodesic.  Before a new transition, only the newest
\(H-1\) historical arrivals/departures are forbidden.  A label used
exactly \(H\) transitions earlier may be reversed now, because the
spanning interval would have \(H+1\) transitions.

If a raw state records

\[
 (X;i_1,\ldots,i_H;d_1,\ldots,d_H)                          \tag{6.1}
\]

from oldest to newest, its exact next-step choices are

\[
 x\in X\setminus\{i_2,\ldots,i_H\},qquad
 y\in X^c\setminus\{d_2,\ldots,d_H\}.                       \tag{6.2}
\]

Thus the exact in/out degree is

\[
                         (m-H+1)^2,                           \tag{6.3}
\]

not \((m-H)^2\).  Equivalently one may store only \(H-1\) transitions,
giving \(W(m)_{H-1}^2\) states.  A state retaining all \(H\) labels still
has \(W(m)_H^2\) presentations, but its oldest pair is allowed in the
next move.

Section 6 of the audited report states this convention correctly.  Any
reliance on the older \(\mathcal Q_H\) theorem which excluded all \(H\)
recorded labels and claimed degree \((m-H)^2\) must be retracted: that
older automaton enforces an \((H+1)\)-transition window.  The depth-
\(H\) trace uses exactly the previous \(H-1\) moves, and the return in
the \(F_r\) macro at the oldest allowed time is legal.

## 7. The fixed-macro cycle lengths are right; the range is wrong

The indexing in Section 7 is correct.  With

\[
 F_r=S O^{r-1},
\]

the spliced rotation-
\(r\) arrow is

\[
                         u_{m-r+1}\longrightarrow u_{m+1},   \tag{7.1}
\]

not \(u_m\to u_{m+1}\) unless \(r=1\).  If

\[
 g=\gcd(\ell,r),qquad s_0={\ell\over g},                    \tag{7.2}
\]

the exact slot-cycle lengths are

\[
                         s_0+k,qquad s_0^{\ (g-1)},          \tag{7.3}
\]

and closure at the first root return is exactly

\[
                         g=1\quad\hbox{or}\quad s_0\mid k.  \tag{7.4}
\]

### Required quantifier correction

The proof's assertion

\[
                         s_0\ge\ell/r>2H                    \tag{7.5}
\]

is false uniformly over \(1\le r<H\).  From \(r<H\) one obtains only
\(s_0>\ell/H\), which can be much smaller than \(2H\).

The reduction of (7.4) to \(g=1\) is valid whenever

\[
                         s_0>2H,                             \tag{7.6}
\]

because \(s_0\mid\ell,k\) would imply \(s_0\mid2H\).  A simple
sufficient hypothesis is

\[
                         r<{ell\over2H}.                    \tag{7.7}
\]

It is valid at the calibrated lengths \(r=\rho\) and \(r=\rho+1\),
since

\[
                         {2H\rho\over\ell}\longrightarrow0.\tag{7.8}
\]

Accordingly, replace “in the reduced range \(1\le r<H\)” by “whenever
\(s_0>2H\), in particular for \(r\in\{\rho,\rho+1\}\).”

There is no theorem that

\[
                         \gcd(\ell,\rho)=1                   \tag{7.9}
\]

for every \(m\).  Therefore a calibrated \(F_\rho\)-cycle with
\(2m\rho\) owner transitions exists only conditionally on (7.9).  The
oriented interval-root catalogue is always physically realizable with
\(r=1\), but that supplies only one owner transition per root block.
Recovering the scalar \(\rho N\) then needs a separately legal clone,
mixed-length, or multiframe construction.

Thus Outcome Item 7 must separate two facts:

1. \(\rho N=W-o(W)\) is the correct scalar occurrence count;
2. the fixed macro realizes that count in zero-monodromy \(2m\)-block
   cycles only when the required arithmetic closure is available.

The catalogue degree \(k!\ell!\) counts oriented cyclic orders.  If
reverse orientations are identified as one simple root hyperedge, the
degree is \(k!\ell!/2\); the relative pair codegree remains
\(2/(k\ell)\).  Physical oriented columns may legitimately retain the
first convention, but it should be named.

## 8. The adjacent-length theorem rules out only one lap

Formula (8.2) and Theorem 8.1 are valid.  If

\[
                         \ell=q\rho+\eta,qquad0\le\eta<\rho,\tag{8.1}
\]

the source's two schedules have exact total stride \(\ell\):

* if \(\eta>0\), use \(\eta\) blocks of length \(\rho+1\) and
  \(q-\eta\) blocks of length \(\rho\);
* if \(\eta=0\), use \(\rho\) long blocks and
  \(q-1-\rho\) short blocks.

Their counts are eventually nonnegative because \(\ell\gg\rho^2\).
Every ordering of either prescribed one-lap multiset fails root closure.

### Required scope correction

This does not prove that adjacent \(\rho/(\rho+1)\)-length floor repair
is impossible in general.  It excludes only positive block words with

\[
                         \sum_i a_i=\ell.                    \tag{8.2}
\]

Multi-lap words and words with other total stride remain open and must
solve the full noncommutative anchored-cycle equation.  Consequently the
section title and statements “adjacent block lengths do not solve the
floor” must be weakened to “the natural one-top-lap adjacent schedule
does not close.”

In particular, the floor remainder in \(W/N\) is not itself identified
with the remainder \(\eta\) in \(\ell=q\rho+\eta\).  A global floor
repair distributes \((\rho+1)\)-blocks across many root occurrences;
Theorem 8.1 does not classify every such distribution.

## 9. Root occurrence count is not owner completion

The implication

\[
                         \rho(N-o(N))=W-o(W)                 \tag{9.1}
\]

is an occurrence count.  It is not a count of distinct covered middle
owners unless all declared owner occurrences are globally pairwise
distinct across every selected root and every selected cycle.

The phrase “each root supports \(\rho\) distinct occurrences” is
insufficient if “distinct” means only within one root block.  The report
does not prove either:

* owner simplicity around one full \(F_r\)-cycle for \(r>1\); or
* owner disjointness between different selected cycles.

Therefore a root near-factor alone gives no owner near-factor.  Replace
the relevant sentence by:

> Conditionally, if the selected physical cycles carry a globally
> owner-simple family of \(W-o(W)\) principal occurrences, then the
> scalar ledger is correct.

The compiler estimate

\[
 L_{\rm word}\le T+2HC+K_{\rm conn}+\mathfrak H             \tag{9.2}
\]

and the condition

\[
                         {N\over C}=\omega(H/\rho)            \tag{9.3}
\]

are correct as conditional sufficient statements.  A root near-factor
by \(2m\)-block cycles would have collar allowance

\[
                         O(HN/m)=o(W),                        \tag{9.4}
\]

but only after owner simplicity, target capacity, connector legality,
and the residual Hall ledger are supplied.

## 10. The column-histogram fibre is not universal

The matrix

\[
 C_{j,v}=\#\{U:\text{label }v\text{ occupies rooted position }j
                 \text{ on }U\}                             \tag{10.1}
\]

is indeed invariant under the specific certified two-top boundary
rectangles and the specific three-top re-root packet cited in Section 9.
It is not invariant under every collar-neutral re-root move admitted
elsewhere in the report.

For a simultaneous four-top shift \(p_i\mapsto Sp_i\), put

\[
 A_{j,v}=\#\{i:p_i(j)=v\}.                                  \tag{10.2}
\]

Its exact derivative is

\[
                         \Delta C_{j,v}=A_{j+1,v}-A_{j,v}.   \tag{10.3}
\]

If this vanished for every \(j,v\), then \(A_{j,v}\) would be independent
of \(j\).  Summing positions would give

\[
                         r_v=M A_{j,v},                      \tag{10.4}
\]

where \(1\le r_v\le4\) is the number of the four tops containing label
\(v\).  For \(M>4\), this is impossible.  Hence the physical four-top
Johnson-square re-root move leaves the column-histogram fibre even though
its protected trace collar cancels exactly.  The same issue applies to
general facet-cycle re-root shifts unless separate column balance is
proved.

Therefore the final statement that the surviving coefficient-one gate
must lie in one fixed \((C_{j,v})\)-fibre is valid only if the allowed
move library is restricted to the cited two-top/three-top moves.  Once
the four-top or growing re-root cycles of Sections 5--7 are allowed, the
fixed-fibre condition is not an invariant and cannot be imposed as a
necessary gate.

The corrected conclusion has two branches:

1. within the narrow rectangle/three-top library, endpoint tables must
   lie in a common column-histogram fibre; or
2. a histogram-changing collar-neutral re-root packet may leave that
   fibre, but its full owner, target, queue, and chronology rows must be
   accounted for.

## 11. Corrected implication boundary

After the corrections above, the exact proved content is:

1. certified intrinsic two-endpoint \(K_2\) rectangle columns form a
   signed incidence system;
2. nonzero-collar components are balanced, and balanced bounded flows
   obey the stated Hoffman cuts and are integrally solvable as formal
   flows;
3. endpoint-coboundary colors, including the middle action, are fixed by
   per-top divergence, so closed certified rectangle chains are
   middle-null;
4. seam holonomy is given by (3.6);
5. the displayed short overlapping-collar mechanism needs
   \(t\rho\ge2H\);
6. physical depth-\(H\) safety has \(H-1\) forbidden historical moves;
7. fixed-macro monodromy has the exact cycle decomposition (7.3) and
   closure alternative (7.4);
8. at calibrated \(r\), gcd-one is the physical closure condition, but
   its truth is an additional arithmetic hypothesis; and
9. the prescribed one-top-lap adjacent-length schedule never closes.

Still unproved are arbitrary colored/resource integrality,
chronological exact-factor installation, a universally available
calibrated physical cycle catalogue, general mixed-length repair,
globally owner-simple root packing, all-depth target capacity, escape or
completion within the appropriate histogram fibre, and coefficient one.
