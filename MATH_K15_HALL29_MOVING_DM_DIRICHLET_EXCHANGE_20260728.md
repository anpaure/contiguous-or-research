# The \(k=15\) Hall-29 moving-DM potential

## Exact exchange current, projection energy, and the fourth-parent obstruction

Date: 2026-07-28

Lane: C, exact \(k=15\) lower-compiler completion.

Method: pure mathematics. The numerical statements used below are the
already frozen exact audits; no new search, SAT call, or numerical experiment
is used here.

## 0. Verdict

There is an exact relocation-aware Hall potential on the physical compiler
graph. There is also a smooth projection/Dirichlet energy with a unique
moving dual. The first follows every maximizing DM witness exactly; the
second responds to every relocated Hall defect through its dual and
layer-cake formula. They lead to literal exchange criteria.

Neither a generic spectral gap on the parent-selection graph nor the current
non-orbit-complete finite list of frozen DM cuts can force either potential
to vanish.

For a legal carrier \(P\), let \(G_P\) be its exact lower-compiler bipartite
graph. If \(\mathcal T\) is the lower-target set and \(\mathcal C\) is the
physical compiler-cell set, put

\[
 h_P(A)=|N_{G_P}(A)|,
 \qquad
 g_P(A)=|A|-h_P(A).
\tag{0.1}
\]

The exact Hall-Lovász potential is

\[
 \boxed{
 \delta(P)
 =\max_{A\subseteq\mathcal T}g_P(A)
 =\max_{0\le w\le1}
 \left[
   \sum_{t\in\mathcal T}w_t
   -\sum_{c\in\mathcal C}
        \max_{t\in\Gamma_P(c)}w_t
 \right].}
\tag{0.2}
\]

Here \(\Gamma_P(c)\) is the exact target shore of cell \(c\), and the maximum
over an empty shore is zero.

For a legal exchange \(P\to Q\), define

\[
 v_{P,Q}(A)=h_Q(A)-h_P(A).
\tag{0.3}
\]

If \(d=\delta(P)>0\), then

\[
 \boxed{
 \delta(Q)\le d-1
 \iff
 v_{P,Q}(A)\ge g_P(A)-d+1
 \quad\text{for every }A\subseteq\mathcal T.}
\tag{CED}
\]

Thus improving the current canonical DM block is not enough. Every current
maximum witness must gain at least one neighbour, every level-\((d-1)\)
witness may not lose a neighbour, and every lower witness may lose only its
exact distance below level \(d-1\).

There is also a smooth objective. Let \(\mathcal P_P\) be the polytope of
fractional target loads supplied by unit-capacity compiler cells. Then

\[
 \boxed{
 \mathscr E(P)=\frac12\operatorname {dist}
          (\mathbf 1,\mathcal P_P)^2}
\tag{0.4}
\]

vanishes exactly at Hall-zero carriers and has the exact dual

\[
 \boxed{
 \mathscr E(P)=\max_{y\ge0}
 \left[
  \sum_ty_t-\frac12\sum_ty_t^2
  -\sum_c\max_{t\in\Gamma_P(c)}y_t
 \right].}
\tag{0.5}
\]

The maximizer \(y_P\in[0,1]^{\mathcal T}\) is unique. Its level sets are the
Hall families in a layer-cake formula, so it is a smoothed moving DM dual.

The new fourth parent gives a sharp obstruction to every frozen version of
this idea. Let \(H=H_{29}\) and \(\tau=(10\ 11)\), using the zero-indexed
coordinate convention of the frozen carrier files. Coordinate covariance
gives

\[
 \delta(\tau H)=\delta(H)=29.
\tag{0.6}
\]

Nevertheless, \(\tau H\) clears the three accumulated old witness families
by exact slacks \(55,343,321\), and all seven old zero-candidate targets have
positive multiplicities

\[
                         (4,1,2,1,3,3,3).
\tag{0.7}
\]

Its deficiency has moved to the transported \(1524-1495\) block
\(\tau A_{29}\). Hence every nonnegative violation objective using only the
three old witness families and seven old zeros has a literal false zero at
\(\tau H\).

