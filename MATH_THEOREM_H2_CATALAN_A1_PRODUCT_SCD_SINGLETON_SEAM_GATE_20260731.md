# The \(a=1\) product-SCD singleton-seam gate

Date: 2026-07-31  
Status: exact raw product ledger and exact criterion inside the
SCD-aligned five-sector surgery class; no unrestricted integral recursion

## 0. Verdict

The two-coordinate fractional flow of Theorem 5.3 in
MATH_THEOREM_CATALAN_BALANCED_SUBCUBE_RESERVE_AND_EXACT_COLLAR_DEFECT_20260731.md
has a literal product-SCD explanation.

Let the collar be \(\{c,z\}\), reserve trace \(\{c\}\), and let the core
parameter be \(n=m-1\). Put

\[
 M=\binom{2n}{n},\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad K=M-N=\operatorname{Cat}_n.
 \tag{0.1}
\]

Before repair, the complement part of the product SCD has five allowed
trace sectors of sizes

\[
 P,\quad N-P,\quad P,\quad N-P,\quad P
 \tag{0.2}
\]

and \(K\) additional forbidden singleton seams from trace
\(\varnothing\) to trace \(\{c,z\}\). The target five-sector ledger is

\[
 P,\quad C,\quad R,\quad C,\quad P,
 \qquad C=M-P,\quad R=N-C=P-K.
 \tag{0.3}
\]

Since

\[
 C=(N-P)+K,\qquad R=P-K,
 \tag{0.4}
\]

an aligned repair is forced to delete every singleton seam, delete exactly
\(K\) deep \(\{z\}\to\{z\}\) flags, and replace these \(2K\) deleted
flags by \(K\) additional cross flags on each shore.

The exact incidence choice is a common-basis problem on the deep core
flags. Choose \(K\) of them so that their upper endpoints match down and
their lower endpoints match up, both bijectively, to the \(K\) core
singleton middle sets. The remaining \(P-K\) deep flags are precisely the
surviving \(z\to z\) sector. After this common basis is chosen, the sole
nonmatroidal row is that the resulting physical support be a linear forest.

This is necessary and sufficient only in the SCD-aligned surgery class
defined below. It is not a no-go for arbitrary five-sector matchings,
nonproduct flags, or a different core skeleton.

## 1. The raw product ledger

Fix an SCD \({\cal S}\) of \(B_{2n}\). A core chain has radius \(s\) when
its minimum rank is \(n-s\). The numbers of chains are

\[
\begin{array}{c|ccc}
\text{class}&s=0&s=1&s\ge2\\ \hline
\text{count}&K&N-P&P.
\end{array}
\tag{1.1}
\]

Indeed the first two entries are \(M-N\) and \(N-P\), while a chain reaches
rank \(n-2\) exactly when \(s\ge2\), giving \(P\) chains.

Use the collar SCD

\[
 \varnothing<\{z\}<\{c,z\},\qquad \{c\}.
 \tag{1.2}
\]

The singleton collar boxes give a literal child SCD on trace \(\{c\}\).
Consider the product of the long collar chain with one core chain.

### Lemma 1.1 (chain-box trace classification)

The central flags contributed by a core chain of radius \(s\) are:

\[
\begin{array}{c|l}
s=0&
 \varnothing\to\{c,z\}\quad\text{(one forbidden seam)},\\
s=1&
 \varnothing\to\{z\},\quad \{z\}\to\{c,z\},\\
s\ge2&
 \varnothing\to\varnothing,\quad
 \{z\}\to\{z\},\quad
 \{c,z\}\to\{c,z\}.
\end{array}
\tag{1.3}
\]

For a singleton core set \(S\), the forbidden seam has physical edge

\[
 \{z\}\cup S\;-\;\{c\}\cup S.
 \tag{1.4}
\]

### Proof

For \(s=0\), the product box is the long collar chain with \(S\) adjoined.
Its central flag has on-chain corner \(z+S\) and opposite corner \(c+S\).

For \(s=1\), the two equal-radius factor chains give two nontrivial product
chains, whose central triples are the two grid bends. Their outer traces are
the two cross sectors in (1.3).

For \(s\ge2\), the collar chain is shorter. The three product children,
indexed by its three members, have central triples moving only in the core
factor and therefore have the three constant traces in (1.3). \(\square\)

