# Domino twins: first ACLE bounds and the \(K_{2,5}\) overlap gate

Date: 2026-07-27

**Subsequent resolution.** The factorial-overlap estimate (0.2) is proved
in
MATH_THEOREM_DOMINO_TWIN_FACTORIAL_OVERLAP_BOUND_20260727.md.
Accordingly \(K_{2,5}\), and in fact every static \(K_{2,\ell}\) through
\(\ell=O(\log m)\), is now closed. The remaining qualifier in this audit
is the dynamic stopped regeneration of that estimate.

## 0. Verdict

Let \(\mathcal Q_R\) be the domino-twin superpacket catalogue of
MATH_THEOREM_DOMINO_TWIN_SUPERPACKET_DEGREES_AND_CRITICAL_FACTOR_GATE_20260727.md.
Write

\[
 K=2n=4m,\qquad D=D^\square,\qquad
 \delta=\Delta_2^\square/D=\frac5{R(n-R)}.
\]

The exact pair profile gives

\[
 K\delta=O(m^{-1}),\qquad
 K^2\delta=O(1).                                          \tag{0.1}
\]

This note proves:

1. every one-vertex protected link has relative one-column influence
   \(O(m^{-1})\);
2. all tree/breadth column moments follow from the bipartite
   tree-homomorphism bound;
3. the first \(C_4\) drift-coherence diagram is \(O(D^4)\), exactly the
   required scale;
4. the higher common-column diagrams \(K_{2,3}\) and \(K_{2,4}\) also
   pass using the exact triangle/quartet scales;
5. the first diagram not closed by the currently proved *ball* bound is
   \(K_{2,5}\). The missing statement is an edge-conditioned overlap
   factorial-moment estimate, not another maximum pair-codegree estimate.

The precise sufficient theorem is

