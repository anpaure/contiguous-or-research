# Cubic flag trades preserve rail histograms: an exact obstruction to post-hoc common rounding

**Date:** 2026-08-01  
**Lane:** K, protected multi-order common rounding  
**Status:** unconditional structural theorem and sharply scoped no-go.  The
all-depth Johnson-triangle trade preserves every named suffix-row multiset,
but it also preserves the coordinate histogram in every deletion position.
Consequently it cannot repair a positional rail imbalance.  At depth three
it preserves the complete de Bruijn rail-divergence vector.  Thus the cubic
absorber is not, by itself, a Markov basis for converting an arbitrary exact
SCD selector into a legal chronology.  Positively, at depth three two
oppositely toggled cubes on one common core give an exact refined-circulation
packet; basewise owner transparency then forces three explicit companion
head rectangles.  This does **not** disprove existence of a prospectively
chosen balanced selector, nor does it address
connectivity, voltage, residence, upper shadows, or the terminal compiler.

## 0. Verdict

Let a depth-\(d\) rooted flag be

\[
             f=(q;z_1,z_2,\ldots,z_{d-1}),
\qquad q\in\binom{[2m+1]}m .                         \tag{0.1}
\]

For a table \({\cal F}\) containing one flag at every root, put

\[
 H_j^{\cal F}(x)=
   |\{f\in{\cal F}:z_j(f)=x\}|,
 \qquad 1\le j<d, x\in[2m+1].                      \tag{0.2}
\]

The following facts are exact.

1. Rail balance implies

   \[
                  H_1^{\cal F}=H_2^{\cal F}=\cdots
                       =H_{d-1}^{\cal F}.             \tag{0.3}
   \]

2. Every all-depth cubic Johnson-triangle trade preserves every vector
   \(H_j^{\cal F}\) separately.
3. When \(d=3\), the vectors \(H_1,H_2\) are the complete prefix and suffix
   state counts.  Hence a cubic trade preserves the **entire** rail
   divergence.  A depth-three exact selector with nonzero divergence can
   never be made chronological by any sequence of cubic trades.
4. For \(d\ge4\), a cubic trade keeps the suffix-state multiset fixed and
   performs a six-cell circulation only in the prefix-state table.  It can
   repair higher-order correlations only inside the fixed positional
   marginals (0.2).
5. The refined overlap-core circulation is stricter than rail balance.  A
   single cube never preserves it.  At $d=3$, an opposite pair of cubes
   sharing one core does preserve its Euler boundary exactly; preserving
   owner colours in the basewise face additionally requires three companion
   head rectangles.
6. At \(d=4\), one free physical root orbit with only two literal flag
   choices per root has a unique half-integral rail-balanced point and no
   integral point.  Thus the colourful circulation gap is physical, not an
   artefact of quotienting, although it remains a restricted-atlas
   obstruction rather than an all-Boolean no-go.

The standard recursive SCD table at \((2m+1,m,d)=(7,3,3)\) has exact marked
suffix coverage but rail-divergence norm \(24\).  It is therefore an exact
finite witness that

\[
 \boxed{\text{exact SCD selector} + \text{post-hoc cubic absorption}}
\]

does not imply common integral chronology.  The stationary pull-clock
circulation has zero positional flux fractionally, so the remaining theorem
must choose the integral selector **prospectively in that zero-flux fibre**,
or use a genuinely basis-changing move with nonzero positional flux.

## 1. Rail balance forces equality of all positional histograms

Write

\[
 \partial^-f=(z_1,\ldots,z_{d-2}),\qquad
 \partial^+f=(z_2,\ldots,z_{d-1}).                  \tag{1.1}
\]

Let

\[
 A_{\cal F}(w)=|\{f:\partial^-f=w\}|,\qquad
 B_{\cal F}(w)=|\{f:\partial^+f=w\}|.              \tag{1.2}
\]

The exact rail equation is

\[
                         A_{\cal F}(w)=B_{\cal F}(w)
                         \quad\hbox{for every }w.     \tag{1.3}
\]

### Lemma 1.1 (positional-flux necessity)

Equation (1.3) implies (0.3).  Equivalently, every vector

\[
             \Phi_j^{\cal F}:=H_j^{\cal F}-H_{j+1}^{\cal F},
             \qquad 1\le j<d-1,                     \tag{1.4}
\]

must vanish.

#### Proof

Fix \(j<d-1\) and a coordinate \(x\).  Sum (1.3) over all words whose
\(j\)-th entry is \(x\).  On the prefix side this counts flags with
\(z_j=x\), namely \(H_j^{\cal F}(x)\).  On the suffix side the same word
position is occupied by \(z_{j+1}\), so it counts
\(H_{j+1}^{\cal F}(x)\).  Hence the two are equal.  This holds for every
\(j,x\). \(\square\)

For \(d=3\), the rail states have length one.  Therefore

\[
 A_{\cal F}(x)=H_1^{\cal F}(x),\qquad
 B_{\cal F}(x)=H_2^{\cal F}(x),                       \tag{1.5}
\]

and (0.3) is not merely necessary but exactly the rail-balance equation.

