# NRFC as an owner--flag transversal with an exact Hall cycle-cover cut

Date: 2026-08-01  
Lane: R, integral monotone-rotor sequel  
Status: unconditional structural theorem.  It identifies exactly what the
full coordinate symmetry proves at one copy and isolates the first remaining
integral cut.  It does not prove NRFC, a physical owner factor, residence,
upper shadows, or a compiler theorem.

## 1. States and the literal transition relation

Fix

\[
                    k\ge r>d\ge1.
\]

For an age type \(c=(c_0,\ldots,c_d)\), with \(c_0>0\), \(c_i\ge0\),
and \(\sum_i c_i=r\), let \(\Omega_c\) be the set of ordered disjoint
tuples

\[
 X=(X_0,\ldots,X_d),\qquad |X_i|=c_i,
 \qquad T(X):=\dot\bigcup_iX_i\in\binom{[k]}r.
\]

For types \(c,c'\), put \(c\leadsto c'\) when

\[
                    c'_{i+1}\le c_i\qquad(0\le i<d).       \tag{1.1}
\]

For \(X\in\Omega_c\) and \(Y\in\Omega_{c'}\), the literal transition is

\[
                    Y_{i+1}=X_i\setminus Y_0
                         \qquad(0\le i<d).                 \tag{1.2}
\]

This is the owner-changing version of the age recurrence.  Mere inclusion
\(Y_{i+1}\subseteq X_i\) is enough only when the common owner has already
been fixed.  Throughout this note, compatibility means the equality (1.2).

Put

\[
                         a_i=c_i-c'_{i+1}\quad(0\le i<d).  \tag{1.3}
\]

The sum identity

\[
                         c'_0=c_d+\sum_{i<d}a_i             \tag{1.4}
\]
will be used repeatedly.

## 2. Exact terminal-star geometry and biregular degrees

### Theorem 2.1 (fixed-source terminal-star theorem)

Assume (1.1), and fix \(X\in\Omega_c\), with owner \(T=T(X)\).  The
owners of literal successors of type \(c'\) are exactly

\[
 \mathcal N(X)=
 \left\{(T\setminus D)\cup E:
 D\subseteq X_d,\ E\subseteq[k]\setminus T,\ |D|=|E|\right\}.       \tag{2.1}
\]

For a fixed member \((T\setminus D)\cup E\) of (2.1), the number of
successor partitions is

\[
                         \prod_{i=0}^{d-1}\binom{c_i}{c'_{i+1}}.     \tag{2.2}
\]

Consequently

\[
 |\mathcal N(X)|
   =\sum_{p\ge0}\binom{c_d}{p}\binom{k-r}{p}
   =\binom{k-r+c_d}{c_d},                                    \tag{2.3}
\]

and the source degree in the full labelled compatibility graph is

\[
 D^+_{c,c'}=\binom{k-r+c_d}{c_d}
             \prod_{i=0}^{d-1}\binom{c_i}{a_i}
        =\binom{k-r+c_d}{c_d}
             \prod_{i=0}^{d-1}\binom{c_i}{c'_{i+1}}.          \tag{2.4}
\]

#### Proof

Choose the survivor \(Y_{i+1}\subseteq X_i\) of size \(c'_{i+1}\)
independently for every \(i<d\).  The complement
\(X_i\setminus Y_{i+1}\), of size \(a_i\), is forced into the refreshed
cell \(Y_0\).  By (1.4), exactly \(c_d\) further elements must enter
\(Y_0\), and they can be any \(c_d\)-subset of

\[
                         X_d\ \dot\cup\ ([k]\setminus T).
\]

If this subset contains \(X_d\setminus D\) and the outside set \(E\),
then necessarily \(|D|=|E|\), and the new owner is precisely
\((T\setminus D)\cup E\).  Conversely every such choice satisfies (1.2).
This proves (2.1), (2.2), and (2.4); (2.3) is Vandermonde's identity.
\(\square\)

The important geometric correction is that (2.1) is a **terminal-star**,
not a full Johnson ball: only elements of the terminal cell \(X_d\) may
leave the old owner.

### Theorem 2.2 (global labelled biregularity)

The directed bipartite graph \(\Gamma_{c,c'}\) from \(\Omega_c\) to
\(\Omega_{c'}\), with edges (1.2), is biregular.  Besides (2.4), its target
degree is

\[
 D^-_{c,c'}=\binom{k-r+c_d}{c_d}
 {c'_0!\over c_d!\prod_{i=0}^{d-1}a_i!}.                     \tag{2.5}
\]

Moreover

\[
 |\Omega_c|D^+_{c,c'}=|\Omega_{c'}|D^-_{c,c'},
 \qquad
 |\Omega_c|={k!\over(k-r)!\prod_i c_i!}.                    \tag{2.6}
\]

Hence every \(S\subseteq\Omega_c\) obeys the normalized expansion bound

\[
 { |N_{\Gamma}(S)|\over|\Omega_{c'}|}
       \ge { |S|\over|\Omega_c|}.                            \tag{2.7}
\]

#### Proof

Fix \(Y\in\Omega_{c'}\).  Choose disjoint subsets
\(R_i\subseteq Y_0\) of sizes \(a_i\).  There are

\[
                         {c'_0!\over c_d!\prod_i a_i!}
\]

ways to do this, leaving a set of size \(c_d\) inside \(Y_0\).  The old
terminal cell \(X_d\) can be any \(c_d\)-subset of that leftover set
together with \([k]\setminus T(Y)\), giving the binomial factor in (2.5).
Set \(X_i=Y_{i+1}\dot\cup R_i\) for \(i<d\).  These choices are exactly
the predecessors satisfying (1.2), proving (2.5).  Substitution gives
(2.6).  Counting the edges from \(S\) into its neighborhood gives
\(D^+|S|\le D^-|N(S)|\), which is (2.7). \(\square\)

Theorem 2.2 is the precise source of the invariant fractional lift and of
all denominator-cleared full-orbit multicovers.  It does not select one
state in each owner fibre.

## 3. What one-step owner Hall gets for free

Suppose distinct-owner states \(X_v\), \(v\in V\), have already been
chosen, and each next role \(v^+\) has a type legally following the type of
\(X_v\).  Form the role-to-owner graph

\[
                         v\sim T'\quad\Longleftrightarrow
                         T'\in\mathcal N(X_v).                \tag{3.1}
\]

### Corollary 3.1 (exact one-step Hall theorem)

A choice of pairwise distinct next owners exists if and only if

\[
                 \left|\bigcup_{v\in A}\mathcal N(X_v)\right|
                         \ge |A|\qquad(A\subseteq V).         \tag{3.2}
\]

If the present owners \(T(X_v)\) are pairwise distinct, (3.2) always holds.

#### Proof

The equivalence is Hall's theorem.  By (2.1),
\(T(X_v)\in\mathcal N(X_v)\) (take \(D=E=\varnothing\)).  Thus
\(v\mapsto T(X_v)\) is already a matching when the current owners are
distinct.  After an owner is chosen, (2.2) supplies a compatible partition.
\(\square\)

This automatic result is strictly one-step.  Reusing the current-owner
matching around a nontrivial role cycle would force all roles on that cycle
to have the same owner, contradicting owner simplicity.  It cannot be
iterated without retaining the chosen state at both its incoming and
outgoing transition.

## 4. Exact NRFC min--max formulation

Fix an aggregate role template \((U,c,J)\), \(|U|=W=\binom kr\), where
\(c(u)\) is the type of role \(u\), and \(J(u)\) is its set of marked
prefix indices.  As in the aggregate theorem, if zero age classes cause
two indices to offer the same rank, at most one of them is retained in
\(J(u)\).  Let \(E_U\subseteq U\times U\) be the allowed rethreading
relation; at minimum it must respect (1.1).  For a candidate state
\(X\in\Omega_{c(u)}\), put

\[
                         P_j(X)=X_0\dot\cup\cdots\dot\cup X_{j-1}.
                                                                    \tag{4.1}
\]

Define the role-labelled digraph \(\mathcal D\) on

\[
                         \{(u,X):u\in U,\ X\in\Omega_{c(u)}\}
\]

by

\[
 (u,X)\longrightarrow(v,Y)
 \quad\Longleftrightarrow\quad
 (u,v)\in E_U\ \hbox{ and }\ Y_{i+1}=X_i\setminus Y_0\ (i<d).       \tag{4.2}
\]

An **owner--flag transversal** is a set

\[
                         \mathcal X=\{(u,X_u):u\in U\}             \tag{4.3}
\]

such that

1. the owners \(T(X_u)\) are pairwise distinct (and hence are all members
   of \(\binom{[k]}r\)); and
2. for every rank \(s\), the marked sets \(P_j(X_u)\), over all
   \(j\in J(u)\) with \(|P_j(X_u)|=s\), are exactly the prescribed residual
   target family of rank \(s\).

### Theorem 4.1 (NRFC Hall equivalence)

For the fixed role template, a one-copy named rotor flag-colouring with any
number of successor cycles exists if and only if there is an owner--flag
transversal \(\mathcal X\) for which

\[
 |N^+_{\mathcal D}(A)\cap\mathcal X|\ge |A|
                         \qquad\hbox{for every }A\subseteq\mathcal X. \tag{4.4}
\]

For fixed \(\mathcal X\), its exact cycle-cover deficiency is

\[
 \delta(\mathcal X)
   =\max_{A\subseteq\mathcal X}
      \bigl(|A|-|N^+_{\mathcal D}(A)\cap\mathcal X|\bigr),          \tag{4.5}
\]

and is the deficit of one ordinary bipartite maximum matching.

#### Proof

Split \(\mathcal X\) into a tail and a head copy, and join a tail to a head
exactly when (4.2) holds.  A successor permutation is precisely a perfect
matching in this bipartite graph.  Hall's theorem gives (4.4), and the
standard deficiency form of Hall gives (4.5).  Such a matching is a
permutation of \(\mathcal X\), hence a disjoint union of directed cycles.
Conversely, every one-copy NRFC successor permutation supplies that perfect
matching.  The owner and flag clauses are exactly the two clauses in the
definition of \(\mathcal X\). \(\square\)

Thus Hamiltonicity is not part of the first gate.  The exact missing
selection theorem is:

> **Owner--Flag Hall Transversal (OFHT).**  For some aggregate semigroup
> template of the canonical Ferrers demand, there is an owner--flag
> transversal \(\mathcal X\) with \(\delta(\mathcal X)=0\).

OFHT is equivalent to the weakest multiple-cycle form of NRFC.  It is the
weakest named owner/target theorem left after aggregate semigroup rounding.

For reference, OFHT has the following exact zero--one formulation.  Use
\(x_{u,X}\) for selecting a candidate and \(y_{uX,vY}\) for a transition:

\[
\begin{aligned}
 &\sum_{X\in\Omega_{c(u)}}x_{u,X}=1 &&(u\in U),\\
 &\sum_{u,X:T(X)=T}x_{u,X}=1 &&(T\in\tbinom{[k]}r),\\
 &\sum_{u,X,j:\,P_j(X)=P}x_{u,X}=1
      &&(P\hbox{ a prescribed residual target}),\\
 &\sum_{v,Y}y_{uX,vY}=x_{u,X},\qquad
   \sum_{v,Y}y_{vY,uX}=x_{u,X},\\
 &y_{uX,vY}=0 &&\text{unless (4.2) holds},\\
 &x,y\in\{0,1\}.
\end{aligned}                                                        \tag{4.6}
\]

The target row is understood occurrencewise over the marked indices
\(j\in J(u)\); boundary targets have right side zero, or equivalently are
omitted from the candidate set.  Once \(x\) is fixed, the \(y\)-subsystem
is totally unimodular and is exactly (4.4).  Joint selection of \(x\) is
not reduced to that bipartite matching: one state simultaneously consumes
an owner and a nested collection of target colours.

## 5. The exact reach and limit of coordinate symmetry

Three consequences are automatic.

1. **Static owner assignment.**  Every type occurs over every rank-\(r\)
   owner, so the role-to-owner projection before transition constraints is
   complete bipartite.  Any \(W\) roles can be bijected with all \(W\)
   owners.

2. **Full-orbit transition expansion.**  Theorem 2.2 gives (2.7), and hence
   perfect matchings after taking the exact clone multiplicities that make
   two complete labelled layers equally large.  This is precisely the
   fractional/bounded-multiplicity lift; it is not a section with one state
   per owner.

3. **Separate rankwise target Hall.**  If \(s=c_0+\cdots+c_{j-1}\), then
   for fixed \(P\subseteq T\), \(|P|=s\), the number of partitions of
   owner \(T\) with \(P_j(X)=P\) is

   \[
   {s!\over\prod_{i<j}c_i!}
   {(r-s)!\over\prod_{i\ge j}c_i!}.                            \tag{5.1}
   \]

   Thus the full owner--rank-\(s\) incidence is biregular.  In the central
   range \(r=\lceil k/2\rceil\), every family \(\mathcal A\) of rank-\(s\)
   targets, \(s<r\), has at least

   \[
                         {W\over\binom ks}|\mathcal A|
                         \ge |\mathcal A|                         \tag{5.2}
   \]

   containing owners.  Hence every one rank separately has an owner SDR.

None of these statements supplies a common transversal for several nested
ranks and the cyclic transition rows.  The full-orbit average in (2.7) can
put several states over one owner and omit another owner; choosing one state
per fibre can destroy every transition edge.  Formula (5.2) likewise does
not couple the different ranks carried by one flag.

## 6. A sharp two-role obstruction invisible to owner Hall

### Proposition 6.1 (an infinite primitive obstruction surviving owner changes)

For arbitrary \(d\ge2\) and \(K\ge0\), put \(r=K+d+2\) and take two roles
of types

\[
 c=(K+1,2,1,\ldots,1),\qquad c'=(K+2,1,1,\ldots,1),             \tag{6.1}
\]

Both type transitions are legal under (1.1).  With the two cross
transitions required, there are no labelled states
\(X\in\Omega_c\), \(Y\in\Omega_{c'}\), on the same or on different owners,
such that both \(X\to Y\) and \(Y\to X\) satisfy (1.2).

#### Proof

Write the cells as \(X_0,\ldots,X_d\) and \(Y_0,\ldots,Y_d\).  From
\(X\to Y\),

\[
                         Y_1=X_0\setminus Y_0.
\]

Since \(|Y_1|=1\) and \(|X_0|=K+1\), this gives
\(|X_0\cap Y_0|=K\).  From \(Y\to X\),

\[
                         X_1=Y_0\setminus X_0,
\]

and the right side has size \((K+2)-K=2=|X_1|\).  Returning to
\(X\to Y\) gives

\[
                         Y_2=X_1\setminus Y_0=\varnothing,
\]

contrary to \(|Y_2|=1\). \(\square\)

For every \(k>r\), the projected owner graph nevertheless sees both
directions between appropriately prepared adjacent rank-\(r\) owners: each
terminal cell has size one, so (2.1) permits a one-element exchange in
either direction.  Therefore all owner-only two-role Hall cuts can pass
while the literal state cycle is impossible.  The case \(d=2,K=0\) is the
published \((1,2,1)\leftrightarrow(2,1,1)\) obstruction and is the smallest
member of this family.

Thus, for every member of the family and every \(k>r\), the two complete
labelled layers separately satisfy the normalized Hall expansion (2.7),
and the two projected owner relations permit reciprocal adjacent-owner
arcs, yet the joint one-copy cycle does not exist.  Hence there is no
black-box implication

\[
 \text{full-orbit biregularity plus owner symmetry}
       \quad\Longrightarrow\quad
 \text{one-copy labelled cycle}.                              \tag{6.2}
\]

Any bounded-multiplicity-to-one-copy theorem must use an explicit
rethreading through additional role occurrences; it cannot be a rounding
of the two separate layer matchings.

### Proposition 6.2 (a unit type self-loop is not a unit labelled loop)

If \(d\ge1\) and \(X_1\ne\varnothing\), then the one-vertex transition
\(X\to X\) is impossible.

#### Proof

Putting \(Y=X\) in (1.2) at \(i=0\) would give

\[
                         X_1=X_0\setminus X_0=\varnothing.
\]

This contradicts the hypothesis. \(\square\)

In particular, the formal short self-loop packages used for the low
semigroup coordinates have positive age-one cells and are not literal
one-state cycles.  Their occurrence copies must also be rethreaded through
other roles.

The “two buffers” in the aggregate conductor are resource coordinates and
families of formal rotor packages, not two specified labelled states.
Consequently their positivity cannot, by itself, remove Proposition 6.1 at
multiplicity one.  A positive claim requires an explicit enlarged role
template and an owner--flag transversal satisfying (4.4).  Buffer roles may
permit such a rethreading, but this is exactly OFHT rather than a consequence
of the conductor inequalities.

The companion theorem
`MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md`
determines this local enlargement sharply.  One primitive adjacent-buffer
package needs exactly `d` additional low-buffer occurrences for a one-copy
owner-simple lift; equivalently, the exact unbuffered primitive multiplicity
is `ceil((d+2)/2)`.  These local modules still have to be packed into the
prescribed global owner and residual-target families, which is the OFHT
selection problem.

## 7. Correct implication boundary

The following are now proved:

* the exact owner-changing transition geometry (2.1);
* the exact full labelled biregular degrees (2.4)--(2.6);
* automatic static owner assignment, one-step owner Hall, and separate
  rankwise target Hall; and
* the exact Hall/min-cut criterion (4.4)--(4.5) after choosing a common
  owner--flag transversal.

The first unproved integral statement is OFHT/NRFC: choose the transversal
itself so that all owner rows, all nested named-target rows, and the cycle-
cover Hall cuts hold simultaneously.  The aggregate two-buffer conductor
does not imply this statement.  After OFHT, connectivity or opening,
Ore--Ryser physical completion, residence, upper/deep witnesses, and the
common compiler cap remain separate gates.