The old two-parent Hall-zero UNSAT theorem gives a second obstruction. On
that finite legal carrier space, every Hall-detecting objective has a
positive-deficiency global, hence local, minimizer. A killed Dirichlet gap on
the carrier-state graph is positive exactly when every state component
already meets the Hall-zero boundary. Such a gap cannot replace the missing
accessibility theorem.

The surviving exact statement is:

> **Moving-DM exchange gate.** At every deficient legal carrier in the
> four-parent directed catalogue, find a legal alternating exchange
> satisfying (CED), or prove the quantitative moving-dual inequality
> \(\gamma_{P,Q}(y_P)>\Xi(P,Q)^2/2\) from (4.11). This makes every local
> minimum Hall zero. A deficient carrier with no such exchange is a literal
> obstruction.

This report proves the potential, exchange calculus, and this obstruction. It
does not claim Hall zero in the four-parent space.

## 1. Exact carrier and compiler spaces

Let

\[
 V=\binom{[15]}8,\qquad |V|=W=6435.
\tag{1.1}
\]

Adjoin a dummy vertex \(\partial\) to a Hamilton path on \(V\). Its successor
map is a perfect matching between source and target copies of
\(V\cup\{\partial\}\). A directed parent catalogue is a union of such
matchings. A selected successor matching is a legal carrier when:

1. it is one directed cycle through \(\partial\), hence one Hamilton path
   after deleting \(\partial\);
2. it has zero depth-three residence defects; and
3. it has complete upper shadows at depths \(1,\ldots,7\).

Two legal carriers are adjacent when their successor matchings differ on one
alternating assignment cycle and the switched matching remains legal. This
is the **legal exchange graph**. The unrestricted Boolean parent cube is not
the relevant graph.

The current four-parent catalogue is

\[
 H_{29},\qquad H_{30},\qquad H_{31},\qquad
 \tau H_{29},\qquad \tau=(10\ 11).
\tag{1.2}
\]

The fourth parent contributes \(3602\) directed successor arcs not present
in the preceding three-parent union. It genuinely enlarges the carrier
space, even though it is coordinate-isomorphic to \(H_{29}\).

The lower-target set is

\[
 \mathcal T=\{X\subseteq[15]:1\le |X|\le7\},
 \qquad |\mathcal T|=2^{14}-1=16383.
\tag{1.3}
\]

At depth three, the three lower OR-Pascal rows have \(W+3,W+2,W+1\)
physical cell addresses, respectively. Thus

\[
                         |\mathcal C|=19311.
\tag{1.4}
\]

For a carrier \(P\), the literal compiler rules, including both endpoint
collars, assign a target shore \(\Gamma_P(c)\subseteq\mathcal T\) to every
\(c\in\mathcal C\). The compiler graph \(G_P\) contains edge \(tc\) exactly
when \(t\in\Gamma_P(c)\). Hall zero means a matching saturating all \(16383\)
target vertices. The cell shore is larger; no balanced-graph assumption is
made.

## 2. Hall-Lovász dual and the DM lattice

### Theorem 2.1 — exact all-witness dual

For \(w\in[0,1]^{\mathcal T}\), define

\[
 \mathcal L_P(w)
 =\sum_{t\in\mathcal T}w_t
  -\sum_{c\in\mathcal C}\max_{t\in\Gamma_P(c)}w_t.
\tag{2.1}
\]

Then

\[
 \delta(P)
 :=|\mathcal T|-\nu(G_P)
 =\max_{A\subseteq\mathcal T}g_P(A)
 =\max_{0\le w\le1}\mathcal L_P(w).
\tag{2.2}
\]

#### Proof

The first equality is Hall's deficiency formula. For
\(A_s=\{t:w_t\ge s\}\), layer cake gives

\[
 \sum_tw_t=\int_0^1|A_s|\,ds.
\tag{2.3}
\]

For a fixed cell \(c\),

\[
 \max_{t\in\Gamma_P(c)}w_t
 =\int_0^1
   \mathbf 1_{\{\Gamma_P(c)\cap A_s\ne\varnothing\}}\,ds.
\tag{2.4}
\]

