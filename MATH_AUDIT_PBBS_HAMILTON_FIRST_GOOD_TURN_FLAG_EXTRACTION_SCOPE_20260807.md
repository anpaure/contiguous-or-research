# Audit of Hamilton-first good-turn flag extraction

**Date:** 2026-08-07  
**Audited source:**  
MATH_THEOREM_PBBS_HAMILTON_FIRST_GOOD_TURN_FLAG_EXTRACTION_20260807.md

**Verdict:** the good-turn normal form, abundance bound, sparse
resource-disjoint extraction, and distinct flag/target choices all pass.
The result is an unconditional abstract co-chosen host theorem.  It does
not currently bypass the PBBS factor gate, because the extracted boundary
targets have not been shown to lie in the feasible face of the residual
Ferrers containment flow, much less in one nested flag/compiler flow.

## 1. Four-label normal form

Write consecutive rank-\(m\) owners on a middle-levels Hamilton cycle as

\[
 T_{i-1},\ T_i,\ T_{i+1},
\tag{1.1}
\]

and define

\[
 \begin{aligned}
 T_{i-1}-T_i&=\{x_i\},&
 T_i-T_{i-1}&=\{y_i\},\\
 T_i-T_{i+1}&=\{u_i\},&
 T_{i+1}-T_i&=\{v_i\}.
 \end{aligned}
\tag{1.2}
\]

Then

\[
 I_{i-1}=T_i-\{y_i\},\qquad
 I_i=T_i-\{u_i\}.
\tag{1.3}
\]

Thus \(I_{i-1}\ne I_i\) is exactly \(u_i\ne y_i\).  At such a good turn,

\[
 R_i=T_i\setminus\{u_i,y_i\}
\tag{1.4}
\]

has rank \(m-2\), and

\[
 \begin{aligned}
 T_{i-1}&=R_i\cup\{u_i,x_i\},\\
 T_i&=R_i\cup\{u_i,y_i\},\\
 T_{i+1}&=R_i\cup\{y_i,v_i\}.
 \end{aligned}
\tag{1.5}
\]

The four labels are pairwise distinct.  All comparisons except
\(x_i\ne v_i\) follow from membership in \(T_i\); if \(x_i=v_i\), then

\[
 J_{i-1}=T_i\cup\{x_i\}=T_i\cup\{v_i\}=J_i,
\tag{1.6}
\]

contradicting the distinct upper vertices of the Hamilton cycle.

Choosing any \(d\)-set \(C_i\subset R_i\) and putting

\[
 M_i=R_i\setminus C_i,\qquad U_i=M_i\cup\{u_i\}
\tag{1.7}
\]

therefore gives exactly the set-valued owner, lower, upper, and forced
coatom rows of a clean lag-two packet.  This is an abstract resource
packet; its individual literal collar exists, but the Hamilton cycle
itself is not yet a common source antecedent.

## 2. Good-turn load and count

Fix a rank-\((m-1)\) lower colour \(I\).  The rank-\(m\) owners containing
\(I\) form a clique of size

\[
 (2m+1)-(m-1)=m+2
\tag{2.1}
\]

in the Johnson graph.  The Hamilton owner cycle's edges having
intersection \(I\) form a maximum-degree-two subgraph on those vertices.
It cannot contain a cycle component: every vertex of such a component
would already use both of its Hamilton-cycle edges internally, so the
component would be the entire Hamilton owner cycle, impossible because
\(W>m+2\).  Hence the coloured subgraph is a linear forest and has at
most

\[
 (m+2)-1=m+1
\tag{2.2}
\]

edges.  Lemma 3.1 passes.

In the cyclic word

\[
 I_0,I_1,\ldots,I_{W-1},
\tag{2.3}
\]

every constant run has length at most \(m+1\).  A good turn is precisely
a boundary between two runs.  Therefore

\[
 g\ge\left\lceil\frac{W}{m+1}\right\rceil.
\tag{2.4}
\]

This bound and its cyclic endpoint convention are correct.

## 3. Sparse resource-disjoint extraction

A selected turn \(i\) uses owner indices \(i-1,i,i+1\), so cyclic
distance at most two excludes at most five turn indices, including \(i\).

A fixed lower colour occurs at no more than \(m+1\) edge indices.  Each
such edge index can occur as the left or right lower colour of at most two
turn indices.  Consequently either selected lower colour forbids at most
\(2(m+1)\) future turns.  Both colours together, plus owner spacing,
remove at most

\[
 4(m+1)+5
\tag{3.1}
\]

candidates.  The greedy condition

\[
 h\,[4(m+1)+5]<\frac{W}{m+1}
\tag{3.2}
\]

is therefore sufficient.  Since

\[
 h\le\binom{d+1}{2}=O(m)
\tag{3.3}
\]

and \(W/(m+1)\) is exponential, it holds for all sufficiently large
optimal parameters.

The selected owner triples, upper pairs, and two lower colours are
pairwise disjoint in their respective ranks.  Their four-incidence-edge
paths are literal subpaths of the fixed Hamilton cycle.  Thus no
protected-factor extension is needed **for this co-chosen abstract
packet bank**.

