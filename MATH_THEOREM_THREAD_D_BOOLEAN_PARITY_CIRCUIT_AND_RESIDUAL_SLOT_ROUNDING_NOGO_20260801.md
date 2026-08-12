# Boolean parity circuits are not charged to the residual `C` slots

Date: 2026-08-01  
Lane: Thread D / prospective `M0` / bounded-defect rounding  
Status: exact full-LP fractional vertex at `m=3`; dimension-uniform local
parity circuit; linear resource-disjoint circuit bank; scoped no-go for
support-preserving or `O(C)` local rounding.  This is **not** a Boolean
integral-infeasibility theorem.

## 0. Verdict

The proposed route

> characterize every fractional vertex as disjoint odd circuits and pay one
> residual `M0` slot for each circuit

is false in two separate ways.

1.  The smallest relevant Boolean atom is an eight-column, four-colour
    three-way parity circuit.  Its compatibility graph is the cube `Q_3`,
    not an odd cycle.  Weight `1/2` on every column has value four, whereas
    the largest integral matching inside the support has value two.
2.  Every lower, tail, and head resource used by this fractional atom is
    already saturated by its `x` columns.  It uses **zero** residual `y`
    mass.  Thus it cannot be charged to the `C=Cat_m` unused lower/owner
    slots by a support-local accounting rule.

At `m=3` the atom extends to a literal fractional extreme point of the
complete oriented-diamond plus residual-matching LP.  In every `m>=3` the
same atom embeds by adding a fixed filler set.  Moreover, the Boolean
catalogue contains at least `U/64` pairwise role-resource-disjoint copies.
Rounding their combined restricted support needs at least `U/32` diamonds
outside that support, much larger than `C` for growing `m`.

This does **not** prove that the unrestricted Boolean system lacks an
integral solution, or even a bounded-defect solution.  It proves that any
such theorem must make genuinely global off-support exchanges.  In
particular, the unused slots cannot absorb fractional atoms one at a time.
The protected tight-pivot bank can be kept disjoint from the circuit bank,
so fixing that bank does not remove this method obstruction.

## 1. The Boolean parity circuit

Use the notation of
`MATH_THEOREM_THREAD_D_PROSPECTIVE_M0_ORIENTED_DIAMOND_AND_RESIDUAL_HALL_20260801.md`.
At `m=3`, consider the following eight genuine oriented diamonds:

\[
\begin{array}{c|c|c|c}
R&L&T&V\\ \hline
1234&14&124&134\\
1234&12&123&124\\
1235&13&123&135\\
1235&15&135&125\\
1245&12&124&125\\
1245&14&145&124\\
1345&15&145&135\\
1345&13&135&134.
\end{array}                                                     \tag{1.1}
\]

Every row satisfies `T intersect V=L` and `T union V=R`.

### Theorem 1.1 (four-colour cube circuit)

Give every column in (1.1) weight `1/2`.  Then:

1. every one of the four upper-colour rows has load one;
2. every used `L`, `T`, and `V` resource has load one;
3. no residual `y` variable is used; and
4. the largest integral upper/tail/head matching contained in these eight
   columns has size exactly two.

Hence this support has fractional value four and integral value two.

#### Proof

The used resources, with multiplicities before multiplying by `1/2`, are

\[
\begin{array}{c|c}
\text{role}&\text{four resources, each occurring twice}\\ \hline
L&12,13,14,15\\
T&123,124,135,145\\
V&124,125,134,135.
\end{array}                                                       \tag{1.2}
\]

Thus all fractional row assertions are immediate.

Join two columns when they have different upper colours and are disjoint
in all three resources `L,T,V`.  Directly from (1.1), the compatibility
edges are

\[
 (1,3),(1,4),(1,7),
 (2,4),(2,7),(2,8),
 (3,5),(3,6),
 (4,6),
 (5,7),(5,8),
 (6,8).                                                      \tag{1.3}
\]

where the columns are numbered from top to bottom.  This is a relabelling
of the three-cube `Q_3`.  In particular it is triangle-free.  Three
pairwise compatible columns would form a triangle, so an integral
matching has size at most two; edges in (1.3) show that size two is
attained.  \(\square\)

The obstruction is stronger than the earlier determinant-two minor: it is
an actual feasible fractional matching atom, and losing one colour does
not suffice to round it inside its support.

## 2. It is a vertex of the complete `m=3` LP

Add the integral diamond

\[
                 (2345;23,234,235)                                 \tag{2.1}
\]

and the five integral residual matching edges

\[
 25\to125,\quad34\to134,\quad35\to235,\quad
 24\to245,\quad45\to345.                                          \tag{2.2}
\]

Set every other `x` and `y` variable to zero.  Equations (1.1)--(2.2)
then satisfy every row of the linear relaxation of system (2.4): all five
upper rows and all lower/tail rows have load one, while every head row has
load at most one.

### Theorem 2.1 (literal fractional extreme point)

The point (1.1)--(2.2) is an extreme point of the complete prospective-`M0`
LP for `m=3`.

