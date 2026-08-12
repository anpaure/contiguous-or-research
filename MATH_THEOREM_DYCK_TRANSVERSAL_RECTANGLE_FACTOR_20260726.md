# A noncanonical Dyck-port-transversal exact odd-cycle factor by one component switch

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input
is used.

## 0. Result

Let

\[
 J=[2r],\qquad {\cal D}_r=\{P\in\tbinom Jr:
             \mathbf1_P\text{ is a Dyck word}\}.             \tag{0.1}
\]

For every \(r\ge2\), there is a noncanonical
\({\cal D}_r\)-port-transversal exact \(C_{2r+1}\)-factor of

\[
 KG(J\cup\{\infty\},r).                              \tag{0.2}
\]

It is obtained from the canonical MSW factor by one connected alternating
8-cycle switch.  The switch changes two rooted traces at one internal
phase, keeps their two canonical Dyck boundary sets as their roots, and
preserves exactly both ownership ledgers:

\[
 \biguplus X_t=\binom Jr,
 \qquad
 \biguplus(X_t\cup X_{t+1})=\binom J{r+1}.           \tag{0.3}
\]

Thus it is a literal exact-factor component switch, not a signed trade
awaiting completion.

The construction is uniform.  Put

\[
 R=\{5,7,\ldots,2r-1\},                             \tag{0.4}
\]

with \(R=\varnothing\) for \(r=2\).  Two canonical rooted traces begin

\[
 \begin{array}{c|ccc}
 1100(10)^{r-2}&12R&14R&34R\\
 (10)^r       &13R&23R&24R.
 \end{array}                                        \tag{0.5}
\]

Replace these initial pieces by

\[
 \boxed{
 12R,23R,34R,
 \qquad
 13R,14R,24R.}                                      \tag{0.6}
\]

All later states remain unchanged.  The four new adjacencies are Johnson
edges, and the old and new adjacent-union multisets are both

\[
 \{123R,124R,134R,234R\}.                           \tag{0.7}
\]

The selected Dyck sets \(12R\) and \(13R\) remain the first states
\(X_0\) of their two infinity-cut Johnson geodesics, and their opposite
ports \(X_r\) remain the complementary sets.  The inserted states
\(23R\) and \(14R\) are not Dyck boundary sets:
the first begins with zero, while the second has negative Dyck height after
its third bit.  Hence the two modified cycles still contain exactly their
old roots from \({\cal D}_r\).  Exact ownership then shows that every other
cycle does also.

The case \(r=1\) is the exact obstruction: \(KG(3,1)=C_3\), so its
\(C_3\)-factor is unique and no noncanonical port-transversal factor exists.

The note also proves two reusable criteria.

1. A port-rooted trace system indexed by \({\cal D}_r\) is a
   \({\cal D}_r\)-port-transversal exact factor if and only if it has legal
   complementary Johnson paths and the two ledgers (0.3).
2. Swapping the phase-\(t\) states of two rooted traces is legal if and
   only if its four cross adjacencies are Johnson edges and its four
   adjacent unions have the same multiset before and after.  If the roots
   are not moved, port-transversality is automatic.

Consequently every affine copy of (0.6) inside an aligned recursive hole
is an exact context substitute.  Phase-disjoint copies commute.  This
closes the finite existence gate for a noncanonical
\({\cal D}_r\)-port-transversal factor.  It does not by itself prove that a
sparse collection of such switches has sufficient global cap-tail action
for coefficient one.

## 1. Rooted trace normal form

Every minimum odd cycle in (0.2), distinguished at its unique edge whose
two endpoints avoid and straddle \(\infty\), may be written

\[
 X_0,Z_0,X_1,Z_1,\ldots,Z_{r-1},X_r,                \tag{1.1}
\]

where

\[
 X_t\in\binom Jr,qquad X_t\sim_JX_{t+1},qquad
 X_r=J\setminus X_0,                                \tag{1.2}
\]

and

\[
 Y_t=X_t\cup X_{t+1},qquad
 Z_t=\{\infty\}\cup(J\setminus Y_t).               \tag{1.3}
\]

The closing edge is \(X_rX_0\), since those two sets are complementary.

