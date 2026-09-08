# The two-coordinate collar: inherited ports and the exact side-forest gate

Date: 2026-07-31  
Status: exact all-(n) reduction and literal positive constructions for
(n=3,4).  The two punctured side forests remain open uniformly in (n).

## 0. Verdict

The five-flow fractional recursion in Theorem 5.3 of
`MATH_THEOREM_CATALAN_BALANCED_SUBCUBE_RESERVE_AND_EXACT_COLLAR_DEFECT_20260731.md`
has a simpler integral middle than Theorem 6.1 initially suggests.

Orient every path of the child Catalan linear matching (F).  For **any**
set (Q\subseteq F), use the tail and head of the removed child edge as its
two seam ports:

\[
                    p^-(U_q)=t_q,\qquad p^+(L_q)=h_q. \tag{0.1}
\]

Both port maps are automatically injective and legal.  More importantly,
after an edge (q=t_qh_q) is removed from the central trace, its two seam
edges put one incidence back at (t_q) and one at (h_q).  The physical
degree of every central-trace vertex is therefore **exactly its old degree
in (F)**.  The zero-slack-looking middle collision problem disappears.

The complete recursion is now equivalent to two punctured saturating
side forests and one ordinary contracted attachment-forest test.  This is
strictly narrower than a new four-resource matching theorem.

The reduction is realized literally for child parameters (n=3) and
(n=4); adjoining the child gives Catalan linear matchings at parameters
(4) and (5).  These are finite validations, not an all-(n) proof.

## 1. The five sectors

Let the core ground set (R) have size (2n), and add collar coordinates
(c,z).  Reserve trace ({c}).  Put

\[
 M=\binom{2n}{n},\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad C=M-P,\quad R_0=N-C.          \tag{1.1}
\]

The five outer flows have sizes

\[
\begin{array}{c|ccccc}
\text{trace transition}&0\to0&0\to z&z\to z&z\to cz&cz\to cz\\ \hline
\text{size}&P&C&R_0&C&P.
\end{array}                                           \tag{1.2}
\]

Let (F) be an oriented Catalan linear matching at parameter (n).  Its
physical lift is a path forest on the rank-(n) core sets.  An atom
(q\in F) has lower and upper colours (L_q,U_q) and oriented physical
edge

\[
                         t_q\longrightarrow h_q,
 \qquad L_q=t_q\cap h_q,\quad U_q=t_q\cup h_q.         \tag{1.3}
\]

Choose (Q\subseteq F) of size (C), so (F-Q) has (R_0) edges.

## 2. Port inheritance

### Theorem 2.1 (the central trace is automatic)

For every (Q\subseteq F), define (0.1).  Then:

1. (p^-) and (p^+) are injective;
2. (p^-(U_q)\subset U_q) and (L_q\subset p^+(L_q));
3. in the union of the retained (z\to z) edges and the two seam families,
   every rank-(n) core vertex has physical degree exactly its degree in
   (F), hence at most two; and
4. the tail and head middle roles are individually injective on the seam
   ports.

#### Proof

Orient each component of (F) as a directed path.  Every physical vertex
is the tail of at most one edge and the head of at most one edge.  Therefore
the two maps in (0.1) are injective.  Both endpoints of a diamond lie
strictly between its lower and upper colours, proving containment.

For (q\notin Q), its old incidence at each of (t_q,h_q) remains on the
central trace.  For (q\in Q), that internal edge is deleted, while the
left seam is incident with (t_q) and the right seam with (h_q).  Thus
every incidence of every old edge is replaced one-for-one.  This proves
the degree identity.  The directed-path orientation proves the last
claim. \(\square\)

This argument uses no Hall theorem and imposes no shape condition on
(Q).

## 3. The two punctured side problems

The complement of the tail image and the complement of the head image are

\[
\begin{aligned}
 D^-&=\binom Rn\setminus\{t_q:q\in Q\},\\
 D^+&=\binom Rn\setminus\{h_q:q\in Q\}.
\end{aligned}                                         \tag{3.1}
\]

Both have size (P).  Equivalently,

\[
\begin{aligned}
 D^-&=(\text{vertices which are no tail of }F)
       \sqcup\{t_q:q\in F-Q\},\\
 D^+&=(\text{vertices which are no head of }F)
       \sqcup\{h_q:q\in F-Q\}.                       \tag{3.2}
\end{aligned}
\]

The left side asks for a perfect containment matching

\[
 \mathcal D^-:D^-\longrightarrow\binom R{n+2},        \tag{3.3}
\]

and the right side for the dual matching

\[
 \mathcal D^+:\binom R{n-2}\longrightarrow D^+.      \tag{3.4}
\]

Let (G^-,G^+) be their lifted graphs on ranks (n+1,n-1), respectively.
The seam anchor sets are

\[
 B^- =\{U_q:q\in Q\}\subseteq\binom R{n+1},\qquad
 B^+ =\{L_q:q\in Q\}\subseteq\binom R{n-1}.          \tag{3.5}
\]