Summing over cells yields

\[
 \mathcal L_P(w)
 =\int_0^1\bigl(|A_s|-h_P(A_s)\bigr)\,ds
 \le\max_Ag_P(A).
\tag{2.5}
\]

Conversely, \(w=\mathbf1_A\) gives
\(\mathcal L_P(w)=g_P(A)\). This proves (2.2). \(\square\)

### Lemma 2.2 — maximum witnesses form a lattice

The function \(h_P\) is submodular and \(g_P\) is supermodular. Therefore the
families attaining \(\delta(P)\) are closed under union and intersection.
Their union is the unique inclusion-maximal maximizing target shore. This
need not be the particular alternating-reachable DM witness returned by a
matching implementation.

#### Proof

For each cell \(c\), the function
\(A\mapsto\mathbf1_{\{A\cap\Gamma_P(c)\ne\varnothing\}}\) is submodular.
Their sum is \(h_P\). Hence \(g_P=|A|-h_P(A)\) is supermodular. If \(A,B\)
both attain \(\delta\), then

\[
 g_P(A\cup B)+g_P(A\cap B)
 \ge g_P(A)+g_P(B)=2\delta.
\]

Neither term on the left exceeds \(\delta\), so both equal \(\delta\).
\(\square\)

## 3. Exact compiler current under an exchange

For a legal exchange \(P\to Q\), identity (0.3) gives

\[
                         g_Q(A)=g_P(A)-v_{P,Q}(A).
\tag{3.1}
\]

### Theorem 3.1 — complete exchange-descent criterion

If \(d=\delta(P)>0\), then (CED) holds.

#### Proof

The inequality \(\delta(Q)\le d-1\) is equivalent to
\(g_Q(A)\le d-1\) for every \(A\). Substitute (3.1) and rearrange.
\(\square\)

Compiler cells on the right shore are indistinguishable unit-capacity
vertices. Define the relabelling-invariant changed-shore count

\[
 m^*(P,Q)=
 \min_{\pi:\mathcal C\to\mathcal C\ {\rm bijective}}
 |\{c:\Gamma_P(c)\ne\Gamma_Q(\pi(c))\}|.
\tag{3.2a}
\]

Each changed shore alters \(h(A)\) by at most one, so

\[
 |v_{P,Q}(A)|\le m^*(P,Q)
 \quad\text{for every }A.
\tag{3.2}
\]

Consequently (CED) need only be checked on the near-critical family

\[
                         g_P(A)\ge d-m^*(P,Q).
\tag{3.3}
\]

Indeed, if (3.3) fails, integrality gives
\(g_P(A)\le d-m^*(P,Q)-1\). The right side of (CED) is then at most
\(-m^*(P,Q)\), which is automatic from (3.2).

### Proposition 3.2 — fractional exchange dual

Fix a finite family \(\mathcal Q(P)\) of legal candidate exchanges and put

\[
                         b_A=g_P(A)-d+1.
\tag{3.4}
\]

There is a probability vector \((\lambda_Q)\) satisfying

\[
 \sum_Q\lambda_Qv_{P,Q}(A)\ge b_A
 \quad\text{for every }A
\tag{3.5}
\]

if and only if, for every finitely supported \(y_A\ge0\),

\[
 \boxed{
 \max_{Q\in\mathcal Q(P)}
       \sum_Ay_Av_{P,Q}(A)
 \ge \sum_Ay_Ab_A.}
\tag{3.6}
\]

#### Proof

Condition (3.5) says that \(b=(b_A)\) lies in the downward closure of the
convex hull of the vectors \(v_{P,Q}\). Separation from this closed convex
set gives a nonnegative normal \(y\), and exactly (3.6). Conversely, failure
of (3.5) gives such a separator. \(\square\)

This is only fractional simultaneous descent. An actual exchange follows if
the exchange family has **dominance-integrality**:

\[
 b\le\sum_Q\lambda_Qv_{P,Q}
 \quad\Longrightarrow\quad
 \exists Q:\ b\le v_{P,Q}.
\tag{3.7}
\]

