# Phase-varying (BA)-orbit atoms: exact port factorization and the sparse owner gate

Date: 2026-07-26

Method: exact orbit geometry, exact enumeration, and an explicit directed-triangle
factorization.  No computation or solver is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad C=BA,\qquad L=m(m+1).
\]

Corollary 4.6 of
`MATH_THEOREM_NESTED_STAR_ATOM_OWNER_NIBBLE_AND_FLOW_GATE_20260726.md`
rules out completing three fixed (BA)-orbits phase by phase.  This note
handles the only surviving possibility: the two partner orbits are allowed
to vary with the phase.

There are four conclusions.

1.  The phase-varying incidence structure is very sparse at the pair
    level.  If \(\mathcal O,\mathcal O'\) are two \(BA\)-orbits and
    \(j=|A_{\mathcal O}\setminus A_{\mathcal O'}|\), then at most
    \(2j\le2m\) pairs of their phase ports can lie in a common protected
    nested-star atom.  The resulting orbit-pair atom codegree is \(o(1)\)
    times the orbit degree, with a factorial margin.

2.  Nevertheless, there is no full-density phase-completion obstruction.
    For every protected height \(2\le H\le m-1\), all \(n!\) permutation
    states admit an explicit partition into protected nested-star atoms.
    It activates every \(BA\)-orbit and its partners necessarily vary with
    phase.

3.  At sparse density, phase variation has a sharp component cost.  If a
    connected protected atom component has \(kn\) \(BA\)-orbits and
    \(h=\lceil H/2\rceil\), then
    \[
       k\ge h+1\quad(m\text{ odd}),\qquad
       k\ge h\quad(m\text{ even}).
    \]
    Thus the relevant blocks have \(\Omega(nH)\) orbit vertices; fixed
    packets and even the first \(2n\)-orbit candidates are ruled out.

4.  The owner equations introduce a parity split.  For even \(m\), the
    source- and successor-owner decks of every full \(BA\)-orbit coincide,
    so the atom-only lane is impossible even with an \(o(W)\) leave.  For
    odd \(m\), those decks are internally disjoint and the exact remaining
    problem is sparse owner-transversal rounding in blocks of size at
    least \(\Omega(nH)\).

Thus partner variation genuinely solves the \(BA\)-flow rows at full
density, but it does not make the sparse owner problem local.  It replaces
the failed three-orbit packet by a growing-block rounding gate, and it
closes the unperturbed lane altogether for even \(m\).

## 1. Protected flags and the two coordinate cycles

Represent a permutation state uniquely as

\[
 e=(a,P,\mathbf K,b),
 \qquad |P|=m,\quad |\mathbf K|=m-1,
 \tag{1.1}
\]

where (a=x_1), (b=x_n), and

\[
 \mathbf K=(k_1,\ldots,k_{m-1})
 =(x_{m+2},\ldots,x_{n-1}).
\]

Let (K) be the underlying set of (\mathbf K).  For
(0\le H\le m-1), define the protected suffix flag

\[
 \Phi_H(e)=\bigl(K;k_1,\ldots,k_H\bigr).
 \tag{1.2}
\]

Equality of these flags is exactly equality of the nested suffix cores
through protected depth (H).

The coordinate permutation

\[
 C(x_1,\ldots,x_n)
 =(x_3,x_4,\ldots,x_{n-1},x_1,x_n,x_2)
\]

has two position cycles: the odd positions, of length (m), and the even
positions together with position (n), of length (m+1).  For a
(C)-orbit (\mathcal O), let

\[
 A_{\mathcal O}=\{\text{labels on the length-}m\text{ position cycle}\},
 \qquad B_{\mathcal O}=[n]\setminus A_{\mathcal O}.
 \tag{1.3}
\]

### Lemma 1.1 (endpoint grid and flag injectivity)

For every (C)-orbit (\mathcal O):

1. the endpoint map
   
   \[
      e\longmapsto(a(e),b(e))
   \]
   
   is a bijection
   
   \[
      \mathcal O\longrightarrow A_{\mathcal O}\times B_{\mathcal O};
      \tag{1.4}
   \]

2. if (H\ge2), then (\Phi_H) is injective on (\mathcal O).

#### Proof

The first endpoint position lies on the length-(m) coordinate cycle and
the second lies on the length-(m+1) cycle.  The powers of (C) advance
the two phases simultaneously.  Since (\gcd(m,m+1)=1), the Chinese
remainder theorem makes the (L=m(m+1)) powers run through every pair of
phases exactly once.  This proves (1.4).

The first two positions of the suffix block have opposite parity, hence
one belongs to each coordinate cycle.  If two powers of (C) have the
same first two ordered suffix labels, distinctness of the labels forces
their phase difference to be (0\pmod m) and (0\pmod{m+1}).  It is
therefore (0\pmod L), proving injectivity. \(\square\)

The exact flag counts will be used repeatedly.  Write

\[
 t_H=(m-1)!(m-1-H)!.
 \tag{1.5}
\]

### Lemma 1.2 (exact port counts)

The number of protected flags is

\[
 |\mathfrak F_H|
 =\binom n{m-1}(m-1)_H
 =\frac{n!}{(m+2)!(m-1-H)!}.
 \tag{1.6}
\]

For a fixed flag (F=(K;k_1,\ldots,k_H)), put
(Q=[n]\setminus K), so (|Q|=m+2).  Then:

\[
 \#\{e:\Phi_H(e)=F\}=(m+2)!(m-1-H)!,
 \tag{1.7}
\]

\[
 \#\{e:\Phi_H(e)=F,(a(e),b(e))=(a,b)\}=m t_H,
 \tag{1.8}
\]

and, if (r(e)) is the final entry of (P),

\[
 \#\{e:\Phi_H(e)=F,(a(e),b(e),r(e))=(a,b,r)\}=t_H.
 \tag{1.9}
\]

#### Proof

Choose (K), then its ordered (H)-prefix.  Once the flag is fixed, the
remaining suffix entries have ((m-1-H)!) orders.  The (m+2) outside
labels occupy the two ordered endpoint positions and the ordered (P)-block
in ((m+2)!) ways.  Fixing (a,b) leaves (m!) orders of (P), and
fixing its last entry leaves ((m-1)!).  These are (1.6)--(1.9). \(\square\)

## 2. The protected atom hypergraph

Three states form a protected (H)-atom if, after a cyclic relabelling,
they have the form

\[
 e_{ab}=(a,P_{ab},\mathbf K_{ab},b),\quad
 e_{bc}=(b,P_{bc},\mathbf K_{bc},c),\quad
 e_{ca}=(c,P_{ca},\mathbf K_{ca},a),
 \tag{2.1}
\]

where

\[
 \Phi_H(e_{ab})=\Phi_H(e_{bc})=\Phi_H(e_{ca}),
 \tag{2.2}
\]

and

\[
 r(e_{ab})\ne c,\qquad r(e_{bc})\ne a,\qquad r(e_{ca})\ne b.
 \tag{2.3}
\]

Condition (2.2) makes the three endpoint edges one directed star triangle
at every protected depth.  Condition (2.3) is precisely the local owner
condition from Proposition 2.8: the boundary entry lies in the common
((m-1))-set (R=Q\setminus\{a,b,c\}).  Hence the six source/successor
owners are distinct inside one atom.

Let (\mathcal A_H) be the 3-uniform hypergraph on all permutation states
whose edges are the protected (H)-atoms.

### Theorem 2.1 (exact state degree and codegree)

The hypergraph (\mathcal A_H) is exactly regular of degree

\[
 \boxed{d_H=(m-1)^3t_H^2.}
 \tag{2.4}
\]

Its maximum pair-codegree is

\[
 \boxed{\Delta_2(\mathcal A_H)=(m-1)t_H,\qquad
 \frac{\Delta_2}{d_H}=\frac1{(m-1)^2t_H}.}
 \tag{2.5}
\]

#### Proof

Fix (e=e_{ab}), with boundary entry (r).  The third endpoint (c) can
be any of the (m-1) elements of (Q\setminus\{a,b,r\}).  Once (c) is
fixed, a companion on (b\to c) may end its (P)-block at any of the
(m-1) allowed entries other than (a), and therefore has
((m-1)t_H) choices by (1.9).  The same count holds for the companion on
(c\to a).  This proves (2.4).

Two prescribed states lie in a common atom only if their flags agree and
their endpoint edges are two consecutive edges of one directed triangle.
The third endpoint is then forced.  If the two boundary conditions hold,
the third state has exactly ((m-1)t_H) choices; otherwise the codegree is
zero.  This proves (2.5). \(\square\)

By Lemma 1.1, an atom uses three distinct (BA)-orbits whenever (H\ge2).
Project (\mathcal A_H) to the 3-uniform multihypergraph
(\mathcal Q_H) on (BA)-orbits.

### Theorem 2.2 (exact orbit-pair overlap bound)

Let (\mathcal O\ne\mathcal O') and put

\[
 j(\mathcal O,\mathcal O')
 =|A_{\mathcal O}\setminus A_{\mathcal O'}|
 =|A_{\mathcal O'}\setminus A_{\mathcal O}|.
 \tag{2.6}
\]

The number of pairs (e\in\mathcal O,e'\in\mathcal O') that can occur
together in one protected atom is at most

\[
                         \boxed{2j(\mathcal O,\mathcal O')\le2m.}
 \tag{2.7}
\]

More precisely, at most (j) pairs have (b(e)=a(e')), and at most
(j) have (b(e')=a(e)).  Consequently

\[
 \deg_{\mathcal Q_H}(\mathcal O)=L(m-1)^3t_H^2,
 \tag{2.8}
\]

\[
 \deg_{\mathcal Q_H}(\mathcal O,\mathcal O')
 \le2j(\mathcal O,\mathcal O')(m-1)t_H,
 \tag{2.9}
\]

and

\[
 \boxed{
 \frac{\Delta_2(\mathcal Q_H)}{\deg(\mathcal Q_H)}
 \le\frac{2}{(m+1)(m-1)^2t_H}.}
 \tag{2.10}
\]

#### Proof

Two distinct directed edges of one directed triangle share an endpoint as
head-to-tail.  Consider first (b(e)=a(e')=x).  Necessarily

\[
 x\in B_{\mathcal O}\cap A_{\mathcal O'}
 =A_{\mathcal O'}\setminus A_{\mathcal O},
\]

which gives (j) possible labels (x).  For a fixed (x), the head phase
of (e) on the length-((m+1)) coordinate cycle and the tail phase of
(e') on the length-(m) cycle are fixed.  Equality of their protected
flags includes one ordered suffix symbol from each coordinate cycle.  It
therefore fixes the two remaining phases uniquely.  Hence at most one
state pair occurs for each (x).  The opposite head-to-tail orientation is
identical and uses
(A_{\mathcal O}\setminus A_{\mathcal O'}).  This proves (2.7).

Every state of an orbit has degree (2.4), and no atom contains two states
of one orbit, proving (2.8).  Each compatible state pair has codegree at
most (2.5); multiply by (2.7) to obtain (2.9), then use
(L=m(m+1)) and (j\le m) to obtain (2.10). \(\square\)

The extra factor (1/m) in (2.10), compared with the suffix-only estimate
in Proposition 4.4 of the previous note, comes from demanding that the two
endpoint edges actually be consecutive in a directed triangle.

## 3. An exact phase-varying factor of the entire state catalogue

The favourable local statistics are not merely heuristic.

### Theorem 3.1 (exact universal protected-atom factor)

For every (m\ge3) and every (0\le H\le m-1), the (n!) permutation
states can be partitioned exactly into protected (H)-atoms.

For (H=m-1), every atom cancels its nested switch divergence at every
depth.  For (H\ge2), the induced factor activates every (BA)-orbit and
its partner orbits necessarily vary with phase.

#### Proof

Work independently inside one flag (F), and put
(Q=[n]\setminus K), (|Q|=m+2).  For each ordered pair (a\ne b) in
(Q), the possible third endpoints and possible boundary labels are both
the same (m)-element set

\[
                         Q\setminus\{a,b\}.
\]

Choose a derangement

\[
 \delta_{a,b}:Q\setminus\{a,b\}\longrightarrow
 Q\setminus\{a,b\}.
 \tag{3.1}
\]

Assign every state on (a\to b) with boundary label (r) to the third
endpoint (c=\delta_{a,b}(r)).  By (1.9), there are exactly (t_H) such
states for every (r); since (\delta_{a,b}) is a bijection, there are
exactly (t_H) assigned states for every third endpoint (c).  The
derangement condition gives (r\ne c), which is (2.3).

Now fix one of the two cyclic orientations of an unordered triple
({a,b,c}).  There are exactly (t_H) available states assigned to
each of the three incidences

\[
 (a\to b;c),\qquad(b\to c;a),\qquad(c\to a;b).
\]

Match these three (t_H)-sets by arbitrary bijections, producing
(t_H) atoms.  Repeat for both orientations of every unordered triple.
Every directed-edge/third-endpoint slot is used exactly once, hence every
state with flag (F) is used exactly once.  Finally repeat independently
over all flags.

For (H\ge2), Lemma 1.1 puts the three states of every atom in distinct
orbits.  Since all states are used, all orbits are fully activated.  The
phase variation assertion follows quantitatively from Theorem 4.3 below.
\(\square\)

Theorem 3.1 is deliberately not called a rotor factor: using every state
violates middle ownership by a factorial multiplicity.  It proves exactly
that the (BA)-flow and protected-atom equations themselves are soluble.

## 4. Necessary Eulerian and congruence conditions at sparse density

Let (\mathscr S) be a family of active (BA)-orbits, (M=|\mathscr S|),
and suppose all (LM) of their states are partitioned into protected
atoms.  For a flag (F), let (D_F) be the directed multigraph whose arcs
are the endpoint edges of the selected states with flag (F).

### Theorem 4.1 (flagwise mod-(3) and Euler equations)

For every protected flag (F):

\[
 |E(D_F)|\equiv0\pmod3,
 \qquad
 d^+_{D_F}(x)=d^-_{D_F}(x)\quad(x\in[n]).
 \tag{4.1}
\]

Equivalently, if (B_H) is the flag-by-orbit incidence matrix and
(y=\mathbf1_{\mathscr S}), then

\[
                         B_Hy\equiv0\pmod3.
 \tag{4.2}
\]

If the states are part of an owner-transversal rotor circulation, then for
each underlying suffix set (K), the union of the (D_F) over flags with
underlying set (K) is an oriented simple graph.  Its arcs are partitioned
into directed triangles, in flag-homogeneous groups.  In particular it has
at most

\[
                         \binom{m+2}{2}
 \tag{4.3}
\]

arcs, and every one of its undirected vertex degrees is even.

#### Proof

Atoms never cross protected flags, and each atom contributes one directed
3-cycle to (D_F).  This proves (4.1)--(4.2).

For fixed (K), two endpoint arcs with the same unordered pair
({a,b}) have the same union colour (K\cup\{a,b}).  The
union-injectivity theorem for selected (A)-switches permits at most one
such arc, including across different ordered prefixes of (K).  Thus the
union is an orientation of a simple graph.  A triangle decomposition gives
(4.3) and even undirected degrees. \(\square\)

There is also a global condition which sees only the two coordinate-cycle
label sets (1.3).

### Theorem 4.2 (the active orbit cuts form a (1)-design)

For (x\in[n]), put

\[
 d_x=|\{\mathcal O\in\mathscr S:x\in A_{\mathcal O}\}|.
\]

Then

\[
                         \boxed{nd_x=mM\quad(x\in[n]).}
 \tag{4.4}
\]

Consequently (n\mid M), every coordinate lies in exactly (mM/n) of
the active (m)-sets (A_{\mathcal O}), and

\[
                         3\mid LM.
 \tag{4.5}
\]

#### Proof

By (1.4), an active orbit contributes all (m(m+1)) arcs of the directed
cut (A_{\mathcal O}\to B_{\mathcal O}).  Hence the global outdegree of
(x) is ((m+1)d_x), while its global indegree is (m(M-d_x)).
Summing the flagwise Euler equations gives equality of these quantities,
which is (4.4).  Since (\gcd(m,n)=1), (n\mid M).  Finally, the total
number (LM) of arcs is three times the number of atoms, proving (4.5).
\(\square\)

When (m\equiv1\pmod3), (L\not\equiv0\pmod3), but then
(n=2m+1\equiv0\pmod3), so (n\mid M) already supplies (4.5).  Thus the
global mod-(3) condition creates no additional asymptotic obstruction.

If the solution is exactly owner-transversal, every active orbit supplies
(2L) distinct source/successor owners and therefore

\[
                         2LM=W.
 \tag{4.6}
\]

Equations (4.4) and (4.6) impose divisibility which generally fails at
finite (m).  With an owner leave (\ell), they become

\[
 W-\ell=2LM,
 \qquad n\mid M.
 \tag{4.7}
\]

The least nonnegative residue allowed by (4.7) is below
(2Ln=O(m^3)=o(W)).  Hence these arithmetic conditions are real but are
not an asymptotic no-go.

### Theorem 4.3 (quantitative phase-variation supersaturation)

Let (\lambda_{\mathcal O,\mathcal O'}) be the number of selected atoms
containing both active orbits.  Then

\[
 \lambda_{\mathcal O,\mathcal O'}
 \le2j(\mathcal O,\mathcal O')\le2m,
 \tag{4.8}
\]

\[
 \sum_{\mathcal O'\ne\mathcal O}
 \lambda_{\mathcal O,\mathcal O'}=2L,
 \qquad
 \sum_{\mathcal O'\ne\mathcal O}
 j(\mathcal O,\mathcal O')\ge L.
 \tag{4.9}
\]

Every active orbit therefore has at least (m+1) distinct partner orbits.
Globally the interaction hypergraph uses at least

\[
 \frac{M(m+1)}2
 \tag{4.10}
\]

distinct orbit pairs and at least

\[
 \frac{M(m+1)}6
 \tag{4.11}
\]

distinct orbit triples.

#### Proof

Equation (4.8) is Theorem 2.2, because a state pair occurs in at most one
selected atom.  Every one of the (L) atoms through an orbit contributes
two partner incidences, proving the equality in (4.9).  Combine it with
(4.8) to obtain the inequality in (4.9) and at least
(2L/(2m)=m+1) partners.

There are (ML/3) atoms and hence (ML) orbit-pair incidences.  Each
distinct pair supports at most (2m) of them, giving (4.10).  A fixed
orbit triple also supports at most (2m) atoms, so division of (ML/3)
by (2m) gives (4.11). \(\square\)

This is the precise replacement for the failed three-orbit grid packet:
partner variation is not optional or sparse.  It must occur on
(\Theta(m)) partners per active orbit.  Theorem 3.1 shows that this
supersaturation demand is achievable.

Each connected component of the orbit interaction hypergraph separately
satisfies Theorem 4.2, because no atom crosses between components.

### Corollary 4.4 (component orders are multiples of \(n\))

Every connected component of a protected atom factor contains a multiple
of \(n=2m+1\) \(BA\)-orbits.  In particular, the smallest possible
phase-varying molecule has \(n\) orbits.

This already rules out every fixed three-orbit completion for \(m\ge2\),
without using the stronger ordered-deck rigidity of Corollary 4.6 in the
previous note.

The apparent next candidate, an \(n\)-orbit molecule, is also impossible
at protected height three.  The obstruction is an equality case of
Theorem 4.3.

### Lemma 4.5 (protected-edge refinement of the pair bound)

Assume \(H\ge3\), let
\[
 j=|A_{\mathcal O}\setminus A_{\mathcal O'}|>0,
\]
and let \(\chi_H(\mathcal O,\mathcal O')\) be the number of pairs of
phase ports which can occur together in a protected atom.  Then

\[
 \chi_H(\mathcal O,\mathcal O')
 \le
 \begin{cases}
  2\min\{j,\max(0,m-j-1)\},&m\text{ odd},\\[1mm]
  2\min\{j,m-j\},&m\text{ even}.
 \end{cases}
 \tag{4.12}
\]

#### Proof

Consider the oriented compatibility \(b(e)=a(e')=x\), for which
\(x\in A_{\mathcal O'}\setminus A_{\mathcal O}\).  The protected symbols
\(k_1,k_3\) occupy consecutive positions on the same coordinate cycle.

If \(m\) is odd, those positions lie on the length-\(m\) cycle.  Equality
of the two protected flags therefore exhibits a common directed edge of
the two cyclic orders on
\[
 A_{\mathcal O}\cap A_{\mathcal O'},
 \qquad |A_{\mathcal O}\cap A_{\mathcal O'}|=m-j.
\]
As \(x\) varies, these common directed edges are distinct: in
\(\mathcal O'\), the endpoint \(x\) fixes the phase immediately preceding
the protected directed edge.  A directed Hamilton cycle has at most
\(s-1\) edges wholly inside a proper \(s\)-vertex subset, so this
orientation contributes at most
\[
 \min\{j,\max(0,m-j-1)\}.
\]

If \(m\) is even, \(k_1,k_3\) lie on the length-\((m+1)\) cycle instead.
Their common directed edge lies in
\[
 B_{\mathcal O}\cap B_{\mathcal O'},
 \qquad |B_{\mathcal O}\cap B_{\mathcal O'}|=m+1-j,
\]
and now \(x=b(e)\) fixes the preceding phase in \(\mathcal O\).  The same
proper-subset argument gives at most \(m-j\) common directed edges, hence
at most \(\min\{j,m-j\}\) compatible pairs in this orientation.

The reverse head-to-tail orientation has the same bound.  Adding the two
orientations proves (4.12). \(\square\)

The same proof uses the whole ordered prefix.  Put
\[
 \ell_H=\left\lceil\frac H2\right\rceil-1
       =\left\lfloor\frac{H-1}{2}\right\rfloor .
\]
The protected symbols on the coordinate cycle containing \(k_1\) form a
directed path of \(\ell_H\) edges.  Hence the stronger all-\(H\) bound is
\[
 \chi_H(\mathcal O,\mathcal O')
 \le
 \begin{cases}
  2\min\{j,\max(0,m-j-\ell_H)\},&m\text{ odd},\\[1mm]
  2\min\{j,\max(0,m+1-j-\ell_H)\},&m\text{ even}.
 \end{cases}
 \tag{4.12a}
\]
Indeed a directed Hamilton cycle has at most \(s-\ell_H\) starting
positions for an \(\ell_H\)-edge path wholly inside one proper
\(s\)-vertex subset.  Lemma 4.5 is the case \(\ell_H\ge1\), weakened to
the first exposed edge.

There is a stronger packing refinement.  Put
\[
 h_H=\left\lceil\frac H2\right\rceil.
\]
In the oriented compatibility \(b(e)=a(e')=x\), the cross label \(x\)
is followed on the coordinate cycle containing \(k_1\) by all \(h_H\)
protected symbols from that cycle.  These symbols lie in the intersection
of the two coordinate-cycle label sets.  Distinct cross labels precede
disjoint intersection runs.  Consequently
\[
 \boxed{
 \chi_H(\mathcal O,\mathcal O')
 \le
 \begin{cases}
  2\min\{j,\lfloor(m-j)/h_H\rfloor\},&m\text{ odd},\\[1mm]
  2\min\{j,\lfloor(m+1-j)/h_H\rfloor\},&m\text{ even}.
 \end{cases}}
 \tag{4.12b}
\]
Unlike (4.12a), this uses the fact that every common path must begin
immediately after a distinct label outside the intersection.

### Theorem 4.6 (universal no-go for the minimal \(n\)-orbit molecule)

For \(m\ge3\) and \(H\ge3\), no family of exactly \(n=2m+1\) full
\(BA\)-orbits can have all its states partitioned into protected
nested-star atoms.

#### Proof

Suppose such a factor exists.  By Theorem 4.2, its \(n\) cut sets
\(A_{\mathcal O}\) form a \(1\)-\((n,m,m)\) design: every coordinate
belongs to exactly \(m\) cuts.

Fix one orbit \(\mathcal O\), and write
\[
 j_{\mathcal O'}=
 |A_{\mathcal O}\setminus A_{\mathcal O'}|.
\]
Double-counting incidences with the \(m\) coordinates in
\(A_{\mathcal O}\) gives
\[
 \sum_{\mathcal O'\ne\mathcal O}
 |A_{\mathcal O}\cap A_{\mathcal O'}|
 =m(m-1).
\]
There are \(2m\) other orbits, so
\[
 \boxed{\sum_{\mathcal O'\ne\mathcal O}j_{\mathcal O'}
 =2m^2-m(m-1)=m(m+1)=L.}
 \tag{4.13}
\]

On the other hand, if
\(\lambda_{\mathcal O,\mathcal O'}\) is the selected atom
pair-multiplicity, Theorem 4.3 gives
\[
 \sum_{\mathcal O'\ne\mathcal O}
 \lambda_{\mathcal O,\mathcal O'}=2L,
 \qquad
 \lambda_{\mathcal O,\mathcal O'}\le2j_{\mathcal O'}.
 \tag{4.14}
\]
Equations (4.13)--(4.14) force equality
\[
 \lambda_{\mathcal O,\mathcal O'}=2j_{\mathcal O'}
 \quad\text{for every }\mathcal O'\ne\mathcal O.
 \tag{4.15}
\]

If \(m\) is odd, Lemma 4.5 and (4.15) force
\[
 j_{\mathcal O'}\le\frac{m-1}{2}
 \quad\text{for every }\mathcal O'\ne\mathcal O.
\]
But (4.13) says their average is
\[
 \frac{L}{2m}=\frac{m+1}{2},
\]
a contradiction.

If \(m\) is even, Lemma 4.5 instead forces
\[
 j_{\mathcal O'}\le\frac m2
\]
for every partner, while the same average is \((m+1)/2\), again a
contradiction. \(\square\)

For the particular cyclic-wreath cut design, there is an even shorter
visible obstruction.  Opposite cuts are disjoint.  When \(m\) is odd,
the first protected suffix symbol lies in the length-\(m\) cycle, so
disjoint cuts cannot share even a height-one flag; when \(m\) is even,
height two already includes a symbol from that cycle.  Yet equality in
(4.14) would require the opposite pair to support \(2m\) atom
coincidences.

Combining Corollary 4.4 and Theorem 4.6, every connected protected atom
molecule has at least
\[
                         \boxed{2n=4m+2}
 \tag{4.16}
\]
active \(BA\)-orbits when \(H\ge3\).

Before the full protected-run constraint is imposed, the first
arithmetically possible component size is \(M=2n\).  Its cut ledger has a
useful exact form.  Theorem 4.11 below subsequently rules this size out
for odd \(m\) as soon as \(H\ge3\).

### Proposition 4.7 (the exact \(2n\)-orbit capacity ledger)

Suppose a protected component has \(M=2n\) orbits, and fix one orbit
\(\mathcal O\).  Then

\[
 \sum_{\mathcal O'\ne\mathcal O}
 j(\mathcal O,\mathcal O')=2L.
 \tag{4.17}
\]

Consequently the protected-edge capacity necessary for a factor is

\[
 \sum_{\mathcal O'\ne\mathcal O}
 f_m\bigl(j(\mathcal O,\mathcal O')\bigr)\ge L,
 \tag{4.18}
\]

where

\[
 f_m(j)=
 \begin{cases}
  \min\{j,\max(0,m-j-1)\},&m\text{ odd},\\
  \min\{j,m-j\},&m\text{ even}.
 \end{cases}
 \tag{4.19}
\]

Equivalently, in the odd case

\[
 \sum_{\mathcal O'\ne\mathcal O}
 (2j-m+1)_+\le L,
 \tag{4.20}
\]

and in the even case

\[
 \sum_{\mathcal O'\ne\mathcal O}
 (2j-m)_+\le L.
 \tag{4.21}
\]

#### Proof

Theorem 4.2 now gives coordinate degree \(2m\).  Hence

\[
 \sum_{\mathcal O'\ne\mathcal O}
 |A_{\mathcal O}\cap A_{\mathcal O'}|
 =m(2m-1).
\]

Subtract this from \(m(M-1)=m(4m+1)\) to get (4.17).
The selected pair multiplicities sum to \(2L\), while Lemma 4.5 bounds
them by \(2f_m(j)\), proving (4.18).  Finally
\(j-f_m(j)\) is respectively
\((2j-m+1)_+\) or \((2j-m)_+\); subtract (4.18) from (4.17).
\(\square\)

The scalar ledger (4.18) leaves genuine room at \(M=2n\); it does not
extend the universal no-go.  Two canonical designs nevertheless fail for
stronger reasons.

### Proposition 4.8 (doubled Hadamard/Paley cuts fail)

Let \(m\) be odd.  Suppose the \(2n\) active cuts are two copies of the
blocks of a symmetric

\[
 2\text{-}(2m+1,m,(m-1)/2)
\]

design, including the Paley/Hadamard difference-set design when it exists.
No choice of directed cyclic orders on those cuts can support a protected
atom factor of height \(H\ge3\).

#### Proof

Across the doubled design, every coordinate pair belongs to exactly
\(m-1\) active cuts.  For a directed label edge \(x\to y\), let \(r_{xy}\)
be the number of length-\(m\) coordinate cycles which use that directed
edge.  Thus

\[
 r_{xy}\le m-1,
 \qquad
 \sum_{x\ne y}r_{xy}=Mm.
 \tag{4.22}
\]

For odd \(m\), every compatible oriented phase pair exposes, through
\((k_1,k_3)\), a common directed edge of the two length-\(m\) cycles.
Therefore the total number \(ML\) of selected orbit-pair incidences is at
most

\[
 \sum_{x\ne y}r_{xy}(r_{xy}-1)
 \le(m-2)\sum_{x\ne y}r_{xy}
 =(m-2)Mm.
 \tag{4.23}
\]

But \(ML=Mm(m+1)>(m-2)Mm\), a contradiction. \(\square\)

### Proposition 4.9 (the coherent doubled cyclic-interval attempt fails)

Let the cut types be the \(n\) cyclic \(m\)-intervals of
\(\mathbb Z_n\), each used twice, and put on every cut the directed cyclic
order inherited from \(\mathbb Z_n\).  Assume \(H\ge3\) when \(m\) is
odd and \(H\ge4\) when \(m\) is even.  Even before imposing the
length-\((m+1)\) coordinate order or full flag equality, each orbit has
only

\[
                         8(m-2)
 \tag{4.24}
\]

compatible ordered partner phases visible in the length-\(m\) coordinate
cycles.  Since

\[
 8(m-2)<2m(m+1)=2L\qquad(m\ge3),
\]

this coherent doubled-interval construction cannot be a protected atom
factor.

#### Proof

For either shift direction and distance \(1\le d\le m-2\), the two
interval cycles have exactly one admissible entrance into a common
directed edge in each head-to-tail orientation.  At distances
\(m-1,m\) they have none.  There are two shift directions and two copies
of each partner cut, giving
\[
 2\text{ orientations}\times2\text{ directions}\times
 2\text{ copies}\times(m-2)=8(m-2).
\]
\(\square\)

Propositions 4.8--4.9 do not rule out every \(2n\)-orbit component.  They
show what a survivor must do:

* its cut design must have coordinate-pair concurrence at least \(m+2\)
  somewhere (for odd \(m\)); and
* its cyclic orders must concentrate their directed adjacencies on those
  high-concurrence pairs, while also matching the other coordinate-cycle
  suffix data.

This is substantially more structured than either a doubled symmetric
design or coherent cyclic intervals.

The full protected prefix gives one further general component-size bound.

### Theorem 4.10 (height-dependent orbit-molecule lower bound)

Let a connected protected component have \(M=kn\) active orbits, with
\(H\ge3\), and put
\[
 \ell_H=\left\lfloor\frac{H-1}{2}\right\rfloor,\qquad
 a_H=
 \begin{cases}
  m-\ell_H,&m\text{ odd},\\
  m+1-\ell_H,&m\text{ even}.
 \end{cases}
 \tag{4.25}
\]
Then necessarily
\[
                         \boxed{
 a_H\ge\frac{2(m+1)}{k+1}.}
 \tag{4.26}
\]

In particular, a \(2n\)-orbit component is impossible whenever
\[
 \ell_H>
 \begin{cases}
  (m-2)/3,&m\text{ odd},\\
  (m+1)/3,&m\text{ even}.
 \end{cases}
 \tag{4.27}
\]

At full protected height this forces at least \(3n\) orbits (up to the
displayed parity rounding).  For \(H=o(m)\), however, (4.26) gives no
improvement over the already proved \(2n\) lower bound.

#### Proof

The coordinate degree is \(km\).  Repeating the double count in
Theorem 4.6 gives, for every fixed orbit,
\[
 \sum_{\mathcal O'\ne\mathcal O}
 j(\mathcal O,\mathcal O')=kL.
 \tag{4.28}
\]
The all-\(H\) refinement (4.12a) says that half the available pair
capacity is at most
\[
 f(j)=\min\{j,(a_H-j)_+\}.
\]
For \(0\le j\le m\),
\[
 f(j)\le\frac{a_H}{2m-a_H}(m-j).
 \tag{4.29}
\]
Indeed the ratio \(f(j)/(m-j)\) increases up to the peak
\(j=a_H/2\) and decreases afterwards.

There are \(kn-1\) partners.  Using (4.28),
\[
 \sum_{\mathcal O'\ne\mathcal O}(m-j)
 =(kn-1)m-kL=m(km-1).
 \tag{4.30}
\]
An atom factor needs \(\sum f(j)\ge L=m(m+1)\).  Equations
(4.29)--(4.30) therefore imply
\[
 \frac{a_H}{2m-a_H}(km-1)\ge m+1.
\]
After collecting the \(a_H\)-terms, this is exactly
\[
 a_H(k+1)m\ge2m(m+1),
\]
which proves (4.26).  Substituting \(k=2\) gives (4.27). \(\square\)

The run-packing refinement (4.12b) gives the sharp component-scale
consequence relevant to growing protected height.

### Theorem 4.11 (linear-in-height orbit supersaturation)

Let a connected protected atom component have \(M=kn\) active
\(BA\)-orbits.  Put \(h_H=\lceil H/2\rceil\).  Then
\[
 \boxed{
 k\ge
 \begin{cases}
  h_H+1,&m\text{ odd},\\
  h_H,&m\text{ even}.
 \end{cases}}
 \tag{4.31}
\]

In particular:

* for odd \(m\), every height-\(3\) component has at least \(3n\)
  orbits, so **all** \(2n\)-orbit candidates are impossible;
* for protected height \(H\), an odd-\(m\) component has
  \(\Omega(nH)\) orbit vertices;
* at all depths, the minimum odd-\(m\) molecule has
  \(\Omega(mn)=\Omega(m^2)\) orbits.

#### Proof

For a fixed orbit, the general \(1\)-design double count is
\[
 \sum_{\mathcal O'\ne\mathcal O}j(\mathcal O,\mathcal O')=kL.
 \tag{4.32}
\]
The selected atom pair-multiplicities sum to \(2L\).  Divide (4.12b)
by two and sum over the partners.

If \(m\) is odd, the right side is at most
\[
 \frac1{h_H}\sum_{\mathcal O'\ne\mathcal O}(m-j)
 =\frac{m(km-1)}{h_H}.
 \tag{4.33}
\]
It must be at least \(L=m(m+1)\), so
\[
 km-1\ge h_H(m+1).
 \]
Since \(h_H<m\) in the allowed range, integrality gives \(k\ge h_H+1\).

If \(m\) is even, the analogous sum is
\[
 \frac1{h_H}\sum_{\mathcal O'\ne\mathcal O}(m+1-j)
 =\frac{(m+1)(k(m+1)-1)}{h_H}.
 \tag{4.34}
\]
Comparison with \(L=m(m+1)\) gives
\[
 k(m+1)-1\ge h_Hm,
 \]
whose integral consequence is \(k\ge h_H\). \(\square\)

## 5. The exact sparse owner-transversal system

The remaining gate can now be stated without de Bruijn flow rows.  Let
(y_{\mathcal O}\in\{0,1\}) activate a (BA)-orbit, and let
(z_\alpha\in\{0,1\}) select a protected atom.  Then the port equations
are

\[
 \boxed{
 \sum_{\alpha\ni e}z_\alpha=y_{\mathcal O(e)}
 \qquad(e\in S_n).}
 \tag{5.1}
\]

They say that an active orbit contributes all its (L) phases and an
inactive orbit contributes none.  Because active sets are unions of full
(BA)-orbits, (5.1) already implies exact alternating de Bruijn balance.

For a middle owner (X), let

\[
 c_X(\mathcal O)
 =|\{e\in\mathcal O:\kappa(e)=X\}|
  +|\{e\in\mathcal O:\kappa(Ae)=X\}|.
 \tag{5.2}
\]

The exact owner equations are

\[
 \boxed{
 \sum_{\mathcal O}c_X(\mathcal O)y_{\mathcal O}=1
 \qquad\left(X\in\binom{[n]}m\right).}
 \tag{5.3}
\]

An asymptotic compiler may replace the right side by (0) or (1) and
allow (o(W)) zeros.

The owner equations reveal a sharp parity obstruction which is invisible
in the endpoint/flag model.

### Theorem 5.1 (even-\(m\) internal owner collision)

Let \(\mathcal O\) be one full \(BA\)-orbit.  Its source-owner deck is
\[
 \mathcal X(\mathcal O)
 =\bigl\{\{x_1,\ldots,x_m\}: (x_1,\ldots,x_n)\in\mathcal O\bigr\},
 \tag{5.4}
\]
and its \(A\)-successor-owner deck is
\[
 \mathcal Y(\mathcal O)
 =\bigl\{\{x_2,\ldots,x_{m+1}\}: (x_1,\ldots,x_n)\in\mathcal O\bigr\}.
 \tag{5.5}
\]

If \(m\) is even, then
\[
                         \boxed{\mathcal X(\mathcal O)
                         =\mathcal Y(\mathcal O)}
 \tag{5.6}
\]
as multisets, and each deck contains \(L\) distinct owners.  Hence every
owner in their common deck is used twice by one active orbit.  No nonempty
union of full \(BA\)-orbits can be owner-transversal.

If \(m\) is odd, the two decks are disjoint and each contains \(L\)
distinct owners.  Thus a single orbit has \(2L\) internally distinct
owners; only cross-orbit collisions remain.

#### Proof

Let the label sets on the two coordinate cycles be \(A_{\mathcal O}\)
and \(B_{\mathcal O}\), of sizes \(m\) and \(m+1\).  The powers of \(BA\)
rotate the two coordinate cycles independently.

Write \(m=2r\).  Each of the position sets
\[
 \{1,\ldots,m\},\qquad\{2,\ldots,m+1\}
\]
meets the length-\(m\) position cycle in one cyclic interval of \(r\)
positions and meets the length-\((m+1)\) cycle in one cyclic interval of
\(r\) positions.  As the two phases range independently, both (5.4) and
(5.5) are therefore exactly the Cartesian deck
\[
 \{I_A(u,r)\cup I_B(v,r):
          u\in\mathbb Z_m,\ v\in\mathbb Z_{m+1}\}.
 \tag{5.7}
\]
This proves (5.6).  A proper cyclic interval in a cycle of distinct labels
determines its starting phase, so the \(L\) sets in (5.7) are distinct.

Now write \(m=2r+1\).  A source owner meets \(A_{\mathcal O}\) in
\(r+1\) labels and \(B_{\mathcal O}\) in \(r\), whereas an
\(A\)-successor owner has the reverse intersection sizes \(r\) and
\(r+1\).  The decks are therefore disjoint.  The same interval
injectivity proves that each has size \(L\). \(\square\)

For even \(m\), the obstruction is linear-sized rather than a divisibility
residue.  An atom-only alternating solution with \(M\) active orbits has
\(2LM\) owner occurrences but at most \(LM\) distinct owners before any
cross-orbit collision is counted.  Thus an \(o(W)\) owner leave cannot
repair it when \(2LM=(1-o(1))W\).  Connector transitions must break a
linear fraction of the full-\(BA\)-orbit structure.

For the rest of this section, the exact fractional statement remains true
for both parities.

### Proposition 5.2 (exact fractional feasibility)

The system (5.1)--(5.3) has an exact uniform fractional solution.  If

\[
 D_0=m!(m+1)!,\qquad p=\frac1{2D_0},
 \tag{5.8}
\]

then

\[
 y_{\mathcal O}=p,qquad z_\alpha=\frac{p}{d_H}
 \tag{5.9}
\]

satisfies every equation.

#### Proof

Every state lies in (d_H) atoms, so (5.1) holds.  The full permutation
catalogue has (D_0=n!/W) states in each middle-owner fibre.  The source
and (A)-successor occurrences therefore give total owner degree (2D_0),
so (5.3) holds as well. \(\square\)

The total fractional activation is

\[
 \frac{n!}{L}\,p=\frac{W}{2L},
\]

exactly the number of active orbits demanded by (4.6).  Thus there is no
fractional, degree, codegree, flag, endpoint-Euler, or phase-factor
obstruction.

## 6. Final status

The exact phase-varying \(BA\)-orbit lane survives only for odd \(m\).
For even \(m\), Theorem 5.1 closes the atom-only alternating model
statewise: every active orbit already repeats each of its owners.

**Proved here:**

* the exact flag/endpoint incidence model;
* exact state degrees and codegrees;
* the (2j\le2m) orbit-pair overlap bound;
* an explicit exact factor of the entire state catalogue into protected
  nested-star atoms;
* the flagwise mod-(3), Eulerian, and global (1)-design necessities;
* the (\Theta(m))-partner supersaturation forced on every active orbit;
* the universal \(n\)-orbit molecule no-go and the two canonical
  \(2n\)-orbit no-gos;
* the even-\(m\) internal owner-deck obstruction;
* exact uniform fractional feasibility of the combined port and owner
  equations.

**Still open for odd \(m\):** round the fractional point (5.9) to an
integral solution of (5.1)--(5.3), or to one with an \(o(W)\) owner leave,
while retaining the protected-height error budget.  Ordinary
fixed-uniformity nibble theory does not perform the all-or-none orbit
activation in (5.1).  Conversely, the fixed-partner rigidity of
Corollary 4.6 does not refute the required phase-varying solution:
Theorem 3.1 gives one at full density.

**Still open for even \(m\):** introduce a linear amount of non-\(BA\)
connector structure.  An \(o(W)\) perturbation of full \(BA\)-orbits
cannot overcome Theorem 5.1.

The next theorem should therefore target **sparse block rounding of the
explicit phase factor**, not another search for three-orbit packets and not
another local atom catalogue.

## 7. Finite audit

The construction in Theorem 3.1 was enumerated directly for the first two
nontrivial cases, using the cyclic derangement of the ordered set
`Q \ {a,b}` for every endpoint pair.  The audit checked that every
permutation state occurs once, all three states in an atom have the same
protected flag, and every boundary label differs from its assigned third
endpoint.

```text
{'m': 3, 'H': 2, 'states': 5040,   'flags': 42,  'atoms': 1680,   'covered': 5040}
{'m': 4, 'H': 2, 'states': 362880, 'flags': 504, 'atoms': 120960, 'covered': 362880}
```

The refined pair bound (4.12b) was also checked on \(100\) independent
random orbit pairs for every \(2\le H\le m-1\) and
\(3\le m\le6\).  The owner decks were enumerated for \(2\le m\le8\):
they coincide for every even \(m\) and are disjoint for every odd \(m\),
exactly as in Theorem 5.1.

These checks are verification of the explicit bookkeeping, not input to
the proof.
