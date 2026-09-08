# Hamilton-first extraction supplies an abstract clean-packet host bank

**Date:** 2026-08-07  
**Status:** unconditional abstract owner/immediate-palette theorem.  If the
small promotion-flag bank may be chosen after a middle-levels Hamilton cycle,
then all of its complete clean lag-two four-edge paths can be chosen already
inside that one Hamilton cycle.  This removes the protected-two-factor
extension gate for the co-chosen flag bank.  It does not prove that the
resulting flags are compatible with one exact residual lower matching, nor
does it give a common literal width-\(d+2\) source antecedent.

## 1. Hamilton-cycle notation

Put

\[
 n=2m+1,\qquad
 X={ [n]\choose m},\qquad
 Y={ [n]\choose {m+1}},\qquad
 W=|X|=|Y|.
\]

Fix a Hamilton cycle in the middle-levels incidence graph and write it as

\[
 T_0,J_0,T_1,J_1,\ldots,T_{W-1},J_{W-1},T_0,
 \tag{1.1}
\]

where

\[
 J_i=T_i\cup T_{i+1},\qquad
 I_i=T_i\cap T_{i+1}
 \tag{1.2}
\]

and indices are cyclic.  Thus every \(T_i\) is a distinct rank-\(m\)
owner and every \(J_i\) is a distinct rank-\((m+1)\) upper colour.

Call \(i\) a **good turn** when

\[
 I_{i-1}\ne I_i.
 \tag{1.3}
\]

## 2. Every good turn is a clean lag-two set-valued packet

### Lemma 2.1

At every good turn \(i\), there are a rank-\((m-2)\) set \(R_i\) and
four pairwise distinct labels \(x_i,u_i,y_i,v_i\notin R_i\) such that

\[
\begin{aligned}
 T_{i-1}&=R_i+u_i+x_i,\\
 T_i&=R_i+u_i+y_i,\\
 T_{i+1}&=R_i+y_i+v_i,
\end{aligned}
 \tag{2.1}
\]

and

\[
 I_{i-1}=R_i+u_i,\qquad I_i=R_i+y_i,
 \tag{2.2}
\]

\[
 J_{i-1}=R_i+u_i+x_i+y_i,\qquad
 J_i=R_i+u_i+y_i+v_i.
 \tag{2.3}
\]

#### Proof

Let \(x_i\) be the unique element of \(T_{i-1}\setminus T_i\), and let
\(y_i\) be the unique element of \(T_i\setminus T_{i-1}\).  Similarly,
let \(u_i\) be the unique element of \(T_i\setminus T_{i+1}\), and
\(v_i\) the unique element of \(T_{i+1}\setminus T_i\).

Condition (1.3) is exactly \(u_i\ne y_i\).  Put

\[
 R_i=T_i\setminus\{u_i,y_i\}.
\]

This gives (2.1)--(2.3).  The labels \(x_i,y_i\) and \(u_i,v_i\) are
distinct by their two exchanges; \(x_i,u_i\) and \(x_i,y_i\) are
distinct because \(x_i\notin T_i\), while \(u_i,y_i\in T_i\); the
analogous statements hold for \(v_i\).  Finally \(x_i\ne v_i\), since
otherwise (2.3) would give \(J_{i-1}=J_i\), contradicting the simplicity
of the Hamilton cycle on the \(Y\)-shore. \(\square\)

For every \(d\)-set \(C_i\subset R_i\), put

\[
 M_i=R_i\setminus C_i,\qquad U_i=M_i+u_i.
 \tag{2.4}
\]

Then \(|M_i|=m-d-2\), and (2.1)--(2.3) are precisely the complete
set-valued resources of the clean lag-two packet for the flag
\((M_i,U_i)\).

## 3. Good turns are abundant

### Lemma 3.1 (one lower colour has bounded load)

For every fixed \(I\in{[n]\choose {m-1}}\),

\[
 \#\{i:I_i=I\}\le m+1.
 \tag{3.1}
\]

#### Proof

All owners containing \(I\) form a clique of size \(m+2\) in the
Johnson graph on \(X\).  The edges of the Hamilton owner cycle coloured
by \(I\) form a maximum-degree-two subgraph on those \(m+2\) vertices.
It cannot contain a cycle component: such a component would already use
both Hamilton-cycle edges at each of its vertices and would therefore be
the whole Hamilton cycle, whereas \(W>m+2\).  It is consequently a
linear forest and has at most \(m+1\) edges. \(\square\)

### Corollary 3.2

The number \(g\) of good turns satisfies

\[
 g\ge \left\lceil {W\over m+1}\right\rceil.
 \tag{3.2}
\]

#### Proof

Read \(I_0,I_1,\ldots,I_{W-1}\) as a cyclic colour word.  Its constant
runs have length at most \(m+1\) by Lemma 3.1, and a good turn is exactly
a boundary between two runs. \(\square\)

