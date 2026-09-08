# Minimal PBBS returns have an exact fixed-core wreath normal form

Date: 2026-07-25

Pure mathematics only.  No computation or external input is used.

## 0. Outcome

Let

\[
 A_{t+1}=[N]\setminus(A_t\cup\{\lambda_t\})
 \tag{0.1}
\]

be a one-step PBBS trajectory in \(KG(2r+1,r)\), where \(\lambda_t\)
is the coordinate omitted by the edge \(A_tA_{t+1}\).  Suppose

\[
 \lambda_{2s+1}=\lambda_0
 \tag{0.2}
\]

and that the half-open label word

\[
 \lambda_0,\lambda_1,\ldots,\lambda_{2s}
 \tag{0.3}
\]

has no repetition.  Then the two step-two owner parities have exactly the
same fixed-core cyclic-window form previously obtained for genuine
zero-winding returns.  No winding hypothesis and no Dyck return chronology
is needed.

Moreover every projected-edge-disjoint return packing contains a
projected-edge-disjoint simple-return packing of at least half its size.
The factor two is the only parity loss: an internal return trace is
contained either in the parent projected arc or in its global one-edge
translate.  Consequently the Catalan-order residence-packing gate is,
up to an absolute factor two, exactly a packing problem for fixed-core open
wreath sectors.

The result is structural, not yet the coefficient-one bound.  The local
central-marker word still has length \(2s+1\), while its selected step-two
parity has only \(s+1\) owners.  A global sharing or a second packing
factor remains necessary.

## 1. The recurrence alone forces two fixed cores

Write

\[
 a_j=\lambda_{2j}\quad(0\le j\le s),
 \qquad
 b_j=\lambda_{2j+1}\quad(0\le j<s).
 \tag{1.1}
\]

By (0.3), these \(2s+1\) labels are pairwise distinct.

### Theorem 1.1 (simple-return owner normal form)

