# Dyck-port path-factor fibres, alternating circuits, and a root-scale non-Motzkin switch

Date: 2026-07-26

Method: pure mathematics only.  No enumeration, solver, or web input is
used.

## 0. Outcome

Let

\[
 J=[2r],\qquad
 \mathcal X=\binom Jr,\qquad
 \mathcal Y=\binom J{r+1},\qquad
 \mathcal D=\mathcal D_r,
 \qquad \overline P=J\setminus P,
 \qquad \overline{\mathcal D}
   =\{\overline P:P\in\mathcal D\}.                    \tag{0.1}
\]

Write `G_r` for the middle-levels inclusion graph on
`mathcal X sqcup mathcal Y`.  The fibre of
`mathcal D_r`-port path factors has the following exact formulation.

* Choose a spanning subgraph `H subseteq G_r` with degree one at every
  port in

  \[
                    \mathcal A=\mathcal D\sqcup\overline{\mathcal D},
  \]

  and degree two at every other vertex.
* Impose only the complement-connectivity conditions that `P` and
  `bar P` lie in the same component for every `P in mathcal D`.

The degree equations contain exactly

\[
                         2r\operatorname {Cat}_r        \tag{0.2}
\]

edges.  Each `P`--`bar P` path has at least `2r` edges.  Hence the
complement conditions force exactly `Cat_r` geodesic path components and
leave no edge for a portless cycle.  This gives an exact integer
fixed-degree-plus-cuts description of the fibre.

If `C` is an `H`-alternating circuit, toggling `C` always preserves the
degree ledger, but it need not preserve the complement endpoint pairing.
There is an exact quotient test: delete the old edges of `C`, contract the
remaining path segments, and insert the new edges of `C`.  The switch is
port-legal if and only if the quotient reconnects the two residual pieces
containing `P` and `bar P` for every touched root.

Two useful consequences are sharp.

1. A reciprocal two-cut exchange which swaps middle segments between two
   rooted paths is always port-legal.
2. A simple alternating cycle which cuts each of `k>=2` distinct rooted
   paths exactly once cyclically permutes their terminal halves.  It is
   never port-legal.

Finally, the peak-free Motzkin normal form is **not** an invariant of the
full port-path-factor fibre.  The five-row `D_3` pentagon is one connected
alternating circuit (vertices may repeat, edges do not).  Wrap it in the
root context `w -> 1w0`.  This gives a literal `D_4`-port switch.  Its five
root ports have Motzkin normal forms

\[
          ULD,\ ULD,\ LLL,\ LLL,\ LLL,                  \tag{0.3}
\]

and an internal owner-routing cycle contains roots from both classes.
Thus it is a root-scale non-Motzkin coordinated alternating-circuit
switch.  This breaks the invariant for the full fibre, although it does
not prove that one **simple** port-legal alternating cycle crosses the
Motzkin classes, nor that these packets generate the whole fibre.

---

## 1. Fixed-degree subgraph formulation

Put

\[
 B=|\mathcal D|=\operatorname {Cat}_r.
\]

Every nonempty Dyck word begins with `1`, whereas its complement begins
with `0`; hence `mathcal D` and `overline{mathcal D}` are disjoint and
`|mathcal A|=2B`.

The shore sizes are

\[
                    |\mathcal X|=(r+1)B,
             \qquad |\mathcal Y|=rB.                    \tag{1.1}
\]

Define the required degree vector on `V(G_r)` by

\[
 d(v)=
 \begin{cases}
  1,&v\in\mathcal A,\\
  2,&v\notin\mathcal A.
 \end{cases}                                             \tag{1.2}
\]

For an edge set `H`, write `x_e=1_(e in H)` and
`x(delta(v))=sum_(e ni v)x_e`.

### Theorem 1.1 (exact fixed-degree-and-pairing fibre)

The `mathcal D_r`-port path factors are in bijection with the integral
solutions of

