# Common-cap existence by guard pruning and robust Hall

Date: 2026-07-31  
Lane: R  
Status: unconditional abstract theorem; exact remaining all-\(k\) hypothesis

## 1. Problem and verdict

Ordinary target-to-cell Hall is not enough for a literal compiler: chosen
intervals overlap in physical positions, and their target labels are
simultaneous pointwise caps.  The exact lift has two layers.

1. Choose a middle-realizing guard word \(Q\), or equivalently a bank of
   candidate incidences protecting one physical trace for every
   nonemptiness, middle-row-bit, and assigned-lower-bit obligation.
2. Prove Hall after deleting the incidences not realized by \(Q\), or after
   the equivalent trace-guard pruning.

The theorem below makes this precise.  For a fixed guard word, the exact
additional hypothesis is a cut-by-cut inequality comparing marginal Hall
surplus with the neighborhood lost under guard pruning.  This inequality is
both necessary and sufficient, and existentially over guard words it is
equivalent to common-cap existence.  Interval length \(d\), middle span
\(d+1\), and permanent owner bits make guard verification local, but do not
imply the cut inequality; explicit counterexamples show that no such
automatic implication is valid.

## 2. Interval compiler system

Let \(P=\{0,\ldots,n-1\}\) be the physical positions and let \(K\) be the
coordinate set.  The middle obligations are labelled intervals

\[
 (T_i,I_i),\qquad I_i\subseteq P,qquad |I_i|\le D.
\]

Define the maximal envelope and the carrier sets

\[
 E_p=\bigcap_{i:p\in I_i}T_i,
 \qquad
 H_{i,b}=\{p\in I_i:b\in E_p\}.                         \tag{2.1}
\]

Assume

\[
 E_p\ne\varnothing,qquad
 \bigvee_{p\in I_i}E_p=T_i.                              \tag{2.2}
\]

Let \({\cal L}\) be the lower-target family and \({\cal C}\) a family of
distinct physical intervals of length at most \(d\).  A candidate edge is
\(e=(S,C)\in G\subseteq{\cal L}\times{\cal C}\).  It is assumed sound when
selected alone.  Two edges are **co-selectable** when they have different
target endpoints and different cell endpoints.

A lower-perfect matching is a matching saturating \({\cal L}\).  For such
a matching \(M\), its maximal common cap is

\[
 A_p(M)=E_p\cap\bigcap_{(S,C)\in M:p\in C}S.              \tag{2.3}
\]

The fixed-matching maximal-cap theorem says that \(M\) is a literal compiler
exactly when all \(A_p(M)\) are nonempty, every middle row has OR \(T_i\),
and every selected cell has its assigned OR.

## 3. Exact trace formulation

For an edge \(e=(S,C)\) and \(b\in S\), put

\[
 H_{e,b}=\{p\in C:b\in E_p\}.                            \tag{3.1}
\]

A **trace decoration** of a matching \(M\) consists of:

1. a coordinate \(a_p\in E_p\) for every position \(p\);
2. a position \(r(i,b)\in H_{i,b}\) for every \(b\in T_i\); and
3. a position \(g(e,b)\in H_{e,b}\) for every \(e=(S,C)\in M\) and
   \(b\in S\).

It is compatible when every selected edge \(f=(R,D)\in M\) preserves every
trace it covers:

\[
\begin{aligned}
 p\in D&\Longrightarrow a_p\in R,\tag{3.2}\\
 r(i,b)\in D&\Longrightarrow b\in R,\tag{3.3}\\
 g(e,b)\in D&\Longrightarrow b\in R.\tag{3.4}
\end{aligned}
\]

In (3.4), the owner edge \(e\) is included; it preserves \(b\) because
\(b\in S\).

### Theorem 3.1 (binary trace-lift equivalence)

A lower-perfect matching has a literal common cap if and only if it admits a
compatible trace decoration.

#### Proof

Given a compatible decoration, (3.2) puts \(a_p\) in \(A_p(M)\), so no
letter is empty.  Equation (3.3) leaves one copy of each required middle bit,
and (3.4) leaves one copy of each required bit on every assigned lower cell.
All maximal-cap letters are already contained in the relevant middle and
lower labels, so equality follows.

Conversely, if \(A(M)\) is a realization, choose
\(a_p\in A_p(M)\).  For every required middle or lower bit, choose a
position at which that bit occurs in \(A(M)\).  Membership in \(A_p(M)\)
means that every selected cap covering that position contains the chosen
bit, so (3.2)--(3.4) hold. \(\square\)