\[
 \boxed{
 \sup_{\substack{X\\F\ni X}}
 \frac1D\sum_{\substack{F'\ni X\\F'\ne F}}
 (|F\cap F'|-1)_p
 \le (Cp)^{Cp}m^{-2}
 \quad(1\le p\le C_0\log m).}                            \tag{0.2}
\]

Under (0.2), every \(K_{2,\ell}\) column moment through logarithmic order
has the required scale and the first top-strip escape disappears.

The current radius-ball theorem proves too little for \(p\ge5\): after
summing the \(\binom Kp\) possible protected rows it loses a polynomial
factor. This is a proof gap, not a demonstrated obstruction. The canonical
six-row local patch actually has degree \(\Theta(m^{-6})D\), exactly the
scale predicted by (0.2). Thus the next task is a common-interval
factorial-moment theorem for two twin superpackets through one entrance
target.

## 1. One-vertex link influence

Fix an entrance target \(X\). Let

\[
 \mathcal F_X=\{F\in\mathcal Q_R:X\in F\},\qquad |\mathcal F_X|=D,
\]

and let \(\mathcal R_X\) be the catalogue columns avoiding \(X\). For
\(e\in\mathcal R_X\), put

\[
 a_X(e)=|\{F\in\mathcal F_X:F\cap e\ne\varnothing\}|.
\]

### Lemma 1.1 (first influence)

\[
 a_X(e)\le K\Delta_2^\square,\qquad
 \alpha:=\frac{\max_ea_X(e)}D\le K\delta=O(m^{-1}).        \tag{1.1}
\]

#### Proof

For every \(F\in\mathcal F_X\) meeting \(e\), choose one
\(Y\in F\cap e\). Since \(X\notin e\),
\[
 a_X(e)\le\sum_{Y\in e}d^\square(X,Y)\le K\Delta_2^\square.
\]
\(\square\)

Put \(L=KD\). The conflict-incidence graph between \(\mathcal F_X\) and
\(\mathcal R_X\) has left degree at most \(L\) and right degree at most
\(A=D\alpha\). Therefore the tree-homomorphism theorem gives, for all
\(h,\ell\ge1\),

\[
 \sum_g\left(\sum_ea_X(e)^{h-1}b_X(e,g)\right)^\ell
 \le DL^{\ell+1}A^{h\ell-1}.                              \tag{1.2}
\]

Thus every first-column breadth moment is controlled with normalized
factor \(\alpha^{\ell-1}\). This includes arbitrarily high moments of one
tree-shaped common event column; no top-strip problem occurs at tree
level.

## 2. Edge-conditioned overlap

For \(F,F'\in\mathcal F_X\), put
\[
 r_X(F,F')=|F\cap F'|-1.
\]

The target \(X\) is removed because it is shared by every pair in
\(\mathcal F_X\).

### Lemma 2.1 (first overlap moment)

Uniformly in \(X\) and \(F\ni X\),
\[
 \frac1D\sum_{F'\ni X}r_X(F,F')
 =\frac{25}{R(n-R)}+O_a(m^{-4})
 =O(m^{-2}).                                               \tag{2.1}
\]

#### Proof

Inside every twin superpacket, a fixed vertex has:

* five other vertices at intersection \(R-1\);
* four at every intersection \(2,\ldots,R-2\);
* five at intersection \(1\);
* \(2(n-2R)+1\) disjoint vertices.

Conditioned on \(X\in F'\), the probability that \(F'\) also contains a
fixed \(Y\) is \(d^\square(X,Y)/D\). Sum this probability over
\(Y\in F\setminus\{X\}\). The \(R-1\) term is
\[
 5\cdot\frac5{R(n-R)}.
\]
The \(R-2\) term is \(O(m^{-4})\), and all remaining terms are smaller.
\(\square\)

This is stronger than the maximum-influence scale \(K\delta=O(m^{-1})\):
two random link rows through the same protected target have only
\(O(m^{-2})\) expected additional overlap.

## 3. The first \(C_4\) closes

For \(F,F'\in\mathcal F_X\), let
\[
 c_X(F,F')
 =|\{e\in\mathcal R_X:e\cap F\ne\varnothing,\
                         e\cap F'\ne\varnothing\}|.
\]

### Lemma 3.1 (common-conflict bound)

\[
 c_X(F,F')
 \le D\,r_X(F,F')+K^2\Delta_2^\square
 \le D\bigl(r_X(F,F')+O(1)\bigr).                         \tag{3.1}
\]

#### Proof

An \(e\in\mathcal R_X\) meeting both \(F,F'\) either contains a common
vertex \(Y\ne X\), or contains distinct vertices
\(Y\in F\), \(Z\in F'\). The first type is bounded by \(Dr_X(F,F')\);
the second by \(K^2\Delta_2^\square\). Use (0.1). \(\square\)

### Theorem 3.2 (time-zero \(C_4\) energy)

\[
 \sum_{e,g\in\mathcal R_X}b_X(e,g)^2=O(D^4).             \tag{3.2}
\]

Equivalently, this is
\[
 O(L^2D^2\alpha^2),
\]
the required first drift-coherence scale.

#### Proof

Swap the order of counting:
\[
 \sum_{e,g}b_X(e,g)^2
 =\sum_{F,F'\in\mathcal F_X}c_X(F,F')^2.
\]
By (3.1),
\[
 c_X(F,F')^2\le C D^2(1+r_X(F,F')^2).
\]
Since \(r^2\le Kr\), Lemma 2.1 gives, for each fixed \(F\),
\[
 \sum_{F'\ni X}r_X(F,F')^2
 \le K\sum_{F'\ni X}r_X(F,F')
 =O(D/m).
\]
Summing over \(F\) proves (3.2). Finally,
\[
 L^2D^2\alpha^2=(KD)^2D^2\,O(m^{-2})=O(D^4).
\]
\(\square\)

Thus the domino pairing does not break the first \(C_4\). Its linear
deeper overlap is invisible at the entrance \(C_4\) scale.

## 4. Exact triangle and quartet scales

The Johnson-distance-one graph induced by one twin superpacket contains
two kinds of triangles: star triangles with a common \((R-1)\)-core and
top triangles inside one \((R+1)\)-set. Each superpacket contains \(2n\)
of each kind. It contains \(n/2\) star \(K_4\)'s and \(n/2\) top
\(K_4\)'s.

Double counting over the \(n!\) labelled columns gives:

\[
 \frac{\Delta_{3,\mathrm{star}}}{D}
 =\frac6{R(n-R)(n-R-1)},                                  \tag{4.1}
\]

\[
 \frac{\Delta_{3,\mathrm{top}}}{D}
 =\frac6{(n-R)R(R-1)},                                    \tag{4.2}
\]

and

\[
 \max\left\{
 \frac{\Delta_{4,\mathrm{star}}}{D},
 \frac{\Delta_{4,\mathrm{top}}}{D}
 \right\}
 =O(m^{-4}).                                               \tag{4.3}
\]

More explicitly,

\[
 \frac{\Delta_{4,\mathrm{star}}}{D}
 =\frac6{R(n-R)(n-R-1)(n-R-2)},                            \tag{4.4}
\]

\[
 \frac{\Delta_{4,\mathrm{top}}}{D}
 =\frac6{(n-R)R(R-1)(R-2)}.                               \tag{4.5}
\]

These formulas also follow directly from the active atom partitions.
They imply, for fixed \(F\ni X\),

\[
 \sum_{F'\ni X}(r_X(F,F'))_p=O(D)
 \qquad(p=2,3,4).                                         \tag{4.6}
\]

Indeed,
\[
 \sum_{F'\ni X}(r)_p
 =p!\sum_{\substack{C\subseteq F\setminus\{X\}\\|C|=p}}
 d^\square(\{X\}\cup C),
\]
and (4.1)--(4.5), together with the distance-two pair bound for
nonclique clusters, pay the \(\binom Kp\) choices.

Consequently the common-column diagrams \(K_{2,\ell}\) have the required
scale through \(\ell=4\).

## 5. The first unclosed diagram

For every \(\ell\ge2\), the \(\ell\)-th common-column moment contains the
complete bipartite incidence core \(K_{2,\ell}\): two link rows \(F,F'\)
and \(\ell\) selected-event columns, every column meeting both rows. After
reversing the count, its size is
\[
 \sum_{F,F'\in\mathcal F_X}c_X(F,F')^\ell.                \tag{5.1}
\]

Equations (3.1) and the factorial expansion of \(r^\ell\) reduce (5.1)
to the moments
\[
 \sum_{F,F'\in\mathcal F_X}(r_X(F,F'))_p,
 \qquad 1\le p\le\ell.                                    \tag{5.2}
\]

The exact small-cluster counts close (5.2) for \(p\le4\). For \(p=5\),
the current radius-ball theorem only says that six vertices in one
superpacket contain a pair at Johnson distance at least two. Hence
\[
 \Delta_6^\square/D=O(m^{-4}).                            \tag{5.3}
\]
After summing the \(\binom K5=\Theta(m^5)\) possible five-row subsets,
(5.3) loses a factor \(m\). Thus \(K_{2,5}\) is the first common-column
diagram not closed by the currently proved higher-codegree bound.

This is not evidence that \(K_{2,5}\) is genuinely large. For the densest
canonical local six-row patch
\[
 P_0,P_1,P_2,P^\tau_0,P^\tau_1,P^\tau_2,
\]
the Boolean atom sizes are
\[
 R-3,\quad n-R-3,\quad 1,1,1,1,1,1.
\]
It has only \(O(n)\) positional embeddings per superpacket orbit, so its
degree is
\[
 O\!\left(\frac{D}{(R)_3(n-R)_3}\right)=O(Dm^{-6}),       \tag{5.4}
\]
which is exactly strong enough. The loss in (5.3) is caused by forgetting
the full common-interval atom partition and retaining only one distant
pair.

## 6. The exact replacement lemma

### Lemma 6.1 (conditional all-order closure)

Assume (0.2). Then for every \(2\le\ell\le C_0\log m\),
\[
 \sum_{F,F'\in\mathcal F_X}c_X(F,F')^\ell
 \le (C\ell)^{C\ell}D^{\ell+2}.                           \tag{6.1}
\]

#### Proof

By (3.1),
\[
 c_X(F,F')^\ell
 \le(CD)^\ell\bigl(1+r_X(F,F')^\ell\bigr).
\]
Expand \(r^\ell\) in falling factorials:
\[
 r^\ell=\sum_{p=1}^{\ell}S(\ell,p)(r)_p.
\]
Sum over \(F'\), apply (0.2), and use
\[
 \sum_p S(\ell,p)(Cp)^{Cp}\le(C\ell)^{C\ell}.
\]
Then sum over the \(D\) choices of \(F\). \(\square\)

Equation (6.1) supplies every \(K_{2,\ell}\) core needed by the
large-jump column hierarchy. Combined with the tree/breadth theorem and
the excess-core compression lemma, it removes the first explicit
top-strip escape.

What it does not by itself prove is dynamic regeneration of (0.2) after
many bites. A complete near-factor proof still needs either:

1. a stopped version of (0.2) stable under the selected-edge trajectory;
   or
2. a one-shot edge-colouring/absorption theorem bypassing residual
   regeneration.

## 7. Exact status

The twin catalogue passes:

* the one-vertex influence gate;
* every tree/breadth column moment;
* the first \(C_4\);
* \(K_{2,3}\) and \(K_{2,4}\);
* the scalar and fractional near-factor ledgers.

The first mixed diagram not closed by the *ball bound alone* is

\[
 \boxed{K_{2,5}.}
\]

Its missing input here is the factorial common-interval overlap estimate
(0.2). That estimate is proved in the subsequent theorem cited at the top
of this file. The dynamic stopped version remains necessary.