The two states \(X_0,X_r\) are exactly the two core \(r\)-windows adjacent
to \(\infty\) in the cyclic order; call them the **ports** of the wreath.
A factor is **\({\cal D}_r\)-port-transversal** when every wreath has
exactly one member of \({\cal D}_r\) among its two ports.  A
**port-rooted** trace system orients each wreath from that unique Dyck
port \(P=X_0\), so its opposite port is \(X_r=J\setminus P\).

Let a rooted trace system be a family

\[
 {\cal X}=\{X_0(P),\ldots,X_r(P):P\in{\cal D}_r\}   \tag{1.4}
\]

with

\[
 X_0(P)=P,qquad X_r(P)=J\setminus P.               \tag{1.5}
\]

### Proposition 1.1 (ordinary transversality is not the interface)

For \(r=2\), put \(\infty=0\), \(J=\{1,2,3,4\}\), and
\[
 D=\{23,24\}.                                       \tag{1.5a}
\]
The cyclic orders
\[
 (0,1,2,3,4),\qquad(0,2,4,1,3)                     \tag{1.5b}
\]
form an exact factor and are \(D\)-transversal.  But the first order has
infinity-cut core trace
\[
 12,23,34,                                          \tag{1.5c}
\]
whose ports are \(12,34\); its selected member \(23\) is interior.
Therefore ordinary \(D\)-transversality neither supplies the boundary
orientation (1.5) nor permits context substitution.

This is why port retention below is a separate condition rather than a
consequence of exact state ownership.

### Theorem 1.2 (necessary and sufficient port-transversal ledgers)

The rooted trace system (1.4) gives a port-rooted
\({\cal D}_r\)-port-transversal exact \(C_{2r+1}\)-factor if and only if

1. \(X_t(P)\sim_JX_{t+1}(P)\) for every \(P,t\);
2. as multisets,
   \[
    \biguplus_{P\in{\cal D}_r}\biguplus_{t=0}^r
       \{X_t(P)\}=\binom Jr;                        \tag{1.6}
   \]
3. as multisets,
   \[
    \biguplus_{P\in{\cal D}_r}\biguplus_{t=0}^{r-1}
       \{X_t(P)\cup X_{t+1}(P)\}=\binom J{r+1}.    \tag{1.7}
   \]

#### Proof

Condition 1 and (1.5) make every row a cycle of the form (1.1)--(1.3).
Condition (1.6) says that every factor vertex avoiding \(\infty\) occurs
once.  Complementation in \(J\), followed by adjoining \(\infty\), is a
bijection

\[
 \binom J{r+1}\longrightarrow
 \{Z\in\tbinom{J\cup\{\infty\}}r:\infty\in Z\}.    \tag{1.8}
\]

Thus (1.7) says precisely that every factor vertex containing \(\infty\)
occurs once.  The cycles consequently form an exact factor.

Their roots \(X_0(P)\), \(P\in{\cal D}_r\), already use every member of
\({\cal D}_r\) once.  By (1.6), no member of \({\cal D}_r\) can occur at
any other state.  Since the number of cycles equals
\(|{\cal D}_r|=\operatorname{Cat}_r\), every cycle contains exactly one
Dyck boundary set.  Since every root is a port, this proves
port-transversality.

Conversely, a port-rooted \({\cal D}_r\)-port-transversal exact factor is
already oriented as in (1.5).  The minimum-cycle normal form gives
Condition 1, while exact ownership gives (1.6)--(1.7). \(\square\)

The important point is that **after port-rooting**, transversality needs no
third incidence ledger.  Once the Dyck ports remain fixed, exact state
ownership makes a second Dyck state in any row impossible.  Proposition
1.1 shows that exact ownership alone cannot manufacture the port-rooting.

### Theorem 1.3 (authoritative middle-levels path-factor form)

Let \(M(J)\) be the bipartite inclusion graph on
\(\binom Jr\mathbin{\dot\cup}\binom J{r+1}\).  Port-rooted
\({\cal D}_r\)-port-transversal exact odd-cycle factors are in bijection with
vertex partitions of \(M(J)\) into the paths
\[
 P=X_0\subset Y_0\supset X_1\subset\cdots\subset
 Y_{r-1}\supset X_r=J\setminus P,
 \qquad P\in{\cal D}_r.                              \tag{1.9}
\]

#### Proof

