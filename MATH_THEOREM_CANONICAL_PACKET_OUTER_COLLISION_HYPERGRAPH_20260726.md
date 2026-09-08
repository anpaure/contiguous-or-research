# The outer physical collision hypergraph of canonical tensor packets

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Fix the canonical first-\(r\)-eligible packet partition and, inside every
packet, one face-separated product decomposition into equal \(Q_s\)-cells,
where \(s\) is a power of two and

\[
                         H\le s/2.                      \tag{0.1}
\]

Let \(G=W-o(W)\) be the number of covered middle owners. The product cells
form a vertex partition

\[
                         \mathscr C,\qquad
 |\mathscr C|={G\over2^s}.                              \tag{0.2}
\]

In each cell \(c\), take the full cube-automorphism orbit
\(\mathscr R_c\) of the recursive injective factor \(F_s\). Selecting one
member of \(\mathscr R_c\) independently for every \(c\) always preserves
middle ownership exactly. Thus the outer problem is not an owner matching:
it is a multiple-choice physical-target covering problem.

For a physical lower or upper target \(T\) at depth \(q\), let

\[
 d^\epsilon_q(T)
 =\#\{c\in\mathscr C:
       T\text{ is the }\epsilon\text{-trace of a }q
       \text{-face of }c\},
 \qquad\epsilon\in\{-,+\}.                              \tag{0.3}
\]

The face, when it exists in a fixed cell, is unique. Under a uniform
factor conjugate in that cell, its exact hit probability is

\[
\boxed{
                         p_{s,q}={2^q\over\binom sq}.}   \tag{0.4}
\]

Consequently independent uniform conjugates give the exact physical miss
formula

\[
\boxed{
 \mathbb E M^\epsilon_q
 =\sum_{T\in\binom{[n]}{m+\epsilon q}}
       (1-p_{s,q})^{d^\epsilon_q(T)}.}                  \tag{0.5}
\]

Here \(m+\epsilon q\) means \(m-q\) for \(\epsilon=-\) and \(m+q\) for
\(\epsilon=+\). Therefore the physical degree condition

\[
 \boxed{
 \sum_{q\le H}\sum_{\epsilon=\pm}\sum_T
       (1-p_{s,q})^{d^\epsilon_q(T)}=o(W)}              \tag{0.6}
\]

is sufficient for one simultaneous integral selection with total missing
mass \(o(W)\), and hence with collision excess equal to the unavoidable
baseline plus \(o(W)\).

The exact first moment of the candidate degrees is

\[
\boxed{
 \sum_Td^\epsilon_q(T)
 =G\,{\binom sq\over2^q},\qquad
 \overline d^\epsilon_q
 ={G\over N^\epsilon_q}{\binom sq\over2^q}.}            \tag{0.7}
\]

Thus

\[
                         p_{s,q}\overline d^\epsilon_q
 ={G\over N^\epsilon_q},                               \tag{0.8}
\]

which is the exact average target load.

Uniform independent conjugation cannot solve the shallow depths. Since
\(d\mapsto(1-p)^d\) is convex, (0.5)--(0.8) imply

\[
\boxed{
 {\mathbb E M^\epsilon_q\over N^\epsilon_q}
 \ge
 (1-p_{s,q})^{(G/N^\epsilon_q)/p_{s,q}}.}              \tag{0.9}
\]

For \(q=o(\sqrt m)\), \(G/N^\epsilon_q=1+o(1)\), and when
\(p_{s,q}=o(1)\), the right side is

\[
                         e^{-1-o(1)}.                   \tag{0.10}
\]

Hence random conjugation has \(\Theta(W)\) expected holes already at one
shallow depth. A structured exact-cover or one-sided discrepancy theorem
is genuinely necessary there.

The raw incidence has exact local codegree atoms. Every selected affine
face contributes its lower and upper physical targets together, and every
factor is closed under antipodal translation of faces. Inside one
candidate cell these give target pairs with

\[
\boxed{\text{local codegree}=\text{local degree}
       =|\Gamma_s|p_{s,q}.}                             \tag{0.11}
\]

After physical targets are merged across cells, the global relative
codegree depends on how many common candidate cells the two targets have.
Thus no low-codegree theorem follows from cube symmetry alone. One must
compute the common-candidate census, or quotient the inseparable
lower/upper-antipodal quartets and prove codegree estimates for that
quotient.

Finally, the exact fractional obstruction is a Hall-support-function
dual. If \(\mathcal S(c,g)\) is the complete set of tagged physical targets
at all depths and both signs supplied by choice \(g\in\mathscr R_c\), then
the fractional minimum number of uncovered target resources is

