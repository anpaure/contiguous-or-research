# Fine strip cover: exact LP dual and the owner-recycling integrality functional

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
 W=\binom{2m}m,\qquad
 N_q=\binom{2m}{m-q},
 \qquad 1\le H<h<m.
 \tag{0.1}
\]

For the whole-strip plus singleton cover program, the exact fractional
optimum is

\[
 \boxed{\tau^*=W+{H\over h}N_1.}
 \tag{0.2}
\]

A clean optimal dual certificate is

\[
 y_S=
 \begin{cases}
 1,&|S|=m,\\[1mm]
 H/(2h),&|S|=m-1\text{ or }m+1,\\[1mm]
 0,&2\le||S|-m|\le H.
 \end{cases}
 \tag{0.3}
\]

Every singleton constraint is satisfied, and every whole \(C_{2h}\)-strip
constraint is tight:

\[
 2h+2(2h){H\over2h}=2h+2H.
 \tag{0.4}
\]

Thus the lower bound does not depend on an aggregate relaxation of the
cycle columns; it is certified against every physical strip separately.

The integral excess also has an exact structural form. For a selected cycle
family \(\mathcal F\), let \(r_S(\mathcal F)\) be the number of selected
strips containing target \(S\). Put

\[
\begin{aligned}
 R_0(\mathcal F)
 &=\sum_{|S|=m}(r_S-1)_+,\\
 L_1(\mathcal F)
 &=|\{S:||S|-m|=1,\ r_S=0\}|,\\
 R_1(\mathcal F)
 &=\sum_{||S|-m|=1}(r_S-1)_+,\\
 L_{\ge2}(\mathcal F)
 &=|\{S:2\le||S|-m|\le H,\ r_S=0\}|.
\end{aligned}
\tag{0.5}
\]

Then

\[
 \boxed{
 \tau-\tau^*
 =\min_{\mathcal F\subseteq\mathscr C_{m,h}}
 \left[
 R_0+{H\over2h}R_1+
 \left(1-{H\over2h}\right)L_1+
 L_{\ge2}
 \right].}
 \tag{0.6}
\]

This is an exact equality, not a bound. Consequently the coefficient-one
integrality gate is equivalent to finding a whole-strip family satisfying

\[
 R_0=o(W),\qquad
 {H\over h}R_1=o(W),\qquad
 L_1=o(W),\qquad
 L_{\ge2}=o(W).
 \tag{0.7}
\]

Middle holes do not appear in (0.6). They are already priced optimally by
middle singleton columns. Middle **repetitions** do appear with unit cost:
this is the exact owner-recycling toll. Depth-one holes have asymptotic
unit cost, depth-one repetitions have the smaller exchange rate \(H/(2h)\),
and every deeper hole again costs one.

Equation (0.6) is the sharpest currently proved reformulation of
\(\tau-\tau^*=o(W)\). No theorem in this note proves that its minimum is
\(o(W)\). In particular, the dependent Hall and SCD-flag theorems select
owner-rooted faces or paths, not whole strip columns, and therefore do not
bound (0.6).

There is a rigorous obstruction to naive rounding. Uniform independent
sampling at the fractional cycle density, or uniform sampling of the
correct number of cycles, leaves

\[
 (2e^{-1}+o(1))N_1=\Theta(W)
 \tag{0.8}
\]

signed depth-one holes in expectation. Hence its expected integral excess
is \(\Omega(W)\). Any successful rounding must impose global
depth-one repulsion/coverage correlations; first moments and orbit symmetry
are insufficient.

## 1. The primal and its exact dual

Let

\[
 \mathcal B_{m,H}
 =\bigcup_{q=-H}^H\binom{[2m]}{m+q}
 \tag{1.1}
\]

and let \(\mathscr C_{m,h}\) be the physical cyclic \(h\)-strip catalogue.
Every \(C\in\mathscr C_{m,h}\) contains

* \(2h\) middle targets;
* \(2h\) lower targets and \(2h\) upper targets at every depth
  \(1\le q\le H\).

The strict inequality \(H<h\) makes all these targets distinct within
their signed layer.

The fractional cover program is

\[
\begin{aligned}
 \min\quad&
 (2h+2H)\sum_Cx_C+\sum_Sz_S,\\
 \text{subject to}\quad&
 z_S+\sum_{C:S\in\mathcal T_H(C)}x_C\ge1
 \qquad(S\in\mathcal B_{m,H}),\\
 &x_C,z_S\ge0.
\end{aligned}
\tag{1.2}
\]