This theorem is exact, but the trace choices still depend on the matching.
The next theorem gives a static bank on which ordinary Hall suffices.

## 4. Guarded banks

Let \(H\subseteq G\).  A **complete guard system** on \(H\) chooses

1. \(a_p\in E_p\) for every \(p\in P\);
2. \(r(i,b)\in H_{i,b}\) for every middle requirement; and
3. \(g(e,b)\in H_{e,b}\) for every \(e=(S,C)\in H\), \(b\in S\),

and satisfies the following tests.

**Position and row tests.**  For every \(f=(R,D)\in H\),

\[
 p\in D\Longrightarrow a_p\in R,
 \qquad
 r(i,b)\in D\Longrightarrow b\in R.                     \tag{4.1}
\]

**Ordered cross-edge test.**  For every ordered pair of co-selectable edges
\(e=(S,C),f=(R,D)\in H\) and every \(b\in S\),

\[
 g(e,b)\in D\Longrightarrow b\in R.                     \tag{4.2}
\]

### Theorem 4.1 (guarded-Hall lift)

If \(H\) has a complete guard system and satisfies Hall's inequalities

\[
 |N_H(X)|\ge |X|\qquad(X\subseteq{\cal L}),              \tag{4.3}
\]

then every lower-perfect matching \(M\subseteq H\) is a literal common-cap
compiler.

#### Proof

Hall gives a matching \(M\) saturating \({\cal L}\).  Restrict the complete
guard system to the selected edges.  Equations (4.1)--(4.2) become exactly
(3.2)--(3.4), because any two distinct selected edges are co-selectable.
Theorem 3.1 finishes. \(\square\)

The word is constructive: after selecting \(M\), output the maximal cap
\(A(M)\) from (2.3).  No independent source-letter search or rounding is
needed.

### Cartesian specialization

Define

\[
 A_p(H)=E_p\cap\bigcap_{(S,C)\in H:p\in C}S.              \tag{4.4}
\]

If \(A(H)\) is nonempty and realizes every middle row and every edge of
\(H\), call \(H\) Cartesian.  Choosing all guards from \(A(H)\) proves that
every Cartesian bank has a complete guard system.  Hence a Cartesian bank
satisfying (4.3) is a sufficient certificate.  Conversely, every literal
compiler matching \(M\) is itself a Cartesian bank.  Therefore

\[
 \boxed{\text{common-cap existence}
 \iff \text{some Cartesian subgraph contains a lower-perfect matching}.}
\tag{4.5}
\]

The complete-guard condition can be weaker than demanding that all edges of
\(H\) be simultaneously realizable: (4.2) ignores pairs which no matching
can select together.

### Theorem 4.2 (exact guard-word cut lift)

A **guard word** is a sequence \(Q=(Q_p)_{p\in P}\) such that

\[
 \varnothing\ne Q_p\subseteq E_p,\qquad
 \bigvee_{p\in I_i}Q_p=T_i\quad\text{for every }i.        \tag{4.6}
\]

For such a word, retain exactly the candidate incidences which it already
realizes:

\[
 H_Q=\left\{(S,C)\in G:\bigvee_{p\in C}Q_p=S\right\}.     \tag{4.7}
\]

Put

\[
 \lambda_Q(X)=|N_G(X)\setminus N_{H_Q}(X)|,\qquad
 \sigma_G(X)=|N_G(X)|-|X|.                               \tag{4.8}
\]

Then:

1. \(H_Q\) is Cartesian;
2. \(H_Q\) contains a lower-perfect matching if and only if

   \[
   \lambda_Q(X)\le\sigma_G(X)\qquad(X\subseteq{\cal L}); \tag{4.9}
   \]

3. a literal common-cap compiler using \(G\) exists if and only if there is
   a guard word \(Q\) satisfying (4.9).

#### Proof

For every edge \((S,C)\in H_Q\) and every \(p\in C\), one has
\(Q_p\subseteq S\).  Hence \(Q_p\subseteq A_p(H_Q)\).  On a middle row,
\(Q\subseteq A(H_Q)\subseteq E\), so its OR is squeezed between \(T_i\)
and \(T_i\).  On an edge \((S,C)\), that edge itself gives
\(A_p(H_Q)\subseteq S\) for \(p\in C\), while (4.7) gives
\(\bigvee_{p\in C}Q_p=S\); again the OR of \(A(H_Q)\) is squeezed to \(S\).
Thus \(H_Q\) is Cartesian.

