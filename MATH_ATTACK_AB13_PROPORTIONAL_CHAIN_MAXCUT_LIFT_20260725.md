# Lane AB13: proportional cover-chain contraction and the exact MaxCut lifting boundary

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computer experiment is used.

## 0. Outcome

The residual \(O(m^{-2})\) noncover overlap has the right numerical size for
the desired leave, but it does **not** lift the proportional Boolean bundles
to common physical rows. The failure occurs in three exact places.

1. A genuine vertical cover-chain resolution does not expose the
   \(O(m^{-2})\) tail. At the two central ranks it leaves a Pascal ladder with
   unrestricted normalized residual at least

   \[
   \left(2+o(1)\right)m^{-1}.
   \]

   More generally, if a contraction leaves \(r\) central ladder components,
   its exact residual in the original atom degrees is

   \[
   \boxed{
   \mathscr R(r)=
   \frac{(r-1)(2b-1)}{b^2(m+1)}.}                  \tag{0.1}
   \]

   Thus \(\mathscr R=o(m^{-1})\) forces \(r=o(b)\), and
   \(\mathscr R=O(m^{-2})\) forces \(r=1\) for all sufficiently large \(m\).
   The second-order scale is therefore incompatible with nontrivial
   cover-chain fragmentation.

2. Contracting every first-order cover pair is not a chain contraction. The
   central ladder becomes one component, every other slot attaches to it,
   and a global target-level contraction collapses both complete central
   ranks into one equivalence class. Selecting the resulting whole-row
   blocks is the original physical atom matching problem.

3. MaxCut has no native physical sign at the contracted-chain level. A
   cover-assignment bit is bookkeeping, while a whole-row on/off bit changes
   both endpoint loads in the same direction. Neither is the
   occurrence-transfer sign furnished by two equal-owner shores in AB12.
   Even if a literal two-shore cube is granted, the \(O(m^{-2})\) statistic
   controls repeated intersections, hence parallel-edge excess, but not the
   odd-cycle frustration of the simple constraint graph.

There is a positive conditional theorem. If the contracted skeletons admit
literal two-shore common-row realizations, every remaining conflict is a
binary parity constraint, and all nonforest constraints inject into the
noncover double intersections, and the selected conditioned system retains
the charge bound \(R=O(p\,m^{-3/4})\), then the conditional theorem gives
additional MaxCut leave

\[
 O(p\,m^{-3/4})=o(p/\sqrt m).                       \tag{0.2}
\]

None of those structural hypotheses follows from vertical Hall packing or
the unrestricted overlap estimate. An actual pair of target-disjoint
proportional atoms is constructed below for which every mixed column signing
is nonphysical. Thus the missing gate is a row-compatible conditional lift,
not another overlap estimate. No constant-one conclusion is claimed.

---

## 1. Parameters and the genuine second-order tail

Use the proportional Gaussian parameters

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 b=\lfloor m^{3/4}\rfloor,\qquad
 p=\left\lfloor\frac Wb\right\rfloor,              \tag{1.1}
\]

\[
 H=\lceil\alpha\sqrt{m\log m}\rceil,\qquad
 \frac1{\sqrt2}<\alpha<\frac{\sqrt3}{2},           \tag{1.2}
\]

and

\[
 N_q=\binom n{m+q},\qquad
 b_q=\left\lfloor\frac{N_q}{p}\right\rfloor
 \quad(-H\le q\le H+1).                            \tag{1.3}
\]

For all sufficiently large \(m\), division of \(W\) by \(b\) gives

\[
 b_0=b_1=b.                                         \tag{1.4}
\]

One proportional atom has

\[
 \kappa=\sum_{q=-H}^{H+1}b_q
 =\left(\sqrt\pi+o(1)\right)b\sqrt m.              \tag{1.5}
\]

Indeed the displayed band contains \(1-o(1)\) of all Boolean sets,
\(2^n/W=(\sqrt\pi+o(1))\sqrt m\), and the total floor error is
\(O(H)=o(b\sqrt m)\).

For two designated position intervals put

\[
 a=|P\setminus Q|,\qquad c=|Q\setminus P|.
\]

