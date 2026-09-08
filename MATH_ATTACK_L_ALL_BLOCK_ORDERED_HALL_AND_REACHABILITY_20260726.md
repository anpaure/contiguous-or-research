# The all-block factor under metric Ordered-Hall: zero shadow deficiency and persistent full-support reachability cycles

Date: 2026-07-26

Method: pure hand mathematics only. No computation, finite search, solver,
or web input is used.

Audit: three independent adversarial checks re-derived (i) the
Catalan-shadow/private-owner injection and exact forced-pair ledger,
(ii) the full-clean interaction indegree, cycle peeling, explicit
\(C_{s-2}\) cylinder, and Ordered-Hall pruning, and (iii) the
phase-zero leaf cut, octahedral quota cube, and bounded-edit estimates.
All scope corrections from those checks are incorporated below.

## 0. Exact verdict

Let \(s\ge 1\), put

\[
 J=[2s],\qquad
 \mathcal X=\binom Js,\qquad
 \mathcal Y=\binom J{s+1},\qquad
 \mathcal D=\mathcal D_s,\qquad N=C_s,
\]

and let \(G_s\) be the all-block factor from
MATH_ATTACK_N_BLOCK_ASSOCIATOR_RECURSION_AND_SHARP_CORE_20260726.md.
There are two distinct meanings of its “first matching.”

1. Its root-first quota table prescribes only \(P-Y_0(P)\), or sometimes
   the two-edge prefix \(P-Y_0(P)-X_1(P)\), for
   \(P\in\mathcal D\). This datum alone does not define the complete clean
   graph \(H_a\), its private-owner function, or a Catalan-shadow
   deficiency.
2. The explicitly completed factor \(G_s\) supplies an entire upward
   matching
   \[
      \alpha_s:\mathcal X\setminus\overline{\mathcal D}
           \longrightarrow\mathcal Y
   \]
   and an entire down matching
   \[
      \beta_s:\mathcal X\setminus\overline{\mathcal D}
           \longrightarrow\mathcal X\setminus\mathcal D.
   \]
   This is the balanced prescribed-first object to which metric
   Ordered-Hall applies.

For the second, mathematically defined object, this note proves:

1. The exact Catalan-shadow/private-owner deficiency is
   \[
                         \boxed{\delta(H_{\alpha_s})=0.}
   \]
   There is no Hall-deficient family to repair. The root-only prescribed
   layer also has zero extension deficiency because the remaining upward
   edges of \(G_s\) give its extension explicitly.
2. The sharp \(a_{s-1}\sim C_s/9\) top/\(2s\) quota cell has
   private-owner count zero. The saturated pair family carrying the
   forced lower-rank recursion has positive Hall slack
   \[
                \frac{s-1}{2}C_s
                   \sim \frac{4^s}{2\sqrt{\pi s}}.
   \]
   Thus the \(1/9\) core is not an ordinary Hall obstruction.
3. On the **full clean allowed support** of every exact \(s\)-path factor,
   not merely \(G_s\), the strand-interaction multidigraph has exact
   indegree \((s-1)^2\) at every root and exactly
   \((s-1)^2C_s\) alternative arcs. It contains at least
   \((s-1)^2\) edge-disjoint directed interaction cycles.
   Therefore full clean reachability is never triangular when \(s\ge2\).
4. For the all-block factor there is a stronger, Catalan-scale witness:
   \(C_{s-2}\) vertex-disjoint root pairs carry directed reachability in
   both directions. Hence at least
   \[
      C_{s-2}
       =\left(\frac1{16}+o(1)\right)C_s
   \]
   distinct cross exits must be deleted (equivalently, every one of the
   \(C_{s-2}\) disjoint pair gadgets must be touched) to destroy these
   displayed two-cycles while retaining the selected factor.
5. This reachability failure does **not** obstruct completion. Restricting
   the allowed support to the explicit arcs \(x\mapsto\beta_s(x)\) gives
   a perfect successor matching, diagonal reachability, and metric defect
   zero. Metric Ordered-Hall then recovers the literal factor.
6. For every \(s\ge3\), there is an exact octahedral \(C_8\) Boolean
   cube of dimension \(C_{s-2}\) whose every state retains the hard cap
   \(a_{s-1}\) exactly. These switches have identity endpoint action.
   Conversely, no bounded or unbounded family of reroutings can make the
   **full clean support** triangular while ending in an exact factor,
   because the universal interaction theorem reapplies.

Consequently there is no persistent Hall cut for the explicit completed
all-block matching. The persistent obstruction is only to the
full-support triangular-reachability sufficient certificate. It is a
certificate obstruction, not a literal-completion obstruction.

No coefficient-one conclusion follows: the remaining issue is not local
completion of \(G_s\), which is already exact, but incorporating completed
root-scale packets into the growing common quota/vertical construction.

## 1. The complete matching extracted from \(G_s\)

Put

\[
 L=\mathcal X\setminus\overline{\mathcal D},\qquad
 R=\mathcal X\setminus\mathcal D,\qquad
 I=\mathcal X\setminus
     (\mathcal D\cup\overline{\mathcal D}).             \tag{1.1}
\]

The exact counts are

\[
 |L|=|R|=|\mathcal Y|=sC_s,\qquad |I|=(s-1)C_s.        \tag{1.2}
\]

Write a row of \(G_s\) as

\[
 P=X_0(P)\subset Y_0(P)\supset X_1(P)\subset\cdots
 \subset Y_{s-1}(P)\supset X_s(P)=\overline P.         \tag{1.3}
\]

Because the factor owns every lower and upper state exactly once, define