Since \(H_Q\subseteq G\),

\[
 |N_{H_Q}(X)|=|N_G(X)|-\lambda_Q(X),
\]

so Hall's inequalities for \(H_Q\) are exactly (4.9).

Finally, if a literal compiler \(Q\) uses a lower-perfect matching \(M\),
then every edge of \(M\) belongs to \(H_Q\), and (4.9) follows.  Conversely,
if (4.9) holds, Hall gives a lower-perfect matching in \(H_Q\); the guard
word \(Q\) itself realizes all its selected cells and every middle row.
\(\square\)

Thus (4.9), existentially over guard words, is an exact common-cap existence
theorem.  For a fixed \(Q\), its coefficient one is sharp.  The complete
guard-bank theorem remains useful when traces are easier to specify locally
than a whole word, but Theorem 4.2 is the logically strongest formulation.

### Corollary 4.3 (per-target deletion budget)

For a guard word \(Q\), put

\[
 B_Q(S)=N_G(S)\setminus N_{H_Q}(S),\qquad b_S=|B_Q(S)|.
\]

Since

\[
 \lambda_Q(X)\le
 \left|\bigcup_{S\in X}B_Q(S)\right|
 \le\sum_{S\in X}b_S,                                   \tag{4.10}
\]

it is sufficient that

\[
 |N_G(X)|\ge |X|+\sum_{S\in X}b_S
 \qquad(X\subseteq{\cal L}).                             \tag{4.11}
\]

In particular, if \(b_S\le b\) for every target, the expansion condition
\(|N_G(X)|\ge(b+1)|X|\) suffices.  The exact union loss in (4.9) can be much
smaller than the sum in (4.11).

## 5. Exact robust-Hall cut theorem

Fix the marginal graph \(G\) and a guarded bank \(H\subseteq G\).  For
\(X\subseteq{\cal L}\), define the marginal surplus and guard-pruning loss

\[
 \sigma_G(X)=|N_G(X)|-|X|,
 \qquad
 \lambda_H(X)=|N_G(X)\setminus N_H(X)|.                  \tag{5.1}
\]

### Theorem 5.1 (weakest cut condition for a fixed guarded bank)

The guarded bank \(H\) satisfies Hall if and only if

\[
 \lambda_H(X)\le \sigma_G(X)\qquad(X\subseteq{\cal L}).  \tag{5.2}
\]

Consequently, marginal Hall lifts to a common-cap matching whenever a
complete guard system can be installed on a bank \(H\) and (5.2) holds.

#### Proof

Because \(H\subseteq G\),

\[
 |N_H(X)|=|N_G(X)|-\lambda_H(X).
\]

Thus (5.2) is algebraically equivalent to
\(|N_H(X)|\ge|X|\) for every \(X\).  Apply Theorem 4.1. \(\square\)

In applications it is enough to prove explicit bounds

\[
 |N_G(X)|\ge |X|+\rho(X),
 \qquad
 \lambda_H(X)\le\rho(X)                                 \tag{5.3}
\]

for every target cut.  The function \(\rho\) may depend on the cut; a
uniform minimum-degree bound is neither required nor generally sufficient.
For a fixed guarded bank, (5.2) is sharp: if it fails on one set \(X\), that
set is a literal Hall obstruction in \(H\).

The condition is algorithmically checkable without a common-cap solver:
run one bipartite maximum matching (equivalently, one unit-capacity
max-flow/min-cut computation) in \(H\).  A deficient alternating shore is an
explicit set \(X\) violating (5.2); a saturating matching is, by Theorem 4.1,
already a literal compiler certificate after maximal-cap materialization.

This is the precise sense in which per-cut expansion can lift marginal Hall
to compatible Hall.  Expansion must be measured after, or against the loss
caused by, all three guard types.  Expansion in the unguarded graph alone
addresses the wrong quantifier.

### Corollary 5.2 (owner-bit robust Hall lift)

Assume there is a permanent owner bit \(a_p\in E_p\) at every position:

\[
 (S,C)\in G, p\in C\quad\Longrightarrow\quad a_p\in S.  \tag{5.4}
\]

Choose middle-bit and assigned-lower-bit guards, and let \(H\subseteq G\)
be any bank satisfying the row and ordered cross-edge tests.  If for every
\(X\subseteq{\cal L}\)