There is a useful exact construction showing that positional zero flux by
itself is easy.  Identify the ground set with \(\mathbb Z_{2m+1}\), and let
\(\tau\) be translation by one.

### Theorem 1.2 (cyclic zero-flux flag table)

The translation action on the rank-\(m\) roots is free.  Choose one root
representative from every translation orbit and choose an arbitrary ordered
\((d-1)\)-tuple of distinct elements in that representative.  Translate
the rooted flag around its complete orbit.  The resulting table has one
flag at every root and satisfies

\[
                  H_j(x)=\frac1{2m+1}\binom{2m+1}m
                        =\operatorname{Cat}_m                 \tag{1.6}
\]

for every deletion position \(j\) and every coordinate \(x\).  In
particular all positional fluxes vanish integrally.

An arbitrary prepared bank can be retained by this construction exactly
when prescribed flags lying in the same root orbit are translates of one
another.  In particular any prepared bank meeting each root orbit at most
once is admissible.

#### Proof

If a nonidentity translation \(\tau^t\) fixes a rank-\(m\) root, that root
is a union of orbits of the subgroup generated by \(t\).  Every such orbit
has one common length \(s>1\), with \(s\mid 2m+1\), so \(s\mid m\).  This
contradicts \(\gcd(2m+1,m)=1\).  Thus every root orbit has size \(2m+1\),
and their number is

\[
 \frac1{2m+1}\binom{2m+1}m
 =\frac1{m+1}\binom{2m}m=\operatorname{Cat}_m.       \tag{1.7}
\]

Within one root orbit, a fixed deleted letter in position \(j\) runs once
through every coordinate as the flag is translated.  Hence that orbit
contributes one to every \(H_j(x)\).  Summing over the
\(\operatorname{Cat}_m\) root orbits proves (1.6).  A prescribed flag fixes
the translated choice on its whole orbit, so two prescriptions on one
orbit are compatible exactly under the stated translate condition.
\(\square\)

Theorem 1.2 does **not** cover the named suffix targets and does not imply
the full word-state equation (1.3) when \(d\ge4\).  Its role is precise:
the first linear chronology projection has an unconditional integral
solution, but its intersection with the SCD target-cover polytope remains
the common-rounding problem.

The cyclic construction is not the only proof of integral zero flux.

### Theorem 1.3 (equitable deletion-order factorization)

There is a full ordering

\[
                    q=(z_1(q),\ldots,z_m(q))                  \tag{1.8}
\]

of every rank-\(m\) root such that, for every position \(j\) and coordinate
\(x\), exactly \(\operatorname{Cat}_m\) roots have \(z_j(q)=x\).

#### Proof

Form the bipartite incidence graph between all rank-\(m\) roots and the
\(2m+1\) coordinates.  Its left degree is \(m\).  The degree of every
coordinate is

\[
             \binom{2m}{m-1}=m\operatorname{Cat}_m.           \tag{1.9}
\]

For each coordinate, partition its incident edges arbitrarily into
\(\operatorname{Cat}_m\) groups of size \(m\), and split the coordinate
vertex into one clone for every group.  The resulting bipartite graph has

\[
      \binom{2m+1}m=(2m+1)\operatorname{Cat}_m
\]

vertices on each shore and is \(m\)-regular.  By the bipartite
one-factorization theorem, its edges split into \(m\) perfect matchings.
Use matching \(j\) as deletion position \(j\).  At a root the \(m\)
matchings use its \(m\) distinct incidence edges, so they order all elements
of the root.  Every matching hits every clone once, and hence hits every
original coordinate exactly \(\operatorname{Cat}_m\) times. \(\square\)

The theorem is again unprotected.  Prescribing complete prefixes turns its
proof into a partial one-factorization extension problem; arbitrary partial
edge-colourings of regular bipartite graphs do not extend for free.  This is
another exact location at which the bounded prepared bank must be coupled
to the construction rather than inserted afterward.

There is an exact quotient formulation of that next projection.  An
ordered \((d-2)\)-word has a free translation orbit.  For each free root
orbit \(c\), every equivariant flag choice is a directed arc

\[
       [\partial^-f]\longrightarrow[\partial^+f]              \tag{1.10}
\]

between translation orbits of rail states, coloured by \(c\).  Choosing
one equivariant flag orbit for each root orbit is rail-balanced exactly when
the selected coloured arcs form an Eulerian directed multigraph.

### Proposition 1.4 (smallest colourful-circulation obstruction)

The colourful rail-circulation polytope is not integral, already for one
root-orbit colour and two rail states.  This obstruction occurs in the
literal Boolean flag host for every \(m\ge4\) at depth \(d=4\).

#### Proof

Work in \(\mathbb Z_{2m+1}\).  Choose a rank-\(m\) root \(q\) containing
\(0,1,2,3\), and restrict its root-orbit colour to the two equivariant flag
orbits generated by

\[
                   f=(q;0,1,3),\qquad g=(q;0,2,3).             \tag{1.11}
\]

Translation orbits of ordered pairs are indexed by their directed
difference.  Hence $f$ gives the rail arc

\[
                           1\longrightarrow2,
\]

while $g$ gives $2\longrightarrow1$.  If their selection variables are
\(x,y\), the one-colour equation and state balance are

