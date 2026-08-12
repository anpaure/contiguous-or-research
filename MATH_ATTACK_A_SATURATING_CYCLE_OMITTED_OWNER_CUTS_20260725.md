# Saturating-cycle omitted owners: exact all-depth shadow slack and the first residual cut

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, or solver is
used.

## 0. Result

Put

\[
 n=2m+1,\qquad V_q=\binom{[n]}{m-q},\qquad
 N_q=|V_q|,\qquad W=N_0.
\]

Let

\[
 S_0,X_0,S_1,X_1,\ldots,S_{N_1-1},X_{N_1-1},S_0
 \tag{0.1}
\]

be the saturating cycle of Section 22 of
`TRANSLATION_PACKET_MULTIDEPTH_RAINBOW_LEMMA_20260725.md`.  Thus all
\(S_i\in V_1\) occur, the \(X_i\in V_0\) are distinct, and

\[
 S_i\subset X_i\supset S_{i+1}.
\]

Write

\[
 U=\{X_i:i\in\mathbb Z_{N_1}\},\qquad
 E=V_0\setminus U,
 \qquad |E|=W-N_1=\frac{2W}{m+2}.                 \tag{0.2}
\]

If this one set could be released at transition one and retained through
\(K=\lceil A\sqrt m\rceil\), its monotone tail cost would already be

\[
 \sum_{q=1}^K\frac{|E|}{c_q}
 \le K|E|
 =\frac{2K}{m+2}W
 =O_A(W/\sqrt m)=o_A(W),                          \tag{0.2a}
\]

because \(c_q\ge1\) on the fixed window.  Thus checking the exact cuts for
this particular \(E\) would indeed close \(\mathrm{MR}_A\), with room to
spare; no stronger cardinality estimate is needed.

Three exact conclusions hold.

1.  The omitted owners solve the complete depth-one residual problem.  They
    have a matching to distinct facets, so after orienting the cycle the
    frozen owners use every member of \(V_1\) once and the omitted owners
    occupy precisely the upper-quota fibres.  Thus every exact survival and
    crossing cut at \(q=1\) holds.

2.  The omitted family has a uniform all-depth shadow bound.  For every
    \(\mathcal A\subseteq E\), every \(1\le q\le m\), and
    \(\partial_q\mathcal A=\{T\in V_q:T\subset X\text{ for some }
    X\in\mathcal A\}\),

    \[
     \boxed{
     |\partial_q\mathcal A|
       \ge \frac{N_q}{N_1}|\mathcal A|.}          \tag{0.3}
    \]

    If \(\lambda_q=W/N_q\) and
    \(\bar c_q=\lceil\lambda_q\rceil\), then all floor effects remain
    exact and

    \[
     \boxed{
     \bar c_q|\partial_q\mathcal A|-|\mathcal A|
       \ge \frac{2}{m}|\mathcal A|.}              \tag{0.4}
    \]

    In particular, the integer slack is at least
    \(\lceil2|\mathcal A|/m\rceil\) for nonempty \(\mathcal A\).
    Moreover all owners of \(E\) admit one common integral nested flow whose
    rank-\(q\) load is at most

    \[
      \left\lceil\frac{N_1}{N_q}\right\rceil,     \tag{0.5}
    \]

    and whose rank-one load is at most one.

3.  This positive slack is not yet the residual cyclic-alignment cut.  The
    latter uses the capacities left after the \(U\)-owners are frozen,
    namely \(b_q-g_q\), rather than the standalone ceiling \(\bar c_q\).
    The first uncontrolled condition is visible already at \(q=2\).  The
    projected lower Hamilton cycle has intersection multiplicities

    \[
      d(T)=|\{i:S_i\cap S_{i+1}=T\}|,
      \qquad T\in V_2.                            \tag{0.6}
    \]

    For \(m\ge8\), \(c_2=1\).  Any two-level frozen continuation exposed by
    (0.1) must satisfy

    \[
      \boxed{d(T)\le2\quad(T\in V_2)}             \tag{0.7}
    \]

    before any crossing matching is possible.  Given rank-one and rank-two
    high sets \(H_1,H_2\), its exact family cut is

    \[
      \boxed{
      \sum_{T\in\mathcal B}
        \bigl(1+\mathbf1_{H_2}(T)-d(T)\bigr)
      \le |H_1\cap N_2(\mathcal B)|
      \qquad(\mathcal B\subseteq V_2).}           \tag{0.8}
    \]

    In particular, if \(d(T)=0\), then the singleton cut requires an omitted
    owner containing \(T\).  Section 22 controls neither (0.7) nor (0.8).
    Thus its \(O(W/m)\) omitted owners have ample intrinsic all-depth
    capacity, but the stated saturating-cycle theorem alone does not prove
    that they form an \(\mathrm{MR}_A\) release set.

