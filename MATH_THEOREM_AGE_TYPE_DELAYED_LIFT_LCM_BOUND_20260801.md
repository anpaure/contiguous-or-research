# Uniform delayed-lift bound for closed age-type walks

Date: 2026-08-01

Status: unconditional theorem.  It sharpens the exact age-composition
quotient by bounding the period multiplication needed to lift a closed type
walk inside one literal owner.  It does **not** give a one-copy owner lift or
an additive upper bound for the contiguous-OR problem.

## 1. Setup

Fix an owner set `T` of rank `r` and depth `d`.  For an age composition

\[
 c=(c_0,\ldots,c_d),\qquad c_0>0,\qquad \sum_i c_i=r,
\]

let `P_c(T)` be the ordered partitions

\[
 P=(P_0,\ldots,P_d),\qquad
 T=P_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}P_d,
 \qquad |P_i|=c_i.
\]

A type arc `c -> c'` is legal when

\[
                         c'_{i+1}\le c_i
                         \qquad(0\le i<d).
\]

Its literal partition relation is

\[
                         P'_{i+1}\subseteq P_i
                         \qquad(0\le i<d).             \tag{1.1}
\]

Every legal type arc has at least one literal realization, and the relation
is invariant under `Sym(T)`.

For a closed type walk

\[
 c^{(0)}\to c^{(1)}\to\cdots\to c^{(L)}=c^{(0)},
\]

define its delayed-lift multiplier to be the least positive `m` for which
the `m`-fold repetition of the walk has a closed literal partition lift.

## 2. Endpoint permutation lemma

### Lemma 2.1

Let

\[
 P=(P_0,\ldots,P_d),\qquad Q=(Q_0,\ldots,Q_d)
\]

be two ordered partitions of `T` with the same block sizes.  There is a
permutation `sigma in Sym(T)` satisfying

\[
                         \sigma(P_i)=Q_i\quad(0\le i\le d)
\]

whose order divides

\[
                         L_d:=\operatorname{lcm}(1,2,\ldots,d+1). \tag{2.1}
\]

#### Proof

Form the directed multigraph on block labels `0,...,d` having one edge
`i -> j` for every element of `P_i intersect Q_j`.  The outdegree and
indegree of label `i` are both `|P_i|=|Q_i|`.  Hence this labelled-edge
multigraph is Eulerian and its edge set decomposes into directed simple
cycles.  Every such cycle has length at most `d+1`.

For one directed cycle

\[
 i_0\to i_1\to\cdots\to i_{ell-1}\to i_0,
\]

let `x_t in P_(i_t) intersect Q_(i_(t+1))` be its edge element.  Define

\[
                         \sigma(x_t)=x_{t-1}
\]

with indices modulo `ell`.  Then an element leaving `P_i` is sent to an
element entering label `i`, hence to `Q_i`.  Doing this independently on
all edge cycles defines a permutation with `sigma(P_i)=Q_i`.  Its cycles
have lengths at most `d+1`, so its order divides (2.1).  `square`

## 3. Uniform delayed-lift theorem

### Theorem 3.1

Every closed age-composition walk at depth `d` has delayed-lift multiplier
at most

\[
                         \boxed{L_d=\operatorname{lcm}(1,\ldots,d+1)}. \tag{3.1}
\]

The bound is independent of the owner rank `r`, the walk length, and the
compositions appearing in the walk.

#### Proof

Choose an arbitrary literal realization of one tour of the type walk.  It
starts at some partition `P in P_(c^(0))(T)` and ends at some partition
`Q` of the same type.  Lemma 2.1 supplies a permutation `sigma` with

\[
                         \sigma(P)=Q,
                         \qquad \operatorname{ord}(\sigma)\mid L_d.
\]

Apply `sigma` to every literal partition in the first lifted tour.  Since
the relation (1.1) is invariant under coordinate permutations, this is
another legal lift of the same type walk, now from `Q=sigma(P)` to
`sigma(Q)=sigma^2(P)`.  Continue with the `sigma^j` image on tour `j`.
After `ord(sigma)` tours the endpoint is again `P`.  This is a closed
literal lift, and its multiplier divides `L_d`.  `square`

The same proof applies to any closed type walk, not only a simple cycle.

### Exact one-tour criterion

For a fixed closed type walk, let `H` be the composed literal relation on
the ordered partitions of its initial type.  A one-tour literal lift exists
if and only if

\[
                         \boxed{(P,P)\in H\text{ for some }P.}       \tag{3.2}
\]

Equivalently, for some literal realization of one tour, the endpoint
overlap matrix

\[
                         A_{ij}=|P_i\cap Q_j|
\]

