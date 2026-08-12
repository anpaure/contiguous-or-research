# Audit of the fixed-colour-pair normal form and lexical-capacity obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

Audited source:
MATH_THEOREM_Q1_FIXED_COLOR_PAIR_NORMAL_FORM_AND_LEXICAL_CAPACITY_OBSTRUCTION_20260726.md.

## 0. Verdict

The source is mathematically sound. I found no invalid theorem or count.
In particular:

1. the fixed-pair path/cycle normal form and its converse are exact;
2. the GMM--dummy augmentation really produces a restricted proper
   \((m+1)\)-edge-colouring whose selected pair is a spanning forest with
   exactly \(D\) nonempty paths;
3. the omitted-owner facet SDR follows from the Lovasz shadow inequality;
4. exactly \(D\) projected GMM edges are replaced, so the upper-hole count
   changes by at most \(D\);
5. the local colour-pair multigraph and endpoint-margin formulas are exact;
6. all-pairs perfection forces \(S(m-1,m,2m)\), and the odd-\(m\)
   quantitative obstruction is correctly normalized;
7. the Greene--Kleitman alternate map has exactly \(W/2\) holes and
   overload excess \(W/2-D\), giving the stated linear capacity loss.

There are only two presentational qualifications.

* In the Kruskal--Katona proof, the empty subfamily should be separated
  before dividing by \(x-m+1\). For every nonempty subfamily one has
  \(x\ge m\), so the displayed ratio is valid.
* The deletion lower bound \(W/4-D\) is mathematically correct even when
  negative; the uniformly nonnegative formulation is
  \(\max\{0,W/4-D\}\). Its asymptotic content is unchanged.

The note does not prove the remaining upper-union estimate and does not
prove constant one.

## 1. Basic degree census and fixed-pair factor

For the inclusion graph \(B_m\) between ranks \(m-1\) and \(m\) of
\([2m]\), the lower degree is \(m+1\), the middle degree is \(m\), and

\[
 W=\binom{2m}m,\qquad
 N=\binom{2m}{m-1}={m\over m+1}W,\qquad
 D=W-N={W\over m+1}.
\]

In a proper \((m+1)\)-edge-colouring, every lower vertex sees every
colour once, while every middle owner sees \(m\) distinct colours and
therefore misses exactly one.

Fix two colours \(a,b\). Suppressing a lower vertex \(R\) between its
\(a\)- and \(b\)-neighbours gives one Johnson edge of intersection \(R\).
Thus there are exactly \(N\) distinct projected edges and every lower
colour occurs once. At a middle owner \(X\), the projected degree is the
number of \(a,b\) present at \(X\), hence

\[
 d_{F_{ab}}(X)=
 \begin{cases}
 1,&\mu(X)\in\{a,b\},\\
 2,&\mu(X)\notin\{a,b\}.
 \end{cases}
\]

Each colour class is a matching saturating all \(N\) lower vertices. It
therefore meets \(N\) middle owners and misses \(D\). Orienting from the
\(a\)-neighbour to the \(b\)-neighbour gives:

* \(D\) sources, namely the owners missing \(b\);
* \(D\) sinks, namely the owners missing \(a\);
* indegree and outdegree one elsewhere.

Every noncyclic component is consequently a directed source-to-sink path,
and there are exactly \(D\) such paths. The remaining components are
directed cycles. This verifies Theorem 1.1 and

\[
                       \operatorname{comp}(F_{ab})=D+c_{ab}.
\]

## 2. Converse proper-colouring normal form

Given a spanning lower-rainbow Johnson graph \(F\) with all owner degrees
one or two, subdivide the edge of lower colour \(R\) at \(R\). The resulting
bipartite graph \(H\subseteq B_m\) has degree two at every lower vertex and
degree one or two at every middle vertex. Each path or even-cycle component
has a proper alternating two-edge-colouring by \(a,b\).