\[
 \alpha_s(X_t(P))=Y_t(P),\qquad
 \beta_s(X_t(P))=X_{t+1}(P)\quad(0\le t<s).            \tag{1.4}
\]

Then \(\alpha_s:L\to\mathcal Y\) and \(\beta_s:L\to R\) are bijections,
and

\[
 X_t(P)\subset\alpha_s(X_t(P))\supset
                   \beta_s(X_t(P)).                    \tag{1.5}
\]

The two lower states in (1.5) are distinct; otherwise the factor would
traverse one incidence twice. Thus \(\beta_s(x)\) is an allowed exit in
the full clean graph \(H_{\alpha_s}\).

Let \(\alpha_0,\beta_0\) denote the corresponding matchings of the
canonical factor \(F_s\), and put

\[
 \eta_s=(2\ 3)(4\ 5)\cdots(2s-2\ 2s-1).              \tag{1.6}
\]

The definition \(G_s(P)=\eta_sF_s(\eta_sP)\) gives, on every state and
not only at the root,

\[
\boxed{
 \alpha_s(x)=\eta_s\alpha_0(\eta_sx),\qquad
 \beta_s(x)=\eta_s\beta_0(\eta_sx).}                  \tag{1.7}
\]

The involution \(\eta_s\) preserves \(\mathcal D\), its complement, and
incidence. Hence it is an isomorphism

\[
                         H_{\alpha_0}\cong H_{\alpha_s}. \tag{1.8}
\]

In particular Hall deficiency and unrestricted reachability of the
complete upward matching are coordinate-conjugacy invariants. The new
\(1/9\) quota profile comes from how physical roots and first targets are
labelled; it cannot create a new ordinary degree-Hall deficit.

### Root-only scope

Let \(E_s=\{Y_0(P):P\in\mathcal D\}\). Exact upper ownership makes this an
\(N\)-set. The internal upward edges in (1.3) match

\[
 I\longrightarrow\mathcal Y\setminus E_s.             \tag{1.9}
\]

Therefore the root-first residual \(Y\)-resource Hall deficiency is zero.
Conversely, the quota matrix (0.5)--(0.6) in the Lane N report, if detached
from the explicit states (1.3), does not specify a unique set \(E_s\) or a
unique internal matching and cannot by itself be assigned a
Catalan-shadow deficiency.

## 2. Exact Catalan-shadow deficiency

For \(U\subseteq\mathcal Y\), put

\[
\begin{aligned}
 \partial^-U&=\{z\in\mathcal X:z\subset Y
                         \text{ for some }Y\in U\},\\
 d_U(z)&=|\{Y\in U:z\subset Y\}|,\\
 \pi_{\alpha_s}(U)
  &=|\{z\in I:\alpha_s(z)\in U,\ d_U(z)=1\}|,\\
 q_{\mathcal D}(U)
  &=|\partial^-U\setminus\mathcal D|-|U|.             \tag{2.1}
\end{aligned}
\]

Thus \(q_{\mathcal D}\) is the non-Dyck lower-shadow surplus denoted
\(s_{\mathcal D}\) in the preceding Ordered-Hall report. The exact clean
deficiency formula is

\[
 \delta(H_{\alpha_s})=\max_{U\subseteq\mathcal Y}
       (\pi_{\alpha_s}(U)-q_{\mathcal D}(U))_+.         \tag{2.2}
\]

### Theorem 2.1 (zero deficiency, with an explicit shadow injection)

For every \(s\ge1\) and every \(U\subseteq\mathcal Y\),

\[
\boxed{
              \pi_{\alpha_s}(U)\le q_{\mathcal D}(U).} \tag{2.3}
\]

Moreover equality in the maximum in (2.2) is attained at
\(U=\mathcal Y\). Consequently

\[
                         \boxed{\delta(H_{\alpha_s})=0.} \tag{2.4}
\]

#### Proof

Let \(S=\alpha_s^{-1}(U)\), and use the specified down matching to form

\[
                         M(U)=\beta_s(S).               \tag{2.5}
\]

Since both matchings are bijections,

\[
 |M(U)|=|S|=|U|,\qquad
 M(U)\subseteq\partial^-U\setminus\mathcal D.          \tag{2.6}
\]

Let

\[
 B(U)=\{z\in I:\alpha_s(z)\in U,\ d_U(z)=1\},          \tag{2.7}
\]

so \(|B(U)|=\pi_{\alpha_s}(U)\). We claim
\(M(U)\cap B(U)=\varnothing\). If \(z=\beta_s(x)\) lay in the
intersection, then both \(\alpha_s(x)\in U\) and
\(\alpha_s(z)\in U\) would contain \(z\). The condition \(d_U(z)=1\)
would force

\[
                         \alpha_s(x)=\alpha_s(z).
\]

Injectivity of \(\alpha_s\) would give \(x=z\), and then
\(\beta_s(z)=z\), contradicting the no-backtrack condition in (1.5).
Thus the two families in (2.6)--(2.7) are disjoint, and

\[
 |\partial^-U\setminus\mathcal D|
   \ge |M(U)|+|B(U)|=|U|+\pi_{\alpha_s}(U).            \tag{2.8}
\]

This is (2.3). For \(U=\mathcal Y\), its non-Dyck shadow is exactly \(R\),
so \(q_{\mathcal D}(U)=|R|-|\mathcal Y|=0\). If \(s\ge2\), every
internal \(z\) has \(d_U(z)=s>1\), while \(I=\varnothing\) at \(s=1\);
hence \(\pi_{\alpha_s}(U)=0\). The maximum in (2.2) is exactly zero.
\(\square\)

The full clean graph has the exact edge ledger