The audited conditional collision majorant, after removing the cover cases
\(a+c=1\), is

\[
 \mathscr S_{\ge2}(r)
 =\sum_{a+c\ge2}
 \frac{(a+c+1)^2}{\binom r a\binom{n-r}c},\qquad
 r=m+o(m).                                          \tag{1.6}
\]

### Lemma 1.1 (sharp leading noncover constant)

Uniformly through the proportional Gaussian band,

\[
 \boxed{
 \mathscr S_{\ge2}(r)=\frac{45+o(1)}{m^2}.}         \tag{1.7}
\]

#### Proof

The three terms with \(a+c=2\) are

\[
 \frac9{\binom r2},\qquad
 \frac9{r(n-r)},\qquad
 \frac9{\binom{n-r}2}.                              \tag{1.8}
\]

Since \(r,n-r=m+o(m)\), they contribute respectively
\(18/m^2,9/m^2,18/m^2\), up to \(o(m^{-2})\). For \(a+c\ge3\), the
binomial-series estimate used in the proportional-atom overlap theorem is
dominated by its first terms and is \(O(m^{-3})\), uniformly because
\(a,c\le b+2H=o(m)\). Summing proves (1.7). \(\square\)

The constant in (1.7) will be used only to audit scale. The obstruction
below persists even if the noncover tail is set equal to zero.

---

## 2. The central contraction--fragmentation theorem

For one atom, write its central position intervals as

\[
 P_i=[i,i+m-1],\qquad U_i=[i,i+m],\qquad 0\le i<b.   \tag{2.1}
\]

Their cover graph is the alternating path

\[
 L_b:\quad
 P_0-U_0-P_1-U_1-\cdots-P_{b-1}-U_{b-1},           \tag{2.2}
\]

because

\[
 P_i\subset U_i,\qquad P_{i+1}\subset U_i
 \quad(0\le i<b-1).                                 \tag{2.3}
\]

For every actual central cover pair \(A\subset B\), the labelled and simple
proportional-atom hypergraphs have the exact intrinsic ratio

\[
 \boxed{
 \lambda_m:=\frac{\deg(A,B)}{\deg(A)}
 =\frac{2b-1}{b(m+1)}.}                             \tag{2.4}
\]

There are \(b\) same-start and \(b-1\) adjacent-start slot representations;
conditioned on a fixed lower slot, each prescribed extension has probability
\(1/(m+1)\). This proves (2.4).

Let \(C\subseteq E(L_b)\) be any set of cover pairs declared contracted.
We grant the contraction its strongest possible effect: the entire intrinsic
codegree of every pair in \(C\) is removed, while the original unrestricted
degrees are retained for the other pairs. Let \(r(C)\) be the number of
components of the forest \((V(L_b),C)\), and define the lower-central
row-averaged residual

\[
 \mathscr R_C
 =\frac1b\sum_{i=0}^{b-1}
   \sum_{\substack{U:\ P_iU\in E(L_b)\setminus C}}
   \frac{\deg(P_i,U)}{\deg(P_i)}.                   \tag{2.5}
\]

### Theorem 2.1 (exact contraction--fragmentation tradeoff)

For every \(C\subseteq E(L_b)\),

\[
 \boxed{
 \mathscr R_C
 =\frac{(r(C)-1)(2b-1)}{b^2(m+1)}.}                 \tag{2.6}
\]

Consequently:

1. if \(C\) comes from any genuine partition into Boolean chains, then

   \[
   r(C)\ge b,\qquad
   \mathscr R_C\ge
   \frac{(b-1)(2b-1)}{b^2(m+1)}
   =\frac{2+o(1)}m;                                 \tag{2.7}
   \]

2. \(\mathscr R_C=o(m^{-1})\) implies \(r(C)=o(b)\);
3. for every fixed \(K\), \(\mathscr R_C\le K/m^2\) implies \(r(C)=1\)
   for all sufficiently large \(m\).

#### Proof

The graph \(L_b\) is a path on \(2b\) vertices. Hence

\[
 |C|=2b-r(C),\qquad
 |E(L_b)\setminus C|=r(C)-1.                       \tag{2.8}
\]