Given a rooted trace, insert \(Y_t=X_t\cup X_{t+1}\) between consecutive
states.  Conditions (1.6)--(1.7) say exactly that these alternating paths
partition both vertex classes of \(M(J)\).  Conversely, from a path factor
(1.9) put
\[
 Z_t=\{\infty\}\cup(J\setminus Y_t).                 \tag{1.10}
\]
Then \(X_t,Z_t,X_{t+1}\) are consecutive pairwise-disjoint odd-graph
vertices, and \(X_r=J\setminus X_0\) supplies the closing edge.  The vertex
partition on the two shores gives exact ownership, while the prescribed
endpoints give the two ports.  The constructions are inverse. \(\square\)

All subsequent switches will therefore be proved directly as rooted
complement-path-factor switches in \(M(J)\).  This avoids the invalid
step of extracting ports from ordinary transversality.

## 2. The exact two-row phase-switch criterion

Take two rows of a rooted exact trace system and one internal phase
\(1\le t\le r-1\).  Write their affected triples as

\[
 A_-\,,A\,,A_+,
 \qquad
 B_-\,,B\,,B_+.                                    \tag{2.1}
\]

Keep all other states fixed and swap only \(A\) and \(B\), producing

\[
 A_-\,,B\,,A_+,
 \qquad
 B_-\,,A\,,B_+.                                    \tag{2.2}
\]

### Theorem 2.1 (one-phase port-preserving component-switch criterion)

The replacement (2.2) is another
\({\cal D}_r\)-port-transversal exact factor if and only if

1. all four pairs
   \[
    A_-B,\ BA_+,\ B_-A,\ AB_+                       \tag{2.3}
   \]
   are Johnson edges; and
2. the adjacent-union multisets agree:
   \[
   \begin{aligned}
    \{A_-\cup A,A\cup A_+,B_-\cup B,B\cup B_+\}
    ={}&\{A_-\cup B,B\cup A_+,\\
        &B_-\cup A,A\cup B_+\}.
   \end{aligned}                                    \tag{2.4}
   \]

#### Proof

The state multiset at phase \(t\) is merely permuted, so (1.6) is
automatic.  Condition (2.3) is exactly Johnson legality for the only four
new transitions.  Since every other transition is unchanged, (2.4) is
necessary and sufficient for the union ledger (1.7).  The roots and
complementary endpoints are unchanged.  Theorem 1.2 now proves both exact
factorhood and \({\cal D}_r\)-port-transversality. \(\square\)

More generally, for a slab replacement

\[
 X'_t(u)=X_t(f_tu)                                   \tag{2.5}
\]

by phasewise permutations \(f_t\), with the two slab-boundary
permutations equal to the identity, state ownership is automatic.  The
necessary and sufficient conditions are Johnson legality and equality of
the aggregate adjacent-union multiset over the whole slab.  If phase zero
is fixed, Theorem 1.2 again makes Dyck port-transversality automatic.

This is the precise component-switch criterion requested in Lane B.  A
phasewise permutation is not legal merely because it preserves middle
states; the adjacent-union ledger (2.4) is the second and indispensable
condition.

## 3. The uniform rectangle construction

Fix \(r\ge2\) and use the spectator set (0.4), of size \(r-2\).  Put

\[
 \begin{array}{lll}
 A=12R,&B=14R,&C=34R,\\
 D=13R,&E=23R,&F=24R.
 \end{array}                                        \tag{3.1}
\]

The two words

\[
 c_r=1100(10)^{r-2},
 \qquad
 e_r=(10)^r                                         \tag{3.2}
\]

are in \({\cal D}_r\), with root sets \(A\) and \(D\), respectively.
The canonical MSW recursion gives the initial trace table

\[
 \begin{array}{c|ccc}
 c_r&A&B&C\\
 e_r&D&E&F.
 \end{array}                                        \tag{3.3}
\]

Apply Theorem 2.1 at phase one, interchanging \(B\) and \(E\).

### Lemma 3.1 (Johnson legality)

The four new pairs

\[
 AE,\ EC,\ DB,\ BF                                  \tag{3.4}
\]

are Johnson edges.

#### Proof

After deleting the common spectator set \(R\), their symmetric
differences are respectively

\[
 \{1,3\},\quad\{2,4\},\quad\{3,4\},\quad\{1,2\}.
                                                               \tag{3.5}
\]

Each has size two. \(\square\)