#### Proof

Restrict to the face on which every unlisted variable is zero.  The fifth
upper row fixes (2.1) to one.  For the first circuit colour, write its two
variables as `x_1,x_2`, and retain the numbering of (1.1).  The `L=14`
row, tight `V=124` row, and `R=1234` row give

\[
 x_1+x_6=1,qquad x_2+x_6=1,qquad x_1+x_2=1,
\]

so `x_1=x_2=x_6=1/2`.  Successively, the `R=1245`, tight
`V=125`, `R=1235`, tight `V=135`, and `R=1345` rows force

\[
 x_5=x_4=x_3=x_7=x_8=1/2.
\]

The five still-unused lower rows then force each variable in (2.2) to
one.  Hence the positive variables are uniquely determined on this face,
which proves extremality.  Equivalently, the active positive-column matrix
has rational rank `14` on `14` columns.  \(\square\)

So the parity atom is not merely a non-TU minor or an artificial restricted
subproblem.  It occurs in a full LP vertex.  The theorem does not say that
this fractional vertex is the only optimum or that the full integer system
is infeasible; in fact the finite `m=3` system has many positive integer
solutions.

## 3. Dimension-uniform embedding

For general `m>=3`, choose an `(m-3)`-set `S` disjoint from five labelled
points `1,2,3,4,5`, and adjoin `S` to every set in (1.1).  The resulting
rows have ranks `m+1,m-1,m,m` and remain genuine oriented diamonds.  All
conclusions of Theorem 1.1 are unchanged.

Thus half-integral Boolean parity circuits occur at every parameter.  This
embedding alone does not assert that the circuit extends to a full
fractional vertex at every `m`.

## 4. A linear resource-disjoint circuit bank

Let `P_m` be the full orbit of one padded circuit under coordinate
permutations.  Regard `R,L,T,V` as four separately tagged resource parts,
and form an auxiliary hypergraph whose edges are the sixteen role-resources
used by a circuit in `P_m`.

Put `N=|P_m|`.  The permutation group is transitive on each rank layer.
Every circuit uses four vertices in every role, so double counting gives

\[
 D_R={4N\over U},\qquad
 D_L=D_T=D_V={4N\over W}.                                         \tag{4.1}
\]

Since `U<W`, the maximum auxiliary degree is `D_R`.  A chosen circuit
conflicts with at most the sum of the degrees of its sixteen resources,
which is at most `16D_R`.  Greedy packing therefore proves:

### Theorem 4.1 (resource-disjoint parity bank)

There are at least

\[
                         \left\lfloor {U\over64}\right\rfloor      \tag{4.2}
\]

pairwise role-resource-disjoint padded parity circuits.

If a protected bank contains `p` fixed diamonds, delete all circuit copies
meeting one of its at most `4p` role-resources before applying the same
greedy argument.  At least

\[
                  \left\lfloor {U\over64}-{p\over4}\right\rfloor  \tag{4.3}
\]

pairwise disjoint circuits remain.  In particular, a tight-pivot bank of
length at most `m-1` changes only the lower-order subtraction in (4.3).

The bank in Theorem 4.1 is a simultaneous feasible fractional support for
its `4K` distinct upper colours: put weight `1/2` on every circuit column.
It is not claimed here that this partial point extends to a full LP vertex
covering every other upper colour.

## 5. Exact consequence for local rounding

Let `K` role-resource-disjoint circuits be selected.  Inside their combined
support, an integral matching uses at most two columns per circuit, hence
covers at most `2K` of their `4K` colours.  Therefore any integral selection
covering all those colours must use at least

\[
                              2K                                  \tag{5.1}
\]

diamonds outside the fractional support.

With (4.2), the necessary off-support motion is at least

\[
 {U\over32}-O(1)
   ={m-1\over32(m+1)}W-O(1),                                      \tag{5.2}
\]

whereas the residual matching has only

\[
                            C={2W\over m+1}                         \tag{5.3}
\]

slots.  Their ratio is `(m-1)/64+o(1)`.

Consequently no proof that rounds only within fractional support, or that
repairs each fractional circuit using `O(1)` independently charged
residual slots, can yield `B+O(1)` (or even `o(C)` defect).  A positive
Boolean theorem must instead provide a correlated off-support exchange in
which one global alternating packet reorganizes many parity circuits at
once, or it must choose a special fractional point whose support excludes
this circuit bank.

This is the sharp surviving gate.  Equations (5.1)--(5.3) are **not** an
integrality-gap lower bound for the unrestricted Boolean instance: external
diamonds are allowed, and they may globally reroute all colours.

## 6. Audit

The exact finite identities, compatibility graph, restricted matching
number, complete `m=3` LP loads, and active rank are replayed by

* `scratch/audit_threadD_boolean_parity_circuit_cslot_nogo_20260801.py`;
* `scratch/audit_threadD_boolean_parity_circuit_cslot_nogo_20260801.audit.json`.

No SAT solver, floating point, or randomized search is used.