The exact old two-parent UNSAT theorem shows that (3.7) cannot be inferred
merely from an assignment-cycle parametrization: at a blocked state, either
the fractional condition (3.6) fails or its conversion to one integral
exchange fails. Hamilton connectivity, residence, upper coverage, and the
common compiler chronology couple the exchange bits.

### Proposition 3.3 — literal alternating matching current

Fix a maximum matching \(M\) of \(G_P\). For a legal exchange \(P\to Q\), let

\[
 r=|M\setminus E(G_Q)|,
 \qquad M_0=M\cap E(G_Q).
\tag{3.8}
\]

Let \(\alpha_Q(M_0)\) be the number of \(M_0\)-augmenting components in the
symmetric difference with a maximum matching of \(G_Q\). Then

\[
 \boxed{
 \delta(Q)-\delta(P)=r-\alpha_Q(M_0).}
\tag{3.9}
\]

Thus deficiency strictly decreases exactly when the new compiler graph
supports more augmentations than the number of old matched edges destroyed.

#### Proof

The retained matching has size

\[
 |M_0|=|\mathcal T|-\delta(P)-r.
\]

If \(M_Q\) is a maximum matching of \(G_Q\), the symmetric difference
\(M_0\triangle M_Q\) is a disjoint union of alternating cycles and paths.
It has no component containing one more \(M_0\)-edge than \(M_Q\)-edge:
flipping \(M_Q\) on such a component would augment the supposedly maximum
matching \(M_Q\), because every edge of \(M_0\) belongs to \(G_Q\).
Consequently its \(M_0\)-augmenting components number
\(|M_Q|-|M_0|\). Hence

\[
 |M_Q|=|M_0|+\alpha_Q(M_0).
\]

Subtract from \(|\mathcal T|\) to obtain (3.9). \(\square\)

This current is compiler-specific. Novel successor-arc counts and nonzero
singleton-target counts do not determine it.

### Proposition 3.4 — the old seam subadditivity is dual subadditivity

For factorable linear pieces \(P,Q,PQ\), the audited compiler theorem gives

\[
                         h_{PQ}(A)\le h_P(A)+h_Q(A)
\tag{3.10}
\]

for every target family \(A\). Consequently, for every \(y\ge0\),

\[
                         H_{PQ}(y)\le H_P(y)+H_Q(y),
\qquad
 H_P(y)=\sum_c\max_{t\in\Gamma_P(c)}y_t.
\tag{3.11}
\]

#### Proof

Apply (3.10) to the level sets \(A_s=\{t:y_t\ge s\}\), use

\[
 H_P(y)=\int_0^\infty h_P(A_s)\,ds,
\]

and integrate. \(\square\)

Thus a fixed-piece concatenation has nonpositive seam correction at every
dual vector, not only at one frozen DM indicator. A directed-parent escape
must create useful intrinsic local compiler words through genuinely new
successor arcs; it cannot treat ordinary component gluing as a positive heat
conductance.

## 4. Smooth Hall projection energy

Let \(\mathcal P_P\subseteq\mathbb R_{\ge0}^{\mathcal T}\) consist of all
load vectors \(p\) for which there are \(f_{tc}\ge0\) satisfying

\[
 p_t=\sum_{c:t\in\Gamma_P(c)}f_{tc},
 \qquad
 \sum_{t\in\Gamma_P(c)}f_{tc}\le1
 \quad(c\in\mathcal C).
\tag{4.1}
\]

### Theorem 4.1 — projection/Fenchel theorem

The energy (0.4) has these properties:

1. \(\mathscr E(P)=0\) exactly when \(G_P\) has a target-saturating matching.
2. Its exact dual is (0.5).
3. The dual maximizer \(y_P\) is unique and belongs to
   \([0,1]^{\mathcal T}\).
4. If \(A\) has deficiency \(a=|A|-h_P(A)>0\), then

   \[
                    \mathscr E(P)\ge\frac{a^2}{2|A|}.
   \tag{4.2}
   \]

5. Conversely, \(\mathscr E(P)\le\delta(P)/2\).

#### Proof

