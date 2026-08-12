# Strict SBE starts from a uniform flow with an exact path-component debt

Date: 2026-07-31  
Status: exact all-parameter identity and equivalent bounded-correction
formulation.  Existence of the required correction for every recursively
supplied forest remains open.

## 0. Statement

Fix either strict direct-occurrence shore of an oriented Catalan path
forest `F` at parameter `n`.  Use

\[
 M=\binom{2n}{n},\qquad N=\binom{2n}{n-1},\qquad
 P=\binom{2n}{n-2},\qquad C=M-P,\qquad R=N-C,
\]

and put `K=M-N=Cat_n`.  Let `G=(O,X;E)` be the strict occurrence
multigraph.  Thus every `o in O` has occurrence-degree `n+2`, while

\[
                         d_G(x)=n-d_F(x)                 \tag{0.1}
\]

for `x in X`.  Choose one terminal endpoint on every nontrivial path of
`F`, and include every isolated vertex; call the resulting terminal set
`Z`.  The SBE middle load is

\[
 y_Z(x)=\begin{cases}1,&x\in Z,\\ R/N,&x\notin Z.\end{cases}      \tag{0.2}
\]

Give every occurrence edge the uniform weight

\[
                              f_0(e)={1\over n+2}.                 \tag{0.3}
\]

Then every outer vertex already has load one.  Its middle load is

\[
                  \ell_F(x)={n-d_F(x)\over n+2}.                  \tag{0.4}
\]

The required correction `b_Z=y_Z-ell_F` is completely explicit:

\[
\begin{array}{c|c}
\text{type of }x&b_Z(x)\\ \hline
\text{internal path vertex }(d_F=2)&-\dfrac{2}{n(n+2)}\\[3pt]
\text{unchosen endpoint }(d_F=1)&-\dfrac1n\\[3pt]
\text{chosen terminal endpoint }(d_F=1)&\dfrac3{n+2}\\[3pt]
\text{isolated vertex }(d_F=0)&\dfrac2{n+2}.
\end{array}                                                       \tag{0.5}
\]

If a path component has `ell` edges, including `ell=0` for an isolated
vertex, then

\[
                 \boxed{\quad b_Z(V(P))
                    ={2(n-\ell)\over n(n+2)}.\quad}               \tag{0.6}
\]

In particular the total debt of a component is independent of its chosen
orientation.  Long paths are donors, short paths are consumers, and the
mean path length is exactly `n`, so the global debt is zero.

Finally, SBE is equivalent to the existence of numbers `theta(e)` such
that

\[
\begin{aligned}
 \sum_{e\ni o}\theta(e)&=0 &&(o\in O),\\
 \sum_{e\ni x}\theta(e)&=b_Z(x) &&(x\in X),\\
 \theta(e)&\ge-{1\over n+2} &&(e\in E).
\end{aligned}                                                     \tag{0.7}
\]

Thus the unresolved SBE theorem is exactly a bounded redistribution of the
uniform outer flow.  Its orientation-dependent part consists only of one
endpoint dipole per nontrivial path; its orientation-independent part is
the path-length debt (0.6).

## 1. Proof of the load table

The exact strict candidate-degree law gives (0.1), while every outer
vertex has occurrence-degree `n+2`.  Hence (0.3) gives outer load one and
middle load (0.4).

The parameter identity

\[
 {C\over N}={2(2n+1)\over n(n+2)}
 \quad\Longrightarrow\quad
 {R\over N}=1-{2(2n+1)\over n(n+2)}                       \tag{1.1}
\]

now gives the four rows directly.  For an internal vertex,

\[
 {R\over N}-{n-2\over n+2}=-{2\over n(n+2)}.             \tag{1.2}
\]

For an unchosen endpoint,

\[
 {R\over N}-{n-1\over n+2}=-{1\over n}.                 \tag{1.3}
\]

For a chosen endpoint and an isolated vertex, respectively,

\[
 1-{n-1\over n+2}={3\over n+2},\qquad
 1-{n\over n+2}={2\over n+2}.                            \tag{1.4}
\]

This proves (0.5).

## 2. Component debt and endpoint dipoles

A nontrivial path with `ell` edges has two endpoints and `ell-1` internal
vertices.  Exactly one endpoint is chosen.  Summing (0.5) gives

\[
 {3\over n+2}-{1\over n}
 -(\ell-1){2\over n(n+2)}
 ={2(n-\ell)\over n(n+2)}.                               \tag{2.1}
\]

For an isolated vertex, (0.6) is the last row of (0.5).  Also

\[
                         N=nK,                             \tag{2.2}
\]

so the sum of all component lengths is `N=nK`.  Summing (0.6) over the
`K` components therefore gives zero, as required by the equality of the
total outer and middle loads.

Reversing a nontrivial path exchanges its chosen and unchosen endpoints.
The change at the two endpoints has magnitude

\[
 {3\over n+2}+{1\over n}
 ={4n+2\over n(n+2)}={C\over N}.                        \tag{2.3}
\]

Thus all orientation dependence is a signed endpoint dipole of strength
`C/N`; (0.6) is unchanged.

## 3. Exact bounded-correction equivalence

If `f` is an SBE fractional matching, put `theta=f-f_0`.  Both `f` and
`f_0` give every outer vertex load one, so the first row of (0.7) holds.
Their middle-load difference is `b_Z`, giving the second row, and
`f>=0` gives the third.

Conversely, any `theta` satisfying (0.7) makes

\[
                             f=f_0+\theta                         \tag{3.1}
\]

nonnegative, preserves outer load one, and changes the middle load from
`ell_F` to `y_Z`.  It is therefore the fractional matching in the SBE
equivalence theorem.  This proves (0.7).

## 4. Scope and next lemma

Equation (0.7) is not itself a construction of `theta`.  Arbitrary
zero-sum demand can have too much congestion in the strict occurrence
graph, and the authenticated small cases already show an endpoint-rounding
gap.  What the identity removes is the mystery about the right-hand side:

* the scalar imbalance is exactly the deviation of each path length from
  `n`;
* endpoint orientation contributes only fixed-strength dipoles; and
* the available per-occurrence negative capacity is exactly `1/(n+2)`.

A sufficient preservation theorem may therefore be stated as a bounded
transshipment invariant: recursively supplied strict occurrence graphs
must route every legal collection of component debts and complementary
endpoint dipoles with congestion at most `1/(n+2)`.  Proving that invariant,
or a weaker version for one coherent orientation, proves SBE and hence the
balanced strict common-basis row.