Upper bounds \(x_C,z_S\le1\) may be added without changing the optimum:
positive costs and covering right-hand side one make larger values
unnecessary.

Its covering dual is

\[
\begin{aligned}
 \max\quad&\sum_Sy_S,\\
 \text{subject to}\quad&
 0\le y_S\le1\qquad(S\in\mathcal B_{m,H}),\\
 &\sum_{S\in\mathcal T_H(C)}y_S\le2h+2H
       \qquad(C\in\mathscr C_{m,h}).
\end{aligned}
\tag{1.3}
\]

### Theorem 1.1 (whole-column dual certificate)

The vector (0.3) is dual feasible, every whole-strip inequality is an
equality, and its objective is \(W+(H/h)N_1\).

#### Proof

The singleton inequalities \(0\le y_S\le1\) hold because
\(0<H/(2h)<1/2\).

Fix an arbitrary physical strip \(C\). It has \(2h\) middle targets, each
of dual weight one. It has \(2h\) targets in each of the two signed
depth-one layers, each of dual weight \(H/(2h)\). All its deeper targets
have dual weight zero. Therefore

\[
 \sum_{S\in\mathcal T_H(C)}y_S
 =2h+4h{H\over2h}
 =2h+2H.
 \tag{1.4}
\]

This checks the constraint for every strip, without averaging over the
catalogue. Finally,

\[
 \sum_Sy_S
 =W+2N_1{H\over2h}
 =W+{H\over h}N_1.
 \tag{1.5}
\]

Weak duality proves the required lower bound. \(\square\)

## 2. Matching primal certificate

For completeness, we independently construct a primal solution with the
same value.

Let \(D_q\) be the number of catalogue strips containing a fixed target in
one signed depth-\(q\) layer. Transitivity and double counting give

\[
 D_0={m!^2\over2(m-h)!^2},
 \tag{2.1}
\]

\[
 D_q={(m+q)!(m-q)!\over2(m-h)!^2}
 \qquad(1\le q<h).
 \tag{2.2}
\]

Indeed,

\[
 |\mathscr C_{m,h}|\,2h=WD_0=N_qD_q.
 \tag{2.3}
\]

Give every cycle the weight

\[
 x_C={1\over D_1}.
 \tag{2.4}
\]

Every signed depth-one target then has load one. A signed depth-\(q\)
target, \(q\ge1\), has load

\[
 {D_q\over D_1}={N_1\over N_q}\ge1.
 \tag{2.5}
\]

Every middle target has load

\[
 {D_0\over D_1}={N_1\over W}={m\over m+1}.
 \tag{2.6}
\]

Set

\[
 z_S=
 \begin{cases}
 1-N_1/W,&|S|=m,\\
 0,&|S|\ne m.
 \end{cases}
 \tag{2.7}
\]

This is primal feasible. Moreover,

\[
 \sum_Cx_C
 ={|\mathscr C_{m,h}|\over D_1}
 ={N_1\over2h}.
 \tag{2.8}
\]

Its objective is

\[
 (2h+2H){N_1\over2h}+W-N_1
 =W+{H\over h}N_1.
 \tag{2.9}
\]

Strong duality and Theorem 1.1 prove (0.2).

## 3. Exact complementary-slackness ledger for an integral family

Fix an arbitrary integral strip family
\(\mathcal F\subseteq\mathscr C_{m,h}\). For a target \(S\), put

\[
 r_S=r_S(\mathcal F)
 =|\{C\in\mathcal F:S\in\mathcal T_H(C)\}|.
 \tag{3.1}
\]

For this family, the cheapest singleton choice is forced:

\[
 z_S=\mathbf1_{\{r_S=0\}}.
 \tag{3.2}
\]

Let \(\tau(\mathcal F)\) be the resulting objective.

### Lemma 3.1 (exact dual-slack identity)

For every integral family,

\[
 \boxed{
 \tau(\mathcal F)-\tau^*
 =
 \sum_{r_S=0}(1-y_S)
 +\sum_{r_S\ge1}y_S(r_S-1),}
 \tag{3.3}
\]

where \(y\) is the dual vector (0.3).

#### Proof

Every selected strip is tight in the dual by (1.4). Hence