If \(\mathbf1\in\mathcal P_P\), (4.1) is a fractional matching saturating
every target. The bipartite matching polytope is integral, so an integral
target-saturating matching exists. The converse is immediate.

For \(y\ge0\), the support function of \(\mathcal P_P\) is

\[
 \sigma_{\mathcal P_P}(y)
 =\sum_{c\in\mathcal C}\max_{t\in\Gamma_P(c)}y_t.
\tag{4.3}
\]

Fenchel duality for squared distance gives

\[
 \frac12\operatorname {dist}(\mathbf1,\mathcal P_P)^2
 =\max_y
 \left[
   \langle\mathbf1,y\rangle-\frac12\|y\|_2^2
   -\sigma_{\mathcal P_P}(y)
 \right].
\tag{4.4}
\]

Because \(\mathcal P_P\) is down-closed, replacing negative coordinates of
\(y\) by zero cannot decrease the objective. The quadratic term makes the
objective strictly concave, hence the maximizer is unique. Equivalently,

\[
 y_P=\mathbf1-\operatorname {proj}_{\mathcal P_P}(\mathbf1).
\]

Down-closedness permits the projection to be chosen coordinatewise at most
one, so \(0\le y_P\le1\).

Choose \(y=\alpha\mathbf1_A\) in (0.5). Its value is

\[
                         \alpha a-\frac12\alpha^2|A|.
\]

The choice \(\alpha=a/|A|\le1\) proves (4.2). A maximum matching leaves
\(\delta(P)\) targets unmatched. Its \(0/1\) load vector lies in
\(\mathcal P_P\) and has squared distance \(\delta(P)\) from \(\mathbf1\),
proving the upper bound. \(\square\)

Consequently, on any legal carrier family which contains a Hall-zero state,
the global minimizers of \(\mathscr E\) are exactly the Hall-zero carriers.
This is an exact objective theorem. What remains nonformal is proving that
the four-parent family contains such a state, or proving the local exchange
condition which forces one.

The nonquadratic part of (0.5) has the layer-cake form

\[
 \sum_ty_t-\sum_c\max_{t\in\Gamma_P(c)}y_t
 =\int_0^1g_P(A_s)\,ds,
 \qquad A_s=\{t:y_t\ge s\}.
\tag{4.5}
\]

For the frozen Hall-29 witness,

\[
 |A_{29}|=1524,\qquad h_H(A_{29})=1495.
\]

Therefore

\[
 \boxed{
 \mathscr E(H)\ge\frac{29^2}{2\cdot1524}
 =\frac{841}{3048}.}
\tag{4.6}
\]

### Theorem 4.2 — exact exchange inequalities

Put

\[
 H_P(y)=\sum_c\max_{t\in\Gamma_P(c)}y_t,
 \qquad
 \gamma_{P,Q}(y)=H_Q(y)-H_P(y).
\tag{4.7}
\]

Every legal exchange \(P\to Q\) satisfies

\[
 -\gamma_{P,Q}(y_P)
 \le\mathscr E(Q)-\mathscr E(P)
 \le-\gamma_{P,Q}(y_Q),
\tag{4.8}
\]

and

\[
 \gamma_{P,Q}(y_P)-\gamma_{P,Q}(y_Q)
 \ge\|y_P-y_Q\|_2^2.
\tag{4.9}
\]

If \(\Xi(P,Q)\) is the \(\ell_2\)-Lipschitz constant of
\(\gamma_{P,Q}\), then

\[
 \boxed{
 \mathscr E(Q)
 \le\mathscr E(P)-\gamma_{P,Q}(y_P)
       +\frac{\Xi(P,Q)^2}{2}.}
\tag{4.10}
\]

In particular,

\[
 \gamma_{P,Q}(y_P)>\frac{\Xi(P,Q)^2}{2}
\tag{4.11}
\]

is a rigorous compiler-linked descent certificate.

#### Proof

Write

\[
 F_P(y)=\sum_ty_t-\frac12\|y\|_2^2-H_P(y).
\]

