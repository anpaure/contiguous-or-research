# The equitable configuration host lies outside the Delcourt--Postle and Joos--Mubayi--Smith black boxes

**Date:** 2026-08-03  
**Status:** unconditional theorem-hypothesis audit for the canonical labelled
configuration hypergraph. This is a sharp **direct-application no-go**, not
an impossibility theorem for an integral matching, a tailored
sparsification, or a Boolean absorber. No computation is used.

Primary sources:

* M. Delcourt and L. Postle, *Finding an almost perfect matching in a
  hypergraph avoiding forbidden submatchings*,
  [arXiv:2204.08981v3](https://arxiv.org/abs/2204.08981v3), especially
  Corollary 1.17.
* F. Joos, D. Mubayi and Z. Smith, *Conflict-free Hypergraph Matchings and
  Coverings*, [arXiv:2407.18144v2](https://arxiv.org/abs/2407.18144v2),
  especially (S1)--(S4), (H1)--(H2), and Theorem 1.1/Theorem 3.1.

## 0. Verdict

Put

\[
 k=2r,\qquad W=\binom{2r}{r},\qquad D_*=Wr!.
\tag{0.1}
\]

Let \(\mathcal K_r\) be the labelled configuration multihypergraph from
MATH_THEOREM_EQUITABLE_PATTERN_CONFIGURATION_FRACTIONAL_MATCHING_20260803.md
for an optimal equitable rank-pattern schedule. Its edges are

\[
 e(i,T,\pi)=\{p_i,o_T\}\cup
 \{\operatorname{pref}_s(\pi):s\in R_i\}.
\tag{0.2}
\]

Then

\[
 |E(\mathcal K_r)|=WD_*,\qquad
 \Delta(\mathcal K_r)=D_*,\qquad
 \Delta_2(\mathcal K_r)\ge (1-o(1)){D_*\over r+1}.
\tag{0.3}
\]

The last inequality already comes from an owner together with one of its
rank-\((r-1)\) facets. Thus the macroscopic collar has normalized
codegree \(\Theta(1/r)\). Also

\[
 \log D_*=r\log r+O(r),\qquad
 \log W=\Theta(r),\qquad
 K_r:=\max_{e\in\mathcal K_r}|e|=\Theta(\sqrt r).
\tag{0.4}
\]

These parameters give two definitive conclusions.

1. **JMS:** for all sufficiently large \(r\), there are no choices of the
   JMS degree parameter \(d_J\) and exponent \(\varepsilon>0\) satisfying
   even (S2), (H1), and (H2) for this natural first-stage host. This is an
   actual numerical contradiction, independent of the later conflict and
   completion rows.
2. **DP:** Corollary 1.17 has no direct all-\(r\) application yielding a
   matching of size \((1-o(1))W\). At the only useful degree scale
   \(D=(1+o(1))D_*\), its power-codegree hypothesis forces
   \(\beta=O(1/r)\), while the corollary fixes \(\beta>0\) and the edge
   bound before sending \(D\) to infinity. The edge bound here is itself
   \(K_r=\Theta(\sqrt r)\).

Even on the nonadjacent retained residual band, where

\[
 \Delta_2/D_*=O(r^{-2}),\qquad K_r^2\Delta_2/D_*=O(r^{-1}),
\tag{0.5}
\]

the natural labelled degree scale turns a polynomial saving into only
\(D_*^{-o(1)}\), not \(D_*^{-\beta}\) for fixed \(\beta>0\).
The subcritical geometric ledger is real; it simply is not the hypothesis
of the published fixed-parameter theorem.

Neither conclusion rules out a purpose-built sparsification followed by a
new growing-uniformity estimate, nor a collar-first factorization which
removes the critical pairs. Those are additional theorems, not black-box
consequences of the two cited papers.

## 1. Exact unweighted ledger of the canonical host

Every labelled configuration has weight \(1/D_*\) in the canonical
fractional matching. Multiplying the proved weighted ledger by \(D_*\)
gives the ordinary labelled degrees. For every pattern and owner,

\[
 d(p_i)=D_*,\qquad d(o_T)=D_*.
\tag{1.1}
\]

For a named rank-\(s\) target \(S\),

\[
 d(S)=D_*{N_s\over\binom{2r}{s}}\le D_*.
\tag{1.2}
\]

Consequently \(\Delta(\mathcal K_r)=D_*\). Summing degrees on the pattern
shore gives

\[
 |E(\mathcal K_r)|=WD_*.
\tag{1.3}
\]

For \(S\subset T\), \(|S|=s\), the exact owner--target codegree is

\[
 d(o_T,S)=D_*{N_s\over W\binom rs}.
\tag{1.4}
\]

At \(s=r-1\),

\[
 \binom{2r}{r-1}=W{r\over r+1}.
\tag{1.5}
\]

The entire triangular Ferrers boundary has \(O(d^2)=O(r)\) cells, so
\(b_{r-1}=O(r)\). Hence

\[
 N_{r-1}=W{r\over r+1}-O(r),
\tag{1.6}
\]

and (1.4) becomes

\[
 d(o_T,S)
 ={D_*\over r+1}-O\left({D_*\over W}\right)
 =(1-o(1)){D_*\over r+1}.
\tag{1.7}
\]

This proves (0.3). There is a second exact witness. Since
\(N_1=2r-b_1>0\) for large \(r\), some pattern contains rank one, and for
every singleton \(x\),

\[
 d(p_i,x)={D_*\over 2r}.
\tag{1.8}
\]

Stirling's formula gives

\[
 \log D_*=\log\binom{2r}{r}+\log(r!)
 =r\log r+(2\log2-1)r+O(\log r).
\tag{1.9}
\]

The optimal depth satisfies \(d=\Theta(\sqrt r)\). Since the total
scheduled rank mass is \(\Theta(dW)\), and the pattern decomposition is
equitable, every configuration has \(\Theta(d)\) target vertices (up to
the harmless one-unit equitable discrepancy). Therefore
\(K_r=\Theta(\sqrt r)\).

### Degree irregularity is not the blocker

Equation (1.2) shows that target degrees can be lower than \(D_*\), but
never higher. This is compatible with the DP coloring corollary, which
uses a maximum-degree bound and the total edge count. It is also compatible
with JMS if the pattern shore is \(P\): all pattern degrees are exactly
\(D_*\), while vertices on the \(Q\)-shore may have lower degree. The
fatal rows are pair concentration and, for JMS, ambient size.

## 2. Joos--Mubayi--Smith: an exact three-row contradiction

Take the pattern vertices as the JMS shore \(P\), and put owners and named
targets on \(Q\). Pattern sizes differ by at most one. If exact uniformity
is desired, pad shorter configurations by edge-private \(Q\)-vertices.
This cannot decrease any old degree or codegree. Likewise, an edge-private
label vertex can make the labelled edges simple without changing the old
pair ledger.

Let \(d_J,\varepsilon\) satisfy the JMS rows. Condition (H1) says

\[
 (1-d_J^{-\varepsilon})d_J\le D_*\le d_J.
\tag{2.1}
\]

Condition (H2), together with (1.7), says for all large \(r\)

\[
 {D_*\over 2r}\le d_J^{1-\varepsilon}.
\tag{2.2}
\]

Condition (S2), because \(|P|=W\), says

\[
 W\le \exp(d_J^{\varepsilon^3}),
 \quad\hbox{or}\quad
 \log\log W\le\varepsilon^3\log d_J.
\tag{2.3}
\]

These are incompatible without hidden constants. Equation (2.3) implies
\(d_J^{-\varepsilon}<1/2\) for large \(r\). Hence (2.1) gives

\[
 D_*\le d_J\le 2D_*,
\qquad \log d_J=\Theta(r\log r).
\tag{2.4}
\]

Using (2.4) in (2.2),

\[
 {1\over2r}\le {d_J\over D_*}d_J^{-\varepsilon}
 \le2d_J^{-\varepsilon},
\]

so

\[
 \varepsilon\log d_J\le\log(4r).
\tag{2.5}
\]

It follows that

\[
 \varepsilon^3\log d_J
 \le {\log^3(4r)\over(\log d_J)^2}
 =O\left({\log r\over r^2}\right)=o(1).
\tag{2.6}
\]

But \(\log\log W=\log r+O(1)\), contradicting (2.3).

### Theorem 2.1 (JMS direct-host no-go)

For all sufficiently large \(r\), the canonical labelled configuration
host satisfies no simultaneous choice of \((d_J,\varepsilon)\) obeying
JMS (S2), (H1), and (H2). Therefore neither the ordinary first-stage
encoding nor a private-completion encoding based on the same first-stage
host is an application of Theorem 1.1/3.1.

The source also fixes the uniformities \(p,q,r\) and conflict bound
\(\ell\) before sending \(d_J\) to infinity, whereas the natural
first-stage edge size here is \(\Theta(\sqrt r)\). That is a second
quantifier mismatch, but it is not needed for Theorem 2.1.

A private completion cannot repair the contradiction: it changes neither
the old owner--target pair in (1.7), the first-stage maximum degree, nor the
exponential pattern shore. It would additionally require a literal decoder
and bounded conflicts for all owner/target collisions of decoded completion
edges.

## 3. Delcourt--Postle: the fixed-power and growing-uniformity boundary

Corollary 1.17 fixes integers \(R,g\ge2\) and a real \(\beta>0\), then
provides a threshold and \(\alpha=\alpha(R,g,\beta)>0\). With empty
configuration conflicts, its relevant host hypotheses are

\[
 \Delta(G)\le D,\qquad \Delta_2(G)\le D^{1-\beta},
\tag{3.1}
\]

and its guaranteed matching size is

\[
 {e(G)\over D}(1-D^{-\alpha}).
\tag{3.2}
\]

Apply this formally to \(G=\mathcal K_r\). Since
\(e(G)=WD_*\) and \(D\ge D_*\), a bound of order
\((1-o(1))W\) from (3.2) requires

\[
 D=(1+o(1))D_*.
\tag{3.3}
\]

At that scale, (1.7) and (3.1) imply

\[
 D^\beta=O(r),\qquad
 \beta\le {\log O(r)\over\log D}=O(1/r).
\tag{3.4}
\]

No fixed positive \(\beta\) satisfies (3.4) along the family.
Independently, the corollary fixes the edge bound \(R\), while
\(R=K_r=\Theta(\sqrt r)\) here. Its threshold and output exponent are not
uniform in this diagonal regime.

Inflating the nominal degree parameter does not give a useful workaround.
For fixed \(\beta>0\), (1.7) and (3.1) force

\[
 D\ge\left({D_*\over2r}\right)^{1/(1-\beta)}.
\tag{3.5}
\]

At this value the numerical lower bound in (3.2), divided by \(W\), is at
most

\[
 {D_*\over D}
 \le
 \left({2r\over D_*^\beta}\right)^{1/(1-\beta)}
 =o(1).
\tag{3.6}
\]

Thus the published guarantee has only \(o(W)\) scale after the inflation
needed to recover a fixed power saving. This says nothing about the actual
maximum matching; it says the corollary no longer guarantees the desired
one.

### Theorem 3.1 (DP direct-host no-go)

Corollary 1.17, as stated, does not imply a matching of size
\((1-o(1))W\) in the full canonical configuration host. At the useful
degree scale there is no fixed power-codegree exponent, and both the host
edge bound and the required exponent vary with \(r\).

Corollary 1.17 is an almost-matching/coloring theorem, not an absorption
theorem. Even a hypothetical valid diagonal application would not by
itself upgrade an \(o(W)\) leave to an exact size-\(W\) matching.

## 4. Why the residual \(K^2\rho_2=o(1)\) estimate does not invoke DP

On the nonadjacent retained central band, the exact flag geometry gives

\[
 {\Delta_2\over D_*}=O(r^{-2}).
\tag{4.1}
\]

This is the correct collision scale for a purpose-built growing-uniformity
nibble: with \(K_r=O(\sqrt r)\), one has
\(K_r^2\Delta_2/D_*=O(r^{-1})\).

It is nevertheless not a fixed power of the labelled degree. If
\(D=(1+o(1))D_*\), the DP hypothesis would require

\[
 D_*^\beta=O(r^2),
\tag{4.2}
\]

which again forces \(\beta=O(1/r)\). The labelled degree is
\(\exp(\Theta(r\log r))\), so every polynomial improvement in \(r\) is
only \(D_*^{-o(1)}\).

The statement of Corollary 1.17 supplies no uniform control of
\(\alpha(R,g,\beta)\) or its degree threshold as \(R\to\infty\) and
\(\beta\to0\). One may not substitute
\(R=\Theta(\sqrt r)\), \(\beta=\Theta(1/r)\) into a fixed-parameter
asymptotic theorem and infer a diagonal conclusion.

## 5. Sharp scope and the viable next theorem

This audit rules out the implication

    canonical equitable fractional configuration
      + published DP or JMS black box
      => (1-o(1))W or W integral configurations.

It does **not** rule out:

1. **Collar-first factorization:** first solve the critical collar
   incidences exactly, then expose a residual host with no
   \(\Theta(D/r)\) pair.
2. **Purpose-built sparsification:** choose a much smaller degree subhost
   while preserving all pattern/owner degrees and the full flag codegree
   hierarchy. Proving this is itself a theorem. DP would still need a
   uniform growing-edge-size estimate; JMS would still need its ambient and
   fixed-uniformity rows.
3. **Boolean absorption or alternating exchange:** complete an almost
   matching using a structured collar absorber. Neither cited source
   supplies it.
4. **A new uniform laminar-flag matching theorem:** use the natural
   parameter \(K^2\rho_2=o(1)\), with an error uniform for
   \(K=\Theta(\sqrt r)\), rather than a fixed power of the labelled degree.

The residual \(O(r^{-2})\) ledger should be retained as genuine positive
structure. The macroscopic collar and the missing uniform
rounding/absorption theorem are the remaining black-box boundary.
