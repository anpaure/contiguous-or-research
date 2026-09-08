# Global Dyck-hash collar braids: an exact triangular compiler and the phase-freeze obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

There is a precise algebraic way in which a nonlocal Dyck-word hash can
break hereditary excursion blindness without violating either ownership
ledger.

The required object is a **split exterior braid module**. Before the Dyck
excursion, the module routes an exterior row label \(c\) to
\(\rho_a(c)\), where \(a\) is a code symbol. After the excursion it
applies the inverse logical route. Every code state has the same physical
prefix and suffix \(X/Y\) palettes. Thus total exterior holonomy is zero,
although the stationary collar seen during the excursion is nontrivial.

If the Dyck filling is \(u\) and \(a=h(u)\), the middle owner map is the
triangular Latin shear

\[
                 (c,u)\longmapsto(\rho_{h(u)}c,u).       \tag{0.1}
\]

It is a bijection for every hash \(h\), since every \(\rho_a\) is a
permutation. Theorem 2.1 proves literally and integrally that this
preserves all lower states, all adjacent-union colours, and every
complementary endpoint.

For fixed exterior root \(c\), a window swallowing the Dyck excursion has
target

\[
                         Q_{\rho_{h(u)}c}.               \tag{0.2}
\]

Thus its load is exactly the largest fibre of
\(u\mapsto\rho_{h(u)}c\). An orbit of size \(M\) permits the sharp
one-context bound

\[
                 \max_T\mu(T)\le \left\lceil {C_r\over M}\right\rceil
                                                               \tag{0.3}
\]

when the hash is chosen to balance that fixed context. One hash balances
all contexts simultaneously when the router permutations contain a
regular translation action; orbit size alone does not imply this stronger
simultaneous conclusion.

In the geodesic boundary identity the construction uses

\[
 O_L(c,u)=O_R(c,u)=Q_{\rho_{h(u)}c},\qquad \tau u=u.     \tag{0.4}
\]

Both sides of

\[
 |O_L(c,u)\setminus O_R(c,u)|
       =|P_u\setminus P_{\tau u}|
\]

are zero, while the stationary exterior depends on \(u\). This is the
filling-dependent escape left open by the fixed-collar theorem.

There is also a statewise obstruction. If a proposed twist keeps every
step between consecutive fixed-rank Chung--Feller layers and only
relabels a fixed-rank exterior context, Johnson-distance additivity
forces the exterior address to be constant at every step. Hence an actual
MSW/PBBS realization of (0.1) must spend physical exterior-router steps,
or use cross-block rank-changing steps.

Alternating \(C_6/C_8\) strand switches would supply the routers under
the literal hypotheses of Proposition 4.1: a prefix word realizes
\(\rho_a\), and a suffix word realizing \(\rho_a^{-1}\) closes the
logical holonomy. What is not proved is the PBBS supply theorem:
no growing serial switch-stable router atlas with orbit at least \(C_r/p\)
is presently known inside one exact MSW/PBBS factor. Thus this report
gives an exact compiler and an exact no-go, but not coefficient one.

## 1. Split exterior braid modules

Let \(E,J\) be disjoint coordinate sets with

\[
                         |E|=2s,\qquad |J|=2r.
\]

Let \(\mathcal C\) be an exterior row set. For \(c\in\mathcal C\), let
\(R_c\subset E\) have size \(s\), with \(c\mapsto R_c\) injective. Let

\[
 P_u=B_0(u),B_1(u),\ldots,B_r(u)=J\setminus P_u,
                  \qquad u\in\mathcal D_r,             \tag{1.1}
\]

be an exact rooted \(\mathcal D_r\)-port factor on \(J\). Put

\[
                         V_t(u)=B_t(u)\cup B_{t+1}(u).  \tag{1.2}
\]

Fix a cut \(0\le k\le s\), a finite alphabet \(\mathcal A\), and, for
every \(a\in\mathcal A\), exterior paths

\[
 R_c=A^a_0(c),A^a_1(c),\ldots,A^a_s(c)=E\setminus R_c,
                  \qquad c\in\mathcal C.               \tag{1.3}
\]

Every consecutive pair in (1.3) is a Johnson edge. Write

\[
                         U^a_i(c)=A^a_i(c)\cup A^a_{i+1}(c).
                                                               \tag{1.4}
\]

### Definition 1.1 (split module)

