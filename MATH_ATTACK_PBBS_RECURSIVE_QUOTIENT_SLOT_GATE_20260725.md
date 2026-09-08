# PBBS quotient residence: the exact recursive slot gate

Date: 2026-07-25

No computation or web search is used in this note.

## 0. Verdict

Put

\[
 N=2r+1,
 \qquad B=\operatorname{Cat}_r.
\]

The estimate

\[
 \overline\nu_H=O(B/N),
 \qquad H=\sqrt r\,\omega(r),
 \qquad H\log r=o(r),
\tag{0.1}
\]

is not proved or disproved below.  What is proved is the exact first gate
which an iterated peak-deletion proof has to cross.

Peak deletion does not send a return to a return with bounded multiplicity.
It sends a return to an **adjacent-particle passage**, and lifting that
passage depends on one Pascal slot which is absent from the pruned Dyck
root.  Retaining this slot gives an exact binomial lifting formula,
Theorem 3.1 below.  Forgetting it is a genuinely false step: there are
edge-disjoint quotient families of exponential size whose complete
two-level pruned return skeleton is identical.

Thus the first unsupported implication in a return-only recursion is

\[
 \text{edge-disjoint parent returns}
 \quad\Longrightarrow\quad
 \text{bounded-overlap pruned returns}.
\tag{0.2}
\]

The failure multiplicity is at least

\[
 {1\over9}
 \left({2^{r-1}-r\over r}-10(2r+1)^{10}\right)
\tag{0.3}
\]

for all sufficiently large \(r\).  Consequently a valid recursive proof of
(0.1) must prove a *binomially weighted adjacent-passage packing theorem*;
an induction only on the number or packing of lower same-label returns
cannot close the quotient gate.

## 1. Pascal slots in one peak-deletion fibre

Let \(D\in\mathcal D_r\), let

\[
 E=\partial D\in\mathcal D_d,
 \qquad k=\operatorname{pk}(E),
 \qquad p=2d+1,
 \qquad K=r-d-k.
\tag{1.1}
\]

The \(p\) equality particles of \(0D\), read from the distinguished one,
record the particle word

\[
 w=0E.
\tag{1.2}
\]

Label them by \(j\in\mathbb Z_p\), with \(j=0\) distinguished, and choose
integer lifts of their physical edge positions in cyclic order.  If \(q_j\)
is the clockwise physical-edge distance from particle (j-1) to particle
(j), put

\[
 \epsilon_j=\mathbf1_{\{w_{j-1}\ne w_j\}}.
\tag{1.3}
\]

Between two consecutive equality particles every edge is unequal, so its
bits alternate.  Therefore there is a unique (n_j\ge0) such that

\[
 \boxed{q_j=1+\epsilon_j+2n_j.}
\tag{1.4}
\]

Since the cyclic word (0E) has (k) transitions (01) and (k)
transitions (10),

\[
 \sum_j\epsilon_j=2k.
\tag{1.5}
\]

Using (sum_jq_j=N) in (1.4) gives

\[
 \boxed{\sum_{j\in\mathbb Z_p}n_j=K=r-d-k.}
\tag{1.6}
\]

### Lemma 1.1 (exact Pascal-slot parametrization)

For fixed (E\in\mathcal D_d), the map

\[
 D\longmapsto(n_0,n_1,\ldots,n_{p-1})
\tag{1.7}
\]

is a bijection from

\[
 \{D\in\mathcal D_r:\partial D=E\}
\]

to the weak compositions of \(K=r-d-k\) into \(p=2d+1\) parts.  In
particular,

\[
 \boxed{
 \#\{D\in\mathcal D_r:\partial D=E\}
 =\binom{K+p-1}{p-1}
 =\binom{r+d-k}{2d}.}
\tag{1.8}
\]

The seam slot between particle \(p-1\) and the distinguished particle is
\(n_0\).  Since every nonempty Dyck word \(E\) ends in zero, its two
recorded endpoint bits agree, and hence

\[
 \boxed{q_0=2n_0+1.}
\tag{1.9}
\]

#### Proof

The parity statement (1.4) follows by walking from one equal edge to the
next: each intervening unequal edge flips the current bit.  Equations
(1.5)--(1.6) then follow by summing.

For surjectivity and uniqueness, use the ordered-plane-tree contour
bijection.  The tree represented by (E) has (d+1) vertices, (d)
child edges, and therefore

\[
 \sum_v(\deg^+(v)+1)=2d+1=p
\]

ordered child slots.  A preimage under simultaneous leaf pruning is obtained
uniquely by inserting a string of new leaf children in every slot, with one
forced new child at each of the (k) old leaves.  After removing these
(k) forced children, the remaining number of new leaves is

\[
 (r-d)-k=K,
\]

distributed freely among the (p) slots.  In contour order these free
slot occupancies are exactly the (n_j)'s in (1.4).  This proves the
bijection and (1.8).  The final root slot lies between the predecessor and
the distinguished particle.  It is unforced when (d\ge1), and every
extra leaf there inserts two alternating physical edges.  This is (1.9).
\(\square\)