\[
 |E(H_{\alpha_s})|
  =(s-1)|I|+s|\overline{\mathcal D}|
  =(s^2-s+1)C_s.                                      \tag{2.9}
\]

Thus its shores have order

\[
 sC_s\sim\frac{4^s}{\sqrt{\pi s}},                    \tag{2.10}
\]

and its edge set has order

\[
 (s^2-s+1)C_s\sim\frac{4^s\sqrt s}{\sqrt\pi},         \tag{2.11}
\]

but its matching deficiency remains identically zero, not merely
\(o(C_s)\).

## 3. The \(1/9\) core has positive Hall slack

The all-block atom count satisfies

\[
 a_{s-1}\sim\frac19C_s.                               \tag{3.1}
\]

These \(a_{s-1}\) rows lie in the top first-return fibre and insert \(2s\)
first. Their first upper states are

\[
                         Y_P=P\cup\{2s\}.             \tag{3.2}
\]

Every owner in (3.2) is the root \(P\in\mathcal D\), whereas the private
count in (2.1) charges only internal owners. Therefore, for any subfamily
\(U\) of these first uppers,

\[
                         \pi_{\alpha_s}(U)=0.           \tag{3.3}
\]

The map \(Y\mapsto Y\setminus\{1\}\) also injects such a family into
\(\partial^-U\setminus\mathcal D\), since every Dyck root contains \(1\)
and every displayed \(Y\) contains \(2s\). Hence (3.2) cannot furnish a
positive Hall deficiency.

Put

\[
 U_*=\{Y\in\mathcal Y:\{1,2s\}\subseteq Y\}.           \tag{3.4}
\]

### Proposition 3.1 (forced-pair shadow ledger)

For \(G_s\), and more generally for every exact
\(\mathcal D_s\)-port complement-path factor \(F\) with complete upward
matching \(\alpha_F\),

\[
\boxed{
 |U_*|=sC_{s-1},\qquad
 \pi_{\alpha_F}(U_*)=0,\qquad
 q_{\mathcal D}(U_*)=\frac{s-1}{2}C_s.}               \tag{3.5}
\]

In particular

\[
 q_{\mathcal D}(U_*)
    \sim\frac{4^s}{2\sqrt{\pi s}}.                    \tag{3.6}
\]

#### Proof

Choose the other \(s-1\) coordinates of \(Y\in U_*\) from
\([2,2s-1]\), giving

\[
 |U_*|=\binom{2s-2}{s-1}=sC_{s-1}.                    \tag{3.7}
\]

An \(s\)-set in \(\partial^-U_*\) contains either both of \(1,2s\), or
exactly one. These two classes have sizes

\[
 \binom{2s-2}{s-2}=(s-1)C_{s-1},\qquad
 2\binom{2s-2}{s-1}=2sC_{s-1}.                        \tag{3.8}
\]

Every Dyck root contains \(1\) and omits \(2s\), so every member of
\(\mathcal D\) lies in the second class. Hence

\[
\begin{aligned}
 q_{\mathcal D}(U_*)
  &=(3s-1)C_{s-1}-C_s-sC_{s-1}\\
  &=(2s-1)C_{s-1}-C_s
   =\frac{s-1}{2}C_s,                                  \tag{3.9}
\end{aligned}
\]

using \(C_s/C_{s-1}=2(2s-1)/(s+1)\).

The forced-core theorem says that the upper states \(U_*\) are exhausted
by the \(C_{s-1}\) rows which insert \(2s\) first and delete \(1\) last.
At phase zero the owner is a root, so it is not charged by \(\pi\). At
every later source phase the owner contains both \(1\) and \(2s\), and
hence has \(d_{U_*}(z)=s>1\) when \(s\ge2\). Thus no internal owner is
private and \(\pi_{\alpha_F}(U_*)=0\). The case \(s=1\) is immediate.
Finally (3.6) follows from
\(C_s\sim4^s/(\sqrt\pi s^{3/2})\). \(\square\)

The recursive lower-rank port condition carried by \(U_*\) is therefore
strictly beyond ordinary scalar Hall: it lives behind positive Hall slack
of order \(4^s/\sqrt s\).

## 4. Full-clean triangular reachability: a universal obstruction

The preceding Hall theorem does not imply that the *full* clean allowed
digraph has unique diagonal reachability. In fact that stronger condition
is impossible for every exact factor once \(s\ge2\).

Let \(F\) be any exact \(\mathcal D_s\)-port factor, with paths

\[
 X_0(P),X_1(P),\ldots,X_s(P),\qquad
 X_0(P)=P,\quad X_s(P)=\overline P,                    \tag{4.1}
\]

and put \(Y_i(P)=X_i(P)\cup X_{i+1}(P)\). Extract its upward and down
matchings

\[
 \alpha(X_i(P))=Y_i(P),\qquad
 \beta(X_i(P))=X_{i+1}(P).                            \tag{4.2}
\]

Every path in (4.1) is a Johnson geodesic: its endpoints have distance
\(s\), and it has exactly \(s\) Johnson arcs.

### Definition 4.1 (strand-interaction multidigraph)

Form a directed multigraph \(\Gamma_F\) on \(\mathcal D\). For every
full-clean allowed exit

\[
                         x\longrightarrow z
                         \quad\text{with }z\ne\beta(x),             \tag{4.3}
\]

put one labelled arc \(P\to Q\) in \(\Gamma_F\) when \(x\) lies on the
path rooted at \(P\) and \(z\) lies on the path rooted at \(Q\).

### Lemma 4.2 (every alternative exit changes strand)

The multidigraph \(\Gamma_F\) has no loop.

#### Proof

