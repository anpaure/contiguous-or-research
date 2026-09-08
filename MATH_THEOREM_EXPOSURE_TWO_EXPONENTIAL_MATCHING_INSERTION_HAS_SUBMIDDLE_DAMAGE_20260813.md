# Exposure-two exponential protected matchings insert with submiddle damage

**Date:** 2026-08-13  
**Status:** unconditional asymptotic matching theorem.  In the balanced
middle incidence graph, a protected matching of size
\(r^{O(1)}2^r\) with both all-occurrence exposures at most two can be
inserted into any prescribed perfect matching while changing only
\(r^{O(1)}2^r=o(W)\) edges.  For the two colours of the transversal lift,
the corresponding simple-factor statement is conditional on a joint
edge-disjoint extension theorem.  Residence and upper-source repair on the
damaged bank remain open.

## 1. Setting

Let

\[
 \mathcal L={{[2r-1]}\choose {r-1}},\qquad
 \mathcal U={{[2r-1]}\choose r},\qquad
 W=|\mathcal L|=|\mathcal U|,                         \tag{1.1}
\]

and let \(G\) be their \(r\)-regular incidence graph.  Let \(F\) be a
matching, with lower endpoint set \(Z\), upper endpoint set \(Y\), and

\[
 f=|F|\le r^C2^r                                    \tag{1.2}
\]

for one fixed constant \(C\).  Assume the all-occurrence exposures

\[
 \widehat\alpha(F)=\max_{x\in\mathcal L}|N(x)\cap Y|,
 \qquad
 \widehat\beta(F)=\max_{U\in\mathcal U}|N(U)\cap Z|  \tag{1.3}
\]

satisfy

\[
                         \widehat\alpha(F),
                         \widehat\beta(F)\le2.        \tag{1.4}
\]

Every prefix of any ordering of \(F\) inherits (1.4).

The sharp protected-matching theorem already implies that \(F\), and
every prefix of \(F\) together with one additional residual edge, extends
to a perfect matching: indeed

\[
 rf=2^{r+O(\log r)}
   =o\left({2r-5\choose r-2}\right).                 \tag{1.5}
\]

The point here is a stronger *relative* conclusion.

## 2. Uniform alternating diameter

Fix a prefix \(F_j\), delete its endpoints, and let \(B_j\) be the residual
incidence graph.  Choose any perfect matching \(N\) of \(B_j\).  Contract
the edges of \(N\), retaining a loop at every contracted vertex, and draw
an arc \(x\to z\) when \(xN(z)\) is an incidence edge of \(B_j\).  Call the
resulting exchange digraph \(D_j\).

### Lemma 2.1

There is an absolute constant \(K\) such that, for every prefix \(j\le f\)
and every choice of \(N\),

\[
                         \operatorname {diam}(D_j)\le Kr^2             \tag{2.1}
\]

for all sufficiently large \(r\).

#### Proof

Let \(S\) be a forward set in \(D_j\), identified with its residual lower
vertices.  Then

\[
 |\Gamma^+(S)|=|N_G(S)\setminus Y_j|.                \tag{2.2}
\]

First suppose

\[
                         |S|\le4rf.                  \tag{2.3}
\]

Complementing \(S\) gives an \(r\)-uniform family of the same size.  Write
\(|S|={x\choose r}\) in the real-binomial convention.  Since

\[
 {\lfloor13r/10\rfloor\choose r}
   =2^{(1+\eta)r-O(\log r)}                           \tag{2.4}
\]

for an absolute \(\eta>0\), (1.2)--(2.3) imply
\(x<13r/10\) eventually.  Lovász--Kruskal--Katona gives

\[
 { |N_G(S)|\over|S|}
 \ge {r\over x-r+1}>{10\over3}-o(1).                \tag{2.5}
\]

By (1.4), at most \(2|S|\) deleted upper vertices meet \(S\).  Therefore

\[
                         |\Gamma^+(S)|>(4/3-o(1))|S|. \tag{2.6}
\]

In particular a forward ball grows by a fixed factor until its size
exceeds \(4rf\), in \(O(r)\) steps.

For \(4rf<|S|\le W/2\), the Johnson spectral-surplus bound used in the
sharp protected-matching theorem gives

\[
 |\Gamma^+(S)|-|S|\ge {|S|\over2r}-j
                         \ge {|S|\over4r}.           \tag{2.7}
\]

Thus another \(O(r\log W)=O(r^2)\) steps make the forward ball larger
than \(W/2\).

Apply the same argument to the reverse digraph.  Here the deleted lower
shore is controlled by \(\widehat\beta(F)\le2\); complementation gives the
same small-family estimate, and the reverse spectral estimate is
identical.  A backward ball also exceeds \(W/2\) within \(O(r^2)\) steps.
The two balls meet, proving (2.1).  \(\square\)

## 3. Relative insertion

### Theorem 3.1

For every perfect matching \(H\) of \(G\), there is a perfect matching
\(M\supseteq F\) satisfying

\[
                         |M\mathbin\triangle H|\le K' r^2 f             \tag{3.1}
\]

for an absolute constant \(K'\) and all sufficiently large \(r\).

#### Proof

Order the edges of \(F\) and insert them one at a time.  Suppose the
current perfect matching contains \(F_j\).  If the next edge is absent,
delete the prefix endpoints and contract the current residual perfect
matching.  Lemma 2.1 supplies a directed return path which, together with
the desired new arc, is an alternating cycle avoiding \(F_j\).  Switching
on this cycle inserts the next protected edge and changes \(O(r^2)\)
matching edges.  Summing over \(f\) insertions gives (3.1).  \(\square\)

### Corollary 3.2 (the exact two-colour gate)

Let \(P\) be an even protected incidence cycle and alternately colour its
edges \(F_0,F_1\), with both colours satisfying (1.2)--(1.4).  Given either
perfect matching \(H_i\), Theorem 3.1 separately supplies a nearby perfect
matching \(M_i\supseteq F_i\) with

\[
                         |M_i\mathbin\triangle H_i|=O(r^2|F_i|).        \tag{3.2}
\]

This does **not** yet give a simple two-factor.  The two separately chosen
extensions can share an incidence edge, even when the base matchings are
disjoint.  An alternating return path used while inserting \(F_0\) may use
an edge of \(F_1\), or an edge later selected by the other extension.

Consequently the exact remaining incidence statement is a joint one:

> construct the two extensions with \(M_0\cap M_1=\varnothing\), while
> retaining the separate damage bounds (3.2).

Equivalently, one may first extend \(F_0\) inside \(G-F_1\) and then extend
\(F_1\) inside \(G-M_0\), but the residual expansion/allowed-edge theorem
must be reproved after deleting the other, generally nonfixed matching.
Ordinary one-colour protected matching extension does not imply this.

For the transversal lift, \(|F_0|=|F_1|=2^{r-1}\), so a positive joint
theorem at the same scale would give total damage

\[
                         r^{O(1)}2^r=o(W).             \tag{3.3}
\]

That implication is conditional here.

## 4. Scope

For one colour, the conclusion is substantially stronger than an arbitrary
matching completion: almost all edges of a prescribed perfect matching
survive.  Turning the two one-colour statements into a simple factor is the
first remaining gate.  Even after that gate, the changed bank must be
chronologically ordered with positive run floor \(q\), and all upper and
source occurrences lost there must be rematerialized.  Those requirements
are nonhereditary and must be imposed on the alternating returns or repaired
on the resulting damaged bank.