Every uncontracted edge contributes the same value \(\lambda_m\) to the
double sum in (2.5), exactly once. This proves (2.6).

A Boolean chain contains at most one cover edge between ranks \(m\) and
\(m+1\); globally those edges form a matching. Its intersection with
\(L_b\) has size at most \(b\), so \(r(C)=2b-|C|\ge b\), proving (2.7).

Multiplying (2.6) by \(m\), and using \(b\to\infty\), gives

\[
 m\mathscr R_C=(2+o(1))\frac{r(C)-1}{b},            \tag{2.9}
\]

which proves the second assertion. Finally,

\[
 r(C)-1
 \le
 \frac{K b^2(m+1)}{m^2(2b-1)}
 =O\left(\frac bm\right)=o(1).                     \tag{2.10}
\]

Since \(r(C)-1\) is a nonnegative integer, it is zero eventually.
\(\square\)

Theorem 2.1 is deliberately favorable to the proposed shortcut. It proves
that one cannot contract a nontrivial family of cover chains and then reuse
the **unconditioned** \(O(m^{-2})\) degree statistic. It is not a lower bound
after restricting to a specially chosen row-compatible chain pool: such
conditioning can change both degrees and codegrees, and may make the
conditioned degree zero. Controlling those conditioned fibers is a separate
unproved theorem.

### Corollary 2.2 (the global seam scale)

Let \(s=p-t\), where \(t=o(p/\sqrt m)\). Every genuine central chain
resolution leaves at least

\[
 s(b-1)=W-o(W)                                      \tag{2.11}
\]

uncontracted central cover seams across the \(s\) prospective rows.

#### Proof

Write \(W=pb+\rho_0\), \(0\le\rho_0<b\). Then

\[
 (p-t)(b-1)=W-\rho_0-p-tb+t.                       \tag{2.12}
\]

Here \(\rho_0=o(W)\), \(p/W\sim1/b=o(1)\), and
\(tb=o(W/\sqrt m)=o(W)\). \(\square\)

Thus reaching the noncover tail requires a genuinely nonlocal operation on
\((1-o(1))W\) cover seams.

### Proposition 2.3 (full cover contraction is global collapse)

If all edges of \(L_b\) are contracted, its \(2b\) central slots form one
component. If, in addition, every designated \(a+c=1\) attachment edge is
contracted, then every noncentral slot attaches to its central slot and the
whole atom is one component.

At target level the collapse is stronger. Every Boolean cover

\[
 A\subset B,\qquad |A|=m,\quad |B|=m+1,             \tag{2.13}
\]

occurs in some proportional atom. The bipartite inclusion graph between the
two complete central ranks is connected. Hence the equivalence relation
generated by contracting every first-order pair has one class containing
both ranks, of total size \(2W\).

#### Proof

The first assertion follows from the path (2.2) and the vertical same-start
chains. For (2.13), place \(A\) in \(P_0\), place the unique point of
\(B\setminus A\) at the added endpoint of \(U_0\), and complete the word
injectively; \(b+H<m\) leaves enough coordinates.

Any Johnson exchange \(A\mapsto A-a+x\) between \(m\)-sets is the two-edge
walk

\[
 A\subset A\cup\{x\}\supset A-a+x.                 \tag{2.14}
\]

The Johnson graph is connected, and every \((m+1)\)-set has a lower
neighbor. Thus the full inclusion graph is connected. \(\square\)

A full contraction can therefore be either global, in which case it has one
capacity class, or occurrence-dependent, in which case target capacities do
not descend to a well-defined quotient hypergraph. Neither case supplies a
nontrivial common-row matching theorem.

---

## 3. Exact legality criterion for a MaxCut lift

Let \(\mathcal V\) be a fixed set of contracted target capacities. For a
collection \(F\) of physical common-row bundles, write
\(\chi(F)\in\mathbb Z_{\ge0}^{\mathcal V}\) for its capacity-incidence
vector.

### Lemma 3.1 (equal-shore necessity)

