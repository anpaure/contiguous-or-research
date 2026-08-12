# Phase-varying nested-star decks: the BA orbit norm and the positive-density no-go

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Exact outcome

Put

\[
 n=2m+1,\qquad C=BA,\qquad L=m(m+1),\qquad
 W=\binom{2m+1}{m}.                                               \tag{0.1}
\]

Throughout, \(m\ge3\). All asymptotic statements are as
\(m\to\infty\); the protected-height application \(H\ge4\) lies in this
range.

The nested-star owner nibble supplies the forced \((1/2-o(1))W\)
switches, but an atom-only alternating completion additionally requires
the source set \(S\) to satisfy

\[
                         S=C(S).                                  \tag{0.2}
\]

The fixed-three-orbit packet is known to fail for protected height
\(H\ge4\). This note allows the atom partners and phases to vary
arbitrarily and obtains a stronger structural conclusion.

1. **A literal phase atom exists.** For every \(2\le p\le m\), the
   positional 3-cycle

   \[
      T_p=(1\ n\ p)                                               \tag{0.3}
   \]

   partitions permutation states into legal canonical nested-star source
   triples. Thus there is no local atom obstruction.

2. **Every multi-orbit packet has a new exact norm obstruction.** For a
   full \(C\)-orbit \(O\), let \(Z(O)\) be the \(m\)-set of labels on
   the length-\(m\) position cycle of \(C\). Its endpoint-edge deck is
   exactly the complete directed cut

   \[
      \overrightarrow K_{Z(O),Z(O)^c}.                            \tag{0.4}
   \]

   Hence its endpoint-divergence norm is

   \[
      \Delta(O)=n\mathbf1_{Z(O)}-m\mathbf1.                       \tag{0.5}
   \]

   Since every nested-star atom is a directed endpoint triangle, every
   phase-varying atom-incidence component containing \(u\) full
   \(BA\)-orbits must satisfy

   \[
      \boxed{
      \sum_O\mathbf1_{Z(O)}={mu\over n}\mathbf1,
      \qquad n\mid u.}                                           \tag{0.6}
   \]

   Thus every nonempty packet contains at least \(n=2m+1\) full orbits.
   In particular, every \(O(1)\)-orbit commutator deck is impossible,
   even with arbitrary phase rematching and orientation and even when
   orbit types may repeat. At the first possible size \(u=n\), the orbit
   types must be an exact 1-design of \(n\) \(m\)-sets, every label
   occurring \(m\) times.

3. **The endpoint connector residue is sharp.** If \(mu=nq+\rho\),
   \(0\le\rho<n\), and \(c\) source states are left outside atom
   triangles, then

   \[
      \boxed{c\ge\rho(n-\rho).}                                  \tag{0.7}
   \]

   This is only polynomial and is asymptotically absorbable. It is the
   sharp finite obstruction in the endpoint-divergence lattice; it is a
   necessary condition, not a sufficiency assertion for physical
   connectors or suffix-fibre atom closure.

4. **A common phase gauge explodes.** If every orbit uses one common
   phase-dependent positional atom \(T_{p_t}\), the conjugate 3-cycles
   generate \(A_n\). A representative deck invariant under them cannot
   contain one representative per \(C\)-orbit. In the fixed-
   commutator form, every nonempty set invariant under both \(C\) and
   \(T_2\) is the entire \(n!\)-state space, loading every owner
   \(2m!(m+1)!\) times. Thus the natural phase-varying commutator cannot
   be nibbled to owner capacity one.

5. **The unrestricted algebraic object is explicit.** After activating
   full \(C\)-orbits, the atom problem decomposes by ordered suffix word.
   In each suffix fibre, the marked endpoint arcs must admit an admissible
   directed-triangle factor, equivalently an order-three successor
   permutation. Ordinary local Hall circulation is not sufficient because
   it may produce longer directed cycles.

