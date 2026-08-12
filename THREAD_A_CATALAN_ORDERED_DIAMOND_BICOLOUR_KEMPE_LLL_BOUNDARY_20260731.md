# Ordered-diamond colours: the exact Kempe split and probabilistic boundary

Date: 2026-07-31  
Status: exact all-\(m\) structural theorems and sharp method obstructions
proved; no all-\(m\) full colour or \(q\)-colouring is claimed

## 1. Verdict

Let \(|\Omega|=2m\), \(m\ge2\), and put

\[
 N=\binom{2m}{m-1}=m\operatorname {Cat}_m,
 \qquad q=m(m+1).
\]

The ordered-diamond conflict graph \(C_m\) has vertices

\[
 \alpha=(L,U,T,H),\qquad L=T\cap H,\quad U=T\cup H,\quad T\ne H,
\]

and two atoms conflict when they have a common lower, upper, tail, or head
resource.  This note proves the following.

1. One full ordered colour is strictly weaker than \(\chi(C_m)=q\):

   \[
   \boxed{\text{one full colour}\iff \alpha(C_m)=N
          \iff \chi_f(C_m)=q.}
   \]

   A Catalan linear matching further requires that maximum independent set
   to be acyclic.

2. The full atom catalogue always has an exact equitable first
   bicolouring.  It follows by orienting the Johnson graph almost
   Eulerianly and assigning opposite colours to reverse atoms.

3. Equitable bicolouring is not hereditary.  For a width-two block there
   is an exact bipartiteness criterion, and an explicit eight-atom block
   at \(m=2\) fails it because of a non-Helly resource triangle.  Thus
   pairwise Kempe balancing cannot be an all-dimensional proof unless it
   carries and cancels an odd-circuit parity token through other colours.

4. The natural probabilistic schemes do not enter the local-lemma regime.
   The canonical one-colour atomic lopsided LLL fails by a dimension-free
   constant, independent random lower-fibre permutations are exponentially
   unlikely to be proper, and the uniform-perfect-matching triple LLL has
   the already audited limiting pressure \(24e\).  These are scoped no-gos
   for the stated samplers, not nonexistence theorems.

5. Exact finite status is

   \[
   \begin{array}{c|c|c}
   m&\text{proved}&\text{not proved here}\\ \hline
   2&\chi=6;\text{ six acyclic classes in one certificate}&-\\
   3&\chi=12;\text{ ten acyclic and two cyclic classes}&-\\
   4&\text{one acyclic full class; }\chi_f=20&\chi=20.
   \end{array}
   \]

The sharp surviving gate is therefore a Boolean, multicolour cancellation
theorem for odd resource circuits, or directly one acyclic maximum
independent set.  Neither ordinary recursive equity nor raw LLL/counting
supplies it.

## 2. Exact graph ledger

Every lower and upper fibre has size \(q\); every tail and head fibre has
size \(m^2\).  Hence

\[
 |V(C_m)|=Nq=\binom{2m}{m}m^2.
\]

### Proposition 2.1 (exact degree)

The graph \(C_m\) is regular of degree

\[
 \boxed{\Delta(C_m)=4m^2-2m-1.}                       \tag{2.1}
\]

After the other \(q-1\) atoms in the same lower fibre are removed, an atom
has exactly

\[
 \boxed{\delta_{\rm cross}=3m(m-1)}                  \tag{2.2}
\]

remaining conflicts.

#### Proof

For one atom, the four resource-fibre sizes are \(q,q,m^2,m^2\).  Their
six pairwise intersections have sizes

\[
 2,m,m,m,m,1.
\]

Every triple intersection and the fourfold intersection consist only of
the atom itself.  Inclusion--exclusion therefore makes the union of the
four fibres have size

\[
 2q+2m^2-(4m+3)+4-1=4m^2-2m.
\]

Deleting the atom proves (2.1), and subtracting its lower clique proves
(2.2).  \(\square\)

Thus generic degree bounds see only

\[
 \alpha(C_m)\ge {Nq\over \Delta+1}
   ={N(m+1)\over4m-2}\sim {N\over4},                 \tag{2.3}
\]

far short of a full \(N\)-atom class.

## 3. One full colour is a fractional-chromatic equality

### Theorem 3.1 (one-colour equivalence)

The following are equivalent:

1. \(C_m\) has an independent set of size \(N\);
2. there is one ordered four-transversal;
3. \(\chi_f(C_m)=q\).

