# From ideal owner slots to endpoint chains: exact cocycle and the uncrossing obstruction

Date: 2026-08-01  
Status: unconditional reduction, exact fixed-SDR chainization formula, and
explicit counterexamples.  This note does not prove an integral bounded-chain
factor or a universal OR word.

## 0. Verdict

The ideal containment SDR theorem closes ordinary Hall, but it is not one
uncrossing step away from the physical lower compiler.

There are exactly three successive objects.

1. **Ideal slots.**  Each strict-lower target `S` is sent to one labelled
   slot `(T,j)` with `S subset T`, where `T` has rank `r`.
2. **Owner chains.**  The targets sent to one owner must be totally ordered
   by inclusion.  This is a perfect matching problem in a hypergraph of
   chain atoms, not the bipartite ideal-slot graph.
3. **Endpoint chronology.**  The owner chains must be ordered and embedded
   in one suffix-OR table satisfying an exact sliding cocycle.  Separate
   nestedness at every owner does not imply this cocycle.

For a fixed ideal SDR `M`, the exact number of its assigned targets that can
be retained without changing owners is

\[
             \sum_T h(F_T),                                    \tag{0.1}
\]

where `F_T` is the family assigned to `T` and `h(F_T)` is the height of that
family.  Hence the fixed-owner chainization loss is

\[
       |M|-\sum_T h(F_T).                                      \tag{0.2}
\]

This loss is not controlled by the ordinary Hall deficiency
`h=(Lambda-dW)_+`.  At `k=5,r=3,d=2` there is a full zero-deficiency ideal
SDR with fixed-owner chainization loss five.

The strongest exact positive reduction is therefore:

> construct an integral bounded owner-chain factor; then solve the
> sliding-OR cocycle on those chain occurrences.

The fractional owner-chain theorem proves the first object fractionally at
depth `D<=d+1`, but neither integral rounding nor the cocycle follows from
ordinary containment Hall.

## 1. The integral owner-chain hypergraph

Let

\[
 \mathcal L=\{S\subseteq[k]:1\le |S|<r\},\qquad
 \mathcal O=\binom{[k]}r .                                  \tag{1.1}
\]

For `q>=1`, a **q-chain atom** is a pair `(T,C)` with `T in O` and

\[
 C=(S_1\subsetneq\cdots\subsetneq S_t),\qquad
 0\le t\le q,\qquad S_t\subset T .                         \tag{1.2}
\]

The empty chain is allowed.  Form the hypergraph whose vertices are
`L dot-union O` and whose atom `(T,C)` covers the owner vertex `T` and all
target vertices in `C`.

### Theorem 1.1 (exact chain-factor equivalence)

There is an assignment of every lower target to one of `q` slots at each
owner, with the targets at every owner nested, if and only if the chain-atom
hypergraph has a matching which covers every vertex of `L` and uses every
owner exactly once (empty atoms pad unused owners).

#### Proof

From a nested slot assignment, sort the nonempty targets at each owner and
take the resulting atom.  Target uniqueness makes the atoms disjoint and
the owner labels make them use every owner once.  Conversely, order each
chosen atom by inclusion and place its members in the labelled owner slots.
\(\square\)

Dropping all pairwise comparability requirements from (1.2) projects this
hypergraph matching onto the ideal containment SDR.  The projection is not
integrality preserving: the ideal problem is bipartite and totally
unimodular, whereas chain atoms couple up to `q` named lower targets in one
hyperedge.

There is an equivalent graph-theoretic formulation.  Let `G_inc` be the
incomparability graph on `L`.  Give a target `S` the colour list

\[
                    \mathcal A(S)=\{T\in\mathcal O:S\subset T\}.          \tag{1.3}
\]

Then an integral owner-chain factor is exactly a capacitated list colouring
of `G_inc`: colour `T` may be used at most `q` times, and every colour class
must be an independent set of `G_inc`, hence a chain.  The ideal SDR is the
same list-colouring problem with all incomparability edges erased.  Although
an incomparability graph is perfect, capacitated list colouring is not
determined by the slot Hall inequalities.  This pinpoints the lost
integrality when one passes from chain atoms to independent owner copies.

Define the exact integral chainization deficiency

\[
 \gamma_q=
  |\mathcal L|-\max\left\{
       \sum_{T\in\mathcal O}|C_T|:
       C_T\text{ are pairwise target-disjoint q-chains below }T
                         \right\}.                           \tag{1.4}
\]

Then

\[
              \gamma_q\ge (\Lambda-qW)_+.                  \tag{1.5}
\]

The fractional owner-chain theorem attains equality in the fractional
relaxation for `q=d`, and gives fractional deficiency zero for
`q=D=ceil(Lambda/W)<=d+1`.  The missing statement is the integral analogue
of that equality.

