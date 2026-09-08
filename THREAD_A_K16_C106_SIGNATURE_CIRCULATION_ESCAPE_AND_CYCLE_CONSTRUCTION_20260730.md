# Thread A: C106 signature circulation, global escape cuts, and cycle construction

Date: 2026-07-30  
Status: **proved in the frozen source-relative 211,604-seam catalogue; no C106 carrier is claimed**

## 1. Scope and conclusion

Let `E` be the authenticated direction-coherent seam catalogue of the
length-eight K16 source.  Its vertices are the 12,870 source ports.  For a
seam \(e:u\to v\), write

\[
 h_e\in\{0,1\}^{D},\qquad s_e\in\mathbb Z_{\ge0}
\]

for its incidence on the 93 frozen lower-q2/upper-q3 defects and its exact
scale-two dual slack.  The catalogue has

\[
 |h_e|\in\{0,1,2\};
\]

there is no lower/lower two-hit seam.

The frozen five-lock theorem says that every integral balanced count-106
cover has one of \(4^5=1024\) signatures.  If \(R\) positions of the
signature are `S`, then exactly \(Q=5-R\) lower, price-one lock targets are
repeated once, every other target occurs once, and

\[
 \sum_e s_ex_e=R.                                      \tag{1.1}
\]

This note proves five further statements.

1. **All 243 slack-zero signatures are impossible**, even as nonnegative
   real balanced flows and without port capacity.  A later exact full-arc
   Farkas certificate also excludes all 405 `R=1` signatures in a continuous
   relaxation larger than the capacity master.
2. Every capacity-one C106 signature obeys an exact service/return ledger.
   In particular, if \(z_j\) is the number of selected seams hitting exactly
   \(j\) defects, then
   \[
                  z_0-z_2=8+R.                         \tag{1.2}
   \]
   Thus every double-provider seam forces one additional hitless return seam
   on top of an unavoidable \(8+R\).
3. A signature-independent shortest-return filter and a complete family of
   port-potential cut inequalities classify the **fractional projection of
   the integer-WLOG return-capable graph**.  For fixed \(R\), one cut acts on
   all signatures through five affine lock choices; 1024 unrelated models
   are unnecessary.
4. Integral feasibility is exactly a vertex-disjoint tight-cycle/portal-
   circuit packing.  Across the whole selection there are at most \(R\le5\)
   positive-slack portal seams.  This gives a proof-guided construction
   space, while preserving the precise point at which integrality remains.
5. Every one of the 1,024 signatures must use at least two seams outside the
   662-seam support of the exact `SSSSS` fractional point; a universal
   cohomology residue gives a proof-guided radius-two completion test.

A later exact result, proved in
`MATH_THEOREM_A_K16_C106_R1_FULL_ARC_EXACT_FARKAS_20260730.md`, closes all
405 \(R=1\) signatures in the full continuous all-slack relaxation.  The
table below records that updated classification; Sections 3--8 retain the
original derivations and construction interfaces.

The rigorous full-catalogue classification obtained here is therefore

\[
\begin{array}{c|rrrrrr}
R&0&1&2&3&4&5\\ \hline
\text{five-lock signatures}&243&405&270&90&15&1\\
\text{integral capacity-one witnesses proved}&0&0&0&0&0&0\\
\text{proved full-catalogue impossible}&243&405&0&0&0&0\\
\text{open}&0&0&270&90&15&1
\end{array}                                             \tag{1.3}
\]

The zeroes in the “integral capacity-one witnesses proved” row mean that no
such witness is presently proved; fractional points do not populate this
row, and the zeroes are not no-go claims.  The `R=1` entry is supported
by `MATH_THEOREM_A_K16_C106_R1_FULL_ARC_EXACT_FARKAS_20260730.md`, whose
integer certificate checks every one of the 211,469 cycle-eligible all-slack
arcs and has positive right-hand side 245,524 against maximum column -1.
It supersedes the earlier truncated numerical census.

Everything here is source-relative.  Width-five seams, close interacting
windows, open-boundary transformations, and other K16 carriers are outside
the theorem.

## 2. Exact signature notation

The five lock triples are

