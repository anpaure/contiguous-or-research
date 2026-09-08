# Bounded owner chains serialize exactly by a coloured trace Euler trail

Date: 2026-08-01  
Status: unconditional exact reduction, constructive sufficient conditions,
and sharp boundary-distance obstruction.  This note isolates lower endpoint
serialization.  It does not supply the bounded-chain factor, upper witnesses,
or residence.

## 0. Outcome

Suppose the strict lower ideal has already been partitioned into `W` chains,
each of length at most `d`, and the chains have been assigned to distinct
rank-`r` owners.  Every individual chain can always be clocked inside one
length-`d+1` owner window.  The global ordering problem is exactly this:

> choose one admissible trace edge for every owner-chain so that the selected
> coloured edges become one Euler trail after adding as few uncoloured bridge
> edges as possible.

More precisely, let `Tr_d(T,C)` be the fibre of length-`d+1` nonempty-letter
words whose full union is `T` and whose suffix unions include every member
of `C`.  Regard such a trace as an edge of the order-`d` de Bruijn graph.
If `chi(E)` is the least number of extra de Bruijn edges needed to turn a
selected multiset `E` into one Euler trail, then the exact serialization
overhead is

\[
 \boxed{
  \min_{e_i\in\operatorname{Tr}_d(T_i,C_i)}
                \chi\!\left(\sum_{i=1}^W e_i\right).}       \tag{0.1}
\]

Thus exact depth-`d` serialization is a coloured Euler-transversal theorem,
not merely an ordering of the abstract chains.

There is a useful checkable sufficient condition.  If the selected traces
form directed trail components with terminal/initial state pairs `(v_i,u_i)`
and they can be ordered so that

\[
 \sum_i\bigl(d-\operatorname{ov}(v_i,u_{i+1})\bigr)\le C,   \tag{0.2}
\]

where `ov` is exact suffix--prefix overlap, then the chains serialize in a
word of length `W+d+C`.

This identifies a sharp obstruction to an `O(1)` boundary sidecar.  A
constant number of components does not suffice: generic endpoint states cost
`d` letters to reset.  Additive-constant serialization requires total
overlap deficit `O(1)`, or an equivalent connected near-Euler selection.

The result is complementary to
`MATH_THEOREM_ORDERED_ORTHOGONAL_CHAIN_BAND_EMBEDDING_20260731.md`.
That theorem starts with both endpoint chain partitions and tests precedence,
bandwidth and pins.  Here only the right-endpoint owner chains are given; the
missing orthogonal partition is generated implicitly by a selected trace
Euler trail.

## 1. Every bounded owner-chain has an admissible trace

Let

\[
 C=(S_1\subsetneq S_2\subsetneq\cdots\subsetneq S_\ell),
 \qquad \ell\le d,\qquad S_\ell\subsetneq T,                 \tag{1.1}
\]

where `T` is a nonempty rank-`r` owner.  The case `ell=0` is allowed.

An **admissible depth-`d` trace** for `(T,C)` is a tuple of nonempty sets

\[
                    e=(B_0,B_1,\ldots,B_d)                   \tag{1.2}
\]

such that

\[
 \bigcup_{h=0}^d B_h=T                                      \tag{1.3}
\]

and every `S_j` is the union of a suffix of (1.2) of length at most `d`.
Write `Tr_d(T,C)` for the collection of all such traces.

### Lemma 1.1 (canonical consecutive clock)

For every `(T,C)` satisfying (1.1), `Tr_d(T,C)` is nonempty.  One may place
`S_j` at suffix length `j` for every `1<=j<=ell`.

#### Proof

Put `S_0=emptyset`, choose `x in S_1` when `ell>0`, and set

\[
 B_{d-j+1}=S_j\setminus S_{j-1}qquad(1\le j\le\ell).       \tag{1.4}
\]

The displayed letters are nonempty because the chain is strict, and their
last `j` unions are exactly `S_j`.  Set every still-unassigned position to
`{x}`, except put

\[
 B_0=(T\setminus S_\ell)\cup\{x\}.                          \tag{1.5}
\]

This is nonempty, changes none of the displayed suffixes, and makes the full
union `T`.  If `ell=0`, choose `x in T`, put `B_0=T`, and put `{x}` in all
other positions. \(\square\)

The lemma is deliberately permissive: source letters may be arbitrary
nonempty subsets.  Restricting them to singletons, fixed ranks, or prescribed
coordinate roles is an additional construction choice.

## 2. The trace de Bruijn graph

Let

\[
                   \mathcal A=2^{[k]}\setminus\{\varnothing\}.             \tag{2.1}
\]

The order-`d` de Bruijn digraph `D_d(A)` has vertex set `A^d`.  Every word

