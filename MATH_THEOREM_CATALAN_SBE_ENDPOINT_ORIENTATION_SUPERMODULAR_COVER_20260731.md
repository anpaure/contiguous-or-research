# Endpoint orientation for strict balanced expansion is a supermodular cover

Date: 2026-07-31  
Status: exact all-parameter reduction and exact fractional separation;
integral orientation and preservation under the direct lift remain open

## 0. Verdict

The strict occurrence graph of a child path forest depends only on its
undirected edges.  Orienting the components does one thing: on each path it
chooses which endpoint is omitted from the tail image and which endpoint is
omitted from the head image.  The strict-balanced-expansion (`SBE`)
condition can therefore be written exactly as a supermodular covering
system on these binary endpoint choices.

For one shore, if `Z` is the selected terminal bank, then

\[
 C|Z\cap A|\ \ge\
 g(A):=N\,|\{o:N_G(o)\subseteq A\}|-R|A|
 \qquad(A\subseteq X).                                      \tag{0.1}
\]

The function `g` is fully supermodular.  Choosing one endpoint from every
nontrivial path is a partition-matroid base constraint.  Thus SBE
orientation is exactly an integral supermodular-cover problem over a
partition base.  The two shores use complementary endpoint choices on
every nontrivial path.

This is a genuine compression: a candidate orientation can be separated by
one submodular-minimization oracle, and the joint upper/lower system is one
coupled binary covering problem.  It is not yet an integrality theorem.
Scaling by `C` is load-bearing; even a one-pair modular example has a
fractionally feasible midpoint and no integral endpoint choice.

## 1. Setup

Fix one strict shore of an undirected Catalan path forest.  Let

\[
                         G=(O,X;E)                         \tag{1.1}
\]

be its occurrence graph.  The outer shore has order `P`, the middle shore
has order `M`, and

\[
 N=|E(F)|,\qquad C=M-P,\qquad R=N-C,\qquad K=M-N.       \tag{1.2}
\]

After orienting every nontrivial child path, let `T` be the image of the
relevant directed endpoints (tails on the upper strict shore, heads on the
lower strict shore), and put

\[
                         Z=X\setminus T.                \tag{1.3}
\]

There is exactly one member of `Z` at the terminal end of each nontrivial
path, while an isolated child vertex belongs to `Z` on both shores.  Hence
`|Z|=K`.

The SBE capacity of a middle set is

\[
 y_Z(x)=
 \begin{cases}
 1,&x\in Z,\\
 R/N,&x\notin Z.
 \end{cases}                                           \tag{1.4}
\]

The shore is SBE exactly when

\[
                  |U|\le y_Z(N_G(U))
                  \qquad(U\subseteq O).                \tag{1.5}
\]

## 2. Closed-neighbourhood duality

For `A subseteq X`, define

\[
                 O(A):=\{o\in O:N_G(o)\subseteq A\}.   \tag{2.1}
\]

### Theorem 2.1 (exact terminal-cover form)

Condition (1.5) is equivalent to (0.1) for every `A subseteq X`.

#### Proof

Assume (1.5).  Apply it to `U=O(A)`.  Since
`N_G(O(A)) subseteq A` and `y_Z` is nonnegative,

\[
 |O(A)|\le y_Z(N_G(O(A)))\le y_Z(A).                  \tag{2.2}
\]

Conversely, assume (2.2) for every `A`.  Given `U subseteq O`, put
`A=N_G(U)`.  Then `U subseteq O(A)`, and therefore

\[
                  |U|\le |O(A)|\le y_Z(A),            \tag{2.3}
\]

which is (1.5).

Finally, since `T=X-Z` and `N=R+C`,

\[
 Ny_Z(A)=R|A|+C|Z\cap A|.                             \tag{2.4}
\]

Multiplying (2.2) by `N` and using (2.4) gives (0.1).
The steps are reversible. `square`

### Lemma 2.2 (supermodularity)

The function

\[
                         g(A)=N|O(A)|-R|A|              \tag{2.5}
\]

is fully supermodular on `2^X`.

#### Proof

For one outer vertex `o`, the indicator

\[
                 h_o(A)={\bf1}_{N_G(o)\subseteq A}     \tag{2.6}
\]

is supermodular.  If its neighbourhood is contained in both sets, it is
also contained in their intersection; if it is contained in exactly one,
it is contained in the union; and if it is split between the two sets, only
the union indicator can become one.  Thus

\[
 h_o(A)+h_o(B)\le h_o(A\cap B)+h_o(A\cup B).           \tag{2.7}
\]

Summing (2.7), multiplying by `N`, and subtracting the modular function
`R|A|` proves the claim. `square`

## 3. The exact endpoint-choice system

Let the endpoint block of a nontrivial child path `P_i` be