\[
\begin{aligned}
T_1&=\{35044,36935,40066\},&
T_2&=\{37320,41102,47364\},\\
T_3&=\{33906,36417,51235\},&
T_4&=\{33337,50976,58385\},\\
T_5&=\{41872,49436,61960\}.&&
\end{aligned}                                           \tag{2.1}
\]

Every displayed mask has rank six.  For

\[
 \alpha=(\alpha_1,\ldots,\alpha_5)\in\{S,0,1,2\}^5,
\]

let \(R(\alpha)=|\{i:\alpha_i=S\}|\).  If \(\alpha_i\ne S\), let
\(t_i(\alpha)\) be the corresponding member of \(T_i\).  Define the exact
target-demand vector

\[
 d^\alpha_t=1+\mathbf 1_{\{t=t_i(\alpha)\text{ for some }i\}}. \tag{2.2}
\]

The five-lock equality theorem gives

\[
 |d^\alpha|_1=98-R(\alpha),\qquad
 b\mathbin\cdot d^\alpha=212-R(\alpha),                 \tag{2.3}
\]

where the direct target prices \(b_t\) lie in \(\{1,2,4\}\).  Together with
balance, the direct identity gives (1.1) and count 106.

## 3. A common exact Farkas cut eliminates every \(R=0\) signature

The earlier exact no-capacity tight-face certificate supplies integer-scaled
multipliers

\[
 K=118200,qquad
 (G_1,G_2,G_4)=(-1980879,2162517,1398229),               \tag{3.1}
\]

port potentials \(A_v\), and nonnegative target multipliers \(Z_t\), with

\[
 \sum_{t\in D}Z_t=132674283.                            \tag{3.2}
\]

For every one of the 1,930 cycle-eligible tight seams \(e:u\to v\), exact
raw replay proves

\[
 A_u-A_v+K+
 \sum_{t\in H(e)}(G_{b_t}-Z_t)\ge0.                    \tag{3.3}
\]

The multipliers were originally recorded for a count-105 face, but the
column inequality (3.3) is independent of the right-hand side.  It can
therefore be reused without rerunning or altering the C105 theorem.

### Theorem 3.1 (all-tight C106 no-go)

No nonnegative real balanced seam flow of count 106 can cover all 93 targets,
have target-price class totals

\[
 (M_1,M_2,M_4)=(20,60,18),                              \tag{3.4}
\]

and have total direct slack zero.  Consequently none of the 243 \(R=0\)
C106 signatures is feasible.

#### Proof

Nonnegative total slack zero forces every positive-flow seam to be tight.
Every positive edge of a finite nonnegative circulation lies on a directed
cycle, so it is one of the cycle-eligible seams on which (3.3) was checked.
Multiply (3.3) by its seam flow and sum.  Balance cancels the \(A_v\) terms.
Using count 106, the three exact class totals, and service at least one at
each target gives

\[
\begin{aligned}
0
&\le \sum_e x_e\left(A_u-A_v+K+
              \sum_{t\in H(e)}(G_{b_t}-Z_t)\right)\\
&\le 106K+20G_1+60G_2+18G_4-\sum_tZ_t\\
&=-4843521<0.
\end{aligned}                                           \tag{3.5}
\]

The scale in (3.5) is \(10^6\); its sign is exact.  This contradiction proves
the first assertion.  In an \(R=0\) C106 normal form, precisely five
price-one targets are repeated, so (3.4) holds.  Hence all 243 signatures are
excluded.  No capacity, separation, q1, residence, or deeper-shadow row was
used.  \(\square\)

This is stronger than the existing numerical 243-signature LP census and
makes that census unnecessary for the theorem.

## 4. Exact hitless-return conservation

Let \(z_j\) count selected seams \(e\) with \(|H(e)|=j\).  Because every seam
hits at most two targets,

\[
 z_0+z_1+z_2=106,qquad z_1+2z_2=|d^\alpha|_1=98-R.      \tag{4.1}
\]

Subtracting proves the exact identity

\[
                         \boxed{z_0-z_2=8+R}.           \tag{4.2}
\]

This is not an asymptotic or LP inequality.  It holds for every integral
capacity-one C106 realization of every signature.

