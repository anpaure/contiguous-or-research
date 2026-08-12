# Lane R update: exact small-family FIFO/residence coupling for \(H29\)

Date: 2026-07-28

**Index convention.** Every coordinate tuple copied from a relabel screen in
this note is zero based.  Thus `[1,12]_0=(2,13)_1`, `[10,11]_0=(11,12)_1`,
and analogous mathematical one-based labels must be shifted by one.

Method: pure mathematics only. No web search, finite search, solver,
certificate enumeration, or long computation is used below. The new factual
input that the coordinate relabel

\[
                         \tau=(1,12)
\tag{0.1}
\]

of \(H29\) has parent-pure interior candidates for all seven old zero targets,
and has strong slack on the indicated DM data, is taken as supplied input.
No candidate count or component signature is inferred from an older relabel.

## 0. Exact outcome

There are three separate gates in the proposed two-parent repair.

1. **Degree coupling.** After closing both parent paths through a dummy
   vertex, every one-in/one-out mixture is obtained by choosing one whole
   shore on each alternating assignment component. Prescribed windows are
   degree-compatible exactly when no component is forced to both shores.
2. **Monodromy and residence.** A degree-compatible mixture need not be one
   Hamilton cycle. There is an exact cycle-product formula for its number of
   components. Depth-three residence is an exact width-four signed clause
   system, equivalently an ordered finite-state condition after deleting the
   dummy.
3. **Deterministic positive coupling.** A protected, collar-safe spanning
   tree of directed \(C_4\) switches fuses a resident cycle cover into one
   Hamilton cycle. More generally, a loose spanning hypertree of assignment
   switches does so. At depth three, three unchanged arcs between switch
   sites suffice, and at most twenty oriented residence collars are checked
   per \(C_4\).

For a fixed \(O(1)\) family of resident parents there is also an intact-block
coupling theorem. Seven dependency windows of at most twelve vertices in
\(\tau H29\), together with the maximal surviving \(H29\)-runs, give at most

\[
                           7\cdot12+8=92
\tag{0.2}
\]

blocks. An exact subset recurrence retaining the ordered residence state is
necessary and sufficient within this block class. If all blocks have at
least four vertices and their safe seam digraph is semicomplete, a
deterministic tournament-insertion argument gives the desired Hamilton path.

These theorems do **not** by themselves certify the supplied
\(H29,\tau H29\) instance. The seven \(\tau H29\) windows alone are trivial
to retain: choose \(\tau H29\) wholesale. The nontrivial coupling problem
begins only when actual incumbent \(H29\) compiler cells/windows, or an exact
statewise Hall requirement, are simultaneously imposed. For that problem
the component signatures, monodromy, residence collars, and post-switch Hall
ledger have not been supplied. Strong marginal DM slack does not determine
any of them.

## 1. Dummy closure and protected windows

Let \(V\) be a finite vertex set. Close a directed Hamilton path

\[
                         P=(v_1,\ldots,v_N)
\tag{1.1}
\]

by adjoining a dummy vertex \(\partial\) and the arcs

\[
                 \partial\to v_1,\qquad v_N\to\partial.
\tag{1.2}
\]

Its successor map is one cycle \(p\in\operatorname{Sym}(\Omega)\), where

\[
                         \Omega=V\sqcup\{\partial\}.
\tag{1.3}
\]

Deleting \(\partial\) from a one-cycle successor permutation recovers a
directed Hamilton path on \(V\). The dummy is only a device for the degree
and monodromy equations. It is not a physical all-zero mask, and residence
words never wrap through it.

A **protected window** is its complete oriented dependency word, including
every arc on which the asserted compiler cell, upper witness, or endpoint
condition depends. Protecting only a distinguished motif core is insufficient.
In the current depth-three \(k=15\) compiler, an interior cell uses \(10\),
\(11\), or \(12\) consecutive middle vertices and a boundary cell uses its
full oriented twelve-vertex prefix or suffix.

## 2. Exact two-parent assignment-orbit classification

Let \(p,q\in\operatorname{Sym}(\Omega)\) be the dummy-closed successor cycles
of two directed Hamilton parents. Put

\[
                         \phi=p^{-1}q,
             \qquad q(x)=p(\phi(x)).
\tag{2.1}
\]

For a union \(T\) of cycles of \(\phi\), let \(\phi_T\) equal \(\phi\) on
\(T\) and the identity off \(T\).

### Theorem 2.1 (whole-orbit shore theorem)

Every one-in/one-out directed factor whose arcs lie in
\(E(p)\cup E(q)\) is uniquely of the form

\[
                         M_T=p\phi_T,
\tag{2.2}
\]

apart from the immaterial choice on common parent arcs. Equivalently, one
chooses the \(q\)-shore or the \(p\)-shore on every nontrivial cycle of
\(\phi\).

#### Proof