Suppose \(x=X_i(P)\) and \(z=X_j(P)\) lie on the same path and form an
allowed exit. Since they are distinct \(s\)-subsets of one
\((s+1)\)-set, they are Johnson adjacent. Geodesicity gives

\[
                         |i-j|=d_J(X_i(P),X_j(P))=1.   \tag{4.4}
\]

If \(j=i+1\), then \(z=\beta(x)\), contrary to (4.3). If \(j=i-1\), then
both \(X_{i-1}(P)\) and \(X_{i+1}(P)\) would be facets of
\(\alpha(X_i(P))=Y_i(P)\). They would therefore be Johnson adjacent,
whereas their geodesic distance along (4.1) is two. This is impossible.
\(\square\)

### Theorem 4.3 (exact interaction indegree and persistent cycles)

For every \(s\ge2\) and every exact factor \(F\), every vertex of
\(\Gamma_F\) has indegree exactly

\[
                              d_s=(s-1)^2.             \tag{4.5}
\]

Consequently

\[
                         |E(\Gamma_F)|=(s-1)^2C_s,     \tag{4.6}
\]

and \(\Gamma_F\) contains at least \((s-1)^2\) pairwise edge-disjoint
directed cycles.

#### Proof

Fix the path rooted at \(Q\). Its \(s-1\) internal target states
\(X_1(Q),\ldots,X_{s-1}(Q)\) lie in \(I\). In the full clean graph, every
internal target has column indegree \(s-1\): it has \(s\) upper supersets,
but its owner/backtrack incidence is deleted. Exactly one remaining
incoming edge is its selected predecessor from (4.2), leaving \(s-2\)
alternative incoming exits.

The terminal \(X_s(Q)=\overline Q\) has no owner and has column indegree
\(s\). Removing its selected predecessor leaves \(s-1\) alternatives.
Lemma 4.2 says that every alternative comes from another strand. Therefore

\[
 d^-_{\Gamma_F}(Q)
   =(s-1)(s-2)+(s-1)=(s-1)^2.                         \tag{4.7}
\]

Summing proves (4.6).

Any finite directed multigraph of minimum indegree at least one contains
a simple directed cycle: repeatedly follow an incoming arc, use finiteness,
and retain the segment between the first repeated vertex.
Remove the arcs of one such simple cycle. Every vertex on it loses one incoming
arc, so the remaining minimum indegree is at least \(d_s-1\). Iterating
proves the existence of \(d_s\) edge-disjoint directed cycles.
\(\square\)

### Corollary 4.4 (full clean reachability is never triangular)

Let \(K_\alpha\) be the off-diagonal root reachability digraph of the full
clean contracted support:

\[
 P\longrightarrow Q
 \quad\Longleftrightarrow\quad
 P\leadsto\overline Q,\quad P\ne Q.                   \tag{4.8}
\]

For every exact factor and every \(s\ge2\), \(K_\alpha\) contains a
directed cycle. Hence the full root-to-complement reachability graph has a
non-diagonal perfect matching and is not triangular in any root order. In
particular, it admits no weakly edge-monotone potential whose paired-port
values are all distinct (and therefore no order-valued potential of the
form required by the monotone Ordered-Hall certificate): there is no
\(\Phi:\mathcal X\to\mathbb R\) with
\(\Phi(P)=\Phi(\overline P)\), with these common values distinct for
distinct \(P\)'s, and with \(\Phi(x)\le\Phi(z)\) on every allowed arc
\(x\to z\).

#### Proof

An interaction arc \(P\to Q\) is witnessed by a source state \(x\) on the
selected \(P\)-path and a target state \(z\) on the selected \(Q\)-path.
Follow the selected path from \(P\) to \(x\), take the allowed alternative
arc \(x\to z\), and then follow the selected suffix from \(z\) to
\(\overline Q\). Thus every arc of \(\Gamma_F\) is an arc of \(K_\alpha\).

A directed cycle in \(\Gamma_F\) is therefore a directed cycle in
\(K_\alpha\). Cyclically shifting the diagonal root--sink matching on its
vertices gives a second perfect matching of the reachability graph. The
equivalence between absence of such cycles and triangular reachability
gives the first assertions. Along a reachability cycle, edge monotonicity
would force the paired-port values successively to be nondecreasing and
then return to the first, hence all equal, contradicting their required
distinctness. \(\square\)

The \((s-1)^2\) cycles in Theorem 4.3 are edge-disjoint in the labelled
interaction multigraph. Their images need not remain distinct after
parallel root-pair witnesses are collapsed in \(K_\alpha\). Nevertheless,
if \(\tau_{\rm alt}(F)\) denotes the minimum number of physical
alternative arcs which must be removed, while every selected
\(\beta\)-arc is retained, to make \(\Gamma_F\) acyclic, then

\[
                              \tau_{\rm alt}(F)\ge(s-1)^2.         \tag{4.9}
\]

This obstruction is structural. Coordinate conjugation, a \(C_6/C_8\)
rerouting, or any other operation ending in an exact port factor produces
a new factor to which Theorem 4.3 applies again.

## 5. A Catalan-scale all-block reachability cylinder

The all-block factor has a much larger explicit obstruction than (4.9).
We first record the canonical concatenation identity used to expose it.

### Lemma 5.1 (MSW right-context concatenation)

Let \(\rho(W)\) be the canonical MSW flip word of a Dyck word \(W\), with
each pair recording the inserted and then deleted coordinate. For Dyck
words \(U,V\),

\[
 \rho(UV)=\rho(U)\mathbin{\Vert}(|U|+\rho(V)).          \tag{5.1}
\]

Equivalently, the canonical row first processes \(U\) with \(V\) fixed,
reaches \(\overline U\,V\), and then processes \(V\) with
\(\overline U\) fixed, ending at \(\overline U\,\overline V\).