There is a sharper shore ledger.  Write \(z_L,z_U,z_{LU},z_{UU}\) for the
numbers of lower-only singleton, upper-only singleton, lower/upper double,
and upper/upper double seams.  There are no lower/lower doubles.  All lock
repeats are lower, so

\[
\begin{aligned}
 z_L+z_{LU}&=50-R,\\
 z_U+z_{LU}+2z_{UU}&=48,\\
 z_0+z_L+z_U+z_{LU}+z_{UU}&=106.                        \tag{4.3}
\end{aligned}
\]

The authenticated double-provider graph has 18 pair-isolated targets:
fifteen lower and three upper.  None lies in a lock triple.  Each therefore
has exact demand one and must use a singleton seam.  Hence

\[
 z_L\ge15,\qquad z_U\ge3.                               \tag{4.4}
\]

Combining (4.3)--(4.4) gives

\[
\begin{aligned}
 z_{LU}&\le35-R,\\
 z_{LU}+2z_{UU}&\le45,\\
 z_2&\le\left\lfloor\frac{80-R}{2}\right\rfloor,\\
 z_0&\ge8+R,\\
 z_1+z_2&\ge58-\left\lfloor\frac R2\right\rfloor.      \tag{4.5}
\end{aligned}
\]

For reference, the last three bounds by slack class are

\[
\begin{array}{c|rrrrrr}
R&0&1&2&3&4&5\\ \hline
z_2\text{ at most}&40&39&39&38&38&37\\
z_0\text{ at least}&8&9&10&11&12&13\\
\text{provider seams at least}&58&58&57&57&56&56.
\end{array}                                             \tag{4.6}
\]

The conceptual content of (4.2) is useful for construction: replacing two
singleton providers by one double provider does not save a selected seam at
count 106.  It creates one mandatory hitless return slot.

## 5. Global return-capable arcs

Give every seam its nonnegative integer length \(s_e\).  Let

\[
 \delta(a,b)=\min\left\{\sum_{e\in P}s_e:
        P\text{ is a directed }a\text{-to-}b\text{ path}\right\},     \tag{5.1}
\]

with value \(+\infty\) when no path exists.  Define

\[
 E_R^{\rm ret}=
 \{e:u\to v:s_e+\delta(v,u)\le R\}.                    \tag{5.2}
\]

### Lemma 5.1 (shortest-return filter)

Every seam selected by an integral balanced circulation of total slack \(R\)
lies in \(E_R^{\rm ret}\).

#### Proof

Capacity one and balance make the selected digraph a vertex-disjoint union
of directed simple cycles.  If \(e:u\to v\) belongs to a selected cycle,
the remainder of that cycle is a \(v\)-to-\(u\) path.  Its slack is at most
\(R-s_e\).  Therefore \(\delta(v,u)\le R-s_e\).  \(\square\)

For \(R=0\), (5.2) is precisely tight-SCC cycle eligibility.  For \(R=1\),
every non-tight selected cycle consists of one slack-one seam and a tight
return path.  Unlike a local `SSSSS` support expansion, (5.2) is global and
applies identically to every signature having the same \(R\).

## 6. Exact global port-potential cuts

Fix \(R\) and use only \(E_R^{\rm ret}\), a sound integer presolve by Lemma
5.1.  Let

\[
 \mathcal P_R=\left\{x\ge0:
 Bx=0,\quad \sum_{e\in\delta^+(v)}x_e\le1\ (v),\quad
 x_e=0\ (e\notin E_R^{\rm ret})\right\}.               \tag{6.1}
\]

The polytope \(\mathcal P_R\) is integral: split every port into an in-node
and out-node, place capacity one on the internal port arc, and regard the
seams as ordinary arcs of a circulation network.

For an arbitrary seam score \(c=(c_e)\), define

\[
 \Gamma_R(c)=\min_{p\in\mathbb R^{V}}
 \sum_{v\in V}\max\left(0,
    \max_{e=v\to w\in E_R^{\rm ret}}
       \{c_e+p_v-p_w\}\right).                         \tag{6.2}
\]

Empty inner maxima are omitted.  Network LP duality gives

\[
 \Gamma_R(c)=\max_{x\in\mathcal P_R}\sum_ec_ex_e.       \tag{6.3}
\]