Summing Lemma 1.1 with (1.1) proves (0.2) and the \(K\) forbidden seams.
It also independently explains why a mere singleton collar chain is not
opposite-corner protected: Theorem 1.1 of the protected-corner note gives
the same intrusion count

\[
 Q_n(1)=M-N=K.
 \tag{1.5}
\]

## 2. The SCD-aligned surgery class

For a positive-radius core chain, let

\[
 L_e<T_e<U_e,\qquad H_e=L_e\cup(U_e\setminus T_e)
 \tag{2.1}
\]

be its central flag and edge. Split these flags into

\[
 {\cal F}_1=\{e:\rho(e)=1\},\qquad
 {\cal F}_{\ge2}=\{e:\rho(e)\ge2\}.
 \tag{2.2}
\]

Thus

\[
 |{\cal F}_1|=N-P,\qquad |{\cal F}_{\ge2}|=P.
 \tag{2.3}
\]

Let \({\cal S}_0\) be the \(K\) singleton rank-\(n\) core sets. The common
SCD port bank is

\[
 B_*=\{T_e:e\in{\cal F}_1\}\ \dot\cup\ {\cal S}_0,
 \qquad |B_*|=(N-P)+K=C.
 \tag{2.4}
\]

For \(e\in{\cal F}_1\), the two bend flags use the same forced port \(T_e\):
their physical edges are

\[
 U_e\;-\;(z+T_e),\qquad
 (z+T_e)\;-\;(cz+L_e).
 \tag{2.5}
\]

Define the SCD-aligned surgery class by the following frozen choices.

1. Keep the \(P\) diagonal flags on each of the
   \(\varnothing\to\varnothing\) and \(cz\to cz\) sectors.
2. Keep the \(2(N-P)\) radius-one bends (2.5).
3. Retain some deep flags as \(z\to z\) edges.
4. Every additional cross flag uses a deep endpoint \(U_e\) or \(L_e\) and
   a port in the singleton bank \({\cal S}_0\).

No assertion is made that an arbitrary complement matching has this normal
form.

## 3. Exact common-basis criterion

On ground set \({\cal F}_{\ge2}\), define two transversal matroids.

* \({\cal M}^-\): \(E\) is independent when the upper endpoints
  \(\{U_e:e\in E\}\) inject into distinct \(S\in{\cal S}_0\) with
  \(S\subset U_e\).
* \({\cal M}^+\): \(E\) is independent when the lower endpoints
  \(\{L_e:e\in E\}\) inject into distinct \(S\in{\cal S}_0\) with
  \(L_e\subset S\).

Write their rank functions \(r_-,r_+\).

### Theorem 3.1 (aligned outer integrality)

An outer-perfect, child-disjoint matching exists in the SCD-aligned surgery
class if and only if \({\cal M}^-,{\cal M}^+\) have a common independent set
\(E\) of size \(K\). Equivalently,

\[
 \min_{X\subseteq{\cal F}_{\ge2}}
 \bigl(r_-(X)+r_+({\cal F}_{\ge2}\setminus X)\bigr)\ge K.
 \tag{3.1}
\]

For any such \(E\), both injections are bijections onto \({\cal S}_0\), and
the surviving \(z\to z\) flags are forced to be

\[
 G={\cal F}_{\ge2}\setminus E,\qquad |G|=P-K=R.
 \tag{3.2}
\]

### Proof

The sector ledger (0.4) forces \(K\) new flags on each cross shore and
forces the deletion of \(K\) of the \(P\) deep \(z\to z\) flags. By the
definition of the aligned class, the same deleted deep set \(E\) supplies
the upper and lower endpoint banks of those new cross flags.

Middle-resource injectivity at the cross ports requires injective maps

\[
 p^-:\{U_e:e\in E\}\to{\cal S}_0,\qquad
 p^+:\{L_e:e\in E\}\to{\cal S}_0
 \tag{3.3}
\]

with \(p^-(U_e)\subset U_e\) and \(L_e\subset p^+(L_e)\). Since both shores
have order \(K\), these maps are bijections. This is exactly common
independence of size \(K\). Formula (3.1) is Edmonds' matroid-intersection
min-max theorem. Conversely, the two bijections construct the missing cross
flags; (0.4) then checks every outer row and column. \(\square\)

The new edges at a singleton port \(S\) are

\[
 U_{e^-}\;-\;(z+S),\qquad
 (z+S)\;-\;(cz+L_{e^+}),
 \tag{3.4}
\]