\[
\boxed{
 \max_{0\le\alpha\le1}
 \left[
  \sum_T\alpha_T
  -\sum_{c\in\mathscr C}
       \max_{g\in\mathscr R_c}
          \sum_{T\in\mathcal S(c,g)}\alpha_T
 \right].}                                             \tag{0.12}
\]

Thus zero fractional deficit is equivalent to the exact cut system

\[
\boxed{
 \sum_T\alpha_T
 \le
 \sum_c\max_{g\in\mathscr R_c}
          \sum_{T\in\mathcal S(c,g)}\alpha_T
 \quad(0\le\alpha\le1).}                               \tag{0.13}
\]

Equations (0.6) and (0.13) isolate the remaining alternatives:

1. prove the physical degree exponential-moment bound (0.6), which is
   sufficient but impossible for uniform random choices at shallow depth;
2. prove the full weighted cut inequalities (0.13) and a specialized
   rounding theorem for resolvable shadow towers.

No sectorwise marginal statement implies either condition.

## 1. Canonical cells and available choices

The canonical packet theorem partitions all but \(o(W)\) middle owners
into packets isomorphic to \(\mathcal V^r\). Fix in every packet the same
local \(Q_2/Q_3\) resolution pattern from the packet-wide injectivity
theorem. If \(a\) local blocks use a six-\(Q_2\) resolution and \(b\) use
a three-\(Q_3\) resolution, every product cell has dimension

\[
                         s=2a+3b.                       \tag{1.1}
\]

Passive local owners are part of the fixed cell label. The local
face-separation theorem implies:

### Lemma 1.1 (unique candidate face in one cell)

Fix a product cell \(c\), a depth \(q\le s\), a sign
\(\epsilon\in\{-,+\}\), and a physical target \(T\). There is at most one
affine \(q\)-face \(R\subseteq c\) whose lower or upper physical trace is
\(T\).

#### Proof

Inside a constant-weight cube, a lower target identifies the active pairs
which are empty and the orientations on every other active pair. An upper
target identifies the active pairs which are full and the same outside
orientations. Thus the physical trace identifies the affine face once the
cell is known. \(\square\)

Different cells can have the same physical trace; those are precisely the
outer collisions.

Let \(\Gamma_s=\operatorname{Aut}(Q_s)=\mathbb F_2^s\rtimes S_s\). For a
base factor \(F_s\), every \(a\in\Gamma_s\) supplies the conjugate

\[
                         aF_sa^{-1}.                    \tag{1.2}
\]

It is harmless to regard automorphisms producing the same factor as
separate menu labels. This gives a uniform finite menu

\[
                         \mathscr R_c=\Gamma_s           \tag{1.3}
\]

in every cell and makes all degree counts literal. Quotienting by the
factor stabilizer divides every degree and codegree by the same number.

Because product cells are owner-disjoint, a tuple

\[
                         g=(g_c:c\in\mathscr C),
 \qquad g_c\in\mathscr R_c,                             \tag{1.4}
\]

always gives a spanning factor of all \(G\) retained owners. No Hall
condition remains on the owner side.

## 2. The exact multiple-choice collision hypergraph

Create one choice color for every cell \(c\). Its alternatives are the
vertices

\[
                         (c,g),\qquad g\in\mathscr R_c. \tag{2.1}
\]

The resource vertices are tagged triples

\[
                         (q,\epsilon,T),
 \qquad1\le q\le H,\quad\epsilon\in\{-,+\}.             \tag{2.2}
\]

The hyperedge of a choice is

\[
 \mathcal S(c,g)
 =\{(q,\epsilon,T):
    T\text{ is a physical }q\text{-trace of }g
    \text{ in }c\}.                                    \tag{2.3}
\]

Packet-wide injectivity implies

\[
 |\mathcal S(c,g)\cap(\{q,\epsilon\}\times\mathcal T^\epsilon_q)|
 =2^s                                                     \tag{2.4}
\]

for every \(q,\epsilon\). Hence

\[
                         |\mathcal S(c,g)|=2H\,2^s.     \tag{2.5}
\]

The outer problem is:

\[
 \boxed{\text{choose one hyperedge of every color }c
 \text{ while controlling the loads of (2.2).}}        \tag{2.6}
\]

This is a resolvable multiple-choice hypergraph, not an ordinary matching
hypergraph. All alternatives of one color cover the same middle owners,
so adding owner vertices would only duplicate the already solved partition.

For a selected tuple \(g\), define

\[
 n^\epsilon_q(T)
 =\#\{c:(q,\epsilon,T)\in\mathcal S(c,g_c)\}.           \tag{2.7}
\]