Then \(F_Q=F_P-\gamma_{P,Q}\), and \(y_P,y_Q\) maximize \(F_P,F_Q\).
Evaluating \(F_Q\) at \(y_P\) gives the lower bound in (4.8). Evaluating
\(F_P(y_Q)\le F_P(y_P)\) gives the upper bound.

Both \(F_P\) and \(F_Q\) are one-strongly concave. Apply strong concavity at
their maximizers and add the inequalities; the \(F_P\) terms cancel and give
(4.9).

Strong concavity also gives

\[
 \mathscr E(Q)-\mathscr E(P)
 \le-\gamma_{P,Q}(y_Q)
      -\frac12\|y_P-y_Q\|_2^2.
\]

Use

\[
 -\gamma_{P,Q}(y_Q)
 \le-\gamma_{P,Q}(y_P)
    +\Xi(P,Q)\|y_P-y_Q\|_2
\]

and maximize \(\Xi x-x^2/2\) over \(x\ge0\). This proves (4.10).
\(\square\)

The criterion is physically local. To bound \(m^*(P,Q)\), pair an old and
new interior cell of the same row depth whenever their complete local vertex
words agree; equivalently, pair unchanged windows by their leading middle
vertex inside a common directed segment. Put

\[
                         s=|E(P)\triangle E(Q)|,
\]

counting both removed and added directed successor arcs. Canonically identify
the remaining equal local words. Every unpaired local word contains an arc of
\(E(P)\triangle E(Q)\). The exact depth-three cell motifs use
\(10,11,12\) consecutive middle vertices. An arc belongs to at most
\(9+10+11=30\) such windows, and there are at most \(18\) cells in each
endpoint collar. Hence the proof-safe bound is

\[
                         m^*(P,Q)\le30s+36.
\tag{4.12}
\]

The actual \(\Xi(P,Q)\) is the collision norm of the changed cell support
functions. It can be much smaller than the crude count in (4.12), but it is
not determined by raw successor-arc novelty.

## 5. Exact fourth-parent obstruction

Let \(H=H_{29}\). Its frozen data are

\[
 \delta(H)=29,\qquad
 |A_{29}|=1524,\qquad h_H(A_{29})=1495,
\tag{5.1}
\]

and its seven zero-candidate targets are

\[
 Z=\{2575,5801,13616,13620,17738,21641,29776\}.
\tag{5.2}
\]

### Lemma 5.1 — coordinate covariance

For every coordinate permutation \(\sigma\),

\[
 h_{\sigma P}(\sigma A)=h_P(A),\qquad
 \delta(\sigma P)=\delta(P),\qquad
 \mathscr E(\sigma P)=\mathscr E(P),\qquad
 y_{\sigma P}=\sigma y_P.
\tag{5.3}
\]

#### Proof

Relabelling maps every target, middle mask, exact compiler envelope,
mandatory mask, and endpoint collar bijectively to its relabelled
counterpart. Hence \(G_P\cong G_{\sigma P}\). It also maps
\(\mathcal P_P\) isometrically to \(\mathcal P_{\sigma P}\). The identities
follow, with uniqueness used for the dual maximizer. \(\square\)

Take \(\tau=(10\ 11)\). The exact fourth-parent screen gives

\[
\begin{array}{c|c|c|c}
 A&|A|&h_{\tau H}(A)&h_{\tau H}(A)-|A|\\ \hline
 A_{29}&1524&1579&55\\
 R_3&1530&1873&343\\
 R_4&1374&1695&321.
\end{array}
\tag{5.4}
\]

The exact multiplicities of the old zero targets in \(\tau H\) are

\[
                         (4,1,2,1,3,3,3).
\tag{5.5}
\]

Yet Lemma 5.1 gives

\[
 |\tau A_{29}|=1524,\qquad
 h_{\tau H}(\tau A_{29})=1495,\qquad
 \delta(\tau H)=29.
\tag{5.6}
\]

The transported zero set is

\[
 \tau Z=
 \{1551,6825,14640,14644,18762,22665,30800\},
\tag{5.7}
\]

which is disjoint from \(Z\).

### Corollary 5.2 — every frozen-witness violation objective has a false zero

