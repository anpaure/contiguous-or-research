# K16: exact token/Farkas lift to the separated port-permutation master

Date: 2026-07-30

Lane: H

Status: proved finite reduction. This note identifies the exact global
signed-circulation model containing the earlier token and peeling
potentials. It does not produce a completion of the remaining 93 targets,
a connected carrier, a compiler, or a length-12,873 word.

## 0. Verdict

The separated port-permutation master is the correct global assignment
model for source-relative, \(d=3\)-separated rethreadings of the full-C8
factor, meaning that distinct cuts have source distance greater than three
(the “four-separated” convention in the finite censuses). The
correspondence is exact in four senses.

1. The difference from the identity assignment is a balanced integral
   tail/head circulation.
2. Every lower/upper q1 token is an arc label of that circulation.
3. Every fixed lower/upper load through depth three is an exact signed arc
   sum, provided the selected cuts are three-separated.
4. A genuine Farkas certificate for the global master consists not only of
   target potentials, but also of free tail/head assignment prices and
   nonnegative prices for separation and physical-conflict rows.

The old peeling potential is therefore a valid arc-cost potential, but it is
not a global obstruction. It separates its frozen C3--C5 columns; the C8
orbit lies on its zero face, and post-C8 columns must be recomputed from the
post-C8 successor map.

## 1. Port assignment and its exact circulation

Let the source oriented two-factor have directed edges

\[
                         e_i=(u_i,v_i),\qquad i\in I.
\]

Both \((u_i)\) and \((v_i)\) enumerate the middle vertices once. Let \(E\)
be the allowed seam set, containing every diagonal \((i,i)\). A final port
assignment is a binary vector \(x\in\{0,1\}^{E}\) satisfying

\[
 \sum_{j:(i,j)\in E}x_{ij}=1,\qquad
 \sum_{i:(i,j)\in E}x_{ij}=1.                 \tag{1.1}
\]

Let

\[
 x^0_{ij}={\bf1}_{i=j},\qquad z=x-x^0,\qquad c_i=1-x_{ii}.
 \tag{1.2}
\]

### Theorem 1.1 (tail/head circulation normal form)

The residual \(z\) satisfies

\[
 \sum_jz_{ij}=0,\qquad \sum_iz_{ij}=0,\qquad
 z_{ii}=-c_i,\qquad z_{ij}=x_{ij}\ge0\quad(i\ne j). \tag{1.3}
\]

If every new seam \(T_i\to H_j\) is oriented from a tail node to a head node
and every deleted diagonal is oriented \(H_i\to T_i\), these arcs form a
balanced integral bipartite circulation. Its alternating circuits are
exactly the nontrivial cycles of the port permutation.

#### Proof

Subtract the identity assignment from the two families in (1.1). This gives
the first two equations. The remaining assertions follow from binary \(x\).
Alternating between a selected nonidentity seam and the deleted identity
matching follows the orbit of the head permutation, and every nontrivial
orbit gives one such alternating circuit. \(\square\)

This is an assignment circulation, not a circulation in the physical
Johnson graph. Physical Johnson legality, cut separation and the absence of
a physical carrier two-cycle remain separate constraints.

## 2. Exact occurrence columns through the collar depth

Fix \(1\le q\le d\). For a cut \(i\), let \(D_{i,q}\) be the
occurrence-multiplicity vector of old \(q\)-windows destroyed at that cut.
For a nonold allowed seam \(i\to j\), let \(A_{ij,q}\) be the
occurrence-multiplicity vector of new \(q\)-windows crossing that seam. Put

\[
 K^q_{ii}=0,\qquad K^q_{ij}=A_{ij,q}-D_{i,q}\quad(i\ne j). \tag{2.1}
\]

### Theorem 2.1 (master shadow identity)

If the selected cuts are \(d\)-separated, then for both signs and every
\(q\le d\),