\[
 |N_G(X)|\ge |X|+\rho(X),
 \qquad
 |N_G(X)\setminus N_H(X)|\le\rho(X),                    \tag{5.5}
\]

then \(H\) contains a literal common-cap matching.

#### Proof

Condition (5.4) supplies the position part of a complete guard system with
no pruning.  The chosen row and edge guards supply the other two parts.
Equation (5.5) implies (5.2), so Theorems 5.1 and 4.1 apply. \(\square\)

This is the desired general matching theorem from owner bits and per-cut
expansion.  The function \(\rho\) is allowed to be asymmetric and
cut-dependent.  Replacing (5.5) by minimum degree, average expansion, or a
bound only on singleton target cuts is not justified.

## 6. What interval length supplies

Suppose lower cells have length at most \(d\) and middle rows have length at
most \(D=d+1\).  Then:

- each middle-bit trace has at most \(d+1\) possible positions;
- each assigned-lower-bit trace has at most \(d\) possible positions;
- an edge can threaten a chosen trace only if its interval contains that
  trace position; and
- every exact common-cap conflict has bounded rank and physical span:

\[
\begin{array}{c|c|c}
\text{conflict}&\text{rank}&\text{span}\\ \hline
\text{empty position}&\le\min\{|E_p|,d(d+1)/2\}&\le2d-1\\
\text{middle bit}&\le d+1&\le3d-1\\
\text{assigned lower bit}&\le d+1&\le3d-2.
\end{array}                                               \tag{6.1}
\]

These bounds make guard selection and failed-matching separation local.
They do not bound \(\lambda_H(X)\) for a large target cut: arbitrarily many
targets may rely on the same few trace positions.  A genuine construction
still has to establish (5.2) or (5.3).

## 7. Sharp counterexamples to automatic lifting

### 7.1 Complete-graph obstruction at every width

Fix \(d,r\ge1\).  Split \(P\) into \(r\) disjoint middle rows, each of
length \(d+1\), and give every row and every position the common label.

\[
 \Omega=\{o,a,x_1,\ldots,x_{dr}\}.                       \tag{7.1}
\]

Take \(dr+1\) lower targets

\[
 S_0=\{o\},\qquad S_j=\{o,x_j\}\quad(1\le j\le dr),
\]

take all \((d+1)r\) singleton physical cells, and let \(G\) be the complete
bipartite graph between the targets and those cells.

Every incidence is individually sound: after capping one singleton, its
row still has \(d\) untouched full-envelope positions, while the singleton
itself has exactly its assigned OR.  Coordinate \(o\) is a permanent owner
bit at every position.  Marginal Hall is maximally symmetric:

\[
 N_G(X)=P\quad\text{for every nonempty }X\subseteq{\cal L}. \tag{7.2}
\]

Nevertheless no lower-perfect matching is compatible.  Every selected
singleton label omits \(a\).  Preserving \(a\) on each row requires at least
one unselected position in that row, so at most \(dr\) cells can be used.
A lower-perfect matching would use \(dr+1\) cells and therefore completely
occupy some row, deleting \(a\) there.

The full target cut makes the failure of Theorem 4.2 exact.  Every
middle-realizing guard word has an \(a\)-bearing position in each row; none
of those \(r\) singleton cells lies in \(N_{H_Q}({\cal L})\).  Hence

\[
 \lambda_Q({\cal L})\ge r
 \quad\text{but}\quad
 \sigma_G({\cal L})=(d+1)r-(dr+1)=r-1.                  \tag{7.3}
\]

Moreover the worst marginal expansion ratio is

\[
 \frac{(d+1)r}{dr+1}\longrightarrow1+\frac1d.
\]

Thus, for every factor below \(1+1/d\), arbitrarily large complete interval
instances have that factor of label-blind marginal expansion and permanent
owners but no common cap.  The missing unit in (7.3) is precisely the
guard-pruned Hall obstruction.

### 7.2 Small owner-bit calibration

Take coordinates \(\{o,a,b,c\}\), positions \(P=\{0,1,2\}\), and one
middle row.

\[
 I=[0,2],\qquad T=E_0=E_1=E_2=\{o,a,b,c\}.
\]

There are two lower targets and exactly one candidate for each:

\[
 (\{o,b\},[0,1]),\qquad (\{o,c\},[2,2]).                \tag{7.4}
\]

