# The GK primitive--sink rotation bank and the sharp `<1/4` threshold reduction

**Date:** 2026-08-07  
**Status:** unconditional endpoint-bank and exact paired-`C_6` rethread
theorem, followed by a conditional sharp contraction reduction.  The bank
has exact Hall, private socket colours, distinct endpoints and a literal
degree-two alternating circuit.  What remains is its correlated selection
with the standard path cover and the protected non-root state.

## 1. Primitive starts and sink ends

Let

\[
 \mathcal P_m=\{,1A0:A\in D_{m-1}\,\},\qquad
 \mathcal S_m=\{,10B:B\in D_{m-1}\,\}.               \tag{1.1}
\]

These are respectively the indegree-zero and outdegree-zero vertices of
the standard depth-two orientation.  Both sets have size
`Cat_{m-1}`.

For a nonempty Dyck word, write its first-return decomposition as

\[
                         A=1D0E                         \tag{1.2}
\]

and define the standard root rotation

\[
                         \rho(A)=D1E0.                  \tag{1.3}
\]

The map `rho` is a bijection of `D_{m-1}`; in the rooted-plane-tree
interpretation it moves the root corner once around the underlying plane
tree.

## 2. Exact endpoint matching

## Theorem 2.1 (primitive--sink rotation bank)

For every `A in D_{m-1}`, there is a depth-two arc

\[
                         1A0\longrightarrow10\rho(A).  \tag{2.1}
\]

As `A` varies, these arcs form a perfect matching from `P_m` to `S_m`.

### Proof

Put `U=1A0=11D0E0`.  Choose for `b` the second position of `U`, namely
the opener of the first primitive of `A`, and choose for `x` its matching
downstep, the displayed downstep after `D`.  The depth-two flip changes

\[
                         11D0E0\quad\hbox{to}\quad10D1E0,
\]

which is exactly `10 rho(A)`.  Since `rho` is bijective, the sources and
targets in (2.1) are both distinct and exhaust the two shores. \(\square\)

This is stronger than a Hall estimate: the matching is literal and closed
form.

## 3. Exact resource audit

For the socket of (2.1), put

\[
                         a_A=1A0-\{1,b\}.               \tag{3.1}
\]

The global depth-two socket theorem implies that all `a_A` are distinct,
and so are all standard unused colours `B_{y,A}`.  The used full-edge
overlaps are

\[
                         B_{x,A}=X_{10\rho(A)},          \tag{3.2}
\]

which are distinct because the sink targets are distinct.

Now read (2.1) in reverse as the corresponding height-one hinge

\[
                         10\rho(A)\dashrightarrow1A0.  \tag{3.3}

The reverse hinge has the same lower core `a_A`, and its shared target
vertex is

\[
                         B_y^{\rm rev}=a_A+\{b\}=X_{1A0}. \tag{3.4}

Thus the entire reverse bank has

* distinct source roots;
* distinct primitive target roots;
* distinct `a` colours; and
* distinct shared target facets `X_{1A0}`.

There is no endpoint Hall or lower-colour collision in this bank.

Taken in isolation, (3.4) shares only the rank-`(m-1)` vertex with the fixed
root edge.  In the present subfamily, however, the required rethread is
already supplied by the paired-root rotation theorem.  Indeed

\[
 U=11D0E0,
 \qquad
 V=10D1E0                                      \tag{3.5}
\]

are exactly the two roots

\[
 L=1A1B0C0D',\qquad R=1A0B1C0D'
\]

of that theorem with `A=D'=empty`, `B=D` and `C=E`.  Their two endpoint
hinges identify to one alternating incidence `C_6`.  The fixed and cross
edges alternate, both roots are ticketed, and the apparent companion
mismatch at (3.4) is absorbed inside the six-cycle.

Moreover the edges (2.1) form a matching in the root-rotation graph.
Therefore the privacy clause of the paired-root theorem applies
simultaneously to the **entire** primitive--sink bank: all of these `C_6`
circuits are mutually resource-disjoint.

Thus there is no remaining local rethread cost in (3.3).  The remaining
issue is only collision with whatever separate hinges and compiler tickets
are used to build the standard base cover.

## 4. How the bank acts on a standard path cover

Assume a capacity-faithful standard depth-two path cover with the optimal
`Cat_{m-1}` components has been selected.  Every component starts at one
primitive root `1A0` and ends at one sink `10B`.  Therefore its endpoint
relation is a permutation

\[
                         \pi:D_{m-1}\longrightarrow D_{m-1}, \tag{4.1}
\]

where the path starting at `1A0` ends at `10 pi(A)`.

Adding the reverse rotation bank (3.3) joins the end `10 rho(A)` to the
start `1A0`.  On the component index set the resulting 2-regular linkage
has permutation

\[
                         \sigma=\pi^{-1}\rho.           \tag{4.2}

If one reverse edge is omitted from every cycle of `sigma`, the result is
a path forest with exactly

\[
                         c(\pi^{-1}\rho)                \tag{4.3}

components, where `c` denotes number of permutation cycles.

All endpoint and lower-colour capacities, including the degree-two
rethread, are already exact by Section 3.  The only additional hypothesis
needed to make the combined operation physical is simultaneous compatibility
of the selected `C_6`s with the base-cover hinges and their protected
non-root compiler/upper tickets.

## 5. The sharp amount of joining actually required

Let `N=Cat_m` and `C=Cat_{m-1}`.  The standard optimal path cover has `C`
components, while strict four-sector contraction asks for fewer than
`N/4`.  Their difference is

\[
\begin{aligned}
 C-{N\over4}
 &=N\left({m+1\over2(2m-1)}-{1\over4}\right)\\
 &= {3N\over4(2m-1)}.                                  \tag{5.1}
\end{aligned}
\]

Thus it is enough to retain only

\[
                         h_m=\left\lfloor{3N\over4(2m-1)}\right\rfloor+1 \tag{5.2}

acyclic reverse joins between distinct standard components.  This is
`Theta(N/m)`, whereas the available rotation bank has

\[
                         C=\left({1\over4}+O(m^{-1})\right)N             \tag{5.3}

pairwise endpoint-disjoint candidates.  Only an `O(1/m)` fraction of the
bank is needed.

Equivalently, under the full endpoint-permutation formulation it suffices
to arrange

\[
                         c(\pi^{-1}\rho)<{N\over4}.      \tag{5.4}

This is vastly weaker than asking that `pi^{-1}rho` be one cycle.

## 6. Exact remaining theorem

The root-layer threshold is reduced to the following correlated statement.

> **Rotation-bank joint-selection lemma.**  There is an optimal standard
> depth-two path cover and a set of `h_m` edges from the primitive--sink
> rotation bank which join distinct cover components, admit simultaneous
> paired-`C_6` insertion with the base-cover hinges, and preserve the
> protected non-root tickets.

The standard bank supplies the `Cat_{m-1}` base paths.  Theorem 2.1 supplies
far more than the required number of private endpoint joins, and the
paired-root theorem supplies their rethreads.  No scalar, ordinary Hall,
`a`-colour, endpoint-facet or local degree-two obstruction remains.  The
only open content is correlated compatibility with the chosen base cover
and its protected compiler state.