6. **Positive density is nevertheless impossible for constant one.**
   Equation (0.2) makes every selected physical component fully
   alternating, regardless of how its \(A\)-sources are regrouped into
   atoms.

   * If \(m\) is even, every full orbit repeats its source and successor
     owner multisets, so no nonempty owner-capacity-one selection exists.
   * If \(m\) is odd and \(A_{\rm BA}\) owner occurrences lie in such
     components inside an otherwise arbitrary owner-transversal hybrid,
     then the rank-\((m-1)\) lower hole count obeys

     \[
       \boxed{
       M_1^-\ge
       \left({A_{\rm BA}\over2}-{2W\over m+2}\right)_+.}          \tag{0.8}
     \]

     In particular, positive-density mass
     \(A_{\rm BA}\ge\alpha W\) forces
     \((\alpha/2-o(1))W\) first-shadow holes. A full atom-only solution
     has

     \[
       M_1^-\ge{m-2\over2(m+2)}W
              =\left({1\over2}-o(1)\right)W.                     \tag{0.9}
     \]

Atom regrouping can cancel every signed nested divergence, but it does
not change the selected states, their alternating directions, or their
prefix targets. Therefore no phase-varying multi-orbit solution of the
strict atom-only equation \(S=BA(S)\) can be used on positive owner
density in a coefficient-one construction. The lane is structurally
closed at \(q=1\), before trail cost: any surviving use has
\(A_{\rm BA}=o(W)\).

## 1. BA orbits and the endpoint cut

Write a permutation state as

\[
 x=(x_1,\ldots,x_n).                                               \tag{1.1}
\]

Write \((Cx)_j=x_{\sigma(j)}\). The pullback position permutation
\(\sigma\) has the two cycles

\[
 P=(1,3,5,\ldots,2m-1),\qquad
 Q=(2,4,6,\ldots,2m,n),                                          \tag{1.2}
\]

of lengths \(m\) and \(m+1\). Since the labels of a state are distinct,
every state orbit has exact length

\[
                          L=m(m+1).                               \tag{1.3}
\]

For a \(C\)-orbit \(O\), let \(Z(O)\) be the set of labels occupying
the positions of \(P\). The labels on \(Q\) are \(Z(O)^c\).

At a selected \(A\)-switch, orient the endpoint edge from its tail to its
head:

\[
                         x_1\longrightarrow x_n.                  \tag{1.4}
\]

### Theorem 1.1 (complete directed-cut theorem)

As \(x\) runs once through a full orbit \(O\), the endpoint edges (1.4)
are exactly

\[
 \boxed{
 \{a\to b:a\in Z(O),\ b\in Z(O)^c\},}                            \tag{1.5}
\]

each with multiplicity one.

Consequently

\[
 \boxed{
 \Delta(O):=
 \sum_{x\in O}({\bf e}_{x_1}-{\bf e}_{x_n})
 =(m+1)\mathbf1_{Z(O)}-m\mathbf1_{Z(O)^c}
 =n\mathbf1_{Z(O)}-m\mathbf1.}                                   \tag{1.6}
\]

#### Proof

Along the \(m\)-cycle, each label of \(Z(O)\) occupies position \(1\)
exactly \(L/m=m+1\) times. Along the \((m+1)\)-cycle, each label of
\(Z(O)^c\) occupies position \(n\) exactly \(L/(m+1)=m\) times.

More precisely, a phase is a pair of shifts modulo \(m\) and \(m+1\).
The Chinese remainder theorem makes these shifts independent. Thus every
ordered pair \((a,b)\in Z(O)\times Z(O)^c\) occurs at a unique phase.
Summing its vector \({\bf e}_a-{\bf e}_b\) proves (1.6). \(\square\)

This cut theorem keeps more information than the aggregate norm. The
endpoint-only quotient of an orbit packet is a union of complete directed
cuts which must be decomposed into directed triangles.

## 2. The orbit-norm and design obstruction

A canonical nested-star atom has endpoint edges

\[
                a\to b,\qquad b\to c,\qquad c\to a,              \tag{2.1}
\]

and therefore has zero endpoint divergence.

### Theorem 2.1 (orbit-design theorem)

Let \(\mathscr Y\) be a multiset of \(u\) full \(C\)-orbits whose states
are partitioned, with arbitrary phase matching and orientation, into
canonical nested-star atoms. Then