There are exactly \(G\) occurrences at each tagged rank:

\[
                         \sum_Tn^\epsilon_q(T)=G.       \tag{2.8}
\]

Put

\[
 C^\epsilon_q=\sum_T(n^\epsilon_q(T)-1)_+,\qquad
 M^\epsilon_q=\#\{T:n^\epsilon_q(T)=0\}.               \tag{2.9}
\]

Then

\[
\boxed{
 M^\epsilon_q=N^\epsilon_q-G+C^\epsilon_q.}            \tag{2.10}
\]

Whenever \(G\ge N^\epsilon_q\), this becomes

\[
 C^\epsilon_q-(G-N^\epsilon_q)=M^\epsilon_q.           \tag{2.11}
\]

In general the exact baseline-corrected identity is

\[
\boxed{
 C^\epsilon_q-(G-N^\epsilon_q)_+
 =M^\epsilon_q-(N^\epsilon_q-G)_+.}                    \tag{2.12}
\]

The second positive part is the forced shortage caused by the omitted
middle owners. For the canonical leave its aggregate is \(o(W)\).
Therefore collision excess equals its unavoidable baseline plus \(o(W)\)
exactly when the aggregate physical missing mass is \(o(W)\), up to this
already audited leave.

## 3. Exact degrees

The number of affine \(q\)-faces in \(Q_s\) is

\[
                         F_{s,q}=2^{s-q}\binom sq.      \tag{3.1}
\]

The factor \(F_s\) has one \(q\)-window at every cube vertex and is
shadow-injective through \(s/2\). Therefore it selects exactly

\[
                         2^s                            \tag{3.2}
\]

distinct affine \(q\)-faces.

The cube automorphism group is transitive on affine \(q\)-faces. For a
fixed face \(R\),

\[
 \Pr_{a\in\Gamma_s}\{R\text{ is selected by }aF_sa^{-1}\}
 ={2^s\over F_{s,q}}
 ={2^q\over\binom sq}=p_{s,q}.                         \tag{3.3}
\]

By Lemma 1.1, a target \(T\) has one prescribed candidate face in each
candidate cell and none in other cells. Consequently its degree in one
candidate color is

\[
                         |\Gamma_s|p_{s,q},             \tag{3.4}
\]

and its total degree over all colors is

\[
\boxed{
                         \deg(q,\epsilon,T)
 =|\Gamma_s|p_{s,q}d^\epsilon_q(T).}                   \tag{3.5}
\]

To sum candidate degrees, count all affine faces in all cells. There are
\(G/2^s\) cells, each contributing (3.1) distinct physical target
incidences. Thus

\[
 \sum_Td^\epsilon_q(T)
 ={G\over2^s}2^{s-q}\binom sq
 =G{\binom sq\over2^q},                                \tag{3.6}
\]

proving (0.7)--(0.8).

The count is physical: equal targets from different cells are merged on
the left side and contribute their multiplicity to \(d(T)\).

## 4. Exact codegrees and higher overlaps

For a cell \(c\), let

\[
                         \mathscr F_q(F_s)              \tag{4.1}
\]

be the \(2^s\)-set of affine \(q\)-faces selected by the base factor.
The group \(\Gamma_s\) has finitely many orbits on tuples of affine faces.
For an ordered tuple \(\mathbf R=(R_1,\ldots,R_k)\), let
\(\tau(\mathbf R)\) denote its orbit type, let
\(\mathcal O_\tau\) be that orbit, and put

\[
 N_F(\tau)=
 \#\{(A_1,\ldots,A_k):
      A_i\in\mathscr F_{q_i}(F_s),\
      \tau(A_1,\ldots,A_k)=\tau\}.                     \tag{4.2}
\]

### Proposition 4.1 (orbit codegree formula)

For prescribed candidate faces \(\mathbf R\) in one cell,

\[
\boxed{
 {1\over|\Gamma_s|}
 \#\{a:R_i\in a\mathscr F_{q_i}(F_s)\ \forall i\}
 ={N_F(\tau(\mathbf R))\over|\mathcal O_{\tau(\mathbf R)}|}.}
\tag{4.3}
\]

#### Proof

Count pairs

\[
 (a,(A_1,\ldots,A_k)):
 a(A_i)=R_i\ \forall i
\]

with the base tuple restricted to orbit type \(\tau(\mathbf R)\). The
group acts transitively on \(\mathcal O_\tau\), so every target tuple has
the same number of preimages. Dividing the total by
\(|\Gamma_s||\mathcal O_\tau|\) proves (4.3). \(\square\)

Formula (4.3) is the exact higher-overlap ledger. It reduces every
codegree question to a finite orbit count inside the recursive factor,
without replacing physical targets by pair types or marginal labels.