### Theorem 3.1 (exact degree criterion)

The full five-sector lift has maximum degree at most two if and only if

\[
\begin{array}{ll}
 \Delta(G^-)\le2,&d_{G^-}(u)\le1\quad(u\in B^-),\\
 \Delta(G^+)\le2,&d_{G^+}(l)\le1\quad(l\in B^+).
\end{array}                                           \tag{3.6}
\]

#### Proof

The three middle trace banks (0,z,cz) are disjoint.  Theorem 2.1 handles
the (z)-bank.  A vertex in (B^-) receives one additional left seam
incidence and no other (0)-bank vertex does.  This gives the first row;
the other is dual. \(\square\)

Thus the outer Hall requirements and the physical side capacities are one
well-defined *punctured saturating forest* problem on each shore.

### 3.1 The diagonal incidence gates are dual common bases

It is useful to remove an ambiguity here.  Theorem 2.1 makes the central
(z)-bank degrees automatic, but it does **not** make (3.3)--(3.4)
automatic.

Let ({\cal T}_{\uparrow}) be the transversal matroid on
(\binom Rn) in which a family is independent when it can be matched to
distinct rank-((n+2)) supersets.  Let ({\cal T}_{\downarrow}) be the
dual-direction transversal matroid in which a family of rank-(n) sets can
be matched to distinct rank-((n-2)) subsets.  Both have rank (P).
Consequently

\[
 \begin{aligned}
 D^-\text{ satisfies (3.3)}&\iff
        I^-:=\{t_q:q\in Q\}\text{ is a basis of }{\cal T}_{\uparrow}^*,\\
 D^+\text{ satisfies (3.4)}&\iff
        I^+:=\{h_q:q\in Q\}\text{ is a basis of }{\cal T}_{\downarrow}^*.
                                                               \tag{3.7}
 \end{aligned}
\]

Pull the two dual matroids back to the common edge set (F) through the
injective tail and head maps.  Call the resulting rank-(C) matroids
({\cal A}_F,{\cal B}_F).  The exact coupled diagonal-incidence gate is

\[
                   \boxed{Q\text{ is a common basis of }
                          {\cal A}_F\text{ and }{\cal B}_F.}     \tag{3.8}
\]

By the matroid-intersection theorem, such a (Q) exists if and only if

\[
 r_{{\cal A}_F}(S)+r_{{\cal B}_F}(F\setminus S)\ge C
                  \qquad(S\subseteq F).                       \tag{3.9}
\]

Equation (3.9), not ordinary Hall on either diagonal separately, is the
first integral gate.

### Theorem 3.2 (each diagonal is individually extendable)

For every (n\ge3), every family of at most
(K=\operatorname {Cat}_n) rank-(n) sets has both

* an injection to distinct rank-((n-2)) subsets; and
* an injection to distinct rank-((n+2)) supersets.

In particular, both pulled-back matroids in (3.8) really have rank (C):
there is a set (Q^-) satisfying the left diagonal gate and, possibly a
different set (Q^+), satisfying the right diagonal gate.

#### Proof

For (n=3), a family of (t\le K_3=5) triples has a two-step lower
shadow equal to its coordinate union.  If that union had size below (t),
then all (t) triples would lie in at most (t-1) coordinates; direct
comparison with \(\binom{t-1}{3}<t\) for (1\le t\le5) is a
contradiction.  Hall applies, and complementation gives the upper case.

Now let (n\ge4) and
({\cal E}\subseteq\binom{[2n]}n), (|{\cal E}|\le K).  The exact
comparison

\[
 K={1\over n+1}\binom{2n}n
 \le \binom{2n-2}n                                    \tag{3.10}
\]

is equivalent to (n^2-4n+1\ge0), and hence holds for (n\ge4).
Write (|{\cal E}|=\binom xn) in the generalized-binomial notation of
Kruskal--Katona.  Then (x\le2n-2), and its two-step lower shadow has size
at least

\[
 \binom{x}{n-2}
 =\binom xn {n(n-1)\over(x-n+1)(x-n+2)}
 \ge |{\cal E}|.                                      \tag{3.11}
\]

The same inequality holds for every subfamily of ({\cal E}), so Hall
gives the lower injection.  Complementation gives the upper injection.

For the application, the vertices which are no tail of (F) form a
family of exactly (K) sets.  The upper injection says this family is
independent in ({\cal T}_{\uparrow}), so it extends to a basis (D^-)
of size (P).  Its complement is contained in the tail image and is a
basis of ({\cal T}_{\uparrow}^*), producing (Q^-).  The head argument
is dual. \(\square\)

The last sentence is deliberately only **individual** extendability.
Kruskal--Katona supplies no reason that (Q^-=Q^+), and hence does not
prove (3.8).  Even a common basis would settle only outer incidence; the
degree rows (3.6) and topology row (4.2) remain.

## 4. Exact topology criterion

Assume (3.6) and assume (G^-,F-Q,G^+) are forests.  Contract every
component of their disjoint union.  For each (q\in Q), retain the two
seam edges