There are disjoint sets \(K,K'\), each of size \(r-s\), such that

\[
 \boxed{
 A_{2j}=K\cup\{a_0,\ldots,a_{j-1}\}
            \cup\{b_j,\ldots,b_{s-1}\}}
 \qquad(0\le j\le s),
 \tag{1.2}
\]

and

\[
 \boxed{
 A_{2j+1}=K'\cup\{b_0,\ldots,b_{j-1}\}
              \cup\{a_{j+1},\ldots,a_s\}}
 \qquad(0\le j\le s).
 \tag{1.3}
\]

The state after the returned endpoint edge is

\[
 \boxed{A_{2s+2}=K\cup\{a_1,\ldots,a_s\}.}
 \tag{1.4}
\]

#### Proof

Equation (0.1) implies first that

\[
 \lambda_{t+1}\in A_t
 \tag{1.5}
\]

whenever \(\lambda_{t+1}\ne\lambda_t\), and then gives the exact
two-step update

\[
 \boxed{A_{t+2}=A_t-\{\lambda_{t+1}\}+\{\lambda_t\}.}
 \tag{1.6}
\]

Indeed, \(\lambda_{t+1}\notin A_{t+1}\), whereas the complement of
\(A_{t+1}\) is \(A_t\cup\{\lambda_t\}\).  Distinctness gives (1.5),
and complementing once more gives (1.6).

Iterating (1.6) on the even parity gives

\[
 A_{2j}
 =A_0-\{b_0,\ldots,b_{j-1}\}
      +\{a_0,\ldots,a_{j-1}\}.
 \tag{1.7}
\]

At the moment \(b_j\) is removed it belongs to \(A_{2j}\).  Since it is
distinct from all earlier inserted and removed labels, (1.7) forces
\(b_j\in A_0\).  At the moment \(a_j\) is omitted it does not belong to
\(A_{2j}\); the same distinctness argument forces \(a_j\notin A_0\).
Thus

\[
 K=A_0\setminus\{b_0,\ldots,b_{s-1}\}
 \tag{1.8}
\]

has size \(r-s\), and (1.2) follows.

Let

\[
 Z=\{a_0,\ldots,a_s,b_0,\ldots,b_{s-1}\},
 \qquad R=[N]\setminus Z.
 \tag{1.9}
\]

The active labels account for \(2s+1\) coordinates, so \(|R|=2(r-s)\).
Put \(K'=R\setminus K\).  Since

\[
 A_1=[N]\setminus(A_0\cup\{a_0\}),
 \tag{1.10}
\]

its inactive part is exactly \(K'\), it contains
\(a_1,\ldots,a_s\), and it contains none of the \(b_j\)'s.  Iterating
(1.6) on the odd parity now proves (1.3).  Finally (0.2) and (1.6) give

\[
 A_{2s+2}=A_{2s}-\{a_0\}+\{a_s\},
\]

which is (1.4).  The construction makes \(K,K'\) disjoint.  \(\square\)

## 2. Open wreath form and literal fusion

Order the active labels cyclically as

\[
 \Gamma_0=(b_0,\ldots,b_{s-1},a_0,\ldots,a_s).
 \tag{2.1}
\]

Equation (1.2) says that the even owners are a fixed core \(K\) together
with successive cyclic \(s\)-windows of \(\Gamma_0\).  Their complements
are a fixed core \(K'\) together with successive cyclic \((s+1)\)-windows.
After rotating (2.1), there are labels

\[
 \gamma_0,\ldots,\gamma_{2s}
\]

for which

\[
 X_j:=[N]\setminus A_{2j}
 =K'\cup\{\gamma_j,\ldots,\gamma_{j+s}\},
 \qquad 0\le j\le s.
 \tag{2.2}
\]

Therefore the central-marker word

\[
 \{\gamma_0\},\ldots,\{\gamma_{s-1}\},
 K'\cup\{\gamma_s\},
 \{\gamma_{s+1}\},\ldots,\{\gamma_{2s}\}
 \tag{2.3}
\]

has length \(2s+1\) and represents every consecutive intersection and
union of the owners in (2.2), through the full depth \(s\).  This is the
abstract central-marker identity from
`PBBS_ZERO_WINDING_FIXED_CORE_FUSION_20260725.md`; Theorem 1.1 shows that
its PBBS applicability requires only the simple-label condition (0.3),
not zero winding.

The same recurrence also gives the endpoint core-swap square.  Put

\[
 U=\{b_0,\ldots,b_{s-1}\},
 \qquad V=\{a_1,\ldots,a_s\}.
\]

Then

\[
 \begin{array}{ccl}
 A_0&=&K\cup U,\\
 A_1&=&K'\cup V,
 \end{array}
 \qquad
 \begin{array}{ccl}
 A_{2s+1}&=&K'\cup U,\\
 A_{2s+2}&=&K\cup V.
 \end{array}
 \tag{2.4}
\]

Both displayed Kneser edges omit \(a_0\).  Also, after ordering the two
cores arbitrarily, the open segment \(A_0,\ldots,A_{2s+1}\) extends to
an ambient \((N,r)\)-wreath exactly as in Theorem 4.2 of
`PBBS_ZERO_WINDING_OWNER_WREATH_STRUCTURE_20260725.md`.  There are
\(((r-s)!)^2\) displayed ordered completions.  The proof there uses only
the owner formulas and the simple omitted-label list, so it transfers
verbatim; zero winding was used in that note only to prove the label list
simple.

## 3. Projected packings reduce to simple returns with loss at most two

Call a consecutive return interval **simple** if its half-open omitted-label
word has no repetition.

### Theorem 3.1 (minimal-return reduction)

Let \(\mathcal P\) be any family of pairwise projected-edge-disjoint PBBS
return intervals, all of gap at most \(G\).  There is a family
\(\mathcal P^{\min}\) of simple returns such that

1. every member of \(\mathcal P^{\min}\) is chronologically contained in
   a distinct member of \(\mathcal P\);
2. every member still has gap at most \(G\);
3. the members are pairwise projected-edge-disjoint;
4. every member has the normal form (1.2)--(1.3); and
5. \(|\mathcal P^{\min}|\ge|\mathcal P|/2\).

#### Proof

Take one return interval \(I=[p,q]\), so
\(\lambda_p=\lambda_q\).  If its half-open label word is not simple,
choose a label with two occurrences in \([p,q)\), and choose two
consecutive occurrences of that label.  They delimit a proper return
subinterval \(I'\subsetneq I\).  Repeat.  Strict containment makes the
procedure terminate, and its terminal interval has no repeated label in
its half-open word.

Perform this independently inside every member of \(\mathcal P\), for the
moment retaining all terminal simple intervals.  Strict shrinking cannot
increase the gap, and the number of intervals is unchanged.

It remains to audit projected-edge disjointness.  Lift one parent
chronological interval to integer positions.  Write its occurrences as

\[
 i,\ i+2s+1
\]

and its projected trace as

\[
 I=\{i-1,i+1,\ldots,i+2s+1\}.
 \tag{3.1}
\]

Suppose the terminal simple subreturn starts at \(i+a\), has gap
\(2s'+1\), and hence ends at \(i+a+2s'+1\).  Chronological containment
gives

\[
 0\le a,
 \qquad a+2s'+1\le2s+1.
 \tag{3.2}
\]

If \(a=2u\), its projected trace is

\[
 J=\{i-1+2(u+h):0\le h\le s'+1\}\subseteq I.
 \tag{3.3}
\]

If \(a=2u+1\), its projected trace is

\[
 J=\{i+2(u+h):0\le h\le s'+1\}
   \subseteq I+1,
 \tag{3.4}
\]

where

\[
 I+1=\{e+1:e\in I\}.
\]

The inclusions follow immediately from (3.2).  They remain valid modulo
the component length, including when the component is opened across the
chosen lift.  Translation by one is a bijection of the full transition
edge set; if the step-two dynamics splits into two parity cycles, it simply
interchanges those cycles.

Partition the terminal simple subreturns according as \(a\) is even or
odd.  In the even class, (3.3) puts every trace inside its pairwise disjoint
parent.  In the odd class, (3.4) puts every trace inside the corresponding
translated parent, and the translated parents are again pairwise disjoint.
Thus both classes separately are projected-edge-disjoint.  Keep the larger
class.  It has at least half the original cardinality.  Finally every
simple gap is odd and Theorem 1.1 applies.  \(\square\)

### Corollary 3.2 (simple-return packing equivalence)

Let \(\nu_H^{\rm simp}(P_r)\) be the maximum projected-edge-disjoint
packing restricted to simple returns, and define the analogous long-cycle
quotient quantity \(\overline\nu_H^{\rm simp}\).  Then

\[
 \boxed{
 \nu_H^{\rm simp}(P_r)\le\nu_H(P_r)
 \le2\nu_H^{\rm simp}(P_r),}
 \tag{3.5}
\]

and

\[
 \boxed{
 \overline\nu_H^{\rm simp}\le\overline\nu_H
 \le2\overline\nu_H^{\rm simp}.}
 \tag{3.6}
\]

Therefore the Catalan-order gate \((CP_A)\) is equivalent, up to an
absolute factor two, to its restriction to simple fixed-core sectors.

## 4. Exact boundary

This reduction removes two distractions.

* Winding is not a separate local geometry after the factor-two
  minimalization: every retained return has the same two-core window normal
  form.
* Complicated internal return nesting can be discarded from the numerical
  projected packing gate at absolute loss at most two.

What remains is genuinely global.  The word (2.3) costs \(2s+1\) letters
for \(s+1\) owners on one selected step-two parity.  Applying it separately
to all packed sectors can therefore lose a constant factor.  To prove
coefficient one one still needs either

1. a deck-level fusion which shares the active-coordinate part of (2.3),
   or
2. the Catalan-order bound
   \(\overline\nu_{\lceil A\sqrt r\rceil}=O_A(\operatorname{Cat}_r/N)\).

The exact advance is that the entire remaining packing gate may be
restricted to fixed-core cyclic-window sectors, with no winding or
chronology exception, at absolute loss at most two.  The unresolved bridge
is now a packing/counting theorem for those open wreath sectors, or a
deck-level fusion that shares their active-coordinate words.