If two target faces lie in different product cells of one packet, the
packet menu is the Cartesian product of the cell menus. Their normalized
codegree is exactly the product of the two single-face probabilities.
All nontrivial codegree geometry is therefore local to one \(Q_s\)-cell.

### Proposition 4.2 (maximal atomic codegrees)

Inside one candidate cell there are distinct physical target resources
whose local codegree equals their local degree.

#### Proof

First fix one selected affine \(q\)-face \(R\). Its lower and upper traces
\[
                         L(R),\qquad U(R)               \tag{4.4}
\]

are supplied together, for every factor choice. Hence their incidence
sets in \(\mathscr R_c\) are identical.

Second, every isometric \(2s\)-cycle reaches the antipodal cube vertex
after \(s\) steps and repeats its direction word. Therefore, whenever a
\(q\)-face \(R\) occurs as a consecutive window, so does

\[
                         R+\mathbf1.                    \tag{4.5}
\]

Conjugation by a cube automorphism preserves the antipodal translation.
Thus \(R\) and \(R+\mathbf1\) also have identical incidence sets.

Combining (4.4)--(4.5), the four resources

\[
 L(R),\ U(R),\ L(R+\mathbf1),\ U(R+\mathbf1)            \tag{4.6}
\]

occur as an inseparable atom in that cell. Any two have local codegree
\(|\Gamma_s|p_{s,q}\), equal to their common local degree. \(\square\)

For arbitrary physical targets \(T,U\), the exact global codegree is

\[
\boxed{
 \operatorname {codeg}(T,U)
 =|\Gamma_s|
   \sum_{c\in\mathscr C(T)\cap\mathscr C(U)}
      p_c(T,U),}                                        \tag{4.7}
\]

where \(p_c(T,U)\) is the orbit ratio in (4.3). For an atomic pairing in
cell \(c\), \(p_c(T,U)=p_{s,q}\). Hence the ratio of (4.7) to the target
degrees (3.5) is controlled by the number of common candidate cells, not
by the internal cube dimension alone.

The correct first quotient nevertheless replaces every local quartet
(4.6) by one atomic resource. Proposition 4.1 remains the exact codegree
formula after this quotient. No small-codegree theorem for the physical
quotient has yet been proved.

## 5. Independent conjugation: exact theorem and exact failure

Choose every cell conjugate independently and uniformly. A target \(T\)
is missed precisely when every one of its candidate cells misses its
unique candidate face. The events belong to different cells and are
independent. Equation (3.3) therefore gives

\[
 \Pr\{T\text{ missed at }(q,\epsilon)\}
 =(1-p_{s,q})^{d^\epsilon_q(T)},                       \tag{5.1}
\]

proving (0.5). Summing (5.1) over all tagged physical targets and applying
the probabilistic method proves (0.6).

This theorem needs the complete degree sequence, not merely its average.
Nevertheless the average already proves that uniform random choices fail
at shallow depths. Since

\[
                         f(d)=(1-p)^d                  \tag{5.2}
\]

is convex, Jensen and (0.7) give (0.9).

For \(q=o(\sqrt m)\),

\[
 {G\over N^\epsilon_q}=1+o(1).                         \tag{5.3}
\]

If \(p=p_{s,q}=o(1)\), then

\[
 (1-p)^{(1+o(1))/p}=e^{-1-o(1)},                       \tag{5.4}
\]

which proves (0.10). In particular, even a perfectly uniform candidate
degree sequence would leave a constant fraction of physical targets under
independent selection.

At deeper ranks, (0.6) can still be useful. A sufficient physical
lower-tail condition is

\[
 \sum_{q,\epsilon}
 \#\{T:p_{s,q}d^\epsilon_q(T)<L_q\}
 +\sum_{q,\epsilon}N^\epsilon_qe^{-L_q}
 =o(W).                                                \tag{5.5}
\]

Taking \(L_q-\log H\to\infty\) makes the second term \(o(W)\). The first
term is the exact candidate-degree lower tail which must then be proved.

## 6. Exact-cover and Hall dual

Let

\[
                         \mathcal T
 =\{(q,\epsilon,T):q\le H,\epsilon=\pm\}                \tag{6.1}
\]

be the full tagged target set. Consider the fractional program

\[
\begin{aligned}
 \min\quad&\sum_{T\in\mathcal T}z_T\\
 \text{s.t.}\quad&
 \sum_{g\in\mathscr R_c}x_{c,g}=1
                   &&(c\in\mathscr C),\\
 &\sum_{c,g:T\in\mathcal S(c,g)}x_{c,g}+z_T\ge1
                   &&(T\in\mathcal T),\\
 &x_{c,g}\ge0,\qquad z_T\ge0.                          \tag{6.2}
\end{aligned}
\]