\[
 (2h+2H)|\mathcal F|
 =\sum_{C\in\mathcal F}
       \sum_{S\in\mathcal T_H(C)}y_S
 =\sum_Sy_Sr_S.
 \tag{3.4}
\]

Using (3.2) and \(\tau^*=\sum_Sy_S\),

\[
\begin{aligned}
 \tau(\mathcal F)-\tau^*
 &=\sum_S\bigl(y_Sr_S+\mathbf1_{\{r_S=0\}}-y_S\bigr)\\
 &=\sum_{r_S=0}(1-y_S)
   +\sum_{r_S\ge1}y_S(r_S-1).
\end{aligned}
\]

Every summand is nonnegative. \(\square\)

Substitution of the three dual weights gives the structural formula.

### Theorem 3.2 (owner-recycling collision--hole functional)

For every integral family,

\[
 \boxed{
 \tau(\mathcal F)-\tau^*
 =R_0(\mathcal F)
 +{H\over2h}R_1(\mathcal F)
 +\left(1-{H\over2h}\right)L_1(\mathcal F)
 +L_{\ge2}(\mathcal F).}
 \tag{3.5}
\]

Consequently (0.6) holds.

#### Proof

At the middle layer, an uncovered target has \(1-y_S=0\), while a target
of multiplicity \(r\ge1\) contributes \(r-1\). At either depth-one layer,
an uncovered target contributes \(1-H/(2h)\), while a covered target
contributes \((H/(2h))(r-1)\). At every deeper layer, an uncovered target
contributes one and repetitions contribute zero. This is exactly (3.5).
Minimizing over \(\mathcal F\) proves (0.6). \(\square\)

The identity explains the term “owner recycling.” Reusing a middle mask in
another selected strip costs exactly one unit per extra incidence, even
though no owner-packing constraint was imposed.

## 4. Exact structural equivalences

All four terms in (3.5) are nonnegative, and

\[
 1-{H\over2h}>{1\over2}.
 \tag{4.1}
\]

### Corollary 4.1 (sharp equivalent gate)

The statement

\[
 \tau-\tau^*=o(W)
 \tag{4.2}
\]

is equivalent to the existence of an integral strip family satisfying

\[
\begin{aligned}
 R_0&=o(W),\\
 {H\over h}R_1&=o(W),\\
 L_1&=o(W),\\
 L_{\ge2}&=o(W).
\end{aligned}
\tag{4.3}
\]

No condition on the number of uncovered middle targets is required.

This separates the exact physical tasks:

1. almost all middle incidences must be first incidences;
2. almost every signed depth-one target must be hit;
3. depth-one repetitions are allowed up to the cheaper scale
   \(o(Wh/H)\);
4. the aggregate number of holes at depths \(2,\ldots,H\) must be \(o(W)\).

Let \(k=|\mathcal F|\). Total signed depth-one incidence gives the exact
identity

\[
 4hk=2N_1-L_1+R_1.
 \tag{4.4}
\]

Hence

\[
 k={N_1\over2h}+{R_1-L_1\over4h}.
 \tag{4.5}
\]

Under (4.3),

\[
 k={N_1\over2h}+o(W/H).
 \tag{4.6}
\]

Thus a successful family automatically has the fractional optimum's cycle
mass to the accuracy required by the literalization toll; this does not
have to be imposed separately.

### Corollary 4.2 (maximum-surplus form)

Let

\[
 U(\mathcal F)=\bigcup_{C\in\mathcal F}\mathcal T_H(C).
 \tag{4.7}
\]

Then

\[
 \tau
 =|\mathcal B_{m,H}|
 -\max_{\mathcal F\subseteq\mathscr C_{m,h}}
 \left(|U(\mathcal F)|-(2h+2H)|\mathcal F|\right).
 \tag{4.8}
\]

Consequently

\[
\begin{aligned}
 \tau-\tau^*
 &=
 |\mathcal B_{m,H}|-W-{H\over h}N_1\\
 &\quad-
 \max_{\mathcal F}
 \left(|U(\mathcal F)|-(2h+2H)|\mathcal F|\right).
\end{aligned}
\tag{4.9}
\]

This is an exact maximum-coverage min--max reformulation. It contains no
owner variables and makes no owner-disjointness assumption.

## 5. A rigorous obstruction to orbitwise independent rounding

Let

\[
 M=|\mathscr C_{m,h}|.
 \tag{5.1}
\]

Recall

\[
 {M\over D_1}={N_1\over2h}.
 \tag{5.2}
\]