Suppose binary blocks \(j=1,\ldots,J\) have two shores
\(L_j,R_j\), each a collection of literal physical rows, and every one of
the \(2^J\) independent shore choices has the same capacity-incidence vector.
Then, for every \(j\),

\[
 \boxed{\chi(L_j)=\chi(R_j).}                       \tag{3.1}
\]

Conversely, (3.1) for every block is sufficient for invariance of the total
capacity vector.

#### Proof

Compare two corners differing only in block \(j\). Their incidence-vector
difference is \(\chi(L_j)-\chi(R_j)\), so invariance forces (3.1). Summing
the equalities proves the converse. \(\square\)

This is the contracted-row analogue of common middle-root ownership in an
exact wreath component. Lemma 3.1 is not a necessity for every conceivable
dependent matching algorithm; it is the necessity for importing AB12's
independent invariant-owner component cube. Vertical contraction does not
supply it.

* A cover-assignment bit chooses which Boolean successor is recorded in one
  chain. It changes bookkeeping, not a target occurrence between two shores.
* A whole-row on/off variable contributes \(+1\) at both members of every
  target pair contained in that row. It is not a \((+1,-1)\) transfer.
* A one-row shore against the empty shore violates (3.1). If
  \(\mathcal V\) retains the actual target capacities, two singleton shores
  satisfying (3.1) are the same simple atom and give no nontrivial move;
  parallel word labels do not create a new matching choice. After a coarser
  contraction, distinct physical rows may have the same vector
  \(\chi\), but that equality alone does not make their uncontracted targets
  compatible or their tail swap physical.

Nontrivial MaxCut machinery therefore requires literal physical trades,
possibly with one row or several rows per shore, whose projected contracted
capacity vectors agree. Neither the Boolean SCD packing nor the noncover
overlap theorem constructs one such trade.

There is a second exact loss when one first fixes a vertical chain pool.

### Lemma 3.2 (conditioned physical-row fiber)

Fix a start \(i\), condition on the central target

\[
 A_{i,0}=\{x_i,\ldots,x_{i+m-1}\}=v,               \tag{3.2}
\]

and prescribe a saturated symmetric segment

\[
 C_{-d}\subset\cdots\subset C_0=v
 \subset\cdots\subset C_{d+1}.                     \tag{3.3}
\]

Then the exact fraction of labelled physical rows through the fixed central
slot which realize (3.3) as their same-start flag is

\[
 \boxed{
 \theta_d=\frac1{(m)_d(m+1)_{d+1}},}               \tag{3.4}
\]

where \((z)_j=z(z-1)\cdots(z-j+1)\).

#### Proof

Conditional on (3.2), the ordering of the \(m\) elements of \(v\) in the
central slot is uniform. The lower chain fixes the ordered letters

\[
 x_{i+m-r}=C_{-(r-1)}\setminus C_{-r}
 \quad(1\le r\le d),                                \tag{3.5}
\]

and hence has probability \(1/(m)_d\). Independently, the ordered complement
letters following the central slot are uniform. The upper chain fixes

\[
 x_{i+m+r-1}=C_r\setminus C_{r-1}
 \quad(1\le r\le d+1),                              \tag{3.6}
\]

and hence has probability \(1/(m+1)_{d+1}\). Multiply the two probabilities.
\(\square\)

At \(d=0\), prescribing only one upper cover already retains exactly a
\(1/(m+1)\) fraction. Let \(Z\ge0\) count noncover double intersections
against a fixed test atom. From the unrestricted estimate

\[
 \mathbb E[Z\mid A_{i,0}=v]\le\frac{C+o(1)}{m^2}   \tag{3.7}
\]

one may infer only

\[
 \mathbb E[Z\mid (3.3),A_{i,0}=v]
 \le\frac{C+o(1)}{m^2\theta_d}.                    \tag{3.8}
\]

Already \(d=0\) weakens the guaranteed bound to \(O(m^{-1})\); for larger
\(d\), (3.8) rapidly becomes vacuous. This is a loss-of-guarantee statement,
not a claim that the conditional overlap actually grows. It identifies the
missing quantifier: one needs a row-compatible chain pool with nonvanishing,
near-regular conditioned row fibers and a new conditional overlap bound.