Let \(\Phi(P)\) be any nonnegative sum, maximum, quadratic penalty, or
lexicographic collection of terms depending only on

\[
 [|A|-h_P(A)]_+,
 \qquad A\in\{A_{29},R_3,R_4\},
\]

and on whether a target in \(Z\) has zero neighbourhood. If \(\Phi=0\)
whenever all these tests pass, then

\[
                         \Phi(\tau H)=0
                         \quad\text{but}\quad
                         \delta(\tau H)=29.
\tag{5.8}
\]

Thus optimizing minimum old-DM slack and old zero-target counts cannot force
Hall zero.

This does not make the fourth parent useless. Its \(3602\) novel arcs can
matter in mixed alternating exchanges. It says that the endpoint parent and
its frozen profile vector do not themselves constitute descent.

Every coordinate-invariant quadratic or target-harmonic energy is also flat
between \(H\) and \(\tau H\). If \(K\) commutes with the coordinate action
and \(u(\sigma P)=U_\sigma u(P)\), then

\[
 u(\tau H)^TKu(\tau H)=u(H)^TKu(H).
\tag{5.9}
\]

The full projection energy is invariant but not blind: it remains positive
at both endpoints and moves its unique dual from \(y_H\) to \(\tau y_H\).
For the whole-parent exchange, (4.8)-(4.9) give

\[
 \gamma_{H,\tau H}(y_H)-\gamma_{H,\tau H}(\tau y_H)
 \ge\|y_H-\tau y_H\|_2^2,
\tag{5.10}
\]

while \(\mathscr E(H)=\mathscr E(\tau H)\).

## 6. Two-parent UNSAT and the spectral obstruction

The exhausted old directed cube is generated by \(H_{30}\) and its image
under \((0\ 5)(2\ 13)\). After the dummy-path reduction it has \(1570\)
assignment components, \(879\) fixed and \(691\) nontrivial. The exact
full-boundary model proves that no resident, all-upper-exact Hamilton state
in this cube has Hall deficiency zero.

The Hall-29 state has the witness (5.1). A legal seven-component state in the
same cube raises the neighbourhood of this old witness to \(1795\), a gain of
\(300\), but has a complementary \(1524-1495\) DM block. Requiring both exact
full-boundary inequalities makes the model UNSAT. The exhaustive
eight-component subcube omitted by the Hall-29 state has \(22\) valid
non-parent states, all of deficiency \(29\) or \(30\).

Therefore:

1. large current on the current canonical witness does not imply (CED);
2. on this finite legal state space, \(\delta\), \(\mathscr E\), and every
   other Hall-detecting objective attain a minimum at positive deficiency;
3. no strict descent theorem holds at every deficient state; and
4. raw assignment-component expansion cannot supply a Hall-zero state.

This has an exact Dirichlet formulation. Let \(\Omega\) be a finite legal
exchange graph with positive vertex weights, and let

\[
 Z_0=\{P\in\Omega:\delta(P)=0\},
\]

and give each legal exchange edge positive conductance. The killed Poincaré
inequality

\[
 \frac12\sum_{P\sim Q}c_{PQ}(f(P)-f(Q))^2
 \ge\lambda\sum_{P\notin Z_0}\pi(P)f(P)^2,
 \qquad f|_{Z_0}=0,
\tag{6.1}
\]

has \(\lambda>0\) if and only if every connected component of \(\Omega\)
meets \(Z_0\).

Indeed, a component disjoint from \(Z_0\) supplies a nonzero constant
zero-energy function. Conversely, on a finite component meeting the zero
boundary, a zero-energy function is constant and therefore zero; compactness
of the unit sphere gives a positive minimum Rayleigh quotient. A killed
spectral gap already contains the Hall-zero accessibility theorem.

Even perfect averaged Hall marginals are insufficient. Take two targets
\(\{1,2\}\), two cells \(\{a,b\}\), and two states. In state \(P_0\), both
cells accept only target \(1\); in state \(P_1\), both accept only target
\(2\). Each state has deficiency one. The two-state chain which jumps to the
uniform distribution in one step has spectral gap one, and