## 4. Flag and boundary-target choices

For one selected turn there are

\[
 \binom{m-2}{d}
\tag{4.1}
\]

choices of \(C_i\).

A previous bottom \(M_j\) forbids at most the unique choice

\[
 C_i=R_i\setminus M_j
\tag{4.2}
\]

when that difference is a valid \(d\)-set.  A previous top \(U_j\) also
forbids at most one choice: equality

\[
 M_i\cup\{u_i\}=U_j
\tag{4.3}
\]

forces \(M_i=U_j\setminus\{u_i\}\), if possible.  Hence at step \(i\)
there are at most \(2(i-1)\), and at the last step at most
\(2(h-1)\), forbidden choices.  The hypothesis

\[
 \binom{m-2}{d}>2(h-1)
\tag{4.4}
\]

is sufficient.

The source proof should say “at most \(2(h-1)\)” rather than “fewer than
\(2(h-1)\),” but its strict inequality (4.4) already has the correct
margin, so the theorem is unaffected.

For prescribed boundary ranks \(1\le s_j\le a=|M_j|\), distinct targets

\[
 S_j\in\binom{M_j}{s_j}
\tag{4.5}
\]

can also be selected.  At a fixed rank \(s<a\),
\(\binom as\ge a>h\) eventually; at rank \(a\), the only choice is
\(S_j=M_j\), and the \(M_j\)'s are already distinct.  Corollary 5.2
passes exactly at the level stated.

## 5. The decisive PBBS quantifier

The proved statement has the form

\[
 \boxed{
 \forall\text{ Hamilton cycles }H\
 \exists(\mathcal T,\mathcal B):
 \text{ the abstract packet paths of }\mathcal T\text{ lie in }H,}
\tag{5.1}
\]

where \(\mathcal T\) is a small co-chosen flag bank and
\(\mathcal B=\{S_j\}\) is a distinct rank-profiled target family contained
in its bottoms.

The existing exact Ferrers theorem has a different existential
correlation.  It chooses boundary targets jointly with a residual
capacity-\(d\) containment assignment:

\[
 \exists(\mathcal B,\Phi):
 \mathcal B\text{ has the Ferrers profile and }
 \Phi\text{ assigns every residual target to a containing owner.}
\tag{5.2}
\]

It does **not** say that every preselected family \(\mathcal B\) with the
right rank counts extends to such a \(\Phi\).  Once the boundary targets
are frozen inside the Hamilton-extracted \(M_j\)'s, the uniform fractional
flow used by the Ferrers theorem is no longer available automatically.
The residual containment Hall cuts must be checked again.

Moreover, PBBS needs more than (5.2): targets assigned to one owner must
form a nested suffix flag, the flags must admit one common compiler, and
the complete top chronology must have one literal width-\(L\) antecedent.

Consequently neither PBBS existential freedom nor the ability to choose
the Hamilton cycle first presently closes the gap.  It permits a
potentially useful reordering of the construction, but a new joint
selection theorem is required.

## 6. Exact remaining lemma

The first missing co-selection statement can be written as follows.

> **Hamilton--Ferrers intersection lemma.**  
> Given the optimal Ferrers rank profile with
> \(h\le\binom{d+1}{2}\), choose one middle-levels Hamilton cycle, \(h\)
> well-spaced good turns, sets \(C_i\subset R_i\), and prescribed-rank
> targets \(S_i\subset M_i=R_i\setminus C_i\), such that deleting the
> \(S_i\)'s leaves a capacity-\(d\) containment assignment of every
> residual lower target.

This lemma would genuinely remove the protected-factor extension gate at
the ordinary containment level: all complete packet paths would already
lie in the Hamilton cycle.

For the actual PBBS implication it must be strengthened further:

1. every residual owner fibre is a strict chain of length at most \(d\);
2. those chains and the selected promotion flags have one literal lower
   compiler;
3. the Hamilton owner/upper cycle admits one width-\(d+2\) source
   antecedent containing the isolated packet collars; and
4. residence, common-cap, and deeper-upper rows survive.

The current Ferrers flag-hypergraph theorem identifies item 1 as a
non-TU configuration-matching problem.  Thus the Hamilton-first note has
not made the sharp lower correlation automatic; it has moved the
protected-factor question into a Hamilton/Ferrers feasible-face
intersection.

## 7. Confidence impact

The note is mathematically useful: good turns are exponentially abundant,
and an \(O(d^2)\) abstract complete-packet bank can always be chosen
inside one Hamilton cycle.  This shows that owner and immediate-upper
geometry are not intrinsically hostile to the promotions.

The proof-status impact is nevertheless conditional.  No existing PBBS
quantifier turns (5.1) and (5.2) into a common witness, and the common
literal antecedent remains open even after such an intersection.  The
unconditional \(B+2\) chain is therefore not shorter yet; the result
replaces the protected \(b\)-factor gate by a precise co-selection lemma
rather than proving it.