\[
 \boxed{
 \sum_{O\in\mathscr Y}\mathbf1_{Z(O)}
 ={mu\over n}\mathbf1.}                                         \tag{2.2}
\]

In particular,

\[
                          \boxed{n\mid u.}                        \tag{2.3}
\]

The same assertions hold separately in every component generated by
\(C\)-moves and atom-partner moves.

#### Proof

Sum (1.6) over \(O\in\mathscr Y\). The atom partition groups all endpoint
edges into triples (2.1), each of sum zero. Hence

\[
 n\sum_O\mathbf1_{Z(O)}-mu\mathbf1=0,
\]

which is (2.2). Its coordinates are integers. Since
\(\gcd(m,n)=1\), one must have \(n\mid u\).

For the componentwise statement, a component containing one selected
state contains its entire \(C\)-orbit and every full atom triple meeting
it. The same sum can therefore be taken inside the component. \(\square\)

At the first possible size \(u=n\), equation (2.2) says that the orbit
types \(Z(O)\) are \(n\) blocks of size \(m\), with every label in exactly
\(m\) blocks. This aggregate invariant is sharp: on labels
\(\mathbb Z_n\), choose any \(m\)-set \(R\) and take the multiset

\[
                         Z_g=R+g\qquad(g\in\mathbb Z_n).           \tag{2.4}
\]

Every label then lies in exactly \(m\) blocks. Equation (2.4) certifies
only the orbit-type norm; it does not supply the ordered-suffix triangle
factor or owner transversality.

### Theorem 2.2 (sharp endpoint connector residue)

Let \(\mathscr Y\) contain \(u\) full orbits, and suppose all but \(c\)
of their source states lie in canonical endpoint triangles. Write

\[
                         mu=nq+\rho,\qquad0\le\rho<n.             \tag{2.5}
\]

Then

\[
                         \boxed{c\ge\rho(n-\rho).}                \tag{2.6}
\]

The same bound holds if the \(c\) exceptional states are replaced by
one-edge connector defects, each of endpoint \(\ell^1\)-norm at most two.

#### Proof

Put

\[
 d_x=n\#\{O:x\in Z(O)\}-mu.                                     \tag{2.7}
\]

The atom triangles contribute zero, so the \(c\) exceptional endpoint
edges must sum to \((d_x)_x\). Each has \(\ell^1\)-norm two, whence

\[
                         2c\ge\sum_x|d_x|.                        \tag{2.8}
\]

Each \(d_x\) is congruent to \(-\rho\pmod n\), and \(\sum_xd_x=0\).
The least possible \(\ell^1\)-norm is obtained by taking \(\rho\)
coordinates equal to \(n-\rho\) and \(n-\rho\) coordinates equal to
\(-\rho\). Thus

\[
                         \sum_x|d_x|\ge2\rho(n-\rho),             \tag{2.9}
\]

which proves (2.6). \(\square\)

The residue in (2.6) is at most \(O(m^2)\). It is not a positive-density
obstruction, but it fixes the sharp finite endpoint-divergence deficit
that any absorber must repair. No sufficiency for literal connectors is
claimed.

## 3. A local positional atom and the common-gauge explosion

Let

\[
 J=\{m+2,m+3,\ldots,2m\}                                        \tag{3.1}
\]

be the ordered suffix positions of a canonical atom.

For \(2\le p\le m\), define \(T_p\) on states by

\[
 (T_px)_1=x_n,\qquad (T_px)_n=x_p,\qquad (T_px)_p=x_1,           \tag{3.2}
\]

fixing every other position. Its pullback permutation is the 3-cycle
\((1\ n\ p)\).

### Theorem 3.1 (literal positional nested-star atom)

For every permutation state \(x\),

\[
                         \{x,T_px,T_p^2x\}                        \tag{3.3}
\]

is a canonical nested-star source triple.

#### Proof

Put \(a=x_1\), \(b=x_n\), and \(c=x_p\). The three endpoint pairs are

\[
                         (a,b),\quad(b,c),\quad(c,a).              \tag{3.4}
\]