After deleting \(H\), every lower degree is \(m-1\), while every middle
degree is \(m-d_F(X)\le m-1\). Konig's line-colouring theorem therefore
colours the residue with \(m-1\) new colours. At every lower vertex those
\(m-1\) colours all occur, so together with \(a,b\) the result is a proper
\((m+1)\)-edge-colouring. Its fixed-pair suppression is exactly \(F\).
There is no hidden regularity, parity, or component hypothesis in Theorem
1.2.

For a fixed pair, the upper loads \(k_U(a,b)\) have total \(N=|\mathcal U|\).
Therefore holes, repeat excess, and half the \(L^1\) discrepancy are equal:

\[
 |\{U:k_U=0\}|=\sum_U(k_U-1)_+
 ={1\over2}\sum_U|k_U-1|.
\]

This verifies Corollary 1.3. Since

\[
 {D\over W/H}={H\over m+1}\longrightarrow0
\]

for \(H=o(m)\), only \(c_{ab}=o(W/H)\) is additionally needed for the
component rate in a general fixed-pair factor.

## 3. Facet SDR for the omitted GMM owners

Let \(\mathcal E\) be the \(D\) middle owners omitted by a GMM saturating
cycle. For \(\mathcal A\subseteq\mathcal E\), write
\(|\mathcal A|=\binom{x}{m}\) in generalized-binomial notation. The Lovasz
form of Kruskal--Katona gives

\[
                    |\partial\mathcal A|\ge\binom{x}{m-1}.
\]

For nonempty \(\mathcal A\),

\[
 |\mathcal A|\le D={W\over m+1}
 \le {W\over2}=\binom{2m-1}{m}
\]

implies \(m\le x\le2m-1\). Hence

\[
 {\binom{x}{m-1}\over\binom{x}{m}}
 ={m\over x-m+1}\ge1.
\]

The empty family satisfies Hall trivially. Thus every subfamily has at
least as many lower facets, and Hall supplies an injective map
\(\phi(Y)\subset Y\). The source's SDR argument is valid for every
\(m\ge2\); no \(m\ge6\) restriction is needed.

Fixing one alternating matching of the GMM cycle maps the distinct facets
\(\phi(Y)\) to distinct cycle owners \(X_Y\). These owners are outside
\(\mathcal E\). Therefore all \(2D\) designated vertices \(Y,X_Y\) are
distinct.

## 4. Audit of the GMM--dummy Hamilton augmentation

The identity \(W=D(m+1)\) permits a partition of all middle owners into
\(D\) groups \(G_Y\) of size \(m+1\), each containing \(Y,X_Y\): after
placing those two owners, exactly \(D(m-1)\) owners remain.

Adding one dummy lower vertex adjacent to each group makes the augmented
graph balanced and \((m+1)\)-regular:

* every real lower vertex already has degree \(m+1\);
* every dummy has degree \(m+1\);
* every middle owner gains exactly one dummy incidence and goes from
  degree \(m\) to \(m+1\).

The incidence edges \(X_YR_Y\) selected on the GMM cycle are distinct.
Replacing each by

\[
                         X_Y-d_Y-Y-R_Y
\]

inserts every dummy and every omitted owner exactly once. All three new
incidences are legal. Thus the result is a simple Hamilton cycle of the
augmented bipartite graph.

Alternately colour this Hamilton cycle by \(a,b\). Removing its edges leaves
an \((m-1)\)-regular bipartite graph, which decomposes into \(m-1\) perfect
matchings. Hence the augmented colouring is proper. Restriction to the
original \(B_m\) remains proper: every real lower vertex retains all
\(m+1\) colours, and every middle owner merely loses its unique dummy edge.

Deleting the \(D\) dummy vertices cuts the Hamilton cycle into exactly
\(D\) paths. They are nonempty after suppression because no middle owner
is a designated neighbour of two dummies: the \(Y,X_Y\) are all distinct.
The paths span every real lower vertex and every middle owner. Suppressing
real lower vertices therefore produces a spanning lower-rainbow Johnson
linear forest with exactly \(D\) path components and no cycles.