\[
 \boxed{
 \begin{aligned}
 x(\delta(v))&=d(v) &&(v\in V(G_r)),\\
 x(\delta(S))&\ge1
   &&\left.
      \begin{array}{l}
       P\in\mathcal D,\\[-2pt]
       P\in S,\ \overline P\notin S,
      \end{array}\right\}\\
 x_e&\in\{0,1\} &&(e\in E(G_r)).
 \end{aligned}}                                          \tag{1.3}
\]

Here the second line ranges over every `P` and every vertex set `S`
separating `P` from `bar P`.

#### Proof

A port path factor plainly satisfies the degree equations and every
separating-cut inequality.

Conversely, let `H` satisfy (1.3).  The cut inequalities are the standard
connectivity criterion: `P` and `bar P` lie in the same component of `H`
for every `P`.  Since every degree is at most two, every component of `H`
is a path or a cycle.  A component containing `P` and `bar P` is a path
whose only degree-one vertices are those two ports.  It cannot contain a
second complementary port pair.

There are therefore at least `B` disjoint path components.  Every path
from an `r`-set `P` to the disjoint `r`-set `bar P` projects, after every
two inclusion edges, to a Johnson step.  Their Johnson distance is `r`,
so each such path has at least `2r` edges.

On the other hand, summing degrees over the `mathcal X` shore counts every
edge of `H` once and gives

\[
 \begin{aligned}
 |E(H)|
   &=2|\mathcal X|-|\mathcal A|\\
   &=2(r+1)B-2B=2rB.                                    \tag{1.4}
 \end{aligned}
\]

The `B` complementary paths already require at least `2rB` edges.  Hence
they all have exactly `2r` edges and exhaust `H`; no portless cycle or
additional component remains.  They partition both shores and are the
required geodesic port paths.  \(\square\)

Thus the nonlinear part of the fibre is exactly complement connectivity.
The fixed-degree equations alone permit wrong endpoint pairings and
portless alternating cycles.

If `x_e in {0,1}` is relaxed to `0<=x_e<=1` while retaining only the
degree equations, the resulting bipartite `b`-matching polytope is
integral by total unimodularity of the bipartite incidence matrix.  The
complement cuts are the entire extra global structure.  No claim is made
that appending all of those cuts preserves total unimodularity or gives
the convex hull of the port fibre fractionally.

### Corollary 1.2 (two-perfect-matching coordinates)

Orient every component from `P in mathcal D` to `bar P` and alternately
colour its edges up and down, beginning with up.  This gives perfect
matchings

\[
 M^\uparrow:\mathcal X\setminus\overline{\mathcal D}
                   \longleftrightarrow\mathcal Y,
 \qquad
 M^\downarrow:\mathcal Y
                   \longleftrightarrow\mathcal X\setminus\mathcal D.
                                                               \tag{1.5}
\]

Conversely, the union of two matchings in (1.5) belongs to the port fibre
if and only if it satisfies the complement cuts in (1.3).

This separates the two ordinary matching ledgers from their common
endpoint monodromy.  Alternating cycles may be toggled independently
inside either matching as matching moves, but the resulting two matchings
need not satisfy the same complement cuts.

---

## 2. Exact endpoint monodromy of an alternating switch

Let `H` be a port factor.  An **alternating circuit** is a closed even
trail `C` with no repeated edge, whose edges alternate between

\[
                 E^-(C)=E(C)\cap E(H),
       \qquad   E^+(C)=E(C)\setminus E(H).              \tag{2.1}
\]

A simple alternating cycle is the special case with no repeated vertex.
Put

\[
                         H'=H\triangle E(C).             \tag{2.2}
\]

At every visit to a vertex the circuit removes and inserts the same number
of incident edges.  Therefore `H'` has exactly the same degree vector as
`H`.

Delete `E^-(C)` from `H`.  The touched old paths split into residual path
segments.  Contract each residual segment to one vertex and retain, as
labels, any global ports lying on that segment.  Add the edges `E^+(C)`
between these contracted vertices.  Call the resulting multigraph
`Q_C`.

### Theorem 2.1 (residual-segment quotient criterion)

The alternating switch (2.2) preserves the `mathcal D_r`-port fibre if
and only if, for every touched `P in mathcal D`, the two quotient vertices
whose residual segments contain `P` and `bar P` lie in the same component
of `Q_C`.