Choose the \(q\)-arc at source \(x\) when \(x\in S\), and the \(p\)-arc
otherwise. Write the resulting map as \(M=ph\). Then

\[
 h(x)=
 \begin{cases}
  \phi(x),&x\in S,\\
  x,&x\notin S.
 \end{cases}
\tag{2.3}
\]

For every \(y\in\Omega\),

\[
 |h^{-1}(y)|
   =\mathbf 1_{y\notin S}
     +\mathbf 1_{\phi^{-1}y\in S}.
\tag{2.4}
\]

Thus \(h\), and hence \(M\), is bijective if and only if

\[
       \mathbf 1_{y\in S}=\mathbf 1_{\phi^{-1}y\in S}
                         \quad(y\in\Omega),
\tag{2.5}
\]

which says exactly that \(S\) is a union of \(\phi\)-cycles. Conversely such
a union makes (2.4) equal to one for every \(y\). Uniqueness follows from the
outgoing arc at any source on a nontrivial component. \(\square\)

The cycles of \(\phi\) are the tail projections of the alternating even
cycles in the symmetric difference of the two bipartite successor matchings.

### Corollary 2.2 (exact window-signature criterion)

For a \(p\)- or \(q\)-window \(W\), inspect every noncommon arc in its full
dependency word. A \(p\)-arc forces shore \(0\) on the corresponding
\(\phi\)-cycle; a \(q\)-arc forces shore \(1\). Denote this partial bit
assignment by \(\operatorname{sig}(W)\).

A family \(\mathcal W\) of prescribed parent windows extends to a
one-in/one-out factor in the two-parent union if and only if:

1. every arc of every \(W\in\mathcal W\) belongs to the parent union; and
2. the signatures \(\operatorname{sig}(W)\) are consistent, meaning no
   \(\phi\)-cycle is forced to both \(0\) and \(1\).

Common arcs impose no sign. Prescribed linear endpoints are included by
protecting the appropriate dummy arcs.

#### Proof

Necessity is Theorem 2.1. Under consistency, set every forced component to
its prescribed shore and choose either shore on every unforced component.
Theorem 2.1 gives the required factor. \(\square\)

This is an exact degree theorem, not a Hamilton theorem.

## 3. Exact monodromy and cycle count

Write \(c(\sigma)\) for the number of cycles of a permutation \(\sigma\).
Let \(\sigma\in\operatorname{Sym}(\Omega)\), let
\(\varnothing\ne S\subseteq\Omega\), and let
\(\psi\in\operatorname{Sym}(\Omega)\) have support contained in \(S\).
Define

\[
 \alpha_{\sigma,S}(x)=\sigma^{j(x)}(x),
 \qquad
 j(x)=\min\{j\ge1:\sigma^j(x)\in S\}
 \quad(x\in S).
\tag{3.1}
\]

Thus \(\alpha_{\sigma,S}(x)\) is the next marked tail encountered after
\(x\) while following its directed \(\sigma\)-cycle.

### Lemma 3.1 (cut-segment cycle identity)

\[
 \boxed{
 c(\sigma\psi)
   =c(\sigma)-c(\alpha_{\sigma,S})
                  +c(\psi\alpha_{\sigma,S}).
 }
\tag{3.2}
\]

#### Proof

Cycles of \(\sigma\) disjoint from \(S\) are unchanged. For \(x\in S\), cut
the arc \(x\to\sigma(x)\), and let \(B_x\) be the directed segment beginning
at \(\sigma(x)\) and ending at \(\alpha_{\sigma,S}(x)\). These segments
partition the \(\sigma\)-cycles meeting \(S\).

Before switching, the transition between segment labels is

\[
                         x\longmapsto\alpha_{\sigma,S}(x),
\tag{3.3}
\]

so \(c(\alpha_{\sigma,S})\) is the number of affected old cycles. In
\(\sigma\psi\), after traversing \(B_x\) to
\(\alpha_{\sigma,S}(x)\), the new outgoing arc enters the segment
\(B_{\psi(\alpha_{\sigma,S}(x))}\). The new segment transition is

\[
                    x\longmapsto
                    \psi(\alpha_{\sigma,S}(x)).
\tag{3.4}
\]

The affected new cycles are therefore the cycles of
\(\psi\alpha_{\sigma,S}\). Adding back the unchanged cycles proves (3.2).
\(\square\)

Since \(p\) is one cycle, \(\alpha_{p,S}\) is one cycle on every nonempty
\(S\). Theorem 2.1 and Lemma 3.1 give the exact monodromy test

\[
 \boxed{
 c(p\phi_T)=c(\phi_T\alpha_{p,S}),
 \qquad S=\operatorname{supp}(\phi_T)\ne\varnothing.
 }
\tag{3.5}
\]

Thus \(p\phi_T\) is Hamilton if and only if
\(\phi_T\alpha_{p,S}\) is one cycle. For \(T=\varnothing\), the factor is the
Hamilton parent \(p\).

