# Functional facet attachments are automatically regular, while top-row localization needs linearly many mixed-length moves

**Date:** 2026-08-06

**Method:** Boolean facet counting, Hall's theorem, and endpoint-chain
capacity; no computation, search, or solver

**Status:** two unconditional theorems at the clean integral frontier.
First, before literal age flags are imposed, every functional
head-to-owner attachment automatically has an exact owner-once root cycle
cover; no additional Hall hypothesis is needed. Second, any stationary
factor with the central optimal rank marginals must move a positive
proportion of the top two rows away from maximal suffix width. Hence a
bounded portal perturbation of the maximal-width top-row rotor cannot be
the desired mixed-length rounding. Literal flag compatibility,
named-target exactness, and one-component Euler fusion remain open.

## 1. The complete functional facet graph

Work in odd dimension

\[
                         n=2m+1.
\]

Let

\[
 {\cal Q}={[n]\choose m},
 \qquad
 {\cal O}={[n]\choose {m+1}},
 \qquad
 |{\cal Q}|=|{\cal O}|=:W.                         \tag{1.1}
\]

Fix any incidence bijection

\[
 \vartheta:{\cal Q}\longrightarrow{\cal O},
 \qquad q\subset\vartheta(q).                       \tag{1.2}
\]

Such a bijection exists because the middle inclusion graph is
\((m+1)\)-regular and bipartite.

Define the **complete functional facet graph**

\[
 {\cal H}_\vartheta=({\cal Q}^-,{\cal Q}^+;E_\vartheta)
                                                               \tag{1.3}
\]

by joining a tail root \(p\in{\cal Q}^-\) to a head root
\(q\in{\cal Q}^+\) exactly when

\[
                         p\ne q,
 \qquad                  p\subset\vartheta(q).       \tag{1.4}
\]

The edge \(pq\) is assigned the owner colour \(\vartheta(q)\). This is the
root/owner projection of the functional attachment model before one
retains only the turns compatible with a selected literal flag at each
root.

### Theorem 1.1 (automatic functional regularity)

For every incidence bijection \(\vartheta\), the graph
\({\cal H}_\vartheta\) is \(m\)-regular on both shores.

Consequently:

1. it decomposes into \(m\) edge-disjoint perfect matchings;
2. every one of those matchings is an owner-exact directed cycle cover of
   the middle roots; and
3. every edge of \({\cal H}_\vartheta\) belongs to some owner-exact cycle
   cover.

#### Proof

Fix a head \(q\). The owner \(\vartheta(q)\) has \(m+1\) rank-\(m\)
facets. One is \(q\), and the other \(m\) are precisely its neighbours on
the tail shore. Thus

\[
                         d_{{\cal H}_\vartheta}(q)=m.          \tag{1.5}
\]

Now fix a tail \(p\). There are \(m+1\) owners containing \(p\). Since
\(\vartheta\) is bijective, each has one distinct preimage \(q\). For the
owner \(\vartheta(p)\), that preimage is \(q=p\), which is excluded by
(1.4). Every other containing owner contributes one neighbour, and hence

\[
                         d_{{\cal H}_\vartheta}(p)=m.          \tag{1.6}
\]

This proves regularity. Every regular bipartite graph decomposes into
perfect matchings by repeated application of Hall's theorem. A perfect
matching uses every head \(q\) once, so its owner colours
\(\vartheta(q)\) are all distinct and exhaust \({\cal O}\). Identifying
the two copies of \({\cal Q}\), it also gives every root one predecessor
and one successor, hence a directed cycle cover. The factorization places
every edge in one of the perfect matchings. \(\square\)

This strengthens the unflagged part of the functional-attachment
criterion: **owner attachment itself never creates a Hall obstruction.**
All possible Hall failure comes from the literal rail/age restrictions
which delete edges from (1.3).

## 2. Sharp global edge-deletion resilience

### Theorem 2.1 (fewer than \(m\) forbidden functional incidences are harmless)