This verifies every structural assertion of Theorem 2.1. In particular,
the proper-colouring restriction does not introduce additional fixed-pair
edges: at every real lower vertex the \(a,b\) edges are precisely its two
Hamilton-cycle incidences.

## 5. Exact projected-edge and upper-hole edit ledger

At \(R_Y\), let \(Z_Y\) be the old GMM cycle neighbour other than \(X_Y\).
Before augmentation the projected edge of lower colour \(R_Y\) is
\(Z_YX_Y\); after deleting the dummy it is \(Z_YY\). These edges differ
because \(Y\) is an omitted owner. Every other lower colour retains its
old projected edge.

Thus exactly \(D\) entries of the \(N\)-term upper-colour multiset are
replaced. Replacing one multiset entry changes support size by at most one,
so

\[
                         |h_+(F)-c_+(P)|\le D.
\]

Because \(D=o(W)\), this proves the equivalence in Corollary 2.2:
\(h_+(F)=o(W)\) if and only if \(c_+(P)=o(W)\). It does not estimate either
quantity.

## 6. Local upper-pair and endpoint ledgers

For a fixed \(U\), each row \(y\in U\) is the middle facet \(U\setminus
\{y\}\). Properness at that middle owner makes the row colours

\[
 \{A_U(y,x):x\ne y\}=C\setminus\{\mu(U\setminus\{y\})\}.
\]

The two entries associated with \(\{x,y\}\) are distinct because their
inclusion edges meet at the same lower vertex. Thus \(p_U\) has no loops.
Its multiplicity at \(\{a,b\}\) is exactly \(k_U(a,b)\), and the degree of
colour \(a\) is

\[
                       \sum_{b\ne a}k_U(a,b)=m+1-n_a(U).
\]

This verifies Proposition 3.1 and confirms the logical distinction:
perfection of one fixed pair asks only \(k_U(a,b)=1\); bijectivity of every
\(p_U\) is much stronger.

Summing the diamond identity

\[
                       1_R+1_U=1_X+1_Y
\]

over the fixed-pair factor gives

\[
 d_{\mathcal E_{ab}}(x)-D
 =-\sum_{\substack{U\ni x}}(k_U(a,b)-1).
\]

Here

\[
 2d_{\mathcal M}(x)-d_{\mathcal L}(x)-d_{\mathcal U}(x)=D
\]

is correct. Summing the triangle inequality and using that each upper set
has \(m+1\) coordinates yields

\[
 \sum_x|d_{\mathcal E_{ab}}(x)-D|
 \le 2(m+1)h_{ab}.
\]

Exact upper coverage therefore forces point degree \(D\) in the endpoint
family. For the dummy forest, its endpoints are exactly the pairwise
disjoint family \(\mathcal E\dot\cup\{X_Y:Y\in\mathcal E\}\).

## 7. All-pairs obstruction

If every \(p_U\) is a bijection, its colour multigraph is \(K_{m+1}\).
The degree identity above then gives \(n_a(U)=1\) for every \(a,U\).
Consequently two members of one missing-colour fibre \(\mathcal M_a\)
cannot share an \((m-1)\)-facet. Since

\[
                         m|\mathcal M_a|=mD=N=|\mathcal L|,
\]

their lower facets partition \(\mathcal L\). Thus every \(\mathcal M_a\)
is \(S(m-1,m,2m)\).

Fixing an \((m-2)\)-set reduces blocks through it to disjoint pairs on the
remaining \(m+2\) points. Exact lower-facet coverage makes those pairs a
perfect matching, forcing \(m+2\) even. Hence all-pairs perfection is
impossible for odd \(m\).

For the quantitative statement, an independent family
\(\mathcal I\subseteq J(2m,m)\) has, through any fixed \((m-2)\)-set, at
most \((m+1)/2\) blocks when \(m\) is odd. Double counting gives

\[
 |\mathcal I|\binom m2
 \le\binom{2m}{m-2}{m+1\over2},
 \qquad
 |\mathcal I|\le {W\over m+2}.
\]