No actual failure of (0.7) is asserted: the exact conclusion is that (0.7)
and then (0.8) are the first properties not supplied by the theorem.

## 1. The exact facet cap

For \(S\in V_1\), let

\[
 e(S)=|\{X\in E:S\subset X\}|,
 \qquad
 u(S)=|\{X\in U:S\subset X\}|.
\]

### Lemma 1.1

For every \(S\in V_1\),

\[
 \boxed{e(S)\le m.}                               \tag{1.1}
\]

#### Proof

Every \((m-1)\)-set has exactly \(m+2\) middle supersets.  In (0.1), the
vertex \(S_i\) is incident with the two distinct middle vertices
\(X_{i-1}\) and \(X_i\), both of which belong to \(U\).  Therefore
\(u(S_i)\ge2\), and

\[
 e(S_i)=m+2-u(S_i)\le m.
\]

All members of \(V_1\) occur among the \(S_i\), proving the assertion.
\(\square\)

The average in (1.1) is exactly two:

\[
 \frac1{N_1}\sum_{S\in V_1}e(S)
 =\frac{m|E|}{N_1}=2.                             \tag{1.2}
\]

The upper bound, rather than the average, is what gives Hall.

## 2. Exact depth-one completion

For \(\mathcal A\subseteq E\), let

\[
 \partial_1\mathcal A
 =\{S\in V_1:S\subset X\text{ for some }X\in\mathcal A\},
\]

and put \(d_{\mathcal A}(S)=|\{X\in\mathcal A:S\subset X\}|\).

### Theorem 2.1

For every \(\mathcal A\subseteq E\),

\[
 |\partial_1\mathcal A|\ge|\mathcal A|.          \tag{2.1}
\]

More precisely,

\[
 \boxed{
 m\bigl(|\partial_1\mathcal A|-|\mathcal A|\bigr)
 =\sum_{S\in\partial_1\mathcal A}
   \left(u(S)-2+d_{E\setminus\mathcal A}(S)\right).}            \tag{2.2}
\]

#### Proof

Count the incidences between \(\mathcal A\) and its facets:

\[
 m|\mathcal A|=\sum_{S\in\partial_1\mathcal A}d_{\mathcal A}(S).
\]

Since

\[
 m+2=u(S)+d_{\mathcal A}(S)+d_{E\setminus\mathcal A}(S),
\]

subtraction from \(m|\partial_1\mathcal A|\) gives (2.2).  Both summands
on its right are nonnegative by Lemma 1.1, proving (2.1).  \(\square\)

Hall's theorem now gives an injection

\[
 \phi:E\longrightarrow V_1,
 \qquad \phi(X)\subset X.                         \tag{2.3}
\]

Let \(H_1=\phi(E)\), so \(|H_1|=|E|=W-N_1=\rho_1\).  Orient (0.1) so
that the frozen owner \(X_i\) uses \(S_i\); these frozen owners then
have load one on every member of \(V_1\).  Send each \(X\in E\) to
\(\phi(X)\).  The resulting load is

\[
 b_1(S)=1+\mathbf1_{H_1}(S),                      \tag{2.4}
\]

which is the exact balanced rank-one vector, since \(c_1=1\) and
\(|H_1|=\rho_1\).  This is an integral residual completion, so by the
necessity direction of the monotone-release theorem it satisfies every
survival and directed crossing cut at transition one.  Thus the
saturating cycle completely closes \(q=1\), not merely its marginal count.

## 3. All-depth omitted-root expansion

For \(T\in V_q\), define

\[
 d_{\mathcal A,q}(T)=|\{X\in\mathcal A:T\subset X\}|.
\]

### Theorem 3.1 — pointwise descendant cap

For every \(\mathcal A\subseteq E\), every \(1\le q\le m\), and every
\(T\in V_q\),

\[
 \boxed{
 d_{\mathcal A,q}(T)
 \le \frac mq\binom{m+q+1}{q-1}
 =\frac{N_1}{N_q}\binom mq.}                     \tag{3.1}
\]