#### Proof

The \(N\) lower fibres are disjoint \(q\)-cliques, so every independent set
has size at most \(N\).  An independent set of size \(N\) meets each lower
fibre once.  There are also \(N\) upper fibres, and it meets each of those
at most once, so it meets every upper fibre once.  Tail and head conflicts
give the other two injections.  This is exactly an ordered
four-transversal, and the converse is immediate.

Coordinate permutations act transitively on ordered diamonds, so \(C_m\)
is vertex-transitive.  For a finite vertex-transitive graph,

\[
 \chi_f(G)={|V(G)|\over\alpha(G)}.
\]

Since \(|V(C_m)|=Nq\) and \(\alpha(C_m)\le N\), the last equivalence
follows.  \(\square\)

The directed middle trace of a full colour has indegree and outdegree at
most one, but it may contain cycles.  Thus Catalan Linear Matching asks for
an **acyclic** maximum independent set.  Also, \(\chi(C_m)=q\) partitions
all atoms into \(q\) full classes and is stronger than Theorem 3.1.  A
certificate of \(\chi=q\) still has to exhibit or separately produce an
acyclic class; an arbitrary proper \(q\)-colouring need not have one.

Near-optimal chromatic bounds do not recover the weaker target by counting.
A \((q+s)\)-colouring forces an \(N\)-vertex class from class sizes only if

\[
                  s(N-1)<q.                           \tag{3.1}
\]

For every \(m\ge3\), \(N-1\ge q\), so even a hypothetical \(q+1\)
colouring would not force a full class by this argument.

## 4. A positive all-dimensional first bicolouring

### Theorem 4.1 (reverse-paired Euler split)

The whole atom catalogue admits a red/blue split such that every lower and
upper fibre contains exactly \(q/2\) atoms of each colour, while every tail
and head fibre contains at most \(q/2\) atoms of either colour.  More
precisely, its two colour loads at a middle role are

\[
 \left\lfloor {m^2\over2}\right\rfloor,
 \quad
 \left\lceil {m^2\over2}\right\rceil.
\]

#### Proof

Pair each atom with its reversal; the pairs are the edges of
\(J(2m,m)\).  Every graph has an orientation in which indegree and
outdegree differ by at most one: pair its odd-degree vertices by auxiliary
edges, take Euler tours, orient the tours, and delete the auxiliary edges.
Orient \(J(2m,m)\) this way.  Colour the atom in the chosen direction red
and its reversal blue.

Every unoriented diamond contributes one red and one blue atom at its lower
and upper resources, giving \(q/2\) of each.  At a middle set, red tail and
head loads are its outdegree and indegree; blue interchanges them.  The
Johnson degree is \(m^2\), proving the displayed loads.  Finally
\(\lceil m^2/2\rceil\le m(m+1)/2=q/2\).  \(\square\)

This theorem is a genuine first split.  It does not recurse automatically,
because either half has lost reverse-pair closure.

## 5. Exact recursive split equations

Call a set \(A\) of atoms an \(r\)-block when

\[
 d_A(L)=d_A(U)=r,\qquad d_A(T),d_A(H)\le r.          \tag{5.1}
\]

### Proposition 5.1 (exact split system)

Let \(r=s+t\).  An \(r\)-block splits into an \(s\)-block and a
\(t\)-block if and only if there is \(x\in\{0,1\}^A\) such that

\[
 x(L)=x(U)=s                                             \tag{5.2}
\]

for all outer resources, and

\[
 \max\{0,d_A(R)-t\}\le x(R)\le s,\qquad R=T,H.      \tag{5.3}
\]

The proportional point \(x_\alpha=s/r\) is always fractionally feasible.

#### Proof

Equations (5.2) give the required outer degrees in the selected child and
leave \(r-s=t\) in its complement.  The upper bound in (5.3) is the selected
middle capacity; the lower bound is exactly the complementary capacity
\(d_A(R)-x(R)\le t\).  Conversely these inequalities are precisely the
two block definitions.  At the proportional point, (5.2) is immediate,
and both inequalities follow from \(d_A(R)\le r\).  \(\square\)

Thus recursive equity is an integrality problem, not a marginal-feasibility
problem.

### Theorem 5.2 (sharp width-two Kempe criterion)

For a two-block \(A\), form \(K_A\) on the atoms of \(A\) by joining the
two atoms in every resource fibre of size two.  Then

