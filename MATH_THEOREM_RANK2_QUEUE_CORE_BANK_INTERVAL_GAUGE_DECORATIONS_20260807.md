# A fixed rank-two queue owner cycle has exponentially many all-depth literal antecedents

**Date:** 2026-08-07  
**Method:** exact maximal carrier intervals and independent core--bank
interval exchanges  
**Status:** unconditional nonrigidity theorem. A fixed \(3p\)-owner
rank-two queue cycle supports at least \(2^{3p}\) distinct literal source
inventories while preserving the owner cycle, flatness, owner residence,
q1 palettes, every proper suffix rank, and fixed-depth target simplicity.
It does not select a pairwise target-disjoint decoration for every owner
translate.

## 1. The fixed owner cycle

Let

\[
 L=3p,\qquad c=m-2p,
\tag{1.1}
\]

and choose a core \(K\) of size \(c\) and pairwise disjoint ordered
triples

\[
 T_a=\{x_{a,0},x_{a,1},x_{a,2}\},
 \qquad a\in\mathbb Z_p.
\tag{1.2}
\]

Index source positions by \(\mathbb Z_L\). At position

\[
 t=a+qp,\qquad a\in\mathbb Z_p,\quad q\in\mathbb Z_3,
\tag{1.3}
\]

put the canonical source letter

\[
 C_t=K\cup\bigl(T_a\setminus\{x_{a,q}\}\bigr).
\tag{1.4}
\]

Its owner cycle is

\[
 O_i=\bigcup_{t=i}^{i+p-1}C_t,
 \qquad i\in\mathbb Z_L.
\tag{1.5}
\]

Every \(O_i\) has rank \(m\), consecutive owners are Johnson adjacent,
and every bank coordinate has owner run \(2p\) and gap \(p\).

For a bank coordinate \(x=x_{a,r}\), its two canonical source
occurrences are the consecutive phase-\(a\) positions

\[
 u_x=a+(r+1)p,\qquad u_x+p
\tag{1.6}
\]

with all indices taken modulo \(L\). Define its closed carrier arc and
open interior by

\[
 J_x=\{u_x,u_x+1,\ldots,u_x+p\},
\qquad
 I_x=\{u_x+1,\ldots,u_x+p-1\}.
\tag{1.7}
\]

Thus \(|J_x|=p+1\) and \(|I_x|=p-1\).

## 2. Exact maximal carriers

For a source position \(t\), let

\[
 P_t=\bigcap_{\substack{i\in\mathbb Z_L\\t\in[i,i+p-1]}}O_i
\tag{2.1}
\]

be its pointwise maximal antecedent envelope.

### Lemma 2.1 (bank carrier interval)

For every bank coordinate \(x\),

\[
 \boxed{x\in P_t\iff t\in J_x.}
\tag{2.2}
\]

Every core coordinate belongs to every \(P_t\).

#### Proof

A \(p\)-position source window contains \(x\) in the canonical word
precisely when it contains one of the two occurrence positions
\(u_x,u_x+p\). A position \(t\in J_x\) has the property that every
\(p\)-window containing \(t\) contains at least one of those endpoints:
the open gap between them has only \(p-1\) positions. Hence \(x\in P_t\).

If \(t\notin J_x\), then \(t\) lies on the other open arc, of length
\(2p-1\). One can choose a \(p\)-window containing \(t\) and avoiding
both \(u_x\) and \(u_x+p\). Its owner omits \(x\), so \(x\notin P_t\).
Core coordinates occur in every owner. \(\square\)

At a position \(t\) of phase \(a\), the two coordinates in the active
block \(C_t\cap T_a\) are endpoints of their carrier arcs. For every
other phase \(b\ne a\), the position \(t\) lies in exactly one interior
\(I_x\), namely the interval between two consecutive phase-\(b\)
updates. Consequently

\[
 |P_t|=c+2+(p-1)=c+p+1.
\tag{2.3}
\]

Thus the canonical rank-\((c+2)\) letter is far from the maximal
antecedent envelope.

The two endpoint occurrences \(u_x,u_x+p\) are nevertheless mandatory in
every antecedent inducing (1.5): the first and last owners in the
length-\(2p\) positive owner run of \(x\) have, respectively, only those
two source positions available as carriers.

## 3. One exact core--bank gauge switch

Fix \(x\in\bigcup_aT_a\) and \(k\in K\). Define a new source word
\(C^{(k,x)}\) by

\[
 C^{(k,x)}_t=
 \begin{cases}
  (C_t\setminus\{k\})\cup\{x\},&t\in I_x,\\
  C_t,&t\notin I_x.
 \end{cases}
\tag{3.1}
\]

The exchanged coordinates are distinct, and \(x\notin C_t\) on \(I_x\),
so every source letter keeps its old rank.

### Theorem 3.1 (single-switch invariance)

The switch (3.1) has all of the following properties.

1. Every \(p\)-window has exactly the same union value as before. Hence
   the complete owner cycle (1.5), its q1 palettes, and its owner
   residence are unchanged.
2. Every cyclic source interval \(Q\) of length \(1\le j\le p\) has the
   same union rank as before.