#### Proof

Count pairs \((X,S)\) satisfying

\[
 X\in\mathcal A,qquad T\subset S\subset X,
 \qquad |S|=m-1.
\]

Every \(X\supset T\) contributes exactly \(q\) such facets \(S\), while
there are \(\binom{m+q+1}{q-1}\) possible facets \(S\supset T\).  By
Lemma 1.1 each of the latter is contained in at most \(m\) members of
\(\mathcal A\).  Therefore

\[
 qd_{\mathcal A,q}(T)
 \le m\binom{m+q+1}{q-1}.                         \tag{3.2}
\]

The identity in (3.1) follows from

\[
 \frac{\frac mq\binom{m+q+1}{q-1}}{\binom mq}
 =\frac{m(m-q)!(m+q+1)!}{m!(m+2)!}
 =\frac{N_1}{N_q}.                                \tag{3.3}
\]

This proves the theorem.  \(\square\)

### Corollary 3.2 — exact root-shadow slack

For every \(\mathcal A\subseteq E\), (0.3) and (0.4) hold.

#### Proof

Count all pairs \((X,T)\) with \(X\in\mathcal A\), \(T\in V_q\), and
\(T\subset X\).  Theorem 3.1 gives

\[
 \binom mq|\mathcal A|
 =\sum_{T\in\partial_q\mathcal A}d_{\mathcal A,q}(T)
 \le \frac{N_1}{N_q}\binom mq
       |\partial_q\mathcal A|,
\]

which is (0.3).

Put \(\alpha_q=N_1/N_q\).  Since

\[
 \alpha_q=\frac{m}{m+2}\lambda_q,
 \qquad \bar c_q\ge\lambda_q,                   \tag{3.4}
\]

(0.3) gives

\[
 \begin{aligned}
 \bar c_q|\partial_q\mathcal A|-|\mathcal A|
 &\ge\left(\frac{\bar c_q}{\alpha_q}-1\right)
       |\mathcal A|\\
 &\ge\left(\frac{m+2}{m}-1\right)|\mathcal A|
 =\frac2m|\mathcal A|.
 \end{aligned}
\]

This retains the exact ceiling, including the case \(\lambda_q\in\mathbb
Z\).  The left side is integral, giving the stated integer refinement.
\(\square\)

### Corollary 3.3 — one common integral omitted-owner flow

There is one integral family of nested paths, one from every root in \(E\),
whose rank-one loads are at most one and whose rank-\(q\) loads are at most
\(\lceil N_1/N_q\rceil\) for every \(q\).

#### Proof

For each \(X\in E\), fractionally average over all deletion orders of the
elements of \(X\).  At rank \(q\), a fixed descendant \(T\subset X\)
receives \(1/\binom mq\) from \(X\).  Hence the load at \(T\) is

\[
 \frac{d_{E,q}(T)}{\binom mq}\le\frac{N_1}{N_q}   \tag{3.5}
\]

by Theorem 3.1.  At rank one the sharper bound is one.

This is a feasible fractional flow in the layered Boolean inclusion network
with unit integral root supplies and integral node capacities one at rank
one and \(\lceil N_1/N_q\rceil\) at rank \(q\).  Split every node into an
in-node and an out-node joined by its capacity arc.  The resulting network
has integral capacities, so flow integrality gives an integral flow of the
same value.  Decomposing it into unit paths gives the claimed common nested
family.  \(\square\)

This is stronger than separate rankwise matchings.  Nevertheless, it uses
the full standalone capacities.  In an \(\mathrm{MR}_A\) completion the
available capacity is instead \(b_q-g_q\), where \(g_q\) is the load of the
frozen cycle owners.  The exact residual crossing inequality is

\[
 (b_q-g_q)(\mathcal B)
 \le (b_{q-1}-g_{q-1})(N_q(\mathcal B))
 \qquad(\mathcal B\subseteq V_q).                 \tag{3.6}
\]

No inequality above bounds either side of this signed residual comparison:
(0.3) concerns all descendants reachable from a root subfamily of \(E\),
whereas (3.6) concerns the particular residual parent copies left after the
frozen owner edges have been retained.

## 4. The first exact residual cut is at rank two

Project (0.1) to the Hamilton Johnson cycle

\[
 S_0S_1\cdots S_{N_1-1}S_0
\]

on \(V_1\), and define \(d(T)\) by (0.6).  The natural two-level oriented
flag exposed by the alternating cycle (and the one obtained from this
indexing when the cycle is tight) is

