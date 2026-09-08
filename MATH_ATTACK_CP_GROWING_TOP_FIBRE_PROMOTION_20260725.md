# Growing-band CP by top-fibre promotion paths

Date: 2026-07-25

Pure mathematics only.  This note audits the proposed scale
\(H\asymp\sqrt{m\log m}\), proves all scalar, flow, path, and fractional
claims, and isolates the one remaining integral design problem.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \lambda_q=\frac{W}{N_q}.                                                   \tag{0.1}
\]

The growing-band top-fibre proposal survives every count and local
bridge audit.  It is not ruled out by the fixed-pair Gaussian deficit,
because the top \(U\) and its cyclic coordinate order may depend on the
owner fibre.

There is a canonical exact choice of depth.  Let \(H\) be the largest
integer \(q<m\) for which

\[
 \lambda_q\le m+q.                                                         \tag{0.2}
\]

Then

\[
 \boxed{m-H<\lambda_H\le m+H},                                             \tag{0.3}
\]

and

\[
 \boxed{H=(1+o(1))\sqrt{m\log m}.}                                        \tag{0.4}
\]

Consequently

\[
 N_H=\frac W{\lambda_H}=\Theta(W/m)=o(W/H),                                \tag{0.5}
\]

and one useful-prefix initialization for every rank-\((m+H)\) top costs

\[
 \boxed{2HN_H=o(W).}                                                       \tag{0.6}
\]

The two Boolean tails beyond depth \(H\) contain only \(O(W/H)=o(W)\)
masks.

For any top \(U\in\binom{[2m]}{m+H}\), a cyclic order of \(U\) gives a
promotion-only bridge cycle of length \(m+H\).  Any consecutive segment of
length \(s\le m+H\) is one bridge-one path, with lower and upper flags equal
to cyclic intervals of lengths \(m-q\) and \(m+q\).  At upper depth \(H\),
all its states expose the common top \(U\).

Write

\[
 a=\lfloor\lambda_H\rfloor,qquad
 r=W-aN_H.                                                                \tag{0.7}
\]

Then \(0\le r<N_H\), and (0.3) ensures

\[
 m-H\le a\le a+1\le m+H                                                    \tag{0.8}
\]

whenever the length \(a+1\) is actually used.  Thus the scalar ledger is
exact: choose \(r\) tops with path length \(a+1\) and the other \(N_H-r\)
tops with path length \(a\).  Their owner counts sum to \(W\), and their
number of paths is exactly \(N_H\).

There is also an explicit symmetric fractional selection of these atoms
which has all of the following properties simultaneously:

* every top has weight exactly one;
* every middle owner has weight exactly one;
* every lower target through depth \(H\) is hit with weight \(W/N_q\);
* every upper target through depth \(H-1\) is hit with weight \(W/N_q\);
* every upper depth-\(H\) target is hit with weight exactly one; and
* total path weight is exactly \(N_H=o(W/H)\).

The exact integral version is not proved here.  It asks for one cyclic
promotion segment at every top so that their middle owners partition the
middle layer and their interval flags cover every other controlled target.
This is the top-fibre promotion design \((\mathrm{TFP}_H)\) in Section 7.
The corresponding LP is solved exactly by the orbit construction.  There
is no remaining divisibility or rank-capacity discrepancy; the remaining
issue is correlated integral rounding of the individual owner and flag
rows.

Thus the route is **not refuted**.  It reduces coefficient one to a cleaner
integral design than fixed-\(A\) CP: one path per top, with path lengths
already forced to two adjacent integers.

## 1. Exact selection of the growing depth

The consecutive load ratio is

\[
 \frac{\lambda_{q+1}}{\lambda_q}
 =\frac{N_q}{N_{q+1}}
 =\frac{m+q+1}{m-q}.                                                       \tag{1.1}
\]

The sequence \(\lambda_q\) is strictly increasing, \(\lambda_0=1\), and
\(\lambda_m=W\).  Hence the largest \(H\) satisfying (0.2) exists and is
strictly less than \(m\).

### Proposition 1.1 (exact load window)

The depth selected by (0.2) satisfies (0.3).