### Lemma 3.2 (exact union ledger)

The old and new union multisets in (2.4) are both

\[
 \boxed{\{123R,124R,134R,234R\}.}                  \tag{3.6}
\]

#### Proof

For the old paths,

\[
 A\cup B=124R,\quad B\cup C=134R,
 \quad D\cup E=123R,\quad E\cup F=234R.            \tag{3.7}
\]

For the new paths,

\[
 A\cup E=123R,\quad E\cup C=234R,
 \quad D\cup B=134R,\quad B\cup F=124R.            \tag{3.8}
\]

These are the same four sets. \(\square\)

In the path-factor normal form, the two old path fragments are
\[
\begin{aligned}
 A&\subset124R\supset B\subset134R\supset C,\\
 D&\subset123R\supset E\subset234R\supset F,
\end{aligned}                                       \tag{3.8a}
\]
whereas the new fragments are
\[
\begin{aligned}
 A&\subset123R\supset E\subset234R\supset C,\\
 D&\subset134R\supset B\subset124R\supset F.
\end{aligned}                                       \tag{3.8b}
\]
Thus the switch repartitions the same six \(r\)-vertices and four
\((r+1)\)-vertices into two paths, while leaving both initial ports and
all terminal ports fixed.

### Theorem 3.3 (noncanonical port-transversal factor for every \(r\ge2\))

Replace (3.3) by

\[
 \begin{array}{c|ccc}
 c_r&A&E&C\\
 e_r&D&B&F,
 \end{array}                                        \tag{3.9}
\]

and leave every later state and every other canonical row unchanged.
The result is a noncanonical \({\cal D}_r\)-port-transversal exact
\(C_{2r+1}\)-factor.

#### Proof

Lemmas 3.1--3.2 and Theorem 2.1 prove exact factorhood.  The selected
ports \(A,D\) and their complementary opposite ports are unchanged,
because only the internal phase-one vertices were exchanged.
The factor is noncanonical because the transition \(A-B\) has been
replaced by the distinct transition \(A-E\).

For a direct port-transversality check, \(E=23R\) begins with a missing first
coordinate and is not a Dyck set.  The first three bits of \(B=14R\) are
\(100\), whose Dyck height after the third bit is \(-1\), so \(B\) is not
a Dyck set either.  Every unchanged internal state was already non-Dyck.
Thus each modified row retains precisely its old Dyck port. \(\square\)