The positions \(1,n,p\) all lie outside \(J\), so the three ordered
suffixes agree. Position \(m+1\) is fixed and has a fourth label, distinct
from \(a,b,c\). Hence the final entry of each middle block lies in the
common \(R\)-set, which is precisely the remaining condition in the
canonical nested-star normal form. \(\square\)

This gives a real local commutator. The obstruction begins when one asks
for a sparse \(C\)-invariant owner deck.

### Lemma 3.2 (connected triples generate the alternating group)

Let \(\mathcal E\) be a collection of oriented 3-cycles on a finite set
\(V\). If the hypergraph of their three-point supports is connected, then

\[
                         \langle\mathcal E\rangle=A(V).           \tag{3.5}
\]

#### Proof

Start with one support, whose cycle generates \(A_3\), and order the
remaining supports along a spanning tree of the support-incidence graph,
so that each new support meets the accumulated vertex set \(U\).
Inductively suppose the generated group contains \(A(U)\).

If a new support adds one vertex \(x\), its cycle has the form
\((a\ b\ x)\) up to inversion, with \(a,b\in U\); together with \(A(U)\)
this generates \(A(U\cup\{x\})\). If it adds two vertices \(x,y\), its
cycle has the form \((a\ x\ y)\). Conjugation by \(A(U)\), which is
transitive on \(U\), supplies \((b\ x\ y)\) for every \(b\in U\). For
distinct \(a,b\in U\),

\[
 (a\ x\ y)(b\ x\ y)^{-1}=(a\ x\ b),                            \tag{3.5a}
\]

up to the harmless convention for composition order. These cycles first
generate \(A(U\cup\{x\})\), and the original cycle then adjoins \(y\).
Thus the induction gives \(A(V)\). \(\square\)

### Theorem 3.3 (common-gauge phase schedules are impossible)

Choose one representative from every activated \(C\)-orbit and let
\(\mathcal R\) be the representative set. Suppose that at each phase
\(t\in\mathbb Z_L\) one common value

\[
                         p_t\in\{2,\ldots,m\}                     \tag{3.6}
\]

is used across the whole deck, so that \(C^t\mathcal R\) is partitioned
into \(T_{p_t}\)-orbits. Then \(\mathcal R=\varnothing\).

#### Proof

The phase condition is equivalent to

\[
 D_t\mathcal R=\mathcal R,\qquad
 D_t=C^{-t}T_{p_t}C^t.                                           \tag{3.7}
\]

Because state-operator composition reverses pullback composition, the
pullback of \(D_t=C^{-t}T_{p_t}C^t\) is
\(\sigma^t(1\ n\ p_t)\sigma^{-t}\). Its support contains the positions

\[
 u_t=\sigma^t(1)\in P,\qquad v_t=\sigma^t(n)\in Q.              \tag{3.8}
\]

As \(t\) ranges modulo \(L\), the CRT makes \((u_t,v_t)\) run through
every pair of \(P\times Q\). Hence the support hypergraph of the
3-cycles \(D_t\) is connected. Lemma 3.2 gives

\[
                         \langle D_t:t\in\mathbb Z_L\rangle=A_n. \tag{3.9}
\]

Every nonempty invariant set of permutation states therefore contains a
full \(A_n\)-orbit, of size \(n!/2\). But \(C\) is odd, so every
\(C\)-orbit contains \(L/2\) states of each parity. An \(A_n\)-orbit
therefore contains \(L/2>1\) states from each \(C\)-orbit, contradicting
the definition of \(\mathcal R\) as a representative set. \(\square\)

For the fixed rule \(T_2\), the conjugate supports are all triples

\[
                         (P_i,Q_{j-1},Q_j),                        \tag{3.10}
\]

and the same proof gives

\[
                         \langle C,T_2\rangle=S_n,                \tag{3.11}
\]

because \(C\) is odd. Thus a state set invariant under both \(C\) and
\(T_2\) is empty or the entire \(n!\)-state space. The full state space
is indeed tiled by the atoms (3.3), but each middle owner occurs