#### Proof

The upper bound is the definition of \(H\).  Maximality gives

\[
 \lambda_{H+1}>m+H+1.
\]

Using (1.1),

\[
 \lambda_H
 =\lambda_{H+1}\frac{m-H}{m+H+1}
 >m-H.
\]

This proves (0.3). \(\square\)

### Proposition 1.2 (asymptotic depth)

The same \(H\) satisfies (0.4).

#### Proof

For \(q=o(m^{2/3})\), (1.1) gives uniformly

\[
 \begin{split}
 \log\lambda_q
 &=\sum_{i=0}^{q-1}
   \log\frac{m+i+1}{m-i}\\
 &=\frac{q^2}{m}+O\!\left(\frac q m+\frac{q^3}{m^2}\right).                \tag{1.2}
 \end{split}
\]

For fixed \(\varepsilon>0\), put
\(q_\pm=(1\pm\varepsilon)\sqrt{m\log m}\).  Formula (1.2) gives

\[
 \lambda_{q_-}=m^{(1-\varepsilon)^2+o(1)}<m-q_-,
\]

and

\[
 \lambda_{q_+}=m^{(1+\varepsilon)^2+o(1)}>m+q_+.
\]

Thus \(q_-\le H<q_+\) for all sufficiently large \(m\).  Since
\(\varepsilon\) is arbitrary, (0.4) follows. \(\square\)

Combining Propositions 1.1 and 1.2 gives

\[
 \frac{H}{\lambda_H}\le\frac{H}{m-H}=o(1),                                \tag{1.3}
\]

which is exactly the reset estimate (0.6) after multiplication by \(2W\).

## 2. Exact tail audit

The rank sizes satisfy

\[
 \frac{N_{q+1}}{N_q}=\frac{m-q}{m+q+1}.                                   \tag{2.1}
\]

For every \(q\ge H\), this ratio is at most

\[
 \rho_H=\frac{m-H}{m+H+1}<1.
\]

Therefore

\[
 \sum_{q=H+1}^mN_q
 \le N_H\frac{\rho_H}{1-\rho_H}
 =N_H\frac{m-H}{2H+1}
 <\frac{W}{2H+1},                                                         \tag{2.2}
\]

where the last inequality uses \(\lambda_H>m-H\).  By complement symmetry,
the two tails together contain fewer than

\[
 \boxed{\frac{2W}{2H+1}=O(W/H)=o(W)}                                      \tag{2.3}
\]

masks.  Hence a \(W+o(W)\) literal construction of the central band through
this growing \(H\) still proves coefficient one after the tails are appended.

## 3. Exact promotion paths inside one top

Fix

\[
 U\in\binom{[n]}{m+H},\qquad M=|U|=m+H,                                   \tag{3.1}
\]

and a cyclic order

\[
 \pi=(u_0,u_1,\ldots,u_{M-1})
\]

of \(U\).  Indices below are read modulo \(M\).  Put

\[
 X_t=\{u_t,u_{t+1},\ldots,u_{t+m-1}\}.                                    \tag{3.2}
\]

Then

\[
 X_{t+1}=X_t-u_t+u_{t+m}=X_t-u_t+u_{t-H}.                                 \tag{3.3}
\]

Define the full flag at \(X_t\) by

\[
 \alpha(X_t)=(u_t,u_{t+1},\ldots,u_{t+H-1}),                               \tag{3.4}
\]

\[
 \beta(X_t)=(u_{t-1},u_{t-2},\ldots,u_{t-H}).                              \tag{3.5}
\]

The arriving coordinate in (3.3) is the last upper singleton
\(\beta_H(X_t)=u_{t-H}\).  The exact queue equations from
`MATH_ATTACK_CP_TWO_FLOW_QUEUE_COUPLING_20260725.md`, Theorem 1.1, give a
last-position promotion arc from \(X_t\) to \(X_{t+1}\).

### Proposition 3.1 (top-fibre promotion atom)

For every \(1\le s\le M\), the states at

\[
 X_0,X_1,\ldots,X_{s-1}                                                     \tag{3.6}
\]

