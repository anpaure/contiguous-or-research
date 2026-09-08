# Restricted central Ucycle splicing: exact rank, collar, and seam-fan audit

Date: 2026-07-25

Scope: pure mathematics.  No computation or search is used.

This note cross-audits and synthesizes the detailed proofs in
`MATH_ATTACK_C_ODD_WREATH_SUCCESSOR_COMPONENT_RANK_20260725.md`,
`MATH_ATTACK_C_RESTRICTED_UCYCLE_GAP_SAFE_SUCCESSOR_SPLICING_20260725.md`,
and `MATH_ATTACK_MSW_ORDERED_STATE_PORTAL_OBSTRUCTION_20260725.md`.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname {Cat}_m.
\]

For a fixed exact odd-graph wreath factor, the restricted ordered-word
route has two sharply different answers.

* Without a mesoscopic recurrence constraint, the optimum successor
  recombination is completely determined: for an orientation choice
  \(\varepsilon\), the number of remaining Euler circuits is

  \[
  C_\varepsilon
  =B-\bigl(\Xi_\varepsilon-\beta_\varepsilon\bigr),
  \tag{0.1}
  \]

  where \(\Xi_\varepsilon\) is ordered-state collision excess and
  \(\beta_\varepsilon\) is the cycle rank of the circuit--state incidence
  graph.  Thus raw pair collisions and even raw collision excess both
  overcount the independent joining rank.
* Every successor system automatically has recurrence gap at least
  \(m+1\).  At target gap \(m+H\), an exact triangular collar condition is
  necessary and sufficient at each adaptive merge.  The canonical
  \(\operatorname {Cat}_{m-1}\) MSW portals fail this condition already
  for \(H=2\), and by themselves leave a positive proportion of circuits.

There is also a positive bypass which is stronger for literal OR output.
One changed successor destroys a triangular family of
\(H(H+1)/2\) shallow flags, but all of them have one common
\((m+1)\)-set core and are restored by a set-valued word of length
\(2H-1\).  Consequently ordered-state rank
\(B-o(B)\), together with \(o(W)\) initial lower-shadow defect, gives a
central-band word of length \(W+o(W)\) for every \(H=o(m)\), without
requiring the final singleton spine itself to have gap \(m+H\).

This is a conditional theorem for a restricted sufficient architecture.
Singleton/FIFO states are not asserted to be without loss of generality
for arbitrary contiguous-OR words.  State multiplicities below are
arbitrary; in particular, no singleton ordered-state class is assumed.

## 1. The fixed ordered-edge system

Choose an orientation of each wreath \(R\), and write its cyclic coordinate
permutation as

\[
 q_R=(q_{R,0},\ldots,q_{R,n-1}).
\]

It supplies the ordered arcs

\[
 e_{R,i}=(q_{R,i},\ldots,q_{R,i+m-1})
 \tag{1.1}
\]

from their length-\((m-1)\) prefixes to their length-\((m-1)\)
suffixes.  Exactness says that the supports of the \(W\) arcs in (1.1)
are all the members of \(\binom{[n]}m\), once each.  Let
\(D_\varepsilon\) be this balanced directed graph.

A successor system is a bijection from incoming to outgoing arcs at every
ordered state.  A legal successor switch transposes two values of one such
bijection.  It changes no selected arc and hence no middle owner.

Form the bipartite incidence graph \(I_\varepsilon\) whose left vertices
are the \(B\) original wreaths, whose right vertices are the used ordered
states, and whose edges are state occurrences.  No wreath repeats an
ordered state, since its coordinate order is a permutation.  If

\[
 V_\varepsilon=|V_R(I_\varepsilon)|,\qquad
 \Xi_\varepsilon=W-V_\varepsilon
   =\sum_v(d(v)-1),                                      \tag{1.2}
\]

and \(\beta_\varepsilon\) is the ordinary cycle rank of
\(I_\varepsilon\), then its number of connected components is the number
\(c(D_\varepsilon)\) of weak components of the selected directed graph.

### Theorem 1.1 (exact independent successor rank)

For fixed \(\varepsilon\), the minimum number of successor circuits is

