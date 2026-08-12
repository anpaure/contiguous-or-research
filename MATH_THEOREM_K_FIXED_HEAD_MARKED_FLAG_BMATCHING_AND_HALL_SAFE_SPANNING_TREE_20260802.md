# Fixed-head marked flags: capacitated matching and a Hall-safe spanning tree

**Date:** 2026-08-02  
**Status:** unconditional exact reduction. It starts after a static
one-copy owner-labelled marked flag table has been chosen. On that face,
literal balance is an integral bipartite \(b\)-matching, and connected
rooted serialization is equivalent to one spanning-tree skeleton followed
by a residual capacitated Hall matching. The theorem does not construct
the required static table from the stationary pull clock.

## 0. Outcome

The corrected pull-clock theorem gives a stationary rational circulation,
but averages over owners, literal flags, and marked occurrences. Suppose
instead that one has already chosen one literal depth-\(d\) suffix word at
each owner and marked its proper suffixes so that every residual named lower
target is used exactly once.

The suffix word fixes the head of the corresponding de Bruijn trace. The
only local freedom needed to make its full owner is the leading source
letter. Consequently the balance problem has only two shores:

* owner-labelled flag occurrences; and
* literal tail states, with demand equal to their fixed head multiplicity.

It is therefore ordinary capacitated Hall and is integral. Connectedness
is exactly one additional graphic row. More precisely, a connected
selection exists if and only if one can reserve distinct labelled options
whose projected state edges contain a spanning tree and the remaining
roles still satisfy capacitated Hall after the reserved tail capacities are
subtracted.

This gives a single exact all-\(k\) target:

> choose the static owner/target-exact flag table and a protected
> Hall-safe spanning-tree skeleton simultaneously.

That statement is necessary and sufficient for the lower labelled rooted
Euler row. Residence, upper interval decks, and common-cap/compiler guards
which depend on the leading source letter remain separate unless they are
included in the option menus.

## 1. A static owner-labelled marked flag table

Let

\[
                    {\cal A}=2^{[k]}\setminus\{\varnothing\}
\]

and let \(D_d({\cal A})\) be the order-\(d\) de Bruijn digraph. Let \(I\)
be a set of \(W=\binom{k}{r}\) occurrence labels. A **static marked flag
table** consists, for every \(i\in I\), of

1. a distinct rank-\(r\) owner \(T_i\), so the \(T_i\) run through all
   rank-\(r\) sets;
2. nonempty source letters
   \(A_{i,1},\ldots,A_{i,d}\subseteq T_i\); and
3. a set of marked proper suffix occurrences of this word,

such that the marked suffix unions over all \(i\) are exactly the declared
residual named lower-target bank, with multiplicity one.

Put

\[
 U_i=\bigcup_{t=1}^d A_{i,t},\qquad
 h_i=(A_{i,1},\ldots,A_{i,d}).                         \tag{1.1}
\]

The allowed leading letters for role \(i\) are

\[
 {\cal B}_i=\{B:\varnothing\ne B\subseteq T_i,\
                       T_i\setminus U_i\subseteq B\}.       \tag{1.2}
\]

For \(B\in{\cal B}_i\), define the literal trace option

\[
 e(i,B)=(B,A_{i,1},\ldots,A_{i,d}),                    \tag{1.3}
\]

with tail and head

\[
 \ell(i,B)=(B,A_{i,1},\ldots,A_{i,d-1}),\qquad h_i.    \tag{1.4}
\]

Equation (1.2) is exactly the owner condition:

\[
                       B\cup U_i=T_i.                  \tag{1.5}
\]

Changing \(B\) changes no proper suffix of (1.3), so it preserves every
marked named target in the static table.

Extra protected conditions depending on \(B\) may be imposed simply by
deleting the corresponding options from \({\cal B}_i\). This convention is
required for upper, exterior, residence, or compiler guards which are not
already fixed by the suffix word.

## 2. Exact capacitated Hall theorem

For a de Bruijn state \(v\in{\cal A}^d\), put

\[
                         a(v)=|\{i:h_i=v\}|,            \tag{2.1}
\]

and let