---

## 4. A literal failure of post-hoc column signing

Vertical contraction cannot universally induce a mixed physical column cube.

### Theorem 4.1 (target-disjoint shores with no mixed common row)

For all sufficiently large \(m\), there exist two target-disjoint physical
proportional atoms \(e(x),e(y)\) such that

\[
 P_j(y)\not\subset U_i(x),\qquad
 P_j(x)\not\subset U_i(y)
 \quad(0\le i,j<b).                                 \tag{4.1}
\]

Any physical tight row assembled from complete vertical columns of \(e(x)\)
and \(e(y)\), even with the columns reordered, uses columns from only one of
the two atoms.

#### Proof

Fix \(x\) and choose a uniformly random injective word \(y\) of the same
template. A prescribed central lower target of \(y\) is a uniform \(m\)-set.
For a fixed \((m+1)\)-target \(U_i(x)\),

\[
 \Pr(P_j(y)\subset U_i(x))=\frac{m+1}{W}.           \tag{4.2}
\]

The same holds with \(x,y\) reversed by coordinate transitivity. A union
bound over all ordered cross pairs gives

\[
 \Pr(\text{some cross containment})
 \le\frac{2b^2(m+1)}W=o(1).                         \tag{4.3}
\]

At rank \(m+q\), a union bound for a common target gives

\[
 \Pr(e(x)\cap e(y)\ne\varnothing)
 \le\sum_{q=-H}^{H+1}\frac{b_q^2}{N_q}=o(1),       \tag{4.4}
\]

because every \(N_q\) is exponential while \(H,b_q\) are polynomial.
Thus a word \(y\) satisfying target disjointness and (4.1) exists.

In a physical tight row, the central lower target of every next column is
contained in the central upper target of the preceding column. A row using
both shores has an adjacent shore-change in its column order, contradicting
one of the containments forbidden by (4.1). \(\square\)

The formal \(2^b\) column-choice cube for these two rows therefore has only
two physical corners. In particular, if one places a formal cut constraint
on each adjacency of the contracted column path, its abstract MaxCut is
\(b-1\), while the physical mixed-shore cut space is empty. This statement
does not rule out globally choosing some other favorable family of rows; it
does rule out a universal post-hoc columnwise two-shore lift from collision
sparsity.

Boolean-chain equality is also weaker than equality of the ordered FIFO
state of a tight row. A tail exchange requires the full ordered queue state
or a literal connector, neither of which is supplied by chain contraction.

---

## 5. What the \(O(m^{-2})\) tail actually buys

Let \(F_1,\ldots,F_s\) be independent unrestricted labelled atoms. Let
\(X_s\) count, over unordered atom pairs, unordered pairs of common targets
whose slot difference has \(a+c\ge2\). The intrinsic calculation behind
Lemma 1.1 gives

\[
 \boxed{
 \mathbb E X_s
 \le\left(\frac{45}{4}+o(1)\right)
 \frac{s(s-1)\kappa}{p m^2}.}                      \tag{5.1}
\]

#### Proof

For a fixed test atom \(e\) and one random atom \(F\), a target \(v\in e\)
lies in \(F\) with probability \((1+o(1))/p\). Conditional on that event,
the ordered noncover collision row sum is at most
\((45+o(1))/m^2\). Sum over the \(\kappa\) choices of \(v\), divide by two
for unordered target pairs, and then sum over the \(\binom s2\) atom pairs.
\(\square\)

At \(s=p\), equations (1.5) and (5.1) give

\[
 \boxed{
 \mathbb E X_p
 \le\left(\frac{45\sqrt\pi}{4}+o(1)\right)
 p m^{-3/4}
 =o(p/\sqrt m).}                                    \tag{5.2}
\]

This is the favorable scale requested in the question. It controls only a
second intersection between the same two prospective rows. The first
intersection ledger is much larger:

\[
 \mathbb E\sum_{i<j}|F_i\cap F_j|
 =\binom s2\sum_q\frac{b_q^2}{N_q}.                 \tag{5.3}
\]

For \(s=p\), the floors are uniformly negligible because
\(\min_qb_q\to\infty\), and hence