### Corollary 1.2 (bounded Boolean-half chain partition)

Let

\[
 \mathcal B_{\le r}^{\times}
   =\{S\subseteq[k]:1\le |S|\le r\}.
\]

An integral `q`-chain factor exists if and only if
`B_(<=r)^times` has a partition into exactly `W` inclusion chains, each of
size at most `q+1`.

#### Proof

Given a chain factor, append its owner `T` to the chain selected at `T`.
The resulting `W` chains are disjoint and cover the strict lower ideal and
all `W` rank-`r` sets.

Conversely, the rank-`r` layer is an antichain of size `W`.  A partition of
`B_(<=r)^times` into `W` chains therefore places exactly one rank-`r` set in
each chain.  It is the top of that chain.  Removing those tops gives the
required owner-chain atoms. \(\square\)

Thus the integral rounding gate is exactly a bounded uniform-chain problem
for one Boolean half.  For even `k`, complementation identifies this, up to
the empty/full boundary, with the upper-half setting of Conjecture 4.2 in
Sudakov--Tomon--Wagner, *Uniform chain decompositions and applications*
(`arXiv:1911.09533`).  Their theorem makes almost all chains asymptotically
uniform; it does not supply the exact maximum length `d+O(1)` required here.

## 2. Exact chainization of one fixed ideal SDR

Let `M` be any ideal containment matching, not necessarily saturating all
targets.  For an owner `T`, let

\[
                    F_T=\{S:M(S)=(T,j)\text{ for some }j\}.  \tag{2.1}
\]

### Theorem 2.1 (fixed-owner height formula)

The maximum number of edges of `M` which can be retained while making every
owner fibre a chain is exactly

\[
                         \sum_T h(F_T).                      \tag{2.2}
\]

Consequently the minimum deletion count without moving a target to another
owner is (0.2).

#### Proof

At owner `T`, a retained nested family is precisely a chain in the induced
poset `F_T`, so it has size at most `h(F_T)`.  Maximum chains may be chosen
independently at different owners because the original matching already
uses every target at most once.  Their union attains the sum. \(\square\)

This is the sharp relation between an already chosen ideal SDR and
chainization.  Ordinary Hall deficiency records only the number of matched
targets; it records none of the heights `h(F_T)`.

## 3. Zero-deficiency counterexample to fixed-SDR laminarization

Take `k=5,r=3,d=2`.  Then

\[
 W=\binom53=10,\qquad \Lambda=\binom51+\binom52=15,
 \qquad (\Lambda-dW)_+=0.                                  \tag{3.1}
\]

Use the following five owners for all ten pairs:

\[
\begin{array}{c|c}
123&12,13\\
145&14,15\\
234&23,24\\
235&25,35\\
345&34,45
\end{array}                                                  \tag{3.2}
\]

and the other five owners for the five singletons:

\[
 124\mapsto1,quad125\mapsto2,quad134\mapsto3,quad
 135\mapsto5,quad245\mapsto4.                              \tag{3.3}
\]

Every displayed target is contained in its owner, all fifteen targets are
distinct, and no owner uses more than two slots.  Thus (3.2)--(3.3) is a
full ideal SDR with zero Hall deficiency.

At each owner in (3.2), the two assigned pairs are distinct sets of the same
rank and are therefore incomparable.  Its fibre has height one.  The five
singleton fibres also have height one.  Theorem 2.1 gives

\[
             \max\text{ retained}=5+5=10,qquad
             \text{fixed-owner loss}=15-10=5.               \tag{3.4}
\]

Thus a zero-deficiency ideal SDR need not even be close to chainized in its
chosen owner fibres.  One must globally reassign targets; sorting the slot
labels is insufficient.

The usual lattice uncrossing is unavailable.  For example, the two targets
`12,13` at owner `123` would be replaced by their meet `1` and join `123`.
The join is a rank-`r` owner, not a strict-lower target, while the meet `1`
is another named target already present elsewhere.  Hence meet/join
replacement does not preserve the target multiset, its rank counts, or the
matching problem.  Submodular uncrossing cannot be invoked on these named
target vertices.

This counterexample does not say that no different chainized factor exists
at `k=5`; one does.  It proves the precise negative needed here: ordinary
Hall plus an arbitrary integral SDR does not carry a lossless uncrossing
procedure.

## 4. A useful positive owner-extension criterion

Suppose the lower ideal has first been partitioned into at most `W` chains
of length at most `q`.  Let `U_C` be the top of chain `C`.  Assigning those
chains to distinct rank-`r` owners is exactly the Hall problem

\[
 \left|\left\{T\in\binom{[k]}r:
            U_C\subset T\text{ for some }C\in\mathcal A\right\}\right|
       \ge |\mathcal A|                                     \tag{4.1}
\]

for every subfamily `A` of chains.

There is a clean sufficient case.