where the two bijections may assign different deep flags \(e^-,e^+\).
Thus every old seam vertex \(z+S\) becomes a degree-two splice and the
reserved vertex \(c+S\) is detached.

### Corollary 3.2 (exact incidence no-go)

The aligned class is impossible if any of the following holds:

1. \(P<K\), equivalently the target \(R=P-K\) is negative;
2. the min in (3.1) is below \(K\);
3. on either shore, some port subset \(Y\subseteq{\cal S}_0\) has fewer than
   \(|Y|\) incident deep endpoints.

Items 2 and 3 are certificate-level Hall/matroid obstructions. For \(n\ge3\),
the scalar obstruction disappears, but the incidence rows need not.

### Proposition 3.3 (canonical BTK has rank-zero deep incidence)

For the canonical BTK/Greene--Kleitman SCD, neither transversal matroid has
any deep incidence:

\[
 r_-({\cal F}_{\ge2})=r_+({\cal F}_{\ge2})=0.
 \tag{3.5}
\]

Consequently the SCD-aligned \(a=1\) repair is impossible for the canonical
BTK core in every positive parameter.

### Proof

Encode a set by a parenthesis word, with \(0\) an opening step and \(1\) a
closing step. A BTK singleton is exactly a balanced word whose prefix
heights are nonnegative.

If \(S\) is such a singleton and \(U\supset S\) has rank \(n+1\), then
\(U\) is obtained by changing one opening step of \(S\) to a closing step.
Every suffix height drops by two, so the resulting path has endpoint and
minimum both equal to \(-2\). Its BTK bracketing therefore has exactly two
unmatched closing positions and no unmatched opening position. Thus \(U\)
lies on a radius-one chain.

Dually, if \(L\subset S\) has rank \(n-1\), changing one closing step to
an opening step leaves a nonnegative path of endpoint \(2\). It has exactly
two unmatched opening positions and lies on a radius-one chain.

Hence no upper endpoint of a deep flag contains a singleton and no lower
endpoint of a deep flag is contained in a singleton. Both incidence graphs
in Section 3 are empty. \(\square\)

This is a no-go for the canonical BTK/product-aligned mechanism, not for a
non-BTK SCD or a nonproduct five-sector realization.

## 4. The remaining physical row

Once \(E,p^-,p^+\) are fixed, let \({\cal R}(E,p^-,p^+)\) be the union of

1. the two fixed diagonal edge families;
2. the radius-one bend edges (2.5);
3. the retained \(z\to z\) edges indexed by \(G\);
4. the singleton splice edges (3.4).

### Theorem 4.1 (exact aligned CLM criterion)

The SCD-aligned surgery gives a complement linear forest if and only
if

\[
 {\cal R}(E,p^-,p^+)\text{ is a linear forest.}
 \tag{4.1}
\]

When (4.1) holds, orienting every path consistently gives injective tail and
head roles and no physical cycle. Conversely, any injective acyclic
orientation has undirected degree at most two and no cycle, hence (4.1).

If the supplied child central graph on trace \(\{c\}\) is also a path
forest, it is vertex-disjoint from this complement support; their union is
the ambient Catalan linear matching.

Thus the \(a=1\) product-SCD gate separates exactly into

\[
 \boxed{\text{common transversal basis (3.1)}
 \quad+\quad\text{graphic path-forest row (4.1)}.}
 \tag{4.2}
\]

Theorem 3.1 decides outer integrality and singleton-seam removal. It does
not decide (4.1).

## 5. Scope

This note sharpens Theorem 6.1 and Corollary 6.3 of the balanced-subcube
reserve theorem only for a fixed product SCD and the aligned surgery class.
It proves:

* the raw trace ledger and all singleton seams;
* the forced deletion count among the remaining \(z\to z\) flags;
* an exact matroid-intersection certificate for the two port shores; and
* the final linear-forest criterion.

For the canonical BTK core, Proposition 3.3 closes the aligned class before
the forest row. The independent finite replay

    scratch/audit_catalan_a1_fiveflow_product_btk_gate_20260731.py
    scratch/catalan_a1_fiveflow_product_btk_gate_20260731.audit.json

checks the empty donor/incidence phenomenon and the complete raw product
through ambient parameters \(m=4,\ldots,8\).

It does not prove that (3.1) holds for every core SCD/CLM, that some common
basis satisfies (4.1), or that arbitrary five-sector complement matchings
normalize to this class.