\[
 \boxed{
 \mathbb E\sum_{i<j}|F_i\cap F_j|
 =\left(1+o(1)\right)\frac{p\kappa}{2}
 =\Theta(p m^{5/4}).}                               \tag{5.4}
\]

Thus (5.2) controls repeated edges in a prospective row-conflict graph, not
its singleton edges.

This distinction has an exact MaxCut form. Let \(\Gamma\) be a loopless
constraint multigraph, let \(\bar\Gamma\) be its underlying simple graph, and
let \(\mu_{uv}\) be its edge multiplicities. Put

\[
 X(\Gamma)=\sum_{uv\in E(\bar\Gamma)}\binom{\mu_{uv}}2. \tag{5.5}
\]

### Lemma 5.1 (parallel excess versus simple frustration)

With

\[
 \operatorname{fr}(G)=|E(G)|-\operatorname{MaxCut}(G),
\]

one has

\[
 \boxed{
 \operatorname{fr}(\bar\Gamma)
 \le\operatorname{fr}(\Gamma)
 \le\operatorname{fr}(\bar\Gamma)+X(\Gamma).}      \tag{5.6}
\]

Every loop adds one unavoidable unit to both sides after its multiplicity is
added separately.

#### Proof

Every monochromatic simple edge contributes at least one monochromatic edge
in \(\Gamma\), proving the lower bound. Color \(\bar\Gamma\) optimally. Its
monochromatic edges contribute their first copies to
\(\operatorname{fr}(\bar\Gamma)\); all further copies contribute at most

\[
 \sum_{uv}(\mu_{uv}-1)_+
 \le\sum_{uv}\binom{\mu_{uv}}2=X(\Gamma).
\]

This proves the upper bound. \(\square\)

The noncover double-intersection estimate can therefore bound at most the
second term in (5.6). It gives no bound on
\(\operatorname{fr}(\bar\Gamma)\).

### Proposition 5.2 (zero double overlap with linear bundle leave)

There are abstract common-row constraint systems on
\(3\lfloor p/3\rfloor\) bundle vertices for which:

* the simple constraint graph is a union of disjoint triangles;
* every triangle edge is one inequality constraint and the logical
  multigraph is simple, so \(X(\Gamma)=0\);
* at every fixed sign corner, two component rows share at most one actual
  target, so the double-intersection statistic is zero;
* every deletion leaving a bipartite constraint graph loses at least
  \(\lfloor p/3\rfloor\) bundles.

#### Proof

For each triangle edge \(e=uv\), introduce two distinct actual targets
\(a_e,b_e\), regarded as two realizations of one contracted capacity. Put
\(a_e\) in the positive shores of both \(u,v\), and put \(b_e\) in their
negative shores. Opposite shores then have no common target on \(e\), while
equal shores have exactly one. Thus \(e\) is one inequality constraint, the
two projected shores have the same contracted incidence, and any fixed pair
of chosen rows shares at most one target. The repeated-pair statistic is
therefore zero, stronger than any \(O(m^{-2})\) bound on that statistic.

An odd triangle cannot satisfy all three inequality constraints. Deleting
one vertex is necessary and sufficient to leave a satisfiable induced graph.
The triangles are disjoint, so the costs add. \(\square\)

This is an abstract logical countermodel, not a Boolean-lattice embedding.
It proves that even zero repeated overlap does not imply the desired
\(o(p/\sqrt m)\) MaxCut frustration. Loads at least three create additional
multiway constraints and lie outside the clean target-disjoint pair theorem.

---

## 6. A conditional common-row MaxCut lifting theorem

The exact additional hypotheses under which (5.2) would become useful can be
stated cleanly.

### Theorem 6.1 (conditional parity-forest lift)

Let \(s=p-t_0\) contracted row skeletons be given. Assume:

1. each skeleton \(i\) has two literal physical common-row realizations
   \(R_i^+,R_i^-\);
2. every choice of one realization per skeleton preserves the contracted
   capacity vector;
3. every remaining target conflict is a binary parity constraint on the two
   signs of the incident skeletons, and satisfying all constraints gives
   pairwise target-disjoint rows;