\[
 \boxed{A\text{ splits into two one-blocks}\iff K_A\text{ is bipartite}.}
                                                               \tag{5.4}
\]

All splits are obtained by independently reversing the two colours on the
connected components of \(K_A\).

#### Proof

Every size-two fibre must split one-one, so a split is a proper
two-colouring of \(K_A\).  Fibres of size zero or one impose no additional
condition.  The converse and the component-flip statement are the standard
bipartite-colouring theorem.  \(\square\)

Pairing colours in a proper \(q\)-colouring and applying Theorem 5.2 gives
an exact all-colours normal form.

### Corollary 5.3 (odd-circuit-free two-block factorization)

Since \(q\) is even,

\[
 \chi(C_m)=q
\]

if and only if the full atom set partitions into \(q/2\) two-blocks
\(A_j\) for which every \(K_{A_j}\) is bipartite.

This removes unnecessary higher-depth recursion: the exact Kempe target is
an odd-resource-circuit-free two-block factorization.

## 6. The determinant-two obstruction is physical

Fix \(X\in\binom\Omega m\), ordered distinct \(p,s\in X\), and ordered
distinct \(q,r\notin X\).  Put

\[
\begin{aligned}
 a_1&=(X-p,X+q,X,X-p+q),\\
 a_2&=(X-p,X+r,X-p+r,X),\\
 a_3&=(X-s,X+r,X,X-s+r).
\end{aligned}                                         \tag{6.1}
\]

Then \(a_1a_2\) share a lower resource, \(a_2a_3\) share an upper
resource, and \(a_3a_1\) share a tail, with no resource common to all
three.  Reversal gives the head version.

### Proposition 6.1 (classification and count)

Every non-Helly conflict triangle is of one of the two forms above.  Their
total number is

\[
 \boxed{2\binom{2m}{m}m^2(m-1)^2
       =2|V(C_m)|(m-1)^2.}                            \tag{6.2}
\]

#### Proof

At an atom of a non-Helly triangle, its two incident pair-conflict types
must differ, or all three atoms share that resource.  A pair sharing two
resources cannot belong to a non-Helly triangle: for example, if two atoms
share \(L,T\), their other middle sets are \(L+q_i\) and their uppers are
\(T+q_i\); a cross containment forces \(q_1=q_2\).  Complement and reversal
give the cases other than a shared \(\{L,U\}\).  In that last case the two
atoms are the reverse orientations \((T,H)\) and \((H,T)\).  A third atom
avoiding the common \(L,U\) would have to share the two tail/head roles
separately, forcing its tail to equal its head, which is impossible.
Hence the three pair types are distinct.  Types
\(\{L,T,H\}\) force a common lower resource and types
\(\{U,T,H\}\) force a common upper, so they are Helly.  The only
non-Helly types are \(\{L,U,T\}\) and \(\{L,U,H\}\), parametrized by
(6.1) and its reversal.  The parameters are recovered from the three
shared resources, proving uniqueness and (6.2).  \(\square\)

On the three shared rows the incidence matrix is

\[
 A_\triangle=
 \begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix},
 \qquad \det A_\triangle=2.                           \tag{6.3}
\]

For residual demand \(b=(b_L,b_U,b_T)\),

\[
 A_\triangle^{-1}b={1\over2}
 \begin{pmatrix}
 b_L-b_U+b_T\\ b_L+b_U-b_T\\-b_L+b_U+b_T
 \end{pmatrix}.                                      \tag{6.4}
\]

Thus integrality requires, in particular, even total parity.  The exact
half-demand \((1,1,1)\) has only the solution
\((1/2,1/2,1/2)\).  Every nonconstant integral bicolouring balances two
rows and leaves one row monochromatic.

This local minor alone does not refute a global split: exterior atoms can
change \(b\).  The following block shows that it can become a closed,
literal Kempe lock.

### Theorem 6.2 (an eight-atom admissible block with no split)

For \(m=2\), \(\Omega=\{0,1,2,3\}\), take the atoms, written
\((L,U;T,H)\),

\[
\begin{array}{lll}
a_1=(1,012;01,12),&a_2=(1,013;13,01),&a_3=(0,013;01,03),\\
a_4=(2,012;02,12),&a_5=(2,123;12,23),&a_6=(3,023;03,23),\\
a_7=(3,123;23,13),&a_8=(0,023;02,03).
\end{array}                                           \tag{6.5}
\]

This is a two-block, but it has no split into two one-blocks.

#### Proof