### Theorem 6.1 (signature-independent global cut family)

If a C106 signature \(\alpha\) has an integral capacity-one realization, then
for every \(\lambda\in\mathbb R^D\) and every
\(\kappa,\eta\in\mathbb R\),

\[
 \boxed{
 \lambda\mathbin\cdot d^\alpha+106\kappa+R\eta
 \le
 \Gamma_R\bigl(\lambda\mathbin\cdot h_e+\kappa+\eta s_e\bigr).}
                                                               \tag{6.4}
\]

Conversely, all inequalities (6.4) hold if and only if the exact service,
count, and slack vector \((d^\alpha,106,R)\) lies in the corresponding
projection of \(\mathcal P_R\).  Thus (6.4) is a complete classification of
the return-capable **fractional projection**, though not of its integral
service fibre.

#### Proof

For a feasible realization, put

\[
 c_e=\lambda\mathbin\cdot h_e+\kappa+\eta s_e.
\]

Its score is the left side of (6.4), while (6.3) upper-bounds the score of
every member of \(\mathcal P_R\).  This proves necessity.  Conversely, the
image of the compact polytope obtained after discarding its zero-coordinate
ports is convex.  If the claimed target vector is outside that image, strict
separation supplies \((\lambda,\kappa,\eta)\) violating (6.4).  \(\square\)

For fixed \(R\), the right side of (6.4) is independent of the lock
signature.  The left side is

\[
 \lambda\mathbin\cdot\mathbf1_D+106\kappa+R\eta+
 \sum_{i:\alpha_i\ne S}\lambda_{t_i(\alpha)}.           \tag{6.5}
\]

Hence one exact cut classifies a Cartesian family of the lock choices.  This
is the appropriate way to turn a rational R1 Farkas ray, or a future R2--R5
capacity ray, into a reusable theorem instead of 1024 solver statuses.

A simpler but weaker consequence, obtained by taking \(p=0,\kappa=\eta=0\),
is the weighted outgoing Hall cut

\[
 \sum_t\lambda_td_t^\alpha
 \le\sum_v\max\left(0,
      \max_{e\in\delta^+(v)\cap E_R^{\rm ret}}
          \sum_{t\in H(e)}\lambda_t\right).            \tag{6.6}
\]

The analogous incoming inequality also holds.  These cuts use the full
return-capable catalogue, not an `SSSSS` seed support.

### 6.2 Adversarial audit: the old tight-face ray has no scalar R1 extension

The most economical attempt to settle all 405 R1 signatures is to retain the
Farkas column score \(c_e\) from Section 3 and add one scalar multiple
\(\lambda s_e\) of direct slack, together with an arbitrary port coboundary.
The R1 right-hand side before this correction is

\[
 -2862642.                                                   \tag{6.7}
\]

An exact shortest-return audit finds a directed closed walk of length 65
with total direct slack one, portal seam `182764`, lock syndrome equal to a
unit vector, and old Farkas score

\[
 -3319234.                                                   \tag{6.8}
\]

Port coboundaries telescope on this walk.  Therefore any scalar
\(\lambda\) making every slack-at-most-one closed walk nonnegative must obey

\[
 \lambda\ge3319234.                                         \tag{6.9}
\]

But then the corrected R1 right-hand side is at least

\[
 -2862642+3319234=456592>0,                                 \tag{6.10}
\]

so this ray cannot contradict R1.  The walk is not a feasible C106 service
solution: it repeats nonlock targets.  Its role is exact and narrower—it
proves that a target-blind scalar slack correction cannot certify R1.
Targetwise multipliers, or a genuinely different cut of the form (6.4), are
necessary.

## 7. Integral cycle/portal classification

Let \(\mathscr C_R\) be the finite family of directed simple cycles of total
slack at most \(R\) in the seam graph.  For \(C\in\mathscr C_R\), write

\[
 V(C),\quad \ell(C),\quad r(C),\quad a_t(C)
\]

for its port set, length, slack, and target-service multiplicities.

### Theorem 7.1 (exact cycle-packing form)

A lock signature \(\alpha\) supports an integral balanced capacity-one C106
circulation if and only if there are variables
\(y_C\in\{0,1\}\), \(C\in\mathscr C_R\), satisfying