4. the parity multigraph has a spanning forest \(T\) such that every loop and
   every edge outside \(T\) is injectively charged to a noncover double
   intersection, with total charge \(R\).

Then there are at least

\[
 s-R=p-(t_0+R)                                      \tag{6.1}
\]

pairwise target-disjoint literal common rows. In particular,

\[
 t_0+R=o(p/\sqrt m)                                 \tag{6.2}
\]

proves the desired proportional-atom lift.

#### Proof

Every signed parity system on a forest is consistent: choose one root sign
per component and propagate. Fix signs satisfying all constraints in \(T\).
At most \(R\) remaining constraints fail. Delete one incident row for every
failed constraint. After these deletions every surviving constraint is
satisfied, so hypothesis 3 makes the surviving physical rows pairwise
target-disjoint. At most \(R\) rows were deleted. \(\square\)

If \(t_0=o(p/\sqrt m)\) and, in addition, the selected conditioned skeleton
system satisfies the quantitative charge bound

\[
 R=O(p\,m^{-3/4}),                                  \tag{6.3}
\]

then (6.2) follows. Equation (5.2) proves this scale only for independent
unrestricted atoms; it does **not** prove (6.3) after chain-pool conditioning.
Thus the numerical \(m^{-2}\) tail is sufficient only after both the physical
signed-cycle structure and survival of the tail estimate have been proved.

For the proportional contraction currently available, none of hypotheses
1--4 is proved:

* Lemma 3.1 and Theorem 4.1 show that contraction does not construct, and
  cannot universally induce, the required invariant two-shore row cube.
* Lemma 3.2 shows that unrestricted overlap does not survive prescribed-chain
  conditioning without a new fiber theorem.
* The first-intersection graph and target multiplicities at least three are
  uncontrolled.
* Lemma 5.1 and Proposition 5.2 show that double intersections do not control
  simple odd-cycle frustration.

---

## 7. Exact proved/conditional boundary

### Proved

1. The noncover collision majorant has the favorable leading scale
   \((45+o(1))/m^2\).
2. The exact contraction tradeoff is (2.6). A genuine vertical chain
   contraction has residual at least \((2+o(1))/m\), while \(O(m^{-2})\)
   forces one central component.
3. Retaining \(p-o(p/\sqrt m)\) rows leaves \(W-o(W)\) first-order seams for
   any one-chain resolution.
4. Contracting every cover pair globally collapses both central ranks;
   contracting it occurrencewise is not a target-capacity quotient.
5. An independent MaxCut cube required to preserve one fixed contracted
   capacity vector needs equal projected shores. Vertical chain contraction
   supplies no such shores.
6. The exact fixed-chain fiber is (3.4), so the unrestricted overlap estimate
   cannot simply be conditioned through the Boolean SCD.
7. There exist two target-disjoint physical atoms with no mixed common-row
   signing.
8. For \(p\) independent unrestricted atoms, the \(m^{-2}\) tail bounds the
   expected repeated intersections by \(O(p m^{-3/4})\), but it does not
   control singleton intersections or simple-graph frustration after
   contraction.
9. Under the explicit parity-forest hypotheses, Theorem 6.1 gives the desired
   common-row lift.

### Unproved

1. No row-compatible global chain pool with nonvanishing, near-regular
   physical-row fibers is known.
2. No literal equal-shore trade decomposition, with single- or multirow
   shores, is known after contraction.
3. No theorem converts the internal laminar cover forest into a nearly
   bipartite singleton-intersection graph with

   \[
   \operatorname{fr}=o(p/\sqrt m).
   \]

4. Higher target multiplicities and the common all-depth row state remain
   uncontrolled.

Accordingly, vertical cover-chain contraction plus residual
\(O(m^{-2})\) cross-column overlap does not prove a
\(p-o(p/\sqrt m)\) common-row packing. The precise quantitative failure is
that reaching the advertised tail already forces whole-ladder contraction,
while using MaxCut after that contraction requires a two-shore row trade and
a near-bipartite simple constraint graph that have not been constructed. No
claim against the proportional matching lemma itself, MWB, or constant one
is made.