\[
 X_i\supset S_i\supset S_{i-1}\cap S_i.           \tag{4.1}
\]

Thus its frozen loads are

\[
 g_1(S)=1,
 \qquad g_2(T)=d(T).                              \tag{4.2}
\]

For \(m\ge8\),

\[
 1<\lambda_2
 =\frac{(m+2)(m+3)}{m(m-1)}<2,                  \tag{4.3}
\]

so every balanced rank-two load is

\[
 b_2(T)=1+\mathbf1_{H_2}(T).                     \tag{4.4}
\]

Let \(H_1\) be the image of a depth-one matching from Section 2.  The
residual loads at the two adjacent ranks are exactly

\[
 r_1(S)=\mathbf1_{H_1}(S),
 \qquad
 r_2(T)=1+\mathbf1_{H_2}(T)-d(T).                \tag{4.5}
\]

### Proposition 4.1 — exact rank-two test

The survival system at rank two is equivalent to

\[
 d(T)\le1+\mathbf1_{H_2}(T)\quad(T\in V_2).      \tag{4.6}
\]

Conditional on survival, the exact directed crossing system is (0.8).

#### Proof

Survival is simply \(r_2(T)\ge0\), which gives (4.6).  The active parent
copies occur exactly once at every member of \(H_1\).  For a child family
\(\mathcal B\subseteq V_2\), their neighborhood therefore has size
\(|H_1\cap N_2(\mathcal B)|\), while the required child multiplicity is
\(r_2(\mathcal B)\).  Hall's theorem is precisely (0.8).  \(\square\)

Several immediate consequences make the boundary exact.

* If \(d(T)\ge3\), the singleton survival cut fails for every balanced
  choice of \(H_2\).
* If \(d(T)=0\), the singleton crossing cut requires

  \[
    1+\mathbf1_{H_2}(T)
    \le |H_1\cap N_2(T)|.                         \tag{4.7}
  \]

  Because each member of \(H_1\) is matched from a distinct omitted owner
  containing it,

  \[
    |H_1\cap N_2(T)|
    \le |\{X\in E:T\subset X\}|.                 \tag{4.8}
  \]

  Hence a missed rank-two colour with no omitted middle superset is an exact
  singleton crossing failure.
* Let \(z=|\{T:d(T)=0\}|\).  Since \(\sum_Td(T)=N_1\), there is a balanced
  vector dominating \(d\) only if

  \[
    \max_Td(T)\le2,
    \qquad z\le |E|.                              \tag{4.9}
  \]

  Conversely, (4.9) is sufficient for the existence of a rank-two balanced
  vector which dominates \(d\): every double colour is made high, and the
  remaining required number of high positions is filled among the zero and
  single colours.  Indeed, if \(n_j=|\{T:d(T)=j\}|\), then

  \[
    n_2-n_0=N_1-N_2,
    \qquad
    \rho_2-n_2=(W-N_2)-n_2=|E|-n_0.              \tag{4.10}
  \]

  The family inequalities (0.8), not merely (4.9), are still required.

The saturating-cycle statement in Section 22 says that all union labels
\(X_i\) are distinct and all vertices \(S_i\) occur.  It gives no bound on
the multiplicities \(d(T)\), no upper bound on \(z\), and no comparison of
the residual demand in (0.8) with the selected parent set \(H_1\).
Therefore (0.7)--(0.8) are the first exact uncontrolled cuts.  They are not
contradictions: a specially chosen saturating cycle could satisfy them.

## 5. Precise proved/conditional boundary

Unconditionally, the omitted set \(E\) has:

* an exact depth-one balanced completion;
* the all-depth descendant bound (3.1);
* the uniform root-shadow slack (0.4); and
* a single integral nested routing under the standalone capacities (0.5).

Conditionally, if the projected cycle multiplicities and the chosen high
sets satisfy (4.6) and (0.8), then the same omitted set passes transition
two.  Analogous residual inequalities would still have to be proved at all
later transitions.

Thus the Section 22 theorem does not yet yield
\(\mathsf{MR}_A(m)=o(W)\).  The new all-depth estimate proves that omitted
owners themselves have enough Boolean-shadow capacity; the precise missing
information is whether the frozen cyclic packet leaves that capacity in the
right fibres.  The first place this information is absent is the exact
rank-two system (0.7)--(0.8).