form one bridge-one path of length \(s\).  Its flags satisfy, for
\(0\le q\le H\),

\[
 L_q(X_t)=\{u_{t+q},\ldots,u_{t+m-1}\},                                    \tag{3.7}
\]

\[
 U_q(X_t)=\{u_{t-q},\ldots,u_{t+m-1}\}.                                    \tag{3.8}
\]

Thus \(L_q(X_t)\) and \(U_q(X_t)\) are cyclic intervals of lengths
\(m-q\) and \(m+q\), respectively.  For fixed \(q\), the \(s\) lower
flags are distinct.  The \(s\) upper flags are distinct when \(q<H\),
while

\[
 U_H(X_t)=U                                                              \tag{3.9}
\]

for every \(t\).

#### Proof

The bridge statement follows from (3.3)--(3.5).  Deleting the first \(q\)
entries of (3.4) gives (3.7), while adjoining the first \(q\) entries of
(3.5) gives (3.8).  Proper cyclic intervals of a fixed length in a cyclic
order of distinct coordinates have distinct starting positions.  This
applies to every lower length \(m-q<M\), and to every upper length
\(m+q<M\) when \(q<H\).  At \(q=H\), the interval length is \(M\), proving
(3.9). \(\square\)

Call the path (3.6), together with these full flags, a **top-fibre
promotion atom** of length \(s\).

## 4. The scalar one-path-per-top ledger is exact

Let

\[
 a=\lfloor\lambda_H\rfloor,qquad r=W-aN_H.                                \tag{4.1}
\]

Since \(W=\lambda_HN_H\),

\[
 0\le r<N_H,qquad
 (N_H-r)a+r(a+1)=W.                                                        \tag{4.2}
\]

Proposition 1.1 gives \(a\ge m-H\).  If \(r>0\), then
\(a+1=\lceil\lambda_H\rceil\le m+H\); if \(r=0\), only length \(a\) is
used.  Hence every required length occurs among the legal atom lengths in
Proposition 3.1.

Choosing one atom at each top, with \(r\) atoms of length \(a+1\) and
\(N_H-r\) of length \(a\), would give exactly

\[
 p=N_H                                                                  \tag{4.3}
\]

paths and exactly \(W\) owner slots.  If the slots can be made into an
exact middle-owner partition with covering flags, the useful-prefix compiler
has central-band length

\[
 W+2HN_H.                                                                \tag{4.4}
\]

By (1.3),

\[
 \frac{2HN_H}{W}=\frac{2H}{\lambda_H}le\frac{2H}{m-H}=o(1).               \tag{4.5}
\]

Together with (2.3), this is a coefficient-one ledger.

This also identifies the exact scale at which promotion-only CP becomes
possible.  Since promotion preserves the top, any promotion-only path cover
must have at least \(N_H\) paths.  The reset condition is therefore

\[
 HN_H=o(W)quad\Longleftrightarrow\quad \frac{H}{\lambda_H}=o(1).           \tag{4.6}
\]

Fixed \(H=A\sqrt m\) has \(\lambda_H\to e^{A^2}\) and fails (4.6).  The
choice (0.2) has \(\lambda_H\asymp m\) and satisfies it with room to spare.

## 5. The unstructured top assignment is already integral

Before requiring a fibre to be a promotion path, one can partition the
middle owners among tops with the exact loads in (4.2).

### Proposition 5.1 (balanced integral top ownership)

There is a map

\[
 \Phi:\binom{[n]}m\longrightarrow\binom{[n]}{m+H},\qquad X\subset\Phi(X),   \tag{5.1}
\]

such that exactly \(r\) tops have \(a+1\) preimages and every other top has
\(a\) preimages.

#### Proof

Use the bipartite inclusion graph between middle owners and tops.  Send one
unit from a source to every middle owner, allow an owner to send its unit to
any containing top, and give each top-to-sink arc the integral capacity
interval \([a,a+1]\).  Demand total flow \(W\).