Two special cases will be used below.

* If \(\psi=(ab)\) and \(a,b\) lie on distinct \(\sigma\)-cycles, then
  \(\alpha_{\sigma,\{a,b\}}\) is the identity, and the switch merges those
  cycles.
* If \(a,b\) lie on one \(\sigma\)-cycle, then
  \(\alpha_{\sigma,\{a,b\}}=(ab)\), and the switch splits that cycle.

More generally, if \(\psi\) is an \(s\)-cycle with one support point on each
of \(s\) distinct \(\sigma\)-cycles, the switch merges all \(s\) cycles.

### Example 3.2 (degree compatibility is not Hamilton compatibility)

On \(\Omega=\{1,2,3,4,5,\partial\}\), let

\[
 p=(1\ 2\ 3\ 4\ 5\ \partial),
 \qquad
 \phi=(1\ 3)(2\ 4),
\tag{3.6}
\]

and \(q=p\phi=(1\ 4\ 3\ 2\ 5\ \partial)\). Both give Hamilton paths with
linear endpoints \(1,5\). Prescribe the \(q\)-arc \(1\to4\) and the \(p\)-arc
\(2\to3\). They force different, hence consistent, assignment components.
The unique forced factor is nevertheless

\[
              p(1\ 3)=(1\ 4\ 5\ \partial)(2\ 3),
\tag{3.7}
\]

which has two cycles. This remains a counterexample with an empty residence
forbidden family. Parent-pure supply, common endpoints, union connectivity,
and degree compatibility do not remove the monodromy gate.

The obstruction survives ordinary target-to-candidate Hall slack. Let

\[
\begin{aligned}
 P_0&=(a,1,2,3,4,5,6,b),\\
 P_1&=(a,1,4,5,3,2,6,b).
\end{aligned}
\tag{3.8}
\]

After dummy closure,

\[
 p_1=p_0(1\ 3)(2\ 5).
\tag{3.9}
\]

Give target \(z_1\) the two candidate arcs \(1\to4,3\to2\), both forcing
the \(P_1\)-shore of \((1\ 3)\), and target \(z_2\) the two candidate arcs
\(2\to3,5\to6\), both forcing the \(P_0\)-shore of \((2\ 5)\). Their
candidate graph has

\[
 |N(z_1)|=|N(z_2)|=2,\qquad
 |N(\{z_1,z_2\})|=4.
\tag{3.10}
\]

Nevertheless every choice of one candidate for each target forces

\[
 p_0(1\ 3)
  =(\partial\ a\ 1\ 4\ 5\ 6\ b)(2\ 3),
\tag{3.11}
\]

which is disconnected. Arbitrarily long common directed prefixes and
suffixes make all four candidates interior without changing the obstruction.
Thus even strong ordinary Hall slack in the union catalogue can forget the
common component sign and monodromy.

## 4. Residence is an exact ordered width-four condition

For a linear middle-mask word and a coordinate \(x\), write its binary trace.
Depth-three residence forbids an internal factor

\[
                         0\,1^j\,0,
                   \qquad 1\le j\le3.
\tag{4.1}
\]

Equivalently, if \(x\) is inserted on an arc, it may not be removed on any
of the next three arcs. Every minimal forbidden residence word has \(2\),
\(3\), or \(4\) directed arcs.

The condition is recognized, for each coordinate separately, by the ordered
automaton

\[
                         \{U,Z,1,2,3,L,\bot\}.
\tag{4.2}
\]

Here \(U\) means that no left zero has yet been seen, \(Z\) that the last
symbol is zero, \(j\) that a left-bracketed current one-run has length \(j\),
\(L\) that it has length at least four, and \(\bot\) is rejection. Its
transitions are

\[
\begin{array}{c|cc}
 &0&1\\ \hline
 U&Z&U\\
 Z&Z&1\\
 1&\bot&2\\
 2&\bot&3\\
 3&\bot&L\\
 L&Z&L.
\end{array}
\tag{4.3}
\]

Every nonrejecting terminal state is accepted because a short run meeting a
linear endpoint is legal. This is why the dummy must be deleted before the
residence word is read.

### Lemma 4.1 (exact signed residence projection)

In a two-parent overlay, introduce one bit for every nontrivial
\(\phi\)-cycle. Every forbidden residence path has exactly one of three
outcomes: it contains an arc outside the parent union and is automatically
unselectable; its shore requirements are inconsistent and it is again
unselectable; or it projects to one forbidden partial bit assignment involving
at most four component bits. Together with the unit assignments forced by
protected windows, the resulting clauses describe exactly the residence-safe
degree covers.

#### Proof