\[
                         V_F=\{v:a(v)>0\}.              \tag{2.2}
\]

Form the bipartite graph

\[
                         \Gamma_F=(I,V_F;E_F)           \tag{2.3}
\]

by putting \(iv\in E_F\) exactly when \(v=\ell(i,B)\) for an
admissible \(B\in{\cal B}_i\). Tail states outside \(V_F\) are omitted:
their required balanced tail demand is zero.

### Theorem 2.1 (fixed-head balance is capacitated Hall)

The static table has a balanced one-copy literal trace selection if and
only if

\[
       |X|\le \sum_{v\in N_{\Gamma_F}(X)}a(v)
                       \qquad\text{for every }X\subseteq I.   \tag{2.4}
\]

Whenever (2.4) holds, a balanced selection is obtained by integral max
flow. It uses every owner once and every marked residual target once.

#### Proof

Select one option \(e(i,B_i)\) for every role. Its head is fixed at
\(h_i\). Hence the selected indegree of state \(v\) is always \(a(v)\),
while its selected outdegree is the number of roles whose chosen tail is
\(v\). Balance is therefore exactly the requirement that the roles be
assigned to tail states with demand \(a(v)\).

The total demand is

\[
                         \sum_v a(v)=|I|.               \tag{2.5}
\]

The capacitated marriage theorem gives (2.4) as the necessary and
sufficient condition, and the bipartite incidence matrix is totally
unimodular. Equations (1.2)--(1.5) preserve each role's owner and every
marked suffix payload. \(\square\)

Thus, after fixing a common owner/target-exact table, no further
fractional-to-integral gap remains in the balance row. The nonintegral
correlation lies in choosing that table, or in the connectivity row below.

## 3. Hall-safe spanning-tree criterion

An option \(iv\in E_F\) projects to the directed state edge

\[
                              v\longrightarrow h_i.     \tag{3.1}
\]

For \(R\subseteq E_F\), let \(I(R)\) be its used role set and put

\[
                         b_R(v)=|\{iv\in R\}|.          \tag{3.2}
\]

Call \(R\) a **Hall-safe spanning-tree skeleton** when:

1. the options in \(R\) use distinct roles;
2. \(b_R(v)\le a(v)\) for every \(v\in V_F\);
3. after loops are discarded, the undirected projections of (3.1) contain
   a spanning tree of \(V_F\); and
4. in the residual graph obtained by deleting \(I(R)\), every
   \(X\subseteq I\setminus I(R)\) satisfies

   \[
   |X|\le
      \sum_{v\in N_{\rm res}(X)}\bigl(a(v)-b_R(v)\bigr).      \tag{3.3}
   \]

The right side of (3.3) consists of exact residual demands, not merely
upper capacities.

### Theorem 3.1 (rooted trace-tree equivalence)

There is a weakly connected balanced one-copy trace selection for the
static table if and only if a Hall-safe spanning-tree skeleton exists.
Such a selection is one Euler component and therefore spells a cyclic
word with no sidecar. It may be rooted at any selected protected trace
option.

#### Proof

Suppose first that \(R\) exists. Equation (3.3) and integral capacitated
Hall select one option for every residual role with exact tail demands
\(a-b_R\). Together with \(R\), every role is used once and every state
has tail multiplicity \(a(v)\). The selected directed multigraph is
balanced by Theorem 2.1. It contains the spanning tree from condition 3,
so its support is weakly connected. A finite weakly connected balanced
digraph has an Euler circuit.

Conversely, take a connected balanced selection. Choose any spanning tree
of its underlying state multigraph and let \(R\) be the selected labelled
options furnishing the tree edges. They use distinct roles, satisfy
\(b_R\le a\), and their removal leaves the remaining selected options as an
exact matching of the residual roles to demands \(a-b_R\). That matching
witnesses (3.3). \(\square\)

For \(|V_F|=1\), the empty skeleton is the spanning tree and Theorem 3.1
reduces to Theorem 2.1. Loops may occur in the residual matching but cannot
serve as tree edges. Parallel occurrence-labelled roles cause no problem.