is diagonal.  “Permutation-diagonal” is not enough for ordered age states:
a nontrivial permutation of age blocks is a different de Bruijn state.
In the endpoint-permutation language of Lemma 2.1, (3.2) is exactly the
existence of a zero-holonomy realization with `sigma=id`.

### Sharpness at the first depth

At `d=1`, the type self-loop `c=(1,1)` has no one-tour literal loop: the
unique age-one singleton must move into the disjoint age-zero singleton.
Two tours swap the two coordinates back.  Thus multiplier two is sometimes
necessary, matching `L_1=2`.

## 4. A sharp reset lemma and its flat-carrier cost

### Lemma 4.1 (unique-fibre reset)

If a closed type walk contains

\[
                         c_*=(r,0,\ldots,0),                         \tag{4.1}
\]

then it has a one-tour literal lift.

#### Proof

The ordered partition fibre of `c_*` consists of the single state

\[
                         (T,\varnothing,\ldots,\varnothing).
\]

Start the walk there and choose any legal literal successor at every type
arc.  (Every source partition on a nonempty invariant type relation has a
successor by transitivity.)  On returning to type `c_*`, the terminal
literal state is forced to be the same unique partition.  Hence the tour
closes in one pass.  `square`

Leaving the reset imposes

\[
                         c'_2=\cdots=c'_d=0,                         \tag{4.2}
\]

because `c'_(i+1)<=c_(*)_i=0` for `i>=1`.  Positive mass can advance only
one age per transition, so reaching a type with positive oldest class
requires a length-`d` build-up collar.

This is a genuine synchronizer, but it is too expensive in the flat
`D^d A` carrier.  State (4.1) means that one source letter equals the full
rank-`r` owner `T`.  Every one of the next `d+1` length-`(d+1)` owner windows
containing that letter is therefore equal to `T`.  The reset consumes one
owner and creates `d` duplicate central cells.  At physical length
`B(k)+C`, the flat central row has only `C` duplicate-owner slots, so this
reset forces

\[
                         C\ge d.                                    \tag{4.3}
\]

It cannot occur at `B(k)` and cannot support `B(k)+O(1)` as
`d=Theta(sqrt(k))`.

The lower-address disturbance is smaller but still quadratic.  Among the
`d+1` trace windows containing the full letter, a reset at local position
`p` lies in exactly `p` of that trace's `d` proper suffixes.  Hence exactly

\[
                         \sum_{p=0}^d p={d(d+1)\over2}               \tag{4.4}
\]

proper suffix occurrences collapse to the full owner and cannot carry a
strict-lower mark.  The whole collar touches only `O(d^2)` marked addresses,
but (4.3), not (4.4), is the fatal additive-cost row.

Thus the reset lemma is sharp but only potentially useful in a genuinely
nonflat, variable-deadline schedule where one full letter does not demand
`d` additional central-owner occurrences.  No such serialization theorem
is currently proved.

## 5. Reconciliation with the exhaustive audit

The finite audit

```text
scratch/audit_age_composition_literal_lifting_20260801.cpp
```

found no missing or spurious projected type edges in the tested cases and
found that every enumerated simple type cycle lifted after a multiple.
Some cycles did not lift in one tour; all delayed examples in that census
used multiplier two.  Theorem 3.1 proves the general bounded-multiple
statement without relying on that census.  It does not assert that two is
always enough.

## 6. Consequence for the `k=17` connected type certificate

The connected 1430-position age-type Euler word at `d=3` has a closed
literal lift inside one fixed owner after at most

\[
                         L_3=\operatorname{lcm}(1,2,3,4)=12
\]

tours.  Thus connected aggregate type support is enough for a bounded-depth
**repeated-owner** Euler lift.

It is not enough for a one-copy owner factor.  A multiplier `m>1` uses `m`
trace occurrences in the same owner fibre.  Repeating that independently
over all `W` named owners costs `(m-1)W` additional owner occurrences, not
`O(1)`.  Moreover

\[
             L_d=\exp(d+o(d)),
\]

while the relevant depth grows as `d=Theta(sqrt(k))`.  Therefore the bound
does not turn aggregate connected Euler support into
`B(k)+O(1)`.

The exact missing theorem remains a coloured one-copy lift: distribute the
successive literal partition states over distinct named owner orbits while
preserving the owner-transition/Johnson factor, nested marked cells, and
the terminal compiler incidences.  Theorem 3.1 removes only the possibility
of an unbounded-in-`r` obstruction inside one fixed depth/type fibre.

The sharp next lemma is therefore one of the following equivalent-strength
routes:

1. a zero-holonomy one-copy lift of the connected type word across the
   named owner orbits; or
2. a synchronizing state/collar with bounded literal fibre and only `O(1)`
   duplicate central owners in a variable-deadline chronology.

The full-letter reset proves neither route in the flat architecture.