Let \(D\subseteq E_\vartheta\). If

\[
                         |D|<m,                              \tag{2.1}
\]

then \({\cal H}_\vartheta-D\) still has a perfect matching and therefore
an owner-exact root cycle cover.

The bound is sharp: deleting the \(m\) edges at one tail root destroys
every perfect matching.

#### Proof

Suppose \({\cal H}_\vartheta-D\) has no perfect matching. By Hall's
theorem there is a tail family \(X\) whose remaining neighbourhood \(Y\)
satisfies

\[
                         |Y|<|X|.                            \tag{2.2}
\]

Every old edge from \(X\) to the complement of \(Y\) belongs to \(D\).
Using \(m\)-regularity,

\[
 \begin{aligned}
 |D|
 &\ge e_{{\cal H}_\vartheta}(X,{\cal Q}^+\setminus Y)\\
 &=m|X|-e_{{\cal H}_\vartheta}(X,Y)\\
 &\ge m|X|-m|Y|
 \ge m,
 \end{aligned}                                             \tag{2.3}
\]

contrary to (2.1). Deleting all \(m\) edges incident with one tail
isolates it, proving sharpness. \(\square\)

### Corollary 2.2 (precise portal scope)

A bounded portal or guard bank which forbids fewer than \(m\) additional
incidences of an already functional complete core has zero owner/root
matching cost. A single prescribed functional atom can likewise be
included in an owner-exact cover by Theorem 1.1.

This does **not** say that an arbitrary fixed flag table is close to the
complete core. A literal order-\(d\) flag can delete almost all \(m\)
candidate predecessors at many roots, and the recursive-SCD dead-root
example does exactly that. Theorem 2.1 applies after a functional
flag-compatible core has been built; it cannot create that core.

## 3. Mixed-length notation

Return to the central parameters of the merged global chart:

\[
 n=2m+1,\qquad r=m,\qquad t=m-d,\qquad
 W={n\choose m}.                                             \tag{3.1}
\]

Let

\[
 q_s={{n\choose s}-b_s\over W}\qquad(1\le s<r)              \tag{3.2}
\]

be the optimal Ferrers-corrected rank demands. Consider any stationary
depth-\(d\) marked age circulation realizing these marginals. Write

\[
                         \lambda_{s,j}                        \tag{3.3}
\]

for the normalized mass of rank-\(s\) marks placed at suffix width \(j\).
Thus

\[
                         \sum_{j=1}^d\lambda_{s,j}=q_s.       \tag{3.4}
\]

Put

\[
 H_>:=\sum_{s=t+1}^{r-1}q_s,                                \tag{3.5}
\]

and let

\[
 L_{\max}:=(q_t-\lambda_{t,d})
          +(q_{t-1}-\lambda_{t-1,d})                         \tag{3.6}
\]

be the total top-two-row mass moved away from maximal width.

## 4. Quantitative endpoint escape

### Theorem 4.1 (linear mixed-length necessity)

Every stationary marked age circulation realizing (3.2) satisfies

\[
 \boxed{
 \lambda_{t,d}+\lambda_{t-1,d}
 \le 1-\frac{H_>}{d}
 }                                                          \tag{4.1}
\]

and therefore

\[
 \boxed{
 L_{\max}
 \ge q_t+q_{t-1}-1+\frac{H_>}{d}.
 }                                                          \tag{4.2}
\]

Since \(q_s\) is nondecreasing,

\[
 L_{\max}
 \ge q_{t-1}+\left(2-\frac1d\right)q_t-1.                   \tag{4.3}
\]

In the eventual central regime,

\[
 \boxed{
 L_{\max}
 \ge 3e^{-\pi/4}-1-o(1)>0.36.
 }                                                          \tag{4.4}
\]

Thus every one-copy realization on \(W\) owner roles must place
\(\Omega(W)\) of the rank-\(t,t-1\) named occurrences at widths smaller
than \(d\).

#### Proof