## 4. A sparse bank with disjoint immediate resources

### Theorem 4.1 (well-spaced good-turn bank)

Let \(h\) satisfy

\[
 h\,[4(m+1)+5]< {W\over m+1}.
 \tag{4.1}
\]

There are \(h\) good turns \(i_1,\ldots,i_h\) such that

1. their three-owner paths are pairwise vertex-disjoint; and
2. all \(2h\) lower colours
   \(I_{i_j-1},I_{i_j}\) are distinct.

In particular, this holds for every

\[
 h\le {d+1\choose2}
 \tag{4.2}
\]

for all sufficiently large optimal parameters.

#### Proof

Choose good turns greedily.  One chosen turn forbids at most five turns
by cyclic distance at most two.  A fixed lower colour occurs on at most
\(m+1\) owner edges, and each such edge is adjacent to at most two turn
positions.  Thus either of the two chosen colours forbids at most
\(2(m+1)\) further good turns.  One choice therefore removes at most
\(4(m+1)+5\) candidates.  Corollary 3.2 and (4.1) complete the greedy
argument.

For (4.2), the left side of (4.1) is polynomial in \(m\), whereas
\(W/(m+1)\) is exponential. \(\square\)

The corresponding four-incidence-edge paths

\[
 T_{i_j-1}\subset J_{i_j-1}\supset T_{i_j}
 \subset J_{i_j}\supset T_{i_j+1}
 \tag{4.3}
\]

are already contained in one spanning Hamilton cycle.  No protected
\(f\)-factor extension is needed for this co-chosen bank.

## 5. The flag bottoms and tops can also be made distinct

### Theorem 5.1 (target-disjoint flag extraction)

Assume

\[
 {m-2\choose d}>2(h-1).
 \tag{5.1}
\]

For the good turns from Theorem 4.1, the sets \(C_i\subset R_i\) can be
chosen so that all flag bottoms \(M_i=R_i\setminus C_i\) are distinct
and all flag tops \(U_i=M_i+u_i\) are distinct.

Condition (5.1) holds for \(h\le\binom{d+1}{2}\) for all sufficiently
large optimal parameters.

#### Proof

At the next turn, one previous bottom \(M_j\) forbids at most one
\(d\)-set \(C_i=R_i\setminus M_j\).  One previous top \(U_j\) likewise
forbids at most one choice, since equality \(M_i+u_i=U_j\) determines
\(M_i=U_j-u_i\), if it is possible at all.  Fewer than \(2(h-1)\)
choices are forbidden, so (5.1) permits greedy selection.  The asymptotic
claim is immediate from \(d=\Theta(\sqrt m)\). \(\square\)

### Corollary 5.2 (rank-profiled boundary labels)

Let \(s_1,\ldots,s_h\) be prescribed ranks with
\(1\le s_j\le |M_j|\).  For all sufficiently large parameters, one may
choose distinct targets

\[
 S_j\in {M_j\choose {s_j}}.
 \tag{5.2}
\]

#### Proof

Targets of different ranks are automatically distinct.  At one fixed
rank \(1\le s<|M_j|\), every \(M_j\) offers at least \(|M_j|\) targets,
and \(|M_j|=m-d-2>h\) eventually.  At the endpoint rank
\(s=|M_j|\), take \(S_j=M_j\), which is distinct by Theorem 5.1.
Greedy choice proves the claim. \(\square\)

## 6. Exact consequence and exact remaining gate

Theorems 4.1 and 5.1 prove the following quantifier-reversed statement:

\[
\boxed{
\begin{minipage}{0.83\linewidth}
After fixing any middle-levels Hamilton cycle, one can extract an
\(O(d^2)\)-sized target-disjoint flag bank whose complete clean lag-two
owner/lower/upper paths are already contained in that cycle.
\end{minipage}}
\tag{6.1}
\]

Thus the first protected-factor gate in the fixed-flag proof disappears
if the Ferrers boundary flags may be selected in this order.

Two correlations are not supplied here.

1. **Residual lower matching.**  The exact Ferrers containment-flow
   theorem chooses its deleted boundary targets jointly with the
   capacity-\(d\) owner matching.  Corollary 5.2 only places targets
   inside the extracted flag bottoms.  It does not prove that deleting
   those particular targets leaves a capacity-\(d\) containment matching
   or a nested literal compiler.
2. **Common literal history.**  The Hamilton cycle gives the set-valued
   owner and immediate-upper chronology.  The separate fixed-core collars
   do not automatically splice into one width-\(d+2\) source word, and no
   deeper-upper/common-cap theorem is asserted.

The sharpened next theorem is therefore a **Hamilton-first Ferrers
intersection theorem**: choose the good turns, their flag bottoms, and the
rank-profiled boundary targets inside the same feasible face of the exact
Ferrers owner flow.  Once that is done, the protected-two-factor cut is no
longer part of the proof.