\[
\begin{aligned}
 \sum_{C:v\in V(C)}y_C&\le1 &&(v),\\
 \sum_C\ell(C)y_C&=106,\\
 \sum_Cr(C)y_C&=R,\\
 \sum_Ca_t(C)y_C&=d_t^\alpha &&(t\in D).
\end{aligned}                                           \tag{7.1}
\]

#### Proof

An integral balanced capacity-one seam set has indegree and outdegree either
both zero or both one at every port, and therefore decomposes uniquely into
vertex-disjoint directed simple cycles.  Their data satisfy (7.1).
Conversely, the port-disjoint cycles selected by any solution of (7.1) give
the required seam set.  \(\square\)

There is a small-slack normal form for every column of (7.1).  Delete the
positive-slack seams from a selected cycle.  What remains is a collection of
tight directed paths.  Thus every non-tight cycle is an alternating cyclic
concatenation

\[
 e_1P_1e_2P_2\cdots e_pP_p,                            \tag{7.2}
\]

where every \(e_i\) has positive slack and every \(P_i\) is tight.  Across
all selected cycles,

\[
                 \#\{\text{positive-slack selected seams}\}\le R\le5.
                                                               \tag{7.3}
\]

Consequently a proof-guided construction should enumerate or construct at
most five portal seams, join them by tight return paths, and complete with
port-disjoint tight cycles.  For \(R=1\), this is exactly one slack-one seam,
one tight return path, and an arbitrary disjoint tight-cycle bank.  This was
the one-portal cycle-column formulation of the R1 face before the later exact
full-arc Farkas certificate excluded it.

Each individual selected cycle also obeys the exact local dual identity

\[
 2\ell(C)=\sum_tb_ta_t(C)+r(C),                         \tag{7.4}
\]

because the port potential telescopes around that cycle.  Equations
(7.1), (7.2), and (7.4) are the construction interface.

### Theorem 7.2 (cyclewise lock saturation)

For a selected cycle \(C\), let \(\sigma(C)\in\mathbb F_2^5\) record the
parities of its service totals on the five lock triples.

In every integral C106 realization, each selected cycle \(C\) satisfies

\[
 \operatorname{wt}(\sigma(C))=r(C),                     \tag{7.5}
\]

the nonzero supports \(\operatorname{supp}\sigma(C)\) are pairwise disjoint,
and their union is exactly the set of the \(R\) `S` positions of the lock
signature.  In particular, every tight selected cycle has zero syndrome, and
there are at most \(R\) positive-slack cycles.

#### Proof

The five-lock closed-walk theorem applies to each cycle separately:

\[
 \operatorname{wt}(\sigma(C))\le r(C).                  \tag{7.6}
\]

The global C106 normal form has syndrome equal to the indicator of its `S`
positions, hence weight \(R\).  Since cycle syndromes combine by XOR,

\[
 R=\operatorname{wt}\!\left(\bigoplus_C\sigma(C)\right)
 \le\sum_C\operatorname{wt}(\sigma(C))
 \le\sum_Cr(C)=R.                                      \tag{7.7}
\]

Equality holds throughout.  Equality in the second inequality forces (7.5)
cyclewise.  Equality between the Hamming weight of an XOR and the sum of the
individual Hamming weights forces the supports to be pairwise disjoint.  Their
XOR is the `S` indicator, so they partition those positions.  \(\square\)

Thus an \(R=1\) construction has one positive cycle whose syndrome is the
unique `S` lock, while every completion cycle is tight and syndrome zero.  At
general \(R\), the portal-cycle syndromes must form a set partition of the
`S` locks; arbitrary positive cycles cannot be combined independently.

The possible positive-cycle syndrome partitions are therefore counted by
the Bell number \(B_R\):

\[
 (B_0,B_1,B_2,B_3,B_4,B_5)=(1,1,2,5,15,52).             \tag{7.8}
\]

There is also an exact lock-triple co-location rule.  At a digit position,
every cycle meets that lock triple an even number of times and the total is
four; its nonzero cycle totals are therefore either \((4)\) or \((2,2)\).
If (t) is the repeated target, the latter case is necessarily

