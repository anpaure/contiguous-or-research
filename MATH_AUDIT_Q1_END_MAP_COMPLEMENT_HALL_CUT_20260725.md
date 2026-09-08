# Depth-one end maps and the exact complement Hall cut

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad T=\frac Wn,
 \qquad N_1=\binom{n}{m-1},
\]

and let \(F\) be an exact middle wreath factor with \(T\) wreath rows.
The depth-one endpoint map satisfies the exact identities

\[
 e_F(R)=2\mu_{F,1}(R),\qquad \sum_R e_F(R)=2W,
 \qquad H_1(F)=\#\{R:e_F(R)=0\}.
\]

For the floor-calibrated row quota

\[
 a_1=\left\lfloor\frac{N_1}{T}\right\rfloor,
 \qquad \delta_1=N_1-a_1T,
\]

the exact capacitated Hall defect is not a function of \(H_1(F)\) alone.
If \(g_F(B)\) denotes the number of supported depth-one targets all of
whose owning rows lie in \(B\subseteq F\), then

\[
 \boxed{
 D_1(F)=
 \max_{B\subseteq F}
 \bigl(H_1(F)-\delta_1+g_F(B)-a_1|B|\bigr)_+.}
 \tag{0.1}
\]

Consequently the often suggested condition

\[
 H_1(F)\le\delta_1
\]

only clears the full-family Hall cut.  It is sufficient if and only if

\[
 \boxed{
 g_F(B)\le a_1|B|+\delta_1-H_1(F)
 \quad\text{for every }B\subseteq F.}
 \tag{0.2}
\]

For \(m\ge5\),

\[
 a_1=n-4,
 \qquad
 \delta_1=\frac{6T}{m+2}=\Theta\!\left(\frac{W}{m^2}\right).
 \tag{0.3}
\]

The audited canonical MSW factor has

\[
 H_1(F_m^{\rm MSW})\ge(1/16-o(1))W,
\]

and hence \(H_1(F_m^{\rm MSW})/\delta_1\to\infty\).  Thus the canonical
factor fails before any proper-subfamily Hall cut is considered.

## 1. Exact endpoint map

For \(R\in\binom{[n]}{m-1}\), define

\[
 e_F(R)=\#\{x\notin R:
 x\text{ is an endpoint of }R\cup\{x\}
 \text{ in its unique owning wreath of }F\}.
 \tag{1.1}
\]

Here every middle \(m\)-set has a unique owning wreath because \(F\) is
an exact middle factor.  Let \(\mu_{F,1}(R)\) be the number of wreath rows
of \(F\) in which \(R\) is a cyclic interval of length \(m-1\).

### Proposition 1.1

For every \(R\),

\[
 \boxed{e_F(R)=2\mu_{F,1}(R).}
 \tag{1.2}
\]

Therefore