### Proposition 5.1 (Bernoulli rounding has linear excess)

Select every strip independently with probability \(p=1/D_1\). Then

\[
 \mathbb E L_1
 =2N_1(1-p)^{D_1}
 =(2e^{-1}+o(1))N_1.
 \tag{5.3}
\]

Consequently,

\[
 \mathbb E[\tau(\mathcal F)-\tau^*]
 \ge
 \left(1-{H\over2h}\right)\mathbb EL_1
 =\left({2\over e}+o(1)\right)W.
 \tag{5.4}
\]

#### Proof

Every signed depth-one target belongs to exactly \(D_1\) catalogue strips.
It is uncovered precisely when none is selected, giving
\((1-p)^{D_1}\). Here \(D_1\to\infty\), so this tends to \(e^{-1}\).
There are \(2N_1\) signed targets. Apply (3.5), use \(H/h=o(1)\) for the
last asymptotic, and note \(N_1/W\to1\). \(\square\)

### Proposition 5.2 (uniform fixed-cardinality rounding also fails)

Let

\[
 k=\left\lfloor{M\over D_1}\right\rceil
 \tag{5.5}
\]

and choose a uniformly random \(k\)-element subfamily. Then

\[
 \mathbb E L_1=(2e^{-1}+o(1))N_1
 \tag{5.6}
\]

and again the expected integrality excess is \(\Omega(W)\).

#### Proof

For a fixed signed depth-one target,

\[
 \Pr(T\text{ uncovered})
 ={\binom{M-D_1}{k}\over\binom Mk}
 =\prod_{i=0}^{k-1}
       \left(1-{D_1\over M-i}\right).
 \tag{5.7}
\]

Since \(k=(1+o(1))M/D_1\),

\[
 \log\Pr(T\text{ uncovered})
 =-{kD_1\over M}+o(1)=-1+o(1).
 \tag{5.8}
\]

Sum over the \(2N_1\) targets and use (3.5). \(\square\)

These propositions do not obstruct a highly correlated selection. They
show exactly why averaging, independent sampling, and fixed-cardinality
orbit sampling do not approach the required additive gap.

## 6. Relation to the Hall and SCD-flag theorems

The dependent mixed-frame Hall theorem chooses one frame per middle owner
and then finds target-to-owner matchings. Its columns are individual owner
states or literal faces. The SCD-Hoffman theorem chooses owner-rooted nested
paths. Neither theorem selects a family
\(\mathcal F\subseteq\mathscr C_{m,h}\) of whole \(2h\)-strips.

There is therefore no valid implication

\[
 \text{Hall quarantine or exact SCD flags}
 \Longrightarrow
 R_0+{H\over2h}R_1+
 \left(1-{H\over2h}\right)L_1+L_{\ge2}=o(W).
 \tag{6.1}
\]

Using such an implication would assume the cycle-bundling statement which
the strip reduction was designed to isolate.

Conversely, a strip family satisfying (4.3) directly compiles to the
coefficient-one word. It needs no exact middle ownership: uncovered middle
targets are repaired by singleton columns, while repeated middle incidences
are already charged by \(R_0\).

## 7. Proved statements and open conjecture

### Proved

1. The fractional optimum is exactly (0.2), with the whole-column dual
   certificate (0.3).
2. The integral gap is exactly the collision--hole minimum (0.6).
3. The four asymptotic conditions (4.3) are necessary and sufficient for
   an \(o(W)\) gap.
4. Independent and uniform fixed-cardinality orbit rounding have
   \(\Theta(W)\) expected gap.
5. The dependent Hall and SCD-flag results do not, without a new
   whole-strip theorem, imply any bound on (0.6).

### Open

> **Owner-recycling strip conjecture.** For
> \(H=\lceil\sqrt{m\log m}\rceil\) and dyadic
> \(h=m^{3/4+o(1)}\), there exists
> \(\mathcal F\subseteq\mathscr C_{m,h}\) satisfying (4.3).

Equivalently,

\[
 \tau_{m,H,h}-\tau^*_{m,H,h}=o(W).
 \tag{7.1}
\]

No exact obstruction to this conjecture is proved here. Any future positive
argument must create correlations strong enough to eliminate the
depth-one \(e^{-1}\) hole fraction while simultaneously keeping middle
repeat excess \(o(W)\) and the aggregate deeper holes \(o(W)\).