\[
                         2m!(m+1)!                                \tag{3.12}
\]

times among sources and \(A\)-successors. It is a flow-valid multicover,
not an owner factor.

The only escape from Theorem 3.3 is a genuinely state- or orbit-dependent
atom permutation. The next section records its exact finite criterion.

## 4. Exact suffix-fibre criterion for an unrestricted deck

Fix a family \(\mathscr Y\) of activated full \(C\)-orbits. For a state
\(e\), write

\[
 K(e)=e|_J,\qquad
 t(e)=e(1),\qquad h(e)=e(n),\qquad \rho(e)=e(m+1).                \tag{4.1}
\]

Define the ordered suffix deck

\[
                 \mathcal D(O)=\{K(e):e\in O\}.                 \tag{4.1a}
\]

For one orbit, each ordered suffix word occurs at most once: equality at
one suffix position from each of the two cycles in (1.2) forces equal
phase shifts modulo \(m\) and \(m+1\).

For every ordered suffix word \(K\), form the marked directed multigraph
\(G_K(\mathscr Y)\). Its arcs are the unique states \(e\) in the selected
orbits with \(K(e)=K\), written

\[
                         t(e)\longrightarrow h(e)                 \tag{4.2}
\]

and marked by \(\rho(e)\).

### Theorem 4.1 (marked triangle-factor criterion)

The selected orbit states admit a phase-varying canonical nested-star atom
partition if and only if, for every suffix word \(K\), the complete arc
multiset of \(G_K(\mathscr Y)\) partitions into directed triangles

\[
                         a\to b,\quad b\to c,\quad c\to a         \tag{4.3}
\]

with \(a,b,c\) distinct and

\[
 \rho(a,b)\ne c,\qquad
 \rho(b,c)\ne a,\qquad
 \rho(c,a)\ne b.                                                 \tag{4.4}
\]

Equivalently, every fibre admits a permutation \(\beta_K\) of its arcs
such that

\[
 \begin{gathered}
  h(e)=t(\beta_Ke),\qquad \beta_K^3e=e,\\
  \text{every }\beta_K\text{-cycle has length }3,\\
  h(\beta_Ke)\notin\{t(e),\rho(e)\}.
 \end{gathered}                                                    \tag{4.5}
\]

#### Proof

The coordinate criterion for one canonical atom says exactly that its
three states share their ordered suffix, have endpoint edges forming
(4.3), and obey the three last-middle exclusions (4.4). This proves both
directions. Encoding the successor edge in each directed triangle gives
\(\beta_K\), and conversely its 3-cycles recover the atoms. \(\square\)

For every endpoint label \(v\), ordinary Hall may match incoming arcs
\(a\to v\) to allowed outgoing arcs \(v\to c\). Those local matchings
produce a directed cycle cover. They are not sufficient for (4.5): the
cycles may have lengths other than three. Thus the exact fibre gate is

\[
 \boxed{
 \text{local Hall circulation}\quad+\quad\beta_K^3=1.}            \tag{4.6}
\]

No commutation law \(\beta C=C\beta\) is required. Activating full
\(C\)-orbits already gives \(S=C(S)\); the atom permutation may vary
freely from suffix fibre to suffix fibre.

### 4.1 A partner-capacity consequence

Assume now that \(m=2r+1\) is odd. For two orbit types put

\[
 d(O,P)=|Z(O)\setminus Z(P)|.                                    \tag{4.7}
\]

If \(O,P\) occur together in an atom, then \(d(O,P)\ge1\). Indeed the
head label of the \(O\)-edge lies in \(Z(O)^c\), while as the tail of the
next edge it lies in \(Z(P)\).

Their ordered suffix decks satisfy

\[
 \boxed{
 |\mathcal D(O)\cap\mathcal D(P)|
 \le(r+2-d(O,P))_+(r+3-d(O,P))_+.}                               \tag{4.8}
\]

To see this, the length-\(r\) window on the \(m\)-cycle must avoid the
\(d\) labels in \(Z(O)\setminus Z(P)\), giving at most
\((r+2-d)_+\) starts. Independently, the length-\(r\) window on the
\((m+1)\)-cycle must avoid the opposite \(d\) labels, giving at most
\((r+3-d)_+\) starts. The CRT multiplies the bounds.