\[
 \{t,t\}\mid\{a,b\}
 \quad\text{or}\quad
 \{t,a\}\mid\{t,b\},                                   \tag{7.9}
\]

where \(\{t,a,b\}\) is the lock triple.  At an `S` position, exactly its
assigned positive cycle has odd incidence and the total is three, so the
nonzero cycle totals are \((3)\) or \((1,2)\).  Thus every lock triple is
carried by at most two selected cycles.  These are finite co-service gates
for a portal-cycle constructor, not merely aggregate parity conditions.

## 8. Universal radius-two escape from the S662 fractional support

Let \(S\) be the 662-seam positive support of the exact rational `SSSSS`
capacity point.  Its support graph has 571 vertices and three weak
components, so its integral circulation lattice has rank

\[
                         662-571+3=94.                    \tag{8.1}
\]

Using a deterministic spanning forest, take the 94 fundamental signed cycles
as a \(\mathbb Z\)-basis.  Map each cycle to its 93 target-service coordinates
and its seam count.  The resulting square integer matrix \(A\) has

\[
 \det A=-7,452,780,650,347,681,984,140,640\ne0.           \tag{8.2}
\]

The exact all-signature audit gives

\[
 \operatorname{rank}_{\mathbb F_2}A=90,
 \qquad \operatorname{rank}_{\mathbb F_5}A=93.           \tag{8.3}
\]

Four mod-two annihilators and one mod-five annihilator reject 1,013 of the
1,024 signature right-hand sides.  The eleven small-prime survivors are

```text
SS12S  S1S22  S2221  0SS2S  01020  01122
1110S  112SS  2S0S0  2S1S2  2S21S
```

and exact rational elimination gives a nontrivial denominator for every one.
Thus no signature supports even a signed integral balanced circulation wholly
on \(S\).

The same calculation yields a stronger full-catalogue statement.  There is
one explicitly audited cohomology label

\[
 \rho:E\longrightarrow\mathbb Z/M\mathbb Z,
 \qquad M=232899395323365062004395,                       \tag{8.4}
\]

which vanishes on \(S\) after an endpoint gauge and satisfies

\[
 \sum_e\rho(e)x_e\equiv r_\alpha\pmod M                 \tag{8.5}
\]

for every balanced signature-\(\alpha\) circulation.  Every one of the 1,024
residues \(r_\alpha\) is nonzero.  If exactly one seam \(e\notin S\) were
used, its endpoints would have to lie in the same support component, it would
have to satisfy \(s_e\le R(\alpha)\), and it would have to obey
\(\rho(e)=r_\alpha\).  Raw replay over all 211,604 seams finds zero such
signature/seam pairs at every \(R=0,\ldots,5\).  Hence every binary balanced
C106 solution uses at least two seams outside \(S\).

This is an all-signature global escape theorem, not merely the old local
`SSSSS` parity cut.

For `SSSSS` itself, the companion audit goes one radius farther.  Combining
the parity and mod-457 rows modulo 914 leaves exactly 208 structurally
balanced two-outside-seam packets (204 quotient-loop pairs and four quotient
two-cycles).  Complete membership tests for the signed support lattice reject
all 208: 198 first fail modulo 32, eight modulo 5 and two modulo 63079.
Consequently every binary `SSSSS` realization uses at least three seams
outside \(S\).  This is not an `SSSSS` no-go and does not extend to the other
1,023 signatures without a separate radius-two audit.

A complete GF(2) check also marks the limit of parity-only strengthening.
The `SSSSS` service/count/slack/balance right-hand side is parity-infeasible
on the 662 columns themselves (rank 658, augmented rank 659), but is feasible
on both the 1,317-column induced expansion (rank 664 on both sides) and the
16,481-column incident expansion (rank 8,170 on both sides).  The two-seam
CRT/lattice theorem therefore uses genuinely integer portal information;
there is no hidden one-hop GF(2) cut to promote.

There is also an exact completion test.  For a proposed outside packet
\(F\subseteq E\setminus S\), let \(b_F\) be its port divergence.  It can be
balanced by support seams only if \(b_F\) vanishes outside the support vertex
set and sums to zero on each of the three support components.  When this
holds, the fixed spanning forest gives a unique signed integral boundary
correction \(q_F\).  Every support completion is