\[
                         E_i=\{s_i,t_i\}.              \tag{3.1}
\]

The blocks are disjoint.  Isolated vertices form singleton blocks whose
terminal bit is fixed to one.  Write `z_x=1` when endpoint `x` is selected
for `Z`.

### Theorem 3.1 (one-shore orientation polytope)

An SBE orientation exists on this shore if and only if the following
binary system is feasible:

\[
\begin{aligned}
 z_{s_i}+z_{t_i}&=1 &&\text{for every nontrivial path }i,\\
 z_x&=1 &&\text{for every isolated child vertex }x,\\
 C\sum_{x\in A}z_x&\ge g(A) &&(A\subseteq X),\\
 z_x&\in\{0,1\}.                                      \tag{3.2}
\end{aligned}
\]

For a fixed vector `z`, the most violated row of (3.2) is found by
minimizing the submodular function

\[
                         A\longmapsto C z(A)-g(A).      \tag{3.3}
\]

Hence the fractional relaxation of (3.2) has a polynomial separation
oracle.

#### Proof

The first two rows are exactly the terminal choices induced by component
orientation.  Theorem 2.1 gives the third row.  Conversely every binary
choice in the first two rows orients each nontrivial path toward its chosen
terminal and therefore realizes precisely that `Z`.

By Lemma 2.2, `-g` is submodular; adding the modular function `Cz(A)`
preserves submodularity.  A negative minimum in (3.3) is exactly a violated
row. `square`

### Corollary 3.2 (the two shores are complementary)

Fix a reference orientation on each nontrivial child path and let `z_i=1`
mean that its second endpoint is the upper-shore terminal.  Then its first
endpoint is the lower-shore terminal.  Reversing the path exchanges the two.
Consequently simultaneous upper/lower SBE is one binary system consisting
of the upper rows (3.2) in `z` and the lower rows (3.2) in `1-z`, with the
isolated vertices fixed on both shores.

This coupling is exact.  Solving the shores independently and then trying
to orient the paths need not work.

## 4. Cheap necessary and orientation-free sufficient cuts

For `A subseteq X`, let

\[
 b_{\min}(A)=\#\{i:E_i\subseteq A\}
              +\#\{\text{isolated }x\in A\},          \tag{4.1}
\]

and

\[
 b_{\max}(A)=\#\{i:E_i\cap A\ne\varnothing\}
              +\#\{\text{isolated }x\in A\}.          \tag{4.2}
\]

Every orientation satisfies

\[
                     b_{\min}(A)\le |Z\cap A|
                                      \le b_{\max}(A). \tag{4.3}
\]

Therefore

\[
                    g(A)\le Cb_{\max}(A)              \tag{4.4}
\]

for every `A` is necessary for some SBE orientation, while

\[
                    g(A)\le Cb_{\min}(A)              \tag{4.5}
\]

for every `A` is sufficient for **every** orientation to be SBE.  The same
tests apply simultaneously to the complementary lower-shore system.

These are filters, not a replacement for (3.2): the choices attaining
`b_max(A)` can be incompatible for different sets `A`.

## 5. Why supermodularity alone does not round

It is tempting to intersect the contra-polymatroid in (3.2) with the
partition-base equations and cite generalized-polymatroid integrality.
The scaling by `C` prevents that inference.

Take one endpoint block `E={a,b}`, let `C=2`, and impose the modular (hence
supermodular) demands

\[
                    g(\{a\})=g(\{b\})=1,
                    \qquad g(E)=2.                    \tag{5.1}
\]

Together with `z_a+z_b=1`, the fractional point

\[
                         z_a=z_b=1/2                  \tag{5.2}
\]

is feasible, but neither integral endpoint choice satisfies both singleton
rows.  Equivalently, replacing `g/C` by its pointwise ceiling need not
preserve supermodularity.

Thus (3.2) isolates rather than removes the integral correlation.  A
positive preservation theorem needs an additional Boolean property: for
example a donor exchange which eliminates every straddling row, a jointly
integral submodular-flow representation, or enough strict slack to round
the endpoint choices without crossing zero.

## 6. Consequence for the direct recursion

The authenticated strict chain is SBE on both shores at child parameters
`n=5,6,7`.  Theorem 3.1 shows exactly what must be propagated:

1. the next undirected structural forest must expose endpoint pairs for
   which the coupled upper-`z`/lower-`(1-z)` system is feasible;
2. that orientation then supplies the balanced strict common-basis
   distribution; and
3. physical side representatives still have to meet the degree, graphic,
   attachment and downstream guard rows.

The result does not claim that every recursively supplied forest admits an
SBE orientation, nor that SBE alone supplies the physical representatives.
It replaces the orientation part of balanced DERF by one explicit coupled
supermodular-cover theorem.