At its tail, each arc of a forbidden path is absent from the union, common to
both parents, exclusive to \(p\), or exclusive to \(q\). An exclusive arc
forces the corresponding component bit. If an arc is absent, the path is
automatically unselectable and contributes no clause. If two arcs force
opposite shores on one component, the whole path is likewise impossible.
Otherwise selecting every arc of the path is precisely the conjunction of
its distinct forced bits. There are at most as many bits as arcs, hence at
most four. Negating this conjunction gives the exact clause. Doing this for
every minimal forbidden path proves both directions. \(\square\)

### Theorem 4.2 (exact two-parent FIFO/residence criterion)

Let \(\mathcal W\) be prescribed full parent windows. There is a resident
directed Hamilton path in \(E(p)\cup E(q)\) retaining every window in
\(\mathcal W\) if and only if there is a union \(T\) of \(\phi\)-cycles such
that:

1. \(T\) extends every signature in \(\mathcal W\);
2. the linear word obtained from \(p\phi_T\) after deleting \(\partial\) is
   accepted by all coordinate residence automata; and
3. \(p\phi_T\) is one cycle, equivalently, for nonempty support,
   \(c(\phi_T\alpha_{p,S})=1\).

#### Proof

Theorem 2.1 and Corollary 2.2 are exactly the degree and window conditions.
Equations (4.1)--(4.3) are exactly linear residence. Equation (3.5) is
exactly Hamilton connectivity. Deleting the dummy converts the one cycle to
the desired linear path and introduces no physical residence seam. Every
step is reversible. \(\square\)

The theorem retains the ordered queue state exactly. It does not replace it
by independent arc marginals or an unordered port relaxation.

## 5. A sharp component-incidence obstruction

Fix a consistent forced shore assignment and let \(M_0\) be the resulting
cycle cover, with every still-free component initially on one chosen shore.
For a free component \(i\), let \(\psi_i\) be the relative permutation which
toggles that component. The supports of the \(\psi_i\) are disjoint.

Form a hypergraph \(\mathcal H(M_0)\) whose vertices are the directed cycles
of \(M_0\). The hyperedge for \(i\) consists of the \(M_0\)-cycles containing
points of \(\operatorname{supp}(\psi_i)\).

### Proposition 5.1 (incidence disconnection obstruction)

If \(\mathcal H(M_0)\) is disconnected, no setting of the remaining free
shore bits is Hamilton.

#### Proof

Let \(K\) be a connected component of \(\mathcal H(M_0)\), and let \(U_K\)
be the union of the vertices on its \(M_0\)-cycle nodes. The base successor
\(M_0\) preserves \(U_K\). Every toggle support lies wholly among cycle
nodes in one hypergraph component. Hence, for \(x\in U_K\), both \(x\) and
\(\psi_i(x)\) lie in \(U_K\), and so does \(M_0(\psi_i(x))\). Products of
the disjoint toggles preserve every nonempty \(U_K\). A permutation
preserving two such blocks cannot be one cycle. \(\square\)

Connectivity of \(\mathcal H(M_0)\) is necessary, not sufficient. The
orientation product in Lemma 3.1 can still split cycles, and a compound
setting can still violate residence.

## 6. Deterministic protected switch fusion

Let \(D\) be a digraph on \(\Omega\), and let \(M\) be a directed permutation
cover contained in \(D\). Suppose \(M\) has \(c\) directed cycles, contains a
protected arc set \(F\), and avoids every member of a local forbidden family
\(\mathcal R\), where

\[
                    |R|\le q\qquad(R\in\mathcal R).
\tag{6.1}
\]