At an age type \(c=(c_0,\ldots,c_d)\), the proper suffix ranks are strictly
increasing with width. A rank-\(t\) mark at width \(d\) forces

\[
                         c_d=r-t=d,                           \tag{4.5}
\]

while a rank-\((t-1)\) mark at width \(d\) forces

\[
                         c_d=d+1.                             \tag{4.6}
\]

These are disjoint terminal events. On either event the largest proper
suffix rank is at most \(t\), so the endpoint carries no mark of rank
greater than \(t\).

Because mark mass at one address is at most the stationary mass of its
type, the stationary mass of endpoints unavailable to the higher rows is
at least

\[
                         \lambda_{t,d}+\lambda_{t-1,d}.       \tag{4.7}
\]

Every remaining endpoint has only \(d\) proper suffix addresses.
Consequently

\[
 H_>
 \le d\bigl(1-\lambda_{t,d}-\lambda_{t-1,d}\bigr),          \tag{4.8}
\]

which is (4.1). Subtracting (4.1) from
\(q_t+q_{t-1}\) gives (4.2).

There are \(d-1\) ranks strictly between \(t\) and \(r\), and
monotonicity gives

\[
                         H_>\ge(d-1)q_t.                     \tag{4.9}
\]

This proves (4.3). Finally

\[
                         q_t,q_{t-1}\longrightarrow
                         e^{-\pi/4},
 \qquad d\longrightarrow\infty,                             \tag{4.10}
\]

so the right side of (4.3) tends to
\(3e^{-\pi/4}-1\), approximately \(0.3678\). This proves
(4.4). \(\square\)

### Corollary 4.2 (bounded portals cannot repair the maximal-width rotor)

Start from any fractional or integral architecture in which all
rank-\(t,t-1\) marks lie at width \(d\). Any modification which changes
only \(o(W)\) marked role occurrences still violates Theorem 4.1 for all
sufficiently large parameters.

In particular, a bounded or polynomial-size portal bank cannot turn the
maximal-two-row rotor into the desired one-copy mixed-length factor. The
base architecture itself must already contain a linear-density
mixed-length population, as the audited monotone/pull-clock circulation
does.

#### Proof

The initial architecture has \(L_{\max}=0\). Changing \(o(W)\) physical
marked occurrences changes normalized \(L_{\max}\) by \(o(1)\), while
Theorem 4.1 requires it to exceed a fixed positive constant. \(\square\)

## 5. Exact clean integral frontier

The two theorems eliminate opposite false obstructions.

1. **Owner/root Hall is automatic before flags.** Any incidence bijection
   \(\vartheta\) gives an exact one-owner-once root cycle cover. A bounded
   number of later forbidden functional incidences is harmless.
2. **Mixed lengths are globally load-bearing.** No bounded portal
   correction of the maximal-width top-row clock can work. One must begin
   with a genuinely mixed-length exact flag population.

Therefore the remaining common rounding theorem can be stated without an
extra unflagged owner-Hall row:

> Jointly choose a mixed-length exact named-target flag table and an
> incidence bijection \(\vartheta\) so that the literal flag-compatible
> subgraph of \({\cal H}_\vartheta\) has a perfect matching. Then
> bipartite integrality supplies the one-owner-once cycle cover.

The unresolved correlation is entirely in the phrase
**literal flag-compatible**. Neither the symmetric pull-clock histogram
nor a static SCD selector supplies it. One-component Euler fusion,
residence, PBBS retention, and upper guards remain later rows.

## 6. Scope

This note proves no common integral flag table and no universal word.
Specifically, it does not prove:

* rail balance for a selected exact target table;
* statewise Hall after literal age restrictions;
* connectedness of the resulting cycle cover;
* PBBS whole-fan compatibility, residence, or upper coverage; or
* \(\nu(k)\le B(k)+O(1)\).

Its exact gain is the removal of the unflagged functional Hall concern and
the proof that the surviving integral construction must be mixed-length on
a linear fraction of roles.