If a particular option \(e_0\) is prescribed, delete its role first,
decrease the demand of its tail by one, and require the skeleton together
with the projected edge of \(e_0\) to span \(V_F\). The resulting Euler
circuit contains \(e_0\) and can be cyclically rotated to start there.

## 4. Label-transparent cycle exchanges

Let \(M\) be a balanced selection. Suppose it contains options

\[
                         iv,\qquad jw                  \tag{4.1}
\]

whose directed edges lie in two different weak components. If the crossed
options

\[
                         iw,\qquad jv                  \tag{4.2}
\]

also belong to \(E_F\), replace (4.1) by (4.2).

### Proposition 4.1 (transparent rectangle fusion)

The exchange (4.1)--(4.2) preserves every owner, every marked named target,
and every state degree, and it merges the two old Euler components.

#### Proof

The roles \(i,j\) and the tail-state multiset \(\{v,w\}\) are unchanged, so
all labelled rows and all state degrees are unchanged. Every edge of a
balanced weak component lies on an undirected cycle and is therefore not a
bridge. Removing the two old edges leaves both old components weakly
connected. Each crossed edge joins the two old vertex sets, so the new
support is their union in one component. \(\square\)

Longer alternating cycles give the same conclusion when they use exactly
one selected edge from each of several distinct components and cyclically
permute their tail states. A port-disjoint tree of such rectangles is a
constructive sufficient certificate for the skeleton in Theorem 3.1.

## 5. The full-depth rigid specialization

If all \(d\) proper suffixes of every role are marked and are globally
distinct, then the fixed heads \(h_i\) are distinct. Thus \(a(v)=1\) on
\(W\) states and Theorem 2.1 becomes an ordinary perfect matching.

Writing the strict chain as

\[
 \varnothing=S_{i,0}\subsetneq S_{i,1}\subsetneq\cdots
    \subsetneq S_{i,d}\subsetneq T_i,                       \tag{5.1}
\]

put

\[
 A_{i,d-j+1}=S_{i,j}\setminus S_{i,j-1}.                    \tag{5.2}
\]

The exact predecessor digraph on chain indices has an arc \(j\to i\) if
and only if

\[
\begin{aligned}
 (A_{j,2},\ldots,A_{j,d})
      &=(A_{i,1},\ldots,A_{i,d-1}),\\
 T_i\setminus S_{i,d}
      &\subseteq A_{j,1}\subseteq T_i.                       \tag{5.3}
\end{aligned}
\]

Theorem 2.1 says exactly that this digraph has a cycle cover; Theorem 3.1
says exactly that it has a Hamilton cycle. Proposition 4.1 is the usual
directed two-cycle merge rectangle, now with every owner and every chain
target retained literally.

## 6. Rebase on the stationary pull clock

The corrected stationary pull-clock theorem proves a rational point before
the static table is chosen. It does not imply the hypotheses above:

* the marked-age semigroup has an explicit saturated hole;
* the canonical \(k=10\) pull-block histogram has a denominator incompatible
  with a \(W\)-position one-copy schedule; and
* symmetric averaging may use several literal states over one owner and no
  state over another.

Conversely, once a static owner/target-exact table is produced, Theorem 2.1
shows that the remaining balance row is ordinary integral flow. Theorem
3.1 identifies the only additional lower-topology row as a Hall-safe
graphic skeleton.

Accordingly the minimal exact all-\(k\) statement left by this reduction is:

> **Triangular rooted spine-tree lemma.** For the canonical residual
> Ferrers target bank, choose a static one-copy owner-labelled marked flag
> table, one protected root option, and a Hall-safe spanning-tree skeleton
> in its literal leading-letter graph.

This one lemma is necessary and sufficient for one trace per owner, one
occurrence per residual named lower target, and one rooted zero-sidecar
Euler chronology. A bounded-component statement is weaker: generic
order-\(d\) endpoint resets cost \(d\), so \(O(1)\) components alone give
only \(O(d)\), not \(O(1)\), sidecar.

The theorem makes no claim about upper interval-union coverage, residence
across an exterior opening, or terminal common-cap feasibility. Those rows
must either be encoded in the option menus before applying Hall or proved
afterward by a separate transparent-transport theorem.