Equivalently, the endpoint involution of `H'` on
`mathcal A` is again

\[
                           P\longleftrightarrow\overline P. \tag{2.3}
\]

#### Proof

Expanding the contracted residual segments shows that components of
`Q_C` are exactly the touched components of `H'`.  Thus the displayed
condition is necessary.

If it holds, `P` is connected to `bar P` in `H'` for every root; untouched
roots retain their old paths.  The degree vector is still (1.2), so
Theorem 1.1, or its edge-count proof, excludes every residual portless
cycle and proves sufficiency.  The endpoint-involution formulation is the
same statement because every degree-one port lies on a unique path of a
maximum-degree-two graph.  \(\square\)

This criterion is exact but global.  The next two lemmas give local
certificates in opposite directions.

## 3. A sufficient reciprocal two-cut cycle

Take two old rooted paths `R_A,R_B`.  Cut two old edges in each, writing
their residual pieces in path order as

\[
             L_A\mid M_A\mid R_A^+,
      \qquad L_B\mid M_B\mid R_B^+.                    \tag{3.1}
\]

Here `L_A,R_A^+` contain the two complementary ports of the first path,
and similarly for the second.  Suppose four unused inclusion edges exist
which splice the pieces as

\[
       L_A-M_B-R_A^+,
       \qquad
       L_B-M_A-R_B^+,                                   \tag{3.2}
\]

and suppose the four removed and four inserted edges form one simple
alternating eight-cycle.

### Lemma 3.1 (reciprocal segment exchange)

Toggling this eight-cycle is a legal port-fibre switch.  It exchanges the
two middle segments but preserves both complementary endpoint pairs.

#### Proof

After contraction, `Q_C` has the two path components displayed in (3.2).
The first has the two original ports of `R_A`; the second has the two
original ports of `R_B`.  Theorem 2.1 applies.  \(\square\)

The pentagon difference in Section 5 contains the simple alternating
eight-cycle

\[
 1236-136-1356-156-1456-146-1246-126-1236,             \tag{3.3}
\]

with old and new edges alternating in that order.  In the old `D_3`
factor it exchanges

\[
 136-1346-146
 \quad\text{and}\quad
 126-1256-156                                           \tag{3.4}
\]

between the paths rooted at `123` and `124`.  The resulting paths are

\[
\begin{aligned}
123-1236-126-1256-156-1456-456,\\
124-1246-146-1346-136-1356-356,
\end{aligned}                                           \tag{3.5}
\]

so the endpoint pairs `123|456` and `124|356` remain literal.

The same proof permits a permutation of several middle segments, provided
every outer shell keeps its own two ports and all boundary inclusion
edges exist.  Such a move is generally a coordinated union of alternating
circuits rather than one simple cycle.

---

## 4. A sharp single-cut obstruction

Suppose a simple alternating cycle meets `k` distinct old rooted paths in
exactly one old edge each.  Orient the `i`-th path from `P_i` to
`bar P_i`, and write the removed edge as `a_i b_i`, with `a_i` on the
`P_i` side and `b_i` on the `bar P_i` side.

### Proposition 4.1 (one cut per path is illegal)

If the `P_i` are distinct and `k>=2`, toggling the cycle does not preserve
the port fibre.

#### Proof

Deleting the `k` old edges produces `2k` residual half-paths.  Each one
contains exactly one global port, and its only exposed vertex is one of
`a_i,b_i`.  Every inserted edge merely pairs two of these half-paths.
For `P_i` to be rejoined to `bar P_i`, the inserted matching would have to
pair `a_i` with `b_i`.  But `a_i b_i` is the removed old edge and is not
an inserted edge of an alternating cycle.  Hence no complementary pair is
restored in the required way.

In the special coherent orientation in which the inserted edges have the
form

\[
                            b_i a_{i+1}
                  \qquad(i\bmod k),                    \tag{4.1}
\]

the wrong endpoint involution is explicitly

\[
                          P_{i+1}\longleftrightarrow\overline{P_i}.
                                                               \tag{4.2}
\]

Other orientation patterns may join two initial halves or two terminal
halves, but are equally illegal.  \(\square\)