## 2. Exact dynamical lifting invariant

Run the canonical PBBS on the particle word \(0E\).  Let

\[
 \kappa_t(E)\in\mathbb Z_p
\]

be its omitted particle label at time \(t\), normalized by

\[
 \kappa_0(E)=0.
\tag{2.1}
\]

For \(j\in\mathbb Z_p\), put

\[
 C_j(t)=\#\{0\le u<t:\kappa_u(E)=j\}.
\tag{2.2}
\]

If \(x_j(t)\) is the physical edge occupied by equality particle \(j\),
Theorem 14.1 of the residence reduction gives the exact lift

\[
 \boxed{x_j(t)=x_j(0)+C_j(t),
 \qquad
 \lambda_t=x_{\kappa_t(E)}(t)+1.}
\tag{2.3}
\]

Here \(\lambda_t\) is the omitted physical coordinate in the rank-\(r\)
PBBS.

### Lemma 2.1 (return = predecessor count = seam slot)

Assume \(d\ge1\) and \(g<N\).  A lift \(D\) of \(E\) starts a consecutive
physical omitted-label return of gap \(g\) if and only if all of the
following hold:

\[
\begin{aligned}
 &\kappa_g(E)=p-1,                                      &&\tag{2.4}\\
 &\kappa_h(E)=0\text{ for some }1\le h<g,              &&\tag{2.5}\\
 &C_{p-1}(g)\text{ is positive and odd},               &&\tag{2.6}\\
 &n_0={C_{p-1}(g)-1\over2}.                            &&\tag{2.7}
\end{aligned}
\]

#### Proof

At time zero the distinguished particle moves into the physical edge whose
label is \(\lambda_0\).  A return before time \(N\) can only be made by its
immediate predecessor, and the distinguished particle must first be selected
again to vacate that edge.  This is exactly (2.4)--(2.5).

Choose integer lifts with

\[
 q_0=x_0(0)-x_{p-1}(0)>0.
\]

Using (2.3), the equality \(\lambda_g=\lambda_0\) is

\[
 x_{p-1}(0)+C_{p-1}(g)+1
 \equiv x_0(0)+1\pmod N.
\tag{2.8}
\]

Both \(C_{p-1}(g)\) and \(q_0\) lie strictly between zero and \(N\), so
(2.8) is the ordinary integer equality

\[
 C_{p-1}(g)=q_0.
\tag{2.9}
\]

Equation (1.9) turns (2.9) into (2.6)--(2.7).

Conversely, (2.4)--(2.7) imply \(\lambda_g=\lambda_0\) by (2.3).  Before
time \(g\), the predecessor has made fewer than \(q_0\) previous moves
whenever it is selected, so it has not yet entered the returned edge.  No
other particle can enter it because particle order is preserved.  A full
wrap is impossible in fewer than \(N\) total particle moves.  Condition
(2.5) says that the distinguished particle has vacated the edge.  Hence the
occurrence at time \(g\) is the first return.  \(\square\)

The important point is that the lower same-label return in (2.5) is not
enough.  The final adjacent-particle passage (2.4), its predecessor count
(2.6), and the parent seam slot (2.7) are independent data which a
return-only induction discards.

## 3. Exact binomial lifting formula

For \(E\in\mathcal D_d\), define

\[
 b_g(E)=C_{p-1}(g)
       =\#\{0\le u<g:\kappa_u(E)=p-1\}.
\tag{3.1}
\]

Let \(\mathcal A_g(d)\) be the set of \(E\in\mathcal D_d\) satisfying
(2.4)--(2.6), and put

\[
 s_g(E)={b_g(E)-1\over2}.
\tag{3.2}
\]

### Theorem 3.1 (weighted adjacent-passage recursion)

Let \(R_g(r)\) be the number of normalized semilength-\(r\) Dyck roots
which start a consecutive omitted-label return of gap \(g<N\).  Then

\[
 \boxed{
 R_g(r)=
 \sum_{d=1}^{r-1}
 \ \sum_{E\in\mathcal A_g(d)}
 \binom{r+d-\operatorname{pk}(E)-s_g(E)-1}{2d-1},}
\tag{3.3}
\]

where a binomial coefficient is zero when its lower argument is negative
or exceeds its upper argument.

#### Proof

Fix \(E\in\mathcal A_g(d)\).  Lemma 2.1 fixes precisely one Pascal slot,

\[
 n_0=s_g(E).
\]

The other \(p-1=2d\) slots form a weak composition of

\[
 K-s_g(E)=r-d-\operatorname{pk}(E)-s_g(E).
\]

The number of choices is therefore

\[
 \binom{K-s_g(E)+p-2}{p-2}
 =\binom{r+d-\operatorname{pk}(E)-s_g(E)-1}{2d-1}.
\]

Different cores or slot vectors give different parent Dyck roots by Lemma
1.1.  Summing proves (3.3).  \(\square\)