The port audit can be recorded without reference to the internal-state
test:
\[
 \partial_\infty(C'_A)=\{A,J\setminus A\},\qquad
 \partial_\infty(C'_D)=\{D,J\setminus D\}.           \tag{3.9a}
\]
The switch (3.8a)--(3.8b) changes neither endpoint of either
middle-levels path.  Moreover the complement of a nonempty Dyck word
starts with zero, so \(J\setminus A,J\setminus D\notin{\cal D}_r\).
Consequently
\[
 |{\cal D}_r\cap\partial_\infty(C'_A)|
 =|{\cal D}_r\cap\partial_\infty(C'_D)|=1.           \tag{3.9b}
\]
Every other wreath is unchanged.  Equations (3.9a)--(3.9b) are the direct
verification of the corrected port condition.

For \(r=2\), this is the explicit pair

\[
 12,23,34,
 \qquad
 13,14,24,                                       \tag{3.10}
\]

inside a noncanonical exact \(C_5\)-factor of \(KG(5,2)\).
Writing \(\infty=0\), the reconstruction (1.10) gives the two odd cycles
\[
 12,04,23,01,34,
 \qquad
 13,02,14,03,24.                                    \tag{3.11}
\]
Their port pairs are respectively \(\{12,34\}\) and \(\{13,24\}\).
For the natural Dyck family \({\cal D}_2=\{12,13\}\), each pair contains
exactly one selected port.  Thus the smallest noncanonical example passes
the corrected interface directly, unlike Proposition 1.1.

## 4. It is one connected alternating component switch

Let \({\cal B}_r\) be the bipartite inclusion graph with shores
\(\binom Jr\) and \(\binom J{r+1}\).  A Johnson transition
\(X-X'\) with union \(Y\) is represented by the two incidences
\(X-Y-X'\).

Four incidences are common to the old and new trace systems:

\[
 B-124R,\quad B-134R,
 \quad E-123R,\quad E-234R.                        \tag{4.1}
\]

After deleting those common incidences, the symmetric difference is the
single alternating 8-cycle

\[
 \boxed{
 A-124R-F-234R-C-134R-D-123R-A.}                   \tag{4.2}
\]

The old incidences on (4.2) are

\[
 A-124R,\quad F-234R,
 \quad C-134R,\quad D-123R,                         \tag{4.3}
\]

and the other four are new.  Toggling the complete connected component
(4.2) therefore gives exactly (3.9).  Every vertex of (4.2) loses and
gains one incidence, so both ownership shores remain saturated once.

This is the promised component interpretation.  The switch is not an
arbitrary reconnection of canonical paths: its support is one balanced
connected component of the two-ledger incidence overlay.  The roots
\(A,D\in{\cal D}_r\) remain the named ports of their rows even though one
incident transition at each root changes.

## 5. General component condition and obstruction

The preceding example suggests the exact reusable formulation.

Let \(F\) be a \({\cal D}_r\)-port-rooted exact factor and let \(Z\) be an
alternating subgraph of its incidence overlay with another trace system.
Toggle all incidences of \(Z\).  The result is a
\({\cal D}_r\)-port-transversal exact factor if and only if all of the
following
hold.

1. **Two-shore balance.**  At every \(r\)-set and every \((r+1)\)-set,
   the number of deleted incidences equals the number inserted.
2. **Trace legality.**  After common incidences are restored, every
   \((r+1)\)-vertex pairs two adjacent \(r\)-states and every resulting
   row is a Johnson path.
3. **Endpoint monodromy.**  The path beginning at each
   \(P\in{\cal D}_r\) ends at \(J\setminus P\); no switched component
   permutes complementary endpoints or creates a closed internal trace.
4. **Port retention.**  The initial occurrence of each
   \(P\in{\cal D}_r\) remains the initial port of its named row.

Necessity is immediate from Theorem 1.3.  Conversely, Conditions 1--3
give the two exact ownership ledgers and legal complementary traces, while
Condition 4 invokes Theorem 1.2 to give
\({\cal D}_r\)-port-transversality.

For a one-phase two-row move, Conditions 1--4 reduce exactly to
(2.3)--(2.4), since the endpoint monodromy and roots are visibly fixed.
For disjoint moves, the ledgers add.  Hence:

### Corollary 5.1 (commuting library)

Any collection of switches of the form (3.9) whose affected row-phase
slabs are disjoint may be performed independently.  All \(2^k\) choices
are \({\cal D}_r\)-port-transversal exact factors, where \(k\) is the
number of
switches.

The conclusion remains true after an arbitrary affine relabelling of
\(J\), provided \({\cal D}_r\) is relabelled with the boundary context.
Thus every aligned recursive hole admits this noncanonical local library.

At \(r=1\), the obstruction is absolute.  There is one Dyck root, one
minimum odd cycle, and the graph in (0.2) is itself that cycle.  Conditions
1--4 have only the identity solution.  For \(r\ge2\), (4.2) is a uniform
nonzero solution of the component conditions.

## 6. Constant-one relevance and limitation

The construction closes the existence question left open by the
port-transversal context-substitution theorem: the canonical MSW factor is
not the only \({\cal D}_r\)-port-transversal exact local factor.

Moreover the switch is not shadow-inert.  Installed in a size-\(r\)
parent context, it changes one internal state of each of two rooted traces;
the parent-coordinate calculation gives different rooted child-window
intersections for the two rows.  Thus the library can split a canonical
invisible child fibre while retaining exact middle ownership and the same
outer Dyck boundary owners.

What is not proved is quantitative sufficiency.  One switch changes only
four transition colours and two row-phase assignments.  A sparse family
of such rectangles has only sparse cap-tail action, and the certified
leaf-rotation graph generated by their canonical embeddings is not
connected on all Dyck fillings.  Constant one still requires either

* a dense packing of phase-disjoint port-transversal rectangles with aggregate
  action \(\Omega(W/(\log r)^{3/2})\), or
* a larger exact component library which moves between the distinct
  leaf-rotation normal-form classes.

The present theorem supplies the exact positive local atom and its full
legality criterion.  It removes nonexistence of a noncanonical
\({\cal D}_r\)-port-transversal factor as a possible obstruction.