Each candidate alone is legal: the untouched position supplies the complete
middle row, and the selected cell has its assigned OR.  The marginal graph
has a perfect matching.  Coordinate \(o\) is a permanent owner bit at every
position and belongs to every candidate covering that position.  Cells have
length at most \(d=2\), while the middle row has length \(d+1=3\).

Selecting both candidates leaves the middle-row OR
\(\{o,b,c\}\), losing \(a\).  Hence interval length, permanent nonempty
owners, and marginal Hall do not imply common-cap existence.

### 7.3 Position and middle guards do not protect assigned lower bits

Take positions \(P=\{0,1,2\}\), one row with constant envelope
\(\{o,a,b\}\), targets \(S_0=\{o,a\}\), \(S_1=\{o,b\}\), and cells
\(C_0=[1,1]\), \(C_1=[0,1]\).  Let \(G=K_{2,2}\), so all four
target-cell incidences are retained:

\[
 {\cal L}=\{S_0,S_1\},\qquad {\cal C}=\{C_0,C_1\}.       \tag{7.5}
\]

Every incidence is individually legal.  Coordinate \(o\) protects every
position, and every middle bit can be guarded at untouched position \(2\).
If a perfect matching assigns \(S_0\) to \(C_0\) and \(S_1\) to \(C_1\),
then the singleton \(C_0\) loses \(a\).  Under the crossed matching,
\(S_1\) is assigned to \(C_0\) and that singleton loses \(b\).  Thus every
marginal perfect matching preserves all position and middle guards but
fails an assigned-lower bit.  The edge-specific guards in (4.2) cannot be
omitted.

Together, the examples prove that the three guard families correspond to
three logically independent failure modes.

## 8. All-\(k\) implication and remaining lemma

Combine this note with the reroot--pin--cap theorem.  A chronology gives a
literal optimal word once it has:

1. exact middle ownership and consecutive-row witnesses for every upper
   target;
2. a chain-aligned optimal-length schedule with every required positional
   pin;
3. a sound complete lower candidate graph \(G\); and
4. a middle-realizing guard word \(Q\) satisfying (4.9), equivalently a
   Cartesian bank \(H_Q\) with a lower-perfect matching.  The stronger
   locally specified alternative is a complete guarded bank satisfying
   (5.2).

The first three properties are supplied in the successful K16 construction
by the genuine-four-filter derivative shores, two endpoint reroots, and one
singleton retiming.  The exact common-cap certificate supplies the fourth.

For a uniform PBBS/Pascal construction, the remaining existence theorem is
now the following checkable statement.

> **Guard-word robust-expansion gate.**  Construct a nonempty
> middle-realizing word \(Q\) such that, for every lower-target cut \(X\),
> the incidences not already realized by \(Q\) remove at most the original
> marginal surplus:
> \(\lambda_Q(X)\le\sigma_G(X)\).

This gate is sufficient and necessary by Theorem 4.2.  It has not been
proved for the general PBBS/Pascal chronology.  The interval bounds in
Section 6 reduce its local certificates to bounded rank and span, but do not
themselves prove its global cut inequalities.

## 9. Audited implication boundary

Proved unconditionally:

- exact trace-lift equivalence;
- guarded-Hall sufficiency;
- Cartesian/saturating-subgraph equivalence;
- exact guard-word characterization, existentially over \(Q\);
- exact robust-Hall loss-versus-surplus criterion;
- independence of the three guard types by explicit interval examples; and
- the all-\(d\) complete-graph obstruction with permanent owners and
  marginal expansion approaching \(1+1/d\).

Not proved:

- existence of a guard word, or a complete guarded bank, satisfying the cut
  inequalities for every derivative-level PBBS/Pascal chronology;
- any implication from marginal Hall plus interval length alone;
- total unimodularity or negative association for the common-cap system.

## 10. Independent audit

The report
MATH_AUDIT_R_COMMON_CAP_OWNER_EXPANSION_COUNTEREXAMPLE_20260731.md
independently verifies Theorems 3.1, 4.1, and 5.1, proves the complete
all-\(d\) obstruction in Section 7, and gives two further boundary results:

- for singleton opposing cells, the correct capacity condition is a
  partition-matroid rank inequality; and
- for genuine interval cells, the safe-family exchange axiom already fails
  at \(d=2,D=3\).

Thus no hidden matroid-Hall shortcut is being assumed in the guard-word
theorem.