3. For \(j<p\), the switch changes the value on \(Q\) exactly when
   \(Q\subseteq I_x\); in that case it replaces \(k\) by \(x\).

#### Proof

The only changed coordinates are \(k\) and \(x\). The coordinate \(k\)
is deleted on the open interval \(I_x\), which has length \(p-1\).
Therefore every \(p\)-window still contains \(k\).

The coordinate \(x\) is added only on \(I_x\). Every \(p\)-window meeting
\(I_x\) contains one of the endpoints \(u_x,u_x+p\), where the canonical
word already contains \(x\). Thus no owner gains \(x\), proving part 1.

Now let \(Q\) be any cyclic interval of length at most \(p\). Relative to
the canonical word, its union loses \(k\) exactly when

\[
 Q\subseteq I_x.
\tag{3.2}
\]

It gains \(x\) exactly when it meets \(I_x\) but contains neither endpoint
\(u_x,u_x+p\). Since \(Q\) is contiguous and has length at most \(p\),
this condition is also exactly (3.2): an interval cannot leave \(I_x\)
without crossing one of its endpoints. Hence the loss and gain occur
together and cancel in cardinality. This proves part 2 and the value
statement in part 3. For \(j=p\), containment in \(I_x\) is impossible,
which recovers the exact owner-value assertion. \(\square\)

## 4. Independent simultaneous switches

Assume

\[
 c\ge3p,
\tag{4.1}
\]

which holds for all sufficiently large triangular parameters. Choose an
injection

\[
 \kappa:\bigcup_{a\in\mathbb Z_p}T_a\longrightarrow K.
\tag{4.2}
\]

For any subset \(E\) of the \(3p\) bank coordinates, apply (3.1)
simultaneously for all pairs

\[
 (\kappa(x),x),\qquad x\in E,
\tag{4.3}
\]

and denote the resulting word by \(C^E\).

### Theorem 4.1 (exponential all-depth decoration family)

The \(2^{3p}\) words \(C^E\) satisfy:

1. \(D^{p-1}C^E=O\) for the same literal owner cycle \(O\);
2. every length-\(j\) source union has rank

   \[
   c+2j,\qquad 1\le j\le p;
   \tag{4.4}
   \]

3. at each fixed proper depth \(1\le j<p\), all \(3p\) cyclic
   length-\(j\) targets are distinct;
4. the target inventories are distinct for all \(2^{3p}\) choices of
   \(E\), already at the singleton row and, separately, at every fixed
   proper depth.

#### Proof

The coordinate pairs in (4.3) are disjoint. Owner-value invariance and
the interval-rank identities of Theorem 3.1 therefore compose
coordinatewise, proving parts 1--2.

Consider a proper interval \(Q\) of length \(j<p\). It contains source
positions from exactly \(j\) consecutive phases. In each active phase,
its intersection with that phase triple remains the canonical two-block:
no interval \(I_x\) of that phase contains a phase position. In every
inactive phase, \(Q\) lies in the gap between two consecutive updates and
is contained in at most one of the three intervals \(I_x\). Hence its
intersection with an active phase triple has size two, while its
intersection with an inactive phase triple has size zero or one.

The set of active phases is therefore recovered from the target value as
the phase triples contributing two coordinates. It recovers the proper
cyclic phase interval. The three occurrences of that interval in one
ring have different canonical two-blocks in every active phase, and the
switches do not alter those active-phase blocks. Thus they remain
distinct, proving part 3.

For any proper depth \(j\), intersect all \(3p\) depth-\(j\) target
values. An unselected core coordinate belongs to every target. If
\(x\in E\), then \(\kappa(x)\) is absent from every \(j\)-interval
contained in \(I_x\), and such intervals exist because \(j\le p-1\).
No bank coordinate belongs to every target. Consequently

\[
 \bigcap_{\substack{Q\text{ cyclic}\\|Q|=j}}
       \bigcup_{t\in Q}C^E_t
 =K\setminus\kappa(E).
\tag{4.5}
\]

The right side recovers \(E\). Hence the inventories are pairwise
different at every proper depth, proving part 4. \(\square\)

## 5. Consequences and exact boundary

The fixed-owner antecedent is therefore highly nonrigid:

\[
 \boxed{
 \text{one fixed }3p\text{-owner ring supports at least }2^{3p}
 \text{ exact all-depth source decorations}.}
\tag{5.1}
\]

The canonical \(3p\)-target obstruction is not intrinsic to the owner
factor. It is an artifact of insisting that the permanent core occur in
every source letter and that bank coordinates occur only at their two
mandatory phase endpoints.

The construction preserves:

1. the exact owner values and owner order;
2. flatness and Johnson adjacency;
3. both owner q1 palettes;
4. owner run/gap residence;
5. the complete rank-two suffix profile;
6. fixed-depth target simplicity within the ring.

It does **not** yet prove that one can choose decorations for
\(\Theta(W/p)\) owner-disjoint rings so that their named targets are
globally disjoint at every depth. The next exact problem is a decoration
matching: choose one subset \(E\) (and, if useful, one injection
\(\kappa\)) for each selected owner ring, subject to cross-ring target
disjointness and the later fusion/compiler constraints.