A directed rectangle between two distinct \(M\)-cycles \(C,C'\) consists of
selected arcs

\[
                  a\to a^+=M(a),\qquad b\to b^+=M(b)
\tag{6.2}
\]

and available cross arcs

\[
                         a\to b^+,
                         \qquad b\to a^+.
\tag{6.3}
\]

### Theorem 6.1 (protected resident \(C_4\)-tree fusion)

Suppose there are \(c-1\) rectangles indexed by the edges of a tree on the
\(c\) initial \(M\)-cycles, satisfying:

1. all \(2(c-1)\) cut arcs in (6.2) are distinct and lie outside \(F\);
2. on each initial \(M\)-cycle, every segment between consecutive cut arcs
   contains at least \(q-1\) uncut \(M\)-arcs; with one cut on a cycle, its
   complementary segment contains \(|C|-1\) uncut arcs; and
3. every proposed seam in (6.3) is \(q\)-collar safe: for every
   \(i,j\ge0\) with \(i+j+1\le q\), the directed word consisting of \(i\)
   predecessor \(M\)-arcs, that seam, and \(j\) successor \(M\)-arcs contains
   no member of \(\mathcal R\).

Then simultaneously toggling all rectangles gives one directed Hamilton
cycle on \(\Omega\), contains \(F\), and is \(\mathcal R\)-safe. Deleting
\(\partial\) gives a directed Hamilton path retaining every protected window.

#### Proof

Distinct cut tails and heads imply that simultaneous replacement preserves
indegree and outdegree one. Toggle the tree edges in any forest order.
Inductively, each connected component of the processed forest corresponds to
one directed cycle. The next tree edge joins two different forest
components; its two still-selected cut arcs lie on their two cycles, and the
directed \(2\)-switch (6.3) merges those cycles. After all \(c-1\) edges,
there is one cycle. No protected arc was cut.

The final cycle is a concatenation of old \(M\)-segments and new seams.
Between consecutive seams there are at least \(q-1\) old arcs. A directed
word containing two seams therefore has at least

\[
                            1+(q-1)+1=q+1
\tag{6.4}
\]

arcs. Every final word of at most \(q\) arcs consequently contains no seam,
when it is an old safe word, or exactly one seam, when it is one of the
audited collars. This proves \(\mathcal R\)-safety. \(\square\)

A seam lies in

\[
                         \sum_{r=1}^{q}r
                         ={q(q+1)\over2}
\tag{6.5}
\]

oriented collar subwords of lengths at most \(q\). Each rectangle has two
seams, so at most \(q(q+1)\) collars are checked. For \(k=15\) depth-three
residence, \(q=4\): three unchanged arcs between cuts suffice and at most
twenty collars are checked per rectangle.

The use of \(c-1\) rectangles is optimal within a \(C_4\)-only, merge-only
scheme: one directed \(2\)-switch changes cycle count by exactly one.

### Corollary 6.2 (loose assignment-hypertree fusion)

Suppose instead that there are disjoint assignment switches
\(\psi_1,\ldots,\psi_t\), with \(\psi_j\) an \(s_j\)-cycle on its cut tails
and every replacement arc \(x\to M(\psi_j(x))\) belonging to \(D\).
Root the incidence hypergraph at one initial \(M\)-cycle. Assume the
\(s_j\) cut tails of each switch lie on \(s_j\) distinct current cycles:
exactly one of these cycles has already been reached and the other
\(s_j-1\) are new initial cycles. Assume also

\[
                         \sum_{j=1}^{t}(s_j-1)=c-1.
\tag{6.6}
\]

If the same cut separation and every new-seam collar condition of Theorem
6.1 hold, toggling all switches gives a protected resident Hamilton cycle.

#### Proof

At each rooted step, the switch has one support point on each of \(s_j\)
distinct current cycles. Lemma 3.1 merges precisely those \(s_j\) cycles.
Induction and (6.6) leave one cycle. The collar proof is unchanged.
\(\square\)

The tree and collar hypotheses are sufficient, not necessary; a compound
exchange can be safe even when its individual rectangles are unsafe.

### Lemma 6.3 (bounded damage from protected arcs)

Let \(D\) be the union of \(r\) successor permutations, and fix a cover \(M\)
in \(D\). A selected arc \(u\to M(u)\) belongs to at most \(r-1\) directed
\(C_4\) rectangles relative to \(M\). Hence \(K\) protected selected arcs
delete at most \(K(r-1)\) such rectangles.

#### Proof

In a rectangle using \(u\to M(u)\), choose the alternative head
\(y\in N_D^+(u)\setminus\{M(u)\}\). There are at most \(r-1\) choices.
The other selected tail is forced to be \(M^{-1}(y)\); only the presence of
its cross arc to \(M(u)\) remains to be checked. Thus each \(y\) gives at
most one rectangle. The union bound proves the last assertion. \(\square\)

For two parents, protecting seven \(10\)- to \(12\)-vertex dependency words
protects at most \(7\cdot11=77\) arcs and therefore destroys at most 77
candidate rectangles. This is only a bounded-damage statement. It does not
prove that the remaining safe exchange graph contains a spanning tree.

## 7. An intact-block theorem for \(O(1)\) resident parents

Let \(P_1,\ldots,P_r\), with fixed \(r=O(1)\), be resident directed Hamilton
parents on \(V\), and let \(D\) be their directed arc union. Suppose
\(B_1,\ldots,B_b\) are intact oriented parent subpaths such that:

1. their vertex sets partition \(V\);
2. every internal block arc belongs to \(D\); and
3. every prescribed full dependency window lies intact in one block.

### Theorem 7.1 (exact ordered block recurrence)

Within the class of paths obtained by concatenating the blocks without
reversing them, the existence of a resident directed Hamilton path retaining
all prescribed windows is characterized exactly by the following recurrence.

A state is

\[
                         (S,i,\omega),
\tag{7.1}
\]

where \(S\subseteq[b]\), \(i\in S\), and \(\omega\) is the product state of
the fifteen ordered automata (4.3) after reading a concatenation of precisely
the blocks in \(S\), ending in \(B_i\). From \((S,i,\omega)\) one may append
\(B_j\), \(j\notin S\), exactly when

\[
          \operatorname{last}(B_i)\to\operatorname{first}(B_j)\in E(D)
\tag{7.2}
\]

and feeding the seam and \(B_j\) from state \(\omega\) does not reject. A
full accepting state with \(S=[b]\) exists if and only if the desired
intact-block path exists.

The base states are

\[
                 (\{i\},i,\omega_i)\qquad(1\le i\le b),
\tag{7.3}
\]

where \(\omega_i\) is obtained by feeding \(B_i\) from the all-\(U\) initial
state and the base state is omitted if that feed rejects.

#### Proof

Every recurrence transition appends one unused vertex-disjoint block through
an available directed union arc, so a full state gives a spanning directed
path. The automaton state is the exact ordered residence history, and item 3
retains every protected window. Conversely, read any valid intact-block
concatenation from left to right. Its successive prefixes give exactly the
states and transitions above. \(\square\)

This theorem remains exact when short blocks allow one residence word to
cross two or more seams.

For a coordinate \(x\), let

\[
 \tau_x(B)=\text{length of the terminal one-run in the \(x\)-trace of \(B\)},
\tag{7.4}
\]

and define \(\iota_x(B)\) analogously for the initial one-run. Zero is used
when the relevant endpoint bit is zero.

### Corollary 7.2 (semicomplete safe-seam coupling)

Assume every block contains at least four vertices. Put a directed edge
\(B\to C\) in the seam graph \(\Gamma\) exactly when:

1. \(\operatorname{last}(B)\to\operatorname{first}(C)\in E(D)\); and
2. for every coordinate \(x\),

\[
                    \tau_x(B)+\iota_x(C)\notin\{1,2,3\}.
\tag{7.5}
\]

If \(\Gamma\) is semicomplete, meaning that between every two distinct blocks
at least one direction is present, then the blocks have a resident directed
Hamilton concatenation retaining all protected windows.

#### Proof

Every new short one-run crossing one seam is the terminal run of the left
block followed by the initial run of the right block, so (7.5) is the exact
one-seam residence test. A forbidden residence factor has at most five
vertices. A factor crossing two seams would contain all of the intermediate
block plus at least one vertex on each side, hence at least six vertices.
Thus residence can be checked one seam at a time.

Choose one available orientation between every pair of blocks. The result is
a tournament. Every tournament has a directed Hamilton path: insert vertices
inductively into an existing directed path immediately before the first
vertex which they dominate, or at the end if there is none. Its edges belong
to \(\Gamma\), and concatenating its block order proves the claim. \(\square\)

The semicomplete hypothesis is explicit. It is not inferred from parent
density or DM slack.

### Corollary 7.3 (the \(92\)-block reduction)

Choose one full interior \(\tau H29\) dependency interval for each of the
seven old zero targets. Merge overlapping intervals along the \(\tau H29\)
order. They give at most seven foreign blocks and contain at most
\(7\cdot12=84\) vertices. Delete those vertices from the \(H29\) order and
use the maximal remaining \(H29\)-runs as base blocks. Deleting at most 84
vertices creates at most 85 nonempty runs. Hence the two families partition
all 6,435 vertices into at most

\[
                              7+85=92
\tag{7.6}
\]

intact parent blocks.

Theorem 7.1 is a faithful finite coupling criterion for this choice.
Corollary 7.2 applies only if its length and semicomplete-seam hypotheses are
proved. If incumbent \(H29\) windows are also prescribed, their complete
dependency words must remain intact in this partition; an overlap forcing
incompatible arcs is an immediate obstruction.

## 8. General small-family exact boundary

Let \(D\) be the directed union of any fixed number of parent paths after
dummy closure, and let \(F\) be a forced arc set. There is a Hamilton cycle
containing \(F\) and avoiding a local forbidden family \(\mathcal R\) if and
only if there are binary variables \(x_e\in\{0,1\}\), \(e\in E(D)\),
satisfying

\[
 \sum_{e\in\delta^+(v)}x_e
 =\sum_{e\in\delta^-(v)}x_e=1
                         \qquad(v\in\Omega),
\tag{8.1}
\]

\[
                         x_e=1\qquad(e\in F),
\tag{8.2}
\]

\[
                  \sum_{e\in R}x_e\le |R|-1
                         \qquad(R\in\mathcal R),
\tag{8.3}
\]

and all directed subtour inequalities

\[
 \sum_{u\in S,\ v\notin S}x_{uv}\ge1
 \quad
 (\varnothing\ne S\subsetneq\Omega).
\tag{8.4}
\]

Equations (8.1) give a cycle cover, (8.4) says it has one cycle, and
(8.2)--(8.3) are precisely window retention and local safety.

After deleting the fixed tails and heads of \(F\), ordinary bipartite Hall
inequalities characterize extension to a cycle cover. They do not imply
(8.4). Theorem 6.1 and Corollary 6.2 give deterministic sufficient ways to
supply the missing connectivity while retaining ordered residence.

## 9. Coordinate-conjugacy obstruction

Suppose

\[
                         q=\tau p\tau^{-1},
                  \qquad \tau(\partial)=\partial,
\tag{9.1}
\]

with \(\tau\) a nonidentity coordinate relabel. Then

\[
                         \phi=p^{-1}\tau p\tau^{-1}
\tag{9.2}
\]

is the exact commutator whose cycles carry the shore bits.

### Proposition 9.1 (no relabel-invariant Hamilton selection)

For nonidentity \(\tau\), no \(\tau\)-invariant selected directed matching in
\(E(p)\cup E(\tau p\tau^{-1})\) is one Hamilton cycle.

#### Proof

Let \(h\) be the successor permutation of such a matching. Directed-edge
invariance gives

\[
                          h\tau=\tau h.
\tag{9.3}
\]

If \(h\) were one cycle on \(\Omega\), its centralizer in
\(\operatorname{Sym}(\Omega)\) would be the cyclic group generated by \(h\).
Thus \(\tau=h^j\) for some \(j\). Since \(\tau\) fixes \(\partial\), the
power \(h^j\) fixes a point of the \(h\)-cycle, which forces
\(j\equiv0\pmod{|\Omega|}\). Hence \(\tau\) would be the identity, a
contradiction. \(\square\)

Therefore a successful \(H29,\tau H29\) coupling must break the natural
relabel symmetry. The proposition rules out only selections whose final
directed matching is \(\tau\)-invariant; it does not rule out asymmetric
shore choices.

## 10. Exact resource and DM ledger

Coordinate relabelling is an isomorphism of the full target--physical-cell
incidence graph. It preserves maximum matching size and total Hall
deficiency. Thus \(\tau H29\) can have strong slack on the old displayed DM
shore and candidates for all old point zeros while moving the deficiency to
relabelled targets.

### Proposition 10.1 (protected physical matching)

If every arc in the full dependency word of a family of physical compiler
cells is put in the protected set \(F\), every one of those incidences
survives Theorem 6.1 exactly. In particular, an explicitly injective
target-to-cell matching whose cells are all protected remains injective after
fusion.

#### Proof

No protected arc is cut. Each protected dependency word remains an unchanged
consecutive directed segment, with the same designated physical cell and
target incidences. \(\square\)

### Proposition 10.2 (local-window loss bound)

Suppose cell type \(\theta\) is indexed by a start position and determined by
exactly \(\ell_\theta\) consecutive vertices. If a rethreading cuts \(b\) old
successor arcs, let \(\Delta_{\partial,A}\) be the number of old
\(A\)-neighbour cells which can be lost solely because the linear endpoint or
dummy collar changes. Then, for every target shore \(A\),

\[
 h_A(\text{after})
 \ge
 h_A(\text{before})
      -b\sum_\theta(\ell_\theta-1)-\Delta_{\partial,A}.
\tag{10.1}
\]

If the complete endpoint/dummy collar is protected, then
\(\Delta_{\partial,A}=0\).

#### Proof

An old local cell can be lost only if its defining interval crosses a cut
arc. For type \(\theta\), a fixed cut arc belongs to exactly
\(\ell_\theta-1\) cyclic intervals of length \(\ell_\theta\). The union bound
therefore gives the displayed maximum number of lost cells. Deleting cells
can decrease a neighborhood cardinality by at most their number; new cells
can only improve it. The separately defined
\(\Delta_{\partial,A}\) bounds the remaining endpoint-only losses.
\(\square\)

For \(C_4\)-tree fusion, \(b=2(c-1)\). Thus the all-shore condition

\[
 h_A(\text{before})-|A|
 \ge
 2(c-1)\sum_\theta(\ell_\theta-1)+\Delta_{\partial,A}
                       \qquad\text{for every Hall shore }A
\tag{10.2}
\]

would preserve Hall. Slack for one canonical DM block is not (10.2), and
several locally positive windows may use the same physical capacity. Without
an all-shore bound, Proposition 10.1 or a direct post-switch physical Hall
proof is mandatory. The same qualification applies to upper shadows.

## 11. Application to \(H29\) and \(\tau=(1,12)\)

Let \(P=H29\), \(Q=\tau H29\), and let \(p,q\) be their dummy-closed
successors. The supplied old zero set is

\[
\begin{split}
 Z_6&=\{2575,13616,17738,21641,29776\},\\
 Z_7&=\{5801,13620\}.
\end{split}
\tag{11.1}
\]

By equivariance, the zero set of \(Q\) is \(\tau Z\). The new input that
\(Q\) has an interior candidate for every \(z\in Z\) implies

\[
                             Z\cap\tau Z=\varnothing.
\tag{11.2}
\]

Consequently \(P\) has candidates on every target in \(\tau Z\). A minimal
point-zero repair genuinely using both parents would protect \(Q\)-windows
for \(Z\) and \(P\)-windows for \(\tau Z\). Full Hall repair requires a
larger, statewise family of protected cells.

For a candidate word \(W\), let

\[
 \Gamma_\phi(W)=
 \{\text{nontrivial cycles of }\phi
       \text{ touched by an exclusive arc of }W\}.
\tag{11.3}
\]

If \(W_z^Q\) and \(W_y^P\) are chosen for \(z\in Z\) and
\(y\in\tau Z\), respectively, their degree-one compatibility is exactly

\[
 \left(\bigcup_{z\in Z}\Gamma_\phi(W_z^Q)\right)
 \cap
 \left(\bigcup_{y\in\tau Z}\Gamma_\phi(W_y^P)\right)
                         =\varnothing,
\tag{11.4}
\]

with the additional requirement that no individual word has an internal
signature conflict. Equation (11.4) is necessary and sufficient for a
successor cycle cover, not for a Hamilton path.

After (11.4), one must pass, in order:

1. every width-four residence clause of Lemma 4.1;
2. the monodromy test (3.5), or Proposition 5.1 followed by a positive
   fusion certificate from Section 6;
3. preservation of every complete compiler dependency word and required
   upper witness; and
4. Proposition 10.1, the all-shore inequality (10.2), or a direct exact
   post-switch physical Hall proof.

The supplied facts establish local candidate existence and reported DM
slack. They do not specify the signatures in (11.3), a common consistent
tuple containing the incumbent cells, the cycles of the forced cover, a safe
spanning tree/hypertree, or an all-shore Hall ledger. Therefore no mixed
Hall-zero \(k=15\) carrier is claimed here.

If only the seven \(Q\)-windows for the old zeros are prescribed, \(Q\)
itself is already a resident Hamilton parent retaining all seven. Calling
that a coupling result would hide the actual issue: \(Q\) has the relabelled
Hall deficiency of \(P\). The hard gate is simultaneous retention of
complementary \(P\)-capacity and global statewise Hall.

Finally, the previously recorded multiplicity vector

\[
                         (4,1,2,1,3,3,3)
\tag{11.5}
\]

belongs to the older transposition \((10,11)\), not to (0.1). It is not used
here and must not be transferred without a separate exact audit.

## 12. Proved boundary and next certificate

The following claims are proved.

1. Two-parent degree factors are classified exactly by whole
   \(\phi=p^{-1}q\) orbit signs.
2. Full prescribed windows are degree-compatible exactly when their signed
   component requirements are consistent.
3. Formula (3.2) gives the exact monodromy of every component switch.
4. Residence projects exactly to clauses of width at most four and is
   retained exactly by the ordered automata (4.3).
5. A disconnected optional-switch incidence hypergraph is a structural
   obstruction to Hamilton completion.
6. A protected, three-separated, collar-safe \(C_4\) spanning tree, or the
   stated loose assignment hypertree, constructs a resident Hamilton path.
7. The intact-block recurrence is exact; semicomplete safe seams give a
   deterministic positive theorem.
8. Seven length-at-most-twelve foreign windows reduce to at most 92 intact
   blocks with the base parent.
9. A relabel-invariant shore selection is never Hamilton for nonidentity
   \(\tau\) fixing the dummy.
10. Protected physical compiler matchings and the local-window loss bound
    give the exact legitimate uses of DM slack.

The unresolved instance-specific certificate is finite and explicit:

* materialize the actual oriented dependency word of every selected
  \(P\)- and \(Q\)-candidate;
* record its \(\phi\)-component/sign signature;
* exhibit one consistent tuple containing the incumbent physical cells that
  must survive;
* decompose the forced successor permutation into cycles;
* exhibit a depth-three-collar-safe spanning tree/hypertree avoiding the
  protected words, or prove the optional incidence hypergraph disconnected;
  and
* give an explicit protected target-to-cell matching or an all-shore
  post-switch Hall ledger.

Candidate counts and marginal DM slack alone are rigorously insufficient, as
Example 3.2 and Proposition 9.1 show. Conversely, the listed positive
certificate would be a complete deterministic FIFO/residence coupling proof;
no further connectivity or chronology lemma would remain.

## 13. Adversarial audit record

An independent hand audit checked the composition order in Lemma 3.1, the
incidence obstruction, every fusion step and collar constant, the
semicomplete block argument, the \(77\)-arc and \(92\)-block counts, the
subtour formulation, the conjugacy obstruction, and the \(H29,\tau H29\)
scope. Three corrections found by that audit are incorporated above:

1. Lemma 4.1 explicitly separates paths containing an arc absent from the
   parent union;
2. Theorem 7.1 explicitly initializes every singleton block state; and
3. Proposition 10.2 and (10.2) retain the endpoint-loss term
   \(\Delta_{\partial,A}\).

No additional claim about the concrete \((1,12)\) overlay is inferred from
the audit. Its safe spanning tree/hypertree and all-shore physical Hall
certificate remain the exact unproved instance-specific data.