Thus an ordinary alternating cycle in the fixed-degree polytope is not a
legal generator merely because it preserves degrees.  A port-legal cycle
must have trivial endpoint monodromy; in particular it must revisit some
touched root path or use a more complicated multiple-cut pattern.

---

## 5. The rooted pentagon as one alternating circuit

On `J=[6]`, use the five old paths

\[
\begin{array}{c|cccc}
1&123&136&146&456\\
2&124&126&156&356\\
3&125&145&345&346\\
4&135&235&245&246\\
5&134&234&236&256
\end{array}                                             \tag{5.1}
\]

and the five new paths

\[
\begin{array}{c|cccc}
1&123&126&156&456\\
2&124&234&345&356\\
3&125&235&236&346\\
4&135&136&146&246\\
5&134&145&245&256.
\end{array}                                             \tag{5.2}
\]

Both tables enumerate every member of `binom([6],3)` once; their adjacent
unions enumerate every member of `binom([6],4)` once; and they have the
same five complement port pairs.  Thus they are two points of the fixed
degree fibre (1.3).

Their complete symmetric difference is the following alternating closed
trail.  A dash labelled `-` is an old edge and a dash labelled `+` is a
new edge:

\[
\begin{aligned}
1236&\mathbin{-}136\mathbin{+}1356
\mathbin{-}156\mathbin{+}1456
\mathbin{-}146\mathbin{+}1246\\
&\mathbin{-}124\mathbin{+}1234
\mathbin{-}134\mathbin{+}1345
\mathbin{-}345\mathbin{+}2345\\
&\mathbin{-}245\mathbin{+}1245
\mathbin{-}125\mathbin{+}1235
\mathbin{-}135\mathbin{+}1356\\
&\mathbin{-}356\mathbin{+}3456
\mathbin{-}346\mathbin{+}2346
\mathbin{-}234\mathbin{+}2345\\
&\mathbin{-}235\mathbin{+}2356
\mathbin{-}256\mathbin{+}2456
\mathbin{-}246\mathbin{+}1246\\
&\mathbin{-}126\mathbin{+}1236.
                                                               \tag{5.3}
\end{aligned}
\]

The repeated `mathcal Y`-vertices `1356,2345,1246` are visits through
different incident edges; no edge is repeated.  Every old-only and every
new-only edge of (5.1)--(5.2) occurs exactly once in (5.3).  Hence (5.3)
is one connected alternating circuit whose toggle replaces the whole old
pentagon by the new one.

The circuit is not simple.  It decomposes as a degree move into simple
alternating cycles, but Theorem 2.1 must be rechecked after each proposed
constituent toggle.  The legality of the coordinated whole does not imply
that every simple constituent preserves the port pairing.  The simple
eight-cycle (3.3) is the reciprocal legal move (3.4)--(3.5); the full
pentagon supplies the larger coordinated endpoint identity.

---

## 6. Root wrapping breaks the Motzkin normal form

Write the five local Dyck roots as binary words

\[
\begin{aligned}
T_1&=111000,&T_2&=110100,&T_3&=110010,\\
T_4&=101010,&T_5&=101100.                               \tag{6.1}
\end{aligned}
\]

The two internal owner-routing permutations of the pentagon are

\[
 c_1=(T_1\ T_2\ T_5\ T_3\ T_4),
 \qquad
 c_2=(T_1\ T_2\ T_3\ T_5\ T_4).                      \tag{6.2}
\]

Now apply the common root context

\[
                              \mathsf J(w)=1w0.          \tag{6.3}
\]

to both sides of the path packet.  Rooted context functoriality preserves
the two aggregate shore ledgers and every row's complementary endpoints:
the two new boundary edges depend only on the common ports, while reversal,
complementation, and adjoining the outer coordinates inject the old
`mathcal X`- and `mathcal Y`-tokens.  Keeping the other nine canonical
`D_4` rows unchanged therefore gives two literal `D_4`-port path factors.
The image of (5.3) is their coordinated alternating circuit after common
edges are suppressed.

The five affected `D_4` ports are