The family (1.3) is a split exterior braid module at cut \(k\) when:

1. the fixed-port identities (1.3) hold for every \(a,c\);
2. for all \(a,a'\), the complete physical prefix multisets

   \[
   \biguplus_{\substack{c\in\mathcal C\\0\le i\le k}}
       \{A^a_i(c)\},\qquad
   \biguplus_{\substack{c\in\mathcal C\\0\le i<k}}
       \{U^a_i(c)\}                                     \tag{1.5}
   \]

   equal their \(a'\)-counterparts;
3. the analogous complete suffix multisets

   \[
   \biguplus_{\substack{c\in\mathcal C\\k\le i\le s}}
       \{A^a_i(c)\},\qquad
   \biguplus_{\substack{c\in\mathcal C\\k\le i<s}}
       \{U^a_i(c)\}                                     \tag{1.6}
   \]

   are independent of \(a\); and
4. there are distinct \(s\)-sets \(Q_c\subset E\) and permutations
   \(\rho_a\in\operatorname{Sym}(\mathcal C)\) such that

   \[
                         A^a_k(c)=Q_{\rho_a(c)}.         \tag{1.7}
   \]

The prefix and suffix hypotheses are equalities of physical token
multisets, not merely equal counts. Columnwise lower equality is a useful
stronger condition but is not needed below.

## 2. Exact triangular hash-braid compiler

Choose any hash

\[
                         h:\mathcal D_r\longrightarrow\mathcal A. \tag{2.1}
\]

For each \((c,u)\), concatenate the following three path pieces, counting
each common join state only once:

\[
\begin{array}{ll}
\text{prefix:}&A^{h(u)}_i(c)\cup P_u,\quad 0\le i\le k,\\[1mm]
\text{excursion:}&Q_{\rho_{h(u)}c}\cup B_t(u),\quad 0\le t\le r,\\[1mm]
\text{suffix:}&A^{h(u)}_i(c)\cup(J\setminus P_u),\quad k\le i\le s.
\end{array}                                                   \tag{2.2}
\]

### Theorem 2.1 (triangular compiler)

Assume that for one fixed code \(a_0\), the paths (2.2) with
\(h\equiv a_0\) form a literal exact product packet. Then the paths (2.2)
for arbitrary \(h\) own exactly the same physical token multiset and are
a literal integral exact replacement of that packet. Specifically:

1. every row is a length-\((s+r)\) Johnson geodesic from

   \[
        R_c\cup P_u\quad\hbox{to}\quad
        (E\setminus R_c)\cup(J\setminus P_u);           \tag{2.3}
   \]
2. the complete lower-state multiset is independent of \(h\);
3. the complete adjacent-union multiset is independent of \(h\); and
4. every root is paired with its literal complement.

Therefore (2.2) may replace a port-closed occurrence of the baseline
product packet inside one exact middle factor.

#### Proof

Moves in the prefix and suffix change only \(E\), and moves in the middle
change only \(J\). The common states at the joins agree by (1.7). Thus
every move is a Johnson edge. The row has \(s+r\) moves, while the two
sets in (2.3) are complementary \((s+r)\)-sets and have Johnson distance
\(s+r\). Hence the row is geodesic.

For prefix and suffix lower ownership, fix \(u\). The \(J\)-restriction is
respectively \(P_u\) and \(J\setminus P_u\). These tags are injective in
\(u\), and (1.5)--(1.6) make the exterior palettes code-independent.

In the middle, for fixed \(u\), the map

\[
                         c\longmapsto\rho_{h(u)}c       \tag{2.4}
\]

is a permutation. Hence, at every local phase \(t\), the states are

\[
 \{Q_d\cup B_t(u):d\in\mathcal C,\ u\in\mathcal D_r\}              \tag{2.5}
\]

once each. This proves the complete lower ledger.

In adding the prefix, middle, and suffix ledgers, the two common seam
palettes

\[
 \{Q_d\cup P_u:d,u\},\qquad
 \{Q_d\cup(J\setminus P_u):d,u\}                       \tag{2.5a}
\]

are each subtracted once, because the joined state occurs only once in
(2.2). Both multisets are code-independent by (2.4). Thus the preceding
comparison is an equality with the fixed-code baseline, with no hidden
double count.

The upper ledger is identical. Prefix and suffix colours are
code-independent by (1.5)--(1.6), after adjoining their respective
\(J\)-tags. Middle colours are exactly

\[
 \{Q_d\cup V_t(u):
       d\in\mathcal C,\ u\in\mathcal D_r,\ 0\le t<r\}              \tag{2.6}
\]

once each, again by (2.4). No edge occurs at either identified join.
Finally (2.3) gives the complementary endpoints. The assumed baseline is
collision-free and exact, and the new physical multiset is identical to
it, so the replacement is collision-free and exact as well. \(\square\)

The middle Latin map is

\[
 \Lambda_h(c,u)=(\rho_{h(u)}c,u),\qquad
 \Lambda_h^{-1}(d,u)=(\rho_{h(u)}^{-1}d,u).            \tag{2.7}
\]

Thus no fractional completion is hidden in the construction.

## 3. Exact fibre and coding bounds

Since (1.1) is a geodesic from \(P_u\) to its complement,

\[
                         \bigcap_{t=0}^r B_t(u)=\varnothing.
\]

Consequently

\[
 \boxed{\;
 \bigcap_{t=0}^r
       (Q_{\rho_{h(u)}c}\cup B_t(u))
       =Q_{\rho_{h(u)}c}.\;}                          \tag{3.1}
\]

### Theorem 3.1 (one-context fibre formula)

For fixed \(c\), the load at \(Q_d\) is exactly

\[
             |\{u\in\mathcal D_r:\rho_{h(u)}c=d\}|.    \tag{3.2}
\]

Put

\[
                         M_c=|\{\rho_a c:a\in\mathcal A\}|.       \tag{3.3}
\]

For this fixed \(c\), a hash can be chosen with maximum load

\[
                         \left\lceil{C_r\over M_c}\right\rceil,   \tag{3.4}
\]

provided every displayed image has a code representative. For arbitrary
\(h\), its cap-\(b\) excess satisfies

\[
       \sum_d(\mu_c(Q_d)-b)_+\ge(C_r-bM_c)_+.           \tag{3.5}
\]

#### Proof

Equation (3.2) is (3.1) and injectivity of \(d\mapsto Q_d\). Distributing
\(C_r\) fillings among the \(M_c\) available images proves (3.4), and
balanced assignment attains it. The total capacity of \(M_c\) bins at
cap \(b\) is \(bM_c\), proving (3.5). \(\square\)

The optimizing hash in Theorem 3.1 may depend on \(c\). The following
condition makes one hash work for every context.

### Corollary 3.2 (simultaneous regular-action balance)

Suppose a finite group \(G\) acts regularly on \(\mathcal C\), the code
alphabet contains \(G\), and

\[
                         \rho_g(c)=g\cdot c.            \tag{3.6}
\]

There is one hash \(h:\mathcal D_r\to G\) such that simultaneously for
all \(c,d\),

\[
 |\{u:\rho_{h(u)}c=d\}|
          \le\left\lceil {C_r\over |G|}\right\rceil.    \tag{3.7}
\]

If \(|G|\ge C_r\), every map \(u\mapsto\rho_{h(u)}c\) can be made
injective simultaneously for all \(c\).

#### Proof

Partition \(\mathcal D_r\) among the elements of \(G\) with class sizes
differing by at most one, and let \(h\) record the class. For fixed
\(c,d\), regularity gives a unique \(g\) with \(g\cdot c=d\), so the left
side of (3.7) is \(|h^{-1}(g)|\). If \(|G|\ge C_r\), take \(h\)
injective. \(\square\)

If each occurrence is also granted one of \(p\) ambient cyclic
translates, its range has size at most \(pM_c\). At cap \(p\), the same
capacity argument gives the raw lower bound

\[
                         (C_r-p^2M_c)_+.               \tag{3.8}
\]

If a router atlas supplies the regular action of \((C_2)^k\), then the
exact one-context cap-\(p\) coding threshold is

\[
 k\ge
 \left\lceil\log_2\left\lceil{C_r\over p}\right\rceil\right\rceil.
                                                               \tag{3.9}
\]

Perfect simultaneous injection requires

\[
 k\ge\lceil\log_2 C_r\rceil
    =2r-\tfrac32\log_2 r+O(1).                         \tag{3.10}
\]

For a regular \((C_3)^k\)-action, replace base \(2\) by base \(3\).
These are coding requirements, not router-supply claims.

## 4. Alternating-cycle realization

View an exterior rooted factor as a path cover of its middle-levels
inclusion graph. Toggling an alternating circuit changes incidence edges
but preserves every physical lower and upper vertex. A clean coherent
\(C_6\) permutes three strand tails by a \(3\)-cycle; a clean coherent
\(C_8\) gives a \(4\)-cycle; an admissible folded \(C_6\) can give a
transposition.

### Proposition 4.1 (router-to-module lemma)

Fix an equal-distance central column with palette
\(\{Q_c:c\in\mathcal C\}\). Suppose that for every code
\(a\in\mathcal A\):

1. a switch-stable alternating-circuit word supported before the central
   column routes roots to the central palette by \(\rho_a\);
2. a switch-stable word supported after the central column routes central
   strands to the prescribed complementary endpoints by
   \(\rho_a^{-1}\); and
3. every toggled state is a root-to-complement path cover, with the same
   root-to-central and central-to-sink lengths as the baseline.

Then these path covers form a split braid module.

#### Proof

Every circuit toggle preserves all physical \(X/Y\) vertices in its
support. The two words lie on opposite sides, so each side's complete
physical ledger is code-independent. The prefix routing gives (1.7).
The suffix inverse makes the total logical strand permutation

\[
                         \rho_a^{-1}\rho_a=1.           \tag{4.1}
\]

Thus root \(c\) reaches the physically complementary endpoint
\(E\setminus R_c\). This does not return the central exterior subset to
the root subset; such physical backtracking would contradict
geodesicity. Switch-stability supplies actual paths, not merely a formal
permutation. Definition 1.1 follows. \(\square\)

A single router is insufficient because it leaves endpoint monodromy.
An abstract permutation word is also insufficient: both halves must be
literal, strand-admissible, equal-distance circuit words with their full
physical ledgers.

### Proposition 4.2 (central distance-graph obstruction)

For a split module at cut \(k\), define the bipartite graph

\[
 \mathcal H_k\subseteq\mathcal C_{\rm root}\times\mathcal C_{\rm centre},
 \qquad
 c\sim d\quad\Longleftrightarrow\quad d_J(R_c,Q_d)=k.   \tag{4.2}
\]

Every code permutation \(\rho_a\) is a perfect matching contained in
\(\mathcal H_k\). Consequently

\[
 M_c\le\deg_{\mathcal H_k}(c)
       \le \binom{s}{k}^{\!2}.                         \tag{4.3}
\]

If a regular group \(G\) is realized as in Corollary 3.2, the matchings
\(\{\rho_g:g\in G\}\) are pairwise edge-disjoint, and their union is a
\(|G|\)-regular bipartite subgraph of \(\mathcal H_k\). In particular,
the simultaneous cap-\(p\) construction requires

\[
             \binom{s}{k}^{\!2}\ge
             \left\lceil{C_r\over p}\right\rceil.       \tag{4.4}
\]

#### Proof

Each exterior row has \(s\) Johnson moves and joins complementary
\(s\)-sets, so it is geodesic. Its prefix of length \(k\) is geodesic.
Equations (1.3) and (1.7) therefore give

\[
                         d_J(R_c,Q_{\rho_a c})=k,
\]

which says that \(\rho_a\) is supported on \(\mathcal H_k\). It is a
perfect matching because \(\rho_a\) is a permutation. An \(s\)-set has
exactly \(\binom{s}{k}\binom{s}{k}\) other \(s\)-sets at Johnson distance
\(k\), proving (4.3), even before restriction to the central palette.

For a regular action, \(\rho_g(c)=\rho_{g'}(c)\) implies \(g=g'\).
Thus the perfect matchings are edge-disjoint and their union is regular.
Combine \(|G|\ge\lceil C_r/p\rceil\) with (4.3) to obtain (4.4).
\(\square\)

This is only a necessary state graph. A suitable regular subgraph does
not supply the required prefix and suffix token-disjoint path covers.
Those are the genuinely stronger router conditions in Proposition 4.1.

### Corollary 4.3 (the present ballot \(C_8\) bank does not compile)

The audited ballot-forced clean suffix-\(C_8\) certificates have rowwise
port displacements

\[
                              (1,1,1,2).                \tag{4.5}
\]

They cannot be one prefix or suffix word in Proposition 4.1: a common
central column requires the same root-to-central length \(k\) on every
strand, equivalently every selected edge must lie in the single distance
graph \(\mathcal H_k\). The four values in (4.5) do not have a common
\(k\).

This does not rule out a larger serial composition which pays additional
row-dependent collar moves and equalizes total lengths. It proves that
the existing \(C_8\) certificate bank is not already the split module
needed by Theorem 2.1.

## 5. Fixed-rank phase freeze

Let \(\mathcal L_0,\ldots,\mathcal L_r\) be pairwise disjoint families
of \(r\)-subsets of \(J\). In the application,

\[
                         \mathcal L_t
       =\{B_t(u):u\in\mathcal D_r\}                    \tag{5.1}
\]

are the Chung--Feller layers. Let \(O_c\subset E\) be distinct
equal-size sets. Consider

\[
 Z_t(c,u)=O_{\alpha_t(c,u)}
             \mathbin{\dot\cup}L_t(\beta_t(c,u)),       \tag{5.2}
\]

where \(L_t(v)\in\mathcal L_t\), and

\[
 F_t=(\alpha_t,\beta_t):
       \mathcal C\times\mathcal D_r
          \longrightarrow\mathcal C\times\mathcal D_r \tag{5.3}
\]

is bijective at every phase.

### Theorem 5.1 (phase-freeze obstruction)

If

\[
                         d_J(Z_t(c,u),Z_{t+1}(c,u))=1             \tag{5.4}
\]

for every \(c,u,t\), then

\[
                         \alpha_{t+1}(c,u)=\alpha_t(c,u)          \tag{5.5}
\]

pointwise. After root normalization \(F_0(c,u)=(c,u)\),

\[
                         \alpha_t(c,u)=c
             \qquad(0\le t\le r).                    \tag{5.6}
\]

No filling-dependent stationary exterior collar exists in this class.
This already follows from statewise adjacency; the upper ledger can only
add constraints.

#### Proof

Since \(E,J\) are disjoint and both block restrictions have fixed size,
Johnson distance is additive:

\[
\begin{aligned}
d_J(Z_t,Z_{t+1})
  ={}&d_J(O_{\alpha_t},O_{\alpha_{t+1}})\\
    &+d_J(L_t(\beta_t),L_{t+1}(\beta_{t+1})).          \tag{5.7}
\end{aligned}
\]

The two local states belong to disjoint layers and hence are unequal.
Their local distance is at least one. Equation (5.4) forces the exterior
term to be zero. Distinctness of the \(O_c\)'s gives (5.5), and induction
gives (5.6). \(\square\)

For a general Johnson edge \(Z=A\dot\cup B\) to
\(Z'=A'\dot\cup B'\) on \(E\dot\cup J\), exactly one alternative holds:

1. \(A=A'\), and \(B,B'\) differ by one internal \(J\)-swap;
2. \(B=B'\), and \(A,A'\) differ by one internal \(E\)-swap;
3. one coordinate moves from \(E\) to \(J\);
4. one coordinate moves from \(J\) to \(E\).

Thus exterior routing requires a step at which the local phase is
stationary, or a cross-block rank defect. A formal hash permutation cannot
hide this physical toll.

## 6. Exact proved/conditional boundary

The following are proved.

1. A split exterior braid module and any Dyck-word hash compose to one
   literal integral exact product-packet factor.
2. The complete \(X/Y\) ownership proof is the triangular Latin
   bijection (2.7), not a fractional averaging argument.
3. The swallowed target and all fibre/coding bounds
   (3.1)--(3.10) are exact.
4. A prefix router word followed by an inverse suffix word is a
   sufficient literal realization of a split module.
5. Every code action lies in the exact central distance graph (4.2), with
   the degree and regular-subgraph restrictions (4.3)--(4.4).
6. A phasewise fixed-rank MSW/Chung--Feller hash cannot move the exterior
   address.

The following remain unproved.

1. The canonical PBBS/MSW factor has a growing serial switch-stable
   \(C_6/C_8\) router atlas satisfying Proposition 4.1.
2. Such an atlas has a regular orbit of size at least \(C_r/p\), or
   \(C_r\), on positive-density aligned contexts.
3. These product packets port-close over all but \(o(W)\) middle owners.
4. Cross-packet physical targets have collision excess \(o(W)\).

Therefore the algebraic hash gate is solved: the exact cocycle is the
triangular shear together with inverse exterior holonomy. The remaining
constant-one gate is geometric and statewise: construct a positive-density
serial router atlas with a growing regular central-collar orbit.