The symmetric fractional flow sends each owner's unit equally among its
containing tops.  By transitivity, every top receives
\(W/N_H=\lambda_H\in[a,a+1]\).  Thus the lower-bounded network is
fractionally feasible.  Integral capacities and total unimodularity of a
directed incidence matrix give an integral flow.  Every owner then chooses
one top, every top receives \(a\) or \(a+1\) owners, and (4.2) forces
exactly \(r\) of the latter. \(\square\)

The balanced full-flag theorem gives more: its upper integral flow chooses
such a top at every owner while covering every intermediate upper target,
and an independent lower flow covers every lower target.  Thus common
middle ownership, exact top loads, and zero flag holes are all feasible
before chronology is imposed.

What Proposition 5.1 does not show is that each fibre
\(\Phi^{-1}(U)\) is the owner set of one promotion atom.  A post-hoc
ordering is unjustified: an arbitrary fibre need not even induce a connected
subgraph of the Johnson graph on \(\binom U m\), whereas one path requires
all consecutive owners to be adjacent and its ordered flags to obey the
promotion queue recurrence.

## 6. Exact symmetric fractional top-fibre design

The path-shaped restriction also has an exact fractional solution.

Fix one canonical length-\(a\) promotion atom and, when \(r>0\), one
canonical length-\((a+1)\) atom.  Take every indexed coordinate relabeling
under \(S_n\); repeated labelled copies are retained.  Write \(G=n!\).
Give every length-\(a\) orbit column weight

\[
 w_a=\frac{N_H-r}{G},                                                       \tag{6.1}
\]

and every length-\((a+1)\) orbit column weight

\[
 w_{a+1}=\frac rG.                                                         \tag{6.2}
\]

If \(r=0\), the second orbit is omitted.

### Theorem 6.1 (fractional one-path-per-top resolution)

The weights (6.1)--(6.2) have the following exact marginals.

1. Every top \(U\in\binom{[n]}{m+H}\) has total atom weight one.
2. Every middle owner has total atom weight one.
3. For every \(1\le q\le H\), each lower rank-\((m-q)\) target has hit
   weight \(W/N_q\).
4. For every \(1\le q<H\), each upper rank-\((m+q)\) target has hit weight
   \(W/N_q\).
5. Every upper rank-\((m+H)\) target has hit weight one.
6. The total atom weight is \(N_H\).

#### Proof

Each orbit column has one top.  In an indexed coordinate orbit, a fixed top
occurs in exactly \(G/N_H\) columns.  Its total weight is therefore

\[
 \frac{G}{N_H}(w_a+w_{a+1})=1.                                             \tag{6.3}
\]

A length-\(s\) column has \(s\) distinct owners.  A fixed owner therefore
occurs in \(Gs/W\) indexed columns of that orbit.  Its total weight is

\[
 \frac G W\bigl(aw_a+(a+1)w_{a+1}\bigr)
 =\frac{a(N_H-r)+(a+1)r}{W}=1                                             \tag{6.4}
\]

by (4.2).

At a lower depth \(q\le H\), Proposition 3.1 gives \(s\) distinct targets
per length-\(s\) column.  Transitivity on the rank and the same calculation
as (6.4) give target weight \(W/N_q\).  The identical argument applies to
upper depth \(q<H\).  At upper depth \(H\), a column hits only its single
top, so (6.3) applies instead.  Finally

\[
 G(w_a+w_{a+1})=N_H,                                                       \tag{6.5}
\]

which proves the path-weight assertion. \(\square\)

Since \(W/N_q\ge1\), every target-cover inequality is fractionally
satisfied.  This orbit mixes the top, the owner assignment, and the cyclic
coordinate order simultaneously.  It is therefore not a construction in
one fixed pair frame.

## 7. The exact integral top-fibre promotion discrepancy

For a top \(U\), let \(\mathscr A_a(U)\) be all length-\(a\) promotion
atoms from Proposition 3.1, and define \(\mathscr A_{a+1}(U)\) similarly
when \(r>0\).  Put

\[
 \mathscr A=\bigcup_U
 \bigl(\mathscr A_a(U)\cup\mathscr A_{a+1}(U)\bigr).                       \tag{7.1}
\]