\[
                       (B_0,\ldots,B_d)                    \tag{2.2}

is an edge from

\[
 (B_0,\ldots,B_{d-1})\quad\hbox{to}\quad(B_1,\ldots,B_d).  \tag{2.3}
\]

Trace edges may repeat as literal words; occurrences remain separately
labelled by their owner-chain colours.

Let the given owner-chain factor be

\[
                       (T_i,C_i),\qquad1\le i\le W.          \tag{2.4}
\]

A **trace selection** chooses one coloured edge

\[
                       e_i\in\operatorname{Tr}_d(T_i,C_i)   \tag{2.5}
\]

for every `i`.

## 3. Exact serialization theorem

For a nonnegative integral edge multiset `z` on `D_d(A)`, let `chi(z)` be
the minimum of `sum_e b_e` over all nonnegative integral bridge multisets
`b` for which:

1. the positive support of `z+b` is weakly connected; and
2. for some vertices `s,t`,

   \[
    \operatorname{out}_{z+b}(v)-\operatorname{in}_{z+b}(v)
       =\mathbf1_{v=s}-\mathbf1_{v=t}.                       \tag{3.1}
   \]

The case `s=t` is an Euler circuit.  Euler's theorem says that `z+b` then
has one directed Euler trail.

### Theorem 3.1 (coloured trace-Euler equivalence)

For an integer `C>=0`, the following are equivalent.

1. There is a word `A_1,...,A_(W+d+C)` and an injection assigning every
   owner-chain `(T_i,C_i)` to a distinct length-`d+1` window whose full union
   is `T_i` and whose suffix unions contain `C_i`.
2. There is a trace selection `(e_i)` such that

   \[
                       \chi\left(\sum_i e_i\right)\le C.     \tag{3.2}
   \]

Consequently the minimum serialization overhead is exactly (0.1).

#### Proof

Assume 1.  The word has exactly `W+C` consecutive length-`d+1` windows.
The `W` assigned windows give the selected coloured traces; the remaining
`C` windows give `b`.  Consecutive windows overlap in exactly `d` letters,
so all `W+C` windows form one de Bruijn trail.  Therefore (3.1) and connected
support hold.

Conversely, take an Euler trail of `z+b`.  Write the `d` letters of its
initial vertex and then append the last letter of every traversed edge.  This
spells a word of length `d+W+sum b_e`.  Each selected coloured edge occurs as
its exact length-`d+1` trace window and hence realizes its owner-chain.
Unused bridge windows are harmless.  If `sum b_e<C`, append arbitrary
nonempty letters at the end; existing witnesses remain. \(\square\)

At `C=0`, this says exactly that one trace per chain must form one connected
Euler trail.  Flow balance without connected support gives a collection of
separate words, not one word.

### Corollary 3.2 (one coloured circulation is sufficient)

Introduce binary variables `x_(i,e)` for `e in Tr_d(T_i,C_i)`.  Exact
serialization at length `W+d` follows if

\[
 \sum_{e\in\operatorname{Tr}_d(T_i,C_i)}x_{i,e}=1
       \qquad(1\le i\le W),                                  \tag{3.3}
\]

the selected arc vector

\[
                            z_e=\sum_i x_{i,e}                \tag{3.4}
\]

satisfies (3.1), and its positive support is weakly connected.  Conversely,
every exact serialization gives such an integral solution.  Connectedness
may be imposed by the standard directed-support cut inequalities.

Thus the independent serialization target is one **coloured integral
circulation with one arc per owner-chain**.  The colour equations coupled to
de Bruijn incidence are the remaining integrality; separately choosing one
trace per chain or merely balancing the aggregate trace marginals is not
enough.

## 4. Exact boundary distance and a practical sufficient condition

For two de Bruijn states

\[
 u=(U_1,\ldots,U_d),\qquad v=(V_1,\ldots,V_d),               \tag{4.1}
\]

define

\[
 \operatorname{ov}(u,v)=\max\{q:
       (U_{d-q+1},\ldots,U_d)=(V_1,\ldots,V_q)\}.            \tag{4.2}
\]

The empty overlap `q=0` is allowed.

### Lemma 4.1 (sharp reset distance)

The shortest directed walk from `u` to `v` in the full de Bruijn graph has
length

\[
                   \operatorname{dist}(u,v)
                     =d-\operatorname{ov}(u,v).              \tag{4.3}
\]

#### Proof

After `c<=d` shifts, the last `d-c` letters of the old state remain and must
equal the first `d-c` letters of the new state.  Hence
`c>=d-ov(u,v)`.  Equality is attained by appending precisely the final
`d-ov(u,v)` letters of `v`. \(\square\)

Now suppose the selected trace edges have been decomposed into directed
trails `P_1,...,P_c`, where `P_i` starts at `u_i` and ends at `v_i`.

### Corollary 4.2 (overlap-splice theorem)

For every ordering `pi` of the trail components, the owner chains serialize
with overhead

\[
 \sum_{j=1}^{c-1}
       \left(d-\operatorname{ov}(v_{\pi(j)},u_{\pi(j+1)})\right).          \tag{4.4}
\]

In particular, (0.2) is a sufficient condition for overhead at most `C`.

#### Proof

Between consecutive component trails insert a shortest walk from Lemma 4.1,
then take the Euler trail inside the next component.  The inserted walk
contributes exactly the stated number of uncoloured windows.  Apply Theorem
3.1. \(\square\)

This is the precise boundary-sidecar ledger.  Merely proving `c=O(1)` gives
only `O(d)` overhead in general.  Since `d=Theta(sqrt(k))`, an additive
constant requires the component ends to have total overlap deficit `O(1)`.

## 5. Immediate exact lower bounds

For a selected edge multiset `z`, put

\[
 P(z)=\sum_v\bigl(\operatorname{out}_z(v)-
                         \operatorname{in}_z(v)\bigr)_+      \tag{5.1}
\]

and let `c(z)` be the number of weak components of its positive support.

### Proposition 5.1 (imbalance and component cuts)

\[
                     \chi(z)\ge P(z)-1,
 \qquad               \chi(z)\ge c(z)-1.                   \tag{5.2}
\]

#### Proof

One added edge changes the positive imbalance mass by at most one, while one
Euler trail has positive imbalance mass at most one.  This proves the first
bound.  One new edge can merge at most two existing weak components, proving
the second. \(\square\)

The bounds are often weaker than the state-distance cost (4.4): two
components may have balanced degrees and still be distance `d` apart.

## 6. Sharp local obstruction: full-depth disjoint traces cost `d`

Take any `k=2r` with `1<=d<r`, and split the coordinates into disjoint
rank-`r` owners

\[
 T_X=\{x_1,\ldots,x_r\},\qquad
 T_Y=\{y_1,\ldots,y_r\}.                                   \tag{6.1}
\]

Give them the full-depth lower chains

\[
 S_j^X=\{x_1,\ldots,x_j\},\qquad
 S_j^Y=\{y_1,\ldots,y_j\},qquad1\le j\le d.               \tag{6.2}
\]

Because each chain has `d` strict members and only `d` legal suffix lengths,
its clock is forced.  Every admissible `X`-trace therefore has

\[
 (B_1,\ldots,B_d)=(\{x_d\},\{x_{d-1}\},\ldots,\{x_1\}),   \tag{6.3}
\]

and every one of its letters is a nonempty subset of `T_X`.  The analogous
statement holds with `Y`.

Since `T_X` and `T_Y` are disjoint, no nonempty `X`-letter equals a nonempty
`Y`-letter.  Thus every suffix--prefix overlap between an `X` endpoint state
and a `Y` endpoint state has length zero.  Lemma 4.1 gives distance exactly
`d` in either direction.

Hence these two bounded owner-chains, considered as two required trace
components, need exactly `d` bridge letters.  This is not a counterexample
to a full lower-ideal factor—other chain traces might bridge them—but it is a
sharp proof that bounded chain length, distinct owners and individual
clockability alone imply no `O(1)` serialization sidecar.

## 7. Relation to orthogonal chains and move-to-front states

Every serialized trace word automatically induces the missing left-endpoint
chain partition: group assigned target intervals by their left endpoints.
The two endpoint partitions are orthogonal, their precedence orders are the
physical orders, and the band condition is automatic.  Thus Theorem 3.1 is
an alternative to first guessing an orthogonal mate and then applying the
ordered-orthogonal-chain theorem.

Conversely, an ordered orthogonal embedding which passes pin survival
produces a literal word and therefore a trace-Euler certificate.  The two
interfaces are equivalent after all interval addresses are fixed, but their
existence hypotheses differ:

* orthogonal chains expose precedence cycles and bandwidth before letters;
* trace Euler exposes memory balance, components and boundary reset cost
  before the second chain partition.

The move-to-front formulation is the coordinatewise quotient of the same
word.  A suffix-OR chain is a subchain of the prefix unions of the current
last-occurrence ordered partition; appending one source letter performs the
corresponding move-to-front update.  The trace formulation retains exactly
`d` literal source letters, which is the memory needed to certify the owner
window and gives the sharp additive cost (4.3).

## 8. Strongest isolated serialization target

The lower-compiler problem may now be separated into two independent-looking
but correlated theorems.

1. **Integral chain factor:** choose the `W` owner-chains.  Its exact defect
   is `gamma_d` from
   `MATH_THEOREM_IDEAL_SDR_TO_ENDPOINT_CHAIN_COCYCLE_AND_UNCROSSING_GATE_20260801.md`.
2. **Coloured near-Euler trace selection:** choose one edge from every
   `Tr_d(T_i,C_i)` so that `chi=O(1)`—or `chi=0` for exact coefficient one.

The second statement is strictly weaker than the full OR construction: it
does not ask for upper targets, Johnson topology, or residence.  It is also
stronger than ordering the chains or balancing rank marginals.  Its exact
certificates are:

\[
 \boxed{
 \text{one edge per colour}\;|\;
 \text{de Bruijn boundary balance}\;|\;
 \text{connected support}\;|\;
 \text{overlap-deficit }O(1).}
\]

This is the natural target for an independent endpoint-serialization proof.