### Proposition 4.1 (antichain tops extend automatically)

If the chain tops form an antichain, then they admit distinct containing
rank-`r` owners.

#### Proof

Fix any symmetric-chain decomposition of the Boolean lattice.  An antichain
meets each symmetric chain at most once.  Move every top upward along its
own symmetric chain to rank `r`.  The images are distinct rank-`r` sets and
contain their preimages. \(\square\)

Therefore a bounded chain partition with antichain tops immediately gives
an integral owner-chain factor.  Without the antichain condition, (4.1) is
the exact remaining owner-extension test.

This shows why the current target is close to a one-sided uniform-chain
theorem: one needs roughly `W` lower chains of maximum size `d` or `d+1`,
not merely `D` independent copies of every owner.

## 5. Exact endpoint suffix-OR cocycle

Owner chains are still not a chronology.  Let `A=(A_1,...,A_n)` be a word
and define, whenever the indices exist,

\[
       Q_{j,t}=A_{j-t+1}\cup\cdots\cup A_j,
       \qquad 1\le t\le d+1.                               \tag{5.1}
\]

For fixed `j`, the values `Q_(j,1),...,Q_(j,d)` form the strict-lower
endpoint chain below the central owner `Q_(j,d+1)`.

### Theorem 5.1 (sliding-OR cocycle)

A triangular table `(Q_(j,t))` is the suffix-OR table of a word if and only
if

\[
 \boxed{
 Q_{j,t}=Q_{j-1,t-1}\cup Q_{j,1}
       \quad(t\ge2)
 }                                                            \tag{5.2}
\]

at every valid address.  In that case the word is uniquely recovered as

\[
                              A_j=Q_{j,1}.                    \tag{5.3}
\]

The central owner ending at `j` is

\[
                              T_j=Q_{j,d+1}.                  \tag{5.4}
\]

#### Proof

Equation (5.2) follows by separating the last letter from the length-`t`
suffix.  Conversely set `A_j=Q_(j,1)` and induct on `t`; (5.2) gives (5.1)
at every cell. \(\square\)

Thus the exact chronology problem is not just to order the chains.  One
must choose an order, assign each chain member to a physical length, and
fill every unused cell so that the overlapping endpoint chains obey (5.2).
The same singleton row is shared by all depths.

### Minimal chronology counterexample

At depth two, prescribe consecutive endpoint data

\[
 Q_{1,1}=\{3\},\qquad
 Q_{2,1}=\{1\},\qquad Q_{2,2}=\{1,2\}.                      \tag{5.5}
\]

Each individual endpoint family is nested, but (5.2) demands

\[
 Q_{2,2}=Q_{1,1}\cup Q_{2,1}=\{1,3\},                      \tag{5.6}
\]

contradicting (5.5).  Hence separate owner-chain feasibility does not imply
serialization even on two consecutive columns.

## 6. Exact implication for the `d`-copy deficiency

Let `h=(Lambda-dW)_+`.  The ideal theorem proves a `d`-slot matching missing
at most `h` targets, and the fractional chain theorem proves a depth-`d`
fractional owner-chain packing missing exactly `h` mass.  The integral
statement actually needed is

\[
                         \gamma_d\le h+C,                    \tag{6.1}
\]

for an absolute `C` (with `C=0` for exact equality), together with a
serialization satisfying (5.2) and the upper/residence/common-cap rows.

Neither existing theorem implies (6.1).  The counterexample in Section 3
shows that it cannot be obtained by chainizing an arbitrary ideal SDR while
keeping its owner fibres.  The fractional theorem shows that any failure of
(6.1) is a genuine integrality/correlation gap, not a capacity gap.

For the robust two-prefix/common-`Q` compiler, the same distinction is
literal.  Its two rays are already chains, but their bases and outward
traces must occupy one suffix-OR table satisfying (5.2).  The conditional
two-host rail is an explicit local solution of that cocycle.  The unresolved
task is planting and regenerating those occurrences in the global table,
not matching the ray targets to abstract containing owners.

## 7. Strongest honest frontier

The current all-dimensional lower-compiler chain is

\[
\begin{array}{c}
\text{ideal containment SDR}\quad\text{(integral, proved)}\\
\Downarrow\quad\text{projection only}\\
\text{fractional owner-chain factor}\quad\text{(proved)}\\
\Downarrow\quad\text{integral hypergraph rounding open}\\
\text{integral bounded owner-chain factor}\\
\Downarrow\quad\text{sliding cocycle (5.2) open globally}\\
\text{physical endpoint compiler chronology}.
\end{array}                                                   \tag{7.1}
\]

Ordinary containment Hall is finished.  The next theorem should target the
integral chain-atom hypergraph or directly construct a cocycle table; a
generic SDR uncrossing lemma is false in the precise fixed-owner sense above.