#### Proof

Use the exact defining recursion

\[
 \rho(1u0v)=
 \bigl(c,\ c-\rho(\mu(u)),\ 1,\ c+\rho(v)\bigr),
 \qquad c=|u|+2,                                     \tag{5.1a}
\]

where \(\mu\) is reverse-complement and scalar addition/subtraction is
entrywise. If \(U=1u0v\), apply (5.1a) first to
\(1u0(vV)\), and then apply it to \(vV\). Induction on semilength gives

\[
 \rho(vV)=\rho(v)\mathbin{\Vert}(|v|+\rho(V)).
\]

The offset in the second block is \(c+|v|=|U|\), which yields (5.1).
The path statement is the same identity translated from flip coordinates
to successive states. \(\square\)

Put

\[
                         A=1100,\qquad C=1010.          \tag{5.2}
\]

Their exact canonical local rows are

\[
\begin{aligned}
 A&\subset1101\supset1001\subset1011\supset0011=\overline A,\\
 C&\subset1110\supset0110\subset0111\supset0101=\overline C.
                                                               \tag{5.3}
\end{aligned}
\]

### Proposition 5.2 (a \(C_{s-2}\)-cylinder of disjoint two-cycles)

For \(s\ge2\) and \(B\in\mathcal D_{s-2}\) (with the empty word allowed
when \(s=2\)), put

\[
 P_B=\eta_s(AB),\qquad Q_B=\eta_s(CB).                 \tag{5.4}
\]

Then \(P_B,Q_B\in\mathcal D_s\), and the full clean root reachability
digraph of \(G_s\) contains

\[
                         P_B\longrightarrow Q_B,\qquad
                         Q_B\longrightarrow P_B.       \tag{5.5}
\]

The pairs in (5.4) are vertex-disjoint as \(B\) varies. Hence the
construction displays \(C_{s-2}\) vertex-disjoint directed two-cycles.

#### Proof

By (5.1)--(5.3), the canonical complete upward owners include

\[
\begin{aligned}
 \alpha_0(AB)&=1101B,\\
 \alpha_0(CB)&=1110B,\\
 \alpha_0(0110B)&=0111B.                              \tag{5.6}
\end{aligned}
\]

The full clean support therefore contains the literal paths

\[
\begin{aligned}
 AB&\longrightarrow0101B=\overline C\,B
      \leadsto\overline C\,\overline B
       =\overline{CB},\\
 CB&\longrightarrow0110B\longrightarrow0011B=\overline A\,B
      \leadsto\overline A\,\overline B
       =\overline{AB}.                                \tag{5.7}
\end{aligned}
\]

In the first line, the cross exit deletes the first coordinate from
\(1101B\). In the second, \(CB\to0110B\) is the selected first exit, and
the cross exit from owner \(0111B\) deletes its second coordinate.
Every displayed target is distinct from its source. All noninitial lower
states shown begin with \(0\), so none is a forbidden Dyck target; the
remaining tail arcs are selected canonical arcs. Thus (5.7) lies in the
full clean support.