Its lower fibres are

\[
 0:\{a_3,a_8\},\ 1:\{a_1,a_2\},\
 2:\{a_4,a_5\},\ 3:\{a_6,a_7\},
\]

and its upper fibres are

\[
 012:\{a_1,a_4\},\ 013:\{a_2,a_3\},\
 023:\{a_6,a_8\},\ 123:\{a_5,a_7\}.
\]

Every tail and head load is at most two.  The outer incidence graph is the
eight-cycle

\[
 L_1-U_{012}-L_2-U_{123}-L_3-U_{023}-L_0-U_{013}-L_1.
\]

However, \(a_1a_2\) share \(L_1\), \(a_2a_3\) share \(U_{013}\), and
\(a_3a_1\) share tail \(01\).  Thus \(K_A\) contains a triangle, and
Theorem 5.2 forbids a split.  \(\square\)

Consequently a theorem saying that every admissible block can be
recursively equitably bicoloured is false in the smallest dimension.
Pairwise Kempe flips only reverse connected components and cannot unlock
(6.5).  At least one atom must be routed through a third colour or through
an exterior parity-cancellation circuit.

## 7. Lopsided-LLL and counting boundaries

### 7.1 One random atom per lower fibre

Choose independently a uniform atom \(Z_L\) in every lower fibre.  For a
cross-conflicting pair \(\alpha\in A_L,\beta\in A_{L'}\), let

\[
 E_{\alpha\beta}=\{Z_L=\alpha,Z_{L'}=\beta\};
 \qquad \Pr(E_{\alpha\beta})=q^{-2}.                 \tag{7.1}
\]

The canonical atomic lopsidependency graph joins inconsistent partial
assignments.  A standard upper bound on its degree is

\[
 D\le2(q-1)\delta_{\rm cross}.                        \tag{7.2}
\]

More importantly, any valid negative-dependency graph must join
\(E_{\alpha\beta}\) to all events that choose a different atom in either
of its two lower fibres: such an event is mutually exclusive with
\(E_{\alpha\beta}\), and conditioning on its complement raises the latter
probability.  After the largest possible double-count subtraction, the
union of these mutually exclusive events has size at least

\[
 D\ge(q-1)(2\delta_{\rm cross}-q+1)
       =(q-1)(5m^2-7m+1).                            \tag{7.3}
\]

Thus even the optimized symmetric lopsided criterion

\[
 p\le {D^D\over(D+1)^{D+1}}                          \tag{7.4}
\]

fails for every \(m\ge2\).  Indeed, the right side of (7.3), plus one,
is at least \(q^2\), whereas (7.4) is strictly below \(1/(D+1)\).  At the
borderline \(m=2\), \(D\ge35\), and explicitly

\[
 {D^D\over(D+1)^{D+1}}
 \le {e^{-35/36}\over36}<{1\over36}=p.
\]

The simpler textbook pressure \(ep(D+1)\) is bounded below, for
\(m=2,3,4\), by

\[
 {36e\over36},\qquad {276e\over144},\qquad
 {1008e\over400},                                    \tag{7.5}
\]

and tends to \(5e\).

This is a no-go for the canonical symmetric atomic LLL.  It does not
exclude an asymmetric absorber using Boolean codegrees.

No theorem using only part size and cross degree can close the gap.  For
\(m\ge3\), take \(q+1\) parts of size \(q\), label vertices by
\([q]\), and join equal labels across parts; pad with \(N-q-1\) isolated
parts.  Its cross degree is \(q\le\delta_{\rm cross}\), but pigeonhole
forbids an independent transversal of the first \(q+1\) parts.  At \(m=2\),
use four parts with two copies of each of three labels; equal-label complete
multipartite graphs have degree six and again forbid a transversal.  The
Boolean incidence structure, not \((q,\delta,N)\), must do the work.

### 7.2 Independent random lower-fibre permutations

Give each lower fibre an independent uniform permutation of all \(q\)
colours.  A fixed tail \(T\) meets \(m\) lower facets, and each contributes
an independent uniform \(m\)-subset of colours.  Hence its \(m^2\) atoms
are all differently coloured with exact probability

\[
 \rho_m={ (q)_{m^2}\over (q)_m^m}.                   \tag{7.6}
\]

Let \(M=\binom{2m}{m}\).  A greedy independent set in
\(J(2m,m)\) has size at least

\[
 s=\left\lceil {M\over m^2+1}\right\rceil.          \tag{7.7}
\]

Nonadjacent tails share no lower facet, so the corresponding events in
(7.6) are independent.  Every proper colouring makes all of them rainbow;
therefore

\[
 \Pr(\text{proper})\le\rho_m^s.                      \tag{7.8}
\]

Sequentially exposing the \(m\) groups gives

\[
 \rho_m\le
 \exp\!\left[-{m^2(m-1)\over2(m+1)}\right],
\]

and consequently

\[
 \Pr(\text{proper})\le
 \exp\!\left[-{M m^2(m-1)\over
                    2(m+1)(m^2+1)}\right]
 =\exp[-(1/2-o(1))M].                                \tag{7.9}
\]

The exact calibrations are

\[
\begin{array}{c|c|c|c}
m&s&\rho_m&\rho_m^s\\ \hline
2&2&2/5&4/25=0.16\\
3&2&21/605&441/366025=0.0012048357\ldots\\
4&5&56056/101094801&5.24163\cdot10^{-17}.
\end{array}                                          \tag{7.10}
\]

Thus the most direct random all-colour assignment is exponentially
atypical, despite the positive \(m=2,3\) constructions.

### 7.3 Uniform outer perfect matching

Sampling one outer perfect matching targets one full colour directly.  The
canonical degree-three overload events at a middle vertex have

\[
 t_m=6\binom m3^2={(m)_3^2\over6}
\]

choices.  A fixed event has

\[
 D_m^{\rm conf}=3m^6+O(m^5)
\]

conflicting events.  Even the optimistic independent-edge calibration
\(p=d^{-3}=(8+o(1))m^{-6}\), where \(d=q/2\), gives

\[
 pD_m^{\rm conf}=24+o(1).                            \tag{7.11}
\]

The symmetric LLL would require \(ep(D+1)\le1\).  Moreover, at \(m=3\)
an exact pair of endpoint-disjoint canonical events is negatively
correlated, so conditioning on the complement of one raises the probability
of the other.  Any valid lopsided graph has degree at least \(59\), while

\[
 p={7164\over502309}=0.01426214\ldots
 >{59^{59}\over60^{60}}=0.00618292\ldots.            \tag{7.12}
\]

This is the independently audited raw perfect-matching LLL obstruction.

## 8. Small-dimensional audit

The graph arithmetic is

\[
\begin{array}{c|r|r|r|r|r}
m&N&q&|V|&\Delta&|E(C_m)|\\ \hline
2&4&6&24&11&132\\
3&15&12&180&29&2610\\
4&56&20&1120&55&30800.
\end{array}                                          \tag{8.1}
\]

The non-Helly triangle counts from (6.2) are respectively

\[
                  48,\qquad1440,\qquad20160.          \tag{8.2}
\]

Authenticated finite conclusions are:

* \(m=2\): a proper six-colouring with all six classes acyclic;
* \(m=3\): a proper twelve-colouring with ten acyclic and two cyclic
  classes;
* \(m=4\): an explicit acyclic full class of size \(56\), consisting of
  twelve nontrivial paths and two isolated path components, hence fourteen
  components in total.  Therefore \(\alpha(C_4)=56\) and
  \(\chi_f(C_4)=20\), but no proper twenty-colouring is certified.

The relevant frozen audits are

```text
scratch/audit_catalan_oriented_factorization_m2_m3_20260731.py
scratch/catalan_oriented_factorization_m2_m3_20260731.audit.json
scratch/audit_catalan_noncancelling_determinant_enumerator_20260731.py
scratch/catalan_noncancelling_determinant_enumerator_20260731.audit.json
scratch/audit_catalan_random_matching_lll_m3_20260731.py
scratch/catalan_random_matching_lll_m3_20260731.audit.json
```

## 9. Exact remaining hypothesis

The all-colours Kempe route is now equivalent to Corollary 5.3: construct a
two-block factorization with no odd component in any resource-conflict
graph \(K_{A_j}\).  The explicit block (6.5) proves that outer equity and
middle capacity do not imply this property.

The weaker one-colour route is exactly \(\alpha(C_m)=N\), followed by
cycle elimination if necessary.  A proof must use more than list size,
maximum degree, raw permanent marginals, or a pairwise equitable split.  A
sufficient new theorem would be a multicolour alternating-circuit/absorber
lemma that routes every parity demand (6.4) to another odd circuit while
preserving all lower and upper equations.  No such all-\(m\) routing theorem
is proved here.