\[
              U_q-t_q,\qquad h_q-L_q                 \tag{4.1}
\]

between the corresponding contracted components.  Call the resulting
tripartite multigraph (Gamma_Q).

### Theorem 4.1 (contracted attachment forest)

The five-sector physical lift is a linear forest if and only if (3.6)
holds and

\[
                              \Gamma_Q\text{ is a forest}.             \tag{4.2}
\]

Loops and parallel pairs in (Gamma_Q) count as cycles.

#### Proof

Before adding the seams, the three trace banks are a disjoint union of
forests.  Adding (4.1) changes cycle rank by exactly the cycle rank of the
component-contracted multigraph.  This is the usual contraction identity

\[
 \beta(G_0+E)=\beta(G_0)+\beta(\Gamma_Q)=\beta(\Gamma_Q).
\]

The degree statement is Theorem 3.1. \(\square\)

A useful sufficient condition is that every component of each side forest
contains at most one seam anchor.  Then the side components are leaves in
(Gamma_Q), so (4.2) follows from the fact that (F-Q) is a forest.  This
condition is not necessary and is too strong in the smallest cases.

### Proposition 4.2 (Catalan component charge)

Each side forest has (N) vertices and (P) edges, hence (N-P)
components, and it carries (C) seam anchors.  If (c_j) is the number of
components containing exactly (j) anchors, then

\[
 \boxed{\sum_{j\ge0}(j-1)c_j=C-(N-P)=M-N=K.}          \tag{4.3}
\]

In particular, if every component has at most two anchors, then

\[
                              c_2-c_0=K.              \tag{4.4}
\]

#### Proof

Sum (j-1) over all components.  The sum of the (j)'s is the number
(C) of anchors, while the number of summands is (N-P).  The last two
equalities are the binomial definitions. \(\square\)

This is the correct recursive topology ledger.  The more attractive claim
"exactly one double-anchor side component per child path" is false even in
the positive finite fixtures.  At (n=3) both shores have histogram
(1^4 2^5), but four double components use two anchors from the same long
child path.  At (n=4), the minus shore has (1^{14}2^{14}), whereas the
plus shore has

\[
                              0^1 1^{12}2^{15}.        \tag{4.5}
\]

Both give charge (K=14), and the complete attachment graph is still a
forest.  Hence the state to preserve is bounded anchor load plus signed
Catalan excess charge, not a canonical pairing with child components.

## 5. Positive finite realizations

The independent audit constructs the five sectors literally.

* At (n=3), retain one child edge and move the other fourteen.  Both side
  matchings satisfying (3.6) are found by exact backtracking, and
  (Gamma_Q) is a forest.  Adjoining the child gives (56) edges in
  (14=\operatorname{Cat}_4) paths.
* At (n=4), use the authenticated (14)-path child forest and retain the
  terminal edge of every path.  Thus (|F-Q|=14=R_0).  The two exact side
  matchings again satisfy (3.6), and the complete lift has (210) edges in
  (42=\operatorname{Cat}_5) paths.

These constructions verify every lower colour, upper colour, physical
degree and cycle directly.  They show that the integral five-flow pattern
is not merely fractional at its first two nontrivial parameters.

## 6. Remaining theorem

The exact all-(n) target is now:

> **Two-coordinate punctured-side theorem.**  Every child Catalan path
> forest can be oriented, and has a set (Q\subseteq F) of size
> (C=\operatorname{Cat}_{n+1}), for which (3.3)--(3.4) admit side forests
> satisfying (3.6) and the contracted attachment condition (4.2).

It would suffice to prove this for one recursively supplied child forest,
not for every (F).  This theorem plus the base cases proves Catalan Linear
Matching for every parameter by induction.

The theorem is an integral interlacing statement.  Ordinary inclusion Hall
alone proves neither the side degree caps nor (4.2), while the inherited
port lemma means no additional central four-resource theorem is needed.

## 7. Trace-matrix warning and a backup collar object

The raw trace constraint matrix is not totally unimodular.  Already on a
four-coordinate collar ((a=2)), fix a trace (S) with three absent
coordinates (x,y,z).  The three (z=2) columns adding
({x,y},\{x,z},\{y,z}) and the three intermediate-trace rows
(S+x,S+y,S+z) contain

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
 \qquad |\det|=2.                                    \tag{7.1}
\]

Thus there is no raw network-matrix/TU shortcut.

There is nevertheless a useful finite backup.  For (a=2,3,4), exact
cover finds an SCD of (B_{2a}) having the prescribed balanced set (A)
as a singleton, such that every off-chain corner of every consecutive
two-step chain window is distinct and avoids (A).  At (a=1) this is
impossible: the unique other length-two chain has (A) as its off-chain
corner.  These punctured turn-rainbow SCDs make every pure (z=2) collar
layer collision-free.  They do not by themselves settle its interaction
with the (z=0) and (z=1) sectors, so the five-flow theorem above remains
the shorter primary target.