\[
 \boxed{C_\varepsilon=c(D_\varepsilon)
 =B-\Xi_\varepsilon+\beta_\varepsilon.}                  \tag{1.3}
\]

It is attained by exactly

\[
 J_\varepsilon=B-C_\varepsilon
 =\Xi_\varepsilon-\beta_\varepsilon                      \tag{1.4}
\]

component-merging switches.  Allowing whole-wreath reversals gives the
exact optimum

\[
 \boxed{C_{\min}(\mathcal F)
 =B-\max_\varepsilon(\Xi_\varepsilon-\beta_\varepsilon).}\tag{1.5}
\]

#### Proof

A successor circuit cannot leave a weak component of the fixed arc graph.
Conversely, if two current circuits lie in the same weak component, a chain
of original arc circuits connects them through shared ordered states.  At
the first shared state between two current parts, transposing one successor
from each part merges the two permutation cycles.  Repeating along a
spanning tree leaves one Euler circuit per weak component and uses one
switch per merger.

The incidence graph has \(W\) edges, \(B+V_\varepsilon\) vertices, and
\(C_\varepsilon\) components.  Therefore

\[
 \beta_\varepsilon
 =W-(B+V_\varepsilon)+C_\varepsilon
 =\Xi_\varepsilon-B+C_\varepsilon,
\]

which rearranges to (1.3)--(1.4).  Every local bijection is reachable from
the original one because transpositions generate the symmetric group at
each state.  Finally optimize (1.3) over the two orientations of every
wreath.  \(\square\)

Thus \(o(B)\) components are possible for the fixed factor if and only if

\[
 \max_\varepsilon(\Xi_\varepsilon-\beta_\varepsilon)
 =B-o(B).                                                 \tag{1.6}
\]

### Lemma 1.2 (multiplicity and orientation ledger)

For every ordered state \(v\),

\[
 2d(v)\le m+2.                                           \tag{1.7}
\]

Let \(M\) be the number of missing unordered depth-one lower shadows.
For every covered support \(S\), identify orders up to reversal; let
\(a(S)\) be the number of resulting classes and put

\[
 \Phi=\sum_{S\ {m covered}}(a(S)-1).
\]

After choosing whole-wreath orientations, let \(b_\varepsilon\) count
the reversal classes whose incidences realize both directed signs.  Then

\[
 \boxed{
 \Xi_\varepsilon
 =\frac{2W}{m+2}+M-\Phi-b_\varepsilon.}                  \tag{1.8}
\]

#### Proof

If the support of \(v\) is \(S\), each occurrence has an incoming and an
outgoing middle owner \(S\cup\{x\}\) and \(S\cup\{y\}\).  Exact middle
ownership makes all \(2d(v)\) extension coordinates distinct, and they
lie in the \((m+2)\)-set \([n]\setminus S\).  This proves (1.7).

There are

\[
 N=\binom n{m-1}=\frac{m}{m+2}W
\]

possible supports.  The first reversal class over every covered support
contributes \(N-M\) directed-state vertices, the additional classes
contribute \(\Phi\), and a class containing both signs contributes one
additional vertex.  Hence

\[
 V_\varepsilon=N-M+\Phi+b_\varepsilon.
\]

Subtracting from \(W\) proves (1.8).  Notice that one orientation sign is
chosen per entire wreath, not independently at its states.  \(\square\)

Equations (1.3) and (1.8) show exactly where unordered collision counts
can fail: order fragmentation, global orientation frustration, and
incidence cycles are three separate losses.

## 2. The exact recurrence condition

The recurrence gap of a cyclic coordinate word is the least positive
cyclic distance between consecutive occurrences of one coordinate.

### Proposition 2.1 (automatic depth-one gap)

Every successor system on the fixed exact arc set has recurrence gap at
least \(m+1\).

#### Proof

If equal coordinates occurred at cyclic distance less than \(m\), some
selected length-\(m\) arc would repeat a coordinate, contrary to (1.1).
If they occurred at distance exactly \(m\), the local word would be
\(x,a_1,\ldots,a_{m-1},x\).  Its length-\(m\) windows starting at the
first and second positions have the same underlying set
\(\{x,a_1,\ldots,a_{m-1}\}\).  They are distinct selected arc
occurrences, contradicting exact middle ownership.  \(\square\)