Formula (3.3) is the exact recursive quotient gate.  The required child
statistic is not \(R_h(d)\): it is the weighted adjacent-passage set
\(\mathcal A_g(d)\), refined by the predecessor occupation \(b_g(E)\).
The weights are literal Pascal coefficients.

For orientation, the two first nontrivial cases reproduce the known exact
counts.

* For gap five, the unique child core is \(E=10\), with
  \(d=k=1\) and \(s_5(E)=0\).  Formula (3.3) gives
  
  \[
   R_5(r)=\binom{r-1}{1}=r-1.
  \]

* For gap seven, the child cores are
  
  \[
   E_d=(10)^{d-2}1100,
   \qquad d\ge2.
  \]
  
  Here \(\operatorname{pk}(E_d)=d-1\), \(b_7(E_d)=1\), and
  \(s_7(E_d)=0\).  Hence the defect-\(d\) fibre is
  
  \[
   \binom r{2d-1},
  \]
  
  and summing gives \(R_7(r)=2^{r-1}-r\).

## 4. Exponential collapse of edge-disjoint quotient intervals

The preceding gap-seven fibres give a quantitative obstruction to
unweighted recursive charging.

### Theorem 4.1 (edge-disjoint families with one pruned skeleton)

For every sufficiently large \(r\), there is a \(d\ge2\) and a family
\(\mathcal P_{r,d}\) of pairwise quotient-edge-disjoint gap-seven intervals
such that

\[
 \boxed{
 |\mathcal P_{r,d}|
 \ge {1\over9}
 \left({2^{r-1}-r\over r}-10(2r+1)^{10}\right).}
\tag{4.1}
\]

Every start root \(D\) in this family satisfies

\[
 \partial D=E_d=(10)^{d-2}1100,
 \qquad
 \partial^2D=10.
\tag{4.2}
\]

Moreover, under the PBBS semiconjugacy all intervals in the family map to
the same ordered gap-five return trace based at \(E_d\), and after a second
deletion to the same rank-one return trace.

#### Proof

The gap-seven classification and Theorem 3.1 give exactly

\[
 \binom r{2d-1}
\tag{4.3}
\]

starts over the core \(E_d\).  Since

\[
 \sum_{d\ge2}\binom r{2d-1}=2^{r-1}-r
\]

and there are at most \(r\) admissible \(d\)'s, choose \(d\) with

\[
 \binom r{2d-1}\ge{2^{r-1}-r\over r}.
\tag{4.4}
\]

A quotient \(\tau\)-cycle of length at most five comes from a quotient
\(\phi\)-cycle of length at most ten.  The ordered-voltage itinerary bound
therefore places at most

\[
 10N^{10}
\tag{4.5}
\]

quotient states on all such short cycles.  Discard them.  On every remaining
cycle, a gap-seven interval is an ordinary interval of five consecutive
quotient edges.  One such interval meets intervals starting at at most nine
edge positions, including its own start.  Greedy selection therefore keeps
at least one ninth of the surviving starts.  Equations (4.4)--(4.5) give
(4.1).

All starts in the chosen fibre have first pruned core \(E_d\).  Its particle
itinerary has the root label at times zero and five and its predecessor at
times two and seven, so every parent return maps to the same ordered
gap-five child trace.  Finally

\[
 \partial E_d=10,
\]

which proves (4.2) and the second collapse.  \(\square\)

Thus even after fixing the child rank \(d\), the pruned trace, both selected
particle labels, and the complete two-level return skeleton, a single child
certificate receives exponentially many mutually edge-disjoint parent
intervals.  The missing information is precisely the Pascal slot vector of
Lemma 1.1.

## 5. The exact remaining recursive assertion

For a fixed odd gap \(g\), its quotient interval has

\[
 L_g={g+3\over2}
\]

consecutive edges.  On long quotient cycles, a greedy packing selects at
least one interval out of every \(2L_g-1=g+2\) starts.  Consequently (0.1)
would in particular force, for every \(g\le2H-1\),

\[
 \sum_{d=1}^{r-1}
 \ \sum_{E\in\mathcal A_g(d)}
 \binom{r+d-\operatorname{pk}(E)-s_g(E)-1}{2d-1}
 =O\!\left({gB\over N}\right)+\exp(o(r)).
\tag{5.1}
\]

The left side is exactly \(R_g(r)\), not an upper surrogate.  Equation
(5.1) is therefore a necessary weighted adjacent-passage anticoncentration
estimate at the correct \(1/N\) quotient scale.

No statement in Sections 14--18 of the residence reduction proves (5.1).
The height theorem remembers only that the root particle repeats; it drops
the final predecessor condition and the Pascal coefficient in (3.3).
Conversely, Theorem 4.1 shows that replacing the weighted passage data by a
bounded-load charge to the repeated child return is false by an exponential
factor.

Hence the exact recursive boundary is:

\[
 \boxed{
 \text{prove a binomially weighted adjacent-passage packing theorem, or
 retain the full slot vector throughout the recursion.}}
\tag{5.2}
\]

Peak deletion by itself supplies a semiconjugacy, not the \(1/N\)
anticoncentration needed for (0.1).