\[
                          x+y=1,\qquad x-y=0.                  \tag{1.12}
\]

The unique solution is $x=y=1/2$; no zero-one solution exists.  The
coefficient matrix has determinant $-2$. \(\square\)

This is an exact restricted-atlas/residual obstruction, not a no-go for the
complete Boolean atlas: other choices of the same colour, or arcs from
other colours, can repair it.  It proves that a fractional pull-clock
circulation cannot be rounded by invoking ordinary network-flow
integrality after the one-per-root-orbit equations are added.  A correlated
absorber must explicitly eliminate such isolated bidirected colour blocks.
Notice that each of the two integral equivariant flag orbits separately has
the uniform positional histograms (1.6).  Thus the example also proves that
zero positional flux is strictly weaker than full word-state balance once
$d\ge4$.

The quotient obstruction is not an artefact of forcing one common choice
around the orbit.

### Corollary 1.5 (physical two-option orbit face)

For \(t\in\mathbb Z_{2m+1}\), put \(q_t=q+t\) and allow the root \(q_t\)
exactly the two flags

\[
 f_t=(q_t;t,t+1,t+3),\qquad
 g_t=(q_t;t,t+2,t+3).                                      \tag{1.13}
\]

Even when the choice is made independently at every physical root \(q_t\),
the one-per-root and literal rail-balance equations have the unique
fractional solution

\[
                         x_t=y_t=\frac12
                         \qquad(t\in\mathbb Z_{2m+1}),        \tag{1.14}
\]

and have no zero-one solution.

#### Proof

Write

\[
 P_t=(t,t+1),\qquad Q_t=(t,t+2).
\]

The flag \(f_t\) has rail arc \(P_t\to Q_{t+1}\), while \(g_t\) has
rail arc \(Q_t\to P_{t+2}\).  If their selected weights are \(x_t,y_t\),
then one choice at root \(q_t\) and balance at the two physical rail states
give

\[
 x_t+y_t=1,\qquad x_t=y_{t-2},\qquad y_t=x_{t-1}.             \tag{1.15}
\]

Thus \(x_t=x_{t-3}\) and \(x_t+x_{t-1}=1\).  Applying these identities at
three consecutive indices gives \(x_{t+1}=x_{t+2}\) and
\(2x_{t+1}=1\).  Hence every \(x_t\), and then every \(y_t\), equals
\(1/2\).  In particular no integral selection exists. \(\square\)

This remains a restricted flag atlas on one free root orbit.  It is not a
no-go for the complete Boolean atlas or for a prospectively co-designed
SCD selector.  It does prove that exact physical root rows plus exact
physical rail rows are already nonintegral; quotient symmetry is not the
source of the gap.

Indeed the complete host contains the missing diagonal orbit

\[
                         h_t=(q_t;t,t+1,t+2).                  \tag{1.16}
\]

Its rail arcs \(P_t\to P_{t+1}\) form an integral directed cycle.  Thus the
two-option obstruction is closed precisely by a physically admissible
diagonal/absorber column.  This is the literal model of the general common
rounding gate: fractional feasibility does not show that the required
diagonal survives the protected turn structural zeros.

## 2. Exact boundary action of the all-depth cubic trade

Use the notation of the all-depth Johnson-triangle trade.  Thus

\[
 R_i=Q-\{u_i\}+\{x_i\},\qquad i\in\mathbb Z_3,       \tag{2.1}
\]

and let \(W=(w_3,\ldots,w_{d-1})\).  Reindex both phases by the common root
\(R_i\).  The old and new flags at that root are

\[
 \begin{aligned}
 f_i^-&=(R_i;x_i,u_{i+1},w_3,\ldots,w_{d-1}),\\
 f_i^+&=(R_i;x_i,u_{i-1},w_3,\ldots,w_{d-1}).
 \end{aligned}                                                \tag{2.2}
\]

This is just the reindexing \(f_i^+=f_{i-1}^1\) of the standard displayed
trade.  It makes the chronology action transparent.

### Theorem 2.1 (cubic positional-histogram invariant)

Replacing \(\{f_i^-:i\in\mathbb Z_3\}\) by
\(\{f_i^+:i\in\mathbb Z_3\}\) preserves

\[
                         H_j(x)\quad
             \hbox{for every }1\le j<d\hbox{ and every }x.   \tag{2.3}
\]

Consequently every positional-flux vector \(\Phi_j\) in (1.4) is invariant
under an arbitrary sequence of all-depth cubic trades.

#### Proof

At position one the three entries are \(x_0,x_1,x_2\) in both phases.  At
position two the old entries are \(u_1,u_2,u_0\), while the new entries are
\(u_2,u_0,u_1\); these are the same multiset.  At each later position all
three flags use the same \(w_j\) in both phases.  This proves (2.3), and
(1.4) then gives the last assertion. \(\square\)

The theorem is stronger than all-depth target neutrality.  Equality of the
named suffix-row multisets does not formally imply equality of the deleted
letter at each position; formula (2.2) proves that extra invariant.

### Theorem 2.2 (exact rail-boundary action)

The suffix-state multiset is unchanged at every depth:

\[
 \{(u_{i+1},w_3,\ldots,w_{d-1}):i\in\mathbb Z_3\}
 =
 \{(u_{i-1},w_3,\ldots,w_{d-1}):i\in\mathbb Z_3\}.   \tag{2.4}
\]

For \(d=3\), the prefix-state multiset is also unchanged, so the complete
rail-divergence vector is invariant.  For \(d\ge4\), the prefix counter
changes by exactly

\[
 \sum_{i\in\mathbb Z_3}
 \left(
  {\bf e}_{(x_i,u_{i-1},w_3,\ldots,w_{d-2})}
 -{\bf e}_{(x_i,u_{i+1},w_3,\ldots,w_{d-2})}
 \right).                                                   \tag{2.5}
\]

Thus the move is a six-cell circulation in the \(z_1\)-versus-\(z_2\)
prefix contingency table, inside one fixed continuation fibre.

#### Proof

Take prefixes and suffixes of (2.2).  Equation (2.4) follows because
\(i\mapsto i+1\) and \(i\mapsto i-1\) both permute \(\mathbb Z_3\).
For \(d=3\), a prefix is the singleton \(x_i\), unchanged rootwise.  For
\(d\ge4\), subtraction of the two prefix counters is precisely (2.5).
\(\square\)

### Corollary 2.3 (one cubic trade is never chronology-neutral for $d\ge4$)

For $d\ge4$, the six ordered prefix states in (2.5) are distinct.  Hence
the rail-boundary change has exact norm

\[
                       \|\Delta(A-B)\|_1=6.                  \tag{2.6}
\]

In particular, applying one cubic trade to a rail-balanced table makes it
unbalanced.  A chronology-preserving use of cubic trades at higher depth
must be a **signed packet** whose prefix-boundary vectors (2.5) cancel
exactly.

#### Proof

States belonging to different indices $i$ have different first entry
$x_i$.  For fixed $i$, the positive and negative states have distinct
second entries $u_{i-1}\ne u_{i+1}$.  Thus no cancellation occurs inside
(2.5), giving three coefficients $+1$, three coefficients $-1$, and
(2.6).  Equation (2.4) says the suffix counter contributes no change.
$\square$

This exposes an extra condition absent from resource-disjoint absorber
packing.  Physical row-disjointness does not itself cancel ordered rail
states.  A usable higher-depth absorber bank must therefore satisfy both

\[
 \text{resource disjointness}
 \quad\text{and}\quad
 \sum_{A\text{ selected}}\Delta_{\rm rail}(A)=0.             \tag{2.7}
\]

The second equation may deliberately require different absorbers to share
ordered coordinate words even though their physical set rows remain
distinct.  It is not supplied by the existing list-to-conflict count.

The minimum such packet can be classified exactly.  For one cubic trade
write its prefix signature as

\[
 \Sigma(T)=
 \left(V;\{(x_i;u_{i-1},u_{i+1}):i\in\mathbb Z_3\}\right),
 \qquad V=(w_3,\ldots,w_{d-2}),                              \tag{2.8}
\]

where the ordered pair after $x_i$ lists its positive and negative
second entries in (2.5).

### Theorem 2.4 (minimal aligned two-cube rail closure)