Conjugacy (1.7) maps (5.7) into the full clean support of \(G_s\), and
\(\eta_s\) commutes with complement. This proves (5.5). If \(B\ne B'\),
the four roots \(AB,CB,AB',CB'\) are distinct because the prefixes
\(A,C\) differ and the suffix is recoverable. Bijectivity of \(\eta_s\)
preserves distinctness. \(\square\)

The witness packets for distinct \(B\)'s lie on distinct canonical rows,
and exact ownership makes their selected \(X/Y\)-states disjoint. To kill
all displayed two-cycles while retaining the selected matching, at least
one of the two cross exits in (5.7) must be removed for every \(B\).
Therefore every such triangular pruning deletes at least

\[
                              C_{s-2}                 \tag{5.8}
\]

alternative edges. The exact density is

\[
 \frac{C_{s-2}}{C_s}
   =\frac{s(s+1)}{4(2s-1)(2s-3)}
      \longrightarrow\frac1{16},                     \tag{5.9}
\]

and the affected-root density tends to \(1/8\). This is a Catalan-scale
full-support reachability obstruction, not a finite boundary anomaly.

## 6. Correct and nontrivial applications of metric Ordered-Hall

On the full clean support, ordinary Hall holds by Theorem 2.1 but the
unique-reachability hypothesis fails by Corollary 4.4 and Proposition 5.2.
Thus the full-support sufficient theorem cannot be invoked.

### 6.1 The selected zero-defect support

The all-block factor explicitly supplies the allowed sub-support

\[
 H_s^\circ=\{x\to\beta_s(x):x\in L\}.                 \tag{6.1}
\]

This is a perfect successor matching. Its only directed components are
the displayed paths (1.3), so its root-to-complement reachability graph is
exactly diagonal. Furthermore

\[
 |\mathcal X|-C_s=sC_s
   =\sum_{P\in\mathcal D}d_J(P,\overline P).           \tag{6.2}
\]

Hence the metric Ordered-Hall defect is

\[
                              \Delta=0.                \tag{6.3}
\]

Metric Ordered-Hall recovers \(C_s\) cycle-free length-\(s\) Johnson
geodesics. The omitted-coordinate reconstruction then makes every
component a literal cyclic-window wreath.

This restriction is legitimate here because \(\beta_s\) is not an
existential object inferred from Hall: the Lane N construction specifies
the whole conjugated canonical tail. For a merely proposed root quota
table with no completed tail, replacing the allowed graph by unknown
singleton exits would be circular.

### 6.2 A large monotone safe pruning

The singleton support (6.1) is not the only available Ordered-Hall
certificate. Fix any total order \(\prec\) of the roots. Retain:

1. every selected arc \(x\to\beta_s(x)\); and
2. an alternative arc from strand \(P\) to strand \(Q\) exactly when
   \(P\prec Q\).

Call the resulting support \(H^\prec\).

### Theorem 6.1 (forward-interaction pruning)

The support \(H^\prec\) satisfies Hall, has triangular root reachability,
and has metric defect zero. Consequently every perfect successor matching
in \(H^\prec\) is a literal \(\mathcal D_s\)-port factor.

Moreover one of an arbitrary order and its reverse retains at least

\[
                  \frac12(s-1)^2C_s                  \tag{6.4}
\]

labelled physical alternative arcs.

#### Proof

The selected matching \(\beta_s\) remains, so Hall holds. Equivalently,
if \(\operatorname{rk}_\prec(P)\) is the rank of strand \(P\), then

\[
 \Phi(X_i(P))=\operatorname{rk}_\prec(P)              \tag{6.4a}
\]

is constant on selected arcs and strictly increases on every retained
alternative arc. Suppress every
maximal selected within-strand segment of a directed path in \(H^\prec\).
Each remaining transition is an alternative interaction arc and strictly
increases the root order. Thus a path from \(P\) to \(\overline Q\) implies
\(P\preceq Q\); diagonal paths are supplied by \(\beta_s\). Root
reachability is triangular.

The vertex count and endpoint distances are unchanged from (6.2), so
metric defect is zero. Metric Ordered-Hall proves the literal conclusion.

Lemma 4.2 says there is no alternative loop. Therefore every alternative
arc is forward in exactly one of \(\prec\) and its reverse. Their retained
counts sum to the total \((s-1)^2C_s\) in (4.6), proving (6.4).
\(\square\)

The perfect-matching fibre of \(H^\prec\) is connected by ordinary
alternating-cycle flips: the symmetric difference of two bipartite perfect
matchings is a disjoint union of alternating cycles. Every intermediate
matching remains monodromy-safe by Theorem 6.1. This does not assert that
there is a second perfect matching beyond \(\beta_s\); it supplies a large
safe arena in which any such alternatives may be used.

Thus the exact support ledger is

\[
\begin{array}{c|c|c}
\text{support}&\text{degree Hall}&\text{diagonal reachability}\\ \hline
\text{full clean }H_{\alpha_s}&\text{yes, deficiency }0&
                       \text{no for every }s\ge2\\
\text{selected }H_s^\circ&\text{yes, a perfect matching}&
                       \text{yes, exactly diagonal}\\
\text{forward-pruned }H^\prec&\text{yes via }\beta_s&
                       \text{yes, triangular}.
\end{array}                                             \tag{6.5}
\]

The first-row failure is a failure of a strong sufficient certificate,
not a failure of literal completion.

## 7. What \(C_6/C_8\) reroutings can and cannot do

Propositions 7.1--7.4 concern elementary alternating \(C_6/C_8\)
factor-to-factor switches whose endpoint is another exact anchored factor
\(F'\). Proposition 7.5 separately treats first-matching exchanges and
strand-admissible switches through root-to-sink path covers; correct
complement monodromy is not assumed there until the target state.

### Proposition 7.1 (Hall and full-reach ledgers after rerouting)

For every such \(F'\):

1. its complete upward matching has Catalan-shadow deficiency zero;
2. its full clean interaction multidigraph has indegree \((s-1)^2\) at
   every root and hence cyclic reachability for \(s\ge2\).

#### Proof

The down matching of \(F'\) witnesses Hall exactly as in Theorem 2.1.
Theorem 4.3 applies to every exact factor, independently of how it was
obtained. \(\square\)

Thus, within the exact-factor fibre, there is no ordinary Hall defect to
repair and no rerouting can lower the already-zero deficiency. No bounded
or unbounded collection of reroutings can make the full clean support
triangular while retaining an exact factor.

For an exact factor \(F\), write \(\operatorname{fr}(P)\) for the
first-return class of its root and define its fibre-resolved first quota by

\[
 Q_F(j,\ell)=
 \#\{P\in\mathcal D_s:\operatorname{fr}(P)=j,
                  \ Y_0^F(P)\setminus P=\{\ell\}\}.  \tag{7.0}
\]

### Proposition 7.2 (generic quota stability)

Assume \(s\ge3\). If every elementary switch avoids the current
root-incident factor edge at every stage, then the entire first-insertion
quota matrix of the all-block factor is unchanged.
In particular its maximum remains exactly \(a_{s-1}\).

More generally, let \(B\) be the number of elementary cycle toggles (so a
macro-packet is counted by its constituent cycles). A \(C_6\) can change
the incident factor edge at at most three roots, and a \(C_8\) at at most
four. Hence at most \(4B\) root rows change first-insertion cells, and

\[
                         |Q_{F'}(j,x)-Q_{G_s}(j,x)|\le4B           \tag{7.1}
\]

for every source-fibre/target cell. Consequently

\[
 \max_{j,x}Q_{F'}(j,x)\le a_{s-1}+4B.                 \tag{7.2}
\]

For fixed \(B\) (and, by the same proof, for \(B=o(C_s)\)),

\[
 \frac{\max_{j,x}Q_{F'}(j,x)}{C_s}
       \le\frac19+o(1).                                \tag{7.3}
\]

#### Proof

The first inserted coordinate in a rooted row is determined by its unique
root-incident upper edge. If that edge is protected, arbitrary interior
reassembly changes no first-insertion datum.

An alternating \(C_{2k}\) removes \(k\) selected cycle edges and inserts
the other \(k\). Only roots incident with the changed boundary can acquire
a different degree-one edge, so it changes at most \(k\le4\) root rows.
After \(B\) switches, at most \(4B\) rows have moved between quota cells,
which gives (7.1)--(7.2). Equation (7.3) follows from
\(a_{s-1}/C_s\to1/9\). \(\square\)

For retaining the **exact** hard cap \(a_{s-1}\), one must additionally
forbid net inflow into a cell already of that size. Interior root-protected
switches satisfy this automatically. If retaining the \(1/9\) cap means
its sharp asymptotic constant, every fixed number of switches satisfies it.

### Proposition 7.3 (the phase-zero \(2s\)-leaf cut)

For every root \(P\in\mathcal D\), put

\[
                         Y_P=P\cup\{2s\}.             \tag{7.4}
\]

In the root-to-first-upper incidence graph, \(Y_P\) has the unique Dyck
neighbour \(P\). Consequently its edge \(P-Y_P\) belongs to no alternating
cycle. Every reconfiguration of the root first matching by phase-zero
alternating cycles, of any length, fixes pointwise

\[
                         \mathcal S_{2s}
   =\{P:\text{the first inserted coordinate is }2s\}. \tag{7.5}
\]

In particular it fixes the all-block top/\(2s\) cell of size
\(a_{s-1}\).

#### Proof

Every \(s\)-facet of \(Y_P\) other than
\(P=Y_P\setminus\{2s\}\) contains coordinate \(2s\). Every Dyck root omits
\(2s\). Hence \(P\) is the unique Dyck facet of \(Y_P\), proving the
degree-one claim. An edge incident with a degree-one upper vertex cannot
lie on an alternating cycle. \(\square\)

The scope is exact: a cross-phase incidence cycle may use a root edge and
internal lower owners, so Proposition 7.3 is a no-go for
phase-homogeneous root-layer rerouting, not for every conceivable
cross-phase router.

### Proposition 7.4 (an exact cap-preserving octahedral \(C_8\) cube)

Assume \(s\ge3\). For every \(R\in\mathcal D_{s-2}\), put

\[
 x_R=1100R,\qquad y_R=1010R,\qquad
 P_R=\eta_sx_R,\qquad Q_R=\eta_sy_R.                  \tag{7.6}
\]

Conjugate by \(\eta_s\) the canonical two-row/two-cut rectangle which
transposes the phase-one states on rows \(x_R,y_R\). For every subfamily
\(\mathcal R\subseteq\mathcal D_{s-2}\), the product of these pairwise
disjoint rectangles is an exact anchored factor. The cube has dimension
\(C_{s-2}\), acts on \(2C_{s-2}\) roots, and every one of its states
satisfies

\[
                  \boxed{\max_{j,\ell}Q_F(j,\ell)=a_{s-1}.}       \tag{7.7}
\]

#### Proof

Before conjugation, the first three canonical states are, after
suppressing the common shifted support of \(R\),

\[
 x_R:(12,14,34),\qquad y_R:(13,23,24).                \tag{7.8}
\]

The octahedral rectangle replaces them by

\[
 x_R:(12,23,34),\qquad y_R:(13,14,24).                \tag{7.9}
\]

It preserves the four upper colours \(123,124,134,234\), returns to the
identity phase after the second cut, and therefore has identity endpoint
action. Distinct suffixes \(R\) give disjoint root pairs and disjoint old
colour supports, so any subfamily switches simultaneously. Coordinate
conjugacy preserves all ledgers and endpoints.

For the physical first targets after conjugation, (7.8)--(7.9) give

\[
\begin{array}{c|c}
P_R&5\longrightarrow2\\
Q_R&3\longrightarrow5.
\end{array}                                           \tag{7.10}
\]

Indeed the \(x_R\)-row changes its inserted coordinate from \(4\) to \(3\)
before applying \(\eta_s\), and the \(y_R\)-row changes it from \(2\) to
\(4\); \(\eta_s(4)=5,\eta_s(3)=2,\eta_s(2)=3\).

The root \(P_R\) has first-return class one. Write the first-return class of
\(Q_R\) as \(j_R\); the all-block atom grammar gives \(j_R\ge3\), with
the exact distribution

\[
 \#\{R:j_R=j\}=
 \begin{cases}
 C_{j-3}C_{s-j},&3\le j\le s-1,\\
 C_{s-3},&j=s.
 \end{cases}                                          \tag{7.11}
\]

Here is the coefficient derivation. In the one-flaw middle-word grammar,
\(\eta_sQ_R=1010R\). Since \(R=1E_R0\), the first two middle blocks of
\(1010R\) are \(01,01\), and its remaining middle blocks encode
\(E_R\). The all-block involution exchanges singleton signs and
bijects the remaining atom suffix. Hence the atom word of \(Q_R\) begins
with two consecutive \(+\) singleton atoms, followed by an arbitrary
one-flaw atom word of total semilength \(s-3\). Its first \(-\) atom therefore cannot
occur before semilength position three. If it first occurs at position
\(j<s\), the atom word has the unique form

\[
 ++\,\underbrace{(\mathcal R\cup\{+\})^*}_{j-3}\,-\,
 \underbrace{(\mathcal R\cup\{+,-\})^*}_{s-j-1},      \tag{7.11a}
\]

where \(\mathcal R\) is the family of positive primitive atoms of
semilength at least two, \(C(z)=\sum_{n\ge0}C_nz^n\), and subscripts
denote total semilength. The two
starred coefficients are respectively \(C_{j-3}\) and \(C_{s-j}\).
If no \(-\) occurs, the suffix after the two initial \(+\)'s has
generating function
\((1-z-z(C(z)-1))^{-1}=C(z)\), and its coefficient is
\(C_{s-3}\). This proves (7.11). These values sum to \(C_{s-2}\) by the
Catalan convolution.

In the baseline all-block quota matrix, physical target \(2\) never
occurs. Physical target \(5\) corresponds to image-return class \(2\).
For every source class \(j\ge2\), its cell is

\[
 M^{(s)}_{j,2}=M^{(s)}_{2,j}=0,                       \tag{7.12}
\]

because the finite diagonal is zero and every off-diagonal entry contains
the factor \(a_1=0\). Thus every increment in (7.10) enters a previously
empty cell, of size at most \(C_{s-2}\). The injection

\[
                         C_{s-2}\le a_{s-1}            \tag{7.13}
\]

follows from the explicit injection \(W\mapsto1W0\) from
\(\mathcal D_{s-2}\) to the no-singleton Dyck words of semilength
\(s-1\). Every
other affected cell is decremented, while the top/\(2s\) cell remains
\(a_{s-1}\). Therefore the maximum after any subfamily is exactly
\(a_{s-1}\). \(\square\)

This is a positive-density exact reconfiguration family: its acted-on row
fraction tends to \(1/8\). It does not repair monodromy or Hall, because
each rectangle has relative phase matchings

\[
                         \sigma_0=\tau_R,\qquad
                         \sigma_1=\tau_R^{-1},          \tag{7.14}
\]

and hence identity total endpoint action.

### Proposition 7.5 (bounded-edit stability for a deficient proposal)

Let \(\alpha,\alpha'\) be balanced complete first matchings which differ
on a set \(T\subseteq L\) of owner rows, and construct both residual
graphs with the same full-clean allowed-incidence rule. Then

\[
\boxed{
 |\nu(H_\alpha)-\nu(H_{\alpha'})|\le|T|,\qquad
 |\delta(H_\alpha)-\delta(H_{\alpha'})|\le|T|,}        \tag{7.15}
\]

where \(\nu\) is maximum-matching size. Consequently a sequence of \(t\)
elementary, phase-preserving \(C_6/C_8\) exchanges of the complete upward
matching, each changing that matching on at most four owner rows, can
reduce an actual Hall deficiency by at most \(4t\).

Separately, suppose every intermediate state of a sequence of
strand-admissible \(C_6/C_8\) switches is a root-to-sink path cover. One
move meets at most four current rooted path components, so its relative
endpoint multiplier is supported on at most four roots. If \(\pi\) and
\(\pi'\) are the initial and desired endpoint permutations, respectively,
their Hamming distance is
\(|\operatorname{supp}(\pi^{-1}\pi')|\). Thus \(t\) moves cannot suffice when

\[
                         |\operatorname{supp}(\pi^{-1}\pi')|>4t. \tag{7.16}
\]

In particular, no uniformly bounded number of these moves can correct a
family of proposals whose Hall deficit or required relative monodromy
support tends to infinity.

#### Proof

The two residual exit graphs have identical row neighbourhoods on
\(L\setminus T\). Delete from a maximum matching of either graph the edges
incident with rows in \(T\); the remaining matching lies in the other
graph and loses at most \(|T|\) edges. This proves the first inequality,
and the second follows from \(\delta=|L|-\nu\).

For a phase-preserving alternating exchange of the complete upward
matching, a \(C_6\) or \(C_8\) changes at most three or four owner rows,
respectively. This proves the Hall consequence under the stated
hypothesis. A strand-admissible move cuts at most three or four current
rooted paths, so its relative endpoint multiplier has the same support
bound; equivalently, it changes the endpoint map on at most four root
arguments. The Hamming triangle inequality for successive endpoint maps
then proves (7.16).
\(\square\)

For the explicit all-block factor, (7.15) is only a stability statement:
its starting deficiency is zero. It becomes a persistent-cut theorem for
a different proposed first matching with deficit \(>4t\).

## 8. Proved boundary for coefficient one

The following conclusions are exact.

1. The complete all-block upward matching has zero \(Y\)-resource and zero
   second-matching Hall deficiency. No persistent Hall cut exists.
2. The \(a_{s-1}\sim C_s/9\) quota core has private-owner count zero, and
   the saturated forced-pair packet has positive Hall slack
   \((s-1)C_s/2\).
3. Full-clean triangular reachability is impossible for every exact factor
   at \(s\ge2\), with exact alternative indegree \((s-1)^2\), total
   alternative mass \((s-1)^2C_s\), and at least \((s-1)^2\)
   edge-disjoint interaction cycles.
4. The all-block factor has the sharper \(C_{s-2}\)-family of disjoint
   reachability two-cycles. Killing these while retaining the selected
   completion requires at least \(C_{s-2}\sim C_s/16\) alternative-edge
   deletions.
5. The selected conjugated canonical tail is a zero-defect diagonal
   Ordered-Hall support. A forward-interaction pruning retains at least
   half the alternative arcs while remaining triangular and Hall-feasible.
6. For \(s\ge3\), the octahedral \(C_8\) cube has dimension
   \(C_{s-2}\), acts on an asymptotic \(1/8\) of the roots, and retains the exact hard
   \(a_{s-1}\) cap, but has identity endpoint action.
7. Root-protected \(C_6/C_8\) reroutings retain the exact quota table;
   bounded root-touching reroutings retain the asymptotic \(1/9\) cap. No
   rerouting can make the full clean support triangular.

What remains unproved is a growing quota construction beyond the sharp
adjacent-block core, coupled across the required outer depths. The local
degree completion of \(G_s\) is already solved and is not that gate.

No coefficient-one theorem is claimed here.