Deleting all but one \(\mathcal M_a\)-facet from each overloaded upper set
uses at most

\[
 h_a=\sum_U(n_a(U)-1)_+
\]

deletions and leaves an independent family. Therefore

\[
 h_a\ge D-{W\over m+2}
 ={W\over(m+1)(m+2)}.
\]

At one \(U\), the support graph's total missing degree is \(2\delta_U\).
It dominates the positive degree deficit of the colour multigraph, namely
\(\sum_a(n_a(U)-1)_+\). Hence

\[
 \delta_U\ge {1\over2}\sum_a(n_a(U)-1)_+.
\]

Summation verifies

\[
 \sum_U\delta_U=\sum_{\{a,b\}}h_{ab}
 \ge {W\over2(m+2)}.
\]

As the source emphasizes, this aggregate obstruction says nothing against
one selected pair having \(o(W)\) holes.

## 8. Greene--Kleitman lexical capacity audit

Every Greene--Kleitman chain meeting rank \(m-1\) also meets rank \(m+1\),
and every such chain contains exactly one set of each rank. This gives the
stated bijection \(\Phi:\mathcal L\to\mathcal U\). Its interval has one
primary and one alternate middle owner.

For a balanced word \(Y\), the standard unmatched-symbol decomposition has
\(j\) unmatched zeroes, \(j\) unmatched ones, \(2j\) noncentral Dyck
slots, and one central Dyck slot. Choosing a primitive factor of the
central slot and changing its first opening symbol to a closing symbol
produces exactly one lower word whose alternate is \(Y\). The primitive
interior remains matched, and the changed first symbol and terminal symbol
are the last two unmatched zeroes. Reversing this operation recovers the
chosen primitive factor. Thus Lemma 5.1,

\[
                         \#\{R:\operatorname{alt}(R)=Y\}=\rho(Y),
\]

is correct.

For exactly \(k\) primitive central factors, the generating function is

\[
 B_k(z)=\sum_{j\ge0}z^jC(z)^{2j}P(z)^k
 ={P(z)^k\over1-zC(z)^2}
 ={P(z)^k\over2-C(z)}.
\]

With \(s=\sqrt{1-4z}\) and \(C(z)=2/(1+s)\),

\[
 B_0(z)={1+s\over2s}.
\]

For every \(m\ge1\), its \(z^m\)-coefficient is
\(\frac12\binom{2m}m=W/2\). Hence the alternate map omits exactly \(W/2\)
owners.

The total alternate multiplicity is the number of lower flags:

\[
                         \sum_Y\rho(Y)=N.
\]

Consequently

\[
 \sum_Y(\rho(Y)-1)_+={W\over2}-D.
\]

There are exactly \(D=W-N\) singleton chains: these are precisely the
chains beginning at central rank \(m\). Primary incidence is one on every
non-singleton-chain owner and zero on a singleton-chain owner. A singleton
can absorb at most one unit of alternate excess, so the total positive
middle-degree excess is at least

\[
                         {W\over2}-2D.
\]

Deleting one interval removes two owner incidences and reduces this excess
by at most two. Thus at least

\[
                         \max\{0,W/4-D\}
\]

flags must be deleted before every middle degree is at most two. This is
linear in \(W\) asymptotically and verifies Theorem 5.2's obstruction.

## 9. Exact boundary

The audited positive chain is

\[
 \text{GMM saturating cycle}
 \Longrightarrow
 \text{fixed-pair spanning forest with exactly }D\text{ paths}.
\]

For \(H=o(m)\), its component count is \(o(W/H)\). The only remaining
estimate in this lane is the opposite-colour bound

\[
 N-\left|\{R_{i-1}\cup R_i\cup R_{i+1}\}\right|=o(W)
\]

for a suitable GMM saturating cycle. Neither the fixed-pair normal form,
the endpoint margin, the all-pairs obstruction, nor the lexical calculation
proves this estimate.