\[
                       \boxed{\mu'_q=\mu_q+K^qx}. \tag{2.2}
\]

#### Proof

At a fixed tail \(i\), either \(x_{ii}=1\), in which case the contribution
in (2.1) is zero, or exactly one off-diagonal \(x_{ij}=1\), in which case
the old crossing occurrences \(D_{i,q}\) are removed and the new crossing
occurrences \(A_{ij,q}\) are added. Separation ensures that no \(q\)-window
contains two cuts, so these occurrence lists are disjoint across selected
tails. Summing gives (2.2). \(\square\)

Equivalently one may define a complete crossing-window column
\(W^q_{ij}=A_{ij,q}\), including \(W^q_{ii}=D_{i,q}\); then

\[
                         \mu'_q-\mu_q=W^q(x-x^0). \tag{2.3}
\]

The zero diagonal in (2.1), or equivalently the subtraction in (2.3), is
mandatory. Adding an \(A_{ii,q}\) term to the source load would already make
the identity permutation fail its own regression test.

For the current source, \(d=3\), so cuts have pairwise source distance
greater than three. Thus (2.2) is literal for q1, q2 and q3.
The 45 lower-q2 holes and the 48 fixed upper-q3 holes are exactly the 93
canonical residual rows; the latter list equals the 48 arbitrary-upper
rank-eleven holes. Filling all 93 while preserving all other q1--q3 rows
therefore completes this bounded-depth bank and rank-eleven arbitrary-upper
coverage. It does not protect deeper fixed shadows or arbitrary-upper
coverage at other ranks.

## 3. Q1 tokens are reduced seam costs

Let \(e^-_L\) and \(e^+_U\) denote lower and upper q1 basis vectors. For
\(i\ne j\), (2.1) specializes to

\[
 K^1_{ij}=
 e^-_{u_i\cap v_j}+e^+_{u_i\cup v_j}
 -e^-_{u_i\cap v_i}-e^+_{u_i\cup v_i}.        \tag{3.1}
\]

Let \(s=\mu_1-\mathbf1\) be the source q1 slack. Exact q1 completeness is

\[
                              K^1x\ge-s.       \tag{3.2}
\]

For any nonnegative q1 potential \(\lambda\), define the reduced seam cost

\[
 r_{ij}(\lambda)=\lambda^{\mathsf T}K^1_{ij}. \tag{3.3}
\]

Then

\[
 \boxed{\lambda^{\mathsf T}(\mu'_1-\mu_1)
       =\sum_{ij}r_{ij}(\lambda)x_{ij}.}       \tag{3.4}
\]

In particular, a new BB edge transports its old upper colour to its new
upper colour. On a tight colour bank this is the usual Eulerian token
condition. On the post-C8 source it is instead the capacitated inequality
(3.2): the orbit move has already created one unit of quotient slack on each
of the duplicated tight-shore q1 orbits represented by lower colour 15497
and upper colour 56980.

### Corollary 3.1 (exact cross-shore checksum)

Let \(A,B\) be the two middle shores. Assignment balance implies

\[
 t_{AB}:=\sum_{u_i\in A,v_j\in B}x_{ij}
 =\sum_{u_i\in B,v_j\in A}x_{ij}=:t.          \tag{3.5}
\]

The full-C8 source has \(t_0=15\), hence

\[
\begin{aligned}
 \mathbf1^{\mathsf T}K_{L_{\bar z}}x&=t-15,&
 \mathbf1^{\mathsf T}K_{L_z}x&=-(t-15),\\
 \mathbf1^{\mathsf T}K_{U_{\bar z}}x&=-(t-15),&
 \mathbf1^{\mathsf T}K_{U_z}x&=t-15.
\end{aligned}                                      \tag{3.6}
\]

#### Proof

Flow balance across the shore cut proves (3.5). A same-shore AA edge
contributes to \(L_{\bar z},U_{\bar z}\), a BB edge to \(L_z,U_z\), and
each cross edge to \(L_{\bar z},U_z\). Since the shore sizes are both 6435,
the four final occurrence masses are

\[
 6435+t,\quad6435-t,\quad6435-t,\quad6435+t.
\]

Subtracting their values at \(t_0=15\) gives (3.6). \(\square\)

These equations are implied by the assignment and literal q1 columns. They
are useful checksum rows, not extra hypotheses.

## 4. Exact scope of the peeling potential

Let \(\alpha\) be the two-round peeling potential and
\(\widetilde\alpha=\sum_{g\in C_{15}}g\alpha\) its orbit symmetrization.
Equation (3.4) turns both into physical seam costs.

For a port-permutation circuit \(P\) computed relative to a fixed source
successor map,

\[
                  \sum_{(i,j)\in P}r_{ij}(\lambda)
                  =\lambda^{\mathsf T}D_P.     \tag{4.1}
\]

Consequently the frozen pre-C8 C3--C5 columns have \(\alpha\)-score at most
\(-1\), the fifteen frozen C8 columns have score zero, and the symmetrized
scores are the already audited ones. But (4.1) is source-relative. In the
separated master based at the full-C8 factor, only an old circuit which
remains literally valid with the same local columns retains its old score.
Every new or overlapping post-C8 circuit must be rescored from the new
successor map.

Moreover \(\alpha\) does not satisfy a nonpositive reduced-cost inequality
on every allowed post-C8 seam. The global master may combine negative short
circuits with positive helper circuits. This is why the peeling theorem is
not a lane-wide no-go.

## 5. The complete master Farkas alternative

Let \(B x=\mathbf1\) contain all tail and head assignment equations. Put all
remaining structural linear rows into the normalized form

\[
                              Gx\ge g.          \tag{5.1}
\]

For example, cut separation is \(x_{ii}+x_{hh}\ge1\) for a forbidden pair
of cuts, while a physical reverse-edge conflict is
\(-x_{ij}-x_{\ell m}\ge-1\), where \(u_\ell=v_j\) and \(v_m=u_i\).
It is not generically the row \(x_{ij}+x_{ji}\le1\). Collar-unsafe and
non-Johnson seams are omitted from the allowed arc set.

Let

* \(Q\) be the relative q1 matrix, with source slack \(s\);
* \(H\) be the relative matrix on the selected source holes;
* \(C\) be the relative matrix on protected source-covered targets, with
  slack \(r\).

Consider the fractional complete-repair master

\[
\begin{aligned}
 Bx&=\mathbf1, & Qx&\ge-s, & Hx&\ge\mathbf1,\\
 Cx&\ge-r,     & Gx&\ge g, & x&\ge0.          \tag{5.2}
\end{aligned}
\]

### Theorem 5.1 (assignment-priced Farkas certificate)

System (5.2) is infeasible if and only if there exist free tail prices
\(p_i\), free head prices \(q_j\), and
\(\alpha,\beta,\gamma,\kappa\ge0\) such that every allowed seam satisfies

\[
 p_i+q_j+\alpha^{\mathsf T}Q_{ij}
 +\beta^{\mathsf T}H_{ij}
 +\gamma^{\mathsf T}C_{ij}
 +\kappa^{\mathsf T}G_{ij}\le0,               \tag{5.3}
\]

while

\[
 \sum_ip_i+\sum_jq_j-\alpha^{\mathsf T}s
 +\beta^{\mathsf T}\mathbf1-\gamma^{\mathsf T}r
 +\kappa^{\mathsf T}g>0.                      \tag{5.4}
\]

#### Proof

Multiply the assignment equalities by the free prices and the four lower
row families by their nonnegative multipliers. Condition (5.3) makes the
weighted left side nonpositive for every \(x\ge0\). Feasibility would make
the same quantity at least the strictly positive expression (5.4), a
contradiction. Conversely this is the standard Farkas alternative for
equalities, lower inequalities and nonnegative variables. \(\square\)

The tail/head prices have one gauge redundancy on each connected component
of the allowed tail--head incidence graph (in particular at least one),
because the corresponding assignment rows are redundant. Any extra
equality, such as a fixed cross count or voltage row, gets an additional
free dual multiplier.

Theorem 5.1 is the precise correction to applying the generator-only Farkas
theorem to the global master. The peeling \(\alpha\) supplies one
target-price block, but a master infeasibility proof must also price
assignment balance and every structural coupling row. Conversely, failure
to find such a fractional dual does not prove an integral port permutation:
the palette, separation and physical-conflict rows destroy the bare
Birkhoff/TU conclusion.

## 6. Exact capped-descent dual inside the master

Let \(\mathcal T\) be a finite bounded-depth target universe, let \(m\) be
its source load vector, let \(S\) be its exact relative matrix from (2.1),
and put

\[
                  B_0=|\{T\in\mathcal T:m_T\ge1\}|.
\]

Introduce \(0\le w\le\mathbf1\) and consider

\[
\begin{aligned}
 Bx&=\mathbf1,          & Qx&\ge-s,\\
 m+Sx&\ge w,            & \mathbf1^{\mathsf T}w&\ge B_0+1,\\
 Gx&\ge g,              & x,w&\ge0,\quad w\le\mathbf1.      \tag{6.1}
\end{aligned}
\]

For integral separated \(x\), this is exactly a strict reduction of the
number of holes in \(\mathcal T\). For fractional \(x\), it is a relaxation.

### Theorem 6.1 (assignment-priced strict-descent dual)

Assume the master without the last strict-descent row is feasible. System
(6.1) is infeasible if and only if there are free \(p_i,q_j\), nonnegative
\(\alpha,\eta,\theta,\kappa\), and \(\rho>0\) such that

\[
 p_i+q_j+\alpha^{\mathsf T}Q_{ij}
 +\eta^{\mathsf T}S_{ij}+\kappa^{\mathsf T}G_{ij}\le0
                                                        \tag{6.2}
\]

for every allowed seam,

\[
                         \eta+\theta\ge\rho\mathbf1,     \tag{6.3}
\]

and

\[
 \sum_ip_i+\sum_jq_j-\alpha^{\mathsf T}s
 -\eta^{\mathsf T}m-\theta^{\mathsf T}\mathbf1
 +\rho(B_0+1)+\kappa^{\mathsf T}g>0.                    \tag{6.4}
\]

#### Proof

Rewrite \(m+Sx\ge w\) as \(Sx-w\ge-m\) and
\(w\le\mathbf1\) as \(-w\ge-\mathbf1\). Give the q1, target, cap,
total-coverage and structural rows multipliers
\(\alpha,\eta,\theta,\rho,\kappa\), respectively. The \(x\)-column
condition is (6.2), the \(w\)-column condition is (6.3), and the weighted
right side is (6.4). Farkas gives the equivalence. If \(\rho=0\), the same
multipliers would separate the feasible master with the strict-descent row
removed; hence \(\rho>0\). \(\square\)

If \(\mathcal T\) is the full protected q2/q3 target universe, then its 93
source holes are the only zero entries of \(m\), and (6.1) is an exact net
fixed-depth descent model. Equivalently, one may retain only 93 capped
variables \(w\) while adding every source-covered q2/q3 row as a hard
constraint. On the 93 residual rows alone, without those protection rows,
filling one target is not a net descent because another fixed-depth target
could be lost. Even the correctly protected fixed-depth model becomes an
exact canonical descent only after final arbitrary-width and deeper-shadow
replay accepts the materialized chronology.

## 7. The unique-token service cut in master variables

The earlier lower-q2 token argument also survives globally, but it requires
witness-incidence variables rather than a naked arc inequality. Work with an
integral q1-complete master assignment relative to the current full-C8
source. The audited 45 lower-q2 holes all contain \(z\), so every witness for
one of them is a BBB three-state window. For every newly served hole, choose
one such witness and mark its unique nonold seam. Such a seam is unique
because the cuts have distance greater than three. Let

* \(g\) be the number of served holes;
* \(k\) be the number of distinct marked new BB seams;
* \(R\) be the number of upper colours used by those seams for which no
  source provider edge of that colour is retained in the final assignment;
* \(2t\) be the number of final cross edges.

Then

\[
                       \boxed{R+t\ge k\ge\lceil g/2\rceil}. \tag{7.1}
\]

The second inequality holds because one selected seam belongs to at most two
three-state windows. For an upper colour \(U\), let \(n_U\) count marked new
BB seams of colour \(U\), let \(r_U\in\{0,1\}\) record whether at least one
source provider of \(U\) is retained, and let \(m_U\) be the final load.
The marked seams are not source edges, so

\[
                   n_U+r_U\le m_U,
\]

and hence

\[
                   n_U\le(m_U-1)+(1-r_U).      \tag{7.2}
\]

Sum (7.2) over the used colours. The exact cross-shore identity gives
\(\sum_{U\in U_z}(m_U-1)=t\), while the number of used colours with
\(r_U=0\) is \(R\). Thus \(k\le t+R\), proving the first inequality.
This proof allows the 15 source colours of load two; no false unique-provider
hypothesis is used.

Standard binary witness variables can linearize
`served target -> chosen crossing window -> its unique new seam`, and
provider-retention variables can linearize \(R\). Thus (7.1) is a valid
lifted master cut. Without those witness and source-provider choices, \(k\)
and \(R\) are not linear functions of the raw seam set, so (7.1) must not be
asserted as an unlifted seam row.

## 8. Relation to bounded history and the exact remaining gate

The bounded-history model is more general than the present master: it may
choose transition options whose local histories are not inherited from one
fixed source factor. In the separated master, each port already fixes its
three incoming and outgoing source transitions. Cut distance greater than
three ensures that collars do not overlap, and the finite collar-safe arc
test checks the only new local history. Therefore the history variables
project away exactly inside this source-relative class.

What does not project away is long chronology. A window of depth greater
than three may cross several selected seams. Consequently:

* q1 and fixed q2/q3 use the exact matrices above;
* positive residence four follows from separated safe collars;
* physical simplicity needs the correctly indexed reverse-edge rows;
* connectivity, Hamiltonicity and voltage need separate constraints;
* deeper fixed shadows and arbitrary-width upper coverage require literal
  materialization and sound CEGAR.

Thus the smallest exact post-C8 finite gate is:

> find one binary, \(d=3\)-separated (cut distance \(>3\)), collar-safe
> physical port assignment
> satisfying both assignment families, both q1 decks, the protected q2/q3
> rows and a strict 93-bank descent; then accept it only if the materialized
> factor passes the complete accumulated-union/deeper-shadow audit.

The master globally admits cancellation among long, individually unsafe or
nongainful port circuits. This is precisely the capability absent from the
bounded single-cycle censuses. No existence theorem for that assignment is
proved here.

## 9. Audit boundary

The algebra above was independently audited in two ways: once from the
occurrence ledger and once by deriving the Farkas system directly from the
tail/head assignment equations. Both audits found the same three necessary
corrections to the source master note:

1. exclude the diagonal from the added-seam term, or use (2.1);
2. the collar comparison count is \(d(d+3)/2\), hence nine at \(d=3\);
3. ban the reverse physical seam, not a generic permutation transposition.

Those corrections have been applied to
`MATH_THEOREM_K16_SEPARATED_PORT_PERMUTATION_MASTER_20260730.md`.

No SAT, CP, LP solve, exhaustive enumeration, remote job or sustained local
process was run for this theorem.