For a growing gap one needs more.  Suppose two current circuits, already
of gap at least \(m+H\), meet at the ordered state

\[
 s=(s_1,\ldots,s_{m-1}).
\]

Write \(p_i^A\) for the \(i\)-th letter before \(s_1\) on circuit \(A\)
and \(q_j^A\) for the \(j\)-th letter after \(s_{m-1}\), and similarly
for \(B\).

### Theorem 2.2 (adaptive triangular collar test)

For \(H\le(m+2)/2\), the successor switch merging \(A\) and \(B\)
preserves gap at least \(m+H\) if and only if

\[
 \boxed{
 p_i^A\ne q_j^B,\qquad p_i^B\ne q_j^A
 \quad(i,j\ge1,\ i+j\le H+1).}                           \tag{2.1}
\]

#### Proof

The retained parts of the two circuits already satisfy the gap condition.
A new repetition must cross one of the two new seams.  The forward distance
from \(p_i^A\) through the common \((m-1)\)-state to \(q_j^B\) is

\[
 m-2+i+j.
\]

It is smaller than \(m+H\) exactly when \(i+j\le H+1\).  The reverse seam
gives the other inequality.  The stated range keeps the two collars
disjoint; alternatively the unrestricted first/last-occurrence formula
gives the same test without a collar notation.  \(\square\)

For \(H=1\), (2.1) is automatic by exact ownership: equality of the
immediate incoming extension on one circuit and outgoing extension on the
other would duplicate the same middle owner.  For mesoscopic \(H\), the
test must use the *current* collars after all earlier mergers.  A static
graph of initially compatible pairs is therefore not a spanning theorem.

Consequently, if one can perform \(B-o(B)\) component-merging switches
which pass (2.1) at the time they are made, the final system has
\(o(B)\) components and gap \(m+H\).  Conversely, a proposed sequential
gap-safe merge is certified exactly by (2.1) at every step.

## 3. Lower invariance, complement duality, and the seam fan

For \(q\ge0\), the length-\((m-q)\) word beginning at a selected arc is
its ordered prefix of that length.  Successor switches do not change this
arc.

### Lemma 3.1 (lower invariance and initial complement identity)

Let \(\delta_q^-\) be the number of missing rank-\((m-q)\) sets in the
initial cyclic wreath windows, with \(\delta_0^-=0\), and put

\[
 \Delta_H^-=\sum_{q=1}^H\delta_q^-.
\]

All lower supports and multiplicities are invariant under successor
switches.  If \(\delta_q^+\) is the initial missing count in rank
\(m+q\), then

\[
 \boxed{\delta_q^+=\delta_{q-1}^-\quad(1\le q\le H).}     \tag{3.1}
\]

Hence the total initial lower and upper defect through depth \(H\) is

\[
 \Delta_H^-+\sum_{q=1}^H\delta_q^+
 =2\sum_{q=1}^{H-1}\delta_q^-+\delta_H^-
 \le2\Delta_H^-.                                        \tag{3.2}
\]

#### Proof

Lower invariance is the fixed-prefix observation.  In one cyclic
permutation, the complement of a length-\((m+q)\) interval is the opposite
cyclic interval of length

\[
 n-(m+q)=m+1-q=m-(q-1).
\]

Opposite interval and set complementation are bijections, so missing upper
targets correspond exactly to missing lower targets at depth \(q-1\).
This proves (3.1), and summation gives (3.2).  \(\square\)

We now repair all upper flags changed by a switch without paying once per
flag.  Around one old successor transition write the local cyclic word as

\[
 \ldots,x_{-1},x_0,x_1,\ldots,x_{m-1},x_m,x_{m+1},\ldots,
\]

where \(x_0\cdots x_{m-1}\) is the incoming selected arc and \(x_m\) is
the old appended coordinate.  Put \(K=\{x_0,\ldots,x_m\}\).

### Lemma 3.2 (one-transition fan compression)

The set-valued word