\[
 \boxed{
 \sum_R e_F(R)=2W,
 \qquad
 H_1(F)=\#\{R:e_F(R)=0\}.}
 \tag{1.3}
\]

#### Proof

If \(R\) is a length-\((m-1)\) interval in one cyclic row, adjoining the
predecessor or the successor of that interval gives exactly two middle
intervals in the same row.  The adjoined coordinate is an endpoint of the
corresponding middle interval.

Conversely, if \(x\) is an endpoint of the owning middle interval
\(R\cup\{x\}\), deleting \(x\) leaves a length-\((m-1)\) interval in that
row.  These two operations are inverse, and a fixed row cannot contain the
same proper cyclic interval at two starts.  Thus every row occurrence of
\(R\) contributes exactly two endpoint extensions, proving (1.2).

There are \(W\) middle owners and each has two endpoints, which gives the
sum in (1.3).  The zero-set identity is immediate from (1.2). \(\square\)

### Corollary 1.2 (duplicate endpoint ledger)

If \(h_1=H_1(F)\), then

\[
 \boxed{
 \#\{R:e_F(R)\ge4\}
 \le W-N_1+h_1
 =\frac{2W}{m+2}+h_1.}
 \tag{1.4}
\]

Indeed,

\[
 \sum_{\mu_{F,1}(R)>0}(\mu_{F,1}(R)-1)
 =W-(N_1-h_1),
\]

and each target with \(e_F(R)\ge4\), equivalently
\(\mu_{F,1}(R)\ge2\), contributes at least one.

## 2. The row-target graph and its exact Hall defect

Let \(G_1(F)\) be the bipartite graph with left class \(F\), right class
\(\binom{[n]}{m-1}\), and an edge \(\pi R\) when \(R\) is a
length-\((m-1)\) cyclic interval of \(\pi\).  Every left degree is \(n\).

Give each left row capacity \(a_1\) and each right target capacity one.
Let \(\nu_1(F)\) be the maximum number of incidences in such a
capacitated matching, and define the unmatched slot defect

\[
 D_1(F)=a_1T-\nu_1(F).
 \tag{2.1}
\]

Cloning every left row \(a_1\) times and applying the Hall-deficiency
theorem gives

\[
 \boxed{
 D_1(F)=\max_{A\subseteq F}
 \bigl(a_1|A|-|N_1(A)|\bigr)_+.}
 \tag{2.2}
\]

The resulting number of targets not certified by this capacitated
selection is exactly

\[
 N_1-\nu_1(F)=\delta_1+D_1(F).
 \tag{2.3}
\]

This partial-capacity formulation is weaker than requiring every retained
row to supply a full \(a_1\)-star.  It is the exact row-specific selection
problem relevant when partially supplied rows are allowed.

## 3. Complement-cut identity

Write

\[
 U_F=N_1(F)=\bigcup_{\pi\in F}N_1(\pi),
 \qquad |U_F|=N_1-H_1(F).
\]

For \(B\subseteq F\), define its exclusive-target set

\[
 X_F(B)=U_F\setminus N_1(F\setminus B)
\]

and put

\[
 g_F(B)=|X_F(B)|.
 \tag{3.1}
\]

Thus \(g_F(B)\) counts the supported targets every occurrence of which is
carried by a row of \(B\).  It is not merely the size of \(N_1(B)\): a
target also carried outside \(B\) is not exclusive.

### Theorem 3.1 (exact complement Hall cut)

Equation (0.1) holds.

#### Proof

In (2.2), write \(A=F\setminus B\).  By definition of \(g_F(B)\),

\[
 |N_1(A)|=|U_F|-g_F(B)=N_1-H_1(F)-g_F(B).
\]

Also

\[
 a_1|A|=a_1(T-|B|)=N_1-\delta_1-a_1|B|.
\]

Subtracting gives the exact identity

\[
 a_1|A|-|N_1(A)|
 =H_1(F)-\delta_1+g_F(B)-a_1|B|.
\]

Maximizing over \(B\subseteq F\) proves (0.1). \(\square\)

### Consequences

1. The cut \(B=\varnothing\), equivalently \(A=F\), has defect
   \(H_1(F)-\delta_1\).  Therefore \(H_1(F)\le\delta_1\) is necessary.
2. It is not sufficient without all the exclusive-target inequalities
   (0.2).
3. Since the rows of \(B\) contain only \(n|B|\) incidences,
   \(g_F(B)\le n|B|\).  Hence
   \[
   a_1|A|-|N_1(A)|
   \le H_1(F)-\delta_1+(n-a_1)|B|.
   \tag{3.2}
   \]
   For \(m\ge5\), this is
   \[
   a_1|A|-|N_1(A)|
   \le H_1(F)-\delta_1+4|B|.
   \tag{3.3}
   \]
   This can quarantine a violating cut to a sufficiently large complement,
   but it cannot eliminate proper-subfamily cuts.
4. More sharply, if \(H_1(F)\le\delta_1\), every violating complement
   \(B\) must satisfy
   \[
   g_F(B)-a_1|B|>\delta_1-H_1(F).
   \tag{3.4}
   \]

## 4. Exact depth-one arithmetic

Since

\[
 \frac{N_1}{T}=\frac{nm}{m+2}
 =2m-3+\frac6{m+2},
 \tag{4.1}
\]

for \(m\ge5\) one has

\[
 a_1=2m-3=n-4,
 \qquad
 \delta_1=\frac{6T}{m+2}.
 \tag{4.2}
\]

As \(T=W/n\),

\[
 \frac{\delta_1}{W}
 =\frac{6}{n(m+2)}=\Theta(m^{-2}).
 \tag{4.3}
\]

By contrast, the proved canonical MSW hole theorem gives

\[
 \frac{H_1(F_m^{\rm MSW})}{W}
 \ge\frac1{16}-o(1).
 \tag{4.4}
\]

Consequently

\[
 \boxed{
 \frac{H_1(F_m^{\rm MSW})}{\delta_1}=\Omega(m^2).}
 \tag{4.5}
\]

No priority, phase designation, or Hall argument inside the unchanged
canonical rows can repair targets absent from their support.  Positive
density exact-factor trades are necessary before the calibrated Hall
problem is even numerically feasible.

## 5. What an abstract pair block does and does not prove

At the level of an arbitrary left-\(n\)-regular incidence graph, a
two-row block \(B\) with many exclusive targets can violate (0.2) even
when \(H_1\le\delta_1\).  For example, when \(H_1=\delta_1\), any pair
with

\[
 g_F(B)>2a_1=2n-8
\]

creates a Hall defect.  This demonstrates exactly why the scalar hole
count is not a sufficient graph-theoretic invariant.

It does not automatically give a counterexample among exact wreath
factors.  A proposed pair block must pass three additional tests:

1. both neighborhoods must be actual length-\((m-1)\) interval families
   of cyclic orders;
2. their middle wreaths must be disjoint;
3. those two wreaths must extend to an exact middle factor.

In particular, taking two rows with identical depth-one neighborhoods is
not an extendible example: for \(2\le m-1\le n-2\), the full family of
cyclic intervals of that length determines the underlying cyclic order up
to dihedral symmetry, and hence determines the same middle wreath.  An
exact factor cannot contain both copies.

For completeness, in the present range \(r=m-1<(n/2)\) this rigidity is
elementary.  From the family of all cyclic \(r\)-intervals, count for each
pair \(x,y\) how many intervals contain both.  If their cyclic distance is
\(d\le r-1\), this count is \(r-d\); if \(d\ge r\), it is zero.  The
maximum value \(r-1\) therefore identifies exactly the adjacent pairs of
the underlying cycle.  Those adjacencies recover the cyclic order up to
rotation and reversal.

Thus an abstract pair-block obstruction refutes a black-box implication
from \(H_1\) to Hall feasibility, but it does not settle the wreath-specific
question.  A positive theorem may still exploit cyclic interval rigidity
to prove (0.2); that additional theorem is presently missing.

## 6. Exact remaining depth-one gate

For a variable exact factor, the calibrated depth-one row selection is
feasible with zero slot defect if and only if

\[
 \boxed{
 H_1(F)-\delta_1+g_F(B)-a_1|B|\le0
 \quad(B\subseteq F).}
 \tag{6.1}
\]

More generally, a row-specific coefficient-one ledger needs the sum of
the positive maxima in (0.1), together with the arithmetic floor defects,
to be \(o(W)\).  The missing mathematics is therefore not merely a
near-rainbow theorem \(H_1=o(W)\), but a hereditary exclusive-target
expansion theorem for one globally traded exact wreath factor.