For \(P\in\mathscr A\), let \(\operatorname{top}(P)\) be its top,
\(M(P)\) its owner set, and \(\mathcal L_q(P),\mathcal U_q(P)\) its sets
of lower and upper flags.  The exact integral question is the feasibility
of

\[
 \sum_{P:\operatorname{top}(P)=U}z_P=1
 \qquad\left(U\in\binom{[n]}{m+H}\right),                                 \tag{7.2}
\]

\[
 \sum_{P:X\in M(P)}z_P=1
 \qquad\left(X\in\binom{[n]}m\right),                                     \tag{7.3}
\]

\[
 \sum_{P:T\in\mathcal L_q(P)}z_P\ge1
 \quad\left(T\in\binom{[n]}{m-q},\ 1\le q\le H\right),                 \tag{7.4}
\]

\[
 \sum_{P:T\in\mathcal U_q(P)}z_P\ge1
 \quad\left(T\in\binom{[n]}{m+q},\ 1\le q<H\right),                    \tag{7.5}
\]

\[
 z_P\in\{0,1\}.                                                          \tag{7.6}
\]

The upper depth-\(H\) rows are already exactly (7.2).  Summing (7.3) and
using (7.2) forces exactly \(r\) chosen atoms to have length \(a+1\), so no
extra length-quota equation is needed.

Call (7.2)--(7.6) the **top-fibre promotion design**
\((\mathrm{TFP}_H)\).

### Proposition 7.1 (exact implication)

If \((\mathrm{TFP}_H)\) is feasible for the depth selected in (0.2), then
the contiguous-OR coefficient is one.

#### Proof

Equations (7.2)--(7.3) give one bridge-one promotion path at each top and
partition the \(W\) middle owners.  Equations (7.4)--(7.5), together with
the upper depth-\(H\) top rows, make the selected full flags a covering
prefix transversal through depth \(H\).  The direct compiler therefore has
length \(W+2HN_H=W+o(W)\) by (4.5).  Appending the two tails costs \(o(W)\)
by (2.3). \(\square\)

### Proposition 7.2 (the LP is solved exactly)

The linear relaxation of \((\mathrm{TFP}_H)\), obtained by replacing
(7.6) with \(z_P\ge0\), is feasible.

#### Proof

Use the orbit weights in Theorem 6.1.  Assertions 1 and 2 give (7.2)--(7.3),
and assertions 3--5 give all target inequalities. \(\square\)

This identifies the precise remaining discrepancy.  It is not any of the
following:

* the reset count, which is (0.6);
* the outer tail, which is (2.3);
* top capacity or divisibility, settled by (4.2) and Proposition 5.1;
* marginal lower/upper flag integrality, settled by the two layered flows;
* local promotion compatibility, supplied by Proposition 3.1; or
* the fixed-pair type deficit, avoided by the full coordinate orbit.

It is the failure, not yet proved or disproved, of an integral point of the
path-atom polytope (7.2)--(7.6).  In concrete terms: choose one cyclic
order and one consecutive block of \(a\) or \(a+1\) middle windows in every
top, with no repeated middle window globally and with every lower and upper
interval target hit.

## 8. Final audit

The growing-band idea changes the earlier fixed-\(A\) verdict in an
essential way.  At fixed \(A\), promotion preservation of the top forces
\(\Theta_A(W)\) path starts and is fatal.  At the depth (0.2), the number of
tops is only \(\Theta(W/m)\), so one start per top is negligible.

The strongest proved statement is therefore:

\[
 \boxed{
 \begin{gathered}
 H\sim\sqrt{m\log m},\quad
 m-H< W/N_H\le m+H,\\
 \text{one legal promotion atom per top has an exact feasible fractional}\
 \text{owner-and-shadow resolution of total reset cost }o(W).
 \end{gathered}}                                                          \tag{8.1}
\]

The construction is not yet integral.  The next theorem should target
\((\mathrm{TFP}_H)\) directly, preferably by an absorption or recursive
exact-decomposition argument which preserves the shallow-rank interval
rows.  Generic independent rounding is inadequate: at shallow depth
\(q\), the target load \(W/N_q=1+O(q^2/m)\) is close to one, so zero holes
must be built into the rounding rather than inferred from large slack.