\[
                         x_S=q_F+Cz,                     \tag{8.6}
\]

where \(C\) is the fundamental-cycle matrix, and its feature equations reduce
to the unique square system

\[
       Az=d_\alpha-\chi(F)-\chi(q_F).                    \tag{8.7}
\]

Thus \(F\) extends in the reduced capacity-one model if and only if the
solution of (8.7) is integral, \(q_F+Cz\) is binary, and
\(F\cup\operatorname{supp}(q_F+Cz)\) obeys port capacity.  Construction
should start at \(|F|=2\) in general, and at \(|F|=3\) for `SSSSS`, filtered
first by

\[
 \sum_{e\in F}s_e\le R(\alpha),\qquad
 \sum_{e\in F}\rho(e)\equiv r_\alpha\pmod M,            \tag{8.8}
\]

and the component-boundary equations.  This is a deterministic
residue-join/forest-completion construction, not a rounding heuristic.

The frozen proof is
`MATH_AUDIT_CC_K16_C106_ALL1024_SUPPORT662_LATTICE_ESCAPE_20260730.md`,
with checker and audit hashes recorded in Section 10.

## 9. The exact remaining boundary

The full source-relative C106 problem is not solved by this note.  What is
now rigorous is:

1. \(R=0\) and \(R=1\) are globally impossible by exact full-arc Farkas
   certificates;
2. every surviving branch has \(R\ge2\), at least \(8+R\) hitless seams, and
   at most \(R\) positive-slack portal seams;
3. every selected seam must satisfy the shortest-return inequality (5.2);
4. the complete return-capable fractional cut system is (6.4);
5. the exact integral object is the cycle packing (7.1).

The smallest unproved full-catalogue class is now \(R=2\): at most two
positive portals plus tight-cycle completion.  The exact full-arc `R=1`
Farkas theorem closes all 405 one-portal signatures and supersedes the old
truncated numerical census.  Conversely, the slack-at-most-one signed cycle
projection is all of \(\mathbb Z^{94}\), so no global GF(2), small-modulus,
or other finite-abelian character of service/count/slack can close
`R=2..4`; nonnegative cyclewise slack, capacity, or a restricted support is
essential.  A corrected all-arcs disjunctive SCIP run over the 270 fixed
`R=2` signatures reached its 1,200-second limit with status `NOT_SOLVED` and
no primal support; the parallel binary-WLOG run did the same.  Thus no fixed
`R=2` fractional signature has yet been authenticated, but these bounded
runs prove no exclusion.
For the `SSSSS` signature (\(R=5\)), any construction based on its exact
fractional support must begin with at least a three-seam outside packet and
pass (8.7); for each of the other 1,023 signatures only the lower bound of
two outside seams is proved.

Even a solution of (7.1) would settle only the balanced/service/capacity
layer.  Four-separation, reverse-edge exclusion, q1 restoration, survivor
shadows, residence, and literal physical replay would still have to be
checked.

## 10. Frozen inputs and new proof artifacts

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

scratch/k16_direct_cycle_dual_exact_20260730.audit.json
  SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d

scratch/ad_k16_c105_s0_repeat1x3_farkas_20260730.certificate.json
  SHA-256 3a8f9d1fa506b56ff2ae5d3a4463a647bfbdf4773ea5df961a3483299da2d582

scratch/k16_defect_provider_edge_cover_20260730.audit.json
  SHA-256 7e0d51edfa2c933eea20808e43ea1445672cfe25e60f68afe3ed11e05c56ed27

scratch/k16_c106_lock_normal_form_20260730.audit.json
  SHA-256 975f8847ecedb0c40ac5ba92aea03dab814cf004490bbf0fb6dc092f5bc3e2bb

MATH_CORRECTION_K16_C106_CONTINUOUS_ROW_SLACK_TRUNCATION_20260730.md
  SHA-256 f14650e37a3380a6757ff68d844725be7027bef8532f63405ae5ead7be2e659b

scratch/audit_a_k16_c106_r0_farkas_r1_scalar_failure_20260730.py
  SHA-256 0c76b1556bca4c5f19df33b1f32020ef6256b028cfb41a8db84b077170728143