\[
\begin{array}{c|c|c|c}
i&W_i=\mathsf J(T_i)&M(W_i)&\operatorname {nf}M(W_i)\\ \hline
1&11110000&ULD&ULD\\
2&11101000&ULD&ULD\\
3&11100100&UDL&LLL\\
4&11010100&LLL&LLL\\
5&11011000&LUD&LLL.
\end{array}                                             \tag{6.4}
\]

Here `M` is obtained from the three internal coordinate pairs by

\[
                    11\mapsto U,\qquad
                    00\mapsto D,\qquad
                    10,01\mapsto L,                    \tag{6.5}
\]

and `nf` repeatedly flattens `UD` to `LL`.

The common context reverses the order of the local internal phases, and
may invert the convention for the cycles in (6.2), but it does not change
which root owns which injected local token.  Hence the wrapped packet has,
up to inversion and interchange, the same two owner cycles on
`W_1,...,W_5`.  In particular one cycle contains the adjacency

\[
                         W_2\longleftrightarrow W_5,     \tag{6.6}
\]

and the other contains

\[
                         W_2\longleftrightarrow W_3.     \tag{6.7}
\]

Both cross from normal form `ULD` to normal form `LLL`.

### Theorem 6.1 (root-scale non-Motzkin port switch)

The root-wrapped pentagon is an integral, port-preserving, coordinated
alternating-circuit switch in the `D_4` middle-levels fibre whose owner
routing does not preserve the peak-free Motzkin normal form.

#### Proof

Integrality, exact shore ownership, and complement pairing follow from
the context argument above.  Formula (6.4) gives two distinct normal
forms, while (6.6)--(6.7) show that the packet routes an internal state
token between their root-owner classes.  \(\square\)

### Corollary 6.2 (all larger root scales)

For every `r>=4`, there is an integral `D_r`-port packet whose owner
routing crosses the peak-free Motzkin normal forms.

#### Proof

Append the common Dyck suffix `(10)^(r-4)` to every port and apply rooted
context functoriality once more.  In the paired Motzkin encoding, each
appended `10` contributes one terminal level step.  The two normal forms
in (6.4) therefore become

\[
                  ULD\,L^{r-4}
       \qquad\text{and}\qquad L^{r-1},                  \tag{6.8}
\]

which remain distinct and peak-free.  The injected owner cycles are still
those in (6.2), up to inversion, so they still cross the two classes.
\(\square\)

This does not contradict the Motzkin invariant for the smaller menu of
leaf rectangles and their even-pair conjugates.  The pentagon is a
coordinated five-row circuit, not one conjugated leaf rectangle.

---

## 7. Exact boundary

The following are now proved.

1. The port fibre is exactly the integral fixed-degree system (1.3).
2. The only nonlinear condition is the complement endpoint pairing;
   the edge-count identity then excludes cycles automatically.
3. The residual-segment quotient is a necessary-and-sufficient legality
   test for every alternating circuit.
4. Reciprocal two-cut segment exchanges are legal, while a single cyclic
   cut through distinct paths is illegal.
5. The rooted pentagon has the explicit connected alternating circuit
   (5.3).
6. Its root wrapping gives a literal non-Motzkin `D_4` port switch, and
   common suffix suspension gives one at every `r>=4`.

The following stronger statements are not proved.

1. The root-wrapped pentagon circuit is not simple.  No claim is made that
   one simple alternating cycle already crosses the Motzkin normal forms.
2. An arbitrary degree-preserving cycle need not satisfy the quotient
   criterion; alternating-cycle generation of the full port fibre remains
   open.
3. Breaking the Motzkin invariant does not prove a full Catalan conveyor.
   Bounded size-three context packets may retain other operadic or
   collapsed-skeleton obstructions.
4. No quantitative cap-tail, shadow-dispersion, or bounded-diameter result
   follows merely from the existence of this switch.

The next sharp finite object is therefore a **simple-cycle monodromy
classification**: determine which simple alternating cycles in the
fixed-degree graph have trivial quotient monodromy, and whether those
cycles alone connect the non-Motzkin owner classes exhibited by
Theorem 6.1.