Let \(c_{OP}\) count selected atoms containing both orbits. Then

\[
 c_{OP}=c_{PO},\qquad c_{OO}=0,\qquad
 c_{OP}\le|\mathcal D(O)\cap\mathcal D(P)|,                       \tag{4.9}
\]

and

\[
                         \sum_{P\ne O}c_{OP}=2L.                  \tag{4.10}
\]

Since a partner has \(d\ge1\), every orbit has at least

\[
 \boxed{
 \left\lceil{2L\over(r+1)(r+2)}\right\rceil
 =\left\lceil{4(2r+1)\over r+2}\right\rceil}                    \tag{4.11}
\]

distinct partner orbits. In particular, for \(m\ge23\), at least eight
partners are necessary. This is weaker than the component-size obstruction
\(u\ge n\); it rules out decks of partner degree at most seven, but does
not rule out all constructions of bounded partner degree.

## 5. BA flow is a positive-density first-shadow obstruction

The preceding sections leave a difficult state-dependent triangle-factor
problem. For coefficient one, however, it need not be solved: every
solution of (0.2) has the same fatal prefix profile.

### Proposition 5.1 (alternating component normal form)

If \(S=C(S)\), then \(S\) is a union of full \(C\)-orbits. For each such
orbit \(O\), the selected physical states are

\[
 e,Ae,Ce,ACe,\ldots,C^{L-1}e,AC^{L-1}e,                          \tag{5.1}
\]

forming one fully alternating rotor component of length \(2L\).

Regrouping the \(L\) source states into nested-star atoms changes neither
the state set in (5.1) nor any prefix target.

#### Proof

Invariance under a permutation is precisely union of its full orbits.
Every source uses its \(A\)-transition, and its successor uses the forced
\(B\)-transition to the next source \(Ce=BAe\). This is (5.1). Atom
membership is extra bookkeeping on the same \(A\)-transitions. \(\square\)

### Theorem 5.2 (even-\(m\) owner-doubling no-go)

If \(m\) is even, no nonempty union of components (5.1) satisfies owner
capacity one.

#### Proof

Let

\[
 \kappa(x)=\{x_1,\ldots,x_m\}.                                   \tag{5.2}
\]

On positions, the owner footprint of \(Ae\) is
\(\{2,\ldots,m+1\}\). For even \(m\), this footprint is the
\(C^{m+1}\)-translate of \(\{1,\ldots,m\}\). Hence, phase by phase,

\[
 \kappa(AC^te)=\kappa(C^{t+m+1}e).                               \tag{5.3}
\]

The source and successor owner multisets of every full orbit are equal.
Their union therefore has even multiplicity at every owner, and cannot be
a nonempty capacity-one family. \(\square\)

Assume from now on that \(m=2r+1\) is odd. The \(2L\) owners in (5.1)
are then distinct. Indeed the source and successor owner footprints
\(\{1,\ldots,m\}\) and \(\{2,\ldots,m+1\}\) meet the two position cycles
in \((r+1,r)\) and \((r,r+1)\) points, respectively, so their
\(C\)-orbits are disjoint; each orbit has length \(L\) because its two
nontrivial cyclic intervals have trivial stabiliser. Thus owner-simple
components are possible.

### Lemma 5.3 (factor-two first-shadow collision)

The \(2L\) rank-\((m-1)\) lower-prefix occurrences in one component
(5.1) have support exactly \(L\): every target occurs twice.

#### Proof

The two base prefix footprints are

\[
 P_{m-1}=\{1,\ldots,m-1\},\qquad
 Q_{m-1}=\{2,\ldots,m\}.                                        \tag{5.4}
\]

Since \(m-1=2r\), both meet the position cycles \(P,Q\) of (1.2) in
\(r\) positions. On the \(m\)-cycle, the second footprint is a one-step
translate of the first; on the \((m+1)\)-cycle their intersections agree.
The CRT therefore supplies a power of \(C\) carrying one footprint to the
other. Their two length-\(L\) target orbits coincide. Each footprint orbit
has full length \(L\), so every target has multiplicity two. \(\square\)