\[
 \boxed{
 (\{x_{-H+1}\},\ldots,\{x_{-1}\},K,
   \{x_{m+1}\},\ldots,\{x_{m+H-1}\})}                  \tag{3.3}
\]

has length \(2H-1\) and realizes every initial upper flag through depth
\(H\) whose continuation uses this successor transition.

#### Proof

At depth \(q\), the affected starts are indexed by \(0\le t<q\), and the
old flag is

\[
 Y_{q,t}=\{x_{-t},x_{-t+1},\ldots,x_{m+q-t-1}\}.         \tag{3.4}
\]

In (3.3), take the last \(t\) left singletons, the core \(K\), and the
first \(q-1-t\) right singletons.  Their OR is exactly (3.4).  This remains
true if the local circuit repeats a coordinate, because both sides are
the same union of indexed letters.  \(\square\)

One successor switch changes two old transitions.  Applying (3.3) to both
of them costs \(2(2H-1)\).  Inductively, after any sequence of \(J\)
switches, the final circuit words plus the \(2J\) fan gadgets retain every
upper target present initially: at each step every disappearing flag uses
one of the two changed transitions and is placed in its fan before the
transition is changed.

## 4. The coefficient-sharp conditional theorem for the restricted route

### Theorem 4.1 (ordered-rank plus lower-quality suffices)

Fix an orientation \(\varepsilon\), let

\[
 R_\varepsilon=\Xi_\varepsilon-\beta_\varepsilon,
 \qquad C_\varepsilon=B-R_\varepsilon,
\]

and let \(1\le H\le(m+2)/2\).  There is a literal set-valued contiguous-OR
word covering every set in the ranks

\[
 m-H,m-H+1,\ldots,m+H
\]

of length at most

\[
\boxed{
 L_H\le
 W+C_\varepsilon(m+H-1)
 +2R_\varepsilon(2H-1)+2\Delta_H^-.}                    \tag{4.1}
\]

In particular, if for some orientation choices

\[
 R_\varepsilon=B-o(B),\qquad
 \Delta_H^-=o(W),\qquad H=o(m),                           \tag{4.2}
\]

then

\[
                         L_H=W+o(W).                       \tag{4.3}
\]

#### Proof

Theorem 1.1 merges the original wreaths to \(C_\varepsilon\) Euler
circuits using exactly \(R_\varepsilon\) switches.  If a final component
has \(L\) arcs, write one coordinate period and repeat its first
\(m+H-1\) letters.  Every cyclic window through length \(m+H\) is now a
literal interval.  Summing over components costs

\[
 W+C_\varepsilon(m+H-1).
\]

The fixed ordered arcs retain the middle layer and every initially covered
lower target.  Lemma 3.2 restores every initially covered upper target at
cost \(2R_\varepsilon(2H-1)\).  Append each initially missing lower or
upper target as one set-valued letter.  Lemma 3.1 bounds this last cost by
\(2\Delta_H^-\), proving (4.1).

Under (4.2),

\[
 C_\varepsilon(m+H-1)=o(Bm)=o(W)
\]

and

\[
 2R_\varepsilon(2H-1)\le4BH
 =\frac{4H}{2m+1}W=o(W).
\]

The last term is \(o(W)\) by hypothesis.  This proves (4.3).  \(\square\)

The theorem does not say that the final singleton spine has gap \(m+H\).
If that stricter conclusion is required, the merge sequence must also pass
Theorem 2.2.  Gap alone still does not imply upper support coverage; the fan
argument is what restores the changed targets at coefficient-sharp cost.

## 5. Audit of the canonical MSW portals

For a Dyck word \(x\), let its MSW omitted-label word be the interleaved
flip permutation followed by the distinguished coordinate.  Step-two
reading gives its tight coordinate order.  Fix

\[
 0\le p\le m-2,\quad P\in\mathcal D_p,\quad
 R\in\mathcal D_{m-p-2},\quad d=2p,
\]

and set

\[
 X=P1100R,\qquad Y=P1010R.
\]

The exact MSW concatenation law gives cyclic omitted-label words

\[
 C=(\delta,\beta,\gamma,\alpha,T),\qquad
 D=(\beta,\alpha,\delta,\gamma,T),                        \tag{5.1}
\]