One cubic trade cannot be rail-neutral at depth \(d\ge4\).  Two cubic
trades \(T,T'\) satisfy

\[
                       \Delta_{\rm rail}(T')
                       =-\Delta_{\rm rail}(T)                 \tag{2.9}
\]

if and only if, after reindexing their three rows, they have the same
continuation \(V\), the same three first labels, and at each first label the
positive and negative second labels are interchanged.  Equivalently,
\(\Sigma(T')\) is the pointwise orientation reversal of \(\Sigma(T)\).

#### Proof

Sufficiency is immediate from (2.5).  Conversely, Corollary 2.3 says each
boundary vector has six distinct supported states.  Equality (2.9) forces
equality of their supports with signs reversed.  Equality of ordered states
forces equality of the continuation \(V\) and of the first entry \(x\);
for each such \(x\), its unique positive and negative second entries must
therefore be interchanged. \(\square\)

The two cubes may still be physically nonidentical: their ambient cores,
roots, exterior labels, and final deletion letter \(w_{d-1}\) are invisible
to the prefix signature (2.8).  Thus Theorem 2.4 supplies a concrete
constructive target rather than only a no-go:

\[
 \boxed{\text{pair two physically disjoint cubes on one inverse rail
 signature, then use their remaining degrees of freedom for Hall/owner
 repair}.}                                                   \tag{2.10}
\]

Whether the Boolean carrier supplies enough such inverse-prefix pairs with
turn-safe diagonals is the first local cubic-absorber existence question.

### Corollary 2.5 (bounded common interface of an aligned pair)

Apply an aligned inverse-prefix pair to an exact rail-balanced flag table,
and assume its two cubes involve at most six roots in total.  Then:

1. every named suffix-row multiset is unchanged;
2. rail balance is unchanged;
3. after deleting the six changed roots from both the tail and head copies,
   the old and new unions of overlap-state graphs are identical; hence

   \[
       |\nu_{\rm state}(F')-\nu_{\rm state}(F)|\le12;         \tag{2.11}
   \]

4. after the same deletion, the old and new tail/head/owner turn
   hypergraphs are identical, so their three-partite matching numbers
   differ by at most (12).

#### Proof

The first assertion is the all-depth cubic identity applied twice.  The
second is (2.9).  A legal turn between two unchanged flags is determined by
those two flags, so it is unchanged.  Therefore every changed edge of the
statewise graph is incident with a changed root on at least one shore.
Deleting the six changed vertices on each shore leaves a common bipartite
graph.  Restricting a maximum matching to that common graph loses at most
twelve edges (six through the changed tail shore and six more through the
changed head shore), in either direction, proving (2.11).

The same argument applies to the tripartite turn hypergraph.  A matching
can use at most six atoms through the changed tail set and at most six
additional atoms through the changed head set.  Restriction therefore
loses at most twelve atoms in either direction. \(\square\)

Thus the aligned pair is a genuine finite **candidate** common-rounding
move: it stays in the exact static and coarse rail-balanced fibre while
changing only a bounded Hall/owner interface.  It need not preserve the
refined bottom-core flow described next.  What remains unproved is a
Boolean supply theorem saying that every nonzero Dulmage--Mendelsohn shore
admits a refined-transparent aligned packet whose finite interface is
augmenting.

### 2.6 The refined overlap-core boundary is strictly stronger

The exact overlap-core flow theorem associates to a flag $f$ and a
chosen routing letter \(\beta\in B(f)\) the directed arc

\[
 I(f,\beta)=
 \bigl((z_1,\ldots,z_{d-2}),
       (B(f)-\{\beta\})\cup\{z_{d-1}\}\bigr)
 \longrightarrow
 O(f)=\bigl((z_2,\ldots,z_{d-1}),B(f)\bigr).         \tag{2.12}
\]

Choosing one such arc per root closes all uncoloured overlap-state
matchings exactly when their directed boundary is zero, together with the
single degree-one no-loop guard.  Therefore coarse prefix/suffix balance is
only the projection obtained by forgetting the core coordinate in (2.12).

For one cubic trade at depth \(d\ge4\), put

\[
 U=\{u_0,u_1,u_2\},\quad
 W=(w_3,\ldots,w_{d-1})=(V,\gamma),\quad
 C=Q-(U\cup W).                                      \tag{2.13}
\]

Using the phases in (2.2), their bottom cores and outgoing nodes are

\[
 \begin{aligned}
 B_i^-&=C\cup\{u_{i-1}\},&
 O_i^-&=((u_{i+1},V,\gamma),C\cup\{u_{i-1}\}),\\
 B_i^+&=C\cup\{u_{i+1}\},&
 O_i^+&=((u_{i-1},V,\gamma),C\cup\{u_{i+1}\}).
 \end{aligned}                                                \tag{2.14}
\]

For routing choices \(\beta_i^\pm\in B_i^\pm\), the incoming nodes are

\[
 \begin{aligned}
 I_i^-&=((x_i,u_{i+1},V),
          (C\cup\{u_{i-1}\}-\{\beta_i^-\})\cup\{\gamma\}),\\
 I_i^+&=((x_i,u_{i-1},V),
          (C\cup\{u_{i+1}\}-\{\beta_i^+\})\cup\{\gamma\}).
 \end{aligned}                                                \tag{2.15}
\]

### Proposition 2.6 (single-cube refined-circulation obstruction)

No choice of the six routing letters makes one cubic trade transparent to
the refined circulation (2.12).  Its two phases have opposite nonzero
decorated $O$-triangles.  Every $I$-node begins with an exterior label
$x_i$, while every $O$-node begins with an internal label $u_j$, so
the $I$-terms cannot cancel that $O$-difference.

Consequently, in the natural **role-separated** two-cube face where the
exterior $x$-labels of either cube are disjoint from the internal
$u$-labels of the other, a refined-transparent packet must first supply
the same decorated $O$-triangle with opposite orientation--the same
ordered suffix continuation and bottom-core map--and must then separately
match the $\beta$-modified $I$-states in (2.15).  The coarse inverse-prefix
condition of Theorem 2.4 is necessary but not sufficient.  Without
cross-cube role separation, an $I$-node of one cube can in principle cancel
an $O$-node of the other; that nonstandard weave is not classified here.

#### Proof

The six nodes in (2.14) are distinct: fixing their first rail letter fixes
the index, and the two phases then have different bottom cores.  Also
\(\{x_0,x_1,x_2\}\cap U=\varnothing\), so no node in (2.15) equals one in
(2.14), independently of the choices \(\beta_i^\pm\).  Hence the outgoing
triangle difference survives in the full boundary

\[
 \sum_i\bigl({\bf e}_{O_i^+}-{\bf e}_{I_i^+}
              -{\bf e}_{O_i^-}+{\bf e}_{I_i^-}\bigr).        \tag{2.16}
\]

For two role-separated cubes, cross-cube $I/O$ cancellation is excluded
for the same first-letter reason.  Cancellation of the outgoing part then
requires an oppositely oriented copy of the same decorated triangle before
the incoming terms can be considered. \(\square\)

The proposition remains true at depth three with the evident shortened
form of (2.14): coarse one-letter rail divergence is invariant there, but
the decorated bottom-core triangle is not.  Thus the refined common-flow
gate is strictly stronger in every nontrivial depth.

There is nevertheless an exact paired escape at depth three.

### Theorem 2.7 (depth-three opposite-cube circulation packet)

Assume \(d=3\) and \(m\ge4\).  Fix one \(m\)-set \(Q\), a three-set
\(U=\{u_0,u_1,u_2\}\subset Q\), and put \(D=Q-U\ne\varnothing\).  Take two
exterior injections

\[
            u_i\mapsto x_i,qquad u_i\mapsto y_i
            \quad (i\in\mathbb Z_3),                           \tag{2.17}
\]

such that the six resulting roots

\[
                  Q-u_i+x_i,\qquad Q-u_i+y_i                 \tag{2.18}
\]

are distinct.  On the \(x\)-cube toggle phase \(-\to+\), and on the
\(y\)-cube toggle the opposite phase \(+\to-\).  At every root choose a
routing letter \(\delta_i\in D\), using the same letter in the two phases
of that root.

Then the six-root packet:

1. preserves every named suffix-row multiset through depth three;
2. preserves the exact refined Euler boundary (2.12), not only coarse rail
   balance.

No one-cube packet has property 2, so two cubes are minimum.

#### Proof

For either exterior injection, the two phase flags at its \(i\)-th root are

\[
 f_{i,x}^-=(Q-u_i+x_i;x_i,u_{i+1})
       \quad\hbox{and}\quad
 f_{i,x}^+=(Q-u_i+x_i;x_i,u_{i-1}),                           \tag{2.19}
\]
and analogously with \(y_i\).  Their bottom cores are respectively
\(D+u_{i-1}\) and \(D+u_{i+1}\), while their last deleted letters are
\(u_{i+1}\) and \(u_{i-1}\).  Therefore, for the common choice
\(\delta_i\in D\),

\[
 I(f_i^-,\delta_i)=I(f_i^+,\delta_i)
 =\left((x_i),(D\setminus\{\delta_i\})
                    \cup\{u_{i-1},u_{i+1}\}\right).         \tag{2.20}
\]

Thus one cube has no \(I\)-boundary at all.  Its complete refined defect is
the decorated \(O\)-triangle of Proposition 2.6, which depends on
\(Q,U\) but not on the exterior injection.  Toggling the second cube in the
opposite direction cancels that triangle exactly.  This proves refined
circulation transparency.  Finally, each cube is an all-depth row trade,
proving item 1.  Proposition 2.6 proves minimality.
\(\square\)

The packet is not a private-resource absorber: its two cubes share the
same auxiliary suffix-row bank determined by \(Q,U\).  In the marked SCD
selector one copy may be quarantined unmarked, so this sharing is not
automatically fatal.  It is fatal in any stricter formulation requiring all
selected suffix occurrences to be distinct.  Moreover the degree-one guard
is **not** automatic: at an affected node the unique outgoing routing label
may belong to an unchanged arc, while the packet changes the exterior label
of the unique incoming flag.  The guard is safe if every affected node has
degree at least two, or after the finitely many unique outgoing labels are
checked against both possible incoming exterior labels.  Owner-rainbow
improvement is also not automatic.  The theorem supplies a six-root move
inside the exact static-plus-Euler-boundary fibre; guard safety and an owner
augmentation remain explicit finite interface rows.

The owner row has one further exact obstruction.  For fixed \(i\), the two
opposite decorated nodes used by the paired packet are

\[
 v_i^-=(u_{i+1},D+u_{i-1}),\qquad
 v_i^+=(u_{i-1},D+u_{i+1}).                         \tag{2.21}
\]

Although the ordered states differ, their owner base is the same facet

\[
       S_i=(u_{i+1})\cup(D+u_{i-1})
          =(u_{i-1})\cup(D+u_{i+1})=Q-u_i.          \tag{2.22}
\]

### Proposition 2.8 (basewise owner transparency forces a companion head rectangle)

In one fixed one-flag-per-root table, the available addition-label sets at
$v_i^-$ and $v_i^+$ are disjoint.  Suppose the distinguished old matches
use additions $b_i^-,b_i^+$ and the distinguished new matches use
$c_i^-,c_i^+$, with all four matches legal and with the complete owner
palette rainbow.  If the two distinguished owner colours **over this fixed
base \(S_i\)** are preserved as a multiset, rather than transported to a
different base \(S_j\), then necessarily

\[
                         c_i^-=b_i^+,
             \qquad      c_i^+=b_i^-.                         \tag{2.23}
\]

Thus the six-root paired cube cannot be basewise owner-transparent while
its head assignment is frozen.  It needs, for every $i$, a companion
two-by-two head rethread which swaps the two addition labels between
$v_i^-$ and $v_i^+$.

#### Proof

An addition label $b$ at either node determines the head root

\[
                              S_i\cup\{b\}.                    \tag{2.24}
\]

The same label cannot occur at both nodes of one table, because that would
assign two different complete flags to the same head root.  This proves
disjointness.

Before the toggle the two distinguished owner pairs outside the common
base $S_i$ are

\[
                         \{x_i,b_i^-\},\qquad
                         \{y_i,b_i^+\},                        \tag{2.25}
\]

and afterward they are

\[
                         \{y_i,c_i^-\},\qquad
                         \{x_i,c_i^+\}.                        \tag{2.26}
\]

In a rainbow palette the pair containing $x_i$ in (2.25) cannot match the
$y_i$-leading pair in (2.26): that cross equality would force both owner
pairs to be the same unordered pair $\{x_i,y_i\}$.  Hence it matches the
$x_i$-leading pair, giving $c_i^+=b_i^-$.  The remaining equality gives
$c_i^-=b_i^+$. \(\square\)

Proposition 2.8 is the exact owner-level boundary of the first positive
cubic packet in the basewise face.  The next basewise local macro is not
merely two opposite cubes; it is

\[
 \boxed{\text{opposite depth-three cubes}
        +\text{ three companion head rectangles}.}           \tag{2.27}
\]

Those rectangles must themselves preserve the suffix rows and refined
circulation.  Normalized matching, SCD target coverage, and fractional
owner marginals do not automatically supply them.  A genuinely nonlocal
alternative may transport owner colours among the three different bases
\(S_0,S_1,S_2\); that six-owner relay is not ruled out here.

## 3. The depth-three post-processing no-go

### Corollary 3.1 (cubic orbit obstruction at depth three)

Let \({\cal F}\) be any depth-three exact marked selector.  If

\[
                         H_1^{\cal F}\ne H_2^{\cal F},        \tag{3.1}
\]

then no table in its all-depth cubic-trade orbit satisfies rail balance.
In particular no table in that orbit has even a literal directed cycle
cover, before owner-rainbow, connectivity, voltage, residence, or upper
constraints are considered.

#### Proof

At depth three, Lemma 1.1 and (1.5) say rail balance is equivalent to
\(H_1=H_2\).  Theorem 2.1 preserves both histograms. \(\square\)

The standard recursive SCD with least-element continuation at
\((7,3,3)\) is an authenticated exact instance of the hypothesis: it has

\[
             |\{x:H_1(x)\ne H_2(x)\}|=6,qquad
             \|H_1-H_2\|_1=24.                       \tag{3.2}
\]

It is still an exact all-high marked selector.  Therefore (3.2) is a
literal separation between static SCD integrality and chronology
integrality, and Corollary 3.1 proves that the existing cubic absorber does
not bridge it post hoc.

The finite numbers in (3.2) are the already independently replayed output
of `scratch/audit_scd_flag_turn_balance_20260801.cpp`; the no-go from those
numbers is theorem-level and uses no new enumeration.

## 4. The higher-depth cubic fibre and its parity split

Theorem 2.2 also identifies a smaller algebraic warning at higher depth.
Fix a continuation 

\[
                  \overline W=(w_3,\ldots,w_{d-2})            \tag{4.1}
\]

and suppose a local block has distinct first labels \(x_1,\ldots,x_t\) and
distinct second labels \(u_1,\ldots,u_t\), each used once.  Its prefix
choices form a permutation matrix.  A cubic move composes the assignment
with a three-cycle on three second labels.  Hence:

### Proposition 4.1 (permutation parity invariant)

Inside a degree-one prefix-contingency block, every sequence of cubic
moves preserves the sign of the \(x\)-to-\(u\) permutation.

#### Proof

Each move changes one assignment by a three-cycle.  Every three-cycle is an
even permutation, so the sign is unchanged. \(\square\)

This is a move-set obstruction, not an obstruction to the complete Boolean
host.  Longer all-depth circuits or a move changing a deletion-position
histogram may join the two parity classes.  It nevertheless proves that the
cubic moves are not a complete Markov basis even after (0.3) has been
imposed.

## 5. Why layered flow and ordinary matroid intersection stop here

The protected SCD theorem uses an integral layered containment flow.  That
network controls the visited set at every rank.  It has no row recording
the coordinate deleted at a specified time.  Adding the equations

\[
                         H_j(x)=H_{j+1}(x)                     \tag{5.1}
\]

couples different layers by label and is not an ordinary one-commodity
network constraint.  Theorem 2.1 shows that cubic post-processing cannot
be invoked to repair a violation of (5.1) after the flow is rounded.

After flags are fixed and rail states are balanced, choosing turns uses
three simultaneous resources:

\[
                   \text{tail root},\quad
                   \text{head root},\quad
                   \text{rank-}(m+1)\text{ owner}.             \tag{5.2}
\]

It is a perfect matching problem in a tripartite three-uniform hypergraph,
equivalently the intersection of three partition constraints.  Two-matroid
intersection therefore does not apply in general.  The exact functional
attachment face remains the valid exception: fixing a bijection from heads
to owners duplicates one row family and reduces (5.2) to bipartite Hall.

Thus the presently justified routes are:

1. prospectively build the chain selector in the zero-flux fibre (5.1),
   then prove statewise Hall and owner-rainbow;
2. prospectively build a functional owner attachment whose predecessor
   graph satisfies Hall; or
3. add a basis-changing all-depth move whose \(\Phi\)-image spans the
   required flux corrections, followed by cubic moves for the
   fixed-marginal correlations.

## 6. The next support-level fractional obstruction after rail balance

There is a sharp distinction between the complete flag host and the
physical common host.  In the complete host, every determinant-two triangle
of chain rows has a diagonal flag and an all-depth cubic absorber.  After
turn structural zeros are imposed, that diagonal or its legal owner
attachment may disappear.

Proposition 1.4 is the smallest fractional obstruction to colourful rail
circulation itself.  Even after rail circulation has been solved, the
tail/head/owner coupling has its own smallest obstruction.  Consider three
residual resource rows and three admissible common columns
with incidence matrix

\[
                         \begin{pmatrix}
                         1&0&1\\
                         1&1&0\\
                         0&1&1
                         \end{pmatrix}.                         \tag{6.1}
\]

The vector \((1/2,1/2,1/2)\) covers every row once, while no zero-one
selection does.  Every one- or two-row exact-packing matrix is integral, so
(6.1) is the smallest possible fractional-but-integral exact-cover
obstruction at this second stage.  The diagonal flag closes it statically; a **turn-safe**
diagonal or an odd portal is required to close it in the common host.

Accordingly, (6.1) is not asserted to be an isolated obstruction in the
full Boolean catalogue.  Its exact role is to identify what any common
rounding theorem must prove: physical structural zeros may not isolate an
odd residual component from every diagonal/portal column.  Fractional
pull-clock feasibility alone does not prove that statement.

## 7. Bounded prepared roots and the exact remaining theorem

Fixing \(O(1)\) roots to one robust order does not alter the invariant.
Their flags contribute a fixed \(O(1)\) vector to every \(H_j\), which the
unprepared part must cancel exactly.  The static protected SCD theorem can
quarantine their marked suffixes, but quarantine does not remove their
prefix/suffix contribution to chronology.

The robust-order theorem supplies each prepared root with
\(m-O(d)\) legal local turns and pair-codegree one.  This is enough to pack a
bounded family of portals once a suitable residual chronology exists.  It
does not construct the residual zero-flux selector.  The exact missing
statement can therefore be weakened and stated without later gates:

> **Zero-flux protected common-rounding lemma.**  For every fixed number of
> robust prepared flags, choose one flag at every other root so that
> (i) every required marked high suffix occurs exactly once,
> (ii) all positional fluxes \(\Phi_j\) vanish,
> (iii) every overlap-state graph has a perfect matching, and
> (iv) those matchings admit one copy of every owner.

Connectivity, voltage, residence, upper shadows, and the compiler are not
part of this lemma.  The results above prove two necessary refinements of
any proposed proof:

* the layered SCD flow must be rounded jointly with zero positional flux;
  zero flux cannot be repaired later by the current cubic absorber;
* even within zero flux, cubic moves have smaller parity fibres, so a
  complete proof needs longer circuits, a basis-changing absorber, or a
  prospective functional-attachment construction.

The common one-copy gap remains open.  What is closed is the tempting
post-processing route from an arbitrary exact SCD table using only the
known all-depth cubic trades.

## 8. Audit basis and exact scope

No new finite search is used in this note.  The structural proofs were
derived against the following frozen inputs:

```text
6ce355b0bb5f5ffeacfb4b44a3fb6225cb6772b96d61103a205257e3447b3465
  MATH_THEOREM_CORRECTED_PULL_CLOCK_PACKING_AND_FRACTIONAL_TRACE_CIRCULATION_20260801.md

eee317a7b1e885595b1d92a2323718fc73d1bd884b0054108a9e22db96548184
  MATH_THEOREM_SCD_EXACT_ALL_HIGH_ORDERED_CHAIN_SELECTOR_AND_PROTECTED_GATE_20260801.md

7c38177c7ec900e0aa47818c679dd1505c5adc8106d18247609503c407daca91
  MATH_THEOREM_SCD_FLAG_RAIL_BALANCE_STATEWISE_HALL_AND_OWNER_GATE_20260801.md

7b1214ab04e7f8f2e8c1021b1e6bd468f9a3f97fd9f955a089578f38fca1c449
  MATH_THEOREM_ORDERED_CHAIN_DIAGONAL_CLOSURE_CUBIC_TRADE_AND_PROTECTED_ABSORBER_20260801.md

8c3b02920dc3fe0a658d3f36de19cbb943067ee23456978c4f77889015d8c40c
  MATH_THEOREM_K_OVERLAP_CORE_FLOW_AND_ROOT_COLOURED_CIRCULATION_GATE_20260801.md
```

The finite SCD calibration quoted in (3.2) is bound to

```text
6aa038097f5904c04dd3244c12e81755faffedc267fec4a92048f06fd03a17de
  scratch/audit_scd_flag_turn_balance_20260801.cpp

20cd6d8ce155f908863b0267eeda86cb13828940f3510d64dbc8d4ae72883b29
  scratch/scd_flag_turn_balance_20260801.audit.txt
```

Every negative conclusion is architecture-scoped:

* Corollary 1.5 concerns its literal two-option root-orbit atlas;
* Corollary 3.1 concerns one cubic-trade orbit of a fixed selector;
* Proposition 2.6 concerns one standard cube;
* Proposition 2.8 concerns basewise owner preservation with the residual
  owner matching fixed outside the displayed interface.

None is a no-go for a different prospectively chosen Boolean flag table.