### Theorem 5.4 (hybrid positive-density no-go)

Let an otherwise arbitrary owner-transversal rotor factor use
\(A_{\rm BA}\) of its \(W\) owner occurrences in disjoint fully
alternating components (5.1). Then its number of missing distinct
rank-\((m-1)\) lower-prefix targets satisfies

\[
 \boxed{
 M_1^-\ge
 \left({A_{\rm BA}\over2}-{2W\over m+2}\right)_+.}               \tag{5.5}
\]

#### Proof

By Lemma 5.3, the alternating occurrences support at most
\(A_{\rm BA}/2\) distinct targets. Each of the other
\(W-A_{\rm BA}\) owner occurrences supports at most one further target.
Thus total first-shadow support is at most

\[
                         W-{A_{\rm BA}\over2}.                    \tag{5.6}
\]

The target layer has size

\[
 N_1=\binom{2m+1}{m-1}={m\over m+2}W
    =W-{2W\over m+2}.                                             \tag{5.7}
\]

Subtracting (5.6) from (5.7), and taking the positive part, proves
(5.5). \(\square\)

For every fixed \(\alpha>0\),

\[
 A_{\rm BA}\ge\alpha W
 \quad\Longrightarrow\quad
 M_1^-\ge(\alpha/2-o(1))W.                                      \tag{5.8}
\]

In particular, a full owner-transversal atom-only completion has
\(A_{\rm BA}=W\) and obeys (0.9). No separate per-letter repair bound is
asserted here. The needed conclusion is the exact one used by the
coefficient-one transfer: its total missing shadow mass must be \(o(W)\).
The linear lower bound (5.8) already violates that necessary condition.

This proof is completely insensitive to the atom partition. It applies to
fixed triples, phase-varying partners, state-dependent commutators, and any
solution of the suffix-fibre criterion in Section 4.

## 6. Exact boundary

The following has now been proved.

* Local canonical phase atoms exist, so the failure is not local.
* Every phase-varying atom-incidence component contains a multiple of
  \(2m+1\) BA orbits and its orbit types form the exact design (2.2).
* The sharp endpoint-divergence connector lower bound is (2.6); physical
  sufficiency is not asserted.
* Every common-gauge positional schedule is empty; the fixed
  \(T_2\)-closure is the full state space and violates owner capacity
  maximally.
* The unrestricted state-dependent deck is exactly the marked
  suffix-fibre order-three factor problem (4.5), with the partner capacity
  (4.11).
* Even \(m\) forbids every nonempty owner-simple BA deck.
* Odd \(m\) permits owner-simple BA components, but positive-density use
  forces the linear first-shadow defect (5.5).

Thus the phase-varying multi-orbit question has two different answers.
At the state-incidence level, large state-dependent decks are not ruled
out; the exact surviving equations are (2.2) and (4.5), and the full-state
\(T_2\)-deck is an explicit multicover. At the coefficient-one level
requested here, the architecture is closed. Precisely, let \(S\) be the
set of \(A\)-source states belonging to the BA components of an
owner-transversal rotor factor. Then

\[
 \boxed{
 S=BA(S),\quad
 \operatorname{mult}_Y
 \bigl(\kappa(x),\kappa(Ax):x\in S\bigr)\le1
 \text{ for every owner }Y,\quad M_1^-=o(W)
 \ \Longrightarrow\ |S|=o(W).}                                  \tag{6.1}
\]

Here \(2|S|=A_{\rm BA}\), so (6.1) is exactly Theorem 5.4. The
owner-capacity hypothesis is essential: without it, the full permutation
state space is a counterexample to the bare sparsity implication. The
atom-only BA mechanism can therefore be only a vanishing reserve inside a
literal coefficient-one factor. Any positive-density nonlocal rethreading
must break strict alternation—by inserting genuinely different
connector/run types which change the internal prefix profile—not merely by
changing the atom partners or their phases.