where

\[
 \delta=d+4,\quad\beta=d+2,\quad
 \gamma=d+3,\quad\alpha=d+1,
\]

and \(T=(t_0,\ldots,t_{2m-4})\) is common.  Put

\[
 E=(t_0,t_2,\ldots,t_{2m-4}),\qquad
 O=(t_1,t_3,\ldots,t_{2m-5}).
\]

Then \(|E|=m-1\), \(|O|=m-2\), and the two tight words are

\[
 \omega_C=(\delta,\gamma,E,\beta,\alpha,O),\qquad
 \omega_D=(\beta,\delta,E,\alpha,\gamma,O).              \tag{5.2}
\]

Thus \(E\) is a genuine common ordered state.

### Proposition 5.1 (exact canonical-family obstruction)

There are exactly

\[
 \sum_{p=0}^{m-2}\operatorname {Cat}_p
                    \operatorname {Cat}_{m-p-2}
 =\operatorname {Cat}_{m-1}                              \tag{5.3}
\]

listed portal occurrences.  Successor systems generated using only these
cross-pair portals have at least

\[
 \operatorname {Cat}_m-\operatorname {Cat}_{m-1}
 =\frac{3m-3}{4m-2}\operatorname {Cat}_m                 \tag{5.4}
\]

Euler components.  Moreover, for \(m\ge3\), an isolated switch at any one
of them has recurrence gap exactly \(m+1\), and is not \((m+2)\)-safe
under either compatible orientation.

#### Proof

The Catalan convolution proves (5.3); the position of the four-letter
change recovers \(p,P,R\), so the listed pair occurrences are distinct.
Make a graph on the \(B\) original circuits with these occurrences as
edges.  Every transition system generated by the listed transpositions
preserves the connected components of this graph.  Since it has at most
\(\operatorname {Cat}_{m-1}\) edges, it has at least the number of
components in (5.4).  The identity

\[
 \frac{\operatorname {Cat}_{m-1}}{\operatorname {Cat}_m}
 =\frac{m+1}{4m-2}
\]

gives the displayed coefficient.

At the common state \(E\), switching produces the two seams

\[
 \delta,\gamma,E,\alpha,\gamma,
 \qquad
 \beta,\delta,E,\beta,\alpha.                            \tag{5.5}
\]

In each seam the repeated letter has forward distance
\(|E|+2=m+1\).  Proposition 2.1 excludes a smaller recurrence.  Reversing
both circuits reverses the same seams and changes no distance; reversing
only one circuit changes the shared state from \(E\) to
\(\operatorname {rev}E\), so it is no longer this ordered portal.
\(\square\)

The qualification is essential.  This is not a classification of all MSW
ordered coincidences, and it does not exclude a clustered repair which
first changes the collars in (5.5).  In fact Lemma 3.2 makes the isolated
depth-two failure cheap for literal OR output.  The genuine residual MSW
questions are whether other ordered states raise the independent rank to
\(B-o(B)\), and whether its initial lower defect satisfies
\(\Delta_H^-=o(W)\).

## 6. Exact proved/conditional boundary

The audit leaves the following statements, with no hidden singleton-state
assumption.

1. **Proved:** the exact unrestricted fusion rank is
   \(\Xi_\varepsilon-\beta_\varepsilon\), optimized only over global
   whole-wreath orientations.
2. **Proved:** recurrence gap \(m+1\) is automatic.  Gap \(m+H\) along a
   sequential merge schedule is governed exactly by the current triangular
   collars (2.1).
3. **Proved:** all switch-induced shallow upper loss is repairable in
   \(O(H)\) letters per switch, giving the exact bound (4.1).
4. **Conditional:** a factor/orientation with independent fusion rank
   \(B-o(B)\) and initial lower defect \(o(W)\) yields a
   \(W+o(W)\) word for the Gaussian central band.
5. **Open:** neither condition in item 4 is known here for the MSW factor
   or for another exact odd-graph factor.  If one insists on an un-repaired
   all-singleton spine, the additional adaptive collar-safe spanning-rank
   theorem is also open.

No full constant-one theorem is claimed.