### Theorem 6.1 (exact fractional cut dual)

The value of (6.2) is

\[
\boxed{
 \max_{0\le\alpha_T\le1}
 \left[
  \sum_T\alpha_T
  -\sum_c\max_{g\in\mathscr R_c}
          \sum_{T\in\mathcal S(c,g)}\alpha_T
 \right].}                                             \tag{6.3}
\]

#### Proof

Give the target covering constraints nonnegative dual weights
\(\alpha_T\). Minimization over \(z_T\ge0\) forces
\(\alpha_T\le1\). For fixed \(\alpha\), minimization over the simplex
\(\sum_gx_{c,g}=1\) chooses a conjugate maximizing its total
\(\alpha\)-weight. Its contribution is

\[
                         -\max_g\sum_{T\in\mathcal S(c,g)}\alpha_T.
\]

Adding the constant \(\sum_T\alpha_T\) proves (6.3). \(\square\)

Zero fractional missing mass is therefore equivalent to (0.13). This is
the exact Hall theorem for whole factor conjugates. Testing only target
indicators, macroprofiles, pair types, or separate depths is weaker than
testing all \(\alpha\) in (0.13).

For desired integer capacities \(b_T\), replace the first term in (6.3)
by

\[
                         \sum_Tb_T\alpha_T.             \tag{6.4}
\]

This gives the exact fractional test for floor/ceiling MWB loads or other
baseline allocations.

## 7. Why generic matching and discrepancy do not close the gate

### 7.1 Exact cover

The canonical middle-owner partition removes the owner side of exact
cover. The unresolved target system (6.2) has columns of size
\(2H2^s\), and its matrix is not a network matrix: all targets in the
same shadow tower are selected together. No total-unimodularity statement
follows from the product-cell partition.

### 7.2 Rainbow matching and nibble

Regard cells as colors and conjugates as colored hyperedges. Proposition
4.2 shows that cellwise cube symmetry gives no relative-codegree saving:
some pairs are forced whenever either member is forced. Whether a global
low-codegree hypothesis holds depends on (4.7), namely the physical
common-candidate census. It has not been proved. Moreover the desired
solution permits the unavoidable baseline target overlaps, so it is a
capacitated cover rather than an ordinary matching. Quotienting the local
quartets and cloning target capacities are necessary before a
rainbow-matching or nibble theorem could even be applied.

### 7.3 Discrepancy

Rounding a fractional solution of (6.2) is a multiple-choice vector
discrepancy problem. Generic discrepancy bounds are additive, while the
shallow target quotas are one or \(1+o(1)\). An \(O(\sqrt d)\) coordinate
error can therefore create a positive-density set of holes even if its
relative error is small. What is required is a one-sided aggregate loss
bound

\[
 \sum_T\left(1-\sum_{c,g:T\in\mathcal S(c,g)}
                       x^{\rm int}_{c,g}\right)_+=o(W), \tag{7.1}
\]

simultaneously over all depths, not a bound on separate marginals or on
the maximum signed coordinate discrepancy.

## 8. The exact remaining combinatorial lemma

The internal packet theorem and the present outer audit reduce the
constant-one lane to the following statement.

### Resolvable shadow-tower cover, \({\rm RSTC}(m,H,s)\)

For the canonical physical cell family \(\mathscr C\) and menus
\(\mathscr R_c\), choose one \(g_c\in\mathscr R_c\) per cell so that

\[
\boxed{
 \sum_{q\le H}\sum_{\epsilon=\pm}
 \#\left\{
 T:\sum_c{\bf1}_{\{T\in\mathcal S(c,g_c)\}}=0
 \right\}=o(W).}                                       \tag{8.1}
\]

By (2.11), this is equivalent to collision excess baseline plus \(o(W)\).
It is an exact physical-target statement and retains all cross-depth
coupling.

Three rigorous facts now delimit it.

1. The zero-candidate support obstruction is small under the audited
   canonical coarse-completion hypotheses; almost every target has at
   least one candidate cell.
2. Uniform independent choices fail by (0.9)--(0.10), even with perfectly
   flat degrees.
3. Raw cube symmetry does not supply a low-codegree estimate; the exact
   missing census is (4.7).

Thus a positive proof must exploit the resolvable tower structure after
the atomic quotient, or prove the full weighted expansion (0.13) followed
by a specialized one-sided rounding theorem. Degrees, sectorwise quotas,
and generic discrepancy alone are insufficient.