scratch/a_k16_c106_r0_farkas_r1_scalar_failure_20260730.audit.json
  SHA-256 d1ed93a1bac2c2e0a57b4c9a6ecab7f7417b31a32ee640c453df2c28300aefed
  payload 2622dfca7e1e611588d0b052cb45624b275ae2f4d7b8a5c01269ec0e74bb61aa

MATH_AUDIT_A_K16_C106_R0_FARKAS_AND_R1_SCALAR_EXTENSION_FAILURE_20260730.md
  SHA-256 f9b39632ceb0ca5940408e66a6aaeeb9db454bc9aebd7975098ac2e270fb3ec4

scratch/audit_cc_k16_c106_all1024_support662_lattice_escape_20260730.py
  SHA-256 cefd0a3be53bb25703444d06122a5ea06946be70d44647edc8f71bdc875b769f

MATH_AUDIT_CC_K16_C106_ALL1024_SUPPORT662_LATTICE_ESCAPE_20260730.md
  SHA-256 e4094f29c240e0cef774e8d656e650dd3b51b3ee0394dd95b1a3c898fa76fa04

scratch/cc_k16_c106_all1024_support662_lattice_escape_20260730.audit.json
  SHA-256 d2470bbb431bb9a636e7bbc6f499661dd16b0c631d57281c1dff9eae447fe6b4
  payload 44ed046c10ccdd79d766b2396d78c8548923e95616eb28d0a0b9e600501b46dc

scratch/ad_k16_c106_sssss_crt914_radius2_v2_20260730.audit.json
  SHA-256 9dce75365e9ce98cd16f8096ea206803e8f83326919cc7b4e01e41ebcc62f4ff
  payload adb22c4a988aa28b21545a5fed645ebe7ea43a740878dffa46e14820d3f417b1

scratch/ad_k16_c106_sssss_crt914_radius2_pairs_replay_20260730.audit.json
  SHA-256 bd33a7a86c27aa45cbc6d9178165e90b065fb633309fa75478a8707820a3c26c

scratch/provider56_audit_k16_c106_sssss_crt914_radius2_lattice_20260730.py
  SHA-256 e1de952e5094b3b54b2fee261b8d0a334652fc4c71cf811c9066cd5696b10fc4

scratch/provider56_k16_c106_sssss_crt914_radius2_lattice_20260730.audit.json
  SHA-256 a84b4e07f8002d4f723c9ff476977f82ccd9568a575551e03b4f76a1584643f1
  payload b36c2c0d658b2e0bc42ee515a085b3e5b927caa741de74fc25db643637b1787b

scratch/threadB_k16_c106_sssss_incident_gf2_20260730.audit.json
  SHA-256 46fc83471f44c368ed9a352c0042c40f32d6f58b3a86fe62db08162baf509b25
  payload d225fcfc7d038c530693aa4c717350c6bb481545a1e14be51a01c6abc96bc38b

MATH_THEOREM_A_K16_C106_R1_FULL_ARC_EXACT_FARKAS_20260730.md
  SHA-256 39c55b6cb34721c1470a061e6e0fa3e7d5ee86703e6957794bf6617e0669385a

MATH_THEOREM_A_K16_C106_SATURATED_PORTAL_PARTITIONS_AND_MODULAR_BARRIER_20260730.md
  SHA-256 94bba350f38b3e69ff89a0d3c0df8bd92b7fbd5243a20831ad793b06371b85f8

scratch/floor106_R2_signature_mip_full.json
  SHA-256 b95b6bfc14ba1f215b35468ca7d96f9282df531ea97955fd268eb2544a884748
  payload 336bd1beecfd000d6587b97120ebc5379d7eae4d39bbdb61fb87f933a942c816

scratch/floor106_R2_signature_mip_binarywlog.json
  SHA-256 620d6fc4c0ca6f9758d355eec7137de0f3350543aa47f08b865362aabfb7e497
  payload 70e4472465c75d9e0a59942ac1932d29a311291a6b1dd05dd3baabfe6fcbcd48
```

No C105 solve was rerun.  The immutable frozen source bundle was not changed;
the explanatory floor106 and equality-face theorem notes were updated.