\[
 \mathbb Eh_P(\{1\})=\mathbb Eh_P(\{2\})=1,\qquad
 \mathbb Eh_P(\{1,2\})=2.
\]

Every averaged Hall inequality holds, but no integral state is Hall zero.
The obstruction is

\[
 \mathbb E\max_Ag_P(A)\ge\max_A\mathbb Eg_P(A).
\tag{6.2}
\]

The exact two-parent UNSAT is the physical \(k=15\) obstruction behind this
dichotomy. By itself it does not decide whether the failure is already a
fractional Farkas obstruction of the form (3.6), or whether the fractional
system is feasible and the remaining failure is integral selection.

## 7. Precise four-parent gate

Let \(\Omega_4\) be the legal state space generated by (1.2). The following
condition is sufficient and contains no hidden heat assumption.

### Moving-DM descent condition \(\mathrm{MDEC}_4\)

For every \(P\in\Omega_4\) with \(d=\delta(P)>0\), there is a legal exchange
\(P\to Q\) satisfying one, hence all, of

\[
 \delta(Q)\le d-1;
\tag{7.1}
\]

\[
 v_{P,Q}(A)\ge g_P(A)-d+1
 \quad\text{for every }A\subseteq\mathcal T;
\tag{7.2}
\]

\[
 \alpha_Q(M\cap E(G_Q))>|M\setminus E(G_Q)|
\tag{7.3}
\]

for a maximum matching \(M\) of \(G_P\), with \(\alpha_Q\) as in
Proposition 3.3.

If \(\mathrm{MDEC}_4\) holds, repeated exchange reaches Hall zero after at
most \(\delta(P_0)\) strict steps, and every local or global minimum of
\(\delta\) is Hall zero. The stronger smooth condition (4.11) at every
positive-energy state makes every local minimum of \(\mathscr E\) Hall zero.

The fourth-parent screen does not establish (7.1)-(7.3). It records
whole-parent fixed-family neighbourhoods and singleton-target counts. The
exact additional data required for an exchange are:

1. the changed compiler shores \(\Gamma_Q(c)\), including both endpoint
   collars;
2. \(v_{P,Q}(A)\) on the near-critical family (3.3), or the matching current
   (3.9);
3. the moving-dual gain \(\gamma_{P,Q}(y_P)\) and collision norm \(\Xi\); and
4. literal Hamilton, residence, and all-upper legality of the same exchange.

The orbit of \(A_{29}\) under the parent permutations must at least be
included in any finite cut catalogue: coordinate covariance forces every
relabelled endpoint to carry the transported obstruction. The two-parent
complementary block shows that this orbit need not be complete. Dynamic DM
separation or the all-witness dual (0.2)/(0.5) is essential.

The proved boundary is:

- a relocation-aware compiler potential and exact exchange current now
  exist;
- frozen-cut and unanchored spectral objectives are rigorously insufficient;
- the old two-parent state space is exactly closed at Hall zero;
- the fourth parent genuinely enlarges the arc catalogue but is itself an
  isometric Hall-29 endpoint; and
- Hall zero in the four-parent space requires the integral moving-DM exchange
  condition, not a generic heat or expansion estimate.

## 8. Frozen inputs

The exact finite facts used above are recorded in:

- scratch/k15_doubletrans_05_213_hall29.json and its Hall/DM sidecars;
- scratch/h29cube_exact_benders8.json;
- scratch/k15_transposition_parent_screen.json;
- scratch/fourth_parent_analytic_screen.json;
- scratch/fourth_parent_p3_screen.json;
- scratch/k15_h29_relabel_t10_11.json;
- K15_PORT_COMPATIBILITY_AND_DM_SUBADDITIVITY_20260728.md;
- K15_NATIVE_SEARCH_PORT_AUDIT_20260728.md; and
- EXACT_OR_FORMULA_SYSTEMATIZED_UNDERSTANDING_20260728.md.

No assertion here strengthens the frozen finite certificates. The new content
is the all-witness dual, exact compiler-current criterion, smooth projection
energy, exchange calculus, and the rigorous separation between a moving-DM
proof and a frozen-profile heat claim.
